# Piano scrittura paper CIM 2026

Scadenza submission: **7 giugno 2026**
Disponibilità: ~7 ore/settimana × 4 settimane = 28 ore totali
Formato: comunicazione orale, 6–8 pagine, double-blind, italiano + abstract inglese

---

## Tesi

> PGE è un ritorno volontario al tempo differito in un momento in cui il real-time
> è disponibile. Questo ritorno corrisponde a una postura compositiva specifica:
> quella in cui composizione e studio della tecnica coincidono, e in cui il loop
> di feedback lungo — specifica → generazione → ascolto → riflessione → riscrittura
> — è lo spazio necessario per abitare gli spazi compositivi della granulazione
> come forma e struttura.

---

## Struttura del paper

### Sezione 1 — Introduzione (~0.75 pp)

**Argomento:** La narrazione in tre atti come apertura argomentativa.

- **Atto 1:** Roads 1978, Di Scipio 1991 — tempo differito come necessità hardware.
  Il computer non regge il real-time granulare; l'unico modo è scrivere,
  compilare, ascoltare dopo.
- **Atto 2:** Truax 1988 — il DMX-1000 rompe il vincolo. Truax teorizza il
  real-time come cambio di paradigma: abbandono del pensiero lineare pre-scritto,
  processi multi-task, feedback immediato. Citare: *"The key is to abandon linear
  modes of compositional thinking [...] and to substitute process-oriented
  multitask strategies for real-time execution."*
- **Atto 3:** PGE — ritorno volontario al tempo differito. Non passo indietro,
  ma scelta compositiva: il loop lungo come spazio di riflessione su forma e
  struttura. Il giudizio drammaturgico del compositore garantisce la non-linearità
  del processo in entrambi i casi; cambia solo la scala temporale del feedback.

**Nota:** non formulare mai come "è meglio fare così". La postura è personale
e situata: "è il modo necessario nel momento in cui composizione e studio
della tecnica coincidono."

**Cita:** Truax1988 (citazione real-time), Roads1978 (primo sistema offline),
DiScipio1991cim (offline per necessità).

---

### Sezione 2 — Sintesi granulare: dal paradigma Gabor al controllo gerarchico (~1.5 pp)

**Argomento:** Panoramica storica essenziale, funzionale alla tesi.
Non enciclopedica — ogni autore citato deve servire la narrazione.

- Gabor 1947: il grano come quanto tempo-frequenza, Δt·Δf ≥ 1.
  Fondamento teorico del paradigma.
- Roads 1978/1988: prima implementazione, vocabolario canonico,
  pattern front-end → engine come precursore architetturale PGE.
- Truax 1988: gerarchia di controllo (Fig. 3), Tabella 1 psychoacoustic
  correlates. **Punto chiave:** la Tabella 1 descrive cosa il loop lungo
  permette di verificare empiricamente — ogni parametro ha un corrispettivo
  percettivo che va *ascoltato e riletto*, non solo letto numericamente.
- Truax 1990: gap controllo/percezione, "absurd to specify each grain".
- Truax 1994: separazione micro/macro come tesi psicoacustica abilitante.
- Precursori CIM offline: Roads 1985, Di Scipio 1991, Arcella 2012.

**Cita:** Gabor1947, Roads1978, Roads1988, Truax1988, Truax1990, Truax1994,
Roads1985cim, DiScipio1991cim, Arcella2012.

---

### Sezione 3 — PGE: architettura per l'indagine parametrica (~1.75 pp)

**Argomento:** Descrizione del sistema orientata alla tesi — non catalogo di feature.
Ogni componente va presentato come implementazione del loop lungo.

- **YAML come DSL/IR** (non score deterministico):
  il compositore specifica intenzioni parametriche (range, probabilità, envelope),
  non grani. Il motore traduce in migliaia di grani attraverso processi stocastici.
  Distinzione esplicita da .sco Csound grezzo. Pattern front-end/IR già in Roads 1978.
  *(Vedi note dettagliate in overview.md — sezione "Note per Sezione 3")*
- **ParameterOrchestrator:** Envelope, dephase, strategie esclusive
  (fill_factor vs density come corrispettivo percettivo della Tabella 1 Truax).
- **Language Server:** scaffolding per il loop lungo — riduce il costo cognitivo
  della specifica YAML.
- **Dual renderer bit-identico:** NumPy / Csound. Abbassa la barriera di
  installazione.
- **Cache incrementale + solo/mute:** il ciclo modifica-un-parametro → riascolta
  è praticabile. Implementazione tecnica del loop lungo iterativo.

**Figura:** schema architettura YAML → engine → audio + graphic score.
Leggibile in B&W.

**Cita:** Roads1978 (pattern front-end → engine), Truax1988 (Stream ispirato
a DMX-1000), PGE, PGEls.

---

### Sezione 4 — La partitura grafica come strumento di retroazione (~1.5 pp)

