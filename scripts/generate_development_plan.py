"""Generate the auditable level/subject/item development plan."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_school_program import dose  # noqa: E402


def is_integrated(code: str) -> bool:
    return " OAA " in code or " OAH " in code or code.startswith(("de Actitud", "de Habilidad"))


def main() -> None:
    snapshot = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
    plan = json.loads((ROOT / "content/development-plan.json").read_text(encoding="utf-8"))
    catalog = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
    records = [record for record in snapshot["records"] if record["course_order"] in {1, 2, 3, 4, 5, 6, 7, 8}]
    records.sort(key=lambda record: (record["course_order"], plan["subject_order"].index(record["subject"])))
    developed_codes = {item["oa_code"] for item in catalog["classes"] if item["editorial_status"] == "desarrollada"}
    statuses = plan["objective_status"] | {code: "desarrollado" for code in developed_codes}
    labels = {"desarrollado": "Desarrollado", "en_desarrollo": "En desarrollo", "pendiente": "Pendiente"}
    lines = [
        "# Plan maestro de desarrollo y control profesional", "",
        "> [⬅️ Volver al centro documental](README.md) · [Estado editorial](../EDITORIAL_STATUS.md) · [Metodología](../METHODOLOGY.md)", "",
        f"**Nivel activo:** {plan['active_level']} · **Asignatura activa:** {plan['active_subject']} · **Unidad de entrega:** {plan['delivery_unit']}", "",
        "Este documento es la fuente de seguimiento del desarrollo pedagógico. Publicar archivos no cierra el desarrollo interno de una asignatura: deben cumplirse sus gates automatizados y mantenerse separadas la producción interna y la revisión profesional humana.", "",
        "## Flujo sostenido", "",
        "~~~mermaid", "flowchart LR", "    A[Investigar OA e indicadores] --> B[Diseñar progresión]", "    B --> C[Escribir clases]", "    C --> D[Control interno]", "    D --> E[Markdown + HTML]", "    E --> F[CI verde]", "    F --> G[Cerrar desarrollo interno]", "    G --> H[Revisión profesional]", "    H --> I[Declarar revisada]", "~~~", "",
        "## Definición y orden editorial de 1° a 8° básico", "",
        "| Nivel | Orden | Asignatura | OA disciplinares | Clases disciplinares | Habilidades/actitudes a integrar | Estado |", "|---|---:|---|---:|---:|---:|---|",
    ]
    subject_details = []
    level_subject_order = {}
    for record in records:
        core = [item for item in record["objectives"] if not is_integrated(item["code"])]
        integrated = [item for item in record["objectives"] if is_integrated(item["code"])]
        class_count = sum(len(dose(item["description"], record["subject_slug"], item.get("readings", []))) for item in core)
        developed = sum(statuses.get(item["code"]) == "desarrollado" for item in core)
        in_progress = sum(statuses.get(item["code"]) == "en_desarrollo" for item in core)
        if developed == len(core):
            state = "Desarrollo interno completo · revisión humana pendiente"
        else:
            state = "Activa" if record["subject"] == plan["active_subject"] else f"{developed}/{len(core)} OA desarrollados"
        if in_progress and record["subject"] != plan["active_subject"]:
            state += f" · {in_progress} en desarrollo"
        level_subject_order[record["course_order"]] = level_subject_order.get(record["course_order"], 0) + 1
        subject_order = level_subject_order[record["course_order"]]
        lines.append(f"| {record['course']} | {subject_order} | {record['subject']} | {len(core)} | {class_count} | {len(integrated)} | {state} |")
        subject_details.append((record, core, integrated))
    lines += ["", "## Plan por asignatura e ítem", "", "Cada fila corresponde a un ítem curricular real. Las clases indicadas son la dosificación actual; pueden ajustarse con evidencia, pero no desaparecer para inflar el avance.", ""]
    for record, core, integrated in subject_details:
        subject_class_count = sum(len(dose(item["description"], record["subject_slug"], item.get("readings", []))) for item in core)
        lines += [f"### {record['subject']} · {record['course']}", "", "| Ítem | Eje | Clases | Estado | Fuente |", "|---|---|---:|---|---|"]
        for item in core:
            count = len(dose(item["description"], record["subject_slug"], item.get("readings", [])))
            state = labels.get(statuses.get(item["code"], "pendiente"), "Pendiente")
            lines.append(f"| `{item['code']}` | {item['axis']} | {count} | {state} | [Currículum Nacional]({item['url']}) |")
        integrated_rows = [item for item in catalog["classes"] if item["course_order"] == record["course_order"] and item["subject_slug"] == record["subject_slug"] and item["editorial_status"] == "integrada"]
        integrated_experiences = len(integrated_rows) if integrated or integrated_rows else None
        if not integrated:
            integration_note = "**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido."
        elif integrated_experiences is not None:
            integration_note = f"**Integración transversal documentada:** {len(integrated)} ítems de habilidades o actitudes se incorporan en {integrated_experiences} experiencias dentro de las {subject_class_count} clases de contenido; no se contabilizan como clases autónomas."
        else:
            integration_note = f"**Integración transversal pendiente:** {len(integrated)} ítems de habilidades o actitudes. Se mapearán dentro de los OA disciplinares; no se cerrarán como clases autónomas."
        lines += ["", integration_note, ""]
    lines += ["## Controles profesionales", "", "| Control | Estado | Evidencia exigida |", "|---|---|---|"]
    control_names = {"disciplinary": "Disciplinar", "pedagogical": "Pedagógico", "accessibility_and_inclusion": "Accesibilidad e inclusión", "cultural_and_contextual": "Cultural y contextual", "documentary_and_sources": "Documental y fuentes", "rights_and_privacy": "Derechos y privacidad"}
    for key, value in plan["professional_controls"].items():
        evidence = value["evidence"] or "Nombre o rol, fecha, alcance, hallazgos y cierre documentado"
        lines.append(f"| {control_names[key]} | {value['status'].replace('_', ' ')} | {evidence} |")
    lines += ["", "## Gates del desarrollo interno de 1° a 8° básico", "", "Estos controles están cerrados para el alcance desarrollado. La revisión profesional continúa como un estado posterior e independiente.", ""]
    lines += [f"- [x] {gate}" for gate in plan["completion_gates"]]
    lines += ["", "## Regla de comunicación", "", "El avance se informa con OA y clases efectivamente desarrollados. No se usan cantidad de archivos, publicación HTML ni plantillas como sustitutos de contenido terminado. Una asignatura solo aparece como **desarrollo interno completo** cuando todos sus OA disciplinares y sus gates internos están cerrados; solo aparece como **revisada** cuando existe evidencia profesional humana registrada.", ""]
    (ROOT / "docs/PLAN_DESARROLLO.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Plan generado: {sum(len(core) for _, core, _ in subject_details)} OA disciplinares de 1° a 8° básico")


if __name__ == "__main__":
    main()
