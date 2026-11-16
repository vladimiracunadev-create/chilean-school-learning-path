"""Cuaderno del estudiante, 4.º medio Inglés (Formación General), OA 03 (conocimiento estratégico del inglés) y OA 04 (interacción fluida, visiones de mundo e identidad).

Los títulos de clase del plan son genéricos; aquí se aplican así.
OA 03: 1 organización del texto y conectores, 2 estrategias de vocabulario y diccionario, 3 voz pasiva y oraciones de relativo, 4 verbos de reporte, afirmación y evidencia.
OA 04: 1 conversar y debatir, 2 diferencias culturales de comunicación, 3 valores, planes e identidad, 4 diálogo intercultural, 5 reparar, reformular y reflexionar.
Textos originales, glosados, en inglés americano; los datos son de ejemplo.
"""
from __future__ import annotations

from fg_ingl_common import ADULT, MAT_L, MAT_R, arith, ex, lesson, mc, ml, mr, task

OA3 = "FG-INGL-4M-OAC-03"
OA4 = "FG-INGL-4M-OAC-04"


def sc(oa, n, rows):
    return [(f"En Inglés de 4.º medio (OA {oa}, clase {n}): {q}", a, w) for q, a, w in rows]


# ================================================================= OA 03
# ------------------------------------------------------------------ clase 1: organización del texto y conectores
CE = "«Many cities have introduced bike lanes. As a result, fewer cars enter the center. Consequently, the air is cleaner and, because of this, more people walk.» (introduced = introdujeron, bike lanes = ciclovías, as a result = como resultado, consequently = en consecuencia, air = aire, walk = caminar)"
PS = "«Problem: Students often forget their homework. Solution: Some schools use a weekly planner. This helps students to organize their tasks, so fewer assignments are forgotten.» (forget = olvidar, weekly planner = agenda semanal, tasks = tareas, assignments = trabajos, forgotten = olvidados)"
COMP = "«Online classes offer flexibility, whereas face-to-face classes offer direct contact. Both can work well; the best choice depends on the student.» (online = en línea, flexibility = flexibilidad, face-to-face = presenciales, direct contact = contacto directo, depends on = depende de)"
CHR = "«First, the team chose a topic. Then they collected data. After that, they wrote a report. Finally, they presented it.» (team = equipo, collected = reunieron, data = datos, report = informe, presented = presentaron)"

lesson(
    OA3, 1, MAT_R,
    "Aprenderé a reconocer cómo se organiza un texto (causa y efecto, problema y solución, comparación, cronología) y las palabras que lo señalan. Sirve para usar mi conocimiento del inglés de manera estratégica al comprender y producir textos.",
    ["Sé usar conectores como because y however.", "Sé encontrar la idea central."],
    [
        "Los textos tienen patrones de organización (text structures). Causa y efecto: una acción provoca un resultado; se señala con as a result, consequently, therefore, because of this, so. Problema y solución: se plantea una dificultad y una respuesta; se señala con problem, solution, this helps, to solve. Comparación y contraste: se destacan semejanzas y diferencias; se señala con whereas, while, both, similarly, unlike. Cronología: eventos en orden de tiempo; se señala con first, then, after that, finally.",
        "Reconocer el patrón ayuda a anticipar qué viene y a resumir. Si ves as a result, esperas un efecto después; si ves problem, esperas una solución. Para producir un texto, elige el patrón según tu propósito: si quieres explicar una consecuencia, usa causa y efecto; si quieres proponer algo, problema y solución. Las palabras señal (signal words) son pistas, pero no siempre aparecen: a veces el patrón se nota por la relación entre las ideas.",
        "Un buen resumen respeta el patrón: en causa y efecto indica qué provoca qué; en problema y solución nombra ambos; en comparación incluye lo común y lo distinto; en cronología conserva el orden. Evita agregar tu opinión. No confundas causa con orden de tiempo: que un hecho ocurra antes no significa que lo provoque.",
    ],
    [("cause and effect", "causa y efecto"), ("problem and solution", "problema y solución"), ("compare and contrast", "comparación y contraste"), ("chronological order", "orden cronológico"), ("signal word", "palabra señal"), ("as a result / consequently", "como resultado / en consecuencia")],
    [
        ("Identificar el patrón", CE + " ¿Qué patrón de organización tiene el texto?", ["Busco as a result y consequently.", "Esas palabras señalan consecuencias.", "Es causa y efecto."], "Causa y efecto"),
        ("Resumir según el patrón", PS + " Resume el texto en una oración.", ["Nombro el problema: se olvidan las tareas.", "Nombro la solución: una agenda semanal.", "Digo el efecto: se olvidan menos trabajos."], "Algunos colegios usan una agenda semanal para que se olviden menos tareas"),
    ],
    [
        ("Pensar que lo que ocurre antes siempre es la causa.", "El orden de tiempo no prueba una causa.", "Busca palabras de causa y una explicación."),
        ("Resumir con una opinión propia.", "El resumen debe decir lo que dice el texto.", "Usa las palabras del texto y el patrón."),
    ],
    [
        mr(CE, "¿Qué palabra señala un resultado?", "As a result", ["Many", "walk"], "As a result introduce el resultado."),
        mr(PS, "¿Qué palabra introduce la solución?", "Solution", ["Problem", "Students"], "El texto marca la solución con Solution."),
        mr(COMP, "¿Qué palabra marca un contraste?", "whereas", ["offer", "depends"], "Whereas une dos ideas distintas."),
    ],
    [
        mr(PS, "¿Cuál es el problema?", "los estudiantes suelen olvidar su tarea", ["la agenda semanal es demasiado cara", "hay pocos profesores en los colegios"], "Problem: Students often forget their homework."),
        mr(COMP, "¿Qué patrón tiene el texto sobre las clases?", "comparación y contraste", ["cronología", "problema y solución"], "Compara dos tipos de clases."),
        mr(CHR, "¿Qué patrón tiene el texto del equipo?", "cronología", ["causa y efecto", "comparación"], "First, then, after that y finally ordenan los pasos."),
    ],
    [
        mr(CE, "¿Qué provoca que más personas caminen según el texto?", "que el aire esté más limpio", ["que haya más autos", "que cierren las ciclovías"], "Because of this se refiere al aire más limpio."),
        mr(CHR, "Ordena con letras: a) presentaron el informe b) escribieron el informe c) eligieron un tema d) reunieron datos. Escribe el orden.", "c, d, b, a", ["c, b, d, a", "d, c, b, a"], "Chose a topic, collected data, wrote a report, presented it."),
        mc("Quieres escribir un texto para proponer una solución a la basura en el patio. ¿Qué patrón conviene?", "problema y solución", ["cronología", "comparación"], "El propósito es proponer una respuesta a un problema."),
    ],
    [
        mc(COMP + " Un compañero dice que este texto tiene patrón cronológico porque habla de dos tipos de clases. ¿Qué le respondes?", "no: contrasta dos opciones con whereas, es comparación", ["sí: los dos tipos de clases tienen una fecha", "sí: porque el texto tiene la palabra both"], "Whereas y both indican comparación."),
        mc("Dos hechos: 'Las ventas subieron. Hubo una campaña.' ¿Qué oración presenta la campaña como causa?", "As a result of the campaign, sales rose", ["After that, sales rose in the shops", "First, sales rose, then there was a campaign"], "As a result of indica causa."),
    ],
    [
        mc("Lees: 'First, mix the dough. Then let it rest. Finally, bake it.' (dough = masa, rest = reposar). ¿Qué patrón es?", "cronología (instrucciones)", ["comparación", "causa y efecto"], "First, then y finally marcan pasos."),
        mc("Lees: 'Many students sleep too little. A later school start could help them.' ¿Qué patrón usa?", "problema y solución", ["cronología", "comparación"], "Plantea una dificultad y una propuesta."),
    ],
    [mc("Quieres explicar por qué se pierde un bus: 'The bus was late; as a result, I missed the exam.' (missed = perdí). ¿Qué patrón es?", "causa y efecto", ["problema y solución", "cronología"], "As a result introduce la consecuencia.")],
    sc(3, 1, [
        ("¿Qué patrón señalan first, then y finally?", "Cronología", "Ordenan los hechos en el tiempo."),
        ("¿Qué patrón señala whereas?", "Comparación y contraste", "Une ideas diferentes."),
        ("¿Para qué sirve reconocer el patrón de un texto?", "Para anticipar y resumir mejor", "Ayuda a comprender y a producir."),
    ]),
    task("Lee: «Many students use phones late at night. As a result, they sleep less. Consequently, they feel tired in class. To solve this problem, some schools suggest a no-screen rule after ten.» (sleep less = duermen menos, tired = cansados, no-screen rule = regla sin pantallas). Escribe en español qué patrones hay, la causa, el efecto y la solución.", "Hay causa y efecto y problema y solución. Causa: usar el teléfono tarde en la noche. Efecto: duermen menos y se sienten cansados. Solución: una regla sin pantallas después de las diez.", ["identifica los patrones", "separa causa, efecto y solución", "usa las palabras señal"], ["tres respuestas"], ["confundir causa y solución", "no mencionar los dos patrones"], "Subraya as a result, consequently y to solve para ubicar cada parte."),
    "Escribe un texto de tres oraciones en inglés con el patrón causa y efecto y subraya las palabras señal.",
    "Escribe una instrucción con first, then y finally.",
)

