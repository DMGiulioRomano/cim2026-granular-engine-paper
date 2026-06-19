#!/usr/bin/env python3
"""
annotate_panels.py — aggiunge etichette di pannello "(a)", "(b)", ... ai plot
dei grani di una map del paper.

Sta a valle di render_example.py: prende lo stesso YAML, ricostruisce la
partitura grafica col PGE pinnato e stampa una lettera nell'angolo in alto a
sinistra di OGNI subplot dei grani (uno per stream), poi riesporta il PDF.
Serve agli esempi multi-stream — tipicamente deviation, i due gemelli
mask_range / mask_dephase — dove il testo della sezione rimanda ai pannelli
come «(a)» e «(b)».

Perche' un secondo script e non una modifica al PGE:
    - lo score_visualizer vive nel submodule (raw/PythonGranularEngine) ed e'
      codice immutabile lato paper: non lo si tocca per un'esigenza editoriale
      del solo paper;
    - render_example.py resta il driver "neutro" (map senza decorazioni);
    - la decorazione (lettere di pannello) e' un passo opzionale, applicato
      solo agli esempi che lo richiedono.

Il rendering e' stocastico (vedi README e CLAUDE.md "Riproducibilita':
andamento, non bit-identico"): questa riesecuzione produce una nuova
realizzazione con lo stesso ANDAMENTO. Il LAYOUT (numero e posizione dei
pannelli) e' invece deterministico, quindi le lettere cadono sempre al posto
giusto.

Le lettere vengono poste solo sui subplot dei GRANI (colonna centrale del
GridSpec, righe-stream), non sul pannello envelope ne' sulle colonne
waveform/colorbar: l'identificazione e' strutturale, via subplotspec, non per
indice fragile.

Uso:
    python annotate_panels.py <path/to/exN.yml>
    python annotate_panels.py <path/to/exN.yml> --labels "(a),(b)"
    python annotate_panels.py <path/to/exN.yml> --output /tmp/altro_map.pdf

Override del PGE (utile in dev con un checkout sibling invece del submodule):
    PGE_HOME=/path/to/PythonGranularEngine python annotate_panels.py <file.yml>
"""
import argparse
import os
import string
import sys


def _resolve_pge():
    """Path del PGE da usare. Default: il submodule pinnato
    (raw/PythonGranularEngine), coerente con render_example.py. Override con
    env PGE_HOME per puntare a un checkout sibling in sviluppo/CI."""
    override = os.environ.get("PGE_HOME", "").strip()
    if override:
        return os.path.abspath(override)
    repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(repo, "raw", "PythonGranularEngine")


def _default_labels(n):
    """('(a)', '(b)', ...) per n pannelli."""
    return [f"({string.ascii_lowercase[i]})" for i in range(n)]


def _grain_axes(fig, n_streams):
    """Subplot dei grani della figura, ordinati per riga (stream order).

    Identificazione strutturale via GridSpec: colonna centrale (col.start == 1)
    e riga di stream (row.start < n_streams). Esclude waveform (col 0),
    colorbar (col 2) e il pannello envelope (riga >= n_streams).
    """
    grain = []
    for ax in fig.axes:
        ss = ax.get_subplotspec()
        if ss is None:
            continue
        if ss.colspan.start == 1 and ss.rowspan.start < n_streams:
            grain.append((ss.rowspan.start, ax))
    grain.sort(key=lambda t: t[0])
    return [ax for _, ax in grain]


def annotate_figure(fig, n_streams, labels, fontsize):
    """Stampa una lettera di pannello su ogni subplot dei grani.

    Posizione: alto a sinistra, appena sotto l'etichetta `stream_id` che il
    visualizer disegna nello stesso angolo (collocarla esattamente nel corner
    si sovrapporrebbe a quella). Quella zona (tempo iniziale, alto del buffer)
    e' tipicamente libera di grani, quindi la lettera resta leggibile."""
    axes = _grain_axes(fig, n_streams)
    for ax, label in zip(axes, labels):
        ax.annotate(
            label,
            xy=(0.02, 0.82), xycoords="axes fraction",
            ha="left", va="top",
            fontsize=fontsize, fontweight="bold", color="black",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                      edgecolor="none", alpha=0.85),
            zorder=10,
        )
    return len(axes)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("yaml_file", help="esempio exN.yml")
    ap.add_argument("--labels", default=None,
                    help="lettere separate da virgola, es. '(a),(b)'. "
                         "Default: (a),(b),(c)... una per subplot grani.")
    ap.add_argument("--output", default=None,
                    help="PDF di output. Default: <name>_map.pdf accanto allo YAML.")
    ap.add_argument("--font-scale", type=float,
                    default=float(os.environ.get("PGE_FONT_SCALE", "2.3")),
                    help="font_scale dello ScoreVisualizer (default env PGE_FONT_SCALE o 2.3).")
    args = ap.parse_args()

    pge = _resolve_pge()
    pge_src = os.path.join(pge, "src")
    if not os.path.isdir(pge_src):
        print(f"PGE non trovato in {pge_src}. Inizializza il submodule "
              f"(git submodule update --init) o usa PGE_HOME.", file=sys.stderr)
        sys.exit(1)
    sys.path.insert(0, pge_src)

    import matplotlib
    matplotlib.use("Agg")
    from matplotlib.backends.backend_pdf import PdfPages
    import matplotlib.pyplot as plt
    from engine.generator import Generator
    from rendering.score_visualizer import ScoreVisualizer

    yaml_file = os.path.abspath(args.yaml_file)
    out_dir = os.path.dirname(yaml_file)
    name = os.path.splitext(os.path.basename(yaml_file))[0]
    out_path = args.output or os.path.join(out_dir, name + "_map.pdf")

    # PATHSAMPLES e' './refs/' (cwd-relative): renderizza dal dir del PGE.
    os.chdir(pge)

    generator = Generator(yaml_file)
    generator.load_yaml()
    generator.create_elements()

    dur = max((s.onset + s.duration) for s in generator.streams)
    viz = ScoreVisualizer(generator, config={
        "page_duration": dur,
        "show_static_params": False,
        "font_scale": args.font_scale,
    })
    viz.analyze()

    # font label coerente con le altre scritte della partitura (label_fontsize
    # scalato), leggermente piu' grande per leggersi come riferimento di figura.
    label_fontsize = viz._fs(viz.config["label_fontsize"] + 1)

    figures = []
    total = 0
    for page_idx, layout in enumerate(viz.page_layouts):
        n_streams = len(layout["active_streams"])
        labels = (args.labels.split(",") if args.labels
                  else _default_labels(n_streams))
        fig = viz.render_page(page_idx)
        total += annotate_figure(fig, n_streams, labels, label_fontsize)
        figures.append(fig)

    with PdfPages(out_path) as pdf:
        for fig in figures:
            pdf.savefig(fig, dpi=150, bbox_inches="tight", pad_inches=0.02)
            plt.close(fig)

    print(f"Map annotata ({total} pannelli) -> {out_path}")


if __name__ == "__main__":
    main()
