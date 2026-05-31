# references_audit.md — Audit bibliografico

Paper sotto review: «Un ambiente Python per la sintesi granulare in tempo differito»
(commit `b9f75b0`). Esito della verifica delle voci bibliografiche citate, dei
numeri di pagina dei virgolettati, dei riferimenti orfani e di quelli mancanti.

**Metodo.** Per ogni `\cite` del paper: (a) esistenza e correttezza della voce in
`refs.bib`; (b) per ogni virgolettato, verifica del numero di pagina. Tre quote-ancora
verificate *verbatim* sui PDF primari in `raw/papers/` (marcate **PDF✓**); le restanti
confrontate con le pagine wiki estratte da PDF primario in sessione precedente
(marcate **wiki✓**). Nessun riferimento inventato. Dove una fonte non è verificabile
dal solo materiale a disposizione, è dichiarato.

---

## A. Voci citate — esistenza, venue, anno

20 chiavi distinte citate nel paper. Tutte presenti in `refs.bib` con venue e anno
corretti:

| Chiave | Tipo | Venue / anno | Stato |
|--------|------|--------------|-------|
| Gabor1947 | @article | Nature 159(4044), 1947 | ✓ |
| Roads1978 | @article | Computer Music Journal 2(2), 1978 | ✓ |
| Roads1988 | @article | Computer Music Journal 12(2), 1988 | ✓ |
| Roads1985cim | @inproceedings | Atti VI CIM, 1985, pp. 195–209 | ✓ |
| Roads2012 | @incollection | *Xenakis Matters*, Pendragon, 2012 | ✓ |
| Truax1988 | @article | Computer Music Journal 12(2), 1988, pp. 14–26 | ✓ |
| Truax1990 | @article | Perspectives of New Music 28(2), 1990 | ✓ |
| Truax1994 | @article | Computer Music Journal 18(2), 1994 | ✓ |
| Truax2014 | @article | eContact! 16(3), 2014 (online) | ✓ |
| DePoliPiccialli1988 | @inproceedings | Atti VII CIM, 1988, pp. 70–74 | ✓ |
| DiScipio1991cim | @inproceedings | Atti IX CIM, 1991, pp. 337–349 | ✓ |
| DiScipio1994 | @article | Contemporary Music Review 10(2), 1994 | ✓ |
| DiScipioTisato1993cim | @inproceedings | Atti X CIM, 1993, pp. 159–165 | ✓ |
| Lippe1993cim | @inproceedings | Atti X CIM, 1993, pp. 178–182 | ✓ |
| Arcella2012 | @inproceedings | Atti XIX CIM, 2012, pp. 144–148 | ✓ |
| Vaggione1996 | @inproceedings | JIM 1996, Tatihou | ✓ |
| Vaggione2002 | @inproceedings | JIM 2002, Marseille | ✓ |
| ValleLombardo2003 | @inproceedings | Atti XIV CIM, 2003, pp. 136–140 | ✓ |
| Markidis2024cim | @inproceedings | Atti XXIV CIM, 2024, pp. 48–56 | ✓ |
| Risset1999 | @article | Contemporary Music Review 18(3), 1999, pp. 31–39 | ✓ |

Nessuna citazione punta a una chiave assente da `refs.bib`. `pdflatex` risolve tutti
i `\cite`.

---

## B. Virgolettati con numero di pagina dichiarato

| Quote (incipit) | Chiave | Pag. nel paper | Verifica |
|-----------------|--------|----------------|----------|
| «déclaration d'un attribut […] généralisé à toutes les instances successives» | Vaggione1996 | p. 2 | wiki✓ (fonte francese) |
| «a single rule may instantiate multiple operations […] a step towards the abstract» | DiScipioTisato1993cim | p. 165 | wiki✓ |
| «score files […] are usually so large that they are impractical to handle» | Truax1988 | p. 14 | **PDF✓** |
| «the superimposition of many similar […] macro-level texture» / «the presence of any particular frequency component […] statistically determined» | Truax1988 | pp. 24–25 | wiki✓ |
| «a continuum between deterministic and stochastic choices» | Truax1988 | p. 23 | **PDF✓** |
| «links frequency and time at the micro level […] independently at the macro level» | Truax1994 | p. 44 | wiki✓ |
| «factor[ed] […] in two» | Arcella2012 | p. 147 | wiki✓ |
| «detached from real-time constraints, ideas can be tested, edited, submixed, or deleted at will» | Roads2012 | p. 8 | wiki✓ |
| «Composition is not — or should not be — a real-time process. […] Non real-time operation is necessary to free oneself of the arrow of time…» | Risset1999 | p. 37 | **PDF✓** |
| «the significance of the control settings is often unknown or obscure» | Risset1999 | p. 34 | wiki✓ |

I tre **PDF✓** sono risultati esatti carattere per carattere; il numero di pagina
combacia. Alta confidenza sulla correttezza dei **wiki✓** (stessa provenienza,
estratti con numero di pagina in fase di ingest).

---

## C. Virgolettati SENZA numero di pagina — da completare

Lo standard CIM per i virgolettati diretti richiede il numero di pagina. Questi quote
sono nel corpo del paper senza pagina, ma la pagina è disponibile e verificata in wiki.
**Raccomandazione: aggiungere il numero.**

