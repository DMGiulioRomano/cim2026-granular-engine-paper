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
Vaggione 2002 fornisce la *legittimazione teorica esplicita* per il livello «per-voice + per-grain dephase» dell'architettura PGE. Non un dettaglio implementativo ma un attributo morfologico-compositivo di prima classe: l'identità spaziale di una figura granulare è costituita dalle decorrelazioni microtemporali tra le sue voci, non aggiunta in post. PGE materializza questa tesi strutturalmente — VoiceManager non è opzione di spazializzazione, è layer architetturale obbligatorio.

Inoltre Vaggione 2002 conferma la *trasversalità della postura indeterministica* tra deferred e real-time (eredita la lezione Di Scipio 1994): le compositional decisions sono determinate da criteri morfologici (multi-locale, time-varying), non dal real-time vs differido come tale. PGE sceglie il differido perché *il loop lungo* è lo spazio di esercizio della scrittura figurale; la tecnica decorrelation di Vaggione resta valida in entrambi i regimi.

## Sezioni del paper CIM 2026 dove citare
- **Sezione 2 Sintesi granulare / paradigma**: decorrelation microtemporelle come tecnica multi-scala addizionale (insieme a granulazione sincrona/asincrona Truax e per-grain processing Roads 2012) — fa parte del catalogo delle operazioni che la postura object-based abilita.
- **Sezione 3 Architettura PGE**: VoiceManager + dephase Controller come implementazione strutturale della *décorrélation microtemporelle*. Differenziatore 7 (per-grain effects processing) si estende a *per-voice microtime decorrelation*: PGE non solo decorrela i parametri di sintesi ma anche le repliche temporali tra voci.
- **Sezione 4 Partitura grafica**: la partitura PGE rende visibile la decorrelation (onset offsets per voce, dephase per grano sono osservabili come scarti orizzontali tra grani) — non solo asse Y posizione-buffer, ma anche asse X come rivelatore di figure spaziali.
- **Sezione 5 Caso compositivo**: la decorrelation come strumento compositivo di figurazione spaziale può essere illustrata da una scelta motivata visivamente nel brano PGE.

## Quote chiave

> «en travaillant dans le cadre d'une situation typique de "studio numérique", c'est-à-dire en temps différé: ayant utilisé pour réaliser mes compositions, depuis fort longtemps, des environnements de programmation appartenant à la famille Music N» (p. 3) — *deferred time come contesto nativo della pratica.*

> «La décorrélation [...] ne peut se séparer des caractéristiques morphologiques des sources. [...] La durée des sons est également un facteur important, ainsi que la densité spectrale (brillance) et les caractéristiques d'évolution temporelle. De plus, le panning n'a pas besoin d'informations concernant la phase des sons auxquels il est appliqué» (p. 9) — *distinzione panning vs decorrelation come distinzione architetturale.*

> «la décorrélation entre diverses pistes contenant le même son ne va pas nécessairement causer des phénomènes de distorsion globale de phase. Elle va plutôt engendrer une grande quantité de différences locales de phase, négatives et positives, qui se succèdent rapidement. C'est cette relation kaléidoscopique ("multi-locale") qui contribue à instaurer une dynamique spatiale» (p. 7) — *fondazione teorica del dephase per-grano + offsets per-voce.*

> «Une figure musicale peut être considérée comme le produit d'articulations singulières, véhiculant des propriétés morphologiques, sur lesquelles on peut réaliser des opérations diverses [Vaggione 1996]. Quand je parle de figuration, je veux signifier la composition de champs de figures musicales ayant chacune des traits singuliers. Les attributs concernant la perception spatiale font partie de ces traits singuliers, au même titre que ceux concernant d'autres catégories et dimensions composables (hauteur, durée, densité, etc.)» (p. 10) — *legame esplicito 2002 ↔ 1996 e statuto del parametro spaziale come dimensione composable.*
