# Time-stretching granulare — meccanismo, artefatto comb, decorrelazione

Sintesi da sessione di indagine (2026-06-11) su `speed_ratio < 1` in PGE:
perché lo stretch granulare "nudo" suona male, perché non è un bug, e come
la tradizione (Truax 1994) ha sempre risposto con la decorrelazione.

## Definizione e distinzione

**Time-stretching**: il tempo macro cambia, il pitch micro resta intatto.
**Varispeed**: pitch e tempo cambiano insieme (nastro rallentato).

In PGE la distinzione è strutturale: `PointerController.speed_ratio` muove
solo la testina di lettura (`pos = start + speed·t`, integrazione se Envelope),
mentre `pitch_ratio` è un controller indipendente. `speed_ratio: .5` con
pitch 1.0 = time-stretch 2×. Varispeed si ottiene agganciando esplicitamente
`pitch_ratio = speed_ratio` nel YAML — il disaccoppiamento dei due controller
rende entrambe le posture esprimibili nel DSL.

Fonte primaria: [[truax1994]] introduce la **variable-rate granulation** con
time-extension factor `TEF = (off+on)/on` (eq. 1, p. 42); prima presentazione
Truax ICMC 1990 (*Time-shifting of sampled sound...*, Glasgow, non in repo).
Pitch invariato esplicito: *"the frequency of the source material is not
distorted, only the rate at which the user advances through it in a
macro-level sense"* (p. 41).

## L'artefatto comb: matematica

Con IOT metronomico e grani deterministici, due grani sovrapposti allo stesso
istante di output `t` leggono dal buffer posizioni distanti:

```
offset = (1 − s) · IOT          s = speed_ratio
```

La somma di due copie sfasate di `offset` = comb filter con notch ogni
`1/offset` Hz a partire da `1/(2·offset)`. Con i default PGE (grain 50 ms,
fill_factor 2 → IOT 25 ms):

| speed s | offset | primo notch | spacing |
|---|---|---|---|
| 1.0 | 0 ms | — | — (identità, ricostruzione esatta) |
| 0.5 | 12.5 ms | 40 Hz | 80 Hz |
| 0.0 (freeze) | 25 ms | 20 Hz | 40 Hz (il "ronzio" di ex2) |

A `s = 1` i grani sovrapposti leggono lo stesso campione sorgente → COLA
ricostruisce esattamente (residuo −74 dB, fig. 1 paper). Sotto 1, il comb
scala linearmente con `(1−s)`. Il **fill_factor è innocente**: l'inviluppo
d'ampiezza resta piatto (COLA vale a ogni speed); l'artefatto è interferenza
di fase fra letture disallineate, non buco di copertura.

## Verifica empirica (2026-06-11, PGE @ 9c4cb4a)

1. **Posizioni pointer esatte al bit**: stream minimo `speed_ratio: .5`,
   79 grani; `max |pos − 0.5·onset| = 0.0`; offset inter-grano misurato
   12.5000 ms = teoria. Nessun errore d'implementazione.
2. **Comb riprodotto in OLA numpy puro** (30 righe, senza PGE), grani identici
   ai default: sinusoide 400 Hz (5.0 cicli in 12.5 ms, in fase) passa intatta
   a speed 0.5 (RMS 0.707 invariato); 440 Hz (5.5 cicli, controfase) attenuata
   a RMS 0.500 (−3 dB) con picco spostato a 420 Hz. Attenuazione
   frequenza-dipendente con periodo 80 Hz = comb predetto.

Conclusione: artefatto **intrinseco al metodo**, qualunque granulatore con
offset deterministico e IOT fisso lo produce identico.

## La risposta storica: decorrelazione, non allineamento

Truax non ha mai inteso lo stretch granulare come ricostruzione fedele
rallentata: *"the purpose is to produce musically interesting sound and not
just a processed signal"* (p. 42). Tre meccanismi anti-comb in GSAMX, tutti
stocastici:

1. **Offset range per-grano** (p. 40): *"Varying the offset from grain to
   grain by means of the offset range allows each grain to be different and
   results in a richer aural effect"* → antenato diretto di
   `pointer.range`/dephase PGE.
2. **Delay/density stocastici** (p. 40): quasi-sync modulato o async con
   delay random 0..2×avg → `distribution` PGE (modello già dichiarato in
   [[density-controller|sources/pge/density-controller]]).
3. **Fino a 18 voci non sincronizzate** (p. 42) → `VoiceManager` + scatter.

Il comb tonale (notch fissi periodici) viene spalmato in rumore a banda
larga: tonale → soffio. Collegamento diretto con [[decorrelazione-granulare]]
(trade-off transparency vs decorrelation di Rolfe-Keller 2000: lo stretch
nudo è il polo transparency che fallisce, la decorrelazione è il polo che
la tradizione sceglie).

Nota secondaria: grani ≤50 ms a inviluppo simmetrico letti in reverse sono
indistinguibili dal forward (p. 41) — antenato di `grain_reverse: auto` PGE.

## Mitigazioni alternative (senza decorrelazione)

- **Varispeed** (`pitch_ratio = speed_ratio`): ogni grano legge `x(s·t)` →
  offset = 0 → comb sparito, ma pitch cala. Ricostruzione pulita del segnale
  pitch-shiftato.
- **Grani più corti** a fill_factor fisso: IOT scende → offset `(1−s)·IOT`
  scende → notch spinti in alto (grain 10 ms → primo notch 200 Hz). Costo:
  rumore di grano in alta frequenza.
- **Più overlap** (fill_factor alto): più grani mediano la fase, notch
  attenuati e spinti in alto.

## Rilevanza per il paper CIM 2026

- **ex2_pointer (freeze)**: il ronzio del freeze è il caso limite `s = 0`
  dello stesso comb (offset = IOT pieno). Il commento YAML che lo presenta
  come *motivazione della sottosezione successiva* (deviazione per-grano)
  segue l'ordine storico esatto: stretch nudo espone l'artefatto → Truax
  risponde randomizzando l'offset → `range`/dephase.
- **Sezione 2**: variable-rate granulation come antenato di `speed_ratio`
  (già in [[truax1994]]); l'artefatto comb e la decorrelazione come ponte
  fra Truax 1994 e Rolfe-Keller 2000.
- **Sezione 3**: il disaccoppiamento pointer/pitch come scelta architetturale
  che espone time-stretch e varispeed come due punti dello stesso spazio
  parametrico YAML.

## Pagine collegate

[[truax1994]] · [[decorrelazione-granulare]] · [[tendency-mask]] ·
[[pointer-controller|sources/pge/pointer-controller]] ·
[[density-controller|sources/pge/density-controller]]
