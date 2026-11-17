"""Interpretación musical 3.º y 4.º medio HC: OAC-07 (relacionar habilidades y conocimientos de la asignatura con contextos laborales, profesionales y de desarrollo personal, a partir de investigaciones). Perfiles y cifras de ejemplo, inventados."""
from __future__ import annotations

from hc_imus_common import build

O7 = "AR-IMUS-3y4-OAC-07"

# ============================================================ OAC-07, clase 1
F = ("Ficha 1 (perfiles de ejemplo, inventados; las personas y las instituciones reales las aporta tu docente o una investigación tuya). "
     "Perfil 1, intérprete de un conjunto: ensaya 3 veces por semana, mantiene el pulso con el grupo, se escucha con las demás partes y maneja los nervios antes de presentar. "
     "Perfil 2, docente de música en un taller: planifica clases, explica con ejemplos, escucha las ideas de cada estudiante y adapta la actividad al grupo. "
     "Perfil 3, técnico de sonido en eventos: prueba los equipos, equilibra el nivel de cada voz e instrumento, cuida el oído del público y resuelve fallas con un plan B. "
     "Perfil 4, productora de eventos culturales: arma el programa con tiempos, coordina personas, calcula costos y comunica con claridad. "
     "Habilidades trabajadas en esta asignatura: pulso compartido, ensamble, bitácora de ensayo, guion de presentación, plan B, evaluación con evidencia.")
