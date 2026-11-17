"""Interpretación y creación en teatro 3.º y 4.º medio HC: OAC-05 (análisis estético de obras de distintas épocas y procedencias, clases 1 a 5) y OAC-06 (juicios estéticos argumentados, clases 1 a 5). Obras, compañías y textos inventados; sin video real."""
from __future__ import annotations

from hc_icte_common import build

O5 = "AR-ICTE-3y4-OAC-05"
O6 = "AR-ICTE-3y4-OAC-06"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). «El juicio del río», de una compañía ficticia, para espacio abierto y sin luz eléctrica: función de día, un coro de seis intérpretes con máscaras de cartón, un actor que representa al río y una jueza. "
     "Observaciones de un grupo de estudiantes: "
     "O1: el coro habla al unísono y avanza en bloque. "
     "O2: el coro repite frases porque quiere mostrar que el pueblo habla con una sola voz. "
     "O3: las máscaras no dejan ver los gestos del rostro. "
     "O4: la obra es la mejor que se ha hecho sobre el agua. "
     "O5: el espacio abierto ayuda a que se oiga el viento, lo que refuerza la idea de un río vivo. "
     "O6: la jueza se ubica sobre una tarima baja y el coro la rodea.")
build(
    O5, 1, F,
    use="Aprenderé un método para analizar una obra teatral en tres pasos (describir, analizar, interpretar), a distinguir cuatro niveles de análisis (dramaturgia, actuación, puesta en escena y contexto) y a respaldar cada afirmación con evidencia.",
    prior=["Distingo lo observable de lo interpretado.", "Conozco los recursos del lenguaje teatral.", "Sé que una obra se evalúa por sus decisiones y no por los cuerpos."],
    explain=[
        "Analizar estéticamente una obra es estudiar cómo sus decisiones producen sentido y efecto. Se hace en tres pasos. Describir es registrar lo que se ve y se oye, sin valorar: «el coro habla al unísono». Analizar es relacionar un rasgo con otros y con su función: «el unísono y el avance en bloque dan la idea de un grupo que actúa como una sola persona». Interpretar es proponer un sentido posible de la obra, rotulado como posible y apoyado en lo analizado. Una valoración, como «es la mejor obra», es un cuarto paso distinto, y requiere argumentos.",
        "Para no perderse se revisan cuatro niveles. La dramaturgia es el texto y su estructura: conflicto, personajes, tema y lenguaje. La actuación es la interpretación: voz, cuerpo, ritmo, relación entre intérpretes. La puesta en escena reúne espacio, luz, sonido, vestuario y objetos. El contexto es el tiempo, el lugar y las condiciones en que se creó y se presenta la obra. Los cuatro niveles se mezclan en la obra, pero se miran por separado para no confundir sus efectos.",
        "Toda afirmación se apoya en evidencia observable de la obra o en un dato de contexto confiable. Cuando no se vio la obra completa, se dice. El análisis habla de las decisiones de la obra, no de los cuerpos de las personas ni de su vida privada. Si la obra trata un tema doloroso, se analiza con sobriedad y se puede detener la conversación si alguien se incomoda.",
    ],
    vocab=[("describir", "registrar lo que se ve y se oye sin valorar"), ("analizar", "relacionar un rasgo con otros y con su función"), ("interpretar", "proponer un sentido posible apoyado en el análisis"), ("dramaturgia", "texto de la obra y su estructura"), ("evidencia", "dato observable de la obra o del contexto que respalda una afirmación"), ("nivel de análisis", "ámbito de la obra que se examina: dramaturgia, actuación, puesta en escena o contexto")],
    worked=[
        ("Clasificar una frase", "«El actor baja la voz al decir la última frase». ¿Descripción, análisis o interpretación?", ["Registra lo que se oye, sin relacionarlo ni valorarlo.", "Es una descripción."], "Descripción"),
        ("Del dato al análisis", "Dato: «las luces bajan a casi nada mientras la pareja discute». Escribe un análisis.", ["Relaciono el rasgo con su función.", "«La luz tenue concentra la atención en la voz y crea un ambiente de tensión»."], "La luz tenue concentra la atención en la voz y crea tensión"),
    ],
    mistakes=[("Escribir «es hermosa» o «me aburrió» como si fuera análisis.", "Son valoraciones sin evidencia y no dicen nada de las decisiones de la obra.", "Describe el rasgo y explica su efecto."),
              ("Dar una interpretación como si fuera un hecho.", "Una obra permite varias lecturas posibles y la interpretación debe rotularse así.", "Usa «podría» o «sugiere» y apóyate en rasgos.")],
    T=[
        ('abc', 'En análisis teatral, ¿qué es describir?', 'Registrar lo que se ve y se oye sin valorar', 'Explicar por qué una obra es mejor que otra', 'Contar el sentido oculto de la obra', 'Describir se limita a lo observable.'),
        ('abc', '{F} ¿Qué observación es una descripción?', 'O1, el coro habla al unísono y avanza en bloque', 'O2, el coro repite para mostrar que el pueblo habla con una voz', 'O4, es la mejor obra que se ha hecho sobre el agua', 'O1 solo registra lo que ocurre; O2 es interpretación y O4, valoración.'),
        ('abc', '{F} ¿Qué observación es una interpretación?', 'O2, el coro repite porque quiere mostrar que el pueblo habla con una sola voz', 'O3, las máscaras de cartón no dejan ver los gestos del rostro de quienes actúan', 'O6, la jueza se ubica sobre una tarima baja y el coro la rodea en un círculo', 'O2 propone un sentido de la repetición; las otras registran rasgos.'),
        ('abc', '{F} ¿Qué observación es una valoración sin argumentos?', 'O4, la obra es la mejor que se ha hecho sobre el agua', 'O5, el viento refuerza la idea de un río vivo', 'O1, el coro habla al unísono', 'O4 emite un juicio sin evidencia; O5 sí vincula un rasgo con un efecto.'),
        ('abc', '{F} ¿En qué nivel de análisis está O6?', 'En la puesta en escena, por la ubicación en el espacio', 'En la dramaturgia, por la estructura del texto', 'En el contexto, por la época de creación', 'La tarima y la ubicación son decisiones de espacio.'),
        ('abc', '{F} ¿Qué observación vincula un rasgo con su función, propia del paso de analizar?', 'O5, el espacio abierto permite oír el viento y refuerza la idea de un río vivo', 'O3, las máscaras no dejan ver los gestos del rostro de las personas del coro', 'O1, el coro habla al unísono y avanza en bloque hacia el centro del espacio', 'O5 une un rasgo con su efecto.'),
        ('abc', '¿Qué nivel de análisis se ocupa del tiempo, el lugar y las condiciones de creación de una obra?', 'El contexto', 'La actuación', 'La dramaturgia', 'El contexto se refiere a las condiciones en que se creó y se presenta.'),
        ('abc', 'Un estudiante dice que una obra «muestra la lucha de clases» sin citar ningún rasgo. ¿Qué le falta?', 'Evidencia observable de la obra que respalde esa lectura', 'Más seguridad al decirlo en voz alta frente al curso para que todos lo acepten', 'Una opinión de la mayoría del curso que respalde esa lectura de la obra', 'Una interpretación necesita rasgos concretos de la obra como respaldo.'),
        ('=', '{F} El coro tiene 6 intérpretes y la obra otros 2 papeles (el río y la jueza). ¿Cuántas personas intervienen en total?', '6+2', 'Se suman los intérpretes del coro y los de los dos papeles.', ' personas'),
        ('abc', 'Un grupo vio solo el último acto de una obra y escribe un análisis de toda ella. ¿Qué corresponde?', 'Declarar qué parte se vio y limitar el análisis a esa parte', 'Analizarla igual como si hubieran visto toda la obra', 'Inventar lo que ocurre en los demás actos', 'Se declara el límite de la evidencia y no se inventa.'),
        ('abc', '{F} Una compañera escribe: «el coro es un grupo de personas feas con máscaras». ¿Qué corrección corresponde?', 'Describir las máscaras como un recurso de la puesta en escena y no hablar de las personas', 'Mantenerlo, porque es una opinión sincera sobre lo que se vio durante la función', 'Cambiarlo por un adjetivo más amable sobre los cuerpos de las personas del coro', 'El análisis habla de decisiones, no de cuerpos.'),
        ('abc', '{F} Un estudiante afirma que «las máscaras son un error porque no se ven los gestos del rostro». ¿Qué falta para que sea un juicio fundado?', 'Relacionar esa decisión con el propósito de la obra, que podría ser mostrar un grupo y no individuos', 'Repetir con más énfasis que no se ven los gestos del rostro durante la función', 'Cambiar la opinión según lo que piense la mayoría del curso en la conversación', 'Un juicio fundado vincula la decisión con el propósito.'),
        ('abc', 'Un grupo tiene dos análisis de la misma escena: uno solo con adjetivos y otro con hechos y su efecto. ¿Cuál sirve mejor?', 'El de hechos y efecto, porque se puede comprobar en la obra', 'El de adjetivos, porque expresa mucho más la emoción de quien vio la obra completa', 'Ninguno de los dos, porque una escena no se puede analizar con ningún método', 'Un análisis útil se apoya en evidencia.'),
    ],
    ctx=('abc', 'Dos estudiantes vieron la misma función de una obra. Una escribe: «el coro, con máscaras y en bloque, mostró un pueblo sin rostro individual». El otro escribe: «no me gustó el coro». ¿Qué diferencia hay?', 'La primera vincula rasgos con un sentido; el segundo solo da un gusto sin evidencia', 'No hay ninguna diferencia, porque ambos escritos son solamente opiniones de espectadores', 'El segundo es mejor porque es más breve y se entiende de inmediato sin explicaciones', 'El primer texto articula descripción, análisis e interpretación.'),
    sc=[
        ("En Teatro: ¿cuáles son los tres pasos del método de análisis?", "Describir, analizar e interpretar", "Van de lo observable a lo que se puede proponer."),
        ("¿Cuáles son los cuatro niveles de análisis?", "Dramaturgia, actuación, puesta en escena y contexto", "Permiten mirar la obra por partes."),
        ("¿Qué se hace si se vio solo una parte de la obra?", "Se declara y se limita el análisis a esa parte", "Se respeta el límite de la evidencia."),
    ],
    op=("Imagina una escena de ejemplo de una obra inventada: dos personajes discuten en una cocina con luz amarilla y un reloj que suena fuerte. Escribe tres observaciones: una descripción, un análisis y una interpretación rotulada como posible, cada una con su nivel de análisis. Evita valoraciones y no hables de los cuerpos de las personas.",
        "Descripción (puesta en escena): la luz amarilla ilumina la mesa y deja el resto en penumbra. Análisis (puesta en escena): la luz dirige la atención a la mesa, donde ocurre la discusión. Interpretación posible (dramaturgia): el reloj que suena sugiere que el tiempo corre en contra de los personajes.",
        ["tres observaciones de tipo distinto", "nombra el nivel de análisis de cada una", "la interpretación está rotulada como posible", "no hay valoraciones ni referencias a cuerpos"],
        ["tres observaciones rotuladas"],
        ["confundir una valoración con un análisis", "presentar la interpretación como hecho"],
        "Pregunta: «¿qué rasgo de la escena respalda esto?». Si no hay rasgo, pídele agregarlo."),
    reinforce="Mira una escena de tu casa (sin personas identificables) y escribe una descripción y un análisis de su luz o su espacio.",
    extend="Explica por qué separar descripción, análisis e interpretación evita discusiones en que cada persona habla de cosas distintas.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (texto dramático de ejemplo, original). «La balanza». Personajes: LA JUEZA, UN PANADERO y EL CORO. Prosa breve y verso en las intervenciones del coro. "
     "1 LA JUEZA: (sin mirarlo) Su pan pesa menos de lo que dice el cartel. "
     "2 EL PANADERO: Pesa lo que pesa la harina que hay, jueza. "
     "3 EL CORO: (en verso) Pesa el hambre, pesa el pan; / la balanza no sabe de eso. "
     "4 LA JUEZA: La ley no pregunta por el hambre; pregunta por los gramos. "
     "5 EL PANADERO: (deja un pan sobre la balanza) Entonces pese esto también. "
     "6 EL CORO: (en verso) Callan los números / cuando alguien tiene hambre.")
