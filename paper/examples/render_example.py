#!/usr/bin/env python3
"""
render_example.py — renderizza un esempio del paper col PGE pinnato nel submodule.

Per un dato YAML produce, nella sua stessa cartella:
    <name>.aif            audio (RENDERER=numpy, mix)          [default]
    <name>_map.pdf        partitura grafica (single-page, page_duration = durata stream)

In modalità STEMS (env STEMS=1) l'audio è invece un file per stream:
    <name>__<stream_id>.aif   un file per ogni stream del YAML
mentre la map resta UNA sola, con tutti gli stream impilati (lo score_visualizer
riceve sempre l'intero generator). Serve agli esempi multi-stream come
deviation, dove i due gemelli vivono in un unico YAML ma vanno ascoltati
separatamente e letti in un'unica figura.

Usa il PGE in raw/PythonGranularEngine (commit pinnato dal submodule), così la
realizzazione spedita corrisponde al codice citato dal paper. Il rendering è
stocastico per gli esempi con gate/async: due run danno grani diversi ma stesso
ANDAMENTO (vedi README e CLAUDE.md "Riproducibilità: andamento, non bit-identico").

Alcuni esempi mostrano la lente d'ingrandimento ("magnify") dello
ScoreVisualizer: un inset che ridisegna ingrandita una regione del piano
tempo×posizione-di-lettura, con marker e connettori sulla sorgente (GridSpec
invariato). Non è una feature di questo driver: sono le chiavi di config
`magnify_auto` / `magnify_targets` già esposte da PGE. Quale esempio la usa, e
come, è dichiarato in POC_BY_EXAMPLE qui sotto.

Uso:
    python render_example.py <path/to/exN.yml>            # mix (default)
    STEMS=1 python render_example.py <path/to/exN.yml>    # un audio per stream
"""
import os
import sys


# POC (lente magnify) per esempio. Chiave = basename del YAML (= token cartella).
# Valori passati tali e quali allo ScoreVisualizer:
#   "auto": True              -> magnify_auto: la lente sul cluster di grani più denso
#   "targets": [ {...}, ... ] -> magnify_targets: target espliciti, ognuno con
#                                almeno 't' (secondi); opzionali y, zoom, out, src, stream
# Gli esempi non elencati non hanno lente (render_page identico a prima).
POC_BY_EXAMPLE = {
    # identita': lente sulla diagonale (t~1s, meta' dello stream) per mostrare
    # la finestra di Hann del singolo grano e l'overlap 2 fra grani adiacenti,
    # illeggibili a piena scala (la diagonale e' una banda piena).
    "identity": {"targets": [
        {"t": 1.0, "zoom": 5.0, "corner": "top-left"},
    ]},
    "distribution": {"targets": [
        {"t": 2.5, "y": 1.035, "zoom": 30.0,  "corner": "bottom-left"},
        {"t": 17.5, "y": 1.035, "zoom": 30.0, "corner": "bottom-right"},
    ]},
    # dimensioni del grano: lente sui grani piu' brevi (durata al minimo, ~1 ms,
    # al 50% della durata, t~5s), illeggibili a piena scala -> inset alto-destra.
    "duration": {"targets": [
        {"t": 5.0, "zoom": 13.0, "corner": "top-right"},
    ]},
    # esempio completo: lente sulla nuvola aperta da offset_range (t~13s) e
    # sul tratto finale trasposto (t~27.5s); y~0.6 = linea di lettura congelata.
    "complete_example": {"targets": [
        {"t": 13, "y": .6, "zoom": 40.0, "corner": "top-left"},
        {"t": 27.5, "y": .6, "zoom": 40.0,  "corner": "top-right"},
    ]},
}


# Forma del glifo del grano nella partitura, per esempio. Chiave = basename del
# YAML (= token cartella). Valore passato tale e quale allo ScoreVisualizer come
# config `grain_shape` (richiede un PGE >= c2cc51b, che introduce la chiave):
#   "arrow"  (default PGE) -> freccia direzionale (verso = segno di speed_ratio)
#   "window" -> silhouette della finestra del grano (l'inviluppo), scalata su
#               durata×altezza. Mostra il disegno delle teste dei grani come
#               inviluppi senza perdere la direzione di lettura.
# Gli esempi non elencati restano alla freccia di default.
GRAIN_SHAPE_BY_EXAMPLE = {
    "identity": "window",
    "complete_example": "window",
    "PGE_voices": "window",
}


