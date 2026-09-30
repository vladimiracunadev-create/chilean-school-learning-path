"""Deterministic, classroom-facing enrichment for developed lessons.

The source modules define disciplinary progressions. This layer adds the
concrete artefact, exact prompt, response reference, assessment anchors and a
real 45-minute distribution that every published lesson must expose.
"""
from __future__ import annotations

import hashlib
import re


LEVELS = (
    ("Aún no observable", "No produce evidencia suficiente o responde sin relacionarla con la consigna."),
    ("En desarrollo", "Responde parcialmente y necesita apoyo para usar el criterio o la evidencia."),
    ("Logrado", "Responde la consigna, usa el criterio central y deja una evidencia comprensible."),
    ("Profundizado", "Justifica, contrasta o transfiere la decisión a una condición nueva."),
)


def _seed(code: str, lesson_number: int) -> int:
    digest = hashlib.sha256(f"{code}:{lesson_number}".encode("utf-8")).hexdigest()
    return int(digest[:8], 16)


def _clean(value: str) -> str:
    value = re.sub(r"\s+,", ",", value)
    value = value.replace(",,", ",").replace("..", ".")
    value = value.replace("Modela cómo modelar un criterio:", "Hace visible el criterio de análisis:")
    value = value.replace(", no por imitar el ejemplo", " y con evidencia propia")
    value = value.replace("no por imitar el ejemplo", "con evidencia propia")
    value = value.replace("no se transfiere mecánicamente a otro OA", "se contrasta con el criterio particular de este OA")
    value = re.sub(r"^Desarrollar (.+?) mediante (.+?), con ", r"Enseñar \1 a través de \2, con ", value)
    return re.sub(r"\s{2,}", " ", value).strip()


def _clean_nested(value):
    if isinstance(value, str):
        return _clean(value)
    if isinstance(value, list):
        return [_clean_nested(item) for item in value]
    if isinstance(value, dict):
        return {key: _clean_nested(item) for key, item in value.items()}
    return value


