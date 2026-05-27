# Tradizione del tempo differito nella sintesi granulare — dal vincolo al ritorno volontario

## Definizione

Il *tempo differito* (deferred time, offline, non-real-time) è la modalità operativa in cui la specifica compositiva e il rendering audio sono separati temporalmente: il compositore scrive, il sistema genera, il compositore ascolta *dopo*. Nella sintesi granulare, il tempo differito nasce come vincolo hardware (1978–1993) e viene abbandonato quando il real-time diventa praticabile (Truax 1988). PGE vi ritorna volontariamente come postura compositiva: il loop lungo — specifica → generazione → ascolto → riflessione → riscrittura — è lo spazio necessario per abitare gli spazi compositivi della granulazione come forma e struttura.

## Tre atti della narrazione

### Atto 1 — Tempo differito come necessità (1978–1993)

Il vincolo è documentato esplicitamente in tre nodi CIM:

- **Roads 1978** ([[roads1978]]): AGS su B6700, front-end ALGOL per MUSIC V. Nessuna alternativa real-time. Il pattern *front-end → engine* nasce qui.
- **Roads 1985 CIM VI** ([[roads1985]]): Music II al MIT, 64 KB address space, max 32 eventi simultanei. «*Past implementations of granular synthesis have been stymied by hardware and software restrictions*» (pp. 205–206). Propone 4X IRCAM come target real-time futuro.
- **Di Scipio 1991 CIM IX** ([[discipio1991]]): IBM PC 286 offline. «*Queste procedure sono attualmente implementate in tempo differito [...] un problema attualmente insormontabile sta nella quantità di RAM*» (p. 345). Formulazione canonica CIM del vincolo hardware.
- **Di Scipio/Tisato 1993 CIM X** ([[discipio-tisato1993]]): ICMS su IBM 9121 mainframe, *zeitwerk*. Ultimo nodo maturo della tradizione offline italiana; annuncia «near future in a real-time version» (p. 165).

Il pattern architetturale di questo atto — separazione tra linguaggio di specifica e motore di rendering — è il pattern che PGE eredita.

### Atto 2 — Il vincolo cade, il differito viene abbandonato (1988–)

- **Truax 1988** ([[truax1988]]): DMX-1000, primo sistema granulare interamente real-time. «*The key is to abandon linear modes of compositional thinking, which result in deterministic output (e.g., score or sequencer driven), and to substitute process-oriented multitask strategies for real-time execution*» (p. 19). Il real-time non è solo possibilità tecnica: è cambio di paradigma compositivo.
- **Di Scipio 1995 CIM XI** ([[discipio1995]]): stesso autore dell'atto 1 ora opera real-time su KYMA/CAPYBARA e PODX/DMX-1000. Documenta sul piano CIM la transizione annunciata nel 1993.
- **Lippe 1993 CIM X** ([[lippe1993]]): ISPW real-time nello stesso volume di Di Scipio/Tisato offline — la transizione è documentata *dentro un singolo Atti CIM*.

### Atto 3 — Ritorno volontario al tempo differito (PGE)

PGE compie il percorso inverso: torna al tempo differito in un momento in cui il real-time è disponibile. Questo ritorno non è regressione — è postura compositiva. Il differito abilita:

- **Loop lungo a scala riflessiva**: il compositore non reagisce all'istante ma riflette tra cicli di rendering. Il giudizio drammaturgico opera sulla riflessione, non sull'atto immediato.
- **Economy of selection** (Roads 2012, pp. 28–29, [[roads2012]]): «*choosing one or a few perceptually and aesthetically optimal or salient choices from a vast desert of unremarkable possibilities*». Il loop lungo è la cornice operativa di questa scelta.
- **Indagine parametrica**: specifica YAML → generazione → partitura grafica → ascolto → riscrittura. Il tempo differito è lo spazio per abitare il gap `d·n` (parametri × grani) identificato da Roads 1985.

## Precedenti CIM della coesistenza RT/differito

Il ritorno al differito non è anomalia — la tradizione CIM documenta la coesistenza:

- **Di Scipio 1994** ([[discipio1994]]): usa sia differito (*kairós* IBM486, *Zeitwerk* IBM3090) sia real-time (*Essai du vide* GSAMX). La postura indeterministica non è vincolata al differito ma al ciclo iterativo.
- **Silvestri 2010 CIM XVIII** ([[silvestri2010]]): *Studio Sonoro III* «interamente basata su algoritmi di wavetable multiplexing implementati sia per la sintesi in tempo reale che, per la parte per nastro, in tempo differito» (nota 10, p. 210). Data-point CIM 2010 della coesistenza nella stessa opera.
- **Arcella/Silvestri 2012 CIM XIX** ([[arcella-silvestri2012]]): pipeline C++ → Csound score → audio, batch by design. «*Variants of the first approach would be required for realtime versions*» (p. 148). Il real-time è opzione non perseguita.
- **Roads 2012** ([[roads2012]]): «*Detached from real-time constraints, ideas can be tested, edited, submixed, or deleted at will*» (p. 8). Formulazione canonica della postura differita dal principale protagonista della lineage real-time-virtuosica. Ammette il fallimento Creatovox: la virtuosità del momento non è il giudice, l'ascolto riflesso lo è.
- **Markidis/Fernández 2016 CIM XXI** ([[markidisfernandez2016]]): sistema presentato come real-time ma con «analisi, ordinamento del database, calcolo dei primi vicini» in tempo differito (p. 181). Riconoscimento CIM 2016 che parte sostanziale del workflow è offline anche in sistemi real-time.

