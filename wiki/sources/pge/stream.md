# Stream / StreamConfig / StreamContext — analisi

## Ruolo nell'architettura

`Stream` è il nucleo della sintesi granulare: riceve il dict YAML di uno stream, istanzia tutti i controller specializzati, genera la lista completa di `Grain`. Ispirato esplicitamente al DMX-1000 di Barry Truax (1988).

`StreamConfig` e `StreamContext` sono dataclass frozen che trasportano configurazione e contesto lungo tutta la catena dei controller.

Pipeline interna:
```
dict YAML
  → StreamContext (identità: id, onset, duration, sample, sample_dur_sec)
  → StreamConfig  (comportamento: time_mode, distribution_mode, dephase, ...)
  → _init_grain_reverse() (semantica reverse YAML — step separato, prima dei parametri)
  → ParameterOrchestrator  (parametri YAML → oggetti Parameter)
  → Controller×4 (Pointer, Pitch, Density, Window)
  → VoiceManager (strategie multi-voce: num_voices, scatter, pitch/onset/pointer/pan)
  → generate_grains() → List[List[Grain]]
```

## Classi principali

### StreamContext (frozen dataclass)
Identità dello stream: `stream_id`, `onset`, `duration`, `sample`, `sample_dur_sec`.  
Costruita con `StreamContext.from_yaml()` + durata sample dal filesystem.

### StreamConfig (frozen dataclass)
Regole di processo condivise tra Stream e tutti i controller:
- `time_mode`: `absolute` (default) o `normalized` (0.0–1.0 → durata reale)
- `distribution_mode`: `uniform` (default) o altro
- `dephase`: `False` / `True` / `dict` / `list` — controllo variazione stocastica per parametro
- `range_always_active`: `bool`
- `time_scale`: `float`
- `context`: puntatore a `StreamContext`

### Stream
Attributi principali:
- `voices: List[List[Grain]]` — grani per voce (struttura canonica)
- `grains: List[Grain]` — flatten + sort per onset (backward compatibility con Generator/ScoreVisualizer)
- `grain_reverse_mode`: `True` (forzato YAML) o `'auto'` (segue pointer_speed)
- Controller privati: `_pointer`, `_pitch`, `_density`, `_window_controller`, `_voice_manager`
- Parametri (assegnati come attributi da ParameterOrchestrator): `grain_duration`, `volume`, `pan`, `reverse`
- `_num_voices`, `_scatter`: Parameter privati gestiti da `_init_voice_manager()`, NON da ParameterOrchestrator. `num_voices` esposto via property; `scatter` acceduto come `self._scatter` internamente in `generate_grains()`.

**Parametri obbligatori YAML:** `stream_id`, `onset`, `duration`, `sample` — errore esplicito se mancanti.

**Sintassi reverse YAML (non ovvia):**
- chiave assente → `auto` (segue pointer_speed)
- `reverse:` senza valore (None) → forzato reverse
- `reverse: true/false` → ERRORE intenzionale (semantica ristretta)

## Comportamento runtime — generate_grains()

Algoritmo multi-voce con cursori temporali indipendenti:
1. Pre-alloca `all_voice_grains[max_voices]`
2. `voice_cursors[max_voices]` — tutti a 0.0
3. Loop `while any(cursor < duration)`:
   - Voice 0 calcola `sync_iot` (inter-onset time) e `scatter_val`
   - Per ogni voce attiva (`voice_index < num_voices.get_value(t)`):
     - Calcola VoiceConfig (offset pitch/pointer/pan/onset)
     - Chiama `_create_grain(t, grain_dur, voice_config)`
     - IOT voce: blend tra `sync_iot` (condiviso) e `indep_iot` pesato da `scatter`
4. Flatten + sort per onset → `self.grains`

**Invariante:** `num_voices` è time-varying (Envelope) — il numero di voci attive può cambiare durante lo stream.

