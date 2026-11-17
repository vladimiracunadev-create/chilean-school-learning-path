"""Artes visuales, audiovisuales y multimediales 3.º y 4.º medio HC: OAC-07 (relacionar la asignatura con contextos laborales, profesionales y de desarrollo personal). Personas, fuentes y casos inventados; sin datos reales de empleo."""
from __future__ import annotations

from hc_avam_common import build

O7 = "AR-AVAM-3y4-OAC-07"

# ============================================================ OAC-07, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). Un curso ficticio crea un cartel y un video corto de 30 segundos para invitar a una feria del libro. "
     "Tareas realizadas: observar carteles y videos anteriores y anotar sus decisiones; bocetar tres ideas; elegir una con criterios; hacer pruebas de color; planificar el trabajo en 4 semanas; recibir y usar comentarios; atribuir las fuentes; presentar el resultado a las familias. "
     "Habilidades de la asignatura que se trabajaron: observación y análisis, composición, comunicación visual, planificación de proyectos, trabajo con críticas, respeto de derechos de autor, presentación de resultados.")
build(
    O7, 1, F,
    use="Aprenderé a reconocer las habilidades y conocimientos que desarrolla la asignatura y a relacionarlos con situaciones de estudio, trabajo y vida personal.",
    prior=["Sé analizar una obra y crear un proyecto.", "Sé evaluar con criterios.", "Sé presentar resultados."],
    explain=[
        "En esta asignatura se desarrollan habilidades que sirven más allá del arte. Observar y analizar permite entender cómo se comunican las imágenes. Componer y decidir con criterios sirve para resolver problemas de diseño. Planificar un proyecto con tiempos y recursos sirve para organizar cualquier trabajo. Recibir críticas y mejorar enseña a aprender de la retroalimentación. Respetar derechos de autor y pedir consentimiento forma parte del trabajo ético con imágenes.",
        "Estas habilidades se relacionan con distintos contextos. En estudios y trabajos pueden aparecer en el diseño gráfico, la ilustración, la fotografía, la producción audiovisual, la animación, el desarrollo de contenidos digitales, la mediación en museos o el montaje de exposiciones. En el desarrollo personal se relacionan con la expresión de ideas y emociones, la participación cultural y el disfrute del arte como actividad propia.",
        "Relacionar una habilidad con un contexto significa explicar con un ejemplo cómo se usa. Por ejemplo, planificar un proyecto con tiempos sirve a quien organiza una exposición porque debe cumplir una fecha. No es necesario dedicarse al arte para usar lo aprendido: muchas profesiones usan comunicación visual y trabajo en equipo.",
    ],
    vocab=[("habilidad", "capacidad que se desarrolla con práctica"), ("conocimiento", "saber que se aprende y se aplica"), ("contexto laboral", "situación de trabajo donde se usa una habilidad"), ("comunicación visual", "transmitir ideas con imágenes"), ("mediación cultural", "acercar al público a obras y proyectos"), ("desarrollo personal", "crecimiento de una persona en sus intereses y capacidades")],
    worked=[
        ("Relacionar habilidad y tarea", "¿Con qué habilidad se relaciona «elegir una idea con criterios»?", ["Elegir con criterios es tomar decisiones fundamentadas.", "Se relaciona con composición y decisión visual, y con la habilidad de resolver problemas."], "Decisión fundamentada y resolución de problemas"),
        ("Relacionar con un contexto", "¿Cómo sirve la planificación en 4 semanas a quien monta una exposición?", ["Una exposición tiene una fecha de apertura.", "Planificar por semanas permite cumplir la fecha."], "Permite cumplir la fecha de apertura")
    ],
    mistakes=[("Pensar que las habilidades del arte solo sirven si uno será artista.", "Planificar, comunicar y recibir críticas se usan en muchos trabajos y estudios.", "Relaciona cada habilidad con varios contextos."),
              ("Decir «sirve para todo» sin ejemplo.", "No se sabe cómo ni para qué.", "Explica con un ejemplo concreto de uso.")],
    T=[
        ('abc', '¿Qué significa relacionar una habilidad con un contexto?', 'Explicar con un ejemplo cómo se usa en esa situación', 'Decir que sirve para todo', 'Listar nombres de profesiones', 'Relacionar es mostrar cómo se aplica con un ejemplo.'),
        ('abc', '{F} ¿Qué habilidad trabaja «anotar las decisiones de carteles anteriores»?', 'Observación y análisis', 'Planificación de tiempos', 'Presentación a las familias', 'Anotar decisiones requiere observar y analizar.'),
        ('abc', '{F} ¿Qué habilidad trabaja «planificar el trabajo en 4 semanas»?', 'Planificación de proyectos', 'Composición', 'Atribución de fuentes', 'La planificación organiza tiempos y recursos.'),
        ('abc', '{F} ¿Qué habilidad trabaja «presentar el resultado a las familias»?', 'Presentación de resultados', 'Observación', 'Planificación', 'La presentación comunica el proyecto a un público.'),
        ('abc', '{F} ¿Qué habilidad trabaja «atribuir las fuentes»?', 'Respeto de derechos de autor', 'Hacer pruebas de color', 'Bocetar', 'Atribuir es reconocer la autoría de otras personas.'),
        ('=', '{F} La ficha menciona 7 habilidades. Si el curso ya comentó 3 de ellas, ¿cuántas faltan por comentar?', '7-3', 'Se restan las comentadas al total de la ficha.', ' habilidades'),
        ('abc', 'Una persona que organiza una exposición debe cumplir la fecha de apertura. ¿Qué habilidad le sirve?', 'Planificación de proyectos', 'Dibujar rápido', 'Memorizar fechas', 'La planificación permite cumplir plazos y fechas de entrega.'),
        ('abc', 'Alguien dice: «no seré artista, entonces no me sirve lo que aprendo aquí». ¿Qué respondes?', 'Que habilidades como comunicar con imágenes, planificar y recibir críticas se usan en muchos estudios y trabajos', 'Tiene razón', 'Que debe ser artista para usarlas', 'Las habilidades se aplican a distintos contextos.'),
        ('abc', '¿Cuál es un ejemplo de contexto laboral donde se usa la composición?', 'El diseño de un afiche para un cliente', 'La preparación de una tabla de multiplicar', 'La limpieza de una sala', 'El diseño gráfico usa composición para ordenar la información.'),
        ('=', 'Un equipo ficticio tiene 4 personas y cada una dedica 6 horas a la semana a un proyecto de 3 semanas. ¿Cuántas horas suman en total?', '4*6*3', 'Se multiplican personas, horas por semana y semanas.', ' horas'),
        ('abc', '¿Qué tiene que ver el desarrollo personal con la asignatura?', 'Expresar ideas y emociones, participar de la cultura y disfrutar del arte', 'Solo ganar dinero', 'Solo sacar buenas notas', 'La asignatura aporta al crecimiento más allá del trabajo.'),
        ('abc', 'Recibir y usar críticas es una habilidad útil porque', 'permite mejorar un trabajo con la mirada de otras personas', 'asegura que nunca habrá errores', 'obliga a aceptar todo comentario', 'Saber usar la crítica ayuda a mejorar en cualquier contexto.'),
        ('abc', 'Un estudiante dice que la mediación cultural es «solo guiar un recorrido». ¿Qué matiz agregas?', 'Es acercar obras y proyectos al público con lenguaje claro, adaptándose a cada grupo', 'Es vender entradas', 'Es limpiar las salas', 'La mediación cultural comunica y acerca el arte al público.'),
    ],
    ctx=('abc', 'Una estudiante quiere explicar a su familia qué le sirve de la asignatura. Escribe: «Aprendí a planificar un proyecto en 4 semanas, y eso me sirve para organizar mi trabajo de ciencias». ¿Qué tiene de bueno?', 'Relaciona una habilidad con otro contexto mediante un ejemplo concreto', 'Dice que todo sirve para todo', 'No explica nada', 'Muestra un uso concreto de la habilidad en otro contexto.'),
    sc=[
        ("En Artes: ¿qué es la comunicación visual?", "Transmitir ideas con imágenes", "Se usa en diseño, audiovisual y muchos otros campos."),
        ("¿Para qué sirve planificar un proyecto?", "Para cumplir plazos organizando tiempos y recursos", "Se usa en cualquier trabajo que tenga plazos."),
        ("¿Hay que ser artista para usar estas habilidades?", "No", "Se aplican en muchos estudios y trabajos."),
    ],
    op=("Elige tres habilidades de la asignatura y para cada una escribe un contexto (de estudio, trabajo o vida personal) y un ejemplo concreto de uso. No inventes sueldos ni cifras.",
        "Habilidad 1: planificación; contexto: un trabajo escolar de historia; ejemplo: repartir las tareas en 3 semanas. Habilidad 2: comunicación visual; contexto: un afiche para un club; ejemplo: usar un título grande. Habilidad 3: recibir críticas; contexto: un equipo deportivo; ejemplo: ajustar jugadas tras comentarios.",
        ["relaciona habilidad y contexto", "ejemplos concretos", "sin cifras inventadas"],
        ["hoja con tres relaciones"],
        ["decir «sirve para todo»", "inventar datos de empleo"],
        "Pregunta: «¿cómo se usa esa habilidad ahí?». Si no hay ejemplo, pídele uno."),
    reinforce="Escribe una habilidad que usaste esta semana en cualquier tarea y cómo la usaste.",
    extend="Explica cómo la habilidad de comunicar con imágenes ayudaría a una persona que trabaja en salud o en educación.",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 2 (perfiles inventados, sin datos reales de empleo). "
     "Camila (ficticia), diseñadora gráfica independiente: trabaja por proyectos para clientes distintos, presenta propuestas, recibe correcciones y entrega archivos para imprimir o publicar. "
     "Diego (ficticio), técnico de montaje en un centro cultural: coordina con el equipo la ubicación de las obras, revisa la seguridad y cuida las fechas de apertura. "
     "Sofía (ficticia), realizadora audiovisual en un equipo: trabaja con guion, storyboard, grabación y edición, y revisa cada etapa con el equipo. "
     "Nota: los perfiles son ejemplos para practicar; no describen sueldos, instituciones ni ofertas reales.")
