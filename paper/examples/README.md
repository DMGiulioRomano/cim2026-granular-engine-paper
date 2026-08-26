# Esempi del paper — PythonGranularEngine (PGE)

Gli esempi seguono l'esposizione bottom-up di `sec:architettura` («una
deviazione alla volta»): si parte dallo *stream minimo* — la specifica che si
limita a riprodurre fedelmente il campione sorgente — e ogni esempio successivo
aggiunge **un solo** scostamento, isolando un meccanismo del sistema. La
sequenza culmina in `complete_example`, la composizione che ricombina i
meccanismi mostrati isolati. Ogni cartella è autocontenuta: sorgente YAML (in git) + una
realizzazione generata (partitura, waveform, spettrogramma — gitignored).
L'audio (`.aif`) va su Zenodo, non in git.

## Nomenclatura: token semantico, niente numeri

Ogni esempio è una **parola-meccanismo** stabile, senza numeri d'ordine. Lo
stesso token è cartella e basename dello YAML, e si propaga a tutti gli output
del render (`<token>.aif`, `<token>_map.pdf`, `<token>_waveform.pdf`,
`<token>_spectrogram.pdf`, `<token>__<stream>.aif`) e ai path citati nel paper
(`\lstinputlisting` / `\includegraphics`). Il blocco `composition:` è
facoltativo — `duration` e `complete_example` non ce l'hanno — e dove c'è
riporta lo stesso token.

Due eccezioni note: `voices/PGE_voices.yml` (basename non allineato) e
`deviation/`, STEMS-only, che non produce il `<token>.aif` singolo. Entrambe
in coda, sotto «Disallineamenti noti».

**L'ordine di lettura non vive nel filesystem: vive solo in `paper.tex`** (la
sequenza degli `\input` di sezione + l'ordine delle figure dentro la sezione).
Riordinare gli esempi non richiede nessuna rinomina; un file si rinomina solo se
cambia il *concetto* che isola. La tabella qui sotto è ordinata per meccanismo,
non per posizione.

| Cartella | Sezione | Variabile isolata | Andamento atteso | Stocastico |
|---|---|---|---|---|
| `identity` | `sec:c-e` | nessuna: le 4 chiavi obbligatorie | copia fedele del campione (residuo RMS gain-matched **−38,1 dB**, misurato 2026-08-27 col PGE pinnato a v8.0.0; il valore −74 dB citato prima qui e in `\notaBande` non è riproducibile — vedi comparison) | no |
| `pointer` | `sec:pointer` | `pointer.speed_ratio` 1→0 | lettura naturale che decelera e si congela su una vocale; invisibile in waveform → è l'esempio che rende necessaria la map | no |
| `distribution` | `sec:griglia` | `distribution` 0→1 (densità 10→200) | treno metronomico → tappeto asincrono (leggibile sulla waveform) | sì |
| `deviation` | `sec:deviazione` | i due gemelli (`mask_range`, `mask_probability`) in un solo YAML, resi come **stems** | una map unica (due subplot impilati) + due audio separati | sì |
| `probability` | `sec:deviazione` | `deviation_probability` 0→100 a gradini, **senza alcun range** | banda netta → nuvola per gradi: il quarto angolo del quadrato 2×2, la micromodulazione implicita | sì |
| `duration` | `sec:dimensioni` | durata del grano 50→1→150 ms, con densità, `distribution`, `pan` e `pan_range` in movimento | più dimensioni sovrapposte in un'unica texture; la durata tocca ~1 ms a metà esempio (lente POC) | sì |
| `voices` | `sec:voci` | blocco `voices`: `num_voices` a envelope, `scatter` 0→1, strategie `step` su pitch/pan e `linear` su pointer | fascio di bande sull'asse della posizione di lettura che si sgancia progressivamente nella nuvola di chiusura | sì |
| `complete_example` | `sec:completo` | — (composizione completa: 1 stream, ~32 s) | il pezzo finale che ricombina i meccanismi isolati | sì |

### `deviation`: i due gemelli in un solo YAML

