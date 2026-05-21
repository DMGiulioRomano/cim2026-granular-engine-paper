# [De Poli, Piccialli, 1988] Forme d'onda per la sintesi granulare sincrona

## Citazione CIM
De Poli, G., Piccialli, A. (1988). Forme d'onda per la sintesi granulare sincrona. In *Atti del VII Colloquio di Informatica Musicale*, pp. 69–73. Cagliari. (Pagina di figure a p. 75.)

## Categoria e lunghezza
Comunicazione orale (Sessione "Elaborazione numerica del suono") — 5 pp. — 9 riferimenti bibliografici.

## Argomento centrale
Studio sistematico delle forme d'onda ottimali per sintesi granulare **sincrona con il periodo** (pitch-synchronous). Propone forme d'onda derivate da filtri FIR a fase lineare passa-banda, ottenute trasformando dinamicamente prototipi passa-basso (gaussiana, secante iperbolica, finestre di Nuttall/Gegenbauer/Kaiser/Dolph-Chebyshev) per controllare indipendentemente frequenza, ampiezza, larghezza di banda e forma di ciascun formante. Rilettura della sintesi granulare attraverso la sintesi per formanti: ogni sequenza di grani tratta come zona/formante dello spettro, ogni grano è la risposta all'impulso di un filtro FIR.

Il contributo non è una piattaforma compositiva generale, ma un **modello di progettazione delle forme d'onda del grano**. Meno attenzione alla distribuzione stocastica di masse sonore, più attenzione a continuità di fase, qualità del timbro e controllo indipendente delle regioni dello spettro.

## Gap o problema identificato
Tre problemi nelle proposte precedenti:

1. L'uso di piccole porzioni di suoni reali conserva il carattere della sorgente ma richiede molti grani diversi e rende difficile il controllo compositivo globale.
2. La collocazione asincrona dei grani a intervalli fissi (10–20 ms) crea problemi nei suoni quasi periodici: manca la continuità di fase tra grani consecutivi e si produce intermodulazione tra segnale e frequenza di aggiornamento.
3. I metodi additivi di sintesi per formanti esaminati (VOSIM, Rodet, Liénard) non garantiscono linearità di fase; la somma di più grani/formanti produce cancellazioni e interferenze indesiderate.

**Soluzione proposta:** sincronizzazione col periodo + forme d'onda derivate da filtri FIR a fase lineare, così da sommare componenti/formanti senza problemi di fase.

## Sistema o strumento descritto
Modello teorico/algoritmico — non riportato sistema software specifico. Riferimento implementativo: tabulazione del prototipo (precompute) e lettura con passo non unitario (scaling per bandwidth, traslazione in frequenza per posizione del formante). Tecniche di trasformazione: lettura a passo non costante, modulazione d'ampiezza, distorsione non-lineare. **Offline** (implicito: studio di forme d'onda, non sistema real-time).

## Rilevanza diretta per PGE
Rilevanza soprattutto **di delimitazione storica e tecnica**, più alcuni pattern strutturali condivisi.

1. **Ramo CIM complementare alla linea Roads/Truax.** Nel 1988, accanto alla svolta real-time di Truax (DMX-1000, ICMC) e al vocabolario generale di Roads, De Poli/Piccialli documentano un ramo italiano orientato alla qualità del singolo grano e alla sintesi formantica. Problema centrale: costruzione di grani coerenti per suoni quasi periodici, non controllo di cloud stocastici.

2. **"Sincrono" qui ≠ `DensityController` PGE.** In PGE la distribuzione sincrona/asincrona derivata da Truax riguarda l'IOT (grani metrici vs random/blend). In De Poli/Piccialli la sincronia è agganciata al **periodo del segnale**/quasi-pitch, con obiettivo continuità di fase. Distinzione che evita falso parallelo terminologico — formalizzata in [[sintesi-granulare-sincrona]].

3. **Grano come risposta di filtro vs grano come lettura di buffer.** PGE è centrato sulla granulazione di campioni: domanda compositiva = "da dove nel buffer viene letto il grano?", da cui l'asse Y della partitura. De Poli/Piccialli lavorano invece sulla forma d'onda prototipo del grano, progettata come risposta FIR lineare. Visualizzazione spettrale/formantica, non partitura tempo-buffer.

4. **Pattern precompute-once / reuse-many**: forma d'onda prototipo tabulata una volta, riusata via lettura con passo variabile. Analogo strutturale al `WindowGenerator` PGE (finestra tabulata, riusata grano-per-grano con scaling). Stesso pattern ripreso e ampliato da [[ortosecco-piccialli1989]] su base wavelet.

5. **Sintesi additiva di stream di grani per formante**: «una sequenza di grani ad ogni zona dello spettro in movimento rispetto alle altre» (p. 71). Concettualmente identico allo `Stream` PGE come unità di organizzazione: ogni stream porta un comportamento parametrico indipendente, la sovrapposizione produce il suono complesso.