build(
    O7, 2, F,
    use="Aprenderé a relacionar los conocimientos de la asignatura con contextos laborales y profesionales reales y diversos, y a describir qué hace cada rol sin inventar datos.",
    prior=["Sé qué habilidades desarrolla la asignatura.", "Sé planificar un proyecto.", "Sé comunicar con imágenes."],
    explain=[
        "Los conocimientos de artes visuales, audiovisuales y multimediales se usan en roles muy variados. Un diseñador gráfico diseña piezas para comunicar (afiches, logotipos, sitios). Un ilustrador crea imágenes para libros o campañas. Un fotógrafo registra o interpreta una realidad. Un realizador audiovisual desarrolla relatos con imagen y sonido. Un animador crea movimiento. Un técnico de montaje o un mediador cultural trabajan en exposiciones. Muchos de estos trabajos se hacen por proyectos y en equipo.",
        "Para describir un rol se responden cuatro preguntas: qué produce (el resultado), con quién trabaja (clientes, equipo, público), qué herramientas usa (tradicionales o digitales) y qué conocimientos necesita. Las rutas de formación son diversas: educación técnica, universitaria, cursos, aprendizaje práctico. No hay una única ruta correcta, y las oportunidades dependen del lugar y del momento.",
        "En este cuaderno los perfiles son ficticios y no se entregan sueldos ni cifras. Para conocer roles reales se investiga con fuentes confiables y se conversa con personas del oficio, con permiso y con respeto, como se verá en la próxima clase.",
    ],
    vocab=[("diseño gráfico", "creación de piezas visuales para comunicar"), ("realización audiovisual", "creación de relatos con imagen y sonido"), ("montaje de exposiciones", "ubicación y cuidado de obras en un espacio"), ("trabajo por proyectos", "trabajo organizado en encargos con inicio y fin"), ("ruta de formación", "camino de estudios o aprendizaje para un oficio")],
    worked=[
        ("Describir un rol", "Describe el rol de Diego con las cuatro preguntas.", ["Produce: una exposición montada y segura. Trabaja con: el equipo del centro cultural.", "Usa: planos y fijaciones; necesita: planificación y atención a la seguridad."], "Monta exposiciones seguras con el equipo del centro cultural"),
        ("Asociar conocimientos", "¿Qué conocimiento de la asignatura usa Sofía al hacer un storyboard?", ["Un storyboard planifica los planos en secuencia.", "Usa conocimientos de lenguaje audiovisual: planos y montaje."], "Lenguaje audiovisual: planos y montaje")
    ],
    mistakes=[("Suponer que cada persona de estas áreas gana mucho o poco sin tener datos.", "Sin fuentes confiables, es un dato inventado.", "No afirmes cifras; investiga con fuentes."),
              ("Creer que hay una sola ruta para dedicarse a estas áreas.", "Existen rutas técnicas, universitarias y prácticas, entre otras.", "Revisa varias rutas y sus requisitos con fuentes confiables.")],
    T=[
        ('abc', '{F} ¿Qué produce Camila?', 'Piezas gráficas para clientes, como archivos para imprimir o publicar', 'Exposiciones de museo', 'Películas largas', 'La ficha indica que Camila entrega archivos para imprimir o publicar.'),
        ('abc', '{F} ¿Qué hace Camila antes de entregar los archivos finales?', 'Presenta propuestas y recibe correcciones del cliente', 'Graba y edita el video del cliente', 'Monta las obras en una sala', 'La ficha dice que Camila presenta propuestas y recibe correcciones.'),
        ('abc', '{F} ¿Qué etapas trabaja Sofía?', 'Guion, storyboard, grabación y edición', 'Solo dibujo a lápiz', 'Solo atención de público', 'La ficha lista guion, storyboard, grabación y edición.'),
        ('abc', '{F} ¿Qué tienen en común los tres perfiles?', 'Trabajan por proyectos y revisan con otras personas', 'Todos trabajan solos', 'Todos hacen el mismo oficio', 'Los tres revisan con clientes o equipos.'),
        ('=', '{F} Sofía revisa 4 etapas con su equipo y cada revisión dura 45 minutos. ¿Cuántos minutos de revisión suma?', '4*45', 'Se multiplica cada revisión por la cantidad de etapas.', ' minutos'),
        ('abc', '¿Qué es el trabajo por proyectos?', 'Trabajar en encargos con un inicio, un fin y un resultado', 'Trabajar siempre sin fecha', 'Trabajar solo los fines de semana', 'Un proyecto tiene inicio, fin y resultado.'),
        ('abc', 'Una compañera dice que Camila gana mucho porque es diseñadora. ¿Qué respondes?', 'Que no hay datos en la ficha ni se pueden afirmar cifras sin fuentes', 'Que tiene razón', 'Que seguro gana poco', 'No se afirman cifras sin fuentes.'),
        ('abc', '¿Cuál es una ruta de formación posible para un rol de este campo?', 'Hay varias: técnica, universitaria, cursos o aprendizaje práctico, según el caso', 'Solo una universidad específica', 'Ninguna, es innato', 'Existen varias rutas, y cada una tiene requisitos.'),
        ('abc', '{F} Además de revisar la seguridad, ¿qué cuida Diego?', 'Las fechas de apertura', 'El guion de los videos', 'Los archivos para imprimir', 'La ficha indica que Diego cuida las fechas de apertura.'),
        ('=', 'Un equipo ficticio tiene 3 diseñadores y 2 realizadores. ¿Cuántas personas tiene el equipo?', '3+2', 'Se suman los integrantes de ambos roles.', ' personas'),
        ('abc', 'Un grupo quiere hablar con un montajista real. ¿Qué paso es adecuado?', 'Pedir permiso al liceo y coordinar con una persona adulta, con respeto y claridad', 'Escribirle a su perfil privado sin avisar', 'Dar datos personales del curso', 'Se coordina con una persona adulta del liceo.'),
        ('abc', '¿Qué conocimiento de la asignatura puede usar un mediador cultural?', 'Análisis de obras para explicarlas con claridad a un público', 'Solo cálculo de costos', 'Solo programación', 'La mediación se apoya en el análisis y la comunicación.'),
        ('abc', '{F} Los perfiles de la ficha, ¿describen empleos reales?', 'No, son ejemplos para practicar', 'Sí, son ofertas actuales', 'Sí, de instituciones conocidas', 'La nota de la ficha aclara que no describen ofertas reales.'),
    ],
    ctx=('abc', 'Un estudiante quiere relacionar la asignatura con su interés en videojuegos. ¿Qué plan es coherente?', 'Investigar con fuentes confiables qué roles existen y qué conocimientos de la asignatura usan, como lenguaje audiovisual, composición y trabajo en equipo', 'Afirmar cuánto ganan sin consultar', 'Dejar la asignatura', 'Investigar con fuentes permite relacionar de manera fundada.'),
    sc=[
        ("En Artes: ¿qué es un montaje de exposiciones?", "La ubicación y el cuidado de obras en un espacio", "Requiere planificación cuidadosa y atención a la seguridad."),
        ("¿Se afirman cifras de sueldos sin fuentes?", "No", "Sería un dato inventado sin fuente que lo respalde."),
        ("¿Hay una sola ruta de formación?", "No, existen varias", "Cada ruta tiene requisitos y tiempos distintos."),
    ],
    op=("Elige un rol de este campo (que no sea de la ficha), y escribe cuatro frases: qué produce, con quién trabaja, qué herramientas usa y qué conocimientos de la asignatura le sirven. Indica qué dato necesitarías investigar para completarlo.",
        "Rol: ilustradora de libros infantiles. Produce: imágenes para cuentos. Trabaja con: editores y escritores. Usa: dibujo y herramientas digitales. Le sirven: composición, comunicación visual y recibir críticas. Debo investigar: rutas de formación posibles con fuentes confiables.",
        ["responde las cuatro preguntas", "relaciona conocimientos", "no inventa cifras"],
        ["hoja con el perfil y un dato por investigar"],
        ["inventar sueldos", "una sola ruta como única"],
        "Pregunta: «¿cómo sabes eso?». Si no tiene fuente, pídele que lo marque como pendiente."),
    reinforce="Pregunta a una persona de tu casa qué oficio le llama la atención del mundo visual y escribe qué conocimientos pensarías que usa.",
    extend="Explica por qué dos personas con el mismo oficio pueden haber seguido rutas de formación muy distintas.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 3 (fuentes y entrevista de ejemplo, inventadas). Un grupo investiga el trabajo de un diseñador gráfico. "
     "Fuente 1: página de una escuela de diseño (ficticia) con malla de estudios, nombre de la institución y fecha de actualización reciente. "
     "Fuente 2: video de una persona que dice que «todos los diseñadores ganan muchísimo» sin dar ninguna fuente. "
     "Fuente 3: entrevista breve a un diseñador (ficticio), con su autorización para ser citado, hecha en el liceo con una persona adulta presente. "
     "Criterios para evaluar una fuente: autor identificable, fecha, propósito, evidencia y posibilidad de contrastar con otra fuente. "
     "Preguntas preparadas para la entrevista: 1) ¿Qué hace en un día de trabajo? 2) ¿Qué herramientas usa? 3) ¿Cómo aprendió su oficio? 4) ¿Qué consejo da a quien comienza? 5) ¿Qué parte de su trabajo es más difícil?")
