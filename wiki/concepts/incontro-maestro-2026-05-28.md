# Incontro con il maestro — 2026-05-28

Direttive metodologiche cross-sezione raccolte in un incontro di revisione del
paper CIM 2026. Pagina di `concepts/` (non fonte citabile): registra richieste
del maestro, decisioni prese e mappatura sull'impatto del paper.

---

## Data, contesto, modalità

- **Data:** 2026-05-28
- **Contesto:** incontro in cui Giulio mostra al maestro lo stato del paper CIM 2026
  (PythonGranularEngine, sintesi granulare in tempo differito) — bibliografia
  raccolta, narrazione tre atti, partitura grafica, e in più una demo del nuovo
  editor grafico in browser.
- **Modalità:** trascrizione Whisper dell'audio in `inbox/audio.txt` (826 righe),
  esportata anche in `audio.{json,srt,tsv,vtt}` (timestamp per segmento).
  **Nessuna diarizzazione automatica** nei file Whisper: l'attribuzione degli
  speaker — **M** = maestro, **G** = Giulio — è ricostruita dal contenuto e dalla
  struttura dei turni. I numeri di riga rimandano a `inbox/audio.txt`.
- **Prossimo incontro:** 9 giugno mattina, in presenza (righe 810–819).
- **Nota deadline:** in conversazione G stima la scadenza «20 o 21 giugno»
  (righe 535–536); la deadline canonica CIM (CLAUDE.md / EasyChair) è **7 giugno
  2026**. Discrepanza da imputare a ricordo approssimativo in dialogo — vale il 7
  giugno. Da verificare se la stima di G segnalava una finestra diversa.

---

## Sintesi richieste maestro (punti operativi)

1. **Risset come ancora filosofica del deferred** — in apertura (righe 1–13) il
   maestro conferma che la riflessione di Risset contro il real-time («*critical
   real time*») è un appiglio legittimo per dare forza alla scelta del tempo
   differito, «scelta che oggi sembra poco consueta». Usare Risset come fonte
   filosofica diretta.

2. **CORREZIONE Truax (economia di mezzi, NON cambio di paradigma compositivo)** —
   il non-determinismo statistico in Truax è **economia di mezzi / economia di
   pensiero** per gestire centinaia di grani al secondo, non una postura
   compositiva. Truax stesso progetta regioni armoniche (*Riverrun*: maschere di
   tendenza concentrate intorno a 100/200/300 Hz). Il punto compositivo vero: la
   granularità *scende nell'intimo del segnale* e impone scelte macroscopiche di
   altro tipo.

3. **Struttura BOTTOM-UP** — partire dal programma Python → architettura → relate
   con l'esistente → implicazioni teorico-compositive **alla fine**. Avvertimento:
   «stai assommando e non focalizzando».

4. **GUI editor browser → secondo paper futuro** — non includere l'editor grafico
   in questo paper; finalizzare questo come fase del lavoro, dedicare un secondo
   paper alla GUI richiamando il primo.

5. **Niente brano forzato** — se il pezzo non c'è, non forzarlo. I piccoli studi
   restano esempi sonori per la presentazione, non un caso compositivo nel paper.

6. **Scrittura artigianale, non sperimentale** — non essere sperimentale nello
   *scrivere* il paper; «un compositore artigianale che fa una buona sonata».
   Studiare i paper antichi citati anche come **modelli di narrazione/chiarezza
   espositiva**, non solo per contenuto.

---

## Quote chiave verbatim

> Le quote conservano la trascrizione Whisper; le correzioni di parole
> chiaramente mal-trascritte sono tra `[ ]`. «canulare» → granulare in tutto.

**[M] Truax = economia di mezzi** (righe 38–45):
> «No, appellandosi, parlando di non determinismo, si riferisce soltanto al fatto
> che quando c'hai così tanti dati da controllare, come nella sintesi
> [granulare]. [...] su un approccio statistico diventa necessario per l'economia
> di mezzi, per l'economia di pensiero [...] lui può raggiungere densità [...]
> fino a alcune centinaia di grani al secondo, e non hai ragione umana per
> razionalizzare tutti questi dati. [...] quindi lo dice soltanto per questo.»

