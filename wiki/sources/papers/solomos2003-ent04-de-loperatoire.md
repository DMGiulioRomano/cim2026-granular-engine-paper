# [Solomos/Soulez/Vaggione, 2003] Formel/Informel — Entretien 4: De l'opératoire

## Posizione nel libro
*De l'opératoire*. In *Formel/Informel: musique-philosophie*, pp. 221–235 (testo) + 235–236 (notes 1–11). L'Harmattan, Paris, 2003. Quarto dei cinque *entretiens* della *Seconde partie*. Interlocutori: Antonia Soulez (filosofa, AS), Makis Solomos (musicologo, MS), Horacio Vaggione (compositore, HV). L'entretien è il documento più chiaro nel libro sul concetto di *opératoire* — Vaggione lo articola dialogicamente in risposta a domande filosofiche (Granger, Goodman) e musicologiche (Risset, Xenakis, sérialisme).

## Argomento centrale
Definizione e difesa del concetto di *opératoire* come categoria che (a) precede ontologicamente la divisione strutturale/materiale, (b) si esercita su tutte le scale temporali (micro/macro), (c) richiede una *triangolarità interaction* input/output/opérateur, (d) si distingue da *musique de Turing* (algoritmo non-interattivo) e da *composition automatique* (sérialisme integrale, Hiller, Barbaud). L'entretien fornisce inoltre la storicizzazione tecnica: lo *opératoire* non era possibile nei linguaggi *structurés* anni 1960–70; diventa possibile con il paradigm shift verso la *programmation orientée-objet* (OOP, fine anni 1990) e con la disponibilità del *temps différé* maturo.

## Struttura dell'entretien

| Pagine | Topic |
|---|---|
| 221–223 (non ingestite in dettaglio: introduzione di AS via Granger, oggetto/operazione) | Granger come quadro filosofico di riferimento (Formes, opérations, objets, Vrin 1994) |
| 224 | HV: l'objet è prodotto dell'opération ma non ipostatizzato come tale; objet = catégorie opératoire (riprende ch. 4 del libro) |
| 225 | Object su tutte le scale temporali; soglia micro/macro empirica ~50 ms o 20 grani/sec da Xenakis-Poisson; soglia *mobile* ma non puramente convenzionale |
| 226–227 | Saisie inconsciente del micro-temps; «chorus effect» d'orchestra (Mannheim, Haydn) come decorrelation di fact; objet musical = objet sonore composto; auditeur che fa operazioni |
| 228–229 | Auditeur come fornitore di sue proprie *versions-monde* (Goodman); compositeur propone una «proposition d'écoute»; Risset come polo psicoacustico, Vaggione come polo operatorio |
| 229–232 | Critica della *musique de Turing* (sérialisme intégral, Hiller/Barbaud, Xenakis GENDYN); definizione dell'interaction come triangolarità input/output/opérateur (p. 230); la situazione attuale rende possibile *interaction permanente* (p. 232) |
| 232–233 | OOP come paradigm shift abilitante; «aujourd'hui, le compositeur ne se limite plus à planifier un processus pour le regarder marcher tout seul; il interagit à tout moment avec lui, pour produire du formel» |
| 233–235 | Formel = morphologique, non formalizzato; immanentismo (forma e materia non in relazione dialettica); position di Vaggione rispetto ad Adorno (de-dialettizzazione del *informel*) |

## Concetti chiave

### 1. Triangolarità interaction (p. 230)
> «AS – L'interaction est donc une relation à trois: entrée, sortie et opérateur.
> HV – Oui, c'est un puzzle triangulaire.»

Formula esplicita della struttura dell'interaction. Una *boîte noire* (Turing-machine, sérialisme integrale, GENDYN) ha solo input/output, niente operatore; le trasformazioni emergono dalla boîte stessa. L'interaction esige la *presenza costante* dell'opérateur che interagisce con il sistema.