| Quote (incipit) | Chiave | Pagina da aggiungere | Fonte |
|-----------------|--------|----------------------|-------|
| «it would be absurd to specify the parameters for each grain individually» | Truax1990 | da recuperare (PNM 28(2), art. p. 120–…) | non in wiki — **verificare sul PDF** |
| «queste procedure sono attualmente implementate in tempo differito, su un IBM PC 286 […] quantità di RAM» | DiScipio1991cim | p. 345 | wiki✓ |
| «of primary importance» | Lippe1993cim | p. 180 | wiki✓ |
| «inside the sound» | Truax2014 | p. 2 (eContact! online, numerazione PDF) | wiki✓ |
| «more operationalized than produced» | DiScipio1994 | p. 142 | wiki✓ |
| «tools and technologies used to produce a musical work are not neutral…» | Arcella2012 | p. 148 | wiki✓ |

Caso che richiede lettura diretta del PDF: **Truax1990** «it would be absurd…» — la
pagina non è registrata in wiki. Da verificare sul PDF prima di aggiungere il numero,
oppure rimuovere le virgolette e parafrasare.

---

## D. Riferimenti orfani in `refs.bib` (presenti ma non citati)

`refs.bib` contiene ~40 voci; ne sono citate 20. Le altre non compaiono nei `\cite`
del paper. Con `\bibliographystyle{plain}` le voci non citate **non vengono stampate**:
non producono un difetto nel PDF finale. `refs.bib` funziona come bibliografia di
lavoro (superset). Elenco orfani principali:

- Roads2001 (*Microsound*), Roads2006, Roads2001Pulsars, Roads2005
- **Roads2021 (EmissionControl2)** — vedi §E, da citare
- DePoliPiccialli1991, Vaggione1991, Solomos2003, Solomos2005, Caires2004
- DiScipio1995cim, DeTintis1995, Rizzuti2006, Silvestri2010
- AgostiniDaubresseGhisi2014, ValentiValleServetti2014, MarkidisFernandez2016cim, Pozzi2016
- KellerRolfe1998, RolfeKeller2000, OrtoseccoPiccialli1989, Sparano2018, Cera2022, Anatrini2024
- Roads1988 è citato; Wegner1997 è orfano (fonte non musicale)

Nessuna azione obbligatoria. Nota: il paper cita 20 fonti — entro il range CIM tool
paper (9–21). Non serve gonfiare la bibliografia con gli orfani.

---

## E. Riferimenti mancanti da raccomandare

1. **Lopez1998 — Vocem** (López, Martí, Resina, *Vocem: An Application for Real-Time
   Granular Synthesis*, Proc. DAFx-98, Barcelona). **Aggiunto a `refs.bib`** in questa
   sessione (chiave `Lopez1998`, PDF in `raw/papers/`). Non ancora `\cite`-ato.
   Da citare in §3 come *foil* (vedi `figure_walkthrough.md`).
   - **Pagine: brief dichiara pp. 2–5; il PDF locale ha 4 facciate, coerente.** Numero
     di pagina iniziale **da confermare** sull'indice degli atti DAFx-98 (non
     ricavabile dal solo PDF dell'articolo). Entry attuale: `pages = {2--5}`.
   - Citazione di pagina per la Fig. 2 (asse): l'articolo non numera le pagine; la
     descrizione dell'asse è nella didascalia di Fig. 2 (terza facciata del PDF).

2. **Roads2021 — EmissionControl2** (CMJ 45(3):20–38, 2021). Già in `refs.bib`,
   orfano. Da citare in §3/§6 come confronto granulare-con-visualizzazione
   contemporaneo (real-time, "Scan Display"). Priorità P2.

---

## F. Incongruenze di tracking (non bloccanti)

- **`wiki/sources/bibliography.md` riga "Debito Zotero"** riporta per `ValleLombardo2003`
  il titolo *"A Two-Level System for Grain Generation and Control Structure"*, mentre
  `refs.bib` e la pagina wiki del proceedings danno *"A Two-Level Method to Control
  Granular Synthesis"*. Il titolo di `refs.bib` è quello citato. Allineare la riga di
  tracking (refuso interno, non tocca il PDF).

---

## G. Sintesi

- **Esistenza/venue/anno**: 20/20 corretti. Nessuna citazione fantasma.
- **Virgolettati con pagina**: 10, tutti plausibili; 3 verificati *verbatim* su PDF
  primario (Truax p.14, p.23; Risset p.37), gli altri su wiki.
- **Virgolettati senza pagina**: 6 — aggiungere il numero (5 disponibili da wiki,
  1 — Truax1990 — da verificare sul PDF).
- **Mancanti da aggiungere**: Vocem (fatto in `refs.bib`, da citare) + EC2 (da citare).
- **Difetti di rendering**: nessuno. Orphan refs non stampati.
- **Refuso di tracking**: titolo ValleLombardo2003 in bibliography.md.

Il dossier referenziale del brief (§4.3, Vocem foil; «frequenza convenzionale»
imprecisa) è **confermato** — dettaglio in `review_report.md` §5 e
`figure_walkthrough.md`.
