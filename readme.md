# pyPDFex (this readme is a WIP)

pyPDFex is a script designed to extract highlights and comments from PDFs and insert them into prexisitng markdown documents. Currently the script is configured to work best with highlight annotations made in the [highlights app](https://highlightsapp.net/).

This script is intedended as part of the using obsidian for academic research workflow documented by [Chris Griesser](https://chris-grieser.de/Comprehensive-Academic-Workflow-from-Reading-to-Writing-in-Markdown).

## Major issues

==current method for recognising and inserting highlight extractions into markdown notes will not update the notes in the future if you add or remove highlights to the original pdf==
If you wish to update a note you need to manually delete the annotations notes and insert the PDFS notes tag (default : `^^PDF_NOTES^^`).

## recommended setup

- Obsidian (plugins:)
  - citations
- Pdf annoator (Highlights)
- Citation manager (Jabref)

## Workflow rules

Comments always have accompanied highlighted text.

## roadmap

- [ ] Non-highlight comments.
- [x] More forgiving colour recognition.
- [ ] Add setting option to add colors in yaml.