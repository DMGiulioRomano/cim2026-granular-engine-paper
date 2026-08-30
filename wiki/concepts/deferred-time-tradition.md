# Tempo differito nella tradizione CIM/CMR — narrazione tre atti

## Definizione

Per *tempo differito* (*deferred time*, *non-real-time*, *offline*) si intende il regime operativo in cui specifica della sintesi e generazione del segnale audio non coincidono temporalmente con l'ascolto. Il compositore scrive una specifica (score Music-N, programma ICMS, YAML), un motore traduce in samples in tempo non vincolato alla durata del risultato, l'ascolto avviene a valle. Si oppone al *tempo reale* (RT), in cui generazione e ascolto sono simultanei e la specifica è interrotta dalla performance.

La distinzione **non** è binaria tecnica fra latenza zero e latenza positiva: è una distinzione di **regime compositivo** lungo l'asse del *rate di feedback* fra specifica e ascolto (cfr. [[discipio1995]] p. 19: «*interactivity cannot simplistically mean immediate audible output [...] it also means that the user can address his/her action to different rates of change*»). Il deferred PGE è il polo lento di questo asse, non l'assenza di interazione.

## Tre atti della tradizione

Narrazione che alimenta il **primo paragrafo di «tradizione» (sezione rimossa, confluita in `sec:conclusioni`)** (genealogia
compressa) e l'**obiezione+risposta di «implicazioni» (sezione rimossa)**. NON fonda
l'introduzione: per direttiva maestro 2026-05-28 il paper apre problem-driven,
senza narrazione tre atti (cfr. [[incontro-maestro-2026-05-28]],
[[modelli-stilistici-bottom-up]]).

### Atto 1 — Deferred per vincolo hardware (1975–1993)

Il tempo differito è l'**unica modalità possibile** finché i DSP commerciali non hanno né RAM né throughput per granulazione real-time su suoni campionati.

- **[[roads1978]]** — *Composing Granular Sound Textures with PLF Routines* (CMJ 1978): primo esempio documentato di architettura *deferred-time + linguaggio compositivo separato dall'engine audio* (PLFs in B6700 Extended ALGOL come front-end MUSIC V). PGE eredita lo stesso pattern (generator.py → renderer Csound/NumPy).
- **[[roads1985]]** — CIM VI 1985: Music II al MIT, 64 KB address space, max 32 eventi simultanei. «*Past implementations of granular synthesis have been stymied by hardware and software restrictions*» (pp. 205–206). Propone 4X IRCAM come target real-time futuro.
- **[[discipio1991]]** — *Caos deterministico, composizione e sintesi del suono* (CIM IX 1991). Quote pietra-angolare p. 345: *«Queste procedure sono attualmente implementate in tempo differito, su un IBM PC 286 [...] un problema attualmente insormontabile sta nella quantità di RAM nella quale il segnale da ridurre in grani è conservato»*. Formulazione canonica CIM-interna del vincolo hardware come causa del deferred.
- **[[depoli-piccialli1988]]**, **[[ortosecco-piccialli1989]]** — sintesi granulare sincrona / wavelets offline su microcomputer italiano.
- **[[discipio-tisato1993]]** — ICMS mainframe IBM 9121, ancora deferred ma su sistema più maturo + programma DSL ante litteram (p. 165 *step towards the abstract*); real-time NeXT annunciato come *«in the near future»* — non realizzato nel paper.

### Atto 2 — Il real-time diventa disponibile (1988–1995)

Il vincolo cade. Il real-time diventa **modo operativo praticabile** e si
afferma come norma; sistemi e autori riorganizzano il controllo attorno a
interazione e feedback immediato. (Il non-determinismo che vi si accompagna è
economia di mezzi, non dottrina compositiva — correzione maestro, cfr. bullet
Truax e [[incontro-maestro-2026-05-28]].)

