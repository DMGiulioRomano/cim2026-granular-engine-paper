# VoiceManager — analisi

## Ruolo nell'architettura

`VoiceManager` calcola gli offset per-voce nel sistema multi-voice di PGE. Istanziato da `Stream.__init__()` come `self._voice_manager`. Chiamato in `Stream.generate_grains()` per ogni voce attiva a ogni step temporale:

```python
voice_config = self._voice_manager.get_voice_config(voice_index, t)
```

Restituisce un `VoiceConfig` (frozen dataclass) con i quattro offset dimensionali da sommare ai valori base calcolati dai controller principali.

## Classi principali

**`VoiceConfig`** (frozen dataclass)
- Attributi: `pitch_offset: float` (semitoni), `pointer_offset: float` (normalizzato), `pan_offset: float` (gradi), `onset_offset: float` (secondi)
- Pattern: frozen dataclass — immutabile, ephemeral per chiamata, creato on-the-fly da `get_voice_config()`
- Voice-0 invariant: ogni strategy garantisce `get_*_offset(0, ...) == 0.0`

**`VoiceManager`**
- Attributi: `max_voices` (int), `_pitch_strategy` (opt.), `_onset_strategy` (opt.), `_pointer_strategy` (opt.), `_pan_strategy` (opt.), `_pan_spread` (StrategyParam: float o Envelope)
- Metodi chiave: `get_voice_config(voice_index, time) → VoiceConfig`; delega alle quattro strategy e risolve `pan_spread` con `resolve_param(pan_spread, time)`
- Pattern: Strategy orchestration — quattro strategy indipendenti opzionali; assenza = offset 0.0

**Strategy di pitch — `VoicePitchStrategy` (ABC):**

| Implementazione | Comportamento |
|-----------------|---------------|
| `StepPitchStrategy` | voce i → i × step(t) semitoni |
| `RangePitchStrategy` | distribuito linearmente in [0, semitone_range(t)] |
| `ChordPitchStrategy` | accordo nominale (es. `dom7`, `maj`, `altered`); extend all'ottava se num_voices > len(chord); supporta `inversion` |
| `StochasticPitchStrategy` | offset fisso per voce con seed deterministico; `_cache[vi] ∈ [-1,1]`; offset = `_cache[vi] × semitone_range(t)` — può essere negativo (pitch sotto base) |
| `SpectralPitchStrategy` | parziali della serie armonica: voce i → round(12 × log2(i+1)) semitoni |

Accordi disponibili: maj, min, dim, aug, sus2, sus4, dom7, maj7, min7, dim7, minmaj7, dom9, maj9, min9, 9sus4, dom9s11, maj9s11, min11, dom13, min13, maj13s11, altered (22 accordi).

**Strategy di onset — `VoiceOnsetStrategy` (ABC):**

| Implementazione | Comportamento |
|-----------------|---------------|
| `LinearOnsetStrategy` | voce i → i × step(t) secondi |
| `GeometricOnsetStrategy` | voce i → step(t) × base(t)^(i-1); spaziatura esponenziale |
| `StochasticOnsetStrategy` | offset fisso per voce con seed deterministico, in [0, max_offset(t)] |

**Strategy di pointer — `VoicePointerStrategy` (ABC):**

| Implementazione | Comportamento |
|-----------------|---------------|
| `LinearPointerStrategy` | voce i → i × step(t); offset normalizzato equidistante |
| `StochasticPointerStrategy` | seed deterministico; `_cache[vi] ∈ [-1,1]`; offset = `_cache[vi] × pointer_range(t)` — può essere negativo |

**Strategy di pan — `VoicePanStrategy` (ABC):**

| Implementazione | Comportamento |
|-----------------|---------------|
| `LinearPanStrategy` | equidistante in [−spread/2, +spread/2] |
| `RandomPanStrategy` | seed deterministico; `_cache[vi] × spread/2` |
| `AdditivePanStrategy` | spread fisso additivo identico per tutte le voci non-zero |

Tutte le strategy sono registrate in registry globali (`VOICE_PITCH_STRATEGIES`, ecc.) e estensibili via `register_*_strategy()`.

## Comportamento runtime

`get_voice_config()` è **stateless** e **ephemeral**: nessuno stato interno aggiornato, nessuna cache. Ogni chiamata ricomputa da zero delegando alle quattro strategy. Questo garantisce che il tempo corrente della voce (`time`) sia il parametro di controllo per strategie time-varying (es. `pan_spread` come Envelope).

**Layering pointer (documentato nel docstring):**
```
pointer_final = base_pointer(t)          # PointerController.calculate()
              + voice_pointer_offset      # VoicePointerStrategy (VoiceManager)
              + grain_jitter(t)           # deviation per-grano (PointerController)
```
Lo stesso schema vale per pitch e onset. Pan è solo VoiceManager + base (nessun jitter separato).

`num_voices` time-varying è gestito da `Stream.generate_grains()`, non da VoiceManager — VoiceManager riceve solo `voice_index` e `time`, non gestisce l'attivazione/disattivazione delle voci.

`pan_spread` accetta float o Envelope: lo spread (apertura dello spazio stereo) può variare nel tempo, risolto a runtime con `resolve_param(pan_spread, time)`.

## Collegamento alla tesi centrale

VoiceManager è il meccanismo che risolve il problema della polyphonia granulare senza moltiplicare la complessità di configurazione. Il gap controllo/percezione per texture polifoniche è: come specificare N voci differenziate mantenendo coerenza strutturale?

PGE risponde con strategie composabili: il compositore sceglie "voci distribuite su accordo X" (ChordPitchStrategy) + "voci sfasate nel tempo di 50ms" (LinearOnsetStrategy) + "voci distribute stereo" (LinearPanStrategy) — combinazione ortogonale, ciascuna dimensione indipendente dall'altra.

Il `scatter` menzionato in stream.md è il parametro che regola il blend tra IOT condiviso (voce 0) e IOT indipendente per voce — separato da VoiceManager, gestito in `generate_grains()`.

## Sezioni del paper CIM 2026 dove descrivere

- Sezione 3 (Architettura): schema layering pointer, struttura VoiceConfig, strategie composabili
- Sezione 4 (Partitura grafica): voci multiple visibili come frecce parallele nella partitura

## Domande aperte

- `ChordPitchStrategy` con `inversion`: il rivolto ruota gli intervalli — effetto percettivo (voce più grave diversa) rilevante per sezione compositiva?
- `pan_spread` come Envelope: apertura spaziale variabile nel tempo — caso d'uso per sezione compositiva?
