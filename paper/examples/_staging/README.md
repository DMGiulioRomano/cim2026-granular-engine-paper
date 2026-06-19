# `_staging/` — esempi non attivi nel paper

Cartelle YAML **non citate** da nessuna sezione attiva di `paper.tex` e
**non renderizzate** da `make examples`: il wildcard del Makefile è
`examples/*/ex*.yml`, mentre questi file stanno un livello più in basso
(`examples/_staging/exN_*/...`), quindi restano fuori dal build.

Materiale conservato come riferimento / staging, non figure del paper:

| Cartella | Perché qui |
|---|---|
| `ex1_dephase` | generazione precedente, superata dai gemelli `ex3a`/`ex3b` e da `exA_micro` |
| `ex3a_range` | gemello A della deviazione (ampiezza); fuso in `ex3_deviazione` (stream `mask_range`) |
| `ex3b_dephase` | gemello B della deviazione (probabilità); fuso in `ex3_deviazione` (stream `mask_dephase`) |
| `exA_micro` | esempio audio-first (bundle Zenodo / presentazione orale), non figura del paper |

Per riattivarne uno: riportarlo in `examples/` (un livello su) e citarlo da
una sezione. Il README principale (`examples/README.md`) descrive il set
attivo.
