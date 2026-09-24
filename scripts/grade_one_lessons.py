"""Pedagogical lesson designs for every first-grade objective."""
from __future__ import annotations

import re


PHASES = {
    "Conectar y diagnosticar": (
        "Abrir el aprendizaje desde una experiencia comprensible y recoger evidencia inicial sin calificarla",
        "Explorar lo que ya sabemos",
        "presenta dos ejemplos contrastados y pide que cada estudiante elija, muestre o explique qué nota",
        "una respuesta inicial registrada antes y después de conversar",
    ),
    "Comprender y modelar": (
        "Hacer visible el procedimiento o criterio disciplinar mediante una demostración breve y pensada en voz alta",
        "Mirar cómo se hace y explicar por qué",
        "resuelve un ejemplo paso a paso, nombra cada decisión y contrasta un caso que no cumple el criterio",
        "una reconstrucción del ejemplo con palabras, gestos, objetos o dibujo",
    ),
    "Practicar con apoyo": (
        "Acompañar el primer desempeño completo con preguntas y retroalimentación inmediata",
        "Practicar juntos y aprender del intento",
        "entrega una tarea breve por turno, detiene al grupo en el punto difícil y pregunta qué pista permite continuar",
        "un desempeño guiado y una corrección explicada",
    ),
    "Aplicar con autonomía": (
        "Comprobar que cada estudiante puede usar el aprendizaje en una situación nueva sin copiar el ejemplo",
        "Resolver un desafío con mis propias decisiones",
        "plantea una situación distinta a la ensayada, recuerda los criterios y observa antes de intervenir",
        "un producto individual que permita ver el razonamiento",
    ),
    "Contrastar y profundizar": (
        "Profundizar mediante comparación, casos límite y explicación de diferencias relevantes",
        "Comparar dos caminos y defender una elección",
        "pone dos soluciones, producciones o interpretaciones lado a lado y pregunta qué cambia, qué se mantiene y cuál se ajusta mejor al propósito",
        "una comparación fundamentada y una mejora",
    ),
    "Transferir al contexto": (
        "Transferir el aprendizaje a una situación cercana sin convertir el contexto en decoración",
        "Usar lo aprendido en una situación de mi entorno",
        "plantea una necesidad del curso, hogar o comunidad y exige usar el mismo criterio aprendido para resolverla",
        "una aplicación situada con explicación de la conexión",
    ),
    "Demostrar y retroalimentar": (
        "Integrar el aprendizaje, ofrecer retroalimentación útil y decidir el paso siguiente con evidencia individual",
        "Mostrar lo aprendido, revisar y mejorar",
        "analiza una respuesta ficticia, localiza una fortaleza y un error, y muestra cómo se mejora sin reemplazar el trabajo del estudiante",
        "un desempeño final, una revisión visible y una breve autoevaluación",
    ),
}


