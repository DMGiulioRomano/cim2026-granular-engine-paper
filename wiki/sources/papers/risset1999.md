# [Risset, 1999] Composing in Real-time?

## Citazione CIM

Risset, J.-C. (1999). Composing in real-time? *Contemporary Music Review*, 18(3), 31–39. DOI: 10.1080/07494469900640331.

## Argomento centrale

Risset gioca esplicitamente all'*avvocato del diavolo*: dopo aver descritto il proprio *Duet for one pianist* (1989, MIT con Scott Van Duyne) — interazione real-time fra pianista e Disklavier via Max — argomenta in cinque punti che la disponibilità del real-time **non è un progresso per la composizione**. Tesi conclusiva: «*Composition is not — or should not be — a real-time process*» (p. 37). La composizione richiede di sottrarsi alla freccia del tempo; il real-time appartiene alla *performance*, non alla *scrittura*.

## Gap o problema identificato

L'entusiasmo per il real-time in IRCAM e nei centri computer-music degli anni '90 ha portato a considerare i sistemi non-real-time *obsoleti*. Risset segnala cinque drawback strutturali:

1. **Complessità sonora limitata** in RT (anche con tecnologia avanzata il limite esiste; complessità ottenuta via *layering* = sospensione del RT).
2. **Flessibilità ridotta** rispetto al software synthesis: i parametri controllabili in RT sono selezionati *ahead of time*, spesso non dal compositore.
3. **Real-time non risolve il mastering della sintesi**: l'illusione di sintonizzare per intuizione e orecchio porta a manipolazioni casuali tipo *Rubik cube*. Patterns facili da produrre live diventano cliché.
4. **Effimerità tecnologica**: pezzi RT legati a specifico hardware muoiono col mutare delle piattaforme — rischio di *perishable, memoriless electronic art*.
5. **Music for tape è viva**: registrazione = pratica matura (Boulez/Lulu/Stratas come modello), tape concerts producono esperienze irreproducibili a casa.

Quattro propri brani (*Mutations* 1969, *Sud* 1985, *Invisibles* 1994, *Voilements* 1987) sono esempi documentati di tecniche **non realizzabili in real-time**: filtro non-causale, time-stretching che incrocia l'originale, sincronizzazione di voci a submultipli di 20 s, processing armonico di voce time-stretched.

## Rilevanza diretta per PGE

**Rilevanza massima — voce critica contemporanea che articola in CMR 1999 la postura compositiva che PGE 2026 materializza tecnicamente.** Risset enuncia il programma di un *ritorno volontario al deferred* 27 anni prima dell'implementazione PGE, in un momento in cui il deferred era già abbandonato come obsoleto.

Quattro corrispondenze dirette con i contributi PGE:

- **Loop lungo come necessità compositiva**: Risset p. 36 *"the construction of the piece may take a lot of patience: but one should also be able to conceive it in a synoptic way, at a glance much faster than the flow of musical time"* = formulazione esplicita CMR 1999 del *loop di feedback* lungo PGE (specifica → generazione → ascolto → riflessione → riscrittura). La doppia temporalità — patience della costruzione + visione sinottica del piano — corrisponde all'asse paper testuale (YAML) + asse partitura grafica (`score_visualizer`) del workflow PGE.
- **Drawback 3 (mastering)** = razionale CMR diretto dell'**esposizione totale dei parametri nel DSL YAML**: la conoscenza accumulata sui modelli sonori è inutilizzabile nei sistemi RT perché *"the significance of the control settings is often unknown or obscure, and one cannot always exert useful bookkeeping"* (p. 34). YAML PGE + Language Server + Score Visualizer sono la risposta operativa al *bookkeeping* invocato da Risset.
- **Drawback 4 (effimerità)** = razionale CMR per l'**architettura textual + open-source** PGE: Risset p. 35 *"the compositional structure should be explicited clearly in term of basic operations that should be made available in future devices"*. YAML + IR Python + renderer pluggable (Csound/NumPy/Reaper) realizza questo principio (la specifica sopravvive al renderer specifico).
- **Drawback 5 (musique sur support viva)** = legittimazione esplicita della pratica deferred come tradizione viva, **non ripiego**. Risset cita le tradizioni francesi GRM/GMEB/GMEM/CIRM, il progetto IDEAMA (ZKM+CCRMA), come prova istituzionale che la musica registrata è oggetto di concerto e di archivio.

