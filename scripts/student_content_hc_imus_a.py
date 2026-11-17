"""Interpretación musical 3.º y 4.º medio HC: OAC-01 (innovar al resolver desafíos de la interpretación: fraseo, ritmo, armonía, ejecución y evaluación crítica). Piezas inventadas y descritas en texto."""
from __future__ import annotations

from hc_imus_common import CLAVE, build

O1 = "AR-IMUS-3y4-OAC-01"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (pieza de ejemplo «Tarde quieta», inventada, para voz y guitarra, a 80 pulsos por minuto). "
     "Melodía: c1 | Mi Mi Fa Sol |; c2 | Sol Fa Mi Re | /; c3 | Do Do Re Mi |; c4 | Re - Do - |. "
     "Acordes de la guitarra: c1 Do, c2 Sol, c3 Do, c4 Sol y luego Do (dos pulsos cada uno). "
     "Dinámica: c1 y c2 en p; c3 con < hasta mf; c4 en mf con >. Frases: la primera es c1-c2 y la segunda es c3-c4. " + CLAVE)
build(
    O1, 1, F,
    use="Aprenderé a reconocer en una frase musical el fraseo, el ritmo, la dinámica, la armonía y la ejecución, y a describirlos con evidencia, para decidir después cómo interpretarla de manera propia.",
    prior=["Sé leer una cuadrícula de pulsos y los nombres de las notas.", "Reconozco dinámica suave y fuerte.", "Sé describir lo que oigo antes de opinar."],
    explain=[
        "Interpretar es dar sonido a una pieza tomando decisiones. Los procedimientos expresivos son las herramientas con que se toman: el fraseo (agrupar los sonidos en frases, como las oraciones de un texto, con un comienzo, una dirección y una respiración), el ritmo (el patrón de duraciones de los sonidos sobre el pulso), la dinámica (la fuerza o suavidad) y la armonía (los acordes, que son varias notas que suenan juntas y acompañan a la melodía).",
        "Para reconocer estos rasgos se escucha o se lee la pieza una vez por cada rasgo. Se pregunta dónde empieza y termina cada frase, qué duraciones se repiten, cómo cambia la fuerza y cuándo cambia el acorde. Cada respuesta se apoya en evidencia: un compás, un símbolo, un pulso. Los símbolos «<» y «>» se llaman crescendo (subir la fuerza poco a poco) y decrescendo (bajarla poco a poco). «Suena triste» no es evidencia; «la frase baja y termina en p» sí lo es.",
        "La ejecución es la manera concreta de tocar o cantar: la postura (espalda larga y hombros sueltos), la respiración, la afinación y la estabilidad del pulso. Innovar al resolver un desafío no es cambiarlo todo, sino decidir con un propósito cuál de estos rasgos conservar y cuál transformar. Por eso, antes de decidir, se reconocen los rasgos de la pieza tal como está escrita.",
    ],
    vocab=[("fraseo", "manera de agrupar y conducir los sonidos en frases, con respiración"), ("ritmo", "patrón de duraciones de los sonidos sobre el pulso"),
           ("dinámica", "grado de fuerza o suavidad del sonido"), ("acorde", "varias notas que suenan juntas como acompañamiento"),
           ("armonía", "forma en que se encadenan los acordes que acompañan"), ("ejecución", "manera concreta de tocar o cantar una pieza"),
           ("crescendo y decrescendo", "subir o bajar la fuerza poco a poco («<» y «>»)")],
    worked=[
        ("Localizar las frases", "Una melodía de ejemplo es | La La Si Do | Si La Sol - | / | Mi Mi Fa Sol | La - - - |. La barra «/» marca una respiración. ¿Cuántas frases tiene y de cuántos compases es cada una?",
         ["La respiración «/» corta la melodía en dos partes: lo que está antes y lo que está después.", "Antes hay 2 compases y después hay otros 2 compases: son 2 frases de 2 compases cada una."],
         "2 frases de 2 compases"),
        ("Describir con evidencia", "En un fragmento de ejemplo, el compás 1 dice «p», el compás 2 dice «<» y el compás 3 dice «f». Describe la dinámica con evidencia.",
         ["Se nombra el rasgo y se cita el símbolo: el fragmento parte suave (p) en el compás 1.", "Luego la fuerza sube poco a poco en el compás 2 (<) y llega a fuerte (f) en el compás 3."],
         "Parte suave, sube poco a poco en el compás 2 y llega a fuerte en el compás 3"),
    ],
    mistakes=[("Escribir «la pieza es linda» como si fuera un rasgo reconocido.", "Es una opinión sin evidencia musical.", "Nombra el rasgo (dinámica, frase, acorde) y cita el compás donde aparece."),
              ("Creer que la respiración de una frase es un silencio del compás.", "Se mezclan la pausa de la escritura con la respiración de la frase.", "La respiración «/» separa frases; un silencio «.» dura un pulso dentro del compás.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es el fraseo?', 'Agrupar los sonidos en frases con comienzo, dirección y respiración', 'Tocar cada sonido con la misma fuerza y sin ninguna pausa entre frases', 'Cambiar el nombre de las notas de la melodía para que parezcan nuevas', 'El fraseo organiza los sonidos como las oraciones de un texto; no es tocar parejo ni renombrar notas.'),
        ('abc', '{F} ¿Dónde termina la primera frase de «Tarde quieta»?', 'Al final del compás 2, donde está la marca de respiración', 'Al final del compás 4, donde terminan todas las notas', 'Al final del compás 1, porque ahí se repite la nota Mi', 'La barra «/» después del compás 2 marca la respiración y cierra la primera frase.'),
        ('abc', '{F} ¿Qué dinámica tienen los compases 1 y 2?', 'Suave (p)', 'Media (mf)', 'Fuerte (f)', 'La ficha indica p en los compases 1 y 2, o sea que suenan suaves.'),
        ('abc', '{F} ¿Qué acorde toca la guitarra en el compás 2?', 'Sol', 'Do', 'Re', 'La ficha asigna el acorde Sol al compás 2; Do suena en los compases 1 y 3.'),
        ('abc', '{F} ¿Qué significa «<» en el compás 3?', 'La fuerza sube poco a poco hasta mf', 'La fuerza baja poco a poco hasta p', 'La melodía se toca más lenta hasta casi detenerse', 'El símbolo < indica crescendo: subir la fuerza gradualmente; la ficha lo lleva hasta mf.'),
        ('=', '{F} La pieza tiene 4 compases de 4 pulsos a 80 pulsos por minuto. ¿Cuántos segundos dura sin contar la respiración?', '4*4*60//80', 'Los segundos se obtienen multiplicando los pulsos por 60 y dividiendo por los pulsos por minuto.', ' s'),
        ('{F} Anota la dinámica de cada compás, de c1 a c4, con los símbolos de la ficha.', 'c1 p; c2 p; c3 < hasta mf; c4 mf con >', 'Se lee compás por compás el símbolo de dinámica que indica la ficha.'),
        ('abc', '{F} Se quiere que la segunda frase suene más intensa que la primera sin cambiar ninguna nota. ¿Qué decisión lo logra?', 'Tocarla con crescendo desde p hasta mf', 'Tocarla en p con el mismo volumen de la primera', 'Cambiarla a decrescendo hasta casi no oírse', 'Un crescendo hacia mf deja la segunda frase más intensa; las otras opciones la dejan igual o más débil.'),
        ('=', '{F} ¿Cuántas notas nuevas suenan en toda la melodía? El guion «-» solo prolonga, no cuenta como nota nueva.', '4+4+4+2', 'Los compases 1, 2 y 3 tienen cuatro notas y el compás 4 tiene dos, porque el guion prolonga.', ' notas'),
        ('abc', 'Dos oyentes describen el compás 4 de «Tarde quieta». Ana: «termina en mf con decrescendo y cambia de acorde a mitad del compás». Beto: «termina feo». ¿Cuál comentario sirve para decidir cómo interpretarlo?', 'El de Ana, porque nombra rasgos y los ubica en un compás', 'El de Beto, porque dice lo que siente sin rodeos', 'Los dos sirven igual, porque cada uno dice lo que piensa', 'Un comentario útil nombra un rasgo audible y su lugar; «feo» no permite saber qué cambiar.'),
        ('abc', '{F} La pieza quiere transmitir calma. ¿Qué rasgo de la ejecución apoyaría más ese propósito?', 'Un pulso estable y una respiración tranquila entre las frases', 'Acelerar el pulso en cada compás para que la pieza suene más viva y animada', 'Cantar siempre en f para que la voz se escuche bien en toda la sala', 'La calma se logra con pulso estable y respiración serena; acelerar o cantar fuerte transmite otra cosa.'),
        ('abc', '{F} Un grupo propone respirar también en medio del compás 3. ¿Qué efecto tendría?', 'Partiría la segunda frase en dos y cambiaría su dirección', 'Haría la primera frase más larga, de tres compases', 'No cambiaría nada, porque la respiración no afecta al fraseo', 'Una respiración adicional corta la frase de dos compases en dos partes; el fraseo depende de dónde se respira.'),
        ('=', '{F} En un ensayo el grupo acelera el compás 3 y lo toca a 120 pulsos por minuto en vez de 80. ¿Cuántos segundos más rápido dura ese compás de 4 pulsos?', '4*60//80-4*60//120', 'Se comparan los segundos del compás a 80 pulsos por minuto y a 120 pulsos por minuto.', ' s'),
    ],
    ctx=('=', 'Para un acto del liceo el grupo toca «Tarde quieta» dos veces seguidas, con una pausa de 4 segundos entre ambas. Cada vez dura 12 segundos. ¿Cuánto dura todo?', '12+4+12', 'Se suman las dos duraciones de la pieza y la pausa que hay entre ellas.', ' s'),
    sc=[
        ("En Interpretación musical: ¿qué es un acorde?", "Varias notas que suenan juntas como acompañamiento", "El acorde acompaña a la melodía; en la ficha cambia de Do a Sol."),
        ('abc', 'Una barra «/» en la notación de este cuaderno indica:', 'Una respiración entre frases', 'Un cambio de acorde en la guitarra', 'Un compás completo de silencio', 'La barra oblicua marca el corte entre frases, donde se respira.'),
        ("¿Por qué se cita un compás al describir un rasgo?", "Porque así la descripción tiene evidencia y otra persona puede comprobarla", "Citar el compás convierte una opinión en una observación comprobable."),
    ],
    op=("Con la {F}, describe en tres frases tres rasgos de «Tarde quieta» (uno de fraseo, uno de dinámica y uno de armonía), cada uno con su compás como evidencia. Luego propón qué rasgo conservarías y cuál cambiarías para un propósito alegre, y por qué.",
        "Fraseo: tiene dos frases de dos compases y se respira tras c2. Dinámica: c1 y c2 están en p y c3 sube con < hasta mf. Armonía: la guitarra cambia de Do a Sol en c2. Para un propósito alegre conservaría las frases y cambiaría la dinámica a mf desde c1, porque la fuerza media suena más animada.",
        ["describe tres rasgos distintos", "cita un compás como evidencia en cada uno", "elige un rasgo que conserva y uno que cambia", "justifica con el propósito alegre"],
        ["hoja con tres descripciones con su compás y la decisión justificada"],
        ["escribir opiniones sin citar compás", "repetir el mismo rasgo tres veces", "cambiar la pieza sin relacionarla con el propósito"],
        "Pregunta: «¿en qué compás se oye eso?». Si no puede citarlo, pídele que vuelva a leer la ficha y busque el símbolo."),
    reinforce="Escribe una frase propia de dos compases en la cuadrícula, con una marca de respiración al final, y anota su dinámica compás por compás.",
    extend="Explica con un ejemplo por qué dos personas pueden describir los mismos rasgos y aun así interpretar la frase de manera distinta.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (registro de tomas de ejemplo, inventado). Ritmo de mesa para dos manos suaves, a 120 pulsos por minuto: | X . X X | X . X . |. "
     "Desafío: que el ritmo suene seguro y claro en una sala de ensayo pequeña. "
     "Toma 1 (articulación): golpes cortos y separados; efecto: más ligero. "
     "Toma 2 (acento): golpe más marcado en el primer pulso de cada compás; efecto: más firme. "
     "Toma 3 (tempo): bajar a 60 pulsos por minuto; efecto: más pesado y calmo. "
     "Toma 4 (postura): sentarse con la espalda larga y los hombros sueltos; efecto: las manos se cansan menos. " + CLAVE)
build(
    O1, 2, F,
    use="Aprenderé a explorar recursos de ejecución (articulación, acento, tempo, postura y respiración) con tomas pequeñas y a registrarlas para decidir con evidencia, cuidando el cuerpo y el oído.",
    prior=["Reconozco fraseo, ritmo, dinámica y acorde.", "Sé leer una cuadrícula de pulsos.", "Sé que una prueba cambia un solo rasgo."],
    explain=[
        "Un recurso de ejecución es algo que se puede variar al tocar o cantar la misma pieza. La articulación es cómo se ataca y se suelta cada sonido: corto y separado (picado) o largo y unido (ligado). El acento es un sonido marcado con más fuerza que sus vecinos. El tempo es la velocidad del pulso, medida en pulsos por minuto. Cada recurso cambia el carácter sin cambiar las notas ni el ritmo escrito.",
        "Explorar es hacer tomas: repeticiones breves donde se cambia un solo recurso y todo lo demás se mantiene. Cada toma se registra con cuatro datos: qué recurso cambió, qué se conservó, cuánto duró y qué efecto se oyó o se sintió. Con varias tomas registradas se compara y se decide con evidencia, no por costumbre ni por gusto del momento.",
        "Interpretar también cuida el cuerpo. Antes de ensayar se calienta con suavidad (soltar hombros, mover muñecas y cuello sin forzar, respirar lento). Se trabaja con volumen moderado, se descansa en silencio entre tomas y se detiene el ensayo si hay dolor, cosquilleo o fatiga fuerte. Una buena postura y una respiración baja también son recursos: ayudan a tocar con más claridad y menos esfuerzo.",
    ],
    vocab=[("articulación", "manera de atacar y soltar cada sonido (picado, ligado)"), ("acento", "sonido marcado con más fuerza que los que lo rodean"),
           ("tempo", "velocidad del pulso, en pulsos por minuto"), ("toma", "repetición breve en la que se cambia un solo recurso"),
           ("calentamiento", "preparación suave del cuerpo antes de ensayar"), ("ligado", "sonidos unidos sin separación entre ellos")],
    worked=[
        ("Reconocer el recurso", "Un grupo toca el ritmo | X . X X | primero con golpes suaves y luego con un golpe más marcado en el primer pulso. ¿Qué recurso cambió?",
         ["El ritmo escrito, el tempo y la articulación son los mismos en las dos tomas.", "Solo cambió la fuerza del primer golpe: se agregó un acento."],
         "El acento"),
        ("Registrar una toma", "Una estudiante canta una frase a 70 pulsos por minuto y luego a 90, y anota «la segunda me gustó». Escribe un registro útil.",
         ["Se anota el recurso que cambió (el tempo) y lo que se conservó (notas, ritmo y dinámica).", "Se agrega un efecto comprobable por otra persona, como «a 90 suena más ligero y animado»."],
         "Toma: tempo 90 en vez de 70; se conservan notas, ritmo y dinámica; efecto: más ligero y animado"),
    ],
    mistakes=[("Cambiar la articulación, el tempo y el acento en la misma toma.", "No se sabe cuál de los tres produjo el efecto.", "Cambia un solo recurso por toma y registra cada una."),
              ("Seguir ensayando con dolor en las manos para terminar la toma.", "Se pone el resultado por encima del cuerpo.", "Detén el ensayo, descansa en silencio y retoma con una postura suelta.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es la articulación?', 'La manera de atacar y soltar cada sonido, por ejemplo picado o ligado', 'La velocidad con que se mantiene el pulso durante toda la pieza, medida en pulsos por minuto', 'El nombre de las notas que se usan dentro de cada compás de la pieza escrita', 'La articulación se refiere a cómo empieza y termina cada sonido; el tempo y las notas son otros recursos.'),
        ('abc', '{F} ¿Qué recurso cambia la toma 2?', 'El acento, porque el primer pulso de cada compás se marca más', 'La articulación, porque los golpes se hacen más cortos y separados entre sí', 'El tempo, porque el pulso se hace más rápido en cada compás de la toma', 'La toma 2 solo agrega un golpe más marcado en el primer pulso; el resto se conserva.'),
        ('abc', '{F} ¿Qué se conserva en la toma 3?', 'El ritmo escrito y la articulación; solo cambia el tempo', 'El tempo; cambian el ritmo escrito, los acentos y la articulación', 'Nada; se cambia toda la forma de tocar el ritmo y la velocidad', 'La toma 3 cambia solamente la velocidad, de 120 a 60 pulsos por minuto.'),
        ('=', '{F} El ritmo tiene 2 compases de 4 pulsos. ¿Cuántos segundos dura una pasada a 120 pulsos por minuto?', '2*4*60//120', 'Los segundos son los pulsos por 60 divididos en los pulsos por minuto.', ' s'),
        ('abc', '¿Por qué conviene hacer una sola variación por toma?', 'Para saber qué cambio produjo el efecto que se oye', 'Para que la toma se termine antes que las otras', 'Para no tener que descansar entre las tomas', 'Si se cambian varios recursos juntos, no se puede saber a cuál se debe el efecto.'),
        ('abc', '{F} Se busca que el ritmo suene más firme sin cambiar la velocidad ni la articulación. ¿Qué toma corresponde?', 'La toma 2, cuyo efecto registrado es más firme', 'La toma 1, cuyo efecto registrado es más ligero', 'La toma 3, cuyo efecto registrado es más calmo', 'El acento de la toma 2 produce el efecto más firme y deja la velocidad igual.'),
        ('=', '{F} La toma 3 baja a 60 pulsos por minuto. ¿Cuántos segundos dura una pasada de 8 pulsos?', '8*60//60', 'Se multiplican los pulsos por 60 y se divide por los pulsos por minuto.', ' s'),
        ('abc', 'Un grupo graba en su registro: «toma 5: ligado en vez de picado; se conservan tempo y acentos; efecto: más cantable». ¿Qué recurso cambió?', 'La articulación', 'El tempo de la pieza', 'El acento del compás', 'Pasar de picado a ligado cambia la articulación; el registro dice que tempo y acentos se conservan.'),
        ('abc', '{F} ¿Cuál es el registro correcto de la toma 1?', 'Cambió la articulación; se conservan ritmo y tempo; efecto: más ligero', 'Cambió el acento; se conservan ritmo y articulación; efecto: más firme', 'Cambió el tempo; se conservan ritmo y articulación; efecto: más calmo', 'La toma 1 solo cambia la articulación a golpes cortos y su efecto registrado es más ligero.'),
        ('abc', '{F} Un grupo dice: «cambiamos articulación, tempo y postura a la vez y la toma salió mejor, así que la articulación fue la clave». ¿Qué falla en su conclusión?', 'Con tres cambios juntos no se sabe cuál mejoró la toma', 'La articulación nunca puede influir en cómo suena un ritmo', 'La postura no se puede registrar porque no se oye', 'Para atribuir un efecto a un recurso hay que variar solo ese recurso y mantener los demás.'),
        ('abc', '{F} La toma 4 registra que las manos se cansan menos. ¿Cómo debe usarse ese dato?', 'Como evidencia para ensayar más tiempo con una postura suelta', 'Como un dato sin valor, porque el cansancio no cambia el sonido del ritmo', 'Como una razón para saltarse el calentamiento previo y ensayar sin pausas', 'Un efecto de comodidad y salud es evidencia válida; sostiene un ensayo más seguro y claro.'),
        ('abc', 'A los 10 minutos de ensayo, Sol siente un hormigueo en la muñeca. ¿Qué decisión es la más adecuada?', 'Detener la toma, descansar en silencio y retomar con una postura más suelta', 'Subir el tempo para terminar la toma más rápido y descansar después del ensayo', 'Apretar más las manos para mantener el control del ritmo hasta el final de la toma', 'Ante hormigueo o dolor se para y se descansa; forzar o acelerar aumenta el riesgo de lesión.'),
        ('=', 'Un grupo hace 4 tomas de 5 minutos cada una y descansa 2 minutos entre toma y toma (3 descansos). ¿Cuántos minutos dura la sesión?', '4*5+3*2', 'Se suman los minutos de las cuatro tomas y los de los tres descansos entre ellas.', ' minutos'),
    ],
    ctx=('abc', 'El desafío admite como máximo 10 segundos por pasada y el grupo quiere tocar el ritmo de 8 pulsos en la toma 3, a 60 pulsos por minuto. ¿Qué decisión es correcta?', 'Aceptar la toma, porque dura 8 segundos y cabe en el máximo', 'Descartar la toma, porque dura 12 segundos y se pasa', 'Aceptar la toma, porque a menor tempo siempre dura menos', 'A 60 pulsos por minuto, 8 pulsos duran 8 segundos, menos que el máximo de 10 segundos.'),
    sc=[
        ("En Interpretación musical: ¿qué es un acento?", "Un sonido marcado con más fuerza que los que lo rodean", "El acento destaca un sonido, como el primer pulso del compás en la toma 2."),
        ('abc', 'Para explorar, ¿cuántos recursos conviene cambiar por toma?', 'Uno', 'Todos a la vez', 'Ninguno', 'Con uno solo se sabe qué produjo el efecto.'),
        ("¿Qué haces si sientes dolor o cosquilleo en las manos durante un ensayo?", "Detengo la toma, descanso en silencio y retomo con una postura suelta", "La salud va primero: se para y se descansa antes de seguir."),
    ],
    op=("Con la {F}, elige dos tomas y escribe para cada una un registro de cuatro datos (recurso, lo que se conserva, duración y efecto). Después decide cuál usarías si el propósito fuera un ritmo de marcha tranquila y explica por qué.",
        "Toma 3: recurso, tempo (60); se conservan ritmo, articulación y acentos; una pasada de 8 pulsos dura 8 s; efecto: más pesado y calmo. Toma 2: recurso, acento en el primer pulso; se conservan tempo y articulación; una pasada dura 4 s; efecto: más firme. Para una marcha tranquila usaría la toma 3, porque su efecto registrado es calmo.",
        ["escribe dos registros con los cuatro datos", "nombra bien el recurso cambiado", "decide según el propósito", "justifica con el efecto registrado"],
        ["hoja con dos registros y la decisión justificada"],
        ["registrar solo «me gustó»", "olvidar qué se conserva", "elegir sin relacionar con el propósito"],
        "Pregunta: «¿qué dato de tu registro apoya tu decisión?». Si cita solo su gusto, pídele que cite el efecto registrado."),
    reinforce="Con el ritmo | X X . X | escribe tres tomas: una cambia la articulación, otra el acento y otra el tempo. Anota qué recurso cambió en cada una.",
    extend="Explica por qué un buen calentamiento y una postura suelta también son recursos de ejecución y no solo cuidados del cuerpo.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (caso de ejemplo «Camino al cerro», inventado, para una voz, a 60 pulsos por minuto). "
     "Melodía: c1 | Sol Sol La Si |; c2 | Do - Si - |; c3 | La La Sol Fa |; c4 | Sol - - . |. Acordes: c1 y c2 Do, c3 Fa, c4 Sol. "
     "Propósito: una frase que sube con esperanza y termina en reposo. Restricción: en el ensayo se hacen máximo 3 pasadas seguidas y luego 1 minuto de silencio. "
     "Opción A: respirar tras c2, crescendo en c1-c2 y decrescendo en c3-c4. "
     "Opción B: sin respirar hasta c4, todo en mf y parejo. "
     "Opción C: respirar tras c1 y tras c3, todo en p. " + CLAVE)
build(
    O1, 3, F,
    use="Aprenderé a ensayar una decisión de interpretación entre tres opciones, a justificarla con dos evidencias y a revisarla cuando cambia una condición, como el tempo o el espacio.",
    prior=["Reconozco fraseo, dinámica y armonía en una pieza.", "Sé registrar tomas con un recurso cambiado.", "Sé que ensayar tiene pausas de silencio."],
    explain=[
        "Una decisión de interpretación es una elección entre varias maneras posibles de tocar o cantar la misma pieza. Para decidir bien se compara cada opción con el propósito de la pieza, es decir, lo que debe transmitir, y con las restricciones del ensayo, como el tiempo, la cantidad de pasadas o el cuidado de la voz. Una opción sirve si apoya el propósito y cabe en las restricciones.",
        "Ensayar una decisión es probarla en pequeño, tomar nota y justificarla con dos evidencias: una de la pieza (por ejemplo, la frase sube en c1-c2) y una del ensayo (por ejemplo, la respiración tras c2 no cortó la melodía). También se explica por qué se descarta otra opción. Una justificación completa dice: «elijo A porque… y descarto B porque…».",
        "Una decisión no es definitiva: se revisa cuando cambia una condición. Si el tempo sube, si el espacio es más grande o si cambia el instrumento, puede que otra opción sirva mejor. Revisar no es un fracaso: es parte de interpretar con criterio. Ensayar con pausas de silencio y sin forzar la voz también forma parte de decidir bien.",
    ],
    vocab=[("decisión de interpretación", "elección de una manera de tocar o cantar una pieza"), ("propósito", "lo que la pieza debe transmitir"),
           ("restricción", "límite que la solución debe respetar, como el tiempo o las pasadas"), ("evidencia", "dato de la pieza o del ensayo que apoya una decisión"),
           ("crescendo", "subir la fuerza poco a poco"), ("decrescendo", "bajar la fuerza poco a poco")],
    worked=[
        ("Elegir con dos evidencias", "Una frase de ejemplo busca «tranquilidad». La opción X la toca en p con respiración cada dos compases; la opción Y la toca en f sin respirar. ¿Cuál elegirías y con qué evidencias?",
         ["La opción X se acerca a la tranquilidad: p es suave y las respiraciones dan calma. Esa es una evidencia de la pieza.", "La opción Y tiene fuerza alta y no respira, lo que tensa el cuerpo y no apoya el propósito. Se elige X y se descarta Y."],
         "La opción X, por su dinámica p y por sus respiraciones cada dos compases"),
        ("Revisar al cambiar la condición", "La decisión «respirar tras el compás 2» funcionaba a 60 pulsos por minuto. Ahora el tempo es de 120 pulsos por minuto. ¿Qué cambia en los segundos que hay para respirar?",
         ["A 120 pulsos por minuto cada pulso dura la mitad (0,5 s); un compás de 4 pulsos dura 2 segundos, no 4.", "Hay menos tiempo para respirar: puede hacer falta una respiración más corta o respirar en un punto de silencio."],
         "Hay la mitad del tiempo para respirar, así que conviene revisar el punto de respiración"),
    ],
    mistakes=[("Elegir una opción solo porque «me gusta más» y no citar evidencias.", "La decisión queda sin sustento y otra persona no puede revisarla.", "Cita una evidencia de la pieza y una del ensayo, y explica por qué descartas otra opción."),
              ("Mantener la decisión aunque cambie el tempo o el espacio.", "Se confunde decidir con no revisar.", "Pregunta qué cambió y si la opción sigue sirviendo al propósito.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es el propósito de una pieza?', 'Lo que se quiere transmitir con la interpretación', 'El número de pasadas que se hacen en un ensayo', 'La lista de las notas que la pieza utiliza', 'El propósito orienta las decisiones; no es una cantidad de pasadas ni una lista de notas.'),
        ('abc', '{F} ¿Qué propone la opción B respecto de la dinámica?', 'Tocar toda la frase en mf, de manera pareja', 'Tocar con crescendo al inicio y decrescendo al final', 'Tocar todo en p, con respiraciones frecuentes', 'La ficha dice que la opción B va en mf y parejo, sin cambios de fuerza.'),
        ('abc', '{F} ¿Cuántas respiraciones propone la opción C?', 'Dos: una tras c1 y otra tras c3', 'Una sola: tras el compás 2', 'Ninguna, porque canta de corrido hasta c4', 'La ficha indica respirar tras c1 y tras c3, es decir, dos veces.'),
        ('abc', '{F} ¿Qué opción responde mejor al propósito «sube con esperanza y termina en reposo»?', 'La opción A, porque crece al comienzo y baja al final', 'La opción B, porque mantiene todo parejo y sin cambios', 'La opción C, porque todo en p evita cualquier subida', 'Crescendo al inicio da sensación de subida y decrescendo al final da reposo.'),
        ('=', '{F} Una pasada completa son 4 compases de 4 pulsos a 60 pulsos por minuto. ¿Cuántos segundos duran 3 pasadas seguidas?', '3*4*4*60//60', 'Una pasada dura 16 pulsos a un pulso por segundo y se multiplica por 3 pasadas.', ' s'),
        ('abc', '{F} ¿Qué restricción del ensayo se está respetando si se hacen 3 pasadas y luego 1 minuto de silencio?', 'La de máximo 3 pasadas seguidas y pausa de silencio', 'La de que el tempo no cambie entre una pasada y otra', 'La de que se use un solo acorde en toda la pieza', 'La restricción habla de pasadas seguidas y de una pausa, que es lo que se cumple.'),
        ('abc', '{F} ¿Cuál justificación de la opción A usa una evidencia de la pieza y una del ensayo?', 'La melodía sube en c1-c2 y, al probar, la respiración tras c2 no cortó la frase', 'Me gusta más que las otras y además la probamos primero en la sala del liceo de siempre', 'Es la primera opción de la lista y casi todos los integrantes del grupo votaron por ella', 'Una evidencia de la pieza (la melodía sube) y otra del ensayo (la respiración no cortó la frase) sostienen la decisión.'),
        ('=', '{F} Un grupo ensaya 5 sesiones de 3 pasadas cada una, y cada pasada dura 16 segundos. ¿Cuántos minutos de canto efectivo suman, sin contar las pausas?', '5*3*16//60', 'Se multiplican las sesiones por las pasadas y por 16 segundos, y se pasa a minutos dividiendo por 60.', ' minutos'),
        ('abc', '{F} Se decide respirar tras c2 y subir la fuerza en c1-c2. ¿Qué rasgo de fraseo se está usando?', 'Una respiración que separa dos frases de dos compases', 'Una repetición exacta de los cuatro compases de la melodía', 'Un cambio de acorde de la guitarra en cada pulso', 'Respirar tras c2 divide la melodía en dos frases de dos compases.'),
        ('abc', '{F} El grupo baja la frase de 60 a 30 pulsos por minuto para cantarla más calmada. ¿Qué pasa con el tiempo para respirar tras c2?', 'Hay el doble de tiempo, así que conviene revisar que la frase no se corte al respirar', 'Hay la mitad del tiempo, así que la respiración debe ser más breve que antes', 'Queda igual, porque el tempo no afecta a las respiraciones de la frase', 'A 30 cada pulso dura el doble que a 60, y por eso el espacio para respirar se alarga.'),
        ('abc', '{F} El ensayo se hace en un salón muy grande y la voz casi no se oye con la opción C. ¿Qué revisión conserva el propósito y cuida la voz?', 'Mantener respiraciones de la opción C y subir un poco la fuerza, sin gritar', 'Cantar todo en f y sin respirar hasta lograr que se oiga hasta el fondo del salón', 'Dejar la opción C igual y pedir al público que se acerque al escenario del salón', 'La revisión debe conservar el propósito y cuidar la voz; gritar o forzar no cumple ninguna de las dos cosas.'),
        ('abc', 'Dos estudiantes defienden su decisión. Lía: «elijo A porque la melodía sube en c1-c2 y el decrescendo final da reposo». Teo: «elijo A porque la elegí antes». ¿Quién justifica mejor?', 'Lía, porque cita rasgos de la pieza que apoyan el propósito', 'Teo, porque mantener una decisión demuestra seguridad y firmeza ante el grupo', 'Ninguno, porque una decisión musical no se puede justificar con datos', 'Una justificación cita evidencia de la pieza; haber elegido antes no es una razón.'),
        ('abc', '{F} Un grupo hace 5 pasadas seguidas sin pausa «para ahorrar tiempo». ¿Qué problema tiene esa decisión?', 'Rompe la restricción de 3 pasadas y descuida la voz', 'Ninguno, porque más pasadas siempre mejoran la interpretación', 'Solo cambia el acorde de la pieza en cada pasada', 'La restricción y el cuidado de la voz piden máximo 3 pasadas seguidas y una pausa de silencio.'),
    ],
    ctx=('abc', 'Para la ceremonia del liceo el grupo debe cantar «Camino al cerro» en un patio abierto y con viento, donde las respiraciones suaves casi no se notan. ¿Qué ajuste conserva el propósito?', 'Marcar un poco más la subida y la llegada, sin forzar la voz', 'Cantar siempre en f y sin ninguna respiración entre frases', 'Eliminar la opción A y cantar en p para que se oiga menos', 'Se exagera un poco el contorno de la frase para que se perciba, sin gritar ni cambiar el propósito.'),
    sc=[
        ("En Interpretación musical: ¿qué es una restricción?", "Un límite que la solución debe respetar, como el tiempo o el número de pasadas", "Las restricciones limitan qué decisiones caben en el ensayo."),
        ('abc', 'Una justificación completa incluye:', 'Evidencia de la pieza, evidencia del ensayo y por qué se descarta otra opción', 'Solo el nombre de la opción elegida y la fecha en que se tomó la decisión', 'Solo el gusto personal de quien decide y lo que dijo la mayoría del grupo', 'Una decisión se sostiene con evidencias y con el motivo de descartar otra opción.'),
        ("¿Por qué se revisa una decisión cuando cambia el tempo?", "Porque puede que otra opción sirva mejor al propósito con la nueva condición", "Cambia el tiempo disponible para respirar y para marcar la dinámica."),
    ],
    op=("Con la {F}, elige una opción (A, B o C), cita una evidencia de la pieza y una del ensayo, y explica por qué descartas otra. Luego cambia una condición (el tempo pasa a 120 pulsos por minuto) y di si mantendrías la opción o la ajustarías.",
        "Elijo A: la melodía sube en c1-c2 y el crescendo lo acompaña (pieza); al probar, respirar tras c2 no cortó la frase (ensayo). Descarto B porque, al ser todo parejo, no muestra la subida. A 120 la respiración se acorta, así que la haría más breve y la mantendría.",
        ["elige una opción", "cita una evidencia de la pieza y una del ensayo", "descarta otra opción con una razón", "revisa la decisión con la condición nueva"],
        ["hoja con la decisión, las dos evidencias, la opción descartada y la revisión"],
        ["elegir sin evidencia", "olvidar descartar otra opción", "mantener la decisión sin revisar la condición"],
        "Pregunta: «¿qué dato de la ficha apoya tu elección?». Si no lo cita, pídele que busque el compás o el símbolo que lo respalda."),
    reinforce="Escribe una frase propia de cuatro compases y dos maneras distintas de interpretarla. Elige una y justifícala con una evidencia.",
    extend="Explica con un ejemplo cómo cambiaría tu decisión si la misma frase la tocara una flauta en vez de una voz.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (interpretaciones de ejemplo, inventadas) de la frase «Camino al cerro»: c1 | Sol Sol La Si |; c2 | Do - Si - |; c3 | La La Sol Fa |; c4 | Sol - - . |, a 60 pulsos por minuto. "
     "Propósito: sube con esperanza y termina en reposo. "
     "Interpretación de Ema: respira tras c2; crescendo en c1-c2 (p a mf); decrescendo en c3-c4 (mf a p); pulso estable; el último Sol se corta en el pulso 4 con el silencio. "
     "Interpretación de Hugo: respira tras c1 y tras c3; todo en mf; en c3 acelera (pasa de 60 a 80 pulsos por minuto); el último Sol se alarga durante el silencio. "
     "Criterios de la pauta: (1) fraseo claro; (2) dinámica al servicio del propósito; (3) pulso estable; (4) final limpio. " + CLAVE)
build(
    O1, 4, F,
    use="Aprenderé a interpretar o analizar una frase integrando fraseo, ritmo, dinámica, armonía y ejecución, y a evaluar críticamente mi trabajo y el de otras personas con una pauta de cuatro criterios.",
    prior=["Reconozco los rasgos expresivos de una frase.", "Sé justificar una decisión con evidencias.", "Sé que ensayar tiene pausas y cuidado del cuerpo."],
    explain=[
        "Interpretar una frase es integrar todas las decisiones en una sola ejecución: dónde se respira, cómo cambia la fuerza, cómo se mantiene el pulso, qué acorde acompaña y cómo se termina. Una interpretación lograda no es la que tiene más cambios, sino la que mantiene sus decisiones coherentes con el propósito. Cada decisión debe poder explicarse con un compás o un símbolo.",
        "La evaluación crítica de una interpretación usa una pauta: criterios claros y observables. Cada criterio se evalúa con evidencia («en c3 el pulso pasa de 60 a 80») y no con adjetivos vagos. Se evalúa primero el trabajo propio y luego el de otras personas, con un orden respetuoso: describir lo que se oyó, valorar lo que cumple el criterio y sugerir un cambio concreto y posible.",
        "Evaluar no es juzgar a la persona, sino la ejecución. Una buena crítica nombra al menos un logro y una sugerencia, y se centra en el criterio, no en el estudiante. Después de evaluar, se decide qué conservar y qué ajustar para la próxima pasada. Antes de ensayar de nuevo se hace una pausa de silencio para descansar la voz o las manos.",
    ],
    vocab=[("interpretación", "ejecución de una pieza con decisiones propias"), ("pauta", "lista de criterios observables para evaluar"), ("evaluación crítica", "valoración razonada con evidencia, centrada en la ejecución"),
           ("coherencia", "acuerdo entre las decisiones y el propósito"), ("pulso estable", "pulso que se mantiene sin acelerar ni frenar sin intención"), ("sugerencia", "cambio concreto y posible que se propone")],
    worked=[
        ("Evaluar un criterio con evidencia", "En una versión de ejemplo, una frase indicada a 60 pulsos por minuto pasa a 80 desde el compás 3, sin que lo pida la pieza. Evalúa el criterio «pulso estable».",
         ["Se compara lo pedido (60 pulsos por minuto todo el tiempo) con lo ejecutado (80 desde el compás 3).", "El pulso no se mantuvo: no cumple el criterio. Se cita la evidencia y se sugiere practicar con pulso marcado en voz baja."],
         "No cumple: el pulso pasa de 60 a 80 desde el compás 3; sugerencia: practicar con pulso marcado en voz baja"),
        ("Formular una crítica respetuosa", "Un compañero termina la frase con el último sonido alargado sobre el silencio. Formula una crítica con descripción, valoración y sugerencia.",
         ["Descripción: el último sonido se alargó durante el silencio del compás final.", "Valoración y sugerencia: la dinámica final fue cuidada; para un final limpio, cortar el sonido en el pulso 4, antes del silencio."],
         "Alargó el último sonido sobre el silencio; la dinámica final fue cuidada; sugiero cortarlo en el pulso 4"),
    ],
    mistakes=[("Evaluar con adjetivos como «estuvo mal» o «estuvo genial».", "No dicen qué criterio se cumplió ni dónde se oyó.", "Nombra el criterio, cita el compás y propón un cambio concreto."),
              ("Criticar a la persona («eres desafinado») en lugar de la ejecución.", "Se juzga a quien toca y no lo que se oyó.", "Habla de la ejecución («la nota del compás 2 sonó baja») y propón una práctica posible.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una pauta de evaluación?', 'Una lista de criterios observables para evaluar una ejecución', 'Una partitura completa de la pieza que se va a tocar en el ensayo', 'La opinión final del público después de un concierto del grupo', 'La pauta organiza criterios que se pueden comprobar al escuchar la ejecución.'),
        ('abc', '{F} ¿Qué hace Ema en la dinámica de c1-c2?', 'Sube de p a mf con un crescendo', 'Baja de mf a p con un decrescendo', 'Mantiene mf parejo hasta el compás 4', 'La ficha indica crescendo de p a mf en los compases 1 y 2.'),
        ('abc', '{F} ¿Dónde respira Hugo?', 'Tras c1 y tras c3', 'Solo tras c2', 'Tras cada nota de la frase', 'La ficha dice que Hugo respira tras el compás 1 y tras el compás 3.'),
        ('abc', '{F} ¿Qué criterio incumple Hugo al pasar de 60 a 80 pulsos por minuto en c3?', 'El pulso estable', 'El fraseo claro', 'El final limpio', 'Cambiar de 60 a 80 sin que lo pida la pieza rompe el pulso estable.'),
        ('=', '{F} Ema canta 4 compases de 4 pulsos a 60 pulsos por minuto. ¿Cuántos segundos dura su interpretación?', '4*4*60//60', 'A 60 pulsos por minuto cada pulso dura un segundo, y se cuentan los 16 pulsos.', ' s'),
        ('abc', '{F} ¿Qué criterio cumple Ema al cortar el último Sol en el pulso 4?', 'El final limpio', 'El pulso estable', 'La dinámica al servicio del propósito', 'Cortar el sonido antes del silencio deja un final limpio, el criterio 4.'),
        ('abc', '{F} ¿Cómo se evalúa con evidencia el criterio 2 (dinámica) en la interpretación de Hugo?', 'No cumple: todo en mf, sin subida ni reposo, que pide el propósito', 'Cumple: todo en mf se oye seguro y eso siempre da esperanza al oyente', 'No se puede evaluar, porque la dinámica depende solo del gusto de cada oyente', 'El propósito pide subir y terminar en reposo, y un mf parejo no muestra ni lo uno ni lo otro.'),
        ('abc', '{F} ¿Qué sugerencia concreta y posible se le puede dar a Hugo sobre el final?', 'Cortar el último Sol en el pulso 4 y dejar el silencio', 'Cantar el último Sol más fuerte para que impresione', 'No terminar el último compás y pasar a otra pieza', 'La sugerencia debe ser concreta y cumplir el criterio 4: cortar en el pulso 4.'),
        ('=', '{F} Hugo acelera en c3 a 80 pulsos por minuto. ¿Cuántos segundos dura su compás 3 de 4 pulsos?', '4*60//80', 'Se multiplican los 4 pulsos por 60 y se dividen por 80 pulsos por minuto.', ' s'),
        ('abc', 'Para evaluar una ejecución, se escribe: «En c1-c2 no se oyó el crescendo que pide la ficha; sugiero marcar con la mano cuándo sube la fuerza». ¿Qué tiene esta crítica que la hace útil?', 'Cita un dato comprobable y propone un cambio concreto', 'Compara a la persona con otra más experta', 'Opina que la ejecución estuvo bien sin explicar por qué', 'Una crítica útil incluye evidencia comprobable y una sugerencia concreta.'),
        ('abc', '{F} ¿Cuál de las dos interpretaciones es más coherente con el propósito «sube con esperanza y termina en reposo»?', 'La de Ema, porque su dinámica sube y luego baja al reposo', 'La de Hugo, porque su aceleración final da más esperanza al público', 'Las dos igual, porque ambas tienen una respiración entre frases', 'La coherencia se mide con el propósito; la dinámica de Ema sube y baja como pide la pieza.'),
        ('abc', 'Tras la crítica, Hugo dice: «No sirvo para esto». ¿Qué respuesta corresponde a una evaluación respetuosa?', 'Recordarle que se evalúa la ejecución, nombrar un logro y proponer un ajuste', 'Aceptar que no sirve y sugerir que no ensaye más para no perder el tiempo', 'Decirle que todo estuvo perfecto aunque haya errores, para que no se sienta mal', 'Una crítica respetuosa separa persona y ejecución, valora algo y propone un cambio posible.'),
        ('abc', '{F} Un grupo propone que Hugo repita su versión 6 veces seguidas para corregir el pulso. ¿Qué decisión cuida mejor su voz?', 'Hacer pasadas cortas con pausas de silencio entre ellas', 'Cantar 6 pasadas seguidas más fuerte para sentir el pulso', 'Seguir hasta que se acabe la voz para no perder el ritmo', 'Las pasadas cortas con pausas cuidan la voz y permiten corregir con calma.'),
    ],
    ctx=('abc', 'Antes de una presentación en el liceo, tu grupo debe elegir una de las dos interpretaciones de la ficha para repetirla ante el curso. Si quieren transmitir esperanza y reposo, ¿cuál conviene y con qué ajuste?', 'La de Ema, tal como está, y repetir pasadas cortas con pausas', 'La de Hugo, aumentando aún más el tempo del compás 3', 'Ninguna, y elegir una pieza distinta el día de la presentación', 'La interpretación de Ema cumple el propósito; las pasadas cortas y las pausas cuidan la voz.'),
    sc=[
        ("En Interpretación musical: ¿qué es la evaluación crítica de una ejecución?", "Una valoración razonada, con evidencia, centrada en lo que se oyó y no en la persona", "Evalúa la ejecución con criterios y evidencia, no a quien toca."),
        ('abc', 'Una crítica respetuosa sigue este orden:', 'Describir, valorar y sugerir', 'Comparar con otra persona y corregir', 'Opinar y no explicar', 'El orden describir, valorar y sugerir mantiene el foco en la ejecución.'),
        ("¿Qué haces antes de ensayar de nuevo después de evaluar?", "Una pausa de silencio para descansar la voz o las manos", "Cuidar el cuerpo evita la fatiga y permite corregir con calma."),
    ],
    op=("Con la {F}, evalúa la interpretación de Ema o la de Hugo con los cuatro criterios de la pauta: para cada uno escribe «cumple» o «no cumple» y una evidencia. Cierra con una sugerencia concreta y posible.",
        "Interpretación de Hugo: (1) fraseo claro, no cumple: respira tras c1 y tras c3, lo que parte la primera frase y no calza con las frases de dos compases; (2) dinámica, no cumple: todo en mf, no muestra subida ni reposo; (3) pulso estable, no cumple: pasa de 60 a 80 en c3; (4) final limpio, no cumple: alarga el último Sol sobre el silencio. Sugerencia: cortar el último Sol en el pulso 4 y practicar el c3 con pulso marcado.",
        ["evalúa los cuatro criterios", "usa «cumple» o «no cumple» con una evidencia", "da una sugerencia concreta y posible", "habla de la ejecución y no de la persona"],
        ["hoja con la pauta completada y la sugerencia"],
        ["evaluar con adjetivos vagos", "olvidar una evidencia", "criticar a la persona"],
        "Pregunta: «¿qué compás respalda tu valoración?». Si no la respalda, pídele que cite el dato de la ficha."),
    reinforce="Escribe una pauta de dos criterios para evaluar una frase de dos compases y evalúa con ella una interpretación que imagines.",
    extend="Explica por qué dos personas pueden evaluar con la misma pauta una interpretación y llegar a valoraciones algo distintas.",
)
