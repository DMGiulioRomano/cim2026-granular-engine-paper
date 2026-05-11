# [Roads, 2001] Microsound — Capitolo 5: Transformation of Microsound

## Posizione nel libro
Capitolo 5 (book pp 179–234 / PDF pp 193–248). Capitolo *pratico-tecnico*: catalogo sistematico delle tecniche di trasformazione sample-based che operano a livello microtemporale (granulazione di file, micromontaggio, convoluzione, pitch-shifting granulare, filtering/dynamics per-grano, spatializzazione per-grano).

## Argomento centrale
Tutte le trasformazioni microsonore (granulazione, micromontaggio, convoluzione, waveset distortion, spatial scattering) condividono lo stesso principio: operare su porzioni temporali brevi (1–100 ms) di un suono campionato preservandone (o modificandone deliberatamente) l'identità acustica. Il capitolo fornisce il *vocabolario operativo* delle tecniche che PGE materializza nel suo workflow per granulazione di campioni (sample-based granular).

## Struttura del capitolo
- **Micromontage** (pp 182–187)
  - Micromontage in a Graphical Sound Editing and Mixing Program (Fig 5.1: 136 file in 12 tracce su DAW; MacMix 1987 → Pro Tools)
  - Micromontage by Script (Csound `soundin` + `loscil`; Music N dialects)
  - Micromontage by Algorithmic Process (high-level cloud spec → note list: start, dur, soundfile, amplitude, location)
  - Composition with Micromontage (Vaggione *Octuor* 1982, *Thema* 1985, *Schall* 1995)
  - Assessment
- **Granulation** (pp 187–193)
  - Parametri (10 voci): selection order, pitch transposition, amplitude, spatial position, spatial trajectory, grain duration, grain density, grain envelope shape, temporal pattern (sync/async), per-grain signal processing
  - Granulation from Sound Files with Asynchronous Playback
  - Implementations: Roads MIT 1981 (C + Music 11), Truax GSAMX 1986/87 DMX-1000, Roads Granulate 1991 (Csound), Cloud Generator 1995, SuperCollider, SoundMagic FX
  - Selective Granulation (separate components → granulate one)
  - Granulation in Real Time (Truax pioneer)
  - Assessment
- **The Creatovox Synthesizer** (pp 193–196): MIDI keyboard real-time granular synth UCSB CREATE
- **Pitch Shifting on a Micro Time Scale** (pp 195–197): grain-by-grain pitch shift
- **Pitch-Time Changing by Granulation** (pp 197–202)
  - History of Digital Pitch-Time Changing (Otis/Grossman/Cuomo 1968; Lexicon Varispeech 1972; Springer Tempophon)
  - Cloud Generator: Random / Statistical evolution / Deterministic progression
  - Malah TDHS 1979, Jones/Parks 1988 (crossfade granular)
  - Lent 1989 (constant formants, zero-crossing pitch estimation, Hanning windows)
  - Gibson 1996 (variable formants, sei stadi)
- **Filtering on a Micro Time Scale** (pp 202–204): GranQ (SuperCollider, constant-Q per-grain bandpass/bandreject, 11 parametri)
- **Dynamics Processing on a Micro Time Scale** (pp 204–205): Spectral Dynamics in SoundHack (Erbe 1995)
- **Waveset and Wavecycle Distortions** (pp 205–209): Wishart catalogo (transposition, reversal, shaking, inversion, omission, shuffling, distortion, substitution, harmonic distortion, averaging, enveloping, transfer, interleaving, time-stretching, time-shrinking, normalizing)
- **Convolution of Microsounds** (pp 209–227)
  - Status of Convolution / Impulse Response and Cross-Synthesis
  - Theory (formula matematica, law of convolution, FIR filtering)
  - Fast and Instant Convolution (Stockham 1969; Picialli instant convolution per pitch-synchronous resynthesis)
  - Real-Time Implementation (block-transform, sectioned)
  - Musical Significance: Cross-Filtering, Spatiotemporal Effects (echo, time-smearing, reverberation), Noise Reverberation, Modulation as Convolution, Excitation/Resonance Modeling
  - Rhythm Input, Convolution and Pulsar Synthesis
