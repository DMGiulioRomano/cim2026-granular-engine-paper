# ScoreVisualizer — analisi

## Ruolo nell'architettura

Genera la partitura grafica del brano granulare come PDF o PNG multipagina. Riceve un `Generator` già processato (con `streams` popolati e grani generati) e produce una rappresentazione visiva dove il piano tempo×buffer-position diventa notazione leggibile.

Non modifica nessun dato: è output-only, lettura da `generator.streams`.

## Classi principali

**ScoreVisualizer**
- Attributi: `generator`, `streams`, `config: dict`, `waveform_cache`, `total_duration`, `page_count`, `page_layouts`
- Entry point: `export_pdf(path)` → `render_all()` → `render_page(page_idx)`
- Workflow: `analyze()` → calcola layout pagine → `render_page()` per ogni pagina

## Sistema di coordinate (nucleo del contributo)

**Asse X:** tempo della partitura (secondi)  
**Asse Y:** posizione nel sample audio (secondi nel file .wav)

Ogni pagina è suddivisa per **sample unico** (non per stream): tutti gli stream che leggono lo stesso campione condividono un subplot, con la waveform verticale del file come riferimento spaziale.

Layout per pagina (GridSpec):
```
[waveform  |  grani per sample 1  ]
[  col     |  grani per sample 2  ]  ← n_samples righe
[  (~6%)   |  envelope panel      ]  ← se presenti envelope
```

## Encoding visivo dei grani

Ogni grano = freccia poligonale:
- **Posizione X:** onset del grano nel tempo
- **Posizione Y:** `grain.pointer_pos` (posizione nel buffer audio)
- **Larghezza:** `grain.duration`
- **Altezza:** `grain.duration` (sample consumato)
- **Forma freccia:** punta in su se `pitch_ratio > 0` (forward), punta in giù se `pitch_ratio < 0` (reverse)
- **Colore:** `pitch_ratio` → colormap `coolwarm` (rosso = alta trasposizione, blu = bassa)
- **Opacità:** `grain.volume` → alpha range (0.3–1.0)

Loop mask: banda arancione semitrasparente che mostra la regione loop_start→loop_end nel buffer per ogni istante temporale. Gestisce wraparound quando il loop supera la fine del file.

## Envelope panel

Pannello separato (30% altezza pagina) per visualizzare tutti i parametri time-varying dello stream (envelope dinamici con >1 breakpoint):
- Ogni stream ha una "corsia" verticale propria
- Envelope normalizzati su range fissi per parametro (es. volume: -90..0 dB, density: 1..200 g/s, pitch_semitones: -36..36 st)
- Tipo `step` → `drawstyle='steps-post'`; tipo `linear`/`cubic` → campionamento denso (500 punti)
- Breakpoint annotati con valore reale + unità (dB, ms, st, g/s, ...)
- Colori fissi per parametro (volume=rosso, density=arancio, pitch_semitones=viola, ...)

## Paginazione e layout

- Default: 30 secondi/pagina, A3 landscape
- Greedy slot assignment: stream non sovrapposti condividono la stessa riga verticale
- Sweep line per calcolare max stream simultanei per pagina

## Collegamento alla tesi centrale

ScoreVisualizer è lo strumento del loop lungo: non precede il processo compositivo, lo traccia e lo rende leggibile. Dopo ogni ciclo specifica → generazione → ascolto, la partitura grafica è il supporto della riflessione — il momento in cui il compositore legge cosa ha prodotto una scelta parametrica e decide se e come modificarla. Senza questo strumento il loop lungo sarebbe cieco: si ascolterebbe il risultato ma non si vedrebbe la struttura che lo ha generato.

La scelta dell'asse Y come posizione-nel-buffer è la decisione progettuale chiave: rende visibile *da dove* ogni grano pesca nel campione sorgente — informazione non udibile direttamente ma decisiva per capire la relazione tra pointer, speed_ratio e texture risultante. Confronto con i precursori: Truax 1988 Fig. 4 usa il piano visivo come **input** di controllo real-time (il compositore disegna le tendency masks mentre ascolta); PGE usa lo stesso piano come **output** analitico del loop lungo (il compositore legge la partitura dopo aver ascoltato). La direzione è invertita, la scala temporale è diversa.

## Sezioni del paper CIM 2026 dove descrivere

- Sezione 4 (Partitura grafica): descrizione completa — piano tempo×buffer, encoding visivo, loop mask, envelope panel. Confronto esplicito con Truax Fig. 4 (input vs output, asse Y diverso) e Roads 1978/1988 (polygon freq/tempo vs posizione-buffer). È la figura principale del paper.
- Sezione 5 (Caso compositivo): come la lettura della partitura nel loop lungo ha motivato almeno una scelta compositiva concreta che solo l'ascolto non avrebbe chiarito

## Domande aperte

- Qual è il brano compositivo usato come caso di studio nel paper? Da scegliere per la figura.
- L'asse Y come "posizione nel buffer" è stato anticipato da qualche approccio nella letteratura (Roads 2001, Di Scipio 1994)? Da verificare post-ingest papers.
- `PATHSAMPLES = './refs/'`: path hardcoded — da verificare se diverso in produzione.
