"""Cuaderno del estudiante, 1.º medio Orientación: OA 09 (opciones académicas y laborales) y OA 10 (diseño flexible y responsable de proyectos de vida)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA9, OA10 = "OR1M OA 09", "OR1M OA 10"


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 09
lesson(
    OA9, 1,
    "Una hoja y un lápiz. El perfil de Tamara, una estudiante inventada, está escrito en los ejercicios. No necesitas contar tu propio perfil.",
    "Aprenderé a conocer los caminos académicos y laborales que existen después de la enseñanza media y a relacionarlos con las habilidades e intereses de un caso. Sirve para contrastar opciones con información y no con rumores.",
    ["Sé separar intereses, capacidades y condiciones (OA 01).", "Sé que tengo derecho a elegir sin discriminación."],
    [
        "En 1.º y 2.º medio todos los estudiantes cursan una formación común. En 3.º y 4.º medio hay tres modalidades: humanístico-científica, que profundiza en áreas como ciencias, humanidades o matemática; técnico-profesional, que enseña una especialidad para trabajar o seguir estudiando; y artística, que desarrolla las artes. Cada una abre caminos hacia el estudio superior o hacia el trabajo.",
        "Después de la enseñanza media hay varios caminos. Se puede estudiar en una universidad, en un instituto profesional o en un centro de formación técnica, o bien trabajar y capacitarse, emprender un negocio o combinar estudio y trabajo. Cada camino pide habilidades distintas, tiene duraciones y costos distintos y puede cambiar con el tiempo. Ninguno es mejor para todos: depende de los intereses, las habilidades y las condiciones de cada persona.",
        "Una habilidad es algo que haces bien o puedes aprender, como comunicarte, resolver problemas, trabajar con las manos, organizar o crear. Para examinar un caso, se anotan las habilidades y los intereses de la persona y se buscan caminos que se relacionen con ellos, sin descartar otros que también podrían servirle.",
    ],
    [("modalidad", "tipo de formación que se elige en 3.º y 4.º medio"), ("formación técnico-profesional", "modalidad que enseña una especialidad para trabajar o seguir estudiando"), ("educación superior", "estudios después de la enseñanza media, en universidades, institutos o centros técnicos"), ("habilidad", "algo que una persona hace bien o puede aprender"), ("emprender", "iniciar un negocio o proyecto propio")],
    [
        W("Relacionar habilidades y caminos", "Tamara es hábil para arreglar aparatos y le gusta ver cómo funcionan. ¿Qué modalidad de 3.º y 4.º medio se relaciona con eso?", ["Le interesa una especialidad práctica.", "La modalidad técnico-profesional enseña especialidades."], "La modalidad técnico-profesional"),
        W("No descartar otros caminos", "Tamara también escribe bien y le gusta ayudar. ¿Se puede descartar la modalidad humanístico-científica?", ["Escribir y ayudar también son habilidades.", "No se descarta ningún camino sin informarse."], "No, sigue siendo una opción"),
    ],
    [
        M("Creer que hay un solo camino «correcto» después del colegio.", "Se piensa que todos deben seguir lo mismo.", "Hay varios caminos y se eligen según intereses, habilidades y condiciones."),
        M("Pensar que una modalidad impide para siempre seguir estudiando.", "No se conoce que hay puentes entre caminos.", "Infórmate: muchos caminos se pueden combinar o retomar."),
    ],
    R=[
        ex("¿Cuáles son las tres modalidades de 3.º y 4.º medio? A) Humanístico-científica, técnico-profesional y artística B) Humanística, comercial y deportiva", "A", "Son las tres modalidades que nombra la clase."),
        ex("¿Cuál de estas es una habilidad? A) Organizar el trabajo de un grupo B) Vivir lejos de la ciudad", "A", "Es algo que se hace o se puede aprender; vivir lejos es una condición."),
        ex("Julián vende en ferias artesanías que él mismo hace. ¿Qué camino sigue? A) Emprender B) Estudiar en un centro de formación técnica", "A", "Inició un negocio propio."),
    ],
    U=[
        ex("¿Qué modalidad enseña una especialidad para trabajar o seguir estudiando? A) La técnico-profesional B) La artística.", "A", "Prepara en un oficio o especialidad."),
        ex("¿Qué camino se relaciona con estudiar en una universidad? A) La educación superior B) El emprendimiento.", "A", "Las universidades son parte de la educación superior."),
        ex("Rafael quiere ganar dinero y a la vez estudiar. ¿Qué existe para eso? A) Combinar trabajo y estudios, por ejemplo con clases vespertinas B) No es posible hacer ambas cosas", "A", "Es una posibilidad que muchas personas usan."),
    ],
    A=[
        ex("Tamara revisa esta lista: 1) organizar una fiesta de curso; 2) vivir a 40 minutos de la ciudad; 3) resolver problemas de matemática; 4) tener un computador compartido. Escribe los números de las habilidades, separados por coma.", "1, 3", "Organizar y resolver problemas se hacen o se aprenden; vivir lejos y compartir un computador son condiciones."),
        ex("A Tamara le encantan el dibujo y el diseño. ¿Qué modalidad de 3.º y 4.º medio se relaciona más con eso? A) La artística B) La técnico-profesional en mecánica.", "A", "Desarrolla las artes y el diseño."),
        ex("Un amigo dice: «Si elijo técnico-profesional, ya no podré seguir estudiando». ¿Qué conviene hacer? A) Informarse sobre cómo seguir estudiando después B) Creerle sin preguntar.", "A", "Muchos caminos permiten continuar estudios."),
    ],
    Z=[
        ex("¿Por qué no se debe elegir un camino solo porque «todos lo hacen»?", "Porque cada persona tiene intereses y condiciones propias", "Lo que le sirve a otros puede no servirte."),
        ex("Tamara tiene dos intereses: tecnología y cuidar personas. ¿Qué conviene? A) Buscar caminos que combinen ambos o probar ambos B) Descartar uno.", "A", "Varias carreras unen tecnología y salud."),
    ],
    D=[
        arith("Un liceo inventado tiene 4 especialidades técnicas y cada una tiene 3 cursos. ¿Cuántos cursos técnicos tiene?", "4*3", "Se multiplican especialidades por cursos."),
        arith("De 120 estudiantes de 1.º medio de un colegio inventado, 45 dicen que quieren estudiar en una universidad. ¿Cuántos no lo dicen?", "120-45", "Al total se le restan los que sí lo dicen."),
    ],
    context=[ex("En una feria del colegio hay stands de un liceo técnico, de un instituto y de una universidad. ¿Qué conviene hacer en cada stand? A) Preguntar qué se estudia, cuánto dura y qué habilidades piden B) Elegir el stand que tenga la fila más corta.", "A", "Se obtiene información útil para decidir.")],
    selfcheck=[ex("En Orientación: ¿en 3.º y 4.º medio hay tres modalidades?", "Sí", "Humanístico-científica, técnico-profesional y artística."), ex("¿Un solo camino sirve para todas las personas?", "No", "Depende de intereses y condiciones."), ex("¿Es importante informarse antes de descartar un camino?", "Sí", "Evita decisiones basadas en rumores.")],
    task=T("Lee el perfil inventado de Mateo: le gusta cocinar para su familia, es ordenado, se pone nervioso al hablar en público, no le gustan mucho las matemáticas y vive a 30 minutos en bus de la ciudad. Escribe: tres habilidades o intereses, dos caminos posibles (uno de estudio y otro laboral) y una pregunta que le harías a una persona que trabaje en algo relacionado.", "Habilidades e intereses: cocinar, orden, preocuparse por su familia. Caminos: carrera técnica en gastronomía; trabajar en una cocina y capacitarse. Pregunta: ¿cómo es un día normal en tu trabajo?", ["identifica tres habilidades o intereses", "propone dos caminos", "formula una pregunta abierta", "no descarta caminos sin información"], ["lista escrita", "texto oral"], ["descartar sin informarse", "ignorar las condiciones"], "Reconoce los caminos relacionados con el perfil y pregunta qué dato faltaría."),
    reinforce="Anota tres habilidades de un personaje inventado y un camino que se relacione con cada una.",
    extend="Explica por qué un camino puede cambiar con el tiempo.",
)

lesson(
    OA9, 2,
    "Una hoja y un lápiz. Las frases sobre estudios y trabajo están escritas en los ejercicios; son datos generales, no cifras exactas.",
    "Aprenderé a distinguir hechos, mitos y requisitos reales sobre estudiar y trabajar, y qué derechos me protegen al elegir. Sirve para no descartar opciones por rumores ni por estereotipos.",
    ["Sé que existen distintas modalidades y caminos.", "Sé que un estereotipo no es un hecho."],
    [
        "Algunos hechos sobre el sistema: la educación superior se ofrece en universidades, institutos profesionales y centros de formación técnica; las carreras técnicas de nivel superior suelen durar cerca de dos años, las profesionales de institutos suelen ser de unos cuatro años y las universitarias suelen ser de entre cuatro y seis años (son duraciones habituales, no siempre iguales). Para entrar a muchas universidades se rinde una prueba de acceso y se consideran las notas.",
        "También hay mitos frecuentes: «la formación técnica es para quienes no sirven para estudiar», «solo la universidad da un buen futuro» o «esa carrera es de hombres». Los tres son falsos o injustos. Cada camino exige esfuerzo y tiene valor, y los estereotipos de género limitan alternativas sin razón. Tienes derecho a elegir sin discriminación por género, origen o situación económica.",
        "Hay también límites reales y límites aparentes. Un límite real, por ejemplo, es el requisito de edad o los años de estudio. Uno aparente puede ser el dinero, porque existen ayudas y becas, o la distancia, porque hay otras formas de estudiar. Antes de descartar, revisa fuentes oficiales y pregunta a personas que conozcan el tema.",
    ],
    [("instituto profesional", "institución de educación superior que forma profesionales"), ("centro de formación técnica", "institución de educación superior que forma técnicos"), ("prueba de acceso", "evaluación que se rinde para postular a muchas universidades"), ("mito", "idea muy repetida que no se puede comprobar"), ("beca", "ayuda económica para estudiar")],
    [
        W("Mito o hecho", "«La formación técnica es solo para quienes no pueden estudiar». ¿Es hecho o mito?", ["Los técnicos tienen una formación específica y exigente.", "La frase generaliza sin pruebas."], "Mito"),
        W("Límite real o aparente", "Camilo piensa: «No puedo estudiar porque no tengo dinero hoy». Hay becas y ahorro posible. ¿Qué tipo de límite es?", ["El dinero puede cambiar con ayudas.", "No es un límite definitivo."], "Un límite aparente"),
    ],
    [
        M("Creer que el título de universidad garantiza por sí solo un buen trabajo.", "Se simplifica una realidad compleja.", "El resultado depende del esfuerzo, la elección y el contexto."),
        M("Descartar una carrera porque «es de otro género».", "Se acepta un estereotipo.", "Tienes derecho a elegir sin discriminación."),
    ],
    R=[
        ex("«Esa carrera es solo de hombres», ¿es un hecho o un estereotipo?", "Un estereotipo", "Generaliza sin considerar a cada persona."),
        ex("Camilo no puede pagar la matrícula este año, pero existe una ayuda económica para estudiar. ¿Cómo se llama? A) Beca B) Prueba de acceso", "A", "La beca es una ayuda económica."),
        ex("¿Qué institución forma técnicos de nivel superior? A) Un centro de formación técnica B) Un instituto profesional", "A", "Es una institución de educación superior que forma técnicos."),
    ],
    U=[
        ex("¿Cuál es un hecho? A) Las carreras técnicas de nivel superior suelen durar cerca de dos años B) Solo la universidad da futuro.", "A", "La primera es una duración habitual; la segunda es un mito."),
        ex("Un requisito de edad mínima, ¿es un límite real o aparente? A) Real B) Aparente.", "A", "No se puede cambiar con esfuerzo."),
        ex("¿Qué hacer antes de descartar un camino? A) Revisar fuentes oficiales y preguntar a personas expertas B) Dejarse llevar por un rumor.", "A", "Evita decidir con información falsa."),
    ],
    A=[
        ex("Clasifica con H (hecho) o M (mito): 1) Hay becas para estudiar. 2) Las mujeres no pueden ser ingenieras. 3) Los institutos forman profesionales. Escribe las letras en orden.", "H, M, H", "La 1 y la 3 son verificables; la 2 es un estereotipo."),
        ex("Una carrera técnica dura 4 semestres. Si cada año tiene 2 semestres, ¿cuántos años dura?", "2", "4 semestres divididos en 2 por año dan 2 años."),
        ex("Valentina quiere estudiar mecánica y le dicen «es de hombres». ¿Qué derecho puede recordar? A) Elegir su carrera sin discriminación B) Tener las mismas notas que todos.", "A", "La elección de estudios no se limita por género."),
    ],
    Z=[
        ex("¿Por qué no se debe decir que un camino es «mejor» para todos?", "Porque depende de los intereses, habilidades y condiciones de cada persona", "Cada persona tiene un contexto distinto."),
        ex("Un joven descarta estudiar porque «es muy caro». ¿Qué debería hacer antes? A) Averiguar becas, créditos y alternativas B) Descartar estudiar, porque el costo no va a cambiar.", "A", "El costo puede tener soluciones."),
    ],
    D=[
        arith("Una carrera dura 8 semestres. Ya cursó 5. ¿Cuántos semestres le faltan?", "8-5", "A la duración se le restan los semestres cursados."),
        arith("Una institución inventada tiene 600 estudiantes, de los cuales 240 reciben beca. ¿Cuántos no reciben beca?", "600-240", "Al total se le restan los que reciben beca."),
    ],
    context=[ex("En la feria, un folleto dice: «Estudia con nosotros y tendrás trabajo asegurado». ¿Qué debes hacer? A) Dudar y revisar si la institución está acreditada y qué datos entrega B) Creerle porque está impreso.", "A", "Una promesa sin datos debe verificarse.")],
    selfcheck=[ex("En Orientación: ¿hay becas para estudiar?", "Sí", "Existen ayudas económicas."), ex("¿Los estereotipos de género limitan las alternativas?", "Sí", "Las reducen sin motivo."), ex("¿Una promesa sin datos debe comprobarse?", "Sí", "Puede ser engañosa.")],
    task=T("Lee las cinco frases inventadas de un grupo de amigos: (a) «Los institutos forman profesionales»; (b) «Solo la universidad sirve»; (c) «Para matricularse en cierto curso de conducción profesional hay que tener 18 años» (dato inventado); (d) «Esa carrera es solo para hombres»; (e) «No tengo dinero hoy, así que nunca podré estudiar». Clasifica cada frase como hecho, mito (o estereotipo), límite real o límite aparente, y explica una con una frase.", "(a) hecho; (b) mito; (c) límite real; (d) estereotipo; (e) límite aparente: se puede buscar becas o ahorrar.", ["clasifica las cinco frases", "explica una con una razón", "distingue límite real de aparente", "no usa cifras inventadas como reales"], ["tabla escrita", "texto oral"], ["aceptar un mito", "confundir límite real con aparente"], "Reconoce las clasificaciones y pregunta qué fuente usaría para comprobar una."),
    reinforce="Escribe un mito sobre estudios y reescríbelo como una pregunta que podrías investigar.",
    extend="Explica por qué una promesa de «trabajo asegurado» debe verificarse.",
)

lesson(
    OA9, 3,
    "Una hoja y un lápiz. Los tres caminos de Camila, una estudiante inventada, y la tabla de criterios están escritos en los ejercicios.",
    "Aprenderé a comparar caminos académicos y laborales con criterios y a prever sus consecuencias a corto y largo plazo. Sirve para decidir con una mirada amplia y para tener un plan alternativo.",
    ["Sé distinguir hechos y mitos sobre estudios.", "Sé comparar alternativas con criterios."],
    [
        "Para contrastar caminos se usa una tabla con criterios. Criterios útiles: interés (me atrae), habilidades (puedo desarrollarlas), duración, costo, condiciones de ingreso, posibilidades de seguir creciendo (estudiar más o cambiar de área) y bienestar (cómo me sentiría). Cada camino se evalúa con datos y no con rumores.",
        "Las consecuencias pueden ser inmediatas o a largo plazo. Un camino corto puede dar trabajo antes pero pedir completar estudios más adelante. Uno largo puede costar más tiempo y dinero, pero abrir más posibilidades. Un camino combinado, como trabajar y estudiar de manera vespertina, exige organización y cansancio, pero aporta ingresos y experiencia.",
        "Es recomendable tener un plan B. Si el plan A no resulta, un plan B evita sentir que se perdió todo. También sirve revisar la elección: tus intereses pueden cambiar, y cambiar de camino no es fracasar. Decidir con información, con apoyo y con flexibilidad es parte de un proyecto de vida responsable.",
    ],
    [("criterio", "regla para comparar"), ("duración", "cuánto tiempo toma un estudio o camino"), ("costo", "dinero que hay que reunir para un camino"), ("plan B", "alternativa preparada por si el plan principal no resulta"), ("flexibilidad", "capacidad de ajustar un plan si cambian los datos")],
    [
        W("Comparar con criterios", "Camila compara dos caminos: carrera técnica de 2 años y carrera profesional de 5 años. Con el criterio «duración», ¿cuál es más corta?", ["2 años es menor que 5 años.", "La técnica dura menos."], "La carrera técnica"),
        W("Plan B", "Si el plan A de Camila es una universidad y no logra el ingreso, ¿qué puede ser su plan B?", ["Un instituto o un centro técnico.", "O trabajar y prepararse para postular de nuevo."], "Estudiar en un instituto o centro técnico, o trabajar y prepararse otra vez"),
    ],
    [
        M("Elegir solo por el camino más corto o más barato.", "Se mira un solo criterio.", "Compara varios criterios y las consecuencias."),
        M("No tener plan B porque «saldrá bien».", "Se confunde optimismo con planificación.", "Prepara una alternativa; no es pesimismo."),
    ],
    R=[
        ex("Ordena de la más corta a la más larga: A) carrera de 6 años; B) carrera de 2 años; C) carrera de 4 años. Escribe las letras en orden.", "B, C, A", "2 años es menos que 4 y 4 es menos que 6."),
        ex("Camila se prepara para una carrera muy competitiva y averigua otra carrera relacionada por si no queda. ¿Qué preparó? A) Un plan B B) Una promesa engañosa", "A", "Es una alternativa por si el plan A no resulta."),
        ex("Un estudiante cambia de camino al descubrir una carrera que le interesa más. ¿Cómo se entiende? A) Ajustó su plan con flexibilidad B) Fracasó", "A", "Cambiar con nueva información es flexibilidad."),
    ],
    U=[
        ex("¿Qué criterio revisa el dinero que hay que reunir? A) El costo B) El interés.", "A", "Es la cantidad de dinero necesaria."),
        ex("¿Qué ventaja tiene un camino más largo? A) Puede abrir más posibilidades B) Siempre es más barato.", "A", "Da más formación para seguir creciendo."),
        ex("¿Qué exige trabajar y estudiar a la vez? A) Mucha organización B) Poco esfuerzo porque tiene ingresos.", "A", "Hay que repartir el tiempo."),
    ],
    A=[
        ex("Camila puntúa 1 punto por criterio cumplido (interés, habilidades, costo posible, duración razonable). Camino A: interés sí, habilidades sí, costo posible no, duración razonable sí. Camino B: interés sí, habilidades no, costo posible no, duración razonable sí. ¿Cuántos puntos más tiene A que B?", "1", "A suma 3 puntos y B suma 2."),
        arith("Un camino cuesta $120.000 al mes durante 24 meses. ¿Cuántos pesos cuesta en total?", "120000*24", "Se multiplica el costo mensual por los meses.", " pesos"),
        ex("Camila sueña con medicina, pero sabe que el ingreso es muy competitivo. ¿Qué le recomiendas? A) Preparar un plan B relacionado con la salud B) No tener plan B.", "A", "Mantiene su interés y reduce el riesgo."),
    ],
    Z=[
        ex("¿Por qué conviene comparar varios criterios y no solo el costo?", "Porque el camino más barato puede no servir para sus intereses o habilidades", "Un solo criterio no muestra todo."),
        ex("Un amigo trabaja y estudia de noche. ¿Qué consecuencia a corto plazo es probable? A) Cansancio y poco tiempo libre B) Mucho tiempo libre.", "A", "Debe repartir su tiempo entre dos actividades."),
    ],
    D=[
        arith("Camila ahorra $25.000 al mes durante 10 meses. ¿Cuánto reúne?", "25000*10", "Se multiplican los pesos por los meses.", " pesos"),
        arith("Una carrera dura 10 semestres y otra 4. ¿Cuántos semestres más dura la larga?", "10-4", "A la duración mayor se le resta la menor."),
    ],
    context=[ex("Un estudiante inventado dice: «Me gustan tanto la música como la ingeniería». ¿Qué conviene hacer? A) Comparar caminos que combinen o permitan probar ambos B) Elegir uno al azar.", "A", "Se decide con información.")],
    selfcheck=[ex("En Orientación: ¿un plan B es útil?", "Sí", "Evita perderlo todo si algo falla."), ex("¿Comparar solo por el costo es suficiente?", "No", "Hay que mirar más criterios."), ex("¿Cambiar de camino es fracasar?", "No", "Es ajustar el plan.")],
    task=T("Camila inventada tiene tres caminos: (1) carrera técnica en enfermería de 2 años; (2) carrera profesional en kinesiología de 5 años; (3) trabajar de ayudante en una farmacia y capacitarse. Haz una tabla con cinco criterios (interés, habilidades, duración, costo, posibilidades de crecer), marca sí/no o un dato y escribe un plan B para el camino 2.", "Camino 1: interés sí, duración 2 años. Camino 2: interés sí, duración 5 años, costo mayor, crece más. Camino 3: ingreso inmediato, crece según capacitación. Plan B del 2: estudiar el camino 1 y luego continuar.", ["completa los cinco criterios", "usa datos y no rumores", "escribe un plan B", "mira corto y largo plazo"], ["tabla escrita", "texto oral"], ["usar un solo criterio", "no tener plan B"], "Reconoce los criterios aplicados y pregunta qué dato falta."),
    reinforce="Compara dos caminos de estudio de un personaje inventado con tres criterios.",
    extend="Explica por qué tener plan B no es pesimismo.",
)

lesson(
    OA9, 4,
    "Una hoja y un lápiz. Los pasos de exploración y las señales de información confiable están escritos en los ejercicios.",
    "Aprenderé a elegir pasos seguros para explorar caminos académicos y laborales (ferias, visitas, entrevistas) y a reconocer información engañosa. Sirve para decidir sin caer en promesas falsas.",
    ["Sé comparar caminos con criterios.", "Sé pedir ayuda y orientación."],
    [
        "Explorar es probar y conocer antes de decidir. Pasos seguros de exploración: asistir a ferias vocacionales con un adulto o el curso, visitar un liceo o instituto con aviso, entrevistar a una persona que trabaje en lo que te interesa, leer la malla de estudios de una carrera y probar actividades de poco riesgo, como un taller corto o un voluntariado con acompañamiento.",
        "Hay que cuidarse de la información engañosa. Señales de alerta: promesas de «empleo asegurado», presión para matricularse rápido, cobros por adelantado sin contrato, instituciones sin información clara de su acreditación y ofertas que piden datos personales o pago por transferencia a cuentas desconocidas. Una institución confiable entrega información comprobable y permite que tomes tiempo y consultes a un adulto.",
        "En una feria, anota preguntas útiles: qué se estudia, cuánto dura, cuánto cuesta, qué se necesita para ingresar y dónde trabajan quienes se titulan. Cuando alguien te pide dinero o datos personales, consulta primero a una persona adulta de confianza. Para decidir con calma, ten siempre a quién consultar.",
    ],
    [("explorar", "probar y conocer antes de decidir"), ("malla de estudios", "lista de asignaturas de una carrera"), ("acreditación", "reconocimiento de calidad que una institución puede recibir"), ("matricularse", "inscribirse en una institución para estudiar"), ("promesa engañosa", "oferta que asegura algo que no puede garantizar")],
    [
        W("Identificar una señal de alerta", "Un folleto dice: «Matricúlate hoy, empleo asegurado y paga por adelantado». ¿Qué señales de alerta aparecen?", ["Promete empleo asegurado.", "Presiona a matricularse hoy.", "Pide pago por adelantado."], "Empleo asegurado, presión y pago por adelantado"),
        W("Explorar de forma segura", "Mateo quiere conocer el oficio de electricista. Opción A: entrevistar a un electricista del colegio con un adulto presente. Opción B: ir solo a una obra desconocida. ¿Cuál es segura?", ["A es conocida y acompañada.", "B es un lugar desconocido."], "La opción A"),
    ],
    [
        M("Matricularse apurado «porque quedan pocos cupos».", "Se cede a la presión comercial.", "Pide tiempo, información y consulta a un adulto."),
        M("Entregar datos personales en una página desconocida para recibir información.", "Se confía en cualquier sitio.", "Usa fuentes oficiales y no des datos sin consultar."),
    ],
    R=[
        ex("Un mensaje dice: «Empleo asegurado si pagas hoy». ¿Qué es eso? A) Una señal de alerta B) Una garantía real", "A", "Nadie puede garantizar un empleo y presiona a pagar."),
        ex("Tomás conversa con una técnica en enfermería sobre cómo es su trabajo. ¿Qué hace? A) Explorar un camino B) Matricularse", "A", "Se informa antes de decidir."),
        ex("¿Qué muestra la malla de estudios de una carrera? A) Las asignaturas que se cursan B) El sueldo de quienes se titulan", "A", "Es la lista de asignaturas de la carrera."),
    ],
    U=[
        ex("¿Qué es lo más seguro en una feria vocacional? A) Ir con tu curso o con un adulto B) Entregar tus datos a cualquiera.", "A", "Hay acompañamiento y cuidado."),
        ex("¿Qué hace una institución confiable cuando dudas? A) Te deja tiempo para consultar a un adulto B) Te pide decidir el mismo día", "A", "No presiona para decidir."),
        ex("¿Qué dato conviene preguntar en un stand? A) Cuánto dura y cuánto cuesta B) Si regalan lápices.", "A", "Es información para decidir."),
    ],
    A=[
        ex("Clasifica con S (señal de alerta) o N (no alerta): 1) «Empleo asegurado»; 2) «Aquí está la malla de estudios y los costos»; 3) «Paga hoy o pierdes el cupo». Escribe las letras en orden.", "S, N, S", "La 1 y la 3 son promesa y presión."),
        ex("Una feria tiene 12 stands y Camila visita 5 en la mañana y 4 en la tarde. ¿Cuántos stands le quedan por visitar?", "3", "12 − 5 − 4 = 3."),
        ex("Un amigo recibe un mensaje: «Transfiere $30.000 hoy para reservar tu cupo». ¿Qué debe hacer? A) Consultar a un adulto y verificar la institución B) Transferir de inmediato.", "A", "Una presión de pago es una señal de alerta."),
    ],
    Z=[
        ex("¿Por qué no se debe pagar ni dar datos bajo presión?", "Porque puede ser un engaño y las decisiones importantes necesitan tiempo", "La presión busca evitar que pienses y consultes."),
        ex("¿Por qué conviene visitar con aviso y acompañamiento? A) Porque protege y permite aprender mejor B) Porque obliga a matricularse.", "A", "Es más seguro y útil."),
    ],
    D=[
        arith("Un estudiante inventado entrevista a 3 personas por semana durante 4 semanas. ¿Cuántas entrevistas hace?", "3*4", "Se multiplican entrevistas por semanas."),
        arith("De 25 preguntas preparadas para una feria, 18 se responden. ¿Cuántas quedan sin responder?", "25-18", "Al total se le restan las respondidas."),
    ],
    context=[ex("Te llega por redes una oferta: «Curso técnico en 2 meses con título oficial, sin ir a clases, paga ya». ¿Qué debes hacer? A) Dudar, consultar a un adulto y revisar fuentes oficiales B) Pagar para asegurar el cupo.", "A", "Hay varias señales de alerta.")],
    selfcheck=[ex("En Orientación: ¿explorar es probar y conocer antes de decidir?", "Sí", "Es una forma de informarse."), ex("¿Se debe pagar por presión?", "No", "Es una señal de alerta."), ex("¿Se consulta a un adulto ante una oferta dudosa?", "Sí", "Ayuda a decidir con cuidado.")],
    task=T("Lee las cuatro situaciones inventadas: (a) una feria vocacional del colegio; (b) un mensaje que dice «curso con empleo asegurado, paga hoy»; (c) una visita a un liceo técnico con tu curso; (d) un adulto desconocido te ofrece «orientación gratis» en un chat privado. Clasifica cada una como exploración segura o señal de alerta y escribe qué harías en cada caso.", "(a) Exploración segura: voy con el curso y anoto preguntas. (b) Alerta: consulto a un adulto y verifico la institución. (c) Exploración segura: pregunto por la malla y los requisitos. (d) Alerta: no respondo, guardo capturas y aviso a un adulto.", ["clasifica las cuatro situaciones", "indica qué hacer en cada una", "reconoce las señales de alerta", "no entrega datos personales"], ["tabla escrita", "texto oral"], ["no ver la presión", "confiar sin verificar"], "Reconoce las clasificaciones y pregunta cuál señal de alerta es la más clara."),
    reinforce="Escribe tres preguntas para hacer en una feria vocacional.",
    extend="Explica por qué una decisión importante necesita tiempo.",
)

# ================================================================ OA 10
lesson(
    OA10, 1,
    "Una hoja y un lápiz. El perfil de Martina, una estudiante inventada, está escrito en los ejercicios. No necesitas contar tu propio proyecto.",
    "Aprenderé a examinar el diseño de un proyecto de vida con cinco elementos: habilidades, motivaciones, metas, posibilidades y limitaciones. Sirve para entender cómo se toman decisiones coherentes.",
    ["Conozco intereses, capacidades y condiciones (OA 01).", "Conozco caminos académicos y laborales (OA 09)."],
    [
        "Diseñar un proyecto de vida es pensar con orden hacia dónde quieres ir y cómo. Se parte de cinco elementos. Las habilidades son lo que puedes hacer o aprender. Las motivaciones son lo que te mueve a actuar, como ayudar, crear o ganar independencia. Las metas son objetivos concretos que quieres lograr. Las posibilidades son las oportunidades que tienes a tu alcance. Las limitaciones son lo que dificulta el camino, como tiempo, dinero o distancia.",
        "Una decisión coherente es la que conversa con esos elementos: por ejemplo, si te mueve ayudar y tienes habilidad para explicar, estudiar pedagogía o salud es coherente. Una decisión incoherente sería elegir algo solo porque otros lo eligieron. Un proyecto flexible se puede ajustar: cambian las posibilidades, los intereses o las limitaciones, y se corrige el rumbo.",
        "Actuar con perseverancia y esfuerzo significa seguir avanzando a pesar de las dificultades, con pasos pequeños y regulares. No es ser perfecto ni no equivocarse; es volver a intentarlo con un plan.",
    ],
    [("habilidad", "lo que una persona puede hacer o aprender"), ("motivación", "lo que mueve a una persona a actuar"), ("meta", "objetivo concreto que se quiere lograr"), ("limitación", "factor que dificulta el camino"), ("perseverancia", "seguir avanzando a pesar de las dificultades")],
    [
        W("Clasificar un dato", "Martina dice: «Quiero ser independiente y trabajar pronto». ¿Es motivación, meta o limitación?", ["Dice lo que la mueve a actuar.", "No es un objetivo concreto con plazo."], "Una motivación"),
        W("Decisión coherente", "A Martina le mueve ayudar y es buena para explicar. ¿Qué decisión es más coherente: estudiar pedagogía o elegir una carrera solo porque su amiga la elige?", ["La primera conversa con sus elementos.", "La segunda depende de otra persona."], "Estudiar pedagogía"),
    ],
    [
        M("Pensar que un proyecto de vida es una lista de deseos.", "Se olvida de las posibilidades y limitaciones.", "Incluye los cinco elementos."),
        M("Creer que perseverar es nunca cambiar de idea.", "Se confunde constancia con rigidez.", "Se persevera en el esfuerzo y se ajusta el camino."),
    ],
    R=[
        ex("Martina escribe: «Quiero aprobar 4.º medio con promedio 5,5». ¿Qué elemento del proyecto es? A) Una meta B) Una limitación", "A", "Es un objetivo concreto."),
        ex("Martina trabaja medio tiempo y le queda poco tiempo para estudiar. ¿Qué elemento es eso? A) Una limitación B) Una motivación", "A", "Dificulta el camino."),
        ex("A Martina la mueve ayudar a otras personas. ¿Qué elemento es? A) Una motivación B) Una habilidad", "A", "Es lo que la mueve a actuar."),
    ],
    U=[
        ex("¿Qué frase es una meta? A) «Terminar 4.º medio con las asignaturas aprobadas.» B) «Me gusta ayudar.»", "A", "La primera es un objetivo concreto."),
        ex("¿Qué son las posibilidades? A) Oportunidades a tu alcance B) Cosas que no existen.", "A", "Son opciones disponibles."),
        ex("¿Qué es una decisión coherente? A) La que conversa con tus habilidades y motivaciones B) La que eligen tus amigos.", "A", "Se basa en tus elementos."),
    ],
    A=[
        ex("Clasifica con H (habilidad), M (motivación), G (meta) o L (limitación): 1) puede explicar con claridad; 2) quiere ayudar a otras personas; 3) vive a una hora del centro de estudios; 4) quiere ingresar a un instituto técnico. Escribe las letras en orden.", "H, M, L, G", "Cada frase corresponde a un elemento distinto."),
        ex("Martina anota: habilidades: explicar y organizar; motivación: ayudar; meta: entrar a un instituto; posibilidades: una charla de un instituto y la ayuda de una tía; limitación: poco tiempo. ¿Cuántas posibilidades anotó?", "2", "La charla y la ayuda de su tía son las dos posibilidades."),
        ex("Martina tiene la limitación «poco tiempo por trabajar a medio tiempo». ¿Qué decisión es más coherente? A) Elegir estudios con horario vespertino B) Elegir estudios que requieren estar todo el día.", "A", "Se ajusta a su limitación."),
    ],
    Z=[
        ex("¿Por qué conviene incluir las limitaciones al diseñar un proyecto?", "Porque permite planificar cómo enfrentarlas", "Ignorarlas lleva a planes irreales."),
        ex("Un joven dice: «Si cambio de idea, fracasé». ¿Qué le responderías? A) Que ajustar un proyecto con nueva información es flexibilidad B) Que tiene razón.", "A", "Un proyecto flexible se corrige."),
    ],
    D=[
        arith("Martina quiere ahorrar $60.000 en 6 meses. ¿Cuánto debe ahorrar por mes en partes iguales?", "60000//6", "Se divide la meta por los meses.", " pesos"),
        arith("Martina estudia 45 minutos al día durante 5 días. ¿Cuántos minutos estudia en la semana?", "45*5", "Se multiplican minutos por días.", " minutos"),
    ],
    context=[ex("En una charla de orientación, una expositora dice que los proyectos pueden cambiar con el tiempo. ¿Qué es lo importante? A) Revisar y ajustar con información nueva B) No cambiar nunca.", "A", "Un proyecto flexible se adapta.")],
    selfcheck=[ex("En Orientación: ¿un proyecto de vida incluye metas y limitaciones?", "Sí", "Son dos de sus cinco elementos."), ex("¿Perseverar es nunca cambiar de idea?", "No", "Es seguir avanzando y ajustar."), ex("¿Una decisión coherente conversa con tus habilidades?", "Sí", "Se basa en tus elementos.")],
    task=T("Lee el perfil inventado de Álvaro: es bueno para el dibujo técnico y la matemática; le motiva diseñar cosas útiles; su meta es estudiar una carrera técnica en construcción; tiene un centro de formación a 40 minutos de su casa y su familia puede ayudar con el pasaje; no tiene computador propio. Escribe los cinco elementos del proyecto y una decisión coherente con ellos.", "Habilidades: dibujo técnico y matemática. Motivación: diseñar cosas útiles. Meta: estudiar la carrera técnica en construcción. Posibilidades: centro a 40 minutos y ayuda con el pasaje. Limitación: no tiene computador propio. Decisión coherente: postular a esa carrera y usar el computador de la biblioteca.", ["identifica los cinco elementos", "usa datos del perfil", "propone una decisión coherente", "no inventa datos"], ["tabla escrita", "texto oral"], ["confundir meta con motivación", "ignorar la limitación"], "Reconoce los elementos bien clasificados y pregunta cómo enfrentaría la limitación."),
    reinforce="Escribe una habilidad, una motivación y una meta de un personaje inventado.",
    extend="Explica por qué un proyecto de vida flexible no es un proyecto débil.",
)

lesson(
    OA10, 2,
    "Una hoja y un lápiz. Los ejemplos de metas están escritos en los ejercicios; son metas de personajes inventados.",
    "Aprenderé a distinguir hechos de deseos al diseñar metas y a escribir metas específicas, medibles, realistas y con plazo. Sirve para que mis metas sean claras y se puedan cumplir.",
    ["Sé identificar los cinco elementos de un proyecto de vida.", "Sé distinguir hechos y opiniones."],
    [
        "Una meta bien escrita responde cinco preguntas: ¿Qué quiero lograr? (específica), ¿cómo sabré que lo logré? (medible), ¿puedo hacerlo con mis posibilidades? (realista), ¿por qué me importa? (relevante) y ¿para cuándo? (con plazo). Por ejemplo, «aprobar Matemática este semestre con nota mínima 5,0 estudiando 3 veces por semana» es mejor que «ser bueno en Matemática».",
        "También hay que distinguir hechos de deseos. Un hecho es algo comprobable: «mi promedio actual es 5,2». Un deseo es algo que se quiere: «quiero un promedio 6,0». El deseo es el punto de partida de la meta; los hechos muestran dónde estás y qué distancia hay. Con ambos se define el plan.",
        "Las limitaciones no se esconden: se anotan y se piensa cómo enfrentarlas. Algunas se pueden modificar con esfuerzo, como organizar el tiempo; otras no por ahora, y se bordean con alternativas. Tienes derecho a revisar tus metas cuando cambian tus intereses o tus condiciones.",
    ],
    [("meta específica", "meta que dice exactamente qué se quiere lograr"), ("meta medible", "meta con un indicador para comprobar si se logró"), ("meta realista", "meta posible con los recursos y el tiempo disponibles"), ("plazo", "fecha o período para lograr la meta"), ("deseo", "algo que se quiere, aún sin plan")],
    [
        W("Mejorar una meta", "«Quiero estar bien en inglés». Reescríbela con las cinco preguntas.", ["Específica: aprobar inglés con nota mínima 5,0.", "Medible: nota en el informe.", "Plazo: este semestre.", "Realista: estudiar 3 veces por semana."], "«Aprobar inglés este semestre con nota mínima 5,0, estudiando 3 veces por semana.»"),
        W("Hecho y deseo", "«Mi promedio es 5,2» y «quiero un promedio 6,0». ¿Cuál es hecho y cuál deseo?", ["El promedio actual se puede comprobar.", "El promedio que se quiere es un deseo."], "Hecho: 5,2; deseo: 6,0"),
    ],
    [
        M("Escribir metas vagas como «ser feliz» o «salir bien».", "No se pueden medir ni planificar.", "Hazlas específicas, medibles y con plazo."),
        M("Elegir metas imposibles para sentirse motivado.", "Se confunde ambición con realismo.", "Divide en metas alcanzables y revísalas."),
    ],
    R=[
        ex("En la meta «Correr 5 km en 6 semanas», ¿qué parte es el plazo? A) «en 6 semanas» B) «5 km»", "A", "El plazo dice para cuándo."),
        ex("«Mi promedio actual es 5,2», ¿es un hecho o un deseo?", "Un hecho", "Se puede comprobar."),
        ex("En la meta «Correr 5 km en 6 semanas», ¿qué parte permite medir si se logró? A) «5 km» B) «Correr»", "A", "La cantidad es el indicador."),
    ],
    U=[
        ex("¿Cuál meta es mejor? A) «Aprobar Matemática este semestre con nota mínima 5,0.» B) «Ser bueno en Matemática.»", "A", "Es específica, medible y con plazo."),
        ex("¿Qué es un deseo? A) Algo que se quiere, aún sin plan B) Un hecho comprobado.", "A", "Es el punto de partida de la meta."),
        ex("¿Qué se hace con una limitación? A) Anotarla y pensar cómo enfrentarla B) Esconderla.", "A", "Ignorarla hace fallar el plan."),
    ],
    A=[
        ex("Clasifica con M (medible) o V (vaga): 1) «Leer 2 libros en 3 meses»; 2) «Leer mucho»; 3) «Ahorrar $30.000 en 5 meses». Escribe las letras en orden.", "M, V, M", "La 1 y la 3 tienen cantidad y plazo; la 2 no."),
        ex("Una meta dice «Subir mi promedio de 5,2 a 5,6 este semestre». ¿Cuántos décimos de nota debe subir?", "4", "5,6 menos 5,2 son 4 décimos."),
        ex("Pía quiere aprobar Física con 5,0 este semestre, pero trabaja tardes y solo puede estudiar 2 veces por semana. ¿Qué ajuste es realista? A) Estudiar 2 veces por semana con sesiones más largas B) Estudiar 7 veces por semana.", "A", "Se ajusta a su limitación de tiempo."),
    ],
    Z=[
        ex("¿Por qué una meta sin plazo es difícil de cumplir?", "Porque no hay un momento para revisarla ni exigirse", "Sin fecha, se posterga."),
        ex("Un joven dice: «Mi meta es ser famoso». ¿Qué le falta para ser una buena meta? A) Hacerla específica, medible, realista y con plazo B) Contarla a más personas para que se haga famosa.", "A", "Sin esos rasgos no se puede planificar."),
    ],
    D=[
        arith("Una meta pide leer 24 páginas por semana durante 5 semanas. ¿Cuántas páginas serán en total?", "24*5", "Se multiplican páginas por semanas."),
        arith("Para ahorrar $45.000 en 9 meses en partes iguales, ¿cuánto se debe ahorrar por mes?", "45000//9", "Se divide la meta por los meses.", " pesos"),
    ],
    context=[ex("En una charla se propone a los estudiantes escribir una meta para el semestre. ¿Cuál cumple los criterios? A) «Terminar 3 informes de Ciencias antes del 15 de junio, uno cada dos semanas.» B) «Hacerlo mejor.»", "A", "Tiene qué, cuánto y plazo.")],
    selfcheck=[ex("En Orientación: ¿una buena meta tiene plazo?", "Sí", "Indica para cuándo."), ex("¿Una meta vaga se puede medir?", "No", "No tiene indicador."), ex("¿Se anotan las limitaciones?", "Sí", "Para planificar cómo enfrentarlas.")],
    task=T("Lee estas tres metas vagas de un personaje inventado, Nicolás: (a) «Quiero ser mejor en deporte»; (b) «Quiero ahorrar»; (c) «Quiero estudiar más». Reescribe cada una con las cinco preguntas (específica, medible, realista, relevante, con plazo) y marca una limitación posible para cada una.", "(a) Correr 2 km sin parar en 8 semanas, entrenando 3 veces por semana; limitación: lluvia (entrenar en casa). (b) Ahorrar $20.000 en 4 meses; limitación: ingresos pequeños. (c) Estudiar 40 minutos de Matemática 4 días por semana este mes; limitación: horario de trabajo.", ["reescribe las tres metas", "cada una es específica, medible y con plazo", "anota una limitación", "las metas son realistas"], ["tabla escrita", "texto oral"], ["metas sin plazo", "ignorar la limitación"], "Reconoce las metas bien escritas y pregunta cómo comprobaría cada una."),
    reinforce="Convierte «quiero sacarme buenas notas» en una meta con cantidad y plazo.",
    extend="Explica por qué revisar las metas es parte de un proyecto flexible.",
)

lesson(
    OA10, 3,
    "Una hoja y un lápiz. Las alternativas de Rocío, una estudiante inventada, están escritas en los ejercicios.",
    "Aprenderé a comparar decisiones de un proyecto de vida y sus consecuencias, equilibrando metas de corto, mediano y largo plazo. Sirve para decidir con coherencia y sin perder de vista lo importante.",
    ["Sé escribir metas con las cinco preguntas.", "Sé que las decisiones tienen consecuencias."],
    [
        "Las metas pueden ser de corto plazo (en semanas o meses), de mediano plazo (en uno o dos años) y de largo plazo (en varios años). Las de corto plazo suelen ser pasos hacia las de largo plazo: aprobar el semestre ayuda a terminar el año; terminar el año ayuda a ingresar a estudios superiores. Una decisión coherente considera cómo afecta a las tres.",
        "Al decidir, a veces hay que equilibrar. Por ejemplo, trabajar a medio tiempo da dinero ahora, pero puede quitar horas de estudio; estudiar más horas puede mejorar notas, pero dejar menos tiempo libre. No hay una respuesta única: se comparan los beneficios y costos para tus metas, y se elige lo que más se acerca a lo que quieres, sin dañarte.",
        "Para decidir mejor, pregunta: ¿esta decisión me acerca a mi meta?, ¿qué estoy dejando de lado?, ¿puedo revertirla?, ¿qué pasaría en un año? Y consulta a una persona adulta de confianza. La perseverancia ayuda a mantener el rumbo cuando la decisión exige esfuerzo.",
    ],
    [("corto plazo", "lo que se logra en semanas o meses"), ("mediano plazo", "lo que se logra en uno o dos años"), ("largo plazo", "lo que se logra en varios años"), ("equilibrar", "repartir tiempo y esfuerzo entre cosas importantes"), ("revertir", "volver atrás una decisión")],
    [
        W("Relacionar plazos", "Rocío quiere ser enfermera (largo plazo). ¿Qué meta de corto plazo la acerca?", ["Aprobar Biología este semestre.", "Es un paso hacia su meta mayor."], "Aprobar Biología este semestre"),
        W("Equilibrar", "Rocío puede trabajar 10 horas semanales en una tienda o dedicar esas horas al estudio. ¿Qué considera para decidir?", ["Dinero ahora frente a tiempo de estudio.", "Cómo afecta a su meta de largo plazo.", "Si puede revertir la decisión."], "Compara beneficios y costos para sus metas"),
    ],
    [
        M("Decidir pensando solo en hoy.", "Se pierde de vista la meta de largo plazo.", "Pregunta cómo afecta a los tres plazos."),
        M("Creer que equilibrar es dividir todo en partes iguales.", "Se confunde equilibrio con igualdad.", "Equilibrar es repartir según las metas y las necesidades."),
    ],
    R=[
        ex("Entrar a una carrera dentro de cuatro años, ¿qué tipo de meta es? A) De largo plazo B) De corto plazo", "A", "Se logra en varios años."),
        ex("Terminar el año con buenas notas ayuda a ingresar a estudios superiores. ¿Qué relación hay entre ambas metas? A) La de corto plazo acerca a la de largo plazo B) Son metas que se oponen", "A", "Las metas cortas acercan a las largas."),
        ex("Rocío duda entre un trabajo de temporada de dos meses, que puede dejar, y firmar un contrato por tres años. ¿Cuál es más fácil de revertir? A) El trabajo de dos meses B) El contrato de tres años", "A", "Se puede dejar sin quedar atada."),
    ],
    U=[
        ex("¿Qué pregunta ayuda a decidir? A) ¿Esta decisión me acerca a mi meta? B) ¿Qué elige mi amigo?", "A", "Conecta la decisión con la meta."),
        ex("Trabajar a medio tiempo da dinero ahora. ¿Qué podría quitar? A) Horas de estudio B) El interés por sus metas.", "A", "El tiempo es limitado."),
        ex("¿Qué plazo corresponde a «aprobar la prueba de la próxima semana»? A) Corto plazo B) Largo plazo.", "A", "Se logra en pocos días."),
    ],
    A=[
        ex("Clasifica con C (corto plazo), M (mediano) o L (largo plazo): 1) aprobar la prueba del viernes; 2) comenzar 3.º medio dentro de un año y medio; 3) titularse de enfermera en seis años. Escribe las letras en orden.", "C, M, L", "Días o semanas, uno o dos años y varios años."),
        ex("Rocío compara dos semanas posibles. Semana X: trabajar 15 horas y estudiar 5. Semana Y: trabajar 5 horas y estudiar 15. Su meta de corto plazo es subir sus notas. ¿Cuál se acerca más a esa meta? A) La semana Y B) La semana X.", "A", "Dedica más horas al estudio."),
        arith("Rocío gana $4.000 por hora y trabaja 10 horas en la semana. ¿Cuántos pesos gana?", "4000*10", "Se multiplica el pago por hora por las horas.", " pesos"),
    ],
    Z=[
        ex("¿Por qué una decisión que parece buena hoy puede no serlo en un año?", "Porque puede alejarte de tus metas de largo plazo", "Hay que mirar más allá del presente."),
        ex("Rocío duda entre dos opciones iguales. ¿Qué conviene? A) Considerar cuál se puede revertir y consultar a un adulto B) Elegir al azar.", "A", "Reduce el riesgo."),
    ],
    D=[
        arith("Rocío quiere reunir $90.000 en 18 semanas en partes iguales. ¿Cuánto debe ahorrar por semana?", "90000//18", "Se divide la meta por las semanas.", " pesos"),
        arith("Su plan es estudiar 3 horas diarias de lunes a viernes. ¿Cuántas horas estudia en la semana?", "3*5", "Se multiplican horas por días.", " horas"),
    ],
    context=[ex("Rocío debe elegir entre un taller de ciencias gratuito los sábados y un trabajo de fin de semana. Su meta es estudiar enfermería. ¿Qué considera? A) Cómo afecta cada opción a su meta y a su tiempo de estudio B) Solo cuál paga más.", "A", "Conecta la decisión con la meta.")],
    selfcheck=[ex("En Orientación: ¿las metas de corto plazo acercan a las de largo plazo?", "Sí", "Son pasos hacia ellas."), ex("¿Equilibrar es repartir en partes iguales siempre?", "No", "Se reparte según las metas."), ex("¿Una decisión revertible es más segura?", "Sí", "Se puede corregir.")],
    task=T("Lee el caso inventado: Tomás quiere ser técnico en electricidad. Tiene dos opciones para este año: (A) un curso de electricidad básica los sábados; (B) un trabajo ayudando en una tienda los sábados, con dinero inmediato. Escribe sus metas de corto, mediano y largo plazo, compara A y B con beneficios y costos, y elige una decisión justificada.", "Corto plazo: aprobar el curso. Mediano plazo: terminar 4.º medio técnico. Largo plazo: ser técnico. A: costo tiempo, beneficio aprendizaje; B: beneficio dinero, costo tiempo de estudio. Decisión: A, porque se acerca a su meta; puede buscar trabajo más adelante.", ["escribe metas de tres plazos", "compara beneficios y costos de A y B", "elige y justifica", "considera si se puede revertir"], ["tabla escrita", "texto oral"], ["decidir solo por dinero", "olvidar el largo plazo"], "Reconoce las metas escalonadas y pregunta cómo revertiría la decisión."),
    reinforce="Escribe una meta de corto, una de mediano y una de largo plazo para un personaje inventado.",
    extend="Explica por qué equilibrar no es lo mismo que dividir en partes iguales.",
)

lesson(
    OA10, 4,
    "Una hoja y un lápiz. El plan A y el plan B de Daniela, una estudiante inventada, están escritos en los ejercicios.",
    "Aprenderé a elegir pasos seguros y flexibles para un proyecto de vida, con un plan A y un plan B, y a mantener el esfuerzo. Sirve para actuar con constancia sin quedar atrapado si algo falla.",
    ["Sé comparar decisiones por sus plazos.", "Sé escribir metas con plazo."],
    [
        "Un plan de acción flexible tiene un plan A, que es el camino principal, y un plan B, que es una alternativa si el plan A no se cumple por razones que no controlas. Ambos tienen pasos pequeños con fecha. Por ejemplo, el plan A de Daniela es estudiar enfermería en un centro técnico; el plan B es trabajar de ayudante en un centro de salud mientras ahorra y vuelve a postular.",
        "Para mantener la perseverancia se usan estrategias: dividir la meta en pasos semanales, anotar los avances, premiar el esfuerzo con algo pequeño, pedir apoyo a una persona de confianza y descansar para no agotarse. Los errores y las dificultades se tratan como información: ¿qué ocurrió?, ¿qué aprendí?, ¿qué cambio?",
        "Una acción segura incluye avisar a un adulto, no arriesgar la salud ni la seguridad por una meta, y no aceptar ofertas dudosas. Si una dificultad se vuelve demasiado grande, como mucho estrés, tristeza o presión de otros, se pide ayuda: perseverar no es aguantar solo.",
    ],
    [("plan A", "camino principal para lograr una meta"), ("plan B", "alternativa preparada por si el plan A no se cumple"), ("avance", "paso concreto logrado"), ("esfuerzo", "trabajo constante para lograr algo"), ("dificultad", "obstáculo que complica el camino")],
    [
        W("Armar plan A y B", "Daniela quiere estudiar enfermería. Plan A: postular a un centro técnico. Plan B: trabajar de ayudante, ahorrar y volver a postular. ¿Es un plan flexible?", ["Tiene un camino principal.", "Tiene una alternativa si el principal no se cumple."], "Sí, tiene plan A y plan B"),
        W("Aprender de una dificultad", "Daniela reprobó una prueba de Biología. Pregunta: ¿qué ocurrió, qué aprendí, qué cambio?", ["Notó que no repasó.", "Aprendió que necesita repasar 3 veces por semana.", "Cambia su horario."], "Registrar qué falló y ajustar el plan"),
    ],
    [
        M("Creer que perseverar es aguantar sin pedir ayuda.", "Se confunde esfuerzo con soledad.", "Pide apoyo cuando una dificultad te supera."),
        M("Armar un plan sin alternativa.", "Se piensa que un plan B resta compromiso.", "Un plan B protege el proyecto."),
    ],
    R=[
        ex("Daniela prepara una alternativa por si no logra ingresar este año. ¿Cómo se llama? A) Plan B B) Plan A", "A", "Es la alternativa por si el plan A no se cumple."),
        ex("¿Qué estrategia ayuda a perseverar? A) Dividir la meta en pasos semanales B) Dejar todo para el último día", "A", "Hace la meta más alcanzable."),
        ex("Daniela reprobó una prueba y se pregunta qué falló. ¿Cómo trata esa dificultad? A) Como información para ajustar el plan B) Como prueba de que no sirve", "A", "Muestra qué cambiar."),
    ],
    U=[
        ex("¿Qué plan es flexible? A) Uno con plan A y plan B B) Uno sin alternativa.", "A", "Tiene un camino de respaldo."),
        ex("Si el estrés es demasiado grande, ¿qué se hace? A) Pedir ayuda a una persona de confianza B) Aguantar solo.", "A", "Perseverar no es aguantar solo."),
        ex("¿Qué se pregunta frente a un error? A) ¿Qué ocurrió y qué aprendí? B) ¿A quién culpo?", "A", "Permite ajustar y mejorar."),
    ],
    A=[
        ex("El plan de Daniela tiene 4 pasos semanales durante 6 semanas. ¿Cuántos pasos son en total?", "24", "4 por 6 semanas da 24 pasos."),
        ex("Un amigo le ofrece a Daniela «un curso exprés» a cambio de un pago inmediato por transferencia y sin contrato. ¿Qué hace? A) Consultar a un adulto y verificar la institución B) Pagar de inmediato.", "A", "Hay señales de alerta."),
        ex("Daniela escribe en su calendario 5 avances en un mes y se propuso 8. ¿Cuántos avances le faltan?", "3", "8 menos 5 son 3."),
    ],
    Z=[
        ex("¿Por qué anotar los avances ayuda a perseverar?", "Porque muestra el progreso y mantiene la motivación", "Ver lo logrado anima a seguir."),
        ex("Un joven dice: «Si pido ayuda, no soy esforzado». ¿Qué falta? A) Que pedir ayuda es parte de un esfuerzo responsable B) Que el esfuerzo se mide por cuánto se aguanta sin ayuda.", "A", "El apoyo ayuda a no abandonar."),
    ],
    D=[
        arith("Daniela estudia 40 minutos al día, 5 días por semana, durante 4 semanas. ¿Cuántos minutos estudia en total?", "40*5*4", "Se multiplican minutos por días por semanas.", " minutos"),
        arith("Su meta es 30 horas de práctica en 6 semanas en partes iguales. ¿Cuántas horas por semana?", "30//6", "Se divide la meta por las semanas.", " horas"),
    ],
    context=[ex("Después de reprobar un control, un compañero dice que dejará todo. Una profesora le sugiere revisar qué falló y ajustar el plan. ¿Qué enseñanza aplica? A) Tratar el error como información B) Rendirse.", "A", "Permite mejorar el plan.")],
    selfcheck=[ex("En Orientación: ¿un plan B protege el proyecto?", "Sí", "Da una alternativa."), ex("¿Perseverar es no pedir ayuda?", "No", "Pedir ayuda es parte."), ex("En Orientación: ¿Los errores sirven para aprender?", "Sí", "Dan información útil.")],
    task=T("Lee el caso inventado: Sebastián quiere ser cocinero. Plan A: entrar a un liceo técnico de gastronomía. Plan B: trabajar como ayudante de cocina y capacitarse. Escribe un plan de cuatro semanas con un paso concreto por semana (cada uno con su evidencia), una dificultad posible y cómo la enfrentaría, y una persona de apoyo.", "Semana 1: visitar el liceo con un adulto y anotar requisitos; semana 2: reunir documentos; semana 3: practicar una receta; semana 4: postular. Dificultad: ponerse nervioso en la entrevista; ensayar con su profesor. Apoyo: el orientador.", ["escribe un paso concreto por semana durante cuatro semanas", "incluye evidencia", "anota una dificultad y cómo enfrentarla", "nombra una persona de apoyo"], ["plan escrito", "tabla"], ["plan sin evidencias", "no nombrar apoyo"], "Reconoce los pasos concretos y pregunta cómo ajustaría si falla un paso."),
    reinforce="Escribe un plan A y un plan B para una meta inventada.",
    extend="Explica por qué pedir ayuda es parte de perseverar.",
)

lesson(
    OA10, 5,
    "Una hoja y un lápiz. El esquema de presentación y los mensajes de ejemplo están escritos en los ejercicios; usa un personaje inventado.",
    "Aprenderé a presentar mi proyecto de vida a una persona adulta de confianza, a pedir orientación y a recibir críticas con apertura. Sirve para obtener apoyo y mejorar mis decisiones.",
    ["Sé armar un plan A y un plan B.", "Sé pedir ayuda con claridad."],
    [
        "Presentar tu proyecto a una persona adulta de confianza, como un familiar, un profesor o una persona orientadora, ayuda a verlo desde otra mirada. Una presentación breve tiene cuatro partes: tu meta, tus pasos, tus limitaciones y lo que necesitas. Ejemplo: «Mi meta es estudiar enfermería; mis pasos son aprobar Biología y visitar un centro; me limita el costo; necesito orientación sobre becas».",
        "Al recibir comentarios, conviene escuchar completo, preguntar para entender («¿qué te preocupa de esa idea?»), agradecer y decidir después cuáles ideas usar. Una crítica útil se enfoca en el plan y no en ti; una crítica que humilla no ayuda y puedes poner un límite: «Prefiero que me digas qué mejorar». Tú tomas la decisión final, informada con lo que escuchaste.",
        "Pedir orientación también significa elegir bien a quién preguntar: alguien que te conozca y se preocupe por ti, o que conozca el tema. Y recuerda que no se comparten datos personales con desconocidos ni se acepta ayuda de quienes piden secreto o pagos dudosos.",
    ],
    [("presentación", "exposición breve de una idea o plan"), ("retroalimentación", "comentarios que ayudan a mejorar"), ("crítica útil", "comentario que se enfoca en el plan y propone mejoras"), ("orientación", "ayuda para decidir con información"), ("límite", "lo que aceptas o no en cómo te hablan")],
    [
        W("Armar la presentación", "Pía presenta: «Mi meta es estudiar enfermería». ¿Qué le falta de las cuatro partes?", ["Tiene la meta.", "Faltan los pasos, las limitaciones y lo que necesita."], "Pasos, limitaciones y lo que necesita"),
        W("Responder a una crítica", "Le dicen: «Tu plan es poco realista». ¿Cómo responde con apertura?", ["Pregunta qué parte.", "Agradece y decide después."], "«¿Qué parte te parece poco realista? Gracias por avisarme.»"),
    ],
    [
        M("Defender el plan con enojo ante cualquier crítica.", "Se toma la crítica como ataque personal.", "Escucha, pregunta y decide después."),
        M("Aceptar toda crítica sin pensarla.", "Se cree que quien opina siempre tiene razón.", "Evalúa qué comentarios ayudan a tu meta."),
    ],
    R=[
        ex("En la presentación de tu proyecto dices: «me limita el costo». ¿Qué parte es? A) Las limitaciones B) Lo que necesito", "A", "Nombra lo que dificulta el camino."),
        ex("Un familiar te dice: «Falta agregar fechas a tus pasos». ¿Qué tipo de comentario es? A) Una crítica útil, porque se enfoca en el plan B) Un comentario que humilla", "A", "Propone una mejora concreta."),
        ex("¿A quién conviene pedir orientación? A) A alguien que te conoce y se preocupa por ti, o que conoce el tema B) A un desconocido que pide guardar secreto", "A", "Una fuente conocida y confiable protege tu decisión."),
    ],
    U=[
        ex("¿Qué frase pide orientación con claridad? A) «Necesito orientación sobre becas para mi meta.» B) «No sé, ayúdame.»", "A", "Dice qué necesita."),
        ex("¿Qué haces con una crítica útil? A) Agradecer y decidir qué usar B) Ignorarla.", "A", "Mejora el plan."),
        ex("¿Qué haces con una crítica que humilla? A) Poner un límite pidiendo comentarios sobre el plan B) Aceptarla sin decir nada.", "A", "Protege tu dignidad."),
    ],
    A=[
        ex("Clasifica con U (útil) o H (humilla): 1) «Podrías agregar un plan B»; 2) «Eres un fracaso»; 3) «Falta una fecha en el paso 2». Escribe las letras en orden.", "U, H, U", "La 1 y la 3 proponen mejoras."),
        ex("Un perfil desconocido en redes ofrece «orientación gratis» y pide tu dirección. ¿Qué haces? A) No compartir datos y avisar a un adulto B) Dar la dirección.", "A", "No se dan datos a desconocidos."),
        arith("Daniela presenta su plan y recibe 3 comentarios de cada una de las 4 personas que la escuchan. ¿Cuántos comentarios recibe?", "3*4", "Se multiplican comentarios por personas."),
    ],
    Z=[
        ex("¿Por qué conviene mostrar el plan a un adulto de confianza?", "Porque aporta otra mirada y puede ayudar a mejorarlo", "Otra persona ve lo que tú no ves."),
        ex("Tú tomas la decisión final. ¿Qué ventaja tiene escuchar antes? A) Decidir con más información B) Cambiar de idea sin razón.", "A", "Escuchar informa la decisión."),
    ],
    D=[
        arith("Una persona orientadora atiende 6 presentaciones de 15 minutos. ¿Cuántos minutos son?", "6*15", "Se multiplican presentaciones por minutos.", " minutos"),
        arith("De 36 estudiantes, 28 presentan su plan en clase y el resto lo hace por escrito. ¿Cuántos lo hacen por escrito?", "36-28", "Al total se le restan los que presentan en clase."),
    ],
    context=[ex("Un profesor le dice a Martín: «Falta que agregues fechas a los pasos». ¿Cómo responde con apertura? A) «Gracias, las agrego esta semana.» B) «Tú no sabes nada.»", "A", "Aprovecha la crítica útil.")],
    selfcheck=[ex("En Orientación: ¿presentar el plan ayuda a mejorarlo?", "Sí", "Aporta otra mirada."), ex("¿Se comparten datos personales con desconocidos?", "No", "Es un riesgo."), ex("¿La decisión final es tuya, informada por lo que escuchaste?", "Sí", "Tú decides con información.")],
    task=T("Prepara la presentación de un proyecto de vida de un personaje inventado, Camilo, que quiere ser diseñador gráfico. Escribe las cuatro partes (meta, pasos, limitaciones, lo que necesita) en cuatro líneas; luego escribe cómo responderías a una crítica útil y a un comentario que humilla.", "Meta: estudiar diseño gráfico. Pasos: aprobar Artes, hacer un portafolio de 5 diseños. Limitaciones: no tiene computador propio. Necesita: orientación sobre becas. Crítica útil: «Gracias, agrego fechas». Comentario que humilla: «Prefiero comentarios sobre el plan».", ["escribe las cuatro partes", "responde a una crítica útil", "pone un límite a la crítica que humilla", "no entrega datos personales reales"], ["texto escrito", "presentación oral"], ["presentación sin pedido", "aceptar una humillación"], "Reconoce las partes presentes y pregunta qué ajuste haría tras la crítica."),
    reinforce="Escribe una frase para pedir orientación sobre becas.",
    extend="Explica por qué una crítica útil se enfoca en el plan y no en la persona.",
)

lesson(
    OA10, 6,
    "Una hoja y un lápiz. Los casos de Ema y de Bruno, personas inventadas, y la lista de revisión están escritos en los ejercicios; no se pide contar tu proyecto.",
    "Aprenderé a aplicar todo lo aprendido a un caso nuevo y a revisar un proyecto con una lista de control. Sirve para diseñar mi proyecto de vida de forma coherente, flexible y responsable.",
    ["Sé armar metas y planes con plan B.", "Sé presentar un proyecto y recibir críticas."],
    [
        "Para transferir, usa una lista de revisión de seis preguntas: 1) ¿Están claros mis habilidades, mis motivaciones y mis metas? 2) ¿Anoté mis posibilidades y mis limitaciones? 3) ¿La meta es específica, medible, realista y con plazo? 4) ¿Tengo pasos pequeños y un plan B? 5) ¿Pedí orientación a una persona adulta de confianza? 6) ¿Cuándo voy a revisarlo? Si todas son sí, el proyecto está bien diseñado.",
        "Un proyecto de vida no es una promesa definitiva. Se revisa cada cierto tiempo, por ejemplo cada tres meses o al terminar el año, y se ajusta con lo aprendido. Los cambios no son fracasos: son parte de crecer. Lo importante es que las decisiones sean coherentes con tus elementos y se tomen con responsabilidad hacia ti y hacia otras personas.",
        "Aplicarlo a un caso ficticio permite practicar sin exponer tu vida personal. Al analizar el proyecto de otra persona, ten cuidado de no juzgar ni de presionar, y recuerda que cada proyecto tiene su contexto. Si algo del caso muestra riesgo para la persona, la recomendación siempre es avisar a una persona adulta de confianza.",
    ],
    [("lista de revisión", "conjunto de preguntas para comprobar un trabajo"), ("coherente", "que conversa con los elementos del proyecto"), ("responsable", "que considera las consecuencias para uno y para otros"), ("ajustar", "cambiar parte de un plan con nueva información"), ("contexto", "circunstancias que rodean a una persona o decisión")],
    [
        W("Usar la lista", "El plan de Ema dice: «Quiero ser la mejor del mundo». ¿Qué pregunta de la lista falla?", ["No es específica ni medible.", "No tiene plazo."], "La pregunta 3"),
        W("Revisar con el tiempo", "Bruno cambió de interés en 2.º medio. ¿Qué hace con su proyecto?", ["Revisa sus elementos.", "Ajusta metas y pasos."], "Revisa y ajusta"),
    ],
    [
        M("Creer que el proyecto de vida se hace una vez y no se toca.", "Se piensa que cambiar es fallar.", "Revísalo cada cierto tiempo."),
        M("Juzgar los proyectos de otros sin conocer su contexto.", "Se compara con el propio.", "Cada proyecto tiene su contexto; apoya sin presionar."),
    ],
    R=[
        ex("En la lista de seis preguntas, ¿cuál revisa si pediste orientación a un adulto de confianza? A) La 5 B) La 3", "A", "La pregunta 5 trata de la orientación."),
        ex("Un estudiante revisa su proyecto cada tres meses y cambia un paso porque surgió una nueva posibilidad. ¿Cómo se entiende? A) Como flexibilidad B) Como fracaso", "A", "Cambian los datos y los intereses."),
        ex("Ema responde «no» a la pregunta 3 de la lista. ¿Qué debe mejorar? A) Que la meta sea específica, medible, realista y con plazo B) Que tenga un plan B", "A", "La pregunta 3 revisa cómo está escrita la meta."),
    ],
    U=[
        ex("¿Qué pregunta de la lista revisa si hay un plan B? A) La 4 B) La 6.", "A", "Habla de pasos pequeños y plan B."),
        ex("¿Qué debe hacerse ante una señal de riesgo en el caso de otra persona? A) Recomendar avisar a una persona adulta de confianza B) Guardar el secreto.", "A", "Es el protocolo seguro."),
        ex("¿Qué hace coherente a una decisión? A) Que conversa con las habilidades, motivaciones y metas B) Que otros la aprueben.", "A", "Parte de los elementos propios."),
    ],
    A=[
        ex("Ema responde a la lista: 1 sí, 2 sí, 3 no, 4 sí, 5 no, 6 sí. ¿Cuántas preguntas quedaron en no?", "2", "La 3 y la 5."),
        ex("Bruno revisa su proyecto cada 3 meses. ¿Cuántas revisiones hace en 1 año?", "4", "12 meses dividido en 3 da 4 revisiones."),
        ex("Un compañero comenta que Ema nunca cumplirá su plan sin conocerla. ¿Qué error comete? A) Juzgar sin conocer su contexto B) Dar un dato comprobado.", "A", "No tiene datos."),
    ],
    Z=[
        ex("¿Por qué conviene revisar el proyecto de vida cada cierto tiempo?", "Porque los intereses y las posibilidades cambian", "Un plan fijo puede dejar de servir."),
        ex("En el caso de Bruno aparece que está muy decaído por semanas. ¿Qué recomiendas? A) Avisar a una persona adulta de confianza B) Que lo resuelva solo.", "A", "Es una señal para pedir ayuda."),
    ],
    D=[
        arith("Un curso de 40 estudiantes revisa proyectos en parejas. ¿Cuántas parejas hay?", "40//2", "Se divide el total entre 2."),
        arith("Una lista de revisión tiene 6 preguntas y un estudiante inventado respondió sí a 4. ¿Cuántas quedan por mejorar?", "6-4", "Al total se le restan las respuestas en sí."),
    ],
    context=[ex("Al final del año, un curso hace una ronda en que cada estudiante revisa un caso inventado con la lista de seis preguntas. ¿Qué ventaja tiene? A) Practica sin exponer su vida personal B) Revela secretos de otros.", "A", "Usa casos ficticios.")],
    selfcheck=[ex("En Orientación: ¿la lista de revisión tiene seis preguntas?", "Sí", "Son las de esta clase."), ex("¿Se puede juzgar un proyecto ajeno sin conocer su contexto?", "No", "Hay que respetar sus circunstancias."), ex("¿Se revisa el proyecto de vida cada cierto tiempo?", "Sí", "Se ajusta con lo aprendido.")],
    task=T("Lee el caso inventado: Ema, de 15 años, quiere estudiar psicología. Es buena para escuchar y escribir; le motiva ayudar a otras personas; su meta es entrar a la universidad; tiene un colegio con orientadora y una tía que le puede ayudar con costos; le preocupa el puntaje y el dinero. Usa la lista de seis preguntas para revisar su proyecto: responde sí o no con un dato y escribe dos mejoras y a quién pediría orientación.", "1 sí (habilidades, motivación, meta). 2 sí (posibilidades: orientadora y tía; limitaciones: puntaje y dinero). 3 no (falta plazo y medición). 4 no (falta plan B). 5 no (tiene orientadora, pero el caso no dice que haya pedido ayuda). 6 no (falta fecha de revisión). Mejoras: escribir la meta con plazo y agregar un plan B. Orientación: la persona orientadora.", ["responde las seis preguntas con datos", "propone dos mejoras", "nombra a quién pedir orientación", "no juzga a Ema"], ["lista escrita", "texto oral"], ["responder sin dato", "juzgar a la persona"], "Reconoce las respuestas con dato y pregunta cuál mejora haría primero."),
    reinforce="Escribe las seis preguntas de la lista de revisión con tus palabras.",
    extend="Explica por qué revisar un proyecto no significa abandonarlo.",
)
