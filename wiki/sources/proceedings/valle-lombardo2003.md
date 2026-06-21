# [Valle & Lombardo, 2003] A Two-Level Method to Control Granular Synthesis (GeoGraphy)

## Citazione CIM
Valle, A., & Lombardo, V. (2003). A Two-Level Method to Control Granular Synthesis. In *Atti del XIV Colloquio di Informatica Musicale (XIV CIM 2003)*, pp. 136–140. Firenze: AIMI, 8–10 maggio 2003. (Affiliation autori: MultiLab e Dipartimento di Informatica, Università di Torino.)

Nota di identificazione: il survey [[cim-survey]] e il piano `docs/plans/setup-workspace.md` riportavano titolo *"A Two-Level System for Grain Generation and Control Structure"* con *autore non identificato dall'OCR*. La title page (PDF p. 145 del volume, printed p. 136) chiarisce: titolo *A Two-Level Method to Control Granular Synthesis*; autori Andrea Valle, Vincenzo Lombardo. *"GEOGRAPHY: A TWO-LEVEL SYSTEM FOR GRAIN GENERATION AND CONTROL STRUCTURE"* è il titolo della sezione 2, non del paper.

## Categoria e lunghezza
Comunicazione scientifica — 5 pagine (pp. 136–140) — 25 riferimenti bibliografici (sezione *3. References* sulle pp. 139–140).

## Argomento centrale
Sistema formale **GeoGraphy** per il controllo algoritmico della sintesi granulare via due livelli: (I) **grain generator** basato su grafi diretti (vertice = grano; arco = relazione temporale di sequenziamento con label = onset delay); (II) **map-based controller** dove i grafi sono posizionati in uno spazio euclideo e i parametri sono controllati navigando lo spazio con uno *space actant* lungo una *trajectory*. Tesi: il sistema generalizza sia l'approccio *note* sia quello *stochastic* alla granular synthesis (Xenakis, Roads, Truax).

## Sistema o strumento descritto
**GeoGraphy** (MultiLab + Dipartimento di Informatica, Università di Torino). Linguaggio non specificato nel paper; richiamo a [16] (Valle/Lombardo, dettagli formali). Architettura:
- *grain* = waveform con durata fissa o sintetizzata
- *graph actant* (token, analogo a Petri net) naviga grafo dirigendo sequenza grani
- *space actant* = device di scansione che a rate costante percorre trajectory in mappa euclidea; distanza dal vertice attivo = parametro di controllo (panning, ampiezza, filtro bandpass)
- Brown motion citato come strategia di trajectory algoritmica.
- Citato come **out-of-time, generative** formalism. Nessun riferimento al real-time.

## Analogia con PGE

GeoGraphy è uno dei sistemi CIM **architettonicamente più organizzati** prima di PGE, ma i vettori di analogia vanno calibrati con cura: il fatto che entrambi siano "sistemi formali a due livelli con grani come unità minima" non implica che le loro componenti siano in corrispondenza biunivoca. Quattro vettori a forza decrescente, più una anti-analogia chiarificatrice.

1. **Separazione strutturale specifica ↔ rendering** (livello I generator vs livello II controller). Analogia **di principio**, non di meccanismo. GeoGraphy separa due *strutture parallele* progettate dal compositore (grafo + mappa); PGE separa una *pipeline sequenziale* (`ParameterOrchestrator` parser YAML → `Stream`/`Controller`/`VoiceManager` rendering). In entrambi i casi la specifica di *cosa* emettere è separata dalla specifica di *come* modularlo, ma in PGE il "controller" non è uno strumento navigabile dal compositore — è il risultato dell'istanziazione di `Parameter` con `Envelope` da YAML. Vettore conservato come **scelta architetturale comune** (modularità delle responsabilità), non come corrispondenza struttura-a-struttura.

2. **Onset time come label di prima classe.** Quote (p. 137): *"A label on an edge represents the temporal distance between the onset times of the two grains connected by the edge itself."* — IOT esplicito come dato strutturale, non derivato da density. PGE realizza la stessa idea via `DensityController` (IOT ricavato da `density` o `fill_factor`) ma con interfaccia continua, non grafo discreto. Vettore solido: entrambi i sistemi trattano l'onset come parametro di prima classe, distinto dalla durata del grano.

3. **Track = sequenza polifonica di grain stream**. P. 137 Figura 1: *"a composition is a set of tracks; each track is a grain sequence"*. Ontologia identica al concetto di `Stream` PGE. Differenza nel meccanismo di generazione: GeoGraphy usa graph actants (token probabilistici su grafi, alla Petri net) che producono sequenze diverse a ogni esecuzione; PGE usa tendency mask (cfr. [[tendency-mask]]) con `dephase` per la variazione stocastica. Multiple tracks GeoGraphy ↔ multiple Stream PGE è una mappatura strutturalmente solida; multi-actant su uno stesso grafo ≠ multi-voce su uno stesso Stream (PGE: voci condividono il puntatore con offset; GeoGraphy: actanti percorrono il grafo in modo indipendente).

