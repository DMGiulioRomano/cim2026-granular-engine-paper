# [Di Scipio, Tisato, 1993] Granular Synthesis with Interactive Computer Music System

## Citazione CIM
Di Scipio, A., Tisato, G. (1993). Granular synthesis with Interactive Computer Music System. In G. Haus, I. Pighi (eds.), *Atti del X Colloquio di Informatica Musicale*, pp. 159–165. Milano: AIMI / LIM-DSI, Università degli Studi di Milano.

## Categoria e lunghezza
Comunicazione scientifica — 7 pagine (pp. 159–165) — 16 riferimenti bibliografici.

## Argomento centrale
Implementazione su **ICMS** (Interactive Computer Music System, Tisato, prima release 1975, mainframe IBM 9121 in time-sharing al Centro di Calcolo Ateneo di Padova) di un sottosistema di sintesi/granulazione che riformula la sintesi granulare come **caso particolare della granulazione**: in entrambi i casi il sistema esegue tre passi per grano — (1) calcolo del puntatore al file sorgente, (2) lettura di n campioni, (3) finestratura e scrittura nel file target. La distinzione "sintesi vs. granulazione" si riduce al contenuto del file sorgente (sinusoide a frequenza variabile vs. suono campionato), non a due algoritmi separati. Il controllo del puntatore è governato da un menu di sette opzioni: passo costante/variabile, moto Browniano (1/f²), distribuzione gaussiana, e quattro mappe non-lineari ("discubic", logistica, Verhulst, May).

## Sistema o strumento descritto
**ICMS — Interactive Computer Music System** (Tisato). Time-sharing su mainframe IBM 9121; restituisce minuti di audio 4 canali in pochi secondi; accessibile da PC e NeXT via Ethernet. Sottomenu `GRANULAR PROC.` dentro `SOUND PROCESSING` menu. Modalità *deferred time*. Pipeline:

```
source soundfile → pointer(t) ─┐
                                ├─ read n samples → envelope → target soundfile
                  control law ──┘
```

Sette opzioni di controllo del puntatore (Fig. 1, p. 162):
1. `CONSTANT-VARIABLE STEP GRANULATION`
2. `GRANULATION WITH BROWNIAN MOTION` (1/f² noise)
3. `GRANULATION WITH GAUSSIAN DISTRIBUTION`
4. `GRANULATION WITH EQ. "DISCUBIC"` `xn = (1−a)xn−1 + a·xn−1³`
5. `GRANULATION WITH EQ. "LOGISTIC"` `xn = a·xn−1·(1−xn−1)`
6. `GRANULATION WITH EQ. "VERHULST"` `xn = (1+a)xn−1 − a·xn−1²`
7. `GRANULATION WITH EQ. "MAY"` `xn = 1 − a·xn−1²`

Parametri di sintesi (Fig. 2, p. 163): mixing coefficients, file portion (limiti inf./sup. in ms su file-aux), grain duration (min/max in ms), grain delay (min/max in ms), grain amplitude (rescaling factor min/max), numero iterazioni, retrogradation switch, amplitude offset, repetitions per grain, phase inversion switch, cosine envelope exponent `p`, coefficiente equazione `a` (con final value per linear sweep nel bifurcation diagram), initial state `x₀`. Per i parametri marcati "tendency-mask" il range varia nel tempo, valore campionato da random generator gaussiano. Phase-level modifications applicate solo a ~50% dei grani (decisione white-noise RNG > 0.5). Inviluppo del grano: `s(t) = 1 − |cos(ω₀t)|^p`.

Brano citato: ***zeitwerk (l'orizzonte delle cose)*** (1992) — quattro sezioni, 8 sinusoidi a frequenza fissa (48, 105, 232, 511, 1124, 2473, 5442, 11972 Hz) come unico contenuto del source file; tutta la morfologia macro deriva da granular processing ricorsivo (layering di stream con grain durations crescenti fino a 0.2 s). Brani precedenti di Di Scipio realizzati con software analogo su IBM 80486 prima del trasferimento su ICMS: *ikon* (1991), *plex* (1991), *Kairos* (1992).

## Analogia con PGE

Cinque vettori di analogia/contrasto a forza decrescente.

**(a) Pipeline 3-step grano = `Stream.generate_grains()` PGE — analogia architetturale forte.**
La descrizione p. 160 («*each grain is generated following three main steps: 1) a pointer to a pre-existent source soundfile is calculated; 2) n samples are read from the file; 3) the sequence of n samples is processed, enveloped by a given function and written into a target soundfile*») è isomorfica al loop interno di `Stream.generate_grains()` (cfr. [[stream]]): `PointerController.position_at(t)` → lettura n campioni dal buffer → `WindowGenerator` × pitch/pan/voice transforms → mix nel buffer target. Questo è il **primo precursore CIM esplicito a livello di pseudocodice** della pipeline interna PGE. Il pattern è dichiarato come *riduzione semplificante* («*radically decreases the computational load of the signal generators and allows one to experiment with different approaches to the design of the control-structure*») — stessa motivazione architetturale della separazione PGE tra `Stream` (pipeline) e `ParameterOrchestrator` (controllo).

