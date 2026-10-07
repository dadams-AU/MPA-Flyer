# share/

Standalone copies of the four `design/` artboards, built by `build.py` for
emailing or opening in any browser: images inlined, canvas runtime removed,
Screen palette filled in. `MPA-Flier-A-Poster.html` is Direction A, picked
2026-10-07 and now the flier (`flier.html`, `MPA-Flier.pdf`).
`MPA-Flier-Previous.html` is the flier as it stood until then; B and C are the
directions not taken. Regenerate after any change to `design/` with
`python3 share/build.py`. Body type still loads Atkinson Hyperlegible from
Google Fonts and falls back to the system face offline.