6. **Inviluppo come finestra di analisi**: «l'inviluppo corrisponde all'uso di finestre nell'analisi dei segnali» (p. 70). Stessa unificazione formale grain envelope ≡ window function che fonda la libreria di finestre PGE.

7. **Controllo percettivo come terreno comune.** Definire l'evoluzione sonora in termini di inviluppo spettrale/formanti anticipa l'esigenza che PGE affronta via DSL parametrico: evitare che il compositore lavori solo su valori grezzi. PGE però sposta il problema dal design del grano alla **leggibilità del processo generativo completo**.

## Posizionamento storico
**Filone offline italiano, scuola De Poli (Padova) / Piccialli (Napoli).** Pubblicato VII CIM 1988, stesso anno di Truax DMX-1000 (ICMC 1988) — ma posizione opposta: mentre Truax annuncia la rottura del vincolo offline, De Poli/Piccialli continuano sul terreno offline approfondendo qualità delle forme d'onda e controllo per formanti. Citano esplicitamente De Poli (1986) per filtri FIR a fase minima e VOSIM/Rodet/Liénard come precedenti additivi non a fase lineare. **Precursore diretto** di [[ortosecco-piccialli1989]] (VIII CIM), che porta lo stesso filone su base teorica wavelet e su DSP Ariel TMS 32025.

## Collegamento alla tesi centrale
Rafforza la tesi non per analogia diretta ma **per contrasto**. Mostra che nella tradizione CIM la sintesi granulare non è un unico percorso lineare verso il real-time: è campo di problemi tecnici e compositivi separabili. Loro problema: qualità del grano + coerenza di fase nei suoni quasi periodici. Problema PGE: abitare grande spazio parametrico di granulazione di campioni, dove la relazione tra specifica, partitura e ascolto richiede il loop lungo.

Utile per evitare di presentare PGE come "migliore" o più generale. PGE sceglie un sottoinsieme situato del paradigma granulare: tempo differito, sample-based granulation, controllo parametrico ad alto livello, lettura retroattiva via partitura. De Poli/Piccialli ricordano che altre scelte legittime portano altrove: grani progettati come filtri, sincronia di periodo, controllo formantico.

## Note stilistiche
Struttura classica CIM 1988: 5 sezioni numerate (1. Sintesi granulare / 2. Modello studiato / 3. Controllo dinamico / 4. Forme d'onda prototipo / 5. Conclusioni) + bibliografia. Densità citazioni media (9 ref). Tono argomentativo-tecnico: dichiara una proposta («La nostra proposta è di risolvere radicalmente questo problema...», p. 71), motiva la scelta, descrive il modello. Apertura analogica (sintesi granulare ≈ cinema, ≈ cartoni animati), chiusura sintetica che riassume i quattro contributi. Figura con esempi di trasformazione di prototipo gaussiano (p. 75 del PDF).

## Sezioni del paper CIM 2026 dove citare
- **Sezione 2 — Sintesi granulare**: ramo CIM della sintesi granulare sincrona; distinzione granulazione stocastica/asincrona ↔ period-synchronous. Da citare assieme a [[ortosecco-piccialli1989]] per documentare il filone De Poli/Piccialli.
- **Sezione 3 — Architettura PGE**: nota di delimitazione tecnica — PGE non è motore di sintesi formantica sincrona ma ambiente sample-based con DSL e renderer differiti; pattern precompute-once / reuse-many della forma d'onda prototipo come precedente CIM 1988 della `WindowGenerator`.

## Quote chiave
- p. 70: «Si riconosce che l'inviluppo corrisponde all'uso di finestre nell'analisi dei segnali. Nella sintesi, la finestra rettangolare può essere usata solo in casi particolari; più spesso essa deve essere opportunamente raccordata con lo zero. Per il raccordo sono stati proposti l'uso di mezzo coseno rialzato (finestra di Tukey), di mezza gaussiana (Roads), di una linea retta (finestra trapezoidale) (Truax).»
- p. 71: «La collocazione temporale dei grani in genere avviene ad intervalli fissi di 10 ÷ 20 millisecondi [...] Questo modo di aggiornamento, che chiameremo asincrono, in genere crea dei problemi nella sintesi di suoni quasi periodici, in quanto manca la continuità di fase tra grani consecutivi.»
- p. 71: «A questo scopo sarà dedicata una sequenza di grani ad ogni zona dello spettro in movimento rispetto alle altre. Riprendendo l'analogia con il cinema, usiamo una tecnica analoga ai cartoni animati, in cui l'immagine è composta di varie parti, elementari, contemporaneamente in movimento tra loro.»
- p. 71: «termini percettivamente significativi»
- p. 71: «sincrono con il periodo»
- p. 72: «filtri FIR a fase lineare»
