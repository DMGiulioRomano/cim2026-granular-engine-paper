# [Roads, 2001] Microsound — Capitolo 2: The History of Microsound from Antiquity to the Analog Era

## Posizione nel libro
Capitolo 2 (book pp 43–84 / PDF pp 57–98). Capitolo *storico-genealogico*: ricostruisce il lignaggio del pensiero microsonico dall'atomismo greco fino all'era analogica (Stockhausen *Kontakte* 1960, Xenakis *Analogique B* 1959). Funge da prequel del cap. 3 (granular synthesis digitale) e del cap. 7 (composizione).

## Argomento centrale
Il pensiero microsonico ha radici antiche (atomismo di Leucippo/Democrito/Lucrezio, teoria corpuscolare di Beekman/Gassendi) ma diventa praticabile musicalmente solo nel XX secolo, attraverso una catena precisa: Einstein 1907 (phonon) → Gabor 1946–1952 (quanto acustico + matrice + granulatore elettro-ottico) → Meyer-Eppler 1950 (Mosaiktechnik, Gabor matrix come spartito) → Xenakis 1959 (screens, ataxy, *Analogique B*) → Stockhausen 1956 (unità tempo musicale, *Kontakte*). Roads costruisce esplicitamente la genealogia che legittima la propria pratica e l'intera tradizione granulare.

## Struttura del capitolo
- Waves versus Particles: Early Concepts of Microsound
  - Optical Wave versus Particle Debate (Newton, Huygens, Maxwell, Einstein)
  - Acoustical Wave versus Particle Debate (atomismo greco, Beekman 1616, Gassendi, Dalton)
  - Waves versus Particles: a Contemporary Perspective (Einstein 1907 phonon, Varèse 1940 *sonal energy*)
- The Modern Concept of Microsound
  - Temporal Continuity in Perception (persistence of vision, Zeno paradox)
  - The Gabor Matrix (Gabor 1946–1952, Δt·Δf ≥ 1, equazione quantum acustico)
  - Electro-optical and Electromechanical Sound Granulation (Gabor Kinematical Frequency Convertor 1946, Schaeffer-Poullin Phonogène 1950s, Springer Zeitregler/Tempophon)
  - Meyer-Eppler (Klangfarbenproblem 1950, Mosaiktechnik 1955; K = 2·W·T; 15 ms = lower JND)
  - Moles (segmentazione sonic message in elementary squares; ~340.000 elements totali nel repertorio percepibile)
  - Wiener (Newton-Gibbs *qualified indeterminism*; scetticismo Fourier)
  - Theory and Experiments of Xenakis (*Metastasis* 1954, *Concret PH* 1958, *Analogique B* 1959; screens; books; ataxy; Markov chains)
  - Problems with a Constant Microtime Grid (critique Δt costante: aesthetically limiting; artefatti AM/comb filtering)
  - Analog Impulse Generators (multivibrator, Kontakte 1960)
  - Stockhausen's Temporal Theory: How Time Passes / Unity of Musical Time (continuum rhythm↔pitch; tone color = result of time structure)
  - Assessment of Stockhausen's Temporal Theory (Backus, Babbitt time-point sets, Cowell 1930 precursore)
  - Other Assessments
- Microsound in the Analog Domain (Stockhausen/Koenig/Xenakis come fondatori della pratica)
- Microsound in the Instrumental Domain (Xenakis *Metastasis*/*Pithoprakta*/*Achorripsis*; cloud stocastico come effetto orchestrale)
- Summary

## Concetti chiave per PGE

- **Wave/particle complementarità su scala** (p. 55): «*Sound can be seen in a similar way, either wavelike or particle-like, depending upon the scale of measurement, the density of particles, and the type of operations that we apply to it.*» — supporto teorico per architettura multi-scala PGE.
- **Gabor matrix e quanto acustico** (pp. 57–60): equazione `g(t) = e^{-a²(t-t₀)²} × e^{2πjf₀t}` (Gaussian envelope × sinusoidal carrier) = stesso modello del grano sintetico PGE; Δt·Δf ≥ 1 = vincolo fondamentale che PGE rispetta in modalità grain-from-sample.
- **Critica della griglia microtemporale costante** (pp. 67–68): Roads identifica esplicitamente il limite estetico delle *screens* di Xenakis con frame rate Δt costante e grain duration costante: «*The idea that all grains have the same duration is aesthetically limiting. Experiments [...] show that grain size is one of the most important time-varying parameters of granular synthesis.*» PGE è progettato esattamente intorno alla soluzione: grain duration come parametro time-varying via Envelope/ProbabilityGate, density per-voice indipendente.
- **Xenakis screens lemma** (p. 65, Xenakis 1992 p. 43): «*All sound, even continuous musical variation, is conceived as an assemblage of a large number of elementary sounds adequately disposed in time. In the attack, body, and decline of a complex sound, thousands of pure sounds appear in a more or less short interval of time Δt.*» — formulazione fondativa del paradigma granulare compositivo.
- **Ataxy e Markov chains** (pp. 66–67): controllo ordine/disordine via matrice di transizione probabilistica; antesignano delle stochastic strategies PGE (ProbabilityGate, stochastic envelope strategies).
- **Stockhausen unità del tempo musicale** (p. 73): «*Pitch and rhythm can both be considered as dimensions of time*»; «*tone-color is the result of time structure*» (Stockhausen 1957, p. 19) — supporto teorico per l'idea che la struttura microtemporale (grain density, dephase, IOT) determina il timbro percepito.
- **Cowell come precursore multi-scala** (p. 78): «*Cowell's writings prove that a comprehensive multiscale view of time can be formulated quite independently of serial theory.*» — anti-corpo necessario contro la lettura di Roads come neo-seriale.
- **Frame rate ideale = sample rate** (p. 68): «*Ideally, however, this frame rate should operate at a speed as close as possible to the audio sampling rate.*» — anticipazione delle architetture per-grain (EmissionControl2 2021) e supporto per la scelta sample-rate del cache PGE.
- **Schaeffer epigrafe** (p. 44): «*Musical ideas are prisoners, more than one might believe, of musical devices.*» (Schaeffer 1977, pp. 16–17) — quote di cornice per la tesi PGE: scelta dello strumento = scelta della postura compositiva.

