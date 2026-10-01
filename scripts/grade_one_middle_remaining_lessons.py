"""Complete the five remaining first-year secondary subject sequences.

Official objectives and URLs come from the checked-in MINEDUC snapshot. Topics,
classroom anchors, progressions, misconceptions and safeguarding decisions are
original pedagogical elaborations for this repository.
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
except ImportError:
    from scripts.grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from scripts.grade_three_music_orientation_technology_lessons import _lesson as mot_lesson
    from scripts.grade_four_remaining_lessons import build_transversal_integration as base_integration
    from scripts.grade_seven_next_five_lessons import _natural_voice as physical_voice
    from scripts.grade_seven_remaining_lessons import _natural_voice as remaining_voice


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
TARGET_SLUGS = {"artes-visuales", "musica", "educacion-fisica-salud", "orientacion", "tecnologia"}

TOPICS = {
    "AR1M OA 01": "Arquitectura, espacio público y diseño urbano",
    "AR1M OA 02": "Grabado, pintura mural e investigación de materiales sustentables",
    "AR1M OA 03": "Libro de artista, arte digital e imaginarios personales",
    "AR1M OA 04": "Juicio crítico de manifestaciones visuales en contexto",
    "AR1M OA 05": "Crítica fundamentada de proyectos visuales propios y de pares",
    "AR1M OA 06": "Diseño de difusión artística para la comunidad",
    "MU1M OA 01": "Apreciación de músicas de tradición oral, escrita y popular",
    "MU1M OA 02": "Comparación musical, lenguaje, composición y propósito expresivo",
    "MU1M OA 03": "Interpretación vocal e instrumental con estilo y expresividad",
    "MU1M OA 04": "Interpretación a una y más voces, registro y presentación",
    "MU1M OA 05": "Improvisación, creación y arreglo desde ideas musicales",
    "MU1M OA 06": "Fortalezas, crecimiento y decisiones del trabajo musical",
    "MU1M OA 07": "Música, identidad, cultura y memoria",
    "EF1M OA 01": "Perfeccionamiento de habilidades motrices específicas",
    "EF1M OA 02": "Estrategias y tácticas específicas en juegos y deportes",
    "EF1M OA 03": "Plan personal de entrenamiento para una condición física saludable",
    "EF1M OA 04": "Actividad física regular, autocuidado y primeros auxilios",
    "EF1M OA 05": "Promoción de actividad física en la comunidad",
    "OR1M OA 01": "Alternativas y decisiones para proyectos de vida",
    "OR1M OA 02": "Sexualidad, vínculos afectivos, respeto y responsabilidad",
    "OR1M OA 03": "Evaluación de riesgos, protección y búsqueda de ayuda",
    "OR1M OA 04": "Acciones autónomas para una vida saludable",
    "OR1M OA 05": "Relaciones constructivas presenciales y digitales",
    "OR1M OA 06": "Resolución de conflictos en un marco de derechos",
    "OR1M OA 07": "Participación social e institucional cercana",
    "OR1M OA 08": "Iniciativas de justicia, buen trato y bien común",
    "OR1M OA 09": "Opciones académicas y laborales para proyectos de vida",
    "OR1M OA 10": "Diseño flexible y responsable de proyectos de vida",
    "TE1M OA 01": "Oportunidades y necesidades para crear un servicio",
    "TE1M OA 02": "Desarrollo ético y seguro de un servicio",
    "TE1M OA 03": "Evaluación y mejora técnica y valórica de un servicio",
    "TE1M OA 04": "Comunicación del diseño y desarrollo para distintas audiencias",
    "TE1M OA 05": "Evolución de productos tecnológicos y entornos",
    "TE1M OA 06": "Efectos sociales de la evolución tecnológica",
}

COUNTS = {
    "AR1M OA 01": 5, "AR1M OA 02": 5, "AR1M OA 03": 5, "AR1M OA 04": 4, "AR1M OA 05": 4, "AR1M OA 06": 6,
    "MU1M OA 01": 4, "MU1M OA 02": 4, "MU1M OA 03": 4, "MU1M OA 04": 5, "MU1M OA 05": 5, "MU1M OA 06": 5, "MU1M OA 07": 5,
    "EF1M OA 01": 5, "EF1M OA 02": 6, "EF1M OA 03": 6, "EF1M OA 04": 5, "EF1M OA 05": 6,
    "OR1M OA 01": 5, "OR1M OA 02": 6, "OR1M OA 03": 6, "OR1M OA 04": 5, "OR1M OA 05": 5,
    "OR1M OA 06": 4, "OR1M OA 07": 6, "OR1M OA 08": 5, "OR1M OA 09": 4, "OR1M OA 10": 6,
    "TE1M OA 01": 4, "TE1M OA 02": 4, "TE1M OA 03": 5, "TE1M OA 04": 4, "TE1M OA 05": 5, "TE1M OA 06": 4,
}

STAGES = {
    "AR": ("Observar contexto, lenguaje y propósito", "Explorar materiales y referentes", "Probar decisiones visuales", "Desarrollar una propuesta propia", "Contrastar con criterios", "Revisar, montar y comunicar"),
    "MU": ("Escuchar y reconocer rasgos", "Relacionar lenguaje, contexto y propósito", "Ensayar una decisión musical", "Interpretar, improvisar o crear", "Registrar y contrastar versiones", "Evaluar y comunicar el proceso"),
    "EF": ("Explorar con seguridad y diagnóstico", "Seleccionar una respuesta motriz", "Combinar habilidades o decisiones", "Aplicar estrategia o plan", "Evaluar y ajustar con evidencia", "Transferir con autonomía"),
    "OR": ("Examinar un caso ficticio protegido", "Distinguir hechos, derechos y límites", "Comparar opciones y consecuencias", "Elegir una acción segura", "Practicar comunicación o búsqueda de ayuda", "Transferir sin exposición personal"),
    "TE": ("Definir necesidad, usuario y criterio", "Investigar soluciones y restricciones", "Representar y planificar", "Implementar con seguridad", "Probar con evidencia", "Mejorar y comunicar impactos"),
}

PRIOR = {
    "AR": "crear, apreciar y argumentar decisiones visuales con contexto, materialidad y autoría en 8° básico",
    "MU": "escuchar, interpretar, crear y evaluar música mediante evidencia audible y contexto en 8° básico",
    "EF": "seleccionar habilidades, regular el esfuerzo y participar con seguridad e inclusión en 8° básico",
    "OR": "analizar decisiones, derechos, autocuidado y participación mediante casos protegidos de 8° básico",
    "TE": "definir necesidades, diseñar, probar y evaluar soluciones tecnológicas en 8° básico",
}

VOCABULARY = {
    "AR": "contexto, referente, lenguaje visual, materialidad, composición, propósito, autoría, criterio, montaje, difusión",
    "MU": "pulso, ritmo, melodía, armonía, textura, timbre, forma, estilo, arreglo, expresividad, identidad",
    "EF": "habilidad motriz, estrategia, táctica, frecuencia, intensidad, recuperación, progresión, seguridad, inclusión, autorregulación",
    "OR": "dignidad, derecho, intimidad, consentimiento, riesgo, autocuidado, consecuencia, apoyo, participación, proyecto de vida",
    "TE": "necesidad, usuario, servicio, criterio, restricción, prototipo, prueba, seguridad, ética, impacto, mejora",
}

MISCONCEPTIONS = {
    "AR": ("copiar un referente sin transformar decisiones", "confundir gusto personal con juicio fundamentado", "difundir obras sin consentimiento, crédito ni cuidado del espacio"),
    "MU": ("confundir calidad musical con volumen o velocidad", "imitar una versión sin reconocer estilo ni tomar decisiones", "evaluar a una persona en vez de la evidencia audible y el proceso"),
    "EF": ("confundir dominio con rendimiento competitivo", "usar una misma carga o variante para todo el curso", "evaluar solo el resultado y no la regulación, estrategia o seguridad"),
    "OR": ("pedir experiencias personales para demostrar aprendizaje", "moralizar, culpar o diagnosticar a una persona", "resolver seguridad mediante secreto, obediencia o exposición pública"),
    "TE": ("construir antes de definir necesidad, usuario y criterios", "evaluar solo apariencia o funcionamiento inmediato", "usar datos, imágenes o herramientas sin revisar privacidad, autoría y seguridad"),
}


def _anchor(code: str, topic: str) -> str:
    prefix = code[:2]
    if prefix == "AR":
        return {
            "AR1M OA 01": "mapas, fotografías atribuidas, planos y recorridos de espacios públicos, más tarjetas de uso, acceso, memoria e impacto urbano",
            "AR1M OA 02": "matrices de grabado escolar, pigmentos seguros, cartón, papel y materiales reutilizados limpios con fichas de origen y descarte",
            "AR1M OA 03": "libros de artista, secuencias visuales y medios digitales sin cuenta, con banco de imágenes propias o autorizadas",
            "AR1M OA 04": "dossier de manifestaciones visuales atribuidas con autoría, fecha, lugar, medio, audiencia y contexto",
            "AR1M OA 05": "bitácoras y proyectos ficticios o propios con criterios de contexto, materialidad, lenguaje visual y propósito",
            "AR1M OA 06": "planos de montaje, fichas de obra, audiencias ficticias y opciones de difusión directa o virtual con consentimiento y créditos",
        }[code]
    if prefix == "MU":
        if code in {"MU1M OA 01", "MU1M OA 02", "MU1M OA 07"}:
            return f"registros musicales autorizados y contrastados, con intérprete, fecha, lugar, contexto y mapa de escucha para {topic.lower()}"
        if code in {"MU1M OA 03", "MU1M OA 04"}:
            return f"partitura convencional o gráfica, grabación autorizada, pistas por voces e instrumentos disponibles a volumen seguro para {topic.lower()}"
        if code == "MU1M OA 05":
            return "células rítmicas y melódicas, instrumentos disponibles o aplicación sin cuenta, partitura gráfica y límites claros para improvisar y arreglar"
        return "dos registros de ensayo, pauta de autoescucha y criterios audibles de coordinación, técnica, expresividad y aporte colectivo"
    if prefix == "EF":
        return {
            "EF1M OA 01": "estaciones accesibles de deporte individual, oposición, colaboración, oposición-colaboración y danza con variantes equivalentes",
            "EF1M OA 02": "juegos reducidos, mapas de espacio, reglas modificables y registro de decisiones tácticas antes y después de una pausa",
            "EF1M OA 03": "perfiles ficticios, circuito regulable, escala de esfuerzo percibido y ficha FITT con recuperación y progresión",
            "EF1M OA 04": "plan de práctica en entornos diversos, protocolo de autocuidado, rutas seguras y casos simulados de primeros auxilios",
            "EF1M OA 05": "consulta anónima de intereses, mapa de recursos comunitarios y plan inclusivo para una actividad física escolar",
        }[code]
    if prefix == "OR":
        if code in {"OR1M OA 01", "OR1M OA 09", "OR1M OA 10"}:
            return f"perfiles y trayectorias ficticias, opciones formativas o laborales, matriz de intereses, apoyos, límites y decisiones reversibles para {topic.lower()}"
        if code in {"OR1M OA 02", "OR1M OA 03", "OR1M OA 04"}:
            return f"casos ficticios en tercera persona, tarjetas de derechos y consentimiento, semáforo de riesgo y rutas institucionales de ayuda para {topic.lower()}"
        return f"situaciones presenciales o digitales ficticias, mapa de actores, derechos, acuerdos, reparación y redes de apoyo para {topic.lower()}"
    return f"desafío de servicio ficticio, ficha de usuario, recursos digitales sin cuenta, criterios de prueba y matriz ética, social y ambiental para {topic.lower()}"


RECORDS = {}
for record in SNAPSHOT["records"]:
    if record["course_order"] != 9 or record["subject_slug"] not in TARGET_SLUGS:
        continue
    for objective in record["objectives"]:
        if objective["code"].startswith("de "):
            continue
        RECORDS[objective["code"]] = {
            "slug": record["subject_slug"], "description": objective["description"],
            "url": objective["url"], "count": COUNTS[objective["code"]],
        }

if set(RECORDS) != set(TOPICS):
    raise RuntimeError(f"Perfiles restantes de 1° medio desalineados: faltan={sorted(set(RECORDS)-set(TOPICS))}; sobran={sorted(set(TOPICS)-set(RECORDS))}")


def _profile(code: str) -> dict:
    prefix = code[:2]
    topic = TOPICS[code]
    seed = sum(ord(char) for char in code)
    return {
        "topic": topic, "prior": PRIOR[prefix], "vocabulary": VOCABULARY[prefix],
        "anchor": _anchor(code, topic), "misconception": MISCONCEPTIONS[prefix][seed % 3],
        "focuses": [f"{stage}: {topic}" for stage in STAGES[prefix][:COUNTS[code]]],
    }


def _retarget_links(lesson: dict, prefix: str) -> None:
    old = {"AR": "AR03", "MU": "MU03", "EF": "EF03", "OR": "OR03", "TE": "TE03"}[prefix]
    new = {"AR": "AR1M", "MU": "MU1M", "EF": "EF1M", "OR": "OR1M", "TE": "TE1M"}[prefix]
    for link in lesson.get("transversal", []):
        link["code"] = link["code"].replace(old, new)


def _art_voice(lesson: dict, profile: dict, index: int) -> None:
    """Give first-middle Arts its own visual-arts voice and classroom actions."""
    focus = profile["focuses"][index]
    action = focus[0].lower() + focus[1:]
    anchor = profile["anchor"]
    misconception = profile["misconception"]
    openings = (
        f"Presenta {anchor}. Cada estudiante registra dos rasgos visuales, una relación con el contexto y una pregunta antes de proponer una obra.",
        f"Dispón dos referentes atribuidos de {anchor}. El curso compara una decisión de composición, materialidad o circulación sin ordenarlos por gusto.",
        f"Recorre {anchor} con una pauta breve de observación. Cada estudiante selecciona un detalle y anticipa cómo podría transformarlo sin copiarlo.",
        f"Muestra una propuesta visual en proceso vinculada con {anchor}. El curso distingue intención, decisión visible y aspecto todavía abierto.",
        f"Cambia audiencia, escala o lugar de exhibición en {anchor}. El curso anticipa qué decisión visual debería revisarse y por qué.",
    )
    models = (
        f"Modela cómo {action}: observa el contexto, formula una intención y prueba una decisión de composición, material o lenguaje visual.",
        "Realiza dos ensayos breves cambiando una sola variable visual. Compara sus efectos y conserva el intento descartado como evidencia del proceso.",
        f"Examina la confusión «{misconception}». Sustituye el juicio general por detalles observables, contexto y un criterio acordado.",
        "Construye una respuesta visual parcial desde un referente atribuido: transforma relaciones de forma, color, textura o espacio sin reproducir la obra.",
        "Modela retroalimentación visual: describe lo que se observa, cita el criterio y propone una revisión que preserve la autoría de quien crea.",
    )
    lesson["purpose"] = f"Acompañar al curso a {action} mediante observación situada, exploración material y decisiones visuales propias."
    lesson["goal"] = f"Hoy voy a {action}; justificaré una decisión visual con un referente, un criterio y evidencia del proceso."
    lesson["opening"] = openings[index % len(openings)]
    lesson["model"] = models[index % len(models)]
    lesson["guided"] = f"En parejas o estaciones realizan dos pruebas visuales con {anchor}. Comparan efectos mediante un criterio preciso y cada autor decide qué incorporar."
    lesson["independent"] = f"Cada estudiante desarrolla una respuesta propia para {action}. Registra una decisión, una revisión y la relación entre contexto, lenguaje visual y propósito."
    lesson["ticket"] = "Presenta una decisión visual, señala la evidencia que la sostiene y explica qué conservaría o revisaría en una nueva versión."
    lesson["evidence"] = f"Producción o análisis visual propio para «{focus.lower()}», con referente atribuido, registro de proceso y justificación disciplinar."
    lesson["criteria"] = [
        "relaciona la propuesta con el contexto y el propósito trabajado",
        "toma una decisión visible de lenguaje, composición o materialidad",
        "fundamenta con evidencia del referente o del proceso y revisa sin perder autoría",
    ]
    lesson["next_step"] = "Avanza cuando intención, decisión visual y evidencia coinciden; si no, compara dos pruebas acotadas y vuelve a decidir sin imponer un modelo estético."


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    prefix = code[:2]
    profile = _profile(code)
    lessons = []
    for index in range(len(profile["focuses"])):
        lesson = applied_lesson(code, index, profile) if prefix in {"AR", "EF"} else mot_lesson(code, index, profile)
        _retarget_links(lesson, prefix)
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
            f"{profile['topic']} parte de {profile['prior']} y avanza con decisiones propias de la disciplina. "
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
    result["generated_for"] = "1-medio-remaining"
    return result


SEQUENCES = {code: True for code in RECORDS}
