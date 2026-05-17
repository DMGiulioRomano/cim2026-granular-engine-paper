# Operations Log

Log append-only. Ogni entry: `## [YYYY-MM-DD] <tipo> | <titolo>`.
Tipi: `ingest`, `query`, `lint`, `restructure`.

---

## [2026-05-04] ingest | CIM Proceedings (23 volumi, 1976–2024)

Fonte: `raw/proceedings/` — `pdftotext` su tutti i PDF, ricerca su radice `granul`.
Output: `wiki/sources/proceedings/cim-survey.md`
Pagine toccate: 1 nuova.
Sintesi: trovati articoli dedicati alla sintesi granulare in 12 dei 23 volumi CIM.
Confronto con PGE documentato nella sezione "tempo differito" del survey.

---

## [2026-05-05] ingest | generator.md — Generator, pipeline YAML→SCO

Fonte: `raw/PythonGranularEngine/src/core/generator.py` + `graph/class_diagram.puml`
Output: `wiki/sources/pge/generator.md`
Contenuto: orchestratore principale, logica solo/mute, eval matematica, build incrementale.

---

## [2026-05-05] ingest | stream.md — Stream / StreamConfig / StreamContext

Fonte: `raw/PythonGranularEngine/src/core/stream.py` + `stream_config.py`
Output: `wiki/sources/pge/stream.md`
Contenuto: nucleo sintesi granulare, algoritmo multi-voce, generate_grains(), ispirazione DMX-1000.

---

## [2026-05-05] ingest | score-visualizer.md — ScoreVisualizer

Fonte: `raw/PythonGranularEngine/src/rendering/score_visualizer.py`
Output: `wiki/sources/pge/score-visualizer.md`
Contenuto: partitura grafica, encoding frecce, loop mask, envelope panel, paginazione A3.

---

## [2026-05-05] ingest | stream-cache-manager.md — StreamCacheManager

Fonte: `raw/PythonGranularEngine/src/rendering/stream_cache_manager.py`
Output: `wiki/sources/pge/stream-cache-manager.md`
Contenuto: cache SHA-256 per build incrementale Csound, dirty detection, garbage collect.

---

## [2026-05-05] ingest | parameter-orchestrator.md — ParameterOrchestrator + Strategie

Fonte: `raw/PythonGranularEngine/src/parameters/parameter_orchestrator.py` + `strategies/strategie.py`
Output: `wiki/sources/pge/parameter-orchestrator.md`
Contenuto: DSL parametrico, ExclusiveGroupSelector, GateFactory, dephase, FillFactor vs DirectDensity.

---

## [2026-05-05] ingest | renderer.md — CsoundRenderer / NumpyAudioRenderer / ReaperProjectWriter

Fonte: `raw/PythonGranularEngine/src/rendering/csound_renderer.py` + `numpy_audio_renderer.py` + `reaper_project_writer.py`
Output: `wiki/sources/pge/renderer.md`
Contenuto: tre renderer, pattern OCP, overlap-add NumPy, STEMS vs MIX, export Reaper.

---

## [2026-05-05] ingest | pointer-controller.md — PointerController

Fonte: `raw/PythonGranularEngine/src/controllers/pointer_controller.py`
Output: `wiki/sources/pge/pointer-controller.md`
Contenuto: posizione testina nel buffer, speed_ratio (costante o Envelope con integrazione), loop statico vs dinamico, phase accumulator inerziale, deviazione per-grano. Risolve open question di stream.md su time_mode:normalized (avviene in _pre_normalize_loop_params prima del pipeline).

---

## [2026-05-05] ingest | voice-manager.md — VoiceManager

Fonte: `raw/PythonGranularEngine/src/controllers/voice_manager.py`
Output: `wiki/sources/pge/voice-manager.md`
Contenuto: VoiceConfig (frozen dataclass, 4 offset dimensionali), voice-0 invariant, 4 strategie ortogonali, layering a 3 livelli (base controller + voice strategy + grain jitter), pan_spread come Envelope.

---

## [2026-05-05] ingest | density-controller.md — DensityController

Fonte: `raw/PythonGranularEngine/src/controllers/density_controller.py`
Output: `wiki/sources/pge/density-controller.md`
Contenuto: fill_factor vs density (mutuamente esclusivi), IOT = 1/density, distribuzione Truax sincrona/asincrona/blend, distribution come Envelope per morphing texture nel tempo.

---

## [2026-05-07] lint | correzioni post-review ingestione Step 2 addendum

Fonte: comparazione wiki vs sorgenti `raw/PythonGranularEngine/src/controllers/` + `src/core/stream.py` + `src/strategies/voice_*`
Correzioni applicate:
- `density-controller.md`: pseudocodice "Ruolo" rimpiazzato con scatter blending reale da `Stream.generate_grains()`. Il frammento precedente mostrava solo `voice_cursors[0] += iot` senza blend multi-voce.
- `pointer-controller.md`: aggiunto step 4 in Comportamento runtime — offset `grain_reverse` (`if grain_reverse: final_pos += grain_duration`) prima del wrap finale.
- `stream.md`: pipeline aggiornata con `_init_grain_reverse()` step separato (avviene prima di ParameterOrchestrator). Attributi `num_voices`/`scatter` corretti: sono `_num_voices`/`_scatter` privati gestiti da `_init_voice_manager()`, non da ParameterOrchestrator.

---

## [2026-05-07] lint | verifica accuracy density-controller, voice-manager, pointer-controller

Fonte: sorgenti `raw/PythonGranularEngine/src/controllers/` + `raw/.../strategies/voice_*`
Correzioni applicate:
- `density-controller.md`: pseudocodice `_apply_truax_distribution` aveva 3 rami; codice reale ha 2 (`<= 0.0` / `else`). Nessun ramo speciale per dist==1.0.
- `voice-manager.md`: conteggio accordi 21→22 (alterato conteggio errato). `StochasticPitchStrategy` e `StochasticPointerStrategy`: range cache `[-1,1]`, offset può essere negativo.
- `pointer-controller.md`: reset loop dinamico incompleto — aggiunto caso backward (`delta_pos < 0` → reset a `loop_end - 1e-9`).
Nessuna modifica strutturale. Pagine rimanenti verificate come accurate.

---

## [2026-05-07] lint | verifica copertura post-review collega

Fonte: analisi diff git dei file modificati nel commit Step 2 addendum
Correzioni applicate:
- `stream.md`: open question `scatter` marcata risolta con riferimento a density-controller.md (algoritmo già documentato lì dal lint precedente).
- `stream.md`: newline mancante a fine file.

---

## [2026-05-07] ingest | truax1990.md — Composing with Real-Time Granular Sound

