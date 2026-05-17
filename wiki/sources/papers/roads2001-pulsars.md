# [Roads, 2001] Sound Composition with Pulsars

## Citazione CIM

Roads, C. (2001). Sound Composition with Pulsars. *Journal of the Audio Engineering Society*, 49(3), 134–147.

## Argomento centrale

Pulsar Synthesis (PS) come tecnica di sintesi a particelle: stream di pulsar — ciascun pulsar = pulsaret waveform `w` di durata `d` seguito da silenzio `s`, periodo `p = d + s`, con due frequenze indipendenti `fp = 1/p` (fundamental, 1 Hz – 5 kHz) e `fd = 1/d` (formant, 80 Hz – 10 kHz). Variando `fp` attraverso la soglia infrasonica/audio (≈20 Hz) lo stream attraversa con continuità il continuum *ritmo ↔ tono*. Roads ne descrive teoria base, modello avanzato (pulsar masking, multiple pulsar generators, convoluzione con campioni), implementazione PulsarGenerator (SuperCollider 2, con Alberto de Campo, 1999), e applicazioni compositive (*Clang-tint* 1994/95, *Half-life* 1998/99, *Tenth Vortex* 2000, *Eleventh Vortex* 2001).

## Gap o problema identificato

Le tecniche analogiche classiche di filtered pulse trains (Stockhausen, Koenig anni '50) mancavano di «*precise programmable control, waveform flexibility, graphical interface, and extensibility*» (p. 134). PS si presenta come digitalizzazione moderna di quella eredità, dove il problema esplicito è lo spazio di controllo *fine-grained per parametro* — ogni pulsar generator ha 7 parametri (`train duration`, `fp`, `fd`, `w`, `v`, `a`, `s`) controllati da *envelope curves separate that span a train of pulsars*.

## Rilevanza diretta per PGE

Tre punti di contatto strutturali, tutti incentrati sul *controllo parametrico via envelope*:

1. **Envelope-per-parametro come architettura di controllo** (pp. 139, 141, Fig. 7 schema e Fig. 11 GUI): PulsarGenerator espone un pannello di ~15 envelope editor — uno per ciascun parametro di sintesi (`fundFreq`, `pulseMask`, `pulsaret`, `pulseEnv`, `formfreq1–3`, `amp1–3`, `pan1–3`). La struttura uno-envelope-per-parametro è la stessa logica architetturale di `ParameterOrchestrator` + `Envelope`/`Controller` PGE; PGE generalizza spostando la specifica dal pannello grafico real-time alla dichiarazione YAML versionata.

2. **Pulsar graph (Fig. 5a) come notazione di rhythm** (p. 137): grafo bidimensionale con asse Y = rate of pulsar emission (note values traditional sulla sinistra, frequencies in Hz sulla destra) e asse X = tempo. Roads esplicitamente: «*This pulsar graph can serve as an alternative form of notation for one dimension of rhythmic structure, namely the onset time of events*». Polo cugino dello `score_visualizer` PGE — entrambi traducono una funzione temporale di un parametro granulare in una rappresentazione grafica leggibile; differenza di scope: pulsar graph rappresenta un solo parametro (`fp`), score_visualizer PGE rappresenta posizione-buffer + pitch ratio + density + envelope ampiezza per-grano simultaneamente.

3. **Polo opposto compositivo (real-time gestural)**: l'ultima sezione *Composing with Pulsars* (pp. 142–143) descrive il workflow PulsarGenerator come iterazione real-time — «*the composer can save various settings and plan how these will be used within a composition. The PulsarGenerator program can also record the sounds produced in a real-time session. This session can be edited by the composer and possibly convolved or mixed with other material*». Notare la *parziale* sovrapposizione con il loop lungo PGE: anche qui esiste un ciclo di iterazione, ma il *primato* è del gesto sul piano grafico, non della riscrittura della specifica testuale. Polo opposto, stessa famiglia di problemi.

## Collegamento alla tesi centrale

Conferma per via di precursore concreto il differenziatore 1 (DSL via envelope/automation). Roads dichiara esplicitamente (Fig. 11 e p. 142) che il workflow compositivo *real-time-driven* di PulsarGenerator richiede comunque una infrastruttura di *envelope time-varying per parametro*: l'envelope è già nel 2001 il punto di articolazione tra gesto e specifica. Il ritorno volontario di PGE al deferred non scarta questa infrastruttura ma la *recupera* sostituendo il pannello grafico real-time con la dichiarazione testuale YAML — la specifica diventa cosa scritta, versionata, leggibile, e il visualizer ne è l'output ispezionabile invece dell'input gestural. Polo opposto sulla superficie compositiva (testo vs. gesto), stessa anatomia di controllo (envelope-per-parametro).

## Sezioni del paper CIM 2026 dove citare

- **Sezione 2** (sintesi granulare: panorama tecniche): PS come ramo *particle synthesis* parallelo alla granulazione di campioni, citata per indicare l'estensione del paradigma Gabor oltre il grano gaussiano (cfr. Microsound cap. 4 già ingestito).
- **Sezione 3** (architettura PGE — DSL): citare il pannello envelope di PulsarGenerator (Fig. 11) come precursore visivo concreto del concetto «*envelope-per-parametro*» che PGE materializza via YAML + `Envelope`/`Controller`.
- **Sezione 4** (partitura grafica): citare il *pulsar graph* (Fig. 5a) come notazione precursore (alternativa di rhythm) — utile per posizionare lo `score_visualizer` PGE in una linea di rappresentazioni grafiche che precedono il piano frequenza/tempo classico.

## Quote chiave

- p. 134: «*Pulsar synthesis belongs to a larger family of microsonic or particle synthesis techniques, of which is granular synthesis [11]–[18]. These techniques stream or scatter acoustic particles in myriad patterns to produce time-varying sounds.*»
- p. 137: «*This pulsar graph can serve as an alternative form of notation for one dimension of rhythmic structure, namely the onset time of events. The correspondence between the musical units of rhythmic structure (such as note values, tuplets, rests) can be made clear by plotting note values on the vertical or frequency scale.*»
- p. 142: «*The PulsarGenerator program can also record the sounds produced in a real-time session. This session can be edited by the composer and possibly convolved or mixed with other material.*» — workflow ibrido: real-time + post-produzione offline, antesignano del workflow STEMS PGE su scala diversa.
- p. 142 (conclusioni musicali): «*The electronic sound palette is based on pulsar synthesis in multiple forms: pulsating blips, elongated formant tones, and clouds of asynchronous pulsars. For the latter, I first generated multiple infrasonic pulsar trains, each one beating at a different frequency in the range of 6 to 18 Hz. I then mixed these together to obtain the asynchronous pulsar cloud.*» — composizione per layering offline di stream con parametri distinti, pattern compositivo analogo allo STEMS PGE.
