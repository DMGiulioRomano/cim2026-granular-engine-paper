#!/usr/bin/env python3
"""bench_cost.py — costo del rendering: numero di grani vs durata dell'uscita.

Sostiene la nota sul costo di calcolo in `sec:architettura`. Tre sweep sullo
stesso PGE pinnato che rende gli esempi del paper:

  A) durata fissa 10 s, densita' crescente  -> tempo vs numero di grani
  B) ~4000 grani costanti, durata crescente -> tempo vs durata a grani fissi
  C) densita' fissa, durata crescente       -> il caso d'uso (grani ∝ durata)

Poi fitta ai minimi quadrati il modello a due termini

    t = a * N_grani + b * D_secondi

e stampa i coefficienti, l'errore relativo e la densita' di pareggio fra i due
termini. Rendering NumPy **sequenziale** (`jobs=1`): il default della CLI e'
`--jobs auto`, ma sotto il migliaio di grani lo spawn del pool costa piu' di
quanto rende, e il claim del paper riguarda la scala, non il wall clock di una
macchina. I coefficienti nel paper vengono da una run su Apple M2 Max,
Python 3.11; su un'altra macchina cambiano i coefficienti, non la forma.

Uso:  make bench       (dalla radice del repo)
      python3.11 examples/bench_cost.py
Scrive `examples/bench_cost.json` con tutti i punti misurati.
"""
import os, sys, time, tempfile, json, statistics

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PGE = os.path.join(REPO, "raw", "PythonGranularEngine")
sys.path.insert(0, os.path.join(PGE, "src"))

import matplotlib; matplotlib.use("Agg")
from pge.engine.generator import Generator
from pge.rendering.rendering_engine import RenderingEngine
from pge.rendering.render_mode import MixRenderMode
from main import _build_renderer

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(PGE)
OUT = tempfile.mkdtemp(prefix="pgebench_")

YAML = """composition:
  title: bench
streams:
  - stream_id: s
    onset: 0.0
    duration: {dur}
    sample: voice.wav
    time_mode: absolute
    density: {den}
    grain:
      duration: 0.02
seed: 2026
"""

REPS = 3

def once(dur, den):
    path = os.path.join(OUT, "bench.yml")
    open(path, "w").write(YAML.format(dur=dur, den=den))
    g = Generator(path); g.load_yaml(); g.create_elements()
    r = _build_renderer("numpy", g, output_sr=48000,
                        ssdir=os.path.join(PGE, "refs"), sfdir=OUT,
                        use_cache=False, jobs=1)
    t0 = time.perf_counter()
    RenderingEngine(r).render(streams=g.streams,
                              output_path=os.path.join(OUT, "bench.aif"),
                              mode=MixRenderMode())
    t = time.perf_counter() - t0
    return t, sum(len(s.grains) for s in g.streams)

def once_yaml(path):
    """Come once(), ma su un YAML gia' scritto (gli esempi del paper).

    Separa anche le due meta' del lavoro. I grani sono lazy: il primo accesso a
    `.grains` li materializza, e se non lo si forza quel costo finisce dentro il
    render. Toccarli prima non cambia il totale, ma dice quanto costa costruire
    la popolazione (gli oggetti Grain) rispetto a sommarla nel buffer.
    """
    t0 = time.perf_counter()
    g = Generator(path); g.load_yaml(); g.create_elements()
    t_setup = time.perf_counter() - t0

    t0 = time.perf_counter()
    n = sum(len(s.grains) for s in g.streams)   # materializza
    t_build = time.perf_counter() - t0

    r = _build_renderer("numpy", g, output_sr=48000,
                        ssdir=os.path.join(PGE, "refs"), sfdir=OUT,
                        use_cache=False, jobs=1)
    t0 = time.perf_counter()
    RenderingEngine(r).render(streams=g.streams,
                              output_path=os.path.join(OUT, "bench.aif"),
                              mode=MixRenderMode())
    t_mix = time.perf_counter() - t0

    d = max(s.onset + s.duration for s in g.streams)
    return t_setup + t_build + t_mix, n, d, t_setup, t_build, t_mix