**Conseguenza per il loop lungo PGE**: il loop lungo è la modalità temporale in cui l'opérateur mantiene il triangolo aperto in tempo differito. Non è regressione a una musica non-interattiva; è interaction differita, dove l'opérateur interviene tra un ciclo render e il successivo. Critica anticipata a chi confonde *deferred* con *non-interactif*: la separazione opérateur/processus rimane, è solo *asincrona*.

### 2. Soglia micro/macro empirica (p. 225)
> «pour situer le niveau du microtemps, on peut parler d'un ordre de grandeur toujours inférieur à 100 millièmes de seconde — en réalité, selon les cas (c'est-à-dire selon les morphologies), on trouve ce seuil entre micro et macrotemps à partir d'un ordre de grandeur de 50 millièmes de seconde. De manière alternative, on pourrait dire que ce seuil se trouve dans des distributions de sons dont la densité dépasse les 20 "grains" par seconde — on l'a vu à propos de la limite de distribution de la loi de Poisson, dans notre discussion sur Xenakis. Il y a donc également une partie empirique, non conventionnelle, qui nous fait percevoir un seuil ou un passage.»

Soglia *empirico-morfologica* (~50 ms o ~20 grains/sec), non convenzionale assoluta, ma neanche puramente arbitraria. Importante per la sezione 2 del paper CIM: la giustificazione dei tempi tipici della granular synthesis non è cieca eredità Gabor/Roads, ma confluence di indicazione percettiva (Gabor) + indicazione morphologique (Vaggione: «morphologies sonores», «structures dynamiques»). PGE eredita questo intervallo come *default range* delle envelope di grain duration.

### 3. Critica della musique de Turing (p. 230)
> «Dans une "musique de Turing" [...] on met quelques données et l'on obtient un résultat, mais sans avoir la moindre interaction dans le chemin entre l'entrée et la sortie. Dans cette situation, il n'y a pas d'opérateur. Et on ne peut pas parler d'opérations s'il n'y a pas d'opérateur.»

Generalizzazione filosofica del concetto: l'operazione richiede l'operatore. Senza operatore c'è solo *calcul* (computation, transition stato → stato). Conseguenza diretta per il design di PGE: il sistema deve preservare *spazi di intervento* dell'operatore in ogni fase della pipeline. Il YAML è esattamente questo spazio: il compositore intervene sul livello *opératoire* (le regole, le strategie, gli envelope), non sul livello *output* (i grani prodotti).

### 4. Aujourd'hui: interaction permanente possibile (p. 232)
> «Aujourd'hui, nous sommes dans une situation où le compositeur ne se limite plus à planifier un processus pour le regarder marcher tout seul, en attendant qu'il lui donne quelque chose: il interagit à tout moment avec lui, pour produire du formel. [...] On peut dire donc qu'il produit ainsi des singularités.»

Tesi storica chiave: l'*interaction permanente* è ora *possibile* (non era prima). Conseguenza implicita: chi sceglie il tempo differito *oggi* lo sceglie come postura compositiva, non come vincolo tecnico. Sostegno argomentativo *diretto* della tesi centrale del paper CIM («PGE è un ritorno *volontario* al tempo differito in un momento in cui il real-time è disponibile»).

### 5. OOP come paradigm shift abilitante (pp. 232–233)
> «l'approche opératoire telle que nous l'avons définie n'était pas possible avec les langages informatiques dits "structurés" des années 1960–1970. Au début de l'informatique, on l'a vu à propos de Xenakis, l'interaction était très faible. On avait toujours affaire à des boîtes noires, qu'elles soient aléatoires ou déterministes. L'idée même d'objet, en tant que catégorie opératoire, ne pouvait pas se poser. Par contre, maintenant qu'elle est posée, en partie grâce à un glissement de paradigme dans l'informatique (allant du "structuré" à ce qu'on appelle "programmation orientée-objet") il serait dommage [...] de se passer des possibilités qu'offrent les moyens numériques afin de composer le matériau.»