def _stems_requested():
    """True se l'env STEMS è impostata a un valore "vero"."""
    return os.environ.get("STEMS", "").strip().lower() in ("1", "true", "yes", "on")

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PGE = os.path.join(REPO, "raw", "PythonGranularEngine")
PGE_SRC = os.path.join(PGE, "src")
PGE_REFS = os.path.join(PGE, "refs")

sys.path.insert(0, PGE_SRC)


def stream_duration(generator):
    """Estremo temporale massimo (onset + duration) fra gli stream."""
    return max((s.onset + s.duration) for s in generator.streams)


def main():
    if len(sys.argv) < 2:
        print("Uso: python render_example.py <file.yml>")
        sys.exit(1)

    yaml_file = os.path.abspath(sys.argv[1])
    out_dir = os.path.dirname(yaml_file)
    name = os.path.splitext(os.path.basename(yaml_file))[0]
    aif_path = os.path.join(out_dir, name + ".aif")
    score_path = os.path.join(out_dir, name + "_map.pdf")

    # Import dopo aver messo PGE_SRC in path
    from pge.engine.generator import Generator
    from pge.rendering.rendering_engine import RenderingEngine
    from pge.rendering.render_mode import MixRenderMode, StemsRenderMode
    from pge.rendering.score_visualizer import ScoreVisualizer
    from main import _build_renderer

    # PATHSAMPLES è './refs/' (cwd-relative): renderizza dal dir del PGE così
    # './refs/voice.wav' risolve. Gli output usano path assoluti.
    os.chdir(PGE)

    generator = Generator(yaml_file)
    print(f"Caricamento {yaml_file} ...")
    generator.load_yaml()
    print("Generazione streams ...")
    generator.create_elements()

    renderer = _build_renderer(
        "numpy",
        generator,
        output_sr=48000,
        ssdir=PGE_REFS,
        sfdir=out_dir,
        use_cache=False,
    )

    engine = RenderingEngine(renderer)
    if _stems_requested():
        # STEMS: un file per stream (<name>__<stream_id>.aif). La map resta
        # unica (export_pdf sotto usa l'intero generator).
        mode = StemsRenderMode()
        print("Modalità STEMS: un file audio per stream.")
    else:
        mode = MixRenderMode()
    generated = engine.render(
        streams=generator.streams,
        output_path=aif_path,
        mode=mode,
    )
    print(f"Audio: {generated}")

    dur = stream_duration(generator)
    # Testo della partitura ingrandito per la stampa del paper. Override con
    # env var PGE_FONT_SCALE (es. PGE_FONT_SCALE=1.5 make examples) per tarare
    # senza editare lo script. Richiede un PGE col supporto font_scale (>= il
    # commit pinnato che introduce la chiave nello ScoreVisualizer).
    font_scale = float(os.environ.get("PGE_FONT_SCALE", "2.3"))
    print(f"Partitura (page_duration={dur}s, single-page, font_scale={font_scale}) ...")
    viz_config = {
        "page_duration": dur,
        "show_static_params": False,
        "font_scale": font_scale,
    }
    grain_shape = GRAIN_SHAPE_BY_EXAMPLE.get(name)
    if grain_shape:
        viz_config["grain_shape"] = grain_shape
        print(f"Forma grano: {grain_shape}")
    poc = POC_BY_EXAMPLE.get(name)
    if poc and poc.get("targets"):
        viz_config["magnify_targets"] = poc["targets"]
        print(f"Magnify (target espliciti): {poc['targets']}")
    elif poc and poc.get("auto"):
        viz_config["magnify_auto"] = True
        print("Magnify (auto: cluster più denso)")
    viz = ScoreVisualizer(generator, config=viz_config)
    viz.export_pdf(score_path)
    print(f"Partitura: {score_path}")


if __name__ == "__main__":
    main()
