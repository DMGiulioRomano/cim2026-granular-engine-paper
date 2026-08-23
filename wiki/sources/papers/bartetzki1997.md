# [Bartetzki, 1997] Csound Score Generation and Granular Synthesis with CMask

## Citazione CIM
Bartetzki, A. (1997). Csound Score Generation and Granular Synthesis with CMask.
Articolo online (marzo 1997) e manuale (luglio 1997), STEAM — Studio für
elektroakustische Musik, Hochschule für Musik «Hanns Eisler» Berlin (studio
fondato e diretto da Bartetzki fino al 2002; la byline dell'articolo riporta
solo «Hochschule für Musik, Berlin», nome autore senza accento).
URL canonico: https://abartetzki.users.ak.tu-berlin.de/CMaskPaper/cmask-article.html
(consultato via snapshot Wayback 2024-08-04; manuale: snapshot 2021-05-13).
Fonte web HTML, non PDF — snapshot in `raw/papers/Bartetzki_1997_*.{html,txt}` (gitignored).

## Argomento centrale
CMask è un generatore stocastico di score Csound in tempo differito: un file di
parametri testuale descrive, campo per campo (`p1…pn`), come generare migliaia di
eventi/grani. Architettura a due stadi per ogni campo: un **generatore** di numeri
(costante, lista ciclica, funzione a segmenti, generatore casuale con distribuzione,
oscillatore) seguito da **modificatori** opzionali (maschera di tendenza, quantizer,
accumulatore/random walk). La maschera di tendenza è il concetto fondante: il
generatore casuale produce valori in {0,1} che vengono mappati linearmente nell'area
delimitata da due bordi tempo-varianti, ciascuno descritto da breakpoint illimitati
con interpolazione configurabile. La seconda parte dell'articolo applica il modello
alla granulazione di file audio (puntatore di lettura come campo dello score,
time-stretching via fattore di overlap, trasposizione per-grano).

## Gap o problema identificato
L'articolo è un tutorial-manifesto, non un paper problematizzante: il problema
implicito è il controllo globale di migliaia di eventi («functions for the global
controlling of thousands of score events») che la scrittura manuale dello score
Csound non consente. Non discute notazione visiva né workflow di riascolto: l'output
è lo score, la verifica è l'ascolto del rendering Csound.

## Rilevanza diretta per PGE
È il precursore più compiuto del **front-end dichiarativo per granulazione in tempo
differito** (testo → score → Csound), nominato come tale in «tradizione» (sezione rimossa, confluita in `sec:conclusioni`) del
paper: maschere di tendenza per ogni campo dello score, bordi mossi nel tempo da
funzioni a segmenti, Csound in uscita. Tre punti di contatto e una distinzione:

1. **Stesso modo operativo** (deferred, specifica testuale, engine separato) e
   stessa unità di organizzazione temporale: in CMask il `p2` è trattato come
   intervallo fra eventi successivi (l'inter-onset time della griglia temporale di
   PGE), e il *field* raggruppa eventi che condividono le stesse maschere per un
   intervallo di tempo (parente della dichiarazione di stream).
2. **Granulazione di campioni come applicazione principale**: puntatore di lettura
   nel file (`p4` in secondi sulla ftable), time-stretching via overlap, fattore di
   trasposizione per-grano — gli stessi assi che PGE espone come posizione di
   lettura, densità e trasposizione.
3. **Nel modello CMask il valore è sempre estratto dalla maschera**: ogni evento
   passa per il mapping {0,1}→bordi. Non esiste un parametro che decida *se* la
   deviazione si applichi al singolo evento.
4. **Il quantizer ha una `strength` continua, non un gate**: tre parametri
   (intervallo, offset, strength), tutti envelope-abili; la strength è
   un'**attrazione parziale applicata a ogni valore** (a 0.5 ogni valore percorre
   metà della distanza verso il punto di griglia più vicino), non una probabilità
   per-evento di applicazione. È il candidato-controesempio più vicino alla
   fattorizzazione ampiezza×probabilità di PGE, e la distinzione — blend continuo
   vs gate Bernoulli per-grano — è esattamente il dimensionamento della proposta 1
   (cfr. [[deviazione-ampiezza-probabilita]]).

## Collegamento alla tesi centrale
Dimensiona la prima proposta del paper: il pattern front-end dichiarativo → engine
non è nuovo (CMask lo realizza compiutamente nel 1997, su lineage Koenig/Truax POD
dichiarato in bibliografia); ciò che CMask non ha è il secondo asse della deviazione
— il gate di probabilità per-grano componibile come envelope. Conferma inoltre che
la granulazione di campioni in tempo differito via score generation era pratica
documentata e insegnabile già nel 1997: il ritorno volontario di PGE al differito
non reinventa il modo operativo, ne riprende uno maturo.

## Sezioni del paper CIM 2026 dove citare
- **non citato nel paper** («tradizione», sezione rimossa e confluita in `sec:conclusioni`): realizzazione compiuta del front-end dichiarativo
  per score granulari; riferimento già presente nel testo per circoscrivere la
  proposta 1.
- **`sec:deviazione`** (secondaria, eventuale): se serve ancorare nel corpo la
  distinzione fra strength continua del quantizer e gate di probabilità — di norma
  basta il rinvio in «tradizione» (sezione rimossa, confluita in `sec:conclusioni`).

## Quote chiave
- «The program CMask is intended as a handy tool for composers. It provides the
  Csound user with functions for the global controlling of thousands of score
  events.» (incipit)
- «Every random generator in CMask is limited to the range {0,1}. In the next score
  generation stage the numbers within this range will be mapped to a new range
  required for real Csound note pfields [...] This is done by tendency masks.»
  (sez. I, *Basics*)
- «The grey moduls are modifier: tendency mask, quantizer and accumulator. QUANT
  and ACCUM are optional, they can be bypassed.» (sez. I, schema del processo)
- «Three dynamical parameters determine this quantization: the quantization
  interval, the offset and the strength. [...] The strength is a kind of
  attraction. 0% means no quantization at all. 50% means that every random number
  is attracted to the half distance between this random value and the next grid
  value. 100% means that all numbers go to their next grid point. The strength and
  the other quantization parameters can be given as a constant or as a segment
  function.» (sez. *Quantization*)
- «Granulation is the term for cutting a sound into small pieces - the grains.
  Their duration is normally very short: about 5 to 50 msecs.» (sez. II, *Sound
  file granulation*)