PROFILES = {
    "artes-visuales": {
        "context": "una imagen, objeto o detalle del entorno natural, cultural o cotidiano",
        "example": "observa líneas, formas, colores, texturas y ubicación; prueba dos decisiones visuales antes de escoger",
        "guided": "crean una prueba pequeña, la miran a distancia y explican qué elección ayuda a comunicar la idea",
        "independent": "realiza una creación propia sin imagen modelo y acompáñala con una frase de artista",
        "materials": "papel reutilizado, lápices, crayones, recortes y materiales seguros disponibles; prepara pocas opciones para privilegiar decisiones",
        "support": "ofrece herramientas de mayor agarre, pictogramas de decisiones y respuesta oral; no intervengas directamente la obra",
        "extension": "produce una segunda versión cambiando un solo recurso visual y compara su efecto",
        "criteria": ["observa o experimenta antes de decidir", "usa recursos visuales con intención", "explica una elección propia"],
    },
    "ciencias-naturales": {
        "context": "un objeto, ser vivo, fenómeno o fotografía cercana que pueda observarse con seguridad",
        "example": "separa «veo o mido» de «pienso que», registra un detalle y explica qué evidencia permite sostener la idea",
        "guided": "observan, clasifican o comparan casos y justifican cada decisión con una característica verificable",
        "independent": "completa un registro con dibujo rotulado, observación, explicación y una pregunta nueva",
        "materials": "objetos o fotografías seguras, lupa opcional, fichas de registro y lápices; observar sin dañar ni extraer seres vivos",
        "support": "usa tabla «observo/pienso», banco visual de vocabulario y explicación oral señalando el registro",
        "extension": "predice qué cambiaría en otro caso y señala qué observación permitiría comprobarlo",
        "criteria": ["registra evidencia observable", "usa vocabulario científico del OA", "explica la relación sin confundir opinión con dato"],
    },
    "educacion-fisica-salud": {
        "context": "un recorrido corto y seguro con zonas claramente delimitadas",
        "example": "demuestra el movimiento a velocidad lenta, señala postura, control y espacio seguro, y luego muestra un error frecuente",
        "guided": "practican en parejas con turnos breves: una persona ejecuta y otra observa un único criterio antes de cambiar",
        "independent": "completa el recorrido o juego regulando su movimiento y explica una decisión de seguridad o autocuidado",
        "materials": "conos, cuerdas, pelotas blandas o marcas de piso; revisa superficie, distancias, hidratación y alternativas de participación",
        "support": "reduce velocidad o distancia, amplía blancos y permite apoyo estable sin reemplazar la habilidad motriz",
        "extension": "combina la habilidad con un cambio de dirección, ritmo o regla manteniendo control y seguridad",
        "criteria": ["ejecuta con control progresivo", "respeta espacio, reglas y seguridad", "reconoce cómo mejorar el movimiento"],
    },
    "historia-geografia-ciencias-sociales": {
        "context": "una fotografía familiar no privada, calendario, plano, objeto o testimonio breve con procedencia",
        "example": "identifica qué muestra la fuente, ordena o ubica la información y distingue el dato visible de una inferencia",
        "guided": "organizan tarjetas, fuentes o lugares y explican su decisión usando antes/después, cerca/lejos, porque o según corresponda",
        "independent": "construye una secuencia, plano, comparación o explicación y señala la fuente o experiencia que la respalda",
        "materials": "fuentes breves identificadas, tarjetas, calendario o plano simple y lápices; evita solicitar información familiar sensible",
        "support": "usa línea de tiempo, símbolos espaciales y relato oral con apoyos visuales; permite elegir un ejemplo ficticio seguro",
        "extension": "compara otra perspectiva o cambia una condición y explica qué se mantendría y qué cambiaría",
        "criteria": ["organiza información temporal, espacial o social", "usa una fuente o evidencia pertinente", "comunica una relación con claridad"],
    },
    "ingles-propuesta": {
        "context": "a short routine, picture, chant or classroom exchange with familiar words",
        "example": "modela primero el significado con imagen, gesto y entonación; luego repite la expresión en un contexto distinto sin traducir palabra por palabra",
        "guided": "escuchan o leen una instrucción breve, señalan la pista que comprendieron y responden en coro, pareja y turno individual",
        "independent": "responde, ordena, dibuja o produce una frase breve para una audiencia clara usando el apoyo disponible",
        "materials": "picture cards, real classroom objects, mini-whiteboards or paper, and an optional audio spoken clearly at natural speed",
        "support": "mantén imagen, gesto, repetición y tiempo de ensayo; acepta respuesta no verbal cuando el OA evalúa comprensión",
        "extension": "cambia personaje, objeto o lugar y usa la expresión en un intercambio nuevo de dos turnos",
        "criteria": ["comprende el propósito global", "usa una pista oral o visual", "responde de manera comprensible aunque no perfecta"],
    },
    "lengua-cultura-pueblos-originarios-ancestrales": {
        "context": "un relato, palabra, práctica o expresión pertinente al pueblo y territorio del establecimiento",
        "example": "presenta la fuente y su procedencia, escucha o lee la expresión con respeto y explica su sentido cultural sin tratar a los pueblos como una realidad única",
        "guided": "practican la expresión, secuencia o significado con apoyo de una persona o fuente culturalmente autorizada cuando esté disponible",
        "independent": "crea un registro oral, gráfico o escrito que conserve el sentido y reconozca de qué comunidad o fuente proviene",
        "materials": "fuentes locales autorizadas, imágenes contextualizadas, tarjetas y grabación opcional; valida pronunciación y protocolos con la comunidad",
        "support": "permite escuchar varias veces, responder en castellano cuando el contexto curricular lo admita y usar gestos o imágenes sin ridiculizar la lengua",
        "extension": "compara respetuosamente usos o sentidos entre contextos, explicitando que una variante no invalida otra",
        "criteria": ["participa con respeto cultural", "comprende o usa el elemento trabajado según el contexto", "reconoce procedencia y significado"],
    },
    "lenguaje-comunicacion": {
        "context": "un nombre, mensaje, poema, relato o texto funcional breve que tenga un destinatario reconocible",
        "example": "lee o escribe pensando en voz alta, señala letras, sonidos, espacios o pistas de significado y vuelve al texto para comprobar",
        "guided": "leen, escuchan, segmentan, ordenan o producen juntos; cada respuesta debe señalar una pista del texto, sonido o intención comunicativa",
        "independent": "produce una respuesta oral, dibujo rotulado, lectura o escritura breve y vuelve a ella para revisar una decisión",
        "materials": "texto ampliado, letras móviles, tarjetas de imágenes, cuaderno y lápiz; selecciona tipografía legible y contenido significativo",
        "support": "ofrece lectura compartida, segmentación oral, letras móviles, dictado al adulto o audio según la barrera, conservando la comprensión o producción objetivo",
        "extension": "cambia destinatario, orden, palabra o final y explica cómo se modifica el significado",
        "criteria": ["comprende o comunica una idea", "usa pistas del lenguaje oral o escrito", "revisa con un propósito claro"],
    },
    "matematica": {
        "context": "una colección de tapas, cubos, tarjetas numéricas o figuras que pueda manipularse y dibujarse",
        "example": "representa primero con objetos, después con dibujo y finalmente con símbolo; estima el resultado y comprueba contando, superponiendo o recorriendo",
        "guided": "resuelven un caso en parejas, comparan dos estrategias y explican qué representa cada objeto, trazo o número",
        "independent": "resuelve una situación nueva, muestra una representación y escribe o dicta una comprobación",
        "materials": "material contable, cubos, tarjetas, cuerda, regla o figuras según el OA, más una hoja de registro; incluye material improvisado sin costo",
        "support": "reduce cantidad de elementos, organiza el espacio y ofrece una representación inicial; no reemplaces el razonamiento por una regla memorizada",
        "extension": "encuentra otra estrategia, crea un caso que no funciona o cambia un dato y predice el efecto",
        "criteria": ["representa la situación con sentido", "explica una estrategia", "comprueba que la respuesta es razonable"],
    },
    "musica": {
        "context": "un sonido del entorno, una canción breve o una pieza de procedencia identificada",
        "example": "escucha una vez sin interrumpir, luego marca con gesto pulso, altura, intensidad, timbre o forma y compara dos fragmentos audibles",
        "guided": "imitan, alternan y crean un patrón corto; el grupo escucha un criterio por vez y describe lo que realmente oyó",
        "independent": "interpreta, representa o crea una respuesta musical breve y explica una elección sonora",
        "materials": "voz, cuerpo, objetos sonoros seguros e instrumento disponible; prepara silencio, señal de inicio y volumen protegido",
        "support": "usa pulso visible, eco de un motivo corto, participación corporal y opción de escuchar sin exposición solista",
        "extension": "transforma el patrón cambiando una cualidad sonora y explica cómo cambia su carácter",
        "criteria": ["escucha y responde a una cualidad sonora", "mantiene control y coordinación", "explica una decisión musical"],
    },
    "orientacion": {
        "context": "un caso ficticio y seguro sobre emociones, convivencia, pertenencia o trabajo escolar",
        "example": "nombra lo observable, ofrece más de una interpretación y piensa una respuesta que cuide a la persona y al grupo",
        "guided": "analizan tarjetas de situaciones, ensayan frases respetuosas y comparan consecuencias sin exigir relatos personales",
        "independent": "elige una respuesta responsable para un caso, explica por qué y reconoce una persona adulta o red de apoyo",
        "materials": "tarjetas de casos ficticios, pictogramas de emociones, semáforo de decisiones y hoja privada de reflexión",
        "support": "permite hablar en tercera persona, pasar turno y responder con pictogramas; no fuerces exposición emocional ni revelaciones",
        "extension": "considera cómo podría sentirse otra persona y ajusta la decisión para cuidar ambas perspectivas",
        "criteria": ["identifica una emoción, necesidad o responsabilidad", "propone una acción segura y respetuosa", "explica una consecuencia o apoyo"],
    },
    "tecnologia": {
        "context": "un objeto cotidiano o una necesidad simple del aula que pueda resolverse con materiales disponibles",
        "example": "define usuario y necesidad, dibuja una idea con partes señaladas y prueba primero una unión o mecanismo antes de construir",
        "guided": "comparan materiales y prototipos pequeños contra un criterio —resistencia, estabilidad o facilidad de uso— y registran el resultado",
        "independent": "diseña, construye o prueba una solución y muestra un cambio realizado a partir de la prueba",
        "materials": "cartón, papel, cinta, lana, tapas y herramientas escolares seguras; organiza piezas y normas antes de repartir",
        "support": "entrega piezas precortadas, plantilla de diseño y opciones de unión; conserva elección, prueba y mejora del estudiante",
        "extension": "añade una restricción de material o usuario y rediseña justificando el cambio",
        "criteria": ["responde a una necesidad o propósito", "elige materiales y pasos con sentido", "prueba y mejora usando un criterio"],
    },
}

