"""Interpretación y creación en danza 3.º y 4.º medio HC: OAC-08 (relacionar, a partir de investigaciones, las habilidades y conocimientos de la asignatura con contextos laborales, profesionales y de desarrollo personal), clases 1 a 4. Casos, fuentes y planes inventados; sin cifras reales de empleo, sueldos ni instituciones."""
from __future__ import annotations

from hc_icda_common import build

O8 = "AR-ICDA-3y4-OAC-08"

# ============================================================ OAC-08, clase 1
F = ("Ficha 1 (mapa de roles de ejemplo, general, sin cifras de empleo ni instituciones). "
     "Intérprete: ejecuta obras y da sentido al movimiento. Coreógrafo o coreógrafa: crea el diseño de una obra y dirige su montaje. "
     "Docente de danza: enseña en escuelas, talleres o centros comunitarios. Gestor o gestora cultural: planifica, busca recursos y difunde proyectos. "
     "Producción técnica: se ocupa de la luz, el sonido, el espacio y el montaje. Mediación y crítica: ayuda al público a comprender y comenta obras con argumentos. "
     "Investigación del movimiento: estudia cómo se mueve el cuerpo en contextos como la educación, el deporte o el patrimonio; algunas ocupaciones que usan el movimiento en salud exigen una formación específica que se consulta en instituciones de educación. "
     "Contextos donde ocurren: escuelas, centros culturales, espacios comunitarios, medios audiovisuales y proyectos independientes. "
     "Habilidades de la asignatura: composición, interpretación, análisis estético, gestión de proyectos y trabajo en equipo.")
