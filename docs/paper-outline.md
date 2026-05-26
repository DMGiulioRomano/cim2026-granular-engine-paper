# CIM 2026 — Outline paper: PythonGranularEngine

**Venue:** XXV Colloquio di Informatica Musicale, L'Aquila, 13–16 ottobre 2026
**Categoria:** comunicazione orale, 6–8 pp., double-blind peer review
**Lingua:** italiano + abstract inglese (150–200 parole)
**Deadline submission:** 7 giugno 2026 — EasyChair

---

## Tesi

PGE (PythonGranularEngine) è un ambiente di sintesi granulare in Python
interamente in tempo differito. Si inserisce nella tradizione CIM di
granulazione offline con controllo algoritmico ad alto livello — Roads
(CIM VI, 1985), Di Scipio (CIM IX, 1991), Di Scipio–Tisato (CIM X, 1993),
Arcella–Silvestri (CIM XIX, 2012) — ereditandone il pattern architetturale
fondamentale: separazione netta tra linguaggio di specifica e motore di
rendering, audio come risultato di un processo deferred.

Tre atti narrativi: (1) Roads 1978 / Di Scipio 1991, *tempo differito come
necessità hardware*; (2) Truax 1988, il DMX-1000 rompe il vincolo e il
real-time diventa cambio di paradigma; (3) PGE, *ritorno volontario al
tempo differito* in un momento in cui il real-time è disponibile. Non è un
passo indietro: corrisponde a una postura compositiva in cui composizione
e studio della tecnica coincidono, e in cui il **loop di feedback lungo**
(specifica → generazione → ascolto → riflessione → riscrittura) è lo spazio
necessario per abitare la granulazione come forma e struttura.

Postura **personale e situata**: il paper non afferma "è meglio fare così".

---

## Contributi (tre)

1. **YAML DSL + Language Server (PGE-ls)** — specifica dichiarativa di
   intenzioni parametriche (range, distribuzioni, envelope), tradotta dal
   motore in migliaia di grani; LSP riduce il costo cognitivo del DSL.
2. **Partitura grafica con asse Y = posizione nel buffer sorgente** —
   notazione non convenzionale che rende visibile *dove* ogni grano pesca
   nel campione (informazione non udibile direttamente). Output, non input.
3. **Workflow STEMS** — rendering per-stream, cache incrementale SHA-256,
   export progetto Reaper auto-generato con struttura temporale YAML
   mappata. Istituzionalizza la pipeline di higher-order granulation
   descritta da Roads (2012).

---

## Indice e contenuti

### 1. Introduzione (~0.75 pp.)

**Obiettivo:** narrazione tre atti come apertura argomentativa.

- Atto 1 — Roads 1978, Di Scipio 1991: tempo differito per necessità
  hardware (computer non regge real-time granulare).
