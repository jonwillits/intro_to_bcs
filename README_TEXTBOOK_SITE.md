# The Interactive Textbook Site (Quarto)

This turns the module **readings** in this repo into a navigable website, where
each reading is a web page **and** a downloadable PDF generated from the *same*
markdown source. It deploys automatically to GitHub Pages. The interactive
**labs** stay in the companion app (`bcogapp`); the site links out to them.

Nothing here touches your existing content workflow: readings stay as plain
`.md` files in their module folders (so the app can still fetch them live), and
labs/slides/READMEs are left alone.

## The files

| File | What it is |
|---|---|
| `_quarto.yml` | Site config: title, sidebar/navbar, which files to render, and the HTML+PDF output settings. |
| `styles.css` | **The one file to edit to restyle everything.** Colors, fonts, and reading-column width live in the `:root` block at the top. |
| `index.qmd` | The landing page. |
| `.github/workflows/publish.yml` | Builds and deploys the site to GitHub Pages on every push to `main`. |

## Preview it on your Mac

Install Quarto once (`brew install quarto`, or the installer from quarto.org),
then from the repo root:

```bash
quarto preview
```

This opens the site in your browser and live-reloads as you edit a reading or
`styles.css`. To build the static site into `_site/` without serving it, run
`quarto render`.

> Add `_site/` and `.quarto/` to `.gitignore` — they're build output, not source.

## Turn on GitHub Pages (one time)

In the repo on GitHub: **Settings → Pages → Build and deployment → Source →
"GitHub Actions."** After that, every push to `main` rebuilds and publishes the
site. The PDFs are built in CI too (the workflow installs TinyTeX for that), so
you never generate them by hand.

The site will live at `https://jonwillits.github.io/intro_to_bcs/`.

## Add a new module (3 steps)

1. Finish its reading at `<module_folder>/<name>_reading.md` (same as Module 0).
2. In `_quarto.yml`, add that path under `project: → render:`.
3. In `_quarto.yml`, add a sidebar entry under `website: → sidebar: → contents:`.

That's it — the PDF link and page appear automatically. There are commented-out
example lines for both steps already in `_quarto.yml`.

## Change the look

Open `styles.css` and edit the values in the `:root` block at the top — the hex
colors (currently Illinois blue + orange), the two font stacks, and
`--bcog-measure` (the reading-column width). Re-run `quarto preview` and the
whole site restyles. You rarely need to touch anything below the `RULES`
divider.

## How the per-reading PDF works

Each reading is rendered to both `html` and `pdf` (configured once in
`_quarto.yml`). Quarto automatically adds an "Other Formats → PDF" link in the
page margin — no per-page editing. The reading's title comes from its first `#`
heading, so your `.md` files need no special front matter.

## Slides (the working pattern)

Module 0's three decks are already converted and linked, as the template for
every module:

1. Convert each `.pptx` to PDF. **You don't need PowerPoint or any local tool
   for this** — just ask Claude to convert the deck (it runs the conversion in
   the cloud and drops the PDF into the module folder). Kept named
   `<module>_lecture<n>.pdf`, the `resources:` glob in `_quarto.yml`
   (`*/*_lecture*.pdf`) copies it into the site automatically, so you never list
   slide files individually.

   *(If you ever want to do it yourself, LibreOffice is free and converts from
   the command line: `soffice --headless --convert-to pdf deck.pptx`. Optional.)*
2. Link them as nested `contents:` under that module in the sidebar — copy the
   three lines under Module 0 in `_quarto.yml` and change the module name.

Later, authoring *new* decks directly in Quarto's `revealjs` format gives you
web slides + PDF + `.pptx` from one markdown source — the point you eventually
want to migrate to.

## Embedding a lab inside a chapter

Right now the site links out to the app. When you want a demo to sit *inside* a
reading, drop an `<iframe>` pointing at the relevant app route into the `.md`,
e.g.:

```html
<iframe src="https://jonwillits.github.io/bcogapp/#/m01-vehicles"
        width="100%" height="520" style="border:1px solid #e2e6ec;border-radius:8px"></iframe>
```

(The app already fetches lab handouts live, so the demo and its instructions
stay in sync.)
