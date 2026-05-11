# [Roads, 2001] Microsound — Capitolo 4: Varieties of Particle Synthesis

## Posizione nel libro
Capitolo 4 (book pp 119–178 / PDF pp 133–192). Capitolo *core* del libro (60 pp): catalogo esteso di nuovi tipi di particella oltre il grano gaussiano classico.

## Argomento centrale
Catalogo sistematico di **dieci tipi di particelle sintetiche**: grain (cap. 3), glisson, grainlet, trainlet, pulsar, micro-arc (graphic/sonographic), FOF/Vosim/window-function (particle-based formant), transient drawing, particle cloning, physical-model particles, abstract-model particles. Per ognuno: definizione, parametri, implementazione, effetti percettivi, applicazioni musicali. Tabella 4.4 (p. 177) sintetizza tutti i tipi con envelope, waveform e caratteristiche distintive.

## Struttura del capitolo
- **Glisson Synthesis** (chirp/chirplet, magnetization patterns, SC1/SC2 implementation 1998–99)
- **Grainlet Synthesis** (parameter linkage 1996, frequency-duration / amplitude-duration / space-duration / frequency-space / amplitude-space experiments)
- **Trainlet Synthesis** (impulse generation, gbuzz, theory + 25 cloud parameters, Creatovox real-time)
- **Pulsar Synthesis** (PS): basic PS — anatomia (pulsaret w / duty cycle d / silence s / period p = d+s) — Pulsaret-Width Modulation (PWM, PulWM, OPulWM by de Campo) — synthesis across time scales — spectra — advanced PS (multiple pulsar generators, pulsar masking burst/channel/stochastic, convolution with samples) — implementations (PulsarGenerator de Campo+Roads, ~1500 LOC SC2) — composing with pulsars — applicazioni in *Clang-Tint* (1993), *Half-life* (1998–99), *Tenth/Eleventh vortex* (2000–01)
- **Graphic and Sonographic Synthesis of Microsound** (UPIC Xenakis 1980/1991 micro-arcs, Phonogramme Lebros 1993 harmonic pen + dot spray, MetaSynth Wenger/Spiegel 1999 granular spray brush)
- **Particle-Based Formant Synthesis** (FOF / CHANT, Vosim Kaegi/Tempelaars, Window Function Bass/Goeddel 1981)
- **Synthesis by Transient Drawing** (synthetic + transformational; Pointillist analogy Seurat; Roads in *Clang-Tint Organic*, *Half-life*)
- **Particle Cloning Synthesis** (Replicate function in sound editor; Roads in *Half-life*)
- **Physical Models of Particles** (PhISEM Cook 1996/97 maracas, Keller/Truax 1998)
- **Abstract Models of Particles** (Sturm 1999 atomic, Xenakis GENDYN, Cosmophone)
- Summary

## Tassonomia particle types (Table 4.4 sintetizzata)
| Particella | Envelope | Waveform | Caratteristica distintiva |
|------------|----------|----------|---------------------------|
| Grain | Gaussian/arbitrary | Arbitrary, sampled | Gabor/Roads, scattering metrico o stocastico |
| Glisson | Gaussian/arbitrary | Arbitrary | Trajectory frequenziale per-particle (chirp) |
| Pulsar | Rect-then-null / Gaussian / expodec / arbitrary | Arbitrary | Controllo indipendente fundamental ↔ formant |
| Trainlet | Expodec/arbitrary | Impulse | Treno impulsi, controllo indip. fund/formant |
| Wavelet | Gaussian/altro vincolato | Sinusoidal | Durata varia con frequenza |
| Grainlet | Gaussian/arbitrary | Sine | Linkage tra parametri di sintesi |
| Micro-arc | Arbitrary | Arbitrary, sampled | Disegno grafico, trasformazioni |
| FOF | Attack/sustain/release | Sine | Envelope controlla spettro formantico |
| Vosim | Linear attack, exp decay | Sine² pulses | Controllo flessibile spettro tonale |
| Window-function | Rectangular-then-nil | Blackman-Harris pulse | Formanti puramente armonici |
| Transient drawing | Arbitrary | Hand-drawn | Ogni transwave unica, sharp/percussive |
| Particle cloning | Arbitrary | Arbitrary, sampled | Replica per costruire continuous tone |