NEXT_STEPS = {
    "artes-visuales": "Si la intención no se reconoce, vuelve a observar y ensayar un recurso visual; si la decisión es clara, invita a transformar color, textura o composición y comparar efectos.",
    "ciencias-naturales": "Si confunden observación e inferencia, clasifica nuevos ejemplos; si usan evidencia, pídeles predecir otro caso y definir qué tendrían que observar para comprobarlo.",
    "educacion-fisica-salud": "Si falta control o seguridad, reduce velocidad, distancia o estímulos y practica el componente crítico; si hay dominio, combina la habilidad con una regla nueva.",
    "historia-geografia-ciencias-sociales": "Si ordenan o ubican sin justificar, vuelve a la fuente, calendario o plano; si explican con evidencia, incorpora otra perspectiva o escala.",
    "ingles-propuesta": "Si no comprenden el mensaje global, recupera imagen, gesto y palabras clave; si responden con sentido, retira una ayuda y cambia un elemento del intercambio.",
    "lengua-cultura-pueblos-originarios-ancestrales": "Si se pierde el sentido o la procedencia, vuelve a la fuente cultural validada; si lo comprenden, úsalo en otro contexto respetando variantes y protocolos.",
    "lenguaje-comunicacion": "Si la dificultad está en sonido, letra, vocabulario o comprensión, forma un grupo breve para ese nudo; si comunican con claridad, cambia destinatario o propósito.",
    "matematica": "Si la representación no coincide con la situación, vuelve a objetos y dibujo; si coincide pero falta explicación, compara estrategias; si hay dominio, cambia un dato y anticipa el efecto.",
    "musica": "Si no sostienen el criterio audible, vuelve a eco, pulso visible o contraste breve; si lo logran, transforma una cualidad y escucha el efecto.",
    "orientacion": "Si la respuesta no cuida a las personas, analiza consecuencias con un caso ficticio; si es segura y respetuosa, incorpora otra perspectiva o red de apoyo.",
    "tecnologia": "Si construyen sin propósito, vuelve a usuario y necesidad; si el objeto responde al criterio, agrega una restricción y realiza una nueva prueba.",
}