`deviation` è la **fusione dei due gemelli della deviazione per grano in un
unico YAML**, con i due stream (`mask_range`, `mask_probability`) resi in modalità
**stems**: lo `score_visualizer` riceve entrambi gli stream e produce **una
sola map** (due subplot impilati, stesso asse temporale), mentre il rendering
audio produce **due file separati**, uno per stream. Si renderizza con la env
`STEMS`:

```bash
STEMS=1 .venv/bin/python paper/examples/render_example.py \
    paper/examples/deviation/deviation.yml
# → deviation__mask_range.aif
#   deviation__mask_probability.aif
#   deviation_map.pdf            (map unica, i due stream impilati)
```

Senza `STEMS=1` lo stesso YAML viene reso in **mix** (i due stream, entrambi a
`onset 0`, si sovrappongono in un unico file): per questo esempio serve sempre
`STEMS=1`. `make examples` lo gestisce con regole dedicate (target
`deviation__mask_range.aif` come rappresentante del render STEMS, più la
`deviation_map.pdf` annotata, vedi sotto), fuori dal pattern generico `%.aif`.
Restano aperti i lineranges dei listati e le caption delle figure di
`sec:deviazione`.

I due gemelli condividono base (freeze a 0.5) e banda massima e differiscono
**solo** per dove sta l'envelope: `mask_range` lo mette sull'ampiezza
(`pointer.offset_range` 0→0.35, gate sempre aperto), `mask_probability` sulla
probabilità (`deviation_probability.pointer` 0→100, ampiezza fissa al massimo).
Non esistono più come esempi separati: la figura del paper è la fusione.

La `deviation_map.pdf` viene poi passata ad `annotate_panels.py`, che stampa
`(a)` e `(b)` sui **pannelli dei grani**, uno per stream, e riesporta come
`deviation_annotated.pdf` (è questa che il paper include). Automatico in
`make examples`, si rigenera a ogni modifica di `deviation.yml`.

Riconosce le corsie envelope dal label `env:<stream_id>` che il visualizer
assegna, non dalla posizione nella griglia: il layout dello `ScoreVisualizer`
è già cambiato una volta (da un pannello envelope unico in coda a uno per
stream, con righe interlacciate) e il filtro posizionale finì per annotare il
subplot sbagliato — col numero giusto di lettere, quindi in silenzio. Se i
pannelli dei grani non sono uno per stream lo script ora si ferma con un
errore invece di produrre una figura plausibile e falsa.

### `complete_example`: il pezzo finale

`complete_example/complete_example.yml` è la **composizione completa** (un
solo stream, ~32 s): l'ultimo esempio della sequenza, in cui i meccanismi
mostrati isolati tornano insieme — densità e `distribution` a envelope, durata
del grano fino a 1 ms, catalogo di finestre che transita
(`hanning`/`rexpodec`/`bartlett`), pitch che sale di due ottave abbondanti nel
tratto finale, `offset_range` che apre la nuvola. È una figura del paper
(`sec:completo`) e insieme il pezzo del bundle audio. La sua map porta due
lenti POC esplicite (vedi sotto).

### POC: la lente d'ingrandimento sulla map

Alcune map portano un **POC** (*point of control*): la lente d'ingrandimento
dello `ScoreVisualizer`, un inset che ridisegna ingrandita una regione del
piano tempo×posizione-di-lettura, con marker e connettori sulla sorgente
(il GridSpec resta invariato — non è uno zoom degli assi). Non è codice di
`render_example.py`: sono le chiavi di config `magnify_auto` / `magnify_targets`
già esposte da PGE, le stesse della CLI `--magnify` / `--magnify-at`.

Quale esempio usa la lente, e come, è dichiarato in un unico posto —
`POC_BY_EXAMPLE` in `render_example.py`, indicizzato sul basename del YAML:

- `distribution` → due target espliciti (`t=10 s` e `t=20,5 s`, `y≈1,035`),
  sui due regimi della griglia;
- `duration` → un target (`t=5 s`, zoom 13×), sui grani più brevi (~1 ms a
  metà esempio), illeggibili a piena scala;
- `complete_example` → due target (`t=13 s` sulla nuvola aperta da
  `offset_range`, `t=27,5 s` sul tratto finale trasposto; `y≈0,6` = linea di
  lettura congelata).

