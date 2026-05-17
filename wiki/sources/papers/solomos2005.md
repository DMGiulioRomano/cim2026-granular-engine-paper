# [Solomos, 2005] An Introduction to Horacio Vaggione's Musical-Theoretical Thought

## Citazione CIM
Solomos, M. (2005). An introduction to Horacio Vaggione's musical-theoretical thought. *Contemporary Music Review*, 24(4-5), 311–326. London: Routledge. HAL: hal-00770212.

## Argomento centrale
Solomos riorganizza in cinque assi sistematici (Interaction, Time, Morphology, Singularities, Object Networks) il pensiero musico-teorico di Vaggione disseminato nelle pubblicazioni 1980–2003. Il filo conduttore esplicito (p. 13): tutte le categorie vaggioniane sono *operative* — «*it is thought that determines both the operation and the object*» (Granger via Vaggione, in Solomos/Soulez/Vaggione 2003: 224). L'articolo è la summa interpretativa più autorevole disponibile in inglese del programma vaggioniano e funziona come *mappa concettuale* del corpus 1980–2005.

## Gap o problema identificato
Solomos avverte che il pensiero di Vaggione è *radicalmente non-lineare*, *work-in-progress*, e *locus d'intersezione* tra molte discipline (p. 2). Qualunque sistematizzazione è quindi *lineare solo in apparenza*: i cinque assi si rinviano l'uno all'altro (Object Networks rinvia a Interaction; Singularities a Morphology). Il gap che Solomos colma è la mancanza, prima del suo articolo, di una presentazione sintetica del programma vaggioniano in inglese — i testi originali sono dispersi in francese su riviste e atti di JIM/Académie Bourges.

## Rilevanza diretta per PGE
Solomos 2005 fornisce a PGE quattro materiali concettuali pronti all'uso, già selezionati e gerarchizzati:

1. **«Articulating Micro-Time»** (Vaggione 1996a, *CMJ* 20/1) — titolo che Solomos (p. 5) eleva a sintesi del progetto vaggioniano: non «inner life» del suono, ma *come comporre l'articolazione* del micro-tempo. Aggancio diretto per la tesi PGE del loop lungo come spazio dell'articolazione micro-strutturale; *score_visualizer* PGE come strumento di lettura di quest'articolazione.

2. **Soglia 50–100 ms / 10–20 grains/sec** (p. 6) — Solomos espone con precisione la formulazione operativa che Vaggione (1998b: 172) adotta: macro-tempo «encompasses all possible scales» sopra la soglia, micro-tempo sotto; «*with less than ten to twenty sounds per second, the ear perceives grains as entities; when there are more, them as belonging to a global texture*» (p. 6). Soglia empirica per scelte di density e fill_factor PGE.

3. **Non-linearità tra scale temporali, irreducibilità** (pp. 6–7) — Solomos nota che l'originalità di Vaggione rispetto a Xenakis (GENDYN: tutto dedotto da una waveform) e Grisey (*Vortex temporum*: stessa outline su più scale temporali) consiste nel *non* postulare il principio di trasposizione tra scale. «*A non-linearity exists between time levels, an irreducibility from one to another*» (p. 7). Conseguenza per PGE: ogni Stream è un mondo morfologico con scale proprie; il global form non si deduce dal grano né viceversa — la composizione attraversa le scale ma non le risolve in una.

4. **Footnote 5 (p. 13): Vaggione vs Roads sul micro-tempo** — Solomos prende posizione esplicita: «*In this the Vaggionian notion of "micro-time" differs for example from the developments of Roads concerning "micro-sounds" (cf. C. Roads, 2002): for the latter, micro-time scales are hypostasised*». Per Vaggione invece «*the time scales themselves are determined according to the "multi-scale" field that is postulated for each composition*» (Vaggione 1998b: 171–172). Snodo cruciale per il posizionamento PGE: la critica vaggioniana a Roads *Microsound* è esplicita e citabile; PGE eredita la postura vaggioniana — le scale del buffer, del grano, del cloud, dello stem non sono dimensioni ontologiche ma campi operativi che il compositore stabilisce con la specifica YAML.

