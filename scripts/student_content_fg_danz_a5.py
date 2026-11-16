"""Danza 3.º y 4.º medio FG: OAC-05 (evaluación crítica de procesos y obras de danza), clases 1 a 5. Fichas inventadas; sin video real."""
from __future__ import annotations

from fg_danz_common import build

O5 = "FG-DANZ-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (pauta de ejemplo, inventada). Cada criterio se puntúa de 1 (se inicia) a 4 (logrado). "
     "Criterio A, propósito claro: la obra permite reconocer qué quiere comunicar. "
     "Criterio B, uso del espacio, el tiempo y la energía: las decisiones apoyan el propósito. "
     "Criterio C, puesta en escena: luz, vestuario y sonido apoyan la idea. "
     "Criterio D, proceso: hay registro de ensayos, cambios y acuerdos del grupo. "
     "Puntajes del grupo «Marea»: A=3, B=4, C=2, D=3.")
build(
    O5, 1, F,
    use="Aprenderé a evaluar una obra o un proyecto de danza con criterios claros, separando el resultado del proceso y fundando cada puntaje en evidencia observable.",
    prior=["Sé interpretar una obra con evidencia.", "Sé que un juicio necesita razones.", "Sé que no se evalúan los cuerpos."],
    explain=[
        "Evaluar críticamente es valorar un proceso o una obra usando criterios y evidencia. Una pauta reúne criterios con niveles de logro. Cada criterio debe ser observable: «propósito claro» se comprueba viendo si se reconoce qué comunica la obra; «hermosa» no es un criterio porque depende del gusto. Además, se evalúa tanto el resultado (la obra presentada) como el proceso (cómo se trabajó, qué decisiones se tomaron y cómo se colaboró).",
        "Al puntuar se escribe una razón que cite evidencia. Por ejemplo, «C = 2 porque la luz no cambia entre secciones y el sonido se oye más fuerte que los pasos». Sin esa razón, el puntaje solo es una cifra. Los criterios nunca incluyen el cuerpo, el peso, la edad ni la condición física de las personas: se evalúa lo que se decide y se hace, no cómo es el cuerpo.",
        "Evaluar es una oportunidad para mejorar, no para humillar. Se comunica con respeto y cada persona puede elegir cómo compartir sus resultados. Una evaluación puede hacerse por escrito, sin exposición pública.",
    ],
    vocab=[("criterio", "aspecto observable que se evalúa"), ("pauta", "lista de criterios con niveles de logro"), ("nivel de logro", "grado en que se cumple un criterio"), ("proceso", "cómo se trabajó hasta llegar a la obra"), ("resultado", "la obra o producto presentado")],
    worked=[
        ("Sumar una pauta", "Con los puntajes del grupo «Marea», ¿cuántos puntos tiene sobre 16?", ["Se suman 3 + 4 + 2 + 3.", "El total es 12 de 16."], "12 de 16"),
        ("Fundar un puntaje", "Escribe una razón para B = 4.", ["Se cita evidencia: los cambios de energía y de velocidad apoyan el propósito en cada sección.", "Se vincula con el criterio de la pauta."], "B = 4 porque los cambios de energía y velocidad apoyan el propósito en cada sección"),
    ],
    mistakes=[("Poner puntaje sin razón («le puse 3 porque sí»).", "Nadie puede revisar ni mejorar con eso.", "Escribe la evidencia que justifica el nivel."),
              ("Incluir en la pauta un criterio sobre el cuerpo («se ve ágil»).", "Evalúa a la persona y no su trabajo.", "Usa criterios sobre decisiones y trabajo.")],
    T=[
        ('abc', '¿Qué es una pauta?', 'Una lista de criterios con niveles de logro', 'Una opinión personal sobre la obra', 'El libreto que se memoriza para la presentación', 'La pauta ordena la evaluación con criterios.'),
        ('abc', '{F} ¿Cuál es el criterio D?', 'Proceso: registro de ensayos, cambios y acuerdos', 'Puesta en escena: luz, vestuario y sonido que apoyan la idea de la obra', 'Propósito claro: la obra permite reconocer qué quiere comunicar', 'La ficha define D como proceso.'),
        ('=', '{F} ¿Cuántos puntos suma el grupo «Marea»?', '3+4+2+3', 'Se suman los cuatro puntajes de la ficha.', ' puntos'),
        ('abc', '{F} ¿Cuál es el criterio con el puntaje más bajo?', 'C, puesta en escena', 'A, propósito claro', 'D, proceso', 'C tiene 2 puntos, el menor.'),
        ('abc', '¿Cuál de estos es un criterio observable?', 'Las decisiones de tiempo y energía apoyan el propósito', 'La obra es linda', 'El grupo es simpático, y eso se nota apenas entra', 'Un criterio debe poder comprobarse con lo que se observa.'),
        ('abc', 'Evaluar el proceso significa', 'revisar cómo se trabajó, qué se decidió y cómo se colaboró', 'mirar solo el resultado final', 'contar cuántos ensayos hizo cada persona sin ver qué hizo', 'El proceso incluye decisiones y colaboración.'),
        ('abc', '{F} ¿Cuál razón fundamenta C = 2?', 'La luz no cambia entre secciones y el sonido tapa los pasos', 'Porque el grupo se ve nervioso y eso baja la calidad de la puesta en escena', 'Porque a mí me gustó menos que el resto de las decisiones del grupo', 'Cita evidencia de puesta en escena.'),
        ('abc', '{F} Un compañero propone agregar el criterio «los intérpretes se ven delgados». ¿Qué corresponde?', 'Rechazarlo porque evalúa el cuerpo y no las decisiones', 'Aceptarlo para tener más criterios y que la pauta sea más completa', 'Aceptarlo si se aplica a todos los grupos por igual y con la misma pauta', 'Los cuerpos de las personas no se evalúan, solo su trabajo.'),
        ('=', '{F} Si el grupo mejora C de 2 a 4 y D de 3 a 4, ¿cuántos puntos más tiene en total?', '(4-2)+(4-3)', 'Se suman las diferencias de los dos criterios.', ' puntos'),
        ('abc', 'Dos grupos tienen igual resultado final, pero uno registró sus decisiones y el otro no. ¿Qué evalúa el criterio de proceso?', 'Que el primero tiene mejor evidencia del proceso', 'Que ambos son iguales, porque el resultado final es el mismo', 'Que el segundo trabajó más, aunque no dejó evidencia de lo que hizo', 'El proceso se evalúa por evidencia del trabajo.'),
        ('abc', 'Una estudiante prefiere no mostrar el resultado en público. ¿Qué evaluación es adecuada?', 'Evaluar su bitácora y una descripción por escrito de su trabajo', 'Ponerle puntaje mínimo porque no presentó el resultado ante el curso', 'Obligarla a mostrarlo en público para poder evaluarla como a las demás', 'Se pueden usar otras evidencias del proceso.'),
        ('=', 'Una pauta tiene 5 criterios con puntaje de 1 a 4. ¿Cuál es el puntaje máximo?', '5*4', 'Se multiplica el número de criterios por el máximo de cada uno.', ' puntos'),
        ('abc', 'Un grupo recibe 12 puntos de 16. ¿Qué es una conclusión fundada?', 'Su desempeño es bueno, y los criterios con menor puntaje indican qué mejorar', 'Es el mejor grupo del curso, porque su puntaje es alto en la pauta', 'No tiene nada que mejorar, porque más de la mitad de los puntos es suficiente', 'Un puntaje se lee junto con los criterios.'),
    ],
    ctx=('abc', 'Un grupo escribe su pauta: (1) propósito claro; (2) uso del espacio; (3) «la coreografía es hermosa»; (4) cuidado de la seguridad en los ensayos. ¿Qué criterio debe reescribirse?', 'El criterio 3, porque «hermosa» depende del gusto y no se puede comprobar', 'El criterio 1, porque es demasiado general y no se puede medir', 'El criterio 4, porque la seguridad no se evalúa en una obra', 'Un criterio debe ser observable y no depender del gusto.'),
    sc=[
        ("En Danza: ¿qué es un criterio?", "Un aspecto observable que se evalúa", "Un criterio se puede comprobar con evidencia de la obra."),
        ("¿Qué se evalúa además del resultado?", "El proceso", "El proceso incluye decisiones, registro y colaboración del grupo."),
        ("¿Se evalúa el cuerpo de las personas?", "No, se evalúan decisiones y trabajo", "El respeto al cuerpo es una regla."),
    ],
    op=("Diseña una pauta de 4 criterios observables para una obra o proyecto de danza (uno de proceso) con niveles de 1 a 4. Puntúa una obra inventada y escribe la razón de dos puntajes.",
        "Criterios: propósito claro, energía y tiempo, puesta en escena, proceso. Puntajes: 3, 4, 2, 3. Razón de energía = 4: los cambios apoyan el propósito. Razón de puesta en escena = 2: la luz no cambia.",
        ["criterios observables", "un criterio de proceso", "razones con evidencia"],
        ["hoja con pauta y dos razones"],
        ["criterios de gusto", "criterios sobre el cuerpo", "puntaje sin razón"],
        "Pregunta: «¿qué viste que justifique el puntaje?». Si responde «me pareció», pídele evidencia."),
    reinforce="Escribe tres criterios observables para evaluar una frase de danza.",
    extend="Explica por qué un criterio como «es bonito» no sirve en una pauta.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (bitácora de ejemplo, inventada). Ensayo 1: probamos el canon de 4 personas; hubo choques de espacio entre P2 y P3; decidimos ampliar a un metro la distancia. "
     "Ensayo 2: el canon ahora se ve limpio, pero el cierre es confuso; probamos una pausa final de 4 tiempos. "
     "Ensayo 3: la pausa final funciona; la música tapa los pasos; bajamos su volumen. "
     "Ensayo 4: terminamos tarde 15 minutos porque no hubo calentamiento ordenado; acordamos 10 minutos de calentamiento al inicio.")
