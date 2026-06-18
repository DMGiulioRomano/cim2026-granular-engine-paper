# [Valenti, Valle, Servetti, 2014] Permutation Synthesis

## Citazione CIM

Valenti, G., Valle, A., Servetti, A. (2014). Permutation Synthesis. In *Atti del XX Colloquio di Informatica Musicale*, pp. 35–40. Roma: AIMI.

## Categoria e lunghezza

Comunicazione orale — 6 pagine — 6 refs. Politecnico di Torino (Valenti + Servetti, Dip. Controllo e Calcolatori) + Università di Torino CIRMA-StudiUm (Valle).

## Argomento centrale

Introduce una tecnica sperimentale di sintesi digitale chiamata **permutation synthesis**: creazione di nuove forme d'onda spostando gruppi di campioni (*chunks*) di onde esistenti. Tecnica *time-based* che opera direttamente sulla forma d'onda discreta. Parametro principale: **permutation frequency** `fp` (inversamente proporzionale alla chunk length); risoluzione vincolata da `fs` con quantisation error definito formalmente. Implementazione SuperCollider plug-in con 3 UGens (`PermUGen`, `PermMod`, `PermModArray`). Posizionamento esplicito nella *non-standard synthesis* family (sez. 7).

## Sistema o strumento descritto

Plugin **SuperCollider** (Windows + Mac compilati, Linux portabile) distribuito via Quarks extension system. Tre UGens leggermente differenti che eseguono permutation synthesis. Pipeline base: array di campioni input → divisione in chunk di dimensione fissa → riordinamento secondo pattern → array output. Latency in real-time via doppio buffer (swap pattern: scrivi su `swapbuf1` secondo pattern, leggi `swapbuf2` sequenziale; al ciclo successivo si invertono).

## Analogia con PGE

**Anti-analogia tecnica esplicita formulata dagli autori contro la sintesi granulare** — citazione Roads *Microsound* in ref [1]. Tre vettori:

1. **Inversione del ruolo dell'envelope.** Quote sez. 1: «*Permutation synthesis is similar to a particular variant of granular synthesis, the so-called time-granulation [1]: here grains are taken from one or more existing files, an envelope is applied, and then the grains are reproduced over time. [...] However, most granulation approaches operate by applying an envelope, thus eliminating most of the discontinuities. Moreover, grains are typically scattered in time following some stochastic distributions. On the contrary, in permutation synthesis time discontinuities are the main feature, and the scrambling process is organised following a precise time-pattern.*» Granulare = envelope per **eliminare** discontinuità + scattering stocastico; permutation = **enfatizza** discontinuità + pattern deterministico. Anti-analogia di principio sul ruolo dei due meccanismi-cardine di PGE (`WindowGenerator` + `DistributionStrategy`).

2. **No stochastic distribution.** PGE: ogni grano è campionato da tendency mask (uniform/gaussian, indipendenza fra grani — cfr. [[tendency-mask]]). Permutation synthesis: pattern di riordinamento dichiarato esplicitamente dall'utente come parametro di sintesi, no stocasticità. Polo opposto sull'asse *controllo deterministico vs stocastico*; affianca [[silvestri2010]] (granulare deterministico CIM combinatorio) e [[discipio1991]] (granulare deterministico CIM caotico-iterativo) come **terza sotto-famiglia** del filone [[granulare-deterministico-cim]] — specificità: **deterministico ma a-causale** (no `xn+1=f(xn)`), pattern fissato a priori.

3. **Time-quantisation error formalizzato.** Sez. 2.2 introduce errore di quantizzazione temporale come duale del quantisation error di ampiezza: `chunk_size = fs/fp` arrotondato all'intero, errore (globally) crescente con `fp`, decrescente con `fs`. Pattern argomentativo trasferibile a sezione 3 paper PGE se si discute il rapporto fra rate di sintesi e risoluzione di `density`/`fill_factor`. In PGE l'analogo è la quantizzazione `IOT = 1/density` su grid di sample del renderer (Csound `kr` o NumPy chunk size).

**Continuità autoriale Valle CIM (11 anni).** Secondo paper CIM granular-related di Andrea Valle dopo [[valle-lombardo2003]] (GeoGraphy, *A Two-Level Method to Control Granular Synthesis*). Traiettoria 2003 → 2014: da architettura sistema formale CAC offline (GeoGraphy a due livelli con space actant) a tecnica DSP sperimentale real-time SC. Stesso autore CIM esplora due poli opposti del granulare (compositivo formale offline → DSP sperimentale real-time) — datapoint sulla varietà del granulare CIM italiano nella stessa autorialità.

## Posizionamento storico

**Non-standard synthesis** (sez. 7) — esplicitamente fuori dal paradigma signal elettronico, *"purely digital member of the modulation family"*. Lineage citato: granulare di Roads (ref [1]) + Computer Music Tutorial (ref [2]) + Miranda *Computer Sound Design* (ref [3]) + manuali SC (refs [4-6]). **Real-time** SuperCollider plugin. Datapoint CIM 2014 del *granulare-derivato non-stocastico*: insieme a CAGE (Agostini-Daubresse-Ghisi, granulazione simbolica) il volume CIM XX 2014 ospita **due paper esplicitamente posizionati rispetto al canone granulare ma fuori da esso** — segno che nel 2014 la sintesi granulare audio classica è abbastanza consolidata da generare ramificazioni e contro-tecniche referenziali.

## Note stilistiche

6 pagine, 6 refs (Roads *Microsound* + Roads CMT + Miranda + 3 manuali SC) — densità molto bassa (1 ref/pp.), giustificata dalla natura tecnica del paper (formule analitiche dominano l'argomento, non confronto con letteratura). Tono **tecnico-empirico**: formule (sez. 2-3-4-5), codice SC reale (sez. 6), figure 8 (steps di permutation, fp desired vs actual, time quantisation error, sonogramma esempio, diagramma modulazione-permutazione, etc.). Struttura accademica IMRAD-like: 1 introduzione/categoria → 2 design → 3-5 analisi (spettro/ampiezza) → 6 esempi → 7 conclusioni. Apertura comparativa col granulare (paragrafo p. 35), chiusura inviting user feedback. **Modello stilistico CIM per tool paper DSP**: 6 refs è il minimo assoluto per tool paper CIM XX. PGE paper deve restare sopra (target 9-21 ref) — è argomentativo, non tecnico-formale.

## Sezioni del paper CIM 2026 dove citare

Fonte non citata nel paper attuale; cfr. [[mappa-citazioni-paper]].

## Quote chiave

> *Permutation synthesis is similar to a particular variant of granular synthesis, the so-called time-granulation [1]: here grains are taken from one or more existing files, an envelope is applied, and then the grains are reproduced over time. If the source of the grain is a single audio stream, granulation results in scrambling parts of the same signal, which is the principle of permutation synthesis. However, most granulation approaches operate by applying an envelope, thus eliminating most of the discontinuities. Moreover, grains are typically scattered in time following some stochastic distributions. On the contrary, in permutation synthesis time discontinuities are the main feature, and the scrambling process is organised following a precise time-pattern.* (p. 35, sez. 1)

> *Permutation synthesis belongs to the family of non-standard synthesis technique. It does not refer to the electronic signal paradigm per se, rather it fully exploits the discrete nature of digital signals. It is a fairly simple method, indeed a purely digital member of the modulation family.* (p. 40, sez. 7 Conclusions)
