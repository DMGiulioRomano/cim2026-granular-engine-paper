# Operations Log

Log append-only. Ogni entry: `## [YYYY-MM-DD] <tipo> | <titolo>`.
Tipi: `ingest`, `query`, `lint`, `restructure`.

---

## [2026-05-05] ingest | PGE source modules (Step 2 setup-workspace)

Fonte: `raw/PythonGranularEngine/src/` + `graph/class_diagram.puml`
Output: 6 pagine nuove in `wiki/sources/pge/`
- `generator.md` — Generator, pipeline YAML→SCO, logica solo/mute, eval matematica
- `stream.md` — Stream + StreamConfig + StreamContext, multi-voce, generate_grains()
- `score-visualizer.md` — partitura grafica, encoding frecce, loop mask, envelope panel
- `stream-cache-manager.md` — cache SHA-256 per build incrementale Csound
- `parameter-orchestrator.md` — DSL parametrico, dephase, strategie Pitch/Density
- `renderer.md` — Csound adapter, NumPy overlap-add, ReaperProjectWriter
Aggiornati: `wiki/index.md`, `wiki/log.md`.

---

## [2026-05-04] ingest | CIM Proceedings (23 volumi, 1976–2024)

Fonte: `raw/proceedings/` — `pdftotext` su tutti i PDF, ricerca su radice `granul`.
Output: `wiki/sources/proceedings/cim-survey.md`
Pagine toccate: 1 nuova.
Sintesi: trovati articoli dedicati alla sintesi granulare in 12 dei 23 volumi CIM.
Confronto con PGE documentato nella sezione "tempo differito" del survey.

---

## [2026-05-04] restructure | Allineamento CLAUDE.md al pattern LLM Wiki

Rimossi da CLAUDE.md: `## Novel contributions`, `## PythonGranularEngine — key technical facts`, citazioni bibliografiche (contenuto → wiki).
Aggiunto pointer a wiki/ per contributi e dettagli tecnici PGE.
Rafforzati workflow query (filing risposte come principio esplicito) e lint (suggerisci nuove domande/fonti).
Creato `wiki/sources/bibliography.md`. Spostati contributi in `wiki/overview.md`.
Aggiornati: `wiki/index.md`, `wiki/log.md`.

---

## [2026-05-04] restructure | Implementazione LLM Wiki

Eliminata `context/` (vuota). Creata `wiki/` con struttura LLM Wiki.
Spostato `docs/cim-granular-survey.md` → `wiki/sources/proceedings/cim-survey.md`.
Aggiunto `wiki/index.md`, `wiki/log.md`, `wiki/overview.md`.
Aggiornato `CLAUDE.md` con sezione Wiki e workflow operativi.
