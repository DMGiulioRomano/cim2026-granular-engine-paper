#!/usr/bin/env python3
"""
gen_grammar_tree.py — genera l'albero della grammatica YAML (R1.M6, decisione D4)
leggendo domini, enum e bounds dal PGE pinnato nel submodule.

Cosa scrive
-----------
Il corpo dell'albero in figures/grammar_tree.tex, testo YAML puro. La sezione lo
include dentro il proprio float con

    \\lstinputlisting[language=yaml,firstline=4]{figures/grammar_tree.tex}

(`firstline=4` salta le tre righe di intestazione), e lì restano caption e
\\label scritti a mano. Non si usa \\input: \\lstinputlisting è verbatim e non
espanderebbe la macro.

Il contratto (leggere prima di fidarsi)
---------------------------------------
La NIDIFICAZIONE del YAML non è dichiarata in nessun posto leggibile a macchina
nel PGE: PITCH_PARAMETER_SCHEMA è vuoto (il pitch è unit-driven), il blocco
`voices` non compare in ALL_SCHEMAS, le chiavi di StreamConfig sono una lista a
mano anche nello SchemaBridge di PGE-ls. Quindi:

  - lo SCHELETRO (quali blocchi esistono e cosa sta dentro cosa) è scritto qui;
  - i DOMINI (enum, bounds, default, chiavi _range e deviation_probability)
    sono derivati dal codice a ogni run;
  - la GUARDIA fallisce se il codice espone una chiave che lo scheletro non
    piazza.

Un bump del submodule aggiorna i domini da solo. Se introduce una chiave nuova,
`make grammar-tree` esce con codice 1 e la elenca: il piazzamento è l'unico
passo manuale, ed è un errore di build, non un'omissione silenziosa.

Sorgente PGE
------------
env PGE_SRC -> submodule raw/PythonGranularEngine (pinnato, path primario) ->
sibling ../PythonGranularEngine. Per il paper conta il submodule: è il codice
che la realizzazione spedita cita.

Uso:
    python gen_grammar_tree.py                  # stile yaml (default)
    python gen_grammar_tree.py --style tree     # stile albero indentato
    python gen_grammar_tree.py --scope paper    # solo i blocchi usati negli esempi
    python gen_grammar_tree.py --stdout         # anteprima, non scrive
"""
from __future__ import annotations

import argparse
import inspect
import re
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(HERE, "grammar_tree.tex")


def _resolve_pge_src() -> str:
    """src/ del PGE: env override -> submodule pinnato -> sibling working repo."""
    candidates = []
    env = os.environ.get("PGE_SRC", "").strip()
    if env:
        candidates.append(env)
    candidates.append(os.path.join(REPO, "raw", "PythonGranularEngine", "src"))
    candidates.append(os.path.join(os.path.dirname(REPO), "PythonGranularEngine", "src"))
    for path in candidates:
        if os.path.isfile(os.path.join(path, "pge", "parameters", "parameter_schema.py")):
            return path
    raise SystemExit(
        "gen_grammar_tree: src/ del PGE non trovato. Inizializza il submodule "
        "(git submodule update --init raw/PythonGranularEngine) oppure imposta "
        "PGE_SRC.\nCercato in:\n  " + "\n  ".join(candidates)
    )


# =============================================================================
# LETTURA DEL CODICE PINNATO
# =============================================================================

