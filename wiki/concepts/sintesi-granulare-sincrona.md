# Sintesi granulare sincrona

## Definizione
Nel contesto De Poli/Piccialli (1988, 1991), la sintesi granulare sincrona e' una tecnica in cui la collocazione temporale dei grani e' agganciata al periodo/pitch del suono quasi periodico, invece che a una griglia di aggiornamento fissa o aleatoria. L'obiettivo e' preservare continuita' di fase, ridurre intermodulazioni indesiderate tra segnale e frequenza di aggiornamento, e rendere indipendenti controllo temporale del pitch e controllo spettrale/formantico.

Il modello studiato e' additivo e vicino alla sintesi per formanti: ogni zona dello spettro ha una propria sequenza di grani; ogni grano puo' essere interpretato come risposta all'impulso di un filtro FIR passa-banda a fase lineare. Nel capitolo 1991 questa idea diventa un modello source-filter: un treno quasi periodico di impulsi determina la griglia temporale, mentre un filtro FIR tempo-variante e trasformazioni di prototype waveforms controllano inviluppo spettrale, formanti, ampiezza, frequenza centrale e larghezza di banda.

## Distinzione terminologica
"Sincrono" puo' indicare cose diverse:

- In De Poli/Piccialli 1988/1991: sincronizzazione dei grani con il periodo/pitch, per continuita' di fase e controllo formantico nei suoni quasi periodici.
- In Truax e nel `DensityController` PGE: distribuzione temporale regolare dell'IOT rispetto a distribuzione casuale o blend, non necessariamente agganciata a un periodo estratto dal segnale.

Questa distinzione e' importante per evitare di sovrapporre due famiglie tecniche diverse.

## Rilevanza per PGE
PGE non implementa una sintesi granulare sincrona in senso De Poli/Piccialli. Il suo caso base e' la granulazione di campioni con posizione di lettura nel buffer, envelope parametrico e distribuzione IOT sincrona/asincrona in senso Truax.

Il confronto e' utile per delimitare PGE: il sistema non propone una teoria universale del grano, ma una postura compositiva situata. Dove De Poli/Piccialli risolvono qualita' del grano e coerenza formantica, PGE rende leggibile il processo sample-based attraverso DSL, partitura tempo-buffer e rendering differito.

La differenza piu' netta e' nella griglia: nel modello pitch-synchronous la griglia dei grani dipende direttamente dal suono e dall'inizio dei periodi di pitch; in PGE la griglia e' una decisione compositiva espressa nel DSL, articolata dal `DensityController` e resa osservabile nella partitura grafica.

## Fonti
- [De Poli & Piccialli 1988](../sources/papers/depolipiccialli1988.md) — modello principale: grani period-synchronous, FIR a fase lineare, controllo formantico
- [De Poli & Piccialli 1991](../sources/papers/depolipiccialli1991.md) — formalizzazione source-filter: treno di impulsi quasi periodico, griglia dipendente dal pitch, prototype waveform transformations
- [density-controller.md](../sources/pge/density-controller.md) — uso PGE del termine sincrono/asincrono per la distribuzione degli IOT, distinto dalla sincronia di periodo

## Sezioni del paper CIM 2026 dove citare
- Sezione 2: ramo CIM della sintesi granulare sincrona e distinzione rispetto a Truax/PGE
- Sezione 3: delimitazione di PGE come ambiente sample-based, non formantico period-synchronous