# ------------------------------------------------------------------ clase 2: estrategias de vocabulario
DICT = "«decide (verb): to make a choice after thinking. Example: She decided to study biology. decision (noun): a choice that you make. decisive (adjective): able to decide quickly and clearly. decisively (adverb): in a decisive way. cope with (phrasal verb): to deal successfully with something difficult.» (make a choice = elegir, deal with = manejar)"

lesson(
    OA3, 2, MAT_R,
    "Aprenderé estrategias de vocabulario: familias de palabras (decide, decision, decisive), la categoría gramatical (sustantivo, verbo, adjetivo, adverbio) y cómo leer una entrada de diccionario. Sirve para usar mi conocimiento del inglés al comprender y producir con precisión.",
    ["Sé usar prefijos y sufijos básicos.", "Conozco colocaciones como make a decision."],
    [
        "Una familia de palabras (word family) reúne palabras que comparten una raíz: decide (verbo), decision (sustantivo), decisive (adjetivo), decisively (adverbio). Los sufijos señalan la categoría: -tion y -ment forman sustantivos (decision, improvement), -ive, -ful y -al forman adjetivos (decisive, helpful), -ly forma adverbios (decisively) y -ize y -en forman verbos (organize, strengthen). Reconocer la categoría ayuda a saber qué función cumple la palabra en la oración.",
        "Una entrada de diccionario (dictionary entry) incluye la palabra, la categoría abreviada (n. sustantivo, v. verbo, adj. adjetivo, adv. adverbio), una definición, un ejemplo y a veces frases fijas. Lee el ejemplo para ver cómo se usa. Si hay varios significados, elige el que encaje con el contexto. Un verbo con preposición (cope with, depend on, rely on) se aprende como bloque.",
        "Para producir texto, escoge la forma que pide la oración: She made a decision (sustantivo después de artículo); She decided quickly (verbo); a decisive answer (adjetivo antes del sustantivo); she answered decisively (adverbio que modifica un verbo). Si dudas, mira la posición de la palabra y su sufijo.",
    ],
    [("word family", "familia de palabras"), ("noun / verb / adjective / adverb", "sustantivo / verbo / adjetivo / adverbio"), ("dictionary entry", "entrada de diccionario"), ("cope with", "manejar, sobrellevar"), ("-tion, -ive, -ly", "sufijos de sustantivo, adjetivo y adverbio"), ("phrasal verb", "verbo con partícula")],
    [
        ("Elegir la categoría", "Completa: 'She made an important ___.' A) decision B) decide", ["Después de important va un sustantivo.", "Decision es un sustantivo.", "Decide es un verbo."], "A) decision"),
        ("Leer una entrada", DICT + " ¿Cuál es el significado de cope with?", ["Busco la entrada cope with.", "La definición dice dealing successfully with something difficult.", "Significa manejar con éxito algo difícil."], "Manejar con éxito algo difícil"),
    ],
    [
        ("Poner un verbo donde va un sustantivo: She made a decide.", "Después de un artículo se necesita un sustantivo.", "Usa decision."),
        ("Ignorar la preposición de un verbo: cope your stress.", "El verbo necesita with.", "Aprende cope with como bloque."),
    ],
    [
        mr(DICT, "¿Qué categoría tiene decisive?", "adjetivo", ["sustantivo", "verbo"], "El diccionario indica adjective."),
        mr(DICT, "¿Qué categoría tiene decisively?", "adverbio", ["adjetivo", "verbo"], "El diccionario indica adverb."),
        mr(DICT, "¿Qué significa decision?", "una elección que haces", ["la acción de elegir rápidamente", "una persona decidida"], "La entrada dice a choice that you make."),
    ],
    [
        mc("¿Qué sufijo forma sustantivos?", "-tion", ["-ly", "-ive"], "-tion forma sustantivos como decision."),
        mc("¿Qué sufijo forma adverbios?", "-ly", ["-tion", "-ment"], "-ly forma adverbios como decisively."),
        mc("Completa: 'She answered ___.'", "decisively", ["decisive", "decision"], "Después de un verbo va un adverbio."),
    ],
    [
        mc("Completa: 'He gave a ___ answer.'", "decisive", ["decisively", "decide"], "Antes de un sustantivo va un adjetivo."),
        mc("Completa (announce = anunciar, rule = regla): 'The ___ of the new rule surprised everybody.'", "announcement", ["announce", "announced"], "El sufijo -ment forma sustantivos y después del artículo va uno."),
        mc("Completa: 'It is hard to ___ with so much work.'", "cope", ["copes", "coping"], "Después de to va el verbo base y with va después."),
    ],
    [
        mc("Un alumno encuentra la palabra depend en el diccionario y escribe 'It depends of the weather'. ¿Qué error cometió?", "usó of en lugar de on; el verbo se aprende como depend on", ["usó mal el artículo the antes de la palabra weather en la oración", "dejó el verbo depend en presente simple en lugar de otro tiempo"], "Depend on es el bloque."),
        mc("Tienes la palabra strengthen. Por su sufijo -en, ¿qué categoría es?", "verbo", ["adjetivo", "adverbio"], "El sufijo -en forma verbos como strengthen."),
    ],
    [
        mc("Lees: 'The company's rapid growth worried the investors.' (growth = crecimiento, investors = inversionistas). Si no conoces rapid, ¿qué estrategia sirve?", "ver que va antes de un sustantivo (adjetivo) y buscarlo en el diccionario", ["ignorar toda la oración y seguir leyendo sin entender nada", "traducir cada palabra por separado sin mirar el contexto"], "La posición ayuda a deducir su categoría."),
        mc("Un diccionario da dos significados de bank: 'a place for money' y 'the side of a river'. En 'We sat on the bank of the river' ¿cuál corresponde?", "el borde de un río", ["el lugar para el dinero", "ninguno"], "El contexto indica river."),
    ],
    [mc("Quieres decir 'una decisión rápida'. ¿Qué opción es correcta?", "a quick decision", ["a quick decide", "a quickly decision"], "Quick es adjetivo y decision es sustantivo.")],
    sc(3, 2, [
        ("¿Qué es una familia de palabras?", "Palabras con una raíz común, de distintas categorías", "Por ejemplo decide, decision y decisive."),
        ("¿Qué indica la abreviatura adj. en un diccionario?", "Que la palabra es un adjetivo", "Indica la categoría."),
        ("¿Cómo se elige un significado de un diccionario?", "Con el contexto de la oración", "Se elige el que encaja."),
    ]),
    task("Completa con la forma correcta de la palabra entre paréntesis y justifica en español la categoría: 1) She made a ___ (decide). 2) He spoke very ___ (clear). 3) The ___ (improve) of the park was fast. 4) It is a very ___ (help) tool.", "1) decision (sustantivo tras artículo). 2) clearly (adverbio que modifica spoke). 3) improvement (sustantivo con -ment tras the). 4) helpful (adjetivo antes de tool).", ["forma correcta", "categoría justificada", "usa la posición y el sufijo"], ["cuatro respuestas con justificación"], ["usar el verbo en vez del sustantivo", "no justificar"], "Observa qué función cumple la palabra en la oración y elige el sufijo."),
    "Arma la familia de palabras de care: care, careful, carefully, careless, carelessly.",
    "Elige cinco palabras de un texto en inglés que tengas a mano y escribe su categoría.",
)

# ------------------------------------------------------------------ clase 3: voz pasiva y oraciones de relativo
PASS = "«Plastic bottles are collected every week in our school. The bottles are taken to a plant, where they are sorted and recycled. The project was started by a group of students, who also made posters.» (collected = recolectadas, plant = planta, sorted = clasificadas, recycled = recicladas, posters = afiches)"

