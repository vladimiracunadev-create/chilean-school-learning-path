"""Creación y composición musical 3.º y 4.º medio HC: OAC-02 (crear obras de distintos estilos y formatos con elementos del lenguaje, procedimientos, recursos de producción y referentes). Obras y referentes inventados."""
from __future__ import annotations

from hc_ccmu_common import CLAVE, build

O2 = "AR-CCMU-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (tres referentes de ejemplo, inventados para este cuaderno; no son obras reales). "
     "Pieza A, referente nacional de ejemplo: dúo de voz y guitarra; 90 pulsos por minuto; compás de 3 pulsos; 4 estrofas de 8 compases cada una; la guitarra rasguea el patrón «X . X» en cada compás; la melodía avanza sobre todo por notas vecinas. "
     "Pieza B, referente internacional de ejemplo: pista electrónica sin voz; 128 pulsos por minuto; compás de 4 pulsos; bombo «X X X X» en cada compás; un motivo de sintetizador de 2 compases que se repite sin cambios; cada 8 compases entra una capa nueva. "
     "Pieza C, referente escolar de ejemplo: ensamble de 6 personas con palmas, chasquidos y objetos de la sala; sin notas definidas; 100 pulsos por minuto; compás de 4 pulsos; patrón «X . X X»; dos grupos de 3 personas se turnan, uno propone y el otro responde. "
     "Clave: X es un golpe, «.» es un silencio y cada casilla es un pulso.")
