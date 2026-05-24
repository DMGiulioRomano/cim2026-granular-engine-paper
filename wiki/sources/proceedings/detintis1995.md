# [De Tintis, 1995] GRAINS: a Software for Real-Time Granular Synthesis and Sampling Running on the IRIS-MARS Workstation

## Citazione CIM

De Tintis, R. (1995). GRAINS: a software for real-time granular synthesis and sampling running on the IRIS-MARS workstation. In *Atti dell'XI Colloquio di Informatica Musicale*, pp. 220–224. Bologna: AIMI.

## Categoria e lunghezza

Comunicazione orale (paper di sistema) — 5 pp. — 9 riferimenti
(Roads CMJ 1988, Truax CMJ 1988, Jones/Parks CMJ 1988, MacKay *Interface* 1984, Mitsuhashi *JAES* 1982, Roads MIT 1991 *Representations of Musical Signals*, Fricke 1995, [[depoli-piccialli1988]] CIM VII, De Poli/Piccialli MIT 1991, Smith ICMC 1987).

## Argomento centrale

Sistema real-time per sintesi granulare quasi-sincrona su workstation IRIS-MARS (4 algoritmi identici, ciascuno produce uno stream di grani), con focus dichiarato sulla *data reduction* per consentire controllo MIDI ad alto livello in performance dal vivo. Ogni algoritmo offre tre uscite indipendenti (clean grain stream / 3-filter bank stile VOSIM / waveguide monodimensionale) per estendere la sintesi granulare verso modelli source-filter.

## Sistema o strumento descritto

**GRAINS** — software real-time per IRIS-MARS workstation (Studio di Fonologia RAI di Milano / IRIS Industria dello Spettacolo). Sviluppato in ambiente grafico **EDIT20**. Interfaccia utente C su piattaforma ATARI (mouse-driven; controlla una sola variabile alla volta come limite). Controllo runtime via MIDI continuous controllers (master keyboard, fader, sequencer, Max). Real-time. Sample rate hardware MARS ≈ 39 kHz. Sampling buffer real-time fino a 25 sec, esportabile in formato binario e convertibile a MIDI Sample Dump per uso su sampler commerciali.

**Architettura sintesi (p. 221):**
- 4 algoritmi identici di granular synthesis quasi-sincrona, ciascuno produce stream di grani in sequenza.
- Parametri per-grano: frequenza, lunghezza, forma d'onda, ampiezza.
- *Horizontal density* = densità all'interno dello stream (decisione di attivazione nuovo grano via confronto con generatore gaussiano random a ogni campione; legge probabilistica).
- *Vertical density* = numero di algoritmi attivi simultaneamente (stratificazione del materiale sonoro).
- Distribuzione normale per lunghezza, ampiezza, horizontal density entro range MIDI-controllati indipendentemente per ciascun parametro.

**Processing dei grani (p. 222):**
- Output #1 = grain stream "clean" dal processo granulare.
- Output #2 = banco a 3 filtri (1 LP + 2 HP secondo ordine) per riprodurre la parte risonante del modello VOSIM.
- Output #3 = risonatore waveguide monodimensionale `Y(n) = X(n) + G·Y(n−T)`.
- Razionale: lo stream di grani come treno di impulsi modellabili è sorgente eccitatrice di modelli source-filter.

## Analogia con PGE

**Convergenze concettuali (con divergenza tecnologica forte):**

1. **Stream di grani come unità di organizzazione di prima classe** — i 4 algoritmi GRAINS sono 4 stream identici controllati indipendentemente; PGE generalizza a N stream YAML-dichiarati. La nozione `stream = sequenza di grani prodotta da un singolo algoritmo` precede esplicitamente in CIM 1995 la stessa scelta architetturale del `Stream` PGE.

2. **Per-stream multi-output routing → precursore concettuale workflow STEMS** — ogni algoritmo GRAINS ha 3 uscite indipendenti con gain real-time controllabile. Stesso *taglio architetturale* del workflow STEMS PGE (rendering separato per stream + bouncing per accesso a ogni livello individualmente). De Tintis usa i 3 output per ramificare verso modelli post-processing (filter/waveguide); PGE usa lo split per cache incrementale + export DAW. Ma la *separazione esplicita del flusso per stream* come oggetto compositivo è il punto comune.

