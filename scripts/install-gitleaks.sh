#!/bin/sh
# Official release, version and archive checksums pinned for repeatable local/CI scans.
set -eu
version=8.30.1
case "$(uname -s)-$(uname -m)" in
  Darwin-arm64) platform=darwin_arm64; checksum=b40ab0ae55c505963e365f271a8d3846efbc170aa17f2607f13df610a9aeb6a5 ;;
  Darwin-x86_64) platform=darwin_x64; checksum=dfe101a4db2255fc85120ac7f3d25e4342c3c20cf749f2c20a18081af1952709 ;;
  Linux-x86_64) platform=linux_x64; checksum=551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb ;;
  Linux-aarch64) platform=linux_arm64; checksum=e4a487ee7ccd7d3a7f7ec08657610aa3606637dab924210b3aee62570fb4b080 ;;
  *) echo "Install Gitleaks $version for this platform manually." >&2; exit 1 ;;
esac
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
curl --proto '=https' --proto-redir '=https' --tlsv1.2 --fail --silent --show-error --location \
  "https://github.com/gitleaks/gitleaks/releases/download/v$version/gitleaks_${version}_${platform}.tar.gz" \
  --output "$scratch/gitleaks.tar.gz"
python3 - "$scratch/gitleaks.tar.gz" "$checksum" <<'PY'
import hashlib
import sys
from pathlib import Path

if hashlib.sha256(Path(sys.argv[1]).read_bytes()).hexdigest() != sys.argv[2]:
    raise SystemExit("Gitleaks archive checksum mismatch")
PY
mkdir -p .runtime/tools
tar -xzf "$scratch/gitleaks.tar.gz" -C .runtime/tools gitleaks
chmod +x .runtime/tools/gitleaks
.runtime/tools/gitleaks version
