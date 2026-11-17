"""Secuencias docentes de las especialidades técnico-profesionales de 3.º y 4.º medio (Formación Diferenciada TP).

Reutiliza el constructor de `grade_three_middle_remaining_lessons` con el dominio «trabajo». Los objetivos de
aprendizaje (perfiles de egreso) salen del snapshot verificado de las Bases Curriculares de Formación
Diferenciada Técnico-Profesional (Decreto Supremo de Educación N.º 452/2013, edición 2016). Los temas son una
derivación mecánica del verbo y contenido del objetivo, no una unidad oficial: las bases no contienen módulos.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

try:
    import grade_three_middle_remaining_lessons as base
except ImportError:  # importado como paquete (tests)
    from scripts import grade_three_middle_remaining_lessons as base

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
TP_ORDERS = {15, 16}

SUBJECT_PROFILES: dict[str, dict] = {}


_CUTS = re.compile(r"[;:]|, | de acuerdo| según| mediante| considerando| aplicando| utilizando| a partir| con el fin| en función| siguiendo| conforme| respetando| teniendo")


def _topic(description: str) -> str:
    clean = description.strip().rstrip(".")
    first = clean
    for match in _CUTS.finditer(clean):
        if match.start() >= 25:
            first = clean[: match.start()]
            break
    if len(first) > 90:
        first = first[:90].rsplit(" ", 1)[0]
    return first[0].upper() + first[1:]


RECORDS: dict[str, dict] = {}
_per_course: dict[tuple[str, int], int] = {}
for _item in CATALOG["classes"]:
    if _item["course_order"] in TP_ORDERS:
        _key = (_item["oa_code"], _item["course_order"])
        _per_course[_key] = _per_course.get(_key, 0) + 1
_counts: dict[str, int] = {}
for (_code, _order), _n in _per_course.items():  # el mismo OA en 3.º y 4.º tiene la misma secuencia
    _counts[_code] = max(_counts.get(_code, 0), _n)
for _record in SNAPSHOT["records"]:
    if _record["course_order"] not in TP_ORDERS:
        continue
    SUBJECT_PROFILES.setdefault(_record["subject_slug"], {
        "domain": "trabajo",
        "continuity": f"Retoma la Formación General y la orientación hacia el trabajo y profundiza en un campo técnico-profesional: {_record['subject']}.",
    })
    for _objective in _record["objectives"]:
        if _objective["code"] not in _counts:
            continue  # primera pasada: el catálogo aún no incluye las especialidades
        RECORDS[_objective["code"]] = {
            "slug": _record["subject_slug"], "subject": _record["subject"], "axis": _objective["axis"],
            "description": _objective["description"], "url": _objective["url"],
            "count": _counts[_objective["code"]], "topic": _topic(_objective["description"]),
        }


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    record = RECORDS[code]
    return base.build_sequence_from_record(code, record, SUBJECT_PROFILES[record["slug"]], "2.º medio")