class Pge:
    """Facciata sui registri del PGE pinnato. Tutto ciò che è derivato passa di qui."""

    def __init__(self, src: str):
        sys.path.insert(0, src)
        from pge.parameters.parameter_schema import ALL_SCHEMAS
        from pge.parameters.parameter_definitions import GRANULAR_PARAMETERS
        from pge.parameters.pitch_unit import PITCH_UNIT_PRESETS
        from pge.controllers.window_registry import WindowRegistry
        from pge.shared.distribution_strategy import DistributionFactory, RANGE_ANCHORS
        from pge.strategies.voice_pitch_strategy import VOICE_PITCH_STRATEGIES, CHORD_INTERVALS
        from pge.strategies.voice_onset_strategy import VOICE_ONSET_STRATEGIES
        from pge.strategies.voice_pan_strategy import VOICE_PAN_STRATEGIES
        from pge.strategies.voice_pointer_strategy import VOICE_POINTER_STRATEGIES
        from pge.strategies.grain_clip_strategy import GRAIN_CLIP_STRATEGIES
        from pge.parameters.parameter_orchestrator import ParameterOrchestrator

        # Il pitch e' unit-driven: non ha ParameterSpec, quindi la sua chiave di
        # gate non sta in ALL_SCHEMAS e va presa dove e' davvero dichiarata,
        # cioe' dal default della firma che PitchController passa a GateFactory.
        # Derivarla invece di scriverla a mano non e' pedanteria: la prima
        # stesura la ometteva, e l'albero stampava una "specifica completa" con
        # una chiave del gate mancante.
        self.pitch_gate_key = inspect.signature(
            ParameterOrchestrator.create_pitch_parameter
        ).parameters["deviation_probability_key"].default

        # Unita' di trasposizione: nel blocco `pitch` l'unita' NON e' il valore di
        # una chiave `unit`, e' la chiave stessa (`semitones: 0`, `cents: 50`).
        # `unit:` esiste solo dentro voices.pitch.
        self.pitch_unit_bounds = {
            name: factory().value_bounds()
            for name, factory in PITCH_UNIT_PRESETS.items()
        }

        self.schemas = ALL_SCHEMAS
        self.bounds = GRANULAR_PARAMETERS
        self.pitch_units = sorted(PITCH_UNIT_PRESETS)
        self.windows = sorted(WindowRegistry.all_names())
        self.dist_modes = sorted(DistributionFactory._registry)
        self.range_anchors = list(RANGE_ANCHORS)
        self.clip_strategies = ["strict"] + sorted(GRAIN_CLIP_STRATEGIES)
        self.voice_strategies = {
            "pitch": sorted(VOICE_PITCH_STRATEGIES),
            "onset_offset": sorted(VOICE_ONSET_STRATEGIES),
            "pointer": sorted(VOICE_POINTER_STRATEGIES),
            "pan": sorted(VOICE_PAN_STRATEGIES),
        }
        self.chords = sorted(CHORD_INTERVALS)
        self._voice_registries = {
            "pitch": VOICE_PITCH_STRATEGIES,
            "onset_offset": VOICE_ONSET_STRATEGIES,
            "pointer": VOICE_POINTER_STRATEGIES,
            "pan": VOICE_PAN_STRATEGIES,
        }

    # --- domini derivati -----------------------------------------------------

    def span(self, name: str) -> str:
        """Intervallo ammesso di un parametro, come '-120..12'. '' se non ha bounds."""
        b = self.bounds.get(name)
        if b is None or b.max_val is None:
            return ""
        return f"{_num(b.min_val)}..{_num(b.max_val)}"

    def range_span(self, name: str) -> str:
        b = self.bounds.get(name)
        if b is None or not b.max_range:
            return ""
        return f"{_num(b.min_range)}..{_num(b.max_range)}"

    def default(self, name: str):
        for schema in self.schemas.values():
            for spec in schema:
                if spec.name == name:
                    return spec.default
        return None

    def strategy_kwargs(self, block: str, strategy: str) -> list[str]:
        """Sotto-chiavi di una strategy, dalla firma del suo costruttore."""
        cls = self._voice_registries[block][strategy]
        params = inspect.signature(cls.__init__).parameters
        skip = {"self", "stream_id", "rng", "kwargs", "args"}
        return [p for p in params if p not in skip]

    # --- guardia -------------------------------------------------------------

    def declared_keys(self) -> set[str]:
        """
        Ogni chiave YAML che il codice espone via ALL_SCHEMAS, come path completo.
        I path interni (prefisso '_') non sono chiavi utente e si saltano, ma le
        loro range_path / deviation_probability_key sì: `pointer_deviation` ha
        base finta e range reale (`offset_range` + `deviation_probability.pointer`).
        """
        keys: set[str] = set()
        for block, schema in self.schemas.items():
            prefix = "" if block == "stream" else f"{block}."
            for spec in schema:
                leaf = spec.yaml_path.split(".")[-1]
                if not leaf.startswith("_"):
                    keys.add(prefix + spec.yaml_path)
                if spec.range_path and not spec.range_path.startswith("_"):
                    keys.add(prefix + spec.range_path)
                if spec.deviation_probability_key:
                    keys.add("deviation_probability." + spec.deviation_probability_key)
        return keys