build(
    O5, 2, F,
    use="Aprenderé a analizar la propuesta dramatúrgica de una obra: su conflicto, personajes, estructura, lenguaje (prosa, verso, coro) y tema, con evidencia tomada del texto.",
    prior=["Sé distinguir descripción, análisis e interpretación.", "Sé leer la estructura dramática.", "Sé que cada personaje tiene objetivo y obstáculo."],
    explain=[
        "La propuesta dramatúrgica es la manera en que un texto construye su conflicto, sus personajes, su estructura y su lenguaje para decir algo. Para analizarla se empieza por el conflicto central (quién quiere qué y qué se lo impide), luego los personajes (objetivo, forma de hablar, relación con los demás), la estructura (cómo se ordenan los hechos y dónde está el punto de mayor tensión) y el lenguaje: si es prosa o verso, si es cotidiano o poético, y si hay recursos como el coro, que es un grupo de voces que comenta la acción.",
        "El tema es la idea general sobre la que trata la obra, como la justicia frente a la necesidad. No es lo mismo que la trama, que es lo que ocurre. Se infiere del conflicto, de lo que los personajes quieren y de lo que el lenguaje subraya. Se dice «el texto sugiere que…» y se cita una línea como evidencia. La cita es breve y se atribuye a la línea y al personaje que la dice.",
        "Cada afirmación se pregunta: ¿qué línea o rasgo del texto lo muestra? Si no hay línea que la respalde, es una opinión. Un mismo texto puede leerse de varias maneras, y se reconoce cuando hay otra lectura posible. Se trata el texto con respeto y se habla de la obra y no de la persona que la escribió o la actúa.",
    ],
    vocab=[("propuesta dramatúrgica", "modo en que un texto construye conflicto, personajes, estructura y lenguaje"), ("coro", "grupo de voces que comenta la acción"), ("verso", "texto organizado en líneas con ritmo propio"), ("prosa", "texto escrito en párrafos o líneas sin ritmo de verso"), ("tema", "idea general sobre la que trata la obra"), ("trama", "serie de hechos que ocurren en la obra")],
    worked=[
        ("Conflicto del texto", "En una escena, una estudiante quiere entregar una tarea y la profesora le dice que el plazo venció. Identifica el conflicto.", ["Quién quiere qué: la estudiante quiere entregar.", "Obstáculo: el plazo venció y la profesora lo aplica."], "La estudiante quiere entregar pero el plazo venció"),
        ("Tema con evidencia", "Línea: «Usted manda pesar el pan, pero no mira a quien lo amasa». ¿Qué tema sugiere?", ["La línea contrasta la regla con la persona.", "Sugiere un tema sobre la mirada humana frente a la norma; se cita la línea como evidencia."], "Un tema sobre la mirada humana frente a la norma, con la línea como evidencia"),
    ],
    mistakes=[("Confundir el tema con la trama.", "La trama cuenta qué ocurre; el tema es la idea general que la obra explora.", "Pregunta qué idea recorre los hechos."),
              ("Dar un tema sin citar ninguna línea.", "Sin evidencia es una opinión que no se puede comprobar en el texto.", "Cita una línea breve y di qué muestra.")],
    T=[
        ('abc', 'En dramaturgia, ¿qué es el coro?', 'Un grupo de voces que comenta la acción', 'Un personaje que solo aparece en el final', 'Una indicación de iluminación', 'El coro es un recurso colectivo que comenta lo que ocurre.'),
        ('abc', '{F} ¿Cuál es el conflicto central de la ficha?', 'La jueza aplica la norma de los gramos, mientras el panadero habla de la necesidad', 'El panadero quiere vender el pan más caro para ganar más dinero ese día', 'El coro no está de acuerdo con la forma de los versos que debe decir en la escena', 'La norma choca con la mirada sobre la necesidad.'),
        ('abc', '{F} ¿Qué línea muestra el objetivo del panadero?', 'La línea 5, cuando pide que pesen también el pan que deja sobre la balanza', 'La línea 1, cuando la jueza le dice que su pan pesa menos y no lo mira', 'La línea 4, cuando la jueza dice qué es lo que pregunta la ley en un juicio', 'En la 5 actúa para que la norma incluya su realidad.'),
        ('abc', '{F} ¿Qué recurso de lenguaje usa el coro?', 'El verso, con frases rítmicas y breves', 'La prosa cotidiana y sin ritmo propio', 'El lenguaje técnico propio de un tribunal', 'El coro habla en verso, lo que lo distingue de los personajes.'),
        ('abc', '{F} ¿Cuál es un tema que el texto sugiere?', 'La tensión entre la norma exacta y la necesidad humana', 'La honestidad de quienes venden alimentos', 'El valor del trabajo en equipo dentro de una panadería', 'Los hechos y las líneas del coro apuntan a esa tensión.'),
        ('abc', '{F} ¿Qué diferencia hay entre la trama y el tema?', 'La trama es lo que ocurre (la jueza pesa el pan); el tema es la idea general sobre la norma y la necesidad', 'La trama es una idea abstracta sobre la obra y el tema es lo que ocurre en ella', 'No hay ninguna diferencia, porque trama y tema son dos palabras sinónimas en teatro', 'La trama son hechos; el tema es la idea que los atraviesa.'),
        ('=', '{F} En la escena hay 6 líneas. Si dos son del coro, ¿cuántas líneas dicen los personajes que no son el coro?', '6-2', 'Se restan las líneas del coro al total de líneas de la escena.', ' líneas'),
        ('abc', '{F} Un compañero dice: «la jueza es una mala persona». ¿Qué corrección apoya mejor en el texto?', 'Indicar que su línea 4 muestra que prioriza la norma sobre la necesidad, sin juzgar su carácter', 'Repetir que es mala persona y citar un adjetivo que la describa ante el curso', 'Cambiar de personaje para no tener que juzgar a nadie dentro del análisis', 'Se analiza la construcción del personaje con una línea de evidencia.'),
        ('abc', '{F} ¿Qué función cumplen las indicaciones entre paréntesis, como «(sin mirarlo)»?', 'Informan acciones o tonos que ayudan a leer la relación entre los personajes', 'Son parte del texto que debe leerse en voz alta junto con las líneas de cada personaje', 'No cumplen ninguna función dramática y se pueden omitir al leer el texto en voz alta', 'Las acotaciones orientan la acción y el tono.'),
        ('abc', '{F} Una estudiante propone que la obra trata de la «traición». ¿Qué respuesta es adecuada?', 'Pedirle una línea que muestre una traición, porque el texto no la evidencia', 'Aceptarlo porque cualquier texto puede leerse de cualquier manera, sin pedir ninguna evidencia', 'Rechazarlo de inmediato y sin discusión, porque no coincide con la lectura del grupo', 'La interpretación se sostiene con evidencia del texto.'),
        ('abc', '{F} Un grupo cambia el final y hace que la jueza acepte el pan sin dudar. ¿Qué cambia en la propuesta dramatúrgica?', 'El conflicto se resuelve de forma más optimista y cambia el tema sugerido', 'Nada, porque el conflicto sigue igual aunque el final de la escena sea distinto', 'La obra deja de tener personajes y se transforma en una lectura de acotaciones', 'Cambiar el desenlace cambia el sentido que sugiere la obra.'),
        ('=', 'Un texto tiene 5 escenas; la escena de mayor tensión es la cuarta. ¿Qué porcentaje del texto se ha desarrollado cuando termina la cuarta escena?', '4*100//5', 'Cuatro de cinco escenas es el 80 % del texto.', ' %'),
        ('abc', 'Una estudiante analiza un texto escrito por una persona de su curso y comenta: «escribe así porque es de familia pobre». ¿Qué corrección corresponde?', 'Hablar del texto y de sus decisiones, no de la vida de quien lo escribió', 'Mantener el comentario porque explica el estilo con que fue escrita esta escena', 'Preguntar a la persona sobre su familia delante del curso, para entender mejor su texto', 'El análisis se centra en la obra, sin exponer a las personas.'),
    ],
    ctx=('abc', 'Un grupo debe decidir qué muestra mejor la propuesta dramatúrgica de «La balanza» para quien no la leyó: un resumen de la trama o un análisis del conflicto con dos líneas citadas. ¿Cuál sirve más?', 'El análisis con líneas citadas, porque muestra cómo se construye el sentido', 'El resumen de la trama, porque es más largo y cuenta todos los hechos del texto', 'Ninguno de los dos, porque un texto teatral no se puede resumir ni analizar', 'Citar y analizar muestra decisiones; el resumen solo cuenta hechos.'),
    sc=[
        ("En Teatro: ¿qué es el tema de una obra?", "La idea general sobre la que trata", "Se infiere del conflicto y del lenguaje."),
        ("¿Qué diferencia hay entre verso y prosa?", "El verso tiene ritmo propio en líneas; la prosa no", "Son dos modos de organizar el lenguaje."),
        ("¿Qué respalda una afirmación sobre el texto?", "Una línea breve citada y atribuida", "La cita permite comprobar la afirmación."),
    ],
    op=("Escribe un texto dramático original de seis líneas con dos personajes y un coro de dos voces, sobre un conflicto sobrio (por ejemplo, un reglamento y una necesidad). Luego redacta un análisis breve de tu propia propuesta: conflicto, personajes, lenguaje y tema, citando una línea como evidencia.",
        "Texto: GUARDIA: (señala un cartel) Hoy no se entra con paraguas. NIÑA: (apoya el suyo en la pared) Entonces ¿dónde lo dejo? CORO: (en verso) Llueve afuera / y la norma está seca. Análisis: conflicto, norma frente a necesidad; personajes, guardia que aplica el cartel y niña que pide una solución; lenguaje, coro en verso; tema, la norma frente a la vida cotidiana; evidencia: «llueve afuera y la norma está seca».",
        ["seis líneas con dos personajes y coro", "analiza conflicto, personajes, lenguaje y tema", "cita una línea como evidencia", "el conflicto es sobrio"],
        ["texto y análisis breve"],
        ["dar un tema sin evidencia", "confundir tema con trama"],
        "Pregunta: «¿qué línea muestra eso?». Si no hay línea, pídele citar una."),
    reinforce="Elige una escena que hayas escrito antes y dile a alguien de tu casa cuál es su conflicto y su tema, citando una línea.",
    extend="Explica por qué el coro puede cambiar la manera en que el público entiende un conflicto y cómo se vería en la puesta en escena.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (descripción de dos intérpretes de una misma escena, de ejemplo, inventada). Escena: un personaje debe decidir si cuenta un error ante su jefa. "
     "Intérprete 1: articula con claridad, proyecta la voz hasta el fondo, repite su partitura idéntica en dos funciones, pero la emoción del personaje se mantiene igual en toda la escena. "
     "Intérprete 2: en el fondo se le oye con dificultad y pierde dos frases, pero sus cambios de ritmo y sus pausas muestran con claridad la duda y el miedo del personaje, y escucha a su compañera para responder. "
     "Criterios técnicos: dicción, proyección, precisión de la partitura. Criterios interpretativos: coherencia del personaje, matices, escucha y relación con el otro.")