**Argomento:** ScoreVisualizer come strumento del loop lungo — non precede
il processo compositivo, lo traccia e lo rende leggibile.

- Piano tempo × posizione-buffer: perché questo asse Y (non frequenza).
  La posizione-buffer rende visibile *da dove* ogni grano pesca nel campione
  — informazione non udibile direttamente ma leggibile nella partitura.
- Encoding visivo: frecce (direzione = reverse/forward), colore (pitch ratio),
  opacità (volume), loop mask, envelope panel separato.
- Come si usa nel loop lungo: si legge la partitura dopo l'ascolto per capire
  cosa ha prodotto una scelta parametrica, poi si torna al YAML e si modifica.
- Confronto con precursori:
  - Truax 1988 Fig. 4: overlay ASCII tendency masks — **input** di controllo
    vs **output** analitico di PGE. Asse Y diverso.
  - Roads 1978/1988: polygon su piano freq/tempo — metafora notazionale,
    non output automatico del sistema.

**Figura principale del paper:** screenshot partitura grafica su brano reale.
Alta risoluzione, leggibile in B&W.

**Cita:** Truax1988 (Fig. 4), Roads1978, Roads1988, Truax1994 (asse Y come
visualizzazione del meccanismo TEF).

---

### Sezione 5 — Caso compositivo (~1 pp)

**Argomento:** Brano realizzato con PGE (~3 minuti).
Descrizione del loop lungo in azione: come si è partiti da stream semplici
(pochi parametri) e si è progressivamente complicato. Almeno una scelta
compositiva concreta motivata dalla lettura della partitura — qualcosa che
solo il loop lungo ha reso visibile e modificabile.

**Non descrivere il brano in termini estetici generici.** Descrivere il processo:
"ho specificato X, la partitura mostrava Y, ho cambiato Z, il risultato è
diventato W." Questo dimostra il funzionamento della tesi sul materiale reale.

**Cita:** Truax1994 (brani di Truax come termine di confronto per postura compositiva).

---

### Sezione 6 — Conclusioni (~0.5 pp)

**Argomento:** PGE come ambiente per il loop lungo nella granulazione in tempo
differito. Il contributo non è solo tecnico ma metodologico: il ciclo
YAML→audio→partitura come spazio di coabitazione tra composizione e studio
della tecnica. Sviluppi futuri: interfaccia grafica, estensione real-time
opzionale, uso in contesto didattico formale.

---

## Piano settimana per settimana

### Settimana 1 (7h) — Materiale
- [ ] Realizzare brano compositivo (~3 min) con PGE
- [ ] Esportare partitura grafica del brano (PNG alta res, leggibile in B&W)
- [ ] Preparare figura architettura (schema YAML→engine→output)
- [ ] Annotare durante il processo compositivo almeno una decisione
      motivata dalla lettura della partitura (serve per Sezione 5)

### Settimana 2 (7h) — Sezioni 1 + 2
- [ ] Scrivere Sezione 1 (Introduzione con narrazione tre atti) — 0.75 pp
- [ ] Scrivere Sezione 2 (Contesto teorico) — 1.5 pp
- [ ] Verificare che ogni citazione sia in refs.bib con chiave corretta

### Settimana 3 (7h) — Sezioni 3 + 4 + 5
- [ ] Scrivere Sezione 3 (Architettura) — 1.75 pp con figura architettura
- [ ] Scrivere Sezione 4 (Partitura grafica) — 1.5 pp con figura principale
- [ ] Scrivere Sezione 5 (Caso compositivo) — 1 pp

### Settimana 4 (7h) — Revisione + submission
- [ ] Scrivere Sezione 6 (Conclusioni) — 0.5 pp
- [ ] Scrivere abstract in inglese (150–200 parole)
- [ ] Revisione: ogni sezione aggancia la tesi (loop lungo / postura compositiva)
- [ ] Verificare che il paper non dica mai "è meglio fare così"
- [ ] Anonimizzazione double-blind (nessun nome, nessun link repo)
- [ ] Compilare PDF finale (due passate pdflatex)
- [ ] Submission via EasyChair entro 7 giugno 2026

---

## Checklist figure

- [ ] Fig. 1 — Schema architettura PGE (sezione 3) — B&W, vettoriale
- [ ] Fig. 2 — Screenshot partitura grafica su brano reale (sezione 4) — figura principale
- [ ] Fig. 3 (opzionale) — Dettaglio YAML annotato (sezione 3)

---

## Referenze target: 12–16

Solide: Roads1978, Roads1988, Truax1988, Truax1990, Truax1994, Gabor1947,
Roads1985cim, DiScipio1991cim, Arcella2012, PGE, PGEls.
Da valutare: Roads2001, DiScipio1994, 1–2 paper CIM 2022/2024 su tool simili.

---

## Rischio principale

Settimana 3 è la più densa. Non posticipare settimana 1 — il brano
e le figure servono *prima* di scrivere le sezioni 4 e 5.