# Camera-ready CIM 2026 — piano di risposta alle review

**Esito:** accettato (comunicazione orale). R1 = 0 borderline, R2 = 2 accept.
**Review verbatim:** `raw/reviews/cim2026-reviews-round1.md` (immutabile).
**Scadenze:** camera-ready + registrazione (un form per autore per paper) **31 ago 2026**.
Oggi 13 ago → 18 giorni. Build-freeze interno **27 ago** (`make paper`, verifica ≤ 8 pagine).
**Obbligo del comitato:** lettera che dichiara cosa è stato recepito e, per ciò che non lo è,
la giustificazione. Questa lettera è il filtro delle righe `parziale` / `declina` della matrice.

**Vincolo duro:** il PDF è già a 8 pagine (cap). R1 chiede insieme di *tagliare* e di
*aggiungere* la specifica completa del linguaggio. I due non stanno entrambi: chiuso in D4
con l'albero della grammatica dentro un `lstlisting`, che è la forma più economica in
colonne — ma l'ingombro va misurato sul PDF prima di dare la fase 4 per fatta, e se sfora
si ripiega sull'albero dei soli parametri degli esempi più rinvio al repo.

---

## Decisioni preliminari (bloccano la riscrittura — chiuderle prima di scrivere)

| ID | Decisione | Opzioni | Note di vincolo |
|----|-----------|---------|-----------------|
| D1 | `dephase` → `deviation_probability` — **DECISA 2026-08-13: (b) rinominare nel paper e nel PGE** | (a) tenere la chiave, glossarla alla prima occorrenza («jitter probabilistico») e giustificare in lettera; (b) rinominare nel paper e nel PGE; (c) rinominare solo nel paper | Il nome non è `jitter`: nel PGE `jitter` nomina già l'ampiezza (`default_jitter`), e per `reverse` il gate è probabilità di flip booleano, senza alcun range. Né `deviation` secco: la deviazione è l'ombrello che si fattorizza in ampiezza × probabilità, e prendersi la parola cancellerebbe la fattorizzazione dal nome. Motivo del cambio: `dephase` è esatto solo nel modo micro (gate sui `default_jitter`) e fuorviante nel macro (gate su un `offset_range` esplicito, dove i grani saltano su un terzo del buffer); il parametro è una probabilità, quindi scale-free, e il vecchio nome si impegnava su una sola scala. Rilasciata in PGE **v7.0.0** (PGE #204), senza alias di retrocompatibilità; language server allineato (PGE-ls #40). Il pin del submodule sale da `v4.0.0-119` a `v7.0.0`, così la notazione pubblicata coincide col sistema scaricabile — l'opzione (c) era esclusa proprio da questo, visto che a D5 il repo viene linkato pubblicamente e chi clona prende HEAD. Risponde a R1.M5 / R1.D19 / R1.D24: accolta la sostanza (il nome ora dice probabilità), respinta la struttura (nidificare sotto `pointer` come `offset_probability` cancellerebbe la forma globale scalare — nei modi `GLOBAL`/`GLOBAL_ENV` il `param_key` è ignorato e la probabilità si applica a tutti i parametri), respinto il nome proposto |
| D2 | Sorte del differito in `sec:implicazioni` — **DECISA 2026-08-12: (a) restringere e concedere · RIAPERTA da D7** | (a) restringere + concedere la distinzione motore/descrizione, tenendo solo la parte difendibile (la MAP come rappresentazione totale post-render); (b) tagliare (R1); (c) espandere la giustificazione (R2) | Concedere a R1.M2 che RT/DT è proprietà del motore, non della descrizione; tenere solo ciò che il differito abilita davvero. Risponde anche a R2.3 e libera spazio. Vincolo maestro: mai «real-time come cambio di paradigma». **Riaperta da D7:** se il motore diventa l'oggetto dichiarato del paper, la concessione «il motore non è oggetto dell'articolo» (R1.M2) non è più disponibile nella forma decisa il 12 ago. Le due si chiudono insieme, e la lettera deve raccontare la scelta senza contraddirsi |
| D3 | Dove risponde l'obiezione «≈ patch Max/PD» — **CHIUSA 2026-08-13: nessuna delle tre. Si ritira la rivendicazione che la provoca** | (a) in introduzione; (b) in `sec:tradizione`; (c) nel riquadro contributi | Non si risponde all'obiezione: si toglie il confronto. Spariscono (i) ogni claim di superiorità del modello dichiarativo su altri sistemi e (ii) ogni asserzione su *come si lavora* con Max, Pure Data, SuperCollider, Csound. Motivo: l'affermazione è confutabile da chiunque con «tu non sai come lavoro io» — la maggior parte dei compositori usa quei sistemi in modo di fatto dichiarativo. **Criterio che sostituisce D3, da applicare in tutto il paper:** le affermazioni positive su ciò che *questo* sistema fa restano; le affermazioni su come altre persone lavorano con altri strumenti vanno via. **Non tocca la genealogia**: i precursori citati con la loro tecnologia (CMask con uscita Csound, Lippe su ISPW, GrainLab, EC2) restano — sono storia, non confronto. Risponde a R1.M1 e R1.D29 per concessione piena |
| D7 | **Contributo dichiarato del paper — APERTA, da chiudere prima della fase 2** | (a) resta il modello dichiarativo\slash notazione (regime attuale); (b) ricentratura sul **motore di granulazione differita come libreria**: un'infrastruttura su cui costruire sistemi, che consente l'intervento puntuale e localizzato sullo stream, contro il granulatore real-time che emette e basta | Proposta dell'autore 2026-08-13, non ancora chiusa («questa cosa ancora non va capita bene»). Se (b): cambia il baricentro di abstract, intro, `40-tradizione` ¶1 e ¶3, `50-conclusioni`; i tre contributi concreti (fattorizzazione della deviazione, blend `scatter`, map) sopravvivono intatti perché sono già feature del motore. **Due vincoli sulla formulazione:** (1) «deterministico» va scopato alla specifica, non alla resa — il rendering è stocastico per costruzione e la riproducibilità è per andamento (cfr. CLAUDE.md, «Riproducibilità»); (2) la contrapposizione al granulatore real-time ricrea il confronto appena ritirato con D3, quindi va detta come capacità propria, non come difetto altrui. Se (b) passa, aggiornare la sezione «Central thesis» di CLAUDE.md e valutare titolo\slash acronimo (vedi nota sotto) |
| D4 | Specifica completa del linguaggio — **DECISA 2026-08-12: (d) albero dentro un listato** | (a) tabella compatta; (b) rinvio a documentazione repo; (c) tabella + rinvio; **(d) albero della grammatica (AST/tree) reso come `lstlisting`** | Un albero indentato in `lstlisting` costa meno spazio di una tabella e mostra la ramificazione proprietà → sottoproprietà → dominio, che è esattamente ciò che R1.M6 chiede. Va generato dallo schema di validazione del PGE, non scritto a mano, per non divergere. Verificare l'ingombro reale prima di committarci: se sfora, ramo `(d) + rinvio al repo` per i parametri fuori dagli esempi |
| D5 | De-anonimizzazione | ripristinare autore/affiliazione/email, scommentare `\blfootnote` copyright, sostituire il link OSF anonimo con link pubblico (+ DOI Zenodo se si pubblica il bundle audio), decidere se citare il repo PGE per nome | Nulla nelle review lo ricorda: è l'errore facile da spedire. `paper.tex:8-26` |
| D6 | Rigenerazione figure/audio — **DECISA 2026-08-13: si rirende tutto**, di fatto già fatto | Fig. 2 va rifatta a densità bassa (R1.D11). Se si rirende, decidere se rirenderizzare anche l'audio del bundle | Il bump del submodule a v7.0.0 (#35) ha imposto la rigenerazione completa di esempi e audio: il motore è salito di due major, tenere figure rese da v4 le avrebbe fatte divergere dal codice citato. La densità di Fig. 2 **non** si rifà: l'esempio è quello scelto per il suono, D11 diventa parziale. Rendering stocastico: riproducibilità per andamento, non bit-identico |

### Note aperte legate a D7

**Titolo e acronimo.** Il titolo dice «ambiente dichiarativo» e `DIRAC` scioglie in
*Declarative Intermediate Representation for Audio Composition*: la parola che D3
ridimensiona è dentro il nome. Raccomandazione: tenere «dichiarativo» come
*descrizione* della notazione (è vera e non comparativa) e togliere solo la
superiorità — così nome e titolo sopravvivono. Se D7 va su (b) e si vuole
demandare la parola, è un cambio di titolo e acronimo in camera-ready: da
decidere esplicitamente, non per inerzia.

**Sviluppi futuri — DECISI 2026-08-13: dentro.** La sezione chiude il paper e serve
anche ad annunciare i lavori successivi (language server, interfaccia). Nota: se D7
va su (b), «motore come libreria» rende l'annuncio strutturale invece che
appiccicato — i lavori futuri sono cose costruite *sopra* la libreria. Il materiale
c'è già in `50-conclusioni.tex:31-56` (analisi del materiale, covarianza dichiarata
fra parametri, ridondanza non cromatica della map): va estratto e intestato, non
scritto da zero.

