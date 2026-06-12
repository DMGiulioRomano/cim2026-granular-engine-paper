# Interattività come rate di feedback — ridefinizione CIM

## Definizione

L'interattività nella composizione assistita dal computer non si riduce a *immediate audible output*. È la possibilità per l'operatore di agire su livelli diversi del flusso musicale — audio-rate, event-rate, livelli superiori — mantenendo aperto il triangolo input/output/opérateur. Il *rate* del feedback determina la *scala temporale* dell'interazione, non la sua presenza o assenza.

PGE è un sistema interattivo il cui rate di feedback è il **loop lungo**: specifica YAML → generazione → ascolto → riflessione → riscrittura. L'interazione non è abolita dal tempo differito — è esercitata a una scala temporale diversa dal real-time gestural.

## Fonti convergenti

Cinque linee indipendenti convergono sulla stessa ridefinizione.

### 1. Di Scipio 1995 — taxonomy 4-quadrant (CIM XI)

> «*Interactivity requires the possibility of exerting real-time controls over various parts of a program such that both the sonic and syntactic levels can be accessed by the user [...] interactivity cannot simplistically mean immediate audible output — it also means that the user can address his/her action to different rates of change in the musical flow, from audio-rate through event-rate and higher*» (p. 19, [[discipio1995]])

Di Scipio distingue 4 quadranti:

| | Program | Environment |
|---|---|---|
| **Composition** | specifica determinata + opzioni event-rate | sistema aperto + variabili ambientali |
| **Performance** | partitura + esecuzione | improvvisazione + real-time feedback |

PGE occupa il quadrante **composition × program** — sistema determinato (YAML) con opzioni event-rate (envelope, strategie, dephase). Il rate del feedback non è audio-rate (gestural) né environment-driven (ecosistemico): è il ciclo render-per-render del loop lungo.

### 2. Truax 1990 — gap controllo/percezione

> «*It is obviously impossible for the composer to specify each individual grain, given that there may be thousands of them per second. It reduces to absurdity the idea of total control by the composer. Hierarchic levels of control are absolutely necessary.*» (p. 131, [[truax1990]])

> «*the composer functions not as an omniscient arbiter, but as the source of control messages that guide the overall process without directly determining it*» (p. 132)

Il gap `d·n` (parametri × grani) è il problema condiviso. La risposta di Truax è il loop stretto real-time — il compositore come sorgente di messaggi di controllo durante l'esecuzione. La risposta di PGE è il loop lungo — il compositore come sorgente di *intenzioni parametriche dichiarative* fra cicli di rendering. Due scale temporali di interazione, stesso gap.

### 3. Vaggione 1996 — interaction forte écriture↔algorithme

> «*toute intervention directe peut être considérée comme la déclaration d'un attribut particulier d'une entité quelconque; cet attribut peut dès lors être généralisé à toutes les instances successives de cette entité [...]. De cette symétrie s'en suit une imbrication des deux possibilités d'action, sans qu'aucune ait à souffrir d'une inféodation à l'autre*» (p. 2, [[vaggione1996]])

L'*interaction forte* è l'imbrication tra polo manuale (écriture directe) e polo algoritmico (traitement). Non richiede real-time: richiede che l'opérateur possa intervenire su entrambi i poli. Il DSL YAML PGE è il livello in cui le due possibilités d'action coesistono — un valore scritto a mano è una *déclaration d'attribut*, un envelope ne è la *généralisation*.

### 4. Solomos/Soulez/Vaggione 2003 — triangolarité interaction

> «*L'interaction est donc une relation à trois: entrée, sortie et opérateur. — Oui, c'est un puzzle triangulaire.*» (p. 230, [[solomos2003-ent04-de-loperatoire]])

> «*Aujourd'hui, nous sommes dans une situation où le compositeur ne se limite plus à planifier un processus pour le regarder marcher tout seul [...] il interagit à tout moment avec lui, pour produire du formel.*» (p. 232)

Una *boîte noire* (musique de Turing, sérialisme integrale, GENDYN) ha solo input/output; manca l'opérateur. L'interazione esige la *presenza costante* dell'opérateur. Il loop lungo PGE mantiene il triangolo aperto in tempo differito: l'opérateur interviene tra un ciclo render e il successivo. Differito ≠ non-interattivo; è interazione *asincrona*.

### 5. Solomos 2005 — concetti operativi, non importati

> «*Vaggione's concepts are not implementations of imported notions. These concepts, Vaggione tells us are operative*» (p. 12, [[solomos2005]])

> «*generalized interaction being internal to the musical work*» (Vaggione 1995: 100, citato p. 3)

L'interazione è *interna all'opera* — non una proprietà dell'interfaccia utente. Il rate del feedback è un parametro compositivo, non un vincolo tecnico. Solomos chiarisce che per Vaggione *interaction* non è latenza dell'interfaccia ma articolazione écriture↔algorithme — il *come* si opera, non la velocità dell'output.

## Sintesi per PGE

Le cinque fonti convergono su una ridefinizione operativa:

| Fonte | Concetto chiave | Rate di feedback |
|---|---|---|
| Di Scipio 1995 | accesso a rate diversi della musical flow | event-rate e higher |
| Truax 1990 | compositore come sorgente di messaggi di controllo | real-time (loop stretto) |
| Vaggione 1996 | imbrication écriture↔algorithme | per-intervento (ciclo editoriale) |
| Vaggione/Solomos 2003 | triangolarité input/output/opérateur | permanente asincrona |
| Solomos 2005 | interazione interna all'opera | determinata dalla composizione |

PGE eredita il quadro unificato: il loop lungo è il rate di feedback a cui l'opérateur mantiene aperto il triangolo nel quadrante composition×program. Il tempo differito è la *configurazione temporale* dell'interazione, non la sua negazione.

Argomento difensivo chiave: chi obietta «PGE non è interattivo perché è offline» confonde *interactivity* con *immediate audible output* — esattamente ciò che Di Scipio 1995 p. 19 dichiara «simplistic». Il Wegner 1997 (CACM 40/5, nota 9 in [[solomos2003-ent04-de-loperatoire]] p. 236) fornisce la base formale esterna alla musica: *Why Interaction is More Powerful Than Algorithms*.

## Sezioni del paper CIM 2026 dove citare

- **`sec:implicazioni`** (primaria): interattività ≠ uscita udibile immediata
  — sostiene l'argomento Vaggione/Di Scipio della sezione.

Fonte di verità: [[mappa-citazioni-paper]].