build(
    O5, 2, F,
    use="Aprenderé a evaluar mi propio proceso con una bitácora: registrar lo ocurrido, reconocer decisiones y problemas con honestidad y decidir qué conservar o cambiar.",
    prior=["Sé usar una pauta con criterios.", "Sé separar hechos y opiniones.", "Sé trabajar en grupo."],
    explain=[
        "La bitácora es un registro breve de cada ensayo. Una buena entrada dice qué se hizo, qué problema apareció y qué decisión se tomó. Por ejemplo: «hubo choques de espacio; se amplió la distancia a un metro». La bitácora permite revisar el proceso con evidencia en lugar de depender de la memoria.",
        "La autoevaluación es valorar el propio trabajo. Para hacerla con honestidad se identifican logros, dificultades y causas, se separan los hechos (terminamos 15 minutos tarde) de las explicaciones (porque el calentamiento no estaba ordenado) y se evita culpar a personas. El foco está en las decisiones del grupo y en lo que se puede cambiar.",
        "También se evalúan aspectos de salud y seguridad del trabajo: si hubo calentamiento y enfriamiento, si se respetaron los límites del cuerpo, si alguien se sintió mal y se detuvo. Si una persona sintió dolor o presión del grupo, lo comunica a una persona adulta.",
    ],
    vocab=[("bitácora", "registro breve de cada ensayo"), ("autoevaluación", "valoración del propio trabajo"), ("dificultad", "problema que aparece en el proceso"), ("decisión", "cambio que se acuerda para mejorar"), ("causa", "razón por la que ocurrió algo")],
    worked=[
        ("Identificar problema y decisión", "En el ensayo 1 de la ficha, ¿cuál fue el problema y cuál la decisión?", ["Problema: choques de espacio entre P2 y P3.", "Decisión: ampliar la distancia a un metro."], "Problema: choques de espacio; decisión: un metro de distancia"),
        ("Separar hecho y explicación", "Del ensayo 4: «terminamos tarde 15 minutos porque el calentamiento no estaba ordenado». Separa hecho y explicación.", ["Hecho: terminaron 15 minutos tarde.", "Explicación: el calentamiento no estaba ordenado."], "Hecho: 15 minutos tarde; explicación: calentamiento desordenado"),
    ],
    mistakes=[("Escribir en la bitácora solo «todo bien» o «ensayo normal».", "No deja evidencia de decisiones ni de problemas.", "Anota qué se hizo, qué problema apareció y qué se decidió."),
              ("Culpar a una persona («P3 arruinó el canon»).", "Quita el foco de las decisiones y daña la relación.", "Describe el hecho y propone una decisión del grupo.")],
    T=[
        ('abc', '¿Qué es una bitácora?', 'Un registro breve de cada ensayo con hechos y decisiones', 'La lista de integrantes del grupo', 'La música de la obra, ordenada por secciones', 'Es un registro del proceso con hechos y decisiones.'),
        ('abc', '{F} ¿Qué problema apareció en el ensayo 2?', 'El cierre se veía confuso', 'La música tapaba los pasos', 'Hubo choques de espacio', 'El cierre confuso es el problema del ensayo 2.'),
        ('abc', '{F} ¿Qué decisión se tomó en el ensayo 3?', 'Bajar el volumen de la música', 'Agregar una pausa final', 'Ampliar la distancia', 'La ficha lo dice: bajar el volumen.'),
        ('=', '{F} Si se mantiene el calentamiento acordado de 10 minutos en los 5 ensayos siguientes, ¿cuántos minutos de calentamiento suman?', '5*10', 'Se multiplica el número de ensayos por los 10 minutos de calentamiento.', ' minutos'),
        ('abc', '{F} «Terminamos tarde 15 minutos» es', 'un hecho', 'una explicación', 'un juicio sobre una persona', 'Se puede comprobar con el reloj.'),
        ('abc', '{F} ¿Qué causa se señala para terminar tarde?', 'Que el calentamiento no estaba ordenado', 'Que P3 llegó tarde y retrasó a todo el grupo', 'Que la música era muy fuerte y tapaba las indicaciones del ensayo', 'La causa está en la ficha.'),
        ('abc', 'Para una autoevaluación honesta conviene', 'registrar logros y dificultades con hechos y causas', 'escribir solo los logros', 'culpar a quien tuvo más dificultades', 'La honestidad incluye lo bueno y lo difícil.'),
        ('abc', '{F} Un integrante dice «P2 siempre choca». ¿Cómo se reformula con foco en la decisión?', 'Hubo choques entre P2 y P3; se amplió la distancia a un metro', 'P2 debe ensayar más solo hasta dejar de chocar con las demás personas', 'P3 debe cuidarse de P2 porque siempre se acerca demasiado', 'Se describe el hecho y se propone una decisión.'),
        ('=', '{F} Si la distancia pasó de 50 centímetros a 1 metro, ¿cuántos centímetros se amplió?', '100-50', 'Un metro son 100 centímetros; se restan los 50 iniciales.', ' centímetros'),
        ('abc', 'Una compañera siente dolor en el hombro durante el ensayo, pero el grupo quiere terminar el conteo. ¿Qué corresponde registrar y hacer?', 'Detener el ejercicio, avisar a una persona adulta y anotarlo en la bitácora', 'Seguir, anotando que fue una molestia pasajera y que no hubo que parar', 'Seguir con otro movimiento más fuerte para que el hombro entre en calor', 'La seguridad va antes que el avance.'),
        ('abc', 'En la bitácora, ¿qué entrada es más útil?', 'Probamos pausa de 4 tiempos; el cierre se ve claro pero falta ensayar la entrada', 'Estuvo bien, avanzamos bastante y todos trabajaron con muchas ganas', 'El ensayo fue largo y nos cansamos bastante, pero terminamos todo lo previsto', 'Dice qué se probó y qué falta.'),
        ('=', '{F} Los ensayos 1 a 3 duraron 60 minutos cada uno y el ensayo 4 duró 60 minutos más los 15 que se pasó de la hora. ¿Cuántos minutos suman los cuatro ensayos?', '4*60+15', 'Se suman los cuatro ensayos de 60 minutos y los 15 minutos de retraso.', ' minutos'),
        ('abc', 'Alguien siente presión del grupo para hacer un movimiento que no quiere. ¿Qué corresponde?', 'Comunicarlo y avisar a una persona adulta; el consentimiento se respeta', 'Hacerlo igual para no entorpecer el ensayo ni retrasar al resto del grupo', 'Pedir que otro lo haga en su lugar sin explicarle al grupo por qué', 'El grupo respeta el no y nadie debe presionar.'),
    ],
    ctx=('abc', 'En su bitácora un grupo escribe: «Ensayo 5: se hizo el canon dos veces sin choques; el cierre sigue confuso; decidimos probar luz baja en el cierre». ¿Qué tiene de valioso esa entrada?', 'Registra un logro, una dificultad y una decisión concreta', 'Solo celebra el logro del grupo y no menciona ninguna dificultad ni decisión', 'Solo señala la dificultad del grupo y no registra ninguna decisión', 'La entrada incluye hechos, un logro y una decisión concreta.'),
    sc=[
        ("En Danza: ¿qué es la bitácora?", "Un registro del proceso con hechos y decisiones", "Permite revisar el proceso con evidencia y no de memoria."),
        ("¿Qué se hace con una dificultad en la bitácora?", "Se registra y se propone una decisión", "Una dificultad registrada orienta el trabajo del siguiente ensayo."),
        ("¿Cómo se evita culpar a personas?", "Describiendo hechos y decisiones del grupo", "El foco está en lo que se puede cambiar."),
    ],
    op=("Escribe una bitácora de dos ensayos inventados: por ensayo, qué se hizo, un problema, su causa y una decisión. Marca una entrada que sea hecho y otra que sea explicación.",
        "Ensayo 1: probamos el cierre; se veía confuso (hecho); causa: nadie sabía cuándo terminar (explicación). Decisión: marcar el final con 4 tiempos de pausa. Ensayo 2: la pausa funciona; la entrada se retrasó; decisión: contar en voz baja.",
        ["incluye hecho, causa y decisión", "no culpa a personas", "registra seguridad si corresponde"],
        ["hoja con dos entradas de bitácora"],
        ["escribir «todo bien»", "culpar a una persona"],
        "Pregunta: «¿qué decidieron cambiar?». Si no hay decisión, pídele proponer una."),
    reinforce="Escribe una entrada de bitácora de un ensayo imaginario con problema, causa y decisión.",
    extend="Explica cómo una bitácora ayuda a decidir qué conservar y qué cambiar.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (comentarios de ejemplo a un trabajo de pares, inventados, sobre una frase en canon). "
     "Comentario 1: «Todo estuvo mal». "
     "Comentario 2: «Observé que la entrada de P3 llegó un tiempo antes y el canon se perdió; sugiero contar 1-2 en voz baja antes de entrar». "
     "Comentario 3: «Me gustó». "
     "Comentario 4: «P2 no tiene el cuerpo para bailar así».")
