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