- **Spatialization of Sound Particles** (pp 222–233)
  - Virtual Spaces, Scattering Particles in Virtual Spaces, Per-Grain Reverberation
  - Spatialization by Modulation with Particles
  - Convolutions with Clouds of Sonic Particles (effect of cloud envelope, particle envelope, particle duration, particle frequency, window type)
  - Particle Pluriphony in Physical Spaces (GMEBaphone/Cybernéphone; Creatophone CREATE UCSB)
- **Summary** (pp 233–234)

## Concetti chiave per PGE

### Micromontage by algorithmic process come anticipatore del DSL YAML

Roads p. 185 mostra un esempio di formato testuale per micromontaggio algoritmico (programma del 1993):
```
Start    Duration  Soundfile  Amplitude  Location
0.137    0.136     8          0.742      0.985
0.281    0.164     10         0.733      0.899
0.346    0.132     12         0.729      0.721
...
```
È esattamente la struttura semantica di uno stream YAML PGE: una lista di eventi con onset, duration, sample reference, amplitude, pan. La differenza: PGE astrae il singolo grano via Envelope/strategy invece di enumerarlo. Roads stesso categorizza i tre metodi (graphical / by script / by algorithm) — PGE estende il terzo con un DSL strutturato e validato.

> «*Instead of specifying each particle manually, however, a computer program handles their extraction and time-scattering. The program reads a high-level specification of the montage from the composer. It then generates all the note statements needed to realize the montage. The high-level specifications might include a list of sound files, the location and length of the segments to be extracted, the overall tendencies of the montage, and so on.*» (p. 185)

Questa è la definizione canonica di YAML PGE *ante litteram*: alto livello → generazione automatica di migliaia di micro-eventi.

### Granulation parameters list (p. 188) ↔ YAML PGE schema

Roads enumera 10 parametri di granulazione:

| Roads 2001 (p. 188) | PGE (YAML schema) |
|---------------------|-------------------|
| Selection order from input stream | `pointer.strategy` (sequential / quasi-sequential / random) |
| Pitch transposition of grains | `pitch.value` + `pitch.envelope` |
| Amplitude of grains | `volume.value` + `volume.envelope` |
| Spatial position | `pan.value` + `pan.envelope` |
| Spatial trajectory | `pan.envelope.strategy` (Linear / Curve / Stochastic) |
| Grain duration | `duration.value` + `duration.envelope` |
| Grain density (grains/sec) | `density.value` + `density.envelope` |
| Grain envelope shape | `window` parametro (Gaussian / Hann / Cosine taper / Trapezoid) |
| Temporal pattern (sync/async) | `dephase` parametro (0 = synchronous; > 0 = stochastic offset) |
| Per-grain signal processing | out-of-scope PGE (delegato a DAW via STEMS) |

Corrispondenza quasi 1:1. PGE non inventa parametri: implementa lo standard Roads 2001 + aggiunge il livello DSL/strategy di astrazione.

### Quote di endorsement deferred granulation (p. 188)

> «*Asynchronous playback from a sound file allows much more freedom than real-time granulation of a sound coming from a microphone. Because the sound to be granulated resides in a file, we have the flexibility of extracting individual grains in any order: sequential, reversed, random, statistical evolution, or in an arbitrary succession.*» (p. 188)

Roads stesso esplicita il vantaggio della granulazione *asincrona da file* (= deferred): controllo arbitrario dell'ordine di estrazione (impossibile in real-time, dove la testina di lettura non può guardare nel futuro — quote Truax 1994a p. 192: «*Granulation may be many things, but it is not omniscient.*»). Questo è il razionale tecnico diretto del workflow PGE: leggere da file consente strategie di puntatore arbitrarie che il real-time non permette.

### Conclusione finale del capitolo (p. 234) — pietra angolare per Sezione 6 paper

> «*By the 1980s, software made it possible to begin to develop a catalog of new digital transformations. Automatic segmentation of sound material into microtemporal particles is the first step in many of these techniques. Recently we have reached a fortunate stage where many transformations operate in real time on inexpensive computers. Besides increasing the efficiency of studio work, this means that powerful sound transformations can be performed in a virtual or physical concert hall.*»
>
> «*Circuit speed is less of a limiting factor, but no matter how fast computers become, certain transformations will always be too difficult for a human being to manipulate effectively in real time (Vaggione 1996c). Musical interfaces that offer control through envelopes, presets, and other automation functions will assist composers in planning detailed and elaborate transformations.*» (p. 234)

