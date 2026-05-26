# [Markidis, Fernández, 2016] Analisi e sintesi in tempo reale mediante riconoscimento timbrico

## Citazione CIM
Markidis, M. M., Fernández, J. M. (2016). Analisi e sintesi in tempo reale mediante riconoscimento timbrico. In *Atti del XXI CIM*, pp. 181–185. Cagliari: AIMI.

## Categoria e lunghezza
Comunicazione orale / system paper — 5 pagine — 8 riferimenti (Puckette 1996/1998, Brent 2009 x2, Schwarz et al. 2006 CataRT, Schnell et al. 2009 MuBu, Schnell et al. 2010 typo-morphological, Gossmann-Neupert 2014 NIME).

## Argomento centrale
Descrive **`path~`**, external open-source (GPLv3) per Pure Data che implementa un sistema di analisi e sintesi concatenativa corpus-based. Estrae descrittori audio (default: MFCC ad alto livello + spectral centroid + RMS amplitude → spazio timbrico 16-dim) da un corpus audio in tempo differito, costruisce un kd-tree e una lista di k-primi-vicini per ogni grano; in tempo reale analizza il segnale entrante, trova il grano del corpus più simile via ricerca euclidea nel kd-tree e sintetizza un treno di grani dai k-vicini.

## Sistema o strumento descritto
Nome: **`path~`** v1.5.0 alpha. Linguaggio: external Pure Data (C), testato su OS X e Linux con Pd Vanilla 0.46.6. Distribuzione: Deken (gestore externals Pd), GPLv3. Architettura ibrida: analisi e indicizzazione in tempo differito (thread worker dedicato), sintesi in tempo reale (thread principale Pd). Anno: 2016.

## Analogia con PGE

1. **Tassonomia esplicita CIM 2016 granular → concatenative**: il paper inquadra la sintesi concatenativa come ramo evolutivo della sintesi granulare in cui *«i grani sono legati fra loro solitamente da un'analisi precedentemente fatta su un file audio»* (p. 181). PGE non implementa concatenative: i grani sono indipendenti (canone Roads/Truax), generati per stream con controllo parametrico. `path~` documenta CIM 2016 la divergenza del ramo concatenative; PGE 2026 ne è esplicitamente fuori — posizionamento sez. 2 del paper PGE come ritorno al canone *grani indipendenti per stream*, non come adesione a concatenative.