def enum(names: list[str], keep: int = 2) -> str:
    """
    Enum come dominio. Se la lista è lunga la elide: la colonna del CIM regge
    ~48 caratteri a 8 pt, e i 17 nomi di finestra da soli fanno 200. Il numero
    totale resta stampato, così il lettore sa che l'elenco è troncato e non
    parziale per errore.
    """
    if len(names) <= keep + 1:
        return " | ".join(names)
    return " | ".join(names[:keep]) + f" | ...({len(names)})"


def _num(x) -> str:
    """Numero compatto: interi senza .0, float senza zeri di coda."""
    if x is None:
        return ""
    f = float(x)
    if f == int(f):
        return str(int(f))
    return f"{f:.6f}".rstrip("0").rstrip(".")


# =============================================================================
# SCHELETRO
# =============================================================================
# Nodo = (chiave, dominio, figli). `dominio` è una stringa già risolta oppure
# una lambda(Pge) -> str. `figli` è una lista di nodi, o None per una foglia.
#
# `scope`: i nodi marcati 'full' escono solo con --scope full. Servono a far
# stare l'albero in colonna quando lo spazio non basta (ramo di ripiego di D4:
# albero dei soli blocchi usati dagli esempi + rinvio al repo).

def skeleton(p: "Pge") -> list:
    """
    Domini asciutti di proposito. «scalare o inviluppo a breakpoint» vale per
    ogni parametro: ripeterlo su venti righe brucia la colonna senza dire nulla,
    quindi sta in didascalia una volta sola e qui resta il solo intervallo, che
    è ciò che cambia da parametro a parametro.
    """

    def par(key, bounds_name, note="", scope="paper"):
        """Foglia parametro: dominio = intervallo dal codice (+ nota di dominio)."""
        dom = p.span(bounds_name)
        if note:
            dom = f"{dom}  {note}" if dom else note
        return (key, dom, None, scope)

    def rng(key, bounds_name, scope="paper"):
        return (key, p.range_span(bounds_name), None, scope)

    # Le chiavi del gate: una per parametro deviabile. Dagli schemi, piu' il
    # pitch, che e' unit-driven e non ne ha uno.
    dev_keys = sorted({
        spec.deviation_probability_key
        for schema in p.schemas.values() for spec in schema
        if spec.deviation_probability_key
    } | {p.pitch_gate_key})

    # Il documento, non lo stream: un YAML e' `seed` piu' una lista di stream,
    # e senza il contenitore l'albero non direbbe la cosa piu' visibile degli
    # esempi del paper, cioe' che piu' stream convivono in un file solo.
    stream_body = [
        ("stream_id", "nome univoco", None, "paper"),
        ("sample", "path del file audio", None, "paper"),
        ("onset", "s", None, "paper"),
        ("duration", "s  (default: durata del sample)", None, "paper"),
        par("volume", "volume", note="dB"),
        rng("volume_range", "volume"),
        par("pan", "pan", note="gradi"),
        rng("pan_range", "pan"),
        ("grain", None, [
            par("duration", "grain_duration", note="s"),
            rng("duration_range", "grain_duration"),
            ("duration_unit", "seconds | samples | milliseconds", None, "full"),
            ("envelope", enum(p.windows), None, "paper"),
            ("reverse", "presente = sempre indietro", None, "paper"),
            ("read_direction", "-1 indietro | +1 avanti", None, "paper"),
        ], "paper"),
        ("pointer", None, [
            par("start", "pointer_start", note="0..1 del buffer"),
            par("speed_ratio", "pointer_speed_ratio"),
            rng("offset_range", "pointer_deviation"),
            par("loop_start", "loop_start", scope="full"),
            par("loop_end", "loop_end", scope="full"),
            par("loop_dur", "loop_dur", scope="full"),
            ("loop_unit", "normalized (default: da time_mode)", None, "full"),
        ], "paper"),
        ("pitch", "una sola chiave-unita per blocco:", [
            (unit, f"{_num(b.min_val)}..{_num(b.max_val)}", None, "paper")
            for unit, b in p.pitch_unit_bounds.items()
        ] + [
            ("edo", "N divisioni/ottava, con value:", None, "paper"),
            ("value", "grado della griglia EDO", None, "paper"),
            ("range", "nella unita attiva", None, "paper"),
        ], "paper"),
        ("density", None, [
            par("density", "density", note="grani/s"),
            par("fill_factor", "fill_factor", note="in alternativa"),
            par("distribution", "distribution", note="0 sincrono, 1 asincrono"),
        ], "paper"),
        ("deviation_probability", "0..100, o per chiave:", [
            (k, "0..100", None, "paper") for k in dev_keys
        ], "paper"),
        ("voices", None, [
            par("num_voices", "num_voices"),
            par("scatter", "scatter"),
        ] + [
            # Sotto ogni blocco di voce: la strategy, e le sue sotto-chiavi.
            # Quali valgano dipende dalla strategy scelta, e un albero piatto lo
            # travisa: stanno su una riga di commento, non come chiavi finte.
            (block, None, [
                ("strategy", enum(names), None, "paper"),
            ] + ({
                "pitch": [("unit", "semitones | {edo: N}", None, "full")],
                "pointer": [("normalized", "true = frazione di buffer", None, "full")],
            }.get(block, [])) + [
                ("# secondo strategy:", enum(sorted({
                    k for n in names for k in p.strategy_kwargs(block, n)
                    if k != "seed"
                }), keep=3), None, "paper"),
            ], "paper")
            for block, names in p.voice_strategies.items()
        ], "paper"),
        ("distribution_mode", enum(p.dist_modes), None, "full"),
        ("range_anchor", enum(p.range_anchors), None, "full"),
        ("range_always_active", "true | false", None, "full"),
        ("clip_strategy", enum(p.clip_strategies), None, "full"),
        ("clip_margin", "s di tolleranza oltre lo stream", None, "full"),
        ("time_mode", "absolute | normalized", None, "full"),
        ("time_scale", "fattore di scala dei tempi", None, "full"),
        ("rng_group", "condivide la sequenza fra stream", None, "full"),
        ("solo", "rende solo questo stream", None, "full"),
        ("mute", "esclude questo stream", None, "full"),
    ]

    return [
        ("seed", "intero, per un render riproducibile", None, "paper"),
        ("streams", None, stream_body, "paper"),
    ]


