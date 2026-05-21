# [Sparano, 2018] GrainLab — Software open source per la sintesi granulare quasi-sincrona

## Citazione CIM
Sparano, G. (2018). GrainLab — Software open source per la sintesi granulare quasi-sincrona. In *Atti del XXII Colloquio di Informatica Musicale*, pp. 243–245. Udine, 20-23 Novembre 2018.

## Categoria e lunghezza
Comunicazione orale — 3 pagine (pp. 243–245) — 7 riferimenti, 4 figure (schemi a blocchi + esempio sfasamento rampa).

## Argomento centrale
Presentazione di **GrainLab**, granulatore quasi-sincrono real-time in Max/MSP basato su linee di ritardo finestrate. Implementato sfruttando Gen (Cycling'74, 2011) per processing a campione. Open source, gratuito. Architettura: un singolo segnale rampa di sincronizzazione globale pilota N grani polifonici tramite sfasamenti deterministici (preset *continuous*/*rhythmic*) o aleatori; finestratura su buffer 512 campioni con 6 funzioni base (Hann, Expodec, Rexpodec, Triangle, Trapezoid, Sinc) in 9 preset (i preset 7–9 sono combinazioni: preset 7 = rotazione di tutte le 6 finestre su gruppi di 6 grani successivi, preset 8 = alternanza Expodec/Rexpodec, preset 9 = alternanza Hann/Sinc); densità via duty cycle del segnale rampa; trasposizione +/− ottava, panning e ampiezze per-grano via tabelle. Cambio parametri click-free grazie a Sample&Hold sincronizzato a fase 0. Caso d'uso: *FENIX DNA* di Fabrizio Plessi (Teatro La Fenice, luglio-agosto 2017) — 5 istanze GrainLab, una per ogni strumento (flauto, cl. basso, viola, pianoforte, soprano) + 4 delay spettrali + spazializzazione multicanale.

## Sistema o strumento descritto
GrainLab — granulatore quasi-sincrono Max/MSP+Gen, real-time, stereo, 2018. Distribuito su http://www.giovannisparano.it/attivita/maxmsp.php.

## Analogia con PGE
**Nessuna analogia architetturale diretta**. GrainLab è polo opposto di PGE su entrambi gli assi:
- **Tempo**: real-time per live electronics da partitura strumentale; PGE deferred per loop lungo compositivo.
- **Architettura**: patch Max/MSP+Gen monolitica senza separazione DSL/IR/renderer; PGE pipeline YAML → IR Python → backend Csound/NumPy.

Una analogia puntuale, non strutturale: GrainLab implementa un **catalogo di 6 finestre in 9 preset** (Hann, Expodec, Rexpodec, Triangle, Trapezoid, Sinc + 1 rotazione + 2 alternanze) come asset compositivo discreto; PGE oggi ha `Grain` con envelope Hann hard-coded — Sparano documenta che il *catalogo finestre* è una decisione compositiva di prima classe (Expodec/Rexpodec come finestre direzionali per attack/release asimmetrici). Non rilevante per il paper CIM ma annotato come *future work* potenziale.

## Posizionamento storico
**Polo real-time italiano CIM post-2000**, opposto al ramo offline Di Scipio 1991 / Arcella-Silvestri 2012 / PGE. Membri stretti del polo *granulare* real-time italiano post-2000: Sparano 2018 (questo paper). Membri allargati del polo *real-time italiano post-2000* per tecniche affini ma non granulari in senso stretto: Markidis/Fernández 2016 (analisi+sintesi real-time con riconoscimento timbrico, da verificare in dettaglio), Pozzi 2016 (Boids su concatenative, non granulare), Cera et al. 2022 (interactive sonification del gesto, non granulare), Markidis 2024 (ecosystemic mediation, non specificamente granulare). La continuità è temporale e di paradigma (real-time, ambiente Max/MSP o Pure Data, granulatore o equivalente come elemento di un sistema più ampio), non tecnica. Sparano è data-point isolato del *granulare* real-time italiano post-2000 nel survey CIM.

GrainLab è specificamente il sotto-tipo **quasi-sincrono** (cita Roads *Computer Music Tutorial* 1996 come fonte teorica) — distribuzione IOT deterministica via fasi del segnale rampa, non stocastica via density probabilistica come Truax/PGE. Anti-precursore del [[density-controller]] PGE (stessa funzione, modello opposto: deterministico fase-based vs stocastico density-based).

## Note stilistiche
- **Struttura**: 4 sezioni numerate (Introduzione → Implementazione → Conclusioni → Bibliografia). Implementazione divisa in 6 sotto-sezioni (Schema generale, Polifonia/sincronizzazione, Lettura/finestratura, Densità, Trasposizione/panning/ampiezze, Gestione parametri).
- **Tono**: descrittivo-implementativo, nessuna postura argomentativa. Apertura con genealogia canonica granulare (Gabor → Xenakis → Roads → Truax → *Riverrun*); chiusura con uso compositivo concreto + sviluppi futuri (multicanale, finestre estese, sorgente preregistrata).
- **Densità citazioni**: 7 ref totali, **6 fonti core granulari** (Gabor 1947, Xenakis *Formalized Music*, Roads *Introduction to GS* CMJ 1988, Truax *Real-Time GS DSP* CMJ 1988, Roads *Computer Music Tutorial* 1996, Roads *Microsound* 2001) + cycling74.com. Niente Truax 1990/1994, niente Vaggione, niente De Poli/Piccialli — **bibliografia minima canone CIM granulare 2018**.
- **Figure**: 4 schemi a blocchi (Schema generale, sfasamento rampa multi-grano, algoritmo densità, gestione parametri) + formule chiuse (sinc, Hann, Expodec). Niente partiture grafiche, niente score visualizer.
- **Apertura**: una sola frase sulla teoria (Gabor 1947) prima di passare alla descrizione tecnica del software.
- **Chiusura**: sviluppi futuri in 3 punti pratici (multicanale + finestre + sorgente preregistrata). Niente riflessione metodologica.

**Modello per CIM 2026 — distanza esplicita**: paper tecnico-implementativo da 3 pp con 7 ref è il polo *minimale* della venue. PGE paper non può adottare questo stile (target 6-8 pp, postura argomentativa, 9-21 ref). Tuttavia conferma che 3 pp + bibliografia minima è una struttura accettata in CIM per tool descriptions — utile come limite inferiore di densità citazionale.

## Sezioni del paper CIM 2026 dove citare
- **Sezione 2** (Sintesi granulare): citazione minore come data-point CIM italiano del polo real-time quasi-sincrono opposto a PGE; data-point isolato del *granulare* real-time italiano CIM post-2000 nel survey, accompagnato (per tecniche affini ma non strettamente granulari) da Markidis/Fernández 2016, Pozzi 2016, Cera et al. 2022, Markidis 2024.
- **Sezione 3** (Architettura): riferimento contrastivo per `DensityController` come scelta esplicita (Truax-stocastico density-based) rispetto all'alternativa CIM contemporanea quasi-sincrona deterministica fase-based di GrainLab; ancoraggio CIM dell'asse stocastico/deterministico del controllo IOT.
