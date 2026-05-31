# revision_checklist.md — Revisioni azionabili

Derivato da `review_report.md`. Ogni voce: **punto del paper · problema · fix · priorità**.
Riferimenti a `paper.tex` (commit `b9f75b0`). Materiale di correzione in
`figure_walkthrough.md`; dettaglio bibliografico in `references_audit.md`.

Priorità: **P1** bloccante per migliorare il paper · **P2** importante · **P3** rifinitura.

---

## P1 — Bloccanti

**1. Risolvere la categoria del sistema (granulazione/micromontage vs sintesi granulare). — ✅ RISOLTA**
- *Punto:* titolo (righe 73–74), abstract (righe 93–94), §1 (righe 128–138) — *vs* corpo
  §3/§4.
- *Problema:* il sistema **granula campioni** (YAML `sample`, `PointerController` =
  posizione di lettura): è *granulazione di campioni* / *granular sampling* / *micromontage*
  (Roads *Microsound* cap. 5; Lippe; Vaggione/Caires), **non** sintesi granulare in senso
  stretto (grani sintetizzati da primitiva Gabor). Titolo/abstract/§1 dicevano «sintesi
  granulare» senza distinguo; il corpo si riconosceva già come *granular sampling*.
- *Risolto in questa sessione:*
  - §1 (128–138): precisazione tassonomica — `granular sampling` (Lippe), granulazione di
    campioni / micromontage, posizione di lettura come parametro dominante. *Già presente
    (commit b9f75b0).*
  - §4 tradizione (603, 661–667): Gabor = paradigma-ombrello; Lippe = transizione
    synthesis↔sampling. *Già presente.*
  - **Titolo (73–74): ibrido applicato** — «…sintesi granulare in tempo differito:
    granulazione di campioni, controllo esplicito e partitura come retroazione». Ombrello
    cercabile + categoria dichiarata.
  - **Abstract (93–94): allineato** — ora dichiara «does not synthesise grains from a
    Gabor primitive but granulates recorded material… *granular sampling*». 199 parole.
- *Nota terminologica:* `granular sampling` = categoria tecnica del motore; `micromontage`
  = pratica compositiva. Non sinonimi: usare ciascuno al suo livello, non sostituirne uno
  ovunque.

**2. Far leggere la partitura in prosa.**
- *Punto:* §3, Fig.~\ref{fig:score} (righe 491–499).
- *Problema:* la figura è inclusa ma **muta** — nessuna riga la legge. È l'esempio
  lavorato che il paper non porta, lasciato inerte.
- *Fix:* innestare la lettura guidata (nuvola→diagonale = deviazione pointer; banda
  discendente = lettura retrograda; colore = pan; striscia inviluppi). Bozza in
  `figure_walkthrough.md` Parte 1. **Verificare i tempi/posizioni sul rendering reale.**

**3. Aggiungere ≥1 esempio YAML con esito sonoro interpretato.**
- *Punto:* §2, listati YAML (righe 229–238, 294–298, 340–346).
- *Problema:* gli esempi sono **sintattici**, mai «questa specifica produce all'ascolto…».
- *Fix:* dopo un listato (es. lo stream `clouds`), 2–3 frasi sull'esito percettivo atteso,
  collegate alla partitura.

**4. Citare Vocem come *foil*.**
- *Punto:* §3, righe 462–470 e Tab.~\ref{tab:repr}.
- *Problema:* il precedente più vicino (stesso asse Y) è assente; senza, il differenziatore
  «inversione di flusso» resta non dimostrato per contrasto.
- *Fix:* testo + riga di tabella pronti in `figure_walkthrough.md` (2.1). `\cite{Lopez1998}`
  — entry **già aggiunta** a `refs.bib` in questa sessione.

**5. Correggere la frase «frequenza convenzionale».**
- *Punto:* §3, righe 434–436.
- *Problema:* contraddice la Tab.~\ref{tab:repr} dello stesso paragrafo (Truax = mask,
  GeoGraphy = mappa spaziale: non frequenza). Incoerenza interna.
- *Fix:* riscrittura concordante in `figure_walkthrough.md` (2.3).

---

## P2 — Importanti

**6. Nominare EmissionControl2 come confronto contemporaneo.**
- *Punto:* §3 (chiusura) o §6.
- *Problema:* l'ambiente granulare-con-visualizzazione real-time di riferimento è assente;
  la scelta del differito non è definita rispetto a un polo attuale.