## Legittimazione teorica

Tre fonti convergono sulla legittimità del differito come *configurazione temporale dell'interazione*, non sua negazione:

1. **Di Scipio 1995** (p. 19): «*interactivity cannot simplistically mean immediate audible output*» — il rate del feedback determina la scala temporale dell'interazione, non la sua presenza. Cfr. [[interactivity-rate]].

2. **Solomos/Vaggione 2003** ([[solomos2003-ent04-de-loperatoire]], p. 232): «*aujourd'hui, le compositeur ne se limite plus à planifier un processus pour le regarder marcher tout seul [...] il interagit à tout moment avec lui*». Chi sceglie il differito *oggi* lo sceglie come postura, non come vincolo.

3. **Arcella/Silvestri 2012** (p. 148): «*Tools and technologies used to produce a musical work are not neutral but incorporate knowledge that influence the choices of the composer*». Lo strumento differito non è neutro — incorpora la postura del loop lungo.

## Tavola sinottica

| Anno | Autore | Sistema | Modalità | Motivazione |
|------|--------|---------|----------|-------------|
| 1978 | Roads | AGS / MUSIC V | differito | vincolo hardware |
| 1985 | Roads (CIM VI) | Music II / MIT | differito | vincolo 64 KB |
| 1988 | Truax | DMX-1000 | **real-time** | cambio di paradigma |
| 1991 | Di Scipio (CIM IX) | IBM 286 | differito | vincolo RAM |
| 1993 | Di Scipio/Tisato (CIM X) | ICMS IBM 9121 | differito | ultimo nodo offline |
| 1993 | Lippe (CIM X) | ISPW | **real-time** | stesso volume CIM |
| 1994 | Di Scipio | kairós + Essai du vide | **entrambi** | postura, non vincolo |
| 1995 | Di Scipio (CIM XI) | KYMA/CAPYBARA | **real-time** | transizione completata |
| 2010 | Silvestri (CIM XVIII) | Csound + PD | **entrambi** | coesistenza nella stessa opera |
| 2012 | Arcella/Silvestri (CIM XIX) | C++ → Csound | differito | batch by design |
| 2012 | Roads | Pro Tools studio | differito | economy of selection |
| 2026 | PGE | Python → Csound/NumPy | **differito** | ritorno volontario |

## Fonti

- [[roads1978]] — AGS front-end MUSIC V, pattern architetturale
- [[roads1985]] — primo CIM, vincolo 64 KB, programma futuro
- [[roads2012]] — economy of selection, studio detached, fallimento Creatovox
- [[truax1988]] — DMX-1000, abandon linear thinking
- [[discipio1991]] — vincolo RAM, formulazione canonica CIM
- [[discipio-tisato1993]] — ultimo nodo offline, programma DSL
- [[discipio1994]] — coesistenza differito/real-time come scelta
- [[discipio1995]] — transizione completata, taxonomy 4-quadrant
- [[lippe1993]] — real-time nello stesso Atti del differito
- [[silvestri2010]] — coesistenza RT/differito nella stessa opera
- [[arcella-silvestri2012]] — pipeline batch, strumenti non neutri
- [[markidisfernandez2016]] — offline dentro il real-time
- [[interactivity-rate]] — ridefinizione interattività come rate
- [[solomos2003-ent04-de-loperatoire]] — triangolarité, interaction permanente

## Sezioni del paper CIM 2026 dove citare

- **Sezione 1 (Introduzione)**: narrazione tre atti come struttura portante. Roads 1985 + Di Scipio 1991 (atto 1) → Truax 1988 (atto 2) → PGE (atto 3). Quote Di Scipio 1991 p. 345 + Truax 1988 p. 19 come poli della transizione.
- **Sezione 2 (Sintesi granulare)**: precedenti CIM della coesistenza (Di Scipio 1994, Silvestri 2010) per disarmare la lettura del differito come regressione.
- **Sezione 6 (Conclusioni)**: economy of selection (Roads 2012) come teorizzazione del loop lungo; strumenti non neutri (Arcella/Silvestri 2012) come ancoraggio CIM della postura.
