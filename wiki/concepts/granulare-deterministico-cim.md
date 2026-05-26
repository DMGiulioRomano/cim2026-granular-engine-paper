# Granulare deterministico CIM — filone e sotto-famiglie

## Definizione

Sottoinsieme della tradizione CIM (Colloquio di Informatica Musicale) di sintesi granulare in cui il controllo dei parametri di grano e/o della sequenza temporale dei grani è **deterministico**, ottenuto rifiutando esplicitamente i generatori di numeri casuali come motore di varietà. La varietà è prodotta da meccanismi formali interni al sistema: iterazione di funzioni non-lineari, reti combinatorie di commutazione, mappe parametriche.

Posizione rispetto al canone Roads/Truax: il canone (Roads 1978/1988, Truax 1988/1990/1994) usa controllo statistico — tendency mask + distribuzione campionata grano per grano (cfr. [[tendency-mask]]). Il filone granulare deterministico CIM si pone come **alternativa di principio**: stessi obiettivi (controllo unitario su `d·n` parametri × grani), meccanismi formali opposti.

## Sotto-famiglie

Il filone si articola in due sotto-famiglie distinte per **tipologia del meccanismo formale**:

### (A) Caotico-iterativo — `xn+1 = f(xn)`

Mappa monoparametrica (logistica, Verhulst, Hénon) iterata; lo stato successivo dipende dal precedente; traiettoria deterministica ma caotica al variare del parametro di controllo.

- **[[discipio1991]]** (CIM IX 1991): prima formulazione CIM. Logistica/Verhulst/Hénon, controllo unitario su livello simbolico (macro-struttura) e sub-simbolico (ampiezza, durata, frequenza, posizione di lettura nel buffer). IBM PC 286 offline. Quote pietra-angolare p. 342: *"riscalare l'intervallo di iterazione [...] in modo che coincida con lo spazio discreto di un vettore V"*.
- **[[rizzuti2006]]** (CIM XVI 2006): restringe alla sola logistica `xt+1 = c·xt·(2 − xt)`, la promuove a principio architetturale. CSound offline, due strumenti (eventi + grani). 15 anni dopo Di Scipio 1991, in piena disponibilità real-time CIM, rivendica esplicitamente l'offline+deterministico.

### (B) Combinatoria deterministica — multiplexer/permutazioni

Nessuna iterazione `xn → xn+1`. Il grano è **prodotto incidentale** di una rete combinatoria che commuta sub-vettori da oscillatori paralleli; la finestratura definisce velocità e durata del quanto, l'apparato di commutazione decreta l'ordinamento temporale.

- **[[silvestri2010]]** (CIM XVIII 2010): wavetable switching per multiplexing. N oscillatori wavetable look-up paralleli + inviluppi sfasati $\phi_n + \Delta t/T_{env}$ + emulatore multiplexer N-bit (rete combinatoria AND/NOT/OR). Csound + Pure Data. Inquadramento esplicito p. 209 come *"forma di sintesi granulare deterministica dove operazioni quali lettura e finestratura rappresentano la generazione del grano [...] mentre l'apparato di commutazione è ciò che guida i parametri del grano stesso"*. Single data-point della sotto-famiglia (al 2026-05).

## Relazione con PGE

**Anti-precursore strutturale.** PGE implementa [[tendency-mask]] statistico: ogni valore parametrico al grano `n+1` è indipendente dal valore al grano `n` (campionamento i.i.d. da Envelope center + range, distribuzione uniforme/gaussiana, `DistributionStrategy` + `ProbabilityGate`). I tre lavori del filone granulare deterministico CIM sono casi limite **non riducibili** al regime PGE:

| Aspetto | Sotto-famiglia A (Di Scipio, Rizzuti) | Sotto-famiglia B (Silvestri) | PGE |
|---|---|---|---|
| Generatore valore | `xn+1 = f(xn)` | rete combinatoria MUX su sub-vettori | sample i.i.d. da distribuzione |
| Memoria fra grani | sì (stato del sistema) | no (combinatoria su sequenza indirizzi) | no (indipendenza) |
| Grano come entità | prima classe (parametri controllati) | prodotto incidentale (commutazione) | prima classe (`Stream.generate_grains()`) |
| Asse di controllo | traiettoria caotica deterministica | sequenza di indirizzi combinatoria | distribuzione probabilistica time-varying |

