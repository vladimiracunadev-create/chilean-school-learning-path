#!/usr/bin/env python3
"""Validate visual structure and representation-safe links across the repository."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", ".venv", "node_modules", "__pycache__"}
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+\S")
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel"}
PUBLIC_ROOT = "https://vladimiracunadev-create.github.io/chilean-school-learning-path/"


def repository_files(root: Path, suffix: str) -> list[Path]:
    return sorted(
        path
        for path in root.rglob(f"*{suffix}")
        if not any(part in EXCLUDED_PARTS for part in path.parts)
    )


def link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    return target.split(maxsplit=1)[0]


def is_external(target: str) -> bool:
    return urlsplit(target).scheme.lower() in EXTERNAL_SCHEMES


def local_path(source: Path, target: str) -> Path | None:
    clean = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not clean:
        return None
    return (source.parent / clean).resolve()


def validate_markdown(path: Path, root: Path) -> list[str]:
    relative = path.relative_to(root).as_posix()
    errors: list[str] = []
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        return [f"{relative}: no es UTF-8 válido ({exc})"]
    if text.startswith("\ufeff"):
        errors.append(f"{relative}: contiene BOM UTF-8")
    if text and not text.endswith("\n"):
        errors.append(f"{relative}: no termina con salto de línea")

    headings: list[tuple[int, int]] = []
    fence: str | None = None
    for number, line in enumerate(text.splitlines(), start=1):
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = marker[0]
            elif marker[0] == fence:
                fence = None
            continue
        if fence is not None:
            continue
        heading = HEADING_RE.match(line)
        if heading:
            headings.append((number, len(heading.group(1))))
        elif re.match(r"^#{1,6}\S", line):
            errors.append(f"{relative}:{number}: título ATX sin espacio")
    if fence is not None:
        errors.append(f"{relative}: bloque de código sin cierre")
    h1_count = sum(level == 1 for _, level in headings)
    if h1_count != 1:
        errors.append(f"{relative}: debe contener exactamente un H1; encontrados={h1_count}")
    for (previous_line, previous), (number, current) in zip(headings, headings[1:]):
        if current > previous + 1:
            errors.append(
                f"{relative}:{number}: jerarquía salta de H{previous} a H{current} "
                f"después de la línea {previous_line}"
            )

    for match in MARKDOWN_LINK_RE.finditer(text):
        label, raw_target = match.groups()
        line = text.count("\n", 0, match.start()) + 1
        target = link_target(raw_target)
        if not label.strip():
            errors.append(f"{relative}:{line}: enlace sin texto visible")
        if not target:
            errors.append(f"{relative}:{line}: enlace sin destino")
            continue
        if is_external(target):
            if (
                target.startswith(PUBLIC_ROOT)
                and target.rstrip("/") != PUBLIC_ROOT.rstrip("/")
            ):
                errors.append(
                    f"{relative}:{line}: Markdown enlaza una página HTML pública secundaria: {target}"
                )
            continue
        resolved = local_path(path, target)
        if resolved is None:
            continue
        clean_suffix = resolved.suffix.lower()
        if clean_suffix in {".html", ".htm"} or "site" in resolved.parts:
            errors.append(f"{relative}:{line}: Markdown no debe enlazar HTML interno: {target}")
        if clean_suffix == ".md" and not resolved.is_file():
            errors.append(f"{relative}:{line}: Markdown enlazado no existe: {target}")
    return errors


def validate_html(path: Path, root: Path) -> list[str]:
    relative = path.relative_to(root).as_posix()
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"{relative}: no es UTF-8 válido ({exc})"]
    for match in HTML_LINK_RE.finditer(text):
        target = match.group(1).strip()
        line = text.count("\n", 0, match.start()) + 1
        if not target or is_external(target) or target.startswith("#"):
            continue
        resolved = local_path(path, target)
        if resolved is None:
            continue
        if resolved.suffix.lower() == ".md":
            errors.append(f"{relative}:{line}: HTML no debe enlazar Markdown interno: {target}")
        if resolved.suffix.lower() in {".html", ".htm"} and not resolved.is_file():
            errors.append(f"{relative}:{line}: HTML enlazado no existe: {target}")
    return errors


def validate(root: Path = ROOT) -> tuple[list[str], dict[str, int]]:
    markdown_files = repository_files(root, ".md")
    html_files = repository_files(root / "site", ".html") if (root / "site").is_dir() else []
    errors: list[str] = []
    for path in markdown_files:
        errors.extend(validate_markdown(path, root))
    for path in html_files:
        errors.extend(validate_html(path, root))
    return errors, {"markdown": len(markdown_files), "html": len(html_files)}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emite un resumen JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors, counts = validate()
    if args.json:
        print(json.dumps({"valid": not errors, "counts": counts, "errors": errors}, ensure_ascii=False, indent=2))
    elif errors:
        print("VALIDACIÓN DE PRESENTACIÓN FALLIDA")
        for error in errors[:200]:
            print(" -", error)
        if len(errors) > 200:
            print(f" - … y {len(errors) - 200} errores más")
    else:
        print(
            f"OK: {counts['markdown']} Markdown y {counts['html']} HTML cumplen "
            "estructura visual y separación de enlaces"
        )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