HOME_TASKS = {
    "artes-visuales": "Busca en casa dos objetos con texturas distintas, dibuja un detalle de cada uno y cuenta qué sensación visual quisiste conservar",
    "ciencias-naturales": "Observa durante cinco minutos un objeto, ser vivo o fenómeno seguro, registra tres detalles y separa lo que viste de lo que supones",
    "educacion-fisica-salud": "Practica en un espacio seguro una versión suave del movimiento y registra con una palabra o dibujo qué ayudó a mantener el control",
    "historia-geografia-ciencias-sociales": "Conversa con una persona adulta sobre una rutina, lugar u objeto cercano y registra un dato sin incluir información privada",
    "ingles-propuesta": "Usa la expresión trabajada en un intercambio de dos turnos con una persona o un juguete y dibuja la pista que ayudó a comprender",
    "lengua-cultura-pueblos-originarios-ancestrales": "Recupera una palabra, relato o práctica solo si la familia desea compartirla; registra su procedencia y evita presentarla como universal",
    "lenguaje-comunicacion": "Lee, escucha o cuenta un texto breve a alguien y registra una idea importante y la pista que permitió comprenderla",
    "matematica": "Encuentra una situación cotidiana que pueda representarse con objetos o dibujo, resuélvela y muestra una forma de comprobar",
    "musica": "Escucha sonidos seguros del entorno, elige dos, represéntalos con trazos y explica en qué se parecen o diferencian",
    "orientacion": "Elige una rutina de autocuidado o convivencia, practícala con apoyo familiar y registra qué paso resultó más útil sin contar asuntos privados",
    "tecnologia": "Observa un objeto cotidiano, identifica a quién ayuda, qué necesidad resuelve y dibuja una mejora posible sin construirla todavía",
}

