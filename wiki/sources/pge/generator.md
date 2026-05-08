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

Generator è l'orchestratore della pipeline e tocca due dei tre contributi del paper:

1. **Primo contributo (YAML DSL).** `_eval_math_expressions` valuta espressioni inline `(pi * 2)`, `(max 3 7)` in sandbox prima del parsing parametri: il compositore può scrivere unità concettuali nel DSL invece di valori numerici raw, abbassando il costo cognitivo della specifica e accorciando ogni iterazione del loop lungo.

2. **Terzo contributo (workflow STEMS).** `generate_score_files_per_stream(cache_manager=...)` è il punto in cui per-stream rendering, cache SHA-256 incrementale e garbage collection si compongono. La logica `_filter_solo_mute` permette di isolare singoli stream senza modificare la struttura YAML — meccanismo tecnico del ciclo modifica-un-parametro → riascolta che rende praticabile il loop lungo iterativo.

`_register_stream_windows` (pre-registrazione finestre prima della generazione grani) è invariante critico per la stabilità della numerazione ftable — vincolo tecnico, non legato alla tesi.

## Sezioni del paper CIM 2026 dove descrivere

- Sezione 3 (Architettura): pipeline YAML → SCO, ruolo orchestratore, delegati; matematica inline come parte del DSL (primo contributo); `generate_score_files_per_stream` + cache + solo/mute come parti del workflow STEMS (terzo contributo)

## Domande aperte

- `stream_data_map` passato a `cache_manager`: come viene serializzato per il fingerprint?
- Qual è il formato esatto del file `.sco` generato da `ScoreWriter`?