build(
    O7, 1, F,
    use="Aprenderé a reconocer oficios y roles ligados a la interpretación musical y a relacionar las habilidades de esta asignatura (pulso, ensamble, bitácora, guion, evaluación) con contextos laborales, profesionales y personales.",
    prior=["Conozco las habilidades de ensayo y presentación.", "Sé evaluar con evidencia.", "Sé que el cuidado del cuerpo es parte del trabajo."],
    explain=[
        "La interpretación musical no se trabaja solo en el escenario. Alrededor de una presentación hay muchos oficios y roles: quien interpreta, quien enseña música, quien opera el sonido, quien organiza el evento, quien dirige un coro o un conjunto. Cada uno usa habilidades que se pueden entrenar en esta asignatura. Reconocer esos vínculos ayuda a imaginar caminos posibles después del colegio, sin que ninguno sea obligatorio ni «mejor» que otro.",
        "Una habilidad es algo que se hace bien gracias al entrenamiento. El pulso compartido y la escucha del ensamble sirven a quien interpreta y a quien dirige. La bitácora y la evaluación con evidencia sirven a quien enseña y a quien produce. El guion y el plan B sirven a quien presenta y a quien organiza. Algunas habilidades también sirven para el desarrollo personal: la constancia, el manejo de los nervios, el trabajo en equipo y el cuidado de la salud valen en cualquier ámbito de la vida.",
        "Para relacionar habilidades con contextos se arma una tabla de tres columnas: la habilidad, la evidencia de que la tengo (algo que hice en clase) y el contexto donde serviría. Con esa tabla se evita decir «sirvo para todo» o «no sirvo para nada»: se mira lo que de verdad se ha practicado. Los datos reales de cada oficio los investigas con fuentes o con una persona que lo ejerza; aquí se trabaja con perfiles inventados.",
    ],
    vocab=[("oficio", "trabajo que se ejerce con conocimientos y práctica"), ("rol", "tarea que una persona asume en un proyecto o en un trabajo"), ("habilidad", "capacidad que se mejora con entrenamiento"),
           ("contexto laboral", "lugar o situación donde se ejerce un trabajo"), ("desarrollo personal", "crecimiento de la persona en su forma de aprender y convivir"), ("evidencia", "algo que hice que muestra que tengo la habilidad")],
    worked=[
        ("Relacionar habilidad y rol", "Un perfil de ejemplo dirige un coro: marca las entradas, cuida que todas las voces mantengan el pulso y escucha el equilibrio entre ellas. ¿Qué habilidades de esta asignatura usa?",
         ["Marcar entradas y mantener el pulso se practica en el ensamble, con pulso compartido y entradas claras.", "Escuchar el equilibrio se practica al ajustar la fuerza de cada parte."],
         "Pulso compartido, entradas claras y equilibrio del ensamble"),
        ("Armar una fila de la tabla", "Una estudiante escribió una bitácora de ensayo todas las semanas. ¿Qué fila de la tabla puede armar?",
         ["Habilidad: registrar y evaluar un proceso. Evidencia: su bitácora de ensayo semanal.", "Contexto: sirve para enseñar, producir o dirigir, porque entrega datos para mejorar."],
         "Registrar un proceso; evidencia: bitácora semanal; contexto: enseñar o producir"),
    ],
    mistakes=[("Pensar que solo existe un camino laboral para la música: ser intérprete en un escenario.", "Se ignoran los oficios que rodean a una presentación.", "Reconoce al menos cuatro roles y las habilidades de cada uno."),
              ("Decir «tengo la habilidad» sin ninguna evidencia.", "No se sabe en qué se apoya.", "Anota algo concreto que hiciste, como una bitácora o una presentación.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una habilidad?', 'Una capacidad que se mejora con entrenamiento', 'Un instrumento que se compra para tocar mejor', 'Un diploma que entrega un liceo al terminar', 'Una habilidad se entrena; no es un objeto ni un diploma.'),
        ('abc', '{F} ¿Qué hace el técnico de sonido según la ficha?', 'Prueba equipos y equilibra el nivel de cada voz', 'Planifica clases y explica ejemplos al grupo', 'Calcula los costos y arma el programa del evento', 'La ficha asigna al perfil 3 probar equipos y equilibrar niveles.'),
        ('abc', '{F} ¿Qué perfil planifica clases y adapta la actividad al grupo?', 'El docente de música de un taller', 'El intérprete de un conjunto estable', 'La productora de eventos culturales', 'El perfil 2 es el que planifica y adapta las clases.'),
        ('abc', '{F} ¿Qué habilidad del perfil 1 se entrena con el pulso compartido y el ensamble?', 'Escucharse con las demás partes del grupo', 'Calcular los costos de un evento cultural', 'Probar los equipos de sonido antes de un acto', 'El pulso compartido y el ensamble se relacionan con escucharse.'),
        ('=', '{F} El perfil 1 ensaya 3 veces por semana. ¿Cuántos ensayos hace en 6 semanas?', '3*6', 'Se multiplican los ensayos semanales por las semanas.', ' ensayos'),
        ('abc', '{F} ¿Qué habilidad de esta asignatura se parece más a «arma el programa con tiempos» de la productora?', 'Armar un programa con tiempos y pausas', 'Escribir una crítica con afirmación y razón', 'Reconocer sesgos al juzgar una obra', 'Armar el programa con tiempos corresponde a la gestión del programa.'),
        ('abc', '{F} ¿Qué habilidad de esta asignatura se parece a «resuelve fallas con un plan B» del técnico?', 'Preparar un plan B para un recurso que falle', 'Hacer una autoevaluación con un plan de mejora', 'Analizar los elementos del lenguaje musical', 'Resolver fallas con un plan B es lo que se practica con el plan B de la presentación.'),
        ('=', '{F} La productora arma un programa con 4 piezas de 3 minutos y 3 pausas de 1 minuto. ¿Cuántos minutos dura?', '4*3+3*1', 'Se suman las cuatro piezas y las tres pausas entre ellas.', ' minutos'),
        ('abc', '{F} Una estudiante dice: «la bitácora me sirve para enseñar o para producir, porque da datos para mejorar». ¿Qué observación es correcta?', 'Es válido, porque registrar un proceso sirve en varios roles', 'Es incorrecto, porque la bitácora solo sirve a quien interpreta', 'Es incorrecto, porque la bitácora no entrega ningún dato útil', 'Registrar un proceso es una habilidad que sirve a varios roles.'),
        ('abc', '{F} ¿Qué habilidad de desarrollo personal se parece a «maneja los nervios antes de presentar»?', 'Manejar la tensión antes de presentar', 'Calcular los costos de un evento de varias personas del grupo', 'Operar los niveles de sonido de un evento grande y con público', 'Manejar los nervios sirve en cualquier situación con exigencia.'),
        ('abc', '{F} Una estudiante afirma «tengo habilidad para dirigir» sin decir nada más. ¿Qué le falta a esa afirmación?', 'Una evidencia, como haber coordinado un ensayo', 'Más años de estudio antes de poder afirmar algo así de sí misma', 'Una opinión de otra persona sobre sus gustos musicales de siempre', 'Una afirmación sobre la propia habilidad se apoya en algo que se hizo.'),
        ('abc', '{F} Un estudiante dice que «solo vale la pena ser intérprete en un escenario». ¿Qué respuesta es correcta?', 'Hay varios roles con habilidades relacionadas', 'Tiene razón, porque los demás roles no usan música en su trabajo diario', 'Tiene razón, porque un escenario es el único contexto posible para la música', 'Los perfiles muestran varios caminos posibles con habilidades en común.'),
        ('=', '{F} Una persona pasa 12 horas semanales en clases de música y 6 en preparación. ¿Cuántas horas suma en una semana?', '12+6', 'Se suman las horas de clases y las horas de preparación.', ' horas'),
    ],
    ctx=('abc', 'Tu grupo organiza un acto de cierre y tú propones encargarte de probar el sonido y tener un plan B. ¿Qué rol y habilidad estás practicando?', 'Técnico de sonido: preparación previa y plan B', 'Intérprete de un conjunto: manejar los nervios antes de tocar', 'Docente: planificar clases con ejemplos para el grupo', 'Probar el sonido y tener un plan B son tareas propias del técnico de sonido.'),
    sc=[
        ("En Interpretación musical: ¿qué es un rol?", "La tarea que una persona asume en un proyecto o trabajo", "Los roles distribuyen tareas en un trabajo."),
        ('abc', 'Una habilidad se demuestra con:', 'Una evidencia de algo que hiciste', 'Una promesa de que la tienes en el futuro', 'Una lista de gustos musicales de tu curso', 'La evidencia muestra que la habilidad existe.'),
        ("¿Por qué la constancia es una habilidad de desarrollo personal?", "Porque sirve en cualquier ámbito, no solo en la música", "La constancia se entrena ensayando y se usa en toda la vida."),
    ],
    op=("Con la {F}, arma una tabla de tres filas: habilidad, evidencia (algo que hiciste en esta asignatura o en tu vida escolar) y contexto laboral o personal donde serviría. Usa al menos dos perfiles distintos de la ficha.",
        "Fila 1: habilidad, mantener el pulso con el grupo; evidencia, tocar en un ensamble en clase; contexto, intérprete de un conjunto. Fila 2: habilidad, registrar un proceso; evidencia, mi bitácora de ensayo; contexto, docente o productora. Fila 3: habilidad, manejar los nervios; evidencia, presentar ante el curso; contexto, cualquier situación con exigencia.",
        ["escribe tres habilidades distintas", "da una evidencia real para cada una", "nombra un contexto para cada una", "usa al menos dos perfiles de la ficha"],
        ["hoja con la tabla de tres filas"],
        ["decir una habilidad sin evidencia", "repetir el mismo contexto", "inventar datos sobre un oficio real"],
        "Pregunta: «¿qué hiciste que muestre esa habilidad?». Si no lo dice, pídele que recuerde una actividad concreta."),
    reinforce="Escribe dos roles que rodean una presentación y una habilidad de esta asignatura que sirva a cada uno.",
    extend="Explica por qué una habilidad como la escucha puede servir en un oficio que no es musical.",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 2 (investigación de ejemplo, inventada) sobre tres trayectorias. Los datos son de ejemplo para practicar el método; los datos reales los investigas con tu docente y con fuentes. "
     "Trayectoria A, docente de música en un taller: 12 horas semanales de clases y 6 de preparación; formación de ejemplo: estudios en educación y práctica con grupos. "
     "Trayectoria B, técnico de sonido en eventos: 3 eventos al mes de 6 horas cada uno; formación de ejemplo: cursos de sonido y práctica con ayudantes. "
     "Trayectoria C, intérprete independiente: 2 ensayos semanales de 3 horas y 2 presentaciones al mes de 2 horas; formación de ejemplo: práctica constante y talleres. "
     "Fuentes de ejemplo: F1, entrevista a una persona que ejerce el oficio; F2, sitio de una institución de formación; F3, comentario anónimo en un foro. "
     "Preguntas de entrevista de ejemplo: ¿cómo es un día de trabajo? ¿qué formación necesitaste? ¿qué cuidados de salud tienes?")
build(
    O7, 2, F,
    use="Aprenderé a investigar un contexto laboral o profesional: formular preguntas, elegir fuentes confiables, registrar datos con su origen y comparar trayectorias con evidencia.",
    prior=["Sé reconocer roles y habilidades.", "Sé distinguir fuentes primarias y opiniones anónimas.", "Sé registrar datos con su fuente."],
    explain=[
        "Investigar un contexto laboral sirve para decidir con información y no con suposiciones. Se empieza con una pregunta clara y respondible: «¿cuántas horas semanales suele trabajar una persona que enseña música en un taller?». Luego se eligen fuentes: la entrevista a alguien que ejerce el oficio es una fuente primaria; el sitio de una institución de formación informa sobre estudios; un comentario anónimo en un foro es una fuente débil porque no se sabe quién habla.",
        "Una buena entrevista tiene pocas preguntas abiertas: cómo es un día de trabajo, qué formación necesitó, qué cuidados de salud tiene, qué consejo daría. Se pide permiso para anotar o grabar, se agradece y se respeta lo que la persona no quiere contar. No se piden datos personales ni de otras personas. Los datos se anotan con su fuente en una tabla, y si dos fuentes difieren, se registran ambas y se busca una tercera.",
        "Para comparar trayectorias se eligen criterios: horas semanales, formación, cuidados de salud, tipo de trabajo (estable o por eventos). Se calculan los datos que se pueden calcular y se anotan los que dependen de la persona. La comparación no decide por nadie qué camino es mejor: muestra qué requiere cada uno, para que cada persona elija con información y según sus intereses.",
    ],
    vocab=[("trayectoria", "camino de estudio y trabajo que sigue una persona"), ("fuente primaria", "fuente que viene de quien ejerce el oficio"), ("pregunta abierta", "pregunta que se responde con una explicación y no con sí o no"),
           ("criterio de comparación", "aspecto elegido para comparar trayectorias"), ("permiso", "aceptación de la persona entrevistada para anotar o grabar"), ("dato de ejemplo", "dato inventado para practicar el método")],
    worked=[
        ("Calcular horas semanales", "Una trayectoria de ejemplo tiene 10 horas de clases y 5 de preparación por semana. ¿Cuántas horas trabaja en 4 semanas?",
         ["Por semana son 10 + 5 = 15 horas.", "En 4 semanas son 15 × 4 = 60 horas."],
         "60 horas"),
        ("Elegir una fuente", "Para saber cómo es un día de trabajo de un técnico de sonido, ¿qué fuente conviene entre una entrevista a un técnico y un comentario anónimo?",
         ["La entrevista viene de quien ejerce el oficio y se sabe quién habla.", "El comentario anónimo no permite saber en qué se apoya."],
         "La entrevista, porque es una fuente primaria"),
    ],
    mistakes=[("Entrevistar con preguntas de sí o no que no dejan explicar.", "Se obtienen poca información y datos poco útiles.", "Haz preguntas abiertas, como «¿cómo es un día de trabajo?»."),
              ("Anotar datos sin decir de qué fuente vienen.", "No se pueden revisar ni contrastar.", "Escribe cada dato con su fuente y su tipo.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una pregunta abierta?', 'Una pregunta que se responde con una explicación', 'Una pregunta que se responde solo con sí o con no', 'Una pregunta que no tiene ninguna respuesta posible', 'La pregunta abierta invita a explicar; la cerrada se responde con sí o no.'),
        ('abc', '{F} ¿Cuántas horas semanales de clases tiene la trayectoria A?', '12 horas de clases por semana', '6 horas de clases por semana', '3 horas de clases por semana', 'La ficha dice 12 horas de clases y 6 de preparación.'),
        ('abc', '{F} ¿Qué fuente de la ficha es una fuente primaria?', 'F1, la entrevista a quien ejerce el oficio', 'F3, el comentario anónimo de un foro de internet musical', 'Ninguna, porque todas son fuentes secundarias de la ficha', 'La entrevista a quien ejerce el oficio es una fuente primaria.'),
        ('abc', '{F} ¿Qué fuente es la más débil para datos de la trayectoria B?', 'F3, porque no se sabe quién habla ni en qué se apoya', 'F1, porque viene de una persona que ejerce el oficio', 'F2, porque viene de una institución que forma personas', 'Un comentario anónimo no permite comprobar el dato.'),
        ('=', '{F} ¿Cuántas horas semanales suma la trayectoria A entre clases y preparación?', '12+6', 'Se suman las horas de clases y las de preparación.', ' horas'),
        ('=', '{F} La trayectoria B tiene 3 eventos al mes de 6 horas cada uno. ¿Cuántas horas trabaja al mes en eventos?', '3*6', 'Se multiplican los eventos por las horas de cada uno.', ' horas'),
        ('=', '{F} La trayectoria C tiene 2 ensayos semanales de 3 horas y 2 presentaciones al mes de 2 horas. ¿Cuántas horas al mes dedica a presentaciones?', '2*2', 'Se multiplican las presentaciones por las horas de cada una.', ' horas'),
        ('abc', '{F} ¿Qué pregunta de entrevista es abierta?', '¿Cómo es un día de trabajo?', '¿Te gusta tu trabajo, sí o no, de verdad?', '¿Trabajas todos los días de la semana, sí o no?', 'Una pregunta abierta pide explicar, como «¿cómo es un día de trabajo?».'),
        ('abc', '{F} Una persona no quiere contar cuánto gana. ¿Qué decisión respeta a la persona entrevistada?', 'Respetarlo, agradecer y pasar a otra pregunta', 'Insistir hasta que lo cuente para completar la tabla', 'Preguntarle a otra persona cuánto gana la primera', 'Una persona puede decidir qué no contar, y se respeta.'),
        ('abc', '{F} Las fuentes F1 y F2 dicen que se necesitan cursos de sonido. ¿Qué se puede decir?', 'Dos fuentes coinciden, lo que da confianza', 'El dato es falso, porque dos fuentes no pueden coincidir nunca', 'El dato es inútil, porque no viene del foro de internet', 'Dos fuentes que coinciden dan más confianza en un dato.'),
        ('abc', '{F} Un grupo escribe en su tabla «trayectoria B: poco trabajo, según un comentario del foro». ¿Qué falla?', 'Usa una fuente débil como dato confiable', 'Usa demasiadas fuentes primarias para un solo dato', 'Escribe el nombre de la trayectoria incorrectamente', 'Una opinión anónima no es un dato confiable.'),
        ('abc', '{F} Una estudiante concluye «la trayectoria A es la mejor porque tiene más horas». ¿Qué observación es correcta?', 'Más horas no significa mejor; depende de cada persona', 'Es correcto, porque más horas siempre significa un mejor trabajo para todos', 'Es incorrecto, porque las horas no se pueden comparar entre oficios distintos', 'La comparación muestra qué requiere cada camino, no cuál es mejor.'),
        ('=', '{F} Si el técnico de la trayectoria B hace 3 eventos al mes de 6 horas, ¿cuántas horas de evento hace en 4 meses?', '3*6*4', 'Se multiplican los eventos al mes, sus horas y los meses.', ' horas'),
    ],
    ctx=('abc', 'Quieres saber cómo cuida su salud auditiva un técnico de sonido. ¿Qué haces?', 'Preparar preguntas abiertas y pedir una entrevista', 'Buscar un comentario anónimo en un foro y copiarlo como dato confiable', 'Suponer la respuesta y escribirla en la tabla de datos como dato', 'Una entrevista con preguntas abiertas y permiso entrega un dato confiable.'),
    sc=[
        ("En Interpretación musical: ¿qué es una trayectoria?", "El camino de estudio y trabajo que sigue una persona", "Una trayectoria incluye formación y trabajo."),
        ('abc', 'Antes de grabar una entrevista se necesita:', 'El permiso de la persona entrevistada', 'El permiso de otro estudiante', 'Ningún permiso si es para un trabajo', 'El permiso es de la persona que habla.'),
        ("¿Por qué se anota la fuente de cada dato?", "Para poder revisarlo y contrastarlo con otra fuente", "Un dato sin fuente no se puede comprobar."),
    ],
    op=("Con la {F}, escribe: (1) tres preguntas abiertas para entrevistar a una persona de un oficio ligado a la música; (2) una tabla con los datos de horas de las tres trayectorias y su fuente de ejemplo; (3) una frase que compare dos trayectorias sin decir cuál es mejor.",
        "(1) ¿Cómo es un día de trabajo? ¿Qué formación necesitaste? ¿Qué cuidados de salud tienes? (2) A: 18 horas semanales (12 clases y 6 preparación), fuente F1. B: 18 horas al mes en eventos, fuente F1. C: 6 horas de ensayo por semana y 4 horas de presentaciones al mes, fuente F1. (3) A tiene un horario semanal estable y B trabaja por eventos, así que requieren organizaciones distintas.",
        ["escribe tres preguntas abiertas", "arma la tabla con datos y fuente", "compara sin juicios de valor", "no inventa datos fuera de la ficha"],
        ["hoja con las preguntas, la tabla y la comparación"],
        ["preguntas de sí o no", "datos sin fuente", "decir cuál es mejor"],
        "Pregunta: «¿de qué fuente viene ese dato?». Si no lo sabe, pídele que lo anote en la tabla."),
    reinforce="Escribe tres preguntas abiertas para entrevistar a una persona que enseña música y una pregunta de seguridad y cuidado de salud.",
    extend="Explica por qué dos personas que ejercen el mismo oficio pueden dar datos distintos sobre sus horas de trabajo.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 3 (mapa de habilidades y opciones de ejemplo, inventados) de Sol, estudiante que tiene 8 horas libres a la semana. "
     "Mapa de habilidades: pulso compartido, evidencia: ensayó 4 semanas con su grupo; bitácora de ensayo, evidencia: 5 entradas completas; guion y plan B, evidencia: presentó en el acto del liceo; manejo de nervios, evidencia: presentó ante el curso. "
     "Opciones para un proyecto de desarrollo personal: A, sumarse a un coro del liceo, 3 horas por semana; B, aprender a operar el sonido en eventos del liceo, 4 horas por semana; C, organizar un ciclo de presentaciones del curso, 5 horas por semana. "
     "Restricción: no más de 8 horas semanales en total y un día de descanso a la semana. "
     "Condición nueva: Sol tiene una semana de pruebas y solo puede dedicar 5 horas.")
build(
    O7, 3, F,
    use="Aprenderé a relacionar mis habilidades con contextos de desarrollo personal y laboral mediante un mapa de habilidades, a decidir entre opciones usando una restricción de tiempo y a revisar la decisión cuando cambia una condición.",
    prior=["Sé reconocer roles y habilidades.", "Sé investigar con fuentes.", "Sé revisar una decisión cuando cambia una condición."],
    explain=[
        "Un mapa de habilidades es una tabla donde cada habilidad se acompaña de la evidencia de que se tiene (algo que hice) y del contexto donde serviría. Sirve para conocerse mejor y para elegir proyectos o caminos de aprendizaje con realismo. Un mapa honesto no inventa habilidades ni las minimiza: se apoya en cosas hechas, como ensayar con un grupo, escribir una bitácora o presentar ante un curso.",
        "Para decidir entre opciones se comparan con tres preguntas. ¿Usa o desarrolla alguna habilidad del mapa? ¿Cabe en el tiempo disponible, incluido el descanso? ¿Cuida mi salud y mi bienestar? La opción que responde mejor a las tres preguntas, y que además corresponde a mi interés, es la más conveniente. No se elige solo por lo que parece más prestigioso, y se acepta que cada persona tenga prioridades distintas.",
        "Una decisión se revisa si cambia una condición. Si aparece una semana con menos tiempo, se puede reducir horas, posponer o elegir una opción más liviana, sin sentir fracaso. El desarrollo personal incluye aprender a decir «hoy no» cuando el cuerpo o la agenda lo piden. Si alguien se siente sobrepasado por el tiempo o la presión, avisa a una persona adulta de confianza.",
    ],
    vocab=[("mapa de habilidades", "tabla de habilidad, evidencia y contexto donde sirve"), ("opción", "alternativa entre las que se puede elegir"), ("restricción", "límite que la decisión debe respetar, como el tiempo"),
           ("desarrollo personal", "crecimiento en la forma de aprender, convivir y cuidarse"), ("prioridad", "lo que una persona considera más importante en ese momento"), ("revisar", "volver a mirar una decisión cuando cambian las condiciones")],
    worked=[
        ("Revisar con una restricción", "Una estudiante tiene 6 horas libres a la semana y quiere hacer una actividad de 4 horas y otra de 3. ¿Caben las dos?",
         ["Las dos suman 4 + 3 = 7 horas.", "Superan las 6 horas disponibles, así que no caben las dos juntas."],
         "No caben: suman 7 horas y tiene 6"),
        ("Relacionar evidencia y contexto", "Una estudiante presentó ante su curso y manejó los nervios. ¿Qué contexto personal o laboral puede relacionar con esa evidencia?",
         ["Presentar ante un grupo se parece a exponer en cualquier estudio o trabajo.", "Contextos: exponer un proyecto, enseñar, producir un evento."],
         "Exponer un proyecto, enseñar o producir un evento"),
    ],
    mistakes=[("Elegir la opción que parece más prestigiosa, aunque no cabe en el tiempo.", "Se ignora la restricción y el bienestar.", "Revisa tiempo, salud e interés antes de decidir."),
              ("Quedarse con la decisión inicial aunque la semana cambie.", "Se confunde constancia con rigidez.", "Revisa la decisión con la nueva condición y ajusta.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es un mapa de habilidades?', 'Una tabla de habilidad, evidencia y contexto', 'Una lista de instrumentos que una persona sabe tocar bien', 'Un plano de las salas de ensayo de un liceo de la ciudad', 'El mapa de habilidades relaciona habilidad, evidencia y contexto.'),
        ('abc', '{F} ¿Cuál es la evidencia de la habilidad «bitácora de ensayo» de Sol?', '5 entradas completas', '4 semanas de ensayo', 'Haber presentado en el acto', 'La ficha indica 5 entradas completas.'),
        ('abc', '{F} ¿Cuántas horas semanales pide la opción C?', '5 horas por semana', '3 horas por semana', '4 horas por semana', 'La opción C, organizar un ciclo de presentaciones, pide 5 horas.'),
        ('abc', '{F} ¿Qué habilidad del mapa se usa en la opción B, operar el sonido en eventos?', 'Guion y plan B, por la preparación y los imprevistos', 'Manejo de nervios, por las presentaciones ante el curso', 'Pulso compartido, por los ensayos con el grupo', 'Operar sonido requiere prever imprevistos y tener un plan B.'),
        ('=', '{F} ¿Cuántas horas suman las opciones A y B juntas?', '3+4', 'Se suman las horas semanales de las dos opciones.', ' horas'),
        ('abc', '{F} Con la restricción de 8 horas, ¿qué combinación de opciones cabe?', 'Las opciones A y B, que suman 7 horas', 'Las opciones B y C, que suman 9 horas', 'Las tres opciones, que suman 12 horas', 'A y B suman 7 horas; B y C suman 9; las tres suman 12.'),
        ('=', '{F} Si Sol elige las opciones A y B, ¿cuántas horas libres le quedan de las 8 disponibles?', '8-(3+4)', 'Se restan las horas de A y B a las 8 horas disponibles.', ' hora'),
        ('abc', '{F} ¿Cuál es la ventaja de la opción A para el bienestar de Sol, que debe manejar los nervios?', 'Practicar en un grupo estable con pocas horas por semana', 'Dedicar el máximo de horas para destacar sobre los demás', 'Evitar cualquier actividad con otras personas', 'Un coro con pocas horas semanales deja espacio para descansar.'),
        ('abc', '{F} Con la condición nueva (solo 5 horas esta semana), ¿qué decisión es razonable?', 'Elegir A o B, que dejan margen, y posponer C, que ocupa las 5 horas', 'Hacer A, B y C igual y descansar menos esa semana', 'No hacer nada en todo el mes para no atrasarse con las pruebas', 'Con 5 horas caben A o B con margen; C pide las 5 horas completas y no deja margen.'),
        ('abc', '{F} Un amigo dice a Sol: «elige C porque es lo más importante». ¿Qué respuesta es adecuada?', 'Revisar su tiempo, su salud y sus intereses', 'Aceptarlo, porque su amigo sabe qué le conviene más que ella', 'Rechazarlo sin pensar, porque nadie puede opinar sobre sus decisiones', 'La decisión se apoya en las tres preguntas y en sus propias prioridades.'),
        ('abc', '{F} Sol siente que está muy presionada por todo lo que tiene que hacer. ¿Qué decisión corresponde?', 'Reducir actividades y hablar con una persona adulta', 'Sumar una cuarta actividad para sentirse más ocupada y útil', 'Ocultar lo que siente y seguir sin cambiar nada del plan', 'Cuando la presión es grande, se reduce y se pide apoyo.'),
        ('abc', 'Una estudiante dice: «no tengo ninguna habilidad musical porque no toco un instrumento». ¿Qué observación es correcta?', 'Hay habilidades como la escucha o el plan B que no dependen de un instrumento', 'Es correcto, porque la música solo exige tocar un instrumento muy bien', 'Es incorrecto, porque todas las personas tienen todas las habilidades musicales', 'Hay muchas habilidades musicales que se pueden demostrar sin tocar un instrumento.'),
        ('=', '{F} Si Sol hace la opción B durante 6 semanas, ¿cuántas horas dedica en total?', '4*6', 'Se multiplican las horas semanales de la opción B por las semanas.', ' horas'),
    ],
    ctx=('abc', 'Un proyecto de tu curso exige 7 horas semanales, pero solo puedes dedicar 5 sin quitar descanso. ¿Qué decisión es adecuada?', 'Conversarlo con tu grupo y repartir tareas', 'Aceptarlo y dormir menos para cumplir con las 7 horas semanales', 'Abandonar el proyecto sin avisar a nadie del grupo ni al docente', 'Se ajusta el reparto de tareas y se cuida el descanso.'),
    sc=[
        ("En Interpretación musical: ¿qué es una restricción de tiempo?", "Un límite de horas que la decisión debe respetar", "La restricción acota las opciones posibles."),
        ('abc', 'Si cambia una condición de tu agenda:', 'Se revisa la decisión y se ajusta', 'Se mantiene igual sin mirar lo que cambió', 'Se abandona todo sin dar explicaciones', 'Revisar mantiene la decisión coherente con la realidad.'),
        ("¿Por qué se incluye el descanso en el tiempo disponible?", "Porque cuidar el cuerpo es parte de un buen plan", "Sin descanso, el plan no es sostenible."),
    ],
    op=("Con la {F}, elige para Sol la opción o combinación que mejor responde a sus habilidades, a su tiempo y a su bienestar, y escribe dos evidencias del mapa que la apoyan. Luego revisa tu decisión con la condición nueva de 5 horas.",
        "Elijo la opción B (4 horas): usa guion y plan B (presentó en el acto del liceo) y bitácora (5 entradas), y deja 4 horas libres para descansar. Con 5 horas esta semana, mantengo B (4 horas) y dejo 1 hora de margen; pospongo cualquier otra opción hasta tener más tiempo.",
        ["elige una opción o combinación que cabe en 8 horas", "cita dos evidencias del mapa", "revisa la decisión con la condición nueva", "considera el descanso"],
        ["hoja con la decisión, dos evidencias y la revisión"],
        ["superar las horas disponibles", "no citar evidencia del mapa", "olvidar el descanso"],
        "Pregunta: «¿cuántas horas suman tus opciones?». Si no suma, pídele que lo calcule."),
    reinforce="Arma un mapa de tres habilidades tuyas con su evidencia y un contexto personal o laboral donde servirían.",
    extend="Explica cómo cambiaría tu decisión si una opción te diera más interés pero no cupiera en el tiempo disponible.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 4 (proyecto de ejemplo y portafolio, inventados). Tres estudiantes organizan una presentación de 40 minutos en el liceo, con la sala gratis. "
     "Presupuesto de ejemplo, en pesos chilenos inventados: programas impresos, 40 hojas a $50 cada una; transporte de un instrumento, $2.000; botellas de agua para las tres personas, $1.500 en total; pegamento y cinta, $500. "
     "Reparto del trabajo: Ana, producción; Hugo, sonido; Sol, presentación y guion. "
     "Portafolio de ejemplo (carpeta con evidencias): programa impreso, bitácora de ensayo, guion, comentarios del público y una grabación de audio, solo con permiso de quienes aparecen. "
     "Cuidados de trabajo: usar protección auditiva si el volumen es alto, hacer pausas de silencio y acordar por escrito quién hace qué y cómo se reconoce la autoría de cada obra y arreglo.")
build(
    O7, 4, F,
    use="Aprenderé a planificar un proyecto como una experiencia de trabajo real (presupuesto, reparto de roles y portafolio), a calcular costos de ejemplo y a cuidar la salud y la autoría al trabajar en música.",
    prior=["Sé reconocer roles y habilidades.", "Sé investigar y registrar fuentes.", "Sé que grabar o difundir requiere permiso y atribución."],
    explain=[
        "Un proyecto musical se parece a un trabajo cuando se organiza con presupuesto, roles y evidencias. El presupuesto es la lista de gastos previstos con su costo: se multiplica la cantidad por el precio de cada ítem y se suman los totales. Los roles se reparten por escrito para que cada persona sepa qué hace. Un buen acuerdo también dice cómo se reconoce la autoría de cada obra y de cada arreglo, y quién decide si algo se publica.",
        "El portafolio es una carpeta con evidencias de lo que se ha hecho: programas, bitácoras, guiones, comentarios del público y, si hay permiso, grabaciones. Sirve para mostrar el trabajo a docentes, a organizaciones o a quienes ofrecen oportunidades. Un portafolio no incluye datos personales de otras personas ni grabaciones sin permiso. Se ordena por fecha o por tipo de evidencia, y cada documento lleva su título y su fecha.",
        "Trabajar en música también exige cuidado ocupacional: protección auditiva si el volumen es alto, pausas de silencio, calentamiento de voz o manos y descanso. Las cifras de dinero de este cuaderno son de ejemplo; los precios, contratos y derechos reales los consultas con tu docente y con quien conozca el tema. Si una persona adulta o un grupo pide algo que te incomoda, avisa a una persona adulta de confianza.",
    ],
    vocab=[("presupuesto", "lista de gastos previstos con su costo"), ("portafolio", "carpeta con evidencias del trabajo hecho"), ("atribución", "reconocimiento de quién hizo cada obra o arreglo"),
           ("cuidado ocupacional", "medidas para proteger la salud al trabajar"), ("protección auditiva", "medidas que reducen el daño del volumen alto al oído"), ("acuerdo escrito", "documento breve que dice quién hace qué")],
    worked=[
        ("Calcular un ítem del presupuesto", "Un presupuesto de ejemplo incluye 60 hojas a $50 cada una. ¿Cuánto cuestan en total?",
         ["Se multiplica la cantidad por el precio de cada hoja: 60 × 50.", "60 × 50 = 3.000 pesos."],
         "$3.000"),
        ("Decidir sobre una grabación", "Un grupo quiere poner en su portafolio una grabación donde aparece una persona que no pertenece al grupo. ¿Qué debe hacer?",
         ["La grabación incluye a una persona que no es parte del grupo.", "Debe pedirle permiso; si no acepta, no se incluye."],
         "Pedir permiso y, si no acepta, no incluirla"),
    ],
    mistakes=[("Guardar en el portafolio grabaciones de personas sin su permiso.", "El permiso es individual y previo.", "Pide permiso y respeta una negativa."),
              ("Ignorar el volumen alto «porque es parte del trabajo».", "Se arriesga el oído.", "Usa protección auditiva, baja el volumen y haz pausas.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es un portafolio?', 'Una carpeta con evidencias del trabajo hecho', 'Una lista de los precios de los instrumentos', 'Un programa impreso que se reparte al público', 'Un portafolio reúne evidencias; no es una lista de precios ni un programa.'),
        ('abc', '{F} ¿Cuántas hojas se imprimen para el programa?', '40 hojas', '50 hojas', '4 hojas', 'La ficha indica 40 hojas a $50 cada una.'),
        ('abc', '{F} ¿Qué rol tiene Hugo en el reparto del trabajo?', 'Sonido', 'Producción', 'Presentación y guion', 'La ficha asigna sonido a Hugo, producción a Ana y presentación a Sol.'),
        ('=', '{F} ¿Cuánto cuestan en total los programas impresos (40 hojas a $50 cada una)?', '40*50', 'Se multiplican las hojas por el precio de cada una.', ' pesos'),
        ('=', '{F} ¿Cuántos pesos suma todo el presupuesto de ejemplo (programas, transporte, agua y materiales)?', '40*50+2000+1500+500', 'Se suman los programas, el transporte, el agua y los materiales de la ficha.', ' pesos'),
        ('abc', '{F} ¿Qué evidencia del portafolio muestra las decisiones del proceso de ensayo?', 'La bitácora de ensayo', 'El programa impreso para el público', 'La grabación de audio del acto', 'La bitácora registra las decisiones del proceso.'),
        ('abc', '{F} ¿Cuál es la condición para incluir la grabación de audio?', 'Tener permiso de quienes aparecen', 'Que la grabación sea más larga que 10 minutos en total', 'Que la haya hecho una persona adulta del liceo', 'La ficha dice que la grabación se incluye solo con permiso.'),
        ('=', '{F} Si el costo total se reparte entre las 3 personas por igual, ¿cuánto paga cada una? (El total es $6.000.)', '6000//3', 'Se divide el total entre las tres personas.', ' pesos'),
        ('abc', '{F} El volumen del acto será alto para el público. ¿Qué cuidado corresponde a quienes operan el sonido?', 'Usar protección auditiva y hacer pausas de silencio', 'Subir más el volumen para que se oiga mejor', 'No usar ninguna protección, porque dificulta el trabajo', 'Un volumen alto exige protección auditiva y pausas.'),
        ('abc', '{F} Un integrante propone publicar la grabación sin avisar a quien no quiso aparecer. ¿Qué decisión es adecuada?', 'No publicarla con esa persona', 'Publicarla igual, porque la mayoría del grupo quiere hacerlo', 'Publicarla sin su nombre para evitar que se entere de la decisión', 'El permiso es individual; la decisión de esa persona se respeta.'),
        ('abc', '{F} Un acuerdo escrito dice «Ana, producción; Hugo, sonido; Sol, presentación». ¿Qué le falta para estar completo?', 'Cómo se reconoce la autoría y quién decide publicar', 'La lista de todas las canciones que sabe cada integrante del grupo', 'Un compromiso de que nadie descansará durante el proyecto completo', 'Un buen acuerdo incluye atribución y decisión sobre la publicación.'),
        ('abc', 'Una persona adulta que organiza un evento les pide a unos estudiantes que trabajen sin descanso y sin protección con un volumen muy alto. ¿Qué deben hacer?', 'Decir que no y avisar a una persona adulta', 'Aceptar para no perder la oportunidad de participar en el evento', 'Ocultar el problema y trabajar sin avisar a nadie de lo ocurrido', 'La salud y el oído van primero, y ante una exigencia insegura se avisa.'),
        ('=', '{F} Si el transporte del instrumento cuesta $2.000 por viaje y se necesitan 2 viajes, ¿cuánto cuesta el transporte?', '2000*2', 'Se multiplica el costo de un viaje por la cantidad de viajes.', ' pesos'),
    ],
    ctx=('abc', 'Tu grupo recibe una invitación para tocar en un evento y quiere saber si les conviene. ¿Qué paso corresponde primero?', 'Calcular costos y tiempo, y repartir los roles por escrito', 'Aceptar de inmediato sin saber cuánto cuesta ni quién hace qué cosa', 'Rechazar sin preguntar nada sobre el evento ni sus condiciones de trabajo', 'Un plan con costos, tiempo y roles permite decidir con información.'),
    sc=[
        ("En Interpretación musical: ¿qué es un presupuesto?", "Una lista de gastos previstos con su costo", "El presupuesto organiza los gastos de un proyecto."),
        ('abc', 'Un portafolio no debe incluir:', 'Grabaciones sin permiso', 'Un programa impreso del acto de cierre', 'Una bitácora de ensayo de varias semanas', 'Sin permiso no se incluye a nadie.'),
        ("¿Qué haces si te piden trabajar sin protección ante un volumen alto?", "Digo que no y aviso a una persona adulta de confianza", "El oído se cuida aunque falte presión del entorno."),
    ],
    op=("Con la {F}, arma tu propio presupuesto de ejemplo para un acto de 30 minutos de tu grupo (tres ítems con cantidad, precio de ejemplo y total), escribe el reparto de tres roles y una lista de cuatro evidencias para el portafolio, indicando cuál necesita permiso.",
        "Presupuesto de ejemplo: 30 hojas a $50 = $1.500; transporte de un instrumento $1.000; agua $1.000; total $3.500. Roles: producción, sonido y presentación. Portafolio: programa impreso, bitácora, guion y una grabación de audio, que necesita el permiso de quienes aparecen.",
        ["calcula tres ítems con total", "reparte tres roles", "enumera cuatro evidencias", "indica qué evidencia necesita permiso"],
        ["hoja con el presupuesto, los roles y el portafolio"],
        ["calcular mal el total", "olvidar el permiso de la grabación", "no repartir los roles"],
        "Pregunta: «¿cuánto suma tu presupuesto?». Si no lo calcula, pídele que lo haga paso a paso."),
    reinforce="Calcula un presupuesto de ejemplo con tres ítems y reparte su costo entre cuatro personas.",
    extend="Explica por qué el portafolio sirve tanto para estudiar como para trabajar, con un ejemplo.",
)
