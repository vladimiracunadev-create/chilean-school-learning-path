"""Validate the repository's layered licensing policy and provenance boundaries."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "LICENSE", "LICENSE-CONTENT.md", "LICENSING.md", "LICENSING_AUDIT.md",
    "DATA-LICENSE.md", "THIRD_PARTY_NOTICES.md", "ASSET_LICENSES.md",
    "TRADEMARKS.md", "CONTRIBUTING.md", "docs/COMMERCIAL_USE.md",
    "docs/LICENSING_HISTORY.md", "config/licensing-policy.json", "CURRICULUM.md",
    "LEARNING_PATHS.md", "OFFICIAL_REFERENCES.md",
    "sources/mineduc-curriculum-snapshot.json", "content/developed-lessons.json",
    "curriculum/catalog.json", "site/catalog.json", "site/index.html",
    "site/styles.css", "site/app.js",
]
LEGAL_MARKDOWN = [
    "LICENSE-CONTENT.md", "LICENSING.md", "LICENSING_AUDIT.md", "DATA-LICENSE.md",
    "ASSET_LICENSES.md", "THIRD_PARTY_NOTICES.md", "TRADEMARKS.md",
    "COMMERCIAL-LICENSING.md", "CONTRIBUTING.md", "docs/COMMERCIAL_USE.md",
    "docs/LICENSING_HISTORY.md",
]
SOURCE_REQUIRED = {
    "id", "title", "author_or_owner", "source_url", "resource_type", "license",
    "redistributed", "modified", "commercial_allowed", "status",
}
TEXT_SUFFIXES = {"", ".css", ".html", ".js", ".json", ".md", ".py", ".xml", ".yaml", ".yml"}
ASSET_SUFFIXES = {
    ".avif", ".eot", ".gif", ".ico", ".jpeg", ".jpg", ".mp3", ".mp4",
    ".ogg", ".otf", ".pdf", ".png", ".svg", ".ttf", ".wav", ".webm",
    ".webp", ".woff", ".woff2",
}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def load_json(path: Path, errors: list[str], root: Path) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"JSON inválido en {relative(path, root)}: {exc}")
        return None


def iter_repository_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts:
            yield path


def validate_legal_links(root: Path, errors: list[str]) -> None:
    for name in LEGAL_MARKDOWN:
        source = root / name
        if not source.is_file():
            continue
        for raw_target in MARKDOWN_LINK.findall(source.read_text(encoding="utf-8")):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            destination = (source.parent / unquote(target)).resolve()
            try:
                destination.relative_to(root.resolve())
            except ValueError:
                errors.append(f"Enlace legal sale del repositorio: {name} -> {raw_target}")
                continue
            if not destination.exists():
                errors.append(f"Enlace legal roto: {name} -> {raw_target}")


def validate_canonical_data_license(root: Path, errors: list[str]) -> None:
    canonical = "DATA-LICENSE.md"
    stale_names = {
        "DATA" + "_LICENSE.md",
        "DATA" + "_LICENSES.md",
        "DATA-" + "LICENSES.md",
    }
    for stale in stale_names:
        if (root / stale).exists():
            errors.append(f"Alias legal obsoleto presente: {stale}; usar {canonical}")
    historical_allowlist = {
        "LICENSING_AUDIT.md",
        "docs/LICENSING_HISTORY.md",
        "site/docs/licensing-audit.html",
        "site/docs/licensing-history.html",
    }
    for path in iter_repository_files(root):
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        name = relative(path, root)
        if name in historical_allowlist:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for stale in stale_names:
            if stale in text:
                errors.append(f"Referencia obsoleta a {stale} en {name}")


def validate_source_snapshot(root: Path, errors: list[str]) -> None:
    snapshot = load_json(root / "sources/mineduc-curriculum-snapshot.json", errors, root)
    if not isinstance(snapshot, dict):
        return
    required = {"source", "source_url", "verified_at", "rights_notice", "records"}
    missing = required - snapshot.keys()
    if missing:
        errors.append(f"Snapshot MINEDUC sin {', '.join(sorted(missing))}")
        return
    notice = str(snapshot["rights_notice"])
    if "MINEDUC" not in notice.upper() and "titulares" not in notice:
        errors.append("Snapshot MINEDUC sin aviso de derechos reconocible")
    if not str(snapshot["source_url"]).startswith("https://www.curriculumnacional.cl/"):
        errors.append("Snapshot MINEDUC con source_url inesperada")
    records = snapshot["records"]
    if not isinstance(records, list) or not records:
        errors.append("Snapshot MINEDUC sin registros")
        return
    record_fields = {"course", "course_slug", "course_url", "subject", "subject_slug", "subject_url", "objectives"}
    objective_fields = {"code", "description", "axis", "url"}
    for record_index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            errors.append(f"Snapshot: registro #{record_index} no es objeto")
            continue
        record_missing = record_fields - record.keys()
        if record_missing:
            errors.append(f"Snapshot: registro #{record_index} sin {', '.join(sorted(record_missing))}")
            continue
        if not str(record["course_url"]).startswith("https://www.curriculumnacional.cl/") or not str(record["subject_url"]).startswith("https://www.curriculumnacional.cl/"):
            errors.append(f"Snapshot: registro #{record_index} sin URLs oficiales")
        objectives = record["objectives"]
        if not isinstance(objectives, list) or not objectives:
            errors.append(f"Snapshot: registro #{record_index} sin objetivos")
            continue
        for objective_index, objective in enumerate(objectives, start=1):
            if not isinstance(objective, dict):
                errors.append(f"Snapshot: objetivo #{record_index}.{objective_index} no es objeto")
                continue
            objective_missing = objective_fields - objective.keys()
            if objective_missing:
                errors.append(f"Snapshot: objetivo #{record_index}.{objective_index} sin {', '.join(sorted(objective_missing))}")
            if not str(objective.get("url", "")).startswith("https://www.curriculumnacional.cl/"):
                errors.append(f"Snapshot: objetivo #{record_index}.{objective_index} sin URL oficial")
            for reading_index, reading in enumerate(objective.get("readings", []), start=1):
                if not isinstance(reading, dict) or not reading.get("title") or not str(reading.get("url", "")).startswith("https://"):
                    errors.append(f"Snapshot: lectura #{record_index}.{objective_index}.{reading_index} sin título/URL")


def validate_inventories(root: Path, errors: list[str]) -> None:
    asset_registry = (root / "ASSET_LICENSES.md").read_text(encoding="utf-8")
    for path in iter_repository_files(root):
        if path.suffix.lower() in ASSET_SUFFIXES:
            name = relative(path, root)
            if name not in asset_registry:
                errors.append(f"Activo no inventariado en ASSET_LICENSES.md: {name}")
    data_registry = (root / "DATA-LICENSE.md").read_text(encoding="utf-8")
    datasets = []
    for directory in (root / "sources", root / "content"):
        datasets.extend(directory.rglob("*.json"))
    datasets.extend([root / "curriculum/catalog.json", root / "site/catalog.json"])
    for path in datasets:
        name = relative(path, root)
        if name not in data_registry:
            errors.append(f"Dataset no inventariado en DATA-LICENSE.md: {name}")


def validate_generated_outputs(root: Path, errors: list[str]) -> None:
    markdown_pages = sorted((root / "curriculum").glob("*/*/*.md"))
    html_pages = sorted((root / "site/classes").glob("*/*/*.html"))
    if not markdown_pages or not html_pages:
        errors.append("No existen fichas generadas Markdown/HTML para validar")
        return
    for path in markdown_pages:
        text = path.read_text(encoding="utf-8").casefold()
        if "quedan cubiertos por la licencia" not in text.replace("\n> ", " "):
            errors.append(f"Salida Markdown sin aviso de derechos oficiales: {relative(path, root)}")
    for path in html_pages:
        text = path.read_text(encoding="utf-8").casefold()
        if "se relicencian bajo cc by-nc-sa 4.0" not in text or "texto oficial mineduc: derechos de su titular" not in text:
            errors.append(f"Salida HTML con aviso de derechos incompleto: {relative(path, root)}")
    for name in ("curriculum/catalog.json", "site/catalog.json"):
        document = load_json(root / name, errors, root)
        if isinstance(document, dict) and not document.get("rights_notice"):
            errors.append(f"{name} sin rights_notice heredado de la fuente")


def validate_example_registries(root: Path, errors: list[str]) -> None:
    for path in (root / "examples").glob("*.json"):
        document = load_json(path, errors, root)
        if not isinstance(document, dict) or not isinstance(document.get("sources"), list):
            continue
        seen: set[str] = set()
        for index, record in enumerate(document["sources"], start=1):
            if not isinstance(record, dict):
                errors.append(f"{path.name}: source #{index} no es objeto")
                continue
            missing = SOURCE_REQUIRED - record.keys()
            if missing:
                errors.append(f"{path.name}: source #{index} sin {', '.join(sorted(missing))}")
            identifier = str(record.get("id", f"#{index}"))
            if identifier in seen:
                errors.append(f"{path.name}: id duplicado {identifier}")
            seen.add(identifier)
            if record.get("license") == "UNKNOWN" and record.get("redistributed") is True:
                errors.append(f"{path.name}: {identifier} UNKNOWN redistribuido")
            if record.get("status") == "quarantined" and record.get("redistributed") is True:
                errors.append(f"{path.name}: {identifier} en cuarentena redistribuido")


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for name in REQUIRED_FILES:
        if not (root / name).is_file():
            errors.append(f"Falta {name}")
    if errors:
        return errors
    policy = load_json(root / "config/licensing-policy.json", errors, root)
    if isinstance(policy, dict):
        expected = {
            "software": "MIT",
            "educational_content": "CC-BY-NC-SA-4.0",
            "unknown_external_content": "QUARANTINE",
            "official_text": "RIGHTS_RETAINED_BY_SOURCE",
            "generated_outputs": "INHERIT_BY_COMPONENT",
        }
        for key, value in expected.items():
            if policy.get(key) != value:
                errors.append(f"Política: {key} debe ser {value}")
    license_text = (root / "LICENSE").read_text(encoding="utf-8")
    for token in ("MIT License", "Permission is hereby granted, free of charge", 'THE SOFTWARE IS PROVIDED "AS IS"'):
        if token not in license_text:
            errors.append(f"LICENSE incompleto: {token}")
    content_license = (root / "LICENSE-CONTENT.md").read_text(encoding="utf-8")
    for token in ("Trayectoria Escolar Chile", "CC BY-NC-SA 4.0", "chilean-school-learning-path"):
        if token not in content_license:
            errors.append(f"LICENSE-CONTENT.md incompleto: {token}")
    data_license = (root / "DATA-LICENSE.md").read_text(encoding="utf-8")
    for token in ("mineduc-curriculum-snapshot.json", "curriculum/catalog.json", "site/catalog.json", "developed-lessons.json"):
        if token not in data_license:
            errors.append(f"DATA-LICENSE.md no documenta {token}")
    validate_legal_links(root, errors)
    validate_canonical_data_license(root, errors)
    validate_source_snapshot(root, errors)
    validate_inventories(root, errors)
    validate_generated_outputs(root, errors)
    validate_example_registries(root, errors)
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDACIÓN FALLIDA")
        for error in errors:
            print(" -", error)
        return 1
    print("OK: capas de licencia, procedencia, inventarios, enlaces y salidas generadas validados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