COMPLEMENTARY_ACTIVITIES = {
    "artes-visuales": "Galería silenciosa: observar tres producciones y dejar una pregunta sobre una decisión visual, nunca sobre si quedó bonita.",
    "ciencias-naturales": "Mesa de evidencias: clasificar nuevos casos en «observo», «pienso» y «necesito comprobar».",
    "educacion-fisica-salud": "Estación de control: repetir el movimiento a tres ritmos y comparar seguridad, precisión y esfuerzo percibido.",
    "historia-geografia-ciencias-sociales": "Fuente sorpresa: incorporar una imagen, objeto o plano nuevo y decidir qué permite saber y qué no.",
    "ingles-propuesta": "Information gap breve: cada pareja posee una pista diferente y debe intercambiar significado, no repetir de memoria.",
    "lengua-cultura-pueblos-originarios-ancestrales": "Mapa de procedencia: ubicar la fuente o comunidad de cada expresión y reconocer variantes sin jerarquizarlas.",
    "lenguaje-comunicacion": "Taller de revisión: comparar dos versiones breves y justificar qué cambio ayuda más al destinatario.",
    "matematica": "Desafío de representaciones: mostrar el mismo caso con objetos, dibujo y símbolo y localizar dónde aparece la misma relación.",
    "musica": "Laboratorio sonoro: transformar una sola cualidad del patrón y describir el efecto audible.",
    "orientacion": "Teatro de decisiones: ensayar dos respuestas seguras ante un caso ficticio y comparar consecuencias.",
    "tecnologia": "Prueba de usuario: otra pareja usa el prototipo o boceto y entrega evidencia ligada a un criterio acordado.",
}

SPECIALIST_COORDINATION = {
    "artes-visuales": "El docente de Artes, si participa, aporta técnica y apreciación; educación diferencial acuerda una vía de acceso sin intervenir la obra del estudiante.",
    "ciencias-naturales": "El docente generalista conduce la indagación; educación diferencial anticipa barreras de registro y el asistente apoya materiales y seguridad sin dar la respuesta.",
    "educacion-fisica-salud": "El docente especialista define progresión y seguridad; otros adultos supervisan zonas acordadas y reportan evidencia con el mismo criterio.",
    "historia-geografia-ciencias-sociales": "El docente conduce el análisis de fuentes; CRA puede apoyar su selección y educación diferencial facilitar acceso sin sustituir la interpretación.",
    "ingles-propuesta": "El especialista de Inglés modela significado y pronunciación; los apoyos mantienen gesto, imagen y ensayo sin exigir traducción palabra por palabra.",
    "lengua-cultura-pueblos-originarios-ancestrales": "El educador tradicional o referente autorizado valida lengua, procedencia y protocolos; el docente articula el OA y evita generalizaciones.",
    "lenguaje-comunicacion": "El docente conduce comprensión y producción; educador diferencial o fonoaudiólogo, cuando corresponda al plan del estudiante, asesora acceso sin reemplazar la enseñanza ni diagnosticar en clase.",
    "matematica": "El docente hace visible el razonamiento; educación diferencial propone representaciones accesibles y el asistente formula preguntas, sin entregar el procedimiento.",
    "musica": "El especialista modela escucha e interpretación; otros adultos apoyan regulación del ambiente y participación sin convertir el apoyo en ejecución por el estudiante.",
    "orientacion": "El profesor jefe conduce casos pedagógicos; convivencia u orientación escolar interviene según protocolo cuando aparece una situación real, sin exponerla ante el curso.",
    "tecnologia": "El docente guía diseño y prueba; asistente o encargado de recursos apoya seguridad y distribución de herramientas sin decidir la solución.",
}

HOME_PHASES = {
    "Conectar y diagnosticar": "Antes de la próxima clase, reúne un ejemplo inicial sin corregirlo todavía.",
    "Comprender y modelar": "Explica a otra persona o a un personaje imaginario el paso que te resultó más importante.",
    "Practicar con apoyo": "Repite un caso breve usando la pista aprendida y marca cuándo pudiste retirarla.",
    "Aplicar con autonomía": "Crea o resuelve un caso distinto al trabajado y conserva una huella de tu decisión.",
    "Contrastar y profundizar": "Compara dos posibilidades y registra una semejanza, una diferencia y tu elección.",
    "Transferir al contexto": "Busca una situación cercana donde sirva el mismo aprendizaje y explica la conexión.",
    "Demostrar y retroalimentar": "Revisa una producción anterior, mejora una decisión y señala qué cambió.",
}


