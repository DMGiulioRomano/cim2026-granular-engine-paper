# [Roads, 1978] Automated Granular Synthesis of Sound

## Citazione CIM
Roads, C. (1978). Automated Granular Synthesis of Sound. *Computer Music Journal*, 2(2), 61–62.

## Argomento centrale
Note informali su **AGS** (Automated Granular Synthesis), il primo sistema software
documentato di sintesi granulare al computer, sviluppato da Roads a inizio 1975
in B6700 Extended ALGOL come *front-end processor* per MUSIC V. Il paper
descrive (a) l'unità grano con inviluppo gaussiano modificato, (b) un livello
superiore di organizzazione chiamato *event* parametrizzato da 6 coppie
valore/slope, (c) una notazione grafica come polygon su piano frequenza/tempo.
È il primo paper su CMJ a presentare un'implementazione concreta dopo le
fondazioni teoriche Gabor → Xenakis.

## Gap o problema identificato
Roads dichiara esplicitamente: *"there appears to be no literature describing
the technique"* (p. 61). Il paper colma questo vuoto bibliografico con note
informali su un sistema funzionante.

Gap implicito (poi reso esplicito da Truax 1990): l'event a 6 coppie
valore/slope assume che parametri come `bandwidth` o `density` evolvano
linearmente. Roads non discute il problema della percezione del risultato
date queste rampe. Il sistema è descritto come efficace ("accessible user
interface — just a few simple parameters") senza interrogare la corrispondenza
tra specifica parametrica e risultato percettivo.

In chiusura indica due direzioni aperte: (a) committere il calcolo grano a
hardware dedicato (anticipa Truax/DMX-1000 1988); (b) la notazione grafica
come *polygon arbitrario* su piano freq/tempo, più libera dei rettangoli di
Stockhausen *Studie II*.

## Rilevanza diretta per PGE
Quadruplo legame, tutti più antichi di Roads 1988:

1. **Pattern *front-end processor → engine sintesi* = pattern PGE.**
   AGS calcola le note records di grano partendo da specifiche di alto livello,
   poi le passa a MUSIC V che fa il calcolo audio. PGE applica lo stesso
   pattern: il generatore Python (`generator.py`) compila il DSL YAML in `.sco`
   Csound (oppure direttamente in samples via NumpyAudioRenderer). Roads 1978
   è il primo esempio documentato dell'architettura *deferred-time + linguaggio
   compositivo separato dall'engine audio* che PGE eredita.

2. **Event a 6 coppie valore/slope = primo precursore del DSL YAML.**
   Roads 1978 introduce 6 parametri con rampa lineare iniziale → finale
   (waveform, center freq, bandwidth, density, amplitude — ognuno con il suo
   *rate-of-change*). Roads 1988 espanderà a 12 parametri (separando initial
   da slope). PGE generalizza ulteriormente con `Envelope` (breakpoint con
   forma arbitraria) ma il principio è già qui nel 1978: ogni parametro
   evolve nel tempo come funzione, non come scalare.

3. **Notazione grafica come polygon su piano freq/tempo = precursore esplicito
   del score_visualizer.** *"This granular synthesis system can model any
   polygon inscribed on the frequency-vs-time plane"* (p. 62). Roads 1978
   anticipa di dieci anni la frase analoga in Roads 1988. Il piano è
   freq/tempo; PGE conserva l'idea di forme inscritte (envelope come polygon)
   ma sostituisce l'asse Y con posizione-nel-buffer per il caso d'uso
   granulazione di campioni.

4. **Inviluppo grano gaussiano modificato.** Roads (1978) si discosta
   esplicitamente dalla gaussiana pura di Xenakis: *"this one more clearly
   articulates the grain with its greater effective amplitude, while retaining
   the smooth rise and decay slopes of the Gaussian curve"*. Inviluppo con
   attacco gaussiano + sustained peak + decay gaussiano. PGE rende l'envelope
   del grano configurabile (`window_controller`), riconoscendo già nel 1978
   che la scelta di finestra è una decisione musicale, non una costante.

Confronto storico chiave: AGS 1975 era limitato a **32 grani simultanei** e
**16-bit / 12-bit DAC output**. PGE non ha limiti pratici sul numero di grani
simultanei (deferred-time, output 32-bit float). Il vincolo hardware del 1975
giustifica il framing "few simple parameters" — Roads doveva ridurre l'input
per gestibilità computazionale; PGE riduce l'input per **leggibilità
compositiva**, non per limiti di calcolo.

## Collegamento alla tesi centrale
Roads 1978 stabilisce due punti che il paper CIM 2026 può citare come *origine*
della linea di pensiero a cui PGE risponde:

- *"The strength of granular synthesis lies in its accessible user interface —
  just a few simple parameters — and its ability to focus computational power
  to accurately realize graphic scores"* (p. 62). Questa è la tesi che PGE
  riprende esplicitamente: il potere espressivo del paradigma granulare
  dipende dalla qualità dell'interfaccia di controllo. Il gap
  controllo/percezione (esplicitato da Truax 1990) è già implicitamente la
  preoccupazione di Roads quando enfatizza l'accessibilità.

- L'esistenza stessa di un livello *event* sopra il grano è la prima risposta
  pratica al problema "governare migliaia di grani senza astrazioni
  intermedie è ingestibile". PGE eredita questa risposta e la estende: dove
  Roads 1978 ha 6 coppie valore/slope, PGE ha `Envelope` arbitrari +
  multi-voice + strategie di dephase + cache incrementale.

In sezione 1 del paper CIM 2026, Roads 1978 è la fonte canonica per il claim
"il problema del controllo è centrale fin dalla prima implementazione computer
della tecnica". In sezione 2, è il primo lavoro nella linea Roads-Truax che
PGE prosegue.

## Sezioni del paper CIM 2026 dove citare
- **Sezione 1 — Problema:** "no literature describing the technique" (1978)
  come riferimento al ritardo storico tra teoria Gabor (1947) e prima
  implementazione computer (AGS 1975). L'enfasi di Roads su *accessible user
  interface* come ancora del problema controllo/percezione.
- **Sezione 2 — Contesto teorico:** prima implementazione documentata della
  tradizione granulare; pattern event-sopra-grano come radice del DSL
  parametrico.
- **Sezione 3 — Architettura:** AGS come front-end MUSIC V → PGE come
  front-end Csound/NumPy. Stesso pattern architetturale a 47 anni di distanza.
- **Sezione 4 — Partitura grafica:** *"any polygon inscribed on the
  frequency-vs-time plane"* come precedente esplicito (più antico di Roads
  1988) della visualizzazione cartesiana di eventi granulari. Riferimento a
  Stockhausen *Studie II* come analogia notazionale.

