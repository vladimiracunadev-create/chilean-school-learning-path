#!/usr/bin/env python3
"""Generate the public longitudinal competency views from canonical JSON data."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any

from competency_evidence import analyze_cycle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site" / "competencias"
PUBLIC_URL = (
    "https://vladimiracunadev-create.github.io/"
    "chilean-school-learning-path/competencias/"
)


def load(relative: str) -> Any:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def first_class_links() -> dict[str, str]:
    catalog = load("curriculum/catalog.json")
    links: dict[str, str] = {}
    for item in catalog["classes"]:
        links.setdefault(item["oa_code"], f"../{item['web_path']}")
    return links


def progression_html(progression: dict[str, Any], links: dict[str, str]) -> str:
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
    skills = " · ".join(f"<code>{esc(skill)}</code>" for skill in progression["primary_skill_ids"])
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
      <a href="{esc(framework['source_url'])}" rel="noopener">Fuente oficial →</a>
    </article>'''


def item_card(item: dict[str, Any]) -> str:
    skills = " · ".join(item["skill_ids"][:3])
    frameworks = " · ".join(link["framework_id"] for link in item["framework_links"])
    return f'''<article class="level-card item-card" id="{esc(item['id'])}">
      <div><span>{esc(item['task_type'])}</span><span>{esc(item['difficulty'])}</span></div>
      <h2>{esc(item['title'])}</h2><p>{esc(item['context'])}</p>
      <p><strong>Habilidades:</strong> {esc(skills)}</p><p><strong>Vista:</strong> {esc(frameworks or 'interna')}</p>
      <p><strong>Estado:</strong> {esc(item['review'])} · versión {esc(item['version'])}</p>
      <a href="data/item-bank.v1.json">Abrir registro trazable →</a>
    </article>'''


def error_row(pattern: dict[str, Any], links: dict[str, str]) -> str:
    interventions = " · ".join(
        f'<a href="{esc(links[code])}">{esc(code)}</a>'
        for code in pattern["intervention_oa_codes"]
    )
    hypotheses = "; ".join(pattern["possible_hypotheses"])
    return f'''<tr><th scope="row">{esc(pattern['name'])}</th><td>{esc(hypotheses)}</td>
      <td>{interventions}</td><td>{esc(pattern['reassessment_rule'])}</td></tr>'''


def page() -> str:
    taxonomy = load("competencies/taxonomy.v1.json")
    progressions = load("competencies/progressions.v1.json")
    frameworks = load("competencies/frameworks.v1.json")
    bank = load("assessments/item-bank.v1.json")
    example = load("evidence/examples/reading-inference-cycle.json")
    summary = analyze_cycle(example)
    links = first_class_links()

    trajectory_sections = "".join(
        progression_html(progression, links)
        for progression in progressions["progressions"]
    )
    framework_cards = "".join(framework_card(item) for item in frameworks["frameworks"])
    item_cards = "".join(item_card(item) for item in bank["items"])
    error_rows = "".join(
        error_row(pattern, links) for pattern in progressions["error_patterns"]
    )
    domain_cards = "".join(
        f'''<article class="level-card"><div><span>{sum(skill['domain_id'] == domain['id'] for skill in taxonomy['skills'])} habilidades</span></div>
        <h2>{esc(domain['name'])}</h2><p>{esc(domain['description'])}</p><a href="data/taxonomy.v1.json">Ver taxonomía →</a></article>'''
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
  <header class="level-hero competency-hero"><div><p class="eyebrow">OA → competencia → evidencia → intervención</p><h1>Competencias a través de los años.</h1><p>Una capa transversal y versionada que conecta aprendizajes existentes desde 1° básico hasta 4° medio. Los OA siguen siendo la fuente curricular; los marcos externos son vistas desacopladas.</p><div class="hero-actions"><a class="button primary" href="#trayectorias">Explorar trayectorias</a><a class="button dark-text" href="#docente">Vista docente</a></div></div><aside><span>Versión inicial</span><strong>{len(taxonomy['skills'])} habilidades</strong><small>{len(progressions['progressions'])} progresiones · {len(bank['items'])} tareas originales</small></aside></header>
  <section class="level-metrics"><div><strong>{len(taxonomy['domains'])}</strong><span>dominios transversales</span></div><div><strong>{len(progressions['progressions'])}</strong><span>trayectorias demostrativas</span></div><div><strong>{len(frameworks['frameworks'])}</strong><span>marcos desacoplados</span></div><div><strong>0</strong><span>porcentajes ficticios</span></div></section>

  <section class="level-intro"><div><p class="eyebrow">Taxonomía transversal</p><h2>Una habilidad, varias asignaturas.</h2></div><p>Interpretar un gráfico científico puede activar lectura, matemática, ciencias y datos. La habilidad se declara una sola vez y se enlaza en muchos contextos.</p></section>
  <section class="level-grid">{domain_cards}</section>

  <div id="trayectorias">{trajectory_sections}</div>

  <section class="level-intro"><div><p class="eyebrow">Marcos de evaluación</p><h2>Vistas, no currículos paralelos.</h2></div><p>PAES, SIMCE, PISA, TIMSS y PIRLS conservan institución, versión, población, fuente y limitaciones. Las correspondencias con esta taxonomía se rotulan como inferencias pedagógicas.</p></section>
  <section class="level-grid">{framework_cards}</section>

  <section class="level-intro" id="estudiante"><div><p class="eyebrow">Vista estudiante</p><h2>Qué mejoró y qué sigue.</h2></div><p>El perfil usa evidencia identificable, no una barra inventada. Este ejemplo es sintético y muestra un ciclo cerrado con tareas nuevas.</p></section>
  <section class="student-profile"><div><span>Habilidad observada</span><strong>Inferencia causal</strong><small>{esc(status_labels.get(summary['status'], summary['status']))}</small></div><div><h3>¿Por qué aparece este estado?</h3><p>{esc(summary['mastery_basis']['reason'])}</p><ul>{evidence_list}</ul></div><div><h3>¿Qué sigue?</h3><p>{esc(summary['next_step'])}</p><p>No es una nota, percentil ni diagnóstico psicométrico.</p></div></section>

  <section class="level-intro" id="docente"><div><p class="eyebrow">Vista docente</p><h2>Errores observables, hipótesis prudentes y clases existentes.</h2></div><p>Cada fila separa lo observado de posibles explicaciones y enlaza intervenciones ya presentes en la trayectoria. Una respuesta aislada nunca etiqueta al estudiante.</p></section>
  <div class="table-scroll"><table class="competency-table"><thead><tr><th>Observación</th><th>Hipótesis posibles</th><th>Contenido existente</th><th>Reevaluación</th></tr></thead><tbody>{error_rows}</tbody></table></div>

  <section class="level-intro" id="banco"><div><p class="eyebrow">Banco inicial</p><h2>Tareas originales y trazables.</h2></div><p>El esquema admite selección, respuestas abiertas, resolución, argumentación, gráficos, tablas, ensayos, proyectos y problemas interdisciplinarios. “Internamente revisado” no significa validado.</p></section>
  <section class="level-grid">{item_cards}</section>

  <section class="level-contract"><div><p class="eyebrow">Límites explícitos</p><h2>La honestidad también es arquitectura.</h2></div><ol><li><strong>OA intactos</strong><span>La taxonomía no modifica el currículo oficial.</span></li><li><strong>IA opcional</strong><span>El núcleo funciona con reglas deterministas y revisión humana.</span></li><li><strong>Psicometría separada</strong><span>No hay IRT, baremos ni validez simulada.</span></li><li><strong>Datos protegidos</strong><span>Git solo admite ejemplos sintéticos; los registros reales permanecen en sistemas locales autorizados.</span></li></ol></section>
</main>
<footer class="site-footer"><div><strong>Competencias y evidencia</strong><span>Taxonomía del proyecto · OA oficiales conservan sus derechos</span></div><div><a href="../documentacion.html">Documentación</a><a href="data/progressions.v1.json">Datos</a><a href="../docs/competency-system.html">Arquitectura</a></div></footer></body></html>'''


def expected_outputs() -> dict[Path, str]:
    outputs = {OUTPUT / "index.html": page()}
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
    entry = f"  <url><loc>{PUBLIC_URL}</loc></url>"
    if entry in current:
        return current
    return current.replace("</urlset>", f"{entry}\n</urlset>")


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