build(
    O7, 3, F,
    use="Aprenderé a investigar contextos laborales y de desarrollo personal con fuentes confiables, a evaluar fuentes y a preparar una entrevista respetuosa.",
    prior=["Sé relacionar habilidades y roles.", "Sé distinguir datos de opiniones.", "Sé pedir permiso antes de usar el trabajo o la imagen de otra persona."],
    explain=[
        "Investigar es buscar información de manera ordenada para responder una pregunta. Para saber si una fuente es confiable se revisan cinco aspectos: autor identificable, fecha, propósito (informar, vender, convencer), evidencia (datos o ejemplos verificables) y posibilidad de contrastar con otra fuente independiente. Una afirmación importante, como una cifra de ingresos, se acepta cuando dos fuentes confiables coinciden.",
        "Una entrevista es una conversación preparada con una persona que conoce un oficio. Se prepara con preguntas abiertas que no se responden con sí o no, se pide el permiso de la persona para registrar y citar sus palabras, y se agradece. Las entrevistas con personas externas se coordinan con el liceo y se hacen con una persona adulta presente o con autorización; no se comparten datos personales como teléfonos o direcciones.",
        "Al terminar, se registra la información con su fuente (quién, dónde y cuándo) y se distingue lo que dice la fuente de lo que concluye el grupo. Si las fuentes se contradicen, se declara la diferencia y no se elige la que gusta más.",
    ],
    vocab=[("fuente confiable", "fuente con autor, fecha, propósito y evidencia"), ("contrastar", "comparar con otra fuente independiente"), ("propósito de la fuente", "para qué fue hecha: informar, vender o convencer"), ("entrevista", "conversación preparada con una persona experta"), ("autorización", "permiso para citar o registrar")],
    worked=[
        ("Evaluar una fuente", "¿Por qué la fuente 2 no es confiable?", ["Dice una cifra («muchísimo») sin dar ninguna fuente.", "No hay evidencia ni forma de contrastarla."], "No tiene evidencia ni se puede contrastar"),
        ("Formular una pregunta abierta", "¿Es abierta la pregunta «¿Le gusta su trabajo?»?", ["Se responde con sí o no.", "No es abierta; una pregunta abierta sería «¿Qué es lo que más le gusta de su trabajo?»"], "No es abierta")
    ],
    mistakes=[("Aceptar una cifra porque suena convincente.", "Puede ser falsa o no aplicar a todos los casos.", "Contrasta con otra fuente confiable o no la uses."),
              ("Publicar fotos o datos personales de la persona entrevistada sin su permiso.", "Se vulnera su privacidad.", "Pide autorización por escrito y evita datos personales.")],
    T=[
        ('abc', '¿Qué significa contrastar una fuente?', 'Compararla con otra fuente independiente', 'Copiar lo que dice', 'Guardarla sin leer', 'Contrastar es comparar con otra fuente independiente.'),
        ('abc', '{F} ¿Qué aspecto de la fuente 1 la hace más confiable?', 'Tiene institución identificable y fecha de actualización reciente', 'Que use un diseño llamativo', 'Que sea muy larga', 'La institución y la fecha permiten revisar su origen y vigencia.'),
        ('abc', '{F} ¿Qué problema tiene la fuente 2?', 'No da fuentes y afirma una cifra vaga', 'Está en video', 'Es muy corta', 'No hay evidencia ni forma de contrastar.'),
        ('abc', '{F} ¿Qué cuidado se tuvo en la fuente 3?', 'Contó con la autorización y una persona adulta presente', 'Se hizo a escondidas', 'Se publicó el teléfono del entrevistado', 'La ficha dice que se hizo con autorización y un adulto presente.'),
        ('abc', '{F} ¿Cuál de estas preguntas es abierta?', '¿Qué hace en un día de trabajo?', '¿Trabaja los fines de semana?', '¿Es difícil su oficio?', 'La primera no se responde con sí o no.'),
        ('=', '{F} El grupo prepara 5 preguntas y la persona entrevistada responde cada una en 3 minutos. ¿Cuántos minutos dura la entrevista?', '5*3', 'Se multiplica la cantidad de preguntas por el tiempo de respuesta.', ' minutos'),
        ('abc', '{F} El grupo tiene dos fuentes que coinciden sobre la formación y una que se contradice sin evidencia. ¿Qué hace?', 'Usa las dos que coinciden, declara la diferencia y no usa la contradictoria sin evidencia', 'Usa la que más le gusta', 'Elimina todo y no informa', 'Se prefieren fuentes que coinciden y se declara la diferencia.'),
        ('abc', '{F} Un integrante quiere publicar en redes la foto del entrevistado. ¿Qué corresponde?', 'Pedirle autorización y consultar al docente antes de publicar', 'Publicarla porque se grabó en el liceo', 'Publicarla sin nombre', 'La imagen de una persona requiere su autorización.'),
        ('=', 'De 4 fuentes revisadas, 3 cumplen los 5 criterios. ¿Cuántas fuentes no los cumplen?', '4-3', 'Se restan las que cumplen al total.', ' fuente'),
        ('abc', 'Al registrar una fuente, ¿qué datos se anotan?', 'Quién la escribió, dónde se publicó y cuándo', 'Solo el título', 'Solo la opinión del grupo', 'Quién, dónde y cuándo permiten verificarla.'),
        ('abc', 'Un entrevistado dice algo que el grupo no comparte. ¿Qué hace?', 'Cita sus palabras tal cual y agrega la opinión del grupo aparte', 'Cambia sus palabras', 'No lo cita', 'Se distingue lo que dice la fuente de lo que concluye el grupo.'),
        ('abc', 'Un desconocido por mensajes ofrece una «entrevista exclusiva» y pide la dirección del liceo. ¿Qué haces?', 'No das datos y avisas a una persona adulta del liceo', 'Le das la dirección', 'Le envías fotos del curso', 'Ante una oferta desconocida se protegen los datos y se avisa a un adulto.'),
        ('abc', 'Para investigar un rol laboral, ¿qué combinación de fuentes es la más sólida?', 'Una institución identificable, una entrevista con autorización y una tercera fuente que coincida', 'Un único video sin fuente', 'Una opinión anónima en un foro', 'Contrastar varias fuentes identificables aumenta la confiabilidad.'),
    ],
    ctx=('abc', 'Un grupo encuentra que una fuente dice que un oficio «tiene mucho trabajo» y otra, que «hay poco». Ninguna da datos. ¿Qué conclusión es coherente?', 'Declarar que las fuentes se contradicen y buscar una fuente con datos verificables', 'Elegir la que más conviene', 'Afirmar que hay mucho trabajo', 'Si no hay datos, se declara la contradicción y se busca mejor evidencia.'),
    sc=[
        ("En Artes: ¿qué es contrastar?", "Comparar con otra fuente independiente", "Reduce el riesgo de aceptar un dato falso."),
        ("¿Qué se pide antes de citar a una persona entrevistada?", "Su autorización", "Es parte del respeto a su palabra."),
        ("¿Se comparten datos personales de quien se entrevista?", "No", "Así se protege su privacidad y su seguridad."),
    ],
    op=("Elige un rol del campo de la asignatura y escribe cómo investigarías: dos tipos de fuentes, cuatro criterios para evaluarlas y cinco preguntas abiertas para una entrevista con autorización.",
        "Rol: fotógrafo. Fuentes: página de una escuela de fotografía y una entrevista. Criterios: autor, fecha, propósito y evidencia. Preguntas: ¿Qué hace en un día de trabajo? ¿Qué herramientas usa? ¿Cómo aprendió? ¿Qué parte es más difícil? ¿Qué consejo da?",
        ["fuentes y criterios", "preguntas abiertas", "autorización y privacidad"],
        ["hoja con el plan de investigación"],
        ["preguntas de sí o no", "no pedir autorización"],
        "Pregunta: «¿cómo sabrás si esa fuente es confiable?». Si no usa criterios, ayúdalo a aplicarlos."),
    reinforce="Anota tres preguntas abiertas que le harías a alguien que trabaje con imágenes.",
    extend="Explica por qué dos fuentes que coinciden dan más seguridad que una sola.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 4 (portafolio y plan de ejemplo, inventados). Una estudiante ficticia revisa su portafolio de 6 trabajos: un afiche, una serie de láminas, un guion de 30 segundos, un storyboard de 6 cuadros, una maqueta de papel y un texto de sala. "
     "Quiere seleccionar 4 trabajos. Para cada uno prepara una ficha con título, propósito, proceso (3 evidencias) y atribución de fuentes; cada ficha le toma 15 minutos. "
     "En el afiche aparece una compañera: la estudiante ya tiene su autorización escrita. En el storyboard usó una frase de una escritora real: la tiene citada entre comillas con atribución. "
     "Plan personal a un año (de ejemplo): objetivo, dos acciones y un recurso. Objetivo: mejorar su comunicación visual. Acciones: practicar un boceto por semana y pedir comentarios cada mes. Recurso: su cuaderno de bitácora.")
