# Micromontage

## Definizione

Micromontage = tecnica compositiva in cui il materiale finale è costruito per *assemblaggio puntuale* di centinaia o migliaia di sample brevi (tipicamente 1–100 ms, scala microsonora), ciascuno trattato come atto compositivo singolo con memoria delle proprie trasformazioni (envelope, pitch shift, phase shift, pan, filtering). Non è granulazione algoritmica indifferenziata: ogni particella è una decisione, anche quando generata da regole globali.

La definizione operativa è codificata in Roads 2001 cap. 5 (pp. 182–187) come *Transformation of Microsound* — micromontage è una delle tecniche di trasformazione sample-based che operano alla scala microtemporale, distinta da granulation pura per il fatto che il composer mantiene il controllo sulla singola particella.

## Tassonomia (Roads 2001, pp. 183–185)

Roads distingue tre forme di micromontage in base alla superficie compositiva:

1. **Micromontage in a Graphical Sound Editing and Mixing Program** — direct manipulation in DAW (MacMix 1987, Pro Tools, Digital Performer). Fig. 5.1 mostra 136 file in 12 tracce. *Polo grafico*.
2. **Micromontage by Script** — linguaggi tipo Music N (Csound `soundin` + `loscil`) o note-list testuali. *Polo testuale a basso livello*.
3. **Micromontage by Algorithmic Process** — specifica ad alto livello (lista di sound file, segmenti, *overall tendencies*) → generazione automatica di migliaia di micro-eventi. *Polo testuale a alto livello*. PGE è la prosecuzione di questa forma con DSL strutturato (cfr. [[roads2001-ch05-transformation]] sezione "Micromontage by algorithmic process come anticipatore del DSL YAML").

Roads stesso (p. 185): «*Instead of specifying each particle manually, however, a computer program handles their extraction and time-scattering. The program reads a high-level specification of the montage from the composer.*»

## Linea storica e teorica

| Anno | Autore | Contributo |
|------|--------|-----------|
| 1982/85/95 | Vaggione | *Octuor*, *Thema*, *Schall* — paradigma compositivo: oggetto sonoro come *categoria operatoria* assemblato per puntuale singolarità (cfr. [[vaggione1991]]) |
| 1991/1996 | Vaggione | Teorizzazione: *object-based composition*, *écriture directe ↔ traitement algorithmique*, gestalt da local singularities (cfr. [[vaggione1991]], [[vaggione1996]]) |
| 2001 | Roads | Cap. 5 *Microsound*: catalogo sistematico delle tre forme + endorsement deferred (p. 188: «*Asynchronous playback from a sound file allows much more freedom than real-time granulation*») (cfr. [[roads2001-ch05-transformation]]) |
| 2002 | Vaggione | *Décorrélation microtemporelle*: phase shift come attributo morfologico-spaziale per-particella. Quote-pietra p. 7: «*on sera bien obligés de passer par des micromontages afin de construire des ensembles musicaux d'une certaine complexité*» — primato del micromontaggio come tecnica abilitante (cfr. [[vaggione2002]]) |
| 2003 | Vaggione | Sintesi tarda del programma (cap. 4 in Solomos/Soulez/Vaggione, *Formel/Informel*): *objet = catégorie opératoire* + *réseau d'objets numériques* + *micro-monde du compositeur*. Distinzione *figure/objet* (p. 101) come mapping concettuale grano/Stream; *unité multiple* (pp. 98-99) come descrizione strutturale del file YAML come oggetto compositivo unitario contenente codes+données+partitions+scripts+sons (cfr. [[solomos2003-ch04-vaggione-composition-moyens-informatiques]], [[solomos2003-ent04-de-loperatoire]]) |
| 2004 | Caires | IRIN: software Max/MSP standalone offline che implementa micromontage object-based su superficie grafica (Sample → Figure → Meso → Timeline); allievo di Vaggione, materializza in software il programma transformational (cfr. [[caires2004]]) |
| 2005 | Roads | *Art of Articulation* (Contemporary Music Review): Tar (1987) Fig. 2 documenta il cmusic code reale — instrument + note-list testuale di 870 microevents — come *prototipo storico del DSL parametrico* per micromontage script (cfr. [[roads2005]]); Schall (1994) workflow *progressive enrichment* (p. 302) come formulazione operativa del loop lungo prima della lettera |
| 2026 | PGE | Forma algorithmic (Roads) + DSL YAML strutturato; loop lungo come metodologia per abitare micromontage compositivamente |

