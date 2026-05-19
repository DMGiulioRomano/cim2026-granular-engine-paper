# [Roads, 1985] Granular Synthesis of Sound: Past Research and Future Prospects

## Citazione CIM
Roads, C. (1985). Granular Synthesis of Sound: Past Research and Future Prospects. In *Musica e tecnologia: industria e cultura per lo sviluppo del Mezzogiorno* (Quaderni di Musica/Realtà 14, Atti del VI CIM, a cura di C. Acreman, I. Ortosecco, F. Razzi), pp. 195–209. Milano: Edizioni Unicopli.

## Categoria e lunghezza
Comunicazione orale full paper (sessione *Software I*) — 15 pagine (numerate 195–209, di cui pagina 195 = titolo di sessione e capofila autore) — 11 riferimenti — 12 figure numerate (1–11 + Fig. 12 conclusive) — 7 sound examples elencati a margine del testo.

## Argomento centrale
Stato dell'arte CIM della sintesi granulare nel 1985: ricostruzione storica (Gabor 1946–47, Bastiaans 1980, Xenakis 1971), enunciazione del problema di controllo (densità `d` ∈ [1000, 5000] grani/min × `n` parametri = `d·n` valori per minuto di suono → necessità di un livello di organizzazione superiore al grano), confronto tra due approcci candidati a tale livello — *frame-based* (Xenakis 1971, non ancora implementato) ed *event-based* (lavoro di Roads, implementato per la composizione *prototype*) — e programma di ricerca per un *environment* integrato (GUI + linguaggio di alto livello tipo Lisp + DSP dedicato tipo 4X).

## Sistema o strumento descritto
Implementazioni sperimentali al MIT su **Music II** (offline, mainframe). Strumento granulare elementare: oscillatore sinusoidale + envelope quasi-gaussiana, posizionabile in spazio quadrafonico (Fig. 2). Composizioni realizzate con sintesi granulare a quella data: *prototype*, *Objet*, *nscor*, *Field* (recente Compact Disc MIT). Front-end implementato in Lisp nel 1983 ma non interfacciabile con Music II per il limite di indirizzamento a 64 KB (max 32 eventi simultanei prima del crash). Proposta esplicita per il futuro: *4X di IRCAM* come target hardware real-time, oltre 100 grani simultanei, *graceful degradation* (deletion delle voci interne) sul modello Moorer 1981 / Kaplan 1981.

## Analogia con PGE

Roads 1985 è il **primo paper CIM dedicato alla sintesi granulare** e introduce nella tradizione CIM tre nuclei concettuali che PGE materializza quarant'anni dopo:

1. **Problema `d·n` come motivazione del DSL.** «*it takes d * n parameter values to specify one minute of sound. Since the density d is often in the range of 1000 to 5000, it is clear that for the purposes of compositional control, a higher-level unit of organization for the grains is needed*» (p. 197). Questa è la formulazione canonica CIM del problema che il DSL YAML PGE risolve: il compositore non specifica `d·n` valori ma intenzioni parametriche (range, envelope, strategie di variazione) che il `ParameterOrchestrator` materializza in grani discreti.

2. **Frame come unità superiore al grano = precursore CIM diretto dello Stream.** «*One way to organize the grains is to assemble them into a regular sequence of frames, like the control frames of linear predictive coding synthesis. Each frame can contain hundreds of grains. [...] At each frame interval, the grain parameters are updated*» (pp. 197–198, Fig. 3). Lo Stream PGE è esattamente questo: contenitore temporale di centinaia/migliaia di grani con i parametri di controllo che variano a livello superiore al grano. Differenza architetturale rilevante: Roads 1985 propone un frame *isocrono* (Δt costante tra 1–10 ms), PGE consente frame rate variabile per-voice via Envelope time-varying — differenziatore già articolato in `overview.md` punto 6 contro il modello screens-of-Xenakis.

3. **Event-based approach con slope = precursore della struttura Controller/Envelope.** «*the composer specifies an event in terms of a duration, an initial frequency, a frequency slope, and initial amplitude, and amplitude slope, and an initial grain density and density slope over the duration of the event. The slopes determine the change in the parameter settings (and hence, sonic content) of the grains over time*» (p. 200, Fig. 6). L'event di Roads 1985 ha 6 coppie *valore iniziale + slope* — è la struttura che si ritrova identica nell'AGS di Roads 1978 (paper già ingestito) e che PGE generalizza in `ParameterOrchestrator` con strategie multiple (Envelope continuo, ProbabilityGate, stocastiche multi-voce). Il *trapezoid* di Roads 1985 è un caso particolare di Envelope lineare a tratti del PGE.