build(
    O5, 3, F,
    use="Aprenderé a analizar una actuación con criterios técnicos (dicción, proyección, precisión, control del cuerpo y del ritmo) e interpretativos (coherencia del personaje, matices, escucha, adecuación al estilo), sin evaluar a las personas ni sus cuerpos.",
    prior=["Sé distinguir descripción, análisis e interpretación.", "Sé construir una partitura y una curva emocional.", "Sé que una actuación se analiza por sus decisiones."],
    explain=[
        "Analizar una actuación es estudiar cómo un intérprete usa su voz, su cuerpo y su atención para construir un personaje. Los criterios técnicos miden la ejecución: dicción (pronunciar con claridad), proyección (hacer llegar la voz sin gritar), precisión (repetir la partitura de forma estable) y control del ritmo y del cuerpo en el espacio. Los criterios interpretativos miden la construcción del personaje: coherencia (que sus decisiones respondan a su objetivo), matices (cambios finos de emoción), escucha (responder a lo que ocurre) y adecuación al estilo de la obra.",
        "Un buen análisis no suma puntos al azar. Describe lo observado, vincula cada rasgo con un criterio y reconoce que técnica e interpretación pueden darse por separado. Una persona puede tener gran precisión técnica sin matices, o muy buenos matices con dificultades de proyección. También considera el contexto: si el espacio era grande, si hubo una falla de sonido o si el estilo pedía otra cosa. No se opina sobre el cuerpo, el aspecto ni la identidad de quien actúa.",
        "Si se analiza el trabajo de pares, se hace con retroalimentación descriptiva y con respeto. Las dificultades técnicas se tratan como aspectos que se pueden entrenar, con calentamiento y cuidado de la voz, y no como defectos de la persona. Nadie queda expuesto frente al curso si no lo desea.",
    ],
    vocab=[("dicción", "claridad al pronunciar las palabras"), ("proyección", "capacidad de hacer llegar la voz lejos sin gritar"), ("precisión", "capacidad de repetir una partitura de forma estable"), ("coherencia", "acuerdo entre las decisiones del personaje y su objetivo"), ("matiz", "cambio fino de emoción o intención"), ("escucha", "atención real a lo que hace y dice la otra persona")],
    worked=[
        ("Clasificar un criterio", "«La actriz cambia de ritmo cuando el otro personaje la interrumpe». ¿Es técnico o interpretativo?", ["Muestra respuesta a lo que ocurre, es decir, escucha.", "Escucha y relación con el otro son criterios interpretativos."], "Interpretativo"),
        ("Análisis con contexto", "Un intérprete se oye poco desde el fondo en un gimnasio con eco. ¿Cómo se analiza?", ["Se describe que la proyección no alcanza el fondo en ese espacio.", "Se considera el eco como contexto y se sugiere trabajar proyección y articulación."], "Proyección insuficiente en ese espacio, con el eco como contexto"),
    ],
    mistakes=[("Juzgar a una persona por cómo se ve o suena su cuerpo.", "El análisis se refiere a decisiones de actuación y no a características físicas.", "Describe la voz y el cuerpo como recursos usados."),
              ("Dar por mala una actuación porque tuvo un error técnico.", "La técnica y la interpretación son aspectos distintos y pueden separarse.", "Evalúa cada criterio por separado.")],
    T=[
        ('abc', 'En actuación, ¿qué es la dicción?', 'Pronunciar con claridad las palabras', 'Hacer llegar la voz a todo el público sin esfuerzo', 'Decir un texto sin errores durante la función', 'La dicción es la claridad de pronunciación.'),
        ('abc', '{F} ¿Qué intérprete muestra mayor precisión técnica?', 'El intérprete 1, que repite idéntica su partitura', 'El intérprete 2, que cambia el ritmo para mostrar duda', 'Ambos por igual, porque actúan la misma escena', 'La repetición idéntica de la partitura es precisión.'),
        ('abc', '{F} ¿Qué criterio muestra el intérprete 2 mejor que el 1?', 'Matices y escucha, al cambiar de ritmo y responder a su compañera', 'Proyección, porque llega a todos los puestos del fondo', 'Dicción, porque no pierde ninguna frase', 'Sus cambios finos y su respuesta al otro son criterios interpretativos.'),
        ('abc', '{F} ¿Qué criterio muestra el intérprete 1 mejor que el 2?', 'Proyección y precisión de la partitura', 'Matices y escucha del compañero', 'Adecuación al estilo de la obra', 'Se le oye hasta el fondo y repite su partitura igual.'),
        ('abc', '{F} ¿Cuál es la afirmación más fundada?', 'El intérprete 1 tiene mejor ejecución técnica, pero el 2 construye con más matices al personaje', 'El intérprete 1 actúa mejor en todo, porque se le oye más desde el fondo de la sala', 'El intérprete 2 actúa peor, porque perdió dos frases durante la escena completa', 'Cada afirmación se limita a criterios y a lo observado.'),
        ('=', '{F} Si el intérprete 2 pierde 2 frases de 20 que tiene la escena, ¿qué porcentaje de las frases dice completo?', '(20-2)*100//20', 'Se restan las frases perdidas y se pasa a porcentaje.', ' %'),
        ('abc', 'Un comentario sobre un actor dice: «es demasiado delgado para el papel». ¿Qué corrección corresponde?', 'Eliminarlo, porque el análisis se refiere a decisiones de actuación y no al cuerpo', 'Mantenerlo, porque es un dato objetivo que describe lo que se ve en el escenario', 'Escribirlo con más suavidad, para que la persona no se sienta mal con el comentario', 'No se evalúa el cuerpo de nadie.'),
        ('abc', '{F} Una intérprete falla en la proyección porque la sala tiene mucho eco. ¿Cómo se considera ese dato?', 'Como parte del contexto que se anota junto con la dificultad observada', 'Se ignora, porque la dificultad de proyección es solo responsabilidad de la persona', 'Se usa para decir que el eco es la única causa de todo lo que ocurrió en escena', 'El contexto matiza el análisis sin borrar lo observado.'),
        ('abc', '{F} El grupo quiere dar una sola nota global de 1 a 7 a cada intérprete. ¿Qué conviene más?', 'Describir cada criterio por separado con evidencia, en vez de una nota global', 'Usar una nota global de 1 a 7 para cada intérprete, porque es más fácil de comunicar', 'No comentar nada sobre la actuación para evitar problemas entre los compañeros', 'Los criterios separados dan información útil para mejorar.'),
        ('abc', 'Una estudiante tiene una dificultad de proyección y se siente avergonzada por un comentario del curso. ¿Qué es lo adecuado?', 'Reforzar que es un aspecto entrenable y proponer ejercicios seguros, sin exponerla', 'Pedirle que repita la escena delante de todos hasta que logre mejorar su proyección', 'Dejar que el curso comente libremente sobre su voz, para que aprenda a aceptar críticas', 'Las dificultades se abordan con respeto y entrenamiento.'),
        ('abc', '{F} Quieres comparar a los dos intérpretes de forma justa. ¿Qué condición se necesita?', 'Mismos criterios, misma escena y condiciones parecidas de espacio y sonido', 'Que uno de los dos intérpretes haya actuado antes que el otro frente al público', 'Que el curso vote cuál de los dos intérpretes prefiere, después de verlos actuar', 'Para comparar con justicia se igualan criterios y condiciones.'),
        ('=', 'En 4 funciones, un intérprete repitió su partitura idéntica en 3 de ellas. ¿Qué porcentaje de las funciones fue idéntico?', '3*100//4', 'Se divide las funciones idénticas entre el total y se pasa a porcentaje.', ' %'),
        ('abc', '{F} Un compañero dice: «el intérprete 2 no sabe actuar porque se le pierden frases». ¿Qué respuesta usa evidencia?', 'Perdió dos frases, pero sus pausas y cambios de ritmo muestran la duda del personaje', 'No importa que haya perdido frases, porque lo único importante es la emoción del personaje', 'Tiene razón, porque no hay ningún otro dato observado que valga para analizarlo', 'Una respuesta fundada considera todos los datos observados.'),
    ],
    ctx=('abc', 'Un curso asiste a una función escolar en que una estudiante olvida una frase y sigue con calma, mientras su compañero se queda inmóvil. Después, un grupo comenta con burlas. ¿Qué conviene hacer?', 'Detener las burlas y analizar lo ocurrido como situación de escena, con respeto y sin exponer a nadie', 'Reírse con ellos para no quedar fuera del grupo y evitar que se burlen también de uno', 'Pedirle a la estudiante que repita la escena a modo de castigo por su olvido', 'El análisis es respetuoso y se detiene el trato dañino.'),
    sc=[
        ("En Teatro: ¿qué es la escucha en actuación?", "Responder realmente a lo que hace y dice la otra persona", "Es un criterio interpretativo, porque mira la relación con el otro."),
        ("¿Qué criterio técnico se refiere a hacer llegar la voz lejos sin gritar?", "La proyección", "La proyección usa respiración y articulación."),
        ("¿Se opina sobre el cuerpo de quien actúa al analizar su trabajo?", "No, solo sobre sus decisiones de actuación", "El análisis no evalúa cuerpos, solo decisiones de actuación."),
    ],
    op=("Describe una actuación de ejemplo inventada (dos intérpretes en una escena de tu elección). Escribe un análisis de cada intérprete con dos criterios técnicos y dos interpretativos, cada uno con evidencia observable. Cierra con una sugerencia de trabajo para cada uno. No hables de cuerpos ni de apariencia.",
        "Escena: una vecina pide ayuda a otra. Intérprete A: dicción clara y proyección hasta el fondo (técnicos); matices limitados, siempre igual (interpretativo); escucha poca. Sugerencia: variar el ritmo. Intérprete B: voz débil al final (técnico); cambios de ritmo que muestran duda (interpretativo); escucha atenta. Sugerencia: ejercicios de respiración.",
        ["dos criterios técnicos y dos interpretativos por intérprete", "evidencia observable en cada criterio", "una sugerencia para cada uno", "no habla de cuerpos ni apariencia"],
        ["análisis de dos intérpretes con sugerencias"],
        ["opinar sobre el cuerpo", "dar una sola nota global sin evidencia"],
        "Pregunta: «¿qué se observó para decir eso?». Si no hay observación, pídele agregarla."),
    reinforce="Describe cómo conversa una persona de tu casa por teléfono usando tres criterios de voz (dicción, ritmo, proyección), sin juzgar.",
    extend="Explica por qué separar criterios técnicos e interpretativos da una visión más justa de una actuación que una sola nota.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (dos obras de ejemplo, inventadas, de épocas y procedencias distintas). "
     "Obra A: «La plaza de los vientos», de una compañía ficticia de tradición de teatro de calle de una ciudad costera; se presenta de día, sin luz artificial, en una plaza, con el público de pie alrededor; vestuario colorido y máscaras grandes que se ven desde lejos; música tocada en vivo; actuación amplia y voz proyectada. "
     "Obra B: «Cuarto 12», de una compañía ficticia contemporánea; se presenta en una sala cerrada con 60 asientos; luz eléctrica con cambios sutiles; proyección de fotografías; actuación contenida y voz natural; la escenografía es un cuarto con una cama y una ventana. "
     "Datos de contexto de ejemplo: en A, el público circula y pasa por la plaza, y puede irse en cualquier momento; en B, el público compra una entrada y se sienta en silencio.")
build(
    O5, 4, F,
    use="Aprenderé a relacionar los elementos de la puesta en escena (espacio, vestuario, luz, sonido, objetos, tecnología) con el contexto de época, lugar y condiciones de presentación de una obra, comparando obras de distinta procedencia con cautela y sin estereotipos.",
    prior=["Sé analizar dramaturgia y actuación.", "Sé distinguir descripción, análisis e interpretación.", "Sé que una obra se estudia con su contexto."],
    explain=[
        "El contexto de una obra reúne la época, el lugar, el público, los medios disponibles y las costumbres teatrales en que nace y se presenta. La puesta en escena de una obra suele responder al contexto: una obra de plaza, sin luz artificial y con público que circula, necesita máscaras grandes, voz proyectada y acciones fáciles de ver desde lejos. Una obra de sala cerrada puede usar luz sutil, voz natural y detalles pequeños porque el público está cerca y en silencio.",
        "Para relacionar puesta en escena y contexto se usan fórmulas prudentes: «pudo responder a», «se explica en parte por», «es coherente con». Se evita el determinismo (decir que el contexto causa una sola decisión posible) y los estereotipos (decir que todas las obras de un país o una época son iguales). Dos obras de procedencias distintas se comparan con los mismos criterios, sin suponer que una es mejor por ser más reciente o más conocida.",
        "Los datos de contexto se confirman en fuentes confiables y se citan. Si no se sabe algo, no se inventa. Cuando una obra proviene de una tradición cultural ajena, se la trata con respeto y se consulta a quienes la conocen. El análisis de lo que ocurre en escena no se extiende a juicios sobre las personas de ese lugar.",
    ],
    vocab=[("contexto", "época, lugar, público y condiciones en que se crea y presenta una obra"), ("verosímil", "creíble dentro del mundo de la obra"), ("determinismo", "idea de que una causa produce una sola consecuencia posible"), ("tradición", "conjunto de prácticas que una comunidad mantiene en el tiempo"), ("comparar", "mirar dos obras con los mismos criterios")],
    worked=[
        ("Relacionar con prudencia", "En una obra de plaza se usan máscaras grandes. ¿Cómo lo relacionas con el contexto?", ["El público está lejos y de pie: necesita ver desde la distancia.", "«El tamaño de las máscaras pudo responder a la distancia del público»."], "Pudo responder a la distancia del público, con fórmula prudente"),
        ("Evitar un estereotipo", "Un estudiante dice: «todo el teatro antiguo es exagerado». ¿Qué corrección corresponde?", ["Es una generalización sin evidencia.", "Se reemplaza por una afirmación sobre una obra concreta, con sus rasgos observados."], "Hablar de una obra concreta y de sus rasgos"),
    ],
    mistakes=[("Decir que una obra «tiene que ser así» por su época.", "El contexto orienta, pero no determina una sola decisión; los artistas eligen.", "Usa «pudo responder a» y busca más de una explicación."),
              ("Comparar dos obras con criterios distintos.", "La comparación resulta injusta y favorece a una sin razón.", "Usa los mismos criterios para ambas.")],
    T=[
        ('abc', 'En análisis de obras, ¿qué es el contexto?', 'La época, el lugar, el público y las condiciones en que se crea y presenta la obra', 'El argumento y los hechos que ocurren en la historia, ordenados escena por escena', 'El nombre de la compañía y de las personas que actúan, junto con su edad y su ciudad', 'El contexto es el entorno de creación y presentación, no solo la trama.'),
        ('abc', '{F} ¿Qué rasgo de la obra A se vincula con que el público está de pie y a distancia?', 'Las máscaras grandes y la voz proyectada', 'Las proyecciones de fotografías', 'La luz eléctrica con cambios sutiles', 'La distancia pide recursos visibles y audibles desde lejos.'),
        ('abc', '{F} ¿Qué rasgo de la obra B se vincula con un público cercano y en silencio?', 'La actuación contenida y la luz con cambios sutiles', 'El vestuario colorido y la música en vivo', 'La ausencia de luz artificial', 'La cercanía y el silencio permiten detalles pequeños.'),
        ('abc', '{F} ¿Cuál es una fórmula prudente para relacionar rasgo y contexto?', '«La voz proyectada de la obra A pudo responder al espacio abierto»', '«La voz proyectada de la obra A se debe solo a que es antigua»', '«Toda obra de plaza usa voz proyectada»', 'Una fórmula prudente deja abierta otra posible explicación.'),
        ('abc', '{F} ¿Cuál es una comparación con los mismos criterios?', 'Revisar en las dos obras cómo usan el espacio y qué efecto producen', 'Decir que la obra B es mejor porque tiene luz eléctrica', 'Decir que la obra A es peor porque no tiene sala cerrada', 'Se aplica el mismo criterio a ambas y se compara el efecto.'),
        ('=', '{F} La sala de la obra B tiene 60 asientos. Si se ocupan 45, ¿cuántos quedan vacíos?', '60-45', 'Se resta lo ocupado al total.', ' asientos'),
        ('abc', '{F} Un compañero afirma: «el teatro de calle es de menor calidad que el de sala». ¿Qué corresponde?', 'Pedir criterios y evidencia comparables, porque son condiciones de presentación distintas', 'Estar de acuerdo con la frase, porque la sala tiene más tecnología que la calle', 'Evitar hablar del tema, porque nadie puede comparar dos formas de hacer teatro', 'Lo distinto no es peor; se compara con los mismos criterios.'),
        ('abc', '{F} El grupo dice que la obra A «usa máscaras porque su tradición es primitiva». ¿Cuál es el problema?', 'Un estereotipo sin evidencia sobre una tradición cultural', 'Que la obra A en realidad no usa máscaras y el grupo se equivocó al observarla', 'Que la obra B es más moderna que la obra A y por eso la tradición no importa', 'No se juzgan tradiciones con prejuicios; se estudian con respeto.'),
        ('abc', 'Un grupo quiere afirmar algo sobre la época de una obra, pero no tiene datos. ¿Qué debe hacer?', 'Buscar fuentes confiables y, si no las hay, decir que no se sabe', 'Inventar un dato verosímil para completar el análisis', 'Usar un dato de otra obra distinta como si fuera igual', 'Lo que no se sabe no se inventa.'),
        ('abc', '{F} ¿Qué se puede decir con prudencia sobre la actuación de la obra B?', 'Es coherente con una sala cerrada, donde la cercanía permite una voz natural', 'Es mejor que la de A porque es contenida y se parece más a la vida cotidiana', 'Está equivocada porque no proyecta la voz hasta el fondo como lo hace la de A', 'La coherencia con el contexto no implica superioridad.'),
        ('=', 'La obra A se presenta 3 veces al día, de 40 minutos cada una, durante 4 días. ¿Cuántos minutos suma en total?', '3*40*4', 'Se multiplican funciones por duración y por días.', ' minutos'),
        ('abc', '{F} Se quiere trasladar la obra B a un patio abierto con 100 personas. ¿Qué decisión de puesta en escena debe revisarse primero?', 'Proyección de la voz y tamaño de los gestos, porque cambian la distancia y el espacio', 'El título de la obra, que tiene que ser más corto para que se entienda a distancia', 'El nombre de las personas del elenco, que debe cambiarse para el público del patio', 'El cambio de contexto afecta voz y gesto.'),
        ('abc', 'Un estudiante dice que una obra «debe juzgarse con las ideas de hoy, sin importar el contexto». ¿Qué respuesta es más completa?', 'Se puede criticar su contenido hoy, pero entendiendo primero en qué contexto se creó', 'No se puede criticar ninguna obra del pasado, porque sus creadores ya no pueden responder', 'Solo se critica lo que se parece a lo actual, y lo antiguo se deja sin analizar', 'Comprender el contexto no impide criticar, pero evita juicios apurados.'),
    ],
    ctx=('abc', 'Un grupo analiza una obra de otra región del país con tradiciones que no conoce. Un integrante propone suponer su significado «porque es obvio». ¿Qué decisión es más respetuosa y rigurosa?', 'Investigar en fuentes confiables o consultar a personas que la conocen antes de interpretar', 'Interpretarla según lo que el grupo se imagina de ese lugar y de su gente', 'Descartarla del análisis para no equivocarse al hablar de una tradición que no se conoce', 'Lo desconocido se investiga con respeto y no se supone.'),
    sc=[
        ("En Teatro: ¿qué es el determinismo al analizar una obra?", "Creer que el contexto produce una sola decisión posible", "Es una simplificación; las decisiones artísticas se eligen."),
        ("¿Cómo se comparan dos obras de distinta procedencia?", "Con los mismos criterios para ambas", "Así la comparación es justa para ambas obras."),
        ("¿Qué se hace con un dato de contexto que no se conoce?", "Se busca en fuentes confiables o se declara que no se sabe", "No se inventan datos que no están comprobados."),
    ],
    op=("Compara dos obras de ejemplo que inventes (una pensada para espacio abierto y otra para sala cerrada). Para cada una describe espacio, luz, vestuario y actuación, y vincula dos rasgos con su contexto usando fórmulas prudentes. Termina con una afirmación comparada que use el mismo criterio para ambas.",
        "Obra 1 (patio abierto): luz natural, vestuario de colores fuertes, actuación amplia; el patio es grande y el público está lejos, por lo que los colores y gestos pudieron responder a la distancia. Obra 2 (sala cerrada): luz tenue, vestuario sobrio, actuación contenida; la sala pequeña permitió detalles. Comparación: ambas ajustan la amplitud de actuación a la distancia del público.",
        ["describe cuatro rasgos de cada obra", "vincula dos rasgos con el contexto con fórmulas prudentes", "usa el mismo criterio para comparar", "evita estereotipos"],
        ["comparación de dos obras con contexto"],
        ["afirmar que el contexto causa una sola decisión", "decir que una obra es mejor por ser más moderna"],
        "Pregunta: «¿por qué ese rasgo responde a ese contexto y no a otro?». Si no hay razón, pídele agregarla."),
    reinforce="Compara cómo se cuenta una historia en una conversación por mensajes y en una conversación en persona, usando el mismo criterio para ambas.",
    extend="Explica por qué comparar con criterios comunes evita decir que una tradición teatral es mejor que otra.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (borrador de informe de análisis, de ejemplo, inventado). Obra «Cuarto 12» (ficha de la clase anterior), con un dato adicional: la compañía publicó un programa de mano con el propósito «mostrar la soledad de una persona que espera una visita». "
     "Afirmación 1: «La escenografía de una cama y una ventana sugiere un espacio íntimo y de espera.» "
     "Afirmación 2: «La luz con cambios sutiles marca el paso de las horas, lo que refuerza la idea de espera.» "
     "Afirmación 3: «Las proyecciones de fotografías muestran que el personaje fue un gran viajero.» (la obra no las atribuye a nadie ni lo dice el programa). "
     "Afirmación 4: «Todo el teatro contemporáneo trabaja la soledad.» "
     "Afirmación 5: «La actuación contenida es coherente con una sala cerrada y con el propósito de intimidad.»")
