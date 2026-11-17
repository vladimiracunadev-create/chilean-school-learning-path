"""Ciencias del ejercicio físico y deportivo, 3.º y 4.º medio HC: OAC-01 (variedad de actividades según intereses y necesidades), clases 1 a 4, y OAC-02 (adaptaciones agudas y crónicas), clases 1 a 5. Datos de ejemplo escritos en cada enunciado; sin video ni mediciones reales."""
from __future__ import annotations

from hc_cefd_common import build

O1 = "EF-CEFD-3y4-OAC-01"
O2 = "EF-CEFD-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Tomás anota en privado su situación. Interés principal: actividades en grupo y al aire libre. "
     "Condiciones: dispone de 45 minutos tres tardes por semana; cerca de su casa hay una plaza con espacio despejado y una cancha techada que abre solo los sábados; "
     "su profesora le pidió consultar a un profesional de la salud antes de hacer esfuerzos muy intensos. "
     "Actividades que le llaman la atención: fútbol recreativo en la plaza, natación en un recinto con salvavidas, tenis de mesa en la cancha techada y baile en el patio.")
build(
    O1, 1, F,
    use="Aprenderé a diagnosticar de forma privada mis intereses y mis condiciones para practicar una variedad de actividades físico-deportivas, respetando mis necesidades y las de otras personas, y a hacerlo con seguridad.",
    prior=["Sé que hay actividades individuales y colectivas.", "Sé hacer un calentamiento general.", "Sé que cada persona se mueve a su propio ritmo."],
    explain=[
        "Una actividad físico-deportiva es un movimiento corporal con metas o reglas: un deporte de equipo, la natación, el baile, una caminata o el tenis de mesa. Hay mucha variedad: actividades individuales o en grupo, al aire libre o bajo techo, con o sin oponente, suaves o intensas. Practicar variedad permite descubrir cuál nos gusta y mantener el hábito en el tiempo.",
        "Para elegir bien conviene un diagnóstico propio con dos partes. Los intereses son lo que me atrae (jugar en grupo, estar al aire libre). Las condiciones o necesidades son lo que debo considerar: tiempo disponible, lugar cercano, costo, nivel de práctica e indicaciones de salud. Respetar la individualidad es decidir con los datos de cada persona, sin copiar lo que hacen otras.",
        "El diagnóstico es privado: es una anotación mía y decido con quién la comparto. Nadie lo usa para ordenar a las personas ni para comentar su cuerpo. Al practicar, se hace calentamiento, se lleva agua y se respeta una señal de detención: ante dolor, mareo o lesión, se para y se avisa a una persona adulta o a un profesional de la salud.",
    ],
    vocab=[("actividad físico-deportiva", "movimiento corporal con metas o reglas"), ("interés", "lo que me atrae de una actividad"), ("condición o necesidad", "dato que debo considerar: tiempo, lugar, costo, salud"), ("individualidad", "características propias de cada persona"), ("diagnóstico privado", "anotación propia que decido compartir o no"), ("variedad", "práctica de actividades de distinto tipo")],
    worked=[
        ("Separar intereses y condiciones", "Un estudiante de ejemplo escribe: «Me gusta trotar con música, tengo 30 minutos los lunes y no tengo dinero para gimnasios». Ordénalo.", ["Interés: trotar con música.", "Condiciones: 30 minutos los lunes y ningún gasto.", "Con eso se buscan opciones gratuitas y de media hora."], "Interés: trotar; condiciones: 30 minutos y sin costo"),
        ("Revisar la variedad", "Un plan de ejemplo dice: lunes, miércoles y viernes, solo trote. ¿Tiene variedad?", ["Las tres sesiones son la misma actividad.", "Conviene cambiar una por otro tipo, como baile o un juego, según sus intereses."], "No: se cambia una sesión por otra actividad de su interés"),
    ],
    mistakes=[("Elegir una actividad solo porque la eligen mis amistades.", "Puede no calzar con mis intereses ni con mis condiciones, y se abandona pronto.", "Compara con mis propios datos antes de decidir."),
              ("Ignorar una indicación de un profesional de la salud porque «me siento bien».", "La indicación protege mi salud aunque hoy no sienta molestia.", "Respeta la indicación y consulta antes de aumentar la exigencia.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es una actividad físico-deportiva?', 'Un movimiento corporal con meta o reglas, como un deporte, un baile o una caminata', 'Solo un deporte de competencia que se juega con árbitro, equipo oficial y puntaje', 'Cualquier actividad que se hace con el cuerpo quieto, como mirar una pantalla', 'Incluye deportes, bailes y caminatas; no se limita a la competencia ni a la quietud.'),
        ('abc', '{F} ¿Cuál de las actividades de la ficha se practica en el agua?', 'Natación en un recinto con salvavidas', 'Baile en el patio', 'Tenis de mesa en la cancha techada', 'La natación es la única actividad nombrada que se hace en el agua.'),
        ('abc', '{F} ¿Cuál de estos datos es una condición (tiempo, lugar o salud) y no un gusto?', 'Dispone de 45 minutos tres tardes por semana', 'Le gustan las actividades en grupo', 'Le llama la atención el baile en el patio', 'El tiempo disponible es una condición; los otros dos datos son gustos.'),
        ('abc', '¿Por qué el diagnóstico de intereses y necesidades es privado?', 'Es una anotación propia y yo decido con quién la comparto', 'Debe esconderse del profesor para que nadie pueda corregir nada', 'Solo vale si otra persona lo lee y ordena al curso por su cuerpo', 'Privado significa que el registro es propio; no sirve para ordenar personas ni compararlas.'),
        ('abc', '{F} Tomás quiere practicar en grupo y al aire libre un día de semana por la tarde. ¿Qué lugar de la ficha calza?', 'La plaza con espacio despejado', 'La cancha techada, aunque abre solo los sábados', 'Ningún lugar, porque la ficha no nombra espacios al aire libre', 'La plaza es el espacio abierto cercano; la cancha techada no está disponible entre semana.'),
        ('abc', '¿Qué significa respetar la individualidad al elegir una actividad?', 'Considerar el nivel, el tiempo, el lugar y las indicaciones de salud de cada persona', 'Elegir la misma actividad para todo el curso para que nadie se sienta distinto', 'Elegir la actividad más exigente para que todas las personas se esfuercen igual', 'Cada persona tiene condiciones distintas, así que se decide con sus propios datos.'),
        ('=', '{F} Tomás dedica 10 minutos de cada tarde a calentar y enfriar, y el resto a la actividad principal. ¿Cuántos minutos de actividad principal hace en la semana?', '3*(45-10)', 'Se restan los 10 minutos a cada sesión de 45 y se multiplica por las tres tardes.', ' minutos'),
        ('ab', 'En el registro de Ana, que dice «me gusta bailar, tengo 30 minutos los martes y jueves y prefiero hacerlo en casa», ¿qué dato es una condición de tiempo a respetar?', 'Tiene 30 minutos los martes y jueves', 'Le gusta bailar, que es lo que más la atrae', 'El horario disponible es una condición; que le guste bailar es un interés.'),
        ('abc', '{F} Tomás quiere una actividad que calce con su interés principal y con la plaza cercana. ¿Cuál conviene?', 'Fútbol recreativo en la plaza, con intensidad acordada', 'Natación en el recinto con salvavidas, porque es una actividad completa', 'Tenis de mesa en la cancha techada, que abre solo los sábados', 'El fútbol recreativo es en grupo y al aire libre; las otras opciones no calzan con ambos datos.'),
        ('abc', 'Luis elige una actividad solo porque la eligen sus amistades, aunque no le atrae ni calza con su tiempo. Eva anota antes sus intereses y condiciones. ¿Quién respeta mejor su individualidad?', 'Eva, porque decide con sus propios intereses y condiciones', 'Luis, porque practicar con amistades siempre asegura constancia', 'Ambos igual, porque los dos terminan practicando algo', 'La individualidad se respeta decidiendo con datos propios y no por imitación.'),
        ('abc', 'Una compañera te pide ver tu diagnóstico para ordenar al curso de «más a menos apto». ¿Qué corresponde?', 'Responder que es tu registro privado y que no se usa para ordenar personas', 'Entregarlo, porque un orden del curso motiva a practicar más a todas las personas', 'Cambiar tus datos para quedar en un buen lugar del orden', 'El diagnóstico es privado y nadie lo usa para ordenar ni comparar a las personas.'),
        ('=', '{F} Tomás planea 4 semanas con 3 sesiones semanales de 45 minutos, de las cuales 10 minutos son calentamiento y enfriamiento. Por lluvia, en una semana solo hace 2 sesiones. ¿Cuántos minutos de actividad principal acumula?', '(3*3+2)*(45-10)', 'Se cuentan 11 sesiones hechas y a cada una se le restan 10 minutos de calentamiento y enfriamiento.', ' minutos'),
        ('abc', 'Un diagnóstico dice: «Soy malo para todos los deportes, así que no voy a practicar nada». ¿Qué defecto tiene para decidir?', 'Juzga a la persona y no registra intereses ni condiciones para elegir', 'Es demasiado largo y detallado para servir como punto de partida', 'Es correcto, porque un diagnóstico privado debe ser lo más crítico posible', 'Un diagnóstico sirve para elegir con datos; una etiqueta sobre uno mismo no aporta ninguno.'),
    ],
    ctx=('abc', 'Marcela anota: le gusta bailar con otras personas, tiene 40 minutos los lunes y miércoles, no puede pagar inscripciones y su profesora le sugirió empezar con esfuerzo suave. ¿Qué decisión de punto de partida es coherente?', 'Probar baile grupal gratuito en el patio, 40 minutos, con intensidad suave', 'Inscribirse a un curso de baile de pago de 90 minutos para empezar con más fuerza', 'Practicar sola un deporte intenso, porque es lo que más gasta energía', 'La opción coherente respeta interés, tiempo, costo y la sugerencia de empezar suave.'),
    sc=[
        ("En Educación Física: ¿qué dos cosas se anotan en un diagnóstico de intereses y necesidades?", "Intereses (lo que me atrae) y condiciones (tiempo, lugar, costo, salud)", "Con ambos se elige una actividad que se pueda sostener."),
        ("¿Quién decide con quién se comparte tu diagnóstico?", "Tú", "Es un registro privado y propio."),
        ("¿Qué haces si aparece dolor, mareo o lesión al practicar?", "Detenerte y avisar a una persona adulta o a un profesional de la salud", "La seguridad va antes que terminar la actividad."),
    ],
    op=("Elige uno de estos perfiles de ejemplo y escribe su diagnóstico privado con intereses y condiciones. Perfil A: le gusta jugar en equipo, tiene 30 minutos cuatro días y un patio techado. Perfil B: prefiere actividades solitarias, tiene 60 minutos los sábados y una plaza cerca. Perfil C: le gusta bailar, tiene 45 minutos tres días y no puede pagar inscripciones. Propón dos actividades distintas que calcen y una medida de seguridad.",
        "Perfil C. Intereses: bailar. Condiciones: 45 minutos, tres días, sin costo. Actividades: baile grupal en el patio y caminata con ritmo. Seguridad: calentar, llevar agua y, ante dolor o mareo, parar y avisar a una persona adulta.",
        ["separa intereses y condiciones", "propone dos actividades distintas que calzan", "incluye una medida de seguridad"],
        ["diagnóstico escrito con dos actividades"],
        ["escribir solo gustos sin condiciones", "juzgar a la persona en vez de registrar datos", "olvidar la seguridad"],
        "Pregunta: «¿qué dato de tus condiciones explica esa elección?». Si responde con un gusto, pídele una condición."),
    reinforce="Escribe en privado tus intereses y tus condiciones de la semana y propón dos actividades distintas que calcen. No compares tu registro con el de otra persona.",
    extend="Explica por qué practicar una variedad de actividades puede ayudar a mantener el hábito sin ignorar las necesidades de cada persona.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (caso de ejemplo, inventado). Camila elige entre cuatro opciones. Sus criterios, escritos en privado: (1) prefiere practicar con otras personas; (2) puede dedicar hasta 45 minutos por sesión; (3) no puede pagar inscripciones; (4) su profesional de la salud le pidió evitar saltos repetidos por ahora. "
     "Opción A: trote solitario de 30 minutos en la plaza. Opción B: baile grupal de 60 minutos en un gimnasio con inscripción de pago. "
     "Opción C: tenis de mesa grupal de 45 minutos en el patio, sin costo y sin saltos. Opción D: voleibol recreativo de 45 minutos en el patio, sin costo y con saltos frecuentes.")
build(
    O1, 2, F,
    use="Aprenderé a elegir una actividad físico-deportiva comparando opciones con criterios propios (interés, tiempo, costo y salud) y a adaptarla cuando algo no calza, sin copiar lo que eligen otras personas.",
    prior=["Sé separar intereses y condiciones.", "Sé que mi diagnóstico es privado.", "Conozco las señales de detención."],
    explain=[
        "Elegir una actividad no es dejarse llevar por el gusto del momento ni por lo que hace el grupo. Un criterio de elección es una razón o condición que uso para comparar opciones: me atrae, cabe en mi tiempo, no tiene costo, respeta las indicaciones de salud. Primero se escriben los criterios y después se miran las opciones, para que la decisión no sirva solo para justificar lo que ya quería.",
        "El método tiene cuatro pasos: listar los criterios, revisar cuáles cumple cada opción, descartar las que fallan en un criterio de salud o de imposibilidad (por ejemplo, un costo que no puedo pagar) y elegir la que cumple más criterios. Si dos opciones empatan, se agrega un criterio nuevo, como el horario o el lugar. Una opción que falla en salud se descarta o se adapta con ayuda de un profesional o del docente.",
        "Adaptar es cambiar una condición de la actividad para que calce: acortar el tiempo, bajar la intensidad, evitar saltos o jugar con reglas inclusivas para distintos niveles. Cada persona tiene criterios distintos, por eso una misma opción no sirve igual a todas. Si durante la práctica aparece dolor, mareo o lesión, se detiene y se avisa a una persona adulta o a un profesional de la salud.",
    ],
    vocab=[("criterio de elección", "razón o condición para comparar opciones"), ("opción", "actividad posible entre las que se compara"), ("descartar", "dejar fuera una opción porque falla en un criterio"), ("adaptar", "cambiar una condición para que la actividad calce"), ("desempate", "criterio nuevo que se agrega si dos opciones empatan")],
    worked=[
        ("Descartar con un criterio", "Un estudiante de ejemplo tiene 30 minutos por sesión y prefiere el aire libre. Opciones: (A) piscina techada de 60 minutos; (B) caminata en la plaza de 30 minutos. ¿Cuál elige?", ["El criterio de tiempo descarta la A, porque dura 60 y él tiene 30.", "La B cumple tiempo y aire libre."], "La opción B"),
        ("Adaptar con ayuda", "Una estudiante elige baile, pero su profesional de la salud pidió evitar saltos por ahora. ¿Descarta el baile?", ["No es necesario descartar toda la actividad: se puede adaptar una versión sin saltos.", "Lo consulta con su docente o con su profesional de la salud antes de empezar."], "Adaptar la actividad sin saltos, con ayuda"),
    ],
    mistakes=[("Elegir primero la opción favorita y buscar criterios que la apoyen.", "La decisión queda sesgada y no considera la salud ni las condiciones reales.", "Escribe los criterios antes de mirar las opciones."),
              ("Contar solo cuántos criterios cumple una opción sin mirar cuáles.", "Un criterio de salud pesa más que uno de comodidad.", "Descarta o adapta la opción que falla en salud, aunque cumpla otros.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es un criterio de elección?', 'Una razón o condición que uso para comparar opciones y decidir', 'El resultado final de un partido después de jugarlo con otro equipo', 'La cantidad de personas que miran una actividad desde afuera', 'Un criterio sirve para comparar opciones; no es un marcador ni el público.'),
        ('abc', '{F} ¿Qué opción queda descartada por el criterio (3), no pagar inscripciones?', 'Opción B, el baile grupal con inscripción de pago', 'Opción A, el trote solitario en la plaza', 'Opción D, el voleibol recreativo en el patio', 'Solo la opción B exige pagar inscripción.'),
        ('abc', '{F} ¿Qué opción queda descartada por el criterio (4), evitar saltos repetidos?', 'Opción D, el voleibol con saltos frecuentes', 'Opción C, el tenis de mesa en el patio', 'Opción A, el trote solitario en la plaza', 'La opción D es la única que dice tener saltos frecuentes.'),
        ('abc', '{F} ¿Por qué la opción A no cumple el criterio (1)?', 'Es un trote solitario y Camila prefiere practicar con otras personas', 'Dura 30 minutos y Camila tiene tiempo disponible para hacer más', 'Se practica en la plaza, y ella prefiere un patio cerrado', 'El criterio (1) pide compañía; que sobre tiempo o cambie el lugar no lo incumple.'),
        ('abc', '¿Qué se hace primero al decidir con criterios?', 'Escribir los criterios antes de mirar las opciones', 'Elegir la opción que más gusta y buscar criterios que la apoyen', 'Preguntar qué eligió el resto y copiar la respuesta', 'Con los criterios escritos primero, la decisión no se sesga hacia el gusto del momento.'),
        ('abc', '¿Qué indica que una opción cumple un criterio?', 'Que, según los datos de la opción, satisface lo que el criterio pide', 'Que a la mayoría del curso le gusta esa opción en particular', 'Que es la opción más intensa de todas las que se comparan', 'Cumplir un criterio se comprueba con los datos de la opción, no con la popularidad.'),
        ('abc', '{F} Aplicando los cuatro criterios, ¿qué opción conviene a Camila?', 'Opción C', 'Opción A', 'Opción D', 'La opción C es grupal, dura 45 minutos, no cuesta y no tiene saltos.'),
        ('=', '{F} Camila hace la opción C con 10 minutos de calentamiento y enfriamiento dentro de los 45 minutos. Si hace 2 sesiones por semana durante 3 semanas, ¿cuántos minutos de juego principal acumula?', '2*3*(45-10)', 'Se calculan las 6 sesiones y a cada una se le restan 10 minutos de calentamiento y enfriamiento.', ' minutos'),
        ('ab', 'Una opción cumple tres criterios, pero falla en uno de salud. ¿Qué conviene?', 'Descartarla o adaptarla con un profesional, pues la salud va primero', 'Elegirla igual porque cumple la mayoría de los criterios de la lista', 'Un criterio de salud pesa más que el número de criterios cumplidos.'),
        ('abc', 'Dos opciones cumplen todos los criterios de Camila. ¿Cómo se desempata?', 'Agregar un criterio nuevo, como el horario o el lugar, y volver a comparar', 'Elegir la más popular, porque la mayoría del grupo ya la eligió', 'Elegir la más cara, porque se supone que es mejor que las demás', 'Se agrega un criterio propio; la popularidad o el precio no son criterios de ella.'),
        ('abc', 'Un compañero dice: «Elige la opción de Camila, así todo el curso hace lo mismo». ¿Qué falla en ese razonamiento?', 'Los criterios de cada persona son distintos, por eso la misma opción no sirve a todas', 'Nada, porque una misma actividad para todo el curso es lo más justo y simple', 'Que Camila no debería tener criterios propios, porque el grupo decide', 'Cada persona tiene condiciones distintas; copiar una elección ignora la individualidad.'),
        ('=', '{F} En una semana de prueba, Camila hace 2 sesiones completas de la opción A y 2 de la opción C. ¿Cuántos minutos suman?', '2*30+2*45', 'Se suman los minutos de dos sesiones de 30 y de dos sesiones de 45.', ' minutos'),
        ('abc', 'Camila prueba la opción C y siente una molestia en la muñeca a los 4 minutos. ¿Qué decisión es correcta?', 'Detenerse, descansar y avisar a una persona adulta o a un profesional', 'Seguir con menos fuerza, porque la molestia es leve y pasará pronto', 'Terminar la sesión sin contarlo, para no perder el cupo del grupo', 'Una molestia es una señal de detención y se informa; seguir o callar puede agravarla.'),
    ],
    ctx=('abc', 'Diego tiene estos criterios: practicar en grupo, 30 minutos, sin costo y sin saltos por indicación de salud. Opciones: (1) caminata en grupo de 30 minutos en la plaza; (2) fútbol de 60 minutos con carreras y saltos; (3) trote solo de 30 minutos. ¿Cuál elige?', 'La opción 1, porque cumple los cuatro criterios', 'La opción 2, porque dura más y es más completa', 'La opción 3, porque cumple el tiempo, el costo y no tiene saltos', 'Solo la opción 1 cumple a la vez grupo, tiempo, costo y ausencia de saltos.'),
    sc=[
        ("En Educación Física: ¿qué se escribe antes de comparar las opciones?", "Los criterios", "Así la decisión no depende solo del gusto del momento."),
        ("¿Qué criterio manda si una opción puede afectar la salud?", "La salud: se descarta o se adapta con ayuda profesional", "La seguridad va antes que el gusto."),
        ("¿Se usa la elección de otra persona para decidir la mía?", "No: mis criterios son propios", "Cada persona tiene intereses y condiciones distintos."),
    ],
    op=("Escribe cuatro criterios propios (interés, tiempo, costo o lugar, y salud) y compara estas tres opciones de ejemplo: (A) caminata en grupo de 40 minutos en una plaza, sin costo; (B) natación individual de 60 minutos en un recinto con salvavidas y pago de entrada; (C) baile grupal de 30 minutos en el patio, sin costo. Elige una con tus criterios e indica una adaptación si algo no calza.",
        "Mis criterios: grupo, hasta 40 minutos, sin costo, esfuerzo suave. A cumple los cuatro; B falla en grupo, tiempo y costo; C cumple tres y dura 30. Elijo A. Adaptación: caminar a ritmo suave y, ante dolor o mareo, parar y avisar a una persona adulta.",
        ["cuatro criterios escritos antes de comparar", "revisa cada opción con los criterios", "elige y propone una adaptación o medida de seguridad"],
        ["tabla o texto con criterios, comparación y elección"],
        ["elegir por gusto sin criterios", "ignorar el criterio de salud", "copiar la elección de otra persona"],
        "Pregunta: «¿qué criterio descartó cada opción?». Si responde con el gusto, pídele el criterio."),
    reinforce="Elige una actividad de tu entorno y compárala con otra usando tres criterios escritos antes. Si algo no calza, anota una adaptación.",
    extend="Explica por qué un criterio de salud pesa más que un criterio de comodidad al elegir una actividad.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (plan semanal de ejemplo, inventado). Joaquín planifica así su semana. Lunes: caminata rápida de 40 minutos. Martes: descanso. Miércoles: baile en grupo de 45 minutos. Jueves: descanso. "
     "Viernes: tenis de mesa de 30 minutos. Sábado: fútbol recreativo de 60 minutos. Domingo: descanso. "
     "Cada sesión incluye calentamiento al inicio y enfriamiento al final dentro de su duración, y se lleva agua.")
build(
    O1, 3, F,
    use="Aprenderé a armar un plan semanal con variedad de actividades, descansos y cuidados, y a preparar una alternativa para cuando algo cambie, respetando mis necesidades.",
    prior=["Sé elegir actividades con criterios propios.", "Sé separar intereses y condiciones.", "Conozco las señales de detención."],
    explain=[
        "Un plan es una decisión escrita sobre qué voy a hacer, cuándo, cuánto tiempo y con qué cuidados. Cada momento de práctica es una sesión, que tiene calentamiento, parte principal y enfriamiento. Un plan semanal reparte las sesiones en los días y deja claro qué días se descansa.",
        "La variedad mejora el plan: alternar actividades de distinto tipo (de resistencia, de coordinación, de juego) permite trabajar capacidades diferentes y mantener el interés. El descanso entre sesiones da tiempo para recuperarse. Si se quiere cambiar algo, conviene cambiar una sola condición a la vez (por ejemplo, la duración de una sesión) para ver cómo responde el cuerpo.",
        "Un buen plan incluye un plan alternativo (plan B) para situaciones como lluvia, cansancio o falta de tiempo: una actividad parecida, más corta o bajo techo. También incluye cuidados: calentamiento, agua y señal de detención. Si aparece dolor, mareo o lesión, se detiene la práctica y se avisa a una persona adulta o a un profesional de la salud.",
    ],
    vocab=[("plan semanal", "decisión escrita de qué, cuándo y cuánto practicar en la semana"), ("sesión", "momento de práctica con calentamiento, parte principal y enfriamiento"), ("descanso", "día o pausa para recuperarse"), ("plan alternativo", "opción preparada para cuando el plan original no se puede"), ("progresión", "cambio gradual de una condición del plan")],
    worked=[
        ("Sumar el tiempo del plan", "Un plan de ejemplo tiene martes 30 minutos, jueves 35 y sábado 50. ¿Cuántos minutos suma?", ["Suma los minutos de las tres sesiones: 30 + 35 + 50.", "Anota también los días de descanso para que el plan quede completo."], "115 minutos"),
        ("Revisar la variedad", "Un plan de ejemplo dice: lunes, miércoles y viernes, trote de 30 minutos. ¿Cómo mejoras la variedad sin cambiar el tiempo?", ["Las tres sesiones son iguales.", "Cambia una por otra actividad de interés, como baile o un juego, y conserva los descansos."], "Cambiar una sesión por otra actividad de 30 minutos"),
    ],
    mistakes=[("Escribir solo la actividad y la duración.", "Falta lo que permite cuidarse y adaptarse: calentamiento, agua, descanso y plan alternativo.", "Agrega cuidados y un plan alternativo."),
              ("Cambiar varias condiciones del plan de una semana a otra.", "No se sabe cuál cambio produjo cansancio o mejora.", "Cambia una sola condición y observa cómo responde el cuerpo.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es una sesión?', 'Un momento de práctica con calentamiento, parte principal y enfriamiento', 'Un resumen que se escribe al terminar la semana y reemplaza al plan', 'Una competencia entre dos personas del curso con puntaje final', 'Una sesión es cada momento de práctica con sus tres partes.'),
        ('abc', '{F} ¿Qué días de la semana descansa Joaquín?', 'Martes, jueves y domingo', 'Lunes, miércoles y viernes', 'Miércoles, sábado y domingo', 'La ficha marca descanso el martes, el jueves y el domingo.'),
        ('abc', '{F} ¿Qué sesión de la semana de Joaquín dura más?', 'El fútbol recreativo del sábado', 'El baile en grupo del miércoles', 'La caminata rápida del lunes', 'El sábado dura 60 minutos, más que cualquier otra sesión.'),
        ('=', '{F} ¿Cuántos minutos de práctica suma Joaquín en la semana?', '40+45+30+60', 'Se suman los minutos de las cuatro sesiones del plan.', ' minutos'),
        ('abc', '¿Para qué sirve alternar actividades distintas en un plan?', 'Para trabajar capacidades variadas y mantener el interés', 'Para que cada sesión sea más corta que la anterior', 'Para evitar el calentamiento en las actividades suaves', 'La variedad trabaja capacidades distintas y mantiene el interés; no reemplaza el calentamiento.'),
        ('abc', '{F} ¿Por qué hay días de descanso entre algunas sesiones?', 'Para que el cuerpo se recupere antes de la sesión siguiente', 'Para comparar el cansancio con el de otras personas', 'Porque descansar reemplaza el calentamiento de la sesión', 'El descanso da tiempo de recuperación; no sirve para comparar ni reemplaza el calentamiento.'),
        ('abc', '{F} El sábado llueve y no puede jugar en la plaza. ¿Cuál es un plan alternativo adecuado?', 'Reemplazarlo por baile en un espacio techado, con calentamiento y agua', 'Duplicar la sesión del viernes para compensar la del sábado', 'Saltarse el calentamiento para terminar antes de que llueva más', 'Una alternativa parecida y segura mantiene el plan; duplicar sesiones o saltar el calentamiento lo debilita.'),
        ('=', '{F} Joaquín quiere pasar la caminata del lunes de 40 a 50 minutos, dejando el resto igual. ¿Cuántos minutos suma entonces la semana?', '50+45+30+60', 'Se suman los minutos con la caminata ya cambiada a 50 minutos.', ' minutos'),
        ('ab', '{F} Joaquín quiere practicar también un día de descanso. ¿Qué decisión conserva la recuperación del plan?', 'Agregar una sesión suave y corta, y mantener al menos un día de descanso en la semana', 'Convertir los tres días de descanso en sesiones intensas para avanzar rápido', 'Se mantiene la recuperación si la semana conserva descansos y la sesión nueva es suave.'),
        ('abc', 'Una estudiante propone: «Hagamos la misma actividad todos los días hasta cansarnos». ¿Qué debilidad tiene frente a un plan variado con descansos?', 'No da tiempo de recuperación ni variedad, y aumenta el cansancio excesivo', 'Ninguna, porque repetir la misma actividad asegura más progreso', 'Que es demasiado fácil de organizar para el curso', 'Sin descansos ni variedad no hay recuperación y crece el riesgo de cansancio excesivo.'),
        ('abc', 'Joaquín anota «viernes: tenis de mesa, 30 minutos» y nada más. ¿Qué le falta a su plan?', 'Los cuidados y un plan alternativo, además de qué, cuándo y cuánto', 'Nada: un plan solo necesita la actividad y la duración', 'Un compañero que lo evalúe y lo compare con su cuerpo', 'Un plan completo incluye cuidados y alternativa; comparar cuerpos no corresponde.'),
        ('=', '{F} Cada sesión incluye 10 minutos entre calentamiento y enfriamiento. ¿Cuántos minutos de parte principal tiene la semana completa?', '40+45+30+60-4*10', 'Se suman los minutos de las cuatro sesiones y se restan los 10 minutos de cada una.', ' minutos'),
        ('abc', '{F} Joaquín llega muy cansado el viernes. ¿Qué decisión de regulación es más razonable?', 'Hacer el tenis de mesa más suave o más corto y observar cómo se siente', 'Hacer el tenis de mesa más fuerte para compensar el cansancio', 'Eliminar el descanso del jueves de la semana siguiente', 'Ante cansancio se baja la exigencia; aumentarla o quitar descansos empeora la recuperación.'),
    ],
    ctx=('abc', 'Fernanda planifica: lunes y jueves, trote suave de 30 minutos; martes, baile de 40; sábado, caminata de 60; los demás días descansa. Una semana de pruebas tiene poco tiempo. ¿Qué ajuste mantiene el sentido del plan?', 'Reducir cada sesión a 20 minutos y conservar los días de descanso', 'Convertir los días de descanso en sesiones largas para recuperar tiempo', 'Dejar de practicar sin avisar a nadie hasta que terminen las pruebas', 'Acortar las sesiones mantiene la práctica y los descansos; los otros cambios quitan recuperación o abandonan el plan.'),
    sc=[
        ("En Educación Física: ¿qué partes tiene una sesión?", "Calentamiento, parte principal y enfriamiento", "Así se cuida el cuerpo antes y después del esfuerzo."),
        ("¿Para qué sirve un plan alternativo?", "Para cuando llueve, hay cansancio o falta tiempo", "Mantiene la práctica sin arriesgar la seguridad."),
        ("¿Cuántas condiciones conviene cambiar a la vez en un plan?", "Una sola", "Así se sabe qué produjo el efecto."),
    ],
    op=("Arma un plan semanal de ejemplo para una persona ficticia que tiene 40 minutos en cinco días de la semana, le gusta el juego en grupo y no puede pagar inscripciones. Incluye al menos tres actividades distintas, dos días de descanso, calentamiento, agua y un plan alternativo para un día de lluvia.",
        "Lunes: juego con pelota blanda, 40 min. Martes: descanso. Miércoles: baile, 40 min. Jueves: caminata rápida, 40 min. Viernes: descanso. Sábado: juego de grupo, 40 min. Domingo: caminata suave, 30 min. Plan B de lluvia: baile bajo techo. Cuidados: calentar, agua; ante dolor o mareo, paro y aviso.",
        ["tres actividades distintas y dos descansos", "calentamiento, agua y señal de detención", "plan alternativo realista"],
        ["tabla o lista de la semana con cuidados y plan B"],
        ["repetir la misma actividad todos los días", "no escribir descansos", "olvidar el plan alternativo"],
        "Pregunta: «¿qué haces si un día llueve o estás muy cansada?». Si no tiene respuesta, pídele el plan alternativo."),
    reinforce="Escribe en papel un plan de tu semana con tres actividades distintas y dos descansos, y anota qué harías si llueve.",
    extend="Explica por qué cambiar una sola condición a la vez permite entender mejor cómo responde el cuerpo a un plan.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (registro de ejemplo, inventado). Plan: 4 sesiones por semana. Semana 1: 4 sesiones hechas, esfuerzo percibido promedio 5 de 10, disfrute 4 de 5. "
     "Semana 2: 3 sesiones hechas, esfuerzo 7, disfrute 3. Semana 3: 2 sesiones hechas, esfuerzo 8, disfrute 2 y la anotación «mucho cansancio». "
     "Escala de esfuerzo: 1 es muy suave y 10 es muy duro. Escala de disfrute: 1 es nada y 5 es mucho.")
build(
    O1, 4, F,
    use="Aprenderé a registrar sesiones, esfuerzo y disfrute, a interpretar el registro y a ajustar una condición del plan para seguir practicando con seguridad y respetando mis necesidades.",
    prior=["Sé armar un plan semanal con descansos.", "Sé que cambio una sola condición a la vez.", "Conozco las señales de detención."],
    explain=[
        "Registrar es anotar lo que ocurrió para decidir mejor. Tres datos sencillos bastan: cuántas sesiones hice de las planificadas, qué tan duro sentí el esfuerzo (de 1 a 10) y cuánto disfruté (de 1 a 5). La adherencia es la proporción de sesiones planificadas que logré hacer; si planifiqué 4 y hice 3, mi adherencia fue 3 de 4, o 75 %.",
        "Interpretar es buscar patrones: ¿cuando sube el esfuerzo bajan las sesiones hechas y el disfrute? Esa combinación es una señal de que conviene regular el plan, por ejemplo con sesiones más suaves o más cortas. No se corrige una semana floja con una semana de castigo ni se abandona el plan: se revisa la causa y se ajusta una sola condición.",
        "Un registro es propio y privado: sirve para compararme conmigo en otro momento, no con otras personas. Si el cansancio no se va o aparecen dolor, mareo o lesión, se detiene la práctica y se avisa a una persona adulta o a un profesional de la salud.",
    ],
    vocab=[("adherencia", "proporción de sesiones planificadas que se logran hacer"), ("esfuerzo percibido", "qué tan duro siento el ejercicio, de 1 a 10"), ("disfrute", "cuánto me gustó la práctica, de 1 a 5"), ("patrón", "regularidad que se repite en un registro"), ("regulación", "ajustar el plan según lo que registro")],
    worked=[
        ("Calcular la adherencia", "Un registro de ejemplo: 2 semanas con 3 sesiones planificadas cada una; hizo 3 y 2. ¿Cuántas de las sesiones planificadas logró hacer?", ["Sesiones planificadas: 3 + 3 = 6. Sesiones hechas: 3 + 2 = 5.", "Se anota como «5 de 6 sesiones»: es la adherencia, sin necesidad de más cálculos."], "5 de 6 sesiones"),
        ("Decidir un ajuste", "Con esfuerzo 8, disfrute 2 y mucho cansancio, ¿qué ajusto?", ["Hay un patrón de exceso de exigencia.", "Bajo el esfuerzo con sesiones más suaves y vuelvo a registrar las tres cosas."], "Sesiones más suaves y nuevo registro"),
    ],
    mistakes=[("Anotar solo «cumplí» o «no cumplí».", "No indica esfuerzo ni disfrute, que permiten entender por qué pasó.", "Anota sesiones, esfuerzo y disfrute."),
              ("Compensar sesiones perdidas con más sesiones intensas.", "Aumenta el cansancio y baja el disfrute.", "Revisa la causa y ajusta una sola condición.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es la adherencia a un plan?', 'La proporción de sesiones planificadas que se logran hacer', 'La fuerza con que se hace cada ejercicio de la sesión', 'El número de personas que practican contigo cada semana', 'La adherencia compara sesiones hechas con sesiones planificadas.'),
        ('=', '{F} ¿Cuántas sesiones hizo en total en las tres semanas?', '4+3+2', 'Se suman las sesiones hechas en cada una de las tres semanas.', ' sesiones'),
        ('abc', '{F} ¿En qué semana fue mayor el disfrute?', 'En la semana 1', 'En la semana 2', 'En la semana 3', 'El disfrute fue 4 de 5 en la semana 1, el más alto del registro.'),
        ('=', '{F} ¿Qué porcentaje de las sesiones planificadas en las tres semanas logró hacer?', '(4+3+2)/12*100', 'Se divide el total de sesiones hechas entre las 12 planificadas y se pasa a porcentaje.', ' %'),
        ('abc', '{F} ¿Qué patrón muestra el registro de las tres semanas?', 'Al subir el esfuerzo bajaron las sesiones hechas y el disfrute', 'Al subir el esfuerzo subió el disfrute y también las sesiones', 'El esfuerzo, las sesiones y el disfrute se mantuvieron iguales', 'El esfuerzo pasó de 5 a 8 mientras sesiones y disfrute bajaron.'),
        ('abc', '{F} ¿Qué dato indica con más claridad que conviene regular el plan?', 'Esfuerzo 8 de 10, disfrute 2 de 5 y mucho cansancio en la semana 3', 'Esfuerzo 5 de 10 y disfrute 4 de 5, con las 4 sesiones hechas', 'Haber hecho 4 sesiones en la semana 1, que es la mejor semana', 'La combinación de esfuerzo alto, poco disfrute y cansancio es la señal de ajustar.'),
        ('abc', '{F} ¿Qué ajuste de una sola condición es coherente con el esfuerzo y el disfrute anotados?', 'Bajar el esfuerzo con sesiones más suaves y volver a registrar', 'Subir el esfuerzo en la semana 4 para compensar las sesiones perdidas', 'Cambiar actividad, horario y duración a la vez para empezar de cero', 'Un ajuste simple y suave cuida el cansancio y permite ver el efecto.'),
        ('=', 'Si en la semana 4 de otro registro hace 3 sesiones y en la semana 5 hace 4, y las semanas 1 a 3 sumaron 9 sesiones, ¿qué porcentaje de las 20 sesiones planificadas en las cinco semanas logró?', '(9+3+4)/20*100', 'Se suman las sesiones hechas en las cinco semanas y se dividen entre las 20 planificadas.', ' %'),
        ('ab', 'Mara anota solo «cumplí el plan». Teo anota sesiones, esfuerzo y disfrute. ¿Qué registro permite regular mejor?', 'El de Teo, porque aporta tres datos para decidir ajustes', 'El de Mara, porque es más corto y basta para saber cómo va', 'Con esfuerzo y disfrute se entiende por qué ocurrió lo registrado y qué ajustar.'),
        ('abc', 'Un estudiante concluye: «Hice menos sesiones, debo castigarme con una semana de más sesiones». ¿Qué corresponde?', 'Revisar por qué bajó la adherencia, como cansancio o poco tiempo, y ajustar', 'Aceptar el castigo, porque compensar las sesiones perdidas es obligatorio', 'Abandonar el plan para siempre porque no se cumplió', 'Se revisa la causa y se ajusta; ni castigarse ni abandonar corrigen el problema.'),
        ('abc', 'Dos estudiantes tienen 75 % de adherencia. Una practica con disfrute 4 de 5 y la otra con disfrute 2 de 5 y mucho cansancio. ¿Qué plan conviene revisar primero?', 'El de la segunda, porque el cansancio y el bajo disfrute amenazan que siga', 'El de la primera, porque disfrutar mucho de practicar distrae del objetivo', 'Ninguno, porque el mismo porcentaje indica que ambos están igual de bien', 'El porcentaje no cuenta toda la historia: el cansancio y el bajo disfrute piden ajuste.'),
        ('=', '{F} Cada sesión dura 45 minutos. ¿Cuántos minutos de práctica hizo en las tres semanas?', '(4+3+2)*45', 'Se multiplican las 9 sesiones hechas por 45 minutos cada una.', ' minutos'),
        ('abc', '{F} En la semana 4 siente un dolor que no es solo cansancio. ¿Qué hace?', 'Detenerse y avisar a una persona adulta o a un profesional de la salud', 'Seguir con sesiones suaves para que el dolor pase solo con el tiempo', 'Anotar el dolor y esperar a la semana 5 para decidir qué hacer', 'El dolor es una señal de detención y se informa de inmediato.'),
    ],
    ctx=('abc', 'Ignacio registra tres semanas de ejemplo: adherencia 100 %, 75 % y 50 %; esfuerzo 4, 6 y 8; disfrute 5, 3 y 2. ¿Qué decisión es más razonable para la semana 4?', 'Reducir el esfuerzo a un nivel suave, mantener tres sesiones y volver a registrar', 'Subir el esfuerzo a 9 para recuperar el 100 % de adherencia de la semana 1', 'Mantener todo igual y dejar de registrar, para no complicarse con los datos', 'Con esfuerzo creciente y disfrute decreciente, se baja el esfuerzo y se sigue registrando.'),
    sc=[
        ("En Educación Física: ¿qué tres datos se anotan en cada semana?", "Sesiones hechas, esfuerzo percibido y disfrute", "Con los tres se entiende cómo respondió la persona."),
        ("Si el esfuerzo sube y el disfrute baja, ¿qué se hace?", "Se regula el plan: sesiones más suaves y nuevo registro", "Insistir con más exigencia empeora el cansancio."),
        ("¿Con quién se compara un registro propio?", "Conmigo en otro momento", "Cada persona tiene condiciones e intereses propios y distintos."),
    ],
    op=("Completa este registro de ejemplo para una persona ficticia: semana 1 con 3 sesiones planificadas, esfuerzo 5 y disfrute 4; semana 2 con 3 planificadas, esfuerzo 7 y disfrute 3. Inventa cuántas sesiones hizo en cada semana, calcula la adherencia, interpreta el patrón y propone un ajuste de una sola condición y una medida de seguridad.",
        "Semana 1: hizo 3 de 3. Semana 2: hizo 2 de 3. Adherencia: 5 de 6. Patrón: al subir el esfuerzo bajaron sesiones y disfrute. Ajuste: sesiones más suaves la semana 3. Seguridad: calentar y, ante dolor o mareo, parar y avisar.",
        ["calcula la adherencia", "interpreta un patrón con los datos", "propone un solo ajuste y una medida de seguridad"],
        ["registro de dos semanas con interpretación y ajuste"],
        ["anotar solo si cumplió", "compensar con más sesiones", "cambiar varias condiciones a la vez"],
        "Pregunta: «¿qué pasó con el disfrute cuando subió el esfuerzo?». Si no mira el registro, pídele que lo relea."),
    reinforce="Durante una semana anota en papel cuántas sesiones planificadas hiciste, tu esfuerzo de 1 a 10 y tu disfrute de 1 a 5. Compara solo contigo.",
    extend="Explica por qué la adherencia sola no basta para decidir si un plan es adecuado para una persona.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 5 (registro de ejemplo, inventado, de una persona ficticia llamada Valentina en una sesión de trote suave). En reposo, sentada: 18 latidos en 15 segundos y 14 respiraciones por minuto. "
     "Después de 5 minutos de trote suave: 35 latidos en 15 segundos y 30 respiraciones por minuto, con sudoración. Tres minutos después de detenerse: 24 latidos en 15 segundos. "
     "Para pasar a latidos por minuto se multiplica por 4.")
build(
    O2, 1, F,
    use="Aprenderé a distinguir las respuestas agudas del cuerpo al ejercicio (las que ocurren durante y justo después) midiendo antes, durante y después, y a hacerlo con seguridad.",
    prior=["Sé hacer un calentamiento general.", "Sé que cada persona responde a su ritmo.", "Sé que ante dolor o mareo se detiene la práctica."],
    explain=[
        "Una respuesta aguda es un cambio inmediato y temporal que ocurre durante o justo después de un ejercicio y que vuelve hacia los valores de reposo al descansar. Las más conocidas son: el corazón late más rápido (aumenta la frecuencia cardíaca), la respiración se hace más rápida, aparece sudoración, sube la temperatura del cuerpo y llega más sangre a los músculos que trabajan.",
        "Para observarlas se mide en tres momentos: en reposo (punto de comparación), durante o justo al terminar el ejercicio, y en la recuperación. El pulso se toma en la muñeca con dos dedos, sin usar el pulgar ni presionar fuerte, contando 15 segundos y multiplicando por 4 para obtener los latidos por minuto. Siempre se miden las mismas condiciones: sentado, mismo lugar y misma forma de contar.",
        "Estos datos son propios y privados: sirven para comparar a la persona con ella misma, no con otras. Si durante la práctica aparecen mareo, dolor en el pecho, falta de aire inusual o malestar fuerte, se detiene la actividad, se descansa y se avisa a una persona adulta o a un profesional de la salud.",
    ],
    vocab=[("respuesta aguda", "cambio inmediato y temporal durante o justo después del ejercicio"), ("frecuencia cardíaca", "latidos del corazón por minuto"), ("reposo", "estado sin actividad, sentado y tranquilo"), ("recuperación", "vuelta hacia los valores de reposo tras el ejercicio"), ("ventilación", "ritmo de respiración")],
    worked=[
        ("Convertir un pulso de 15 segundos", "En reposo, una persona de ejemplo cuenta 21 latidos en 15 segundos. ¿Cuántos latidos por minuto son?", ["Se multiplica por 4 porque 15 segundos son un cuarto de minuto.", "21 × 4 = 84."], "84 latidos por minuto"),
        ("Calcular la subida", "En reposo, 80 latidos por minuto; durante un trote suave, 128. ¿Cuánto subió?", ["Se resta el valor de reposo al valor durante el ejercicio.", "128 − 80 = 48."], "48 latidos por minuto más"),
    ],
    mistakes=[("Medir el pulso con el pulgar o presionando fuerte el cuello.", "El pulgar tiene su propio pulso y presionar fuerte el cuello puede ser inseguro.", "Usa dos dedos en la muñeca, sin presionar fuerte."),
              ("Creer que un pulso alto durante el ejercicio es una enfermedad.", "Subir con el esfuerzo es una respuesta aguda normal.", "Compara con el reposo y observa si vuelve a bajar al descansar.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es una respuesta aguda al ejercicio?', 'Un cambio inmediato y temporal que ocurre durante o justo después del ejercicio', 'Un cambio permanente que aparece después de varios meses de práctica', 'Una lesión repentina que ocurre durante la práctica del ejercicio', 'Aguda significa inmediata y temporal; los cambios de meses son otra cosa.'),
        ('abc', '{F} ¿Qué midió Valentina cuando contó 18 latidos en 15 segundos?', 'Su frecuencia cardíaca en reposo', 'Su frecuencia cardíaca después del trote', 'Su ritmo de respiración en reposo', 'Contar latidos en reposo mide la frecuencia cardíaca en reposo.'),
        ('=', '{F} ¿Cuántos latidos por minuto tiene Valentina en reposo?', '18*4', 'Se multiplican los latidos de 15 segundos por 4 para llegar a un minuto.', ' latidos por minuto'),
        ('=', '{F} ¿Cuántos latidos por minuto tiene después de los 5 minutos de trote?', '35*4', 'Se multiplican los 35 latidos de 15 segundos por 4.', ' latidos por minuto'),
        ('abc', '{F} ¿Qué cambió con el trote, además del pulso?', 'La respiración pasó de 14 a 30 por minuto y apareció sudoración', 'La respiración bajó de 30 a 14 por minuto mientras trotaba', 'La sudoración desapareció y la respiración se mantuvo igual', 'Con el esfuerzo subió la respiración y apareció sudoración.'),
        ('abc', '¿Por qué se mide primero en reposo, antes del ejercicio?', 'Para tener un punto de comparación con lo que ocurre durante y después', 'Para poder omitir el calentamiento si el pulso está bajo', 'Para decidir qué persona del curso tiene mejor pulso', 'El reposo es la referencia; no reemplaza el calentamiento ni sirve para comparar personas.'),
        ('=', '{F} ¿Cuántos latidos por minuto bajó el pulso de Valentina en los 3 minutos de recuperación, desde el valor después del trote?', '35*4-24*4', 'Se pasan ambos pulsos a latidos por minuto y se restan.', ' latidos por minuto'),
        ('abc', '{F} Valentina anota 30 latidos en 15 segundos un minuto después de detenerse. ¿Qué indica comparado con los 24 de tres minutos después?', 'A los 3 minutos su pulso estaba más cerca del valor de reposo', 'Su pulso estaba más bajo al minuto que a los 3 minutos', 'Su pulso se quedó igual de alto y dejó de recuperarse', '30 latidos en 15 segundos son más que 24, así que el pulso seguía bajando.'),
        ('ab', '¿Cómo se toma el pulso con el método de 15 segundos?', 'Con dos dedos en la muñeca, contando 15 segundos y multiplicando por 4', 'Con el pulgar presionando fuerte el cuello durante 5 segundos', 'El método seguro usa dos dedos en la muñeca y presión suave.'),
        ('abc', 'Una estudiante dice: «Mi pulso subió mucho al correr, así que algo anda mal». ¿Qué corresponde?', 'Es una respuesta aguda esperable; se compara con el reposo y se observa si baja', 'Es una señal de que no debió calentar y debe terminar la sesión de inmediato', 'Significa que debe aumentar la intensidad hasta que el pulso baje solo', 'El pulso sube con el esfuerzo y vuelve a bajar al descansar; es una respuesta aguda.'),
        ('abc', 'Durante una medición aparecen mareo y falta de aire inusual. ¿Qué hace la persona?', 'Detenerse, sentarse y avisar a una persona adulta o a un profesional', 'Medir el pulso de nuevo mientras sigue trotando para ver si baja', 'Aumentar el ritmo para que el malestar pase rápido y terminar la sesión', 'Mareo y falta de aire inusual son señales de detención.'),
        ('=', '{F} Valentina repite el trote y obtiene 38 latidos en 15 segundos. ¿Cuántos latidos por minuto más que en la ficha?', '38*4-35*4', 'Se pasan ambos pulsos a latidos por minuto y se resta el primero al segundo.', ' latidos por minuto'),
        ('abc', '{F} ¿Qué conclusión sostienen los datos de la ficha?', 'El pulso y la respiración subieron con el trote y el pulso bajó, sin llegar aún al reposo', 'El pulso volvió al valor de reposo a los 3 minutos y la respiración también', 'El trote no cambió ninguna medición, solo apareció sudoración al terminar', 'A los 3 minutos el pulso era 96 por minuto, más alto que los 72 de reposo.'),
    ],
    ctx=('abc', 'Sofía mide su pulso: reposo 76 latidos por minuto; durante una caminata rápida 112; 2 minutos después de detenerse 88. ¿Qué es correcto?', 'Su pulso subió con el esfuerzo y bajó al descansar sin llegar aún al valor de reposo', 'Su pulso subió y quedó igual de alto, lo que muestra que no responde al descanso','Su pulso es incorrecto, porque debe ser igual en reposo y en caminata', 'El pulso subió de 76 a 112 y bajó a 88: es una respuesta aguda que aún se recupera.'),
    sc=[
        ("En Ciencias del ejercicio: ¿cuánto dura una respuesta aguda?", "Es temporal: ocurre durante o justo después del ejercicio y vuelve hacia el reposo", "Eso la distingue de un cambio duradero."),
        ("¿Cómo se pasa un pulso de 15 segundos a latidos por minuto?", "Multiplicando por 4", "Quince segundos son un cuarto de minuto."),
        ("¿Qué haces si aparecen mareo o falta de aire inusual?", "Detenerte, descansar y avisar a una persona adulta o a un profesional de la salud", "La seguridad va antes que terminar la medición."),
    ],
    op=("Con estos datos de ejemplo de una persona ficticia: reposo 20 latidos en 15 segundos; después de 4 minutos de caminata rápida 31 latidos en 15 segundos; 2 minutos después de detenerse 25 latidos en 15 segundos. Convierte cada valor a latidos por minuto, calcula la subida y la bajada, y explica qué respuesta aguda observas. Menciona una señal para detener la práctica.",
        "Reposo 80; caminata 124; recuperación 100. Subió 44 y bajó 24. Es una respuesta aguda: el pulso sube con el esfuerzo y baja al descansar sin llegar aún al reposo. Si hay mareo o falta de aire inusual, paro y aviso.",
        ["convierte los tres pulsos a latidos por minuto", "calcula subida y bajada", "explica la respuesta aguda y una señal de detención"],
        ["tabla con tres valores y dos diferencias"],
        ["olvidar multiplicar por 4", "no comparar con el reposo", "no mencionar la seguridad"],
        "Pregunta: «¿cuál es tu punto de comparación y por qué?». Si no nombra el reposo, pídele que lo busque en los datos."),
    reinforce="Con una persona adulta de tu casa, toma tu pulso de reposo sentado, con dos dedos en la muñeca, durante 15 segundos y multiplica por 4. Si te mareas, detente.",
    extend="Explica por qué las respuestas agudas se miden mejor comparando con el reposo de la misma persona.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 6 (observaciones de ejemplo, inventadas, sobre una persona ficticia). a) Durante una carrera suave, su pulso sube a 150 latidos por minuto. "
     "b) Tras 8 semanas de entrenamiento regular, su pulso en reposo bajó de 74 a 68 latidos por minuto. c) Durante el esfuerzo aparece sudoración. "
     "d) Tras 6 semanas de práctica, puede trotar 12 minutos seguidos; antes solo 8. e) Al correr, su respiración se hace más rápida. "
     "f) Tras 10 semanas de práctica regular, su fuerza de agarre en una prueba de ejemplo aumentó.")
build(
    O2, 2, F,
    use="Aprenderé a distinguir una adaptación aguda de una adaptación crónica según cuándo aparece y cuánto dura, y a reconocer ejemplos de cada una.",
    prior=["Sé qué es una respuesta aguda.", "Sé medir y convertir el pulso.", "Sé que cada persona responde a su ritmo."],
    explain=[
        "Una adaptación aguda es la respuesta temporal del cuerpo durante o justo después de un ejercicio: sube el pulso, se acelera la respiración, aparece sudoración. Desaparece al descansar. Una adaptación crónica es un cambio duradero que aparece tras semanas o meses de entrenamiento regular, como un pulso de reposo más bajo, más resistencia para sostener un esfuerzo o más fuerza muscular.",
        "Para clasificar se hacen dos preguntas: ¿cuándo aparece (durante la sesión o tras semanas de práctica regular)? y ¿se mantiene en el reposo (sí, si es crónica; no, si es aguda)? Las adaptaciones crónicas dependen de practicar con regularidad y recuperarse bien. Además son reversibles: si se deja de practicar por mucho tiempo, se van perdiendo poco a poco.",
        "Cada persona se adapta a su ritmo: dos personas con el mismo plan pueden cambiar distinto, y eso no las hace mejores ni peores. Por eso las adaptaciones se comparan solo con las mediciones anteriores de la misma persona. Ante dolor, mareo o malestar, se detiene la práctica y se avisa a una persona adulta o a un profesional de la salud.",
    ],
    vocab=[("adaptación aguda", "respuesta temporal durante o justo después del ejercicio"), ("adaptación crónica", "cambio duradero tras semanas o meses de práctica regular"), ("resistencia", "capacidad de sostener un esfuerzo por más tiempo"), ("reversibilidad", "pérdida gradual de las adaptaciones al dejar de practicar"), ("fuerza muscular", "capacidad de los músculos para vencer una resistencia")],
    worked=[
        ("Clasificar una observación", "Una persona de ejemplo anota: «mientras pedaleo mi respiración se acelera». ¿Aguda o crónica?", ["Aparece durante el ejercicio.", "Al descansar vuelve a la normalidad: es temporal."], "Aguda"),
        ("Clasificar otra observación", "Tras 12 semanas, una persona de ejemplo sube 6 escalones más sin detenerse que al empezar. ¿Aguda o crónica?", ["Apareció después de semanas de práctica regular.", "Se mantiene fuera de la sesión: es un cambio duradero."], "Crónica"),
    ],
    mistakes=[("Llamar «adaptación crónica» a cualquier aumento del pulso durante un ejercicio.", "Ese aumento es temporal y desaparece al descansar.", "Pregunta cuánto dura y cuándo aparece."),
              ("Pensar que una adaptación crónica se mantiene aunque se deje de practicar por meses.", "Las adaptaciones son reversibles.", "Mantén la práctica regular para conservarlas.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es una adaptación crónica?', 'Un cambio duradero que aparece tras semanas o meses de entrenamiento regular', 'Un cambio que dura solo mientras se hace ejercicio y luego desaparece', 'Una molestia que aparece después de un solo día de práctica intensa', 'Crónica significa duradera y asociada a práctica regular de semanas o meses.'),
        ('abc', '{F} ¿Cuál observación es una adaptación aguda?', 'La a: el pulso sube a 150 durante la carrera suave', 'La b: el pulso en reposo bajó de 74 a 68 tras 8 semanas', 'La d: puede trotar 12 minutos seguidos tras 6 semanas', 'Solo la a ocurre durante el esfuerzo y es temporal.'),
        ('abc', '{F} ¿Cuál observación es una adaptación crónica?', 'La b: el pulso en reposo bajó de 74 a 68 tras 8 semanas', 'La c: aparece sudoración durante el esfuerzo de la carrera', 'La e: la respiración se acelera durante la carrera suave', 'La b es un cambio duradero que aparece tras semanas de práctica.'),
        ('abc', '{F} Clasifica la observación e, la respiración más rápida al correr.', 'Aguda, porque ocurre durante el esfuerzo y se normaliza al descansar', 'Crónica, porque aparece con el entrenamiento regular de semanas', 'Crónica, porque dura todo el día después de la carrera', 'La respiración acelerada es temporal: se normaliza al terminar el esfuerzo.'),
        ('abc', '{F} ¿Qué observación muestra mayor resistencia tras entrenar?', 'La d: trota 12 minutos seguidos tras 6 semanas, en vez de 8', 'La c: aparece sudoración durante el esfuerzo de la carrera', 'La a: el pulso sube a 150 latidos durante la carrera', 'La d muestra que sostiene más tiempo el esfuerzo tras semanas de práctica.'),
        ('=', '{F} ¿Cuántos latidos por minuto bajó el pulso en reposo con las 8 semanas de entrenamiento?', '74-68', 'Se resta el pulso de reposo final al inicial.', ' latidos por minuto'),
        ('abc', 'Una persona deja de entrenar 3 meses y su pulso en reposo vuelve a 74. ¿Qué ilustra?', 'Reversibilidad: las adaptaciones se pierden poco a poco si se deja de entrenar', 'Que el entrenamiento nunca produjo ningún cambio real', 'Que el pulso en reposo siempre vuelve a 74 en todas las personas', 'La vuelta del valor inicial tras una pausa larga muestra reversibilidad.'),
        ('=', '{F} En la observación d, ¿en qué porcentaje aumentó el tiempo que puede trotar seguido, respecto de los 8 minutos iniciales?', '(12-8)/8*100', 'Se calcula el aumento de 4 minutos y se divide entre el tiempo inicial de 8 minutos.', ' %'),
        ('ab', 'Una persona hace una sola sesión intensa y al día siguiente nota cansancio. ¿Es una adaptación crónica?', 'No: es un efecto temporal de una sola sesión; lo crónico pide práctica regular', 'Sí, porque el cansancio del día siguiente es un cambio duradero en el cuerpo', 'Un cansancio tras una sesión es temporal; la adaptación crónica pide semanas de práctica regular.'),
        ('abc', 'Alguien afirma: «Si mi pulso sube a 150 al correr, ya tengo una adaptación crónica». ¿Qué falla?', 'Confunde un cambio temporal durante el esfuerzo con un cambio duradero tras semanas', 'Nada, porque cualquier aumento del pulso durante el ejercicio ya es crónico', 'Que el pulso nunca sube con el ejercicio, sino que baja al correr', 'Subir durante la carrera es temporal; lo crónico se ve en el reposo tras semanas.'),
        ('abc', 'Dos personas hacen el mismo plan 8 semanas. A baja su pulso en reposo 6 latidos por minuto y B lo baja 3. ¿Qué conclusión es adecuada?', 'Cada persona se adapta a su ritmo y se compara solo con sus propias mediciones', 'A es mejor persona que B, y B debe esforzarse el doble hasta igualarla', 'B no tuvo adaptación alguna y por eso debe dejar el plan de entrenamiento', 'Las adaptaciones varían entre personas y no sirven para juzgarlas.'),
        ('=', 'Otra persona de ejemplo baja su pulso en reposo 9 latidos por minuto en 12 semanas, a ritmo parejo. ¿Cuántos latidos bajó cada 4 semanas?', '9/(12/4)', 'Doce semanas contienen tres bloques de 4 semanas, y 9 se reparte en tres.', ' latidos por minuto'),
        ('abc', 'Un plan quiere observar una adaptación crónica de resistencia. ¿Qué medición repetida tiene más sentido?', 'Cuántos minutos trota seguida cada dos semanas, en las mismas condiciones', 'El pulso máximo que se alcanza en una sola sesión muy exigente de trote', 'La cantidad de sudor que aparece en una sola sesión de trote con calor', 'Una medición repetida en las mismas condiciones muestra cambios duraderos de resistencia.'),
    ],
    ctx=('abc', 'Camilo entrena 10 semanas y registra: pulso en reposo 80 al inicio y 73 al final; pulso durante un trote suave de 10 minutos, 150 en la semana 1 y 141 en la semana 10. ¿Qué se interpreta?', 'Hay adaptaciones crónicas: bajó el pulso de reposo y el de la misma tarea', 'Solo hay respuestas agudas, porque el pulso sigue subiendo al trotar', 'No hay cambios, porque el pulso sigue subiendo durante cada trote', 'Ambos pulsos bajaron tras semanas de práctica, y eso es un cambio duradero.'),
    sc=[
        ("En Ciencias del ejercicio: ¿cuál es la diferencia entre una adaptación aguda y una crónica?", "La aguda es temporal y la crónica es duradera tras semanas de práctica", "El tiempo de aparición y duración las distingue."),
        ("¿Qué pasa con las adaptaciones crónicas si se deja de practicar mucho tiempo?", "Se pierden poco a poco", "Esa pérdida gradual se llama reversibilidad."),
        ("¿Se juzga a una persona por cuánto se adapta?", "No: cada persona se compara solo con sus propias mediciones", "Cada una se adapta a su ritmo."),
    ],
    op=("Clasifica estas observaciones de ejemplo como aguda o crónica y explica cada una en una frase: (1) el pulso sube a 140 durante un trote; (2) tras 6 semanas, la persona sostiene 5 minutos más de caminata rápida; (3) tras correr aparece sudoración; (4) tras 8 semanas, su pulso en reposo es más bajo. Agrega una frase sobre qué pasaría si dejara de practicar tres meses.",
        "(1) Aguda: ocurre durante el esfuerzo. (2) Crónica: aparece tras semanas. (3) Aguda: se detiene al descansar. (4) Crónica: se mide en reposo tras semanas. Si deja de practicar tres meses, parte de lo logrado se perdería (reversibilidad). Ante dolor o mareo, paro y aviso.",
        ["clasifica las cuatro con una razón", "usa tiempo de aparición y duración", "menciona la reversibilidad y la seguridad"],
        ["cuatro clasificaciones razonadas"],
        ["llamar crónico a todo lo que sube con el ejercicio", "no explicar por qué", "olvidar la reversibilidad"],
        "Pregunta: «¿se mantiene al descansar o desaparece?». Si dice «no sé», pídele que piense en cuánto dura."),
    reinforce="Escribe dos ejemplos de adaptaciones agudas y dos de adaptaciones crónicas, con una razón cada uno. No compares tus datos con los de otras personas.",
    extend="Explica por qué las adaptaciones crónicas necesitan práctica regular y recuperación, y no se logran con una sola sesión intensa.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 7 (plan de observación de ejemplo, inventado). Objetivo: observar si el entrenamiento regular produce adaptaciones crónicas en Elena, una persona ficticia. "
     "Plan: 3 sesiones por semana de trote o caminata suave de 30 minutos durante 6 semanas. Medición: cada lunes por la mañana, sentada y tras 5 minutos de reposo, con el mismo método (pulso de muñeca, 15 segundos por 4). "
     "Pulso de reposo por semana, en latidos por minuto: semana 1, 74; semana 2, 73; semana 3, 72; semana 4, 71; semana 5, 70; semana 6, 70.")
build(
    O2, 3, F,
    use="Aprenderé a planificar y registrar mediciones repetidas para observar adaptaciones crónicas, cuidando que las condiciones sean iguales y que la interpretación sea honesta.",
    prior=["Sé distinguir adaptaciones agudas y crónicas.", "Sé medir el pulso con el método de 15 segundos.", "Sé que cada persona se compara consigo misma."],
    explain=[
        "Para saber si el entrenamiento produce una adaptación crónica hay que medir más de una vez. La primera medición, antes de entrenar, es la línea de base: el punto de partida con el que se compara. Después se repite la misma medición cada cierto tiempo, por ejemplo cada semana, y se observa la tendencia, es decir, hacia dónde van los valores en conjunto.",
        "Las condiciones deben ser iguales en cada medición: mismo día y hora, misma postura, mismo tiempo de reposo previo y mismo método. Así las diferencias se deben al entrenamiento y no a haber corrido hace un rato, dormido mal o estar nervioso. Un cambio pequeño de un día, como 1 o 2 latidos, puede ser variación normal de la medición: se anota la condición y se mira la tendencia de varias semanas.",
        "Un plan de observación escrito dice qué se mide, cuándo, cómo, con qué condiciones y qué cuidados se tienen: calentamiento, agua, descanso. Si en alguna sesión aparecen dolor, mareo o falta de aire inusual, se detiene y se avisa a una persona adulta o a un profesional de la salud. Los datos son propios y privados.",
    ],
    vocab=[("línea de base", "primera medición, antes de entrenar, usada para comparar"), ("medición repetida", "la misma medición hecha varias veces"), ("tendencia", "dirección en que cambian los valores en conjunto"), ("condiciones iguales", "mismo momento, postura, reposo y método"), ("variación normal", "pequeño cambio de un día que no indica una adaptación")],
    worked=[
        ("Identificar la línea de base", "Un plan de ejemplo mide el pulso en reposo en las semanas 1, 2 y 3: 78, 77, 75. ¿Cuál es la línea de base y qué tendencia hay?", ["La línea de base es la primera medición: 78.", "Los valores bajan semana a semana: la tendencia es hacia abajo."], "Línea de base 78; tendencia a la baja"),
        ("Revisar las condiciones", "Una persona de ejemplo midió un lunes después de subir corriendo una escalera. ¿Sirve la medición?", ["No cumple el reposo previo de 5 minutos.", "Debe repetirse en condiciones iguales o anotarse como no comparable."], "No es comparable"),
    ],
    mistakes=[("Medir una vez antes y una vez después y concluir que el entrenamiento causó el cambio.", "Con dos puntos no se ve la tendencia ni se descartan otras causas.", "Mide varias veces, en las mismas condiciones."),
              ("Cambiar la hora, la postura y el método según el día.", "Las diferencias pueden venir de las condiciones y no del entrenamiento.", "Fija condiciones iguales y anota las excepciones.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es la línea de base?', 'La primera medición, antes de entrenar, con la que se compara después', 'La última medición del plan, la que se usa para cerrar la serie', 'La mejor medición de toda la serie, la que tiene menos latidos', 'La línea de base es el punto de partida para comparar.'),
        ('=', '{F} ¿Cuántas sesiones hay planificadas en las 6 semanas?', '3*6', 'Se multiplican las 3 sesiones semanales por las 6 semanas.', ' sesiones'),
        ('abc', '{F} ¿Cuál es la línea de base de Elena?', '74 latidos por minuto, de la semana 1', '70 latidos por minuto, de la semana 6', '72 latidos por minuto, de la semana 3', 'La primera medición del plan es la de la semana 1.'),
        ('=', '{F} ¿Cuántos latidos por minuto bajó su pulso de reposo entre la semana 1 y la semana 6?', '74-70', 'Se resta el valor de la semana 6 al de la semana 1.', ' latidos por minuto'),
        ('abc', '{F} ¿Qué describe mejor la tendencia de los seis valores?', 'Baja poco a poco y se estabiliza en las dos últimas semanas', 'Sube cada semana y termina por encima del valor inicial', 'Cambia sin ningún orden y no muestra una tendencia clara', 'Los valores bajan de 74 a 70 y se repiten en las semanas 5 y 6.'),
        ('abc', '¿Por qué se mide siempre el lunes por la mañana, sentada y tras 5 minutos de reposo?', 'Para que las condiciones sean iguales y la comparación sea válida', 'Para que el pulso salga siempre más bajo y se vea una mejora', 'Para que la medición sea más rápida y no se pierda tiempo', 'Condiciones iguales hacen que las diferencias vengan del entrenamiento.'),
        ('abc', 'Un lunes Elena mide su pulso justo después de correr para alcanzar un bus. ¿Qué pasa con esa comparación?', 'No es comparable, porque no cumple las condiciones de reposo del plan', 'Es más confiable, porque con el pulso más alto es más fácil de contar', 'Es igual de válida, porque se hizo en lunes y con el método de 15 segundos', 'Sin el reposo previo se mediría una respuesta aguda, no el reposo.'),
        ('=', '{F} Un lunes Elena cuenta 19 latidos en 15 segundos. ¿Cuántos latidos por minuto son?', '19*4', 'Se multiplica por 4 para pasar de 15 segundos a un minuto.', ' latidos por minuto'),
        ('ab', 'Una semana el pulso de reposo sube 2 latidos respecto de la anterior, tras una mala noche. ¿Qué conviene?', 'Anotar la condición y mirar la tendencia de varias semanas', 'Concluir de inmediato que el entrenamiento dejó de funcionar', 'Un cambio pequeño de un día puede ser variación normal; la tendencia da más información.'),
        ('abc', 'Alguien dice: «Con una medición antes y otra después ya sé que el entrenamiento causó el cambio». ¿Qué falta?', 'Más mediciones en iguales condiciones y descartar otras causas', 'Nada: dos mediciones siempre bastan para asegurar la causa', 'Medir con otra persona al lado para comparar sus cuerpos', 'Con más mediciones se ve la tendencia y se descartan otras causas.'),
        ('abc', 'El pulso de reposo se mantiene en 70 en las semanas 5 y 6. ¿Qué es lo más razonable?', 'Seguir midiendo, porque puede estabilizarse y eso también es información', 'Concluir que el entrenamiento no sirve y suspender todas las mediciones', 'Duplicar de inmediato la exigencia del plan para que el pulso siga bajando', 'Un valor estable es parte de la tendencia; no justifica abandonar ni exigir más.'),
        ('=', 'Un pulso de reposo anotado fue de 72 latidos por minuto. ¿Cuántos latidos se contaron en 15 segundos?', '72/4', 'Se divide entre 4 porque 15 segundos son un cuarto de minuto.', ' latidos'),
        ('abc', '{F} Elena cambia a la vez la duración de las sesiones al doble y las horas de sueño. ¿Qué problema tiene para interpretar?', 'Cambió varias condiciones a la vez y no sabrá cuál explica la adaptación', 'Ninguno, porque más cambios aseguran más adaptación en menos tiempo', 'Que el pulso de reposo ya no se puede medir con el método de 15 segundos', 'Con varios cambios juntos no se puede atribuir el efecto a uno solo.'),
    ],
    ctx=('abc', 'Tomás mide su pulso de reposo cada lunes en las mismas condiciones: 78, 77, 79, 76, 75, 74 latidos por minuto. En la semana 3 durmió poco. ¿Cómo se interpreta?', 'Hay tendencia a bajar; el 79 puede deberse al poco sueño y se anota como condición', 'El 79 prueba que el entrenamiento falló y debe abandonarse el plan', 'No se puede interpretar nada, porque los números cambian de una semana a otra', 'Con seis mediciones se ve la tendencia, y el valor aislado se explica con su condición.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué es la línea de base?", "La primera medición, antes de entrenar", "Sirve para comparar los cambios posteriores."),
        ("¿Por qué las condiciones de medición deben ser iguales?", "Para que la diferencia se deba al entrenamiento y no a otra causa", "Si las condiciones cambian, se confunde la interpretación del resultado."),
        ("¿Qué haces si aparece mareo o dolor durante una sesión del plan?", "Detenerte y avisar a una persona adulta o a un profesional de la salud", "La seguridad va antes que el plan."),
    ],
    op=("Escribe un plan de observación de 4 semanas para una persona ficticia que hará caminata rápida de 30 minutos tres veces por semana. Indica qué medirás (el pulso de reposo, por ejemplo), cuándo, cómo, qué condiciones mantendrás iguales y qué cuidados tendrás. Con esta tabla de ejemplo (semana 1, 80; semana 2, 79; semana 3, 79; semana 4, 77) identifica la línea de base y la tendencia.",
        "Mediré el pulso de reposo cada lunes por la mañana, sentada, tras 5 minutos de reposo, con dos dedos en la muñeca y 15 segundos por 4. Cuidados: calentar, llevar agua y parar ante mareo o dolor. Línea de base: 80. Tendencia: baja leve, de 80 a 77.",
        ["qué, cuándo y cómo medir", "condiciones iguales y cuidados", "línea de base y tendencia correctas"],
        ["plan escrito y lectura de la tabla"],
        ["medir solo una vez", "cambiar las condiciones en cada medición", "olvidar la seguridad"],
        "Pregunta: «¿qué mantienes igual en cada medición y por qué?». Si no lo sabe, pídele que mire su plan."),
    reinforce="Anota tu pulso de reposo, sentado y tras 5 minutos de calma, un mismo día de tres semanas distintas y observa la tendencia sin compararte con nadie.",
    extend="Explica por qué una variación pequeña de un solo día no basta para concluir que hubo una adaptación.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 8 (registro de ejemplo, inventado). Tarea fija: trote suave de 10 minutos. En las tres mediciones el pulso máximo fue de 150 latidos por minuto y se midió el pulso 2 minutos después de detenerse. "
     "Semana 1: 120. Semana 4: 112. Semana 8: 104. Se llama recuperación a los latidos por minuto que baja el pulso en esos 2 minutos: pulso máximo menos pulso a los 2 minutos.")
build(
    O2, 4, F,
    use="Aprenderé a registrar la recuperación del pulso en una tarea fija, a interpretar cambios entre semanas y a decidir con cuidado qué se puede afirmar y qué no.",
    prior=["Sé qué es una adaptación crónica.", "Sé fijar condiciones iguales.", "Sé calcular diferencias."],
    explain=[
        "La recuperación del pulso es cuánto baja la frecuencia cardíaca en un tiempo fijo después de detener el ejercicio, por ejemplo 2 minutos. Se calcula restando: pulso máximo menos pulso a los 2 minutos. Si con la misma tarea y el mismo pulso máximo la persona baja más latidos que antes, su recuperación fue mayor.",
        "Una recuperación que mejora con las semanas es compatible con una adaptación crónica, pero no la prueba por sí sola: el sueño, el calor, el nerviosismo y la hidratación pueden alterar la medición. Por eso se registran la tarea, el pulso máximo, el tiempo fijo y las condiciones del día. Si una medición sale distinta, se anota la condición y se repite otro día.",
        "El registro sirve para comparar a la persona con ella misma, nunca con otras. Quien tenga una recuperación menor que otra persona no es peor: cada cuerpo parte de un punto distinto. Si durante la tarea aparecen mareo, dolor o falta de aire inusual, se detiene y se avisa a una persona adulta o a un profesional de la salud.",
    ],
    vocab=[("recuperación del pulso", "latidos por minuto que baja el pulso en un tiempo fijo tras detenerse"), ("tarea fija", "ejercicio que se repite igual en cada medición"), ("pulso máximo", "valor más alto alcanzado en la tarea"), ("registro", "anotación ordenada de las mediciones"), ("condición del día", "factor como sueño o calor que se anota")],
    worked=[
        ("Calcular una recuperación", "En una tarea de ejemplo el pulso máximo fue 140 y a los 2 minutos fue 110. ¿Cuál fue la recuperación?", ["Se resta el pulso a los 2 minutos al pulso máximo.", "140 − 110 = 30."], "30 latidos por minuto"),
        ("Comparar dos semanas", "Con el mismo pulso máximo, la recuperación fue 30 en la semana 1 y 36 en la semana 6. ¿Qué se dice con cuidado?", ["La recuperación aumentó 6 latidos con una exigencia similar.", "Es compatible con una adaptación crónica, pero se revisan otras condiciones."], "Es compatible con una adaptación; se revisan otras causas"),
    ],
    mistakes=[("Registrar solo el pulso final sin el máximo ni el tiempo fijo.", "Sin esos datos no se puede calcular la recuperación ni comparar.", "Anota pulso máximo, tiempo fijo y pulso final."),
              ("Afirmar que la mejora «prueba» que la persona rinde mejor que otras.", "Las mediciones solo comparan a la persona consigo misma y tienen otras causas posibles.", "Interpreta con cuidado y solo contra su propio registro.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es la recuperación del pulso?', 'Los latidos por minuto que baja el pulso en un tiempo fijo tras detenerse', 'El pulso máximo que se alcanza al correr durante una sesión completa', 'La cantidad de sesiones hechas en la semana respecto de las planificadas', 'La recuperación mide cuánto baja el pulso tras parar, en un tiempo fijo.'),
        ('=', '{F} ¿Cuántos latidos por minuto bajó el pulso en la semana 1?', '150-120', 'Se resta el pulso a los 2 minutos al pulso máximo.', ' latidos por minuto'),
        ('=', '{F} ¿Cuántos latidos por minuto bajó el pulso en la semana 4?', '150-112', 'Se resta el pulso a los 2 minutos al pulso máximo.', ' latidos por minuto'),
        ('=', '{F} ¿Cuántos latidos por minuto bajó el pulso en la semana 8?', '150-104', 'Se resta el pulso a los 2 minutos al pulso máximo.', ' latidos por minuto'),
        ('abc', '{F} ¿Qué cambió entre la semana 1 y la semana 8 con la misma tarea?', 'El pulso a los 2 minutos fue más bajo, o sea, la recuperación fue mayor', 'El pulso máximo subió de 150 a 160 latidos por minuto en la semana 8', 'La recuperación fue menor en cada medición, semana tras semana', 'Con el mismo máximo, el pulso a los 2 minutos bajó de 120 a 104.'),
        ('abc', '{F} ¿Por qué ayuda que el pulso máximo sea igual (150) en las tres mediciones?', 'Porque con una exigencia similar se puede comparar la recuperación', 'Porque demuestra que no hubo ninguna adaptación a lo largo de las semanas', 'Porque garantiza que no hubo cansancio ni calor en ninguna medición', 'Con igual máximo, las diferencias de recuperación se comparan con más sentido.'),
        ('=', '{F} ¿Cuántos latidos más bajó el pulso en la semana 8 que en la semana 1?', '(150-104)-(150-120)', 'Se calculan ambas recuperaciones y se restan.', ' latidos por minuto'),
        ('abc', '{F} Con estos datos, ¿qué se puede afirmar con cuidado?', 'Mejoró la recuperación: es compatible con una adaptación, no una prueba', 'La recuperación prueba que la persona rinde más que sus compañeros de curso', 'La recuperación mejoró solo porque aumentó la exigencia de la tarea', 'La mejora es compatible con adaptación, pero no la prueba ni sirve para comparar personas.'),
        ('ab', 'En una nueva medición el pulso a los 2 minutos fue 130 con el mismo máximo de 150. ¿Qué conviene?', 'Anotar la condición del día, como poco sueño o calor, y repetir', 'Concluir que la adaptación se perdió por completo de un día para otro', 'Una medición aislada distinta se explica anotando condiciones y repitiendo.'),
        ('abc', '¿Qué factor externo puede alterar la recuperación y conviene anotar?', 'El calor del día y las horas de sueño de la noche anterior', 'Cuántas personas observan la sesión desde la tribuna del patio', 'El color de la ropa deportiva y del patio donde se hace la medición', 'El calor y el sueño pueden cambiar el pulso; los otros factores no tienen relación.'),
        ('abc', 'Una compañera dice: «Mi recuperación es 20 y la tuya es 46, soy peor». ¿Qué corresponde?', 'Compararse solo con las propias mediciones de otras semanas', 'Aceptar que 20 es peor y esforzarse más que todas las demás personas', 'Subir el esfuerzo hasta igualar el 46, aunque sienta mareo o dolor', 'Los registros son propios; compararse con otras personas no es válido ni seguro.'),
        ('=', '{F} Entre la semana 4 y la semana 8, ¿cuántos latidos mejoró la recuperación por semana, en promedio?', '((150-104)-(150-112))/4', 'Se calcula cuánto aumentó la recuperación entre ambas semanas y se divide entre las 4 semanas.', ' latidos por semana'),
        ('abc', 'Un registro dice solo «semana 1: 120; semana 4: 112; semana 8: 104». ¿Qué problema tiene?', 'No permite saber la recuperación ni comparar: faltan el máximo y el tiempo fijo', 'Ninguno, porque con el pulso final basta para calcular la recuperación', 'Que los números son demasiado bajos para ser mediciones reales de pulso', 'Sin el máximo y el tiempo fijo no se puede calcular la recuperación.'),
    ],
    ctx=('abc', 'Lucía mide su recuperación a los 2 minutos con el mismo trote suave: semana 1, 28; semana 5, 35; semana 9, 33, en una semana de calor fuerte y poco sueño. ¿Qué interpretación es más cuidadosa?', 'Hay mejora general; el 33 pudo verse afectado por el calor y el sueño', 'La mejora terminó en la semana 9, por lo que conviene abandonar el plan', 'Los datos no sirven para nada, porque los valores no son siempre iguales', 'La tendencia mejora y un valor menor se explica con su condición, sin descartar todo.'),
    sc=[
        ("En Ciencias del ejercicio: ¿cómo se calcula la recuperación del pulso?", "Pulso máximo menos pulso a los 2 minutos", "Muestra cuánto bajó en un tiempo fijo."),
        ("¿Por qué se anotan condiciones como el calor o el sueño?", "Porque pueden alterar la medición", "Así se interpreta con más cuidado."),
        ("¿Con quién se compara tu recuperación?", "Contigo en otras mediciones", "Cada persona parte de un punto distinto."),
    ],
    op=("Con estos datos de ejemplo de una persona ficticia, misma tarea: semana 1, máximo 148 y 2 minutos después 126; semana 5, máximo 148 y 2 minutos después 118; semana 9, máximo 148 y 2 minutos después 112. Calcula la recuperación de cada semana, interpreta con cuidado qué se puede afirmar y escribe dos condiciones del día que anotarías.",
        "Recuperaciones: 22, 30 y 36. Mejoró 14 latidos en 8 semanas con la misma tarea: es compatible con una adaptación crónica, pero no la prueba. Condiciones: calor y horas de sueño. Si hay mareo o dolor, paro y aviso.",
        ["calcula las tres recuperaciones", "interpreta con cuidado sin exagerar", "nombra dos condiciones que anotaría"],
        ["tabla con tres recuperaciones e interpretación"],
        ["afirmar que la mejora prueba que rinde más que otras personas", "olvidar el máximo y el tiempo fijo", "no anotar condiciones"],
        "Pregunta: «¿qué otra cosa podría explicar el cambio?». Si responde «nada», pídele pensar en calor, sueño o nervios."),
    reinforce="Con un trote o caminata suave de 10 minutos, si tu docente lo organiza, mide tu pulso máximo y a los 2 minutos de parar, y anota las condiciones del día. Detente ante mareo o dolor.",
    extend="Explica por qué una mejora en la recuperación del pulso es compatible con una adaptación crónica pero no la prueba por sí sola.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 9 (caso de ejemplo, inventado). Rodrigo hace una prueba de 1 kilómetro de trote a ritmo constante en una pista despejada. Tiempo inicial: 390 segundos. Tras 8 semanas de práctica regular: 350 segundos. "
     "Después de 3 semanas sin practicar: 372 segundos. En la semana 12 de un nuevo plan, anota que el cansancio no se le va, duerme mal y está de peor ánimo.")
build(
    O2, 5, F,
    use="Aprenderé a evaluar cómo las adaptaciones agudas y crónicas se relacionan con el rendimiento, a interpretar mejoras y pérdidas y a ajustar un plan reconociendo señales de cansancio excesivo.",
    prior=["Sé distinguir adaptaciones agudas y crónicas.", "Sé registrar mediciones repetidas.", "Sé que cada persona se compara consigo misma."],
    explain=[
        "El rendimiento es el resultado que una persona obtiene en una tarea medida, por ejemplo el tiempo que tarda en trotar 1 kilómetro a ritmo constante. Las adaptaciones crónicas, como más resistencia, pueden mejorar el rendimiento: con el mismo trabajo se rinde más. Las respuestas agudas, en cambio, ocurren durante la prueba y no son por sí solas una mejora.",
        "Evaluar es comparar con la línea de base y con las condiciones de cada prueba: calcular el cambio (por ejemplo, 40 segundos menos) y revisar qué pasó entre pruebas. Si se interrumpe la práctica, parte de la mejora se pierde (reversibilidad). Las mejoras no son lineales ni iguales en todas las personas, y el descanso es parte del entrenamiento porque en la recuperación el cuerpo se adapta.",
        "Si se acumula cansancio que no se va, el sueño empeora y el ánimo baja mientras el rendimiento cae, es una señal de cansancio excesivo: se reduce la carga, se descansa y se avisa a una persona adulta o a un profesional de la salud. No se corrige con más entrenamiento. Todos estos datos son propios y no sirven para comparar ni juzgar a otras personas.",
    ],
    vocab=[("rendimiento", "resultado que se obtiene en una tarea medida"), ("prueba", "tarea repetida que mide el rendimiento"), ("mejora", "cambio del resultado hacia algo mejor"), ("cansancio excesivo", "cansancio que no se va, con mal sueño o ánimo bajo y peor resultado"), ("ajuste", "cambio de una condición del plan según lo que muestran los datos")],
    worked=[
        ("Evaluar un cambio", "En una prueba de ejemplo de 1 kilómetro, una persona baja de 420 a 395 segundos. ¿Mejoró y cuánto?", ["En esta prueba menos tiempo es mejor rendimiento.", "420 − 395 = 25 segundos menos."], "Sí: 25 segundos menos"),
        ("Ajustar ante cansancio", "Una persona de ejemplo anota semanas de cansancio que no se va y peor sueño, con tiempos peores. ¿Qué ajuste corresponde?", ["Son señales de cansancio excesivo.", "Reduce la carga, descansa y avisa a una persona adulta o a un profesional de la salud."], "Reducir la carga, descansar y avisar"),
    ],
    mistakes=[("Creer que si el rendimiento baja hay que entrenar más.", "Si hay cansancio excesivo, más carga empeora el estado.", "Descansa, reduce la carga y avisa a una persona adulta o a un profesional."),
              ("Interpretar la mejora de una persona como prueba de que otra lo hizo mal.", "Cada persona parte de un tiempo y condiciones distintos.", "Interpreta cada registro solo contra el propio.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es el rendimiento en una prueba?', 'El resultado de una tarea medida, como el tiempo en 1 kilómetro', 'El esfuerzo que se siente al hacer la tarea, en una escala de 1 a 10', 'El número de personas que participan en la prueba al mismo tiempo', 'El rendimiento es el resultado medido en la tarea.'),
        ('=', '{F} ¿Cuántos segundos mejoró Rodrigo en las 8 semanas?', '390-350', 'Se resta el tiempo final al tiempo inicial.', ' segundos'),
        ('abc', '{F} En esta prueba de 1 kilómetro, ¿qué significa un tiempo menor?', 'Mejor rendimiento, porque recorre la misma distancia en menos segundos', 'Peor rendimiento, porque se esforzó menos que en la prueba anterior', 'No cambia el rendimiento, porque la distancia recorrida es la misma', 'Con la misma distancia, menos segundos es un mejor resultado.'),
        ('=', '{F} Tras 3 semanas sin practicar, ¿cuántos segundos perdió respecto de los 350 segundos?', '372-350', 'Se resta el mejor tiempo al tiempo después de la pausa.', ' segundos'),
        ('abc', '{F} ¿Qué muestra el paso de 350 a 372 segundos?', 'Reversibilidad: parte de la mejora se pierde al dejar de practicar', 'Una mejora crónica, porque el tiempo cambió respecto de la prueba', 'Una respuesta aguda, porque el pulso subió durante la prueba final', 'Una pausa de práctica hizo perder parte de lo logrado.'),
        ('=', '{F} ¿Qué porcentaje de la mejora de 40 segundos perdió con la pausa?', '(372-350)*100/(390-350)', 'Se divide la pérdida de 22 segundos entre la mejora de 40 y se pasa a porcentaje.', ' %'),
        ('abc', '{F} Rodrigo reanuda con sesiones suaves y regulares. ¿Qué es razonable esperar?', 'Recuperar poco a poco parte de lo perdido, sin garantía de tiempos exactos', 'Volver a 350 segundos en una sola semana de sesiones suaves y regulares', 'Que no cambie nada porque ya perdió todo lo que había mejorado antes', 'Las adaptaciones se recuperan gradualmente y varían entre personas.'),
        ('=', '{F} Si en la reanudación mejora 12 segundos desde los 372, ¿cuántos segundos le faltan para igualar su mejor tiempo?', '372-12-350', 'Se resta la mejora al tiempo de 372 y luego se compara con 350.', ' segundos'),
        ('ab', '{F} En la semana 12, ¿qué decisión corresponde ante el cansancio que no se va, el mal sueño y el peor ánimo?', 'Reducir la carga, descansar y avisar a una persona adulta o a un profesional', 'Aumentar la carga para superar el mal momento y no perder lo logrado', 'Esas señales indican cansancio excesivo: se descansa y se pide ayuda, no se aumenta la carga.'),
        ('abc', 'Alguien concluye: «El descanso es tiempo perdido; solo cuenta cuando entreno». ¿Qué falla?', 'La recuperación permite adaptarse y evita el cansancio excesivo', 'Nada: solo la práctica produce adaptaciones, y el descanso no influye', 'Que el descanso solo sirve a quien aún no practicó nada durante la semana', 'La adaptación ocurre durante la recuperación, por eso el descanso es parte del entrenamiento.'),
        ('abc', 'Rodrigo mejoró 40 segundos en 8 semanas. Otro estudiante mejoró 25 segundos con otro plan. ¿Qué se puede decir?', 'Que cada persona parte de un tiempo y de condiciones distintos', 'Que el segundo estudiante hizo mal el plan y debe repetirlo desde cero', 'Que Rodrigo es mejor deportista que el otro estudiante porque mejoró más', 'Los cambios se interpretan contra el propio punto de partida, no entre personas.'),
        ('=', '{F} Tras reanudar, Rodrigo baja a 361 segundos. ¿Qué porcentaje de los 22 segundos que había perdido recuperó?', '(372-361)*100/22', 'Se calcula cuántos segundos recuperó y se divide entre los 22 perdidos.', ' %'),
        ('abc', 'Un informe sobre Rodrigo dice «mejoró por el entrenamiento» y no explica cómo midió. ¿Qué datos hacen falta para evaluarlo?', 'Las condiciones de cada prueba y varias mediciones repetidas', 'Solo el tiempo final, porque el inicial no cambia la conclusión', 'La opinión de otras personas sobre cómo se ve Rodrigo al correr', 'Para evaluar hacen falta mediciones repetidas con condiciones claras.'),
    ],
    ctx=('abc', 'Ana, persona ficticia, mejoró su tiempo en dos pruebas seguidas, pero en la tercera empeoró y anotó cansancio y sueño irregular durante dos semanas. ¿Qué decisión de ajuste es más razonable?', 'Reducir la carga unos días, priorizar el descanso y consultar si persiste', 'Entrenar el doble los días siguientes para recuperar el tiempo perdido', 'Ignorar la tercera prueba y seguir con el plan exactamente igual que antes', 'Con señales de cansancio excesivo se baja la carga y se pide ayuda si continúa.'),
    sc=[
        ("En Ciencias del ejercicio: ¿cómo se relaciona una adaptación crónica con el rendimiento?", "Puede mejorarlo: con el mismo trabajo se rinde más", "Es el efecto de semanas de práctica regular."),
        ("¿Qué se hace ante cansancio que no se va, mal sueño y ánimo bajo?", "Reducir la carga, descansar y avisar a una persona adulta o a un profesional de la salud", "Estas señales indican un cansancio excesivo que requiere descanso."),
        ("¿Se usa el rendimiento para juzgar a otras personas?", "No: se compara cada persona solo con su propio registro", "Los puntos de partida son distintos."),
    ],
    op=("Con estos datos de ejemplo de una persona ficticia en una prueba de 1 kilómetro: inicial 410 segundos; tras 6 semanas, 385; tras 2 semanas de pausa, 398. Calcula la mejora y la pérdida, di qué principio se muestra y propone un ajuste de una sola condición para reanudar con seguridad. Incluye qué señales te harían detener y avisar.",
        "Mejora: 25 segundos. Pérdida: 13 segundos. Muestra reversibilidad. Ajuste: reanudar con sesiones suaves y regulares, una condición cambiada a la vez. Señales: dolor, mareo, cansancio que no se va o mal sueño; paro y aviso a una persona adulta o a un profesional.",
        ["calcula mejora y pérdida", "nombra la reversibilidad", "propone un ajuste y señales de detención"],
        ["cálculos, principio y ajuste escritos"],
        ["confundir menos tiempo con peor rendimiento", "aumentar la carga ante el cansancio", "juzgar a otras personas"],
        "Pregunta: «¿qué pasó con el tiempo cuando dejó de practicar?». Si no lo lee en los datos, pídele que calcule."),
    reinforce="Escribe en papel un ejemplo de una mejora, una pérdida por pausa y un ajuste razonable. Usa datos inventados y no compares personas.",
    extend="Explica por qué el descanso es parte del entrenamiento y cómo reconocer cuándo el cansancio es excesivo.",
)
