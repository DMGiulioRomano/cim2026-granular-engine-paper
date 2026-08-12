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
   - **Presets / Sound objects** (set di valori salvati richiamabili) ↔ blocchi YAML riutilizzabili: stream come unità riusabili nel `Generator`.
   - **Ramps** (cambio nel tempo a rate predefinito) ↔ `Envelope` PGE (tempo-varying lineare/curva su qualsiasi parametro).
   - **Tendency masks** (area visiva con range stocastico) ↔ pair `Parameter + range` con `deviation_probability` (range stocastico configurabile per parametro e per istante via `EnvelopeGate`).
   - **Score** (sequenza di sound objects in tempo) ↔ documento YAML complessivo (lista di stream con onset assoluti).

   `StreamConfig` (`time_mode`, `distribution_mode`, `deviation_probability`, `range_always_active`, `time_scale`) non ha analogo diretto in Fig. 3: è meta-livello sul **come** interpretare i parametri, più vicino alle opzioni globali del programma GSX/GSAMX/GRMSKX (scelta modello AS/FM/SAM, sample rate) che ai control variables.

   Truax la presenta come "absolutely necessary"; PGE ne dà una formalizzazione dichiarativa scritta in YAML invece che vincolata a comandi di tastiera live.

3. **Tendency masks come overlay ASCII (Fig. 4)** — Truax mostra una schermata terminale a 24 righe in cui frequency mask (`*`), duration mask (`-`), amplitude envelope (`+`) e delay envelope (`/`) sono sovrapposti su asse tempo (`==T==`). È il **primo precedente concreto di una rappresentazione visiva multi-parametro nel tempo per controllo granulare**, antecedente diretto e più specifico del `score_visualizer.py` PGE: Roads (1978, 1988) parla di poligoni su piano frequenza/tempo come metafora; Truax 1988 implementa l'overlay multi-traccia. PGE inverte il segno (output visivo delle decisioni invece di input visivo del controllo) e cambia asse Y (posizione-buffer invece di parametro). Per il lineage completo delle rappresentazioni visive granulari cfr. [[graphic-score]].

4. **GSAMX granulating sampled sound: due modalità** — (a) segmento fisso 4032 campioni in memoria DMX, con offset variabile e direzione di lettura (Fig. 2a); (b) stream continuo su delay-line/memoria circolare con offset rispetto a "current time" (Fig. 2b). PGE implementa la modalità (a) tramite `PointerController` (loop statico/dinamico su buffer caricato); la modalità (b) richiede ingresso real-time, fuori scope per architettura deferred-time. La separazione concettuale duration/offset/range introdotta da Truax è ricalcata negli attributi `pointer.start`, `pointer.range`, `loop_*` di PGE.

## Collegamento alla tesi centrale

Truax 1988 è l'**Atto 2** della narrazione storica di PGE: il momento in cui il vincolo hardware cade e il real-time diventa disponibile. La citazione chiave è programmatica: *"The key is to abandon linear modes of compositional thinking, which result in deterministic output (e.g., score or sequencer driven), and to substitute process-oriented multitask strategies for real-time execution."* (p. 19) Il «abandon linear modes» riguarda il **modo operativo** — processo multitask real-time contro output deterministico score/sequencer-driven.

**Correzione del maestro (2026-05-28, cfr. [[incontro-maestro-2026-05-28]]):** non leggere l'adozione del non-determinismo statistico come cambio di paradigma *compositivo*. È **economia di mezzi** — l'unico modo di governare 1000–2000 grani/sec, dati che gli «score editors... are usually so large that they are impractical to handle» (p. 14); «Given the enormous amount of data involved in specifying thousands of events per second, powerful control strategies are required» (p. 19). Truax stesso progetta la macro-struttura: in *Riverrun* «the superimposition of many similar and spectrally related subevents produces a clearly defined and controllable macro-level texture», mentre «the presence of any particular frequency component at the micro-level... can only be statistically determined» (pp. 24–25). Macro deterministico-progettato + micro statistico; la tendency mask è esplicitamente «a continuum between deterministic and stochastic choices» (p. 23), non randomness pura. Cfr. [[tendency-mask]], [[deferred-time-tradition]].

PGE risponde a questa posizione compiendo il percorso inverso: sceglie il loop lungo (tempo differito) nel momento in cui il loop stretto è disponibile. La risposta non è una critica a Truax — è una postura compositiva diversa, situata in un momento diverso (composizione che coincide con studio della tecnica). Il "linear thinking" che Truax abbandona è il sequencer deterministico; il YAML di PGE non è quello: è un DSL di intenzioni parametriche che il motore traduce nella IR (lo Stream dichiarativo) e poi materializza attraverso processi stocastici, più vicino alle tendency masks di Truax che a uno score Csound.

