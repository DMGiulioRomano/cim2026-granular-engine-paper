# ParameterOrchestrator + Strategie — analisi

## Ruolo nell'architettura

Collega `ParameterFactory` (crea oggetti Parameter da YAML) e `GateFactory` (crea ProbabilityGate per variazione stocastica) senza accoppiarle. È il layer che trasforma il DSL YAML in parametri eseguibili a runtime.

Usato da:
- `Stream._init_stream_parameters()` → parametri diretti dello stream
- Controller (`PointerController`, `PitchController`, `DensityController`) → parametri dei sottodomini

## Classi principali

### ParameterOrchestrator

Attributi: `_param_factory: ParameterFactory`, `_config: StreamConfig`

**`create_all_parameters(yaml_data, schema)`:**
1. `ExclusiveGroupSelector.select_parameters(schema, yaml_data)` — risolve gruppi mutualmente esclusivi (es. `density` vs `fill_factor`): il vincitore è il parametro con YAML presente e priorità più alta; il perdente riceve `None` come valore
2. Per ogni spec selezionata:
   - `is_smart=True` → `create_parameter_with_gate()` (Parameter + ProbabilityGate iniettato)
   - `is_smart=False` → `_param_factory.create_raw_parameter()` (Parameter senza gate)
3. Perdenti dei gruppi esclusivi → `None` nel dict risultante
4. Garantisce shape completa: consumer non deve testare `hasattr`

**`create_parameter_with_gate(yaml_data, param_spec)`:**
1. Crea `Parameter` base (valore + mod_range opzionale)
2. `GateFactory.create_gate(dephase, param_key, ...)` → `ProbabilityGate` appropriato
3. `param.set_probability_gate(gate)` → inietta gate nel Parameter

**`create_constant_parameter(name, value)`:** wrapper thin su ParameterFactory.

### Schema dei parametri (STREAM_PARAMETER_SCHEMA)

Schema data-driven: lista di `ParameterSpec` che descrivono ogni parametro:
- `name`: nome attributo risultante
- `yaml_path`: chiave nel dict YAML
- `default`: valore default
- `range_path`: chiave YAML per il range di variazione stocastica
- `dephase_key`: chiave nel dict `dephase:` per il gate probabilistico
- `is_smart`: se True, riceve ProbabilityGate
- `exclusive_group`, `group_priority`: per gruppi mutualmente esclusivi

### Strategie (strategie.py)

