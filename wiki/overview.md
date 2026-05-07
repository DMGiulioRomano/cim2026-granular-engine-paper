# Overview — PythonGranularEngine nel panorama CIM

Pagina di sintesi evolutiva. Aggiornare dopo ogni nuova ingestione significativa.

---

## Tesi corrente

PythonGranularEngine si inserisce in una tradizione CIM di sintesi granulare **offline con controllo algoritmico ad alto livello**, che inizia con Roads (CIM VI, 1985) e Di Scipio (CIM IX, 1991). Il contributo specifico è la separazione netta tra **linguaggio di specifica** (YAML DSL con espressioni matematiche) e **rendering** (NumPy o Csound), con output bit-identico tra i due backend.

---

## Precursori diretti nella tradizione CIM

| Anno | Autore | Sistema | Analogia con PGE |
|------|--------|---------|-----------------|
| 1985 | Roads | MUSIC language, offline | Frame ≈ Stream (organizzazione sopra il grano) |
| 1991 | Di Scipio | IBM PC 286, tempo differito | Mappe non-lineari ≈ parameter strategies |
| 2003 | Autore n.d. | GeoGraphy, offline | Due livelli (sequenza + controller) ≈ Stream + Envelope |
| 2006 | Rizzuti | CSound, offline | `partitura → strumento eventi → grani` ≈ `YAML → Python → .sco` |
| 2012 | Arcella/Silvestri | C++ → CSound → audio | Pipeline quasi identica; PGE aggiunge YAML come livello intermedio |

---

## Differenziatori chiave

1. **YAML DSL** come linguaggio compositivo dichiarativo — nessun precursore CIM usa YAML
2. **Graphic score** con Y-axis = posizione nel buffer (non frequenza) — notazione non convenzionale
3. **Workflow STEMS con cache incrementale e export DAW** — rendering per-stream, SHA-256 fingerprint, progetto Reaper auto-generato con struttura temporale YAML già mappata; con renderer esterni a python (es. Csound) la cache rende praticabile la composizione iterativa su brani con decine di stream diminuendo drasticamente i tempi di render totale.
---

## Contributi del paper (tre, non quattro)

**1. YAML DSL + Language Server (PGE-ls)**
Linguaggio compositivo dichiarativo per sintesi granulare. YAML è il syntax host; lo schema semantico (parametri, envelope, strategie di variazione, architettura multi-voice, espressioni matematiche) è il domain language. PGE-ls aggiunge autocompletamento, validazione inline, hover docs — primo feedback loop durante la scrittura compositiva.

**2. Partitura grafica con asse Y = posizione nel buffer**
Non il piano tempo/frequenza. Y codifica la posizione nel buffer sorgente. Encoding visivo per grano: freccia su = playback avanti, freccia giù = inverso; colore = pitch ratio (coolwarm); opacità = volume dB; larghezza = durata grano; altezza = campioni consumati. Output: A3 landscape PDF, 30 secondi/pagina. Roads (Microsound) dichiara necessità di rappresentazioni granular-level ma non presenta strumenti implementati. Truax (1990) usa tendency masks come input visivo; la partitura PGE è l'inverso: output visivo delle decisioni compositive.

**3. Workflow STEMS: rendering per-stream, cache incrementale, export DAW**
In modalità STEMS ogni stream YAML viene renderizzato come file audio indipendente (NumpyAudioRenderer; Csound disponibile come renderer esterno alternativo). Questo abilita due meccanismi: (a) cache SHA-256 per stream — il fingerprint è calcolato sul dict YAML del singolo stream, quindi solo gli stream modificati vengono ri-renderizzati tra una sessione e l'altra, con garbage collection automatica degli stream rimossi o rinominati; (b) export automatico di un progetto Reaper (.rpp) in cui ogni stem occupa una traccia con nome `stream_id`, posizionata sulla timeline secondo l'onset definito nel YAML. La modalità MIX supporta anch'essa l'export Reaper: in questo caso tutte le tracce referenziano il file mix unico, mantenendo onset e duration di ciascuno stream. Il compositore ottiene un ambiente DAW pronto per il missaggio finale o per interventi di post-produzione senza ricostruire manualmente la struttura temporale.

---

## Gap da colmare (prossime ingestioni)

- Papers in `raw/papers/`: Roads 1988, Truax 1988/1990/1994, Di Scipio 1994, Gabor 1947, EmissionControl2
- Sorgente PGE: da ingestire: `parameters/` (parameter.py, parameter_schema.py), `strategies/` (voice e density strategies), `controllers/pitch_controller.py`, `controllers/window_controller.py`
  — già ingestiti: generator, stream, renderer, cache, parameter-orchestrator, pointer, density, voice-manager, score-visualizer
- Atti CIM 2022 e 2024: paper demo simili per calibrare tono e struttura
