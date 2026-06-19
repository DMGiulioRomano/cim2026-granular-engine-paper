#!/usr/bin/env python3
"""
gen_jitter_table.py — genera il corpo della tabella dei jitter impliciti
(Tab.~\\ref{tab:jitter} in sections/24-deviazione.tex) leggendo i valori
direttamente dal PGE pinnato, così i numeri stampati non possono divergere dal
codice citato dal paper.

Cosa scrive
-----------
Un frammento LaTeX in figures/jitter_table.tex con SOLO il contenuto interno
della tabella: l'ambiente `tabular` (header + righe dati) e la footnote del
dagger. caption e \\label restano scritti a mano nella sezione, che include il
frammento con `\\input{figures/jitter_table}`.

Da dove vengono i numeri
------------------------
La tabella elenca, per parametro, la deviazione massima per grano sotto
campionamento uniforme quando il gate `dephase` apre in assenza di range
esplicito (Scenario B). Il sampling uniforme è
    v = center + random.uniform(-0.5, 0.5) * spread      (UniformDistribution)
con spread = `default_jitter` del parametro (Parameter._calculate_range, path
`_mod_range is None`). La deviazione massima è quindi ±default_jitter/2.

Eccezioni:
  - pitch (unità EDO: semitones/cents/quarter_tone/eighth_tone/edo:N): il detune
    implicito NON passa da default_jitter (il value-space EDO è quantizzato).
    UnitPitchStrategy applica random.uniform(-c, c) cents con
    c = EDO_IMPLICIT_DETUNE_CENTS, quindi la semi-ampiezza è ±c DIRETTO (no /2).
  - pitch (unità ratio): nessun detune in cents (implicit_detune_cents = 0); il
    jitter segue il path normale del Parameter, ±RatioUnit.default_jitter/2.
  - reverse: variation_mode='invert', nessun jitter additivo -> "flip discreto".

Lo script possiede il LESSICO DI DOMINIO (etichette di riga, unità, prosa della
footnote): non è un dump del registro. Garantisce che i NUMERI siano sempre
sincronizzati col codice, non che le righe compaiano/scompaiano da sole: se PGE
aggiunge un parametro, la riga va aggiunta qui a mano scegliendone etichetta e
unità.

Sorgente PGE
------------
Risolve src/ in quest'ordine: env PGE_SRC -> submodule raw/PythonGranularEngine
(commit pinnato, path primario) -> sibling ../PythonGranularEngine (comodità in
ambienti senza submodule inizializzato). Per il paper conta il submodule: è il
codice che la realizzazione spedita cita.

Uso:
    python gen_jitter_table.py            # scrive figures/jitter_table.tex
    PGE_SRC=/path/to/src python gen_jitter_table.py
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(HERE, "jitter_table.tex")


def _resolve_pge_src() -> str:
    """src/ del PGE: env override -> submodule pinnato -> sibling working repo."""
    candidates = []
    env = os.environ.get("PGE_SRC", "").strip()
    if env:
        candidates.append(env)
    candidates.append(os.path.join(REPO, "raw", "PythonGranularEngine", "src"))
    candidates.append(os.path.join(os.path.dirname(REPO), "PythonGranularEngine", "src"))
    for path in candidates:
        if os.path.isfile(os.path.join(path, "parameters", "parameter_definitions.py")):
            return path
    raise SystemExit(
        "gen_jitter_table: src/ del PGE non trovato. Inizializza il submodule "
        "(git submodule update --init raw/PythonGranularEngine) oppure imposta "
        "PGE_SRC.\nCercato in:\n  " + "\n  ".join(candidates)
    )


def fmt(x: float) -> str:
    """Numero in stile italiano: virgola decimale, niente zeri di coda."""
    s = f"{x:.6f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def pm(x: float) -> str:
    return r"$\pm$" + fmt(x)


def build_fragment() -> str:
    PGE_SRC = _resolve_pge_src()
    sys.path.insert(0, PGE_SRC)
    from parameters.parameter_definitions import GRANULAR_PARAMETERS
    from parameters.pitch_unit import EDO_IMPLICIT_DETUNE_CENTS, make_pitch_unit

    G = GRANULAR_PARAMETERS
    dj_volume = G["volume"].default_jitter
    dj_pan = G["pan"].default_jitter
    dj_dur = G["grain_duration"].default_jitter          # secondi
    dj_ptr = G["pointer_deviation"].default_jitter        # frazione di buffer
    edo_cents = float(EDO_IMPLICIT_DETUNE_CENTS)
    dj_ratio = make_pitch_unit("ratio").value_bounds().default_jitter

    # (etichetta dominio, valore formattato + unità). Deviazione = ±spread/2,
    # tranne pitch EDO (semi-ampiezza diretta in cents) e reverse (discreto).
    rows = [
        ("volume",  pm(dj_volume / 2) + "~dB"),
        ("pan",     pm(dj_pan / 2) + r"\textdegree"),
        ("durata",  pm(dj_dur / 2 * 1000) + "~ms"),
        ("lettura", pm(dj_ptr / 2 * 100) + r"\% del buffer"),
        ("pitch",   pm(edo_cents) + r"~cents$^{\dagger}$"),
        ("reverse", "flip discreto"),
    ]

    lines = [
        "% Generato da paper/figures/gen_jitter_table.py — non editare a mano.",
        "% Valori derivati dal PGE pinnato (parameter_definitions.py, pitch_unit.py).",
        "% Rigenera con: make jitter-table",
        r"  \begin{tabular}{ll}",
        r"    \hline",
        r"    parametro & jitter implicito \\",
        r"    \hline",
    ]
    width = max(len(label) for label, _ in rows)
    for label, value in rows:
        lines.append(f"    {label.ljust(width)} & {value} \\\\")
    lines.append(r"    \hline")
    lines.append(r"  \end{tabular}\\[2pt]")
    lines.append(r"  {\footnotesize $^{\dagger}$ detune in ratio-space dopo la quantizzazione")
    lines.append(r"  di griglia; " + pm(dj_ratio / 2)
                 + r" sul moltiplicatore per unità \texttt{ratio}.}")
    return "\n".join(lines) + "\n"


def main() -> None:
    fragment = build_fragment()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(fragment)
    print(f"gen_jitter_table: scritto {os.path.relpath(OUT, REPO)}")


if __name__ == "__main__":
    main()
