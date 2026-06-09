# PRD / Design Doc — Personal Radio (working title)

status: draft v0.1 · owner: DM · scope: high-level

## 1. One-liner

A music-nerd friend in chat: it knows *you* deeply (through conversation, not just
clicks) and knows music culture broadly (LLM), and turns "хочу щось тихе і темне на
вечір" into a queue that hits.

## 2. Problem

Streaming recommenders optimize engagement across millions of users; they model your
center of mass, not you. They cannot be told things ("this era of my library isn't me
anymore", "no vocals when I work"), they under-serve the long tail where chills live,
and they offer no conversation. Meanwhile people demonstrably *want* to talk about
their taste — to someone who actually listens.

## 3. Bet / value proposition

The LLM-era substitute for Spotify's collaborative-filtering moat is a rich,
user-co-authored taste dossier + an LLM that has absorbed decades of music discourse.
Depth-of-one beats breadth-of-millions for the listener who cares.

Primary success metric: **chills per week** (self-reported delight events from
unfamiliar artists). Secondary: queue acceptance rate, dossier correction rate
trending down, tester retention.

## 4. Target user

- v0: DM (dogfood).
- v1: 3–10 friends — music-invested people dissatisfied with algorithmic recs.
- Later: niche/long-tail listeners (post-rock, metal, experimental scenes) where
  mainstream recommenders fail hardest and word-of-mouth culture already exists.

## 5. Interaction modes (product surface = chat)

1. **Grill-me** — interviewer agent builds/updates the taste dossier. Sessions
   15–20 min, resumable, plus event-triggered micro-interviews.
2. **Vibe request** — user opens chat and says what they want *right now*, in
   abstractions ("guitar fuzz but sad", "background, no words, kid is asleep").
   Curator resolves it against the dossier into a queue.
3. **Lean-back radio** — "just play" with zero input; curator picks the likeliest
   mode from context (time of day, history) and runs a session.
4. **Feedback** — lightweight reactions in chat ("skip-not-for-me", "more like
   this", "that third track — wow"), folded back into the dossier.

## 6. Blocks

```
┌─────────────┐     ┌─────────────┐
│ Interviewer  │     │  Curator     │  ← "suggester"
│ (exists v0.1)│     │              │
└──────┬──────┘     └──┬───────┬──┘
       │  writes        │ reads  │ emits
       ▼                ▼        ▼
┌──────────────────┐   ┌──────────────┐
│  Dossier store    │   │ Annotated    │
│  (md in git)      │   │ queue        │
└──────────────────┘   └──┬───────────┘
       ▲                   ▼
┌──────┴──────┐     ┌──────────────┐
│ Feedback     │◄────│  Resolver +  │
│ collector    │     │  playback    │
└─────────────┘     │  adapter     │
                     └──────────────┘
```

**Interviewer** — done (v0.1, `taste-interviewer-agent.md`). Reference probes added.

**Curator (suggester)** — input: dossier + vibe request (or inferred mode) + recent
feedback. Tools: MusicBrainz/ListenBrainz/Last.fm lookups, web search for scene
context. Output: annotated queue — N tracks, each with a one-line *why* derived from
the dossier, framed per the dossier's `framing_style`. Internal steps: interpret
request → select mode → generate candidates (mostly inside the taste manifold;
exploration slots per mode's novelty dial) → verify every track exists (see Resolver)
→ order for flow.

**Dossier store** — plain markdown in a per-user git repo. Human-readable,
user-ownable, diff-able, exportable. (Same philosophy as the 3-docs-per-module
pattern: markdown over opaque vectors; provenance on every claim.)

**Resolver + playback adapter** — maps "Artist — Track" strings to canonical IDs
(MusicBrainz first) and then to the user's streaming service. Doubles as the
**hallucination gate**: any track the resolver can't confirm in MusicBrainz/the
service catalog is silently dropped and logged. v0 playback = write a playlist /
queue links into the user's service; the service is a swappable adapter
(personal-use Spotify first, Apple MusicKit as the product path).

**Feedback collector** — v0: chat reactions only. v1: ListenBrainz scrobble diffing
(what was actually played/skipped vs what was queued) for ground-truth feedback
without user effort.

## 7. v0 hosting & stack decision

Recommendation: **Telegram bot + Claude Agent SDK on a small VPS.**

- Telegram is the natural surface for the user base (UA + friends), gives chat UX,
  voice notes, inline buttons for feedback reactions — for free. No web app to build.
- Agent SDK (not Claude Code) because this is programmatic, unattended, multi-user
  orchestration — the established division of labor.
- Dossiers: one private git repo per user (or one repo, per-user dirs), bot commits
  after each session.
- Secrets/config per existing conventions (.env by role, env selector).

Stage 0 (this week, zero infra): a claude.ai Project — interviewer agent as project
instructions, dossier as project knowledge, curator runs as a second project. Manual,
but validates the conversations before any hosting work.

Parked (explicitly out of scope until v2+): the Threads resident agent that initiates
conversations in music topics. It's a distribution idea, not a product idea — it needs
the product to exist first, and it carries platform-automation policy and consent
questions that deserve their own review.

## 8. Non-goals (v0–v1)

- No own streaming/licensing. No mobile app. No embeddings/ML pipeline — the LLM +
  dossier + open metadata IS the model until evals prove it insufficient.
- No multi-tenant scaling work before 10 happy users.
- No Threads/social autonomous agent.

## 9. Testing pipeline

Three layers, automatable with the existing Claude Code eval habits:

**L1 — Interviewer evals (synthetic personas).**
Build 5–8 persona files: an LLM roleplays a listener with a hidden ground-truth
dossier (distinct carriers, framing styles, vetoes; include one terse/low-effort
persona and one eager-to-please persona). Run the interviewer against each persona
unattended; compare the extracted dossier to ground truth — field-level assertions
(carrier ranked top? veto captured? framing_style correct?) + LLM-as-judge for the
portrait paragraph. Regression-run on every interviewer prompt change.

**L2 — Curator evals (golden dossiers).**
Fixture dossiers + a bank of vibe requests → judge the emitted queue:
- hard assertions: zero veto violations; every track resolves in MusicBrainz
  (hallucination rate is THE metric to watch); obscurity targets met when
  framing_style = distinction; mode constraints respected (no vocals in focus mode).
- soft judge: does each "why" actually follow from the dossier?
- diversity check: no artist more than twice per queue, embedding-free heuristics
  (artist/label/era spread).

**L3 — Human eval (the only one that counts).**
- Blind distinguishability: given the friends' dossiers unlabeled, can DM match
  dossier → person? If not, the interviewer extracts platitudes.
- Chills journal: testers log delight events for 4 weeks; compare against their
  Spotify-radio baseline week.
- Read-back correction rate per session, trending down = dossier converging.

CI shape: persona + golden-dossier suites run nightly via Agent SDK; report to the
existing GH Actions + Pages habits. Prompt changes go through the suite before merge —
prompts are code.

## 10. Risks

| Risk | Mitigation |
|---|---|
| LLM hallucinates tracks/artists | Resolver gate; hallucination rate in CI; never show unresolved tracks |
| Spotify ToS (ML/profile clauses) | Model fed ONLY from open data (MusicBrainz/ListenBrainz/Last.fm) + user conversation; Spotify used solely as user-authorized playback; Apple MusicKit as the product path. Verify current playlist-write endpoints (Feb 2026 API changes shuffled them) during the resolver spike |
| Dossier privacy (taste reveals identity, politics) | User-owned repo, exportable, deletable; veto rules stored in user's own words; no third-party sharing |
| Sycophantic dossier (sounds deep, says nothing) | L3 blind-distinguishability test as acceptance gate |
| Over-building (known tendency) | Stage 0 requires zero infra; no component is built before the previous stage's eval passes |

## 11. Roadmap

- **M0 (now):** claude.ai Project dogfood — interviewer on self + 2 friends; manual
  curator runs; blind-distinguishability check. Gate: dossiers are distinguishable.
- **M1:** Telegram bot, Agent SDK host, resolver with MusicBrainz gate, playlist
  writing; 5 testers; L1/L2 eval suites in CI. Gate: hallucination rate < 2%,
  queue acceptance > 60%.
- **M2:** ListenBrainz scrobble feedback loop; event-triggered micro-interviews;
  chills-journal study vs baseline. Gate: chills/week beats personal Spotify baseline.
- **M3:** Apple MusicKit in-chat playback path; onboarding for strangers.
- **Parked:** Threads outreach agent; embedding pipeline (only if L2 evals show the
  LLM+metadata curator plateauing).
