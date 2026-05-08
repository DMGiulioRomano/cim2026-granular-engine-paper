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

## [2026-05-08] ingest | depolipiccialli1991.md — Pitch-Synchronous Granular Synthesis

Fonte: `raw/papers/DePoli-Piccialli_1991_Pitch-Synchronous-Granular-Synthesis.pdf` (*Representations of Musical Signals*, MIT Press, pp. 187-219). PDF scannerizzato, letto con OCR locale.
Output: `wiki/sources/papers/depolipiccialli1991.md`
Contenuto: formalizzazione del ramo pitch-synchronous/source-filter: la sintesi granulare come famiglia di modelli, grano = risposta all'impulso FIR, treno quasi periodico di impulsi agganciato al pitch, griglia dipendente dal suono, prototype waveform transformations per controllare formanti, ampiezza, frequenza centrale, bandwidth e shape.

Aggiornati: `bibliography.md` (DePoliPiccialli1991 ✗→✓, sezioni 2, 3); `index.md`; `overview.md` (radici teoriche, tabella rami complementari, gap); `wiki/concepts/sintesi-granulare-sincrona.md` con formalizzazione source-filter, griglia dipendente dal pitch e prototype waveform transformations.

---
