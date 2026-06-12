# [Ortosecco, Piccialli, 1989] Sintesi granulare e Digital Signal Processing

## Citazione CIM
Ortosecco, I., & Piccialli, A. (1989). Sintesi granulare e Digital Signal Processing. In *Atti dell'VIII Colloquio di Informatica Musicale* (pp. 58-67). Cagliari.

Nota: nel sommario degli atti il contributo compare come *"Sintesi granulare e metodi di analisi"* (titolo della sezione tematica); il titolo effettivo del paper nel corpo è *"Sintesi granulare e Digital Signal Processing"*. Affiliazione autori: Dipartimento di Scienze Fisiche, Università di Napoli.

## Categoria e lunghezza
Comunicazione — 10 pagine (pp. 58-67) — 11 riferimenti bibliografici — 6 figure (channel vocoder classico vs wavelets, risposte filtri mirror, scaling function, ricostruzioni segnale sintetico).

## Argomento centrale
Il paper propone le **wavelets ortonormali** come base teorica rigorosa della sintesi granulare, identificando la *wavelet* con il *grano* di Roads. Sulla base di questa identificazione gli autori implementano un sistema di analisi a banco di filtri (channel vocoder) derivato da wavelet quasi-ortogonale di Kronland-Martinet e da wavelet ortonormale propria, eseguito su scheda DSP Ariel con processore TMS 32025 su PC AT. Obiettivo: fornire all'operatore musicale uno strumento di analisi/sintesi in cui i coefficienti wavelet diventano i parametri compositivi della successiva risintesi granulare.

## Sistema o strumento descritto
Banco di filtri (channel vocoder) basato su wavelets — due varianti: (a) wavelet quasi-ortogonale di Kronland-Martinet (gaussiana × esponenziale complesso); (b) wavelet ortonormale calcolata dagli autori a partire da coppia di filtri mirror passa-basso/passa-alto (condizione di ricostruzione perfetta). Wavelet prototipo tabulata su 4096 campioni, sottocampioni dedotti dalla tabella base. Hardware: scheda Ariel con TMS 32025 su PC AT. Memorizzazione segnale + riascolto dopo modifiche parametriche tramite DAC. **Offline** (analisi su segnale memorizzato + risintesi). Anno: 1989.

## Analogia con PGE
Analogia indiretta ma significativa. Tre punti di contatto:

1. **Tabulazione del grano**: Ortosecco/Piccialli tabulano la wavelet prototipo su 4096 campioni e generano i grani per sottocampionamento da tabella; PGE pre-genera la finestra del grano una sola volta nel `WindowGenerator` e riusa la tabella per tutti i grani della specifica YAML. Stesso pattern *precompute-once, reuse-many* che separa la costruzione della forma d'onda dalla riproduzione.

2. **Analisi come precondizione della specifica**: il loop lungo PGE include il momento di ascolto e riflessione su materiale già renderizzato; Ortosecco/Piccialli formalizzano l'estrazione di parametri da segnale dato come base per la risintesi granulare controllata. Entrambi separano un livello *analitico* (parametri estratti / parametri dichiarati in YAML) da un livello *sintetico* (rendering).

3. **Offline come scelta tecnica esplicita**: gli autori riconoscono che le implementazioni in tempo reale sono "in via di progettazione" ma il lavoro presentato è offline su scheda DSP. Non rifiuto del real-time, ma fase metodologica precedente. PGE riprende questa postura in chiave compositiva volontaria (cfr. [[discipio1991]]).

Nessuna analogia diretta a livello di pipeline: PGE non fa analisi (non estrae parametri da segnale), parte da specifica dichiarativa YAML.

## Posizionamento storico
Filone *analisi/sintesi granulare con fondamento DSP*. Si distingue dalla linea Roads (sintesi sintetica da modello sinusoide+gaussiana) e dalla linea Truax (granulazione di samples in real-time). Posizionamento esplicito nel testo: la sintesi granulare di Gabor "ha avuto scarse applicazioni" per problemi teorici; l'avvento delle wavelets (Kronland-Martinet et al. 1987, Mallat) fornisce "una solida base teorica" che colma il gap. Linea italiana CIM: prosegue il lavoro De Poli/Piccialli 1988 sulla sintesi granulare sincrona ([[depoli-piccialli1988]] su CIM VII), cita esplicitamente il paper precedente come riferimento per le periodicità dell'inviluppo nelle strutture formantiche (p. 60).

## Note stilistiche
- Struttura sezioni: introduzione → "Channel Vocoder" (interpretazione classica) → "Channel Vocoder mediante Wavelets" (proprietà wavelets, formule integrali, filtri mirror) → "Implementazione del sistema di analisi" (hardware Ariel/TMS 32025) → "Conclusioni" → Bibliografia → Figure (6 figure non incluse nel testo principale, accodate alle pp. 64-67).
- Densità citazioni: 11 riferimenti — mix DSP classico (Schroeder 1966, Gold & Rader 1967), wavelets (Kronland-Martinet 1987, Mallat, Bastians 1980), filtri mirror (Pirani-Zingarelli 1984, Vaidyanathan 1987), sintesi granulare (Gabor 1946-47, Roads-Strawn 1985, De Poli-Piccialli 1988).
- Uso figure: 6 figure in fondo — schematiche, contrasto alto, leggibili in B&W. Confronto a coppia (Fig. 5 wavelet ortonormale vs Fig. 6 quasi-ortonormale) sostiene visivamente la tesi della maggiore efficienza.
- Tono argomentativo: posizionamento esplicito del proprio contributo ("se identifichiamo la wavelet con il grano… l'approccio mediante wavelet fornisce una solida base teorica"). Apertura inquadra il problema, conclusioni rivendicano il risultato.
- Apertura/chiusura tipiche: apre con motivazione percettiva ("sintesi granulare fornisce un metodo intuitivo per modellare sorgenti sonore"), chiude con prospettiva real-time futura ("strutture di calcolo ad alto parallelismo permetterà in futuro implementazioni in tempo reale già in via di progettazione").

## Quote chiave

Apertura (motivazione percettiva): *"sintesi granulare fornisce un metodo intuitivo per modellare sorgenti sonore"*.

Posizionamento storico del paradigma granulare prima dell'apporto wavelets: la sintesi granulare di Gabor *"ha avuto scarse applicazioni"* per problemi teorici; *"l'approccio mediante wavelet fornisce una solida base teorica"* alla sintesi granulare.

Tesi centrale (identificazione wavelet=grano): *"se identifichiamo la wavelet con il grano […] l'approccio mediante wavelet fornisce una solida base teorica"*.

Riferimento esplicito al lavoro precedente di De Poli/Piccialli (p. 60): periodicità dell'inviluppo nelle strutture formantiche come specifica del modello pitch-synchronous (citazione di De Poli, Piccialli 1988, CIM VII).

Chiusura (postura offline come fase metodologica, non rifiuto del real-time): *"strutture di calcolo ad alto parallelismo permetterà in futuro implementazioni in tempo reale già in via di progettazione"*.

## Sezioni del paper CIM 2026 dove citare

Fonte non citata nel paper attuale; cfr. [[mappa-citazioni-paper]].