build(
    O8, 1, F,
    use="Aprenderé a relacionar las habilidades y conocimientos de la asignatura con roles y contextos laborales y profesionales del campo de la danza, y a investigar con fuentes confiables qué hace cada rol.",
    prior=["Sé componer, interpretar y analizar obras.", "Sé gestionar una presentación.", "Sé evaluar procesos y resultados."],
    explain=[
        "La danza no es solo bailar: es un campo de trabajo con muchos roles que se complementan. El intérprete ejecuta y da sentido a las obras. El coreógrafo o la coreógrafa crea el diseño y dirige el montaje. El docente enseña en escuelas, talleres o centros comunitarios. El gestor o la gestora cultural planifica, busca recursos y difunde proyectos. La producción técnica se ocupa de la luz, el sonido, el espacio y el montaje. La mediación y la crítica ayudan al público a comprender. Y la investigación estudia el movimiento en contextos como la educación o el patrimonio.",
        "Cada rol usa habilidades que ya trabajaste en esta asignatura: componer (coreografía), interpretar (intérprete), analizar y argumentar juicios (mediación y crítica), gestionar presentaciones (gestión cultural), planificar espacio y recursos (producción técnica), enseñar y dar retroalimentación (docencia). Vincular habilidades con roles ayuda a imaginar posibles caminos, sin que ninguno sea obligatorio ni «mejor» que otro. Un mismo proyecto suele necesitar varios roles a la vez.",
        "Para investigar un rol se usan fuentes confiables: instituciones educativas y culturales oficiales, documentos públicos y entrevistas hechas con consentimiento a personas que trabajan en el medio. Este cuaderno no entrega cifras de empleo, sueldos ni nombres de instituciones: son orientaciones generales y de ejemplo, y cualquier decisión vocacional se conversa con una persona orientadora y se contrasta con información actual. Ninguna ocupación se evalúa por el cuerpo de quien la ejerce.",
    ],
    vocab=[("rol", "conjunto de tareas dentro de un proyecto o profesión"), ("contexto laboral", "lugar o ámbito donde se ejerce un trabajo"), ("gestión cultural", "planificar, financiar y difundir proyectos culturales"), ("producción técnica", "ocuparse de luz, sonido, espacio y montaje"), ("mediación", "ayudar al público a comprender una obra"), ("fuente confiable", "fuente identificable, actual y con información verificable")],
    worked=[
        ("Relacionar una habilidad con un rol", "Una persona es muy buena planificando presupuestos y calendarios para presentaciones. ¿Con qué rol se relaciona?", ["Planificar y buscar recursos es parte de la gestión.", "Ese rol es gestor o gestora cultural."], "Gestión cultural"),
        ("Distinguir roles de un mismo proyecto", "En una muestra, una persona diseña el montaje de luces y otra escribe el programa de mano. ¿Qué roles son?", ["Luces y montaje son producción técnica.", "El programa de mano es difusión y mediación."], "Producción técnica y difusión o mediación"),
    ],
    mistakes=[("Creer que la danza solo ofrece el camino de ser intérprete.", "El campo tiene muchos roles que se complementan.", "Explora varios roles y las habilidades que usa cada uno."),
              ("Usar cifras de sueldos o empleo vistas sin fuente.", "Los datos sin fuente identificable pueden ser falsos o estar desactualizados.", "Busca fuentes oficiales actuales o conversa con personas del medio.")],
    T=[
        ('abc', 'En creación en danza, ¿qué hace la persona que cumple el rol de producción técnica?', 'Se ocupa de la luz, el sonido, el espacio y el montaje', 'Escribe y publica críticas de las obras que ve', 'Busca recursos y diseña la difusión de los proyectos', 'La producción técnica ve lo material de una presentación.'),
        ('abc', '{F} ¿Qué rol crea el diseño de una obra y dirige su montaje?', 'Coreógrafo o coreógrafa', 'Gestor o gestora cultural', 'Docente de danza', 'La ficha asigna la creación y dirección del diseño al coreógrafo o coreógrafa.'),
        ('abc', '{F} ¿En qué contextos puede enseñar un docente de danza?', 'En escuelas, talleres o centros comunitarios', 'Solo en teatros de gran tamaño con escenario frontal', 'Únicamente en programas de televisión de la tarde', 'La ficha menciona escuelas, talleres y centros comunitarios.'),
        ('abc', '{F} ¿Qué habilidad de la asignatura se vincula más con el rol de mediación y crítica?', 'Análisis estético y juicios argumentados', 'Composición de frases de movimiento con motivos', 'Montaje de luces y de sonido en la sala', 'La mediación y la crítica comentan obras con argumentos.'),
        ('abc', '{F} ¿Qué habilidad se vincula más con la gestión cultural?', 'Planificar, buscar recursos y difundir', 'Memorizar secuencias de movimiento largas', 'Analizar el flujo de una frase de danza', 'La gestión cultural planifica, financia y difunde.'),
        ('abc', '{F} Una persona dice: «solo se puede trabajar en danza siendo intérprete». ¿Qué corresponde responder?', 'Que hay muchos roles que se complementan', 'Que tiene razón, porque los otros roles no existen en la danza', 'Que los otros roles son de menor valor para una obra', 'El campo tiene muchos roles y ninguno es «mejor» que otro.'),
        ('=', '{F} Un proyecto de una muestra necesita 1 coreógrafo, 4 intérpretes, 2 personas de producción técnica y 1 de gestión. ¿Cuántas personas son en total?', '1+4+2+1', 'Se suman las personas de cada rol.', ' personas'),
        ('abc', '{F} Para investigar qué hace una persona que gestiona proyectos, ¿cuál es la fuente más confiable?', 'Una entrevista con consentimiento a quien trabaja en ello', 'Un comentario anónimo sin fecha ni autoría en un foro', 'Un rumor que se comenta en el patio del colegio', 'Una entrevista con consentimiento identifica a quien habla y su experiencia.'),
        ('abc', '{F} Alguien dice que en este campo «se gana mucho» y no cita fuente. ¿Qué corresponde?', 'Pedir la fuente o buscar información oficial actual', 'Aceptarlo como cierto y usarlo para elegir', 'Repetirlo al curso para avisar a todas las personas', 'Una afirmación sin fuente no es evidencia; se contrasta.'),
        ('abc', 'Dos estudiantes discuten: uno dice que el rol de intérprete es el único «de verdad»; la otra, que todos los roles son necesarios para que una obra exista. ¿Quién argumenta mejor?', 'La otra, porque una obra necesita varios roles', 'El primero, porque el intérprete es quien más se ve', 'Ninguno, porque los roles no son necesarios en una obra', 'Una obra se sostiene con muchos roles, aunque algunos se vean más.'),
        ('abc', '{F} Un curso quiere organizar una muestra y le falta alguien que se encargue del sonido y las luces. ¿Qué rol necesita?', 'Producción técnica', 'Mediación y crítica', 'Investigación del movimiento', 'Luz y sonido pertenecen a la producción técnica.'),
        ('abc', '{F} Un integrante propone elegir un rol según «quién tiene el cuerpo más adecuado». ¿Qué corresponde?', 'Rechazarlo: los roles se eligen por intereses y habilidades', 'Aceptarlo, porque los cuerpos influyen en todo lo que se hace', 'Aceptarlo solo para el rol de intérprete y de coreografía', 'Los cuerpos no se evalúan ni definen roles.'),
        ('abc', 'Una estudiante investiga una ocupación que usa el movimiento en el ámbito de la salud y duda cómo se llega a ella. ¿Qué es lo más adecuado?', 'Consultar a una persona orientadora y a instituciones de educación', 'Practicar por su cuenta con otras personas sin formación', 'Dar por hecho que no se necesita formación especial', 'Las ocupaciones de salud exigen formación específica y se consultan en instituciones.'),
    ],
    ctx=('abc', 'Un curso tiene 12 estudiantes y quiere organizar una muestra. Reparten 5 intérpretes, 2 de producción técnica, 2 de gestión y difusión, 1 de coreografía y el resto de mediación y crítica. ¿Cuántas personas hay en mediación y crítica?', '2 personas', '3 personas', '1 persona', 'Los otros roles suman 10 y quedan 12 - 10 = 2 personas para mediación y crítica.'),
    sc=[
        ("En creación en danza: ¿qué hace un gestor o gestora cultural?", "Planifica, busca recursos y difunde proyectos", "Son tareas de organización y difusión."),
        ("¿Por qué conviene investigar con fuentes identificables?", "Porque se puede verificar quién lo dice y si está actualizado", "Una fuente anónima no se puede comprobar."),
        ("¿Se elige un rol por el cuerpo de la persona?", "No: se elige por intereses y habilidades", "Los cuerpos no se evalúan ni definen un rol."),
    ],
    op=("Elige dos roles del mapa de la ficha. Para cada uno escribe: qué hace, dos habilidades de esta asignatura que usa, un contexto donde podría ejercerse y una pregunta que le harías en una entrevista (con consentimiento) a una persona que lo ejerza. Luego escribe en dos oraciones por qué ninguna ocupación es «mejor» que otra y una fuente confiable que consultarías para contrastar. No uses cifras de sueldos ni de empleo.",
        "Roles: docencia y gestión cultural. Docencia: enseña en escuelas o talleres; usa composición y retroalimentación; contexto: centro comunitario; pregunta: «¿qué habilidades de la danza usa cuando prepara una clase?». Gestión: planifica y difunde proyectos; usa gestión de presentaciones y trabajo en equipo; contexto: centro cultural; pregunta: «¿cómo organiza un cronograma?». Todas las ocupaciones complementan un proyecto. Fuente confiable: sitio de una institución de educación y conversación con una persona orientadora.",
        ["relaciona habilidades de la asignatura con cada rol", "propone preguntas y fuentes confiables", "evita cifras sin fuente y no valora cuerpos"],
        ["hoja con dos roles, habilidades, contextos, preguntas y fuente"],
        ["usar cifras sin fuente", "valorar roles por el cuerpo", "asumir que hay un solo camino"],
        "Pregunta: «¿qué habilidad de la asignatura usa ese rol?». Si responde «baila», pídele que piense en composición, gestión o análisis."),
    reinforce="Escribe una lista de cuatro roles de un proyecto de danza y para cada uno una tarea y una habilidad de esta asignatura.",
    extend="Explica por qué una obra de danza necesita varios roles y qué pasaría si faltara uno de ellos.",
)