build(
    O5, 5, F,
    use="Aprenderé a redactar un informe de análisis estético que integre dramaturgia, actuación, puesta en escena y contexto, a revisar la evidencia de cada afirmación y a declarar los límites de lo que se sabe.",
    prior=["Sé analizar los cuatro niveles de una obra.", "Sé usar fórmulas prudentes.", "Sé citar fuentes."],
    explain=[
        "Un informe de análisis reúne en un texto breve lo que se observó y se interpretó de una obra. Su estructura es: identificación de la obra y de lo que se vio; propósito declarado o inferido; análisis por niveles con evidencia; relaciones entre niveles; interpretación rotulada como posible; límites. Las relaciones entre niveles son la parte más valiosa: por ejemplo, cómo la luz sutil (puesta en escena) refuerza el tema de la espera (dramaturgia) y es coherente con la actuación contenida y con la sala pequeña (contexto).",
        "Antes de entregar el informe se verifica cada afirmación con una pregunta: ¿qué observación de la obra o qué fuente confiable la respalda? Si no la hay, se elimina, se reformula con prudencia o se declara como hipótesis. Una generalización sin datos («todo el teatro contemporáneo…») también se elimina. Los límites se declaran: qué parte de la obra se vio, qué fuentes se usaron y qué quedó sin comprobar.",
        "Un buen informe conserva la coherencia: la interpretación se apoya en lo analizado, y lo analizado, en lo descrito. Se escribe con respeto y sin juicios sobre las personas del elenco. Lo tomado de otros textos se cita. Un informe puede ser revisado por pares con retroalimentación descriptiva, y quien lo escribe decide qué cambiar.",
    ],
    vocab=[("informe de análisis", "texto que integra observaciones, interpretación y límites sobre una obra"), ("hipótesis", "afirmación posible que aún no está comprobada"), ("coherencia", "acuerdo entre lo descrito, lo analizado y lo interpretado"), ("relación entre niveles", "conexión entre aspectos de dramaturgia, actuación, puesta en escena y contexto"), ("límites", "lo que no se vio, no se sabe o no se pudo comprobar")],
    worked=[
        ("Verificar una afirmación", "«La luz roja indica que el personaje está enojado». El programa y la obra no dicen nada del color. ¿Qué haces?", ["Falta evidencia que respalde esa relación.", "La reformulo como hipótesis: «la luz roja podría sugerir enojo, aunque no hay otra evidencia»."], "Reformularla como hipótesis prudente"),
        ("Relacionar niveles", "Dato: la sala es pequeña y la actuación es contenida. ¿Qué relación puedes proponer?", ["La cercanía del público permite gestos pequeños.", "«La actuación contenida es coherente con la cercanía de la sala»."], "La actuación contenida es coherente con la cercanía de la sala"),
    ],
    mistakes=[("Escribir un informe con una lista de datos sin relaciones.", "Sin conexiones no hay análisis, solo descripción.", "Vincula al menos dos niveles."),
              ("Afirmar algo sin evidencia porque «es lógico».", "Lo lógico no es lo observado y puede ser falso.", "Reformula como hipótesis o elimina.")],
    T=[
        ('abc', 'En un informe de análisis, ¿qué es una hipótesis?', 'Una afirmación posible que aún no está comprobada', 'Un dato que aparece en el programa de mano', 'Una opinión sobre si la obra gustó', 'La hipótesis se declara como tal y no como hecho.'),
        ('abc', '{F} ¿Qué afirmación respalda con evidencia directa la propuesta de puesta en escena?', 'La afirmación 2, que vincula luz y paso de las horas con evidencia observada', 'La afirmación 4, que habla de todo el teatro contemporáneo sin mostrar datos de la obra', 'La afirmación 3, que dice que el personaje es un gran viajero sin que lo diga la obra', 'La afirmación 2 se apoya en un rasgo observable de la obra.'),
        ('abc', '{F} ¿Por qué la afirmación 3 no está respaldada?', 'Porque ni la obra ni el programa dicen que las fotografías sean del personaje', 'Porque las fotografías proyectadas no forman parte de la puesta en escena', 'Porque es demasiado breve para ser una afirmación válida dentro de un informe de análisis', 'Falta una fuente que indique de quién son las fotografías.'),
        ('abc', '{F} ¿Qué problema tiene la afirmación 4?', 'Es una generalización sin datos', 'Está mal escrita, pero tiene evidencia', 'Habla del contexto, que no se analiza', 'Una generalización sin datos no puede respaldarse.'),
        ('abc', '{F} ¿Qué afirmación vincula dos niveles de análisis?', 'La afirmación 5, que vincula actuación, sala cerrada y propósito', 'La afirmación 1, que solo habla de la escenografía de una cama y una ventana', 'La afirmación 3, que solo habla de las fotografías proyectadas durante la obra', 'La 5 conecta actuación, contexto y dramaturgia.'),
        ('abc', '{F} ¿Cómo se reformula la afirmación 3 con prudencia?', '«Las fotografías podrían sugerir viajes, aunque no se indica de quién son»', '«Es seguro que el personaje fue un gran viajero, porque así lo muestran las fotografías»', '«No hay fotografías en la obra, por lo que la afirmación se elimina del informe»', 'Se declara como posible y con su límite.'),
        ('=', '{F} El informe tiene 5 afirmaciones y 3 están respaldadas por evidencia. ¿Qué porcentaje está respaldado?', '3*100//5', 'Se divide las afirmaciones respaldadas entre el total y se pasa a porcentaje.', ' %'),
        ('abc', '¿Qué debe declarar un informe sobre sus límites?', 'Qué parte de la obra se vio, qué fuentes se usaron y qué quedó sin comprobar', 'Que el análisis es perfecto y completo, y que no necesita ninguna revisión posterior', 'Que otras personas deben coincidir con lo que dice el informe para que sea válido', 'Declarar los límites protege la honestidad del informe.'),
        ('abc', '{F} Una compañera quiere agregar que la actriz «parecía triste en la vida real». ¿Qué corresponde?', 'Eliminarlo, porque el análisis trata de la obra y no de la vida privada de las personas', 'Mantenerlo, porque da más emoción al informe y ayuda a entender el personaje de la obra', 'Preguntarle a la actriz delante del curso si estaba triste en su vida real', 'No se especula sobre las personas fuera de la obra.'),
        ('abc', '{F} Un informe tiene análisis separados de luz, actuación y texto, pero ninguna relación entre ellos. ¿Qué mejora tiene?', 'Agregar relaciones entre niveles, como luz sutil y tema de la espera', 'Eliminar el análisis de la actuación, para que el informe quede más breve y simple', 'Repetir las descripciones con más adjetivos, para que el informe se vea más largo', 'Lo que da valor al informe son las relaciones.'),
        ('abc', 'Dos informes sobre la misma obra proponen interpretaciones distintas, ambas con evidencia. ¿Qué conclusión es adecuada?', 'Ambas pueden ser lecturas posibles y se discuten con su evidencia', 'Una debe estar equivocada y se elimina del trabajo, porque dos lecturas no pueden convivir', 'Hay que votar cuál es la correcta y descartar la que obtenga menos votos del curso', 'Una obra puede admitir varias lecturas fundadas.'),
        ('=', 'Un informe de 5 párrafos dedica 1 a la identificación, 2 al análisis, 1 a las relaciones y el resto a los límites. ¿Cuántos párrafos son de límites?', '5-(1+2+1)', 'Se resta del total lo que ocupan las otras partes.', ' párrafo'),
        ('abc', '{F} Antes de entregar el informe, ¿qué pregunta se hace a cada afirmación?', '¿Qué observación o fuente confiable la respalda?', '¿Cuántas personas están de acuerdo con ella?', '¿Qué tan original es respecto de los informes de otros grupos?', 'La evidencia es el criterio de verificación.'),
    ],
    ctx=('abc', 'Un grupo vio solo una grabación parcial de una obra y debe entregar un informe. Uno propone «completar» lo que no vieron con lo que imaginan. ¿Qué decisión es adecuada?', 'Declarar los límites y limitar el análisis a lo visto, con hipótesis marcadas', 'Completar con lo más probable y presentarlo como un hecho, sin avisar que se imaginó', 'No entregar el informe, para evitar errores, porque no se vio la obra completa', 'La honestidad sobre los límites es parte del análisis.'),
    sc=[
        ("En Teatro: ¿para qué sirve declarar los límites de un informe?", "Para decir qué se vio, qué se sabe y qué quedó sin comprobar", "Muestra honestidad y permite revisar el análisis."),
        ("¿Qué se hace con una afirmación sin evidencia?", "Se elimina, se reformula con prudencia o se declara como hipótesis", "Una afirmación sin respaldo no puede quedar como hecho."),
        ("¿Qué relaciones aportan más valor a un informe?", "Las relaciones entre niveles de análisis", "Muestran cómo se articulan las decisiones."),
    ],
    op=("Redacta un informe de análisis breve (cinco o seis líneas) de una obra de ejemplo que inventes. Incluye identificación, propósito, un análisis con evidencia de dos niveles, una relación entre niveles, una interpretación rotulada como posible y una frase de límites. No uses obras reales con derechos.",
        "Obra de ejemplo: «El último tren», compañía ficticia, sala pequeña. Propósito inferido: mostrar la espera. Puesta en escena: un banco y un reloj sin agujas. Actuación: voz baja y pausas largas. Relación: la ausencia de agujas refuerza la espera sin fin que muestran las pausas. Interpretación posible: el tiempo no avanza para el personaje. Límites: se vio solo el primer acto.",
        ["identifica la obra y su propósito", "analiza dos niveles con evidencia", "incluye una relación y una interpretación posible", "declara los límites"],
        ["informe de cinco a seis líneas"],
        ["listar datos sin relaciones", "afirmar sin evidencia"],
        "Pregunta: «¿qué respalda esa frase?». Si no hay respaldo, pídele reformularla o quitarla."),
    reinforce="Elige una película o serie que conozcas y escribe una relación entre dos rasgos suyos, sin inventar datos del rodaje.",
    extend="Explica por qué un informe honesto sobre sus límites es más confiable que uno que parece saberlo todo.",
)

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (reacciones de espectadores, de ejemplo, inventadas). Obra «Cuarto 12»: una persona espera una visita en un cuarto con una cama y una ventana; la luz cambia despacio y la actuación es contenida. "
     "Espectadora A: «Me dio ganas de llorar; me acordé de mi abuela. Fue la mejor obra que he visto.» "
     "Espectador B: «No me gustan las obras lentas. Me aburrí y miré el teléfono.» "
     "Espectadora C: «La luz que cambia despacio me hizo sentir el paso de las horas; creo que la obra muestra la espera, aunque a mí me gusta más el teatro con acción.» "
     "Dato: A es amiga de una actriz de la compañía; B llegó cansado y con hambre; C anotó dos rasgos de la obra mientras la veía.")
