"""Detecta UTF-8 inválido y secuencias típicas de mojibake en archivos del repositorio."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


PATTERNS = (
    re.compile(chr(0x00C3) + r"[\x80-\xbf]"),
    re.compile(chr(0x00C2) + r"[\x80-\xbf]"),
    re.compile(chr(0x00F0) + chr(0x0178)),
    re.compile(chr(0x00E2) + r"[€€™œ\x9d“”—…]"),
    re.compile(chr(0xFFFD)),
)


def main() -> int:
    names = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        text=True,
        encoding="utf-8",
    ).splitlines()
    findings: list[str] = []
    checked = 0
    skipped = 0
    for name in names:
        try:
            text = Path(name).read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            skipped += 1
            continue
        checked += 1
        for line_number, line in enumerate(text.splitlines(), 1):
            if any(pattern.search(line) for pattern in PATTERNS):
                findings.append(f"{name}:{line_number}:{line[:160]}")
    if findings:
        print("MOJIBAKE DETECTADO")
        print("\n".join(findings[:100]))
        return 1
    print(f"UTF-8 OK: {checked} archivos de texto; {skipped} binarios u omitidos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
