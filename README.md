# Career management

Open this folder as its own Cursor project (File → Open Folder → `output/career-management`). Use `AGENTS.md` as the front door and the role files under `.cursor/agents/` when you invoke a specialist.

The frozen design is `ARCHITECTURE.md`. Do not redesign from this README.

## Flowchart

```mermaid
flowchart TD
  subgraph weekly [Weekly awareness]
    Vanguard[Mrs. Vanguard]
    Scripts[DOI resolve, dedupe, send checklist]
    Vanguard --> Scripts
    Scripts --> GrantMail[Monday grant digest]
    Scripts --> PaperMail[Thursday paper digest]
  end
  GrantMail --> GrantEnd[Grant path ends]
  Bar{Checklist met?}
  PaperMail --> Bar
  Bar -->|no| Stop[Digest only]
  Bar -->|yes| Pick[Mrs. Vanguard nominates one paper]
  Pick --> DevilBar[The Devil on the nomination]
  DevilBar -->|kill| PaperMail
  DevilBar -->|pass| Lantern[Mrs. Lantern, fresh chat]
  Lantern --> Pin[Frozen idea]
  Pin --> Write[Mrs. Lantern, fresh chat, idea file only]
  Write --> DevilDoc[The Devil on the document]
  DevilDoc -->|pass| Share[Mrs. Vanguard shares the document]
  DevilDoc -->|fail| Ananth[Ananth]
```





## Site

Edit `site/index.html` for homepage changes. Leave `site/index_original.html` alone.

## Human checkpoints

- What science to stand behind.
- Whether to apply, and to which call.
- A document The Devil failed.
- Any change to remit, recipients, or this path.

