#!/usr/bin/env sh
set -eu

APP_DIR="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$APP_DIR"

if [ -x "AudioStemLab/AudioStemLab" ]; then
  exec "AudioStemLab/AudioStemLab"
fi

if [ -x ".venv311/bin/python" ]; then
  exec .venv311/bin/python app.py
fi

exec python3 app.py
