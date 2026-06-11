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


def residual_rms_db(orig, sr_o, rend, sr_r, trim=0.05, max_lag_ms=1.0):
    """RMS del residuo gain-matched in dB relativo all'RMS del segnale di riferimento.

    Passaggi:
    1. Ricampiona orig a sr_r con np.interp (stesso metodo del GrainRenderer).
    2. Scarta `trim` secondi a testa/coda (bordi COLA instabili).
    3. Allinea via cross-correlazione (±max_lag_ms ms) per compensare il
       drift di ±1 sample dovuto all'accumulazione float del tempo tra grani.
    4. Stima α = dot(orig,rend)/dot(orig,orig) per neutralizzare:
       - differenze di livello assoluto (volume default)
       - fattore √2 della legge di pan constant-power a centro (by design)
    5. Residuo = rend - α·orig; riferimento = α·orig.
    """
    if sr_o != sr_r:
        t_new = np.arange(int(len(orig) * sr_r / sr_o)) / sr_r
        orig = np.interp(t_new, np.arange(len(orig)) / sr_o, orig)
    n = min(len(orig), len(rend))
    lo, hi = int(trim * sr_r), n - int(trim * sr_r)
    x_full, y_full = orig[lo:hi], rend[lo:hi]

    # Trova il lag ottimale (accumulazione float IOT → grain onset ±1 sample)
    max_lag = max(1, int(max_lag_ms * sr_r / 1000))
    xcorr = np.correlate(y_full, x_full[max_lag:-max_lag] if max_lag else x_full, mode='valid')
    best_lag = int(np.argmax(np.abs(xcorr))) - max_lag
    # Applica lag: taglia orig e rend in modo allineato
    lo2 = max(0, best_lag)
    lo3 = max(0, -best_lag)
    m = min(len(x_full) - lo2, len(y_full) - lo3)
    x, y = x_full[lo2:lo2 + m], y_full[lo3:lo3 + m]

    alpha = np.dot(x, y) / np.dot(x, x)
    ref = alpha * x
    diff = y - ref
    rms_ref = np.sqrt(np.mean(ref ** 2))
    rms_diff = np.sqrt(np.mean(diff ** 2))
    return 20 * np.log10(rms_diff / rms_ref), alpha, best_lag


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

    res_db, alpha, lag = residual_rms_db(orig, sr_o, rend, sr_r)
    print(f"  gain factor α = {alpha:.4f}  ({20*np.log10(abs(alpha)):.1f} dB)")
    print(f"  align lag: {lag} samples ({lag / sr_r * 1000:.3f} ms)")
    print(f"  residuo RMS gain-matched: {res_db:.1f} dB rel. al sorgente")

    t_o = np.arange(len(orig)) / sr_o
    t_r = np.arange(len(rend)) / sr_r

    ymax = max(np.abs(orig).max(), np.abs(rend).max(), 1e-6) * 1.05

    fig, axes = plt.subplots(2, 1, figsize=(COL_W_IN, COL_W_IN * 0.9),
                             sharex=False)

    for ax, t, signal, label in (
        (axes[0], t_o, orig, "originale"),
        (axes[1], t_r, rend, "elaborato"),
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
