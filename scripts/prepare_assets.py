"""Prepare local web exports; never modify the supplied logo or design sources."""

import argparse
import base64
import hashlib
import http.client
import io
import json
import tarfile
from pathlib import Path
from urllib.parse import urlsplit

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "app/static"


def export(source, destination, width, quality=85):
    with Image.open(source) as image:
        image.thumbnail((width, width))
        image.save(destination, format="WEBP", quality=quality, method=6)


def vendor(package, version, wanted):
    url = f"https://registry.npmjs.org/{package}/{version}"
    metadata = json.loads(fetch_registry(url))
    data = fetch_registry(metadata["dist"]["tarball"])
    expected = metadata["dist"]["integrity"].split("sha512-")[1]
    if base64.b64encode(hashlib.sha512(data).digest()).decode() != expected:
        raise RuntimeError("Package integrity check failed")
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
        for source, dest in wanted.items():
            member = archive.getmember(source)
            output = STATIC / dest
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(archive.extractfile(member).read())
    return {
        "package": package,
        "version": version,
        "url": metadata["dist"]["tarball"],
        "integrity": metadata["dist"]["integrity"],
    }


def fetch_registry(url):
    parsed = urlsplit(url)
    if (
        parsed.scheme != "https"
        or parsed.hostname != "registry.npmjs.org"
        or parsed.username
        or parsed.port
    ):
        raise ValueError("Only the HTTPS npm registry is allowed.")
    connection = http.client.HTTPSConnection("registry.npmjs.org", timeout=60)
    try:
        connection.request("GET", parsed.path)
        response = connection.getresponse()
        if response.status != 200:
            raise RuntimeError("Registry download failed; redirects are not followed.")
        data = response.read(32 * 1024 * 1024 + 1)
        if len(data) > 32 * 1024 * 1024:
            raise ValueError("Unexpectedly large vendor package.")
        return data
    finally:
        connection.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hero", type=Path, required=True)
    parser.add_argument("--panorama", type=Path, required=True)
    args = parser.parse_args()
    images = STATIC / "images"
    images.mkdir(parents=True, exist_ok=True)
    export(args.hero, images / "hero.webp", 1920)
    export(args.panorama, images / "panorama.webp", 2048, 90)
    for key, source in [("project-01", "plot-a"), ("project-02", "plot-b")]:
        export(
            ROOT / f"design/concepts/v2/imagery-revision/assets/{source}.png",
            images / f"{key}.webp",
            1280,
        )
    export(ROOT / "RCPDL.png", images / "logo.webp", 600, 95)
    with Image.open(ROOT / "RCPDL.png") as logo:
        logo.thumbnail((96, 96))
        logo.save(images / "favicon.png")
    manifests = [
        vendor(
            "pannellum",
            "2.5.7",
            {
                "package/build/pannellum.js": "vendor/pannellum.js",
                "package/build/pannellum.css": "vendor/pannellum.css",
                "package/COPYING": "vendor/PANNELLUM-LICENSE.txt",
            },
        ),
        vendor(
            "@fontsource-variable/noto-sans",
            "5.3.0",
            {
                "package/files/noto-sans-latin-wght-normal.woff2": "fonts/noto-sans.woff2",
                "package/LICENSE": "fonts/NOTO-SANS-LICENSE.txt",
            },
        ),
        vendor(
            "@fontsource-variable/noto-sans-bengali",
            "5.3.0",
            {
                "package/files/noto-sans-bengali-bengali-wght-normal.woff2": "fonts/noto-bengali.woff2",
                "package/LICENSE": "fonts/NOTO-BENGALI-LICENSE.txt",
            },
        ),
    ]
    (STATIC / "vendor/MANIFEST.json").write_text(json.dumps(manifests, indent=2) + "\n")
    print("Prepared web exports, self-hosted fonts and panorama viewer.")


if __name__ == "__main__":
    main()
