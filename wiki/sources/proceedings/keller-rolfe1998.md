# [Keller & Rolfe, 1998] The Corner Effect

## Citazione CIM
Keller, D., & Rolfe, C. (1998). The Corner Effect. In *Atti del XII Colloquio di Informatica Musicale*, pp. 236–239. Gorizia: AIMI.

Nota di identificazione: il survey [[cim-survey]] (sezione *1998 — XII CIM*) attribuiva erroneamente il paper a *"MacPod: real-time granular synthesis for the Macintosh"* di Keller & Truax — errore di OCR/lettura: *MacPod* compare nel paper come **didascalia di una figura** (p. 239) e come **riferimento bibliografico [11]** (Rolfe, C., 1998, *MacPod. Real-time asynchronous granular synthesis software for the Macintosh PowerPC*, Vancouver: Third Monk Inc.), non come titolo. Il paper CIM XII presenta **MacPod** come implementazione di riferimento, ma il suo titolo è *The Corner Effect* e gli autori sono Keller (SFU) e Rolfe (Third Monk Software / CCWIA), non Truax. Il volume 1998 della stessa coppia di autori sull'argomento ecologically-based granular synthesis è invece Keller & Truax (1998), ICMC Ann Arbor — citato come ref [6] del paper.

## Categoria e lunghezza
Comunicazione scientifica — 4 pagine (pp. 236–239) — 13 riferimenti bibliografici.

## Argomento centrale
Analisi teorica e pratica del *corner effect*: artefatto comb-filter prodotto dalla finestra trapezoidale (usata da MacPod per ridurre il costo computazionale rispetto alla gaussiana). Tesi: ciò che la teoria DSP scarta come artefatto non desiderato diventa parametro compositivo utile nella sintesi granulare, perché modificazioni spettrali analoghe sono comunque inerenti al GS in regime di overlap medio-alto. Affianca all'analisi della finestra una proposta architetturale per *ecologically-based resynthesis* basata su grain pool pre-costruito, controllo della phase-synchronicity inter-stream e definizione dell'*event* come unità di alto livello.

## Sistema o strumento descritto
**MacPod** (Macintosh PowerPC, real-time, derivato dal modello POD di Truax 1988). Implementazione di riferimento di Keller/Rolfe basata su finestra trapezoidale efficiente. Fino a 20 grain stream simultanei, grain rate minimo 1 ms. Single pointer al materiale sorgente. Phase-synchronicity inter-stream come parametro compositivo unico per controllare overlap. Quattro modalità di accesso al sound database: incremental, loop, cycle, random.

## Analogia con PGE
Vettori di analogia diretta — anche se MacPod è real-time, l'**ontologia degli oggetti** anticipa quella di PGE:

1. **Stream come unità di voce indipendente.** Quote (p. 237, sez. *The stream*): *"Although some GS systems combine several grain streams into a single voice [1], it is conceptually clearer to conceive each voice as a separate stream. Thus, overlap can be controlled from a unique parameter which stands for the coincidence [3], or phase-synchronicity, among grain onsets in all active voices."* Ontologia di `Stream` PGE — un grain generator produce un singolo grano alla volta, polifonia ottenuta moltiplicando stream. Pattern identico.

3. **The pointer** (p. 238, sezione dedicata): 4 modalità di lettura del file — incremental, loop, cycle, random. Precursore diretto di `PointerController` PGE (speed_ratio + modalità loop statico/dinamico + accesso indicizzato). PGE generalizza `cycle` come `direction` parametro e `random` come deviazione stocastica.

5. **Density come parametro globale di alto livello.** Esempio Keller/Rolfe (p. 238, sez. *The event*): density definita da `duration × quantity of grains` con grain overlap come unica control variable; «*the quantity of grains and the overall duration change accordingly*». Stessa logica di `DensityController` PGE: `fill_factor` o `density` come variabile di alto livello che induce ricalcolo automatico di IOT/numero grani.

## Posizionamento storico
**Atto 2** della narrazione tre atti: post-DMX-1000 (Truax 1988), real-time è disponibile su workstation generaliste (Macintosh PowerPC, 1998). Tappa intermedia tra:
- Truax 1988 (DMX-1000, hardware dedicato) — real-time ma su DSP custom.
- MacPod / *The Corner Effect* 1998 — real-time su CPU general-purpose, grazie a finestra trapezoidale efficiente.
- EmissionControl2 2021 (Roads/Kilgore/DuPlessis) — real-time per-grain interattivo a piena maturità.

