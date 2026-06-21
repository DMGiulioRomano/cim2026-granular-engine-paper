# [Qiu & Ichise, 2025] Declarative Music Composition with Event Graph Transformations

## Citazione CIM
Qiu, T. & Ichise, R. (2025). Declarative Music Composition with Event Graph Transformations. In *Proceedings of the 10th International Conference on Technologies for Music Notation and Representation (TENOR 2025)*, pp. 193–200. Beijing, China: Central Conservatory of Music.

## Argomento centrale
Propone una composizione musicale dichiarativa basata su un modello a grafo di eventi unificato, attraversato lungo tutta la compilazione dalla notazione di alto livello fino al rendering audio; le trasformazioni del grafo sono funzioni di prima classe, esplicite e ispezionabili.

## Gap o problema identificato
I linguaggi musicali si dividono fra sistemi di alto livello (notazione, poca programmabilità) e sistemi event-based di basso livello (programmabilità piena, ma incapaci di rappresentare la notazione come contesto dichiarativo). Manca un modello unico che tenga la rappresentazione dichiarativa *lungo* la compilazione.

## Rilevanza diretta per PGE
È il fratello più prossimo sull'asse linguaggio/DSL: stessa famiglia (dichiarativo + rappresentazione intermedia attraversata dalla compilazione, cfr. [[intermediate-representation]]). Contrasto preciso: la loro IR è un grafo di trasformazioni *general-purpose* notazione→audio; PGE è granulazione di materiale registrato, con IR dichiarativa e **materializzazione differita grano-per-grano**. Continuità sull'idea (rappresentazione dichiarativa leggibile e processabile), divergenza sull'oggetto (eventi notazionali vs grani da campione) e sul differimento.

## Collegamento alla tesi centrale
Serve la proposta 1 e il posizionamento di `sec:tradizione`: dà un parente contemporaneo e diretto alla coppia «dichiarativo + IR», utile per dire cosa PGE eredita e cosa fa di proprio (il differito e la posizione di lettura come parametro dominante).

## Sezioni del paper CIM 2026 dove citare
- `(intro)` (primaria): stato dell'arte sulle rappresentazioni dichiarative per comporre/descrivere il suono.
- `sec:tradizione` (secondaria): il precedente più vicino del binomio dichiarativo+IR, contro cui si dimensiona il contributo PGE.

## Quote chiave
- «Representing music in declarative languages allows accurate, human-readable representation, and the automated processing of musical data.» (p. 193)
- «a unified graph-based event model used throughout the compilation process, from high-level musical notations to low-level audio rendering.» (p. 193)

## Note
Cfr. [[intermediate-representation]] e [[micromontage]].
