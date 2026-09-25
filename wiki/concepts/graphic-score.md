# Rappresentazioni visive per sintesi granulare — lineage storico (verso la map)

> Nota lessicale: nel paper consegnato l'output visivo di PGE si chiama
> **MAP** (*Multiparametric Audio Plot*), «mappa sinottica». La parola
> «partitura» resta solo per gli *altri* sistemi del lineage e per contrasto.
>
> Cosa dice il paper (`sec:architettura`, nota `\notaLineage`): precedenti
> Truax 1988 Fig. 4 (p. 24, «*inherently a visual control method*», p. 23),
> Roads 1978 (p. 62) e 1985 (p. 200), IRIN (Caires 2004); differenza: nella
> MAP l'ordinata è il punto del materiale da cui proviene ciascun grano. Nel
> senso di Seeger la MAP è notazione **descrittiva**. Il resto della pagina è
> lineage della knowledge base: le fonti non elencate qui non sono citate.

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

Fig. 4 ([[truax1988]]): overlay di quattro curve ASCII su terminale 24 righe — frequency mask, duration mask, amplitude envelope, delay envelope. Primo precedente *concreto* di rappresentazione visiva multi-parametro tempo-dipendente per controllo granulare.

**Correzione 2026-08-26 (lettura diretta del PDF, pp. 23–24 = PDF pp. 10–11).** La formulazione precedente («disegnato dal compositore prima del rendering», «curve che il compositore traccia») era sbagliata: il terminale non è una superficie di disegno. Il compositore *specifica* fino a tre maschere e due inviluppi (dieci segmenti ciascuno, salvati su file o generati per interpolazione fra preset) e il programma ne restituisce la sovrapposizione: «*A graphic overlay of the masks and envelopes shows their synchronization (Fig. 4)*» (p. 23). Durante l'esecuzione «*the current values are reported to the user via the screen values once every second*» (p. 23). Resta corretta la classificazione come **input** nel senso che ciò che è plottato pilota la sintesi, ma la ragione è questa, non il gesto del disegnare.

**Il discrimine utile non è input/output, è cosa sta sugli assi.** Fig. 4 ha ascissa tempo (0–22) e ordinata il valore del parametro (0–100): plotta le **curve di controllo**, non gli eventi. È l'equivalente del pannello inferiore della map PGE (gli inviluppi coi breakpoint), non del pannello superiore. Truax possiede già metà dell'oggetto; la metà che manca è la popolazione materializzata.

Differenza fondamentale con PGE: Truax Fig. 4 = **input** (il compositore specifica le maschere, il programma le plotta, il sistema genera grani); la map PGE = **output** (il sistema genera grani → la map mostra cosa è successo). Stessa famiglia di artefatti, inversione di flusso.

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

EmissionControl2 Scan Display ([[roads2021]]): pointer dei grani sovrapposti al waveform in **real-time**. Scopi opposti: Scan Display = feedback gestuale durante performance; map PGE = analisi *post-synthesis* per il ciclo di riscrittura. EC2 mostra *dove* il sistema sta leggendo adesso; PGE mostra *dove ha letto* nell'intera composizione.

**Correzione 2026-08-26 (didascalia Fig. 3 e p. 25 del PDF).** Lo Scan Display **non appartiene al lineage del piano cartesiano**: «*showing the waveform of the sound file from which EC2 is currently sampling grains. The scan range is overlaid on the sound file*». È una forma d'onda disegnata orizzontalmente con marker sopra, quindi **un asse solo** (la posizione nel buffer, in ascissa) e nessun asse per il tempo dello stream. È il monitor del buffer che hanno tutti gli ambienti real-time, `waveform~` di Max compreso. Va tenuto fuori dal confronto con la map: la versione precedente di questa voce lo trattava come parente prossimo per via dell'asse, e sbagliava. Escluso su indicazione dell'utente dalla nota `\notaLineage` del paper.

### 10. Anatrini 2024 — WavePilot meta-GUI (anti-analogia)

Meta-GUI come spazio di navigazione dello spazio parametrico ([[anatrini2024]]). Stessa inversione input/output osservata in [[valle-lombardo2003]]: la meta-GUI WavePilot è *spazio di controllo* (il compositore naviga per generare suono); la map PGE è *output diagnostico*. Convergenza di obiettivo (rendere navigabile lo spazio parametrico), inversione di flusso.

## Tavola sinottica

Colonna «Cosa è plottato» aggiunta il 2026-08-26: è il discrimine che regge la
rivendicazione del paper, mentre la colonna I/O da sola non discrimina (cfr.
correzione alla voce 3 e nota `\notaLineage` in `sec:architettura`).

| Anno | Sistema | Asse Y | Cosa è plottato | Ruolo | I/O |
|---|---|---|---|---|---|
| 1978 | Roads AGS | frequenza | forma della nuvola (metafora) | metafora geometrica | — |
| 1985 | Roads CIM VI | frequenza | forma della nuvola (metafora) | illustrazione su carta | — |
| 1988 | Truax DMX-1000 | valore del parametro | **curve di controllo** | tendency mask | **input** |
| 2001 | Roads PulsarGenerator | note values | curve di un parametro | notazione singolo param. | **output** |
| 2003 | Valle GeoGraphy | spazio topology | traiettorie di controllo | space actant | **input** |
| 2004 | Caires IRIN | traccia (polifonia) | **eventi effettivi** | timeline editabile | **input** |
| 2006 | Roads Ynez | (dichiarato, non impl.) | (dichiarato, non impl.) | study score | — |
| 2021 | Roads EC2 | *nessuna* (asse unico: il buffer in ascissa) | grani vivi, come marker sul buffer | scan display real-time | **output** |
| 2024 | Anatrini WavePilot | dimensione latente | spazio di controllo | meta-GUI navigabile | **input** |
| 2026 | PGE | **posizione buffer** | **eventi effettivi** + curve nel pannello sotto | map (study score) deferred | **output** |