3. **Density terminology / hierarchical control** — pp. 221 *"horizontal density"* / *"vertical density"*: doppia direzione del controllo granulare (asse tempo di un singolo stream + asse stratificazione fra stream) come due gradi di libertà ortogonali. PGE replica questa ortogonalità in YAML con `density` per-stream + numero di stream definiti a livello di brano. Terminologia *vertical density* per stratificazione di stream rimane utile per descrivere l'output di `score_visualizer` PGE (asse Y = posizione nel buffer; sovrapposizione fra stream = stratificazione verticale).

4. **Source-filter resonatore come prolungamento del grain stream** — De Tintis tratta esplicitamente il grain stream come sorgente eccitatrice di filter bank + waveguide (p. 222 *"every algorithm has three outputs"*). PGE non implementa filter bank in catena interna, ma il workflow STEMS rende possibile il routing post-rendering identico (file AIF di stream + post-process in DAW). Ergonomia analoga: separare sintesi granulare *pura* da processing risonante a valle.

**Anti-analogie strutturali (poli compositivi opposti):**

1. **Real-time MIDI gestuale (De Tintis) vs deferred declarativo (PGE)** — De Tintis dedica l'intera sez. 2 *Data Reduction* a giustificare la riduzione drastica dei parametri come *requisito* del real-time («the reduction of data is a fundamental goal for the effectiveness and the efficiency for the composer who can work with high level parameters», p. 221). PGE inverte: il tempo differito permette di *non* ridurre i parametri ma esporli completamente nel DSL YAML, perché il loop lungo assorbe il costo cognitivo. Argomento di Sezione 2 e Sezione 3 del paper CIM 2026: due risposte opposte allo stesso problema di density of control.

2. **MIDI continuous controllers vs YAML + envelope curves** — la generazione probabilistica per-grano in GRAINS dipende dallo stato runtime dei controller MIDI; in PGE i parametri sono *funzioni del tempo* (envelope curves dichiarative nel YAML) renderizzate offline. Stesso obiettivo (variazione temporale di amplitude/length/frequency) con primitivi opposti: *physical-time gesture* (De Tintis) vs *score-time function* (PGE).

3. **Limiti hardware imposti (sample rate 39 kHz MARS, buffer 25 sec) vs rendering arbitrario (PGE)** — il vincolo hardware MARS dell'epoca produce un sistema *constraint-driven*; PGE è *constraint-free* sul fronte sample rate / buffer e accumula questo vantaggio nella cache per-stream (SHA-256 fingerprint, no ricomputazione). Snodo storico: i sistemi real-time italiani 1995 (GRAINS, KYMA in [[discipio1995]]) operavano contro vincoli che il deferred Python 2026 non ha più ma che PGE *sceglie* come postura.

4. **VOSIM lineage (De Tintis) vs source-only deferred (PGE)** — De Tintis prolunga lo stream di grani in source-filter via filter bank + waveguide, ereditando direttamente il lineage VOSIM/Rodet citato in [[depoli-piccialli1988]] e [[ortosecco-piccialli1989]]. PGE non integra modelli source-filter nel core; lascia la sintesi *granulare pura* e demanda il post-processing alla DAW via workflow STEMS. Stesso lineage tecnologico CIM (VOSIM → De Poli/Piccialli → Ortosecco/Piccialli → De Tintis) divaricato sul piano architetturale.

## Posizionamento storico

**Atto 2 della narrazione tre-atti (real-time come cambio di paradigma) — CIM 1995.** Quinto paper della tradizione CIM dedicato esplicitamente al granulare real-time: dopo [[lippe1993]] (ISPW IRCAM) e [[discipio1995]] (KYMA/CAPYBARA + PODX/DMX-1000), De Tintis 1995 documenta la terza piattaforma real-time italiana (IRIS-MARS / Studio di Fonologia RAI Milano).