### _create_grain()
Per ogni grano:
1. **Pitch:** `PitchController.calculate()` × `voice.pitch_factor` (moltiplicazione diretta del fattore di ratio; in v4.0.0 non più `2^(voice.pitch_offset/12)` — la geometria è già nella `PitchUnit`, nessun guard `!= 0.0`)
2. **Pointer:** `PointerController.calculate()` + `voice.pointer_offset`, poi **re-wrap** in `[0, sample_dur)` via `% self.sample_dur_sec` (fix issue #79: prima l'offset di voce restava oltre `sample_dur`, e `ScoreVisualizer` clippava le voci sopra il bordo del buffer facendole "ricomparire insieme" al wrap della voce 0; ora `grain.pointer_pos` è la posizione reale di lettura, condivisa da audio e partitura)
3. **Volume:** `volume.get_value(t)`
4. **Pan:** `pan.get_value(t)` + `voice.pan_offset`
5. **Onset:** `self.onset + elapsed + voice.onset_offset`
6. **Window:** `WindowController.select_window(t)` → lookup `window_table_map`

> v4.0.0 ha rimosso le property legacy `Stream.pitch_ratio` / `Stream.pitch_semitones` (ratio/semitoni-only, prive di consumer). La visualizzazione legge ora `Stream.pitch_value` + `Stream.pitch_unit`, validi per ogni unità.

## Collegamento alla tesi centrale

Stream è il nucleo del **primo contributo** (YAML come DSL → IR dichiarativa → grani): riceve un dict YAML di intenzioni parametriche e produce una `List[List[Grain]]` — migliaia di grani discreti che il YAML non specifica direttamente. La pipeline interna (`StreamContext` → `StreamConfig` → `_init_grain_reverse` → `ParameterOrchestrator` → controller×4 → `VoiceManager` → `generate_grains`) materializza il pattern DSL → IR → backend documentato per la prima volta da Roads (1978, AGS → MUSIC V) e ispirato qui esplicitamente al DMX-1000 di Truax (1988): il codice cita Truax nel docstring. La IR è lo Stream dichiarativo costruito da `__init__` (Parameter, controller, strategie); i grani sono la realizzazione della IR, non la IR stessa ([[intermediate-representation]]).

Due conseguenze per la tesi:

1. **YAML come DSL di intenzioni, non score deterministico.** Ogni parametro è un `Parameter` con Envelope time-varying e gate stocastico (`dephase`); due esecuzioni dello stesso YAML con `dephase` attivo producono output diversi. Stream è il punto della pipeline dove la IR si costruisce — coerente con la posizione del paper: il YAML è più vicino alle tendency masks di Truax che a uno score Csound grezzo.

2. **Output di `generate_grains` = dato per partitura grafica (secondo contributo).** `voices: List[List[Grain]]` e `grains: List[Grain]` sono letti direttamente da `ScoreVisualizer` per costruire la rappresentazione su piano tempo × posizione-buffer. La partitura non è una traccia parallela: è proiezione visiva della struttura interna di Stream.

Stream è anche il granulo del **terzo contributo** (workflow STEMS): la cache SHA-256 e l'export Reaper operano per-stream, e l'identità definita da `StreamContext.from_yaml()` è la chiave del fingerprint.

## Sezioni del paper CIM 2026 dove descrivere

- **`sec:architettura`** (primaria): il loop di generazione che campiona la IR
  e materializza la lista di `Grain` (contratto fra generazione e uscita).

Lessico nel paper: stream, loop di generazione, `Grain`.

## Domande aperte

- `ParameterOrchestrator.create_all_parameters()`: come risolve `dephase` per parametro? Da analizzare `parameter_orchestrator.py`.
- ~~`scatter`~~: **risolto** (→ density-controller.md). Voice 0 calcola `sync_iot`; le altre voci blendano tra `sync_iot` e `indep_iot` pesato da `scatter_val`. `scatter=0` → texture compatta; `scatter=1` → ogni voce IOT indipendente. Semantica musicale: gradazione continua metrica↔stocastica.

- ~~`time_mode: normalized`~~: **risolto** (→ pointer-controller.md). La normalizzazione avviene in `PointerController._pre_normalize_loop_params()`, prima del pipeline `ParameterOrchestrator`. È l'unico punto del sistema che legge `loop_unit` direttamente; i valori scalati entrano nel pipeline già in secondi assoluti.
