"""Specific third-grade Music, Orientation and Technology sequences."""
from __future__ import annotations


ATTITUDES = {
    "MU": (
        ("de Actitud MU03 OAA A", "curiosidad y disfrute ante sonidos y música"),
        ("de Actitud MU03 OAA B", "confianza progresiva al compartir música"),
        ("de Actitud MU03 OAA C", "comunicación de percepciones, ideas y sentimientos mediante música"),
        ("de Actitud MU03 OAA D", "valoración de estilos y expresiones musicales diversos"),
        ("de Actitud MU03 OAA E", "reconocimiento respetuoso de dimensiones espirituales y trascendentes de la música"),
        ("de Actitud MU03 OAA F", "creatividad mediante juego, experimentación e imaginación sonora"),
        ("de Actitud MU03 OAA G", "participación y colaboración respetuosa en experiencias musicales"),
    ),
    "TE": (
        ("de Actitud TE03 OAA A", "curiosidad por usos, funcionamiento y materiales tecnológicos"),
        ("de Actitud TE03 OAA B", "creatividad mediante experimentación y pensamiento divergente"),
        ("de Actitud TE03 OAA C", "iniciativa en diseño y creación tecnológica"),
        ("de Actitud TE03 OAA D", "colaboración y recepción de retroalimentación"),
        ("de Actitud TE03 OAA E", "uso seguro y responsable de internet y respeto de autoría"),
    ),
}


def _p(topic: str, prior: str, vocabulary: str, anchor: str, misconception: str, focuses: str) -> dict:
    return {
        "topic": topic,
        "prior": prior,
        "vocabulary": vocabulary,
        "anchor": anchor,
        "misconception": misconception,
        "focuses": [focus.strip() for focus in focuses.split("|")],
    }


MU = {
    "MU03 OA 01": _p("Cualidades del sonido y organización musical", "reconocer pulso y contrastes sonoros básicos", "altura, timbre, intensidad, duración, pulso, acento, patrón, sección", "audiciones breves y producciones corporales o instrumentales a volumen seguro", "nombrar elementos sin localizarlos en lo escuchado o confundir altura con intensidad", "Localizar cualidades del sonido|Reconocer pulso, acento y patrón|Comparar repetición, contraste y variación|Representar dinámica y tempo|Distinguir secciones A, AB y ABA"),
    "MU03 OA 02": _p("Respuestas elaboradas a la música escuchada", "expresar una sensación mediante palabra, gesto o imagen", "sensación, emoción, idea, gesto, imagen, movimiento, evidencia sonora", "una audición identificada y dos medios expresivos disponibles", "atribuir una emoción universal a la obra o decorar sin referirse al sonido", "Separar lo escuchado de lo imaginado|Expresar mediante cuerpo y movimiento|Traducir una cualidad a imagen|Construir una respuesta multimodal"),
    "MU03 OA 03": _p("Escucha abundante de músicas de diversos contextos", "escuchar respetando silencio, turnos y volumen", "tradición escrita, raíz folclórica, popular, contexto, intérprete, fuente, escucha", "selección atribuida y autorizada de músicas chilenas y del mundo", "ordenar estilos como superiores o presentar una pieza como representación total de una cultura", "Escuchar tradición escrita con contexto|Escuchar música inspirada en raíces folclóricas|Escuchar música popular situada|Comparar sin jerarquizar estilos|Construir una bitácora de escucha diversa"),
    "MU03 OA 04": _p("Canto e interpretación instrumental coordinada", "mantener pulso, seguir señales y cuidar la voz e instrumentos", "unísono, canon, entrada, pulso, frase, percusión, instrumento melódico", "repertorio apropiado a tesitura y recursos disponibles, con volumen y pausas seguros", "premiar sólo potencia o exactitud y exponer individualmente a quien necesita ensayo", "Afinar escucha y respiración en unísono|Sostener una parte en canon simple|Coordinar percusión con pulso y acentos|Integrar voz e instrumento en una interpretación"),
    "MU03 OA 05": _p("Improvisación y creación con propósito musical", "explorar sonidos y repetir un patrón breve", "improvisar, crear, motivo, contraste, variación, propósito, estructura", "paleta limitada de sonidos corporales, vocales, objetos o instrumentos seguros", "confundir improvisar con tocar sin escuchar ni respetar restricciones", "Improvisar dentro de una consigna|Crear un motivo reconocible|Variar una cualidad conservando identidad|Organizar pregunta y respuesta|Construir y revisar una pieza breve"),
    "MU03 OA 06": _p("Presentación musical responsable ante otros", "ensayar entradas, cierres y cuidado del material", "presentación, audiencia, ensayo, rol, señal, programa, retroalimentación", "presentación breve con roles flexibles y alternativa a la exposición solista", "equiparar compromiso con perfección o forzar actuación pública", "Definir propósito, audiencia y roles|Ensayar por secciones con evidencia|Ajustar transiciones y cuidado sonoro|Presentar y recoger retroalimentación"),
    "MU03 OA 07": _p("Experiencias musicales en vida y sociedad", "reconocer músicas en situaciones cotidianas", "celebración, reunión, festividad, cotidiano, función, contexto, experiencia", "casos ficticios y fuentes atribuidas; compartir experiencias personales es opcional", "suponer la misma función para toda música o exigir revelar prácticas familiares", "Mapear sonidos de situaciones cotidianas|Relacionar música y celebración|Comparar funciones sociales|Documentar una experiencia sin generalizar"),
    "MU03 OA 08": _p("Reflexión sobre escucha, interpretación y creación", "describir una decisión y recibir comentarios", "fortaleza, área de mejora, criterio, evidencia, estrategia, ensayo, progreso", "registros propios breves y criterios conocidos antes de evaluar", "convertir la reflexión en juicio sobre talento, voz o personalidad", "Identificar una fortaleza con evidencia|Localizar un área de mejora|Elegir una estrategia de práctica|Comprobar progreso y siguiente paso"),
}


