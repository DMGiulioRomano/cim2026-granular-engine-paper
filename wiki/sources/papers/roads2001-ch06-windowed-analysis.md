# [Roads, 2001] Microsound — Capitolo 6: Windowed Analysis and Transformation

## Posizione nel libro
Capitolo 6 (book pp 235–300 / PDF pp 249–314). Capitolo *tecnico-DSP*: trattamento esaustivo delle tecniche di analisi-risintesi a finestra (STFT, phase vocoder, vector oscillator transform, wavelet, Gabor transform). Complemento al cap. 5: laddove cap. 5 lavora nel time-domain, cap. 6 passa per il frequency-domain.

## Argomento centrale
La microsound può essere manipolata via analisi-risintesi a finestra (windowed analysis): segmentazione del segnale → trasformata a finestra → modifica dei dati spettrali → risintesi. Roads catalogizza STFT, phase vocoder (PV), tracking phase vocoder (TPV), vector oscillator transform (VOT), wavelet transform (WT), Gabor transform (GT) come strumenti per pitch-time changing, spectral filtering, stable/transient extraction, cross-synthesis, formant filtering, sonographic transformations, timbre morphing.

## Struttura del capitolo (sintesi)
- Overview of Windowed Spectrum Analysis (methods, models, spectrum vs timbre, data packing/reduction)
- Theory of Fourier Analysis (Fourier series, FT, DFT)
- The Short-Time Fourier Transform (windowing, time-frequency uncertainty/tradeoffs)
- The Phase Vocoder (parameters: window size, FFT/hop size, window type; overlap-add e oscillator-bank resynthesis)
- Sound Transformation with Windowed Spectrum Operations (pitch-time changing, frequency-domain filtering, stable/transient extraction, dynamic range manipulations, vocoding/spectral mutation/formant filtering)
- Sonographic Transformations (sonogram filtering)
- The Tracking Phase Vocoder (peak tracking, accuracy, TPV editing, timbre morphing, deterministic + stochastic TPV)
- The Vector Oscillator Transform
- Wavelet Analysis and Resynthesis (history, FWT, wavelet display, transformations, synthetic wavelets)
- Gabor Analysis (theory of GT, Gaussian window properties, musical applications: Arfib/Delprat, Kronland-Martinet; assessment)
- Summary

## Concetti chiave per PGE

### Gabor analysis come fondamento teorico del grano PGE

