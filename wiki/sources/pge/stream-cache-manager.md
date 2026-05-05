# StreamCacheManager — analisi

## Ruolo nell'architettura

Build incrementale per il pipeline (Attivo in modalità STEMS (--per-stream) con flag --cache, indipendentemente dal renderer (NumPy o Csound). In MIX mode la cache non è applicabile: l'output è un file unico, non per-stream). 

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

Contributo tecnico secondario (non tesi principale). La cache è il meccanismo che rende praticabile il workflow STEMS su composizioni di durata reale. Con brani che hanno decine di stream e un renderer esterno (come Csound), il tempo di compilazione per build completa può essere di minuti — la cache riduce ogni iterazione al solo stream modificato. Questo chiude il loop modifica/ascolto che altrimenti renderebbe la composizione iterativa impraticabile.

Funziona con entrambi i renderer (NumPy e Csound): il vincolo è la modalità STEMS (`--per-stream`), non il tipo di renderer. In MIX mode la cache non è applicabile: l'output è un file unico, non per-stream.

Menzionare nella Sezione 3 come feature del workflow STEMS, non come contributo principale.

## Sezioni del paper CIM 2026 dove descrivere

- Sezione 3 (Architettura): cenno come ottimizzazione della pipeline Csound
- Non approfondire — spazio limitato (6–8 pp) e non centrale alla tesi

## Domande aperte

- Il garbage_collect viene chiamato automaticamente o richiede invocazione esplicita? Da verificare in `main.py`.
- La cache è per-brano (una directory per progetto YAML) o globale? Dipende da dove `cache_path` è impostato da `main.py`.
