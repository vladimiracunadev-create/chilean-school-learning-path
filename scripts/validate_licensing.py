from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "LICENSE", "LICENSE-CONTENT.md", "LICENSING.md", "DATA-LICENSE.md",
    "THIRD_PARTY_NOTICES.md", "ASSET_LICENSES.md", "TRADEMARKS.md", "CURRICULUM.md",
    "LEARNING_PATHS.md", "OFFICIAL_REFERENCES.md", "curriculum/catalog.json",
    "site/index.html", "site/styles.css", "site/app.js",
]
SOURCE_REQUIRED = {
    "id", "title", "author_or_owner", "source_url", "resource_type", "license",
    "redistributed", "modified", "commercial_allowed", "status",
}


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

    content_license = (root / "LICENSE-CONTENT.md").read_text(encoding="utf-8")
    for token in ("Trayectoria Escolar Chile", "CC BY-NC-SA 4.0", "chilean-school-learning-path"):
        if token not in content_license:
            errors.append(f"LICENSE-CONTENT.md incompleto: {token}")

    data_license = (root / "DATA-LICENSE.md").read_text(encoding="utf-8")
    for token in ("mineduc-curriculum-snapshot.json", "curriculum/catalog.json", "developed-lessons.json"):
        if token not in data_license:
            errors.append(f"DATA-LICENSE.md no documenta {token}")

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

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDACIÓN FALLIDA")
        for error in errors:
            print(" -", error)
        return 1
    print("OK: política de licenciamiento y registro de fuentes validados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
