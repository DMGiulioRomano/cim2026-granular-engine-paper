# Rappresentazioni visive per sintesi granulare — lineage storico (verso la map)

> Nota lessicale (Fase 4): l'output visivo di PGE **non** si chiama più
> «partitura grafica» ma **map** (mappa sinottica). La parola «partitura» resta
> solo per gli *altri* sistemi del lineage (Truax, Roads, Caires…) e per
> contrasto (ciò che la map non è).

## Definizione

Rappresentazione visiva statica o dinamica del comportamento temporale di un processo di sintesi granulare. Non è partitura prescrittiva (il visualizer non pilota il motore); è *study score* — artefatto che rende leggibile la relazione tra specifica parametrica e risultato sonoro.

Il differenziatore PGE nel lineage: **asse Y = posizione nel buffer sorgente** (non frequenza, non traccia), e **inversione di flusso** — la map è output delle decisioni compositive, non input di controllo.

## Lineage cronologico

### 1. Roads 1978 — polygon su piano freq/tempo (metafora)

> «*This granular synthesis system can model any polygon inscribed on the frequency-vs-time plane*» (p. 62, [[roads1978]])

Prima formulazione documentata. Il grano ha inviluppo gaussiano; collezioni di grani formano poligoni arbitrari su piano frequenza×tempo. Roads cita *Studie II* di Stockhausen come precedente notazionale. È metafora geometrica, non output software: AGS non produce immagini.

### 2. Roads 1985 (CIM VI) — Figg. 7–9, polygon inscribed

> «*"any polygon inscribed on the frequency-versus-time plane" [...] lines, triangles, rhomboids*» (p. 200, Figg. 7–9, [[roads1985]])

Primo precursore CIM. Amplia la formulazione 1978 con figure concrete (linee, triangoli, rombi) inscritte sul piano freq/tempo. Rimane descrizione verbale + illustrazione su carta, non output automatico. L'idea di «*shapes inscribed*» persiste in tutto il lineage.

### 3. Truax 1988 — Fig. 4 ASCII tendency masks (primo concreto)

Fig. 4 ([[truax1988]]): overlay di quattro curve ASCII su terminale 24 righe — frequency mask, duration mask, amplitude envelope, delay envelope. Primo precedente *concreto* di rappresentazione visiva multi-parametro tempo-dipendente per controllo granulare. Non è output di rendering: è **input di controllo**, disegnato dal compositore prima del rendering. Le curve sono tendency masks che il compositore traccia per guidare il processo — il DMX-1000 le traduce in distribuzioni di grani.

Differenza fondamentale con PGE: Truax Fig. 4 = **input** (il compositore disegna le curve → il sistema genera grani); la map PGE = **output** (il sistema genera grani → la map mostra cosa è successo). Stessa famiglia di artefatti, inversione di flusso.

### 4. Truax 1990 — tendency masks come input visivo

> «*the composer functions not as an omniscient arbiter, but as the source of control messages that guide the overall process without directly determining it*» (p. 132, [[truax1990]])

Consolidamento della postura: le tendency masks sono lo strumento visivo con cui il compositore interagisce col processo. L'asse Y è ancora frequenza o parametro di controllo. L'overlay multi-parametro di Fig. 4 (1988) è qui integrato nel flusso compositivo real-time.

### 5. Roads 2001 — pulsar graph (Y = note values)

Fig. 5a in [[roads2001-pulsars]]: asse Y = note values (non frequenza Hz né posizione buffer), X = tempo. Notazione per la rhythm structure di un pulsar train. Polo cugino della map PGE — scope ridotto a un singolo parametro, asse Y specifico al pulsar domain. Conferma che nella lineage UCSB la rappresentazione visiva per-parametro è lo strumento analitico naturale della composizione granulare/particle.

### 6. Roads 2006 — Ynez project, "study scores for electronic music"

> «*Study scores and for electronic music, comprising still images that intermingle sonographic, iconic, and symbolic representations.*» (p. 11, [[roads2006]])

Categoria dichiarata esplicitamente come obiettivo di ricerca UCSB. Roads identifica la classe di artefatti — still images che mescolano rappresentazioni sonografiche, iconiche e simboliche — senza presentare un'implementazione per output granulare deferred. PGE materializza la categoria: il PDF A3 landscape con frecce (iconico), colore pitch-ratio (simbolico), asse Y posizione-buffer (sonografico-spaziale).

### 7. Caires 2004 — IRIN Timeline (Y = traccia, editabile)

> «*tracks may be used precisely as a compositional tool, helping the composer to arrange the polyphonic stratification of his material in a more systematic way*» (p. 222, [[caires2004]])

Timeline IRIN con shapes-view colorato per grano. Primo software documentato che tratta la partitura granulare come strumento compositivo autonomo (non ridondanza del playback). Asse Y = numero di traccia (layout polifonico); décorrélation microtemporelle come attributo visivamente editabile. **Input** — il compositore edita la Timeline e renderizza ciò che vede. PGE inverte: il compositore scrive YAML e verifica visivamente ciò che ha scritto.