build(
    O5, 3, F,
    use="Aprenderé a dar retroalimentación a mis pares que sea descriptiva, fundada y respetuosa, y a reconocer comentarios que no sirven o que no se deben decir.",
    prior=["Sé usar criterios.", "Sé separar hecho y opinión.", "Sé que no se comentan los cuerpos."],
    explain=[
        "La retroalimentación es un comentario que ayuda a mejorar. Una fórmula útil tiene tres partes: lo observado (qué se vio), el criterio o efecto (por qué importa) y una sugerencia o pregunta (qué se podría probar). Por ejemplo: «Observé que la entrada de P3 llegó un tiempo antes y el canon se perdió; sugiero contar en voz baja antes de entrar». Es específica y se puede aplicar.",
        "Los comentarios generales («estuvo mal», «me gustó») son amables o duros, pero no orientan. Los comentarios que hablan del cuerpo, del peso o del aspecto de una persona no son críticas: son faltas de respeto y no se aceptan en el trabajo. Si ocurre, se detiene la conversación, se recuerdan los acuerdos y se avisa a una persona adulta si sigue.",
        "Quien recibe la retroalimentación puede escuchar sin discutir, preguntar y decidir qué usar. Es útil empezar por lo que funcionó, siempre que sea verdad, y luego señalar lo que se puede mejorar.",
    ],
    vocab=[("retroalimentación", "comentario que ayuda a mejorar un trabajo"), ("específico", "que señala algo concreto"), ("sugerencia", "propuesta de cambio posible"), ("respeto", "trato digno a las personas y sus cuerpos"), ("acuerdos de trabajo", "reglas del grupo para trabajar bien")],
    worked=[
        ("Identificar el mejor comentario", "En la ficha, ¿cuál comentario sirve más para mejorar?", ["El 2 dice qué se observó, qué efecto tuvo y qué probar.", "Los otros son generales o hablan del cuerpo."], "El comentario 2"),
        ("Reformular un comentario vago", "Reescribe «todo estuvo mal» como retroalimentación.", ["Elige un hecho: la entrada de P3 llegó un tiempo antes.", "Agrega efecto y sugerencia: el canon se perdió; contar antes de entrar."], "Observé que la entrada de P3 llegó antes y el canon se perdió; sugiero contar antes de entrar"),
    ],
    mistakes=[("Dar un comentario que solo dice «bien» o «mal».", "No dice qué cambiar ni qué conservar.", "Señala un hecho, su efecto y una sugerencia."),
              ("Comentar el cuerpo de una persona como si fuera una crítica útil.", "Es una falta de respeto y no mejora el trabajo.", "Comenta decisiones de movimiento y puesta en escena.")],
    T=[
        ('abc', '¿Qué tiene una retroalimentación útil?', 'Lo observado, el efecto y una sugerencia', 'Solo una opinión sobre si gustó o no', 'Una comparación con otros grupos, para que se note quién fue mejor', 'Esas tres partes la hacen aplicable.'),
        ('abc', '{F} ¿Cuál comentario es específico y respetuoso?', 'El comentario 2', 'El comentario 1', 'El comentario 3', 'El 2 señala un hecho, un efecto y una sugerencia.'),
        ('abc', '{F} ¿Qué observó el comentario 2?', 'Que la entrada de P3 llegó un tiempo antes', 'Que la música estaba muy alta durante todo el canon', 'Que el vestuario de las cuatro personas era gris', 'La ficha lo indica en la entrada de ese ensayo.'),
        ('abc', '{F} ¿Por qué el comentario 4 no se acepta?', 'Porque habla del cuerpo de una persona', 'Porque es muy largo', 'Porque no propone nada sobre el canon', 'El cuerpo de una persona no se comenta como crítica.'),
        ('abc', '{F} El comentario 3 («me gustó») es', 'amable pero poco útil para mejorar', 'la mejor retroalimentación posible', 'una falta de respeto', 'No dice qué conservar ni qué cambiar en el trabajo.'),
        ('=', '{F} El canon de 4 personas entra cada 2 tiempos y P3 entró en el tiempo 4 en lugar del 5. ¿Cuántos tiempos antes entró?', '5-4', 'Se resta el tiempo real del tiempo esperado.', ' tiempo'),
        ('abc', '{F} Quieres sugerir algo sobre la entrada de P3. ¿Cuál formulación es mejor?', '¿Podrían contar en voz baja antes de entrar para mantener los tiempos?', 'Tienen que entrar bien o se arruina todo el canon, así que concéntrense más', 'P3 siempre se equivoca en la entrada y atrasa a todo el grupo', 'Una pregunta o sugerencia orienta sin culpar.'),
        ('abc', 'Recibes un comentario que no entiendes. ¿Qué haces?', 'Pedir un ejemplo de lo que vio', 'Responder con una crítica a quien lo hizo', 'Ignorar todo lo que dijo', 'Pedir un ejemplo ayuda a entender qué se vio.'),
        ('=', 'Un curso de 30 personas forma grupos de 5 y cada grupo da 3 comentarios específicos a otro grupo. ¿Cuántos comentarios se dan en total?', '30//5*3', 'Se calcula el número de grupos y se multiplica por 3.', ' comentarios'),
        ('abc', 'Alguien dice en voz alta un comentario sobre el cuerpo de un compañero. ¿Qué corresponde?', 'Detener el comentario, recordar los acuerdos y avisar a una persona adulta si continúa', 'Reír para que no sea tan grave y que no se arme un problema', 'Responder con otro comentario parecido, para que se dé cuenta de cómo se siente', 'Se detiene y se cuida a la persona.'),
        ('abc', 'Un grupo recibe 5 comentarios: 2 generales y 3 específicos. ¿Con cuáles trabajan primero?', 'Con los específicos, porque indican qué cambiar', 'Con los generales, porque son más amables', 'Con ninguno', 'Los comentarios específicos se pueden aplicar en el ensayo.'),
        ('=', 'Cada comentario específico tarda 45 segundos en decirse. Si un grupo recibe 4 comentarios de 3 grupos distintos, ¿cuántos segundos de comentarios escucha?', '3*4*45', 'Se multiplican los grupos por los comentarios y los segundos.', ' segundos'),
        ('abc', 'Quieres empezar tu comentario por algo que funcionó. ¿Qué condición debe cumplir?', 'Que sea verdad y específico', 'Que sea un elogio general', 'Que suene amable aunque no sea cierto', 'Un elogio sirve solo si es real y específico.'),
    ],
    ctx=('abc', 'Un grupo recibe: (1) «Todo bien»; (2) «Observé que el cierre no se entiende porque la luz sigue igual; ¿probarían bajarla?»; (3) «Se nota que X no sabe bailar». ¿Cuál es retroalimentación útil y respetuosa?', 'El comentario 2, que da un hecho, su efecto y una sugerencia', 'El comentario 1, porque es amable y breve', 'El comentario 3, porque es sincero y directo', 'El comentario 2 cita hecho, efecto y sugerencia sin hablar de personas.'),
    sc=[
        ("En Danza: ¿qué es retroalimentación?", "Un comentario que ayuda a mejorar", "Tiene una observación, su efecto y una sugerencia."),
        ("¿Se comentan los cuerpos?", "No", "Solo se comentan decisiones de trabajo y de movimiento."),
        ("¿Qué haces con un comentario que no entiendes?", "Pides un ejemplo", "Pedir un ejemplo ayuda a entender qué se vio."),
    ],
    op=("Escribe una retroalimentación para un trabajo de pares inventado: una observación, el efecto en el resultado y una sugerencia o pregunta. Luego identifica un comentario inadecuado y reescríbelo.",
        "Observé que el grupo cambió de formación en 2 tiempos y se rozaron. Eso hizo el cambio inseguro. Sugiero acordar caminos y hacerlo en 4 tiempos. Inadecuado: «se ven torpes». Reescrito: «el cambio de formación necesita más tiempo».",
        ["observación, efecto y sugerencia", "no habla del cuerpo", "reescribe un comentario inadecuado"],
        ["hoja con retroalimentación y reescritura"],
        ["comentarios generales", "comentarios sobre el cuerpo"],
        "Pregunta: «¿qué viste exactamente?». Si responde con una opinión, pídele un hecho."),
    reinforce="Escribe una retroalimentación de tres partes sobre una frase de danza imaginada.",
    extend="Explica por qué «me gustó» no alcanza como retroalimentación.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (tres posturas de ejemplo sobre la obra «Marea», ya conocida: seis intérpretes que ondulan en línea, se cruzan en diagonal y quedan quietos; luz que baja; percusión suave). "
     "Postura A: «Me gustó porque soy fan del mar». "
     "Postura B: «Pienso que logra mostrar el ir y venir, porque la línea se separa y vuelve, según el criterio de uso del espacio». "
     "Postura C: «Es mala porque no tiene música cantada».")
