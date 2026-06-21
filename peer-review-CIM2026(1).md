# Peer review — *Un ambiente Python per l'elaborazione granulare: dal codice alla partitura grafica*

**Conferenza:** XXV CIM — Colloquio di Informatica Musicale, L'Aquila, 13–16 ottobre 2026
**Tema:** *Sounding the Posthuman*
**Sistema descritto:** DIRAC — *Declarative Intermediate Representation for Audio Composition*
**Stato del manoscritto:** corpo "quasi" completo; mancano abstract, introduzione e conclusioni.
**Modalità di selezione:** double-blind.

---

## Indice

1. [Inquadramento e adeguatezza alla call](#1-inquadramento-e-adeguatezza-alla-call)
2. [Valutazione sintetica](#2-valutazione-sintetica)
3. [Punti di forza](#3-punti-di-forza)
4. [Criticità maggiori](#4-criticità-maggiori-da-affrontare-in-revisione)
5. [Criticità minori ed editoriali](#5-criticità-minori-ed-editoriali-rapide-da-correggere)
6. [Tratti potenzialmente riconoscibili come LLM](#6-tratti-potenzialmente-riconoscibili-come-llm)
7. [Proposta di abstract (tre livelli)](#7-proposta-di-abstract-tre-livelli)
8. [Consigli per l'introduzione](#8-consigli-per-lintroduzione)
9. [Consigli per le conclusioni](#9-consigli-per-le-conclusioni)
10. [Checklist operativa pre-invio](#10-checklist-operativa-pre-invio)

---

## 1. Inquadramento e adeguatezza alla call

Il paper descrive **DIRAC** (*Declarative Intermediate Representation for Audio Composition*), un ambiente Python per la granulazione di materiale campionato basato su:

- un **DSL dichiarativo in YAML** (il compositore dichiara *l'esito voluto*, non la procedura);
- una **rappresentazione intermedia (IR) ancora dichiarativa**, interrogabile, con **materializzazione differita** grano-per-grano;
- la **MAP**, un sistema di logging grafico multiparametrico presentato come "notazione differenziale" / partitura.

L'esposizione procede *per scostamenti dalla trasformazione identica*: dal grano minimo fino a una texture complessa a più voci. È una strategia espositiva elegante e coerente.

**Adeguatezza alla call: alta.** Il lavoro intercetta in modo diretto almeno cinque topic:

- *Programming languages and music representation paradigms*
- *Computer-aided composition and performance*
- *Computing in sound art practices*
- *Aesthetics of computer and interactive music*
- *Extended, Distributed and Posthuman Agency in Composing and Performing*

Quest'ultimo è il gancio più forte al tema **"Sounding the Posthuman"**: l'idea di un'agency distribuita tra la *dichiarazione* del compositore e la *materializzazione autonoma e differita* del sistema è esattamente la "co-evoluzione tra intenzionalità e autonomia dei sistemi" evocata dalla call — ma **questo legame nel corpo non è mai reso esplicito** (vedi §4). Va recuperato in introduzione/conclusioni.

---

## 2. Valutazione sintetica

Contributo solido, originale e ben scritto sul piano espositivo, ma allo stato **incompleto** non solo per l'assenza di abstract/intro/conclusioni: mancano **stato dell'arte/posizionamento** e **qualunque forma di valutazione o discussione dei limiti**.

| | Giudizio |
|---|---|
| Con le integrazioni indicate | **Accept** |
| Allo stato attuale | **Weak accept / major revision** |
| Correttezza tecnica e formale | Buona / verificata |

---

## 3. Punti di forza

1. **Idea centrale forte e ben motivata.** Il livello intermedio dichiarativo + materializzazione differita + ispezionabilità è una proposta concettualmente interessante, in controtendenza rispetto all'opacità del DSP granulare in tempo reale. L'argomento *"questo comportamento non è visualizzabile attraverso forma d'onda, sonogramma o altre rappresentazioni sinottiche"* (p. 2) giustifica bene la MAP.
2. **Coerenza espositiva.** Il filo degli "scostamenti dalla trasformazione identica" tiene insieme tutto il paper e ha valore pedagogico dichiarato.
3. **Radicamento nella tradizione granulare:** Roads, Truax (real-time GS, sync/async, tendency mask), De Poli–Piccialli, Vaggione (*décorrélation microtemporelle*). Citazioni pertinenti.
4. **Formalizzazione corretta.** Verifica dei passaggi matematici:
   - **Eq. (1)** — `IOT(d) = (1−d)·IOT̄ + d·𝒰(0, 2·IOT̄)`: valore atteso = `IOT̄` per ogni *d*, coerente con l'affermazione che la densità media si conserva. ✔
   - **Eq. (2)/(3)** — tendency mask con gate Bernoulliano: per `p≡1` la (3) ricade correttamente nella (2). ✔
   - **Eq. (4)** — matrice Blumlein: `L²+R² = s²` (potenza conservata ✔); a 0° centrato, a ±45° tutto su un canale, oltre ±45° eccede gli altoparlanti (regione fuori fase). Tutte le affermazioni del testo tornano. ✔
5. **Onestà del dato.** Il confronto sorgente/resa è *gain-matched* e quantificato (residuo < −74 dB RMS, Fig. 1): verifica concreta dell'invarianza nella configurazione minima.

> **★ Insight — perché l'idea "IR dichiarativa" è non banale**
> In informatica un'IR è di norma un *lowering* verso istruzioni più concrete; qui invece l'IR resta allo stesso livello logico della specifica — è ancora dichiarativa, ne calcola il valore a ogni tempo *t* senza averlo materializzato. È una forma di *deferred / lazy evaluation* applicata alla composizione: il sistema mantiene la *legge* (l'envelope) e non il *campione*. Questo è ciò che rende la specifica "interrogabile" e graficabile — ed è il vero perno teorico del paper, attualmente sotto-tematizzato.

---

## 4. Criticità maggiori (da affrontare in revisione)

1. **Assenza di stato dell'arte / posizionamento.** Le 7 referenze coprono solo la tradizione granulare fondativa. Manca il confronto con ciò a cui DIRAC si oppone o si affianca: linguaggi/DSL per la composizione e la sintesi (Csound score, Common Music/Nyquist, SuperCollider patterns, Faust), sistemi a partitura/notazione algoritmica (l'area TENOR, fortemente contigua al CIM), e tool granulari esistenti. Senza questo, la novità resta affermata ma non *situata*. **È la lacuna più seria sul piano scientifico.**
2. **Nessuna valutazione né discussione dei limiti.** Il paper è interamente descrittivo. Per un *system paper* servono almeno:
   - una sezione "limiti e lavori futuri";
   - una *availability statement* (repository, anche anonimizzato);
   - dettagli implementativi/architetturali (come avviene il rendering, performance, dipendenze);
   - idealmente esempi audio linkati o un mini-confronto qualitativo.
3. **Tensione concettuale "log ↔ partitura" irrisolta.** Il titolo promette "partitura grafica", ma il corpo la chiama "logging grafico" e "notazione differenziale". *Partitura* implica prescrittività/leggibilità per un lettore; il *log* è descrittivo e post-hoc. È una distinzione importante — e proprio il terreno su cui il CIM (area notazione/TENOR) valuterà il lavoro. Va chiarito esplicitamente: la MAP è descrittiva, prescrittiva, o entrambe a seconda dell'uso? Materiale ideale per le conclusioni.
4. **Il tema "posthuman" non è agganciato nel corpo.** C'è un sistema che merita la cornice della call, ma il legame con l'agency distribuita/non-umana è tutto implicito. Va reso esplicito (senza forzature: la materializzazione differita e autonoma *è già* l'argomento posthuman).
5. **"MAP" non è mai definita.** L'acronimo/termine compare decine di volte ("la MAP del rendering") senza essere sciolto né introdotto alla prima occorrenza. Per un termine così centrale è un problema.

---

## 5. Criticità minori ed editoriali (rapide da correggere)

- **Cross-reference rotto:** a p. 2 — *"Resta da guardare questa griglia: è l'oggetto di §2.3"* — ma la sezione è **§1.3** ("La griglia temporale"). Non esiste alcuna §2.3. Da correggere.
- **Placeholder rimasto nel testo:** la didascalia del **Listing 5 recita letteralmente "da inserire"** (p. 5), mentre il listato c'è. Va sostituita con una caption reale. È esattamente il tipo di residuo da bonificare prima dell'invio.
- **Numerazione delle sezioni:** tutto il paper è annidato sotto "1. DIRAC…" (1.1–1.7). Aggiungendo intro e conclusioni la struttura andrà ri-livellata (intro come §1, DIRAC come §2…); rifare i rimandi interni *dopo*, per evitare nuovi §-rotti.
- **Leggibilità delle figure.** Le MAP (Figg. 2–3, 5–10) sono molto dense: testo degli assi e legende minuscoli, rischio illeggibilità in stampa/PDF a colonna. Valutare zoom su un dettaglio significativo o figure a piena larghezza per le 1–2 più importanti.
- **Accessibilità (special topic della call!).** La MAP codifica il *pitch* col colore (colormap). Vale la pena dichiararlo come limite e/o offrire ridondanza non cromatica — coerente con il topic *Accessibility and inclusion*.
- **Titolo.** "Ambiente Python" mette in primo piano il linguaggio di implementazione, che nel corpo è quasi incidentale; il contributo è il DSL dichiarativo + la MAP. Valutare un titolo che porti avanti DIRAC / la dimensione dichiarativa-notazionale.
- **Densità di note a piè di pagina** (≈12): alcune portano contenuto tecnico sostanziale (nota 4 su delta di Dirac/Gabor, nota 10 su *fill_factor*/Roads, nota 11 su sincrono/asincrono). Almeno le più rilevanti starebbero meglio nel corpo.
- **Anonimizzazione:** l'header è correttamente anonimo (Anonymous / anonymous@anonymous) ✔. Attenzione però al **registro fortemente in prima persona + posizionamento biografico**: in un double-blind, una voce così marcata e il riferimento ravvicinato a [3] (Di Scipio–Tisato) in ambito CIM possono rendere identificabile l'autore. Non è un blocco, ma va tenuto presente.

---

## 6. Tratti potenzialmente riconoscibili come LLM

**Premessa onesta:** la prosa è in larga parte spiccatamente umana e idiosincratica — la voce in prima persona (*"Non è una difficoltà solo mia"*, *"lascio che siano esse stesse a saggiarlo"*, le chiuse aforistiche tipo *"Si compone il segnale, non si dispongono suoni"*) è l'*opposto* del registro tipico di un LLM. Non si ha l'impressione di un testo "generato". I residui possibili, se ci sono, si annidano altrove:

1. **Densità altissima di trattini lunghi (—).** È il tell statistico più noto degli LLM. *Però* qui è confuso con uno stile saggistico italiano legittimo (e affine alla scrittura di Di Scipio): da considerare "da controllare", non un verdetto.
   *Operativo:* leggere ad alta voce; se un inciso non cambia il respiro della frase, spesso il trattino può diventare virgola o punto.
2. **Formulazioni "troppo ordinate" e simmetriche** nelle descrizioni del sistema dei parametri — zone dove la rifinitura automatica tende a uniformare il ritmo. Candidati da rileggere:
   - *"Ampiezza (ρ) e probabilità (p) sono dunque due envelope ortogonali — il gemello A muove la prima a gate aperto, il gemello B la seconda a banda fissa."*
   - lo schema ricorrente *"X agisce sul tempo… Y agisce sul contenuto"* (complementarità), ripetuto più volte;
   - le didascalie molto "complete" e parallele tra loro.
   Non sono errori; hanno solo un ritmo più "liscio" del resto. Verificare che la cadenza sia dell'autore.
3. **"da inserire" (Listing 5)** non è un tratto LLM ma un TODO umano dimenticato: è comunque il primo segnale di "lavoro non rifinito" che un revisore nota. Da bonificare.

**Sintesi:** nessuna prova di testo LLM-generato nel discorso; rischio marginale e localizzato nelle descrizioni schematiche e nelle didascalie. L'azione più utile è uniformare l'uso dei trattini e rileggere ad alta voce i passaggi parametrici.

---

## 7. Proposta di abstract (tre livelli)

Articolato nei tre livelli richiesti; in fondo una versione "fusa" (~140 parole) pronta da limare. Tutto in forma anonimizzata.

### Livello 1 — Topic
La granulazione di materiale campionato pone il controllo compositivo alla scala del grano, dove l'esito sonoro emerge da popolazioni di eventi e non è riconducibile uno-a-uno ai parametri di sintesi. Nei sistemi granulari in tempo reale questo governo resta opaco: la generazione è relegata in un livello DSP non ispezionabile, e si apre una "distanza" tra ciò che il compositore dichiara e ciò che percepisce.

### Livello 2 — Stato dell'arte
La tradizione granulare (Roads; Truax; De Poli–Piccialli; Vaggione) ha fornito modelli consolidati — sincronia/asincronia, tendency mask, *décorrélation microtemporelle* — implementati però prevalentemente come processi in tempo reale o come oggetti DSP, privi di un livello intermedio dichiarativo e di una rappresentazione che renda il processo leggibile come notazione.
*(Qui andrà inserito il confronto con DSL/linguaggi per la composizione e con i sistemi di notazione algoritmica — vedi criticità §4.1.)*

### Livello 3 — Proposta
Si presenta DIRAC, un ambiente in cui il compositore dichiara l'esito voluto in un DSL basato su YAML; la specifica è tradotta in una rappresentazione intermedia *ancora dichiarativa* e interrogabile, materializzata in modo differito grano-per-grano. Una rappresentazione grafica multiparametrica (MAP) restituisce la specifica in forma ispezionabile, come notazione differenziale del processo. Il sistema è esposto per scostamenti progressivi dalla trasformazione identica, dal grano singolo fino alla texture a più voci, e mira a rendere "pensabile e leggibile" il governo della massa granulare, ricomponendo la distanza tra dichiarazione e percezione.

### Versione fusa (≈140 parole)
> La granulazione di materiale campionato colloca il controllo compositivo alla scala del grano, dove l'esito emerge da popolazioni di eventi e sfugge a un rapporto diretto coi parametri; nei sistemi in tempo reale tale governo resta opaco, relegato in un livello DSP non ispezionabile. La tradizione granulare ha consolidato modelli — sincronia/asincronia, tendency mask, décorrélation microtemporelle — privi però di un livello intermedio dichiarativo e di una rappresentazione che renda leggibile il processo. Presentiamo DIRAC: il compositore dichiara l'esito voluto in un DSL basato su YAML, tradotto in una rappresentazione intermedia ancora dichiarativa e interrogabile, materializzata in modo differito grano-per-grano. Una rappresentazione grafica multiparametrica (MAP) restituisce la specifica come notazione differenziale del processo. Il sistema è esposto per scostamenti progressivi dalla trasformazione identica, dal grano singolo alla texture a più voci, per rendere pensabile e leggibile il governo della massa granulare.

> **Nota pratica:** verificare sul template CIM se è richiesto anche un abstract in inglese (di norma sì). La traduzione può essere preparata a parte.

---

## 8. Consigli per l'introduzione

L'impostazione concordata — **contestualizzare l'ambito → puntare alla letteratura di riferimento → scivolarci dentro con la narrazione** — è tecnicamente corretta. Per questo paper, tre mosse:

1. **Aprire dal problema, non dal sistema.** Il sistema arriva come *risposta*. Il problema è la "distanza opaca tra dichiarazione e percezione" alla scala del grano: è già scritto bene nell'attuale §1, ma va isolato come motivazione iniziale prima di nominare DIRAC.
2. **Agganciare esplicitamente la letteratura e poi il tema della call.** Poche righe che collocano DIRAC rispetto a (a) tradizione granulare, (b) DSL/notazione per la composizione, (c) agency distribuita/posthuman — chiudendo sul fatto che la *materializzazione differita e autonoma* è il modo in cui il lavoro "suona il posthuman". Questo aggancio mancante farà la differenza in sede di review.
3. **Anticipare la struttura "per scostamenti".** Una frase che dichiara il metodo espositivo (dalla trasformazione identica alla complessità) prepara il lettore e legittima il registro in prima persona come scelta metodologica, non come vezzo. Attenzione all'anonimato: tenere la prima persona sul piano del *metodo*, non della biografia.

*Da evitare:* iniziare con definizioni da manuale di sintesi granulare (il lettore CIM le conosce). Entrare dal taglio proprio del lavoro: l'ispezionabilità.

---

## 9. Consigli per le conclusioni

1. **Sciogliere il nodo "log vs partitura".** Dichiarare cosa la MAP *è* e cosa *ambisce* a essere. È il punto più interrogabile del titolo: meglio anticiparlo prima del revisore.
2. **Limiti onesti** = punti di forza in una review: niente tempo reale/interattività; rendering offline; dipendenza cromatica della MAP (→ accessibilità); assenza di valutazione con utenti; ecc. Elencarli mostra controllo del lavoro.
3. **Lavori futuri concreti**, ancorati al corpo: interattività/real-time, audio examples e repository, estensione del DSL, eventuale studio di leggibilità della MAP con compositori.
4. **Chiudere ricongiungendosi al tema.** Una frase che rilegge DIRAC come spazio di co-autorialità umano/sistema chiude il cerchio con "Sounding the Posthuman" senza retorica.

> **★ Insight — struttura tipica di un *system paper***
> Problema → Stato dell'arte/gap → Proposta → Sistema/architettura → Esempi/valutazione → Limiti & future work → Conclusione.
> Questo paper è fortissimo sui due blocchi centrali (proposta + esempi) e oggi scoperto su *gap*, *valutazione* e *limiti*. Le sezioni mancanti non sono "cornice": sono i blocchi che un revisore cerca per primi.

---

## 10. Checklist operativa pre-invio

- [ ] Aggiungere **abstract** (IT + EN se richiesto dal template).
- [ ] Scrivere **introduzione** (problema → letteratura → tema posthuman → struttura).
- [ ] Scrivere **conclusioni** (log vs partitura, limiti, future work, ricongiungimento al tema).
- [ ] Aggiungere **stato dell'arte / posizionamento** (DSL compositivi, notazione algoritmica, tool granulari).
- [ ] Inserire **availability statement** + dettagli implementativi minimi.
- [ ] **Definire "MAP"** alla prima occorrenza.
- [ ] Correggere il **cross-reference §2.3 → §1.3**.
- [ ] Sostituire la caption **"Listing 5: da inserire"**.
- [ ] **Ri-livellare la numerazione** delle sezioni dopo l'aggiunta di intro/conclusioni, poi ricontrollare tutti i rimandi.
- [ ] Migliorare **leggibilità figure** (zoom/figure a piena larghezza per le MAP chiave).
- [ ] Verificare **anonimizzazione** (prima persona sul metodo, non sulla biografia).
- [ ] **Uniformare i trattini lunghi** e rileggere ad alta voce i passaggi parametrici.
- [ ] Verificare conformità al **template CIM** (margini, font, struttura, citazioni).