- Atto 2 — Truax 1988: DMX-1000 rompe il vincolo; real-time come
  abbandono del pensiero lineare pre-scritto, multi-task, feedback
  immediato (cit. *"abandon linear modes of compositional thinking […]
  substitute process-oriented multitask strategies"*).
- Atto 3 — PGE: ritorno volontario al tempo differito come postura.
  Il giudizio drammaturgico del compositore garantisce la non-linearità
  in entrambi i casi; cambia solo la scala temporale del feedback.

**Citazioni:** `Truax1988`, `Roads1978`, `DiScipio1991cim`, `Arcella2012`
(quote *"tools and technologies […] are not neutral"*).

---

### 2. Sintesi granulare: dal paradigma Gabor al controllo gerarchico (~1.5 pp.)

**Obiettivo:** panoramica storica funzionale alla tesi — non enciclopedica.

- Gabor 1947: grano come quanto tempo-frequenza, Deltat·Deltaf >= 1.
- Roads 1978/1988: prima implementazione, vocabolario canonico,
  pattern *front-end → engine* come precursore architetturale PGE.
- Truax 1988: gerarchia di controllo (Fig. 3) + Tabella 1
  *psychoacoustic correlates* (ciò che il loop lungo permette di
  verificare empiricamente, parametro per parametro).
- Truax 1990: "absurd to specify each grain"; gap controllo/percezione.
- Truax 1994: separazione micro/macro come tesi psicoacustica abilitante.
- Ramo CIM italiano: De Poli/Piccialli 1988/1991, Ortosecco/Piccialli 1989
  (wavelet=grano, precompute-once/reuse-many tipo `WindowGenerator` PGE).
- Precursori CIM offline: Roads 1985 (problema `d·n`, frame, event,
  polygon su piano freq/tempo), Di Scipio 1991, Arcella–Silvestri 2012
  (topologia *algoritmo → score → Csound → audio*).

**Citazioni:** `Gabor1947`, `Roads1978`, `Roads1988`, `Truax1988`,
`Truax1990`, `Truax1994`, `Roads1985cim`, `DiScipio1991cim`, `Arcella2012`,
`OrtoseccoPiccialli1989`.

---

### 3. PGE: architettura per l'indagine parametrica (~1.75 pp.)

**Obiettivo:** descrizione del sistema orientata alla tesi — non catalogo
di feature. Ogni componente è presentato come implementazione del loop
lungo.

- **YAML come DSL/IR**: il compositore specifica *intenzioni parametriche*
  (range, probabilità, envelope), non grani. Distinzione esplicita da
  `.sco` Csound grezzo. Pattern front-end/IR già in Roads 1978.
- **ParameterOrchestrator**: Envelope time-varying, dephase per-grano,
  strategie esclusive (`fill_factor` vs `density` come corrispettivo
  percettivo della Tabella 1 Truax).
- **Language Server (PGE-ls)**: scaffolding del loop lungo.
- **Dual renderer bit-identico** (NumPy / Csound): abbassa la barriera
  d'installazione.
- **Cache incrementale + solo/mute per stream**: il ciclo
  modifica-un-parametro → riascolta è praticabile.

**Figura 1:** schema architettura YAML → engine → audio + graphic score
(B&W vettoriale).

**Citazioni:** `Roads1978` (front-end/engine), `Truax1988` (Stream
ispirato a DMX-1000), `Arcella2012` (topologia condivisa, livelli di
astrazione divergenti), `PGE`, `PGEls`.

---

### 4. La partitura grafica come strumento di retroazione (~1.5 pp.)

**Obiettivo:** lo `score_visualizer` come strumento del loop lungo —
non precede il processo compositivo, lo traccia e lo rende leggibile.

- Piano tempo × posizione-buffer: motivazione dell'asse Y non-frequenza
  (rende visibile *da dove* ogni grano pesca nel campione). Giustificata
  percettivamente da Truax 2014: *"listening inside the sound"*.
- Encoding visivo: frecce (direzione playback), colore (pitch ratio),
  opacità (volume), loop mask, envelope panel separato.
- Uso nel loop lungo: si legge dopo l'ascolto per capire cosa ha prodotto
  una scelta parametrica, poi si torna al YAML.
- Confronto con precursori: Truax 1988 Fig. 4 (overlay ASCII tendency
  masks — *input* di controllo); Roads 1978/1988 (polygon su freq/tempo —
  metafora); Roads 2006 progetto Ynez (*study scores*, antesignano
  programmatico); EC2 Scan Display (Roads 2021, real-time gestural).
  PGE inverte il segno: partitura come *output* delle decisioni.

**Figura 2 (principale):** screenshot partitura grafica su brano reale
(alta risoluzione, leggibile in B&W).

**Citazioni:** `Truax1988`, `Roads1978`, `Roads1988`, `Truax1994`,
`Truax2014`, `Roads2006`, `Roads2021`.

---

### 5. Caso compositivo (~1 p.)

**Obiettivo:** brano realizzato con PGE (~3 minuti). Descrizione del
*processo*, non del risultato estetico.

- Da stream semplici (pochi parametri) verso progressiva complicazione.
- Almeno una scelta compositiva concreta motivata dalla lettura della
  partitura — qualcosa che solo il loop lungo ha reso visibile e
  modificabile.
- Pattern espositivo: "ho specificato X, la partitura mostrava Y, ho
  cambiato Z, il risultato è diventato W."

**Citazioni:** `Truax1994` (brani Truax come termine di confronto per
postura), `Vaggione2002` (décorrélation microtemporelle).

---

### 6. Conclusioni (~0.5 pp.)

**Obiettivo:** PGE come ambiente per il loop lungo nella granulazione
deferred. Contributo non solo tecnico ma metodologico: YAML → audio →
partitura come spazio di coabitazione tra composizione e studio della
tecnica.

**Sviluppi futuri:** interfaccia grafica, estensione real-time
opzionale, uso didattico formale.

**Citazioni:** `Truax2014`, `Roads2012`, `Roads2021`, `Arcella2012`.

---

## Bibliografia chiave (target 12–16 ref. su un censito di ~40)

**Fondazionali:** `Gabor1947`.

**Truax / Roads canone:** `Roads1978`, `Roads1988`, `Roads2001`,
`Roads2012`, `Truax1988`, `Truax1990`, `Truax1994`, `Truax2014`.

**Precursori CIM offline:** `Roads1985cim`, `DiScipio1991cim`,
`DiScipioTisato1993cim`, `Arcella2012`, `OrtoseccoPiccialli1989`.

**Contemporanei (poli opposti):** `Roads2021` (EC2 real-time),
`Anatrini2024` (deep learning), `Markidis2024cim` (ecosystemic).

**Sistema:** `PGE`, `PGEls`.

Selezione finale da fare in fase di scrittura. Vincolo CIM: 9–21 ref.
tipici per tool/system paper.

---

## Figure pianificate

1. **Fig. 1** — Schema architettura PGE (Sez. 3). B&W vettoriale.
2. **Fig. 2** — Screenshot partitura grafica su brano reale (Sez. 4).
   Figura principale.
3. **Fig. 3 (opzionale)** — Dettaglio YAML annotato (Sez. 3).

---

## Vincoli formato CIM 2026

- A4 portrait, area testo 17.2 × 25.2 cm. Margini: top 2.0, bottom 2.5,
  left/right 1.9 cm.
- Due colonne 8.2 cm + gutter 0.8 cm.
- Times New Roman 10 pt body, 12 pt heading, 16 pt title bold caps.
- No header, footer, page number nel PDF sottomesso (li aggiunge
  l'editor degli atti).
- Copyright 8 pt bottom-left p. 1.
- Riferimenti numerati `[1]`, ordine alfabetico.
- **Double-blind:** PDF anonimizzato. Nessun nome autore, affiliazione,
  link repo riconoscibile. Auto-citazioni → "the system described in
  [anonymous]".

---

## Stato lavoro (al 26 maggio 2026)

- Wiki knowledge base: 33 paper + 20 atti CIM + 9 moduli PGE + 5 concept
  page. Pronta per scrittura.
- `paper.tex`: scheletro template CIM 2026, sezioni vuote.
- `refs.bib`: entry papers OK; **18 entry proceedings CIM da registrare
  in Zotero prima di iniziare a scrivere** (vedi
  `wiki/sources/bibliography.md` "Debito Zotero").
- Brano compositivo (Sez. 5): in produzione.
- Figura architettura (Fig. 1): da realizzare.