OR = {
    "OR03 OA 01": _p("Características, habilidades, fortalezas y metas de mejora", "nombrar intereses y aprendizajes sin compararse", "característica, habilidad, fortaleza, evidencia, meta, acción, progreso", "perfiles ficticios y opción de trabajar con un personaje", "convertir una característica en etiqueta fija o pedir información íntima", "Describir sin etiquetar|Reconocer habilidades con evidencia|Valorar fortalezas diversas|Proponer una acción concreta de mejora"),
    "OR03 OA 02": _p("Aceptación y manejo de emociones", "distinguir emoción, sensación y conducta", "emoción, intensidad, aceptación, estrategia, impacto, escucha, regulación", "situaciones ficticias y escala visual; nadie debe contar experiencias privadas", "clasificar emociones como buenas o malas o decidir lo que otra persona siente", "Identificar emoción y señales con cautela|Aceptar emoción y limitar conductas dañinas|Practicar espera y regulación|Escuchar y considerar impacto"),
    "OR03 OA 03": _p("Sexualidad como vínculo, amor, intimidad y origen de la vida", "reconocer afecto, cuidado, intimidad y límites corporales", "sexualidad, vínculo, amor, intimidad, consentimiento, cuidado, origen de la vida", "lenguaje claro y adecuado a la edad, casos ficticios y protocolo institucional", "reducir sexualidad a anatomía, imponer un modelo familiar o solicitar relatos personales", "Distinguir dimensiones de la sexualidad|Reconocer vínculos respetuosos diversos|Comprender intimidad, consentimiento y límites|Explicar el origen de la vida con lenguaje adecuado"),
    "OR03 OA 04": _p("Autocuidado autónomo, intimidad y protección", "aplicar rutinas de higiene, descanso, movimiento y ayuda", "higiene, descanso, alimentación, intimidad, información personal, seguridad, apoyo", "casos ficticios, protocolo escolar y red institucional de ayuda", "responsabilizar al niño por recursos familiares o enseñar secretos sobre seguridad corporal", "Planificar rutinas flexibles de autocuidado|Equilibrar descanso, recreación y actividad|Cuidar alimentación sin culpa ni control corporal|Resguardar cuerpo, intimidad e información|Aplicar parar, alejarse, contar y seguir contando"),
    "OR03 OA 05": _p("Solidaridad, empatía, buen trato y rechazo de violencia", "usar turnos, peticiones y reparación en convivencia", "empatía, solidaridad, buen trato, violencia, discriminación, inclusión, reparación", "casos ficticios diferenciando conflicto, accidente, agresión y discriminación", "tratar violencia como desacuerdo entre iguales o forzar reconciliación", "Comprender otra perspectiva sin hablar por ella|Practicar buen trato observable|Actuar solidariamente sin sustituir|Rechazar violencia y discriminación|Incluir y reparar con seguridad"),
    "OR03 OA 06": _p("Resolución guiada de conflictos entre pares", "separar hechos, interpretaciones, emociones y necesidades", "conflicto, perspectiva, escucha, opción, acuerdo, reparación, mediación", "historias ficticias; nunca se media violencia real en la clase", "buscar culpable antes de comprender o exigir un acuerdo que expone a alguien", "Reconstruir hechos y perspectivas|Escuchar y reformular necesidades|Proponer opciones compatibles con derechos|Acordar, reparar y pedir ayuda cuando corresponde"),
    "OR03 OA 07": _p("Participación y responsabilidades en comunidad escolar", "proponer ideas y cumplir un rol breve", "iniciativa, participación, responsabilidad, derecho, rol, distribución, seguimiento", "proyecto ficticio de curso con roles accesibles y rotativos", "confundir participar con dirigir o asignar roles por género, popularidad o habilidad", "Proponer y recibir iniciativas|Decidir con reglas claras|Distribuir roles con equidad|Cumplir y evaluar responsabilidades"),
    "OR03 OA 08": _p("Hábitos, esfuerzo, honestidad y organización escolar", "preparar materiales y formular una meta pequeña", "puntualidad, plazo, organización, esfuerzo, plagio, autoría, estrategia", "agenda y producciones ficticias; se ofrecen alternativas ante recursos no disponibles", "equiparar cumplimiento con aprendizaje o culpar por condiciones fuera del control infantil", "Organizar tiempo y materiales|Cumplir plazos con un plan ajustable|Respetar el trabajo y concentración ajenos|Distinguir ayuda, copia y plagio|Evaluar esfuerzo, estrategia y siguiente paso"),
}


