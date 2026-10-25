# CLAUDE.md — Radio for One

## What this project is

A personal radio, shipped as one installable skill (`skills/radio-for-one/`) for
Claude Code, claude.ai and Claude desktop. It interviews a listener and reads their
favorites into a taste dossier, then serves 10-track queues with a *why* per track
and learns from reactions. `dev/prd.md` holds the product thinking, roadmap gates
and the three-layer eval plan (L1 interviewer personas, L2 curator golden dossiers,
L3 human blind tests).

## Layout

- `skills/radio-for-one/` — **the product**. Everything here ships to users, so it
  stays general: no founder data, no session history, no dated changelogs.
  `SKILL.md` routes; `references/` hold the method (interview, favorites, curate,
  dossier format).
- `dev/` — founder workspace: PRD, `history/` (past session learnings), `tools/`
  (listen-link, playlist import), `evals/`, `tests/`.
- `dossiers/` — real listener dossiers, gitignored. The founder's is
  `dossiers/dm.md`; when running the skill in this repo, use it.

## Conventions

- **Learnings go to the right home.** A lesson about one listener goes into their
  dossier. A lesson that holds for any listener becomes a rule in the matching
  reference file, written in its current form — git keeps the history.
- **Prompts are code.** A change to the skill should run the relevant eval suite
  before merge. Until L1/L2 exist, the founder's explicit go-ahead in chat stands
  in for it; say which suite would have covered the change.
- **Dossiers are markdown, user-owned, evidence-bearing.** Format and update rules:
  `skills/radio-for-one/references/dossier.md`.
- **Open data only feeds the model.** MusicBrainz / ListenBrainz / Last.fm.
  Spotify content must never be ingested into prompts, dossiers, or evals
  (Developer Policy prohibits ML/profile use). Spotify may appear only as a
  user-authorized playback adapter.
- **Every served track is verified** (curate.md, Verification).
- **Language:** the skill mirrors the listener (UA/EN). Code and docs in English.
- **Tests:** `python -m unittest discover dev/tests`. Package for claude.ai:
  `bash dev/package-skill.sh`.

## Current focus (M0)

1. Publish the skill and dogfood it: founder + two friends install it, get
   interviewed, and use the queues.
2. M0 gate is HUMAN, not automated: the three dossiers blind-matched to their
   humans. Do not build Telegram/hosting/resolver infrastructure until this gate
   passes (see `dev/prd.md` §11).
3. Next after the gate: a click-to-listen radio link (prototype in
   `dev/tools/make_listen_link.py`).

## Scope guard (standing instruction from the founder)

The founder is a self-acknowledged over-builder. If a session starts drifting
toward infrastructure ahead of the current roadmap gate (embeddings, multi-tenant
hosting, social-platform agents, "while we're at it" frameworks) — say so plainly
and point at the gate. Elegant architecture that skips a gate is scope creep
wearing a suit.

## Founding facts

- Name: Radio for One. First track ever to be played: DakhaBrakha — "Specially
  for You" (see README founding myth — keep it intact).
- Parked ideas (do not develop unprompted): Threads outreach agent; NeoPromin
  (separate product); embedding/ML pipeline (only if L2 evals plateau).
