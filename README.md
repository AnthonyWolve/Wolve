# Wolve

The portfolio of Anthony Wolve Eigbe. Chief Creative Officer, Lagos.

## How this site is laid out

| Page | Address | What it holds |
| --- | --- | --- |
| Home | `/` | Hero reel, selected work, stage, frames |
| Work | `/work/` | Every campaign and experience, plus earlier films |
| Case studies | `/work/<name>/` | One page per campaign |
| Frames | `/frames/` | The visual gallery, with a small, medium and large grid |
| Stage | `/stage/` | TEDxEnugu, juries, panels and workshops |
| Story | `/story/` | Bio, career, recognition, brands |
| Let's talk | `/contact/` | Email and socials |
| CIG version | `/cig/` | The November 2026 interview site, kept as it was. Old `?for=cig` links still land here |

## Where things live

- `tools/build.py` holds all the words and the list of work. Every page is built from it.
- `assets/site.css` is the look. `assets/site.js` is the motion and the gallery.
- `assets/` holds the photos, posters, video loops and fonts.

## Making a change

1. Edit the words in `tools/build.py`.
2. Run `python3 tools/build.py`. It rewrites every page.
3. Commit and push. GitHub Pages puts it live in about a minute.

Small text fixes can also be made straight in a page's `index.html` on github.com, but the next build will overwrite them, so put the same fix in `tools/build.py` too.