**[M] Gli stimoli statistici hanno una loro dimensione percettiva; regioni
armoniche progettate in *Riverrun*** (righe 52–62):
> «[...] gli stimoli statistici hanno una loro dimensione percettiva, gli stimoli
> non statistici hanno una loro dimensione percettiva. [...] se tu ascolti il
> [Riverrun], ci sono delle parti dove la dimensione armonica della propulsione è
> evidente [...] il fatto che ricorra a un motore di numeri casuali, perché ci
> sono un sacco di dati, [non] significa che non possa progettare la relazione tra
> maschere di tendenza che si concentrano in regioni tra loro in rapporto. Uno può
> avere una [risonanza] intorno ai 100 Hz, [...] 200 Hz, [...] 300 Hz, e c'è una
> dimensione armonica.»

**[M] L'event list non è più deterministica — necessità, non teoria della
composizione** (righe 64–72):
> «Il suo riferimento a una partitura, e parliamo di partiture al computer [...]
> l'event list [...] non è più deterministica, come era obbligatorio fare sui
> linguaggi tipo [Music V], [Csound], eccetera, ma aveva bisogno di ricorrere a
> event list talmente [variegate], rapide e in quantità mostruose che sentiva
> necessario passare all'aspetto statistico.»

**[M] La granularità scende nell'intimo del segnale** (righe 73–86):
> «Quindi non ne farei una tematica particolarmente impegnativa, non è teoria
> della composizione [...] si introdusse una dimensione statistica che peraltro
> non era neanche ignota all'epoca di Truax [...] semplicemente vorrei
> sottolineare come la dimensione della granularità, scendendo così nell'intimo
> del segnale, ti provoca una scelta macroscopica, un orientamento macroscopico di
> altro tipo.»

**[M] Stai assommando, non focalizzando** (righe 287–299):
> «perché adesso forse stai, come ti capita spesso, assommando e non focalizzando
> le cose. Stai assommando. E devi un po' decidere che cosa vuoi presentare.»

**[M] Top-down vs bottom-up** (righe 341–360):
> «se tu parti dall'alto [e] vai verso il basso, potrebbe essere un paper di
> carattere più informatico e teorico, di teoria della composizione informatica.
> Se tu parti dalla sintesi e astrai verso l'alto [...]»

**[M] Direttiva bottom-up esplicita** (righe 550–558):
> «In un paper di quattro pagine tu devi individuare, inizialmente, la tematica
> [...] e far vedere il tuo approccio, scendendo nei dettagli, dell'approccio
> anche informatico. [...] Io ho scritto un programma Python che fa sintesi
> [granulare] del suono, lo sviluppo, lo mostro, e poi lo metto in relazione con
> l'esistente [...]. Ma passare direttamente [...] a tutti i fatti storici [...]»

**[M] Implicazioni alla fine; «python usato come sintetizzatore»** (righe 569–588):
> «questa possibilità di notazione, con le [sue] differenze [...] emerge come
> frutto del lavoro, che non te la premetti, e poi fai vedere come [...] io non lo
> so se esistono esempi di python usato come sintetizzatore, quindi partire da
> quello, da tutte le problematiche [del] tempo differito [...] review della
> letteratura se vuoi [...] le cose più vicine alle tue esigenze, e poi [...]
> facendo emergere le implicazioni teorico musicali, teorico compositive alla
> fine.»

**[M] Secondo paper per la GUI** (righe 443–456):
> «Finalizzando questo paper, perché rappresenta una fase del lavoro e ha una sua
> logica costruttiva e anche riferimenti alla literature review [...]. Poi magari
> presento un secondo paper [...] dedicato invece all'interfaccia grafica [...]
> richiamandolo, se lo vuoi presentare al CIM [...]. Se li vuoi mettere insieme
> adesso rischi che non ne fai uno buono dei due.»

