# [Rolfe, Keller 2000] Decorrelation as a By-Product of Granular Synthesis

## Citazione CIM

Rolfe, C., & Keller, D. (2000). Decorrelation as a By-Product of Granular Synthesis. In *Atti del XIII Colloquio di Informatica Musicale*. L'Aquila: AIMI. Poster Session II.

Third Monk Software (Rolfe, Vancouver, Canada) + CCWIA (Keller, Stanford, CA). **Stessa coppia di autori di [[keller-rolfe1998]] (CIM XII, *The Corner Effect*), con ordine invertito** — Rolfe primo autore qui, Keller primo nel 1998. Il paper 2000 estende formalmente l'ontologia 1998 (stream/waveform/pointer/event) a una teoria misurabile della correlazione.

## Categoria e lunghezza

Poster Session II — short paper (~3-4 pp.), 5 riferimenti inline ([1]-[5]) senza sezione *References* esplicita. Sezioni numerate 1 *Introduction and Definitions*, 2 *Importance of Correlation in Granular Synthesis*, 3 *Implementation* (modello con delay taps). Densità tecnica alta per il formato — paper teorico-formale che apre con la definizione matematica della cross-correlation function:

$$F(\tau) = \lim \frac{1}{T} \int y_1(t) \cdot y_2(t+\tau) \, dt$$

normalizzata al range $-1.0 \leq k \leq 1.0$.

## Argomento centrale

Numerosi autori (Kendall 1995, Truax 1992) hanno notato che la decorrelazione *occorre come by-product* della granular synthesis (effetti stereo e panning unici). Ma **la misura di correlazione non è esplicita né variabile nei modelli GS esistenti**. Il paper propone un approccio sistematico per **rendere la decorrelazione un parametro di controllo esplicito**, relazionando ogni parametro implementativo ai suoi effetti misurabili su tre livelli ortogonali di correlazione.

## Sistema o strumento descritto

Modello GS reference con $N$ grain streams che condividono buffer di input.
- **Architettura per-stream**: delay tap aggiornato a fine grain cycle con valore random in range `delay-range`; finestra triangolare (peak = grain amplitude, edges = 0)
- **Pairing scheme**: stream accoppiati per cancellare modulazione di ampiezza ⇒ N effettivi = N totali / 2
- **Parametri primari di decorrelazione**: `delay-range` per stream (varianza temporale fra grani), `advance rate` (grain hop nel buffer scan), distribuzione random sui delay tap
- **Range pratico**: 23-64 streams sufficienti per smearing efficace degli AM artifacts
- **Pitch-shift escluso dal modello core** — trattato come pre-processing di stream perché dipende dall'algoritmo di interpolazione scelto

Real-time deliberato (non specificato linguaggio/piattaforma — paper teorico-formale, non descrizione di software specifico).

## Analogia con PGE

**Tre livelli di correlazione = tre assi su cui PGE opera con strumenti diversi**:

| Livello Rolfe-Keller | Decorrelation tool Rolfe-Keller | Tool PGE corrispondente |
|---|---|---|
| **Grain-to-grain** (intra-stream) | grain duration wander + advance rate | `PointerController.speed_ratio` + deviazione per-grano + `Envelope` range sui parametri |
| **Cross-channel/stream** (inter-stream) | delay-range per stream + pairing | `VoiceManager` con deviation_probability strategy + N stream YAML-dichiarati |
| **Instance/event** (inter-execution) | distribuzione random sui delay tap | `DistributionStrategy` (uniform/gaussian) — ogni run produce un *instance* decorrelato |

PGE eredita il *framework concettuale* Rolfe-Keller (correlazione misurabile su 3 livelli) ma inverte il trade-off centrale: Rolfe-Keller scelgono *decorrelation per chorusing/thickening* in real-time; PGE espone esplicitamente entrambi i poli (transparency vs. decorrelation) come configurazioni del DSL YAML, perché il deferred time abilita il confronto diretto fra rendering.

## Posizionamento storico