Roads articola nel 2001 — quando il real-time è ormai disponibile (Truax 1988 ha già rotto il vincolo da 13 anni) — la **necessità di interfacce dichiarative (envelopes, presets, automation) per trasformazioni che eccedono la capacità di manipolazione real-time umana**. La velocità del calcolo non è il vincolo: il vincolo è cognitivo-compositivo. Roads/Vaggione legittimano *esplicitamente* il programma PGE: YAML DSL = «musical interface offering control through envelopes, presets, and other automation functions». Citazione cardine per Sezione 6 (conclusioni) e per la difesa del posizionamento PGE.

### Convolution e spatialization come out-of-scope PGE

Cap. 5 dedica ~25 pagine a convoluzione, cross-synthesis, spatial scattering, per-grain reverberation. Queste tecniche sono **fuori dallo scope diretto di PGE 2026**: PGE rende ogni grano come overlap-add di waveform (con o senza pitch shift) e lascia ogni post-processing (convoluzione, reverberation, spatialization stereo/multichannel oltre il pan) al DAW host via workflow STEMS. Cap. 5 documenta cosa PGE *non* fa — utile per il paper per delimitare lo scope ed evitare ambiguità con sistemi più ampi.

### Waveset / wavecycle distortions

Wishart catalogo (pp 205–208) è una direzione *complementare* a PGE: opera su unità definite da zero-crossings invece che da finestre temporali fisse. PGE non implementa waveset operations.

### Pitch shifting on micro time scale (p. 197)

> «*Digital techniques let us alter the playback speed instantaneously, over any time scale. It is possible, for example, to pitch shift to different intervals on a grain-by-grain basis. The main parameters being the amount of pitch shift (in percent, semitones, or cents, where a 5.9% pitch shift represents one semitone or 100 cents), grain duration, and grain overlap.*»

Modello concettuale del `pitch_controller` PGE: pitch ratio per-grano, con il pitch_envelope che può variare nel tempo di stream.

## Rilevanza diretta per PGE

**Sezione 3 (Architettura PGE).** Cap. 5 fornisce la corrispondenza parametri Roads ↔ YAML schema PGE (tabella sopra). PGE non innova al livello parametri: innova al livello *linguaggio di specifica* e *strategie di variazione*. Citazione p. 185 (micromontaggio algoritmico) come precursore concettuale diretto del DSL YAML.

**Sezione 1 (Introduzione) e Sezione 6 (Conclusioni).** Quote p. 234 come pietra angolare per la difesa della scelta deferred + DSL: Roads stesso dichiara che envelopes + presets + automation sono necessari per gestire trasformazioni che eccedono la manipolazione real-time umana. PGE = realizzazione contemporanea di questo programma.

**Sezione 2 (Sintesi granulare).** Quote p. 188 («*asynchronous playback from sound file allows much more freedom*») + Truax p. 192 («*not omniscient*») come razionale tecnico-compositivo della modalità deferred. Roads + Truax convergono nel 2001 sul punto: deferred consente operazioni che il real-time non può fare.

**Delimitazione scope.** Convoluzione, cross-synthesis, waveset distortions, spatial scattering avanzato — out-of-scope PGE. Utile per il paper per chiarire cosa PGE *non* è (non è un sample-based granular processor full-stack come SoundHack/Composer Desktop Project): è un *engine compositivo* deferred che lascia il post-processing al DAW.

## Collegamento alla tesi centrale

**Tesi loop lungo.** Cap. 5 implicitamente sostiene la tesi: tutte le tecniche descritte (specialmente convoluzione con cloud di particelle, micromontaggio con migliaia di sound files, GranQ con 11 parametri tempo-varianti) richiedono iterazione e sperimentazione su parametri non manipolabili gestualmente. La conclusione p. 234 lo dice esplicitamente. PGE = strumento progettato attorno a questa necessità.