5. **Operative > implementations of imported notions** (p. 12) — «*Vaggione's concepts are not implementations of imported notions. These concepts, Vaggione tells us are operative: "the concept of composing with networks of objects is above all operative, its main purpose being to allow working at several simultaneous time scales"*» (in O. Budón, 2000: 13). Il framework concettuale di PGE (Stream/Voice/Controller/Envelope/Strategy) è da posizionare come *operativo* — definito dai propri scopi compositivi, non come implementazione di categorie OOP prese a prestito.

## Collegamento alla tesi centrale
Solomos 2005 lega tre nodi della tesi PGE:

- **Loop lungo** ← «*generalized interaction* being *internal to the musical work*» (p. 3) + «*aujourd'hui le compositeur interagit à tout moment*» (via 2003 ent4, qui rievocato p. 13). L'interazione vaggioniana è permanente e interna; PGE la materializza in tempo differito come ciclo iterativo *specifica → ascolto → riscrittura*. Solomos chiarisce che *interaction* per Vaggione non significa real-time gestural ma articolazione écriture↔algorithme — *interaction* è il modo di operare, non la latenza.

- **DSL YAML / 3 contributi** ← «*direct actions [...] as being in constant interaction with algorithmic calculations*» (p. 3); il YAML PGE è il livello in cui *direct action* (valore scritto a mano, espressione matematica, override per-grain) coesiste con *algorithmic calculation* (envelope, gate, strategie stocastiche). Solomos riassume la formula 1996 di Vaggione («*a local action of écriture definitely has the possibility of being integrated into an algorithmic process*») citandola da Vaggione 1996c: 24 (p. 4), confermando la formulazione già nota da [[vaggione1996]] e [[solomos2003-ch04-vaggione-composition-moyens-informatiques]].

- **Partitura grafica** ← *morphological singularities*, *saliences*, *details* (pp. 9, p. 92 di Vaggione 2003a citato): «*morphological details, which can be brought out and projected here and there into other regions, in the interplay of the work's vectors*» (p. 9). L'asse Y posizione-buffer del *score_visualizer* PGE rende leggibili le saliencies del campione sorgente — *dove* nel buffer si concentra l'attenzione granulare; il compositore identifica la salience, la *progetta* in altre regioni (loop, dephase, voice offset), e verifica visivamente lo *interplay of vectors*.

## Sezioni del paper CIM 2026 dove citare

- **Sezione 1 (Introduzione)** — citare *Articulating Micro-Time* come keyword sintetica della postura compositiva del loop lungo applicata alla scrittura granulare; citare la triangolazione *direct action ↔ algorithmic calculation* come framework dell'écriture mediata da DSL.
- **Sezione 2 (Sintesi granulare)** — citare soglia 50–100 ms / 10–20 grains/sec (p. 6) e *pluralism beneath identity* (p. 5, da Vaggione 1998c) come giustificazione percettivo-compositiva della granulazione di campioni come metodo per *trovare pluralismo* sotto l'identità di un campione sorgente. Citare la posizione di Vaggione contro l'«inner life» del suono come spaziale (p. 5) — Vaggione preferisce parlare di *micro-time* perché è questione di *come comporre l'articolazione*, non di *immergersi*.
- **Sezione 3 (Architettura)** — citare la tripletta *figures / objects / networks* (pp. 10–11) come framework per Stream / Voice / Controller PGE; citare la definizione vaggioniana di *object* (funzioni, liste di parametri, script, suoni — p. 11, da Vaggione 1998b: 187) come legittimazione del file Stream YAML come *unité multiple*; citare il concetto di *operative* (p. 12) come argomento metodologico contro la lettura del framework PGE come applicazione di categorie OOP astratte.
- **Sezione 4 (Partitura grafica)** — citare *morphological singularities* / *saliences* / *details* (p. 9) come razionale del visualizer come strumento di lettura morfologica; citare l'opposizione *morphological approach ≠ parametric approach* (p. 8) e la complementarità ammessa da Vaggione (Budón 2000: 13) come argomento per la doppia natura del visualizer (legge parametri ma rivela morfologie).
- **Sezione 5 (Caso compositivo)** — citare *écriture-processing* come *prism technique* (p. 10): «*compositions consist in making singularities productive through the construction of three-tiered musical edifices*» (p. 11). Costruzione del brano PGE come *progressive enrichment* di una salience del campione sorgente attraverso operazioni di loop/dephase/voice come *prism*.
- **Sezione 6 (Conclusioni)** — citare footnote 5 (p. 13) come *snodo storico-teorico* del posizionamento PGE: la critica esplicita di Solomos/Vaggione a Roads *Microsound* sull'ipostatizzazione delle scale temporali — PGE eredita la postura *operativa* multi-scala di Vaggione (scale come campo che il compositore postula per ogni composizione), non l'ontologia stratificata di Roads.