def _math(topic: str, focus: str, seed: int, grade: int) -> dict:
    if grade <= 1:
        a, b, c = 4 + seed % 8, 2 + seed % 3, 1 + seed % 3
    elif grade == 2:
        a, b, c = 12 + seed % 29, 2 + seed % 5, 1 + seed % 5
    else:
        a, b, c = 12 + seed % 19, 3 + seed % 7, 2 + seed % 5
    lowered = f"{topic} {focus}".lower()
    if any(word in lowered for word in ("conteo", "contar", "cardinal")):
        total = min(15, a + b + c) if grade == 1 else a + b + c
        resource = f"Colección de {total} fichas, bandeja con zonas «por contar/contado» y tarjeta numeral {total}."
        prompt = f"Cuenta las {total} fichas sin omitir ni repetir, registra el total y compruébalo después de cambiar su disposición."
        reference = f"Debe asignar una palabra número a cada ficha, declarar {total} como cardinal y conservar el total al reorganizar la colección."
    elif "fracc" in lowered:
        a, b = 2 + seed % 5, 6 + seed % 7
        resource = f"Tarjeta A: {a}/{b}; tarjeta B: {(a + 1)}/{b}; rectángulo dividido en {b} partes iguales."
        prompt = f"Representa {a}/{b}, compáralo con {(a + 1)}/{b} y explica qué permanece igual y qué cambia."
        reference = f"Una respuesta lograda representa {a} y {a + 1} partes de un mismo entero dividido en {b}, usa < y justifica con la unidad común."
    elif any(word in lowered for word in ("porcentaje", "porcent")):
        percent, whole = (10 + seed % 7) * 5, (4 + seed % 5) * 20
        resource = f"Cuadrícula de 100 casillas y tarjeta de situación: calcular {percent}% de {whole}."
        prompt = f"Representa {percent}% en la cuadrícula, calcula {percent}% de {whole} por dos vías y comprueba que coinciden."
        reference = f"Debe relacionar {percent}% con {percent}/100 y obtener {percent * whole // 100}; la segunda vía puede usar 10%, 5% o proporcionalidad."
    elif any(word in lowered for word in ("área", "perímetro", "ángulo", "geometr")):
        width, height = 4 + seed % 8, 3 + seed % 6
        resource = f"Rectángulo cuadriculado de {width} por {height} unidades, regla y una variante con una dimensión duplicada."
        prompt = f"Representa la figura, calcula las medidas pertinentes y predice qué cambia al duplicar el lado de {width} unidades."
        reference = f"La respuesta muestra operaciones con {width} y {height}, rotula unidades y distingue qué medida cambia de manera aditiva o multiplicativa."
    elif any(word in lowered for word in ("dato", "gráfico", "probab", "azar")):
        values = [c + ((seed >> shift) % 7) for shift in (0, 3, 6, 9)]
        resource = "Tabla de frecuencias: A={0}, B={1}, C={2}, D={3}; cuatro tarjetas para representar los mismos datos.".format(*values)
        prompt = "Construye una representación, formula una afirmación verificable y señala el dato que podría hacerla falsa."
        reference = "La representación conserva las cuatro frecuencias, incluye escala y la conclusión cita al menos dos valores de la tabla."
    else:
        if grade <= 2:
            values = (a, a + b, a + b + c)
        else:
            values = (a, a * b, a * b + c)
        resource = f"Tarjetas numéricas {values[0]}, {values[1]}, {values[2]} y una recta numérica sin completar."
        prompt = f"Ordena y relaciona {values[0]}, {values[1]} y {values[2]}; resuelve una situación que use las tres cantidades y comprueba con otra representación."
        reference = "La solución usa las tres cantidades, muestra un procedimiento reproducible y comprueba sin repetir exactamente el mismo cálculo."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _language(topic: str, focus: str, seed: int) -> dict:
    names = ("Amaya", "Benjamín", "Camila", "Diego", "Elena", "Fabián")
    name = names[seed % len(names)]
    object_name = ("cuaderno", "semillero", "mapa", "afiche", "grabación", "maqueta")[seed % 6]
    microtext = (f"{name} encontró un {object_name} sin firma junto a la biblioteca. Antes de usarlo, preguntó quién lo había creado, "
                 "comparó dos pistas y dejó una nota para devolverlo. Al final descubrió que la primera explicación no bastaba.")
    return {
        "resource": f"Microtexto original del proyecto: «{microtext}»",
        "prompt": f"Trabaja el foco «{focus.lower()}»: marca dos evidencias del microtexto, formula una interpretación o producción y revisa una decisión para su audiencia.",
        "reference": "Una respuesta lograda cita o parafrasea dos pistas distintas, conecta ambas con su interpretación y explica una revisión; un resumen sin inferencia no basta.",
    }


def _science(topic: str, focus: str, seed: int) -> dict:
    start = 2 + seed % 5
    values_a = [start, start + 2, start + 5, start + 7]
    values_b = [start, start + 1, start + 2, start + 3]
    return {
        "resource": (f"Registro de indagación para «{topic}»: tiempos 0, 5, 10 y 15 min; condición A={values_a}; "
                     f"condición B={values_b}. La fuente se rotula como conjunto didáctico simulado, no como medición real."),
        "prompt": f"Para «{focus.lower()}», identifica variable independiente, variable observada y dos constantes; compara A y B usando valores y escribe una limitación del registro.",
        "reference": "Debe nombrar qué cambia entre A y B, citar al menos dos pares de valores, mantener dos condiciones constantes y no presentar el patrón como prueba causal definitiva.",
    }


