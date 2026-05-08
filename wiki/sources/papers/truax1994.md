# [Truax, 1994] Discovering Inner Complexity: Time Shifting and Transposition with a Real-time Granulation Technique

## Citazione CIM
Truax, B. (1994). Discovering Inner Complexity: Time Shifting and Transposition with a Real-time Granulation Technique. *Computer Music Journal*, 18(2), 38–48.

## Argomento centrale
Truax descrive `GSAMX`, programma DMX-1000 per granulazione real-time di suono campionato, e introduce due estensioni rispetto al sistema 1988: (a) **variable-rate granulation** — interpolazione fra modalità fixed-sample e continuous-sample tramite ratio `off:on` che produce un *time-extension factor* (TEF) arbitrario senza alterare il pitch della sorgente; (b) **harmonization scheme** — trasposizione simultanea a serie armonica con fondamentale `F=4`, dove ogni voce o grain stream può scegliere armonico `N` indipendente. La conseguenza compositiva è ciò che Truax chiama "scoperta della complessità interna": stiramenti temporali estremi (TEF fino a 1000×) rivelano risonanze, voci interne e pattern micro-spettrali altrimenti inudibili — il paradigma "magnification" come strumento estetico.

## Gap o problema identificato
"Granulation is clearly situated in a different psychoacoustic domain than that occupied by most computer music, which commonly is based in instrumental music concepts. By separating the micro level from the macro level in terms of sound features and allowing pitch and time warping without the limitations inherent in Fourier-based approaches, the techniques introduced here create a unique sound world." (p. 48)

Truax formula esplicitamente la **separazione micro/macro come premessa fondante** del paradigma granulare: la granulazione "links frequency and time at the micro level [so it] makes it possible to treat these two variables independently at the macro level" (p. 44). Questa è la versione del 1994 del gap controllo/percezione di Truax 1990: il controllo deterministico singolo-grano è ancora dichiarato impraticabile ("Deterministic control by predetermined values would be burdensome for both the user and the computer", p. 40), ma il paper mostra che la sua impraticabilità *è la condizione abilitante* della complessità sonora interna emergente.

## Rilevanza diretta per PGE
Il paper è il precursore concettuale più diretto della scelta architetturale di PGE su `PointerController` + asse Y partitura. Quattro corrispondenze:

1. **Variable-rate granulation come ancestor di `speed_ratio` Envelope.** Il ratio `off:on` di Truax controlla "the rate at which new samples are introduced into the granulation process" (p. 41). In PGE `PointerController.speed_ratio` può essere costante o `Envelope` con integrazione: il TEF di Truax è una funzione del tempo che corrisponde all'integrale di `speed_ratio` (vedi `wiki/sources/pge/pointer-controller.md`). PGE generalizza il meccanismo a tempo differito con curva continua, eliminando la quantizzazione `off`/`on` ms imposta dal DMX-1000.

2. **Asse Y partitura PGE = visualizzazione esplicita del meccanismo Truax.** Truax descrive a parole come la testina di lettura del buffer si muova rispetto al tempo di output ("the rate at which the user advances through it", p. 41): la partitura grafica di PGE rende quel movimento osservabile come traiettoria sull'asse Y (posizione-nel-buffer) vs asse X (tempo). La scelta di PGE — Y = posizione-buffer e non frequenza — è motivata esattamente dal caso d'uso descritto qui: time-stretching di campioni dove il pitch resta intatto e l'unica variabile percettivamente significativa è *dove* nel buffer i grani vengono prelevati.

3. **Harmonization scheme F=4 come precedente del PitchController multi-voce.** Truax sceglie fondamentale F=4 per ottenere range ±2 ottave attorno al pitch originale (armonico 4 = unisono, armonici 5–8 = ottava sopra, armonici 1–3 = ottave sotto). DMX-1000 permette 15 voci simultanee ognuna con `N` indipendente (p. 44). PGE implementa lo stesso pattern via `VoiceManager` + `PitchController`: ogni voce ha `pitch_offset` indipendente, e `StochasticPitchStrategy` può scegliere offset random per-grano. Il vincolo armonico discreto di Truax (`N` intero) è sostituito in PGE da pitch_ratio continuo via cents/Hz.

