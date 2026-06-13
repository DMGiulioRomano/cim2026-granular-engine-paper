# VoiceManager — analisi

## Ruolo nell'architettura

`VoiceManager` calcola gli offset per-voce nel sistema multi-voice di PGE. Istanziato da `Stream.__init__()` come `self._voice_manager`. Chiamato in `Stream.generate_grains()` per ogni voce attiva a ogni step temporale:

```python
voice_config = self._voice_manager.get_voice_config(voice_index, t)
```

Restituisce un `VoiceConfig` (frozen dataclass) con i quattro offset dimensionali da sommare ai valori base calcolati dai controller principali.

## Classi principali

**`VoiceConfig`** (frozen dataclass)
- Attributi: `pitch_factor: float` (fattore di ratio sul pitch base, `1.0` = identità), `pointer_offset: float` (normalizzato), `pan_offset: float` (gradi), `onset_offset: float` (secondi)
- Pattern: frozen dataclass — immutabile, ephemeral per chiamata, creato on-the-fly da `get_voice_config()`
- Voice-0 invariant: pitch → `get_pitch_factor(0, ...) == 1.0`; gli altri assi → `get_*_offset(0, ...) == 0.0`. `Stream._create_grain` moltiplica `pitch_factor` direttamente sul ratio base (nessun guard `!= 0.0`, nessuna conversione `2^/12` a valle: la geometria è già nell'unità)

**`VoiceManager`**
- Attributi: `max_voices` (int), `_pitch_strategy` (opt.), `_onset_strategy` (opt.), `_pointer_strategy` (opt.), `_pan_strategy` (opt.), `_pan_spread` (StrategyParam: float o Envelope)
- Metodi chiave: `get_voice_config(voice_index, time) → VoiceConfig`; delega alle quattro strategy e risolve `pan_spread` con `resolve_param(pan_spread, time)`
- Pattern: Strategy orchestration — quattro strategy indipendenti opzionali; assenza = offset 0.0

**Strategy di pitch — `VoicePitchStrategy` (ABC):** `get_pitch_factor(voice_index, num_voices, time, unit) → float` (ratio). In PGE v4.0.0 (PR #84) il metodo non emette più un offset in semitoni (`get_pitch_offset`) ma un **fattore di ratio**; la geometria della distribuzione vive nella `PitchUnit` passata (`unit`), non nella strategy.

| Implementazione | Comportamento |
|-----------------|---------------|
| `StepPitchStrategy` | posizione voce i = i, ampiezza = step(t) → `unit.materialize(i, step(t))`. Con `semitones`: passo lineare in semitoni; con `unit: ratio`: geometrico `step^i` (ottave pulite per step=2) — **breaking sui valori delle voci ≥2 vs pre-v4.0.0** |
| `RangePitchStrategy` | posizione voce i = i/(num_voices−1) ∈ [0,1], ampiezza = `pitch_range(t)` (rinominato da `semitone_range`) → `unit.materialize(position, pitch_range(t))`. Es. semitones, pitch_range=12, 4 voci → [0,4,8,12] st |
| `ChordPitchStrategy` | accordo nominale (es. `dom7`, `maj`, `altered`); extend all'ottava se num_voices > len(chord); supporta `inversion`. **Semitone-locked**: offset assoluti in semitoni via `unit.to_ratio`, accetta solo `unit: semitones` |
| `StochasticPitchStrategy` | posizione fissa per voce (seed `hash(stream_id+voce)`, stabile entro un run, non fra run); `_cache[vi] ∈ [-1,1]`; fattore = `unit.materialize(_cache[vi], pitch_range(t))`. EDO → distribuzione ± attorno all'identità; `unit: ratio` → geometrica sempre positiva (niente ratio sub-zero) |
| `SpectralPitchStrategy` | parziali della serie armonica: voce i → round(12 × log2(i+1)) semitoni via `unit.to_ratio`. **Semitone-locked** |

Vincolo unità: `chord`/`spectral` sono definiti intrinsecamente in semitoni e accettano solo `unit: semitones` (o assente) → altre unità: `InvalidStrategyConfigError`. La vecchia chiave `voices.pitch.semitone_range` è un hard break: solleva `InvalidStrategyConfigError` con hint di migrazione (guard in `Stream._init_voice_manager`).

Accordi disponibili: maj, min, dim, aug, sus2, sus4, dom7, maj7, min7, dim7, minmaj7, dom9, maj9, min9, 9sus4, dom9s11, maj9s11, min11, dom13, min13, maj13s11, altered (22 accordi).

**Strategy di onset — `VoiceOnsetStrategy` (ABC):**

| Implementazione | Comportamento |
|-----------------|---------------|
| `LinearOnsetStrategy` | voce i → i × step(t) secondi |
| `GeometricOnsetStrategy` | voce i → step(t) × base(t)^(i-1); spaziatura esponenziale |
| `StochasticOnsetStrategy` | offset fisso per voce (seed `hash(stream_id+voce)`, stabile entro un run, non fra run), in [0, max_offset(t)] |

**Strategy di pointer — `VoicePointerStrategy` (ABC):**

| Implementazione | Comportamento |
|-----------------|---------------|
| `LinearPointerStrategy` | voce i → i × step(t); offset normalizzato equidistante |
| `StochasticPointerStrategy` | offset fisso per voce (seed `hash(stream_id+voce)`, stabile entro un run, non fra run); `_cache[vi] ∈ [-1,1]`; offset = `_cache[vi] × pointer_range(t)` — può essere negativo |

**Strategy di pan — `VoicePanStrategy` (ABC):**

| Implementazione | Comportamento |
|-----------------|---------------|
| `LinearPanStrategy` | equidistante in [−spread/2, +spread/2] |
| `RandomPanStrategy` | offset fisso per voce (seed `hash(stream_id+voce)`, stabile entro un run, non fra run); `_cache[vi] × spread/2` |
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

VoiceManager è uno dei siti tecnici del **primo contributo** (YAML DSL): N voci differenziate via quattro strategie ortogonali (pitch, onset, pointer, pan), ciascuna selezionata e parametrizzata da una singola chiave YAML. Il compositore scrive `pitch_strategy: chord, chord: dom7` + `onset_strategy: linear, step: 0.05` + `pan_strategy: linear, spread: 90` — combinazione ortogonale, una linea YAML per asse, semantica polifonica esplicita.

Precedente diretto: l'**harmonization scheme** di Truax 1994 (F=4 con N indipendente per voce, fino a 15 voci simultanee sul DMX-1000). PGE estende il meccanismo con quattro assi ortogonali invece del solo pitch (onset, pointer, pan), strategie stocastiche per voce con offset stabile entro l'esecuzione, e supporto a unità pitch arbitrarie (semitoni, cents, EDO, ratio) via `PitchUnit` — dettaglio tecnico di `sec:voci`, non proposta autonoma.

> **Nota su stocasticità e riproducibilità (verificato 2026-05-31).** Le strategie *Stochastic*/*Random* seminano un RNG locale con `seed = hash(stream_id + str(voice_index))`; poiché `hash()` di stringa è randomizzato per-processo, l'offset per voce è stabile *entro* un run ma cambia *fra* run. Il nucleo stocastico per-grano — `ProbabilityGate` (`dephase`), distribuzione async (`density_controller`), scelta finestra — usa il modulo `random` globale non seminato. Quindi due run dello stesso YAML producono grani diversi. **Questo è voluto, non un difetto: è la natura della tendency mask** (cfr. [[tendency-mask]]). Il bit-identico non è un obiettivo del progetto né del paper; ciò che si conserva fra run è l'**andamento** — densità, dispersione, traiettoria, distribuzione delle voci. Vedi `CLAUDE.md` di progetto, "Riproducibilità: andamento, non bit-identico", e [[parameter-orchestrator]]/[[stream]].

Le voci sono visibili nella partitura grafica (**secondo contributo**) come frecce parallele sull'asse Y: il compositore osserva direttamente come le strategie distribuiscono le voci nel buffer e nel tempo, e modifica la specifica YAML in base a ciò che legge. Senza questa proiezione visiva il layering multi-voce sarebbe verificabile solo all'ascolto.

Il `scatter` menzionato in `stream.md` è separato — non gestito da VoiceManager — e regola il blend IOT condiviso/indipendente in `Stream.generate_grains()`.

## Sezioni del paper CIM 2026 dove descrivere

- **`sec:voci`** (primaria): quattro assi ortogonali di differenziazione,
  strategie intercambiabili, `scatter` come accoppiamento temporale.

Lessico nel paper: le voci, il blocco `voices` (mai `VoiceManager`).

## Domande aperte

- `ChordPitchStrategy` con `inversion`: il rivolto ruota gli intervalli — effetto percettivo (voce più grave diversa) rilevante per sezione compositiva?
- `pan_spread` come Envelope: apertura spaziale variabile nel tempo — caso d'uso per sezione compositiva?
