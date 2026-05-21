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

**C. Lippe** — *"Real-time Control of Granular Sampling via Nonlinear Processes Using the IRCAM Signal Processing Workstation"*
Articolo dedicato. Controllo real-time della granulazione via processi non-lineari su IRCAM ISPW. **Real-time.**

---

### 1995 — XI CIM

**R. De Tintis** — *"GRAINS: a Software for Real-Time Granular Synthesis and Sampling Running on the IRIS-MARS Workstation"*
Articolo dedicato. Software real-time su workstation IRIS-MARS. **Real-time.**

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

**Chris Rolfe, Daniil Keller** (Third Monk Software / CCWIA) — *"Decorrelation as a By-Product of Granular Synthesis"*
Articolo dedicato. Analisi sistematica della decorrelazione grain-to-grain, cross-channel (stream) e a livello di istanza (evento). Approccio sistematico alla decorrelazione granulare come strumento compositivo (panning, effetti stereo). Collegamento a MacPod. Prevalentemente teorico/analitico.

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

**Stefano Silvestri** — *"Introduzione alla sintesi wavetable switching per multiplexing di segnali"*
Menzione teorica. La tecnica proposta ("wavetable switching per multiplexing") è inquadrata esplicitamente come "forma di sintesi granulare deterministica dove operazioni quali lettura e finestratura rappresentano la generazione del grano (o quanto sonoro), mentre l'apparato di commutazione è ciò che guida i parametri del grano stesso."

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

### 2016 — XXI CIM

**Marco Matteo Markidis, José Miguel Fernández** — *"Analisi e sintesi in tempo reale mediante riconoscimento timbrico"*
Articolo dedicato (sintesi concatenativa). `path~` per Pure Data: corpus-based concatenative synthesis dove la sintesi avviene tramite granulazione dei k-vicini più simili nel spazio dei descrittori. **Real-time.**

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

**Marco Matteo Markidis** — *"Mediation Process in a Computer Music Interpretation: an Ecosystemic Approach"*
Menzione rilevante. Reimplementazione di *Audible Ecosystemics no. 3a* di Di Scipio in Pure Data. Granulatore asincrono ("grain sampling") come elemento del sistema eco-sistemico. Problemi tecnici: densità dei grani, gestione del feedback loop con `[tabsend~]`/`[tabreceive~]`. **Live electronics** (non offline).

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

1993 Lippe, 1995 De Tintis, 1995 Di Scipio (*Real-time Polyphonic Time-shifting* — vedi [[discipio1995]]; snodo CIM offline → real-time per lo stesso autore di [[discipio1991]] e [[discipio-tisato1993]]), 1998 Keller/Rolfe (*The Corner Effect* / MacPod — vedi [[keller-rolfe1998]]), 2016 Markidis/Fernández, 2016 Pozzi, 2018 Sparano (vedi [[sparano2018]]), 2022 Cera et al. (vedi [[cera2022]]), 2024 Markidis.

---

*Survey condotto: 2026-05-04. Strumento: `pdftotext` su tutti i 23 PDF in `raw/proceedings/`, ricerca su radice `granul`.*
