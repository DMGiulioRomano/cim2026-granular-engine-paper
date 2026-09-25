# Slide dell'intervento orale — CIM 2026

Bozza della struttura, 2026-09-25. Fonte unica: `paper/sections/*.tex`.
Formato: reveal.js in `slides/` (`make slides-serve`). Intervento di 10 minuti
+ 5 di domande, 10 slide.

## Principio

Le slide seguono il percorso del paper, dal basso e uno scostamento alla volta:
ogni slide di esempio mostra **le sole chiavi che cambiano**, la **MAP** e,
dove serve, un **ascolto breve**. L'argomento non si spiega a voce prima di
mostrarlo: si mostra la MAP, poi si dice che cosa vi si legge.

I due contributi del paper devono restare riconoscibili:
- **la MAP** (slide 3–4, poi in ogni esempio);
- **il gate di probabilità** (slide 7, la più lunga).

## Budget di tempo (600 s)

| # | Slide | Tempo | Ascolto |
|---|---|---|---|
| 1 | Titolo | 0:20 | – |
| 2 | Il problema | 0:50 | – |
| 3 | L'ambiente | 1:00 | – |
| 4 | Condizioni minime + come si legge la MAP | 1:10 | `identity` 2 s |
| 5 | La posizione di lettura | 1:10 | `pointer` 7 s |
| 6 | Inter-onset time | 1:00 | `distribution` ~8 s |
| 7 | Ampiezza e probabilità | 1:30 | `deviation` a/b ~5+5 s |
| 8 | Dalla voce singola all'esempio completo | 0:50 | `complete_example` ~8 s |
| 9 | Le voci | 1:10 | `PGE_voices` ~10 s |
| 10 | Conclusioni | 1:00 | – |
| | **Totale** | **10:00** | ~45 s |

## Slide per slide

### 1. Titolo
- **Testo**: *PythonGranularEngine: un ambiente dichiarativo per la
  granulazione e la sua mappa sinottica*. Giulio Romano De Mattia,
  Conservatorio «A. Casella», L'Aquila.
- **Materiale**: link al repository, DOI del software (10.5281/zenodo.22177167)
  e degli esempi (10.5281/zenodo.22176140).

### 2. Il problema — introduzione
- **Messaggio**: pochi secondi di granulazione sono decine di migliaia di
  eventi. La event list non si legge, e dall'audio non si risale ai parametri:
  senza una rappresentazione della popolazione si procede per tentativi.
- **Materiale**: il paragone fra una event list (qualche centinaio di righe
  di `.sco` che scorrono) e il file audio corrispondente. Da generare.
- **Fonte**: introduzione (Roads 1978, Truax 1988, CMask).

### 3. L'ambiente — `sec:architettura`
- **Messaggio**: specifica YAML → lista di `Grain` (rappresentazione
  intermedia) → tre back-end audio, export, MAP. Lo YAML è notazione
  prescrittiva, la MAP descrittiva (Seeger).
- **Materiale**: diagramma della pipeline. Da disegnare in SVG
  (`paper/figures/arch-pipeline.tikz` non è nel paper e codifica la lettura
  della wiki, con lo Stream come IR: non riusarlo tale e quale).
- **Nota a voce**: finalità pedagogica, vocabolario di Roads e Truax.

### 4. Le condizioni minime di esistenza — `sec:c-e`
- **Messaggio**: due chiavi bastano (`stream_id`, `sample`); ciò che non è
  scritto vale come default. Qui si impara a leggere la MAP: ascissa tempo,
  ordinata posizione di lettura, forma d'onda a sinistra, poligono per grano,
  testa = verso + finestra, colore = trasposizione.
- **Materiale**: `identity.yml` righe 3–7; `identity_map` con la lente.
- **Ascolto**: `identity.aif` intero (2 s), poi `voice.wav` originale per il
  confronto.

### 5. La posizione di lettura — `sec:pointer`
- **Messaggio**: la MAP non ricalca la `speed_ratio` ma il suo integrale.
  Wrap-around a ~1,35 s, lettura all'indietro fra 2 e 3,5 s, coda congelata.
