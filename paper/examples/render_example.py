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

Uso:
    python render_example.py <path/to/exN.yml>            # mix (default)
    STEMS=1 python render_example.py <path/to/exN.yml>    # un audio per stream
"""
import os
import sys


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
    from engine.generator import Generator
    from rendering.rendering_engine import RenderingEngine
    from rendering.render_mode import MixRenderMode, StemsRenderMode
    from rendering.score_visualizer import ScoreVisualizer
    from main import _build_renderer

    # PATHSAMPLES è './refs/' (cwd-relative): renderizza dal dir del PGE così
    # './refs/weNeedToTalkAboutIt.wav' risolve. Gli output usano path assoluti.
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
    viz = ScoreVisualizer(generator, config={
        "page_duration": dur,
        "show_static_params": False,
        "font_scale": font_scale,
    })
    viz.export_pdf(score_path)
    print(f"Partitura: {score_path}")


if __name__ == "__main__":
    main()