La linea attraversa quattro decenni con un invariante: *memoria di tutte le azioni*. Caires 2004 p. 219 lo espone come imperativo architetturale: «*a memory of all actions and respective data involved within the process of creating the tiniest sound particle is needed so that a consistent proliferation of the musical material can be achieved*». PGE eredita lo stesso imperativo via YAML versionato + cache incrementale per-stream.

## Rilevanza per PGE

PGE è la **forma algorithmic di micromontage by DSL**: il YAML è la *high-level specification* di Roads p. 185 portata a sistema con schema validato, LSP, e generazione deterministica di eventi (`Stream` → `Generator` → `.sco`). Nessuna invenzione di paradigma: PGE implementa il programma Roads/Vaggione con strumenti del 2020.

Posizionamento rispetto alle altre forme:
- **Vs. polo grafico (IRIN, Caires 2004)**: stessa famiglia di problemi (memoria, gerarchia, partitura come strumento), superficie compositiva opposta — direct manipulation vs scrittura testuale. Il [[score-visualizer]] di PGE non è superficie editoriale (come Timeline IRIN) ma rappresentazione ispezionabile dell'output: inversione di flusso a parità di categoria.
- **Vs. polo script (Csound note-list)**: PGE astrae il singolo grano via `Envelope`/strategy invece di enumerarlo. Roads p. 185 osserva che l'enumerazione manuale del grano è impraticabile oltre la dozzina di eventi — il DSL risolve esattamente questo.

Connessione alla tesi centrale del paper: micromontage *richiede* tempo differito per definizione (memoria di tutte le azioni, ordine arbitrario di estrazione dal buffer, granulator inside editor con regenerable output). Il ritorno volontario di PGE al deferred non è anacronismo: è la postura nativa della tecnica.

## Fonti

- [[roads2001-ch05-transformation]] — definizione e tassonomia tre forme, granulation parameters list, endorsement deferred granulation
- [[roads2005]] — Tar Fig. 2 cmusic note-list = prototipo storico del DSL micromontage by script; Schall *progressive enrichment* come pattern operativo del loop lungo; IRIN 24 variations Fig. 3 con asse Y non-pitch come categoria del visualizer PGE
- [[vaggione1991]] — *object-based composition* come radice teorica
- [[vaggione1996]] — *interaction forte* écriture ↔ algorithme, déclaration d'attribut généralisé
- [[vaggione2002]] — décorrélation microtemporelle + primato del micromontaggio (p. 7)
- [[solomos2003-ch04-vaggione-composition-moyens-informatiques]] — *objet = catégorie opératoire / unité multiple* + *réseau d'objets numériques* + *micro-monde* + distinzione *figure/objet*: sintesi tarda del programma object-based
- [[solomos2003-ent04-de-loperatoire]] — triangolarité interaction = input/output/opérateur (p. 230) + OOP come paradigm shift abilitante (pp. 232-233): legittimazione storico-tecnica del DSL come configurazione opératoire
- [[caires2004]] — IRIN come materializzazione operativa offline del paradigma object-based + décorrélation
- [[score-visualizer]] — implementazione PGE della partitura per micromontage (asse Y = posizione buffer)

## Sezioni del paper CIM 2026 dove citare

- **Sezione 1** (introduzione, narrazione tre atti): il micromontage attraversa entrambi i poli (offline Vaggione/Caires, real-time Truax) senza coincidere con nessuno — è la tecnica che *rende necessario* il deferred indipendentemente dalla disponibilità del real-time.
- **Sezione 2** (sintesi granulare): tassonomia Roads delle tre forme come quadro di posizionamento; PGE = forma algorithmic con DSL.
- **Sezione 3** (architettura PGE): YAML come *high-level specification* nel senso di Roads p. 185; gerarchia Stream/Voice/Controller come materializzazione dell'oggetto Vaggione.
- **Sezione 4** (partitura grafica): contrasto con Timeline IRIN (superficie editoriale) — `score_visualizer` PGE come output ispezionabile sulla stessa categoria.
