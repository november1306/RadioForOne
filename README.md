# Radio for One

A radio station with an audience of exactly one listener — you.

It learns you through conversation, not clicks: a short interview and your
favorites list become a **taste dossier**, a markdown file you own. Then you ask for
music in your own words — "хочу щось тихе і темне на вечір", "heavy but not all the
same", "just play" — and get 10 tracks, each with a one-line *why* drawn from what
it knows about you. Tell it what hit and what missed; the next 10 get better.

**Primary metric: chills per week.**

## Install

**Claude Code**

```
/plugin install radio-for-one --marketplace november1306/RadioForOne
```

On older Claude Code versions, add the marketplace first:

```
/plugin marketplace add november1306/RadioForOne
/plugin install radio-for-one@radio-for-one
```

**claude.ai and Claude desktop**

1. Download `radio-for-one.zip` from the
   [latest release](https://github.com/november1306/RadioForOne/releases), or build
   it with `bash dev/package-skill.sh`.
2. Settings → Capabilities → Skills → Upload skill, and pick the zip.

## Use

Just talk about music: "recommend me something", "interview me about my taste",
"here are my favorites: …". The first time, it asks a few questions, reads any
favorites you paste, and serves your first queue.

**Where your dossier lives**

- Claude Code: `~/.radio-for-one/<name>.md`.
- claude.ai / Claude desktop chat: at the end of a conversation you get the updated
  dossier as a file. Attach it next time, or add it to a Project so it loads
  automatically.

It's plain markdown: read it, correct it, delete it. Every claim carries the quote
it came from.

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
skills/radio-for-one/   the product: SKILL.md + references (interview, favorites,
                        curate, dossier format) + scripts/verify_tracks.py
.claude-plugin/         plugin + marketplace manifests
dev/                    founder workspace: PRD, eval plan, history, tools, tests
```

## Principles (short form)

- Depth-of-one beats breadth-of-millions.
- Markdown over embeddings until evals prove otherwise.
- The model is fed from open data and conversation only (MusicBrainz, ListenBrainz,
  Last.fm); streaming services are swappable playback adapters.
- Every recommended track must be a real recording — verified, not assumed.
