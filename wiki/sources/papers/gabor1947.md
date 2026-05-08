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

Gabor 1947 è la radice teorica del paradigma granulare ereditato da PGE. Tre conseguenze dirette per la tesi del paper:

1. **Grano come unità.** Il segnale elementare gaussiana × sinusoide è il modello del grano emesso da `Stream.generate_grains()`. Δt·Δf ≥ 1 fissa il trade-off durata/altezza che il compositore PGE incontra ogni volta che modifica `grain_duration`: sotto ~10 ms l'altezza svanisce, sopra ~50 ms i grani diventano eventi separati. La finestra 1–50 ms del paradigma granulare deriva direttamente dai due meccanismi di hearing di Gabor.

2. **Information diagram = ancestor della partitura grafica.** La matrice cᵢ,ₖ di Fig. 3 è la prima rappresentazione bidimensionale di un suono come collezione di grani discreti. Il `score_visualizer` di PGE eredita la struttura — grani come oggetti su un piano — ma sostituisce l'asse Y (frequenza → posizione-nel-buffer) per il caso d'uso granulazione di campioni. Specializzazione, non rottura: lo spettro emergente è codificato in colore (pitch ratio) e larghezza (durata), non rimosso. Questa eredità è ciò che rende leggibile la partitura nel loop lungo: il compositore osserva pattern su quanti tempo-buffer, non uno spettrogramma astratto.

3. **Separazione micro/macro.** Il "secondo meccanismo" di Gabor (p. 593) — inibizione laterale che affina la frequenza fino a ~250 ms — è la base fisiologica della separazione micro/macro che Truax 1994 formalizza come tesi psicoacustica abilitante del paradigma. Per PGE: gli Envelope su parametri devono evolvere su scale ≥ 250 ms per produrre percezione di "tendenza"; sotto quella scala il compositore lavora la texture, sopra la forma. Il loop lungo ha senso esattamente in questa seconda regione, dove la riflessione tra cicli opera su materiale percepito come forma e non come grano singolo.

## Sezioni del paper CIM 2026 dove citare

- **Sezione 2 (Sintesi granulare: dal paradigma Gabor al controllo gerarchico):** origine del paradigma. Δt·Δf ≥ 1 come fondamento del trade-off durata/altezza; due meccanismi di hearing come giustificazione della finestra 1–50 ms.
- **Sezione 4 (Partitura grafica):** information diagram Fig. 3 come ancestor concettuale; cambio d'asse Y come specializzazione.

## Quote chiave

> "Δt · Δf ≥ 1; that is to say, the area of the characteristic rectangle or cell of a signal is at least unity. This is the exact formulation of the uncertainty relation between time and frequency." (p. 591)

> "the ear possesses a threshold area of discrimination of the order unity." (p. 592)

> "It is interesting to note that we begin to perceive a sound as 'musical' just at the point where the second mechanism takes over. Speech would be perfectly intelligible by the first mechanism alone; but the second is necessary to enable us to appreciate music." (p. 593)