def _history(topic: str, focus: str, seed: int) -> dict:
    lowered = topic.lower()
    if any(word in lowered for word in ("derecho", "ciudad", "democr", "particip", "conviv")):
        resource = ("Caso cívico ficticio: un consejo debe decidir entre publicar de inmediato una medida o abrir una consulta accesible de dos días. "
                    "Tarjetas de actores: autoridad, dos organizaciones vecinales y una persona que requiere apoyo de acceso.")
        prompt = f"Para «{focus.lower()}», identifica derecho, responsabilidad y dos perspectivas; propone una decisión, su resguardo y una forma pública de rendir cuenta."
        reference = "La respuesta distingue derecho e interés, incorpora al menos dos perspectivas, propone un mecanismo realizable y explica cómo evita excluir o exponer a una persona."
    elif any(word in lowered for word in ("territ", "región", "paisaje", "clima", "ambiente", "mapa", "geograf")):
        resource = ("Mapa didáctico esquemático con norte, escala y tres zonas A, B y C; tabla asociada: distancia al agua 2/8/15 km, "
                    "pendiente baja/media/alta y población 40/25/10. Datos simulados para aprender a argumentar, no para describir un lugar real.")
        prompt = f"Aplica «{focus.lower()}»: compara dos zonas con tres datos, formula una decisión territorial y señala qué información falta antes de aplicarla a un lugar real."
        reference = "La respuesta cita al menos tres valores o rasgos, relaciona ubicación y decisión y declara una limitación; no convierte el mapa simulado en información de Chile."
    else:
        resource = (f"Dos tarjetas de interpretación creadas para la clase sobre «{topic}», no fuentes primarias: A afirma que un proceso tiene una sola causa y ocurre igual en todos los territorios; "
                    "B propone contrastar antecedentes, actores, ritmos y lugares. Matriz con columnas afirmación, evidencia necesaria, perspectiva y límite.")
        prompt = f"Aplica «{focus.lower()}»: compara A y B, identifica dos supuestos y escribe qué fuentes verificables necesitarías antes de sostener una conclusión histórica."
        reference = "La respuesta reconoce que ambas tarjetas son interpretaciones didácticas, cuestiona la causa única, pide al menos dos fuentes identificables y limita la conclusión hasta revisarlas."
    return {"resource": resource, "prompt": prompt, "reference": reference}


def _english(topic: str, focus: str, seed: int) -> dict:
    place = ("library", "school garden", "sports court", "community centre")[seed % 4]
    dialogue = f"A: What do we need for the {place}? B: We need a clear plan. A: I can bring the list. B: Great. Let's check it together."
    return {
        "resource": f"Original classroom dialogue: “{dialogue}”",
        "prompt": f"Use the dialogue to work on “{focus.lower()}”. Underline two useful chunks, change one detail and perform or write a new exchange that keeps the meaning clear.",
        "reference": "A successful response reuses two meaningful chunks, changes the place or contribution coherently and remains understandable; accent imitation is not required.",
    }


def _arts(topic: str, focus: str, seed: int) -> dict:
    constraints = (("two colours", "repeated line", "paper texture"), ("warm/cool contrast", "one geometric form", "reused cardboard"), ("foreground/background", "three values", "collage"))[seed % 3]
    return {
        "resource": f"Brief de creación: comunicar «{topic}» usando {constraints[0]}, {constraints[1]} y {constraints[2]}; hoja de pruebas y ficha de autoría.",
        "prompt": f"Realiza dos pruebas pequeñas para «{focus.lower()}», elige una con un criterio visible, desarrolla la obra y anota una decisión que cambió durante el proceso.",
        "reference": "La evidencia incluye dos pruebas distintas, una elección justificada, una producción propia y una explicación basada en elementos visuales, no solo en gusto o parecido.",
    }


def _music(topic: str, focus: str, seed: int) -> dict:
    pattern = ("TA – ti-ti – TA – silencio", "ti-ti – TA – ti-ti – TA", "TA – TA – ti-ti – silencio")[seed % 3]
    return {
        "resource": f"Patrón musical de trabajo: {pattern}; pulso estable marcado con palmas y dos versiones de dinámica. No requiere reproducir repertorio protegido.",
        "prompt": f"Escucha o interpreta el patrón para «{focus.lower()}», describe dos rasgos audibles, modifica uno y explica cómo cambia el resultado.",
        "reference": "La respuesta mantiene el pulso, identifica ritmo/dinámica con evidencia audible y explica el efecto de una modificación; decir solo “me gusta” no es suficiente.",
    }


