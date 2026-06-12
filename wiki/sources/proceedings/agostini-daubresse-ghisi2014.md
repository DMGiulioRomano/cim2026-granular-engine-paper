# [Agostini, Daubresse, Ghisi, 2014] Cage: una libreria di alto livello per la composizione assistita da computer in tempo reale

## Citazione CIM

Agostini, A., Daubresse, É., Ghisi, D. (2014). Cage: una libreria di alto livello per la composizione assistita da computer in tempo reale. In *Atti del XX Colloquio di Informatica Musicale*, pp. 17–22. Roma: AIMI.

## Categoria e lunghezza

Comunicazione orale — 6 pagine — 13 refs. Versione italiana di Agostini-Daubresse-Ghisi *cage: a high-level library for real-time computer-aided composition*, ICMC 2014 Athens (ref [1]).

## Argomento centrale

Introduzione a **cage**, libreria Max alpha di moduli alto-livello per la composizione assistita da computer (CAC). Costruita sopra **bach** (libreria di ~200 oggetti per dati simbolici musicali via `llll`, *Lisp-like linked list*, struttura ad albero). Tutti i moduli sono astrazioni Max ispezionabili e modificabili (connotazione pedagogica esplicita).

## Sistema o strumento descritto

Libreria **cage** (2014, alpha) per Max 6, basata su bach (Agostini-Ghisi). Famiglie di moduli: (1) generazione altezze (`cage.scale`, `cage.arpeggio`, `cage.harmser`, `cage.noterandom`, `cage.notewalk`); (2) profili melodici (`cage.profile.gen/stretch/mirror/snap/rectify/perturb/filter` su modello libreria Profile di Patchwork/OpenMusic); (3) **processi ispirati da pratiche elettroacustiche** simboliche (`cage.freqshift`, `cage.pitchshift`, `cage.rm`, `cage.fm` su modello Esquisse OpenMusic, `cage.virtfun`, `cage.delay`, `cage.looper`, `cage.cascade~`, `cage.pitchfilter`, **`cage.granulate`** motore di granulazione **simbolica**); (4) interpolazione armonica/ritmica + agogica (`cage.chordinterp`, `cage.rhythminterp`, `cage.timewarp`, `cage.accrall`); (5) automi cellulari + L-sistemi (`cage.chain`, `cage.life`, `cage.lombricus`); (6) set theory (`cage.chroma.topcset/frompcset/tocentroid/fromcentroid`); (7) trattamento partiture (`cage.rollinterp`, `cage.envelopes`, `cage.scissors`, `cage.glue`, `cage.ezptrack`); (8) supporto SDIF (lettura/scrittura partial tracking, frequenze fondamentali, marker via `cage.sdif.*`); (9) rendering audio essenziale (`cage.ezaddsynth~` additivo + `cage.ezseq~` campionatore). **Real-time simbolico**: i moduli operano su `bach.roll`/`bach.score` (rappresentazione partitura) durante l'editing, non su buffer audio. Lambda loop (configurazione feedback simbolico via outlet/inlet dedicato) come meccanismo di personalizzazione del comportamento (analogo concettuale al `for`-each con callback su dati simbolici).

## Analogia con PGE

**Anti-analogia ontologica forte — apre asse argomentativo nuovo nella tradizione CIM.** Prima occorrenza CIM di *granulazione simbolica* come categoria distinta da *granulazione audio*. Quattro vettori:

1. **`cage.granulate` vs PGE Stream — stesso vocabolario, oggetti incompatibili.** Quote p. 19: «*cage.granulate è un motore di granulazione simbolica. I parametri della granulazione sono gli stessi del corrispondente processo elettroacustico: l'intervallo di tempo tra due grani, la durata di ogni grano, la regione di partitura da cui i grani devono essere estratti. L'altezza e la durata dei singoli grani può essere modificata. Basandosi su questi parametri, cage.granulate riempie in tempo reale un oggetto bach.roll collegato al suo outlet.*» — i tre parametri (IOT fra grani, durata grano, regione sorgente) sono identici al canone Roads/Truax/PGE, **ma il "grano" è una nota simbolica con altezza e durata MIDI, non una porzione di campioni audio**. PGE granula buffer (campioni); CAGE granula `bach.roll` (sequenze di note). Categoria *granulazione* applicata a due ontologie disgiunte. Argomento di Sezione 2 paper CIM 2026: la categoria *granulare* nella tradizione CIM include anche il piano simbolico — il paper si delimita esplicitamente al piano *audio sample-based* (canone Roads/Truax).

2. **Real-time symbolic vs deferred audio.** CAGE opera real-time perché manipola entità simboliche (note discrete) il cui ritmo di aggiornamento è dell'ordine del macro-evento musicale (≪ 1 kHz). PGE opera offline perché manipola campioni audio (44/48 kHz) in stream multipli con cache SHA-256. Le due scelte non sono comparabili sull'asse real-time/deferred: la posta in gioco computazionale è di tre ordini di grandezza diversa. Argomento utile per Sezione 1 paper CIM 2026: chiarire che la *narrazione tre atti* (hardware constraint → real-time disponibile → ritorno volontario deferred) riguarda il piano audio, non quello simbolico.