lesson(
    OA3, 3, MAT_R,
    "Aprenderé la voz pasiva (be + participio) y las oraciones de relativo (who, which, that, whose, where) para entender textos más densos y escribir ideas con precisión. Sirve para usar mi conocimiento del inglés de manera estratégica.",
    ["Sé usar el pasado simple y conozco los participios más comunes.", "Sé reconocer sujetos y objetos."],
    [
        "En la voz pasiva (passive voice) lo importante es la acción o el resultado, no quién la hace. Se forma con be + participio: Plastic bottles are collected (presente), The project was started (pasado). El agente se puede omitir o añadir con by: ... by a group of students. Se usa cuando el agente es desconocido, obvio o poco importante: The window was broken. Participios irregulares útiles: make → made, write → written, take → taken, choose → chosen, give → given, build → built, see → seen.",
        "Las oraciones de relativo (relative clauses) dan información sobre un sustantivo. Who se usa para personas, which para cosas, that para personas o cosas en oraciones que identifican, whose indica posesión y where indica lugar. Las oraciones especificativas (defining) no llevan comas y son necesarias para identificar: The teacher who organized the project is Ms. Rojas. Las explicativas (non-defining) llevan comas, agregan información extra y no usan that: My sister, who lives abroad, is a nurse.",
        "Por qué importa: la pasiva y los relativos son frecuentes en noticias, informes y ensayos. Con ellos puedes unir ideas en una sola oración y evitar repeticiones: I met a student. She won the prize → I met a student who won the prize. Revisa siempre que el participio sea el correcto y que el pronombre relativo corresponda al sustantivo.",
    ],
    [("passive voice", "voz pasiva: be + participio"), ("by + agent", "por + quien hace la acción"), ("who / which / that", "quien / que (cosas) / que"), ("whose", "cuyo"), ("where", "donde"), ("defining / non-defining", "especificativa / explicativa")],
    [
        ("Reconocer la pasiva", PASS + " ¿Qué verbo muestra que no se dice quién recoge las botellas?", ["Busco be + participio.", "Are collected es pasiva.", "No aparece el agente."], "Are collected (pasiva sin agente)"),
        ("Elegir el relativo", PASS + " ¿A quién se refiere who en who also made posters?", ["Who se usa para personas.", "Se refiere a a group of students.", "Ellos hicieron los afiches."], "A un grupo de estudiantes"),
    ],
    [
        ("Escribir was wrote en lugar de was written.", "En la pasiva se usa el participio, no el pasado.", "Aprende write, wrote, written."),
        ("Usar that en una oración explicativa con comas.", "Con comas se usa which o who, no that.", "Escribe My sister, who lives abroad, ..."),
    ],
    [
        mc("¿Cuál oración está en voz pasiva?", "Plastic bottles are collected every week", ["Students collect plastic bottles", "Students are collecting bottles"], "Se forma con be + participio."),
        mr(PASS, "¿Cuál es el participio de take en el texto?", "taken", ["took", "taking"], "Are taken usa el participio."),
        mr(PASS, "¿Quién empezó el proyecto?", "un grupo de estudiantes", ["la municipalidad", "los profesores"], "Dice was started by a group of students."),
    ],
    [
        mr(PASS, "¿Qué se hace con las botellas en la planta?", "se clasifican y se reciclan", ["se venden y se comen", "se guardan sin usar"], "They are sorted and recycled."),
        mr(PASS, "¿Qué significa where en where they are sorted and recycled?", "en la planta", ["en el colegio", "en la calle"], "Where se refiere al lugar mencionado, a plant."),
        mc("¿Para qué se usa la voz pasiva en 'The window was broken'?", "porque no se sabe o no importa quién la rompió", ["porque la acción no ocurrió en realidad", "porque la oración es una pregunta"], "Se centra en el resultado."),
    ],
    [
        mc("Convierte a pasiva: 'Students collect the bottles.'", "The bottles are collected by students", ["The bottles collect students", "The bottles were collecting students"], "El objeto pasa a sujeto y se usa be + participio."),
        mc("Completa: 'The teacher ___ organized the project is Ms. Rojas.'", "who", ["whose", "where"], "Who se usa para personas."),
        mc("Completa: 'The book ___ cover is red is mine.'", "whose", ["who", "which"], "Whose indica posesión."),
    ],
    [
        mc("Compara: 1) 'My brother who lives abroad is a nurse.' 2) 'My brother, who lives abroad, is a nurse.' ¿Qué sugiere la primera?", "que hay otros hermanos y se identifica a uno", ["que vive en la casa de la familia", "que no tiene otros hermanos más que él"], "Sin comas la oración identifica entre varios."),
        mc("¿Cuándo es útil la voz pasiva?", "cuando el agente es desconocido o poco importante", ["cuando se quiere nombrar siempre al agente", "cuando se hace una pregunta"], "Pone el foco en la acción."),
    ],
    [
        mc("Corrige: 'The report was wrote by two students.'", "The report was written by two students", ["The report was writing by two students", "The report is wrote by two students"], "El participio de write es written."),
        mc("Une: 'I met a student. She won the prize.'", "I met a student who won the prize", ["I met a student which won the prize", "I met a student whose won the prize"], "Who se refiere a personas."),
    ],
    [mc("Completa: 'The park ___ opened last month has a new playground.'", "that", ["whose", "where"], "That puede referirse a cosas en una oración especificativa.")],
    sc(3, 3, [
        ("¿Cómo se forma la voz pasiva?", "Be + participio", "Por ejemplo, is collected."),
        ("¿Cuándo no se usa that?", "En oraciones explicativas entre comas", "Se usa who o which."),
        ("¿Qué indica whose?", "Posesión", "Equivale a cuyo."),
    ]),
    task("Escribe en inglés tres oraciones sobre tu colegio: una en voz pasiva sin agente, una en voz pasiva con by y una con who o which para unir dos ideas. (colegio = school)", "The playground is cleaned every day. The mural was painted by a group of students. I know a teacher who runs the music club.", ["una pasiva sin agente", "una pasiva con by", "una oración de relativo"], ["tres oraciones"], ["usar el pasado en lugar del participio", "usar which para personas"], "Revisa be + participio y el pronombre."),
    "Escribe tres oraciones activas y conviértelas en pasivas.",
    "Une cuatro pares de oraciones con who, which, whose y where.",
)

# ------------------------------------------------------------------ clase 4: verbos de reporte, afirmación y evidencia
ART = "«The mayor claims that the new bus line has reduced traffic. A local study, however, points out that traffic fell only in the morning. Critics argue that the city should publish more data, and the mayor admits that the figures are not complete.» (mayor = alcalde, claims = afirma, reduced = redujo, local study = estudio local, points out = señala, critics = críticos, argue = sostienen, publish = publicar, admits = reconoce, figures = cifras; texto de ejemplo)"