PGE è collocabile nella famiglia opposta (statistica) lungo l'asse di controllo, ma condivide col filone deterministico CIM la **postura compositiva offline** — varietà generata internamente dalla specifica formale, non da scelta interattiva real-time del compositore.

## Architetture a due moduli — precursore debole della separazione Stream/grano

Sotto-famiglia A: Rizzuti 2006 separa esplicitamente *strumento generatore di eventi* e *strumento generatore di grani* (entrambi dentro CSound). Di Scipio 1991 menziona la separazione macro-strutturale (selezione elementi) vs sub-simbolica (parametri di grano) ma non la fattorizza in moduli software distinti.

PGE separa specifica YAML (DSL/IR) → `ParameterOrchestrator` → renderer CSound/NumPy. Precursore CIM **diretto** della topologia è [[arcella-silvestri2012]] (`score.cpp C++ → Xscore.txt → Analogique.csd`); il filone granulare deterministico CIM offre la separazione di principio (responsabilità) ma non quella di linguaggio (nessun livello DSL above CSound).

## Cluster sociologici intersecanti

- **Magistero Di Scipio**: tutti e tre i lavori del filone hanno legame diretto col magistero Di Scipio. Di Scipio 1991 (autore stesso); Rizzuti 2006 (filiazione concettuale esplicita, "controllo deterministico vs stocastico"); Silvestri 2010 (tesista I Liv. Cons. S. Pietro a Majella, relatore Di Scipio, A.A. 2008/2009). Continuità di scuola attraverso tre decenni e tre volumi CIM (IX, XVI, XVIII).
- **Lineage napoletano CIM (intersezione con sotto-famiglia B)**: Silvestri 2010 è terzo nodo DSP-orientato dopo [[depoli-piccialli1988]] e [[ortosecco-piccialli1989]]; il lineage napoletano è ortogonale al filone granulare deterministico (De Poli/Piccialli 1988 e Ortosecco/Piccialli 1989 non sono deterministici nel senso qui usato — sincronia, wavelets), si interseca solo via Silvestri.
- **Thread Di Scipio allievi**: Silvestri tesista 2008/2009 → co-autore [[arcella-silvestri2012]] nel volume CIM XIX successivo. Continuità di magistero documentata su due volumi CIM consecutivi (XVIII 2010, XIX 2012).

## Citabilità nel paper CIM 2026

- **Sezione 2 (Sintesi granulare: dal paradigma Gabor al controllo gerarchico)**: introdurre il filone granulare deterministico CIM come **alternativa interna alla tradizione** al canone Roads/Truax stocastico. Citazione collettiva (Di Scipio 1991 + Rizzuti 2006 + Silvestri 2010) come testimonianza che il rifiuto del controllo stocastico non è scelta isolata di PGE ma linea ricorrente CIM. Posizionare PGE nella famiglia opposta (statistica) per **contrasto controllato**, non come superamento. Distinguere le due sotto-famiglie (caotico-iterativo vs combinatoria MUX) per evitare la lettura del filone come blocco omogeneo.
- **Sezione 6 (Conclusioni / metodologia loop lungo)**: Silvestri 2010 *Studio Sonoro III* (nota 10, p. 210) come data-point CIM 2010 della coesistenza tempo reale + tempo differito nella stessa opera — disinnesca la lettura del differito PGE come regressione rispetto al real-time.

## Domande aperte

- Esiste un quarto data-point del filone tra 2012 e 2024? Survey [[cim-survey]] non ne registra al 2026-05 — verificare scansione volumi XX–XXIV.
- Markidis 2024 (CIM XXIV, mediation process) appartiene al filone? Non deterministico in senso `xn+1=f(xn)` né combinatorio MUX, ma ecosistemico. Probabile famiglia distinta — non includere senza ingest mirato.
- Sotto-famiglia (B) ha un solo data-point CIM. Investigare se Silvestri ha continuità di pratica oltre il paper (composizioni successive, ulteriori implementazioni Csound/PD).
