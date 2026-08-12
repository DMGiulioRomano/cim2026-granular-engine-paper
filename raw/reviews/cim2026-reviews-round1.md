# CIM 2026 — Submission 159: esito e review (verbatim)

**Fonte:** email Comitato Organizzatore XXV CIM + EasyChair, ricevuta 2026-08-12.
**Esito:** ACCEPTED (comunicazione orale). Review 1: score 0 (borderline). Review 2: score 2 (accept).
**Camera-ready + registrazione:** entro 2026-08-31.
**File immutabile** (layer `raw/`): non modificare. Le risposte vivono in `docs/plans/`.

---

## Lettera di accettazione

Dear Author,

We are pleased to inform you that the article titled “DIRAC: UN AMBIENTE DICHIARATIVO PER LA GRANULAZIONE E LA SUA MAPPA SINOTTICA” has been accepted for presentation and publication at the 25th Colloquium on Music Informatics, to be held in L’Aquila from October 13 to 16, 2026.

IMPORTANT:
When submitting the final version of the article (camera-ready), due by August 31, please incorporate the reviewers’ comments or inform us of any comments you choose not to incorporate, providing an appropriate justification for your decision. The Scientific Committee reserves the right to review the final version of the article to verify that it is consistent with the feedback provided during the review process and, if necessary, to contact the authors again.

We also invite you to register for the Colloquium by August 31, reminding you that the presentation and publication of the paper are CONDITIONAL upon the attendance of at least one of the authors.

Here is the link to the registration form: https://forms.gle/gLvKXoqSD9Wrx5eR9
PLEASE NOTE! A separate registration form must be completed for each participating author and for each accepted paper.

On the CIM website https://musel.consaq.it/cim2026/strutture-ricettive/, you will also find useful information regarding accommodations during the conference. We encourage you to book your stay as soon as possible, as there will be many events related to L’Aquila, Italian Capital of Culture 2026, taking place during the conference.

As soon as the detailed program of activities and musical performances is available, you will receive a notification. In the meantime, we encourage you to check the Colloquium website periodically for the most up-to-date information: https://musel.consaq.it/cim2026/

Congratulations, and we look forward to seeing you in L’Aquila!

The Organizing Committee of the 25th CIM

SUBMISSION: 159
TITLE: DIRAC: UN AMBIENTE DICHIARATIVO PER LA GRANULAZIONE E LA SUA MAPPA SINOTTICA

---

## ----------------------- REVIEW 1 ---------------------

SUBMISSION: 159
TITLE: DIRAC: UN AMBIENTE DICHIARATIVO PER LA GRANULAZIONE E LA SUA MAPPA SINOTTICA

----------- Overall evaluation -----------
SCORE: 0 (borderline paper)
----- TEXT:
L'articolo propone una codifica testuale dei parametri tradizionali di granulazione (e una mappa grafica che ne rappresenta possibili istanze concrete).

Il sistema è interessante e può essere utile a compositori che vogliano pensare alla granulazione in tempo differito. Ho apprezzato molto l'idea di partire da una granulazione "nulla" e costruire sistemi più complicati.
Detto questo, l'articolo ha anche due problemi maggiori.

1) L'articolo espone  l'elemento dichiarativo della sintesi granulare come elemento di novità della ricerca (con eccezione per il caso di CMask). A me sembra che tutto ciò che l'articolo propone è un tipo di encoding dei parametri fondamentali su cui opera la granulazione. Gli esempi più avanzati, in fondo all'articolo, sono esempi che uno studente di un corso di musica elettronica fa tranquillamente in ambiente Max o PD usando funzioni come inviluppi, numeri come input, e così via.

I controlli di ingresso di una patch simile (ignorando il motore di sintesi) sono equivalenti alla scrittura YAML che l'articolo propone, sono egualmente dichiarativi, e si potrebbe muovere l'obiezione che sono anche più efficaci. Da un lato, l'articolo dovrebbe avere più cautela nel posizionarsi – e molti dei paragrafi incomprensibili, temo, collasserebbero a quasi nulla se si togliesse il linguaggio fumoso dietro a cui un po' si nascondono.

Dall'altro lato, l'articolo spiegare meglio in quali contesti la notazione testuale sarebbe che propone sarebbe più efficace, e perché, rispetto alla una notazione grafica e interattiva degli ambienti descritti sopra.