build(
    O6, 1, F,
    use="Aprenderé a distinguir la apreciación personal (reacción y gusto) del análisis y del juicio estético, a reconocer los sesgos que influyen en cómo miro una obra y a pasar de una reacción a una valoración con criterios.",
    prior=["Sé analizar una obra por niveles.", "Distingo describir, analizar e interpretar.", "Sé que una opinión necesita evidencia."],
    explain=[
        "Ante una obra se dan tres cosas distintas. La reacción es lo que se siente en el momento: emoción, risa, aburrimiento. El gusto es la preferencia personal por ciertos estilos o temas. El juicio estético es una valoración de la obra, como «está bien lograda» o «no cumple su propósito», que se apoya en criterios y en evidencia de la obra. La reacción y el gusto son válidos como experiencia, pero no bastan para sostener un juicio, porque dependen de quien mira.",
        "La apreciación personal es el punto de partida de un juicio, no su reemplazo. Para pasar de una a otro se hacen tres cosas: se nombra la reacción, se busca qué rasgos de la obra la provocaron y se revisa si el criterio elegido es adecuado al propósito de la obra. También se reconocen los sesgos, que son factores que inclinan el juicio sin que se note: ser amiga del elenco, llegar cansado, esperar otro tipo de obra, o dejarse llevar por lo que opina el grupo.",
        "Un juicio fundado puede diferir del gusto: se puede reconocer que una obra está muy bien lograda aunque no sea de nuestro estilo preferido. Y se puede sentir una emoción intensa sin que la obra cumpla bien su propósito. En clase, nadie debe justificar sus lágrimas ni su aburrimiento: son reacciones personales que se respetan, y lo que se discute es la valoración de la obra.",
    ],
    vocab=[("reacción", "lo que se siente en el momento al ver una obra"), ("gusto", "preferencia personal por estilos o temas"), ("juicio estético", "valoración de una obra apoyada en criterios y evidencia"), ("sesgo", "factor que inclina el juicio sin que se note"), ("criterio", "aspecto con el que se valora una obra")],
    worked=[
        ("Separar reacción y juicio", "«Me aburrí, por eso la obra es mala». ¿Qué falta para que sea un juicio?", ["Hay una reacción personal, pero ninguna evidencia ni criterio.", "Faltan rasgos de la obra (por ejemplo, ritmo o estructura) y el criterio con el que se valora."], "Rasgos de la obra y un criterio"),
        ("Reconocer un sesgo", "Una estudiante es hermana de un actor y dice que la obra es excelente. ¿Qué sesgo puede influir?", ["Su cercanía con el elenco puede inclinar su juicio.", "Se declara el vínculo y se apoya la valoración en evidencia de la obra."], "El vínculo con el elenco; se declara y se usa evidencia"),
    ],
    mistakes=[("Creer que una emoción intensa prueba que la obra es buena.", "La emoción depende de quien mira y de sus recuerdos, no solo de la obra.", "Nombra la emoción y busca qué rasgos la provocaron."),
              ("Descalificar la opinión de otra persona porque su gusto es distinto.", "El gusto no es un error; lo que se discute es la valoración fundada.", "Pide criterios y evidencia, no cambies de gusto.")],
    T=[
        ('abc', 'En apreciación teatral, ¿qué es el gusto?', 'Una preferencia personal por ciertos estilos o temas', 'Una valoración basada en criterios y evidencia', 'Lo que sucede en la obra durante una función', 'El gusto es subjetivo y no necesita justificarse.'),
        ('abc', '{F} ¿Qué frase es solo una reacción?', 'El de A: «me dio ganas de llorar»', 'El de C: «la luz me hizo sentir el paso de las horas, por eso creo que muestra espera»', 'El de B: «no me gustan las obras lentas»', 'La reacción es lo que se siente, aunque no se respalde.'),
        ('abc', '{F} ¿Qué enunciado se acerca más a un juicio con evidencia?', 'El de C, porque vincula la luz con el paso de las horas', 'El de B, porque es sincero y dice con claridad lo que sintió al ver la obra', 'El de A, porque la emoción que sintió fue intensa y se emocionó al llorar', 'C señala un rasgo de la obra y un efecto.'),
        ('abc', '{F} ¿Qué sesgo puede influir en el enunciado de A?', 'Ser amiga de una actriz de la compañía', 'Haber llegado con hambre', 'Haber anotado dos rasgos de la obra', 'La amistad con el elenco puede inclinar la valoración.'),
        ('abc', '{F} ¿Qué sesgo puede influir en el enunciado de B?', 'Haber llegado cansado y con hambre', 'Tener una amiga en el elenco', 'Haber vinculado la luz con el tema', 'El estado físico influye en cómo se percibe la obra.'),
        ('abc', '{F} C dice que prefiere el teatro con acción, pero valora la obra como logro de su propósito. ¿Qué muestra eso?', 'Que se puede reconocer lo logrado de una obra aunque no sea del gusto propio', 'Que su juicio es poco sincero, porque no coincide con lo que prefiere ver', 'Que no tiene criterios para valorar, porque prefiere otro tipo de teatro más rápido', 'El juicio puede diferir del gusto.'),
        ('=', '{F} Un curso de 36 estudiantes vio la obra; 9 dijeron que la sintieron lenta. ¿Qué porcentaje del curso dijo eso?', '9*100//36', 'Se divide el número de estudiantes entre el total y se pasa a porcentaje.', ' %'),
        ('abc', 'Un estudiante dice: «a mí no me gusta, así que la obra es mala». ¿Cuál es el error?', 'Pasa de un gusto a una valoración sin criterios ni evidencia', 'Usó un criterio demasiado exigente para valorarla', 'Habló de la obra en vez de hablar de sí mismo', 'El gusto no sustituye al juicio.'),
        ('abc', '{F} Un grupo pide a la espectadora A que justifique por qué lloró. ¿Qué corresponde?', 'Respetar su reacción, y conversar sobre qué rasgos de la obra pudieron provocarla si ella lo desea', 'Exigirle que se explique frente al curso, aunque no quiera hablar de lo que sintió', 'Decirle que llorar no es una respuesta válida para analizar una obra de teatro', 'Las reacciones personales se respetan y nadie debe exponerse.'),
        ('abc', '¿Qué sesgo hay en «como todos dicen que está buenísima, debe ser excelente»?', 'Dejarse llevar por la opinión del grupo', 'Haber leído el programa antes de la función', 'Querer comparar con otra obra', 'La opinión de otros puede reemplazar el propio análisis.'),
        ('abc', '{F} Quieres convertir tu reacción en juicio. ¿Cuál es el primer paso?', 'Anotar qué rasgos de la obra pudieron provocar la reacción', 'Preguntar qué opinan los demás para igualar su opinión con la del resto del curso', 'Olvidar lo que sentiste para poder ser objetivo y escribir solo sobre los hechos', 'Se parte de la reacción y se busca su causa en la obra.'),
        ('=', 'De 5 espectadores, 2 declaran un vínculo con el elenco. ¿Qué porcentaje declaró un posible sesgo?', '2*100//5', 'Se divide quienes declararon entre el total y se pasa a porcentaje.', ' %'),
        ('abc', '{F} Un compañero dice que A «no sabe de teatro» por haber llorado. ¿Qué corresponde?', 'Responder que una reacción emocional es válida y que lo que se discute es la valoración', 'Estar de acuerdo con él, porque llorar es poco crítico a la hora de valorar una obra', 'Pedir a A que no vuelva a opinar sobre obras, porque se deja llevar por sus emociones', 'Se respeta la reacción y se discute con criterios.'),
    ],
    ctx=('abc', 'Antes de una función, un curso decide anotar en una hoja, sin firma, cómo llegó cada persona (con sueño, con hambre, con ganas) y cualquier vínculo con el elenco. ¿Para qué sirve?', 'Para reconocer sesgos posibles al analizar los juicios después', 'Para decidir quiénes no pueden opinar sobre la obra porque tienen una amistad con el elenco', 'Para saber quién merece una nota más alta en la actividad de análisis del curso', 'Reconocer sesgos ayuda a valorar con honestidad.'),
    sc=[
        ("En Teatro: ¿qué es un juicio estético?", "Una valoración de la obra apoyada en criterios y evidencia", "Se diferencia de la reacción y del gusto."),
        ("¿Qué es un sesgo?", "Un factor que inclina el juicio sin que se note", "Se reconoce para valorar con honestidad."),
        ("¿Se puede valorar bien una obra que no es de nuestro gusto?", "Sí, porque el juicio se apoya en criterios y no en el gusto", "Gusto y juicio son cosas distintas."),
    ],
    op=("Escribe una bitácora de espectador sobre una escena de ejemplo (puede ser inventada o una situación cotidiana). Anota en tres columnas tu reacción, dos rasgos de la escena que la provocaron y un posible sesgo tuyo. Después redacta una frase de juicio que use un criterio y uno de esos rasgos.",
        "Escena: una persona espera en un andén. Reacción: calma e inquietud. Rasgos: la luz baja lentamente y el silencio entre frases. Sesgo: estoy cansada y me gustan las obras tranquilas. Juicio: «el ritmo lento y la luz que baja sostienen bien el propósito de mostrar la espera».",
        ["separa reacción, rasgos y sesgo", "los rasgos son observables", "el juicio usa un criterio y un rasgo", "no expone experiencias personales dolorosas"],
        ["bitácora en tres columnas y una frase de juicio"],
        ["pasar del gusto a la valoración sin evidencia", "ignorar el sesgo"],
        "Pregunta: «¿qué rasgo provocó esa reacción?». Si no hay rasgo, pídele revisar la escena."),
    reinforce="Después de ver una película o serie, anota tu reacción y dos rasgos que la provocaron, sin escribir si es buena o mala.",
    extend="Explica por qué reconocer los propios sesgos hace más confiable un juicio y da un ejemplo propio.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (tres juicios de ejemplo sobre la obra «Cuarto 12», inventados). "
     "J1: «La obra es muy buena.» "
     "J2: «La luz cambia despacio durante toda la obra.» "
     "J3: «La obra logra mostrar la espera (tesis), porque la luz cambia despacio (evidencia) y eso hace sentir el paso del tiempo, que es lo que se espera cuando alguien espera (justificación); aunque algunos momentos se alargan demasiado (matiz).» "
     "Criterio usado en J3: coherencia entre recursos de puesta en escena y propósito.")
