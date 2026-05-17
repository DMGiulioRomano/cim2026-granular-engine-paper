# [Vaggione, 1996] Vers une approche transformationnelle en CAO

## Citazione CIM
Vaggione, H. (1996). Vers une approche transformationnelle en CAO. In *Actes des Journées d'Informatique Musicale (JIM 1996)*, île de Tatihou, mai 1996. Caen: Les Cahiers du GREYC, CNRS-Université de Caen. (HAL hal-02986472, 9 pp.)

## Argomento centrale
Manifesto dell'*interaction forte* tra écriture directe (intervento manuale, scelte sempre singolari) e traitement algorithmique (generalizzazione/propagazione di vincoli) come condizione metodologica della CAO. Vaggione formula una *prospettiva trasformazionale*: ogni gesto locale può essere dichiarato come attributo di una classe e propagato algoritmicamente; ogni risultato algoritmico può essere ri-toccato manualmente. Il testo presenta poi due tecniche di trasformazione figurale macroscopica importate dal signal processing — convolution e distorsione non lineare (waveshaping) — come *prismi modulanti* alternativi a permutazioni combinatoriali o variazioni stocastiche.

## Gap o problema identificato
- I «jeux de miroirs» classici (retrograduazione, inversione) sono operazioni *strettamente lineari* — citato Xenakis 1979 sulle manipolazioni inconsce dei gruppi di Klein. La relativizzazione delle altezze tonali apre la necessità di trasformazioni non-lineari, topologiche, vettoriali.
- I tassi o percentuali di variazione (linguaggi stocastici) sono «palliatifs au manque de visée proprement figurale» — non sostituiscono il lavoro morfologico su saillances.
- Critica al timbro come «couleur ajoutée»: la scrittura tradizionale ignora che il timbro non è trasponibile (cita Erehsman-Wessel 1978, Wessel 1979) — l'identità di una figura non si conserva sotto trasposizione, perché muta il substrato spettrale.

## Rilevanza diretta per PGE
1. **Quote-pietra-angolare per il differenziatore DSL** (sezione *Ecriture directe et traitement algorithmique*, p. 2): «toute intervention directe peut être considérée comme la déclaration d'un attribut particulier d'une entité quelconque; cet attribut peut dès lors être généralisé à toutes les instances successives de cette entité, et non pas rester isolé dans la localité d'une seule instance — au moins que soit ceci le cas désiré. Ainsi une action locale d'écriture a bien la possibilité de s'intégrer dans un processus algorithmique, de la même façon dont, symétriquement, le produit d'un processus algorithmique peut être transformé localement par une action d'écriture directe. De cette symétrie s'en suit une imbrication des deux possibilités d'action, sans qu'aucune ait à souffrir d'une inféodation à l'autre, pouvant au contraire amplifier mutuellement leurs implications, intégrant choix et contrainte, changement et héritage, localité et vectorisation.»

   Questo passaggio è la *legittimazione argomentativa* più precisa del DSL YAML di PGE: un valore YAML è una *déclaration d'un attribut*; un envelope o una strategy è la sua *généralisation à toutes les instances*; la modifica successiva di un singolo valore è l'écriture directe che si imbriqua nel risultato algoritmico. ParameterOrchestrator non sostituisce la scrittura manuale: la propaga.

2. **Loop lungo come imbrication tra modi**: la simmetria écriture↔algoritmo richiede di fatto un ciclo di feedback per esercitare entrambi i poli. La specifica YAML → generazione grani → ascolto → editing della specifica è la realizzazione tecnica dell'*imbrication* descritta da Vaggione.

3. **Tahil (1992) e Kitab (1992) come precedenti compositivi**: Vaggione dichiara di usare il pattern object-based + transformational anche per opere puramente strumentali (Tahil, piano solo) o miste (Kitab). Conferma che la *postura* non dipende dalla scala temporale specifica del rendering, ma dalla configurazione del flusso di lavoro. (Date dalla lista opere autorata in Vaggione 2003, ch. 4 p. 104; in Vaggione 1996 non sono specificate.)

4. **Convolution come synthèse croisée macroscopica e distorsion non linéaire come *prisme modulant*** (sezione *Convolution, distorsion non linéaire*, pp. 4-6): non implementate direttamente in PGE, ma indicano un'orizzonte di estensione del ParameterOrchestrator (cross-modulation di figure attraverso operatori trasformazionali). Da menzionare in *sviluppi futuri* (sezione 6) se rilevante.

5. **Critica esplicita ai tassi/percentuali stocastici** (p. 4): «taux ou pourcentages de variation, qui sont souvent utilisés comme des palliatifs au manque de visée proprement figurale». PGE evita questo rischio mantenendo il visualizer come strumento di lettura figurale post-synthesis: il compositore non valuta uno stream da «percentuali» ma da *figure* osservate.

## Collegamento alla tesi centrale
Vaggione 1996 fornisce la *cornice metodologica* del loop lungo: l'*interaction forte* è precisamente il flusso di feedback specifica → generazione → ascolto → riflessione → riscrittura, ma articolata come imbrication strutturale tra polo manuale e polo algoritmico, non come scelta esclusiva. PGE eredita la simmetria: la modalità tempo differito non è scelta perché l'algoritmico sia inadeguato, ma perché la *réflexion entre cycles* è lo spazio di esercizio della scrittura diretta sul risultato algoritmico.

La quote-pietra-angolare sull'attributo dichiarato/generalizzato è il complemento perfetto al programma DSL Roads 2001 cap. 1 («musical interface in which a musician specifies the desired sonic result in a musically descriptive language»): Roads articola la visione macro del linguaggio; Vaggione articola la meccanica fine della *dichiarazione di attributo propagato*. Insieme costituiscono la doppia radice teorica del differenziatore 1 di PGE.

## Sezioni del paper CIM 2026 dove citare
- **Sezione 1 Introduzione**: l'*interaction forte* come quadro metodologico del loop lungo; legame con la tesi tempo differito = postura, non vincolo.
- **Sezione 3 Architettura PGE**: la quote-pietra-angolare *déclaration d'attribut généralisé* come fondamento argomentativo del DSL + ParameterOrchestrator + envelope time-varying. Critica ai tassi/percentuali come *palliatifs* — legittimazione del visualizer figurale.
- **Sezione 5 Caso compositivo**: precedente di Tahil/Kitab come opere costruite per «réseau d'objets logiciels» con cicli iterativi di scrittura/propagazione.
- **Sezione 6 Conclusioni / sviluppi futuri** (eventuale): convolution e DNL macroscopica come orizzonti di estensione del ParameterOrchestrator.

## Quote chiave

> «toute intervention directe peut être considérée comme la déclaration d'un attribut particulier d'une entité quelconque; cet attribut peut dès lors être généralisé à toutes les instances successives de cette entité [...]. De cette symétrie s'en suit une imbrication des deux possibilités d'action, sans qu'aucune ait à souffrir d'une inféodation à l'autre, pouvant au contraire amplifier mutuellement leurs implications, intégrant choix et contrainte, changement et héritage, localité et vectorisation» (p. 2)

> «taux ou pourcentages de variation, qui sont souvent utilisés comme des palliatifs au manque de visée proprement figurale» (p. 4)

> «la condition première qui sous-tend une telle démarche étant le fait d'une "interaction forte" entre écriture directe et traitement algorithmique» (conclusione, p. 7)

> «en milieu numérique — et dans un sens strict — "tout est texte": même le son est texte, avant de passer par la conversion numérique-analogique» (p. 4) — *anticipo della tesi "YAML come IR" del paper CIM: la specifica testuale non si oppone al sonoro, ne è il duale numerico.*
