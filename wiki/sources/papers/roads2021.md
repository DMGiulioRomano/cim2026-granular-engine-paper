# [Roads, Kilgore, DuPlessis, 2021] Architecture for Real-Time Granular Synthesis With Per-Grain Processing: EmissionControl2

## Citazione CIM
Roads, C., Kilgore, J., and DuPlessis, R. (2021). Architecture for Real-Time Granular Synthesis With Per-Grain Processing: EmissionControl2. *Computer Music Journal*, 45(3), pp. 20–38. doi:10.1162/COMJ_a_00613

## Argomento centrale
EC2 è un granulatore real-time cross-platform (MacOS/Windows/Linux) con per-grain processing: ogni grano può avere valori unici per tutti i 15 parametri di granulazione (envelope, waveform, amplitude, frequency, spatial position, filter center, filter resonance). Il paper descrive l'architettura, la GUI, la teoria di operazione (scanning/playback rate), il motore a 3 stadi (Granulation Controls / Grain Generation / Grain Emission) e i casi d'uso (insegnamento, studio, performance, generative music).

## Gap o problema identificato
EC2 riconosce esplicitamente la complessità del parametro space granulare come sfida principale: "The tradeoff for laying bare the nuts and bolts of granular synthesis is that beginners can feel overwhelmed when first launching EC2." La risposta è una GUI ergonomica con color-grouping (Tabella 2: blu=timing, verde=pitch, giallo=source, rosso=ampiezza/spazio), preset con morphing, e 6 LFO indipendenti per modulazione. Il limite rimane nell'approccio gestural: la specifica dello spazio parametrico passa attraverso slider e presets, non attraverso un linguaggio dichiarativo. Non esiste una rappresentazione esplicita delle intenzioni compositive al di fuori del gesto immediato.

## Rilevanza diretta per PGE
EC2 e PGE condividono la stessa lineage architetturale ma incarnano paradigmi opposti:

**Corrispondenze strutturali dirette:**
| EC2 | PGE |
|-----|-----|
| Scanner (scan_begin, scan_range, scan_speed) | PointerController (pointer_start, loop, speed_ratio) |
| Grain Rate + Asynchronicity + Streams | DensityController (fill_factor/density, sync/async/blend, num_voices) |
| Per-grain LFO modulation | Envelope/ProbabilityGate strategies in ParameterOrchestrator |
| Grain Duration | grain_duration (StreamConfig) |
| Playback Rate | PointerController.playback_rate (equivalente funzionale) |
| Scan Display (waveform + grain pointers in real-time) | Score Visualizer (Y = posizione buffer, frecce) |

**Differenze paradigmatiche:**
- EC2 è *gestural/interactive*: il compositore agisce in tempo reale, modifica slider mentre l'audio scorre, "the tape is running." Il modo d'uso studio è: registrare output continuo e "cull the good parts" (p. 32).
- PGE è *declarative/deferred*: il compositore specifica intenzioni parametriche in YAML, genera, ascolta, riflette, riscrive. Non c'è tape che scorre — c'è un ciclo deliberato.
- EC2 ha un Scan Display real-time che mostra i grain pointers sul waveform. PGE ha una partitura grafica generata post-synthesis che mostra Y=posizione-buffer con encoding visivo di tutti i parametri per grano. Stesso fenomeno fisico (lettura nel buffer), rappresentazioni diverse con scopi diversi: EC2 = feedback immediato; PGE = analisi e riflessione post-generazione.

**OSC scripting in EC2** (introdotto in v1.2): apre la porta al controllo algoritmico, ma come scripting esterno che invia messaggi OSC — non come DSL integrato con schema semantico, validazione, e Language Server.

## Collegamento alla tesi centrale
EC2 è il polo opposto della postura PGE: massima accessibilità al feedback immediato, controllo gestural, nessun layer di specifica dichiarativa. È il rappresentante più avanzato del paradigma real-time che Truax (1988) aveva inaugurato. PGE non compete con EC2 nella dimensione real-time/gestural; occupa una posizione diversa nello spazio compositivo: quella del loop lungo, della specifica deliberata, del ritorno volontario al tempo differito come spazio di indagine parametrica. I due sistemi sono complementari, non sostitutivi. Citare EC2 in conclusioni come sviluppo futuro (GUI, integrazione real-time opzionale) e in sezione 3 come confronto architetturale.

La separazione scanner/playback in EC2 (p. 26, Tabella 3: time-stretched = scan_speed 0.5, playback_rate 1; pitch-shifted down = scan_speed 1, playback_rate 0.5) è la stessa separazione che PointerController e PitchController di PGE implementano in modo indipendente — confermando la scelta architetturale di PGE.

## Sezioni del paper CIM 2026 dove citare
- Sezione 3 (PGE: architettura per l'indagine parametrica): confronto architetturale diretto — stessa lineage (scanner/density/per-grain), paradigma diverso (declarative vs gestural). Tabella comparativa EC2 vs PGE sarebbe utile.
- Sezione 6 (Conclusioni): EC2 come punto di riferimento per sviluppi futuri (GUI interattiva, modalità real-time opzionale come estensione del workflow PGE).

## Quote chiave
- p. 20 (Abstract): "By contrast, we believe that it is more interesting from an aesthetic standpoint to articulate heterogeneity at the micro time scale of individual grains."
- p. 32 (Studio Composition): "In studio composition, the presumed mode of work is a constant the 'tape is running.' Later the 'good parts' can be culled from the recording."
- p. 35 (Evaluation): "We designed EC2 as a professional instrument that does not attempt to hide the complexity of granular synthesis. All of the important parameters for real-time granular synthesis can be directly controlled by the user."