def _short(text: str, limit: int = 120) -> str:
    clean = re.sub(r"\s+", " ", text).strip().rstrip(".")
    if len(clean) <= limit:
        return clean
    cut = clean[:limit].rsplit(" ", 1)[0]
    return cut + "…"


def build_grade_one_lessons(item: dict) -> dict:
    """Return a complete age-appropriate editorial contract for a grade-one OA."""
    profile = PROFILES[item["subject_slug"]]
    oa = _short(item["oa_text"], 190)
    topic = _short(item["topic"], 92).lower()
    title_topic = _short(item["topic"], 46).lower()
    lessons = []
    for index, (phase, focus) in enumerate(item["phases"], 1):
        purpose, title, move, evidence_kind = PHASES[phase]
        lessons.append({
            "title": f"{title}: {title_topic}",
            "purpose": f"{purpose}, centrado en «{oa}».",
            "goal": f"Hoy aprenderé a {topic} y mostraré cómo lo hice.",
            "opening": f"Sitúa {profile['context']}. {move.capitalize()}. Recoge una respuesta de todo el curso y conserva dos ejemplos para compararlos al cierre.",
            "model": f"Para trabajar «{oa}», {profile['example']}. Formula una pregunta auténtica y deja cinco segundos de espera antes de aceptar respuestas.",
            "guided": f"{profile['guided'].capitalize()}. Usa la pregunta «¿qué viste, escuchaste, hiciste o pensaste que te permite decirlo?» y retroalimenta el criterio, no la rapidez.",
            "independent": f"Cada estudiante {profile['independent']}. La evidencia debe ser individual aunque materiales y conversación puedan compartirse.",
            "ticket": f"Vuelve a la respuesta inicial: cada estudiante muestra qué mantendría y qué cambiaría. Recoge {evidence_kind} vinculada a «{focus}».",
            "materials": profile["materials"].capitalize(),
            "support": profile["support"].capitalize(),
            "extension": profile["extension"].capitalize(),
            "evidence": f"{evidence_kind.capitalize()} que responda al OA y permita reconocer una decisión del estudiante.",
            "criteria": profile["criteria"],
            "next_step": NEXT_STEPS[item["subject_slug"]],
            "short_version": "Conserva apertura, demostración, un único desempeño individual y ticket; reduce cantidad de casos o turnos, no el objetivo ni la explicación.",
            "home_task": f"Tarea breve y flexible (10 minutos): {HOME_PHASES[phase]} {HOME_TASKS[item['subject_slug']]}. Puede resolverse oralmente, con dibujo u objetos; no requiere internet, impresión ni compra de materiales.",
            "complementary": [
                COMPLEMENTARY_ACTIVITIES[item["subject_slug"]],
                f"Recuperación opcional: vuelve a un ejemplo concreto de «{title_topic}», ofrece una sola pista y retírala cuando el estudiante explique la decisión.",
                f"Profundización opcional: cambia una condición del desafío sobre «{title_topic}» y pide predecir, comprobar y revisar.",
            ],
            "difficulty_actions": [
                {"signal": "No inicia o no comprende la consigna", "action": "Di la consigna en un paso, muéstrala con un ejemplo distinto y pide al estudiante señalar o explicar qué hará primero.", "check": "Inicia el primer paso sin copiar el ejemplo."},
                {"signal": "Participa, pero no demuestra el aprendizaje", "action": f"Vuelve al criterio «{profile['criteria'][0]}» y solicita una respuesta individual breve con objetos, gesto, oralidad, dibujo o escritura pertinente.", "check": "La producción individual permite atribuir una decisión al estudiante."},
                {"signal": "Se frustra, evita o abandona", "action": "Reduce cantidad de casos, ofrece una elección entre dos vías y acuerda un intento breve; mantén el mismo aprendizaje y evita exponer públicamente.", "check": "Retoma la tarea y completa un intento observable."},
                {"signal": "El grupo pierde foco o aparecen conflictos", "action": "Pausa, restablece la regla con una demostración de 30 segundos, asigna turnos o roles concretos y reinicia con tiempo visible.", "check": "El grupo sostiene un ciclo completo respetando la regla."},
                {"signal": "Termina rápido sin explicar", "action": f"No agregues repetición. {profile['extension'].capitalize()}.", "check": "Compara, justifica o transfiere en vez de acumular respuestas."},
            ],
            "specialist_coordination": SPECIALIST_COORDINATION[item["subject_slug"]],
        })
    return {"generated_for": "1-basico", "lessons": lessons}