# ============================================================ OAC-08, clase 2
F = ("Ficha 2 (evidencias y habilidades de ejemplo, inventadas). Habilidades transferibles: trabajo en equipo, comunicación, gestión del tiempo, resolución de problemas, memoria y atención, creatividad y perseverancia. "
     "Evidencias de ejemplo del trabajo en esta asignatura: E1, «coordinamos entradas de un canon de 5 personas sin contacto y ajustamos una señal de mirada»; "
     "E2, «llegamos al ensayo general con el montaje listo 1 hora antes y un guion horario»; "
     "E3, «cuando falló el sonido, acordamos una versión en silencio y la presentación siguió»; "
     "E4, «dimos retroalimentación descriptiva a otro grupo con observo, esto produce y me pregunto si»; "
     "E5, «repetimos 6 ensayos de 30 minutos, con descansos, hasta cumplir la meta de claridad». "
     "Contextos de uso de ejemplo: coordinar un equipo en una empresa pequeña, exponer un proyecto ante un público, enseñar a otras personas, organizar un evento, resolver un imprevisto en un trabajo grupal.")
build(
    O8, 2, F,
    use="Aprenderé a identificar habilidades transferibles que desarrollo en esta asignatura y a respaldarlas con evidencias de mi trabajo, para relacionarlas con contextos laborales, profesionales y de desarrollo personal.",
    prior=["Conozco roles del campo de la danza.", "Sé evaluar procesos y resultados con evidencias.", "Sé dar retroalimentación descriptiva."],
    explain=[
        "Una habilidad transferible es una capacidad que se aprende en un contexto y sirve en otros. En esta asignatura se entrenan varias: trabajo en equipo (coordinar entradas, acordar decisiones), comunicación (explicar un propósito, dar retroalimentación), gestión del tiempo (cumplir un cronograma), resolución de problemas (ajustar una frase cuando algo falla), memoria y atención, creatividad (componer con propósito) y perseverancia (repetir ensayos hasta una meta). Estas capacidades no pertenecen solo a la danza: se valoran en proyectos de muchos ámbitos.",
        "Decir «soy buena en trabajo en equipo» no basta. Una habilidad se demuestra con una evidencia: un hecho concreto de lo que hiciste, con un resultado observable. Por ejemplo, «coordinamos las entradas de un canon de 5 personas sin contacto y ajustamos una señal de mirada» es evidencia de trabajo en equipo y resolución de problemas. Para vincular una habilidad con un contexto se explica cómo se usa allí: coordinar entradas se parece a organizar turnos de un equipo en un evento.",
        "El desarrollo personal también cuenta: cuidar el cuerpo con calentamiento y descanso, reconocer los propios límites y pedir ayuda a una persona adulta cuando algo preocupa son parte de las habilidades para la vida. Las habilidades no se comparan entre personas ni se miden por el cuerpo: cada persona avanza a su ritmo. Este cuaderno no promete resultados laborales: solo propone formas de reconocer lo aprendido y de explicarlo con evidencias.",
    ],
    vocab=[("habilidad transferible", "capacidad que se aprende en un contexto y sirve en otros"), ("evidencia", "hecho concreto que demuestra una habilidad"), ("resolución de problemas", "ajustar el plan cuando algo falla"), ("perseverancia", "continuar un trabajo hasta alcanzar una meta"), ("gestión del tiempo", "cumplir plazos y organizar tareas"), ("desarrollo personal", "crecimiento en habilidades y cuidado de uno mismo")],
    worked=[
        ("Respaldar una habilidad", "Dices que tienes gestión del tiempo. ¿Qué evidencia de la ficha la respalda?", ["Busca una evidencia que muestre plazos cumplidos.", "E2 muestra un montaje listo con anticipación y un guion horario."], "E2"),
        ("Relacionar con un contexto", "Coordinar las entradas de un canon, ¿con qué tarea de otro contexto se parece?", ["Es organizar turnos y señales entre varias personas.", "Se parece a coordinar turnos de un equipo en un evento."], "Coordinar turnos de un equipo en un evento"),
    ],
    mistakes=[("Afirmar una habilidad sin mostrar ninguna evidencia.", "Sin un hecho concreto no se puede comprobar ni comunicar.", "Cita un hecho con su resultado observable."),
              ("Creer que una habilidad vale solo en la danza.", "Las habilidades transferibles sirven en otros contextos.", "Explica cómo se usaría en otro ámbito.")],
    T=[
        ('abc', 'En creación en danza, ¿qué es una habilidad transferible?', 'Una capacidad que se aprende en un contexto y sirve en otros', 'Un paso de danza que se puede enseñar a otras personas', 'Una técnica especial que solo usan las personas profesionales', 'Una habilidad transferible no se limita a un contexto.'),
        ('abc', '{F} ¿Qué evidencia respalda el trabajo en equipo?', 'E1, coordinar un canon sin contacto', 'E5, repetir ensayos hasta la meta', 'E3, acordar versión en silencio', 'E1 muestra coordinación entre varias personas; E3 muestra resolución de problemas.'),
        ('abc', '{F} ¿Qué habilidad respalda la evidencia E3?', 'Resolución de problemas', 'Memoria', 'Creatividad', 'Cuando falló el sonido, buscaron una alternativa para que la presentación siguiera.'),
        ('abc', '{F} ¿Qué habilidad respalda la evidencia E5?', 'Perseverancia', 'Comunicación', 'Gestión del tiempo', 'Repetir ensayos hasta cumplir la meta muestra perseverancia.'),
        ('abc', '{F} ¿Qué habilidad respalda la evidencia E4?', 'Comunicación', 'Perseverancia', 'Memoria', 'La retroalimentación descriptiva es una forma de comunicarse con claridad y respeto.'),
        ('=', '{F} En E5, ¿cuántos minutos de ensayo suman los 6 ensayos?', '6*30', 'Se multiplican los ensayos por su duración.', ' minutos'),
        ('abc', '{F} ¿Qué contexto de uso de la ficha se parece más a E2, el montaje listo con anticipación?', 'Organizar un evento', 'Enseñar a otras personas', 'Exponer un proyecto ante un público', 'Preparar el montaje con tiempo se parece a organizar un evento.'),
        ('abc', '{F} Una persona dice: «tengo creatividad» sin dar ningún ejemplo. ¿Qué corresponde pedirle?', 'Una evidencia concreta, como una frase que compuso', 'Que lo repita con más seguridad y más fuerza', 'Que se compare con otra persona del curso y diga quién es mejor', 'Una habilidad se respalda con un hecho concreto y no con una declaración.'),
        ('abc', '{F} ¿Cuál es la forma más completa de presentar una habilidad ante una persona que organiza un proyecto?', 'Decir la habilidad, citar una evidencia y explicar cómo se usaría', 'Decir que se tiene la habilidad y que se es una persona responsable', 'Decir que todo se aprende rápido y que no hay problema', 'La estructura habilidad, evidencia y uso permite comprobar y relacionar.'),
        ('abc', 'Dos estudiantes discuten: uno dice que las habilidades de la danza solo sirven para bailar; la otra, que varias se pueden usar en otros contextos. ¿Quién argumenta mejor?', 'La otra, porque coordinar y comunicar se usan en muchos ámbitos', 'El primero, porque cada disciplina tiene habilidades exclusivas de su campo', 'Ninguno, porque las habilidades no se pueden transferir a otros ámbitos', 'Las habilidades transferibles sirven en otros contextos.'),
        ('abc', '{F} Un integrante dice que su habilidad «es mejor» que la de otra persona porque su cuerpo se mueve con más amplitud. ¿Qué corresponde?', 'Recordar que las habilidades no se comparan por el cuerpo', 'Aceptarlo, porque la amplitud del movimiento es una habilidad', 'Pedir que se compare con todo el curso y se haga una lista', 'No se compara el cuerpo ni se jerarquizan personas.'),
        ('abc', '{F} Si una empresa pequeña busca a alguien para coordinar turnos en un evento, ¿qué evidencia de la ficha sería más pertinente?', 'E1, porque muestra coordinación de entradas', 'E4, porque muestra retroalimentación a otro grupo', 'E5, porque muestra repetición de ensayos con descanso', 'Coordinar turnos se parece a coordinar entradas de un canon.'),
        ('abc', 'Después de varias semanas de ensayos, una estudiante siente un cansancio fuerte y se pone triste. ¿Qué corresponde?', 'Descansar, reducir la carga y avisar a una persona adulta', 'Seguir ensayando todo el día para mostrar perseverancia', 'Ocultarlo para no preocupar al grupo ni a las personas de su casa', 'El bienestar va primero; se avisa a una persona adulta de confianza.'),
    ],
    ctx=('abc', 'Una estudiante prepara su presentación personal para un taller de voluntariado en un centro comunitario y quiere mostrar su trabajo en equipo. ¿Cuál es la frase mejor armada?', 'Coordinamos las entradas de un canon de 5 personas, lo que me sirve para coordinar turnos', 'Soy muy buena para trabajar en equipo y todo el mundo lo sabe', 'Siempre he sido una persona muy responsable y puntual en todo lo que hago', 'La primera cita una evidencia y la relaciona con el nuevo contexto.'),
    sc=[
        ("En creación en danza: ¿cómo se respalda una habilidad?", "Con una evidencia concreta y observable", "Un hecho concreto permite comprobarla y explicarla a otras personas."),
        ("¿Qué significa que una habilidad sea transferible?", "Que sirve en contextos distintos de donde se aprendió", "Se puede usar en otros ámbitos."),
        ("¿Se comparan las habilidades por el cuerpo de las personas?", "No, nunca", "Los cuerpos no se evalúan ni se jerarquizan."),
    ],
    op=("Elige tres habilidades de la ficha. Para cada una escribe: una evidencia propia o inventada del trabajo de esta asignatura (con un resultado observable) y un contexto donde se usaría (laboral, profesional o de desarrollo personal), explicando cómo se parece la tarea. Luego escribe una frase de presentación de dos oraciones para ese contexto. No uses cifras que no puedas respaldar.",
        "Habilidad 1: gestión del tiempo. Evidencia: preparamos el montaje 1 hora antes con un guion horario. Contexto: organizar un evento escolar; se parece porque ambos exigen cumplir un cronograma. Habilidad 2: comunicación. Evidencia: dimos retroalimentación con observo, esto produce y me pregunto si. Contexto: enseñar a otras personas. Habilidad 3: resolución de problemas. Evidencia: ante la falla del sonido hicimos una versión en silencio. Contexto: un imprevisto en un equipo. Presentación: «Tengo experiencia coordinando montajes con guion horario y adaptándome a imprevistos».",
        ["cada habilidad tiene una evidencia concreta", "relaciona la habilidad con un contexto y explica la semejanza", "la frase de presentación es clara y no inventa cifras"],
        ["hoja con tres habilidades, evidencias, contextos y frase de presentación"],
        ["habilidad sin evidencia", "cifras sin respaldo", "comparar cuerpos o personas"],
        "Pregunta: «¿qué hecho muestra esa habilidad?». Si responde con un adjetivo, pídele un ejemplo con resultado."),
    reinforce="Escribe tres evidencias distintas de tu trabajo en esta asignatura y la habilidad transferible que muestra cada una.",
    extend="Explica por qué una evidencia concreta convence más que una afirmación general y cómo la usarías en una presentación personal.",
)

