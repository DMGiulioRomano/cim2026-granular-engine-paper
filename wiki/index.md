# Wiki Index

Catalogo di tutte le pagine wiki. Leggi questo file prima di ogni ricerca.
Aggiorna dopo ogni ingest o query sostanziale.

---

## Sources — Proceedings

- [CIM Survey](sources/proceedings/cim-survey.md) — survey sistematico 23 volumi CIM (1976–2024) su sintesi granulare; confronto con pipeline PGE

## Sources — Papers

- [Bibliography](sources/bibliography.md) — citazioni formattate disponibili + gap da ingestire
- [truax1988.md](sources/papers/truax1988.md) — DMX-1000 real-time granular, tre modelli AS/FM/SAM, Tabella 1 psychoacoustic correlates, gerarchia Fig. 3, Fig. 4 ASCII tendency masks come primo overlay multi-parametro
- [truax1990.md](sources/papers/truax1990.md) — gerarchia di controllo granulare, postura compositiva real-time come polo opposto del loop lungo PGE, tendency masks come precursore visivo della partitura
- [truax1994.md](sources/papers/truax1994.md) — variable-rate granulation, harmonization scheme F=4, separazione micro/macro come tesi psicoacustica abilitante; precursore concettuale di PointerController.speed_ratio e asse Y partitura
- [roads1978.md](sources/papers/roads1978.md) — AGS, prima implementazione computer della sintesi granulare; pattern front-end MUSIC V; event a 6 coppie valore/slope; polygon su piano freq/tempo come notazione grafica
- [roads1988.md](sources/papers/roads1988.md) — editoriale CMJ, vocabolario canonico (grain/density/event/cloud), event a 12 parametri come precursore DSL, eventi come forme geometriche su piano frequenza/tempo
- [gabor1947.md](sources/papers/gabor1947.md) — radice teorica del paradigma granulare: information diagram tempo×frequenza, Δt·Δf ≥ 1, grano gaussiano, soglia di discriminazione dell'orecchio ≈ 1 quantum
- [depolipiccialli1988.md](sources/papers/depolipiccialli1988.md) — sintesi granulare sincrona con il periodo; grani come risposte FIR a fase lineare; ramo CIM formantico da distinguere dalla distribuzione sincrona/asincrona Truax/PGE
- [depolipiccialli1991.md](sources/papers/depolipiccialli1991.md) — modello pitch-synchronous source-filter: grano come risposta FIR, griglia dipendente dal pitch, prototype waveform transformations per controllo formantico
- [discipio1994.md](sources/papers/discipio1994.md) — "models of detailed sonic design": postura indeterministica nella micro-time sonic design, timbre come forma emergente, ciclo osservazione→modifica come necessità compositiva; affinamento tesi (loop lungo ≠ solo "deferred time")
- [roads2021.md](sources/papers/roads2021.md) — EmissionControl2: granulatore real-time per-grain, polo opposto di PGE (gestural vs declarative); tabella corrispondenze architetturali EC2↔PGE; Scan Display vs Score Visualizer
- [roads2006.md](sources/papers/roads2006.md) — Xenakis Symposium lecture: lineage UCSB gestural (PulsarGenerator 2001 → EmissionControl 2005 → EC2 2021); cavitation/density come parametro compositivo primario; Ynez "study scores for electronic music" come categoria-antesignana del score_visualizer; sonic brushes come metafora del software granulare
- [roads2001.md](sources/papers/roads2001.md) — **hub** *Microsound*: indice ingest per capitolo, tre quote pietra-angolare, mappa capitoli → contributi/sezioni paper, posizionamento argomentativo del paper CIM rispetto al libro
- [roads2001-ch01-time-scales.md](sources/papers/roads2001-ch01-time-scales.md) — *Microsound* cap. 1: tassonomia 9 scale temporali; quote pietra angolare p. 10 (loop di feedback come parte essenziale della composizione, contrasto con real-time improviser); quote p. 26 (DSL musicale come interfaccia immaginata)
- [roads2001-ch02-history-microsound.md](sources/papers/roads2001-ch02-history-microsound.md) — *Microsound* cap. 2: genealogia antiquo→analogico (atomismo greco → Gabor → Meyer-Eppler → Xenakis → Stockhausen); quote Schaeffer p. 44 (musical ideas as prisoners of devices); critique constant microtime grid pp. 67–68 come razionale del differenziatore frame rate per-voice PGE
- [roads2001-ch03-granular-synthesis.md](sources/papers/roads2001-ch03-granular-synthesis.md) — *Microsound* cap. 3: teoria GS digitale, 6 organizzazioni globali, parametri (envelope, durata, density, fill factor), storia implementazioni 1974–2000
- [roads2001-ch04-particle-synthesis.md](sources/papers/roads2001-ch04-particle-synthesis.md) — *Microsound* cap. 4: varietà di particle synthesis (pulsar, glisson, grainlet, trainlet); out-of-scope rispetto a PGE sample-based granular
- [roads2001-ch05-transformation.md](sources/papers/roads2001-ch05-transformation.md) — *Microsound* cap. 5: catalogo trasformazioni sample-based (micromontage, granulation, pitch-time changing, convolution, spatialization); quote p. 185 (micromontage by algorithmic process = DSL ante litteram); quote p. 188 (asynchronous file granulation > real-time); pietra angolare p. 234 (envelopes+presets+automation come interfacce per trasformazioni che eccedono real-time)
- [roads2001-ch06-windowed-analysis.md](sources/papers/roads2001-ch06-windowed-analysis.md) — *Microsound* cap. 6: STFT, phase vocoder, wavelet, Gabor transform; fondamento DSP del grano gaussiano PGE; delimitazione scope (PGE è time-domain, analisi-risintesi spettrale out-of-scope)
- [roads2001-ch07-composition.md](sources/papers/roads2001-ch07-composition.md) — *Microsound* cap. 7: composizioni Roads (nscor, Field, Clang-Tint, Half-life, vortex), analisi compositiva Truax/Vaggione
- [roads2001-ch08-aesthetics.md](sources/papers/roads2001-ch08-aesthetics.md) — *Microsound* cap. 8: estetica multi-scala, principi compositivi, critica omogeneità
- [roads2001-ch09-conclusion.md](sources/papers/roads2001-ch09-conclusion.md) — *Microsound* cap. 9: predizioni 2001 vs realtà 2026; PGE come bifurcazione della lineage real-time-virtuosa proiettata da Roads; storehouse di gesti firma come precondizione del ritorno volontario al deferred time
- [roads2001-appA-cloud-generator.md](sources/papers/roads2001-appA-cloud-generator.md) — *Microsound* app. A: Cloud Generator (Roads/Alexander 1995) come tool single-stream offline; precursore di Stream PGE

