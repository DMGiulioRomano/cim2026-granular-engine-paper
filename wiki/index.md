# Wiki Index

Catalogo di tutte le pagine wiki. Leggi questo file prima di ogni ricerca.
Aggiorna dopo ogni ingest o query sostanziale.

---

## Sources — Proceedings

- [CIM Survey](sources/proceedings/cim-survey.md) — survey sistematico 23 volumi CIM (1976–2024) su sintesi granulare; confronto con pipeline PGE

## Sources — Papers

- [Bibliography](sources/bibliography.md) — citazioni formattate disponibili + gap da ingestire

*(una pagina per ogni PDF in `raw/papers/` — da popolare)*

## Sources — PGE

- [generator.md](sources/pge/generator.md) — orchestratore principale: YAML → Stream/Cartridge → .sco; logica solo/mute, eval matematica, build incrementale
- [stream.md](sources/pge/stream.md) — nucleo sintesi granulare: StreamConfig/StreamContext, controller×4, VoiceManager, generate_grains(); ispirazione DMX-1000
- [score-visualizer.md](sources/pge/score-visualizer.md) — partitura grafica: piano tempo×posizione-buffer, encoding grani come frecce, loop mask, envelope panel
- [stream-cache-manager.md](sources/pge/stream-cache-manager.md) — cache incrementale SHA-256 per stream Csound; dirty detection + garbage collect
- [parameter-orchestrator.md](sources/pge/parameter-orchestrator.md) — DSL parametrico: ParameterOrchestrator + GateFactory + strategie Pitch/Density; dephase/variazione stocastica
- [renderer.md](sources/pge/renderer.md) — tre renderer (Csound subprocess, NumPy overlap-add, ReaperProjectWriter); pattern OCP; STEMS vs MIX
- [pointer-controller.md](sources/pge/pointer-controller.md) — testina di lettura: speed_ratio, loop statico/dinamico, phase accumulator, deviazione per-grano; risolve open question time_mode:normalized
- [voice-manager.md](sources/pge/voice-manager.md) — offset multi-voce: VoiceConfig, 4 strategie ortogonali (pitch/onset/pointer/pan), layering architetturale a 3 livelli
- [density-controller.md](sources/pge/density-controller.md) — IOT granulare: fill_factor vs density, distribuzione Truax sincrona/asincrona, blend lineare via Envelope

## Concepts

*(da popolare: concetti trasversali alle fonti)*

## Overview

- [Overview](overview.md) — tesi evolutiva: posizionamento di PGE nel panorama della sintesi granulare

## Assets

- [Call graph PGE](../graph/call_graph.dot) — grafo delle chiamate tra moduli
- [Class diagram PGE](../graph/class_diagram.puml) — diagramma classi PlantUML