Tesi storica forte: la *catégorie opératoire* di Vaggione è abilitata storicamente dal paradigma OOP. Conseguenza per PGE: l'architettura OOP di PGE (Controller, VoiceManager, Strategy, GateFactory, Renderer) non è scelta arbitraria ma *condizione di possibilità* dell'approccio opératoire. Argomento storico-tecnico per giustificare l'uso di Python OOP in un dominio (sintesi granulare) tradizionalmente dominato da approcci procedural (Csound score) o stream-based (SuperCollider).

### 6. Formel = morphologique, non formalizzato (p. 234)
> «AS – Qu'est-ce que le formel, de ton point de vue?
> HV – Ce n'est pas le formalisé (dans le sens d'un calcul), mais le morphologique; le formel n'est pas extérieur à la matière. L'opératoire instaure des contenus morphologiques, qui sont aussi des contenus sensibles. Le formel dénote, à mon sens, ce caractère "interne" des morphologies qui est irréductible à la notion classique — dualiste — de Forme.»

Distinzione tecnica fondamentale: *formel* (in senso vaggioniano) ≠ *formalisé*. Il *formel* è la dimensione morphologique interna dei contenuti, non un'operazione di calcul applicata dall'esterno. Conseguenza per la lettura della partitura grafica PGE: la partitura non è formalizzazione astratta (codifica simbolica esterna del processo), è *visualizzazione delle morphologies*. Il *formel* prodotto dal loop lungo è la coerenza morphologique riconosciuta nell'ascolto, non la pulizia formale del YAML.

### 7. Proposition d'écoute (pp. 227–228)
> «MS – Tu absorbes l'audition dans tes opérations?
> HV – Si la question est dirigée vers moi-même, en tant que compositeur, certainement mes opérations sont, comme je l'ai dit, des perceptions, et cela de façon non dualiste: tout objet sonore est pour moi un objet musical, parce qu'il se situe dans le domaine du composable. Si la question implique l'auditeur, je dirais que je ne l'oblige pas, mais que je lui fournis une quantité de choses avec lesquelles il peut réaliser ses propres opérations musicales.
> [...]
> HV – Je pense que tous les compositeurs font de même. Je ne connais pas de musicien qui ne fasse pas, d'une manière ou d'une autre, une "proposition d'écoute". Chaque artiste propose une "version-monde", comme dirait Goodman, une manière de percevoir les choses qui est en fait une opération de production de sens.»

Concetto di *proposition d'écoute* / *version-monde*: il compositore non determina l'ascolto dell'auditeur, gli propone uno spazio di operazioni d'ascolto. Goodman è il riferimento filosofico (*Ways of Worldmaking*). Conseguenza per il design della partitura grafica PGE: la partitura è una *proposition d'écoute* visualizzata, non una scrittura prescrittiva. Il compositore la rilegge come *first listener* del proprio brano e ne deriva decisioni di riscrittura.

### 8. Immanentismo (p. 234)
> «AS – Forme et matière, pour Horacio, ne sont pas en relation dialectique. [...] *ce que* tu composes ne se distingue pas de *ce avec quoi* tu composes: le son est à la fois matériau et moyen de former le matériau en produisant des contenus formels, synthèses d'objet, comme dirait Cavaillès. On est donc dans le cadre de l'immanence: ta conception de l'opération est immanentiste.
> HV – Oui, je suis tout à fait d'accord: c'est en effet une conception immanentiste.»

Posizione esplicita: non c'è dualismo materia/forma. Conseguenza per PGE: il YAML *non rappresenta* una forma esterna che il render *imprime* sul materiale; il YAML *è* il materiale composto, nelle sue articolazioni *operatorie*. Distinzione che il paper può usare per argomentare *contro* la lettura del DSL come «codifica simbolica di intenzioni»: il DSL è la modalità con cui le intenzioni *sono già* operazioni sul materiale.

## Rilevanza diretta per PGE

1. **Triangolarità interaction → loop lungo come configurazione opératoire deferred**. Il loop lungo PGE non è regressione pre-real-time ma *modalità asincrona* dell'interaction. Sostegno argomentativo diretto per la sezione 1 del paper (narrazione tre atti: il *ritorno volontario* al tempo differito è ritorno a una configurazione *operatoria specifica*, non abbandono dell'interaction).

