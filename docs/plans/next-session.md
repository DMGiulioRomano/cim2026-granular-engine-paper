# Piano scrittura paper CIM 2026 — bottom-up

> **SUPERSEDED (2026-06-12).** Questo piano risale al 2026-05-28 e descrive la
> struttura pre-riallineamento (numerazione a 6 sezioni, tesi come premessa).
> Riferimenti aggiornati: struttura per label in `CLAUDE.md` («Paper
> structure»), citazioni in `wiki/concepts/mappa-citazioni-paper.md`
> (rigenerabile con `make cite-map`), tesi corrente in `wiki/overview.md`.
> Le parti operative ancora valide (scadenza, formato, checklist submission)
> restano leggibili qui sotto.

Scadenza submission: **20 giugno 2026** (EasyChair, rinviata dal 7 giugno)
Formato: comunicazione orale, 6–8 pagine, double-blind, italiano + abstract inglese
Branch di lavoro: `paper-bottom-up`

> **Deadline confermata: 20 giugno 2026.** L'incontro col maestro del **9 giugno
> mattina** cade prima della submission: c'è margine per la sua revisione del
> draft prima di sottomettere.

---

## Stato attuale (2026-05-28)

Draft completo bottom-up **già scritto** in `paper.tex` (branch `paper-bottom-up`):
6 pagine, compila pulito (`pdflatex` ×2 + `bibtex`), 19 riferimenti, zero undefined.
Struttura ristrutturata dopo incontro maestro (cfr.
`wiki/concepts/incontro-maestro-2026-05-28.md`). Variante top-down archiviata in
GitHub issue #1.

Resta: figura partitura su brano reale, rifinitura abstract, revisione narrativa,
verifica anonimizzazione, eventuale margine di lunghezza (ora al minimo 6 pp).

---

## Tesi (invariata)

> Ritorno volontario al tempo differito in un momento in cui il real-time è
> disponibile. Postura compositiva in cui composizione e studio della tecnica
> coincidono; il loop di feedback lungo — specifica → generazione → ascolto →
> riflessione → riscrittura — è lo spazio per abitare gli spazi compositivi della
> granulazione. **La tesi emerge alla fine come frutto del lavoro, non come
> premessa** (direttiva maestro: bottom-up).

---

## Struttura del paper (bottom-up — come da draft)

| Sez | Contenuto | pp |
|-----|-----------|----|
| 1. Introduzione | apertura **problem-driven**: programma Python, problema del controllo parametrico esplicito su migliaia di grani; anticipa i 3 contributi. Niente tre atti in apertura | ~0.5 |
| 2. Architettura | **dal grano (frozen dataclass) allo stream** → DSL YAML/tendency mask → inviluppi e cicli → controllori → multi-voce → renderer (NumPy nativo + OCP, Csound secondario) → cache → Language Server. Fig. 1 dopo i componenti | ~3 |
| 3. Partitura grafica | asse Y = posizione-buffer; encoding; output read-only; confronto precursori (Truax Fig.4, Roads polygon, GeoGraphy). Fig. 2 + Tab. confronto | ~1.5 |
| 4. Posizionamento | lit-review compatta e tardiva; **Truax corretto** (economia di mezzi, *Riverrun*); precursori CIM offline; arco deferred→RT→deferred (Lippe) | ~1.5 |
| 5. Implicazioni | loop lungo *abilitato* dal sistema; Risset 5 drawback; Di Scipio observation-driven; strumenti non neutri (Arcella) | ~1 |
| 6. Conclusioni | sviluppi futuri: GUI (secondo paper), real-time opzionale, didattica | ~0.3 |

**Mai** «è meglio fare così»: postura personale e situata.
**Mai** «Truax = real-time come cambio di paradigma compositivo» (cfr. memory
`feedback-truax-economia-mezzi`).

---

## Piano fino al 20 giugno

### Ora → 8 giugno — Materiale + revisione draft
- [ ] Realizzare/scegliere un brano reale e **esportare la partitura grafica**
      (PNG alta res, leggibile B&W) → sostituisce `score_example.png` in Fig. 2
- [ ] Rilettura critica del draft: ogni sezione aggancia la tesi; tono argomentativo
- [ ] Rifinire abstract inglese (150–200 parole; bozza già in `paper.tex`)
- [ ] Verificare che Fig. 1 (TikZ) sia leggibile in B&W

### 9 giugno — Incontro maestro
- [ ] Mostrare il draft completo; raccogliere feedback prima della submission

### 10 → 18 giugno — Integrazione feedback + finalizzazione
- [ ] Integrare le osservazioni del maestro
- [ ] Eventuale espansione per margine di lunghezza (ora 6 pp, minimo): Sez. 3 o 5
- [ ] Verifica anonimizzazione double-blind (nessun nome, nessun link repo; `[anonymous]`)
- [ ] Verificare ogni citazione contro `refs.bib`

### 19 → 20 giugno — Submission
- [ ] Compilazione PDF finale (`pdflatex` ×2 + `bibtex`)
- [ ] Controllo formato CIM (margini, 2 colonne, Times 10pt, 6–8 pp, no header/footer)
- [ ] Submission via EasyChair entro il 20 giugno

---

## Figure
- [x] Fig. 1 — Schema architettura (TikZ, B&W, vettoriale) — nel draft
- [ ] Fig. 2 — Partitura grafica su **brano reale** (sostituire `score_example.png`)
- Tab. 1 (multi-voce) e Tab. 2 (rappresentazioni visive) — nel draft

---

## Riferimenti (19 nel draft, range CIM 9–21)
Gabor1947, Roads1978, Roads1988, Roads1985cim, Truax1988, Truax1990, Truax1994,
Truax2014, DiScipio1991cim, DiScipio1994, DiScipioTisato1993cim, DePoliPiccialli1988,
Lippe1993cim, ValleLombardo2003, Arcella2012, Vaggione1996, Vaggione2002,
Markidis2024cim, Roads2012, Risset1999.

---

## Rischi
- **Brano per Fig. 2**: il maestro ha detto di non forzare un brano; per la *figura*
  basta una partitura rappresentativa, non un caso compositivo nel testo.
- **Lunghezza al minimo** (6 pp): margine sottile, evitare tagli che scendano sotto 6.

---

## Domande aperte da ingest precedenti

### Da [[pozzi2016]] (ingest 2026-05-27)
- Documentazione successiva (post-2016) del sistema Pozzi? Brano *Cocktail Break* finalizzato?
- Concept page `loop-lungo-cim.md` da creare quando 4 nodi siano allineati: Pozzi *Breakpoint* + Vaggione *progressive enrichment* (Roads 2005 p. 302) + Roads *economy of selection* (Roads 2012 pp. 28–29) + Di Scipio osservazione→modifica (Di Scipio 1994).