Gli esempi non elencati non hanno lente (map identica a prima).

## Riproducibilità: il seed è parte della specifica

**Aggiornato 2026-08-27 (PGE v8.0.0).** La versione precedente di questa sezione
diceva che il `random` non è seminato in produzione e che due run dello stesso
YAML danno grani diversi. Non è più così: le issue #81/#154/#169 hanno
introdotto il seeding deterministico in `src/pge/shared/seeding.py`.

- Con `seed:` dichiarato top-level nello YAML, ogni sito stocastico riceve un
  RNG derivato via `hashlib.sha256` da `f"{seed}:{stream_id}:{componente}"`.
  `hashlib` non dipende da `PYTHONHASHSEED`: la realizzazione è **identica fra
  processi e fra macchine**.
- Senza `seed:`, il Generator ne deriva uno dal timestamp e lo stampa
  (`[SEED] ... Per riprodurre questo run aggiungi 'seed: N' allo YAML`): anche
  un run non dichiarato resta ricostruibile a posteriori.
- Ogni sito stocastico ha il proprio stream RNG (nome del Parameter,
  `gate:<chiave>`, `iot`, `window`, `detune`). Solo/mute, cache degli stem e
  ordine di materializzazione non alterano i draw degli altri componenti:
  mutare uno stream lascia identici i grani degli altri.

Verifica empirica su `probability.yml`, tre processi separati con
`PYTHONHASHSEED=random`: con `seed: 7` sempre 998 grani e fingerprint
`71136596c62514d6`; con `seed: 8` cambia; senza seed cambia a ogni run.

Gli YAML di questa cartella dichiarano il seed, quindi le figure stampate nel
paper e i file audio dell'archivio sono **la** realizzazione che si riottiene
eseguendoli, non una fra le tante.

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

`deviation/` è l'eccezione al `<token>.aif` singolo: essendo STEMS-only produce
`deviation__mask_range.aif` e `deviation__mask_probability.aif`, più
`deviation_map.pdf` e la sua versione annotata `deviation_annotated.pdf` (che è
quella inclusa dal paper). Non ha waveform né spettrogramma: il Makefile la
esclude dal pattern generico.

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
non viene rirenderizzato) e copre tutti gli esempi, `complete_example` incluso.
Fa, nell'ordine:

1. `link-refs` (prerequisito automatico) — symlinka i file audio reali dal
   repo PGE sibling (`../PythonGranularEngine/refs`, override con env
   `PGE_REFS=...`) nella `refs/` vuota del submodule. Serve il campione
   sorgente `voice.wav` (voce di donna, ~2 s).
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

## Audio (OSF)

Archivio ad accesso aperto (view-only anonimo per la submission double-blind):
`https://osf.io/xqmh5/?view_only=5a6d9ac26adb466697477801e73b153f`.
Citato nella footnote del cappello di `sec:architettura`. Per il double-blind
il view-only token non basta: va spuntato anche "Anonymize contributor list for
this link" su OSF, altrimenti il nome del contributor resta visibile.

## Disallineamenti noti

- `voices/PGE_voices.yml`: **l'intestazione del file è stale**, non il paper.
  Il commento in testa promette «5 voci con strategie DETERMINISTICHE, pitch
  `chord dom9`, pan `linear spread 150`, BIT-IDENTICO»; il contenuto ha
  `num_voices` a envelope (50→7→70), `pitch: {strategy: step, step: 12}`,
  `pan: {strategy: step}`, più `scatter` 0→1, `distribution` e
  `deviation_probability` sul volume — quindi stocastico e non bit-identico.
  `sec:voci` descrive già la versione corrente (voci che «si sganciano in
  istanti diversi a ogni esecuzione»): da riallineare è il commento YAML.
- `voices/PGE_voices.yml`: unico esempio il cui basename non coincide col
  token della cartella (gli altri hanno `<token>/<token>.yml`). Funziona — il
  paper referenzia `examples/voices/PGE_voices_map` — ma rompe la convenzione.
- `graph/class_diagram.puml` (fuori da `examples/`, ma tocca chi legge questi
  YAML): non più rigenerabile su PGE v7, vedi issue #37.