- **[[truax1988]]** — *Real-Time Granular Synthesis with a Digital Signal Processor* (CMJ 1988): primo sistema granulare interamente RT documentato (DMX-1000 + PDP Micro 11). Quote pietra-angolare p. 19: *«The key is to abandon linear modes of compositional thinking, which result in deterministic output (e.g., score or sequencer driven), and to substitute process-oriented multitask strategies for real-time execution.»* Il «*abandon linear modes*» riguarda il **modo operativo** RT (processo multitask vs score pre-scritto). **Correzione (maestro, 2026-05-28, cfr. [[incontro-maestro-2026-05-28]]):** il passaggio all'event list non-deterministica è **economia di mezzi**, non teoria della composizione — Truax adotta l'approccio statistico perché centinaia di grani/sec non sono razionalizzabili in una event-list deterministica alla Music V/Csound, non per dottrina compositiva («non ne farei una tematica particolarmente impegnativa», righe 73–86). Il non-determinismo statistico (tendency mask) **convive** in Truax con regioni armoniche progettate (*Riverrun*, ~100/200/300 Hz): non abbandono del controllo macro-strutturale. Cfr. [[tendency-mask]].
- **[[lippe1993]]** — IRCAM ISPW + Max (CIM X 1993): punto di transizione CIM, granular sampling signal-driven (pitch/amplitude tracking del clarinetto pilota tendency masks). Stesso volume di Di Scipio/Tisato offline.
- **[[discipio1995]]** — KYMA/CAPYBARA + GSAMX/DMX-1000 su brani *Hybris* (1994) e *Essai du vide* (1993). Snodo CIM **dello stesso autore** dell'atto 1: Di Scipio 1991 deferred su IBM 286 → Di Scipio 1995 RT su DSP commerciale. Documenta sul piano CIM la transizione che [[discipio-tisato1993]] aveva annunciato.
- **[[detintis1995]]** — GRAINS su IRIS-MARS (CIM XI 1995), MIDI continuous controller. Polo opposto sull'asse data reduction vs data exposure: p. 221 *«the reduction of data is a fundamental goal for the effectiveness and the efficiency for the composer who can work with high level parameters»* — il RT MIDI richiede riduzione drastica dei parametri esposti.

### Atto 3 — Ritorno volontario al deferred (PGE 2026 + precursore filosofico CMR 1999)

Il deferred ritorna come **scelta**, non come ripiego. La motivazione sposta da vincolo hardware (atto 1) a postura compositiva: composizione che coincide con studio della tecnica, loop di feedback lungo come spazio necessario per abitare gli spazi compositivi della granulazione come forma e struttura.

- **[[risset1999]]** — *Composing in Real-time?* (CMR 18/3): **fonte filosofica diretta** del ritorno volontario, articolata 27 anni prima dell'implementazione PGE su laptop. Quote pietra-angolare p. 37: *«Composition is not — or should not be — a real-time process. [...] Non real-time operation is necessary to free oneself of the arrow of time and its tyranny, of the dictates of haste, instancy, habits, reflexes. Writing music implies prediction and elaboration.»* Cinque drawback strutturali del RT (complessità sonora limitata, flessibilità ridotta, impossibilità del *bookkeeping* compositivo, effimerità tecnologica, *music for tape* come tradizione viva di concerto e archivio) fondano in CMR la legittimità del deferred come configurazione operativa, non come ripiego. Risset compositore che pratica RT (*Duet for one pianist*, MIT 1989) mentre lo rifiuta filosoficamente — primo caso documentato di coabitazione esplicita RT-pratica + deferred-filosofia.
- **PGE 2026** — Atto 3 in forma tecnica: DSL YAML + IR Python + dual renderer Csound/NumPy + score_visualizer + cache + LSP. Realizzazione laptop del programma Risset 1999.

## Coesistenza RT + deferred — anti-pattern netti CIM

Né l'atto 2 estingue l'atto 1, né l'atto 3 abolisce l'atto 2. La tradizione CIM/CMR documenta esplicitamente compositori che operano contemporaneamente nei due regimi, con motivazioni differenziate:

- **[[discipio1994]]** — *kairós* (1991/92 IBM486 deferred) + *Zeitwerk* (1992 mainframe IBM3090 deferred) + *Essai du vide* (1993 GSAMX RT su DMX-1000 di Truax). Stessa epoca, stesso autore, stesso filone (*models of detailed sonic design*). Affinamento esplicito della tesi: la postura indeterministica **non è vincolata** al deferred — è vincolata al *ciclo di esplorazione iterativa*; PGE sceglie il deferred perché il loop lungo a *scala riflessiva* è lo spazio compositivo che abilita l'indagine parametrica, non come imposizione hardware.
- **[[silvestri2010]]** — *Studio Sonoro III* (CIM XVIII 2010, nota 10 p. 210): *«composizione interamente basata su algoritmi di wavetable multiplexing implementati sia per la sintesi in tempo reale che, per la parte per nastro, in tempo differito»*. Data-point CIM 2010 in cui la dicotomia RT/deferred non è scelta esclusiva ma repertorio tecnico interno alla stessa opera.
- **[[arcella-silvestri2012]]** — CIM XIX 2012: pipeline C++ → Csound score → audio, batch by design. «*Variants of the first approach would be required for realtime versions*» (p. 148). Il real-time è opzione non perseguita per scelta tecnica esplicita.
- **[[roads2012]]** — «*Detached from real-time constraints, ideas can be tested, edited, submixed, or deleted at will*» (p. 8). Formulazione canonica della postura differita dal principale protagonista della lineage real-time-virtuosica. Ammette il fallimento Creatovox: la virtuosità del momento non è il giudice, l'ascolto riflesso lo è.
- **[[markidisfernandez2016]]** — CIM XXI 2016: sistema presentato come real-time ma con «analisi, ordinamento del database, calcolo dei primi vicini» in tempo differito (p. 181). Riconoscimento CIM 2016 che parte sostanziale del workflow è offline anche in sistemi RT.
- **[[risset1999]]** — *Duet for one pianist* (RT, Disklavier + Max/Puckette, 1989) coesistente con la sezione *Composition and real-time* (pp. 36–37) anti-RT. Coabitazione **filosoficamente tematizzata**: il RT è *cosmetic rather than structural* (p. 37) nel workflow di Risset, mentre la composizione richiede il deferred.

