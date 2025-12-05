# Liam Berrisford — Profile Site

Static personal site showcasing projects, publications, teaching, and awards. Hosted on GitHub Pages at `https://liamjberrisford.github.io/me/`. Everything runs client-side with no build step.

## Quick start (local)
- Serve the folder so Markdown files can be fetched: `python3 -m http.server 8000`
- Open `http://localhost:8000` (hash-based routing picks the section from the URL).
- Opening `index.html` directly via `file://` works too, but falls back to the inline copies of the Markdown content.

## Content model
- Sections are configured in `app.js` (`sections` array) and load Markdown from `content/*.md`.
- Headings in the Markdown drive the sub-navigation; `#` becomes the page title and each `##` becomes a sub-section toggle.
- The simple Markdown renderer supports headings, lists, links, images, horizontal rules, and inline formatting.
- Images whose base filename matches a video in `_static/videos` are upgraded to autoplay videos with poster frames from `_static/images`.

## Structure
- `index.html` — shell HTML, navigation containers, and footer.
- `app.js` — hash-based navigation, Markdown loading/parsing, sub-nav logic, media enhancement, and PWA registration.
- `styles.css` — layout, typography, responsive rules, and content styling.
- `content/` — editable Markdown per section (`about.md`, `projects.md`, `publications.md`, `teaching.md`, `awards.md`).
- `_static/images` / `_static/videos` — media assets referenced by the content.
- `manifest.webmanifest` — PWA metadata (name, theme colors).
- `sw.js` — caches core assets for offline/low-connectivity use.

## Editing and extending
- Update the Markdown files to change copy; serve over HTTP to see live fetches instead of inline fallbacks.
- Add a new section by creating `content/<section>.md` and adding an entry to the `sections` array in `app.js`.
- When changing cached assets, bump `CACHE_NAME` in `sw.js` so clients pick up fresh content.
- Customise branding and metadata in `index.html` (title, description) and colors/spacing in `styles.css`.

## Deployment
- Live site: `https://liamjberrisford.github.io/me/` (served via GitHub Pages).
- For other static hosts, deploy the repository as-is. The service worker caches the routes listed in `CORE_ASSETS` for offline support.