(Tra l'altro gli autori invece mettono nelle conclusioni una discussione su tempo reale e tempo differito che non fa mai male, ma che non è strettamente necessaria. A essere tempo reale o tempo differito è il *motore* della granulazione, non la descrizione: basta considerare nuovamente il parallelo tra la codifica YAML e i controlli in patch Max. E il motore di granulazione non è in alcun modo oggetto dell'articolo. L'unico elemento che è soggetto a questa distinzione nell'articolo è la mappa che gli autori chiamano MAP – una rappresentazione visiva certamente utile, ma il cui status penso sia sopravvalutato nell'articolo.)

2) L'articolo è scritto in maniera a tratti confusa e a tratti incomprensibile, con locuzioni forse evocative in contesti poetici, ma al limite dell'incomprensibile a una lettura di articolo da conferenza ("la specifica si compila e si consuma", "l’artefatto normalizzato su cui operano le trasformazioni", "Nel congelamento le due vie sono complementari", "come gli esempi successivi dispiegano", "grani fedeli e grani devianti in proporzione componibile nel tempo" "I primi tre angoli del quadro sono già a tema", "un controllo che la tradizione tiene fuso o binario", "là subìto, qui scelto in quanto abitabile"...)
A tratti, sono proprio parole in libertà. Altre volte, sono termini fuorvianti (come dephase invece di jitter).

L'autore/gli autori dovrebbero fare uno sforzo di chiarezza, ed essere molto più semplici, a partire dall'introduzione.
Dovrebbero riportare i codici sotto le immagini corrispondenti, perché altrimenti ci si perde.
Dovrebbero ripensare la terminologia, semplificandola e rendendola più chiara.
Dovrebbero anche, se possibile, includere una specifica completa del linguaggio che faccia capire la ramificazione di proprietà, sottoproprietà e valori.
Ho anche la sensazione che l'articolo sia troppo lungo per quello che propone, e che lo sforzo di chiarezza potrebbe sfrondare un po' di lungaggini a vantaggio di una facilità di lettura.

Per esempio, le equazioni riportate sono corrette, così come i modelli probabilistici indicati, ma francamente non servono a granché nel contesto di questo articolo: è parte del fumo che copre l'oggetto fondamentale.


Per tutte queste ragioni, penso che l'articolo sia completamente accettabile nel suo contenuto, ma non nella sua forma, e per essere accettabile dovrebbe avere una riscrittura accurata.



=========
Note dettagliate:

Abstract
-> "queryable IR" – non è chiaro cosa si intenda: immagino "intermediate representation", come nell'acronimo precedente, ma allora è meglio scriverlo per esteso.

§1

"Quando la massa passa a un controllo algoritmico, fra ciò che si dichiara in ingresso e ciò che si percepisce in uscita resta una distanza opaca: la dichiarazione governa il risultato senza renderlo leggibile." -> in che senso "ciò che si dichiara in ingresso"? Quando la massa passa a un controllo algoritmico, tipicamente in ingresso ci sono valori di parametri base (posizione e durata dei grani, jitter vari, densità etc.). Se questo è ciò che l'autore intende, dovrebbe spiegare perché questo è "dichiarativo", e perché rende il risultato non leggibile.


"dove il parametro espressivo dominante è la posizione di lettura nel materiale, cioè proprio ciò che una specifica testuale non mostra: da quale punto del campione ogni grano è pescato" -> certo, l'onset dei grani è un parametro fondamentale in una granulazione – ma che vuol dire "una specifica testuale non mostra"? Quale specifica testuale? Una specifica testuale può tranquillamente mostrare l'onset del grano insieme a altre proprietà...

"Tre tradizioni hanno attraversato questa distanza da lati diversi, e nessuna la chiude dallo stesso lato." -> ho finito di leggere il paragrafo e mi sono perso nei suoi meandri...


