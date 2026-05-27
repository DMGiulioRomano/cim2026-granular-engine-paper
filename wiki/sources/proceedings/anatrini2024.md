# [Anatrini, 2024] WavePilot: Framework multidimensionale per l'esplorazione dello spazio parametrico di strumenti digitali

## Citazione CIM
Anatrini, A. (2024). WavePilot: Framework multidimensionale per l'esplorazione dello spazio parametrico di strumenti digitali. In *Atti del XXIV Colloquio di Informatica Musicale*, pp. 129–135. Torino: AIMI.

## Categoria e lunghezza
Comunicazione orale (Session 3 — Tools and platforms) — 7 pp. (pp. 129–135) — 25 riferimenti.

## Argomento centrale
Anatrini presenta WavePilot, framework Python+JavaScript che mappa lo spazio parametrico di Digital Multimedia Instruments (DMmI) in uno spazio virtuale a bassa dimensionalità tramite Variational Autoencoder (VAE), con meta-GUI browser navigabile per interpolazione non lineare (RBF) tra preset. L'obiettivo è ridurre la curva di apprendimento di sintetizzatori complessi e unificare programmazione parametrica e attività compositiva.

## Sistema o strumento descritto
WavePilot — framework open source (github.com/anatrini/WavePilot), Python + JavaScript browser, host plugin via Reaper/Live + OSC verso Max/TouchDesigner/FAUST, real-time interactive, 2021–2024 (origine come patch Max 2021).

## Analogia con PGE
**Doppia analogia + anti-analogia simmetrica** sull'asse dell'esplorazione dello spazio parametrico:

*Analogia di scopo*:
- Entrambi affrontano il problema della *distanza concettuale tra interfaccia di controllo, spazio percettivo e spazio semantico* (Anatrini Fig. 1, p. 130, citando Wessel/Wright [13]).
- Entrambi unificano programmazione e composizione: Anatrini «superare la tradizionale separazione tra il processo di programmazione dei parametri della sintesi sonora e l'attività compositiva in sé» (p. 130) ≡ tesi PGE del loop lungo come spazio compositivo.
- Entrambi citano Xenakis UPIC e Matthews Graphic I [8] come radice della *meta-GUI come partitura* (sez. 2.1).

*Anti-analogia su quattro assi ortogonali*:

1. **Black box vs white box**: WavePilot opera su plugin VST commerciali (Ob-Xd 83 parametri, Anatrini Fig. 3 p. 133) trattati come scatole parametriche opache; il VAE apprende mappature non lineari *senza* conoscenza preliminare della semantica dei parametri. PGE opera su DSL YAML strutturato dove ogni parametro è semanticamente esplicito nell'IR Python.

