"""Filosofía 3.º medio FG: OA 03 (preguntas ontológicas sobre el ser y la realidad). Casos y resúmenes de ejemplo inventados y simplificados."""
from __future__ import annotations

from fg_filo_common import build

O3 = "FG-FILO-3M-OAC-03"

# ============================================================ OA 03, clase 1
F = ("Ficha 1 (caso de ejemplo): Rita tiene una bicicleta azul que le regaló su abuela. Con los años la repara: cambia las ruedas, luego la cadena, luego el manubrio, luego el marco, hasta que ya no queda ninguna pieza original. "
     "Rita la sigue llamando «la bicicleta de mi abuela». Su hermano dice: «Eso ya es otra bicicleta».")
build(
    O3, 1, F,
    use="Aprenderé a convertir situaciones cotidianas en preguntas sobre el ser y la realidad (ontología): qué existe, qué permanece cuando algo cambia y qué distingue lo real de lo aparente.",
    prior=["Sé formular preguntas filosóficas y detectar supuestos.", "Sé que la ontología pregunta por lo que existe.", "Sé distinguir una pregunta empírica de una filosófica."],
    explain=[
        "La ontología es la parte de la filosofía que se pregunta por el ser: qué existe, qué tipos de cosas hay y qué significa existir. Un ente es cualquier cosa que existe (una piedra, una persona, una idea, un número). Las preguntas ontológicas suelen surgir de situaciones cotidianas: ¿existe lo que no veo?, ¿qué hace que algo siga siendo la misma cosa aunque cambie?, ¿es real lo que aparece en una pantalla?",
        "La identidad es lo que hace que una cosa sea la misma a lo largo del tiempo. El cambio es que una cosa deje de tener una propiedad y adquiera otra. El caso de la bicicleta de Rita enfrenta ambas ideas: si cambian todas las piezas, ¿sigue siendo la misma bicicleta? Hay varias respuestas razonadas: la misma por continuidad (se fue reparando gradualmente), otra porque ya no queda material original, o depende de qué entendamos por «misma».",
        "Problematizar ontológicamente es pasar del caso a la pregunta general: describir qué ocurre, detectar el supuesto («para que algo siga siendo lo mismo debe conservar sus piezas») y formular la pregunta («¿qué hace que algo siga siendo lo que es?»). Una apariencia es cómo algo se muestra; la realidad, cómo es. Preguntar si coinciden también es una pregunta ontológica.",
    ],
    vocab=[("ontología", "parte de la filosofía que pregunta por el ser y por lo que existe"), ("ente", "cualquier cosa que existe"), ("identidad", "lo que hace que algo sea el mismo a lo largo del tiempo"), ("cambio", "que algo deje de tener una propiedad y adquiera otra"), ("apariencia y realidad", "cómo algo se muestra frente a cómo es")],
    worked=[
        ("Detectar el supuesto", "Frase de ejemplo: «Mi celular nuevo ya es otro porque le cambiaron la pantalla». ¿Qué supuesto hay?", ["Se supone que cambiar una parte importante cambia lo que algo es.", "Eso es discutible: una parte no siempre define el todo."], "Supuesto: cambiar una parte importante vuelve a algo en otra cosa"),
        ("Formular la pregunta ontológica", "Un curso de ejemplo se pregunta si un equipo sigue siendo el mismo cuando cambian todos los jugadores. ¿Qué pregunta general sale?", ["Se trata de identidad en el cambio.", "La pregunta general es qué hace que algo siga siendo lo mismo."], "¿Qué hace que algo siga siendo lo mismo aunque cambie?"),
    ],
    mistakes=[("Responder con un dato en lugar de analizar el concepto de identidad.", "Contar piezas no resuelve qué significa «ser el mismo».", "Aclara qué criterio de identidad usas: piezas, función o historia."),
              ("Creer que hay una sola respuesta correcta obvia.", "Hay varias respuestas razonadas y cada una usa un criterio distinto.", "Presenta al menos dos criterios y sus razones.")],
    T=[
        ('abc', '¿Qué estudia la ontología?', 'Lo que existe y qué significa existir', 'Cómo se justifican las creencias', 'Cuándo una acción es correcta', 'La ontología pregunta por el ser; la epistemología por el conocimiento y la ética por la acción.'),
        ('abc', '{F} ¿Qué pregunta ontológica plantea el caso de Rita?', '¿Qué hace que algo siga siendo la misma cosa aunque cambien todas sus partes?', '¿Cuánto cuesta reparar una bicicleta y cuánto tiempo toma conseguir las piezas nuevas?', '¿Cuántas ruedas, cadenas y manubrios tiene una bicicleta de adulto en promedio?', 'Trata de identidad y cambio; las otras piden datos.'),
        ('abc', '{F} ¿Qué criterio usa el hermano de Rita para decir que es otra bicicleta?', 'Que ya no queda ninguna pieza original', 'Que la bicicleta ahora es de otro color que cuando se la regaló la abuela', 'Que Rita la usa menos que antes y por eso ya no es la misma de la abuela', 'Su razón es que la identidad exige conservar el material original.'),
        ('abc', '{F} ¿Qué criterio podría usar Rita para decir que es la misma?', 'La continuidad: se fue reparando poco a poco y mantuvo su historia', 'Que la bicicleta sigue siendo azul, y el color basta para que siga siendo la misma', 'Que nadie la ha visto cambiar de una vez, porque los cambios fueron pequeños', 'Defiende la identidad por la historia continua de cambios graduales.'),
        ('abc', '¿Qué es un ente?', 'Cualquier cosa que existe', 'Una cosa que se puede tocar', 'Una persona viva', 'Incluye cosas, personas, ideas y números; no solo lo tangible.'),
        ('abc', '¿Qué es la identidad en ontología?', 'Lo que hace que algo sea el mismo a lo largo del tiempo', 'El nombre que alguien le pone a algo', 'El documento que acredita quién es una persona', 'En ontología se refiere a que algo sigue siendo lo mismo, no al carnet.'),
        ('abc', 'Frase de ejemplo: «Un equipo es el mismo mientras conserve sus jugadores». ¿Qué supuesto contiene?', 'Que la identidad de un grupo depende de sus miembros originales', 'Que los equipos nunca cambian de integrantes y por eso conservan siempre su identidad', 'Que los jugadores no existen más allá del nombre del equipo que los reúne', 'Solo así la frase puede afirmar que el equipo cambia al cambiar sus jugadores.'),
        ('abc', 'Un curso de ejemplo discute si una foto en pantalla muestra la realidad. ¿Qué par de ideas está en juego?', 'Apariencia y realidad', 'Norma y valor', 'Premisa y conclusión', 'Se pregunta si lo que se muestra coincide con lo que es.'),
        ('abc', '{F} ¿Por qué no basta contar piezas para resolver el caso de Rita?', 'Porque antes hay que decidir qué significa «ser la misma», es decir, el criterio de identidad', 'Porque contar piezas sirve para una bicicleta, pero no para otros objetos', 'Porque las piezas nuevas siempre son idénticas a las antiguas y no hay nada que contar', 'El conteo aporta un dato, pero la pregunta es conceptual.'),
        ('abc', '{F} Un estudiante responde: «Es la misma porque Rita la quiere». ¿Qué falla?', 'Confunde un sentimiento con un criterio que explique la identidad', 'Aplica el criterio de la continuidad, porque considera la historia de la bicicleta', 'Aplica el criterio de las piezas, porque cuenta cuántas se cambiaron', 'El cariño no explica qué hace que algo siga siendo lo mismo, aunque puede importar para otros asuntos.'),
        ('abc', 'Se quiere problematizar «mi amigo es el mismo de siempre». ¿Qué pregunta ontológica sale?', '¿Qué cambia y qué permanece en una persona con el tiempo?', '¿Cuántos amigos tienes hoy y cuántos tenías cuando eras más pequeño o pequeña?', '¿Dónde vive tu amigo y a qué hora suele salir de su casa cada día?', 'Examina identidad y cambio en una persona.'),
        ('abc', 'Alguien dice: «Si todo cambia, nada es real». ¿Qué supuesto oculta?', 'Que solo es real lo que permanece sin cambiar', 'Que lo que cambia es siempre más real que lo que permanece', 'Que el cambio es una ilusión que solo ocurre en la imaginación', 'Sin ese supuesto, de «todo cambia» no se sigue «nada es real».'),
        ('abc', '{F} ¿Cuál es una respuesta razonada que admite que depende del criterio?', 'Si el criterio es el material, es otra; si es la historia continua, es la misma', 'Es la misma porque sí, y no hace falta dar razones ni elegir criterio alguno', 'No se puede preguntar eso, porque una bicicleta no puede tener identidad propia', 'Reconoce que la respuesta depende del criterio y lo explica.'),
    ],
    ctx=('abc', 'Un club ficticio ha cambiado sus socios y sus colores en veinte años, pero conserva su nombre y su sede. ¿Qué pregunta ontológica plantea?', '¿Qué hace que el club siga siendo el mismo club?', '¿Cuántos socios tiene el club hoy?', '¿Quién paga las cuotas?', 'Trata de identidad en el cambio.'),
    sc=[
        ('abc', '¿Cuál es una pregunta empírica?', '¿Cuántas piezas cambió Rita?', '¿Qué es la identidad?', '¿Es real lo que veo?', 'Se responde contando; las otras son conceptuales.'),
        ('En Filosofía: ¿qué es la identidad?', 'Lo que hace que algo sea el mismo a lo largo del tiempo', 'Es el criterio por el que decimos que una cosa sigue siendo la misma pese al cambio.'),
        ('abc', '¿Qué significa «apariencia»?', 'Cómo algo se muestra', 'Cómo algo es en sí mismo', 'Lo que alguien opina', 'La apariencia es lo que se muestra; la realidad es cómo es.'),
    ],
    op=("Elige un objeto o grupo que cambie con el tiempo (por ejemplo, un curso, una banda de música ficticia, un libro reparado). Escribe: (1) el caso en dos líneas; (2) un supuesto; (3) una pregunta ontológica general; (4) dos criterios de identidad posibles y qué respondería cada uno.",
        "(1) Una banda cambia a todos sus integrantes. (2) La banda es la misma si tiene los mismos integrantes. (3) ¿Qué hace que un grupo siga siendo el mismo? (4) Criterio de miembros: es otra. Criterio de historia y nombre: es la misma.",
        ["describe el caso", "detecta un supuesto real", "da dos criterios distintos"], ["cuatro frases"], ["responder con un dato", "no distinguir criterios"],
        "Pide que invente un tercer criterio y diga qué respuesta daría."),
    reinforce="Escribe una pregunta ontológica sobre algo que cambie a tu alrededor y explica qué supuesto la sostiene.",
    extend="Busca en tu vida un ejemplo donde algo «sigue siendo lo mismo» aunque haya cambiado mucho.",
)

