# Esempi del paper — PythonGranularEngine (PGE)

Gli esempi seguono l'esposizione bottom-up di §2 del paper («una deviazione
alla volta»): si parte dallo *stream minimo* — la specifica che si limita a
riprodurre fedelmente il campione sorgente — e ogni esempio successivo aggiunge
**un solo** scostamento, isolando un meccanismo del sistema. Ogni cartella è
autocontenuta: sorgente YAML (in git) + una realizzazione generata (partitura,
waveform, spettrogramma — gitignored). L'audio (`.aif`) va su Zenodo, non in git.

| Cartella | § paper | Variabile isolata | Andamento atteso | Bit-identico |
|---|---|---|---|---|
| `ex0_identity` | 2.1 | nessuna: le 4 chiavi obbligatorie | copia fedele del campione (residuo RMS ≈ −74 dB, vedi comparison) | sì |
| `ex1_distribution` | 2.2 | `distribution` 0→1 | treno metronomico → tappeto asincrono (leggibile sulla waveform) | no |
| `ex2_pointer` | 2.3 | `pointer.speed_ratio` 1→0 | lettura naturale che decelera e si congela su una vocale; invisibile in waveform → è l'esempio che rende necessaria la partitura | sì |
| `ex3a_range` | 2.4 (gemello A) | `pointer.offset_range` 0→0.35 | cresce l'**ampiezza** della deviazione: cuneo a riempimento uniforme | no |
| `ex3b_dephase` | 2.4 (gemello B) | `dephase.pointer` 0→100 (range fisso 0.35) | cresce la **probabilità**: la linea centrale persiste, la popolazione deviante si infittisce | no |
| `ex4_voices` | 2.5 | blocco `voices`: 5 voci, `chord dom9` + `pointer linear` + `pan linear` 150° | 5 bande parallele sull'asse Y, colore = trasposizione | sì |
| `ex5_scatter` | 2.5 | `scatter` 0→1 (4 voci, `distribution: 1` costante) | colonne di onset allineate → griglie temporali indipendenti per voce | no |
| `exA_micro` | 2.4 (prosa) | `dephase: 40` senza alcun `_range` (jitter implicito di sistema) | A/B sulla stessa vocale congelata: treno periodico (pettine) vs micromodulazione | A sì, B no |

I gemelli `ex3a`/`ex3b` condividono base (freeze a 0.5) e banda massima:
differiscono **solo** per dove sta l'envelope (ampiezza vs probabilità).

`exA_micro` è un esempio **audio-first** (bundle Zenodo / presentazione orale),
non una figura del paper: doppio stream A/B in un unico YAML. Eventuale
promozione a figura (coppia di spettrogrammi) da verificare in B&W.

## Riproducibilità: andamento, non bit-identico

Il rendering PGE è stocastico (tendency mask alla Truax): il `random` non è
seminato in produzione, due run dello stesso YAML producono **grani diversi**.
È voluto, non un difetto. Ciò che si conserva è l'**andamento**: densità,
dispersione, traiettoria del pointer, distribuzione delle voci. La stessa
specifica produce sempre la stessa *forma*.

- `ex0`, `ex2`, `ex4` usano solo default e strategie deterministiche
  (`chord`, `linear`) → **bit-identici** fra le esecuzioni.
- `ex1`, `ex3a`, `ex3b`, `ex5` e lo stream B di `exA` usano gate/campionamenti
  non seminati → **non bit-identici**, ad andamento invariante.

Lo YAML è la fonte di verità spedita: chiunque lo esegue ottiene lo stesso
andamento. Partitura/audio inclusi sono **una** realizzazione di esempio.

## File per cartella

```
exN_*/
  exN_*.yml                sorgente, fonte di verità          (git)
  exN_*.aif                audio renderizzato                 (gitignored → Zenodo)
  exN_*_score.pdf          partitura grafica generata         (gitignored → make examples)
  exN_*_waveform.pdf       forma d'onda                       (gitignored → make examples)
  exN_*_spectrogram.pdf    spettrogramma B&W-safe             (gitignored → make examples)
```

Solo `ex0_identity/` ha in più `ex0_identity_comparison.pdf` (originale vs
elaborato sui primi 2 s, generato da `plot_comparison.py`): è la figura dello
stream minimo nel paper.

## Gli YAML sono input LaTeX

`paper.tex` include i sorgenti via `\lstinputlisting[linerange=...]`: i numeri
di riga dei `.yml` fanno parte del paper. Editando un file in modo da spostare
righe vanno aggiornati i `linerange` corrispondenti in `paper.tex` (diversi
`TODO linerange` sono ancora aperti lì).

## Come rigenerare

Dalla root del repo:

```bash
make examples                 # incrementale: rirenderizza solo gli .yml cambiati
make examples-clean examples  # forza la rigenerazione completa
```

Il target è incrementale sui timestamp (un `.aif` più recente del suo `.yml`
non viene rirenderizzato) e fa, nell'ordine:

1. `link-refs` (prerequisito automatico) — symlinka i file audio reali dal
   repo PGE sibling (`../PythonGranularEngine/refs`, override con env
   `PGE_REFS=...`) nella `refs/` vuota del submodule. Serve il campione
   sorgente `weNeedToTalkAboutIt.wav` (voce di donna, ~2 s).
2. `render_example.py` — audio (`RENDERER=numpy`, 48 kHz, mix) + partitura
   single-page (`page_duration` = durata dello stream) col PGE **pinnato nel
   submodule**, così la realizzazione corrisponde al codice citato dal paper.
3. `plot.py` — waveform + spettrogramma dall'`.aif` (scala di grigi, larghezza
   colonna CIM, leggibili in stampa B&W).
4. solo per `ex0_identity`: `plot_comparison.py` — pannello originale/elaborato.

`make paper` ha `examples` come prerequisito: le figure non sono tracciate in
git e vanno rigenerate prima della compilazione.

Per un singolo esempio:

```bash
.venv/bin/python paper/examples/render_example.py paper/examples/ex2_pointer/ex2_pointer.yml
.venv/bin/python paper/examples/plot.py paper/examples/ex2_pointer/ex2_pointer.aif
```

## Audio (Zenodo)

DOI: `TODO` — placeholder fino al caricamento del bundle. Per la submission
double-blind il record va anonimizzato (nessun nome autore, nessun link al repo).

## Disallineamenti noti (stato al 2026-06-11)

- `ex4_voices.yml`: `num_voices` è ancora l'envelope sperimentale
  `[[0,5],[.5,1],[1,10]]` e `duration: 2.0` — il paper (caption, claim
  bit-identico, 5 bande parallele) presuppone 5 voci costanti e ~20 s.
  Da fissare prima di rigenerare la figura.
- `ex5_scatter.yml`: il blocco `voices.pointer` (linear) è commentato, ma il
  paper e l'header del file descrivono quattro bande di lettura distinte
  sull'asse Y. Riattivarlo o riscrivere la lettura della figura.
- `ex1_dephase/` (vecchia generazione): superata dai gemelli `ex3a`/`ex3b` e
  da `exA_micro`; finché la cartella resta in `examples/` la wildcard del
  Makefile la renderizza comunque. Rimuoverla o spostarla fuori.
- `exA_micro`: lo stream B ha la chiave `pitch` del dephase disattivata in
  attesa del jitter implicito sul pitch (vedi nota nel file); la variante
  globale vs per-parametro è da scegliere all'ascolto.