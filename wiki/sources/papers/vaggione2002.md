# [Vaggione, 2002] Décorrélation microtemporelle, morphologies et figurations spatiales

## Citazione CIM
Vaggione, H. (2002). Décorrélation microtemporelle, morphologies et figurations spatiales. In *Actes des Journées d'Informatique Musicale (JIM 2002)*, Marseille, mai 2002. (HAL hal-02992872, 12 pp.)

## Argomento centrale
Generazione di attributi morfologici di ordine spaziale per mezzo di *decorrélation microtemporelle*: piccoli offset temporali (ordine dei millisecondi, talvolta microsecondi) applicati a repliche di un suono distribuite su canali fisicamente separati. La decorrelazione opera *a monte* dei sistemi di diffusione/spazializzazione globale e modella, in modo deliberatamente esagerato rispetto al modello ITD (interaural time delay) acustico, una direzionalità o ambiguità spaziale composta come attributo della morfologia stessa.

## Gap o problema identificato
- Tecniche di decorrelazione esistono in ingegneria del segnale e spazializzazione globale (Lindemann 1986, Kendall 1995, Kaup et al. 1999), ma manca *elaborazione teorica e letteratura sugli aspetti compositivi* dell'uso «morphophorique» (Vaggione, p. 2).
- Il *panning* classico posiziona suoni in campo spaziale stabile, sincronico, esterno rispetto alle morfologie in gioco — non è interazione tra caratteristiche morfologiche e localizzazione (p. 9).
- Modellazione stretta dell'ITD (5 µs – 1.5 ms) è insufficiente per scopi compositivi: occorre giocare con intervalli «arbitrari» (decine di ms) per generare direzionalità musicalmente significative anche se acusticamente non realistiche (p. 5).

## Condizioni minime della décorrélation microtemporelle (p. 6)
a) repliche distribuite in canali fisicamente diversi (evitare phasing / colorations frequenziali);
b) polifonia: più sorgenti con repliche decorrelate, valori time-varying degli offset (altrimenti immagine fissa);
c) lavorare nel microtemps (qualche millisecondo); offset più grandi escono dal fenomeno spaziale e diventano eventi separati.

## Rilevanza diretta per PGE
1. **VoiceManager realizza direttamente la decorrelazione microtemporelle**. Le quattro strategie ortogonali della classe `VoiceManager` (pitch, onset, pointer, pan) producono *per ogni voce* una replica decorrelata della specifica Stream: la `onset_offset` strategy realizza esattamente il decalage di ms tra repliche; la `pan` strategy le distribuisce su canali distinti (condizione a Vaggione); il loro layering produce la *polyphonie spatialisée* richiesta (condizione b).

2. **Dephase per-grano come decorrelazione fine**. `PointerController` + `DensityController` introducono deviazione per-grano (dephase) che frantuma la sincronizzazione tra grani omologhi di voci diverse. È esattamente la *relation kaléidoscopique multi-locale* di Vaggione (p. 7): non distorsione globale di fase, ma «une grande quantité de différences locales de phase, négatives et positives, qui se succèdent rapidement».