def _physical(topic: str, focus: str, seed: int) -> dict:
    seconds = 20 + (seed % 4) * 10
    return {
        "resource": f"Estación delimitada de 4 × 4 m, cuatro conos y cronómetro: {seconds} s de acción, {seconds} s de pausa, tres intentos; variante sin desplazamiento disponible.",
        "prompt": f"Practica «{focus.lower()}» priorizando control, distancia segura y autorregulación; registra una decisión técnica y una señal corporal antes y después.",
        "reference": "Se considera logrado cuando mantiene control y seguridad en dos intentos, ajusta intensidad a una señal corporal y explica una decisión; velocidad sola no acredita logro.",
    }


def _orientation(topic: str, focus: str, seed: int) -> dict:
    cases = (
        "Alex recibe un mensaje que le incomoda y no sabe si pedir ayuda",
        "Sam queda fuera de una decisión grupal y necesita proponer una salida respetuosa",
        "Noa asumió demasiadas tareas y debe renegociar un acuerdo sin culpar a otra persona",
    )
    case = cases[seed % len(cases)]
    return {
        "resource": f"Caso ficticio protegido: {case}. Tarjetas de opciones: detenerse, expresar un límite, buscar apoyo, acordar seguimiento.",
        "prompt": f"Analiza el caso desde «{focus.lower()}»: separa hechos de suposiciones, compara dos opciones y escribe una acción segura y una persona o institución de apoyo.",
        "reference": "La respuesta no exige experiencias personales, distingue hecho/emoción/suposición, anticipa una consecuencia y propone apoyo seguro sin secreto ni culpabilización.",
    }


def _technology(topic: str, focus: str, seed: int) -> dict:
    load = 5 + seed % 8
    return {
        "resource": f"Desafío de diseño: construir con cartón reutilizado, papel y cinta una solución estable para sostener {load} fichas; límite de base 20 × 20 cm y tres pruebas registradas.",
        "prompt": f"Para «{focus.lower()}», define usuario y dos criterios, dibuja con medidas, construye o simula, registra tres pruebas y modifica una sola variable.",
        "reference": f"La solución lograda declara usuario, cumple la base máxima, soporta {load} fichas, registra tres resultados y justifica una mejora con evidencia, no solo por apariencia.",
    }


def _cultural(topic: str, focus: str, seed: int) -> dict:
    return {
        "resource": (f"Ficha situada para «{topic}»: pueblo y territorio, nombre de la fuente comunitaria, persona o institución responsable, fecha, autorización, "
                     "variante lingüística cuando corresponda y límites de circulación. Si esos datos faltan, la actividad se detiene."),
        "prompt": f"Trabaja «{focus.lower()}» únicamente con una fuente autorizada: registra procedencia, distingue lo que la fuente dice de tu interpretación y prepara una devolución respetuosa.",
        "reference": "La respuesta atribuye pueblo, territorio y fuente, no inventa lengua ni generaliza a otros pueblos y declara qué requiere validación de educador tradicional o comunidad.",
    }


def _generic(topic: str, focus: str, seed: int) -> dict:
    options = ("A", "B", "C")
    return {
        "resource": f"Caso didáctico sobre «{topic}» con tres opciones ({', '.join(options)}), una restricción visible y una tabla para registrar decisión, evidencia y revisión.",
        "prompt": f"Resuelve «{focus.lower()}»: elige una opción, cita dos evidencias, explica por qué descartas otra y revisa tu decisión al cambiar una condición.",
        "reference": "La respuesta lograda hace una elección reproducible, usa dos evidencias y modifica la conclusión cuando cambia la condición; participar sin justificar no basta.",
    }