### 8. Valle-Lombardo 2003 — GeoGraphy space actant (anti-analogia)

Lo *space actant* di GeoGraphy ([[valle-lombardo2003]]) è **input di controllo compositivo**: il compositore disegna trajectory nello spazio; lo space actant le scansiona modulando parametri granulari via distanza dai vertici. La map PGE è **output diagnostico read-only**. Oggetti opposti per ruolo nel workflow: input vs output, eventi potenziali vs attuali, editabile vs derivato. La quote p. 139 «*a map space should be used with caution in simulating a time/frequency space*» è un avvertimento sul limite intrinseco della rappresentazione spaziale come proxy del tempo — non si trasferisce a PGE dove l'asse Y è la grandezza fisica effettiva (posizione nel buffer).

### 9. Roads et al. 2021 — EC2 Scan Display (real-time)

EmissionControl2 Scan Display ([[roads2021]]): pointer dei grani sovrapposti al waveform in **real-time**. Stesso fenomeno fisico (lettura nel buffer), scopi opposti: Scan Display = feedback gestural durante performance; Score Visualizer PGE = analisi e riflessione *post-synthesis* per ciclo di riscrittura. EC2 mostra *dove* il sistema sta leggendo adesso; PGE mostra *dove ha letto* nell'intera composizione.

### 10. Anatrini 2024 — WavePilot meta-GUI (anti-analogia)

Meta-GUI come spazio di navigazione dello spazio parametrico ([[anatrini2024]]). Stessa inversione input/output osservata in [[valle-lombardo2003]]: la meta-GUI WavePilot è *spazio di controllo* (il compositore naviga per generare suono); la map PGE è *output diagnostico*. Convergenza di obiettivo (rendere navigabile lo spazio parametrico), inversione di flusso.

## Tavola sinottica

| Anno | Sistema | Asse Y | Ruolo | I/O |
|---|---|---|---|---|
| 1978 | Roads AGS | frequenza | metafora geometrica | — |
| 1985 | Roads CIM VI | frequenza | illustrazione su carta | — |
| 1988 | Truax DMX-1000 | parametro di controllo | tendency mask | **input** |
| 2001 | Roads PulsarGenerator | note values | notazione singolo param. | **output** |
| 2003 | Valle GeoGraphy | spazio topology | space actant | **input** |
| 2004 | Caires IRIN | traccia (polifonia) | timeline editabile | **input** |
| 2006 | Roads Ynez | (dichiarato, non impl.) | study score | — |
| 2021 | Roads EC2 | waveform position | scan display real-time | **output** |
| 2024 | Anatrini WavePilot | dimensione latente | meta-GUI navigabile | **input** |
| 2026 | PGE | **posizione buffer** | map (study score) deferred | **output** |

## Differenziatore PGE nel lineage

Due assi di differenziazione:

1. **Asse Y = posizione nel buffer sorgente.** Non frequenza (Roads 1978/1985/1988), non parametro generico (Truax 1988), non traccia (Caires 2004), non dimensione latente (Anatrini 2024). La scelta è motivata dal caso d'uso: granulazione di campioni. Truax 1994 descrive a parole il *meccanismo* che la map PGE rende osservabile: il movimento della testina di lettura nel buffer rispetto al tempo macro. Truax 2014 (p. 2) ne aggiunge il correlato percettivo: «*listening "inside" the sound*» — la dilatazione temporale sposta l'attenzione verso le componenti spettrali interne. L'asse Y PGE rende visibile *dove* il compositore sta ascoltando dentro il campione. Lippe 1993 (p. 180) legittima ulteriormente: «*onset time into the stored sound [...] of primary importance*» ([[lippe1993]]).

2. **Inversione di flusso: output, non input.** Nel lineage dominano le partiture-input (Truax 1988 tendency masks, Caires 2004 Timeline, Valle 2003 space actant, Anatrini 2024 meta-GUI). PGE inverte: la partitura è *risultato* della specifica YAML, non sua sorgente. Il compositore scrive intenzioni parametriche nel DSL, genera, verifica il risultato nella map, riscrive. La map è il componente visivo del loop lungo — il *feedback del triangolo opératoire* (cfr. [[interactivity-rate]]).

## La map nel quadro descrittivo/prescrittivo: né log né partitura, ma mappa

La tradizione della notazione oppone due poli: **prescrittivo** — istruzione
ex-ante su cosa fare, che «*may not necessarily reflect the sonic result*»
([[frame2023]] p. 23) — e **descrittivo** — resa a posteriori dell'esito,
«*typically used for analysis or discussion*», fino a coincidere con la pura
documentazione/log ([[frame2023]] p. 23). I due poli non sono mutuamente
esclusivi: un solo artefatto può servirli entrambi ([[bacon2022]] p. 75;
[[hron2017]] p. 114, l'Acousmographe «*simultaneously descriptive and
prescriptive*»).