Questa coesistenza disinnesca la lettura del deferred PGE come regressione: nella tradizione CIM/CMR i due regimi non sono in successione storica esclusiva ma in alternanza funzionale per obiettivo compositivo.

## Legittimazione teorica

Tre fonti convergono sulla legittimità del differito come *configurazione temporale dell'interazione*, non sua negazione:

1. **[[discipio1995]]** (p. 19): «*interactivity cannot simplistically mean immediate audible output*» — il rate del feedback determina la scala temporale dell'interazione, non la sua presenza. Cfr. [[interactivity-rate]].

2. **[[solomos2003-ent04-de-loperatoire]]** (p. 232): «*aujourd'hui, le compositeur ne se limite plus à planifier un processus pour le regarder marcher tout seul [...] il interagit à tout moment avec lui*». Chi sceglie il differito *oggi* lo sceglie come postura, non come vincolo.

3. **[[arcella-silvestri2012]]** (p. 148): «*Tools and technologies used to produce a musical work are not neutral but incorporate knowledge that influence the choices of the composer*». Lo strumento differito non è neutro — incorpora la postura del loop lungo.

## Cinque drawback Risset → razionali tecnici PGE

Risset 1999 articola in CMR cinque drawback strutturali del RT che PGE indirizza tecnicamente. Mapping diretto:

| Drawback CMR (Risset 1999) | Razionale PGE corrispondente |
|---|---|
| 1. Complessità sonora limitata in RT | Tempo differito assorbe il costo computazionale; layering arbitrario di Stream YAML |
| 2. Flessibilità ridotta vs software synthesis (parametri RT selezionati *ahead of time*) | DSL YAML espone l'intero dominio parametrico, controllo deterministico-stocastico esplicito |
| 3. Mastering impossibile in RT (p. 34: *«the significance of the control settings is often unknown or obscure, and one cannot always exert useful bookkeeping»*) | DSL YAML + Language Server + `score_visualizer` = esposizione totale + bookkeeping del processo compositivo |
| 4. Effimerità tecnologica (p. 35: *«the compositional structure should be explicited clearly in term of basic operations that should be made available in future devices»*) | Architettura textual + IR Python + renderer pluggable (Csound/NumPy/Reaper): la specifica sopravvive al renderer specifico |
| 5. *Music for tape* viva come tradizione di concerto e archivio | Workflow STEMS + export DAW: il rendering PGE è oggetto archiviabile e ri-componibile |

Drawback 3 e 4 sono quelli con mapping più stretto sui nuclei del paper
(notazione YAML e partitura; architettura testuale con renderer pluggable).

## Tavola sinottica

| Anno | Autore | Sistema | Modalità | Motivazione |
|------|--------|---------|----------|-------------|
| 1978 | Roads | AGS / MUSIC V | differito | vincolo hardware |
| 1985 | Roads (CIM VI) | Music II / MIT | differito | vincolo 64 KB |
| 1988 | Truax | DMX-1000 | **real-time** | primo RT documentato; statistica come economia di mezzi |
| 1991 | Di Scipio (CIM IX) | IBM 286 | differito | vincolo RAM |
| 1993 | Di Scipio/Tisato (CIM X) | ICMS IBM 9121 | differito | ultimo nodo offline |
| 1993 | Lippe (CIM X) | ISPW | **real-time** | stesso volume CIM |
| 1994 | Di Scipio | kairós + Essai du vide | **entrambi** | postura, non vincolo |
| 1995 | Di Scipio (CIM XI) | KYMA/CAPYBARA | **real-time** | transizione completata |
| 1999 | Risset (CMR) | Duet + tape works | **entrambi** | RT cosmetic, deferred strutturale |
| 2010 | Silvestri (CIM XVIII) | Csound + PD | **entrambi** | coesistenza nella stessa opera |
| 2012 | Arcella/Silvestri (CIM XIX) | C++ → Csound | differito | batch by design |
| 2012 | Roads | Pro Tools studio | differito | economy of selection |
| 2016 | Markidis/Fernández (CIM XXI) | RT + analysis offline | **entrambi** | offline dentro RT |
| 2026 | PGE | Python → Csound/NumPy | **differito** | ritorno volontario |

## Relazione con PGE

