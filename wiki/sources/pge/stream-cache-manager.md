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

`StreamCacheManager` è componente tecnico del **terzo contributo** del paper (workflow STEMS: rendering per-stream, cache incrementale, export DAW). Con brani che hanno decine di stream e un renderer esterno come Csound, il tempo di build completa può essere di minuti; la cache riduce ogni iterazione al solo stream modificato e chiude il ciclo modifica-un-parametro → riascolta che il loop lungo richiede. Senza cache, il loop lungo collasserebbe sotto i tempi di render totale: la cache è ciò che rende il workflow iterativo praticabile, non un'ottimizzazione opzionale.

Tre meccanismi rilevanti per la tesi:
1. **Fingerprint SHA-256** sul dict YAML serializzato (`sort_keys=True`): identità stabile dello stream indipendente dall'ordine chiavi YAML — il compositore può riformattare senza invalidare la cache.
2. **Tre condizioni di dirty in OR** (`stream_id` nuovo, fingerprint cambiato, file `.aif` mancante): tollerante a build incomplete o file cancellati a mano.
3. **`garbage_collect`** rimuove entry orfane e file `.aif` corrispondenti per stream rinominati o rimossi: la cache resta coerente attraverso le iterazioni del loop lungo, non accumula stato morto.

Funziona con entrambi i renderer (NumPy e Csound): il vincolo è la modalità STEMS (`--per-stream`), non il tipo di renderer. In MIX mode la cache non è applicabile: l'output è file unico, non per-stream.

## Sezioni del paper CIM 2026 dove descrivere

- Sezione 3 (Architettura): cache SHA-256 + dirty detection + garbage collect come parte del workflow STEMS (terzo contributo) — il meccanismo che rende il loop lungo iterativo praticabile su brani reali

## Domande aperte

- Il garbage_collect viene chiamato automaticamente o richiede invocazione esplicita? Da verificare in `main.py`.
- La cache è per-brano (una directory per progetto YAML) o globale? Dipende da dove `cache_path` è impostato da `main.py`.