lesson(
    OA3, 4, MAT_R,
    "Aprenderé a usar verbos de reporte (claim, argue, suggest, point out, admit, deny) para distinguir afirmaciones de evidencia y para expresar mi postura con precisión. Sirve para comprender y producir textos con sentido crítico.",
    ["Sé usar voz pasiva y relativos.", "Sé distinguir hechos y opiniones."],
    [
        "Los verbos de reporte (reporting verbs) introducen lo que otras personas dicen y muestran la actitud de quien reporta. Say es neutro. Claim (afirmar) indica algo que se dice sin que esté probado; argue (sostener) presenta un argumento; suggest (sugerir) es suave; point out (señalar) presenta algo como un hecho; admit (reconocer) indica una concesión; deny (negar) rechaza una acusación; insist (insistir) muestra firmeza. Se usan con that: The mayor claims that traffic has fallen.",
        "Una afirmación (claim) debe separarse de su evidencia (evidence): datos, estudios o ejemplos comprobables. En el texto, el alcalde afirma una reducción del tráfico, un estudio señala que solo bajó en la mañana y los críticos piden más datos. Para evaluar, pregunta: ¿quién lo dice?, ¿qué evidencia hay?, ¿qué verbo eligió el autor? Claim puede indicar duda, mientras que point out indica que algo se presenta como hecho.",
        "Al escribir tu postura, reporta con justicia. Elige un verbo neutro o preciso, no uno que desacredite sin razones. Puedes expresar prudencia con may, seems y suggests. Por ejemplo: The study suggests that traffic fell only in the morning, so the claim may be incomplete. Reporta lo que dice la fuente, separa tu opinión y usa un tono respetuoso.",
    ],
    [("claim", "afirmar (sin prueba)"), ("argue", "sostener, argumentar"), ("suggest", "sugerir"), ("point out", "señalar"), ("admit / deny", "reconocer / negar"), ("evidence", "evidencia")],
    [
        ("Distinguir afirmación y evidencia", ART + " ¿Qué es una afirmación del alcalde y qué es evidencia?", ["Claims introduce la afirmación del alcalde.", "El estudio local aporta evidencia sobre la mañana.", "La afirmación es que el tráfico se redujo; la evidencia matiza que fue solo en la mañana."], "Afirmación: el tráfico se redujo; evidencia: el estudio señala que bajó solo en la mañana"),
        ("Elegir el verbo adecuado", ART + " ¿Qué muestra el verbo admits sobre el alcalde?", ["Admit indica un reconocimiento.", "El alcalde reconoce algo que no le favorece.", "Sus cifras no están completas."], "Que reconoce que las cifras no están completas"),
    ],
    [
        ("Pensar que claim siempre significa que es falso.", "Claim indica que no está probado, no que sea falso.", "Busca evidencia para decidir."),
        ("Usar deny cuando alguien solo explica.", "Deny rechaza una acusación.", "Usa say, explain o point out."),
    ],
    [
        mr(ART, "¿Qué afirma el alcalde?", "que la nueva línea de bus ha reducido el tráfico", ["que no hay datos sobre el tráfico en toda la ciudad", "que el estudio local es falso y no sirve para nada"], "Dice the mayor claims that the new bus line has reduced traffic."),
        mr(ART, "¿Qué señala el estudio local?", "que el tráfico bajó solo en la mañana", ["que el tráfico bajó todo el día", "que no hay tráfico"], "Points out that traffic fell only in the morning."),
        mr(ART, "¿Qué piden los críticos?", "que la ciudad publique más datos", ["que se cierre la línea", "que se baje el precio"], "Argue that the city should publish more data."),
    ],
    [
        mc("¿Qué verbo presenta algo como un hecho?", "point out", ["claim", "suggest"], "Point out presenta un dato como cierto."),
        mc("¿Qué verbo es más suave?", "suggest", ["insist", "deny"], "Suggest propone sin imponer."),
        mr(ART, "¿Qué actitud del autor muestra la palabra claims?", "que lo afirmado aún no está comprobado", ["que está seguro de que es falso", "que está de acuerdo"], "Claim indica una afirmación no probada."),
    ],
    [
        mc("Completa: 'The report ___ that the data are incomplete.' (señala como hecho)", "points out", ["claims", "denies"], "Points out presenta un hecho."),
        mc("Completa: 'The company ___ that it caused the problem, but the video shows otherwise.' (rechaza)", "denies", ["admits", "points out"], "Deny rechaza una acusación."),
        mc("Completa: 'The author ___ that cities need more green spaces.' (presenta un argumento)", "argues", ["admits", "denies"], "Argue presenta un argumento."),
    ],
    [
        mc(ART + " Un compañero resume este texto diciendo 'The mayor lied.' ¿Qué problema tiene?", "el texto no dice que mintió; solo que afirma algo y reconoce cifras incompletas", ["usa mal el pasado del verbo lie, que debería estar en presente simple", "falta el sujeto de la oración, por eso el resumen no se entiende bien"], "Se debe reportar con justicia y sin acusar sin pruebas."),
        mc("¿Cuál resumen separa mejor afirmación y evidencia?", "The mayor claims that traffic fell, but a study points out that it fell only in the morning", ["The mayor is right and the study is wrong, so traffic fell all day in the city", "The study is wrong, so the mayor lied to everybody about the new bus line"], "Distingue qué dice quién."),
    ],
    [
        mc("Debes expresar prudencia sobre el estudio. ¿Qué frase sirve?", "The study suggests that the result may be partial", ["The study proves everything about the result", "The study is useless, so ignore the result"], "Suggests y may marcan prudencia."),
        mc("¿Qué reporte es más respetuoso con una postura distinta de la tuya?", "Some people argue that tablets distract students", ["People who say that are silly", "Fools believe that tablets distract"], "Reporta la postura sin burlarse."),
    ],
    [mc("Un vecino afirma: «The new park is the best in the world.» sin dar datos. ¿Cómo lo reportas con precisión?", "A neighbor claims that the new park is the best in the world, without giving data", ["A neighbor proves that the new park is the best in the world, with strong data", "A neighbor admits that the new park is the best in the world, without data"], "Claim indica que no hay pruebas.")],
    sc(3, 4, [
        ("¿Qué indica claim en un reporte?", "Que se afirma algo que aún no está comprobado", "No significa que sea falso."),
        ("¿Qué indica point out?", "Que se presenta algo como un hecho", "Señala un dato."),
        ("¿Por qué separar afirmación y evidencia?", "Para evaluar si lo dicho se apoya en datos", "Es parte del análisis crítico."),
    ]),
    task("Lee: «A company says its new soda is healthy. A nutrition report points out that one bottle has more sugar than the daily recommendation. The company denies this and insists that its data are correct.» (soda = bebida, healthy = saludable, sugar = azúcar, daily recommendation = recomendación diaria; texto de ejemplo). Escribe en español qué afirma cada parte, qué verbos usa el texto y una postura prudente con may o suggests.", "La empresa afirma que la bebida es saludable. El informe señala que una botella tiene más azúcar que la recomendación diaria. La empresa niega y asegura que sus datos son correctos. Los verbos son says, points out, denies e insists. Una postura prudente: Los datos del informe sugieren que la bebida podría no ser tan saludable, pero habría que revisar ambas fuentes.", ["separa quién afirma qué", "nombra los verbos de reporte", "plantea una postura prudente"], ["tres respuestas en español"], ["decidir sin evidencia", "confundir points out con says"], "Subraya los verbos de reporte y busca la evidencia que cada uno introduce."),
    "Escribe tres frases que reporten lo que dice una persona con claim, point out y admit.",
    "Elige una noticia en español y reescríbela con dos verbos de reporte en inglés.",
)

# ================================================================= OA 04
# ------------------------------------------------------------------ clase 1: conversar y debatir
DISC = "«Ana: I think every student should learn a second foreign language. Ben: I take your point, but I'm not so sure. Some students already find English difficult. Ana: That's a fair concern. What do you think about making it optional? Ben: Optional could work. Carla, you haven't spoken yet. What's your view? Carla: I partly agree with Ana. A second language opens doors, but time is limited. Ana: To sum up, we agree that language learning matters, but we disagree on whether it should be compulsory.» (take your point = entiendo tu punto, fair concern = preocupación razonable, optional = optativo, view = opinión, partly = en parte, compulsory = obligatorio)"

lesson(
    OA4, 1, MAT_L,
    "Aprenderé a participar en una conversación o debate breve: dar y pedir opiniones, estar de acuerdo o en desacuerdo, invitar a hablar, resumir y respetar los turnos. Sirve para interactuar con fluidez y tomar conciencia de mi propia postura frente a otras visiones de mundo.",
    ["Sé presentarme y hacer preguntas abiertas.", "Sé discrepar con cortesía."],
    [
        "En una conversación o debate se usan frases para cada función. Dar la opinión: I think that..., In my view..., As far as I'm concerned. Pedir la opinión: What do you think?, What's your view?, How do you feel about...? Estar de acuerdo: I totally agree, That's a good point, I take your point. Estar en desacuerdo con cortesía: I'm not so sure, I see it differently, I partly agree, but... Invitar a hablar: You haven't spoken yet. What's your view? Interrumpir con cortesía: Sorry to interrupt, but..., May I add something?",
        "También hay frases para resumir: To sum up,... , So we agree that... and disagree on... y para ceder el turno: Go ahead, Please continue. Un buen debate respeta los turnos, escucha antes de responder y critica ideas, no personas. La fluidez no significa hablar mucho: significa que tus aportes se entiendan y que el diálogo avance.",
        "Cuando el tema es de interés común (idiomas, transporte, tecnología) varias posturas son válidas. Practica distinguir lo que acuerdan y lo que no. Identificar tus valores y los de otras personas te ayuda a conocerte mejor: quizá valoras la oportunidad, la comodidad o la equidad. Nombrarlos hace más claro tu aporte.",
    ],
    [("I take your point", "entiendo tu punto"), ("I'm not so sure", "no estoy tan seguro"), ("What's your view?", "¿cuál es tu opinión?"), ("May I add something?", "¿puedo agregar algo?"), ("To sum up", "para resumir"), ("compulsory / optional", "obligatorio / optativo")],
    [
        ("Reconocer funciones", ADULT + DISC + " ¿Qué función cumple la frase de Ben, Carla, you haven't spoken yet?", ["Ben le habla a Carla, que no había hablado.", "La invita a dar su opinión.", "Su función es invitar a participar."], "Invitar a Carla a dar su opinión"),
        ("Resumir", ADULT + DISC + " ¿En qué coinciden y en qué no?", ["Coinciden en que aprender idiomas importa.", "No coinciden en si debe ser obligatorio.", "Ana lo resume en to sum up."], "Coinciden en la importancia de aprender idiomas; no en que sea obligatorio"),
    ],
    [
        ("Hablar sin dejar hablar a otros.", "El diálogo se transforma en monólogo.", "Invita a otros con What's your view?"),
        ("Decir You are wrong como desacuerdo.", "Ataca a la persona y no argumenta.", "Usa I see it differently."),
    ],
    [
        ml(DISC, "¿Qué opina Ana al inicio?", "que todos deberían aprender un segundo idioma", ["que nadie debe aprender otros idiomas", "que el inglés es suficiente para todos"], "Dice every student should learn a second foreign language."),
        ml(DISC, "¿Qué dice Ben sobre algunos estudiantes?", "que ya les cuesta el inglés", ["que dominan el francés", "que no quieren estudiar"], "Dice some students already find English difficult."),
        mc("¿Qué frase pide la opinión de otra persona?", "What's your view?", ["I totally agree", "To sum up"], "Pide una opinión."),
    ],
    [
        ml(DISC, "¿Qué propone Ana después de la preocupación de Ben?", "hacerlo optativo", ["eliminarlo", "hacerlo solo para algunos"], "Dice What do you think about making it optional?"),
        mc("¿Qué frase muestra desacuerdo parcial?", "I partly agree, but", ["I totally agree", "You are wrong"], "Reconoce parte de la postura y matiza."),
        mc("¿Cuál frase interrumpe con cortesía?", "Sorry to interrupt, but may I add something?", ["That's wrong, let me talk now because it is my turn to speak", "Stop talking and listen to me, because I know the answer here"], "Pide permiso antes de intervenir."),
    ],
    [
        mc("Estás de acuerdo con una compañera pero tienes una duda. ¿Qué dices?", "That's a good point, but I'm not sure about the cost", ["No way, that costs too much", "Whatever, I do not care about the cost"], "Reconoce y plantea la duda."),
        mc("Dos compañeros no se ponen de acuerdo sobre usar uniforme. ¿Qué frase resume bien?", "To sum up, we agree that comfort matters, but we disagree on uniforms", ["We are all wrong about comfort and uniforms, so nobody can decide", "Nobody speaks, so there is nothing to sum up about the discussion"], "Resume coincidencia y diferencia."),
        mc("Quieres darle la palabra a alguien que no ha hablado. ¿Qué dices?", "We haven't heard from you yet. What do you think?", ["Be quiet and let the others speak, because you talk too much", "Why are you silent all the time? You never say anything at all"], "Invita sin presionar."),
    ],
    [
        mc("Un compañero dice que, para tener fluidez, hay que hablar sin parar para no perder el turno. ¿Qué respuesta es correcta?", "la fluidez incluye escuchar, esperar el turno y hacerse entender", ["la fluidez es hablar rápido y sin detenerse, aunque nadie entienda", "tiene razón: hay que ocupar todo el turno para no perder la palabra"], "La fluidez en una conversación es hacer que avance con claridad."),
        mc("Ana dice 'we disagree on whether it should be compulsory'. ¿Qué actitud muestra?", "reconoce con respeto una diferencia que quedó sin resolver", ["se enoja con los demás por no estar de acuerdo", "evita el tema para no seguir discutiendo"], "Resume sin imponer."),
    ],
    [
        mc("Debes dar una opinión sobre usar el celular en el recreo. ¿Qué respuesta combina postura, razón y cortesía?", "In my view, phones should be allowed because breaks are for rest, but I take your point", ["Phones are good, period, and nobody should discuss this with me any more", "I don't know if phones should be allowed, because I have no view on it"], "Tiene postura, razón y concesión."),
        mc("Escuchas una opinión muy distinta de la tuya. ¿Qué es lo mejor?", "preguntar: Could you tell me more about why you think so?", ["decirle de inmediato que está equivocado", "irte de la conversación sin responderle"], "Escuchar ayuda a comprender otras visiones de mundo."),
    ],
    [mc("Quieres decir 'Entiendo tu punto pero pienso distinto'. ¿Qué frase sirve?", "I take your point, but I see it differently", ["I am agree with you, but no", "You are right, but you are wrong"], "Es una forma cortés de discrepar.")],
    sc(4, 1, [
        ("¿Cómo se invita a alguien a hablar?", "What's your view?", "Es una pregunta de invitación."),
        ("¿Para qué sirve To sum up?", "Para resumir lo acordado y lo no acordado", "Cierra la conversación."),
        ("¿Qué significa I'm not so sure?", "No estoy tan seguro", "Es un desacuerdo suave."),
    ]),
    task("Escribe en inglés un diálogo de al menos cinco intervenciones entre tres estudiantes que opinan sobre 'Should schools have a longer lunch break?' (lunch break = hora de almuerzo). Incluye dar una opinión, I take your point, una invitación a hablar, una interrupción cortés y To sum up.", "A: In my view, schools should have a longer lunch break. B: I take your point, but I'm not so sure. The day would finish later. A: That's fair. C, you haven't spoken yet. What's your view? C: I partly agree. A longer break gives time to rest. B: Sorry to interrupt, but may I add something? Many students take the bus after school. C: Go ahead. A: To sum up, we agree that rest matters, but we disagree on the finish time.", ["usa los cinco elementos", "mantiene el respeto", "resume con claridad"], ["diálogo de al menos cinco intervenciones"], ["omitir la invitación a hablar", "criticar a la persona"], "Marca las cinco funciones; agrega las que falten."),
    "Lee en voz alta tu diálogo con dos personas de tu casa, cada una con un rol.",
    "Escribe cinco frases para estar de acuerdo, en desacuerdo y pedir opinión.",
)