Fonte: `raw/papers/Truax_1990_Composing-with-Real-Time-Granular-Sound.pdf`
Output: `wiki/sources/papers/truax1990.md`
Contenuto: gerarchia di controllo granulare (control variables → presets/ramps → score/tendency masks), gap controllo/percezione esplicitato, tendency masks come precursore diretto del score_visualizer PGE, riposizionamento del compositore come sorgente di messaggi di controllo.
Quote chiave: "It reduces to absurdity the idea of total control by the composer. Hierarchic levels of control are absolutely necessary." (p. 131)

---

## [2026-05-08] ingest | roads1988.md — Introduction to Granular Synthesis

Fonte: `raw/papers/Roads_1988_Introduction-to-Granular-Synthesis.pdf` (Computer Music Journal 12(2), pp. 11–13)
Output: `wiki/sources/papers/roads1988.md`
Contenuto: editoriale CMJ del numero monografico granulare, definizione canonica (grani quasi-gaussiani 1–50ms, density, additive synthesis), lignaggio Gabor → Wiener → Moles → Xenakis, event a 12 parametri (begin/duration/waveform/center freq/bandwidth/density/amplitude + slope) come precursore diretto del DSL YAML PGE, scattering random per density slope = DensityController, eventi come "lines, triangles, rhomboid shapes" su piano frequenza/tempo come precedente di score_visualizer (con scarto: PGE asse Y = posizione-buffer, non frequenza).
Aggiornato `overview.md` (differenziatore 2 cita esplicitamente Roads 1988; gap rimosso).

---

## [2026-05-08] ingest | gabor1947.md — Acoustical Quanta and the Theory of Hearing

Fonte: `raw/papers/Gabor_1947_Acoustical-Quanta-and-the-Theory-of-Hearing.pdf` (*Nature*, 159(4044), pp. 591–594)
Output: `wiki/sources/papers/gabor1947.md`
Contenuto: radice teorica del paradigma granulare. Information diagram tempo×frequenza, principio di indeterminazione Δt·Δf ≥ 1, segnale elementare gaussiana × sinusoide (grano Gabor), matrice di grani come prima rappresentazione bidimensionale di un suono come collezione di quanti discreti, soglia di discriminazione dell'orecchio ≈ 1 sui dati Bürck–Kotowski–Lichte 1935 e Shower–Biddulph 1931, due meccanismi di hearing (risuonatori cocleari ~10 ms + raffinamento neurale ~250 ms) che giustificano la finestra 1–50 ms come range tipico del grano.
Aggiornato `overview.md`: nuova sezione "Radici teoriche" con Gabor come fondamento; rimosso dal gap.

---

## [2026-05-08] ingest | truax1988.md — Real-Time Granular Synthesis with a Digital Signal Processor

Fonte: `raw/papers/Truax_1988_Real-Time-Granular-Synthesis-with-a-Digital-Signal-Processor.pdf` (Computer Music Journal 12(2), pp. 14–26)
Output: `wiki/sources/papers/truax1988.md`
Contenuto: documento tecnico fondativo del primo sistema granulare interamente real-time (DMX-1000 + PDP Micro 11). Tre programmi GSX/GSAMX/GRMSKX, tre modelli unit grain (AS/FM/SAM). Quattro corrispondenze con PGE: (1) Tabella 1 psychoacoustic correlates come mappatura **documentale** ricalcata in PGE solo in punti specifici (`FillFactorStrategy` vs `DirectDensityStrategy`, distribuzione sincrona/asincrona/blend di `DensityController`); (2) gerarchia Fig. 3 (`Score → Presets → Ramps → Tendency masks → Control variables`) mappata su YAML con bijezione parziale — `StreamConfig` non corrisponde a control variables (è meta-layer); (3) Fig. 4 overlay ASCII su terminale 24-line come **primo precedente concreto** di rappresentazione visiva multi-parametro tempo-dipendente (più diretto di Roads 1978/1988 che parlano di poligoni metaforici); (4) due modalità granulating sampled sound (segmento fisso vs stream continuo) — PGE implementa la fissa.
Quote chiave: "Two problems that must be solved... generating the large amount of data... and designing the control variables required to give the musician a powerful means to link the lower-level data to macro-level compositional strategies and gestures." (p. 14)
Aggiornati: `bibliography.md` (Truax1988 ✗→✓, sezioni 1, 2, 3, 4); `index.md`; `overview.md` (rimosso da gap; differenziatore 2 esteso con Fig. 4 Truax 1988 come primo overlay multi-parametro concreto, distinto da poligoni metaforici di Roads).
Note: prima stesura conteneva due claim sovrastimati (correlato percettivo per ogni parametro DSL; StreamConfig = control variables) — corretti dopo review utente con riferimento a `parameter-orchestrator.md` e `stream.md`. Propagazione differenziatore 2 aggiunta in seconda passata di review.

---

## [2026-05-08] ingest | roads1978.md — Automated Granular Synthesis of Sound

Fonte: `raw/papers/Roads_1978_Automated-Granular-Synthesis-of-Sound.pdf` (Computer Music Journal 2(2), pp. 61–62)
Output: `wiki/sources/papers/roads1978.md`
Contenuto: AGS (Automated Granular Synthesis), prima implementazione computer documentata della sintesi granulare (B6700 ALGOL, 1975, front-end MUSIC V). Inviluppo grano gaussiano modificato (attacco gauss + sustained peak + decay gauss); event a **6 coppie valore/slope** (begin/duration/waveform/center freq/bandwidth/density/amplitude — precursore diretto del 12-param di Roads 1988 e del DSL YAML PGE); pattern *front-end → engine* identico ad architettura PGE (`generator.py` → Csound/NumPy); notazione grafica come polygon arbitrario su piano freq/tempo, con riferimento esplicito a Stockhausen *Studie II*. Limite hardware: 32 grani simultanei, 16-bit interno → 12-bit DAC.
Aggiornato `overview.md`: radici teoriche (Roads 1978 = prima implementazione computer), tabella precursori (riga 1978 inserita prima di Roads 1985), differenziatore 2 (precedente notazionale Roads 1978 + Stockhausen, prima di Roads 1988). Aggiornato `bibliography.md` colonna Wiki ✗→✓ + sezioni 1, 2, 3, 4.

---

## [2026-05-08] ingest | truax1994.md — Discovering Inner Complexity

