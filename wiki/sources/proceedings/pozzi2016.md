# [Pozzi, 2016] Composing Exploration: A Multi-Agent Approach to Corpus-Based Concatenative Synthesis

## Citazione CIM
Pozzi, D. (2016). Composing Exploration: A Multi-Agent Approach to Corpus-Based Concatenative Synthesis. In *Atti del XXI Colloquio di Informatica Musicale*, pp. 190–196. Cagliari: AIMI.

## Categoria e lunghezza
Comunicazione orale (system paper sperimentale) — 7 pagine — 18 riferimenti.
Autore unico, IEM Graz (Institut für Elektronische Musik und Akustik), Kunstuniversität Graz.

## Argomento centrale
Sistema agent-based per corpus-based concatenative synthesis (CBCS) implementato in SuperCollider: un gruppo di agenti software (boids di Reynolds) esplora autonomamente uno spazio bidimensionale di descrittori popolato da unità sonore, e ciascun agente controlla in real-time i parametri di un proprio granulatore. L'obiettivo dichiarato è spostare il paradigma CBCS dal pattern *target-driven* (mouse cursor che punta una regione, come in CataRT) a un pattern *exploration-driven* in cui le morfologie sonore emergono come risultato primario del processo esplorativo.

## Sistema o strumento descritto
Nome: nessun nome di prodotto (sistema implementato come patch SuperCollider).
Ambiente: **SuperCollider** + tre librerie/quark — `SCMIR` (Nick Collins, music information retrieval), `KDTree` quark (Dan Stowell, nearest-neighbor search), `RedUniverse` quark (Fredrik Olofsson, modelli fisici di forze e attrattori).
Tecnica: Reynolds Boids (1987) — `separation` + `alignment` + `cohesion` con raggi percettivi distinti per task, estesi con goal-setting (attrattori) e boundary-setting. Ogni boid è accoppiato a un'istanza di granular SynthDef: la posizione del boid → grain selection (sample più vicino nello spazio descrittori via `nearest-neighbors` UGen); il numero di neighbors → amplitude; la distanza dal center-of-mass del flock → grain length; la velocity → playback rate del grano. Spatial swarm granulation (rif. Wilson 2008) testata in 24 canali al CUBE IEM.
Tempo: **real-time** (analisi/disposizione corpus offline preliminare, poi flocking + sintesi live).
Anno: 2016.