**PitchStrategy** (ABC) → `UnitPitchStrategy` (strategy unica, modello
**unit-driven** introdotto in PGE v4.0.0, PR #84). La conversione del valore di
pitch in fattore di frequenza è delegata a una `PitchUnit`
(`src/parameters/pitch_unit.py`), unica fonte di verità per conversione e bounds:
- `EdoUnit(divisions)`: famiglia Equal Division of the Octave, `to_ratio(v) = 2^(v/N)`.
  Preset: `semitones` = EdoUnit(12, `st`), `quarter_tone` = EdoUnit(24, `qt`),
  `eighth_tone` = EdoUnit(48, `et`), `cents` = EdoUnit(1200, `c`), più `{edo: N}`
  arbitrario.
- `RatioUnit`: moltiplicatore diretto (`to_ratio(v) = v`).
- Factory `make_pitch_unit(spec)`: risolve preset-stringa o `{edo: N}`; unità
  sconosciuta → `InvalidFieldValueError` con hint.
- Ogni unità espone `symbol`, `value_bounds()`, `identity_value()` e
  `materialize(position, amount)` (geometria della distribuzione voci: EDO
  additiva `2^(position·amount/N)`, ratio geometrica `amount^position`).

Le vecchie `SemitonesStrategy`/`RatioStrategy` sono state rimosse. Il blocco
`pitch` YAML accetta **una sola chiave-unità** (niente più mutua esclusione
`semitones`/`ratio` con priorità implicita): più chiavi-unità, una chiave
sconosciuta, o un blocco vuoto/non-mapping → `InvalidFieldValueError` (No Silent
Failures). Default invariato: `semitones`, valore neutro → ratio 1.0.

**DensityStrategy** (ABC) → `FillFactorStrategy` / `DirectDensityStrategy`:
- `FillFactorStrategy`: `density = fill_factor / grain_duration` (relazione durata-densità)
- `DirectDensityStrategy`: densità in grani/secondo diretta

Le due strategie incarnano i due livelli di controllo per la densità nel DSL:
- `DirectDensityStrategy` = controllo numerico (grani/sec)
- `FillFactorStrategy` = controllo perceptual-first (riempimento: quanto del tempo è occupato da grani; invariante alla durata del grano)

### GateFactory e modalità dephase

`dephase` in YAML determina il tipo di `ProbabilityGate`:
- assente / `false` → `NeverGate` (nessuna variazione stocastica)
- `true` → `AlwaysGate` o `RandomGate(DEFAULT_PROB)` (variazione sempre attiva)
- `{param_key: prob}` → `RandomGate(prob)` per parametro specifico
- `{param_key: envelope}` → `EnvelopeGate(envelope)` (probabilità time-varying)

`range_always_active: true` in StreamConfig → il range di variazione si applica anche senza gate probabilistico.

## Modello di controllo: tendency mask

PGE eredita il pattern **tendency mask** (Truax 1988, gerarchia di controllo per sintesi granulare): per ogni parametro il compositore specifica una traiettoria centrale nel tempo (Envelope) e un range di deviazione campionata indipendentemente per ogni grano.

**Meccanismo concreto** (`raw/PythonGranularEngine/src/shared/distribution_strategy.py`):
- `Parameter.value_at(t)` interpola Envelope → `center(t)` (offset time-varying).
- `mod_range` definisce `spread` (ampiezza deviazione).
- `distribution_mode: 'uniform' | 'gaussian'` seleziona via `DistributionFactory` la strategia campionatrice:
  - **UniformDistribution**: `center + random.uniform(-0.5, 0.5) * spread` → bounds `[center − spread/2, center + spread/2]`.
  - **GaussianDistribution**: `random.gauss(μ=center, σ=spread)` → ~68% in `[μ±σ]`, ~99.7% in `[μ±3σ]`; clamping ai bounds del Parameter in `Parameter._clamp()`.
- `ProbabilityGate` (`dephase`) decide *se* applicare la deviazione al grano corrente; quando aperto, il valore è il sample della distribuzione, altrimenti `center(t)` puro.

**Proprietà chiave:** valore al grano `n+1` è **indipendente** dal valore al grano `n` (nessuna memoria di stato fra grani consecutivi). Il processo è deterministico nella specifica (envelope + range + distribuzione) e statistico nella generazione (campionamento i.i.d. al grano).

**Contrasto controllato con Di Scipio 1991** (cfr. [[discipio1991]]): Di Scipio usa mappe caotiche deterministiche (logistica, Verhulst, Hénon) con dipendenza `xn+1 = f(xn)` — traiettoria deterministica ma caotica, memoria di stato fra iterazioni. Le due famiglie (tendency mask statistica vs. caos iterativo) appartengono a regimi diversi di controllo algoritmico e non sono varianti dello stesso pattern. PGE non astrae né generalizza il modello caotico-iterativo; lo affianca come alternativa nella tradizione CIM offline.

## Collegamento alla tesi centrale

ParameterOrchestrator è il componente che rende operativo il loop lungo: ogni parametro YAML può avere Envelope time-varying, variazione stocastica configurabile (dephase), e range. Il compositore specifica un'intenzione ("densità media 30 g/s, variazione ±20% con probabilità 70%") — l'orchestratore traduce in un Parameter con gate e range che il motore applica grano per grano. Il risultato sonoro emerge dall'interazione tra determinismo (envelope) e stocasticità (gate): il YAML non determina il suono, lo orienta.

`FillFactorStrategy` vs `DirectDensityStrategy` è l'esempio più diretto di corrispettivo percettivo operativo (Tabella 1 Truax 1988): `fill_factor` è il parametro con cui il compositore pensa in termini di saturazione temporale percepita; `density` in grani/secondo è il controllo tecnico. Nel loop lungo, la partitura grafica e l'ascolto permettono di verificare empiricamente quale dei due corrisponde meglio all'intenzione compositiva in un contesto specifico.

## Sezioni del paper CIM 2026 dove descrivere

- **`sec:deviazione`** (primaria): tendency mask + gate di probabilità —
  cfr. [[tendency-mask]] e [[deviazione-ampiezza-probabilita]].
- **`sec:architettura`** (secondaria, cappello): la fase dichiarativa che
  interpreta la specifica.

Lessico nel paper: interpretazione della specifica, gate di probabilità
(`dephase`), campionamento per grano.

## Domande aperte

- Qual è `DEFAULT_PROB`? Verificare in `parameter_definitions.py`.
- `ExclusiveGroupSelector`: come gestisce il caso in cui entrambi i parametri del gruppo sono presenti nel YAML? Errore o priorità?
- `mod_prob` in Parameter: è distinto da `_mod_range`? Come interagisce il gate con il range?