TE = {
    "TE03 OA 01": _p("Diseño de objetos y sistemas tecnológicos simples", "identificar necesidad, usuario y criterios básicos", "problema, usuario, criterio, restricción, boceto, modelo, TIC, decisión", "casos cercanos y materiales de representación, antes de construir", "elegir un objeto atractivo antes de comprender el problema", "Investigar problema, usuario y contexto|Definir criterios y restricciones|Generar ideas divergentes|Representar a mano alzada|Construir un modelo concreto o digital|Seleccionar y comunicar una propuesta"),
    "TE03 OA 02": _p("Planificación de una elaboración tecnológica segura", "ordenar acciones y distinguir material de herramienta", "plan, secuencia, material, herramienta, técnica, tiempo, seguridad", "objeto de referencia desmontable, tarjetas de pasos y herramientas revisadas", "ordenar por intuición sin reconocer dependencias ni medidas de seguridad", "Descomponer el resultado en tareas|Relacionar materiales, herramientas y técnicas|Ordenar dependencias y puntos de control|Construir un plan seguro y realizable"),
    "TE03 OA 03": _p("Elaboración de un objeto con dominio técnico", "medir, marcar, cortar, plegar y unir bajo indicaciones", "medir, marcar, cortar, plegar, unir, acabado, precisión, seguridad", "papeles, cartones, fibras, plásticos limpios y herramientas escolares apropiadas", "seguir pasos sin comprobar función o elegir herramienta sólo por rapidez", "Comparar materiales según función|Practicar técnicas en retazos|Construir con puntos de control|Integrar acabado sin ocultar fallas|Documentar decisiones y uso seguro"),
    "TE03 OA 04": _p("Prueba y evaluación técnica, ambiental y segura", "distinguir opinión de resultado observable", "prueba, criterio técnico, ambiente, seguridad, dato, falla, iteración", "prototipos, cargas livianas y pauta acordada antes de probar", "evaluar sólo apariencia o cambiar muchas variables simultáneamente", "Definir criterios antes de probar|Aplicar una prueba repetible|Registrar resultados y fallas|Dialogar desde evidencia|Mejorar una variable y volver a probar"),
    "TE03 OA 05": _p("Presentaciones digitales para comunicar ideas", "crear archivos y ordenar texto e imagen con claridad", "diapositiva, propósito, audiencia, jerarquía, imagen, fuente, transición", "software disponible sin cuenta y alternativa equivalente desconectada", "llenar diapositivas de texto o usar efectos como sustituto de organización", "Definir propósito y audiencia|Organizar una secuencia de diapositivas|Combinar texto e imagen propia o autorizada|Presentar y revisar legibilidad"),
    "TE03 OA 06": _p("Creación y edición en procesador de textos", "escribir, corregir y guardar un documento breve", "documento, cursor, selección, párrafo, formato, imagen, guardar, recuperar", "procesador local, carpeta acordada y contenido ficticio sin datos personales", "usar formato decorativo sin jerarquía o guardar sin comprobar recuperación", "Crear y organizar párrafos|Editar mediante selección y movimiento|Aplicar formato que mejora lectura|Insertar un recurso con autoría|Guardar, cerrar y recuperar"),
    "TE03 OA 07": _p("Búsqueda, extracción y almacenamiento seguro de información", "navegar por enlaces docentes y reconocer fuente", "buscador, palabra clave, resultado, fuente, autor, fecha, archivo, privacidad", "sitios previamente seleccionados, navegador protegido y ficha de registro", "usar el primer resultado como verdad, descargar sin revisar o copiar sin atribuir", "Construir una búsqueda específica|Leer resultados antes de abrir|Evaluar fuente y seguridad|Extraer, atribuir y almacenar información"),
}


