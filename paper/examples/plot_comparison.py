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


def build_ola_reference(orig, sr_o, sr_r, n_out_samples, grain_dur=0.05, fill_factor=2):
    """Ricostruisce la reference OLA ideale con t = k * iot (no accumulo float).

    Usa la stessa logica del GrainRenderer (interp lineare, Hanning, no pan)
    ma calcola il tempo di ogni grain come k * iot_sec per evitare il drift
    di accumulazione float che sposta i grain onset di ±1 sample.
    """
    n_source = len(orig)
    sample_len_sec = n_source / sr_o
    n_grain = int(grain_dur * sr_r)
    iot_sec = grain_dur / fill_factor
    increment = sr_o / sr_r
    w = np.hanning(n_grain)

    buf = np.zeros(n_out_samples)
    k = 0
    while True:
        t = k * iot_sec
        if t >= n_out_samples / sr_r:
            break
        onset = int(t * sr_r)
        start_sample = (t / sample_len_sec) * n_source
        idx = start_sample + np.arange(n_grain, dtype=np.float64) * increment
        idx = idx % n_source
        i0 = idx.astype(np.int64) % n_source
        i1 = (i0 + 1) % n_source
        frac = idx - idx.astype(np.int64)
        g = orig[i0].astype(np.float64) * (1.0 - frac) + orig[i1].astype(np.float64) * frac
        end = min(onset + n_grain, n_out_samples)
        buf[onset:end] += (g * w)[:end - onset]
        k += 1
    return buf


def residual_rms_db(orig, sr_o, rend, sr_r, trim=0.05, grain_dur=0.05, fill_factor=2):
    """RMS del residuo gain-matched in dB relativo all'RMS del segnale di riferimento.

    Passaggi:
    1. Costruisce la reference OLA ideale (t = k * iot, Hanning, no pan) per
       eliminare il drift di accumulazione float del grain scheduler.
    2. Scarta `trim` secondi a testa/coda (bordi COLA instabili).
    3. Stima α = dot(ref,rend)/dot(ref,ref) per neutralizzare il fattore 1/√2
       della legge di pan constant-power a centro (by design).
    4. Residuo = rend - α·ref; misura l'errore COLA puro.
    """
    n = min(len(orig) * sr_r // sr_o, len(rend))
    ref = build_ola_reference(orig, sr_o, sr_r, n, grain_dur=grain_dur, fill_factor=fill_factor)
    lo, hi = int(trim * sr_r), n - int(trim * sr_r)
    x, y = ref[lo:hi], rend[lo:hi]
    alpha = np.dot(x, y) / np.dot(x, x)
    diff = y - alpha * x
    rms_ref = np.sqrt(np.mean((alpha * x) ** 2))
    rms_diff = np.sqrt(np.mean(diff ** 2))
    return 20 * np.log10(rms_diff / rms_ref), alpha


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

    res_db, alpha = residual_rms_db(orig, sr_o, rend, sr_r)
    print(f"  gain factor α = {alpha:.4f}  ({20*np.log10(abs(alpha)):.1f} dB)")
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