# ------------------------------------------------------------------ clase 2: diferencias culturales de comunicación
CASE1 = "«A student on exchange asks to change rooms. The host says, 'That might be difficult.' The student thinks it means 'maybe'. The host meant 'probably not'.» (exchange = intercambio, host = anfitrión, change rooms = cambiar de habitación; caso de ejemplo)"
CASE2 = "«A guest is invited for dinner at seven. In some places, arriving ten minutes after seven is polite; in others, it is rude. A good guest can ask: 'What time should I arrive?'» (guest = invitado, rude = descortés, arrive = llegar; caso de ejemplo)"
INTV = "«Interviewer: Tell me about yourself. Student: I am seventeen and I live in a small city. I love science, and last year I volunteered at a community garden. I would like to study biology because I enjoy understanding how living things work. Interviewer: Why should we choose you? Student: I am organized and I work well in a team.» (interviewer = entrevistador, volunteered = fui voluntario, community garden = huerto comunitario, living things = seres vivos, organized = organizado, team = equipo)"

lesson(
    OA4, 2, MAT_R,
    "Aprenderé a notar diferencias en cómo las personas se comunican (directo o indirecto, puntualidad, cortesía, registro formal) sin estereotipar, y a prepararme para entrevistas y encuentros formales. Sirve para interactuar con fluidez en situaciones que involucran otras visiones de mundo.",
    ["Sé reconocer la cortesía y el significado implícito.", "Sé evitar generalizaciones sobre grupos."],
    [
        "Las personas se comunican con distintos estilos. Un estilo directo dice lo que quiere con pocos rodeos (No, I can't); uno indirecto lo sugiere (That might be difficult). Ninguno es mejor: dependen de la cultura, la situación y la relación. Hay también diferencias en la puntualidad (llegar justo a la hora o un poco después), en el espacio personal, en cuánto se conversa antes de ir al tema y en los saludos. Son tendencias (tendencies), no reglas para todas las personas.",
        "Para evitar malentendidos, pregunta con cortesía: What time should I arrive?, Do you mean...?, Is it okay if...? y observa lo que hace la mayoría de las personas en esa situación. No supongas que todas las personas de un lugar se comportan igual y evita los estereotipos. Tu propia manera de comunicarte también es cultural: puedes explicarla si crees que se malinterpreta.",
        "En una entrevista formal (de beca, estudio o trabajo) se usa registro formal y una estructura clara: presente (I am seventeen), pasado reciente (last year I volunteered), futuro (I would like to study biology) y una razón (because...). Habla de tus fortalezas con ejemplos y evita datos demasiado personales. La fluidez se nota en respuestas ordenadas, no en la velocidad.",
    ],
    [("direct / indirect", "directo / indirecto"), ("tendency", "tendencia: no es regla"), ("stereotype", "estereotipo"), ("What time should I arrive?", "¿a qué hora debo llegar?"), ("interview", "entrevista"), ("strength", "fortaleza")],
    [
        ("Interpretar un estilo indirecto", CASE1 + " ¿Qué quiso decir realmente el anfitrión?", ["That might be difficult es una frase indirecta.", "El texto dice que quiso decir probably not.", "Quiso decir que probablemente no."], "Que probablemente no se podía cambiar de habitación"),
        ("Organizar una respuesta de entrevista", INTV + " ¿Qué tiempos verbales usa el estudiante para presentarse?", ["Usa presente: I am seventeen.", "Usa pasado: I volunteered.", "Usa condicional de deseo: I would like to study."], "Presente, pasado reciente y deseo para el futuro"),
    ],
    [
        ("Pensar que todas las personas de un lugar se comportan igual.", "Es un estereotipo; hay diversidad.", "Habla de tendencias y pregunta."),
        ("Responder a una entrevista con una sola palabra.", "No entrega información suficiente.", "Responde con una razón y un ejemplo."),
    ],
    [
        mr(CASE1, "¿Qué piensa el estudiante que significa 'That might be difficult'?", "que tal vez se pueda", ["que no se puede", "que está prohibido"], "El estudiante lo interpreta como maybe."),
        mr(CASE2, "¿Qué puede preguntar un buen invitado?", "What time should I arrive?", ["Why are you late?", "Where is the food?"], "Es una forma cortés de aclarar."),
        mr(INTV, "¿Qué estudio le interesa a la estudiante?", "biología", ["historia", "música"], "Dice I would like to study biology."),
    ],
    [
        mr(INTV, "¿Qué experiencia reciente menciona?", "fue voluntaria en un huerto comunitario", ["trabajó en una tienda del barrio", "viajó al extranjero con su familia"], "Dice last year I volunteered at a community garden."),
        mr(INTV, "¿Qué fortaleza menciona?", "ser organizada y trabajar bien en equipo", ["hablar muy rápido en inglés", "ser la mejor alumna de su curso"], "Dice I am organized and I work well in a team."),
        mc("¿Qué estilo muestra la frase 'No, I can't come on Friday'?", "directo", ["indirecto", "silencioso"], "Dice no claramente."),
    ],
    [
        mc("Un amigo extranjero llega 15 minutos tarde a una cena en tu casa y dice 'Sorry!'. ¿Qué es lo más adecuado?", "recibirlo con cortesía y preguntar cómo llegó; en muchas partes la puntualidad varía", ["asumir que es descortés siempre y decírselo delante de todos tus invitados", "no dejarlo entrar porque llegó tarde y eso es una falta de respeto"], "Se evita el estereotipo y se comprende la diferencia."),
        mc("¿Qué frase es más adecuada en una entrevista formal?", "I would like to study biology because I enjoy science", ["Dunno, biology maybe, I guess, because my friends will study it too", "I wanna do biology, it is cool and I like it a lot, you know"], "Es formal y da una razón."),
        mc("Quieres aclarar una respuesta indirecta. ¿Qué dices?", "Do you mean it is probably not possible?", ["You are lying, so just tell me no", "Whatever, I will not ask again"], "Es una pregunta de aclaración cortés."),
    ],
    [
        mc("Un compañero dice 'Todas las personas de ese país son indirectas'. ¿Cuál es una mejor formulación?", "Some people may be more indirect in certain situations", ["Everyone there is always indirect with everybody", "Nobody there ever says no to anything"], "Cuantifica y habla de tendencias."),
        mc("Un entrevistador pregunta 'Why should we choose you?'. ¿Qué respuesta es más completa?", "I am organized, and last year I led a school project", ["I don't know, nobody has asked me that", "Because I want the place, that's why"], "Da una fortaleza y un ejemplo."),
    ],
    [
        mc("Te invitan a un evento y no sabes cómo vestirte. ¿Qué haces?", "preguntar: What should I wear?", ["no ir", "imaginar lo que prefieras sin preguntar"], "Preguntar evita malentendidos."),
        mc("Tu estilo es directo y tu anfitrión es indirecto. ¿Qué podrías hacer?", "explicar que a ti te ayuda una respuesta clara y preguntar con cortesía", ["enojarte porque no te dan una respuesta clara y directa a tu pregunta", "cambiar tu personalidad para parecerte a él y no tener más problemas"], "Explicar tu estilo y preguntar ayuda."),
    ],
    [mc("En una entrevista no entiendes una pregunta. ¿Qué dices?", "Sorry, could you rephrase the question, please?", ["What? I did not understand a thing", "I don't care about this question"], "Es una petición cortés.")],
    sc(4, 2, [
        ("¿Qué es un estilo de comunicación indirecto?", "Uno que sugiere sin decir directamente", "Ninguno es mejor."),
        ("¿Por qué hablar de tendencias y no de reglas?", "Porque las personas de un lugar son diversas", "Así se evitan los estereotipos."),
        ("¿Qué estructura tiene una buena respuesta de entrevista?", "Presente, pasado reciente, futuro y una razón", "Se ordena con claridad."),
    ]),
    task("Responde en inglés, en cuatro o cinco oraciones, a la pregunta de entrevista «Tell me about yourself» (de ejemplo). Incluye tu edad o curso, algo que haces ahora, una experiencia pasada, lo que te gustaría estudiar y por qué. Usa registro formal.", "I am seventeen and I am a fourth-year student. I like drawing and I am learning to program. Last year I helped organize a school fair. I would like to study architecture because I enjoy designing spaces. I am organized and creative.", ["usa presente, pasado y deseo", "da una razón", "registro formal"], ["respuesta de cuatro o cinco oraciones"], ["responder con una palabra", "usar jerga"], "Ordena tu respuesta presente, pasado y futuro y agrega una razón."),
    "Escribe dos formas indirectas de decir no con cortesía.",
    "Haz tres preguntas para saber cómo vestirte, a qué hora llegar y qué llevar a un evento.",
)

