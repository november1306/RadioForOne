---
name: curator
description: >
  STUB — to be drafted in Claude Code (see CLAUDE.md "Current focus" #1).
  Turn a taste dossier + a vibe request into an annotated queue: N real,
  resolver-verified tracks, each with a one-line why derived from dossier
  fields, framed per the dossier's framing_style.
---

# Curator — TODO (M0)

Contract (from docs/prd.md §6):

- **Input:** `dossiers/{user}.md` + vibe request (free text, UA/EN) or inferred mode.
- **Tools:** MusicBrainz / ListenBrainz / Last.fm lookups; web search for scene context.
- **Output:** queue of N tracks: `Artist — Track · why (one line, dossier-derived)`.
- **Hard rules:** zero veto violations; every track must resolve (no hallucinated
  tracks ever shown); exploration slots sized by the active mode's novelty dial;
  obscurity targeting when framing_style = distinction; no artist more than twice.
- First track of the first-ever queue: DakhaBrakha — "Specially for You".
