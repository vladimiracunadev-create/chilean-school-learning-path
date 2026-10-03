#!/usr/bin/env python3
"""Generate the public longitudinal competency views from canonical JSON data."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any

from competency_evidence import analyze_cycle
from evaluation_catalog import INSTRUMENTS, SAMPLE_FORMS, VARIANTS


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site" / "competencias"
EVALUATION_OUTPUT = ROOT / "site" / "evaluaciones"
PUBLIC_URL = (
    "https://vladimiracunadev-create.github.io/"
    "chilean-school-learning-path/competencias/"
)
EVALUATION_PUBLIC_URL = (
    "https://vladimiracunadev-create.github.io/"
    "chilean-school-learning-path/evaluaciones/"
)

FRAMEWORK_INSTRUMENTS = {
    value["framework_id"]: key
    for key, value in INSTRUMENTS.items()
    if value["framework_id"]
}

TASK_TYPE_LABELS = {
    "multiple_choice": "Selección múltiple",
    "complex_multiple_choice": "Selección múltiple compleja",
    "short_response": "Respuesta breve",
    "developed_response": "Respuesta desarrollada",
    "mathematical_resolution": "Resolución matemática",
    "explanation": "Explicación",
    "argumentation": "Argumentación",
    "chart_interpretation": "Interpretación de gráfico",
    "table_interpretation": "Interpretación de tabla",
    "comparison": "Comparación",
    "synthesis": "Síntesis",
    "essay": "Ensayo",
    "project": "Proyecto",
    "interdisciplinary_problem": "Problema interdisciplinario",
}

DIFFICULTY_LABELS = {
    "foundational": "Fundamentos",
    "application": "Aplicación",
    "reasoning": "Razonamiento",
    "transfer": "Transferencia",
    "advanced": "Desempeño avanzado",
}

REVIEW_LABELS = {
    "draft": "Borrador del proyecto",
    "internal_review": "Revisión interna",
    "piloted": "Pilotada",
    "analyzed": "Analizada",
    "revised": "Revisada tras pilotaje",
    "validated": "Validada",
}

ALIGNMENT_LABELS = {
    "official": "Alineamiento oficial declarado",
    "pedagogical_inference": "Correspondencia pedagógica inferida",
    "project_proposal": "Propuesta propia del proyecto",
}

IMPLEMENTATION_AREAS = [
    {
        "title": "Currículo y clases como fuente",
        "state": "Conservado y conectado",
        "purpose": "Mantener los OA y las clases existentes como punto de partida, sin reconstruir un currículo paralelo.",
        "available": "Las rutas abren OA y clases concretas del repositorio y separan la fuente oficial de la elaboración pedagógica propia.",
        "limit": "Las correspondencias con instrumentos externos requieren revisión disciplinar y no son equivalencias oficiales.",
        "path": "docs/COMPETENCY_GAP_REPORT.md",
    },
    {
        "title": "Competencias y progresión longitudinal",
        "state": "Implementación inicial",
        "purpose": "Hacer visible cómo una habilidad se construye, consolida y transfiere entre niveles.",
        "available": "Taxonomía versionada, cinco progresiones demostrativas y rutas PAES que recorren varios niveles.",
        "limit": "No existe todavía un mapeo revisado de todas las habilidades para los 2.823 OA.",
        "path": "docs/COMPETENCY_SYSTEM.md",
    },
    {
        "title": "Instrumentos complementarios",
        "state": "Trece guías docentes",
        "purpose": "Explicar cada instrumento sin confundirlo con el currículo ni con otro instrumento.",
        "available": "Trece documentos individuales con historia, diseño, población, interpretación, límites, fuentes y rutas docentes.",
        "limit": "Los ciclos y temarios deben revisarse cuando las instituciones publiquen nuevas versiones.",
        "path": "docs/evaluaciones/README.md",
    },
    {
        "title": "Tareas, muestras y cobertura",
        "state": "Parcial y explícito",
        "purpose": "Distinguir una muestra breve de un ensayo con cobertura y de una prueba oficial.",
        "available": "Banco inicial y 45 muestras calculables originales con clave, rúbrica y trazabilidad.",
        "limit": "Las muestras breves no son ensayos completos; faltan matrices oficiales exhaustivas y tareas para cada contenido de cada versión.",
        "path": "docs/ENSAYOS_EJEMPLO.md",
    },
    {
        "title": "Evidencia, diagnóstico e intervención",
        "state": "Prototipo determinista",
        "purpose": "Separar observación, patrón, hipótesis, intervención y reevaluación.",
        "available": "Ciclo documentado que reutiliza clases y exige una situación nueva para comprobar transferencia.",
        "limit": "No sustituye juicio profesional, pilotaje ni validación con datos educativos reales.",
        "path": "docs/EVIDENCE_CYCLE.md",
    },
    {
        "title": "Vistas para docente, estudiante y trayectoria",
        "state": "Demostración navegable",
        "purpose": "Explicar qué se aprende, qué evidencia existe, qué practicar y qué sigue sin etiquetar personas.",
        "available": "Vistas públicas sintéticas y perfiles descriptivos sin porcentajes inventados.",
        "limit": "No existe cuenta, persistencia personal ni panel de curso con datos reales.",
        "path": "docs/GUIA_DOCENTE_COMPETENCIAS.md",
    },
    {
        "title": "Adaptación, IA y privacidad",
        "state": "Reglas y resguardos",
        "purpose": "Permitir adaptación futura sin delegar decisiones simples ni medición a una IA.",
        "available": "Reglas deterministas, IA opcional, trazabilidad y prohibición de datos personales en Git.",
        "limit": "No existe tutor adaptativo de producción ni análisis automático de respuestas abiertas.",
        "path": "docs/COMPETENCY_SYSTEM.md",
    },
    {
        "title": "Revisión, pilotaje y psicometría",
        "state": "Límites definidos",
        "purpose": "Evitar que una colección de preguntas se presente como instrumento validado.",
        "available": "Estados separados para borrador, revisión, pilotaje, análisis y validación.",
        "limit": "No hay muestras, IRT, DIF, confiabilidad ni validez empírica; no se simulan.",
        "path": "docs/COMPETENCY_SYSTEM.md",
    },
]

SCORING_NOTES = {
    "paes": "DEMRE transforma respuestas correctas mediante tablas oficiales de cada aplicación y forma, con equiparación entre formas. La escala vigente va de 100 a 1.000 puntos. Una tabla de otro proceso, una muestra del proyecto o una regla de tres no permiten reconstruir el puntaje oficial exacto.",
    "simce": "La Agencia construye resultados con metodología estandarizada y los interpreta junto con Estándares de Aprendizaje y contexto. No corresponde convertir aciertos de una prueba propia en puntaje o nivel SIMCE ni usar un promedio institucional como nota individual.",
    "dia": "La plataforma corrige y reporta según el instrumento y periodo disponibles. Los resultados se usan internamente para diagnóstico, monitoreo y cierre; no son calificaciones y este repositorio no reproduce su algoritmo ni sus instrumentos.",
    "pisa": "La OCDE estima desempeños poblacionales mediante modelos y múltiples formas; los resultados nacionales no son una suma simple de aciertos ni una calificación individual. Una tarea inspirada en PISA sólo puede usar su propia rúbrica visible.",
    "timss": "IEA obtiene escalas comparables mediante diseño muestral, equiparación y modelos estadísticos. Los porcentajes de una tarea de aula no se convierten en puntajes TIMSS ni permiten ubicar a una persona en la escala internacional.",
    "pirls": "IEA reporta escalas y niveles internacionales a partir de un diseño muestral y psicométrico. Una lectura breve del proyecto entrega evidencia por criterio, no un puntaje PIRLS.",
    "erce": "UNESCO/LLECE construye resultados regionales y nacionales con procedimientos técnicos del estudio. Las tareas propias no producen escala ERCE, comparación entre países ni nivel de desempeño oficial.",
    "icils": "IEA reporta alfabetización computacional e informacional mediante escalas del estudio y diseño muestral. Una actividad escolar no reproduce el entorno digital, la equiparación ni el puntaje ICILS.",
    "iccs": "IEA informa conocimientos y razonamiento cívico con escalas del estudio y reporta actitudes por separado. No se puntúa una posición ideológica y una tarea local no se convierte en resultado ICCS.",
    "eces": "El foco es describir sistemas, contextos y experiencias de educación inicial. No corresponde calcular un puntaje escolar de aprendizaje dentro del tramo 1° básico–4° medio.",
    "impulso-lector": "Al corte documental, la primera aplicación 2026 todavía no ha publicado resultados ni una regla definitiva para convertir observaciones en reportes. El proyecto no inventa umbrales de fluidez, escalas o niveles.",
    "estudios-nacionales": "Cada estudio define su propia metodología, unidad de reporte y año. No existe una escala común para lectura, escritura, ciudadanía, inglés y competencias técnico-profesionales, por lo que deben leerse sus informes por separado.",
    "interna": "Las muestras del proyecto suman dos preguntas cerradas de 1 punto y una respuesta desarrollada de 0 a 2: máximo 4 puntos. Esa suma describe sólo la muestra aplicada; no es porcentaje de dominio, nota, percentil ni escala longitudinal.",
}

FIELD_LABELS = {
    "week": "Semana",
    "fountain_a_liters": "Bebedero A (litros)",
    "fountain_b_liters": "Bebedero B (litros)",
}


def load(relative: str) -> Any:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def slug(value: str) -> str:
    """Return a stable, readable URL segment for a public teacher view."""
    return re.sub(r"[^a-z0-9-]+", "-", value.lower().replace(".", "-")).strip("-")


def documentation_html_href(markdown_path: str) -> str:
    """Return the public HTML counterpart for a repository Markdown path."""
    relative = markdown_path.removeprefix("docs/")
    path = Path(relative)
    if path.name.lower() == "readme.md":
        html_path = path.parent / "index.html"
    else:
        html_path = path.with_suffix(".html").with_name(
            path.stem.lower().replace("_", "-") + ".html"
        )
    return "../docs/" + html_path.as_posix()


def teacher_label(value: str, labels: dict[str, str]) -> str:
    return labels.get(value, value.replace("_", " ").replace("-", " ").capitalize())


def skill_names(taxonomy: dict[str, Any]) -> dict[str, str]:
    return {skill["id"]: skill["name"] for skill in taxonomy["skills"]}


def item_url(item: dict[str, Any], prefix: str = "") -> str:
    return f"{prefix}tareas/{slug(item['id'])}.html"


def framework_url(framework_id: str, prefix: str = "") -> str:
    instrument = FRAMEWORK_INSTRUMENTS.get(framework_id)
    if instrument:
        return f"{prefix}../evaluaciones/{instrument}.html"
    return f"{prefix}marcos-evaluacion.html#{esc(framework_id)}"


def first_class_links() -> dict[str, str]:
    catalog = load("curriculum/catalog.json")
    links: dict[str, str] = {}
    for item in catalog["classes"]:
        links.setdefault(item["oa_code"], f"../{item['web_path']}")
    return links


def first_class_sources() -> dict[str, str]:
    catalog = load("curriculum/catalog.json")
    sources: dict[str, str] = {}
    for item in catalog["classes"]:
        sources.setdefault(item["oa_code"], item["path"])
    return sources


def class_references() -> dict[str, dict[str, Any]]:
    """Return the first published class for every OA used as a reference."""
    catalog = load("curriculum/catalog.json")
    references: dict[str, dict[str, Any]] = {}
    for item in catalog["classes"]:
        references.setdefault(item["oa_code"], item)
    return references


def progression_html(
    progression: dict[str, Any],
    links: dict[str, str],
    skill_labels: dict[str, str],
) -> str:
    stages = []
    for index, stage in enumerate(progression["stages"], start=1):
        oa_links = " · ".join(
            f'<a href="{esc(links[code])}">{esc(code)}</a>' for code in stage["oa_codes"]
        )
        indicators = "".join(f"<li>{esc(item)}</li>" for item in stage["observable_indicators"])
        levels = f"{stage['level_range'][0]}–{stage['level_range'][1]}"
        stages.append(
            f'''<article class="competency-stage" id="{esc(stage['id'])}">
              <div class="stage-number">{index:02d}</div>
              <div><p class="eyebrow">Niveles {levels}</p><h3>{esc(stage['descriptor'])}</h3>
              <ul>{indicators}</ul><p class="stage-links"><strong>OA relacionados:</strong> {oa_links}</p></div>
            </article>'''
        )
    skills = " → ".join(
        esc(skill_labels.get(skill, skill)) for skill in progression["primary_skill_ids"]
    )
    return f'''<section class="trajectory-block" id="{esc(progression['id'])}">
      <header><p class="eyebrow">Trayectoria longitudinal</p><h2>{esc(progression['name'])}</h2><p>{skills}</p></header>
      <div class="trajectory-list">{''.join(stages)}</div>
    </section>'''


def framework_card(framework: dict[str, Any]) -> str:
    limitations = "".join(f"<li>{esc(item)}</li>" for item in framework["limitations"])
    instrument = FRAMEWORK_INSTRUMENTS.get(framework["id"], "")
    return f'''<article class="level-card framework-card">
      <div><span>{esc(framework['short_name'])}</span><span>{esc(framework['version'])}</span></div>
      <h2>{esc(framework['name'])}</h2><p>{esc(framework['population'])}</p>
      <details><summary>Alcance y límites</summary><p>{esc(framework['scope'])}</p><ul>{limitations}</ul></details>
      <a href="../evaluaciones/{esc(instrument)}.html">Abrir {esc(framework['short_name'])}: documentos, clases y muestras →</a>
    </article>'''


def item_card(
    item: dict[str, Any],
    skills_by_id: dict[str, str],
    frameworks_by_id: dict[str, str],
) -> str:
    skills = " · ".join(skills_by_id.get(value, value) for value in item["skill_ids"][:3])
    frameworks = " · ".join(
        frameworks_by_id.get(link["framework_id"], link["framework_id"])
        for link in item["framework_links"]
    )
    return f'''<article class="level-card item-card" id="{esc(item['id'])}">
      <div><span>{esc(teacher_label(item['task_type'], TASK_TYPE_LABELS))}</span><span>{esc(teacher_label(item['difficulty'], DIFFICULTY_LABELS))}</span></div>
      <h2>{esc(item['title'])}</h2><p>{esc(item['context'])}</p>
      <p><strong>Habilidades:</strong> {esc(skills)}</p><p><strong>Vista:</strong> {esc(frameworks or 'interna')}</p>
      <p><strong>Estado:</strong> {esc(teacher_label(item['review'], REVIEW_LABELS))} · versión {esc(item['version'])}</p>
      <a href="{esc(item_url(item))}">Abrir tarea completa para docentes →</a>
    </article>'''


def error_row(pattern: dict[str, Any], links: dict[str, str]) -> str:
    interventions = " · ".join(
        f'<a href="{esc(links[code])}">{esc(code)}</a>'
        for code in pattern["intervention_oa_codes"]
    )
    hypotheses = "; ".join(pattern["possible_hypotheses"])
    return f'''<tr><th scope="row">{esc(pattern['name'])}</th><td>{esc(hypotheses)}</td>
      <td>{interventions}</td><td>{esc(pattern['reassessment_rule'])}</td></tr>'''


def page_top(title: str, description: str, back_href: str = "index.html") -> str:
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#071c2c"><meta name="description" content="{esc(description)}">
<link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css">
<title>{esc(title)} | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenido">Saltar al contenido</a>
<header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="{esc(back_href)}">← Volver a competencias</a></header>'''


def page_footer() -> str:
    return '''<footer class="site-footer"><div><strong>Competencias y evidencia</strong><span>Lectura pedagógica para docentes · datos técnicos validados en segundo plano</span></div><div><a href="index.html">Competencias</a><a href="../evaluaciones/index.html">Evaluaciones: PAES y todas las demás</a><a href="banco-tareas.html">Banco de tareas</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''


def stimulus_html(stimulus: dict[str, Any]) -> str:
    parts: list[str] = []
    if stimulus.get("text"):
        parts.append(f'<p class="stimulus-text">{esc(stimulus["text"])}</p>')
    if stimulus.get("brief"):
        parts.append(f'<p class="stimulus-text">{esc(stimulus["brief"])}</p>')
    if stimulus.get("table"):
        rows = stimulus["table"]
        columns = list(rows[0]) if rows else []
        head = "".join(f"<th>{esc(FIELD_LABELS.get(column, column))}</th>" for column in columns)
        body = "".join(
            "<tr>" + "".join(f"<td>{esc(row[column])}</td>" for column in columns) + "</tr>"
            for row in rows
        )
        parts.append(f'<div class="table-scroll"><table class="competency-table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')
    if stimulus.get("constraints"):
        items = "".join(f"<li>{esc(value)}</li>" for value in stimulus["constraints"])
        parts.append(f"<h3>Condiciones de trabajo</h3><ul>{items}</ul>")
    if stimulus.get("note"):
        parts.append(f'<p class="task-note"><strong>Dato importante:</strong> {esc(stimulus["note"])}</p>')
    return "".join(parts)


def options_html(item: dict[str, Any]) -> str:
    if not item.get("options"):
        return ""
    options = "".join(
        f'<li><strong>{esc(option["id"])}.</strong> {esc(option["text"])}</li>'
        for option in item["options"]
    )
    return f'<ol class="task-options">{options}</ol>'


def rubric_html(item: dict[str, Any]) -> str:
    rows = "".join(
        f'<tr><th scope="row">{esc(row["level"])}</th><td>{esc(row["descriptor"])}</td></tr>'
        for row in item["scoring"]["rubric"]
    )
    criteria = "".join(f"<li>{esc(value)}</li>" for value in item["scoring"]["criteria"])
    return f'''<div class="teacher-grid"><section><h3>Qué observar</h3><ul>{criteria}</ul></section><section><h3>Rúbrica descriptiva</h3><div class="table-scroll"><table class="competency-table"><thead><tr><th>Nivel observado</th><th>Descriptor</th></tr></thead><tbody>{rows}</tbody></table></div></section></div>'''


def task_page(
    item: dict[str, Any],
    taxonomy: dict[str, Any],
    frameworks: dict[str, Any],
    links: dict[str, str],
    previous_item: dict[str, Any] | None,
    next_item: dict[str, Any] | None,
) -> str:
    skills_by_id = skill_names(taxonomy)
    frameworks_by_id = {value["id"]: value for value in frameworks["frameworks"]}
    skills = "".join(f"<li>{esc(skills_by_id.get(value, value))}</li>" for value in item["skill_ids"])
    prerequisites = "".join(
        f"<li>{esc(skills_by_id.get(value, value))}</li>" for value in item["prerequisite_skill_ids"]
    )
    oa_links = "".join(
        f'<li><a href="../{esc(links[code])}">{esc(code)} · abrir clase existente</a></li>'
        for code in item["oa_codes"]
    )
    framework_rows = "".join(
        f'''<tr><th scope="row"><a href="../../evaluaciones/{esc(FRAMEWORK_INSTRUMENTS[link['framework_id']])}.html">{esc(frameworks_by_id[link['framework_id']]['short_name'])}</a></th>
        <td>{esc(ALIGNMENT_LABELS[link['alignment_type']])}</td><td>{esc(link['note'])}</td></tr>'''
        for link in item["framework_links"]
    )
    answer = item["answer"] if isinstance(item["answer"], str) else ", ".join(item["answer"])
    previous_link = (
        f'<a class="sequence-link" href="{esc(slug(previous_item["id"]))}.html"><span>← Tarea anterior</span><strong>{esc(previous_item["title"])}</strong></a>'
        if previous_item else "<span></span>"
    )
    next_link = (
        f'<a class="sequence-link" href="{esc(slug(next_item["id"]))}.html"><span>Tarea siguiente →</span><strong>{esc(next_item["title"])}</strong></a>'
        if next_item else "<span></span>"
    )
    top = page_top(
        item["title"],
        f"Tarea original para docentes: {item['title']}",
        "../banco-tareas.html",
    ).replace('href="../icon.svg"', 'href="../../icon.svg"').replace(
        'href="../styles.css"', 'href="../../styles.css"'
    ).replace('class="brand" href="../index.html"', 'class="brand" href="../../index.html"')
    return top + f'''
<main id="contenido" class="level-shell task-detail">
  <nav class="breadcrumbs"><a href="../index.html">Competencias</a><span>/</span><a href="../banco-tareas.html">Banco de tareas</a><span>/</span><span>{esc(item['title'])}</span></nav>
  <header class="task-hero"><div><p class="eyebrow">Tarea original del proyecto · no es un ítem oficial</p><h1>{esc(item['title'])}</h1><p>{esc(item['context'])}</p></div><aside><span>{esc(teacher_label(item['task_type'], TASK_TYPE_LABELS))}</span><strong>{esc(teacher_label(item['difficulty'], DIFFICULTY_LABELS))}</strong><small>Niveles {esc(', '.join(map(str, item['levels'])))} · edades orientativas {esc(item['age_range']['min'])}–{esc(item['age_range']['max'])}</small></aside></header>
  <section class="task-student"><p class="eyebrow">Versión para aplicar</p><h2>Situación</h2>{stimulus_html(item['stimulus'])}<h2>Pregunta o producto esperado</h2><p class="task-prompt">{esc(item['prompt'])}</p>{options_html(item)}</section>
  <section class="task-teacher"><p class="eyebrow">Clave docente</p><h2>Respuesta y razonamiento esperado</h2><div class="teacher-grid"><section><h3>Respuesta</h3><p>{esc(answer)}</p></section><section><h3>Solución explicada</h3><p>{esc(item['worked_solution'])}</p></section></div>{rubric_html(item)}</section>
  <section class="task-teacher"><p class="eyebrow">Conexión con la trayectoria</p><h2>Por qué esta tarea está aquí</h2><div class="teacher-grid"><section><h3>Habilidades observadas</h3><ul>{skills}</ul></section><section><h3>Prerrequisitos que conviene revisar</h3><ul>{prerequisites}</ul></section><section><h3>OA y clases existentes para intervenir</h3><ul>{oa_links}</ul></section></div><h3>Relación con marcos de evaluación</h3><div class="table-scroll"><table class="competency-table"><thead><tr><th>Marco</th><th>Tipo de relación</th><th>Qué significa</th></tr></thead><tbody>{framework_rows}</tbody></table></div></section>
  <section class="task-warning"><strong>Lectura responsable</strong><p>{esc(teacher_label(item['review'], REVIEW_LABELS))}. Esta tarea no predice puntajes, no diagnostica por una respuesta aislada y no posee validación psicométrica. Autoría: {esc(item['authorship'])}; licencia: {esc(item['license'])}; versión {esc(item['version'])}.</p></section>
  <nav class="sequence-nav">{previous_link}{next_link}</nav>
</main>''' + page_footer().replace('href="index.html"', 'href="../index.html"').replace('href="../evaluaciones/index.html"', 'href="../../evaluaciones/index.html"').replace('href="banco-tareas.html"', 'href="../banco-tareas.html"').replace('href="../documentacion.html"', 'href="../../documentacion.html"')


def skills_page(taxonomy: dict[str, Any], progressions: dict[str, Any]) -> str:
    used_by: dict[str, list[dict[str, Any]]] = {}
    for progression in progressions["progressions"]:
        for skill_id in progression["primary_skill_ids"]:
            used_by.setdefault(skill_id, []).append(progression)
    sections = []
    for domain in taxonomy["domains"]:
        rows = []
        for skill in (value for value in taxonomy["skills"] if value["domain_id"] == domain["id"]):
            routes = " · ".join(
                f'<a href="index.html#{esc(route["id"])}">{esc(route["name"])}</a>'
                for route in used_by.get(skill["id"], [])
            ) or "Aún sin trayectoria demostrativa publicada"
            rows.append(f'<tr><th scope="row">{esc(skill["name"])}</th><td>{routes}</td></tr>')
        sections.append(f'''<section class="teacher-section" id="{esc(domain['id'])}"><p class="eyebrow">Dominio transversal</p><h2>{esc(domain['name'])}</h2><p>{esc(domain['description'])}</p><div class="table-scroll"><table class="competency-table"><thead><tr><th>Habilidad en lenguaje docente</th><th>Recorrido longitudinal disponible</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div></section>''')
    return page_top("Habilidades en lenguaje docente", "Taxonomía transversal explicada sin identificadores técnicos") + f'''
<main id="contenido" class="level-shell"><header class="plain-hero"><p class="eyebrow">Guía docente · 7 dominios y {len(taxonomy['skills'])} habilidades</p><h1>Qué habilidades organiza el programa.</h1><p>Esta página traduce la taxonomía técnica a nombres pedagógicos. Los identificadores JSON existen para que el sistema valide relaciones, pero no son la interfaz de lectura.</p></header>{''.join(sections)}</main>''' + page_footer()


def bank_page(
    bank: dict[str, Any], taxonomy: dict[str, Any], frameworks: dict[str, Any]
) -> str:
    skills_by_id = skill_names(taxonomy)
    frameworks_by_id = {value["id"]: value["short_name"] for value in frameworks["frameworks"]}
    cards = "".join(item_card(item, skills_by_id, frameworks_by_id) for item in bank["items"])
    return page_top("Banco de tareas para docentes", "Tareas originales completas, rúbricas y conexiones curriculares") + f'''
<main id="contenido" class="level-shell"><header class="plain-hero"><p class="eyebrow">Banco inicial · {len(bank['items'])} tareas originales</p><h1>Tareas que se pueden leer y aplicar.</h1><p>Cada ficha abre una versión completa: situación, pregunta, respuesta, solución, criterios, rúbrica, OA, prerrequisitos y relación responsable con PAES, SIMCE, PISA, TIMSS, PIRLS o evaluación interna.</p></header><section class="task-warning"><strong>Estado real</strong><p>Es un banco inicial revisado internamente, no un banco exhaustivo, pilotado ni psicométricamente validado. Las tareas son originales y no copian preguntas protegidas.</p></section><section class="level-grid">{cards}</section></main>''' + page_footer()


def frameworks_page(
    registry: dict[str, Any],
    bank: dict[str, Any],
    taxonomy: dict[str, Any],
    links: dict[str, str],
) -> str:
    skills_by_id = skill_names(taxonomy)
    status_rows = []
    sections = []
    for framework in registry["frameworks"]:
        related_items = [
            item for item in bank["items"]
            if any(link["framework_id"] == framework["id"] for link in item["framework_links"])
        ]
        task_count = len(related_items)
        result = (
            f"{len(framework['competency_links'])} correspondencias documentadas y {task_count} "
            f"{'tarea original' if task_count == 1 else 'tareas originales'}"
        )
        status_rows.append(
            f'<tr><th scope="row"><a href="#{esc(framework["id"])}">{esc(framework["short_name"])}</a></th><td>{esc(result)}</td><td>No es currículo, preparación oficial ni equivalencia automática.</td></tr>'
        )
        dimensions = "".join(f"<li>{esc(value)}</li>" for value in framework["official_dimensions"])
        limitations = "".join(f"<li>{esc(value)}</li>" for value in framework["limitations"])
        mapping_rows = "".join(
            f'<tr><th scope="row">{esc(skills_by_id.get(value["skill_id"], value["skill_id"]))}</th><td>{esc(ALIGNMENT_LABELS[value["alignment_type"]])}</td><td>{esc(value["basis"])}</td></tr>'
            for value in framework["competency_links"]
        )
        item_cards = []
        for item in related_items:
            relation = next(
                value for value in item["framework_links"]
                if value["framework_id"] == framework["id"]
            )
            oa_values = " · ".join(
                f'<a href="{esc(links[code])}">{esc(code)}</a>' for code in item["oa_codes"]
            )
            item_cards.append(f'''<article class="framework-task"><h3><a href="{esc(item_url(item))}">{esc(item['title'])}</a></h3><p><strong>Tipo de relación:</strong> {esc(ALIGNMENT_LABELS[relation['alignment_type']])}</p><p>{esc(relation['note'])}</p><p><strong>Regreso al currículo:</strong> {oa_values}</p></article>''')
        tasks = "".join(item_cards) or '<p class="empty-note">Todavía no existe una tarea original publicada para esta vista. La arquitectura está preparada, pero no se presenta como contenido terminado.</p>'
        sections.append(f'''<section class="framework-detail" id="{esc(framework['id'])}"><header><div><p class="eyebrow">{esc(framework['short_name'])} · {esc(framework['version'])}</p><h2>{esc(framework['name'])}</h2></div><span class="status-badge developed">{esc(result)}</span></header><div class="teacher-grid"><section><h3>Qué mide y a quién</h3><p>{esc(framework['population'])}</p><p>{esc(framework['scope'])}</p></section><section><h3>Dimensiones declaradas por el marco</h3><ul>{dimensions}</ul></section><section><h3>Límites que no se deben olvidar</h3><ul>{limitations}</ul></section></div><h3>Qué conexión hizo este proyecto</h3><div class="table-scroll"><table class="competency-table"><thead><tr><th>Habilidad del proyecto</th><th>Clasificación</th><th>Fundamento</th></tr></thead><tbody>{mapping_rows}</tbody></table></div><h3>Tareas originales vinculadas</h3><div class="framework-tasks">{tasks}</div><p class="source-line"><strong>Fuente consultada:</strong> {esc(framework['institution'])}, {esc(framework['document'])}, {esc(framework['year'])}. <a href="{esc(framework['source_url'])}" rel="noopener">Abrir fuente institucional →</a> Consulta registrada: {esc(framework['accessed_at'])}.</p></section>''')
    legend = "".join(
        f'<li><strong>{esc(label)}</strong><span>{esc(registry["alignment_types"][key])}</span></li>'
        for key, label in ALIGNMENT_LABELS.items()
    )
    return page_top("Marcos de evaluación explicados", "Qué se implementó con PAES, SIMCE, PISA, TIMSS y PIRLS") + f'''
<main id="contenido" class="level-shell"><header class="plain-hero"><p class="eyebrow">Arquitectura de evaluación conectada</p><h1>Qué se hizo con PAES y los otros marcos.</h1><p>Se construyeron vistas de evaluación sobre la trayectoria escolar: se registró qué mide cada marco, se relacionaron habilidades con cautela, se crearon tareas originales y se conservó el camino de regreso a OA y clases. No se creó un preuniversitario ni se declaró una equivalencia oficial inexistente.</p></header><section class="task-warning"><strong>En una frase</strong><p>PAES, SIMCE, PISA, TIMSS y PIRLS sirven para mirar competencias construidas durante años; no reemplazan el currículo chileno.</p></section><div class="table-scroll"><table class="competency-table status-table"><thead><tr><th>Marco</th><th>Implementado ahora</th><th>No significa</th></tr></thead><tbody>{''.join(status_rows)}</tbody></table></div><section class="level-contract"><div><p class="eyebrow">Tres rótulos obligatorios</p><h2>No mezclar evidencia con interpretación.</h2></div><ol>{legend}</ol></section>{''.join(sections)}</main>''' + page_footer()


def evaluation_page_top(title: str, description: str, back_href: str = "index.html") -> str:
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#071c2c"><meta name="description" content="{esc(description)}">
<link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css">
<title>{esc(title)} | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenido">Saltar al contenido</a>
<header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Evaluaciones conectadas al currículo</small></span></a><a class="back-link" href="{esc(back_href)}">← Centro de evaluaciones</a></header>'''


def evaluation_footer(prefix: str = "") -> str:
    return f'''<footer class="site-footer"><div><strong>Evaluaciones complementarias</strong><span>Instrumentos explicados · OA y clases de referencia · cobertura sin simulación</span></div><div><a href="{prefix}index.html">Todos los instrumentos</a><a href="{prefix}ensayos.html">Muestras y cobertura</a><a href="{prefix}brechas.html">Brechas</a><a href="{prefix}estado-implementacion.html">Estado de implementación</a><a href="{prefix}../index.html">Portal</a></div></footer></body></html>'''


def variants_for(instrument: str) -> list[dict[str, Any]]:
    return [variant for variant in VARIANTS if variant["instrument"] == instrument]


def reference_cards(oa_codes: list[str], references: dict[str, dict[str, Any]], prefix: str = "../") -> str:
    cards = []
    for code in dict.fromkeys(oa_codes):
        item = references.get(code)
        if not item:
            continue
        cards.append(
            f'''<article class="reference-card"><p class="eyebrow">{esc(item['course'])} · {esc(item['subject'])}</p><h3>{esc(code)}</h3><p>{esc(item['topic'])}</p><small>Clase {item['lesson']} de {item['lesson_count']} · {esc(item['phase'])}</small><a href="{esc(prefix + item['web_path'])}">Abrir esta clase existente →</a></article>'''
        )
    return "".join(cards) or '<p class="empty-note">Este instrumento está fuera del tramo curricular del repositorio o aún no tiene una referencia pedagógica publicada.</p>'


def html_list(values: list[str]) -> str:
    return "".join(f"<li>{esc(value)}</li>" for value in values)


def curriculum_route_card(
    variant: dict[str, Any],
    references: dict[str, dict[str, Any]],
    prefix: str = "../",
    show_exam: bool = True,
) -> str:
    steps = []
    journey = variant.get("journey") or [("Preparar y enseñar", variant["oa_codes"])]
    step_number = 0
    for stage, codes in journey:
        for code in codes:
            item = references.get(code)
            if not item:
                continue
            step_number += 1
            steps.append(
                f'''<li><span>{step_number:02d}</span><div><p class="eyebrow">{esc(stage)}</p><h4>{esc(code)} · {esc(item['topic'])}</h4><p>{esc(item['course'])} · {esc(item['subject'])} · clase {item['lesson']} de {item['lesson_count']}: {esc(item['phase'])}.</p><a href="{esc(prefix + item['web_path'])}">Abrir la clase exacta →</a></div></li>'''
            )
    exam_step = ""
    if show_exam:
        exam_step = f'''<li><span>{step_number + 1:02d}</span><div><p class="eyebrow">Muestra breve · cobertura parcial</p><h4>{esc(variant['name'])}</h4><p>{esc(variant['reassess'])}</p><a href="ensayos/{esc(variant['id'])}.html">Abrir muestra calculable →</a></div></li>'''
    return f'''<article class="curriculum-route"><header><div><p class="eyebrow">{esc(variant['level'])} · {esc(variant['domain'])}</p><h3>{esc(variant['name'])}</h3></div><span>Correspondencia pedagógica inferida</span></header><p class="route-focus"><strong>Contenido y desempeño:</strong> {esc(variant['focus'])}</p><ol>{''.join(steps)}{exam_step}</ol><div class="route-decision"><p><strong>Qué observar:</strong> {esc(variant['observe'])}</p><p><strong>Si aparece dificultad:</strong> {esc(variant['intervene'])}</p></div></article>'''


def instrument_page(
    key: str,
    registry: dict[str, Any],
    bank: dict[str, Any],
    taxonomy: dict[str, Any],
    references: dict[str, dict[str, Any]],
) -> str:
    instrument = INSTRUMENTS[key]
    variants = variants_for(key)
    framework = next(
        (value for value in registry["frameworks"] if value["id"] == instrument["framework_id"]),
        None,
    )
    related_items = []
    if framework:
        related_items = [
            item for item in bank["items"]
            if any(link["framework_id"] == framework["id"] for link in item["framework_links"])
        ]
    oa_codes = [code for variant in variants for code in variant["oa_codes"]]
    oa_codes.extend(code for item in related_items for code in item["oa_codes"])
    documents = "".join(
        f'<li><a href="{esc(url)}" rel="noopener"><strong>{esc(label)}</strong><span>Fuente institucional para definición, historia, diseño o aplicación.</span></a></li>'
        for label, url in instrument["documents"]
    ) or '<li><a href="../docs/evaluacion-formativa.html"><strong>Evaluación formativa del proyecto</strong><span>Fuente canónica interna.</span></a></li><li><a href="../docs/evidence-cycle.html"><strong>Ciclo de evidencia</strong><span>Reglas deterministas del proyecto.</span></a></li>'
    variant_cards = "".join(
        f'''<article class="exam-card"><div><span>{esc(variant['level'])}</span><span>{esc(variant['domain'])}</span></div><h3>{esc(variant['name'])}</h3><p>Muestra breve original con dos preguntas cerradas, una respuesta justificada y cálculo de puntos del proyecto. Cobertura parcial explícita.</p><a href="ensayos/{esc(variant['id'])}.html">Abrir muestra y calcular resultado →</a></article>'''
        for variant in variants
    ) or '<p class="empty-note">No corresponde crear un ensayo escolar porque este estudio está fuera del tramo 1° básico–4° medio.</p>'
    skills_by_id = skill_names(taxonomy)
    if framework:
        mapping_rows = "".join(
            f'<tr><th scope="row">{esc(skills_by_id.get(value["skill_id"], value["skill_id"]))}</th><td>{esc(ALIGNMENT_LABELS[value["alignment_type"]])}</td><td>{esc(value["basis"])}</td></tr>'
            for value in framework["competency_links"]
        )
        mapping = f'''<section class="teacher-section"><p class="eyebrow">Conexión registrada</p><h2>Habilidades relacionadas con cautela.</h2><div class="table-scroll"><table class="competency-table"><thead><tr><th>Habilidad</th><th>Tipo de relación</th><th>Fundamento</th></tr></thead><tbody>{mapping_rows}</tbody></table></div></section>'''
    else:
        mapping = '''<section class="task-warning"><strong>Estado de la conexión</strong><p>El instrumento está explicado y tiene OA de referencia para orientar la lectura docente, pero todavía no posee un mapeo exhaustivo de competencias. Esas referencias son propuestas pedagógicas del proyecto, no equivalencias oficiales.</p></section>'''
    task_cards = "".join(
        f'<article class="framework-task"><h3><a href="../competencias/{esc(item_url(item))}">{esc(item["title"])}</a></h3><p>Tarea completa del banco inicial con solución, rúbrica y regreso a clases.</p></article>'
        for item in related_items
    ) or '<p class="empty-note">No existe todavía una tarea extensa del banco para este instrumento; las muestras breves no sustituyen esa brecha.</p>'
    framework_limits = "".join(f"<li>{esc(value)}</li>" for value in framework["limitations"]) if framework else "<li>No se copian instrumentos ni preguntas oficiales.</li><li>La referencia curricular es pedagógica, no una equivalencia oficial.</li>"
    history = "".join(
        f'''<li><time>{esc(period)}</time><div><h3>{esc(title)}</h3><p>{esc(detail)}</p></div></li>'''
        for period, title, detail in instrument["history"]
    )
    predecessors = "".join(
        f'''<article><span>Antecedente</span><h3>{esc(name)}</h3><p>{esc(relation)}</p></article>'''
        for name, relation in instrument["predecessors"]
    )
    routes = "".join(curriculum_route_card(variant, references) for variant in variants)
    trajectory_note = (
        '''<section class="trajectory-notice"><div><span>Importante</span><h2>PAES se rinde al final; la competencia no comienza en 4° medio.</h2></div><p>Las rutas siguientes muestran antecedentes curriculares desde educación básica, consolidación y transferencia. Son una reconstrucción pedagógica del proyecto. <strong>No significan que cada OA enlazado sea contenido directo del temario PAES vigente:</strong> el temario oficial de cada proceso sigue siendo la fuente para delimitar lo evaluado.</p></section>'''
        if key == "paes" else ""
    )
    quick_facts = "".join(
        f"<div><span>{esc(label)}</span><strong>{esc(value)}</strong></div>"
        for label, value in (
            ("Responsable", instrument["responsible"]),
            ("Inicio", instrument["first_cycle"]),
            ("Periodicidad", instrument["cadence"]),
            ("Cobertura aquí", f"{len(variants)} rutas docentes" if variants else "Explicación sin enlace curricular forzado"),
        )
    )
    return evaluation_page_top(instrument["short_name"], f"Explicación docente de {instrument['short_name']}") + f'''
<main id="contenido" class="level-shell">
  <nav class="breadcrumbs" aria-label="Migas de pan"><a href="index.html">Evaluaciones</a><span>›</span><span>{esc(instrument['short_name'])}</span></nav>
  <header class="evaluation-hero instrument-hero"><div><p class="eyebrow">{esc(instrument['category'])}</p><h1>{esc(instrument['short_name'])}</h1><p>{esc(instrument['name'])}</p><div class="hero-actions"><a class="button primary" href="#que-es">Entender el instrumento</a><a class="button dark-text" href="#rutas">Recorrer la trayectoria</a><a class="button dark-text" href="../docs/evaluaciones/{esc(key)}.html">Leer guía docente completa</a></div></div><aside><span>Estado en este proyecto</span><strong>{esc(instrument['status'])}</strong><small>No es material oficial ni predice resultados.</small></aside></header>
  <nav class="instrument-nav" aria-label="Contenido de la página"><a href="#que-es">Qué es</a><a href="#historia">Historia</a><a href="#diseno">Cómo funciona</a><a href="#resultados">Resultados y límites</a><a href="#rutas">Rutas docentes</a><a href="#fuentes">Fuentes</a><a href="#ensayos">Muestras</a></nav>
  <section class="instrument-facts" aria-label="Datos esenciales">{quick_facts}</section>
{trajectory_note}
  <section class="instrument-definition" id="que-es"><div><p class="eyebrow">Definición completa</p><h2>Qué es y por qué existe.</h2><p class="definition-lead">{esc(instrument['definition'])}</p></div><aside><h3>Problema que intenta resolver</h3><p>{esc(instrument['why_exists'])}</p><h3>Población o unidad observada</h3><p>{esc(instrument['population'])}</p></aside></section>
  <section class="teacher-section history-section" id="historia"><p class="eyebrow">Historia y versiones anteriores</p><h2>No apareció de la nada.</h2><p>La línea de tiempo distingue antecesores, transiciones y forma vigente. Los nombres anteriores no son versiones intercambiables.</p><ol class="instrument-timeline">{history}</ol><div class="predecessor-grid">{predecessors}</div></section>
  <section class="teacher-section" id="diseno"><p class="eyebrow">Diseño del instrumento</p><h2>Cómo funciona y qué observa.</h2><div class="design-grid"><section><h3>Arquitectura</h3><ol>{html_list(instrument['design'])}</ol></section><section><h3>Uso pedagógico responsable</h3><ol>{html_list(instrument['classroom_use'])}</ol></section></div></section>
  <section class="result-boundaries" id="resultados"><div><p class="eyebrow">Lo que sí entrega</p><h2>Resultados que pueden leerse.</h2><ul>{html_list(instrument['reporting'])}</ul></div><div><p class="eyebrow">Lo que no permite concluir</p><h2>Límites explícitos.</h2><ul>{html_list(instrument['boundaries'])}{framework_limits}<li>El resultado de una muestra propia no se transforma en escala oficial.</li></ul></div></section>
  <section class="scoring-explanation"><div><p class="eyebrow">Resultados y puntajes</p><h2>Cómo se calculan —o por qué no corresponde calcularlos aquí.</h2></div><p>{esc(SCORING_NOTES[key])}</p></section>
  {mapping}
  <section class="teacher-section routes-section" id="rutas"><p class="eyebrow">Regreso preciso al programa chileno</p><h2>Qué enseñar antes, qué clase abrir y cómo comprobar.</h2><p>Cada ruta nombra el contenido observable, abre clases que ya existen y termina con una situación nueva. No crea un curso paralelo ni presenta el vínculo como oficial.</p><div class="curriculum-routes">{routes or '<p class="empty-note">Este estudio observa educación parvularia como sistema. No corresponde forzar una ruta a OA escolares de 1° básico a 4° medio.</p>'}</div><details class="all-references"><summary>Ver todas las referencias OA reunidas</summary><div class="reference-grid">{reference_cards(oa_codes, references)}</div></details></section>
  <section class="teacher-section" id="tareas"><p class="eyebrow">Banco de tareas</p><h2>Tareas extensas ya disponibles.</h2><div class="framework-tasks">{task_cards}</div></section>
  <section class="teacher-section coverage-section" id="ensayos"><p class="eyebrow">Versiones, áreas y cobertura</p><h2>Muestras breves con cálculo transparente.</h2><p>Estas piezas explican formato, criterios y cálculo sobre cuatro puntos. <strong>No son ensayos completos</strong>: no cubren todos los contenidos ni reproducen longitud, dificultad, equiparación o escala oficial. La matriz de cada guía identifica la cobertura y la brecha que permanece.</p><div class="exam-grid">{variant_cards}</div></section>
  <section class="teacher-section source-section" id="fuentes"><p class="eyebrow">Trazabilidad documental</p><h2>Fuentes institucionales consultadas.</h2><ul class="official-document-list">{documents}</ul><p class="source-line">Consulta revisada el 3 de octubre de 2026. Cada síntesis anterior debe leerse junto con la fuente del ciclo correspondiente; los enlaces externos conservan sus propios derechos y pueden actualizarse.</p></section>
</main>''' + evaluation_footer()


def exam_page(variant: dict[str, Any], references: dict[str, dict[str, Any]]) -> str:
    instrument = INSTRUMENTS[variant["instrument"]]
    form = SAMPLE_FORMS[variant["form"]]
    questions = []
    answers = []
    for index, question in enumerate(form["questions"], start=1):
        answers.append(question["answer"])
        options = "".join(
            f'<label><input type="radio" name="q{index}" value="{option_index}"> <span>{esc(option)}</span></label>'
            for option_index, option in enumerate(question["options"])
        )
        questions.append(f'''<fieldset><legend>{index}. {esc(question['prompt'])}</legend><div class="exam-options">{options}</div></fieldset>''')
    rubric = "".join(f"<li>{esc(value)}</li>" for value in form["open_rubric"])
    scoring_note = (
        "DEMRE publica tablas de transformación para cada aplicación y forma. Solo esas tablas oficiales convierten respuestas correctas en puntaje PAES; esta muestra no usa esa escala."
        if variant["instrument"] == "paes"
        else "Este resultado describe únicamente el desempeño en tres tareas originales. No es puntaje oficial, percentil, nivel de logro institucional ni diagnóstico."
    )
    script = f'''<script>(function(){{const form=document.getElementById("exam-form");const result=document.getElementById("exam-result");const answers={json.dumps(answers)};form.addEventListener("submit",function(event){{event.preventDefault();let points=0;answers.forEach(function(answer,index){{const chosen=form.querySelector('input[name="q'+(index+1)+'"]:checked');if(chosen&&Number(chosen.value)===answer)points+=1;}});points+=Number(document.getElementById("open-score").value||0);let label="Sin evidencia suficiente: revisar el punto de partida.";if(points>=1&&points<=2)label="Evidencia inicial: retroalimentar y probar otra situación.";if(points===3)label="Evidencia consistente en esta muestra: consolidar con otro contexto.";if(points===4)label="Evidencia sólida en esta muestra: comprobar transferencia.";result.hidden=false;result.innerHTML='<strong>'+points+' de 4 puntos del proyecto</strong><span>'+label+'</span><small>No es un puntaje oficial de {esc(instrument['short_name'])}.</small>';result.focus();}});form.addEventListener("reset",function(){{result.hidden=true;}});}})();</script>'''
    top = evaluation_page_top(
        f"{instrument['short_name']} · {variant['name']}",
        f"Muestra breve original de referencia para {variant['name']}",
        f"../{variant['instrument']}.html",
    ).replace('href="../icon.svg"', 'href="../../icon.svg"').replace(
        'href="../styles.css"', 'href="../../styles.css"'
    ).replace('class="brand" href="../index.html"', 'class="brand" href="../../index.html"')
    return top + f'''
<main id="contenido" class="level-shell exam-detail">
  <nav class="breadcrumbs" aria-label="Migas de pan"><a href="../index.html">Evaluaciones</a><span>›</span><a href="../{esc(variant['instrument'])}.html">{esc(instrument['short_name'])}</a><span>›</span><span>{esc(variant['name'])}</span></nav>
  <header class="task-hero"><div><p class="eyebrow">Muestra breve original · cobertura parcial · no oficial</p><h1>{esc(variant['name'])}</h1><p>{esc(form['title'])}</p></div><aside><span>{esc(variant['level'])}</span><strong>{esc(variant['domain'])}</strong><small>2 preguntas cerradas + 1 respuesta justificada · máximo 4 puntos</small></aside></header>
  <section class="coverage-disclosure"><strong>Esto no es un ensayo completo</strong><p>La muestra no cubre todos los contenidos del instrumento. Sirve para ver una situación, la clave, la rúbrica y el cálculo. Consulta la matriz de cobertura en la guía del instrumento antes de decidir qué falta evaluar.</p><a href="../../docs/evaluaciones/{esc(variant['instrument'])}.html">Abrir matriz y guía docente →</a></section>
  <section class="task-warning"><strong>Cómo leer el resultado</strong><p>{esc(scoring_note)}</p></section>
  <section class="exam-purpose"><div><p class="eyebrow">Antes de aplicar</p><h2>Contenido y desempeño que se observará.</h2><p>{esc(variant['focus'])}</p></div><div><h3>Decisión acordada de antemano</h3><p>Esta muestra sirve para producir una observación breve. Si aparece dificultad, no se repite mecánicamente: se identifica el proceso implicado, se abre la clase correspondiente y se recoge otra evidencia.</p></div></section>
  <form id="exam-form" class="sample-exam"><section class="task-student"><p class="eyebrow">Situación original</p><h2>Lee, resuelve y justifica.</h2><p class="stimulus-text">{esc(form['stimulus'])}</p>{''.join(questions)}<fieldset><legend>3. {esc(form['open_prompt'])}</legend><textarea aria-label="Respuesta desarrollada" rows="6" placeholder="Escribe aquí tu respuesta y evidencia..."></textarea><label class="self-score" for="open-score">Puntaje de la respuesta abierta según la rúbrica</label><select id="open-score"><option value="0">0 puntos</option><option value="1">1 punto</option><option value="2">2 puntos</option></select></fieldset><div class="exam-actions"><button class="button primary" type="submit">Calcular puntos de la muestra</button><button class="button dark-text" type="reset">Limpiar respuestas</button></div><output id="exam-result" class="exam-result" tabindex="-1" hidden></output></section></form>
  <section class="task-teacher"><p class="eyebrow">Clave docente</p><h2>Corrección transparente.</h2><div class="teacher-grid"><section><h3>Preguntas cerradas</h3><ol>{''.join(f'<li>Alternativa {chr(65 + answer)}</li>' for answer in answers)}</ol></section><section><h3>Rúbrica de la respuesta abierta</h3><ul>{rubric}</ul></section><section><h3>Qué observar</h3><p>{esc(variant['observe'])}</p></section></div></section>
  <section class="teacher-section"><p class="eyebrow">Conexión curricular de referencia</p><h2>Ruta de intervención con clases existentes.</h2><div class="curriculum-routes">{curriculum_route_card(variant, references, '../../', False)}</div><div class="reassessment-panel"><div><h3>Si aparece dificultad</h3><p>{esc(variant['intervene'])}</p></div><div><h3>Cómo reevaluar</h3><p>{esc(variant['reassess'])}</p></div></div></section>
</main>{script}''' + evaluation_footer("../")


def evaluation_hub(registry: dict[str, Any]) -> str:
    modeled = sum(1 for value in INSTRUMENTS.values() if value["framework_id"])
    instrument_cards = "".join(
        f'''<article class="evaluation-card"><div><span>{esc(value['category'])}</span><span>{len(variants_for(key))} rutas</span></div><h2>{esc(value['short_name'])}</h2><h3>{esc(value['name'])}</h3><p>{esc(value['definition'])}</p><dl><div><dt>Inicio</dt><dd>{esc(value['first_cycle'])}</dd></div><div><dt>Periodicidad</dt><dd>{esc(value['cadence'])}</dd></div></dl><strong>{esc(value['status'])}</strong><a href="{esc(key)}.html">Abrir historia, diseño, límites, clases y muestras →</a></article>'''
        for key, value in INSTRUMENTS.items()
    )
    reading_links = "".join(
        f'<a href="{key}.html"><strong>{esc(INSTRUMENTS[key]["short_name"])}</strong><span>{esc(label)}</span></a>'
        for key, label in (
            ("impulso-lector", "Precursores, comprensión y fluidez en 2° básico desde 2026"),
            ("estudios-nacionales", "Lectura inicial y otros estudios muestrales por área"),
            ("paes", "Competencia Lectora al final de la trayectoria"),
            ("simce", "Lectura en 4°, 6° básico y II medio en 2026"),
            ("dia", "Lectura para diagnóstico, monitoreo y cierre"),
            ("pisa", "Lectura aplicada alrededor de los 15 años"),
            ("pirls", "Comprensión literaria e informativa alrededor de 4° básico"),
            ("erce", "Lectura y escritura en 3° y 6° básico"),
        )
    )
    return evaluation_page_top("Centro de evaluaciones", "PAES, SIMCE, DIA y estudios internacionales conectados a clases") + f'''
<main id="contenido" class="level-shell">
  <header class="evaluation-hero evaluation-hub-hero"><div><p class="eyebrow">Entrada directa para docentes</p><h1>Evaluaciones complementarias.</h1><p>No necesitas adivinar una ruta: selecciona el instrumento por su nombre. Cada página explica definición, origen, instrumentos anteriores, razón de existir, diseño, resultados, límites y uso pedagógico; después enlaza OA y clases precisas del programa.</p><div class="hero-actions"><a class="button primary" href="#instrumentos">Elegir instrumento</a><a class="button dark-text" href="ensayos.html">Ver muestras y cobertura</a><a class="button dark-text" href="estado-implementacion.html">Ver estado de implementación</a></div></div><aside><span>Panorama visible</span><strong>{len(INSTRUMENTS)} instrumentos o estudios</strong><small>{len(VARIANTS)} muestras breves · {modeled} marcos con mapeo de competencias</small></aside></header>
  <section class="task-warning"><strong>La ruta correcta</strong><p>Currículo chileno → OA → clase existente → habilidad → instrumento complementario → tarea o muestra → evidencia → intervención → reevaluación. Ninguna prueba externa reemplaza el currículo.</p></section>
  <section class="teacher-section reading-route"><p class="eyebrow">Comprensión lectora</p><h2>Todas las entradas lectoras, en un solo lugar.</h2><p>No son equivalentes: cambian población, propósito y diseño. Se reúnen aquí para que puedas comparar sin duplicar un curso de lectura.</p><div class="reading-link-grid">{reading_links}</div></section>
  <section id="instrumentos"><div class="level-intro"><div><p class="eyebrow">Nacionales, de acceso e internacionales</p><h2>Selecciona por nombre.</h2></div><p>Los estados distinguen lo que ya posee mapeo y tareas de lo que solo está explicado y conectado como referencia.</p></div><div class="evaluation-grid">{instrument_cards}</div></section>
  <section class="implementation-summary"><div><p class="eyebrow">Antes de implementar</p><h2>Informe de brechas histórico.</h2><p>Conserva la fotografía del repositorio antes de crear la capa longitudinal. No se reescribe para aparentar que lo nuevo ya existía.</p><a href="../docs/competency-gap-report.html">Leer informe previo →</a></div><div><p class="eyebrow">Después de implementar</p><h2>Qué se cerró y qué sigue parcial.</h2><p>La comparación actual muestra rutas, muestras, mapeos y límites pendientes con enlaces directos.</p><a href="brechas.html">Comparar brecha por brecha →</a></div></section>
  <section class="level-contract"><div><p class="eyebrow">Puntajes responsables</p><h2>Calcular sin inventar.</h2></div><ol><li><strong>Puntos del proyecto</strong><span>Cada muestra informa 0 a 4 puntos con una rúbrica visible.</span></li><li><strong>Escala oficial</strong><span>Solo la institución responsable puede publicar conversiones y niveles oficiales.</span></li><li><strong>Sin diagnóstico automático</strong><span>Una aplicación breve produce observaciones, no etiquetas.</span></li><li><strong>Cobertura explícita</strong><span>Ninguna muestra parcial se presenta como ensayo completo.</span></li></ol></section>
</main>''' + evaluation_footer()


def exams_index_page() -> str:
    groups = []
    for key, instrument in INSTRUMENTS.items():
        variants = variants_for(key)
        if not variants:
            continue
        cards = "".join(
            f'<a class="exam-index-link" href="ensayos/{esc(variant["id"])}.html"><span>{esc(variant["level"])}</span><strong>{esc(variant["name"])}</strong><small>{esc(variant["domain"])} · 4 puntos del proyecto</small></a>'
            for variant in variants
        )
        groups.append(f'<section class="teacher-section"><p class="eyebrow">{esc(instrument["category"])}</p><h2><a href="{esc(key)}.html">{esc(instrument["short_name"])}</a></h2><div class="exam-index-grid">{cards}</div></section>')
    return evaluation_page_top("Muestras y cobertura", "Muestras originales calculables y estado real de cobertura") + f'''
<main id="contenido" class="level-shell"><header class="plain-hero"><p class="eyebrow">{len(VARIANTS)} variantes visibles · cobertura parcial</p><h1>Muestras calculables, no ensayos completos.</h1><p>Cada versión incluye situación, preguntas, clave, rúbrica, cálculo de puntos y regreso a OA y clases. No cubre todos los contenidos, no es un facsímil y no predice puntajes oficiales.</p></header><section class="coverage-disclosure"><strong>Qué falta para llamarlas ensayos</strong><p>Una matriz vigente de contenidos y al menos una tarea verificable por cada eje. Hasta entonces, el sitio las presenta con el nombre que corresponde: muestras breves.</p></section><section class="task-warning"><strong>Resultado que sí se calcula</strong><p>El sitio calcula de 0 a 4 puntos de la muestra. PAES, SIMCE, PISA, TIMSS, PIRLS y otros organismos usan diseños, equiparaciones y escalas que no se pueden reconstruir con tareas propias.</p></section>{''.join(groups)}</main>''' + evaluation_footer()


CURRENT_GAP_ROWS = [
    ("Comprensión lectora", "EXISTE Y SE CONECTÓ", "PAES, SIMCE, DIA, PISA, PIRLS y ERCE tienen entradas visibles, variantes, OA y clases de referencia.", "Conservar los OA; ampliar revisión y pilotaje."),
    ("Evaluación formativa", "EXISTE Y SE AMPLIÓ", "Ciclo de evidencia, banco, muestras, intervención y reevaluación enlazados.", "Pilotar y registrar revisión humana."),
    ("Competencias", "EXISTE PARCIALMENTE", "86 habilidades en 7 dominios y cinco progresiones demostrativas.", "Mapear de manera revisada el resto de los 2.823 OA."),
    ("Diagnóstico", "PROTOTIPO DISPONIBLE", "Estados separados y DIA explicado como instrumento externo de referencia.", "Crear una aplicación local autorizada antes de usar datos reales."),
    ("Banco de ítems", "EXISTE PARCIALMENTE", "6 tareas extensas y 45 muestras breves para las variantes documentadas.", "Construir matrices completas, ampliar, revisar por disciplina y pilotar."),
    ("PAES", "EXISTE PARCIALMENTE", "Página propia, 5 áreas, documentos, trayectoria multinivel, una tarea extensa y muestras breves.", "Falta cubrir todos los contenidos de cada temario; no existe banco oficial, predictor ni conversión propia."),
    ("SIMCE", "EXISTE PARCIALMENTE", "Página propia, 6 variantes 2026, documentos, OA, clases, una tarea extensa y muestras breves.", "No reproduce ítems ni niveles de logro oficiales; falta cobertura completa."),
    ("PISA", "EXISTE PARCIALMENTE", "Página propia, 4 dominios, documentos, OA, clases, dos tareas extensas y muestras breves.", "No reproduce unidades PISA ni resultados de sistema; falta cobertura completa."),
    ("TIMSS", "EXISTE PARCIALMENTE", "Página propia, 4 combinaciones de grado/área, documentos, OA, clases, tareas y muestras breves.", "Las referencias de grado no son equivalencias administrativas chilenas; falta cobertura completa."),
    ("PIRLS", "EXISTE PARCIALMENTE", "Página propia, 2 propósitos lectores, documentos, OA, clases, tarea y muestras breves.", "No crea otro curso de comprensión lectora; falta cobertura completa."),
    ("Impulso Lector", "EXISTE Y SE CONECTÓ", "Página propia para la evaluación censal 2026 de 2° básico: precursores, comprensión y fluidez, diferenciada de SIMCE y DIA.", "Actualizar reportes, escala y continuidad sólo cuando la Agencia publique la aplicación y sus resultados."),
    ("Estudios nacionales", "EXISTEN Y SE CONECTARON PARCIALMENTE", "Familia muestral explicada con rutas para Lectura 2°, Escritura 6°, Formación Ciudadana 8°, Inglés y competencias TP.", "Verificar cada ciclo en el plan vigente y ampliar sólo con marcos oficiales."),
    ("Otros instrumentos", "EXPLICADOS Y PARCIALMENTE CONECTADOS", "DIA, ERCE, ICILS e ICCS aparecen con historia y rutas; ECES queda explicado sin forzar OA escolares.", "Completar mapeos solo con revisión disciplinar."),
    ("Progresión longitudinal", "EXISTE PARCIALMENTE", "Cinco progresiones y regreso verificable a clases.", "Extender sin convertir rangos etarios en reglas rígidas."),
    ("Análisis de errores", "EXISTE Y SE AMPLIÓ", "Patrones, hipótesis prudentes e intervención enlazada.", "Reunir evidencia de aula antes de generalizar."),
    ("Adaptación", "ARQUITECTURA PREPARADA", "Reglas deterministas descritas.", "No existe todavía tutor adaptativo de producción."),
]


def gaps_page() -> str:
    rows = "".join(f'<tr><th scope="row">{esc(name)}</th><td>{esc(status)}</td><td>{esc(evidence)}</td><td>{esc(action)}</td></tr>' for name, status, evidence, action in CURRENT_GAP_ROWS)
    return evaluation_page_top("Brechas antes y después", "Comparación entre la auditoría previa y el estado actual") + f'''
<main id="contenido" class="level-shell"><header class="plain-hero"><p class="eyebrow">Trazabilidad de implementación</p><h1>Brechas antes y después.</h1><p>El informe previo del 2 de octubre de 2026 se conserva como registro histórico. Esta vista no lo reemplaza: muestra qué cambió después y qué sigue incompleto.</p></header><section class="implementation-summary"><div><p class="eyebrow">Línea base histórica</p><h2>Antes de programar.</h2><p>Registró que PAES, SIMCE, PISA, TIMSS, PIRLS y el banco no existían como capa estructurada.</p><a href="../docs/competency-gap-report.html">Abrir informe previo completo →</a></div><div><p class="eyebrow">Estado actual</p><h2>Después de implementar.</h2><p>La existencia de páginas o código no equivale a cobertura exhaustiva, revisión humana o validación psicométrica.</p><a href="estado-implementacion.html">Ver capacidades y límites →</a></div></section><div class="table-scroll"><table class="competency-table gap-table"><thead><tr><th>Elemento</th><th>Estado actual</th><th>Evidencia disponible</th><th>Acción pendiente</th></tr></thead><tbody>{rows}</tbody></table></div></main>''' + evaluation_footer()


def implementation_status_page() -> str:
    cards = "".join(
        f'''<article class="implementation-area-card"><header><div><p class="eyebrow">Capacidad pedagógica</p><h2>{esc(item['title'])}</h2></div><strong class="status-pill">{esc(item['state'])}</strong></header><p class="area-purpose">{esc(item['purpose'])}</p><div class="status-explanation"><section><h3>Qué se puede usar hoy</h3><p>{esc(item['available'])}</p><a href="{esc(documentation_html_href(item['path']))}">Abrir evidencia HTML →</a></section><section><h3>Límite o trabajo pendiente</h3><p>{esc(item['limit'])}</p></section></div></article>'''
        for item in IMPLEMENTATION_AREAS
    )
    return evaluation_page_top("Estado de implementación pedagógica", "Capacidades disponibles, límites y próximos pasos") + f'''
<main id="contenido" class="level-shell"><header class="plain-hero implementation-hero"><p class="eyebrow">Cobertura y límites del sistema</p><h1>Qué puede usar un docente y qué sigue pendiente.</h1><p>Esta página está organizada por capacidades educativas reales. No reproduce instrucciones de desarrollo ni presenta una lista técnica como si fuera contenido pedagógico.</p></header><section class="implementation-summary-strip" aria-label="Resumen"><div><strong>{len(IMPLEMENTATION_AREAS)}</strong><span>áreas explicadas</span></div><div><strong>{len(INSTRUMENTS)}</strong><span>guías de instrumentos</span></div><div><strong>{len(VARIANTS)}</strong><span>muestras breves</span></div><div><strong>0</strong><span>ensayos completos declarados</span></div></section><section class="coverage-disclosure"><strong>Por qué aparece cero en ensayos completos</strong><p>Una muestra de tres tareas no cubre un instrumento. El proyecto conserva esas piezas como ejemplos calculables, pero sólo declarará un ensayo completo cuando exista una matriz vigente y una tarea para todos sus contenidos.</p></section><div class="implementation-area-list">{cards}</div><section class="task-warning"><strong>Límite central</strong><p>La capa es navegable, pero todavía no posee revisión disciplinar completa, pilotaje amplio, datos reales de estudiantes ni validez psicométrica.</p></section></main>''' + evaluation_footer()


def md_escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def teacher_guide_markdown(
    taxonomy: dict[str, Any], progressions: dict[str, Any], bank: dict[str, Any]
) -> str:
    domain_rows = "\n".join(
        f"| {domain['name']} | {sum(skill['domain_id'] == domain['id'] for skill in taxonomy['skills'])} | {domain['description']} |"
        for domain in taxonomy["domains"]
    )
    progression_rows = "\n".join(
        f"| [{progression['name']}](COMPETENCY_SYSTEM.md) | {len(progression['stages'])} | {len({code for stage in progression['stages'] for code in stage['oa_codes']})} |"
        for progression in progressions["progressions"]
    )
    return f'''# Guía docente de competencias, diagnóstico y progreso

Esta es la entrada pedagógica a la capa longitudinal. Los archivos JSON sostienen la validación automática, pero **no son la lectura esperada para docentes**.

[Sistema longitudinal](COMPETENCY_SYSTEM.md) · [Marcos de evaluación](ASSESSMENT_FRAMEWORKS.md) · [Banco de tareas completo](BANCO_TAREAS.md) · [Ciclo de evidencia](EVIDENCE_CYCLE.md)

## Qué existe hoy

| Componente | Resultado disponible | Cómo usarlo |
|---|---|---|
| Habilidades | {len(taxonomy['skills'])} habilidades en {len(taxonomy['domains'])} dominios | Nombrar qué desempeño se observa sin reemplazar el OA |
| Trayectorias | {len(progressions['progressions'])} recorridos demostrativos | Ver antecedentes, progreso y transferencia entre niveles |
| Marcos | PAES, SIMCE, PISA, TIMSS, PIRLS e interno | Mirar competencias desde una evaluación sin convertirla en currículo |
| Banco | {len(bank['items'])} tareas originales completas | Aplicar, observar, retroalimentar y reevaluar |
| Evidencia | Un ciclo sintético cerrado | Separar observación, patrón, hipótesis, intervención y dominio documentado |

## Qué no existe todavía

- un mapeo exhaustivo de todos los OA a las {len(taxonomy['skills'])} habilidades;
- una plataforma con fichas reales de estudiantes;
- un banco amplio pilotado y validado psicométricamente;
- equivalencias oficiales entre los OA y PAES, SIMCE, PISA, TIMSS o PIRLS;
- un preuniversitario o un predictor de puntajes.

## Los dominios en lenguaje pedagógico

| Dominio | Habilidades | Para qué sirve |
|---|---:|---|
{domain_rows}

## Las trayectorias desarrolladas

| Recorrido | Etapas | OA de referencia distintos |
|---|---:|---:|
{progression_rows}

## Cómo usar la capa durante una clase

1. Comienza en el OA y la clase existente.
2. Selecciona la habilidad que quieres observar.
3. Usa una tarea o evidencia apropiada; una respuesta aislada es sólo una observación.
4. Si aparece un patrón, formula una hipótesis prudente y revisa prerrequisitos.
5. Reutiliza las clases enlazadas para intervenir.
6. Reevalúa con una situación distinta para comprobar transferencia.

## Estado y límites

La taxonomía y sus correspondencias son propuestas del proyecto. Los OA mantienen su texto y fuente oficial. El sistema no produce porcentajes ficticios, diagnósticos clínicos ni resultados psicométricos.
'''


def bank_markdown(
    bank: dict[str, Any],
    taxonomy: dict[str, Any],
    frameworks: dict[str, Any],
    sources: dict[str, str],
) -> str:
    skills_by_id = skill_names(taxonomy)
    frameworks_by_id = {value["id"]: value["short_name"] for value in frameworks["frameworks"]}
    sections = []
    for item in bank["items"]:
        stimulus = item["stimulus"].get("text") or item["stimulus"].get("brief") or ""
        extra = ""
        if item["stimulus"].get("table"):
            rows = item["stimulus"]["table"]
            columns = list(rows[0]) if rows else []
            extra += "\n| " + " | ".join(FIELD_LABELS.get(column, column) for column in columns) + " |\n"
            extra += "|" + "|".join("---" for _ in columns) + "|\n"
            extra += "\n".join("| " + " | ".join(md_escape(row[column]) for column in columns) + " |" for row in rows) + "\n"
        if item["stimulus"].get("constraints"):
            extra += "\n**Condiciones:**\n\n" + "\n".join(f"- {value}" for value in item["stimulus"]["constraints"]) + "\n"
        if item["stimulus"].get("note"):
            extra += f"\n> **Dato importante:** {item['stimulus']['note']}\n"
        options = ""
        if item.get("options"):
            options = "\n" + "\n".join(f"- **{option['id']}.** {option['text']}" for option in item["options"]) + "\n"
        answer = item["answer"] if isinstance(item["answer"], str) else ", ".join(item["answer"])
        rubric = "\n".join(
            f"| {md_escape(row['level'])} | {md_escape(row['descriptor'])} |"
            for row in item["scoring"]["rubric"]
        )
        oa_links = " · ".join(f"[{code}](../{sources[code]})" for code in item["oa_codes"])
        framework_links = " · ".join(
            f"{frameworks_by_id[link['framework_id']]} — {ALIGNMENT_LABELS[link['alignment_type']]}"
            for link in item["framework_links"]
        )
        sections.append(f'''## {item['title']}

**Uso orientativo:** niveles {', '.join(map(str, item['levels']))}; {teacher_label(item['task_type'], TASK_TYPE_LABELS)}; {teacher_label(item['difficulty'], DIFFICULTY_LABELS)}.

**Asignaturas:** {', '.join(item['subject_domains'])}.

**Estado:** {teacher_label(item['review'], REVIEW_LABELS)}, versión {item['version']}.

### Situación

{stimulus}
{extra}
### Pregunta o producto esperado

{item['prompt']}
{options}
### Clave docente

**Respuesta:** {answer}

**Solución explicada:** {item['worked_solution']}

### Qué observar

{chr(10).join(f'- {criterion}' for criterion in item['scoring']['criteria'])}

| Nivel observado | Descriptor |
|---|---|
{rubric}

### Conexión con la trayectoria

- **Habilidades:** {', '.join(skills_by_id.get(value, value) for value in item['skill_ids'])}.
- **Prerrequisitos:** {', '.join(skills_by_id.get(value, value) for value in item['prerequisite_skill_ids'])}.
- **OA y clases existentes:** {oa_links}.
- **Marcos:** {framework_links}.

Esta tarea es original del proyecto. No es un ítem oficial ni predice puntaje.
''')
    return f'''# Banco inicial de tareas para docentes

Este documento presenta las {len(bank['items'])} tareas completas sin exigir la lectura de archivos JSON. Incluye estímulo, consigna, clave, solución, criterios, rúbrica y conexión curricular.

[Guía docente de competencias](GUIA_DOCENTE_COMPETENCIAS.md) · [Marcos de evaluación](ASSESSMENT_FRAMEWORKS.md) · [Ciclo de evidencia](EVIDENCE_CYCLE.md)

> **Estado real:** banco inicial con revisión interna. No es exhaustivo, no ha sido validado psicométricamente y no contiene preguntas oficiales de organismos externos.

{chr(10).join(sections)}
## Autoría y licencia

Las tareas son originales de `chilean-school-learning-path` y se publican bajo CC BY-NC-SA 4.0, según el registro de cada tarea.
'''


def _legacy_evaluation_markdown(references: dict[str, dict[str, Any]]) -> str:
    sections = []
    for key, instrument in INSTRUMENTS.items():
        variants = variants_for(key)
        documents = "\n".join(f"- [{label}]({url})" for label, url in instrument["documents"])
        if not documents:
            documents = "- [Evaluación formativa](EVALUACION_FORMATIVA.md)\n- [Ciclo de evidencia](EVIDENCE_CYCLE.md)"
        variant_rows = []
        for variant in variants:
            oa_links = []
            for code in variant["oa_codes"]:
                reference = references.get(code)
                if reference:
                    oa_links.append(f"[{code} · {reference['topic']}](../{reference['path']})")
            variant_rows.append(
                f"| [{variant['name']}](ENSAYOS_EJEMPLO.md#{slug(variant['name'])}) | {variant['level']} | {variant['focus']} | {' / '.join(oa_links) or 'Fuera del alcance actual'} |"
            )
        variants_table = "\n".join(variant_rows) if variant_rows else "| No corresponde | Educación parvularia | Fuera de 1° básico–4° medio | Sin enlace forzado |"
        history_rows = "\n".join(
            f"| {period} | **{title}** | {detail} |"
            for period, title, detail in instrument["history"]
        )
        predecessor_rows = "\n".join(
            f"- **{name}:** {relation}" for name, relation in instrument["predecessors"]
        )
        routes = []
        for variant in variants:
            route_steps = []
            for index, code in enumerate(variant["oa_codes"], start=1):
                reference = references.get(code)
                if reference:
                    action = "Antecedente" if index == 1 else "Consolidar o transferir"
                    route_steps.append(
                        f"{index}. **{action}:** [{code} · {reference['topic']}](../{reference['path']}) — {reference['course']}, {reference['subject']}, clase {reference['lesson']} de {reference['lesson_count']} ({reference['phase']})."
                    )
            routes.append(f'''#### {variant['name']}

**Contenido y desempeño:** {variant['focus']}

{chr(10).join(route_steps)}
**Muestra breve para comprobar un desempeño:** [{variant['name']}](ENSAYOS_EJEMPLO.md#{slug(variant['name'])}) en una situación original. No cubre el instrumento completo.

- **Qué observar:** {variant['observe']}
- **Si aparece dificultad:** {variant['intervene']}
- **Cómo reevaluar:** {variant['reassess']}
''')
        sections.append(f'''## {instrument['short_name']} · {instrument['name']}

[Abrir la guía individual completa](evaluaciones/{key}.md)

**Tipo:** {instrument['category']}.

**Responsable:** {instrument['responsible']}.

**Inicio o primera aplicación:** {instrument['first_cycle']}.

**Periodicidad:** {instrument['cadence']}.

### Qué es y por qué existe

{instrument['definition']}

{instrument['why_exists']}

**A quién se dirige o qué unidad observa:** {instrument['population']}

**Para qué sirve:** {instrument['purpose']}

**Estado en el proyecto:** {instrument['status']}.

### Historia y versiones anteriores

| Periodo | Hito | Qué cambió |
|---|---|---|
{history_rows}

**Antecedentes que no deben confundirse con el instrumento vigente**

{predecessor_rows}

### Cómo funciona

{chr(10).join(f'{index}. {value}' for index, value in enumerate(instrument['design'], start=1))}

### Qué resultados entrega y qué no permite concluir

**Lectura válida**

{chr(10).join(f'- {value}' for value in instrument['reporting'])}

**Límites**

{chr(10).join(f'- {value}' for value in instrument['boundaries'])}

### Uso docente responsable

{chr(10).join(f'{index}. {value}' for index, value in enumerate(instrument['classroom_use'], start=1))}

### Documentos y fuentes institucionales

{documents}

### Mapa rápido de variantes y contenidos

| Variante | Nivel o población | Contenido y desempeño | OA y clases de referencia |
|---|---|---|---|
{variants_table}

> Las referencias a OA son correspondencias pedagógicas del proyecto. No son tablas oficiales de equivalencia.

### Rutas docentes precisas usando contenido existente

{chr(10).join(routes) if routes else 'ECES queda fuera del tramo 1° básico–4° medio: se explica como estudio de sistemas y no se fuerza una ruta a OA escolares.'}
''')
    return f'''# Evaluaciones complementarias conectadas a la trayectoria chilena

Esta es la entrada Markdown para docentes. Reúne evaluaciones nacionales censales y muestrales, acceso a educación superior, herramientas diagnósticas, estudios internacionales y evaluación interna sin tratarlos como equivalentes.

[Índice de las 13 guías individuales](evaluaciones/README.md) · [Informe de brechas previo](COMPETENCY_GAP_REPORT.md) · [Estado actual de brechas](INFORME_BRECHAS_ACTUAL.md) · [Muestras y cobertura](ENSAYOS_EJEMPLO.md) · [Estado de implementación](ESTADO_IMPLEMENTACION.md)

## Cómo se conectan

`Currículo → OA → clase existente → habilidad → instrumento complementario → evidencia → intervención → reevaluación`

Los JSON son fuentes internas de validación. La lectura docente está en este documento y en el portal HTML.

## Comprensión lectora sin duplicar un curso

La lectura aparece, con propósitos y poblaciones distintas, en Impulso Lector, Estudios Nacionales, PAES Competencia Lectora, SIMCE Lectura, DIA, PISA Lectura, PIRLS y ERCE. Cada sección enlaza los OA y clases ya existentes; no se crea un curso genérico paralelo.

{chr(10).join(sections)}
## Regla sobre puntajes

Las muestras breves calculan entre 0 y 4 puntos del proyecto con criterios visibles. No son ensayos completos y no se convierten en puntaje PAES, SIMCE, PISA, TIMSS, PIRLS, ERCE, ICILS, ICCS o DIA. Las escalas oficiales dependen del diseño y de los procedimientos de cada institución.
'''


def _legacy_exams_markdown(references: dict[str, dict[str, Any]]) -> str:
    sections = []
    for variant in VARIANTS:
        instrument = INSTRUMENTS[variant["instrument"]]
        form = SAMPLE_FORMS[variant["form"]]
        closed = []
        for index, question in enumerate(form["questions"], start=1):
            options = "\n".join(f"- **{chr(65 + option_index)}.** {option}" for option_index, option in enumerate(question["options"]))
            closed.append(f"**{index}. {question['prompt']}**\n\n{options}")
        answer_key = ", ".join(
            f"{index}: {chr(65 + question['answer'])}"
            for index, question in enumerate(form["questions"], start=1)
        )
        oa_links = []
        route_steps = []
        for code in variant["oa_codes"]:
            reference = references.get(code)
            if reference:
                oa_links.append(f"[{code}](../{reference['path']})")
                action = "Preparar" if not route_steps else "Enseñar y practicar"
                route_steps.append(
                    f"{len(route_steps) + 1}. **{action}:** [{code} · {reference['topic']}](../{reference['path']}) — {reference['course']}, {reference['subject']}, clase {reference['lesson']} de {reference['lesson_count']} ({reference['phase']})."
                )
        sections.append(f'''## {variant['name']}

**Instrumento de referencia:** [{instrument['short_name']}](evaluaciones/{variant['instrument']}.md).

**Población orientativa:** {variant['level']} · **Dominio:** {variant['domain']}.

> **Muestra breve original del proyecto · cobertura parcial.** No es un ensayo completo, no es una pregunta oficial y no reproduce la extensión, contenidos totales o escala del instrumento.

### Antes de aplicar

**Contenido y desempeño que se observará:** {variant['focus']}

**Qué observar sin etiquetar:** {variant['observe']}

### Situación

{form['stimulus']}

### Preguntas cerradas

{chr(10).join(closed)}

### Respuesta desarrollada

3. {form['open_prompt']}

### Clave y rúbrica

- **Clave de cerradas:** {answer_key}.
{chr(10).join(f'- {value}' for value in form['open_rubric'])}

### Cálculo

- 1 punto por cada respuesta cerrada correcta.
- 0, 1 o 2 puntos para la respuesta desarrollada según la rúbrica.
- Máximo: 4 puntos del proyecto.
- 0: evidencia insuficiente; 1–2: evidencia inicial; 3: evidencia consistente; 4: evidencia sólida en este ejemplo y pendiente de transferencia.

**OA y clases para enseñar o reforzar:** {' · '.join(oa_links)}.

### Ruta con contenido existente

{chr(10).join(route_steps)}

3. **Comprobar en otra situación:** aplicar esta muestra y registrar la evidencia por criterio.

- **Si aparece dificultad:** {variant['intervene']}
- **Cómo reevaluar:** {variant['reassess']}
''')
    return (f'''# Muestras calculables y estado de cobertura

Este documento reúne {len(VARIANTS)} muestras breves de versiones o áreas. Cada una contiene dos preguntas cerradas y una respuesta desarrollada. La puntuación es una regla didáctica del proyecto y no una conversión oficial.

**Son muestras breves, no ensayos completos.**

> **Corrección de alcance:** estas piezas no cubren todos los contenidos de los instrumentos y, por tanto, no se presentan como ensayos completos. Un ensayo de ejemplo requerirá una matriz de contenidos y al menos una tarea por cada eje; uno completo deberá cubrir todo el temario o marco de su versión.

[Guías individuales de instrumentos](evaluaciones/README.md) · [Evaluaciones complementarias](EVALUACIONES_COMPLEMENTARIAS.md) · [Banco de tareas extensas](BANCO_TAREAS.md) · [Ciclo de evidencia](EVIDENCE_CYCLE.md)

{chr(10).join(sections)}
''').rstrip() + "\n"


def evaluation_markdown(references: dict[str, dict[str, Any]]) -> str:
    del references
    return '''# Índice de evaluaciones complementarias

Este archivo es únicamente una puerta de entrada. **No contiene instrumentos concatenados.**

Cada instrumento conserva toda su explicación, historia, versiones, diseño, resultados, rutas curriculares, muestras, claves y rúbricas dentro de su propio archivo Markdown.

[Abrir el índice de archivos individuales](evaluaciones/README.md)

## Regla documental

- Un instrumento = un Markdown propio.
- El contenido de un instrumento no continúa con otro instrumento en este archivo.
- Los índices solo ayudan a encontrar el documento correcto.
- Los archivos JSON permanecen como soporte técnico y no como lectura docente.

[Informe de brechas previo](COMPETENCY_GAP_REPORT.md) · [Brechas actuales](INFORME_BRECHAS_ACTUAL.md) · [Estado de implementación](ESTADO_IMPLEMENTACION.md)
'''


def exams_markdown(references: dict[str, dict[str, Any]]) -> str:
    del references
    return f'''# Índice de muestras por instrumento

Este archivo es únicamente un índice. **No reúne PAES, SIMCE ni otros instrumentos uno después de otro.**

Las {len(VARIANTS)} muestras breves, sus claves, rúbricas, cálculo, intervención y reevaluación están dentro del Markdown individual del instrumento correspondiente.

[Abrir el índice de archivos individuales](evaluaciones/README.md)

## Alcance

- La cobertura parcial actual corresponde a muestras breves: no ensayos completos.
- Cada Markdown individual declara su cobertura y sus límites.
- Los puntos del proyecto no se convierten en escalas oficiales.
- Un ensayo completo solo puede declararse después de cubrir toda la matriz vigente de su versión.
'''


def current_gaps_markdown() -> str:
    rows = "\n".join(
        f"| {name} | **{status}** | {evidence} | {action} |"
        for name, status, evidence, action in CURRENT_GAP_ROWS
    )
    return f'''# Informe de brechas actual · después de la implementación

**Fecha:** 3 de octubre de 2026

Este documento complementa, pero no reemplaza, el [informe de brechas previo](COMPETENCY_GAP_REPORT.md). El informe previo conserva la línea base anterior a la programación; esta tabla registra el estado observable posterior.

| Elemento | Estado actual | Evidencia disponible | Acción pendiente |
|---|---|---|---|
{rows}

## Lectura responsable

- “Existe” significa que hay un artefacto navegable y verificable, no que exista cobertura exhaustiva.
- “Parcial” no se promueve a “completo” por tener código o muchas páginas.
- Las muestras breves son originales, no son ensayos completos y sus puntos no equivalen a escalas oficiales.
- Revisión humana, pilotaje y validación psicométrica continúan siendo estados separados.
'''


def implementation_status_markdown() -> str:
    rows = "\n".join(
        f"| {item['title']} | **{item['state']}** | {item['available']} | {item['limit']} | [{Path(item['path']).name}]({item['path'].removeprefix('docs/')}) |"
        for item in IMPLEMENTATION_AREAS
    )
    return f'''# Estado de implementación pedagógica

**Fecha de corte:** 3 de octubre de 2026

Esta guía responde qué puede usar hoy un docente, para qué sirve, qué límite conserva y dónde comprobarlo. Está organizada por capacidades educativas y no por instrucciones de desarrollo.

| Capacidad | Estado | Qué existe | Límite o trabajo pendiente | Evidencia |
|---|---|---|---|---|
{rows}

## Cómo leer los estados

- **Conservado o conectado:** existe una salida navegable para el alcance declarado.
- **Inicial, parcial, prototipo o demostración:** hay una base funcional, pero no cobertura completa, pilotaje o validación externa.
- **Reglas o límites definidos:** existe arquitectura y resguardo; no se afirma que el producto completo esté terminado.

## Diferencia entre muestra y ensayo

El repositorio publica {len(VARIANTS)} muestras breves calculables. Sirven para comprender una situación, la clave, la rúbrica y el cálculo, pero **no son ensayos completos**. Un ensayo sólo se declarará completo cuando su matriz muestre todos los contenidos de la versión correspondiente y cada uno tenga tareas verificables.

## Límite general

La capa es navegable, pero no posee revisión disciplinar completa, pilotaje amplio, registros reales de estudiantes ni validez psicométrica.
'''


def instrument_markdown_index() -> str:
    rows = "\n".join(
        f"| [{item['short_name']}]({key}.md) | {item['category']} | {item['population']} | {len(variants_for(key))} |"
        for key, item in INSTRUMENTS.items()
    )
    return f'''# Guías individuales de instrumentos complementarios

Cada guía explica un instrumento o familia con su propio contexto, historia, diseño, interpretación, límites, rutas curriculares y fuentes. Ninguno reemplaza el currículo chileno.

[Brechas actuales](../INFORME_BRECHAS_ACTUAL.md) · [Estado de implementación](../ESTADO_IMPLEMENTACION.md)

| Instrumento | Tipo | Población o unidad observada | Rutas disponibles |
|---|---|---|---:|
{rows}

## Regla de navegación

Cada fila abre un archivo independiente. La explicación y las muestras de un instrumento permanecen dentro de ese mismo Markdown; no continúan con el instrumento siguiente. El portal público genera versiones HTML equivalentes sin mezclar extensiones.
'''


def instrument_markdown(key: str, references: dict[str, dict[str, Any]]) -> str:
    instrument = INSTRUMENTS[key]
    variants = variants_for(key)
    history = "\n".join(f"| {period} | **{title}** | {detail} |" for period, title, detail in instrument["history"])
    predecessors = "\n".join(f"- **{name}:** {relation}" for name, relation in instrument["predecessors"])
    documents = "\n".join(f"- [{label}]({url})" for label, url in instrument["documents"])
    if not documents:
        documents = "- [Evaluación formativa del proyecto](../EVALUACION_FORMATIVA.md)\n- [Ciclo de evidencia](../EVIDENCE_CYCLE.md)"
    coverage_rows = []
    route_sections = []
    sample_sections = []
    for variant in variants:
        linked = []
        stages = []
        journey = variant.get("journey") or [("Referencia curricular", variant["oa_codes"])]
        for stage, codes in journey:
            stage_links = []
            for code in codes:
                reference = references.get(code)
                if not reference:
                    continue
                linked.append(code)
                stage_links.append(f"[{code} · {reference['topic']}](../../{reference['path']})")
            if stage_links:
                stages.append(f"- **{stage}:** " + " · ".join(stage_links))
        coverage_rows.append(
            f"| [{variant['name']}](#{slug('muestra-' + variant['name'])}) | {variant['level']} | {variant['domain']} | {len(linked)} referencias curriculares | Muestra breve; no cubre el instrumento completo |"
        )
        route_sections.append(f'''### {variant['name']}

**Qué se busca observar:** {variant['focus']}

{chr(10).join(stages) if stages else 'No se fuerza una referencia curricular fuera del alcance del repositorio.'}

- **Qué observar:** {variant['observe']}
- **Si aparece dificultad:** {variant['intervene']}
- **Cómo reevaluar:** {variant['reassess']}
- **Muestra calculable:** [{variant['name']}](#{slug('muestra-' + variant['name'])}).
''')
        form = SAMPLE_FORMS[variant["form"]]
        closed_questions = []
        for question_index, question in enumerate(form["questions"], start=1):
            options = "\n".join(
                f"- **{chr(65 + option_index)}.** {option}"
                for option_index, option in enumerate(question["options"])
            )
            closed_questions.append(
                f"**{question_index}. {question['prompt']}**\n\n{options}"
            )
        answer_key = ", ".join(
            f"{question_index}: {chr(65 + question['answer'])}"
            for question_index, question in enumerate(form["questions"], start=1)
        )
        sample_sections.append(f'''### Muestra · {variant['name']}

**Población orientativa:** {variant['level']} · **Dominio:** {variant['domain']}.

> **Muestra breve original · cobertura parcial.** Pertenece únicamente a {instrument['short_name']}; no es una pregunta oficial ni un ensayo completo.

**Contenido y desempeño:** {variant['focus']}

#### Situación

{form['stimulus']}

#### Preguntas cerradas

{chr(10).join(closed_questions)}

#### Respuesta desarrollada

3. {form['open_prompt']}

#### Clave, rúbrica y cálculo

- **Clave de cerradas:** {answer_key}.
{chr(10).join(f'- {value}' for value in form['open_rubric'])}
- 1 punto por cada respuesta cerrada correcta.
- 0, 1 o 2 puntos para la respuesta desarrollada según la rúbrica.
- Máximo: 4 puntos del proyecto; no se convierte a una escala oficial.

#### Decisión pedagógica

- **Qué observar:** {variant['observe']}
- **Si aparece dificultad:** {variant['intervene']}
- **Cómo reevaluar:** {variant['reassess']}
''')
    paes_note = '''
> **PAES no comienza en 4° medio.** La prueba se aplica al final de la trayectoria, pero lectura, modelación, uso de evidencia y pensamiento crítico se construyen durante años. Las etapas enlazadas abajo son antecedentes pedagógicos inferidos. No significan que cada OA sea contenido directo del temario PAES vigente; para eso se consulta el temario oficial del proceso.
''' if key == "paes" else ""
    return f'''# {instrument['short_name']} · {instrument['name']}

> **Guía docente individual · corte documental 3 de octubre de 2026.** Esta síntesis no es un documento oficial del organismo responsable y no reproduce preguntas protegidas.

[Índice de instrumentos](./README.md)

{paes_note}
## En una mirada

| Aspecto | Descripción |
|---|---|
| Tipo | {instrument['category']} |
| Responsable | {instrument['responsible']} |
| Población o unidad | {instrument['population']} |
| Inicio o primer ciclo | {instrument['first_cycle']} |
| Periodicidad | {instrument['cadence']} |
| Estado en este proyecto | {instrument['status']} |
| Rutas docentes disponibles | {len(variants)} |

## Qué es

{instrument['definition']}

## Por qué existe

{instrument['why_exists']}

**Para qué sirve:** {instrument['purpose']}

## Qué preguntas ayuda a responder y cuáles no

Puede aportar evidencia sobre su población, dominio y propósito dentro del diseño declarado. No explica por sí solo la causa de un error individual, no reemplaza evaluación de aula y no convierte una correspondencia del proyecto en alineamiento oficial.

## Historia y versiones anteriores

| Periodo | Hito | Qué cambió |
|---|---|---|
{history}

### Antecedentes que no deben confundirse con el instrumento vigente

{predecessors}

## Cómo funciona y qué observa

{chr(10).join(f'{index}. {value}' for index, value in enumerate(instrument['design'], start=1))}

## Qué significan los resultados

{chr(10).join(f'- {value}' for value in instrument['reporting'])}

## Qué no permiten concluir

{chr(10).join(f'- {value}' for value in instrument['boundaries'])}
- Una muestra breve del proyecto no se transforma en la escala oficial del instrumento.
- Un resultado aislado no constituye diagnóstico pedagógico ni etiqueta a un estudiante.

## Cómo se calculan los resultados o puntajes

{SCORING_NOTES[key]}

## Uso pedagógico antes, durante y después

### Antes

Definir qué información se necesita, revisar la versión y población correctas y acordar el criterio observable antes de mirar resultados.

### Durante

{chr(10).join(f'- {value}' for value in instrument['classroom_use'])}

### Después

Volver a OA y clases existentes, recoger más de una evidencia, intervenir sobre una dificultad observable y reevaluar con una situación diferente.

## Matriz de cobertura disponible

| Versión o área | Población | Dominio | Referencias conectadas | Cobertura real de la muestra |
|---|---|---|---:|---|
{chr(10).join(coverage_rows) if coverage_rows else '| No corresponde | Educación parvularia | Estudio del sistema | 0 | No se fuerza un ensayo escolar |'}

> **Lectura honesta:** las muestras actuales no cubren todos los contenidos del instrumento. La tabla evita llamar “ensayo completo” a tres tareas. Una versión completa deberá incorporar la matriz oficial vigente y una tarea verificable por cada contenido.

## Rutas longitudinales hacia clases existentes

{chr(10).join(route_sections) if route_sections else 'Este estudio observa educación parvularia como sistema. No corresponde forzar una ruta a OA escolares de 1° básico a 4° medio.'}

## Muestras calculables de este instrumento

{chr(10).join(sample_sections) if sample_sections else 'No corresponde crear una muestra escolar: este estudio observa sistemas de educación parvularia y no evalúa directamente a estudiantes del tramo escolar.'}

## Preguntas frecuentes

### ¿Este instrumento define qué enseñar?

No. El currículo y los OA definen la trayectoria escolar; el instrumento observa una parte de lo aprendido desde un propósito específico.

### ¿Una baja respuesta permite diagnosticar una habilidad?

No. Es una observación. Se necesita evidencia acumulada, análisis de la tarea, revisión de prerrequisitos y una reevaluación diferente.

### ¿Las rutas de esta guía son oficiales?

No. Son correspondencias pedagógicas inferidas y trazables del proyecto. Las fuentes oficiales aparecen separadas.

### ¿Los puntos de las muestras son puntajes oficiales?

No. Son puntos didácticos del proyecto y no se convierten a escalas, niveles de logro, percentiles ni resultados institucionales.

## Fuentes institucionales

{documents}

## Autoría, revisión y límites

La explicación y las muestras son contenido original del proyecto bajo CC BY-NC-SA 4.0. Los nombres, marcos, OA y documentos enlazados conservan titularidad y condiciones de sus instituciones. Estado editorial: revisión interna; revisión disciplinar, pilotaje y validación psicométrica pendientes.
'''


def page() -> str:
    taxonomy = load("competencies/taxonomy.v1.json")
    progressions = load("competencies/progressions.v1.json")
    frameworks = load("competencies/frameworks.v1.json")
    bank = load("assessments/item-bank.v1.json")
    example = load("evidence/examples/reading-inference-cycle.json")
    summary = analyze_cycle(example)
    links = first_class_links()
    skills_by_id = skill_names(taxonomy)
    frameworks_by_id = {value["id"]: value["short_name"] for value in frameworks["frameworks"]}

    trajectory_sections = "".join(
        progression_html(progression, links, skills_by_id)
        for progression in progressions["progressions"]
    )
    framework_cards = "".join(framework_card(item) for item in frameworks["frameworks"])
    item_cards = "".join(
        item_card(item, skills_by_id, frameworks_by_id) for item in bank["items"]
    )
    error_rows = "".join(
        error_row(pattern, links) for pattern in progressions["error_patterns"]
    )
    domain_cards = "".join(
        f'''<article class="level-card"><div><span>{sum(skill['domain_id'] == domain['id'] for skill in taxonomy['skills'])} habilidades</span></div>
        <h2>{esc(domain['name'])}</h2><p>{esc(domain['description'])}</p><a href="habilidades.html#{esc(domain['id'])}">Ver habilidades explicadas →</a></article>'''
        for domain in taxonomy["domains"]
    )

    status_labels = {
        "mastery_documented": "Dominio descriptivo documentado",
        "transfer_observed": "Transferencia observada",
        "improvement_observed": "Mejora observada",
    }
    evidence_ids = summary["mastery_basis"].get("evidence_ids", [])
    evidence_list = "".join(f"<li>{esc(record_id)}</li>" for record_id in evidence_ids)

    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#071c2c"><meta name="description" content="Trayectorias longitudinales de competencias enlazadas al currículo chileno, evaluación y evidencia.">
<link rel="canonical" href="{PUBLIC_URL}"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css">
<title>Competencias y evidencia | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#competencias">Saltar a competencias</a>
<header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al portal</a></header>
<main id="competencias" class="level-shell">
  <header class="level-hero competency-hero"><div><p class="eyebrow">Guía para docentes · OA → competencia → evidencia → intervención</p><h1>Competencias a través de los años.</h1><p>Una capa transversal y versionada que conecta aprendizajes existentes desde 1° básico hasta 4° medio. Los OA siguen siendo la fuente curricular; los marcos externos son vistas desacopladas.</p><div class="hero-actions"><a class="button primary" href="../evaluaciones/index.html">Evaluaciones: PAES, SIMCE, DIA y estudios</a><a class="button dark-text" href="banco-tareas.html">Abrir tareas completas</a><a class="button dark-text" href="#que-existe">Estado de la capa</a></div></div><aside><span>Versión inicial</span><strong>{len(taxonomy['skills'])} habilidades</strong><small>{len(progressions['progressions'])} progresiones · {len(bank['items'])} tareas originales</small></aside></header>
  <section class="level-metrics"><div><strong>{len(taxonomy['domains'])}</strong><span>dominios transversales</span></div><div><strong>{len(progressions['progressions'])}</strong><span>trayectorias demostrativas</span></div><div><strong>{len(frameworks['frameworks'])}</strong><span>marcos desacoplados</span></div><div><strong>0</strong><span>porcentajes ficticios</span></div></section>

  <section class="implementation-summary" id="que-existe"><div><p class="eyebrow">Respuesta directa</p><h2>Qué quedó realmente implementado.</h2><ul><li>Una taxonomía de {len(taxonomy['skills'])} habilidades con nombres estables y lectura docente.</li><li>{len(progressions['progressions'])} trayectorias demostrativas enlazadas a OA y clases ya existentes.</li><li>PAES, SIMCE, PISA, TIMSS y PIRLS como vistas de evaluación, con fuentes, límites y relaciones clasificadas.</li><li>{len(bank['items'])} tareas originales completas con respuesta, solución, rúbrica y trazabilidad.</li><li>Un ciclo determinista que separa observación, patrón, hipótesis, intervención y reevaluación.</li></ul><p><a href="habilidades.html">Ver las habilidades sin códigos técnicos →</a></p></div><div><p class="eyebrow">Lo que no se afirma</p><h2>Qué todavía no existe.</h2><ul><li>No hay un mapeo exhaustivo de todos los OA.</li><li>No hay banco masivo ni plataforma con registros reales de estudiantes.</li><li>No hay pilotaje amplio, baremos ni validación psicométrica.</li><li>No hay equivalencia oficial con PAES, SIMCE, PISA, TIMSS o PIRLS.</li><li>No se creó un preuniversitario ni un predictor de puntaje.</li></ul><p><a href="marcos-evaluacion.html">Revisar marco por marco →</a></p></div></section>

  <section class="level-intro"><div><p class="eyebrow">Taxonomía transversal</p><h2>Una habilidad, varias asignaturas.</h2></div><p>Interpretar un gráfico científico puede activar lectura, matemática, ciencias y datos. La habilidad se declara una sola vez y se enlaza en muchos contextos.</p></section>
  <section class="level-grid">{domain_cards}</section>

  <div id="trayectorias">{trajectory_sections}</div>

  <section class="level-intro"><div><p class="eyebrow">Marcos de evaluación</p><h2>Vistas, no currículos paralelos.</h2></div><p>PAES, SIMCE, PISA, TIMSS y PIRLS conservan institución, versión, población, fuente y limitaciones. Cada tarjeta abre ahora una explicación completa de lo implementado y de lo pendiente.</p></section>
  <section class="level-grid">{framework_cards}</section>

  <section class="level-intro" id="estudiante"><div><p class="eyebrow">Vista estudiante</p><h2>Qué mejoró y qué sigue.</h2></div><p>El perfil usa evidencia identificable, no una barra inventada. Este ejemplo es sintético y muestra un ciclo cerrado con tareas nuevas.</p></section>
  <section class="student-profile"><div><span>Habilidad observada</span><strong>Inferencia causal</strong><small>{esc(status_labels.get(summary['status'], summary['status']))}</small></div><div><h3>¿Por qué aparece este estado?</h3><p>{esc(summary['mastery_basis']['reason'])}</p><ul>{evidence_list}</ul></div><div><h3>¿Qué sigue?</h3><p>{esc(summary['next_step'])}</p><p>No es una nota, percentil ni diagnóstico psicométrico.</p></div></section>

  <section class="level-intro" id="docente"><div><p class="eyebrow">Vista docente</p><h2>Errores observables, hipótesis prudentes y clases existentes.</h2></div><p>Cada fila separa lo observado de posibles explicaciones y enlaza intervenciones ya presentes en la trayectoria. Una respuesta aislada nunca etiqueta al estudiante.</p></section>
  <div class="table-scroll"><table class="competency-table"><thead><tr><th>Observación</th><th>Hipótesis posibles</th><th>Contenido existente</th><th>Reevaluación</th></tr></thead><tbody>{error_rows}</tbody></table></div>

  <section class="level-intro" id="banco"><div><p class="eyebrow">Banco inicial</p><h2>Tareas originales que se pueden leer.</h2></div><p>Cada ficha abre el contenido completo para docentes. El JSON sigue existiendo para validación, pero deja de ser la interfaz del programa. “Revisión interna” no significa validación.</p></section>
  <section class="level-grid">{item_cards}</section>

  <section class="level-contract"><div><p class="eyebrow">Límites explícitos</p><h2>La honestidad también es arquitectura.</h2></div><ol><li><strong>OA intactos</strong><span>La taxonomía no modifica el currículo oficial.</span></li><li><strong>IA opcional</strong><span>El núcleo funciona con reglas deterministas y revisión humana.</span></li><li><strong>Psicometría separada</strong><span>No hay IRT, baremos ni validez simulada.</span></li><li><strong>Datos protegidos</strong><span>Git solo admite ejemplos sintéticos; los registros reales permanecen en sistemas locales autorizados.</span></li></ol></section>
</main>
<footer class="site-footer"><div><strong>Competencias y evidencia</strong><span>Lectura pedagógica para docentes · OA oficiales conservan sus derechos</span></div><div><a href="habilidades.html">Habilidades</a><a href="../evaluaciones/index.html">Evaluaciones</a><a href="banco-tareas.html">Tareas</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''


def add_level_evaluation_shortcut(content: str) -> str:
    marker = 'class="evaluation-shortcut"'
    if marker in content:
        return content
    shortcut = '''<section class="evaluation-shortcut"><div><p class="eyebrow">Evaluaciones complementarias</p><h2>¿Cómo se relaciona este nivel con SIMCE, DIA, PISA, TIMSS, PIRLS, ERCE, PAES y otros estudios?</h2><p>Abre el centro por nombre del instrumento. Allí encontrarás propósito, población, documentos oficiales, muestras con cobertura explícita y enlaces de regreso a OA y clases.</p></div><a class="button primary" href="../evaluaciones/index.html">Abrir evaluaciones y guías →</a></section>'''
    return re.sub(
        r'(</header>)(\s*<section class="level-metrics"[^>]*>)',
        rf'\1{shortcut}\2',
        content,
        count=1,
    )


def expected_outputs() -> dict[Path, str]:
    taxonomy = load("competencies/taxonomy.v1.json")
    progressions = load("competencies/progressions.v1.json")
    frameworks = load("competencies/frameworks.v1.json")
    bank = load("assessments/item-bank.v1.json")
    links = first_class_links()
    sources = first_class_sources()
    references = class_references()
    outputs = {
        OUTPUT / "index.html": page(),
        OUTPUT / "habilidades.html": skills_page(taxonomy, progressions),
        OUTPUT / "banco-tareas.html": bank_page(bank, taxonomy, frameworks),
        OUTPUT / "marcos-evaluacion.html": frameworks_page(frameworks, bank, taxonomy, links),
        ROOT / "docs" / "GUIA_DOCENTE_COMPETENCIAS.md": teacher_guide_markdown(taxonomy, progressions, bank),
        ROOT / "docs" / "BANCO_TAREAS.md": bank_markdown(bank, taxonomy, frameworks, sources),
        ROOT / "docs" / "EVALUACIONES_COMPLEMENTARIAS.md": evaluation_markdown(references),
        ROOT / "docs" / "ENSAYOS_EJEMPLO.md": exams_markdown(references),
        ROOT / "docs" / "INFORME_BRECHAS_ACTUAL.md": current_gaps_markdown(),
        ROOT / "docs" / "ESTADO_IMPLEMENTACION.md": implementation_status_markdown(),
        ROOT / "docs" / "evaluaciones" / "README.md": instrument_markdown_index(),
        EVALUATION_OUTPUT / "index.html": evaluation_hub(frameworks),
        EVALUATION_OUTPUT / "ensayos.html": exams_index_page(),
        EVALUATION_OUTPUT / "brechas.html": gaps_page(),
        EVALUATION_OUTPUT / "estado-implementacion.html": implementation_status_page(),
    }
    for key in INSTRUMENTS:
        outputs[ROOT / "docs" / "evaluaciones" / f"{key}.md"] = instrument_markdown(key, references)
        outputs[EVALUATION_OUTPUT / f"{key}.html"] = instrument_page(
            key, frameworks, bank, taxonomy, references
        )
    for variant in VARIANTS:
        outputs[EVALUATION_OUTPUT / "ensayos" / f"{variant['id']}.html"] = exam_page(
            variant, references
        )
    for index, item in enumerate(bank["items"]):
        previous_item = bank["items"][index - 1] if index else None
        next_item = bank["items"][index + 1] if index + 1 < len(bank["items"]) else None
        outputs[OUTPUT / "tareas" / f"{slug(item['id'])}.html"] = task_page(
            item, taxonomy, frameworks, links, previous_item, next_item
        )
    copies = {
        "taxonomy.v1.json": ROOT / "competencies" / "taxonomy.v1.json",
        "progressions.v1.json": ROOT / "competencies" / "progressions.v1.json",
        "frameworks.v1.json": ROOT / "competencies" / "frameworks.v1.json",
        "item-bank.v1.json": ROOT / "assessments" / "item-bank.v1.json",
        "evidence-cycle.example.json": ROOT / "evidence" / "examples" / "reading-inference-cycle.json",
    }
    for name, source in copies.items():
        outputs[OUTPUT / "data" / name] = source.read_text(encoding="utf-8")
    for level_path in sorted((ROOT / "site" / "levels").glob("*.html")):
        outputs[level_path] = add_level_evaluation_shortcut(
            level_path.read_text(encoding="utf-8")
        )
    return outputs


def updated_sitemap() -> str:
    path = ROOT / "site" / "sitemap.xml"
    current = path.read_text(encoding="utf-8")
    bank = load("assessments/item-bank.v1.json")
    urls = [
        PUBLIC_URL,
        f"{PUBLIC_URL}habilidades.html",
        f"{PUBLIC_URL}marcos-evaluacion.html",
        f"{PUBLIC_URL}banco-tareas.html",
        *(f"{PUBLIC_URL}tareas/{slug(item['id'])}.html" for item in bank["items"]),
        EVALUATION_PUBLIC_URL,
        f"{EVALUATION_PUBLIC_URL}ensayos.html",
        f"{EVALUATION_PUBLIC_URL}brechas.html",
        f"{EVALUATION_PUBLIC_URL}estado-implementacion.html",
        *(f"{EVALUATION_PUBLIC_URL}{key}.html" for key in INSTRUMENTS),
        *(f"{EVALUATION_PUBLIC_URL}ensayos/{variant['id']}.html" for variant in VARIANTS),
    ]
    entries = [f"  <url><loc>{url}</loc></url>" for url in urls]
    missing = [entry for entry in entries if entry not in current]
    if not missing:
        return current
    missing_block = "\n".join(missing)
    return current.replace("</urlset>", f"{missing_block}\n</urlset>")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Comprobar sin escribir")
    args = parser.parse_args()
    outputs = expected_outputs()
    outputs[ROOT / "site" / "sitemap.xml"] = updated_sitemap()
    stale = [path for path, content in outputs.items() if not path.exists() or path.read_text(encoding="utf-8") != content]
    if args.check:
        if stale:
            print("Salidas de competencias desactualizadas:")
            for path in stale:
                print(path.relative_to(ROOT))
            return 1
        print("OK: portal de competencias reproducible.")
        return 0
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Generadas {len(outputs)} salidas de competencias.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