# ============================================================ OAC-08, clase 3
F = ("Ficha 3 (investigación de ejemplo, inventada; sin personas, instituciones ni cifras reales). Pregunta de investigación: «¿Qué hace una persona que gestiona proyectos de danza y qué habilidades usa?» "
     "Fuente A (entrevista de ejemplo, hecha con consentimiento): una gestora cultural ficticia dice «mi trabajo es planificar el calendario, buscar recursos y coordinar a las personas de un proyecto». "
     "Fuente B (sitio de ejemplo de una institución educativa ficticia): describe un programa de formación en gestión cultural, con requisitos y duración. "
     "Fuente C (comentario anónimo en un foro de ejemplo, sin fecha): «con la danza se gana mucho dinero». "
     "Criterios de confiabilidad: se sabe quién lo dice, es actual, está respaldada y tiene propósito claro. "
     "Registro de ejemplo: fuente, qué dice, fecha, confiabilidad y para qué sirve. "
     "Reglas éticas de la entrevista: pedir consentimiento, avisar para qué se usará, no pedir datos personales ni cifras privadas y poder retirar lo dicho.")
build(
    O8, 3, F,
    use="Aprenderé a investigar un contexto laboral o profesional con preguntas claras, fuentes confiables y un registro ordenado, contrastando fuentes y respetando la ética de una entrevista.",
    prior=["Conozco roles y habilidades del campo.", "Sé respaldar una afirmación con evidencias.", "Sé citar el origen de una información."],
    explain=[
        "Investigar es buscar respuestas a una pregunta con método. Se parte por una pregunta clara («¿qué hace una persona que gestiona proyectos de danza y qué habilidades usa?»), se buscan fuentes distintas y se registra lo que cada una dice. Una fuente puede ser una entrevista, un documento oficial, el sitio de una institución educativa o un artículo. No toda fuente es igual de confiable: se evalúa si se sabe quién lo dice, si es actual, si está respaldada con información comprobable y si su propósito es claro.",
        "Un comentario anónimo y sin fecha, como «con la danza se gana mucho dinero», es una fuente débil: no se sabe quién lo dice ni de dónde sale. Se contrasta con otras fuentes y, si no se puede respaldar, no se usa. Contrastar es comparar lo que dicen dos o más fuentes: si coinciden, la información se fortalece; si se contradicen, se busca una tercera o se aclara la diferencia. El registro anota fuente, qué dice, fecha, confiabilidad y para qué sirve.",
        "La entrevista a una persona del medio exige ética. Se pide su consentimiento, se explica para qué se usará lo que diga, no se piden datos personales ni cifras privadas, y la persona puede retirar lo que dijo. En las entrevistas a personas adultas o a personas menores de edad se cuida la privacidad. Este cuaderno no entrega datos laborales reales: usa fuentes inventadas para practicar el método.",
    ],
    vocab=[("pregunta de investigación", "pregunta clara que guía la búsqueda"), ("fuente", "origen de una información"), ("confiabilidad", "grado en que una fuente merece confianza"), ("contrastar", "comparar lo que dicen varias fuentes"), ("registro", "anotación ordenada de fuente, dato y fecha"), ("consentimiento", "autorización para usar lo que alguien dice")],
    worked=[
        ("Evaluar una fuente", "Un texto sin autor ni fecha dice que «todo el mundo estudia gestión cultural». ¿Es confiable?", ["No se sabe quién lo dice ni cuándo.", "No está respaldado: es débil."], "No es confiable"),
        ("Contrastar dos fuentes", "Fuente 1: «la formación dura 2 años». Fuente 2: «la formación dura 4 años». ¿Qué conviene hacer?", ["Hay una contradicción.", "Se busca una tercera fuente o se aclara si hablan de programas distintos."], "Buscar una tercera fuente o aclarar si son programas distintos"),
    ],
    mistakes=[("Quedarse con la primera fuente que se encuentra.", "Una sola fuente puede ser incompleta o sesgada.", "Busca al menos dos fuentes y contrástalas."),
              ("Pedir en una entrevista cifras privadas o datos personales.", "Es una intromisión y no es necesario para la investigación.", "Pregunta por tareas, habilidades y formación, no por datos privados.")],
    T=[
        ('abc', 'En creación en danza, ¿qué significa contrastar fuentes?', 'Comparar lo que dicen varias fuentes sobre lo mismo', 'Elegir la fuente que dice lo que uno quiere escuchar', 'Copiar la fuente más larga para no equivocarse', 'Contrastar es comparar para fortalecer o aclarar.'),
        ('abc', '{F} ¿Cuál es la pregunta de investigación?', '¿Qué hace una persona que gestiona proyectos de danza y qué habilidades usa?', '¿Cuánto dinero gana una persona que se dedica a la danza, cada mes y cada año?', '¿Quién es la persona más famosa de la danza en el país y qué premios tiene?', 'La pregunta de la ficha se centra en tareas y habilidades.'),
        ('abc', '{F} ¿Qué fuente de la ficha es una entrevista?', 'La fuente A', 'La fuente B', 'La fuente C', 'La fuente A es una entrevista de ejemplo hecha con consentimiento.'),
        ('abc', '{F} ¿Qué fuente es la menos confiable?', 'La fuente C, porque es anónima y sin fecha', 'La fuente A, porque habla una sola persona sobre su experiencia', 'La fuente B, porque describe un programa de formación', 'La fuente C no permite saber quién lo dice ni de dónde sale.'),
        ('abc', '{F} ¿Qué información aporta la fuente A sobre las tareas?', 'Planificar el calendario y coordinar personas', 'Cuánto dinero gana la persona cada mes', 'Dónde vive la persona entrevistada y con quién', 'La fuente A describe tareas de gestión.'),
        ('=', '{F} La fuente B dice que el programa tiene 4 semestres y cada semestre dura 5 meses. ¿Cuántos meses dura en total?', '4*5', 'Se multiplican los semestres por los meses de cada uno.', ' meses'),
        ('abc', '{F} ¿Qué se debe hacer con la fuente C si no se puede respaldar?', 'No usarla o buscar otras fuentes que la confirmen', 'Usarla porque es breve y fácil de citar', 'Usarla como dato central de la investigación', 'Una fuente sin respaldo no sirve como dato central.'),
        ('abc', '{F} Para una entrevista a una persona del medio, ¿qué paso es obligatorio?', 'Pedir su consentimiento y explicar para qué se usará', 'Grabar sin avisar para que hable con naturalidad', 'Preguntarle cuánto gana y cuánto ahorra', 'La entrevista exige consentimiento y propósito claros.'),
        ('abc', '{F} ¿Cuál de estas es una buena pregunta de entrevista?', '¿Qué tareas hace en un día de trabajo?', '¿Cuánto dinero tiene en el banco y qué ahorra?', '¿Dónde vive y con quién comparte su casa?', 'Pregunta por tareas y habilidades, no por datos privados.'),
        ('abc', 'Dos estudiantes discuten: uno dice que con una sola fuente basta si es muy convincente; la otra, que hay que contrastar al menos dos. ¿Quién argumenta mejor?', 'La otra, porque contrastar fortalece la información', 'El primero, porque lo convincente siempre es verdadero y completo', 'Ninguno, porque las fuentes no se pueden evaluar con criterios', 'Una sola fuente puede estar sesgada o incompleta.'),
        ('abc', '{F} Una fuente dice que un taller de producción dura 6 meses y otra que dura 12. ¿Qué conclusión es más prudente?', 'Hay una diferencia que conviene aclarar con otra fuente', 'La primera es verdadera y la otra es falsa por ser distinta', 'Las dos son falsas porque no coinciden entre sí', 'Una contradicción se investiga, no se resuelve por impresión.'),
        ('abc', '{F} Una persona entrevistada pide retirar una frase que dijo. ¿Qué corresponde?', 'Retirar la frase del registro y respetar su decisión de hablar', 'Dejarla en el informe porque ya se grabó la entrevista', 'Pedirle que la explique en detalle antes de retirarla', 'El consentimiento incluye poder retirar lo dicho.'),
        ('abc', 'Una estudiante menor de edad quiere entrevistar sola a una persona desconocida en un lugar apartado. ¿Qué corresponde?', 'Hacerlo en un lugar público y avisar a una persona adulta', 'Hacerlo en secreto para que sea más espontáneo y natural', 'Hacerlo sin avisar a nadie, porque es un trabajo de la clase', 'La seguridad primero: lugar público, compañía y aviso a una persona adulta.'),
    ],
    ctx=('abc', 'Un curso investiga qué hace una persona que organiza proyectos de danza. Tiene la fuente A (entrevista con consentimiento), la fuente B (sitio institucional) y la fuente C (comentario anónimo sin fecha). ¿Qué plan es más sólido?', 'Usar A y B, contrastarlas y descartar C', 'Usar solo C porque es la más breve y fácil de citar', 'Usar solo A y no contrastar con otras fuentes confiables', 'Contrastar dos fuentes confiables y descartar la débil es el método más sólido.'),
    sc=[
        ("En creación en danza: ¿qué criterios hacen confiable una fuente?", "Se sabe quién la dice, es actual, está respaldada y tiene propósito claro", "Esos criterios permiten comprobar la fuente con datos."),
        ("¿Qué se pide antes de una entrevista?", "El consentimiento de la persona", "Explicar para qué se usará lo que diga."),
        ("¿Qué se hace con una afirmación sin fuente?", "Se contrasta o no se usa", "Sin respaldo una afirmación no es evidencia."),
    ],
    op=("Elige un rol del campo de la danza (docencia, gestión, producción técnica, mediación u otro) y escribe una pregunta de investigación. Luego completa un registro de tres fuentes (de ejemplo, inventadas por ti): qué dice cada una, su fecha, su confiabilidad según los cuatro criterios y para qué sirve. Escribe tres preguntas de entrevista (sin datos privados) y una regla ética que cumplirías. Termina con una conclusión de dos oraciones que cite al menos dos fuentes.",
        "Rol: producción técnica. Pregunta: ¿qué hace y qué habilidades usa? Fuente 1 (entrevista ficticia, hoy): «preparo luz, sonido y montaje antes de cada función»; confiable: se sabe quién lo dice. Fuente 2 (sitio de una institución, ficticio): describe un taller de producción técnica; confiable. Fuente 3 (comentario anónimo): «es fácil»; no confiable. Preguntas: ¿qué hace en un montaje?, ¿qué habilidades usa?, ¿cómo se prepara para una función?. Regla: pedir consentimiento. Conclusión: según las fuentes 1 y 2, la producción técnica prepara luz, sonido y montaje y exige organización y atención.",
        ["la pregunta es clara y las fuentes están evaluadas con criterios", "las preguntas de entrevista no piden datos privados", "la conclusión cita fuentes y es prudente"],
        ["hoja con pregunta, registro de fuentes, entrevistas y conclusión"],
        ["usar fuentes anónimas como evidencia", "preguntar datos privados", "no contrastar fuentes"],
        "Pregunta: «¿qué fuente respalda esa conclusión y qué tan confiable es?». Si no cita fuentes, pídele que vuelva al registro."),
    reinforce="Escribe tres criterios para decidir si una fuente es confiable y aplícalos a una fuente inventada.",
    extend="Explica por qué contrastar fuentes ayuda a evitar errores y qué harías si dos fuentes confiables se contradicen.",
)

