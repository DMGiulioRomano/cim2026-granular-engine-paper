#!/usr/bin/env python3
"""
plot_comparison.py — waveform incolonnate: originale vs rendering PGE.

Genera un PDF con due forme d'onda sovrapposte verticalmente per mostrare
la relazione input→output di PGE con parametri minimi.

Uso:
    python plot_comparison.py <rendered.aif> <original.wav> [--duration T] [--output path.pdf]
"""
import argparse
import os
import sys

import numpy as np
import soundfile as sf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

COL_W_IN = 3.23  # 8.2 cm — larghezza colonna CIM


def load_mono(path, duration=None):
    data, sr = sf.read(path, always_2d=True)
    mono = data.mean(axis=1)
    if duration is not None:
        mono = mono[:int(duration * sr)]
    return mono, sr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rendered", help="file .aif renderizzato da PGE")
    ap.add_argument("original", help="file .wav originale")
    ap.add_argument("--duration", type=float, default=2.0,
                    help="secondi da visualizzare (default: 2.0)")
    ap.add_argument("--output", default=None,
                    help="path PDF output (default: <rendered_stem>_comparison.pdf)")
    args = ap.parse_args()

    for path in (args.rendered, args.original):
        if not os.path.exists(path):
            print(f"file non trovato: {path}", file=sys.stderr)
            sys.exit(1)

    orig, sr_o = load_mono(args.original, args.duration)
    rend, sr_r = load_mono(args.rendered, args.duration)

    t_o = np.arange(len(orig)) / sr_o
    t_r = np.arange(len(rend)) / sr_r

    ymax = max(np.abs(orig).max(), np.abs(rend).max(), 1e-6) * 1.05

    fig, axes = plt.subplots(2, 1, figsize=(COL_W_IN, COL_W_IN * 0.9),
                             sharex=False)

    for ax, t, signal, label in (
        (axes[0], t_o, orig, "originale"),
        (axes[1], t_r, rend, "PGE"),
    ):
        ax.plot(t, signal, color="black", linewidth=0.3)
        ax.set_xlim(0, args.duration)
        ax.set_ylim(-ymax, ymax)
        ax.set_ylabel(label, fontsize=7)
        ax.tick_params(labelsize=6)
        ax.spines[["top", "right"]].set_visible(False)

    axes[0].set_xticklabels([])
    axes[1].set_xlabel("tempo (s)", fontsize=7)

    fig.tight_layout(pad=0.3)

    out = args.output or os.path.splitext(args.rendered)[0] + "_comparison.pdf"
    fig.savefig(out, format="pdf", bbox_inches="tight")
    plt.close(fig)
    print(f"  comparison -> {out}")


if __name__ == "__main__":
    main()
