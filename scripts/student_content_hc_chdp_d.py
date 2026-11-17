"""Comprensión histórica del presente (electivo HC, 3.º y 4.º medio): OAC-04 (iniciativas de mejoramiento social con fundamentos históricos), clases 1 a 4, y OAC-05 (historia local, relatos de la comunidad y espacios de memoria), clases 1 a 4. Casos, fuentes y datos ficticios o de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada caso, tabla o ficha está escrito en el enunciado. "
             "Todo es ficticio o de ejemplo (la comuna «Lomas del Sur» y el barrio «Los Aromos» no existen). Las posturas se presentan con sus razones y sin tomar partido. "
             "Si trabajas con relatos reales de tu comunidad, pide siempre permiso, cuida la privacidad y trata los temas dolorosos con sobriedad; si algo te afecta, conversa con una persona adulta de confianza. "
             "La historia de los pueblos originarios la cuentan sus comunidades y los educadores y educadoras tradicionales.")
build = make_build(MATERIALS)

O4 = "HI-CHDP-3y4-OAC-04"
O5 = "HI-CHDP-3y4-OAC-05"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (caso de ejemplo, ficticio). Problema: en el barrio Los Aromos de Lomas del Sur faltan lugares de encuentro entre jóvenes y personas mayores. "
     "Antecedentes: la sede vecinal se construyó hace treinta años para reuniones de dirigentes; hace quince años se cerró un club de adultos mayores por falta de monitores; hace cinco años un grupo de estudiantes pidió un espacio para ensayar música, pero la sede estaba ocupada. "
     "Criterios de una sociedad democrática e inclusiva: participación de todas las personas afectadas, respeto de sus derechos, no discriminación y deliberación con razones.")
build(
    O4, 1, F,
    use="Aprenderé a hacer un diagnóstico histórico de un problema social, a distinguir antecedentes, síntomas y causas, y a usar criterios de una sociedad democrática e inclusiva para empezar a pensar una iniciativa de mejoramiento.",
    prior=["Sé formular preguntas e hipótesis históricas.", "Distingo causas y consecuencias.", "Conozco los ejes del cambio reciente: sociedad civil, derechos, desigualdad e inclusión."],
    explain=[
        "Una iniciativa es una propuesta de acción para mejorar una situación de la sociedad, como un taller, un programa o una campaña. Para que sea realista necesita un diagnóstico: entender cuál es el problema, a quiénes afecta y de dónde viene. Un síntoma es lo que se ve del problema (faltan lugares de encuentro). Una causa es lo que ayuda a explicarlo (la sede se pensó solo para dirigentes). Una iniciativa que atiende solo síntomas suele repetir los mismos problemas.",
        "Los antecedentes históricos son hechos y experiencias anteriores que explican cómo se llegó a la situación y que aportan lecciones. Los fundamentos son las razones que justifican la iniciativa: pueden ser históricas (lo que ya se intentó), de derechos (quién tiene derecho a participar) y de datos. Una propuesta con fundamentos puede ser discutida con razones y no solo defendida por intuición.",
        "En una sociedad democrática e inclusiva, las iniciativas se diseñan con quienes serán afectados, respetan sus derechos, evitan discriminar y se deciden deliberando con razones. Eso significa preguntarse quiénes podrían quedar fuera por su edad, su condición física, su horario de trabajo u otra circunstancia, y cómo evitarlo desde el inicio.",
    ],
    vocab=[("iniciativa", "propuesta de acción para mejorar una situación social"), ("diagnóstico", "análisis del problema, de a quiénes afecta y de sus causas"), ("síntoma", "lo que se ve del problema"), ("causa", "factor que ayuda a explicar el problema"), ("antecedente histórico", "hecho o experiencia anterior que explica cómo se llegó a la situación"), ("fundamento", "razón que justifica una iniciativa")],
    worked=[
        ("Distinguir síntoma y causa", "Problema de ejemplo: «Pocos jóvenes asisten a la junta de vecinos.» Se dice que los jóvenes no se interesan, pero las reuniones son a las 15:00 y el aviso se pega solo en la sede. ¿Qué es síntoma y qué es causa posible?",
         ["El síntoma es la baja asistencia de jóvenes.", "Las causas posibles son un horario poco accesible y un aviso que no los alcanza."],
         "Síntoma: poca asistencia; causas: horario y aviso poco accesibles"),
        ("Revisar una propuesta con los criterios", "Propuesta de ejemplo: «La directiva decidirá sola cómo usar el patio comunitario.» Evalúa con los criterios de una sociedad democrática e inclusiva.",
         ["No hay participación de las personas afectadas ni deliberación.", "Podría excluir a quienes usan el patio y no están en la directiva."],
         "No cumple: falta participación y deliberación"),
    ],
    mistakes=[("Proponer una solución sin diagnosticar las causas.", "Se actúa sobre lo que se ve sin preguntar de dónde viene.", "Separa síntomas y causas con ayuda de los antecedentes."),
              ("Diseñar la iniciativa «para» las personas sin consultarlas.", "Se supone que se sabe lo que necesitan.", "Incluye en el diseño a quienes serán afectados y registra sus razones.")],
    T=[
        ("abc", "{F} ¿Cuál es el problema que plantea la ficha?", "Faltan lugares de encuentro entre jóvenes y personas mayores", "Sobran sedes vecinales", "Los estudiantes no quieren estudiar música", "Es el problema declarado al inicio de la ficha."),
        ("abc", "{F} ¿Para qué se construyó la sede vecinal?", "Para reuniones de dirigentes", "Para ensayos de música", "Para el club de adultos mayores", "La ficha dice que se construyó pensando en reuniones de dirigentes."),
        ("abc", "{F} ¿Por qué se cerró el club de adultos mayores?", "Por falta de monitores", "Por falta de socios", "Porque la sede se vendió", "El antecedente indica la falta de monitores como motivo."),
        ("abc", "En Comprensión histórica, ¿qué es una iniciativa?", "Una propuesta de acción para mejorar una situación social", "Una fuente primaria", "Una ley nacional", "Es una propuesta concreta de acción para mejorar algo."),
        ("abc", "En Comprensión histórica, ¿qué es un antecedente histórico?", "Un hecho o experiencia anterior que explica cómo se llegó a la situación", "Una opinión sobre el futuro", "Una cifra cualquiera", "Aporta contexto y lecciones para entender el problema."),
        ("abc", "{F} ¿Qué antecedente muestra que los jóvenes ya habían pedido un espacio?", "La petición de los estudiantes hace cinco años para ensayar música", "El cierre del club de adultos mayores", "La construcción de la sede hace treinta años", "Es el único hecho que muestra una petición de estudiantes."),
        ("abc", "{F} ¿Cuál de estas afirmaciones es una causa y no un síntoma?", "La sede se pensó solo para reuniones de dirigentes", "Jóvenes y personas mayores casi no conversan", "El barrio se siente silencioso", "La primera ayuda a explicar el problema, mientras las otras describen lo que se ve."),
        ("abc", "{F} ¿Quiénes deben participar en el diseño de la iniciativa según los criterios?", "Las personas afectadas: jóvenes, personas mayores y otras que usen la sede", "Solo la directiva de la junta de vecinos", "Solo personas expertas externas", "Participar implica incluir a quienes serán afectados."),
        ("abc", "{F} Una propuesta dice: «El taller será los martes a las 10:00 y solo se avisará a quienes pertenecen a la junta.» ¿Qué criterio incumple?", "La no discriminación y la participación de las personas afectadas", "El respeto del medio ambiente", "La precisión de las fechas", "El horario y el aviso dejan fuera a quienes trabajan o no pertenecen a la junta."),
        ("abc", "{F} ¿Cuál propuesta cumple mejor con los criterios?", "Un taller abierto en la sede, con horarios acordados con jóvenes y personas mayores", "Un taller solo para dirigentes de la junta", "Un taller con horario fijo elegido por una persona", "Incluye a ambos grupos y decide con ellos."),
        ("abc", "{F} ¿Cómo podría la iniciativa usar el antecedente del club cerrado por falta de monitores?", "Incluyendo la formación de un equipo de monitores para no depender de pocas personas", "Ignorando el antecedente", "Proponiendo cerrar la sede", "Una lección del pasado permite anticipar un riesgo."),
        ("abc", "¿Qué diferencia una iniciativa democrática de una impuesta?", "Se decide deliberando con razones junto a las personas afectadas", "Se aprueba con rapidez sin escuchar", "Se mantiene en secreto hasta su inicio", "La deliberación y la participación caracterizan a una iniciativa democrática."),
        ("abc", "Para no discriminar, ¿qué medida es adecuada al planificar un taller en una sede?", "Verificar que haya acceso para personas con movilidad reducida y horarios variados", "Realizarlo en un solo horario fijo para simplificar", "Invitar solo a quienes ya participan", "Evitar la discriminación exige pensar quiénes podrían quedar fuera."),
    ],
    ctx=("abc", "Un centro de estudiantes ficticio quiere crear un espacio de estudio en el liceo. Antes de decidir, una estudiante propone revisar por qué la antigua sala de estudio se cerró, quiénes la usaban y a quiénes no les servía. ¿Qué paso del diagnóstico sigue?", "Reunir antecedentes y testimonios de quienes usaban y no usaban la sala", "Construir el espacio sin más información", "Elegir el diseño más barato", "Un buen diagnóstico se apoya en antecedentes y en las voces de las personas afectadas."),
    sc=[
        ("En Comprensión histórica: ¿qué diferencia hay entre un síntoma y una causa?", "El síntoma es lo que se ve del problema y la causa ayuda a explicarlo", "Atender solo el síntoma suele dejar el problema de fondo."),
        ("¿Qué aportan los antecedentes históricos a una iniciativa?", "Contexto y lecciones de experiencias anteriores", "Permiten no repetir errores pasados y anticipar riesgos conocidos."),
        ("¿Cuáles son cuatro criterios de una sociedad democrática e inclusiva para diseñar una iniciativa?", "Participación, respeto de derechos, no discriminación y deliberación", "Guían quiénes participan y cómo se decide."),
    ],
    op=("Elige un problema de ejemplo. Problema 1: en el liceo hay pocos espacios de descanso para estudiantes con distintas necesidades. Problema 2: en la comuna las personas migrantes tienen dificultades para informarse de los servicios públicos. "
        "Escribe un diagnóstico con un síntoma, dos causas posibles, dos antecedentes (inventa dos, rotulados de ejemplo), a quiénes afecta y qué personas podrían quedar fuera de una primera idea de solución, usando los cuatro criterios de una sociedad democrática e inclusiva.",
        "Problema 2. Síntoma: las personas migrantes no usan los servicios. Causas: la información está solo en un idioma y se publica en lugares poco visibles. Antecedentes: hace cinco años se hizo un folleto, pero se imprimieron pocos. Afecta a migrantes y a funcionarios. Podrían quedar fuera quienes no leen. Participación: consultarlos.",
        ["distingue síntoma y causas", "propone antecedentes plausibles y rotulados", "identifica a quiénes afecta y quiénes podrían quedar fuera", "aplica los cuatro criterios"],
        ["diagnóstico escrito con síntoma, causas, antecedentes, personas afectadas y criterios"],
        ["confundir síntoma con causa", "presentar los antecedentes inventados como hechos reales", "no pensar en quiénes quedan fuera"],
        "Pregunta: «¿a quién consultaste para escribir ese diagnóstico?». Si a nadie, propón entrevistar a las personas afectadas."),
    reinforce="Con el caso de la ficha, escribe una causa posible adicional del problema y un antecedente que la sustente.",
    extend="Elige una iniciativa que conozcas en tu liceo o barrio y escribe qué diagnóstico y qué antecedentes habrían ayudado a diseñarla mejor.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (datos de ejemplo, ficticios). Para fundamentar una iniciativa en el barrio Los Aromos, un grupo aplicó una encuesta voluntaria a 120 personas (60 jóvenes y 60 personas mayores). "
     "Resultados: 84 personas dijeron que les gustaría un espacio de encuentro entre generaciones; 36 dijeron que no. De las 60 personas mayores, 21 señalaron que su principal problema para asistir sería el transporte. "
     "Registro del club cerrado: llegó a tener 40 socios. Situación de partida: hoy hay 0 actividades intergeneracionales. Meta propuesta: 8 actividades en un semestre, con al menos 30 asistencias en total.")
build(
    O4, 2, F,
    use="Aprenderé a fundamentar una iniciativa con fuentes e indicadores: situación de partida (línea base), meta medible e indicadores de seguimiento, reconociendo los límites de una encuesta y del registro histórico.",
    prior=["Sé hacer un diagnóstico con antecedentes.", "Sé leer un indicador con sus límites.", "Sé distinguir fuentes primarias y secundarias."],
    explain=[
        "Fundamentar una iniciativa significa respaldarla con evidencia: antecedentes históricos, datos y testimonios. Una encuesta aporta datos sobre opiniones o necesidades de una cantidad de personas. Un registro histórico, como la lista de socios de un club, muestra que algo existió y tuvo interés en el pasado. Ambos sirven, pero tienen límites: una encuesta voluntaria no representa a todo el barrio, y un registro antiguo no asegura que hoy haya el mismo interés.",
        "La línea base es la situación de partida medida antes de la iniciativa: por ejemplo, hoy hay cero actividades. La meta es el resultado que se quiere lograr y debe ser medible y plazo definido. Un indicador de seguimiento es un dato que se registra durante la iniciativa para saber si avanza hacia la meta, como el número de actividades realizadas o de asistencias por sesión.",
        "Con línea base, meta e indicadores se puede evaluar sin depender de impresiones. Se compara el resultado con la meta, se revisan las causas de las diferencias y se ajusta la iniciativa. Lo importante es no concluir más de lo que los datos permiten: «84 de 120 personas encuestadas» no es «todo el barrio».",
    ],
    vocab=[("encuesta", "recolección de respuestas de un grupo de personas a las mismas preguntas"), ("muestra", "grupo de personas cuyas respuestas se analizan"), ("línea base", "situación de partida medida antes de la iniciativa"), ("meta", "resultado medible que se quiere lograr en un plazo"), ("indicador de seguimiento", "dato que se registra para saber si se avanza hacia la meta"), ("asistencia", "presencia de una persona en una actividad")],
    worked=[
        ("Línea base, meta e indicador", "Iniciativa de ejemplo: un club de lectura en un liceo. Hoy hay 0 sesiones; se quiere lograr 6 sesiones en el semestre. ¿Cuál es la línea base, la meta y un indicador?",
         ["La línea base es 0 sesiones.", "La meta es 6 sesiones en el semestre y un indicador es el número de sesiones realizadas."],
         "Línea base: 0 sesiones; meta: 6 sesiones; indicador: sesiones realizadas"),
        ("Límite de una muestra", "Una encuesta de ejemplo se respondió solo por quienes asistían a la junta de vecinos. ¿Qué límite tiene?",
         ["Las personas que no asisten a la junta no pudieron opinar.", "Los resultados no representan a todo el barrio."],
         "No representa a quienes no asisten a la junta"),
    ],
    mistakes=[("Decir que una encuesta voluntaria refleja la opinión de todo el barrio.", "Se confunde una muestra con el total.", "Indica cuántas personas respondieron y quiénes pudieron haber quedado fuera."),
              ("Plantear una meta como «mejorar la convivencia», sin cifra ni plazo.", "No se define cómo saber si se cumplió.", "Define cuánto, en qué plazo y con qué indicador.")],
    T=[
        ("abc", "{F} ¿Cuántas personas respondieron la encuesta?", "120", "60", "84", "La ficha indica 120 personas, 60 jóvenes y 60 mayores."),
        ("=", "{F} De las 60 personas mayores, ¿cuántas no señalaron el transporte como principal problema?", "60-21", "Se resta a las 60 personas mayores las 21 que mencionaron el transporte."),
        ("abc", "En Comprensión histórica, ¿qué es la línea base de una iniciativa?", "La situación de partida medida antes de la iniciativa", "El resultado final esperado", "El presupuesto total", "Se mide al inicio para poder comparar después."),
        ("abc", "{F} ¿Cuál es la línea base de la ficha?", "0 actividades intergeneracionales hoy", "8 actividades en un semestre", "120 personas encuestadas", "La situación de partida es la que existe hoy, sin actividades."),
        ("abc", "{F} ¿Cuál es la meta propuesta?", "8 actividades en un semestre con al menos 30 asistencias en total", "40 socios en el club", "84 personas a favor", "La ficha la define con cifra y plazo."),
        ("abc", "{F} ¿Qué indicador de seguimiento corresponde a la meta?", "Número de actividades realizadas y de asistencias registradas", "Cantidad de sillas de la sede", "Número de integrantes de la directiva", "Mide directamente lo que la meta plantea."),
        ("abc", "{F} ¿Qué aporta el registro de 40 socios del club cerrado?", "Un antecedente de que hubo interés en el pasado", "Una prueba de que hoy todos quieren participar", "La línea base de la nueva iniciativa", "Muestra interés pasado, pero no prueba el interés actual."),
        ("abc", "{F} ¿Cuál es un límite de la encuesta?", "Fue voluntaria y respondieron solo 120 personas, por lo que no representa a todo el barrio", "Fue demasiado larga", "Preguntó por el transporte", "Una muestra voluntaria puede dejar fuera a quienes no respondieron."),
        ("abc", "{F} ¿Qué conclusión está justificada por la encuesta?", "Una mayoría de las personas encuestadas, 84 de 120, desea un espacio de encuentro", "Todo el barrio quiere el espacio", "Nadie tiene problemas de transporte", "La conclusión se limita a las personas que respondieron."),
        ("abc", "{F} ¿Cuál de estas afirmaciones NO está justificada por los datos?", "El 100 % del barrio apoya la iniciativa", "21 personas mayores señalaron el transporte", "Hubo 36 respuestas que no desean el espacio", "Los datos no permiten hablar de todo el barrio."),
        ("=", "{F} Si cada una de las 8 actividades tuviera 5 asistencias, ¿cuántas asistencias habría en total?", "8*5", "Se multiplican las actividades por las asistencias de cada una."),
        ("abc", "{F} Con 8 actividades de 5 asistencias cada una, ¿se cumple la meta de al menos 30 asistencias?", "Sí, porque el total es 40 asistencias", "No, porque 5 es menor que 8", "No se puede saber sin otra encuesta", "El total de 40 es mayor que el mínimo de 30."),
        ("abc", "¿Por qué una meta debe ser medible y tener plazo?", "Para poder saber con evidencia si se cumplió", "Para que nadie pueda evaluarla", "Para que sea más difícil de lograr", "Sin cifra ni plazo no hay forma de comprobar el avance."),
    ],
    ctx=("abc", "Un grupo de estudiantes ficticio quiere crear un taller de reciclaje en el liceo. Escriben la meta «que todo el liceo recicle más». Su profesor les sugiere cambiarla. ¿Cuál es una mejor meta?", "Realizar 10 jornadas de reciclaje en el semestre con al menos 100 asistencias en total", "Que el liceo sea más ecológico", "Que los estudiantes se comprometan", "La meta mejor definida incluye cantidad, plazo y un indicador."),
    sc=[
        ("En Comprensión histórica: ¿qué es un indicador de seguimiento?", "Un dato que se registra durante la iniciativa para saber si avanza hacia la meta", "Permite evaluar con evidencia y ajustar."),
        ("¿Por qué una encuesta voluntaria no representa a todo el barrio?", "Porque solo responden quienes quieren y pueden hacerlo", "Quienes no respondieron pueden pensar distinto."),
        ("¿Qué aporta un registro histórico como la lista de socios de un club?", "Un antecedente de que existió una actividad y su alcance", "No asegura el mismo interés hoy."),
    ],
    op=("Elige una iniciativa de ejemplo. Iniciativa 1: un taller de apoyo escolar entre estudiantes de cursos distintos. Iniciativa 2: un huerto comunitario en una plaza. "
        "Escribe una línea base, una meta con cifra y plazo, dos indicadores de seguimiento, un dato que usarías para fundamentarla (inventa uno, rotulado de ejemplo) y un límite de ese dato.",
        "Iniciativa 2. Línea base: 0 huertas en la plaza. Meta: 4 camas de cultivo en 6 meses con 20 asistencias en jornadas de trabajo. Indicadores: camas construidas y asistencias registradas. Dato de ejemplo: 30 vecinos dijeron en una encuesta que participarían. Límite: no representa a todos los vecinos.",
        ["define una línea base coherente", "formula una meta con cifra y plazo", "propone dos indicadores medibles", "señala un dato de fundamento y su límite"],
        ["ficha con línea base, meta, indicadores, dato y límite"],
        ["dar una meta sin cifra", "usar indicadores que no miden la meta", "olvidar el límite del dato"],
        "Pregunta: «¿cómo sabrías en seis meses si lo lograste?». Si no puede responder, la meta es difusa."),
    reinforce="Con la ficha, escribe una segunda meta distinta de la propuesta y su indicador de seguimiento.",
    extend="Explica cómo cambiarías la encuesta de la ficha para que representara mejor a todo el barrio.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (experiencias y alternativas de ejemplo, ficticias). Experiencia pasada 1: el club de adultos mayores funcionó seis años, pero dependía de una sola persona voluntaria y cerró cuando ella se fue. "
     "Experiencia pasada 2: el taller de música de estudiantes tuvo buena asistencia, pero se hacía solo en horario de clases y las personas mayores no pudieron ir. "
     "Alternativas para la nueva iniciativa: A) taller semanal de oficios y música en la sede, con un equipo de 6 monitores voluntarios, en horario de tarde; B) plataforma digital para conversar; C) feria de un día al año. "
     "Puntuación de ejemplo, de 1 a 3 (3 es lo mejor). Participación: A 3, B 1, C 2. Accesibilidad: A 3, B 1, C 2. Sostenibilidad en el tiempo: A 2, B 2, C 1. Costo bajo: A 2, B 1, C 3.")
build(
    O4, 3, F,
    use="Aprenderé a sacar lecciones de experiencias históricas anteriores y a comparar alternativas de iniciativa con criterios explícitos, reconociendo los límites de una matriz de puntajes.",
    prior=["Sé hacer un diagnóstico con antecedentes.", "Sé fundamentar una iniciativa con datos.", "Sé comparar perspectivas."],
    explain=[
        "Las experiencias anteriores sirven como lecciones: qué funcionó, qué no y por qué. Una lección histórica no es una receta, sino un aprendizaje que se aplica con cuidado porque el contexto cambia. Por ejemplo, si un club cerró por depender de una sola persona, la lección es que una iniciativa debe repartir responsabilidades, no que hay que evitar los clubes.",
        "Para comparar alternativas se usan criterios, que son los aspectos que importan para decidir, como participación, accesibilidad, sostenibilidad y costo. Una matriz de puntajes asigna un valor a cada alternativa en cada criterio y permite sumar. Es una ayuda para ordenar la discusión, no una verdad: los criterios y los puntajes son juicios que deben conversarse con las personas afectadas.",
        "El resultado de una matriz cambia si cambia el peso de los criterios. Si el costo bajo se considera más importante, una alternativa barata puede subir de lugar. Por eso conviene revisar qué pasa si se modifican los pesos y explicar la decisión con razones, no solo con la suma final.",
    ],
    vocab=[("lección histórica", "aprendizaje que se saca de una experiencia anterior"), ("criterio", "aspecto que se usa para comparar alternativas"), ("matriz de puntajes", "tabla que asigna un valor a cada alternativa en cada criterio"), ("sostenibilidad", "capacidad de mantenerse en el tiempo"), ("accesibilidad", "posibilidad de que cualquier persona pueda participar"), ("peso de un criterio", "importancia relativa que se le da en la decisión")],
    worked=[
        ("Sacar una lección", "Experiencia de ejemplo: una feria de libros fracasó porque se anunció solo por redes sociales y muchas personas mayores no la conocieron. ¿Qué lección se obtiene?",
         ["El problema fue el canal de difusión, que excluyó a un grupo.", "La lección es usar varios canales, incluidos carteles y avisos presenciales."],
         "Difundir por varios canales para no dejar a nadie fuera"),
        ("Sumar una matriz", "Alternativa de ejemplo X: participación 2, accesibilidad 3, costo bajo 1. Alternativa Y: participación 3, accesibilidad 1, costo bajo 3. ¿Cuál suma más?",
         ["X suma 2 más 3 más 1, es decir, 6.", "Y suma 3 más 1 más 3, es decir, 7."],
         "Y suma 7 y X suma 6"),
    ],
    mistakes=[("Elegir la alternativa con la suma más alta sin revisar los criterios ni los puntajes.", "Se cree que el número reemplaza la discusión.", "Examina qué criterios pesan más y qué ocurriría si cambian."),
              ("Aplicar una lección del pasado como si el contexto fuera idéntico.", "Se olvida que el contexto cambia.", "Adapta la lección y explica en qué se parecen las situaciones.")],
    T=[
        ("abc", "{F} ¿Por qué cerró el club de adultos mayores?", "Porque dependía de una sola persona voluntaria", "Porque tenía pocos socios", "Porque se mudó la sede", "La experiencia 1 dice que cerró cuando esa persona se fue."),
        ("abc", "{F} ¿Qué limitó al taller de música de estudiantes?", "Que se hacía solo en horario de clases", "Que no tenía asistentes", "Que costaba mucho", "Las personas mayores no pudieron asistir por el horario."),
        ("abc", "En Comprensión histórica, ¿qué es una lección histórica?", "Un aprendizaje que se saca de una experiencia anterior", "Una clase de historia", "Un tipo de fuente", "Se obtiene al analizar qué funcionó y qué no."),
        ("abc", "{F} ¿Qué lección se obtiene de la experiencia 1?", "Repartir las responsabilidades en un equipo para no depender de una sola persona", "Evitar los clubes", "No trabajar con voluntarios", "La causa del cierre fue la dependencia de una persona."),
        ("abc", "{F} ¿Qué lección se obtiene de la experiencia 2?", "Fijar horarios en que puedan asistir todos los grupos", "Hacer actividades solo para estudiantes", "Evitar los talleres de música", "El horario excluyó a las personas mayores."),
        ("=", "{F} ¿Cuál es el puntaje total de la alternativa A?", "3+3+2+2", "Se suman sus cuatro puntajes: participación, accesibilidad, sostenibilidad y costo."),
        ("=", "{F} ¿Cuál es el puntaje total de la alternativa B?", "1+1+2+1", "Se suman sus puntajes en los cuatro criterios."),
        ("=", "{F} ¿Cuál es el puntaje total de la alternativa C?", "2+2+1+3", "Se suman sus puntajes en los cuatro criterios."),
        ("abc", "{F} ¿Qué alternativa obtiene el mayor puntaje total?", "La A, con 10 puntos", "La B, con 5 puntos", "La C, con 8 puntos", "La A suma 10, más que las demás."),
        ("abc", "{F} ¿Cómo responde la alternativa A a la lección de la experiencia 1?", "Con un equipo de 6 monitores voluntarios, no depende de una sola persona", "Con una plataforma digital", "Con una feria de un solo día", "El equipo de monitores reparte las responsabilidades."),
        ("abc", "{F} ¿Qué debilidad mantiene la alternativa A según los puntajes?", "Su sostenibilidad en el tiempo solo recibe 2 puntos y su costo bajo, 2", "No recibe ninguna puntuación", "Su participación es la más baja", "Su puntaje de sostenibilidad no es el máximo, por lo que hay que cuidarla."),
        ("abc", "{F} Si el costo bajo se contara dos veces (el doble), ¿qué alternativa tendría más puntos?", "La A, con 12 puntos frente a 11 de la C", "La C, con 14 puntos", "La B, con 6 puntos", "A suma 10 más 2 y C suma 8 más 3, y A sigue arriba."),
        ("abc", "¿Por qué no basta con mirar el puntaje total para decidir?", "Porque los criterios y puntajes son juicios que deben discutirse con las personas afectadas", "Porque los números nunca sirven", "Porque la suma siempre está mal hecha", "La matriz ayuda a ordenar la discusión pero no la reemplaza."),
    ],
    ctx=("abc", "Un liceo ficticio compara dos formas de tener un huerto escolar: una a cargo de un solo profesor y otra a cargo de un equipo de profesores y apoderados. Hace un tiempo, el huerto a cargo de un solo profesor se abandonó cuando él cambió de colegio. ¿Qué lección conviene aplicar?", "Elegir la opción con un equipo para que no dependa de una sola persona", "Elegir la opción más barata", "No hacer ningún huerto", "La experiencia anterior muestra el riesgo de depender de una sola persona."),
    sc=[
        ("En Comprensión histórica: ¿qué es un criterio de decisión?", "Un aspecto que se usa para comparar alternativas", "Por ejemplo, la participación o el costo."),
        ("¿Qué muestra que una matriz de puntajes es solo una ayuda?", "Que los criterios y puntajes son juicios y el resultado cambia si cambian los pesos", "Debe discutirse con las personas afectadas."),
        ("¿Por qué una lección histórica no es una receta?", "Porque el contexto cambia y la lección debe adaptarse", "Se aplica comparando las situaciones y adaptando lo aprendido."),
    ],
    op=("Compara tres alternativas de ejemplo para mejorar la convivencia en un liceo: A) un consejo de curso mensual con una mediadora; B) un buzón anónimo de sugerencias; C) una jornada anual de convivencia. "
        "Escribe una experiencia pasada de ejemplo y su lección, elige cuatro criterios (incluye la participación y la accesibilidad), asigna puntajes de 1 a 3 con una razón breve, suma y justifica cuál elegirías, y qué pasaría si un criterio pesara más.",
        "Experiencia: un buzón anónimo se llenó de bromas y no se usó. Lección: pedir razones y dar respuesta. Criterios: participación, accesibilidad, sostenibilidad y costo. A: 3, 3, 2, 2 = 10; B: 2, 3, 1, 3 = 9; C: 2, 2, 1, 2 = 7. Elijo A. Si el costo pesara más, B se acerca.",
        ["presenta una experiencia y una lección", "usa cuatro criterios con puntajes razonados", "suma correctamente", "revisa cómo cambia el resultado si se modifica un peso"],
        ["matriz con criterios, puntajes y razones, y una justificación"],
        ["puntuar sin razones", "sumar mal", "no revisar cambios de peso"],
        "Pregunta: «¿cambia tu decisión si el criterio más importante fuera otro?»."),
    reinforce="Con la ficha 3, calcula el total de cada alternativa si la sostenibilidad se contara dos veces y compara con el resultado original.",
    extend="Explica cómo incluirías las opiniones de las personas afectadas para asignar los puntajes de una matriz.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (plan de ejemplo, ficticio). Iniciativa: «Taller intergeneracional» en la sede de Los Aromos. Plan: 8 sesiones en un semestre, una por semana; se espera que asistan 15 personas por sesión (8 jóvenes y 7 personas mayores); un equipo de 6 monitores voluntarios. "
     "Consecuencias esperadas: más conversación entre generaciones y más participación en la junta de vecinos. Posibles consecuencias no esperadas: que las sesiones no puedan atender a personas con movilidad reducida, que se desgasten los monitores o que otros grupos se sientan excluidos. "
     "Seguimiento: registrar la asistencia de cada sesión y, al final, preguntar a las personas asistentes qué cambiarían.")
build(
    O4, 4, F,
    use="Aprenderé a prever las consecuencias esperadas y no esperadas de una iniciativa, a identificar quiénes podrían quedar fuera y a diseñar un seguimiento y una evaluación abiertos, con fundamentos históricos y de derechos.",
    prior=["Sé diagnosticar un problema con antecedentes.", "Sé fijar línea base, meta e indicadores.", "Sé comparar alternativas con criterios."],
    explain=[
        "Toda iniciativa tiene consecuencias. Las esperadas son las que se buscan, como más conversación entre generaciones. Las no esperadas aparecen cuando la iniciativa interactúa con la realidad: pueden ser positivas, como que los asistentes inicien otras actividades, o negativas, como que algunas personas queden fuera. Anticiparlas desde la experiencia histórica ayuda a prevenirlas. Si un taller anterior tuvo problemas de acceso, esa lección permite revisar desde ahora el lugar y el horario.",
        "Una iniciativa democrática e inclusiva se evalúa con quienes participan. El seguimiento registra datos, como la asistencia por sesión, y la evaluación final pregunta qué funcionó, qué no y qué cambiarían. Si los resultados no alcanzan la meta, se revisan las causas con las personas antes de abandonar la iniciativa o buscar culpables, y se hacen ajustes.",
        "Los fundamentos de una iniciativa pueden ser históricos, de derechos y de datos. Una iniciativa que busca que todas las personas del barrio puedan participar se apoya en el derecho a la participación y en la lección de experiencias anteriores. Informar a la comunidad lo que se logró y lo que no es una forma de rendir cuentas y de mantener la confianza.",
    ],
    vocab=[("consecuencia esperada", "efecto que se busca con la iniciativa"), ("consecuencia no esperada", "efecto que no se buscaba y aparece al aplicarla"), ("seguimiento", "registro de datos durante la iniciativa"), ("evaluación", "análisis de lo logrado y lo pendiente, con las personas participantes"), ("rendir cuentas", "informar a la comunidad lo que se hizo y lo que se logró"), ("ajuste", "cambio en la iniciativa a partir de la evaluación")],
    worked=[
        ("Anticipar una consecuencia no esperada", "Iniciativa de ejemplo: una biblioteca abierta solo de 9:00 a 13:00 en un barrio donde muchas personas trabajan en ese horario. ¿Qué consecuencia no esperada es posible?",
         ["El horario coincide con la jornada laboral de muchas personas.", "Podrían quedar fuera quienes trabajan, aunque la iniciativa buscaba abrirse a todas."],
         "Que queden fuera las personas que trabajan en ese horario"),
        ("Ajustar tras el seguimiento", "El taller de ejemplo esperaba 15 asistentes por sesión, pero asistieron 6. Un grupo propone culpar a la gente. ¿Qué es más adecuado?",
         ["Se revisan con las personas posibles causas, como el horario o la difusión.", "Se ajusta la iniciativa y se vuelve a medir la asistencia."],
         "Revisar causas con las personas y ajustar la iniciativa"),
    ],
    mistakes=[("Evaluar solo si se cumplió la meta, sin preguntar a las personas participantes.", "Se confunde cumplir la cifra con lograr el objetivo.", "Combina datos de asistencia con la voz de quienes participaron."),
              ("Ocultar los resultados que no fueron buenos.", "Se teme perder apoyo de la comunidad.", "Informa lo logrado y lo pendiente: la confianza se construye con transparencia.")],
    T=[
        ("=", "{F} ¿Cuántas asistencias en total se esperan en las 8 sesiones?", "8*15", "Se multiplican las 8 sesiones por las 15 personas esperadas en cada una."),
        ("abc", "{F} ¿Cuántas personas mayores se esperan por sesión?", "7", "8", "15", "El plan indica 7 personas mayores y 8 jóvenes."),
        ("=", "{F} Si en una sesión están los 6 monitores y las 15 personas asistentes esperadas, ¿cuántas personas hay en total?", "6+15", "Se suman los monitores y las personas asistentes."),
        ("abc", "En Comprensión histórica, ¿qué es una consecuencia no esperada?", "Un efecto que no se buscaba y aparece al aplicar la iniciativa", "El objetivo principal de la iniciativa", "Un dato de la línea base", "No formaba parte de lo que se buscaba."),
        ("abc", "{F} ¿Cuál es una consecuencia esperada de la iniciativa?", "Más conversación entre generaciones", "Que se desgasten los monitores", "Que algunas personas queden excluidas", "El plan la nombra como lo que se busca."),
        ("abc", "{F} ¿Cuál es una consecuencia no esperada que menciona el plan?", "Que las sesiones no puedan atender a personas con movilidad reducida", "Más participación en la junta de vecinos", "Que asistan 15 personas", "El plan la menciona como una posibilidad no buscada."),
        ("abc", "{F} ¿Qué medida previene la exclusión de personas con movilidad reducida?", "Verificar el acceso a la sede y, si no existe, buscar otro lugar o habilitarlo", "Ignorar el problema", "Cambiar el nombre del taller", "Prevenir exige actuar sobre el acceso físico antes de comenzar."),
        ("abc", "{F} Para saber si el horario incluye a quienes trabajan en la tarde, ¿qué dato falta?", "Los horarios de trabajo de las personas del barrio", "El nombre de los monitores", "El número de sillas", "Sin ese dato no se puede evaluar quién queda fuera."),
        ("abc", "{F} ¿Qué indicador mide mejor «más participación en la junta de vecinos»?", "Cuántas personas asistentes al taller asisten luego a reuniones de la junta", "Cuántas sesiones tuvo el taller", "Cuántos monitores hay", "Mide directamente la relación entre el taller y la junta."),
        ("abc", "{F} ¿Para qué sirve preguntar al final qué cambiarían las personas asistentes?", "Para evaluar con participación y mejorar la iniciativa", "Para elegir un culpable", "Para evitar que haya otra iniciativa", "Incorporar su voz es parte de una evaluación democrática."),
        ("abc", "{F} Si asisten 9 personas por sesión y no 15, ¿qué conviene hacer primero?", "Revisar con las personas las causas, como el horario o la difusión, y ajustar", "Cerrar el taller de inmediato", "Culpar a los monitores", "Antes de decidir hay que entender qué impide asistir."),
        ("abc", "¿Qué fundamento de derechos apoya una iniciativa para que todas las personas puedan participar?", "El derecho a participar en la vida de la comunidad sin discriminación", "El derecho a no ser consultado", "El derecho a decidir solo", "Participación y no discriminación son principios de una sociedad inclusiva."),
        ("abc", "¿Cómo rinde cuentas una iniciativa a la comunidad?", "Informando lo logrado y lo pendiente, con datos y testimonios", "Mostrando solo los éxitos", "Sin comunicar nada", "La transparencia con logros y pendientes mantiene la confianza."),
    ],
    ctx=("abc", "Un centro de estudiantes ficticio hizo un taller de debate. Se esperaban 30 participantes y asistieron 12, casi todos de tercero medio. En la evaluación, estudiantes de primero dijeron que no sabían del taller. ¿Qué ajuste es más pertinente?", "Mejorar la difusión en todos los niveles y volver a medir la asistencia", "Culpar a los estudiantes de primero", "Cancelar el taller", "El problema parece ser la difusión, y el ajuste busca incluir a todos los niveles."),
    sc=[
        ("En Comprensión histórica: ¿qué es una consecuencia esperada?", "El efecto que se busca con la iniciativa", "Se define al diseñar la meta."),
        ("¿Por qué conviene evaluar con las personas participantes?", "Porque aportan información que los datos no muestran y la evaluación es democrática", "Su voz completa los números de asistencia."),
        ("¿Qué se hace si no se alcanza la meta?", "Se revisan las causas con las personas y se ajusta la iniciativa", "No se busca culpables ni se oculta el resultado."),
    ],
    op=("Elige una iniciativa de ejemplo. Iniciativa 1: un taller de lengua de señas chilena para personas del liceo, guiado por una persona sorda de la comunidad. Iniciativa 2: un programa de acompañamiento a estudiantes recién llegados al liceo desde otras comunas. "
        "Escribe dos consecuencias esperadas, dos no esperadas (una positiva y una negativa), quiénes podrían quedar fuera y cómo lo evitarías, un indicador de seguimiento, una pregunta para la evaluación final con participantes y cómo informarías a la comunidad.",
        "Iniciativa 2. Esperadas: más amistades y mejor adaptación. No esperadas: positiva, estudiantes antiguos aprenden de otras comunas; negativa, quienes llegan tarde en el año no se integran. Quedar fuera: quienes llegan a mitad de año; ofrecer inscripción abierta. Indicador: acompañamientos activos. Pregunta: ¿qué cambiarías? Informe: panel en el liceo.",
        ["distingue consecuencias esperadas y no esperadas", "identifica personas que podrían quedar fuera y una medida", "propone un indicador y una pregunta de evaluación", "plantea cómo rendir cuentas"],
        ["ficha con consecuencias, exclusiones, indicador, pregunta y rendición de cuentas"],
        ["no pensar en quién queda fuera", "confundir un efecto esperado con uno no esperado", "evaluar sin consultar a las personas participantes"],
        "Pregunta: «¿a quién consultarías antes de comenzar y después de terminar?»."),
    reinforce="Con la ficha 4, escribe una tercera consecuencia no esperada posible y una medida para prevenirla.",
    extend="Explica por qué rendir cuentas a la comunidad fortalece una iniciativa y qué dificultades podría tener.",
)

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (lugares de ejemplo, ficticios). En Lomas del Sur: Lugar 1, una plaza con un árbol plantado por vecinos hace treinta años para celebrar la llegada del agua potable al barrio. "
     "Lugar 2, un sitio sin uso donde, según los vecinos, nunca ocurrió nada especial. Lugar 3, una placa en el muro de la sede vecinal que recuerda a las familias fundadoras del barrio. "
     "Lugar 4, una tienda de ropa de una cadena nacional abierta hace dos años.")
build(
    O5, 1, F,
    use="Aprenderé qué es la historia local y un espacio de memoria, quiénes son los actores de una comunidad y cómo trabajar con relatos y fuentes propias con permiso, respeto y cuidado.",
    prior=["Sé quiénes son sujetos históricos.", "Sé interrogar fuentes de la historia reciente.", "Sé que algunos temas requieren un trato sobrio."],
    explain=[
        "La historia local estudia el pasado de una comunidad cercana, como un barrio, una comuna o un liceo, con las fuentes que ella misma conserva: fotografías familiares, cartas, objetos, actas de organizaciones y relatos de vecinas y vecinos. No es una historia menor: muestra cómo los procesos nacionales se vivieron en un lugar concreto y cómo la gente de ese lugar los transformó.",
        "Un espacio de memoria es un lugar, objeto o práctica donde una comunidad recuerda hechos importantes de su pasado y los transmite a otras personas, como una plaza, una placa, un mural o una ceremonia. Puede recordar logros, esfuerzos colectivos o hechos dolorosos. Su valor no depende de que sea oficial, sino de que la comunidad lo reconozca como parte de su historia.",
        "Trabajar con relatos de personas exige ética. Se pide permiso antes de grabar, anotar o fotografiar, se explica para qué se usará, se respeta la decisión de no responder y se cuida la privacidad. Los temas dolorosos se tratan con sobriedad, sin detalles gráficos, y si algo afecta a alguien se conversa con una persona adulta de confianza. La historia de los pueblos originarios no se escribe en su nombre: la cuentan sus comunidades y los educadores y educadoras tradicionales.",
    ],
    vocab=[("historia local", "estudio del pasado de una comunidad cercana con sus propias fuentes"), ("espacio de memoria", "lugar, objeto o práctica donde una comunidad recuerda hechos importantes y los transmite"), ("relato de la comunidad", "recuerdo contado por una persona o grupo de un lugar"), ("fuente de la comunidad", "documento, foto u objeto que conserva una comunidad"), ("consentimiento", "permiso libre e informado de una persona para usar su testimonio"), ("privacidad", "derecho a decidir qué datos personales se comparten")],
    worked=[
        ("Reconocer un espacio de memoria", "En un barrio de ejemplo hay un mural pintado por estudiantes y vecinas para recordar a las mujeres que organizaron una olla común. ¿Es un espacio de memoria?",
         ["Es un lugar que recuerda un esfuerzo colectivo de la comunidad.", "Transmite ese recuerdo a otras personas del barrio."],
         "Sí: recuerda un esfuerzo colectivo y lo transmite"),
        ("Aplicar el consentimiento", "Una estudiante de ejemplo quiere usar la foto familiar de un vecino en una exposición. ¿Qué debe hacer?",
         ["Pedir permiso al vecino y explicarle para qué se usará.", "Respetar su respuesta y no publicar si no acepta."],
         "Pedir permiso, explicar el uso y respetar la respuesta"),
    ],
    mistakes=[("Creer que solo es historia lo que ocurrió en grandes ciudades o con autoridades.", "Se asocia la historia con lo nacional.", "La historia local muestra cómo las comunidades vivieron y transformaron los procesos."),
              ("Usar relatos o fotos de vecinos sin preguntarles.", "Se piensa que los recuerdos del barrio son de todos.", "Pide siempre permiso y explica el uso.")],
    T=[
        ("abc", "{F} ¿Cuál de los lugares es un espacio de memoria?", "El lugar 1, la plaza con el árbol", "El lugar 2, el sitio sin uso", "El lugar 4, la tienda de ropa", "El árbol recuerda un logro colectivo de la comunidad."),
        ("abc", "{F} ¿Qué recuerda la placa del lugar 3?", "A las familias fundadoras del barrio", "La llegada del agua potable", "La apertura de una tienda", "La ficha dice que la placa recuerda a las familias fundadoras."),
        ("abc", "En Comprensión histórica, ¿qué es la historia local?", "El estudio del pasado de una comunidad cercana con sus propias fuentes", "El estudio de la historia de todo el mundo", "La lista de alcaldes de un país", "Se centra en la comunidad cercana y en lo que ella conserva."),
        ("abc", "En Comprensión histórica, ¿qué es un espacio de memoria?", "Un lugar, objeto o práctica donde una comunidad recuerda hechos importantes y los transmite", "Una bodega de archivos oficiales", "Un lugar que solo puede ser creado por el gobierno", "Lo que lo define es que la comunidad lo reconoce y transmite su recuerdo."),
        ("abc", "{F} ¿Qué hecho celebra el árbol del lugar 1?", "La llegada del agua potable al barrio", "La fundación del barrio", "La apertura de una tienda", "La ficha lo indica en la descripción del lugar."),
        ("abc", "{F} ¿Quiénes plantaron el árbol según la ficha?", "Vecinos del barrio", "Una empresa nacional", "Un ministerio", "Fueron los vecinos, es decir, la propia comunidad."),
        ("abc", "¿Cuál de estas es una fuente propia de la comunidad?", "Una carta guardada por una familia del barrio", "Un catálogo de ropa", "Un mapa del sistema solar", "Una carta familiar es un documento que conserva la comunidad."),
        ("abc", "Antes de grabar en audio el relato de una vecina para un trabajo del curso, lo adecuado es", "Pedirle permiso y explicarle para qué se usará", "Grabarla sin avisar para que hable con naturalidad", "Grabar y pedir permiso al terminar", "El consentimiento es previo y debe ser informado."),
        ("abc", "Una vecina, al recordar un hecho doloroso, prefiere no seguir hablando. ¿Qué corresponde?", "Respetar su decisión y no insistir", "Pedirle que continúe porque es importante", "Escribir igual lo que se imagina", "La persona decide qué contar, y el trato debe ser sobrio y respetuoso."),
        ("abc", "{F} Un compañero dice: «El árbol no es histórico porque lo plantaron vecinos y no autoridades.» ¿Qué error comete?", "Cree que solo es histórico lo que hacen las autoridades", "Confunde el árbol con una placa", "Usa mal las fechas", "Los esfuerzos de la comunidad también son historia local."),
        ("abc", "Un grupo quiere contar la historia de un pueblo originario de la zona usando solo libros. ¿Qué conviene hacer?", "Invitar a su comunidad y a educadores o educadoras tradicionales a contarla", "Escribirla en su nombre", "Omitirla", "Su historia la cuentan sus propias comunidades."),
        ("abc", "{F} Para iniciar una iniciativa de historia local en Lomas del Sur, ¿cuál es un primer paso adecuado?", "Conversar con la comunidad y definir con su permiso qué lugar y qué relatos recoger", "Imprimir carteles sin consultar", "Elegir el lugar 4 porque es el más nuevo", "Una iniciativa local parte del diálogo y el permiso de la comunidad."),
        ("abc", "¿Qué diferencia a la historia local de la nacional?", "Estudia una comunidad cercana y sus fuentes propias", "Estudia solo temas del pasado lejano", "No usa fuentes", "Su escala de estudio es la comunidad cercana."),
    ],
    ctx=("abc", "En el liceo, un grupo quiere hacer una exposición sobre la historia del barrio. Una estudiante lleva fotos de su abuelo y otras de la junta de vecinos. ¿Qué paso conviene primero?", "Pedir permiso a las personas que aparecen y a quienes son dueñas de las fotos", "Pegar las fotos en la pared", "Cambiar los nombres para que nadie se dé cuenta", "El permiso y la información sobre el uso son el primer paso ético."),
    sc=[
        ("En Comprensión histórica: ¿qué es un espacio de memoria?", "Un lugar, objeto o práctica donde la comunidad recuerda hechos importantes", "Lo reconoce la comunidad, aunque no sea oficial."),
        ("¿Qué se debe hacer antes de grabar o anotar el relato de una persona?", "Pedir su permiso y explicar para qué se usará", "Es lo que se llama consentimiento informado de la persona."),
        ("¿Quién cuenta la historia de un pueblo originario?", "Su propia comunidad, con el apoyo de educadores y educadoras tradicionales", "No se escribe en su nombre."),
    ],
    op=("Elige un lugar de ejemplo de tu barrio o de esta lista: una plaza, una sede vecinal, una cancha, un mural o una escuela antigua. Escribe: qué hecho o esfuerzo podría recordar, quiénes serían los actores de la comunidad, dos fuentes propias que podrías buscar (por ejemplo, una foto o un acta), "
        "a quiénes pedirías permiso antes de usar un relato o una imagen y qué cuidado tendrías si el recuerdo fuera doloroso para alguien.",
        "Lugar: una cancha de barrio. Recuerda el esfuerzo de vecinos que la construyeron. Actores: vecinos y un club. Fuentes: fotos y acta del club. Permiso: a quienes aparecen y al club. Cuidado: no insistir en recuerdos dolorosos y respetar si alguien prefiere no hablar.",
        ["identifica un lugar y el hecho que recuerda", "señala actores y dos fuentes de la comunidad", "indica a quiénes pediría permiso", "plantea un cuidado ante recuerdos dolorosos"],
        ["ficha breve con lugar, hecho, actores, fuentes, permisos y cuidados"],
        ["omitir el consentimiento", "elegir fuentes que no son de la comunidad", "no pensar en el trato de temas dolorosos"],
        "Pregunta: «¿qué persona tendría que autorizar el uso de esa foto?»."),
    reinforce="Con los lugares de la ficha, escribe cuál no sería un espacio de memoria y por qué.",
    extend="Conversa con una persona adulta de tu casa sobre un lugar del barrio que recuerde algo importante y anota qué recuerda ella.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (guion de entrevista de ejemplo). Se prepara una entrevista a doña Marta (personaje ficticio), vecina de 78 años, sobre la plaza del barrio. Preguntas del guion: "
     "1) «¿Cómo era la plaza cuando usted era joven?» 2) «¿No es cierto que la plaza era mejor antes?» 3) «¿Se acuerda de alguna fiesta en la plaza? ¿Cómo fue?» 4) «¿Tiene fotos?» 5) «Cuénteme qué le gustaría que los jóvenes supieran de la plaza.» "
     "Protocolo: pedir permiso para grabar o anotar, explicar para qué se usará, anotar fecha y lugar, y dejar que la persona decida no responder.")
build(
    O5, 2, F,
    use="Aprenderé a preparar y realizar una entrevista de historia oral con preguntas abiertas y consentimiento, y a registrar y cuidar fuentes de la comunidad, para recoger relatos sin inducir respuestas.",
    prior=["Sé qué es un espacio de memoria.", "Sé interrogar fuentes orales y sus límites.", "Conozco el consentimiento y la privacidad."],
    explain=[
        "La historia oral recoge el testimonio de personas mediante entrevistas. Una entrevista se prepara con un guion de preguntas. Las preguntas abiertas invitan a describir y narrar («¿cómo era?», «¿qué recuerda?»). Las preguntas cerradas se responden con sí o no y aportan poco. Las preguntas inductivas ya traen la respuesta («¿no es cierto que antes era mejor?») y condicionan lo que la persona dirá, por lo que deben evitarse.",
        "Antes de comenzar se explica quién entrevista, para qué y cómo se usará el relato, se pide permiso para grabar o anotar y se aclara que la persona puede no responder o detenerse. Se registra la fecha, el lugar, el nombre de quien entrevista y, con permiso, el nombre de la persona. Se escucha con respeto y se evita interrumpir o corregir.",
        "Un testimonio es una fuente valiosa, pero depende de la memoria. Por eso se contrasta con otras fuentes, como fotos, actas o relatos de otras personas, y se entrevista a personas de distintas edades y experiencias. Las fuentes de la comunidad que se reciben prestadas, como álbumes o cartas, se tratan con cuidado y se devuelven.",
    ],
    vocab=[("historia oral", "reconstrucción del pasado a partir de testimonios hablados"), ("guion de entrevista", "lista de preguntas preparadas antes de entrevistar"), ("pregunta abierta", "pregunta que invita a describir o narrar"), ("pregunta cerrada", "pregunta que se responde con sí o no"), ("pregunta inductiva", "pregunta que sugiere la respuesta esperada"), ("registro", "anotación de fecha, lugar y datos de la entrevista")],
    worked=[
        ("Clasificar preguntas", "Guion de ejemplo: (a) «¿Qué recuerda de la fiesta del barrio?» (b) «¿Fue una fiesta?» (c) «¿No le parece que la fiesta era muy bonita?» Clasifica cada una.",
         ["(a) invita a narrar: es abierta.", "(b) se responde con sí o no: es cerrada; (c) sugiere que era bonita: es inductiva."],
         "(a) abierta; (b) cerrada; (c) inductiva"),
        ("Reescribir una pregunta inductiva", "Pregunta de ejemplo: «¿No es verdad que la escuela estaba mejor antes?» Reescríbela como abierta y neutral.",
         ["Se quita la sugerencia de que estaba mejor.", "Se pide describir cambios: ¿qué diferencias recuerda en la escuela con el paso del tiempo?"],
         "¿Qué diferencias recuerda en la escuela con el paso del tiempo?"),
    ],
    mistakes=[("Hacer preguntas que ya traen la respuesta.", "Se quiere confirmar lo que ya se piensa.", "Reformula en forma abierta y neutral."),
              ("Interrumpir para corregir los datos del relato.", "Se confunde entrevistar con comprobar.", "Escucha primero y contrasta después con otras fuentes.")],
    T=[
        ("abc", "{F} ¿Cuál de las preguntas es inductiva?", "La pregunta 2: «¿No es cierto que la plaza era mejor antes?»", "La pregunta 1", "La pregunta 3", "La pregunta 2 sugiere la respuesta que se espera."),
        ("abc", "{F} ¿Cuál pregunta se responde con sí o no?", "La pregunta 4: «¿Tiene fotos?»", "La pregunta 1", "La pregunta 5", "Pide solo una afirmación o negación, por eso es cerrada."),
        ("abc", "{F} ¿Cuál pregunta pide el recuerdo de un episodio concreto?", "La pregunta 3, sobre una fiesta en la plaza", "La pregunta 2", "La pregunta 4", "Pide recordar y describir una fiesta determinada."),
        ("abc", "En Comprensión histórica, ¿qué es una pregunta abierta?", "Una pregunta que invita a describir o narrar", "Una pregunta que se responde con sí o no", "Una pregunta que sugiere la respuesta", "Las preguntas abiertas permiten narrar con libertad."),
        ("abc", "{F} Antes de grabar a doña Marta, ¿qué corresponde?", "Pedir su permiso y explicarle para qué se usará", "Grabar sin avisar para que sea más natural", "Preguntar solo a sus familiares", "El consentimiento informado es previo a la grabación."),
        ("abc", "{F} Si doña Marta no quiere responder la pregunta 5, ¿qué se hace?", "Se respeta su decisión y se continúa", "Se insiste hasta que responda", "Se inventa su respuesta", "El protocolo permite que ella decida no responder."),
        ("abc", "{F} ¿Qué datos conviene anotar en el registro de la entrevista?", "Fecha, lugar y quién entrevistó", "Solo el nombre de la plaza", "Solo la opinión de quien entrevista", "Son datos básicos para identificar la fuente."),
        ("abc", "{F} ¿Cuál es una mejor versión de la pregunta 4 para recoger más información?", "¿Qué fotos conserva de la plaza y qué recuerda de cada una?", "¿Tiene fotos o no tiene?", "¿Verdad que tiene muchas fotos antiguas?", "Es abierta, neutral y pide describir y narrar."),
        ("=", "{F} ¿Cuántas preguntas del guion no son ni inductivas ni cerradas?", "5-1-1", "Se resta del total de 5 la inductiva (pregunta 2) y la cerrada (pregunta 4)."),
        ("abc", "Un álbum familiar prestado para la exposición de ejemplo debe", "Cuidarse y devolverse a su dueña o dueño", "Quedarse en el liceo", "Ser modificado para que se vea mejor", "Las fuentes prestadas pertenecen a quien las conserva."),
        ("abc", "Al ver una fotografía antigua de la plaza, ¿qué pregunta ayuda a interrogarla?", "¿Quién la tomó, cuándo y dónde, y qué deja fuera el encuadre?", "¿De qué color es el marco?", "¿Cuántas personas la compraron?", "Esas preguntas permiten ubicar y evaluar la fuente."),
        ("abc", "¿Por qué conviene entrevistar a personas de distintas edades sobre un mismo lugar?", "Porque sus recuerdos y puntos de vista pueden complementarse o diferir", "Porque todas contarán lo mismo", "Para terminar más rápido", "Distintas generaciones vivieron el lugar de maneras diferentes."),
        ("abc", "Un relato de la entrevista dice que la fiesta fue en una fecha que parece incorrecta. ¿Qué conviene hacer?", "Contrastar con otras fuentes, como actas o fotos, sin interrumpir a la persona", "Corregirla durante la entrevista", "Descartar todo el relato", "Se escucha primero y se verifica después con otras fuentes."),
    ],
    ctx=("abc", "Un grupo ficticio entrevistará al presidente del club deportivo del barrio. Un integrante propone empezar con «¿No cree que el club fue siempre muy unido?». Otro propone «¿Cómo recuerda la relación entre los socios en los primeros años?». ¿Cuál conviene y por qué?", "La segunda, porque es abierta y neutral", "La primera, porque es más breve", "Ninguna, porque no se deben hacer preguntas", "La segunda permite narrar sin sugerir la respuesta."),
    sc=[
        ("En Comprensión histórica: ¿qué es una pregunta inductiva?", "Una pregunta que sugiere la respuesta esperada", "Condiciona lo que dirá la persona."),
        ("¿Qué se debe explicar a la persona antes de la entrevista?", "Quién entrevista, para qué y cómo se usará el relato", "Esa explicación es parte del consentimiento informado de la persona."),
        ("¿Por qué se contrasta un testimonio con otras fuentes?", "Porque la memoria puede olvidar, exagerar o reordenar", "Otras fuentes ayudan a comprobar o complementar el relato."),
    ],
    op=("Prepara un guion de entrevista de ejemplo (a una persona ficticia, no a una real) sobre un espacio de tu barrio, como una plaza, una cancha o una sede. Escribe seis preguntas: tres abiertas, una cerrada útil y dos que reescribas desde una inductiva. "
        "Agrega el texto breve que dirías al comenzar (quién eres, para qué es la entrevista, permiso y posibilidad de no responder) y la lista de datos que registrarías.",
        "Guion sobre una cancha. Abiertas: ¿cómo era la cancha cuando era niño?, ¿qué partidos recuerda?, ¿qué cambió con los años? Cerrada: ¿participó en su construcción? Reescritas: de «¿no es cierto que antes había más gente?» a «¿cómo era la asistencia de gente a los partidos?». Inicio: me llamo..., hago un trabajo de historia local... Registro: fecha, lugar, quién entrevista.",
        ["incluye tres preguntas abiertas y una cerrada pertinente", "reescribe dos preguntas inductivas", "redacta un inicio con permiso y posibilidad de no responder", "lista los datos del registro"],
        ["guion de seis preguntas, texto de inicio y lista de datos de registro"],
        ["dejar preguntas que sugieren la respuesta", "olvidar el permiso", "no incluir un registro"],
        "Pregunta: «¿qué pregunta de tu guion puede responderse solo con sí o no?»."),
    reinforce="Reescribe las preguntas 2 y 4 del guion de la ficha como preguntas abiertas y neutrales.",
    extend="Explica qué fuentes usarías para comprobar el recuerdo de una persona sobre una fiesta de hace cuarenta años.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (relatos y fuentes de ejemplo, ficticios). Dos relatos sobre el árbol de la plaza de Lomas del Sur. Relato de don Lalo: «El árbol lo plantamos todos los vecinos el día en que llegó el agua; yo cargué el agua para regarlo.» "
     "Relato de doña Inés: «El árbol lo plantó la junta de vecinos con ayuda de un vivero; ese día repartieron pan y hubo discursos.» "
     "Fuentes de apoyo: una foto sin fecha de vecinos alrededor de un arbolito; un acta de la junta de vecinos (año de ejemplo: 1995) con el acuerdo «plantar un árbol en la plaza»; una carta del vivero (año de ejemplo: 1995) que agradece el encargo de un árbol.")
build(
    O5, 3, F,
    use="Aprenderé a comparar relatos distintos sobre un mismo lugar, a distinguir memoria e historia y a contrastar los relatos con otras fuentes de la comunidad, para construir una versión prudente.",
    prior=["Sé entrevistar con preguntas abiertas.", "Sé contrastar fuentes de distinto tipo.", "Sé que la memoria es selectiva."],
    explain=[
        "La memoria es el recuerdo vivo que una persona o comunidad conserva del pasado. Está cargada de emociones, selecciona lo que importa y cambia con el tiempo. La historia, como disciplina, reconstruye el pasado con método: pregunta, reúne fuentes, las contrasta y explica sus límites. La memoria es una fuente valiosa para la historia, y la historia ayuda a revisar la memoria, sin que una reemplace a la otra.",
        "Cuando dos relatos sobre un mismo lugar difieren, no siempre se contradicen: pueden destacar aspectos distintos, como quién organizó, quién participó o qué se sintió. Primero se identifican los puntos de coincidencia, luego las diferencias y, por último, se buscan otras fuentes que ayuden a decidir, como actas, cartas o fotos con fecha.",
        "Cada fuente tiene un alcance. Una foto sin fecha muestra que algo ocurrió, pero no cuándo. Un acta registra un acuerdo, pero no dice si se cumplió. Una carta muestra un vínculo entre dos actores. Combinando varias, se puede construir una versión prudente que diga lo que se sabe, lo que se supone y lo que falta averiguar.",
    ],
    vocab=[("memoria", "recuerdo vivo de una persona o comunidad, con emociones y selección"), ("historia", "reconstrucción del pasado con método, fuentes y contraste"), ("versión prudente", "relato que distingue lo que se sabe, lo que se supone y lo que falta averiguar"), ("coincidencia", "punto en que dos relatos o fuentes están de acuerdo"), ("complementarse", "completarse aportando partes distintas"), ("alcance de una fuente", "aquello que una fuente permite afirmar")],
    worked=[
        ("Coincidencias y diferencias", "Relato A de ejemplo: «La feria comenzó en un patio y la organizaron los comerciantes.» Relato B: «La feria comenzó en un patio con ayuda de la junta de vecinos.» ¿Qué coincide y qué difiere?",
         ["Coinciden en que comenzó en un patio.", "Difieren en quién la organizó: los comerciantes o la junta con ayuda."],
         "Coinciden en el lugar; difieren en quién la organizó"),
        ("Alcance de una fuente", "Un acta de ejemplo dice: «Se acuerda instalar un letrero en la plaza.» ¿Qué permite afirmar y qué no?",
         ["Permite afirmar que hubo un acuerdo de instalarlo.", "No permite afirmar que el letrero se instaló ni cuándo."],
         "Que hubo un acuerdo; no que se cumplió"),
    ],
    mistakes=[("Pensar que si dos relatos difieren, uno miente.", "Se confunde diferencia de perspectiva con falsedad.", "Busca qué aspecto destaca cada relato y qué fuente ayuda a decidir."),
              ("Descartar un recuerdo porque no es exacto.", "Se cree que solo vale lo comprobable.", "La memoria muestra cómo la comunidad vivió y valora su pasado, y se contrasta.")],
    T=[
        ("abc", "{F} ¿Quién plantó el árbol según don Lalo?", "Todos los vecinos", "La junta de vecinos con un vivero", "Una empresa", "Don Lalo dice «lo plantamos todos los vecinos»."),
        ("abc", "{F} ¿Qué agrega doña Inés a la versión de don Lalo?", "Que la junta de vecinos lo hizo con ayuda de un vivero", "Que nadie plantó el árbol", "Que el árbol llegó solo", "Menciona a la junta y a un vivero."),
        ("abc", "{F} ¿En qué coinciden los dos relatos?", "En que la comunidad participó en plantar el árbol", "En quién organizó la plantación", "En el año de la plantación", "Ambos hablan de personas del barrio presentes en la plantación."),
        ("abc", "{F} ¿En qué difieren principalmente?", "En quién organizó: todos los vecinos o la junta con un vivero", "En el nombre de la plaza", "En el tipo de árbol", "Un relato enfatiza a la comunidad y el otro, a la junta."),
        ("abc", "En Comprensión histórica, ¿qué es la memoria?", "El recuerdo vivo de una persona o comunidad, con emociones y selección", "Una fuente oficial sin errores", "Un método para ordenar archivos", "La memoria incluye emociones, selecciona y cambia."),
        ("abc", "En Comprensión histórica, ¿qué es la historia como disciplina?", "La reconstrucción del pasado con método, fuentes y contraste", "El recuerdo personal de un testigo", "Una lista de fechas", "Se distingue de la memoria por el método y el contraste."),
        ("abc", "{F} ¿Se contradicen necesariamente los dos relatos?", "No: pueden complementarse, pues la junta organizó y los vecinos participaron", "Sí: uno de los dos miente", "Sí, porque hablan de años distintos", "Destacan aspectos diferentes que pueden ser compatibles."),
        ("abc", "{F} ¿Qué fuente apoya la versión de doña Inés?", "El acta de la junta y la carta del vivero", "La foto sin fecha", "Ninguna", "Muestran un acuerdo de la junta y un vínculo con un vivero."),
        ("abc", "{F} ¿Por qué es débil la foto como evidencia por sí sola?", "No tiene fecha y no se sabe quiénes aparecen ni cuándo se tomó", "Porque es muy grande", "Porque es en blanco y negro", "Sin fecha ni nombres, su alcance es limitado."),
        ("abc", "{F} ¿Qué afirmación se puede sostener con el acta y la carta?", "Que hubo un acuerdo de plantar un árbol y un encargo a un vivero en el mismo año de ejemplo", "Que don Lalo cargó el agua", "Que asistieron 100 vecinos", "Solo esas dos fuentes apoyan lo del acuerdo y el encargo."),
        ("abc", "{F} ¿Qué pregunta ayudaría a continuar la investigación?", "¿Quiénes participaron el día de la plantación y quién regó el árbol después?", "¿Cuánto cuesta un árbol hoy?", "¿Qué pasó en otro país?", "Se relaciona con los puntos todavía abiertos entre los relatos."),
        ("abc", "{F} ¿Cuál es una versión prudente de lo ocurrido?", "Varias fuentes sugieren que la junta organizó la plantación con un vivero y que vecinos participaron; falta saber cuántos y cuándo exactamente", "Fue solo don Lalo", "Fue solo la junta, y los vecinos no participaron", "Distingue lo que apoyan las fuentes de lo que falta averiguar."),
        ("abc", "¿Por qué la memoria sigue siendo valiosa aunque no sea exacta?", "Porque muestra cómo la comunidad vive y valora su pasado", "Porque reemplaza al método histórico", "Porque no necesita contrastarse", "Aporta experiencia y sentido, y se contrasta con otras fuentes."),
    ],
    ctx=("abc", "Dos vecinas de un barrio ficticio recuerdan de forma distinta cuántas personas asistieron a una fiesta: una dice «muchísimas» y otra «unas pocas». Una estudiante propone buscar fotos con fecha, una lista de invitados y otro testimonio. ¿Cómo califica este plan?", "Adecuado, porque contrasta los relatos con otras fuentes", "Innecesario, porque basta preguntar a una vecina más", "Incorrecto, porque no se puede contrastar una memoria", "Contrastar con fuentes distintas ayuda a ubicar un rango más confiable."),
    sc=[
        ("En Comprensión histórica: ¿qué diferencia hay entre memoria e historia?", "La memoria es recuerdo vivo y selectivo; la historia reconstruye con método y contraste", "Se complementan, pero no son lo mismo."),
        ("¿Por qué una foto sin fecha tiene alcance limitado?", "Porque no se sabe cuándo se tomó ni quiénes aparecen", "Muestra que algo ocurrió, pero no cuándo."),
        ("¿Qué incluye una versión prudente?", "Lo que se sabe, lo que se supone y lo que falta averiguar", "Declara los límites de la evidencia."),
    ],
    op=("Elige un caso de ejemplo. Caso 1: dos relatos sobre quién fundó la cancha del barrio (un exjugador dice que fue el club; una vecina dice que fueron los vecinos). Caso 2: dos relatos sobre cuándo se pintó el mural de la escuela (una exalumna dice que fue en una fiesta de fin de año; un profesor dice que fue en un taller). "
        "Inventa el contenido de los dos relatos (rotulados de ejemplo) y tres fuentes de apoyo (por ejemplo, un acta, una foto y una carta). Escribe coincidencias, diferencias, qué apoya cada fuente y una versión prudente de tres frases.",
        "Caso 2. Coinciden en que el mural lo pintaron personas de la escuela. Difieren en la ocasión. Fuentes: un acta del taller, una foto sin fecha y una carta del director. El acta apoya al profesor. Versión: probablemente se pintó en el taller; la foto no permite fechar; falta saber el año.",
        ["inventa relatos y fuentes coherentes", "identifica coincidencias y diferencias", "asigna cada fuente a un relato con razón", "redacta una versión prudente"],
        ["tabla de relatos y fuentes, y una versión prudente de tres frases"],
        ["declarar a un relato falso sin evidencia", "usar una fuente sin fecha como prueba de una fecha", "omitir lo que falta averiguar"],
        "Pregunta: «¿qué fuente podría contradecir tu versión?»."),
    reinforce="Con la ficha 3, escribe qué fuente adicional te gustaría tener para decidir entre don Lalo y doña Inés.",
    extend="Explica por qué dos relatos distintos de un mismo lugar pueden enriquecer la historia local en vez de debilitarla.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (ficha de espacio de memoria, borrador de ejemplo). Nombre: «El árbol de la plaza». Ubicación: plaza de Lomas del Sur. Qué recuerda: la llegada del agua potable al barrio y la plantación del árbol por la comunidad. "
     "Fuentes: relatos de don Lalo y doña Inés, un acta y una carta (de ejemplo). Falta: autorización de las personas para usar sus nombres y fotos; un texto breve para visitantes; los cuidados del lugar. "
     "Propuesta de recorrido: 4 paradas de 10 minutos cada una, más 15 minutos de apertura y cierre.")
build(
    O5, 4, F,
    use="Aprenderé a relevar un espacio de memoria: elaborar una ficha, escribir un texto breve y respetuoso para visitantes, planificar un recorrido y devolver el trabajo a la comunidad, cuidando consentimiento, privacidad y temas sensibles.",
    prior=["Sé entrevistar y contrastar relatos de la comunidad.", "Sé distinguir memoria e historia.", "Conozco el consentimiento y la privacidad."],
    explain=[
        "Relevar un espacio de memoria es darlo a conocer y cuidarlo. Para ello se elabora una ficha con el nombre, la ubicación, qué recuerda, quiénes lo hicieron o lo cuidan, las fuentes, los permisos obtenidos y los cuidados necesarios. La ficha ordena lo que se sabe y deja visible lo que falta, como autorizaciones o datos por confirmar.",
        "El texto para visitantes debe ser breve, claro y prudente. Dice qué recuerda el lugar, indica en qué fuentes se apoya y evita absolutos como «siempre» o «todos». Evita juicios sobre personas y, si el hecho es doloroso, se escribe con sobriedad, sin detalles gráficos. Cuando un recuerdo afecta a alguien de la comunidad, se conversa con esa persona y con una persona adulta de confianza antes de publicarlo.",
        "Un recorrido planifica paradas, tiempos y actividades: en cada una se presenta un relato, una fuente y una pregunta para quienes visitan. Al terminar, el trabajo se devuelve a la comunidad: se muestra a quienes aportaron relatos, se corrigen errores con ellos y se deja una copia en un lugar accesible. Esta devolución es parte de la ética de la historia local. La historia de los pueblos originarios se incorpora solo con la participación de sus comunidades y de educadores y educadoras tradicionales.",
    ],
    vocab=[("relevar", "dar a conocer y poner en valor algo que la comunidad aprecia"), ("ficha de espacio de memoria", "registro con nombre, ubicación, qué recuerda, fuentes, permisos y cuidados"), ("texto para visitantes", "texto breve que explica un lugar a quienes lo visitan"), ("recorrido", "secuencia de paradas con tiempos y actividades"), ("devolución a la comunidad", "presentar el trabajo a quienes aportaron y corregir con ellos"), ("sobriedad", "trato respetuoso, sin dramatizar ni dar detalles gráficos")],
    worked=[
        ("Detectar lo que falta en una ficha", "Ficha de ejemplo: nombre «El mural del patio», ubicación del liceo y descripción del mural. No tiene permisos, fuentes ni cuidados. ¿Qué falta?",
         ["Faltan las fuentes que sostienen lo que dice.", "Faltan los permisos de las personas y los cuidados del mural."],
         "Fuentes, permisos y cuidados"),
        ("Calcular la duración de un recorrido", "Recorrido de ejemplo: 3 paradas de 8 minutos cada una, más 6 minutos de apertura y cierre. ¿Cuánto dura en total?",
         ["Las paradas suman 3 por 8, es decir, 24 minutos.", "Con 6 minutos de apertura y cierre dan 30 minutos."],
         "30 minutos"),
    ],
    mistakes=[("Publicar nombres y fotos sin avisar a las personas.", "Se piensa que son de dominio público porque están en el barrio.", "Pide autorización y explica dónde se mostrarán."),
              ("Escribir textos con absolutos o juicios sobre personas.", "Se busca un tono emotivo y rotundo.", "Usa frases prudentes, apoyadas en fuentes y sin juicios sobre personas.")],
    T=[
        ("abc", "{F} ¿Cuál es el nombre del espacio de memoria de la ficha?", "El árbol de la plaza", "La placa de la sede", "La tienda de ropa", "Es el nombre indicado en la ficha."),
        ("=", "{F} ¿Cuántos minutos dura en total el recorrido propuesto?", "4*10+15", "Se multiplican las 4 paradas por 10 minutos y se agregan los 15 minutos de apertura y cierre."),
        ("abc", "{F} Antes de publicar los nombres y fotos de las personas, ¿qué hay que obtener?", "Su autorización", "Una nueva foto", "El permiso de un ministerio", "El consentimiento de las personas es previo a publicar."),
        ("abc", "En Comprensión histórica, ¿qué es una devolución a la comunidad?", "Presentar el trabajo a quienes aportaron y corregir con ellos", "Entregar las fotos prestadas para siempre", "Cobrar por la exposición", "Es parte de la ética de la historia local."),
        ("abc", "{F} ¿Cuál es el mejor texto para el cartel del lugar?", "El árbol fue plantado por la comunidad, según relatos y un acta de la junta de vecinos, para recordar la llegada del agua.", "El árbol es la prueba de que todos los vecinos siempre trabajaron unidos.", "Un vecino plantó este árbol solo y nadie lo ayudó.", "La primera opción es breve, indica fuentes y evita absolutos."),
        ("abc", "{F} ¿Qué problema tiene el texto «el árbol es la prueba de que todos los vecinos siempre trabajaron unidos»?", "Usa absolutos y generaliza desde un solo hecho", "Es demasiado breve", "Menciona el agua potable", "«Todos» y «siempre» afirman más de lo que las fuentes permiten."),
        ("abc", "{F} ¿Qué debería hacer cada parada del recorrido?", "Presentar un relato, una fuente y una pregunta para el público", "Mostrar solo un cartel sin conversar", "Repetir el mismo texto cuatro veces", "Así el recorrido combina memoria, evidencia y participación."),
        ("abc", "{F} ¿Qué cuidado sencillo y seguro podría incluir la ficha para proteger el árbol y su entorno?", "Pedir no clavar objetos en el tronco ni dejar basura, y avisar a la junta si se daña", "Cubrir el árbol con carteles clavados", "Cortar sus ramas para fotografiarlo", "Son medidas de cuidado simples y seguras."),
        ("abc", "Para un espacio que recuerda un hecho doloroso, ¿qué texto es más adecuado?", "Uno sobrio, apoyado en fuentes y sin detalles gráficos", "Uno con descripciones detalladas para impresionar", "Uno que culpe a personas sin pruebas", "La sobriedad respeta a las personas afectadas."),
        ("abc", "Una vecina se emociona al recordar un hecho doloroso para una exposición. ¿Qué corresponde?", "Detenerse si ella lo desea, no insistir y apoyarse en una persona adulta de confianza", "Seguir hasta terminar", "Publicar igual su relato", "Se prioriza el bienestar de la persona sobre la exposición."),
        ("abc", "Se quiere incluir la historia de un pueblo originario de la zona en el recorrido. ¿Qué es lo adecuado?", "Invitar a su comunidad y a educadores o educadoras tradicionales a participar y contar su historia", "Escribirla a partir de libros sin consultar", "Representar sus ritos en el recorrido", "No se habla en nombre de un pueblo ni se representan sus ritos."),
        ("Si el recorrido de la ficha empieza a las 16:00 y dura 55 minutos, ¿a qué hora termina?", "A las 16:55", "Se suman 55 minutos a las 16:00.", ),
        ("abc", "{F} ¿Por qué este lugar es relevante para la memoria local?", "Muestra cómo una comunidad recuerda un logro colectivo", "Es el lugar más antiguo del país", "Pertenece a una cadena nacional", "Su valor está en que la comunidad lo reconoce como parte de su historia."),
    ],
    ctx=("abc", "Un curso del liceo ficticio terminó una exposición sobre un mural del barrio. ¿Cuál es una buena forma de devolver el trabajo a la comunidad?", "Presentarla a las personas que aportaron relatos, recoger sus correcciones y dejar una copia en la sede vecinal", "Guardarla en el computador del curso", "Venderla a las personas que aportaron", "La devolución incluye mostrar, corregir con la comunidad y dejar el trabajo accesible."),
    sc=[
        ("En Comprensión histórica: ¿qué datos tiene una ficha de espacio de memoria?", "Nombre, ubicación, qué recuerda, fuentes, permisos y cuidados", "Ordena lo que se sabe y deja ver lo que falta."),
        ("¿Por qué conviene evitar palabras como «siempre» y «todos» en un cartel?", "Porque afirman más de lo que las fuentes permiten", "Un texto prudente se apoya en evidencia."),
        ("¿Qué se hace antes de publicar un recuerdo que afecta a una persona de la comunidad?", "Se conversa con ella y se pide su autorización", "Su bienestar y su decisión son lo primero."),
    ],
    op=("Elige un espacio de ejemplo: una plaza, una sede, un mural o una cancha. Escribe una ficha con nombre, ubicación, qué recuerda, dos fuentes, los permisos que pedirías y los cuidados del lugar. "
        "Luego redacta un cartel de tres frases para visitantes (prudente, sin absolutos, con fuentes), el plan de un recorrido de tres paradas con minutos y la forma en que devolverías el trabajo a la comunidad.",
        "Espacio: el mural de la escuela. Ficha: ubicado en el patio; recuerda un taller de arte; fuentes: acta y foto; permisos: a participantes y a la dirección; cuidados: no tocar la pintura. Cartel: «Este mural fue pintado por estudiantes en un taller, según un acta y una foto.» Recorrido: 3 paradas de 8 minutos y 6 minutos de cierre, 30 minutos. Devolución: mostrarlo a participantes.",
        ["completa todos los elementos de la ficha", "escribe un cartel prudente con fuentes", "planifica un recorrido con tiempos correctos", "describe una devolución a la comunidad"],
        ["ficha, cartel de tres frases, plan de recorrido y devolución"],
        ["omitir permisos", "usar absolutos o juicios sobre personas", "calcular mal los minutos del recorrido"],
        "Pregunta: «¿a quién mostrarías este trabajo antes de publicarlo?»."),
    reinforce="Completa la ficha 4 con el texto breve para visitantes que le falta.",
    extend="Explica qué cambiarías en el recorrido para que una persona con movilidad reducida pueda participar.",
)