Fonte: `raw/papers/Truax_1994_Discovering-Inner-Complexity.pdf` (Computer Music Journal 18(2), pp. 38–48)
Output: `wiki/sources/papers/truax1994.md`
Contenuto: GSAMX su DMX-1000, due estensioni rispetto al 1988 — (a) variable-rate granulation: ratio `off:on` come time-extension factor (TEF) tra fixed-sample e continuous-sample, time-stretching arbitrario senza pitch shift; (b) harmonization scheme F=4 con N variabile per voce/grano. Quattro corrispondenze PGE: (1) variable-rate = ancestor di `PointerController.speed_ratio` Envelope (TEF Truax = integrale di speed_ratio PGE); (2) asse Y partitura PGE = visualizzazione esplicita del movimento testina vs tempo descritto a parole da Truax; (3) harmonization F=4 = precedente di `VoiceManager` + `PitchController` multi-voce; (4) PGE implementa solo fixed-sample. Formulazione esplicita della **separazione micro/macro come tesi psicoacustica abilitante** del paradigma granulare: la granulazione separa micro-pattern d'onda da macro-evoluzione temporale.
Quote chiave: "By linking frequency and time at the micro level, granulation makes it possible to treat these two variables independently at the macro level" (p. 44); "Time stretching is a unique way to bring out the inner complexity of a sound" (p. 45).
Aggiornati: `bibliography.md` (Truax1994 ✗→✓, sezioni 1, 2, 4, 5); `index.md`; `overview.md` — radici teoriche estese con quote separazione micro/macro e quarta conseguenza diretta (asse Y = posizione-buffer giustificato da Truax 1994); differenziatore 2 esteso con riferimento al meccanismo variable-rate.

---

## [2026-05-08] lint | riallineamento wiki + CLAUDE.md al nuovo orientamento

Trigger: cambio tesi paper (gap controllo/percezione → loop lungo / postura tempo differito; 3 atti narrativi; 3 contributi: DSL+LSP, partitura, STEMS).

Modifiche: sezioni "Collegamento alla tesi centrale" e "Sezioni del paper CIM 2026" riformulate in `papers/{truax1994, roads1988, gabor1947}.md` e in `pge/{generator, stream, stream-cache-manager, renderer, pointer-controller, voice-manager, density-controller}.md`. Refusi puntuali: header duplicato in `papers/truax1988.md`, lista monca in `pge/parameter-orchestrator.md`. Refuso fattuale in `pge/pointer-controller.md`: pointer = asse Y partitura, non X. `bibliography.md`: Roads2021/Roads2006 sez.7→6 (sez.7 non esiste); Truax1990 sez.+4. `index.md`: descrizione truax1990 ricontestualizzata. `CLAUDE.md`: sezione "Central thesis" + "Paper structure" riscritte; schema "Collegamento alla tesi centrale" nei workflow ingest aggiornato; riferimento "Sezione 1 Problema" → "Sezione 1 Introduzione".

---

## [2026-05-08] ingest | depolipiccialli1988.md — Forme d'onda per la sintesi granulare sincrona

Fonte: `raw/papers/DePoli-Piccialli_1988_Forme-dOnda-Sintesi-Granulare-Sincrona_CIM-VII.pdf` (*Atti del VII Colloquio di Informatica Musicale*, pp. 70-74; figura p. 75)
Output: `wiki/sources/papers/depolipiccialli1988.md`
Contenuto: ramo CIM complementare alla linea Roads/Truax: sintesi granulare additiva sincrona con il periodo, orientata a suoni quasi periodici e controllo formantico dell'inviluppo spettrale. Problemi identificati: grani campionati difficili da controllare globalmente; collocazione asincrona a 10-20 ms problematica per continuita' di fase; metodi additivi formantici senza linearita' di fase soggetti a cancellazioni/interferenze. Soluzione: grani come risposte FIR passa-banda a fase lineare, tabulati e trasformati dinamicamente (passo non costante, AM, distorsione non lineare).
Aggiornati: `bibliography.md` (DePoliPiccialli1988 ✗→✓, sezioni 2, 3); `index.md`; `overview.md` (radici teoriche, tabella precursori, gap); nuova pagina concetto `wiki/concepts/sintesi-granulare-sincrona.md` per distinguere period-synchronous granular synthesis dalla distribuzione IOT sincrona/asincrona Truax/PGE.

---

## [2026-05-08] lint | review ingest depolipiccialli1988

Trigger: review post-ingest del paper De Poli/Piccialli 1988.
Modifica: in `overview.md` la sezione "Precursori diretti nella tradizione CIM" e' stata rinominata "Precursori e rami complementari nella tradizione CIM" per includere De Poli/Piccialli 1988 come ramo CIM contrastivo senza sovrastimarlo come precursore diretto di PGE.

---

## [2026-05-09] restructure | review-ingest fix — discipio1994 + roads2021

Trigger: workflow review-ingest sui due ingest 2026-05-08.
Issue 1 (page numbers DiScipio1994): paginazione PDF (p. 4, p. 8) sostituita con paginazione articolo (p. 138, p. 142). Articolo: *Contemporary Music Review* 10(2), pp. 135-148. Mapping verificato: PDF p. N = articolo p. 134+N. Corretti `discipio1994.md` (3 quote) e `overview.md` (1 quote).
Issue 2 (tabella precursori): aggiunta riga DiScipio 1994 in tabella "Precursori e rami complementari" come precursore concettuale del loop lungo. Aggiunta nuova sezione "Sistemi contemporanei (poli compositivi opposti)" con riga Roads/Kilgore/DuPlessis 2021 (EC2) come polo gestural opposto al declarative PGE.
Issue 4 (differenziatori chiave): integrato confronto EC2 in differenziatore 1 (OSC scripting v1.2 = scripting esterno vs DSL+LSP integrato) e differenziatore 2 (Scan Display real-time vs Score Visualizer post-synthesis — stesso fenomeno fisico, scopi opposti).
File toccati: `wiki/sources/papers/discipio1994.md`, `wiki/overview.md`, `wiki/log.md`.

---

## [2026-05-08] ingest | roads2021.md — EmissionControl2 Architecture

Fonte: `raw/papers/Roads_2021_Architecture-Real-Time-Granular-Synthesis-EmissionControl2.pdf` (*Computer Music Journal*, 45(3), pp. 20–38, doi:10.1162/COMJ_a_00613)
Output: `wiki/sources/papers/roads2021.md`
Contenuto: EC2 come granulatore real-time per-grain, polo opposto di PGE nel paradigma gestural vs declarative. Tabella corrispondenze architetturali EC2↔PGE (scanner=PointerController, Asynchronicity+Streams=DensityController, LFO modulation=Envelope strategies, Scan Display vs Score Visualizer). Quote chiave: studio composition = "tape is running," culling good parts — contrasto diretto con il workflow YAML→genera→ascolta→rifletti di PGE. OSC scripting (v1.2) apre al controllo algoritmico ma non raggiunge l'astrazione di DSL dichiarativo PGE.
Aggiornati: `bibliography.md` (Roads2021 ✗→✓, sezioni 3, 6); `index.md`; `overview.md` (gap aggiornato).

---

## [2026-05-08] ingest | discipio1994.md — Micro-time sonic design and timbre formation

