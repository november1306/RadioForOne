---
name: listen-link
description: Turn a curator queue (pasted text or file) into one verified click-to-listen YouTube link via dev/tools/make_listen_link.py, rescuing any mismatched tracks. Use when the user wants to listen to a suggested queue.
---

Produce a single `youtube.com/watch_videos?video_ids=...` link (temporary
anonymous playlist, max 50 tracks, nothing written to any account) for a
picked queue. The script does the deterministic work; your job is only the
rows it flags.

## Procedure

1. **Input.** If the argument is a file path, use it. If the user pasted a
   queue, save it *verbatim* to `dev/tools/queue-YYYY-MM-DD.txt` — the script
   parses curator output as-is (numbering, ★, `· annotations`, stray prose,
   duplicated paste tails are all handled). Do not reformat by hand.
2. **Run** `python dev/tools/make_listen_link.py <file>`.
3. **All rows `OK`** → verify and deliver (step 6).
4. **Rows marked `??` or `MISS`** — the search hit a different title or
   nothing. Rescue each one:
   a. **Ground truth from MusicBrainz** (1 req/s, User-Agent
      `RadioForOne/0.1 (tol1306@gmail.com)`): search
      `artist:"X" AND recording:"Y"` on `/ws/2/recording?fmt=json`; note the
      canonical title, length (ms), and release. If MusicBrainz has no such
      recording, the curator's track string itself is suspect — report it
      back instead of guessing.
   b. **Official audio route** (`ytmusicapi`, unauthenticated `YTMusic()`):
      `search(filter='artists')` → `get_artist(browseId)` → scan
      `albums`/`singles` results → `get_album(browseId)` tracklist for the
      title. Streaming albums sometimes carry fewer tracks than the
      MusicBrainz release — absence here is real, not a lookup failure.
   c. **Fan-upload fallback**: `search(filter='videos')`; pick the candidate
      whose duration exactly matches the MusicBrainz length, highest views
      as tiebreaker. Note the provenance in your report.
   d. **Substitute** the found videoId at the same position in the URL's
      `video_ids` list (don't rerun the whole script — other rows may
      reshuffle, search is nondeterministic).
5. **No rescue found** → drop the track from the link and say so explicitly;
   never ship a wrong-song ID to fill a slot.
6. **Verify** before delivering:
   `curl -sI "<link>" | grep -i "^location"` must 303-redirect to
   `youtube.com/watch?v=...&list=TLGG...`.
7. **Deliver** the link plus a one-line note per substitution, miss, or drop.

## Boundaries

- This is listening tooling for the founder's own queue reviews. It is NOT
  the resolver/hallucination gate (`verify_tracks.py` in the skill) and must not be
  presented as verification that a curator suggestion is real.
- Never create playlists in YT Music / any account for this workflow.