build(
    O6, 2, F,
    use="Aprenderé a construir un juicio estético argumentado con cinco partes (tesis, criterio, evidencia, justificación y matiz) y a revisar si cada parte está presente y se conecta con las demás.",
    prior=["Sé separar reacción, gusto y juicio.", "Sé analizar una obra con evidencia.", "Conozco sesgos frecuentes."],
    explain=[
        "Un juicio estético argumentado tiene partes que se pueden revisar. La tesis es la afirmación central: «la obra logra mostrar la espera». El criterio es el aspecto con el que se valora, por ejemplo la coherencia entre recursos y propósito. La evidencia es el rasgo observable de la obra que respalda la tesis: «la luz cambia despacio». La justificación explica por qué esa evidencia cuenta como razón: «eso hace sentir el paso del tiempo, que es lo propio de esperar». El matiz reconoce un límite: «aunque algunos momentos se alargan».",
        "La justificación es la parte que más se olvida. Sin ella, la evidencia queda suelta: se dice un dato y una tesis, pero no se explica la conexión entre ambos. El matiz no debilita el juicio; lo hace honesto, porque reconoce que casi ninguna obra es perfecta ni totalmente fallida. Un juicio con tesis, criterio y evidencia, pero sin justificación ni matiz, queda incompleto.",
        "Un juicio se evalúa por su calidad argumentativa, no por si coincide con el nuestro. Se puede estar en desacuerdo con una tesis y reconocer que está bien argumentada. Se escribe con respeto: se juzga la obra y sus decisiones, no a las personas del elenco ni su cuerpo. Un buen hábito es leer el juicio en voz alta y preguntarse si otra persona que no vio la obra entendería por qué se sostiene.",
    ],
    vocab=[("tesis", "afirmación central de un juicio"), ("criterio", "aspecto con el que se valora una obra"), ("evidencia", "rasgo observable que respalda la tesis"), ("justificación", "explicación de por qué la evidencia cuenta como razón"), ("matiz", "reconocimiento de un límite o de otra posibilidad")],
    worked=[
        ("Completar un juicio", "Tesis: «la escenografía es eficaz». Evidencia: «solo hay una cama y una ventana». ¿Qué justificación falta?", ["Hay que explicar por qué esa evidencia sostiene la tesis.", "Por ejemplo: «los pocos objetos dejan ver el espacio vacío, lo que refuerza la idea de espera»."], "Explicar que los pocos objetos refuerzan la espera"),
        ("Reconocer las partes", "«La obra es lenta (tesis), porque cada escena dura más de lo esperado (evidencia); eso hace perder el ritmo (justificación)». ¿Qué parte falta?", ["Están tesis, evidencia y justificación.", "Falta el criterio explícito y el matiz."], "Criterio y matiz"),
    ],
    mistakes=[("Poner una tesis y una evidencia sin explicar su conexión.", "El lector no sabe por qué esa evidencia sostiene esa tesis.", "Agrega una justificación con «porque» o «lo que significa que»."),
              ("Creer que el matiz debilita el juicio.", "El matiz muestra honestidad y sostiene mejor la tesis.", "Incluye un límite que reconozca lo que no se cumplió.")],
    T=[
        ('abc', 'En un juicio argumentado, ¿qué es la justificación?', 'La explicación de por qué la evidencia cuenta como razón de la tesis', 'El dato observable de la obra que respalda la tesis de quien escribe el juicio', 'La afirmación central del juicio, que resume lo que quien escribe piensa de la obra', 'La justificación conecta evidencia y tesis.'),
        ('abc', '{F} ¿Qué juicio es solo una tesis sin evidencia?', 'J1, «la obra es muy buena»', 'J2, la luz cambia despacio durante toda la obra', 'J3, el juicio completo con las cinco partes', 'J1 no entrega razones ni rasgos observables.'),
        ('abc', '{F} ¿Qué parte tiene J2 y le falta a J1?', 'La evidencia, porque cita el rasgo de la luz que cambia despacio', 'El matiz, porque reconoce un límite de la obra y muestra honestidad en el juicio', 'El criterio explícito de coherencia entre las decisiones de la obra y su propósito', 'J2 agrega evidencia, aunque le faltan otras partes.'),
        ('abc', '{F} En J3, ¿cuál es la evidencia?', 'La luz que cambia despacio', 'La obra logra mostrar la espera', 'Algunos momentos se alargan demasiado', 'La evidencia es el rasgo observable que sostiene la tesis.'),
        ('abc', '{F} En J3, ¿cuál es la tesis?', 'La obra logra mostrar la espera', 'La luz cambia despacio', 'Algunos momentos se alargan demasiado', 'La tesis es la afirmación central del juicio.'),
        ('abc', '{F} En J3, ¿cuál es el matiz?', 'Algunos momentos se alargan demasiado', 'La luz cambia despacio', 'La coherencia entre recursos y propósito', 'El matiz reconoce un límite de la obra.'),
        ('abc', '{F} ¿Qué parte le falta a J2 para estar completo?', 'La tesis, la justificación, el criterio y el matiz', 'Solo el matiz, porque ya tiene tesis, criterio, evidencia y justificación', 'Solo la evidencia, porque lo demás ya está presente en la frase del juicio J2', 'J2 solo entrega un rasgo observable; faltan las demás partes.'),
        ('=', '{F} J3 tiene cinco partes. Si un juicio tiene 3 de esas 5 partes, ¿qué porcentaje de las partes tiene?', '3*100//5', 'Se divide las partes presentes entre las cinco y se pasa a porcentaje.', ' %'),
        ('abc', 'Un estudiante escribe: «la obra es excelente porque tiene buena luz». ¿Qué le falta?', 'Explicar por qué esa luz cuenta como razón de su valoración, y un criterio', 'Eliminar la palabra excelente, porque ninguna obra puede ser valorada de esa manera', 'Repetir con otras palabras que la luz es buena, para que el lector lo crea más', 'Se necesita conectar la luz con el propósito o el criterio.'),
        ('abc', 'Una estudiante dice que el matiz «le quita fuerza al juicio». ¿Qué respuesta es correcta?', 'El matiz hace más honesto el juicio y lo vuelve más creíble', 'Tiene razón; los juicios deben ser absolutos y no admitir ningún límite en lo que dicen', 'El matiz es solo una forma de no comprometerse con ninguna idea sobre la obra', 'Reconocer límites aumenta la credibilidad de la argumentación.'),
        ('abc', '{F} Quieres cambiar el criterio de J3 a «claridad del texto». ¿Qué debe cambiar para mantener la coherencia?', 'La evidencia y la justificación, que deben apoyar ese nuevo criterio', 'Nada, porque el criterio no tiene vínculo con las demás partes', 'Solo la tesis, porque la evidencia y la justificación pueden seguir siendo las mismas', 'Las partes deben estar alineadas con el criterio.'),
        ('=', 'Un curso escribe 24 juicios y 18 de ellos tienen evidencia. ¿Cuántos juicios no tienen evidencia?', '24-18', 'Se restan los juicios con evidencia al total.', ' juicios'),
        ('abc', 'Dos juicios sobre la misma obra tienen tesis opuestas, ambas bien argumentadas. ¿Qué conclusión es adecuada?', 'Ambos pueden ser válidos como juicios fundados y se discuten con respeto', 'Uno debe retirarse del debate, porque dos tesis opuestas no pueden convivir en un curso', 'El juicio de la persona con más experiencia es el correcto y el otro debe corregirse', 'La calidad del argumento no depende de coincidir con la propia tesis.'),
    ],
    ctx=('abc', 'Un curso hace un taller de reseñas. Un grupo entrega frases como «me gustó mucho». Otro entrega frases con tesis, evidencia y justificación. ¿Cuál puede conversar mejor con quien no vio la obra?', 'El segundo, porque su juicio se puede comprender y discutir', 'El primero, porque dice cómo se sintió', 'Ninguno, porque quien no vio la obra no puede opinar', 'Un juicio argumentado se puede evaluar sin haber visto la obra.'),
    sc=[
        ("En Teatro: ¿cuáles son las cinco partes de un juicio argumentado?", "Tesis, criterio, evidencia, justificación y matiz", "Cada parte cumple una función distinta dentro del juicio."),
        ("¿Qué parte conecta la evidencia con la tesis?", "La justificación", "Explica por qué la evidencia cuenta como razón."),
        ("¿Para qué sirve el matiz?", "Para reconocer un límite y hacer más honesto el juicio", "Muestra que la valoración no es absoluta."),
    ],
    op=("Elige una escena de ejemplo (la de la ficha de esta clase o una inventada por ti) y escribe un juicio argumentado de cuatro a seis líneas con tesis, criterio, evidencia, justificación y matiz. Rotula las cinco partes entre paréntesis. No hables de los cuerpos ni de la vida de las personas.",
        "Tesis: la escena muestra la espera con eficacia (tesis). Criterio: coherencia entre recursos y propósito (criterio). Evidencia: el silencio largo entre frases y la luz que baja (evidencia). Justificación: ese silencio y esa luz hacen sentir que el tiempo no avanza, lo propio de esperar (justificación). Matiz: el segundo silencio dura más de lo necesario (matiz).",
        ["incluye las cinco partes", "la evidencia es observable", "la justificación conecta evidencia y tesis", "habla de la obra y no de las personas"],
        ["juicio escrito con las cinco partes rotuladas"],
        ["omitir la justificación", "hablar de cuerpos o de la vida privada"],
        "Pregunta: «¿por qué esa evidencia sostiene tu tesis?». Si no puede explicarlo, pídele agregar la justificación."),
    reinforce="Escribe una tesis y una evidencia sobre un libro, serie o canción, y pide a una persona de tu casa que te diga si falta una justificación.",
    extend="Explica por qué un juicio con justificación se puede discutir con respeto aunque se esté en desacuerdo con su tesis.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (fragmentos de un debate sobre la obra «Cuarto 12», de ejemplo, inventados). "
     "F1: «Esa crítica no vale, porque quien la escribió ni siquiera ha actuado nunca.» "
     "F2: «Todo el curso aplaudió al final, así que la obra tiene que ser excelente.» "
     "F3: «Una reconocida directora dijo que la obra es magistral, así que no hay nada que discutir.» "
     "F4: «Vi una escena lenta, así que toda la obra es lenta.» "
     "F5: «O la obra es perfecta, o es un fracaso total.» "
     "F6: «Aunque la luz funciona bien, la escena final se alarga; por eso creo que la obra es buena, pero mejorable.»")