# ============================================================ OA 03, clase 2
F = ("Ficha 2 (casos de ejemplo): una manzana es roja hoy y verde ayer. Un árbol pierde las hojas en otoño y sigue siendo el mismo árbol. Un compás de música no se puede tocar con las manos, pero se puede escuchar. El número 7 no se puede ver ni tocar y se usa para calcular.")
build(
    O3, 2, F,
    use="Aprenderé a definir y usar conceptos ontológicos básicos: ser, existencia, esencia, accidente, propiedad, sustancia y realidad, con ejemplos y contraejemplos.",
    prior=["Sé qué es un ente y qué es la identidad.", "Sé definir un concepto y probarlo con contraejemplos.", "Sé distinguir apariencia y realidad."],
    explain=[
        "La existencia es el hecho de que algo sea, esté ahí; no es lo mismo que ser material (una idea o un número pueden existir de modos distintos al de una piedra). Una propiedad es un rasgo que tiene una cosa, como el color o el tamaño. Una esencia es aquello sin lo cual algo dejaría de ser lo que es; un accidente es un rasgo que puede cambiar sin que la cosa deje de ser lo que es. Por ejemplo, el color de una manzana es accidental; que sea una fruta, quizá esencial.",
        "Esa distinción es discutible: no todas las teorías aceptan que haya esencias. Algunas dicen que lo que llamamos esencia es solo una forma útil de clasificar. Una sustancia, en un sentido tradicional, es lo que existe por sí mismo y sostiene sus propiedades (el árbol que tiene hojas, ramas y color). Esto es una definición usada en la tradición, no un dato comprobado.",
        "La realidad es el conjunto de lo que existe. Una pregunta ontológica clave es qué tipos de cosas pertenecen a ella: ¿solo lo material, o también lo mental y lo abstracto, como los números? Al definir conceptos ontológicos conviene dar un ejemplo, un contraejemplo y señalar si la definición es polémica.",
    ],
    vocab=[("existencia", "hecho de que algo sea o esté ahí"), ("propiedad", "rasgo que tiene una cosa, como color o tamaño"), ("esencia", "aquello sin lo cual algo dejaría de ser lo que es"), ("accidente", "rasgo que puede cambiar sin que la cosa deje de ser lo que es"), ("sustancia", "en sentido tradicional, lo que existe por sí mismo y sostiene sus propiedades")],
    worked=[
        ("Distinguir esencia y accidente", "Caso de ejemplo: una pelota de fútbol se desinfla y se mancha de barro. ¿Qué es accidental?", ["Estar desinflada y manchada son rasgos que pueden cambiar.", "Sigue siendo una pelota."], "Estar manchada o desinflada es accidental"),
        ("Probar una definición", "Definición de ejemplo: «Existir es poder tocarse». ¿Qué contraejemplo la muestra demasiado estrecha?", ["Un número o una idea no se tocan.", "Y para algunos existen de algún modo."], "Los números o las ideas, que no se tocan y quizá existen"),
    ],
    mistakes=[("Creer que existir es lo mismo que ser material.", "Hay teorías que admiten que las ideas o los números existen de otro modo.", "Aclara qué tipo de existencia estás definiendo."),
              ("Dar por seguro qué es esencial en una cosa.", "La distinción es discutible y depende de la teoría.", "Presenta el criterio con el que decides y señala que es una postura.")],
    T=[
        ('abc', '¿Qué es una propiedad?', 'Un rasgo que tiene una cosa, como color o tamaño', 'La dueña de un objeto, que es quien decide qué rasgos tendrá y cuáles perderá', 'La causa de que algo exista, es decir, lo que lo produjo en un comienzo', 'Una propiedad es un rasgo; no se refiere a quien posee la cosa.'),
        ('abc', '{F} ¿Qué rasgo de la manzana es accidental?', 'Su color, que puede cambiar sin que deje de ser manzana', 'Ser una fruta, que es lo que la manzana comparte con otras frutas de su tipo', 'Existir, que es lo que la manzana comparte con cualquier cosa que exista', 'El color cambia y la manzana sigue siendo manzana.'),
        ('abc', '{F} ¿Qué cambio del árbol es accidental?', 'Perder las hojas en otoño', 'Dejar de ser un árbol', 'Dejar de existir', 'Seguir siendo el mismo árbol indica que el cambio no afecta lo que es.'),
        ('abc', '¿Qué es una esencia, según la definición de la clase?', 'Aquello sin lo cual algo dejaría de ser lo que es', 'Un rasgo que cambia todos los días', 'Una opinión sobre la cosa', 'La esencia es lo que no puede faltar sin que la cosa deje de ser lo que es.'),
        ('abc', '¿Por qué la distinción entre esencia y accidente es discutible?', 'Porque algunas teorías sostienen que las esencias son solo una forma útil de clasificar', 'Porque nadie puede ver los accidentes y entonces no se pueden distinguir de lo esencial', 'Porque solo vale para los números y no para los objetos que podemos tocar', 'No todas las teorías aceptan que existan esencias reales.'),
        ('abc', '{F} El compás de música, ¿qué muestra sobre la existencia?', 'Que algo puede existir sin poder tocarse', 'Que todo lo que existe se puede tocar', 'Que la música no existe', 'La existencia no se limita a lo táctil, según la ficha.'),
        ('abc', '{F} El número 7, ¿qué pregunta ontológica plantea?', 'Si lo que no se ve ni se toca existe y de qué modo', 'Cuántos números hay en total y si se pueden contar hasta llegar al último de ellos', 'Si el 7 es un número par o impar, cosa que se resuelve calculando', 'Pregunta qué tipos de cosas pertenecen a la realidad.'),
        ('abc', '¿Qué es una sustancia en el sentido tradicional?', 'Lo que existe por sí mismo y sostiene sus propiedades', 'Un líquido que se mezcla con agua', 'Una propiedad que cambia con el tiempo', 'En ese sentido es el soporte de propiedades; no se refiere a química.'),
        ('abc', 'Definición de ejemplo: «Existir es poder verse». ¿Qué caso la muestra demasiado estrecha?', 'El aire, que no se ve y existe', 'Una nube densa en el cielo, que se ve y existe', 'Una montaña visible desde lejos, que se ve y existe', 'Algo que existe pero no se ve es contraejemplo de estrechez.'),
        ('abc', 'Un estudiante dice: «Lo que no es material no existe». ¿Qué respuesta es más justa?', 'Es una tesis que algunas posturas defienden y otras discuten; hay que dar razones', 'Es un hecho comprobado por todos, de modo que no hace falta discutirlo ni dar razones', 'Es una frase sin sentido, porque nada puede existir sin ser material o tocable', 'Es una postura ontológica, no un dato.'),
        ('abc', '{F} ¿Qué rasgo del árbol podría considerarse esencial?', 'Ser un árbol, un ser vivo con tronco', 'Tener hoy el mismo número de hojas', 'Estar mojado por la lluvia', 'Es lo que, según el criterio, no puede faltar sin que deje de ser árbol.'),
        ('abc', '¿Qué conviene hacer al definir un concepto ontológico?', 'Dar ejemplo, contraejemplo y señalar si la definición es polémica', 'Elegir la definición más corta, porque lo breve es siempre más claro que lo explicado', 'Usar la misma palabra para definirla, así queda claro de qué concepto se habla', 'Se prueba y se reconoce su carácter discutible.'),
        ('abc', 'Alguien afirma: «Por definición, las esencias existen y no hace falta discutirlo». ¿Qué falla?', 'Presenta una postura discutible como si fuera un dato incuestionable', 'Da una razón que prueba que las esencias existen, porque cita un ejemplo', 'Da un contraejemplo que muestra que la definición falla en algún caso concreto', 'Las esencias son objeto de debate; no son un hecho cerrado.'),
    ],
    ctx=('abc', 'Un taller de ejemplo cambia el color de una mesa de madera de café a blanco. ¿Qué es accidental y qué podría ser esencial, según el criterio de la clase?', 'El color es accidental; ser una mesa para apoyar cosas podría ser esencial', 'Ambos son accidentes', 'Ninguno puede cambiar', 'Usa el criterio: lo accidental cambia sin que la cosa deje de ser lo que es.'),
    sc=[
        ('abc', '¿Qué es un accidente en ontología?', 'Un rasgo que puede cambiar sin que la cosa deje de ser lo que es', 'Un choque entre dos objetos que deja algún daño visible en uno de los dos', 'Lo que daña a una cosa y la hace dejar de ser lo que era antes', 'No se refiere a un percance sino a un rasgo cambiable.'),
        ('En Filosofía: ¿qué es la existencia?', 'El hecho de que algo sea o esté ahí', 'Es que algo sea, sin presuponer que sea material.'),
        ('abc', '¿Qué hace un contraejemplo?', 'Muestra que una definición falla en un caso', 'Confirma siempre una definición, porque muestra que se cumple en todos los casos', 'Repite la definición con otras palabras para que se entienda mejor la idea', 'Sirve para refutar o limitar una definición.'),
    ],
    op=("Elige tres objetos o ideas de la {F} (por ejemplo, la manzana, el árbol y el número 7) y para cada uno escribe: una propiedad, un accidente, algo que podría ser esencial y una pregunta ontológica. Señala cuál de tus respuestas es más discutible.",
        "Manzana: propiedad, color; accidente, estar roja o verde; esencial, ser fruta; pregunta, ¿qué la hace manzana? Árbol: propiedad, hojas; accidente, perderlas; esencial, ser un ser vivo con tronco. Número 7: propiedad, ser impar; pregunta, ¿existe sin que lo veamos? Lo más discutible: qué es esencial.",
        ["distingue propiedad, accidente y esencia", "formula preguntas ontológicas", "reconoce lo discutible"], ["tabla de tres objetos"], ["afirmar esencias como hechos", "confundir color con esencia"],
        "Pide que explique qué criterio usó para decidir qué es esencial."),
    reinforce="Define con tus palabras «accidente» y «esencia» y da un ejemplo de cada uno.",
    extend="Busca un objeto cuyo uso cambie con el tiempo y discute qué sería esencial en él.",
)

