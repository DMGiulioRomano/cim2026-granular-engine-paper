# Renderer (Csound / NumPy / Reaper) — analisi

## Ruolo nell'architettura

Layer di output: converte la lista di `Grain` prodotta da `Stream` in audio o progetto DAW. Tre renderer concreti implementano l'interfaccia astratta `AudioRenderer`.

Pattern: OCP (Open-Closed Principle) — aggiungere un renderer non richiede modificare il codice esistente. `RendererFactory` seleziona il renderer dal flag `--renderer` a CLI.

Pipeline per renderer:
```
Stream.grains/voices
  → CsoundRenderer:  ScoreWriter → .sco → csound subprocess → .aif
  → NumpyAudioRenderer: overlap-add NumPy in-memory → .aif
  → ReaperProjectWriter: stream.onset/duration → .rpp (riferimenti .aif)
```

## AudioRenderer ABC

Due metodi atomici:
- `render_single_stream(stream, output_path)` — STEMS mode: un file per stream, onset relativi (parte da 0)
- `render_merged_streams(streams, output_path)` — MIX mode: tutti gli stream in un file, onset assoluti

## CsoundRenderer

**Adapter pattern:** wrappa la pipeline storica (ScoreWriter → .sco → `csound` subprocess) nell'interfaccia AudioRenderer. Non modifica `ScoreWriter`, `FtableManager`, `main.orc`.

Attributi: `score_writer`, `csound_config` (orc_path, env_vars, log_dir, message_level), `cartridges`, `cache_manager`, `stream_data_map`, `sco_dir`

Pipeline per stream singolo (`render_single_stream`):
1. Cache check via `StreamCacheManager.is_dirty()` — skip se clean
2. `_write_score()` → ScoreWriter → `.sco` (tempfile o path deterministico con `--keep-sco`)
3. `_run_csound()` → `subprocess.run(['csound', '--env:...', '-m', orc, sco, '-o', aif])`
4. Cleanup `.sco` temporaneo (se non `--keep-sco`)
5. `cache_manager.update_after_build()` — aggiorna fingerprint

Differenza STEMS/MIX: onset relativi (per-stream) vs assoluti (tutti insieme + cartridges).

## NumpyAudioRenderer

**Overlap-add** in Python puro senza Csound. Renderer alternativo (flag `--renderer numpy`).

Attributi: `sample_registry` (cache .wav), `window_registry` (cache finestre), `table_map: Dict[int, (type, name)]`, `output_sr=48000`, `cache_manager`, `stream_data_map`, `_grain_renderer: GrainRenderer`

Pipeline interna (`_add_grain_at_position`):
1. Risolvi `grain.sample_table` → nome sample (via `table_map`)
2. Risolvi `grain.envelope_table` → nome finestra
3. `GrainRenderer.render(grain, sample_name, window_name)` → buffer NumPy stereo del grano
4. Clamp ai bordi buffer (grani che iniziano prima di 0 o finiscono dopo la fine)
5. `buffer[onset:end] += grain_buffer` (overlap-add)

STEMS: buffer dimensionato per `stream.duration`, onset = `grain.onset - stream.onset`  
MIX: buffer dimensionato per `max(onset+duration)`, onset = `grain.onset` assoluto

Output: `soundfile.write(..., format='AIFF')` a 48kHz stereo float64 con clamp [-1, 1].

## ReaperProjectWriter

Esporta la composizione come progetto Reaper `.rpp`. Non renderizza audio: referenzia i file `.aif` già prodotti da CsoundRenderer o NumpyAudioRenderer, non li incorpora.

Formato: un `TRACK` per stream, un `ITEM` per track, posizionato con `POSITION=onset`, `LENGTH=duration`, `SOURCE WAVE FILE=path.aif`. I valori onset, duration e stream_id vengono trasferiti direttamente da YAML senza trasformazione intermedia.

Attivo con flag `--reaper`, indipendente da `--per-stream`. Comportamento per modalità:
- **STEMS mode**: ogni TRACK punta al proprio `.aif` dedicato — struttura temporale e isolamento per stream completi
- **MIX mode**: tutti i TRACK puntano al file mix unico, ma con onset/duration del proprio stream — consente analisi visiva della struttura compositiva anche senza STEMS

## Collegamento alla tesi centrale

L'architettura renderer contribuisce al gap controllo/percezione su due livelli:

`NumpyAudioRenderer` è il renderer nativo: rendering in-memory senza dipendenze esterne, abbassa la barriera di installazione e rende PGE utilizzabile in contesti didattici senza Csound (sezione 6 del paper). `CsoundRenderer` è disponibile come renderer esterno alternativo per chi già lavora nella tradizione Csound/Roads.

Il workflow STEMS+cache+Reaper è il contributo compositivo più rilevante: la cache rende praticabile l'iterazione su brani con decine di stream; il progetto Reaper auto-generato trasferisce la struttura YAML direttamente in DAW senza ricostruzione manuale. Questa catena — specifica YAML → audio per-stream → DAW con timeline già mappata — è analoga al workflow multitrack di Vaggione (strati algoritmici → timeline DAW per intervento diretto), implementato però in modo interamente automatizzato.

## Sezioni del paper CIM 2026 dove descrivere

- Sezione 3 (Architettura): diagramma pipeline con i tre renderer, pattern OCP
- Sezione 6 (Proposta didattica): NumpyRenderer come enabler per contesti senza Csound
- Sezione 7 (Conclusioni): Reaper + altri renderer come direzione aperta

## Domande aperte

- `main.orc`: qual è il contenuto dell'orchestra Csound? Quali opcode granulari usa? Da vedere per capire le assunzioni sul formato `.sco`.
- `GrainRenderer.render()`: come costruisce il buffer grano? Applica pitch_ratio via resampling o via Csound opcode?
- `SampleRegistry`: carica tutto in memoria o stream? Rilevante per brani lunghi con molti sample.
- `ReaperProjectWriter` in MIX mode: le tracce puntano tutte allo stesso file mix — qual è il caso d'uso compositivo concreto rispetto a STEMS? Da chiarire nella sezione Architettura.

## Versioni software (da citare in Sezione 3)

Da recuperare nell'ambiente di produzione prima della stesura:

```bash
python --version
pip show numpy soundfile
csound --version
```
Inserire i risultati qui e citarli nella Sezione 3 del paper
come richiesto da Di Scipio (mail 2026-05).