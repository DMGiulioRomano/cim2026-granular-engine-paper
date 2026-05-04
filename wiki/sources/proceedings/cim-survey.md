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
Articolo dedicato. Panoramica storica, basi teoriche (Gabor 1946–47), strumento granulare semplice (oscillatore sinusoidale + inviluppo quasi-gaussiano). Introduce il concetto di **frame** come unità di organizzazione superiore al grano: ogni frame aggiorna i parametri per centinaia di grani. Problema esplicito: densità 1000–5000 grani/minuto richiede `d × n` valori di controllo → necessità di un livello di organizzazione più alto. Granulazione temporale di suoni registrati. Pipeline: MUSIC language, **offline**.

---

### 1988 — VII CIM

**G. De Poli, A. Piccialli** — *"Forme d'onda per la sintesi granulare sincrona"*
Articolo dedicato. Analisi forme d'onda ottimali per sintesi granulare sincrona. Confronto con sintesi per formanti. Intervallo tra grani 10–20 ms. Riferimenti: Roads 1978, Truax DMX-1000 (ICMC 86).

---

### 1989 — VIII CIM

**Immacolata Ortosecco, Aldo Piccialli** — *"Sintesi granulare e metodi di analisi / Sintesi granulare e Digital Signal Processing"*
Articolo dedicato. Connessione tra sintesi granulare, wavelets e DSP. Completezza della wavelet ortogonale di Martinet come base teorica della sintesi granulare. Sistema di analisi tramite banco di filtri (channel vocoder) derivato da wavelet. **Offline**.

---

### 1991 — IX CIM

**Agostino Di Scipio** — *"Caos deterministico, composizione e sintesi del suono"*
Keywords: composition, granular synthesis, timbre, deterministic chaos, non-linear dynamics.
Articolo dedicato (applicazione). Sistemi dinamici non-lineari per controllo parametri granulari: ampiezza, durata, posizione nel buffer, frequenza di granulazione. Mappa logistica e distribuzioni biparametriche. Granulazione di suoni reali (campionati). Granulazione a cascata. Esplicita: **"procedure attualmente implementate in tempo differito, su IBM PC 286"**. Implementazione in tempo reale non implementata per limiti di RAM (granulazione di suoni reali "problema attualmente insormontabile").

---

### 1993 — X CIM

**A. Di Scipio, G. Tisato** — *"Granular synthesis with Interactive Computer Music System"*
Articolo dedicato. Sistema ICMS con menu di granulazione: passo costante/variabile, moto browniano, distribuzioni gaussiane, equazioni non-lineari (logistica `xn = a·xn-1(1-xn-1)`, Verhulst, May, "discubic"). Granulazione con puntatore variabile da equazione. Menziona Tisato ICMS.

**C. Lippe** — *"Real-time Control of Granular Sampling via Nonlinear Processes Using the IRCAM Signal Processing Workstation"*
Articolo dedicato. Controllo real-time della granulazione via processi non-lineari su IRCAM ISPW. **Real-time.**

---

### 1995 — XI CIM

**R. De Tintis** — *"GRAINS: a Software for Real-Time Granular Synthesis and Sampling Running on the IRIS-MARS Workstation"*
Articolo dedicato. Software real-time su workstation IRIS-MARS. **Real-time.**

**Agostino Di Scipio** — *"Real-time Polyphonic Time-shifting of Sound with Interactive Systems"*
Articolo dedicato. Elaborazione granulare real-time per time-shifting polifonico e granulazione ricorsiva. Sistemi KYMAC/APYB (LMS) e PODX (Simon Fraser University). **Real-time.**

---

### 1998 — XII CIM

**D. Keller (& B. Truax)** — *"MacPod: real-time granular synthesis for the Macintosh"*
Articolo dedicato. Implementazione su Macintosh PowerPC. Finestra trapezoidale per efficienza computazionale (drastica riduzione tempi vs. gaussiana). Decorrelazione tra stream tramite phase-synchronicity. Resintesi ecologica con grain pool pre-costruito. Fino a 20 stream simultanei, grain rate minimo 1 ms. **Real-time.**

---

### 2000 — XIII CIM

**Chris Rolfe, Daniil Keller** (Third Monk Software / CCWIA) — *"Decorrelation as a By-Product of Granular Synthesis"*
Articolo dedicato. Analisi sistematica della decorrelazione grain-to-grain, cross-channel (stream) e a livello di istanza (evento). Approccio sistematico alla decorrelazione granulare come strumento compositivo (panning, effetti stereo). Collegamento a MacPod. Prevalentemente teorico/analitico.

---

### 2003 — XIV CIM

*Autore non identificato dall'OCR* — *"[GeoGraphy]: A Two-Level System for Grain Generation and Control Structure"*
Articolo dedicato. Sistema formale a due livelli: (1) generatore di sequenze di grani basato su grafi diretti (vertice = grano, arco = relazione di sequenziamento con tempo di onset); (2) controller parametrico delle forme d'onda tramite mappe. Generalizza approccio per-nota e approccio stocastico (Xenakis/Truax). Termine: "GeoGraphy". Presumibilmente **offline** (nessuna menzione real-time).

---

### 2006 — XVI CIM

**Costantino Rizzuti** — *"Il 'caos sonoro': studi preliminari per la realizzazione di un sistema di sintesi granulare controllato mediante iterazione di funzioni non lineari"*
Articolo dedicato. Mappa logistica `xt+1 = c·xt(2-xt)` per controllo deterministico (senza generatori casuali) di ampiezza, durata, istante d'attacco e frequenza dei grani. Architettura CSound: due strumenti separati — uno genera eventi sonori da partitura, l'altro genera i grani su direttive del primo. Pipeline: **partitura → strumento eventi → strumento grani → audio**, **offline**.

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

