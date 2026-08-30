# [Di Scipio, 1991] Caos deterministico, composizione e sintesi del suono

## Citazione CIM
Di Scipio, A. (1991). Caos deterministico, composizione e sintesi del suono. In *Atti del IX Colloquio di Informatica Musicale*, pp. 337–349. Genova: AIMI / DIST Università di Genova.

## Categoria e lunghezza
Comunicazione scientifica — 13 pagine (pp. 337–349) — 22 riferimenti bibliografici (sezione *References* alle pp. 348–349).

## Argomento centrale
Sistemi dinamici non-lineari (iterazioni monoparametriche, mappe logistiche/Hénon) come strumento di controllo unitario su livello simbolico (selezione macro-strutturale di elementi musicali) e sub-simbolico (parametri di grani sonori: ampiezza, durata, frequenza, posizione nel buffer). Tesi: dialettica ordine/disordine intrinseca a questi modelli legittima un approccio compositivo in cui la macroforma emerge dall'auto-organizzazione del materiale.

## Sistema o strumento descritto
Procedure di sintesi/granulazione implementate su **IBM PC 286**, in linguaggio non specificato per la granulazione (MUSIC360 citato solo per FM a tripla portante in *fractus*). Inviluppi granulari ottenuti come `|sin(2πω₀t)|^p` e complementare (p. 345). Brani citati: *fractus* (1989/90, viola+nastro), *ikon* (1991, 4 tracce).

## Analogia con PGE

**Divergenza fondamentale sul modello di controllo parametrico.** Di Scipio usa mappe caotiche deterministiche (logistica, Verhulst, Hénon): `xn+1 = f(xn)`, valore successivo dipende dal precedente, traiettoria deterministica ma caotica. Prima formulazione CIM della sotto-famiglia (A) caotico-iterativa del filone [[granulare-deterministico-cim]] (continuata in [[rizzuti2006]]; sotto-famiglia (B) combinatoria MUX in [[silvestri2010]]). PGE usa **maschere di tendenza** (tendency masks, lineage Truax 1988; cfr. [[tendency-mask]]): per ogni parametro l'utente specifica un offset (centro) e un range di deviazione su distribuzione uniforme o gaussiana — deterministico nel processo, statistico nella generazione del valore. Non c'è memoria tra grano `n` e `n+1`: ogni valore è campionato indipendentemente dalla distribuzione specificata. I due regimi appartengono a famiglie diverse di controllo algoritmico (caos iterativo vs. distribuzione campionata) e non sono varianti dello stesso pattern.

Conseguenza: né `ParameterOrchestrator` né `PointerController` di PGE sono generalizzazione del pattern di Di Scipio. "Riscalare xn entro un vettore V" (p. 342) e "xn riscalato sul numero di campioni" (pp. 344-345, granulazione di suoni numerici) descrivono entrambi la stessa famiglia caotico-iterativa applicata rispettivamente ai parametri di grano e alla posizione di lettura nel buffer. PGE applica tendency mask sia ai parametri di grano (`ParameterOrchestrator`) sia alla posizione di lettura (`PointerController`: Envelope su `loop_start`/`loop_end`/`speed_ratio` + range stocastico campionato grano per grano, indipendenza fra grani). Famiglie opposte di controllo, stesso problema (controllo unitario su parametri di grano + posizione di lettura in deferred time), scelte algoritmiche divergenti.

Resta un solo vettore di analogia diretta:

**Tempo differito dichiarato esplicitamente.** P. 345: *"Queste procedure sono attualmente implementate in tempo differito, su un IBM PC 286."* Riga dopo: *"un problema attualmente insormontabile sta nella quantità di RAM nella quale il segnale da ridurre in grani è conservato […]; la memoria indirizzabile dai DSP in commercio è molto più ridotta, e non rende ottenibili, per ora, i risultati realizzabili in tempo differito."* Formulazione canonica CIM del **vincolo hardware** che fonda l'atto 1 della narrazione del paper CIM 2026: deferred time non come scelta ma come necessità tecnica. PGE rovescia il segno: stesso modo operativo (offline), motivazione opposta (postura compositiva, non vincolo).

## Posizionamento storico
Filone CIM **offline / deferred time / controllo algoritmico parametri granulari**. Si colloca tra:
- Roads 1985 (CIM VI) — primo paper CIM su granular synthesis, framing offline, problema d·n parametri.
- De Poli/Piccialli 1988 (CIM VII) — sintesi granulare sincrona offline.
- Ortosecco/Piccialli 1989 (CIM VIII) — granular + wavelets, offline.
- Di Scipio 1991 (questo paper) — **chiude la fase offline-su-microcomputer**; menziona già limiti DSP per real-time su suoni campionati.
- Di Scipio/Tisato 1993 (CIM X, cfr. [[discipio-tisato1993]]) — ICMS mainframe IBM 9121, ancora **deferred time**, ma su sistema più maturo + programma DSL ante litteram («*step towards the abstract*», p. 165). Real-time NeXT annunciato come *"in the near future"* ma non realizzato nel paper.
- Lippe 1993 (CIM X, stesso volume) — IRCAM ISPW, **real-time** su workstation DSP dedicata. Punto di transizione effettiva.