# ------------------------------------------------------------------ clase 3: valores, planes e identidad
SELF = "«My name is Valentina. What matters most to me is honesty. I come from a family that values education. I'm good at organizing events, and I'm proud of the school garden project I led. After school, I'm going to apply to a university, and I hope to study environmental engineering. If I could change one thing in my community, I would build more safe bike lanes.» (honesty = honestidad, values = valora, organizing = organizar, proud = orgullosa, led = lideré, apply = postular, environmental engineering = ingeniería ambiental, community = comunidad, safe = seguras)"

lesson(
    OA4, 3, MAT_R,
    "Aprenderé a hablar de mis valores, planes e identidad en inglés usando frases como What matters most to me is..., I'm proud of..., I'm going to..., I hope to... y el segundo condicional (If I could, I would). Sirve para interactuar con fluidez y tomar conciencia de quién soy frente a otras visiones de mundo.",
    ["Sé usar el segundo condicional.", "Sé presentarme y comparar costumbres."],
    [
        "Para hablar de mis valores (values) uso What matters most to me is..., I care about..., I believe in..., I value... Para hablar de mi origen: I come from a family that..., I grew up in... Para hablar de mis fortalezas: I'm good at..., I'm proud of... Para planes: I'm going to... (plan decidido), I hope to... (deseo posible), I'd like to... (deseo cortés), I plan to... (intención).",
        "El segundo condicional permite imaginar un cambio: If I could change one thing in my community, I would build more safe bike lanes. If + pasado simple, would + verbo base. Sirve para decir lo que harías en una situación hipotética y revela tus prioridades. Evita hablar mal de otras personas; centra la frase en lo que valoras.",
        "La identidad (identity) no es fija ni única: tiene muchas partes (familia, lengua, intereses, ideas) y cambia con el tiempo. Al compartirla con alguien de otra cultura, elige lo que quieras mostrar y ofrece ejemplos concretos. No hace falta que coincidas con otros: basta que seas claro y escuches. Conocerte mejor te ayuda a entender también a quienes piensan distinto.",
    ],
    [("What matters most to me", "lo que más me importa"), ("I'm proud of", "estoy orgulloso/a de"), ("I'm going to / I hope to", "voy a / espero"), ("If I could, I would", "si pudiera, haría"), ("identity", "identidad"), ("value", "valor / valorar")],
    [
        ("Reconocer valores", SELF + " ¿Qué es lo que más le importa a Valentina?", ["Busco What matters most to me.", "Dice honesty.", "Es la honestidad."], "La honestidad"),
        ("Usar el segundo condicional", SELF + " ¿Qué haría Valentina si pudiera cambiar algo de su comunidad?", ["Busco If I could.", "Después aparece would build.", "Construiría más ciclovías seguras."], "Construiría más ciclovías seguras"),
    ],
    [
        ("Decir If I will have time, I would go.", "En el segundo condicional se usa pasado después de if.", "Escribe If I had time, I would go."),
        ("Usar I'm going to para algo que solo deseas.", "I'm going to expresa un plan decidido.", "Usa I hope to."),
    ],
    [
        mr(SELF, "¿Qué hace bien Valentina?", "organizar eventos", ["cocinar", "dibujar"], "Dice I'm good at organizing events."),
        mr(SELF, "¿De qué se siente orgullosa?", "del proyecto de huerto escolar que lideró", ["de un premio de música que ganó", "de un viaje al extranjero que hizo"], "Dice I'm proud of the school garden project I led."),
        mr(SELF, "¿Qué valora su familia?", "la educación", ["los deportes", "el dinero"], "Dice a family that values education."),
    ],
    [
        mr(SELF, "¿Qué plan decidido expresa I'm going to?", "postular a una universidad", ["viajar a otro país", "cambiar de colegio"], "Dice I'm going to apply to a university."),
        mr(SELF, "¿Qué desea estudiar Valentina?", "ingeniería ambiental", ["medicina", "arte"], "Dice I hope to study environmental engineering."),
        mc("¿Qué frase expresa un deseo posible, no un plan seguro?", "I hope to travel", ["I'm going to travel on Monday", "I traveled"], "Hope to expresa deseo."),
    ],
    [
        mc("Completa: 'If I ___ more time, I would learn another language.'", "had", ["have", "will have"], "Segundo condicional: if + pasado."),
        mc("Completa: 'If I could choose, I ___ study music.'", "would", ["will", "am"], "Segundo condicional: would + verbo."),
        mc("¿Qué frase expresa un valor?", "What matters most to me is respect", ["I am tall and I like sports", "I go to school every morning"], "What matters most to me is... expresa un valor."),
    ],
    [
        mc("Un compañero dice que su identidad es solo su nacionalidad. ¿Qué respuesta es adecuada?", "la identidad tiene muchas partes: familia, intereses, ideas y cambia en el tiempo", ["tiene razón: la identidad es solo la nacionalidad que se tiene al nacer y no cambia", "la identidad no existe, es solo una idea que inventan las personas"], "Es una construcción de varias partes."),
        mc("¿Qué frase evita hablar mal de otros y expresa un valor?", "What matters to me is that everybody has a place to study", ["People are awful because they do not study", "Those who don't study are lazy and should be ashamed"], "Se centra en lo que valoras."),
    ],
    [
        mc("Debes describir en inglés un plan de futuro y una razón. ¿Qué opción es mejor?", "I hope to study nursing because I want to help people", ["I like help, and nursing is a job that I want to have one day", "Nursing is nice and I like it a lot, and also I like doctors"], "Incluye un deseo y una razón."),
        mc("Escribes: 'If I could change one thing in my school, I would add a quiet room.' ¿Qué muestra?", "una prioridad: el valor de la tranquilidad", ["que ya tienes una sala tranquila", "que no te interesa el cambio"], "El condicional revela lo que valoras."),
    ],
    [mc("Quieres decir con cortesía 'Me gustaría conocer su país algún día'. ¿Qué frase sirve?", "I would like to visit your country one day", ["I want visiting your country one day", "I will to visit your country one day"], "Would like to + verbo base es cortés.")],
    sc(4, 3, [
        ("¿Cómo se dice lo que más me importa?", "What matters most to me is...", "Presenta un valor."),
        ("¿Cuál es la fórmula del segundo condicional?", "If + pasado simple, would + verbo base", "Habla de lo hipotético."),
        ("¿Por qué la identidad tiene muchas partes?", "Porque incluye familia, intereses, ideas y experiencias", "No es única ni fija."),
    ]),
    task("Escribe en inglés un texto de seis oraciones sobre tu identidad (de ejemplo): un valor, algo de tu familia o comunidad, algo en lo que eres bueno/a, algo de lo que estás orgulloso/a, un plan con I'm going to o I hope to, y un segundo condicional con If I could, I would. Comparte solo lo que quieras mostrar.", "What matters most to me is respect. I come from a family that likes cooking together. I'm good at explaining things. I'm proud of helping my class with a school fair. After school, I hope to study design. If I could change one thing in my town, I would build more parks.", ["incluye las seis partes", "usa el condicional correcto", "no revela datos demasiado privados"], ["texto de seis oraciones"], ["omitir el condicional", "usar will después de if"], "Revisa cada parte y corrige el condicional con if + pasado, would + verbo."),
    "Habla durante un minuto sobre lo que más te importa, con una persona de tu casa.",
    "Escribe tres frases con If I could, I would sobre tu colegio, tu barrio y tu país.",
)

