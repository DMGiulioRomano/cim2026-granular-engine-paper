# Prompt per la conclusione — paper DIRAC (CIM2026)

Materiale di supporto per scrivere la **conclusione** del paper
*"Un ambiente Python per l'elaborazione granulare: dal codice alla partitura
grafica"* (sistema: **DIRAC**). Gemello del file `prompt-introduzione-CIM2026.md`.
Basato sulla peer review (§9) e sullo **stato corrente** del paper
(`paper/sections/2*.tex` + `wiki/overview.md`), non sulle bozze stale.

---

## Premessa: la conclusione di questo paper NON è un recap

La review §9 dà consigli da *system-paper* generico (limiti, lavori futuri). Ma è stata scritta **senza vedere la
chiusura**: nel PDF recensito le sezioni di chiusura erano `%\input`
commentate. La chiusura reale di questo paper è la sezione delle
**implicazioni** — l'argomento del tempo differito. Quindi il §9 va usato come **checklist di ciò che
un revisore cercherà**, da incorporare nella chiusura, non come la sua
struttura.

Tre fatti che cambiano *come* si scrive:

1. **La chiusura è già una tesi, non un riassunto.** Forma: obiezione nella
   sua versione più forte (tutto girerebbe in real-time su un laptop) → Risset
   (precedente filosofico del ritorno volontario) → Vaggione (teoria positiva:
   interazione come triangolo input/output/operatore, non come latenza;
   *déclaration d'attribut généralisé*) → le **tre proposte** come conseguenze
   della postura → il **costo** detto con franchezza. Il "loop lungo"
   (specifica → generazione → ascolto → riscrittura) entra **come esito, non
   come bandiera**.
2. **Il nodo log/partitura è già piantato nel corpo.** `sec:architettura`
   definisce la MAP come *«una mappa [...] non un registro che scorre nel
   tempo, ma una vista sinottica»*. La tesi "mappa sinottica, né log né
   partitura" è già nel testo: la conclusione la **atterra**, non la deriva.
   La review §4.5 ("MAP mai definita") e §4.3 ("log vs partitura") sono già in
   parte assorbite dal corpo: alla chiusura resta il *landing*, non la
   definizione.

### Cosa tenere del materiale stale
- Vecchio `50-implicazioni.tex`: **butta la prosa**. La *direzione* (obiezione →
  Risset → Vaggione → conseguenze → costo) coincide con la tesi corrente: lo
  scheletro si riusa, le frasi no. Ricostruire sul corpo attuale e sui nomi
  DIRAC/MAP.

---

## Vincoli (dal repo — non negoziabili)

Da mettere in testa a ogni prompt, perché la chat che scrive non li violi:

- **Tempo differito = implicazione argomentata in chiusura**, non premessa
  identitaria. Arriva come risposta a una possibile obiezione, non come dichiarazione di
  fede.
- **FORMULAZIONE VIETATA**: mai «real-time come cambio di paradigma» / «rompe
  il vincolo». Il non-determinismo di Truax 1988 è **economia di mezzi**, non
  cambio di paradigma compositivo. (correzione vincolante del maestro, ripetuta)
- **Mai «è meglio fare così»**: la postura è personale e situata, non
  prescrittiva.
- **Il costo NON è una roadmap travestita.** Performance, gesto, strumento sono
  rinunce deliberate e argomentate, non voci di "lavori futuri".
- **Lessico di dominio, non nomi di classe**: testina / posizione di lettura,
  griglia / densità, le voci, gate di probabilità (`dephase`), partitura
  grafica / MAP, cache per stream. Le chiavi YAML (`speed_ratio`, `dephase`,
  `scatter`, `distribution`) sono ammesse: sono la notazione.
- **Italiano. No emoji, no emoticon.**
- **Double-blind**: nomi DIRAC/MAP; prima persona sul **metodo**, mai sulla
  biografia; attenzione al *clustering* di auto-citazioni identificanti (la
  review §5 segnala la prossimità a Di Scipio/Tisato come rischio di
  de-anonimizzazione in ambito CIM).
- **6–8 pagine, due colonne**: la chiusura è stretta. Stimare le lunghezze.

---

## I prompt (in sequenza, conversazioni separate)

Stessa logica del file-intro: ragionare sulla struttura e scrivere sono compiti
diversi; mescolarli fa saltare al testo finale senza pensare. Il vincolo «NON
scrivere ancora» del Prompt 1 evita la fuga in avanti.

> **★ Insight**
> La conclusione di questo paper si gioca su un equilibrio: deve **chiudere un
> argomento** (il differito) e insieme **soddisfare un revisore** che cerca
> limiti e collocazione. Il rischio non è "poche cose" ma il **tono**: se la
> chiusura scivola in checklist (limiti elencati, lavori futuri promessi),
> uccide la postura situata che regge il resto del paper. Ogni elemento della
> review va *fuso* nell'argomento, non appiccicato in coda.

---

### Prompt 1 — Ragionare sulla struttura della chiusura (NON scrivere)

```
Sei un assistente alla scrittura accademica. NON scrivere ancora la conclusione:
in questo passaggio RAGIONA solo sulla sua struttura e propommi un'ossatura
commentata che approverò prima della stesura.

CONTESTO
- Paper per il XXV CIM. Sistema: DIRAC (Declarative Intermediate Representation
  for Audio Composition), ambiente Python per la granulazione di materiale
  campionato: DSL dichiarativo in YAML -> rappresentazione intermedia (IR)
  ancora dichiarativa e interrogabile -> materializzazione differita grano per
  grano. La MAP (Multiparametric Audio Plot) e' una vista sinottica read-only
  del rendering.
- La chiusura del paper e' la sezione delle IMPLICAZIONI: il tempo differito
  mentre il real-time e' disponibile. NON e' un riassunto.
- Il corpo (sec:architettura) e' completo ed espone il sistema per scostamenti
  dalla trasformazione identica. La tesi corrente e' in wiki/overview.md.
- IMPORTANTE: ignora le bozze in paper/sections/40-*.tex e 50-*.tex: sono stale
  (versioni vecchie). Basati sul corpo attuale 2*.tex.

ARGOMENTO DELLA CHIUSURA
Obiezione nella forma piu' forte (tutto girerebbe in real-time su un laptop) ->
Risset (precedente filosofico del ritorno volontario al differito) -> Vaggione
(interazione come triangolo input/output/operatore, non come latenza;
declaration d'attribut generalise: scrittura e algoritmo si imbricano) -> le tre
proposte come CONSEGUENZE della postura, non come dotazioni:
  (1) YAML come notazione + il gate ampiezza x probabilita' (dephase);
  (2) partitura grafica con asse Y = posizione di lettura, output read-only;
  (3) workflow per stem: cache incrementale + export DAW.
-> il COSTO detto con franchezza: performance, gesto, strumento (rinunce
   deliberate, NON una roadmap). Il loop lungo entra come esito, non bandiera.

DA INCORPORARE (checklist della peer review, fusa nell'argomento, non in coda)
- LIMITI ibridi: tieni il costo gia' argomentato, aggiungi un beat onesto e
  breve (la MAP codifica il pitch col colore -> accessibilita'; nessuna
  valutazione formale/con utenti; offline per scelta) + 1-2 direzioni davvero
  possedute. NIENTE tono da roadmap, niente "lavori futuri" come lista.
- Availability statement anonimo (repo / DOI Zenodo): dove collocarlo.

VINCOLI
- Tempo differito come implicazione argomentata, mai premessa identitaria.
- VIETATO "real-time come cambio di paradigma" / "rompe il vincolo": il
  non-determinismo di Truax e' economia di mezzi.
- Mai "e' meglio fare cosi'": postura personale e situata.
- Lessico di dominio, non nomi di classe. Italiano, no emoji.
- Double-blind: prima persona sul metodo, non sulla biografia.

COSA VOGLIO DA TE ORA
- Una scaletta della chiusura in 4-6 paragrafi: per ciascuno (i) la funzione
  retorica, (ii) la frase-cardine che lo apre, (iii) quali citazioni/concetti
  vanno li'.
- Segnala dove rischia di diventare (a) un recap generico, (b) una roadmap
  travestita, (c) una checklist appiccicata.
- Stima la lunghezza per paragrafo (6-8 pagine, chiusura stretta).
- Fammi 2-3 domande se qualcosa e' ambiguo. NON scrivere prosa finale.
```

---

### Prompt 2 — Stress-test della scaletta (il "secondo cervello")

```
Ora fai il revisore scettico della scaletta che hai appena prodotto.

Per ogni paragrafo chiediti:
- L'argomento del differito e' GUADAGNATO (ancorato a un fenomeno mostrato nel
  corpo) o solo AFFERMATO? Dove dico "scelgo il differito" senza dire "contro
  quale obiezione e con quale guadagno"?
- Il COSTO e' onesto o e' una roadmap travestita? (la rinuncia a
  performance/gesto/strumento e' una scelta argomentata, non una voce di lavori
  futuri.)
- Il beat dei LIMITI appiattisce la postura situata in una checklist? Si puo'
  fondere nell'argomento invece di elencarlo?
- L'atterraggio della MAP e' coerente con come il corpo l'ha gia' definita
  (vista sinottica, non un registro che scorre)? Sto ri-derivando qualcosa di
  gia' detto?
- C'e' da qualche parte la formulazione vietata ("real-time come cambio di
  paradigma" / "rompe il vincolo")? un "e' meglio cosi'"?
- Sto duplicando il posizionamento sulla notazione che fa gia' l'introduzione,
  invece di limitarmi ad atterrarlo qui?

Riscrivi la scaletta correggendo i punti deboli. Evidenzia cosa hai cambiato e
perche'.
```

---

### Prompt 3 — Atterrare il nodo log / partitura / mappa (landing, non derivazione)

```
Mi serve la chiusura del nodo "log vs partitura". La posizione e' gia' ferma e
NON va riaperta: la MAP non e' un log (registro descrittivo che scorre,
post-hoc) ne' una partitura prescrittiva (letta ex-ante da un esecutore); e' una
MAPPA, sinottica, output read-only del rendering.

CONTESTO
- Nel corpo la MAP e' gia' definita come "una mappa [...] non un registro che
  scorre nel tempo, ma una vista sinottica".
- L'introduzione imposta il vocabolario della teoria della notazione
  (descrittivo / prescrittivo, alla Goodman; eventuale aggancio TENOR). La
  conclusione deve ATTERRARE cio' che l'intro IMPOSTA, senza ri-derivarlo e
  senza duplicarlo.

COSA FARE
1. Produci il passaggio di 2-4 frasi che atterra "mappa sinottica" nella
   chiusura, usando con precisione il lessico descrittivo/prescrittivo: dire
   cosa la MAP NON e' (log; partitura prescrittiva) e cosa E' (mappa sinottica
   read-only), e perche' questo e' la conseguenza naturale del tempo differito
   (l'intera specifica e' ispezionabile tutta insieme perche' non scorre in
   tempo reale).
2. Indica come questo passaggio si incastra con l'introduzione (cosa da' per
   gia' detto, cosa aggiunge) per evitare ridondanza.
3. Verifica che il lessico sia di dominio (partitura grafica / MAP, posizione di
   lettura), non nomi di classe.

VINCOLI: italiano, no emoji; double-blind; niente "e' meglio cosi'".
Output: il passaggio + una nota di coordinamento con l'intro.
```

---

### (opzionale) Prompt 4 — Limiti onesti + disponibilità, senza roadmap

Da usare solo se nel Prompt 1 decidi che limiti e direzioni meritano un
movimento distinto invece di essere fusi nei paragrafi del costo.

```
Scrivi il beat dei limiti in modo che NON diventi una lista di lavori futuri.

REGOLE
- Tieni il costo gia' argomentato (performance, gesto, strumento = rinuncia
  deliberata): NON ripeterlo come limite, richiamalo.
- Aggiungi limiti onesti e brevi, ciascuno con la sua direzione naturale ma
  senza promesse:
    * la MAP codifica il pitch col colore -> limite di accessibilita' (special
      topic della call); direzione: ridondanza non cromatica.
    * nessuna valutazione formale / studio di leggibilita' con compositori.
    * offline per scelta, non per mancanza: dirlo come postura, non come gap.
- Una sola frase, non una sezione, per l'availability statement anonimo
  (repo / DOI Zenodo).
- Tono: situato e franco, mai "in futuro implementeremo".

Output: il paragrafo (o i due paragrafi) + dove collocarli nella scaletta.
```

---

## Note d'uso

- I prompt vanno usati **in sequenza**, in conversazioni separate o con conferma
  in mezzo. Il «NON scrivere ancora» del Prompt 1 e' la diga contro la fuga
  verso la prosa.
- **Punta sempre la chat al materiale corrente**: `wiki/overview.md` (tesi) e
  `paper/sections/2*.tex` (corpo). Di' esplicitamente di **ignorare**
  `40-*.tex` e `50-*.tex` (stale), o la chat ricostruira' la muffa.
- **Coordinamento con l'introduzione**: il nodo notazione si imposta nell'intro
  e si atterra qui. Tieni i due testi davanti per non duplicare.
- **Dipendenza da `sec:partitura`**: se verra' scritta una sezione partitura
  autonoma, parte dell'atterraggio MAP potrebbe migrare li'; in tal caso la
  conclusione sintetizza, non ripete.
- Un eventuale **Prompt 5 di stesura finale** (scrivi la prosa definitiva, ~N
  parole per stare in 6-8 pp.) si aggiunge quando la scaletta e' approvata e i
  passaggi-chiave (MAP, limiti) sono pronti.

### Decisioni ancora aperte (da confermare prima della stesura)
1. **Una chiusura o due tempi?** La conclusione e' la sola sezione implicazioni
   rilavorata (argomento del differito con i must-have della review fusi
   dentro), oppure vuoi anche una breve coda separata di sintesi / sviluppi
   futuri (la "mezza pagina alla Truax", che CLAUDE.md lascia come decisione
   aperta)?
2. **La spina dorsale resta il differito?** `wiki/overview.md` dice di si'; se
   il paper e' cambiato anche su questo, va detto prima del Prompt 1.
