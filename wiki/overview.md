# Overview — PythonGranularEngine nel panorama CIM

Pagina di sintesi evolutiva. Aggiornare dopo ogni nuova ingestione significativa.

---

## Tesi corrente

PythonGranularEngine si inserisce nella tradizione CIM di sintesi granulare offline con controllo algoritmico ad alto livello — che inizia con Roads (CIM VI, 1985) e Di Scipio (CIM IX, 1991) — ereditandone il pattern architetturale fondamentale: separazione netta tra linguaggio di specifica e motore di rendering, con output audio come risultato di un processo in tempo differito.
Questa tradizione nasce per necessità hardware: il tempo differito è l'unico modo possibile finché il real-time è inaccessibile. Con Truax (1988) il vincolo cade — il DMX-1000 rende praticabile la granulazione in tempo reale — e il tempo differito viene deliberatamente abbandonato in favore di un paradigma compositivo basato sull'immediatezza del feedback e sull'abbandono del pensiero lineare pre-scritto. PGE compie il percorso inverso: torna volontariamente al tempo differito in un momento in cui il real-time è disponibile.
Questo ritorno non è un passo indietro. Corrisponde a una postura compositiva specifica: quella in cui composizione e studio della tecnica coincidono, e in cui il loop di feedback lungo — specifica → generazione → ascolto → riflessione → riscrittura — è lo spazio necessario per abitare gli spazi compositivi della granulazione come forma e struttura. Il giudizio drammaturgico del compositore garantisce la non-linearità del processo indipendentemente dalla scala temporale del feedback: nel real-time questo giudizio opera sull'atto immediato, nel tempo differito opera sulla riflessione tra un ciclo e l'altro. Il contributo specifico di PGE — DSL YAML come linguaggio di specifica di intenzioni parametriche, partitura grafica automatica, Language Server — è la realizzazione tecnica di questa postura.

---

## Radici teoriche

Il paradigma granulare nasce con Gabor (1947, *Nature*): il suono come matrice di grani gaussiani su piano tempo × frequenza, soggetti al principio di indeterminazione Δt · Δf ≥ 1. Xenakis (*Formalized Music*, 1971) ne formula la teoria compositiva. Roads (1978) ne fornisce la prima implementazione computer documentata — AGS, front-end per MUSIC V — introducendo l'astrazione *event* (6 coppie valore/slope) come livello di controllo sopra il grano. Roads (1988) e Truax (1988, 1990) consolidano la pratica. Truax (1994) formalizza la conseguenza compositiva: la granulazione "links frequency and time at the micro level [so it] makes it possible to treat these two variables independently at the macro level" (p. 44), separando micro-pattern d'onda e macro-evoluzione temporale. 

(questa riga è da ripensare) Truax (1988) introduce la Tabella 1 dei psychoacoustic correlates: ogni parametro di controllo (center frequency, grain duration, density, amplitude...) ha un corrispettivo percettivo che è più significativo del valore numerico grezzo come base per l'organizzazione compositiva. Nel contesto della tesi PGE, questa tabella descrive ciò che il loop lungo permette di verificare empiricamente: la relazione tra specifica parametrica e risultato percettivo, parametro per parametro, con la partitura grafica come strumento di lettura.

PGE eredita quattro conseguenze dirette: (a) il grano come unità sintetica gaussiana × sinusoide, (b) la rappresentazione bidimensionale di un suono come collezione di grani discreti — ancestor della partitura grafica, (c) la finestra 1–50 ms come range tipico, derivata dai due meccanismi di Gabor (risuonatori cocleari ~10 ms + raffinamento neurale fino a ~250 ms), (d) la separazione micro/macro come *tesi psicoacustica abilitante* del time-stretching e dell'asse Y partitura PGE = posizione-buffer.

## Precursori diretti nella tradizione CIM

| Anno | Autore | Sistema | Analogia con PGE |
|------|--------|---------|-----------------|
| 1978 | Roads | AGS (B6700 ALGOL), front-end MUSIC V | Pattern *front-end → engine sintesi* identico a `generator.py` → Csound/NumPy; event a 6 coppie valore/slope come prima radice del DSL parametrico |
| 1985 | Roads | MUSIC language, offline | Frame ≈ Stream (organizzazione sopra il grano) |
| 1991 | Di Scipio | IBM PC 286, tempo differito | Mappe non-lineari ≈ parameter strategies |
| 2003 | Autore n.d. | GeoGraphy, offline | Due livelli (sequenza + controller) ≈ Stream + Envelope |
| 2006 | Rizzuti | CSound, offline | `partitura → strumento eventi → grani` ≈ `YAML → Python → .sco` |
| 2012 | Arcella/Silvestri | C++ → CSound → audio | Pipeline quasi identica; PGE aggiunge YAML come livello intermedio |

---

## Differenziatori chiave

1. **YAML DSL** come linguaggio compositivo dichiarativo — nessun precursore CIM usa YAML
2. **Graphic score** con Y-axis = posizione nel buffer (non frequenza) — notazione non convenzionale che rende visibile da dove ogni grano pesca nel campione sorgente. Precursori: Truax 1988 (Fig. 4, overlay ASCII tendency masks su terminale — primo overlay multi-parametro concreto); Roads 1978/1988 (polygon su piano freq/tempo — metafora, non output automatico). PGE inverte il segno: la partitura è output delle decisioni, non input di controllo.
3. **Workflow STEMS con cache incrementale e export DAW** — rendering per-stream, SHA-256 fingerprint, progetto Reaper auto-generato con struttura temporale YAML già mappata; con renderer esterni a python (es. Csound) la cache rende praticabile la composizione iterativa su brani con decine di stream diminuendo drasticamente i tempi di render totale.
4. Language Server Protocol integrato — scaffolding per il loop lungo: riduce il costo cognitivo della specifica YAML, abbassa la soglia di entrata nel sistema.
5. Cache incrementale + solo/mute per stream — il ciclo modifica-un-parametro → riascolta è praticabile senza rigenerare tutto. Implementazione tecnica del loop lungo iterativo.


