# Notes for Claude

One-page Letter-size print flier for the Cal State Fullerton Master of Public
Administration program, a press twin with bleed, an accessible web page, and
the sources for a Claude Design canvas. Owner: David Adams (PAJ Division, CSUF).

## Facts that override older files or commits

- Fall application deadline is **May 1**; spring is **November 15**. Commit
  278162c had changed fall to "early May"; the owner corrected it back on
  2026-09-04. Do not "fix" it to match old text.
- **2026-10-07: faculty picked Direction A · Poster, and it is now the flier.**
  Headline is the MPA program card's, **"Lead with integrity. / Serve Orange
  County and beyond."** (`~/Repos/csuf-program-cards`), two lines at 46px. The
  navy banner carries that card's palm photo (3T8A9224) under a navy gradient,
  darker at the top so the orange kicker keeps its contrast. Earlier headlines,
  both retired: "The management degree for public service." (9/04 to 10/07)
  and "Move from doing the work to running it." (cheesy).
- The Poster drops the coursework list and the alumni line by design.
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

- `flier.html` is the Letter page. `flier-print.html` is the press version for
  Digital Print Services: 0.125in bleed on every side (8.75 x 11.25 in, no crop
  marks, page edge = bleed edge, as with the program cards). The two differ
  only in `--bleed` and `@page`; regenerate the twin with
  `sed -e 's/^  --bleed:0px;/  --bleed:12px;/' -e 's/^@page{size:8.5in 11in;/@page{size:8.75in 11.25in;/' flier.html >| flier-print.html`
  rather than editing both. Until 2026-10-07 the twin was a printer-friendly
  palette instead.
- `assets/mpa-banner.jpg` is 2700px wide (~309 ppi in the press PDF), made from
  the card repo's `assets/photos/originals/3T8A9224.JPG`.
- `csuf-mpa-program.html` is the accessible web version. It still carries the
  9/04 headline, "The management degree for public service.", and its footer
  reads "Updated September 2026"; it was not changed when the Poster was
  adopted. Its overview H2 is "The program at a glance", deliberately not the
  headline.

## Rebuilding the PDFs

```
chromium --headless=new --disable-gpu --no-sandbox --virtual-time-budget=10000 \
  --no-pdf-header-footer --print-to-pdf="$PWD/MPA-Flier.pdf" "file://$PWD/flier.html"
```

Same for `flier-print.html` -> `MPA-Flier-print.pdf`. Expect exactly one page
each (`pdfinfo`): Letter (612 x 792 pts) and 630 x 810 pts. `pdffonts` must
show Atkinson Hyperlegible embedded. Always look at the result:
`pdftoppm -png -r 72 -singlefile MPA-Flier.pdf out` and read `out.png`.

## Design canvas

- Live canvas: https://claude.ai/code/artifact/822067ff-2d5b-4e30-b61d-bffe0753d35c
  (Claude Design preview inside Claude Code, title "CSUF MPA Flier").
- Sources in `design/`: `Main.dc.html` is the flier as it stood until
  2026-10-07, with its Screen/Print palette tweak; `Poster.dc.html` (Direction
  A, now the flier; same copy as `flier.html`),
  `Editorial.dc.html` (Direction B), `Pathway.dc.html` (Direction C) are
  redesign directions; plus `canvas.json`, `hero.jpg` (816px wide, ~80 KB),
  `banner.jpg` (Poster only), `csuf_logo.png`, `qr.png`.
- Direction names A/Poster, B/Editorial, C/Pathway are fixed. Never renumber
  or rename them. A was picked 2026-10-07 and built into `flier.html`;
  `canvas.json` relabels Main as the previous flier. The live canvas has not
  been republished since 2026-09-04.
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
