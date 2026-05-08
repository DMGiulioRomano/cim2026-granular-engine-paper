# [Truax, 1988] Real-Time Granular Synthesis with a Digital Signal Processor

## Citazione CIM
Truax, B. (1988). Real-Time Granular Synthesis with a Digital Signal Processor. *Computer Music Journal*, 12(2), 14–26.

## Argomento centrale
Descrizione tecnica completa del primo sistema di sintesi granulare interamente real-time documentato (DMX-1000 DSP controllato da PDP Micro 11), in tre programmi (GSX, GSAMX, GRMSKX) che implementano tre modelli di unit grain (Additive Synthesis, Frequency Modulation, Sampling). Articola la gerarchia di controllo compositivo da grano a forma macro (Fig. 3: Control variables → Presets → Ramps → Ramp file/Tendency masks → Score) e introduce la mappatura canonica parametro → correlato psicoacustico (Tabella 1).

## Gap o problema identificato
"Two problems that must be solved for the effective use of granular synthesis are generating the large amount of data required to specify the sound, since typically 1000–2000 grains/second can be involved, and designing the control variables required to give the musician a powerful means to link the lower-level data to macro-level compositional strategies and gestures." (p. 14)

Truax circoscrive il problema in due tronconi: (a) generare la massa di dati grano-per-grano e (b) progettare un linguaggio di controllo che colleghi micro-evento e gesto compositivo. Nota inoltre che gli editor di score offline producono file "impractical to handle"; il real-time DSP è la sua scommessa per superare l'impraticabilità.

## Rilevanza diretta per PGE
Truax 1988 è il documento tecnico fondativo della tradizione che PGE estende al tempo differito. Quattro corrispondenze dirette:

