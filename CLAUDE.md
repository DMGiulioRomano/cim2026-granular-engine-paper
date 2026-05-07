# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## What this repository is

LaTeX source for an **oral communication paper (6–8 pages)** submitted to **XXV CIM 2026** (Colloquio di Informatica Musicale), L'Aquila, 13–16 October 2026. The paper describes [PythonGranularEngine](https://github.com/DMGiulioRomano/PythonGranularEngine) (PGE), a deferred-time granular synthesis environment written in Python.

**Submission deadline:** 7 June 2026 via EasyChair: https://easychair.org/conferences/?conf=xxvcim2026

---

## Repository structure

```
cim2026-granular-engine-paper/
├── CLAUDE.md                        ← this file (schema wiki)
├── Makefile                         ← `make graph`
├── paper.tex                        ← main LaTeX source
├── graph/                           ← structural graphs (py2puml, pyan3)
│   ├── class_diagram.puml           ← py2puml output: PGE class structure
│   └── call_graph.dot               ← pyan3 output: call graph (large, query with grep)
├── wiki/                            ← LLM-generated knowledge base (LLM writes, human reads)
│   ├── index.md                     ← catalog: read first before every search
│   ├── log.md                       ← append-only operations log
│   ├── overview.md                  ← evolving thesis: PGE in granular synthesis landscape
│   ├── sources/
│   │   ├── proceedings/
│   │   │   └── cim-survey.md        ← survey 23 CIM volumes on granular synthesis
│   │   ├── papers/                  ← one page per PDF in raw/papers/
│   │   └── pge/                     ← one page per PGE module analyzed
│   ├── concepts/                    ← cross-source concept synthesis
│   └── semantic/                    ← classes → paper concepts mapping
├── docs/
│   └── plans/                       ← session planning notes (not wiki)
├── raw/                             ← immutable sources (LLM reads, never modifies)
│   ├── papers/                      ← PDF articoli citati (gitignored via *.pdf)
│   ├── proceedings/                 ← PDF atti CIM (gitignored via *.pdf)
│   └── PythonGranularEngine/        ← git submodule (pinned commit)
└── templates/
```

**Layer separation:**
- `raw/` = immutable sources — PDFs, git submodule. Never modified.
- `wiki/` = LLM-generated knowledge base — summaries, synthesis, cross-references. LLM writes; human reads.
- `CLAUDE.md` = schema — structure conventions + operation workflows.

**graph/ usage:** `class_diagram.puml` is readable as context. `call_graph.dot` is 583KB — do not load whole file; use `grep` for specific module queries.

**wiki/ usage:** always read `wiki/index.md` first to find relevant pages. After any substantial operation, update `index.md` and append to `log.md`.

---

## Central thesis

The paper answers an open question in the literature:

> Why is granular synthesis hard to teach and practice, and what can be done to reduce the gap between parametric control and perceptual result?

Truax (1990) identifies this gap as the central problem of granular composition. PGE addresses it at three explicit levels (see contributions below).

This is not a technical description paper. It is an argumentative paper that uses PGE as evidence for a theoretical claim.

---

## Paper structure (6–8 pages)

| Section | Content | Target length |
|---------|---------|---------------|
| 1. Problema | gap controllo/percezione (Roads 1988, Truax 1990) | ~0.5 pp |
| 2. Contesto teorico | gerarchia di controllo Truax, piano tempo/posizione-nel-buffer | ~1 pp |
| 3. Architettura | DSL YAML, Language Server, renderer, pipeline. Diagram. | ~1.5 pp |
| 4. Partitura grafica | asse Y, encoding visivo, confronto con rappresentazioni esistenti | ~1.5 pp |
| 5. Caso compositivo | brano realizzato con PGE, come la visualizzazione ha guidato le scelte | ~0.5 pp |
| 6. Proposta didattica | PGE come strumento per insegnare la granulare in conservatorio | ~0.5 pp |
| 7. Conclusioni | real-time come direzione aperta, altri renderer, analisi | ~0.5 pp |

---

## CIM 2026 formatting constraints

Hard requirements — do not deviate:

