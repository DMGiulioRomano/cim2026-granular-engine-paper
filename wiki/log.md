# Operations Log

Log append-only. Ogni entry: `## [YYYY-MM-DD] <tipo> | <titolo>`.
Tipi: `ingest`, `query`, `lint`, `restructure`.

---

## [2026-06-12] restructure | riallineamento wiki al regime bottom-up del paper

Riallineamento completo dello strato direzionale della wiki al paper reale
(branch `paper-bottom-up`), piano `buzzing-otter` approvato dopo tre giri di
revisione. La wiki era costruita per il vecchio regime (tre atti in
introduzione, 6 sezioni col caso compositivo, mapping classi→fonti); il paper
riscritto procede dal basso con label LaTeX e tre proposte dimensionate.

Interventi (branch `fix/wiki-riallineamento-bottom-up`, 6 step):
1. **CMask + quadrato 2×2** (vedi entry ingest sotto) — sbloccava `sec:tradizione`.
2. **CLAUDE.md**: Central thesis riformulata (granulazione, gate in primo
   piano, LSP di contorno, implicazioni in chiusura); struttura per funzione
   e label; formulazione Truax vietata eliminata e codificata come check;
   sezione Lessico (tabella classi→dominio); schemi ingest su label con
   tetto primaria+secondaria; checklist review-ingest estesa (3 check).
3. **graphic-score.md**: dispensa di `sec:partitura` rimappata e tradotta.
4. **overview.md**: Tesi corrente riscritta; Differenziatori 1–8 + Contributi
   riorganizzati in «Le tre proposte» + «Ciò che non è nuovo».
5. **mappa-citazioni-paper.md** (fonte di verità, stati citata/candidata/
   background) + `make cite-map` (`tools/cite_map.py`, marker BEGIN/END,
   hash di paper.tex, gancio anti-drift nel commento di testa di paper.tex);
   rimappatura per-pagina di ~70 pagine (curate/sub/background); sinossi di
   `index.md` convertite; `bibliography.md` colonne→label;
   `deferred-time-tradition.md` corretta (ruolo, atto 2, tavola, citabilità).
6. **Sweep a due livelli** (grep numerico con triage + pattern lessicali):
   residui prescrittivi azzerati fuori dalle eccezioni (log storico, verbale
   incontro, sezioni interne alle fonti); `docs/plans/next-session.md`
   marcato superseded; lint wikilink: zero rotti.

Lato paper (prescritto dai TODO interni): 5 chiavi placeholder allineate a
refs.bib (`Sparano2018`, `DeTintis1995`, `RolfeKeller2000`, `Arcella2012`,
`Solomos2003`); build verificata pulita (pdflatex+bibtex, zero undefined).

---

## [2026-06-12] ingest | Bartetzki 1997 — CMask (articolo + manuale, fonte web)

Ingest della fonte web *Csound Score Generation and Granular Synthesis with
CMask* (Bartetzki, STEAM/HfM Berlin, articolo 03/1997 + manuale 07/1997),
recuperata via snapshot Wayback (TLS rotto sull'host originale); snapshot
HTML/TXT in `raw/papers/` (gitignored con regole nuove).

**Esito centrale per la proposta 1**: in CMask il valore è sempre estratto
dalla maschera; il quantizer ha tre parametri (interval, offset, strength) e
la **strength è un'attrazione continua per-valore** («50% means that every
random number is attracted to the half distance»), envelope-abile ma applicata
a ogni evento — un *blend continuo*, non un gate Bernoulli per-grano. La
distinzione regge la rivendicazione circoscritta del paper.

