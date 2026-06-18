# Piano — Pacchetto esempi del paper + organizzazione `paper/`

Data: 2026-05-31 · Branch: `paper-bottom-up`

## Contesto

La review (`review_report.md`, `REVIEW_BRIEF.md`) imputa al paper il difetto
*tells-not-shows*: i meccanismi (dephase, distribution, voci) sono nominati ma
mai mostrati all'ascolto, e gli esempi YAML sono sintattici. La figura
`score_example.png` va **cancellata**: non ha YAML sorgente, non è riproducibile.

Decisione del maestro (2026-05-31): tre esempi nuovi, scritti da zero, ciascuno
con YAML spedibile + una realizzazione (partitura + audio). Sorgente = `weNeedToTalkAboutIt.wav`
(voce di donna, in `raw/PythonGranularEngine/refs/`, gitignored).

## Principio di riproducibilità (NON bit-identico)

Il rendering PGE è stocastico (tendency mask): il `random` non è seminato, due run
danno grani diversi. **Voluto, non un difetto.** Ciò che si conserva è
l'**andamento** (densità, dispersione, traiettoria, distribuzione voci). Gli
esempi spediscono il YAML (chiunque ottiene lo stesso andamento) + una
realizzazione audio/partitura come istanza. Vedi `CLAUDE.md` §"Riproducibilità:
andamento, non bit-identico" e la nota in `wiki/sources/pge/voice-manager.md`.
Issue docstring fuorvianti aperta: PythonGranularEngine#76.

## I tre esempi

| Esempio | Parametro mostrato | Andamento atteso | Riproducibile bit? |
|---------|--------------------|------------------|--------------------|
| ex1_dephase | `dephase: [[0,0],[T,100]]`, resto default + `_range` su pan/pitch/pointer | banda pulita → nuvola che si allarga | no (gate non seminato) |
| ex2_distribution | `distribution: [[0,0],[T,1]]` | treno sync → tappeto async (leggibile su waveform) | no (async non seminato) |
| ex3_voices | `num_voices: 5`, `pitch: chord dom9`, `pan: linear spread 150` | 5 bande parallele, colore per pan | sì (strategie deterministiche) |

Bit-identico irrilevante: conta l'andamento.

## Layout target

```
cim2026-.../
  paper/
    paper.tex            (git mv da root)
    refs.bib             (git mv da root)
    examples/
      README.md          (come rendere + nota weNeedToTalkAboutIt.wav + DOI Zenodo placeholder)
      ex1_dephase/
        ex1_dephase.yml      sorgente        (git)
        score.pdf            partitura gen.  (git)
        waveform.pdf         plot gen.       (git)
        spectrogram.pdf      plot gen.       (git)
        ex1_dephase.aif      audio gen.      (gitignored -> Zenodo)
      ex2_distribution/  (idem)
      ex3_voices/        (idem)
  Makefile               (pdflatex gira in paper/; nuovo target `examples`)
  raw/ wiki/ graph/ docs/ templates/
```

Una cartella per esempio (autocontenuta, facile bundle Zenodo).

## Passi

1. **Pacchetto `paper/`**
   - `git mv paper.tex refs.bib paper/`
   - crea `paper/examples/` + `README.md`

2. **`.gitignore`**
   - eccezione PDF esempi: `!paper/examples/**/*.pdf`
   - ignora audio: `*.aif`, `*.wav`

3. **Tre YAML** in `paper/examples/exN_*/` (bozze già concordate in sessione)

4. **Makefile**
   - target `examples`: per ogni yml → render PGE `RENDERER=numpy` → copia
     partitura PDF + audio → script plot waveform+spettrogramma dell'`.aif`
   - `paper:` aggiornato per girare `pdflatex` in `paper/`

5. **paper.tex**
   - rimuovi riga `\includegraphics{raw/.../score_example.png}` (ex 493)
   - `\includegraphics` dai nuovi `examples/exN_*/score.pdf` (+ waveform/spettrogramma)
   - aggiungi lettura guidata in prosa (bozza in `figure_walkthrough.md` Parte 1)
   - risolvi categoria sistema (granulazione/granular sampling) + Vocem foil + EC2
     + frase «frequenza» (vedi `revision_checklist.md`)

6. **CLAUDE.md** — aggiorna schema repository (nuovo `paper/`, `examples/`)

7. **Plot script** — piccolo script Python (matplotlib + soundfile) per
   waveform + spettrogramma B&W-safe da `.aif`. Dove: `paper/examples/` o `utils/`.

## Aperto da decidere in fase di esecuzione

- Durata `T` degli esempi (20 s? più corto per figura leggibile?).
- Posizione script plot (examples/ vs utils/).
- Spettrogramma: scala log/lin, colormap grayscale per stampa B&W.
- DOI Zenodo: placeholder finché non si carica il bundle (anonimizzato per double-blind).