Lineage CIM → CMR sulla decorrelazione:
- **1998** [[keller-rolfe1998]] (CIM XII): ontologia *stream / waveform / pointer / event* — entità nominate
- **2000** Rolfe-Keller (CIM XIII): stessa ontologia diventa **base per definizione formale dei 3 livelli di correlazione misurabili**
- **2002** Vaggione (*décorrélation microtemporelle*, vedi [[vaggione2002]]): generalizzazione della decorrelazione da fenomeno tecnico granulare a *attributo morfologico-spaziale di prima classe* del dominio compositivo
- **Filiazione cronologica**: il paper Rolfe-Keller 2000 è anello mancante CIM **fra il vocabolario granular tecnico (1998) e il vocabolario compositivo Vaggione (2002)**. Il paper 2000 rende quantificabile ciò che 2 anni dopo Vaggione costruirà come dimensione compositiva autonoma.

**Filone real-time CIM 2000**: Rolfe-Keller appartiene al ramo real-time-evoluto (post-Truax, post-Lippe) che però — diversamente da [[lippe1993]] / [[detintis1995]] — non documenta un sistema specifico ma propone un framework teorico-formale di analisi della GS. È il primo paper CIM granulare *meta-livello* (analizza il behavior dei modelli, non li implementa).

## Note stilistiche

- **Densità citazionale**: 5 ref. inline su ~3 pp. — limite inferiore per Poster Session CIM 2000
- **Apertura abstract**: nomina due autori-riferimento (Kendall 1995, Truax 1992) nelle prime due righe per posizionare il contributo come *estensione formale* di un fenomeno già osservato
- **Strategia argomentativa**: definizione matematica formale → giustificazione percettiva (riferimenti a precedence effect, externalization headphone, ICCC) → tassonomia tecnica → implementazione di riferimento
- **Tono**: argomentativo-teorico. Nessuna descrizione di brano applicativo, nessun audio example. Paper *concettuale* in formato poster
- **Strutturazione sezioni**: titoli compatti, definizioni esplicite (cross-correlation function, decorrelation), tabelle implicite nel testo (parametri → effetti)
- **Modello stilistico riutilizzabile per CIM 2026 sezione 4**: la sequenza *definizione formale → tre livelli ortogonali → mapping su parametri implementativi* è la struttura argomentativa che PGE può adottare per descrivere il `score_visualizer` (definizione asse Y → tre livelli di visualizzazione → mapping su parametri Stream)

## Quote chiave

> "Several researchers (Kendall, 1995; Truax, 1992) have noted that decorrelation occurs as a by-product of granular synthesis (GS). [...] The correlation measure itself, however, is not generally explicit or variable within existing synthesis models. The following paper describes a systematic approach to granular decorrelation, relating individual parameters to their effect upon grain-to-grain, cross-channel (stream) and instance (event) signal correlation."
> — Abstract (definizione esplicita dei 3 livelli ortogonali)

> "Varying a given stream delay by a random amount introduces phase-shifting causing the value k [cross-correlation] to vary dynamically from -1.0 ... 1.0. The precise amount of decorrelation depends upon the relation between grain duration and source content, but can, with practice, be tuned by ear to the desired result."
> — Sez. 3 (formulazione esplicita: variazione random → decorrelazione misurabile)

> "Because we selectively introduce random variation into our stream delays, however, we are in a sense forgoing the goal of transparency in our GS model in favour of a thickening or chorusing, and thus decorrelating effect. Transparent time-expansion requires maximizing correlation at all levels, best suited to one or two determinate streams, while we are interested equally in useful applications of decorrelation and multiple streams."
> — Sez. 3 (trade-off esplicito transparency vs. decorrelation — PGE espone entrambi i poli nel DSL)

> "Generally, the rule of thumb is that greater delay variation in more prominent (louder, earlier) streams increases output instance correlation."
> — Sez. 3 (heuristic compositiva *empirically discovered* — esempio canonico del tipo di scoperta che il loop lungo PGE può sistematizzare e visualizzare)

> "Most published granular synthesis (GS) models also allow for stochastic variation of control parameters, usually as a parameter range specification, as does our model."
> — Sez. 2 (conferma CIM 2000 che il *parameter range* — Envelope center+range PGE — era pattern condiviso fra modelli GS già nel 2000)

## Concetti correlati

- [[decorrelazione-granulare]] — sintesi cross-source della filiazione CIM → CMR e mapping completo su PGE

## Sezioni del paper CIM 2026 dove citare

- **`sec:tradizione`** (primaria): decorrelazione come proprietà della massa
  granulare teorizzata in ambito CIM (anello fra [[keller-rolfe1998]] e
  [[vaggione2002]]).

Fonte di verità: [[mappa-citazioni-paper]].

