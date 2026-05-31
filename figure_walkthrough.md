# figure_walkthrough.md — Lettura guidata della partitura + note di posizionamento

Materiale di lavoro per l'autore. Due parti:
1. **Lettura guidata** di `score_example.png`, in prosa, pronta da adattare e
   innestare in §3 (*La partitura grafica come retroazione*). Chiude la debolezza 1
   (asse esperienziale) e fornisce l'esempio lavorato che oggi manca (debolezza 2).
2. **Tre blocchi paste-ready** per il posizionamento (Vocem foil, EC2, correzione
   frase «frequenza»).

I numeri (tempi, posizioni) vanno **verificati dall'autore** sul rendering reale:
qui sono ripresi dalla descrizione della figura e vanno confermati prima della
submission. Dove il testo propone un *episodio diagnostico*, è un **template** da
riempire con un caso vero — non inventare lo scarto.

---

## Parte 1 — Lettura guidata (bozza per §3)

> *Da inserire dopo la descrizione generale dell'encoding e prima del rinvio alla
> Tab. delle rappresentazioni. Collega la figura, oggi muta, al testo.*

La Fig. (partitura) mostra una finestra di quindici secondi (30–45 s) di un brano a
più stream. Sul margine sinistro la forma d'onda della sorgente è tracciata **in
verticale**, allineata all'asse Y: l'asse di lettura non è una scala astratta ma il
contenuto reale del campione, così che ogni segno si legge come «qui, dentro questo
punto del suono sorgente». L'asse orizzontale è il tempo d'uscita; ogni grano è un
segno collocato alla coppia (istante d'uscita, posizione di lettura), e il colore ne
codifica un parametro per-grano (il pan).

Il pannello superiore apre con una **nuvola larga** (≈30–36 s): i grani sono dispersi
su un ampio intervallo di posizioni di lettura. È la firma visiva di una deviazione
del pointer elevata — il `PointerController` campiona, per ogni grano, un offset
lontano dalla traiettoria centrale. All'ascolto corrisponde una texture diffusa, in
cui il campione è disgregato e la sua identità sorgente è sospesa. Verso i 40–45 s la
nuvola **collassa su una diagonale ascendente nitida**: la deviazione si stringe e la
testina avanza in lettura. Il passaggio da banda a linea rende visibile, in un colpo
d'occhio, la transizione percettiva da granulato indistinto a scansione orientata —
il momento in cui la sorgente torna riconoscibile e il movimento «in avanti dentro il
suono» diventa udibile.

Il pannello centrale mostra una **banda compatta discendente** (≈1.2→0.5 s di
posizione di lettura): qui la deviazione è bassa e la traiettoria del pointer scende
con continuità, una lettura retrograda lenta che l'orecchio segue come un abbassarsi
progressivo del punto d'ascolto nel campione. La densità dei segni — alta e uniforme —
dice che il flusso è fitto e regolare, là dove il pannello superiore era rado e
disperso.

La striscia inferiore allinea, sullo stesso asse temporale, gli inviluppi dei
parametri continui (densità, distribuzione, durata del grano, pan, pitch, volume).
È il livello che spiega *perché* i due pannelli hanno quella forma: l'annotazione del
pan a −30° intorno ai 36 s, per esempio, si legge insieme al viraggio di colore dei
segni nel pannello superiore. La partitura non è un esito decorativo: mette in fila la
dichiarazione (gli inviluppi), la sua realizzazione (i grani) e la posizione di lettura
(l'asse Y), e rende ispezionabile lo scarto fra ciò che il YAML enuncia e ciò che il
rendering produce.

> *Frase di chiusura del paragrafo, opzionale:* È in questo confronto — dichiarazione
> sopra, grani al centro, sorgente di lato — che il loop lungo trova il suo punto di
> appoggio: ciò che l'ascolto coglie a fatica, la partitura lo localizza.

### Episodio diagnostico (TEMPLATE — da riempire con un caso reale)

> *Chiude la debolezza 2 con un'iterazione concreta del loop. Sostituire i segnaposto
> con un episodio vero del proprio lavoro; non usare l'esempio se non è accaduto.*

«Nel pannello centrale, intorno ai ⟨42⟩ s, la banda ⟨si assottiglia/si interrompe⟩:
la partitura segnala un ⟨calo di densità non voluto⟩ là dove l'inviluppo di
`fill_factor` ⟨tocca il minimo⟩. L'ascolto registrava solo un generico
⟨indebolimento⟩; la partitura ne ha mostrato la causa e il punto esatto. La riscrittura
⟨ha alzato il pavimento dell'inviluppo a … ⟩, e il rendering successivo ⟨ha riportato
la banda a densità costante⟩.»

Una sola iterazione di questo tipo — specifica → grani → partitura → scarto → riscrittura
— dimostra la tesi che oggi il paper asserisce soltanto.

---

## Parte 2 — Blocchi paste-ready per il posizionamento

### 2.1 — Vocem come *foil* (verificato sul PDF primario)

> *Da aggiungere in §3, dopo il confronto con Truax Fig. 4 / Roads polygon, e come
> riga nella Tab. delle rappresentazioni. Vocem è il caso che più assomiglia a questo
> sistema — stesso asse Y — e proprio per questo ne isola il differenziatore.*

Testo proposto:

«L'unico precedente che adotta lo stesso asse — la posizione di lettura nel file
sorgente sul verticale — è l'interfaccia del parametro *offset* di Vocem~\cite{Lopez1998},
ambiente granulare in tempo reale: tempo sull'orizzontale, posizione nel campione sul
verticale (0 = inizio, 1 = fine). Là, però, quell'asse ospita una **singola curva di
controllo disegnata in input** — un inviluppo che il compositore traccia per pilotare
la lettura — non i grani prodotti. Vocem non plotta la popolazione granulare, non
mostra la deviazione per-grano, non àncora l'asse alla forma d'onda della sorgente.
La rappresentazione qui descritta inverte il flusso: stesso asse, ma **output**
diagnostico dell'intera nuvola di grani realizzati, non **input** di una traiettoria
ideale.»

Riga per la tabella `tab:repr`:

```latex
Vocem 1998 (offset)        & posizione-buffer & input (1 curva)\\
```

(Posiziona la riga prima di «questo sistema»; rafforza la colonna *Flusso*:
input/curva singola vs output/popolazione.)

### 2.2 — EmissionControl2 come confronto contemporaneo

> *Da aggiungere in §3 (chiusura) o §6. Definisce la scelta del differito rispetto
> all'ambiente granulare-con-visualizzazione di riferimento di oggi.*

Testo proposto:

«Sul versante real-time contemporaneo, EmissionControl2~\cite{Roads2021} affianca alla
granulazione uno *Scan Display* — forma d'onda con scanner sovrapposto in tempo reale.
È la rappresentazione viva del «dove sto leggendo» mentre il suono scorre. La partitura
qui descritta condivide l'oggetto (la posizione di lettura) ma ne ribalta il regime
temporale: non un cursore che segue l'esecuzione, ma una mappa statica e completa
dell'intera popolazione di grani, ispezionabile fuori dal tempo, su cui il loop lungo
ritorna.»

### 2.3 — Correzione della frase «frequenza convenzionale»

> *Difetto di coerenza interna: l'attuale frase di §3 contraddice la Tab. dello stesso
> paragrafo. Vedi paper.tex:434–436 e la Tab. `tab:repr` (Truax = mask, GeoGraphy =
> mappa spaziale: nessuno dei due è frequenza).*

Frase attuale (da sostituire):

> «il verticale codifica la posizione di lettura nel buffer sorgente, **dove le
> rappresentazioni convenzionali del controllo granulare collocano la frequenza**.»

Problema: la tabella elenca Truax 1988 (parametro/mask) e GeoGraphy 2003 (mappa
spaziale); la frequenza è solo una delle scelte storiche (Roads, *metafora*).
L'affermazione «le convenzionali collocano la frequenza» è imprecisa.

Riscrittura proposta:

> «il verticale codifica la posizione di lettura nel buffer sorgente. Le rappresentazioni
> storiche del controllo granulare hanno usato il verticale per grandezze diverse — la
> frequenza come metafora geometrica (Roads), il valore di un parametro entro la mask
> (Truax), una mappa spaziale (GeoGraphy), una curva di offset come controllo (Vocem) —
> ma mai la posizione di lettura come **output** misurato del rendering (Tab.~\ref{tab:repr}).»

Così la frase concorda con la propria tabella e incassa Vocem nel ragionamento.
