# [Roads, 2001] Microsound — Appendice A: The Cloud Generator Program

## Posizione nel libro
Appendice A (book pp 383–388 / PDF pp 397–402). 6 pp. **Precursore architetturale diretto di PGE.**

## Argomento centrale
Cloud Generator (CG) è il programma stand-alone MacOS sviluppato da Roads + John Alexander nel 1995 (linguaggio C), basato sui programmi precedenti di Roads 1988–1992 (Synthulate, Granulate). Unifica granular synthesis sintetica e granulazione di soundfile sotto un'interfaccia GUI a singola finestra (fig. A.1). Calcola **offline** (più veloce del real-time), output AIFF o textfile numerico opzionale. Roads dichiara nel 2001 che CG diventerà presto obsoleto per cambiamenti di OS, e che la sua funzionalità è migrata a Creatovox (real-time SC2, 1998+). PGE 2026 recupera e estende il modello CG offline — *exactly* la lineage che Roads ha abbandonato.

## Architettura di Cloud Generator

- **Linguaggio/piattaforma:** C, MacOS (1995). Roads dichiara obsolescenza progressiva (G3/450 MHz, MacOS 8.6 NFPU emulation come ultima compatibilità).
- **Modello esecuzione:** **offline**, deferred-time. Calcola in RAM (max 47 sec stereo audio buffer) e poi scrive su disco. «Many clouds compute faster than real time» (p. 384).
- **Interfaccia:** GUI singolo pannello (fig. A.1) «designed to look like a laboratory signal generator» (p. 385). Tutti i parametri visibili contemporaneamente.
- **Modello compositivo:** **una cloud per session**. Più cloud → più session + montage in editing/mixing program esterno. Roads p. 385 menziona esplicitamente: «*A positive start time, such as 2.0, creates a sound file containing silence for two seconds, followed by the cloud. This feature could be useful in precisely synchronizing multiple soundfiles in an editing and mixing program.*» Workflow STEMS *ante litteram*.
- **Output:** AIFF stereo (mode normale) o textfile (numerical properties di ogni grano). Il textfile è leggibile da plotting program per produrre **partitura grafica** (vedi Hosale, sotto).
- **Visualizzazione runtime:** «*As it is calculating, CG displays the formation of the cloud as a plot of time versus frequency.*» (p. 385) — CG mostra il piano TF mentre genera. Asse Y = frequenza (canonico, non posizione-buffer come PGE).

## Parametri di controllo

Schema completo (fig. A.1):

| Parametro | Sub-controlli | Range |
|-----------|---------------|-------|
| Start Time | — | seconds (può essere ≠0) |
| Duration | — | 0.000001 – 47.0 sec (limite RAM) |
| Density | Initial / Final | g/s; 2–20 metrici, >100 noise |
| Bandlimits | High Initial/Final, Low Initial/Final | Hz; 4 angoli trapezoide freq×time |
| Cloud Type | Synchronous / Asynchronous | binario |
| Stereo Location | Initial/Final + Random checkbox | L/R + jitter |
| Amplitude | Initial / Final | percentuale 0–100 |
| Grain Duration | Initial / Final + Random checkbox (min/max) | seconds |
| Selection Order *(solo granulated)* | Random / Statistical evolution / Deterministic progression | enum |
| Waveform | Synthetic (Sine/Sawtooth/Square/User-drawn/Imported 2048-sample) **o** Granulated (path to soundfile) | enum + path |
| Output | AIFF / Text | enum |

**Note critiche:**
- *Selection Order* (p. 387) è il parametro più importante per la lineage PGE: definisce come la testina di lettura attraversa il buffer. Roads enumera tre modi: random scatter, statistical left-right drift (come probabilità crescente verso fine), strict deterministic progression. Tutti e tre sono primitive di `PointerController` PGE (vedi sotto).
- *Bandlimits trapezoide* (4 angoli) è una griglia 2D rigida: PGE generalizza con `Envelope` arbitrari su frequency_range.
- *Random checkbox* su Stereo Location e Grain Duration è meccanismo grezzo di stocastico: PGE astrae con strategie (`StochasticPointerStrategy`, dephase, ecc.).
- *Initial/Final* su quasi ogni parametro è interpolazione lineare: PGE generalizza a `Envelope` con curve arbitrarie.

## Tabella corrispondenze Cloud Generator 1995 ↔ PGE 2026

