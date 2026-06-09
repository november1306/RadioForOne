# Radio for One

A radio station with an audience of exactly one listener — you.

It knows you deeply (through conversation, not clicks) and knows music culture
broadly. You talk to it about music the way you'd talk to a friend who actually
listens; it builds a taste dossier and turns "хочу щось тихе і темне на вечір"
into a queue that hits.

**Primary metric: chills per week.**

## Founding myth

On the evening of June 9, 2026, in Lviv, while the name was being chosen, the
founder's speakers — unprompted, mid-playlist — played
**DakhaBrakha — "Specially for You."**

The name "Radio for One" was locked in that minute. DakhaBrakha — «давати-брати»,
give and take — even names the architecture: the interviewer takes, the curator gives.

By decree of this myth, *Specially for You* is the first track Radio for One
will ever play: the demo queue opener, the bot's first broadcast.

## What's here

```
agents/     taste-interviewer.md  — the "grill me" interview agent (v0.1, drafted)
            curator.md            — the suggester agent (stub, next up)
docs/       prd.md                — product definition, blocks, roadmap, eval plan
evals/      personas/             — synthetic listeners for interviewer regression (L1)
dossiers/   per-user taste dossiers (markdown; gitignored except examples)
CLAUDE.md   working context & conventions for Claude Code sessions
```

## Status

Pre-M0. Current gate (from `docs/prd.md`): run the interviewer on the founder and
two friends; dossiers must pass the blind-distinguishability test before any
infrastructure is built.

## Principles (short form)

- Depth-of-one beats breadth-of-millions.
- Markdown over embeddings until evals prove otherwise.
- Prompts are code: no agent change lands without the eval suite.
- The model is fed from open data and conversation only (MusicBrainz, ListenBrainz,
  Last.fm); streaming services are swappable playback adapters.
- Every recommended track must resolve against a real catalog — the resolver is a
  hallucination gate, not a convenience.