**Contributo (1) DSL YAML.** Pp. 184–185 documentano i tre modelli storici di micromontaggio: graphical (DAW), by script (Csound), by algorithmic process (high-level spec). PGE estende il terzo con strutturazione semantica (schema validato), Language Server, ed espressioni matematiche embedded. La quote p. 185 («*high-level specification of the montage*») è la definizione *ante litteram* del programma DSL.

**Contributo (3) STEMS workflow.** Cap. 5 mostra che il dominio delle trasformazioni microsonore copre operazioni che eccedono il singolo grain envelope: convoluzione, spatialization, dynamics processing. PGE delega questi a DAW via STEMS — scelta architetturale che permette di concentrarsi sul livello «sintesi granulare deferred di campioni» lasciando il post-processing all'ecosistema audio engineering esistente. Coerente con la visione p. 234 (envelopes + presets + automation come interfacce).

**Differenziatore frame rate per-voice.** Cap. 5 mostra (Fig 5.1 micromontaggio 136 file in 12 tracce, distinti per durata e timing) che la pratica reale richiede density/duration eterogenee per traccia/stream. PGE supporta questo via ParameterOrchestrator + Stream multipli con strategie indipendenti.

## Quote chiave

> «*Instead of specifying each particle manually, however, a computer program handles their extraction and time-scattering. The program reads a high-level specification of the montage from the composer. It then generates all the note statements needed to realize the montage.*» (p. 185) — *definizione canonica del DSL ante litteram.*

> «*Asynchronous playback from a sound file allows much more freedom than real-time granulation of a sound coming from a microphone. Because the sound to be granulated resides in a file, we have the flexibility of extracting individual grains in any order: sequential, reversed, random, statistical evolution, or in an arbitrary succession.*» (p. 188) — *razionale tecnico deferred granulation.*

> «*Granulation may be many things, but it is not omniscient.*» (Truax 1994a, riportato p. 192) — *limite intrinseco del real-time: la testina non può guardare nel futuro.*

> «*Circuit speed is less of a limiting factor, but no matter how fast computers become, certain transformations will always be too difficult for a human being to manipulate effectively in real time (Vaggione 1996c). Musical interfaces that offer control through envelopes, presets, and other automation functions will assist composers in planning detailed and elaborate transformations.*» (p. 234) — *pietra angolare per Sezione 6: legittimazione esplicita del DSL come interfaccia compositiva.*

> «*Our principal metaphor for musical composition must change from one of architecture to one of chemistry. We may imagine a new personality combing the beach of sonic possibilities, not someone who selects, rejects, classifies and measures the acceptable, but a chemist who can take any pebble, and, by numerical sorcery, separate its constituents, and merge the constituents from two quite different pebbles ...*» (Wishart 1994, riportato p. 233) — *metafora del compositore-chimico = sperimentazione iterativa con parametri micro; sintonia con tesi loop lungo.*

> «*Particle pluriphony [...] When we project these microspatial effects in a physical space over widely separated loudspeakers, these tiny virtual displacements appear far larger, and the sounds dance.*» (p. 233) — *spazializzazione per-grano come confine dello scope PGE (delegato a DAW + diffusione live).*

## Sezioni del paper CIM 2026 dove citare

- **Sezione 1 (Introduzione).** Quote Truax p. 192 («not omniscient») come supporto per la limitazione intrinseca del real-time.
- **Sezione 2 (Sintesi granulare).** Quote p. 188 (asynchronous playback freedom). Riferimento generale a cap. 5 per il dominio delle tecniche granular sample-based.
- **Sezione 3 (Architettura PGE).** Quote p. 185 (high-level specification → note list) come precursore concettuale diretto del DSL YAML. Tabella parametri Roads vs PGE.
- **Sezione 4 (Partitura grafica).** Fig 5.1 (micromontaggio 136 file in DAW) come precursore visivo della rappresentazione multi-stream; PGE differisce per scelta dell'asse Y (posizione-buffer vs traccia).
- **Sezione 6 (Conclusioni).** Quote p. 234 (envelopes + presets + automation) come pietra angolare per la legittimazione del DSL deferred come scelta architetturale matura, non come limitazione tecnologica.