**(b) "Step towards the abstract" / "synthesis by rules" = programma DSL ante litteram — quote pietra-angolare.**
P. 165 (paragrafo finale, *Final observations*): «*further work should include the automation of operations that currently can be only done "by hand", including the processing of previously generated streams of grains and the layering of arbitrarily large numbers of streams. Some sort of synthesis by rules can be devised, based on the particular microstructural approach. In that case, a single rule may instantiate multiple operations in the realization of an entire process. This higher-level approach would represent a "step towards the abstract" for a perspective of sonic design which, by definition, is closely bounded to the level of sound materials.*» Formulazione CIM 1993 esplicita del programma che PGE realizza trent'anni dopo: una *single rule* (lo Stream YAML) instantia *multiple operations* (migliaia di grani) via `ParameterOrchestrator` + `VoiceManager` + `Controller`s. Il livello di astrazione che Di Scipio/Tisato dichiarano come direzione di lavoro futuro è il DSL YAML PGE.

**(c) Tendency-mask control = `ParameterOrchestrator` Envelope + range — continuità diretta.**
P. 162: «*For some parameters, a tendency-mask control is available, which makes the range of possible values change through time. Value assignment, in that case, is done using a random number generator (gaussian distribution). All this applies with parameters "grain duration", "grain delay" (time delay between two grains), "grain amplitude" (amplitude rescaling factor) and the portion of the source soundfile submitted to granulation.*» **Conferma documentale CIM 1993 dell'adozione del modello tendency-mask Truax 1988** (range time-varying + sampling da distribuzione gaussiana, valore al grano n+1 indipendente dal precedente) — esattamente il modello di [[tendency-mask]] implementato da PGE in `Parameter.value_at(t)` + `GaussianDistribution`. Lo stesso paper (opzioni 4-7) usa anche il modello caotico-iterativo `xn → xn+1` di [[discipio1991]]: **ICMS è la coesistenza in un singolo sistema delle due famiglie di controllo** (tendency-mask statistico per parametri di sintesi + iterazione deterministica per puntatore). PGE eredita esplicitamente la prima (vedi differenziatore 8 in [[overview]]), affianca la seconda come alternativa, non astrazione superiore.

**(d) Layering ricorsivo di stream + grain delay = workflow STEMS PGE — precursore concettuale.**
P. 163 (*Recursive processes*): «*Each time the system writes new samples in the target soundfile, it rescales and mixes them with already stored samples (rescaling factors are declared in the synthesis parameters submenu). That gives the user the opportunity of layering no matter how many streams of grains, if rescaling and grain delay are well-studied.*» Layering arbitrario di stream con coefficienti di missaggio dichiarati come parte della specifica = primitiva CIM 1993 della modalità STEMS PGE. Differenze materiali: ICMS scrive sul medesimo target file (no audio per-stem persistito); PGE scrive ogni stream come AIF indipendente con cache SHA-256 + export Reaper auto-generato (cfr. [[renderer]], [[stream-cache-manager]]). Stessa intenzione architetturale, profondità di astrazione divergenti.