# ============================================================ OA 03, clase 3
F = ("Ficha 3 (resúmenes de ejemplo, muy simplificados). Perspectiva materialista: lo real es lo material; la mente depende del cuerpo, en particular del cerebro, y se explica por procesos físicos. "
     "Perspectiva dualista: existen dos tipos de realidad distintos, lo material y lo mental; la mente no se reduce a procesos físicos. "
     "Caso de ejemplo: Sofía se pregunta si sus pensamientos son solo actividad del cerebro o algo más.")
build(
    O3, 3, F,
    use="Aprenderé a reconstruir dos teorías ontológicas sobre la mente y la materia (materialismo y dualismo) con su tesis, razones y objeciones.",
    prior=["Sé reconstruir una perspectiva con tesis, razones y supuestos.", "Sé qué son esencia, accidente y existencia.", "Sé qué es una objeción."],
    explain=[
        "Una teoría ontológica propone qué tipos de cosas existen. El materialismo sostiene que todo lo real es material; la mente se explica por procesos físicos. El dualismo sostiene que existen dos tipos de realidad, lo material y lo mental, que no se reducen una a la otra. Ambos son resúmenes muy simples de familias de posturas: dentro de cada una hay versiones distintas.",
        "Para reconstruir cada teoría se identifican su tesis, sus razones y su principal objeción. Una razón del materialismo es que cuando el cerebro se altera cambian los pensamientos. Una razón del dualismo es que la experiencia subjetiva (lo que se siente al ver un color o sentir alegría) parece distinta de describir células. Las objeciones: al materialismo se le pide explicar la experiencia subjetiva; al dualismo, explicar cómo interactúan lo material y lo mental.",
        "Reconstruir con rigor es mostrar cada teoría en su mejor versión (principio de caridad), sin decidir todavía cuál es verdadera. Importa también la relación con la vida: según qué teoría se acepte, cambian ideas sobre responsabilidad, tratamientos médicos o sobre qué entendemos por «yo». Si una pregunta sobre tu propia salud mental te angustia, conviene hablar con una persona adulta de confianza.",
    ],
    vocab=[("materialismo", "teoría según la cual todo lo real es material"), ("dualismo", "teoría según la cual existen dos tipos de realidad: lo material y lo mental"), ("experiencia subjetiva", "lo que se siente en primera persona, como ver un color"), ("reducir", "explicar algo como si fuera solo otra cosa más básica"), ("interacción", "influencia mutua entre dos cosas")],
    worked=[
        ("Tesis y razón", "Resumen de ejemplo: «La mente es solo actividad del cerebro, pues si se daña una zona cambian ciertas capacidades». ¿Cuál es la tesis y cuál la razón?", ["Tesis: la mente es actividad del cerebro.", "Razón: el daño cerebral cambia capacidades."], "Tesis: mente = actividad cerebral; razón: el daño cambia capacidades"),
        ("Formular la objeción", "Al dualismo se le pregunta: «¿cómo puede algo no material mover un brazo?». ¿Qué objeción es?", ["Cuestiona la interacción.", "Pide explicar cómo se influyen lo mental y lo material."], "Problema de la interacción"),
    ],
    mistakes=[("Presentar una teoría solo con sus defectos.", "No se aplica el principio de caridad y se cae en el hombre de paja.", "Expón primero su mejor versión y sus razones."),
              ("Creer que una teoría ontológica se prueba con un solo dato.", "Cada teoría interpreta los datos de modo distinto.", "Pregunta cómo explicaría cada una el mismo dato.")],
    T=[
        ('abc', '{F} ¿Cuál es la tesis del materialismo?', 'Que todo lo real es material y la mente depende de procesos físicos', 'Que la mente es una realidad completamente independiente del cuerpo', 'Que existen dos tipos de realidad que no se reducen una a la otra', 'Es la afirmación central que da el resumen.'),
        ('abc', '{F} ¿Cuál es la tesis del dualismo?', 'Que existen dos tipos de realidad, lo material y lo mental, que no se reducen una a la otra', 'Que solo existen cosas materiales y todo lo mental se explica por procesos físicos', 'Que la mente es una ilusión y por eso no pertenece a ningún tipo de realidad', 'El dualismo admite dos tipos de realidad.'),
        ('abc', '{F} ¿Qué razón puede dar el materialismo?', 'Que si se altera el cerebro cambian los pensamientos', 'Que nadie siente emociones, porque todo lo que se siente es solo una invención del lenguaje', 'Que los cerebros no existen y por eso la mente tiene que explicarse de otro modo', 'La razón conecta el cambio mental con cambios cerebrales.'),
        ('abc', '{F} ¿Qué razón puede dar el dualismo?', 'Que sentir algo en primera persona parece distinto de describir procesos físicos', 'Que el cerebro nunca se altera, y por eso los pensamientos no dependen de él', 'Que los pensamientos son visibles al microscopio como cualquier otra parte del cuerpo', 'La razón apunta a la experiencia subjetiva.'),
        ('abc', '{F} ¿Qué objeción se le hace al materialismo?', 'Que debe explicar cómo la actividad física produce la experiencia subjetiva', 'Que acepta demasiados tipos de realidad y no sabe cómo ordenarlos entre sí', 'Que no habla del cerebro ni de ningún proceso físico cuando explica la mente', 'Es la objeción clásica sobre la experiencia en primera persona.'),
        ('abc', '{F} ¿Qué objeción se le hace al dualismo?', 'Que debe explicar cómo interactúan lo mental y lo material', 'Que niega que exista la experiencia subjetiva y la reemplaza por una simple opinión', 'Que dice que todo es material y no necesita explicar cómo se experimenta algo', 'Si son realidades distintas, cabe preguntar cómo se influyen.'),
        ('abc', 'Reconstruir una teoría en su mejor versión se llama aplicar', 'El principio de caridad', 'La falacia genética', 'La ambigüedad', 'Es interpretar la postura en su versión más razonable.'),
        ('abc', '{F} Una compañera dice: «Los materialistas creen que la gente no siente nada». ¿Qué falla?', 'Deforma la tesis: afirman que lo que se siente se explica por procesos físicos, no que no exista', 'Aplica el principio de caridad, porque presenta la tesis en su versión más razonable', 'Da una razón para la tesis, porque explica por qué el materialismo es correcto', 'Eso es un hombre de paja: se exagera la postura para atacarla.'),
        ('abc', '{F} Si un dato muestra que un medicamento cambia el ánimo, ¿cómo lo interpretaría un materialista?', 'Como una muestra de que lo mental depende de procesos físicos', 'Como una prueba de que la mente no existe', 'Como un dato sin relación con el cerebro', 'Para esa teoría, cambiar procesos físicos cambia lo mental.'),
        ('abc', '{F} ¿Cómo podría un dualista interpretar el mismo dato?', 'Como una interacción entre lo material y lo mental, sin que lo mental se reduzca a lo material', 'Como una prueba de que la mente no existe y que todo se reduce a un medicamento', 'Como un hecho irrelevante para la salud, que no dice nada sobre mente y cuerpo', 'Reconoce la influencia mutua sin reducir una cosa a la otra.'),
        ('abc', '{F} ¿Se puede decidir cuál teoría es verdadera solo con ese dato?', 'No: ambas teorías pueden interpretarlo, hace falta evaluar sus razones completas', 'Sí, el dato prueba el materialismo, porque muestra que lo mental depende del cerebro por completo', 'Sí, el dato prueba el dualismo, porque muestra que lo mental existe aparte del cuerpo', 'Los datos se interpretan desde una teoría; con uno no basta para decidir.'),
        ('abc', 'Según la clase, ¿por qué esta discusión importa para la vida?', 'Porque cambia ideas sobre responsabilidad, tratamientos y sobre qué entendemos por «yo»', 'Porque decide qué ropa usar y qué comida conviene comer cada día de la semana', 'Porque no tiene ninguna consecuencia en la vida real, ya que son ideas abstractas', 'La postura ontológica influye en decisiones y en cómo nos entendemos.'),
        ('abc', '{F} Sofía se angustia al pensar en estas preguntas y no logra dormir por varios días. ¿Qué conviene?', 'Contárselo a una persona adulta de confianza', 'Guardárselo para no preocupar a nadie', 'Dejar de pensar para siempre en cualquier pregunta', 'Una angustia que afecta el sueño merece apoyo de un adulto de confianza.'),
    ],
    ctx=('abc', 'Un estudiante de ejemplo afirma: «Si cada pensamiento es actividad cerebral, entonces nadie es responsable de nada». ¿Qué conviene preguntar?', 'Si de esa tesis ontológica se sigue necesariamente esa conclusión sobre la responsabilidad', 'Si ese estudiante cursó filosofía antes de opinar', 'Si la mayoría del curso está de acuerdo con él', 'Examina la inferencia de la ontología a la responsabilidad.'),
    sc=[
        ('abc', '¿Qué es el dualismo?', 'La teoría de que existen dos tipos de realidad: lo material y lo mental', 'La teoría de que todo es material', 'La teoría de que lo mental no existe', 'El dualismo admite dos tipos de realidad.'),
        ('En Filosofía: ¿qué es la experiencia subjetiva?', 'Lo que se siente en primera persona, como ver un color', 'Es lo que una persona vive desde su propia perspectiva, difícil de reducir a una descripción externa.'),
        ('abc', '¿Qué es reducir una cosa a otra?', 'Explicarla como si fuera solo otra cosa más básica', 'Hacerla más pequeña para que ocupe menos espacio y sea más fácil de entender', 'Negar que exista, porque se la considera una forma disfrazada de otra cosa', 'Aquí significa explicarla por otra más básica.'),
    ],
    op=("Con la {F}, reconstruye en una tabla las dos teorías: tesis, una razón, una objeción y una consecuencia práctica de cada una. Cierra con una pregunta para seguir investigando que no tome partido.",
        "Materialismo: tesis, todo lo real es material; razón, el daño cerebral cambia pensamientos; objeción, explicar la experiencia subjetiva; consecuencia, buscar explicaciones físicas. Dualismo: tesis, dos tipos de realidad; razón, la experiencia en primera persona; objeción, la interacción; consecuencia, no reducir lo mental a lo físico. Pregunta: ¿qué evidencia podría ayudar a decidir?",
        ["describe cada teoría con fidelidad", "una razón y una objeción por teoría", "pregunta final abierta"], ["tabla de dos columnas"], ["deformar una teoría", "tomar partido sin razones"],
        "Pide que cambie una objeción por la de la otra teoría y vea si sigue valiendo."),
    reinforce="Explica con tus palabras la diferencia entre materialismo y dualismo con un ejemplo cotidiano.",
    extend="Busca una frase de tu vida donde se asuma que lo mental y lo físico están relacionados.",
)

