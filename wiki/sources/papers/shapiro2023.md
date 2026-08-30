# [Shapiro, 2023] MusAssist: A Domain Specific Language for Music Notation

## Citazione CIM
Shapiro, I. (2023). MusAssist: A Domain Specific Language for Music Notation. In *Proceedings of the Eighth International Conference on Technologies for Music Notation and Representation (TENOR 2023)*, pp. 75–82. Boston, MA: Northeastern University.

## Argomento centrale
Presenta MusAssist, un DSL esterno e dichiarativo per la notazione musicale: l'utente scrive specifiche di scale, accordi, cadenze, sequenze armoniche al livello di astrazione delle strutture teoriche; un compilatore Haskell le traduce in MusicXML.

## Gap o problema identificato
Esiste un divario di astrazione tra la teoria musicale occidentale e la scrittura della composizione: serve un linguaggio dichiarativo che permetta di esprimere strutture al livello concettuale e generarne l'espansione notazionale.

## Rilevanza diretta per PGE
Match diretto sull'asse linguaggio/DSL: un DSL esterno e dichiarativo, come il YAML di PGE. Contrasto utile del tipo *fire-and-forget*: MusAssist compila in MusicXML e consegna a un editor per il seguito, **senza** una IR persistente e interrogabile né materializzazione differita governata dal sistema. PGE conserva la specifica come oggetto interrogabile (cfr. [[intermediate-representation]]) e tiene il rendering dentro il proprio ciclo. Stessa forma dichiarativa, diversa permanenza della rappresentazione.

## Collegamento alla tesi centrale
Serve la proposta 1: dà un parente dichiarativo recente contro cui dimensionare la rivendicazione PGE (non «abbiamo inventato il DSL dichiarativo», ma «la specifica resta interrogabile e la materializzazione è differita e governata»).

## Sezioni del paper CIM 2026 dove citare
- `(intro)` (primaria): stato dell'arte sui DSL dichiarativi per notazione/composizione.
- «tradizione» (sezione rimossa, confluita in `sec:conclusioni`) (secondaria): contrasto fire-and-forget (compila-e-consegna) vs IR persistente + differito.

## Quote chiave
- «This paper presents MusAssist, an external, declarative DSL for music notation that closes the abstraction gap between Western music theory and written composition.» (p. 82)
- «MusAssist programs are translated by its Haskell-based compiler to MusicXML, enabling the composition to be loaded into notation software for further manual editing and playback.» (p. 82)

## Note
Cfr. [[intermediate-representation]], [[micromontage]]. Settima referenza TENOR (riserva promossa a core su richiesta).
