# Esempi del paper — PythonGranularEngine (PGE)

Gli esempi seguono l'esposizione bottom-up di `sec:architettura` («una
deviazione alla volta»): si parte dallo *stream minimo* — la specifica che si
limita a riprodurre fedelmente il campione sorgente — e ogni esempio successivo
aggiunge **un solo** scostamento, isolando un meccanismo del sistema. La
sequenza culmina in `ex_completo`, la composizione che ricombina i meccanismi
mostrati isolati. Ogni cartella è autocontenuta: sorgente YAML (in git) + una
realizzazione generata (partitura, waveform, spettrogramma — gitignored).
L'audio (`.aif`) va su Zenodo, non in git.

## Nomenclatura: token semantico, niente numeri

Ogni esempio è una **parola-meccanismo** stabile, senza numeri d'ordine. Lo
stesso token è cartella, basename dello YAML e `composition.title`, e si propaga
a tutti gli output del render (`<token>.aif`, `<token>_map.pdf`,
`<token>_waveform.pdf`, `<token>_spectrogram.pdf`, `<token>__<stream>.aif`) e ai
path citati nel paper (`\lstinputlisting` / `\includegraphics`).

**L'ordine di lettura non vive nel filesystem: vive solo in `paper.tex`** (la
sequenza degli `\input` di sezione + l'ordine delle figure dentro la sezione).
Riordinare gli esempi non richiede nessuna rinomina; un file si rinomina solo se
cambia il *concetto* che isola. La tabella qui sotto è ordinata per meccanismo,
non per posizione.

| Cartella | Sezione | Variabile isolata | Andamento atteso | Bit-identico |
|---|---|---|---|---|
| `identity` | `sec:c-e` | nessuna: le 4 chiavi obbligatorie | copia fedele del campione (residuo RMS ≈ −74 dB, vedi comparison) | sì |
| `distribution` | `sec:griglia` | `distribution` 0→1 (densità 10→200) | treno metronomico → tappeto asincrono (leggibile sulla waveform) | no |
| `density` | `sec:density` | *fill factor*: densità 40→400, durata grano fissa | grani separati (pettine) → sovrapposizione continua man mano che la densità sale | no |
| `pointer` | `sec:pointer` | `pointer.speed_ratio` 1→0 | lettura naturale che decelera e si congela su una vocale; invisibile in waveform → è l'esempio che rende necessaria la partitura | sì |
| `deviation` | `sec:deviazione` | i due gemelli (`mask_range`, `mask_dephase`) in un solo YAML, resi come **stems** | una map unica (due subplot impilati) + due audio separati | no |
| `voices` | `sec:voci` | blocco `voices`: 5 voci, `chord dom9` + `pointer linear` + `pan linear` 150° | 5 bande parallele sull'asse Y, colore = trasposizione | sì |
| `scatter` | `sec:voci` | `scatter` 0→1 (4 voci, `distribution: 1` costante) | colonne di onset allineate → griglie temporali indipendenti per voce | no |
| `ex_completo` | `sec:render` | — (composizione completa: 9 stream, ~629 s) | il pezzo finale che ricombina i meccanismi isolati; **audio-first** per Zenodo / presentazione orale | misto |

### `deviation`: i due gemelli in un solo YAML

`deviation` è la **fusione dei due gemelli della deviazione per grano in un
unico YAML**, con i due stream (`mask_range`, `mask_dephase`) resi in modalità
**stems**: lo `score_visualizer` riceve entrambi gli stream e produce **una
sola map** (due subplot impilati, stesso asse temporale), mentre il rendering
audio produce **due file separati**, uno per stream. Si renderizza con la env
`STEMS`:

```bash
STEMS=1 .venv/bin/python paper/examples/render_example.py \
    paper/examples/deviation/deviation.yml
# → deviation__mask_range.aif
#   deviation__mask_dephase.aif
#   deviation_map.pdf            (map unica, i due stream impilati)
```

Senza `STEMS=1` lo stesso YAML viene reso in **mix** (i due stream, entrambi a
`onset 0`, si sovrappongono in un unico file): per questo esempio serve sempre
`STEMS=1`. `make examples` lo gestisce con regole dedicate (target
`deviation__mask_range.aif` come rappresentante del render STEMS, più la
`deviation_map.pdf` annotata, vedi sotto), fuori dal pattern generico `%.aif`.
Restano aperti i lineranges dei listati e le caption delle figure di
`sec:deviazione`.

La `deviation_map.pdf` viene poi passata ad `annotate_panels.py`, che vi stampa
le lettere di pannello `(a)`/`(b)` sui due subplot dei grani: anche questo è
automatico in `make examples` e si ri-genera a ogni modifica di `deviation.yml`.

I gemelli isolati (`range` = solo ampiezza, `dephase` = solo probabilità)
vivono in `_staging/` come riferimento: condividono base (freeze a 0.5) e banda
massima e differiscono **solo** per dove sta l'envelope. Non sono figure del
paper — la figura è la fusione `deviation`.

### `ex_completo`: il pezzo finale

`ex_completo/PGE_cim.yml` è la **composizione completa** (~629 s, 9 stream):
l'ultimo esempio della sequenza, in cui i meccanismi mostrati isolati tornano
insieme. È **audio-first** (bundle Zenodo / presentazione orale), non una figura
a colonna del paper. È incluso nel render automatico di `make examples` come
gli altri (incrementale sui timestamp: la sua lunga durata pesa solo quando il
suo YAML cambia). La sua map porta il **POC automatico** (lente `magnify_auto`
dello `ScoreVisualizer`, sul cluster di grani più denso). Unico esempio il cui
basename (`PGE_cim.yml`) non coincide ancora col token della cartella:
convenzione da sanare.

