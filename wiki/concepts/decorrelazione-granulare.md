---
name: decorrelazione-granulare
description: Decorrelazione come framework tecnico-compositivo nella sintesi granulare — da fenomeno osservato (1992) a parametro esplicito (2000) ad attributo morfologico di prima classe (2002). Mapping su PGE.
metadata:
  type: project
---

# Decorrelazione granulare

## Definizione tecnica

La **cross-correlation** fra due segnali $y_1(t)$ e $y_2(t)$ è definita (Rolfe-Keller 2000, [[rolfe-keller2000]]):

$$F(\tau) = \lim \frac{1}{T} \int y_1(t) \cdot y_2(t+\tau) \, dt$$

normalizzata al range $-1.0 \leq k \leq 1.0$. Correlazione massima ($k=1.0$) = segnali identici in fase; decorrelazione ($k \to -1.0$) = segnali in controfase.

In sintesi granulare la decorrelazione emerge come **by-product strutturale**: distribuzione stocastica dei parametri su più stream produce automaticamente output parzialmente decorrelati. Truax (1992) e Kendall (1995) lo notano senza formalizzarlo come variabile di controllo.

## Filiazione cronologica CIM → CMR

| Anno | Fonte | Contributo |
|---|---|---|
| 1998 | [[keller-rolfe1998]] (CIM XII) | Ontologia *stream / waveform / pointer / event* — entità nominate. Base concettuale. |
| 2000 | [[rolfe-keller2000]] (CIM XIII) | **Teoria misurabile su 3 livelli ortogonali.** Decorrelazione da fenomeno osservato a parametro di controllo esplicito e variabile. |
| 2002 | [[vaggione2002]] (CMJ) | **Attributo morfologico-spaziale di prima classe.** *Décorrélation microtemporelle* come dimensione composable al pari di altezza, durata, densità. |

## I tre livelli ortogonali (Rolfe-Keller 2000)

| Livello | Scala | Meccanismo |
|---|---|---|
| **Grain-to-grain** (intra-stream) | Singolo grano | grain duration wander + advance rate scan |
| **Cross-channel/stream** (inter-stream) | Tra stream | delay-range per stream + pairing per cancellare AM |
| **Instance/event** (inter-execution) | Tra esecuzioni | distribuzione random sui delay tap |

Trade-off esplicito (Rolfe-Keller 2000, sez. 3): scegliere *decorrelation* (chorusing/thickening) significa «forgoing the goal of transparency» — i due poli (transparency vs. decorrelation) sono mutuamente esclusivi nella scelta real-time single-shot.

## Décorrélation microtemporelle (Vaggione 2002)

Condizioni minime (Vaggione 2002, p. 6):
1. Repliche distribuite su canali fisicamente diversi (evitare phasing/colorazioni frequenziali)
2. Polifonia con valori time-varying degli offset (offset fisso = immagine spaziale fissa)
3. Offset nell'ordine dei millisecondi (offset più grandi = eventi separati, non decorrelazione)

Distinzione fondamentale rispetto al panning classico: il panning opera su «*champ spatial stable, synchronique [...] externe, non lié directement aux relations entre les morphologies en jeux*» (p. 9). La decorrelazione è *interna* alla morfologia: la posizione spaziale è attributo costitutivo della figura, non aggiunta in post.

Risultato percettivo: «*une grande quantité de différences locales de phase, négatives et positives, qui se succèdent rapidement. C'est cette relation kaléidoscopique ("multi-locale") qui contribue à instaurer une dynamique spatiale*» (Vaggione 2002, p. 7).

## Mapping su PGE

| Livello Rolfe-Keller | Tool Rolfe-Keller | Componente PGE | Note |
|---|---|---|---|
| Grain-to-grain | grain duration wander + advance rate | `PointerController.speed_ratio` + `Envelope` range | deviazione per-grano |
| Cross-channel/stream | delay-range per stream + pairing | `VoiceManager` dephase strategy + N stream YAML | dephase inter-stream |
| Instance/event | distribuzione random sui delay tap | `DistributionStrategy` (uniform/gaussian) | ogni run = instance decorrelata |

PGE e la tesi centrale:

**PGE inverte il trade-off di Rolfe-Keller**: in real-time single-shot occorre scegliere il polo (transparency vs. decorrelation). PGE, operando in deferred time, espone entrambi i poli come configurazioni del DSL YAML e permette il confronto diretto fra rendering successivi — il loop lungo come strumento di esplorazione dello spazio transparency/decorrelation.

**VoiceManager come décorrélation microtemporelle strutturale**: le quattro strategie (`pitch`, `onset`, `pointer`, `pan`) producono per ogni voce una replica decorrelata di Stream — realizzazione diretta delle condizioni di Vaggione 2002. La `onset_offset` strategy = decalage di ms tra repliche (condizione 3); `pan` = distribuzione su canali separati (condizione 1); layering = polifonia time-varying (condizione 2).

**Partitura grafica come rivelatore di decorrelazione**: gli onset offset per-voce e il dephase per-grano sono osservabili come scarti orizzontali tra grani nel `score_visualizer` — PGE rende visibile *prima dell'ascolto* ciò che Rolfe-Keller affidano al solo orecchio («*tuned by ear to the desired result*», sez. 3).

## Contesto PGE nella filiazione

PGE eredita tutte e tre le tappe della filiazione:
- L'**ontologia** stream/pointer/event ([[keller-rolfe1998]], 1998)
- Gli **strumenti tecnici** di controllo della correlazione su 3 livelli ([[rolfe-keller2000]], 2000)
- La **dignità compositiva** della decorrelazione come attributo morfologico ([[vaggione2002]], 2002)

Vaggione 2002 conferma che la pratica è nata in deferred time («*en temps différé*», p. 3) ed è stata estesa al real-time come opzione successiva — pattern identico a PGE.

## Sezioni del paper CIM 2026

- **Sezione 2**: 3 livelli Rolfe-Keller come framework di analisi del comportamento decorrelativo di PGE; filiazione CIM 1998–2000–CMR 2002 come linea critica distinta da Truax
- **Sezione 3**: VoiceManager + dephase come implementazione strutturale della décorrélation microtemporelle; tabella mapping
- **Sezione 4**: partitura grafica come rivelatore visivo della decorrelazione (asse X + scarti orizzontali) — anti-citazione Rolfe-Keller *"tuned by ear"*
- **Sezione 6**: trade-off transparency/decorrelation come esempio di esplorazione abilitata dal loop lungo vs. scelta single-shot real-time
