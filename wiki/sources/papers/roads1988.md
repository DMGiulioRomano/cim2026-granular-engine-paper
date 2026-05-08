# [Roads, 1988] Introduction to Granular Synthesis

## Citazione CIM
Roads, C. (1988). Introduction to Granular Synthesis. *Computer Music Journal*, 12(2), 11–13.

## Argomento centrale
Editoriale introduttivo che apre il numero monografico di *CMJ* dedicato alla
sintesi granulare (con i paper Truax 1988 e Jones & Parks 1988). Definisce la
tecnica come forma di sintesi additiva su migliaia di grani quasi-gaussiani
(1–50 ms), ne ricostruisce il lignaggio teorico (Gabor → Wiener → Moles →
Xenakis) e codifica per la prima volta in CMJ il vocabolario operativo:
*grain*, *grain density*, *event*, *cloud*, *granulation*.

## Gap o problema identificato
Roads non formula un gap esplicito — il pezzo è descrittivo. Tuttavia
l'enumerazione dei *dodici parametri* di un evento (begin, duration, waveform,
waveform slope, center freq, freq slope, bandwidth, bw slope, density,
density slope, amplitude, amp slope) introduce implicitamente il problema che
Truax 1990 renderà esplicito: governare dodici inviluppi temporali simultanei
senza un livello superiore di organizzazione è opaco al compositore. Roads
non lo nomina; lo struttura come dato di fatto della pratica.

In chiusura indica due direzioni aperte rilevanti: (a) il *frame/screen*
xenakiano "merita ulteriori studi" perché i problemi tecnici non sono
risolti; (b) il real-time "si avvicina" grazie al DSP DMX-1000 di Truax —
ancora futuro nel 1988.

## Rilevanza diretta per PGE
Triplo legame:

1. **Event a 12 parametri = precursore diretto del DSL YAML PGE.**
   I parametri Roads sono variabili indipendenti con *slope*: una rampa
   lineare iniziale → finale. PGE generalizza con l'astrazione `Envelope`
   (lista di breakpoint con forma) applicabile a ogni parametro
   (`density.distribution`, `pointer.position`, `pitch`, etc.) — non solo
   slope lineare ma curve arbitrarie. Stessa logica di alto livello, più
   espressiva.

2. **"Within an event, grains are scattered randomly according to the
   initial grain density and the density slope" (p. 12) = esattamente
   `DensityController` PGE.** L'IOT = 1/density e la modulazione tramite
   `Envelope` riproducono il comportamento Roads, con in più la blend
   sincrono/asincrono di Truax 1990 (vedi `density-controller.md`).

3. **"Events can be plotted as lines, triangles, and rhomboid shapes on a
   frequency-versus-time graph" (p. 12).** Roads anticipa la visualizzazione
   di eventi come forme su piano cartesiano. PGE conserva lo spirito
   (forme = inviluppi parametrici visualizzabili) ma sostituisce l'asse
   frequenza con asse *posizione-nel-buffer* (vedi `score-visualizer.md`):
   scelta motivata dal caso d'uso granulazione di campioni, dove la
   posizione di lettura è il parametro espressivo dominante che emerge tramite `speed_ratio` del PointerController.

Riferimenti diretti a Truax 1988 (DMX-1000) e Xenakis screens: PGE si colloca
nella tradizione Roads-Truax (granulazione, parametri continui) più che in
quella xenakiana (scattering stocastico per nuvole astratte).

## Collegamento alla tesi centrale

Roads 1988 fornisce il vocabolario canonico (grain, density, event, cloud,
granulation) e il lignaggio Gabor → Wiener → Moles → Xenakis → Roads in cui
PGE si inserisce come ramo deferred-time della linea Roads-Truax. Non
formula problemi compositivi: codifica il paradigma come dato di fatto
della pratica.

Tre punti di leva diretti per i contributi del paper:

1. **Primo contributo (YAML DSL).** L'event a 12 parametri (initial value +
   slope per ognuno) è il precursore diretto del DSL YAML. PGE generalizza
   slope lineare → `Envelope` con breakpoint a forma arbitraria, e
   l'astrazione `Stream` eredita l'idea di evento come oggetto di alto
   livello che incapsula migliaia di grani.

2. **Secondo contributo (partitura grafica).** "Events plotted as lines,
   triangles, and rhomboid shapes on a frequency-versus-time graph" (p. 12)
   anticipa la visualizzazione di eventi come forme su piano cartesiano.
   PGE conserva lo spirito (forme = inviluppi parametrici visualizzabili)
   ma sostituisce l'asse frequenza con asse posizione-nel-buffer per il
   caso d'uso granulazione di campioni — scarto motivato dal contributo 2,
   non rottura concettuale.

3. **Lignaggio architetturale.** "Within an event, grains are scattered
   randomly according to the initial grain density and the density slope"
   (p. 12) è esattamente `DensityController` PGE (IOT = 1/density,
   Envelope su `density` o `distribution`).

Roads 1988 si colloca prima di Truax 1990 nella narrazione storica
(atto 1 ↔ atto 2): è ancora la stagione del tempo differito vissuto come
dato della pratica — il real-time DSP è citato come direzione futura
("granular synthesis is approaching real time", p. 12).

## Sezioni del paper CIM 2026 dove citare
- **Sezione 1 (Introduzione):** definizione canonica di sintesi granulare
  e vocabolario (grain, density, event, cloud).
- **Sezione 2 (Sintesi granulare: dal paradigma Gabor al controllo
  gerarchico):** lignaggio Gabor → Xenakis → Roads → Truax; event a 12
  parametri come antenato del DSL parametrico PGE.
- **Sezione 4 (Partitura grafica):** "events plotted as lines, triangles,
  rhomboid shapes" come precedente di visualizzazione cartesiana di eventi
  granulari, motivando il nostro scarto (asse Y = posizione-buffer, non
  frequenza).

## Quote chiave

> "Granular synthesis involves generating thousands of very short *sonic
> grains* to form larger acoustic events. The technique can be classified
> as a form of *additive synthesis*." (p. 11)

> "An event is characterized by twelve parameters: 1. Beginning time
> 2. Duration 3. Initial waveform 4. Waveform slope […] 9. Initial grain
> density 10. Grain density slope 11. Initial amplitude 12. Amplitude
> slope. Within an event, grains are scattered randomly according to the
> initial grain density and the density slope." (p. 12)

> "Depending on the parameter values specified for them, events can be
> plotted as lines, triangles, and rhomboid shapes on a frequency-versus-
> time graph. These shapes can be configured to form arbitrary inscriptions
> and polygons mapped onto the graph of audible sounds." (p. 12)

> "The screen or frame-based approach to grain organization suggested by
> Xenakis (1971) merits further study. Although there are several technical
> problems to be resolved, it appears to be an interesting and possibly
> fruitful avenue of research." (p. 12)