Fonte: `raw/papers/DiScipio_1994_Micro-Time-Sonic-Design-and-Timbre-Formation.pdf` (*Contemporary Music Review*, 10(2), pp. 135–148)
Output: `wiki/sources/papers/discipio1994.md`
Contenuto: teorizzazione dei "models of detailed sonic design" come approccio indeterministico alla composizione micro-strutturale. Supera la distinzione composing-the-sound / composing-with-sound (Truax 1990b) in una visione olistica timbro=forma. Opere discusse: *kairós* (1991/92, IBM486 home studio, deferred time), *Zeitwerk l'orizzonte delle cose* (1992, IBM3090 + ICMS Padova, deferred time), *Essai du vide. Schweigen* (1993, GSAMX real-time, Simon Fraser). Affinamento tesi: la postura indeterministica non è vincolata al deferred time ma al ciclo iterativo di osservazione; PGE sceglie il deferred come spazio compositivo, non per costrizione hardware.
Aggiornati: `bibliography.md` (DiScipio1994 ✗→✓, sezioni 2, 3); `index.md`; `overview.md` (radici teoriche estese con Di Scipio 1994, gap aggiornato).

---

## [2026-05-08] ingest | depolipiccialli1991.md — Pitch-Synchronous Granular Synthesis

Fonte: `raw/papers/DePoli-Piccialli_1991_Pitch-Synchronous-Granular-Synthesis.pdf` (*Representations of Musical Signals*, MIT Press, pp. 187-219). PDF scannerizzato, letto con OCR locale.
Output: `wiki/sources/papers/depolipiccialli1991.md`
Contenuto: formalizzazione del ramo pitch-synchronous/source-filter: la sintesi granulare come famiglia di modelli, grano = risposta all'impulso FIR, treno quasi periodico di impulsi agganciato al pitch, griglia dipendente dal suono, prototype waveform transformations per controllare formanti, ampiezza, frequenza centrale, bandwidth e shape.

Aggiornati: `bibliography.md` (DePoliPiccialli1991 ✗→✓, sezioni 2, 3); `index.md`; `overview.md` (radici teoriche, tabella rami complementari, gap); `wiki/concepts/sintesi-granulare-sincrona.md` con formalizzazione source-filter, griglia dipendente dal pitch e prototype waveform transformations.

---

## [2026-05-09] ingest | roads2001 (Microsound) — ingest parziale ch1 + ch9

Fonte: `raw/papers/Roads_2001_Microsound.pdf` (libro, 423 pp PDF / 9 capitoli + 2 appendici).
Output (creati): `wiki/sources/papers/roads2001-ch01-time-scales.md`, `wiki/sources/papers/roads2001-ch09-conclusion.md`
Strategia: 10 sub-agent paralleli (ch1–9 + appA), schema fisso adattato a libro multi-capitolo.

**Esito.**
- ch9: agent ha letto pp 363–366, Write negato dalla quota, body completo restituito come testo e persistito manualmente in main.
- ch1: agent ha letto pp 15–56, Write negato; restituito solo summary ≤200 wd con 3 quote killer (pp. 6, 10, 26). File scritto come *stub partial* da main, marcato in testa.
- ch2 (history), ch3 (granular synthesis), ch4 (particle synthesis), ch5 (transformation), ch6 (windowed analysis), ch7 (composition), ch8 (aesthetics), appA (cloud generator): falliti per stream timeout o quota limit reached. Nessun file scritto.

**Quote chiave da ch1 (pietra angolare tesi loop lungo):**
> «This backtracking is not necessarily time wasted; it is part of an important feedback loop in which the composer refines the work. … Compare all this with the efficiency of the real-time improviser!» (p. 10)
>
> «One can imagine a musical interface in which a musician specifies the desired sonic result in a musically descriptive language which would then be translated into particle parameters and rendered into sound.» (p. 26)

**Quote chiave da ch9 (cornice terzo atto):**
> «Few maps exist, and shortcuts are scarce. So we base our composition strategy on a heuristic search for remarkable sound objects…» (p. 351)

Aggiornati: `bibliography.md` (Roads2001 ✗→◐ ch1+ch9; sezioni estese 2,4 → 1,2,4,6); `index.md` (2 nuove entry); legenda colonna Wiki estesa con simbolo ◐.

**Da completare in pass successivo (post reset quota):**
- ch1: re-ingest body integrale (pagina attuale è stub da summary, non da rilettura)
- ch2 history, ch3 granular synthesis (core), ch4 particle synthesis (core), ch5 transformation (sample-based granular = core), ch6 windowed analysis (tangenziale), ch7 composition (modello sezione 5 paper), ch8 aesthetics (core argomentativo), appA cloud generator (precursore architetturale diretto)
- propagazione `overview.md` (precursori, differenziatori, lineage UCSB) — rimandata fino a ingest core completo (ch3, ch4, ch8, appA)

---

## [2026-05-09] ingest | roads2006.md — The evolution of granular synthesis (Xenakis Symposium)

Fonte: `raw/papers/Roads_2006_Evolution-Granular-Synthesis.pdf` (lecture, *International Symposium on The Creative and Scientific Legacies of Iannis Xenakis*, University of Guelph, 8–10 June 2006, 14 pp.)
Output: `wiki/sources/papers/roads2006.md`
Contenuto: panoramica programmatica della linea UCSB 2001–2006. Cinque progetti: PulsarGenerator (de Campo+Roads, 2001) con controllo via envelope time-varying su tutti i parametri di un pulsar train; SweepingQGranulator (SuperCollider) per microfiltration constant-Q per-grano; matching pursuit decomposition (Mallat–Zhang) come analisi TF atomica; EmissionControl 2005 (Thall+Roads) come prototipo della lineage gestural che culmina in EC2 (Roads 2021); progetto Ynez per visualizzazione e *study scores for electronic music* — dichiarazione programmatica della categoria di artefatto che PGE materializza nel score_visualizer. Cavitation/density-opacity formulati come parametri compositivi primari ("ratio of sound to silence"); metafora delle "sonic brushes" come computer programs che gettano particelle sul canvas tempo×frequenza. Citazione di Babbitt 1988 ("tape is for storage, control time as measurable distance of tape") usata da Roads per giustificare la fine-grained precision (5 µsec a 192 kHz).
Quattro corrispondenze PGE: (1) PulsarGenerator envelope-based control = `ParameterOrchestrator` su `Envelope` strategies; (2) EmissionControl 2005 = tappa intermedia della lineage gestural opposta a PGE; (3) Ynez "study scores" come categoria-antesignana di score_visualizer; (4) cavitation/density come riferimento concettuale per `DensityController`.
Aggiornati: `bibliography.md` (Roads2006 ✗→✓, sezioni 3, 6); `index.md`; `overview.md` — tabella "Sistemi contemporanei" estesa con righe 2001 (PulsarGenerator), 2005 (EmissionControl), 2006 (Ynez project) per tracciare la lineage UCSB pre-EC2; differenziatore 2 esteso con Ynez come antesignano programmatico (non implementato per output granulare deferred); gap aggiornato.

