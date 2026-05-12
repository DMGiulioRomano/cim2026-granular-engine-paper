# [Caires, 2004] IRIN: Micromontage in Graphical Sound Editing and Mixing Tool

## Citazione CIM

Caires, C. (2004). IRIN: Micromontage in Graphical Sound Editing and Mixing Tool. In *Proceedings of the International Computer Music Conference*, vol. 30, pp. 219–222. Miami, FL: ICMA.

## Argomento centrale

IRIN è un tool di composizione standalone Max/MSP (Mac OS X) per *micromontage*: gerarchia di oggetti sonori (Sample → Figure → Meso-structure → Timeline) con editing grafico, generazione algoritmica e variazione di sequenze. Combina script editing e timeline polifonica con shape-view colorato per ogni grano/sample.

## Gap o problema identificato

I sequencer DAW tradizionali (ProTools, Digital Performer) trattano panning/volume come proprietà *track-dependent*: spostare un evento tra tracce ne altera proprietà. Per micromontage — dove ogni sample è un atto compositivo con memoria di tutte le sue trasformazioni — serve un ambiente che mantenga le proprietà *track-independent* dell'oggetto sonoro. Inoltre il tracking di "all important sound operations" sui grani richiede architettura object-based dedicata, non offerta dai DAW.

## Rilevanza diretta per PGE

Quattro punti di contatto:

1. **Gerarchia oggetti come precursore semantico** (non architetturale): Sample/Figure/Meso-structure di IRIN sono progettati come categorie compositive con eredità di proprietà ("Each class inherits the properties of its predecessor"). PGE non eredita la classificazione (Stream/Voice/Controller sono assi ortogonali), ma condivide la postura: *il grano non è un oggetto medio*, è istanziazione di una specifica decisione compositiva con memoria delle sue trasformazioni.

2. **Timeline con shapes view come precursore concreto del score_visualizer PGE**: Caires sceglie esplicitamente che le proprietà del suono (envelope, panning, phase shift) siano "track-independent feature" — la traccia è metafora di rigo di partitura, non bus audio DAW. La Timeline IRIN diventa partitura grafica multi-traccia con shapes colorate, dove "local sound agglomerations are easily tracked at a quick glance, since the materials can be arranged as if they were in a score". È la stessa postura di score_visualizer di PGE: la rappresentazione visiva non è ridondanza del playback ma strumento compositivo autonomo.

3. **Granulator inside Figure Editor**: IRIN integra un granulatore che genera "a stream of a pre-defined number of particles with a particular behaviour as regards the evolution of their properties" (duration, distance, phase shift, filtering), poi modificabile manualmente per singola istanza. È esattamente il pattern *global laws + per-grain manual edit* che PGE realizza via ParameterOrchestrator + dephase per-grano: il grano nasce da una specifica parametrica ma è singolare.

4. **Phase shift come *décorrélation microtemporelle* esplicita**: nota 2 di Caires cita Vaggione 2002b in modo letterale: "Phase shifting in this context is used as a composition technique belonging to the micro-scale domain (*micro decorrélation temporelle*). It concerns the definition of spatial attributes of small sound particles by placing micro delayed replica of it into different channels". IRIN è il primo sistema documentato (CIM-tradition) che implementa la décorrélation microtemporelle come *attributo per-sample editabile graficamente*. PGE realizza lo stesso meccanismo via VoiceManager + dephase Controller in modalità deferred declarativa.

## Collegamento alla tesi centrale

Caires 2004 è la **realizzazione operativa diretta del programma transformational di Vaggione** (Caires è studente di Vaggione: «I should like to thank my supervisor, Horacio Vaggione»). IRIN materializza in software gli oggetti Vaggione 1991/1996 + décorrélation Vaggione 2002, sei anni prima di PGE. Posizionamento argomentativo nel paper PGE:

- IRIN è offline (Max/MSP standalone con render finale a file multitraccia) → conferma che la tradizione transformational *richiede tempo differito* per memoria-di-tutte-le-azioni e proliferazione organica del materiale.
- IRIN sceglie GUI grafica come superficie compositiva → polo opposto del DSL YAML di PGE sulla stessa famiglia di problemi. Il loop lungo Caires passa per direct manipulation; quello PGE per scrittura testuale + visualizer come output.
- La partitura-Timeline IRIN è *score editabile come input* (si suona/renderizza ciò che si edita); score_visualizer PGE è *score come output ispezionabile* (si renderizza ciò che si scrive in YAML). Stessa categoria (study score per micromontage granulare), inversione di flusso.

## Sezioni del paper CIM 2026 dove citare

- **Sezione 2** (sintesi granulare): IRIN come prosecuzione CIM-tradition del paradigma micromontage Roads/Vaggione; conferma vitalità del tempo differito nel 2004 in piena epoca real-time disponibile (Truax DMX-1000 1986, Max/MSP audio 1998).
- **Sezione 3** (architettura PGE): contrasto GUI direct-manipulation (IRIN) vs DSL testuale (PGE) come due risposte legittime al problema *come specificare micromontage*; Sample/Figure/Meso ≠ Stream/Voice/Controller ma stessa motivazione (memoria delle trasformazioni).
- **Sezione 4** (partitura grafica): IRIN Timeline shapes-view come precedente concreto di partitura granulare multi-traccia con encoding cromatico-formale; differenziatore PGE: asse Y = posizione nel buffer (PGE) vs asse Y = numero di traccia (IRIN). PGE rappresenta il *meccanismo di lettura nel sample*, IRIN il *layout polifonico degli eventi*.

## Quote chiave

- p. 219 (sezione 1, motivazione architettura object-based):
  > «sound transformation, far from a mere "effect", is an act of composition, a memory of all actions and respective data involved within the process of creating the tiniest sound particle is needed so that a consistent proliferation of the musical material can be achieved.»

- p. 220 (nota 2, décorrélation microtemporelle come tecnica compositiva):
  > «Phase shifting in this context is used as a composition technique belonging to the micro-scale domain (*micro decorrélation temporelle*). It concerns the definition of spatial attributes of small sound particles by placing micro delayed replica of it into different channels (Vaggione 2002b).»

- p. 222 (sezione 4, Timeline come metafora di score):
  > «As a metaphor for score staffs, tracks may be used precisely as a compositional tool, helping the composer to arrange the polyphonic stratification of his material in a more systematic way.»