---

## Contributi del paper (tre, non quattro)

**1. YAML DSL + Language Server (PGE-ls)**
Linguaggio compositivo dichiarativo per sintesi granulare. YAML è il syntax host; lo schema semantico (parametri, envelope, strategie di variazione, architettura multi-voice, espressioni matematiche) è il domain language. PGE-ls aggiunge autocompletamento, validazione inline, hover docs — primo feedback loop durante la scrittura compositiva.

**2. Partitura grafica con asse Y = posizione nel buffer**
Non il piano tempo/frequenza. Y codifica la posizione nel buffer sorgente. Encoding visivo per grano: freccia su = playback avanti, freccia giù = inverso; colore = pitch ratio (coolwarm); opacità = volume dB; larghezza = durata grano; altezza = campioni consumati. Output: A3 landscape PDF, 30 secondi/pagina. Roads (1978) anticipa già la notazione come *"any polygon inscribed on the frequency-vs-time plane"*, citando *Studie II* di Stockhausen come precedente notazionale; Roads (1988) ripete la formulazione (lines, triangles, rhomboids su piano tempo/frequenza); Roads (*Microsound*, 2001) dichiara la necessità di rappresentazioni granular-level senza presentare strumenti implementati. Truax (1988, Fig. 4) presenta un overlay ASCII multi-traccia (frequency mask, duration mask, amplitude/delay envelopes) su terminale 24-line: primo precedente concreto di rappresentazione visiva multi-parametro tempo-dipendente per controllo granulare, distinto dai poligoni metaforici di Roads. Truax (1990) usa tendency masks come input visivo. Truax (1994) descrive a parole il *meccanismo* che la partitura PGE rende osservabile: il movimento della testina di lettura nel buffer rispetto al tempo di output (variable-rate granulation, ratio off:on come time-extension factor) — la scelta dell'asse Y in PGE è la rappresentazione esplicita di quel meccanismo. La partitura PGE è l'inverso delle tendency masks: output visivo delle decisioni compositive, con scelta di asse Y motivata dal caso d'uso granulazione di campioni.

**3. Workflow STEMS: rendering per-stream, cache incrementale, export DAW**
In modalità STEMS ogni stream YAML viene renderizzato come file audio indipendente (NumpyAudioRenderer; Csound disponibile come renderer esterno alternativo). Questo abilita due meccanismi: (a) cache SHA-256 per stream — il fingerprint è calcolato sul dict YAML del singolo stream, quindi solo gli stream modificati vengono ri-renderizzati tra una sessione e l'altra, con garbage collection automatica degli stream rimossi o rinominati; (b) export automatico di un progetto Reaper (.rpp) in cui ogni stem occupa una traccia con nome `stream_id`, posizionata sulla timeline secondo l'onset definito nel YAML. La modalità MIX supporta anch'essa l'export Reaper: in questo caso tutte le tracce referenziano il file mix unico, mantenendo onset e duration di ciascuno stream. Il compositore ottiene un ambiente DAW pronto per il missaggio finale o per interventi di post-produzione senza ricostruire manualmente la struttura temporale.

---

## Note per Sezione 3 del paper — YAML come DSL/IR

Il YAML di PGE non è una partitura nel senso che Truax critica ("deterministic
output, score or sequencer driven"). È una Intermediate Representation:

intenzione compositiva
        ↓
YAML DSL  ← il compositore lavora qui
        ↓
ParameterOrchestrator (Envelope, ProbabilityGate, strategie)
        ↓
grani discreti (migliaia di oggetti)
        ↓
audio
Il YAML non specifica neanche un grano. Specifica intenzioni parametriche
con range, probabilità, envelope. Due esecuzioni dello stesso YAML con
elementi stocastici attivi producono output diversi. È più vicino alle
tendency masks di Truax che a uno score Csound grezzo.
Il pattern front-end/IR risale già a Roads 1978 (AGS → MUSIC V).

---

## Gap da colmare (prossime ingestioni)

- Papers in `raw/papers/` da ingestire: Di Scipio 1994, EmissionControl2 (Roads 2021), Roads 2001 *Microsound*, Roads 2001 *Pulsars*, Roads 2005, Roads 2006, Roads 2012, De Poli/Piccialli 1988/1991, Vaggione 1991/1996/2002, Solomos 2003/2005, Caires 2004, Truax 2014
  — già ingestiti: Gabor 1947, Roads 1978, Roads 1988, Truax 1988, Truax 1990, Truax 1994
- Sorgente PGE: da ingestire: `parameters/` (parameter.py, parameter_schema.py), `strategies/` (voice e density strategies), `controllers/pitch_controller.py`, `controllers/window_controller.py`
  — già ingestiti: generator, stream, renderer, cache, parameter-orchestrator, pointer, density, voice-manager, score-visualizer
- Atti CIM 2022 e 2024: paper demo simili per calibrare tono e struttura
