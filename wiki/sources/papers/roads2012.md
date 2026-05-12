# [Roads, 2012] From Grains to Forms

## Citazione CIM
Roads, C. (2012). From Grains to Forms. In S. Kanach (ed.), *Xenakis Matters: Contexts, Processes, Applications*. Hillsdale, NY: Pendragon Press. ISBN 978-1-57647-238-5.

## Argomento centrale
Saggio argomentativo sulla composizione granulare meso/macro: come organizzare i grani in forme musicali su scala più ampia. Roads passa in rassegna sei paradigmi di organizzazione (screen/cloud/stream/spray, montage studio, controllo gestuale, higher-order granulation, dictionary-based pursuit, modelli fisico-biologici, modelli generativi astratti) e li valuta criticamente rispetto al problema irrisolto del *multiscale organization*. Tesi: nessuno dei paradigmi puramente formali, gestuali o emergentisti basta; serve un approccio ibrido formale/informale guidato da *economy of selection* — la scelta umana ispirata su un orizzonte di possibilità.

## Gap o problema identificato
Multiscale coherence: come trasferire complessità da uno strato basso a forme leggibili sulla scala meso/macro mantenendo qualità essenziali? Roads cita Wesley Smith (2011): *"One of the major challenges in building a system that can increase in complexity as it runs is figuring out how to transfer complex structures in a lower level space into simple structures in a higher level space while still maintaining the essential qualities that the complex lower level structure represents."* Strategie bottom-up di "emergent self-organization" cadono corte; servono forze long-term high-level. La risposta proposta è esplicitamente *euristica*: combinare potenza algoritmica con scelta intuitiva umana. Le formule da sole producono *unremarkable music* (cf. nota 5 su WolframTones).

## Rilevanza diretta per PGE
Tre punti di sovrapposizione strutturale:

1. **Per-grain processing come signature** (pp. 14–15). Roads: *"per-grain effects processing [...] amazingly seems to be missing in other implementations. [...] many granulators that feed the entire grain stream through the same effects channel tend to sound flat and one-dimensional."* PGE realizza questo principio architetturalmente: Stream + Controller × 4 (pitch, density, pointer, voice) + VoiceManager permettono deviazione stocastica per-grano su tutti i parametri. Argomento di forza per sezione 3 — il differenziatore "per-grain freedom" non è nuovo ma è citato dall'autore stesso.

2. **Higher-order granulation = workflow STEMS** (p. 13). Roads descrive la propria pratica: *Now* (2004) è regranulazione di *Volt air* (2003); *Never* (2010) è regranulazione di terzo ordine di *Now*; *Always* (in progress) è di quarto ordine. Metodo: rendering offline, organizzazione in Pro Tools timeline. PGE STEMS workflow è precisamente questa pipeline costituita architetturalmente: rendering per-stream + cache incrementale + export multitraccia DAW. Roads lo fa manualmente; PGE lo formalizza nel sistema.

3. **Studio detached from real-time = postura loop lungo** (p. 8). Roads esplicito: *"Detached from real-time constraints, ideas can be tested, edited, submixed, or deleted at will."* È la formulazione canonica della postura tempo differito. PGE estende questa postura non solo al montaggio (Pro Tools) ma alla generazione stessa: il ciclo specifica → generazione → ascolto → riscrittura abita lo spazio differito di Roads ma ne sposta il baricentro dal mixing alla scrittura del materiale.

Quattro punti di posizionamento argomentativo (differenziatori che Roads NON copre):

4. **PGE come bifurcazione della lineage UCSB.** Roads racconta in prima persona la traiettoria Cloud Generator (1995) → Creatovox (1999–2000) → PulsarGenerator → EmissionControl → EC2. È la *gestural/virtuosic line*. Roads ammette il fallimento Creatovox: *"A funny thing happened at this point. Every time I went out in public to demonstrate the Creatovox, the results disappointed me. [...] a virtuoso instrument requires a virtuoso performer who practices the instrument every day! Ultimately I decided that becoming a virtuoso performer was not central to my interests in composition."* PGE si colloca nel filone parallelo che Roads non sviluppa: il ritorno volontario al deferred time non per limitazione hardware ma per scelta di posture.