**(e) Phase-level switches (reverse, repetition, offset, inversion) = controller switches PGE — precursore di feature.**
Pp. 162-163: switches per (i) writing samples backwards (citato come tecnica da [[truax1988]] = Truax 1990 ICMC), (ii) amplitude offset, (iii) phase inversion, (iv) repetitions del grano corrente prima del successivo (descritto come «*kind of "group delay unit" with effects similar to comb-filtering by-products*»). Attivazione probabilistica al 50% via white-noise RNG > 0.5. **Corrispondenze PGE:** (i) `grain_reverse` in `PointerController` (step 4 documentato in [[pointer-controller]]); (ii) ampiezza per-grano via `pitch_controller` + `volume` Envelope; (iii) phase inversion non implementato direttamente (fuori scope); (iv) repetitions = pattern simile a `deviation_probability` granulare ma con semantica diversa (PGE: deviazione per-grano del parametro; Di Scipio/Tisato: ripetizione bit-identical del grano N volte prima di emettere il successivo). Il *50% probability switch* è precursore concettuale del `ProbabilityGate` PGE (cfr. [[parameter-orchestrator]]) — decide se applicare una deviazione/trasformazione al grano corrente.

## Posizionamento storico

Articolazione finale del filone CIM **offline / controllo algoritmico parametri granulari** prima della transizione real-time:

| Anno | Volume | Autore | Sistema | Pipeline |
|------|--------|--------|---------|----------|
| 1985 | CIM VI | Roads | Music II / MIT | offline, frame come unità superiore al grano |
| 1988 | CIM VII | De Poli/Piccialli | additive pitch-synchronous | offline, ramo formantico |
| 1989 | CIM VIII | Ortosecco/Piccialli | channel vocoder Ariel TMS 32025 | offline, wavelet=grano |
| 1991 | CIM IX | Di Scipio | IBM PC 286 | offline, mappe caotiche pure |
| **1993** | **CIM X** | **Di Scipio/Tisato** | **ICMS mainframe IBM 9121** | **offline, tendency-mask + mappe caotiche coesistenti** |
| 1993 | CIM X | Lippe | IRCAM ISPW | **real-time** (stesso volume — punto di articolazione) |
| 1995 | CIM XI | De Tintis / Di Scipio | IRIS-MARS / KYMA / PODX | real-time |

Stesso volume CIM X (1993) ospita Di Scipio/Tisato (deferred su mainframe) e Lippe (real-time su ISPW): la transizione è documentata *all'interno di un singolo Atti*. ICMS è il sistema più maturo della tradizione CIM offline (15 anni di sviluppo da Tisato 1977 *Sistema interattivo per la sintesi dei suoni*, ref [7]), pronto al momento in cui la tradizione si biforca. La dichiarazione di Di Scipio/Tisato a p. 165 («*in the near future in a real-time version on a NeXT computer*») accompagna il programma di automazione astratta ("synthesis by rules"): i due assi (real-time e astrazione DSL) sono visti come direzioni *complementari* di sviluppo nel 1993, non come alternative. La tradizione CIM successiva sviluppa pienamente il primo asse (real-time) e lascia il secondo (DSL declarative per granulare deferred) come gap che PGE riempie nel 2026.

## Note stilistiche

- **Struttura del paper**: 7 sezioni, ciascuna su 0.5–1.5 pp. Introduction → Control-structure relevance → Precedents of the work → Basic technical criteria → Dynamical parameters controls → Recursive processes → Final observations + References. *Precedents of the work* dedicata interamente al lineage personale Di Scipio (3 brani su IBM 80486) + introduzione ICMS — modello stilistico riusabile per situare un sistema dentro una traiettoria autoriale. Le figure (2) sono richiamate puntualmente, no decorative.
- **Tono**: argomentativo-tecnico bilanciato. L'introduzione formalizza esplicitamente il duplice problema della sintesi granulare (signal processing + control structure), citando Roads 1985 (ref [1]) come framework. La sezione *Control-structure relevance* legge il problema come questione cognitiva e compositiva ("*The problem of making some higher-level morphological coherence emerge from many partial details, is a compositional problem tout court*", p. 160) — tono pre-figurazione della tesi non-neutralità degli strumenti che Arcella/Silvestri 2012 formuleranno esplicitamente.
- **Densità citazioni**: 16 riferimenti misti DSP (Jones/Parks 1988, Roads 1985, Truax 1988/1990/1991, Hamman 1991), composizione (Di Scipio ICMC 1990, Di Scipio CIM IX 1991, Di Scipio Workshop 1992, Di Scipio Bull. IMA 1992), cognizione (Bregman 1990, Laske 1991), epistemologia/estetica (Di Scipio ISMEZ 1991), sistemi non-lineari (May 1976, Collet/Eckmann 1980), documentazione ICMS (Tisato 1990 manuale, Tisato 1977 CIM II). Mix in linea con [[discipio1991]] (22 ref) ma più compatto. **Pattern riusabile per CIM 2026**: alternanza DSP/composizione/cognizione con riferimenti puntuali al lineage autoriale (proprio + sistema ricevuto).
- **Apertura**: dichiarazione frontale del duplice problema («*granular synthesis raises twofold set of strictly related problems, concerning 1) the inexpansiveness and effectiveness of algorithms of signal processing [...] and 2) the design of a high-level control-structure, defined as "front-end parameter processor"*») citando Roads 1985 come framework. Modello stilistico: apertura tecnica che dichiara il programma del paper come *posizionamento dentro una formulazione canonica esistente*. Utile come pattern per Sezione 1 CIM 2026 (Roads/Truax/Di Scipio).
- **Chiusura**: paragrafo programmatico ("step towards the abstract") che enuncia direzione di lavoro futura come dichiarazione di postura compositiva. Modello riusabile per Sezione 6 paper CIM 2026.

