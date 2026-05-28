# Modelli stilistici bottom-up per il paper CIM 2026

Sintesi cross-source dell'**architettura espositiva** dei paper canonici della
tradizione granulare, in funzione della riscrittura bottom-up del paper CIM 2026
(direttiva maestro, cfr. [[incontro-maestro-2026-05-28]]).

Il maestro non ha indicato *quali* paper studiare come modelli (ha dato un
consiglio generale: «leggi non solo contenuti ma anche come si è sforzato di
comunicarli con chiarezza [...] l'analisi compositiva di come è stato scritto»,
righe 706–733, 763–771). La scelta di Truax 1988 + Roads 1978/1988 come campione
è **interpretazione di Giulio**: sono i paper canonici in cui un autore descrive
il proprio sistema granulare. Confronto esteso a due tool paper CIM recenti già
ingestiti con note stilistiche ([[arcella-silvestri2012]], [[anatrini2024]]).

Fonti dirette dei dati: lettura PDF in `raw/papers/` ([[roads1978]], [[roads1988]],
[[truax1988]] — sezioni «Architettura espositiva» nelle rispettive pagine).

---

## Matrice paper × dimensione espositiva

| Dimensione | Roads 1978 (2 pp) | Roads 1988 (3 pp, editoriale) | Truax 1988 (13 pp) | Arcella/Silvestri 2012 (5 pp CIM) | Anatrini 2024 (7 pp CIM) |
|---|---|---|---|---|---|
| **Apertura** | genealogia breve + gap + annuncio sistema | definizione del grano (unità) *prima* della teoria | genealogia 2 frasi + **problema (volume dati)** + sistema + *Riverrun* | analisi del processo compositivo storico (*Analogique B*) | motivazionale/biografica (Healing Soundscape) |
| **Build** | **grano → event → implementazione** | grano → teoria(bg) → impl. → estensioni | **problema → sistema → controlli → forma macro** | analisi storica → critica → implementazione | cornice teorica → sistema → applicazioni |
| **Diagramma di sistema** | Fig. 2 in *Implementation* (presto) | nessuna figura | **Fig. 3 tardi** (dopo le variabili) | Fig. 7 in sez. 5 (fattorizzazione esplicita) | schema funzionamento in sez. 3 |
| **Lit-review** | apertura, 4 ref foundational | distribuito, denso (review) | distribuito, mai sezione propria | mirato, 9 ref | **sezione propria (sez. 2 *Contesto*)** |
| **Implicazioni teoriche** | **in chiusura** (*Summary*) | teoria up-front (bg) + conclusione estetica | **in chiusura** (*Musical Applications*) | **in chiusura** (sez. 6, meta) | distribuite + chiusura |
| **Densità ref** | 4 / 2 pp (minima) | ~11 / 3 pp (alta, review) | ~22 / 12 pp (~1.8/pp) | 9 / 5 pp | **25 / 7 pp (alta)** |
| **Chiusura** | tecnica + estetica leggera | brevissima estetica | doppia: musicale + tecnica | riflessione meta su strumenti | sviluppi futuri |
| **Verdetto** | **bottom-up puro** | survey (bottom-up parziale) | **bottom-up forte** | bottom-up (ricostruzione) | **top-down** (cornice teorica prima) |

---

## Lettura della matrice

- **Il canone granulare-autodescrittivo è bottom-up.** Roads 1978 e Truax 1988 —
  i due paper in cui l'autore descrive il proprio sistema — costruiscono dal
  grano/dal problema verso l'alto e collocano le implicazioni teorico-musicali
  **in chiusura**. Roads 1978 nomina letteralmente il movimento: «*Higher-Level*
  Organization of Grains».
- **La teoria come *background*, non come premessa-tesi.** Anche dove la teoria
  compare presto (Roads 1988), è etichettata «Theoretical Background» e segue la
  definizione concreta dell'unità. Il top-down con cornice teorica come sezione
  propria (Anatrini 2024, sez. *Contesto*) è il modello **opposto** — coerente con
  ciò che il maestro ha sconsigliato («partire dall'alto» = «paper di carattere
  più informatico e teorico»).
- **Il diagramma di sistema non apre.** In Truax 1988 la Fig. 3 (gerarchia dei
  controlli) arriva *dopo* aver introdotto i mattoni. Per CIM 2026: introdurre i
  componenti, poi la figura d'insieme.
- **Apertura problem-driven.** Truax apre col problema (1000–2000 grani/sec
  ingovernabili in event-list deterministica) → è anche la radice della
  *correzione economia di mezzi* (cfr. [[deferred-time-tradition]], [[tendency-mask]]).
- **Densità ref calibrata al genere.** Survey/editoriale denso (Roads 1988,
  Anatrini 2024); system/implementation paper più sobrio (Arcella/Silvestri 9 ref).
  Il paper CIM 2026 (system paper argomentativo) sta nella fascia **9–21 ref**
  (vincolo CIM, cfr. CLAUDE.md), modulando verso il basso come Arcella/Silvestri.
- **Modello da non imitare**: Anatrini 2024 per la *struttura* (top-down), CAGE
  2014 per il *tono* (descrittivo enciclopedico). Il paper resta argomentativo su
  un sistema.

---

## Spina dorsale derivata per il paper CIM 2026 (bottom-up)

Mappatura dei modelli sulle sezioni proposte:

1. **Introduzione** — apertura **problem-driven alla Truax**: che cos'è il
   programma Python e quale problema risolve (controllo parametrico esplicito su
   migliaia di grani in tempo differito). Genealogia compressa a poche frasi, *non*
   tesi premessa. Niente narrazione tre atti in apertura.
2. **Architettura del sistema** — **build dal basso alla Roads 1978/Truax**:
   grano/DSL → orchestratore → stream/voci → renderer → cache. Frammenti YAML come
   i listing Csound di Arcella/Silvestri; **fattorizzazione esplicita** del sistema
   in moduli (modello Arcella/Silvestri sez. 5). Diagramma d'insieme (Fig. 1)
   **dopo** aver introdotto i componenti (modello Truax Fig. 3).
3. **La partitura grafica** — emerge come *frutto del lavoro* (direttiva maestro:
   «non te la premetti»); confronto con i precursori visivi (Truax Fig. 4 ASCII,
   Roads polygon) trattato qui, non in cornice teorica iniziale. Cfr. [[graphic-score]].
4. **Posizionamento nella tradizione** — lit-review **compatta e tardiva**, «le
   cose più vicine alle tue esigenze» (maestro). Truax corretto (economia di mezzi).
5. **Implicazioni teorico-compositive** — **in chiusura**, come Roads 1978
   (*Summary*) e Truax 1988 (*Musical Applications*): il loop lungo come postura
   *abilitata* dal sistema, non tesi premessa. Quote Risset p. 37.
6. **Conclusioni** — sviluppi futuri (modello *Future Directions* di Truax): GUI
   come secondo paper, real-time opzionale, didattica.

**Principio guida unico**: ogni mossa di astrazione segue, non precede,
l'esposizione del mattone concreto. «Se tu parti dalla sintesi e astrai verso
l'alto» (maestro, righe 355–360).

Vedi anche: [[incontro-maestro-2026-05-28]], [[deferred-time-tradition]],
[[graphic-score]], [[truax1988]], [[roads1978]], [[roads1988]].
