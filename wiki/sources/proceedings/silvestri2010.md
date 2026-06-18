# [Silvestri, 2010] Introduzione alla sintesi Wavetable Switching per Multiplexing di segnali

## Citazione CIM

Silvestri, S. (2010). Introduzione alla sintesi Wavetable Switching per Multiplexing di segnali. In *Atti del XVIII Colloquio di Informatica Musicale (XVIII CIM)*, pp. 209–213. Università IUAV di Venezia, ed. DADI — Dip. Arti e Design Industriale.

## Categoria e lunghezza

Comunicazione orale (paper tecnico-formale) — 5 pagine — 9 riferimenti.

## Argomento centrale

Introduce un procedimento tempo-discreto di sintesi per *wavetable switching per multiplexing di segnali*: oscillatori wavetable look-up paralleli, ciascuno con inviluppo quadro sfasato $\phi_n + \Delta t / T_{env}$; un emulatore di multiplexer N-bit (rete combinatoria AND/NOT/OR) commuta i sub-vettori e produce in uscita un segnale risultante $y_n$ composto da brevi frazioni di campioni. Per $f_{cm} > 20\div25\,\mathrm{Hz}$ ($T_{cm} \approx 50\div40\,\mathrm{ms}$) il sistema si colloca al confine fusione percettiva / arricchimento spettrale (bande laterali) e l'autore lo inquadra esplicitamente come *forma di sintesi granulare deterministica*.

## Sistema o strumento descritto

Modello algoritmico (non un singolo software): implementazioni provate in **Csound** e **Pure Data** (p. 210, nota 9). Composizione di riferimento **«Studio Sonoro III»** «interamente basata su algoritmi di wavetable multiplexing implementati sia per la sintesi in tempo reale che, per la parte per nastro, in tempo differito» (nota 10, p. 210). Lavoro estratto dalla tesi I Liv. dell'autore (Cons. S. Pietro a Majella, A.A. 2008/2009, relatore A. Di Scipio).

## Analogia con PGE

**Anti-precursore strutturale**, doppia direzione:

1. Il grano in Silvestri **non è generato per loop generativo** (`Stream.generate_grains()` PGE) ma è il prodotto incidentale di un meccanismo combinatorio di commutazione: la finestratura $T_\lambda$ definisce velocità e durata del quanto, l'apparato MUX «decreta l'ordinamento temporale del quanto stesso» (p. 211). Asse di controllo trasversale rispetto a Roads/Truax: nessuna `density`, nessuna `tendency-mask`, solo logica combinatoria deterministica sulla sequenza di indirizzi.
2. **Coesistenza tempo-reale + tempo-differito nella stessa opera** (Studio Sonoro III): il differito non è ripiego ma è scelto «per la parte per nastro», cioè per il segmento in cui il controllo fine sui transienti spettrali microstrutturali è prioritario. Conferma CIM 2010 della legittimità compositiva del differito *quando il materiale lo richiede* — coerente con la postura PGE ma argomentata su un asse tecnico opposto (combinatoria spettrale vs cache+IR).

## Posizionamento storico

- Filone **granulare deterministico** CIM (cfr. [[granulare-deterministico-cim]]): con [[rizzuti2006]] (mappa logistica → controllo grani) e [[discipio1991]] (mappe non-lineari) forma il sottoinsieme dei lavori che rifiutano la sintesi stocastica come modello obbligato per il livello macro. Silvestri 2010 è single data-point della **sotto-famiglia (B) combinatoria deterministica MUX**, distinta dalla sotto-famiglia (A) caotico-iterativa di Di Scipio/Rizzuti (nessuna `xn+1=f(xn)`, il grano è prodotto incidentale della rete combinatoria di commutazione).
- **Lineage napoletano CIM**: terzo nodo dopo [[depoli-piccialli1988]] (forme d'onda granulari sincrone) e [[ortosecco-piccialli1989]] (wavelet=grano). Tutti tre i lavori sono ad orientamento DSP/segnale, contrastano con il filone padovano/veneto-orientato-al-controllo.
- **Thread Di Scipio CIM allievi**: Silvestri è studente di Di Scipio (tesi 2008/2009). Lo stesso autore appare co-firmatario con Arcella nel volume successivo [[arcella-silvestri2012]] (*Analogique B*, Xenakis): continuità di un magistero che attraversa due volumi CIM consecutivi.
- **Tempo reale + differito coesistenti**: dichiarato esplicitamente per Studio Sonoro III. Punto di osservazione CIM 2010 in cui la dicotomia paradigmatica RT/offline non si presenta come scelta esclusiva ma come repertorio tecnico interno alla stessa composizione.

## Note stilistiche

Densità simbolica alta (formule numerate E.1–E.7, oscillatori wavetable formalizzati con accumulatori di fase $\phi_n = (n+1) \bmod N$, multiplexer formalizzato come $U = 2^I$). Tre figure: spettrogramma del test, schema a blocchi dell'algoritmo, dettaglio sotto-modulo "Mux". Tono **tecnico-descrittivo** con apertura argomentativa breve («metodi transizionali», riferimento Palm 1975) e chiusura programmatica (sez. 5 «Concluzioni e sviluppi» elenca direzioni: porting su MCU DSP RISC, espansione a sorgenti acquisite real-time, controllo combinatoriale delle permutazioni). 9 references miste: 2 manuali storici italiani (De Poli 1981, Mathews 1976), 2 dispense Di Scipio/Cavaliere 2009, 1 tesi propria, 2 paper AES tecnici (Bristow-Johnson 1996, Horner-Beauchamp-Haken 1993), 1 manuale telecom italiano (Valdoni-Vatalaro 1984), 1 manuale italiano sintetizzatori (Horn 1988). **Nessun riferimento a Roads, Truax, Xenakis nella bibliografia** nonostante Xenakis-Gabor compaiano nella chiusura (citati nel corpo, non in lista ref) — pattern stilistico CIM 2010 «short ref list, citazione interna estesa».

Modello stilistico utile per PGE su un aspetto specifico: paper formale con un solo autore, 5 pagine, 9 ref, esplicitamente derivato da tesi di laurea — soglia minima del paper CIM accettato, utile come benchmark inferiore di densità.

## Sezioni del paper CIM 2026 dove citare

Fonte non citata nel paper attuale; cfr. [[mappa-citazioni-paper]].

## Quote chiave

> «Tale metodica [...] può essere visto come una forma di sintesi granulare deterministica dove operazioni quali lettura e finestratura rappresentano la generazione del grano <<o quanto sonoro>>, mentre l'apparato di commutazione è ciò che guida i parametri del grano stesso.» — p. 209

> «Studio Sonoro III — composizione interamente basata su algoritmi di wavetable multiplexing implementati sia per la sintesi in tempo reale che, per la parte per nastro, in tempo differito.» — p. 210, nota 10

> «La variante di wavetable switching qui introdotta può essere quindi assimilata ad un processo granulare-deterministico atto a fornire una rappresentazione quantistica [Xenakis, Gabor], pur sempre ordinata degli stream sonori.» — p. 212
