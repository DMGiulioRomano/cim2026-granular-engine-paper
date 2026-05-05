# StreamCacheManager — analisi

## Ruolo nell'architettura

Build incrementale per il pipeline Csound (attivo solo con `STEMS=true CACHE=true RENDERER=csound`). Evita di rigenerare `.sco` e ricompilare `.aif` per stream invariati tra sessioni.

Posizione nella pipeline:
```
Generator.generate_score_files_per_stream(cache_manager=...) 
  → StreamCacheManager.get_dirty_stream_dicts()  ← decide chi riscrivere
  → [scrittura .sco solo per dirty]
  → StreamCacheManager.update_after_build()       ← aggiorna manifest
```

## Classi principali

**StreamCacheManager**
- Attributo: `cache_path: str` — path del file manifest JSON su disco
- Nessuno stato in-memory oltre il path: carica/salva manifest a ogni operazione

**Metodi:**
- `compute_fingerprint(stream_dict)` → SHA-256 del JSON serializzato con `sort_keys=True`
- `load()` → `Dict[stream_id, fingerprint]`, vuoto se file assente o malformato
- `save(manifest)` — crea directory genitore se mancante
- `is_dirty(stream_dict, aif_path)` → `True` se: stream_id assente nel manifest, fingerprint cambiato, o file `.aif` mancante su disco
- `get_dirty_stream_dicts(stream_dicts, aif_dir, aif_prefix)` → lista dei dict dirty (logga ogni stream)
- `update_after_build(stream_dicts)` → aggiorna fingerprint nel manifest per i dict buildati
- `garbage_collect(current_stream_ids, aif_dir, aif_prefix)` → rimuove entry orfane dal manifest + cancella `.aif` corrispondenti

## Comportamento runtime

Fingerprint = SHA-256 del dict YAML raw dello stream serializzato come JSON. `sort_keys=True` garantisce stabilità indipendente dall'ordine chiavi.

Tre condizioni di dirty (OR):
1. `stream_id` non in manifest (prima build)
2. fingerprint corrente ≠ fingerprint salvato (YAML modificato)
3. file `.aif` assente su disco (build precedente incompleta o file cancellato)

Il manifest è un file JSON semplice: `{stream_id: "sha256hex", ...}`.

## Collegamento alla tesi centrale

Contributo tecnico secondario (non tesi principale). Rilevante per uso produttivo del sistema: pipeline granulare con molti stream (>10) ha tempi di compilazione Csound significativi; la cache incrementale rende praticabile la composizione iterativa.

Menzionare nella sezione Architettura come feature del pipeline Csound, non come contributo principale.

## Sezioni del paper CIM 2026 dove descrivere

- Sezione 3 (Architettura): cenno come ottimizzazione della pipeline Csound
- Non approfondire — spazio limitato (6–8 pp) e non centrale alla tesi

## Domande aperte

- Il garbage_collect viene chiamato automaticamente o richiede invocazione esplicita? Da verificare in `main.py`.
- La cache è per-brano (una directory per progetto YAML) o globale? Dipende da dove `cache_path` è impostato da `main.py`.