- **6–8 pages** (oral communication / comunicazione orale category).
- A4 portrait. Text area 17.2 × 25.2 cm. Margins: top 2.0 cm, bottom 2.5 cm, left/right 1.9 cm.
- Two columns, 8.2 cm each, 0.8 cm gutter.
- Body text: Times New Roman 10 pt. Title: 16 pt bold caps. Section heads: 12 pt bold centered.
- No headers, footers, or page numbers in submitted PDF (added by proceedings editor).
- Copyright notice in 8 pt Times New Roman at bottom-left of page 1 (via `\blfootnote` in `paper.tex`).
- References: numbered `[1]`, listed at end in alphabetical order. See `templates/cim2026_template_paper.pdf`.
- **Double-blind peer review:** submitted PDF must be anonymized. No author name, affiliation, or recognizable repo links. Use "the system described in [anonymous]" for self-references.
- Language: Italian or English. If Italian body, English abstract mandatory.
- Abstract: 150–200 words.

---

## Academic level

CIM tool/system papers (from CIM 2022/2024 proceedings): 9–21 references mixing foundational audio DSP with software documentation. Figures must be high-contrast (readable in B&W print). Include GitHub link and Zenodo DOI if available.

Tone: argumentative, not descriptive. Each section must connect back to the central thesis.

---

## Build

```bash
pdflatex paper.tex
pdflatex paper.tex   # second pass resolves cross-references
```

Output: `paper.pdf` (not tracked in git).

---

## Novel contributions e dettagli tecnici PGE

Contenuto in `wiki/overview.md` (contributi, posizionamento, differenziatori) e `wiki/sources/pge/` (analisi moduli). Struttura classi in `graph/class_diagram.puml`. Non riprodurre qui.

---

## Bibliography

Gestione bibliografica con **Zotero + Better BibTeX**.

- `refs.bib` — generato attraverso workflow add-paper, fonte di verità per LaTeX.
  Non modificare a mano. Incluso in paper.tex con `\bibliography{refs}`.
- `wiki/sources/bibliography.md` — tabella di tracciamento:
  chiavi BibTeX ↔ stato ingest wiki ↔ sezioni del paper.
  Aggiornare colonna Wiki dopo ogni ingest completato.
  Aggiornare colonna Sezioni durante la scrittura.
- PDFs in `raw/papers/` (gitignored) — importati anche in Zotero.
- Proceedings in `raw/proceedings/` (gitignored) — i paper individuali
  citati vengono aggiunti a Zotero manualmente dopo l'ingest.

Chiavi BibTeX definite manualmente in Zotero — formato:
`Cognome1Anno` / `CognomeCognome1Anno` / `Cognome1AnnoXxx`.
Usare le stesse chiavi in wiki, paper.tex e bibliography.md.

---

## Graph tooling

`make graph` regenerates both graph files from `raw/PythonGranularEngine/src/`:

```bash
make graph        # runs py2puml + pyan3, outputs to graph/
make context-all  # runs graphify on pge-src + papers + proceedings
```

Use `graph/class_diagram.puml` as structural reference when writing wiki concept pages. Do not read `call_graph.dot` whole — grep specific module names.

---

## Wiki (knowledge base)

Three layers: `raw/` (immutable) → `wiki/` (LLM-generated) → `CLAUDE.md` (schema).

### Wiki structure
- `wiki/index.md` — catalog: read before every search
- `wiki/log.md` — append-only log: add entry after every operation
- `wiki/sources/proceedings/` — `cim-survey.md` per survey trasversale;
  una pagina per ogni paper ingestito individualmente (`<autore-anno>.md`)
- `wiki/sources/papers/` — one page per PDF in `raw/papers/`
- `wiki/sources/pge/` — one page per PGE module analyzed
- `wiki/concepts/` — cross-source concept synthesis
- `wiki/overview.md` — evolving thesis

### Workflow ingest (paper PDF)
1. Read PDF with Read tool
2. Write summary page in `wiki/sources/papers/<author-year>.md`
   Schema fisso:
```markdown
   # [Autore, Anno] Titolo completo

   ## Citazione CIM
   [formato: Autore, A. (anno). Titolo. *Rivista*, vol(n), pp.]

   ## Argomento centrale
   [1-2 frasi: cosa afferma il paper]

   ## Gap o problema identificato
   [cosa manca o rimane aperto secondo l'autore]

   ## Rilevanza diretta per PGE
   [come PGE risponde o si posiziona rispetto a questo paper]

   ## Collegamento alla tesi centrale
   [come questo paper supporta o contesta il gap controllo/percezione]

   ## Sezioni del paper CIM 2026 dove citare
   [es: sezione 1, sezione 2, related work]

   ## Quote chiave
   [massimo 2-3 frasi testuali rilevanti, con numero di pagina]
```
3. Se il paper introduce nuovi elementi per tesi, differenziatori o
   tabella precursori: aggiorna `wiki/overview.md`
