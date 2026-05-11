# [Roads, 2001] Microsound — pagina hub

## Citazione CIM
Roads, C. (2001). *Microsound*. Cambridge, MA: The MIT Press. ISBN 0-262-18215-7. 409 pp.

## Stato ingest

Roads 2001 è il testo di riferimento centrale del paper CIM. Ingestione per capitolo. Pagine specifiche:

| Capitolo | Pagine libro | File wiki | Stato |
|----------|--------------|-----------|-------|
| 1. Time Scales of Music | 1–42 | [roads2001-ch01-time-scales.md](roads2001-ch01-time-scales.md) | ✓ |
| 2. The History of Microsound from Antiquity to the Analog Era | 43–84 | [roads2001-ch02-history-microsound.md](roads2001-ch02-history-microsound.md) | ✓ |
| 3. Granular Synthesis | 85–118 | [roads2001-ch03-granular-synthesis.md](roads2001-ch03-granular-synthesis.md) | ✓ |
| 4. Varieties of Particle Synthesis | 119–178 | [roads2001-ch04-particle-synthesis.md](roads2001-ch04-particle-synthesis.md) | ✓ |
| 5. Transformation of Microsound | 179–234 | [roads2001-ch05-transformation.md](roads2001-ch05-transformation.md) | ✓ |
| 6. Windowed Analysis and Transformation | 235–300 | [roads2001-ch06-windowed-analysis.md](roads2001-ch06-windowed-analysis.md) | ✓ |
| 7. Microsound in Composition | 301–324 | [roads2001-ch07-composition.md](roads2001-ch07-composition.md) | ✓ |
| 8. Aesthetics of Composing with Microsound | 325–348 | [roads2001-ch08-aesthetics.md](roads2001-ch08-aesthetics.md) | ✓ |
| 9. Conclusion | 349–352 | [roads2001-ch09-conclusion.md](roads2001-ch09-conclusion.md) | ✓ |
| App. A. The Cloud Generator Program | 383–388 | [roads2001-appA-cloud-generator.md](roads2001-appA-cloud-generator.md) | ✓ |

Tutti i capitoli rilevanti per il paper CIM 2026 sono ingestiti. Bibliography: `Roads2001 | ◐ ch1+ch2+ch3+ch4+ch5+ch6+ch7+ch8+ch9+appA` (= integrale).

## Argomento centrale del libro

*Microsound* è la sintesi argomentativa del lavoro di Roads tra il 1974 (Klang-1, prima granular synthesis digitale) e il 2000 (Cloud Generator, PulsarGenerator, Creatovox). Articola una **tassonomia multi-scala** (9 time scales, cap. 1), una **genealogia storica** del pensiero microsonico (cap. 2), il **catalogo teorico-tecnico** delle tecniche granular e particle synthesis (cap. 3–4), le **trasformazioni microsonore** time-domain e frequency-domain (cap. 5–6), e infine il **versante compositivo ed estetico** (cap. 7–8) con una conclusione programmatica (cap. 9).

Il libro è simultaneamente:
- **Diario di ricerca** personale di Roads (1974–2000): «*Microsound records this first round of experimentation, and thus serves as a diary of research*» (Introduzione, p. viii)
- **Trattato di riferimento** della disciplina granular synthesis nella sua forma matura
- **Manifesto epistemologico**: stabilire il microsuono come dominio compositivo autonomo, con vocabolario proprio, perception model proprio, repertorio proprio

## Tre quote pietra-angolare per il paper CIM

### 1. Loop lungo (cap. 1, p. 10) — pietra angolare assoluta

> «*Composition is itself a supratemporal activity. Its results last only a fraction of the time required for its creation. A composer may spend a year to complete a ten-minute piece. [...] This backtracking is not necessarily time wasted; it is part of an important feedback loop in which the composer refines the work. [...] Compare all this with the efficiency of the real-time improviser!*»

Roads, scrivendo nel 2001 quando il real-time è già disponibile da 13 anni (Truax 1988), riabilita esplicitamente il **backtracking iterativo** come feedback loop costitutivo della composizione. PGE = realizzazione tecnica contemporanea di questa postura.

### 2. DSL musicale (cap. 1, p. 26) — legittimazione del contributo (1)

> «*One can imagine a musical interface in which a musician specifies the desired sonic result in a musically descriptive language which would then be translated into particle parameters and rendered into sound.*»

Programma DSL articolato esplicitamente da Roads. PGE YAML + Language Server = materializzazione.

### 3. Interfacce dichiarative (cap. 5, p. 234) — legittimazione architetturale

> «*Circuit speed is less of a limiting factor, but no matter how fast computers become, certain transformations will always be too difficult for a human being to manipulate effectively in real time (Vaggione 1996c). Musical interfaces that offer control through envelopes, presets, and other automation functions will assist composers in planning detailed and elaborate transformations.*»

Roads/Vaggione dichiarano nel 2001 che velocità ≠ usabilità compositiva. Per trasformazioni microsonore complesse servono interfacce dichiarative. PGE = realizzazione di questo principio.

## Mappa capitoli → contributi PGE