File: `sources/papers/bartetzki1997.md` (schema papers completo) + nuova
concept `concepts/deviazione-ampiezza-probabilita.md` (quadrato 2×2 +
verifica di non-precedenza datata 2026-06-11/12 su CMask, switch ICMS
50%-fissi, AC Toolbox beta-mask, Common Music idioma — registro «non abbiamo
trovato»). Propagazione: `tendency-mask.md` (rinvio senza sovrapposizione),
`refs.bib` (entry aggiornata all'articolo, eccezione Zotero dichiarata),
`bibliography.md`, `index.md`, `overview.md` (proposta 1 + gap chiuso).

---

## [2026-05-27] ingest | concept page deferred-time-tradition

Terza concept page Step 5: `wiki/concepts/deferred-time-tradition.md`. Narrazione tre atti
(vincolo hardware → caduta vincolo → ritorno volontario PGE) con tavola sinottica 12 nodi
cronologici. Sezione precedenti CIM coesistenza RT/differito (Di Scipio 1994, Silvestri 2010,
Arcella/Silvestri 2012, Markidis/Fernández 2016). Legittimazione teorica: economy of selection
(Roads 2012), strumenti non neutri (Arcella/Silvestri 2012), link a [[interactivity-rate]].
Propagazione: index.md, log.md, inbound links da source pages (discipio1991, roads1985,
arcella-silvestri2012, roads2012).

---

## [2026-05-27] lint | review-ingest Step 5 — inbound links + Wegner1997

Review post-ingest Step 5. Lacune identificate e risolte:

1. **Inbound links mancanti dalle source pages.** Aggiunti `[[graphic-score]]` a 6 pagine
   (score-visualizer, roads1985, truax1988, caires2004, roads2021, anatrini2024) e
   `[[interactivity-rate]]` a 4 pagine (discipio1995, vaggione1996,
   solomos2003-ent04-de-loperatoire, solomos2005).

2. **Wegner 1997** (*Why Interaction is More Powerful Than Algorithms*, CACM 40/5) aggiunto
   a `refs.bib` e `bibliography.md` sezione Fonti senza PDF. Referenziato in
   `interactivity-rate.md` riga 70 e in `solomos2003-ent04-de-loperatoire.md` nota 9.

---

## [2026-05-27] ingest | Step 5 — concept pages interactivity-rate + graphic-score

Step 5 di `docs/plans/setup-workspace.md`. Lint wiki eseguito: 5 concept pages già presenti
(tendency-mask, decorrelazione-granulare, micromontage, granulare-deterministico-cim,
sintesi-granulare-sincrona); 4 delle 6 pagine predefinite nel piano non necessarie (DSL YAML,
deferred-time, granular-synthesis, control-hierarchy — coperte da overview.md differenziatori
e concept pages esistenti). 2 nuove concept pages scritte:

1. **`wiki/concepts/interactivity-rate.md`** — ridefinizione CIM di interattività come rate
   di feedback. Sintetizza 5 fonti: Di Scipio 1995 (taxonomy 4-quadrant), Truax 1990
   (gap controllo/percezione), Vaggione 1996 (interaction forte), Solomos/Vaggione 2003
   (triangolarité), Solomos 2005 (concetti operativi). PGE = interactive composition program
   a rate lento (loop lungo). Serve sez. 1 + 6 del paper.

2. **`wiki/concepts/graphic-score.md`** — lineage storico delle rappresentazioni visive per
   sintesi granulare. 10 sistemi da Roads 1978 a PGE. Tavola sinottica anno/sistema/asse Y/
   ruolo/I-O. Doppio differenziatore PGE: asse Y = posizione buffer + inversione di flusso
   (output non input). Serve sez. 4 del paper (primaria) + sez. 2, 6.

Propagazione: `index.md` aggiornato con 2 nuove entry. Wikilink orfano `[[depolipiccialli1988]]`
già corretto in precedente lint (2026-05-24). overview.md non necessita aggiornamento (le concept
pages sintetizzano lineage; overview ospita tesi e differenziatori).
---

## [2026-05-27] restructure | concept page `deferred-time-tradition.md` — promozione Atto 1/2/3 da overview a concept

Creata concept page `wiki/concepts/deferred-time-tradition.md` che promuove la narrazione tre atti di `overview.md` a sintesi multi-fonte stand-alone. Cluster citazionale di 10+ nodi sopra soglia 3-nodi per promozione (4 atto 1: [[roads1978]] [[discipio1991]] [[depoli-piccialli1988]] [[ortosecco-piccialli1989]] [[discipio-tisato1993]]; 4 atto 2: [[truax1988]] [[lippe1993]] [[discipio1995]] [[detintis1995]]; atto 3: [[risset1999]] + PGE; coesistenza: [[discipio1994]] [[silvestri2010]] [[risset1999]]).

Struttura: Definizione (regime compositivo lungo asse rate-di-feedback, non binario tecnico — quote [[discipio1995]] p. 19 per disambiguazione *interactivity ≠ immediate audible output*) · Tre atti con quote pietra-angolare per atto ([[discipio1991]] p. 345 vincolo hardware + [[truax1988]] p. 19 *abandon linear modes* + [[risset1999]] p. 37 *arrow of time and its tyranny*) · Coesistenza RT+deferred come anti-pattern netti CIM ([[discipio1994]] *kairós*/*Zeitwerk* deferred + *Essai du vide* RT; [[silvestri2010]] *Studio Sonoro III* sia RT sia tape; [[risset1999]] *Duet for one pianist* RT + filosofia anti-RT) · Tabella mapping 5 drawback Risset → razionali tecnici PGE (DSL/LSP/score_visualizer/IR pluggable/STEMS) · Relazione PGE come Atto 3 con asse regime temporale ortogonale ad asse controllo statistico/deterministico (eredita primo da Truax 1988, secondo da Roads 1978/Di Scipio 1991, rovesciandone la motivazione) · Citabilità Sez. 1/2/6 · Domande aperte.

Step 5f del piano `docs/plans/setup-workspace.md` chiuso (promozione concept page prevista). Backlink reciproci verso concept page sorella [[granulare-deterministico-cim]] — entrambe tagliano la tradizione lungo un asse indipendente (regime temporale vs tipologia di controllo), domanda aperta su 2×2 in Sez. 2 paper.

File creati: `wiki/concepts/deferred-time-tradition.md`.
Aggiornati: `wiki/index.md` (entry nuova in §Concepts), `wiki/log.md` (questa entry).
Non toccati: `overview.md` (narrazione tre atti già presente con paragrafo Risset 1999 — la concept page sintetizza e amplia, non sostituisce).

---

## [2026-05-27] lint | review-ingest Risset+Pozzi — chiusura lacune

Review degli ingest [[risset1999]] + [[pozzi2016]] (sessione collega stessa data). Schema fisso entrambe le pagine completo; propagazione mancante un solo step (Pozzi → `overview.md`, autodichiarato rinviato a concept page `loop-lungo-cim.md`).

Lacune chiuse in questa sessione:

1. **Pozzi in `overview.md`**: aggiunta riga nuova nella tabella *Sistemi contemporanei (poli compositivi opposti)* dopo Markidis 2016 (stesso volume CIM XXI). Quote pietra-angolare *Breakpoint* p. 194 inserita verbatim, anti-analogia *renounce to control* sez. 4 p. 193, coppia CBCS CIM 2016 target-driven vs exploration-driven con [[markidisfernandez2016]], anti-analogia simmetrica con [[anatrini2024]] (Boids ↔ VAE ↔ deferred), quarto data-point lessico Di Scipio CIM. Backlink reciproco aggiunto nella riga Markidis 2016 (testo "con Pozzi" → "con [[pozzi2016]]"). Concept page `loop-lungo-cim.md` resta rinviata (richiede sintesi 4-nodi multi-fonte).
2. **Domande aperte Pozzi**: appuntate in `docs/plans/next-session.md` sezione nuova *Domande aperte da ingest precedenti*: documentazione post-2016 sistema Pozzi, continuità *iterative compositional strategy Breakpoint* in CIM XXII/XXIII, quadrilatero CIM-CMR del loop iterativo (Pozzi + Vaggione progressive enrichment + Roads economy of selection + Di Scipio osservazione→modifica) per concept page futura.

Lacune non chiuse (non bloccanti):
- `refs.bib` `Risset1999` usa path relativo nel campo `file` come tutti gli altri entry, in disallineamento col workflow add-paper di `CLAUDE.md` che prescrive path assoluto. Convenzione repo prevale, workflow doc disallineato.
- Schema proceedings di `CLAUDE.md` non include *Quote chiave* + *Domande aperte*; `pozzi2016.md` li aggiunge come estensione utile. Drift schema minore.

File modificati: `wiki/overview.md` (riga Pozzi 2016 aggiunta + backlink reciproco Markidis), `docs/plans/next-session.md` (sezione *Domande aperte* nuova), `wiki/log.md` (questa entry).

---

## [2026-05-27] ingest | Risset 1999 *Composing in Real-time?* — fonte filosofica CMR diretta del ritorno volontario al deferred

Ingestione paper Risset (CMR 18/3, pp. 31–39, DOI 10.1080/07494469900640331) — *avvocato del diavolo* contro l'egemonia RT in IRCAM anni '90. Cinque drawback strutturali (complessità, flessibilità, mastering, effimerità, music-for-tape viva) + quattro brani come prove di tecniche non-realizzabili in RT (filtri non-causali, time-stretching che incrocia l'originale, sincronizzazione a submultipli di 20 s, processing armonico voce time-stretched).

**Rilevanza massima per tesi PGE — voce critica CMR 1999 che articola il *ritorno volontario al deferred* 27 anni prima dell'implementazione su laptop.** Quote pietra-angolare p. 37 *"Composition is not — or should not be — a real-time process. [...] Non real-time operation is necessary to free oneself of the arrow of time and its tyranny"* = fonte filosofica diretta per Sez. 1 e Sez. 6. Drawback 3 (mastering, bookkeeping impossibile in RT) = razionale CMR dell'esposizione totale parametri nel DSL YAML; Drawback 4 (effimerità, *perishable memoriless electronic art*) = razionale dell'architettura textual + IR pluggable. Genealogia RT (GROOVE 1970/Synclavier 1974/Chadabe 1981/Disklavier 1989/Manoury *Jupiter*) per Sez. 2. Cita Virilio (*L'art du moteur* 1993) + Borges contro l'*immediate satisfaction* = registro etico-filosofico Sez. 6. Coesistenza compositiva RT+deferred nello stesso autore (*Duet for one pianist* MIT 1989 RT vs filosofia 1999 anti-RT) = pattern condiviso con [[discipio1995]] e [[silvestri2010]].

Citabile Sez. 1 (narrazione tre atti, atto 3 ha precedente filosofico CMR documentato), Sez. 2 (genealogia RT), Sez. 6 (loop lungo contro RT frenzy). **Non** Sez. 3/4 — argomentazione filosofica generale, non discute architetture DSL o notazioni.

File creati: `wiki/sources/papers/risset1999.md`.
Aggiornati: `wiki/sources/bibliography.md` (✓ + Sezioni 1,2,6), `wiki/index.md`, `wiki/overview.md` (paragrafo aggiunto alla *Tesi corrente* dopo la formulazione del *ritorno volontario*: Risset come fonte filosofica CMR diretta + mapping due drawback su contributi PGE + cornice Virilio/Borges).

---

## [2026-05-26] restructure | chiusura debito Zotero — 20 proceedings CIM scritti in refs.bib

Bypass autorizzato del workflow Zotero standard (CLAUDE.md: "i paper individuali citati vengono aggiunti a Zotero manualmente dopo l'ingest"). Utente richiede scrittura diretta in `refs.bib` per sbloccare compilazione `pdflatex`.

**Stato pre-sessione:** 6/20 chiavi proceedings CIM già presenti in `refs.bib` (`Roads1985cim`, `DiScipio1991cim`, `DiScipioTisato1993cim`, `Arcella2012`, `OrtoseccoPiccialli1989`, `Markidis2024cim`, `DePoliPiccialli1988`).

**Aggiunte 14 entry @inproceedings:**
`Lippe1993cim`, `DiScipio1995cim`, `DeTintis1995`, `KellerRolfe1998`, `RolfeKeller2000`, `ValleLombardo2003`, `Rizzuti2006`, `Silvestri2010`, `AgostiniDaubresseGhisi2014`, `ValentiValleServetti2014`, `MarkidisFernandez2016cim`, `Sparano2018`, `Cera2022`, `Anatrini2024`.

Dati estratti da `## Citazione CIM` di ogni pagina wiki `sources/proceedings/`. Pattern entry segue modello `DePoliPiccialli1988`: `booktitle = {Atti del {{N Colloquio}} di {{Informatica Musicale}}}`, `publisher = {AIMI}` (con varianti documentate: CIM X 1993 + XVIII 2010 hanno publisher esteso con istituzione ospitante; XVI Genova ha InfoMus Lab+DIST), `address = {Città}`, `file = {raw/proceedings/<volume>.pdf}`, `langid` per lingua paper (italian/english).

**Lacune note:** `Rizzuti2006` e `RolfeKeller2000` mancano del campo `pages` — paginazione non disponibile nelle wiki pages corrispondenti (PDF OCR scan, `pdftotext` restituisce solo testo senza numerazione). Annotato in `bibliography.md` come da completare in fase scrittura.

**Propagazione:**
- `refs.bib`: 14 entry appese in coda al file (totale @inproceedings ora 25, di cui 20 CIM).
- `bibliography.md` sezione *Debito Zotero*: header riformulato a *RISOLTO 2026-05-26* con nota sul bypass autorizzato e necessità di sincronizzare Zotero a posteriori; aggiunta nota lacune pagine.

**Verifica:** loop sui 20 keys con `grep -c "^@.*{<key>," refs.bib` → 20/20 OK. Compilazione `pdflatex` ora dovrebbe risolvere `\cite{...}` per tutti i proceedings CIM censiti.

---

## [2026-05-26] restructure | concept refresh granulare-deterministico-cim — promozione quarta sotto-famiglia (C, permutation a-causale)

Concept refresh richiesto come prosecuzione dopo che proceedings ingest è sostanzialmente completo (cfr. opzione *Concept refresh + lint* scelta in `docs/plans/prosegui-con-ingest-proceedings-magical-manatee.md`). [[valenti-valle-servetti2014]] (CIM XX 2014, ingestita 2026-05-26) era già marcata dall'ingest log come «quarta variante CIM di rifiuto della tendency mask — deterministico a-causale», ma il concept page `concepts/granulare-deterministico-cim.md` conteneva ancora due sotto-famiglie + nota in *Domande aperte* «esiste un quarto data-point del filone tra 2012 e 2024?». Promozione formale chiude il debito.

**Modifiche `concepts/granulare-deterministico-cim.md`:**
1. Definizione filone: «due sotto-famiglie» → «tre sotto-famiglie».
2. Nuova sezione `### (C) Combinatoria a-causale — permutazione di chunk` con definizione del meccanismo (nessuna iterazione `xn→xn+1`, nessuna combinatoria su sub-vettori di oscillatori paralleli, pattern di riordinamento dichiarato a priori, chunk size = `fs/fp`); single data-point [[valenti-valle-servetti2014]] con quote pp. 35 sez. 1 contro il canone granulare-stocastico-envelopato + ref [1] Roads *Microsound* contrapposto.
3. Tabella `## Relazione con PGE` estesa da 3 a 4 colonne (Sotto-famiglie A / B / C / PGE); riga *Generatore valore* sotto-famiglia C = «pattern di permutazione fissato a priori»; *Memoria fra grani* = «no (lookup su pattern dichiarato)»; *Grano come entità* = «prodotto incidentale (chunk a confine fisso)»; *Asse di controllo* = «sequenza dichiarata `fp` + chunk_size».
4. `## Cluster sociologici intersecanti`: bullet *Magistero Di Scipio* riformulato come «sotto-famiglie A+B» (la sotto-famiglia C resta fuori dal cluster); nuovo bullet *Continuità autoriale Valle CIM (sotto-famiglia C)* — Valle attraversa due famiglie granulari CIM in 11 anni ([[valle-lombardo2003]] formale CAC offline + [[valenti-valle-servetti2014]] permutation a-causale), unica continuità autoriale del filone deterministico fuori dal magistero Di Scipio.
5. `## Citabilità nel paper CIM 2026` sezione 2: citazione collettiva del filone aggiornata a quattro lavori (Di Scipio 1991 + Rizzuti 2006 + Silvestri 2010 + Valenti/Valle/Servetti 2014); formulazione «stesso obiettivo (rifiuto del controllo stocastico), tre meccanismi formali distinti».
6. `## Domande aperte`: rimossa domanda «esiste un quarto data-point tra 2012 e 2024?» (risposto); riformulato bullet *Sotto-famiglia B ha un solo data-point* → «Sotto-famiglie (B) e (C) hanno entrambe un solo data-point CIM al 2026-05» con investigazione mirata per ciascuna; aggiornata nota Markidis 2024 come *non* riducibile a nessuna delle tre sotto-famiglie (ecosistemico signal-driven, famiglia distinta).

**Propagazione minima:**
- `index.md`: entry concept page riscritta da «due sotto-famiglie» → «tre sotto-famiglie» con elenco esplicito A/B/C + nota cluster sociologico A+B (Di Scipio) vs C (Valle).
- `valenti-valle-servetti2014.md`: punto 2 *Analogia con PGE* aggiornato — i due wikilink esistenti [[silvestri2010]] + [[discipio1991]] riformulati come *terza sotto-famiglia del filone [[granulare-deterministico-cim]]* (link al concept page consolidato precedentemente mancante).

**Non toccato (intenzionalmente):** `overview.md` (sezione *Differenziatori* riferisce già il filone con citazione collettiva al livello discorsivo — la sotto-famiglia in più non altera il differenziatore #8); `cim-survey.md` entry 2014 (già completa); `bibliography.md` (chiave presente); `refs.bib` (regola CLAUDE.md: solo Zotero).

**Workflow lint (eseguito contestualmente — report inline alla sessione):**
- Wikilink rotti rilevati e risolti: `[[depolipiccialli1988]]` (residuo della rename 2026-05-21 papers/→proceedings/) presente in `rizzuti2006.md` (riga 34) e `ortosecco-piccialli1989.md` (righe 29 e 51) — sostituito con `[[depoli-piccialli1988]]` in entrambi i file. `[[markidis2024]]` da [[anatrini2024]] già risolto in precedente lint (2026-05-22). `[[granulare-deterministico-cim]]` ora linkato da [[valenti-valle-servetti2014]] (target esiste). Dopo fix: nessun wikilink rotto residuo nel wiki.
- Pagine orfane: nessuna fra `wiki/sources/proceedings/` e `wiki/sources/papers/` priva di inbound link da `index.md` (verifica per ispezione del file `index.md`, ogni file ha entry dedicata).
- Concept candidates non ancora promossi: `interactivity-rate` (citato da [[discipio1995]] + [[truax1990]] + [[vaggione1996]] + [[discipio-tisato1993]], gap esplicito in `overview.md`) e *meta-GUI come partitura* (lineage Matthews/UPIC/Hyperscore/WavePilot, emerso da [[anatrini2024]]). Entrambi documentati in `overview.md` *Gap da colmare* e in `setup-workspace.md` Step 5 — non promossi in questa sessione per restare nello scope concept refresh sul deterministico.
- Debito Zotero `refs.bib`: 20 chiavi proceedings ingestite ma non ancora in `refs.bib` — stato invariato (gestione settimana 2 piano scrittura).

---

## [2026-05-26] restructure | review-ingest CIM XX 2014 — backlink Valle traiettoria autoriale

Review-ingest sul doppio ingest CIM XX 2014 (entry sotto). Lacuna identificata: continuità autoriale Valle CIM 11 anni citata da [[valenti-valle-servetti2014]], `overview.md`, `cim-survey.md`, ma `valle-lombardo2003.md` non riferiva [[valenti-valle-servetti2014]] → asimmetria link bidirezionale.

Fix: aggiunto paragrafo finale a sezione *Posizionamento storico* di [[valle-lombardo2003]] che esplicita traiettoria 2003 → 2014 (sistema formale CAC offline → DSP sperimentale real-time SC) come datapoint sulla varietà del granulare CIM italiano nella stessa autorialità.

Lacune residue accettate (sotto soglia):
- Lambda loop CAGE come pattern compositivo non concettualizzato (singolo nodo).
- Lineage CAC simbolica CIM (OpenMusic/PatchWork → bach/cage) non promosso a concept page (1 nodo CIM).
- `concepts/granulare-deterministico-cim.md` non esteso con quarta sotto-famiglia *deterministico a-causale* (Permutation = 1 nodo, soglia promozione 3).

---

## [2026-05-26] ingest | proceedings CIM XX 2014 — Agostini/Daubresse/Ghisi (cage) + Valenti/Valle/Servetti (Permutation)

Ingest doppio dello stesso volume CIM XX 2014 per chiudere completamente il volume (entrambi i paper granular-related rilevanti mai promossi al piano originale, censiti in [[cim-survey]] ma non ingestiti). Approvato in `docs/plans/prosegui-con-ingest-proceedings-robust-spark.md` opzione raccomandata.

Estrazione testo via `pdftotext -layout` su `raw/proceedings/2014_CIM_XX_Atti.pdf`:
- CAGE: pp. 17–22 (range righe 1728–2100)
- Permutation: pp. 35–40 (range righe 3079–3500)

Pagine create con schema fisso completo (10 sezioni):
- `wiki/sources/proceedings/agostini-daubresse-ghisi2014.md`
- `wiki/sources/proceedings/valenti-valle-servetti2014.md`

**Contributi argomentativi acquisiti (CAGE):**

1. **Prima occorrenza CIM di *granulazione simbolica* come categoria distinta da *granulazione audio*** — quote p. 19 *"cage.granulate è un motore di granulazione simbolica. I parametri della granulazione sono gli stessi del corrispondente processo elettroacustico: l'intervallo di tempo tra due grani, la durata di ogni grano, la regione di partitura da cui i grani devono essere estratti"*. I tre parametri canonici (IOT, durata grano, regione sorgente) di Roads/Truax/PGE sono **identici** in CAGE, ma il "grano" è una nota simbolica MIDI con altezza+durata, non porzione di campioni audio. Categoria *granulazione* applicata a due ontologie disgiunte. Argomento di delimitazione esplicita per Sezione 2 paper CIM 2026: PGE = piano audio sample-based, CAGE = piano simbolico.

2. **Real-time symbolic vs deferred audio non comparabili** — CAGE opera real-time perché manipola entità simboliche (note discrete) il cui ritmo di aggiornamento è macro-evento (≪ 1 kHz); PGE opera offline perché manipola campioni audio (44/48 kHz) in stream multipli. Posta computazionale di tre ordini di grandezza diversa. Chiarimento utile per Sezione 1 narrazione tre atti: il framing real-time/deferred riguarda il piano audio.

3. **Convergenza obiettivo (modificabilità strumenti) via tecnologica opposta** — CAGE: astrazioni Max ispezionabili e modificabili dall'utente (sez. 1 *"open source intrinsecamente"*). PGE: DSL testuale + Language Server. Stessa vocazione pedagogica per due tecnologie opposte. Argomento di Sezione 3 paper.

4. **Lineage CAC OpenMusic/PatchWork → bach/cage Max** — cage.profile ispirata a libreria Profile [4]; cage.rm/cage.fm a libreria Esquisse [5,6]; bach a tradizione Lisp/Patchwork. Lineage CIM CAC simbolica distinto dal lineage CIM granular-audio (Roads/Truax/Di Scipio) e dal lineage CIM concatenative ([[markidisfernandez2016]]). CAGE = terza famiglia CIM 2014.

5. **Modello stilistico CIM da non imitare** — 6 pp / 13 refs / catalogo descrittivo famiglia-per-famiglia (sez. 3 enciclopedica) / no sezione conclusioni argomentativa. Versione italiana di paper ICMC 2014 parallelo. PGE paper CIM 2026 deve restare argomentativo, non catalogo.

**Contributi argomentativi acquisiti (Permutation):**

1. **Anti-analogia tecnica esplicita formulata dagli autori contro il canone granulare-stocastico-envelopato** — quote sez. 1 *"most granulation approaches operate by applying an envelope, thus eliminating most of the discontinuities. Moreover, grains are typically scattered in time following some stochastic distributions. On the contrary, in permutation synthesis time discontinuities are the main feature, and the scrambling process is organised following a precise time-pattern"*. Inversione del ruolo dell'envelope (eliminare vs enfatizzare discontinuità) + pattern deterministico vs scattering stocastico. Polo opposto a `WindowGenerator` + `DistributionStrategy` PGE su **entrambi** i meccanismi-cardine. Roads *Microsound* citato come riferimento contrapposto in ref [1].

2. **Quarta variante CIM di rifiuto della tendency mask** — affianca [[discipio1991]] (caotico-iterativo `xn+1=f(xn)`), [[rizzuti2006]] (logistica), [[silvestri2010]] (combinatorio MUX): permutation = deterministico **a-causale** (no memoria di stato, no funzione iterata; pattern fissato a priori). Sotto-famiglia distinta nel quadro `concepts/granulare-deterministico-cim.md` — potenzialmente promovibile a quarta sotto-famiglia se si decide di estendere il concept page.

3. **Continuità autoriale Valle CIM (11 anni)** — secondo paper CIM granular-related di Andrea Valle dopo [[valle-lombardo2003]] (GeoGraphy *A Two-Level Method to Control Granular Synthesis*). Traiettoria 2003 → 2014: da architettura sistema formale CAC offline a tecnica DSP sperimentale real-time SC. Datapoint sulla varietà del granulare CIM italiano nella stessa autorialità.

4. **Time-quantisation error formalizzato come duale di amplitude quantisation** — sez. 2.2: `chunk_size = fs/fp` arrotondato all'intero, errore (globally) crescente con `fp`, decrescente con `fs`. Pattern argomentativo trasferibile a discussione PGE del rapporto fra rate di sintesi e risoluzione di `density`/`fill_factor` (quantizzazione `IOT = 1/density` su grid di sample del renderer).

5. **Modello stilistico CIM tool paper DSP minimale** — 6 pp / 6 refs (1 ref/pp.). Limite inferiore assoluto CIM XX per tool paper DSP. Densità bassa giustificata dalla natura tecnico-formale del paper (formule analitiche dominano). PGE paper CIM 2026 deve restare sopra (target 9-21 ref) per postura argomentativa.

**Coppia stesso volume CIM XX 2014** — datapoint CIM 2014 che il canone granulare audio è **abbastanza consolidato da generare ramificazioni e contro-tecniche referenziali**: CAGE estende la categoria al piano simbolico, Permutation la inverte sull'asse stocastico/deterministico. Entrambi i paper si posizionano **rispetto** al canone Roads/Truax pur restando fuori da esso. Argomento utile per Sezione 2 paper PGE: il canone granular audio nel 2014 è abbastanza stabile da essere oggetto di delimitazione esplicita.

**Sezioni paper CIM 2026 mappate:**
- Sezione 2 (Sintesi granulare): CAGE come anti-analogia ontologica (categoria *granulazione* su ontologie disgiunte audio vs simbolico); Permutation come anti-analogia tecnica esplicita formulata dagli autori contro il canone Roads.
- Sezione 3 (PGE architettura): CAGE come convergenza obiettivo (modificabilità) per via tecnologica opposta (astrazioni Max vs DSL+LSP).

**Propagazione completata:**
- `overview.md`: aggiunte due righe *2014 | Agostini/Daubresse/Ghisi (CIM XX)* e *2014 | Valenti/Valle/Servetti (CIM XX)* nella tabella precursori subito dopo riga 2012 Arcella/Silvestri.
- `cim-survey.md`: ampliate entry 2014 con link `[[agostini-daubresse-ghisi2014]]` e `[[valenti-valle-servetti2014]]` + paginazione esatta Permutation 35–40; aggiunti riferimenti in sezione *Non comparabili (real-time)*.
- `bibliography.md`: aggiunte righe `AgostiniDaubresseGhisi2014` e `ValentiValleServetti2014` nella tabella Proceedings + voci corrispondenti in *Debito Zotero* (conteggio: 18 → 20 chiavi).
- `index.md`: aggiunte entry sintetiche per entrambe le pagine subito prima di `markidisfernandez2016.md` (ordine cronologico).

Nessuna concept page nuova creata. Potenziale estensione `concepts/granulare-deterministico-cim.md` con quarta sotto-famiglia (permutation deterministico a-causale) — al momento Valenti-Valle-Servetti è singolo nodo CIM della categoria, sotto soglia 3 nodi per promozione standalone (cfr. nota Pozzi 2016 in `docs/plans/setup-workspace.md`). Se in scrittura sezione 2/concept refresh si decide di estendere, basta aggiungere quarta voce al concept page esistente.

Resta aperto:
- Pozzi 2016 (Boids su CataRT, CIM XXI) non ingestito — singolo nodo multi-agent, sotto soglia.
- Santini 2008 (CIM XVII) non ingestito — fuori scope audio→video.
- Debito Zotero: 20 chiavi proceedings da generare in `refs.bib` (settimana 2 piano scrittura).

---

## [2026-05-24] restructure | review-ingest Rolfe-Keller 2000 — correzioni post-review

Review ingest `rolfekeller2000.md` eseguita il 2026-05-24. Tre lacune risolte:

1. **Rename filename** — `rolfekeller2000.md` → `rolfe-keller2000.md` per coerenza con convenzione `autore1-autore2-anno.md` (cfr. `keller-rolfe1998.md`, `discipio-tisato1993.md` ecc.). Tutti i link interni aggiornati in `overview.md`, `log.md`, `index.md`, `cim-survey.md`.

2. **Concept page decorrelazione** — creata `wiki/concepts/decorrelazione-granulare.md`: sintesi cross-source della filiazione CIM → CMR ([[keller-rolfe1998]] ontologia → [[rolfe-keller2000]] framework formale 3 livelli → [[vaggione2002]] attributo morfologico di prima classe) + mapping completo su componenti PGE + sezioni paper CIM 2026. `index.md` aggiornato.

3. **Pagine mancanti (pp. nella citazione)** — non risolvibile in questa sessione (PDF OCR, numerazione non recuperabile via `pdftotext`). Segnalato come da completare quando il PDF originale è disponibile in formato leggibile o via indice del volume.

---

## [2026-05-24] ingest | proceedings Rolfe-Keller 2000 — Decorrelation as a By-Product CIM XIII

Ingest del paper *Decorrelation as a By-Product of Granular Synthesis* (Chris Rolfe + Damian Keller, XIII CIM 2000, Poster Session II, ~3–4 pp., 5 refs inline senza sezione References esplicita). Stessa coppia di autori di [[keller-rolfe1998]] con ordine invertito.

Estrazione testo via `pdftotext -layout` su `raw/proceedings/2000_CIM_XIII_Atti.pdf` (range righe 3070–3260). Numerazione pagine non recuperabile via pdftotext (PDF Adobe Acrobat Paper Capture, OCR scan); riferimenti a sezioni 1/2/3 nel testo.

Pagina creata: `wiki/sources/proceedings/rolfe-keller2000.md` con schema fisso completo (citazione / categoria / argomento / sistema / analogia PGE con tabella mapping / posizionamento storico / note stilistiche / 5 quote chiave / sezioni paper CIM 2026).

**Contributi argomentativi acquisiti:**

1. **Primo paper CIM granulare *meta-livello*** — Rolfe-Keller 2000 non descrive un sistema specifico ma propone un *framework di analisi* della GS. È l'unico paper CIM granulare ingestito finora che opera a livello meta (analizza il behavior dei modelli, non li implementa). Precedente importante per CIM 2026 sez. 4 dove la partitura PGE è descritta non come strumento di un brano ma come *framework* di lettura di qualunque rendering granulare.

2. **Anello cronologico CIM → CMR sulla decorrelazione** (filiazione esplicita in 3 tappe):
   - 1998 [[keller-rolfe1998]] (CIM XII, *The Corner Effect*): ontologia stream/waveform/pointer/event — entità nominate
   - **2000 Rolfe-Keller (CIM XIII)**: ontologia diventa base per teoria misurabile della correlazione su 3 livelli ortogonali
   - 2002 [[vaggione2002]] (CMR): generalizzazione di decorrelation da fenomeno tecnico granulare a *attributo morfologico-spaziale di prima classe* del dominio compositivo
   Il paper Rolfe-Keller 2000 è anello mancante CIM **fra vocabolario granular tecnico (1998) e vocabolario compositivo Vaggione (2002)** — rende quantificabile ciò che 2 anni dopo Vaggione costruirà come dimensione compositiva autonoma. PGE eredita tutte e tre le tappe (ontologia → strumenti misurabili → dignità compositiva).

3. **Tassonomia 3 livelli di correlazione = 3 assi PGE** — formalizzazione esplicita di tre livelli ortogonali su cui PGE opera con strumenti diversi:
   - *grain-to-grain* (intra-stream) → `PointerController.speed_ratio` + deviazione per-grano + `Envelope` range
   - *cross-channel/stream* (inter-stream) → `VoiceManager` con dephase strategy + N stream YAML-dichiarati
   - *instance/event* (inter-execution) → `DistributionStrategy` (uniform/gaussian), ogni run produce un *instance* decorrelato
   Quote sez. 3 *"Varying a given stream delay by a random amount introduces phase-shifting causing the value k [cross-correlation] to vary dynamically from -1.0...1.0"* = formulazione esplicita CIM 2000 di come variazione random produce decorrelazione misurabile. Referente CIM diretto per giustificare la scelta architetturale PGE (`DistributionStrategy` + `dephase` come strumenti di controllo della correlazione cross-stream).

4. **Trade-off transparency vs decorrelation come dimensione del DSL** — Rolfe-Keller (sez. 3, *"forgoing the goal of transparency [...] in favour of a thickening or chorusing"*) scelgono *un polo* (decorrelation per chorusing real-time); PGE espone *entrambi i poli* nel DSL YAML perché il deferred time abilita il confronto diretto fra rendering. Argomento di Sezione 6 (conclusioni): scelta compositiva che il deferred time permette di esplorare via re-rendering successivi vs scelta single-shot real-time.

5. **Modello stilistico CIM 2000 riusabile** — sequenza argomentativa *definizione matematica formale → tre livelli ortogonali → mapping su parametri implementativi* è riutilizzabile per descrivere il `score_visualizer` in sez. 4 (definizione asse Y → tre livelli di visualizzazione → mapping su parametri Stream). Primo paper CIM granulare che apre con definizione matematica formale (cross-correlation function $F(\tau)$).

6. **Conferma CIM 2000 di parameter range come pattern condiviso** — Rolfe-Keller sez. 2 (*"Most published granular synthesis (GS) models also allow for stochastic variation of control parameters, usually as a parameter range specification, as does our model"*) documenta che il pattern *parameter range* (Envelope center+range PGE) era già condiviso fra modelli GS nel 2000. Rafforza il differenziatore #8 (tendency mask): non solo Truax 1988 → ICMS 1993 → ISPW 1993 → IRIS-MARS 1995, ma anche Rolfe-Keller 2000 documenta la canonicità del pattern fra modelli pubblicati.

**Sezioni paper CIM 2026 mappate:**
- Sezione 2 (Sintesi granulare): tassonomia 3 livelli di correlazione come framework teorico CIM 2000; anello cronologico fra [[keller-rolfe1998]] e [[vaggione2002]] sulla decorrelazione.
- Sezione 3 (PGE architettura): mapping diretto Rolfe-Keller → PGE (`VoiceManager` + dephase + `DistributionStrategy` come implementazione del modello *decorrelation explicit and variable*); referente CIM per la scelta architetturale.
- Sezione 4 (Partitura grafica): modello stilistico (sequenza definizione formale → livelli ortogonali → mapping). Quote *"tuned by ear to the desired result"* come anti-citazione: PGE rende visibile *prima* dell'ascolto ciò che Rolfe-Keller affidano al solo orecchio in real-time.
- Sezione 6 (Conclusioni): trade-off transparency vs decorrelation come esempio di scelta compositiva esplorabile in deferred time.

**Propagazione completata:**
- `overview.md`: aggiunta riga *2000 | Rolfe, Keller (CIM XIII)* nella tabella precursori (subito dopo Keller-Rolfe 1998, prima di Vaggione 1991/1996/2002/2003); esteso differenziatore #7 (per-grain effects / décorrélation) con paragrafo sull'anello cronologico CIM 1998 → CIM 2000 → CMR 2002 sulla decorrelazione, esplicitando le tre tappe ereditate da PGE.
- `cim-survey.md`: ampliata entry 2000 Rolfe-Keller (era 2 righe minime) con tassonomia 3 livelli, definizione matematica, modello reference (N stream + delay tap + pairing), trade-off transparency/decorrelation, anello cronologico → CMR Vaggione; aggiunto rinvio in sezione *Non comparabili (real-time)* con ruolo *primo paper CIM granulare meta-livello + anello CIM intermedio decorrelation*.
- `bibliography.md`: aggiunta riga `RolfeKeller2000` nella tabella Proceedings con sezioni paper [2, 3, 4, 6]; aggiunta voce corrispondente in *Debito Zotero* (conteggio: 14 → 15 chiavi).
- `index.md`: aggiunta entry sintetica `rolfe-keller2000.md` subito dopo `keller-rolfe1998.md` (coerenza con tabella precursori).

Nessuna concept page nuova creata. Concept *correlation/decorrelation 3 levels* potenzialmente promuovibile a concept page autonoma — già coperto a sufficienza nella tabella precursori + differenziatore #7; ulteriore consolidamento se concept rilevante in fase di scrittura sezione 3/4 del paper.

---

## [2026-05-22] ingest | proceedings De Tintis 1995 — GRAINS IRIS-MARS CIM XI

Ingest del paper *GRAINS: a software for real-time granular synthesis and sampling running on the IRIS-MARS workstation* (Raffaele de Tintis, XI CIM 1995, pp. 220–224, 9 refs).

Estrazione testo via `pdftotext -layout` su `raw/proceedings/1995_CIM_XI_Atti.pdf` (range righe 8990–9280).

Pagina creata: `wiki/sources/proceedings/detintis1995.md` con schema fisso completo (citazione / categoria / argomento / sistema / analogia PGE / posizionamento / note stilistiche / sezioni paper / 5 quote chiave).

**Contributi argomentativi acquisiti:**

1. **Precursore architetturale CIM 1995 di *stream come unità di prima classe*** — quote p. 221 *"Sound computation is made by four identical algorithms that calculate quasi-synchronous granular synthesis, with the output from every algorithm being a stream with the grains following one after the other"* = definizione esplicita CIM 1995 di `stream = output di un algoritmo granulare = sequenza ordinata di grani`. Precursore terminologico diretto del `Stream` PGE. I 4 algoritmi GRAINS = 4 stream identici controllati indipendentemente; PGE generalizza a N stream YAML-dichiarati.

2. **Precursore architetturale del workflow STEMS PGE** — quote p. 222 *"every algorithm has three outputs, each with an independent gain controllable in real-time"* = per-stream multi-output routing con gain indipendente. Stesso *taglio per stream* del rendering STEMS PGE (rendering separato per stream + bouncing per accesso a ogni livello individualmente). De Tintis usa i 3 output per ramificare verso modelli post-processing (filter bank VOSIM-like + waveguide); PGE usa lo split per cache incrementale + export DAW. La *separazione esplicita del flusso per stream* come oggetto compositivo è il punto comune.

3. **Anti-analogia centrale *data reduction vs data exposure*** — De Tintis sez. 2 *Data Reduction* dedica l'intera sezione a giustificare la riduzione drastica dei parametri come *requisito* del real-time MIDI («the reduction of data is a fundamental goal for the effectiveness and the efficiency for the composer who can work with high level parameters», p. 221). PGE inverte la postura: il tempo differito permette di *non* ridurre i parametri ma esporli completamente nel DSL YAML, perché il loop lungo assorbe il costo cognitivo. Argomento di Sezione 2 e Sezione 3 del paper CIM 2026: due risposte opposte allo stesso problema di density-of-control, prodotte sullo stesso volume di Atti del 1995.

4. **Terzo data-point CIM tendency mask Truax 1988** — De Tintis p. 221 cita esplicitamente *"the tendency masks introduced by Truax"* come stato dell'arte fra «*important criteria [...] to better organize the high number of variables*». Terza piattaforma real-time italiana (IRIS-MARS, dopo ICMS 1993 e ISPW 1993) che documenta nel proprio paper CIM l'adozione canonica del modello. La sequenza ICMS 1993 + ISPW 1993 + IRIS-MARS 1995 mostra che entro due anni dal modello originale Truax 1988 la tendency mask era nomenclatura standard CIM. Rinforza differenziatore #8 in `overview.md` da doppio a triplo data-point.

5. **Lineage VOSIM italiano CIM** — De Tintis cita esplicitamente De Poli/Piccialli 1988 (CIM VII) + De Poli/Piccialli MIT 1991. I 3 output per algoritmo (clean / 3-filter bank stile VOSIM / waveguide) ereditano direttamente il lineage VOSIM/Rodet già attivo nella tradizione CIM offline italiana ([[depoli-piccialli1988]], [[ortosecco-piccialli1989]]). De Tintis 1995 = anello mancante 1995 tra CIM 1988/89 (offline, forme d'onda pitch-synchronous) e CIM 2018 [[sparano2018]] (real-time quasi-sincrono Max/MSP+Gen) — punto medio del lineage italiano *granular quasi-sincrono*.

6. **Coppia stesso volume CIM XI 1995 — polarizzazioni *synthesis vs sampling*** — [[discipio1995]] (Kyma/PODX-DMX1000, granular sampling, ricorsione + time-shifting, brano *Hybris* 1994 / *Essai du vide* 1993) + [[detintis1995]] (IRIS-MARS, granular synthesis classica VOSIM-like, stratificazione + 3-output routing). Doppia uscita CIM 1995 mostra che il real-time granulare era *istituzionalizzato* in CIM 1995 in *entrambe* le accezioni della tassonomia [[lippe1993]] (synthesis = forme d'onda sintetiche; sampling = porzioni di sample). Rafforza l'argomento del paper CIM 2026 che il ritorno volontario PGE 2026 al deferred è una scelta postuma alla disponibilità del real-time.

7. **Terminologia *horizontal/vertical density*** — pp. 221–222 *"horizontal density [...] vertical density dicidmg how many algorithms are active at the same time controlling the stratification of the sonic material"*. Doppia direzione del controllo granulare (asse tempo di un singolo stream + asse stratificazione fra stream) come due gradi di libertà ortogonali. Terminologia riutilizzabile per descrivere il `score_visualizer` PGE come visualizzazione simultanea della densità orizzontale (asse tempo) + stratificazione verticale (asse Y = posizione buffer + sovrapposizione stream).

**Sezioni paper CIM 2026 mappate:**
- Sezione 1 (Introduzione): atto 2 narrazione tre-atti — terzo data-point CIM 1995 di sistemi real-time granulari italiani (con [[discipio1995]] stesso volume); doppia uscita CIM XI 1995 mostra istituzionalizzazione real-time granulare.
- Sezione 2 (Sintesi granulare): lineage VOSIM italiano CIM (1988 De Poli/Piccialli → 1989 Ortosecco/Piccialli → 1995 De Tintis); terzo data-point CIM tendency mask; coppia *granular sampling vs granular synthesis* (De Tintis = synthesis classica, [[discipio1995]] = sampling).
- Sezione 3 (PGE architettura): anti-analogia *data reduction* (De Tintis 1995) ↔ *data exposure* (PGE 2026); conferma CIM 1995 del concetto *stream* come unità di organizzazione (4 stream identici GRAINS → N stream YAML PGE).
- Sezione 4 (Partitura grafica): terminologia *horizontal/vertical density* utilizzabile per descrivere il `score_visualizer` PGE.

**Propagazione completata:**
- `overview.md`: aggiunta riga *1995 | De Tintis (CIM XI)* nella tabella precursori (prima della riga Di Scipio 1995, perché ordinata per anno ma De Tintis è il polo opposto sull'asse data reduction); aggiornato differenziatore #8 (tendency mask) da doppio a triplo data-point CIM 1993–95 (ICMS + ISPW + IRIS-MARS).
- `cim-survey.md`: ampliata entry De Tintis 1995 (era 2 righe minime) con pagine, architettura 4-algoritmi/3-output, MIDI control, horizontal/vertical density, tendency mask reference, link [[detintis1995]]; aggiornato rinvio in sezione *Non comparabili (real-time)* con precisazione del ruolo (terzo data-point tendency mask + lineage VOSIM + coppia *synthesis vs sampling* con [[discipio1995]]).
- `bibliography.md`: aggiunta riga `DeTintis1995` nella tabella Proceedings con sezioni paper [1, 2, 3, 4]; aggiunta voce corrispondente in *Debito Zotero* (conteggio: 14 → 15 chiavi).
- `index.md`: aggiunta entry sintetica `detintis1995.md` subito dopo `discipio1995.md` (stesso volume CIM XI 1995).

Nessuna concept page nuova creata. Anti-analogia *data reduction vs data exposure* potenzialmente promuovibile a concept page autonoma se altri proceedings real-time confermano il pattern.

---

## [2026-05-22] lint | review ingest Anatrini 2024 — risolto wikilink orfano

Review ingest [[anatrini2024]] (sessione separata collega). Verdetto: schema fisso completo, propagazione completa (overview / cim-survey / bibliography / index / log). Una lacuna risolta:

- Wikilink orfano `[[markidis2024]]` in `anatrini2024.md` sezione *Posizionamento storico* — pagina `markidis2024.md` non esistente (Markidis 2024 censito solo come menzione in `cim-survey.md` sez. 2024). Sostituito con riferimento testuale esteso a `cim-survey.md` (no wikilink) per preservare semantica del confronto senza link rotto. `setup-workspace.md` step 4 punto 7 prevede 1–2 paper tool/sistema CIM 2024; Markidis non rientra in quel taglio (live electronics ecosystemic, non tool paper), quindi pagina dedicata non pianificata.

Nota calibratura non bloccante: «modello stilistico CIM 2024» nel log Anatrini generalizza da n=1; mantenere come ipotesi, da confermare se secondo paper CIM 2024 verrà ingerito.

Concept candidate emersa dall'ingest, non ancora scritta: *meta-GUI come partitura* (lineage Matthews Graphic I → UPIC → Hyperscore → WavePilot → score_visualizer PGE) — coperta da Step 5 piano se sopravvive lint.

---

## [2026-05-22] ingest | proceedings Anatrini 2024 — WavePilot CIM XXIV (chiude gap CIM 2024)

Ingest del paper *WavePilot: Framework multidimensionale per l'esplorazione dello spazio parametrico di strumenti digitali* (Alessandro Anatrini, XXIV CIM 2024, pp. 129–135, Session 3 — Tools and platforms, 25 refs).

Estrazione testo via `pdftotext -f 164 -l 171` su `raw/proceedings/2024_CIM_XXIV_Atti.pdf` (113 MB, 187 pp.).

Pagina creata: `wiki/sources/proceedings/anatrini2024.md` con schema fisso completo (citazione / categoria / argomento / sistema / analogia PGE / posizionamento / note stilistiche / sezioni paper / 5 quote chiave).

**Contributi argomentativi acquisiti:**

1. **Polo CIM 2024 dell'esplorazione parametrica via deep learning** — VAE per riduzione dimensionale parametri DMmI + meta-GUI browser + interpolazione RBF. WavePilot opera su plugin VST commerciali (Ob-Xd 83 parametri) trattati come black box; PGE opera su DSL YAML strutturato (white box). Anti-analogia simmetrica su quattro assi ortogonali (black/white box, riduzione/esposizione dimensionalità, real-time gestuale/deferred declarativo, GUI input/partitura output).

2. **Convergenza di obiettivo / divergenza tecnologica** — Anatrini p. 130 enuncia esplicitamente lo stesso scopo del loop lungo PGE («superare la tradizionale separazione tra il processo di programmazione dei parametri della sintesi sonora e l'attività compositiva in sé»). Le vie tecnologiche sono opposte: WavePilot accetta dimensioni latenti *entangled* per controllo intuitivo, PGE espone il dominio parametrico per controllo deterministico-stocastico esplicito. Argomento forte per Sezione 2 (panorama) e Sezione 3 (architettura) del paper CIM 2026.

3. **Anti-analogia inversione di flusso, raddoppio di [[valle-lombardo2003]]** — La meta-GUI WavePilot come *spazio di controllo* (compositore naviga → suono) è analogo concettuale del *space actant* GeoGraphy; il score_visualizer PGE è *output diagnostico read-only* (compositore legge → riflessione). Doppio data-point CIM (Valle/Lombardo 2003 + Anatrini 2024) per consolidare differenziatore #2 del paper.

4. **Modello stilistico CIM 2024 per tool paper** — Pattern *cornice teorica = una sezione propria* (sez. 2 *Contesto* di Anatrini, 2.1 *Meta-GUI come partitura* + 2.2 *Perdere il controllo per acquisire complessità*) prima dell'architettura. Densità citazionale 25 ref / 7 pp. mista informatica musicale (NIME/SMC/ICMC/CMJ) + filosofia/STS (Di Scipio, Borgdorff, Tomás) + machine learning (arXiv VAE/normalizing flows). Apertura motivazionale (progetto biografico Healing Soundscape) + chiusura su sviluppi futuri. Bibliografia *mista* utile per il paper CIM 2026 (target 9–21 ref) con copertura informatica musicale + Vaggione/Di Scipio + tooling. Calibratura tono CIM 2024 acquisita.

5. **Lineage CIM/CMJ *meta-GUI come partitura*** — Anatrini sez. 2.1 cita Matthews Graphic I (1968) → UPIC Xenakis → Hyperscore Farbood (2001) → Pearse et al. SMC 2019 come precedenti della meta-GUI come strumento compositivo di alto livello. Materiale utile per Sezione 4 del paper se si vuole inserire una nota sul ruolo storico della meta-GUI come partitura in informatica musicale (e quindi consolidare il differenziatore score_visualizer come *output* anziché *input*).

**Propagazione:**

- Aggiornata tabella *Sistemi contemporanei (poli compositivi opposti)* in `overview.md` con riga 2024 Anatrini (anti-analogia simmetrica su 4 assi, doppio data-point inversione di flusso con [[valle-lombardo2003]], modello stilistico CIM 2024). Aggiornata sezione *Gap da colmare*: gap CIM 2024 chiuso.
- Aggiornato `cim-survey.md` sezione *2024 — XXIV CIM* (Anatrini aggiunto come paper non granulare in senso stretto ma direttamente rilevante per il posizionamento PGE) + lista *Non comparabili (real-time)*.
- Aggiornato `bibliography.md`: `[CIM2024-tbd]` → `Anatrini2024`, ✓ ingest, sezioni 2/3/4/6. Aggiunto a *Debito Zotero* (chiavi da generare 13 → 14) con entry completa.
- Aggiornato `index.md` con entry sintetica `anatrini2024.md`.

Nessuna concept page nuova creata. Concept candidate emersa dall'ingest (non ancora scritta): *meta-GUI come partitura* — categoria che attraverserebbe Matthews/UPIC/Hyperscore/WavePilot/PGE score_visualizer, utile per Sezione 4 del paper.

---

## [2026-05-22] ingest | proceedings Lippe 1993 — Real-time Granular Sampling ISPW IRCAM CIM X

Ingest del paper *Real-time Control of Granular Sampling via Nonlinear Processes Using the IRCAM Signal Processing Workstation* (Cort Lippe, X CIM 1993, pp. 178–182, 12 refs).

Estrazione testo via `pdftotext -layout` su `raw/proceedings/1993_CIM_X_Atti.pdf` (range righe 7940–8210).

Pagina creata: `wiki/sources/proceedings/lippe1993.md` con schema fisso completo (citazione / categoria / argomento / sistema / analogia PGE / posizionamento / note stilistiche / sezioni paper / 4 quote chiave).

**Contributi argomentativi acquisiti:**

1. **Precursore tassonomico CIM**: distinzione esplicita *granular synthesis* (elektronische Musik, forme d'onda sintetiche) vs *granular sampling* (musique concrète, porzioni di sample) pp. 179–180. PGE collocato come *granular sampling* nella tassonomia Lippe → legittima `PointerController` come componente di prima classe e l'asse Y = posizione nel buffer del `score_visualizer`. Quote pietra-angolare p. 180: *"onset time into the stored sound [...] of primary importance [...] grain order may have important consequences, creating an implicit hierarchy of parameters"*.

2. **Doppia conferma indipendente tendency mask CIM 1993**: Lippe ISPW real-time + Di Scipio/Tisato ICMS offline, stesso volume X CIM 1993, entrambi adottano esplicitamente tendency masks come tecnica primaria. Lippe p. 181: *"choose grains statistically within defined tendency masks (constantly moving windows with varying sizes)"*. Rinforza concept page [[tendency-mask]] e differenziatore #8 in `overview.md` (modello PGE come postura consolidata della tradizione CIM 1993, non invenzione).

3. **Recursive aspect** p. 180 (real-time mixing dell'output di task simultanee + reuse come stored samples per altre task) = primitiva architetturale identica al workflow STEMS PGE in real-time; precursore CIM 1993 della recursive granulation `x_{n+1} = f_b(f_a(x_n))` di [[discipio1995]].

4. **Anti-analogia controllo**: Lippe = real-time signal-driven (pitch/amplitude tracking del clarinetto in *Music for Clarinet and ISPW* pilota tendency masks) vs PGE = deferred declarativo (loop lungo). Coppia con [[roads2021]] EmissionControl2 come due poli del real-time gestural CIM-internal.

5. **Rete CIM 1993 documentata**: Lippe ringrazia Miller Puckette, Jean Piche e *Agostino Di Scipio* negli acknowledgements (p. 182) — scambio diretto tradizione offline ↔ real-time documentata all'interno del singolo volume X CIM.

**Sezioni paper CIM 2026 mappate:**
- Sezione 1 (Introduzione): atto 2 narrazione tre-atti — snodo offline→real-time documentato CIM 1993 (coppia con [[discipio-tisato1993]]).
- Sezione 2 (Sintesi granulare): tassonomia *granular synthesis vs sampling*; PGE = granular sampling.
- Sezione 3 (PGE architettura): tendency masks 1993 doppia conferma; rinforzo [[tendency-mask]] in `ParameterOrchestrator`.
- Sezione 4 (Partitura grafica): quote p. 180 onset time *"of primary importance"* = legittimazione CIM 1993 dell'asse Y = buffer.

**Propagazione completata:**
- `overview.md`: aggiunta riga *1993 | Lippe (CIM X)* nella tabella precursori (subito dopo Di Scipio/Tisato 1993); aggiornato differenziatore #8 (tendency mask) con doppio datapoint CIM 1993; aggiornata riga Di Scipio/Tisato 1993 con link [[lippe1993]] (stesso volume X CIM).
- `cim-survey.md`: ampliata entry Lippe 1993 (era 2 righe minime) con pagine, contenuto tassonomico, tendency masks, recursive aspect, link [[lippe1993]]; aggiunto rinvio in sezione *Non comparabili (real-time)* con precisazione del ruolo (precursore tassonomico + conferma tendency mask).
- `bibliography.md`: aggiunta riga `Lippe1993cim` nella tabella Proceedings con sezioni paper [1, 2, 3, 4]; aggiunta voce corrispondente in *Debito Zotero* (conteggio: 12 → 13 chiavi).
- `index.md`: aggiunta entry Sources — Proceedings per `lippe1993.md` (inserita prima di [[discipio1995]] in ordine cronologico).
- Schema fisso del workflow ingest proceedings rispettato integralmente.

Concept pages: nessuna nuova creazione necessaria; [[tendency-mask]] rinforzata via overview.md (non ri-aggiornata direttamente perché la formulazione attuale del concept page già include le tendency masks Truax 1988 / Di Scipio/Tisato 1993 — l'aggiunta Lippe è materia di precursori, non di definizione del modello).

Resta aperto:
- CIM 2024 Markidis (unico ✗ rimasto in bibliography table).
- Concept page `interactivity-rate.md` candidata da [[discipio1995]] (vedi gap overview.md).
- Debito Zotero: 13 chiavi proceedings da generare in `refs.bib` (settimana 2 piano scrittura).

---

## [2026-05-22] lint | review-ingest discipio1995 + risoluzione lacune

Review-ingest del proceeding [[discipio1995]] (ingestito 2026-05-21).
Schema fisso rispettato, propagazione completa (overview / cim-survey /
bibliography / index / log). Lacune individuate e risolte:

1. **Deviazione piano** — CIM XI 1995 era in `setup-workspace.md`
   Livello C (ignora). Riclassificato a Livello A punto 5 con motivazione
   (snodo offline → real-time stesso autore di 1991/1993). Nota di
   migrazione lasciata anche in Livello C.

2. **Debito BibTeX `refs.bib`** — 11 chiavi proceedings (`Roads1985cim`,
   `DiScipio1991cim`, `DiScipioTisato1993cim`, `DiScipio1995cim`,
   `Rizzuti2006`, `Arcella2012`, `KellerRolfe1998`, `ValleLombardo2003`,
   `OrtoseccoPiccialli1989`, `Sparano2018`, `Cera2022`) ✓ in wiki ma
   assenti da `refs.bib`. Pattern pre-esistente (CLAUDE.md: aggiunta
   manuale via Zotero). Aggiunta sezione "Debito Zotero" in
   `bibliography.md` con elenco esplicito + modello pattern; refs.bib
   non modificato a mano (regola CLAUDE.md). Da risolvere settimana 2
   piano scrittura, prima di `pdflatex`.

3. **Conteggio refs** — `discipio1995.md` dichiara 11 refs; conteggio
   effettivo confermato 11 (Di Scipio 1994a/b/1995 = 3 voci distinte
   compattate nella scrittura). Nessuna correzione.

4. **Concept page candidate** — `interactivity-rate.md` emersa da
   taxonomy 4-quadrant Di Scipio 1995 p. 19 + definizione interactivity
   ≠ immediate audible output. Aggiunta a `overview.md` sezione "Gap da
   colmare" come candidate per Step 5 piano (post step 2-4).

5. **Cross-link `near future`** — quote Di Scipio/Tisato 1993 p. 165
   referenziata in [[discipio1995]] / `overview.md` riga 1995 verificata
   presente in [[discipio-tisato1993]] righe 67, 96. Consistente.

---

## [2026-05-21] ingest | proceedings Di Scipio 1995 — Real-time Polyphonic Time-shifting CIM XI

Fonte: `raw/proceedings/1995_CIM_XI_Atti.pdf` pp. 19–22.
Output: `wiki/sources/proceedings/discipio1995.md`.

Contenuto: KYMA/CAPYBARA (*Hybris*, g-flute+bcl+computer 1994) + PODX/GSAMX/DMX-1000 (*Essai du vide. Schweigen*, tape 1993). Smalltalk-80 scripts annidati; nuova classe `aSample&ShiftWithAllPass` con parametri custom (grain dur 10–70 ms, stretch factor, allpass delay = grain_dur/2). 4 stream a 5"/10"/15"/20" con ratio 5×/4×/3×/2× più lenti. Recursive granulation `x_{n+1} = f_b(f_a(x_n))`. Taxonomy 4-quadrant `{composition,performance} × {program,environment}`.

Significato: **snodo CIM Di Scipio offline → real-time** per stesso autore di [[discipio1991]] e [[discipio-tisato1993]] — documenta sul piano CIM la transizione di paradigma annunciata Di Scipio/Tisato 1993 p. 165. PGE 2026 = ritorno volontario al deferred *dopo* il completamento della transizione. Citabile sez. 2 (chiusura filone Di Scipio), 5 (modello stilistico paper compositivo CIM), 6 (taxonomy interactivity ≠ immediate output).

Propagazione:
1. `overview.md` — aggiunta riga 1995 alla tabella precursori (tra 1994 e 1998) con quote pietra-angolare p. 19 (interactivity definition + 4-quadrant) e p. 22 (quanta-of-silence reversal).
2. `cim-survey.md` — espansa entry 1995 con dettagli implementazione + link `[[discipio1995]]`; aggiunto link in elenco real-time non-comparabili.
3. `bibliography.md` — nuova riga `DiScipio1995cim | CIM XI | ✓ | 2, 5, 6`.
4. `index.md` — nuova riga in Sources—Proceedings sotto discipio-tisato1993.
5. Concept pages: nessuna toccata (paper consolida tesi narrazione tre atti, già coperta in overview).

---

## [2026-05-21] restructure | De Poli/Piccialli 1988 da papers/ → proceedings/

Fonte: già ingestita 2026-05-08 come `wiki/sources/papers/depolipiccialli1988.md`. Riclassificata: il documento è proceedings CIM VII 1988 (`raw/proceedings/1988_CIM_VII_Atti.pdf`, pp. 69–73), non paper PDF standalone — convenzione CLAUDE.md richiede `wiki/sources/proceedings/`.

Operazioni:
1. Creata `wiki/sources/proceedings/depoli-piccialli1988.md` fondendo lo schema proceedings (Categoria/lunghezza, Note stilistiche, Posizionamento storico, Sistema o strumento descritto) con i campi della vecchia pagina papers (Gap o problema identificato, Rilevanza punto-per-punto, Collegamento alla tesi centrale). Aggiunti 4 nuovi punti di rilevanza: pattern precompute-once/reuse-many, Stream-per-formante, inviluppo≡finestra di analisi, controllo percettivo.
2. Rimossa `wiki/sources/papers/depolipiccialli1988.md`.
3. Aggiornati: `cim-survey.md` (entry 1988 espansa con dettagli FIR/prototipi/precompute + link `[[depoli-piccialli1988]]`); `index.md` (rimossa riga in Papers, nuova riga in Proceedings con sintesi); `concepts/sintesi-granulare-sincrona.md` (link aggiornato a `proceedings/`); `bibliography.md` invariato (chiave `DePoliPiccialli1988` ✓, sezioni 2,3).
4. Non toccato `overview.md` (testo cita "De Poli/Piccialli 1988" senza wikilink — i contenuti restano validi).

---

## [2026-05-04] ingest | CIM Proceedings (23 volumi, 1976–2024)

Fonte: `raw/proceedings/` — `pdftotext` su tutti i PDF, ricerca su radice `granul`.
Output: `wiki/sources/proceedings/cim-survey.md`
Pagine toccate: 1 nuova.
Sintesi: trovati articoli dedicati alla sintesi granulare in 12 dei 23 volumi CIM.
Confronto con PGE documentato nella sezione "tempo differito" del survey.

---

## [2026-05-05] ingest | generator.md — Generator, pipeline YAML→SCO

Fonte: `raw/PythonGranularEngine/src/core/generator.py` + `graph/class_diagram.puml`
Output: `wiki/sources/pge/generator.md`
Contenuto: orchestratore principale, logica solo/mute, eval matematica, build incrementale.

---

## [2026-05-05] ingest | stream.md — Stream / StreamConfig / StreamContext

Fonte: `raw/PythonGranularEngine/src/core/stream.py` + `stream_config.py`
Output: `wiki/sources/pge/stream.md`
Contenuto: nucleo sintesi granulare, algoritmo multi-voce, generate_grains(), ispirazione DMX-1000.

---

## [2026-05-05] ingest | score-visualizer.md — ScoreVisualizer

Fonte: `raw/PythonGranularEngine/src/rendering/score_visualizer.py`
Output: `wiki/sources/pge/score-visualizer.md`
Contenuto: partitura grafica, encoding frecce, loop mask, envelope panel, paginazione A3.

---

## [2026-05-05] ingest | stream-cache-manager.md — StreamCacheManager

Fonte: `raw/PythonGranularEngine/src/rendering/stream_cache_manager.py`
Output: `wiki/sources/pge/stream-cache-manager.md`
Contenuto: cache SHA-256 per build incrementale Csound, dirty detection, garbage collect.

---

## [2026-05-05] ingest | parameter-orchestrator.md — ParameterOrchestrator + Strategie

Fonte: `raw/PythonGranularEngine/src/parameters/parameter_orchestrator.py` + `strategies/strategie.py`
Output: `wiki/sources/pge/parameter-orchestrator.md`
Contenuto: DSL parametrico, ExclusiveGroupSelector, GateFactory, dephase, FillFactor vs DirectDensity.

---

## [2026-05-05] ingest | renderer.md — CsoundRenderer / NumpyAudioRenderer / ReaperProjectWriter

Fonte: `raw/PythonGranularEngine/src/rendering/csound_renderer.py` + `numpy_audio_renderer.py` + `reaper_project_writer.py`
Output: `wiki/sources/pge/renderer.md`
Contenuto: tre renderer, pattern OCP, overlap-add NumPy, STEMS vs MIX, export Reaper.

---

## [2026-05-05] ingest | pointer-controller.md — PointerController

Fonte: `raw/PythonGranularEngine/src/controllers/pointer_controller.py`
Output: `wiki/sources/pge/pointer-controller.md`
Contenuto: posizione testina nel buffer, speed_ratio (costante o Envelope con integrazione), loop statico vs dinamico, phase accumulator inerziale, deviazione per-grano. Risolve open question di stream.md su time_mode:normalized (avviene in _pre_normalize_loop_params prima del pipeline).

---

## [2026-05-05] ingest | voice-manager.md — VoiceManager

Fonte: `raw/PythonGranularEngine/src/controllers/voice_manager.py`
Output: `wiki/sources/pge/voice-manager.md`
Contenuto: VoiceConfig (frozen dataclass, 4 offset dimensionali), voice-0 invariant, 4 strategie ortogonali, layering a 3 livelli (base controller + voice strategy + grain jitter), pan_spread come Envelope.

---

## [2026-05-05] ingest | density-controller.md — DensityController

Fonte: `raw/PythonGranularEngine/src/controllers/density_controller.py`
Output: `wiki/sources/pge/density-controller.md`
Contenuto: fill_factor vs density (mutuamente esclusivi), IOT = 1/density, distribuzione Truax sincrona/asincrona/blend, distribution come Envelope per morphing texture nel tempo.

---

## [2026-05-07] lint | correzioni post-review ingestione Step 2 addendum

Fonte: comparazione wiki vs sorgenti `raw/PythonGranularEngine/src/controllers/` + `src/core/stream.py` + `src/strategies/voice_*`
Correzioni applicate:
- `density-controller.md`: pseudocodice "Ruolo" rimpiazzato con scatter blending reale da `Stream.generate_grains()`. Il frammento precedente mostrava solo `voice_cursors[0] += iot` senza blend multi-voce.
- `pointer-controller.md`: aggiunto step 4 in Comportamento runtime — offset `grain_reverse` (`if grain_reverse: final_pos += grain_duration`) prima del wrap finale.
- `stream.md`: pipeline aggiornata con `_init_grain_reverse()` step separato (avviene prima di ParameterOrchestrator). Attributi `num_voices`/`scatter` corretti: sono `_num_voices`/`_scatter` privati gestiti da `_init_voice_manager()`, non da ParameterOrchestrator.

---

## [2026-05-07] lint | verifica accuracy density-controller, voice-manager, pointer-controller

Fonte: sorgenti `raw/PythonGranularEngine/src/controllers/` + `raw/.../strategies/voice_*`
Correzioni applicate:
- `density-controller.md`: pseudocodice `_apply_truax_distribution` aveva 3 rami; codice reale ha 2 (`<= 0.0` / `else`). Nessun ramo speciale per dist==1.0.
- `voice-manager.md`: conteggio accordi 21→22 (alterato conteggio errato). `StochasticPitchStrategy` e `StochasticPointerStrategy`: range cache `[-1,1]`, offset può essere negativo.
- `pointer-controller.md`: reset loop dinamico incompleto — aggiunto caso backward (`delta_pos < 0` → reset a `loop_end - 1e-9`).
Nessuna modifica strutturale. Pagine rimanenti verificate come accurate.

---

## [2026-05-07] lint | verifica copertura post-review collega

Fonte: analisi diff git dei file modificati nel commit Step 2 addendum
Correzioni applicate:
- `stream.md`: open question `scatter` marcata risolta con riferimento a density-controller.md (algoritmo già documentato lì dal lint precedente).
- `stream.md`: newline mancante a fine file.

---

## [2026-05-07] ingest | truax1990.md — Composing with Real-Time Granular Sound

Fonte: `raw/papers/Truax_1990_Composing-with-Real-Time-Granular-Sound.pdf`
Output: `wiki/sources/papers/truax1990.md`
Contenuto: gerarchia di controllo granulare (control variables → presets/ramps → score/tendency masks), gap controllo/percezione esplicitato, tendency masks come precursore diretto del score_visualizer PGE, riposizionamento del compositore come sorgente di messaggi di controllo.
Quote chiave: "It reduces to absurdity the idea of total control by the composer. Hierarchic levels of control are absolutely necessary." (p. 131)

---

## [2026-05-08] ingest | roads1988.md — Introduction to Granular Synthesis

Fonte: `raw/papers/Roads_1988_Introduction-to-Granular-Synthesis.pdf` (Computer Music Journal 12(2), pp. 11–13)
Output: `wiki/sources/papers/roads1988.md`
Contenuto: editoriale CMJ del numero monografico granulare, definizione canonica (grani quasi-gaussiani 1–50ms, density, additive synthesis), lignaggio Gabor → Wiener → Moles → Xenakis, event a 12 parametri (begin/duration/waveform/center freq/bandwidth/density/amplitude + slope) come precursore diretto del DSL YAML PGE, scattering random per density slope = DensityController, eventi come "lines, triangles, rhomboid shapes" su piano frequenza/tempo come precedente di score_visualizer (con scarto: PGE asse Y = posizione-buffer, non frequenza).
Aggiornato `overview.md` (differenziatore 2 cita esplicitamente Roads 1988; gap rimosso).

---

## [2026-05-08] ingest | gabor1947.md — Acoustical Quanta and the Theory of Hearing

Fonte: `raw/papers/Gabor_1947_Acoustical-Quanta-and-the-Theory-of-Hearing.pdf` (*Nature*, 159(4044), pp. 591–594)
Output: `wiki/sources/papers/gabor1947.md`
Contenuto: radice teorica del paradigma granulare. Information diagram tempo×frequenza, principio di indeterminazione Δt·Δf ≥ 1, segnale elementare gaussiana × sinusoide (grano Gabor), matrice di grani come prima rappresentazione bidimensionale di un suono come collezione di quanti discreti, soglia di discriminazione dell'orecchio ≈ 1 sui dati Bürck–Kotowski–Lichte 1935 e Shower–Biddulph 1931, due meccanismi di hearing (risuonatori cocleari ~10 ms + raffinamento neurale ~250 ms) che giustificano la finestra 1–50 ms come range tipico del grano.
Aggiornato `overview.md`: nuova sezione "Radici teoriche" con Gabor come fondamento; rimosso dal gap.

---

## [2026-05-08] ingest | truax1988.md — Real-Time Granular Synthesis with a Digital Signal Processor

Fonte: `raw/papers/Truax_1988_Real-Time-Granular-Synthesis-with-a-Digital-Signal-Processor.pdf` (Computer Music Journal 12(2), pp. 14–26)
Output: `wiki/sources/papers/truax1988.md`
Contenuto: documento tecnico fondativo del primo sistema granulare interamente real-time (DMX-1000 + PDP Micro 11). Tre programmi GSX/GSAMX/GRMSKX, tre modelli unit grain (AS/FM/SAM). Quattro corrispondenze con PGE: (1) Tabella 1 psychoacoustic correlates come mappatura **documentale** ricalcata in PGE solo in punti specifici (`FillFactorStrategy` vs `DirectDensityStrategy`, distribuzione sincrona/asincrona/blend di `DensityController`); (2) gerarchia Fig. 3 (`Score → Presets → Ramps → Tendency masks → Control variables`) mappata su YAML con bijezione parziale — `StreamConfig` non corrisponde a control variables (è meta-layer); (3) Fig. 4 overlay ASCII su terminale 24-line come **primo precedente concreto** di rappresentazione visiva multi-parametro tempo-dipendente (più diretto di Roads 1978/1988 che parlano di poligoni metaforici); (4) due modalità granulating sampled sound (segmento fisso vs stream continuo) — PGE implementa la fissa.
Quote chiave: "Two problems that must be solved... generating the large amount of data... and designing the control variables required to give the musician a powerful means to link the lower-level data to macro-level compositional strategies and gestures." (p. 14)
Aggiornati: `bibliography.md` (Truax1988 ✗→✓, sezioni 1, 2, 3, 4); `index.md`; `overview.md` (rimosso da gap; differenziatore 2 esteso con Fig. 4 Truax 1988 come primo overlay multi-parametro concreto, distinto da poligoni metaforici di Roads).
Note: prima stesura conteneva due claim sovrastimati (correlato percettivo per ogni parametro DSL; StreamConfig = control variables) — corretti dopo review utente con riferimento a `parameter-orchestrator.md` e `stream.md`. Propagazione differenziatore 2 aggiunta in seconda passata di review.

---

## [2026-05-08] ingest | roads1978.md — Automated Granular Synthesis of Sound

Fonte: `raw/papers/Roads_1978_Automated-Granular-Synthesis-of-Sound.pdf` (Computer Music Journal 2(2), pp. 61–62)
Output: `wiki/sources/papers/roads1978.md`
Contenuto: AGS (Automated Granular Synthesis), prima implementazione computer documentata della sintesi granulare (B6700 ALGOL, 1975, front-end MUSIC V). Inviluppo grano gaussiano modificato (attacco gauss + sustained peak + decay gauss); event a **6 coppie valore/slope** (begin/duration/waveform/center freq/bandwidth/density/amplitude — precursore diretto del 12-param di Roads 1988 e del DSL YAML PGE); pattern *front-end → engine* identico ad architettura PGE (`generator.py` → Csound/NumPy); notazione grafica come polygon arbitrario su piano freq/tempo, con riferimento esplicito a Stockhausen *Studie II*. Limite hardware: 32 grani simultanei, 16-bit interno → 12-bit DAC.
Aggiornato `overview.md`: radici teoriche (Roads 1978 = prima implementazione computer), tabella precursori (riga 1978 inserita prima di Roads 1985), differenziatore 2 (precedente notazionale Roads 1978 + Stockhausen, prima di Roads 1988). Aggiornato `bibliography.md` colonna Wiki ✗→✓ + sezioni 1, 2, 3, 4.

---

## [2026-05-08] ingest | truax1994.md — Discovering Inner Complexity

Fonte: `raw/papers/Truax_1994_Discovering-Inner-Complexity.pdf` (Computer Music Journal 18(2), pp. 38–48)
Output: `wiki/sources/papers/truax1994.md`
Contenuto: GSAMX su DMX-1000, due estensioni rispetto al 1988 — (a) variable-rate granulation: ratio `off:on` come time-extension factor (TEF) tra fixed-sample e continuous-sample, time-stretching arbitrario senza pitch shift; (b) harmonization scheme F=4 con N variabile per voce/grano. Quattro corrispondenze PGE: (1) variable-rate = ancestor di `PointerController.speed_ratio` Envelope (TEF Truax = integrale di speed_ratio PGE); (2) asse Y partitura PGE = visualizzazione esplicita del movimento testina vs tempo descritto a parole da Truax; (3) harmonization F=4 = precedente di `VoiceManager` + `PitchController` multi-voce; (4) PGE implementa solo fixed-sample. Formulazione esplicita della **separazione micro/macro come tesi psicoacustica abilitante** del paradigma granulare: la granulazione separa micro-pattern d'onda da macro-evoluzione temporale.
Quote chiave: "By linking frequency and time at the micro level, granulation makes it possible to treat these two variables independently at the macro level" (p. 44); "Time stretching is a unique way to bring out the inner complexity of a sound" (p. 45).
Aggiornati: `bibliography.md` (Truax1994 ✗→✓, sezioni 1, 2, 4, 5); `index.md`; `overview.md` — radici teoriche estese con quote separazione micro/macro e quarta conseguenza diretta (asse Y = posizione-buffer giustificato da Truax 1994); differenziatore 2 esteso con riferimento al meccanismo variable-rate.

---

## [2026-05-08] lint | riallineamento wiki + CLAUDE.md al nuovo orientamento

Trigger: cambio tesi paper (gap controllo/percezione → loop lungo / postura tempo differito; 3 atti narrativi; 3 contributi: DSL+LSP, partitura, STEMS).

Modifiche: sezioni "Collegamento alla tesi centrale" e "Sezioni del paper CIM 2026" riformulate in `papers/{truax1994, roads1988, gabor1947}.md` e in `pge/{generator, stream, stream-cache-manager, renderer, pointer-controller, voice-manager, density-controller}.md`. Refusi puntuali: header duplicato in `papers/truax1988.md`, lista monca in `pge/parameter-orchestrator.md`. Refuso fattuale in `pge/pointer-controller.md`: pointer = asse Y partitura, non X. `bibliography.md`: Roads2021/Roads2006 sez.7→6 (sez.7 non esiste); Truax1990 sez.+4. `index.md`: descrizione truax1990 ricontestualizzata. `CLAUDE.md`: sezione "Central thesis" + "Paper structure" riscritte; schema "Collegamento alla tesi centrale" nei workflow ingest aggiornato; riferimento "Sezione 1 Problema" → "Sezione 1 Introduzione".

---

## [2026-05-08] ingest | depolipiccialli1988.md — Forme d'onda per la sintesi granulare sincrona

Fonte: `raw/papers/DePoli-Piccialli_1988_Forme-dOnda-Sintesi-Granulare-Sincrona_CIM-VII.pdf` (*Atti del VII Colloquio di Informatica Musicale*, pp. 70-74; figura p. 75)
Output: `wiki/sources/papers/depolipiccialli1988.md`
Contenuto: ramo CIM complementare alla linea Roads/Truax: sintesi granulare additiva sincrona con il periodo, orientata a suoni quasi periodici e controllo formantico dell'inviluppo spettrale. Problemi identificati: grani campionati difficili da controllare globalmente; collocazione asincrona a 10-20 ms problematica per continuita' di fase; metodi additivi formantici senza linearita' di fase soggetti a cancellazioni/interferenze. Soluzione: grani come risposte FIR passa-banda a fase lineare, tabulati e trasformati dinamicamente (passo non costante, AM, distorsione non lineare).
Aggiornati: `bibliography.md` (DePoliPiccialli1988 ✗→✓, sezioni 2, 3); `index.md`; `overview.md` (radici teoriche, tabella precursori, gap); nuova pagina concetto `wiki/concepts/sintesi-granulare-sincrona.md` per distinguere period-synchronous granular synthesis dalla distribuzione IOT sincrona/asincrona Truax/PGE.

---

## [2026-05-08] lint | review ingest depolipiccialli1988

Trigger: review post-ingest del paper De Poli/Piccialli 1988.
Modifica: in `overview.md` la sezione "Precursori diretti nella tradizione CIM" e' stata rinominata "Precursori e rami complementari nella tradizione CIM" per includere De Poli/Piccialli 1988 come ramo CIM contrastivo senza sovrastimarlo come precursore diretto di PGE.

---

## [2026-05-09] restructure | review-ingest fix — discipio1994 + roads2021

Trigger: workflow review-ingest sui due ingest 2026-05-08.
Issue 1 (page numbers DiScipio1994): paginazione PDF (p. 4, p. 8) sostituita con paginazione articolo (p. 138, p. 142). Articolo: *Contemporary Music Review* 10(2), pp. 135-148. Mapping verificato: PDF p. N = articolo p. 134+N. Corretti `discipio1994.md` (3 quote) e `overview.md` (1 quote).
Issue 2 (tabella precursori): aggiunta riga DiScipio 1994 in tabella "Precursori e rami complementari" come precursore concettuale del loop lungo. Aggiunta nuova sezione "Sistemi contemporanei (poli compositivi opposti)" con riga Roads/Kilgore/DuPlessis 2021 (EC2) come polo gestural opposto al declarative PGE.
Issue 4 (differenziatori chiave): integrato confronto EC2 in differenziatore 1 (OSC scripting v1.2 = scripting esterno vs DSL+LSP integrato) e differenziatore 2 (Scan Display real-time vs Score Visualizer post-synthesis — stesso fenomeno fisico, scopi opposti).
File toccati: `wiki/sources/papers/discipio1994.md`, `wiki/overview.md`, `wiki/log.md`.

---

## [2026-05-08] ingest | roads2021.md — EmissionControl2 Architecture

Fonte: `raw/papers/Roads_2021_Architecture-Real-Time-Granular-Synthesis-EmissionControl2.pdf` (*Computer Music Journal*, 45(3), pp. 20–38, doi:10.1162/COMJ_a_00613)
Output: `wiki/sources/papers/roads2021.md`
Contenuto: EC2 come granulatore real-time per-grain, polo opposto di PGE nel paradigma gestural vs declarative. Tabella corrispondenze architetturali EC2↔PGE (scanner=PointerController, Asynchronicity+Streams=DensityController, LFO modulation=Envelope strategies, Scan Display vs Score Visualizer). Quote chiave: studio composition = "tape is running," culling good parts — contrasto diretto con il workflow YAML→genera→ascolta→rifletti di PGE. OSC scripting (v1.2) apre al controllo algoritmico ma non raggiunge l'astrazione di DSL dichiarativo PGE.
Aggiornati: `bibliography.md` (Roads2021 ✗→✓, sezioni 3, 6); `index.md`; `overview.md` (gap aggiornato).

---

## [2026-05-08] ingest | discipio1994.md — Micro-time sonic design and timbre formation

Fonte: `raw/papers/DiScipio_1994_Micro-Time-Sonic-Design-and-Timbre-Formation.pdf` (*Contemporary Music Review*, 10(2), pp. 135–148)
Output: `wiki/sources/papers/discipio1994.md`
Contenuto: teorizzazione dei "models of detailed sonic design" come approccio indeterministico alla composizione micro-strutturale. Supera la distinzione composing-the-sound / composing-with-sound (Truax 1990b) in una visione olistica timbro=forma. Opere discusse: *kairós* (1991/92, IBM486 home studio, deferred time), *Zeitwerk l'orizzonte delle cose* (1992, IBM3090 + ICMS Padova, deferred time), *Essai du vide. Schweigen* (1993, GSAMX real-time, Simon Fraser). Affinamento tesi: la postura indeterministica non è vincolata al deferred time ma al ciclo iterativo di osservazione; PGE sceglie il deferred come spazio compositivo, non per costrizione hardware.
Aggiornati: `bibliography.md` (DiScipio1994 ✗→✓, sezioni 2, 3); `index.md`; `overview.md` (radici teoriche estese con Di Scipio 1994, gap aggiornato).

---

## [2026-05-08] ingest | depolipiccialli1991.md — Pitch-Synchronous Granular Synthesis

Fonte: `raw/papers/DePoli-Piccialli_1991_Pitch-Synchronous-Granular-Synthesis.pdf` (*Representations of Musical Signals*, MIT Press, pp. 187-219). PDF scannerizzato, letto con OCR locale.
Output: `wiki/sources/papers/depolipiccialli1991.md`
Contenuto: formalizzazione del ramo pitch-synchronous/source-filter: la sintesi granulare come famiglia di modelli, grano = risposta all'impulso FIR, treno quasi periodico di impulsi agganciato al pitch, griglia dipendente dal suono, prototype waveform transformations per controllare formanti, ampiezza, frequenza centrale, bandwidth e shape.

Aggiornati: `bibliography.md` (DePoliPiccialli1991 ✗→✓, sezioni 2, 3); `index.md`; `overview.md` (radici teoriche, tabella rami complementari, gap); `wiki/concepts/sintesi-granulare-sincrona.md` con formalizzazione source-filter, griglia dipendente dal pitch e prototype waveform transformations.

---

## [2026-05-09] ingest | roads2001 (Microsound) — ingest parziale ch1 + ch9

Fonte: `raw/papers/Roads_2001_Microsound.pdf` (libro, 423 pp PDF / 9 capitoli + 2 appendici).
Output (creati): `wiki/sources/papers/roads2001-ch01-time-scales.md`, `wiki/sources/papers/roads2001-ch09-conclusion.md`
Strategia: 10 sub-agent paralleli (ch1–9 + appA), schema fisso adattato a libro multi-capitolo.

**Esito.**
- ch9: agent ha letto pp 363–366, Write negato dalla quota, body completo restituito come testo e persistito manualmente in main.
- ch1: agent ha letto pp 15–56, Write negato; restituito solo summary ≤200 wd con 3 quote killer (pp. 6, 10, 26). File scritto come *stub partial* da main, marcato in testa.
- ch2 (history), ch3 (granular synthesis), ch4 (particle synthesis), ch5 (transformation), ch6 (windowed analysis), ch7 (composition), ch8 (aesthetics), appA (cloud generator): falliti per stream timeout o quota limit reached. Nessun file scritto.

**Quote chiave da ch1 (pietra angolare tesi loop lungo):**
> «This backtracking is not necessarily time wasted; it is part of an important feedback loop in which the composer refines the work. … Compare all this with the efficiency of the real-time improviser!» (p. 10)
>
> «One can imagine a musical interface in which a musician specifies the desired sonic result in a musically descriptive language which would then be translated into particle parameters and rendered into sound.» (p. 26)

**Quote chiave da ch9 (cornice terzo atto):**
> «Few maps exist, and shortcuts are scarce. So we base our composition strategy on a heuristic search for remarkable sound objects…» (p. 351)

Aggiornati: `bibliography.md` (Roads2001 ✗→◐ ch1+ch9; sezioni estese 2,4 → 1,2,4,6); `index.md` (2 nuove entry); legenda colonna Wiki estesa con simbolo ◐.

**Da completare in pass successivo (post reset quota):**
- ch1: re-ingest body integrale (pagina attuale è stub da summary, non da rilettura)
- ch2 history, ch3 granular synthesis (core), ch4 particle synthesis (core), ch5 transformation (sample-based granular = core), ch6 windowed analysis (tangenziale), ch7 composition (modello sezione 5 paper), ch8 aesthetics (core argomentativo), appA cloud generator (precursore architetturale diretto)
- propagazione `overview.md` (precursori, differenziatori, lineage UCSB) — rimandata fino a ingest core completo (ch3, ch4, ch8, appA)

---

## [2026-05-09] ingest | roads2006.md — The evolution of granular synthesis (Xenakis Symposium)

Fonte: `raw/papers/Roads_2006_Evolution-Granular-Synthesis.pdf` (lecture, *International Symposium on The Creative and Scientific Legacies of Iannis Xenakis*, University of Guelph, 8–10 June 2006, 14 pp.)
Output: `wiki/sources/papers/roads2006.md`
Contenuto: panoramica programmatica della linea UCSB 2001–2006. Cinque progetti: PulsarGenerator (de Campo+Roads, 2001) con controllo via envelope time-varying su tutti i parametri di un pulsar train; SweepingQGranulator (SuperCollider) per microfiltration constant-Q per-grano; matching pursuit decomposition (Mallat–Zhang) come analisi TF atomica; EmissionControl 2005 (Thall+Roads) come prototipo della lineage gestural che culmina in EC2 (Roads 2021); progetto Ynez per visualizzazione e *study scores for electronic music* — dichiarazione programmatica della categoria di artefatto che PGE materializza nel score_visualizer. Cavitation/density-opacity formulati come parametri compositivi primari ("ratio of sound to silence"); metafora delle "sonic brushes" come computer programs che gettano particelle sul canvas tempo×frequenza. Citazione di Babbitt 1988 ("tape is for storage, control time as measurable distance of tape") usata da Roads per giustificare la fine-grained precision (5 µsec a 192 kHz).
Quattro corrispondenze PGE: (1) PulsarGenerator envelope-based control = `ParameterOrchestrator` su `Envelope` strategies; (2) EmissionControl 2005 = tappa intermedia della lineage gestural opposta a PGE; (3) Ynez "study scores" come categoria-antesignana di score_visualizer; (4) cavitation/density come riferimento concettuale per `DensityController`.
Aggiornati: `bibliography.md` (Roads2006 ✗→✓, sezioni 3, 6); `index.md`; `overview.md` — tabella "Sistemi contemporanei" estesa con righe 2001 (PulsarGenerator), 2005 (EmissionControl), 2006 (Ynez project) per tracciare la lineage UCSB pre-EC2; differenziatore 2 esteso con Ynez come antesignano programmatico (non implementato per output granulare deferred); gap aggiornato.

---

## [2026-05-11] ingest | roads2001 — Microsound cap. 2, 5, 6 + hub roads2001.md

Fonte: `raw/papers/Roads_2001_Microsound.pdf` (libro intero, 409 pp.). Sessione di chiusura dell'ingest integrale di *Microsound*: completati i tre capitoli mancanti (cap. 2 history, cap. 5 transformation, cap. 6 windowed analysis) e creato il file hub aggregatore.

Output:
- `wiki/sources/papers/roads2001-ch02-history-microsound.md` (pp 43–84): genealogia antiquo→analogico (atomismo greco, Beekman/Gassendi corpuscolare, Einstein 1907 phonon, Gabor 1946–1952, Meyer-Eppler Mosaiktechnik, Xenakis screens/ataxy/Markov chains, Stockhausen *How Time Passes* + Kontakte, Cowell precursore multi-scala 1930). Quote chiave: Schaeffer p. 44 («*musical ideas are prisoners of musical devices*»); critica frame rate costante pp. 67–68 («*the idea that all grains have the same duration is aesthetically limiting*») come razionale del differenziatore PGE; wave/particle dualismo p. 55 come razionale architetturale multi-scala.
- `wiki/sources/papers/roads2001-ch05-transformation.md` (pp 179–234): catalogo trasformazioni sample-based (micromontage graphical/script/algorithmic, granulation parameters list a 10 voci con corrispondenza 1:1 a YAML PGE, pitch-time changing granulare, filtering per-grano GranQ, waveset/wavecycle Wishart, convolution con cloud, spatialization per-grano). Quote pietra-angolare p. 234 (Roads/Vaggione): «*Circuit speed is less of a limiting factor [...] Musical interfaces that offer control through envelopes, presets, and other automation functions will assist composers in planning detailed and elaborate transformations*» — legittimazione esplicita del DSL come interfaccia compositiva matura, indipendente dalla velocità del calcolo. Quote p. 185 (micromontage by algorithmic process: «*high-level specification → note statements*») = DSL ante litteram. Quote p. 188 (asynchronous file granulation freedom > real-time).
- `wiki/sources/papers/roads2001-ch06-windowed-analysis.md` (pp 235–300): STFT, phase vocoder, tracking PV, vector oscillator transform, wavelet, Gabor transform. Capitolo *meno citabile* per PGE (PGE è time-domain, cap. 6 è frequency-domain) ma fondamentale per (a) razionale teorico del grano gaussiano via Gabor transform, (b) delimitazione scope: PGE è granular engine time-domain deferred, analisi-risintesi spettrale è out-of-scope per scelta. Quote Mallat p. 238 e Orcalli p. 300.
- `wiki/sources/papers/roads2001.md` (**hub**): indice di tutti i capitoli ingestiti (1–9 + appA), tre quote pietra-angolare (loop lungo p. 10, DSL p. 26, interfacce dichiarative p. 234), mappa capitoli → contributi PGE → sezioni paper CIM, posizionamento argomentativo del paper rispetto al libro (riprendere loop lungo + adempiere programma DSL + risolvere problema frame rate costante).

Aggiornati:
- `bibliography.md`: `Roads2001 | ◐ ch1+ch9 → ✓ (integrale: ch1–9 + appA)`; sezioni paper estese a 1, 2, 3, 4, 6.
- `overview.md`: differenziatore (1) YAML DSL esteso con tre quote esplicite di Roads (cap. 1 p. 26, cap. 5 p. 185, cap. 5 p. 234) che articolano in tre punti distinti del libro il programma di un'interfaccia compositiva dichiarativa che PGE materializza. Aggiunto differenziatore (6) density/durata grano time-varying per-voice, con riferimento esplicito alla critique constant microtime grid di Roads cap. 2 pp. 67–68. Gap section aggiornato (Roads 2001 *Microsound* rimosso dai gap, marcato come integrale tra gli ingestiti).
- `index.md`: hub `roads2001.md` + entry per ciascun capitolo (ch2, ch3, ch4, ch5, ch6, ch7, ch8, appA) con sintesi ≤2 righe ciascuna.

**Tre quote pietra-angolare di Roads 2001 per il paper CIM** (tutte tracciate nel hub):
> «*Composition is itself a supratemporal activity. [...] This backtracking is not necessarily time wasted; it is part of an important feedback loop in which the composer refines the work. [...] Compare all this with the efficiency of the real-time improviser!*» (cap. 1 p. 10) — tesi loop lungo.
>
> «*One can imagine a musical interface in which a musician specifies the desired sonic result in a musically descriptive language which would then be translated into particle parameters and rendered into sound.*» (cap. 1 p. 26) — programma DSL.
>
> «*Circuit speed is less of a limiting factor, but no matter how fast computers become, certain transformations will always be too difficult for a human being to manipulate effectively in real time [...] Musical interfaces that offer control through envelopes, presets, and other automation functions will assist composers in planning detailed and elaborate transformations.*» (cap. 5 p. 234) — legittimazione architetturale.

Note metodologiche:
- ch3, ch4, ch7, ch8, appA risultano untracked nello stato git (creati in sessioni precedenti); confermati per integrazione in questo ingest di chiusura.
- Roads 2001 è ora il testo di riferimento *integralmente coperto* della bibliografia PGE. Le citazioni nel paper potranno riferirsi al libro intero (`Roads2001`) con rinvio a capitolo specifico via wiki.

---

## [2026-05-11] restructure | CLAUDE.md variante book-chapter + quote DSL pp. 26-27

Review-ingest del collega su roads2001 ha esposto due lacune formali (entrambe minori). Fix:

1. **CLAUDE.md**: aggiunta nuova sottosezione `Workflow ingest (libro suddiviso per capitolo)` tra `Workflow ingest (paper PDF)` e `Workflow ingest (PGE source module)`. Documenta lo schema usato per ingest libri-trattato (es. Roads 2001 Microsound): struttura file (pagina hub + sub-pages capitolo + appendici); schema hub (Citazione + Stato ingest + Argomento del libro + Quote pietra-angolare + Mappa contributi + Capitoli per sezione + Posizionamento); schema sub-page capitolo (Posizione + Argomento + Struttura + Concetti chiave + Rilevanza PGE + Tesi centrale + Quote chiave + Sezioni CIM); regole di propagazione. La variante book-chapter era già stata applicata di fatto a roads2001 ma non documentata come schema canonico.

2. **Quote 2 (DSL musicale)**: attribuzione corretta da "p. 26" a "pp. 26-27" in tutte le occorrenze. La frase attraversa effettivamente le due pagine ("...which would then be translated" termina a p. 26; "into particle parameters and rendered into sound." apre p. 27). Update in:
   - `wiki/sources/papers/roads2001.md` (3 occorrenze: heading sezione, mappa contributi, mossa argomentativa 2)
   - `wiki/sources/papers/roads2001-ch01-time-scales.md` (4 occorrenze: heading "DSL legitimation", riferimento contributo 1, quote chiave, sezione 3)
   - `wiki/index.md` (entry ch01)
   - `wiki/overview.md` (differenziatore 1)

Resta in log.md la dicitura "p. 26" nelle entry storiche (2026-05-09 e 2026-05-11) come testimonianza del fix — log è append-only.

---

## [2026-05-11] ingest | roads2012.md — Roads 2012 *From Grains to Forms*

Fonte: `raw/papers/Roads_2012_From-Grains-to-Forms.pdf` (40 pp., Xenakis Symposium Paris 2012).
Output: `wiki/sources/papers/roads2012.md` (nuovo).

Schema standard paper PDF applicato. Tre punti di sovrapposizione strutturale con PGE:

1. **Per-grain effects processing come signature** (pp. 14–15): Roads dichiara che molti granulatori suonano *flat and one-dimensional* perche' mandano l'intero stream nello stesso effects channel; per-grain processing e' la signature di *truly granular signal processing*. PGE soddisfa la clausola architetturalmente (Controller x 4 + VoiceManager + dephase per-grano).
2. **Higher-order granulation = workflow STEMS** (p. 13): *Now* (2004) regranulazione di *Volt air*, *Never* (2010) regranulazione di terzo ordine, *Always* di quarto ordine — Roads assembla manualmente in Pro Tools; PGE istituzionalizza la pipeline (stem multitraccia + cache + export DAW).
3. **Studio detached from real-time** (p. 7): formulazione canonica della postura tempo differito.

Tre legittimazioni argomentative (non coperte in altre ingestioni):
- **PulsarGenerator compromise script + envelope** (p. 35, conclusione): endorsement esplicito dello spazio di interazione che PGE-ls + score_visualizer abita.
- **Fallimento Creatovox** (pp. 10–11): ammissione di prima persona da parte di Roads che la lineage virtuosica richiede pratica giornaliera che e' incompatibile con l'interesse compositivo; legittima la scelta architetturale PGE di non perseguire real-time.
- **Economy of selection** (pp. 31–32): teorizzazione esplicita del loop lungo come metodologia compositiva — *choosing one or a few perceptually and aesthetically optimal or salient choices from a vast desert of unremarkable possibilities*.

Propagazione:
- `overview.md`: differenziatore 1 (DSL) aggiunto quote PulsarGenerator compromise; differenziatore 3 (STEMS) aggiunta pratica higher-order granulation + quote "detached from real-time"; nuovo differenziatore 7 *per-grain effects processing come signature architetturale*; nuova sezione *Note per Sezione 6 — economy of selection come teorizzazione del loop lungo*; entry Roads 2012 spostata in lista *gia' ingestiti*.
- `bibliography.md`: Roads2012 — Wiki ✗ → ✓; Sezioni paper "4" → "1, 2, 3, 4, 5, 6".
- `index.md`: entry roads2012.md aggiunta sotto roads2006.md.

Niente concept pages nuove. Niente update a sintesi-granulare-sincrona.md (paper non tratta la distinzione SGS pitch-synchronous De Poli-Piccialli).

---

## [2026-05-11] fix | roads2012.md — review-ingest: citazione + page numbers + stile

Review-ingest del collega ha esposto un bug bloccante (citazione CIM errata) e tre errori di citazione pagine verificati contro PDF (`raw/papers/Roads_2012_From-Grains-to-Forms.pdf`, convention: PDF page N = printed page N, footer in fondo pagina).

1. **Citazione CIM**: era "In M. Solomos (ed.), *Proceedings of the international Symposium Xenakis* (université Paris 8, May 2012)" — pubblicazione errata. Corretto a "In S. Kanach (ed.), *Xenakis Matters: Contexts, Processes, Applications*. Hillsdale, NY: Pendragon Press. ISBN 978-1-57647-238-5", allineato a refs.bib (`@incollection{Roads2012}`). Solomos 2012 è altro volume da Paris 8; Kanach 2012 è il volume Pendragon che contiene "From Grains to Forms".

2. **Page numbers verificati contro PDF**:
   - "Detached from real-time constraints..." era p. 7 → corretto a **p. 8**.
   - "compromise between gestural interaction... PulsarGenerator" era p. 35 → corretto a **p. 30** (p. 35 è bibliografia; quote è in sezione CONCLUSION).
   - "principle of economy of selection / vast desert of unremarkable possibilities" era pp. 31–32 → corretto a **pp. 28–29** (sezione "The principle of economy of selection" inizia a p. 28).
   - "Recycling sounds... higher-order granulation" p. 13 ✓ (verificato).
   - "essential feature ... per-grain effects processing" pp. 14–15 ✓ (verificato).
   - "A funny thing happened... Creatovox" pp. 10–11 ✓ (verificato, quote continua p. 11 con Bebe Barron).

3. **Inconsistenza pp/p**: "(p. 14–15)" sezione Rilevanza → "(pp. 14–15)".

4. **Neologismo**: "cita-by-author" → "citato dall'autore stesso".

Propagazione page-number fix:
- `wiki/sources/papers/roads2012.md`: 8 occorrenze (Rilevanza, Collegamento tesi, Sezioni CIM, Quote chiave).
- `wiki/overview.md`: 3 occorrenze (differenziatore 1 p. 35→30, differenziatore 3 p. 7→8, Note Sezione 6 pp. 31-32→28-29).

Le citazioni errate nell'entry log immediatamente precedente (ingest roads2012 stesso giorno) restano come testimonianza — log è append-only.

## [2026-05-12] ingest | vaggione1991.md + vaggione1996.md + vaggione2002.md — trilogia Vaggione object-based / transformational / decorrelation

Fonti:
- `raw/papers/Vaggione_1991_On-Object-Based-Composition.pdf` (10 pp., versione francese 1995 in Ars Sonora — adattamento riveduto dell'originale Interface 1991)
- `raw/papers/Vaggione_1996_Approche-Transformationnelle-CAO.pdf` (9 pp., JIM 1996 Tatihou)
- `raw/papers/Vaggione_2002_Decorrelation-Microtemporelle.pdf` (12 pp., JIM 2002 Marseille)

Output: tre nuove pagine `wiki/sources/papers/vaggione{1991,1996,2002}.md`.

Schema standard paper PDF applicato a ciascuna. La trilogia funziona come triplice radice teorica del DSL e dell'architettura PGE:

1. **Vaggione 1991 — framework concettuale**: l'oggetto sonoro digitale come (a) collezione di oggetti discreti funzionante come entità unitaria, (b) collezione di échantillons; *transparent* contro l'opacità del supporto magnetico analogico. OOP applicato a composizione (clôture/héritage/polymorphisme). Multiple représentations come *réécritures*. → Fondamento concettuale del network Stream/Voice/Controller PGE + asse Y partitura (= posizione nella collection d'échantillons).

2. **Vaggione 1996 — meccanica fine del DSL**: quote-pietra-angolare *interaction forte* (p. 2): «toute intervention directe peut être considérée comme la déclaration d'un attribut particulier d'une entité quelconque; cet attribut peut dès lors être généralisé à toutes les instances successives de cette entité». Questa è la legittimazione argomentativa più precisa del DSL YAML + ParameterOrchestrator. Vaggione condanna anche i «taux ou pourcentages de variation [...] palliatifs au manque de visée proprement figurale» (p. 4) → legittima il visualizer figurale come strumento di lettura non statistica. Tahil/Kitab come precedenti compositivi nel reseau object-based.

3. **Vaggione 2002 — legittimazione spaziale di VoiceManager**: décorrélation microtemporelle (offset di ms su canali fisicamente separati, valori time-varying per voce) come attributo morfologico-spaziale, distinto dal panning classico (campo sincrono esterno). Realizzato direttamente da VoiceManager (onset/pointer/pan strategies) + dephase Controller per-grano («relation kaléidoscopique multi-locale», p. 6). Tempo differito esplicito come contesto nativo della tecnica (Music N family). Cita esplicitamente Vaggione 1996 a p. 7 — conferma la *colonna vertebrale* metodologica delle tre opere.

Propagazione:
- `overview.md`:
  - differenziatore 1 (DSL): aggiunta quote 1996 «déclaration d'attribut généralisé» + critica «palliatifs» come fondamento argomentativo accanto a Roads 2001 cap. 1/5
  - differenziatore 7 (per-grain effects): aggiunta estensione 2002 spazio = «décorrélation microtemporelle» con quote «relation kaléidoscopique multi-locale» + distinzione panning/decorrelation
  - tabella precursori CIM: nuova riga 1991/1996/2002 Vaggione che riassume la triplice radice
  - gap list aggiornata
- `bibliography.md`:
  - Vaggione1991 — Wiki ✗ → ✓; Sezioni "2, 4" → "1, 2, 3, 4"
  - Vaggione1996 — Wiki ✗ → ✓; Sezioni "3, 4" → "1, 3, 5, 6"
  - Vaggione2002 — Wiki ✗ → ✓; Sezioni "4" → "2, 3, 4, 5"
- `index.md`: tre entry aggiunte sotto roads2001-appA-cloud-generator.md.

Niente nuove concept pages. Niente update a sintesi-granulare-sincrona.md (la trilogia non tocca la distinzione SGS pitch-synchronous De Poli-Piccialli ma opera su un asse diverso: object-based composition, transformational CAO, decorrelation spaziale).

Una sola entry log per i tre paper, come da convenzione (ingest multipli stessa sessione).

---

## [2026-05-12] fix | vaggione2002.md + vaggione1991.md + overview.md — review-ingest collega

Review-ingest dei tre Vaggione ha esposto un bug bloccante non-Vaggione + page numbers off-by-one in vaggione2002.md + citazione header vaggione1991.md.

1. **Typo regressione `overview.md`** (riga Di Scipio 1994, hunk vaggione): "indeterismatica" → "indeterministica". Carattere `t` saltato, ortografia errata. Refuso introdotto durante l'edit della tabella precursori per aggiungere la riga Vaggione 1991/1996/2002 immediatamente sotto.

2. **Citazione header `vaggione1991.md`**: "(PDF letto: versione francese, 10 pp.)" → "(PDF letto: versione francese web-archived da archive.org, 8 pp.; originale a stampa pp. 33-52)". Il PDF locale è 8 pp fisiche (versione archive.org di Ars Sonora 1995); il conteggio "10 pp" era errato. Chiarito anche che pp. 33-52 è paginazione del fascicolo Ars Sonora originale.

3. **Page numbers `vaggione2002.md`** verificati con `pdftotext -f N -l N` contro PDF (12 pp fisiche, no footer printed numbers). Correzioni:
   - Gap section: panning `p. 8` → `p. 9` (PDF p. 9 ha "le panning n'a pas besoin d'informations concernant la phase").
   - Sezione "Condizioni minime" header: `pp. 5-6` → `p. 6` (lista a/b/c interamente su PDF p. 6).
   - Rilevanza 3 (real-time extension): `p. 6` → `p. 7` (sezione "Temps différé/temps réel" inizia PDF p. 7).
   - Rilevanza 5 (richiamo Vaggione 1996): `p. 7` → `p. 8` (PDF p. 8: «Dans un texte présenté aux JIM [Vaggione 1996]»).
   - Rilevanza 6 (micromontage): `p. 6` → `p. 7` (PDF p. 7 fine: «micromontages afin de construire des ensembles musicaux»).
   - Quote chiave 2 (panning): `p. 8` → `p. 9`.
   - Quote chiave 3 (kaléidoscopique): `p. 6` → `p. 7` (era anche contraddizione interna: Rilevanza 2 citava già `p. 7` correttamente).
   - Quote chiave 4 (figure musicale): `p. 9` → `p. 10` (PDF p. 10 inizio).

4. **Page numbers `overview.md` differenziatore 7** (citazioni Vaggione 2002 inline propagate dal collega):
   - kaléidoscopique: `p. 6` → `p. 7`.
   - champ spatial stable: `p. 8` → `p. 9` (PDF p. 9: «un champ spatial stable, ainsi que de les... champ toujours synchronique»).

Citazioni verificate corrette e mantenute: morphophorique p. 2, ITD 5 µs – 1.5 ms p. 5, studio numérique p. 3, kaléidoscopique Rilevanza 2 p. 7.

Out of scope review: schema deviation `vaggione2002.md` (sezione extra "Condizioni minime" tra Gap e Rilevanza — non prevista da workflow paper PDF "Schema fisso") e mancanza concept pages per object-based composition / décorrélation microtemporelle — note come follow-up non bloccante.

I refusi nelle entry log immediatamente precedenti (`p. 6/p. 8/p. 9` originali) restano come testimonianza — log append-only.

---

## [2026-05-12] ingest | Caires 2004 — IRIN: Micromontage in Graphical Sound Editing and Mixing Tool

Fonte: `raw/papers/Caires_2004_IRIN-Micromontage-Graphical.pdf` (ICMC 2004 Proceedings, Miami).
Output: `wiki/sources/papers/caires2004.md` (nuova).
Pagine toccate: 1 nuova + `wiki/sources/bibliography.md` (Wiki ✓, Sezioni 2,3,4) + `wiki/index.md` (entry sotto Vaggione 2002 per evidenziare filiazione) + `wiki/overview.md` (riga 2004 in tabella precursori CIM; aggiornata "Gap da colmare" rimuovendo Caires 2004 dai pending e aggiungendolo a ingestiti).

Sintesi:
- IRIN è Max/MSP standalone Mac OS X (offline, render finale a file multitraccia) di Carlos Caires (CICM Paris VIII, allievo di Horacio Vaggione — ringraziato come supervisor).
- Gerarchia oggetti: Sample (atomo: source file, speed, biquad filter, envelope 256pt, phase shift, shape colorato) → Figure (array Samples con onset modificabili + granulator integrato che genera particle stream con global laws su duration/distance/phase shift/filtering, poi editabile per-istanza) → Meso-structure (8-layer sequencer di Figure) → Timeline (4 track polifonici + Sound file + MIDI track).
- Differenziatore IRIN vs DAW: proprietà sonore (panning, envelope, phase shift) sono *track-independent feature* — la traccia è metafora di rigo di partitura, non bus audio. "Shapes view" mode su Timeline = primo score grafico multi-traccia per micromontage granulare con encoding cromatico-formale.
- Citazione letterale di Vaggione 2002b in nota 2: "Phase shifting in this context is used as a composition technique belonging to the micro-scale domain (*micro decorrélation temporelle*)". IRIN materializza la décorrélation microtemporelle come attributo per-sample editabile graficamente.

Rilevanza per tesi PGE:
- Conferma vitalità del tempo differito nel 2004 in piena epoca real-time disponibile (Max/MSP audio 1998); IRIN è applicazione operativa diretta del programma transformational Vaggione (1991/1996/2002b) in software, sei anni prima di PGE.
- Polo opposto in superficie compositiva (GUI direct-manipulation vs DSL YAML) sulla stessa famiglia di problemi del loop lungo.
- Timeline IRIN come precursore concreto di score_visualizer PGE: stessa categoria (study score per micromontage granulare), inversione di flusso (score editabile come input vs score come output ispezionabile); differenziatore PGE: asse Y = posizione nel buffer vs asse Y = traccia in IRIN.

Quote chiave estratte (per uso in paper): p. 1 (memory of all actions come imperativo architetturale del micromontage), p. 2 nota 2 (micro decorrélation temporelle), p. 3 (gestalt da local singularities, citando Vaggione 1996/2002a), p. 4 (tracks as metaphor for score staffs).

Aperto per sessione successiva: valutare se aprire concept page `concepts/micromontage.md` per consolidare la linea Roads 2001 cap.5 + Caires 2004 + Vaggione (filiazione); non bloccante.

---

## [2026-05-12] review-ingest | Caires 2004 — risoluzione lacune minori

Review dell'ingest precedente. Tre lacune risolte:

1. **Citazione CIM senza pagine** → ricerca web ha confermato ICMC 2004 vol. 30 pp. 219–222. Aggiornati:
   - `wiki/sources/papers/caires2004.md` sezione Citazione CIM (formato completo con vol./pp./publisher)
   - `refs.bib` entry `Caires2004` (campi `volume`, `pages`, `publisher` aggiunti)
   - Riferimenti interni alle quote: `p. 1 → p. 219`, `p. 2 nota 2 → p. 220`, `p. 4 → p. 222`

2. **Quote count = 4** vs workflow vincolo "massimo 2-3" → rimossa quote p. 221 (gestalt da local singularities, sezione 3.2): contenuto derivativo (cita Vaggione 1996/2002a già pietra-angolare nelle rispettive pagine wiki). Trattenute le 3 quote uniche di IRIN: p. 219 (memory of all actions), p. 220 nota 2 (micro decorrélation temporelle), p. 222 (tracks as metaphor for score staffs).

3. **Concept page `concepts/micromontage.md`** → creata. Sintesi cross-source di Roads 2001 cap. 5 (tassonomia tre forme: graphical/script/algorithmic) + linea Vaggione 1991/1996/2002 + Caires 2004 IRIN. PGE posizionata come quarta variante operativa della forma *algorithmic* di Roads (DSL YAML strutturato come *high-level specification*). Pagina propagata a `wiki/index.md` sezione Concepts (sotto sintesi-granulare-sincrona).

Pagine toccate: `wiki/sources/papers/caires2004.md`, `refs.bib`, `wiki/concepts/micromontage.md` (nuova), `wiki/index.md`, `wiki/log.md`.

Note di processo: la citazione mancava perché ICMC 2004 è CDROM Proceedings (verificato via `pdfinfo` Subject field) — paginazione non sempre disponibile su Crossref; localizzata via search su quod.lib.umich.edu (mirror ICMA proceedings).

---

## [2026-05-17] ingest | truax2014.md — Interacting with Inner and Outer Sonic Complexity

Fonte: `raw/papers/Truax_2014_Interacting-Inner-Outer-Sonic-Complexity-Microsound-to-Soundscape.pdf` (*eContact!* 16(3), 6 pp., online).
Output: `wiki/sources/papers/truax2014.md` (nuova).

Schema standard paper PDF applicato. Retrospettiva Truax @ 25+ anni di time-frequency methods (granular time-stretching, risuonatori, convoluzione) come quadro unificato micro/macro. Quattro corrispondenze PGE:

1. **Listening "inside" the sound** (p. 2): correlato percettivo del time-stretching granulare — l'attenzione si sposta dal contorno macro alle componenti spettrali interne. Giustificazione percettiva diretta dell'asse Y = posizione-buffer in `score_visualizer` PGE.
2. **Abstracted vs abstract processing** (p. 5): criterio di adeguatezza coerente con differenziatore 7 (per-grain effects, Roads 2012) — il design deve bring out internal aspects, non obliterating identity.
3. **Composing "through" sound** (p. 5): formula della postura compositiva del loop lungo, cugina del *composing-the-sound/with-sound* di Truax 1990b.
4. **Tassonomia computer-realized / computer-assisted / computer-composed** (p. 6): PGE come computer-assisted — partnership che cambia vocabolario, posizionamento utile in sezione 6.

Non rilevante: sezione *Soundscape Composition* (PGE non è strumento soundscape composition-specific).

Propagazione:
- `bibliography.md`: Truax2014 — Wiki ✗ → ✓; Sezioni "2" → "2, 4, 6".
- `index.md`: entry sotto truax1994.md.
- `overview.md`: radici teoriche estese con quote *listening "inside" the sound* come giustificazione percettiva dell'asse Y; contributo 2 (partitura grafica) esteso con riferimento Truax 2014 dopo Truax 1994; gap list aggiornata (Truax 2014 spostato da pending a ingestiti).

Niente nuove concept pages. Niente nuovi differenziatori (Truax 2014 rafforza differenziatore 2 e differenziatore 7 esistenti).

---

## [2026-05-17] ingest | Roads 2001 *Pulsars*

Fonte: `raw/papers/Roads_2001_Sound-Composition-Pulsars.pdf` (14 pp., JAES 49/3 March 2001, pp. 134–147).

Output: `wiki/sources/papers/roads2001-pulsars.md`.

Distinto dal libro *Microsound* (stesso anno): paper JAES su Pulsar Synthesis, implementazione PulsarGenerator (SuperCollider 2, con Alberto de Campo), 7 envelope-per-parametro (Fig. 11 GUI come precursore architetturale del `ParameterOrchestrator` PGE — uno-envelope-per-parametro, polo real-time/gestural opposto al DSL YAML). *Pulsar graph* (Fig. 5a, asse Y = note values, X = tempo) come notazione precursore a singolo parametro dello `score_visualizer`. Composizioni: *Clang-tint*, *Half-life*, *Tenth/Eleventh Vortex*. Conferma differenziatore 1 (envelope-as-interface come pattern condiviso fra real-time gestural e deferred declarative) e arricchisce tabella *Sistemi contemporanei* in overview.

Propagazione:
- `bibliography.md`: Roads2001Pulsars ✗ → ✓ (sezioni 2,3,4).
- `index.md`: entry sotto caires2004.md.
- `overview.md`: tabella *Sistemi contemporanei*: riga 2001 PulsarGenerator estesa con dettagli Fig. 7/Fig. 11 + pulsar graph; gap list aggiornata (Roads 2001 *Pulsars* spostato da pending a ingestiti).

Niente nuove concept pages. Niente nuovi differenziatori: rafforza 1 (envelope-per-parametro) + 2 (notazione grafica come strumento di lettura).

---

## [2026-05-17] ingest | Roads 2005 *The Art of Articulation: Vaggione*

Fonte: `raw/papers/Roads_2005_Art-Articulation-Vaggione.pdf` (16 pp., Contemporary Music Review 24/4-5 Aug-Oct 2005, pp. 295–309).

Output: `wiki/sources/papers/roads2005.md`.

Analisi documentata della traiettoria Vaggione 1971–2001 con accesso ai materiali compositivi. Quattro contributi forti:
1. *Tar* (1987) Fig. 2 = codice cmusic reale: `var` declarations + `ins` instrument + note-list testuale di 870 microevents (`<58 ms`, durate+amp+location quadrafonica per-evento). **Prototipo storico documentato del DSL parametrico micromontage by script** — pattern identico al YAML PGE (sound files dichiarati + envelope/strategy + eventi materializzati). Aggiunto come riga 1987 in tabella *Precursori* di overview.
2. *Schall* (1994) workflow *progressive enrichment* — quote Vaggione 1999 p. 302: «*making a frame of 7 minutes and 30 seconds and filling it by 'replacing' silence with objects, progressively enriching the texture*». Formulazione operativa del loop lungo in prima persona da un protagonista della scena.
3. Quote graphical timeline mid-1980s p. 301: «*The simple ability to align multiple sounds along a timeline [...] changed the nature of electroacoustic composition*» — razionale storico per la partitura grafica.
4. Fig. 3 IRIN score di *24 variations* (2001) con asse Y non-pitch — consolida (da Roads stesso) la parentela score_visualizer/IRIN già documentata via [[caires2004]].

Propagazione:
- `bibliography.md`: Roads2005 ✗ → ✓ (sezioni 1,2,3,4,5).
- `index.md`: entry sotto roads2001-pulsars.md.
- `overview.md`: tabella *Precursori e rami complementari*: nuova riga 1987 Vaggione/Tar via Roads 2005 (precedente CIM concreto al DSL micromontage by script); gap list aggiornata (Roads 2005 spostato da pending a ingestiti).
- `concepts/micromontage.md`: riga 2005 aggiunta in tabella linea storica + voce *Fonti*.

Niente nuove concept pages (micromontage concept rafforzato, non duplicato). Niente nuovi differenziatori: rafforza 1 (DSL) + 3 (workflow STEMS, via *progressive enrichment*).

---

## [2026-05-17] ingest | Solomos/Soulez/Vaggione 2003 *Formel/Informel: musique-philosophie* (libro)

Fonte: `raw/papers/Solomos_2003_Formel-Informel.pdf` (L'Harmattan, Paris, coll. Musique-Philosophie, 263 pp.).

Output: hub `wiki/sources/papers/solomos2003.md` + 2 sub-page:
- `solomos2003-ch04-vaggione-composition-moyens-informatiques.md` (capitolo 4 Vaggione, pp. 91–117)
- `solomos2003-ent04-de-loperatoire.md` (entretien 4 Soulez/Solomos/Vaggione, pp. 221–235)

Ingest selettivo: del libro 5 textes + 5 entretiens, solo i due capitoli con Vaggione come autore/locutore sono rilevanti per PGE. Gli altri (Adorno/Schönberg, Dahlhaus, Soulez/Wittgenstein, Solomos/Xenakis e relativi entretiens) sono di interesse musicologico/filosofico generale, fuori scope.

Tre contributi forti per il paper CIM:

1. **Objet come catégorie opératoire / unité multiple** (ch. 4 pp. 98–99). Quote-pietra-angolare per la sezione 3 del paper: «un objet [...] constitue une "unité multiple", c'est-à-dire une entité (ensemble) pouvant contenir simultanément des représentations diverses, des codes concernant autant des procédures (des actions spécifiques) que des données (des sons, des structures temporelles), embrassant une pluralité de niveaux opératoires». Descrizione *struttura per struttura* della configurazione Stream YAML di PGE. Rafforza il differenziatore 1 (DSL) e fornisce architettura concettuale per sezione 3.

2. **Triangolarità interaction = input/output/opérateur** (entretien p. 230). Legittimazione strutturale del loop lungo come configurazione opératoire deferred, non come boîte noire non-interattiva. Combinata con la frase (p. 232) «Aujourd'hui, nous sommes dans une situation où le compositeur ne se limite plus à planifier un processus pour le regarder marcher tout seul [...] il interagit à tout moment avec lui, pour produire du formel», fornisce l'aggancio argomentativo più diretto per la tesi del paper («ritorno *volontario* al tempo differito»).

3. **OOP come paradigm shift abilitante** (entretien pp. 232–233). Tesi storico-tecnica: l'approccio opératoire non era possibile nei linguaggi *structurés* 1960–70; diventa possibile con OOP. Conseguenza per PGE: l'architettura object-oriented di PGE non è scelta ingegneristica neutra, è *condizione di possibilità* dell'approccio opératoire vaggioniano. Riferimento tecnico esterno aggiuntivo segnalato da Vaggione (nota 9 entretien): Wegner *Why Interaction is More Powerful Than Algorithms*, CACM 40/5, 1997.

Altri contributi più puntuali:
- Soglia micro/macro empirica ~50 ms o 20 grains/sec (entretien p. 225) come riferimento per i default range PGE.
- Distinzione *figure/objet* (ch. 4 p. 101) come mapping concettuale grano/Stream.
- *Micro-monde du compositeur* (ch. 4 p. 100) come modello dello spazio compositivo del DSL YAML.
- *Proposition d'écoute* / version-monde Goodman (entretien p. 228) come framework per il score_visualizer.
- Immanentismo materia/forma (entretien p. 234) come argomento contro la lettura del DSL come «codifica simbolica esterna».
- *Formel = morphologique, non formalisé* (entretien p. 234) come tesi conclusiva per sezione 6.
- Lista opere Vaggione 1985–1999 (ch. 4 p. 104) come modelli stilistici per sezione 5.

Posizione rispetto a Vaggione 1991/1996/2002 già ingestiti: 2003 è la *sintesi tarda e filosofica* del programma Vaggione, dove la coppia *objet/figure* + *réseau* + *micro-monde* viene articolata in forma sistematica e dialogica. Coesistenza con 1996 (meccanica fine déclaration d'attribut) e 2002 (decorrelation): 2003 fornisce la cornice architetturale concettuale; non duplica.

Propagazione:
- `bibliography.md`: Solomos2003 ✗ → ◐ (ch4 Vaggione + ent4 De l'opératoire); sezioni paper 1, 2, 3, 4, 6.
- `index.md`: tre entry sotto roads2005.md (hub + 2 sub-page).
- `overview.md`: integrate due nuove voci nei differenziatori (objet = catégorie opératoire come argomento aggiuntivo per differenziatore 1; OOP come paradigm shift abilitante in Note sezione 3). Aggiornata gap list (Solomos 2003 spostato da pending a ingestiti parziali; Solomos 2005 resta pending).

Niente nuove concept pages (vocabolario opératoire vaggioniano già coperto in vaggione1996/vaggione2002; 2003 lo *consolida*, non lo amplia con concetti nuovi). Niente nuovi differenziatori: rafforza 1 (DSL) + introduce argomentazione storico-tecnica complementare per l'architettura OOP (sezione 3).

---

## [2026-05-17] review-ingest | Solomos 2003 — fix di propagazione e contradizione date

Review dell'ingest Solomos 2003. Tre fix applicati:

1. **`bibliography.md`** colonna Sezioni paper: `1, 2, 3, 4, 6` → `1, 2, 3, 4, 5, 6`. Hub e sub-page ch04 dichiarano entrambi la sezione 5 (lista opere Vaggione p. 104 come modelli stilistici), ma era stata omessa dalla riga di bibliografia.

2. **`concepts/micromontage.md`** aggiornato: aggiunta riga `2003 | Vaggione` nella tabella linea storica con sintesi tarda del programma (objet = catégorie opératoire, réseau d'objets numériques, micro-monde, distinzione figure/objet); aggiunte due voci nella sezione *Fonti* per le due sub-page. Il workflow paper-ingest prevede esplicitamente «Update affected concept pages» e Solomos 2003 è la generalizzazione tarda della linea Vaggione già censita in concept.

3. **Discrepanza date opere Vaggione** risolta tramite consultazione fonte primaria Solomos 2003 p. 104 (autorato da Vaggione): *Till* 1991, *Tahil* **1992**, *Kitab* 1992. Vaggione 1996 PDF nomina Tahil e Kitab ma non specifica date. Stale corretto in:
   - `overview.md` tabella precursori riga 1991/1996/2002/2003: `*Tahil* (piano solo, 1991)` → `*Till* (piano + electroacoustique, 1991), *Tahil* (piano solo, 1992)`. *Till* aggiunto (era omesso).
   - `sources/papers/vaggione1996.md` §3: «Tahil (1991) e Kitab (1992)» → «Tahil (1992) e Kitab (1992)», con nota che la datazione viene dalla lista autorata in Solomos 2003 p. 104.

Niente altre lacune residue rilevate. Hub + sub-page ch04 + sub-page ent04 confermati conformi a schema. Wegner 1997 CACM segnalato come acquisizione esterna utile per sezione 1 del paper.

---

## [2026-05-17] ingest | Solomos 2005 — *An Introduction to Horacio Vaggione's Musical-Theoretical Thought* (CMR 24/4-5)

Ingest dell'articolo di sintesi interpretativa di Solomos su Vaggione (16 pp., HAL hal-00770212). Funzione complementare a [[solomos2003]]: 2003 è quadro maturo *interno* dialogico (Vaggione locutore + Soulez/Solomos interlocutori), 2005 è *cartografia esterna* (Solomos solo, cinque assi sistematici).

File creato:
- `wiki/sources/papers/solomos2005.md` — schema fisso paper PDF, mappato su 5 assi Solomos (Interaction/Time/Morphology/Singularities/Object Networks), con sezione esplicita di relazione con ingest 2003.

Materiali concettuali estratti utili al paper CIM:
1. *Articulating Micro-Time* (titolo Vaggione 1996a, CMJ 20/1) — Solomos p. 5 lo eleva a sintesi del progetto vaggioniano. Keyword sintetica per sezione 1 e tesi loop lungo.
2. Soglia 50–100 ms / 10–20 grains-sec (p. 6) — formulazione operativa estratta da Solomos da Vaggione 1998b: 172; ridondante con citazione equivalente già censita in [[solomos2003-ent04-de-loperatoire]] p. 225, ma con riferimento bibliografico differente (CMR vs L'Harmattan) — utile come fonte secondaria autorevole in inglese.
3. *Pluralism beneath identity* (Vaggione 1998c citato p. 5) — giustificazione percettivo-compositiva della granulazione di campioni come metodo per *trovare pluralismo* sotto l'identità di un campione sorgente.
4. **Footnote 5 p. 13: Vaggione vs Roads su micro-time** — Solomos prende posizione esplicita: per Roads (*Microsound* 2002) le scale micro-temporali sono *hypostasised*; per Vaggione sono *campo postulato per ogni composizione*. Snodo cruciale per posizionamento PGE in sezione 6 — il paper può citare *via* Solomos la critica a Roads senza doverla formulare autonomamente.
5. *Operative* (p. 12, da Granger via Vaggione 2003: 224) — «*it is thought that determines both the operation and the object*». Argomento metodologico per il framework concettuale PGE (Stream/Voice/Controller) come dispositivo *operativo*, non implementazione di categorie OOP astratte.
6. Non-linearità tra scale temporali / irreducibilità (pp. 6–7) — opposizione a Xenakis GENDYN (tutto dedotto da waveform) e Grisey *Vortex temporum* (stessa outline su più scale). Conseguenza per PGE: ogni Stream è mondo morfologico con scale proprie, il global form non si deduce dal grano né viceversa.

Propagazione:
- `bibliography.md`: Solomos2005 ✗ → ✓; sezioni paper 2 → 1, 2, 3, 4, 5, 6.
- `index.md`: aggiunta entry `solomos2005.md` sotto le due sub-page di Solomos 2003.
- `overview.md`:
  - tabella precursori riga 1991/1996/2002/2003: aggiunta clausola finale che cita Solomos 2005 come cartografia interpretativa esterna del corpus vaggioniano, con menzione esplicita footnote 5 p. 13 (posizione anti-ipostatizzazione roadsiana);
  - sezione *Note per Sezione 6*: aggiunto paragrafo che usa footnote 5 p. 13 + Solomos p. 12 (operative) come contrappunto teorico complementare al *principle of economy of selection* di Roads 2012 — costruzione argomentativa per sezione 6 conclusioni (PGE eredita postura operativa multi-scala vaggioniana, non ontologia stratificata roadsiana);
  - gap list aggiornata: Solomos 2005 spostato a ingestiti; lista papers da ingestire ora vuota (tutti i PDF in `raw/papers/` censiti, salvo i proceedings CIM da identificare).

Niente nuove concept pages: il vocabolario operativo vaggioniano (objet, figure, network, écriture↔algorithme, micro-time, salience/singularity, multi-scale) è già coperto da [[vaggione1991]], [[vaggione1996]], [[vaggione2002]], [[solomos2003-ch04-vaggione-composition-moyens-informatiques]], [[solomos2003-ent04-de-loperatoire]]; Solomos 2005 lo *cartografa* e *sintetizza* per il lettore anglofono, non lo amplia con concetti nuovi.

Niente nuovi differenziatori: Solomos 2005 fornisce *legittimazione argomentativa esterna* (fonte secondaria autorevole sintetica in inglese) ai differenziatori 1 (DSL) e 6 (multi-scala), e materiale di posizionamento per sezione 6 (vs Roads).

---

## [2026-05-18] review-fix | refs.bib Solomos2005 volume

Review-ingest di Solomos 2005 rileva mismatch: wiki cita `Contemporary Music Review, 24(4-5)` (corretto: CMR vol 24 = special issue Vaggione part I, 2005), refs.bib aveva `volume = {25}` (metadata HAL errata, vol 25 è 2006). Fix `refs.bib:245`: `25` → `24`. Pagine 311–326 e altri campi invariati.

---

## [2026-05-18] ingest | roads1985.md — Granular Synthesis of Sound: Past Research and Future Prospects (VI CIM)

Fonte: `raw/proceedings/1985_CIM_VI_Atti.pdf`, pp. 195–209 (sessione *Software I*).
Output: `wiki/sources/proceedings/roads1985.md`.
Workflow: ingest paper da proceedings CIM (schema fisso).

Argomento del paper: stato dell'arte CIM 1985 della sintesi granulare. Ricostruzione storica (Gabor → Bastiaans → Xenakis → Roads 1978), enunciazione formale del problema di controllo (`d·n` parametri per minuto), confronto tra approccio *frame-based* (proposto da Xenakis 1971, mai implementato) ed *event-based* (lavoro proprio di Roads, implementato per *prototype*, *Objet*, *nscor*, *Field*), problemi delle implementazioni Music II (64 KB address space, max 32 events simultanei), programma per un environment integrato (GUI + Lisp + 4X IRCAM).

Quattro nuclei concettuali ereditati da PGE estratti come quote verbatim:
1. Problema `d·n` (p. 197) = motivazione formale del DSL YAML.
2. Frame come unità superiore al grano (pp. 197–198) = precursore CIM diretto dello Stream (con differenziatore PGE: Δt variabile per-voice vs frame isocrono Roads 1985).
3. Event a 6 coppie valore+slope (p. 200, Fig. 6) = precursore della struttura Controller/Envelope; il *trapezoid* è caso particolare di Envelope lineare a tratti PGE.
4. Polygon su piano frequency/time (p. 200, Fig. 7–9) = precursore concettuale dello `score_visualizer`; PGE inverte l'asse Y (posizione-buffer anziché frequenza) motivato dal caso d'uso granulazione di campioni.

Quote-pietra-angolare aggiuntiva (pp. 205–206): formulazione esplicita del pattern *front-end Lisp → engine* — anticipazione CIM 1985 dell'architettura YAML→Python→Csound di PGE. Quote 5 (p. 203, random deviation 2 μs → −10/−20 dB sui sidebands) come fondamento DSP della distribuzione asincrona Truax/PGE e del `dephase`.

Posizionamento storico: **primo paper CIM dedicato alla sintesi granulare**. Cronologicamente prima del DMX-1000 di Truax (1988): è la formulazione canonica CIM del problema di controllo *prima* che il paradigma real-time renda apparentemente obsoleta la questione. Pilastro dell'atto 1 della narrazione tre atti del paper CIM 2026 (tempo differito per necessità hardware → Truax 1988 atto 2 → PGE atto 3 ritorno volontario).

Propagazione:
- `bibliography.md`: `Roads1985cim` ✗ → ✓; sezioni paper aggiornate `2` → `1, 2, 3, 4`.
- `index.md`: aggiunta entry `roads1985.md` sotto `cim-survey.md` con sintesi delle 4 ereditate concettuali + quote 7.
- `overview.md`: riga tabella precursori CIM (anno 1985) riscritta con 4 quote verbatim e numeri di pagina, sostituendo il rinvio generico precedente (*"Frame ≈ Stream"*). Citazione `[[roads1985]]` aggiunta.
- `cim-survey.md`: già censito nel survey originale (sezione *1985 — VI CIM* e sezione *1985 — Roads* in *Offline con controllo algoritmico dei parametri*) — nessuna modifica richiesta.

Niente nuove concept pages: i temi (frame, event, polygon, problema `d·n`) sono già coperti da `wiki/sources/papers/roads1978.md` e `roads1988.md`. Roads 1985 ne fornisce la formulazione CIM-specifica utile per il posizionamento argomentativo nel paper, non concetti nuovi.

Nessun nuovo differenziatore: Roads 1985 *anticipa* differenziatori 1 (DSL), 6 (multi-scala vs frame isocrono), 7 (per-grain effects via random deviation) — fornisce le quote per documentare la genealogia CIM.

---

## [2026-05-19] review-fix | cim-survey.md wikilink roads1985

Review-ingest di roads1985.md rileva assenza wikilink `[[roads1985]]` in `cim-survey.md`. Fix: aggiunto `Vedi [[roads1985]].` in calce a entrambe le voci esistenti (sezione `### 1985 — VI CIM` e voce `1985 — Roads` in *Offline con controllo algoritmico dei parametri*).

---

## [2026-05-20] ingest | discipio1991.md — Caos deterministico, composizione e sintesi del suono (IX CIM)

Fonte: `raw/proceedings/1991_CIM_IX_Atti.pdf`, pp. 337–349.
Output: `wiki/sources/proceedings/discipio1991.md`.
Workflow: ingest paper da proceedings CIM.

Argomento: mappe logistiche/Verhulst/Hénon come strumento di controllo unitario su livello simbolico (macroforma) e sub-simbolico (parametri granulari: ampiezza, durata, frequenza, posizione nel buffer). Brani citati: *fractus* (1989/90), *ikon* (1991). Implementazione su IBM PC 286 in tempo differito.

Tre vettori di analogia diretta con PGE estratti come quote verbatim:
1. Riscaling iterazione non-lineare su vettore V (p. 342) = precursore di `ParameterOrchestrator` (strategia astratta → riscaling su parametro concreto).
2. xn riscalato su numero campioni per granulazione di suoni reali (pp. 344–345) = precursore di `PointerController` (mappatura buffer-position esplicita).
3. Quote pietra-angolare p. 345 — *"Queste procedure sono attualmente implementate in tempo differito, su un IBM PC 286 [...] un problema attualmente insormontabile sta nella quantità di RAM"* — formulazione CIM canonica del vincolo hardware per il deferred time (atto 1 della narrazione tre atti).

Posizionamento: chiude la fase offline-su-microcomputer CIM, immediatamente prima del passaggio real-time (Di Scipio/Tisato 1993 CIM X). Lo stesso autore enuncia il vincolo nel 1991 e contribuisce al superamento entro due anni.

## [2026-05-20] ingest | keller-rolfe1998.md — The Corner Effect (XII CIM)

Fonte: `raw/proceedings/1998_CIM_XII_Atti.pdf`, pp. 236–239.
Output: `wiki/sources/proceedings/keller-rolfe1998.md`.
Workflow: ingest paper da proceedings CIM.

Identificazione autori/titolo: il survey [[cim-survey]] e il piano `setup-workspace.md` riportavano il paper come *"MacPod: real-time granular synthesis for the Macintosh"* di Keller & Truax. Verifica visiva della title page (PDF p. 235 del volume = printed p. 236) ha rivelato che il titolo effettivo è *The Corner Effect* e gli autori sono Damián Keller (SFU) + Chris Rolfe (Third Monk Software/CCWIA). *MacPod* compare nel paper come didascalia di figura (p. 239) e come ref [11] (Rolfe 1998, Third Monk Inc.), non come titolo. Il volume 1998 di Keller & Truax sull'argomento è ICMC Ann Arbor (ref [6]), non il paper CIM. La pagina wiki è stata creata col nome corretto `keller-rolfe1998.md`.

Argomento: analisi del *corner effect* (artefatto comb-filter della finestra trapezoidale) + proposta di *ecologically-based resynthesis* con grain pool pre-costruito, phase-synchronicity inter-stream, *event* come unità di alto livello. MacPod su Macintosh PowerPC: 20 stream simultanei, grain rate min 1 ms.

Cinque vettori di analogia PGE: (1) Stream come voce indipendente (p. 237, *The stream*); (2) phase-synchronicity inter-stream (p. 237); (3) 4 modalità pointer incremental/loop/cycle/random (p. 238, *The pointer*) = precursore `PointerController`; (4) event come unità di alto livello (p. 238, *The event*) = correlazione parametrica via durata evento; (5) density via `duration × quantity of grains` (p. 238) = `DensityController`.

Posizionamento: atto 2 narrazione (real-time post-DMX-1000 su CPU general-purpose). Pattern stilistico *sezione = oggetto del sistema* (The stream/The waveform/The pointer/The event) riusabile per CIM 2026 sez. 3.

## [2026-05-20] ingest | valle-lombardo2003.md — A Two-Level Method to Control Granular Synthesis (XIV CIM)

Fonte: `raw/proceedings/2003_CIM_XIV_Atti.pdf`, pp. 136–140.
Output: `wiki/sources/proceedings/valle-lombardo2003.md`.
Workflow: ingest paper da proceedings CIM.

Identificazione autori/titolo: il survey [[cim-survey]] aveva *"A Two-Level System for Grain Generation and Control Structure"* con *autore non identificato dall'OCR*. Verifica visiva title page (PDF p. 145 = printed p. 136): titolo effettivo *A Two-Level Method to Control Granular Synthesis*; autori Andrea Valle + Vincenzo Lombardo (MultiLab/UniTo). *"GEOGRAPHY: A TWO-LEVEL SYSTEM..."* è titolo della sezione 2, non del paper.

Argomento: **GeoGraphy** — sistema formale offline a due livelli. Level I: grain generator basato su grafi diretti (vertice = grano, arco = relazione temporale con label = onset delay; *graph actant* analogo a token Petri net). Level II: map-based controller, *space actant* scansiona trajectory su mappa euclidea, distanza dai vertici → valore parametro waveform.

Cinque vettori di analogia PGE (sistema architettonicamente più vicino a PGE di quasi tutti i precursori CIM):
1. Separazione esplicita generator (level I) ↔ controller (level II) = Stream ↔ ParameterOrchestrator PGE.
2. Onset time come label di prima classe (p. 137) = `DensityController` IOT esplicito.
3. Track = sequenza polifonica (p. 137) = Stream PGE.
4. Mappa di controllo bidimensionale con space actant = precursore diretto di `score_visualizer` PGE (con asse non-frequenza).
5. Generalizzazione esplicita note + stochastic approach (p. 139) = razionale del DSL YAML come livello di astrazione che generalizza.

Quote pietra-angolare p. 139: *"a map space should be used with caution in simulating a time/frequency space"* — argomento esplicito contro l'identificazione automatica della partitura granulare con il piano tempo/frequenza, legittima la scelta PGE di asse Y = posizione nel buffer. *Objets sonores* (Schaeffer ref [24], p. 140) come anticipazione CIM della linea Vaggione/object-based.

## [2026-05-20] review-fix | propagazione + identificazione paper CIM XII/XIV

Trigger: review-ingest sui tre ingest precedenti (discipio1991, keller-truax1998, valle-lombardo2003) eseguiti da collega in sessione separata, senza propagazione.

Fix di contenuto:
- **`keller-truax1998.md` → `keller-rolfe1998.md`**: rinominato file. Titolo *MacPod...* → *The Corner Effect*; autori Keller & Truax → Keller & Rolfe; pagine `pp. ~` → pp. 236–239 (4 pp). Aggiunte page numbers a tutte le quote (p. 237 sez. *The stream*; p. 238 sez. *The pointer*/*The event*). Eliminato refuso `(p. ~13218)` (artefatto OCR). Aggiunta *Nota di identificazione* che documenta l'errore del survey.
- **`valle-lombardo2003.md`**: pagine `pp. 135–139` → `pp. 136–140`; refs `6` → `25` (lista completa); quote *map space caution* p. 138 → p. 139; quote *cumulus/stratus tassonomia* p. 138 → p. 137; Schaeffer ref `[24] non visibile nei ref.` → `visibile a p. 140 ([24] = Traité des objets musicaux, Seuil 1966)`. Aggiunta *Nota di identificazione*.
- **`discipio1991.md`**: refs `15` → `22` (conteggio verificato sez. References pp. 348–349); arricchita Note stilistiche con tre filoni (DSP / sistemi non-lineari / cognizione-estetica) ed elenco esplicito autori chiave per filone.

Propagazione applicata in questa stessa sessione:
- `bibliography.md`: chiave `KellerTruax1998 ✗` → `KellerRolfe1998 ✓` (sez. 2); chiave `Geography2003 ✗ "Autore n.d."` → `ValleLombardo2003 ✓` (sez. 2, 3, 4); `DiScipio1991cim ✗` → `✓` (sez. 1, 2, 3).
- `index.md`: aggiunte 3 entry proceedings sotto `roads1985.md`.
- `overview.md`: aggiornata riga tabella precursori `2003 | Autore n.d.` → `Valle, Lombardo` con quote verbatim p. 139; arricchita riga `1991 | Di Scipio` con quote pp. 342/344-345/345; aggiunta riga `1998 | Keller, Rolfe` in *Sistemi contemporanei* (atto 2) prima di Thall/Roads 2005.
- `cim-survey.md`: fix bug attribuzione `(& B. Truax)` → `(& C. Rolfe)`; titolo della voce 1998 corretto; aggiunti wikilink `Vedi [[discipio1991]].`, `Vedi [[keller-rolfe1998]].`, `Vedi [[valle-lombardo2003]].` in calce alle voci esistenti.

Out-of-scope (da fare in Zotero/refs.bib quando i paper saranno aggiunti come citazioni nel paper LaTeX): creazione entry `KellerRolfe1998`, `ValleLombardo2003`, `DiScipio1991cim`.

---

## [2026-05-21] review | discipio1991.md — correzione analogia ParameterOrchestrator / PointerController

Trigger: utente segnala che riga 18 (`controllo parametrico per-grano via DSL evolutivo`) postula analogia inesistente. Famiglia di controllo divergente: Di Scipio = mappe caotiche deterministiche (`xn → xn+1`, logistica/Verhulst/Hénon); PGE = tendency masks statistiche (offset + range, distribuzione uniforme/gaussiana, nessuna memoria tra grani).

File aggiornati:
- `wiki/sources/proceedings/discipio1991.md`: sezione *Analogia con PGE* riscritta — eliminato vettore #1 (ParameterOrchestrator), declassato vettore #2 (PointerController) a "da verificare", mantenuto vettore #3 (tempo differito) come unica analogia diretta; aperto blocco *Divergenza fondamentale sul modello di controllo parametrico*; *Sezioni del paper CIM 2026 dove citare*: riformulata sezione 2 come "contrasto controllato", rimossa sezione 3; commenti delle quote chiave (pp. 342, 344-345) ribilanciati su contrasto, non continuità.
- `wiki/overview.md`: riga tabella precursori `1991 | Di Scipio` ribaltata da "precursore diretto di tre meccanismi" a "precursore per contrasto controllato"; mantenuta sola analogia diretta (deferred time + ribaltamento di segno PGE).
- `wiki/index.md`: entry `discipio1991.md` riformulata coerentemente.

Out-of-scope (segnalato): stessa critica vale per analogia PointerController (vettore #2 nella vecchia formulazione). In attesa di conferma dall'utente prima di estendere ulteriormente la revisione su quel fronte.

---

## [2026-05-21] restructure | tendency mask come modello di controllo esplicito nel wiki

Trigger: utente segnala che la distinzione tendency mask (PGE) vs. caos iterativo (Di Scipio 1991) non è esposta in modo chiaro nel wiki — emerge solo in `discipio1991.md` dopo la revisione precedente, ma le pagine PGE (parameter-orchestrator, stream) non nominano mai esplicitamente il pattern, né documentano `UniformDistribution` / `GaussianDistribution`, né dichiarano l'indipendenza fra grani.

File aggiornati:
- `wiki/sources/pge/parameter-orchestrator.md`: nuova sezione *Modello di controllo: tendency mask* con (a) definizione operativa (Envelope `center(t)` + `mod_range` `spread` + `distribution_mode` + `ProbabilityGate`), (b) implementazione concreta letta da `raw/PythonGranularEngine/src/shared/distribution_strategy.py` (formule Uniform/Gaussian, clamping bounds), (c) proprietà chiave (indipendenza fra grani, `n+1 ⊥ n`), (d) contrasto controllato con Di Scipio 1991 (mappe caotiche con dipendenza `xn+1 = f(xn)`).
- `wiki/concepts/tendency-mask.md`: **pagina concept nuova** (cross-source). Definizione, lineage Koenig/Truax/PGE, contrasto Di Scipio, implementazione, sezioni paper CIM 2026 dove descrivere, domande aperte.
- `wiki/overview.md`: aggiunto differenziatore #8 *Modello di controllo parametrico: tendency mask, non caos iterativo* con quote di implementazione e wikilink a `[[discipio1991]]` e `[[parameter-orchestrator]]`.
- `wiki/index.md`: nuova entry sotto *Concepts* per `tendency-mask.md`; entry esistente di `parameter-orchestrator.md` arricchita con esplicito riferimento al modello tendency mask e contrasto con caos iterativo.

Conferma utente per estensione: pendente la revisione equivalente su `PointerController` (analogia #2 originale in discipio1991.md, ora declassata a "da verificare"). Da fare solo dopo conferma esplicita.

---

## [2026-05-21] review | discipio1991.md — estensione critica a PointerController + rimozione riferimento Koenig

Trigger: utente conferma che anche analogia #2 originale (`PointerController` ↔ Di Scipio pp. 344-345 "xn riscalato sul numero dei campioni") va declassata a contrasto controllato — stessa logica del declassamento di analogia #1: PGE seleziona posizione di lettura via tendency mask statistica (Envelope `loop_start/loop_end/speed_ratio` + range stocastico, indipendenza fra grani), Di Scipio via mappa caotica iterativa. Inoltre rimosso riferimento a Koenig come origine pattern tendency mask perché non attestato da fonti ingestite (solo letteratura standard, non in `raw/`).

File aggiornati:
- `wiki/sources/proceedings/discipio1991.md`: sezione *Analogia con PGE* riscritta — eliminata "Nota su granulazione di buffer (da verificare)", estesa la *Divergenza fondamentale* per coprire esplicitamente sia `ParameterOrchestrator` sia `PointerController`; commento quote pp. 344-345 ribilanciato su contrasto controllato; lineage tendency mask attribuito unicamente a Truax 1988.
- `wiki/concepts/tendency-mask.md`: rimosso punto Koenig dal lineage storico; aggiunta domanda aperta su ingest pre-Truax (manuale PR2 o fonte secondaria affidabile) come prerequisito per citare lineage Koenig nel paper CIM 2026.
- `wiki/sources/pge/parameter-orchestrator.md`: rimosso riferimento Koenig nella sezione *Modello di controllo: tendency mask*.
- `wiki/overview.md`: rimosso "Koenig anni '70" dal differenziatore #8.
- `wiki/index.md`: rimosso "Koenig" dall'entry concept *Tendency mask*.

---

## [2026-05-21] review | valle-lombardo2003.md — riformulazione space actant ≠ score_visualizer (anti-analogia)

Trigger: utente chiarisce che il `score_visualizer` PGE è semplicemente una *partitura di test* (PDF read-only post-rendering, verifica che il YAML produca quanto atteso) e chiede di rileggere meglio cos'è lo *space actant* di Valle/Lombardo prima di affermare l'analogia. Re-lettura del paper (pp. 137-139 via `pdftotext` da `raw/proceedings/2003_CIM_XIV_Atti.pdf`):

Space actant = **scanning device che percorre una trajectory disegnata dal compositore nello map space a rate costante**. La sua distanza da ogni vertice modula parametri (pan, ampiezza, bandwidth) del grano associato (*"parameters value ranges are mapped onto spatial distance, and the nearer is a trajectory to some vertex, the higher is the value of some parameter for the grain waveform represented by that vertex"*, p. 137). È un **input di controllo compositivo**, parte della specifica del brano.

Il `score_visualizer` PGE è il suo **opposto funzionale**: output diagnostico read-only generato post-rendering per verificare il comportamento del YAML. Direzione del flusso, ruolo nel loop compositivo, editabilità, contenuto rappresentato (eventi attuali vs potenziali): tutto opposto.

L'analogia precedente (vettore #4 nella pagina, e nella riga `2003 | Valle, Lombardo` di `overview.md`) era basata sulla coincidenza superficiale "rappresentazione 2D + asse Y non-frequenza" — proiezione, non analogia strutturale. La quote p. 139 sul time/frequency space discute un limite intrinseco di GeoGraphy (mappa di eventi potenziali separata dal generator), non legittima Y=buffer in PGE.

File aggiornati:
- `wiki/sources/proceedings/valle-lombardo2003.md`: sezione *Analogia con PGE* completamente riscritta — da "5 vettori, uno dei quali precursore diretto del score_visualizer" a "4 vettori a forza decrescente + anti-analogia chiarificatrice space actant ≠ score_visualizer" con tabella di confronto direzione-flusso / ruolo / contenuto / editabilità / funzione nel loop; *Sezioni del paper CIM 2026 dove citare* sez. 4 riformulata da "precursore diretto" a "contrasto di flusso". Il differenziatore PGE sulla partitura non è la scelta Y ≠ frequenza (già nello stato dell'arte CIM: Truax 1988 Fig. 4, GeoGraphy, IRIN) ma l'**inversione di flusso** (rendering → partitura, non partitura → rendering).
- `wiki/overview.md`: riga tabella precursori 2003 ribilanciata (cinque vettori → quattro + anti-analogia); rimossa l'affermazione che lo space actant legittima Y=buffer.
- `wiki/index.md`: entry `valle-lombardo2003.md` riformulata coerentemente.

Vettori conservati (con calibrazione): (1) separazione strutturale come analogia *di principio*, non struttura-a-struttura (PGE = pipeline sequenziale, GeoGraphy = strutture parallele); (2) onset come label di prima classe (solido); (3) track/grain (solido, meccanismi divergenti); (4) generalizzazione note+stochastic (postura argomentativa, meccanismi diversi).

---

## [2026-05-21] ingest | arcella-silvestri2012.md (XIX CIM, 2012)

Trigger: utente richiede prossimo ingest proceedings CIM, uno per volta.

Fonte: `raw/proceedings/2012_CIM_XIX_Atti.pdf`, pp. 144–148 (PDF pp. 9343–9700 nel testo concatenato). Comunicazione scientifica, 5 pagine, 9 ref. Autori: Andrea Arcella, Stefano Silvestri (Conservatorio di Napoli).

Argomento: ricostruzione software di *Analogique B* di Xenakis (1958–59, considerato dagli autori — sulla scia di Roads CMT — il primo brano basato su sintesi granulare; nota: paper cita ref [6]=Gabor per questa attribuzione, probabile refuso per ref [5]=Roads). Architettura a due moduli: `score.cpp` (C++, itera MPT 8×8) → `Xscore.txt` (Csound score) → `Analogique.csd` (orchestra con `grain` opcode, 8 strumenti A–H, 10 grain generators sovrapposti per strumento) → audio. Esplicitamente *out-of-time, additive* (p. 147); *offline* by design.

Posizionamento PGE: **precursore CIM architetturale più diretto** tra quelli censiti finora nel survey. Stessa topologia *algoritmo → score → Csound → audio*, fattorizzazione esplicita in due moduli (quote p. 147 *"Our software implementation factors the whole problem in two"*). Quote pietra-angolare p. 148 *"Tools and technologies used to produce a musical work are not neutral but incorporate knowledge that influence the choices of the composer"* = formulazione CIM diretta della tesi paper sul carattere non-neutrale degli strumenti compositivi (ancoraggio CIM per Sezione 1 narrazione tre atti + Sezione 6 conclusioni).

Differenziatore PGE: **livello di astrazione del modulo algoritmico**. Arcella/Silvestri scrivono score Csound testuale direttamente da C++ imperativo (specifico al brano, renderer-coupled). PGE introduce YAML dichiarativo + IR Python (`Stream`/`Grain`) intermedia: cambio renderer senza toccare specifica, editing assistito PGE-ls, cache SHA-256 per-stream, workflow STEMS. Anti-analogia formalizzata con tabella di confronto (livello specifica / IR / renderer / editing / cache / riusabilità).

File creato/aggiornati:
- **Nuovo**: `wiki/sources/proceedings/arcella-silvestri2012.md` (schema fisso CIM proceedings: citazione, categoria, argomento, sistema descritto, 4 vettori analogia + anti-analogia, posizionamento storico, note stilistiche, sezioni paper, quote chiave).
- `wiki/overview.md`: riga tabella precursori 2012 espansa da one-liner a entry corposa con quote pietra-angolare e differenziatore PGE esplicito; riferimento [[arcella-silvestri2012]].
- `wiki/sources/proceedings/cim-survey.md`: entry 2012 nel catalogo per anno integrata con quote conclusiva p. 148 e link [[arcella-silvestri2012]]; entry nel sottoinsieme *tempo differito* affinata sulla fattorizzazione esplicita p. 147 e sul differenziatore IR Python.
- `wiki/sources/bibliography.md`: chiave `Arcella2012` aggiornata da ✗ a ✓, colonna sezioni paper aggiornata `2, 3` → `1, 2, 3, 6` per riflettere ancoraggio CIM della tesi non-neutralità strumenti.
- `wiki/index.md`: nuova entry sotto *Sources — Proceedings*.

---

## [2026-05-21] review-ingest correction | arcella-silvestri2012

Trigger: review-ingest workflow su ingest precedente della stessa sessione. Tre lacune identificate, tutte corrette.

1. **Page reference error**: quote *"Our software implementation factors..."* e *"out-of-time, additive procedure"* citate erroneamente a p. 146. Verifica diretta sul PDF (PDF p. 154 = paper p. 147, sezione 5 inizia su p. 147). Corretto p. 146 → p. 147 in: `arcella-silvestri2012.md` (4 occorrenze: linee 30, 38, 92, 93), `overview.md` (2 occorrenze nella riga tabella precursori 2012), `cim-survey.md` (1 occorrenza), `log.md` (3 occorrenze nell'entry precedente). Riferimenti corretti a Figure 5/6 e nota 3 a p. 146 mantenuti.
2. **Attribuzione ref [6]**: parafrasi *"citando Roads CMT"* sostituita inferenza editoriale al ref number paper. Ref [6] in bibliografia = Gabor 1947, non Roads (=[5]). Probabile refuso del paper originale. Aggiunta nota esplicita in `arcella-silvestri2012.md:10` e nella Quote chiave p. 144.
3. **Figura 7 caption**: nel paper Figura 7 è captioned *"Single grain"* (duplicato del caption di Figura 6), ma il contenuto è il diagramma a blocchi `score.cpp → Xscore.txt → Analogique.csd → Csound rendering`. Aggiunta annotazione del refuso in `arcella-silvestri2012.md` sez. *Sistema descritto* e sez. *Note stilistiche*.

File modificati: `arcella-silvestri2012.md`, `overview.md`, `cim-survey.md`, `log.md` (questa entry).


---

## [2026-05-21] ingest | rizzuti2006 — Il "caos sonoro" (XVI CIM)

Fonte: `raw/proceedings/2006_CIM_XVI_Atti.pdf` (Costantino Rizzuti, abstract esteso ~1.5 pp, 4 riferimenti).

Sintesi: mappa logistica `xt+1 = c·xt·(2−xt)` per controllo deterministico di ampiezza, durata, onset, frequenze parziali. CSound offline, due strumenti separati (eventi + grani). Posizionamento: secondo data-point CIM del filone caotico-iterativo dopo Di Scipio 1991 — stessa famiglia anti-precursore PGE (caos iterativo vs tendency mask statistico). Architettura due-strumenti CSound = precursore debole della separazione Stream/grano PGE; differenza: Rizzuti tiene tutto dentro CSound (no DSL above), mentre PGE separa YAML/IR Python dal rendering. Meno diretto di Arcella-Silvestri 2012 (che ha fattorizzazione esplicita `C++ → CSound`). Densità tecnica del paper troppo bassa per trattazione di corpo: citabile in sez. 2 come nota documentale del filone.

File creati/aggiornati:
- **Nuovo**: `wiki/sources/proceedings/rizzuti2006.md` (schema CIM proceedings completo).
- `wiki/sources/proceedings/cim-survey.md`: aggiunto link `[[rizzuti2006]]` in entry 2006 — XVI CIM e in entry *tempo differito*.
- `wiki/sources/bibliography.md`: `Rizzuti2006` ✗ → ✓.
- `wiki/index.md`: nuova entry sotto *Sources — Proceedings*.

---

## [2026-05-21] review-ingest correction | rizzuti2006

Trigger: review-ingest workflow su ingest precedente della stessa sessione. Gap propagazione + due nit identificati, tutti corretti.

1. **Gap overview.md (propagazione mancante)**: riga 41 tabella precursori `2006 | Rizzuti` rimasta nello stato pre-ingest (one-liner `partitura → strumento eventi → grani ≈ YAML → Python → .sco`) — incoerente con framing post-ingest della pagina wiki (anti-precursore famiglia di controllo + precursore architetturale **debole** rispetto ad Arcella-Silvestri 2012). Riga riscritta con framing nuovo: secondo data-point CIM caos iterativo dopo Di Scipio 1991, anti-analogia tendency mask, architettura due-strumenti come precursore *di principio* (no DSL above), nota su densità tecnica bassa (non modello stilistico). Aggiunti link `[[rizzuti2006]]`, `[[discipio1991]]`, `[[tendency-mask]]`.
2. **Nit quote senza numero pagina**: aggiunto riferimento `(atti PDF p. 20)` e `(atti PDF p. 21)` alle due quote chiave in `rizzuti2006.md`. CIM XVI Atti non riporta numeri di pagina stampati, quindi annotata convenzione `atti PDF p. N` con nota esplicativa.
3. **Nit concept tendency-mask non aggiornato**: in `wiki/concepts/tendency-mask.md` sez. *Contrasto controllato con Di Scipio 1991*, aggiunto paragrafo finale che cita `[[rizzuti2006]]` come secondo data-point CIM del filone caotico-iterativo, ristretto alla logistica, con rivendicazione esplicita di deterministico vs stocastico. Compounding del concept con il nuovo ingest.

File modificati: `overview.md`, `rizzuti2006.md`, `tendency-mask.md`, `log.md` (questa entry).

---

## [2026-05-21] ingest | sparano2018.md — GrainLab — Software open source per la sintesi granulare quasi-sincrona

Fonte: `raw/proceedings/2018_CIM_XXII_Atti.pdf`, pp. 243–245 (3 pp., 7 refs, 4 figure).
Output: `wiki/sources/proceedings/sparano2018.md` (schema CIM proceedings completo).

Sintesi: GrainLab — granulatore quasi-sincrono Max/MSP+Gen real-time per live electronics da ensemble. Singolo segnale rampa pilota con sfasamenti deterministici (preset *continuous*/*rhythmic*) o aleatori, 9 preset finestratura (Hann/Expodec/Rexpodec/Triangle/Trapezoid/Sinc + 3 alternanze), densità via duty cycle, cambio parametri click-free via Sample&Hold sincronizzato a fase 0. Caso d'uso: *FENIX DNA* di Plessi al Teatro La Fenice (lug-ago 2017), 5 istanze per ensemble (flauto, cl. basso, viola, pianoforte, soprano).

Posizionamento: polo opposto a PGE su entrambi gli assi (real-time vs deferred; patch monolitica Max/MSP vs DSL+IR+renderer Python). **Anti-precursore di `DensityController`**: distribuzione IOT deterministica via fasi del segnale rampa, non stocastica via density probabilistica come Truax/PGE. Conferma il **cluster real-time italiano post-2000** (con Markidis/Fernández 2016, Pozzi 2016, Cera 2022, Markidis 2024) come polo gestural-improvvisativo della tradizione CIM, opposto al ramo offline Di Scipio 1991 / Arcella-Silvestri 2012 / PGE.

Bibliografia di sole 7 ref con 6 fonti core canoniche granulari (Gabor 1947, Xenakis *Formalized Music*, Roads CMJ 1988, Truax CMJ 1988, Roads CMT 1996, Roads Microsound 2001) — utile come limite inferiore di densità citazionale per CIM tool papers. PGE paper non può adottare questo stile (target 6-8 pp, postura argomentativa, 9-21 ref) ma conferma che tool description 3 pp con bibliografia minima è formato accettato in CIM.

File creati/aggiornati:
- **Nuovo**: `wiki/sources/proceedings/sparano2018.md`.
- `wiki/sources/proceedings/cim-survey.md`: entry Sparano 2018 estesa con numeri pagina, tecniche specifiche, link `[[sparano2018]]`.
- `wiki/sources/bibliography.md`: `Sparano2018` ✗ → ✓.
- `wiki/index.md`: nuova entry sotto valle-lombardo2003.

Nessun aggiornamento a `overview.md`: Sparano non è precursore diretto (real-time post-PGE-line) né anti-precursore strutturalmente rilevante; citabile solo come data-point del cluster real-time post-2000. Nessuna nuova concept page.

---

## [2026-05-21] review-ingest | sparano2018.md — fix imprecisioni + propagazione deepening

Trigger: review-ingest workflow su ingest precedente della stessa sessione. Gap: 1 imprecisione fattuale, 1 framing overstated, 1 gap propagazione overview.md, 1 compounding non eseguito.

1. **Imprecisione fattuale preset finestratura**: pagina e cim-survey dicevano "9 preset (Hann/Expodec/Rexpodec/Triangle/Trapezoid/Sinc + 3 alternanze)". PDF sez. 2.3 specifica: 6 funzioni base in 9 preset; preset 7 = rotazione di tutte le 6 finestre su gruppi di 6 grani successivi (non alternanza), preset 8 = alternanza Expodec/Rexpodec, preset 9 = alternanza Hann/Sinc. Fix in `sparano2018.md` (sez. Argomento + Analogia), `cim-survey.md` entry Sparano, `index.md` entry Sparano.

2. **Framing "cluster real-time italiano post-2000" overstated**: i membri elencati (Markidis/Fernández 2016, Pozzi 2016, Cera 2022, Markidis 2024) sono real-time italiani CIM post-2000 ma su tecniche eterogenee — Pozzi è concatenativa (Boids), Cera è interactive sonification del gesto (DanzArTe), Markidis 2024 è ecosystemic mediation, Markidis/Fernández 2016 è analisi+sintesi con riconoscimento timbrico. Solo Sparano è granulare in senso stretto. Riformulato in `sparano2018.md` sez. Posizionamento storico (e propagato in `index.md`) come "data-point isolato del *granulare* real-time italiano CIM post-2000" con elenco esplicito dei contemporanei real-time per tecniche affini ma non granulari.

3. **Gap propagazione overview.md**: tabella "Sistemi contemporanei (poli compositivi opposti)" saltava da 2006 Ynez a 2021 EC2. Aggiunta riga 2018 Sparano con: caso *FENIX DNA*, opposizione real-time/deferred + monolitico/DSL, anti-precursore di `DensityController` (fase-based deterministico vs density-based stocastico), vincolo S&H a fase 0 specifico real-time, bibliografia 7 ref come limite inferiore di densità citazionale CIM.

4. **Compounding `density-controller.md`**: claim "anti-precursore di `DensityController`" presente in `sparano2018.md` ma non back-referenziato nella pagina PGE corrispondente. Aggiunta sezione "Anti-precursore CIM — Sparano 2018 (GrainLab)" in `wiki/sources/pge/density-controller.md` che esplicita il contrasto fase-based deterministico vs density-based stocastico su due assi (architettura + regime di controllo IOT) e l'utilità per Sezione 2/3 del paper CIM 2026 come ancoraggio CIM dell'alternativa scelta da PGE.

File modificati: `sparano2018.md`, `cim-survey.md`, `index.md`, `overview.md`, `density-controller.md`, `log.md` (questa entry).

---

## [2026-05-21] ingest | cera2022 — Interactive Sonification of Expressive Gesture (XXIII CIM)

Fonte: `raw/proceedings/2022_CIM_XXIII_Atti.pdf`, pp. 79–86 (comunicazione orale, 33 refs, nessuna figura). Autori: Cera, Canepa, Ferrari, Pilotto, Coletta, Ghisio, Camurri (Casa Paganini-InfoMus + E.O. Galliera).

Sintesi: sistema multimodale real-time per anziani fragili (progetto DanzArTe). Sonificazione interattiva del gesto via Kinect II + EyesWeb + Max/MSP+Ableton. Tecnica granulare (sez. 5.3): coppia di granulatori per motore — principale finestra 5 s con transp. −1 ottava + secondario finestra 1 s no-transp. −10 dB, head condivisa con jitter; sound-file diviso in 12 sezioni armoniche, head migra in 15-20 s. Cita **Lippe 1994** (IRCAM ISPW, *Contemporary Music Review* Vol. 10) come unica fonte canonica granulare in 33 ref — stesso Lippe del CIM X 1993 nel survey. Apre con citazione Valéry 1938 contro la velocità, paradigma *Slow Mood* + *Aesthetic Resonance*.

Posizionamento: estensione del cluster **real-time italiano CIM post-2000** già documentato in `sparano2018.md` (ora 5 data-point: Markidis/Fernández 2016, Pozzi 2016, Sparano 2018, Cera et al. 2022, Markidis 2024). Cera et al. occupa il **polo applicativo** del cluster — granulazione come strumento operativo per obiettivo extra-compositivo (sonificazione del gesto), non oggetto di studio di prima classe come in Sparano. Nessuna analogia architetturale con PGE (polo opposto su tempo + architettura + dominio). Due analogie indirette di postura: (a) coppia di granulatori finestra-eterogenea (5:1) come pattern multi-voce non-omogeneo — debole analogia con VoiceManager PGE che è omogeneo per definizione; (b) postura anti-velocità esplicita (Valéry, Slow Mood) come *ancoraggio CIM contemporaneo* della tesi PGE del loop lungo — citabile in sez. 6 con cautela (sonificazione fruitiva vs processo compositivo: stessa intuizione applicata a domini diversi).

Densità citazionale opposta a Sparano: 33 ref interdisciplinari (psicologia musicale, audio descriptors, HCI sonification, studi sul movimento, geriatria, filosofia) con **una sola fonte canonica granulare** (Lippe 1994). Conferma che CIM accetta sia tool papers tecnici (Sparano 7 ref) sia paper argomentativi alta-densità (Cera et al. 33 ref) — utile come modello per CIM 2026 (target 9-21 ref).

File creati/aggiornati:
- **Nuovo**: `wiki/sources/proceedings/cera2022.md` (schema CIM proceedings completo).
- `wiki/sources/proceedings/cim-survey.md`: entry 2022 espansa da menzione tecnica a entry corposa con numeri pagina, tecnica granulare dettagliata, postura Slow Mood, link `[[cera2022]]`. Sottoinsieme real-time: lista data-point con link `[[cera2022]]` e `[[sparano2018]]`.
- `wiki/sources/bibliography.md`: chiave `[CIM2022-tbd]` ✗ → `Cera2022` ✓, colonna sezioni paper `2, 6`.
- `wiki/index.md`: nuova entry sotto `cera2022.md` immediatamente prima di `sparano2018.md`.

Nessun aggiornamento a `overview.md`: Cera et al. non è precursore architetturale né anti-precursore strutturalmente rilevante (real-time applicativo, dominio non compositivo). La postura Slow Mood è ancoraggio culturale contiguo, non strutturale — citabile direttamente nel testo del paper CIM 2026 sez. 6 senza richiedere riga di tabella nei differenziatori PGE.

Nessuna nuova concept page. Il concetto *loop lungo* non ha ancora pagina dedicata in `wiki/concepts/` (vive in `overview.md`); aspirazionalmente notato come gap.

---

## [2026-05-21] review-fix | cera2022 — chiusura lacuna overview

Trigger: review-ingest workflow su ingest cera2022 della stessa sessione. Lacuna borderline identificata: la pagina `cera2022.md` e `bibliography.md` (sez. `2, 6`) sostengono che Slow Mood + esplicitazione della *scala temporale* sono ancoraggio CIM contemporaneo della tesi PGE del loop lungo, ma `overview.md` (tesi in evoluzione) non back-referenziava il claim → rischio drift in fase di scrittura sez. 6.

Fix:
1. Aggiunto paragrafo "Ancoraggio CIM contemporaneo della postura anti-velocità" alla sezione "Note per Sezione 6 del paper — economy of selection come teorizzazione del loop lungo" in `overview.md`. Quote Valéry 1938 + paradigma Slow Mood + quote p. 79 *"to rediscover the long time"* inserite verbatim. Differenza esplicita di dominio (fruizione real-time vs processo compositivo deferred) annotata per evitare collassi tesi-a-tesi.
2. Aggiornata sezione "Gap da colmare" in `overview.md`: "Atti CIM 2022 e 2024" → "Atti CIM 2024" (2022 ora coperto da [[cera2022]] e [[sparano2018]]).

File modificati: `overview.md`, `log.md` (questa entry).

Concept page *loop lungo* in `wiki/concepts/` resta gap aspirazionale (Step 5 piano, non eseguito in questa sessione).

---

## [2026-05-21] demote | cera2022 — marcato marginale, non citare

Decisione editoriale: Cera et al. 2022 marcato come fonte **marginale**, esclusa dalle citazioni del paper CIM 2026. Motivazione: dominio (sonificazione interattiva applicata a riabilitazione cognitiva anziani fragili) non sovrapponibile a PGE; granulazione usata come strumento operativo extra-compositivo; né precursore architetturale né anti-precursore strutturale; l'analogia *Slow Mood ↔ loop lungo* è troppo distante (pacing fruizione vs pacing processo compositivo) per reggere come ancoraggio citazionale CIM.

Fix propagati:
1. `wiki/sources/proceedings/cera2022.md`: riscritto. Banner di status marginale in testa; sezioni ridotte all'essenziale (citazione, lunghezza, argomento, motivi marginalità, decisione, condizione di rivisitazione).
2. `wiki/overview.md`: rimosso il paragrafo "Ancoraggio CIM contemporaneo della postura anti-velocità" aggiunto nel fix precedente (sezione "Note per Sezione 6"). Aggiornata sezione "Gap da colmare": Cera marcato come ingestito ma marginale.
3. `wiki/sources/bibliography.md`: colonna Wiki da `✓` a `✓ (marginale, non citare)`; colonna Sezioni da `2, 6` a `—`. Chiave `Cera2022` mantenuta per tracciabilità del volume CIM XXIII.
4. `wiki/index.md`: entry ridotta da bullet corposo a riga breve con flag "Marginale — non citare nel paper CIM 2026"; rimosso anche `Cera 2022` dalla lista contemporanei nell'entry `sparano2018` (era citato come data-point del cluster real-time italiano post-2000, ora marginale).
5. `wiki/sources/proceedings/cim-survey.md`: entry 2022 ridotta da paragrafo dettagliato a 2 righe con flag marginalità.

Condizione di rivisitazione: se sez. 6 del paper richiederà un ancoraggio CIM contemporaneo della postura anti-velocità e nessuna altra fonte CIM lo offrirà, riaprire la decisione e annotarlo in `log.md`.

File modificati: `cera2022.md`, `overview.md`, `bibliography.md`, `index.md`, `cim-survey.md`, `log.md` (questa entry).

---

## [2026-05-21] ingest | proceedings Ortosecco/Piccialli 1989 — Sintesi granulare e DSP CIM VIII

Fonte: `raw/proceedings/1989_CIM_VIII_Atti.pdf` (pp. 58–67)
Output: `wiki/sources/proceedings/ortosecco-piccialli1989.md`

Identificazione wavelet=grano (via Roads 1985) come base teorica della sintesi granulare. Implementazione channel vocoder a wavelets su scheda Ariel TMS 32025 / PC AT. Offline. Linea italiana CIM post-De Poli/Piccialli 1988.

Analogie con PGE — tre punti di contatto indiretti:
1. Tabulazione del grano: wavelet prototipo tabulata su 4096 campioni, grani per sottocampionamento dalla tabella base — pattern *precompute-once / reuse-many* analogo al `WindowGenerator` PGE.
2. Separazione analisi/sintesi: livello analitico (coefficienti wavelet) separato dal livello sintetico (risintesi) — analogo al pattern *spec dichiarativa → IR → rendering* di PGE.
3. Offline come fase metodologica esplicita (non rifiuto del real-time): "implementazioni in tempo reale già in via di progettazione" — postura affine al loop lungo PGE in chiave 1989.

Nessuna analogia diretta a livello di pipeline: PGE non fa analisi, parte da specifica YAML.

Fix propagati:
1. `wiki/sources/proceedings/ortosecco-piccialli1989.md`: nuova pagina con schema fisso proceedings CIM.
2. `wiki/sources/proceedings/cim-survey.md`: entry 1989 espansa con dettagli (pp. 58–67, identificazione wavelet=grano, scheda Ariel, citazione De Poli/Piccialli 1988); aggiunta nuova sotto-sezione "Fondazione DSP/wavelet della sintesi granulare" nel confronto offline con PGE.
3. `wiki/sources/bibliography.md`: aggiunta riga `OrtoseccoPiccialli1989 | Ortosecco, Piccialli 1989 | CIM VIII | ✓ | 2`.
4. `wiki/index.md`: nuova entry sotto Sources — Proceedings.
5. `refs.bib`: entry BibTeX da aggiungere (TODO — chiave `OrtoseccoPiccialli1989`).

File modificati: `ortosecco-piccialli1989.md` (nuovo), `cim-survey.md`, `bibliography.md`, `index.md`, `log.md` (questa entry).

---

## [2026-05-21] review-fix | ortosecco-piccialli1989 — chiusura lacune review

Trigger: review-ingest workflow su ingest ortosecco-piccialli1989 della stessa sessione. Tre fix + un chiarimento.

Lacune chiuse:
1. **Quote chiave assenti**: aggiunta sezione "Quote chiave" in `ortosecco-piccialli1989.md` con verbatim apertura (*"metodo intuitivo per modellare sorgenti sonore"*), posizionamento storico (*"ha avuto scarse applicazioni"* + *"una solida base teorica"*), tesi centrale identificazione wavelet=grano, chiusura sulla prospettiva real-time (*"strutture di calcolo ad alto parallelismo permetterà in futuro implementazioni in tempo reale già in via di progettazione"*). Schema proceedings CIM non richiede esplicitamente la sezione, ma il workflow paper PDF sì — uniformazione utile per riusi futuri.
2. **`overview.md` non toccato dall'ingest**: aggiunta menzione in "Radici teoriche" (paragrafo Gabor/Roads/Truax/De Poli/Piccialli). Ortosecco/Piccialli 1989 chiude la triade ramo CIM italiano 1988→1989→1991 e fornisce il primo ancoraggio CIM esplicito del pattern *precompute-once / reuse-many* (wavelet tabulata 4096 campioni, grani per sottocampionamento) analogo a `WindowGenerator` PGE. Non aggiunta riga nella tabella precursori — Ortosecco/Piccialli 1989 è precursore *teorico DSP*, non architetturale; la menzione in "Radici teoriche" è il livello editoriale corretto.
3. **Deviazione piano `setup-workspace.md` (Livello C "ignora") non annotata**: aggiunta `OrtoseccoPiccialli1989` alla lista cita di Sezione 2 in `next-session.md` con nota di posizionamento (ramo CIM italiano post-DePoli/Piccialli 1988 + pattern precompute-once/reuse-many). La scelta editoriale di ingestire CIM VIII fuori piano è ora visibile nel piano di scrittura — non più solo nel `log.md`.

Chiarimento `refs.bib` (non lacuna specifica dell'ingest):
- CLAUDE.md prescrive *"Non modificare a mano"* `refs.bib`; gestione via Zotero + Better BibTeX, batch.
- Stato attuale: chiavi proceedings CIM (DiScipio1991, Roads1985, Rizzuti2006, Arcella2012, KellerRolfe1998, ValleLombardo2003, Sparano2018, Cera2022, OrtoseccoPiccialli1989) tutte registrate in `wiki/sources/bibliography.md` con `✓`, nessuna entry in `refs.bib`. Pattern coerente con tutti i precedenti ingest proceedings — non è regressione dell'ingest Ortosecco.
- Implicazione operativa: prima della compilazione `paper.tex`, batch Zotero per popolare `refs.bib` con tutte le chiavi proceedings pre-allocate.

Borderline non chiuso (lasciato esplicito):
- Concept page `precompute-once-reuse-many` (pattern cross-cutting tra `WindowGenerator` PGE e Ortosecco/Piccialli 1989 wavelet table): non creata. Pattern citato in `overview.md`, `cim-survey.md` e `ortosecco-piccialli1989.md`, ma un singolo data-point storico non giustifica ancora una concept page propria (rischio over-generalizzazione). Da rivisitare se un secondo data-point CIM (es. lettura tabella di waveforms in altri sistemi storici) emerge dall'ingest.

File modificati: `ortosecco-piccialli1989.md`, `overview.md`, `next-session.md`, `log.md` (questa entry).

---

## [2026-05-21] ingest | proceedings Di Scipio/Tisato 1993 — Granular synthesis with ICMS CIM X

Fonte: `raw/proceedings/1993_CIM_X_Atti.pdf` (pp. 159–165, 7 pp, 16 refs)
Output: `wiki/sources/proceedings/discipio-tisato1993.md`

Sistema ICMS (Tisato, prima release 1975, mainframe IBM 9121 time-sharing al Centro di Calcolo Ateneo Padova). Sottomenu `GRANULAR PROC.` con 7 opzioni di controllo del puntatore (constant-variable step / Brownian 1/f² / Gaussian / discubic / logistic / Verhulst / May) + tendency-mask control per grain duration/delay/amplitude/file-portion. Layering ricorsivo di stream con mixing coefficients dichiarativi. Phase-level switches (reverse/repetition/offset/inversion) ad attivazione 50%-probabilistica. Pipeline 3-step per grano (pointer → read → envelope/write target). Brano *zeitwerk (l'orizzonte delle cose)* (1992) con 8 sinusoidi a frequenza fissa come unico source. Offline.

Cinque vettori di analogia con PGE:
1. **Pipeline 3-step grano** (p. 160) = primo precedente CIM a livello di pseudocodice del loop `Stream.generate_grains()` PGE.
2. **Quote pietra-angolare p. 165** *"a single rule may instantiate multiple operations [...] step towards the abstract"* = **programma DSL ante litteram CIM 1993** che PGE realizza nel 2026 (Stream YAML = single rule; migliaia di grani = multiple operations via ParameterOrchestrator).
3. **Tendency-mask control** (p. 162, range time-varying + sampling gaussiano + indipendenza fra grani) = conferma documentale CIM 1993 dell'adozione del modello Truax 1988 = stesso pattern [[tendency-mask]] in PGE.
4. **Layering ricorsivo stream + mixing coefficients** (p. 163) = primitiva CIM del workflow STEMS PGE in forma embrionale.
5. **Phase-level switches 50%-probabilistici** (pp. 162–163) = precursore concettuale del `ProbabilityGate` PGE.

Coesistenza nel singolo sistema ICMS di due famiglie di controllo (tendency-mask statistica + mappe caotiche deterministiche delle opzioni 4-7) — PGE eredita esplicitamente la prima, affianca la seconda come alternativa nella tradizione CIM offline. Posizionamento storico: ultimo nodo maturo della tradizione offline italiana CIM. Lo stesso volume CIM X 1993 ospita Lippe ISPW real-time, e Di Scipio/Tisato annunciano *"in the near future in a real-time version on a NeXT computer"* (p. 165) — la transizione tradizione offline → real-time è documentata all'interno di un singolo Atti.

Propagazione:
1. `wiki/sources/proceedings/discipio-tisato1993.md`: nuova pagina con schema proceedings CIM completo.
2. `wiki/overview.md`: tabella precursori riga 1993 Di Scipio/Tisato aggiunta tra 1991 Di Scipio e 1994 Di Scipio (cinque vettori condensati); differenziatore 1 (YAML DSL) aperto con quote-pietra-angolare CIM 1993 *"step towards the abstract"* come ancoraggio CIM-interno del programma DSL (prima di Roads 2001 e Vaggione 1996/2003).
3. `wiki/sources/bibliography.md`: aggiunta riga `DiScipioTisato1993cim | Di Scipio, Tisato 1993 | CIM X | ✓ | 1, 2, 3, 6`.
4. `wiki/sources/proceedings/cim-survey.md`: entry 1993 Di Scipio/Tisato espansa con pagine, pipeline 3-step, tendency-mask, layering ricorsivo, quote pietra-angolare; aggiunta sotto-sezione 1993 Di Scipio/Tisato in "Offline con controllo algoritmico dei parametri" del confronto offline con PGE.
5. `wiki/index.md`: nuova entry sotto Sources — Proceedings tra `discipio1991.md` e `keller-rolfe1998.md`.
6. `refs.bib`: entry BibTeX da aggiungere via Zotero batch (chiave `DiScipioTisato1993cim`).

File modificati: `discipio-tisato1993.md` (nuovo), `overview.md`, `bibliography.md`, `cim-survey.md`, `index.md`, `log.md` (questa entry).

---

## [2026-05-21] review-ingest | fix propagazione Di Scipio/Tisato 1993

Review-ingest sulla nuova pagina `discipio-tisato1993.md`. Schema fisso e contenuto OK; quattro gap di propagazione chiusi.

Gap 1 — `wiki/sources/proceedings/discipio1991.md:31`: affermazione errata «Di Scipio/Tisato 1993 (CIM X), Lippe 1993 — transizione al real-time grazie a workstation dedicate (ISPW)». Confonde i due paper del medesimo volume CIM X. ICMS Di Scipio/Tisato 1993 è ancora deferred su mainframe IBM 9121; il real-time NeXT è annunciato come *"in the near future"* (p. 165) ma non realizzato. Solo Lippe 1993 è effettivamente real-time. Corretto: riformulato in due voci separate, aggiunto wikilink `[[discipio-tisato1993]]`.

Gap 2 — `wiki/concepts/tendency-mask.md`: la nuova pagina dichiara «conferma documentale CIM 1993 del modello Truax 1988» come vettore (c) e referenzia `[[tendency-mask]]`, ma la concept page non era stata aggiornata. Aggiunto in *Lineage storico* il datapoint Di Scipio/Tisato 1993 (ICMS) con quote p. 162 sul tendency-mask control + sampling gaussiano applicato a grain duration/delay/amplitude/file-portion. Aggiunto inoltre paragrafo *Coesistenza nel singolo sistema (ICMS)* nella sezione di contrasto controllato: ICMS mantiene tendency-mask per i parametri di sintesi e affianca al medesimo livello le mappe caotiche per il controllo del puntatore (opzioni 4–7 del menu `GRANULAR PROC.`) — modello di coesistenza, non gerarchia.

Gap 3 — `wiki/overview.md` differenziatore 8: non menzionava ICMS come datapoint CIM 1993 di coesistenza, mentre la nuova pagina rivendica esplicitamente diff. 8 come argomento storico. Esteso il paragrafo finale di diff. 8 con (a) la quote tendency-mask p. 162; (b) la lista delle quattro mappe caotiche (discubic/logistic/Verhulst/May) come modalità parallele del puntatore; (c) la conclusione argomentativa che la scelta PGE di ereditare tendency-mask e affiancare il caos riflette una postura già documentata in CIM 1993, non un'invenzione.

Gap 4 (falso positivo) — `refs.bib`: la review aveva segnalato l'entry mancante. Verificato che nessuna chiave `*cim` (Roads1985cim, DiScipio1991cim, Rizzuti2006, Arcella2012, KellerRolfe1998, ValleLombardo2003, OrtoseccoPiccialli1989, Sparano2018, Cera2022) è presente in `refs.bib`: convenzione del workspace è gestire le proceedings CIM via Zotero batch separato (`bibliography.md` come fonte di tracciamento, `refs.bib` rigenerato da Zotero). Il flag «BibTeX da aggiungere via Zotero batch» nel log entry dell'ingest è coerente con la convenzione, non lacuna del workflow ingest. Non toccato `refs.bib` per non corrompere lo stato Zotero-generato.

File modificati: `discipio1991.md`, `tendency-mask.md`, `overview.md`, `log.md` (questa entry).

---

## [2026-05-22] review-ingest | fix propagazione Lippe 1993

Review-ingest sulla nuova pagina `lippe1993.md`. Schema fisso proceedings CIM completo (Citazione/Categoria/Argomento/Sistema/Analogia PGE/Posizionamento/Note stilistiche/Sezioni CIM 2026/Quote chiave); contenuto denso e ben articolato (4 vettori di analogia controllata + 4 quote verbatim con pp.). Propagazione globalmente corretta su `overview.md`, `bibliography.md`, `cim-survey.md`, `index.md`. Due gap chiusi + un fix step 0 (riclassificazione livello).

Gap 1 — `wiki/concepts/tendency-mask.md`: la nuova pagina rivendica in (c) **"doppia conferma documentale CIM 1993"** del modello Truax 1988 (Lippe + Di Scipio/Tisato stesso volume X CIM) e il differenziatore #8 di `overview.md` è stato esteso con identica formulazione "doppio datapoint CIM 1993", ma la concept page `tendency-mask` non era stata aggiornata. Il log entry dell'ingest giustificava l'omissione con «Lippe è materia di precursori, non di definizione del modello» — motivazione asimmetrica: il datapoint Di Scipio/Tisato 1993 era stato invece incluso in `tendency-mask.md` durante la review precedente (2026-05-21) con identico ruolo di "precursore CIM" e identica meccanica (Truax 1988 ripresa in CIM 1993). Aggiunto secondo bullet nel *Lineage storico* della concept page con quote p. 181 Lippe e nota esplicita sul significato della coppia offline/real-time stesso anno (la diffusione del pattern attraversa entrambi i paradigmi di esecuzione, non è proprietà esclusiva di nessuno dei due).

Gap 2 — `docs/plans/setup-workspace.md`: la nuova pagina costituisce una riclassificazione del paper Lippe 1993 da Livello C ("ignora") a Livello A ("precursore diretto"). Il piano elencava esplicitamente `CIM X 1993 (Lippe)` nella sezione "Livello C — ignora" (riga 146), in linea con la valutazione iniziale del survey ("Articolo dedicato. Controllo real-time della granulazione via processi non-lineari su IRCAM ISPW. Real-time." — 2 righe). La review precedente (2026-05-21) ha stabilito il precedente di documentare in `setup-workspace.md` la riclassificazione di Di Scipio 1995 da C → A (punto 5 dello Step 4 Livello A + nota in Livello C). Applicato lo stesso pattern per Lippe 1993: aggiunto punto 5bis nello Step 4 Livello A con motivazione (precursore tassonomico + doppia conferma tendency mask + recursive aspect); rimosso `(Lippe)` dalla riga Livello C; aggiunta nota di riclassificazione data 2026-05-22.

Non-gap (verificati):
- Schema fisso: tutti i campi del workflow ingest (paper da proceedings CIM) presenti.
- `index.md`: entry inserita in posizione cronologica corretta tra [[discipio-tisato1993]] e [[discipio1995]].
- `bibliography.md`: riga aggiunta con sezioni paper [1, 2, 3, 4]; *Debito Zotero* aggiornato (12 → 13 chiavi).
- `cim-survey.md`: entry Lippe ampliata da 2 righe a 6 righe con pagine + contenuto tassonomico + tendency masks + recursive aspect + link; rinvio in *Non comparabili (real-time)* aggiornato con ruolo (precursore tassonomico + conferma tendency mask).
- `overview.md`: nuova riga tabella precursori 1993 Lippe inserita correttamente fra 1993 Di Scipio/Tisato e 1994 Di Scipio; differenziatore #8 esteso con doppio datapoint CIM 1993; link `[[lippe1993]]` aggiunto nella riga Di Scipio/Tisato 1993.
- `refs.bib`: non toccato (convenzione workspace via Zotero batch — coerente con review precedente).

File modificati: `tendency-mask.md`, `setup-workspace.md`, `log.md` (questa entry).

---

## [2026-05-24] ingest | proceedings Markidis 2024 — Mediation Process / Ecosystemic CIM XXIV

Ingest individuale del paper Markidis (CIM XXIV, pp. 48–56) — quarto e ultimo paper del thread Di Scipio CIM, in fase ermeneutica. Prima della sessione il paper era censito in `cim-survey.md` come "menzione rilevante" (riclassificazione: → "articolo dedicato"). Selezione minima nello scope di ingest concordata con l'utente (1 paper dei 6 candidati dell'inventory survey), motivata dalla rilevanza per il posizionamento PGE su quattro vettori:

1. **Pattern *separare specifica da implementazione*** condiviso col DSL YAML PGE per via tecnologica opposta. Quote pietra-angolare p. 48: *"By making the DSP score available [...] in a high-level language not dependent on any specific implementation, the composer enables performers to create patches in an environment of their choosing. [...] the composer abstracts the piece from its specific implementation network, albeit at the cost of an additional mediation layer."* Il graphical DSP score Di Scipio funge da specifica renderer-independent; PGE textual DSL parsing automatico, Markidis graphical + interprete umano (metodologia *layer of mediation* a 4 strati).
2. **Chiusura del thread Di Scipio CIM**: [[discipio1991]] (offline, vincolo hardware) → [[discipio-tisato1993]] (ICMS, DSL ante litteram) → [[discipio1995]] (snodo offline → real-time KYMA) → **Markidis 2024** (fase ermeneutica, sustainability via graphical score). Il filone si sposta da problema implementativo (1991-95) a problema ermeneutico (2024).
3. **Secondo data-point CIM della terminologia *grain sampling*** dopo [[lippe1993]]: il score Di Scipio (rev. 2016) cita verbatim *"granular sampling"* + *"grain density controls and slight random variations on grain parameters ('jitter')"* (p. 53), ricezione operativa della tassonomia Lippe + del modello tendency-mask Truax 1988 in lingua compositiva italiana.
4. **Quarto data-point CIM tendency-mask** in declinazione *compositiva* (non tecnica): la coppia *grain density* + *jitter* = formulazione non-tecnica della meccanica range time-varying + sampling distribuito + indipendenza fra grani. La sequenza CIM completa è ora ICMS 1993 (tecnica) → ISPW 1993 (tecnica) → IRIS-MARS 1995 (tecnica) → AE3a score 2003/2016 + Markidis CIM 2024 (compositiva) — quattro decenni e tre paradigmi di esecuzione.

Anti-analogie strutturali per delimitare il prestito concettuale:
- Granulator come *componente* di un ecosistema audio-feedback signal-driven vs *motore primario* declarative PGE.
- `tabsend~`/`tabreceive~` per spezzare DSP loop (sez. 5.3, p. 52) = stratagemma real-time signal-flow specifico, non trasferibile a deferred.

Coppia stesso volume CIM XXIV con [[anatrini2024]]: due polarità 2024 dell'unificazione programmazione/composizione (WavePilot riduce dimensionalità via deep learning real-time gestuale; Markidis preserva dimensionalità via graphical DSP score real-time ermeneutico); PGE = terzo polo declarative deferred.

Propagazione:
1. `wiki/sources/proceedings/markidis2024.md`: nuova pagina con schema fisso proceedings CIM completo (4 vettori di analogia + 5 quote verbatim con pp.).
2. `wiki/sources/proceedings/cim-survey.md`: entry 2024 Markidis riclassificata da "menzione rilevante" ad "articolo dedicato" + sintesi denuda (pagine + contenuto + quote pietra-angolare + thread Di Scipio + grain sampling lineage); rinvio aggiornato in *Non comparabili (real-time)* con sintesi 2 righe + link.
3. `wiki/overview.md`: nuova riga tabella *Sistemi contemporanei* per 2024 Markidis inserita tra 2021 Roads/Kilgore/DuPlessis e 2024 Anatrini (mantenendo ordine cronologico + coppia CIM XXIV consecutiva). Riga documenta chiusura thread Di Scipio + pattern *separare specifica da implementazione* + anti-analogie strutturali + cornice CIM 2024 (coppia con WavePilot + PGE terzo polo).
4. `wiki/concepts/tendency-mask.md`: aggiunto quarto datapoint CIM in *Lineage storico* con quote score Di Scipio p. 53 + nota su transizione tecnica → compositiva del modello + sequenza CIM completa (ICMS 1993 → ISPW 1993 → IRIS-MARS 1995 → AE3a 2003/2016 + Markidis CIM 2024).
5. `wiki/sources/bibliography.md`: riga aggiunta Proceedings table (`Markidis2024cim | Markidis 2024 | CIM XXIV | ✓ | 1, 2, 3, 6`); voce aggiunta in *Debito Zotero* (contatore 15 → 16).
6. `wiki/index.md`: nuova entry sotto Sources — Proceedings inserita prima di [[anatrini2024]] per ordine cronologico interno (pp. 48 < 129) e per coppia CIM XXIV consecutiva.
7. `refs.bib`: non toccato (convenzione workspace via Zotero batch — coerente con review precedenti).

File modificati: `markidis2024.md` (nuovo), `cim-survey.md`, `overview.md`, `tendency-mask.md`, `bibliography.md`, `index.md`, `log.md` (questa entry).

---

## 2026-05-26 — Ingest proceedings CIM XVIII 2010: Silvestri *Wavetable Switching per Multiplexing*

Ingest del paper Stefano Silvestri (Cons. S. Pietro a Majella, Napoli), *"Introduzione alla sintesi Wavetable Switching per Multiplexing di segnali"*, in *Atti XVIII CIM* 2010 pp. 209–213.

Estrazione PDF via `pdftotext -layout`, lettura integrale (5 pp). Paper monoautore da tesi I Liv. (relatore A. Di Scipio, A.A. 2008/2009), 9 references prevalentemente italiane (Mathews 1976, De Poli 1981, Horn 1988, Valdoni-Vatalaro 1984, Bristow-Johnson 1996, Horner-Beauchamp-Haken 1993, Di Scipio/Cavaliere dispense 2009).

Procedimento tempo-discreto: oscillatori wavetable look-up paralleli con accumulatori di fase $\phi_n = (n+1) \bmod N$, finestrature quadre o gaussiane di periodo $T_{env}$ sfasate, emulatore multiplexer N-bit (rete combinatoria AND/NOT/OR) che commuta i sub-vettori in uscita. Per $f_{cm} > 20\div25\,\mathrm{Hz}$ il sistema produce arricchimento spettrale (bande laterali AM) al confine della fusione percettiva. Composizione di riferimento *Studio Sonoro III* (nota 10 p. 210).

Vettori di analogia identificati:

1. **Terzo data-point CIM *granulare deterministico*** dopo [[discipio1991]] (mappe caotiche iterative) e [[rizzuti2006]] (logistica) — **sotto-famiglia distinta**: combinatoria deterministica sulla sequenza di indirizzi MUX, non $x_{n+1}=f(x_n)$. Asse di controllo trasversale rispetto a Roads/Truax: il grano non è entità di prima classe ma prodotto incidentale del meccanismo combinatorio (cfr. inquadramento autoriale esplicito p. 209 + chiusura p. 212).

2. **Data-point CIM 2010 coesistenza RT + offline nella stessa opera**: *Studio Sonoro III* «interamente basata su algoritmi di wavetable multiplexing implementati sia per la sintesi in tempo reale che, per la parte per nastro, in tempo differito» (nota 10, p. 210). Il differito non è ripiego ma scelta «per la parte per nastro», cioè per il segmento che richiede controllo fine sui transienti spettrali microstrutturali — conferma documentale CIM della legittimità compositiva del differito *quando il materiale lo richiede*, coerente con la postura PGE su asse tecnico opposto (combinatoria spettrale vs cache + IR).

3. **Lineage napoletano CIM**: terzo nodo DSP-orientato dopo [[depoli-piccialli1988]] e [[ortosecco-piccialli1989]] — tutti e tre ad orientamento elaborazione del segnale, in contrasto col filone padovano/veneto orientato al controllo.

4. **Thread Di Scipio allievi CIM**: Silvestri come tesista 2008/2009 → co-autore con Arcella nel volume successivo [[arcella-silvestri2012]]. Continuità di magistero su due volumi CIM consecutivi.

5. **Modello stilistico CIM 2010**: 5 pp, 9 ref, mono-autore da tesi — soglia minima paper CIM accettato. Pattern *short ref list + citazione interna estesa* (Xenakis-Gabor in chiusura p. 212 senza essere in bibliografia). Utile come benchmark inferiore di densità per il paper PGE 2026.

Citabilità: sez. 2 (filone granulare deterministico CIM, asse di controllo trasversale), sez. 6 (data-point CIM coesistenza RT+offline che disinnesca la lettura del differito PGE come regressione).

Propagazione:
1. `wiki/sources/proceedings/silvestri2010.md`: nuova pagina con schema fisso proceedings CIM completo (5 quote verbatim con pp., 3 quote chiave finali).
2. `wiki/sources/proceedings/cim-survey.md`: entry 2010 Silvestri riclassificata da "menzione teorica" ad "articolo dedicato" con sintesi denuda (terzo nodo granulare deterministico + Studio Sonoro III RT+offline + lineage napoletano + thread allievi Di Scipio).
3. `wiki/overview.md`: nuova riga 2010 inserita nella tabella precursori tra Rizzuti 2006 e Arcella/Silvestri 2012 (ordine cronologico + continuità anti-analogia controllo deterministico + ponte al thread Silvestri co-autore).
4. `wiki/sources/bibliography.md`: riga aggiunta Proceedings table (`Silvestri2010 | Silvestri 2010 | CIM XVIII | ✓ | 2, 6`); voce aggiunta in elenco *Debito Zotero* preservando ordine cronologico (dopo Rizzuti2006, prima di Arcella2012).
5. `wiki/index.md`: nuova entry sotto Sources — Proceedings inserita dopo [[rizzuti2006]] e prima di [[arcella-silvestri2012]] per ordine cronologico crescente, coerente col resto del blocco proceedings.
6. `refs.bib`: non toccato (convenzione workspace via Zotero batch).

File modificati: `silvestri2010.md` (nuovo), `cim-survey.md`, `overview.md`, `bibliography.md`, `index.md`, `log.md` (questa entry).

---

## 2026-05-26 — Promozione concept page: granulare deterministico CIM

Review-ingest del paper Silvestri 2010 ha identificato che il filone *granulare deterministico CIM* è arrivato a 3 nodi (Di Scipio 1991, Rizzuti 2006, Silvestri 2010) e si è articolato in 2 sotto-famiglie distinte (caotico-iterativo `xn+1=f(xn)` vs combinatoria deterministica MUX). Soglia per concept page autonoma. Promosso.

Contenuto concept page `wiki/concepts/granulare-deterministico-cim.md`:
- Definizione del filone come alternativa di principio al canone Roads/Truax stocastico.
- Articolazione in due sotto-famiglie con descrizione del meccanismo formale di ciascuna e mapping ai data-point CIM.
- Tabella comparativa 4×4 (sotto-famiglia A / sotto-famiglia B / PGE) sugli assi: generatore valore, memoria fra grani, ruolo del grano, asse di controllo.
- Discussione architetture a due moduli come precursore debole della separazione Stream/grano PGE; rinvio a [[arcella-silvestri2012]] come precursore CIM diretto della topologia DSL→IR→renderer.
- Cluster sociologici: magistero Di Scipio attraversa tutti e tre i nodi; intersezione con lineage napoletano CIM via Silvestri; thread Di Scipio allievi su volumi consecutivi (XVIII 2010 → XIX 2012).
- Citabilità sez. 2 (citazione collettiva del filone per contrasto controllato, distinguendo le due sotto-famiglie) e sez. 6 (Silvestri *Studio Sonoro III* per coesistenza RT+offline).
- Domande aperte: data-point XX–XXIV non investigati; Markidis 2024 da inquadrare; continuità di pratica Silvestri post-2010.

Propagazione:
1. `wiki/concepts/granulare-deterministico-cim.md`: nuova pagina.
2. `wiki/sources/proceedings/silvestri2010.md`: backlink in *Posizionamento storico* + specificazione single-data-point sotto-famiglia (B).
3. `wiki/sources/proceedings/rizzuti2006.md`: backlink in *Analogia con PGE* in chiusura di paragrafo (inquadramento d'insieme A+B).
4. `wiki/sources/proceedings/discipio1991.md`: backlink in *Analogia con PGE* prima frase (prima formulazione CIM sotto-famiglia A, ponte verso Rizzuti/Silvestri).
5. `wiki/index.md`: entry nuova in sezione Concepts dopo `decorrelazione-granulare`.
6. `wiki/log.md`: questa entry.

Non toccati: `overview.md` (la tabella precursori contiene già righe Di Scipio 1991, Rizzuti 2006, Silvestri 2010 con descrizione anti-analogia esplicita — il concept page funge da pagina di sintesi del filone, non sostituisce le righe; rinvii overview→concept opzionali, non aggiunti per evitare ridondanza), `bibliography.md`, `cim-survey.md`, `tendency-mask.md` (già contiene cross-link bidirezionale verso il filone via `[[discipio1991]]` e `[[rizzuti2006]]`; aggiunta link al concept page rinviata se diventerà rilevante in futuro ingest).

File modificati: `granulare-deterministico-cim.md` (nuovo), `silvestri2010.md`, `rizzuti2006.md`, `discipio1991.md`, `index.md`, `log.md` (questa entry). Inoltre: correzione retroattiva descrizione index nella entry precedente (era "prima di rizzuti2006 ordine inverso", corretto in "dopo rizzuti2006 prima di arcella-silvestri2012 ordine crescente"): allineamento descrizione log alla modifica reale del diff.

---

## 2026-05-26 — Survey CIM XX 2014 + ingest proceedings CIM XXI 2016: Markidis/Fernández *path~*

Sessione doppia: completamento del survey trasversale `cim-survey.md` con la sezione 2014 — XX CIM finora mancante (volume non scansionato con `grep granul`) + ingest dedicato del paper Markidis/Fernández 2016 sulla concatenative synthesis `path~` per Pure Data, finora presente in survey solo come menzione.

### Sub-entry 1 — Survey CIM XX 2014

Estrazione testo via `pdftotext -layout` su `raw/proceedings/2014_CIM_XX_Atti.pdf`, ricerca su radice `granul`. Tre paper rilevanti identificati:

1. **Agostini, Daubresse, Ghisi** *"CAGE: una libreria di alto livello per la composizione assistita da computer in tempo reale"* (pp. 17–22) — Libreria **cage** per Max, basata su bach (struttura `llll`). Modulo **`cage.granulate`** = *motore di granulazione **simbolica*** che opera su `bach.roll` (rappresentazione partitura), non su buffer audio. Prima occorrenza CIM della *granulazione simbolica* come categoria distinta dal granulare audio — anti-analogia di principio rispetto a tutta la tradizione granular audio CIM, incluso PGE. **Real-time simbolico**, non audio.
2. **Valenti, Valle, Servetti** *"Permutation synthesis"* (pp. 35 ss.) — Tecnica sperimentale che riarrangia chunk di campioni dello stesso segnale senza envelope. Posiziona granular synthesis come tecnica di riferimento di confronto: granulare applica envelope per eliminare discontinuità, permutation enfatizza discontinuità come feature. Andrea Valle = secondo paper CIM granular-related dopo [[valle-lombardo2003]], continuità autoriale CIM su 11 anni.
3. Menzioni marginali (granulation+waveshaping per distorsione, granular synthesis su DAC R2R 8-bit) annotate ma non rilevanti per il paper PGE.

Vettori di analogia con PGE da queste osservazioni di survey:
- **`cage.granulate` come anti-analogia ortogonale**: amplia il dominio della granulazione fuori dal segnale audio (simbolico vs. audio). Asse di delimitazione ulteriore per il paper PGE — non solo *deferred vs real-time* (Sparano/EC2/path~), non solo *grani indipendenti vs concatenative* (path~), ma anche *audio vs simbolico* (cage.granulate). Utile in sez. 2 come terza dimensione di delimitazione del dominio PGE.
- **Andrea Valle CIM thread**: GeoGraphy 2003 (offline, formal) → Permutation synthesis 2014 (sperimentale, RT) — coerenza autoriale CIM su un asse di ricerca *granular-adjacent* per 11 anni. Riservare nota nel paper PGE solo se [[valle-lombardo2003]] viene citato direttamente, non standalone.

Propagazione survey:
1. `cim-survey.md`: nuova sezione `### 2014 — XX CIM` inserita fra 2012 e 2016, due paper dedicati (cage / permutation synthesis) + menzioni marginali aggregate.
2. `cim-survey.md` entry 2016 riformulata (era 2 righe, ora paragrafo completo) per inquadrare Markidis/Fernández in vista dell'ingest dedicato sotto-entry 2.
3. `cim-survey.md` sezione *Non comparabili (real-time)*: rinvio 2016 Markidis/Fernández esteso con sintesi 2 righe + link a [[markidisfernandez2016]].

Non creata pagina wiki dedicata per cage 2014 né per permutation 2014: i due paper sono coperti dalla sezione survey, non hanno ancora soglia per pagina autonoma (sono singoli data-point su rispettive dimensioni di anti-analogia, non nodi di un filone con ≥3 nodi).

### Sub-entry 2 — Ingest proceedings CIM XXI 2016: Markidis/Fernández *path~*

Lettura integrale PDF (pp. 181–185, 5 pp, 8 references). Affiliazioni: Markidis = nonoLab Parma, Fernández = IRCAM Parigi.

Architettura `path~`: external GPLv3 per Pure Data Vanilla, corpus-based concatenative synthesis con kd-tree e k-nearest neighbors nel spazio dei descrittori (default 16-dim: MFCC ad alto livello 14-dim + spectral centroid + RMS amplitude). Pipeline ibrida — analisi/segmentazione/estrazione descrittori/costruzione kd-tree/ordinamento/calcolo knn list **in tempo differito** su thread worker; estrazione descrittori input + ricerca primo vicino nel kd-tree + sintesi grano + treno di k-vicini per concatenazione **in tempo reale** su thread principale Pd. Latency <2 ms su database 30K grani; analisi differita <1 min su 10 min audio. 2 modalità di segmentazione (window-based costante / threshold-based variabile event-driven); DSL preset script con sintassi a token (window, hopsize, concatenate, amp, envelope, weight, threshold). Outputs audio vettorializzati (numero canali virtuali = max grani simultanei). Esclusione opzionale della parte di sintesi per modalità control-only (CPU saving). Composizioni di riferimento: *Cattedrali di Sabbia*, *Dispersion de trajectoires* (estratto partitura in Fig. 1).

Vettori di analogia identificati (4):

1. **Tassonomia esplicita CIM 2016 granular → concatenative**: paper inquadra la sintesi concatenativa come ramo evolutivo della sintesi granulare in cui *«i grani sono legati fra loro solitamente da un'analisi precedentemente fatta su un file audio»* (p. 181). PGE non implementa concatenative — grani indipendenti per stream, canone Roads/Truax. `path~` documenta CIM 2016 la divergenza del ramo concatenative, PGE 2026 ne è esplicitamente fuori. **Posizionamento sez. 2 del paper PGE come ritorno al canone *grani indipendenti per stream***, non come adesione a concatenative.

2. **Precursore CIM dell'ibridazione RT/differito necessaria nel granulare-derivato**: paper afferma esplicitamente *«Oltre all'analisi, altre operazioni sono eseguite in tempo differito, come l'ordinamento del database o il calcolo dei primi vicini, necessario per la parte di sintesi dell'algoritmo»* (p. 181). Riconoscimento CIM 2016 che parte sostanziale del workflow granulare-derivato è *necessariamente* offline anche in sistemi che si presentano come real-time. **Anti-analogia con PGE**: PGE estende il differito a *tutto* il pipeline come scelta compositiva (non come vincolo computazionale dell'analisi); `path~` minimizza la quota differita per servire la performance, PGE massimizza la quota differita per servire il loop lungo specifica → ascolto → riscrittura. Inversione di polarità.

3. **Markidis CIM thread (8 anni)**: primo paper CIM di Marco Matteo Markidis, autore poi di [[markidis2024]] (CIM XXIV, *Mediation Process in a Computer Music Interpretation*). Evoluzione autoriale documentabile: 2016 = tool builder (external Pd per concatenative analysis/synthesis); 2024 = metodologo della traduzione fra ambienti (libreria aeLib + framework *layer of mediation* a 4 strati). Continuità di principio: in entrambi i paper la *separazione fra rappresentazione e implementazione* è centrale. Spostamento di scala: da componente a framework.

4. **Multithreading offline-during-RT come pattern complementare al deferred-total PGE**: `path~` usa un thread worker dedicato per non bloccare il thread audio Pd durante l'analisi del corpus. PGE può permettersi un approccio single-thread senza vincoli di latenza audio: il rendering può occupare l'intera CPU per minuti senza che questo conti come *latenza* — riformulazione del trade-off RT/offline come scelta di cosa misurare (tempo wall-clock di rendering vs latenza fra trigger e suono).

Citabilità: sez. 2 (delimitazione PGE come *non-concatenative*, posizionamento nel cluster contemporaneo del granulare CIM). Non sez. 1, 4, 5, 6.

Propagazione ingest:
1. `markidisfernandez2016.md` (nuovo): schema fisso proceedings CIM completo, 4 vettori di analogia, 4 quote verbatim con pp.
2. `cim-survey.md`: entry 2016 riformulata + rinvio in *Non comparabili (real-time)* (già coperto in sub-entry 1).
3. `overview.md`: nuova riga 2016 in tabella *Sistemi contemporanei (poli compositivi opposti)* inserita fra 2006 Roads Ynez e 2018 Sparano per ordine cronologico crescente. Riga documenta ramo concatenative + anti-analogia ontologica grani indipendenti vs grani legati + precursore CIM ibridazione RT/differito + thread Markidis CIM.
4. `markidis2024.md`: nuovo paragrafo *Markidis CIM thread (8 anni)* in *Posizionamento storico* dopo paragrafo *Posizionamento nel volume CIM XXIV*. Retro-link bidirezionale a [[markidisfernandez2016]] con sintesi shift tool builder → metodologo.
5. `bibliography.md`: riga aggiunta a Proceedings table (`MarkidisFernandez2016cim | Markidis, Fernández 2016 | CIM XXI | ✓ | 2`) inserita dopo Arcella2012 per ordine cronologico; voce aggiunta in *Debito Zotero* nella stessa posizione cronologica; contatore aggiornato 16 → 18 (correzione retroattiva: il contatore era già fuori sincronia di una unità prima di questa sessione perché l'aggiunta di Markidis2024cim non aveva incrementato).
6. `index.md`: nuova entry sotto Sources — Proceedings inserita dopo `arcella-silvestri2012` per ordine cronologico (Arcella 2012 → Markidis/Fernández 2016 → Valle/Lombardo 2003 — l'ordine interno del blocco proceedings non è strettamente cronologico, ma la posizione subito dopo Arcella mantiene il sub-ordine cronologico fra i paper italiani di area DSL/architettura compositiva).
7. `refs.bib`: non toccato (convenzione workspace via Zotero batch — coerente con review precedenti).
8. Non creata concept page su *concatenative CIM*: singolo nodo CIM ingestito (Markidis/Fernández 2016), sotto soglia 3 nodi per promozione. Annotata come *domanda aperta*: se Pozzi 2016 verrà ingestito → 2 nodi, ancora sotto soglia; se CataRT 2006 verrà ingestito (non CIM, citato come riferimento) → categoria diversa (sistema esterno, non paper CIM). Promozione rinviata.

File modificati: `markidisfernandez2016.md` (nuovo), `cim-survey.md`, `overview.md`, `markidis2024.md`, `bibliography.md`, `index.md`, `log.md` (questa entry).


---

## [2026-05-27] ingest | Pozzi 2016 *Composing Exploration* (CIM XXI) — anti-analogia multi-agent + analogia diretta loop iterativo *Breakpoint*

Ingestione paper Daniele Pozzi (IEM Graz) *Composing Exploration: A Multi-Agent Approach to Corpus-Based Concatenative Synthesis* (Atti XXI CIM, Cagliari 2016, pp. 190–196, 18 refs). Sistema SuperCollider con SCMIR + KDTree + RedUniverse: Boids di Reynolds esplorano uno spazio 2D di descrittori (CataRT-like) e ciascun boid pilota un'istanza di granular SynthDef — posizione → grain selection via kNN, n neighbors → amplitude, distanza dal center-of-mass → grain length, velocity → playback rate. Spatial swarm granulation 24-canali al CUBE IEM. Brani: *Breakpoint* (fixed media iterativo), *In Vitro* (installazione), *Cocktail Break* (live + Rear Diffused Illumination + piezo).

Quattro vettori di analogia documentati nella pagina:

1. **Analogia diretta unica (loop lungo)**. Sez. 5 *Musical Contexts — Breakpoint*, p. 194 quote pietra-angolare: *«The audio outcome is recorded, edited and musically inserted in the previous collage of samples. The so obtained track is again analyzed and explored, and so on, in a cyclic procedure.»* Formulazione CIM 2016 esplicita del loop lungo PGE (specifica → generazione → ascolto → riflessione → riscrittura) realizzata su tecnologia opposta: real-time emergent multi-agent invece di deferred declarative DSL. Stesso pattern strutturale, meccanismi tecnici ortogonali. Quote utile per sez. 1 e sez. 5 del paper PGE come precedente CIM esplicito della metodologia ciclica documentata in un brano specifico.

2. **Anti-analogie strutturali su 4 assi** (controllo, predicibilità, esplorazione parametrica, spazializzazione). Tabella 5 righe nella pagina. Punto centrale: *renounce to control* esplicito (sez. 4, p. 193) come polo opposto della postura PGE (control granulare declarativo come parte della scrittura).

3. **Cluster CIM 2016 (coppia stesso volume)** con [[markidisfernandez2016]]. Doppietto CIM XXI 2016 *corpus-based concatenative* polarizzato sull'asse target-driven vs exploration-driven: Markidis input determina nearest neighbor (target-driven), Pozzi agenti autonomi cercano regioni (exploration-driven). Coppia simmetrica precedentemente sospesa (Pozzi non era ingestito) ora documentata.

4. **Anti-analogia simmetrica con [[anatrini2024]]** sull'asse esplorazione parametrica via tecnologie incomparabili: Pozzi 2016 (Boids real-time SC) ↔ Anatrini 2024 (VAE deep learning real-time Python+JS) ↔ PGE (declarative deferred). Tutti e tre convergono sull'obiettivo enunciato da Anatrini p. 130 («*superare la tradizionale separazione tra programmazione parametri e attività compositiva*») via tre tecnologie radicalmente diverse.

Sotto-osservazione: quarto data-point CIM 2016 di adozione del vocabolario Di Scipio dopo [[lippe1993]], [[detintis1995]], [[arcella-silvestri2012]]. Pozzi cita Di Scipio 1994 ICMC [#8] per giustificare *formation of both timbre and form in a natural dynamic process* (sez. 6). Pozzi formato a IEM Graz ma allineato esplicitamente col lessico Di Scipio del *micro-composition paradigm*.

Citabilità: sez. 1 (precedente CIM esplicito del loop lungo via tecnologia opposta), sez. 2 (anti-analogia multi-agent al canone tendency mask + coppia CBCS CIM 2016), sez. 5 (modello stilistico CIM 2016 di documentazione del loop iterativo in un brano specifico — raro nel canone CIM), sez. 6 (polo opposto *renounce to control*).

Propagazione ingest:
1. `pozzi2016.md` (nuovo): schema fisso proceedings CIM completo, 4 vettori di analogia, 4 quote verbatim con pp., tabella anti-analogie 5 righe, 3 domande aperte.
2. `cim-survey.md`: entry 2016 Pozzi riformulata da 1 frase a paragrafo completo con backlink [[pozzi2016]]; rinvio in *Non comparabili (real-time)* paragrafo finale aggiornato con backlink + sintesi.
3. `bibliography.md`: riga aggiunta a Proceedings table (`Pozzi2016 | Pozzi 2016 | CIM XXI | ✓ | 1, 2, 5, 6`) inserita dopo MarkidisFernandez2016cim per ordine cronologico (stesso volume); contatore Debito Zotero aggiornato 20 → 21; heading aggiornato con `(+1 entry 2026-05-27)`; voce aggiunta in lista chiavi `refs.bib`.
4. `refs.bib`: entry `@inproceedings{Pozzi2016, ...}` (rigo 502-512) inserita dopo `MarkidisFernandez2016cim`, modello `MarkidisFernandez2016cim` con `langid = english` (paper in inglese).
5. `index.md`: nuova entry sotto Sources — Proceedings inserita dopo `markidisfernandez2016` con sintesi estesa (12 righe: tecnica + analogia diretta + anti-analogia + cluster CIM 2016 + anti-analogia Anatrini + lineage Di Scipio + sezioni paper).
6. `overview.md`: **non toccato** in questa sessione (Pozzi sez. 5 *Breakpoint* iterativo come precedente CIM esplicito del loop lungo merita potenzialmente entry nei differenziatori PGE, ma richiede integrazione cross-source con Vaggione *progressive enrichment* + Roads *economy of selection* + Di Scipio osservazione→modifica → rinviato a sessione dedicata "concept page `loop-lungo-cim.md`").
7. Non creata concept page `loop-lungo-cim.md`: richiede sintesi multi-fonte (4 nodi: Pozzi *Breakpoint*, Vaggione progressive enrichment via Roads 2005 p. 302, Roads *economy of selection* via Roads 2012 pp. 28-29, Di Scipio osservazione→modifica via Di Scipio 1994). Promozione rinviata.
8. Non aggiornata `concepts/granulare-deterministico-cim.md`: Pozzi è stocastico emergent, non rifiuta tendency mask — fuori dal filone deterministico CIM.

File modificati: `pozzi2016.md` (nuovo), `cim-survey.md`, `bibliography.md`, `refs.bib`, `index.md`, `log.md` (questa entry).

## [2026-05-28] ristrutturazione | Ingest verbale incontro maestro + correzione Truax + studio stilistico bottom-up

Sessione di ristrutturazione del paper CIM 2026 dopo incontro col maestro (2026-05-28). Fonte: trascrizione Whisper `inbox/audio.txt` (826 righe) + esportazioni `audio.{json,srt,tsv,vtt}` con timestamp per segmento. Nessuna diarizzazione automatica nei file Whisper: attribuzione speaker (maestro / Giulio) ricostruita da contenuto + struttura dei turni.

Cinque direttive del maestro + decisioni:

1. **Correzione Truax (economia di mezzi)** — il non-determinismo statistico in Truax NON è cambio di paradigma compositivo ma economia di mezzi per gestire centinaia di grani/sec (event-list deterministica impraticabile). Convive con regioni armoniche progettate (*Riverrun*, ~100/200/300 Hz). Corroborata verbatim leggendo il PDF Truax 1988 (p. 14 «score files... impractical to handle»; p. 19 «enormous amount of data... powerful control strategies are required»; pp. 24–25 macro «clearly defined and controllable» + micro «can only be statistically determined»; p. 23 tendency mask «continuum between deterministic and stochastic choices»).
2. **Struttura bottom-up** — Python → architettura → tradizione → implicazioni alla fine («stai assommando, non focalizzando»).
3. **GUI editor browser → secondo paper futuro** (fuori scope).
4. **Niente brano forzato** — Sez. 5 caso compositivo eliminata.
5. **Scrittura artigianale non sperimentale** + studio narrativo dei paper antichi citati.

Propagazione:
1. `concepts/incontro-maestro-2026-05-28.md` (nuovo): verbale con quote verbatim attribuite + numeri di riga, distinzione quote vs interpretazione, mapping richieste → impatto paper, decisioni. Nota discrepanza deadline (G dice «20 giugno» in dialogo; canonica 7 giugno).
2. `overview.md`: corretto §Tesi corrente (riga Truax) — rimossa formulazione «paradigma compositivo basato sull'immediatezza»; sostituita con economia di mezzi + regioni armoniche *Riverrun* + «intimo del segnale».
3. `concepts/deferred-time-tradition.md`: aggiunta nota di correzione all'Atto 2 (bullet Truax 1988) per coerenza wiki — «abandon linear modes» = modo operativo; non-determinismo statistico = economia di mezzi.
4. `sources/papers/truax1988.md`: corretto §Collegamento tesi (rimosso «cambio di paradigma compositivo»); aggiunte 3 quote verbatim (economia di mezzi / continuum / macro-micro); aggiunta sezione **Architettura espositiva**.
5. `sources/papers/roads1978.md` + `roads1988.md`: aggiunta sezione **Architettura espositiva** (lettura diretta PDF).
6. `concepts/modelli-stilistici-bottom-up.md` (nuovo): matrice paper × dimensione espositiva (Roads 1978/1988, Truax 1988, Arcella-Silvestri 2012, Anatrini 2024) → derivazione spina dorsale 6 sezioni bottom-up.
7. `CLAUDE.md`: aggiunto campo opzionale «Architettura espositiva» allo schema `Workflow ingest (paper PDF)`.
8. `index.md`: 2 nuove entry concepts (incontro-maestro + modelli-stilistici-bottom-up).
9. GitHub issue **#1** (`paper-strategy`): variante top-down archiviata per riferimento futuro.

Decisioni: solo branch bottom-up sviluppato; `paper.tex` da riscrivere da zero in branch `paper-bottom-up`; doc PGE canonica `raw/PythonGranularEngine/docs/` come fonte oltre a `wiki/sources/pge/`.

Da fare (sessione successiva): riscrittura `paper.tex` bottom-up (branch dedicato), aggiornamento `docs/plans/next-session.md`, memory file (feedback Truax + project ristrutturazione).

File modificati: `concepts/incontro-maestro-2026-05-28.md` (nuovo), `concepts/modelli-stilistici-bottom-up.md` (nuovo), `overview.md`, `concepts/deferred-time-tradition.md`, `sources/papers/truax1988.md`, `sources/papers/roads1978.md`, `sources/papers/roads1988.md`, `CLAUDE.md`, `index.md`, `log.md` (questa entry). GitHub issue #1 creato.

---

## [2026-06-06] restructure | allineamento wiki/paper a PGE v4.0.0 "Unit-Driven Pitch"

Bump submodule `raw/PythonGranularEngine` da `0908c47` (v3.9.0-38) a `58b8e2c`
(tag v4.0.0). Release breaking: sistema pitch **unit-driven** (PR #84). Riallineate
le pagine PGE stale e il paper alla nuova realtà del codice.

Cosa cambia in v4.0.0 (verificato leggendo `src/parameters/pitch_unit.py`,
`src/strategies/strategie.py`, `src/strategies/voice_pitch_strategy.py`,
`src/controllers/voice_manager.py`, `src/core/stream.py`, `src/rendering/score_visualizer.py`):
- `PitchUnit`/`EdoUnit`/`RatioUnit` + factory `make_pitch_unit`; strategy unica
  `UnitPitchStrategy` (rimosse `SemitonesStrategy`/`RatioStrategy`). 6 unità:
  semitones(12)/quarter_tone(24)/eighth_tone(48)/cents(1200)/edo:N/ratio. Famiglia
  EDO `2^(v/N)`, ratio moltiplicatore diretto.
- Validazione strict del blocco `pitch`: una sola chiave-unità, chiave sconosciuta
  o blocco vuoto/non-mapping → `InvalidFieldValueError` (No Silent Failures).
- Voci: `semitone_range` → `pitch_range` (hard break); strategy emettono fattore
  di ratio (`get_pitch_factor`, prima `get_pitch_offset`); `VoiceConfig.pitch_offset`
  → `pitch_factor`; geometria nella `PitchUnit.materialize` (EDO additiva vs ratio
  geometrica). `chord`/`spectral` semitone-locked.
- Issue #79: `Stream._create_grain` re-wrappa l'offset pointer di voce in
  `[0, sample_dur)`; la partitura non clippa più le voci sopra il bordo buffer.
- Issue #76: rimosso il claim falso "seed riproducibile fra sessioni" da docstring/README.
- Rimosse property legacy `Stream.pitch_ratio/pitch_semitones`,
  `PitchController.base_ratio/base_semitones` e chiavi `pitch_*` morte nel visualizer.

Verifiche: `make examples` rende ex1–ex4 senza errori di validazione strict
(esempi salvi: ex1 senza blocco pitch, ex3/ex4 usano `pitch:chord` semitone-locked +
`linear`, nessun `semitone_range`). Figure score rigenerate: ex3 identica al pixel
(deterministica, #79 non la tocca — voci dentro buffer), ex4 differisce solo per
stocasticità (scatter). Colore glifo confermato ancora su `grain.pitch_ratio`
(`_pitch_to_color`) → claim del paper invariato.

Propagazione:
1. `sources/pge/parameter-orchestrator.md`: riscritta sezione Strategie pitch
   (UnitPitchStrategy + PitchUnit/EdoUnit/RatioUnit + validazione strict).
2. `sources/pge/voice-manager.md`: `pitch_factor`, invariante voce-0, tabella
   strategy pitch unit-driven, vincolo chord/spectral, hard break `semitone_range`.
3. `sources/pge/stream.md`: `_create_grain` pitch (× pitch_factor) + re-wrap pointer
   issue #79 + nota property rimosse (pitch_value/pitch_unit).
4. `sources/pge/score-visualizer.md`: envelope panel pitch unit-driven (chiave unica
   `'pitch'`, bounds/symbol da unità, entry per-unità rimosse).
5. `paper/paper.tex`: sez. 3 PitchController unit-driven (semitoni/cents/EDO/ratio).
6. `index.md`: aggiornate entry parameter-orchestrator + voice-manager.

File modificati: pin submodule, `paper/paper.tex`, `wiki/sources/pge/{parameter-orchestrator,voice-manager,stream,score-visualizer}.md`, `index.md`, `log.md` (questa entry). Memory `project_pge_rendering_non_riproducibile` aggiornata (issue #76).

## [2026-06-11] query→ingest | Time-stretching granulare: artefatto comb di speed_ratio<1 + verifica empirica + risposta Truax

Domanda di partenza: "perché con speed_ratio .5 il granulatore non ricostruisce
bene l'onda?" Indagine completa: lettura `PointerController`/`DensityController`,
rilettura diretta Truax 1994 pp. 39–42, due test empirici su PGE @ 9c4cb4a.

Risultati:
- Algoritmo PGE **corretto al bit**: stream minimo speed .5, 79 grani,
  `max |pos − 0.5·onset| = 0.0`; offset lettura inter-grano 12.5000 ms =
  teoria `(1−s)·IOT`. fill_factor innocente (COLA piatto a ogni speed).
- Artefatto = **comb filter intrinseco**: somma di grani sovrapposti che
  leggono posizioni distanti `(1−s)·IOT` → notch ogni 80 Hz a speed 0.5
  (default 50 ms / IOT 25 ms). Riprodotto in OLA numpy puro senza PGE:
  400 Hz intatto, 440 Hz −3 dB con sideband. Freeze ex2 = caso limite s=0.
- Truax 1994: variable-rate granulation (TEF eq. 1 p. 42) = prima
  formalizzazione journal del time-stretch granulare (prima assoluta ICMC
  1990, non in repo); pitch invariato esplicito p. 41; anti-comb per
  **decorrelazione** (offset range p. 40 + async + 18 voci p. 42), mai
  ricostruzione fedele (*"not just a processed signal"* p. 42).

Propagazione:
1. Nuova concept page `concepts/time-stretching-granulare.md` (meccanismo,
   tabella notch per speed, verifica empirica, mitigazioni, mapping sez. 2/3).
2. `index.md`: entry concept aggiunta.

File modificati: `wiki/concepts/time-stretching-granulare.md` (nuovo),
`wiki/index.md`, `wiki/log.md` (questa entry).

## [2026-06-11] add-paper + ingest | Dutilleux/De Poli/von dem Knesebeck/Zölzer 2016 — Elaborazione di segmenti temporali

Workflow add-paper: `inbox/PDF.pdf` identificato come trad. it. (R. Neri, rev.
De Poli) di "Time-segment processing", DAFX cap. 6 (Zölzer 2011), pubblicata in
*Musica/Tecnologia* 10 (2016), pp. 75–115, DOI 10.13128/Music_Tec-18437
(verificato via Crossref). Rinominato
`raw/papers/Dutilleux_2016_Elaborazione-Segmenti-Temporali.pdf`; entry
`Dutilleux2016` (@article) appesa a `paper/refs.bib`.

Ingest integrale (41 pp.): varispeed (sez. 2, pitch+durata accoppiati, storia
Phonogène/Furukawa), time stretching (sez. 3: Phonogène universel/Springer,
SOLA con cross-correlation, PSOLA con pitch marks), pitch shifting (sez. 4:
Harmonizer, stretch+resampling, delay line modulata, PSOLA formant-preserving),
ricombinazione temporale/brassage + granulazione (sez. 5), conclusioni (sez. 6).

Punti acquisiti:
- Tassonomia canonica it.: granulazione = sintesi granulare su segnale di
  ingresso, Truax primo sviluppatore (p. 108) — fonte terminologica per il
  titolo/posizionamento del paper (granulazione, non sintesi granulare).
- Quote pietra-angolare p. 112: «l'ampia scelta di strategie per
  l'organizzazione dei grani implica un atteggiamento alla composizione sonora
  da parte dell'utente. Così la granulazione è diventata una sorta di metafora
  per la composizione musicale partendo dal micro livello» — un trattato DSP
  individua nella granulazione il punto di cessione del controllo alla postura
  compositiva; il DSL PGE occupa il livello lasciato aperto.
- Sincrono-deterministico vs asincrono-stocastico (pp. 110–111) + coppia
  ritardo-intra-flusso / sincronicità-inter-flussi (p. 111) = fattorizzazione
  DensityController/VoiceManager; parametri principali granulazione (p. 111)
  mappano uno-a-uno sui controller PGE.
- «Treno di impulsi filtrati» (p. 110) = radice DSP del comb verificato
  empiricamente in concepts/time-stretching-granulare.md.
- Lineage brassage GRM (Parmegiani 1980 → Geslin) = ramo francese del
  micromontage, anteriore alla tassonomia Roads 2001.
- PSOLA come granulazione pitch-synchronous = ponte fra i due sensi di
  "sincrono" (De Poli/Piccialli vs Truax) in sintesi-granulare-sincrona.md.

Propagazione:
1. Nuova pagina `sources/papers/dutilleux2016.md` (schema fisso completo).
2. `concepts/time-stretching-granulare.md`: ancoraggio SOLA/PSOLA + storage
   p. 80 + conferma DSP del comb (p. 110).
3. `concepts/sintesi-granulare-sincrona.md`: ponte PSOLA/granulazione + fonte.
4. `concepts/micromontage.md`: due righe lineage GRM/brassage in tabella + fonte.
5. `overview.md`: paragrafo Radici teoriche (tre ancoraggi DSP) + Gap aggiornato.
6. `bibliography.md`: riga Dutilleux2016, Wiki ✓, sezioni 2/3/6.
7. `index.md`: entry Sources — Papers.

File modificati: `paper/refs.bib`, `wiki/sources/papers/dutilleux2016.md`
(nuovo), `wiki/concepts/{time-stretching-granulare,sintesi-granulare-sincrona,micromontage}.md`,
`wiki/overview.md`, `wiki/sources/bibliography.md`, `wiki/index.md`,
`wiki/log.md` (questa entry).

---

## 2026-06-11 — Query + fix claim "copia fedele" (§2.1): finestratura come modulazione

Domanda: la claim «lo stream minimo ricostruisce fedelmente il materiale
sorgente» (paper.tex §2.1, con footnote «l'overlap-add restituisce la forma
d'onda di partenza») è sostenibile? No — verifica fonti raw + numerica.

Fonti trovate (finestratura = modulazione/filtraggio):
- Roads 2001 pp. 98 (stream periodico = AM, sidebands a 1/periodo inviluppo),
  101 (envelope contributes AM, 50 ms → 20 Hz, Table 3.1), 88 (Keller-Rolfe:
  comb-shaped spectral effects).
- Keller & Rolfe 1998 *The Corner Effect* (XII CIM pp. 236–239): quote
  verbatim estratte dal PDF degli atti («comb-filter delay» p. 238;
  «unwanted artifact by DSP theory becomes a useful parameter» p. 239).
- Dutilleux 2016 p. 110 («treno di impulsi filtrati», già in wiki).
- De Poli & Piccialli 1988 p. 70 («inviluppo ≡ finestra di analisi»).

Verifica numerica (OLA numpy): PGE usa `np.hanning` (Hann simmetrica) →
ripple COLA 2.02·10⁻⁴ RMS = −73.9 dB a N=2400/hop=1200 (48 kHz, 50 ms,
overlap 2) — coincide col residuo −74 dB di fig. 1 del paper. Hann periodica:
elisione a precisione macchina. Il residuo è interamente spiegato.

Decisione (utente): rovescio argomentativo, non correzione minimale — la
copia fedele è caso limite dell'elisione dei prodotti di modulazione; anche
il grado zero finestra, somma e modula.

Propagazione:
1. `paper/paper.tex` §2.1: riscritto passaggio + footnote (cit. Roads2001 +
   KellerRolfe1998); «ricostruisca fedelmente» → «approssimi al meglio»;
   chiusa del paragrafo grado-zero riformulata.
2. Nuova pagina `concepts/finestratura-come-modulazione.md` (fonti, tabella
   verifica numerica, vincolo di onestà matematica, implicazione argomentativa).
3. `concepts/time-stretching-granulare.md`: corretta riga «COLA ricostruisce
   esattamente» → elisione quasi completa con ripple quantificato; link nuova
   pagina.
4. `sources/proceedings/keller-rolfe1998.md`: aggiunte 4 quote artefatto
   (comb-filter delay, corner come parametro, smearing, blurring) + citabilità
   § stream minimo.
5. `index.md`: entry Concepts per la nuova pagina.
6. `log.md`: questa entry.

File modificati: `paper/paper.tex`,
`wiki/concepts/finestratura-come-modulazione.md` (nuovo),
`wiki/concepts/time-stretching-granulare.md`,
`wiki/sources/proceedings/keller-rolfe1998.md`, `wiki/index.md`,
`wiki/log.md` (questa entry).
