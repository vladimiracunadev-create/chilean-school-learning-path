"""Check one student-content module in isolation (used while several authors work in parallel).

    python scripts/check_student_module.py student_content_xx_a
    python scripts/check_student_module.py --missing 1-basico/ciencias-naturales

The first form imports only the baseline math modules plus the module under review, so a
half-written module by another author cannot break this check. It reports structural and
arithmetic problems, repeated questions (within the module and against the baseline) and
dominant templates. The second form lists the lessons of a subject that still lack a notebook
in ANY module currently present in scripts/.
"""
from __future__ import annotations

import importlib
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import student_lessons as sl  # noqa: E402
import validate_student_lessons as validator  # noqa: E402

HEADING = re.compile(r"^### Clase (\d+) de (\d+):", re.M)


def baseline_modules() -> list[str]:
    """Fixed reference set: 1.º Matemática (ma01_*) and the first five 2.º modules (ma02_a..e)."""
    return sorted(p.stem for p in HERE.glob("student_content_ma0[12]_?.py") if p.stem[-1] in "abcdef" and not p.stem.startswith("student_content_ma02_f"))


def check_module(name: str) -> list[str]:
    for base in baseline_modules():
        if base != name:
            importlib.import_module(base)
    before = set(sl.REGISTRY)
    importlib.import_module(name)
    mine = sorted(set(sl.REGISTRY) - before)
    if not mine:
        return [f"{name}: no registra ninguna clase"]
    errors: list[str] = []
    seen = {item["q"].strip().lower(): key for key in before for item in sl.all_questions(sl.REGISTRY[key])}
    for oa_code, number in mine:
        content = sl.REGISTRY[(oa_code, number)]
        errors += sl.problems(oa_code, number, content)
        path = validator.curriculum_file(oa_code)
        if path is None:
            errors.append(f"{oa_code}: el OA no existe en el currículo (revisa el código exacto del encabezado)")
            continue
        total = len(HEADING.findall(path.read_text(encoding="utf-8")))
        if not 1 <= number <= total:
            errors.append(f"{oa_code}: la clase {number} no existe (el OA tiene {total})")
        templates = Counter(validator.template(item["q"]) for item in sl.all_questions(content))
        top, count = templates.most_common(1)[0]
        if count / sum(templates.values()) > validator.MAX_TEMPLATE_SHARE:
            errors.append(f"{oa_code} clase {number}: {count} ejercicios comparten la plantilla «{top[:50]}»")
        for item in sl.all_questions(content):
            key = item["q"].strip().lower()
            if key in seen and seen[key] != (oa_code, number):
                other = seen[key]
                same_subject = other[0].split()[0][:2] == oa_code.split()[0][:2]
                if not same_subject:
                    errors.append(f"{oa_code} clase {number}: enunciado idéntico a {other}: {item['q'][:50]}")
            seen[key] = (oa_code, number)
    print(f"{name}: {len(mine)} clases revisadas")
    return errors


def missing(subject_path: str) -> list[str]:
    level, subject = subject_path.split("/")
    sl.load_all()
    gaps = []
    for path in sorted((ROOT / "curriculum" / level / subject).glob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.match(r"# (\S+ OA [A-Z]*\s?\d+) ", text)
        if not match or re.search(r"OA[HA] ", text.split("\n")[0]):
            continue
        code = match.group(1)
        total = len(HEADING.findall(text))
        for number in range(1, total + 1):
            if (code, number) not in sl.REGISTRY:
                gaps.append(f"{code} clase {number} de {total}")
    return gaps


def main(argv: list[str]) -> int:
    if len(argv) == 2 and argv[0] == "--missing":
        gaps = missing(argv[1])
        print("\n".join(gaps) if gaps else "Sin clases pendientes.")
        return 0
    if len(argv) != 1:
        print(__doc__)
        return 2
    errors = check_module(argv[0])
    print("\n".join(errors) if errors else "Sin problemas.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
