#!/usr/bin/env python3
"""Turn a picked queue into one click-to-listen YouTube link. Local only —
no account, no playlist created: youtube.com/watch_videos?video_ids=...
makes a temporary anonymous playlist (max 50 tracks).

Usage: python dev/tools/make_listen_link.py queue.txt

Accepts two line formats, auto-detected per line (UTF-8):
  Artist|Title                      — same as mb_resolve.py
  3. ★ Artist — Title · annotation  — curator queue output, pasted as-is

Prints the picked match per track for verification, then the link.
Rows marked ?? returned a different title than requested — verify those
(see .claude/skills/listen-link). Search is unauthenticated; this link is
for listening, not a resolver substitute.
"""
import pathlib
import re
import sys

from ytmusicapi import YTMusic

MAX_IDS = 50  # watch_videos URL cap
CURATOR_LINE = re.compile(r"^\d+\.\s*[★☆]?\s*(.+?)\s+[—–-]\s+(.+)$")


def parse_queue(lines):
    queue, seen = [], set()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "|" in line:
            artist, title = (p.strip() for p in line.split("|", 1))
        elif m := CURATOR_LINE.match(line):
            artist = m.group(1).strip()
            title = m.group(2).split(" · ", 1)[0].strip()
        else:
            continue  # prose between queue lines — not a track
        key = (artist.casefold(), title.casefold())
        if key not in seen:  # curator pastes often repeat the tail
            seen.add(key)
            queue.append((artist, title))
    return queue


def same_title(requested: str, returned: str) -> bool:
    norm = lambda s: s.replace("’", "'").casefold().strip()  # noqa: E731
    return norm(requested) == norm(returned)


def pick(yt: YTMusic, artist: str, title: str):
    af, tf = artist.casefold(), title.casefold()
    for flt in ("songs", "videos"):
        results = yt.search(f"{artist} {title}", filter=flt, limit=8)
        if not results:
            continue
        def match(r, want_title):
            names = " ".join(a.get("name", "") for a in r.get("artists", []))
            if af not in names.casefold():
                return False
            return not want_title or r.get("title", "").casefold() == tf
        # exact artist+title beats artist-only beats first hit
        for want_title in (True, False):
            for r in results:
                if match(r, want_title):
                    return r
        return results[0]
    return None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 2:
        sys.exit("usage: python dev/tools/make_listen_link.py queue.txt")
    lines = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").splitlines()
    queue = parse_queue(lines)
    if len(queue) > MAX_IDS:
        print(f"warning: {len(queue)} tracks, link holds {MAX_IDS} — truncating")
        queue = queue[:MAX_IDS]

    yt = YTMusic()
    video_ids = []
    for i, (artist, title) in enumerate(queue, 1):
        try:
            hit = pick(yt, artist, title)
        except Exception as e:  # noqa: BLE001 — log and keep batch going
            print(f"{i:>2}. ERR  | {artist} — {title}  ({e})")
            continue
        if hit is None:
            print(f"{i:>2}. MISS | {artist} — {title}")
            continue
        names = ", ".join(a.get("name", "") for a in hit.get("artists", []))
        video_ids.append(hit["videoId"])
        mark = "OK  " if same_title(title, hit.get("title", "")) else "??  "
        print(f"{i:>2}. {mark} | {artist} — {title}  =>  {names} — {hit.get('title')}")

    if not video_ids:
        sys.exit("\nnothing resolved — no link")
    print(f"\nLISTEN ({len(video_ids)}/{len(queue)} tracks):")
    print("https://www.youtube.com/watch_videos?video_ids=" + ",".join(video_ids))


if __name__ == "__main__":
    main()
