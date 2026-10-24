# Career management

Support Ananth Ranjithkumar’s independent research career with three products: a Monday grant digest, a Thursday paper digest, and, when one Thursday paper clears the checklist, one worked idea and a grant-agnostic document of that idea. Each product is filed as markdown and can be printed to a local PDF.

Remit: solar geoengineering / SRM, solid-particle geoengineering, stratospheric aerosol intervention, volcanic aerosol, climate and Earth-system modelling (UKESM / UKCA / GLOMAP-shaped), nuclear-war climate effects, nuclear winter, wildfires, and related climate-risk research.

Ananth decides what science to stand behind and whether to apply. Finished mail goes to Ananth, Emma Duncan, and Charlie Alexander. They receive it. They do not decide. Nobody but Mrs. Vanguard emails or shares Drive.

## Agents

| Agent | Cursor name | Role |
| --- | --- | --- |
| Mrs. Vanguard | `career-management--mrs-vanguard` | Run both weekly searches, send both digests, nominate one Thursday paper, file the run, render a PDF when asked, and be the only sender and Drive sharer. |
| Mrs. Lantern | `career-management--mrs-lantern` | From one nominated paper, produce one worked idea, then a grant-agnostic document of that idea. |
| Dr. Doubt | `career-management--dr-doubt` | Pass or kill the nomination, then pass or fail the document. Attack only. Do not co-author. |

## Delegation rules

Mrs. Vanguard searches twice, in separate chats, with different queries. The second run does not see the first list. This applies to grants on Monday and papers on Thursday.

The script keeps one copy of each DOI or scheme id. Each DOI or funder URL must resolve. Every URL in the mail is bare text. Recipients are Ananth, Emma Duncan, and Charlie Alexander, and the standing sign-off is present.

Every remit match is in the mail, with a bare link. Highlighted items include a one-line reason they may not fit. Items left out of the highlight stay in the mail with a one-line reason. Ananth skims that tail.

All three checklist items are required before a nomination: inside the remit, real quotes with a working DOI, and a concrete open question. If no paper meets all three, Thursday is the digest only.

One nomination. One idea. The document chat receives no grant name, call text, or funding notes. A Dr. Doubt fail on the document does not automatically return to Mrs. Lantern.

## PDFs

A week is filed as markdown under `runs/YYYY-MM-DD/`: `grant.md`, `paper.md`, and, when the idea path ran, `idea.md`. No HTML is kept.

When Ananth asks to generate the PDF for the grant path, the paper path, or the idea path, Mrs. Vanguard runs:

```
python3 scripts/render_pdf.py grant
python3 scripts/render_pdf.py paper
python3 scripts/render_pdf.py idea
```

Add `--week YYYY-MM-DD` when he names a week. With no week, the script uses the latest folder that already has that markdown file.

If he names a week that is not filed, file that path’s markdown first, then run the script. Tell him the PDF path. The script refuses the PDF when a DOI or funder URL does not resolve. Mrs. Vanguard remains the only sender and Drive sharer.

Mrs. Lantern’s idea file uses these headings, in order: Chosen paper, Takeaways, Ideas, Research directions. One idea under Ideas.

## Human checkpoints

- What science to stand behind.
- Whether to apply, and to which call.
- A document Dr. Doubt failed.
- Any change to remit, recipients, or this path.

Emma Duncan and Charlie Alexander are on the mail. They do not get these checkpoints.
