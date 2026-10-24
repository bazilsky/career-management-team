# Local desk

This project runs on the machine. It does not maintain a website.

## Products

Monday grant digest, Thursday paper digest, and, when one paper clears the checklist, one idea and a grant-agnostic document. Filed as markdown:

- `runs/YYYY-MM-DD/grant.md`
- `runs/YYYY-MM-DD/paper.md`
- `runs/YYYY-MM-DD/idea.md`

## PDF

When Ananth asks to generate the PDF for a path, Mrs. Vanguard runs `python3 scripts/render_pdf.py <grant|paper|idea>`. Add `--week YYYY-MM-DD` for a named week. Otherwise the latest filed week is used. If that week has no markdown, file it first, then render. The script checks every URL, prints with local Google Chrome, deletes the temporary page, and writes `runs/<week>/<path>.pdf`.

## Desk

Mrs. Vanguard, Mrs. Lantern, and Dr. Doubt (`career-management--dr-doubt`). One nomination. One idea. The idea file headings are Chosen paper, Takeaways, Ideas, Research directions.

The week of 28 September 2026 is filed under `runs/2026-09-28/`. That idea file records the three ideas from the digest that week. Later idea files hold one idea.

## Remit

Solar geoengineering / SRM, solid-particle geoengineering, stratospheric aerosol intervention, volcanic aerosol, UKESM / UKCA / GLOMAP, nuclear-war climate effects, nuclear winter, wildfires, and related climate-risk research.
