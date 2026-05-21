# [Di Scipio, 1995] Real-time Polyphonic Time-shifting of Sound with Interactive Systems

## Citazione CIM

Di Scipio, A. (1995). Real-time Polyphonic Time-shifting of Sound with Interactive Systems. In *Atti del XI Colloquio di Informatica Musicale*, pp. 19–22. Bologna: AIMI.

## Categoria e lunghezza

Scientific Session "Digital Signal Processing (I)" — comunicazione orale — 4 pagine — 11 riferimenti bibliografici (Bregman 1990; De Poli/Piccialli/Roads eds. 1991; Di Scipio 1994ab/1995; Jones & Parks 1988; Rowe 1993; Scaletti & Hebel 1991; Simon & Newell 1970; Tisato & Di Scipio 1993; Truax 1988).

## Argomento centrale

Metodi di **granular processing real-time** per time-shifting polifonico del suono live (alterazione durata senza side-effects in frequenza) e granulazione ricorsiva. Caso d'uso: brani *Hybris* (g-flute, basso clarinetto + computer, 1994) e *Essai du vide. Schweigen* (tape, 1993). Sistemi: **KYMA/CAPYBARA** (LMS L'Aquila) + **PODX/GSAMX** su DMX-1000 (Simon Fraser).

## Sistema o strumento descritto

- **HYBRIS1** algoritmo su KYMA 2.0 / CAPYBARA DSP (poi portato KYMA 4.0). Smalltalk-80 scripts annidati (`HYBRIS1` scheduling 4 `RTPTM`, ciascuno scheduling 4 `INSTR`). Nuova classe `aSample&ShiftWithAllPass` con icona + parametri custom (grain duration, stretch factor, allpass delay, spatial trajectory).
- **GSAMX** su PODX/DMX-1000 (Simon Fraser, B. Truax), accesso real-time via single line shell sul PDP Micro11. Parametri: avg grain dur, dur range, intergrain delay/density, intergrain range, time-shift ratio.
- Pipeline interna granulator: input → 5" wavetable cyclic write (wrap m volte) → cyclic lookup pointer (rampa/gaussiana/slider) → minimum lookup increment = grain duration → gaussian/trapezium envelope → allpass filter (delay = grain_dur/2) → stream. Due granulatori sfalsati di metà grain duration = uno "stream of grain". Grain duration 10–70 ms. Intergrain delay e allpass delay random entro range = "asynchronous granulation". Parametri micro-tempo opzionalmente sincroni a pitch tracking dell'input.

## Analogia con PGE

Granulazione real-time esce dal perimetro PGE. Però:

- **Layering polifonico di stream con parametri propri** (4 processi avviati a 5"/10"/15"/20" con ratio 5×/4×/3×/2× più lenti del reale) — pattern strutturalmente analogo allo *Stream* PGE come unità di traccia con parametri propri, schedulata a offset. Diversità: PGE concretizza scheduling in YAML offline; *Hybris* lo concretizza in script Smalltalk-80 a runtime KYMA.
- **Recursive granulation** `x_{n+1} = f_b(f_a(x_n))` (granulazione + accesso random + granulazione ricorsiva) in *Essai du vide*: iterazione nonlineare composizionalmente significativa. PGE non implementa granulazione ricorsiva direttamente, ma il workflow STEMS (rendering per-stream + reimport DAW + re-input) abilita la composizione di passaggi ricorsivi nella DAW.
- **aSample&ShiftWithAllPass** come nuovo oggetto custom esposto con parametri rehearsing-time = anticipa l'idea di astrazione DSL: i parametri pubblici di un oggetto compositivo sono solo quelli rilevanti per la sessione, gli altri customizzati e nascosti.

## Posizionamento storico

**Snodo Di Scipio offline → real-time** (1991/1993 → 1995). Lo stesso autore che nel 1991 (IX CIM) e 1993 (X CIM) operava in tempo differito su IBM PC 286 e mainframe IBM 9121, in 1995 (XI CIM) opera real-time su CAPYBARA e DMX-1000. Documenta sul piano CIM la transizione di paradigma annunciata Di Scipio/Tisato 1993 p. 165 ("near future in a real-time version on a NeXT computer"). PGE 2026 è il *ritorno volontario* al tempo differito *dopo* che questa transizione si è compiuta.

Filone: real-time + controllo interattivo + composizione live → opposto al filone tempo-differito offline italiano (1988 De Poli-Piccialli, 1989 Ortosecco-Piccialli, 1991/1993 Di Scipio stesso).

## Note stilistiche

- Struttura: 1 Introduction (1.1 microcomposition, 1.2 notion of interactivity), 2 Polyphonic time-shifting (2.1 granulation of live sound, 2.2 algorithmic control in Hybris, 2.3 KYMA implementation, 2.4 considerations), 3 Recursive processing (3.1 Essai du vide), References. Apertura su brani concreti, chiusura su implicazioni compositive.
- **Tono argomentativo, non descrittivo.** Quote pietra-angolare p. 19: *"Interactivity requires the possibility of exerting real-time controls over various parts of a program such that both the sonic and syntactic levels can be accessed by the user"* — chiarisce che interattività ≠ "immediate audible output", ma accesso a livelli sintattici a rate diversi (audio-rate, event-rate, higher). Distinzione esplicita 4 classi: composition/performance × program/environment.
- Quote p. 21 sulla performance: *"the performer becomes here a source of feedback and self-regulation within a dynamical system. Far from being a just matter of reproducing written symbols into audible sounds, his/her task is more one of self-regulating the whole 'performance system' in order to avoid totally uncontrolled results as much as strictly periodic behaviors."*
- Quote p. 22 su recursive granulation: *"It is a method for subtracting energy from the sound, in opposition to methods of granular synthesis: in the former case one puts 'quanta of silence into the sound', in the latter 'puts quanta of sound in the otherwise silent flow of time'."* — capovolge framing Roads "quanta of sound into silence" come dialettica costruttiva.
- 1 figura inline (HYBRIS1 algorithm graph, oggetti KYMA top-down). Pseudocode Smalltalk-80 in monospace. Tabelle stretch ratio implicite nel testo.

## Sezioni del paper CIM 2026 dove citare

- **Sezione 2** (Sintesi granulare: dal paradigma Gabor al controllo gerarchico) — citare come **bookend** del filone Di Scipio: 1991/1993 offline → 1995 real-time. Chiude la transizione di paradigma; nel 2026 PGE riapre la posizione offline come postura compositiva volontaria, non come vincolo hardware.
- **Sezione 5** (Caso compositivo) — *Hybris* + *Essai du vide* come modelli stilistici di paper compositivo CIM: descrizione del brano con dettagli tecnici intercalati a riflessione estetica (microcomposition, performer come feedback). Tono argomentativo applicabile alla sezione caso compositivo PGE.
- **Sezione 6** (Conclusioni) — la distinzione 4-quadrant composition/performance × program/environment offre vocabolario per posizionare PGE nello spazio: *interactive composition program* (case 1 di Di Scipio). PGE è programma + offline + composizione = differito → tempo lungo del loop come dimensione interattiva ad un *rate* lento.