### POC: la lente d'ingrandimento sulla map

Alcune map portano un **POC** (*point of control*): la lente d'ingrandimento
dello `ScoreVisualizer`, un inset che ridisegna ingrandita una regione del
piano tempo×posizione-di-lettura, con marker e connettori sulla sorgente
(il GridSpec resta invariato — non è uno zoom degli assi). Non è codice di
`render_example.py`: sono le chiavi di config `magnify_auto` / `magnify_targets`
già esposte da PGE, le stesse della CLI `--magnify` / `--magnify-at`.

Quale esempio usa la lente, e come, è dichiarato in un unico posto —
`POC_BY_EXAMPLE` in `render_example.py`, indicizzato sul basename del YAML:

- `distribution` → target esplicito (`t=10 s`, `y=0.5`, a metà dell'asse della
  posizione di lettura);
- `ex_completo` (`PGE_cim`) → automatico (cluster di grani più denso).

Gli esempi non elencati non hanno lente (map identica a prima).

## Riproducibilità: andamento, non bit-identico

Il rendering PGE è stocastico (tendency mask alla Truax): il `random` non è
seminato in produzione, due run dello stesso YAML producono **grani diversi**.
È voluto, non un difetto. Ciò che si conserva è l'**andamento**: densità,
dispersione, traiettoria del pointer, distribuzione delle voci. La stessa
specifica produce sempre la stessa *forma*.

- `identity`, `pointer`, `voices` usano solo default e strategie deterministiche
  (`chord`, `linear`) → **bit-identici** fra le esecuzioni.
- `distribution`, `density`, `deviation`, `scatter` usano gate/campionamenti
  non seminati → **non bit-identici**, ad andamento invariante.

Lo YAML è la fonte di verità spedita: chiunque lo esegue ottiene lo stesso
andamento. Partitura/audio inclusi sono **una** realizzazione di esempio.

## File per cartella

```
<token>/
  <token>.yml                sorgente, fonte di verità          (git)
  <token>.aif                audio renderizzato                 (gitignored → Zenodo)
  <token>_map.pdf            partitura grafica generata         (gitignored → make examples)
  <token>_waveform.pdf       forma d'onda                       (gitignored → make examples)
  <token>_spectrogram.pdf    spettrogramma B&W-safe             (gitignored → make examples)
```

In modalità `STEMS=1` l'audio è invece un file per stream
(`<token>__<stream_id>.aif`), mentre la map resta unica.

Solo `identity/` ha in più `identity_comparison.pdf` (originale vs elaborato sui
primi 2 s, generato da `plot_comparison.py`): è la figura dello stream minimo
nel paper.

## `_staging/` — esempi non attivi

Materiale fuori dal build (un livello sotto il wildcard del Makefile, quindi non
renderizzato): generazioni superate e gemelli isolati conservati come
riferimento. Vedi `_staging/README.md`.

## Gli YAML sono input LaTeX

I file di sezione in `paper/sections/` includono i sorgenti via
`\lstinputlisting[linerange=...]`: i numeri di riga dei `.yml` fanno parte del
paper. Editando un file in modo da spostare righe vanno aggiornati i `linerange`
corrispondenti nel file di sezione (diversi `TODO linerange` sono ancora aperti).

## Come rigenerare

Dalla root del repo:

```bash
make examples                 # incrementale: rirenderizza solo gli .yml cambiati
make examples-clean examples  # forza la rigenerazione completa
```

Il target è incrementale sui timestamp (un `.aif` più recente del suo `.yml`
non viene rirenderizzato) e copre tutti gli esempi, `ex_completo` incluso.
Fa, nell'ordine:

1. `link-refs` (prerequisito automatico) — symlinka i file audio reali dal
   repo PGE sibling (`../PythonGranularEngine/refs`, override con env
   `PGE_REFS=...`) nella `refs/` vuota del submodule. Serve il campione
   sorgente `weNeedToTalkAboutIt.wav` (voce di donna, ~2 s).
2. `render_example.py` — audio (`RENDERER=numpy`, 48 kHz, mix) + partitura
   single-page (`page_duration` = durata dello stream) col PGE **pinnato nel
   submodule**, così la realizzazione corrisponde al codice citato dal paper.
3. `plot.py` — waveform + spettrogramma dall'`.aif` (scala di grigi, larghezza
   colonna CIM, leggibili in stampa B&W).
4. solo per `identity`: `plot_comparison.py` — pannello originale/elaborato.

`make paper` ha `examples` come prerequisito: le figure non sono tracciate in
git e vanno rigenerate prima della compilazione.

Per un singolo esempio:

```bash
.venv/bin/python paper/examples/render_example.py paper/examples/pointer/pointer.yml
.venv/bin/python paper/examples/plot.py paper/examples/pointer/pointer.aif
```

## Audio (Zenodo)

DOI: `TODO` — placeholder fino al caricamento del bundle. Per la submission
double-blind il record va anonimizzato (nessun nome autore, nessun link al repo).

## Disallineamenti noti

- `voices.yml`: `num_voices` è ancora l'envelope sperimentale
  `[[0,5],[.5,1],[1,10]]` e `duration: 2.0` — il paper (caption, claim
  bit-identico, 5 bande parallele) presuppone 5 voci costanti e ~20 s.
  Da fissare prima di rigenerare la figura.
- `scatter.yml`: il blocco `voices.pointer` (linear) è commentato, ma il
  paper e l'header del file descrivono quattro bande di lettura distinte
  sull'asse Y. Riattivarlo o riscrivere la lettura della figura.
- `ex_completo/PGE_cim.yml`: basename non ancora allineato al token della
  cartella (gli altri esempi hanno `<token>/<token>.yml`).