---

## [2026-05-11] ingest | roads2001 — Microsound cap. 2, 5, 6 + hub roads2001.md

Fonte: `raw/papers/Roads_2001_Microsound.pdf` (libro intero, 409 pp.). Sessione di chiusura dell'ingest integrale di *Microsound*: completati i tre capitoli mancanti (cap. 2 history, cap. 5 transformation, cap. 6 windowed analysis) e creato il file hub aggregatore.

Output:
- `wiki/sources/papers/roads2001-ch02-history-microsound.md` (pp 43–84): genealogia antiquo→analogico (atomismo greco, Beekman/Gassendi corpuscolare, Einstein 1907 phonon, Gabor 1946–1952, Meyer-Eppler Mosaiktechnik, Xenakis screens/ataxy/Markov chains, Stockhausen *How Time Passes* + Kontakte, Cowell precursore multi-scala 1930). Quote chiave: Schaeffer p. 44 («*musical ideas are prisoners of musical devices*»); critica frame rate costante pp. 67–68 («*the idea that all grains have the same duration is aesthetically limiting*») come razionale del differenziatore PGE; wave/particle dualismo p. 55 come razionale architetturale multi-scala.
- `wiki/sources/papers/roads2001-ch05-transformation.md` (pp 179–234): catalogo trasformazioni sample-based (micromontage graphical/script/algorithmic, granulation parameters list a 10 voci con corrispondenza 1:1 a YAML PGE, pitch-time changing granulare, filtering per-grano GranQ, waveset/wavecycle Wishart, convolution con cloud, spatialization per-grano). Quote pietra-angolare p. 234 (Roads/Vaggione): «*Circuit speed is less of a limiting factor [...] Musical interfaces that offer control through envelopes, presets, and other automation functions will assist composers in planning detailed and elaborate transformations*» — legittimazione esplicita del DSL come interfaccia compositiva matura, indipendente dalla velocità del calcolo. Quote p. 185 (micromontage by algorithmic process: «*high-level specification → note statements*») = DSL ante litteram. Quote p. 188 (asynchronous file granulation freedom > real-time).
- `wiki/sources/papers/roads2001-ch06-windowed-analysis.md` (pp 235–300): STFT, phase vocoder, tracking PV, vector oscillator transform, wavelet, Gabor transform. Capitolo *meno citabile* per PGE (PGE è time-domain, cap. 6 è frequency-domain) ma fondamentale per (a) razionale teorico del grano gaussiano via Gabor transform, (b) delimitazione scope: PGE è granular engine time-domain deferred, analisi-risintesi spettrale è out-of-scope per scelta. Quote Mallat p. 238 e Orcalli p. 300.
- `wiki/sources/papers/roads2001.md` (**hub**): indice di tutti i capitoli ingestiti (1–9 + appA), tre quote pietra-angolare (loop lungo p. 10, DSL p. 26, interfacce dichiarative p. 234), mappa capitoli → contributi PGE → sezioni paper CIM, posizionamento argomentativo del paper rispetto al libro (riprendere loop lungo + adempiere programma DSL + risolvere problema frame rate costante).

Aggiornati:
- `bibliography.md`: `Roads2001 | ◐ ch1+ch9 → ✓ (integrale: ch1–9 + appA)`; sezioni paper estese a 1, 2, 3, 4, 6.
- `overview.md`: differenziatore (1) YAML DSL esteso con tre quote esplicite di Roads (cap. 1 p. 26, cap. 5 p. 185, cap. 5 p. 234) che articolano in tre punti distinti del libro il programma di un'interfaccia compositiva dichiarativa che PGE materializza. Aggiunto differenziatore (6) density/durata grano time-varying per-voice, con riferimento esplicito alla critique constant microtime grid di Roads cap. 2 pp. 67–68. Gap section aggiornato (Roads 2001 *Microsound* rimosso dai gap, marcato come integrale tra gli ingestiti).
- `index.md`: hub `roads2001.md` + entry per ciascun capitolo (ch2, ch3, ch4, ch5, ch6, ch7, ch8, appA) con sintesi ≤2 righe ciascuna.

**Tre quote pietra-angolare di Roads 2001 per il paper CIM** (tutte tracciate nel hub):
> «*Composition is itself a supratemporal activity. [...] This backtracking is not necessarily time wasted; it is part of an important feedback loop in which the composer refines the work. [...] Compare all this with the efficiency of the real-time improviser!*» (cap. 1 p. 10) — tesi loop lungo.
>
> «*One can imagine a musical interface in which a musician specifies the desired sonic result in a musically descriptive language which would then be translated into particle parameters and rendered into sound.*» (cap. 1 p. 26) — programma DSL.
>
> «*Circuit speed is less of a limiting factor, but no matter how fast computers become, certain transformations will always be too difficult for a human being to manipulate effectively in real time [...] Musical interfaces that offer control through envelopes, presets, and other automation functions will assist composers in planning detailed and elaborate transformations.*» (cap. 5 p. 234) — legittimazione architetturale.

Note metodologiche:
- ch3, ch4, ch7, ch8, appA risultano untracked nello stato git (creati in sessioni precedenti); confermati per integrazione in questo ingest di chiusura.
- Roads 2001 è ora il testo di riferimento *integralmente coperto* della bibliografia PGE. Le citazioni nel paper potranno riferirsi al libro intero (`Roads2001`) con rinvio a capitolo specifico via wiki.

---

## [2026-05-11] restructure | CLAUDE.md variante book-chapter + quote DSL pp. 26-27

Review-ingest del collega su roads2001 ha esposto due lacune formali (entrambe minori). Fix:

1. **CLAUDE.md**: aggiunta nuova sottosezione `Workflow ingest (libro suddiviso per capitolo)` tra `Workflow ingest (paper PDF)` e `Workflow ingest (PGE source module)`. Documenta lo schema usato per ingest libri-trattato (es. Roads 2001 Microsound): struttura file (pagina hub + sub-pages capitolo + appendici); schema hub (Citazione + Stato ingest + Argomento del libro + Quote pietra-angolare + Mappa contributi + Capitoli per sezione + Posizionamento); schema sub-page capitolo (Posizione + Argomento + Struttura + Concetti chiave + Rilevanza PGE + Tesi centrale + Quote chiave + Sezioni CIM); regole di propagazione. La variante book-chapter era già stata applicata di fatto a roads2001 ma non documentata come schema canonico.

