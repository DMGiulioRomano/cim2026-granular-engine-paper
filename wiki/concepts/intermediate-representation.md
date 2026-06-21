# Intermediate Representation (IR) in PGE

## Definizione

IR = **specifica dichiarativa post-parsing**, indipendente dalla sintassi d'ingresso (YAML) e dal formato d'uscita (audio), su cui operano le trasformazioni. Il termine è mutuato dall'architettura dei compilatori: la footnote in `sec:architettura` di paper.tex lo definisce come «forma che il codice sorgente assume dopo il parsing e prima della generazione del codice target».

In PGE la IR è lo **Stream dichiarativo**: l'oggetto costruito da `Stream.__init__` — Parameter (via ParameterOrchestrator), controller×4 (Pointer, Pitch, Density, Window), VoiceManager, strategie di distribuzione, clip strategy, seed — **prima e indipendentemente** dalla materializzazione dei grani.

**Chiarimento terminologico:** questa "IR" è *Intermediate Representation*, non *impulse response* (che compare altrove nel corpus, es. convoluzione di microsuoni in Kyma, filtri FIR in [[depoli-piccialli1988]]). Le due sigle non hanno nulla in comune.

## I tre livelli

```
YAML (DSL / sorgente)
        ↓  parsing (ParameterOrchestrator)
IR = Stream dichiarativo (specifica)
        ↓  generate_grains() (campionamento)
lista di Grain (realizzazione / target abbassato)
        ↓
renderer (Csound / NumPy) = backend / codegen
        ↓
audio
```

### Analogia col compilatore

| Compilatore classico | PGE |
|---|---|
| Sorgente (linguaggio ad alto livello) | YAML |
| IR (forma intermedia su cui operano i pass di ottimizzazione) | Stream dichiarativo (Parameter/controller/strategie) |
| Codice target abbassato (three-address code, bytecode) | lista di Grain |
| Backend / codegen (emette linguaggio macchina) | Renderer (Csound `.sco` / NumPy overlap-add) |

## Perché la IR è la specifica e NON i grani

Quattro criteri, di cui tre convergono sulla specifica dichiarativa e uno tirerebbe verso i grani.

### (1) Le trasformazioni operano sulla specifica e PRODUCONO i grani

Le operazioni compositive — envelope time-varying, ProbabilityGate (`dephase`), voice strategy (scatter, offset pitch/pointer/pan/onset), density distribution (sincrona/asincrona) — sono tutte definite sulla IR e si materializzano durante `generate_grains()`. I grani sono il **risultato** delle trasformazioni, non l'oggetto su cui le trasformazioni operano. Nel vocabolario del compilatore: i pass di ottimizzazione agiscono sulla IR, non sul codice target.

### (2) Determinazione dalla sorgente

La specifica dichiarativa è **sempre** determinata dalla sorgente YAML: dato un YAML, la IR è univoca. La lista di grani lo è solo includendo il seed del generatore random — e il paper rivendica invarianza per *andamento statistico*, non bit-identica (cfr. sezione Riproducibilità in CLAUDE.md). L'invariante compositivamente significativo è ciò che la specifica fissa (traiettorie, range, strategie); la lista di grani è una delle realizzazioni possibili.

### (3) Livello compositivamente significativo

Il contributo di PGE rispetto ad [[arcella-silvestri2012]] (precursore CIM architetturale più vicino) è proprio l'aver introdotto uno strato dichiarativo indipendente dal renderer, dove Arcella/Silvestri scrivono direttamente score Csound da C++ imperativo (DSL e IR coincidono col target). Lo strato che giustifica il differenziatore è la IR dichiarativa, non la lista di grani.

### (4) Controcanto onesto: l'analogia col compilatore puro tirerebbe verso i grani

L'unico criterio che favorisce i grani come IR è l'analogia stretta col compilatore: la lista piatta di grani (onset, freq, amp, dur, pointer, pan, window) somiglia a un three-address code — istruzioni atomiche completamente esplicite, nessun costrutto di alto livello. In un compilatore LLVM, quel livello **è** la IR bassa. Ma i tre criteri precedenti prevalgono: (1) le trasformazioni non operano sui grani, li producono; (2) l'invariante compositivo è la specifica, non i grani; (3) il differenziatore architetturale di PGE è lo strato dichiarativo.