build(
    O6, 3, F,
    use="Aprenderé a anticipar contraargumentos, a responderlos con respeto y a reconocer falacias frecuentes (ataque a la persona, apelación a la mayoría, apelación a la autoridad, generalización apresurada y falso dilema) en discusiones sobre obras.",
    prior=["Sé armar un juicio con tesis, evidencia y justificación.", "Conozco los sesgos frecuentes.", "Sé separar gusto de juicio."],
    explain=[
        "Un contraargumento es una razón que va en contra de una tesis. Anticiparlo fortalece el juicio: se piensa qué diría alguien que opina distinto y se responde con evidencia. Responder no es ganar, sino mostrar que la tesis sigue en pie o ajustarla. Se hace con tres pasos: reconocer lo valioso del contraargumento, señalar qué evidencia lo limita y, si hace falta, reformular la tesis con un matiz.",
        "Una falacia es un error de razonamiento que parece válido pero no lo es. Ataque a la persona (ad hominem): descalificar a quien opina en vez de revisar su argumento. Apelación a la mayoría: decir que algo es cierto porque muchos lo creen. Apelación a la autoridad: aceptar algo solo porque lo dice alguien famoso, sin revisar su razón. Generalización apresurada: concluir sobre todo a partir de un caso. Falso dilema: presentar solo dos opciones extremas cuando hay más. Una autoridad puede dar razones útiles, pero hay que mirar sus razones y no solo su cargo.",
        "Un debate respetuoso se centra en argumentos y no en personas. Se escucha completo antes de responder, se reconoce cuando alguien tiene razón y se acepta cambiar de opinión si aparece mejor evidencia. Si una discusión se vuelve agresiva o alguien se siente humillado, se detiene y se avisa a una persona adulta de confianza.",
    ],
    vocab=[("contraargumento", "razón que va en contra de una tesis"), ("falacia", "error de razonamiento que parece válido"), ("ataque a la persona", "descalificar a quien opina en vez de revisar su argumento"), ("apelación a la mayoría", "decir que algo es cierto porque muchos lo creen"), ("generalización apresurada", "concluir sobre todo a partir de un solo caso"), ("falso dilema", "presentar solo dos opciones extremas cuando hay más")],
    worked=[
        ("Reconocer una falacia", "«Su opinión no importa, porque tiene 15 años». ¿Qué falacia es?", ["Descalifica a la persona y no revisa el argumento.", "Es un ataque a la persona."], "Ataque a la persona"),
        ("Responder un contraargumento", "Tesis: «la obra muestra bien la espera». Contraargumento: «algunas escenas se alargan». ¿Cómo respondes?", ["Reconozco lo valioso: algunas escenas son largas.", "Reformulo con matiz: «muestra bien la espera, aunque dos escenas podrían acortarse»."], "Reconocer, limitar y matizar la tesis"),
    ],
    mistakes=[("Responder al contraargumento atacando a quien lo dice.", "Es una falacia y no resuelve el desacuerdo.", "Responde a su razón con evidencia."),
              ("Creer que cambiar de opinión es perder.", "Cambiar ante mejor evidencia es señal de buen juicio.", "Ajusta la tesis si aparece una razón más fuerte.")],
    T=[
        ('abc', 'En una discusión, ¿qué es un contraargumento?', 'Una razón que va en contra de una tesis', 'Una opinión que se repite con más fuerza', 'Una pregunta que se hace al final del debate', 'El contraargumento cuestiona una tesis con razones.'),
        ('abc', '{F} ¿Qué falacia es F1?', 'Ataque a la persona, porque descalifica a quien escribe en vez de revisar su argumento', 'Apelación a la mayoría, porque dice que muchas personas creen lo mismo sobre la crítica', 'Generalización apresurada, porque concluye sobre toda la obra a partir de una sola escena', 'F1 no examina la crítica y ataca a su autor.'),
        ('abc', '{F} ¿Qué falacia es F2?', 'Apelación a la mayoría, porque usa los aplausos como prueba de calidad', 'Falso dilema, porque presenta solo dos opciones extremas entre las cuales elegir', 'Ataque a la persona, porque descalifica a quien opina en lugar de revisar su razón', 'La cantidad de personas que aplaude no demuestra la calidad.'),
        ('abc', '{F} ¿Qué falacia es F3?', 'Apelación a la autoridad, porque acepta algo solo por quien lo dice', 'Generalización apresurada, porque saca una conclusión sobre todo a partir de un caso', 'Falso dilema, porque presenta solo dos posibilidades extremas para valorar la obra', 'No revisa las razones de la directora, solo su prestigio.'),
        ('abc', '{F} ¿Qué falacia es F4?', 'Generalización apresurada, porque saca una conclusión de una sola escena', 'Ataque a la persona, porque descalifica a quien opina sin revisar su argumento', 'Apelación a la mayoría, porque dice que muchas personas piensan lo mismo que él', 'Una escena no permite concluir sobre toda la obra.'),
        ('abc', '{F} ¿Qué falacia es F5?', 'Falso dilema, porque presenta solo dos extremos', 'Apelación a la autoridad, porque acepta algo solo por quien lo dice y no por sus razones', 'Ataque a la persona, porque descalifica a quien escribe la crítica sin mirar su argumento', 'Entre perfecta y fracaso hay muchas posibilidades.'),
        ('abc', '{F} ¿Por qué F6 es una buena respuesta a un contraargumento?', 'Reconoce lo que funciona y lo que se alarga, y concluye con un matiz', 'Porque no se compromete con ninguna conclusión y deja la valoración sin decidir', 'Porque repite la tesis sin cambios, aunque aparezca un contraargumento que la limita', 'F6 reconoce el límite y ajusta la valoración.'),
        ('=', '{F} En los 6 fragmentos hay 5 con falacia. Si un debate de 12 fragmentos tuviera la misma proporción, ¿cuántos fragmentos tendrían falacia?', '12*5//6', 'Se mantiene la proporción de 5 de cada 6 sobre 12 fragmentos.', ' fragmentos'),
        ('abc', 'Una estudiante dice: «tu opinión sobre la actuación vale poco, porque eres de otro curso». ¿Qué respuesta es adecuada?', 'Pedir que revise el argumento en lugar de a la persona', 'Responder atacándola también a ella, para que entienda lo que se siente al ser descalificada', 'Dejar de opinar sobre las obras para evitar conflictos con otros cursos del colegio', 'Se responde a las razones y no a la persona.'),
        ('abc', 'Un compañero aclara que una directora famosa elogió la obra, pero también explica en qué rasgos se basa. ¿Cómo se considera?', 'Como un argumento útil, porque entrega razones y no solo prestigio', 'Como una falacia, porque cita a una autoridad aunque explique en qué rasgos se basa', 'Como un ataque a la persona, porque nombra a una directora que no está en la sala', 'La autoridad es útil si se revisan sus razones.'),
        ('abc', 'Dos estudiantes discuten y una se siente humillada por los comentarios sobre ella. ¿Qué corresponde?', 'Detener la discusión, centrarse en los argumentos y avisar a una persona adulta si continúa', 'Seguir la discusión hasta que alguien gane, aunque una persona se sienta humillada', 'Pedir a la estudiante que se retire de la sala para evitar que la discusión continúe', 'El respeto es condición del debate.'),
        ('=', 'En una votación 14 de 20 estudiantes prefieren la obra. Si eso fuera una apelación a la mayoría, ¿qué porcentaje apoya la afirmación?', '14*100//20', 'Se divide los votos entre el total y se pasa a porcentaje.', ' %'),
        ('abc', '{F} Quieres responder a F4 sin caer en otra falacia. ¿Qué haces?', 'Preguntar por otras escenas y revisar la obra completa con evidencia', 'Responder que quien la dice no sabe de teatro y que por eso no debe opinar sobre la obra', 'Decir que toda la obra es rápida, para equilibrar la generalización de quien la dijo', 'Se usa más evidencia y no se ataca a la persona.'),
    ],
    ctx=('abc', 'En una conversación de curso, alguien dice: «los que aplauden de pie siempre tienen razón». ¿Qué falacia es y cómo se responde?', 'Apelación a la mayoría; se responde pidiendo razones específicas', 'Ataque a la persona; se responde con otro ataque, para que el otro entienda la situación', 'Falso dilema; se responde con silencio, porque no hay forma de discutir con quien lo usa', 'Los aplausos no prueban calidad; se piden razones.'),
    sc=[
        ("En Teatro: ¿qué es una falacia?", "Un error de razonamiento que parece válido", "Reconocerla ayuda a argumentar mejor en un debate."),
        ("¿Qué se hace al responder un contraargumento?", "Se reconoce lo valioso, se muestra la evidencia que lo limita y se matiza la tesis", "Responder no es ganar, sino mejorar el juicio."),
        ("¿Qué se hace si una discusión se vuelve agresiva?", "Se detiene y se avisa a una persona adulta de confianza", "El respeto está antes que ganar."),
    ],
    op=("Escribe un breve diálogo de cuatro a seis líneas entre dos estudiantes que discuten sobre una obra inventada. Incluye una falacia y señala cuál es; después reescribe esa línea como respuesta con evidencia. Sin atacar a personas reales.",
        "A: «Esa obra no sirve, porque la hizo un curso chico (ataque a la persona)». B: «Revisemos qué hace la obra». A: «Seguro es buena, porque todos la vieron (apelación a la mayoría)». Reescritura: «la obra usa pocos objetos para mostrar vacío, y eso apoya su propósito».",
        ["cuatro a seis líneas", "incluye una falacia rotulada", "reescribe la línea con evidencia", "no ataca a personas reales"],
        ["diálogo con falacia identificada y reescritura"],
        ["no rotular la falacia", "atacar a una persona en la reescritura"],
        "Pregunta: «¿qué razón da esa línea?». Si no da razón, pídele reescribirla."),
    reinforce="Observa en una conversación familiar o una red una frase que sea falacia y anota cómo la responderías sin atacar a nadie.",
    extend="Explica por qué cambiar de opinión ante mejor evidencia es una fortaleza en un debate sobre arte.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (dos obras de ejemplo y tres juicios, inventados). "
     "Obra A: «Sombras de plaza», de una tradición ficticia de teatro de calle, con máscaras grandes, humor físico y voz muy proyectada, que se presenta al aire libre. "
     "Obra B: «Cuarto 12», de sala cerrada, actuación contenida y luz sutil. "
     "J1: «La obra A es peor, porque sus gestos son exagerados y los de B son naturales.» "
     "J2: «Los gestos amplios de A son coherentes con una plaza y con el humor físico que busca; en B, la actuación contenida es coherente con una sala cerrada y con su propósito de intimidad.» "
     "J3: «Según nuestros criterios actuales, la obra A es poco interesante, porque la gente hoy prefiere cosas más rápidas.»")
build(
    O6, 4, F,
    use="Aprenderé a argumentar juicios estéticos sobre obras de distintas épocas y procedencias, usando criterios internos a la obra o tradición, reconociendo mi mirada y evitando juzgar con criterios ajenos o por prejuicios.",
    prior=["Sé armar un juicio con cinco partes.", "Sé relacionar puesta en escena y contexto.", "Reconozco falacias frecuentes."],
    explain=[
        "Al valorar obras de distintas épocas y procedencias conviene preguntarse con qué criterios se las mide. Los criterios internos nacen del propósito de la obra y de su tradición: una obra de calle se valora por si logra captar al público que pasa y se entiende a distancia. Los criterios externos vienen de otro contexto: si se mide una obra de plaza con las expectativas de una sala cerrada, el juicio resulta injusto. Primero se comprende desde sus propios criterios; después se puede ampliar la mirada con criterios propios y declararlos.",
        "Un error frecuente es el juicio anacrónico, que valora una obra del pasado como si hubiera sido creada hoy, sin considerar sus condiciones. Otro es el juicio por prejuicio, que descalifica una tradición por ser distinta o ajena. También conviene reconocer desde dónde se mira: edad, experiencias, cultura y gustos influyen. Reconocer esa mirada no invalida el juicio; lo hace más honesto.",
        "Comprender el contexto no obliga a aprobar todo. Una obra puede reproducir ideas de su época que hoy se consideran injustas, y se puede criticar su contenido con argumentos, sin dejar de comprender de dónde viene. Se respeta a las comunidades y personas representadas, y nadie queda expuesto o ridiculizado por su origen.",
    ],
    vocab=[("criterio interno", "criterio que nace del propósito y la tradición de la obra"), ("criterio externo", "criterio que viene de otro contexto"), ("juicio anacrónico", "valorar una obra del pasado como si hubiera sido creada hoy"), ("prejuicio", "juicio previo sin conocer ni revisar"), ("mirada propia", "lugar desde el que cada persona valora, con su edad, cultura y gustos")],
    worked=[
        ("Elegir un criterio", "Para valorar una obra de calle, ¿qué criterio interno conviene?", ["Su propósito es captar al público que pasa y entenderse a distancia.", "Un criterio interno es si logra captar y se entiende desde lejos."], "Si capta al público y se entiende a distancia"),
        ("Detectar un juicio anacrónico", "«La obra de hace mucho es mala porque no usa proyecciones». ¿Qué error tiene?", ["Valora con una tecnología que no existía en su contexto.", "Es un juicio anacrónico."], "Juicio anacrónico"),
    ],
    mistakes=[("Medir toda obra con los criterios de las obras que conocemos.", "Cada tradición tiene propósitos y criterios propios.", "Parte de sus criterios y luego amplía con los tuyos."),
              ("Creer que entender el contexto obliga a aprobar todo.", "Se puede comprender y criticar un contenido a la vez.", "Argumenta tu crítica y reconoce el contexto.")],
    T=[
        ('abc', 'En juicio estético, ¿qué es un criterio interno?', 'El que nace del propósito y de la tradición de la obra', 'El que se toma de una obra totalmente distinta', 'El que solo conoce la persona que escribe la crítica', 'Un criterio interno respeta lo que la obra se propone.'),
        ('abc', '{F} ¿Qué error tiene J1?', 'Valora la obra A con los gestos de una sala cerrada, un criterio ajeno a su tradición', 'Usa un criterio interno de la obra A, pero no lo respalda con ninguna evidencia', 'Cita evidencia y justificación suficientes sobre la obra A para sostener su tesis', 'Compara con criterios que no corresponden a la obra de calle.'),
        ('abc', '{F} ¿Por qué J2 es más justo?', 'Porque valora cada obra por su coherencia con su propósito y su contexto', 'Porque dice que ambas obras son iguales y por eso no hace ninguna valoración entre ellas', 'Porque evita toda valoración, de modo que nadie pueda discutir su contenido', 'Aplica criterios comparables sin desconocer el contexto.'),
        ('abc', '{F} ¿Qué problema tiene J3?', 'Usa un criterio actual como si fuera universal y no considera el propósito de la obra A', 'Cita evidencia sobre las máscaras y la voz de la obra A, pero no habla del contexto', 'Respeta la tradición de la obra y la valora con criterios propios de la plaza', 'Es un juicio anacrónico y con prejuicio sobre el gusto actual.'),
        ('abc', '{F} ¿Qué criterio interno sirve para valorar la obra A?', 'Si los gestos y la voz se entienden a distancia en la plaza', 'Si los detalles se aprecian en silencio, desde las primeras filas de una sala cerrada', 'Si usa luz eléctrica con cambios sutiles, que se aprecian desde cerca del escenario', 'La plaza exige que se entienda a distancia.'),
        ('abc', '{F} ¿Qué criterio interno sirve para valorar la obra B?', 'Si la actuación contenida logra intimidad en la sala', 'Si los gestos llegan a quien pasa por la calle', 'Si hay máscaras grandes', 'La sala cerrada permite detalles sutiles.'),
        ('abc', 'Un juicio anacrónico es', 'valorar una obra del pasado como si se hubiera hecho hoy', 'valorar una obra solo por su duración, sin considerar lo que se propone comunicar', 'valorar una obra por su título, sin leerla ni verla en la función o en su ensayo', 'No considera las condiciones de su época.'),
        ('=', '{F} La obra A se presenta 2 veces al día durante 3 días y llegan 40 personas por función. ¿Cuántas personas ven la obra en total?', '2*3*40', 'Se multiplican funciones por días y por personas.', ' personas'),
        ('abc', 'Una estudiante dice que una tradición teatral ajena «es rara». ¿Qué corresponde?', 'Investigar su propósito y su contexto antes de valorarla', 'Descartarla del análisis', 'Compararla con la tradición propia y decir cuál es mejor', 'Lo ajeno se estudia antes de valorarlo.'),
        ('abc', 'Una obra antigua representa a un grupo de personas con ideas que hoy se consideran injustas. ¿Qué es lo más adecuado?', 'Reconocer el contexto y criticar el contenido con argumentos', 'Aprobar todo su contenido para no juzgar la época en que fue creada por sus autores', 'Descartarla sin analizarla, para evitar problemas con quienes la ven hoy como injusta', 'Comprender y criticar son acciones compatibles entre sí.'),
        ('abc', '{F} Quieres comparar justamente las obras A y B. ¿Qué paso corresponde?', 'Aplicar a ambas el mismo criterio, por ejemplo coherencia con el propósito', 'Usar solo los criterios de la obra B para valorar las dos, porque es más reciente', 'Preguntar cuál de las dos obras es más antigua y elegir esa como la mejor', 'Se compara con criterios comunes que consideren cada contexto.'),
        ('=', 'De 30 juicios de un curso, 6 usan solo criterios externos. ¿Qué porcentaje usa criterios internos o mixtos?', '(30-6)*100//30', 'Se resta los juicios externos al total y se pasa a porcentaje.', ' %'),
        ('abc', '{F} Una estudiante señala que su mirada propia valora más la acción rápida. ¿Cómo mejora su juicio?', 'Declarando esa mirada y aplicando criterios internos de la obra', 'Escondiendo su gusto para parecer más objetiva ante el resto del curso', 'Cambiando su gusto por el del grupo, para que su juicio se parezca al de todos', 'Reconocer la mirada propia hace más honesto el juicio.'),
    ],
    ctx=('abc', 'Un curso estudia una obra de teatro tradicional de otra región del país. Algunos dicen que «es aburrida» sin conocerla. ¿Qué decisión conviene?', 'Investigar su propósito y contexto en fuentes confiables y luego argumentar sus juicios', 'Descartarla porque ya se habló lo suficiente y no se cuenta con tiempo para investigar', 'Pedir a un compañero de esa región que explique todo en nombre de su comunidad', 'Se investiga con respeto antes de valorar; nadie debe cargar con explicarlo todo.'),
    sc=[
        ("En Teatro: ¿qué es un juicio anacrónico?", "Valorar una obra del pasado como si hubiera sido creada hoy", "Ignora las condiciones de su época."),
        ("¿Cuál es el primer paso para valorar una obra de otra tradición?", "Comprenderla desde sus propios criterios", "Así el juicio no parte de un prejuicio."),
        ("¿Qué significa declarar mi mirada propia?", "Reconocer desde dónde valoro: gustos, cultura y experiencias", "Hace más honesto y creíble el juicio."),
    ],
    op=("Escribe un juicio argumentado comparando dos obras de ejemplo inventadas de contextos distintos (una de calle y una de sala o dos épocas). Usa un criterio interno para cada una, declara tu mirada propia en una frase y cierra con un matiz. No generalices sobre pueblos o regiones.",
        "Obra 1: de calle, con tambores; criterio interno: capta al público que pasa y se entiende a distancia; evidencia: sus gestos grandes se ven desde lejos. Obra 2: de sala; criterio interno: logra intimidad; evidencia: la luz baja y el silencio. Mi mirada: me gusta más el teatro tranquilo. Matiz: la obra 1 alarga un cambio de escena.",
        ["criterio interno para cada obra", "declara su mirada propia", "incluye evidencia y matiz", "no generaliza sobre pueblos o regiones"],
        ["juicio comparado con mirada declarada"],
        ["usar el mismo criterio ajeno para todas las obras", "generalizar sobre una cultura"],
        "Pregunta: «¿qué se propone esa obra y con qué criterio la valoras?». Si el criterio no corresponde, pídele cambiarlo."),
    reinforce="Elige dos tipos de música o de juego muy distintos que conozcas y escribe un criterio interno para valorar cada uno.",
    extend="Explica por qué se puede comprender el contexto de una obra y a la vez criticar una idea de su época sin caer en un juicio anacrónico.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (borrador de reseña de ejemplo, inventado). Obra «Cuarto 12». "
     "Párrafo 1 (síntesis): «Una persona espera una visita en un cuarto con una cama y una ventana.» "
     "Párrafo 2 (análisis): «La luz cambia despacio y la actuación es contenida.» "
     "Párrafo 3 (juicio): «La obra logra mostrar la espera, porque la luz y el ritmo hacen sentir el paso de las horas; aunque dos escenas se alargan, el efecto general se sostiene.» "
     "Párrafo 4 (cierre): «Es una obra para quien aprecia el ritmo lento. El actor que hace al personaje es feo y torpe, y no debería seguir actuando.» "
     "Créditos: obra de una compañía ficticia, función de ejemplo; reseña escrita por un grupo del curso.")