La map di PGE (la «MAP» nel paper) sta fuori da entrambi: non
prescrive (non pilota il motore — l'inversione di flusso del differenziatore 2)
e non è puro log (non trascrive un ascolto: è generata dalla specifica
dichiarativa). È **mappa sinottica** del processo dichiarato — e «mappa» non è
metafora libera: Bacon lega esplicitamente la notazione alla cartografia e alle
sue tecniche di stratificazione informativa («*bridging notation with the many
information layering techniques found in map making*», [[bacon2022]] p. 70).
Questo è il quadro con cui il paper scioglie il nodo «log vs partitura»
(introduzione + conclusioni): la MAP è un terzo termine, cartografico, fra la
partitura-istruzione e il log-documentazione.

Distinzione dai precedenti TENOR del «doppio servizio»: in [[hron2017]] la
rappresentazione è analisi a posteriori (Acousmographe sull'eseguito) *riusata*
come prescrizione; la MAP non viene riusata come input — resta output. Il
parente sull'asse del *differimento* è [[magnusson2015]] (code-score real-time
eseguibile e alterabile): polo opposto rispetto a cui la MAP differita si
definisce.

Nota terminologica: «sinottico» è parola del paper, assente nei PDF TENOR — va
appoggiata su Bacon (cartografia), non spacciata per lessico della venue. La
coppia prescrittivo/descrittivo è canonicamente di Charles Seeger (1958):
citazione esterna da aggiungere a parte se serve l'ur-fonte (Frame la attribuisce
a un riferimento non risolto nel PDF).

## Encoding visivo della map PGE (`score_visualizer`)

Per ogni grano, il PDF A3 landscape codifica:
- **Freccia**: su = playback avanti, giù = inverso (direzione di lettura nel buffer)
- **Colore**: pitch ratio via coolwarm colormap
- **Opacità**: volume dB
- **Larghezza**: durata grano
- **Altezza**: campioni consumati nel buffer
- **Posizione X**: onset nel tempo macro
- **Posizione Y**: posizione nel buffer sorgente

Loop mask e envelope panel come pannelli aggiuntivi. 30 secondi/pagina.

Cfr. [[score-visualizer]] per dettagli implementativi.

## Fonti

- [[roads1978]] — polygon su piano freq/tempo
- [[roads1985]] — Figg. 7–9 primo precursore CIM
- [[truax1988]] — Fig. 4 ASCII tendency masks
- [[truax1990]] — tendency masks come input visivo
- [[truax1994]] — meccanismo testina di lettura descritto a parole
- [[truax2014]] — «listening inside the sound» correlato percettivo
- [[lippe1993]] — «onset time into the stored sound of primary importance»
- [[roads2001-pulsars]] — pulsar graph (Fig. 5a, Y=note values)
- [[roads2006]] — Ynez project, «study scores for electronic music»
- [[caires2004]] — IRIN Timeline shapes-view
- [[valle-lombardo2003]] — GeoGraphy space actant (anti-analogia)
- [[roads2021]] — EC2 Scan Display
- [[anatrini2024]] — WavePilot meta-GUI (anti-analogia)
- [[score-visualizer]] — implementazione PGE
- [[frame2023]] — TENOR 2023: definizioni prescrittivo/descrittivo + descrittivo = documentazione/log
- [[bacon2022]] — TENOR 2022: notazione↔cartografia, information layering (fonda «mappa sinottica»); poli non esclusivi
- [[hron2017]] — TENOR 2017: Acousmographe «simultaneously descriptive and prescriptive» (collasso log↔score)
- [[magnusson2015]] — TENOR 2015: code-score real-time (contrasto sull'asse del differimento)

## Sezioni del paper CIM 2026 dove citare

- **`sec:architettura`** (primaria): la map è descritta qui, non in sezione
  propria. Doppio differenziatore (asse Y = posizione di lettura + inversione
  di flusso); Truax 1994/2014 per la motivazione dell'asse Y. Caires 2004 ed
  EC2 come poli di contrasto (input editabile, real-time pointer). Ynez 2006
  come categoria dichiarata, PGE come implementazione. Cluster delle fonti
  (cfr. [[mappa-citazioni-paper]]): Truax 1988 Fig. 4, Roads polygon
  1978/1985, Caires 2004, Valle-Lombardo 2003, Lippe 1993 p. 180,
  Truax 1994/2014.
- **non citato nel paper** («tradizione», sezione rimossa e confluita in `sec:conclusioni`): il precursore concreto della proposta 2
  (Truax 1988 Fig. 4) e la descrizione verbale del meccanismo (Truax 1994),
  già nominati nel testo del paper.

Fuori paper: sviluppi futuri (GUI interattiva che renda la partitura anche
input) → presentazione orale / secondo paper GUI / eventuale chiusura se
ripristinata.
