"""Complete fourth-year secondary sequences from the official MINEDUC snapshot.

The official wording, codes and URLs remain external-source material. Topics,
progressions, classroom decisions, evidence and safeguards are original
pedagogical elaborations for this repository.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

try:
    from grade_three_middle_remaining_lessons import (
        SUBJECT_PROFILES as SHARED_PROFILES,
        TOPICS_BY_SUBJECT as SHARED_TOPICS,
        build_sequence_from_record,
    )
except ImportError:
    from scripts.grade_three_middle_remaining_lessons import (
        SUBJECT_PROFILES as SHARED_PROFILES,
        TOPICS_BY_SUBJECT as SHARED_TOPICS,
        build_sequence_from_record,
    )


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
CATALOG = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
THIRD_ONLY_SLUGS = {"educacion-ciudadana-3-medio", "filosofia-3-medio", "ingles-3o-medio"}


TOPICS_BY_SUBJECT = {
    slug: list(topics)
    for slug, topics in SHARED_TOPICS.items()
    if slug not in THIRD_ONLY_SLUGS
}
TOPICS_BY_SUBJECT.update(
    {
        "educacion-ciudadana-4-medio": [
            "Institucionalidad democrática, representación y distribución del poder",
            "Corresponsabilidad ética ante desafíos y conflictos multiescalares",
            "Modelos de desarrollo, políticas económicas y justicia climática",
            "Derechos laborales, instituciones y organización social",
            "Libertad, igualdad y solidaridad ante desafíos democráticos",
            "Medios, tecnologías, participación y vida privada",
            "Territorio, espacio público, interculturalidad e inclusión",
            "Principios éticos, virtudes públicas y decisiones ciudadanas",
        ],
        "ingles-4o-medio": [
            "Relevant information for a specific purpose and cultural perspectives",
            "Clear texts, critical stance and respect for other positions",
            "Strategic English knowledge for critical comprehension and production",
            "Fluent interaction, worldviews and identity awareness",
        ],
        "lengua-literatura-4o-medio": [
            "Interpretación comparada de obras, contextos y efectos estéticos",
            "Interpretaciones múltiples desde criterios de análisis literario",
            "Evaluación crítica de discursos no literarios e ideologías",
            "Recursos multimodales, posicionamiento y construcción de sentido",
            "Producción coherente y cohesionada para análisis, postura y creación",
            "Recursos lingüísticos y no lingüísticos en la producción discursiva",
            "Diálogo argumentativo para construir, ampliar y refutar ideas",
            "Investigación ética para enriquecer lecturas y análisis",
        ],
        "matematica-4o-medio": [
            "Decisiones financieras mediante porcentajes, tasas e índices",
            "Decisiones bajo incerteza con modelos binomial y normal",
            "Modelos de crecimiento, decrecimiento y periodicidad",
            "Rectas y circunferencias mediante representación analítica",
        ],
    }
)


SUBJECT_PROFILES = {
    slug: copy.deepcopy(profile)
    for slug, profile in SHARED_PROFILES.items()
    if slug not in THIRD_ONLY_SLUGS
}
for profile in SUBJECT_PROFILES.values():
    profile["continuity"] = (
        "Retoma en 4° medio el OA compartido y exige mayor autonomía para seleccionar fuentes, "
        "justificar decisiones, revisar efectos y comunicar límites antes del egreso."
    )

SUBJECT_PROFILES.update(
    {
        "educacion-ciudadana-4-medio": {
            "purpose": "Evaluar instituciones, desarrollo, trabajo, medios, territorio y decisiones éticas para participar corresponsablemente en democracia.",
            "continuity": "Profundiza la deliberación de 3° medio hacia evaluación institucional, justicia social, derechos laborales y acción pública autónoma.",
            "barrier": "reducir ciudadanía a opinión o preferencia política sin conceptos, fuentes, contrapunto, viabilidad ni resguardo de derechos",
            "outcomes": ["evaluar institucionalidad y poder", "deliberar sobre desarrollo y justicia", "analizar derechos, medios y territorio", "decidir y actuar con ética pública"],
            "method": "Contrasta normas, indicadores, actores y casos públicos; delibera con reglas y transforma conclusiones en acciones democráticas evaluables.",
            "evidence": "análisis o propuesta individual con marco ciudadano, fuentes, contrapunto, decisión ética, viabilidad y límite",
            "domain": "citizenship",
        },
        "ingles-4o-medio": {
            "purpose": "Comprender, producir e interactuar con fluidez reparable en inglés para propósitos específicos, posturas críticas e intercambio entre visiones de mundo.",
            "continuity": "Consolida la comunicación de 3° medio mediante selección autónoma de evidencia, adaptación a audiencia y revisión estratégica del significado.",
            "barrier": "equiparar fluidez con velocidad o acento, traducir literalmente o sostener una postura sin evidencia ni consideración de otras perspectivas",
            "outcomes": ["select relevant information for a purpose", "communicate a respectful critical stance", "use English strategically", "interact fluently across worldviews"],
            "method": "Uses original or authorized input, purposeful information gaps, strategic support, rehearsal, feedback and independent revision.",
            "evidence": "comprehensible independent response that selects evidence, adapts language to purpose, engages another viewpoint and repairs meaning",
            "domain": "english",
        },
        "lengua-literatura-4o-medio": {
            "purpose": "Interpretar obras comparativamente, evaluar discursos y producir, dialogar e investigar con autonomía, evidencia y responsabilidad ética.",
            "continuity": "Consolida aprendizajes de 3° medio mediante comparación de contextos, criterios explícitos, lectura ideológica y producción multimodal autónoma.",
            "barrier": "formular interpretaciones o juicios sin criterio, atribuir intenciones sin evidencia o revisar solo la superficie del texto",
            "outcomes": ["comparar interpretaciones y efectos estéticos", "evaluar discursos y posicionamientos", "producir y revisar textos multimodales", "dialogar e investigar con fuentes"],
            "method": "Trabaja con corpus atribuidos, criterios visibles, evidencia acotada, contraste de lecturas, escritura por procesos y uso ético de fuentes.",
            "evidence": "interpretación, análisis o producción individual con criterio, evidencia textual y contextual, decisiones discursivas y revisión",
            "domain": "language",
        },
        "matematica-4o-medio": {
            "purpose": "Fundamentar decisiones financieras y estadísticas y construir modelos funcionales y geométricos con representaciones, comprobación y límites.",
            "continuity": "Integra modelación, probabilidad, funciones y geometría de 3° medio en decisiones más autónomas y problemas cercanos al egreso.",
            "barrier": "aplicar fórmulas o herramientas digitales sin condiciones, interpretación, comprobación, análisis de sensibilidad ni límites del modelo",
            "outcomes": ["fundamentar decisiones financieras", "decidir bajo incerteza", "construir modelos funcionales", "resolver geometría analítica"],
            "method": "Intercala problemas con datos trazables, representaciones múltiples, estimación, tecnología verificable, argumentación y análisis de límites.",
            "evidence": "resolución o modelo individual con datos, condiciones, representaciones, estrategia, interpretación, comprobación y límite",
            "domain": "mathematics",
        },
    }
)


COUNTS: dict[tuple[str, str], int] = {}
for item in CATALOG["classes"]:
    if item["course_order"] == 12:
        key = (item["subject_slug"], item["oa_code"])
        COUNTS[key] = COUNTS.get(key, 0) + 1

RECORDS: dict[str, dict] = {}
for source_record in SNAPSHOT["records"]:
    slug = source_record["subject_slug"]
    if source_record["course_order"] != 12:
        continue
    topics = TOPICS_BY_SUBJECT.get(slug, [])
    if len(topics) != len(source_record["objectives"]):
        raise RuntimeError(f"{slug}: {len(topics)} temas para {len(source_record['objectives'])} OA oficiales")
    for topic, objective in zip(topics, source_record["objectives"]):
        RECORDS[objective["code"]] = {
            "slug": slug,
            "subject": source_record["subject"],
            "axis": objective["axis"],
            "description": objective["description"],
            "url": objective["url"],
            "count": COUNTS[(slug, objective["code"])],
            "topic": topic,
        }

if set(TOPICS_BY_SUBJECT) != set(SUBJECT_PROFILES):
    raise RuntimeError("Los perfiles y temas de asignatura de 4° medio no coinciden")
if len(RECORDS) != 91 or sum(item["count"] for item in RECORDS.values()) != 466:
    raise RuntimeError(
        f"Cobertura de 4° medio inesperada: {len(RECORDS)} OA, "
        f"{sum(item['count'] for item in RECORDS.values())} clases"
    )


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    record = RECORDS[code]
    sequence = build_sequence_from_record(code, record, SUBJECT_PROFILES[record["slug"]], "3° medio")
    for lesson in sequence["lessons"]:
        if lesson["goal"].startswith("Today I will"):
            lesson["goal"] = lesson["goal"].rstrip(".") + "; I will work independently and state the limits of my response."
            lesson["extension"] += " Complete the transfer with less scaffolding and justify which support is no longer necessary."
        else:
            lesson["goal"] = lesson["goal"].rstrip(".") + "; trabajaré con autonomía y explicitaré los límites de mi respuesta."
            lesson["extension"] += " Realiza la transferencia con menor andamiaje y justifica qué apoyo ya no resulta necesario."
    return sequence


SEQUENCES = {code: True for code in RECORDS}
