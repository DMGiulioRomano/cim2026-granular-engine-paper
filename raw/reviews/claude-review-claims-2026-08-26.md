# Review interna dei claim — Claude, 2026-08-26

**Chi l'ha scritta:** Claude (Opus 5), in sessione Claude Code su richiesta
dell'autore. **Non è una review della venue.** Le review dei revisori CIM stanno
in `cim2026-reviews-round1.md`; questo file è una lettura critica interna, fatta
assumendo la postura di un revisore ostile, per trovare le affermazioni
attaccabili prima che le trovi qualcun altro.

**Richiesta dell'autore (verbatim):** «Leggi attentamente tutto il paper e voglio
che mi dici se ci sono dei punti in cui è necessario inserire delle citazioni per
dare valenza a quello che sto dicendo che magari non è corroborata da fonti, devi
cercare di mettere nella condizione in cui un reviewer potrebbe contestare
qualcosa.»

## Stato del repository al momento della review

- **Commit base:** `4776f73` (2026-08-23, *docs(paper): apri sec:architettura su
  cio' che l'ambiente e', non su cio' da cui si discosta*), branch
  `fix/camera-ready-cim2026`.
- **Working tree sporco:** tre file portavano modifiche non committate.
  Il loro contenuto è poi confluito in:
  | File | Commit |
  |---|---|
  | `paper/sections/10-introduzione.tex` | `1078984` (2026-08-27) |
  | `paper/sections/27-voci.tex` | `c078fcd` (2026-08-27) |
  | `paper/sections/20-architettura.tex` | `1dd9a9b` (2026-08-26), insieme alla `\notaLineage` |

  Verificato il 2026-08-27 che le righe citate qui sotto corrispondono, con la
  stessa numerazione, alle versioni committate.
- **Submodule PGE:** `d6f4110` (v8.0.0 "Timeline Origin").
- **Stato del paper:** 7 pagine. **Abstract e conclusioni non erano ancora
  scritti** nella forma definitiva. L'autore lo ha precisato dopo la consegna
  della review, quindi i punti A1, A2 e parte di E vanno letti sapendo che
  riguardano testo provvisorio.

---

## A. Claim di novità e di confronto

### A1 — Conclusioni: «analisi, debugging e documentazione che altri sistemi non offrono in modo nativo»
`50-conclusioni.tex:9-10`. Claim comparativo su un campo intero, senza un nome né
una citazione. Il reviewer risponde con EmissionControl2 (`Roads2021`,
visualizzazione e controllo per-grano, in bibliografia e mai citato), IRIN
(`Caires2004`), GrainLab (`Sparano2018`), `ValleLombardo2003`. Serve un confronto
con sistemi nominati e citati, oppure la ritirata a un claim circoscritto.

### A2 — Abstract: «Existing declarative environments … are not built to make the generated grain population inspectable»
`00-abstract.tex:3-6`. Stessa struttura, in prima pagina. SuperCollider è nominato
senza riferimento. L'affermazione è falsificabile: EC2 mostra i grani, CMask
produce una score Csound ispezionabile.

### A3 — Il gate probabilistico non è mai rivendicato né difeso
`24-deviazione.tex:103`, «L'estensione di questo modello introduce il gate
probabilistico $g_n$». Manca la formula di priorità con hedge e mancano i
precursori con la differenza. Senza, il verdetto probabile è «contributo già
disponibile altrove». È il punto su cui il paper vive o muore.

### A4 — La `\textsc{map}` è descritta senza un solo precursore
`20-architettura.tex:88-107`. Il lineage completo esiste in
`wiki/concepts/graphic-score.md` e il paper ne usa zero.

### A5 — Contraddizione interna su «riproducibile»
Abstract «versionable, reproducible specification» e `20-architettura.tex:68`
«la riproducibilità … del processo compositivo», contro `27-voci.tex:64-66`
«cambia a ogni esecuzione».

## B. Attribuzioni contestabili

1. **`10-introduzione.tex:6-8` e `24-deviazione.tex:88`: la *tendency mask*
   attribuita a Truax.** Il concetto è di G. M. Koenig (PROJECT2/SSP); Truax lo
   implementa nel GSX, Bartetzki lo diffonde con CMask.
2. **Le due equazioni sono dell'autore, non di Truax.** `eq:tendency_mask`
   (`24-deviazione.tex:92`) si legge come sua; `eq:iot` (`23-griglia.tex:25`)
   dice almeno «derivata dalla descrizione». Chi controlla Truax 1988 non trova
   né l'una né l'altra. Servono «riformulazione mia» e numero di pagina.
3. **`10-introduzione.tex:41`: *granular sampling* attribuito a `Lippe1993cim`.**
   Il termine circola prima; aggiungere `Truax1990`.
4. **`10-introduzione.tex:3-4`: «La prima sintesi granulare al calcolatore».**
   Contestabile: Xenakis, *Analogique B* (1959), e `Arcella2012` è in bibliografia.
5. **`23-griglia.tex:9`: sincrono/asincrono «nel senso di Truax».** La
   tripartizione è canonicamente di Roads (`Roads1988`, `Roads2001`).

## C. Claim tecnici senza evidenza

1. **`\notaRepo` (`20-architettura.tex:26-27`): «Il costo di calcolo non cresce
   con la durata d'ascolto ma col numero di grani».** Zero misure.
2. **`\notaBande` (`20-architettura.tex:39-43`): «−74 dB, sotto la soglia
   udibile».** Manca la procedura di misura e manca la fonte per la soglia.