build(
    O7, 4, F,
    use="Aprenderé a organizar un portafolio, a cuidar derechos de autor y consentimiento, y a escribir un plan de desarrollo personal con objetivos y acciones.",
    prior=["Sé relacionar habilidades con contextos.", "Sé evaluar fuentes.", "Sé atribuir y pedir permiso."],
    explain=[
        "Un portafolio es una selección de trabajos que muestra lo que sabes hacer y cómo lo hiciste. No incluye todo: se eligen los trabajos que mejor muestran habilidades y procesos. Cada trabajo lleva una ficha con título, propósito, evidencias del proceso y atribución de fuentes. Un portafolio puede servir para estudios, trabajos o para el crecimiento personal.",
        "En el portafolio se cuidan los derechos y la privacidad. La persona que crea una obra es titular de sus derechos de autor, y las obras de otras personas se usan con permiso o con cita breve y atribución. Si aparece una persona, se necesita su consentimiento. No se publican datos personales como direcciones o teléfonos. Antes de publicar en línea se consulta al liceo y, cuando corresponde, a una persona adulta responsable.",
        "El desarrollo personal se planifica con un objetivo, acciones concretas y recursos. Un buen objetivo es específico y posible («mejorar mi comunicación visual practicando un boceto por semana»), no vago («ser mejor»). Se revisa cada cierto tiempo y se ajusta. El plan es propio: no se compara con el de otras personas.",
    ],
    vocab=[("portafolio", "selección de trabajos que muestra habilidades y proceso"), ("derechos de autor", "protección de quien crea una obra"), ("consentimiento", "permiso de una persona para mostrar su imagen"), ("objetivo", "meta específica que se quiere lograr"), ("recurso", "medio que se usa para lograr una meta")],
    worked=[
        ("Calcular el tiempo de las fichas", "¿Cuántos minutos toman las fichas de 4 trabajos?", ["Cada ficha toma 15 minutos.", "4 × 15 = 60."], "60 minutos"),
        ("Revisar derechos y privacidad", "En el afiche aparece una compañera. ¿Puede incluirlo en el portafolio público?", ["La ficha dice que tiene su autorización escrita.", "Sí, con esa autorización y sin datos personales."], "Sí, con su autorización escrita y sin datos personales")
    ],
    mistakes=[("Incluir todos los trabajos en el portafolio.", "Se pierde el foco y se muestra poco proceso.", "Selecciona los más representativos y explica su proceso."),
              ("Escribir un objetivo vago como «ser mejor».", "No se sabe cómo lograrlo ni cómo comprobarlo.", "Hazlo específico, con acciones y un plazo.")],
    T=[
        ('abc', '¿Qué es un portafolio?', 'Una selección de trabajos que muestra habilidades y proceso', 'Un archivo con todos los trabajos sin orden', 'Una nota final', 'El portafolio selecciona y explica los trabajos.'),
        ('abc', '{F} ¿Cuántos trabajos quiere incluir la estudiante?', '4', '6', '2', 'La ficha dice que selecciona 4 de 6.'),
        ('abc', '{F} ¿Qué evidencias lleva cada ficha de trabajo?', '3 evidencias del proceso', '10 evidencias', 'Ninguna', 'La ficha indica 3 evidencias de proceso.'),
        ('abc', '{F} ¿Por qué puede usar la frase de la escritora real en el storyboard?', 'Porque es una cita breve entre comillas y con atribución', 'Porque está en internet', 'Porque nadie lo notará', 'Una cita breve atribuida es aceptable.'),
        ('=', '{F} Si prepara las 4 fichas, ¿cuántas evidencias de proceso reúne en total (3 por ficha)?', '4*3', 'Se multiplican las fichas por las evidencias de cada una.', ' evidencias'),
        ('=', '{F} Si decidiera preparar 5 fichas en lugar de 4, ¿cuántos minutos necesitaría?', '5*15', 'Se multiplica la cantidad de fichas por los minutos de cada una.', ' minutos'),
        ('abc', '{F} En el plan personal, ¿qué es una acción?', 'Practicar un boceto por semana', 'Mejorar su comunicación visual', 'Tener un cuaderno', 'La acción es algo concreto que se hace; el objetivo es la meta.'),
        ('abc', '{F} ¿Qué recurso menciona el plan?', 'Su cuaderno de bitácora', 'Un computador nuevo', 'Un curso pagado', 'El plan menciona su cuaderno de bitácora como recurso.'),
        ('abc', 'La estudiante quiere subir su portafolio a internet con su dirección de casa. ¿Qué corresponde?', 'No publicar la dirección y consultar al liceo y a una persona adulta', 'Publicarla', 'Publicarla en un foro', 'No se publican datos personales en espacios abiertos.'),
        ('abc', 'Un compañero aparece en un trabajo y no ha dado permiso. ¿Qué haces?', 'Pedirle su autorización o no mostrar su imagen', 'Mostrarlo porque está en la foto', 'Cambiar su nombre', 'Mostrar a una persona requiere su consentimiento.'),
        ('=', 'Un plan personal tiene 3 acciones y cada una se repite 12 veces al año. ¿Cuántas veces se hacen al año?', '3*12', 'Se multiplica la cantidad de acciones por las repeticiones.', ' veces'),
        ('abc', '¿Cuál es un objetivo específico y posible?', 'Mejorar mi comunicación visual practicando un boceto por semana', 'Ser el mejor artista del mundo', 'Ser mejor', 'Es específico, tiene acción y se puede comprobar.'),
        ('abc', 'Una persona dice que su plan personal debe ser igual al de su amiga. ¿Qué respondes?', 'Que el plan es propio y depende de sus intereses y posibilidades', 'Que tiene razón', 'Que no es necesario planificar', 'Cada plan responde a objetivos personales.'),
    ],
    ctx=('abc', 'Una estudiante prepara su portafolio y piensa incluir una ilustración copiada de una revista sin citar. ¿Qué es lo mejor?', 'No incluirla o reemplazarla por una obra propia, o citarla y usarla solo con permiso o en comentario breve', 'Incluirla como propia', 'Cambiarle el título', 'Se respeta la autoría y los derechos.'),
    sc=[
        ("En Artes: ¿qué es un portafolio?", "Una selección de trabajos que muestra habilidades y proceso", "Se eligen los trabajos más representativos."),
        ("¿Qué se necesita para mostrar a una persona en un trabajo?", "Su consentimiento", "Así se respeta su imagen y su decisión."),
        ("¿Cómo es un buen objetivo personal?", "Específico, posible y con acciones", "Se puede comprobar si se cumple."),
    ],
    op=("Imagina que tienes 5 trabajos y debes elegir 3 para un portafolio. Elige cuáles con una razón, escribe la ficha de uno (título, propósito, 3 evidencias, atribución) y un plan personal con un objetivo, dos acciones y un recurso.",
        "Elijo: afiche, storyboard y maqueta, porque muestran proceso. Ficha del afiche: título «Lee hoy»; propósito: invitar; evidencias: boceto, prueba de color, comentario; atribución: inspirado en una idea de un cartel conocido (anotado). Plan: objetivo, mejorar mi composición; acciones: un boceto por semana y pedir comentarios cada mes; recurso: mi bitácora.",
        ["selección con razón", "ficha completa con atribución", "plan específico"],
        ["hoja con selección, ficha y plan"],
        ["objetivo vago", "olvidar consentimiento o atribución"],
        "Pregunta: «¿cómo sabrás si cumpliste tu objetivo?». Si no sabe, ayúdalo a hacerlo específico."),
    reinforce="Escribe un objetivo específico para este semestre y dos acciones para lograrlo.",
    extend="Explica por qué mostrar el proceso en un portafolio es tan importante como mostrar el resultado.",
)