4. Update affected concept pages in `wiki/concepts/`
5. Aggiorna colonna Wiki in `wiki/sources/bibliography.md` per la fonte ingestita
6. Update `wiki/index.md` with new entry
7. Append entry to `wiki/log.md`
   — Una entry per paper, anche se più paper vengono ingestiti nella stessa sessione.

### Workflow ingest (PGE source module)
1. Read source file(s) from `raw/PythonGranularEngine/src/`
2. Write analysis page in `wiki/sources/pge/<module>.md`

```markdown
   # [NomeModulo] — analisi

   ## Ruolo nell'architettura
   [posizione nella pipeline: dove viene istanziato, da chi, chi lo usa]

   ## Classi principali
   [per ogni classe: attributi rilevanti, metodi chiave, pattern usato]

   ## Comportamento runtime
   [cosa succede a runtime: flusso dati, decisioni, side effects]

   ## Collegamento alla tesi centrale
   [come questo modulo risponde al gap controllo/percezione —
   se non diretto, indicare quale contribuzione implementa]

   ## Sezioni del paper CIM 2026 dove descrivere
   [es: sezione 3 Architettura, sezione 4 Partitura grafica]

   ## Domande aperte
   [aspetti non chiari dalla lettura del sorgente — da verificare]
```
3. Se il modulo chiarisce o modifica un differenziatore chiave:
   aggiorna `wiki/overview.md`
4. Create/update concept pages in `wiki/concepts/` if new cross-cutting
   concepts emerge
5. Aggiorna colonna Wiki in `wiki/sources/bibliography.md` per la fonte ingestita
6. Update `wiki/index.md`
7. Append entry to `wiki/log.md`
   — Una entry per modulo, anche se più moduli vengono ingestiti nella stessa sessione.

### Workflow ingest (paper da proceedings CIM)

Scopo duplice: (a) calibrare tono, densità tecnica e struttura dei paper della venue;
(b) identificare lavori precedenti nella tradizione CIM direttamente rilevanti per
posizionare il contributo del paper corrente.

1. Leggere il PDF con Read tool
2. Scrivere pagina in `wiki/sources/proceedings/<autore-anno>.md` con schema fisso:

```markdown
# [Autore, Anno] Titolo completo

## Citazione CIM
[formato: Autore, A. (anno). Titolo. In *Atti del N CIM*, pp. Città.]

## Categoria e lunghezza
[comunicazione orale / demo / keynote — N pagine — N riferimenti]

## Argomento centrale
[1-2 frasi: cosa afferma o dimostra il paper]

## Sistema o strumento descritto
[nome, linguaggio/ambiente, offline/real-time, anno]

## Analogia con PGE
[come questo lavoro anticipa, contrasta o si affianca a PGE —
se non rilevante, scrivere "nessuna analogia diretta"]

## Posizionamento storico
[in quale filone si inserisce: tempo differito / real-time /
notazione / controllo parametrico / altro]

## Note stilistiche
[struttura delle sezioni, densità citazioni, uso figure,
tono argomentativo vs descrittivo, apertura e chiusura tipiche]

## Sezioni del paper CIM 2026 dove citare
[es: sezione 1 Problema, sezione 2 Contesto, related work]
```

3. Se il paper è un precursore diretto: aggiorna tabella precursori
   in `wiki/overview.md`
4. Update `wiki/sources/proceedings/cim-survey.md` se non già censito
5. Aggiorna colonna Wiki in `wiki/sources/bibliography.md` per la fonte ingestita
6. Update `wiki/index.md`
7. Append entry to `wiki/log.md`
   — Una entry per paper, anche se più paper vengono ingestiti nella stessa sessione.

### Workflow query
1. Read `wiki/index.md` to find relevant pages
2. Read those pages
3. Synthesize answer with citations to wiki pages
4. **Ogni risposta sostanziale = nuovo ingest.** Archivia come pagina wiki (concepts/, sources/, o overview.md). Le esplorazioni compoundano la knowledge base esattamente come i sorgenti.