## Analogia con PGE
**Analogia diretta unica** (sez. 5 *Musical Contexts — Breakpoint*, pp. 193–194): l'autore descrive un'**iterative compositional strategy** per il brano *Breakpoint*: «*First of all, a number of samples is arranged by hand in a simple temporal structure. The resulting short collage is then analyzed and explored through the system. The audio outcome is recorded, edited and musically inserted in the previous collage of samples. The so obtained track is again analyzed and explored, and so on, in a cyclic procedure.*» Formulazione CIM 2016 esplicita del **loop lungo** (specifica → generazione → ascolto → riflessione → riscrittura) realizzata su tecnologia opposta a PGE: real-time emergent multi-agent invece di deferred declarative DSL. Stesso pattern strutturale (rifeed dell'output nella specifica), meccanismi tecnici ortogonali. Riferimento utile come precedente CIM esplicito della metodologia del loop per la sez. 1 e sez. 5 del paper PGE.

**Anti-analogie strutturali principali** (asse controllo e asse esplorazione parametrica):

| Asse | Pozzi 2016 | PGE |
|------|------------|-----|
| Controllo | emergent multi-agent (sum interazioni locali) | declarative deterministic (YAML + IR) |
| Predicibilità | unpredictability esplicitamente accettata (p. 193: «*renounce to a certain degree of control over the creative process*») | controllo granulare declarativo come parte della scrittura |
| Esplorazione spazio parametrico | Boids in spazio descrittori 2D (input gestuale del compositore via knob panel) | partitura grafica `score_visualizer` (output diagnostico post-rendering, asse Y = posizione nel buffer) |
| Spazializzazione | spatial swarm granulation 24-canali come side-effect emergente del flocking | `VoiceManager` pan strategies declarative |
| Selezione grano | kNN su feature space (CataRT-like) | indice campione esposto direttamente dal DSL |

**Anti-analogia simmetrica con [[anatrini2024]]** (esplorazione parametrica via tecnologie incomparabili): Pozzi 2016 (Boids real-time SuperCollider) ↔ Anatrini 2024 (VAE deep learning real-time Python+JS) ↔ PGE (declarative deferred). Tutti e tre convergono sull'obiettivo enunciato da [[anatrini2024]] p. 130 («*superare la tradizionale separazione tra programmazione parametri e attività compositiva*»), via tre tecnologie radicalmente diverse.

## Posizionamento storico
**Filone**: corpus-based concatenative synthesis (CBCS) — ramo della granulazione in cui «*i grani sono legati fra loro solitamente da un'analisi precedentemente fatta su un file audio*» ([[markidisfernandez2016]] p. 181). PGE è esplicitamente *fuori* da questo ramo (grani indipendenti per stream, canone Roads/Truax).

**Sotto-filone**: swarm music / multi-agent systems applicati alla composizione (Blackwell-Young *Swarm Granulator* 2004 ref [11], ChocK di T. O'Brien, ISO/ISS allo ZHdK Zurigo ref [16]). Pozzi 2016 è il primo data-point CIM di questo filone.

**Cluster CIM 2016 (coppia stesso volume)**: con [[markidisfernandez2016]] forma il doppietto CIM XXI 2016 *corpus-based concatenative*:
- [[markidisfernandez2016]]: `path~` per Pure Data, kNN deterministico **target-driven** (estrazione descrittori input → primo vicino → grano)
- Pozzi 2016: SuperCollider Boids, multi-agent **exploration-driven** (agenti autonomi cercano regioni dello spazio descrittori)
Polarizzazione interna al doppietto sull'asse target-driven vs exploration-driven della CBCS.

**Lineage Di Scipio CIM esteso**: Pozzi cita Di Scipio 1994 ICMC [#8] *Formal Processes of Timbre Composition* per giustificare la formulazione «*formation of both timbre and form in a natural dynamic process*» (sez. 6, p. 195). Quarto data-point CIM 2016 di adozione del vocabolario Di Scipio dopo [[lippe1993]] (acknowledgements), [[detintis1995]] (lessico granulazione complessa), [[arcella-silvestri2012]] (allievo + ricostruzione storica). Pozzi formato a IEM Graz ma allineato esplicitamente col lessico Di Scipio del *micro-composition paradigm*.

**Lineage swarm computer music CIM**: Pozzi 2016 apre un nuovo filone CIM (swarm music) non documentato in volumi precedenti; nessun nodo CIM successivo nel survey si aggancia direttamente. Continuità autoriale: Pozzi continua il lavoro a IEM con i brani *In Vitro* (installazione) e *Cocktail Break* (live performance con Rear Diffused Illumination + piezo transducers).

## Note stilistiche
**Struttura**: 7 sezioni numerate — 1 *Introduction*, 2 *The Agent* (2.1 algorithm + 2.2 swarms and music = related work integrato), 3 *Technical Outline* (3.1–3.4: analysis, flocking, relationships, spatial distribution), 4 *Composing Exploration* (4.1 texture design + 4.2 controls), 5 *Musical Contexts* (5.1 *Cocktail Break*), 6 *Considerations*, 7 *References*. Niente abstract/conclusion separati: sez. 1 fa da abstract esteso, sez. 6 da conclusion.

**Densità citazioni**: 18 ref / 7 pp ≈ 2.6 ref/pp — medio-alta per tool paper CIM (cfr. Anatrini 2024 25/7 ≈ 3.6, Sparano 2018 7/3 ≈ 2.3, De Tintis 1995 11/5 ≈ 2.2). Mix: literature swarm music (refs 10–15 Blackwell et al.) + CBCS canonica (refs 1–2 Schwarz CataRT) + ICST Zurigo (ref 16 ISO/ISS) + canone granulare PGE-condiviso (Roads *Microsound* [7], Di Scipio 1994 [8]).

**Uso figure**: 6 figure — Fig. 1 (boids/canvas), Fig. 2 (analisi *Pairs* Wolff), Fig. 3 (control panel), Fig. 4 (50s spectral contraction — 3 stati + spettrogramma), Fig. 5 (interfaccia fisica), Fig. 6 (schematics *Cocktail Break*). Alto rapporto figure/pagine; tutte sostengono argomenti specifici (Fig. 2 mostra le regioni A/B emergenti dall'analisi citate nel testo).

**Tono**: descrittivo + dimostrativo (riferimento a brani specifici come prova del comportamento del sistema). Argomentatività moderata: la sez. 6 *Considerations* difende l'approccio multi-agent come «*reasonable and pliable choice*» ma senza polemica esplicita verso il pattern CataRT target-driven. **Code snippet SuperCollider esplicito** (sez. 3.3, p. 192): pattern raro per CIM, utile come precedente di leggibilità per la sez. 3 del paper PGE.

**Apertura**: sez. 1 contestualizza CBCS contemporanea (CataRT come «*most diffused example*»), identifica il limite (mouse cursor target-driven) e annuncia l'approccio alternativo in 4 frasi. Modello stilistico pulito per l'introduzione del paper PGE.

**Chiusura**: sez. 6 sintetizza la differenza di postura («*sound cataloguing... rather used as ground for building a dynamic system with emergent properties*») senza riepilogare i contenuti tecnici. Modello CIM di chiusura argomentativa pura.

## Quote chiave

> «*The system described in this article seeks for a different approach to content-based environments, aiming to create specific conditions that enable sound morphologies to emerge as primary and main element of the interactive explorative synthesis process.*» (sez. 1, p. 190)
— framing exploration-driven vs target-driven.

> «*The audio outcome is recorded, edited and musically inserted in the previous collage of samples. The so obtained track is again analyzed and explored, and so on, in a cyclic procedure.*» (sez. 5 *Breakpoint*, p. 194)
— **quote pietra-angolare** per il loop lungo: formulazione CIM 2016 esplicita della metodologia ciclica rifeed → analisi → riesplorazione.

> «*The most obvious [aesthetic implication] is the renounce to a certain degree of control over the creative process [...] the resulting complexity of such a system, whose behavior is defined by the sum of a high number of small interactions among its single elements, inevitably introduces a certain unpredictability and pronounced emergent properties.*» (sez. 4, p. 193)
— polo opposto della postura PGE (control declarativo come parte della scrittura).

> «*Sound cataloguing is commonly employed to enhance the composer's control over materials, from this perspective it is rather used as ground for building a dynamic system with emergent properties, capable of producing unexpected and surprising results. Through this approach, the materials themselves are enhanced, leading to the formation of both timbre and form in a natural dynamic process.*» (sez. 6, p. 195)
— cita Di Scipio 1994 [#8] implicitamente nel passaggio *formation of both timbre and form*.

## Sezioni del paper CIM 2026 dove citare

Fonte non citata nel paper attuale; cfr. [[mappa-citazioni-paper]].

## Domande aperte
- Esiste documentazione successiva (post-2016) del sistema Pozzi? Il brano *Cocktail Break* è stato finalizzato? Se sì, verificare lineage CIM successivo
- L'iterative compositional strategy di *Breakpoint* (sez. 5) ha continuità nella letteratura swarm CIM/ICMC successiva, o resta un'occorrenza isolata? Cercare in atti CIM XXII (2018) e XXIII (2022)
- Se nuovo concept page `loop-lungo-cim.md` viene creato in sessione separata: Pozzi *Breakpoint* + Vaggione *progressive enrichment* (Roads 2005 p. 302) + Roads *economy of selection* (Roads 2012 pp. 28–29) + Di Scipio osservazione→modifica (Di Scipio 1994) formano il quadrilatero CIM-CMR del loop iterativo