Cap. 6 pp. 295–299 dedica una sezione alla Gabor transform digitale (Arfib/Delprat anni '90). La gaboret (Gaussian window × complex exponential) è la versione analitica del *grain sintetico* PGE: stesso modello, scopo opposto (PGE genera grani, Gabor analizza segnali in grani).

Fig 6.8 schema GT: source × gaboret → modulus + phasogram → resynthesis via reproducing kernel.

Questa è la **versione analitica della pipeline PGE in reverse**: il grano è l'atomo per costruzione (PGE) o per decomposizione (GT). Il framework teorico è identico — Δt·Δf ≥ 1, Gaussian envelope, comportamento sull'asse tempo-frequenza.

### Windowing = synchronous granulation (p. 239)

> «*Windowing is akin to synchronous granulation (see chapter 5). The use of the term window, however, usually implies that a form of spectrum analysis will follow.*» (p. 239)

Roads articola la corrispondenza esplicita: finestratura per analisi spettrale = granulazione sincrona vista dall'altra parte. PGE è quindi *connesso architetturalmente* al framework spettrale anche se non esegue analisi-risintesi: condivide la primitiva atomica (la finestra/grano gaussiano).

### Uncertainty principle Δt·Δf ≥ 1

Il principio di indeterminazione di Gabor è citato ripetutamente (pp. 245–246, 295, 299). PGE rispetta implicitamente questo vincolo: la durata del grano determina la risoluzione spettrale percepita. Grani molto corti (< 10 ms) hanno spettro largo (rumorisi); grani lunghi (> 50 ms) preservano la qualità tonale del sample. Questo è il razionale fisico per gli encoding visivi della partitura grafica PGE (larghezza grano = durata).

### Out-of-scope per PGE 2026

L'intero apparato analisi-risintesi (STFT, PV, TPV, VOT, WT) è **fuori dallo scope di PGE**. PGE opera esclusivamente nel time-domain: legge campioni, li finestra (Gaussian/Hann/cosine taper), applica pitch shift via resampling, e somma overlap-add. Non c'è FFT, non c'è dominio frequenziale.

Cap. 6 documenta il *territorio adiacente* che PGE *non* tocca. Utile per il paper per delimitare lo scope con precisione: PGE è un granular engine *time-domain* deferred. Per pitch-time changing avanzato preservando i formanti, per spectral morphing, per timbre interpolation, per cross-synthesis spettrale → si usano altri strumenti (SuperVP/AudioSculpt, SoundHack, Composer Desktop Project). PGE è complementare, non sostitutivo.

### Quote di apertura cap. 6 (Mallat 1998, p. 238)

> «*Yet, classical signal processing has devoted most of its efforts to the design of time-invariant and space-invariant operators, that modify stationary signal properties. This has led to the indisputable hegemony of the Fourier transform, but leaves aside many information-processing applications. The world of transients is considerably larger and more complex than the garden of stationary signals.*» — *manifesto della microsound: il mondo dei transienti è il dominio reale della musica, e richiede strumenti non-Fourier.*

### Summary cap. 6 (Orcalli 1993, p. 300)

> «*By allowing noise to make inroads into musical sound, Varèse accelerated a trend toward the shattering of traditional musical language. Together with the inadequacy of neo-serialism, this resulted in a fragmentation of musical language and a consequent proliferation of composition techniques, very far from a possible theoretical unification. On the other hand, the increase in methods of acoustic analysis created a situation analogous to the physics of the microcosmos — an imagined unity of sonic phenomena. Here began an opposition to the continuous wave theory of sound, a granular atomism that was capable of representing any chaotic state of sound material and was also effective on the plane of synthesis.*» (Orcalli 1993)

Questa quote è **utile per Sezione 2** del paper: cattura in 4 frasi il movimento storico che porta dal serialismo al granulare, e riconosce esplicitamente che l'atomismo granulare opera contemporaneamente come *modello analitico* e *piano di sintesi*.

### Hugo epigrafe cap. 6 (p. 299)

> «*Where the telescope ends, the microscope begins. Which has the grander view?*» (Victor Hugo 1862)

Quote evocativa per Sezione 4 o Sezione 6: il cambio di scala come questione metodologica, non solo tecnica.

## Rilevanza diretta per PGE

**Razionale teorico del grano gaussiano.** Cap. 6 fornisce il fondamento DSP per il modello del grano in PGE: gaussian × exponential carrier (analitico) ↔ gaussian envelope × sample lookup (sintetico). Per la Sezione 3 del paper, basta una nota o citazione: il modello PGE deriva dal framework Gabor consolidato in Roads 2001.

**Delimitazione scope.** Cap. 6 è la fonte canonica per dire al revisore: «PGE è un granular engine time-domain, non un analyzer-resynthesizer. Tecniche spettrali avanzate (PV, TPV, wavelet) sono fuori scope per scelta, non per mancanza». Utile in Sezione 3 o 6.

**Gap esplicito.** PGE *potrebbe* in futuro integrare un mode «analyze-then-granulate» (granulate spectral data invece di campioni). Cap. 6 è il riferimento per questo gap futuro (sviluppo evolutivo possibile).

**Non priorità per il paper CIM.** Cap. 6 è il capitolo *meno citabile* di Roads 2001 per il paper PGE — operiamo in time-domain, cap. 6 è frequency-domain. Riferimento principalmente per (a) razionale teorico Gabor, (b) delimitazione scope.

## Collegamento alla tesi centrale

**Razionale teorico del grano.** Cap. 6 conferma che PGE adotta consapevolmente il modello atomico Gabor-Xenakis come unità sintetica. Coerente con il lignaggio storico (cap. 2) e con la tassonomia multi-scala (cap. 1).

**Differenziatore vs analyzer-resynthesizer tools.** Il paper può dichiarare esplicitamente: PGE *non* è un PV o TPV o wavelet processor. È un granular engine time-domain deferred con DSL YAML. Questa precisazione sgombera il campo da confusioni con sistemi adiacenti.

**Out-of-scope dichiarato.** Cap. 6 fornisce il vocabolario tecnico per delimitare lo scope in Sezione 3: «PGE opera nel time-domain; trasformazioni spettrali sono delegate a tool esterni del workflow audio engineering del compositore».

## Quote chiave

> «*Yet, classical signal processing has devoted most of its efforts to the design of time-invariant and space-invariant operators, that modify stationary signal properties. This has led to the indisputable hegemony of the Fourier transform, but leaves aside many information-processing applications. The world of transients is considerably larger and more complex than the garden of stationary signals.*» (Mallat 1998, citato p. 238) — *cornice epistemica per l'intero campo microsound.*

> «*Windowing is akin to synchronous granulation (see chapter 5). The use of the term window, however, usually implies that a form of spectrum analysis will follow.*» (p. 239) — *connessione esplicita tra granular synthesis (PGE) e windowed analysis.*

> «*Here began an opposition to the continuous wave theory of sound, a granular atomism that was capable of representing any chaotic state of sound material and was also effective on the plane of synthesis.*» (Orcalli 1993, citato p. 300) — *granular atomism come modello analitico + sintetico unificato.*

> «*Where the telescope ends, the microscope begins. Which has the grander view?*» (Victor Hugo 1862, citato p. 299) — *quote epigrafica per cambio di scala.*

> «*Beginning in the 1950s, a handful of visionary scientists, acoustical engineers, and musicians such as Gabor, Meyer-Eppler, Xenakis, and Stockhausen proposed new theories of sound organization based on microsonic particles. Critics attacked them on the basis that sound quanta were divisible and therefore not fundamental, thereby missing the point. While there are no fundamental sound particles, any sound can be decomposed into an innumerable number of different particles, depending on the chosen basis functions.*» (p. 300, summary) — *legittimazione operazionale del paradigma granulare: non serve che il grano sia ontologicamente fondamentale; basta che sia operativamente potente.*

## Sezioni del paper CIM 2026 dove citare

- **Sezione 2 (Sintesi granulare).** Quote Orcalli p. 300 (granular atomism come modello). Riferimento opzionale a cap. 6 come trattazione DSP complementare.
- **Sezione 3 (Architettura PGE).** Riferimento a cap. 6 (Gabor transform) per fondamento teorico del modello del grano. Delimitazione scope: PGE è time-domain.
- **Sezione 6 (Conclusioni — sviluppi futuri).** Possibile menzione di analyze-then-granulate mode come direzione futura, con cap. 6 come riferimento per le tecniche di analisi disponibili.
