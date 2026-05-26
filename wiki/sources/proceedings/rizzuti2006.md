# [Rizzuti, 2006] Il "caos sonoro": studi preliminari per la realizzazione di un sistema di sintesi granulare controllato mediante iterazione di funzioni non lineari

## Citazione CIM
Rizzuti, C. (2006). Il "caos sonoro": studi preliminari per la realizzazione di un sistema di sintesi granulare controllato mediante iterazione di funzioni non lineari. In *Atti del XVI Colloquio di Informatica Musicale*. Genova: AIMI / InfoMus Lab — DIST Università di Genova.

## Categoria e lunghezza
Comunicazione orale — abstract esteso ~1.5 pagine — 4 riferimenti bibliografici. Formato breve, senza sezioni numerate, senza figure, senza equazioni numerate (una sola equazione inline, la mappa logistica).

## Argomento centrale
Sistema di sintesi granulare asincrona in cui tutti i parametri di controllo (ampiezza, durata, istante d'attacco dei grani; frequenze delle parziali armoniche/inarmoniche) sono guidati in modo deterministico dall'iterazione di una mappa logistica del tipo `xt+1 = c·xt·(2 − xt)` con `c ∈ [0, 2]`. Posizione esplicita: rifiutare l'impiego di generatori di numeri casuali, sostituendoli con la varietà e l'imprevedibilità prodotte dal regime caotico delle funzioni non-lineari.

## Sistema o strumento descritto
Implementazione **CSound**, **offline**. Architettura a due strumenti:
1. **Strumento generatore di eventi**: riceve istruzioni dalla partitura, genera eventi sonori secondo l'iterazione caotica.
2. **Strumento generatore di grani**: riceve direttive dal primo strumento e dalla partitura, produce i grani sonori.
Pipeline: `partitura CSound → strumento eventi → strumento grani → audio`.

Nota: la formula riportata (`xt+1 = c·xt·(2 − xt)` con `c ∈ [0, 2]`) è una variante della logistica classica `xt+1 = c·xt·(1 − xt)` con `c ∈ [0, 4]`. Comportamento qualitativo equivalente (convergenza → periodicità → caos al variare di `c`).

## Analogia con PGE

**Stessa famiglia di controllo di Di Scipio 1991, anti-precursore PGE.** Rizzuti 2006 è il secondo data-point CIM di **controllo caotico-iterativo** dei parametri di grano (`xn → xn+1`, traiettoria deterministica). PGE adotta la famiglia opposta — **tendency mask statistico** (Envelope center + range, distribuzione campionata uniforme/gaussiana, indipendenza fra grani; cfr. [[tendency-mask]]). I due regimi non sono varianti dello stesso pattern. Stessa analisi già fatta per [[discipio1991]]: Rizzuti 2006 conferma che la famiglia caotico-iterativa ha radici CIM ricorrenti, non è episodio isolato di Di Scipio 1991. Inquadramento d'insieme del filone (sotto-famiglie A caotico-iterativo + B combinatoria MUX) in [[granulare-deterministico-cim]].

**Architettura a due strumenti CSound come analogia di principio, non di struttura.** L'architettura `strumento eventi → strumento grani` separa due livelli di responsabilità (generazione del flusso vs sintesi del grano) e prefigura per principio la separazione Stream/Voice di PGE. Differenze sostanziali:
- Rizzuti codifica controllo e parametri **direttamente nella partitura CSound**, in linguaggio score Csound, senza livello intermedio (no DSL above).
- PGE separa il livello di specifica (YAML come DSL/IR, [[parameter-orchestrator]]) dal livello di rendering ([[renderer]] CSound/NumPy), con `ParameterOrchestrator` che valuta tendency mask prima della scrittura del .sco.

In termini di precedenza architetturale, Rizzuti 2006 è **meno diretto** di Arcella-Silvestri 2012 (vedi [[arcella-silvestri2012]]): Arcella-Silvestri ha la fattorizzazione esplicita `score.cpp C++ → Xscore.txt → Analogique.csd` (due moduli con linguaggi distinti), Rizzuti tiene tutto dentro CSound.

## Posizionamento storico

Filone CIM **offline / deferred time / controllo algoritmico parametri granulari**.
- **1985 Roads** — primo paper CIM su granular synthesis, problema `d·n` (vedi [[roads1985]]).
- **1988 De Poli, Piccialli** — sintesi granulare sincrona offline (formantica, vedi [[depolipiccialli1988]]).
- **1991 Di Scipio** — prima formulazione CIM del controllo caotico-iterativo (logistica, Verhulst, Hénon; vedi [[discipio1991]]).
- **2006 Rizzuti (questo paper)** — riprende la linea caotico-iterativa di Di Scipio 1991, la restringe alla sola logistica e ne fa il principio architetturale (deterministico **invece di** stocastico). 15 anni dopo Di Scipio, in piena disponibilità real-time CIM (Lippe 1993, ISPW; PulsarGenerator 2001) Rizzuti rivendica esplicitamente l'**offline + deterministico** come scelta metodologica. Postura affine — ma non identica — al ritorno volontario al deferred time di PGE.
- **2012 Arcella, Silvestri** — ricostruzione Xenakis offline, fattorizzazione `C++ → CSound` (vedi [[arcella-silvestri2012]]).

## Note stilistiche

- **Formato**: comunicazione breve in stile abstract esteso (no abstract separato, no sezioni numerate, no figure). Una sola equazione inline. Apertura tematica ("Il presente lavoro nasce dalla volontà…"), chiusura procedurale ("Si provvederà ad illustrare…"). Niente conclusioni, niente discussione dei risultati.
- **Densità citazioni**: 4 riferimenti — due divulgativi su caos (Nina Hall, Gleick), uno su modelli matematici/linguaggi/musica (Bertacchini-Bilotta-Pantano), uno su computer music (Dodge-Jerse). Bassa densità tecnica, niente Roads/Truax/De Poli citati per la parte granular: posizionamento storico-CIM mancante. **Non adoperabile come modello stilistico per il paper CIM 2026** (densità troppo bassa, scope troppo locale).
- **Tono**: descrittivo, non argomentativo. Espone la scelta deterministica come preferenza personale ("In questo lavoro si è adottato un approccio piuttosto differente dal solito") senza confronto puntuale con la letteratura.

## Sezioni del paper CIM 2026 dove citare

- **Sezione 2 (Sintesi granulare)**: secondo data-point CIM del filone caotico-iterativo dopo Di Scipio 1991. Citabile in nota a piè di pagina o in riferimento parentetico per documentare che la linea "controllo deterministico non-lineare" è ricorrente nella tradizione CIM offline, non episodio isolato. Non meritevole di trattazione propria nel corpo del testo (densità tecnica del paper troppo bassa, scope limitato a logistica monoparametrica).

## Quote chiave

Nota: gli Atti CIM XVI 2006 non riportano numeri di pagina stampati. Riferimenti dati come pagina del PDF (`atti PDF p. N`) del file `raw/proceedings/2006_CIM_XVI_Atti.pdf`. L'abstract esteso di Rizzuti occupa PDF pp. 20–21.

- (atti PDF p. 20) *"Si è scelto, al contrario, di controllare tutti i parametri e le grandezze in maniera deterministica mediante ferree relazioni matematiche; soltanto il manifestarsi del comportamento caotico delle funzioni non lineari consente di introdurre varietà e imprevedibilità all'interno del materiale sonoro."* — formulazione esplicita della scelta caotico-iterativa **contro** il controllo stocastico, opposta alla tendency mask PGE. Citabile come testimonianza CIM diretta della famiglia di controllo che PGE non adotta.
- (atti PDF p. 21) *"L'implementazione di questo sistema di sintesi granulare asincrona è stata realizzata in CSound; sono stati creati due differenti strumenti: uno realizza la generazione degli eventi sonori secondo le istruzioni fornite in partitura, l'altro provvede ad effettuare la generazione dei grani sonori secondo le direttive fornite dal primo strumento e dalla partitura."* — descrizione canonica dell'architettura a due strumenti CSound; precursore CIM (debole) della separazione Stream/grano PGE, senza il livello DSL/IR sopra.
