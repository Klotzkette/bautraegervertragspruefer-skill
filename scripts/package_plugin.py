#!/usr/bin/env python3
"""Build/check the portable plugin, prompt mirrors and deterministic ZIP."""

import argparse
import io
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/bautraegervertragspruefer"
ARCHIVE = ROOT / "docs/downloads/bautraegervertragspruefer-plugin.zip"


def targets():
    return {
        ROOT / "docs/SKILL.md": ROOT / "skill/SKILL.md",
        ROOT / "docs/MINI_SKILL.md": ROOT / "skill/MINI_SKILL.md",
        PLUGIN / "skills/bautraegervertrag-pruefen/references/werkstatt.md": ROOT / "skill/SKILL.md",
        PLUGIN / "LICENSE-MIT": ROOT / "LICENSE-MIT",
        PLUGIN / "LICENSE-APACHE": ROOT / "LICENSE-APACHE",
    }


def zip_bytes():
    buffer = io.BytesIO()
    with ZipFile(buffer, "w", ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(PLUGIN.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts or path.name == ".DS_Store":
                continue
            if path.is_symlink():
                raise ValueError(f"Symlink not allowed in plugin: {path}")
            entry = ZipInfo("bautraegervertragspruefer/" + path.relative_to(PLUGIN).as_posix(), (2026, 9, 4, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
    return buffer.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check committed files without writing")
    args = parser.parse_args()
    for destination, source in targets().items():
        if args.check:
            if not destination.is_file() or destination.read_bytes() != source.read_bytes():
                raise SystemExit(f"Stale/missing plugin mirror: {destination.relative_to(ROOT)}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(source.read_bytes())
    data = zip_bytes()
    if args.check:
        if not ARCHIVE.is_file() or ARCHIVE.read_bytes() != data:
            raise SystemExit("Plugin archive differs from plugin sources; run scripts/package_plugin.py")
    else:
        ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
        ARCHIVE.write_bytes(data)
    print(f"Plugin package {'verified' if args.check else 'built'}: {ARCHIVE.relative_to(ROOT)} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
