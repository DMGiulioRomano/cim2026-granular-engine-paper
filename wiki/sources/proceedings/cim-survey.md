# Sintesi granulare e granulazione negli Atti CIM — Survey

Survey sistematico su tutti i 23 volumi degli Atti CIM disponibili in `raw/proceedings/`.
Fonte: estrazione testo con `pdftotext`, ricerca su radice `granul`.

---

## Tutti gli articoli trovati, per anno

### 1983 — V CIM

**Bruno Fagarazzi** — *"Programma per il controllo di parametri timbrici mediante il volo di Levy applicato al MUSIC5"*
Applica volo di Lévy a diverse tecniche tra cui sintesi granulare (menzione: "additiva, granulare, modulazione di frequenza, distorsione non lineare"). Non articolo dedicato.

---

### 1985 — VI CIM

**Curtis Roads** — *"Granular Synthesis of Sound: Past Research and Future Prospects"*
Articolo dedicato. Panoramica storica, basi teoriche (Gabor 1946–47), strumento granulare semplice (oscillatore sinusoidale + inviluppo quasi-gaussiano). Introduce il concetto di **frame** come unità di organizzazione superiore al grano: ogni frame aggiorna i parametri per centinaia di grani. Problema esplicito: densità 1000–5000 grani/minuto richiede `d × n` valori di controllo → necessità di un livello di organizzazione più alto. Granulazione temporale di suoni registrati. Pipeline: MUSIC language, **offline**. Vedi [[roads1985]].

---

### 1988 — VII CIM

