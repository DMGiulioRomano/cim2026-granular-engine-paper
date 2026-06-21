# Mappa citazioni ↔ paper — fonte di verità

Unica fonte di verità per «dove citare» rispetto al paper reale
(`paper/paper.tex`, branch `paper-bottom-up`). I campi «Sezioni dove citare»
delle singole pagine wiki rinviano qui; in caso di conflitto vale questa
pagina, che a sua volta deriva dai `\cite{}` del sorgente.

Due parti: un **blocco meccanico** rigenerabile (`make cite-map`, marker
BEGIN/END — non editare a mano) e una **parte editoriale** (stati e funzioni,
mantenuta a mano con giudizio).

<!-- BEGIN cite-map -->

Generato da `make cite-map` su `paper/paper.tex` (con gli \input di `sections/` espansi; sha256 del sorgente espanso: `8341058b6099`). Non editare a mano questo blocco.

**Chiavi citate (21):** `Arcella2012`, `Bartetzki1997`, `DeTintis1995`, `DiScipio1991cim`, `DiScipio1995cim`, `DiScipioTisato1993cim`, `KellerRolfe1998`, `Lippe1993cim`, `Risset1999`, `Roads1978`, `Roads1985cim`, `Roads2001`, `Roads2021`, `RolfeKeller2000`, `Solomos2003`, `Sparano2018`, `Truax1988`, `Truax1988realtime`, `Truax1994`, `Vaggione1996`, `Vaggione2002`

| Blocco del paper | Chiavi citate (in ordine di apparizione) |
|---|---|
| Introduzione | `Roads1978`, `Lippe1993cim` |
| `sec:architettura` | `Roads2001`, `Truax1988realtime`, `DiScipioTisato1993cim` |
| `sec:c-e` | `Roads2001`, `KellerRolfe1998` |
| `sec:griglia` | `Truax1988`, `Lippe1993cim` |
| `sec:pointer` | `Lippe1993cim`, `Truax1988`, `Vaggione2002` |
| `sec:deviazione` | `Truax1988`, `Vaggione2002` |
| `sec:tradizione` | `Roads1978`, `Roads1985cim`, `DiScipioTisato1993cim`, `Lippe1993cim`, `Sparano2018`, `Roads2021`, `Truax1988`, `DeTintis1995`, `Bartetzki1997`, `RolfeKeller2000`, `Vaggione2002`, `DiScipio1991cim`, `Truax1994` |
| `sec:implicazioni` | `Risset1999`, `Solomos2003`, `Vaggione1996`, `DiScipio1995cim`, `Arcella2012` |

<!-- END cite-map -->

## Stati

- **citata** — la chiave compare nei `\cite{}` del paper attuale.
- **candidata `sec:partitura`** — shortlist per la sezione partitura ancora da
  scrivere (cfr. [[graphic-score]]); non ancora citata.
- **background** — nella knowledge base, non nel paper. Le pagine background
  portano la dicitura standard «fonte non citata nel paper attuale».

## Parte editoriale — funzioni per fonte (tetto: primaria + secondaria)

### Citate

| Chiave | Pagina wiki | Funzione primaria | Funzione secondaria |
|---|---|---|---|
| `Roads1978` | [[roads1978]] | (intro) + `sec:tradizione`: prima implementazione documentata, problema della specifica esplicita, pattern front-end→engine | — |
| `Roads1985cim` | [[roads1985]] | `sec:tradizione`: primo articolo CIM dedicato; formula il problema del controllo; quantifica la micro-deviazione | — |
| `Roads2001` | [[roads2001]] | `sec:c-e`: la finestratura come modulazione d'ampiezza — bande laterali spaziate all'inverso del periodo dell'inviluppo | — |
| `Lippe1993cim` | [[lippe1993]] | (intro/abstract) + `sec:pointer`: tassonomia *granular sampling*, posizione di lettura come asse dominante (p. 180) | `sec:tradizione`: snodo 1993 nello stesso volume; aspetto «ricorsivo» come parente real-time del workflow stem |
| `Truax1988` | [[truax1988]] | `sec:griglia` + `sec:deviazione`: modello sincrono/asincrono; tendency mask | `sec:tradizione`: genealogia; Fig. 4 come precursore della partitura (proposta 2) |
| `Truax1994` | [[truax1994]] | `sec:tradizione`: descrizione verbale del meccanismo della testina (proposta 2) | candidata `sec:partitura`: motivazione dell'asse Y |
| `DiScipioTisato1993cim` | [[discipio-tisato1993]] | `sec:architettura` (cappello): «single rule may instantiate multiple operations» | `sec:tradizione`: ultimo nodo offline, adozione tendency mask 1993 |
| `DiScipio1991cim` | [[discipio1991]] | `sec:tradizione`: famiglia di controllo caotica affiancata (contrasto controllato) | — |
| `DiScipio1995cim` | [[discipio1995]] | `sec:implicazioni`: interattività ≠ uscita udibile immediata, rifiutata «in questa stessa sede» trent'anni fa | — |
| `DeTintis1995` | [[detintis1995]] | `sec:tradizione`: tendency mask citata come stato dell'arte 1995 (terzo data-point) | — |
| `KellerRolfe1998` | [[keller-rolfe1998]] | `sec:c-e`: il profilo spettrale della finestra come parametro timbrico (*corner effect*) | — |
| `RolfeKeller2000` | [[rolfe-keller2000]] | `sec:tradizione`: decorrelazione come proprietà della massa granulare (ambito CIM) | — |
| `Vaggione2002` | [[vaggione2002]] | `sec:deviazione`: *décorrélation microtemporelle* (quarto angolo del 2×2) | `sec:tradizione`: piano compositivo della decorrelazione; montaggio multitraccia come parente del workflow stem |
| `Vaggione1996` | [[vaggione1996]] | `sec:implicazioni`: *déclaration d'attribut* généralisé; critica dei tassi come palliativi | — |
| `Solomos2003` | [[solomos2003]] | `sec:implicazioni`: triangolarità input/output/operatore (entretien 4, pp. 230–232) | — |
| `Risset1999` | [[risset1999]] | `sec:implicazioni`: precedente filosofico del ritorno volontario (p. 37) | — |
| `Arcella2012` | [[arcella-silvestri2012]] | `sec:implicazioni`: strumenti non neutri (p. 148) | — |
| `Sparano2018` | [[sparano2018]] | `sec:tradizione`: linea real-time CIM fino a GrainLab | — |
| `Roads2021` | [[roads2021]] | `sec:tradizione`: linea real-time fuori CIM (EC2) | candidata `sec:partitura`: Scan Display come polo di contrasto |
| `Bartetzki1997` | [[bartetzki1997]] | `sec:tradizione`: CMask come realizzazione compiuta del front-end dichiarativo; dimensiona la proposta 1 (gate) | — |

