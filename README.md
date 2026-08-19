# MPA Flier

This repository contains a one-page print flier for the CSUF Master of Public Administration program.

## What this is

The project is a simple HTML flier that is designed to be printed as a clean, single-page PDF. It includes:

- a header with the CSUF logo and program identity
- a large hero image and headline
- program details, career paths, coursework, and contact information
- a QR code that links to the MPA website

## Files

- flier.html — the main flier source in HTML/CSS
- flier-print.html — a print-optimized variant with a lighter color palette for printing
- csuf-mpa-program.html — a responsive, accessible web version of the MPA program information
- assets/csuf-mpa-hero.jpg — web-optimized campus image used by the web page and both fliers
- assets/qr-mpa-fullerton.png — generated QR code image for the program website
- 1C7A4634.jpg — original high-resolution campus photo source
- csuf_logo.png — CSUF logo used in the flier
- MPA-Flier.pdf — generated printable PDF from flier.html
- MPA-Flier-print.pdf — generated printable PDF from flier-print.html

## Why it is not fully accessible

The flier is visually polished and print-friendly, but it is not fully accessible in the strict web accessibility sense. The main reasons are:

- the layout is highly visual and designed for print, not for screen-reader-first navigation
- the content relies heavily on visual hierarchy, spacing, and color styling
- the PDF export is not a fully accessibility-compliant PDF/A or tagged PDF workflow
- the flier uses decorative graphics and a QR image that are fine for print but do not provide a rich accessible experience for assistive technology

## How to use it

Open flier.html in a browser and print it to PDF, or use the existing generated PDFs directly. For an accessible, shareable web page, publish csuf-mpa-program.html and assets/csuf-mpa-hero.jpg together, then link to its hosted URL.

If you want to make it more accessible in the future, the next steps would be:

- simplify the layout and improve semantic structure for screen readers
- add proper document tags and accessible PDF metadata
- ensure all text remains legible and not dependent on color alone
- provide an accessible alternative format such as a text-only version or a web page with better navigation
