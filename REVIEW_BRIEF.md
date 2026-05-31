# REVIEW_BRIEF — Review sistematica, critica e referenziale
### Paper CIM 2026: «Un ambiente Python per la sintesi granulare in tempo differito»

> File di istruzioni per Claude Code. Da posizionare nella root del progetto di review.
> Tutto ciò che segue nella sez. 4 è **già stato verificato** in sessione precedente:
> trattalo come dossier di partenza da *confermare ed estendere*, non da riscoprire da zero.

---

## 1. Obiettivo

Produrre un **referee report** in stile AIMI/CIM: **critico** (individua i punti deboli, non riassume soltanto), **referenziale** (ogni affermazione su altri sistemi/letteratura è ancorata a una fonte verificata, nessuna citazione inventata), **ben organizzato** (struttura fissa, raccomandazioni azionabili). Lingua: **italiano**. Registro: accademico, asciutto.

Raccomandazione attesa (da confermare con l'analisi, non da assumere): **accept with revisions**.

---

## 2. Deliverable attesi

1. `review_report.md` — il referee report finale (struttura in §7).
2. `revision_checklist.md` — lista numerata di revisioni azionabili per l'autore, ciascuna con: punto del paper, problema, fix proposto, priorità (P1/P2/P3).
3. `references_audit.md` — esito della verifica bibliografica (§ Fase 3).
4. (opz.) `figure_walkthrough.md` — bozza della lettura guidata della partitura (vedi Fase 4, asse esperienziale).

---

## 3. Input / file da raccogliere nel progetto

- [ ] `paper.pdf` — il paper sotto review (submission anonimizzata; copyright dichiara G. De Mattia Romano).
- [ ] `score_example.png` — la **partitura grafica generata dal sistema** (artefatto chiave: vedi §4.2).
- [ ] `dafx98-marti.pdf` — paper Vocom/Vocem di riferimento (scaricabile: `http://mtg.upf.edu/files/publications/dafx98-marti.pdf`).
- [ ] (opz.) abstract/PDF di EmissionControl2 (Roads et al., CMJ 45/3, 2021) per il confronto contemporaneo.

---

## 4. Dossier di partenza (fatti già verificati)

### 4.1 Il paper in breve
- **Tema**: ambiente Python per sintesi granulare in **tempo differito**; tesi centrale = il differito abilita un *loop di feedback lungo* (specifica → genera → ascolta → riflette → riscrive) come **postura compositiva**.
- **Architettura (§2)**: `Grain` (dataclass immutabile, frozen+slots, 8 campi) → `Stream` → IR Python → renderer disaccoppiato. DSL in **YAML** interpretato come *tendency mask* (Truax): traiettoria centrale `c(t)` + range di deviazione `s` + campionamento per-grano. `ProbabilityGate` sulla chiave `dephase`. Inviluppi `f(t)→v` a breakpoint (lin/cubica Fritsch–Carlson/step). 4 controllori ortogonali (Density, Pointer, Pitch, Window). `GrainClipStrategy` = unica fonte di verità sui grani. Multi-voce su 4 assi (pitch/onset/pointer/pan). Renderer: NumPy (nativo), Csound, ReaperWriter, dietro `AudioRenderer` (Open-Closed). Cache **SHA-256** per-stream. Language Server (LSP + JSON Schema).
- **Partitura grafica (§3)**: generata dalla stessa IR; **asse Y = posizione di lettura nel buffer sorgente** (non frequenza); output diagnostico, non input.
- **Posizionamento (§4)**: Gabor → Roads (AGS) → Truax (tendency mask, micro/macro) → linea offline italiana (De Poli/Piccialli, Di Scipio, Arcella/Silvestri) → Lippe (transizione real-time) → ritorno volontario al differito (Risset).
- **§5 implicazioni**: composizione = studio della tecnica; «la forma del suono è più *operazionalizzata* che prodotta» (Di Scipio); strumenti non neutri.

### 4.2 La figura della partitura (artefatto chiave — `score_example.png`)
- Forma d'onda della **sorgente plottata in verticale** sul margine sinistro, allineata all'asse Y (Sample in s): l'asse di lettura è ancorato al contenuto reale del campione.
- **Ogni grano** disegnato come segno a (tempo d'uscita, posizione di lettura); migliaia di marche; colore = parametro per-grano (pan/pitch), orientamento del segno = altro parametro.
- Pannello 001: 30–36 s nuvola larga (deviazione pointer alta) → 40–45 s collasso su diagonale ascendente nitida (deviazione che si stringe, lettura in avanti). Pannello 002: banda compatta discendente ~1.2→0.5. Striscia inferiore: inviluppi (density/distribution/grain duration/pan/pitch/volume); pan annotato −30° a ~36 s.
- **Conseguenza per la review**: questa figura È l'esempio lavorato/dimostrazione che il testo non porta. Va spostata nel corpo del paper con lettura guidata in prosa.

### 4.3 Posizionamento verificato (referenziale)
- **Vocem** (D. López, F. Martí, E. Resina, *Proc. DAFx-98*, pp. 2–5, Barcelona, 1998): la sua interfaccia per il parametro *offset* ha tempo sull'orizzontale e **posizione nel file sorgente sul verticale** (0=inizio, 1=fine) — MA come **inviluppo di controllo disegnato in input**, una singola curva. **Non** plotta i grani, non mostra deviazione, non àncora l'asse alla forma d'onda. → È un **foil**, NON un precedente. Citarlo come contrasto rafforza il paper.
- **EmissionControl2** (C. Roads, J. Kilgore, R. DuPlessis, *Computer Music Journal* 45(3):20–40, 2021): ambiente granulare **real-time** con "Scan Display" = forma d'onda + scanner sovrapposto in tempo reale. → da **nominare** come l'ambiente granulare-con-visualizzazione contemporaneo rispetto a cui si definisce la scelta del differito. Attualmente assente dal paper.
- Altri tool passati in rassegna (nessuno fa la rappresentazione del paper): Borderlands (nuvola spaziale), Tasty Chips GR-1 / NI Reaktor (marcatore sulla forma d'onda statica), Adroit Synthesis (posizione sull'asse **orizzontale**).
- La frase del paper «dove le rappresentazioni convenzionali collocano la frequenza» è **imprecisa**: la stessa Tab. 2 mostra Truax = mask e GeoGraphy = mappa spaziale, nessuno dei due è frequenza.

### 4.4 Findings critici consolidati (baseline da verificare/estendere)
- **Verdetto generale**: comprensibile per specialisti; **compatto/denso, non superficiale**; chiaramente progettato (ingegneria reale).
- **Punti di forza**: problema ben posto; architettura coerente (`GrainClipStrategy` come single source of truth, Open-Closed, cache SHA-256); genealogia italiana CIM accurata; due idee reali (postura sul differito via Risset; partitura diagnostica con Y=read position); distinzione `density`/`fill_factor`; inviluppo che unifica macro-forma e micro-modulazione.
- **Debolezza 1 (principale) — asse esperienziale / *tells-not-shows*** : il testo dice il suono ma non lo mostra. Esempi percettivi mancanti:
  - cosa cambia all'ascolto quando `distribution` passa da 0 (sincrono) a 1 (asincrono);
  - cosa produce musicalmente una loop window mobile vs statica;
  - come si distinguono all'orecchio multi-voce `stochastic` vs `chord`.
  Gli esempi YAML sono sintattici, mai interpretati musicalmente. Frasi dense senza stadio operativo intermedio (es. «Gate e range sono ortogonali: il valore fissa l'intenzione, l'inviluppo la generalizza nel tempo, il gate sceglie dove…»: esatta ma va riletta due volte).
- **Debolezza 2 — assenza di valutazione**: nessun caso studio, nessun brano, nessuna iterazione del loop in cui la partitura rivela uno scarto poi corretto. Tesi centrale asserita, non dimostrata. Dati di performance vaghi (grani/s, footprint). → Risolvibile sfruttando `score_example.png` come dimostrazione narrata.
- **Debolezza 3 — posizionamento della partitura**: vedi §4.3 (Vocem come foil; nominare EC2; correggere «frequenza convenzionale»). NB: la critica originaria di "overclaim sull'asse Y" è stata **ritirata** dopo aver visto la figura reale — la rappresentazione è di categoria diversa da tutto il panorama.
- **Stile**: registro continentale alto, chiuse aforistiche, triadi bilanciate; la densità filosofica a tratti sovrasta la descrizione tecnica (es. «una configurazione operativa di cui il sistema è insieme strumento e argomento»). OK per CIM, rischioso per lettore interdisciplinare.
- **(opz.) AI-authorship**: la prosa ha marcatori da rifinitura LLM (triadi, aforismi); ma la *sostanza* — citazioni accurate con numeri di pagina, architettura coerente — indica autore umano competente. Il detection stilistico è inaffidabile: trattare come nota laterale, non come accusa.

---

## 5. Standard di lavoro

- **Referenziale**: ogni claim su un sistema/paper terzo va verificato su fonte primaria (PDF, atti, CMJ). **Mai** inventare riferimenti o numeri di pagina. Se una fonte non si trova, dichiararlo.
- **Critico**: per ogni sezione del paper chiedersi «dove si scopre?», «cosa contesterebbe un referee ostile?». Distinguere problemi di *sostanza* da problemi di *forma*.
- **Tracciabile**: ogni rilievo nel report rimanda a un punto preciso del paper (sezione/figura/frase).
- **Calibrato**: separare ciò che è dimostrato da ciò che è asserito; non sovra/sotto-stimare la novità (cfr. la correzione su Vocem: confermare prima di affermare).

---

## 6. Workflow a fasi (TODO)

### Fase 0 — Setup
- [ ] Confermare presenza dei file di §3.
- [ ] Creare i 4 file deliverable vuoti (§2) con intestazioni.

### Fase 1 — Comprensione e mappatura
- [ ] Leggere `paper.pdf` integralmente.
- [ ] Estrarre la **mappa dei claim**: per ogni sezione, elencare le affermazioni verificabili (tecniche, storiche, teoriche) in `review_report.md` (sezione di lavoro temporanea).
- [ ] Marcare ciascun claim come {dimostrato | asserito | referenziale-da-verificare}.

### Fase 2 — Verifica tecnica / architetturale
- [ ] Confrontare l'architettura descritta con il dossier §4.1: coerenza interna, scelte di design (immutabilità, Open-Closed, single source of truth, cache).
- [ ] Verificare la coerenza dei costrutti del DSL (es. relazione `density = fill_factor / grain_duration`; ortogonalità gate/range/inviluppo).
- [ ] Annotare claim tecnici non quantificati (performance: grani/s, footprint, tempo di build).

### Fase 3 — Verifica bibliografica e di posizionamento
- [ ] Audit di **tutte** le voci bibliografiche del paper → `references_audit.md`: esistenza, venue, anno, numeri di pagina dei quote (controllare in particolare Truax, Risset, Roads, Di Scipio, Vaggione).
- [ ] Confermare il dossier §4.3: Vocem come foil; EC2 da nominare; imprecisione «frequenza convenzionale» vs Tab. 2.
- [ ] (opz.) Controllo di completezza su filoni potenzialmente mancanti (DAFx/MTG; corpus-based/CataRT-Schwarz — verificare che usino spazi di *descrittori* e non posizione lineare nel buffer, quindi non confliggono).
- [ ] Registrare riferimenti **mancanti** da raccomandare (almeno: Vocem, EmissionControl2).

### Fase 4 — Analisi critica per assi
- [ ] **Asse esperienziale** (debolezza 1): elencare ogni concetto introdotto-ma-non-mostrato; produrre la lista dei 3+ esempi percettivi mancanti; bozza di `figure_walkthrough.md` leggendo `score_example.png` (nuvola che si stringe = deviazione pointer; banda discendente = lettura retrograda; colore = pan).
- [ ] **Asse valutazione** (debolezza 2): formalizzare la mancanza di evidenza; proporre il minimo indispensabile (1 micro-workflow idea→YAML→grani→partitura→esito sonoro atteso; 1 caso diagnostico).
- [ ] **Asse posizionamento** (debolezza 3): redigere la nota Vocom-foil + EC2 + correzione frase, pronta da incollare.
- [ ] **Asse stile**: 2–3 esempi di iper-densità; raccomandare frasi di mediazione dopo i nodi teorici.
- [ ] **Punti di forza**: consolidare in prosa (no elenco appeso).

### Fase 5 — Sintesi del referee report
- [ ] Scrivere `review_report.md` secondo la struttura §7.
- [ ] Derivare `revision_checklist.md` (numerata, con priorità).

### Fase 6 — QA / self-check
- [ ] Ogni rilievo rimanda a un punto preciso del paper? 
- [ ] Nessuna affermazione referenziale senza fonte verificata?
- [ ] Sostanza vs forma chiaramente separate?
- [ ] La raccomandazione finale segue dall'analisi (non assunta)?
- [ ] Coerenza terminologica con il paper (italiano, lessico CIM).

---

## 7. Struttura di `review_report.md`

1. **Giudizio complessivo** (4–6 frasi: comprensibilità, compattezza, 2 contributi reali, 3 debolezze in ordine di gravità).
2. **Punti di forza** (prosa).
3. **Debolezza 1 — Asse esperienziale** (lista esempi mancanti + lettura della partitura come fix).
4. **Debolezza 2 — Assenza di valutazione**.
5. **Debolezza 3 — Posizionamento della partitura** (Vocem foil, EC2, frase «frequenza»).
6. **Stile**.
7. **Raccomandazione** (accept/revise/reject + 1 frase di sintesi).
8. **Revisioni azionabili** (rimando a `revision_checklist.md`).

---

## 8. Checklist finale (P1 = bloccante per migliorare il paper)

- [ ] **P1** — Inserire `score_example.png` nel corpo con lettura guidata (chiude asse esperienziale + valutazione).
- [ ] **P1** — Aggiungere ≥1 esempio YAML con esito sonoro atteso interpretato musicalmente.
- [ ] **P1** — Citare Vocem come *foil* e correggere la frase «frequenza convenzionale».
- [ ] **P2** — Nominare EmissionControl2 come confronto contemporaneo.
- [ ] **P2** — Aggiungere ≥1 caso diagnostico (la partitura rivela X, corretto in Y).
- [ ] **P2** — Quantificare performance (grani/s, footprint, tempo build).
- [ ] **P3** — Frasi di mediazione dopo i passaggi teorici più densi.
- [ ] **P3** — (opz.) Alleggerire alcune chiuse aforistiche.
