# Career Management Team / Lighthouse — workflow flowchart

Locked 27 Sep 2026. Sole sender: Mrs. Vanguard.

```mermaid
flowchart TD
  Ananth([Ananth — owner decisions:<br/>science / apply / which call])

  subgraph Roles["Team roles"]
    V[Mrs. Vanguard<br/>coordinate · search · digests<br/>sole email/send]
    L[Mrs. Lantern<br/>shortlist · ideas · directions<br/>not grants · never sends]
    D[The Devil<br/>PASS/KILL · FAIL critics<br/>ideas only · never sends]
  end

  subgraph Joke["Digest joke rota only"]
    J1[Mrs. V] --> J2[D] --> J3[Mrs. L] --> J1
  end

  Joke -.->|opener + byline<br/>Mrs. V / D / Mrs. L| MonDigest
  Joke -.->|opener + byline| ThuDigest
  Joke -.->|no joke| IdeaEmail

  subgraph Mon["Monday — grants only"]
    M1[V: two grant searches<br/>separate fresh chats] --> M2[Merge · dedupe · verify URLs<br/>compare prior digests]
    M2 --> M3[Build grant digest<br/>GO/MAYBE/NO-GO · Georgia HTML]
    M3 --> M4{Send checks?}
    M4 -->|pass + nonempty| MonDigest[V sends Monday digest<br/>sign-off: Mrs. V, Career Mgmt Team]
    M4 -->|fail / empty| M6[No send · record reason]
    MonDigest --> MStop([HARD STOP<br/>no Devil · no Lantern · no apply])
    M6 --> MStop
  end

  subgraph Thu["Thursday — papers + optional idea path"]
    T1[V: two paper searches<br/>separate fresh chats] --> T2[Merge · dedupe by DOI<br/>verify · compare prior]
    T2 --> T3[Build six newest→oldest]
    T3 --> ThuDigest[V sends paper digest]
    ThuDigest --> T4[V ships all six to Lantern]
    T4 --> T5[L alone shortlists ≤3<br/>author-documented quoted<br/>inferred marked]
    T5 --> T6[D fresh chat: PASS/KILL each<br/>no beauty contest]
    T6 -->|all KILL| T7[Record kills · STOP idea path]
    T6 -->|≥1 PASS| T8[L picks one PASSed paper]
    T8 --> T9[L: ≤5 ideas + research-directions write-up]
    T9 --> T10[D separate fresh chat:<br/>each idea + doc as whole]
    T10 -->|doc PASS| IdeaEmail[V: Idea Path Activated email<br/>all ideas · red FAIL critics<br/>blue joint note · no joke]
    T10 -->|doc FAIL| T11[V emails Ananth only<br/>no auto-rewrite · no wider share]
  end

  MonDigest --> Ananth
  ThuDigest --> Ananth
  IdeaEmail --> Ananth
  T11 --> Ananth
  M6 --> Ananth

  V --- M1
  V --- T1
  V --- MonDigest
  V --- ThuDigest
  V --- IdeaEmail
  V --- T4
  L --- T5
  L --- T8
  L --- T9
  D --- T6
  D --- T10

  Ananth -.->|feedback / go-ahead / unlock Emma·Charlie| V
```

## Edges that matter
- Monday never feeds idea path.
- Paper digest always sends before idea work; idea path never holds the digest.
- Devil never touches Monday or shortlist choice; two fresh chats (shortlist vs ideas+doc).
- Idea-path email: no joke opener; joint note bold dark blue; sign-off Mrs. V, Ananth's Career Management Team.