4. **Generalizzazione esplicita di note + stochastic approach**. P. 139: *"the time/frequency domain, and hence the stochastic approaches, can be considered a special case of the map space"*. Vettore **argomentativo**, non strutturale: entrambi i sistemi formali si presentano come livello di astrazione che ingloba sia l'approccio *note-per-note* sia quello *stocastico* (Roads/Xenakis/Truax). Meccanismi diversi (GeoGraphy via spazio metrico + scanning device; PGE via DSL dichiarativo + tendency mask + envelope time-varying), ma la **postura argomentativa** del paper PGE può essere posta in continuità CIM citando Valle/Lombardo come precedente.

---

**Anti-analogia chiarificatrice: space actant ≠ score_visualizer.**

Lo *space actant* di GeoGraphy è un **input di controllo compositivo**: il compositore disegna una trajectory nello map space; lo space actant la percorre a rate costante; la sua distanza dai vertici modula i parametri dei grani associati (*"parameters value ranges are mapped onto spatial distance, and the nearer is a trajectory to some vertex, the higher is the value of some parameter for the grain waveform represented by that vertex"*, p. 137). Esempi di parametri controllati: pan, ampiezza, bandwidth del bandpass filter. Lo space actant è parte della **specifica** del brano, scritta dal compositore prima del rendering.

Il `score_visualizer` di PGE è una **partitura di test diagnostica**: PDF read-only generato *dopo* il rendering, che mostra la traccia effettiva dei grani prodotti dal YAML. Funzione esplicita: verificare che il YAML scritto produca il comportamento atteso (test di consistenza tra intenzione e output). Non controlla nulla, non è editabile, non fa parte del file di composizione.

I due oggetti sono **opposti per ruolo nel workflow compositivo**:

| | space actant (GeoGraphy) | score_visualizer (PGE) |
|---|---|---|
| Direzione del flusso | input → rendering | rendering → output |
| Ruolo nel loop | controllo compositivo (specifica) | diagnostica read-only (verifica) |
| Contenuto rappresentato | eventi *potenziali* (vertici) | eventi *attuali* (grani generati) |
| Editabilità | disegnato dal compositore | derivato dal YAML, non editabile |
| Funzione nel ciclo | specifica → suono | suono → verifica → riscrittura |

Condividere la rappresentazione 2D è coincidenza superficiale. L'avvertenza p. 139 (*"a map space should be used with caution in simulating a time/frequency space"*) non si trasferisce direttamente a PGE: Valle/Lombardo discutono il limite intrinseco del *loro* sistema (la mappa contiene eventi solo potenziali, separati dal grain generator), mentre il `score_visualizer` PGE non ha quel problema — disegna eventi attuali emessi dal renderer.

Il differenziatore PGE rispetto al filone Truax 1988 Fig. 4 (input gestural) / Valle-Lombardo 2003 (input compositivo) / Caires 2004 IRIN Timeline (input editabile) **non è la scelta di Y ≠ frequenza** — quella scelta è già nello stato dell'arte CIM. Il differenziatore è l'**inversione di flusso**: la partitura come output diagnostico di un loop lungo basato su specifica testuale.

## Posizionamento storico
Filone **formal/offline / controllo gerarchico parametrico**. Si colloca:
- Nel solco *note approach + stochastic approach* (Roads, Xenakis, Truax), che cita esplicitamente come approcci che il sistema generalizza.
- Cronologicamente vicino a **Roads, *Microsound* (2001)**, citato come [2]; Valle/Lombardo recepiscono la tassonomia roadsiana cumulus/stratus/glissandi (p. 137) e la usano come metafora descrittiva delle configurazioni di grafi.
- Precorre il framework Vaggione *object-based* recepito da PGE: i vertici come *objets sonores* (Schaeffer, *Traité des objets musicaux*, Seuil 1966 — ref [24] del paper, sez. References p. 140); il grafo come *"set of relations between vertices, which can be thought as objets sonores"* (p. 139). Linea concettuale comune con Vaggione 1991 / Solomos 2005, importata nella tradizione CIM.

