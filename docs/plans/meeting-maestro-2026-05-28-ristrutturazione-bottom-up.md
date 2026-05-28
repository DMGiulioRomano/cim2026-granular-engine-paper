# Piano — Ingest incontro maestro + riscrittura paper bottom-up

## Context

Utente ha incontrato maestro per mostrare stato paper CIM 2026 (PythonGranularEngine, deferred-time granular synthesis). Trascrizione Whisper in `inbox/audio.txt` (826 righe). Risset 1999 già ingestito in `wiki/sources/papers/risset1999.md`. Maestro ha contestato lettura attuale di Truax + raccomanda struttura bottom-up + consiglia studio stilistico dei paper antichi citati + sconsiglia di forzare il brano + dice di tenere GUI editor browser per secondo paper futuro.

`paper.tex` corrente (500 righe, intro + Sez 2 + Sez 3 parziale) è generazione Claude precedente. Utente conferma: può essere **scartato per intero** e riscritto da zero — niente piccole correzioni.

Nuova doc canonica PGE disponibile in `raw/PythonGranularEngine/docs/` — struttura Diátaxis (reference / explanation / how-to) con `INDEX.md` auto-generato. Da usare in parallelo a `wiki/sources/pge/` (analisi LLM-orientata) come fonte canonica per descrizione architettura.

## Verifica trascrizione su consigli stilistici maestro

Onestà filologica: maestro NON ha detto specificamente "studia Truax/Roads come modello bottom-up della spina dorsale". Quello che ha detto (righe 706–733, 763–771):

> *«alcuni dei [paper] più antichi che tu citavi [...] potrebbero essere utili. [...] quando leggi uno di questi paper leggi non solo contenuti ma leggi anche come [...] si è sforzato [...] di comunicarli con chiarezza [...] proprio l'analisi compositiva di come è stato scritto, di come ha portato anche la narrazione»*

Quindi: consiglio generale di analisi narrativa dei paper antichi citati come modello stilistico. *Quali* paper non specificato.

Interpretazione utente (studiare Truax 1988 + Roads 1985cim/1988 come modelli di descrizione bottom-up del proprio sistema) è coerente con il consiglio generale del maestro ed è razionale: sono i paper canonici della tradizione granulare in cui un autore descrive il proprio sistema. Procediamo con questa lettura, segnalando esplicitamente che è interpretazione e non quote.

## Punti operativi dal maestro

1. **Risset come ancora filosofica deferred** — confermato; usare quote pietra-angolare p. 37 da `wiki/sources/papers/risset1999.md`.

2. **CORREZIONE Truax**: il non-determinismo statistico è **economia di mezzi** per gestire centinaia di grani/sec, NON cambio di paradigma compositivo. Truax stesso usa regioni armoniche progettate (es. *Riverrun* tendency mask a 100/200/300 Hz). La granularità *scende nell'intimo del segnale* e impone scelte macro di altro tipo — questo è il punto compositivo.

3. **Struttura BOTTOM-UP**: parti da PGE come programma Python → architettura → relate a esistente → implicazioni teorico-compositive **alla fine**. Avvertimento maestro: *«stai assommando, ma non focalizzando»*.

4. **GUI editor → secondo paper futuro**. Non menzionare qui.

5. **Niente brano forzato** — Sez 5 caso compositivo eliminata.

6. **Scrittura artigianale** non sperimentale. Studia narrativa paper antichi citati come modelli stilistici.

## Decisioni utente

- **Solo branch bottom-up** sviluppato. Top-down archiviato come GitHub issue con piano dettagliato per eventuale ripensamento.
- **`paper.tex` scartabile per intero** — riscrittura da zero, niente patch.
- Doc PGE canonica `raw/PythonGranularEngine/docs/` come fonte oltre a `wiki/sources/pge/`.

---

## Piano operativo

### Step 1 — Ingest verbale incontro come pagina wiki

File nuovo: `wiki/concepts/incontro-maestro-2026-05-28.md`. Categoria `concepts/` perché contiene direttive metodologiche cross-sezione, non fonte da citare.

Sezioni:
- Data, contesto, modalità (trascrizione Whisper di audio in `inbox/audio.txt`)
- Sintesi richieste maestro (5 punti operativi sopra)
- Quote chiave verbatim con numero di riga della trascrizione
- Distinzione esplicita tra **quote testuali** e **interpretazione utente** (es. "Truax/Roads come modello bottom-up" = interpretazione)
- Mapping richieste → impatto sul paper
- Decisioni prese in questa sessione

Aggiornare `wiki/index.md` (entry nuova in sezione concepts) e `wiki/log.md` (entry sessione).

### Step 2 — Correzione `wiki/overview.md` (Atto 2 Truax)

