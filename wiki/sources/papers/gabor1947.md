# [Gabor, 1947] Acoustical Quanta and the Theory of Hearing

## Citazione CIM

Gabor, D. (1947). Acoustical Quanta and the Theory of Hearing. *Nature*, 159(4044), 591–594.

## Argomento centrale

Gabor estende il proprio approccio comunicazionale (Gabor 1946, *J. Inst. Elect. Eng.*) all'acustica soggettiva. Sostituisce la rappresentazione Fourier-only del suono con un **information diagram** bidimensionale tempo × frequenza, dimostra una relazione di indeterminazione Δt · Δf ≥ 1, e mostra che l'orecchio umano possiede una soglia di discriminazione di ordine unitario — un *acoustical quantum* di informazione.

## Gap o problema identificato

La teoria classica di Ohm–Helmholtz descrive l'udito come analizzatore di Fourier: la sensazione sarebbe somma dei moduli delle componenti spettrali. Ma Fourier è una descrizione *timeless* in termini di onde di durata infinita. L'esperienza più elementare mostra invece che il suono ha simultaneamente **pattern temporale e pattern di frequenza**. Manca una descrizione matematica che tratti *ab ovo* questa dualità.

Gabor risolve assumendo tempo e frequenza come coordinate ortogonali e definendo, per ogni segnale, un rettangolo caratteristico (cella) nel piano. La diseguaglianza di Schwarz applicata alle deviazioni quadratiche medie delle distribuzioni di energia (segnale e suo spettro) dà:

> Δt · Δf ≥ 1   (eq. 1, p. 591)

L'area minima — il "quanto di informazione" — corrisponde ai segnali elementari di forma gaussiana modulata:

> s(t) = exp(−α²(t − t₀)²) · exp(i 2π f₀ t)   (eq. 2, p. 591)

Un segnale arbitrario può essere espanso su un reticolo di tali grani con coefficienti complessi cᵢₖ (Fig. 3, p. 592 — la matrice di segnali elementari).

L'analisi delle soglie sperimentali di Bürck–Kotowski–Lichte (1935) e Shower–Biddulph (1931) mostra che l'orecchio discrimina aree tempo-frequenza ≈ 1.05–1.17, prossime al limite quantistico, su un range di rapporti Δt/Δf di oltre un ordine di grandezza. Gabor postula due meccanismi: (a) risuonatori meccanici della coclea, fortemente smorzati (decadimento ~10 ms); (b) un secondo meccanismo non meccanico che affina la frequenza percepita fino a 250 ms — probabilmente inibizione laterale tra fibre nervose adiacenti. La percezione "musicale" inizia quando subentra il secondo meccanismo.

## Rilevanza diretta per PGE

Foundational. Il paradigma granulare nasce qui: Xenakis (*Formalized Music*) e poi Roads, Truax, Di Scipio citano Gabor come radice teorica.

Tre punti di contatto specifici con PGE:

1. **Grano Gabor = unità sintetica di PGE.** Il segnale elementare gaussiana × sinusoide è esattamente il modello del singolo grano emesso da `Stream.generate_grains()`. Il window controller di PGE applica un inviluppo (oggi tipicamente Hann o trapezio, ma la famiglia gaussiana è inclusa) sul segnale risincronizzato; la durata del grano e la sua frequenza fondamentale determinano l'aspetto Δt × Δf della cella tempo-frequenza occupata dal grano.

2. **Information diagram di Fig. 3 = ancestor della partitura grafica.** La matrice c_{i,k} su piano tempo × frequenza è il primo schema di rappresentazione bidimensionale di un suono *come collezione di grani*. La partitura PGE (`score_visualizer.py`) eredita la struttura — grani come oggetti discreti su un piano — ma cambia l'asse Y: posizione nel buffer sorgente invece di frequenza. Sostituzione motivata dal caso d'uso (granulazione di sample, non sintesi pura), non rottura concettuale.

3. **Limite quantistico spiega la soglia psicoacustica del granulare.** Truax (1988, 1990) sceglie 1–50 ms come range tipico del grano: sotto ~10 ms l'orecchio non distingue altezza (coclea non si è ancora sintonizzata); oltre ~50 ms i grani diventano eventi separati. Questa finestra deriva dai due meccanismi di Gabor (Fig. 5, p. 593). La densità che separa percezione "pulsata" da continuum granulare in PGE (`DensityController`, blend lineare Truax sincrono/asincrono) opera proprio nella regione in cui il numero di grani-quanto al secondo supera la risoluzione del secondo meccanismo.

## Collegamento alla tesi centrale

Il gap controllo/percezione ha qui la sua origine teorica. Gabor mostra che la percezione **non opera su Fourier puro** ma su quanti tempo-frequenza con dualità irriducibile. Il compositore granulare manipola direttamente questi quanti — un evento granulare è già nello spazio percettivamente rilevante, non un'astrazione spettrale da decodificare.

Conseguenza per PGE: la mediazione visuale (`score_visualizer`) deve operare allo stesso livello del fenomeno percettivo — un grano = un oggetto grafico discreto, non un sample-level waveform né uno spettrogramma astratto. La scelta di posizione-buffer come asse Y è un trade-off pragmatico (granulazione di campioni richiede di vedere *da dove* viene prelevato il materiale), non una negazione del piano Gabor: lo spettro emergente dei grani è implicito nella loro densità + pitch ratio, codificati in colore e larghezza.

Inoltre il "secondo meccanismo" di Gabor (p. 593) — inibizione laterale che affina la frequenza nel tempo — è la ragione fisiologica per cui i tendency masks di Truax e gli envelope di PGE devono evolvere su scale ≥ 250 ms per produrre percezione di "tendenza" coerente. Sotto quella scala, il compositore controlla texture; sopra, gestisce forma.

## Sezioni del paper CIM 2026 dove citare

- **Sezione 2 (Contesto teorico):** origine del paradigma granulare. Gabor come radice teorica della gerarchia di controllo Truax. Citare Δt·Δf ≥ 1 come fondamento del trade-off durata/altezza nel grano.
- **Sezione 4 (Partitura grafica):** information diagram (Fig. 3) come ancestor concettuale di tutte le rappresentazioni grafiche granulari. Esplicitare il cambio d'asse Y (frequenza → buffer-position) come specializzazione, non rottura.

## Quote chiave

> "Δt · Δf ≥ 1; that is to say, the area of the characteristic rectangle or cell of a signal is at least unity. This is the exact formulation of the uncertainty relation between time and frequency." (p. 591)

> "the ear possesses a threshold area of discrimination of the order unity." (p. 592)

> "It is interesting to note that we begin to perceive a sound as 'musical' just at the point where the second mechanism takes over. Speech would be perfectly intelligible by the first mechanism alone; but the second is necessary to enable us to appreciate music." (p. 593)