(Incidentalmente, in che senso SuperCollider dichiara l'esito e non la procedura? Mi sembra che in superCollider uno possa tranquillamente dichiarare la procedura...)


§2
Nell'esempio in Figura 1 ho un certo numero di domande

- che c'entra la legenda "pitch(cents)"?
Se c'è solo perché la MAP è fatta così e non viene ancora usata (come penso), specificarlo in didascalia.

-> perché c'è un wrapping tra la fine e l'inizio? Implicitamente il modello assume buffer circolari e senza click? È un'assunzione forte che va quantomeno esplicitata. Che succede ai campioni che sono a cavallo?

- perché il verso di lettura cambia? Capisco che cambi sempre in direzione della derivata (ma allora perché cambia alla fine?) ma in ogni caso non è quello che uno potrebbe volere (io, per esempio, non lo vorrei). Non dovrebbe essere un parametro a parte?

- "Questo comportamento non è visualizzabile attraver- so la forma d’onda, sonogramma o altre rappresentazioni sinottiche."; " si può comprendere indirettamente osservando la disposizione retrograda del materiale ma solamente in condizioni di variazioni minime" -> non ho capito. Mi sembra che questo comportamento sia semplicemente cinematica di base.


- Attenzione alla footnote 7, che fa sembrare il numero due alla settima. La nota sul fatto che il "fill_factor" è semplicemente l'overlap andrebbe messa nel testo, perché quello è il termine colloquiale più noto, nonostante la reference di Roads.

Figura 2:
non è leggibile: serve una figura con densità di grani molto più bassa per far capire cosa succede. Tra l'altro penso che la figura 2 vada quindi messa dopo.

Perché IOT ha una linea superiore? È perché è il passo medio, suppongo, ma a questo punto è meglio spiegare, e meglio ancora sarebbe mettere IOT_{average}

"in ascissa il tempo del brano, in ordinata la posizione di let- tura nel buffer, qui costante, per il freeze, e ogni segmento un grano; da sinistra a destra la spaziatura passa da unifor- me a dispersa, a parità di numero medio di grani" -> questa deve andare nella didascalia della figura.

"Quando la densità è alta e il passo regolare, la griglia è essa stessa periodica, e un treno periodico di grani ha uno spettro a ri- ghe, spaziate a multipli della densità" -> Servirebbero illustrazioni spettrali e non temporali per queste affermazioni.

"Nel congelamento le due vie sono complementari" -> congelamento di cosa?

Il listato 3 non è referenziato nel testo e andrebbe commentato. Non si capisce la sua relazione con le altre figure.

"ed entrambe accettano envelope" -> inviluppi è una parola italiana che si può tranquillamente usare al posto di Envelope in tutto l'articolo.

"Le due masche- re di questa sottosezione vivono in un solo YAML, due stream affiancati in un’unica MAP ed etichettati (a) e (b) nella figura, costruiti per isolarle." -> Manca il numero della figura.

L'implementazione dello spostamento probabilistico di FIgura3/Listing4 è barocca se non  (incidentalmente sarebbe meglio che tutti i listing andassero con le loro figure, per chiarezza)
Il nome "dephase.pointer" per ciò che il parametro fa è fuorviante: questa è una probabilità di spostamento dell'onset. Dephase richiama tutto tranne la probabilità (e solo marginalmente lo spostamento dell'onset).
Se ho capito bene il caso specifico, penso che questo inviluppo dovrebbe essere anch'esso una sotto-proprietà del pointer, p.es. offset_probability. (O magari non ho capito io l'esempio, nel qual caso andrebbe spiegato meglio.)

"le due morfologie non potrebbero essere più diverse" -> Locuzione un po' colloquiale che va tolta – certo che possono essere più diverse! ;-)
Anche la spiegazione successiva è esageratamente floreale...

Equazione 2:
cos'è v_n?

"Il caso (a) è questo modello all’opera", ok, però con funzione c(tau_n) costante

"Ampiezza (ρ) e probabilità (p) sono dunque due envelope ortogonali, (a) muove la prima a gate aperto, (b) la seconda
a banda fissa." -> non si capisce

Attenzione che "dephase" è scelto male come termine anche successivamente: dephase non è deviazione... Sicuri che non volete parlare di jitter invece?

Figura 4:
"La probabilità sale da 0 a 100% con andamento cubico fra il 20% e l’80% della durata; la banda netta di sinistra si sfrangia in nuvola a destra." -> dove vedete l'andamento cubico nella curva? io vedo una lineare a tratti a scalini... Idem per 20% e 80%, non lo vedo. Il valore di deviazione, che alla fine della figura è 100, che cosa rappresenta? 100% di cosa? Della lunghezza del grano?