build(
    O5, 4, F,
    use="Aprenderé a construir una postura personal fundada y respetuosa sobre una obra o proceso: decir mi juicio, apoyarlo con evidencia y criterio, distinguirlo del gusto y estar dispuesta a revisarlo.",
    prior=["Sé dar retroalimentación específica.", "Sé usar afirmación, evidencia y criterio.", "Sé separar gusto de juicio."],
    explain=[
        "Una postura personal fundada es un juicio sobre una obra o un proceso que se apoya en criterios y evidencia. Tiene la forma: «Pienso que… porque… según el criterio de…». El gusto («me gustó porque me gusta el mar») es válido como sensación, pero no es un juicio fundado porque no se apoya en lo que la obra hace. Un juicio fundado puede coincidir o no con mi gusto: puedo reconocer que una obra logra su propósito aunque no sea mi favorita.",
        "Una postura respetuosa critica el trabajo, no a las personas, usa un lenguaje cuidadoso y reconoce el valor de las lecturas ajenas. Además, es revisable: si aparece nueva evidencia, se puede cambiar de opinión. Cambiar de postura con razones es una señal de pensamiento crítico y no de debilidad.",
        "Para opinar en grupo se escucha primero, se pide la palabra y se evita descalificar. Cada persona puede dar su postura por escrito si prefiere no hablar. Los comentarios que ofenden o hablan del cuerpo se detienen.",
    ],
    vocab=[("postura", "juicio personal sobre una obra o un proceso"), ("fundada", "apoyada en criterios y evidencia"), ("gusto", "preferencia personal"), ("revisable", "que se puede cambiar con nueva evidencia"), ("respetuosa", "que critica el trabajo y no a las personas")],
    worked=[
        ("Reconocer la postura fundada", "En la ficha, ¿cuál es una postura fundada?", ["La B cita un criterio (uso del espacio) y evidencia (la línea se separa y vuelve).", "La A es gusto y la C no se apoya en un criterio relevante."], "La postura B"),
        ("Separar gusto y juicio", "Alguien dice «no me gusta el mar, pero la obra logra mostrar el ir y venir». ¿Es coherente?", ["Reconoce que el gusto es suyo y que el juicio se funda en la obra.", "Es coherente: puede valorar un trabajo que no es de su preferencia."], "Sí, separa el gusto del juicio"),
    ],
    mistakes=[("Decir que una obra es mala solo porque no coincide con mi preferencia.", "Es gusto y no explica qué hace la obra.", "Explica qué criterio usas y qué evidencia ves."),
              ("Defender mi postura sin escuchar nueva evidencia.", "Una postura fundada es revisable cuando hay evidencia nueva.", "Si hay datos nuevos, evalúa si cambias tu postura.")],
    T=[
        ('abc', '¿Qué es una postura fundada?', 'Un juicio apoyado en criterios y evidencia', 'Una opinión repetida con más fuerza', 'Una preferencia personal que mucha gente comparte', 'Se apoya en lo que la obra hace.'),
        ('abc', '{F} ¿Cuál postura está fundada?', 'La postura B', 'La postura A', 'La postura C', 'La B cita criterio y evidencia.'),
        ('abc', '{F} La postura A es', 'una expresión de gusto', 'un juicio fundado', 'una descripción de la obra', 'Se basa en la preferencia personal.'),
        ('abc', '{F} ¿Por qué la postura C no está fundada?', 'Porque exige un rasgo que la obra no se propone, sin explicar por qué importa', 'Porque es negativa y toda valoración negativa carece de fundamento', 'Porque no menciona el mar ni ninguna otra imagen de la obra', 'Un juicio debe apoyarse en criterios pertinentes.'),
        ('=', '{F} Cada una de las 6 personas del grupo escribe una postura fundada como la B y una de gusto como la A. ¿Cuántas posturas escriben entre todas?', '6*2', 'Cada persona escribe 2 posturas y son 6 personas.', ' posturas'),
        ('abc', 'Reconocer que una obra logra su propósito aunque no sea mi favorita demuestra', 'separar el gusto del juicio fundado', 'que no tengo opinión propia sobre la obra que vi', 'que cambié de gusto personal después de verla', 'El juicio se apoya en la obra.'),
        ('abc', '{F} Quieres convertir la postura A en fundada. ¿Qué cambio sirve?', 'Decir qué hace la obra, como la línea que vuelve, y con qué criterio lo valoras', 'Decir lo mismo, con más énfasis y repetirlo varias veces', 'Decir que a todos les gustó y que por eso es una obra muy buena', 'Se añade evidencia observable y el criterio usado.'),
        ('abc', 'Alguien descubre un dato nuevo que contradice su postura. ¿Qué es lo más razonable?', 'Revisar si la evidencia cambia su juicio y, si corresponde, modificarlo', 'Mantener su postura sin mirar el dato, porque ya la había expresado en público', 'Ocultar el dato nuevo para que la postura anterior no cambie', 'Una postura fundada es revisable cuando hay evidencia nueva.'),
        ('=', 'En una conversación, 8 personas dan su postura de 40 segundos cada una, con 10 segundos de cambio entre una y otra (7 cambios). ¿Cuántos segundos dura?', '8*40+7*10', 'Se suman las posturas y los cambios.', ' segundos'),
        ('abc', 'Una compañera critica a un intérprete diciendo que «no tiene el físico». ¿Qué corresponde?', 'Redirigir la crítica a las decisiones de movimiento y recordar el respeto al cuerpo', 'Aceptarlo como parte de la crítica, porque el físico también forma parte de la obra', 'Responder con otro comentario sobre el físico de quien criticó, para equilibrar', 'No se critica el cuerpo, solo las decisiones de movimiento.'),
        ('abc', 'Una estudiante prefiere dar su postura por escrito. ¿Qué corresponde?', 'Aceptarlo; la postura se puede compartir por escrito', 'Obligarla a hablar delante del grupo porque todas las posturas deben expresarse en voz alta', 'No tomar en cuenta su postura mientras no la diga en voz alta', 'La forma de compartir es una decisión personal.'),
        ('=', 'Una obra recibió 20 posturas: 14 fundadas y el resto de gusto. ¿Cuántas posturas son de gusto?', '20-14', 'Se restan las fundadas del total.', ' posturas'),
        ('abc', 'Escribes: «Pienso que el cierre es claro porque hay 4 tiempos de pausa, según el criterio de tiempo». ¿Qué parte es la evidencia?', 'Hay 4 tiempos de pausa', 'El cierre es claro', 'Según el criterio de tiempo', 'La evidencia es el hecho observable.'),
    ],
    ctx=('abc', 'Después de ver una obra, una estudiante escribe: «Pienso que el uso de la luz es insuficiente porque no cambia entre las secciones, según el criterio de puesta en escena. A mí me gustó el vestuario, pero eso es mi gusto». ¿Qué hizo bien?', 'Dio un juicio fundado y separó su gusto', 'Mezcló gusto y juicio sin separarlos ni explicar nada de la obra', 'No dio ninguna razón ni citó ningún rasgo observable de la obra', 'El texto separa juicio fundado y preferencia.'),
    sc=[
        ("En Danza: ¿qué es una postura fundada?", "Un juicio con criterios y evidencia", "Una postura fundada no es solo gusto personal."),
        ("¿Qué forma tiene una postura fundada?", "Pienso que… porque… según el criterio de…", "La forma une el juicio, la evidencia y el criterio."),
        ("¿Una postura puede cambiar?", "Sí, si aparece nueva evidencia", "Una postura es revisable si aparece evidencia nueva."),
    ],
    op=("Escribe tu postura sobre una obra inventada breve con la forma «Pienso que… porque… según el criterio de…». Añade una frase que separe tu gusto del juicio y reconoce otra lectura.",
        "Obra: cuatro personas caminan en círculo y se detienen juntas. Pienso que logra la idea de unión porque se detienen a la vez, según el criterio de tiempo. Mi gusto: me gustó menos la luz. Otra lectura posible: espera.",
        ["usa la forma pedida", "separa gusto y juicio", "reconoce otra lectura"],
        ["hoja con postura breve"],
        ["solo gusto", "descalificar a otras personas"],
        "Pregunta: «¿qué criterio usaste?». Si no lo dice, pídele que lo agregue."),
    reinforce="Escribe una postura con la forma de la clase sobre una escena imaginada.",
    extend="Explica por qué cambiar de postura con razones es una señal de pensamiento crítico.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (resultados de ejemplo de un grupo, inventados, en una pauta de 1 a 4). "
     "A propósito claro: 3. B uso de espacio, tiempo y energía: 4. C puesta en escena: 2. D proceso y registro: 2. "
     "Comentarios de pares: «el cierre no se entiende», «la bitácora está incompleta», «el canon quedó limpio». "
     "Faltan 3 semanas para la muestra y hay 1 ensayo de 45 minutos por semana.")