**G. De Poli, A. Piccialli** — *"Forme d'onda per la sintesi granulare sincrona"* (pp. 69–73)
Articolo dedicato. Analisi forme d'onda ottimali per sintesi granulare **pitch-synchronous** (sincrona col periodo). Grani come risposte all'impulso di filtri FIR passa-banda a fase lineare; prototipo passa-basso tabulato (gaussiana/secante iperbolica/Nuttall/Gegenbauer/Kaiser/Dolph-Chebyshev) + trasformazioni dinamiche (scaling per bandwidth, shift per frequenza formante, modulazione d'ampiezza, distorsione non-lineare). Intervallo tra grani 10–20 ms (asincrono → problemi continuità di fase nei suoni quasi periodici). Sintesi additiva per formanti: una sequenza di grani per ogni zona dello spettro. Pattern *precompute-once / reuse-many* per la forma d'onda prototipo. Riferimenti: Roads (1978/1985), Truax DMX-1000 (ICMC 86), VOSIM, Rodet, Liénard. **Offline.** Vedi [[depoli-piccialli1988]].

---

### 1989 — VIII CIM

**Immacolata Ortosecco, Aldo Piccialli** — *"Sintesi granulare e metodi di analisi / Sintesi granulare e Digital Signal Processing"* (pp. 58–67)
Articolo dedicato. Connessione tra sintesi granulare, wavelets e DSP. Identificazione wavelet=grano (via Roads 1985) come base teorica rigorosa. Sistema di analisi: banco di filtri (channel vocoder) derivato da wavelet quasi-ortogonale di Kronland-Martinet e da wavelet ortonormale propria; implementazione su scheda Ariel TMS 32025 / PC AT. Wavelet prototipo tabulata su 4096 campioni (pattern precompute-once / reuse-many). Cita esplicitamente De Poli/Piccialli 1988. **Offline.** Vedi [[ortosecco-piccialli1989]].

---

### 1991 — IX CIM

**Agostino Di Scipio** — *"Caos deterministico, composizione e sintesi del suono"*
Keywords: composition, granular synthesis, timbre, deterministic chaos, non-linear dynamics.
Articolo dedicato (applicazione). Sistemi dinamici non-lineari per controllo parametri granulari: ampiezza, durata, posizione nel buffer, frequenza di granulazione. Mappa logistica e distribuzioni biparametriche. Granulazione di suoni reali (campionati). Granulazione a cascata. Esplicita: **"procedure attualmente implementate in tempo differito, su IBM PC 286"**. Implementazione in tempo reale non implementata per limiti di RAM (granulazione di suoni reali "problema attualmente insormontabile").
Vedi [[discipio1991]].

---

### 1993 — X CIM

**A. Di Scipio, G. Tisato** — *"Granular synthesis with Interactive Computer Music System"* (pp. 159–165)
Articolo dedicato. Sistema **ICMS** (Tisato, prima release 1975, mainframe IBM 9121 time-sharing al Centro di Calcolo Ateneo di Padova) con sottomenu `GRANULAR PROC.` integrato nel `SOUND PROCESSING` menu. Pipeline 3-step per grano (pointer → read n samples → envelope/write target) come riformulazione: la sintesi granulare è caso particolare della granulazione (cambia solo il contenuto del source file). 7 opzioni di controllo del puntatore: passo costante/variabile, moto Browniano (1/f²), distribuzione gaussiana, equazioni non-lineari (logistica, Verhulst, May, "discubic"). Tendency-mask control con sampling gaussiano per grain duration/delay/amplitude/file-portion. Layering ricorsivo arbitrario di stream con mixing coefficients. Phase-level switches (reverse/repetition/offset/inversion) ad attivazione 50%-probabilistica. Brano *zeitwerk (l'orizzonte delle cose)* (1992) con 8 sinusoidi a frequenza fissa come source. **Offline.** Quote pietra-angolare p. 165: *"a single rule may instantiate multiple operations [...] step towards the abstract"* = programma DSL ante litteram CIM 1993. Vedi [[discipio-tisato1993]].

**C. Lippe** — *"Real-time Control of Granular Sampling via Nonlinear Processes Using the IRCAM Signal Processing Workstation"* (pp. 178–182)
Articolo dedicato. ISPW IRCAM + Max come interfaccia utente. Distingue *granular synthesis* (forme d'onda sintetiche, elektronische Musik) da *granular sampling* (porzioni di suono campionato, musique concrète) come categorie tassonomicamente separate (pp. 179–180); l'onset time nel sample sorgente è "of primary importance" (p. 180), non parametro commutativo. Controllo via tendency masks (p. 181, *"constantly moving windows with varying sizes in which grains are statistically chosen"*) + chaotic equations + signal-driven (pitch/amplitude tracking del clarinetto in *Music for Clarinet and ISPW*). Recursive aspect: real-time mixing dell'output di task simultanee e reuse come sample sorgenti (p. 180). Ringrazia Di Scipio negli acknowledgements. **Real-time.** Vedi [[lippe1993]].

---

### 1995 — XI CIM

**R. De Tintis** — *"GRAINS: a Software for Real-Time Granular Synthesis and Sampling Running on the IRIS-MARS Workstation"* (pp. 220–224)
Articolo dedicato. Software real-time per IRIS-MARS workstation (Studio di Fonologia RAI Milano), sviluppato in ambiente grafico EDIT20 con interfaccia ATARI. Architettura: 4 algoritmi identici di granular synthesis quasi-sincrona, ciascuno produce stream di grani con parametri per-grano (frequency/length/waveform/amplitude). Controllo runtime via MIDI continuous controllers in configurazione gerarchica o flat. *Horizontal density* via gate gaussian random a ogni campione; *vertical density* via numero algoritmi attivi (stratificazione). Tre uscite indipendenti per algoritmo: clean grain stream / 3-filter bank stile VOSIM / waveguide monodimensionale `Y(n)=X(n)+G·Y(n-T)`. Sampling buffer real-time 25 sec esportabile in MIDI Sample Dump. Cita esplicitamente «*tendency masks introduced by Truax*» (p. 221) come stato dell'arte: terzo data-point CIM dell'adozione modello Truax 1988 dopo [[discipio-tisato1993]] + [[lippe1993]]. Lineage VOSIM italiano CIM (anello 1995 fra [[depoli-piccialli1988]] e [[sparano2018]]). **Real-time.** Vedi [[detintis1995]].

**Agostino Di Scipio** — *"Real-time Polyphonic Time-shifting of Sound with Interactive Systems"* (pp. 19–22)
Articolo dedicato. Elaborazione granulare real-time per time-shifting polifonico e granulazione ricorsiva. Sistemi **KYMA/CAPYBARA** (L'Aquila LMS, brano *Hybris* 1994) e **PODX/GSAMX su DMX-1000** (Simon Fraser, brano *Essai du vide. Schweigen* 1993). Stream HYBRIS1 in Smalltalk-80: 4 processi granulazione avviati a 5"/10"/15"/20" con ratio 5×/4×/3×/2× più lenti. Nuova classe `aSample&ShiftWithAllPass` con icona + parametri custom (grain dur 10–70 ms, stretch factor, allpass delay = grain_dur/2, spatial trajectory). Recursive granulation `x_{n+1} = f_b(f_a(x_n))` in *Essai du vide*. Tassonomia 4-quadrant `{composition,performance} × {program,environment}` (p. 19). **Snodo CIM offline → real-time per lo stesso autore di [[discipio1991]] e [[discipio-tisato1993]]**: documenta la transizione di paradigma annunciata 1993 p. 165. **Real-time.** Vedi [[discipio1995]].

---

### 1998 — XII CIM

**D. Keller, C. Rolfe** — *"The Corner Effect"* (pp. 236–239)
Articolo dedicato. **Errata-corrige rispetto a versione iniziale del survey**: identificazione precedente *"MacPod... di Keller & Truax"* errata — *MacPod* compare nel paper come didascalia di figura (p. 239) e come ref [11] (Rolfe 1998, Third Monk Inc.), non come titolo. Autori effettivi: Keller (SFU) + Rolfe (Third Monk Software/CCWIA). Il volume Keller & Truax 1998 sull'argomento è ICMC Ann Arbor (ref [6] del paper), non CIM XII.
Contenuto: analisi del *corner effect* (artefatto comb-filter della finestra trapezoidale usata da MacPod per efficienza vs. gaussiana). Decorrelazione tra stream tramite phase-synchronicity. Resintesi ecologica con grain pool pre-costruito. Fino a 20 stream simultanei, grain rate minimo 1 ms. **Real-time.**
Vedi [[keller-rolfe1998]].

---

### 2000 — XIII CIM

**Chris Rolfe, Damian Keller** (Third Monk Software / CCWIA) — *"Decorrelation as a By-Product of Granular Synthesis"* (Poster Session II, ~3–4 pp.)
Articolo dedicato. **Stessa coppia di autori di [[keller-rolfe1998]] (CIM XII) con ordine invertito** — Rolfe primo qui, Keller primo nel 1998. Estende formalmente l'ontologia 1998 (stream/waveform/pointer/event) a una **teoria misurabile della correlazione su 3 livelli ortogonali**: grain-to-grain (intra-stream), cross-channel/stream (inter-stream), instance/event (inter-execution). Definizione matematica esplicita di cross-correlation $F(\tau) = \lim \frac{1}{T} \int y_1(t) y_2(t+\tau) dt$ normalizzata $-1.0 \leq k \leq 1.0$. Modello reference con N grain stream condividenti buffer di input, delay tap per stream con `delay-range` random + pairing per cancellare AM, 23-64 streams per smearing artifacts. Pitch-shift esplicitamente escluso dal modello core (pre-processing di stream). Trade-off esplicito *transparency vs decorrelation* (sez. 3). **Primo paper CIM granulare *meta-livello*** (analizza il behavior dei modelli, non li implementa). **Anello cronologico CIM → CMR sulla decorrelazione**: ontologia [[keller-rolfe1998]] (1998) → framework formale Rolfe-Keller 2000 (correlazione misurabile) → [[vaggione2002]] (decorrelation come attributo morfologico-spaziale di prima classe). Real-time, anche se piattaforma specifica non dichiarata. Vedi [[rolfe-keller2000]].

---

### 2003 — XIV CIM

**Andrea Valle, Vincenzo Lombardo** (MultiLab/UniTo) — *"A Two-Level Method to Control Granular Synthesis"* (pp. 136–140)
Articolo dedicato. **Errata-corrige**: autori identificati via title page (PDF p. 145 = printed p. 136); il titolo *"GEOGRAPHY: A TWO-LEVEL SYSTEM..."* in maiuscolo è titolo della sezione 2 del paper, non titolo paper. Sistema formale (**GeoGraphy**) a due livelli: (1) generatore di sequenze di grani basato su grafi diretti (vertice = grano, arco = relazione di sequenziamento con tempo di onset); (2) controller parametrico delle forme d'onda tramite mappe. Generalizza approccio per-nota e approccio stocastico (Xenakis/Truax). **Offline** (out-of-time, generative).
Vedi [[valle-lombardo2003]].

---

### 2006 — XVI CIM

**Costantino Rizzuti** — *"Il 'caos sonoro': studi preliminari per la realizzazione di un sistema di sintesi granulare controllato mediante iterazione di funzioni non lineari"*
Articolo dedicato. Mappa logistica `xt+1 = c·xt(2-xt)` per controllo deterministico (senza generatori casuali) di ampiezza, durata, istante d'attacco e frequenza dei grani. Architettura CSound: due strumenti separati — uno genera eventi sonori da partitura, l'altro genera i grani su direttive del primo. Pipeline: **partitura → strumento eventi → strumento grani → audio**, **offline**. Vedi [[rizzuti2006]].

---

### 2008 — XVII CIM

**Alessio Santini** — *"Comporre (con) oggetti audio-visivi: un ambiente di lavoro in via di sviluppo"*
Menzione rilevante. La granulazione del suono in Max/MSP è punto di partenza che motiva estensione al dominio video (micro-frammentazione temporale audio-visiva sincronizzata). Patch disponibile su Cycling'74.

---

### 2010 — XVIII CIM

**Stefano Silvestri** (Cons. S. Pietro a Majella, Napoli) — *"Introduzione alla sintesi Wavetable Switching per Multiplexing di segnali"* (pp. 209–213)
Articolo dedicato. Procedimento tempo-discreto: oscillatori wavetable look-up paralleli + finestrature quadre/gaussiane sfasate + emulatore multiplexer N-bit (rete combinatoria AND/NOT/OR) che commuta i sub-vettori. Inquadrato esplicitamente dall'autore come *forma di sintesi granulare deterministica*: «operazioni quali lettura e finestratura rappresentano la generazione del grano [...] mentre l'apparato di commutazione è ciò che guida i parametri del grano stesso» (p. 209). Implementazioni Csound + Pure Data. Composizione **Studio Sonoro III** «interamente basata su algoritmi di wavetable multiplexing implementati sia per la sintesi in tempo reale che, per la parte per nastro, in tempo differito» (nota 10, p. 210) = data-point CIM 2010 della coesistenza RT+offline nella stessa opera. Tesi I Liv. con Di Scipio relatore (A.A. 2008/2009) → terzo nodo *granulare deterministico CIM* dopo [[discipio1991]] e [[rizzuti2006]]; terzo nodo *lineage napoletano CIM* dopo [[depoli-piccialli1988]] e [[ortosecco-piccialli1989]]; *thread Di Scipio allievi* continuato in [[arcella-silvestri2012]] (Silvestri co-autore). Vedi [[silvestri2010]].

---

### 2012 — XIX CIM

**Andrea Arcella, Stefano Silvestri** — *"Analogique B: A computer model of the compositional process"* (pp. 144–148)
Articolo dedicato (ricostruzione storica). Ricostruzione digitale di *Analogique A et B* di Xenakis (1958–59), considerato il primo brano basato sulla sintesi granulare. Pipeline:
```
C++ (score.cpp) → Xscore.txt (formato score Csound)
                ↓
       Analogique.csd (orchestra Csound) → audio
```
Analisi del processo compositivo originale con schermi markoviani (MPT 8×8). Procedure Xenakis definite "out-of-time, additive". **Offline.** Quote conclusiva p. 148: *"Tools and technologies used to produce a musical work are not neutral but incorporate knowledge that influence the choices of the composer"* — formulazione CIM diretta della tesi sul carattere non neutrale degli strumenti compositivi. Vedi [[arcella-silvestri2012]].

---

### 2014 — XX CIM

**Andrea Agostini, Éric Daubresse, Daniele Ghisi** (HES-SO Ginevra / Cons. Cuneo) — *"CAGE: una libreria di alto livello per la composizione assistita da computer in tempo reale"* (pp. 17–22)
Articolo dedicato (system paper). Libreria **cage** per Max, basata su bach (struttura `llll` Lisp-like linked list per dati simbolici musicali). Modulo **`cage.granulate`** = *motore di granulazione **simbolica*** che opera su `bach.roll` (rappresentazione partitura), non su buffer audio: parametri analoghi al granulare audio (intervallo fra grani, durata grano, regione di partitura sorgente), ma le entità manipolate sono note simboliche con altezza e durata, non campioni. Pedagogia esplicita: moduli come astrazioni Max ispezionabili. **Real-time simbolico**. Prima occorrenza CIM di *granulazione simbolica* come categoria distinta dal granulare audio — anti-analogia di principio rispetto a tutta la tradizione granular audio CIM (incluso PGE).

**Giacomo Valenti, Andrea Valle, Antonio Servetti** (Politecnico Torino + UniTo CIRMA) — *"Permutation synthesis"* (pp. 35 ss.)
Articolo dedicato (synthesis paper sperimentale). Tecnica che riarrangia chunk di campioni dello stesso segnale senza envelope per generare nuove forme d'onda. Posiziona esplicitamente la sintesi granulare come tecnica di riferimento di confronto: granulare e *time-granulation* applicano envelope per eliminare discontinuità e scattering stocastico nel tempo; permutation synthesis al contrario *enfatizza* le discontinuità come feature. Riferimento Roads citato come fondamento. Andrea Valle = secondo paper CIM granular-related dopo [[valle-lombardo2003]] — continuità autoriale su 11 anni. **Real-time.**

Menzioni marginali nel volume: granulation+waveshaping per distorsione (Potter's architecture) e granular synthesis con DAC R2R 8-bit (hardware esperimentale). Non rilevanti per il paper PGE.

---

### 2016 — XXI CIM

**Marco Matteo Markidis, José Miguel Fernández** (nonoLab Parma + IRCAM Parigi) — *"Analisi e sintesi in tempo reale mediante riconoscimento timbrico"* (pp. 181–185)
Articolo dedicato (system paper). **`path~`** per Pure Data, external GPLv3: corpus-based concatenative synthesis con kd-tree e k-nearest neighbors nel spazio descrittori (default 16-dim: MFCC 14 + spectral centroid + RMS). Pipeline ibrida: segmentazione + estrazione descrittori + costruzione kd-tree + ordinamento + calcolo knn list **in tempo differito** (thread worker); estrazione descrittori sull'input + ricerca primo vicino + sintesi grano **in tempo reale**. Latency <2 ms su DB 30K grani; analisi offline <1 min su 10 min audio. Posiziona esplicitamente la sintesi concatenativa come *evoluzione contemporanea della sintesi granulare* in cui «i grani sono legati fra loro solitamente da un'analisi precedentemente fatta su un file audio» (p. 181) — differenza ontologica con scatter stocastico Roads/Truax. Primo paper CIM Markidis (continua in [[markidis2024]] 8 anni dopo, con shift da tool builder a metodologo della traduzione fra ambienti). **Real-time + tempo differito misti.** Vedi [[markidisfernandez2016]].

**Daniele Pozzi** — *"Composing Exploration: A Multi-Agent Approach to Corpus-Based Concatenative Synthesis"*
Articolo dedicato. Agenti Boids che esplorano uno spazio 2D di descrittori e controllano granulatori individuali. Comportamento emergente genera texture granulari spaziali. **Real-time.**

---

### 2018 — XXII CIM

**Giovanni Sparano** — *"GrainLab - Software open source per la sintesi granulare quasi-sincrona"* (pp. 243–245)
Articolo dedicato. Granulatore quasi-sincrono Max/MSP+Gen su linee di ritardo finestrate, singolo segnale rampa pilota con sfasamenti deterministici (preset *continuous*/*rhythmic*) o aleatori, 6 funzioni di finestratura (Hann/Expodec/Rexpodec/Triangle/Trapezoid/Sinc) in 9 preset (preset 7 = rotazione su gruppi di 6 grani, preset 8 = alternanza Expodec/Rexpodec, preset 9 = alternanza Hann/Sinc), densità via duty cycle, cambio parametri click-free via Sample&Hold a fase 0. Open source. Caso d'uso: *FENIX DNA* di Fabrizio Plessi al Teatro La Fenice (luglio-agosto 2017), 5 istanze per ensemble (flauto, cl. basso, viola, pianoforte, soprano) + 4 delay spettrali + spazializzazione multicanale. **Real-time.** Vedi [[sparano2018]].

---

### 2022 — XXIII CIM

**Andrea Cera, Corrado Canepa, Nicola Ferrari, Alberto Pilotto, Paolo Coletta, Simone Ghisio, Antonio Camurri** — *"Interactive Sonification of Expressive Gesture: the DanzArTe - Emotion Wellbeing Technology Project"* (pp. 79–86)
**Marginale — non citare nel paper CIM 2026.** Sonificazione interattiva applicata per riabilitazione cognitiva anziani fragili; granulazione strumento operativo extra-compositivo, dominio non sovrapponibile a PGE. Né precursore né anti-precursore strutturale. **Real-time.** Pagina conservata come memoria di scansione: [[cera2022]].

---

### 2024 — XXIV CIM

**Marco Matteo Markidis** — *"Mediation Process in a Computer Music Interpretation: an Ecosystemic Approach"* (pp. 48–56)
Articolo dedicato. Reimplementazione in Pure Data di *Audible Ecosystemics no. 3a* (Di Scipio 2003, rev. 2016) a partire dal solo graphical DSP score rilasciato CC. Sviluppa la libreria PD open-source **aeLib** + la metodologia **layer of mediation** a quattro strati (*Conceptual/Paradigm*, *Runtime Environment*, *Hardware*, *Syntax-Language*) come framework per la traduzione fra ambienti di computer music. Granulatore = sotto-componente di un ecosistema audio-feedback signal-driven; quote granulator score Di Scipio p. 53 = secondo data-point CIM della terminologia *grain sampling* dopo [[lippe1993]] e ricezione del modello tendency-mask Truax 1988 in lingua compositiva (*"grain density controls and slight random variations on grain parameters ('jitter')"*). Quote pietra-angolare p. 48: *"By making the DSP score available [...] in a high-level language not dependent on any specific implementation, the composer enables performers to create patches in an environment of their choosing. [...] the composer abstracts the piece from its specific implementation network"* = formulazione CIM 2024 esplicita del programma *separare specifica da implementazione*, pattern condiviso col DSL YAML PGE per via tecnologica opposta (graphical DSP score real-time vs textual DSL deferred). Chiude il thread Di Scipio CIM: [[discipio1991]] (offline, vincolo hardware) → [[discipio-tisato1993]] (ICMS, DSL ante litteram) → [[discipio1995]] (snodo real-time KYMA) → **Markidis 2024** (fase ermeneutica, sustainability via graphical score). **Live electronics** (non offline). Vedi [[markidis2024]].

**Alessandro Anatrini** — *"WavePilot: Framework multidimensionale per l'esplorazione dello spazio parametrico di strumenti digitali"* (pp. 129–135, Session 3 — Tools and platforms)
Non granulare in senso stretto (no "granul" nel testo), ma **direttamente rilevante per il posizionamento PGE** sull'asse dell'esplorazione dello spazio parametrico di strumenti digitali. Framework Python+JavaScript, VAE per riduzione dimensionale parametri DMmI, meta-GUI browser navigabile + interpolazione RBF + OSC verso Reaper/Live/Max/TouchDesigner. Open source. **Real-time interattivo**. Aggiunto al sottoinsieme "non comparabili (real-time)" per simmetria di scopo + opposizione tecnologica con PGE. Modello stilistico CIM 2024 per tool paper con cornice teorica estesa (sez. 2 *Contesto* dedicata, 25 ref / 7 pp.). Vedi [[anatrini2024]].

---

## Nessun articolo rilevante

1976 (I CIM), 1977 (II CIM), 1979 (III CIM), 1981 (IV CIM).

---

## Sottoinsieme: tempo differito — confronto con PythonGranularEngine

**Pipeline PGE:** `YAML → Python → AIF`
Ispirazione dichiarata: Truax DMX-1000 (1988). Offline, controllo parametrico ad alto livello.

### Pipeline analoga (codice → score → Csound → audio)

**2012 — Arcella, Silvestri**
Pipeline quasi identica: C++ genera score Csound → CSound orchestra → audio. Stessa separazione tra logica compositiva (C++/Python) e rendering (CSound). Fattorizzazione esplicita in due moduli (p. 147). Differenza: PGE introduce YAML dichiarativo + IR Python (`Stream`/`Grain`) intermedia, mentre Arcella/Silvestri scrivono direttamente score Csound da C++ (renderer-coupled, specifico al brano). Vedi [[arcella-silvestri2012]].

**2006 — Rizzuti**
CSound con due strumenti separati: generatore eventi (equivalente alla generazione dello score PGE) + generatore grani. Schema `partitura → strumento eventi → strumento grani → audio`. Differenza: PGE separa il livello di specifica (YAML) dal livello di rendering (CSound); Rizzuti codifica il controllo direttamente nella partitura CSound senza livello intermedio. Vedi [[rizzuti2006]].

### Offline con controllo algoritmico dei parametri

**1991 — Di Scipio**
Esplicitamente "tempo differito, IBM PC 286". Mappe non-lineari per controllo parametri granulari. Problema RAM per granulazione di suoni reali — problema che PGE affronta con il NumPy renderer e il caching per stream (SHA-256 fingerprint).
Vedi [[discipio1991]].

**1993 — Di Scipio, Tisato (ICMS)**
Continuazione diretta del filone Di Scipio 1991 su sistema più maturo (ICMS, mainframe IBM 9121, time-sharing). Pipeline 3-step grano (pointer → read → envelope/write) come **primo precedente CIM a livello di pseudocodice** del loop `Stream.generate_grains()` PGE. Quote pietra-angolare p. 165 *"single rule may instantiate multiple operations [...] step towards the abstract"* = **programma DSL ante litteram CIM 1993** che PGE realizza nel 2026. Tendency-mask control = conferma documentale CIM 1993 dell'adozione del modello Truax 1988 (sampling gaussiano + indipendenza fra grani). Layering ricorsivo di stream con mixing coefficients = primitiva STEMS PGE. Coesistenza nel singolo sistema di tendency-mask statistica + mappe caotiche deterministiche (le opzioni 4-7 del menu). **Ultimo nodo maturo della tradizione offline italiana CIM**: lo stesso volume CIM X 1993 ospita Lippe ISPW real-time, e Di Scipio/Tisato annunciano «*near future in a real-time version on a NeXT computer*» (p. 165). Vedi [[discipio-tisato1993]].

**1985 — Roads**
Offline, MUSIC language. Il concetto di frame come unità di organizzazione superiore al grano (frame interval → aggiornamento parametri) è l'analogo strutturale dello stream in PGE. Identica motivazione: densità alta → necessità di controllo ad alto livello anziché per-grano. Vedi [[roads1985]].

### Fondazione DSP/wavelet della sintesi granulare

**1989 — Ortosecco, Piccialli**
Identificazione wavelet=grano (via Roads 1985) come base teorica della sintesi granulare. Analisi offline tramite channel vocoder a wavelets; risintesi controllata dai coefficienti estratti. Implementazione su DSP Ariel TMS 32025. Pattern *precompute-once / reuse-many* (wavelet prototipo tabulata 4096 campioni) analogo al `WindowGenerator` PGE. Linea italiana CIM post-De Poli/Piccialli 1988. Vedi [[ortosecco-piccialli1989]].

### Astrazione compositiva formale

**2003 — Valle, Lombardo (GeoGraphy)**
Sistema a due livelli (generatore sequenze + controller parametrico) architetturalmente analogo a PGE (Stream = traccia di grani, envelope = variazione parametrica nel tempo). Offline (out-of-time, generative). Autori identificati via title page (errata-corrige rispetto a versione iniziale del survey).
Vedi [[valle-lombardo2003]].

### Non comparabili (real-time)

1993 Lippe (vedi [[lippe1993]]; precursore tassonomico CIM *granular synthesis vs granular sampling* + doppia conferma indipendente del modello tendency mask 1993 assieme a [[discipio-tisato1993]]), 1995 De Tintis (vedi [[detintis1995]]; terzo data-point CIM tendency mask + lineage VOSIM italiano CIM, coppia stesso volume CIM XI 1995 con [[discipio1995]] come due polarizzazioni *synthesis vs sampling*), 1995 Di Scipio (*Real-time Polyphonic Time-shifting* — vedi [[discipio1995]]; snodo CIM offline → real-time per lo stesso autore di [[discipio1991]] e [[discipio-tisato1993]]), 1998 Keller/Rolfe (*The Corner Effect* / MacPod — vedi [[keller-rolfe1998]]), 2000 Rolfe/Keller (*Decorrelation as a By-Product of Granular Synthesis* — vedi [[rolfe-keller2000]]; primo paper CIM granulare *meta-livello* — framework formale 3 livelli correlazione misurabile, anello CIM intermedio fra [[keller-rolfe1998]] e [[vaggione2002]]), 2016 Markidis/Fernández (vedi [[markidisfernandez2016]]; primo paper CIM Markidis, `path~` per Pd, concatenative synthesis come *evoluzione esplicita CIM 2016 della sintesi granulare* con grani legati per somiglianza nei descrittori vs scatter stocastico; pipeline ibrida RT/differito con multithreading; precursore CIM dell'idea che parte del workflow granulare-derivato sia *necessariamente* offline), 2016 Pozzi, 2018 Sparano (vedi [[sparano2018]]), 2022 Cera et al. (vedi [[cera2022]]), 2024 Markidis (*Mediation Process in a Computer Music Interpretation* — vedi [[markidis2024]]; chiude il thread Di Scipio CIM offline → real-time → fase ermeneutica 2024 via graphical DSP score + metodologia *layer of mediation* a 4 strati; secondo data-point CIM della terminologia *grain sampling* dopo [[lippe1993]]; quote pietra-angolare p. 48 *"high-level language not dependent on any specific implementation"* = pattern *separare specifica da implementazione* condiviso col DSL YAML PGE per via tecnologica opposta), 2024 Anatrini (*WavePilot* — vedi [[anatrini2024]]; non granulare in senso stretto, aggiunto per simmetria di scopo sull'esplorazione parametrica con anti-analogia tecnologica forte vs PGE).

---

*Survey condotto: 2026-05-04. Strumento: `pdftotext` su tutti i 23 PDF in `raw/proceedings/`, ricerca su radice `granul`.*
