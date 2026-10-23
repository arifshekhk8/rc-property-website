#!/usr/bin/env bash
set -euo pipefail
rc_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$rc_root"
if [ ! -x .venv/bin/python ]; then
  printf '%s\n' 'Create .venv and install requirements-dev.lock first; see app/README.md.'
  exit 1
fi
.venv/bin/python app/manage.py migrate --noinput
.venv/bin/python app/manage.py seed_demo
exec .venv/bin/python app/manage.py runserver "127.0.0.1:${RCP_PORT:-8000}"