5. **PulsarGenerator come endorsement del compromise script + envelope visivo.** Conclusione (p. 30): *"In the studio, graphical envelope control as in PulsarGenerator is an excellent compromise between gestural interaction and the kind of detailed micro control that can only come from scripts or code."* PGE-ls (YAML editing) + score_visualizer (rendering grafico) si pongono esplicitamente in questo *compromise space* indicato da Roads come desiderabile. La differenza: PulsarGenerator usa envelope come input control; PGE inverte la freccia — il visualizer è output di lettura del codice. Stessa filosofia compositiva, asse di interazione opposto.

6. **MetaSynth/UPIC/Borderlands come riferimento del piano tempo×frequenza.** Roads (p. 5): MetaSynth permette di "spray grains onto a time-frequency grid". Fig. 3 (MetaSynth) e Fig. 6 (Borderlands) mostrano il piano canonico T×F. PGE score_visualizer differisce sostanzialmente: asse Y = posizione nel buffer audio sorgente. Non è frequenza percepita ma puntatore sample. Roads non considera questa scelta — è un differenziatore genuino non coperto dalla letteratura precedente. Va citato in sezione 4 per delimitare il piano scelto.

7. **Economy of selection come teorizzazione esplicita del loop lungo.** Sezione "The principle of economy of selection" (pp. 28–29): *"choosing one or a few perceptually and aesthetically optimal or salient choices from a vast desert of unremarkable possibilities. This choice relies on the powerful aesthetic perception of an expert practitioner."* È praticamente la definizione del loop lungo come metodologia compositiva, formulata da Roads in modo indipendente. Citazione pietra-angolare per sezione 6: il loop lungo PGE non è una scelta idiosincratica ma una istanza dell'economy of selection applicata alla scrittura granulare.

## Collegamento alla tesi centrale
Paper-cardine per la narrazione in tre atti, ma soprattutto per il *secondo movimento* della tesi (PGE come ritorno volontario al deferred time). Roads stesso, nel 2012, ammette i limiti del polo real-time-virtuosico e propone il *compromise space*: studio detached from real-time + ascolto come giudice + economy of selection. La tesi PGE non si oppone a Roads — la prolunga sul versante del DSL programmabile. La differenza rispetto a Roads 2001 (loop di feedback come problema) e Roads 2006 (continuità Cloud Generator → EC2): Roads 2012 *teorizza esplicitamente* l'esistenza di una postura ibrida formal/informal che lega euristica, ascolto e selezione. È la legittimazione argomentativa più forte del loop lungo come metodologia, scritta da uno dei sostenitori principali della lineage real-time.

Per la postura tempo differito: la quote p. 8 ("Detached from real-time constraints, ideas can be tested, edited, submixed, or deleted at will") è la formulazione canonica.

Per i tre contributi:
- DSL YAML: matrix modulation di EmissionControl (Fig. 8) come precursore parametrico GUI; PGE estende verso testo programmabile + LSP, ma il principio di "parametri modulati da LFO+random" è già in Roads.
- Score visualizer: align spirituale con UPIC/MetaSynth/Borderlands; differenziatore PGE = asse Y posizione buffer.
- Workflow STEMS: aderenza letterale alla pratica higher-order granulation di Roads (Now/Never/Always); PGE la istituzionalizza nel rendering engine.

## Sezioni del paper CIM 2026 dove citare
- **Sezione 1 (Introduzione)**: quote Risset 2005 (slippery continuum tra micro e macro, supporto al DSL che attraversa scale); incipit quote *"the granular paradigm refuses to die"*.
- **Sezione 2 (Sintesi granulare)**: tassonomia SGS/AGS (pp. 6–7); per-grain processing come signature granular (pp. 14–15); limiti dei modelli puramente generativi formali.
- **Sezione 3 (PGE architettura)**: per-grain effects come pilastro architetturale; EmissionControl matrix modulation come precursore GUI del DSL; ammissione esplicita Roads del fallimento Creatovox (legittima scelta architetturale PGE non-real-time).
- **Sezione 4 (Partitura grafica)**: MetaSynth/UPIC/Borderlands come riferimenti del piano T×F; PulsarGenerator envelope come endorsement compromise visual+script; delimitazione differenziatore PGE (asse Y = posizione buffer).
- **Sezione 5 (Caso compositivo)**: higher-order granulation come precedente del workflow STEMS PGE; *Now/Never/Always* come esempi di pratica iterativa di regranulazione su scala compositiva.
- **Sezione 6 (Conclusioni)**: economy of selection (pp. 28–29) come teorizzazione esplicita del loop lungo; hybrid formal/informal heuristics; quote pietra-angolare PulsarGenerator (compromise script + envelope, p. 30).