2. **Riduzione vs esposizione della dimensionalità**: WavePilot *riduce* alta-dimensionalità → spazio 2D/3D navigabile per controllo intuitivo, accettando ambiguità («le dimensioni ridotte sono "entangled" [...] non hanno necessariamente un'interpretazione diretta nel contesto dei dati originali», p. 131). PGE *espone* la dimensionalità nel DSL declarativo per controllo deterministico-stocastico esplicito (tendency mask + ProbabilityGate).

3. **Real-time gestuale vs deferred declarativo**: WavePilot è real-time interattivo — cursore-traiettoria nella meta-GUI guida modulazione simultanea di tutti i parametri via OSC; PGE è offline batch — YAML → SCO → AIF con feedback dopo rendering.

4. **GUI come input vs partitura come output**: la meta-GUI WavePilot è *spazio di controllo* in cui il compositore naviga per generare suono (analogo concettuale al *space actant* di Valle/Lombardo 2003); il score_visualizer PGE è *output diagnostico read-only* che il compositore legge per riflettere. Stessa inversione di flusso già osservata in [[valle-lombardo2003]]. Cfr. [[graphic-score]] per la tavola sinottica del lineage visivo granulare (anti-analogia WavePilot inclusa).

## Posizionamento storico
Linea **DMI auto-programming** (Automatic Synthesizer Programming, ASP): Anatrini distingue *parameter exploration* (algoritmi genetici, mapping, unsupervised learning) e *sound matching* (deep learning su descrittori percettivi). WavePilot si colloca nel primo filone come strumento agnostico verso la tipologia di DMmI (audio/video/effetti). Filone CIM real-time italiano post-2020 al polo opposto di PGE; complementare a [[sparano2018]] (granulazione quasi-sincrona Max+Gen, polo gestuale Eurorack-like) e [[markidis2024]] (*Mediation Process in a Computer Music Interpretation*, XXIV CIM, pp. 48–56, ecosystemic Di Scipio real-time interpretation — coppia stesso volume CIM XXIV: due polarità 2024 sull'unificazione programmazione/composizione, riduzione via deep learning vs preservazione via graphical DSP score). Lineage meta-GUI: Matthews Graphic I (1968) → UPIC Xenakis → Hyperscore Farbood (2001).

## Note stilistiche
**Struttura**: abstract bilingue + 5 sezioni (Motivazioni / Contesto / WavePilot / Applicazioni pratiche / Conclusioni) + bibliografia 25 voci. Densità citazionale alta (25 ref / 7 pp.) — modello CIM 2024 per tool paper con framing teorico esteso. Sezione 2 (*Contesto*) interamente dedicata a posizionamento concettuale prima dell'architettura — pattern *cornice teorica = una sezione propria* riusabile per CIM 2026 sez. 2. Uso esteso di formule matematiche (Eq. 1–5: MSE loss VAE, divergenza KL, RBF gaussiana) come densità tecnica del corpo. 3 figure (schema concettuale + schema funzionamento + grafico errore vs entry). Bibliografia mista *informatica musicale* (NIME/SMC/ICMC/CMJ) + *filosofia/STS* (Di Scipio, Borgdorff, Tomás) + *machine learning* (arXiv preprints VAE/normalizing flows). Apertura motivazionale (progetto Healing Soundscape come radice biografica) + chiusura su sviluppi futuri.

**Tono**: argomentativo e auto-riflessivo. Quote-tipo «perdere il controllo per acquisire complessità» (sez. 2.2) inquadra esplicitamente l'accettazione dell'ambiguità come *scelta* compositiva — postura opposta ma simmetrica al loop lungo PGE.

## Sezioni del paper CIM 2026 dove citare
- **Sezione 2** (panorama): WavePilot come polo CIM 2024 dell'esplorazione parametrica via deep learning, contraltare di PGE come esplorazione parametrica via DSL declarativo. Citare in nota sulla pluralità di approcci attuali alla relazione interfaccia-suono.
- **Sezione 3** (architettura): citare WavePilot come riferimento sulla *meta-GUI come partitura* + framing della distanza tra parameter/perceptual/semantic space (Fig. 1 p. 130). Pattern di paper CIM 2024 che premette sezione concettuale prima dell'architettura.
- **Sezione 4** (partitura grafica): WavePilot come anti-analogia di flusso (GUI input vs partitura output), insieme a [[valle-lombardo2003]] per consolidare la differenziazione del score_visualizer come strumento diagnostico read-only.
- **Sezione 6** (conclusioni / sviluppi futuri): WavePilot come riferimento per eventuale GUI navigabile come direzione di sviluppo PGE complementare al loop lungo, non sostitutiva.

## Quote chiave
- p. 130: «la pratica compositiva dell'autore [...] mira a integrare in modo organico i diversi aspetti del sound design, della generazione di materiale e della gestione formale dell'atto compositivo attraverso l'uso di una meta-GUI».
- p. 130: «La motivazione della programmazione automatica dei DMI risiede nella riduzione della curva di apprendimento [...] la distanza concettuale che si crea tra l'interfaccia di controllo (spazio dei parametri), il suono effettivamente prodotto dallo strumento (spazio percettivo) e come viene interpretato qualitativamente dall'utente (spazio semantico)».
- p. 131: «La rappresentazione a bassa dimensionalità dello spazio parametrico assume di conseguenza una valenza percettiva ambigua. Il carattere agnostico del tool implica che la valenza semantica delle dimensioni ridotte sia fortemente influenzata dai preset scelti in partenza».
- p. 131: «non siamo più di fronte a un'interazione tra utente e un sistema deterministico con degli obiettivi predefiniti, ma a un dialogo uomo-macchina che coinvolge diverse modalità di rappresentazione della conoscenza».
- p. 132: «il compito della programmazione di un DMmI è ridotto ad un problema di mapping non lineare all'interno di uno spazio virtuale multidimensionale».