- *Fix:* blocco in `figure_walkthrough.md` (2.2). `\cite{Roads2021}` — già in `refs.bib`
  (oggi orfano).

**7. Aggiungere ≥1 caso diagnostico.**
- *Punto:* §3 o §5.
- *Problema:* il loop lungo è descritto, mai mostrato in azione (debolezza 3).
- *Fix:* un'iterazione specifica→grani→partitura→scarto→riscrittura. Template in
  `figure_walkthrough.md` Parte 1 — **riempire con un episodio reale, non inventato.**

**8. Quantificare la performance.**
- *Punto:* §2, riga 400 («tempo di build […] dell'ordine dei minuti»).
- *Problema:* dato vago, nessun numero.
- *Fix:* grani/s, picco di memoria, tempo di build misurato su un brano di riferimento.

**9. Rendere percettivi i meccanismi-chiave (almeno 3).**
- *Punto:* §2 — `distribution` 0→1 (righe 313–316), finestra di loop statica/mobile
  (righe 319–320), multi-voce `stochastic` vs `chord` (Tab.~\ref{tab:voci}, riga 343).
- *Problema:* definiti come meccanica, mai come esito d'ascolto.
- *Fix:* 1–2 frasi percettive per ciascuno (sincrono = pulsato/metronomico vs asincrono =
  diffuso; loop mobile = punto d'ascolto che scorre; chord = impasto armonico vs stochastic
  = dispersione).

---

## P3 — Rifinitura

**10. Frasi di mediazione dopo i nodi teorici densi.**
- *Punto:* §2 righe 259–265 (ortogonalità gate/range); §5 righe 627–628 (chiusa
  «strumento e argomento»).
- *Fix:* dopo il passaggio denso, una frase che lo riporti a un esempio o a una conseguenza
  concreta. Non sovra-correggere: la voce del paper è un pregio.

**11. (Opz.) Alleggerire una o due chiuse aforistiche.**
- *Punto:* chiuse di §2/§5.
- *Fix:* mantenere il registro, ridurre la frequenza degli effetti.

**12. Completare i numeri di pagina dei virgolettati.**
- *Punto:* §2/§3/§4/§5 — quote senza pagina (cfr. `references_audit.md` §C).
- *Fix:* aggiungere — `DiScipio1991cim` p. 345 · `Lippe1993cim` p. 180 · `Truax2014` p. 2 ·
  `DiScipio1994` p. 142 · `Arcella2012` (non-neutralità) p. 148. **Verificare sul PDF** la
  pagina di `Truax1990` («it would be absurd…») o parafrasare togliendo le virgolette.

**13. (Tracking, non tocca il PDF) Allineare il titolo di `ValleLombardo2003`.**
- *Punto:* `wiki/sources/bibliography.md`, sezione «Debito Zotero».
- *Problema:* riporta «A Two-Level System for Grain Generation and Control Structure»;
  `refs.bib` (corretto) ha «A Two-Level Method to Control Granular Synthesis».
- *Fix:* correggere la riga di tracking.

---

## Quadro di priorità

| # | Revisione | Priorità | Materiale pronto |
|---|-----------|----------|------------------|
| 1 | Categoria sistema (granulazione/micromontage) | P1 | ✅ fatto (titolo ibrido + abstract) |
| 2 | Lettura guidata partitura | P1 | figure_walkthrough Parte 1 |
| 3 | YAML con esito sonoro | P1 | — |
| 4 | Vocem foil + tabella | P1 | figure_walkthrough 2.1 (+ refs.bib fatto) |
| 5 | Correzione «frequenza» | P1 | figure_walkthrough 2.3 |
| 6 | EC2 confronto | P2 | figure_walkthrough 2.2 |
| 7 | Caso diagnostico | P2 | figure_walkthrough Parte 1 (template) |
| 8 | Numeri di performance | P2 | — |
| 9 | Meccanismi percettivi | P2 | — |
| 10 | Frasi di mediazione | P3 | — |
| 11 | Chiuse aforistiche | P3 | — |
| 12 | Pagine dei virgolettati | P3 | references_audit §C |
| 13 | Refuso tracking title | P3 | references_audit §F |