# ------------------------------------------------------------------ clase 4: diálogo intercultural
VID = "«Lena: Our school starts at eight. When does yours start? Tomás: At eight too, but we finish later. Lena: Interesting! Do you think a later start would help? Tomás: I'm not sure. If it started later, many families would need to change their schedules. What do you think? Lena: I understand. In my town, some students travel a long way, so a later start could help them. If I understand correctly, you are worried about family schedules? Tomás: Yes, exactly. Maybe we agree that it depends on the situation.» (schedules = horarios, travel a long way = viajar mucho, worried = preocupado, depends on = depende de; diálogo de ejemplo)"

lesson(
    OA4, 4, MAT_L,
    "Aprenderé a sostener un diálogo intercultural breve: preguntar, escuchar, parafrasear lo que dijo la otra persona, mostrar un punto de vista propio y buscar acuerdos. Sirve para producir y comprender con fluidez situaciones comunicativas que involucran otras visiones de mundo y la mía.",
    ["Sé conversar y debatir con cortesía.", "Sé hablar de mis valores y planes."],
    [
        "Un diálogo intercultural (intercultural dialogue) es una conversación entre personas con distintos contextos. Su meta no es ganar, sino comprender y, si es posible, encontrar acuerdos. Pasos útiles: 1) preguntar por el contexto del otro (When does yours start?), 2) mostrar interés (Interesting!), 3) dar tu opinión con cuidado (I'm not sure; I think that...), 4) parafrasear (If I understand correctly, you are worried about...), 5) buscar un punto en común (Maybe we agree that it depends).",
        "Parafrasear (paraphrase) lo que dijo la otra persona demuestra que escuchaste y evita malentendidos: So what you're saying is..., If I understand correctly, you think that..., In other words, ... La otra persona puede confirmar (Yes, exactly) o corregir (Not exactly. What I mean is...). Usa el segundo condicional para imaginar sin imponer: If it started later, many families would need to change their schedules.",
        "Mantén la curiosidad. Pregunta más en lugar de suponer: Could you tell me more about...? Reconoce lo valioso del contexto del otro (In my town it is different) y describe el tuyo sin presentarlo como el mejor. Tu forma de ver el mundo también se conoce al explicarla: puedes descubrir tus propios valores al compararlos con los de otra persona.",
    ],
    [("intercultural dialogue", "diálogo intercultural"), ("paraphrase", "parafrasear"), ("If I understand correctly", "si entiendo bien"), ("Could you tell me more about...?", "¿podrías contarme más sobre...?"), ("common ground", "punto en común"), ("It depends on the situation", "depende de la situación")],
    [
        ("Parafrasear", ADULT + VID + " ¿Cómo parafrasea Lena la preocupación de Tomás?", ["Busco If I understand correctly.", "Dice you are worried about family schedules.", "Eso es parafrasear."], "If I understand correctly, you are worried about family schedules"),
        ("Buscar un punto en común", ADULT + VID + " ¿Qué acuerdan al final?", ["Busco Maybe we agree.", "Dicen que depende de la situación.", "Ese es el punto en común."], "Que depende de la situación"),
    ],
    [
        ("Responder sin haber entendido la opinión del otro.", "El diálogo se trunca.", "Parafrasea para comprobar."),
        ("Presentar tu contexto como el único razonable.", "Cierra la conversación.", "Describe tu contexto como una posibilidad."),
    ],
    [
        ml(VID, "¿A qué hora empieza la escuela de Lena?", "a las ocho", ["a las nueve", "a las siete"], "Dice Our school starts at eight."),
        ml(VID, "¿Qué diferencia hay en la escuela de Tomás?", "termina más tarde", ["empieza más tarde", "no tiene recreo"], "Dice we finish later."),
        ml(VID, "¿Por qué le preocupa un horario más tarde a Tomás?", "porque muchas familias tendrían que cambiar sus horarios", ["porque nadie desayuna en su casa temprano", "porque los profesores llegarían tarde a clases"], "Dice many families would need to change their schedules."),
    ],
    [
        ml(VID, "¿Por qué un inicio más tarde podría ayudar en el pueblo de Lena?", "porque algunos estudiantes viajan mucho", ["porque todos duermen muy poco", "porque hace mucho frío en el pueblo"], "Dice some students travel a long way."),
        mc("¿Qué frase sirve para parafrasear?", "So what you're saying is that you prefer to keep it as it is", ["I don't care what you prefer to do, because I have my own plan", "You are wrong, and you should change it as soon as possible"], "Repite la idea con otras palabras."),
        mc("¿Qué frase invita a profundizar?", "Could you tell me more about your schedule?", ["Why is your schedule so strange", "That's all I wanted to know"], "Muestra curiosidad por el otro."),
    ],
    [
        mc("Tu compañera extranjera te cuenta que en su colegio no hay uniforme. ¿Qué respuesta mantiene el diálogo?", "Interesting! How do students decide what to wear?", ["That's weird; in my school we wear uniforms", "We are better because we have a uniform"], "Muestra interés y pregunta."),
        mc("Completa para imaginar sin imponer: 'If we ___ a later start, students would sleep more.'", "had", ["have", "will have"], "Es segundo condicional: if más pasado."),
        mc("Un interlocutor corrige tu parafraseo: 'Not exactly'. ¿Qué haces?", "pedirle que explique y volver a parafrasear", ["insistir en tu versión sin escuchar", "terminar el diálogo de inmediato"], "La corrección ayuda a entender mejor."),
    ],
    [
        mc("Un compañero dice que el diálogo intercultural solo sirve para convencer al otro. ¿Qué respuesta es correcta?", "su meta es comprender y buscar acuerdos posibles", ["se trata de evitar el tema siempre", "tiene razón: se trata de ganar la discusión"], "Se trata de comprender."),
        ml(VID, "¿Qué hace Lena para mostrar que escuchó a Tomás?", "parafrasea su preocupación", ["cambia de tema", "interrumpe"], "Dice If I understand correctly, you are worried about family schedules."),
    ],
    [
        mc("Debes iniciar un diálogo con un estudiante extranjero sobre el transporte en su ciudad. ¿Cuál es la mejor pregunta?", "How do students usually get to school in your city?", ["Why is school so far from the houses in your city, is it bad", "Is your city bad for students, or is it just very big"], "Es abierta y respetuosa."),
        mc("Tras una opinión diferente de la tuya, ¿qué frase busca acuerdo?", "Maybe we agree that it depends on the situation", ["You are wrong about the situation, and I will not agree with it", "Nothing matters in the situation, so we do not need to agree"], "Reconoce una base compartida."),
    ],
    [mc("Quieres describir tu contexto sin presentarlo como el mejor. ¿Qué frase sirve?", "In my town, students usually go by bus, but it is different elsewhere", ["In my town everything is better than elsewhere, especially the buses", "Only my town has buses for students, and no other place does"], "Describe sin comparar para ganar.")],
    sc(4, 4, [
        ("¿Qué es parafrasear en un diálogo?", "Decir con otras palabras lo que dijo el otro", "Comprueba que se entendió."),
        ("¿Cuál es la meta de un diálogo intercultural?", "Comprender y buscar acuerdos posibles", "No se trata de ganar."),
        ("¿Para qué sirve Could you tell me more about...?", "Para invitar a profundizar con curiosidad", "Muestra interés por la otra persona."),
    ]),
    task("Escribe en inglés un diálogo de seis a ocho líneas entre tú y un estudiante de otro país sobre el tema 'tiempo libre después de clases' (free time after school). Incluye una pregunta sobre el contexto del otro, una opinión tuya, una paráfrasis con If I understand correctly, un segundo condicional y un punto en común.", "A: What do students usually do after school in your town? B: Many go to the park or help at home. A: Interesting! In my town, many students join clubs. B: I'm not sure about clubs. If we had more time, we would join one. A: If I understand correctly, you would like clubs but you don't have time? B: Yes, exactly. A: Maybe we agree that free time matters.", ["incluye los cinco elementos", "mantiene un tono respetuoso", "no estereotipa"], ["diálogo de seis a ocho líneas"], ["omitir la paráfrasis", "presentar un contexto como el mejor"], "Marca los cinco elementos y agrega los que falten."),
    "Practica el diálogo con una persona de tu casa, alternando roles.",
    "Escribe cinco preguntas abiertas para conocer el contexto de un estudiante extranjero.",
)