3. **DSL vs libreria di astrazioni Max.** CAGE come bach realizza la *vocazione pedagogica* via astrazioni Max ispezionabili (p. 17 *"tutti i moduli sono astrazioni, che si prestano quindi ad essere facilmente analizzate e modificate"*); PGE realizza la stessa via DSL testuale + Language Server. Convergenza di obiettivo (rendere modificabili gli strumenti compositivi dell'utente) per via tecnologica opposta (patch grafica modificabile vs testo dichiarativo con scaffolding LSP). Argomento per Sezione 3 paper.

4. **Lambda loop CAGE come precursore concettuale debole di `ProbabilityGate` / strategie PGE.** Lambda loop (p. 18 nota 5): outlet `lambda` fornisce dati al campo applicativo dell'utente; risultato re-immesso in inlet dedicato → callback simbolico parametrizzabile per ordinamento, filtraggio, sostituzione. Pattern analogo al modo in cui PGE configura strategie di variazione parametriche via Envelope + ProbabilityGate dichiarate nel YAML. Non precursore architetturale diretto (CAGE = runtime Max, PGE = parser + IR Python), ma stesso *pattern compositivo*: la decisione locale per-grano/per-nota è esposta come funzione configurabile dall'utente.

## Posizionamento storico

Lineage **CAC OpenMusic/PatchWork → bach/cage Max** dichiarato esplicitamente: cage.profile family ispirata a libreria Profile di Patchwork [4]; cage.rm/cage.fm a libreria Esquisse OpenMusic [5,6]; cage = «*composition assistée Genève*» (sez. 4) come acronimo che riconosce supporto HES-SO Ginevra. Filiazione CIM-internal: bach (Agostini-Ghisi ICMC 2012 [2], CIM/SMC 2013 [3]) → cage 2014 → continuità in pubblicazioni successive ICMC/CIM. Distinto dal lineage CIM granulare-audio (Roads/Truax/Di Scipio) e dal lineage CIM concatenative ([[markidisfernandez2016]]): CAGE è **CAC simbolica real-time**, terza famiglia.

## Note stilistiche

6 pagine, 13 refs ben distribuite: 6 self-references gruppo (bach/cage in ICMC/SMC 2010-2013), 3 lineage CAC francese (Profile + Esquisse Patchwork/OpenMusic), 2 set theory (Harte-Sandler, Lerdahl), 2 SDIF (Wright). Densità citazionale: ~2.2 ref/pp. — sotto soglia tipica CIM ma giustificata da natura introduttiva del paper (versione italiana di pubblicazione ICMC parallela). Tono **descrittivo enciclopedico**: sezione 3 catalogo famiglia per famiglia di moduli (no narrazione argomentativa). Figure: 5 figure tutte screenshot di patch Max + bach.roll output. Apertura motivazionale (sez. 2 «Un approccio in tempo reale alla composizione assistita da computer») che enuncia tesi sul ruolo del real-time nella composizione simbolica come polo del paradigma `bach`. Chiusura (sez. 4 Ringraziamenti): nessuna sezione conclusioni argomentativa — il paper rimane descrittivo. **Modello stilistico CIM da non imitare** per CIM 2026 paper PGE (che deve restare argomentativo, non catalogo).

## Sezioni del paper CIM 2026 dove citare

Fonte non citata nel paper attuale; cfr. [[mappa-citazioni-paper]].

## Quote chiave

> *cage.granulate è un motore di granulazione simbolica. I parametri della granulazione sono gli stessi del corrispondente processo elettroacustico: l'intervallo di tempo tra due grani, la durata di ogni grano, la regione di partitura da cui i grani devono essere estratti. L'altezza e la durata dei singoli grani può essere modificata. Basandosi su questi parametri, cage.granulate riempie in tempo reale un oggetto bach.roll collegato al suo outlet.* (p. 19, sez. 3.3)

> *Il paradigma del tempo reale influenza profondamente la natura stessa del processo compositivo. [...] compositori che lavorano con dati simbolici potrebbero volere che il computer si adatti nel più breve tempo possibile alla nuova configurazione di dati. Il paradigma che soggiace a cage è lo stesso che ha improntato la libreria bach: creare e modificare dati simbolici non è necessariamente un'attività fuori dal tempo, ma segue il flusso temporale compositivo, e si adatta ad esso.* (p. 18, sez. 2)

> *tutti i moduli della libreria sono astrazioni, che si prestano quindi ad essere facilmente analizzate e modificate. Non è difficile, per l'utilizzatore che voglia imparare a trattare i dati musicali, copiare, modificare o ritoccare le patch per le proprie necessità. In quest'ottica, tutti gli oggetti della libreria sono intrinsecamente open source.* (p. 17, sez. 1)
