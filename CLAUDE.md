# CLAUDE.md — Radio for One

## What this project is

A chat-first personal radio: an interviewer agent builds a per-user taste dossier
through conversation; a curator agent turns the dossier + a vibe request into an
annotated track queue. Read `docs/prd.md` before non-trivial work — it defines the
blocks, the roadmap gates, and the three-layer eval plan (L1 interviewer personas,
L2 curator golden-dossiers, L3 human blind tests).

## Conventions

- **Prompts are code.** Agent definitions live in `agents/*.md` with YAML
  frontmatter (Claude Code skill format). Any change to an agent must run the
  relevant eval suite before merge. No "small prompt tweaks" outside this rule.
- **Dossiers are markdown, user-owned, evidence-bearing.** Every claim in a dossier
  carries confidence + verbatim evidence quote + status, per the schema in
  `agents/taste-interviewer.md`. Never silently rewrite a user's dossier — append
  and date.
- **Open data only feeds the model.** MusicBrainz / ListenBrainz / Last.fm.
  Spotify content must never be ingested into prompts, dossiers, or evals
  (Developer Policy prohibits ML/profile use). Spotify may appear only as a
  user-authorized playback adapter behind `resolver/`.
- **Resolver = hallucination gate.** No track string reaches a user without
  resolving to a MusicBrainz ID. Hallucination rate is a tracked CI metric.
- **Language:** user-facing agents mirror the user (UA/EN). Code and docs in English.

## Current focus (pre-M0 → M0)

1. `agents/curator.md` — draft the suggester. Inputs: dossier + vibe request.
   Output: queue of N tracks, each with a one-line *why* derived from dossier
   fields, framed per `framing_style`. The inference maps in the interviewer's
   dossier schema were written to feed this agent directly.
2. `evals/personas/` — L1 harness: 5–8 synthetic listener personas, each a hidden
   ground-truth dossier + roleplay instructions. Include one terse/low-effort
   persona and one eager-to-please persona (the two failure modes of elicitation).
   Runner: interviewer vs persona unattended → extracted dossier → field-level
   assertions + LLM-as-judge vs ground truth.
3. M0 gate is HUMAN, not automated: founder + two friends interviewed, dossiers
   blind-matched to their humans. Do not build Telegram/hosting/resolver until
   this gate passes (see prd.md §11).

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

## Agent skills

### Issue tracker

Issues live in GitHub Issues on november1306/RadioForOne (via `gh`). See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-role vocabulary: needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `CONTEXT.md` + `docs/adr/` at the repo root (created lazily). See `docs/agents/domain.md`.
