# Piano: configurazione workspace CIM 2026

> **Nota:** Questo file sostituisce la versione precedente (`setup-workspace.md`),
> scritta prima dell'adozione del pattern LLM Wiki. Tutti i path `docs/semantic/`
> e `docs/literature/` della versione precedente sono obsoleti. La struttura
> corrente è `wiki/` — vedi `CLAUDE.md` sezione "Wiki (knowledge base)".

Esegui questo piano in ordine. Ogni step è indipendente e verificabile.
Repo: `cim2026-granular-engine-paper/`. Submodule PGE in `raw/PythonGranularEngine/`.
Leggi `CLAUDE.md` prima di iniziare.

---

## Step 1 — Verifica prerequisiti

Controlla che le seguenti cartelle esistano già (create con la migrazione al pattern LLM Wiki):

```
wiki/
  index.md                          ✓ già presente
  log.md                            ✓ già presente
  overview.md                       ✓ già presente
  sources/
    bibliography.md                 ✓ già presente
    proceedings/
      cim-survey.md                 ✓ già presente
    papers/                         vuoto — da popolare negli step successivi
    pge/                            vuoto — da popolare negli step successivi
  concepts/                         vuoto — da popolare negli step successivi
```

Se una cartella manca, creala:

```bash
mkdir -p wiki/sources/papers
mkdir -p wiki/sources/pge
mkdir -p wiki/concepts
```

---

## Step 2 — Ingest moduli PGE core

Per ogni modulo segui il **Workflow ingest (PGE source module)** in `CLAUDE.md`.
Ordine di priorità:

1. `generator.py` → `wiki/sources/pge/generator.md`
   Input aggiuntivo: `graph/class_diagram.puml`

2. `stream.py` + `stream_config.py` → `wiki/sources/pge/stream.md`
   Input aggiuntivo: `graph/class_diagram.puml`

3. `score_visualizer.py` → `wiki/sources/pge/score-visualizer.md`
   Trova con: `find raw/PythonGranularEngine/src -name "score_visualizer.py"`

4. `stream_cache_manager.py` → `wiki/sources/pge/stream-cache-manager.md`
   Trova con: `find raw/PythonGranularEngine/src -name "stream_cache_manager.py"`

5. `parameter_orchestrator.py` + strategie → `wiki/sources/pge/parameter-orchestrator.md`
   Input aggiuntivo: `graph/class_diagram.puml` (gerarchia strategie)

6. `csound_renderer.py` + `numpy_audio_renderer.py` + `reaper_project_writer.py`
   → `wiki/sources/pge/renderer.md`
   Trova con: `find raw/PythonGranularEngine/src -name "*renderer*" -o -name "*reaper*"`

## Step 3 — Ingest papers (fonti primarie)

Per ogni paper segui il **Workflow ingest (paper PDF)** in `CLAUDE.md`.
I PDF si trovano in `raw/papers/`.

### Priorità 1 — tesi centrale e contesto teorico
1. `truax1990.md`  ← Truax 1990, Composing with Real-Time Granular Sound
2. `roads1988.md`  ← Roads 1988, Introduction to Granular Synthesis
3. `truax1988.md`  ← Truax 1988, Real-Time Granular Synthesis with a DSP
4. `gabor1947.md`  ← Gabor 1947, Acoustical Quanta and the Theory of Hearing

### Priorità 2 — contribuzioni specifiche PGE
5. `roads2001.md`  ← Roads 2001, Microsound (libro — ingestire come fonte primaria,
                     trattare come paper lungo: estrarre solo capitoli rilevanti
                     su notazione granulare, densità, rappresentazione)
6. `discipio1994.md`  ← Di Scipio 1994, Micro-Time Sonic Design and Timbre Formation
7. `roads2012.md`  ← Roads 2012, From Grains to Forms
8. `truax1994.md`  ← Truax 1994, Discovering Inner Complexity
9. `truaxsd.md`    ← Truax sd, Interacting Inner Outer Sonic Complexity

### Priorità 3 — comparabili tecnici e storici
10. `depoli-piccialli1988.md`  ← De Poli, Piccialli 1988, Forme d'onda sintesi
                                  granulare sincrona (CIM VII)
11. `depoli-piccialli1991.md`  ← De Poli, Piccialli 1991, Pitch Synchronous
                                  Granular Synthesis
12. `roads1978.md`  ← Roads 1978, Automated Granular Synthesis of Sound
13. `roads-kilgore-duplessis2021.md`  ← Roads, Kilgore, DuPlessis 2021,
                                         Architecture Real-Time Granular Synthesis
                                         EmissionControl2

## Step 4 — Ingest paper proceedings CIM

Per ogni paper segui il **Workflow ingest (paper da proceedings CIM)** in `CLAUDE.md`.
I PDF dei volumi si trovano in `raw/proceedings/`.

Il filtraggio dei volumi rilevanti è già documentato in
`wiki/sources/proceedings/cim-survey.md` — leggilo prima di iniziare
questo step per orientarti sui contenuti di ciascun volume.

### Livello A — ingest completo del paper
Precursori diretti + calibrazione stilistica venue recente.
Per i volumi recenti (2022, 2024): cerca paper di tipo tool/sistema,
comunicazione orale 6–8 pagine; ingerisci solo quelli.

1. `roads1985.md`
   Volume: `1985_CIM_VI_Atti.pdf`
   Paper: Roads, "Granular Synthesis of Sound: Past Research and Future Prospects"