## Concetti chiave
- **Engines of particle synthesis are not especially complicated. It is the combination of many simple elements that forms a complex time-varying sound. We shape the sound's evolution by controlling this combination from a high musical level.** (p. 121) — *principio architetturale generale che PGE eredita.*
- **Parameter linkage** (grainlet, p. 125): esplicita interdipendenza tra parametri di sintesi (es. duration ∝ 1/frequency come nei wavelet; oppure amplitude ↔ duration; oppure space ↔ duration). Roads pone parameter linkage come *strategia generativa* a sé.
- **Pulsar parameters** (pp. 138–141): pulsaret waveform `w`, pulsaret envelope `v`, pulsar period `p`, duty cycle `d`, silence `s`, fundamental freq `fp = 1/p`, formant freq `fd = 1/d`. Indipendenza fp/fd è il salto concettuale chiave: rate di emissione e formante controllati separatamente.
- **Synthesis across time scales** (p. 142–144): pulsar attraversa la barriera infrasonic↔audio. Sopra ~25 ms si percepisce ritmo, sotto ~200 µsec tono continuo. *Pulsar graph* (p. 144, fig. 4.14) come notazione tempo×rate-di-emissione con asse Y a doppia scala (note values + frequenze).
- **Pulsar masking** (burst / channel / stochastic, p. 149–151): generazione di sotto-strutture ritmiche dal mascheramento di un pulsar train regolare.
- **Graphic vs sonographic synthesis** (p. 157–162): graphic = time-domain (UPIC original); sonographic = frequency-domain (UPIC arcs come F×T). MetaSynth granular spray brush — *unico esempio nella letteratura di tool grafico che produce granular*.
- **Pointillist analogy** (p. 171, transient drawing): «In effect, the composer works in a manner similar to a Pointillist painter such as Georges Seurat, building an image from thousands of tiny brush strokes.»

## Pulsar synthesis (in dettaglio)

Roads dedica ~20 pagine alla pulsar synthesis. È **la sua tecnica firma post-Microsound** e diventerà il filone UCSB (PulsarGenerator 2001 → EmissionControl 2005 → EC2 2021, vedi `roads2006.md` e `roads2021.md`).

**Differenza da granular synthesis classica:** PS è *sintesi* (genera waveform da zero, no buffer), granular è *granulazione* (estrae da buffer). Roads pone PS come tecnica indipendente perché:
- ha controllo *indipendente* di fundamental (fp) e formant (fd) — non possibile in granular classica
- attraversa la barriera infrasonic/audio in un parametro continuo → unifica rhythm e pitch
- ammette PWM/PulWM/OPulWM come trasformazioni proprie

**Versione differenziata da articolo CMJ 2001 (`Roads2001Pulsars`):**
- Cap. 4 libro: trattazione + advanced PS (multiple generators, pulsar masking, convolution con sampled sound — fig. 4.16 schema completo); descrizione PulsarGenerator (~1500 LOC SC2, fig. 4.20 GUI); applicazioni in *Clang-Tint*, *Half-life*, *Tenth/Eleventh vortex*.
- Articolo CMJ: già documentato in bibliography come `Roads2001Pulsars` — versione condensata, focus su PWM/PulWM, identificazione di alcuni tonepulses.
- **Da ingestire separatamente** `Roads2001Pulsars` per identificare delta materiale.

## Rilevanza diretta per PGE

**PGE è di tipo (4) Asynchronous + (6) Granulation of sampled (cap. 3).** Cap. 4 introduce 8+ tipi alternativi di particella che PGE *non implementa*. Questa non-implementazione è una scelta deliberata: il dominio di PGE è la granulazione di buffer audio, non la particle-synthesis-from-scratch.

