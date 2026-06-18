#!/usr/bin/env python3
"""Rigenera il blocco meccanico di wiki/concepts/mappa-citazioni-paper.md
dai \\cite{} reali di paper/paper.tex e dei file \\input in paper/sections/.

Il blocco generato vive fra i marker:
    <!-- BEGIN cite-map -->
    <!-- END cite-map -->
e viene sostituito in blocco: tutto il resto della pagina (parte editoriale:
funzioni, stati, shortlist) non viene toccato. Vedi `make cite-map`.
"""

import hashlib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEX = REPO / "paper" / "paper.tex"
MAP = REPO / "wiki" / "concepts" / "mappa-citazioni-paper.md"

BEGIN = "<!-- BEGIN cite-map -->"
END = "<!-- END cite-map -->"


def expand_inputs(path, seen=None):
    """Espande ricorsivamente \\input{}/\\include{} a partire da `path`.

    I percorsi sono risolti rispetto alla cartella di paper.tex (come fa
    latexmk, che gira con cwd = paper/). Si assume un \\input per riga, com'e'
    nei file del paper; gli \\input commentati sono ignorati, come fa TeX.
    Un set di file gia' visti evita i cicli. Il sorgente cosi' ricomposto e'
    in ordine di documento: la stessa logica a blocchi di main() ci gira sopra.
    """
    if seen is None:
        seen = set()
    path = path.resolve()
    if path in seen:
        return ""
    seen.add(path)
    base = TEX.parent
    out = []
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        code = line.split("%", 1)[0]  # parte non commentata (basta per i nostri file)
        m = re.search(r"\\(?:input|include)\{([^}]+)\}", code)
        if m:
            inc = base / m.group(1)
            if not inc.suffix:
                inc = inc.with_suffix(".tex")
            if inc.exists():
                out.append(expand_inputs(inc, seen))
                continue
        out.append(line)
    return "".join(out)


def main() -> int:
    src = expand_inputs(TEX)
    digest = hashlib.sha256(src.encode("utf-8")).hexdigest()[:12]

    # blocchi: dall'inizio del file, ogni \section o \subsection con
    # \label{sec:...} apre un blocco col proprio label (le \subsection
    # etichettate producono quindi righe a grana fine: sec:c-e,
    # sec:griglia, ...). Una \subsection SENZA label non cambia blocco.
    section_re = re.compile(
        r"\\(section|subsection)\*?\{([^}]*)\}(?:\s*\\label\{([^}]*)\})?"
    )
    # cattura anche la forma con argomento opzionale: \cite[p.~37]{Chiave}
    cite_re = re.compile(r"\\cite(?:\[[^\]]*\])?\{([^}]*)\}")

    # posizione -> label corrente
    events = []  # (pos, kind, label, title)
    for m in section_re.finditer(src):
        kind, title, label = m.group(1), m.group(2), m.group(3)
        events.append((m.start(), kind, label or "(senza label)", title))

    blocks: dict[str, list[str]] = {"(preambolo/intro)": []}
    order = ["(preambolo/intro)"]
    current = "(preambolo/intro)"

    def block_for(pos: int) -> str:
        nonlocal current
        return current

    # costruzione sequenziale: scorri cite ed eventi insieme
    ev_idx = 0
    for cm in cite_re.finditer(src):
        while ev_idx < len(events) and events[ev_idx][0] < cm.start():
            pos, kind, label, title = events[ev_idx]
            if kind == "section":
                current = f"`{label}`" if label.startswith("sec:") else title
            elif kind == "subsection" and label.startswith("sec:"):
                current = f"`{label}`"
            else:
                ev_idx += 1
                continue
            if current not in blocks:
                blocks[current] = []
                order.append(current)
            ev_idx += 1
        for key in cm.group(1).split(","):
            key = key.strip()
            if key and key not in blocks[current]:
                blocks[current].append(key)

    all_keys = sorted({k for keys in blocks.values() for k in keys})

    lines = [BEGIN, ""]
    lines.append(
        f"Generato da `make cite-map` su `paper/paper.tex` (con gli \\input di "
        f"`sections/` espansi; sha256 del sorgente espanso: `{digest}`). "
        f"Non editare a mano questo blocco."
    )
    lines.append("")
    lines.append(f"**Chiavi citate ({len(all_keys)}):** " + ", ".join(f"`{k}`" for k in all_keys))
    lines.append("")
    lines.append("| Blocco del paper | Chiavi citate (in ordine di apparizione) |")
    lines.append("|---|---|")
    for name in order:
        if blocks[name]:
            lines.append(f"| {name} | " + ", ".join(f"`{k}`" for k in blocks[name]) + " |")
    lines.append("")
    lines.append(END)
    generated = "\n".join(lines)

    page = MAP.read_text(encoding="utf-8")
    if BEGIN not in page or END not in page:
        sys.stderr.write(f"marker {BEGIN} / {END} mancanti in {MAP}\n")
        return 1
    pre, rest = page.split(BEGIN, 1)
    _, post = rest.split(END, 1)
    MAP.write_text(pre + generated + post, encoding="utf-8")
    print(f"cite-map: {len(all_keys)} chiavi, hash {digest} -> {MAP.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