# ------------------------------------------------------------------ clase 5: reparar, reformular y reflexionar
REFL = "«Before the exchange, I thought that people from other places would find my customs strange. I was wrong. I learned that many of us care about the same things, such as family and respect, but we show them differently. I also noticed that I am proud of my sense of humor and my way of welcoming guests. Next time, I will ask more questions before I make assumptions.» (exchange = intercambio, customs = costumbres, noticed = noté, sense of humor = sentido del humor, welcoming = recibir, assumptions = suposiciones; reflexión de ejemplo)"

lesson(
    OA4, 5, MAT_R,
    "Aprenderé a reparar y reformular lo que digo, a negociar significados cuando hay malentendidos y a escribir una reflexión sobre lo que aprendí de otras visiones de mundo y de mi identidad. Sirve para interactuar con fluidez y tomar conciencia de quién soy.",
    ["Sé parafrasear lo que dice otra persona.", "Sé hablar de mis valores e identidad."],
    [
        "Cuando hay un malentendido, negociar el significado (negotiate meaning) es probar diferentes formas hasta entenderse. Reformula: What I mean is..., Let me put it another way... Pide aclaración: What do you mean by...?, Do you mean...? Confirma: So you're saying that..., Is that right? Corrige una suposición: I thought that..., but now I understand that... Mantén la calma y el respeto: un malentendido no es culpa de nadie, es una oportunidad.",
        "Tras una experiencia intercultural, reflexiona por escrito. Una reflexión (reflection) tiene cuatro partes: qué pensabas antes (I thought that...), qué descubriste (I learned that...), qué notaste de ti (I also noticed that I am proud of...), y qué harás distinto (Next time, I will...). Usa pasado para lo ocurrido, presente para lo que valoras y futuro con will para el compromiso.",
        "La autoevaluación (self-assessment) te ayuda a seguir aprendiendo: ¿puedo presentarme?, ¿puedo explicar mi opinión?, ¿puedo pedir aclaraciones?, ¿puedo parafrasear?, ¿puedo evitar estereotipos? Identifica una fortaleza y una meta. Aprender sobre otras visiones de mundo no cambia tu valor ni tu identidad: les da más claridad.",
    ],
    [("negotiate meaning", "negociar el significado"), ("Let me put it another way", "déjame decirlo de otra forma"), ("assumption", "suposición"), ("reflection", "reflexión"), ("self-assessment", "autoevaluación"), ("I was wrong", "me equivoqué")],
    [
        ("Reconocer partes de la reflexión", REFL + " ¿Qué parte corresponde a lo que la autora aprendió?", ["Busco I learned that.", "Dice many of us care about the same things.", "Esa es la parte de aprendizaje."], "I learned that many of us care about the same things, but we show them differently."),
        ("Reformular", "Dijiste 'It's a pain' (a pain = una molestia) y tu amiga no entendió. ¿Cómo reformulas? A) What I mean is that it is annoying. B) Whatever.", ["Busco una frase de reformulación.", "What I mean is... explica con otras palabras.", "Whatever no aclara."], "A) What I mean is that it is annoying."),
    ],
    [
        ("Culpar a la otra persona por un malentendido.", "Un malentendido es compartido.", "Reformula con calma."),
        ("Escribir una reflexión sin decir qué harás distinto.", "Falta el compromiso.", "Agrega Next time, I will..."),
    ],
    [
        mr(REFL, "¿Qué pensaba la autora antes del intercambio?", "que su costumbre sería extraña para otros", ["que nadie tiene costumbres", "que todos eran iguales a ella"], "Dice I thought that people from other places would find my customs strange."),
        mr(REFL, "¿Qué descubrió sobre otras personas?", "que muchas cuidan lo mismo, como la familia y el respeto", ["que no valoran la familia ni el respeto en sus propias casas", "que no tienen costumbres propias y siguen las de los demás"], "Dice many of us care about the same things."),
        mr(REFL, "¿Qué hará distinto la autora?", "hacer más preguntas antes de suponer", ["hablar menos con las personas nuevas", "viajar más a otros países"], "Dice Next time, I will ask more questions."),
    ],
    [
        mr(REFL, "¿De qué se siente orgullosa la autora?", "de su sentido del humor y de cómo recibe a los invitados", ["de sus notas y de lo bien que le va en su colegio", "de su casa y de los muebles que tiene en ella"], "Dice I am proud of my sense of humor and my way of welcoming guests."),
        mc("¿Qué frase pide aclaración?", "What do you mean by 'a pain'?", ["I know everything", "You never explain"], "Pide el significado."),
        mc("¿Qué frase confirma lo que entendiste?", "So you're saying that the meeting is moved, is that right?", ["You said nothing about a meeting, so I do not understand you", "Whatever, I understood it all and I do not need to confirm"], "Confirma y da lugar a corregir."),
    ],
    [
        mc("Completa para reflexionar: 'I thought that all families celebrated in the same way, but I ___ that there are many ways.'", "learned", ["learns", "learning"], "Pasado simple para lo ocurrido."),
        mc("Completa: 'Next time, I ___ ask more questions.'", "will", ["would to", "am"], "Will expresa un compromiso futuro."),
        mc("¿Qué frase corrige una suposición de forma adecuada?", "I thought that you were upset, but now I understand that you were just tired", ["I knew it all along, you were upset and you did not want to say it", "You were upset, period, and that is that, so there is nothing to discuss"], "Reconoce el cambio de idea."),
    ],
    [
        mc("Un compañero dice que reflexionar significa decidir cuál cultura es mejor. ¿Qué respuesta es correcta?", "reflexionar es comprender diferencias y conocerse mejor, no elegir una mejor", ["tiene razón: se trata de elegir la mejor cultura después de comparar", "no sirve para nada en una conversación porque no cambia lo que piensas"], "La reflexión se centra en aprender."),
        mc("Después de una conversación te das cuenta de que usaste un estereotipo. ¿Qué es lo mejor?", "reconocerlo con respeto y corregirlo: I made an assumption, sorry", ["negarlo y decir que no fue así, porque nadie lo notó en la conversación", "irte sin decir nada del tema, para evitar una discusión más larga"], "Reparar es parte de la interacción."),
    ],
    [
        mc("Haces una autoevaluación. ¿Cuál es la mejor meta?", "Next month I will practice paraphrasing in three conversations", ["I will be perfect next month and I will never make a mistake", "I will not speak in conversations because it is too difficult"], "Es concreta y alcanzable."),
        mc("Una persona dice algo que no entiendes y se produce un silencio. ¿Qué haces?", "pedir aclaración y volver a intentarlo", ["fingir que entendiste", "cambiar de tema sin avisar"], "Negociar el significado evita errores."),
    ],
    [mc("Quieres cerrar tu reflexión con un compromiso respetuoso. ¿Qué frase sirve?", "I will listen first and judge later", ["I will always be right", "I will avoid other cultures"], "Es abierto y respetuoso.")],
    sc(4, 5, [
        ("¿Qué es negociar el significado?", "Probar formas de decir hasta entenderse", "Se reformula, se pide aclaración y se confirma."),
        ("¿Qué partes tiene una reflexión?", "Qué pensaba, qué aprendí, qué noté de mí y qué haré distinto", "Cierra con un compromiso."),
        ("¿Para qué sirve la autoevaluación?", "Para ver fortalezas y fijar metas", "Ayuda a seguir aprendiendo."),
    ]),
    task("Escribe una reflexión de cinco oraciones en inglés tras una conversación (de ejemplo) con un estudiante de otro país: qué pensabas antes (I thought that...), qué aprendiste (I learned that...), qué notaste de ti (I also noticed that...), qué harás distinto (Next time, I will...) y una meta de autoevaluación.", "I thought that students in other countries had very different days. I learned that many of them also share meals and homework. I also noticed that I am proud of how I explain ideas. Next time, I will ask more questions. My goal is to practice paraphrasing every week.", ["usa las cinco estructuras", "no juzga la otra cultura", "fija una meta concreta"], ["reflexión de cinco oraciones"], ["omitir el compromiso", "decir que una cultura es mejor"], "Marca las cinco partes y agrega las que falten."),
    "Haz tu autoevaluación con cinco preguntas can-do y marca sí, a veces o aún no.",
    "Escribe cinco frases de reformulación y aclaración que quieras recordar.",
)