| Contributo PGE | Capitoli Roads 2001 chiave |
|----------------|----------------------------|
| (Cornice) Tesi loop lungo | ch1 (p. 10), ch5 (p. 234), ch9 (heuristic composition) |
| (1) YAML DSL + PGE-ls | ch1 (p. 26 DSL); ch5 (p. 185 micromontage by algorithmic process) |
| (2) Partitura grafica asse Y = posizione-buffer | ch1 (cornice multi-scala); ch3 (parametri granulari); ch8 (estetica multi-scala) |
| (3) STEMS workflow | ch1 (p. 41 sound mixing program); ch5 (delimitazione scope: convoluzione/spatialization delegati a DAW); appA (Cloud Generator come tool single-output, PGE estende a multi-stream) |
| Differenziatore frame rate per-voice | ch2 (pp. 67–68 critique constant microtime grid); ch3 (parametri time-varying); ch5 (granulation parameters list) |
| Posizionamento storico (terzo atto) | ch2 (genealogia antiquo→analogico); ch7 (composizioni Roads); ch9 (proiezione real-time virtuosistico) |
| Razionale teorico grano gaussiano | ch1 (Gabor); ch2 (Gabor matrix); ch6 (Gabor transform) |

## Capitoli per sezione del paper CIM 2026

- **Sezione 1 (Introduzione).** ch1 (loop lungo p. 10) + ch2 (Schaeffer p. 44 «*musical ideas are prisoners of musical devices*») + ch9 (proiezione real-time del 2001 da cui PGE 2026 bifurca).
- **Sezione 2 (Sintesi granulare).** ch2 (genealogia completa) + ch3 (teoria GS + sei organizzazioni globali + implementazioni storiche) + ch4 (varieties of particle synthesis) + ch6 (cornice teorica Gabor opzionale).
- **Sezione 3 (Architettura PGE).** ch1 (p. 26 DSL) + ch5 (p. 185 micromontage by algorithmic process; p. 188 granulation parameters list; p. 234 envelopes+presets+automation) + ch3 (anatomy of grain).
- **Sezione 4 (Partitura grafica).** ch1 (cornice multi-scala; p. 28 heterogeneity in sound particles) + ch3 (parametri visibili) + ch8 (estetica multi-scala) + appA (Cloud Generator GUI come precursore single-pane).
- **Sezione 5 (Caso compositivo).** ch7 (composizioni di Roads: nscor, Field, Clang-Tint, Half-life, Tenth/Eleventh vortex; analisi compositiva di Truax e Vaggione) + ch8 (estetica).
- **Sezione 6 (Conclusioni).** ch5 (p. 234) + ch9 (predizioni + composizione euristica) + ch1 (p. 41 sound mixing program for macroform).

## Posizionamento del paper CIM rispetto a Roads 2001

Il paper non *aggiunge* sostanza tecnica a Roads 2001: il dominio è canonicamente trattato. Il paper *afferma* una **postura compositiva** specifica entro quel dominio canonico, e mostra come una scelta architetturale (YAML DSL + deferred + STEMS) la materializzi.

Tre mosse argomentative principali:

1. **Riprendere il loop lungo (cap. 1 p. 10) come tesi guida.** Roads stesso articola il backtracking come feedback loop costitutivo. Il paper CIM non ha bisogno di inventare la tesi: la cita e la rilancia mostrando che oggi è una *scelta consapevole*, non un vincolo hardware.

2. **Adempiere il programma DSL (cap. 1 p. 26 + cap. 5 p. 185 + cap. 5 p. 234).** Roads articola in tre punti distinti del libro il programma di un'interfaccia compositiva dichiarativa. PGE YAML + Language Server è la sua realizzazione contemporanea integrata e validata semanticamente.

3. **Risolvere il problema del frame rate costante (cap. 2 pp. 67–68).** Roads identifica esplicitamente il limite estetico delle screens Xenakis con durata grano uniforme. PGE supera via ParameterOrchestrator + Envelope time-varying per-voice + dephase per-grain.

## Note metodologiche

- Roads 2001 cita raramente l'idea di *postura compositiva* come scelta vs vincolo. La sua narrazione è progressista-tecnologica: ogni avanzamento (real-time, micro-time domain, virtuoso interface) come miglioramento. Il paper CIM **eredita la sostanza** del libro ma **rovescia la direzione** sul punto specifico della temporalità del processo compositivo.
- Roads tratta PSGS, Pulsar, glisson, trainlet, grainlet come *varietà* di particle synthesis (cap. 4). PGE *non* implementa pulsar synthesis o pitch-synchronous granular: si limita a sample-based granular con asynchronous/synchronous control. Delimitazione esplicita.
- Roads non scrive un manuale di workflow: il libro è argomentativo-tecnico, non procedurale. Il paper CIM eredita questo tono (argomentativo, non descrittivo).

## Quote ricorrenti utili

- Schaeffer p. 44: *«Musical ideas are prisoners of musical devices»*
- Mallat p. 238 (cap. 6): *«The world of transients is considerably larger and more complex than the garden of stationary signals»*
- Wishart p. 233 (cap. 5): *«Our principal metaphor for musical composition must change from one of architecture to one of chemistry»*
- Truax 1994a p. 192 (cap. 5): *«Granulation may be many things, but it is not omniscient»*
- Hugo p. 299 (cap. 6): *«Where the telescope ends, the microscope begins. Which has the grander view?»*

## Cross-reference dentro la wiki

- Cornice multi-scala: vedi anche `wiki/concepts/` se creato.
- Tesi loop lungo: `wiki/overview.md` sezione «Tesi corrente».
- Cloud Generator come precursore single-stream di STEMS: `roads2001-appA-cloud-generator.md`.
- Roads 2006 (Xenakis Symposium) come continuazione: introduce *study scores for electronic music* come categoria notazionale (rilevante per Sezione 4 PGE).
- Roads 2021 (EmissionControl2) come polo opposto: real-time per-grain GUI vs declarative deferred YAML.
