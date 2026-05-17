# [Truax, 2014] Interacting with Inner and Outer Sonic Complexity: from Microsound to Soundscape Composition

## Citazione CIM

Truax, B. (2014). Interacting with Inner and Outer Sonic Complexity: from Microsound to Soundscape Composition. *eContact!*, 16(3). URL: http://econtact.ca/16_3/truax_soniccomplexity.html

## Argomento centrale

Retrospettiva di Truax sui 25+ anni di pratica con time-frequency methods (granular time-stretching, risuonatori, convoluzione) ricondotti a un quadro unificato che lega *inner complexity* (micro-domain granulare) e *outer complexity* (soundscape). Tre tecniche persistenti, due domini estremi del mondo sonoro, una stessa postura compositiva: usare il computer per *enhance the inner workings of sounds to reflect their contextual meanings*.

## Gap o problema identificato

Truax non identifica un gap tecnico ma un punto di vista compositivo: differenza tra usare la tecnologia come *servant* della produzione (computer-realized composition) e come *partner* che cambia vocabolario artistico (computer-assisted/computer-composed). I granulatori che processano flat — *imposing unrelated processing artifacts onto those sounds* — sono il negativo del programma: il design del compositore deve *bring out the internal aspects of the sounds being used, and enhance them, rather than obliterating the identity of the source material*.

## Rilevanza diretta per PGE

Quattro corrispondenze:

1. **Listening inside the sound** (p. 2). Il time-stretching granulare sposta l'attenzione percettiva dal contorno macro alle componenti spettrali interne: «*As the temporal shape of a sound becomes elongated [...] one's attention shifts towards the spectral components of the sound, either discrete frequency components, harmonics or inharmonics, or resonant regions and broadband textures. I often refer to this process as listening "inside" the sound*». L'asse Y di `score_visualizer` PGE (posizione-buffer) rende **visivamente esplicito** lo spostamento di attenzione che Truax descrive a parole: il compositore non vede solo l'evoluzione macro nel tempo ma il *punto di ascolto interno* — quale porzione del campione viene investigata in ogni istante.

2. **Per-grain processing come differenziatore di adeguatezza** (p. 5). La distinzione *abstracted* vs *abstract* — «*the composer's sound design through processing somehow brings out the internal aspects of the sounds being used, and enhances them, rather than obliterating the identity of the source material and/or imposing unrelated processing artifacts*» — è coerente con il differenziatore 7 di `overview.md` (per-grain effects come signature) formulato da Roads 2012. Truax aggiunge il criterio percettivo: il processing deve essere *trasparente* al source, non un layer omogeneo sovrapposto. PGE soddisfa la clausola via Controller×4 + VoiceManager + dephase per-grano.

3. **Composing through sound** (p. 5). «*I sometimes refer to the nature of these processes as allowing me to compose "through" sound, not just "with" it*». La preposizione (*through*) descrive la postura compositiva del loop lungo: la specifica YAML non manipola il suono come materiale opaco esterno ma attraversa la sua struttura interna parametricamente. È formulazione cugina del *composing-the-sound/composing-with-sound* di Truax 1990b, ridiscussa qui in chiave retrospettiva.

4. **Tassonomia artista-macchina** (p. 6). Truax propone tre modi della relazione: *computer-realized* (computer come servant della produzione), *computer-assisted* (interactive partnership che cambia vocabolario), *computer-composed* (fully automated rule-based). PGE si colloca nella zona *computer-assisted*: il sistema partecipa cambiando il vocabolario compositivo (DSL YAML + score grafica come strumenti che strutturano l'intenzione) senza essere né mero esecutore né autore autonomo. *«When the computer is used to control complexity that results in emergent forms, the role of the artist is profoundly changed to many possible scenarios: guide, experimenter, designer, visionary, poet»* (p. 6) — descrizione del ruolo del compositore nel loop lungo.

Non rilevante per PGE: la sezione *Soundscape Composition* (pp. 4–5) — PGE non è uno strumento per soundscape composition specifico (riconoscibilità del source material come principio (a) non è obiettivo di PGE che lavora su qualsiasi buffer). Vale come cornice del lavoro di Truax, non come precursore di feature PGE.

## Collegamento alla tesi centrale

Affinamento del **terzo atto** della narrazione (ritorno volontario al tempo differito): Truax stesso, padre del real-time granular (1988), nel 2014 elenca tre tecniche — granular time-stretching, risuonatori, convoluzione — che ha usato *over the past 25 years*. Non c'è ammissione di abbandono del real-time, ma c'è continuità di una *postura di indagine interna al suono* che attraversa la scala temporale del feedback. Il quote *composing "through" sound* legittima il vocabolario della tesi PGE: il loop lungo non è una limitazione tecnologica residua ma uno spazio compositivo in cui la struttura interna del suono diventa terreno di scrittura.

Affinamento del **contributo 2** (partitura grafica con asse Y = posizione-buffer): il *listening "inside" the sound* (p. 2) è la giustificazione percettiva dell'asse Y. Truax 1994 (separazione micro/macro come tesi psicoacustica) + Truax 2014 (l'ascolto del compositore *abita* lo spazio interno mentre il tempo si dilata) → la partitura PGE codifica visivamente questo spazio di ascolto. La scelta Y = posizione-buffer non è arbitraria, è la rappresentazione del *dove sto ascoltando dentro il campione*.

## Sezioni del paper CIM 2026 dove citare

- **Sezione 2** (Sintesi granulare): continuità della pratica granulare 1988→2014 in Truax stesso; *listening inside the sound* come effetto percettivo canonico del time-stretching granulare.
- **Sezione 4** (Partitura grafica): *listening "inside" the sound* (p. 2) come giustificazione percettiva diretta dell'asse Y = posizione-buffer.
- **Sezione 6** (Conclusioni): tassonomia computer-realized/assisted/composed per posizionare PGE come *computer-assisted* — partnership che cambia vocabolario. *Composing "through" sound* come formula della postura compositiva.

## Quote chiave

> «*As the temporal shape of a sound becomes elongated [...] one's attention shifts towards the spectral components of the sound [...] I often refer to this process as listening "inside" the sound*» (p. 2)

> «*I sometimes refer to the nature of these processes as allowing me to compose "through" sound, not just "with" it*» (p. 5)

> «*When the computer is used to control complexity that results in emergent forms, the role of the artist is profoundly changed to many possible scenarios: guide, experimenter, designer, visionary, poet*» (p. 6)