**Coppia stesso volume CIM XI 1995:**
- *Real-time Polyphonic Time-shifting* di Di Scipio (pp. 19–22) → vedi [[discipio1995]] — Kyma/PODX-DMX1000, focus su granulazione di suoni campionati per time-shifting e ricorsione.
- *GRAINS* di De Tintis (pp. 220–224) → questo paper — IRIS-MARS, focus su 4 stream paralleli con 3-output routing source-filter.

Lo stesso volume documenta *due* polarizzazioni del real-time granulare italiano CIM 1995: Di Scipio = *granular sampling* (riprende [[lippe1993]] p. 180) con accento su ricorsione e time-shifting; De Tintis = *granular synthesis* nel senso classico (forme d'onda sintetiche + filter bank VOSIM-like) con accento su stratificazione e MIDI control.

**Lineage VOSIM/forme d'onda granulari CIM:**
- 1988: [[depoli-piccialli1988]] CIM VII — forme d'onda ottimali per granulare pitch-synchronous.
- 1989: [[ortosecco-piccialli1989]] CIM VIII — wavelet/grano come base teorica DSP.
- 1995: De Tintis CIM XI — *implementazione real-time* dell'idea VOSIM su grain stream (filter bank + waveguide come prolungamento source-filter).

Anello mancante tra CIM 1988/89 (offline, forme d'onda pitch-synchronous) e CIM 2018 [[sparano2018]] (real-time quasi-sincrono Max/MSP+Gen). De Tintis 1995 = punto medio del lineage italiano *granular quasi-sincrono*.

**Tendency mask reference:** De Tintis cita esplicitamente «*tendency masks introduced by Truax*» (p. 221) come stato dell'arte per organizzare l'alto numero di variabili. Terzo data-point CIM dell'adozione modello Truax 1988, dopo [[discipio-tisato1993]] + [[lippe1993]] (stesso volume X CIM 1993). Conferma che nel 1995 il modello tendency mask era nomenclatura canonica nella tradizione CIM.

## Note stilistiche

- **Lunghezza/refs:** 5 pp / 9 ref — paper compatto, taglio descrittivo-tecnico più che argomentativo.
- **Densità citazionale:** Bilanciata (CMJ 12(2) 1988 *Granular Synthesis Issue* citato tre volte: Roads / Truax / Jones-Parks); MIT Press 1991 *Representations of Musical Signals* citato per Roads e De Poli/Piccialli; ICMC/SMC presenti (Smith 1987); CIM interno citato 1× (De Poli/Piccialli 1988). Bibliografia *technical/DSP* più che *philosophical*.
- **Struttura sezioni:** 1 *Introduction* / 2 *Data Reduction* (giustificazione architetturale del controllo MIDI) / 3 *Sound Generation* (architettura algoritmi quasi-sincroni) / *Grains Processing* (3-output routing) / chiusura interfaccia ATARI + features + Refs. Niente sezione di cornice teorica esplicita; la motivazione è inglobata in sez. 2 (sintetica).
- **Tono:** descrittivo-implementativo, prima persona dell'autore («This was the primary aim I tryed to achieve...», p. 221), niente posizionamento estetico esplicito. Apertura motivazionale leggera (flessibilità MIDI), chiusura su feature operative (sampling + MIDI Sample Dump export).
- **Figure:** un solo schema architetturale (Excitator Source = Grain Stream → 3 Filter Bank / Monodimensional Wave Guide) + formula waveguide `Y(n) = X(n) + G·Y(n−T)`. Stile *system diagram* essenziale.
- **Apertura/chiusura:** apertura tecnica diretta («This paper describes Grains, a tool for sound synthesis based on granular techniques...», p. 220), chiusura su feature di sampling real-time + esportazione (no future work narrativo).
- **Modello stilistico utile per il paper CIM 2026:** *no* come modello globale (troppo descrittivo per la tesi argomentativa PGE), *sì* come modello locale per la sezione 3 (Architettura PGE) — densità tecnica della descrizione algoritmica + nomenclatura *horizontal/vertical density* riutilizzabile.

## Sezioni del paper CIM 2026 dove citare

- **Sezione 1 (Introduzione):** atto 2 della narrazione tre-atti — terzo data-point CIM 1995 di sistemi real-time granulari italiani (con [[discipio1995]] stesso volume) a rinforzo dello snodo offline→real-time. La doppia uscita CIM XI 1995 (Di Scipio + De Tintis) mostra che il real-time granulare era *istituzionalizzato* in CIM 1995, rendendo il ritorno volontario PGE 2026 al deferred una scelta postuma alla disponibilità del real-time.
- **Sezione 2 (Sintesi granulare):** lineage VOSIM italiano CIM (1988 De Poli/Piccialli → 1989 Ortosecco/Piccialli → 1995 De Tintis); terzo data-point CIM tendency mask Truax (con [[discipio-tisato1993]] + [[lippe1993]]); coppia *granular sampling vs granular synthesis* (De Tintis = synthesis classica, [[discipio1995]] = sampling, distinzione formalizzata da [[lippe1993]]).
- **Sezione 3 (PGE architettura):** anti-analogia *data reduction* (De Tintis 1995) ↔ *data exposure* (PGE 2026) come due risposte opposte al problema density-of-control. Conferma CIM 1995 del concetto *stream* come unità di organizzazione (4 stream identici GRAINS → N stream YAML PGE).
- **Sezione 4 (Partitura grafica):** terminologia *horizontal/vertical density* utilizzabile per descrivere il `score_visualizer` PGE come visualizzazione simultanea della densità orizzontale (asse tempo) + stratificazione verticale (asse Y = posizione buffer + sovrapposizione stream).
- **Sezione 6 (Conclusioni):** *opzionale* — punto di contrasto storico per la postura tempo differito (i vincoli hardware MARS 1995 imponevano data reduction; PGE 2026 non ha quei vincoli ma sceglie di esporre comunque la complessità nel DSL).

## Quote chiave

> «*The reduction of data is a fundamental goal for the effectiveness and the efficiency for the composer who can work with high level parameters. This was the primary aim I tryed to achieve with the current implementation in order to reach an improved real-time feedback in a live performance.*» (p. 221)

— Tesi *data-reduction-as-real-time-requirement*, da contrapporre direttamente alla postura PGE di esposizione parametrica completa nel YAML.

> «*Many important criteria have been presented in order to better organize the high number of variables involved, from the hierarchical approach to the tendency masks introduced by Truax.*» (p. 221)

— Terzo data-point CIM dell'istituzionalizzazione modello Truax 1988 nel lessico granulare italiano (dopo [[discipio-tisato1993]] + [[lippe1993]]).

> «*Sound computation is made by four identical algorithms that calculate quasi-synchronous granular synthesis, with the output from every algorithm being a stream with the grains following one after the other.*» (p. 221)

— Definizione esplicita CIM 1995 di *stream = output di un algoritmo granulare = sequenza ordinata di grani*. Precursore terminologico del `Stream` PGE.

> «*A fifth parameter, the horizontal density, determines if, when one grain is terminated, a new one has to be activated [...] The horizontal density by the relative variable and the vertical density dicidmg how many algorithms are active at the same time controlling the stratification of the sonic material.*» (pp. 221–222)

— Coppia terminologica *horizontal/vertical density* riutilizzabile per descrivere l'architettura di stratificazione PGE + asse Y `score_visualizer`.

> «*In Grains, every algorithm has three outputs, each with an independent gain controllable in real-time. The first one contains the "clean" result from the granular process, the second one goes into a 3 filters bank reproducing the resonating part of the Vosim model [...] The third output goes into a waveguide resonator for the simulation of one-dimensional wave propagation.*» (p. 222)

— Precursore architetturale CIM 1995 del per-stream multi-output (workflow STEMS PGE). Tre uscite indipendenti per algoritmo = stessa *taglio per stream* del rendering STEMS PGE, anche se finalizzato a routing source-filter (filter bank + waveguide) anziché export DAW.