"È la matrice somma-differenza di Blumlein [2]: a θ = 0 il grano è centrato, a ±45◦ è tutto su un canale" -> perché specificare MId-Side e Blumlein? Theta è una rappresentazione astratta dell' azimuth, no? Come venga poi realizzata dovrebbe essere irrilevante a questo livello, no?
E perché non estendere la rappresentazione allo spazio e non solo alla circonferenza unitaria – uno poi può realizzare i grani con lo spazializzatore che più preferisce...

"Come ogni parametro, pan ammette una traiettoria centrale e un range: pan_range distribui- sce i grani sul campo, grano per grano, secondo lo schema" -> non capisco: pan_range non sembra un jitter sul pan, giusto? È l'apertura del fronte sonoro per ogni grano? Nel qual caso penso che range sia un cattivo nome (aperture?) e non capisco il "Come ogni parametro"... offset_range era un jitter sull'offset; pan_range non è un jitter sul pan?
Se invece non è questo il caso, allora proprio non ho capito cos'è pan_range...

§3
"La svolta è do- cumentabile con precisione negli atti: nel volume del 1993" -> se ricordo bene, la sintesi granulare in tempo reale in realtà data di molto prima, ed è noto anche agli autori il caso di Riverrun di Truax (1986). E in generale ho l'impressione che il panorama di riferimenti degli autori sia molto focalizzato su articoli CIM, per una ragione che non comprendo bene. Questo certamente non aiuta l'articolo...

In che senso "Ciò che qui è proprio è dove la specifica resta interrogabile" ? Serve più chiarezza, e parlare di casi concreti. Che cosa si può fare con questa rappresentazione YAML che non si possa fare con l'interfaccia di oggetti Max di cui parlavo in apertura di review? (anch'essi hanno uno stato mantenuto durante tutto il sequencing dei grani)

"esporre come asse dichiarativo continuo, componibile come envelope, un controllo che la tradizione tiene fuso o binario. Due casi la circoscrivono" -> qui proprio non si capisce. A che cosa si riferisce il "la" e come fanno due casi a "circoscrivere" (sic) qualcosa...? Rimane estremamente fumoso per me anche tutto il paragrafo successivo.

§4
"perché l’architettura tiene il ritorno dell’ascolto abbastanza vicino alla scrittura da fare del ciclo uno spazio di lavoro" -> ma che vuol dire?


## ----------------------- REVIEW 2 ---------------------

SUBMISSION: 159
TITLE: DIRAC: UN AMBIENTE DICHIARATIVO PER LA GRANULAZIONE E LA SUA MAPPA SINOTTICA

----------- Overall evaluation -----------
SCORE: 2 (accept)
----- TEXT:
The paper presents DIRAC, a declarative environment for granular synthesis expanded with a graphical representation of the compositional processes through the Multiparametric Audio Plot.

In general, I found the contribution technically concrete and well grounded in the literature. The authors provide a functioning implemented system, code and audio examples, explicit configurations, and several useful visualizations. I also found the structure of the paper particularly effective, as it makes the description of the system’s individual controls generally clear and easy to follow.

I still have several minor concerns.

First, the actual usefulness of the MAP is mostly asserted rather than evaluated. The figures show that the representation can display several parameters at once, and this is particularly relevant in the more complex examples, where the amount of information becomes quite dense and potentially difficult to interpret. A few comments on this would help strengthen the motivation for introducing this visualization.

Second, the novelty of the contribution could be stated more clearly. While the authors acknowledge that most of the granular algorithms are inherited from previous work, the distinction between established techniques and the original aspects of DIRAC remains somewhat dispersed throughout the paper. As a matter of presentation, a more explicit summary of the main contributions would help clarify where the main novelty lies.

Finally, I found the justification for deferred-time rendering only partially convincing. The authors state that offline rendering is a necessary condition for the proposed approach, but they do not fully explain why the same declarative representation and visual analysis could not be maintained in a real-time or hybrid system. A brief comment on this would clarify the claim.

Besides these, overall, I strongly recommend revising the writing style. The paper frequently alternates between overly colloquial formulations and highly elaborate expressions, often privileging linguistic virtuosity over direct and precise explanation. This makes the register inconsistent and occasionally obscures otherwise clear technical content.

Despite these minor concerns, I still believe that the paper has merit and constitutes a solid contribution. For these reasons, I lean toward acceptance, while still encouraging the authors to revise the writing and clarify the aforementioned points.