2. `discipio1991.md`
   Volume: `1991_CIM_IX_Atti.pdf`
   Paper: Di Scipio, "Caos deterministico, composizione e sintesi del suono"

3. `rizzuti2006.md`
   Volume: `2006_CIM_XVI_Atti.pdf`
   Paper: Rizzuti, "Il 'caos sonoro': studi preliminari..."

4. `arcella-silvestri2012.md`
   Volume: `2012_CIM_XIX_Atti.pdf`
   Paper: Arcella, Silvestri, "Analogique B: A computer model..."

5. `<autore-anno>.md` — 1–2 paper tool/sistema da `2022_CIM_XXIII_Atti.pdf`
   Strategia: `pdftotext 2022_CIM_XXIII_Atti.pdf | grep -i "sistema\|tool\|software\|ambiente"`
   per localizzare candidati, poi leggere solo quelli

6. `<autore-anno>.md` — 1–2 paper tool/sistema da `2024_CIM_XXIV_Atti.pdf`
   Stessa strategia

### Livello B — estrai solo il paper dal volume
Articoli dedicati alla granulare ma non precursori diretti.
Usa `pdftotext` + grep per localizzare le pagine esatte nel volume,
poi leggi solo quelle pagine.

7. `depoli-piccialli1988-cim.md`
   Volume: `1988_CIM_VII_Atti.pdf`
   Paper: De Poli, Piccialli, "Forme d'onda per la sintesi granulare sincrona"
   Nota: stesso autore del paper in raw/papers/ — confronta le due versioni

8. `keller-truax1998.md`
   Volume: `1998_CIM_XII_Atti.pdf`
   Paper: Keller, Truax, "MacPod: real-time granular synthesis for the Macintosh"

9. `geography2003.md`
   Volume: `2003_CIM_XIV_Atti.pdf`
   Paper: autore n.d., "A Two-Level System for Grain Generation and Control Structure"

10. `sparano2018.md`
    Volume: `2018_CIM_XXII_Atti.pdf`
    Paper: Sparano, "GrainLab - Software open source per la sintesi granulare quasi-sincrona"

### Livello C — ignora
Volumi con sole menzioni (non articoli dedicati):
CIM V 1983, CIM VIII 1989, CIM X 1993 (Lippe), CIM XI 1995,
CIM XIII 2000, CIM XVII 2008, CIM XVIII 2010, CIM XXI 2016,
CIM XXIII 2022 e XXIV 2024 eccetto i paper Livello A scelti.

---
## Step 5 — Scrivi pagine concetti

**Da eseguire dopo il completamento degli step 2–4.**

Le pagine concetti emergono dall'ingest — non sono predefinibili.
Prima di iniziare questo step:

1. Leggi `wiki/index.md` per vedere cosa è stato ingestito
2. Esegui il **Workflow lint** (`CLAUDE.md`) per identificare:
   - concetti citati in più pagine ma senza pagina propria
   - connessioni trasversali emerse dall'ingest
3. Scrivi le pagine concetti che il lint suggerisce,
   seguendo il pattern: ogni pagina sintetizza fonti già ingestate,
   non introduce contenuto nuovo

Le pagine attese (da verificare dopo l'ingest) sono documentate
in `wiki/overview.md` sezione "Gap da colmare".

---

## Step 6 — Aggiorna wiki/overview.md

Dopo step 2–5, rileggi `wiki/overview.md` e aggiorna:
- Tabella precursori con eventuali nuovi dettagli emersi dall'ingest
- Sezione "Differenziatori chiave" con elementi tecnici precisi dai moduli PGE
- Sezione "Gap da colmare" — rimuovi le voci completate

---

## Step 7 — Lint wiki

Chiedi a Claude Code di eseguire il **Workflow lint** definito in `CLAUDE.md`:
- Pagine orfane (nessun inbound link)
- Contraddizioni tra pagine
- Concetti citati ma senza pagina propria
- Gap di fonti ancora aperti

---

## Verifica finale

Al termine di tutti gli step, il repo deve avere:

```
wiki/
  index.md                              ✓ aggiornato
  log.md                                ✓ aggiornato
  overview.md                           ✓ aggiornato
  sources/
    bibliography.md                     ✓ aggiornato
    proceedings/
      cim-survey.md                     ✓ già presente
      roads1985.md                      ✓ step 4
      arcella-silvestri2012.md          ✓ step 4
      rizzuti2006.md                    ✓ step 4
      discipio1991.md                   ✓ step 4
      <autore-anno>.md (x2 CIM 2022/24) ✓ step 4
    papers/
      truax1990.md                      ✓ step 3
      roads2001.md                      ✓ step 3
      roads1988.md                      ✓ step 3
      truax1988.md                      ✓ step 3
    pge/
      generator.md                      ✓ step 2a
      stream.md                         ✓ step 2b
      score-visualizer.md               ✓ step 2c
      stream-cache-manager.md           ✓ step 2d
      parameter-orchestrator.md         ✓ step 2e
      renderer.md                       ✓ step 2f
  concepts/
    control-perception-gap.md           ✓ step 5a
    granular-synthesis.md               ✓ step 5b
    truax-control-hierarchy.md          ✓ step 5c
    dsl-yaml.md                         ✓ step 5d
    graphic-score.md                    ✓ step 5e
    deferred-time-tradition.md          ✓ step 5f
```

Dopo la verifica: aggiorna `docs/plans/next-session.md` con il piano
per la fase di scrittura del paper.
