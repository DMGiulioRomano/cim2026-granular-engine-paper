# Granulare deterministico CIM — filone e sotto-famiglie

## Definizione

Sottoinsieme della tradizione CIM (Colloquio di Informatica Musicale) di sintesi granulare in cui il controllo dei parametri di grano e/o della sequenza temporale dei grani è **deterministico**, ottenuto rifiutando esplicitamente i generatori di numeri casuali come motore di varietà. La varietà è prodotta da meccanismi formali interni al sistema: iterazione di funzioni non-lineari, reti combinatorie di commutazione, mappe parametriche.

Posizione rispetto al canone Roads/Truax: il canone (Roads 1978/1988, Truax 1988/1990/1994) usa controllo statistico — tendency mask + distribuzione campionata grano per grano (cfr. [[tendency-mask]]). Il filone granulare deterministico CIM si pone come **alternativa di principio**: stessi obiettivi (controllo unitario su `d·n` parametri × grani), meccanismi formali opposti.

## Sotto-famiglie

Il filone si articola in tre sotto-famiglie distinte per **tipologia del meccanismo formale**:

### (A) Caotico-iterativo — `xn+1 = f(xn)`

Mappa monoparametrica (logistica, Verhulst, Hénon) iterata; lo stato successivo dipende dal precedente; traiettoria deterministica ma caotica al variare del parametro di controllo.

- **[[discipio1991]]** (CIM IX 1991): prima formulazione CIM. Logistica/Verhulst/Hénon, controllo unitario su livello simbolico (macro-struttura) e sub-simbolico (ampiezza, durata, frequenza, posizione di lettura nel buffer). IBM PC 286 offline. Quote pietra-angolare p. 342: *"riscalare l'intervallo di iterazione [...] in modo che coincida con lo spazio discreto di un vettore V"*.
- **[[rizzuti2006]]** (CIM XVI 2006): restringe alla sola logistica `xt+1 = c·xt·(2 − xt)`, la promuove a principio architetturale. CSound offline, due strumenti (eventi + grani). 15 anni dopo Di Scipio 1991, in piena disponibilità real-time CIM, rivendica esplicitamente l'offline+deterministico.

### (B) Combinatoria deterministica — multiplexer/permutazioni

Nessuna iterazione `xn → xn+1`. Il grano è **prodotto incidentale** di una rete combinatoria che commuta sub-vettori da oscillatori paralleli; la finestratura definisce velocità e durata del quanto, l'apparato di commutazione decreta l'ordinamento temporale.

- **[[silvestri2010]]** (CIM XVIII 2010): wavetable switching per multiplexing. N oscillatori wavetable look-up paralleli + inviluppi sfasati $\phi_n + \Delta t/T_{env}$ + emulatore multiplexer N-bit (rete combinatoria AND/NOT/OR). Csound + Pure Data. Inquadramento esplicito p. 209 come *"forma di sintesi granulare deterministica dove operazioni quali lettura e finestratura rappresentano la generazione del grano [...] mentre l'apparato di commutazione è ciò che guida i parametri del grano stesso"*. Single data-point della sotto-famiglia (al 2026-05).

### (C) Combinatoria a-causale — permutazione di chunk

Nessuna iterazione `xn → xn+1`, nessuna rete combinatoria su sub-vettori di oscillatori paralleli. Il pattern di riordinamento è dichiarato esplicitamente come parametro di sintesi e applicato a chunk fissi del buffer di ingresso. Determinismo *a-causale*: lo stato al chunk `n+1` non dipende dallo stato al chunk `n` né da una funzione iterata, ma dall'indice di permutazione fissato a priori.

- **[[valenti-valle-servetti2014]]** (CIM XX 2014): permutation synthesis. Plugin SuperCollider (`PermUGen` / `PermMod` / `PermModArray`); chunk size = `fs/fp` arrotondato all'intero (con time-quantisation error formalizzato sez. 2.2). Posizionamento esplicito sez. 1 contro il canone granulare-stocastico-envelopato: *"most granulation approaches operate by applying an envelope, thus eliminating most of the discontinuities. Moreover, grains are typically scattered in time following some stochastic distributions. On the contrary, in permutation synthesis time discontinuities are the main feature, and the scrambling process is organised following a precise time-pattern"* (p. 35). Roads *Microsound* citato come riferimento contrapposto in ref [1]. Anti-analogia su entrambi i meccanismi-cardine PGE (envelope + distribuzione). Continuità autoriale Valle CIM 11 anni dopo [[valle-lombardo2003]]. Single data-point della sotto-famiglia (al 2026-05).

## Relazione con PGE

**Anti-precursore strutturale.** PGE implementa [[tendency-mask]] statistico: ogni valore parametrico al grano `n+1` è indipendente dal valore al grano `n` (campionamento i.i.d. da Envelope center + range, distribuzione uniforme/gaussiana, `DistributionStrategy` + `ProbabilityGate`). I quattro lavori del filone granulare deterministico CIM sono casi limite **non riducibili** al regime PGE:

| Aspetto | Sotto-famiglia A (Di Scipio, Rizzuti) | Sotto-famiglia B (Silvestri) | Sotto-famiglia C (Valenti/Valle/Servetti) | PGE |
|---|---|---|---|---|
| Generatore valore | `xn+1 = f(xn)` | rete combinatoria MUX su sub-vettori | pattern di permutazione fissato a priori | sample i.i.d. da distribuzione |
| Memoria fra grani | sì (stato del sistema) | no (combinatoria su sequenza indirizzi) | no (lookup su pattern dichiarato) | no (indipendenza) |
| Grano come entità | prima classe (parametri controllati) | prodotto incidentale (commutazione) | prodotto incidentale (chunk a confine fisso) | prima classe (`Stream.generate_grains()`) |
| Asse di controllo | traiettoria caotica deterministica | sequenza di indirizzi combinatoria | sequenza dichiarata `fp` + chunk_size | distribuzione probabilistica time-varying |