Modifica chirurgica al paragrafo "Tesi corrente" (righe 9–13): rimuovere formulazione *«Truax teorizza il real-time come cambio di paradigma»*. Sostituire con: Truax 1988 = consolidamento tecnico DMX-1000 + adozione tendency mask come **economia di mezzi** per densità granulare. Non-determinismo statistico ≠ postura compositiva; convive con regioni armoniche progettate quando il materiale lo richiede. Il vero punto compositivo della granularità: *scende nell'intimo del segnale* → impone scelte macro di altro tipo.

La tesi PGE *ritorno volontario al deferred* resta invariata; cambia come si argomenta l'Atto 2.

### Step 3 — GitHub issue archivio branch top-down

Aprire issue nel repository `cim2026-granular-engine-paper` con label `paper-strategy` (creare label se non esiste):

Titolo: `Variante top-down della narrazione: piano dettagliato per riferimento futuro`

Body: piano completo della variante top-down (narrazione tre atti Roads/Di Scipio → Truax → PGE in apertura; struttura sezioni attuale corretta su Truax; ridistribuzione 1 pp da Sez 5 a Sez 4+6; Risset in conclusioni). Conclude con: *«variante scartata in favore della struttura bottom-up dopo incontro maestro 2026-05-28; lasciata come riferimento per eventuale ripensamento»*.

Verificare con `gh auth status` che l'autenticazione GitHub sia attiva prima di aprire l'issue.

### Step 4 — Studio stilistico paper antichi per modello bottom-up

**Vincolo documentale**: schema ingest `wiki/sources/papers/` definito in CLAUDE.md NON include sezione "Note stilistiche" (presente solo in `proceedings/`). Quindi per Truax 1988, Roads 1978, Roads 1988 i markdown wiki esistenti coprono contenuto ma non architettura espositiva. Bisogna tornare ai PDF originali.

PDF disponibili in `raw/papers/`:
- `Truax_1988_Real-Time-Granular-Synthesis-with-a-Digital-Signal-Processor.pdf` (CMJ 12.2)
- `Truax_1990_Composing-with-Real-Time-Granular-Sound.pdf`
- `Roads_1978_Automated-Granular-Synthesis-of-Sound.pdf` (CMJ 2.2)
- `Roads_1988_Introduction-to-Granular-Synthesis.pdf` (CMJ 12.2)

Per ognuno estrarre (lettura diretta PDF):
- Apertura: prime 2 frasi del paper (apertura tecnica / teorica / storica)
- Ordine sezioni con loro titoli effettivi
- Posizione del diagramma di sistema (in quale sezione compare la prima figura tecnica)
- Posizione delle citazioni: dove si concentra il lit-review (apertura / intercalata / chiusura)
- Posizione delle implicazioni teoriche (in apertura come tesi premessa / intercalate / in chiusura come riflessione)
- Densità ref/pagina e tipo di ref (foundational vs vicine)
- Forma della chiusura (sviluppi futuri tecnici / implicazioni musicali / entrambi)

Aggiungere a confronto:
- `wiki/sources/proceedings/arcella-silvestri2012.md` — già ingestito con sezione "Note stilistiche", modello CIM recente di tool paper bottom-up
- `wiki/sources/proceedings/anatrini2024.md` — CIM 2024, già con note stilistiche

Output: 
1. Estensione schema `wiki/sources/papers/`: aggiungere sezione opzionale "Architettura espositiva" alle pagine di Truax 1988, Roads 1978, Roads 1988 (estensione retroattiva del workflow ingest in CLAUDE.md → propagabile a futuri ingest)
2. Pagina nuova `wiki/concepts/modelli-stilistici-bottom-up.md` con scaletta sintetica: matrice paper × dimensione espositiva → derivazione spina dorsale paper CIM 2026

Aggiornamento workflow CLAUDE.md: aggiungere campo "Architettura espositiva" come sezione opzionale dello schema `papers/` (non retroattivo per tutti gli ingest, solo dove rilevante come modello stilistico).

### Step 5 — Riscrittura `paper.tex` da zero in branch dedicato

Branch nuovo: `paper-bottom-up` da `main`.

Struttura proposta (rivedibile dopo Step 4):

| Sez | Contenuto | pp target |
|-----|-----------|-----------|
| 1. Introduzione | apertura tecnica: programma Python per sintesi granulare in tempo differito; problema controllo parametrico esplicito; tre frasi su cosa il sistema fa concretamente | 0.5 |
| 2. Architettura del sistema | YAML come DSL; ParameterOrchestrator + Stream/Voice/Controller; renderer NumPy/Csound; cache per-stream SHA-256; Language Server; STEMS export. Schema architettura come Fig. 1 | 2.5 |
| 3. La partitura grafica | asse Y = posizione-buffer; encoding visivo per-grano; ruolo nel workflow loop lungo. Screenshot brano reale come Fig. 2 (principale) | 1.5 |
| 4. Posizionamento nella tradizione | lit review compatta: Roads/Truax canone + tendency mask come economia di mezzi (Truax corretto); Di Scipio/Tisato/Arcella+Silvestri precursori CIM; Risset voce critica deferred contemporanea | 1.5 |
| 5. Implicazioni teorico-compositive | il loop lungo emerge come postura abilitata dal sistema, non come tesi premessa. Quote Risset p. 37 + Roads economy of selection 2012 + Di Scipio observation-driven 1994. Citazione *«tools and technologies are not neutral»* Arcella/Silvestri 2012 | 1 |
| 6. Conclusioni | sviluppi futuri (GUI come secondo paper, real-time opzionale, didattica) | 0.3 |

