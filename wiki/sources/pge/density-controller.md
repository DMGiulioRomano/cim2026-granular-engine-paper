# DensityController — analisi

## Ruolo nell'architettura

`DensityController` calcola l'inter-onset time (IOT) tra grani consecutivi, implementando il modello temporale di Truax. Istanziato da `Stream.__init__()` come `self._density`. Chiamato in `Stream.generate_grains()` con scatter blending per voce:

```python
# Voice 0 è il riferimento: definisce sync_iot e scatter
sync_iot = self._density.calculate_inter_onset(t0, grain_dur_0)
scatter_val = self._scatter.get_value(t0)

# per ogni voce attiva:
if voice_index == 0 or scatter_val == 0.0:
    iot = sync_iot                                          # voci sincrone
else:
    indep_iot = self._density.calculate_inter_onset(t, grain_dur)
    iot = (1.0 - scatter_val) * sync_iot + scatter_val * indep_iot  # blend

voice_cursors[voice_index] += iot
```

`scatter=0` → tutte le voci avanzano con lo stesso IOT (texture compatta). `scatter=1` → ogni voce calcola il proprio IOT indipendente (texture stocastica multi-strato). Valori intermedi: blend continuo.

IOT è il parametro che governa la texture granulare nel tempo: basso IOT → texture densa continua; alto IOT → grani isolati percepibili singolarmente.

## Classi principali

**`DensityController`**
- Attributi: `_orchestrator` (ParameterOrchestrator), `_strategy` (strategy selezionata da ExclusiveGroupSelector tra `fill_factor` e `density`), `distribution_param` (Parameter autonomo, separato dal gruppo esclusivo)
- Metodi chiave:
  - `calculate_inter_onset(elapsed_time, current_grain_duration) → float`: entry point pubblico; richiama `_strategy.calculate_density()` poi `_apply_truax_distribution()`
  - `_find_selected_param() → str`: rileva quale parametro esclusivo è sopravvissuto; non decide — la priorità è già in `ExclusiveGroupSelector`
  - `_apply_truax_distribution(avg_iot, elapsed_time) → float`: implementa il modello Truax; blend lineare tra IOT sincrono e casuale in base a `distribution`
- Properties: `mode` (nome strategy attiva), `distribution`, `fill_factor`, `density` (accesso ai Parameter sottostanti)
- Pattern: Strategy (selezione tramite `ExclusiveGroupSelector`) + `ParameterOrchestrator` per parsing

## Comportamento runtime

**Due modalità mutuamente esclusive:**

**fill_factor** (prioritaria se presente):
```
density = fill_factor / grain_duration
```
La densità si adatta automaticamente alla durata del grano. `fill_factor=1.0` → grani contigui (no overlap, no gap). `fill_factor>1.0` → overlap. `fill_factor<1.0` → gap tra grani. Controllo percettivo diretto: il compositore specifica "saturazione temporale", non grani/secondo.

**density** (esplicita):
```
density = valore fisso o Envelope  [grani/secondo]
```
Controllo diretto. Preferita quando la texture desiderata è indipendente dalla durata del singolo grano.

La selezione è delegata a `ExclusiveGroupSelector` (in `ParameterOrchestrator`) — se entrambe presenti nel YAML, `fill_factor` vince. Il `DensityController` non decide: trova quale parametro è sopravvissuto alla selezione.

**Distribuzione Truax — `_apply_truax_distribution()`:**

```python
avg_iot = 1.0 / density

if dist_val <= 0.0:              # SYNCHRONOUS
    return avg_iot               # metronomo perfetto

else:                            # ASYNC o BLEND (distribution > 0)
    async_iot = random.uniform(0.0, 2.0 * avg_iot)
    return (1.0 - dist_val) * avg_iot + dist_val * async_iot
    # dist=1.0 → return async_iot puro (Poisson-like)
```

**distribution = 0** → texture sincrona: ogni grano nasce a distanza fissa. Periodica, metrica, meccanica.
**distribution = 1** → texture asincrona: IOT casuale tra 0 e 2×avg. Media preservata, distribuzione stocastica.
**distribution intermedia** → blend lineare: gradazione continua tra metrica e stocastica.

`distribution` è un `Parameter` autonomo — può essere Envelope: il compositore compone una transizione da texture sincrona a stocastica nel tempo, senza specificare ogni singolo IOT.

## Collegamento alla tesi centrale

DensityController è il punto dove il gap controllo/percezione si manifesta più direttamente.

Il compositore specifica:
- `density: 50` → "voglio 50 grani al secondo" (intenzione percettiva)
- `distribution: 0.7` → "con quest'ansia sincopata" (qualità della texture)

Il controller traduce in IOT discreti per ogni grano — migliaia di decisioni concrete da un'unica coppia di valori. Questo è esattamente il livello di astrazione che Truax (1990) identifica come necessario per rendere la granulare praticabile compositivamente.

`fill_factor` porta il controllo ancora più in alto: il compositore pensa in termini di "quanto spazio occupa questa texture" piuttosto che "quanti grani al secondo". Completamente invariante alla durata del grano — parametro perceptual-first.

Il parametro `distribution` come Envelope è l'implementazione della  "morphing texture" — concetto centrale nella composizione granulare di Roads (2001) e nel lavoro di Truax stesso. 
⚠️ **Da verificare in Zotero prima di scrivere sezione 2:** la data originale "1991" non ha corrispondenza in refs.bib. Se non esiste un roads 1991, la citazione è Roads2001 (Microsound). Se esiste, va aggiunto a Zotero e a bibliography.md prima della submission.

## Sezioni del paper CIM 2026 dove descrivere

- Sezione 2 (Contesto teorico): distribuzione Truax sincrona/asincrona — la citazione va qui con riferimento diretto al codice
- Sezione 3 (Architettura): fill_factor come esempio di controllo perceptual-first nel DSL
- Sezione 4 (Partitura grafica): density visibile come frequenza delle frecce nell'asse temporale

## Domande aperte

- `distribution` come Envelope: il blend avviene ogni grano → la transizione sincrona→asincrona è a livello di grano, non di stream. Vale la pena menzionare nel paper come granularità del controllo?
- `fill_factor > 1.0` (overlap): come si comporta il renderer Csound con grani overlappati? La partitura grafica mostra sovrapposizione?
