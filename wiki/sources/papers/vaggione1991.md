# [Vaggione, 1991] On Object-Based Composition / Objets, représentations, opérations

## Citazione CIM
Vaggione, H. (1991). On Object-Based Composition. In O. Laske (Ed.), *Composition Theory*, Interface — Journal of New Music Research, 20(3-4), 209-216. Adaptation française révisée et augmentée: «Objets, représentations, opérations», Ars Sonora Revue 2, 1995, pp. 33-52. (PDF letto: versione francese web-archived da archive.org, 8 pp.; originale a stampa pp. 33-52)

## Argomento centrale
Programma teorico-operativo della *object-based composition*: l'oggetto sonoro digitale è una *categoria operatoria* — collezione di oggetti discreti che funziona come entità unitaria *e* collezione di campioni — manipolabile da reti di operazioni morfologiche (fragmentation / agglutination, fenêtrage) che attraversano tutte le scale temporali, dal micro al macro, eliminando la separazione classica tra composizione del suono e composizione dell'opera.

## Gap o problema identificato
- L'oggetto sonoro analogico (Schaeffer) è *opaco* rispetto alla sua micro-struttura; la bande magnétique non permette discretizzazione simbolica del segnale e quindi nessuna operazione interna sull'oggetto stesso.
- L'idea «composition = programmation» è riduttiva: l'incorporazione di tecniche OOP in composizione non deve confondere categorie dichiarative e procedurali (cita Desain/Honing 1992).
- I sistemi à manipulation directe (Scaletti 1989) e i sistemi testuali di derivazione Music V (Cmusic, Csound) restano alternative non integrate: serve consenso su rappresentazioni come *interfacce/réécritures* tra livelli operatori e codice macchina.

## Rilevanza diretta per PGE
Vaggione formula nel 1991 il framework concettuale sotto cui PGE opera nel 2026:

1. **Oggetto come collezione di campioni** (definizione b, p. 3 fr.): «un objet sonore est une collection d'échantillons». L'asse Y del *score_visualizer* PGE (posizione nel buffer) materializza esattamente questa definizione: la partitura grafica mostra da dove ogni grano pesca nella collezione di échantillons che costituisce il source object.

2. **Multi-scala come fragmentation/agglutination ricorsiva** (p. 2 fr.): «La forme globale de l'œuvre résulte ici du même travail de génération de détails et de complexités, étendu à tous les niveaux temporels. Fragmentation et agglutination sont donc des aspects du même processus». Stream → Voice → Grain in PGE è precisamente questa cascata; il VoiceManager con strategie ortogonali (pitch/onset/pointer/pan) realizza l'agglutination ascendante; la cache STEMS realizza il fenêtrage a livello stream.

3. **Réécritures tra rappresentazioni** (p. 3 fr.): YAML DSL (testuale/alfanumerica) e score_visualizer (grafica) sono entrambi accessi al medesimo dispositivo numerico — exactly «des formes différentes d'accès aux échantillons» con il code-machine ad assicurare compatibilità. PGE-ls è la traduzione/réécriture che rende il livello testuale operativamente confortevole.

4. **Encapsulation/héritage/polymorphisme come network of objects** (pp. 4-5 fr.): Stream è classe; VoiceConfig istanzia per voce; Controller × 4 sono polimorfi (stesso messaggio `tick(t)` → comportamenti diversi). ParameterOrchestrator + strategies (Pitch/Density) è esattamente la *connectivité hiérarchique* descritta da Vaggione, dove attributi di una classe vengono ereditati e ri-specificati nelle sotto-classi.

5. **Critica disjonctive declarativo/procedurale**: PGE rispetta la separazione che Vaggione raccomanda — YAML è dichiarativo (intenzione compositiva), ParameterOrchestrator è procedurale (generazione grani), nessun aggancio confuso à la Desain/Honing.

## Collegamento alla tesi centrale
Vaggione 1991 è la pre-formulazione *concettuale* del paradigma in cui PGE opera, scritta in un contesto rigorosamente tempo differito (Cmusic Music-V offspring). Il loop lungo (specifica → generazione → ascolto → riflessione → riscrittura) trova in Vaggione la sua giustificazione operatoria: l'oggetto digitale è *transparent*, *re-écrivable*, *manipolabile sintatticamente* — il che rende possibile e necessario il ciclo di osservazione/modifica esteso nel tempo. Vaggione condivide con Di Scipio 1994 la postura indeterministica del *models of detailed sonic design*, ma la traduce in framework OOP esplicito che PGE eredita con due decenni di distanza.

Vaggione anticipa anche l'argomento Roads 2001 cap. 1 sul DSL musicale: «un consensus pourrait s'établir sur la nécessité de considérer les différents modes de représentation (graphiques ou textuelles) comme des interfaces des "traductions"... entre les divers niveaux opératoires accessibles au compositeur et celui des codes numériques manipulés par la machine» (p. 3 fr.) — anticipo del programma Roads 2001 pp. 26-27 (*musical interface in which a musician specifies the desired sonic result*).

## Sezioni del paper CIM 2026 dove citare
- **Sezione 1 Introduzione**: tradizione object-based come radice del paradigma PGE (insieme a Roads, Truax, Di Scipio).
- **Sezione 2 Sintesi granulare / paradigma**: collegamento Schaeffer → oggetto digitale transparent; multi-scala come fragmentation/agglutination ricorsiva — cornice teorica della separazione micro/macro che la sintesi granulare realizza tecnicamente.
- **Sezione 3 Architettura PGE**: object-based composition come framework teorico del network Stream/Voice/Controller; classi + héritage + polymorphisme come pattern realizzato da PGE; critica declarativo/procedurale come legittimazione separazione YAML / ParameterOrchestrator.
- **Sezione 4 Partitura grafica**: «objet sonore = collection d'échantillons» come fondamento concettuale dell'asse Y = posizione-buffer.

## Quote chiave

> «un objet sonore est une collection d'objets discrets fonctionnant comme une entité unitaire; un objet sonore est une collection d'échantillons. [...] L'objet n'est pas donc un "atome insécable" mais une structure, un "composé"» (p. 2 fr.)

> «La forme globale de l'œuvre résulte ici du même travail de génération de détails et de complexités, étendu à tous les niveaux temporels. Fragmentation et agglutination sont donc des aspects du même processus» (p. 2 fr.)

> «tandis que l'objet sonore de la musique concrète analogique est opaque en relation à sa micro-structure, l'objet sonore numérique est transparent, c'est-à-dire, il peut être ouvert afin d'offrir l'accès à sa structure interne, et par conséquent permettre une écriture directe de la matière sonore elle-même» (p. 3 fr.)

> «un consensus pourrait s'établir sur la nécessité de considérer les différents modes de représentation (graphiques ou textuelles) comme des interfaces des "traductions", ou plus précisément, des "réécritures" entre les divers niveaux opératoires accessibles au compositeur et celui des codes numériques manipulés par la machine» (p. 3 fr.)

> «Il ne s'agit donc pas de réduire l'objet sonore à l'objet logiciel. [...] un réseau dans lequel les concepts et techniques dérivés d'un paradigme de programmation sont mis au service des stratégies de composition, et non pas limités par des considérations de conception du software utilisé» (p. 5 fr.) — *clausola di adeguatezza che PGE eredita: il DSL non riduce l'oggetto musicale a struttura YAML, ma usa YAML come strato di mediazione.*