**Andrea Arcella, Stefano Silvestri** — *"Analogique B: A computer model of the compositional process"*
Articolo dedicato (ricostruzione storica). Ricostruzione digitale di *Analogique A et B* di Xenakis (1958–59), considerato il primo brano basato sulla sintesi granulare. Pipeline:
```
C++ (score.cpp) → Xscore.txt (formato score Csound)
                ↓
       Analogique.csd (orchestra Csound) → audio
```
Analisi del processo compositivo originale con schermi markoviani (MPT 8×8). Procedure Xenakis definite "out-of-time, additive". **Offline.**

---

### 2016 — XXI CIM

**Marco Matteo Markidis, José Miguel Fernández** — *"Analisi e sintesi in tempo reale mediante riconoscimento timbrico"*
Articolo dedicato (sintesi concatenativa). `path~` per Pure Data: corpus-based concatenative synthesis dove la sintesi avviene tramite granulazione dei k-vicini più simili nel spazio dei descrittori. **Real-time.**

**Daniele Pozzi** — *"Composing Exploration: A Multi-Agent Approach to Corpus-Based Concatenative Synthesis"*
Articolo dedicato. Agenti Boids che esplorano uno spazio 2D di descrittori e controllano granulatori individuali. Comportamento emergente genera texture granulari spaziali. **Real-time.**

---

### 2018 — XXII CIM

**Giovanni Sparano** — *"GrainLab - Software open source per la sintesi granulare quasi-sincrona"*
Articolo dedicato. Granulatore quasi-sincrono su linee di ritardo finestrate. Open source. Scalabile, parametri: numero grani, ampiezze, densità probabilistica, fase, ritardo. Usato in ensemble acustico (flauto, cl. basso, viola, pianoforte, soprano). **Real-time.**

---

### 2022 — XXIII CIM

**Andrea Cera, Corrado Canepa, Nicola Ferrari, Alberto Pilotto, Paolo Coletta, Simone Ghisio, Antonio Camurri** — *"Interactive Sonification of Expressive Gesture: the DanzArTe - Emotion Wellbeing Technology Project"*
Menzione tecnica. Due granulatori sovrapposti per ogni motore di sonificazione: finestra principale 5s (trasposizione -1 ottava) + finestra secondaria 1s (-10 dB). Controllo posizione/trasposizione da metadati di analisi del movimento corporeo (Kinect II). **Real-time.**

---

### 2024 — XXIV CIM

**Marco Matteo Markidis** — *"Mediation Process in a Computer Music Interpretation: an Ecosystemic Approach"*
Menzione rilevante. Reimplementazione di *Audible Ecosystemics no. 3a* di Di Scipio in Pure Data. Granulatore asincrono ("grain sampling") come elemento del sistema eco-sistemico. Problemi tecnici: densità dei grani, gestione del feedback loop con `[tabsend~]`/`[tabreceive~]`. **Live electronics** (non offline).

---

## Nessun articolo rilevante

1976 (I CIM), 1977 (II CIM), 1979 (III CIM), 1981 (IV CIM).

---

## Sottoinsieme: tempo differito — confronto con PythonGranularEngine

**Pipeline PGE:** `YAML → Python → .sco (Csound score) → Csound → AIF`
Ispirazione dichiarata: Truax DMX-1000 (1988). Offline, controllo parametrico ad alto livello.

### Pipeline analoga (codice → score → Csound → audio)

**2012 — Arcella, Silvestri**
Pipeline quasi identica: C++ genera score Csound → CSound orchestra → audio. Stessa separazione tra logica compositiva (C++/Python) e rendering (CSound). Differenza: PGE usa YAML + Python come livello di astrazione; Arcella/Silvestri usano C++ direttamente.

**2006 — Rizzuti**
CSound con due strumenti separati: generatore eventi (equivalente alla generazione dello score PGE) + generatore grani. Schema `partitura → strumento eventi → strumento grani → audio`. Differenza: PGE separa il livello di specifica (YAML) dal livello di rendering (CSound); Rizzuti codifica il controllo direttamente nella partitura CSound senza livello intermedio.

### Offline con controllo algoritmico dei parametri

**1991 — Di Scipio**
Esplicitamente "tempo differito, IBM PC 286". Mappe non-lineari per controllo parametri granulari. Problema RAM per granulazione di suoni reali — problema che PGE affronta con il NumPy renderer e il caching per stream (SHA-256 fingerprint).

**1985 — Roads**
Offline, MUSIC language. Il concetto di frame come unità di organizzazione superiore al grano (frame interval → aggiornamento parametri) è l'analogo strutturale dello stream in PGE. Identica motivazione: densità alta → necessità di controllo ad alto livello anziché per-grano.

### Astrazione compositiva formale

**2003 — GeoGraphy (autore non identificato)**
Sistema a due livelli (generatore sequenze + controller parametrico) architetturalmente analogo a PGE (Stream = traccia di grani, envelope = variazione parametrica nel tempo). Nessuna menzione real-time → presumibilmente offline.

### Non comparabili (real-time)

1993 Lippe, 1995 De Tintis, 1995 Di Scipio, 1998 MacPod, 2016 Markidis/Fernández, 2016 Pozzi, 2018 Sparano, 2022 Cera et al., 2024 Markidis.

---

*Survey condotto: 2026-05-04. Strumento: `pdftotext` su tutti i 23 PDF in `raw/proceedings/`, ricerca su radice `granul`.*
