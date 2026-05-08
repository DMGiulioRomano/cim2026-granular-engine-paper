# [De Poli & Piccialli, 1991] Pitch-Synchronous Granular Synthesis

## Citazione CIM
De Poli, G., & Piccialli, A. (1991). Pitch-Synchronous Granular Synthesis. In G. De Poli, A. Piccialli, & C. Roads (Eds.), *Representations of Musical Signals* (pp. 187-219). Cambridge, MA: MIT Press.

Nota: il PDF e' scannerizzato; il testo e' stato letto tramite OCR locale.

## Argomento centrale
Il capitolo presenta la sintesi granulare non come un singolo modello di sintesi, ma come una famiglia di modelli che usano forme d'onda localmente definite. Dopo aver ricondotto STFT, wavelet e overlap-and-add a interpretazioni granulari, De Poli e Piccialli propongono un modello pitch-synchronous per suoni intonati: un treno quasi periodico di impulsi, sincronizzato al pitch, eccita un filtro FIR tempo-variante che modella l'inviluppo spettrale.

In questa lettura, il grano coincide con la risposta all'impulso del filtro, la posizione temporale del grano determina l'articolazione del pitch, e la trasformata di Fourier del grano determina l'inviluppo spettrale. Il sistema punta a un controllo compatto e musicalmente significativo tramite prototype waveforms e trasformazioni di forma d'onda: ampiezza, somma pesata, traslazione in frequenza, scala temporale, distorsione della scala temporale e distorsione di fase.

## Gap o problema identificato
Il capitolo individua un problema doppio:

1. Le rappresentazioni non parametriche come STFT e wavelet offrono un fondamento rigoroso, ma producono molti coefficienti o grani la cui interpretazione non e' sempre significativa per il musicista.
2. Per un uso musicale efficiente servono pochi parametri legati a un modello concettuale: pitch, forma dell'inviluppo spettrale, formanti, ampiezza, larghezza di banda e trasformazioni controllabili nel tempo.

La soluzione e' usare informazione a priori sul processo acustico: per suoni intonati, la griglia dei grani non e' indipendente dal segnale, ma segue l'inizio di ogni periodo di pitch. Cosi' si riduce il numero di grani necessari e si separa piu' chiaramente il controllo temporale/pitch dal controllo spettrale/formantico.

## Rilevanza diretta per PGE
La rilevanza per PGE e' soprattutto contrastiva e terminologica.

1. **De Poli/Piccialli 1991 consolidano il ramo source-filter.** Rispetto al paper CIM 1988, il capitolo MIT rende piu' esplicita la cornice: sintesi granulare come controllo di grani-risposta FIR, organizzati da un treno di impulsi quasi periodico. Il centro non e' la distribuzione di cloud sample-based, ma il disegno del grano e la sua funzione nel controllo formantico.

2. **La griglia dipende dal suono, non da una timeline compositiva autonoma.** Nelle figure 6.5-6.7 il confronto e' tra griglie STFT/wavelet indipendenti dal segnale e griglia pitch-synchronous agganciata all'inizio dei periodi. In PGE, invece, la distribuzione dei grani e' definita dal DSL e dal `DensityController`; non deriva da un pitch tracking del materiale sorgente.

3. **"Sincrono" resta un falso amico per PGE.** Qui significa sincronizzazione dei grani con il periodo di pitch e aggiornamento dei parametri spettrali in corrispondenza degli impulsi. In PGE, la sincronia/asincronia riguarda l'IOT e l'organizzazione temporale dello stream, non una sorgente quasi periodica.

4. **Controllo parametrico come terreno comune.** Il capitolo cerca parametri pochi, separabili e percettivamente significativi; PGE condivide questa esigenza ma la sposta su un altro oggetto: non prototype waveforms e formanti, ma regioni di buffer, envelope, pitch ratio, densita', pan, voci e rendering per stream.

## Collegamento alla tesi centrale
De Poli e Piccialli 1991 rafforzano la tesi centrale per delimitazione. Mostrano che la granularita' puo' diventare un paradigma di rappresentazione molto rigoroso, capace di unificare STFT, wavelet, OLA e sintesi formantica quando il problema compositivo e' il controllo di suoni intonati e della loro struttura spettrale.

PGE abita un'altra postura: granulazione di campioni, tempo differito scelto, DSL dichiarativo, partitura tempo-buffer e workflow STEMS. Il confronto evita di presentare PGE come approdo generale della sintesi granulare: PGE e' una risposta situata al problema di esplorare spazi parametrici sample-based attraverso un loop lungo di specifica, generazione, ascolto e riscrittura.

## Sezioni del paper CIM 2026 dove citare
- Sezione 2 (Sintesi granulare: dal paradigma Gabor al controllo gerarchico): ramo pitch-synchronous/source-filter della sintesi granulare; distinzione tra griglie STFT/wavelet e griglia dipendente dal pitch
- Sezione 3 (PGE: architettura per l'indagine parametrica): delimitazione tecnica di PGE come ambiente sample-based con DSL e renderer differiti, non come sintetizzatore formantico pitch-synchronous

## Quote chiave
- "granular synthesis is not a single synthesis model" (p. 187)
- "directly and separately controlling a few perceptually significant parameters" (p. 188)
- "the grid depends directly on the sound" (p. 196)
