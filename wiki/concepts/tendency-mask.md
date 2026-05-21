# Tendency mask come modello di controllo parametrico in PGE

## Definizione

Per ogni parametro di un grano (durata, frequenza, posizione nel buffer, pan, volume, densità, ecc.) il compositore specifica due componenti:

1. **Centro time-varying** — traiettoria deterministica `center(t)` definita da un Envelope (sequenza di breakpoint con interpolazione).
2. **Range di deviazione** — ampiezza `spread` (anch'essa potenzialmente time-varying) entro cui il valore è campionato grano per grano da una distribuzione di probabilità.

La distribuzione è configurabile via `distribution_mode` nello `StreamConfig`:
- `uniform` — `center + random.uniform(-0.5, 0.5) * spread`, bounds teorici `[center − spread/2, center + spread/2]`.
- `gaussian` — `random.gauss(μ=center, σ=spread)`, con clamping ai bounds del Parameter in `Parameter._clamp()`.

Un `ProbabilityGate` (`dephase`) decide se applicare la deviazione al grano corrente: gate chiuso → valore = `center(t)` puro; gate aperto → valore = sample della distribuzione.

## Proprietà fondamentale: indipendenza fra grani

Il valore al grano `n+1` è **indipendente** dal valore al grano `n`. Nessuna memoria di stato fra grani consecutivi. Il processo è:
- deterministico nella specifica (envelope + range + scelta di distribuzione);
- statistico nella generazione (campionamento i.i.d. al grano).

Questa proprietà distingue tendency mask da qualunque modello iterativo a stato (sequenze caotiche, Markov, ricorsioni).

## Lineage storico

- **Truax 1988** (DMX-1000): tendency mask come gerarchia esplicita di controllo per sintesi granulare real-time; Fig. 4 introduce l'overlay ASCII multi-traccia di frequency mask, duration mask, amplitude/delay envelope come **prima rappresentazione visiva multi-parametro** del modello in contesto granular. È l'antecedente diretto e attestato da fonte ingestita ([[truax1988]]).
- **Truax 1990, 1994**: tendency masks come input visivo di controllo e come strumento per *listening inside the sound*.
- **Di Scipio/Tisato 1993** (ICMS, CIM X): **conferma documentale CIM 1993 dell'adozione del modello Truax 1988** dentro la tradizione offline italiana. P. 162: «*For some parameters, a tendency-mask control is available, which makes the range of possible values change through time. Value assignment, in that case, is done using a random number generator (gaussian distribution).*» Applicato a `grain duration`, `grain delay`, `grain amplitude`, `file portion`. Stessa identica meccanica (range time-varying + sampling gaussiano + indipendenza fra grani) implementata in PGE in `Parameter.value_at(t)` + `GaussianDistribution`. Cfr. [[discipio-tisato1993]] vettore (c).
- **PGE**: eredita il modello, lo materializza nel DSL YAML (Envelope + `mod_range` + `dephase` + `distribution_mode`) e ne inverte il ruolo della rappresentazione visiva — non più input gestural ma output analitico del loop lungo (cfr. [[score-visualizer]]).

## Contrasto controllato con Di Scipio 1991

Cfr. [[discipio1991]]. Di Scipio adotta una famiglia di controllo **opposta**: mappe caotiche deterministiche (logistica, Verhulst, Hénon) con dipendenza `xn+1 = f(xn)`. Proprietà:
- traiettoria deterministica ma caotica (sensibilità alle condizioni iniziali);
- memoria di stato fra iterazioni;
- nessuna distribuzione di probabilità — il "disordine" emerge dalla dinamica non-lineare, non dal campionamento.

Le due famiglie condividono il problema (controllo unitario su molti parametri di molti grani in deferred time) ma scelgono regimi opposti. PGE non astrae né generalizza il modello caotico-iterativo: lo affianca come alternativa nella tradizione CIM offline. Citare Di Scipio 1991 nel paper CIM 2026 **per contrasto controllato**, non come precursore diretto di `ParameterOrchestrator` o `PointerController`.

Secondo data-point CIM del filone caotico-iterativo: [[rizzuti2006]] (CIM XVI). Stessa famiglia di controllo di Di Scipio 1991 ristretta alla sola logistica `xt+1 = c·xt·(2−xt)` con rivendicazione esplicita del deterministico **invece di** stocastico. Conferma che la linea non è episodio isolato del 1991, ma traccia ricorrente nella tradizione CIM offline — utile da citare insieme a Di Scipio 1991 quando il paper CIM 2026 documenta il filone opposto a tendency mask.

**Coesistenza nel singolo sistema (ICMS, [[discipio-tisato1993]]):** Di Scipio/Tisato 1993 mantiene tendency-mask control per i parametri di sintesi del grano (duration/delay/amplitude/file-portion) e affianca al medesimo livello le mappe caotiche (opzioni 4–7 del menu `GRANULAR PROC.`: discubic, logistic, Verhulst, May) per il controllo del puntatore. Le due famiglie convivono come modalità separate dentro lo stesso sistema: l'autore le tratta come scelte alternative, non come gerarchia di astrazione. PGE eredita la prima (tendency-mask) come pattern centrale, non incorpora la seconda — coerente con la postura del paper CIM 2026 (le due famiglie restano alternative parallele nella tradizione CIM offline, non assorbite l'una dall'altra).

## Implementazione PGE

File chiave nel codice (`raw/PythonGranularEngine/src/`):
- `shared/distribution_strategy.py` — `DistributionStrategy` (ABC), `UniformDistribution`, `GaussianDistribution`, `DistributionFactory` (registry pattern).
- `parameters/parameter.py` — `Parameter.value_at(t)` (interpolazione envelope → center), `Parameter._clamp()` (bounds enforcement).
- `parameters/probability_gate.py` — `NeverGate`, `AlwaysGate`, `RandomGate(prob)`, `EnvelopeGate(envelope_di_probabilità)`.
- `parameters/orchestrator.py` — `ParameterOrchestrator` come componente che assembla `Parameter` + `ProbabilityGate` da YAML.

Selezione della distribuzione: `StreamConfig.distribution_mode: 'uniform' | 'gaussian'` (default `uniform`).

## Sezioni del paper CIM 2026 dove descrivere

- **Sezione 2 (Sintesi granulare: dal paradigma Gabor al controllo gerarchico)**: tendency mask come pattern ereditato da Truax 1988 (gerarchia di controllo) e formalizzato in PGE come modello centrale di specifica parametrica. Citare insieme a Di Scipio 1991 per contrasto controllato all'interno della tradizione CIM offline.
- **Sezione 3 (Architettura PGE)**: descrizione del meccanismo concreto (Envelope + `mod_range` + `dephase` + `distribution_mode`) come materializzazione del pattern nel DSL YAML. Cfr. [[parameter-orchestrator]].
- **Sezione 4 (Partitura grafica)**: il visualizer rende leggibile *post-synthesis* la deviazione effettiva campionata dalla tendency mask grano per grano — inversione di ruolo rispetto a Truax 1988 Fig. 4 (input di controllo).

## Domande aperte

- Quale `DEFAULT_PROB` per `RandomGate` quando `dephase: true` senza valore esplicito? Cfr. `parameter-orchestrator.md` domande aperte.
- `mod_range` può essere a sua volta un Envelope time-varying? Da verificare in `parameter.py`.
- La distribuzione è selezionabile per-parametro o solo a livello di Stream? Attualmente `distribution_mode` è in `StreamConfig` (globale dello stream).
- **Lineage pre-Truax** (origine storica del pattern in Koenig PR1/PR2 anni '60-'70): attestato in letteratura standard ma **non in fonti ingestite**. Per citarlo nel paper CIM 2026 serve ingest di una fonte primaria (manuale PR2) o secondaria affidabile. Finché manca, attribuire il pattern unicamente a Truax 1988.