- **Materiale**: `pointer.yml` righe 38–45; `pointer_map`.
- **Ascolto**: `pointer.aif` intero (7 s).
- **Ponte**: con la lettura ferma si vede la griglia di emissione.

### 6. Inter-onset time — `sec:griglia`
- **Messaggio**: `density` e `distribution`; `distribution` interpola fra
  griglia sincrona e asincrona (eq. IOT). Righe spettrali dove la griglia è
  sincrona e densa, che si smerigliano quando diventa asincrona.
- **Materiale**: `distribution.yml` righe 38–44; `distribution_map` +
  spettrogramma impilati; eq. IOT in piccolo.
- **Ascolto**: estratto ~8 s attorno al passaggio sincrono → asincrono. Da
  scegliere ascoltando.

### 7. Ampiezza e probabilità — `sec:deviazione` (contributo)
- **Messaggio**: stessa traiettoria, stessa ampiezza massima. (a) cresce
  l'ampiezza: cuneo. (b) cresce la probabilità: linea che diventa nuvola.
  Il gate `g_n ~ Bernoulli(p)` rende i due assi indipendenti; per p ≡ 1 si
  torna a Truax. Precedenti: ICMS (probabilità fissa, switch discreti), EC2
  *intermittency* (gate sull'emissione, non sulla deviazione).
- **Materiale**: `deviation.yml` (le due chiavi che differiscono:
  `offset_range` come inviluppo vs `deviation_probability.pointer`);
  `deviation_annotated`; eq. `gated` sotto la figura.
- **Ascolto**: A/B dei due stem, ~5 s ciascuno, dalla seconda metà dove la
  differenza è più udibile. Da scegliere ascoltando.

### 8. Dalla voce singola all'esempio completo — `sec:dimensioni`, `sec:completo`
- **Messaggio**: sovrapponendo i parametri già visti (più durata del grano e
  pan Mid-Side) la MAP resta leggibile: la finestra passa da Hann a
  `rexpodec` a Bartlett e lo si legge nella forma della testa.
- **Materiale**: `complete_example_map` con le lenti; poche righe dello YAML
  (`grain.envelope.states`), non il listato intero.
- **Ascolto**: estratto ~8 s.
- **Scelta aperta**: fondere qui `duration`, o tenerlo come slide di riserva.

### 9. Le voci — `sec:voci`
- **Messaggio**: moltiplicare lo stream con uno scarto per voce (pitch,
  pointer, onset, pan); `num_voices` come inviluppo (50 → 7 → 70);
  `scatter` decide se le voci condividono la stessa scansione temporale.
- **Materiale**: `PGE_voices.yml` righe 48–62; `PGE_voices_map`.
- **Ascolto**: estratto ~10 s dalla seconda metà (le bande si sfasano).

### 10. Conclusioni — `sec:conclusioni`
- **Messaggio**: il gate aggiunge un terzo grado alla tendency mask; la
  specifica si versiona e si rigenera col seed; la MAP sostituisce i
  tentativi. Tre limiti: posizione e non contenuto, assi senza covarianza,
  altezza solo nel colore.
- **Materiale**: tre righe + link e QR al repository.

## Slide di riserva (dopo la 10, per le domande)

- `probability`: la sola probabilità a quattro gradini + `tab:jitter`.
- `duration`: la prima texture complessa (se non fusa nella slide 8).
- Eq. IOT per esteso e la nota sul sincrono di De Poli–Piccialli.
- Precedenti della MAP: Truax 1988 Fig. 4, poligoni di Roads, IRIN.
- La discrepanza sulla «copia fedele»: residuo −73,9 dB a 48 kHz con Hann
  simmetrica (cfr. `wiki/concepts/finestratura-come-modulazione.md`).

## Decisioni aperte

1. Slide 8: fondere `duration` o no.
2. Slide 2: come mostrare l'illeggibilità della event list (scroll di `.sco`,
   conteggio dei grani, altro).
3. Estratti audio: punti di attacco da scegliere ascoltando; poi un target
   `make` che li tagli con ffmpeg.
4. Lingua delle slide: il paper è in italiano con abstract inglese.
