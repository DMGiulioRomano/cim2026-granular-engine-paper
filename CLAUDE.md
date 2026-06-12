# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## What this repository is

LaTeX source for an **oral communication paper (6–8 pages)** submitted to **XXV CIM 2026** (Colloquio di Informatica Musicale), L'Aquila, 13–16 October 2026. The paper describes [PythonGranularEngine](https://github.com/DMGiulioRomano/PythonGranularEngine) (PGE), a deferred-time granular synthesis environment written in Python.

**Submission deadline:** 20 June 2026 via EasyChair: https://easychair.org/conferences/?conf=xxvcim2026 (rinviata dal 7 giugno)

---

## Repository structure

```
cim2026-granular-engine-paper/
├── CLAUDE.md                        ← this file (schema wiki)
├── Makefile                         ← `make graph` · `make paper` · `make examples`
├── paper/                           ← pacchetto LaTeX + esempi
│   ├── paper.tex                    ← main LaTeX source (pdflatex gira qui)
│   ├── refs.bib                     ← bibliografia (fonte di verità per LaTeX)
│   └── examples/                    ← esempi del paper (vedi paper/examples/README.md)
│       ├── README.md                ← come rendere + nota riproducibilità + DOI Zenodo
│       ├── render_example.py        ← driver: YAML → audio + partitura (PGE pinnato)
│       ├── plot.py                  ← .aif → waveform + spettrogramma B&W-safe
│       └── exN_*/                   ← una cartella per esempio (yml + score/wave/spec PDF + aif)
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

Il problema del sistema è il controllo parametrico: rendere esplicito e
leggibile il governo di una massa di grani che nessun compositore può
razionalizzare grano per grano. PGE non sintetizza grani da una primitiva
di Gabor: **granula** materiale registrato (*granular sampling* alla Lippe,
granulazione alla Dutilleux) — il parametro espressivo dominante è la
posizione di lettura nel materiale.

Il paper procede **dal basso** (direttiva maestro 2026-05-28, cfr.
`wiki/concepts/incontro-maestro-2026-05-28.md`): prima il sistema per
esempi, poi la partitura, poi la tradizione, infine le implicazioni. La
tesi del tempo differito NON è premessa: arriva in chiusura
(`sec:implicazioni`) come obiezione+risposta — Risset (precedente
filosofico), Vaggione (triangolarità input/output/operatore; déclaration
d'attribut), conseguenze tecniche (cache, stem, partitura), costo
dichiarato (performance, gesto, strumento).

Tre proposte del paper, dimensionate in `sec:tradizione` su un fondo di
«quasi nulla è nuovo», ciascuna col proprio precursore più vicino:
1. **YAML come notazione** — specifica dichiarativa completa, validata
   durante la scrittura, insieme documento di lavoro e oggetto che si
   spedisce. Dentro questo modello la rivendicazione circoscritta è la
   **fattorizzazione della deviazione per grano in ampiezza e probabilità
   indipendenti** (il gate `dephase` come asse dichiarativo, «per quanto
   ci risulta» senza precedente diretto; precursore del pattern front-end
   dichiarativo: CMask di Bartetzki — cfr.
   `wiki/concepts/deviazione-ampiezza-probabilita.md`). Il Language Server
   è strumento di contorno, non contributo di punta.
2. **Partitura grafica con asse Y = posizione di lettura nel buffer**
   (precursori: Truax 1988 Fig. 4; meccanismo descritto a parole in
   Truax 1994). Output read-only del rendering, non input di controllo.
3. **Workflow per stem**: cache incrementale per stream, export DAW
   (parenti: aspetto ricorsivo di Lippe; montaggio multitraccia di
   Vaggione).

**Correzione vincolante (maestro, ripetuta due volte):** il
non-determinismo di Truax 1988 è *economia di mezzi*, non cambio di
paradigma compositivo. MAI scrivere «real-time come cambio di paradigma» o
«rompe il vincolo»: il real-time è un modo operativo, e Truax progetta
regioni armoniche deterministiche (*Riverrun*) dentro il controllo
statistico.

This is not a technical description paper. It is an argumentative paper:
ogni aggancio teorico è ancorato a un fenomeno appena mostrato (cellula
espositiva di `sec:architettura`: domanda musicale → diff YAML → lettura
della figura → meccanismo → aggancio teorico → ponte).

Non formulare mai come "è meglio fare così". La postura è personale e
situata.

---

## Riproducibilità: andamento, non bit-identico

Il rendering PGE usa processi stocastici (tendency mask alla Truax): il modulo
`random` non è seminato in produzione, quindi due run dello stesso YAML producono
grani diversi. **Questo è voluto e non è un difetto.** Il bit-identico NON è
l'obiettivo e non interessa il paper.

La riproducibilità rilevante è l'**andamento statistico** leggibile nelle maschere:
la stessa specifica YAML produce sempre la stessa *forma* (densità, dispersione,
traiettoria del pointer, distribuzione delle voci) — i singoli grani cambiano, il
comportamento d'insieme no. Quando il paper parla di esempi riproducibili intende
questo: il YAML è spedito (chiunque lo esegue e ottiene lo stesso andamento), e una
realizzazione audio/partitura specifica accompagna come istanza. Non promettere mai
output rigenerabile identico al campione.

---

## Paper structure (6–8 pages)

Struttura descritta per **funzione e label LaTeX**: i numeri di sezione
possono cambiare, i label no — nei riferimenti (wiki, note, piani) usare
SEMPRE i label, mai «sezione N» o «§N.M».

| Label | Funzione |
|-------|----------|
| (intro) | Introduzione problem-driven: il problema del controllo, la precisazione tassonomica (granulazione, non sintesi di grani), i tre nuclei, l'annuncio del percorso dal basso. **Da riscrivere** (ancora vecchio regime) |
| `sec:architettura` | Il sistema per esempi, uno scostamento alla volta: `sec:stream-minimo` (copia fedele), `sec:griglia` (distribuzione temporale), `sec:pointer` (posizione di lettura), `sec:deviazione` (ampiezza × probabilità), `sec:voci` (voci + scatter), `sec:render` (dal `Grain` all'audio: renderer, stem, cache, DAW, LSP). Esempi ex0–ex5 come spina dorsale |
| `sec:partitura` | La partitura grafica: asse Y = posizione di lettura, output read-only. **Da scrivere** (label già referenziato) |
| `sec:tradizione` | Genealogia compressa (un paragrafo) + «quasi nulla è nuovo» + le tre proposte dimensionate |
| `sec:implicazioni` | Il tempo differito mentre il real time è disponibile: obiezione, Risset, Vaggione, conseguenze, costo. Chiude il paper |

La chiusura (eventuale mezza pagina di sviluppi futuri alla Truax *Future
Directions*) è **decisione aperta**: non darla né per inclusa né per
esclusa nello schema. Il vecchio schema a 6 sezioni è superato: la sezione
storica autonoma è compressa in `sec:tradizione`, il caso compositivo è
eliminato (gli studi restano esempi sonori per la presentazione orale), la
GUI è materia di un secondo paper.

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

## Lessico: dominio nel paper, classi solo in `wiki/sources/pge/`

Il paper usa il **lessico del dominio**, mai i nomi delle classi: il rischio
da evitare è il manuale del software. I nomi di classe restano confinati a
`wiki/sources/pge/` (analisi dei moduli) e ai campi implementativi delle
concept page. Nei campi argomentativi delle pagine wiki (Rilevanza,
Collegamento alla tesi, Sezioni dove citare) usare il termine di dominio,
eventualmente con la classe tra parentesi alla prima occorrenza.

| Classe | Termine nel paper |
|--------|-------------------|
| `PointerController` | testina / posizione di lettura |
| `DensityController` | griglia temporale, densità |
| `VoiceManager` | le voci, il blocco `voices` |
| `ProbabilityGate` | gate di probabilità (`dephase`) |
| `ParameterOrchestrator` | interpretazione della specifica (fase dichiarativa) |
| `DistributionStrategy` | campionamento per grano (uniforme/gaussiano) |
| `WindowGenerator` | finestra / inviluppo del grano |
| `score_visualizer` | partitura grafica |
| `StreamCacheManager` | cache per stream |
| `Stream`, `Grain` | stream, `Grain` (termini del dominio: ammessi) |

Le chiavi YAML (`speed_ratio`, `dephase`, `scatter`, `distribution`, …) sono
ammesse ovunque: sono la notazione, non l'implementazione.

---

## Build

```bash
make paper        # latexmk (pdf + bibtex), gira dentro paper/
make examples     # rigenera audio + partiture + plot degli esempi (serve weNeedToTalkAboutIt.wav)
make link-refs    # symlink dei file audio reali nella refs/ vuota del submodule
```

`make paper` è `.PHONY` (evita la collisione col nome della cartella `paper/`).
Output: `paper/paper.pdf` (not tracked in git). A mano: `cd paper && pdflatex paper.tex`.

**Refs audio del submodule (REGOLA OPERATIVA):** la `refs/` del submodule
`raw/PythonGranularEngine/refs/` è **sempre vuota** su clone/pull (i `.wav` sono
gitignored nel submodule). I file audio reali vivono nel repo PGE di lavoro,
sibling del repo padre: `../PythonGranularEngine/refs/`. **Dopo ogni `git pull`
o `git submodule update --init --remote`, esegui `make link-refs`** per ricreare i
symlink. Il path del repo reale è calcolato dinamicamente come sibling
`../PythonGranularEngine/refs`; override con env `PGE_REFS` su macchine con layout
diverso. `make examples` lo lancia già come prerequisito. I symlink restano
gitignored, non vengono mai committati.

Esempi del paper: `paper/examples/` — tre esempi (dephase, distribution, voices),
ciascuno con YAML sorgente + realizzazione (score/waveform/spectrogram PDF + aif
gitignored). Riproducibilità per andamento, non bit-identico — vedi
`paper/examples/README.md` e la sezione "Riproducibilità" sotto.

---

## Novel contributions e dettagli tecnici PGE

Contenuto in `wiki/overview.md` (contributi, posizionamento, differenziatori) e `wiki/sources/pge/` (analisi moduli). Struttura classi in `graph/class_diagram.puml`. Non riprodurre qui.

---

## Bibliography

Gestione bibliografica **diretta su `refs.bib`** (nessun gestore esterno:
Zotero non è in uso).

- `paper/refs.bib` — fonte di verità per LaTeX, mantenuto attraverso il
  workflow add-paper (le entry si scrivono lì direttamente). Incluso in
  `paper/paper.tex` con `\bibliography{refs}`.
- `wiki/sources/bibliography.md` — tabella di tracciamento:
  chiavi BibTeX ↔ stato ingest wiki ↔ label del paper
  (colonna derivata da `wiki/concepts/mappa-citazioni-paper.md`).
  Aggiornare colonna Wiki dopo ogni ingest completato.
- PDFs in `raw/papers/` (gitignored); fonti web come snapshot HTML/TXT,
  anch'essi gitignored.
- Proceedings in `raw/proceedings/` (gitignored).

Chiavi BibTeX definite manualmente nel workflow add-paper — formato:
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
   [come questo paper si lega a uno dei tre nuclei (YAML come notazione +
   gate ampiezza×probabilità; partitura Y=posizione di lettura; workflow
   stem/cache/DAW) o alle implicazioni del differito (sec:implicazioni)]

   ## Sezioni del paper CIM 2026 dove citare
   [label LaTeX, MAI numeri di sezione. Una funzione primaria + eventuale
   secondaria, tetto due. Es: `sec:tradizione` (primaria): …;
   `sec:deviazione` (secondaria): …]

   ## Quote chiave
   [massimo 2-3 frasi testuali rilevanti, con numero di pagina]

   ## Architettura espositiva   ← SEZIONE OPZIONALE
   [Solo per paper usati come modello stilistico bottom-up (cfr.
   wiki/concepts/modelli-stilistici-bottom-up.md). Richiede lettura diretta
   del PDF, non solo del contenuto. Dimensioni da estrarre:
   - Apertura (tecnica / teorica / storica / problem-driven)
   - Ordine sezioni con testate effettive (direzione del build)
   - Posizione prima figura tecnica e del diagramma di sistema
   - Posizione del lit-review (apertura / distribuito / sezione propria)
   - Posizione delle implicazioni teoriche (premessa / chiusura)
   - Densità ref/pagina e tipo (foundational vs vicine)
   - Forma della chiusura (tecnica / musicale / entrambe)
   - Lezione per il paper CIM 2026]
```
3. Se il paper introduce nuovi elementi per tesi, differenziatori o
   tabella precursori: aggiorna `wiki/overview.md`