### Workflow lint
Check: orphan pages (no inbound links), contradictions between pages, stale claims superseded by newer sources, concepts mentioned but lacking own page.
Suggerisci anche: domande aperte che il wiki non risponde ancora, gap di fonti (paper non ancora ingestiti, moduli PGE non analizzati), nuove direzioni da investigare.

### Workflow add-paper

Aggiunge nuovi PDF da `inbox/` a `raw/papers/`, genera le entry BibTeX
e aggiorna `refs.bib` e `wiki/sources/bibliography.md`.
Non usare per proceedings CIM (restano in `raw/proceedings/`).

`inbox/` è la staging area: droppa i PDF trovati lì, poi esegui questo workflow.
A workflow completato `inbox/` deve essere vuota.

**Nomenclatura filename:**
- 1 autore  → `Truax_1988_Real-Time-Granular-Synthesis.pdf`
- 2 autori  → `DePoli-Piccialli_1988_Forme-Onda-Sintesi.pdf` (solo cognomi)
- 3+ autori → `Roads_2021_Architecture-Real-Time-Granular.pdf` (solo primo cognome)
- Cognomi composti → concatenati senza spazio: `DePoli`, `DiScipio`
- Titolo: prime 6–8 parole significative, no articoli/preposizioni iniziali, ASCII

**Chiave BibTeX:** `Cognome1Anno` / `CognomeCognome1Anno` / disambigua con suffisso.

1. Scansiona `inbox/` per trovare PDF da processare.
   Se vuota: notifica e termina.
   Se più file: processa uno per volta, chiedi conferma per ciascuno.
2. Leggi il PDF corrente (prime 4 pagine) con Read tool
3. Estrai: autori, anno, titolo, tipo documento, venue/journal, volume, pagine, DOI
4. Verifica e completa i campi:
   - Se DOI disponibile: `GET https://api.crossref.org/works/<DOI>` → JSON
   - Altrimenti: `web_search "<titolo>" "<primo autore>"` → cerca pagina publisher
5. Costruisci entry BibTeX in stile Better BibTeX:
   - Nomi propri/acronimi nel titolo tra `{{doppie graffe}}`
   - campo `author`: formato BibTeX standard `Cognome, Nome and Cognome, Nome` es. `author = {Truax, Barry}` / `author = {De Poli, Giovanni and Piccialli, Aldo}`
   - `file = {<path_assoluto>/raw/papers/<FILENAME>.pdf}`
   - `note = {\url{https://...}}` se URL disponibile
   - Tipo: `@article` / `@inproceedings` / `@incollection` / `@book`
1. Mostra: filename proposto, chiave, entry completa — **attendi conferma**
2. Dopo conferma:
   a. Sposta `inbox/<file>.pdf` → `raw/papers/<FILENAME>.pdf`
   b. Appendi entry a `refs.bib` (riga vuota di separazione dall'entry precedente)
   c. Aggiungi riga alla tabella Papers di `wiki/sources/bibliography.md`: `| <chiave> | <Autori> <anno> | <titolo breve> | ✗ | — |`
3. Ripeti dal passo 2 per il PDF successivo in `inbox/`

Sì, è ridondante — le checklist ripetono schemi già definiti nei workflow di ingest. Una versione snella:

---

### Workflow review-ingest

Scopo: verificare un ingest fatto da un **collega** in sessione separata.
Analisi critica — non presupporre alcuna correttezza.

**Step 0 — Contesto**
Prima di analizzare, leggi `docs/plans/setup-workspace.md` (se presente)
per identificare quali gap sono pianificati e a quale step appartengono.
Non segnalare come lacuna ciò che è previsto in uno step successivo del piano.

**Step 1 — Diff**
```bash
git diff HEAD && git diff --cached && git status
```

Nota: i file nuovi (untracked) non appaiono in git diff — vanno letti separatamente.

**Step 2 — Leggi ogni file modificato o untracked per intero.**

**Step 3 — Per ogni pagina wiki creata, verifica:**
- Schema fisso del workflow corrispondente rispettato (tutte le sezioni presenti)?
- "Rilevanza PGE" e "Collegamento tesi centrale" sono specifici, non generici?
- Sezioni CIM 2026 dove citare: compilate con numero di sezione?

**Step 4 — Verifica propagazione completa del workflow:**
`overview.md` · concept pages · `bibliography.md` colonna Wiki · `index.md` · `log.md`
— segnalare ogni passo mancante come lacuna.

---