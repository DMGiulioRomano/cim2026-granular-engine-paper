#!/usr/bin/env python3
"""
render_map_pages.py — MAP di un esempio del paper divisa in pagine di durata
fissa, per le slide: a pagina più corta i grani si leggono meglio.

Stesso PGE pinnato, stesso YAML (seed compreso) e stessa configurazione della
MAP del paper (paper/examples/render_example.py): cambia solo page_duration.
Non rende l'audio e non tocca paper/examples/. Output in slides/media/:
    <name>_map_<secondi>s_p<N>.svg   una pagina per file (png con il terzo
                                     argomento: le pagine che si alternano
                                     durante l'ascolto devono comparire subito,
                                     le svg da 10+ MB no)

Uso:
    python slides/render_map_pages.py paper/examples/complete_example/complete_example.yml [secondi] [svg|png]
"""
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PGE = os.path.join(REPO, "raw", "PythonGranularEngine")
MEDIA = os.path.join(REPO, "slides", "media")
sys.path.insert(0, os.path.join(PGE, "src"))
sys.path.insert(0, os.path.join(REPO, "paper", "examples"))

# Lenti diverse da quelle del paper, solo per le slide. Chiave = basename YAML.
# complete_example: la lente in alto a sinistra coprirebbe l'etichetta dello
# stream, qui scende in basso a destra, sotto la coda della nuvola.
SLIDE_TARGETS = {
    "complete_example": [
        {"t": 13, "y": .6, "zoom": 8.0, "corner": "bottom-right"},
        {"t": 27.5, "y": .6, "zoom": 8.0, "corner": "top-right"},
    ],
}


def main():
    if len(sys.argv) < 2:
        sys.exit("Uso: python slides/render_map_pages.py <file.yml> [secondi]")
    yaml_file = os.path.abspath(sys.argv[1])
    page = float(sys.argv[2]) if len(sys.argv) > 2 else 10.0
    fmt = sys.argv[3] if len(sys.argv) > 3 else "svg"
    name = os.path.splitext(os.path.basename(yaml_file))[0]
    os.makedirs(MEDIA, exist_ok=True)

    import matplotlib
    matplotlib.use("Agg")
    from pge.engine.generator import Generator
    from pge.rendering.score_visualizer import ScoreVisualizer
    from render_example import POC_BY_EXAMPLE, GRAIN_SHAPE, GRAIN_SHAPE_BY_EXAMPLE

    os.chdir(PGE)
    generator = Generator(yaml_file)
    generator.load_yaml()
    generator.create_elements()

    config = {
        "page_duration": page,
        "show_static_params": False,
        "font_scale": float(os.environ.get("PGE_FONT_SCALE", "2.3")),
        "grain_shape": GRAIN_SHAPE_BY_EXAMPLE.get(name, GRAIN_SHAPE),
    }
    poc = POC_BY_EXAMPLE.get(name) or {}
    targets = SLIDE_TARGETS.get(name, poc.get("targets"))
    if targets:
        config["magnify_targets"] = targets
    viz = ScoreVisualizer(generator, config=config)
    pdf = os.path.join(MEDIA, f"{name}_map_pages.pdf")
    viz.export_pdf(pdf)
    for n in range(1, viz.page_count + 1):
        out = os.path.join(MEDIA, f"{name}_map_{page:g}s_p{n}")
        if fmt == "png":
            cmd = ["pdftoppm", "-png", "-r", "200", "-singlefile", "-f", str(n), "-l", str(n), pdf, out]
        else:
            cmd = ["pdftocairo", "-svg", "-f", str(n), "-l", str(n), pdf, out + ".svg"]
        subprocess.run(cmd, check=True)
        print(f"MAP: {out}.{fmt}")
    os.remove(pdf)


if __name__ == "__main__":
    main()
