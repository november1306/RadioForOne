#!/usr/bin/env python3
"""Check that every track in a queue is a real MusicBrainz recording.

Usage: python verify_tracks.py queue.txt

Reads a queue as served (UTF-8), one track per line, in any of these forms:
  Artist — Title · why        (curator output; numbering, ★ and **bold** are fine)
  Artist - Title
  Artist|Title
Lines that aren't tracks (headers, prose, blank) are skipped.

Prints one row per track:
  OK   — a recording with this exact title exists for this artist
  ??   — closest hit has a different title; check it by hand
  MISS — nothing found; replace the track
  ERR  — lookup failed (network, rate limit)
Stdlib only. Respects the MusicBrainz 1 req/s rate limit.
"""
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "RadioForOne/0.1 ( https://github.com/november1306/RadioForOne )"
API = "https://musicbrainz.org/ws/2/recording"
PAUSE = 1.5  # seconds between requests; MB 503s on tighter bursts

PREFIX = re.compile(r"^\s*(?:\d+[.)]\s*)?[★☆*\s]*")
DASH = re.compile(r"\s+[—–-]\s+")


def parse_line(line):
    """Return (artist, title) for a track line, or None for anything else."""
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    line = PREFIX.sub("", line).replace("**", "")
    line = line.split(" · ", 1)[0].strip()
    if "|" in line:
        artist, title = line.split("|", 1)
    else:
        parts = DASH.split(line, 1)
        if len(parts) != 2:
            return None
        artist, title = parts
    artist, title = artist.strip(), title.strip().strip('"“”')
    if not artist or not title:
        return None
    return artist, title


def parse_queue(text):
    tracks, seen = [], set()
    for line in text.splitlines():
        track = parse_line(line)
        if track is None:
            continue
        key = tuple(s.casefold() for s in track)
        if key not in seen:
            seen.add(key)
            tracks.append(track)
    return tracks


def norm(s):
    return s.replace("’", "'").casefold().strip()


def lookup(artist, title):
    query = f'artist:"{artist}" AND recording:"{title}"'
    url = f"{API}?query={urllib.parse.quote(query)}&fmt=json&limit=5"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp).get("recordings", [])
        except urllib.error.HTTPError as e:
            if e.code != 503 or attempt == 2:
                raise
            time.sleep(PAUSE * 2)
    return []


def verdict(title, recordings):
    """Pick the best recording and classify the match."""
    if not recordings:
        return "MISS", None
    exact = [r for r in recordings if norm(r.get("title", "")) == norm(title)]
    if exact:
        return "OK", exact[0]
    return "??", recordings[0]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 2:
        sys.exit("usage: python verify_tracks.py queue.txt")
    text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    tracks = parse_queue(text)
    if not tracks:
        sys.exit("no track lines found")
    for i, (artist, title) in enumerate(tracks, 1):
        try:
            mark, rec = verdict(title, lookup(artist, title))
        except Exception as e:  # noqa: BLE001 — report and keep the batch going
            print(f"{i:>2}. ERR  | {artist} — {title} | {e}")
        else:
            if rec is None:
                print(f"{i:>2}. MISS | {artist} — {title}")
            else:
                credit = "".join(
                    c.get("name", c["artist"]["name"]) + c.get("joinphrase", "")
                    for c in rec.get("artist-credit", [])
                )
                print(
                    f"{i:>2}. {mark:<4} | {artist} — {title} | "
                    f"{rec['id']} | {credit} — {rec.get('title', '')}"
                )
        time.sleep(PAUSE)


if __name__ == "__main__":
    main()
