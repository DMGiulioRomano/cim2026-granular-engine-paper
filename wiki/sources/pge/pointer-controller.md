# PointerController — analisi

## Ruolo nell'architettura

`PointerController` gestisce la posizione della testina di lettura nel sample sorgente per ogni grano. Istanziato da `Stream.__init__()` come `self._pointer`. Chiamato in `Stream._create_grain()` con `elapsed_time` dello stream per ottenere la posizione in secondi nel buffer.

Pipeline interna:
```
YAML pointer dict
  → _pre_normalize_loop_params()   # converte normalized → secondi
  → ParameterOrchestrator          # crea Parameter per ogni sotto-parametro
  → calculate(elapsed_time)        # restituisce posizione in secondi
```

## Classi principali

**`PointerController`**
- Attributi fissi: `_config` (StreamConfig), `_sample_dur_sec` (float), `_orchestrator` (ParameterOrchestrator), `has_loop` (bool), `_loop_is_dynamic` (bool)
- Attributi dinamici (impostati via `setattr` da `_init_params`): `start`, `speed_ratio`, `deviation`, `loop_start`, `loop_end`, `loop_dur` — ciascuno è un `Parameter`
- Stato loop (mutabile): `_in_loop`, `_loop_absolute_pos`, `_last_linear_pos`, `_prev_loop_start`, `_prev_loop_end`
- Metodi chiave:
  - `calculate(elapsed_time, grain_duration, grain_reverse) → float`: entry point; compone posizione lineare + loop + deviazione per-grano
  - `_calculate_linear_position(elapsed_time) → float`: `start + ∫speed_ratio dt`; se `speed_ratio` è Envelope, integrazione via `Envelope.integrate()`
  - `_apply_loop(linear_pos, elapsed_time) → tuple[float, float]`: phase accumulator con rilevazione bounds-change e wrap modulare
  - `_pre_normalize_loop_params(params) → dict`: unico punto che legge `loop_unit`; se `normalized`, scala `start`, `loop_start`, `loop_end`, `loop_dur` per `sample_dur_sec`
  - `reset()`: azzera stato loop per riuso
- Properties: `sample_dur_sec`, `in_loop`, `loop_phase` (fase 0.0–1.0 nel loop corrente)
- Pattern: Phase Accumulator (inerziale, aggiorna posizione assoluta incrementalmente) + ParameterOrchestrator per parsing

**Parametri YAML principali:**

| Parametro | Tipo | Significato |
|-----------|------|-------------|
| `start` | float | posizione iniziale nel sample (secondi o normalizzata) |
| `speed_ratio` | float / Envelope | velocità di scansione (1.0 = real-time) |
| `deviation` | float / Envelope | jitter per-grano, normalizzato su loop_length |
| `loop_start` | float / Envelope | inizio finestra di loop |
| `loop_end` / `loop_dur` | float / Envelope | fine o durata finestra di loop |
| `loop_unit` | `'normalized'` / assente | se `normalized`: [0,1] → secondi prima del parsing |

## Comportamento runtime

Tre stadi in `calculate()`:

**1. Posizione lineare:**
```
linear_pos = start + ∫₀ᵗ speed_ratio(t) dt
```
Se `speed_ratio` è costante: `start + elapsed × speed_ratio`.
Se `speed_ratio` è Envelope: integrazione numerica via `Envelope.integrate()`.

**2. Loop (se `loop_start` presente):**
- **Statico**: il pointer entra nel loop quando la posizione lineare interseca `[loop_start, loop_end)`. Poi usa phase accumulator inerziale: `pos += delta_pos` per ogni grano. Wrap modulare quando supera `loop_end`.
- **Dinamico** (`loop_start` è Envelope): il pointer entra nel loop immediatamente a `t=0` a `loop_start(0)`. La finestra si muove nel tempo — il pointer la segue per inerzia. Se esce dai bounds (la finestra si è spostata), reset a `loop_start` corrente.

**3. Deviazione per-grano:**
```
final_pos = base_pos + deviation(t) × loop_length
```
`deviation` è un offset normalizzato rispetto alla finestra attiva. Non modifica lo stato del loop: è variazione micro per-grano. Wrap finale sempre sul sample intero.

**Normalizzazione `loop_unit`:** avviene in `_pre_normalize_loop_params()`, chiamato prima del pipeline standard. Legge `loop_unit` dal dict raw YAML (o fallback a `config.time_mode`). Se `normalized`: moltiplica `start`, `loop_start`, `loop_end`, `loop_dur` per `sample_dur_sec`. I valori scalati entrano nel pipeline come secondi assoluti. Questo è l'unico punto del sistema che legge `loop_unit` direttamente: è un meta-parametro che controlla l'interpretazione degli altri, non un valore sintetizzabile.

## Collegamento alla tesi centrale

PointerController è la materializzazione diretta del concetto di "testina di lettura" di Truax (DMX-1000, 1988). Il codice cita esplicitamente Truax nel docstring.

Due livelli di controllo che riducono il gap controllo/percezione:
1. **speed_ratio come Envelope**: il compositore specifica una traiettoria di scansione del buffer — velocità variabile nel tempo traduce in morfologia timbrica continua
2. **loop dinamico**: `loop_start` come Envelope permette di specificare "scansiona questa regione del buffer, poi sposta la finestra" — controllo percettivo diretto senza specificare ogni singolo grano

Il pointer è anche l'asse X della partitura grafica (ScoreVisualizer): la traiettoria nel buffer è visibile come posizione orizzontale delle frecce-grano. Ciò che il compositore compone con `speed_ratio` + `loop_start` è leggibile visivamente nella partitura.

## Sezioni del paper CIM 2026 dove descrivere

- Sezione 2 (Contesto teorico): `speed_ratio` come implementazione della testina Truax
- Sezione 3 (Architettura): loop statico vs dinamico come esempio di DSL espressivo
- Sezione 4 (Partitura grafica): asse X = posizione pointer → visualizzazione diretta della traiettoria

## Domande aperte

- `deviation` su loop dinamico: se la finestra si sposta, la deviazione scala rispetto alla finestra mobile — il grano può "sfuggire" al loop. Semantica intenzionale (bypass) o artefatto? Chiarire per sezione 3.
- `speed_ratio < 0`: lettura inversa nel buffer. Interazione con `grain_reverse`?