def _artifact(subject_slug: str, topic: str, focus: str, seed: int, grade: int) -> dict:
    if subject_slug == "matematica":
        return _math(topic, focus, seed, grade)
    if subject_slug == "lenguaje-comunicacion":
        return _language(topic, focus, seed)
    if subject_slug == "ciencias-naturales":
        return _science(topic, focus, seed)
    if subject_slug == "historia-geografia-ciencias-sociales":
        return _history(topic, focus, seed)
    if subject_slug in {"ingles", "ingles-propuesta"}:
        return _english(topic, focus, seed)
    if subject_slug == "artes-visuales":
        return _arts(topic, focus, seed)
    if subject_slug == "musica":
        return _music(topic, focus, seed)
    if subject_slug == "educacion-fisica-salud":
        return _physical(topic, focus, seed)
    if subject_slug == "orientacion":
        return _orientation(topic, focus, seed)
    if subject_slug == "tecnologia":
        return _technology(topic, focus, seed)
    if subject_slug == "lengua-cultura-pueblos-originarios-ancestrales":
        return _cultural(topic, focus, seed)
    return _generic(topic, focus, seed)


def enrich_item(item: dict) -> dict:
    """Mutate one generated objective with concrete classroom artefacts."""
    sequence = item.get("developed")
    if not sequence:
        return item
    cleaned_sequence = _clean_nested(sequence)
    sequence.clear()
    sequence.update(cleaned_sequence)
    topic = _clean(sequence.get("topic") or item["topic"])
    sequence["topic"] = topic
    lessons = sequence.get("lessons", [])
    for index, lesson in enumerate(lessons, 1):
        for field, value in list(lesson.items()):
            if isinstance(value, str):
                lesson[field] = _clean(value)
        focus = _clean(lesson.get("title") or item["oa_code"])
        artefact = _artifact(item["subject_slug"], topic, focus, _seed(item["oa_code"], index), item["course_order"])
        lesson["concrete_resource"] = artefact["resource"]
        lesson["exact_prompt"] = artefact["prompt"]
        lesson["response_reference"] = artefact["reference"]
        lesson["assessment_levels"] = [
            {"level": level, "descriptor": f"{descriptor} Referencia de esta clase: {artefact['reference']}" if position == 2 else descriptor}
            for position, (level, descriptor) in enumerate(LEVELS)
        ]
        lesson["timing_45"] = [
            {"minutes": 5, "action": "Activación breve y lectura de la consigna exacta."},
            {"minutes": 8, "action": "Modelado con el insumo concreto y una decisión visible."},
            {"minutes": 12, "action": "Primer intento guiado y retroalimentación según un criterio."},
            {"minutes": 15, "action": "Desempeño individual con evidencia atribuible."},
            {"minutes": 5, "action": "Ticket, clasificación del nivel y decisión posterior."},
        ]
        lesson["teacher_checklist"] = [
            "Preparar el insumo concreto sin datos personales ni material sin autorización.",
            "Ensayar la respuesta de referencia y anticipar al menos un error plausible.",
            "Definir cómo recogerá evidencia individual durante el desempeño.",
            "Comprobar accesibilidad, seguridad y alternativa sin conectividad.",
        ]
        if "Recursos reutilizables para" in lesson.get("materials", ""):
            lesson["materials"] = (
                f"Prepare o proyecte este insumo: {artefact['resource']} Añada pizarra, cuaderno y una copia de la consigna; "
                "compruebe legibilidad, seguridad, procedencia y una alternativa sin conectividad."
            )
        generic_criteria = {
            "responde al foco específico de la clase",
            "usa evidencia disciplinar pertinente y contextualizada",
            "explica una decisión y reconoce límites o revisa un error",
        }
        if generic_criteria.intersection(set(lesson.get("criteria", []))) or any(
            "responde al foco específico de la clase" in criterion for criterion in lesson.get("criteria", [])
        ):
            lesson["criteria"] = [
                f"resuelve la consigna exacta de «{focus.lower()}»",
                "usa al menos dos datos, rasgos o evidencias del insumo concreto",
                "explica una decisión y revisa su respuesta ante una condición nueva",
            ]
    return item

