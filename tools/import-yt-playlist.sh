#!/usr/bin/env bash
# Import a YouTube playlist as raw listening data for a dossier.
#
# Usage:
#   tools/import-yt-playlist.sh <playlist-url> [output-file]
#
# Prints "title | uploader" per track (UTF-8). If output-file is given, writes
# there instead of stdout. Paste the result into the dossier's
# "Raw listening data" appendix with date + source URL — it is evidence,
# not claims (see agents/taste-interviewer.md, rule 12).
#
# Caveats:
#   - Works for public/unlisted playlists. Private ones need
#     --cookies-from-browser <browser> added to the yt-dlp call.
#   - Uploader is often but not always the artist ("- Topic" channels are
#     auto-generated artist channels; others may be fan/label uploads).
#     Resolve via MusicBrainz before treating as artist ground truth.

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <playlist-url> [output-file]" >&2
  exit 1
fi

url="$1"
out="${2:-}"

# yt-dlp may be on PATH or installed as a Python module only.
if command -v yt-dlp >/dev/null 2>&1; then
  ytdlp=(yt-dlp)
else
  ytdlp=(python -m yt_dlp)
fi

export PYTHONIOENCODING=utf-8

if [[ -n "$out" ]]; then
  "${ytdlp[@]}" --flat-playlist --print "%(title)s | %(uploader)s" "$url" > "$out"
  echo "wrote $(wc -l < "$out") tracks to $out" >&2
else
  "${ytdlp[@]}" --flat-playlist --print "%(title)s | %(uploader)s" "$url"
fi