# =============================================================================
# GUARDIA DI DRIFT
# =============================================================================

def placed_keys(nodes: list, prefix: str = "") -> set[str]:
    out: set[str] = set()
    for key, _dom, children, _scope in nodes:
        path = prefix + key
        out.add(path)
        if children:
            out |= placed_keys(children, path + ".")
    return out


def check_highlighting(body: list[str]) -> None:
    """
    Ogni chiave stampata dev'essere fra le keywords della lingua yaml in
    cim2026.sty, altrimenti esce in tondo mentre le sue sorelle sono in
    grassetto — e il listato che dovrebbe mostrare la ramificazione la
    nasconde. `listings` non ha look-ahead: le chiavi sono un elenco a mano,
    quindi l'unico modo di tenerlo allineato è verificarlo.
    """
    # Apostrofi e virgolette: in cim2026.sty la lingua yaml dichiara
    # `morestring=[b]'`, quindi un apostrofo apre una stringa. In un dominio
    # scritto in italiano non si chiude mai, e da lì in giù TUTTO il listato
    # finisce dentro la stringa e perde il grassetto — senza un solo errore di
    # compilazione. È già successo con «nell'unita attiva»: le chiavi da
    # `density` in poi uscivano in tondo e sembrava un problema di keywords.
    for line in body:
        if "'" in line or '"' in line:
            raise SystemExit(
                "gen_grammar_tree: apostrofo o virgolette in un dominio — "
                "aprono una stringa che non si chiude e spengono "
                "l'evidenziazione di tutto il resto del listato:\n  " + line
            )

    sty_path = os.path.join(os.path.dirname(HERE), "cim2026.sty")
    sty = open(sty_path, encoding="utf-8").read()
    block = re.search(r"keywords=\{(.*?)\n  \},", sty, re.S)
    if not block:
        raise SystemExit(f"gen_grammar_tree: keywords non trovate in {sty_path}")
    # Via i commenti LaTeX, poi la lista separata da virgole.
    raw = re.sub(r"%.*", "", block.group(1))
    declared = {k.strip() for k in raw.replace("\n", " ").split(",") if k.strip()}

    printed = set()
    for line in body:
        if line.lstrip().startswith("#"):
            continue
        m = re.match(r"\s*-?\s*([a-z_][a-z0-9_]*):", line)
        if m:
            printed.add(m.group(1))

    missing = sorted(printed - declared)
    if missing:
        raise SystemExit(
            "gen_grammar_tree: chiavi stampate nell'albero ma non dichiarate fra "
            "le keywords yaml di cim2026.sty (uscirebbero senza grassetto):\n  "
            + "\n  ".join(missing)
        )