4. **Polygon su frequency/time plane = precursore della partitura grafica (con asse Y diverso).** «*events can be visualized as instances of trapezoids — four-sided figures with two parallel sides. In practice, we can use granular synthesis to fill in any polygon inscribed on the frequency/time plane*» (p. 200, Fig. 7–9). Il `score_visualizer` PGE eredita lo schema *figura geometrica sul piano (X=tempo, Y=parametro)* ma sceglie un asse Y diverso (posizione-buffer anziché frequenza), motivato dal caso d'uso granulazione di campioni in cui la frequenza è derivata da `pitch_ratio` e la posizione-buffer è il parametro compositivamente significativo (cfr. Truax 2014 *listening "inside" the sound*).

5. **Hardware limits come razionale storico del deferred time.** Roads 1985 documenta esplicitamente i vincoli che hanno reso necessario il tempo differito: 64 KB address space di Music II, max 32 events simultanei, density limit ~1600 grain/sec. Il paper *prospetta* il superamento (4X di IRCAM, 100 grain simultanei) — superamento che si realizzerà tre anni dopo con Truax 1988 (DMX-1000). Questa è la pietra angolare della narrazione tre atti del paper CIM 2026: Roads 1985 = atto 1 (tempo differito per necessità), Truax 1988 = atto 2 (real-time come paradigma), PGE = atto 3 (ritorno volontario al deferred).

6. **Time granulation di suoni naturali** (saxophone di Earl Howard, percussioni) come tecnica già nominata nel 1985 — anticipa l'asse Y posizione-buffer come categoria compositivamente significativa: granulare un campione significa muovere una testina di lettura nel buffer, quindi la posizione-buffer è il parametro che il compositore controlla davvero (cfr. PointerController PGE).

## Posizionamento storico
**Primo paper CIM dedicato alla sintesi granulare.** Apre il filone CIM sul controllo gerarchico parametrico (1985 Roads → 1991 Di Scipio → 1993 Tisato → 2003 GeoGraphy → 2006 Rizzuti → 2012 Arcella/Silvestri). Posizionato cronologicamente **prima del DMX-1000 di Truax (1988)**: è la formulazione canonica CIM del problema di controllo *prima* che il paradigma real-time renda la questione apparentemente obsoleta. Roads 1985 cita Roads 1985 (libro, *Foundations of Computer Music*) come fonte parallela — i due documenti articolano in parallelo la stessa tesi su due venue diverse.

Doppia funzione storica: (a) **stato dell'arte** consolidato (Gabor → Xenakis → Roads 1978 → MIT 1985) leggibile come summa del filone tempo-differito CIM; (b) **programma prospettico** per l'environment integrato (GUI + Lisp + DSP), che documenta la lineage architetturale che porterà a PulsarGenerator (2001), EmissionControl (2005), EC2 (2021) — il polo real-time-gestural opposto a PGE.

## Note stilistiche

**Struttura del paper:** Abstract (5 righe) → Introduction (genealogia Gabor/Xenakis + definizione tecnica) → Granular Synthesis Instrument (descrizione strumento) → Control Data for Granular Synthesis (problema `d·n`) → Frames (proposta Xenakis non implementata) → Events (lavoro proprio) → Realization of Graphic Scores (polygon su piano freq/time) → Signal Processing Aspects (sidebands, random deviation 2 μs) → Time Granulation of Sounds → Psychoacoustics Research Questions → Problems with Past Implementations (limiti Music II) → An Environment for Granular Synthesis (programma futuro) → Sound Examples → Conclusion → References.

**Tono:** argomentativo + descrittivo + programmatico. Roads alterna ricostruzione storica, descrizione di lavoro proprio (*"My own research in granular synthesis"*, p. 200), e programma di ricerca futura — modalità retorica utile come modello per il paper CIM 2026, che ha la stessa triplice valenza (radici teoriche → architettura PGE → loop lungo come metodologia prospettata).

**Densità citazioni:** 11 riferimenti — mix di fondamenti teorici (Gabor 1946/47, Bastiaans 1980, Green 1971, Xenakis 1971), implementazioni computer-music (Moorer 1981, Kaplan 1981), pratica concorrente (Risset/Wessel 1982), e auto-riferimento (Roads 1978, 1985 *Foundations*). Tipico paper di systems-and-overview CIM ante-litteram.

**Figure:** 12 figure totali (di cui Fig. 5 e Fig. 12 sono *tabelle/elenchi puntati* in forma di figura — pattern utile per la Tabella 1 di overview.md o per il diagramma di architettura PGE). Fig. 9 = excerpt della partitura grafica di *prototype* — primo esempio di pubblicazione CIM di una partitura granulare a polygon su piano freq/tempo.

