"""Complete the remaining second-year secondary subject sequences.

The snapshot supplies official objectives and URLs. Topics, classroom anchors,
progressions, misconceptions and safeguarding decisions are authored here.
"""
from __future__ import annotations

import json
from pathlib import Path

try:
    from grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from grade_three_music_orientation_technology_lessons import _lesson as mot_lesson
    from grade_four_remaining_lessons import build_transversal_integration as base_integration
    from grade_seven_next_five_lessons import _natural_voice as physical_voice
    from grade_seven_remaining_lessons import _natural_voice as remaining_voice
    from grade_one_middle_remaining_lessons import STAGES, VOCABULARY, MISCONCEPTIONS, _art_voice
except ImportError:
    from scripts.grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from scripts.grade_three_music_orientation_technology_lessons import _lesson as mot_lesson
    from scripts.grade_four_remaining_lessons import build_transversal_integration as base_integration
    from scripts.grade_seven_next_five_lessons import _natural_voice as physical_voice
    from scripts.grade_seven_remaining_lessons import _natural_voice as remaining_voice
    from scripts.grade_one_middle_remaining_lessons import STAGES, VOCABULARY, MISCONCEPTIONS, _art_voice


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
TARGET_SLUGS = {"artes-visuales", "musica", "educacion-fisica-salud", "orientacion", "tecnologia"}

TOPICS = {
    "AR2M OA 01": "Proyectos visuales sobre problemáticas sociales y juveniles",
    "AR2M OA 02": "Escultura, diseño y materiales sustentables",
    "AR2M OA 03": "Video, multimedia y creación contemporánea",
    "AR2M OA 04": "Criterios estéticos y juicio crítico personal",
    "AR2M OA 05": "Evaluación fundamentada de proyectos visuales",
    "AR2M OA 06": "Difusión artística y aporte a la comunidad",
    "MU2M OA 01": "Valoración crítica de músicas de Chile y el mundo",
    "MU2M OA 02": "Contraste musical, composición y propósito expresivo",
    "MU2M OA 03": "Selección, interpretación y dirección de repertorio",
    "MU2M OA 04": "Interpretación, registro y difusión musical",
    "MU2M OA 05": "Improvisación, innovación y arreglos musicales",
    "MU2M OA 06": "Evaluación musical y plan personal de mejora",
    "MU2M OA 07": "Registro, transmisión y evolución de la música",
    "EF2M OA 01": "Precisión en habilidades motrices específicas",
    "EF2M OA 02": "Diseño y evaluación de estrategias deportivas",
    "EF2M OA 03": "Plan personal de entrenamiento y condición saludable",
    "EF2M OA 04": "Práctica regular, seguridad y primeros auxilios",
    "EF2M OA 05": "Liderazgo y promoción de vida activa comunitaria",
    "OR2M OA 01": "Alternativas y decisiones para proyectos de vida",
    "OR2M OA 02": "Sexualidad, vínculos, respeto e integridad",
    "OR2M OA 03": "Evaluación de riesgos y redes de apoyo",
    "OR2M OA 04": "Acciones autónomas para una vida saludable",
    "OR2M OA 05": "Relaciones constructivas e inclusión en redes",
    "OR2M OA 06": "Resolución de conflictos en un marco de derechos",
    "OR2M OA 07": "Participación, equidad y bienestar en el entorno",
    "OR2M OA 08": "Iniciativas democráticas de justicia y buen trato",
    "OR2M OA 09": "Opciones académicas y laborales para el proyecto de vida",
    "OR2M OA 10": "Diseño flexible, coherente y perseverante del proyecto de vida",
    "TE2M OA 01": "Necesidades energéticas y materiales sustentables",
    "TE2M OA 02": "Soluciones colaborativas para reducir impactos",
    "TE2M OA 03": "Evaluación ética, legal, económica y ambiental",
    "TE2M OA 04": "Escenarios, audiencias y comunicación tecnológica segura",
    "TE2M OA 05": "Innovaciones actuales, sociedad y ambiente",
    "TE2M OA 06": "Proyección de impactos de innovaciones tecnológicas",
}

PRIOR = {
    "AR": "crear, analizar y difundir proyectos visuales con contexto, materialidad y autoría en 1° medio",
    "MU": "escuchar, interpretar, crear y evaluar música mediante evidencia audible, estilo y contexto en 1° medio",
    "EF": "aplicar habilidades, tácticas y planes de actividad física con regulación, seguridad e inclusión en 1° medio",
    "OR": "analizar proyectos de vida, autocuidado, derechos y participación mediante casos protegidos en 1° medio",
    "TE": "definir usuarios, diseñar servicios y evaluar impactos éticos y ambientales en 1° medio",
}


