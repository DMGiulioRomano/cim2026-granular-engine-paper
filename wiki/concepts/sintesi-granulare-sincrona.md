# Sintesi granulare sincrona

## Definizione
Nel contesto De Poli/Piccialli (1988), la sintesi granulare sincrona e' una tecnica in cui la collocazione temporale dei grani e' agganciata al periodo del suono quasi periodico, invece che a una griglia di aggiornamento fissa o aleatoria. L'obiettivo e' preservare continuita' di fase e ridurre intermodulazioni indesiderate tra segnale e frequenza di aggiornamento.

Il modello studiato e' additivo e vicino alla sintesi per formanti: ogni zona dello spettro ha una propria sequenza di grani; ogni grano puo' essere interpretato come risposta all'impulso di un filtro FIR passa-banda a fase lineare.

## Distinzione terminologica
"Sincrono" puo' indicare cose diverse:

- In De Poli/Piccialli 1988: sincronizzazione dei grani con il periodo/pitch, per continuita' di fase nei suoni quasi periodici.
- In Truax e nel `DensityController` PGE: distribuzione temporale regolare dell'IOT rispetto a distribuzione casuale o blend, non necessariamente agganciata a un periodo estratto dal segnale.

Questa distinzione e' importante per evitare di sovrapporre due famiglie tecniche diverse.

## Rilevanza per PGE
PGE non implementa una sintesi granulare sincrona in senso De Poli/Piccialli. Il suo caso base e' la granulazione di campioni con posizione di lettura nel buffer, envelope parametrico e distribuzione IOT sincrona/asincrona in senso Truax.

Il confronto e' utile per delimitare PGE: il sistema non propone una teoria universale del grano, ma una postura compositiva situata. Dove De Poli/Piccialli risolvono qualita' del grano e coerenza formantica, PGE rende leggibile il processo sample-based attraverso DSL, partitura tempo-buffer e rendering differito.

## Fonti
- [De Poli & Piccialli 1988](../sources/papers/depolipiccialli1988.md) — modello principale: grani period-synchronous, FIR a fase lineare, controllo formantico
- [density-controller.md](../sources/pge/density-controller.md) — uso PGE del termine sincrono/asincrono per la distribuzione degli IOT, distinto dalla sincronia di periodo

## Sezioni del paper CIM 2026 dove citare
- Sezione 2: ramo CIM della sintesi granulare sincrona e distinzione rispetto a Truax/PGE
- Sezione 3: delimitazione di PGE come ambiente sample-based, non formantico period-synchronous
