# Prompt per l'introduzione — paper DIRAC (CIM2026)

Materiale di supporto allo studente per scrivere l'introduzione del paper
*"Un ambiente Python per l'elaborazione granulare: dal codice alla partitura grafica"*
(sistema: **DIRAC**), basato sulla peer review `peer-review-CIM2026.md`.

---

## Sull'idea dell'inquadramento storico via TENOR: sì, con due raffinamenti

L'idea di scaricare i proceedings **TENOR** e fare citazioni mirate è **giusta e non generica**,
perché si aggancia a due lacune precise già diagnosticate nella review:

- **§4.1** — manca il confronto con i sistemi a partitura/notazione algoritmica,
  *"l'area TENOR, fortemente contigua al CIM"*;
- **§4.3** — la tensione irrisolta **"log ↔ partitura"**, *"proprio il terreno su cui il CIM
  valuterà il lavoro"*.

TENOR (*Technologies for Music Notation and Representation*) è il consesso dove quella tensione
è il pane quotidiano. Scaricare i proceedings e cercarvi il vocabolario "descrittivo vs
prescrittivo", "notazione del processo", "score follower / generativo" è il modo più economico
per dare alla MAP una collocazione difendibile.

**Due raffinamenti:**

1. **TENOR copre l'asse "notazione", non l'asse "DSL/linguaggio".** Il §4.1 chiede *due*
   posizionamenti: notazione algoritmica (→ TENOR) **e** linguaggi/DSL compositivi (Csound
   score, SuperCollider patterns, Nyquist/Common Music, Faust). Quest'ultimo asse in TENOR
   c'è solo di sbieco. TENOR risolve metà del gap, non tutto.

2. **Citazione funzionale, non tappeto bibliografico.** Il gap non è "poche citazioni" ma
   "novità non *situata*": ogni citazione deve sostenere una mossa argomentativa precisa
   (questo fa X, io faccio diverso perché Y). **Attenzione al double-blind**: auto-citarsi a
   TENOR/CIM in modo riconoscibile de-anonimizza.

> **★ Insight**
> - Il gap non è "poche citazioni" ma "novità non *situata*": le citazioni definiscono un
>   *contrasto*, non riempiono. Mossa forte: "X esiste e fa così → mi colloco *qui* perché
>   faccio diversamente".
> - La distinzione log/partitura è descrittivo↔prescrittivo: dicotomia classica della teoria
>   della notazione (Goodman, *Languages of Art*), che TENOR declina in continuo. Trovare quel
>   lessico dà allo studente le parole per *sciogliere* il nodo del titolo invece di subirlo.

---

## I tre prompt (da usare in sequenza)

Far ragionare sulla *struttura* e far *raccogliere/posizionare la letteratura* sono compiti
cognitivi diversi: mescolarli porta il modello a saltare al testo finale senza pensare.
Usare i prompt **in sequenza**, in conversazioni separate o con conferma in mezzo.

---

### Prompt 1 — Ragionare sulla struttura (NON scrivere ancora)

```
Sei un assistente alla scrittura accademica. NON scrivere ancora l'introduzione:
in questo passaggio devi solo RAGIONARE sulla sua struttura e propormi un'ossatura
commentata che io approverò prima di passare alla stesura.

CONTESTO
- Paper per il XXV CIM (Colloquio di Informatica Musicale), tema "Sounding the Posthuman".
- Sistema descritto: DIRAC, ambiente Python per granulazione di materiale campionato,
  basato su un DSL dichiarativo in YAML → una IR ancora dichiarativa e interrogabile
  → materializzazione differita grano-per-grano. Una rappresentazione grafica
  multiparametrica (MAP) restituisce la specifica in forma ispezionabile.
- Il corpo è quasi completo; mancano abstract, introduzione e conclusioni.
- l'abstract lo scrivo alla fine, la introduzione e la conclusione sono accennate come bozze ma non so cosa tenere.

VINCOLI DI STRUTTURA (da una peer review che ho ricevuto)
1. Aprire DAL PROBLEMA, non dal sistema: la "distanza opaca tra dichiarazione e
   percezione" alla scala del grano. DIRAC arriva DOPO, come risposta.
2. Agganciare in poche righe la letteratura su tre fronti — (a) tradizione granulare,
   (b) DSL/notazione per la composizione.
3. Anticipare il metodo espositivo "per scostamenti dalla trasformazione identica"
   (dal grano singolo alla texture), legittimando la prima persona come scelta di metodo.
4. DA EVITARE: definizioni da manuale di sintesi granulare (il lettore CIM le conosce).
5. Double-blind: prima persona sul METODO, mai sulla biografia.

COSA VOGLIO DA TE ORA
- Una scaletta dell'introduzione in 4–6 paragrafi: per ciascuno indica (i) la funzione
  retorica, (ii) la frase-cardine che lo apre, (iii) quali citazioni/concetti vanno lì.
- Segnala dove il testo rischia di scivolare nel "manuale" o nella biografia.
- Stima la lunghezza per paragrafo (il CIM ha vincoli di pagine).
- Fammi 2–3 domande se qualcosa è ambiguo. NON scrivere prosa finale.
```

