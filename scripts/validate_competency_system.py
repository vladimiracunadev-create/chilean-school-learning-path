#!/usr/bin/env python3
"""Validate the longitudinal competency, assessment and evidence layers."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from competency_evidence import EvidenceError, analyze_cycle


ROOT = Path(__file__).resolve().parents[1]
ALIGNMENT_TYPES = {"official", "pedagogical_inference", "project_proposal"}
TASK_TYPES = {
    "multiple_choice",
    "multiple_select",
    "complex_multiple_choice",
    "short_response",
    "developed_response",
    "mathematical_resolution",
    "explanation",
    "argumentation",
    "chart_interpretation",
    "table_interpretation",
    "comparison",
    "synthesis",
    "essay",
    "project",
    "interdisciplinary_problem",
}
REVIEW_STATES = {
    "draft",
    "internal_review",
    "expert_review",
    "piloted",
    "analyzed",
    "validated",
}
REQUIRED_DOMAINS = {
    "reading",
    "mathematics",
    "science",
    "critical-thinking",
    "data-literacy",
    "writing-communication",
    "digital-information",
}


def load_json(relative: str) -> Any:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def unique(values: list[Any], label: str, errors: list[str]) -> set[Any]:
    result = set(values)
    if len(result) != len(values):
        errors.append(f"IDs duplicados en {label}")
    return result


def validate_https(url: str, label: str, errors: list[str]) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.netloc:
        errors.append(f"URL no HTTPS o inválida en {label}: {url}")


def official_oa_codes() -> set[str]:
    snapshot = load_json("sources/mineduc-curriculum-snapshot.json")
    return {
        objective["code"]
        for record in snapshot["records"]
        for objective in record["objectives"]
    }


def validate(root: Path = ROOT) -> list[str]:
    del root  # Paths are intentionally anchored to this repository.
    errors: list[str] = []
    taxonomy = load_json("competencies/taxonomy.v1.json")
    progressions = load_json("competencies/progressions.v1.json")
    frameworks = load_json("competencies/frameworks.v1.json")
    bank = load_json("assessments/item-bank.v1.json")
    oa_codes = official_oa_codes()

    domains = taxonomy.get("domains", [])
    domain_ids = unique([item.get("id") for item in domains], "dominios", errors)
    if domain_ids != REQUIRED_DOMAINS:
        errors.append(
            f"Dominios esperados {sorted(REQUIRED_DOMAINS)}; encontrados {sorted(domain_ids)}"
        )
    skills = taxonomy.get("skills", [])
    skill_ids = unique([item.get("id") for item in skills], "habilidades", errors)
    if len(skill_ids) < 80:
        errors.append("La taxonomía transversal debe declarar al menos 80 habilidades.")
    for skill in skills:
        if skill.get("domain_id") not in domain_ids:
            errors.append(f"Habilidad con dominio inexistente: {skill.get('id')}")
        if not str(skill.get("id", "")).startswith(f"{skill.get('domain_id')}."):
            errors.append(f"ID de habilidad fuera de su namespace: {skill.get('id')}")

    progression_ids = unique(
        [item.get("id") for item in progressions.get("progressions", [])],
        "progresiones",
        errors,
    )
    stage_ids: set[str] = set()
    for progression in progressions.get("progressions", []):
        for skill_id in progression.get("primary_skill_ids", []):
            if skill_id not in skill_ids:
                errors.append(f"Habilidad inexistente en {progression.get('id')}: {skill_id}")
        previous_start = 0
        for stage in progression.get("stages", []):
            stage_id = stage.get("id")
            if stage_id in stage_ids:
                errors.append(f"Etapa duplicada: {stage_id}")
            stage_ids.add(stage_id)
            level_range = stage.get("level_range", [])
            if (
                len(level_range) != 2
                or not all(isinstance(value, int) and 1 <= value <= 12 for value in level_range)
                or level_range[0] > level_range[1]
            ):
                errors.append(f"Rango inválido en {stage_id}: {level_range}")
            elif level_range[0] < previous_start:
                errors.append(f"Progresión no ordenada en {stage_id}")
            else:
                previous_start = level_range[0]
            if not stage.get("observable_indicators"):
                errors.append(f"Etapa sin indicadores observables: {stage_id}")
            for oa_code in stage.get("oa_codes", []):
                if oa_code not in oa_codes:
                    errors.append(f"OA inexistente en {stage_id}: {oa_code}")
    if len(progression_ids) < 6:
        errors.append("Deben existir al menos seis progresiones longitudinales demostrativas.")

    for link in progressions.get("cross_links", []):
        if link.get("from_stage") not in stage_ids or link.get("to_stage") not in stage_ids:
            errors.append(f"Enlace transversal con etapa inexistente: {link}")
    error_patterns = progressions.get("error_patterns", [])
    error_pattern_ids = unique(
        [item.get("id") for item in error_patterns], "patrones de error", errors
    )
    for pattern in error_patterns:
        for skill_id in pattern.get("skill_ids", []):
            if skill_id not in skill_ids:
                errors.append(f"Patrón {pattern.get('id')} usa habilidad inexistente: {skill_id}")
        for oa_code in pattern.get("intervention_oa_codes", []):
            if oa_code not in oa_codes:
                errors.append(f"Intervención {pattern.get('id')} usa OA inexistente: {oa_code}")

    framework_items = frameworks.get("frameworks", [])
    framework_ids = unique(
        [item.get("id") for item in framework_items], "marcos", errors
    )
    required_frameworks = {
        "paes-2027",
        "simce-2026",
        "pisa-2025",
        "timss-2027",
        "pirls-2026",
        "internal-formative-v1",
    }
    if not required_frameworks <= framework_ids:
        errors.append(f"Faltan marcos: {sorted(required_frameworks - framework_ids)}")
    for framework in framework_items:
        validate_https(framework.get("source_url", ""), framework.get("id", "marco"), errors)
        if framework.get("accessed_at") != "2026-10-02":
            errors.append(f"Fecha de consulta inesperada en {framework.get('id')}")
        if not framework.get("limitations"):
            errors.append(f"Marco sin limitaciones explícitas: {framework.get('id')}")
        for link in framework.get("competency_links", []):
            if link.get("skill_id") not in skill_ids:
                errors.append(
                    f"Marco {framework.get('id')} usa habilidad inexistente: {link.get('skill_id')}"
                )
            if link.get("alignment_type") not in ALIGNMENT_TYPES:
                errors.append(f"Tipo de alineamiento inválido en {framework.get('id')}")

    item_ids = unique([item.get("id") for item in bank.get("items", [])], "ítems", errors)
    for item in bank.get("items", []):
        item_id = item.get("id")
        if item.get("task_type") not in TASK_TYPES:
            errors.append(f"Tipo de tarea inválido en {item_id}: {item.get('task_type')}")
        if item.get("review") not in REVIEW_STATES:
            errors.append(f"Estado de revisión inválido en {item_id}: {item.get('review')}")
        if item.get("license") != "CC-BY-NC-SA-4.0":
            errors.append(f"Licencia inesperada en ítem original {item_id}")
        for skill_id in item.get("skill_ids", []) + item.get("prerequisite_skill_ids", []):
            if skill_id not in skill_ids:
                errors.append(f"Ítem {item_id} usa habilidad inexistente: {skill_id}")
        for oa_code in item.get("oa_codes", []):
            if oa_code not in oa_codes:
                errors.append(f"Ítem {item_id} usa OA inexistente: {oa_code}")
        for link in item.get("framework_links", []):
            if link.get("framework_id") not in framework_ids:
                errors.append(f"Ítem {item_id} usa marco inexistente: {link.get('framework_id')}")
            if link.get("alignment_type") not in ALIGNMENT_TYPES:
                errors.append(f"Ítem {item_id} usa alineamiento inválido")
            if link.get("alignment_type") == "official":
                errors.append(f"Ítem original no puede declararse alineamiento oficial: {item_id}")
        options = item.get("options", [])
        if item.get("task_type") in {
            "multiple_choice",
            "multiple_select",
            "complex_multiple_choice",
        }:
            if len(options) < 2 or not any(option.get("correct") for option in options):
                errors.append(f"Ítem cerrado sin opciones válidas: {item_id}")
            for option in options:
                pattern_id = option.get("error_pattern_id")
                if pattern_id and pattern_id not in error_pattern_ids:
                    errors.append(f"Distractor de {item_id} usa patrón inexistente: {pattern_id}")
        rubric_levels = [row.get("level") for row in item.get("scoring", {}).get("rubric", [])]
        if rubric_levels != ["Aún no observable", "En desarrollo", "Logrado", "Profundizado"]:
            errors.append(f"Rúbrica incompleta o desordenada en {item_id}")
    if len(item_ids) < 6:
        errors.append("El banco inicial debe demostrar al menos seis tareas originales.")

    example_paths = sorted((ROOT / "evidence" / "examples").glob("*.json"))
    if not example_paths:
        errors.append("Falta al menos un ciclo de evidencia sintético.")
    for path in example_paths:
        cycle = json.loads(path.read_text(encoding="utf-8"))
        if cycle.get("skill_id") not in skill_ids:
            errors.append(f"Ciclo {path.name} usa habilidad inexistente")
        for record in cycle.get("records", []):
            pattern_id = record.get("error_pattern_id")
            if pattern_id and pattern_id not in error_pattern_ids:
                errors.append(f"Ciclo {path.name} usa patrón inexistente: {pattern_id}")
            for oa_code in record.get("intervention_oa_codes", []):
                if oa_code not in oa_codes:
                    errors.append(f"Ciclo {path.name} usa OA inexistente: {oa_code}")
        try:
            summary = analyze_cycle(cycle)
        except EvidenceError as exc:
            errors.append(f"Ciclo inválido {path.name}: {exc}")
        else:
            if summary.get("status") != "mastery_documented":
                errors.append(
                    f"El ejemplo completo debe cerrar el ciclo sin porcentajes: {path.name}"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emitir resultado estructurado")
    args = parser.parse_args()
    errors = validate()
    result = {
        "valid": not errors,
        "errors": errors,
        "files": {
            "taxonomy": "competencies/taxonomy.v1.json",
            "progressions": "competencies/progressions.v1.json",
            "frameworks": "competencies/frameworks.v1.json",
            "item_bank": "assessments/item-bank.v1.json",
        },
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif errors:
        for error in errors:
            print(f"ERROR: {error}")
    else:
        print("OK: taxonomía, progresiones, marcos, banco y evidencia son coherentes.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
