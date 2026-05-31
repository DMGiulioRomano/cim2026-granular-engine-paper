# Referee report

**Paper.** «Un ambiente Python per la sintesi granulare in tempo differito: controllo
parametrico esplicito e partitura come retroazione» (submission anonimizzata, CIM 2026,
comunicazione orale).
**Revisione.** Critica, referenziale, tracciabile. I rilievi rimandano a sezione, figura
o riga di `paper.tex` (commit `b9f75b0`). Audit bibliografico in `references_audit.md`;
materiale di correzione in `figure_walkthrough.md`; revisioni numerate in
`revision_checklist.md`.

---

## 1. Giudizio complessivo

Il paper è comprensibile per uno specialista e ben costruito: dietro c'è ingegneria
reale, non una descrizione di facciata. È **compatto e denso, non superficiale** — la
costruzione bottom-up (grano → stream → IR → renderer, poi tradizione, poi implicazioni)
regge e l'apparato storico-bibliografico è accurato e verificato. Porta due contributi
genuini: (a) una **postura compositiva sul tempo differito** ancorata con precisione a
Risset 1999, non nostalgica ma argomentata; (b) una **partitura grafica diagnostica** il
cui asse verticale è la posizione di lettura nel buffer e il cui flusso è invertito
(output del rendering, non input di controllo) — categoria distinta da tutto il panorama
storico. Le debolezze, in ordine di gravità: una **questione di categoria** — il sistema fa
*granulazione*/*micromontage* di campioni, non sintesi granulare in senso stretto, ma
titolo, abstract e §1 lo chiamano «sintesi granulare» mentre il corpo si riconosce già come
*granular sampling*; il testo **dice il suono ma non lo mostra** (asse esperienziale); la
**tesi centrale è asserita, non dimostrata** (manca ogni valutazione/caso); il
**posizionamento della partitura** ha una lacuna (Vocem, EC2) e una frase incoerente con la
propria tabella. Sono tutte risolvibili senza ristrutturare il paper, in larga parte
facendo parlare un artefatto già presente — la figura della partitura — oggi
sottoutilizzato.

**Nota di calibrazione.** Una critica plausibile a priori — «overclaim sull'asse Y» —
**non regge** alla lettura della figura: la rappresentazione è davvero di categoria diversa
dai precursori. Il rilievo è ritirato; resta solo la questione di posizionamento (§6).

---

## 2. Punti di forza

Il problema è ben posto: la sintesi granulare richiede di specificare migliaia di grani al
secondo, e già la prima implementazione computer lo segnala come intrattabile (§1, righe
122–126, `Roads1978`); il sistema mette al centro il **controllo parametrico esplicito e
leggibile**, non l'ennesimo motore di sintesi. L'architettura è coerente e motivata:
`Grain` immutabile (`frozen`+`slots`), una `GrainClipStrategy` come **unica fonte di verità**
sui grani che esistono (§2, righe 328–330), il layer di rendering dietro `AudioRenderer`
secondo l'Open-Closed Principle (righe 378–383), la cache SHA-256 per-stream come
precondizione del ciclo modifica→riascolto (righe 395–400). La genealogia italiana CIM è
accurata e, dove ho verificato, le citazioni reggono *verbatim* (Truax 1988 p. 14 e p. 23,
Risset 1999 p. 37: cfr. `references_audit.md`). Due distinzioni tecniche sono reali e ben
spese: `density`/`fill_factor` come due intenzioni diverse sullo stesso inter-onset time
(righe 274–281) e l'inviluppo che **unifica macro-forma e micro-modulazione** come sola
questione di scala dei breakpoint (righe 300–306). L'eredità della *tendency mask* di Truax
è dichiarata con onestà storica — modello di controllo adottato, postura sul tempo reale
no (righe 540–542). Il Language Server come *scaffolding* del primo anello del loop (la
scrittura della specifica, righe 411–424) è un'osservazione non banale.

---

## 3. Debolezza 1 — Categoria del sistema: granulazione/micromontage, non sintesi granulare in senso stretto

Di **sostanza**, e la più fondamentale perché tocca il titolo. Il sistema non sintetizza
grani da una primitiva (oscillatore/forma d'onda alla Gabor): **granula campioni**. Il YAML
dichiara un `sample` (es. `voce.aif`, §2 riga 233); il `PointerController` determina *dove
la testina legge nel sample* (§2 righe 318–320); ogni grano è un segmento finestrato di
materiale registrato. Nella tassonomia di Roads (*Microsound*, cap. 5) e nella distinzione
di Lippe questo è **granulazione di campioni** / *granular sampling*; e, per l'assemblaggio
algoritmico via DSL di micro-eventi da campioni, **micromontage** (Roads 2001 cap. 5,
*micromontage by algorithmic process*; cfr. Vaggione, *Tar*, e IRIN di Caires).

Il paper lo sa, ma **a metà**: §3 (righe 448–452) e §4 (righe 567–568) si riconoscono
correttamente come *granular sampling* «a cui questo lavoro appartiene». Ma **titolo**
(righe 73–74), **abstract** («deferred-time granular synthesis», riga 93) e **§1** (righe
116–117, 120: «La sintesi granulare costruisce il suono come collezione di migliaia di
grani») dicono *sintesi granulare*. È un'incoerenza interna, e un'imprecisione di categoria
proprio nella testata, dove pesa di più: un referee della tradizione granulare la nota
subito.

La conseguenza tocca anche la narrazione: §4 fonda il sistema sul paradigma Gabor (matrice
di quanti **sintetici**, righe 505–509), ma il sistema vive nel ramo
granulazione/micromontage — che da Gabor eredita la grana temporale, non il metodo di
produzione del grano. La genealogia propria del sistema passa più per Roads cap. 5
(granulazione/micromontage), Lippe (granular sampling) e Vaggione/Caires (micromontage) che
per la sintesi-di-grani.

**Fix.** Rendere la categoria precisa e coerente. Minimo: allineare titolo, abstract e §1 al
corpo (granulazione / *granular sampling*) e dichiarare esplicitamente in §1 la collocazione
tassonomica — *sintesi granulare* come paradigma-ombrello, il sistema come
**granulazione/micromontage di campioni**. Sul titolo c'è un trade-off da decidere: «sintesi
granulare» è il termine-ombrello riconoscibile e cercabile; «granulazione»/«micromontage» è
preciso ma meno standard come keyword. La scelta è dell'autore — ma l'incoerenza
titolo↔corpo va comunque rimossa.

---

## 4. Debolezza 2 — Asse esperienziale (*tells, not shows*)

Difetto di **sostanza**. Il testo nomina i meccanismi con precisione ma non dice quasi mai
cosa producono all'ascolto. I concetti introdotti-ma-non-mostrati:

- **`distribution` 0→1** (§2, righe 313–316): definito come blend sincrono↔asincrono, mai
  detto cosa cambia all'orecchio passando da metronomo perfetto a campionamento uniforme.
- **finestra di loop statica vs mobile** (§2, righe 319–320): citata come capacità del
  `PointerController`, mai interpretata musicalmente.
- **multi-voce `stochastic` vs `chord`** (§2, Tab.~\ref{tab:voci}, riga 343): la differenza
  percettiva tra le strategie non è mai resa.
- gli **esempi YAML** (stream `clouds`, densità in accelerando, `voices`) sono **sintattici**:
  mostrano la forma del DSL, mai l'esito sonoro che la giustifica.

A ciò si aggiunge la densità di alcune frasi senza stadio operativo intermedio — es. «Gate
e range sono ortogonali: il valore fissa l'intenzione, l'inviluppo la generalizza nel
tempo, il gate sceglie dove…» (righe 259–265): esatta, ma da rileggere due volte.

**Fix.** L'antidoto è già nel paper ma inerte: la **figura della partitura**
(Fig.~\ref{fig:score}) è inclusa **senza una sola riga che la legga**. Una lettura guidata
in prosa (nuvola larga = deviazione del pointer alta → diagonale nitida = deviazione che si
stringe; banda discendente = lettura retrograda lenta; colore = pan) trasforma la figura
muta nell'esempio lavorato che manca, e àncora i meccanismi astratti a un esito visibile.
Bozza pronta in `figure_walkthrough.md` (Parte 1). In aggiunta, **almeno un esempio YAML
interpretato musicalmente** («questa specifica produce…»).

---

## 5. Debolezza 3 — Assenza di valutazione

Anche questo di **sostanza**. La tesi centrale — il differito abilita un loop di feedback
lungo come postura compositiva (§5, righe 580–598) — è **asserita ma mai dimostrata**. Manca
ogni evidenza: nessun caso studio, nessun brano, nessuna iterazione del loop in cui la
partitura riveli uno scarto poi corretto. Il loop lungo è descritto come meccanismo, non
mostrato in azione. I dati di performance sono vaghi: «il tempo di build completa è
dell'ordine dei minuti» (§2, riga 400), senza grani/s, footprint di memoria, né un tempo di
build misurato.

**Fix.** Il minimo indispensabile, compatibile con il limite di pagine:
1. **un micro-workflow** idea → YAML → grani → partitura → esito sonoro atteso, anche
   breve, che esibisca un giro del loop;
2. **un episodio diagnostico** — la partitura mostra X, corretto in Y (template in
   `figure_walkthrough.md`, Parte 1; **da riempire con un caso vero**, non inventato);
3. **due o tre numeri** di performance (grani/s, picco di memoria, tempo di build su un
   brano di riferimento).
La debolezza 2 e la 3 si chiudono in larga parte con lo **stesso gesto**: far parlare la
figura già presente.

---

## 6. Debolezza 4 — Posizionamento della partitura

Di **sostanza** ma circoscritta. Tre punti, due dei quali verificati su fonte primaria.

- **Vocem come *foil* mancante.** Vocem (López, Martí, Resina, *Proc. DAFx-98*, 1998 —
  ora in `refs.bib`, chiave `Lopez1998`) è l'**unico** precedente che usa lo stesso asse Y
  (posizione nel file sorgente). Verificato sul PDF: lì quell'asse ospita una **singola
  curva di controllo disegnata in input** (parametro *offset*, Fig. 2), in tempo reale, e
  **non** plotta i grani, **non** mostra la deviazione, **non** àncora l'asse alla forma
  d'onda. È il contrasto che rende esplicito il differenziatore di questo sistema —
  l'inversione di flusso, dalla curva-input alla popolazione-output. Citarlo **rafforza** il
  paper. Testo e riga di tabella pronti in `figure_walkthrough.md` (2.1).
- **EmissionControl2 da nominare.** L'ambiente granulare-con-visualizzazione contemporaneo
  di riferimento (Roads, Kilgore, DuPlessis, CMJ 2021 — `Roads2021`, già in `refs.bib` ma
  mai citato) ha uno *Scan Display* real-time. È il polo rispetto a cui si definisce la
  scelta del differito; oggi è assente. Blocco pronto in `figure_walkthrough.md` (2.2).
- **Frase «frequenza convenzionale» incoerente.** «il verticale codifica la posizione di
  lettura […] dove le rappresentazioni convenzionali del controllo granulare collocano la
  frequenza» (§3, righe 434–436) **contraddice la Tab.~\ref{tab:repr} dello stesso
  paragrafo**, che elenca Truax = parametro/mask e GeoGraphy = mappa spaziale: nessuno dei
  due è frequenza. Riscrittura concordante con la tabella in `figure_walkthrough.md` (2.3).

Va ribadito (cfr. §1): la critica «overclaim sull'asse Y» **non si applica** — la categoria
è genuinamente nuova. Qui si tratta solo di chiudere il giro del confronto.

---

## 7. Stile (forma)

Registro continentale alto, chiuse aforistiche, triadi bilanciate. Funziona per il pubblico
CIM, ma a tratti la densità filosofica sovrasta la descrizione tecnica e rischia il lettore
interdisciplinare. Esempi: «una configurazione operativa di cui il sistema è insieme
strumento e argomento» (§5, righe 627–628); la frase sull'ortogonalità gate/range (§2, righe
259–265). **Raccomandazione (P3):** dopo i nodi teorici più densi, una **frase di mediazione**
che riporti a terra il concetto con un esempio o una conseguenza concreta; alleggerire una o
due chiuse aforistiche. Non è un difetto di sostanza — non sovra-correggere: la voce del
paper è un suo pregio.

*(Nota laterale, non un'accusa.)* La prosa porta marcatori di rifinitura LLM (triadi,
aforismi), ma la sostanza — citazioni accurate con numeri di pagina, architettura coerente —
indica un autore umano competente. Il *detection* stilistico è inaffidabile: irrilevante ai
fini della valutazione.

---

## 8. Raccomandazione

**Accept with revisions.** Le quattro debolezze sono di contenuto ma **tutte risolvibili
entro l'attuale impianto e il limite di pagine**. La più fondamentale — la categoria
(granulazione/micromontage vs sintesi granulare) — si chiude allineando testata e corpo. Le
altre, in larga parte facendo parlare un artefatto già incluso (la partitura). Nessuna
ristrutturazione richiesta; le aggiunte P1 alzano il paper da «descrizione competente di un
sistema» a «dimostrazione della sua tesi».

---

## 9. Revisioni azionabili

Lista numerata con priorità in **`revision_checklist.md`**. Sintesi delle P1 (bloccanti per
il miglioramento): risolvere la categoria del sistema (titolo/abstract/§1 vs corpo); far
leggere la partitura in prosa; aggiungere ≥1 esempio YAML con esito sonoro; citare Vocem
come foil e correggere la frase «frequenza».