def _anchor(code: str, topic: str) -> str:
    prefix = code[:2]
    number = int(code.rsplit(" ", 1)[-1])
    if prefix == "AR":
        return {
            1: "manifestaciones visuales atribuidas sobre problemáticas sociales y juveniles, mapas del espacio público y voces comunitarias públicas",
            2: "muestras limpias de materiales reutilizados, fichas de ciclo de vida y referentes atribuidos de escultura y diseño",
            3: "secuencias audiovisuales autorizadas, guiones gráficos y herramientas sin cuenta para video o multimedia",
            4: "selección contrastada de obras con autoría, contexto, lenguaje visual y criterios estéticos discutibles",
            5: "bitácoras y proyectos propios o ficticios con criterios ajustados al tipo de obra y registro de decisiones",
            6: "planos de montaje, fichas de obra, audiencias y medios de difusión con consentimiento, créditos y accesibilidad",
        }[number]
    if prefix == "MU":
        if number in {1, 2, 7}:
            return f"registros musicales autorizados con intérprete, fecha, lugar, tecnología de registro y mapa de escucha para {topic.lower()}"
        if number in {3, 4}:
            return f"repertorio elegido desde opciones accesibles, partitura o guía auditiva, pistas por función y medios de registro a volumen seguro para {topic.lower()}"
        if number == 5:
            return "células musicales, canción autorizada, rasgos estilísticos acordados, partitura gráfica e instrumentos o aplicación sin cuenta"
        return "dos registros de ensayo o creación, pauta de autoescucha y matriz de fortalezas, prioridades y acciones de mejora"
    if prefix == "EF":
        return {
            1: "estaciones accesibles de deporte individual, oposición, colaboración, oposición-colaboración y danza con variantes equivalentes",
            2: "juegos reducidos, mapas de espacio, reglas adaptables y registro de decisiones tácticas antes y después de una pausa",
            3: "perfiles ficticios, circuito regulable, escala de esfuerzo, ficha FITT y registro de recuperación, progresión e ingesta sin datos corporales públicos",
            4: "plan de práctica en entornos diversos, protocolo de autocuidado, hidratación, calentamiento y casos simulados de primeros auxilios",
            5: "consulta anónima de intereses, mapa de recursos, roles rotativos y plan inclusivo de actividad física comunitaria",
        }[number]
    if prefix == "OR":
        if number in {1, 9, 10}:
            return f"perfiles y trayectorias ficticias, opciones académicas o laborales y matriz de intereses, apoyos, límites y decisiones reversibles para {topic.lower()}"
        if number in {2, 3, 4}:
            return f"casos ficticios en tercera persona, tarjetas de derechos, consentimiento, riesgo y rutas institucionales de ayuda para {topic.lower()}"
        return f"situaciones presenciales o digitales ficticias, mapa de actores, derechos, acuerdos, reparación y participación para {topic.lower()}"
    return f"caso ficticio de uso energético o material, ficha de usuarios, datos de impacto, herramientas TIC sin cuenta y matriz ética, legal, económica, ambiental y social para {topic.lower()}"


COUNTS: dict[str, int] = {}
for item in CATALOG["classes"]:
    if item["course_order"] == 10 and item["subject_slug"] in TARGET_SLUGS and not item["oa_code"].startswith("de "):
        COUNTS[item["oa_code"]] = COUNTS.get(item["oa_code"], 0) + 1

RECORDS = {}
for record in SNAPSHOT["records"]:
    if record["course_order"] != 10 or record["subject_slug"] not in TARGET_SLUGS:
        continue
    for objective in record["objectives"]:
        if objective["code"].startswith("de "):
            continue
        RECORDS[objective["code"]] = {
            "slug": record["subject_slug"], "description": objective["description"],
            "url": objective["url"], "count": COUNTS[objective["code"]],
        }

if set(RECORDS) != set(TOPICS):
    raise RuntimeError(f"Perfiles restantes de 2° medio desalineados: faltan={sorted(set(RECORDS)-set(TOPICS))}; sobran={sorted(set(TOPICS)-set(RECORDS))}")


def _profile(code: str) -> dict:
    prefix = code[:2]
    topic = TOPICS[code]
    seed = sum(ord(char) for char in code)
    return {
        "topic": topic, "prior": PRIOR[prefix], "vocabulary": VOCABULARY[prefix],
        "anchor": _anchor(code, topic), "misconception": MISCONCEPTIONS[prefix][seed % 3],
        "focuses": [f"{stage}: {topic}" for stage in STAGES[prefix][:RECORDS[code]['count']]],
    }


def _retarget_links(lesson: dict, prefix: str) -> None:
    old = {"AR": "AR03", "MU": "MU03", "EF": "EF03", "OR": "OR03", "TE": "TE03"}[prefix]
    new = {"AR": "AR2M", "MU": "MU2M", "EF": "EF2M", "OR": "OR2M", "TE": "TE2M"}[prefix]
    for link in lesson.get("transversal", []):
        link["code"] = link["code"].replace(old, new)


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    prefix = code[:2]
    profile = _profile(code)
    lessons = []
    for index in range(len(profile["focuses"])):
        lesson = applied_lesson(code, index, profile) if prefix in {"AR", "EF"} else mot_lesson(code, index, profile)
        _retarget_links(lesson, prefix)
        if prefix == "OR":
            lesson["transversal"] = []
        if prefix == "EF":
            physical_voice(lesson, profile, index, prefix)
        else:
            remaining_voice(lesson, profile, index, prefix)
            if prefix == "AR":
                _art_voice(lesson, profile, index)
        lessons.append(lesson)
    record = RECORDS[code]
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": (
            f"{profile['topic']} recupera {profile['prior']} y avanza con decisiones propias de la disciplina. "
            f"Cada clase cambia situaciones, fuentes, recursos y evidencias, y enfrenta la confusión «{profile['misconception']}»."
        ),
        "prerequisites": profile["prior"], "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Eje oficial · progresión interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del objetivo; no se presenta como una unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del objetivo oficial.",
            "source": record["url"],
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    result = base_integration(item)
    result["generated_for"] = "2-medio-remaining"
    return result


SEQUENCES = {code: True for code in RECORDS}