2. **Precursore CIM dell'ibridazione RT/differito necessaria nel granulare-derivato**: il paper afferma esplicitamente *«Oltre all'analisi, altre operazioni sono eseguite in tempo differito, come l'ordinamento del database o il calcolo dei primi vicini, necessario per la parte di sintesi dell'algoritmo»* (p. 181). Riconoscimento CIM che parte sostanziale del workflow granulare-derivato è *necessariamente* offline anche in sistemi che si presentano come real-time. Anti-analogia con PGE: PGE estende il differito a *tutto* il pipeline come scelta compositiva (non come vincolo computazionale dell'analisi), invertendo la polarità — `path~` minimizza la quota differita per servire la performance, PGE massimizza la quota differita per servire il loop lungo specifica → ascolto → riscrittura.

3. **Markidis CIM thread (8 anni)**: primo paper CIM di Marco Matteo Markidis, autore poi di [[markidis2024]] (CIM XXIV, *Mediation Process in a Computer Music Interpretation*). Evoluzione autoriale documentabile: 2016 = tool builder (external Pd per concatenative analysis/synthesis); 2024 = metodologo della traduzione fra ambienti (libreria aeLib + framework *layer of mediation* a 4 strati). Continuità: in entrambi i paper la separazione fra rappresentazione e implementazione è centrale — 2016 nel separare descrittori (analisi) da grani sintetizzati (riproduzione), 2024 nel separare graphical DSP score dalla patch eseguibile. Da citare nel paper PGE solo se si fa riferimento a [[markidis2024]] per il pattern *separare specifica da implementazione*, come nota a piè di pagina sul lineage Markidis CIM. Probabilmente non citare direttamente.

4. **Multithreading offline-during-RT come pattern complementare al deferred-total PGE**: `path~` usa un thread worker dedicato per non bloccare il thread audio Pd durante l'analisi del corpus. PGE può permettersi un approccio single-thread senza vincoli di latenza audio: il rendering può occupare l'intera CPU per minuti senza che questo conti come *latenza* — riformulazione del trade-off RT/offline come scelta di cosa misurare (tempo wall-clock di rendering vs latenza fra trigger e suono).

## Posizionamento storico
**Ramo concatenative del granulare CIM**, primo nodo CIM dedicato a `path~`. Cluster CIM concatenative XXI 2016: coppia stesso volume con Pozzi (Boids su CataRT) — entrambi su corpus-based concatenative, due polarizzazioni *signal-driven* (Markidis/Fernández, descrittori → ricerca knn → grano sintetizzato) vs *agent-driven* (Pozzi, Boids esplorano spazio descrittori → trigger grani per vicinanza). Il filone concatenative CIM trova in `path~` l'opzione *embedded in singolo external Pd* — vs CataRT che richiede librerie esterne (FTM, Gabor, MnM, MuBu) in Max/MSP. Connessione internazionale: Fernández è IRCAM, dove CataRT e MuBu sono sviluppati — `path~` come implementazione Pd compatta del paradigma IRCAM-MuBu in ambiente open-source.

## Note stilistiche
5 pagine, 8 riferimenti, struttura standard 5-section: Abstract → Introduzione → Lavori collegati → Metodi → Risultati → Discussione e conclusioni. Density tecnica significativa: 3 formule numerate (Mel scale, MFCC discrete cosine transform, spectral centroid), 1 code listing (preset script DSL), 2 figure (diagramma pipeline RT/differito + estratto partitura *Dispersion de trajectoires* per applicazione musicale). Sezione *Risultati* divisa in *Latenza* (benchmark quantitativo) + *Applicazioni nella composizione contemporanea* (esempi musicali). Apertura accademica con narrativa storica (Xenakis + percorso sintesi granulare → concatenative). Modello stilistico utile per il paper PGE: la combinazione di **diagramma pipeline che separa visivamente RT da differito** + **code listing del DSL preset** + **benchmark latency/timing** corrisponde a tre artefatti che il paper PGE 2026 può adottare (diagramma sez. 3 con asse offline-only, code listing YAML sez. 3, benchmark cache hit-rate sez. 3 o sez. 6).

## Sezioni del paper CIM 2026 dove citare
- **Sez. 2** (Sintesi granulare: dal paradigma Gabor al controllo gerarchico): citazione obbligatoria nella delimitazione *PGE non è concatenative*. Posizionare nella mappa CIM contemporanea fra ramo concatenative (path~ 2016, Pozzi 2016, CataRT 2006) e ramo stocastico canonico (Truax 1988, Roads 1988). Quote p. 181 *«nella sintesi concatenativa i grani sono legati fra loro [...] da un'analisi precedentemente fatta»* utile per la delimitazione.
- **Sez. 3** (PGE: architettura per l'indagine parametrica): possibile rinvio per il pattern *diagramma pipeline che separa RT da differito* come modello CIM 2016 di rappresentazione architetturale.

Non citare in sez. 1, 4, 5, 6 (no rilevanza diretta per narrazione tre atti, partitura grafica, caso compositivo, conclusioni).

## Quote chiave

> «Storicamente la sintesi granulare compare tra le prime applicazioni di produzione e ricostruzione sonora. A differenza di altre tecniche di sintesi, ormai cristallizzate nel tempo, la sintesi granulare continua ad avere un percorso di sviluppo lasciando aperte discussioni su varie tecniche, in particolare la sintesi concatenativa ed i mosaici audio.» (p. 181)

> «La differenza principale tra queste tecniche e la sintesi granulare è che nella sintesi concatenativa i grani sono legati fra loro solitamente da un'analisi precedentemente fatta su un file audio. Questa relazione può essere basata su differenti metodi ed è solitamente guidata dall'analisi.» (p. 181)

> «Oltre all'analisi, altre operazioni sono eseguite in tempo differito, come l'ordinamento del database o il calcolo dei primi vicini, necessario per la parte di sintesi dell'algoritmo.» (p. 181)

> «path∼ supporta una strategia di multithreading. In questo modo, un thread worker esegue l'analisi in tempo differito mentre il thread principale di Pd continua la sua esecuzione. Con questa strategia, l'analisi in tempo differito può essere eseguita senza interrompere il flusso audio.» (p. 183)