TABLES = {"MU": MU, "OR": OR, "TE": TE}
SLUGS = {"MU": "musica", "OR": "orientacion", "TE": "tecnologia"}


def _attitude(code: str, index: int, goal: str) -> list[dict[str, str]]:
    pool = ATTITUDES.get(code[:2], ())
    if not pool:
        return []
    seed = int(code.rsplit(" ", 1)[-1])
    attitude_code, description = pool[(seed + index * 2) % len(pool)]
    return [{
        "code": attitude_code,
        "type": "Actitud",
        "application": f"Se promueve {description} durante «{goal}» mediante una acción observable; no se evalúan personalidad, talento, cuerpo, intimidad ni obediencia.",
    }]


def _lesson(code: str, index: int, profile: dict) -> dict:
    prefix = code[:2]
    focus = profile["focuses"][index]
    topic = profile["topic"]
    anchor = profile["anchor"]
    misconception = profile["misconception"]
    goal = f"desarrollaré «{focus.lower()}» y explicaré una decisión con evidencia"
    if prefix == "MU":
        opening = f"Escuchan o producen una vez {anchor} para «{focus.lower()}». Cada estudiante registra un rasgo audible mediante gesto, símbolo o palabra antes de nombrar categorías."
        model = f"Interpreta o reproduce un ejemplo distinto y verbaliza la escucha para {focus.lower()}; aísla pulso, timbre, altura, intensidad, duración o forma y contrasta «{misconception}»."
        guided = f"Por eco, representación o turnos breves practican «{focus.lower()}»; alternan interpretar, escuchar y ajustar un rasgo audible a volumen seguro."
        independent = f"Construye una respuesta, interpretación o creación nueva para «{focus.lower()}»; conserva un criterio musical y revisa el resultado desde la escucha."
        ticket = f"En «{focus.lower()}», interpreta, representa o localiza un rasgo musical y explica qué evidencia audible sostiene la respuesta."
        materials = f"{anchor}; voz, cuerpo, objetos o instrumentos revisados; señal de silencio, distancia y volumen seguro."
        support = "Reduce extensión, mantiene pulso visible, ofrece eco, gesto, notación gráfica y rol vocal, corporal o instrumental equivalente; nunca fuerza exposición solista."
        extension = "Transforma una cualidad o sección manteniendo las demás y anticipa y describe el efecto audible."
        evidence = f"Respuesta, representación, interpretación o creación individual de «{focus.lower()}» con rasgo musical audible y explicación breve."
        coordination = "El docente conduce escucha, interpretación y cuidado auditivo; educación diferencial acuerda acceso sensorial, motor o gráfico sin reemplazar la decisión musical."
    elif prefix == "OR":
        opening = f"Presenta un caso ficticio y protegido para «{focus.lower()}» usando {anchor}. Nadie debe revelar vivencias, cuerpo, familia, identidad o emociones personales para participar."
        model = f"Distingue hechos, emociones, límites, opciones, consecuencias y apoyo adulto en «{focus.lower()}». Usa lenguaje adecuado a la edad y contrasta «{misconception}» sin diagnosticar ni prometer secreto."
        guided = f"En parejas o de forma privada eligen respuestas para «{focus.lower()}», anticipan consecuencias y practican una frase de cuidado, límite, acuerdo, autoría o solicitud de ayuda."
        independent = f"Resuelve individualmente un caso ficticio nuevo sobre «{focus.lower()}»; justifica una decisión segura y señala apoyo adulto o protocolo cuando corresponde."
        ticket = f"Ante «{focus.lower()}», elige una acción, explica qué derecho o criterio protege y nombra cuándo corresponde pedir ayuda sin contar una experiencia propia."
        materials = f"{anchor}; tarjetas de opciones y red institucional de apoyo. No se solicitan datos personales ni demostraciones corporales."
        support = "Ofrece personajes ficticios, opciones visuales, lectura en voz alta y derecho a pasar o responder en privado; deriva situaciones reales al protocolo institucional."
        extension = "Agrega una perspectiva, barrera o límite y revisa la decisión conservando dignidad, consentimiento, seguridad y posibilidad de ayuda."
        evidence = f"Decisión individual ante un caso ficticio de «{focus.lower()}», con razón, límite y apoyo o recurso pertinente."
        coordination = "El docente enseña prevención y convivencia; orientación o convivencia escolar recibe situaciones reales según protocolo. No investiga, media violencia ni expone revelaciones durante la clase."
    else:
        opening = f"Presenta {anchor} como problema abierto para «{focus.lower()}». Cada estudiante registra qué debe lograrse, para quién y una restricción antes de nombrar soluciones."
        model = f"Piensa en voz alta como diseñador para {focus.lower()}: separa necesidad, usuario, decisión, prueba, seguridad y autoría; conserva un intento fallido y contrasta «{misconception}»."
        guided = f"En parejas desarrollan una variante de «{focus.lower()}», registran acción y resultado y comparan dos soluciones mediante criterios técnicos, ambientales, comunicativos o de seguridad."
        independent = f"Resuelve una versión nueva de «{focus.lower()}» sin copiar el modelo; toma una decisión técnica o digital, produce evidencia y revisa según el criterio acordado."
        ticket = f"Para «{focus.lower()}», muestra diseño, archivo, procedimiento o resultado y explica qué decisión cumple el criterio y qué debe mejorar."
        materials = f"{anchor}; materiales, herramientas o software disponibles con alternativa desconectada; protección y organización acordes a la tarea."
        support = "Ofrece materiales precortados, plantillas de organización, dispositivo compartido, atajos accesibles o alternativa desconectada; no ejecuta la decisión del estudiante."
        extension = "Cambia usuario, material, dato, audiencia o restricción y adapta la solución; luego vuelve a probar o revisar."
        evidence = f"Diseño, objeto, archivo o registro individual de «{focus.lower()}» con propósito, decisión, prueba, seguridad y mejora explicados."
        coordination = "El docente conduce diseño y seguridad física y digital; educación diferencial acuerda acceso a herramientas o interfaz sin ejecutar la solución, y coordinación TIC protege cuentas y datos."
    return {
        "title": focus,
        "purpose": f"Desarrollar {topic.lower()} mediante «{focus.lower()}», con una experiencia disciplinar específica, segura y revisable.",
        "goal": f"Hoy {goal}.",
        "opening": opening,
        "model": model,
        "guided": guided,
        "independent": independent,
        "ticket": ticket,
        "materials": materials,
        "support": support,
        "extension": extension,
        "evidence": evidence,
        "criteria": ["responde al foco específico de la clase", "toma una decisión pertinente y segura", "explica o localiza evidencia y reconoce límites"],
        "next_step": "Avanza cuando decisión, evidencia y explicación coinciden; si no, cambia acceso o ejemplo y vuelve a recoger evidencia sin etiquetar al estudiante.",
        "short_version": "Conserva situación específica, modelado, práctica guiada, desempeño individual y cierre; reduce cantidad o turnos, no el criterio disciplinar.",
        "home_task": "Observa, practica o registra una versión breve y segura con recursos disponibles. No requiere compras, internet, datos personales ni exposición familiar, corporal o emocional.",
        "complementary": [
            "Recuperación: aísla una decisión o criterio y vuelve luego a la tarea completa.",
            f"Análisis de error: revisa un caso ficticio que muestra esta confusión: {misconception}.",
            "Transferencia: cambia contexto, material, audiencia, regla o condición y explica qué debe adaptarse.",
        ],
        "difficulty_actions": [
            {"signal": "Imita, repite o termina sin tomar una decisión", "action": "Ofrece dos alternativas y pide elegir una según el propósito específico.", "check": "Puede mostrar qué eligió, para qué y con qué evidencia."},
            {"signal": misconception.capitalize(), "action": support, "check": "Resuelve un caso nuevo sin repetir la confusión."},
            {"signal": "Se inhibe, queda expuesto o no accede al formato", "action": "Reduce exposición y ofrece una vía equivalente de participación, manteniendo el OA.", "check": "Produce evidencia propia mediante una vía accesible y segura."},
        ],
        "specialist_coordination": coordination,
        "transversal": _attitude(code, index, goal),
    }