1. **Tabella 1 (psychoacoustic correlates)** — Truax mappa center frequency → average pitch, frequency range → bandwidth (pitch → noise), average duration → density (audio rate fusion → discrete events), duration range → modulation (periodic AM → random), delay → secondary density/modulation. È mappatura **documentale**: ogni control variable ha correlato percettivo esplicito al livello della prosa, non del codice. PGE ricalca questa filosofia in **due punti specifici**, non come principio sistemico: (a) `FillFactorStrategy` vs `DirectDensityStrategy` (controllo percettivo "riempimento" vs controllo numerico "grani/sec") e (b) `DensityController` distribuzione sincrona/asincrona/blend (`distribution` come Envelope per morphing tra audio-rate fusion e discrete events — direttamente l'asse Truax durata→densità). Il resto del `ParameterOrchestrator` è layer di gestione (Parameter + ProbabilityGate + range stocastico + gruppi esclusivi) senza semantica psicoacustica codificata.

2. **Gerarchia compositiva Fig. 3** — `Score → Presets → Ramp file → Ramps → Tendency masks → Control variables`. PGE replica questa gerarchia in contesto YAML, con mappature non bijettive:
   - **Control variables** (parametri grano-per-grano in Truax: center freq, freq range, avg dur, dur range, delay) ↔ in PGE i parametri assegnati come attributi di `Stream` da `ParameterOrchestrator` (`grain_duration`, `volume`, `pan`, `reverse`) e i parametri gestiti dai Controller (`PitchController`, `PointerController`, `DensityController`, `WindowController`). **Non** corrispondono a `StreamConfig`, che è layer meta (regole di processo).
   - **Presets / Sound objects** (set di valori salvati richiamabili) ↔ blocchi YAML riutilizzabili: stream e cartridge come unità riusabili nel `Generator`.
   - **Ramps** (cambio nel tempo a rate predefinito) ↔ `Envelope` PGE (tempo-varying lineare/curva su qualsiasi parametro).
   - **Tendency masks** (area visiva con range stocastico) ↔ pair `Parameter + range` con `dephase` (range stocastico configurabile per parametro e per istante via `EnvelopeGate`).
   - **Score** (sequenza di sound objects in tempo) ↔ documento YAML complessivo (lista di stream con onset assoluti).

   `StreamConfig` (`time_mode`, `distribution_mode`, `dephase`, `range_always_active`, `time_scale`) non ha analogo diretto in Fig. 3: è meta-livello sul **come** interpretare i parametri, più vicino alle opzioni globali del programma GSX/GSAMX/GRMSKX (scelta modello AS/FM/SAM, sample rate) che ai control variables.

   Truax la presenta come "absolutely necessary"; PGE ne dà una formalizzazione dichiarativa scritta in YAML invece che vincolata a comandi di tastiera live.

3. **Tendency masks come overlay ASCII (Fig. 4)** — Truax mostra una schermata terminale a 24 righe in cui frequency mask (`*`), duration mask (`-`), amplitude envelope (`+`) e delay envelope (`/`) sono sovrapposti su asse tempo (`==T==`). È il **primo precedente concreto di una rappresentazione visiva multi-parametro nel tempo per controllo granulare**, antecedente diretto e più specifico del `score_visualizer.py` PGE: Roads (1978, 1988) parla di poligoni su piano frequenza/tempo come metafora; Truax 1988 implementa l'overlay multi-traccia. PGE inverte il segno (output visivo delle decisioni invece di input visivo del controllo) e cambia asse Y (posizione-buffer invece di parametro).

4. **GSAMX granulating sampled sound: due modalità** — (a) segmento fisso 4032 campioni in memoria DMX, con offset variabile e direzione di lettura (Fig. 2a); (b) stream continuo su delay-line/memoria circolare con offset rispetto a "current time" (Fig. 2b). PGE implementa la modalità (a) tramite `PointerController` (loop statico/dinamico su buffer caricato); la modalità (b) richiede ingresso real-time, fuori scope per architettura deferred-time. La separazione concettuale duration/offset/range introdotta da Truax è ricalcata negli attributi `pointer.start`, `pointer.range`, `loop_*` di PGE.

## Collegamento alla tesi centrale

Truax 1988 è l'**Atto 2** della narrazione storica di PGE: il momento in cui il vincolo hardware cade e il tempo differito viene deliberatamente abbandonato. La citazione chiave è programmatica: *"The key is to abandon linear modes of compositional thinking, which result in deterministic output (e.g., score or sequencer driven), and to substitute process-oriented multitask strategies for real-time execution."* Truax teorizza il real-time non solo come possibilità tecnica ma come cambio di paradigma compositivo — il loop di feedback stretto come liberazione dalla partitura pre-scritta.

PGE risponde a questa posizione compiendo il percorso inverso: sceglie il loop lungo (tempo differito) nel momento in cui il loop stretto è disponibile. La risposta non è una critica a Truax — è una postura compositiva diversa, situata in un momento diverso (composizione che coincide con studio della tecnica). Il "linear thinking" che Truax abbandona è il sequencer deterministico; il YAML di PGE non è quello: è una IR di intenzioni parametriche che il motore traduce attraverso processi stocastici, più vicino alle tendency masks di Truax che a uno score Csound.

Sul piano tecnico, Truax 1988 rimane la spina dorsale architetturale di PGE: gerarchia Fig. 3 mappata in YAML, Tabella 1 psychoacoustic correlates come obiettivo del loop lungo, pattern front-end DMX-1000 come precedente del pattern `generator.py` → renderer. La partitura grafica PGE risponde direttamente a Fig. 4: stesso problema (visualizzare parametri nel tempo), soluzione invertita (output analitico vs input di controllo) e asse Y diverso (posizione-buffer vs parametro).

## Sezioni del paper CIM 2026 dove citare

- Sezione 1 (Introduzione): citazione "abandon linear modes" come formulazione della postura real-time a cui PGE risponde consapevolmente con il loop lungo
- Sezione 2 (Contesto teorico): Tabella 1 psychoacoustic correlates come obiettivo empirico del loop lungo; gerarchia Fig. 3 come schema canonico del controllo gerarchico
- Sezione 3 (Architettura): pattern front-end (PDP Micro 11) → DSP engine (DMX-1000) come precedente architetturale; Stream ispirato a DMX-1000
- Sezione 4 (Partitura grafica): Fig. 4 (overlay tendency masks) come precursore — confronto input/output e asse Y diverso

## Quote chiave
- "Two problems that must be solved for the effective use of granular synthesis are generating the large amount of data required to specify the sound, since typically 1000–2000 grains/second can be involved, and designing the control variables required to give the musician a powerful means to link the lower-level data to macro-level compositional strategies and gestures." (p. 14)
- "Each of the control variables cited previously have a psychoacoustic correlate that may be more suggestive as a basis for compositional organization than the numerical values of each variable (Table 1)." (p. 18)
- "The key is to abandon linear modes of compositional thinking, which result in deterministic output (e.g., score or sequencer driven), and to substitute process-oriented multitask strategies for real-time execution." (p. 19)
- "The tendency mask, being inherently a visual control method, presents a visual image of the control shape based on the limiting values within which choices are made. The tendency mask suggests gestures, whereas the pair of changing numerical parameters suggests on-going processes." (p. 23)