Sul piano tecnico, Truax 1988 rimane la spina dorsale architetturale di PGE: gerarchia Fig. 3 mappata in YAML, Tabella 1 psychoacoustic correlates come obiettivo del loop lungo, pattern front-end DMX-1000 come precedente del pattern `generator.py` → renderer. La partitura grafica PGE risponde direttamente a Fig. 4: stesso problema (visualizzare parametri nel tempo), soluzione invertita (output analitico vs input di controllo) e asse Y diverso (posizione-buffer vs parametro).

## Sezioni del paper CIM 2026 dove citare

- **`sec:griglia` + `sec:deviazione`** (primaria): modello sincrono/asincrono
  della griglia; tendency mask come meccanismo della deviazione per grano.
- **`sec:tradizione`** (secondaria): genealogia (primo sistema real-time
  documentato); Fig. 4 come precursore concreto della partitura (proposta 2),
  cfr. candidatura in [[graphic-score]].

Fonte di verità: [[mappa-citazioni-paper]].

## Quote chiave
- "Two problems that must be solved for the effective use of granular synthesis are generating the large amount of data required to specify the sound, since typically 1000–2000 grains/second can be involved, and designing the control variables required to give the musician a powerful means to link the lower-level data to macro-level compositional strategies and gestures." (p. 14)
- "Each of the control variables cited previously have a psychoacoustic correlate that may be more suggestive as a basis for compositional organization than the numerical values of each variable (Table 1)." (p. 18)
- "The key is to abandon linear modes of compositional thinking, which result in deterministic output (e.g., score or sequencer driven), and to substitute process-oriented multitask strategies for real-time execution." (p. 19)
- "The tendency mask, being inherently a visual control method, presents a visual image of the control shape based on the limiting values within which choices are made. The tendency mask suggests gestures, whereas the pair of changing numerical parameters suggests on-going processes." (p. 23)
- "Given the enormous amount of data involved in specifying thousands of events per second, powerful control strategies are required to make this synthesis technique effective for the composer." (p. 19) — razionale *economia di mezzi*
- "The width of the mask at any point determines the range of choices available, thereby providing a continuum between deterministic and stochastic choices." (p. 23) — tendency mask come continuum, non randomness
- "The superimposition of many similar and spectrally related subevents produces a clearly defined and controllable macro-level texture. The presence of any particular frequency component at the micro-level, however, can only be statistically determined." (pp. 24–25) — macro progettato + micro statistico (*Riverrun*)

## Architettura espositiva

> Sezione opzionale — modello stilistico per il paper CIM 2026. Cfr. [[modelli-stilistici-bottom-up]].

- **Apertura** (p. 14): genealogia compressa in 2 frasi (Gabor/Xenakis/Roads) → immediatamente il **problema** (complessità di calcolo → non-real-time → «few composers have worked with the technique») → soluzione DSP → scope dell'articolo + proprio brano *Riverrun*. Apertura **problem-driven, sistema-first**: il quadro storico è strumentale al problema, non tesi premessa.
- **Ordine sezioni**: Introduction → A Granular Synthesis Implementation (i due problemi) → GSX/GSAMX Programs (modelli AS/FM/SAM) → Control Variables → Psychoacoustic Variables [Table 1] → Compositional Control Strategies [Fig. 3] → Real-Time User Controls → Ramps → Envelope Shape → Presets and Objects → Ramp Files → Tendency Masks (GRMSKX) [Fig. 4] → Musical Applications → Future Directions → References. **Build dal basso**: grano/envelope → modelli → variabili di controllo → gerarchia → forma macro → applicazioni musicali.
- **Prima figura / diagramma di sistema**: Fig. 1 (grain envelopes) presto, dentro i modelli (p. 15). Il **diagramma di sistema** (Fig. 3, gerarchia dei controlli) compare **tardi** (p. 20), dopo aver introdotto le variabili — non in apertura.
- **Lit-review**: distribuito, mai sezione propria. Genealogia 2 frasi in apertura; teoria percettiva (McAdams & Bregman 1979, MacKay 1984, Olson 1967) concentrata in *Musical Applications* (tardi); fitta auto-citazione (Truax 1977–1987).
- **Implicazioni teorico-musicali**: in *Musical Applications*, **verso la fine** — analisi di *Riverrun*, stochastic texture, metafora del fiume, «a different mode of listening». Emergono *dopo* l'esposizione tecnica.
- **Densità ref**: ~22 ref / ~12 pp ≈ 1.8/pp; forte auto-citazione, mix foundational + percettivo + DSP + tangenziale.
- **Chiusura**: doppia — *Musical Applications* (estetica/percettiva) seguita da *Future Directions* (tecnica). Chiude su implicazioni musicali **e** sviluppi tecnici.
- **Lezione per CIM 2026**: modello bottom-up forte — aprire col problema (controllo del volume di dati / esposizione parametrica), costruire dal sistema, collocare le implicazioni compositive alla fine; diagramma di sistema non in apertura ma dopo i mattoni.
