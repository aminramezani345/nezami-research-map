# Nezami Lab Research Map

An interactive, linkable sunburst map of the Nezami Lab's research. It has four layers:

- **Center**: the lab's vision
- **Ring 1**: research areas (5)
- **Ring 2**: subtopics and methods (21)
- **Ring 3**: grants, projects and publications (58), styled by status

Below the map is a section on the principal investigator, with roles, training, awards and profile links. Its content comes from `meta.pi` in the JSON.

## Files

```
index.html               built page: self-contained, opens offline (data inlined)
data/research-map.json   all content (edit this file)
src/template.html        page code and styles (no external libraries)
build.py                 inlines the JSON into index.html and checks the data
VERIFICATION.md          items and details that need the lab's confirmation
```

## Run it

- **Quickest:** open `index.html` in any browser.
- **Live data while editing:** run `python3 -m http.server 8000` in this folder and open <http://localhost:8000>. When served over HTTP, the page reads `data/research-map.json` directly, so you only need to refresh.

## Update the content

1. Edit `data/research-map.json`.
   - Add a project or paper: copy an item inside the right `subtopics[].items` list and give it a unique `id`.
   - `status` must be one of: `grant`, `journal` (published papers and preprints), `conference` (conference papers and abstracts), `hsrd`.
   - `linkType`: `pubmed`, `doi`, `preprint`, `profile`, `publisher`, `scholar` (a Google Scholar title search) or `none`.
   - `short` is the label used in tooltips and lists. Keep it under 25 characters.
   - Add a new area by giving it a `color`. Keep the colors muted and dark enough for white text.
2. Run `python3 build.py`. It checks for duplicate ids and unknown statuses, then writes `index.html`.

HSRD 2027 items must hold only general information (a general title, the presenter and the status) until the work is public. Do not copy abstract text, methods or results into them. Once the work is public, change `status` to `journal` or `conference`, and add the real title, the authors and the link.

## Interaction

- Click or tap any segment to open it. The panel shows details, and the map highlights that segment's branch.
- Keyboard: use **Tab** to reach a segment. **←/→** moves within a ring, **↑** moves outward, **↓** moves inward, **Enter** opens and **Esc** resets.
- Status chips filter the outer ring.
- Deep links: append `#<id>` to the URL, for example `#model` or `#hsrd-steiger`. The address updates as you click.

## Design notes

The page uses plain JavaScript and SVG instead of React. This keeps it to one file with no build tools or CDN dependency, and it is easier for the lab to maintain. It does not use any logos or images, and it does not imply BWH or Harvard endorsement.