3. **`25-esempio_di_mezzo.tex:8-14`: Mid-Side → perifonia → ambisonics.** Il
   punto più fragile sul piano tecnico: M/S a due canali corrisponde a $W$ più
   una sola componente orizzontale.
4. **`27-voci.tex:23-26`: «Sotto la soglia dei pochi millisecondi».** Soglia vaga
   e sbagliata per difetto; `Vaggione2002` non sostiene il valore numerico.
5. **`27-voci.tex:27-29`: «fino a diciotto voci» in `Truax1994`.** Verificare sul
   PDF e mettere la pagina.
6. **`23-griglia.tex` caption:52-56: «spettro a righe spaziate a multipli della
   densità».** Vero e classico, quindi facile da citare (`DePoliPiccialli1991`,
   `Roads2001`).
7. **`10-introduzione.tex:18-19`: «il file audio non consente di risalire ai
   parametri».** Assoluto: l'analisi spettrale ne recupera una parte.

## D. Riferimenti già in bibliografia, mai citati

`Seeger1958` (prescrittivo/descrittivo, la coppia che il paper mette in scena
senza nominarla); il blocco TENOR `Magnusson2015tenor`, `Shapiro2023tenor`,
`QiuIchise2025tenor`, `Bacon2022tenor`, mentre il primo contributo del paper è
«la specifica è notazione»; `RolfeKeller2000`, che sostiene direttamente la frase
di `24-deviazione.tex:152-154`; la tradizione CIM (`Sparano2018`, `DeTintis1995`,
`ValleLombardo2003`, `DiScipioTisato1993cim`, `Lopez1998`), zero citazioni ai
precedenti granulari della venue in cui si sottomette; `Truax1994`, da citare
anche in `sec:pointer`.

## E. Placeholder da chiudere

`20-architettura.tex:24` «github METTERE LINK» e `:52` «[URL]»;
`:49` `\notaClaude{DA SCRIVERE}`, agganciata a un claim non banale; `:31` link OSF
ancora *view-only* anonimo; `24-deviazione.tex:38-40` TODO aperti;
`paper.tex:34` `\blfootnote` del copyright commentato e `\input` dell'abstract
duplicato.

**Priorità dichiarata nella review:** A1/A2 (claim comparativo), A3 (difesa del
gate), B1 (attribuzione della tendency mask).

---

## Stato successivo (aggiornato 2026-08-27)

Cosa è stato trattato dopo la review, nella stessa sessione:

| Punto | Esito | Commit |
|---|---|---|
| A3 | Paragrafo di dimensionamento dopo `eq:gated`: rivendicazione ristretta a «asse dichiarabile e componibile nel tempo», precursori ICMS e EC2 nominati | `9450c22` |
| A4 | `\notaLineage` alla prima occorrenza di `\textsc{map}`: Truax 1988, Roads 1978/1985, Caires 2004 | `1dd9a9b` |
| A5 | Ribaltato: il seeding esiste, si rivendica invece di attenuarlo | `8eab58c` |
| A1, A2 | Sospesi: si chiudono scrivendo abstract e conclusioni | — |
| B, C, D, E | Aperti | — |

**Scadenza (decisione dell'autore, 2026-08-27): tutti i punti aperti vanno
chiusi entro il 31 agosto 2026**, data di consegna della camera-ready. Aggiornare
questa tabella a ogni punto chiuso, col commit. Ordine di lavorazione
consigliato: E (placeholder, costo zero), B (attribuzioni: rischio alto e costo
basso), D (citazioni già in bibliografia), C (richiede misure o riformulazioni),
A1/A2 insieme alla scrittura di abstract e conclusioni. Vincolo: il paper è a 8
pagine, che è il tetto CIM, quindi ogni aggiunta va compensata con un taglio.

**Due errori della review stessa, emersi verificando le fonti.**

1. **A4 conteneva una lettura sbagliata di EC2.** La review sosteneva che lo Scan
   Display di EmissionControl2 plottasse i grani sull'asse della posizione di
   lettura, e quindi che il differenziatore «asse Y = posizione di lettura» non
   fosse esclusivo. La didascalia della Fig. 3 dice altro: è la forma d'onda del
   file disegnata orizzontalmente con dei marker sopra, quindi un asse solo e
   nessun asse per il tempo dello stream. Segnalato dall'autore, verificato sul
   PDF, EC2 escluso dalla nota. Il differenziatore corretto è *cosa è plottato*
   sul piano, non l'asse Y da solo.
2. **La review dava per mancante una precisazione che c'era già.** Sosteneva che
   `wiki/concepts/deviazione-ampiezza-probabilita.md` non dicesse che la
   probabilità degli switch ICMS è fissa. Lo diceva.

**Un errore vero trovato solo lavorando su A5.** Il residuo RMS gain-matched
dell'esempio `identity` misura **−38,1 dB**, non i −74 dB di `\notaBande`
(punto C2, che chiedeva la procedura di misura senza sospettare che il valore
fosse sbagliato). Verificato che non è artefatto della misura: lag ottimo di
allineamento 0, indipendente dal seed, e a 44100 senza ricampionamento peggiora
a −21,1 dB. Da decidere se è una regressione di PGE o una frase da rifare.

**Nota sul metodo, valida oltre questo file.** La lacuna su EC2 nel registro di
non-precedenza del gate era di una specie ricorrente: EC2 era già ingestito nel
wiki e già censito per lo Scan Display, ma non era mai stato interrogato *come
candidato-controesempio del gate*. Una fonte ingestita per un contributo non è
verificata per gli altri.
