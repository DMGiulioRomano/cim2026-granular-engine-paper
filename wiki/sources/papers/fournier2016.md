# [Fournier-S'niehotta, Rigaux & Travers, 2016] Is There a Data Model in Music Notation?

## Citazione CIM
Fournier-S'niehotta, R., Rigaux, P. & Travers, N. (2016). Is There a Data Model in Music Notation? In *Proceedings of the Second International Conference on Technologies for Music Notation and Representation (TENOR 2016)*, pp. 85–91. Cambridge, UK: Anglia Ruskin University.

## Argomento centrale
Le partiture sono oggetti strutturati; gli autori propongono di estrarre dalle codifiche di notazione un modello dati con un'algebra di operazioni composabili, in corrispondenza diretta con l'algebra relazionale e i database. La rappresentazione diventa così *interrogabile*.

## Gap o problema identificato
Le codifiche correnti (MusicXML, MEI) sono pensate per rendering e scambio, non sono istanze di un modello dati chiaro: non si possono interrogare né manipolare algebricamente in forma chiusa. Manca lo strato su cui «operare» la specifica.

## Rilevanza diretta per PGE
È il precedente più vicino all'idea di **IR interrogabile** (cfr. [[intermediate-representation]]): rappresentazione dichiarativa su cui si eseguono operazioni in forma chiusa. Contrasto netto e utile: loro rendono interrogabile la *partitura* (l'output, una codifica esistente); PGE rende interrogabile la *specifica* dichiarativa prima della materializzazione dei grani. Stessa intuizione (rappresentazione come oggetto manipolabile), oggetto diverso (output vs specifica) e momento diverso (a valle vs a monte del rendering).

## Collegamento alla tesi centrale
Serve la proposta 1 (la specifica dichiarativa come oggetto di lavoro che si interroga e si spedisce) e lo strato IR di `sec:architettura`: dà alla «IR interrogabile» un parente esplicito nella letteratura della notazione.

## Sezioni del paper CIM 2026 dove citare
- `(intro)` (primaria): stato dell'arte sulle rappresentazioni dichiarative/interrogabili del materiale musicale.
- `sec:architettura` (secondaria): la IR come specifica su cui operare, con il distinguo a monte/a valle del rendering.

## Quote chiave
- «Current score encodings, however, are designed for rendering and exchange purposes, and cannot directly be exploited as instances of a clear data model supporting algebraic manipulations.» (p. 85)
- «direct correspondence with relational databases and the relational algebra [...] we obtain an algebraic structure [...] that lets us manipulate score material in order to produce new representations.» (p. 86)

## Note
Tre autori (terzo: Nicolas Travers) per l'indice del volume; la prima pagina del paper ne stampa due — citare tutti e tre. Chiave BibTeX `Fournier2016tenor`. Cfr. [[intermediate-representation]].