**Continuità autoriale Valle CIM (11 anni) — primo nodo di una traiettoria.** Andrea Valle torna in ambito CIM granular-related undici anni dopo con [[valenti-valle-servetti2014]] (*Permutation Synthesis*, CIM XX 2014, plugin SuperCollider). Traiettoria 2003 → 2014: da **architettura sistema formale CAC offline** (GeoGraphy a due livelli con space actant, registro descrittivo-formale, 25 refs) a **tecnica DSP sperimentale real-time SC** (3 UGens, formule analitiche dominanti, 6 refs). Stesso autore CIM esplora due poli opposti del granulare-derivato: compositivo formale offline → DSP sperimentale real-time. Datapoint sulla varietà del granulare CIM italiano nella stessa autorialità.

## Note stilistiche
- **Struttura**: Abstract → 1. Composition with granular synthesis (storico-tassonomico) → 2. GEOGRAPHY: a two-level system (formale, con figure e parametri) → expressivity issues → 4. Conclusions → References. Pattern utilizzabile come modello per `sec:architettura`: brevissimo inquadramento storico → presentazione formale dei livelli architetturali con figure dedicate → discussione expressivity / generalizzazione → conclusioni.
- **Tono**: descrittivo-formale, con argomentazione che culmina in "sistema come generalizzazione di approcci esistenti". Registro accademico CIM tipico, asciutto. Niente epigrafi.
- **Densità citazioni**: 25 ref totali nella sezione *3. References* (pp. 139–140). Mix tematico: granular synthesis (De Poli/Piccialli/Roads 1991 [1], Roads 1985 [12], Roads 1988 [3], Roads 2001 *Microsound* [2], Roads 1996 [4], Xenakis *Formalized Music* [5], Wishart 1994 [6], Truax 1988 [10], Truax 1990 [7], Jones-Parks 1988 [8], Lee Csound 2000 [9], Roads 1991 [11], Giordani GSC4 1998 [13], Bartetzki CMask 2002 [14]) + teoria dei grafi (Diestel 2000 [15]) + auto-riferimento (Valle 2002 *Del Gran Paese* [16]) + percezione/timbro (Plomp 1976 [17], Wessel 1979 [18], Rasch-Plomp 1982 [19], Slawson 1985 [20], Risset-Wessel 1982 [21], Lerdahl 1991 [22], Shepard 1982 [23]) + objets sonores / cognizione (Schaeffer 1966 [24], Bel 1992 [25]). **Lezione**: 25 ref su 5 pagine = densità citazioni alta, mix tecnico/percettivo/filosofico — utile come modello per il paper CIM 2026.
- **Pattern figure**: ogni figura ha didascalia in box separato, riferita esplicitamente nel corpo per numero. Mix grafi simbolici + spettrogrammi + diagramma trajectory.
- **Apertura sezione 2**: introduce un oggetto formale con nome (GeoGraphy) e ne descrive subito i due livelli. Modello *agente formale* riusabile per descrivere `ParameterOrchestrator` e `Stream` PGE.

## Sezioni del paper CIM 2026 dove citare

- **candidata `sec:architettura`**: space actant come input di controllo —
  anti-analogia di flusso rispetto alla partitura PGE (output read-only).
  Non ancora citata nel paper.

Fonte di verità: [[mappa-citazioni-paper]]; dispensa: [[graphic-score]].

## Quote chiave
- *"The formal system GeoGraphy consists of two components: a graph-based generator of grain sequences (i.e. tracks), and a map-based controller of grain waveform parameters."* (p. 137) — formulazione canonica della separazione **generator ↔ controller**, ripresa direttamente nell'architettura PGE.
- *"A label on an edge represents the temporal distance between the onset times of the two grains connected by the edge itself."* (p. 137) — IOT come dato strutturale di prima classe, equivalente alla scelta PGE di esporre `density` e `fill_factor` come parametri DSL espliciti.
- *"a composition is a set of tracks; each track is a grain sequence […]. The grains are waveforms that result from granular synthesis and parametric control."* (p. 137) — ontologia track/grain identica a Stream/grano PGE.
- *"the time/frequency domain, and hence the stochastic approaches, can be considered a special case of the map space in which: a) one axis represents frequency; b) the other represents time; c) the trajectory coincides with the time axis […]. It must be noted that a map space should be used with caution in simulating a time/frequency space."* (p. 139) — argomento esplicito contro l'identificazione automatica della partitura granulare con il piano tempo/frequenza; legittima la scelta PGE di asse Y = posizione nel buffer.
- *"The advantages of the GeoGraphy model for the composer rely mostly upon the symbolic approach, in that each graph structure represents a set of relations between vertices, which can be thought as objets sonores. Sound objects as defined by Schaeffer are symbolic objects encoding sonic properties apt to be used in compositional practice."* (p. 139) — apertura schaefferiana/vaggioniana esplicita in ambito CIM; precedente per inquadrare PGE nella linea object-based.
