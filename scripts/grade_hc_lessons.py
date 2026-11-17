"""Secuencias docentes de los electivos HC de 3.º y 4.º medio (Formación Diferenciada Humanístico-Científica).

Reutiliza el constructor de `grade_three_middle_remaining_lessons` (misma forma de secuencia que la Formación
General) y lo aplica a los 27 electivos. Los OA son compartidos entre 3.º y 4.º medio: el mismo código de OA
produce la misma secuencia en ambos niveles. El enunciado oficial y la URL salen del snapshot verificado; los
temas son una derivación mecánica del verbo y contenido del OA, no una unidad oficial del programa.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import grade_three_middle_remaining_lessons as base

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))

DOMAINS = {
    "geometria-3d": "mathematics", "limites-derivadas-integrales": "mathematics",
    "pensamiento-computacional-programacion": "mathematics", "probabilidades-estadistica-descriptiva-inferencial": "mathematics",
    "lectura-escritura-especializadas": "language", "participacion-argumentacion-democracia": "citizenship",
    "taller-literatura": "language",
    "biologia-celular-molecular": "science", "biologia-ecosistemas": "science", "ciencias-salud": "science",
    "fisica": "science", "quimica": "science",
    "comprension-historica-presente": "social", "economia-sociedad": "social",
    "geografia-territorio-desafios-socioambientales": "social",
    "estetica": "philosophy", "filosofia-politica": "philosophy", "seminario-filosofia": "philosophy",
    "artes-visuales-audiovisuales-multimediales": "visual", "diseno-arquitectura": "visual",
    "creacion-composicion-musical": "music", "interpretacion-musical": "music",
    "interpretacion-creacion-danza": "dance", "interpretacion-creacion-teatro": "theater",
    "ciencias-ejercicio-fisico-deportivo": "physical", "expresion-corporal": "dance",
    "promocion-estilos-vida-activos-saludables": "physical",
}
CONTINUITY = {
    "mathematics": "Retoma las herramientas matemáticas de la Formación General y de 2.º medio y las aplica a un campo electivo de mayor profundidad.",
    "language": "Retoma lectura, escritura y discurso de 2.º medio y de la Formación General y profundiza en un campo electivo.",
    "citizenship": "Retoma la formación ciudadana de la Formación General y profundiza en participación, argumentación y deliberación.",
    "science": "Retoma la indagación científica de 2.º medio y de la Formación General y profundiza en un campo electivo.",
    "social": "Retoma el pensamiento histórico, geográfico y económico de la Formación General y profundiza en un campo electivo.",
    "philosophy": "Retoma el trabajo con argumentos de la Formación General y profundiza en un campo filosófico electivo.",
    "visual": "Retoma la creación y apreciación de 2.º medio y de la Formación General y profundiza en un campo artístico electivo.",
    "music": "Retoma la escucha, interpretación y creación de 2.º medio y de la Formación General y profundiza en un campo musical electivo.",
    "dance": "Retoma la expresión corporal de 2.º medio y de la Formación General y profundiza en un campo electivo.",
    "theater": "Retoma las artes escénicas de 2.º medio y de la Formación General y profundiza en un campo electivo.",
    "physical": "Retoma la actividad física y el autocuidado de 2.º medio y de la Formación General y profundiza en un campo electivo.",
}
SUBJECT_PROFILES = {slug: {"domain": d, "continuity": CONTINUITY[d]} for slug, d in DOMAINS.items()}


def _topic(description: str) -> str:
    clean = description.strip().rstrip(".")
    first = re.split(r"[;:]", clean, maxsplit=1)[0]
    if len(first) > 90:
        first = first[:87].rsplit(" ", 1)[0] + "…"
    return first[0].upper() + first[1:]


RECORDS: dict[str, dict] = {}
_counts: dict[str, int] = {}
for _item in CATALOG["classes"]:
    if _item["course_order"] == 13:
        _counts[_item["oa_code"]] = _counts.get(_item["oa_code"], 0) + 1
for _record in SNAPSHOT["records"]:
    if _record["course_order"] != 13:
        continue
    for _objective in _record["objectives"]:
        if _objective["code"] not in _counts:
            continue  # primera pasada: el catálogo aún no incluye los electivos
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