## Quote chiave

> «*The emergence of an approach articulated around the idea of generalized interaction (being internal to the musical work) allows us to consider at the same time the existence of many possible doorways between previously unrelated time-dimensions and the nature of the non-linearities arising from their interaction*» (Vaggione 1995: 100, *nota bene*, citato p. 3)

> «*Descending into micro-time is for a musician, the means of discovering phenomena he is unaware of when he satisfies himself with the agitation of sound surfaces without taking into account their substrates. […] We have to "find the pluralism beneath identity"*» (Vaggione 1998c, citato p. 5)

> «*With less than ten to twenty sounds per second, the ear perceives grains as entities; when there are more, them as belonging to a global texture*» (p. 6)

> «*For Vaggione, non-linearities between time scales not only exist, but can also be productive to musicians: "To recognise the reality of [the] mismatches [between the different time levels] does not drive us to paralysis; on the contrary, it gives us the possibility to explore the passages between different dimensions, allowing us to articulate them inside a syntactic network covering the whole spectrum of composable relationships"*» (in O. Budón 2000: 15, citato p. 7)

> «*Objects can be "functions (algorithms), lists of parameters (scores), scripts (chains of actions to be undertaken) or sounds (products as well as sources)"*» (Vaggione 1998b: 187, citato p. 11)

> «*The "operative" thought should not be confused with pure "instrumentalism": "it is thought that determines both the operation and the object"*, Vaggione writes, referring to Granger (in M. Solomos, A. Soulez, H. Vaggione, 2003: 224)» (p. 13)

> «*In this the Vaggionian notion of "micro-time" differs for example from the developments of Roads concerning "micro-sounds" (cf. C. Roads, 2002): for the latter, micro-time scales are hypostasised*» (footnote 5, p. 13)

## Note stilistiche

Articolo di sintesi interpretativa: 16 pagine, struttura esplicitamente non-lineare ma cinque sezioni canoniche; densità citazionale altissima (decine di rinvii a Vaggione 1980–2005, più Adorno, Thom, Prigogine, Lévy-Leblond, Bachelard, Serres); tono argomentativo ma deferente — Solomos è coautore della monografia 2003 con Vaggione, posizione non neutrale. La traduzione inglese (Rose/Grice) sostituisce «*écriture*» con «*direct action*» / «*intervention*» / «*writing*» a seconda del contesto — utile come glossario per il paper CIM se scritto in italiano (mantenere «*écriture*» come tecnicismo vaggioniano).

## Relazione con ingest precedenti

Solomos 2005 *non duplica* [[solomos2003]] né [[vaggione1991]]/[[vaggione1996]]/[[vaggione2002]]: è la *cartografia interpretativa esterna* (Solomos solo) del corpus vaggioniano, mentre il libro 2003 era *dialogico interno*. Funzioni complementari:

- **2003** = quadro maturo *interno* (Vaggione si esprime in prima persona, Solomos/Soulez sono interlocutori filosofici).
- **2005** = sistematizzazione *esterna* (Solomos legge Vaggione, propone 5 assi, prende posizione su Roads).

Per il paper CIM, **2005** è più utile in sede di citazione sintetica (un'unica fonte secondaria autorevole sintetizza il programma vaggioniano), mentre **2003** è la fonte primaria per quote testuali estese.