2. **OOP come condition de possibilité storico-tecnica**. L'architettura object-oriented di PGE è *condizione abilitante* dell'approccio opératoire vaggioniano. Sostegno argomentativo per la sezione 3 (architettura): la scelta di Python OOP (Controller, Strategy, VoiceManager, Renderer) non è ingegneristica neutra ma *coerente con la postura compositiva*.

3. **Critica della musique de Turing → critica dei sistemi non-interattivi**. PGE *non è* un Turing-music system: nonostante il render sia non-interattivo nel tempo (batch), l'opérateur interviene fra cicli sul livello *opératoire* (il YAML). Distinzione chiave per il paper: differido ≠ Turing.

4. **Soglia micro/macro empirica come riferimento per i default PGE**. Density range, grain duration range, envelope behavior — i default PGE (cfr. `DensityController` e `StreamConfig`) si situano nello stesso intervallo empirico (~50 ms, ~20 grains/sec) identificato da Vaggione come soglia morfologica. Riferimento argomentativo per giustificare le scelte di range.

5. **Proposition d'écoute → score_visualizer come visualizzazione operatoria, non prescrittiva**. La partitura grafica PGE non *prescrive* l'ascolto ma *propone uno spazio di operazioni d'ascolto* (Goodman/Vaggione). Il compositore la legge come *first listener*: questo è il loop lungo (specifica → render → visualizer → riascolto → editing). Argomento per sezione 4.

6. **Immanentismo → YAML è materiale composto, non codifica di forma esterna**. Argomento filosofico per resistere alla lettura del DSL YAML come *notazione simbolica*. Il YAML è *modalità operatoria* dello stesso materiale che il render produce — non una descrizione esterna del materiale. Argomento per sezione 3 (architettura) e per la difesa concettuale del DSL contro obiezioni tipo «è solo una partitura testuale Csound-like».

7. **Lista dei riferimenti filosofici per il paper**: Granger (*Formes, opérations, objets*, Vrin 1994), Goodman (*Ways of Worldmaking*), Wegner (*Why Interaction is More Powerful Than Algorithms*, CACM 40/5, 1997 — nota 9 p. 236). Quest'ultimo è particolarmente utile come fonte tecnica esterna alla musica per giustificare la tesi *interaction > algorithm* nel paper.

## Collegamento alla tesi centrale

L'entretien è *il documento Vaggione più diretto* per la sezione 1 del paper CIM. La frase «aujourd'hui, le compositeur [...] interagit à tout moment avec lui, pour produire du formel» (p. 232) costituisce un *aggancio argomentativo perfetto* per la tesi del ritorno volontario al tempo differito: *oggi* la situazione tecnica abilita l'interaction permanente, ma PGE *sceglie* una modalità di interaction differita perché il loop lungo è lo spazio di esercizio del *formel morphologique* sul materiale granulare.

La triangolarità input/output/opérateur (p. 230) è la legittimazione strutturale del loop lungo: differido non significa boîte noire, significa che il triangolo resta aperto su scale temporali maggiori. Combinando entretien (triangolarità + interaction permanente) + capitolo 4 (réseau d'objets + déclaration d'attribut), il paper può argomentare che PGE *istituisce esplicitamente* il triangolo opératoire-deferred mediante la pipeline DSL/render/visualizer/editing.

Riferimento Wegner (Why Interaction is More Powerful Than Algorithms) è un *gift* per il paper: fonte tecnica esterna che rafforza la tesi senza dipendere solo da Vaggione.

## Quote chiave

> «Il convient à toutes les échelles de temps possibles, du micro au macrotemps. C'est précisément l'intérêt de la *catégorie d'objet*: pouvoir mettre en rapport des échelles différentes, avec leurs modes de représentation propres, dans la même entité opératoire» (p. 225)

