# Operations Log

Log append-only. Ogni entry: `## [YYYY-MM-DD] <tipo> | <titolo>`.
Tipi: `ingest`, `query`, `lint`, `restructure`.

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

## [2026-05-04] ingest | CIM Proceedings (23 volumi, 1976–2024)

Fonte: `raw/proceedings/` — `pdftotext` su tutti i PDF, ricerca su radice `granul`.
Output: `wiki/sources/proceedings/cim-survey.md`
Pagine toccate: 1 nuova.
Sintesi: trovati articoli dedicati alla sintesi granulare in 12 dei 23 volumi CIM.
Confronto con PGE documentato nella sezione "tempo differito" del survey.

---