4. Update affected concept pages in `wiki/concepts/`
5. Aggiorna colonna Wiki in `wiki/sources/bibliography.md` per la fonte ingestita
6. Update `wiki/index.md` with new entry
7. Append entry to `wiki/log.md`
   — Una entry per paper, anche se più paper vengono ingestiti nella stessa sessione.

### Workflow ingest (libro suddiviso per capitolo)

Variante del workflow paper PDF per libri-trattato (es. Roads 2001 *Microsound*).
Quando la fonte è un libro intero rilevante per più sezioni del paper CIM,
non comprimere in una sola pagina: ingest per capitolo + pagina hub.

**Struttura file:**
- `wiki/sources/papers/<autore-anno>.md` — pagina hub aggregatore
- `wiki/sources/papers/<autore-anno>-ch<NN>-<slug>.md` — uno per capitolo
- `wiki/sources/papers/<autore-anno>-app<X>-<slug>.md` — appendici rilevanti

**Schema pagina hub:**
```markdown
# [Autore, Anno] Titolo libro — pagina hub

## Citazione CIM
[formato monografia: Autore, A. (anno). *Titolo*. Editore. ISBN. N pp.]

## Stato ingest
[tabella: Capitolo | Pagine | File wiki | Stato ✓/◐/✗]

## Argomento centrale del libro
[2-3 frasi: tesi complessiva]

## Quote pietra-angolare per il paper CIM
[2-4 quote verbatim con numero pagina che sostengono i contributi PGE]

## Mappa capitoli → contributi PGE
[tabella: contributo paper | capitoli libro rilevanti]

## Capitoli per sezione del paper CIM 2026
[lista per label LaTeX: per ogni label del paper, capitoli libro da citare]

## Posizionamento del paper CIM rispetto al libro
[come il paper si pone rispetto al libro: eredita, contraddice, estende]
```