## Sources — PGE

- [generator.md](sources/pge/generator.md) — orchestratore principale: YAML → Stream → .sco; logica solo/mute, eval matematica, build incrementale
- [stream.md](sources/pge/stream.md) — nucleo sintesi granulare: StreamConfig/StreamContext, controller×4, VoiceManager, generate_grains(); ispirazione DMX-1000
- [score-visualizer.md](sources/pge/score-visualizer.md) — partitura grafica: piano tempo×posizione-buffer, encoding grani come frecce, loop mask, envelope panel
- [stream-cache-manager.md](sources/pge/stream-cache-manager.md) — cache incrementale SHA-256 per stream Csound; dirty detection + garbage collect
- [parameter-orchestrator.md](sources/pge/parameter-orchestrator.md) — DSL parametrico: ParameterOrchestrator + GateFactory + strategie Pitch/Density; dephase/variazione stocastica
- [renderer.md](sources/pge/renderer.md) — tre renderer (Csound subprocess, NumPy overlap-add, ReaperProjectWriter); pattern OCP; STEMS vs MIX
- [pointer-controller.md](sources/pge/pointer-controller.md) — testina di lettura: speed_ratio, loop statico/dinamico, phase accumulator, deviazione per-grano; risolve open question time_mode:normalized
- [voice-manager.md](sources/pge/voice-manager.md) — offset multi-voce: VoiceConfig, 4 strategie ortogonali (pitch/onset/pointer/pan), layering architetturale a 3 livelli
- [density-controller.md](sources/pge/density-controller.md) — IOT granulare: fill_factor vs density, distribuzione Truax sincrona/asincrona, blend lineare via Envelope

## Concepts

- [Sintesi granulare sincrona](concepts/sintesi-granulare-sincrona.md) — distinzione tra period/pitch-synchronous granular synthesis (De Poli/Piccialli 1988/1991) e distribuzione IOT sincrona/asincrona in senso Truax/PGE

## Overview

- [Overview](overview.md) — tesi evolutiva: posizionamento di PGE nel panorama della sintesi granulare

## Assets

- [Call graph PGE](../graph/call_graph.dot) — grafo delle chiamate tra moduli
- [Class diagram PGE](../graph/class_diagram.puml) — diagramma classi PlantUML