Vincoli CIM 2026 invariati: 6–8 pp, Times 10 pt, due colonne, A4, doppio cieco, italiano + abstract inglese 150–200 parole.

Fonti documentali per Sez 2 e Sez 3:
- `wiki/sources/pge/*.md` (analisi LLM dei moduli — già usato)
- `raw/PythonGranularEngine/docs/explanation/architecture.md` (doc canonica progetto — nuovo)
- `raw/PythonGranularEngine/docs/explanation/multi-voice.md`
- `raw/PythonGranularEngine/docs/explanation/caching.md`
- `raw/PythonGranularEngine/docs/reference/yaml.md` (per descrizione DSL)
- `graph/class_diagram.puml` per figura architettura

Fonti per Sez 4: tutte le pagine in `wiki/sources/papers/` e `wiki/sources/proceedings/`, modulando densità citazionale per non oltrepassare range CIM 9–21 ref totali.

### Step 6 — Aggiornamento `docs/plans/next-session.md`

Sostituire calendario settimanale corrente con:
- Settimana corrente: ingest verbale + correzione overview + GitHub issue top-down + studio stilistico
- Settimana 2: schema architettura (Fig. 1) + screenshot partitura (Fig. 2) + abstract inglese
- Settimana 3: Sez 1+2 scritte
- Settimana 4: Sez 3+4 scritte
- Settimana 5: Sez 5+6 scritte + revisione + submission

Deadline submission: 7 giugno 2026.

### Step 7 — Salvataggio memoria

Due memory file:

**Feedback memory** `feedback_truax_economia_mezzi.md`: maestro ha contestato lettura di Truax come cambio di paradigma compositivo. Il non-determinismo statistico in Truax è economia di mezzi per densità granulare (centinaia di grani/sec non razionalizzabili in event-list deterministica Music V/Csound), non postura. Convive con regioni armoniche progettate (Riverrun). *Why:* incontro maestro 2026-05-28, trascrizione `inbox/audio.txt` righe 38–86. *How to apply:* mai formulare "Truax = real-time come cambio di paradigma compositivo" nel paper o nel wiki.

**Project memory** `project_paper_cim_ristrutturazione.md`: paper CIM 2026 ristrutturato bottom-up dopo incontro maestro 2026-05-28; `paper.tex` scartato e riscritto da zero in branch `paper-bottom-up`; Sez 5 caso compositivo eliminata; GUI editor browser fuori scope (→ secondo paper futuro); variante top-down archiviata come GitHub issue. *Why:* direttive maestro + decisioni utente in questa sessione. *How to apply:* quando lavoro sul paper sapere che scope è ristretto, che esiste un GitHub issue con variante alternativa, che la doc PGE canonica è in `raw/PythonGranularEngine/docs/`.

---

## File coinvolti

- `inbox/audio.txt` — read-only fonte verbale
- nuovo: `wiki/concepts/incontro-maestro-2026-05-28.md`
- nuovo: `wiki/concepts/modelli-stilistici-bottom-up.md`
- `wiki/overview.md` — correzione Tesi corrente righe 9–13
- `wiki/index.md` — entry nuove
- `wiki/log.md` — entry sessione
- `docs/plans/next-session.md` — calendario aggiornato
- GitHub issue nuovo (variante top-down archiviata)
- branch git nuovo `paper-bottom-up`
- `paper.tex` (in branch) — scartato e riscritto da zero
- Memory: `feedback_truax_economia_mezzi.md` + `project_paper_cim_ristrutturazione.md`

## Verifica

- `gh issue list` mostra nuovo issue label `paper-strategy`
- `wiki/overview.md` non contiene più "Truax teorizza il real-time come cambio di paradigma"
- `wiki/concepts/incontro-maestro-2026-05-28.md` esiste, linkato da `index.md`, contiene quote verbatim con numeri riga
- `git branch -a` mostra `paper-bottom-up`
- `pdflatex paper.tex` (in branch) compila senza errori, output 6–8 pp
- Nessuna menzione GUI editor in `paper.tex` finale
- Risset citato in Sez 5 con quote pietra-angolare p. 37
- Truax citato senza formulazione "cambio di paradigma compositivo"; tendency mask presentato come economia di mezzi
- Decisione submission entro 2026-06-03 per polish residuo + EasyChair upload entro 2026-06-07