# ============================================================ OAC-08, clase 4
F = ("Ficha 4 (plan de desarrollo personal de ejemplo, inventado). Persona inventada: Sofía, estudiante de enseñanza media. Meta de 12 semanas: «mejorar mi gestión de proyectos escolares de danza». "
     "Acciones: A1, practicar un cronograma hacia atrás para una muestra (1 hora por semana); A2, ensayar una presentación breve del proyecto ante 1 o 2 personas de confianza (30 minutos por semana); "
     "A3, entrevistar con consentimiento a una persona que gestiona proyectos (2 horas en total); A4, dormir y descansar según lo que recomiende una persona adulta de confianza, sin descuidar el estudio. "
     "Tiempo disponible: 3 horas por semana para su meta. Indicadores: tener un cronograma con 5 tareas ordenadas hacia atrás y cumplir la presentación en 5 minutos. "
     "Criterio SMART resumido: específica, medible, alcanzable, relevante y con plazo. "
     "Cuidado personal: calentar antes y descansar después de las actividades físicas; si hay dolor, cansancio fuerte o tristeza persistente, avisar a una persona adulta de confianza. "
     "Este plan es solo un ejemplo y no es consejo médico ni vocacional.")
build(
    O8, 4, F,
    use="Aprenderé a elaborar un plan de desarrollo personal con una meta específica y medible, acciones con tiempos, indicadores y cuidado del cuerpo y del bienestar, relacionando lo aprendido en la asignatura con mi proyecto personal.",
    prior=["Conozco roles y habilidades transferibles.", "Sé investigar con fuentes confiables.", "Sé planificar con cronogramas."],
    explain=[
        "Un plan de desarrollo personal es un proyecto sobre uno mismo: define qué se quiere lograr, cómo y en cuánto tiempo. Una meta útil cumple cinco condiciones, que forman el criterio SMART resumido: es específica (dice exactamente qué), medible (se puede comprobar con un dato), alcanzable (es realista con el tiempo y los recursos), relevante (importa para la persona) y tiene plazo (una fecha o un número de semanas). «Mejorar mi gestión de proyectos escolares de danza en 12 semanas» es más útil que «mejorar».",
        "Las acciones son los pasos concretos, con tiempo asignado. En la ficha, Sofía dispone de 3 horas por semana: 1 hora de cronograma, 30 minutos de ensayo de la presentación, y las 2 horas de entrevista repartidas en las semanas. Se verifica que las acciones quepan en el tiempo disponible. Los indicadores muestran si se avanza: tener un cronograma con 5 tareas y presentar en 5 minutos. Si algo no funciona, se ajusta el plan sin culparse.",
        "El desarrollo personal incluye cuidar el cuerpo y el bienestar: calentar antes y descansar después de actividades físicas, dormir lo necesario, no comparar el cuerpo ni el progreso con otras personas, y avisar a una persona adulta de confianza si hay dolor, cansancio fuerte o tristeza que no pasa. Un plan no debe exigir más de lo que cada cuerpo y cada vida permiten. Este cuaderno no da consejos médicos ni vocacionales: son ejemplos para practicar.",
    ],
    vocab=[("plan de desarrollo personal", "proyecto sobre uno mismo con meta, acciones y plazos"), ("meta SMART", "meta específica, medible, alcanzable, relevante y con plazo"), ("indicador", "dato que muestra si se avanza"), ("acción", "paso concreto con tiempo asignado"), ("alcanzable", "realista según el tiempo y los recursos"), ("bienestar", "estado de cuidado del cuerpo y de la mente")],
    worked=[
        ("Revisar una meta", "«Quiero ser mejor en danza». ¿Qué condiciones SMART le faltan?", ["No dice qué aspecto específico ni cómo se medirá.", "Tampoco tiene un plazo."], "Específica, medible y con plazo"),
        ("Verificar el tiempo", "Un plan tiene 2 acciones de 1 hora y 45 minutos por semana y se dispone de 3 horas. ¿Caben?", ["Suma el tiempo en minutos: 60 + 60 + 45 = 165 minutos.", "3 horas son 180 minutos y 165 es menor."], "Sí, caben con 15 minutos libres"),
    ],
    mistakes=[("Plantear metas vagas como «mejorar» o «ser mejor».", "No se pueden medir ni tienen plazo.", "Haz la meta específica, medible y con plazo."),
              ("Llenar el plan de actividades hasta no dejar descanso.", "Sin descanso se pone en riesgo el bienestar y el plan no se sostiene.", "Verifica que quepa en el tiempo y deja espacio para descansar.")],
    T=[
        ('abc', 'En creación en danza, ¿qué significa que una meta sea medible?', 'Que se puede comprobar con un dato', 'Que se hace en un lugar con medidas conocidas de antemano', 'Que otra persona la elige y la mide por uno durante el año', 'Una meta medible se comprueba con un dato observable.'),
        ('abc', '{F} ¿Cuál es la meta de Sofía?', 'Mejorar su gestión de proyectos en 12 semanas', 'Mejorar su danza en general durante todo el año', 'Ser mejor que las otras personas del curso en danza', 'La ficha dice mejorar la gestión de proyectos en 12 semanas.'),
        ('abc', '{F} ¿Qué condición SMART cumple «en 12 semanas»?', 'Tiene plazo', 'Es medible', 'Es específica', 'Las 12 semanas son el plazo.'),
        ('=', '{F} ¿Cuántos minutos por semana dedican A1 y A2 juntas?', '60+30', 'A1 dura 1 hora (60 minutos) y A2 30 minutos.', ' minutos'),
        ('=', '{F} Sofía tiene 3 horas por semana. ¿Cuántos minutos son?', '3*60', 'Una hora tiene 60 minutos.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos le quedan libres cada semana después de A1 y A2?', '3*60-(60+30)', 'Se restan de los minutos disponibles los que usan A1 y A2.', ' minutos'),
        ('abc', '{F} ¿Cuál es un indicador de la ficha?', 'Tener un cronograma con 5 tareas hacia atrás', 'Sentirse más segura que otras personas del curso', 'Ser elegida para dirigir el proyecto del curso', 'El indicador debe ser observable y medible.'),
        ('abc', '{F} ¿Cuál de las acciones requiere consentimiento de otra persona?', 'A3, la entrevista', 'A1, el cronograma', 'A4, el descanso', 'La entrevista exige el consentimiento de la persona entrevistada.'),
        ('abc', '{F} Una persona propone que Sofía agregue 5 horas de ensayo físico a la semana para «avanzar más rápido». ¿Qué corresponde?', 'Revisar que el plan sea alcanzable y deje descanso', 'Aceptarlo, porque más horas siempre es mejor para avanzar', 'Aceptarlo y reducir las horas de sueño y de descanso', 'Un plan debe ser realista y cuidar el descanso.'),
        ('abc', 'Dos estudiantes discuten: uno dice que una meta ambiciosa pero imposible motiva más; la otra, que una meta alcanzable y medible es más útil. ¿Quién argumenta mejor?', 'La otra, porque una meta alcanzable permite comprobar el progreso', 'El primero, porque lo imposible exige más esfuerzo a todas las personas', 'Ninguno, porque las metas no sirven para planificar nada', 'Una meta alcanzable y medible permite verificar el avance.'),
        ('abc', '{F} Sofía siente mucho cansancio y tristeza que no pasan durante varias semanas. ¿Qué corresponde en su plan?', 'Reducir la carga y avisar a una persona adulta de confianza', 'Continuar con el plan completo para no perder el ritmo', 'Ocultarlo para no preocupar a las personas de su casa', 'El bienestar va primero y se avisa a una persona adulta de confianza.'),
        ('abc', '{F} Un compañero propone que cada persona del curso compare su progreso con el de las demás en un ranking. ¿Qué corresponde?', 'Rechazarlo: el plan es personal y no se compara con otras personas', 'Aceptarlo, porque ayuda a competir y a esforzarse más', 'Aceptarlo solo con los resultados de las demás personas del curso', 'El desarrollo personal no se mide comparando personas.'),
        ('abc', 'Una estudiante quiere incluir en su plan una dieta muy estricta para «mejorar su rendimiento». ¿Qué corresponde responder?', 'Consultar a una persona adulta y a un profesional de la salud antes de cambiar su alimentación', 'Aplicarla de inmediato, porque lo dice una publicación que leyó en línea', 'Aplicarla en secreto para no recibir críticas de las demás personas', 'Los cambios de alimentación se consultan con profesionales de la salud y personas adultas de confianza.'),
    ],
    ctx=('abc', 'Un estudiante quiere «aprender sobre producción técnica» y escribe su meta. ¿Cuál reescritura cumple mejor con el criterio SMART?', 'En 8 semanas, entrevistar a una persona de producción técnica y escribir un plano de luz y sonido', 'Aprender mucho sobre producción técnica algún día, cuando haya tiempo', 'Ser el mejor de mi curso en producción técnica y ganar un premio', 'La primera tiene plazo, es específica, medible y alcanzable.'),
    sc=[
        ("En creación en danza: ¿cuáles son las condiciones de una meta SMART?", "Específica, medible, alcanzable, relevante y con plazo", "Estas cinco condiciones hacen útil una meta."),
        ("¿Qué se verifica al armar las acciones de un plan?", "Que quepan en el tiempo disponible y dejen descanso", "Un plan debe ser realista para poder cumplirse."),
        ("¿Qué se hace ante cansancio fuerte o tristeza persistente?", "Se reduce la carga y se avisa a una persona adulta de confianza", "El bienestar va primero que cualquier meta del plan."),
    ],
    op=("Elabora un plan de desarrollo personal de 8 semanas para una meta propia relacionada con lo aprendido en esta asignatura (por ejemplo, gestión, composición, análisis o mediación). Escribe: la meta SMART, tres acciones con tiempo semanal, el tiempo total disponible por semana y la verificación de que caben, dos indicadores, una acción de cuidado del cuerpo o del bienestar y a quién avisarías si el plan te sobrecarga. No compares tu progreso con el de otras personas ni uses cifras de empleo.",
        "Meta: en 8 semanas, escribir y ensayar una presentación de 5 minutos para un proyecto de danza del curso. Acciones: A1, escribir el guion (45 minutos por semana); A2, ensayar ante una persona de confianza (30 minutos por semana); A3, entrevistar con consentimiento a una persona que presente proyectos (1 hora en total). Tiempo disponible: 2 horas por semana (120 minutos); A1 + A2 = 75 minutos, caben. Indicadores: guion de 5 tareas ordenadas y presentación en 5 minutos. Cuidado: descanso de un día completo. Si me sobrecarga, aviso a una persona adulta de confianza.",
        ["la meta cumple las condiciones SMART", "el cálculo de tiempo es correcto y deja descanso", "incluye cuidado del bienestar y no compara con otras personas"],
        ["hoja con meta, acciones, cálculo de tiempo, indicadores y cuidado"],
        ["metas vagas", "plan que no cabe en el tiempo", "compararse con otras personas"],
        "Pregunta: «¿cómo sabrás que lo lograste?». Si responde «me sentiré mejor», pídele un indicador observable."),
    reinforce="Reescribe tres metas vagas como «mejorar», «ser mejor» o «aprender más» convirtiéndolas en metas SMART con plazo.",
    extend="Explica por qué un plan de desarrollo personal debe incluir descanso y cuidado del bienestar y cómo ajustarías el tuyo si aparece cansancio.",
)