---

### Prompt 2 — Stress-test della scaletta (il "secondo cervello")

```
Ora fai il revisore scettico della scaletta che hai appena prodotto.

Per ogni paragrafo chiediti:
- Un revisore CIM che non ha mai visto DIRAC capisce QUI perché il sistema serve,
  o sto assumendo conoscenza che il lettore non ha ancora?
- La novità è SITUATA (contrasto esplicito con ciò che esiste) o solo AFFERMATA?
  Dove dico "questo è nuovo" senza dire "rispetto a cosa"?
- L'aggancio al tema "posthuman" è argomentato o è retorica appiccicata alla fine?
- Il passaggio problema → letteratura → sistema scorre, o ci sono salti logici?

Riscrivi la scaletta correggendo i punti deboli che trovi. Evidenzia cosa hai cambiato
e perché.
```

---

### Prompt 3 — Inquadramento storico via TENOR (raccolta + posizionamento citazioni)

```
Mi serve costruire il posizionamento storico-scientifico dell'introduzione.
Ho scaricato i proceedings della conferenza TENOR (Technologies for Music Notation and
Representation) in [CARTELLA]. Sono in [PDF].

OBIETTIVO
Trovare i lavori che mi servono per situare DIRAC su DUE assi (non solo uno):
  ASSE A — NOTAZIONE: la tensione "log descrittivo (post-hoc) ↔ partitura prescrittiva
    (leggibile, ex-ante)". La MAP di DIRAC ritengo non sia né una partitura né un log:
    è una mappa, poiché è sinottica. Cerco
    lavori TENOR su notazione descrittiva vs prescrittiva, notazione del processo,
    visualizzazione di processi sonori, rappresentazioni intermedie.
  ASSE B — LINGUAGGIO/DSL: linguaggi e rappresentazioni dichiarative per comporre o
    descrivere il suono (anche fuori TENOR: Csound score, SuperCollider patterns,
    Nyquist/Common Music, Faust). Cerco il contrasto: DIRAC è dichiarativo + IR
    interrogabile + materializzazione differita; cosa NON lo è e perché.

COSA FARE
1. Spoglia i PDF nella cartella ed estrai i candidati pertinenti ai due assi.
2. Per OGNI candidato produci una riga: [autore, anno, titolo] — claim del lavoro in
   1 frase — COME lo uso io (contrasto / continuità / vocabolario che prendo in prestito).
3. Scarta i lavori che non fanno lavoro argomentativo: voglio citazioni FUNZIONALI,
   non un tappeto bibliografico. Punta a 4–7 referenze totali, le più incisive.
4. Proponi, per l'asse A, il vocabolario tecnico (es. descrittivo/prescrittivo,
   eteronomo/autonomo, ecc.) che mi serve per sciogliere nelle conclusioni il nodo
   "log vs partitura".

VINCOLI
- Cita SOLO ciò che è realmente nei PDF (niente riferimenti a memoria o inventati:
  riporta il file e la pagina da cui prendi il claim).
- Double-blind: segnalami se qualche candidato è plausibilmente mio/identificante,
  così decido se citarlo o no.
- Output: una tabella di posizionamento + un paragrafo di sintesi (5–7 righe) pronto
  da fondere nello "stato dell'arte".
```

---

## Note d'uso

- I prompt vanno usati **in sequenza**, in conversazioni separate o con conferma in mezzo:
  il vincolo "NON scrivere ancora" del Prompt 1 evita la fuga in avanti verso la prosa finale.
- Il **Prompt 3 presuppone i PDF già in una cartella locale**: l'estrazione "con file e pagina"
  blinda contro le citazioni inventate (il rischio numero uno con i proceedings). Se i PDF non
  sono scaricabili facilmente, si può usare la ricerca accademica integrata, ma allora la
  verifica fonte-per-fonte va fatta a mano.
- **TENOR copre l'asse A, non l'asse B** — per i linguaggi/DSL servono comunque fonti diverse.

> Possibile **quarto prompt** dedicato all'aggancio al tema *posthuman* (review §4.4: il legame
> più debole e più premiante da esplicitare). Da aggiungere se utile.