**[M] Non forzare il brano** (righe 465, 470–471):
> «No, se il pezzo non c'era non ti devi forzare affatto.» [...] «Intanto possono
> essere esempi sonori da presentare quando vai a fare la presentazione.»

**[M] Studiare i paper antichi come modelli stilistici** (righe 706–733, 763–771):
> «alcuni dei [paper] [...] più antichi che [...] tu citavi [...] potrebbero
> essere utili [...] quando leggi uno di questi paper leggi non solo contenuti ma
> leggi anche come [...] fino a che punto si è sforzato [...] di comunicarli con
> chiarezza.» [...] «proprio l'analisi compositiva di come è stato scritto, cioè
> di come ha portato anche la narrazione.»

**[M] Artigianale, non sperimentale** (righe 778–801):
> «ti consiglio di non essere molto sperimentale [nello] scrivere un paper, ma un
> compositore che riesce a scrivere un buon paper e che raggiunge l'obiettivo
> [...] un compositore artigianale che fa una buona sonata, però si chiama paper
> in questo caso.»

---

## Quote vs interpretazione — onestà filologica

- Il maestro **NON** ha nominato Truax o Roads come «modelli bottom-up della spina
  dorsale». Ha dato un consiglio **generale** di analisi narrativa dei paper
  antichi citati (righe 706–733, 763–771), senza specificare *quali*.
- L'interpretazione di studiare **Truax 1988 + Roads 1978/1988** come modelli di
  descrizione bottom-up del proprio sistema è **lettura di Giulio**, coerente col
  consiglio generale ma non quote testuale. Da segnalare come interpretazione
  ovunque venga usata.
- «Riverrun» e «100/200/300 Hz» sono ricostruiti da trascrizione mal-resa
  («il verano», «disfunzione»): plausibili dal contesto (Truax, *Riverrun*,
  regioni armoniche) ma non certi al 100%.

---

## Mapping richieste → impatto sul paper

| Richiesta maestro | Impatto |
|-------------------|---------|
| Truax = economia di mezzi (non cambio paradigma) | Correzione `overview.md` Atto 2 + Sez. 4 paper; mai «Truax = real-time come cambio di paradigma compositivo» |
| Struttura bottom-up | Riscrittura `paper.tex` da zero: Python → architettura → tradizione → implicazioni alla fine |
| GUI = secondo paper | Editor browser fuori scope; nessuna menzione nel paper (eventuale rinvio in conclusioni come sviluppo futuro) |
| Niente brano forzato | Sez. 5 «caso compositivo» eliminata; studi come esempi sonori per la presentazione orale |
| Risset ancora deferred | Quote pietra-angolare Risset p. 37 nelle implicazioni finali |
| Artigianale non sperimentale + studio narrativa | Studio architettura espositiva paper antichi → `concepts/modelli-stilistici-bottom-up.md` |

---

## Direzioni future emerse (fuori scope di questo paper)

- **GUI editor browser** — secondo paper (punto 4).
- **Generazione grani via grafi alla Valle** — G ha letto e apprezzato un paper di
  Andrea Valle (grafi dove ogni nodo è un grano, distribuzioni di probabilità sulla
  rete; cfr. [[valle-lombardo2003]]); vorrebbe portarlo nel real-time via microfoni
  (righe 485–510). Orizzonte di ricerca a 4–5 anni, non materia di questo paper.

---

## Decisioni prese in sessione

- Sviluppare **solo la variante bottom-up**; archiviare la variante top-down come
  GitHub issue con piano dettagliato per eventuale ripensamento.
- `paper.tex` **scartato per intero** e riscritto da zero in branch
  `paper-bottom-up`.
- Doc PGE canonica `raw/PythonGranularEngine/docs/` (Diátaxis) usata come fonte
  oltre a `wiki/sources/pge/`.

Vedi anche: [[deferred-time-tradition]], [[tendency-mask]], [[risset1999]],
[[truax1988]], [[modelli-stilistici-bottom-up]].