3. **Tempo differito esplicito come contesto compositivo nativo della tecnica**: Vaggione apre la sezione *Approche du mixage algorithmique* (p. 3) dichiarando: «en travaillant dans le cadre d'une situation typique de "studio numérique", c'est-à-dire en temps différé: ayant utilisé pour réaliser mes compositions, depuis fort longtemps, des environnements de programmation appartenant à la famille Music N». La decorrelation è nata in deferred time, e poi *estesa* al real-time («plus tard, j'ai utilisé des objets logiciels pour régler les offsets et les variations micro temporelles en temps réel», p. 7) — pattern identico a quello di PGE: il differido è lo spazio nativo dell'operazione, il real-time è un'estensione opzionale.

4. **Distinzione tra panning e decorrelation come distinzione architetturale PGE**: Vaggione separa nettamente *panning* (campo stabile, sincronico, esterno) e *decorrelation* (campo dinamico, multi-locale, interno alle morfologie). PGE oggi assegna il pan via `VoiceConfig.pan` (strategia per-voce) e dephase via `Controller` — combinazione che realizza, nei termini di Vaggione, la decorrelation propriamente detta, non un semplice panning.

5. **Esplicito richiamo a Vaggione 1996** (p. 8): Vaggione 2002 cita esplicitamente la quote-pietra-angolare *déclaration d'attribut généralisé* del 1996 come fondamento metodologico anche della decorrelation. Conferma che il principio è la *colonna vertebrale* della pratica Vaggione, valido tanto per altezze (1996) quanto per spazio (2002).

6. **Micromontage come prerequisito** (p. 7): «même si on utilise des techniques de décorrélation massivement basées sur des procédures d'analyse/resynthèse, on sera bien obligés de passer par des micromontages afin de construire des ensembles musicaux d'une certaine complexité» (rinvio a Roads 2002 *Microsound* cap. 5). Conferma il primato del micromontaggio come tecnica abilitante — primato che PGE eredita strutturalmente con il workflow STEMS.

## Collegamento alla tesi centrale
Vaggione 2002 dà il termine alla micromodulazione del quarto angolo del 2×2
(`sec:deviazione`, cfr. [[deviazione-ampiezza-probabilita]]): la
*décorrélation microtemporelle* tratta gli scarti di millisecondi fra voci e
grani come attributo morfologico-spaziale di prima classe, non come effetto
aggiunto in post. Nel lessico del paper: la deviazione per grano e
l'indipendenza delle voci non sono opzioni di spazializzazione ma parte della
scrittura — il fenomeno che i due gemelli di `sec:deviazione` e lo `scatter`
di `sec:voci` rendono udibile e leggibile in partitura. Sul piano compositivo,
il montaggio multitraccia praticato da Vaggione è il parente della terza
proposta (workflow per stem, `sec:tradizione`).

Vaggione 2002 conferma inoltre la trasversalità della postura indeterministica
fra deferred e real-time (in continuità con Di Scipio 1994): le decisioni sono
guidate da criteri morfologici (multi-locale, time-varying), non dal regime
temporale in sé. La decorrelazione resta valida in entrambi i regimi; il paper
sceglie il differito per le ragioni argomentate in `sec:implicazioni`.

## Concetti correlati

- [[decorrelazione-granulare]] — sintesi cross-source della filiazione CIM → CMR (Keller-Rolfe 1998 → Rolfe-Keller 2000 → Vaggione 2002) e mapping completo su PGE

## Sezioni del paper CIM 2026 dove citare

- **`sec:deviazione`** (primaria): *décorrélation microtemporelle* come
  termine della micromodulazione — quarto angolo del 2×2, cfr.
  [[deviazione-ampiezza-probabilita]].
- **`sec:tradizione`** (secondaria): piano compositivo della decorrelazione;
  montaggio multitraccia come parente del workflow stem.

Fonte di verità: [[mappa-citazioni-paper]].

## Quote chiave

> «en travaillant dans le cadre d'une situation typique de "studio numérique", c'est-à-dire en temps différé: ayant utilisé pour réaliser mes compositions, depuis fort longtemps, des environnements de programmation appartenant à la famille Music N» (p. 3) — *deferred time come contesto nativo della pratica.*

> «La décorrélation [...] ne peut se séparer des caractéristiques morphologiques des sources. [...] La durée des sons est également un facteur important, ainsi que la densité spectrale (brillance) et les caractéristiques d'évolution temporelle. De plus, le panning n'a pas besoin d'informations concernant la phase des sons auxquels il est appliqué» (p. 9) — *distinzione panning vs decorrelation come distinzione architetturale.*

> «la décorrélation entre diverses pistes contenant le même son ne va pas nécessairement causer des phénomènes de distorsion globale de phase. Elle va plutôt engendrer une grande quantité de différences locales de phase, négatives et positives, qui se succèdent rapidement. C'est cette relation kaléidoscopique ("multi-locale") qui contribue à instaurer une dynamique spatiale» (p. 7) — *fondazione teorica del dephase per-grano + offsets per-voce.*

> «Une figure musicale peut être considérée comme le produit d'articulations singulières, véhiculant des propriétés morphologiques, sur lesquelles on peut réaliser des opérations diverses [Vaggione 1996]. Quand je parle de figuration, je veux signifier la composition de champs de figures musicales ayant chacune des traits singuliers. Les attributs concernant la perception spatiale font partie de ces traits singuliers, au même titre que ceux concernant d'autres catégories et dimensions composables (hauteur, durée, densité, etc.)» (p. 10) — *legame esplicito 2002 ↔ 1996 e statuto del parametro spaziale come dimensione composable.*