4. **Modalità fixed-sample = caso base di PGE.** Truax distingue fixed-sample (≤4032 campioni in memoria, accesso libero al buffer) e continuous-sample (streaming da disco con finestra mobile). PGE implementa solo la prima — buffer audio caricato interamente, posizione di lettura libera nel range `[loop_start, loop_end]` — coerente con il paradigma deferred-time. Il continuous-sample con finestra mobile è uno dei limiti del real-time del 1994 che PGE non eredita.

## Collegamento alla tesi centrale

Truax 1994 fornisce la **formulazione esplicita della separazione micro/macro come tesi psicoacustica abilitante** del paradigma granulare: "by linking frequency and time at the micro level, granulation makes it possible to treat these two variables independently at the macro level" (p. 44). Per la tesi del paper questa separazione è la condizione strutturale che rende necessario il loop lungo: il compositore non può specificare grano per grano (impraticabile e percettivamente irrilevante), deve lavorare a livello di intenzione parametrica e leggere il risultato emergente. PGE materializza esattamente questo: il YAML opera al livello "presets/ramps" della gerarchia Truax (cioè il livello dove il controllo è praticabile), la partitura grafica rende leggibile l'overlay risultante.

Truax 1994 è anche fonte primaria per due dei tre contributi del paper:

1. **Secondo contributo (partitura, asse Y = posizione buffer).** Il **variable-rate granulation** (ratio off:on come time-extension factor) è il meccanismo descritto a parole: la testina di lettura nel buffer si muove rispetto al tempo di output. L'asse Y della partitura PGE è la rappresentazione esplicita di quel meccanismo come traiettoria visibile.

2. **Primo contributo (DSL espressivo).** L'**harmonization scheme** F=4 con N indipendente per voce è il precedente del multi-voice di PGE (`VoiceManager` + `PitchController`); PGE generalizza con pitch_offset continuo e quattro assi indipendenti.

PGE eredita la modalità fixed-sample; continuous-sample resta fuori scope (richiede ingresso real-time).

## Sezioni del paper CIM 2026 dove citare
- **Sezione 1 (Introduzione)**: postura real-time di Truax come polo opposto del loop lungo (insieme a Truax 1988/1990); "magnification" come accenno alla pratica compositiva di Truax
- **Sezione 2 (Sintesi granulare: dal paradigma Gabor al controllo gerarchico)**: separazione micro/macro come tesi psicoacustica abilitante (quote p. 44); variable-rate granulation; harmonization scheme F=4
- **Sezione 4 (Partitura grafica)**: asse Y PGE come visualizzazione esplicita del meccanismo TEF descritto a parole da Truax
- **Sezione 5 (Caso compositivo)**: precedenti compositivi (Wings of Nike, Pacific, Dominion, Basilica) come termine di confronto per la postura compositiva del brano realizzato con PGE

## Quote chiave
- "this process has the effect that micro-level waveform patterns and macro-level temporal changes have been effectively separated." (p. 41) — fonte primaria della separazione micro/macro
- "By linking frequency and time at the micro level, granulation makes it possible to treat these two variables independently at the macro level" (p. 44) — formulazione esplicita della conseguenza compositiva del paradigma Gabor
- "Time stretching is a unique way to bring out the inner complexity of a sound." (p. 45) — giustificazione estetica del time-shifting
- "Granulation is clearly situated in a different psychoacoustic domain than that occupied by most computer music, which commonly is based in instrumental music concepts." (p. 48) — posizionamento del paradigma rispetto alla tradizione computer-music
- "Deterministic control by predetermined values would be burdensome for both the user and the computer. The simplest solution... is to adopt a stochastic model in which the user specifies the average or minimum value of the control variable and a range within which individual parameter choices may randomly be made." (p. 40) — eco di Truax 1990 sul controllo gerarchico, applicato al livello implementativo (range stocastico per-grano)
