# Operations Log

Log append-only. Ogni entry: `## [YYYY-MM-DD] <tipo> | <titolo>`.
Tipi: `ingest`, `query`, `lint`, `restructure`.

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
