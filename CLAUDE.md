# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

LaTeX source for a **demo paper** (max 4 pages) submitted to **XXV CIM 2026** (Colloquio di Informatica Musicale), L'Aquila, 13–16 October 2026. The paper describes [PythonGranularEngine](https://github.com/DMGiulioRomano/PythonGranularEngine), a deferred-time granular synthesis engine written entirely in Python.

## Build

```bash
pdflatex paper.tex
pdflatex paper.tex   # second pass resolves cross-references
```

Output: `paper.pdf` (not tracked in git).

## CIM 2026 formatting constraints

These are hard requirements — do not deviate:

- **Max 4 pages** (demo category). Full papers are 8 pages.
- A4 portrait. Text area 17.2 × 25.2 cm. Margins: top 2.0 cm, bottom 2.5 cm, left/right 1.9 cm.
- Two columns, 8.2 cm each, 0.8 cm gutter.
- Body text: Times New Roman 10 pt. Title: 16 pt bold caps. Section heads: 12 pt bold centered.
- No headers, footers, or page numbers in the submitted PDF (added by the proceedings editor).
- Copyright notice in 8 pt Times New Roman at bottom-left of page 1 (already in `paper.tex` via `\blfootnote`).
- References: numbered `[1]`, listed at end in alphabetical order. Citation format documented in `templates/cim2026_template_paper.pdf`.
- **Double-blind peer review**: the submitted PDF must be anonymized (remove author name and affiliation before submission).
- Language: Italian or English. If Italian body text, English abstract is mandatory.
- Abstract: 150–200 words.
- Submission via EasyChair: https://easychair.org/conferences/?conf=xxvcim2026 (deadline 7 June 2026).

## Academic level (derived from CIM 2022/2024 proceedings)

CIM tool/system papers cite 9–21 references mixing foundational audio DSP papers with software documentation. Expected structure: abstract → introduction (motivation + related work) → system architecture → demonstration/results → conclusions. Figures should be high-contrast (visible in B&W print). Include a GitHub link and, if possible, a Zenodo DOI for reproducibility.

## PythonGranularEngine — key technical facts for the paper

The engine described in the paper has these components (source: https://github.com/DMGiulioRomano/PythonGranularEngine):

**Core data structures:** `Grain` (immutable: onset, duration, buffer pointer, pitch ratio, volume, pan), `Stream` (sequence of grains sharing a strategy), `Cartridge` (collection of streams = one composition section).

**YAML DSL:** declarative configuration with mathematical expression evaluation at parse time (e.g. `pi/100`, `10/3`). Nested envelope structures parametrize all grain attributes over normalized time [0.0, 1.0].

**Dual rendering backend:**
- *NumPy renderer*: pure overlap-add synthesis — accumulates windowed grain samples into output buffer with sample-accurate positioning. No external audio dependencies.
- *Csound renderer*: generates `.sco` score files executed by a Csound orchestra. Produces bit-identical output to the NumPy renderer.

**Incremental cache:** SHA-256 fingerprinting skips re-rendering unchanged streams.

**Parameter strategies:**
- Pitch: chord, step, range, stochastic intervals
- Timing: linear canons, micro-polyrhythms with onset variations
- Pointer: linear reading, stochastic dispersal through source buffer
- Panning: stereo spread

**Graphic score:** generated PDF where Y-axis = position in source buffer (not frequency), color = pitch ratio, opacity = volume, width = grain duration, arrow direction = playback direction.

**Density experiment config (`PGE_density_experiment.yml`):** 9 sections, density 4–300 grains/sec, explores perceptual fusion thresholds of granular texture. This is the primary demo material for the paper.

**I/O:** WAV input, AIFF float64 output, stereo.

## Novel contributions to highlight

1. Pure-Python granular engine with no real-time dependency — entire pipeline (YAML → grains → audio + score) is reproducible and scriptable.
2. Dual renderer producing bit-identical output (NumPy vs Csound) — enables flexible deployment.
3. Graphic score whose Y-axis encodes buffer position, not pitch — bridges symbolic and granular notation.
4. Declarative YAML DSL with mathematical expressions and nested envelopes as compositional language.

## Local reference materials (not in git)

- `proceedings/CIM2024_XXIV_Atti.pdf` — full CIM 2024 proceedings (112 MB)
- `proceedings/CIM2022_XXIII_Atti.pdf` — full CIM 2022 proceedings (65 MB)
- `templates/cim2026_template_paper.pdf` — official formatting template