def check_drift(p: "Pge", nodes: list) -> None:
    declared = p.declared_keys()
    placed = placed_keys(nodes)
    # Lo scheletro nomina le chiavi locali dentro il loro blocco; il codice usa
    # path relativi al controller. Confrontiamo su entrambe le forme.
    placed_leaves = {k.split(".")[-1] for k in placed}
    orphans = sorted(
        k for k in declared
        if k not in placed and k.split(".")[-1] not in placed_leaves
    )
    if orphans:
        raise SystemExit(
            "gen_grammar_tree: il PGE pinnato espone chiavi che lo scheletro non "
            "piazza. Aggiungile in skeleton() scegliendo blocco e dominio:\n  "
            + "\n  ".join(orphans)
        )


# =============================================================================
# RENDERER
# =============================================================================

def render_yaml(nodes: list, indent: int = 0) -> list[str]:
    """Stile notazione: chiave: <dominio>, nidificazione a due spazi."""
    lines = []
    pad = "  " * indent
    for key, dom, children, _scope in nodes:
        if children:
            head = f"{pad}{key}:"
            if dom:
                head += f"  # {dom}"
            lines.append(head)
            body = render_yaml(children, indent + 1)
            if key == "streams":
                # `streams` è una lista: il trattino sul primo figlio, e tutti
                # gli altri rientrati sotto di lui. Senza questo l'albero
                # direbbe che uno YAML contiene UNO stream, mentre gli esempi
                # del paper ne affiancano due nello stesso file.
                body = [("  - " + body[0].lstrip())] + ["  " + b for b in body[1:]]
            lines += body
        elif key.startswith("#"):
            # Riga di commento: non è una chiave, e non deve sembrarlo.
            lines.append(f"{pad}{key} {dom}")
        else:
            # Dominio vuoto = il codice non dichiara bounds: si stampa la sola
            # chiave, mai un `<>` che sembrerebbe un dominio vuoto anziché assente.
            lines.append(f"{pad}{key}: <{dom}>" if dom else f"{pad}{key}:")
    return lines


def render_tree(nodes: list, prefix: str = "") -> list[str]:
    """Stile albero indentato, connettori ASCII."""
    lines = []
    last = len(nodes) - 1
    for i, (key, dom, children, _scope) in enumerate(nodes):
        conn = "`-- " if i == last else "|-- "
        line = f"{prefix}{conn}{key}"
        if dom and not children:
            line += f"  : {dom}"
        elif dom:
            line += f"  : {dom}"
        lines.append(line)
        if children:
            lines += render_tree(children, prefix + ("    " if i == last else "|   "))
    return lines


def prune(nodes: list, scope: str) -> list:
    if scope == "full":
        return nodes
    out = []
    for key, dom, children, node_scope in nodes:
        if node_scope != "paper":
            continue
        out.append((key, dom, prune(children, scope) if children else None, node_scope))
    return out


# =============================================================================

def build(style: str, scope: str) -> str:
    p = Pge(_resolve_pge_src())
    nodes = skeleton(p)
    check_drift(p, nodes)          # sempre sull'albero completo, mai sul potato
    body = (render_yaml if style == "yaml" else render_tree)(prune(nodes, scope))
    if style == "yaml":
        check_highlighting(body)
    # Intestazione come commento YAML, non LaTeX: il file si consuma con
    # \lstinputlisting (verbatim, non espande \input), e la sezione la salta
    # con firstline=4. Se qualcuno dimentica firstline, queste righe escono
    # come commenti YAML innocui invece che come simboli LaTeX crudi.
    header = [
        "# Generato da paper/figures/gen_grammar_tree.py - non editare a mano.",
        "# Domini ed enum derivati dal PGE pinnato (submodule).",
        f"# Rigenera con: make grammar-tree   (stile: {style}, scope: {scope})",
    ]
    return "\n".join(header + body) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", choices=("yaml", "tree"), default="yaml")
    ap.add_argument("--scope", choices=("paper", "full"), default="full")
    ap.add_argument("--stdout", action="store_true", help="stampa senza scrivere")
    a = ap.parse_args()

    text = build(a.style, a.scope)
    if a.stdout:
        print(text, end="")
        return
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    n = len(text.splitlines()) - 3
    print(f"gen_grammar_tree: scritto {os.path.relpath(OUT, REPO)} ({n} righe di albero)")


if __name__ == "__main__":
    main()
