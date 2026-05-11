# [Di Scipio, 1994] Micro-time sonic design and timbre formation

## Citazione CIM
Di Scipio, A. (1994). Micro-time sonic design and timbre formation. *Contemporary Music Review*, 10(2), 135–148.

## Argomento centrale
Il paper teorizza la "micro-time sonic design" come modalità compositiva in cui il timbro *è* forma: i processi micro-strutturali discreti del suono (granulazione, funzioni non-lineari iterate) producono proprietà macro-strutturali emergenti, dissolvendo la distinzione classica tra materiale sonoro e forma musicale. Introduce il concetto di *models of detailed sonic design* — modelli indeterministici in cui la specifica parametrica non prescrive un esito ma apre uno spazio di possibili comportamenti sonori da esplorare.

## Gap o problema identificato
L'approccio "composing-the-sound" (deterministic, dualistic, output pre-immaginato) e "composing-with-sound" (Truax 1990b, real-time feedback) sono trattati come poli opposti. Di Scipio sostiene che la micro-time sonic design supera questa dicotomia: la forma emerge dal processo, non è pre-scritta né puramente reattiva. Il limite rimasto aperto è la mancanza di strumenti di rappresentazione che rendano osservabile questa emergenza durante il ciclo compositivo — il compositore deve fare affidamento sulla propria memoria d'ascolto tra un'iterazione e l'altra.

## Rilevanza diretta per PGE
PGE implementa tecnicamente la postura che Di Scipio 1994 descrive concettualmente:
- Il YAML DSL come specifica di *intenzioni parametriche* (non di singoli grani) è la forma operativa dei "models of detailed sonic design"
- La partitura grafica automatica colma il gap che Di Scipio non risolve: rende visibile l'emergenza micro→macro *tra un ciclo e l'altro*, senza richiedere real-time
- Il ParameterOrchestrator con envelope/gate/strategie stocastiche è l'equivalente strutturale delle funzioni non-lineari iterate di Di Scipio (orbit space → spazio parametrico)
- La cache SHA-256 + solo/mute rende praticabile l'iterazione "osservo → modifico → riascolto" che Di Scipio descrive come necessaria ma non supporta strumentalmente

## Collegamento alla tesi centrale
Di Scipio 1994 fornisce il fondamento teorico della postura del loop lungo *prima* che PGE esista. La sua affermazione che "The design task cannot be accomplished in a goal-driven style of design — at least not before the composer has observed the behavior of the micro-level process extensively enough to predict its outcomes" (p. 8) è la descrizione esatta di ciò che il loop lungo abilita: specifica → generazione → ascolto → riflessione → riscrittura *come spazio necessario* (non come fallback). PGE è la realizzazione tecnica di questa postura nel 2024.

Nota rilevante per la narrativa del paper: Di Scipio opera in *tempo differito* per *kairós* (1991/92, IBM486 home studio, non-real-time) e *Zeitwerk* (1992, mainframe IBM3090 a Padova, ICMS, deferred), ma usa il real-time GSAMX di Truax per *Essai du vide. Schweigen* (1993, Simon Fraser). La postura indeterministica non è quindi vincolata al tempo differito — è vincolata al *ciclo di esplorazione*. Ciò affina la tesi PGE: non è "deferred vs real-time" ma "loop lungo come spazio compositivo vs feedback immediato come paradigma diverso".

## Sezioni del paper CIM 2026 dove citare
- Sezione 2 (Sintesi granulare: dal paradigma Gabor al controllo gerarchico): Di Scipio 1994 come articolazione teorica della postura offline/indeterministica; posizionare dopo Roads 1985/1988 e Truax 1988 come approfondimento compositivo, non solo tecnico
- Sezione 3 (PGE: architettura per l'indagine parametrica): il concetto di "models of detailed sonic design" come cornice teorica in cui il DSL YAML si inscrive

## Quote chiave
- p. 138 (highlighted): "microstructural time modelling of sound. Such strategies imply some model or knowledge of how macro-level properties of musical structure can emerge from micro-level morphological conditions."
- p. 142: "The design task cannot be accomplished in a goal-driven style of design — at least not before the composer has observed the behavior of the micro-level process extensively enough to predict its outcomes. The overall shape of the final sound-object is more *operationalized* than *produced* following a sound image which pre-exists to the composition."
- p. 142: "a *true* exploration must be an indeterministic, open ended experience."