Di Scipio 1991 è il punto di articolazione: stesso autore enuncia il vincolo hardware nel 1991 e prosegue su ICMS deferred nel 1993 (CIM X), mentre la transizione real-time arriva nello stesso volume via Lippe/ISPW.

## Note stilistiche
- **Struttura**: Introduzione (problema storico/concettuale) → Proprietà dei sistemi non-lineari (formale, con equazioni numerate) → Sulla composizione di *fractus* (caso applicativo macro) → Procedure di sintesi del suono (caso applicativo micro) → Considerazioni e prospettive.
- **Tono**: argomentativo-formale. Le equazioni sono numerate ([eq.1]–[eq.8]); le figure (7) sono richiamate nel testo con riferimenti puntuali; pochissime quote da altri autori (Brün in esergo, Schaeffer, Truax).
- **Densità citazioni**: 22 riferimenti, mix DSP + composizione + cognizione + epistemologia dei sistemi complessi. Tre filoni: (a) DSP/sintesi (Jones/Parks 1988, Roads 1985, Truax 1987/1990, De Poli/Piccialli/Roads 1991, Arfib 1990); (b) sistemi non-lineari e caos (Collet/Eckmann 1980, Gleick 1987, Carmona/Nualart 1989, Degazio 1986, Pressing 1988, Dewdney 1991, Prigogine/Stengers 1988, von Foerster 1985, Maturana/Varela 1980); (c) cognizione/estetica (McAdams 1987/1989, Schaeffer 1966, Brün 1966, Duchez 1991). Pattern che PGE/CIM 2026 può ereditare: bibliografia che alterna riferimenti tecnici e riferimenti compositivi/estetici, con il filone epistemologico (Prigogine, von Foerster, Maturana) come terzo asse argomentativo.
- **Apertura**: esergo Brün ("Music […] preserves at least traces of the processes by which it emerged from chaos") che dichiara la postura concettuale prima di entrare nel formalismo. Apertura adoperabile come modello: epigrafe + paragrafo che situa storicamente il problema.
- **Chiusura**: paragrafo metariflessivo su "approccio sub-simbolico", legato alla cognizione (filtro percettivo McAdams) — collega micro e macro per via cognitiva, non tecnica. Modello argomentativo riusabile per la conclusione del paper CIM 2026 (loop lungo come postura, non come tecnica).

## Sezioni del paper CIM 2026 dove citare

- **non citato nel paper** («tradizione», sezione rimossa e confluita in `sec:conclusioni`): famiglia di controllo caotica come
  alternativa affiancata dentro la tradizione offline (contrasto controllato).

Fonte di verità: [[mappa-citazioni-paper]].

## Quote chiave
- *"La quantità di dati da gestire attraverso elaboratore - i parametri relativi a migliaia di grani sonori - è tale da richiedere approcci di tipo statistico (Roads, 1985; Truax, 1987). Per questo, la necessità di ideare eventi acustici complessi nel dettaglio con mezzi operativi efficaci, ha suggerito l'impiego di sistemi dinamici non-lineari"* (p. 344) — formulazione esplicita del problema `d·n` (numero parametri × numero grani) che motiva il controllo gerarchico, identico al razionale del DSL YAML PGE.
- *"Il principio generale adottato è quello di riscalare l'intervallo di iterazione di un dato sistema dinamico non-lineare in modo che coincida con lo spazio discreto di un vettore V di elementi numerabili. Il valore xn, che descrive lo stato istantaneo nell'evoluzione del sistema, coincide allora con uno degli elementi V(i), cioè lo seleziona."* (p. 342) — pattern operativo caotico-iterativo, **non** generalizzato da PGE: `ParameterOrchestrator` campiona da tendency mask statistica (offset + range, distribuzione uniforme/gaussiana), senza dipendenza `xn → xn+1`. Quote da citare per contrasto, non per continuità.
- *"Nella granulazione di suoni già in forma numerica, xn è riscalato sul numero dei campioni che descrivono il suono originale; il campione così selezionato viene considerato il primo campione del grano n-esimo."* (pp. 344–345) — applicazione della stessa famiglia caotico-iterativa alla posizione di lettura nel buffer. **Non** precursore di `PointerController` PGE: PGE seleziona la posizione di lettura via tendency mask (Envelope `loop_start/loop_end/speed_ratio` + range stocastico, indipendenza fra grani), regime opposto. Quote da citare per contrasto controllato, non per continuità.
- *"Queste procedure sono attualmente implementate in tempo differito, su un IBM PC 286. In una eventuale implementazione in tempo reale non esisterebbero problemi legati al calcolo delle iterazioni monoparametriche […]. Per la granulazione di suoni reali, invece, un problema attualmente insormontabile sta nella quantità di RAM nella quale il segnale da ridurre in grani è conservato"* (p. 345) — **pietra angolare per atto 1 narrazione**: vincolo hardware esplicito, non scelta estetica.
