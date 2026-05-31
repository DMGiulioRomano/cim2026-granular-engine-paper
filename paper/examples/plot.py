#!/usr/bin/env python3
"""
plot.py — waveform + spettrogramma B&W-safe da un file audio.

Genera due PDF vettoriali accanto al file audio:
    <stem>_waveform.pdf      forma d'onda (mono mixdown)
    <stem>_spectrogram.pdf   spettrogramma in scala di grigi

Scelte per la stampa B&W del paper CIM:
    - colormap 'gray_r' (nero = energia alta) leggibile in bianco e nero
    - nessuna dipendenza da scipy: usa matplotlib.mlab.specgram (FFT numpy)
    - figure a colonna singola (8.2 cm) coerenti col layout a due colonne

Uso:
    python plot.py <audio.aif> [--duration T] [--fmax HZ]
"""
import argparse
import os
import sys

import numpy as np
import soundfile as sf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Larghezza colonna CIM: 8.2 cm ~= 3.23 in
COL_W_IN = 3.23


def load_mono(path):
    data, sr = sf.read(path, always_2d=True)
    mono = data.mean(axis=1)
    return mono, sr


def plot_waveform(mono, sr, out_path, duration=None):
    n = len(mono)
    if duration:
        n = min(n, int(duration * sr))
        mono = mono[:n]
    t = np.arange(n) / sr
    fig, ax = plt.subplots(figsize=(COL_W_IN, COL_W_IN * 0.5))
    ax.plot(t, mono, color="black", linewidth=0.3)
    ax.set_xlim(0, t[-1] if n else 1)
    ymax = np.abs(mono).max() or 1.0
    ax.set_ylim(-ymax * 1.05, ymax * 1.05)
    ax.set_xlabel("tempo (s)", fontsize=8)
    ax.set_ylabel("ampiezza", fontsize=8)
    ax.tick_params(labelsize=7)
    fig.tight_layout(pad=0.3)
    fig.savefig(out_path)
    plt.close(fig)
    print(f"  waveform -> {out_path}")


def plot_spectrogram(mono, sr, out_path, duration=None, fmax=None):
    n = len(mono)
    if duration:
        n = min(n, int(duration * sr))
        mono = mono[:n]
    fig, ax = plt.subplots(figsize=(COL_W_IN, COL_W_IN * 0.6))
    nfft = 2048
    spectrum, freqs, t, im = ax.specgram(
        mono, NFFT=nfft, Fs=sr, noverlap=nfft // 2,
        cmap="gray_r", scale="dB", vmin=-100, vmax=-20,
    )
    ax.set_ylim(0, fmax if fmax else sr / 2)
    ax.set_xlabel("tempo (s)", fontsize=8)
    ax.set_ylabel("frequenza (Hz)", fontsize=8)
    ax.tick_params(labelsize=7)
    fig.tight_layout(pad=0.3)
    fig.savefig(out_path)
    plt.close(fig)
    print(f"  spectrogram -> {out_path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("--duration", type=float, default=None)
    ap.add_argument("--fmax", type=float, default=8000.0,
                    help="frequenza massima nello spettrogramma (Hz)")
    args = ap.parse_args()

    if not os.path.exists(args.audio):
        print(f"file non trovato: {args.audio}")
        sys.exit(1)

    mono, sr = load_mono(args.audio)
    stem = os.path.splitext(args.audio)[0]
    plot_waveform(mono, sr, stem + "_waveform.pdf", args.duration)
    plot_spectrogram(mono, sr, stem + "_spectrogram.pdf", args.duration, args.fmax)


if __name__ == "__main__":
    main()
