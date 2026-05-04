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
2. **Dual renderer** (NumPy + CSound) con output bit-identico — originalità tecnica verificabile
3. **Graphic score** con Y-axis = posizione nel buffer (non frequenza) — notazione non convenzionale
4. **SHA-256 cache** per stream — soluzione ingegneristica al problema RAM citato da Di Scipio 1991

---

## Contributi del paper (tre, non quattro)

**1. YAML DSL + Language Server (PGE-ls)**
Linguaggio compositivo dichiarativo per sintesi granulare. YAML è il syntax host; lo schema semantico (parametri, envelope, strategie di variazione, architettura multi-voice, espressioni matematiche) è il domain language. PGE-ls aggiunge autocompletamento, validazione inline, hover docs — primo feedback loop durante la scrittura compositiva.

**2. Partitura grafica con asse Y = posizione nel buffer**
Non il piano tempo/frequenza. Y codifica la posizione nel buffer sorgente. Encoding visivo per grano: freccia su = playback avanti, freccia giù = inverso; colore = pitch ratio (coolwarm); opacità = volume dB; larghezza = durata grano; altezza = campioni consumati. Output: A3 landscape PDF, 30 secondi/pagina. Roads (Microsound) dichiara necessità di rappresentazioni granular-level ma non presenta strumenti implementati. Truax (1990) usa tendency masks come input visivo; la partitura PGE è l'inverso: output visivo delle decisioni compositive.

**3. Architettura multi-renderer con cache incrementale**
Renderer Csound e NumPy intercambiabili, output bit-identico da stessa spec YAML. SHA-256 fingerprint per stream — solo stream modificati ri-renderizzati. Garbage collection automatica di stream rimossi/rinominati. Export Reaper (.rpp): in modalità STEMS ogni stream diventa file audio indipendente e traccia Reaper posizionata sul timeline dall'onset dello stream.

---

## Gap da colmare (prossime ingestioni)

- Papers in `raw/papers/`: Roads 1988, Truax 1988/1990/1994, Di Scipio 1994, Gabor 1947, EmissionControl2
- Sorgente PGE: moduli `core/`, `rendering/`, `parameters/`, `strategies/`
- Atti CIM 2022 e 2024: paper demo simili per calibrare tono e struttura
