# Deviazione per grano: ampiezza × probabilità — il quadrato 2×2

Concept page della **prima proposta del paper** («tradizione» (sezione rimossa, confluita in `sec:conclusioni`)), nel suo nucleo
argomentativo esposto in `sec:deviazione`. Documenta il framing del quadrato 2×2 e
la verifica di non-precedenza del gate (2026-06-11/12).

## Definizione

PGE fattorizza la deviazione per grano in **due assi indipendenti**, entrambi
componibili come envelope:

1. **Ampiezza** (*quanto* un grano può deviare): il range attorno alla traiettoria
   centrale, campionato in modo indipendente per grano (uniforme, centro ± range/2;
   gaussiana selezionabile). È la tendency mask classica (cfr. [[tendency-mask]]).
2. **Probabilità** (*se* la deviazione avviene): un gate Bernoulli per grano —
   la chiave `deviation_probability` — che decide grano per grano se la maschera si applica.
   Gate chiuso → il grano resta sulla traiettoria centrale; gate aperto → il grano
   devia sull'intera banda dichiarata.

## Il quadrato 2×2

| | senza `deviation_probability` | con `deviation_probability` |
|---|---|---|
| **senza range** | envelope puro: regime interamente scritto (`sec:pointer`) | micromodulazione implicita: deviazioni minime di sistema, decorrelazione alla Vaggione |
| **con range** | maschera Truax classica: tutti i grani deviano, banda che si deforma (gemello A, stream `mask_range`) | maschera *gated*: popolazione mista fedeli/devianti componibile nel tempo (gemello B, stream `mask_probability`) |

- **Gemello A** (`sec:deviazione`): envelope sull'ampiezza, gate sempre aperto —
  morfologia a **cuneo a riempimento uniforme**: nessun grano resta sulla linea
  centrale.
- **Gemello B**: ampiezza fissa, envelope sulla probabilità — la **linea centrale
  persiste** mentre una popolazione crescente la abbandona saltando da subito
  sull'intera banda. Non un allargamento ma una **mistura bimodale**.
- **Quarto angolo** (deviation_probability senza range): il gate apre deviazioni implicite di
  entità minima definite dal sistema — valori correnti circa ±1,5 dB sul volume,
  ±15° sul pan, ±5 ms sulla durata, ±5% del buffer sulla lettura (da aggiornare se
  i default cambiano: issue pitch in corso). Micromodulazione che non disegna
  alcuna traiettoria ma decorrela la massa grano per grano, nei termini della
  *décorrélation microtemporelle* di [[vaggione2002]]; da sola scioglie il ronzio
  del congelamento (cfr. [[time-stretching-granulare]], caso limite s=0).

## Verifica di non-precedenza del gate (2026-06-11/12, integrata 2026-08-26)

La rivendicazione del paper è **circoscritta**. Formulazione scritta in
`sec:deviazione` dal 2026-08-26: «per quanto mi risulta, non ha precedente
diretto **come asse dichiarabile e componibile nel tempo**» — i due attributi
(probabilità scritta nella specifica, variabile nel corso del brano) sono ciò
che regge, non il meccanismo in sé. Registro epistemico di questa pagina:
**non abbiamo trovato**, mai "non esiste". Candidati-controesempio esaminati:

### CMask (Bartetzki 1997) — il vicino più prossimo fuori CIM
Fonte primaria letta integralmente (cfr. [[bartetzki1997]]). Due esiti:

1. **Il valore è sempre estratto dalla maschera**: ogni evento passa per il mapping
   {0,1}→bordi; non esiste un parametro che decida *se* l'evento devii dalla
   traiettoria (la traiettoria centrale, come oggetto distinto dalla banda, non è
   nemmeno un'entità del modello — c'è solo la banda).
2. **Il quantizer ha una `strength`, ma è un blend continuo**: «The strength is a
   kind of attraction. 0% means no quantization at all. 50% means that every random
   number is attracted to the half distance between this random value and the next
   grid value.» La strength è envelope-abile come il deviation_probability di PGE, ma deforma
   **ogni** valore in proporzione — non decide per-evento se applicare o no.

### ICMS (Di Scipio/Tisato 1993) — il vicino più prossimo dentro CIM
I *phase-level switches* di ICMS (reverse, repetitions, offset, inversion) hanno
attivazione 50%-probabilistica per evento (cfr. [[discipio-tisato1993]], vettore e):
è un meccanismo Bernoulli per-evento documentato in tradizione CIM. Distinzioni:
la probabilità è **fissa** (50%, non dichiarabile né envelope-abile) e governa
**switch discreti di trasformazione** (inversione di fase, lettura retrograda),
non l'applicazione della deviazione di maschera a un parametro continuo. È il
precursore concettuale del gate, non il gate come asse dichiarativo.

### EmissionControl2 (Roads et al. 2021) — il vicino più prossimo per *forma*
Aggiunto al registro il 2026-08-26: la verifica 06-11/12 non lo aveva esaminato,
ed è la lacuna più grave che la review interna abbia trovato — EC2 è il sistema
più recente e visibile del campo, su CMJ, degli autori che con ogni probabilità
arbitrano l'area. La chiave `Intermittency` **è** un gate Bernoulli per grano,
dichiarabile e modulabile con continuità (i 15 parametri EC2 sono tutti
assegnabili a uno dei sei LFO): «*The intermittency control sets the probability
that a tick will not occur*» (Scheduler, p. 28); «*increasing the probability of
masking a grain (the grain will not sound)*» (Sound Example 9b, p. 38).

