# Content Pipeline

Working area for the **Writing Engine** skill (`.claude/skills/writing-engine/`). Each
idea is a single Markdown note that moves through these numbered folders as it
progresses through the Flowers writing process (Madman → Architect → Carpenter → Judge):

| Folder | Flowers role | Mindset | What lives here |
|--------|-------------|---------|-----------------|
| `00-idea-bank/` | Madman | Wild, generative | Raw ideas, no judgment |
| `01-research/` | Architect | Structural | Ideas with an outline + sources |
| `02-drafts/` | Carpenter | Crafting | Full working drafts |
| `03-review/` | Judge | Critical | Drafts being polished |
| `04-ready/` | — | Tactical | Approved, awaiting publish |

**Published posts do NOT live here.** When a note clears `04-ready/`, the skill
emits a real Hugo post into `content/posts/<slug>.md` (TOML front matter,
`draft = false`) and a LinkedIn-formatted version, then archives the pipeline note.

Notes are plain Markdown with YAML front matter (this is a working area, not Hugo
content — the YAML `status:` field tracks pipeline position). Promoting a note =
move the file to the next folder + update `status:`.

This folder is tracked in git so drafts are versioned and synced across machines.
