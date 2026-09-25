#!/usr/bin/env python3
"""
render_sco.py — rende un esempio del paper col back-end Csound e ne conserva
lo .sco, per la slide sul problema della leggibilità (event list vs audio).

Stesso PGE pinnato e stesso YAML (seed compreso) di paper/examples/render_example.py:
cambia solo il back-end. Output in slides/media/:
    <name>.sco          la event list che Csound consuma, una riga per grano
    <name>_csound.aif   l'audio reso da Csound

Uso:
    python slides/render_sco.py paper/examples/complete_example/complete_example.yml
"""
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PGE = os.path.join(REPO, "raw", "PythonGranularEngine")
MEDIA = os.path.join(REPO, "slides", "media")
sys.path.insert(0, os.path.join(PGE, "src"))


def main():
    if len(sys.argv) < 2:
        sys.exit("Uso: python slides/render_sco.py <file.yml>")
    yaml_file = os.path.abspath(sys.argv[1])
    name = os.path.splitext(os.path.basename(yaml_file))[0]
    os.makedirs(MEDIA, exist_ok=True)

    from pge.engine.generator import Generator
    from pge.rendering.rendering_engine import RenderingEngine
    from pge.rendering.render_mode import MixRenderMode
    from main import _build_renderer

    # csound/main.orc e ./refs/ sono relativi alla radice del PGE.
    os.chdir(PGE)
    generator = Generator(yaml_file)
    generator.load_yaml()
    generator.create_elements()

    renderer = _build_renderer(
        "csound",
        generator,
        output_sr=48000,
        ssdir=os.path.join(PGE, "refs"),
        sfdir=MEDIA,
        log_dir=MEDIA,
        sco_dir=MEDIA,
        use_cache=False,
    )
    aif = os.path.join(MEDIA, f"{name}_csound.aif")
    out = RenderingEngine(renderer).render(
        streams=generator.streams, output_path=aif, mode=MixRenderMode())
    print(f"Audio: {out}")


if __name__ == "__main__":
    main()
