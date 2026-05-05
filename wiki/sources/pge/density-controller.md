# DensityController — analisi

## Ruolo nell'architettura

`DensityController` calcola l'inter-onset time (IOT) tra grani consecutivi, implementando il modello temporale di Truax. Istanziato da `Stream.__init__()` come `self._density`. Chiamato in `Stream.generate_grains()`:

```python
iot = self._density.calculate_inter_onset(elapsed_time, current_grain_duration)
voice_cursors[0] += iot  # determina quando nasce il prossimo grano
```

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

if distribution == 0.0:          # SYNCHRONOUS
    return avg_iot               # metronomo perfetto

elif distribution == 1.0:        # ASYNCHRONOUS
    return random.uniform(0.0, 2.0 * avg_iot)  # Poisson-like

else:                            # INTERPOLAZIONE
    async_iot = random.uniform(0.0, 2.0 * avg_iot)
    return (1 - distribution) * avg_iot + distribution * async_iot
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

Il parametro `distribution` come Envelope è l'implementazione della "morphing texture" — concetto centrale nella composizione granulare di Roads (1991/2001) e nel lavoro di Truax stesso.

## Sezioni del paper CIM 2026 dove descrivere

- Sezione 2 (Contesto teorico): distribuzione Truax sincrona/asincrona — la citazione va qui con riferimento diretto al codice
- Sezione 3 (Architettura): fill_factor come esempio di controllo perceptual-first nel DSL
- Sezione 4 (Partitura grafica): density visibile come frequenza delle frecce nell'asse temporale

## Domande aperte

- `distribution` come Envelope: il blend avviene ogni grano → la transizione sincrona→asincrona è a livello di grano, non di stream. Vale la pena menzionare nel paper come granularità del controllo?
- `fill_factor > 1.0` (overlap): come si comporta il renderer Csound con grani overlappati? La partitura grafica mostra sovrapposizione?