## Tabella sintetica precursori storici (Cap. 2)

| Anno | Autore/opera | Contributo microsonico | Mappatura PGE |
|------|--------------|------------------------|---------------|
| ~440 BC | Leucippo/Democrito | Atomismo: materia composta da particelle indivisibili | Pre-concezione grano |
| 1616 | Beekman | Teoria corpuscolare del suono | — |
| 1808 | Dalton | Teoria atomica della materia | — |
| 1907 | Einstein | Phonon: quanto acustico ultrasonico | Fondamento teorico grano |
| 1946–1952 | Gabor | Matrice acustica + Kinematical Frequency Convertor (granulatore elettro-ottico) + Δt·Δf ≥ 1 | Modello grano sintetico PGE |
| 1950 | Meyer-Eppler | Mosaiktechnik (Gabor matrix come spartito) + 15 ms JND | DSL anticipato come notazione |
| 1950s | Schaeffer/Poullin | Phonogène (granulatore rotating-head) | Granulazione sample anticipata (analogica) |
| 1958 | Xenakis | *Concret PH*: granulazione intuitiva di brace ardente su nastro | Composizione granulare pre-digitale |
| 1959 | Xenakis | *Analogique B*: screens, books, ataxy, distribuzioni esponenziali/lineari | Stochastic strategies + density control PGE |
| 1959 | Meyer-Eppler libro | K = 2·W·T (max structure content) | — |
| 1960 | Stockhausen | *Kontakte*: synthesis-by-impulses + recirculating feedback loops | Pulsar pre-digitale; out-of-scope PGE |
| 1957–62 | Stockhausen scritti | *How Time Passes* + *Unity of Musical Time*: continuum rhythm↔pitch | Razionale per cornice multi-scala |

## Rilevanza diretta per PGE

**Genealogia storica completa per Sezione 2 del paper.** Cap. 2 fornisce in 42 pagine il lignaggio antiquo→analogico che il paper CIM deve compattare nei primi paragrafi della Sezione 2 ("Sintesi granulare: dal paradigma Gabor al controllo gerarchico"). Strategia di citazione: 1–2 frasi che condensano il lignaggio Gabor → Meyer-Eppler → Xenakis → Stockhausen, citando Roads 2001 cap. 2 come fonte di riferimento completa.

**Critica esplicita del frame rate costante (pp. 67–68).** Roads articola nel 2001 il limite estetico delle screens Xenakis (grain duration uniforme, comb filtering). PGE risolve via density e duration come parametri time-varying per-voice. Questo passaggio è cruciale per posizionare il `ParameterOrchestrator` come superamento esplicito del modello *screens*: non un raffinamento incrementale ma una risposta diretta a un problema identificato in letteratura.

**Schaeffer quote pp. 44 come framing.** «*Musical ideas are prisoners, more than one might believe, of musical devices.*» — quote da aprire la Sezione 1 in alternativa o complemento alla quote pp. 10 cap. 1: la postura compositiva è inseparabile dalla scelta dell'ambiente tecnologico. PGE come scelta consapevole di un device (deferred-time, DSL YAML) che abilita una postura specifica (loop lungo).

**Wave/particle dualismo come framework multi-scala.** Citazione p. 55 come razionale architetturale per la separazione di responsabilità in PGE: ciascuna scala richiede operazioni differenti (composizione su macro/meso = YAML; granulation su micro = generator; rendering su sample = NumPy/Csound).

**Ataxy e Markov chains.** I controlli di ordine/disordine di Xenakis (cap. 2 pp. 66–67) sono il prototipo concettuale delle voice/density strategies PGE. La differenza chiave: PGE espone questo controllo come scelta YAML esplicita (strategy + parametri), non come matrice numerica criptica.

