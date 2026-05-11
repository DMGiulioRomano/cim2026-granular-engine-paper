# [Roads, 2001] Microsound — Capitolo 3: Granular Synthesis

## Posizione nel libro
Capitolo 3 (book pp 85–118 / PDF pp 99–132). Capitolo **core** del libro: teoria + storia delle implementazioni di sintesi granulare digitale.

## Argomento centrale
Survey teorico ed empirico della sintesi granulare digitale (sintesi *con* forme d'onda, distinta dalla granulazione *di* sample trattata in cap. 5). Roads classifica le forme di GS in sei tipi secondo come organizzano i grani sul piano tempo-frequenza, articola gli effetti dei singoli parametri (envelope, durata, waveform, banda, densità, fill factor, spazialità), e ricostruisce la storia delle implementazioni dal 1974 al 2000.

## Struttura del capitolo
- **Theory of Granular Synthesis**
  - Anatomy of a Grain (envelope: Gaussian, quasi-Gaussian, line-segment, triangular, sinc, expodec, rexpodec)
  - The Grain Generator (env_gen + osc + spatial panner)
  - Global Organization of the Grains (6 tipi)
    - Matrices and Screens on the Time-Frequency Plane
    - Pitch-Synchronous Granular Synthesis (PSGS, De Poli/Piccialli)
    - Synchronous and Quasi-Synchronous Granular Synthesis (SGS/QSGS)
    - Pitch and Noise Perception in SGS
    - Asynchronous Granular Synthesis (AGS — clouds)
    - Physical and Algorithmic Models
    - Streams and Clouds of Granulated Samples
  - Spectra of Granular Streams (AM, sidebands, eigenfunction Gaussian)
- **Parameters of Granular Synthesis**
  - Grain Envelope Shape Effects
  - Experiments in Time Reversal
  - Grain Duration Effects
  - Grain Waveform Effects (cloud color: monochrome/polychrome/transchrome)
  - Frequency Band Effects (cumulus / stratus)
  - Density and Fill Factor (Sparse/Covered/Packed)
  - Granular Spatial Effects
- Granular Clouds as Sound Objects
- Cloud Mixtures
- **Implementations of Granular Synthesis**
  - The Author's Implementations (1974 Klang-1 → 1975 Prototype → 1980/81 MIT → 1988 Synthulate/Granulate → 1995 Cloud Generator → SuperCollider)
  - Other Implementations (Truax DMX-1000 1986, Cavaliere/Piccialli PSO Troll 1988, Arfib/Delprat, McCartney Synth-O-Matic/SC2, Helmuth StochGran, IRCAM GIST/FOG, Csound fof/grain/granule, CDP GrainMill, Cornbucket, Audiomulch, Kyma, Behles Granular, CMask, MacPOD, Waveboy, ChaosSynth Miranda)
- Summary

## Concetti chiave
- **Grain** = building block del sound object: forma d'onda + envelope; cattura sia time-domain (start, duration, envelope) che frequency-domain (pitch, spettro)
- **Grain envelope tipologie** (Fig. 3.2): Gaussian (matematicamente più liscio, sidelobe −42 dB); **quasi-Gaussian / Tukey / cosine taper** (Roads 1978a, 1985 — cosine convoluto con rettangolo, sidelobe −18 dB, ampiezza utile maggiore); line-segment 3-stage (Truax 1987/88, risparmio memoria, comb-shaped spectral effects su Gauss + null points); triangular; sinc (sidelobes molto modulanti); expodec (sharp attack, exp decay) e rexpodec (long attack, sudden decay) — usati da Roads stesso
- **Sei organizzazioni globali dei grani** (p. 91 lista canonica): matrices/screens, pitch-synchronous, synchronous/quasi-sync, asynchronous, physical/algorithmic, granulation of sampled
- **Cloud color**: monochrome (1 waveform), polychrome (≥2), transchrome (mutazione lineare nel tempo)
- **Cumulus** vs **Stratus** (frequency band, p. 104): cumulus = scattering uniforme entro banda; stratus = align a pitch-set
- **Fill Factor** (p. 105): FF = density × grain_duration_in_seconds; Sparse FF<0.5, Covered FF~1.0, Packed FF>1.0
- **Soglie di densità percettive** (p. 106): <15 g/s ritmiche; 15–25 flutter; 25–50 grain order disappears; 50–100 texture band; >100 continuous mass
- **Eigenfunction Gaussiana**: per envelope gaussiano, lo spettro AM-modulato è esso stesso gaussiano

## Tassonomia delle organizzazioni di grani (riformulata da p. 91)
| # | Tipo | Logica organizzativa | Real-time tipico? | Equivalente PGE |
|---|------|----------------------|-------------------|-----------------|
| 1 | Matrices/screens (Gabor/Xenakis) | Snapshot tempo×freq, riempimento stocastico/CA | No | non implementato (PGE non opera su screens TF) |
| 2 | Pitch-synchronous (PSGS) | Resintesi analisi-sintesi, grano = risposta filtro per cella | No | non implementato (linea De Poli/Piccialli) |
| 3 | Synchronous/Quasi-Sync (SGS/QSGS) | Stream regolare con delay costante o lievemente random | Sì | `DensityController` distribuzione *sincrona*/blend |
| 4 | Asynchronous (AGS) | Cloud — scattering stocastico nei limiti TF | Sì | `DensityController` *asincrona*; AGS è il modello principale di PGE |
| 5 | Physical/algorithmic | PhISEM (Cook), CA, chaotic functions | Sì | non implementato (no physical modeling) |
| 6 | Granulation of sampled | Scan attraverso buffer, riassemblaggio | Sì | **PointerController + Stream** = cuore di PGE |

PGE materializza i tipi (3), (4), (6) — mappatura diretta su `DensityController` + `PointerController` + `VoiceManager`. Tipi (1), (2), (5) sono al di fuori del dominio progettuale.

## Survey delle implementazioni storiche (con anno/sistema/autore)
**Lineage Roads (deferred → real-time):**
- 1974 Klang-1 (UCSD, B6700 Algol, punched cards, primo AGS)
- 1975 *Prototype* (8-min studio, Algol+MUSIC V)
- 1980 PDP-11/50 MIT, C, score Csound (offline)
- 1981 MIT, granulazione di sample con Music 11 soundin
- 1988 Synthulate / Granulate (Mac II, Music 4C, home studio)
- 1991 Kunitachi (Tokyo) — revisione
- 1992 Paris — porting Csound
- 1995 **Cloud Generator** (Roads+Alexander, MacOS, stand-alone, app A)
- 1996+ SuperCollider 1/2 (real-time)
- 1997 Creatovox (real-time virtuoso, cap. 5)

**Linea real-time DSP-dedicato:**
- 1986 Truax DMX-1000 (cap. 7 e Truax 1988)
- 1988 Cavaliere/Piccialli PSO Troll (Naples, fino a 16 voci, 62.5 kHz)
- 1990 Truax real-time on incoming sound source

**Linea ambienti/programmi (anni '90):**
- IMPAC EMS Stockholm (Hinton 1984, FOF on Atari/Csound by Clarke 1988)
- Sound Mutations (Arfib/Delprat 1992/93, Marseille)
- Synth-O-Matic (McCartney 1990/94, MacOS)
- StochGran (Helmuth 1991, NeXT/IRIX, Cmix front-end) + Max-IRCAM 1993
- Granular control via cellular automata (Orton/Hunt/Kirk 1991, York)
- IRCAM GIST + FOG (Eckel/Rocha-Iturbide/Becker 1995)
- Csound `fof/fof2/grain/granule/fog` (Boulanger 2000, Lippe 1993, Lee 1995)
- CDP GrainMill (Wishart, Granula 1996+)
- Cornbucket (Erbe 1995)
- Audiomulch (Bencina 2000)
- Kyma (1997 Symbolic Sound, real-time + MIDI)
- Granular (Behles, TU Berlin) + Stampede
- CMask (Bartetzki 1997 — per Csound) + Cmask models di Keller/Truax 1998
- MacPOD (Rolfe/Keller 1999, soundfile granulation)
- Waveboy plugin Ensoniq ASR-10
- ChaosSynth (Miranda 1998, CA-driven)
- Hyperprism scattering granulator (Arboretum 1999)

**Lineage MIDI-based:**
- Earl Howard su K2500 (layering streams)
- Barlow *spectastics* (200 notes/sec)

PGE 2026 si inserisce **dopo** la convergenza generale verso il real-time (Roads stesso identifica SC come sua piattaforma di scelta, p. 111): è l'unico esempio di ritorno al deferred-time *post* avvenuta convergenza, e quindi lo legge come scelta non come limite hardware.

## Rilevanza diretta per PGE

**Mappature terminologiche dirette.** Il vocabolario canonico del cap. 3 è il vocabolario di base che la sezione 2 del paper CIM eredita: grain (envelope+waveform), cloud, density, fill factor, cumulus/stratus, monochrome/polychrome, asynchronous/synchronous, granulation of sampled sound. PGE riusa questi termini *senza ridefinirli*.

**Trade-off composizionale (p. 91): pietra angolare del DSL PGE.**
> «As a general principle of synthesis, we can trade off instrument complexity for score complexity. A simple instrument suffices, because the complexity of the sound derives from the changing combinations of many grains. Hence we must furnish a massive stream of control data for each parameter of the instrument.» (p. 91)

Roads formula nel 2001 il principio architetturale che giustifica YAML+LSP in PGE 2026: granular = strumento semplice + score densissimo. PGE adotta la posizione massima del trade-off (instrument minimo: pointer+envelope+osc; score gigantesco: orchestrazione YAML multi-stream con strategie parametriche). PGE-ls è la risposta diretta al problema del *massive stream of control data* (p. 87, p. 91).

**Sette parametri AGS (p. 96): precursore diretto della specifica YAML stream.** Roads enumera per la cloud:
1. start-time + duration
2. grain duration (constant / time-varying / random / parameter-dependent)
3. density (with max depending on implementation; can vary over cloud)
4. frequency band (high/low curves o pitch-set)
5. amplitude envelope of cloud
6. waveform(s) within grains
7. spatial dispersion

Mappa quasi 1:1 sulla specifica YAML stream PGE (`start_time`, `duration`, `grain_duration`, `density`/`fill_factor`, `pitch_set`/`pitch_band`, `amplitude`, `waveform`, `pan`/`spatial`). I 7 parametri AGS sono lo schema concettuale che PGE-ls valida.

**Quattro classi di grain duration (p. 101).** Costante / time-varying / random / parameter-dependent. PGE supporta tutte e quattro via `Envelope` strategies + dephase stocastico — schema acquisito.

**Fill factor → `FillFactorStrategy`.** P. 105 Sparse/Covered/Packed è esattamente il ragionamento dietro `FillFactorStrategy` di PGE (vedi `pge/density-controller.md`): il composer pensa in termini di copertura (FF), non di density assoluta. PGE traduce internamente FF → density via grain_duration corrente.

**Soglie di densità percettive (p. 106) → vincolo per partitura grafica (sezione 4 paper CIM).** Le soglie 15/25/50/100 grani-sec sono il razionale per cui la rappresentazione visiva PGE *deve* attraversare scale diverse (un punto-grano a 5 g/s vs una banda continua a >100 g/s sono fenomeni percettivi distinti).

**Cumulus/Stratus → `PitchController` PGE.** Distinzione p. 104 tra random scatter in band (cumulus) e align a pitch-set (stratus) corrisponde alle due modalità del `PitchController` PGE (`StochasticPitchStrategy` con range vs `pitch_set`).

**Granulation of sampled sound (tipo 6) come dominio principale di PGE.** Roads tratta brevemente la granulation in cap. 3 (p. 98) e rinvia al cap. 5; PGE è esattamente di tipo 6 + tipo 4 (cloud asincrona di grani estratti da buffer).

**Cloud Generator (1995) come precursore architetturale.** Roads cita il proprio Cloud Generator come *teaching aid* + ricerca + composizione (p. 111), e rinvia all'appendice A. Per PGE, Cloud Generator è il riferimento storico più vicino: stand-alone, file-based, MacOS, parametric specification of clouds. Vedi `roads2001-appA-cloud-generator.md` per tabella corrispondenze CG↔PGE.

**Spettro AM e eigenfunction gaussiana (p. 99).** Per envelope gaussiano lo spettro è gaussiano. Implicazione PGE: la scelta dell'envelope (in YAML) è scelta sulla *forma spettrale globale*, non solo sulla forma temporale. Da menzionare in sezione 2 paper CIM.

## Collegamento alla tesi centrale

**Loop lungo (Atto 3).** Cap. 3 è il documento più completo della tradizione "convergenza verso real-time": Roads chiude la sezione Author's Implementations dichiarando «SuperCollider is my synthesis environment of choice at the present time» (p. 111). PGE 2026 esplicita la bifurcazione: assume tutto il vocabolario e il trade-off di Roads cap. 3, ma li dirige verso un workflow deferred-time iterativo. Non è ignoranza dei progressi real-time, è scelta successiva ad essi.

**Contributo (1) DSL+LSP.** Le citazioni p. 87 (massive stream of control data) e p. 91 (instrument↔score complexity trade-off) sono il razionale tecnico-compositivo del DSL PGE.

**Contributo (2) Partitura grafica con asse Y = posizione-buffer.** Roads cap. 3 *non* propone un asse Y dedicato alla buffer position; le sue figure (3.4, 3.6) usano il piano canonico tempo×frequenza/amplitudine. PGE introduce un piano nuovo perché lavora su tipo (6) granulation of sampled, dove la buffer position è il parametro che la freq/pitch non comunica.

**Contributo (3) STEMS workflow.** Cap. 3 menziona "Cloud Mixtures" come strategia di composizione (p. 108): «To create such textures, the most flexible strategy is first to generate each individual cloud. Then to mix the clouds to precisely order and balance their flow in time.» Questo è esattamente il workflow STEMS PGE: per-stream rendering + mixing successivo. Roads articola il principio nel 2001; PGE lo automatizza nel 2026 (cache incrementale + Reaper export).

## Quote chiave
> «Granular synthesis requires a massive amount of control data. If *n* is the number of parameters per grain, and *d* is the density of grains per second, it takes *n* times *d* parameter values to specify one second of sound. Since *n* is usually greater than ten and *d* can exceed one thousand, it is clear that a global unit of organization is necessary for practical work. That is, the composer specifies the sound in global terms, while the granular synthesis algorithm fills in the details.» (p. 87)

> «As a general principle of synthesis, we can trade off instrument complexity for score complexity. A simple instrument suffices, because the complexity of the sound derives from the changing combinations of many grains. Hence we must furnish a massive stream of control data for each parameter of the instrument.» (p. 91)

> «The main forms of granular synthesis can be divided into six types, according to how each organizes the grains: matrices and screens on the time-frequency plane; pitch-synchronous overlapping streams; synchronous and quasi-synchronous streams; asynchronous clouds; physical or abstract models; granulation of sampled sound.» (p. 91)

> «To create such textures, the most flexible strategy is first to generate each individual cloud. Then to mix the clouds to precisely order and balance their flow in time. To create a polychrome cloud texture, for example, several monochrome clouds, each with a different grain waveform are superimposed in a mixing program.» (p. 108)

> «SuperCollider is my synthesis environment of choice at the present time.» (p. 111) — *contesto: dichiarazione esplicita della convergenza Roads → real-time, dopo 25 anni di esperimenti deferred-time. PGE 2026 si posiziona come bifurcazione cosciente di questa convergenza.*

## Sezioni del paper CIM 2026 dove citare

- **Sezione 2 (Sintesi granulare).** Capitolo *principale* per la cornice tassonomica. Citare: 6 organizzazioni (p. 91), 7 parametri AGS (p. 96), trade-off instrument/score (p. 91), terminologia canonica (cumulus/stratus, monochrome/polychrome, FF Sparse/Covered/Packed).
- **Sezione 3 (Architettura PGE).** Quote p. 87 e p. 91 come razionale del DSL+LSP (contributo 1). Trade-off come decisione architetturale ereditata.
- **Sezione 4 (Partitura grafica).** Soglie densità percettive (p. 106) come vincolo per il design del visualizzatore (zoom multi-scala).
- **Sezione 5 (Caso compositivo).** Cloud Mixtures (p. 108) come legittimazione storica del workflow STEMS PGE.
- **Sezione 1 (Introduzione).** Quote p. 111 (SC come ambiente di scelta di Roads) come pivot della narrazione tre atti — la convergenza verso real-time è documentata da Roads stesso, PGE è la bifurcazione successiva.
