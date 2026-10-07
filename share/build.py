#!/usr/bin/env python3
"""Build standalone, attachable HTML copies of the design/ artboards.

The .dc.html files in design/ are canvas artboards: images by relative path,
a support.js runtime that is not in the repo, and (for Main) a Screen/Print
palette resolved at runtime. Emailed bare they open with no images. This
script inlines the four images as data URIs, drops the runtime, fills the
Screen palette, and writes one self-contained file per artboard into share/.
Run from the repo root:  python3 share/build.py
"""
import base64, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
src, out = root / "design", root / "share"

def datauri(name, mime):
    return f"data:{mime};base64," + base64.b64encode((src / name).read_bytes()).decode()

imgs = {
    "hero.jpg": datauri("hero.jpg", "image/jpeg"),
    "csuf_logo.png": datauri("csuf_logo.png", "image/png"),
    "qr.png": datauri("qr.png", "image/png"),
    "banner.jpg": datauri("banner.jpg", "image/jpeg"),
}
screen = {"bg": "#ebfbff", "surface": "#d9eaf1", "muted": "#eef2f4",
          "border": "#cfdde0", "accent": "#00244e"}  # Main.dc.html, palette=Screen
files = {
    "Main": ("MPA-Flier-Previous.html", "Previous flier, to 2026-10-07"),
    "Poster": ("MPA-Flier-A-Poster.html", "Direction A, Poster"),
    "Editorial": ("MPA-Flier-B-Editorial.html", "Direction B, Editorial"),
    "Pathway": ("MPA-Flier-C-Pathway.html", "Direction C, Pathway"),
}
for key, (name, title) in files.items():
    s = (src / f"{key}.dc.html").read_text(encoding="utf-8")
    for img, uri in imgs.items():
        s = s.replace(f'src="{img}"', f'src="{uri}"')
    s = re.sub(r'\s*<script src="\./support\.js"></script>', "", s)
    s = re.sub(r"<script data-dc-script.*?</script>\s*", "", s, flags=re.S)
    s = re.sub(r"\{\{c\.(\w+)\}\}", lambda m: screen[m.group(1)], s)
    s = s.replace("<x-dc>", '<div class="artboard" style="width:816px;height:1056px;'
                  'margin:0 auto;overflow:hidden;position:relative">').replace("</x-dc>", "</div>")
    s = s.replace("<helmet>", "").replace("</helmet>", "")
    s = s.replace('<meta charset="utf-8">',
                  f'<meta charset="utf-8">\n  <title>CSUF MPA Flier: {title}</title>', 1)
    assert "{{" not in s and "support.js" not in s and "data-dc-script" not in s
    (out / name).write_text(s, encoding="utf-8")
    print(f"{name}: {len(s):,} bytes")