**Tassonomia ibrida CMR 1999**: Risset (p. 36) presenta *Voilements* (1987) come modello operativo di articolazione *RT performance data → deferred synthesis*: MIDI keyboard cattura nuances in RT → conversione formato MUSICV → sintesi differita complessa. È il pattern *gesture capture + deferred render* che PGE non implementa ma di cui anticipa l'urgenza. Note Risset stesso p. 37 che il ruolo del RT in questo workflow è *cosmetic rather than structural*.

**Anti-analogia controllata** con il *Duet for one pianist* (1989): Risset compositore che pratica RT mentre dichiara filosoficamente di rifiutarlo come paradigma compositivo. Stessa coabitazione che si trova in Di Scipio 1995 (offline + real-time nello stesso periodo) e Silvestri 2010 (*Studio Sonoro III* RT + nastro nella stessa opera). PGE = scelta polare opposta: rifiuto operativo del RT come paradigma, non solo come filosofia.

## Collegamento alla tesi centrale

**Diretto — voce d'autorità storica per l'obiezione+risposta di `sec:implicazioni`.** Risset 1999 è il testo CMR che articola per primo, in forma argomentativa esplicita, il *ritorno volontario al tempo differito* che il paper CIM 2026 argomenta in chiusura:

- **Atto 1 narrazione tre atti** (Roads 1978 / Di Scipio 1991: deferred come vincolo): Risset riconosce il vincolo storico ma dichiara che la sua caduta non rende il deferred obsoleto.
- **Atto 2** (con Truax 1988 il vincolo hardware cade): Risset documenta la genealogia dei sistemi che resero il real-time disponibile (GROOVE 1970, Synclavier 1974, Chadabe 1981, Vercoe synthetic performer, Manoury *Jupiter*, Puckette/Dannenberg, Disklavier 1989) — la genealogia CMR del modo operativo, scritta da chi lo praticava.
- **Atto 3** (PGE: ritorno volontario): Risset 1999 enuncia esplicitamente la posizione *prima* che diventi praticabile su laptop. La sezione *Composition and real-time* (pp. 36–37) è la **fonte filosofica diretta** per la formulazione del paper CIM 2026: non «meglio differito», ma «differito = configurazione necessaria per un certo tipo di lavoro compositivo».

**Quote-pietra-angolare p. 37** *"Non real-time operation is necessary to free oneself of the arrow of time and its tyranny, of the dictates of haste, instancy, habits, reflexes. Writing music implies prediction and elaboration"* = formulazione CMR 1999 della **postura PGE**. Risset cita Virilio (*L'art du moteur* 1993) e Borges per articolare la critica filosofica del *real-time technological frenzy* — registro che il paper richiama in `sec:implicazioni` per inquadrare il loop lungo non come arretratezza tecnica ma come configurazione operativa contro l'*immediate satisfaction*.

**Posizionamento rispetto alla tradizione CIM**: Risset 1999 sta a CMR come Di Scipio 1991/1994 sta a CIM — formulazione coeva ma asse di motivazione differente (CMR filosofico/anti-Virilio; CIM vincolo hardware + teoria del *detailed sonic design*). PGE eredita la postura da entrambi i fronti: Di Scipio per la metodologia del ciclo iterativo, Risset per la difesa argomentativa esplicita del deferred contro l'egemonia RT.

## Sezioni del paper CIM 2026 dove citare

- **`sec:implicazioni`** (primaria): precedente filosofico del ritorno
  volontario («*Composition is not — or should not be — a real-time
  process*», «*arrow of time and its tyranny*», p. 37).

Fonte di verità: [[mappa-citazioni-paper]].

## Quote chiave

- p. 37: «*Composition is not — or should not be — a real-time process. Musical notation applies time over space. It refers the reality of the music to a representation — the score — which is out of time. This representation suggested transformations that could not be conceived or performed in real-time — such as symmetries with respect to the pitch or the time axis used in counterpoint. Non real-time operation is necessary to free oneself of the arrow of time and its tyranny, of the dictates of haste, instancy, habits, reflexes. Writing music implies prediction and elaboration.*»
- p. 35: «*Porting a piece realized on a real-time system onto another one is hard and uninspiring work, so that many composers produce a new piece rather than adapting their piece for the new device. This situation leaves no chance to develop traditions for performance or to let musical works become classics. It brings the risk of a perishable, memoriless electronic art. [...] the compositional structure should be explicited clearly in term of basic operations that should be made available in future devices.*»
- p. 37: «*Our epoch is too keen on immediate satisfaction. Impatience favors hasty, blind or reflex reaction rather than documented and thoughtful action. It jeopardizes memory. Paul Virilio draws attention on the danger of succumbing to the frenzy of real-time technologies and to break "the wall of time".*»