# ============================================================ OA 03, clase 4
F = ("Ficha 4 (argumentos de ejemplo). Argumento de Bruno: «Algo es real si produce efectos. Los sueños producen efectos: a veces nos despiertan angustiados. Por lo tanto, los sueños son reales». "
     "Objeción de Camila: «Una ilusión óptica también produce efectos: nos hace ver una línea más larga. ¿Entonces la ilusión es real tal como se ve?».")
build(
    O3, 4, F,
    use="Aprenderé a formular y evaluar argumentos sobre qué es real, distinguiendo entre que algo exista y que sea tal como parece.",
    prior=["Sé reconstruir teorías ontológicas.", "Sé distinguir apariencia y realidad.", "Sé detectar premisas ocultas y ambigüedades."],
    explain=[
        "Un criterio de realidad es una regla para decidir qué cuenta como real. El argumento de Bruno usa un criterio: «algo es real si produce efectos». Ese criterio tiene fuerza (lo que no produce efecto alguno es difícil de distinguir de lo que no existe) pero también problemas. Para evaluar un criterio se buscan casos que lo cumplen y no parecen reales, o al revés.",
        "La objeción de Camila muestra una ambigüedad: «ser real» puede significar que existe como experiencia (la ilusión se experimenta) o que es tal como aparece (la línea realmente es más larga). Distinguir ambos sentidos permite una respuesta más precisa: la ilusión existe como experiencia, pero su apariencia no coincide con la realidad del objeto.",
        "Evaluar un argumento ontológico implica revisar si las premisas son aceptables, si la conclusión se sigue y si el criterio de realidad es adecuado. También se puede reformular la conclusión para hacerla más precisa: no «los sueños son reales», sino «los sueños existen como experiencias con efectos reales».",
    ],
    vocab=[("criterio de realidad", "regla para decidir qué cuenta como real"), ("ilusión", "experiencia en que algo aparece distinto de como es"), ("efecto", "cambio que una cosa produce en otra"), ("precisar", "reformular una afirmación para que sea más exacta"), ("sentido de una palabra", "uno de los significados que puede tener un término")],
    worked=[
        ("Aplicar un criterio", "Criterio de ejemplo: «Es real lo que se puede medir». ¿Cumple el calor de una sala?", ["El calor se mide con termómetros.", "Según el criterio, es real."], "Sí, cumple el criterio"),
        ("Buscar un contraejemplo al criterio", "El mismo criterio: «Es real lo que se puede medir». ¿Qué caso podría ser un contraejemplo?", ["Algo que existe pero aún no se sabe medir.", "Por ejemplo, un sentimiento que no se mide con instrumentos."], "Un sentimiento que existe y no se mide"),
    ],
    mistakes=[("Aceptar un criterio de realidad sin buscar contraejemplos.", "Un criterio puede dejar fuera cosas reales o incluir cosas que no lo son.", "Prueba el criterio con casos distintos."),
              ("Usar «real» con dos sentidos en el mismo argumento.", "Se pasa de «existe como experiencia» a «es tal como aparece» sin avisar.", "Define cada sentido y úsalo con coherencia.")],
    T=[
        ('abc', '{F} ¿Cuál es la conclusión del argumento de Bruno?', 'Los sueños son reales', 'Los sueños angustian a todos', 'Todo lo que produce efectos es un sueño', 'Es lo que las premisas buscan sostener.'),
        ('abc', '{F} ¿Qué criterio de realidad usa Bruno?', 'Algo es real si produce efectos', 'Algo es real si se puede ver', 'Algo es real si todos lo creen', 'La primera premisa expone el criterio.'),
        ('abc', '{F} ¿Qué objeción presenta Camila?', 'Que el criterio también haría real a una ilusión tal como se ve', 'Que los sueños no existen y que por eso no pueden tener efectos reales en nadie', 'Que el criterio de Bruno es demasiado estrecho y deja fuera cosas reales', 'Camila muestra una consecuencia problemática del criterio.'),
        ('abc', '{F} ¿Qué ambigüedad hay en «real» en esta discusión?', 'Puede significar existir como experiencia o ser tal como aparece', 'Puede significar existir o ser importante, según lo que opine cada persona', 'Solo significa «material», es decir, algo que se puede tocar y medir con instrumentos', 'La ilusión existe como experiencia pero no es como aparece.'),
        ('abc', '{F} ¿Cómo se puede precisar la conclusión de Bruno para evitar la objeción?', 'Los sueños existen como experiencias que tienen efectos reales', 'Los sueños son tan reales como una piedra', 'Los sueños no existen', 'Limita el sentido de «real» a la existencia como experiencia.'),
        ('abc', '{F} ¿Por qué el ejemplo de la ilusión óptica es un buen contraejemplo?', 'Porque cumple el criterio (produce efectos) y no es real tal como aparece', 'Porque no produce ningún efecto y, aun así, sigue siendo considerada real por todos', 'Porque nadie la ve y por eso no puede servir de ejemplo en una discusión', 'Muestra que el criterio incluye casos problemáticos.'),
        ('abc', 'Criterio de ejemplo: «Es real lo que ven todos». ¿Qué caso lo pone en problemas?', 'Algo que existe y casi nadie ve, como un microorganismo', 'Una montaña muy visible, que todos ven y por eso cumple perfectamente el criterio', 'Una persona famosa, a quien todos ven en la televisión y por eso confirma el criterio', 'Algo real que no ven todos es contraejemplo.'),
        ('abc', 'Criterio de ejemplo: «Es real lo que se puede medir». ¿Qué problema puede tener?', 'Podría dejar fuera cosas que existen, pero que aún no sabemos medir', 'No deja fuera nada nunca, por lo que el criterio es perfecto para cualquier caso', 'Solo sirve para el calor y la temperatura, y no para otras cosas', 'Un criterio puede ser demasiado estrecho.'),
        ('abc', '{F} Una estudiante dice: «Bruno siempre discute por discutir». ¿Qué falla?', 'Ataca a la persona y no al argumento', 'Examina una premisa', 'Señala una ambigüedad', 'No responde a las razones del argumento.'),
        ('abc', '{F} Si se acepta el criterio «real es lo que produce efectos», ¿qué debe aceptarse?', 'Que muchas cosas no materiales, como las emociones, serían reales', 'Que nada es real, porque el criterio incluye tanto lo que existe como lo que no', 'Que solo los objetos tocables son reales, aunque el criterio hable de efectos', 'El criterio incluye todo lo que produce efectos.'),
        ('abc', 'Para evaluar un criterio de realidad, ¿qué estrategia sirve?', 'Buscar casos que lo cumplan pero no parezcan reales, o al revés', 'Repetirlo con más fuerza, hasta que todos los participantes lo acepten sin objetar', 'Preguntar quién lo inventó, para decidir si merece confianza por su autor', 'Los contraejemplos ponen a prueba el criterio.'),
        ('abc', '{F} ¿Qué premisa oculta necesita el argumento de Bruno?', 'Que angustiar a alguien es un efecto', 'Que todos tienen sueños todas las noches', 'Que Camila está equivocada', 'Para pasar de «despiertan angustiados» a «producen efectos» se necesita eso.'),
        ('abc', '{F} ¿Es suficiente la respuesta «la ilusión es real, fin de la discusión»?', 'No: falta distinguir en qué sentido se la llama real', 'Sí, porque Camila está equivocada', 'Sí, porque Bruno es mayor', 'La respuesta ignora la ambigüedad señalada.'),
    ],
    ctx=('abc', 'Una joven de ejemplo dice: «Mi amistad en un juego en línea es real porque me ayuda cuando estoy mal». ¿Qué criterio usa?', 'Algo es real si produce efectos importantes en la vida', 'Algo es real si se puede tocar', 'Algo es real si dura mucho', 'Su razón es el efecto que tiene la amistad en su vida.'),
    sc=[
        ('abc', '¿Qué es un criterio de realidad?', 'Una regla para decidir qué cuenta como real', 'Una lista de objetos que se pueden contar o tocar en el lugar donde uno vive', 'Un dato medido por un instrumento, que indica cuánto de algo hay en una cosa', 'Es una regla que sirve para decidir qué cuenta como real.'),
        ('En Filosofía: ¿qué es una ilusión?', 'Una experiencia en que algo aparece distinto de como es', 'Es la diferencia entre cómo se muestra algo y cómo es realmente.'),
        ('abc', '¿Qué se hace al precisar una conclusión?', 'Se reformula para que sea más exacta', 'Se cambia por una opinión', 'Se elimina', 'Precisar una conclusión reduce ambigüedades y la hace más exacta.'),
    ],
    op=("Formula un argumento breve sobre si algo cotidiano es real (por ejemplo, una amistad en línea, una canción o un sueño, que son casos de ejemplo). Incluye: (1) criterio de realidad; (2) premisa; (3) conclusión; (4) un contraejemplo al criterio; (5) una conclusión precisada.",
        "(1) Es real lo que produce efectos. (2) Una canción hace cambiar el ánimo. (3) La canción es real. (4) Un recuerdo falso también produce efectos. (5) La canción existe como experiencia y como sonido, con efectos reales.",
        ["criterio claro", "contraejemplo pertinente", "conclusión precisada"], ["argumento de cinco partes"], ["no probar el criterio", "usar «real» con dos sentidos"],
        "Pide que cambie el criterio y vea si el contraejemplo sigue valiendo."),
    reinforce="Escribe un criterio de realidad y busca un caso que lo ponga en problemas.",
    extend="Observa cómo se usa la palabra «real» en conversaciones cotidianas y anota sus distintos sentidos.",
)