**Schema sub-page capitolo:**
```markdown
# [Autore, Anno] Titolo libro — Capitolo N: titolo capitolo

## Posizione nel libro
[pp. book / pp. PDF, ruolo del capitolo nel libro]

## Argomento centrale
[1-2 frasi]

## Struttura del capitolo
[lista sezioni come nel libro]

## Concetti chiave
[per ogni concetto: cosa afferma + numero pagina]

## Rilevanza diretta per PGE
[come PGE risponde o si posiziona]

## Collegamento alla tesi centrale
[loop lungo / 3 contributi]

## Quote chiave
[verbatim con numero pagina; se la quote attraversa due pagine
indicare "pp. N-N+1"]

## Sezioni del paper CIM 2026 dove citare
[mappatura su label LaTeX del paper, mai numeri]
```

Campi opzionali (aggiungere se il capitolo li giustifica): tabelle precursori
storici, tassonomie, survey implementazioni, modelli stilistici di scrittura,
punti di convergenza/divergenza con tesi PGE.

**Propagazione:**
1. Bibliography: `<chiave> | ✓ (integrale: ch1–N + appX)` quando il libro
   è coperto integralmente; `◐ ch1+ch9` durante ingest parziale
2. `overview.md`: integrare quote verbatim del libro nei differenziatori
   (non solo rinvii generici "vedi cap. N")
