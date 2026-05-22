# [Lippe, 1993] Real-time Control of Granular Sampling via Nonlinear Processes Using the IRCAM Signal Processing Workstation

## Citazione CIM
Lippe, C. (1993). Real-time Control of Granular Sampling via Nonlinear Processes Using the IRCAM Signal Processing Workstation. In *Atti del X Colloquio di Informatica Musicale*, pp. 178–182. Milano: AIMI.

## Categoria e lunghezza
Comunicazione orale — 5 pagine (pp. 178–182) — 12 riferimenti

## Argomento centrale
Distingue *granular synthesis* (forme d'onda sintetiche, elektronische Musik) da *granular sampling* (porzioni di suono campionato, musique concrète) come categorie tassonomicamente separate, e documenta su ISPW IRCAM il controllo real-time del granular sampling via processi non-lineari (chaotic equations, tendency masks) e via signal-driven control da strumenti dal vivo (pitch/amplitude tracking del clarinetto).

## Sistema o strumento descritto
IRCAM Signal Processing Workstation (ISPW) + Max [11][12] come interfaccia utente; real-time; 1993; pitch tracking + amplitude tracking + mapping su parametri granulari; "recursive aspect" = mixing real-time dell'output di task simultanee e reuse come sample sorgenti per altre task.

## Analogia con PGE
**Anti-analogia controllata e precursore tassonomico simultaneo.**

(a) **Categoria di sintesi.** PGE è granular *sampling* nella tassonomia Lippe (buffer-based, `PointerController.start_position` come asse compositivo primario, onset time nel sample sorgente = parametro di prima classe). Lippe (p. 180): *"in granular sampling, an additional parameter exists: onset time into the stored sound. This additional parameter can be of primary importance"* — formulazione CIM 1993 della legittimità dell'asse Y = posizione nel buffer del score_visualizer PGE come asse compositivo, non solo diagnostico.

(b) **Anti-analogia controllo.** Lippe è real-time signal-driven (gestualità del performer pilota la sintesi); PGE è deferred declarativo (loop lungo specifica→generazione→ascolto). Coppia con [[roads2021]] EmissionControl2 come due poli del real-time gestural: Lippe = performer come sorgente di control signal; Roads 2021 = composer/performer come operatore di MIDI controller.

(c) **Tendency masks confermati 1993.** Lippe (p. 181) usa esplicitamente *tendency masks* come tecnica primaria (*"choose grains statistically within defined tendency masks (constantly moving windows with varying sizes in which grains are statistically chosen)"*); coesiste nello stesso volume CIM X 1993 con [[discipio-tisato1993]] che usa tendency-mask control con sampling gaussiano. Doppia conferma documentale CIM 1993 dell'adozione del modello Truax 1988 → rinforza [[tendency-mask]] come canone CIM del periodo.

(d) **Recursive granulation.** Lippe (p. 180): *"a recent addition to the system allows for real-time mixing and sampling of the granular output of simultaneous tasks, which then may be reused as stored samples for other granular sampling tasks. This 'recursive' aspect offers exponential increases in densities, and a musically 'reflexive' dimension"* = primitiva architetturale identica a STEMS PGE (rendering per-stream + reuse come sorgente), ma in real-time; precursore CIM 1993 di [[discipio1995]] *recursive granulation* `x_{n+1} = f_b(f_a(x_n))`.

## Posizionamento storico
**Real-time** — secondo data-point CIM dello snodo offline→real-time (1993): nello stesso volume CIM X 1993, Lippe (ISPW, real-time, granular sampling signal-driven) coesiste con Di Scipio/Tisato (ICMS, mainframe time-sharing, offline, tendency-mask con annuncio NeXT real-time "near future"). Il volume X CIM è il punto di osservazione documentale del passaggio di paradigma annunciato nella narrazione tre-atti del paper CIM 2026.

Lineage: Truax DMX-1000 1987 (ICMC, ref [3] del paper) → Lippe ISPW 1993 (Max-based real-time, controllo non-lineare) → continua nella linea Max/MSP real-time fino a [[sparano2018]] (GrainLab) e [[roads2021]] (EC2). Lippe ringrazia esplicitamente Di Scipio negli acknowledgements (p. 182): rete di scambio diretto CIM offline ↔ real-time.

## Note stilistiche
- Struttura 7 sezioni brevi (Introduction / Granular Techniques / Compositional Implications / ISPW User Interface / Initial Experiments / Nonlinear Control / Mapping Musical Expression / Conclusion + Acknowledgements + References) — modello *short paper con sezioni titolate* tipico CIM anni '90.
- Densità citazioni: 12 ref in 5 pp. ≈ 2.4 ref/pp, mix paritetico fra teoria compositiva (Xenakis, Roads CMJ 1978), tecnica granulare (Truax 1987, Jones/Parks CMJ 1988) e infrastruttura ISPW (Lindemann/Starkier/Dechelle 1990, Lippe/Puckette ICMC 1991, Wessel/Bristow/Settel ICMC 1987).
- 1 figura ASCII (Figure 1, p. 181) — mapping performer-expression su parametri elettronici tramite OCR illegibile nel PDF (parole strappate: "derives discrete and continuous control signals such: articulation, notedensity, et:lUel of spcclral mus, pitchmbility").
- Tono argomentativo-tassonomico (la tesi *synthesis vs sampling* è argomentata, non descrittiva) + descrittivo tecnico (sezioni ISPW User Interface e Initial Experiments).
- Apertura referenziale: cita compositional strategies "by various composers [1], [2]" come terreno comune prima di affermare il proprio contributo (granular sampling controllato non-linearmente).
- Chiusura sintetica (5 righe): granular sampling come strumento, control non-lineare + signal-driven come contributo metodologico, "expressive control over an electronic score" come scopo musicale.

## Sezioni del paper CIM 2026 dove citare

- **Sezione 1 (Introduzione)** — snodo offline→real-time documentato CIM 1993 (assieme a [[discipio-tisato1993]]). Coppia: Di Scipio/Tisato annunciano NeXT real-time "near future" (p. 165), Lippe nello stesso volume mostra il real-time *già* operativo su ISPW. Atto 2 della narrazione tre-atti (Truax DMX-1000 1987 → Lippe ISPW 1993).
- **Sezione 2 (Sintesi granulare)** — tassonomia *granular synthesis vs granular sampling* (Lippe pp. 179–180) come distinzione canonica CIM. PGE collocato esplicitamente come granular sampling nella tassonomia Lippe; legittima la centralità di `PointerController` e dell'asse Y = posizione nel buffer.
- **Sezione 3 (PGE architettura)** — tendency masks 1993 (Lippe + Di Scipio/Tisato stesso volume) come conferma doppia CIM dell'adozione del modello Truax. Citazione rinforza [[tendency-mask]] in `ParameterOrchestrator`.
- **Sezione 4 (Partitura grafica)** — quote p. 180 *"onset time into the stored sound [...] of primary importance"* come legittimazione CIM 1993 dell'asse Y = posizione nel buffer come asse compositivo di prima classe.

## Quote chiave

p. 180 (granular synthesis vs sampling):
> *"While granular synthesis and granular sampling are variants of the same technique, their musical essences lie at opposite poles of the electronic music paradigm. One is immediately confronted, historically speaking, with the two main categories of electronic music: granular synthesis is elektronische Musik, making use of purely synthetic sounds, while granular sampling is part of the world of musique concrète in which recorded sounds are manipulated and transformed."*

p. 180 (onset time come parametro di prima classe):
> *"Since the synthetic waveform used in granular synthesis is replaced by a small portion of a stored sampled sound in granular sampling, an additional parameter exists: onset time into the stored sound. This additional parameter can be of primary importance in granular sampling. No longer a kind of 'commutative' or arbitrary parameter, grain order may have important consequences, creating an implicit hierarchy of parameters."*

p. 181 (tendency masks):
> *"A first attempt at controlling granular sampling using nonlinear mapping was simply to choose grains statistically within defined 'tendency masks' (constantly moving windows with varying sizes in which grains are statistically chosen)."*

p. 180 (recursive granulation):
> *"A recent addition to the system allows for real-time mixing and sampling of the granular output of simultaneous tasks, which then may be reused as stored samples for other granular sampling tasks. This 'recursive' aspect offers exponential increases in densities, and a musically 'reflexive' dimension, namely, the ability to recall earlier musical material in a real-time context."*
