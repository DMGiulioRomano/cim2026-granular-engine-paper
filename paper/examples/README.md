# Esempi del paper — PythonGranularEngine (PGE)

Tre esempi minimi, ciascuno isola **un** meccanismo del sistema e ne mostra
l'esito sonoro. Ogni cartella è autocontenuta: sorgente YAML + realizzazione
(partitura, waveform, spettrogramma). L'audio (`.aif`) è su Zenodo, non in git.

| Esempio | Parametro isolato | Andamento | Bit-identico? |
|---------|-------------------|-----------|---------------|
| `ex1_dephase` | `dephase` 0→100 | banda pulita → nuvola che si allarga | no |
| `ex2_distribution` | `distribution` 0→1 | treno sincrono → tappeto asincrono (sulla waveform) | no |
| `ex3_voices` | 5 voci, `chord dom9`, pan/pointer lineari | 5 bande parallele, colore per pitch | sì |

## Riproducibilità: andamento, non bit-identico

Il rendering PGE è stocastico (tendency mask alla Truax): il modulo `random` non
è seminato in produzione, quindi due run dello stesso YAML producono **grani
diversi**. È voluto, non un difetto. Ciò che si conserva è l'**andamento**:
densità, dispersione, traiettoria del pointer, distribuzione delle voci. La
stessa specifica YAML produce sempre la stessa *forma*.

- `ex1` e `ex2` usano gate/jitter non seminati → **non bit-identici**, ma
  l'andamento (apertura della nuvola, transizione sync→async) è invariante.
- `ex3` usa solo strategie deterministiche (`chord`, `linear`) → **bit-identico**.

Lo YAML è la fonte di verità spedita: chiunque lo esegue ottiene lo stesso
andamento. La partitura/audio inclusi sono **una** realizzazione di esempio.

## File per cartella

```
exN_*/
  exN_*.yml                 sorgente, fonte di verità (git)
  exN_*_score.pdf           partitura grafica generata (git)
  exN_*_waveform.pdf        forma d'onda (git)
  exN_*_spectrogram.pdf     spettrogramma B&W-safe (git)
  exN_*.aif                 audio (gitignored → Zenodo)
```

## Come rigenerare

Dalla root del repo:

```bash
make examples
```

Richiede il campione sorgente `weNeedToTalkAboutIt.wav` in
`raw/PythonGranularEngine/refs/` (gitignored — voce di donna, ~2 s). Il target:

1. renderizza audio + partitura con il PGE **pinnato nel submodule**
   (`render_example.py`, `RENDERER=numpy`), così la realizzazione corrisponde
   al codice citato dal paper;
2. genera waveform + spettrogramma dall'`.aif` (`plot.py`, scala di grigi
   leggibile in stampa B&W).

Per un singolo esempio:

```bash
.venv/bin/python paper/examples/render_example.py paper/examples/ex1_dephase/ex1_dephase.yml
.venv/bin/python paper/examples/plot.py paper/examples/ex1_dephase/ex1_dephase.aif
```

## Audio (Zenodo)

DOI: `TODO` — placeholder fino al caricamento del bundle. Per la submission
double-blind il record va anonimizzato (nessun nome autore, nessun link al repo).
