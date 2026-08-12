# Camera-ready CIM 2026 — piano di risposta alle review

**Esito:** accettato (comunicazione orale). R1 = 0 borderline, R2 = 2 accept.
**Review verbatim:** `raw/reviews/cim2026-reviews-round1.md` (immutabile).
**Scadenze:** camera-ready + registrazione (un form per autore per paper) **31 ago 2026**.
Oggi 12 ago → 19 giorni. Build-freeze interno **27 ago** (`make paper`, verifica ≤ 8 pagine).
**Obbligo del comitato:** lettera che dichiara cosa è stato recepito e, per ciò che non lo è,
la giustificazione. Questa lettera è il filtro delle righe `parziale` / `declina` della matrice.

**Vincolo duro:** il PDF è già a 8 pagine (cap). R1 chiede insieme di *tagliare* e di
*aggiungere* la specifica completa del linguaggio. I due non stanno entrambi: i tagli di
prosa finanziano al massimo una tabella-specifica compatta, altrimenti si declina con rinvio
alla documentazione del repo. Da decidere in D4.

---

## Decisioni preliminari (bloccano la riscrittura — chiuderle prima di scrivere)

| ID | Decisione | Opzioni | Note di vincolo |
|----|-----------|---------|-----------------|
| D1 | `dephase` → `deviation_probability` — **DECISA 2026-08-13: (b) rinominare nel paper e nel PGE** | (a) tenere la chiave, glossarla alla prima occorrenza («jitter probabilistico») e giustificare in lettera; (b) rinominare nel paper e nel PGE; (c) rinominare solo nel paper | Il nome non è `jitter`: nel PGE `jitter` nomina già l'ampiezza (`default_jitter`), e per `reverse` il gate è probabilità di flip booleano, senza alcun range. Né `deviation` secco: la deviazione è l'ombrello che si fattorizza in ampiezza × probabilità, e prendersi la parola cancellerebbe la fattorizzazione dal nome. Motivo del cambio: `dephase` è esatto solo nel modo micro (gate sui `default_jitter`) e fuorviante nel macro (gate su un `offset_range` esplicito, dove i grani saltano su un terzo del buffer); il parametro è una probabilità, quindi scale-free, e il vecchio nome si impegnava su una sola scala. Rilasciata in PGE **v7.0.0** (PGE #204), senza alias di retrocompatibilità; language server allineato (PGE-ls #40). Il pin del submodule sale da `v4.0.0-119` a `v7.0.0`, così la notazione pubblicata coincide col sistema scaricabile — l'opzione (c) era esclusa proprio da questo, visto che a D5 il repo viene linkato pubblicamente e chi clona prende HEAD. Risponde a R1.M5 / R1.D19 / R1.D24: accolta la sostanza (il nome ora dice probabilità), respinta la struttura (nidificare sotto `pointer` come `offset_probability` cancellerebbe la forma globale scalare — nei modi `GLOBAL`/`GLOBAL_ENV` il `param_key` è ignorato e la probabilità si applica a tutti i parametri), respinto il nome proposto |
| D2 | Sorte del differito in `sec:implicazioni` — **DECISA 2026-08-12: (a) restringere e concedere** | (a) restringere + concedere la distinzione motore/descrizione, tenendo solo la parte difendibile (la MAP come rappresentazione totale post-render); (b) tagliare (R1); (c) espandere la giustificazione (R2) | Concedere a R1.M2 che RT/DT è proprietà del motore, non della descrizione; tenere solo ciò che il differito abilita davvero. Risponde anche a R2.3 e libera spazio. Vincolo maestro: mai «real-time come cambio di paradigma» |
| D3 | Dove risponde l'obiezione «≈ patch Max/PD» | (a) in introduzione; (b) in `sec:tradizione`; (c) nel riquadro contributi | Determina la riscrittura dell'introduzione: farlo prima |
| D4 | Specifica completa del linguaggio — **DECISA 2026-08-12: (d) albero dentro un listato** | (a) tabella compatta; (b) rinvio a documentazione repo; (c) tabella + rinvio; **(d) albero della grammatica (AST/tree) reso come `lstlisting`** | Un albero indentato in `lstlisting` costa meno spazio di una tabella e mostra la ramificazione proprietà → sottoproprietà → dominio, che è esattamente ciò che R1.M6 chiede. Va generato dallo schema di validazione del PGE, non scritto a mano, per non divergere. Verificare l'ingombro reale prima di committarci: se sfora, ramo `(d) + rinvio al repo` per i parametri fuori dagli esempi |
| D5 | De-anonimizzazione | ripristinare autore/affiliazione/email, scommentare `\blfootnote` copyright, sostituire il link OSF anonimo con link pubblico (+ DOI Zenodo se si pubblica il bundle audio), decidere se citare il repo PGE per nome | Nulla nelle review lo ricorda: è l'errore facile da spedire. `paper.tex:8-26` |
| D6 | Rigenerazione figure/audio — **DECISA 2026-08-13: si rirende tutto**, di fatto già fatto | Fig. 2 va rifatta a densità bassa (R1.D11). Se si rirende, decidere se rirenderizzare anche l'audio del bundle | Il bump del submodule a v7.0.0 (#35) ha imposto la rigenerazione completa di esempi e audio: il motore è salito di due major, tenere figure rese da v4 le avrebbe fatte divergere dal codice citato. Resta da fare la sola densità di Fig. 2 → #36. Rendering stocastico: riproducibilità per andamento, non bit-identico |

---

## Matrice delle risposte

Classe: **A** = accetta · **P** = parziale · **D** = declina (con giustificazione in lettera).
Stato: ☐ da fare · ☑ fatto.

### R1 — osservazioni maggiori

| ID | Osservazione | Azione proposta | Classe | Dove | Stato |
|----|--------------|-----------------|--------|------|-------|
| R1.M1 | Novità sopravvalutata: il YAML equivale ai controlli di una patch Max/PD, egualmente dichiarativi e forse più efficaci; dire in quali contesti la notazione testuale conviene | Ridimensionare la rivendicazione; aggiungere risposta concreta (artefatto testuale persistente, diffabile e versionabile, validato in scrittura, IR interrogabile, un'unica specifica → audio *e* MAP); dichiarare i contesti d'uso | P | D3, intro + `sec:tradizione` | ☐ |
| R1.M2 | La discussione tempo reale/differito non serve: RT/DT è proprietà del *motore*, non della descrizione; il motore non è oggetto dell'articolo; solo la MAP è soggetta alla distinzione, e il suo status è sopravvalutato | Concedere la distinzione motore/descrizione (è corretta e rafforza il resto); ridurre la sezione alla sola parte difendibile | P | D2, `sec:implicazioni` | ☐ |
| R1.M3 | Prosa a tratti incomprensibile; elenco di locuzioni «parole in libertà»; semplificare a partire dall'introduzione | Riscrittura di chiarezza, una locuzione alla volta dalla lista verbatim | A | tutte | ☐ |
| R1.M4 | Listati sotto le figure corrispondenti | Riposizionare ogni `lstlisting` accanto alla propria figura | A | `20`–`27` | ☐ |
| R1.M5 | Ripensare e semplificare la terminologia | Vedi D1 — applicata: `dephase` → `deviation_probability` in paper e motore (#35, PGE v7.0.0) | P | D1 | ☑ |
| R1.M6 | Includere specifica completa del linguaggio (proprietà, sottoproprietà, valori) | Vedi D4 | P/D | D4 | ☐ |
| R1.M7 | Articolo troppo lungo per quello che propone | Tagli di prosa (finanziano lo spazio per D4 e per il riquadro contributi) | A | tutte | ☐ |
| R1.M8 | Equazioni e modelli probabilistici corretti ma inutili qui, «parte del fumo» | Tenere solo le formule che un'affermazione del testo usa davvero; le altre via | P | `24-deviazione` | ☐ |

### R1 — note dettagliate

| ID | Punto | Azione | Classe | Dove | Stato |
|----|-------|--------|--------|------|-------|
| R1.D1 | «queryable IR» non chiaro | Sciogliere per esteso | A | `00-abstract` | ☐ |
| R1.D2 | «distanza opaca»: perché dichiarativo, perché illeggibile | Riformulare con parametri concreti | A | `10-introduzione` | ☐ |
| R1.D3 | «ciò che una specifica testuale non mostra»: quale specifica? il testo può mostrare l'onset | Correggere la formulazione: il punto non è che il testo non possa dirlo, ma che l'esito per-grano non è leggibile nella specifica | A | `10-introduzione` | ☐ |
| R1.D4 | «Tre tradizioni…»: paragrafo in cui il lettore si perde | Riscrivere o eliminare | A | `10-introduzione` | ☐ |
| R1.D5 | SuperCollider «dichiara l'esito, non la procedura»: dubbio | Verificare e correggere o circostanziare | A | `10-introduzione` | ☐ |
| R1.D6 | Legenda «pitch (cents)» non usata in Fig. 1 | Dichiararlo in didascalia | A | `22-pointer` | ☐ |
| R1.D7 | Wrapping fine→inizio: buffer circolare? click? campioni a cavallo? | Esplicitare l'assunzione e cosa fa l'implementazione | A | `22-pointer` | ☐ |
| R1.D8 | Il verso di lettura cambia: perché, e non dovrebbe essere un parametro? | Spiegare il meccanismo; se è un limite, dirlo | A | `22-pointer` | ☐ |
| R1.D9 | «non visualizzabile con forma d'onda o sonogramma»: «è cinematica di base» | Ridimensionare la claim | P | `22-pointer` | ☐ |
| R1.D10 | Footnote 7 sembra un esponente; `fill_factor` = overlap va nel corpo | Spaziatura nota + overlap nel testo | A | `23-griglia` | ☐ |
| R1.D11 | Fig. 2 illeggibile: serve densità molto più bassa; spostarla dopo | Rigenerare l'esempio a densità bassa (D6) e riposizionare | A | D6, `23-griglia` | ☐ |
| R1.D12 | IOT con soprallineatura → `IOT_avg` e spiegare | Cambiare notazione | A | `23-griglia` | ☐ |
| R1.D13 | Le istruzioni di lettura del grafico vanno in didascalia | Spostare in caption | A | `23-griglia` | ☐ |
| R1.D14 | Le affermazioni sullo spettro a righe chiedono figure spettrali | Se non c'è spazio per una figura spettrale: attenuare l'affermazione o citarla da letteratura | P | `23-griglia` | ☐ |
| R1.D15 | «Nel congelamento le due vie sono complementari»: congelamento di cosa? | Riscrivere | A | `23-griglia` | ☐ |
| R1.D16 | Listato 3 mai referenziato né commentato | Referenziare e commentare (o togliere) | A | `23-griglia` | ☐ |
| R1.D17 | «envelope» → «inviluppo» in tutto l'articolo | Sostituzione sistematica | A | tutte | ☐ |
| R1.D18 | Manca il numero della figura in «etichettati (a) e (b) nella figura» | Aggiungere `\ref` | A | `24-deviazione` | ☐ |
| R1.D19 | `dephase.pointer` fuorviante: è probabilità di spostamento dell'onset; meglio sotto `pointer` (es. `offset_probability`); implementazione «barocca» | Vedi D1; in ogni caso spiegare meglio il caso | P | D1, `24-deviazione` | ◐ nome accolto (`deviation_probability.pointer`), struttura respinta con motivazione in D1; resta il «spiegare meglio il caso» |
| R1.D20 | «non potrebbero essere più diverse» colloquiale; spiegazione floreale | Riscrivere piano | A | `24-deviazione` | ☐ |
| R1.D21 | Eq. 2: cos'è `v_n`? | Definire | A | `24-deviazione` | ☐ |
| R1.D22 | «(a) è questo modello all'opera» — con `c(τ_n)` costante | Precisare | A | `24-deviazione` | ☐ |
| R1.D23 | «due inviluppi ortogonali, (a) muove la prima a gate aperto…» non si capisce | Riscrivere | A | `24-deviazione` | ☐ |
| R1.D24 | `dephase` ≠ deviazione; considerare jitter | Vedi D1 — sostanza accolta, `jitter` respinto (nomina già l'ampiezza: `default_jitter`) | P | D1 | ☑ |
| R1.D25 | Fig. 4: l'andamento cubico 20–80% non si vede (sembra lineare a scalini); deviazione = 100 di cosa? | Verificare la figura contro il YAML; correggere didascalia e unità | A | `24-deviazione`, #36 | ◐ didascalia corretta: il revisore aveva ragione, l'esempio ha `type: step` e non `cubic` — corretti «cubico» → «a gradini» e «con continuità» → «per gradi». Resta l'unità: la legenda dice `ptr dev %` ma quella curva è la probabilità, non l'ampiezza (etichetta generata da `page_layout.py` del motore) → #36 |
| R1.D26 | Mid-Side/Blumlein superfluo; θ è azimuth astratto; perché non oltre la circonferenza unitaria | Ridurre a θ astratto, rinviare la realizzazione; dichiarare il limite stereo | P | `27-voci` | ☐ |
| R1.D27 | `pan_range`: jitter sul pan o apertura del fronte? nome cattivo; «come ogni parametro» non torna | Chiarire la semantica; uniformare il discorso su `*_range` | A | `27-voci` | ☐ |
| R1.D28 | «svolta nel volume 1993»: il real-time granulare è precedente (Riverrun 1986); riferimenti troppo centrati su CIM | Chiarire che la scansione è *negli atti CIM* (il testo già dice «negli atti»), non nella storia generale; ampliare la bibliografia extra-CIM. Attenzione: non riformulare in «real-time come cambio di paradigma» (vincolo maestro) | P | `40-tradizione` | ☐ |
| R1.D29 | «dove la specifica resta interrogabile»: casi concreti; cosa fa il YAML che gli oggetti Max non fanno | Rispondere con casi concreti (stessa risposta di R1.M1) | A | D3, `40-tradizione` | ☐ |
| R1.D30 | «asse dichiarativo continuo… Due casi la circoscrivono»: referente ignoto, paragrafo fumoso | Riscrivere | A | `40-tradizione` | ☐ |
| R1.D31 | «tiene il ritorno dell'ascolto abbastanza vicino alla scrittura…»: che vuol dire | Riscrivere piano | A | `50-conclusioni` | ☐ |

### R2

| ID | Punto | Azione | Classe | Dove | Stato |
|----|-------|--------|--------|------|-------|
| R2.1 | Utilità della MAP asserita, non valutata; negli esempi complessi la densità informativa diventa difficile da interpretare | Aggiungere due o tre righe di motivazione + ammettere il limite di leggibilità nei casi densi | A | `20-architettura` | ☐ |
| R2.2 | Novità dispersa nel testo: serve un riepilogo esplicito dei contributi | Riquadro/paragrafo contributi (serve anche a R1.M1) | A | D3, intro | ☐ |
| R2.3 | Giustificazione del differito solo parzialmente convincente: perché la stessa rappresentazione dichiarativa e la stessa analisi visiva non starebbero in un sistema real-time o ibrido? | Rispondere esplicitamente; si compone con R1.M2 (concedere che la descrizione è indipendente dal motore, e tenere solo ciò che il differito abilita davvero) | A | D2, `50-conclusioni` | ☐ |
| R2.4 | Registro incoerente: colloquiale ↔ elaborato, virtuosismo sopra la precisione | Stessa riscrittura di R1.M3 | A | tutte | ☐ |

---

## Fasi di lavoro

Branch dedicato (`fix/camera-ready-cim2026`), un commit per fase.

| # | Fase | Contenuto | Prerequisito |
|---|------|-----------|--------------|
| 0 | Decisioni | D1–D6 chiuse con l'utente (D2 anche con il maestro) | — |
| 1 | Batch meccanico | R1.D1, D10, D12, D13, D16, D17, D18, D21, D22 + listati accanto alle figure (R1.M4) | — |
| 2 | Chiarezza | R1.M3, R2.4, D2–D5, D15, D20, D23, D30, D31 — riscrittura frase per frase dalla lista verbatim | 0 (D3) |
| 3 | Sostanza | risposta Max/PD (R1.M1, D29), riquadro contributi (R2.2), MAP ridimensionata + limite di densità (R1.M2, R2.1), differito riformulato (R1.M2, R2.3) | 0 (D2, D3) |
| 4 | Terminologia e specifica | D1 applicata (R1.M5, D19, D24), `pan_range`/θ (D26, D27), tabella specifica se D4=a | 0 (D1, D4) |
| 5 | Figure | Fig. 2 a densità bassa e riposizionata (D11), Fig. 1 didascalia/wrap/verso (D6–D8), Fig. 4 verificata (D25), spettro (D14) | 0 (D6) |
| 6 | Tagli e de-anonimizzazione | R1.M7, M8; D5 (autore, copyright footnote, link pubblici, DOI); `make paper` ≤ 8 pagine | 1–5 |
| 7 | Consegna | lettera al comitato (filtro righe P/D della matrice), registrazione via form, upload camera-ready | 6 |

Fuori dal paper ma con la stessa scadenza: **registrazione al colloquio** (un form per ogni
autore partecipante e per ogni paper accettato) e prenotazione alloggio a L'Aquila.