3. `index.md`: hub + una entry per sub-page con sintesi ≤2 righe
4. `log.md`: una entry per sessione di ingest libro
   (anche se più capitoli vengono ingestiti nella stessa sessione)

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
   [come questo modulo materializza uno dei tre nuclei (YAML come notazione
   + gate ampiezza×probabilità; partitura Y=posizione di lettura; workflow
   stem/cache/DAW) o abilita il ciclo scrivi–renderizza–ascolta; se non
   diretto, indicare il vincolo tecnico che soddisfa]

   ## Sezioni del paper CIM 2026 dove descrivere
   [label LaTeX, MAI numeri. Es: `sec:render`, `sec:partitura`]

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
[label LaTeX, MAI numeri. Una funzione primaria + eventuale secondaria,
tetto due. Es: `sec:tradizione` (primaria), `sec:partitura` (secondaria)]
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
e aggiorna `paper/refs.bib` e `wiki/sources/bibliography.md`.
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
   b. Appendi entry a `paper/refs.bib` (riga vuota di separazione dall'entry precedente)
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
- Sezioni CIM 2026 dove citare: compilate con **label LaTeX** (mai «sezione N»
  o «§N.M»), funzione primaria + eventuale secondaria, tetto due?
- **Formulazione Truax vietata assente**: nessun «real-time come cambio di
  paradigma» / «rompe il vincolo» (ammessa solo dove citata per negarla)?
- **Lessico di dominio nei campi argomentativi**: nomi di classe solo in
  `wiki/sources/pge/` o tra parentesi alla prima occorrenza (cfr. sezione
  Lessico)?

**Step 4 — Verifica propagazione completa del workflow:**
`overview.md` · concept pages · `bibliography.md` colonna Wiki · `index.md` · `log.md`
— segnalare ogni passo mancante come lacuna.

---