## Collegamento alla tesi centrale

**Sezione 2 (Sintesi granulare).** Cap. 2 è la fonte canonica per condensare il lignaggio storico in 1–2 paragrafi del paper. Citazione `Roads2001` con riferimento esplicito al cap. 2 per la genealogia completa.

**Tesi loop lungo.** Cap. 2 mostra che la pratica microsonica nasce *labour-intensive* (Xenakis *Concret PH*: splicing manuale di registrazioni di brace ardente; Stockhausen *Kontakte*: patch elaborate con feedback loops; *Analogique B*: 2 min 25 sec ottenuti da migliaia di frammenti di sinusoide su nastro). Il loop lungo non è un'invenzione PGE: è la modalità di lavoro fondativa del campo, ridotta artificialmente con l'avvento del real-time DSP (Truax 1988) e oggi riabilitata con strumenti DSL. PGE è la materializzazione contemporanea della temporalità storica del lavoro microsonico.

**Contributo (1) DSL YAML.** Meyer-Eppler già nel 1955 descrive la Gabor matrix come «*a kind of score that could be composed with a Mosaiktechnik*» (p. 62). Roads in cap. 1 propone esplicitamente il «*musically descriptive language*» (p. 26). YAML PGE è la realizzazione contemporanea di un programma teorico vecchio di 70 anni.

**Differenziatore frame rate non-costante.** Pp. 67–68 documentano il problema del grain-duration uniforme. PGE risolve via ParameterOrchestrator + Envelope time-varying per-voice + dephase per-grain. Argomentazione di posizionamento nel paper sez. 3.

## Quote chiave

> «*Musical ideas are prisoners, more than one might believe, of musical devices.*» (Schaeffer 1977 pp. 16–17, riportato da Roads p. 44) — *framing della Sezione 1.*

> «*Sound can be seen in a similar way, either wavelike or particle-like, depending upon the scale of measurement, the density of particles, and the type of operations that we apply to it.*» (p. 55) — *razionale multi-scala.*

> «*All sound, even continuous musical variation, is conceived as an assemblage of a large number of elementary sounds adequately disposed in time. In the attack, body, and decline of a complex sound, thousands of pure sounds appear in a more or less short interval of time Δt.*» (Xenakis 1992 p. 43, riportato da Roads p. 65) — *lemma fondativo granular synthesis compositivo.*

> «*The idea that all grains have the same duration is aesthetically limiting. Experiments [...] show that grain size is one of the most important time-varying parameters of granular synthesis.*» (p. 67) — *critica del frame rate costante, supporto per ParameterOrchestrator PGE.*

> «*Ideally, however, this frame rate should operate at a speed as close as possible to the audio sampling rate.*» (p. 68) — *anticipazione architettura per-grain.*

> «*The important thing ... is that tone-color is the result of time structure.*» (Stockhausen 1957 p. 19, riportato da Roads p. 78) — *timbro come emergenza microtemporale; razionale per asse Y partitura PGE.*

> «*The contemporary scientific view of microsound dates back to Dennis Gabor, who applied the concept of an acoustic quantum (already introduced by Einstein) to the threshold of human hearing. With Meyer-Eppler as intermediary, the pioneering composers Xenakis, Stockhausen, and Koenig injected this radical notion into music.*» (p. 84, summary) — *genealogia compatta per Sezione 2.*

## Sezioni del paper CIM 2026 dove citare

- **Sezione 1 (Introduzione).** Quote Schaeffer p. 44 come framing alternativo o complementare alla quote loop lungo p. 10 cap. 1.
- **Sezione 2 (Sintesi granulare).** Sezione cardine. Quote summary p. 84 (genealogia compatta Gabor → Meyer-Eppler → Xenakis/Stockhausen/Koenig). Quote Xenakis lemma p. 65. Riferimento generale a cap. 2 di Roads2001 per l'intero lignaggio storico.
- **Sezione 3 (Architettura PGE).** Quote pp. 67–68 (critica frame rate costante) come *anti-pattern di riferimento* che ParameterOrchestrator + Envelope time-varying risolvono. Quote p. 55 (multi-scala) come razionale modulare.
- **Sezione 4 (Partitura grafica).** Stockhausen quote p. 78 (tone-color = time structure) come supporto teorico per la rappresentazione esplicita della microstruttura nella partitura PGE.
- **Sezione 6 (Conclusioni).** Quote Schaeffer come chiusura: ribadire che PGE è una scelta di *device* che incarna una postura.

## Quote di apertura cap. 2 (Roads stesso)

> «*The evolution of sound synthesis has always been interwoven with the engines of acoustic emission, be they mechanoacoustic, electromechanical, electro-optical, analog electronic, or digital. The current state of music technology has been arrived at through decades of laboratory experimentation. If we are to benefit from this legacy, we must revisit the past and recover as much knowledge as we can.*» (p. 44) — *manifesto programmatico del cap. 2; razionale per la prospettiva storica del paper CIM.*
