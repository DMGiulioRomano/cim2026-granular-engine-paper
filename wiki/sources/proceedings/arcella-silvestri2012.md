# [Arcella & Silvestri, 2012] Analogique B — A computer model of the compositional process

## Citazione CIM
Arcella, A., & Silvestri, S. (2012). Analogique B — A computer model of the compositional process. In *Atti del XIX Colloquio di Informatica Musicale (XIX CIM 2012)*, pp. 144–148. Trieste: AIMI, 21–24 novembre 2012. (Affiliazione autori: Conservatorio di Napoli.)

## Categoria e lunghezza
Comunicazione scientifica — 5 pagine (pp. 144–148) — 9 riferimenti bibliografici (sezione *7. References*, p. 148).

## Argomento centrale
Ricostruzione software di *Analogique B* di Iannis Xenakis (1958–59), considerato dagli autori il primo brano musicale basato su quella che oggi si chiama *granular synthesis* (p. 144, citato come ref [6]; nota: nel paper [6]=Gabor 1947, probabile refuso per [5]=Roads *Computer Music Tutorial* 1996, fonte canonica dell'attribuzione). Il sistema implementa il "meccanismo" compositivo originale di Xenakis (matrice di transizione 8×8, *screens* parametrici, sintesi granulare di Gabor) con architettura **a due moduli software**: motore algoritmico in C++ che genera la score Csound, motore di sintesi in Csound che la rende in audio. La tesi del paper è duplice: (a) il rendering digitale di un processo analog/empirico richiede *scelte* che incorporano una postura compositiva ("*Tools and technologies used to produce a musical work are not neutral but incorporate knowledge that influence the choices of the composer*", p. 148); (b) l'analisi del processo compositivo (Xenakis 1963 / *Musique Formelles*) è una base più solida del solo studio dei risultati (Laske 1991, ref [8]).

## Sistema o strumento descritto
Sistema senza nome proprio — riferito come "*our software implementation*" o "*Analogique B compositional engine*". Architettura esplicita (Figura 7 nel paper, p. 147 — nota: il caption stampato dice erroneamente "*Single grain*" duplicando il caption di Figura 6, ma il contenuto è il diagramma a blocchi):

```
score.cpp ── output ──► Xscore.txt ──► Analogique.csd ──► Csound rendering ──► audio
(C++ engine)            (Csound        (Csound orchestra
                         score format)  con grain opcode)
```

- **Algorithm engine** (`score.cpp`): C++ standard (Dev-C++ IDE, mingw). Loop principale itera la MPT 8×8 di Xenakis. L'utente fissa lo *screen* iniziale e la lunghezza del *protocol* (numero di iterazioni). Output: file di testo in formato score Csound (`Xscore.txt`).
- **Synthesis engine** (`Analogique.csd`): Csound v5.15. Definisce 8 strumenti (uno per ciascuno *screen* A–H). Ogni strumento contiene 10 generatori granulari sovrapposti (`grain` opcode). Parametri opcode: waveform table (sin), sync window table, durata grano 0.04 s costante, range frequenza (offset + width per ciascuna f-region), range ampiezza (offset + width per ciascuna g-region), densità in grain-per-second.

Dati formali del modello (combinatoria 23 variabili → 8 screens):
- 16 *f-regions* (42 Hz – 11400 Hz) raggruppate in due *f-set*: f0 e f1
- 4 *g-regions* (50–60, 60–70, 70–80, 80–90 phones) in due *g-set*: g0 e g1
- 7 *d-regions* (1.3 → 957.7 gps) in due *d-set*: d0 e d1
- A = f0·g0·d0, B = f0·g0·d1, … H = f1·g1·d1

Granularità temporale: durata grano fissa 0.04 s, finestra sync (`ftgen 2, 0, 8192, 20, 9`). Densità max attivata: 315.9 gps (d-region 6); la d-region 7 = 957.7 gps non viene mai usata, "*probably due to the restrictions of the technological means available to Xenakis*" (p. 145). Esplicitamente caratterizzato come **"out-of-time, additive procedure"** (p. 147) e implementato **offline**.

Rilievo accessorio (sezione 3): l'analisi spettrografica del nastro originale (sonogrammi pp. 145–146) mostra inviluppi di grano *smoothed* (Figura 6), non rettangolari come Xenakis affermava — gli autori ipotizzano l'uso di filtri passa-banda in fase di mix studio, "*That already represents a significant deviation from Gabor's theory of acoustical quanta*" (nota 3 a p. 146).

## Analogia con PGE

Arcella/Silvestri 2012 è il **precursore CIM più vicino a PGE sul piano architetturale** tra quelli censiti nel survey. La pipeline è strutturalmente isomorfa; le differenze sono di livello di astrazione del modulo algoritmico, non di topologia del sistema. Quattro vettori di analogia a forza decrescente, più un'anti-analogia.

1. **Pipeline a due moduli con separazione algoritmo ↔ rendering.** Quote (p. 147): *"Our software implementation factors the whole problem in two: it splits into two software modules; the first written in C++ language generates the screen sequence (i.e. it creates the 'protocols'), based on the Xenakis MPT. The second module is written in Csound and implements the granular synthesis process, driven by the screen values."* — questa è la stessa topologia di PGE: `ParameterOrchestrator` legge YAML, costruisce gli stream e produce una rappresentazione intermedia (lista di grani con onset, freq, amp, env); il renderer (Csound `.sco`/`.csd` o NumPy in-memory) traduce la lista in audio. La differenza chiave non è la topologia, è la **natura della IR**: Arcella/Silvestri emettono direttamente score Csound testuale; PGE espone una IR Python (oggetti `Stream`/`Grain`) intermedia tra DSL e renderer. Vettore strutturale forte: stessa decisione architetturale di base.

2. **Tempo differito esplicito e motivato.** Arcella/Silvestri non discutono real-time come opzione; la loro pipeline è batch by design. Il paper non lo problematizza — è la modalità data dalla natura del problema (riproduzione di un processo storicamente offline). PGE recupera la stessa modalità ma in un contesto in cui il real-time esiste ed è disponibile: il *ritorno volontario al tempo differito* (cfr. [[deferred-time-tradition]]) trova in Arcella/Silvestri 2012 un precedente CIM dove l'offline è dato, in PGE diventa **postura compositiva scelta**. Vettore argomentativo solido per sezione 1.

3. **"Tools incorporate knowledge that influence the composer's choices."** Quote conclusiva (p. 148): *"Tools and technologies used to produce a musical work are not neutral but incorporate knowledge that influence the choices of the composer."* — questa frase è la formulazione più diretta nel corpus CIM della stessa tesi che PGE sostiene attraverso il loop lungo: lo strumento non è trasparente, configurare il DSL YAML è già una scelta compositiva. Citabile come precedente CIM diretto della tesi paper (sezione 1, sezione 6).

4. **Generazione di score Csound come *atto compositivo* programmatico.** Sezione 5.1, p. 147: il C++ "*outputs a text file with the Csound 'score' format*". Stessa scelta architetturale di PGE Csound renderer, che emette `.sco` per ciascun brano/stream. Vettore concreto per giustificare la scelta in sezione 3 PGE: precedente CIM, non importazione esogena.

---

**Anti-analogia: score Csound testuale ≠ DSL YAML + IR Python.**

In Arcella/Silvestri il modulo algoritmico **scrive direttamente** righe `i` di score Csound. Non c'è livello di specifica compositiva indipendente dal renderer: cambiare engine richiede riscrivere `score.cpp`. Inoltre il C++ è codice imperativo che descrive *come* generare la sequenza, non *cosa* deve produrre.

In PGE il livello di specifica è il **YAML** — dichiarativo, leggibile, indipendente dal renderer. Il `ParameterOrchestrator` traduce YAML in IR Python (`Stream` con liste di `Grain`); il renderer (Csound o NumPy) consuma la IR. Tre conseguenze:
- Cambiare renderer non tocca la specifica.
- Il YAML è editabile da PGE-ls (language server) — non si edita C++ con un LSP musicale.
- La IR Python permette caching per stream (SHA-256 fingerprint) e workflow STEMS — non implementabili partendo da score Csound testuale.

| | Arcella/Silvestri 2012 | PGE |
|---|---|---|
| Livello di specifica | C++ imperativo | YAML dichiarativo |
| IR | score Csound testuale | IR Python (`Stream`/`Grain`) |
| Renderer | Csound (fisso) | Csound + NumPy (intercambiabili) |
| Editing assistito | nessuno (IDE C++ generico) | PGE-ls (LSP dedicato) |
| Cache per stream | non applicabile | SHA-256 fingerprint |
| Riusabilità del modulo algoritmico | specifico a *Analogique B* | DSL generale |

La topologia "algoritmo → score → Csound → audio" è condivisa; la **scelta di che cosa stia al livello superiore** (codice imperativo specifico vs DSL generale + IR dichiarativa) è il differenziatore PGE. Citabile come precedente architetturale (continuità CIM) ma anche come punto di contrasto per giustificare l'introduzione di un DSL.

## Posizionamento storico
Filone **offline / ricostruzione storica con pipeline codice→score→Csound**. Cronologicamente:
- Posteriore a Roads 1985 (CIM VI, [[roads1985]]) e a Di Scipio 1991 (CIM IX, [[discipio1991]]) — eredita dal filone CIM dello *offline parametric control* ma applicato a un compito specifico (digital reconstruction).
- Contemporaneo a Roads 2012 *From Grains to Forms* (citato come ref [5] sotto Roads, *Computer Music Tutorial*, MIT Press 1996; Roads 2012 non è in bibliografia).
- Anticipa Rizzuti 2006 (CIM XVI, due strumenti Csound separati) e ne condivide la posture: usare Csound come **motore di rendering**, non come ambiente di composizione diretto.
- L'ascendenza Xenakis-Gabor è dichiarata (refs [4] Xenakis *Musique Formelles* / *Formalized Music*; [6] Gabor 1947 *Acoustical Quanta*).

Esiste un'implementazione concorrente: Hagan 2005 "*Genetic Analysis of Analogique B*" (ref [9]), citata come variante per *realtime versions*. Arcella/Silvestri scelgono esplicitamente offline: "*Variants of the first approach would be required for realtime versions*" (p. 148) — il real-time è opzione non perseguita, coerente con il loro framework concettuale.

## Note stilistiche
- **Struttura**: Abstract → 1. Analytical remarks on the *Analogique B* compositional process (formale, definizione di MPT e screens) → 2. Time-frequency analysis of the tape sound (sonogrammi del nastro originale) → 3. Xenakis' grains: theory and practice (rilievo discrepanza teoria/pratica Xenakis) → 4. Xenakis in the studio (ricostruzione storica del workflow analogico) → 5. Software implementation (5.1 algorithm engine, 5.2 synthesis engine) → 6. Conclusion (riflessione meta su strumenti e composizione) → 7. References. Pattern: **analisi del processo compositivo storico → critica del processo → implementazione → riflessione meta**.
- **Tono**: tecnico-descrittivo con apertura analitica (analisi spettrografica) e chiusura argomentativa (riflessione su strumenti come incorporazione di scelte). Niente epigrafi. Inglese sobrio, accademico.
- **Densità citazioni**: 9 ref totali su 5 pagine (Di Scipio non pubblicato [1], Di Scipio Sonus 1995 [2], Di Scipio Atti Convegno Xenakis Milano 2005 — non con anno [3], Xenakis *Formalized Music* [4], Roads *Computer Music Tutorial* MIT 1996 [5], Gabor 1947 [6], Silvestri 2011 unpublished [7], Laske 1991 *Interface* [8], Hagan 2005 *EMS* [9]). **Lezione**: per un paper di ricostruzione/implementazione è accettabile un numero ridotto di citazioni mirate; il paper CIM 2026 (system paper) dovrebbe stare nella fascia 12–20 (cfr. survey CIM tool papers).
- **Pattern figure**: 7 figure (matrice MPT, sonogrammi, singolo grano, diagramma di architettura). La Figura 7 (diagramma a blocchi score.cpp → Xscore.txt → Analogique.csd → Csound rendering — caption stampato erroneamente come "Single grain", refuso paper) è il modello stilistico utile per il diagramma architettura PGE in sezione 3.
- **Pattern code listing**: il paper alterna prosa descrittiva e listing Csound (definizioni `ftgen`, `gifreg*`, `gigain*`, definizione `instr 2` con 10 generatori `grain`). Listing inseriti in colonna sinistra/destra, font monospaziato. Modello applicabile alla sezione 3 PGE per inserire frammenti YAML.
- **Apertura sezione 5**: introduce il sistema con un periodo che esplicita la *fattorizzazione* in due moduli, poi figura, poi sottosezioni dedicate. Modello *fattorizzazione esplicita* riusabile per descrivere `ParameterOrchestrator` + renderer in PGE.

## Sezioni del paper CIM 2026 dove citare
- **Sezione 1 (Introduzione, narrazione tre atti)**: citare la frase conclusiva di Arcella/Silvestri (p. 148) — *"Tools and technologies used to produce a musical work are not neutral but incorporate knowledge that influence the choices of the composer"* — come precedente CIM diretto della tesi sul loop lungo come postura compositiva.
- **Sezione 2 (Sintesi granulare: dal paradigma Gabor al controllo gerarchico)**: citare come ricostruzione del *primo brano* basato su sintesi granulare (Analogique B 1958–59, riferimento Roads); collega la lineage Xenakis-Gabor a un'implementazione CIM contemporanea offline. Utile per dimostrare che il filone *codice→score→Csound→audio* è una tradizione attiva CIM, non un'invenzione PGE.
- **Sezione 3 (PGE: architettura per l'indagine parametrica)**: citare come **precursore architetturale diretto** della pipeline PGE. Stessa topologia algoritmo → score Csound → audio. Il riferimento serve a posizionare l'introduzione del DSL YAML + IR Python come *evoluzione di livello di astrazione* rispetto al precedente CIM, non come importazione esogena. Possibilmente affiancato a Rizzuti 2006 (due strumenti Csound separati, CIM XVI).
- **Sezione 6 (Conclusioni)**: riprendere la frase su *tools incorporate knowledge* come ancoraggio CIM per la postura PGE.

## Quote chiave
- *"Our software implementation factors the whole problem in two: it splits into two software modules; the first written in C++ language generates the screen sequence (i.e. it creates the 'protocols'), based on the Xenakis MPT. The second module is written in Csound and implements the granular synthesis process, driven by the screen values."* (p. 147) — fattorizzazione canonica algoritmo ↔ rendering, isomorfa alla pipeline PGE.
- *"This out-of-time, additive procedure, which is anyway rather cumbersome and time-consuming, allowed Xenakis to get fractional density values."* (p. 147) — caratterizzazione esplicita del workflow come *out-of-time*; PGE eredita la stessa modalità, ma come scelta non come vincolo.
- *"Variants of the first approach would be required for realtime versions."* (p. 148) — il real-time è opzione non perseguita; coerente con la postura tempo differito (Sezione 1 paper CIM 2026).
- *"Our choice followed not merely from the available technology, but from a design strategy making full advantage of the digital domain. Tools and technologies used to produce a musical work are not neutral but incorporate knowledge that influence the choices of the composer."* (p. 148) — formulazione CIM diretta della tesi sul carattere non neutrale degli strumenti compositivi. Citabile come ancoraggio CIM della postura PGE.
- *"Analogique B is considered the first musical work based [on] what is known, today, as 'granular synthesis' [6]."* (p. 144) — riferimento storico per sezione 2; collega lineage Xenakis-Gabor a CIM proceedings tradition. Nota: nel paper ref [6]=Gabor 1947 (refuso evidente — l'attribuzione canonica viene da Roads, *The Computer Music Tutorial* 1996, ref [5] nello stesso paper).
