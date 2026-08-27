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
- errore relativo **mediano 1,1%**, massimo 2,4%

Due parametri spiegano tre ordini di grandezza di grani e due di durata.

**Densità di pareggio dei due termini: ~41 grani/s.** Sotto, comanda la durata;
sopra, comandano i grani. Il regime granulare d'uso sta sopra (Roads, cap. 3,
p. 106: 50-100 g/s è la banda continua, oltre 100 la massa), quindi il claim
resta vero *nel regime in cui si lavora*, ma non come enunciato assoluto. A
densità 100 il termine dei grani pesa 2,4 volte quello della durata; a 800 pesa
venti volte.

Caso di riferimento citato nel paper: **30 000 grani su 5 minuti di uscita,
1,3 s**.

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
riferimento e il fit; scrive `paper/examples/bench_cost.json` (gitignorato: è
una misura di macchina). Non è prerequisito di `make paper` — rilanciarlo altrove
cambierebbe i numeri stampati nel paper.

## Dove sta nel paper

`sec:architettura`, dentro `\notaRepo`: formula, densità di pareggio, caso
concreto, condizioni. Cfr. [[numpy-audio-renderer]] per il meccanismo di
overlap-add e il parallelo.
