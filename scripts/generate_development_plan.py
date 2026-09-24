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
    records = [record for record in snapshot["records"] if record["course_order"] == 1]
    records.sort(key=lambda record: plan["subject_order"].index(record["subject"]))
    statuses = plan["objective_status"]
    labels = {"desarrollado": "Desarrollado", "en_desarrollo": "En desarrollo", "pendiente": "Pendiente"}
    lines = [
        "# Plan maestro de desarrollo y control profesional", "",
        "> [⬅️ Volver al centro documental](README.md) · [Estado editorial](../EDITORIAL_STATUS.md) · [Metodología](../METHODOLOGY.md)", "",
        f"**Nivel activo:** {plan['active_level']} · **Asignatura activa:** {plan['active_subject']} · **Unidad de entrega:** {plan['delivery_unit']}", "",
        "Este documento es la fuente de seguimiento del desarrollo pedagógico. Publicar archivos no cierra una asignatura: deben cumplirse todos los gates y mantenerse separadas la producción interna y la revisión profesional humana.", "",
        "## Flujo sostenido", "",
        "~~~mermaid", "flowchart LR", "    A[Investigar OA e indicadores] --> B[Diseñar progresión]", "    B --> C[Escribir clases]", "    C --> D[Control interno]", "    D --> E[Markdown + HTML]", "    E --> F[CI verde]", "    F --> G[Revisión profesional]", "    G --> H[Cerrar asignatura]", "~~~", "",
        "## Orden de resolución de 1° básico", "",
        "| Orden | Asignatura | OA disciplinares | Clases disciplinares | Habilidades/actitudes a integrar | Estado |", "|---:|---|---:|---:|---:|---|",
    ]
    subject_details = []
    for order, record in enumerate(records, 1):
        core = [item for item in record["objectives"] if not is_integrated(item["code"])]
        integrated = [item for item in record["objectives"] if is_integrated(item["code"])]
        class_count = sum(len(dose(item["description"], record["subject_slug"], item.get("readings", []))) for item in core)
        developed = sum(statuses.get(item["code"]) == "desarrollado" for item in core)
        in_progress = sum(statuses.get(item["code"]) == "en_desarrollo" for item in core)
        if developed == len(core) and record["subject"] == "Matemática":
            state = "Desarrollo interno completo · revisión humana pendiente"
        else:
            state = "Activa" if record["subject"] == plan["active_subject"] else f"{developed}/{len(core)} OA desarrollados"
        if in_progress and record["subject"] != plan["active_subject"]:
            state += f" · {in_progress} en desarrollo"
        lines.append(f"| {order} | {record['subject']} | {len(core)} | {class_count} | {len(integrated)} | {state} |")
        subject_details.append((record, core, integrated))
    lines += ["", "## Plan por asignatura e ítem", "", "Cada fila corresponde a un ítem curricular real. Las clases indicadas son la dosificación actual; pueden ajustarse con evidencia, pero no desaparecer para inflar el avance.", ""]
    for record, core, integrated in subject_details:
        lines += [f"### {record['subject']}", "", "| Ítem | Eje | Clases | Estado | Fuente |", "|---|---|---:|---|---|"]
        for item in core:
            count = len(dose(item["description"], record["subject_slug"], item.get("readings", [])))
            state = labels.get(statuses.get(item["code"], "pendiente"), "Pendiente")
            lines.append(f"| `{item['code']}` | {item['axis']} | {count} | {state} | [Currículum Nacional]({item['url']}) |")
        if record["subject"] == "Matemática":
            integration_note = f"**Integración transversal documentada:** {len(integrated)} ítems de habilidades o actitudes se incorporan en 68 experiencias dentro de las 83 clases de contenido; no se contabilizan como clases autónomas."
        else:
            integration_note = f"**Integración transversal pendiente:** {len(integrated)} ítems de habilidades o actitudes. Se mapearán dentro de los OA disciplinares; no se cerrarán como clases autónomas."
        lines += ["", integration_note, ""]
    lines += ["## Controles profesionales", "", "| Control | Estado | Evidencia exigida |", "|---|---|---|"]
    control_names = {"disciplinary": "Disciplinar", "pedagogical": "Pedagógico", "accessibility_and_inclusion": "Accesibilidad e inclusión", "cultural_and_contextual": "Cultural y contextual", "documentary_and_sources": "Documental y fuentes", "rights_and_privacy": "Derechos y privacidad"}
    for key, value in plan["professional_controls"].items():
        evidence = value["evidence"] or "Nombre o rol, fecha, alcance, hallazgos y cierre documentado"
        lines.append(f"| {control_names[key]} | {value['status'].replace('_', ' ')} | {evidence} |")
    lines += ["", "## Gates para cerrar una asignatura", ""]
    lines += [f"- [ ] {gate}" for gate in plan["completion_gates"]]
    lines += ["", "## Regla de comunicación", "", "El avance se informa con OA y clases efectivamente desarrollados. No se usan cantidad de archivos, publicación HTML ni plantillas como sustitutos de contenido terminado. Una asignatura solo aparece como **completa** cuando todos sus OA disciplinares y todos los gates están cerrados.", ""]
    (ROOT / "docs/PLAN_DESARROLLO.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Plan generado: {sum(len(core) for _, core, _ in subject_details)} OA disciplinares de 1° básico")


if __name__ == "__main__":
    main()
