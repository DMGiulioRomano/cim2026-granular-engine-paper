# [Truax, 1990] Composing with Real-Time Granular Sound

## Citazione CIM
Truax, B. (1990). Composing with Real-Time Granular Sound. *Perspectives of New Music*, 28(2), 120–134.

## Argomento centrale
Truax descrive la sua esperienza compositiva con la sintesi granulare real-time sul DMX-1000, articolando una gerarchia di controllo a tre livelli (variabili di controllo → preset/ramps → score/tendency masks) che rende praticabile la composizione con migliaia di grani al secondo. Il paper riposiziona il compositore da "arbitro onnisciente" a "sorgente di messaggi di controllo che guidano il processo senza determinarlo direttamente".

## Gap o problema identificato
"It is obviously impossible for the composer to specify each individual grain, given that there may be thousands of them per second. It reduces to absurdity the idea of total control by the composer. Hierarchic levels of control are absolutely necessary." (p. 131)

Il controllo diretto è fisicamente impossibile: la granulare richiede astrazione gerarchica obbligatoria. Il paper non risolve il problema percettivo — descrive come Truax lo ha affrontato nel suo sistema real-time specifico (DMX-1000 + PODX), senza generalizzare a sistemi deferred-time o ambienti basati su notazione.

## Rilevanza diretta per PGE
PGE implementa esattamente la gerarchia di Truax in contesto deferred-time: YAML DSL come "score", ParameterOrchestrator come livello "presets/ramps", StreamConfig come "control variables". Le tendency masks di Truax (forme grafiche di controllo nel tempo) sono l'antecedente diretto del `score_visualizer.py` di PGE, che proietta stream sul piano tempo × posizione-nel-buffer.

## Collegamento alla tesi centrale

Truax 1990 è la formulazione più esplicita della postura compositiva real-time — il polo opposto rispetto a cui PGE si posiziona. Il loop stretto del real-time permette al compositore di essere "source of control messages that guide the overall process without directly determining it": il feedback immediato è il meccanismo che sostituisce la pre-scrittura. PGE non nega questa postura — riconosce che il giudizio drammaturgico del compositore garantisce la non-linearità del processo in entrambi i casi. Cambia la scala temporale: nel real-time il giudizio opera sull'atto immediato, nel tempo differito opera sulla riflessione tra un ciclo e l'altro.

Il gap controllo/percezione ("absurd to specify each grain") rimane il problema condiviso. La risposta di Truax è il loop stretto in real-time. La risposta di PGE è il loop lungo in tempo differito — con la partitura grafica come strumento che rende leggibile ciò che il loop stretto rivela nell'atto e che il loop lungo rivela nella riflessione.

## Sezioni del paper CIM 2026 dove citare

- Sezione 1 (Introduzione): "absurd to specify each grain" come problema condiviso; postura compositiva real-time come il polo rispetto a cui PGE si definisce per differenza (loop stretto vs loop lungo)
- Sezione 2 (Contesto teorico): gerarchia di controllo, figura "Composition Hierarchy"; il compositore come "source of control messages"
- Sezione 4 (Partitura grafica): tendency masks come precursore visivo della partitura PGE


## Quote chiave
- "It is obviously impossible for the composer to specify each individual grain, given that there may be thousands of them per second. It reduces to absurdity the idea of total control by the composer. Hierarchic levels of control are absolutely necessary." (p. 131)
- "the composer functions not as an omniscient arbiter, but as the source of control messages that guide the overall process without directly determining it." (p. 132)
- "The fundamental paradox of granular synthesis—that the enormously rich and powerful textures it produces result from its being based on the most 'trivial' grains of sound" (p. 124)