build(
    O2, 1, F,
    use="Aprenderé a investigar referentes de distintos estilos y formatos describiendo sus rasgos con los elementos del lenguaje musical, para tener una base propia antes de crear una obra.",
    prior=["Reconozco ritmo, melodía, timbre, textura y forma.", "Sé leer una cuadrícula de pulsos.", "Sé que investigar es observar y anotar con evidencia."],
    explain=[
        "Un estilo es un conjunto de rasgos del lenguaje musical (ritmo, melodía, armonía, timbre, textura, forma) que se repiten en muchas obras. Un formato es la combinación de voces, instrumentos o tecnologías que ejecutan una obra, como un dúo de voz y guitarra, un ensamble de percusión o una pista electrónica. Un mismo estilo puede darse en varios formatos, y un formato puede servir a varios estilos.",
        "Un referente es una obra o creadora que se estudia para aprender de sus decisiones. Investigar un referente significa escuchar, anotar rasgos que se puedan comprobar (tempo, compás, formato, forma, patrón rítmico) y, si se consulta una fuente escrita, anotar quién la escribió y cuándo. Hay referentes nacionales, de Chile, y referentes internacionales, de otros países; aquí se usan referentes de ejemplo inventados porque las obras reales las aporta tu docente.",
        "Inspirarse no es copiar. Inspirarse es tomar una idea general, como la forma de estrofas o un patrón rítmico repetido, y resolverla con material propio. Copiar es reproducir la melodía, el ritmo característico, la letra o la grabación de otra persona. Este cuaderno no reproduce obras con derechos: toda obra descrita es de ejemplo y se trabaja con lápiz y papel.",
    ],
    vocab=[("estilo", "conjunto de rasgos del lenguaje musical que se repiten en muchas obras"), ("formato", "combinación de voces, instrumentos o tecnologías que ejecutan una obra"), ("referente", "obra o creadora que se estudia para aprender de sus decisiones"),
           ("forma", "organización de una obra en secciones, como estrofas"), ("compás", "grupo de pulsos entre dos barras"), ("inspirarse", "tomar una idea general y resolverla con material propio")],
    worked=[
        ("Identificar un formato", "Un grupo de ejemplo está formado por dos flautas dulces y un tambor. ¿Qué formato tiene?",
         ["Se cuentan los medios: dos flautas dulces (instrumentos melódicos) y un tambor (percusión).", "Como son tres intérpretes de instrumentos, es un ensamble instrumental de tres integrantes."],
         "Ensamble instrumental de tres integrantes"),
        ("Describir rasgos", "Pieza D de ejemplo: coro de 8 voces sin instrumentos, 60 pulsos por minuto, compás de 4 pulsos, tres estrofas con melodía de notas largas. Describe sus rasgos.",
         ["Formato: coro de 8 voces sin instrumentos. Tempo: 60 pulsos por minuto, es decir, lento.", "Compás: 4 pulsos. Forma: tres estrofas. Melodía: notas largas."],
         "Coro a voces, lento, compás de 4 pulsos, tres estrofas, notas largas"),
    ],
    mistakes=[("Decir que una pieza es de cierto estilo por un solo rasgo.", "Un rasgo aislado aparece en muchos estilos.", "Anota varios rasgos que se repiten antes de nombrar el estilo."),
              ("Creer que inspirarse es copiar un poco.", "Se confunde una idea general con la expresión concreta de otra persona.", "Toma la idea general y resuélvela con melodía, ritmo y texto propios.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un formato?', 'La combinación de voces, instrumentos o tecnologías que ejecutan una obra', 'La duración total de una obra expresada en segundos, según su tempo y su compás', 'El texto con que se canta una canción, es decir, la letra de cada estrofa', 'El formato describe con qué medios suena una obra, por ejemplo un dúo o una pista electrónica.'),
        ('abc', '{F} ¿Qué formato tiene la pieza B?', 'Una pista electrónica sin voz', 'Un dúo de voz y guitarra', 'Un ensamble de percusión corporal y objetos', 'La ficha describe a la pieza B como pista electrónica sin voz.'),
        ('abc', '{F} ¿Qué pieza no tiene notas definidas?', 'La pieza C, porque usa palmas, chasquidos y objetos', 'La pieza A, porque usa una guitarra que se puede reemplazar por objetos', 'La pieza B, porque usa un sintetizador y un bombo que suenan en cada pulso', 'Solo la pieza C trabaja con sonidos de palmas, chasquidos y objetos, sin notas definidas.'),
        ('abc', '{F} ¿Qué rasgo del ritmo tiene la pieza B?', 'Un bombo que suena en los cuatro pulsos de cada compás', 'Un rasgueo en el primer y el tercer pulso de un compás de 3', 'Un patrón que deja un silencio en el segundo pulso', 'La ficha indica el bombo «X X X X» en cada compás de 4 pulsos.'),
        ('=', '{F} Si la pista B dura 16 compases de 4 pulsos, ¿cuántos segundos dura a 128 pulsos por minuto?', '16*4*60//128', 'Se multiplican los compases por los pulsos de cada compás y por 60, y se divide por los pulsos por minuto.', ' s'),
        ('abc', '{F} ¿Qué forma tiene la pieza A?', 'Cuatro estrofas de ocho compases', 'Un motivo de dos compases que se repite sin cambios', 'Dos grupos que se turnan en preguntas y respuestas', 'La ficha dice que la pieza A tiene 4 estrofas de 8 compases.'),
        ('=', '{F} ¿Cuántos segundos dura la pieza A completa? Son 4 estrofas de 8 compases, cada compás de 3 pulsos, a 90 pulsos por minuto.', '4*8*3*60//90', 'Primero se cuentan los pulsos totales y luego se pasan a segundos con los pulsos por minuto.', ' s'),
        ('abc', '{F} Un grupo quiere componer una pieza que use solo objetos de la sala. ¿Cuál de las piezas le sirve de referente por su formato?', 'La pieza C, porque se hace con palmas, chasquidos y objetos', 'La pieza A, porque es nacional', 'La pieza B, porque tiene el tempo más rápido', 'El formato que usa objetos de la sala es el de la pieza C.'),
        ('Escribe el formato, el tempo y el compás de la pieza A de la {F}', 'Dúo de voz y guitarra; 90 pulsos por minuto; compás de 3 pulsos', 'Son tres datos que la ficha entrega de la pieza A.'),
        ('abc', '{F} ¿Qué rasgos comparten las piezas B y C, y no la pieza A?', 'El compás de 4 pulsos y la ausencia de melodía cantada', 'La voz cantada y la guitarra que rasguea el patrón en cada compás', 'El compás de 3 pulsos y la forma en estrofas de ocho compases', 'A tiene compás de 3 pulsos y voz; B y C tienen compás de 4 y no tienen melodía cantada.'),
        ('abc', 'Para describir los rasgos de un referente que investigas, ¿qué hace una fuente más confiable?', 'Escuchar la obra y anotar rasgos comprobables, y contrastar con una fuente que indique autoría y fecha', 'Usar el primer comentario que aparezca en una búsqueda, aunque no indique quién lo escribió', 'Anotar solo lo que le gusta a la mayoría del curso, porque así se evitan desacuerdos', 'Una fuente confiable indica quién la escribió y cuándo, y se contrasta con lo que se escucha.'),
        ('abc', '{F} Una estudiante quiere una pieza «entre A y B». ¿Qué decisión toma rasgos de ambas sin copiar?', 'Escribir estrofas con melodía y texto propios sobre una base repetida de 4 pulsos', 'Copiar la melodía de la pieza A y ponerle el bombo de la pieza B', 'Usar exactamente el motivo del sintetizador de la pieza B', 'Toma la forma de A y la base de B, pero con material propio; las otras opciones copian.'),
        ('abc', 'Escuchas una canción real y quieres inspirarte en ella. ¿Qué está permitido y qué no?', 'Tomar la idea general, como una forma de estrofas, y no reproducir su melodía ni su letra', 'Copiar su melodía completa si se cambia el título de la obra y se dice que es una inspiración', 'Copiar su letra palabra por palabra si se canta más lento que en la versión original', 'Las ideas generales pueden inspirar; la melodía y la letra concretas son expresión de otra persona.'),
    ],
    ctx=('=', 'Para investigar referentes, un grupo escucha 3 piezas de 2 minutos cada una y dedica 1 minuto a anotar rasgos después de cada pieza. ¿Cuántos minutos necesita en total?', '3*(2+1)', 'Cada pieza ocupa 2 minutos de escucha más 1 minuto de notas, y son tres piezas.', ' minutos'),
    sc=[
        ("En Composición musical: ¿qué es un estilo?", "Un conjunto de rasgos del lenguaje musical que se repiten en muchas obras", "Un estilo se reconoce por varios rasgos que se repiten."),
        ('abc', 'Un dúo de voz y guitarra es un ejemplo de:', 'Formato', 'Compás', 'Forma', 'Un dúo es una combinación de medios, o sea, un formato.'),
        ("¿Qué diferencia hay entre inspirarse y copiar?", "Inspirarse toma una idea general y la resuelve con material propio; copiar reproduce la expresión de otra persona", "Solo la segunda reproduce melodía, ritmo característico, letra o grabación."),
    ],
    op=("Con la {F}, elige un referente y escribe una ficha con su formato, tempo, compás y forma. Luego propón, en dos líneas, una idea general que tomarías para tu pieza y lo que harías con material propio.",
        "Referente: pieza C. Formato: ensamble de 6 personas con palmas, chasquidos y objetos; 100 pulsos por minuto; compás de 4; dos grupos que se turnan. Tomo la idea de proponer y responder, pero con un patrón rítmico mío y objetos que yo elija.",
        ["la ficha nombra formato, tempo, compás y forma", "toma una idea general y no una expresión concreta", "propone material propio"],
        ["hoja con la ficha del referente y las dos líneas de propuesta"],
        ["nombrar el estilo sin rasgos", "proponer copiar una melodía", "no indicar qué sería propio"],
        "Pregunta: «¿qué tomaste del referente y qué hiciste tú?». Si no distingue ambas cosas, pídele que separe la idea de su resolución."),
    reinforce="Escribe la ficha de una canción que conozcas con formato, tempo aproximado, forma y dos rasgos de ritmo, sin copiar su letra.",
    extend="Explica con un ejemplo inventado cómo un mismo estilo puede darse en dos formatos distintos.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (recursos de un grupo de 4 estudiantes en una sala de un liceo ficticio). "
     "Voz: cuatro voces (dos graves y dos agudas), habladas o cantadas. "
     "Objetos sonoros: una caja de cartón (golpe grave, seco y corto); una botella plástica cerrada con arroz adentro (agitada suena como lluvia continua); reglas de plástico apoyadas en el borde de una mesa (golpe agudo y corto). "
     "Instrumentos: un metalófono (barras de metal; sonido brillante que se apaga lento); una flauta dulce (sonido sostenido); una guitarra. "
     "Tecnología: un teléfono con grabadora de voz y un programa de edición de ejemplo que puede repetir un trozo en bucle, agregar eco y subir o bajar el volumen. Regla del grupo: volumen moderado y pausas de silencio para cuidar los oídos. " + CLAVE)
build(
    O2, 2, F,
    use="Aprenderé a experimentar con voz, objetos sonoros, instrumentos y tecnologías, a describir sus timbres y a elegir recursos según lo que la obra necesita.",
    prior=["Sé que el timbre es el color del sonido.", "Sé leer una cuadrícula de pulsos.", "Conozco algunas familias de instrumentos."],
    explain=[
        "Los recursos de producción musical son todo lo que se usa para hacer sonar y registrar una obra: la voz, los objetos sonoros, los instrumentos y las tecnologías. La voz puede cantar, hablar o susurrar, en zona grave o aguda. Un objeto sonoro es un objeto cotidiano que se usa como fuente de sonido, como una caja o una botella plástica con arroz. Un instrumento está hecho para producir sonidos musicales.",
        "Cada recurso tiene un timbre y una forma de sonar en el tiempo: puede ser seco y corto, como un golpe en una caja, o sostenido, como una flauta dulce, o apagarse lento, como un metalófono. Antes de componer se explora cada recurso y se anota cómo suena, para decidir cuál sirve a cada idea. La tecnología puede grabar, repetir un trozo en bucle (loop), agregar eco, superponer capas y cambiar el volumen.",
        "La tecnología es un recurso, no el autor: quien compone toma las decisiones. En este cuaderno el programa de edición es de ejemplo y se describe por escrito; el trabajo con software real queda como complemento de tu docente. Se cuida el oído con volumen moderado y pausas, no se golpean objetos que se rompan ni con bordes filosos, y se pide permiso antes de grabar o compartir la voz de otras personas.",
    ],
    vocab=[("recurso de producción", "voz, objeto sonoro, instrumento o tecnología que se usa para hacer o registrar música"), ("objeto sonoro", "objeto cotidiano usado como fuente de sonido"), ("bucle", "trozo grabado que se repite una y otra vez"),
           ("capa", "sonido o grabación que se superpone a otros"), ("eco", "efecto que repite el sonido más débil después de un instante"), ("sostenido", "que se mantiene sonando")],
    worked=[
        ("Elegir por timbre", "Se necesita un sonido sostenido y de tono definido para una melodía lenta. Los recursos son una caja, una flauta dulce y unas reglas. ¿Cuál conviene?",
         ["La caja y las reglas dan golpes cortos; no sostienen el sonido.", "La flauta dulce sostiene el sonido y tiene notas definidas."],
         "La flauta dulce"),
        ("Calcular un bucle", "Un trozo de 4 pulsos a 60 pulsos por minuto se repite en bucle 6 veces. ¿Cuántos segundos dura el resultado?",
         ["A 60 pulsos por minuto cada pulso dura 1 segundo, así que el trozo dura 4 segundos.", "Repetido 6 veces dura 6 × 4 = 24 segundos."],
         "24 segundos"),
    ],
    mistakes=[("Elegir un recurso por «el que más suena» y no por el timbre que la idea necesita.", "Se confunde volumen con expresión.", "Elige según cómo suena en el tiempo: seco, sostenido o que se apaga."),
              ("Pensar que la tecnología compone sola.", "Se olvida que las decisiones las toma quien compone.", "Decide tú qué grabar, qué repetir y cuándo; la tecnología solo lo ejecuta.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un objeto sonoro?', 'Un objeto cotidiano que se usa como fuente de sonido musical', 'Un instrumento caro que solo se compra en tiendas', 'Una nota escrita en la cuadrícula', 'Un objeto sonoro nace de un objeto cotidiano, como una caja o una botella con arroz.'),
        ('abc', '{F} ¿Cuál de los recursos de la ficha es un instrumento?', 'El metalófono', 'La caja de cartón', 'La botella plástica con arroz', 'El metalófono está hecho para producir sonidos musicales; la caja y la botella son objetos sonoros.'),
        ('abc', '{F} ¿Qué recurso produce un sonido continuo parecido a la lluvia?', 'La botella plástica con arroz, agitada', 'La caja de cartón golpeada', 'Las reglas golpeadas en la mesa', 'La ficha dice que la botella con arroz agitada suena como lluvia continua.'),
        ('abc', '{F} Para marcar con un golpe grave, seco y corto los pulsos de una pieza, ¿qué recurso conviene?', 'La caja de cartón', 'La flauta dulce', 'La botella con arroz', 'La ficha describe la caja como golpe grave, seco y corto, lo que se necesita.'),
        ('=', '{F} Un patrón de 8 pulsos, a 120 pulsos por minuto, se repite en bucle 8 veces. ¿Cuántos segundos dura el resultado?', '8*8*60//120', 'Primero se cuentan los pulsos totales del bucle y luego se pasan a segundos.', ' s'),
        ('abc', 'En Composición musical: ¿qué hace un bucle (loop)?', 'Repite un trozo grabado una y otra vez', 'Cambia las notas de un trozo sin que nadie lo decida', 'Apaga el sonido cuando alguien habla', 'El bucle repite un trozo; no cambia las notas ni apaga el sonido.'),
        ('=', 'Un grupo graba una pieza capa por capa: 4 capas, cada una de 16 segundos, grabadas una después de otra. ¿Cuántos segundos de grabación necesita en total?', '4*16', 'Cada capa se graba por separado, así que se suman los segundos de las cuatro.', ' s'),
        ('abc', '{F} Se busca una melodía de sonido sostenido y notas definidas. ¿Qué recurso de la ficha sirve?', 'La flauta dulce', 'Las reglas de plástico', 'La botella con arroz', 'La flauta dulce sostiene el sonido y tiene notas definidas.'),
        ('{F} Escribe qué recurso usarías para (a) un golpe agudo y corto y (b) una textura de lluvia continua. Responde en ese orden.', '(a) las reglas de plástico; (b) la botella con arroz', 'Según la ficha, las reglas dan golpe agudo y corto y la botella imita la lluvia.'),
        ('abc', '{F} El grupo usa metalófono, guitarra y las cuatro voces a volumen alto durante todo el ensayo. ¿Qué decisión cuida mejor sus oídos?', 'Bajar a volumen moderado, hacer pausas de silencio y tocar por turnos', 'Seguir igual para que el oído se acostumbre poco a poco al volumen alto', 'Taparse una oreja solo mientras suena fuerte y seguir con el mismo volumen', 'La regla del grupo pide volumen moderado y pausas; acostumbrarse al ruido no protege el oído.'),
        ('abc', 'Una estudiante graba su voz con eco y dice que «la tecnología compuso la pieza». ¿Qué es más preciso?', 'La tecnología grabó y transformó el sonido, pero quien compone decidió qué grabar y cómo usarlo', 'Es correcto: cuando se usa tecnología, la obra queda compuesta sola por el programa', 'La tecnología no puede transformar el sonido, solo reproducirlo tal como fue grabado', 'La tecnología es un recurso; las decisiones de composición son de quien la usa.'),
        ('abc', '{F} La restricción dice: «solo recursos de la sala y voces, sin comprar nada y sin dañar objetos». ¿Qué propuesta la cumple?', 'Voces, botella con arroz y caja de cartón golpeada con las manos', 'Comprar un sintetizador para la pieza', 'Golpear el metalófono con un martillo para lograr un sonido nuevo', 'Solo la primera usa recursos disponibles y no daña objetos; las otras compran o dañan.'),
        ('abc', 'Un grupo graba una prueba con las voces de sus compañeros y la sube a un chat público sin preguntar. ¿Qué corresponde?', 'Pedir permiso antes de compartir las voces y compartir solo por el medio acordado con el grupo', 'Dejarla publicada, porque era solo una prueba y nadie la va a tomar en serio', 'Borrar el chat para que nadie se entere y no volver a hablar del tema', 'Grabar y compartir son decisiones distintas; las personas deben dar permiso para cada una.'),
    ],
    ctx=('abc', '{F} Un grupo compone un paisaje sonoro «tormenta que pasa». ¿Qué asignación de recursos es coherente con la ficha?', 'Lluvia con la botella con arroz, trueno con la caja de cartón y gotas con las reglas', 'Lluvia con las reglas, trueno con la botella y gotas con la caja', 'Lluvia con la flauta dulce, trueno con las reglas y gotas con la caja', 'La botella imita lluvia continua, la caja da golpe grave como un trueno y las reglas dan golpes agudos como gotas.'),
    sc=[
        ("En Composición musical: ¿qué es un recurso de producción?", "Una voz, un objeto sonoro, un instrumento o una tecnología que se usa para hacer o registrar música", "Los recursos son los medios con que se hace sonar y se registra una obra."),
        ('abc', 'Un sonido que se mantiene sonando mientras se sopla es:', 'Sostenido', 'Seco', 'Corto', 'Sostenido significa que se mantiene sonando.'),
        ("¿Qué regla cuida los oídos al explorar recursos?", "Usar volumen moderado y hacer pausas de silencio", "El oído se protege bajando el volumen y descansando."),
    ],
    op=("Con la {F}, diseña una pieza de 4 compases para el grupo. Escribe qué recurso hace cada capa (ritmo, melodía y textura), con un patrón de 4 pulsos como «X . X X» para el ritmo y una nota de la escala por pulso para la melodía.",
        "Ritmo: caja de cartón «X . X X». Textura: botella con arroz agitada suavemente en los pulsos 1 y 3. Melodía: flauta dulce | Mi Fa Sol Mi |. Cuatro compases: el patrón se repite y la flauta varía la última nota en el compás 3.",
        ["asigna un recurso a cada capa", "escribe un patrón rítmico con X y puntos", "escribe una melodía con notas", "respeta la regla de volumen moderado"],
        ["hoja con las tres capas escritas"],
        ["usar un recurso que no está en la ficha", "olvidar el volumen moderado", "patrones con más o menos de 4 pulsos"],
        "Pregunta: «¿por qué elegiste ese recurso para esa capa?». Si no usa el timbre como argumento, pídele que lo describa."),
    reinforce="Anota tres objetos seguros de tu casa, cómo los harías sonar sin dañarlos y si el sonido sería corto, sostenido o que se apaga.",
    extend="Explica con un ejemplo inventado cómo cambiaría el carácter de una melodía si se tocara con voz en vez de flauta dulce.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (dos planes de ejemplo, inventados). Desafío: un tema de 8 compases para un cortometraje escolar ficticio. Cada compás tiene 4 pulsos. "
     "Plan P1, ambiente tranquilo: 64 pulsos por minuto; un acorde por compás en el orden Do, La menor, Fa, Sol, que se repite una vez; melodía de notas largas. "
     "Plan P2, ambiente de baile: 120 pulsos por minuto; un acorde por compás en el orden La menor, Fa, Do, Sol, que se repite una vez; un bombo repetido con el patrón «X . . . X . . .». "
     "Notas de los acordes: Do = Do Mi Sol; La menor = La Do Mi; Fa = Fa La Do; Sol = Sol Si Re. "
     "Cuadrícula de 8 casillas por compás: cada pulso se divide en 2 casillas, así que los pulsos 1, 2, 3 y 4 caen en las casillas 1, 3, 5 y 7. Clave: X es un golpe y «.» un silencio.")
build(
    O2, 3, F,
    use="Aprenderé a elegir elementos del lenguaje musical (ritmo, melodía, armonía, textura, forma) y procedimientos (ostinato, pregunta y respuesta) para lograr un estilo o ambiente que mi obra necesita.",
    prior=["Conozco los parámetros del sonido.", "Sé leer una cuadrícula de pulsos.", "Sé que un acorde suena como varias notas juntas."],
    explain=[
        "Al componer se eligen elementos del lenguaje musical según el ambiente o estilo que se busca. El ritmo organiza los sonidos en el tiempo. La melodía es una sucesión de notas. La armonía es la combinación de notas que suenan a la vez, formada por acordes; un acorde es un grupo de tres o más notas que suenan juntas, por ejemplo Do–Mi–Sol. La textura es la cantidad de capas que suenan al mismo tiempo.",
        "Los procedimientos ayudan a organizar esos elementos. Un ostinato es un patrón breve que se repite sin cambios y sirve de base, como un bombo que repite «X . . . X . . .» (golpe en los pulsos 1 y 3). La pregunta y respuesta es un diálogo entre dos frases: la pregunta suele terminar en una nota que deja la idea abierta y la respuesta en la nota de reposo, que en Do mayor es Do. Un tempo lento y notas largas suelen dar calma; un tempo rápido y un ostinato claro suelen invitar a bailar.",
        "Los acordes menores, como La menor, suelen sonar más serios o sombríos que los mayores, pero el efecto también depende del tempo, el timbre y el ritmo. Por eso cada decisión se prueba y se justifica con el propósito. No existe una fórmula única: se combinan elementos, se escuchan los resultados y se ajusta.",
    ],
    vocab=[("armonía", "combinación de notas que suenan a la vez, formada por acordes"), ("acorde", "grupo de tres o más notas que suenan juntas"), ("ostinato", "patrón breve que se repite sin cambios como base"),
           ("textura", "cantidad de capas que suenan al mismo tiempo"), ("pregunta y respuesta", "diálogo entre dos frases: una abierta y otra que reposa"), ("elemento del lenguaje musical", "ritmo, melodía, armonía, timbre, textura o forma")],
    worked=[
        ("Elegir según el ambiente", "Una escena ficticia de mucha energía pide un ambiente de baile. Las opciones son (a) 56 pulsos por minuto con notas largas, o (b) 128 pulsos por minuto con un ostinato repetido. ¿Cuál conviene y por qué?",
         ["El ambiente pide energía y movimiento; el tempo rápido y el ostinato claro los favorecen.", "El tempo lento con notas largas favorece la calma."],
         "La opción (b), por su tempo rápido y su ostinato"),
        ("Escribir un ostinato", "Escribe en 8 casillas un ostinato que suene solo en los pulsos 2 y 4.",
         ["Los pulsos 1, 2, 3 y 4 caen en las casillas 1, 3, 5 y 7, así que los pulsos 2 y 4 son las casillas 3 y 7.", "Se ponen X en esas casillas y puntos en las demás."],
         ". . X . . . X ."),
    ],
    mistakes=[("Elegir acordes sin revisar qué notas los forman.", "Se mezclan notas que no pertenecen al acorde.", "Escribe las notas del acorde antes de armar la melodía de apoyo."),
              ("Dar por seguro que lo menor siempre suena triste.", "Se ignora el efecto del tempo, el timbre y el ritmo.", "Di «suele sonar más sombrío» y verifica con una prueba.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un ostinato?', 'Un patrón breve que se repite sin cambios y sirve de base', 'Una melodía larga que cambia en cada compás y nunca vuelve a repetirse', 'Un acorde que suena una sola vez al final de la pieza y la cierra', 'El ostinato se define por repetir un patrón breve sin cambios.'),
        ('abc', 'En Composición musical: ¿qué es un acorde?', 'Un grupo de tres o más notas que suenan juntas', 'Una sola nota que se toca muy fuerte para marcar el pulso de la pieza', 'Un silencio de cuatro pulsos que separa dos secciones de una obra', 'Un acorde combina varias notas que suenan al mismo tiempo.'),
        ('abc', '{F} ¿Qué notas forman el acorde de Fa en la ficha?', 'Fa, La y Do', 'Do, Mi y Sol', 'Sol, Si y Re', 'La ficha da Fa = Fa La Do.'),
        ('abc', '{F} ¿Qué plan usa el tempo más lento?', 'P1, a 64 pulsos por minuto', 'P2, a 120 pulsos por minuto', 'Los dos usan el mismo tempo', 'P1 va a 64 y P2 a 120 pulsos por minuto; 64 es el más lento.'),
        ('=', '{F} ¿Cuántos segundos más dura el plan P1 que el P2? Cada plan tiene 8 compases de 4 pulsos.', '8*4*60//64-8*4*60//120', 'Se calcula la duración de cada plan en segundos y se restan.', ' s'),
        ('abc', '{F} En el compás de Fa de P1, ¿qué nota de la melodía pertenece al acorde?', 'La', 'Re', 'Si', 'La forma parte de Fa–La–Do; Re y Si no.'),
        ('abc', '{F} ¿Con qué acorde comienza el plan P2?', 'La menor, que es un acorde menor', 'Do, que es un acorde mayor', 'Sol, que es un acorde mayor', 'El orden de P2 empieza en La menor.'),
        ('{F} Escribe en 8 casillas un ostinato de bombo que suene solo en los pulsos 1 y 4.', 'X . . . . . X .', 'Los pulsos 1 y 4 caen en las casillas 1 y 7; el resto son silencios.'),
        ('abc', 'Una frase de pregunta termina en Sol y la frase de respuesta en Do. ¿Qué efecto produce en Do mayor?', 'La pregunta queda abierta y la respuesta cierra en el reposo', 'Las dos frases cierran por igual en la nota de reposo y suenan idénticas', 'Las dos frases quedan abiertas, sin llegar nunca a la nota de reposo', 'Sol deja la idea abierta; Do es la nota de reposo en Do mayor.'),
        ('abc', '{F} ¿Qué plan responde mejor a una «canción de cuna»?', 'P1, por su tempo lento y sus notas largas', 'P2, por su ostinato de bombo y su tempo rápido', 'Ninguno de los dos sirve para ese ambiente', 'Una canción de cuna busca calma, y P1 es lento con notas largas.'),
        ('abc', '{F} En P2 la melodía puede variar cada dos compases. ¿Por qué se sostiene el bombo igual?', 'El ostinato da una base estable para bailar y la variación se agrega en la melodía', 'Porque el bombo no puede cambiar nunca, por reglas de la forma musical', 'Porque la melodía no debe variar mientras el bombo marca el pulso', 'Un ostinato estable sostiene el baile y permite variar sobre él.'),
        ('abc', 'Un estudiante afirma que un acorde menor siempre suena triste. ¿Qué respuesta es más precisa?', 'Suele sonar más sombrío, pero depende también del tempo, el timbre y el ritmo', 'Tiene razón: un acorde menor siempre suena triste en cualquier tempo y timbre', 'Los acordes menores no tienen ningún efecto en cómo se siente una pieza', 'El efecto de un acorde se combina con otros elementos, así que no es una regla fija.'),
        ('abc', '{F} Una estudiante quiere el plan P2 pero con un ambiente de misterio. ¿Qué cambio de elementos es el más coherente?', 'Bajar el tempo, mantener La menor como acorde inicial y tocar el bombo suave', 'Subir el tempo y tocar el bombo más fuerte para dar más tensión a la escena', 'Cambiar el acorde inicial a Do mayor y subir el tempo para dar más luminosidad', 'El misterio suele pedir lentitud, color menor y poca fuerza; las otras opciones aumentan la energía.'),
    ],
    ctx=('abc', 'Un cortometraje escolar ficticio pide una música de misterio para una escena nocturna de 8 compases. ¿Qué combinación de elementos es la más coherente?', 'Tempo lento, un acorde menor al comienzo, ostinato suave y timbre grave', 'Tempo rápido, acorde mayor, bombo fuerte y una melodía que salta de nota en nota', 'Tempo rápido, textura de muchas capas, volumen alto y un ostinato muy marcado', 'El misterio suele pedir lentitud, color menor y suavidad; las otras opciones corresponden a energía.'),
    sc=[
        ("En Composición musical: ¿qué es la textura?", "La cantidad de capas que suenan al mismo tiempo", "La textura describe cuántas capas se oyen a la vez."),
        ('abc', 'Un patrón de bombo que se repite sin cambios es un:', 'Ostinato', 'Contraste', 'Retrógrado', 'Un patrón breve que se repite sin cambios es un ostinato.'),
        ("¿Dónde termina la frase de respuesta en Do mayor?", "En Do, que es la nota de reposo", "En Do mayor la nota de reposo es Do, y la respuesta cierra ahí."),
    ],
    op=("Con la {F}, elige el plan P1 o el P2 y escribe para él: el ambiente, el tempo, los acordes de los 4 primeros compases y un ostinato de 8 casillas. Explica en una frase qué elemento del lenguaje musical hace que se logre el ambiente.",
        "Elijo P1, ambiente tranquilo, 64 pulsos por minuto; acordes Do, La menor, Fa, Sol; ostinato suave «X . . . . . . .». El tempo lento y las notas largas logran la calma.",
        ["elige un plan y nombra el ambiente", "escribe tempo, acordes y un ostinato con 8 casillas", "explica con un elemento del lenguaje musical"],
        ["hoja con el plan, el ostinato y la explicación"],
        ["ostinato con más o menos de 8 casillas", "acordes que no están en la ficha", "no explicar con un elemento"],
        "Pregunta: «¿qué elemento del lenguaje musical produce el ambiente que buscas?». Si no puede nombrarlo, pídele que revise tempo, ritmo y acorde."),
    reinforce="Escribe un ostinato de 8 casillas para un ambiente de baile y otro para un ambiente de calma, y compara cuántos golpes tiene cada uno.",
    extend="Explica con un ejemplo inventado por qué dos piezas con los mismos acordes pueden sonar muy distintas.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (pieza de ejemplo «Camino de lluvia», inventada, forma ABA, 96 pulsos por minuto, compás de 4 pulsos). "
     "Sección A, compases 1 a 4: c1 | Mi Fa Sol Mi |; c2 | Fa Sol La Sol |; c3 | Mi Fa Sol Mi |; c4 | Re Mi Re Do |. "
     "Sección B, compases 5 a 8: c5 | La - La - |; c6 | Sol - Sol - |; c7 | La - Sol - |; c8 | Sol - - . |. "
     "Retorno de A, compases 9 a 12: igual que los compases 1 a 4. Arreglo: la sección A con flauta dulce y guitarra; la sección B solo con metalófono. " + CLAVE)
build(
    O2, 4, F,
    use="Aprenderé a componer una obra breve con forma ABA, usando repetición, variación y contraste, y a distribuir los recursos de producción por sección para un formato concreto.",
    prior=["Reconozco repetición, variación y contraste.", "Sé escribir motivos en una cuadrícula de pulsos.", "Conozco recursos como voz, objetos e instrumentos."],
    explain=[
        "La forma musical es la organización de una obra en secciones. La forma ABA tiene una sección A de inicio, una sección B que contrasta y un retorno de A. El retorno da unidad, porque el oyente reconoce la idea inicial, y el contraste de B da variedad. Las secciones se rotulan con letras y se dice cuántos compases tiene cada una.",
        "Dentro de una sección se pueden usar procedimientos: una frase de pregunta (compases 1 y 2) y otra de respuesta (compases 3 y 4), con la respuesta repitiendo el comienzo y terminando en reposo. La sección B puede contrastar con notas largas, otro registro o menos capas. El arreglo es la decisión de qué recurso toca cada parte; cambiar de recursos entre secciones también contrasta, porque cambia el timbre y la textura.",
        "Componer una obra breve es un proceso: se escribe el plan de la forma, se redactan las secciones con notas y pulsos, se revisa que cada compás tenga sus 4 pulsos y se anota quién toca cada parte. Todo se registra en texto, con la misma notación del cuaderno, sin necesidad de software ni de partitura formal.",
    ],
    vocab=[("forma", "organización de una obra en secciones"), ("sección", "parte de una obra con una idea propia, rotulada con una letra"), ("retorno", "vuelta de la sección inicial al final"),
           ("arreglo", "decisión de qué recurso toca cada parte de la obra"), ("frase", "unidad musical que expresa una idea completa"), ("reposo", "sensación de llegada que da una nota final")],
    worked=[
        ("Calcular la duración", "Una pieza ABA tiene 3 secciones de 3 compases, cada compás de 4 pulsos, a 108 pulsos por minuto. ¿Cuántos segundos dura?",
         ["Hay 3 × 3 = 9 compases, y cada uno tiene 4 pulsos, o sea 36 pulsos.", "A 108 pulsos por minuto, 36 pulsos duran 36 × 60 ÷ 108 = 20 segundos."],
         "20 segundos"),
        ("Reconocer el retorno", "Una pieza ficticia es | Re Mi Fa Re | La - La - | Re Mi Fa Re |. ¿Qué forma tiene?",
         ["El primer compás (A) y el tercero son iguales: hay un retorno.", "El compás del medio usa notas largas y otras notas: contrasta (B)."],
         "ABA"),
    ],
    mistakes=[("Hacer que la sección B sea la sección A con otro volumen.", "No hay contraste suficiente: solo cambia un rasgo.", "Cambia varios rasgos en B, como ritmo, registro o recursos."),
              ("Escribir compases con más o menos de 4 pulsos.", "No se cuenta cada pulso, incluidos los silencios y las prolongaciones.", "Cuenta los pulsos de cada compás antes de pasarlo en limpio.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es la forma ABA?', 'Una sección inicial, una sección que contrasta y el retorno de la inicial', 'Tres secciones completamente distintas que no vuelven a aparecer en la obra', 'Una sola sección repetida tres veces seguidas sin ningún cambio ni contraste', 'ABA vuelve a la idea inicial después de un contraste.'),
        ('abc', '{F} ¿Qué compases forman la sección B?', 'Los compases 5 a 8', 'Los compases 1 a 4', 'Los compases 9 a 12', 'La ficha indica que B ocupa los compases 5 a 8.'),
        ('abc', '{F} ¿En qué compás de la sección A termina la respuesta en reposo?', 'El compás 4, que termina en Do', 'El compás 2, que termina en Sol', 'El compás 3, que termina en Mi', 'El compás 4 termina en Do, la nota de reposo en Do mayor.'),
        ('=', '{F} La pieza tiene 12 compases de 4 pulsos. ¿Cuántos segundos dura a 96 pulsos por minuto?', '12*4*60//96', 'Se calculan los pulsos totales y se pasan a segundos con los pulsos por minuto.', ' s'),
        ('abc', '{F} ¿Qué relación hay entre el compás 1 y el compás 3?', 'Repetición: son idénticos', 'Contraste: suenan completamente distintos', 'Variación: cambia la última nota', 'Ambos dicen | Mi Fa Sol Mi |, sin ningún cambio.'),
        ('abc', '{F} ¿Qué nota final distingue la respuesta (compás 4) de la pregunta (compás 2)?', 'La respuesta termina en Do y la pregunta en Sol', 'La respuesta termina en Sol y la pregunta en Do', 'Las dos terminan en Mi', 'El compás 2 termina en Sol (abierto) y el compás 4 en Do (reposo).'),
        ('=', '{F} ¿Cuántos pulsos suenan en la sección B, sin contar los silencios? Cuenta cada nota con sus prolongaciones.', '4+4+4+3', 'Los compases 5, 6 y 7 suenan los 4 pulsos y el compás 8 suena 3 pulsos y deja un silencio.', ' pulsos'),
        ('{F} ¿Qué compases forman el retorno de A?', 'Los compases 9 a 12', 'Son los compases que repiten los compases 1 a 4 después de la sección B.'),
        ('abc', '{F} El arreglo toca B solo con metalófono. ¿Qué contraste produce respecto de A?', 'Un cambio de timbre y de textura, porque quedan menos capas y otro color', 'Ninguno, porque las notas son las mismas y solo con otras notas habría contraste', 'Solo un cambio de dinámica, porque el metalófono suena más fuerte que la flauta', 'Menos instrumentos y otro timbre cambian la textura y el color de la sección.'),
        ('abc', '¿Por qué el retorno de A al final de una pieza ABA sirve a la obra?', 'Da unidad, porque el oyente vuelve a reconocer la idea inicial', 'Alarga la obra sin ninguna razón musical, solo para llegar a la duración pedida', 'Evita que haya contraste, porque borra lo que ocurrió en la sección B', 'El retorno hace reconocible la idea inicial después del contraste.'),
        ('abc', 'Un estudiante propone una sección B idéntica a la A pero tocada fuerte. ¿Cumple la función de B?', 'No del todo, porque solo cambia la dinámica y B debe contrastar en varios rasgos', 'Sí, porque cualquier cambio entre dos secciones es suficiente para ser un contraste', 'Sí, porque con más volumen la sección B ya suena como una idea completamente distinta', 'Una sección B contrasta cuando cambia varios rasgos; solo cambiar la dinámica es una variación.'),
        ('abc', '{F} Si la pieza se tocara a 120 pulsos por minuto y el límite fuera de 20 segundos, ¿qué ocurre?', 'No cabe: dura 24 segundos, 4 más que el límite', 'Cabe: dura 12 segundos, 8 menos que el límite de 20 segundos', 'Cabe: dura 20 segundos justos, igual que el límite que permite el desafío', 'Son 48 pulsos y a 120 pulsos por minuto duran 24 segundos.'),
        ('abc', 'Una estudiante toma una melodía de una canción comercial, cambia una sola nota y la presenta como propia. ¿Qué corresponde?', 'Crear material propio o declarar la fuente y pedir permiso, porque cambiar una nota no la hace propia', 'Presentarla como propia, porque con una sola nota distinta ya es una obra nueva', 'Cambiar solo el título de la obra para evitar problemas con quien la creó', 'Una pequeña modificación no convierte una melodía ajena en propia.'),
    ],
    ctx=('abc', '{F} Para que otro grupo pueda tocar «Camino de lluvia» en la muestra, ¿qué información debe tener el registro en texto?', 'Título, forma ABA, tempo, compases con sus pulsos y qué recurso toca cada sección', 'Solo el título de la pieza y los nombres de las personas que la tocarán', 'La forma ABA sin las notas, porque el otro grupo las puede inventar al tocar', 'Para tocar la pieza otro grupo necesita las notas, los pulsos, el tempo y el arreglo por sección.'),
    sc=[
        ("En Composición musical: ¿qué es el arreglo?", "La decisión de qué recurso toca cada parte de la obra", "El arreglo reparte voces e instrumentos por sección."),
        ('abc', 'Una sección que vuelve igual al final de la pieza se llama:', 'Retorno', 'Contraste', 'Cadencia', 'El retorno repite la sección inicial al final.'),
        ("¿Qué se revisa en cada compás antes de pasar en limpio una pieza?", "Que sume sus 4 pulsos, contando notas, prolongaciones y silencios", "Cada compás debe completar los pulsos del compás."),
    ],
    op=("Con la {F} como modelo de forma, compón una pieza ABA de 3 compases por sección (9 compases) en Do mayor. Escribe cada compás con 4 pulsos, el tempo, y qué recurso toca cada sección. La sección B debe contrastar en al menos dos rasgos.",
        "Tempo 90. A: | Do Mi Sol Mi | Fa La Fa Re | Mi Re Do - |. B: | Sol - Sol - | La - Sol - | Sol - - . |. A vuelve igual. Flauta y guitarra en A; solo metalófono en B. B contrasta en ritmo (notas largas) y en recursos.",
        ["nueve compases con 4 pulsos cada uno", "forma ABA con retorno", "B contrasta en al menos dos rasgos", "indica tempo y recursos"],
        ["hoja con la pieza escrita en texto y el arreglo"],
        ["compases con más o menos de 4 pulsos", "B igual a A con otro volumen", "olvidar el tempo o los recursos"],
        "Pregunta: «¿en qué dos rasgos contrasta tu sección B?». Si solo cambió uno, pídele que pruebe otro, como el registro o los recursos."),
    reinforce="Escribe una pieza AB de 2 compases por sección y marca con una línea los dos rasgos que cambian en B.",
    extend="Explica con un ejemplo inventado cuándo una forma ABA puede ser mejor que una forma AB para un propósito.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 5 (registro de ejemplo de la pieza «Marea», versión 1, inventada). Tempo: 80 pulsos por minuto; 8 compases. "
     "c1 | Do Re Mi Fa |; c2 | Sol - Mi . |; c3 | La Sol Fa |; c4 | Mi Re Do - - |; c5 | Re Mi Fa Sol |; c6 | La - - . |; c7 | Sol Fa Mi Re |; c8 | Do - - - |. "
     "Observaciones del ensayo: (1) en el compás 3 el grupo se adelantó; (2) el metalófono suena más fuerte que la flauta durante todo el tema; (3) no se entiende cuándo termina la pieza. " + CLAVE)
build(
    O2, 5, F,
    use="Aprenderé a registrar una obra en notación de texto, a rotular sus versiones y a ajustar la pieza a partir de lo observado en un ensayo, con criterios y prioridades.",
    prior=["Sé escribir compases de 4 pulsos.", "Sé que un compás debe sumar sus pulsos.", "Sé dar retroalimentación con observación, efecto y sugerencia."],
    explain=[
        "Registrar una obra es dejar por escrito lo necesario para que otra persona la pueda tocar o para volver a ella más tarde. Una ficha técnica incluye el título, la autoría, la forma, el tempo, el compás, los instrumentos o recursos de cada parte y la duración. La partitura en texto escribe los compases con la notación de este cuaderno, y cada compás debe sumar sus 4 pulsos, contando notas, prolongaciones y silencios.",
        "Cada vez que se cambia la obra se guarda una versión nueva (versión 1, versión 2) y se anota qué cambió y por qué. Así se puede volver atrás y saber a qué versión se refiere cada comentario. Tras un ensayo se anotan las observaciones, se ordenan por prioridad (primero lo que impide tocar juntos o entender la obra) y se prueba un ajuste a la vez.",
        "Para saber si un ajuste mejoró la obra se vuelve a tocar el trozo cambiado y se compara con el registro anterior: ¿se resolvió el problema observado y se mantuvo el propósito? Ajustar no es empezar de nuevo, sino cambiar lo necesario con evidencia. Este cuaderno no usa software de edición real: el registro se hace en papel.",
    ],
    vocab=[("ficha técnica", "registro de título, autoría, forma, tempo, compás, recursos y duración"), ("versión", "forma de la obra en un momento del proceso"), ("prioridad", "lo que se resuelve primero por su importancia"),
           ("ajuste", "cambio que se hace para resolver un problema observado"), ("ensayo", "momento en que se toca la obra para probarla"), ("registro", "anotación por escrito de la obra o del proceso")],
    worked=[
        ("Detectar un error de pulsos", "Un compás dice | Fa Mi Re |. ¿Está bien escrito para un compás de 4 pulsos?",
         ["Se cuenta un pulso por cada palabra: Fa, Mi, Re son 3 pulsos.", "Faltan 1 pulso para completar 4: se puede prolongar Re con un guion o agregar una nota o un silencio."],
         "No: tiene 3 pulsos y debe tener 4"),
        ("Priorizar un ajuste", "Después de un ensayo, un grupo observa dos problemas: (a) dos compases tienen pulsos incorrectos y se tocan distinto; (b) el volumen de un instrumento es algo fuerte. ¿Qué resuelve primero?",
         ["El problema (a) impide tocar juntos, porque cada integrante lee un compás distinto.", "El problema (b) se corrige después, sin cambiar la partitura."],
         "Primero (a), los compases con pulsos incorrectos"),
    ],
    mistakes=[("Borrar la versión anterior al hacer un cambio.", "Después no se puede comparar ni volver atrás.", "Guarda cada versión rotulada y anota qué cambió."),
              ("Cambiar varias cosas a la vez tras un ensayo.", "No se sabe cuál ajuste mejoró o empeoró la obra.", "Cambia una cosa por vez y vuelve a probar.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es una ficha técnica de una obra?', 'Un registro del título, la autoría, la forma, el tempo, el compás, los recursos y la duración', 'Un comentario del público sobre si la obra gustó y qué sintieron al oírla', 'Una lista de las personas que asistieron a la muestra y a qué hora llegaron', 'La ficha técnica reúne los datos necesarios para entender y volver a tocar la obra.'),
        ('abc', '¿Para qué sirve rotular cada versión de una obra (versión 1, versión 2)?', 'Para volver atrás y saber a qué versión se refiere cada comentario', 'Para que el grupo no tenga que ensayar la versión anterior otra vez', 'Para que la versión 1 se borre sola cuando se termine la versión 2', 'Rotular las versiones permite comparar y no confundir comentarios.'),
        ('abc', '{F} ¿Qué compases de la ficha no suman 4 pulsos?', 'Los compases 3 y 4', 'Los compases 1 y 2', 'Solo el compás 8', 'El compás 3 tiene 3 pulsos y el compás 4 tiene 5; los demás suman 4.'),
        ('{F} ¿Cuántos pulsos tiene el compás 4 tal como está escrito?', '5 pulsos', 'Mi, Re, Do suman 3 pulsos y los dos guiones prolongan Do dos pulsos más, así que son 5.'),
        ('=', '{F} ¿Cuántos pulsos suman los 8 compases tal como están escritos?', '4+4+3+5+4+4+4+4', 'Se suman los pulsos que tiene cada compás tal como está escrito, incluidos el de 3 y el de 5.', ' pulsos'),
        ('=', '{F} Si la pieza se corrige a 8 compases de 4 pulsos, ¿cuántos segundos dura a 80 pulsos por minuto?', '8*4*60//80', 'Se pasan los pulsos totales a segundos con los pulsos por minuto.', ' s'),
        ('{F} Corrige el compás 3 prolongando Fa un pulso, de modo que sume 4 pulsos.', '| La Sol Fa - |', 'Con La y Sol de un pulso cada una y Fa de dos pulsos, el compás suma 4.'),
        ('{F} Corrige el compás 4 quitando el pulso sobrante y conservando todas las notas.', '| Mi Re Do - |', 'Con Mi y Re de un pulso y Do de dos pulsos, el compás suma 4.'),
        ('abc', '{F} La observación 2 dice que el metalófono tapa a la flauta. ¿Qué ajuste es coherente?', 'Bajar la dinámica del metalófono para equilibrarlo con la flauta', 'Subir el tempo de toda la pieza para que el metalófono suene menos', 'Eliminar la flauta de la pieza para que no compita con el metalófono', 'El problema es de equilibrio de volumen, que se resuelve ajustando la dinámica.'),
        ('abc', '{F} La observación 3 dice que no se entiende cuándo termina la pieza. ¿Qué ajuste ayuda más?', 'Escribir un final con la nota larga del compás 8 y una indicación de apagar el sonido al terminar', 'Agregar cuatro compases más con notas nuevas para que el final se alargue y se note', 'Subir el volumen del metalófono en todo el tema para que el final se destaque', 'Marcar el final con una nota larga que se apaga indica claramente el cierre.'),
        ('abc', 'Un estudiante borra la versión 1 antes de probar la versión 2. ¿Qué riesgo tiene?', 'Si la versión 2 empeora, no se puede volver atrás ni comparar', 'Ninguno, porque las versiones anteriores no sirven una vez que existe una nueva', 'La pieza se vuelve más rápida porque desaparece la versión que marcaba el tempo', 'Sin la versión anterior no hay con qué comparar ni a dónde volver.'),
        ('abc', '{F} Hay tiempo para corregir un solo problema antes de la próxima clase. ¿Qué criterio permite priorizar?', 'Resolver primero lo que impide tocar juntos o entender la obra, como los compases con pulsos incorrectos', 'Resolver primero lo que menos tiempo toma, aunque no cambie lo que impide ensayar', 'Resolver primero lo que más le gusta al autor de la pieza, aunque sea secundario', 'Los compases incorrectos hacen que cada integrante toque algo distinto; eso impide el ensayo.'),
        ('abc', 'Tras un ajuste, ¿cómo se comprueba que la pieza mejoró?', 'Se vuelve a tocar el trozo cambiado y se compara con la observación anterior y con el propósito', 'Se asume que mejoró porque se hizo un cambio y el grupo trabajó mucho en él', 'Se pregunta solo a quien hizo el cambio si cree que quedó mejor que antes', 'La evidencia de mejora es que el problema observado se resuelve al volver a tocar.'),
    ],
    ctx=('=', 'Tras el ajuste, la versión 2 de «Marea» tiene 32 pulsos y el grupo la prueba a 96 pulsos por minuto. ¿Cuántos segundos dura?', '32*60//96', 'Los 32 pulsos se pasan a segundos con los pulsos por minuto.', ' s'),
    sc=[
        ("En Composición musical: ¿qué es una versión de una obra?", "La forma de la obra en un momento del proceso", "Cada versión guarda un estado de la obra para comparar."),
        ('abc', 'Un compás de 4 pulsos escrito | Do Re Mi Fa Sol | tiene:', '5 pulsos, uno de más', '4 pulsos, está bien', '3 pulsos, falta uno', 'Cinco nombres de nota suman cinco pulsos.'),
        ("¿Qué se ajusta primero tras un ensayo?", "Lo que impide tocar juntos o entender la obra", "Esos problemas afectan a todo el grupo."),
    ],
    op=("Con la {F}, escribe la versión 2 de los compases 3 y 4 con la corrección que indicaste en tus respuestas, y anota en una frase qué cambió y por qué. Después elige otra observación del ensayo y propón un ajuste.",
        "Versión 2: c3 | La Sol Fa - |; c4 | Mi Re Do - |. Cambié las duraciones para que los compases sumen 4 pulsos; así el grupo se mueve junto. Observación 2: bajo la dinámica del metalófono para equilibrarlo con la flauta.",
        ["escribe los dos compases con 4 pulsos", "explica qué cambió y por qué", "propone otro ajuste con relación a una observación"],
        ["hoja con los compases corregidos y los ajustes"],
        ["dejar compases sin sumar 4 pulsos", "no decir por qué", "cambiar más de un rasgo sin registrarlo"],
        "Pregunta: «¿cómo sabes que los compases ahora suman 4?». Si no cuenta, pídele que lo haga en voz alta."),
    reinforce="Escribe tres compases de 4 pulsos con un error de pulsos cada uno, y luego corrígelos explicando qué cambiaste.",
    extend="Explica con un ejemplo inventado por qué conviene cambiar una sola cosa tras cada ensayo.",
)

# ============================================================ OAC-02, clase 6
F = ("Ficha 6 (obra de ejemplo «Marea» de un grupo ficticio, que la presentará en la muestra del liceo). Elementos que el grupo usó: "
     "(1) una melodía creada por el grupo; "
     "(2) un patrón de bombo de 4 pulsos repetido, inspirado en la idea general de la pieza B de un referente internacional de ejemplo, pero con ritmo propio; "
     "(3) un fragmento de 10 segundos de una canción comercial, que el grupo quiere usar de fondo sin permiso; "
     "(4) la voz de una compañera, que aceptó cantar, pero no ha dicho si acepta que se publique en línea; "
     "(5) una foto de portada sacada de internet, de autoría desconocida. La pieza dura 90 segundos.")
build(
    O2, 6, F,
    use="Aprenderé a evaluar una obra propia, a atribuir las fuentes que la inspiraron o que usa, a respetar los derechos de autor y los permisos de las personas y a decidir cómo difundirla.",
    prior=["Sé la diferencia entre inspirarse y copiar.", "Sé registrar versiones.", "Sé dar retroalimentación sobre una obra."],
    explain=[
        "El derecho de autor protege la obra concreta de quien la crea: su melodía, su letra, su grabación. No protege las ideas generales, como usar estrofas o repetir un patrón. Por eso se puede inspirar en una idea, pero no reproducir la expresión de otra persona sin permiso. Atribuir es indicar quién creó lo que se usa o lo que inspiró la obra; se hace en los créditos, con nombre de la obra y de la persona.",
        "Algunas personas publican su obra con licencias abiertas, que permiten ciertos usos si se cumplen condiciones, como nombrar a la autora. Las obras pasan a ser de uso libre después de un plazo que fija la ley; si tienes dudas, consulta a tu docente o a un especialista. La voz y la imagen de una persona también requieren su permiso, y el permiso para grabar no es lo mismo que el permiso para publicar.",
        "Antes de difundir una obra se evalúa el proceso y el resultado: si cumple el propósito, qué decisiones funcionaron y qué se mejoraría. Luego se elige el medio de difusión según el público: una muestra presencial, un enlace privado para familias o un medio público. Los créditos incluyen a quienes participaron, las fuentes que inspiraron la obra y la licencia. Este cuaderno no entrega asesoría legal.",
    ],
    vocab=[("derecho de autor", "protección de la obra concreta de quien la crea"), ("atribuir", "indicar quién creó lo que se usa o inspiró la obra"), ("licencia abierta", "permiso de uso con condiciones, como nombrar a la autora"),
           ("crédito", "mención de quienes participaron o inspiraron la obra"), ("permiso", "autorización para usar la voz, imagen u obra de alguien"), ("difundir", "dar a conocer una obra a un público")],
    worked=[
        ("Decidir sobre una fuente", "Un grupo ficticio quiere usar 8 segundos de una canción comercial como fondo de su video escolar. ¿Qué debe hacer?",
         ["Una canción comercial tiene titular de derechos y el grupo no lo es.", "Debe pedir permiso al titular o reemplazar el fragmento por material propio."],
         "Pedir permiso o usar material propio"),
        ("Redactar un crédito", "Un grupo se inspiró en una idea de patrón repetido de una pieza ficticia «Luz» de la compositora ficticia Ana Rojas. Redacta el crédito.",
         ["El crédito nombra la obra y su autora y dice qué se tomó: la idea general.", "También aclara que el ritmo y las notas son propios."],
         "Patrón inspirado en la idea general de «Luz», de Ana Rojas (ejemplo); ritmo y notas propios"),
    ],
    mistakes=[("Pensar que si cambio una nota ya no necesito atribuir.", "Una pequeña modificación no vuelve propia una obra ajena.", "Atribuye lo que inspiró la obra y crea material propio."),
              ("Creer que el permiso para grabar sirve para publicar.", "Grabar y publicar son decisiones distintas.", "Pide permiso para cada uso y respeta si alguien no acepta.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es atribuir una fuente?', 'Indicar quién creó la idea, melodía o grabación que se usa o inspiró la obra', 'Cambiar una nota de una melodía ajena para que parezca una melodía distinta', 'Borrar el nombre de quien creó la melodía para que la obra quede más limpia', 'Atribuir es reconocer públicamente a quien creó lo que se usa o inspiró.'),
        ('abc', '¿Qué protege el derecho de autor?', 'La obra concreta, como la melodía, la letra o la grabación', 'Cualquier idea general, como usar estrofas o repetir un patrón de cuatro pulsos', 'Solo las obras que tienen muchos oyentes y que ya se han hecho famosas', 'Protege la expresión concreta, no las ideas generales.'),
        ('abc', '{F} ¿Qué elemento de la ficha es creación propia del grupo y no necesita permiso de otra persona?', 'El elemento 1, la melodía creada por el grupo', 'El elemento 3, el fragmento de la canción comercial', 'El elemento 5, la foto de internet', 'La melodía creada por el grupo es de su autoría.'),
        ('abc', '{F} ¿Qué corresponde hacer con el elemento 3, el fragmento de canción comercial?', 'Pedir permiso al titular de los derechos o reemplazarlo por material propio', 'Usarlo igual, porque dura solo 10 segundos y nadie notará que es de otra persona', 'Usarlo si se cambia el título de la obra y se menciona que es de ejemplo', 'Una canción comercial tiene titular de derechos; la duración no elimina esa necesidad.'),
        ('abc', '{F} El elemento 2 toma la idea general de un patrón repetido y lo resuelve con ritmo propio. ¿Qué corresponde?', 'Mencionar la inspiración en los créditos', 'Ocultar la inspiración para que parezca todo original', 'Pedir permiso al referente para usar patrones repetidos', 'La idea general no está protegida, pero se reconoce la inspiración en los créditos.'),
        ('=', '{F} La pieza dura 90 segundos y 10 segundos son del fragmento comercial. ¿Cuántos segundos son de material del grupo?', '90-10', 'Se restan los segundos del fragmento ajeno al total de la pieza.', ' s'),
        ('abc', '{F} ¿Qué crédito es completo para el elemento 2?', 'Patrón de bombo inspirado en la idea general de la pieza B del referente internacional de ejemplo; ritmo propio', 'Patrón de bombo inspirado en algo que escuchamos por ahí, sin indicar la fuente', 'Sin crédito, porque lo cambiamos tanto que ya no se parece a ninguna otra obra', 'El crédito completo nombra la fuente y aclara qué es propio.'),
        ('abc', 'Una compositora publica su pieza con una licencia que permite usarla si se la nombra. ¿Qué debes hacer al usarla?', 'Nombrar a la compositora y respetar las condiciones de la licencia', 'Usarla sin nombrarla, porque la licencia es abierta', 'Usarla con cualquier condición, porque «abierta» significa sin condiciones', 'Una licencia abierta permite el uso bajo condiciones, como la atribución.'),
        ('abc', '{F} La compañera aceptó cantar, pero no dijo si acepta que su voz se publique en línea. ¿Qué corresponde?', 'Preguntarle y respetar su decisión; si no acepta, presentar la obra solo en la muestra o regrabarla sin su voz', 'Publicarla igual en línea, porque la compañera ya aceptó cantarla para la grabación', 'Publicarla primero y avisarle después, para que no tenga tiempo de negarse', 'El permiso para cantar no incluye el permiso para publicar.'),
        ('abc', 'Un estudiante dice: «si cambio una nota ya es mío». ¿Qué respuesta es correcta?', 'Una pequeña modificación no convierte una obra ajena en propia; hay que crear material propio o atribuir', 'Es correcto: con una nota distinta la obra ya es propia y no hace falta atribuir', 'Es correcto, pero solo si la canción original es muy famosa y todos la conocen', 'Una modificación mínima no cambia que la expresión original es de otra persona.'),
        ('abc', '{F} La foto de portada del elemento 5 es de autoría desconocida. ¿Qué decisión es adecuada?', 'Reemplazarla por una imagen propia del grupo o con permiso de quien la creó', 'Usarla igual, porque si no se sabe de quién es, nadie podrá reclamar por ella', 'Quitarle el recuadro de la autoría para que no se note de dónde proviene', 'Si no se sabe quién es el autor, no se puede pedir permiso; es mejor una imagen propia.'),
        ('abc', 'El grupo debe elegir un medio para difundir su obra. ¿Cuál criterio es el más razonable?', 'Elegir según el propósito, el público y los permisos de todas las personas que aparecen', 'Elegir el medio con más gente aunque alguien no haya dado permiso', 'Elegir el medio que guarde la obra por más tiempo, aunque no llegue al público pensado', 'La difusión se decide con el público y los permisos, no con la cantidad de oyentes.'),
        ('abc', 'Al cerrar el proyecto, ¿qué evaluación es completa?', 'Compara el resultado con el propósito, explica las decisiones tomadas e incluye la atribución de las fuentes', 'Dice si la obra les gustó a sus integrantes y cuánto trabajaron en ella', 'Dice cuántas personas la oyeron y cuántas aplaudieron al terminar la presentación', 'La evaluación completa une propósito, decisiones y atribución.'),
    ],
    ctx=('abc', 'El liceo publicará un catálogo de proyectos. La ficha de «Marea» dice solo «Créditos: el grupo». ¿Qué le falta?', 'Los nombres de quienes aceptaron aparecer, las fuentes que inspiraron la obra y la fecha de la versión', 'Una foto de los integrantes tomada sin pedirles permiso a cada persona', 'El nombre de otro proyecto del liceo que también participó en el catálogo', 'Los créditos nombran a quienes participaron con permiso y las fuentes, y la versión indica cuál se presenta.'),
    sc=[
        ("En Composición musical: ¿qué es un crédito?", "La mención de quienes participaron o inspiraron la obra", "Los créditos reconocen a las personas y fuentes de una obra."),
        ('abc', 'El permiso para grabar la voz de una persona:', 'No equivale al permiso para publicarla', 'Equivale al permiso para publicarla', 'No se necesita nunca', 'Grabar y publicar son usos distintos que se autorizan por separado.'),
        ("¿Qué es una licencia abierta?", "Un permiso de uso con condiciones, como nombrar a la autora", "Las licencias abiertas permiten usos, pero piden respetar sus condiciones."),
    ],
    op=("Con la {F}, escribe la lista de créditos de «Marea» (qué se agradece o atribuye y a quién), y propone qué harías con los elementos 3, 4 y 5 para que la obra pueda presentarse sin problemas. Escribe además una frase de evaluación de la obra en relación con su propósito.",
        "Créditos: melodía y letra, el grupo; patrón de bombo inspirado en la idea general de la pieza B del referente internacional de ejemplo; voz, la compañera, con su permiso para la muestra. Elemento 3: pedir permiso o reemplazar por material propio. Elemento 4: preguntar y respetar su decisión sobre publicar. Elemento 5: usar una imagen propia. Evaluación: la pieza cumple el propósito de calma porque el tempo es lento y el final cierra con una nota larga.",
        ["créditos con fuentes y personas", "decisión para los elementos 3, 4 y 5", "evaluación relacionada con el propósito"],
        ["hoja con créditos, decisiones y evaluación"],
        ["no atribuir una fuente", "publicar la voz sin permiso", "evaluar solo por gusto"],
        "Pregunta: «¿de quién es cada elemento y qué permiso tienes?». Si no distingue lo propio de lo ajeno, pídele una lista de dos columnas."),
    reinforce="Escribe los créditos de una pieza inventada tuya: autoría, fuente de inspiración y las personas que participaron con su permiso.",
    extend="Explica con un ejemplo inventado por qué conviene preguntar a un especialista cuando no se sabe si una obra es de uso libre.",
)
