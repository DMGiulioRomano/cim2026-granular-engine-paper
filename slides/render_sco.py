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
    sco_video(os.path.join(MEDIA, f"{name}_csound.sco"),
              os.path.join(MEDIA, f"{name}_sco.mp4"))


def sco_video(sco, mp4, n=300, w=800, h=420, line_h=16, px_s=40):
    """Video muto delle prime n righe-evento che scorrono, per la slide 2.

    Un mp4 costa al browser meno di un <pre> di migliaia di righe animato.
    """
    import subprocess
    from PIL import Image, ImageDraw, ImageFont

    with open(sco) as f:
        lines = [l.rstrip() for l in f if l.startswith('i "Grain"')][:n]
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 13)
    except OSError:  # ponytail: Menlo solo su macOS, altrove il font di default
        font = ImageFont.load_default(size=13)
    img = Image.new("RGB", (w, len(lines) * line_h + h), "#111")
    draw = ImageDraw.Draw(img)
    for i, line in enumerate(lines):
        draw.text((8, i * line_h), line, fill="#9f9", font=font)
    png = mp4[:-4] + ".png"
    img.save(png)
    dur = len(lines) * line_h / px_s
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-loop", "1", "-framerate", "30",
                    "-i", png, "-vf", f"crop={w}:{h}:0:'t*{px_s}'", "-t", str(dur),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "28", mp4], check=True)
    os.remove(png)
    print(f"Video: {mp4}")


if __name__ == "__main__":
    main()