2. **Quote 2 (DSL musicale)**: attribuzione corretta da "p. 26" a "pp. 26-27" in tutte le occorrenze. La frase attraversa effettivamente le due pagine ("...which would then be translated" termina a p. 26; "into particle parameters and rendered into sound." apre p. 27). Update in:
   - `wiki/sources/papers/roads2001.md` (3 occorrenze: heading sezione, mappa contributi, mossa argomentativa 2)
   - `wiki/sources/papers/roads2001-ch01-time-scales.md` (4 occorrenze: heading "DSL legitimation", riferimento contributo 1, quote chiave, sezione 3)
   - `wiki/index.md` (entry ch01)
   - `wiki/overview.md` (differenziatore 1)

Resta in log.md la dicitura "p. 26" nelle entry storiche (2026-05-09 e 2026-05-11) come testimonianza del fix — log è append-only.

---

## [2026-05-11] ingest | roads2012.md — Roads 2012 *From Grains to Forms*

Fonte: `raw/papers/Roads_2012_From-Grains-to-Forms.pdf` (40 pp., Xenakis Symposium Paris 2012).
Output: `wiki/sources/papers/roads2012.md` (nuovo).

Schema standard paper PDF applicato. Tre punti di sovrapposizione strutturale con PGE:

1. **Per-grain effects processing come signature** (pp. 14–15): Roads dichiara che molti granulatori suonano *flat and one-dimensional* perche' mandano l'intero stream nello stesso effects channel; per-grain processing e' la signature di *truly granular signal processing*. PGE soddisfa la clausola architetturalmente (Controller x 4 + VoiceManager + dephase per-grano).
2. **Higher-order granulation = workflow STEMS** (p. 13): *Now* (2004) regranulazione di *Volt air*, *Never* (2010) regranulazione di terzo ordine, *Always* di quarto ordine — Roads assembla manualmente in Pro Tools; PGE istituzionalizza la pipeline (stem multitraccia + cache + export DAW).
3. **Studio detached from real-time** (p. 7): formulazione canonica della postura tempo differito.

Tre legittimazioni argomentative (non coperte in altre ingestioni):
- **PulsarGenerator compromise script + envelope** (p. 35, conclusione): endorsement esplicito dello spazio di interazione che PGE-ls + score_visualizer abita.
- **Fallimento Creatovox** (pp. 10–11): ammissione di prima persona da parte di Roads che la lineage virtuosica richiede pratica giornaliera che e' incompatibile con l'interesse compositivo; legittima la scelta architetturale PGE di non perseguire real-time.
- **Economy of selection** (pp. 31–32): teorizzazione esplicita del loop lungo come metodologia compositiva — *choosing one or a few perceptually and aesthetically optimal or salient choices from a vast desert of unremarkable possibilities*.

Propagazione:
- `overview.md`: differenziatore 1 (DSL) aggiunto quote PulsarGenerator compromise; differenziatore 3 (STEMS) aggiunta pratica higher-order granulation + quote "detached from real-time"; nuovo differenziatore 7 *per-grain effects processing come signature architetturale*; nuova sezione *Note per Sezione 6 — economy of selection come teorizzazione del loop lungo*; entry Roads 2012 spostata in lista *gia' ingestiti*.
- `bibliography.md`: Roads2012 — Wiki ✗ → ✓; Sezioni paper "4" → "1, 2, 3, 4, 5, 6".
- `index.md`: entry roads2012.md aggiunta sotto roads2006.md.

Niente concept pages nuove. Niente update a sintesi-granulare-sincrona.md (paper non tratta la distinzione SGS pitch-synchronous De Poli-Piccialli).

---

## [2026-05-11] fix | roads2012.md — review-ingest: citazione + page numbers + stile

Review-ingest del collega ha esposto un bug bloccante (citazione CIM errata) e tre errori di citazione pagine verificati contro PDF (`raw/papers/Roads_2012_From-Grains-to-Forms.pdf`, convention: PDF page N = printed page N, footer in fondo pagina).

1. **Citazione CIM**: era "In M. Solomos (ed.), *Proceedings of the international Symposium Xenakis* (université Paris 8, May 2012)" — pubblicazione errata. Corretto a "In S. Kanach (ed.), *Xenakis Matters: Contexts, Processes, Applications*. Hillsdale, NY: Pendragon Press. ISBN 978-1-57647-238-5", allineato a refs.bib (`@incollection{Roads2012}`). Solomos 2012 è altro volume da Paris 8; Kanach 2012 è il volume Pendragon che contiene "From Grains to Forms".

2. **Page numbers verificati contro PDF**:
   - "Detached from real-time constraints..." era p. 7 → corretto a **p. 8**.
   - "compromise between gestural interaction... PulsarGenerator" era p. 35 → corretto a **p. 30** (p. 35 è bibliografia; quote è in sezione CONCLUSION).
   - "principle of economy of selection / vast desert of unremarkable possibilities" era pp. 31–32 → corretto a **pp. 28–29** (sezione "The principle of economy of selection" inizia a p. 28).
   - "Recycling sounds... higher-order granulation" p. 13 ✓ (verificato).
   - "essential feature ... per-grain effects processing" pp. 14–15 ✓ (verificato).
   - "A funny thing happened... Creatovox" pp. 10–11 ✓ (verificato, quote continua p. 11 con Bebe Barron).

3. **Inconsistenza pp/p**: "(p. 14–15)" sezione Rilevanza → "(pp. 14–15)".

4. **Neologismo**: "cita-by-author" → "citato dall'autore stesso".

Propagazione page-number fix:
- `wiki/sources/papers/roads2012.md`: 8 occorrenze (Rilevanza, Collegamento tesi, Sezioni CIM, Quote chiave).
- `wiki/overview.md`: 3 occorrenze (differenziatore 1 p. 35→30, differenziatore 3 p. 7→8, Note Sezione 6 pp. 31-32→28-29).

Le citazioni errate nell'entry log immediatamente precedente (ingest roads2012 stesso giorno) restano come testimonianza — log è append-only.

## [2026-05-12] ingest | vaggione1991.md + vaggione1996.md + vaggione2002.md — trilogia Vaggione object-based / transformational / decorrelation