PGE è collocabile esplicitamente come **Atto 3** della narrazione:

- *Stesso modo operativo* dell'Atto 1 (offline, specifica → motore → audio), ma con **motivazione opposta**: postura compositiva consapevole, non vincolo hardware. Cfr. [[discipio1991]] nota in [[granulare-deterministico-cim]] §Relazione con PGE.
- *Risposta esplicita* alla teorizzazione RT dell'Atto 2 ([[truax1988]] p. 19 *abandon linear modes*): PGE non rifiuta tecnicamente il RT — sceglie il loop lungo come *rate di feedback* compositivamente adeguato all'indagine parametrica. Il YAML non è uno score deterministico nel senso che Truax abbandona: è un DSL di intenzioni parametriche tradotte nella IR (lo Stream dichiarativo, [[intermediate-representation]]) attraverso processi stocastici (tendency masks Truax stesso, [[tendency-mask]]).
- *Realizzazione tecnica* della posizione filosofica [[risset1999]] (Atto 3 filosofico CMR 1999) su laptop generalista 27 anni dopo, in un momento in cui il deferred è scelta polare opposta al RT egemonico.

L'asse di controllo (tendency masks statistiche grano-per-grano, cfr. [[tendency-mask]]) e l'asse del regime temporale (deferred) sono **ortogonali**: PGE eredita il primo da Truax 1988 (Atto 2) e il secondo da Roads 1978 / Di Scipio 1991 (Atto 1) rovesciandone la motivazione.

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
- [[detintis1995]] — data reduction vs data exposure
- [[silvestri2010]] — coesistenza RT/differito nella stessa opera
- [[arcella-silvestri2012]] — pipeline batch, strumenti non neutri
- [[markidisfernandez2016]] — offline dentro il real-time
- [[risset1999]] — fonte filosofica del ritorno volontario
- [[interactivity-rate]] — ridefinizione interattività come rate
- [[solomos2003-ent04-de-loperatoire]] — triangolarité, interaction permanente
- [[granulare-deterministico-cim]] — polo gemello (asse deterministico/stocastico)
- [[tendency-mask]] — asse di controllo ortogonale al regime temporale

## Citabilità nel paper CIM 2026

- **«tradizione» (sezione rimossa, confluita in `sec:conclusioni`)** (primaria, primo paragrafo): genealogia compressa.
  Cluster effettivamente citato dal paper: [[roads1978]] + [[roads1985]]
  (problema del controllo in differito) → [[discipio-tisato1993]] +
  [[lippe1993]] (lo snodo documentato nello stesso volume 1993) →
  [[sparano2018]] + [[roads2021]] (il real-time come norma). [[discipio1991]]
  entra per la famiglia di controllo, non per il vincolo hardware.
- **non citato nel paper** («implicazioni», sezione rimossa): obiezione+risposta. [[risset1999]]
  p. 37 come precedente filosofico; [[discipio1995]] p. 19 (interattività ≠
  uscita immediata); [[arcella-silvestri2012]] p. 148 (strumenti non neutri).
  Il resto del materiale di questa pagina (coesistenze, drawback estesi,
  economy of selection) è background di supporto, non da citare in blocco.

Non citare in `sec:architettura` — argomento di cornice,
non di dettaglio implementativo. Fonte di verità: [[mappa-citazioni-paper]].

## Domande aperte

- **Atto 2 ha un precursore filosofico CMR analogo a Risset 1999 per l'Atto 3?** Truax 1988 p. 19 (*abandon linear modes*) è formulazione tecnica del paradigma RT; manca un equivalente CMR di posizione filosofica esplicita pro-RT del 1980s. Verificare CMR vol. 1–3 (1984–1989) per testi programmatici IRCAM/CCRMA pro-RT.
- **Catena lineage Atto 3 oltre PGE?** Esistono altri sistemi 2020+ che esplicitano il ritorno volontario al deferred come scelta compositiva, non come ripiego didattico o vincolo? Da monitorare in survey CMJ/CIM post-2024.
- **Coesistenza RT+deferred nella stessa opera al di fuori dei casi censiti** ([[discipio1994]], [[silvestri2010]], [[risset1999]], [[markidisfernandez2016]])? Pattern strutturale ricorrente o eccezione documentata? Cfr. [[anatrini2024]] e [[pozzi2016]] come polo RT contemporaneo per scansioni successive.
- **Promozione [[granulare-deterministico-cim]] come polo gemello?** Entrambe le concept pages tagliano la tradizione CIM lungo un asse (deterministico vs stocastico / deferred vs RT). Verificare se in «tradizione» (sezione rimossa, confluita in `sec:conclusioni`) conviene presentarle come due dimensioni indipendenti dello spazio di posizionamento PGE (2×2: deterministico+offline, statistico+offline = PGE, deterministico+RT, statistico+RT).