---

## Matrice delle risposte

Classe: **A** = accetta · **P** = parziale · **D** = declina (con giustificazione in lettera).
Stato: ☐ da fare · ☑ fatto.

### R1 — osservazioni maggiori

| ID | Osservazione | Azione proposta | Classe | Dove | Stato |
|----|--------------|-----------------|--------|------|-------|
| R1.M1 | Novità sopravvalutata: il YAML equivale ai controlli di una patch Max/PD, egualmente dichiarativi e forse più efficaci; dire in quali contesti la notazione testuale conviene | **Concessione piena (D3 chiusa):** si ritira la rivendicazione, non si difende. Via ogni claim di superiorità del dichiarativo e ogni asserzione su come si lavora con altri sistemi. Restano solo le capacità positive del sistema, dette senza termine di paragone | A | D3, intro + `40-tradizione` | ☐ |
| R1.M2 | La discussione tempo reale/differito non serve: RT/DT è proprietà del *motore*, non della descrizione; il motore non è oggetto dell'articolo; solo la MAP è soggetta alla distinzione, e il suo status è sopravvalutato | Concedere la distinzione motore/descrizione (è corretta e rafforza il resto); ridurre la sezione alla sola parte difendibile | P | D2, `sec:implicazioni` | ☐ |
| R1.M3 | Prosa a tratti incomprensibile; elenco di locuzioni «parole in libertà»; semplificare a partire dall'introduzione | Riscrittura di chiarezza, una locuzione alla volta dalla lista verbatim | A | tutte | ☐ |
| R1.M4 | Listati sotto le figure corrispondenti | Ogni `lstinputlisting` è dentro il float `figure` della propria map: un solo posizionamento, due caption e due contatori | A | `20`–`27` | ☑ chiusa 2026-08-14 |
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
| R1.D6 | Legenda «pitch (cents)» non usata in Fig. 1 | La colormap è già spiegata nel cappello (`20-architettura`), dove la MAP si presenta prima di comparire: non serve ripeterlo in didascalia | A | `20-architettura` | ☑ 2026-08-15 |
| R1.D7 | Wrapping fine→inizio: buffer circolare? click? campioni a cavallo? | Esplicitare l'assunzione e cosa fa l'implementazione | A | `22-pointer` | ◐ 2026-08-15 (`4648254`): la didascalia di Fig. 1 dichiara che la durata dello stream eccede quella del file, la testina esaurisce il buffer a ≈1,35 s e rientra da zero. **Resta**: click e campioni a cavallo del punto di giunzione |
| R1.D8 | Il verso di lettura cambia: perché, e non dovrebbe essere un parametro? | Spiegare il meccanismo; se è un limite, dirlo | A | `22-pointer` | ☑ 2026-08-15 (`4648254`): dove la `speed_ratio` è negativa si invertono insieme verso di percorrenza del buffer e verso interno ai grani; l'accoppiamento è il default, e `grain.reverse` rende i due versi dichiarabili separatamente — quindi è un parametro, come il revisore chiedeva |
| R1.D9 | «non visualizzabile con forma d'onda o sonogramma»: «è cinematica di base» | Ridimensionata togliendo la nota sulla disposizione retrograda (macro `\notaSinottica`, ora rimossa): la frase non parla più della cinematica del puntatore ma del fatto che la posizione di lettura è un asse della MAP — ed è quello che forma d'onda e sonogramma non hanno | P | `22-pointer` | ☑ 2026-08-15 |
| R1.D10 | Footnote 7 sembra un esponente; `fill_factor` = overlap va nel corpo | Spaziatura nota + overlap nel testo | A | `23-griglia` | ☑ |
| R1.D11 | Fig. 2 illeggibile: serve densità molto più bassa; spostarla dopo | **Riposizionata ✓. Densità bassa declinata:** l'esempio è quello scelto dall'autore per il suono. Si concede la premessa e si risponde con la leggibilità del pannello inferiore — vedi «Disallineamento di `distribution.yml`» sotto | P | `23-griglia` | ☑ (P — in lettera) |
| R1.D12 | IOT con soprallineatura → `IOT_avg` e spiegare | Cambiare notazione | A | `23-griglia` | ☑ |
| R1.D13 | Le istruzioni di lettura del grafico vanno in didascalia | Spostare in caption | A | `23-griglia` | ☑ |
| R1.D14 | Le affermazioni sullo spettro a righe chiedono figure spettrali | **DECISA 2026-08-13: la figura spettrale si fa.** Lo spazio lo finanziano i tagli di prosa (M7), che l'autore ha confermato essere estesi. Generabile da `paper/examples/plot.py` | A | `23-griglia` | ☑ |
| R1.D15 | «Nel congelamento le due vie sono complementari»: congelamento di cosa? | Riscrivere | A | `23-griglia` | ☐ |
| R1.D16 | Listato 3 mai referenziato né commentato | Referenziare e commentare (o togliere) | A | `23-griglia` | ☑ |
| R1.D17 | «envelope» → «inviluppo» in tutto l'articolo | Sostituzione sistematica | A | tutte | ☑ |
| R1.D18 | Manca il numero della figura in «etichettati (a) e (b) nella figura» | Aggiungere `\ref` | A | `24-deviazione` | ☑ |
| R1.D19 | `dephase.pointer` fuorviante: è probabilità di spostamento dell'onset; meglio sotto `pointer` (es. `offset_probability`); implementazione «barocca» | Vedi D1; in ogni caso spiegare meglio il caso | P | D1, `24-deviazione` | ◐ nome accolto (`deviation_probability.pointer`), struttura respinta con motivazione in D1; resta il «spiegare meglio il caso» |
| R1.D20 | «non potrebbero essere più diverse» colloquiale; spiegazione floreale | Riscrivere piano | A | `24-deviazione` | ☐ |
| R1.D21 | Eq. 2: cos'è `v_n`? | Definire | A | `24-deviazione` | ☑ |
| R1.D22 | «(a) è questo modello all'opera» — con `c(τ_n)` costante | Precisare | A | `24-deviazione` | ☑ |
| R1.D23 | «due inviluppi ortogonali, (a) muove la prima a gate aperto…» non si capisce | Riscrivere | A | `24-deviazione` | ☑ riscritta insieme a D22 (fase 1): ora dice esplicitamente quale inviluppo si muove e quale resta fermo in ciascuno dei due stream. **Non riscriverla di nuovo in fase 2** |
| R1.D24 | `dephase` ≠ deviazione; considerare jitter | Vedi D1 — sostanza accolta, `jitter` respinto (nomina già l'ampiezza: `default_jitter`) | P | D1 | ☑ |
| R1.D25 | Fig. 4: l'andamento cubico 20–80% non si vede (sembra lineare a scalini); deviazione = 100 di cosa? | Verificare la figura contro il YAML; correggere didascalia e unità | A | `24-deviazione`, #36 | ◐ didascalia corretta: il revisore aveva ragione, l'esempio ha `type: step` e non `cubic` — corretti «cubico» → «a gradini» e «con continuità» → «per gradi». Resta l'unità: la legenda dice `ptr dev %` ma quella curva è la probabilità, non l'ampiezza (etichetta generata da `page_layout.py` del motore) → #36 |
| R1.D26 | Mid-Side/Blumlein superfluo; θ è azimuth astratto; perché non oltre la circonferenza unitaria | Ridurre a θ astratto, rinviare la realizzazione; dichiarare il limite stereo | P | `27-voci` | ☐ |
| R1.D27 | `pan_range`: jitter sul pan o apertura del fronte? nome cattivo; «come ogni parametro» non torna | Chiarire la semantica; uniformare il discorso su `*_range` | A | `27-voci` | ☐ |
| R1.D28 | «svolta nel volume 1993»: il real-time granulare è precedente (Riverrun 1986); riferimenti troppo centrati su CIM | Chiarire che la scansione è *negli atti CIM* (il testo già dice «negli atti»), non nella storia generale; ampliare la bibliografia extra-CIM. Attenzione: non riformulare in «real-time come cambio di paradigma» (vincolo maestro) | P | `40-tradizione` | ☐ |
| R1.D29 | «dove la specifica resta interrogabile»: casi concreti; cosa fa il YAML che gli oggetti Max non fanno | Non si risponde al confronto: si toglie (D3). Resta la sola descrizione positiva di dove la specifica è interrogabile, senza «cosa fa in più di» | A | D3, `40-tradizione` | ☐ |
| R1.D30 | «asse dichiarativo continuo… Due casi la circoscrivono»: referente ignoto, paragrafo fumoso | Riscrivere | A | `40-tradizione` | ☐ |
| R1.D31 | «tiene il ritorno dell'ascolto abbastanza vicino alla scrittura…»: che vuol dire | Riscrivere piano | A | `50-conclusioni` | ☐ |

### R2

| ID | Punto | Azione | Classe | Dove | Stato |
|----|-------|--------|--------|------|-------|
| R2.1 | Utilità della MAP asserita, non valutata. **Rilettura 2026-08-14:** la richiesta operativa è «*a few comments would help strengthen the motivation*» — motivare, non ammettere. L'«*information dense and difficult to interpret*» è ambiguo e la vecchia riga lo risolveva contro il paper | Presentare la map nel cappello prima che compaia (come si legge: assi, waveform laterale, glifo del grano, colore, `stream_id`, pannello inviluppi) e motivarla: è negli esempi fitti che la vista d'insieme serve **di più** | A | `20-architettura` | ☑ 2026-08-14 |
| R2.2 | Novità dispersa nel testo: serve un riepilogo esplicito dei contributi | Riquadro/paragrafo contributi (serve anche a R1.M1) | A | D3, intro | ☐ |
| R2.3 | Giustificazione del differito solo parzialmente convincente: perché la stessa rappresentazione dichiarativa e la stessa analisi visiva non starebbero in un sistema real-time o ibrido? | Rispondere esplicitamente; si compone con R1.M2 (concedere che la descrizione è indipendente dal motore, e tenere solo ciò che il differito abilita davvero) | A | D2, `50-conclusioni` | ☐ |
| R2.4 | Registro incoerente: colloquiale ↔ elaborato, virtuosismo sopra la precisione | Stessa riscrittura di R1.M3 | A | tutte | ☐ |

---

## Fasi di lavoro

Branch dedicato (`fix/camera-ready-cim2026`), un commit per fase.

| # | Fase | Contenuto | Prerequisito |
|---|------|-----------|--------------|
| 0 | Decisioni | D1, D3, D4, D6 chiuse. **Restano D7** (contributo dichiarato: blocca tutto il resto), **D2** (riaperta da D7) **e D5** (de-anonimizzazione) | — |
| 1 | Batch meccanico | R1.D10, D12, D13, D16, D17, D18, D21, D22 + listati accanto alle figure (R1.M4). **R1.D1 esce di fase**: l'abstract si riscrive comunque sotto D7, rifinire «queryable IR» adesso è lavoro buttato | — |
| 2 | Chiarezza | R1.M3, R2.4, D2–D5, D15, D20, D23, D30, D31 — riscrittura frase per frase dalla lista verbatim | 0 (D7) |
| 3 | Sostanza | ritiro dei confronti e dei claim di superiorità (D3 → R1.M1, D29), riquadro contributi (R2.2), MAP ridimensionata + limite di densità (R1.M2, R2.1), differito riformulato (R1.M2, R2.3) | 0 (D7, D2) |
| 4 | Terminologia e specifica | D1 applicata ✓ (rinomina fatta in #35). Restano `pan_range`/θ (D26, D27), il «spiegare meglio il caso» di D19, e l'albero della grammatica di D4 generato dallo schema | 0 (D1 ✓, D4 ✓) |
| 5 | Figure | D11 chiusa ✓ (riposizionata; densità bassa declinata). Resta l'unità di Fig. 4 (D25) → **issue #36**; Fig. 1: D6 ✓, D8 ✓, D7 ◐ (restano click e campioni a cavallo); **figura spettrale nuova (D14, decisa: si fa)** | 0 (D6 ✓) |
| 6 | Tagli e de-anonimizzazione | ~~Riverificare M4 sull'impaginazione finale~~ (chiusa 2026-08-14: il listato è dentro il float, il vincolo regge da sé — vedi nota sotto); R1.M7, M8 — **tagli estesi, non cosmetici**: l'autore riferisce l'indicazione di scendere ben sotto le 8 pagine, e che troppo spazio va in spiegazioni fumose. Finanziano D4, D14 e il riquadro contributi; D5 (autore, copyright footnote, link pubblici, DOI); `make paper` | 1–5 |
| 7 | Consegna | lettera al comitato (filtro righe P/D della matrice), registrazione via form, upload camera-ready | 6 |

### Regola operativa del branch: le modifiche si vedono in rosso

`make paper-diff` compila `paper/paper-diff.pdf` con le modifiche marcate —
aggiunte in rosso ondulato, tagli in rosso barrato — via `latexdiff` contro
`DIFF_BASE`, che punta al tag **`cim2026-submitted`** (`c30a0d6`, 23 giu): la
versione spedita a EasyChair, identificata contro il PDF conservato dall'autore
(nel PDF la didascalia di Fig. 3 precede il paragrafo d'apertura di
`sec:deviazione`, disposizione introdotta da quel commit; dopo di lui nessun
commit tocca `paper/` fino ad agosto; 8 pagine). **Non usare il merge-base con
`main`**: `main` aveva già ricevuto la rinomina `deviation_probability` e il
bump a PGE v7 il 13 agosto, e con quel baseline la risposta a R1.M5/D24
sparirebbe dal rosso. Per rileggere il solo lavoro recente:
`make paper-diff DIFF_BASE=$(git merge-base main HEAD)`.
**Strumento di rilettura, non di consegna**: al comitato va il
camera-ready pulito più la lettera. Output gitignored, si rigenera a comando.
Non ha `examples` come prerequisito: rigenerare gli esempi cambierebbe le
figure (rendering stocastico) senza motivo.

### Ordine di lavoro deciso (2026-08-14)

**Si parte dal corpo, sequenziale `20` → `27`.** Introduzione, conclusioni e
abstract si riscrivono alla fine — dipendono da D7 e dal contributo dichiarato,
e rifinirli adesso è lavoro buttato. Criterio dell'autore: **prima si aggiunge
ciò che manca, poi si sfoltisce**; i tagli di M7/M8 restano in fase 6.

**Conto pagine:** dopo il blocco sulla map il paper è a **9 pagine** (cap: 8).
La fase 6 deve recuperare almeno una pagina piena.

### Il ponte YAML → motore manca nel capitolo 2 (aperto)

Verificato 2026-08-14: la regola «quasi ogni parametro è valore base + banda di
deviazione (`chiave_range`) + probabilità che si applichi
(`deviation_probability.chiave`)» è enunciata **una volta sola e tardi**, in
`24-deviazione.tex:68-73`, e per giunta come nota di generalizzazione a
posteriori («scelta come istanza»). In `25-esempio_di_mezzo.tex:14` viene
richiamata («Come ogni parametro…») ed è esattamente lì che il revisore si
perde su `pan_range` (R1.D27): non ha mai letto la regola *come regola*.
Nel cappello e in `sec:c-e` non c'è nulla sul funzionamento del motore.

**Deciso:** il blocco va scritto. **Aperto:** dove (cappello / sottosezione
propria / dentro `sec:c-e`) e cosa ci entra oltre alla regola (inviluppi a
breakpoint, stream e grano, catena YAML → grani → audio + map).

### Inventario delle frasi opache (R1.M3 + note dettagliate, 2026-08-14)

Diciassette punti. Le otto locuzioni della lista verbatim di R1.M3 sono tutte
ancora nel testo: la fase 1 ha fatto solo il batch meccanico.

| # | Dove | Frase | Obiezione | Destino |
|---|------|-------|-----------|---------|
| 1 | `00-abstract:13` | «queryable IR» | R1.D1 | fine (dopo D7) |
| 2 | `10:7-9` | «resta una distanza opaca» | R1.D2 | fine |
| 3 | `10:12-14` | «ciò che una specifica testuale non mostra» | R1.D3 | fine |
| 4 | `10:16-34` | tutto il paragrafo «Tre tradizioni» | R1.D4 | **rimandata** (taglio / riduzione / riscrittura) |
| 5 | `10:28` | SuperCollider «dichiara l'esito anziché la procedura» | R1.D5 | fine |
| 6 | `10:32` | «la specifica si compila e si consuma» | R1.M3 | fine |
| 7 | `10:54` | «l'artefatto normalizzato su cui operano le trasformazioni» | R1.M3 | fine |
| 8 | ~~`22-pointer:27-30`~~ | «non è visualizzabile attraverso la forma d'onda, sonogramma…» | R1.D9 | ☑ chiusa 2026-08-15 (via nota rimossa) |
| 9 | `23-griglia:83` | «Nel congelamento le due vie sono complementari» | R1.M3 + D15 | corpo |
| 10 | `24-deviazione:73` | «come gli esempi successivi dispiegano» | R1.M3 | corpo |
| 11 | `24-deviazione:100` | «non potrebbero essere più diverse» | R1.D20 | corpo |
| 12 | `24-deviazione:101-108` | il cuneo, «grani fedeli e grani devianti in proporzione componibile» | R1.M3 + D20 | corpo |
| 13 | `24-deviazione:141` | «I primi tre angoli del quadro sono già a tema» | R1.M3 | corpo |
| 14 | `24-deviazione:115-139` | Eq. 1 e Eq. 2 | R1.M8 | **DECISO: restano entrambe, giustificate nel testo** (la differenza fra le due è un solo fattore, ed è il contributo) |
| 15 | `40-tradizione:47` | «Ciò che qui è proprio è dove la specifica resta interrogabile» | R1.D29 | dopo il corpo |
| 16 | `40-tradizione:49-52` | «esporre come asse dichiarativo continuo… Due casi la circoscrivono» | R1.D30 | **DECISO: taglio del confronto** — ma prima va capito cosa afferma (vedi sotto) |
| 17 | `50-conclusioni:61-65` | «là subìto, qui scelto in quanto abitabile…» | R1.M3 + D31 | **rimandata a dopo D2** |

**Perché #16 non si capisce (esegesi 2026-08-14).** Il paragrafo ha **due
enumerazioni a coppie annidate senza segnale**: «le proposte sono due» (YAML
come notazione; la map) e, dentro la prima, «due casi la circoscrivono»
(fattorizzazione della deviazione; blend `scatter`). Il lettore arriva a «La
seconda è la map» e non sa se sia il secondo caso o la seconda proposta. Il
«la» di «Due casi **la** circoscrivono» rinvia a «una mossa ricorrente», tre
righe sopra, oltre un inciso fra trattini. «Circoscrivere» vale qui *delimitare
la portata*: sono le sole due istanze, quindi non è un principio generale — una
cautela che nessun lettore ricostruisce. E «Ciò che qui è proprio è X e Y»
coordina un avverbio di luogo («**dove** la specifica resta interrogabile») con
un sostantivo («**una mossa** ricorrente»). Da ritirare per D3: «un controllo
che la tradizione tiene fuso o binario», «nei generatori di score di questa
famiglia il valore è sempre estratto dalla maschera» e «negli ambienti Lisp un
gate è costruibile come idioma ma non è parametro di prima classe» — asserzioni
su altri sistemi, per giunta senza citazione a sostegno.

### Disallineamento di `distribution.yml` (trovato 2026-08-13, chiuso 2026-08-14)

Non era un difetto dell'esempio: era il testo rimasto indietro rispetto
all'esempio. L'autore aveva modificato il YAML per ottenere un risultato sonoro
più interessante — aggiungendo un terzo stream marcato `solo:` e rirenderizzando
il 13 ago — senza poi aggiornare listato e prosa, ancora fermi ai primi due
stream. **Figura e audio sono corretti e non si toccano.**

`paper/examples/distribution/distribution.yml` contiene tre stream; il terzo
porta la chiave `solo:` (valore nullo), e in PGE `solo` filtra per **presenza**
della chiave, non per valore: `solo_mode = any('solo' in s for s in
stream_data_list)` in `src/pge/engine/generator.py:283`. Quindi solo il terzo
stream viene renderizzato, ed è quello in Fig. 2 — che è esattamente ciò che
l'autore voleva sentire.

Il disallineamento toccava tre punti, tutti corretti in `4804b88`:

1. **Il listato mostrava un altro esempio.** Il `linerange={5,10,11,16,21,22,27}`
   pescava righe degli stream 1 e 2. In particolare la riga 27
   (`distribution: [[0,0],[1,1]]`) è una rampa monotona che *non* è quella
   plottata. È il «non si capisce la sua relazione con le altre figure» di
   R1.D16: il revisore ha visto l'incoerenza senza avere il file.
   Ora `linerange={29,35-39,41}`, cioè lo stream reso.
2. **Didascalia e corpo affermavano il falso.** Lo stream 3 ha
   `density: [[0,10],[0.5,200],[1,10]]` e `distribution: [[0.3,0],[.75,1],[1,0]]`:
   la densità non è costante (quindi «a parità di numero medio di grani» era
   falso) e la `distribution` è piatta a 0 fino al 30%, tocca 1 al 75% e rientra
   (quindi «da uniforme a dispersa» ne descriveva solo un tratto). Il paragrafo
   ora dichiara i due inviluppi e il loro **sfasamento**: il culmine della
   densità cade dove la griglia è ancora regolare, l'asincronia piena arriva a
   densità già calante.
3. **Gli onset non sono risolvibili** al picco di 200 grani/s: la banda è una
   massa piena e serve la lente. Il testo non lo nega più — lo dichiara, e ne fa
   il punto in cui la specifica resta leggibile (pannello inferiore) dove la
   massa dei grani non lo è.

**Riclassificazione di R1.D11: da A a P.** La densità bassa che il revisore
chiede non si fa: significherebbe rifare l'esempio che l'autore ha scelto per il
suono. Si concede la premessa (a quella densità la map non risolve i singoli
onset) e si risponde con la leggibilità del pannello inferiore. **Va in lettera.**
Il riposizionamento della figura, l'altra metà di D11, è fatto.

**Conseguenza su #36:** la metà «Fig. 2 a densità bassa» si dissolve. Resta la
sola unità di Fig. 4 (R1.D25).

**Due trappole del file, da non innescare:**
- **Non rinominare `stream_id`**: `sync_to_async` è stampato dentro la figura, in
  entrambi i pannelli. Rinominarlo nel YAML desincronizza listato e figura senza
  rirenderizzare.
- **Non ripulire il YAML da solo** (stream 1-2 morti, `solo:`, i `#10.0`
  residui): il `linerange` è a numeri di riga assoluti, e ogni pulizia lo rompe
  in silenzio — la stessa classe di bug appena corretta. Se si ripulisce,
  `linerange` nello stesso commit.

**Lezione di metodo, da applicare al resto della fase 5:** ogni didascalia va
verificata contro il YAML *renderizzato* e contro la figura resa, non contro il
YAML letto di sfuggita. R1.D25 era già questo errore (`type: step` spacciato per
`cubic`). Quanto a `solo:`/`mute:`, il controllo su tutti gli esempi è **fatto**:
`grep -c "solo:\|mute:" paper/examples/*/*.yml` trova solo `distribution.yml`.
Gli altri esempi renderizzano tutti gli stream che dichiarano.

**Chiusura di M4 (2026-08-14).** La verifica del 2026-08-13 constatava che le
coppie cadevano già nella stessa pagina, ma per fortuna: il `figure` fluttuava e
il `\lstinputlisting` con caption restava ancorato al testo — due regimi di
posizionamento per un blocco che si legge insieme, che le riscritture delle fasi
2-3 avrebbero rimescolato. Adottata la soluzione robusta già indicata lì: **il
listato sta dentro il float `figure`** (commit `6f00958`, `354d466`). Restano due
caption e due contatori — figura e listato hanno ruoli argomentativi distinti
nella cellula espositiva (specifica → risultato) — quindi ogni `\ref` in prosa è
invariato. Uniformato il piazzamento a `[!t]` (erano `[h]`, `[H]`, `[t]`),
sostituito `\captionof{figure}` con `\caption`, e tradotto `\lstlistingname` in
«Listato» dentro `\captionsitalian`: il PDF diceva «Listing N» mentre la prosa
scriveva «Listato N». Il caso peggiore (`26-esempio_completo`: 15 righe di YAML +
map a due pannelli) sta in colonna, nessun `Float too large`. `sec:c-e` resta
fuori: listato breve senza figura, ancorato di proposito dentro il paragrafo.
**Non serve più ricontrollare in fase 6** — il vincolo è ora strutturale, non
fortunato. Nota di metodo che resta valida: `pdftotext | grep "Listato N"` conta
anche i richiami nel testo corrente, non solo le didascalie — verificare per nome
del file YAML (`grep -oE "pointer\.yml|distribution\.yml|…"`), che compare solo in
didascalia.

Fuori dal paper ma con la stessa scadenza: **registrazione al colloquio** (un form per ogni
autore partecipante e per ogni paper accettato) e prenotazione alloggio a L'Aquila.