> «en réalité, selon les cas (c'est-à-dire selon les morphologies), on trouve ce seuil entre micro et macrotemps à partir d'un ordre de grandeur de 50 millièmes de seconde. De manière alternative, on pourrait dire que ce seuil se trouve dans des distributions de sons dont la densité dépasse les 20 "grains" par seconde» (p. 225)

> «Je ne connais pas de musicien qui ne fasse pas, d'une manière ou d'une autre, une "proposition d'écoute". Chaque artiste propose une "version-monde", comme dirait Goodman» (p. 228)

> «Dans une "musique de Turing" [...] on met quelques données et l'on obtient un résultat, mais sans avoir la moindre interaction dans le chemin entre l'entrée et la sortie. Dans cette situation, il n'y a pas d'opérateur. Et on ne peut pas parler d'opérations s'il n'y a pas d'opérateur» (p. 230)

> «L'interaction est donc une relation à trois: entrée, sortie et opérateur. — Oui, c'est un puzzle triangulaire.» (p. 230)

> «Aujourd'hui, nous sommes dans une situation où le compositeur ne se limite plus à planifier un processus pour le regarder marcher tout seul, en attendant qu'il lui donne quelque chose: il interagit à tout moment avec lui, pour produire du formel. [...] On peut dire donc qu'il produit ainsi des singularités» (p. 232)

> «l'approche opératoire telle que nous l'avons définie n'était pas possible avec les langages informatiques dits "structurés" des années 1960–1970 [...] maintenant qu'elle est posée, en partie grâce à un glissement de paradigme dans l'informatique (allant du "structuré" à ce qu'on appelle "programmation orientée-objet")» (pp. 232–233)

> «Ce n'est pas le formalisé (dans le sens d'un calcul), mais le morphologique; le formel n'est pas extérieur à la matière. L'opératoire instaure des contenus morphologiques, qui sont aussi des contenus sensibles» (p. 234)

> Nota 9 (p. 236): «Cette question est actuellement débattue dans le champ de la théorie informatique: cf. Peter WEGNER, "Why Interaction is More Powerful Than Algorithms", *Communications of the ACM* vol. 40 n° 5, 1997, p. 80–91.»

## Sezioni del paper CIM 2026 dove citare

- **Sezione 1 Introduzione**: triangolarità interaction (p. 230) + *interaction permanente possible aujourd'hui* (p. 232) come legittimazione del ritorno volontario al tempo differito come scelta operatoria, non vincolo tecnico. Cit. Wegner 1997 come riferimento esterno.
- **Sezione 2 Sintesi granulare**: soglia ~50 ms / 20 grains-sec (p. 225) come riferimento empirico-morphologique per i default range PGE.
- **Sezione 3 PGE architettura**: OOP come paradigm shift abilitante (pp. 232–233) — giustificazione filosofica della scelta architetturale OOP di PGE; *catégorie d'objet su tutte le scale temporali* (p. 225) come argomento per la coerenza Stream/Voice/Controller a scale gerarchiche multiple.
- **Sezione 4 Partitura grafica**: *proposition d'écoute* / *version-monde* alla Goodman (p. 228) come framework concettuale del score_visualizer; immanentismo (p. 234) come argomento contro la lettura della partitura come formalizzazione esterna.
- **Sezione 6 Conclusioni**: *formel = morphologique, non formalisé* (p. 234) come tesi conclusiva — il loop lungo PGE produce *du formel* nel senso vaggioniano, articolazione morphologique del materiale, non formalizzazione astratta.

## Domande aperte

- Le pp. 221–223 (introduzione di AS via Granger) non sono state lette in dettaglio. Eventualmente da rivisitare per estrarre l'inquadramento granger-iano dell'objet/opération se il paper finisce per esplicitare il riferimento Granger (Granger 1994 *Formes, opérations, objets* è citato in nota 1 p. 235).
- La connessione *cognitivisme énactif* / *paradigm shift en intelligence artificielle* (p. 239, fine del successivo entretien Schönberg/Wittgenstein dove HV interviene) — se rilevante per giustificare il framework opératoire come *non-simbolico*, andrebbe verificata.