def run_yaml(path):
    ts, parts, n, d = [], None, 0, 0.0
    for _ in range(REPS):
        t, n, d, ts_, tb, tm = once_yaml(path)
        ts.append(t)
        if parts is None or t == min(ts):
            parts = (ts_, tb, tm)
    return dict(dur=d, den=None, n=n, t=min(ts), t_med=statistics.median(ts),
                t_setup=parts[0], t_build=parts[1], t_mix=parts[2])


def run(dur, den):
    ts, n = [], 0
    for _ in range(REPS):
        t, n = once(dur, den)
        ts.append(t)
    return dict(dur=dur, den=den, n=n, t=min(ts), t_med=statistics.median(ts))

def fit(rows):
    """Minimi quadrati su t = a*N + b*D, sui tre sweep.

    Il caso di riferimento e' escluso: e' un esempio reale multi-stream con
    voci e deviazioni, quindi un costo per grano diverso da quello degli sweep.
    Serve a verificare l'ordine di grandezza, non a fittare il modello.
    """
    import numpy as np
    pts = [(r["n"], r["dur"], r["t"]) for k in ("A", "B", "C") for r in rows[k]]
    M = np.array([[n, d] for n, d, _ in pts])
    y = np.array([t for _, _, t in pts])
    (a, b), *_ = np.linalg.lstsq(M, y, rcond=None)
    err = np.abs(M @ np.array([a, b]) - y) / y
    print(f"\n== fit su {len(pts)} punti ==")
    print(f"  t = {a*1e6:.1f} us/grano * N  +  {b*1e3:.2f} ms/s * D")
    print(f"  errore relativo: mediano {np.median(err)*100:.1f}%, max {err.max()*100:.1f}%")
    print(f"  i due termini pareggiano a {b/a:.0f} grani/s\n")


def main():
    rows = {}
    print("\n== A: durata fissa 10 s, densita' crescente ==")
    print(f"{'density':>8} {'grani':>7} {'t_min(s)':>9} {'us/grano':>9}")
    rows["A"] = []
    for den in (10, 25, 50, 100, 200, 400, 800, 1600, 3200):
        r = run(10.0, den); rows["A"].append(r)
        print(f"{den:>8} {r['n']:>7} {r['t']:>9.3f} {1e6*r['t']/r['n']:>9.1f}")

    print("\n== B: ~4000 grani, durata crescente (density = 4000/durata) ==")
    print(f"{'durata':>8} {'density':>9} {'grani':>7} {'t_min(s)':>9}")
    rows["B"] = []
    for dur in (5, 10, 20, 40, 80, 160, 320):
        r = run(float(dur), round(4000/dur, 4)); rows["B"].append(r)
        print(f"{dur:>7}s {r['den']:>9} {r['n']:>7} {r['t']:>9.3f}")

    print("\n== C: density 100 fissa, durata crescente (grani ∝ durata) ==")
    print(f"{'durata':>8} {'grani':>7} {'t_min(s)':>9} {'us/grano':>9}")
    rows["C"] = []
    for dur in (5, 10, 20, 40, 80, 160, 320):
        r = run(float(dur), 100); rows["C"].append(r)
        print(f"{dur:>7}s {r['n']:>7} {r['t']:>9.3f} {1e6*r['t']/r['n']:>9.1f}")

    # Caso di riferimento citato nella nota sul costo in sec:architettura:
    # l'esempio completo del paper, non un caso sintetico.
    ref = run_yaml(os.path.join(HERE, "complete_example", "complete_example.yml"))
    rows["ref"] = [ref]
    print(f"\n== caso di riferimento (complete_example): {ref['n']} grani su "
          f"{ref['dur']:.1f} s -> {ref['t']:.2f} s ==")
    print(f"   parse+setup {ref['t_setup']:.3f}s | costruzione dei grani "
          f"{ref['t_build']:.3f}s ({1e6*ref['t_build']/ref['n']:.1f} us/grano) | "
          f"overlap-add+scrittura {ref['t_mix']:.3f}s")

    fit(rows)
    p = os.path.join(HERE, "bench_cost.json")
    json.dump(rows, open(p, "w"), indent=1)
    print("json:", p)

if __name__ == "__main__":
    main()