## Quote chiave

**Per-grain processing come signature** (pp. 14–15):
> *"I should mention here an essential feature that is characteristic of all my granulators since 1988, and which amazingly seems to be missing in other implementations: per-grain effects processing. [...] In a similar per-grain fashion we can pitch-shift, ring-modulate, etc. each grain individually with different parameter settings for each grain. The resulting heterogeneity of sound is the signature of truly granular signal processing. By comparison, many granulators that feed the entire grain stream through the same effects channel tend to sound flat and one-dimensional."*

**Studio detached from real-time** (p. 8):
> *"This approach is extremely free in terms of compositional options, considering that material at any time scale can be processed by plugins and placed anywhere in the time line. Detached from real-time constraints, ideas can be tested, edited, submixed, or deleted at will."*

**Higher-order granulation** (p. 13):
> *"Recycling sounds by means of higher-order granulation is a method of spawning new granular mesostructures out of old ones. [...] I did not begin to experiment with higher-order granulation until 2003 with the realization of Now (2004), a regranulation of my composition Volt air (2003). In turn, Never (2010) was a third-order granulation of Now. I am currently working on a fourth-order granulation of Now in the work-in-progress Always."*

**Fallimento Creatovox e ritorno allo studio** (pp. 10–11):
> *"A funny thing happened at this point. Every time I went out in public to demonstrate the Creatovox, the results disappointed me. It was not the fault of our design, it had to do with the fact that I had not invested a great deal of time to practice playing this instrument. What a surprise: a virtuoso instrument requires a virtuoso performer who practices the instrument every day! Ultimately I decided that becoming a virtuoso performer was not central to my interests in composition. [...] in this case the Creatovox was used to generate fragments that were ultimately assembled in Pro Tools."*

**PulsarGenerator compromise script + envelope** (conclusione, p. 30):
> *"In the studio, graphical envelope control as in PulsarGenerator is an excellent compromise between gestural interaction and the kind of detailed micro control that can only come from scripts or code."*

**Economy of selection** (pp. 28–29):
> *"Hand-in-hand with the use of heuristic algorithms is one of the most important issues in composition: the principle of economy of selection (Roads forthcoming). Economy of selection means choosing one or a few perceptually and aesthetically optimal or salient choices from a vast desert of unremarkable possibilities. This choice relies on the powerful aesthetic perception of an expert practitioner. [...] Economy of selection is an important concept because it emphasizes the role of intuitive choice in all compositional strategies. Even in generative composition, the algorithms are chosen according to subjective preferences. [...] Computer programs can solve for and enumerate many of these solutions, but carefully picking the 'best' or 'optimal' solution is a human talent."*

**Risset su DSL che attraversa scale** (citato p. 3):
> *"By bridging gaps between traditionally disconnected spheres like material and structure, or vocabulary and grammar, software creates a continuum between microstructure and macrostructure. It is no longer necessary to maintain traditional distinctions between an area exclusive to sound production and another devoted to structural manipulation on a larger temporal level. The choice of granulation, or of the fragmenting of sound elements, is a way of avoiding mishaps on a slippery continuum: it permits the sorting of elements within a scale while it allows individual elements to be grasped. The formal concern extends right into the microstructure, lodging itself within the sound grain."* — Risset (2005).

**Limitations of formalism** (p. 22):
> *"Works of art make rules, rules do not make works of art."* — Debussy (citato in Risset 2004).

**Multiscale coherence problem** (pp. 25–26):
> *"This is one of the great unsolved problems in algorithmic composition. The issue is not merely a question of scale, i.e., of creating larger sound objects out of grains. It is a question of creating coherent multiscale behavior extending all the way to the meso and macro time scales. Multiscale behavior means that long-term high-level forces are as powerful as short-term low-level processes."*
