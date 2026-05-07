# Generator — analisi

## Ruolo nell'architettura

Orchestratore principale della pipeline. Entry point della generazione: riceve path YAML, coordina tutti i sottosistemi, produce file `.sco` Csound o stems separati per stream.

Pipeline:
```
YAML → Generator.load_yaml() → Generator.create_elements() → Generator.generate_score_file()
                                      ↓                              ↓
                                   Stream              FtableManager + ScoreWriter
```

Istanziato da `main.py`. Delega a: `FtableManager` (gestione ftable), `ScoreWriter` (scrittura .sco), `Stream` (logica granulare).

## Classi principali

**Generator**
- Attributi: `yaml_path`, `data`, `streams: List[Stream]`, `ftable_manager`, `score_writer`, `stream_data_map: Dict[str, dict]`
- `load_yaml()`: carica YAML, valuta espressioni matematiche inline (es. `(pi)`, `(10/2)`) tramite `_eval_math_expressions()` con `safe_eval`
- `create_elements()`: estrae stream/cartridges da YAML, applica logica solo/mute, pre-registra finestre, genera grani
- `generate_score_file(output_path)`: delega a `ScoreWriter.write_score()`
- `generate_score_files_per_stream(...)`: uno `.sco` per stream; supporta `StreamCacheManager` per build incrementale (scrive solo stream "dirty")

**Logica solo/mute** (`_filter_solo_mute`):
- Se almeno uno stream ha flag `solo` → solo quelli
- Altrimenti → tutti tranne quelli con flag `mute`

**Pre-registrazione finestre** (`_register_stream_windows`):
- Usa `WindowController.parse_window_list()` (metodo statico)
- Registra tutte le finestre possibili per lo stream in `FtableManager` prima della generazione grani
- Invariante critico: la numerazione ftable dipende da questo ordine — non lazy-registrare

**Preprocessing YAML** (`_eval_math_expressions`):
- Ricorsione su dict/list/str
- Pattern `(espressione)` → `eval()` in sandbox con `abs, int, float, min, max, pow, pi, e`
- Converte risultato in `int` o `float` se possibile

## Comportamento runtime

1. `load_yaml()` — parse YAML + eval espressioni matematiche
2. `_filter_solo_mute()` — filtra stream
3. Per ogni stream: crea `Stream`, registra sample ftable, pre-registra finestre, chiama `stream.generate_grains()`
4. `generate_score_file()` o `generate_score_files_per_stream()` — scrittura output

Modalità cache (solo con `STEMS=true CACHE=true RENDERER=csound`):
- `StreamCacheManager.get_dirty_stream_dicts()` confronta fingerprint YAML per stream
- Solo stream dirty vengono riscritti; cartridges sempre riscritte

## Collegamento alla tesi centrale

Generator incarna il primo livello del gap controllo/percezione: traduce un DSL dichiarativo (YAML con espressioni matematiche) in score parametrico. La matematica inline (`(pi * 2)`, `(max 3 7)`) abbassa la soglia cognitiva del compositore — parametri espressi in unità concettuali, non numeriche raw.

La logica solo/mute supporta il flusso compositivo iterativo: ascolto isolato di stream singoli senza dover modificare la struttura YAML.

## Sezioni del paper CIM 2026 dove descrivere

- Sezione 3 (Architettura): pipeline YAML → SCO, ruolo orchestratore, delegati
- Sezione 4 (Partitura grafica): cenno alla separazione per-stream come base per visualizzazione

## Domande aperte

- `stream_data_map` passato a `cache_manager`: come viene serializzato per il fingerprint?
- Qual è il formato esatto del file `.sco` generato da `ScoreWriter`?