### Candidate `sec:partitura` (shortlist della sezione da scrivere)

| Pagina wiki | Ruolo previsto |
|---|---|
| [[truax1988]] Fig. 4 | precursore concreto: overlay multi-parametro come **input** (già citata altrove) |
| [[roads1978]] / [[roads1985]] polygon | piano tempo–frequenza come metafora, contro cui si definisce l'asse Y (già citate altrove) |
| [[caires2004]] | IRIN Timeline: partitura editabile come input — inversione di flusso |
| [[valle-lombardo2003]] | space actant come input di controllo — anti-analogia di flusso |
| [[lippe1993]] p. 180 | legittimazione dell'asse Y = posizione nel materiale (già citata altrove) |
| [[truax1994]] / [[truax2014]] | meccanismo della testina + correlato percettivo (*listening inside*) |

Dispensa completa della sezione: [[graphic-score]].

### Candidate posizionamento TENOR (non ancora citate)

Fonti TENOR per lo stato dell'arte dell'introduzione su due assi — notazione
(descrittivo/prescrittivo, mappa sinottica) e linguaggio/DSL (dichiarativo, IR
interrogabile, differito). Non ancora nei `\cite{}` del paper: quando entreranno,
rigenerare il blocco meccanico (`make cite-map`) e spostarle in «Citate».

| Pagina wiki | Ruolo previsto |
|---|---|
| [[frame2023]] | (intro) + `sec:partitura`: definizioni prescrittivo/descrittivo, descrittivo = log; ancora del nodo log↔mappa |
| [[bacon2022]] | `sec:partitura` + (intro): notazione↔cartografia, fonda «mappa sinottica»; poli non mutuamente esclusivi |
| [[hron2017]] | `sec:partitura` + (intro): collasso descrittivo/prescrittivo in un solo artefatto (Acousmographe) |
| [[fournier2016]] | (intro) + `sec:architettura`: partitura come modello dati interrogabile = parente della IR interrogabile |
| [[shapiro2023]] | (intro) + `sec:tradizione`: DSL esterno dichiarativo → MusicXML (contrasto fire-and-forget) |
| [[qiuichise2025]] | (intro) + `sec:tradizione`: dichiarativo + IR a grafo attraversata dalla compilazione (fratello più prossimo) |
| [[magnusson2015]] | (intro) + `sec:implicazioni`: code-score real-time, contrasto sull'asse del differimento |

### Background

Tutte le altre fonti della wiki. Restano knowledge base (anti-analogie,
data-point, modelli stilistici): non entrano nel paper attuale. Se una
riscrittura le promuove, aggiornare prima il paper, poi rigenerare il blocco
meccanico (`make cite-map`) e spostare la riga qui.

## Manutenzione

- Dopo ogni modifica ai `\cite{}` di `paper.tex`: `make cite-map` (rigenera il
  blocco fra i marker e aggiorna l'hash; la parte editoriale non viene toccata).
- Check di coerenza: ogni chiave del blocco meccanico deve avere una riga
  nella tabella «Citate»; nessuna riga «Citate» senza chiave nel blocco.