def build_sequence(code: str) -> dict | None:
    prefix = code[:2]
    profile = TABLES.get(prefix, {}).get(code)
    if not profile:
        return None
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": f"{profile['topic']} se desarrolla mediante experiencias propias de la disciplina. La secuencia parte de {profile['prior']} y enfrenta la confusión «{profile['misconception']}».",
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Eje oficial · organización interna en {len(profile['focuses'])} clases"],
            "unit_origin": "Organización interna derivada del eje y del OA; no se presenta como unidad oficial del programa de estudio.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial",
            "source": f"https://www.curriculumnacional.cl/curriculum/1o-6o-basico/{SLUGS[prefix]}/3-basico/{code.lower().replace(' ', '-')}",
        },
        "lessons": [_lesson(code, index, profile) for index in range(len(profile["focuses"]))],
    }


def build_transversal_integration(item: dict) -> dict:
    code = item["oa_code"]
    prefix = code.split("03", 1)[0].removeprefix("de Actitud ")
    description = item["oa_text"].split("Unidad de Currículum", 1)[0].strip().rstrip(".")
    context, decision = {
        "MU": ("una experiencia de escucha, interpretación o creación musical", "decisión musical audible"),
        "TE": ("una experiencia de diseño, elaboración o comunicación digital", "decisión técnica, segura o de autoría"),
    }[prefix]
    lessons = []
    for index, (phase, _) in enumerate(item["phases"]):
        title = f"{phase}: {description.lower()} en acción {index + 1}"
        lessons.append({
            "title": title,
            "purpose": f"Integrar «{description}» dentro de {context}, sin convertir la actitud en charla aislada ni rasgo personal.",
            "goal": f"Hoy haré visible una {decision} y explicaré cómo aportó al aprendizaje.",
            "opening": f"Contrasta dos respuestas ficticias a {context}: una sólo nombra la actitud y otra la muestra mediante una acción. Localizan evidencia para «{title.lower()}».",
            "model": f"Modela una {decision} que manifiesta «{description}» y señala su efecto concreto en el trabajo, la escucha, la seguridad, la autoría o la revisión.",
            "guided": f"Realizan una tarea breve de «{title.lower()}», marcan una acción observable y reciben retroalimentación sobre ella, nunca sobre talento, cuerpo, personalidad u obediencia.",
            "independent": f"Cada estudiante completa una nueva versión de {context}, identifica su decisión y explica cómo «{description.lower()}» influyó en el resultado.",
            "ticket": f"En «{title.lower()}», señala una evidencia propia de la actitud y completa: esta acción ayudó porque…",
            "materials": "Materiales del OA anfitrión y una tarjeta que expresa la actitud como acción observable.",
            "support": "Ofrece dos ejemplos, frase inicial y vía equivalente de participación; conserva la decisión disciplinar y los resguardos auditivos, físicos, digitales o de autoría.",
            "extension": "Transfiere la actitud a otro OA de la asignatura y compara cómo cambia su manifestación concreta.",
            "evidence": f"Producción o desempeño disciplinar de «{title.lower()}» con acción y explicación atribuibles al estudiante.",
            "criteria": ["resuelve una tarea disciplinar pertinente", "hace visible la actitud mediante una acción", "explica su efecto sin etiquetas personales"],
            "next_step": "Integra nuevamente si depende del apoyo; cambia el contexto cuando la acción aparece con autonomía.",
            "short_version": "Conserva tarea, acción observable, evidencia individual y cierre; reduce repetición, no integración.",
            "home_task": "Explica o representa un ejemplo seguro de la actitud dentro de la asignatura; no requiere compras, internet ni datos personales.",
            "complementary": ["Clasificar evidencia y no evidencia de la actitud.", "Revisar un caso que confunde actitud con obediencia o talento.", "Transferir la acción a otro eje."],
            "difficulty_actions": [
                {"signal": "Nombra la actitud, pero no la aplica", "action": "Pide señalar una decisión concreta dentro de la tarea.", "check": "La evidencia queda localizada."},
                {"signal": "Evalúa talento o personalidad", "action": "Reformula como acción modificable y vinculada al OA.", "check": "La retroalimentación describe qué hizo y qué puede probar."},
                {"signal": "La actitud desplaza el contenido", "action": "Recupera el criterio disciplinar y usa la actitud como medio.", "check": "El ticket demuestra contenido e integración."},
            ],
            "specialist_coordination": "El docente mantiene el OA disciplinar como foco; profesionales pertinentes acuerdan una barrera, variante y evidencia sin sustituir la decisión del estudiante.",
        })
    return {"generated_for": "3-basico", "lessons": lessons}