| Cloud Generator 1995 | PGE 2026 | Note |
|----------------------|----------|------|
| Linguaggio C, MacOS, GUI fissa | Python, cross-platform, **DSL YAML + LSP** | rimozione GUI ↔ riproposizione textuale (più vicino a Synthulate command-line di Roads) |
| Una cloud per session | **Streams arbitrari** in singolo YAML, orchestrati da `Generator` | scaling architetturale |
| Sync/Async cloud type binario | `DensityController` distribution sincrona / asincrona / **blend** | PGE include continuum (Truax 1988 + Roads CG) |
| Density Initial/Final lineare | `density` o `fill_factor` come **Envelope** (curve arbitrarie) | generalizzazione |
| Grain Duration Initial/Final + Random | `grain_duration` Envelope + `dephase` stocastico | strategie ortogonali |
| Bandlimits trapezoide 4 corners | `frequency_range` Envelope o `pitch_set` | continuo vs discreto |
| Stereo Location Initial/Final + Random | `pan` Envelope + `pan_spread` Envelope (`VoiceManager`) | layering 3 livelli |
| Selection Order: Deterministic | `PointerController` con `speed_ratio` costante (forward) | mappatura diretta |
| Selection Order: Statistical evolution | `PointerController` con `Envelope` su position (drift) | mappatura diretta |
| Selection Order: Random | `PointerController` con `StochasticPointerStrategy` | mappatura diretta |
| Waveform Synthetic (Sine/Saw/Square + 2048-sample import) | minimo (PGE è prevalentemente granulated, no sintesi waveform separata) | PGE rinuncia a synthetic mode |
| Waveform Granulated da soundfile | dominio principale di PGE | core funzionalità |
| Limite buffer RAM 47s | nessun limite (Csound subprocess streaming) | scaling tecnico |
| Output AIFF singolo | per-stream rendering + **STEMS** + Reaper export | contributo (3) PGE |
| Output Text (textfile numerical properties di ogni grano) | **score_visualizer** post-render | contributo (2) PGE — vedi sotto |
| Visualizzazione TF durante calc | score_visualizer post-render con asse Y = posizione-buffer | shift asse Y, da freq a buffer |
| Faster-than-real-time offline | deferred-time PGE come scelta | identità di postura |
| Cache: nessuna (calcolo da zero ogni run) | `StreamCacheManager` SHA-256 + dirty detection | contributo abilitante (3) |

## Caso paradigmatico: Hosale e la partitura grafica come uso emergente

p. 385: «*If desired, it can also produce a textfile, listing the numerical properties of each grain in a cloud. Plotting programs can read this text. In one, exceptional, case, the composer Mark-David Hosale used CG to produce texts that he transcribed into an instrumental composition.*»

Roads documenta nel 2001 un uso che CG *non aveva previsto come funzione primaria*: il textfile output → plotting program → partitura → strumento acustico. Hosale ha dimostrato che la composizione granulare può produrre **notazione strumentale**. Per il paper CIM 2026, questo è il **caso d'uso che il score_visualizer di PGE materializza come funzione primaria**, non come uso emergente.

p. 388 (sezione finale appendice): «*This option lets one save the cloud data in the form of numerical text. This text could be read by a plotting program to make a graphical score.*»

Roads articola esplicitamente «*graphical score*» come possibile output della pipeline granulare nel 2001. PGE 2026 riprende questa apertura e la materializza come componente built-in (ScoreVisualizer module). **CG anticipa concettualmente il contributo (2) di PGE.**

## Lineage architetturale (1988 → 2026)

```
1988–1992  Synthulate, Granulate (Roads, C, command-line, MacOS Music 4C)
              │
              ▼
1995       Cloud Generator (Roads + Alexander, C, GUI MacOS, single cloud)
              │ ramificazione 1998
              ├─→ 1998+  Creatovox (Roads + de Campo, real-time SC2, virtuoso) ─→  EmissionControl 2005 ─→  EC2 2021
              │                                                                                            (lineage UCSB gestural)
              │
              ▼ (lineage offline abbandonata da Roads stesso)
2026       PGE (Romano, Python, DSL YAML + LSP, multi-stream + cache + STEMS + score_visualizer)
```

PGE 2026 è **l'erede della lineage CG-offline che Roads ha abbandonato nel 1998** in favore di Creatovox real-time. Questa è una mossa narrativa precisa per il paper CIM: non si tratta di ignorare la lineage UCSB gestural (vedi `roads2021.md` su EC2), ma di recuperare la **biforcazione lasciata vuota** da Roads stesso.

## Rilevanza diretta per PGE

**Critica.** CG è il *singolo precursore architetturale più vicino* a PGE in tutta la letteratura granular. La tabella corrispondenze sopra mostra mappatura quasi 1:1 dei parametri. PGE non solo eredita il modello, ma:

1. Recupera la **lineage offline** abbandonata da Roads stesso (CG → Creatovox real-time, 1998).
2. Scala da **una-cloud-per-session** a **streams arbitrari + orchestrator** (multi-stream YAML).
3. Sostituisce GUI con **DSL+LSP** (textual, scriptable, version-controllable in git).
4. Generalizza Initial/Final lineari in **Envelope curve arbitrarie**.
5. Materializza l'apertura **textfile→graphical score** (Hosale, p. 385) come componente built-in (ScoreVisualizer).
6. Aggiunge **STEMS workflow** (cache + multi-renderer + Reaper export) come contributo originale non presente in CG.
7. Cambia asse Y partitura: CG visualizza freq×time durante calcolo (p. 385); PGE visualizza posizione-buffer×time post-calcolo come scelta semantica.

## Collegamento alla tesi centrale

**Loop lungo (Atto 3) — supporto storico.** CG materializzava già nel 1995 una pipeline deferred-time: parametri YAML-style (numerici, esplicit), generazione offline, output WAV + textfile, montage in mixing program esterno. Roads l'ha abbandonata nel 1998 per Creatovox real-time. PGE 2026 recupera la pipeline, la scala, e la rilancia come *scelta volontaria*. La tesi del loop lungo non sta inventando una postura: sta riprendendo la lineage CG e rilanciando il filone abbandonato.

**Contributo (1) DSL+LSP:** CG aveva un set di parametri rigido in GUI (~10 parametri tutti visibili insieme). PGE generalizza a YAML strutturato + tipi controllati da LSP. La discontinuità da CG è il passaggio da *GUI fissa con ~10 parametri* a *DSL aperto con strategie componibili* — più espressivo, più scriptable, ma anche più ostico per il principiante (CG era *teaching aid* per principianti, p. 383; PGE non lo è).

**Contributo (2) Partitura grafica:** CG produceva textfile leggibile da plotting program (p. 385, p. 388). Hosale lo ha usato come ponte verso partitura strumentale. PGE materializza il ponte come built-in. *L'asse Y di PGE = posizione-buffer è la novità*; il principio (text→graphical score) è già in CG.

**Contributo (3) STEMS workflow:** CG menziona esplicitamente *editing and mixing program* esterno per combinare più cloud (p. 385). PGE automatizza tutta la pipeline (per-stream cache + Reaper export) come componente integrato. La logica «multi-cloud → mixing program» di CG è la radice concettuale di STEMS PGE.

## Concetti chiave
- Stand-alone offline granular synthesis program 1995
- Front panel «laboratory signal generator» metaphor (~10 parametri tutti visibili)
- Synthetic + Granulated grain types
- Cloud type: synchronous / asynchronous
- Selection Order (granulated): Random / Statistical evolution / Deterministic
- Initial/Final lineari su quasi ogni parametro (durata, density, bandlimits, stereo, amp, grain duration)
- Output AIFF + opzionale textfile numerico
- TF visualization runtime
- Lineage abbandonata 1998 → Creatovox real-time

## Quote chiave

> «*CG merged the code from several of these programs into a single stand-alone application. It unified them under a common interface. Our goal was to create a tool for experimentation, teaching, and composition with granular techniques.*» (p. 384)

> «*As it is calculating, CG displays the formation of the cloud as a plot of time versus frequency. It produces a stereo soundfile output. If desired, it can also produce a textfile, listing the numerical properties of each grain in a cloud. Plotting programs can read this text. In one, exceptional, case, the composer Mark-David Hosale used CG to produce texts that he transcribed into an instrumental composition.*» (p. 385)

> «*Since 1998, Alberto de Campo and I moved most of the functionality of CG to the Creatovox instrument, which chapter 5 documents.*» (p. 384) — *contesto: Roads dichiara la migrazione da deferred-time a real-time, abbandonando la lineage CG. PGE 2026 recupera questa lineage.*

> «*This option lets one save the cloud data in the form of numerical text. This text could be read by a plotting program to make a graphical score.*» (p. 388)

## Sezioni del paper CIM 2026 dove citare

- **Sezione 2 (Sintesi granulare).** CG (1995) come **precursore architetturale diretto** in tabella precursori. Distinzione con linea UCSB gestural (Creatovox 1998+ → EC2 2021).
- **Sezione 3 (Architettura PGE).** Tabella corrispondenze CG ↔ PGE (sopra) come **figura/tabella del paper** se spazio lo permette. Quote p. 384 (scopo CG: experimentation/teaching/composition) come legittimazione storica del scope PGE.
- **Sezione 4 (Partitura grafica).** Quote p. 385 (Hosale + textfile→graphical score) e p. 388 (numerical text → plotting program → graphical score) come **precedente esplicito** del score_visualizer PGE. PGE materializza built-in ciò che CG offriva come uso emergente.
- **Sezione 5 (Caso compositivo).** Riferimento a Hosale come precedente di uso del granular generator come fonte per partitura → strumento acustico.
- **Sezione 6 (Conclusioni).** Quote p. 384 (migrazione 1998 a Creatovox) come **punto di bifurcazione storica**: PGE come ripresa della lineage abbandonata.