**La distinzione è nell'oggetto del gate, non nella sua forma.** EC2 gatta
l'**esistenza** del grano: gate chiuso → il grano non suona → la densità cala
(«*Intermittency results in a loss of grains (decrease in density)*», didascalia
Fig. 6). Il gate PGE lascia esistere il grano e decide se applicargli la
**deviazione**: la densità resta quella dichiarata, cambia la proporzione fra
popolazione fedele e popolazione deviante. Conseguenza morfologica leggibile
nella map e usata nel paper come controfattuale verificabile: la linea centrale
resta popolata mentre la nuvola cresce, dove un gate sull'emissione l'avrebbe
diradata.

Nota di metodo: EC2 era già ingestito ([[roads2021]]) e già censito in
[[graphic-score]] per lo Scan Display, ma non era stato interrogato come
candidato-controesempio *del gate*. Una fonte ingestita per un contributo non è
verificata per gli altri.

### AC Toolbox (Berg) — selezione dalla maschera via beta
La tendency mask di AC Toolbox sceglie l'elemento dalla maschera secondo una
funzione beta (parametri A, B della specifica `(N A1 A2 Z1 Z2 A B)`): la forma
della distribuzione è controllabile, ma la selezione resta **dalla maschera per
ogni evento** — non trovato un gate di probabilità per-evento come parametro di
prima classe del modello di maschera. (Verifica su documentazione web; il manuale
completo non è stato letto integralmente.)

### Common Music (Taube) — gate costruibile come idioma
Ambiente Lisp con primitive stocastiche (es. scelta pesata/`odds`): un gate
per-evento è **costruibile come idioma** (condizionale con probabilità p fra
valore centrale e valore deviato), ma non è parametro di prima classe del modello
di pattern/maschera. È la formulazione usata dal paper: «negli ambienti Lisp un
gate è costruibile come idioma ma non è parametro di prima classe del modello».

### La distinzione che regge la proposta
Due assi, non uno. Il primo separa il gate dai *blend continui*; il secondo — reso
necessario da EC2, che un gate Bernoulli ce l'ha — separa i gate per **oggetto**:
gate sull'**emissione** del grano (EC2 `Intermittency`: cambia la densità) contro
gate sull'**applicazione della deviazione** (PGE `deviation_probability`: densità
invariata, popolazione bimodale). Il primo asse da solo non discrimina più.

**Blend continuo** (CMask strength, mapping esponenziale, beta shaping): ogni
evento riceve una deformazione parziale; la popolazione resta **unimodale**, la
linea centrale non sopravvive come popolazione distinta.
**Gate Bernoulli per grano** (PGE `deviation_probability`): ogni grano o devia per intero o
resta esattamente sul centro; la probabilità è dichiarabile e componibile come
envelope; la popolazione è una **mistura bimodale** la cui proporzione evolve nel
tempo. La conseguenza morfologica è leggibile nella map: solo il gate produce
la linea centrale persistente con popolazione migrante del gemello B. Questa
distinzione rende la rivendicazione più solida, non più debole: il vicino esiste
ed è nominato, la differenza è strutturale.

## Collegamento alla tesi centrale
È il cuore della prima proposta («tradizione» (sezione rimossa, confluita in `sec:conclusioni`)): dentro un modello di controllo
ereditato (tendency mask Truax, nomenclatura canonica CIM 1993–95), PGE aggiunge
un asse dichiarativo. La leggibilità delle due morfologie nella map
(`sec:architettura`) è ciò che rende l'asse *verificabile* nel ciclo
scrivi–renderizza–ascolta.

## Citabilità nel paper
- **`sec:deviazione`** (primaria): i due gemelli, il quadrato 2×2, la
  micromodulazione come quarto angolo.
- **`sec:deviazione`**, dal 2026-08-26: il paragrafo di dimensionamento dopo
  `eq:gated` nomina due precursori — switch ICMS
  (`\cite{DiScipioTisato1993cim}`: probabilità fissa, switch discreti) e
  `Intermittency` EC2 (`\cite{Roads2021}`: gate sull'emissione). CMask e gli
  ambienti Lisp restano fuori dal paper per spazio: la verifica vive qui.

## Fonti
- [[bartetzki1997]] — CMask: maschera obbligatoria, quantizer strength continua
- [[roads2021]] — EC2 `Intermittency`: gate Bernoulli per grano sull'emissione
- [[discipio-tisato1993]] — phase-level switches 50% (precursore concettuale CIM)
- [[tendency-mask]] — il modello di base (asse ampiezza)
- [[truax1988]] — tendency mask originaria
- [[vaggione2002]] — décorrélation microtemporelle (quarto angolo)
- [[time-stretching-granulare]] — ronzio del freeze che la micromodulazione scioglie

## Domande aperte
- Release successive di CMask (port OSX di Kozar) introducono campi nuovi? Non
  verificato; la verifica copre articolo 03/1997 + manuale 07/1997.
- Selection principles di Koenig (PR1/PR2): lineage pre-Truax della maschera già
  segnalato in [[tendency-mask]] come non ingestito; vale anche per l'eventuale
  preistoria di meccanismi probabilistici per-evento.
- AC Toolbox: lettura integrale del manuale (non solo documentazione web) se la
  rivendicazione dovesse essere contestata in review.
- Altri sistemi già ingestiti per *altri* contributi e mai interrogati come
  candidati-controesempio del gate (la lacuna EC2 era di questa specie):
  [[caires2004]], [[valle-lombardo2003]], [[lopez1998]], [[sparano2018]].
  Da passare in rassegna prima della consegna del 31 agosto 2026.