## Quote chiave

> "Thirty years ago, Dr. Dennis Gabor [...] made the first allusions to a
> granular approach to the synthesis of sound. [...] Iannis Xenakis was the
> first to explicate a compositional theory for grains of sound in his 1971
> book, *Formalized Music*. Since then, I've heard of a number of experiments
> with granular synthesis, but there appears to be no literature describing
> the technique." (p. 61)

> "By specifying several parameters at a higher level, a composer can call for
> the automatic computation of thousands of grains. The composer works with
> units called *events*, which are characterized by the parameters: (1)
> Beginning time and duration of an event (2) Initial waveform and waveform
> rate-of-change (slope) (3) Initial center frequency and rate-of-change of
> center frequency (4) Initial bandwidth (frequency dispersion) and bandwidth
> rate-of-change (5) Initial grain density and grain density rate-of-change
> (6) Initial amplitude and amplitude rate-of-change." (p. 61)

> "The sounds produced by granular synthesis can be represented by a graphic
> notation similar to that used for Stockhausen's *Studie II*. However, it is
> freer, since Stockhausen's composition uses rectangles to describe sonic
> events while this granular synthesis system can model any polygon inscribed
> on the frequency-vs-time plane." (p. 62)

> "The strength of granular synthesis lies in its accessible user interface —
> just a few simple parameters — and its ability to focus computational power
> to accurately realize graphic scores of the type described above." (p. 62)