**Sound examples:** 7 esempi numerati e referenziati nel corpo (es. *"Sound Example 7 is an excerpt from my piece Field"*). Indica che il paper era accompagnato da supporto audio in sede di presentazione — pattern non più replicabile nel paper CIM 2026 scritto (ma traducibile in figure + repository pubblico).

**Apertura/chiusura:** apre con la genealogia Gabor, chiude su *"granular synthesis is potentially a general synthesis method, capable of synthesizing nearly any sound. At this stage of development, however, we are satisfied just to be able to add to the computer musician's palette"* — chiusura misurata, anti-trionfalistica, programmatica. Modello stilistico utile per la conclusione del paper CIM 2026.

## Quote chiave (verbatim)

1. **(problema `d·n`, p. 197)** «*If n is the number of parameters for each grain, and d is the mean grain density per minute of sound, it takes d * n parameter values to specify one minute of sound. Since the density d is often in the range of 1000 to 5000, it is clear that for the purposes of compositional control, a higher-level unit of organization for the grains is needed.*»

2. **(frame come unità superiore, pp. 197–198)** «*One way to organize the grains is to assemble them into a regular sequence of frames, like the control frames of linear predictive coding synthesis. Each frame can contain hundreds of grains. [...] At each frame interval, the grain parameters are updated.*»

3. **(event con slope, p. 200)** «*the composer specifies an event in terms of a duration, an initial frequency, a frequency slope, and initial amplitude, and amplitude slope, and an initial grain density and density slope over the duration of the event. The slopes determine the change in the parameter settings (and hence, sonic content) of the grains over time. Within the boundaries of an event, grains are automatically scattered according to the tendencies specified by the event's parameters.*»

4. **(polygon su piano freq/time, p. 200)** «*events can be visualized as instances of trapezoids — four-sided figures with two parallel sides. In practice, we can use granular synthesis to fill in any polygon inscribed on the frequency/time plane.*»

5. **(random deviation, p. 203)** «*strictly sequential grains are a boundary case, since the appearance of a grain at a particular time point is determined by a call to a random function. [...] just a 2 μs random deviation from a strictly sequential chain attenuates most of the regular sidebands by 10 to 20 db.*» — fondamento DSP di `DensityController` modalità asincrona e di `dephase` per-grano.

6. **(limiti Music II, pp. 205–206)** «*Past implementations of granular synthesis have been stymied by hardware and software restrictions. At MIT, we have been limited to synthesis using the Music II language [...]. The anachronistic 64 Kbyte address space limitation inherent in Music II proved fatal: No more than 32 events can be playing simultaneously or the program crashes.*»

7. **(programma front-end / IR, pp. 205–206)** «*the key to generalized granular synthesis is the use of relatively simple synthesis instruments driven by more complicated programs written in High-level languages such as Lisp. In this case, granular synthesis can be realized with a simple synthesis instrument that is driven by massive amounts of data. This data is created by a front-end program that interacts with a user.*» — formulazione esplicita CIM 1985 del pattern *front-end → engine* che PGE eredita (YAML + Python → Csound/NumPy).

## Sezioni del paper CIM 2026 dove citare

- **Sezione 1 (Introduzione, narrazione tre atti):** Roads 1985 come formulazione CIM canonica dell'atto 1 (tempo differito per necessità hardware). Citare quote 1 (`d·n`) come problema fondante e quote 6 (limiti Music II) come razionale storico del deferred time. Pendant CIM diretto di Di Scipio 1991 (IBM 286).
- **Sezione 2 (Sintesi granulare):** quote 2 (frame) + quote 3 (event con slope) + quote 4 (polygon su piano freq/time) — questi sono i tre nuclei concettuali ereditati. Inserire nella tabella precursori la riga 1985 Roads CIM con citazione esplicita (oggi è già presente in overview.md ma genericamente). Quote 5 (random deviation 2 μs) come fondamento DSP della distribuzione asincrona Truax/PGE.
- **Sezione 3 (PGE Architettura):** quote 7 (front-end Lisp → engine) come precedente storico CIM del pattern YAML→Python→Csound; quote 1 come motivazione formale del DSL. Citare frame=Stream nella discussione dell'astrazione gerarchica.
- **Sezione 4 (Partitura grafica):** quote 4 (polygon su piano freq/time) come precursore concettuale dello score_visualizer, esplicitando l'inversione di asse Y (frequenza → posizione-buffer) motivata dal caso d'uso granulazione di campioni.
- (Sezione 5: non rilevante — Roads 1985 non documenta brani specifici utilizzabili come riferimento compositivo.)
- (Sezione 6: non rilevante in modo diretto.)
