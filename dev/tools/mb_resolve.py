#!/usr/bin/env python3
"""Resolver gate: batch-resolve (artist, title) candidates to MusicBrainz
recording IDs. Curator hard rule 1 — no unverified track reaches the user.
Usage: python mb_resolve.py candidates.txt   (UTF-8 lines: Artist|Title)
Respects the 1 req/s MusicBrainz rate limit.
"""
import pathlib
import json
import sys
import time
import urllib.parse
import urllib.request

UA = "RadioForOne/0.1 (tol1306@gmail.com)"


def resolve(artist: str, title: str):
    query = f'artist:"{artist}" AND recording:"{title}"'
    url = (
        "https://musicbrainz.org/ws/2/recording?query="
        + urllib.parse.quote(query)
        + "&fmt=json&limit=5"
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    recs = data.get("recordings", [])
    if not recs:
        return None
    # prefer an exact-title match (avoids remixes/edits outranking originals)
    exact = [r for r in recs if r.get("title", "").casefold() == title.casefold()]
    r = exact[0] if exact else recs[0]
    credit = ", ".join(c["artist"]["name"] for c in r.get("artist-credit", []))
    return {
        "id": r["id"],
        "score": r.get("score", 0),
        "title": r.get("title", ""),
        "artist": credit,
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    lines = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").splitlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        artist, title = (p.strip() for p in line.split("|", 1))
        try:
            hit = resolve(artist, title)
        except Exception as e:  # noqa: BLE001 — log and keep batch going
            print(f"ERROR | {artist} | {title} | {e}")
            time.sleep(1.1)
            continue
        if hit is None:
            print(f"MISS  | {artist} | {title} | no result")
        else:
            print(
                f"{hit['score']:>3} | {artist} | {title} | "
                f"{hit['id'][:8]} | {hit['artist']} — {hit['title']}"
            )
        time.sleep(1.1)


if __name__ == "__main__":
    main()
