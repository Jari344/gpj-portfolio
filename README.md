# GPJ Codes · black + lime portfolio

Static site, no backend. Drop the folder on Vercel (or push it to the GitHub repo Vercel watches).
Preview locally: `python3 -m http.server 8000` then open http://localhost:8000

## Where things live
- `index.html`, `projects.html`, `about.html`, `contact.html`, `privacy.html`, `404.html` and `project/*.html` are GENERATED.
- `css/style.css` (all pages) and `css/pages.css` (inner pages) are hand-written.
- `js/site.js` shared UI (nav, search, menu, cursor, transitions) needs no libraries.
- `js/scenes.js` the Three.js scenes. `js/home.js` and `js/pages.js` page scripts.
- `tools/site_data.py` is the ONE place for content. `js/data.js`, the sitemap and every project page come from it.

## Change content
1. Edit `tools/site_data.py` (projects, journey, testimonials, press, links).
2. Run `python3 tools/build.py` from the site folder.
3. Commit and deploy.

## Add a real screenshot to a project
Put the image in `assets/` (create the folder), then set `img='assets/gpj-ai.jpg'` on that project and rebuild.
It appears on the card and on the project page. Use ~1280x800 JPG or WebP.

## Mark a project as live
Open the URL yourself first. Then set `s='live'`, `live='https://...'` and `v=1`.
The build stops with an error if a project says `live` without `v=1`.

## Testimonials and press
Add real entries to `TESTIMONIALS` / `PRESS`. The sections stay out of the page while the lists are empty.

## Libraries (loaded from CDNs, optional)
GSAP 3.12.5 + ScrollTrigger (cdnjs), Three.js r128 (cdnjs), Lenis 1.3.4 (jsDelivr).
If one fails to load the site still works: no animation, no 3D, native scrolling.
After deploying, open DevTools > Network and confirm all four requests return 200.
