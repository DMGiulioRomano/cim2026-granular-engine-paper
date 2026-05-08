# [De Poli & Piccialli, 1988] Forme d'onda per la sintesi granulare sincrona

## Citazione CIM
De Poli, G., & Piccialli, A. (1988). Forme d'onda per la sintesi granulare sincrona. In *Atti del VII Colloquio di Informatica Musicale* (pp. 70-74). Roma: Associazione Musica Verticale.

Nota: il PDF include anche una pagina di figure a p. 75.

## Argomento centrale
Il paper studia una variante di sintesi granulare additiva sincrona con il periodo, pensata per suoni quasi periodici e per un controllo percettivamente significativo dell'inviluppo spettrale. La proposta tratta ogni sequenza di grani come una zona/formante dello spettro: ogni grano e' la risposta all'impulso di un filtro FIR passa-banda a fase lineare, tabulato per efficienza e trasformato dinamicamente per controllare frequenza, ampiezza, larghezza di banda e forma.

Il contributo non e' una piattaforma compositiva generale, ma un modello di progettazione delle forme d'onda del grano. La sintesi granulare viene riletta attraverso la sintesi per formanti: meno attenzione alla distribuzione stocastica di masse sonore, piu' attenzione a continuita' di fase, qualita' del timbro e controllo indipendente delle regioni dello spettro.

## Gap o problema identificato
De Poli e Piccialli individuano tre problemi nelle proposte precedenti:

1. L'uso di piccole porzioni di suoni reali conserva bene il carattere della sorgente ma richiede molti grani diversi e rende difficile il controllo compositivo delle caratteristiche globali.
2. La collocazione asincrona dei grani a intervalli fissi, tipicamente 10-20 ms, crea problemi nei suoni quasi periodici: manca la continuita' di fase tra grani consecutivi e si produce intermodulazione tra segnale e frequenza di aggiornamento.
3. I metodi additivi di sintesi per formanti discussi dagli autori non garantiscono linearita' di fase; nella somma di piu' grani/formanti possono quindi apparire cancellazioni e interferenze indesiderate.

La soluzione proposta e' sincronizzare la collocazione temporale dei grani con il periodo e usare forme d'onda derivate da filtri FIR a fase lineare, cosi' da sommare componenti/formanti senza problemi di fase.

## Rilevanza diretta per PGE
La rilevanza per PGE e' soprattutto di delimitazione storica e tecnica.

1. **Ramo CIM complementare alla linea Roads/Truax.** Nel 1988, accanto alla svolta real-time di Truax e al vocabolario generale di Roads, De Poli e Piccialli documentano un ramo italiano orientato alla qualita' del singolo grano e alla sintesi formantica. Il problema centrale non e' il controllo di cloud stocastici, ma la costruzione di grani coerenti per suoni quasi periodici.

2. **"Sincrono" qui non significa la stessa cosa del `DensityController` PGE.** In PGE la distribuzione sincrona/asincrona derivata da Truax riguarda l'IOT: grani metrici vs random/blend. In De Poli e Piccialli la sincronia e' invece agganciata al periodo del segnale/quasi-pitch, con l'obiettivo di continuita' di fase. Questa distinzione evita un falso parallelo terminologico.

3. **Grano come risposta di filtro vs grano come lettura di buffer.** PGE e' centrato sulla granulazione di campioni: la domanda compositiva diventa "da dove nel buffer viene letto il grano?", da cui l'asse Y della partitura. De Poli e Piccialli lavorano invece sulla forma d'onda prototipo del grano, progettata come risposta FIR lineare. La loro visualizzazione e' spettrale/formantica, non una partitura tempo-buffer.

4. **Controllo percettivo come terreno comune.** Il desiderio di definire l'evoluzione sonora in termini di inviluppo spettrale e formanti anticipa la stessa esigenza generale che PGE affronta via DSL parametrico: evitare che il compositore lavori solo su valori tecnici grezzi. PGE pero' sposta il problema dal design del grano alla leggibilita' del processo generativo completo.

## Collegamento alla tesi centrale
De Poli e Piccialli 1988 rafforzano la tesi non per analogia diretta, ma per contrasto. Mostrano che, nella tradizione CIM, la sintesi granulare non e' un unico percorso lineare verso il real-time: e' un campo di problemi tecnici e compositivi separabili. Nel loro caso il problema e' la qualita' del grano e la coerenza di fase nei suoni quasi periodici; nel caso PGE il problema e' abitare un grande spazio parametrico di granulazione di campioni, dove la relazione tra specifica, partitura e ascolto richiede il loop lungo.

Questo aiuta a non presentare PGE come "migliore" o piu' generale. PGE sceglie un sottoinsieme situato del paradigma granulare: tempo differito, sample-based granulation, controllo parametrico ad alto livello, lettura retroattiva tramite partitura. De Poli e Piccialli ricordano che altre scelte legittime portano altrove: verso grani progettati come filtri, sincronia di periodo e controllo formantico.

## Sezioni del paper CIM 2026 dove citare
- Sezione 2 (Sintesi granulare: dal paradigma Gabor al controllo gerarchico): ramo CIM della sintesi granulare sincrona; distinzione tra granulazione stocastica/asincrona e period-synchronous granular synthesis
- Sezione 3 (PGE: architettura per l'indagine parametrica): nota di delimitazione tecnica — PGE non e' un motore di sintesi formantica sincrona, ma un ambiente sample-based con DSL e renderer differiti

## Quote chiave
- "termini percettivamente significativi" (p. 71)
- "sincrono con il periodo" (p. 71)
- "filtri FIR a fase lineare" (p. 72)