build(
    O5, 5, F,
    use="Aprenderé a usar los resultados de una evaluación para mejorar: priorizar, fijar metas, acciones y evidencias, y recibir comentarios con apertura y cuidado.",
    prior=["Sé usar una pauta.", "Sé dar y recibir retroalimentación.", "Sé fundar una postura."],
    explain=[
        "La evaluación sirve para decidir qué hacer después. Un plan de mejora tiene cuatro partes: qué criterio se mejorará (priorizando los de menor logro o los más importantes para el propósito), una meta concreta, una acción que se hará y la evidencia con que se comprobará. Por ejemplo: criterio C (puesta en escena), meta: que la luz cambie en el cierre; acción: probar luz baja en el cierre en el próximo ensayo; evidencia: registro en la bitácora y comentario de un par.",
        "Priorizar significa elegir pocas acciones realistas con el tiempo disponible. Si quedan 3 ensayos de 45 minutos, hay 135 minutos en total, y no se pueden mejorar diez cosas a la vez. Se empieza por lo más relevante y lo que tiene menor puntaje.",
        "Recibir comentarios con apertura significa escuchar, preguntar y decidir qué se usa; no es obligatorio aceptar todo. Si alguien recibe comentarios ofensivos o sobre su cuerpo, lo comunica a una persona adulta. El plan de mejora también cuida la salud: se mantiene el calentamiento y se respetan los límites del cuerpo.",
    ],
    vocab=[("plan de mejora", "acciones para elevar un criterio débil"), ("meta", "resultado concreto que se busca"), ("acción", "lo que se hará para lograr la meta"), ("prioridad", "lo que se trabaja primero"), ("evidencia de logro", "dato con que se comprueba la mejora")],
    worked=[
        ("Elegir la prioridad", "En la ficha, ¿qué criterios tienen menor puntaje?", ["C tiene 2 y D tiene 2.", "Son los dos candidatos a priorizar."], "C y D"),
        ("Armar un plan breve", "Plan para C: meta, acción y evidencia.", ["Meta: que el cierre se note por un cambio de luz.", "Acción: probar luz baja en el cierre. Evidencia: registro en la bitácora y comentario de un par."], "Meta: cierre con cambio de luz; acción: probarla; evidencia: bitácora y comentario"),
    ],
    mistakes=[("Proponer cambiar todo («mejorar todo»).", "No hay tiempo ni foco para lograrlo.", "Elige uno o dos criterios y una acción concreta."),
              ("Plan sin evidencia de logro.", "No se sabrá si mejoró.", "Define cómo se comprobará: bitácora, comentario de un par.")],
    T=[
        ('abc', '¿Qué es un plan de mejora?', 'Acciones concretas para mejorar un criterio débil', 'Una lista de los errores de cada persona', 'El horario de los ensayos, ordenado por fecha', 'Parte de la evaluación para actuar.'),
        ('abc', '{F} ¿Qué criterios convienen priorizar por puntaje?', 'C y D, que tienen 2', 'A, que tiene 3 puntos y es el criterio de propósito claro', 'B, que tiene 4 puntos y es el criterio de uso del espacio, el tiempo y la energía', 'Los de menor puntaje son C y D.'),
        ('=', '{F} ¿Cuántos minutos de ensayo quedan antes de la muestra?', '3*45', 'Se multiplican las semanas por los 45 minutos de cada ensayo.', ' minutos'),
        ('abc', '{F} El comentario «el cierre no se entiende» se relaciona con', 'puesta en escena o propósito', 'solo con el proceso de trabajo del grupo y no con la obra', 'el vestuario de las personas, que se nota poco en el cierre', 'Un cierre confuso afecta propósito y escena.'),
        ('abc', '{F} ¿Cuál es una meta concreta para C?', 'Que el cierre se note por un cambio de luz', 'Mejorar todo lo que se pueda en los tres ensayos que quedan', 'Ser mejores como grupo y que se note más en la muestra', 'Una meta debe ser observable para poder comprobarla.'),
        ('abc', '{F} ¿Qué evidencia comprobaría la mejora del criterio D?', 'Una bitácora completa de los ensayos restantes', 'Un aplauso del público', 'Un número más grande en la pauta, sin revisión', 'La evidencia debe mostrar el proceso.'),
        ('=', '{F} Si se dedican 15 minutos de cada ensayo al cierre, ¿cuántos minutos suman en los 3 ensayos?', '3*15', 'Se multiplican los ensayos por los minutos del cierre.', ' minutos'),
        ('abc', '{F} Un integrante propone trabajar A, B, C y D en el primer ensayo. ¿Qué respondes?', 'Elegir uno o dos criterios para que se alcance a mejorar con foco', 'Estar de acuerdo, porque todos los criterios son igual de importantes y hay que trabajarlos', 'Dejar de ensayar hasta tener claro qué criterio conviene mejorar primero', 'Priorizar permite lograr algo con el tiempo que hay.'),
        ('abc', '{F} Recibes el comentario «la bitácora está incompleta». ¿Qué decisión es adecuada?', 'Asignar un registro al final de cada ensayo y revisarlo en el siguiente', 'Ignorarlo, porque la bitácora no influye en la calidad de la obra', 'Culpar a la persona que debía escribir la bitácora y quitarle el rol', 'La acción es concreta y se puede revisar en el siguiente ensayo.'),
        ('abc', 'Alguien recibe un comentario sobre su cuerpo. ¿Qué corresponde?', 'Avisar a una persona adulta y recordar los acuerdos de respeto', 'Aceptarlo como parte de la crítica, porque el físico también forma parte de la obra', 'Cambiar su ropa de ensayo para que no se note su cuerpo y evitar nuevos comentarios', 'Los comentarios sobre el cuerpo no son críticas.'),
        ('=', 'Un grupo quiere subir C de 2 a 4 y D de 2 a 3. ¿Cuántos puntos pretende ganar?', '(4-2)+(3-2)', 'Se suman las mejoras de cada criterio.', ' puntos'),
        ('abc', 'Después de mejorar, el grupo vuelve a evaluar y C sube de 2 a 3. ¿Cómo se interpreta?', 'Mejoró, aunque quedan acciones para llegar a la meta', 'Fracasó, porque no llegó al puntaje máximo de 4 que se había propuesto', 'No sirvió el plan, porque el criterio sigue sin estar logrado del todo', 'El avance es parcial: mejoró, pero falta para la meta.'),
        ('abc', 'El plan incluye mantener un calentamiento de 10 minutos. ¿Para qué sirve?', 'Para cuidar el cuerpo y trabajar con seguridad', 'Para acortar el ensayo y tener más tiempo para otras tareas', 'Para evitar comentarios negativos de quienes miran la muestra', 'El plan incluye salud y seguridad.'),
    ],
    ctx=('abc', 'Con los resultados de la ficha, un grupo escribe: «Criterio C. Meta: que el cierre se note. Acción: probar luz baja en el cierre en el ensayo 1. Evidencia: registro y comentario de un par». ¿Qué falta para estar completo?', 'Nada esencial: tiene criterio, meta, acción y evidencia', 'Falta el nombre del grupo y la fecha de la muestra para que sea un plan', 'Falta una meta, porque solo se enuncia un criterio y una acción', 'Contiene las cuatro partes de un plan de mejora.'),
    sc=[
        ("En Danza: ¿qué partes tiene un plan de mejora?", "Criterio, meta, acción y evidencia", "Son las cuatro partes que hacen completo el plan."),
        ("¿Cómo se prioriza?", "Eligiendo pocas acciones realistas", "Se elige según el tiempo disponible antes de la muestra."),
        ("¿Qué se hace con comentarios sobre el cuerpo?", "Se avisa a una persona adulta", "Esos comentarios no son críticas válidas y se avisa."),
    ],
    op=("Con la ficha 5 u otros resultados inventados, escribe un plan de mejora para un criterio: meta, acción, evidencia y tiempo disponible. Explica por qué lo priorizas.",
        "Criterio D: proceso. Meta: bitácora completa en los 3 ensayos. Acción: una persona anota al final y otra revisa. Evidencia: tres entradas. Tiempo: 135 minutos de ensayo. Lo priorizo por tener 2 puntos.",
        ["criterio, meta, acción y evidencia", "justifica la prioridad", "usa el tiempo disponible"],
        ["hoja con plan de mejora"],
        ["mejorar todo a la vez", "plan sin evidencia de logro"],
        "Pregunta: «¿cómo sabrás que mejoró?». Si no hay evidencia, pídele definirla."),
    reinforce="Escribe un plan de mejora breve para una frase de danza imaginaria.",
    extend="Explica qué harías si el plan de mejora no funcionara en el primer intento.",
)