## Differenziatore PGE nel lineage

Due assi di differenziazione:

1. **Asse Y = posizione nel buffer sorgente.** Non frequenza (Roads 1978/1985/1988), non parametro generico (Truax 1988), non traccia (Caires 2004), non dimensione latente (Anatrini 2024). La scelta è motivata dal caso d'uso: granulazione di campioni. (Knowledge base, non nel paper, da qui a fine punto:) Truax 1994 descrive a parole il *meccanismo* che la map PGE rende osservabile: il movimento della testina di lettura nel buffer rispetto al tempo macro. Truax 2014 (p. 2) ne aggiunge il correlato percettivo: «*listening "inside" the sound*» — la dilatazione temporale sposta l'attenzione verso le componenti spettrali interne. L'asse Y PGE rende visibile *dove* il compositore sta ascoltando dentro il campione. Lippe 1993 (p. 180) legittima ulteriormente: «*onset time into the stored sound [...] of primary importance*» ([[lippe1993]]).

2. **Inversione di flusso: output, non input.** Nel lineage dominano le partiture-input (Truax 1988 tendency masks, Caires 2004 Timeline, Valle 2003 space actant, Anatrini 2024 meta-GUI). PGE inverte: la partitura è *risultato* della specifica YAML, non sua sorgente. Il compositore scrive intenzioni parametriche nel DSL, genera, verifica il risultato nella map, riscrive. Nel paper: la MAP «non viene riletta come input» (`sec:architettura`) e «sostituisce il tentativo per approssimazioni successive» (`sec:conclusioni`). La lettura come *feedback del triangolo opératoire* (cfr. [[interactivity-rate]]) è della knowledge base.

## La MAP nel quadro descrittivo/prescrittivo

La tradizione della notazione oppone due poli: **prescrittivo** — istruzione
ex-ante su cosa fare, che «*may not necessarily reflect the sonic result*»
([[frame2023]] p. 23) — e **descrittivo** — resa a posteriori dell'esito,
«*typically used for analysis or discussion*», fino a coincidere con la pura
documentazione/log ([[frame2023]] p. 23). I due poli non sono mutuamente
esclusivi: un solo artefatto può servirli entrambi ([[bacon2022]] p. 75;
[[hron2017]] p. 114, l'Acousmographe «*simultaneously descriptive and
prescriptive*»).

**Posizione del paper** (`sec:architettura`): «Nel senso di
Seeger~\cite{Seeger1958} lo YAML è notazione prescrittiva, istruzione data al
motore prima del rendering. La MAP è notazione descrittiva: documenta ciò che è
stato effettivamente generato, e non viene riletta come input.» Il paper non
la presenta come terzo termine fra partitura e log e non cita le fonti TENOR.

Lettura della knowledge base, non adottata dal paper: la MAP non è un log di
ascolto (è generata dalla specifica dichiarativa), e «mappa» si può appoggiare
su Bacon, che lega la notazione alla cartografia («*bridging notation with the
many information layering techniques found in map making*», [[bacon2022]]
p. 70).

Distinzione dai precedenti TENOR del «doppio servizio»: in [[hron2017]] la
rappresentazione è analisi a posteriori (Acousmographe sull'eseguito) *riusata*
come prescrizione; la MAP non viene riusata come input — resta output. Il
parente sull'asse del *differimento* è [[magnusson2015]] (code-score real-time
eseguibile e alterabile): polo opposto rispetto a cui la MAP differita si
definisce.

Nota terminologica: «sinottico» è parola del paper, assente nei PDF TENOR. La
coppia prescrittivo/descrittivo è di Charles Seeger (1958), che il paper cita
direttamente in `sec:architettura`.

## Encoding visivo della MAP, come lo descrive il paper

Da `sec:architettura` e `sec:completo`:
- **Ascissa**: tempo dello stream; **ordinata**: posizione di lettura nel file;
  a sinistra, sullo stesso asse verticale, la forma d'onda della sorgente.
- **Ogni grano è un poligono**: posizione orizzontale = onset, verticale =
  punto di lettura; larghezza = durata; altezza = spazio percorso nel buffer.
- **Testa**: orientamento = verso di lettura del buffer per quel grano; sulla
  testa è disegnato il profilo della finestra (il glifo «non è una freccia ma
  la silhouette della finestra», `sec:completo`).
- **Colore**: trasposizione del grano, con colorbar a scala lineare e unità
  dinamica stampata sulla legenda.
- **Pannello inferiore**: gli inviluppi dichiarati, con i breakpoint annotati.
- **Lenti**: ingrandimenti di dettagli illeggibili a piena scala (`fig:c-e`,
  `fig:griglia-map`, `fig:dimensioni`, `fig:completo`).

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

- **`sec:architettura`**: la MAP, lettura e precursori in nota (Truax 1988 Fig. 4, Roads 1978/1985, Caires 2004).
- **`sec:conclusioni`**: la MAP sostituisce i tentativi per approssimazioni successive; limite del colore.
