# Mappa citazioni ↔ paper — fonte di verità

Unica fonte di verità per «dove citare» rispetto al paper consegnato
(`paper/xxv_cim_2026_pythongranularengine.tex` + `paper/sections/`). I campi
«Sezioni dove citare» delle singole pagine wiki rinviano qui; in caso di
conflitto vale questa pagina, che a sua volta deriva dai `\cite{}` del
sorgente.

Due parti: un **blocco meccanico** rigenerabile (`make cite-map`, marker
BEGIN/END, non editare a mano) e una **parte editoriale** (funzione di ogni
citazione nel testo, mantenuta a mano).

<!-- BEGIN cite-map -->

Generato da `make cite-map` su `paper/xxv_cim_2026_pythongranularengine.tex` (con gli \input di `sections/` espansi; sha256 del sorgente espanso: `b44fd45d7a39`). Non editare a mano questo blocco.

**Chiavi citate (17):** `Bartetzki1997`, `Blumlein1931`, `Caires2004`, `DeMattia2026Pge`, `DePoliPiccialli1988`, `DiScipioTisato1993cim`, `Dutilleux2016`, `Gerzon1975`, `Lippe1993cim`, `Roads1978`, `Roads1985cim`, `Roads2001`, `Roads2001Pulsars`, `Roads2021`, `Seeger1958`, `Truax1988`, `Vaggione2002`

| Blocco del paper | Chiavi citate (in ordine di apparizione) |
|---|---|
| Introduzione | `Roads1978`, `Truax1988`, `Bartetzki1997`, `Lippe1993cim`, `Roads2001` |
| `sec:architettura` | `DeMattia2026Pge`, `Seeger1958`, `Truax1988`, `Roads1978`, `Roads1985cim`, `Caires2004` |
| `sec:c-e` | `Roads2001` |
| `sec:griglia` | `Roads2001`, `DePoliPiccialli1988`, `Roads2001Pulsars` |
| `sec:deviazione` | `Truax1988`, `Bartetzki1997`, `DiScipioTisato1993cim`, `Roads2021`, `Vaggione2002` |
| `sec:dimensioni` | `Blumlein1931`, `Gerzon1975` |
| `sec:voci` | `Vaggione2002`, `Truax1988`, `Dutilleux2016` |
| `sec:conclusioni` | `Truax1988` |

<!-- END cite-map -->

## Stati

- **citata**: la chiave compare nei `\cite{}` del paper consegnato (17 chiavi).
- **background**: nella knowledge base, non nel paper. Le pagine background
  portano la dicitura «Non citata nel paper consegnato».

Le categorie precedenti («candidata `sec:partitura`», «tradizione» e
«implicazioni» come sezioni) non esistono più: il paper consegnato non ha una
sezione sulla partitura, né una sezione storica, né una sulle implicazioni.

## Parte editoriale: funzione di ogni citazione nel testo

| Chiave | Pagina wiki | Dove | Cosa sostiene nel paper |
|---|---|---|---|
| `Roads1978` | [[roads1978]] | introduzione; `sec:architettura` (nota MAP) | la specifica grano per grano diventa intrattabile oltre poche unità al secondo; i poligoni frequenza/tempo (p. 62) come precedente della MAP |
| `Roads1985cim` | [[roads1985]] | `sec:architettura` (nota MAP) | poligoni frequenza/tempo (p. 200), forma della nuvola |
| `Truax1988` | [[truax1988]] | introduzione; `sec:architettura` (nota MAP); `sec:deviazione`; `sec:voci`; `sec:conclusioni` | tendency mask; Fig. 4 (p. 24) e «inherently a visual control method» (p. 23); maschera (p. 17); oltre 50 ms i grani si separano (p. 18); controllo a più livelli (p. 25) |
| `Bartetzki1997` | [[bartetzki1997]] | introduzione; `sec:deviazione` | CMask: specifica testuale → event list; la maschera come mappatura fra estremi |
| `Lippe1993cim` | [[lippe1993]] | introduzione | *granular sampling*; posizione di lettura come parametro di prima classe |
| `Roads2001` | [[roads2001]] ([[roads2001-ch03-granular-synthesis]]) | introduzione; `sec:c-e`; `sec:griglia` | griglia sincrona / quasi-sincrona / asincrona (p. 93); bande laterali della finestratura (nota) |
| `DeMattia2026Pge` | — | `sec:architettura` (nota repository) | archivio Zenodo della versione di PGE usata per gli esempi |
| `Seeger1958` | — | `sec:architettura` | YAML notazione prescrittiva, MAP notazione descrittiva |
| `Caires2004` | [[caires2004]] | `sec:architettura` (nota MAP) | timeline di IRIN: eventi con il numero di traccia in ordinata |
| `DePoliPiccialli1988` | [[depoli-piccialli1988]] | `sec:griglia` (nota) | senso *pitch-synchronous*, distinto dal sincrono di Roads |
| `Roads2001Pulsars` | [[roads2001-pulsars]] | `sec:griglia` (didascalia) | spettro a righe a multipli della densità |
| `DiScipioTisato1993cim` | [[discipio-tisato1993]] | `sec:deviazione` | antecedente prossimo del gate (ICMS, probabilità fissa su switch discreti) |
| `Roads2021` | [[roads2021]] | `sec:deviazione` | *intermittency* di EC2: gate sull'emissione, non sulla deviazione |
| `Vaggione2002` | [[vaggione2002]] | `sec:deviazione`; `sec:voci` | jitter implicito come decorrelazione microtemporale; scarti di pochi ms fra voci come attributo spaziale |
| `Blumlein1931` | — | `sec:dimensioni` | codifica Mid-Side del pan |
| `Gerzon1975` | — | `sec:dimensioni` (nota) | mid e side come pickup a figura otto ortogonali |
| `Dutilleux2016` | [[dutilleux2016]] | `sec:voci` | ritardo intra-flusso e sincronicità inter-flusso come coppia canonica (`scatter`) |

### Background

Tutte le altre fonti della wiki, comprese quelle che versioni precedenti del
paper citavano (Truax 1994, Truax 2014, Di Scipio 1991 e 1995, De Tintis 1995,
Keller–Rolfe 1998, Rolfe–Keller 2000, Vaggione 1996, Solomos 2003, Risset
1999, Arcella–Silvestri 2012, Sparano 2018, le fonti TENOR). Se una
riscrittura le promuove, aggiornare prima il paper, poi rigenerare il blocco
meccanico (`make cite-map`) e aggiungere la riga qui.

## Manutenzione

- Dopo ogni modifica ai `\cite{}` del paper: `make cite-map` (rigenera il
  blocco fra i marker e aggiorna l'hash; la parte editoriale non viene
  toccata). Lo script ignora i commenti ed espande le note `\notaXxx` nel
  punto in cui sono richiamate.
- Check di coerenza: ogni chiave del blocco meccanico ha una riga nella
  tabella editoriale, e nessuna riga senza chiave nel blocco.
