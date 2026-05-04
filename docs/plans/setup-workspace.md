# Piano: configurazione workspace CIM 2026

Esegui questo piano in ordine. Ogni step è indipendente e verificabile.  
Repo: `cim2026-granular-engine-paper/`. Submodule PGE in `raw/PythonGranularEngine/`.  
CLAUDE.md aggiornato — leggilo prima di iniziare.

---
### usare LLM wiki di karpathy
---

## Step 2 — Crea struttura cartelle semantic/ e literature/

```bash
mkdir -p docs/semantic
mkdir -p docs/literature/concepts
```

Crea file placeholder vuoti:
```bash
touch docs/semantic/architecture.md
touch docs/semantic/dsl-yaml.md
touch docs/semantic/graphic-score.md
touch docs/semantic/renderer-cache.md
touch docs/literature/index.md
touch docs/literature/roads1988.md
touch docs/literature/roads_microsound.md
touch docs/literature/truax1988.md
touch docs/literature/truax1990.md
touch docs/literature/concepts/granular-synthesis.md
touch docs/literature/concepts/tendency-masks.md
```

---

## Step 3 — Scrivi docs/semantic/architecture.md

Input da leggere (in ordine):
1. `graph/class_diagram.puml` — struttura classi PGE (py2puml)
2. `context/pge-src/graphify-out/GRAPH_REPORT.md` — sintesi graphify (se generato nello step 1)
3. `CLAUDE.md` sezione "Novel contributions" — cosa mappare

Schema del file da produrre:

```markdown
# Architettura PGE — layer semantico

## Pipeline completa
[descrivi YAML → Generator → Stream/Cartridge → Renderer → audio + ScoreVisualizer]

## Classi principali e loro ruolo nel paper

### Grain
[attributi: onset, duration, pointer_pos, pitch_ratio, volume, pan, sample_table, envelope_table]
[ruolo paper: unità atomica della sintesi granulare — corrisponde al "grano" di Xenakis/Roads]

### Stream
[attributi: voices, grains, generated]
[ruolo paper: sequenza di grani con strategia condivisa — livello intermedio della gerarchia Truax]

### Cartridge
[ruolo paper: sezione compositiva — livello alto della gerarchia]

### Generator
[ruolo paper: orchestratore top-level, punto d'ingresso della pipeline YAML]

### ScoreVisualizer
[ruolo paper: CONTRIBUZIONE 2 — asse Y = posizione nel buffer, non frequenza]
[collegamento letteratura: Roads (Microsound) afferma necessità rappresentazioni granulari, non implementa]

### StreamCacheManager
[ruolo paper: CONTRIBUZIONE 3 — SHA-256 fingerprint per stream, skip unchanged]

### CsoundRenderer / NumpyAudioRenderer
[ruolo paper: CONTRIBUZIONE 3 — dual renderer, output bit-identical]

### ParameterOrchestrator + strategy pattern
[ruolo paper: CONTRIBUZIONE 1 — implementazione DSL YAML, strategie di variazione parametrica]

## Gerarchia di controllo (Truax 1990)
[mappa livelli Truax → classi PGE:
  - livello micro (grano) → Grain
  - livello meso (stream) → Stream + controllers
  - livello macro (composizione) → Cartridge + Generator]
```

---

## Step 4 — Scrivi docs/literature/index.md

Schema fisso da usare per ogni entry:

```markdown
| File | Autore | Anno | Tag | Rilevanza per paper |
|------|--------|------|-----|---------------------|
| roads1988.md | Roads | 1988 | #granular #introduzione | sezione 1 Problema |
| roads_microsound.md | Roads | 2001 | #granular #notazione #densità | sezione 4 Partitura |
| truax1988.md | Truax | 1988 | #realtime #dsp #granular | sezione 2 Contesto |
| truax1990.md | Truax | 1990 | #composizione #gap #controllo | TESI CENTRALE |
```

---

## Step 5 — Scrivi i file docs/literature/

Schema fisso per ogni file (usa questo template, non inventare strutture diverse):

