# [Roads, 2005] The Art of Articulation: The Electroacoustic Music of Horacio Vaggione

## Citazione CIM

Roads, C. (2005). The Art of Articulation: The Electroacoustic Music of Horacio Vaggione. *Contemporary Music Review*, 24(4/5), 295–309. DOI: 10.1080/07494460500172121.

## Argomento centrale

Roads traccia la traiettoria estetica e tecnica di Vaggione dalle prime esperienze con computer (Music N, IBM 7090, programma *Papova*, fine anni '60) attraverso le opere micromontage CARL/Cmusic degli anni '80 (*Octuor* 1982, *Thema* 1985, *Tar* 1987) fino alle composizioni multi-scala dell'epoca personal-computer (*Schall* 1994, *Nodal* 1997, *Agon* 1998, *Préludes Suspendus* 2000, *24 variations* 2001). La tesi del paper: l'arte di Vaggione è *articolazione su molteplici scale temporali* — micromontage come tecnica essenziale, alternanza algoritmo↔intervento manuale come strategia compositiva, sound editor grafici (mid-1980s in poi) come *abilitanti* della composizione su molteplici scale.

## Gap o problema identificato

Roads dichiara apertamente l'oggetto del paper come *building a new analytical vocabulary* per la musica di Vaggione (p. 295): «*This music's complexity and subtlety challenges mere textual description, posing formidable problems of discourse*». Il gap è duplice: (a) mancanza di un vocabolario analitico per articolazione multi-scala; (b) mancanza di una storia documentata della transizione dal mainframe deferred (anni '70-'80) al PC graphical-editor (mid-1980s in poi) come *cambio di postura compositiva*, non solo di hardware.

## Rilevanza diretta per PGE

Quattro punti di contatto, fortissimi:

1. **Tar (1987) note-list cmusic come DSL ante litteram** (Fig. 2, p. 300). Roads riporta in figura l'effettivo codice CARL/Cmusic di *Tar*: (a) lista di sound file dichiarati con `var`, (b) instrument definition con `seg`/`sndfile`/`mult`/`out`, (c) note-list testuale di 870 note con campi `start | duration | amp | location` — ciascuna nota è un microevent (`<58 ms`). Roads commenta: «*The construction of Thema by script meant that the material could be organized on an unprecedented level of micro detail*». Questo è il pattern *high-level specification of montage* di Roads 2001 cap. 5 p. 185, ma documentato qui con il codice sorgente reale dell'opera. Precursore CIM diretto del DSL YAML PGE: stesso paradigma testuale dichiarativo, stesso problema (centinaia/migliaia di microeventi non enumerabili manualmente in DAW), stessa soluzione (linguaggio compositivo + interprete + sintesi offline).

2. **Schall (1994) e la *progressive enrichment*** come pattern compositivo. Quote Vaggione 1999 (p. 302): «*Considering the hand-crafted side, this is the way I worked on Schall (along with algorithmic generation and manipulation of sound materials): making a frame of 7 minutes and 30 seconds and filling it by 'replacing' silence with objects, progressively enriching the texture by adding here and there different instances (copies as well as transformations of diverse order) of the same basic material*». È la formulazione operativa più chiara del *loop lungo* in prima persona da un protagonista della scena: il compositore alterna generazione algoritmica e manipolazione manuale su una *frame* (= contenitore temporale) progressivamente popolata. PGE è la materializzazione del *frame* via stream YAML + cache incrementale: il compositore arricchisce iterativamente la specifica testuale, e ogni modifica triggera ricalcolo selettivo via cache SHA-256.

3. **Graphical timeline editor come abilitante storico della partitura grafica** (p. 301): «*The simple ability to align multiple sounds along a timeline, to zoom in and out, and jump across time scales with the click of a button changed the nature of electroacoustic composition*». Roads identifica nel mid-1980s una transizione tecnologica che cambia *la natura* della composizione elettroacustica: la disponibilità di superfici grafiche multi-scala. Il `score_visualizer` PGE eredita questa lezione invertendone il flusso: non superficie editoriale di input (timeline DAW) ma rappresentazione ispezionabile di output (PDF A3, asse Y = posizione buffer), pensata per il ciclo di lettura riflessiva fra una sessione e l'altra.

4. **24 variations (2001) + IRIN** (p. 306, Fig. 3): Roads riproduce l'estratto della *score* IRIN per *24 variations* — rettangoli grigi su una timeline, asse Y = posizione nella traccia (non pitch). Roads esplicitamente: «*The vertical position of a sample within a track is not significant (i.e., it does not correspond to pitch). IRIN lets one encapsulate figures within tracks and represent them as a single fragment, permitting a hierarchical building up of mesostructure*». Conferma per via storica la categoria del visualizer PGE: rappresentazione grafica del materiale granulare in cui *l'asse Y non codifica pitch ma una proprietà strutturale diversa* (in IRIN: traccia; in PGE: posizione-buffer). La parentela con Caires 2004 è qui consolidata da Roads stesso.

## Collegamento alla tesi centrale

Il paper consolida la *narrazione tre atti* della tesi centrale con un caso documentato dall'interno. Vaggione non sceglie il deferred per vincolo hardware (per la maggior parte della sua carriera il real-time era disponibile, ma la sua opera resta sistematicamente deferred); sceglie il deferred perché il *micromontage by script* + *progressive enrichment* + *graphical multi-scale editing* richiedono un loop lungo come postura nativa. Roads — protagonista della lineage real-time UCSB (PulsarGenerator, EmissionControl) — *firma* nel 2005 l'analisi più dettagliata di un'opera deferred (Vaggione) come *fine art* della composizione elettroacustica contemporanea (p. 308: «*He sets the standard for the electroacoustic music of today*»). Conferma esplicita: il deferred non è anacronismo, è una postura compositiva specifica e validata dalla scena.

Contributo 1 (DSL YAML): Tar Fig. 2 è il precedente CIM/CMR più concreto.
Contributo 2 (partitura grafica): graphical-editor mid-1980s + IRIN timeline 24 variations.
Contributo 3 (STEMS workflow): progressive enrichment di Schall come pattern compositivo che STEMS + cache + Reaper export rendono praticabile.

## Sezioni del paper CIM 2026 dove citare

- **Sezione 1** (introduzione, narrazione tre atti): citare il paper come *certificazione di scena* del deferred come postura — Vaggione, protagonista assoluto, sceglie deferred per ragioni compositive, non hardware.
- **Sezione 2** (sintesi granulare / micromontage tradition): Tar Fig. 2 come precursore concreto del DSL testuale dichiarativo per microeventi.
- **Sezione 3** (architettura PGE — DSL): Tar Fig. 2 come prototipo storico del DSL parametrico; Schall *progressive enrichment* come pattern compositivo che il workflow STEMS rende praticabile.
- **Sezione 4** (partitura grafica): graphical timeline mid-1980s (p. 301) come premessa storica; IRIN timeline 24 variations (Fig. 3) come parente diretto del `score_visualizer` PGE per scelta dell'asse Y non-pitch.
- **Sezione 5** (caso compositivo): citare il workflow Schall (frame 7'30'' + progressive enrichment) come modello di riferimento per descrivere il proprio loop lungo.

## Quote chiave

- p. 297 (Vaggione 1982, *Modelos de Universo*): «*I began by writing a score in music notation derived from the inherent noninteractivity of the system, and the necessity of developing a strategy to produce the wanted sounds before entering the data for synthesis*». Loop lungo *avant la lettre*: scrittura testuale + necessità strategica come conseguenza diretta della non-interattività.
- p. 299 (Vaggione 1984, *Octuor*): «*Beyond 20 events per second, one is no longer dealing with sounds as individual entities. However, the goal in building this linear structure by combining high density of sounds with highly contrasted parametric values was to create a texture showing a kind of kaleidoscopic 'internal' behaviour*». Il lavoro micromontage è già nel 1984 un lavoro sul *comportamento interno* della texture — anticipa l'ascolto *inside the sound* di Truax 2014 per via compositiva.
- p. 300 (Roads): «*Granulation techniques share many similarities with micromontage [...]. Perhaps the best way to draw a distinction between granulation and micromontage is to observe that granulation is inevitably an automatic process: the composer's brush becomes a refined spray jet of sound color. By contrast, a sound artist can realize micromontage by working directly in the manner of a Pointillist painter: particle by particle. It therefore demands unusual patience. Of course, micromontage and granulation techniques can be seamlessly intermingled*». PGE è nel punto di *intermingling*: granulazione algoritmica + DSL che permette di trattare singoli stream/voci/grani come oggetti compositivi nominati.
- p. 301: «*The simple ability to align multiple sounds along a timeline, to zoom in and out, and jump across time scales with the click of a button changed the nature of electroacoustic composition*».
- p. 302 (Vaggione 1999, sul workflow Schall): «*making a frame of 7 minutes and 30 seconds and filling it by 'replacing' silence with objects, progressively enriching the texture by adding here and there different instances (copies as well as transformations of diverse order) of the same basic material*».
- p. 303: «*The availability of dozens of tracks lets the composer work extremely precisely on every time scale*». Razionale storico per il workflow STEMS PGE: il rendering per-stream produce esattamente le *dozens of tracks* su cui il compositore può intervenire in DAW.
- p. 306 (su 24 variations + IRIN Fig. 3): «*Each rectangle represents a sound clip or sample. The vertical position of a sample within a track is not significant (i.e., it does not correspond to pitch). IRIN lets one encapsulate figures within tracks and represent them as a single fragment, permitting a hierarchical building up of mesostructure*».
