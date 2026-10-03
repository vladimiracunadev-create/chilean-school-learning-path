#!/usr/bin/env python3
"""Motor descriptivo y determinista para ciclos de evidencia pedagógica.

No calcula porcentajes de dominio, habilidad latente ni puntajes psicométricos.
Resume registros ya observados y exige decisiones profesionales explícitas para
hipótesis, diagnóstico pedagógico y dominio.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


SUCCESS_RESULTS = {"achieved", "deepened"}
DIFFICULTY_RESULTS = {"not_yet_observable", "developing"}
PERFORMANCE_TYPES = {"observation", "practice", "reassessment"}


class EvidenceError(ValueError):
    """Raised when a cycle is internally inconsistent."""


def _record_index(cycle: dict[str, Any]) -> dict[str, dict[str, Any]]:
    records = cycle.get("records", [])
    ids = [record.get("id") for record in records]
    if len(ids) != len(set(ids)):
        raise EvidenceError("Los ID de evidencia deben ser únicos.")
    index = {record["id"]: record for record in records}
    for record in records:
        for reference in record.get("evidence_refs", []):
            if reference not in index:
                raise EvidenceError(
                    f"{record['id']} referencia evidencia inexistente: {reference}"
                )
    return index


def _supported_decision(
    records: list[dict[str, Any]], record_type: str
) -> dict[str, Any] | None:
    matches = [
        record
        for record in records
        if record.get("type") == record_type and record.get("decision") == "supported"
    ]
    return matches[-1] if matches else None


def _pattern_summary(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        pattern_id = record.get("error_pattern_id")
        if (
            record.get("type") in PERFORMANCE_TYPES
            and record.get("result") in DIFFICULTY_RESULTS
            and pattern_id
        ):
            grouped.setdefault(pattern_id, []).append(record)

    patterns = []
    for pattern_id, observations in sorted(grouped.items()):
        item_ids = {record.get("item_id") for record in observations}
        sessions = {record.get("session_id") for record in observations}
        if len(item_ids) >= 2 and len(sessions) >= 2:
            patterns.append(
                {
                    "error_pattern_id": pattern_id,
                    "observation_ids": [record["id"] for record in observations],
                    "distinct_items": len(item_ids),
                    "distinct_sessions": len(sessions),
                }
            )
    return patterns


def _mastery_basis(
    decision: dict[str, Any] | None,
    index: dict[str, dict[str, Any]],
    records: list[dict[str, Any]],
) -> dict[str, Any]:
    if not decision:
        return {"supported": False, "reason": "No existe una decisión profesional de dominio."}

    referenced = [index[ref] for ref in decision.get("evidence_refs", [])]
    successful = [
        record
        for record in referenced
        if record.get("type") in {"practice", "reassessment"}
        and record.get("result") in SUCCESS_RESULTS
    ]
    interventions = [record for record in records if record.get("type") == "intervention"]
    reassessments = [
        record for record in successful if record.get("type") == "reassessment"
    ]
    item_ids = {record.get("item_id") for record in successful}
    contexts = {record.get("context") for record in successful}
    item_types = {record.get("item_type") for record in successful}

    checks = {
        "explicit_professional_decision": bool(decision.get("responsible_role")),
        "intervention_recorded": bool(interventions),
        "three_successful_evidences": len(successful) >= 3,
        "two_reassessments": len(reassessments) >= 2,
        "distinct_items": len(item_ids) >= 3,
        "multiple_contexts": len(contexts) >= 2,
        "multiple_task_types": len(item_types) >= 2,
    }
    supported = all(checks.values())
    return {
        "supported": supported,
        "checks": checks,
        "evidence_ids": [record["id"] for record in successful],
        "reason": (
            "La decisión se apoya en práctica y reevaluaciones con transferencia."
            if supported
            else "La decisión existe, pero todavía no reúne la diversidad mínima declarada."
        ),
    }


def analyze_cycle(cycle: dict[str, Any]) -> dict[str, Any]:
    """Return a transparent, non-psychometric summary of an evidence cycle."""

    if cycle.get("privacy") != "no_personal_data":
        raise EvidenceError("El ciclo debe declarar privacy=no_personal_data.")
    learner_ref = str(cycle.get("learner_ref", ""))
    if not learner_ref.startswith(("SYNTH-", "LOCAL-")):
        raise EvidenceError("learner_ref debe ser sintético o un código local seudonimizado.")

    records = cycle.get("records", [])
    index = _record_index(cycle)
    patterns = _pattern_summary(records)
    hypothesis = _supported_decision(records, "hypothesis")
    diagnosis = _supported_decision(records, "pedagogical_diagnosis")
    mastery = _supported_decision(records, "mastery_decision")
    mastery_basis = _mastery_basis(mastery, index, records)
    interventions = [record for record in records if record.get("type") == "intervention"]
    reassessments = [record for record in records if record.get("type") == "reassessment"]
    reassessment_successes = [
        record for record in reassessments if record.get("result") in SUCCESS_RESULTS
    ]

    if mastery_basis["supported"]:
        status = "mastery_documented"
        next_step = "Transferir a una situación más compleja y continuar monitoreando."
    elif interventions and len(reassessment_successes) >= 2:
        status = "transfer_observed"
        next_step = "Documentar la decisión profesional o ampliar la evidencia si corresponde."
    elif interventions and reassessment_successes:
        status = "improvement_observed"
        next_step = "Reevaluar con otro ítem, formato y contexto para comprobar transferencia."
    elif interventions and reassessments:
        status = "hypothesis_needs_revision"
        next_step = "Revisar la hipótesis, los prerrequisitos y la accesibilidad de la tarea."
    elif interventions:
        status = "reassessment_pending"
        next_step = "Aplicar una situación nueva; no repetir la respuesta practicada."
    elif diagnosis:
        status = "pedagogical_diagnosis_documented"
        next_step = "Seleccionar una intervención enlazada a contenido existente."
    elif hypothesis:
        status = "hypothesis_documented"
        next_step = "Comprobar la hipótesis antes de documentar un diagnóstico pedagógico."
    elif patterns:
        status = "pattern_observed"
        next_step = "Formular y comprobar una hipótesis pedagógica; no etiquetar al estudiante."
    elif records:
        status = "observation_only"
        next_step = "Recoger otra evidencia comparable en una situación distinta."
    else:
        status = "no_evidence"
        next_step = "Definir un indicador observable y recoger la primera evidencia."

    result_counts = Counter(
        record.get("result")
        for record in records
        if record.get("type") in PERFORMANCE_TYPES and record.get("result")
    )
    return {
        "cycle_id": cycle.get("cycle_id"),
        "learner_ref": learner_ref,
        "skill_id": cycle.get("skill_id"),
        "status": status,
        "counts": {
            "records": len(records),
            "observations": sum(record.get("type") == "observation" for record in records),
            "patterns": len(patterns),
            "interventions": len(interventions),
            "reassessments": len(reassessments),
            "results": dict(sorted(result_counts.items())),
        },
        "patterns": patterns,
        "hypothesis_documented": bool(hypothesis),
        "pedagogical_diagnosis_documented": bool(diagnosis),
        "mastery_basis": mastery_basis,
        "next_step": next_step,
        "cautions": [
            "Este resumen no es un puntaje ni una medición psicométrica.",
            "Una observación aislada no constituye patrón, diagnóstico ni dominio.",
            "Las barreras de acceso y la evidencia insuficiente no se cuentan como error conceptual.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cycle", type=Path, help="Ciclo JSON sin datos personales")
    args = parser.parse_args()
    cycle = json.loads(args.cycle.read_text(encoding="utf-8"))
    print(json.dumps(analyze_cycle(cycle), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