## Evidenza dal codice

- **`stream.py` — `Stream.__init__`**: costruisce solo la struttura dichiarativa (Parameter via ParameterOrchestrator, controller×4, VoiceManager, strategie, clip strategy, seed). I backing field `_voices`/`_grains` restano vuoti; `self.generated = False`. La IR esiste prima della materializzazione.
- **`stream.py` — `generate_grains()`**: dopo issue #117 è **lazy** — scatta al primo accesso alle property `.voices`/`.grains`. Per stream cache-clean non scatta affatto: il renderer corto-circuita su `is_dirty` prima di leggerli (restano `generated=False`). La IR (Stream dichiarativo) e la sua materializzazione (lista di Grain) sono temporalmente e logicamente disgiunte.
- **`generator.py` — `Generator`**: orchestra la pipeline YAML → Stream → rendering; la fase dichiarativa (costruzione IR) e la fase imperativa (campionamento → Grain) sono passi distinti.
- **`main.py`**: entry point che connette il parsing YAML alla pipeline Generator. Conferma la sequenza: parsing → IR → (lazy) grani → renderer.

Lo Stream fa da contenitore prima e dopo (`self._grains` è caching del risultato di `generate_grains()`), ma "tenere i grani" è dettaglio di implementazione (cache), non una dichiarazione su cosa la IR sia.

## Diagramma di riferimento

`paper/figures/arch-pipeline.tikz` codifica visivamente la lettura corretta: il box IR contiene Stream/VoiceManager/Controller×4; l'output sotto è `List[List[Grain]]`. Non modificare il diagramma — è il riferimento.

`paper/figures/param-orchestrator.tikz` contiene il box "IR" che delimita la specifica dichiarativa.

## Nota: two-stage lowering (prospettiva aperta)

Si potrebbe descrivere PGE come abbassamento a due stadi: specifica → grani → audio, con analogia alla distinzione LLVM tra IR alta (vicina alla sorgente, strutturata) e IR bassa (vicina al target, piatta). Lo Stream dichiarativo sarebbe la IR alta; la lista di grani la IR bassa. Questa lettura è più ricca ma meno maneggevole per la prosa della sezione Architettura — registrata come alternativa per sviluppi futuri, non adottata nel paper corrente.

## Sezioni del paper CIM 2026 dove descrivere

- **`sec:architettura`** (primaria): la footnote che definisce IR; la distinzione fase dichiarativa (costruzione IR) vs fase imperativa (campionamento → Grain); il diagramma della pipeline.

## Fonti

- [[arcella-silvestri2012]] — precursore CIM architetturale: DSL e IR coincidono col target (score Csound); PGE introduce lo strato dichiarativo intermedio
- [[stream]] — analisi del modulo Stream: `__init__` come costruzione IR, `generate_grains()` come materializzazione
- [[generator]] — orchestrazione della pipeline: fase dichiarativa + fase imperativa
- [[tendency-mask]] — il modello di controllo che opera sulla IR (Envelope + range + distribuzione)
- [[roads1978]] — primo esempio documentato del pattern front-end/IR (AGS → MUSIC V)
- [[roads1985]] — formulazione CIM 1985 del pattern *front-end → engine*
- [[deferred-time-tradition]] — il differito come contesto operativo della pipeline DSL → IR → backend
- [[fournier2016]] — TENOR 2016: partitura come modello dati con algebra di operazioni in forma chiusa = precedente più vicino dell'**IR interrogabile**, ma applicato all'output (codifica della partitura) anziché alla specifica a monte del rendering. Contrasto utile: PGE interroga la specifica *prima* della materializzazione
- [[qiuichise2025]] — TENOR 2025: modello a grafo di eventi dichiarativo attraversato lungo tutta la compilazione (notazione → audio), trasformazioni come funzioni di prima classe. Parente diretto del binomio dichiarativo+IR; diverge per oggetto (eventi notazionali general-purpose vs grani da campione) e per il differimento grano-per-grano di PGE