```markdown
# [Autore, Anno] Titolo completo

## Citazione
[formato CIM: Autore, A. (anno). Titolo. *Rivista*, vol(n), pp.]

## Argomento centrale
[1-2 frasi: cosa afferma il paper]

## Gap o problema identificato
[cosa manca o cosa rimane aperto secondo l'autore]

## Rilevanza diretta per PGE
[come PGE risponde o si posiziona rispetto a questo paper]

## Sezioni del paper CIM dove citare
[es: sezione 1, sezione 2, related work]

## Quote chiave
[massimo 2-3 frasi testuali rilevanti, con numero di pagina se disponibile]
```

Priorità di scrittura:
1. `truax1990.md` — tesi centrale, più urgente
2. `roads_microsound.md` — contribuzione 2 (notazione grafica)
3. `roads1988.md` — sezione introduttiva
4. `truax1988.md` — contesto tecnico real-time
5. `docs/literature/concepts/granular-synthesis.md` — glossario termini usati nel paper

Per leggere i PDF: si trovano in `raw/papers/`. Se non presenti, chiedere all'utente di verificare.

---

## Step 6 — Scrivi docs/semantic/dsl-yaml.md

Input: leggi `raw/PythonGranularEngine/CLAUDE.md` + un file YAML di esempio in `raw/PythonGranularEngine/` (cerca `*.yml` o `*.yaml`).

Contenuto da produrre:
- Schema YAML: campi principali, struttura envelope, espressioni matematiche al parse time
- Differenza tra "YAML generico" e "DSL compositiva YAML-hosted"
- Ruolo di PGE-ls (https://github.com/DMGiulioRomano/PGE-ls): autocompletamento, validazione inline, hover docs
- Come questo risponde al gap controllo/percezione: scrittura compositiva con feedback immediato

---

## Step 7 — Scrivi docs/semantic/graphic-score.md

Input: leggi `graph/class_diagram.puml` per attributi di `ScoreVisualizer`. Poi leggi sorgente direttamente:
```bash
find raw/PythonGranularEngine/src -name "score_visualizer.py" | head -1
```

Contenuto da produrre:
- Perché Y = posizione nel buffer e non frequenza (argomento teorico)
- Encoding visivo completo: colore, opacità, larghezza, altezza, direzione freccia
- Confronto con tendency masks di Truax (input visivo vs output visivo)
- Confronto con Roads: necessità affermata vs strumento implementato
- Output: PDF A3 landscape, 30 sec/pagina, generato automaticamente con l'audio

---

## Step 8 — Scrivi docs/semantic/renderer-cache.md

Input: cerca in sorgente PGE:
```bash
find raw/PythonGranularEngine/src -name "stream_cache_manager.py"
find raw/PythonGranularEngine/src -name "*reaper*"
```

Contenuto da produrre:
- Logica SHA-256: cosa viene fingerprinted, quando si ricalcola
- Garbage collection stream rimossi/rinominati
- Dual renderer: perché output identico è una contribuzione (portabilità, riproducibilità)
- Export Reaper .rpp: struttura del file, come stream → tracce posizionate per onset

---

## Step 9 — .gitignore (già aggiornato)

`.gitignore` è già aggiornato con:
```
context/*/graphify-out/graph.json
context/*/graphify-out/graph.html
context/*/graphify-out/cache/
context/*/graphify-out/cost.json
context/*/graphify-out/manifest.json
```
`GRAPH_REPORT.md` e `wiki/` restano tracciati.

---

## Step 10 — requirements.txt (già aggiornato)

`graphifyy` è già in `requirements.txt`. Esegui `make install` per installarlo.

---

## Verifica finale

Al termine di tutti gli step, il repo deve avere:

```
graph/
  class_diagram.puml               ✓ già presente
  call_graph.dot                   ✓ già presente
context/
  pge-src/graphify-out/
    GRAPH_REPORT.md                ✓ generato step 1
docs/semantic/
  architecture.md                  ✓ scritto step 3
  dsl-yaml.md                      ✓ scritto step 6
  graphic-score.md                 ✓ scritto step 7
  renderer-cache.md                ✓ scritto step 8
docs/literature/
  index.md                         ✓ scritto step 4
  roads1988.md                     ✓ scritto step 5
  roads_microsound.md              ✓ scritto step 5
  truax1988.md                     ✓ scritto step 5
  truax1990.md                     ✓ scritto step 5
  concepts/
    granular-synthesis.md          ✓ scritto step 5
    tendency-masks.md              ✓ scritto step 5
```

Dopo la verifica: aggiorna `docs/plans/next-session.md` con il piano per la scrittura del paper.
