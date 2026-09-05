# Notes for Claude

One-page Letter-size print flier for the Cal State Fullerton Master of Public
Administration program, a print-palette twin, an accessible web page, and the
sources for a Claude Design canvas. Owner: David Adams (PAJ Division, CSUF).

## Facts that override older files or commits

- Fall application deadline is **May 1**; spring is **November 15**. Commit
  278162c had changed fall to "early May"; the owner corrected it back on
  2026-09-04. Do not "fix" it to match old text.
- Headline is **"The management degree for public service."** The old line
  "Move from doing the work to running it." was retired as cheesy.
- Two courses a term is typical, not the rule (some take 1, 3, or 4). Write
  "most students take two courses a term"; never state it as a requirement.
- 36 units = 21 core + 15 of **concentration and electives** (Human Resources,
  Public Finance, Local Government, Public Policy).
- Tuition ($2,480/term) always carries its conditions: 2026–27, California
  resident, 6 units, plus campus fees.
- The alumni employer list always ends with "and many more".
- Never invent facts. Anything not in flier.html or from the owner gets a
  bracketed placeholder.

## Files

- `flier.html` and `flier-print.html` differ only in the `:root` palette
  (screen vs. printer-friendly). Change copy in both.
- The hero card is 440px wide so the two-line headline fits. At 396px the
  headline wraps to three lines and the kicker is clipped off the top.
- `csuf-mpa-program.html` is the accessible web version. Its overview H2 is
  "The program at a glance", deliberately not the headline, so the page does
  not repeat itself. Keep its "Updated <month year>" footer in step with the
  fliers.

## Rebuilding the PDFs

```
chromium --headless=new --disable-gpu --no-sandbox --virtual-time-budget=10000 \
  --no-pdf-header-footer --print-to-pdf="$PWD/MPA-Flier.pdf" "file://$PWD/flier.html"
```

Same for `flier-print.html` -> `MPA-Flier-print.pdf`. Expect exactly one
Letter page (`pdfinfo`). Always look at the result:
`pdftoppm -png -r 72 -singlefile MPA-Flier.pdf out` and read `out.png`.

## Design canvas

- Live canvas: https://claude.ai/code/artifact/822067ff-2d5b-4e30-b61d-bffe0753d35c
  (Claude Design preview inside Claude Code, title "CSUF MPA Flier").
- Sources in `design/`: `Main.dc.html` is the current flier as an editable
  artboard with a Screen/Print palette tweak; `Poster.dc.html` (Direction A),
  `Editorial.dc.html` (Direction B), `Pathway.dc.html` (Direction C) are
  redesign directions; plus `canvas.json`, `hero.jpg` (816px wide, ~80 KB),
  `csuf_logo.png`, `qr.png`.
- Direction names A/Poster, B/Editorial, C/Pathway are fixed. Never renumber
  or rename them. No direction had been chosen as of 2026-09-04; when one is,
  build it into `Main.dc.html` and move the others to a second page.
- To update: edit the files in `design/`, re-seed with `/design`, republish
  to the URL above (contract pin 0.1.31, no capabilities on republish). If
  the owner has edited the canvas in the browser since, extract from the live
  artifact first instead of re-seeding from `design/`.
- Direction artboards keep body text at 16px or larger and labels at 12px or
  larger (12pt and 9pt at 96px per inch). Main mirrors the original flier's
  smaller sizes on purpose.
- Looking at a seeded canvas locally: headless `chromium --screenshot` never
  gets past "Loading artboard…". Use Python Playwright with
  `executable_path='/usr/bin/chromium'`, `goto`, sleep about 12 s, then
  `screenshot`. To see one artboard at 1:1, seed a throwaway copy whose
  `canvas.json` has `"launch": {"view": "focused", "file": "<Name>.dc.html"}`
  and use an 1100x1300 viewport. Seed output filenames must be lowercase.