Fonti:
- `raw/papers/Vaggione_1991_On-Object-Based-Composition.pdf` (10 pp., versione francese 1995 in Ars Sonora — adattamento riveduto dell'originale Interface 1991)
- `raw/papers/Vaggione_1996_Approche-Transformationnelle-CAO.pdf` (9 pp., JIM 1996 Tatihou)
- `raw/papers/Vaggione_2002_Decorrelation-Microtemporelle.pdf` (12 pp., JIM 2002 Marseille)

Output: tre nuove pagine `wiki/sources/papers/vaggione{1991,1996,2002}.md`.

Schema standard paper PDF applicato a ciascuna. La trilogia funziona come triplice radice teorica del DSL e dell'architettura PGE:

1. **Vaggione 1991 — framework concettuale**: l'oggetto sonoro digitale come (a) collezione di oggetti discreti funzionante come entità unitaria, (b) collezione di échantillons; *transparent* contro l'opacità del supporto magnetico analogico. OOP applicato a composizione (clôture/héritage/polymorphisme). Multiple représentations come *réécritures*. → Fondamento concettuale del network Stream/Voice/Controller PGE + asse Y partitura (= posizione nella collection d'échantillons).

2. **Vaggione 1996 — meccanica fine del DSL**: quote-pietra-angolare *interaction forte* (p. 2): «toute intervention directe peut être considérée comme la déclaration d'un attribut particulier d'une entité quelconque; cet attribut peut dès lors être généralisé à toutes les instances successives de cette entité». Questa è la legittimazione argomentativa più precisa del DSL YAML + ParameterOrchestrator. Vaggione condanna anche i «taux ou pourcentages de variation [...] palliatifs au manque de visée proprement figurale» (p. 4) → legittima il visualizer figurale come strumento di lettura non statistica. Tahil/Kitab come precedenti compositivi nel reseau object-based.

3. **Vaggione 2002 — legittimazione spaziale di VoiceManager**: décorrélation microtemporelle (offset di ms su canali fisicamente separati, valori time-varying per voce) come attributo morfologico-spaziale, distinto dal panning classico (campo sincrono esterno). Realizzato direttamente da VoiceManager (onset/pointer/pan strategies) + dephase Controller per-grano («relation kaléidoscopique multi-locale», p. 6). Tempo differito esplicito come contesto nativo della tecnica (Music N family). Cita esplicitamente Vaggione 1996 a p. 7 — conferma la *colonna vertebrale* metodologica delle tre opere.

Propagazione:
- `overview.md`:
  - differenziatore 1 (DSL): aggiunta quote 1996 «déclaration d'attribut généralisé» + critica «palliatifs» come fondamento argomentativo accanto a Roads 2001 cap. 1/5
  - differenziatore 7 (per-grain effects): aggiunta estensione 2002 spazio = «décorrélation microtemporelle» con quote «relation kaléidoscopique multi-locale» + distinzione panning/decorrelation
  - tabella precursori CIM: nuova riga 1991/1996/2002 Vaggione che riassume la triplice radice
  - gap list aggiornata
- `bibliography.md`:
  - Vaggione1991 — Wiki ✗ → ✓; Sezioni "2, 4" → "1, 2, 3, 4"
  - Vaggione1996 — Wiki ✗ → ✓; Sezioni "3, 4" → "1, 3, 5, 6"
  - Vaggione2002 — Wiki ✗ → ✓; Sezioni "4" → "2, 3, 4, 5"
- `index.md`: tre entry aggiunte sotto roads2001-appA-cloud-generator.md.

Niente nuove concept pages. Niente update a sintesi-granulare-sincrona.md (la trilogia non tocca la distinzione SGS pitch-synchronous De Poli-Piccialli ma opera su un asse diverso: object-based composition, transformational CAO, decorrelation spaziale).

Una sola entry log per i tre paper, come da convenzione (ingest multipli stessa sessione).

---

## [2026-05-12] fix | vaggione2002.md + vaggione1991.md + overview.md — review-ingest collega

Review-ingest dei tre Vaggione ha esposto un bug bloccante non-Vaggione + page numbers off-by-one in vaggione2002.md + citazione header vaggione1991.md.

1. **Typo regressione `overview.md`** (riga Di Scipio 1994, hunk vaggione): "indeterismatica" → "indeterministica". Carattere `t` saltato, ortografia errata. Refuso introdotto durante l'edit della tabella precursori per aggiungere la riga Vaggione 1991/1996/2002 immediatamente sotto.

2. **Citazione header `vaggione1991.md`**: "(PDF letto: versione francese, 10 pp.)" → "(PDF letto: versione francese web-archived da archive.org, 8 pp.; originale a stampa pp. 33-52)". Il PDF locale è 8 pp fisiche (versione archive.org di Ars Sonora 1995); il conteggio "10 pp" era errato. Chiarito anche che pp. 33-52 è paginazione del fascicolo Ars Sonora originale.

3. **Page numbers `vaggione2002.md`** verificati con `pdftotext -f N -l N` contro PDF (12 pp fisiche, no footer printed numbers). Correzioni:
   - Gap section: panning `p. 8` → `p. 9` (PDF p. 9 ha "le panning n'a pas besoin d'informations concernant la phase").
   - Sezione "Condizioni minime" header: `pp. 5-6` → `p. 6` (lista a/b/c interamente su PDF p. 6).
   - Rilevanza 3 (real-time extension): `p. 6` → `p. 7` (sezione "Temps différé/temps réel" inizia PDF p. 7).
   - Rilevanza 5 (richiamo Vaggione 1996): `p. 7` → `p. 8` (PDF p. 8: «Dans un texte présenté aux JIM [Vaggione 1996]»).
   - Rilevanza 6 (micromontage): `p. 6` → `p. 7` (PDF p. 7 fine: «micromontages afin de construire des ensembles musicaux»).
   - Quote chiave 2 (panning): `p. 8` → `p. 9`.
   - Quote chiave 3 (kaléidoscopique): `p. 6` → `p. 7` (era anche contraddizione interna: Rilevanza 2 citava già `p. 7` correttamente).
   - Quote chiave 4 (figure musicale): `p. 9` → `p. 10` (PDF p. 10 inizio).

4. **Page numbers `overview.md` differenziatore 7** (citazioni Vaggione 2002 inline propagate dal collega):
   - kaléidoscopique: `p. 6` → `p. 7`.
   - champ spatial stable: `p. 8` → `p. 9` (PDF p. 9: «un champ spatial stable, ainsi que de les... champ toujours synchronique»).

Citazioni verificate corrette e mantenute: morphophorique p. 2, ITD 5 µs – 1.5 ms p. 5, studio numérique p. 3, kaléidoscopique Rilevanza 2 p. 7.

Out of scope review: schema deviation `vaggione2002.md` (sezione extra "Condizioni minime" tra Gap e Rilevanza — non prevista da workflow paper PDF "Schema fisso") e mancanza concept pages per object-based composition / décorrélation microtemporelle — note come follow-up non bloccante.

I refusi nelle entry log immediatamente precedenti (`p. 6/p. 8/p. 9` originali) restano come testimonianza — log append-only.

---

## [2026-05-12] ingest | Caires 2004 — IRIN: Micromontage in Graphical Sound Editing and Mixing Tool

Fonte: `raw/papers/Caires_2004_IRIN-Micromontage-Graphical.pdf` (ICMC 2004 Proceedings, Miami).
Output: `wiki/sources/papers/caires2004.md` (nuova).
Pagine toccate: 1 nuova + `wiki/sources/bibliography.md` (Wiki ✓, Sezioni 2,3,4) + `wiki/index.md` (entry sotto Vaggione 2002 per evidenziare filiazione) + `wiki/overview.md` (riga 2004 in tabella precursori CIM; aggiornata "Gap da colmare" rimuovendo Caires 2004 dai pending e aggiungendolo a ingestiti).

Sintesi:
- IRIN è Max/MSP standalone Mac OS X (offline, render finale a file multitraccia) di Carlos Caires (CICM Paris VIII, allievo di Horacio Vaggione — ringraziato come supervisor).
- Gerarchia oggetti: Sample (atomo: source file, speed, biquad filter, envelope 256pt, phase shift, shape colorato) → Figure (array Samples con onset modificabili + granulator integrato che genera particle stream con global laws su duration/distance/phase shift/filtering, poi editabile per-istanza) → Meso-structure (8-layer sequencer di Figure) → Timeline (4 track polifonici + Sound file + MIDI track).
- Differenziatore IRIN vs DAW: proprietà sonore (panning, envelope, phase shift) sono *track-independent feature* — la traccia è metafora di rigo di partitura, non bus audio. "Shapes view" mode su Timeline = primo score grafico multi-traccia per micromontage granulare con encoding cromatico-formale.
- Citazione letterale di Vaggione 2002b in nota 2: "Phase shifting in this context is used as a composition technique belonging to the micro-scale domain (*micro decorrélation temporelle*)". IRIN materializza la décorrélation microtemporelle come attributo per-sample editabile graficamente.

Rilevanza per tesi PGE:
- Conferma vitalità del tempo differito nel 2004 in piena epoca real-time disponibile (Max/MSP audio 1998); IRIN è applicazione operativa diretta del programma transformational Vaggione (1991/1996/2002b) in software, sei anni prima di PGE.
- Polo opposto in superficie compositiva (GUI direct-manipulation vs DSL YAML) sulla stessa famiglia di problemi del loop lungo.
- Timeline IRIN come precursore concreto di score_visualizer PGE: stessa categoria (study score per micromontage granulare), inversione di flusso (score editabile come input vs score come output ispezionabile); differenziatore PGE: asse Y = posizione nel buffer vs asse Y = traccia in IRIN.

Quote chiave estratte (per uso in paper): p. 1 (memory of all actions come imperativo architetturale del micromontage), p. 2 nota 2 (micro decorrélation temporelle), p. 3 (gestalt da local singularities, citando Vaggione 1996/2002a), p. 4 (tracks as metaphor for score staffs).

Aperto per sessione successiva: valutare se aprire concept page `concepts/micromontage.md` per consolidare la linea Roads 2001 cap.5 + Caires 2004 + Vaggione (filiazione); non bloccante.

---

## [2026-05-12] review-ingest | Caires 2004 — risoluzione lacune minori

Review dell'ingest precedente. Tre lacune risolte:

1. **Citazione CIM senza pagine** → ricerca web ha confermato ICMC 2004 vol. 30 pp. 219–222. Aggiornati:
   - `wiki/sources/papers/caires2004.md` sezione Citazione CIM (formato completo con vol./pp./publisher)
   - `refs.bib` entry `Caires2004` (campi `volume`, `pages`, `publisher` aggiunti)
   - Riferimenti interni alle quote: `p. 1 → p. 219`, `p. 2 nota 2 → p. 220`, `p. 4 → p. 222`

2. **Quote count = 4** vs workflow vincolo "massimo 2-3" → rimossa quote p. 221 (gestalt da local singularities, sezione 3.2): contenuto derivativo (cita Vaggione 1996/2002a già pietra-angolare nelle rispettive pagine wiki). Trattenute le 3 quote uniche di IRIN: p. 219 (memory of all actions), p. 220 nota 2 (micro decorrélation temporelle), p. 222 (tracks as metaphor for score staffs).

3. **Concept page `concepts/micromontage.md`** → creata. Sintesi cross-source di Roads 2001 cap. 5 (tassonomia tre forme: graphical/script/algorithmic) + linea Vaggione 1991/1996/2002 + Caires 2004 IRIN. PGE posizionata come quarta variante operativa della forma *algorithmic* di Roads (DSL YAML strutturato come *high-level specification*). Pagina propagata a `wiki/index.md` sezione Concepts (sotto sintesi-granulare-sincrona).

Pagine toccate: `wiki/sources/papers/caires2004.md`, `refs.bib`, `wiki/concepts/micromontage.md` (nuova), `wiki/index.md`, `wiki/log.md`.

Note di processo: la citazione mancava perché ICMC 2004 è CDROM Proceedings (verificato via `pdfinfo` Subject field) — paginazione non sempre disponibile su Crossref; localizzata via search su quod.lib.umich.edu (mirror ICMA proceedings).

---

## [2026-05-17] ingest | truax2014.md — Interacting with Inner and Outer Sonic Complexity

Fonte: `raw/papers/Truax_2014_Interacting-Inner-Outer-Sonic-Complexity-Microsound-to-Soundscape.pdf` (*eContact!* 16(3), 6 pp., online).
Output: `wiki/sources/papers/truax2014.md` (nuova).

Schema standard paper PDF applicato. Retrospettiva Truax @ 25+ anni di time-frequency methods (granular time-stretching, risuonatori, convoluzione) come quadro unificato micro/macro. Quattro corrispondenze PGE:

1. **Listening "inside" the sound** (p. 2): correlato percettivo del time-stretching granulare — l'attenzione si sposta dal contorno macro alle componenti spettrali interne. Giustificazione percettiva diretta dell'asse Y = posizione-buffer in `score_visualizer` PGE.
2. **Abstracted vs abstract processing** (p. 5): criterio di adeguatezza coerente con differenziatore 7 (per-grain effects, Roads 2012) — il design deve bring out internal aspects, non obliterating identity.
3. **Composing "through" sound** (p. 5): formula della postura compositiva del loop lungo, cugina del *composing-the-sound/with-sound* di Truax 1990b.
4. **Tassonomia computer-realized / computer-assisted / computer-composed** (p. 6): PGE come computer-assisted — partnership che cambia vocabolario, posizionamento utile in sezione 6.

Non rilevante: sezione *Soundscape Composition* (PGE non è strumento soundscape composition-specific).

Propagazione:
- `bibliography.md`: Truax2014 — Wiki ✗ → ✓; Sezioni "2" → "2, 4, 6".
- `index.md`: entry sotto truax1994.md.
- `overview.md`: radici teoriche estese con quote *listening "inside" the sound* come giustificazione percettiva dell'asse Y; contributo 2 (partitura grafica) esteso con riferimento Truax 2014 dopo Truax 1994; gap list aggiornata (Truax 2014 spostato da pending a ingestiti).

Niente nuove concept pages. Niente nuovi differenziatori (Truax 2014 rafforza differenziatore 2 e differenziatore 7 esistenti).