build(
    O6, 5, F,
    use="Aprenderé a escribir y revisar una reseña crítica con síntesis, análisis, juicio argumentado y cierre, a mantener un tono respetuoso con la obra y las personas, y a atribuir lo que se cita.",
    prior=["Sé construir un juicio con cinco partes.", "Sé reconocer falacias.", "Sé citar fuentes."],
    explain=[
        "Una reseña crítica es un texto breve que informa y valora una obra para un lector que no la vio. Tiene una estructura: título y datos de la obra (nombre, compañía, lugar y fecha), una síntesis neutral de qué trata sin contar todo el final, un análisis de dos o tres decisiones importantes con evidencia, un juicio argumentado con su tesis y su matiz, y un cierre breve que oriente al lector sobre a quién puede interesarle. Debe ser clara, ordenada y proporcionada: el juicio no debe ocupar todo el espacio ni quedar sin respaldo.",
        "El tono importa. La reseña habla de la obra y de sus decisiones, no de la apariencia, el cuerpo o la vida de las personas que actúan. Una frase como «el actor es feo» no es crítica: es una agresión. Se evitan las burlas, los adjetivos humillantes y las predicciones sobre el futuro de alguien. Cuando se critica, se hace con precisión y con una sugerencia posible. Si la obra la realizó un grupo escolar, se cuida aún más no exponer a nadie.",
        "Antes de publicar, la reseña se revisa: se verifica que cada afirmación tenga evidencia, que no haya falacias, que las citas estén atribuidas y que se haya pedido permiso si se incluyen imágenes. Se recibe retroalimentación de pares y se decide qué cambiar. Publicar es una decisión del grupo, y si alguien de la obra pide corregir un dato, se atiende con apertura.",
    ],
    vocab=[("reseña crítica", "texto breve que informa y valora una obra para quien no la vio"), ("síntesis", "resumen neutral de lo que trata la obra"), ("cierre", "párrafo final que orienta al lector sobre a quién puede interesarle"), ("tono", "actitud con que se escribe: respetuosa o agresiva, por ejemplo"), ("atribución", "indicar de quién es un dato, una cita o una idea")],
    worked=[
        ("Corregir un tono", "Una reseña dice: «la actriz es pésima y tiene voz fea». ¿Cómo se corrige?", ["Habla de la persona y de su voz y no de las decisiones.", "Se reemplaza por: «la proyección no alcanza el fondo en la segunda escena; se podría trabajar con ejercicios de respiración»."], "Hablar de las decisiones y proponer una mejora"),
        ("Ordenar una reseña", "Ordena las partes: cierre, juicio, síntesis, análisis. ¿En qué orden se escriben?", ["Primero informa qué trata la obra: síntesis.", "Luego analiza decisiones con evidencia, después juzga y al final cierra."], "Síntesis, análisis, juicio y cierre"),
    ],
    mistakes=[("Hablar de la apariencia o el cuerpo de quienes actúan.", "Daña a las personas y no dice nada de las decisiones de la obra.", "Describe las decisiones de actuación y su efecto."),
              ("Contar todo el final de la obra en la síntesis.", "Le quita al lector la posibilidad de verla con sorpresa.", "Cuenta lo necesario para situar al lector.")],
    T=[
        ('abc', 'En una reseña, ¿qué función cumple la síntesis?', 'Informar al lector de qué trata la obra, sin contar todo el final', 'Dar el juicio final de la obra y decir si el lector debe verla o no verla', 'Presentar los créditos de la compañía, con los nombres de todas las personas del elenco', 'La síntesis sitúa al lector para entender el análisis.'),
        ('abc', '{F} ¿Qué parte de la reseña es el párrafo 3?', 'El juicio argumentado, con tesis, evidencia y matiz', 'La síntesis neutral de la obra, que cuenta lo que trata sin hacer una valoración', 'El cierre dirigido al lector, que cuenta a quién le puede interesar la obra', 'Contiene la valoración con evidencia y un matiz.'),
        ('abc', '{F} ¿Qué parte del borrador debe corregirse por su tono?', 'La segunda oración del párrafo 4, porque agrede a una persona', 'El párrafo 1, porque cuenta la historia con demasiados detalles de lo que ocurre', 'El párrafo 2, porque describe la luz y la actuación con adjetivos muy fuertes', 'Esa oración juzga a una persona y no la decisión de actuación.'),
        ('abc', '{F} ¿Cómo se reescribe esa oración de manera respetuosa?', '«La actuación podría ganar variedad de ritmo en las escenas largas»', '«El actor tiene mala voz y debería cambiar de oficio antes de volver a actuar»', '«Nadie debería ver esta obra, porque el elenco no cuidó nada de lo que hizo»', 'La reescritura habla de la decisión y propone una mejora.'),
        ('abc', '{F} ¿Qué falta en el párrafo 2 para ser un buen análisis?', 'Relacionar la luz y la actuación con su efecto o su función', 'Agregar adjetivos sobre la belleza de los actores', 'Incluir el final de la obra', 'Un análisis une rasgo y efecto.'),
        ('abc', '{F} ¿Qué dato falta en el borrador para identificar la obra?', 'La fecha y el lugar de la función', 'El nombre completo de cada integrante del elenco', 'Un resumen del final de la obra', 'Los datos de la obra incluyen lugar y fecha, que no están completos.'),
        ('=', '{F} El borrador tiene 4 párrafos. Si cada uno tarda 2 minutos en leerse en voz alta, ¿cuántos minutos dura la lectura?', '4*2', 'Se multiplican los párrafos por el tiempo de cada uno.', ' minutos'),
        ('abc', 'Un grupo quiere publicar su reseña en el sitio del colegio con una foto del elenco. ¿Qué paso corresponde?', 'Pedir consentimiento a quienes aparecen, y a apoderados si son menores', 'Publicarla y retirar la foto después, solo si alguna persona del elenco lo reclama', 'Subirla al sitio del colegio porque es una actividad escolar y la foto es del curso', 'Se pide consentimiento antes de publicar imágenes.'),
        ('abc', '{F} Un compañero propone cerrar con «no vayan nunca a ver esta compañía». ¿Qué problema tiene?', 'Es una descalificación sin argumentos que no orienta al lector', 'Es demasiado breve para cerrar una reseña y debería contar el final de la obra', 'Es demasiado largo para un cierre y debería ocupar un párrafo completo', 'El cierre orienta; descalificar sin razones no cumple esa función.'),
        ('abc', 'Una estudiante incluye en la reseña una frase de otra crítica sin cita. ¿Qué es esto?', 'Plagio; se debe citar con atribución', 'Una síntesis, porque la frase es breve', 'Una paráfrasis, aunque sea exacta', 'Una frase ajena exige atribución clara de su autoría.'),
        ('abc', '{F} El grupo quiere recibir retroalimentación sobre la reseña. ¿Qué es lo más útil?', 'Que un par señale qué parte tiene evidencia, qué parte no y cómo se oye el tono', 'Que un par cambie la reseña a su manera, para que quede mejor escrita en un solo intento', 'Que nadie la lea antes de publicarla, para evitar críticas que desanimen al grupo', 'La retroalimentación descriptiva ayuda a revisar con criterio.'),
        ('=', 'Una reseña de 200 palabras dedica 30 a la síntesis, 70 al análisis y 60 al juicio. ¿Cuántas palabras quedan para el cierre?', '200-(30+70+60)', 'Se resta del total lo usado en las otras partes.', ' palabras'),
        ('abc', 'Una integrante de la compañía pide corregir un dato equivocado de la reseña. ¿Qué hace el grupo?', 'Revisar el dato y corregirlo con apertura si está equivocado', 'Negarse a corregir el dato, porque la reseña ya fue publicada y no se puede cambiar', 'Ignorar el mensaje de la integrante, para evitar discusiones con la compañía sobre la reseña', 'Corregir un error es parte de un buen trabajo crítico.'),
    ],
    ctx=('abc', 'Un curso escribe reseñas de la función de otro curso. Una estudiante se siente muy mal porque en una reseña se burlan de su voz. ¿Qué corresponde?', 'Retirar la burla, conversar con quien la escribió y avisar a una persona adulta si continúa', 'Dejar la reseña tal cual y pedirle a la estudiante que se acostumbre a las críticas', 'Responder con una burla sobre quien escribió la reseña, para que sienta lo mismo', 'El trato dañino se corrige y se informa a un adulto.'),
    sc=[
        ("En Teatro: ¿cuál es el orden de una reseña crítica?", "Síntesis, análisis, juicio argumentado y cierre", "Va de informar a valorar y orientar."),
        ("¿De qué debe hablar la crítica de una actuación?", "De las decisiones de actuación y su efecto, no de la persona", "Así se cuida el respeto hacia las personas."),
        ("¿Qué se pide antes de publicar una reseña con fotos?", "El consentimiento de quienes aparecen", "Cada persona decide sobre su imagen."),
    ],
    op=("Escribe una reseña de ejemplo de seis a ocho líneas sobre una obra inventada (o sobre la escena de una obra del cuaderno). Incluye título con datos, síntesis, análisis con evidencia, juicio con tesis y matiz, y un cierre respetuoso. Revisa con una lista: ¿hay evidencia?, ¿hay falacias?, ¿se cuida a las personas?",
        "«El último tren» (compañía ficticia, sala pequeña). Síntesis: una mujer espera en un andén. Análisis: la luz baja y los silencios largos muestran la espera. Juicio: logra transmitir el paso del tiempo (tesis), porque los silencios sostienen la tensión (evidencia); el final se alarga un poco (matiz). Cierre: recomendable para quien disfruta del ritmo lento. Revisión: cumple con evidencia y respeto.",
        ["incluye todas las partes de una reseña", "el juicio tiene tesis, evidencia y matiz", "el tono es respetuoso", "no habla de cuerpos ni apariencias"],
        ["reseña completa y lista de revisión"],
        ["agredir a una persona", "contar todo el final"],
        "Pregunta: «¿qué decisión critica esta frase?». Si critica a una persona, pídele reescribirla."),
    reinforce="Escribe tres líneas de reseña sobre una película o serie, sin hablar de la apariencia de nadie.",
    extend="Explica por qué una crítica respetuosa y precisa puede ayudar más a una compañía que una burla, y da un ejemplo.",
)
