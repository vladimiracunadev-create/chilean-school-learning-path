"""Emprendimiento y Empleabilidad EPJA Media N1 y N2, módulo 2: planificación de proyectos (OAD-05), regulaciones y normativa laboral (OAD-06), presupuesto (OAD-07) y evaluación del plan (OAD-08). Casos ficticios rotulados; cifras de ejemplo; sin tasas, impuestos ni plazos reales (se remite a la norma vigente). Todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma. Todos los casos, cifras y fichas son de ejemplo (personas, negocios y montos ficticios); no se usan tasas, impuestos ni plazos reales, ni calculadora ni internet. Todo se resuelve con lo escrito en la ficha."
build = make_build(MATERIALS)

O5 = "EPJA-EMEM-NM1y2-OAD-05"
O6 = "EPJA-EMEM-NM1y2-OAD-06"
O7 = "EPJA-EMEM-NM1y2-OAD-07"
O8 = "EPJA-EMEM-NM1y2-OAD-08"
PRIOR = ["He organizado alguna tarea con otras personas, en la casa, la comunidad o el trabajo.", "Sé sumar, restar y multiplicar con montos de dinero y con tiempo."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    stmt, example, crit, ev, err, fb = op
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=(stmt, example, crit, ev, err, fb), reinforce=rf, extend=ex_)


# ====================================================== OAD-05 clase 1
F = ("Ficha 1 (proyecto ficticio). Una junta de vecinos ficticia organiza una feria de trueque de ropa en la plaza. Objetivo: que 100 personas intercambien ropa en un sábado. "
     "Tareas: T1 pedir autorización del espacio a la junta. T2 hacer afiches. T3 reunir 10 mesas. T4 realizar la feria. T5 evaluar lo ocurrido y agradecer a quienes ayudaron. "
     "Recursos: 10 mesas, 2 cartulinas por afiche, 6 voluntarios.")
K(O5, 1, F,
  "Hoy aprenderé qué es un proyecto, cuáles son sus etapas y cómo identificar objetivo, actividades, recursos, herramientas y responsables al planificar.",
  ["Un proyecto es un conjunto de actividades con un objetivo claro, un inicio y un final. Una feria de trueque, la renovación de una sede o el lanzamiento de un servicio son proyectos. Tienen cuatro etapas: inicio, donde se define el objetivo; planificación, donde se decide qué, cuándo y con qué; ejecución, donde se hace; y cierre, donde se evalúa y se agradece.",
   "Planificar es responder preguntas simples. ¿Qué queremos lograr? ¿Qué actividades hay que hacer? ¿Quién se encarga de cada una? ¿Qué recursos se necesitan, como dinero, materiales, personas y tiempo? ¿Qué herramientas ayudan, como una lista, un calendario o una planilla? Un objetivo bueno se puede medir: «100 personas intercambian ropa» dice cuánto y cuándo.",
   "Gestionar con responsabilidad significa usar bien el tiempo y los recursos: no gastar más de lo que hay, no prometer lo que no se puede cumplir y avisar a tiempo si algo cambia. Un indicador es un dato que muestra si se está logrando el objetivo, como el número de personas que llegaron. El caso de esta clase es inventado."],
  [("proyecto", "conjunto de actividades con un objetivo, un inicio y un final"), ("planificación", "decidir qué hacer, cuándo, con qué y quién lo hace"), ("recurso", "lo que se necesita: personas, dinero, materiales, tiempo"), ("indicador", "dato que muestra si se logra el objetivo")],
  [("Ubicar una tarea", "«Evaluar lo ocurrido y agradecer a quienes ayudaron». ¿En qué etapa del proyecto va?", ["Es lo que se hace al terminar.", "Corresponde al cierre."], "Cierre"),
   ("Medir el objetivo", "El objetivo es que 100 personas intercambien ropa. Llegaron 80. ¿Cuántas faltaron para el objetivo?", ["Se compara con la meta.", "100 menos 80."], "20 personas")],
  [("Confundir objetivo con actividad.", "Se piensa en lo que se hará sin definir lo que se quiere lograr.", "El objetivo dice qué se logrará; las actividades dicen cómo."),
   ("Planificar sin contar los recursos.", "Se supone que alcanzarán sin revisar.", "Anota cuántos recursos hay y cuántos faltan.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿qué es un proyecto?", "Un conjunto de actividades con un objetivo, un inicio y un final", "Una tarea que no termina nunca", "Un contrato de trabajo", "Un proyecto tiene principio, fin y propósito."),
   ("abc", "{F} ¿Cuál es el objetivo del proyecto de la ficha?", "Que 100 personas intercambien ropa en un sábado", "Reunir 10 mesas", "Hacer afiches", "El objetivo es lo que se quiere lograr; las demás cosas son actividades."),
   ("ab", "Decidir qué se hará, cuándo y con qué recursos corresponde a la etapa de", "planificación", "cierre", "En esa etapa se organiza antes de comenzar a hacer."),
   ("abc", "{F} ¿Qué tarea corresponde a la etapa de ejecución?", "T4, realizar la feria", "T1, pedir autorización", "T5, evaluar y agradecer", "La feria es el momento en que se hace lo planificado."),
   ("abc", "{F} ¿Cuál de estos es un recurso del proyecto?", "Las 10 mesas", "El objetivo", "La etapa de cierre", "Las mesas son un material que el proyecto necesita."),
   ("=", "{F} Si se hace un afiche con 2 cartulinas y se quieren 8 afiches, ¿cuántas cartulinas hacen falta?", "2*8", "Se multiplica lo que usa cada afiche por la cantidad de afiches.", " cartulinas"),
   ("=", "{F} Si llegaron 64 personas a la feria, ¿cuántas faltaron para llegar al objetivo de 100?", "100-64", "Se resta lo logrado a la meta para saber lo que faltó.", " personas"),
   ("abc", "¿Qué indicador muestra si se logró el objetivo de la feria?", "El número de personas que intercambiaron ropa", "El color de los afiches", "El nombre de la plaza", "El indicador debe mostrar el avance hacia el objetivo."),
   ("abc", "Un grupo planifica una actividad que necesita 12 mesas, pero solo tiene 10. ¿Qué es lo más responsable?", "Anotar que faltan 2 y buscar cómo conseguirlas antes del día", "Hacer la feria sin avisar", "Eliminar el objetivo", "Planificar con responsabilidad es prever lo que falta."),
   ("ab", "Alguien dice: «si ya tengo la idea, no necesito planificar». Lo más acertado es decir que", "planificar permite ordenar tiempo, recursos y responsables", "planificar es perder tiempo", "Sin plan es más fácil olvidar recursos y plazos."),
   ("abc", "Un objetivo dice: «hacer una feria bonita». ¿Cuál es su problema?", "No dice cuánto ni cuándo, por lo que no se puede medir", "Es demasiado preciso", "Tiene demasiados números", "Un objetivo medible permite saber si se logró."),
   ("abc", "{F} Hay 6 voluntarios y 5 tareas. ¿Qué conviene hacer con las personas responsables?", "Asignar a cada tarea al menos una persona responsable", "No asignar a nadie para evitar discusiones", "Dejar que todo ocurra sin coordinar", "Quien tiene una tarea asignada sabe qué se espera de ella."),
   ("abc", "Se avisa con una semana de anticipación que la feria se pasa para el sábado siguiente. ¿Qué principio de gestión responsable se cumple?", "Avisar a tiempo si algo cambia", "Ocultar el cambio", "Cambiar sin explicar", "La comunicación oportuna evita que otras personas pierdan tiempo.")],
  ("abc", "Una persona adulta ficticia organiza una once comunitaria. Tiene la fecha, 30 invitados y un presupuesto, pero no ha dicho quién compra el pan. ¿Qué falta en la planificación?", "Asignar una persona responsable de esa actividad", "Un nuevo objetivo", "Más invitados", "Toda actividad necesita alguien que se haga cargo."),
  [("En Emprendimiento y Empleabilidad: ¿cuáles son las cuatro etapas de un proyecto?", "Inicio, planificación, ejecución y cierre", "Ordenan el trabajo desde la idea hasta la evaluación."),
   ("En Emprendimiento y Empleabilidad: ¿Qué es un indicador?", "Un dato que muestra si se logra el objetivo", "Permite verificar el avance con números."),
   ("¿Por qué asignar responsables?", "Para que cada tarea tenga a alguien que se haga cargo", "Sin responsable, una tarea puede quedar sin hacer.")],
  ("{F} Escribe para el proyecto de la ficha una tabla con las cinco tareas, la etapa a la que pertenece cada una y una persona responsable ficticia. Agrega un indicador para el objetivo.",
   "T1 autorización, planificación, Rosa. T2 afiches, planificación, Luis. T3 mesas, planificación, Ana. T4 feria, ejecución, todo el grupo. T5 evaluación, cierre, Pedro. Indicador: número de personas que intercambiaron ropa.",
   ["ubica cada tarea en una etapa", "asigna una persona responsable a cada tarea", "propone un indicador medible"],
   ["tabla con cinco tareas, etapas, responsables e indicador"],
   ["dejar tareas sin responsable", "proponer un indicador que no mide el objetivo"],
   "Comprueba que el indicador tenga relación con el objetivo. Si hay tareas sin responsable, pregunta quién se haría cargo."),
  "Escribe el objetivo de un proyecto ficticio de limpieza de una plaza de forma que se pueda medir.",
  "Escribe tres recursos que necesitaría un proyecto de once comunitaria con 30 personas.")

# ====================================================== OAD-05 clase 2
F = ("Ficha 2 (cronograma ficticio, duración en semanas). Proyecto de feria de trueque. "
     "A: obtener autorización del espacio, 1 semana, parte primero. B: hacer y pegar afiches, 2 semanas, puede comenzar cuando termina A. "
     "C: reunir mesas, 1 semana, puede comenzar cuando termina A, junto con B. D: realizar la feria, 1 semana de preparación y evento, comienza cuando terminan B y C. "
     "E: evaluar y agradecer, 1 semana, comienza cuando termina D.")
K(O5, 2, F,
  "Hoy aprenderé a ordenar actividades en un cronograma, a reconocer cuáles dependen de otras y a calcular cuánto dura el proyecto.",
  ["Un cronograma es una tabla o calendario que muestra cuándo se hace cada actividad. Una carta Gantt lo dibuja como barras en semanas. Algunas actividades dependen de otras: no se puede realizar la feria sin la autorización. Otras se pueden hacer a la vez si hay personas suficientes, como hacer afiches y reunir mesas.",
   "Para calcular cuánto dura el proyecto se mira la ruta más larga, es decir, la cadena de actividades que dependen una de otra. Las actividades que corren en paralelo no se suman: se cuenta solo la más larga. Si A dura 1, luego B dura 2 y C dura 1 a la vez, ese tramo dura 2 semanas, no 3.",
   "Un cronograma sirve para gestionar el tiempo con responsabilidad: ver atrasos, repartir tareas y avisar a tiempo. Si una actividad de la ruta larga se atrasa, todo el proyecto se atrasa. Las demás tienen algo de holgura, que es tiempo extra que se puede usar sin demorar el final. Se puede hacer con papel, una planilla o una herramienta de calendario."],
  [("cronograma", "tabla o calendario que muestra cuándo se hace cada actividad"), ("dependencia", "relación en que una actividad no puede comenzar hasta que termine otra"), ("ruta más larga", "cadena de actividades dependientes que determina la duración total"), ("holgura", "tiempo extra que una actividad puede usar sin demorar el final")],
  [("Dependencia", "¿Se puede realizar la feria sin la autorización del espacio?", ["La autorización permite usar el lugar.", "La feria depende de A."], "No, la feria depende de la autorización"),
   ("Duración con tareas en paralelo", "B dura 2 semanas y C dura 1 semana, y se hacen a la vez. ¿Cuánto dura ese tramo?", ["Corren juntas, no se suman.", "Dura lo que la más larga."], "2 semanas")],
  [("Sumar todas las duraciones aunque algunas sean simultáneas.", "Se olvida que las tareas en paralelo ocurren a la vez.", "Suma solo la ruta más larga."),
   ("Pensar que atrasar cualquier actividad atrasa el proyecto.", "No se distingue entre actividades críticas y con holgura.", "Si una actividad tiene holgura, puede atrasarse hasta cierto punto sin cambiar el final.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿qué es un cronograma?", "Una tabla o calendario que muestra cuándo se hace cada actividad", "Una lista de precios", "Un contrato", "Muestra cuándo empieza y termina cada actividad; una lista de precios o un contrato no ordenan el tiempo."),
   ("ab", "Una actividad que no puede empezar hasta que otra termine tiene", "una dependencia", "un indicador", "Esa relación de orden obligatorio entre actividades se llama dependencia."),
   ("abc", "{F} ¿Qué actividades pueden hacerse al mismo tiempo, una vez terminada A?", "B y C", "D y E", "A y D", "Ambas parten cuando termina A, así que corren en paralelo."),
   ("abc", "{F} ¿De cuáles actividades depende D, la feria?", "De B y de C", "Solo de E", "Solo de A", "D comienza cuando terminan B y C."),
   ("=", "{F} ¿Cuántas semanas dura la ruta A, B, D y E? Suma 1, 2, 1 y 1.", "1+2+1+1", "Se suman las actividades de la ruta que dependen una de otra.", " semanas"),
   ("=", "{F} ¿Cuántas semanas dura la ruta A, C, D y E?", "1+1+1+1", "Se suman las actividades de esa ruta de dependencia.", " semanas"),
   ("abc", "{F} Si ambas rutas se comparan, ¿cuál es la ruta más larga?", "A, B, D, E, que dura 5 semanas", "A, C, D, E, que dura 4 semanas", "Las dos duran lo mismo", "La que pasa por B es más larga porque B dura 2 semanas."),
   ("ab", "{F} Entonces la duración total del proyecto es", "5 semanas", "6 semanas", "La ruta más larga determina el total, que es de 5 semanas."),
   ("abc", "{F} Si C se atrasa una semana, ¿se atrasa el proyecto?", "No, porque C tiene una semana de holgura respecto de B", "Sí, siempre", "Solo si se atrasa dos semanas más", "D espera a B, que termina después de C."),
   ("abc", "{F} Si B se atrasa una semana, ¿qué ocurre?", "El proyecto dura una semana más, porque B está en la ruta más larga", "No ocurre nada", "El proyecto dura una semana menos", "Un atraso en la ruta más larga mueve el final."),
   ("abc", "Una persona ficticia dice: «como son cinco actividades, el proyecto dura 5 semanas». ¿Qué conviene revisar?", "Si hay actividades simultáneas y cuánto dura cada una", "Nada, porque tiene razón siempre", "El nombre de las actividades", "La duración depende de la ruta, no del número de actividades."),
   ("abc", "Un grupo no tiene voluntarios suficientes para hacer B y C a la vez. ¿Qué ocurre con el cronograma?", "Se alarga, porque deberán hacerse una después de la otra", "Se acorta", "No cambia", "Sin personas, las actividades paralelas pasan a ser secuenciales."),
   ("abc", "El grupo ve que va con 2 semanas de atraso en B. ¿Cuál es una respuesta responsable?", "Avisar, revisar el cronograma y acordar cambios con el grupo", "Ocultarlo", "Cancelar sin conversar", "Informar y reorganizar es gestionar el tiempo con responsabilidad.")],
  ("=", "Una persona ficticia organiza una jornada de salud comunitaria con tres etapas seguidas: obtener permiso, 2 semanas; preparar el lugar, 1 semana; realizar la jornada, 1 semana. ¿Cuántas semanas dura el proyecto en total?", "2+1+1", "Las etapas son seguidas, por lo que se suman sus duraciones.", " semanas"),
  [("En Emprendimiento y Empleabilidad: ¿qué es una dependencia?", "Una relación en que una actividad no empieza hasta que otra termine", "Marca el orden obligatorio entre las actividades."),
   ("¿Qué actividades no se suman al calcular la duración?", "Las que se hacen en paralelo", "Se cuenta solo la más larga."),
   ("En Emprendimiento y Empleabilidad: ¿Qué es la holgura?", "El tiempo extra que una actividad puede usar sin demorar el final", "Las actividades con holgura toleran pequeños atrasos.")],
  ("{F} Dibuja una carta Gantt con barras por semana para las actividades A a E y marca con color la ruta más larga. Escribe cuánto dura el proyecto y qué actividad tiene holgura.",
   "Semana 1: A. Semanas 2 y 3: B, y en la semana 2: C. Semana 4: D. Semana 5: E. Ruta más larga: A, B, D, E, 5 semanas. C tiene una semana de holgura.",
   ["ubica las cinco actividades por semana", "marca la ruta más larga", "indica la duración total y una actividad con holgura"],
   ["cuadro por semanas con barras, ruta marcada y respuesta final"],
   ["sumar B y C como si fueran seguidas", "no indicar la holgura"],
   "Verifica que B y C parten en la misma semana. Si suma 6 semanas, pregunta qué actividades ocurren a la vez."),
  "Escribe tres actividades de un proyecto ficticio y di cuál depende de cuál.",
  "Cambia la duración de B a 3 semanas y calcula la nueva duración del proyecto.")

# ====================================================== OAD-05 clase 3
F = ("Ficha 3 (caso ficticio). Un grupo de seis personas organiza una jornada de reciclaje en una plaza. Disponibilidad por semana: "
     "Camila 6 horas, Don Ramón 4 horas, Josefa 8 horas, Matías 3 horas, Pamela 5 horas y Tomás 4 horas. "
     "Camila y Don Ramón cuidan a familiares y no pueden salir después de las 18 h. Josefa se moviliza en silla de ruedas. "
     "Actividades: A1 hacer difusión, 10 horas; A2 preparar puntos de acopio, 12 horas; A3 coordinar el día de la jornada, 8 horas. "
     "Recursos: 4 bolsas grandes por punto de acopio y 5 puntos. Herramientas: planilla de horas y grupo de mensajería.")
K(O5, 3, F,
  "Hoy aprenderé a repartir tareas en un equipo de manera justa y diversa, a calcular recursos y horas, y a elegir herramientas para gestionar un proyecto.",
  ["Un proyecto lo hace un equipo, y cada persona tiene tiempo, habilidades y condiciones distintas. Repartir bien las tareas significa mirar la disponibilidad de cada una, sus intereses y sus necesidades. Por ejemplo, quien cuida a familiares puede tener horarios acotados, y una persona que se moviliza en silla de ruedas necesita lugares accesibles.",
   "La perspectiva de género y diversidad en un proyecto significa no asignar tareas por estereotipos, como que las mujeres hagan la comida y los hombres cargue peso. Todas las personas pueden proponer, decidir y liderar. Se revisa que las voces del grupo se escuchen y que los horarios y lugares permitan participar. Así el equipo aprovecha mejor sus capacidades.",
   "Para gestionar se calculan las horas necesarias y las disponibles, y se listan los recursos y herramientas. Una planilla de horas o un grupo de mensajería ayudan a coordinar. Si las horas no alcanzan, se piden más voluntarios, se acorta el alcance o se mueve el plazo. Todo el caso es ficticio; en tu comunidad cada equipo decide cómo organizarse."],
  [("equipo", "grupo de personas que trabaja junto en un proyecto"), ("disponibilidad", "tiempo que cada persona puede dedicar"), ("estereotipo", "idea fija sobre cómo «deben» ser o actuar ciertas personas"), ("accesibilidad", "condiciones que permiten que cualquier persona participe")],
  [("Calcular horas disponibles", "Camila tiene 6 horas, Don Ramón 4 y Josefa 8. ¿Cuántas horas suman entre las tres?", ["Se suman las disponibilidades.", "6 más 4 más 8."], "18 horas"),
   ("Evitar un estereotipo", "Se propone que Pamela prepare solo la comida de la jornada porque «es mujer». ¿Qué conviene hacer?", ["La tarea no debe asignarse por estereotipo.", "Se pregunta qué tarea le interesa y se reparte según disponibilidad y habilidades."], "Asignar según interés, habilidad y disponibilidad, sin estereotipos")],
  [("Asignar tareas por estereotipos de género.", "Se piensa que ciertas tareas «corresponden» a algunas personas.", "Reparte según disponibilidad, habilidades e intereses."),
   ("Programar reuniones en lugares o horarios que dejan fuera a alguien.", "No se consultó qué necesita cada persona.", "Pregunta por horarios y accesibilidad antes de fijar fechas.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿qué es un estereotipo?", "Una idea fija sobre cómo deben ser o actuar ciertas personas", "Una herramienta digital", "Un recurso del proyecto", "Los estereotipos limitan la participación y las capacidades."),
   ("=", "{F} ¿Cuántas horas semanales suman las seis personas del equipo? Suma 6, 4, 8, 3, 5 y 4.", "6+4+8+3+5+4", "Se suman todas las disponibilidades individuales.", " horas"),
   ("=", "{F} ¿Cuántas horas necesitan en total las tres actividades A1, A2 y A3?", "10+12+8", "Se suman las horas que necesita cada actividad.", " horas"),
   ("abc", "{F} Con 30 horas disponibles por semana y 30 necesarias, ¿qué se concluye?", "Alcanzan justo, sin margen para imprevistos", "Sobran muchas horas", "No alcanza para nada", "Ambas cifras son iguales, así que no queda holgura."),
   ("=", "{F} Si hay 5 puntos de acopio y cada uno necesita 4 bolsas grandes, ¿cuántas bolsas hacen falta?", "5*4", "Se multiplica la cantidad de puntos por las bolsas de cada uno.", " bolsas"),
   ("abc", "{F} ¿Qué condición debe cumplir el lugar de reunión para que Josefa participe?", "Ser accesible para una silla de ruedas", "Estar en el segundo piso sin ascensor", "Tener escalones", "La accesibilidad permite que todas las personas participen."),
   ("abc", "{F} ¿Qué horario es más adecuado para una reunión de todo el equipo?", "Antes de las 18 h", "A las 20 h", "A las 22 h", "Camila y Don Ramón no pueden salir después de las 18 h."),
   ("ab", "Una persona dice: «los hombres deberían cargar las cajas y las mujeres hacer afiches». Conviene responder", "que cada persona elija según sus habilidades y disponibilidad", "que tiene razón", "Las tareas no se reparten según el género sino según criterios del proyecto."),
   ("abc", "Matías solo puede 3 horas por semana. ¿Qué tarea le conviene?", "Una tarea breve y acotada, como entregar volantes un día", "Coordinar toda la jornada", "Ninguna, porque tiene poco tiempo", "Las horas limitadas se aprovechan con tareas pequeñas."),
   ("abc", "El grupo ve que solo habla la misma persona en las reuniones. ¿Qué acción promueve la diversidad?", "Dar la palabra por turnos y preguntar la opinión de quienes hablaron menos", "Que decida solo quien habla más", "Terminar las reuniones más rápido", "Escuchar a todas las voces enriquece las decisiones."),
   ("ab", "Si las horas disponibles no alcanzan, una respuesta responsable es", "pedir más voluntarios o acotar el alcance del proyecto", "pedir a las personas que trabajen sin descanso", "Se ajusta el plan a los recursos reales, sin sobrecargar a nadie."),
   ("abc", "{F} Camila tiene 6 horas disponibles y recibe una tarea de 9 horas. ¿Qué conviene hacer?", "Repartir parte de la tarea con otra persona", "Pedirle que trabaje más sin avisar", "Eliminar la tarea sin conversarlo", "La carga debe ajustarse a su disponibilidad real."),
   ("abc", "¿Qué herramienta ayuda a anotar quién hace qué y cuántas horas lleva?", "Una planilla de horas", "Una fotografía", "Un afiche", "La planilla ordena responsables y horas en una tabla.")],
  ("abc", "Una persona adulta ficticia lidera un taller en que dos integrantes no pueden venir en la tarde por cuidados familiares. ¿Qué decisión incluye a más personas?", "Ofrecer reunirse en la mañana o tener una opción por mensajería", "Fijar la reunión de noche sin consultar", "Excluirlas por no poder en la tarde", "Adaptar horarios y medios permite que todas las personas participen."),
  [("En Emprendimiento y Empleabilidad: ¿qué es accesibilidad?", "Condiciones que permiten que cualquier persona participe", "Incluye espacios, horarios y formas de comunicación."),
   ("¿Cómo se reparten las tareas de forma justa?", "Según disponibilidad, habilidades e intereses", "Así no se asignan por estereotipos."),
   ("¿Qué se hace si las horas no alcanzan?", "Se ajusta el plan: más personas, menos alcance o más plazo", "Ajustar el plan evita sobrecargar al equipo.")],
  ("{F} Reparte las tres actividades entre las seis personas, indicando cuántas horas le asignas a cada una sin pasar su disponibilidad, y explica cómo respetaste los horarios y la accesibilidad. Anota una herramienta que usarías para coordinar.",
   "A1 difusión (10 h): Pamela 5 h, Tomás 4 h y Matías 1 h. A2 puntos de acopio (12 h): Josefa 8 h y Camila 4 h. A3 coordinación (8 h): Camila 2 h, Don Ramón 4 h y Matías 2 h. Reuniones antes de las 18 h en un lugar accesible. Herramienta: planilla de horas.",
   ["asigna las tres actividades sin pasar la disponibilidad", "explica horarios y accesibilidad", "nombra una herramienta"],
   ["tabla de reparto con horas por persona y una explicación breve"],
   ["pasar la disponibilidad de una persona", "asignar por estereotipos"],
   "Suma las horas por persona y compáralas con su disponibilidad. Si asignó por género o edad, pide que explique el criterio con habilidades o interés."),
  "Escribe tres señales de que un equipo está incluyendo a todas las personas.",
  "Propón una forma de realizar una reunión para que participe una persona que solo puede por mensajería.")

# ====================================================== OAD-06 clase 1
F = ("Ficha 4 (tarjetas de vocabulario ficticias; el contenido legal depende de la norma vigente). "
     "Tarjeta 1: iniciación de actividades, aviso que una persona o empresa hace a la autoridad tributaria para comenzar a realizar una actividad económica. "
     "Tarjeta 2: patente municipal, permiso de la municipalidad para funcionar en un lugar. "
     "Tarjeta 3: contrato de trabajo, acuerdo escrito entre quien emplea y quien trabaja. "
     "Tarjeta 4: cotizaciones, aportes a la protección social (pensiones, salud y seguros) que se hacen según la norma vigente. "
     "Tarjeta 5: prevención de riesgos, medidas para evitar accidentes y enfermedades del trabajo.")
K(O6, 1, F,
  "Hoy aprenderé el vocabulario básico de las regulaciones para crear y operar una empresa o actividad y de las normativas laborales, y que lo que se exige se consulta en fuentes oficiales.",
  ["Quien emprende o emplea a otras personas debe cumplir normas. Algunas regulan cómo se crea y se opera una actividad, por ejemplo avisar a la autoridad tributaria que se iniciará una actividad y pedir el permiso municipal para funcionar en un lugar. Otras regulan el trabajo: el contrato, la remuneración, el descanso, la protección social y la seguridad.",
   "Las normas cambian con el tiempo y dependen del tipo de actividad, del lugar y del tamaño. Por eso en esta clase no se dan cifras, tasas ni plazos: siempre se dice «según la norma vigente» y se consulta la fuente oficial o a una persona profesional. Este material enseña el vocabulario y cómo buscar información; no es asesoría legal ni tributaria.",
   "Conocer las normas protege a todas las partes. Quien trabaja sabe qué derechos tiene, y quien emplea sabe qué debe cumplir y evita multas o accidentes. La protección social agrupa los aportes y beneficios que permiten enfrentar la vejez, la enfermedad o los accidentes. Un proyecto responsable incluye en su plan el tiempo y el costo de cumplir con la normativa."],
  [("regulación", "norma que ordena cómo se hace una actividad"), ("normativa laboral", "normas que regulan la relación entre quien emplea y quien trabaja"), ("protección social", "aportes y beneficios para enfrentar la vejez, la enfermedad o los accidentes"), ("fuente oficial", "sitio o institución del Estado que publica las normas vigentes")],
  [("Elegir término", "Una persona quiere funcionar en un local y necesita un permiso de la municipalidad. ¿Cómo se llama?", ["Es un permiso municipal.", "Se llama patente municipal."], "Patente municipal"),
   ("Buscar información", "Una persona duda cuál es el plazo vigente para un trámite. ¿Dónde debe consultar?", ["Los plazos cambian.", "Se consulta la fuente oficial vigente."], "En la fuente oficial vigente")],
  [("Dar por seguro un plazo o un monto que se escuchó.", "Las normas cambian y varían según la actividad.", "Consulta la fuente oficial antes de decidir."),
   ("Pensar que la normativa es solo un problema para quien emplea.", "Se ve la norma como una carga y no como una protección.", "La norma protege a quien trabaja y orienta a quien emplea.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿qué es una regulación?", "Una norma que ordena cómo se hace una actividad", "Un tipo de producto", "Un consejo personal", "Las regulaciones fijan reglas comunes para realizar actividades."),
   ("abc", "{F} ¿Qué tarjeta describe el permiso de la municipalidad para funcionar en un lugar?", "Tarjeta 2, la patente municipal", "Tarjeta 3, el contrato de trabajo", "Tarjeta 5, la prevención de riesgos", "La patente es el permiso municipal."),
   ("abc", "{F} ¿Qué tarjeta describe el acuerdo escrito entre quien emplea y quien trabaja?", "Tarjeta 3, el contrato de trabajo", "Tarjeta 1, la iniciación de actividades", "Tarjeta 4, las cotizaciones", "El contrato fija lo acordado entre las partes."),
   ("ab", "{F} Las cotizaciones se hacen", "según la norma vigente", "según lo que cada persona recuerde", "Los aportes se regulan por normas que pueden cambiar."),
   ("abc", "¿A qué sirve la prevención de riesgos?", "A evitar accidentes y enfermedades del trabajo", "A aumentar los precios", "A elegir el nombre del negocio", "Previene daños a las personas que trabajan."),
   ("ab", "Para saber cuál es el plazo vigente de un trámite conviene", "consultar la fuente oficial", "preguntar a quien lo escuchó de otra persona", "Las fuentes oficiales publican la norma actualizada."),
   ("abc", "Una persona ficticia dice: «escuché que la tasa es de un cierto número, así que la usaré». ¿Qué es más prudente?", "Verificar el dato en una fuente oficial vigente", "Usarlo sin revisar", "Inventar otro número", "Las cifras cambian y deben comprobarse."),
   ("abc", "¿Por qué las normas laborales son importantes para quien trabaja?", "Porque protegen sus derechos y su seguridad", "Porque solo benefician a quien emplea", "Porque son opcionales y cada parte decide si las cumple", "Fijan reglas claras de trato, pago y seguridad, y esas reglas no dependen de la voluntad de una sola parte."),
   ("abc", "Un grupo quiere vender comida en una feria. ¿Qué paso conviene antes de comenzar?", "Averiguar en fuentes oficiales qué permisos requiere la actividad", "Comenzar de inmediato sin consultar", "Pedir que otra persona lo averigüe sin avisar", "El permiso depende de la actividad y del lugar."),
   ("abc", "Un proyecto de ejemplo considera dos semanas para tramitar permisos. ¿Qué aclaración corresponde?", "Que el plazo real debe verificarse según la norma vigente", "Que ese plazo es seguro", "Que no hace falta tramitar nada", "El número del ejemplo no sustituye el plazo vigente."),
   ("ab", "La protección social incluye aportes para", "pensiones, salud y seguros según la norma vigente", "comprar productos", "Agrupa las coberturas que protegen a las personas en distintas situaciones."),
   ("abc", "Alguien dice: «con un contrato escrito ambas partes quedan sin derechos». ¿Qué respuesta es más adecuada?", "El contrato escrito aclara lo acordado y respalda a ambas partes", "Es cierto", "Los contratos no sirven", "Dejar por escrito lo acordado reduce los malentendidos entre las partes."),
   ("abc", "Una persona ficticia necesita orientación sobre su caso particular de trabajo. ¿Qué conviene?", "Consultar a la institución o profesional competente", "Decidir por lo que opine un conocido", "No averiguar nada", "Un caso particular requiere orientación experta.")],
  ("abc", "Una persona adulta ficticia quiere vender postres en su comunidad y se pregunta si necesita algún permiso. ¿Cuál es el mejor primer paso?", "Revisar fuentes oficiales o consultar a la municipalidad sobre qué se exige", "Esperar a que alguien la fiscalice", "Preguntar solo a quien le compró", "Los requisitos se informan en fuentes oficiales."),
  [("En Emprendimiento y Empleabilidad: ¿qué es la protección social?", "Aportes y beneficios para enfrentar vejez, enfermedad y accidentes", "Se regula según la norma vigente."),
   ("¿Qué es una patente municipal?", "Un permiso de la municipalidad para funcionar en un lugar", "Cada actividad puede tener requisitos distintos."),
   ("¿Por qué decir «según la norma vigente»?", "Porque las normas cambian y deben verificarse", "Se evita dar datos que ya no sirvan.")],
  ("{F} Elige dos tarjetas de la ficha. Para cada una escribe con tus palabras qué es, quién la necesita en un proyecto ficticio de venta de postres y dónde buscarías información vigente.",
   "Patente municipal: permiso para funcionar en un lugar; la necesita quien vende en un local; busco en la municipalidad o su sitio oficial. Contrato de trabajo: acuerdo escrito; lo necesita quien emplea; busco en la institución del Estado a cargo del trabajo.",
   ["explica dos tarjetas con sus palabras", "indica quién la necesitaría", "dice dónde buscar información vigente"],
   ["dos tarjetas con explicación, persona y fuente de consulta"],
   ["dar plazos o montos concretos", "no nombrar fuente oficial"],
   "Comprueba que no escriba montos ni plazos como si fueran seguros. Si no nombra una fuente oficial, pide que indique a quién consultaría."),
  "Escribe cuatro términos de la ficha con una frase breve cada uno.",
  "Escribe tres preguntas que harías a una institución oficial antes de iniciar un emprendimiento de venta de comida.")

# ====================================================== OAD-06 clase 2
F = ("Ficha 5 (documentos ficticios; cifras de ejemplo, no corresponden a valores reales). "
     "Contrato de ejemplo: partes (empleadora ficticia y trabajador ficticio), cargo ayudante de cocina, lugar de trabajo, jornada semanal, remuneración pactada de $450.000 mensuales, fecha de inicio. "
     "Liquidación de ejemplo: remuneración $450.000; bono de colación $30.000; descuentos de protección social $52.000 (monto de ejemplo, no una tasa real); líquido a pagar = remuneración más bono menos descuentos.")
K(O6, 2, F,
  "Hoy aprenderé qué datos incluye un contrato de trabajo y una liquidación de remuneraciones, cuáles son derechos laborales básicos y cómo leer un documento de ejemplo.",
  ["Un contrato de trabajo escrito deja claro lo acordado. Suele indicar quiénes son las partes, el cargo, el lugar de trabajo, la jornada, la remuneración y la fecha de inicio. Quien trabaja tiene derecho a recibir una copia. Los derechos específicos, como el descanso, los días de feriado y el monto mínimo de pago, se consultan según la norma vigente.",
   "La liquidación de remuneraciones es un documento mensual que muestra cuánto se pagó. Tiene haberes, que son lo que se suma, como el sueldo y los bonos, y descuentos, que son lo que se resta, como los aportes a la protección social. El líquido a pagar es lo que la persona recibe: haberes menos descuentos. Si algo no se entiende, se pregunta a quien lo emitió o a una institución competente.",
   "Respetar los derechos laborales es parte de emprender con responsabilidad: pagar lo acordado, respetar el descanso y no pedir trabajos inseguros. Un emprendimiento que no cumple pone en riesgo a las personas y a sí mismo. Estos son documentos de ejemplo; no reemplazan la revisión de un contrato real por la institución o la persona profesional correspondiente."],
  [("contrato de trabajo", "acuerdo escrito entre quien emplea y quien trabaja"), ("haberes", "montos que se suman a la remuneración, como sueldo y bonos"), ("descuentos", "montos que se restan de la remuneración"), ("líquido a pagar", "monto que la persona recibe después de los descuentos")],
  [("Leer un contrato", "El contrato de ejemplo dice «cargo ayudante de cocina». ¿Qué dato aporta?", ["Dice qué función cumplirá la persona.", "Aclara lo que se espera de ella."], "El cargo o función de la persona"),
   ("Calcular el líquido", "Haberes $480.000 y descuentos $52.000. ¿Cuál es el líquido a pagar?", ["Se resta el descuento al total de haberes.", "480.000 menos 52.000."], "$428.000")],
  [("Confundir remuneración con líquido a pagar.", "No se descuentan los aportes de la liquidación.", "El líquido es haberes menos descuentos."),
   ("Firmar un documento sin entenderlo.", "Se tiene vergüenza de preguntar.", "Pregunta lo que no entiendas y pide una copia.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿qué es un contrato de trabajo?", "Un acuerdo escrito entre quien emplea y quien trabaja", "Una liquidación de remuneraciones", "Una cotización de proveedor", "Deja constancia de lo acordado por ambas partes."),
   ("abc", "{F} ¿Cuál de estos datos aparece en el contrato de ejemplo?", "El cargo, la jornada y la remuneración pactada", "El precio de venta de los productos", "El detalle de las ventas del mes", "El contrato fija lo esencial de la relación de trabajo."),
   ("=", "{F} ¿Cuáles son los haberes de la liquidación? Suma la remuneración y el bono de colación.", "450000+30000", "Se suman los montos que se agregan a la remuneración.", " pesos"),
   ("=", "{F} ¿Cuál es el líquido a pagar? Suma haberes y resta los descuentos.", "450000+30000-52000", "Al total de haberes se le restan los descuentos de la liquidación.", " pesos"),
   ("ab", "Los descuentos de una liquidación son", "montos que se restan de la remuneración", "montos que se suman al sueldo", "Los descuentos reducen lo que la persona recibe."),
   ("abc", "Una persona nota que su liquidación tiene un monto que no entiende. ¿Qué conviene hacer?", "Preguntar a quien la emitió o a una institución competente", "Ignorarlo sin averiguar", "Romper el documento", "Preguntar aclara dudas antes de que se vuelvan problemas."),
   ("abc", "{F} Si los haberes fueran $500.000 y los descuentos $60.000, ¿cuál sería el líquido?", "$440.000", "$560.000", "$500.000", "Se resta el descuento del total de haberes."),
   ("abc", "¿Por qué se recomienda tener el contrato por escrito?", "Porque deja claro lo acordado y respalda a las partes", "Porque no hace falta saber lo acordado", "Porque sirve solo a una de las partes", "El documento escrito reduce malentendidos entre quienes firman."),
   ("ab", "Los derechos como el descanso y el monto mínimo de pago se consultan", "según la norma vigente y las fuentes oficiales", "según lo que diga cualquier persona", "Cambian con las normas, por lo que se verifican en fuentes oficiales."),
   ("abc", "Un emprendedor ficticio promete pagar «lo que se pueda» sin escribir nada. ¿Qué riesgo hay?", "Falta de claridad sobre lo acordado y posibles conflictos", "Ninguno, porque es más flexible", "Mejor protección", "Sin acuerdo escrito, ambas partes pueden entender cosas distintas."),
   ("abc", "En la ficha, ¿qué diferencia hay entre remuneración y líquido a pagar?", "La remuneración es el monto pactado y el líquido es lo recibido tras los descuentos", "Son siempre iguales", "El líquido es mayor que los haberes", "El líquido descuenta lo que se restó."),
   ("abc", "Una persona dice: «el bono de colación se resta, porque es un gasto». Según la liquidación de ejemplo, ¿qué es?", "Un haber que se suma", "Un descuento", "Un monto que no aparece", "En la ficha aparece sumando a la remuneración."),
   ("abc", "Un grupo quiere contratar a una persona para una tarea peligrosa sin implementos de seguridad. ¿Qué conviene?", "No hacerlo y ofrecer condiciones seguras según la norma vigente", "Hacerlo porque es más barato", "Pedir silencio sobre el riesgo", "Los derechos laborales incluyen condiciones seguras.")],
  ("abc", "Una persona ficticia recibe una liquidación con haberes $520.000 y descuentos $58.000. ¿Cuál es su líquido?", "$462.000", "$578.000", "$520.000", "Se restan los descuentos de los haberes."),
  [("En Emprendimiento y Empleabilidad: ¿qué son los haberes?", "Montos que se suman a la remuneración, como bonos", "Aumentan el total antes de descuentos."),
   ("¿Cómo se calcula el líquido a pagar?", "Haberes menos descuentos", "Es lo que la persona realmente recibe."),
   ("¿Qué datos suele tener un contrato?", "Partes, cargo, lugar, jornada, remuneración y fecha de inicio", "Resumen lo esencial de lo acordado.")],
  ("{F} Escribe tres datos del contrato de ejemplo y explica por qué son importantes. Luego calcula el líquido si el bono fuera de $20.000 y los descuentos fueran $50.000, y escribe a quién preguntarías una duda.",
   "Cargo: dice qué hará la persona. Jornada: dice cuánto tiempo trabajará. Remuneración: dice cuánto se pagará. Líquido: 450.000 más 20.000 menos 50.000 son $420.000. Preguntaría a quien emitió la liquidación o a la institución competente.",
   ["nombra tres datos del contrato con una razón", "calcula el líquido correctamente", "indica a quién preguntar una duda"],
   ["tres datos con razón, un cálculo y una persona o institución"],
   ["sumar los descuentos en vez de restarlos", "no indicar a quién preguntar"],
   "Revisa el cálculo: debe restar los descuentos. Si no hay institución o persona a quien preguntar, pide que lo agregue."),
  "Escribe qué dato de un contrato te interesaría revisar primero y por qué.",
  "Calcula el líquido con haberes de $390.000 y descuentos de $45.000 (cifras de ejemplo).")

# ====================================================== OAD-06 clase 3
F = ("Ficha 6 (local ficticio). Taller de costura de seis personas. Condiciones observadas: C1 cables sueltos en el piso. C2 extintor con revisión vencida. "
     "C3 salida de emergencia bloqueada con cajas. C4 sillas ajustadas y buena iluminación. C5 sin botiquín. "
     "Fuentes de información posibles: F1 sitio de una institución del Estado con fecha de actualización visible. F2 mensaje reenviado sin firma. "
     "F3 opinión de un foro anónimo. F4 documento de una municipalidad con su nombre y fecha.")
K(O6, 3, F,
  "Hoy aprenderé a identificar condiciones de seguridad en un lugar de trabajo, a reconocer derechos y deberes en la prevención de riesgos y a buscar información confiable con medios digitales.",
  ["La seguridad en el trabajo busca evitar accidentes y enfermedades. Quien emplea debe cuidar las condiciones del lugar y quien trabaja debe seguir las medidas y avisar de los peligros, según la norma vigente. Algunas señales de riesgo son cables sueltos, salidas bloqueadas, falta de extintor o de botiquín, piso resbaladizo y máquinas sin protección.",
   "Cuando se detecta un riesgo se avisa, se corrige lo antes posible y se deja constancia. Se puede ordenar por gravedad: lo que puede causar un daño serio, como una salida de emergencia bloqueada, se corrige primero. Un lugar seguro es más productivo, porque se evitan accidentes y paralizaciones.",
   "Para averiguar qué exige la norma, se usan las tecnologías de la información. Una buena fuente es oficial, tiene un autor identificable y una fecha de actualización. Un mensaje reenviado, una opinión anónima o un video sin fuente no sirven para decidir. Contrastar al menos dos fuentes confiables reduce errores. Esta clase no es asesoría legal: para un caso real se consulta a la institución competente."],
  [("prevención de riesgos", "medidas para evitar accidentes y enfermedades del trabajo"), ("fuente confiable", "información con autor identificable, origen oficial y fecha"), ("contrastar", "comparar la información con otras fuentes"), ("constancia", "registro escrito de que algo se informó o se hizo")],
  [("Ordenar por gravedad", "Hay un cable suelto y una salida de emergencia bloqueada. ¿Qué se corrige primero?", ["Una salida bloqueada impide evacuar.", "El riesgo de daño serio es mayor."], "La salida de emergencia bloqueada"),
   ("Elegir una fuente", "Hay un mensaje reenviado sin firma y un documento de una municipalidad con nombre y fecha. ¿Cuál es más confiable?", ["El documento tiene origen y fecha.", "El mensaje no tiene autoría."], "El documento de la municipalidad")],
  [("Ignorar un riesgo porque «nunca ha pasado nada».", "Se piensa que la falta de accidentes prueba seguridad.", "Se corrigen los riesgos antes de que ocurra un accidente."),
   ("Creer en información solo porque llegó por mensaje.", "No se pregunta quién la escribió ni cuándo.", "Busca el origen y contrasta con una fuente oficial.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿para qué sirve la prevención de riesgos?", "Para evitar accidentes y enfermedades del trabajo", "Para vender más", "Para reducir la jornada", "Evita daños antes de que ocurran."),
   ("abc", "{F} ¿Qué condición del taller es la más grave?", "C3, la salida de emergencia bloqueada", "C4, las sillas ajustadas", "C1, cables sueltos en el piso", "Una salida bloqueada impide evacuar en una emergencia."),
   ("abc", "{F} ¿Qué condición del taller es positiva?", "C4, sillas ajustadas y buena iluminación", "C1, cables sueltos", "C5, sin botiquín", "Cuida la comodidad y la visión de quienes trabajan."),
   ("abc", "{F} ¿Qué fuente de información es más confiable?", "F1, el sitio de una institución del Estado con fecha de actualización", "F2, un mensaje reenviado sin firma", "F3, una opinión de un foro anónimo", "Tiene un origen identificable y una fecha de actualización visible."),
   ("ab", "{F} La fuente F4, un documento de una municipalidad con nombre y fecha, es", "confiable, porque identifica su origen y su fecha", "poco confiable, porque es oficial", "Un autor identificable y una fecha permiten comprobar la información."),
   ("abc", "{F} ¿Qué corresponde hacer con el extintor con revisión vencida (C2)?", "Avisar y gestionar su revisión o reemplazo", "Dejarlo igual porque no hay incendios", "Retirarlo sin reemplazarlo", "Un extintor vencido no ofrece la protección esperada."),
   ("=", "{F} Se observaron 5 condiciones, y 4 son riesgos. ¿Cuántas no son riesgo?", "5-4", "Se resta la cantidad de riesgos del total observado.", " condición"),
   ("abc", "Una persona ve un piso mojado sin señal. ¿Qué acción es más adecuada?", "Avisar, señalizar y secar", "Pasar rápido y no decir nada", "Esperar a que alguien se caiga", "Señalar y corregir el piso evita caídas de otras personas."),
   ("abc", "Un grupo debe decidir qué normas de seguridad exige su actividad. ¿Qué es más prudente?", "Consultar fuentes oficiales y contrastar al menos dos", "Seguir lo que dijo una persona conocida sin preguntar", "No consultar nada", "Contrastar fuentes confiables reduce los errores en la decisión."),
   ("ab", "Si un mensaje reenviado dice un plazo legal, lo más responsable es", "verificarlo en una fuente oficial antes de usarlo", "darlo por cierto porque es urgente", "Los mensajes sin origen no sirven para tomar decisiones."),
   ("abc", "Una persona del taller avisa a su encargada que hay un cable suelto y no recibe respuesta. ¿Qué es más adecuado?", "Dejar constancia por escrito y consultar a una institución competente", "No volver a hablar del tema", "Esconder el cable", "Dejar constancia y consultar permite buscar solución."),
   ("abc", "Un emprendedor dice: «el botiquín es un gasto innecesario». ¿Qué respuesta es más acertada?", "Un botiquín ayuda a responder a un accidente y es parte de la seguridad", "Tiene razón", "Es solo para empresas grandes", "Permite responder rápido ante lesiones menores en el trabajo."),
   ("abc", "Una persona busca por internet cómo es una norma. ¿Qué dato debe mirar para saber si está al día?", "La fecha de actualización", "El color de la página", "La cantidad de anuncios", "Las normas cambian y la fecha muestra su vigencia.")],
  ("abc", "Una persona adulta ficticia trabaja en una bodega donde las cajas bloquean un pasillo de emergencia. ¿Qué es lo más adecuado?", "Avisar a quien corresponda y dejar constancia para que se despeje", "Seguir trabajando sin decir nada", "Mover las cajas encima de la salida", "Una salida despejada es esencial para evacuar."),
  [("En Emprendimiento y Empleabilidad: ¿qué es una fuente confiable?", "Información con autor identificable, origen oficial y fecha", "Permite comprobar la información con otras fuentes confiables."),
   ("¿Qué riesgo se corrige primero?", "El que puede causar un daño más serio", "Se ordenan los riesgos por gravedad para actuar primero."),
   ("En Emprendimiento y Empleabilidad: ¿Por qué contrastar fuentes?", "Porque reduce errores al comparar información", "Una sola fuente puede estar desactualizada.")],
  ("{F} Ordena los cinco hallazgos del taller de mayor a menor gravedad con una razón para el primero y el último. Luego elige una fuente de información de la ficha y explica por qué la usarías.",
   "Orden: C3, C2, C5, C1, C4. C3 es el más grave porque impide evacuar. C4 no es un riesgo. Usaría F1 porque es una institución del Estado con fecha de actualización.",
   ["ordena los hallazgos con criterio de gravedad", "justifica el primero y el último", "elige una fuente confiable con razón"],
   ["lista ordenada con dos razones y una fuente elegida"],
   ["poner C4 como un riesgo", "elegir F2 o F3 como confiables"],
   "Comprueba que C3 quede primero y que C4 no figure como riesgo. Si elige una fuente anónima, pide que explique cómo comprobaría el dato."),
  "Escribe tres señales de riesgo en un lugar de trabajo y una medida para cada una.",
  "Escribe qué dos fuentes consultarías para saber qué exige la seguridad en una cocina comunitaria.")

# ====================================================== OAD-07 clase 1
F = ("Ficha 7 (proyecto ficticio, cifras de ejemplo). Taller de repostería de una persona ficticia. Cada mes espera vender 80 tortas a $9.000 cada una. "
     "Costo variable: $4.000 de ingredientes por torta. Costos fijos mensuales: arriendo de cocina $90.000, transporte $30.000 y publicidad $20.000. "
     "Inversión inicial, que se paga una sola vez: batidora y moldes por $150.000.")
K(O7, 1, F,
  "Hoy aprenderé qué es un presupuesto, a distinguir ingresos, costos fijos, costos variables e inversión inicial, y a calcular el saldo mensual de un proyecto.",
  ["Un presupuesto es un cálculo anticipado de cuánto dinero entrará y cuánto saldrá en un proyecto. Sirve para decidir con información, no con suposiciones. Se hace con tablas simples en papel o en una planilla, y se revisa cuando cambian los precios o las ventas.",
   "Los ingresos son el dinero que se espera recibir por vender. Los costos variables cambian con la cantidad producida, como los ingredientes. Los costos fijos son iguales cada mes, como el arriendo. La inversión inicial es un gasto que se hace una sola vez para partir, como comprar equipos. El saldo mensual es el ingreso menos todos los costos del mes.",
   "Un buen presupuesto es honesto: usa cifras que se puedan respaldar, anota de dónde salen y deja una reserva para imprevistos. Si el saldo da negativo, el proyecto pierde dinero y hay que ajustar precios, ventas o costos. Los montos de esta clase son de ejemplo y no representan precios reales."],
  [("presupuesto", "cálculo anticipado de lo que entra y sale de dinero en un proyecto"), ("saldo", "ingresos menos costos"), ("inversión inicial", "gasto que se hace una sola vez para comenzar"), ("imprevisto", "gasto que no estaba planificado")],
  [("Calcular un ingreso", "Se venden 80 tortas a $9.000. ¿Cuál es el ingreso mensual?", ["Se multiplica la cantidad por el precio.", "80 por 9.000."], "$720.000"),
   ("Calcular el saldo", "Ingresos $720.000 y costos $460.000. ¿Cuál es el saldo mensual?", ["Se resta el costo total al ingreso.", "720.000 menos 460.000."], "$260.000")],
  [("Contar la inversión inicial como un gasto mensual.", "No se distingue lo que se paga una vez de lo que se paga cada mes.", "La inversión inicial se anota aparte y no se repite cada mes."),
   ("Calcular el presupuesto sin dejar reserva.", "Se supone que todo saldrá según lo previsto.", "Agrega una reserva para gastos imprevistos.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿qué es un presupuesto?", "Un cálculo anticipado de lo que entra y sale de dinero en un proyecto", "El dinero que ya se gastó", "Una lista de deseos", "Anticipa números para decidir con información."),
   ("abc", "{F} ¿Cuál de estos es un costo variable?", "Los $4.000 de ingredientes por torta", "El arriendo de cocina", "La publicidad mensual", "Los ingredientes cambian con la cantidad de tortas."),
   ("ab", "{F} El arriendo de cocina de $90.000 es un costo", "fijo, porque se paga igual cada mes", "variable, porque cambia con cada torta", "No depende de cuántas tortas se vendan."),
   ("=", "{F} ¿Cuál es el ingreso mensual esperado?", "80*9000", "Se multiplica la cantidad de tortas por el precio de cada una.", " pesos"),
   ("=", "{F} ¿Cuánto suman los costos variables de las 80 tortas?", "80*4000", "Se multiplica la cantidad de tortas por el costo variable de cada una.", " pesos"),
   ("=", "{F} ¿Cuánto suman los costos fijos mensuales?", "90000+30000+20000", "Se suman el arriendo, el transporte y la publicidad.", " pesos"),
   ("=", "{F} ¿Cuál es el saldo mensual? Ingreso menos costos variables menos costos fijos.", "720000-320000-140000", "Se restan al ingreso todos los costos del mes.", " pesos"),
   ("abc", "{F} ¿Cómo se trata la compra de la batidora y los moldes por $150.000?", "Como una inversión inicial, que se paga una sola vez", "Como un costo variable mensual", "Como un ingreso", "Se hace una vez para comenzar y no se repite cada mes."),
   ("=", "{F} Si cada torta se vende en $9.000 y cuesta $4.000 de ingredientes, ¿cuánto queda por torta para pagar los costos fijos?", "9000-4000", "Se resta el costo variable al precio de venta de cada torta.", " pesos"),
   ("abc", "Una persona ficticia dice: «el presupuesto da $260.000, así que gastaré los $260.000 sin guardar nada». ¿Qué conviene?", "Dejar una reserva para imprevistos", "Gastarlo todo", "Subir el precio sin avisar", "Los imprevistos pueden aparecer cualquier mes."),
   ("ab", "Si el saldo mensual da negativo, lo más razonable es", "ajustar precios, ventas o costos", "ignorar el resultado", "Un saldo negativo indica que el proyecto pierde dinero con esos números."),
   ("abc", "Un presupuesto usa un precio de ingredientes que se supone, sin saber de dónde salió. ¿Qué mejora es más útil?", "Anotar la fuente del precio, como una cotización o una boleta", "Subir el número al azar", "No mencionar el precio", "Cifras con respaldo permiten revisar y confiar en el presupuesto."),
   ("abc", "Un grupo vende 60 tortas en vez de 80, con los mismos costos fijos. ¿Qué ocurre con el saldo?", "Baja, porque entran menos ingresos y los costos fijos siguen igual", "Sube", "No cambia", "Los costos fijos no bajan aunque se venda menos.")],
  ("=", "Una persona adulta ficticia quiere vender 50 panes amasados a $1.500 cada uno. Cada pan cuesta $600 en ingredientes y los costos fijos son $20.000. ¿Cuál es el saldo mensual de este ejemplo?", "50*1500-50*600-20000", "Al ingreso se le restan los costos variables y los costos fijos.", " pesos"),
  [("En Emprendimiento y Empleabilidad: ¿qué es una inversión inicial?", "Un gasto que se hace una sola vez para comenzar", "No se repite cada mes porque se paga una sola vez."),
   ("¿Cuál es la diferencia entre costo fijo y variable?", "El fijo no cambia con la cantidad y el variable sí", "Se tratan de manera distinta en el presupuesto."),
   ("¿Por qué dejar una reserva?", "Para enfrentar gastos imprevistos", "Reduce el riesgo de quedar sin dinero.")],
  ("{F} Arma una tabla de presupuesto mensual con ingresos, costos variables, costos fijos y saldo. Aparte, anota la inversión inicial. Escribe una reserva que propondrías y por qué.",
   "Ingresos $720.000. Costos variables $320.000. Costos fijos $140.000. Saldo $260.000. Inversión inicial $150.000. Reserva: $30.000 al mes para imprevistos, porque los ingredientes podrían subir de precio.",
   ["calcula ingresos, costos y saldo", "anota la inversión aparte", "propone una reserva con una razón"],
   ["tabla con cuatro cifras, inversión y reserva"],
   ["sumar la inversión a los costos mensuales", "olvidar los costos variables"],
   "Verifica el saldo. Si suma la inversión al mes, pregunta cuántas veces se paga."),
  "Escribe un costo fijo, un costo variable y una inversión inicial de un negocio ficticio de venta de sándwiches.",
  "Calcula el saldo mensual si el precio de la torta sube a $10.000 y se venden 80.")

# ====================================================== OAD-07 clase 2
F = ("Ficha 8 (proyecto ficticio, cifras de ejemplo; no son sueldos ni montos legales reales). Taller de repostería que contrata a una ayudante. "
     "Costos fijos del taller: arriendo $90.000, transporte $30.000, publicidad $20.000. Remuneración pactada de la ayudante: $250.000 al mes. "
     "Aportes de empleador y trámites: $45.000 al mes de ejemplo; el monto real depende de la norma vigente. "
     "Ingresos esperados: $720.000 al mes. Costos variables: $320.000 al mes. Reserva para imprevistos propuesta: el 10 % de todos los costos.")
K(O7, 2, F,
  "Hoy aprenderé a incluir en el presupuesto las remuneraciones, los aportes y los trámites que exige la norma vigente, a calcular una reserva y a revisar si el proyecto es viable.",
  ["Cuando un proyecto contrata a una persona, el presupuesto debe incluir su remuneración y los aportes y trámites que la norma vigente exija a quien emplea. Dejar estos gastos fuera hace que el presupuesto parezca mejor de lo que es. En esta clase usamos montos de ejemplo: los valores reales se consultan en fuentes oficiales.",
   "Una reserva es un porcentaje de los costos que se guarda para imprevistos. Un 10 por ciento significa 10 de cada 100: para calcularlo se divide el total por 10. Si los costos son $500.000, la reserva de 10 por ciento es $50.000. Se suma a los costos para ver cuánto debe cubrir el ingreso.",
   "Un proyecto es viable si el ingreso cubre los costos, incluida la reserva. Si no cubre, se ajusta: subir precios con cuidado, bajar costos o vender más. Un presupuesto responsable también considera la actividad económica del proyecto, porque algunas actividades tienen permisos y gastos propios, según la norma vigente."],
  [("remuneración", "pago que recibe una persona por su trabajo"), ("reserva", "dinero que se guarda para imprevistos"), ("viable", "que se puede mantener porque el ingreso cubre los costos"), ("aportes del empleador", "pagos que debe hacer quien emplea según la norma vigente")],
  [("Calcular una reserva", "Los costos suman $500.000. ¿Cuánto es una reserva de 10 por ciento?", ["Un 10 por ciento es la décima parte.", "500.000 dividido en 10."], "$50.000"),
   ("Revisar viabilidad", "Los ingresos son $700.000 y los costos con reserva $720.000. ¿Es viable?", ["El ingreso debe cubrir los costos.", "700.000 es menor que 720.000."], "No es viable con esos números")],
  [("Dejar fuera del presupuesto las remuneraciones y los aportes.", "Se piensa solo en el gasto de materiales.", "Incluye siempre el costo de las personas que trabajan."),
   ("Usar un porcentaje que alguien mencionó sin verificarlo.", "No se consulta una fuente oficial.", "Verifica los montos y porcentajes legales en fuentes oficiales.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿qué es una reserva en un presupuesto?", "Dinero que se guarda para imprevistos", "Un descuento al cliente", "Un tipo de contrato", "Se aparta para cubrir gastos inesperados."),
   ("=", "{F} ¿Cuánto suman la remuneración y los aportes de la ayudante?", "250000+45000", "Se suman la remuneración y los aportes de ejemplo.", " pesos"),
   ("=", "{F} ¿Cuánto suman los costos fijos del taller (arriendo, transporte y publicidad)?", "90000+30000+20000", "Se suman los tres costos fijos del taller.", " pesos"),
   ("=", "{F} ¿Cuál es el costo total mensual, con costos variables, costos fijos y personal?", "320000+140000+250000+45000", "Se suman todos los costos del mes, incluidas las personas.", " pesos"),
   ("=", "{F} ¿Cuánto es la reserva del 10 % de ese costo total de $755.000?", "755000//10", "El 10 por ciento se obtiene dividiendo por 10.", " pesos"),
   ("=", "{F} ¿Cuánto debe cubrir el ingreso, sumando el costo total y la reserva de $75.500?", "755000+75500", "El ingreso debe cubrir costos y reserva.", " pesos"),
   ("abc", "{F} Con ingresos esperados de $720.000, ¿qué se concluye?", "No alcanza para cubrir costos más reserva", "Alcanza con mucho sobrante", "Alcanza exactamente", "720.000 es menor que 830.500, que es lo que se necesita."),
   ("abc", "{F} ¿Qué ajuste puede hacer viable el proyecto?", "Vender más tortas o bajar algunos costos", "Aumentar la remuneración sin vender más", "Eliminar la reserva y los aportes sin revisar la norma", "Más ingresos o menos costos acercan el presupuesto a lo necesario."),
   ("ab", "Una persona dice: «los aportes de la ayudante no los incluyo porque se pagan después». Es más acertado decir que", "debe incluirlos porque son un costo del proyecto", "puede dejarlos fuera sin problemas", "Los aportes son parte del costo real de emplear a alguien."),
   ("abc", "Un grupo calcula una reserva del 10 % de sus costos de $400.000. ¿Cuánto es?", "$40.000", "$4.000", "$400.000", "Se divide el total por 10."),
   ("abc", "Un grupo no sabe qué permisos necesita su actividad. ¿Qué incluye prudentemente en su presupuesto?", "Una partida para trámites, con el monto que informe la fuente oficial", "Nada, porque son gratis siempre", "Un monto inventado como si fuera oficial", "El valor real debe informarse según la norma vigente."),
   ("abc", "Si el grupo sube la remuneración de la ayudante en $20.000 mensuales, ¿qué cambia en el presupuesto?", "El costo total sube y puede necesitarse más ingreso", "Nada cambia", "Los ingresos suben solos", "Más remuneración significa más costo fijo."),
   ("abc", "¿Cómo se explica «viable» a otra persona?", "El ingreso cubre todos los costos del proyecto", "Es un proyecto muy conocido", "Es un proyecto sin riesgos", "Si el dinero que entra cubre lo que sale, el proyecto se puede sostener.")],
  ("=", "Un puesto ficticio de comida tiene costos mensuales de $600.000 y quiere una reserva del 10 %. ¿Cuánto dinero total debe cubrir el ingreso? (Cifras de ejemplo.)", "600000+600000//10", "Se suma al costo la reserva del 10 por ciento.", " pesos"),
  [("En Emprendimiento y Empleabilidad: ¿qué significa viable?", "Que el ingreso cubre todos los costos y se puede mantener", "Un proyecto viable se sostiene en el tiempo."),
   ("¿Cómo se calcula un 10 % de un número?", "Se divide por 10", "10 de cada 100 equivale a la décima parte."),
   ("¿Por qué incluir los aportes y trámites?", "Porque son costos reales del proyecto según la norma vigente", "Dejarlos fuera hace parecer mejor el presupuesto.")],
  ("{F} Cambia un dato del presupuesto para que el proyecto sea viable: elige entre aumentar ventas, bajar un costo o subir un precio. Escribe el cambio, el nuevo ingreso o costo y comprueba si el ingreso cubre el costo total con reserva.",
   "Subo el precio de 9.000 a 10.500 con 80 tortas: ingreso 840.000, que cubre los 830.500 necesarios. Riesgo: que haya menos clientes con el precio nuevo.",
   ["propone un cambio concreto", "calcula el nuevo valor", "compara con el costo total con reserva", "nombra un riesgo del cambio"],
   ["cambio, cálculo, comparación y riesgo"],
   ["no comparar con el total con reserva", "ignorar el riesgo del cambio"],
   "Revisa que compare con $830.500 y no con $755.000. Si no nombra riesgo, pregunta qué pasaría con los clientes."),
  "Calcula la reserva del 10 % de costos de $320.000.",
  "Propone dos formas distintas de hacer viable un proyecto que no cubre sus costos.")

# ====================================================== OAD-07 clase 3
F = ("Ficha 9 (caso ficticio, cifras de ejemplo). Un grupo de cuatro personas arma el presupuesto de un taller de reparación de bicicletas. "
     "Cotizaciones de repuestos para una misma compra: Proveedor A $180.000, Proveedor B $165.000. "
     "Una persona del grupo propone copiar la lista de precios de otro taller, que recibió en confianza y no es pública. "
     "Otra propone publicar el teléfono de los clientes para hacer publicidad sin preguntarles. "
     "Dos personas trabajarán igual cantidad de horas y con las mismas tareas; se propone pagar $200.000 a una y $180.000 a la otra sin otra razón.")
K(O7, 3, F,
  "Hoy aprenderé a elaborar un presupuesto con principios éticos en el uso de la información y con igualdad de trato en las remuneraciones, y a incorporar una mirada social.",
  ["Un presupuesto usa información: precios, cotizaciones, datos de clientes. Usarla con ética significa citar de dónde viene, no copiar listas que alguien entregó en confianza, no inventar cifras y no usar datos personales sin permiso. Comparar cotizaciones de varios proveedores es correcto; apropiarse de información privada de otro no lo es.",
   "La mirada de género y diversidad también está en el presupuesto. Si dos personas hacen el mismo trabajo, con las mismas tareas y horas, la remuneración debe ser la misma, según la norma vigente. Las diferencias de pago solo se justifican con razones objetivas del trabajo, como la jornada o las funciones, y no por género, edad u otra característica personal.",
   "Una evaluación social del presupuesto pregunta qué beneficio trae el gasto a las personas: ¿cuántas personas se favorecen?, ¿hay alguien que quede fuera? Un presupuesto transparente se puede mostrar a todo el grupo y a la comunidad. Esto aumenta la confianza y permite corregir errores a tiempo."],
  [("cotización", "precio que ofrece un proveedor por un producto o servicio"), ("transparencia", "mostrar con claridad de dónde salen las cifras y cómo se decidió"), ("igualdad de trato", "dar las mismas condiciones a quienes hacen el mismo trabajo"), ("confidencial", "que se entregó en reserva y no debe difundirse")],
  [("Comparar cotizaciones", "Proveedor A cobra $180.000 y B $165.000 por lo mismo. ¿Cuánto se ahorra con B?", ["Se compara el precio de ambos.", "180.000 menos 165.000."], "$15.000"),
   ("Detectar una falta ética", "Una persona propone copiar una lista de precios que otro taller entregó en confianza. ¿Es correcto?", ["Esa información es confidencial.", "No es correcto usarla sin permiso."], "No es correcto")],
  [("Usar información privada de otros para ahorrar tiempo.", "Se piensa que no importa de dónde viene el dato.", "Usa fuentes propias y cotizaciones abiertas o autorizadas."),
   ("Pagar menos por igual trabajo sin una razón objetiva.", "Se acepta una diferencia que nadie explica.", "La remuneración debe ser igual por trabajo igual, según la norma vigente.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿qué es una cotización?", "El precio que ofrece un proveedor por un producto o servicio", "El nombre de un cliente", "Un contrato laboral", "Sirve para comparar precios antes de comprar."),
   ("=", "{F} ¿Cuánto se ahorra al elegir al proveedor B en lugar de A?", "180000-165000", "Se resta el precio de B al de A.", " pesos"),
   ("abc", "{F} ¿Es ético copiar la lista de precios que otro taller entregó en confianza?", "No, porque es información confidencial", "Sí, porque ahorra tiempo", "Sí, si nadie se entera", "Usar información reservada sin permiso falta a la honestidad."),
   ("abc", "{F} ¿Qué corresponde con el teléfono de los clientes?", "No publicarlo sin su permiso", "Publicarlo para hacer publicidad", "Entregarlo a otro taller", "Los datos personales solo se usan con el consentimiento de cada persona."),
   ("abc", "{F} Dos personas hacen las mismas tareas y horas. ¿Qué remuneración corresponde?", "La misma para ambas, salvo razones objetivas del trabajo", "Más para quien lleva más tiempo viviendo en el barrio", "Menos para quien tenga más edad", "A igual trabajo corresponde igual trato en la remuneración."),
   ("=", "{F} Si el taller paga $200.000 a una persona y $180.000 a otra sin razón, ¿cuál es la diferencia mensual entre ambas?", "200000-180000", "Se resta la remuneración menor de la mayor.", " pesos"),
   ("abc", "¿Cuál de estas es una razón objetiva para una diferencia de pago?", "Que una persona trabaja más horas por semana", "Que una persona es más joven", "Que una persona es de otro género", "La jornada es una condición del trabajo, no una característica personal."),
   ("ab", "Citar de dónde viene el precio de un repuesto es", "una práctica ética y transparente", "algo innecesario", "Permite comprobar la cifra y da confianza al grupo."),
   ("abc", "Una persona ficticia propone inventar cifras más bajas de costos para que un presupuesto parezca más atractivo. ¿Qué principio se vulnera?", "La honestidad con los datos", "La rapidez", "La innovación", "Cifras falsas engañan a quienes toman decisiones."),
   ("abc", "Un presupuesto transparente permite", "mostrar a todo el grupo de dónde salen las cifras y corregir errores", "ocultar los datos importantes", "dejar decidir a una sola persona", "La claridad ayuda a detectar errores a tiempo."),
   ("ab", "Para una evaluación social del presupuesto, una pregunta útil es", "¿cuántas personas se benefician y quién queda fuera?", "¿qué proveedor tiene el nombre más conocido?", "Mira el efecto del gasto sobre las personas."),
   ("abc", "Un grupo compara tres cotizaciones y elige la más barata sin leer que no incluye despacho. ¿Qué debió hacer?", "Comparar lo que incluye cada cotización antes de decidir", "Elegir siempre la más cara", "No cotizar", "El precio más bajo puede no incluir todo lo necesario."),
   ("abc", "Una persona descubre que dos compañeras ganan distinto por el mismo trabajo y sin motivo. ¿Cuál es una acción adecuada?", "Plantearlo al grupo y proponer corregirlo", "Callar para evitar conflictos", "Rebajar el sueldo de ambas", "Hablar y corregir cumple el trato igualitario.")],
  ("abc", "Una persona adulta ficticia arma el presupuesto de un servicio de cuidado de plantas. Le pasan una lista de clientes con teléfonos de otro negocio sin permiso. ¿Qué es lo más adecuado?", "No usar la lista y buscar clientes con avisos propios", "Usar la lista porque ahorra trabajo", "Vender la lista", "Usar datos ajenos sin autorización es una falta ética."),
  [("En Emprendimiento y Empleabilidad: ¿qué es la transparencia en un presupuesto?", "Mostrar con claridad de dónde salen las cifras", "Permite que el grupo revise y corrija."),
   ("¿Cuándo es justa una diferencia de pago?", "Cuando hay una razón objetiva del trabajo, como las horas", "No se justifica por género, edad o características personales."),
   ("¿Qué datos personales no se usan sin permiso?", "Teléfono, dirección y otros que identifican a una persona", "Se protegen por respeto y por norma.")],
  ("{F} Escribe tres reglas éticas para el presupuesto del taller sobre información, datos de clientes y remuneraciones, y explica con un ejemplo de la ficha por qué cada una importa. Elige entre A y B con una razón.",
   "Regla 1: citar la fuente de cada precio. Regla 2: no usar teléfonos sin permiso. Regla 3: igual pago por igual trabajo. Elijo B por ahorrar $15.000, siempre que incluya lo mismo que A.",
   ["escribe tres reglas distintas", "las relaciona con la ficha", "elige proveedor con una razón"],
   ["tres reglas con ejemplo y una elección de proveedor"],
   ["elegir B sin considerar si incluye lo mismo", "repetir una misma regla con otras palabras"],
   "Verifica que las tres reglas sean distintas y que cada una cite un caso. Si elige proveedor sin mirar qué incluye, pregunta si ofrecen lo mismo."),
  "Escribe tres datos que nunca publicarías de tus clientes sin permiso.",
  "Escribe cómo explicarías a un equipo que dos personas con el mismo trabajo deben recibir la misma remuneración.")

# ====================================================== OAD-08 clase 1
F = ("Ficha 10 (proyecto ficticio, cifras de ejemplo). Huerto comunitario de un sector. Gastos del año: semillas $60.000, herramientas $120.000, agua $60.000, total $240.000. "
     "Resultados: 600 kg de verduras y 40 familias participantes. Meta del plan: 500 kg y 50 familias. "
     "Un voluntario nota que se usaron 40 horas de trabajo adicionales no previstas.")
K(O8, 1, F,
  "Hoy aprenderé qué significa evaluar un plan, a calcular indicadores de eficiencia como el costo por unidad, y a mirar el impacto en las personas de la comunidad.",
  ["Evaluar un plan es comparar lo que se hizo con lo que se había propuesto, para mejorar. Se usan indicadores, que son datos que muestran el avance. Un indicador de eficiencia mide cuánto se logra con los recursos usados, como el costo por kilo de verdura. Un indicador de impacto mide qué cambió en las personas, como cuántas familias participaron.",
   "Ser eficiente no es gastar poco, sino lograr más con lo que se tiene. El costo por unidad se calcula dividiendo el gasto total por lo logrado. Si el huerto gastó $240.000 y produjo 600 kilos, el costo por kilo es 240.000 dividido en 600, es decir $400. Se compara con la meta o con otra alternativa para saber si fue un buen uso del dinero.",
   "Evaluar también significa reconocer lo que no estaba en el plan, como horas extra de trabajo. Se anota, se agradece y se corrige la próxima vez. Una evaluación honesta muestra tanto los logros como los problemas, y se comparte con la comunidad. Los números de esta clase son de ejemplo."],
  [("indicador", "dato que muestra el avance o el resultado"), ("eficiencia", "lograr más con los mismos recursos"), ("costo por unidad", "gasto total dividido por lo logrado"), ("impacto", "cambio que el proyecto produce en las personas o en el entorno")],
  [("Costo por kilo", "El huerto gastó $240.000 y produjo 600 kg. ¿Cuál es el costo por kilo?", ["Se divide el gasto por los kilos.", "240.000 dividido en 600."], "$400 por kilo"),
   ("Comparar con la meta", "La meta era 500 kg y se lograron 600 kg. ¿Se cumplió?", ["Se compara el resultado con la meta.", "600 es mayor que 500."], "Sí, se superó la meta")],
  [("Evaluar solo lo que salió bien.", "Se esconden los problemas para evitar críticas.", "Anota logros y problemas por igual."),
   ("Creer que gastar menos siempre es ser más eficiente.", "Se mira el gasto sin mirar lo logrado.", "La eficiencia relaciona el gasto con lo que se logró.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿qué es un indicador?", "Un dato que muestra el avance o el resultado", "Una opinión sin números", "Un permiso", "Permite medir con un número qué se logró en el proyecto."),
   ("=", "{F} ¿Cuánto suman los gastos del año? Suma 60.000, 120.000 y 60.000.", "60000+120000+60000", "Se suman semillas, herramientas y agua.", " pesos"),
   ("=", "{F} ¿Cuál es el costo por kilo producido?", "240000//600", "Se divide el gasto total por los kilos obtenidos.", " pesos"),
   ("=", "{F} ¿Cuál es el costo por familia participante?", "240000//40", "Se divide el gasto total por las familias del huerto.", " pesos"),
   ("abc", "{F} ¿Se cumplió la meta de kilos?", "Sí, se produjeron 600 kg y la meta era 500", "No, se produjeron menos", "No se puede saber", "600 kg supera los 500 kg del plan."),
   ("abc", "{F} ¿Se cumplió la meta de familias participantes?", "No, participaron 40 y la meta era 50", "Sí, participaron más de 50", "Sí, justo 50", "40 es menor que 50 y faltan 10 familias."),
   ("=", "{F} ¿Cuántas familias faltaron para la meta?", "50-40", "Se resta lo logrado a la meta.", " familias"),
   ("abc", "¿Qué indicador mide eficiencia?", "Costo por kilo producido", "Número de afiches", "Color del huerto", "Relaciona el gasto con lo logrado."),
   ("abc", "¿Qué indicador mide impacto en la comunidad?", "Número de familias que participaron", "Precio de la semilla", "Largo de la cerca", "Muestra a cuántas personas llegó el proyecto."),
   ("ab", "Si el costo por kilo baja de $400 a $300 produciendo lo mismo, el proyecto es", "más eficiente", "menos eficiente", "Se logra lo mismo con menos dinero."),
   ("abc", "El voluntario nota 40 horas extra no previstas. ¿Qué conviene hacer?", "Anotarlas y considerarlas en el próximo plan", "Ignorarlas", "Ocultarlas", "Una evaluación honesta incluye lo no previsto."),
   ("abc", "Una persona dice: «el proyecto fue un fracaso porque no llegamos a las 50 familias». ¿Qué respuesta es más equilibrada?", "Superó la meta de kilos y no la de familias; conviene ver por qué", "Todo salió perfecto", "No se puede evaluar", "Mira logros y brechas por separado."),
   ("abc", "Un grupo quiere compartir la evaluación con la comunidad. ¿Qué incluye?", "Logros, problemas y propuestas de mejora", "Solo los logros", "Solo los problemas", "Una evaluación completa informa con honestidad.")],
  ("=", "Una persona ficticia organizó una feria de trueque con gastos de $90.000 y la asistencia de 150 personas. ¿Cuál es el costo por persona asistente? (Cifras de ejemplo.)", "90000//150", "Se divide el gasto total por las personas asistentes.", " pesos"),
  [("En Emprendimiento y Empleabilidad: ¿qué es eficiencia?", "Lograr más con los mismos recursos", "Relaciona el logro con el gasto."),
   ("¿Cómo se calcula el costo por unidad?", "Gasto total dividido por lo logrado", "Permite comparar proyectos distintos con una misma medida."),
   ("¿Qué es el impacto?", "El cambio que el proyecto produce en las personas o el entorno", "Va más allá del dinero gastado.")],
  ("{F} Escribe una evaluación breve: dos logros, un problema, un indicador de eficiencia con su cálculo y un indicador de impacto. Termina con una propuesta de mejora.",
   "Logros: 600 kg y 40 familias. Problema: 40 horas extra no previstas. Eficiencia: $400 por kilo. Impacto: 40 familias. Mejora: invitar a 10 familias más y prever las horas extra.",
   ["nombra dos logros y un problema", "calcula un indicador de eficiencia", "nombra un indicador de impacto", "propone una mejora"],
   ["texto breve con cinco partes"],
   ["no mencionar problemas", "calcular el costo dividiendo al revés"],
   "Verifica la división. Si no hay problemas, pregunta qué no salió como estaba previsto."),
  "Escribe un indicador de eficiencia y uno de impacto para una feria de trueque.",
  "Calcula el costo por familia si el huerto gasta $240.000 y participan 48 familias.")

# ====================================================== OAD-08 clase 2
F = ("Ficha 11 (alternativas ficticias, cifras de ejemplo). Un grupo compara dos alternativas para un taller. "
     "Alternativa A: inversión inicial $300.000; ingresos mensuales $200.000; costos mensuales $150.000. "
     "Alternativa B: inversión inicial $180.000; ingresos mensuales $120.000; costos mensuales $100.000. "
     "La ganancia mensual es ingresos menos costos. El tiempo de recuperación es la inversión dividida por la ganancia mensual.")
K(O8, 2, F,
  "Hoy aprenderé a evaluar financieramente un plan: calcular la ganancia mensual, el tiempo de recuperación de la inversión y a comparar alternativas con eficiencia.",
  ["La evaluación financiera responde si un plan se paga solo. La ganancia mensual es lo que queda cada mes después de pagar los costos. La inversión inicial se recupera con esas ganancias. El tiempo de recuperación se calcula dividiendo la inversión por la ganancia mensual. Si la inversión es $300.000 y la ganancia $50.000, se recupera en 6 meses.",
   "Para comparar alternativas se calculan los mismos indicadores en todas. No siempre gana la de mayor ganancia: puede ser que exija más inversión y se recupere más lento. También importan el riesgo, porque una alternativa con inversión alta es más peligrosa si algo sale mal, y los efectos sobre las personas, que se ven en la evaluación social.",
   "Un buen uso de los recursos financieros busca eficiencia, es decir, mayor beneficio con menor gasto, sin dañar a nadie. Los números ayudan, pero la decisión se toma mirando también lo que no se mide en dinero. Las cifras de esta clase son de ejemplo; en una decisión real se verifican con datos reales y con apoyo de una persona experta."],
  [("ganancia mensual", "ingresos menos costos de un mes"), ("tiempo de recuperación", "meses que tarda la ganancia en cubrir la inversión"), ("alternativa", "una de las opciones que se comparan"), ("evaluación financiera", "análisis de si un plan se paga y cuánto deja")],
  [("Ganancia mensual", "Un plan tiene ingresos de $200.000 y costos de $150.000. ¿Cuál es la ganancia mensual?", ["Se restan los costos de los ingresos.", "200.000 menos 150.000."], "$50.000"),
   ("Tiempo de recuperación", "La inversión es $300.000 y la ganancia mensual es $50.000. ¿En cuántos meses se recupera?", ["Se divide la inversión por la ganancia.", "300.000 dividido en 50.000."], "6 meses")],
  [("Elegir la alternativa solo por la mayor ganancia mensual.", "No se mira cuánto cuesta ni cuánto riesgo tiene.", "Compara también la inversión y el tiempo de recuperación."),
   ("Dividir la ganancia por la inversión.", "Se invierte el orden de la división.", "Divide la inversión por la ganancia mensual.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿qué es el tiempo de recuperación?", "Los meses que tarda la ganancia en cubrir la inversión", "Los meses que dura un contrato", "El tiempo de entrega de un pedido", "Mide cuánto demora el plan en pagarse."),
   ("=", "{F} ¿Cuál es la ganancia mensual de la alternativa A?", "200000-150000", "Se restan los costos mensuales de los ingresos de A.", " pesos"),
   ("=", "{F} ¿Cuál es la ganancia mensual de la alternativa B?", "120000-100000", "Se restan los costos mensuales de los ingresos de B.", " pesos"),
   ("=", "{F} ¿En cuántos meses se recupera la inversión de A?", "300000//50000", "Se divide la inversión de A por su ganancia mensual.", " meses"),
   ("=", "{F} ¿En cuántos meses se recupera la inversión de B?", "180000//20000", "Se divide la inversión de B por su ganancia mensual.", " meses"),
   ("abc", "{F} ¿Qué alternativa se recupera más rápido?", "La A, con 6 meses", "La B, con 9 meses", "Ninguna se recupera", "A tarda menos meses que B en cubrir su inversión."),
   ("abc", "{F} ¿Qué alternativa necesita menos inversión inicial?", "La B, con $180.000", "La A, con $300.000", "Las dos iguales", "El monto de 180.000 es menor que el de 300.000."),
   ("ab", "{F} Si el grupo teme perder dinero y no puede asumir una pérdida alta, puede preferir", "la B, porque arriesga menos dinero al comenzar", "la A, porque deja más ganancia", "Menor inversión significa menor pérdida si algo sale mal."),
   ("abc", "{F} En un año, ¿cuánta ganancia acumula la alternativa A, sin contar la inversión?", "$600.000", "$240.000", "$300.000", "Son 12 meses de ganancia de $50.000 cada uno."),
   ("abc", "Una persona dice: «la alternativa con más ganancia siempre es mejor». ¿Qué respuesta es más acertada?", "No necesariamente: también importan la inversión y el riesgo", "Sí, siempre", "No, porque la ganancia no importa", "La decisión considera varios criterios además de la ganancia."),
   ("abc", "Una alternativa se recupera en 6 meses, pero depende de un cliente que puede irse. ¿Qué debería considerar el grupo?", "El riesgo de perder a ese cliente", "Que no hay ningún riesgo", "Solo el nombre del cliente", "Depender de un solo cliente aumenta el riesgo."),
   ("ab", "Una evaluación financiera con datos reales debe revisarse con", "datos verificados y apoyo de una persona experta", "números inventados", "Las decisiones reales necesitan información comprobable."),
   ("abc", "La alternativa B sube sus costos mensuales a $110.000. ¿Qué pasa con su ganancia mensual?", "Baja a $10.000", "Sube a $30.000", "No cambia", "Se restan costos mayores de los mismos ingresos.")],
  ("abc", "Una persona adulta ficticia compara un puesto de feria con inversión de $60.000 y ganancia mensual de $20.000 con otro de inversión de $90.000 y ganancia de $45.000. ¿Cuál se recupera más rápido?", "El segundo: 2 meses frente a 3 meses", "El primero: 2 meses frente a 3 meses", "Los dos iguales", "90.000 dividido en 45.000 es 2, y 60.000 dividido en 20.000 es 3."),
  [("En Emprendimiento y Empleabilidad: ¿cómo se calcula la ganancia mensual?", "Ingresos menos costos del mes", "Es lo que queda después de pagar."),
   ("En Emprendimiento y Empleabilidad: ¿Cómo se calcula el tiempo de recuperación?", "Inversión dividida por ganancia mensual", "Muestra en cuántos meses se paga el plan."),
   ("¿Qué más importa además de la ganancia?", "La inversión, el riesgo y los efectos sobre las personas", "La decisión considera varios criterios además de la ganancia.")],
  ("{F} Cambia una cifra de la alternativa B para que se recupere en 6 meses o menos (por ejemplo, ingresos o costos). Escribe tu cambio, la nueva ganancia mensual, el nuevo tiempo de recuperación y un riesgo del cambio.",
   "Subo los ingresos de B a $150.000: ganancia $50.000 y recuperación 180.000 dividido en 50.000, 3,6 meses, o sea 4 meses. Riesgo: que los clientes no acepten pagar más.",
   ["propone un cambio concreto", "calcula la nueva ganancia", "calcula el tiempo de recuperación", "nombra un riesgo"],
   ["cambio, dos cálculos y un riesgo"],
   ["calcular la recuperación con la ganancia anterior", "no nombrar riesgos"],
   "Revisa que use la ganancia nueva. Si el cambio es poco realista, pregunta cómo se lograría."),
  "Calcula la ganancia mensual de un plan con ingresos de $90.000 y costos de $60.000.",
  "Escribe cuándo preferirías una alternativa que se recupera más lento pero arriesga menos dinero.")

# ====================================================== OAD-08 clase 3
F = ("Ficha 12 (caso ficticio, cifras de ejemplo). Un taller de reciclaje de cartón en un barrio evaluó su primer año con una consulta a 60 vecinos. "
     "Resultados: 45 vecinos dicen que el taller mejoró la limpieza; 12 vecinos dicen que el ruido de las máquinas molesta en la tarde (algunos de ellos también dicen lo de la limpieza); 8 vecinos no conocen el taller y no opinaron. "
     "Además: el taller emplea a 5 personas (3 mujeres y 2 hombres) y 2 de ellas son mayores de 55 años. "
     "Herramientas posibles: H1 planilla con gráfico de barras, H2 formulario en línea, H3 presentación para la junta de vecinos.")
K(O8, 3, F,
  "Hoy aprenderé a evaluar el impacto de un plan en las comunidades, a usar herramientas tecnológicas para analizar y presentar resultados, y a decidir ajustes con criterios sociales.",
  ["El impacto de un proyecto es lo que cambia en las personas y el entorno, para bien o para mal. Un taller puede mejorar la limpieza y dar empleo, pero también producir ruido. Evaluar el impacto es preguntarse quién se beneficia, quién se perjudica y si alguien queda fuera. Se consulta a las personas de la comunidad, y se miran los resultados en números y en opiniones.",
   "Las herramientas tecnológicas ayudan a analizar. Una planilla con un gráfico de barras permite ver rápido qué opinión predomina. Un formulario en línea recoge opiniones, y una presentación muestra los resultados a la junta de vecinos. Si no hay computador, se hace en papel y con reuniones. Se cuidan los datos personales: se presentan resultados agrupados, sin nombres.",
   "Con los resultados se decide: mantener lo que funciona, corregir lo que perjudica y agregar lo que falta. Un buen plan incluye ajustes con las personas afectadas: por ejemplo, cambiar el horario del ruido y avisar a quienes no conocen el taller. También se mira la diversidad de quienes participan o trabajan, para que no queden fuera personas por edad, género u otra condición."],
  [("impacto social", "efecto del proyecto sobre las personas de la comunidad"), ("gráfico de barras", "dibujo que compara cantidades con barras de distinta altura"), ("ajuste", "cambio para corregir o mejorar el plan"), ("comunidad", "personas que viven o trabajan en un mismo lugar y se relacionan")],
  [("Leer resultados", "45 de 60 vecinos dicen que el taller mejoró la limpieza. ¿Es la mayoría?", ["La mitad de 60 es 30.", "45 es mayor que 30."], "Sí, es la mayoría de los consultados"),
   ("Decidir un ajuste", "12 vecinos dicen que el ruido molesta en la tarde. ¿Qué ajuste es razonable?", ["El problema es el horario.", "Cambiar las máquinas ruidosas a la mañana y conversar con quienes se quejaron."], "Cambiar el horario de las máquinas ruidosas")],
  [("Ignorar a la minoría que se queja.", "Se piensa que solo importa lo que dice la mayoría.", "También se escuchan los perjuicios, aunque afecten a menos personas."),
   ("Mostrar nombres de quienes opinaron en la presentación.", "Se olvida proteger sus datos.", "Presenta resultados agrupados, sin nombres.")],
  [("abc", "En Emprendimiento y Empleabilidad: ¿qué es el impacto social de un proyecto?", "El efecto del proyecto sobre las personas de la comunidad", "El costo total del proyecto", "El tamaño del local", "Mira cómo cambia la vida de las personas."),
   ("=", "{F} ¿Cuántos vecinos mencionaron el ruido o no conocen el taller? Suma 12 y 8.", "12+8", "Quienes se quejan del ruido conocen el taller, así que no se repiten con los 8 que no lo conocen: 12 + 8 = 20.", " vecinos"),
   ("=", "{F} ¿Cuántos vecinos no dicen que mejoró la limpieza? Resta 45 del total de 60.", "60-45", "Se resta quienes sí lo dicen del total consultado.", " vecinos"),
   ("abc", "{F} ¿Qué impacto positivo muestra la consulta?", "La mayoría dice que mejoró la limpieza", "Nadie conoce el taller", "Todos están molestos", "45 de 60 vecinos reportan ese beneficio."),
   ("abc", "{F} ¿Qué impacto negativo muestra la consulta?", "Que el ruido molesta a 12 vecinos en la tarde", "Que mejoró la limpieza", "Que hay 5 personas empleadas", "Es un perjuicio para una parte de la comunidad."),
   ("abc", "{F} ¿Qué ajuste atiende a los 8 vecinos que no conocen el taller?", "Informar con avisos y una visita abierta", "No hacer nada", "Cerrar el taller", "El desconocimiento se corrige informando a los vecinos del sector."),
   ("abc", "{F} ¿Qué herramienta ayuda a comparar rápido las opiniones de los vecinos?", "Una planilla con un gráfico de barras", "Un afiche sin números", "Una lista con los nombres de los vecinos", "El gráfico muestra de un vistazo qué opinión predomina."),
   ("ab", "{F} Para recoger la opinión de quienes no usan internet, conviene", "preguntar en persona y anotar con su permiso", "no consultarlos", "Un método accesible incluye a más personas."),
   ("abc", "{F} Respecto de la diversidad en el equipo, ¿qué dato de la ficha es relevante?", "Que trabajan 3 mujeres, 2 hombres y 2 personas mayores de 55 años", "Que el taller es de cartón", "Que hay 60 vecinos", "Muestra que el equipo incluye distintas edades y géneros."),
   ("abc", "Un grupo presenta resultados con los nombres de quienes se quejaron del ruido. ¿Qué problema hay?", "Se exponen datos personales sin permiso", "Es más transparente y no hay problema", "Se ahorra tiempo", "Los resultados se agrupan sin identificar."),
   ("abc", "Una persona dice: «solo 12 se quejaron, no importa». ¿Qué respuesta es más adecuada?", "Un perjuicio a 12 vecinos merece atención y un ajuste", "Tiene razón", "Hay que cerrar el taller", "El impacto negativo, aunque afecte a menos personas, se atiende."),
   ("ab", "Un buen plan de mejora después de la evaluación incluye", "ajustes acordados con las personas afectadas", "decisiones tomadas sin conversar", "Conversar con las personas afectadas mejora las soluciones."),
   ("abc", "Después de cambiar el horario del ruido, ¿qué debería hacer el grupo?", "Volver a consultar para ver si el problema se resolvió", "No volver a consultar nunca", "Esconder los resultados", "Evaluar de nuevo permite comprobar si el ajuste funcionó.")],
  ("abc", "Una persona adulta ficticia evalúa un servicio de reparto de pan a personas mayores. Los resultados muestran que la mayoría está satisfecha, pero a algunas personas el reparto llega tarde. ¿Qué es lo más adecuado?", "Mantener lo que funciona y corregir la hora de reparto con ayuda de quienes recibieron tarde", "Ignorar a quienes reciben tarde", "Cerrar el servicio", "Un buen ajuste conserva lo bueno y corrige lo que perjudica."),
  [("En Emprendimiento y Empleabilidad: ¿qué es un ajuste?", "Un cambio para corregir o mejorar el plan", "Se hace después de evaluar los resultados del plan."),
   ("En Emprendimiento y Empleabilidad: ¿Para qué sirve un gráfico de barras?", "Para comparar cantidades de un vistazo", "Facilita presentar resultados de manera clara a otras personas."),
   ("¿Cómo se protegen los datos de quienes opinan?", "Presentando resultados agrupados, sin nombres", "Evita exponerlos a otras personas sin su permiso.")],
  ("{F} Escribe una evaluación de impacto con un impacto positivo, un impacto negativo, un ajuste concreto, una herramienta tecnológica para presentar los resultados y una forma de consultar a quienes no usan internet.",
   "Positivo: 45 de 60 vecinos notan más limpieza. Negativo: 12 sienten ruido en la tarde. Ajuste: usar las máquinas ruidosas en la mañana. Herramienta: presentación con un gráfico de barras. Consulta: conversar en la sede de la junta.",
   ["nombra un impacto positivo y uno negativo con datos", "propone un ajuste concreto", "elige una herramienta con razón", "incluye una forma accesible de consulta"],
   ["texto breve con cinco partes"],
   ["no usar los datos de la ficha", "proponer un ajuste que no resuelve el perjuicio"],
   "Comprueba que el ajuste atienda el perjuicio nombrado. Si no pensó en quienes no usan internet, pregunta cómo los incluiría."),
  "Escribe dos preguntas para consultar a una comunidad sobre el impacto de un taller.",
  "Escribe cómo explicarías a la junta de vecinos los resultados de la consulta en tres frases.")
