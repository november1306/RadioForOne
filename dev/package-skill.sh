#!/usr/bin/env bash
# Build dist/radio-for-one.zip for upload to claude.ai / Claude desktop
# (Settings → Capabilities → Skills → Upload skill).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
rm -f dist/radio-for-one.zip
python - <<'PY'
import pathlib, zipfile
root = pathlib.Path("skills")
with zipfile.ZipFile("dist/radio-for-one.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted((root / "radio-for-one").rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts:
            z.write(p, p.relative_to(root).as_posix())
PY
echo "wrote dist/radio-for-one.zip"