PGE è collocabile nella famiglia opposta (statistica) lungo l'asse di controllo, ma condivide col filone deterministico CIM la **postura compositiva offline** — varietà generata internamente dalla specifica formale, non da scelta interattiva real-time del compositore.

## Architetture a due moduli — precursore debole della separazione Stream/grano

Sotto-famiglia A: Rizzuti 2006 separa esplicitamente *strumento generatore di eventi* e *strumento generatore di grani* (entrambi dentro CSound). Di Scipio 1991 menziona la separazione macro-strutturale (selezione elementi) vs sub-simbolica (parametri di grano) ma non la fattorizza in moduli software distinti.

PGE separa specifica YAML (DSL/IR) → `ParameterOrchestrator` → renderer CSound/NumPy. Precursore CIM **diretto** della topologia è [[arcella-silvestri2012]] (`score.cpp C++ → Xscore.txt → Analogique.csd`); il filone granulare deterministico CIM offre la separazione di principio (responsabilità) ma non quella di linguaggio (nessun livello DSL above CSound).

## Cluster sociologici intersecanti

- **Magistero Di Scipio (sotto-famiglie A+B)**: tutti i lavori delle sotto-famiglie A e B hanno legame diretto col magistero Di Scipio. Di Scipio 1991 (autore stesso); Rizzuti 2006 (filiazione concettuale esplicita, "controllo deterministico vs stocastico"); Silvestri 2010 (tesista I Liv. Cons. S. Pietro a Majella, relatore Di Scipio, A.A. 2008/2009). Continuità di scuola attraverso tre decenni e tre volumi CIM (IX, XVI, XVIII). La sotto-famiglia C resta fuori da questo cluster.
- **Continuità autoriale Valle CIM (sotto-famiglia C)**: Andrea Valle attraversa due famiglie granulari CIM in 11 anni — [[valle-lombardo2003]] (architettura formale CAC offline GeoGraphy, *non* deterministica nel senso qui usato) e [[valenti-valle-servetti2014]] (sotto-famiglia C deterministica a-causale). La sotto-famiglia C condivide solo l'autore con la traiettoria Valle-Lombardo, non il magistero Di Scipio che attraversa A+B.
- **Lineage napoletano CIM (intersezione con sotto-famiglia B)**: Silvestri 2010 è terzo nodo DSP-orientato dopo [[depoli-piccialli1988]] e [[ortosecco-piccialli1989]]; il lineage napoletano è ortogonale al filone granulare deterministico (De Poli/Piccialli 1988 e Ortosecco/Piccialli 1989 non sono deterministici nel senso qui usato — sincronia, wavelets), si interseca solo via Silvestri.
- **Thread Di Scipio allievi**: Silvestri tesista 2008/2009 → co-autore [[arcella-silvestri2012]] nel volume CIM XIX successivo. Continuità di magistero documentata su due volumi CIM consecutivi (XVIII 2010, XIX 2012).

## Citabilità nel paper CIM 2026

- **Sezione 2 (Sintesi granulare: dal paradigma Gabor al controllo gerarchico)**: introdurre il filone granulare deterministico CIM come **alternativa interna alla tradizione** al canone Roads/Truax stocastico. Citazione collettiva (Di Scipio 1991 + Rizzuti 2006 + Silvestri 2010 + Valenti/Valle/Servetti 2014) come testimonianza che il rifiuto del controllo stocastico non è scelta isolata di PGE ma linea ricorrente CIM. Posizionare PGE nella famiglia opposta (statistica) per **contrasto controllato**, non come superamento. Distinguere le tre sotto-famiglie (caotico-iterativo / combinatoria MUX / permutation a-causale) per evitare la lettura del filone come blocco omogeneo: stesso obiettivo (rifiuto del controllo stocastico), tre meccanismi formali distinti.
- **Sezione 6 (Conclusioni / metodologia loop lungo)**: Silvestri 2010 *Studio Sonoro III* (nota 10, p. 210) come data-point CIM 2010 della coesistenza tempo reale + tempo differito nella stessa opera — disinnesca la lettura del differito PGE come regressione rispetto al real-time.

## Domande aperte

- Markidis 2024 (CIM XXIV, mediation process) appartiene al filone? Non deterministico in senso `xn+1=f(xn)` né combinatorio MUX né permutation a-causale, ma ecosistemico signal-driven. Probabile famiglia distinta — non includere senza ingest mirato (cfr. [[markidis2024]]: granulator come sotto-componente di ecosistema audio-feedback, non motore primario).
- Sotto-famiglie (B) e (C) hanno entrambe un solo data-point CIM al 2026-05. Da monitorare in future scansioni dei volumi successivi a XXIV 2024. Per (B): investigare se Silvestri ha continuità di pratica oltre il paper (composizioni successive, ulteriori implementazioni Csound/PD). Per (C): verificare se Valle o altri autori CIM proseguono il filone permutation post-2014.
- Esiste un quinto meccanismo formale deterministico nella tradizione CIM oltre i tre censiti? Survey [[cim-survey]] non ne registra al 2026-05.