Testimonia che entro 10 anni dal DMX-1000 il vincolo hardware era già rotto su piattaforme commerciali. Rafforza l'argomento del paper CIM 2026: il deferred time di PGE non è ricaduta su vincoli hardware ma scelta postura compositiva.

## Note stilistiche
- **Struttura**: introduzione tecnica (windowing, corner effect) → ontologia (overlap, stream, waveform, pointer, event) → conclusione. Sezioni brevi (1-2 paragrafi); pattern *sezione = oggetto del sistema*. Apertura su problema tecnico (efficienza windowing) senza preamboli storici.
- **Tono**: descrittivo-tecnico, registro CMJ. Quasi nessuna argomentazione estetica.
- **Densità citazioni**: 13 ref. Mix DSP (Jones/Parks 1988 [4], Truax 1988 [12], Roads 1997 [9]) + cognitivo-ecologico (Truax 1992 *soundscape* [13]) + tools (Rolfe 1998 MacPod [11], Keller/Truax 1998 ICMC [6]).
- **Modello da non imitare per CIM 2026**: il paper PGE deve aprire argomentativamente, non con dettaglio implementativo.
- **Modello riusabile**: titolare ogni sezione con il nome dell'oggetto del sistema (*The stream*, *The waveform*, *The pointer*, *The event*) — pattern utilizzabile per PGE sezione 3.

## Concetti correlati

- [[decorrelazione-granulare]] — ontologia stream/waveform/pointer/event come base per il framework formale della decorrelazione ([[rolfe-keller2000]] 2000 → [[vaggione2002]] 2002)
- [[finestratura-come-modulazione]] — il corner effect come fonte CIM diretta per la claim "finestratura = modulazione, mai trasparente" (riformulazione §2.1 del paper, 2026-06-11)

## Sezioni del paper CIM 2026 dove citare

- **`sec:stream-minimo`** (primaria): il profilo spettrale della finestra come
  parametro timbrico (*corner effect*), nel passaggio sulla finestratura come
  modulazione. Cfr. [[finestratura-come-modulazione]].

Fonte di verità: [[mappa-citazioni-paper]].

## Quote chiave
- *"Although some GS systems combine several grain streams into a single voice [1], it is conceptually clearer to conceive each voice as a separate stream. Thus, overlap can be controlled from a unique parameter which stands for the coincidence [3], or phase-synchronicity, among grain onsets in all active voices."* (p. 237, sez. *The stream*) — formulazione canonica dell'ontologia Stream + parametro inter-stream globale; ripresa diretta nell'architettura PGE.
- *"GS systems access the sound database contents in four different ways to: (1) incremental, the file is read from beginning to end; (2) loop, the file is read repeatedly from beginning to end; (3) cycle, the file is read repeatedly from beginning to end and backwards; and (4) random, the file is read at random locations."* (p. 238, sez. *The pointer*) — tassonomia delle modalità di lettura buffer; precursore esplicito di `PointerController` PGE.
- *"by using grain overlap as the only control variable and letting the quantity of grains and the overall duration change accordingly, we will be dealing directly with the relevant perceptual parameters."* (p. 238, sez. *The event*) — principio di parametro perceptually-relevant come singola variabile di controllo; legittima la strategia `DensityController` PGE (fill_factor / density come singolo handle).
- *"the effect of the overlapping grains can be simply explained as a comb-filter delay. If one assumes a fixed grain envelope, an asynchronous grain six milliseconds later than the original is simply a six-millisecond delay mixed in with the original signal."* (p. 238, sez. *The pointer*) — lettura comb-filter della sovrapposizione di grani disallineati; stessa matematica dell'artefatto documentato in [[time-stretching-granulare]].
- *"This type of window produces a spectral profile which depends on the placement of the 'corners' of the trapezoid. Thus, what has been regarded as an unwanted artifact by DSP theory, becomes a useful parameter for sound synthesis."* (p. 239, conclusione) — tesi del paper: l'artefatto di finestratura come parametro compositivo; fonte CIM per [[finestratura-come-modulazione]].
- Minori, stessa direzione: *"a slight 'smearing' of the spectrum"* (confronto spettrogrammi gaussiana vs trapezoidale, p. 237) e *"avoiding the 'blurring' effect that occurs in asynchronous GS"* (p. 238, sez. *The waveform*, sul grain pool ecologico).
