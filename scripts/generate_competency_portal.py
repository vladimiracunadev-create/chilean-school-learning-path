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


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site" / "competencias"
PUBLIC_URL = (
    "https://vladimiracunadev-create.github.io/"
    "chilean-school-learning-path/competencias/"
)

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


def teacher_label(value: str, labels: dict[str, str]) -> str:
    return labels.get(value, value.replace("_", " ").replace("-", " ").capitalize())


def skill_names(taxonomy: dict[str, Any]) -> dict[str, str]:
    return {skill["id"]: skill["name"] for skill in taxonomy["skills"]}


def item_url(item: dict[str, Any], prefix: str = "") -> str:
    return f"{prefix}tareas/{slug(item['id'])}.html"


def framework_url(framework_id: str, prefix: str = "") -> str:
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
    return f'''<article class="level-card framework-card">
      <div><span>{esc(framework['short_name'])}</span><span>{esc(framework['version'])}</span></div>
      <h2>{esc(framework['name'])}</h2><p>{esc(framework['population'])}</p>
      <details><summary>Alcance y límites</summary><p>{esc(framework['scope'])}</p><ul>{limitations}</ul></details>
      <a href="marcos-evaluacion.html#{esc(framework['id'])}">Qué hizo el proyecto con {esc(framework['short_name'])} →</a>
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
    return '''<footer class="site-footer"><div><strong>Competencias y evidencia</strong><span>Lectura pedagógica para docentes · datos técnicos validados en segundo plano</span></div><div><a href="index.html">Competencias</a><a href="marcos-evaluacion.html">Marcos de evaluación</a><a href="banco-tareas.html">Banco de tareas</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''


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
        f'''<tr><th scope="row"><a href="../marcos-evaluacion.html#{esc(link['framework_id'])}">{esc(frameworks_by_id[link['framework_id']]['short_name'])}</a></th>
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
</main>''' + page_footer().replace('href="index.html"', 'href="../index.html"').replace('href="marcos-evaluacion.html"', 'href="../marcos-evaluacion.html"').replace('href="banco-tareas.html"', 'href="../banco-tareas.html"').replace('href="../documentacion.html"', 'href="../../documentacion.html"')


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
<main id="contenido" class="level-shell"><header class="plain-hero"><p class="eyebrow">Respuesta directa al prompt maestro</p><h1>Qué se hizo con PAES y los otros marcos.</h1><p>Se construyeron vistas de evaluación sobre la trayectoria escolar: se registró qué mide cada marco, se relacionaron habilidades con cautela, se crearon tareas originales y se conservó el camino de regreso a OA y clases. No se creó un preuniversitario ni se declaró una equivalencia oficial inexistente.</p></header><section class="task-warning"><strong>En una frase</strong><p>PAES, SIMCE, PISA, TIMSS y PIRLS sirven para mirar competencias construidas durante años; no reemplazan el currículo chileno.</p></section><div class="table-scroll"><table class="competency-table status-table"><thead><tr><th>Marco</th><th>Implementado ahora</th><th>No significa</th></tr></thead><tbody>{''.join(status_rows)}</tbody></table></div><section class="level-contract"><div><p class="eyebrow">Tres rótulos obligatorios</p><h2>No mezclar evidencia con interpretación.</h2></div><ol>{legend}</ol></section>{''.join(sections)}</main>''' + page_footer()


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
  <header class="level-hero competency-hero"><div><p class="eyebrow">Guía para docentes · OA → competencia → evidencia → intervención</p><h1>Competencias a través de los años.</h1><p>Una capa transversal y versionada que conecta aprendizajes existentes desde 1° básico hasta 4° medio. Los OA siguen siendo la fuente curricular; los marcos externos son vistas desacopladas.</p><div class="hero-actions"><a class="button primary" href="#que-existe">Entender qué se implementó</a><a class="button dark-text" href="banco-tareas.html">Abrir tareas completas</a><a class="button dark-text" href="marcos-evaluacion.html">Entender PAES y otros marcos</a></div></div><aside><span>Versión inicial</span><strong>{len(taxonomy['skills'])} habilidades</strong><small>{len(progressions['progressions'])} progresiones · {len(bank['items'])} tareas originales</small></aside></header>
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
<footer class="site-footer"><div><strong>Competencias y evidencia</strong><span>Lectura pedagógica para docentes · OA oficiales conservan sus derechos</span></div><div><a href="habilidades.html">Habilidades</a><a href="marcos-evaluacion.html">Marcos</a><a href="banco-tareas.html">Tareas</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''


def expected_outputs() -> dict[Path, str]:
    taxonomy = load("competencies/taxonomy.v1.json")
    progressions = load("competencies/progressions.v1.json")
    frameworks = load("competencies/frameworks.v1.json")
    bank = load("assessments/item-bank.v1.json")
    links = first_class_links()
    sources = first_class_sources()
    outputs = {
        OUTPUT / "index.html": page(),
        OUTPUT / "habilidades.html": skills_page(taxonomy, progressions),
        OUTPUT / "banco-tareas.html": bank_page(bank, taxonomy, frameworks),
        OUTPUT / "marcos-evaluacion.html": frameworks_page(frameworks, bank, taxonomy, links),
        ROOT / "docs" / "GUIA_DOCENTE_COMPETENCIAS.md": teacher_guide_markdown(taxonomy, progressions, bank),
        ROOT / "docs" / "BANCO_TAREAS.md": bank_markdown(bank, taxonomy, frameworks, sources),
    }
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
