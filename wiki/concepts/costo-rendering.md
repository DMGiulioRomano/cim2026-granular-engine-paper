# Costo del rendering: numero di grani e durata dell'uscita

Misura fatta il 2026-08-27 per chiudere il punto C1 della review interna
(`raw/reviews/claude-review-claims-2026-08-26.md`), che segnalava «zero misure»
sotto il claim di `\notaRepo`: «il costo di calcolo non cresce con la durata
d'ascolto ma col numero di grani».

## Il claim era falso come assoluto

A numero di grani costante (~4000) e durata dell'uscita crescente da 5 a 320
secondi, il tempo di rendering passa da 0,13 a 0,54 s. La durata pesa: il buffer
di uscita va allocato, normalizzato e scritto, e quel lavoro scala coi campioni,
non coi grani.

## Modello a due termini

$$t \approx a \cdot N_{\text{grani}} + b \cdot D_{\text{secondi}}$$

Fit ai minimi quadrati su 24 punti (tre sweep: densità crescente a durata fissa;
grani fissi a durata crescente; densità fissa a durata crescente), copertura da
$10^2$ a $3{\cdot}10^4$ grani e da 5 a 320 s:

- $a \approx 32\ \mu s$ per grano
- $b \approx 1{,}3\ ms$ per secondo di uscita
- errore relativo **mediano sotto l'1%**, massimo ~2%
  (su run ripetute i coefficienti oscillano di qualche punto percentuale, la
  densità di pareggio resta 40-41 grani/s)

Due parametri spiegano tre ordini di grandezza di grani e due di durata.

**Densità di pareggio dei due termini: ~41 grani/s.** Sotto, comanda la durata;
sopra, comandano i grani. Il regime granulare d'uso sta sopra (Roads, cap. 3,
p. 106: 50-100 g/s è la banda continua, oltre 100 la massa), quindi il claim
resta vero *nel regime in cui si lavora*, ma non come enunciato assoluto. A
densità 100 il termine dei grani pesa 2,4 volte quello della durata; a 800 pesa
venti volte.

Caso di riferimento citato nel paper: **l'esempio completo di `sec:completo`,
38 072 grani su 32,4 s, poco più di un secondo** (~29 µs/grano). È un esempio
reale multi-stream, con voci e deviazioni, quindi con un costo per grano diverso
da quello degli sweep: sta fuori dal fit e serve a verificare l'ordine di
grandezza, non a stimare i coefficienti. Un caso sintetico più estremo — 30 000
grani distribuiti su cinque minuti — si rende in 1,4 s, ma nel paper si legge
male: invita a pensare al fattore rispetto al tempo reale, che non è il punto.

## Dove va il tempo: costruire la popolazione costa quanto sommarla

I grani sono **lazy** (`Stream.grains` è una property che chiama
`generate_grains()` al primo accesso), quindi chi tocca `.grains` per primo è il
render: senza forzare la materializzazione, il costo di costruire gli oggetti
`Grain` finisce dentro il tempo di rendering. Forzarla prima non cambia il
totale — verificato sull'esempio completo, 1,071 s a freddo contro 1,085 s
materializzando prima — ma mostra la ripartizione:

| fase | tempo | per grano |
|---|---|---|
| parse YAML + `create_elements` | 0,008 s | — |
| costruzione dei 38 072 oggetti `Grain` | **0,523 s** | 13,7 µs |
| overlap-add + normalizzazione + scrittura | **0,571 s** | 15 µs |

Metà del costo è la materializzazione della rappresentazione intermedia, non il
DSP. È coerente con la tesi: il prezzo si paga per avere la popolazione esplicita
e ispezionabile, che è la cosa che rende possibile la \textsc{map}.

Wall clock del processo intero (interprete + import di NumPy e matplotlib +
lavoro): 1,44 s, di cui 0,29 s di soli import. Nessun costo fuori dalla misura.

## Condizioni della misura

- PGE pinnato dal submodule (v8.0.0), renderer NumPy, output 48 kHz, cache off.
- **Rendering sequenziale, `jobs=1`.** Il default della CLI è `--jobs auto`, ma
  il claim riguarda la scala, non il wall clock: col pool attivo sotto il
  migliaio di grani lo spawn costa più di quanto rende (a 999 grani 0,04 s
  sequenziali; oltre i ~2000 grani, soglia `min_parallel_grains`, il pool
  aggiunge circa un secondo fisso alla prima chiamata).
- Apple M2 Max, Python 3.11. Su un'altra macchina cambiano i coefficienti, non
  la forma del modello.

## Riproduzione

`make bench` → `paper/examples/bench_cost.py`. Stampa i tre sweep, il caso di
riferimento (che rende `paper/examples/complete_example/`) e il fit; scrive `paper/examples/bench_cost.json` (gitignorato: è
una misura di macchina). Non è prerequisito di `make paper` — rilanciarlo altrove
cambierebbe i numeri stampati nel paper.

## Dove sta nel paper

`sec:architettura`, dentro `\notaRepo`: formula, densità di pareggio, caso
concreto, condizioni. Cfr. [[numpy-audio-renderer]] per il meccanismo di
overlap-add e il parallelo.
