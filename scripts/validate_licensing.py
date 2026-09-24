from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "LICENSE", "LICENSE-CONTENT.md", "LICENSING.md", "DATA-LICENSE.md",
    "THIRD_PARTY_NOTICES.md", "TRADEMARKS.md", "CURRICULUM.md",
    "LEARNING_PATHS.md", "OFFICIAL_REFERENCES.md", "curriculum/catalog.json",
    "site/index.html", "site/styles.css", "site/app.js",
]
SOURCE_REQUIRED = {
    "id", "title", "author_or_owner", "source_url", "resource_type", "license",
    "redistributed", "modified", "commercial_allowed", "status",
}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def load_json(path: Path, errors: list[str], root: Path) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"JSON inválido en {path.relative_to(root)}: {exc}")
        return None


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"Falta {relative}")
    if errors:
        return errors

    policy = load_json(root / "config/licensing-policy.json", errors, root)
    if isinstance(policy, dict):
        expected = {"software": "MIT", "educational_content": "CC-BY-NC-SA-4.0", "unknown_external_content": "QUARANTINE"}
        for key, value in expected.items():
            if policy.get(key) != value:
                errors.append(f"Política: {key} debe ser {value}")

    license_text = (root / "LICENSE").read_text(encoding="utf-8")
    for token in ("MIT License", "Permission is hereby granted, free of charge", 'THE SOFTWARE IS PROVIDED "AS IS"'):
        if token not in license_text:
            errors.append(f"LICENSE incompleto: {token}")

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

    manifest = load_json(root / "PACKAGE_MANIFEST.json", errors, root)
    if isinstance(manifest, dict):
        files = manifest.get("files")
        if not isinstance(files, list) or len(files) != len(set(files)):
            errors.append("PACKAGE_MANIFEST.json: files debe ser una lista sin duplicados")
        else:
            for relative in files:
                if not (root / relative).is_file():
                    errors.append(f"Manifiesto apunta a archivo inexistente: {relative}")
        for relative in manifest.get("generated_roots", []):
            if not (root / relative).is_dir():
                errors.append(f"Directorio generado inexistente: {relative}")

    catalog = load_json(root / "curriculum/catalog.json", errors, root)
    if isinstance(catalog, dict):
        classes = catalog.get("classes")
        if not isinstance(classes, list):
            errors.append("El catálogo no contiene una lista de clases")
        else:
            for key, value in {"class_count": 192, "subjects": 16, "levels": 4}.items():
                if catalog.get(key) != value:
                    errors.append(f"Catálogo: {key} debe ser {value}")
            if len(classes) != 192:
                errors.append(f"Catálogo: se esperaban 192 clases y hay {len(classes)}")
            ids = [item.get("id") for item in classes if isinstance(item, dict)]
            if ids != list(range(1, 193)):
                errors.append("Catálogo: ids deben ser consecutivos 1..192")
            subjects = {item.get("subject") for item in classes if isinstance(item, dict)}
            levels = {item.get("level") for item in classes if isinstance(item, dict)}
            if len(subjects) != 16 or levels != {1, 2, 3, 4}:
                errors.append("Catálogo: asignaturas o niveles no coinciden con 16 × 4")
            for item in classes:
                if not isinstance(item, dict):
                    continue
                for field in ("topic", "subject", "level", "outcome", "practice", "evidence", "path"):
                    if not item.get(field):
                        errors.append(f"Clase {item.get('id', '?')}: falta {field}")
                if not (root / str(item.get("path", ""))).is_file():
                    errors.append(f"Clase {item.get('id', '?')}: no existe {item.get('path')}")
            pages = list((root / "curriculum").glob("level-*/class-*/README.md"))
            if len(pages) != 192:
                errors.append(f"Currículo generado: se esperaban 192 páginas y hay {len(pages)}")

    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            file_part = unquote(target.split("#", 1)[0])
            if file_part and not (path.parent / file_part).resolve().exists():
                errors.append(f"Enlace local roto en {path.relative_to(root)}: {target}")

    html = (root / "site/index.html").read_text(encoding="utf-8")
    for token in ("192", "16", "4", "24", "id=\"decidir\"", "id=\"mapa\"", "app.js", "styles.css"):
        if token not in html:
            errors.append(f"Portal incompleto: falta {token}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDACIÓN FALLIDA")
        for error in errors:
            print(" -", error)
        return 1
    print("OK: 192 clases, 16 asignaturas, 4 niveles y política de licenciamiento validados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