## Sezioni del paper CIM 2026 dove citare

- **`sec:architettura`** (primaria, cappello): «*a single rule may instantiate
  multiple operations [...] a step towards the abstract*» (p. 165) come
  programma della fase dichiarativa.
- **`sec:tradizione`** (secondaria): ultimo nodo offline; adozione della
  tendency mask in CIM 1993; coesistenza con Lippe nello stesso volume.

Fonte di verità: [[mappa-citazioni-paper]].

## Quote chiave

> «*[granular synthesis raises a] twofold set of strictly related problems, concerning 1) the inexpansiveness and effectiveness of algorithms of signal processing (oscillators, envelope generators, phase-level controls) and 2) the design of a high-level control-structure, defined as "front-end parameter processor"*» (p. 159) — formulazione canonica del duplice problema, identica al rationale architetturale PGE (`Stream`+`WindowGenerator` per il signal processing layer + YAML+`ParameterOrchestrator` per il control-structure layer).

> «*The control-structure should be conceived as the task of providing a description of how grains overlap and repeat through time. [...] It represents, indeed, the operationalization of some theoretical model of how does the low-level organization and temporal displacement of myriads of grains give rise to a global, coherent acoustical behaviour.*» (pp. 159-160) — definizione operativa della control-structure come *modello operazionalizzato* del comportamento globale. Definizione che il DSL YAML PGE materializza: ogni file YAML è un modello operazionalizzato dello Stream → cloud → forma.

> «*The very basic idea is that granular synthesis can be reduced to a particular case of granular processing [...] each grain is generated following three main steps: 1) a pointer to a pre-existent source soundfile is calculated; 2) n samples are read from the file; 3) the sequence of n samples is processed, enveloped by a given function and written into a target soundfile.*» (p. 160) — **pseudocodice CIM 1993 del loop interno PGE `Stream.generate_grains()`**, primo precedente CIM esplicito a livello di pipeline algoritmica.

> «*For some parameters, a tendency-mask control is available, which makes the range of possible values change through time. Value assignment, in that case, is done using a random number generator (gaussian distribution).*» (p. 162) — **conferma documentale CIM 1993 dell'adozione del modello tendency-mask Truax 1988** (range time-varying + sampling gaussiano + indipendenza fra grani). Identico al modello implementato in PGE [[tendency-mask]].

> «*Each time the system writes new samples in the target soundfile, it rescales and mixes them with already stored samples [...] That gives the user the opportunity of layering no matter how many streams of grains, if rescaling and grain delay are well-studied.*» (p. 163) — primitiva CIM 1993 del layering arbitrario di stream con coefficienti di missaggio dichiarativi = workflow STEMS PGE in forma embrionale.

> «*Independently of the implementation (in the near future in a real-time version on a NeXT computer), further work should include the automation of operations that currently can be only done "by hand", including the processing of previously generated streams of grains and the layering of arbitrarily large numbers of streams. Some sort of synthesis by rules can be devised, based on the particular microstructural approach. In that case, a single rule may instantiate multiple operations in the realization of an entire process. This higher-level approach would represent a "step towards the abstract" for a perspective of sonic design which, by definition, is closely bounded to the level of sound materials.*» (p. 165) — **quote pietra-angolare**. Programma DSL CIM 1993 esplicito che PGE realizza nel 2026. Da citare in Sezione 1 (narrazione tre atti — il programma del terzo atto è già enunciato nel primo) e Sezione 3 (architettura — DSL come "step towards the abstract" annunciato e realizzato).