**Mappature parziali:**
- **Grainlet parameter linkage (p. 125–128) ↔ PGE Envelope strategies.** Roads formalizza l'idea che ogni parametro possa essere funzione di un altro («any parameter of synthesis can be made dependent on (or linked to) any other parameter») come tecnica generativa. PGE materializza la stessa idea via `Envelope` strategies + `ParameterOrchestrator`: density, pitch, pan, pointer-position possono essere envelope time-varying o stocastici legati ad altri parametri (vedi `pge/parameter-orchestrator.md`). PGE eredita il principio del parameter linkage senza adottare il vocabolario «grainlet».
- **Pulsar graph (p. 144, fig. 4.14) ↔ partitura grafica PGE.** Il pulsar graph plotta rate-di-emissione vs tempo con asse Y a scala mista (note values + frequenze). È *esattamente* un precedente notazionale per la partitura PGE (asse X = tempo, asse Y = parametro continuo legato all'emissione). La differenza: pulsar graph plotta *rate* (parametro di controllo), partitura PGE plotta *posizione-buffer* (parametro di stato di lettura). Entrambi però rinunciano all'asse Y = frequenza canonico.
- **Pulsar masking burst/channel/stochastic ↔ DensityController + envelope sull'amplitude.** Roads articola tre meccanismi per modulare la regolarità di un pulsar train; PGE può ottenere effetti analoghi via `DensityController` distribution sincrona/asincrona/blend + amplitude envelope per zero-out di intervalli. Non c'è una primitiva «mask» dedicata.
- **Particle cloning + transient drawing ↔ asse Y partitura.** Entrambe le tecniche operano disegnando/clonando particelle in waveform editor sul piano *tempo-domain*. La partitura PGE rappresenta lo stesso tipo di operazione (selezione di porzione di buffer + replica) ma a livello di metadata, non di waveform editing diretto.

**Differenze critiche da preservare nel paper CIM:**
- PGE non genera waveform da zero (no glisson, no pulsar, no FOF/Vosim/WF, no abstract/physical models); estrae waveform da buffer audio. Questa è una scelta architetturale che limita PGE al sotto-dominio di Roads cap. 5 (transformation), non cap. 4 (particle synthesis from-scratch).
- PGE è offline; le tecniche di cap. 4 sono prevalentemente real-time (PulsarGenerator, MetaSynth, Creatovox, FOF in Csound).
- PGE non ha graphic input (no UPIC, no Phonogramme, no MetaSynth); ha graphic *output* (score_visualizer mostra il risultato della sintesi, non lo specifica).

**Pulsar graph (p. 144) come legittimazione storica della partitura PGE.** Roads scrive: «Such a *pulsar graph* can serve as an alternative form of notation for one dimension of rhythmic structure, namely the onset time of events. The correspondence between the musical units of rhythmic structure (note values, tuplets, rests, etc.) and the vertical or frequency scale can be made clear by plotting note values on the vertical or frequency scale.» (p. 144) Roads articola il principio (asse Y = parametro di controllo, non frequenza canonica); PGE 2026 lo materializza con asse Y = posizione-buffer.

## Collegamento alla tesi centrale

**Loop lungo (Atto 3).** Cap. 4 mostra l'estensione del paradigma microsound oltre il grano gaussiano classico — un'estensione che è avvenuta *durante* la fase di convergenza real-time degli anni 1990–2000s. PulsarGenerator (~1500 LOC SC2, fig. 4.20) è esempio paradigmatico: real-time, gestural, GUI con sliders per envelope. PGE 2026 prende dalla famiglia delle *granular sample-based* (cap. 5 Roads) e rinuncia esplicitamente alle particelle from-scratch.

**Contributo (1) DSL+LSP.** Quote p. 121: «*The engines of particle synthesis are not especially complicated. It is the combination of many simple elements that forms a complex time-varying sound. We shape the sound's evolution by controlling this combination from a high musical level. High-level controls imply the existence of algorithms that can interpret a composer's directives, translating them into low-level particle specifications.*» Roads articola il pattern *high-level musical control → low-level particle specifications* esattamente come progettato in PGE: YAML musicalmente leggibile → ParameterOrchestrator → grain-level data per Csound/NumPy renderer. Citazione di apertura cap. 4 utilizzabile in sez. 3 paper CIM (architettura).

**Contributo (2) Partitura grafica.** Pulsar graph p. 144 + fig. 4.14 sono il **più diretto precedente concettuale** della partitura grafica PGE nel libro Microsound. Roads disegna note-values su asse Y, PGE disegna buffer-position. Stessa mossa concettuale: rinunciare all'asse Y = frequenza per un parametro più informativo per la tecnica specifica.

**Contributo (3) STEMS workflow.** Pulsar synthesis p. 156: «A final stage of pulsar composition is to merge multiple trains to form a composite texture. This is a question of montage, and is best handled by editing and mixing software designed for this purpose. Each layer of the texture may have its own rhythmic pattern, choice of convolved objects, and spatial path.» — esattamente l'argomento per per-stream rendering + mixing successivo (STEMS PGE).

## Quote chiave

> «The engines of particle synthesis are not especially complicated. It is the combination of many simple elements that forms a complex time-varying sound. We shape the sound's evolution by controlling this combination from a high musical level. High-level controls imply the existence of algorithms that can interpret a composer's directives, translating them into low-level particle specifications.» (p. 121)

> «The fundamental notion of grainlet synthesis is that any parameter of synthesis can be made dependent on (or linked to) any other parameter. One is not, for example, limited to an interdependence between frequency and duration.» (p. 125)

> «Such a *pulsar graph* can serve as an alternative form of notation for one dimension of rhythmic structure, namely the onset time of events. The correspondence between the musical units of rhythmic structure (note values, tuplets, rests, etc.) and the vertical or frequency scale can be made clear by plotting note values on the vertical or frequency scale.» (p. 144)

> «Pulsar synthesis offers a seamless link between the time scales of individual particle rhythms, periodic pitches, and the meso or phrase level of composition.» (p. 157)

> «A final stage of pulsar composition is to merge multiple trains to form a composite texture. This is a question of montage, and is best handled by editing and mixing software designed for this purpose. Each layer of the texture may have its own rhythmic pattern, choice of convolved objects, and spatial path.» (p. 156)

> «In effect, the composer works in a manner similar to a Pointillist painter such as Georges Seurat, building an image from thousands of tiny brush strokes. In Seurat's later paintings (for example, *La Luzerne, Saint-Denis*) the particles can be scattered within dense masses. When one of these particles appears isolated by silence, its singularity conveys a striking impact.» (p. 171)

## Sezioni del paper CIM 2026 dove citare

- **Sezione 2 (Sintesi granulare).** Tabella 4.4 (p. 177) come riferimento panoramico per la varietà di particle types — citare ai margini per delimitare il dominio PGE (granular sampled, *non* particle-synthesis-from-scratch). Quote p. 125 (parameter linkage grainlet) come radice concettuale degli `Envelope` strategies di PGE.
- **Sezione 3 (Architettura PGE).** Quote p. 121 (high-level controls → low-level particle specifications) come razionale della pipeline DSL→ParameterOrchestrator→renderer.
- **Sezione 4 (Partitura grafica).** Pulsar graph p. 144 + fig. 4.14 come **precedente notazionale diretto** dell'asse Y non-frequenza. Confronto con UPIC/Phonogramme/MetaSynth come esempi di *graphic input* (PGE inverte: graphic *output* dello score_visualizer).
- **Sezione 5 (Caso compositivo).** Quote p. 156 (montage / editing & mixing per pulsar trains) come legittimazione storica del workflow STEMS PGE. Riferimenti a *Half-life* (1998–99) e *Tenth/Eleventh vortex* (2000–01) come esempi di Roads che usa pulsar offline + sound editor (workflow vicino al loop lungo PGE).
- **Sezione 1 (Introduzione).** Quote p. 171 (analogia Pointillist Seurat) come immagine evocativa del lavoro al microsound — eventualmente in apertura.
