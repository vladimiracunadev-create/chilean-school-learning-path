"""Artes visuales, audiovisuales y multimediales 3.º y 4.º medio HC: OAC-05 (argumentar juicios estéticos) y OAC-06 (evaluar críticamente procesos y resultados). Obras y casos inventados; sin imágenes reales."""
from __future__ import annotations

from hc_avam_common import build

O5 = "AR-AVAM-3y4-OAC-05"
O6 = "AR-AVAM-3y4-OAC-06"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (obra inventada, descrita por escrito). «Faros»: cinco figuras de cartón pintadas de blanco, de 40, 60, 80, 100 y 120 cm de alto, en fila de menor a mayor sobre una tela azul; cada una tiene una ventana recortada arriba. "
     "Afirmación A: «No me gusta el blanco.» "
     "Afirmación B: «Es la mejor obra del año porque todos lo dicen.» "
     "Afirmación C: «El orden de menor a mayor guía la mirada hacia la derecha y refuerza la idea de crecer; por eso la composición es coherente.» "
     "Afirmación D: «Me parece triste porque las ventanas están vacías.»")
build(
    O5, 1, F,
    use="Aprenderé a distinguir gusto, opinión y juicio estético, y a reconocer qué hace que un juicio esté argumentado.",
    prior=["Sé analizar una obra con descripción e interpretación.", "Sé identificar evidencias en una obra.", "Sé que dos personas pueden ver una obra de modo distinto."],
    explain=[
        "El gusto es una preferencia personal («no me gusta el blanco»): no necesita justificarse, pero tampoco sirve para convencer a nadie de que una obra es buena o mala. Una opinión es lo que alguien piensa de algo, con o sin razones. Un juicio estético es una valoración de la obra que se apoya en un análisis, en criterios y en evidencias visibles, y que otra persona puede revisar.",
        "Un juicio estético argumentado tiene tres partes: una afirmación (qué valoro), un criterio (con qué lo valoro, como coherencia, originalidad o expresividad) y una evidencia (qué detalle de la obra lo muestra). Decir «es la mejor porque todos lo dicen» no es un juicio argumentado: la popularidad no dice nada sobre la obra misma. Tampoco lo es «me gusta», aunque sea sincero.",
        "Argumentar no exige que todas las personas coincidan: dos juicios distintos pueden estar bien fundamentados. Lo que se exige es que cada uno se apoye en la obra y respete a las demás personas. Un juicio puede cambiar si aparecen razones nuevas.",
    ],
    vocab=[("gusto", "preferencia personal"), ("opinión", "lo que alguien piensa, con o sin razones"), ("juicio estético", "valoración de una obra apoyada en análisis, criterios y evidencias"), ("criterio", "cualidad con la que se valora una obra"), ("evidencia", "detalle de la obra que respalda una afirmación"), ("argumentar", "apoyar una afirmación con razones y evidencias")],
    worked=[
        ("Clasificar una afirmación", "Clasifica la afirmación A de la ficha.", ["Habla de una preferencia personal por un color, sin criterio ni evidencia de la obra.", "Es un gusto."], "Un gusto"),
        ("Reconocer un juicio argumentado", "¿Por qué la afirmación C es un juicio argumentado?", ["Tiene una afirmación (la composición es coherente), un criterio (coherencia) y una evidencia (el orden de menor a mayor).", "Otra persona puede revisarlo mirando la obra."], "Tiene afirmación, criterio y evidencia"),
    ],
    mistakes=[("Escribir «es la mejor obra porque a todos les gusta» como juicio estético.", "La popularidad no es una razón sobre la obra.", "Apóyate en un criterio y una evidencia visible."),
              ("Creer que si no hay una respuesta correcta, cualquier juicio vale igual.", "Los juicios mejor fundamentados son más útiles y convincentes.", "Fundamenta con evidencia y criterio, y revisa si otro argumento es más sólido.")],
    T=[
        ('abc', '¿Qué es un juicio estético?', 'Una valoración de la obra apoyada en análisis, criterios y evidencias', 'Una preferencia personal que no necesita razones', 'Una norma que todos deben aceptar', 'El juicio estético se fundamenta; no es un gusto ni una norma.'),
        ('abc', '{F} ¿Cuál afirmación contiene a la vez un criterio y una evidencia de la obra?', 'La afirmación C', 'La afirmación A', 'La afirmación B', 'Solo C nombra un criterio (coherencia) y una evidencia (el orden de menor a mayor).'),
        ('abc', '{F} ¿Por qué B no es un juicio argumentado?', 'Porque se apoya en lo que dicen otros y no en la obra', 'Porque usa la palabra mejor', 'Porque es demasiado larga', 'La popularidad no es una evidencia de la obra.'),
        ('abc', '{F} ¿Qué criterio usa la afirmación C?', 'La coherencia de la composición', 'El precio de la obra', 'La opinión de la mayoría', 'C valora la composición por su coherencia con la idea de crecer.'),
        ('abc', '{F} ¿Qué evidencia respalda la afirmación C?', 'Las figuras ordenadas de 40 a 120 cm, de menor a mayor', 'El hecho de que sea blanca', 'Que la obra está expuesta en una sala', 'La evidencia es el orden de alturas descrito en la ficha.'),
        ('=', '{F} Cada figura es 20 cm más alta que la anterior. Si la serie siguiera desde 40 cm hasta 160 cm, ¿cuántas figuras tendría?', '(160-40)//20+1', 'Se calcula cuántos saltos de 20 hay entre 40 y 160 y se suma la primera figura.', ' figuras'),
        ('abc', '{F} ¿Cómo se clasifica la afirmación D?', 'Como una interpretación personal con un detalle de apoyo, que necesitaría un criterio para ser un juicio completo', 'Como un juicio completo y cerrado', 'Como un dato objetivo', 'D se apoya en un detalle (las ventanas vacías), pero falta el criterio de valoración.'),
        ('abc', '{F} ¿Cómo se podría convertir A en un juicio más útil?', 'Explicando qué criterio cumple o no el blanco: por ejemplo, que unifica las cinco figuras', 'Repitiendo «no me gusta» con más fuerza', 'Agregando que a la mayoría tampoco le gusta', 'Un juicio útil nombra un criterio y una evidencia, aunque el gusto personal sea otro.'),
        ('=', 'En una clase, 9 de los 12 textos de juicio entregados incluyen una evidencia de la obra. ¿Qué porcentaje de los textos la incluye?', '9*100//12', 'Se calcula cuántos de cada 100 textos la incluyen.', ' %'),
        ('abc', 'Dos estudiantes valoran distinto una misma obra y ambos citan evidencias. ¿Qué corresponde pensar?', 'Que pueden existir dos juicios bien fundamentados y se comparan sus argumentos', 'Que alguien miente', 'Que la obra no tiene valor', 'Distintos juicios pueden ser sólidos si se apoyan en la obra.'),
        ('abc', 'Un compañero dice que la obra es buena porque es famosa. ¿Qué respondes?', 'Que la fama no es una cualidad de la obra misma, y que necesita un criterio y una evidencia', 'Que tiene razón porque la fama prueba la calidad', 'Que no se puede opinar', 'La fama no equivale a un criterio estético.'),
        ('abc', 'Después de oír un argumento sólido de otra persona, cambias de juicio. ¿Cómo se entiende eso?', 'Como una señal de que revisaste tus razones con apertura', 'Como una debilidad', 'Como una derrota', 'Un juicio puede cambiar si aparecen razones nuevas.'),
        ('abc', '¿Qué diferencia hay entre gusto y juicio estético?', 'El gusto es una preferencia y el juicio se apoya en análisis, criterios y evidencias', 'No hay diferencia', 'El juicio es siempre una preferencia compartida por todos', 'El juicio se fundamenta en la obra; el gusto no necesita hacerlo.'),
    ],
    ctx=('abc', 'Al analizar «Faros», una estudiante escribe: «Me parece una obra expresiva, porque las ventanas vacías de las figuras generan la sensación de espera, y eso conecta con la idea de crecer». ¿Qué tiene de bueno su juicio?', 'Nombra un criterio (expresividad) y lo apoya en una evidencia de la obra', 'Solo expresa que le gustó', 'Se apoya en que todos opinan igual', 'Tiene afirmación, criterio y evidencia visible.'),
    sc=[
        ("En Artes: ¿qué es un juicio estético?", "Una valoración apoyada en análisis, criterios y evidencias", "Se diferencia del gusto porque se fundamenta."),
        ("¿Cuáles son las tres partes de un juicio argumentado?", "Afirmación, criterio y evidencia", "Con ellas otra persona puede revisarlo."),
        ("¿La popularidad prueba la calidad de una obra?", "No", "La popularidad no dice nada sobre la obra misma."),
    ],
    op=("Elige una obra inventada tuya o descrita por escrito y escribe tres frases: un gusto, una interpretación con un detalle y un juicio argumentado con afirmación, criterio y evidencia. Rotula cada una.",
        "Obra: un dibujo de una bicicleta contra una pared. Gusto: me gustan los tonos azules. Interpretación: la bicicleta sola podría sugerir espera, porque no hay nadie cerca. Juicio: la composición es coherente (criterio) porque la bicicleta a un lado deja espacio vacío que refuerza la espera (evidencia).",
        ["distingue gusto, interpretación y juicio", "el juicio tiene criterio y evidencia", "usa detalles de la obra"],
        ["hoja con tres frases rotuladas"],
        ["usar la popularidad como razón", "no citar evidencia"],
        "Pregunta: «¿qué criterio y qué evidencia usaste?». Si falta alguno, pídele que lo agregue."),
    reinforce="Escribe una frase de gusto y una de juicio sobre un afiche que veas esta semana.",
    extend="Explica por qué un juicio estético bien fundamentado puede convencer a alguien que tiene un gusto distinto.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (obra inventada, descrita por escrito). «Mesa para tres»: fotografía ficticia de tres sillas de madera vacías alrededor de una mesa, iluminadas por la luz de una ventana; sobre la mesa hay una sola taza. "
     "Borrador 1: «Es buena porque sí.» "
     "Borrador 2: «La obra comunica ausencia, porque hay tres sillas y una sola taza, lo que hace notar que faltan personas.» "
     "Borrador 3: «Hay tres sillas y una taza.» "
     "Modelo de argumento: AFIRMACIÓN (qué valoro) + EVIDENCIA (qué detalle de la obra lo muestra) + RAZÓN (por qué esa evidencia sostiene la afirmación).")
build(
    O5, 2, F,
    use="Aprenderé a construir un argumento estético con afirmación, evidencia y razón, y a reconocer cuándo falta alguna de las tres.",
    prior=["Sé distinguir gusto y juicio.", "Sé identificar evidencias en una obra.", "Sé usar la palabra «porque» con una razón."],
    explain=[
        "Un argumento estético tiene tres componentes. La afirmación dice qué valoras o interpretas de la obra (por ejemplo, que comunica ausencia). La evidencia es el detalle visible que se puede señalar (tres sillas y una taza). La razón explica por qué esa evidencia sostiene la afirmación (la diferencia hace notar que faltan personas). Si falta la razón, la evidencia queda suelta; si falta la evidencia, la afirmación queda sin apoyo.",
        "Para escribir un buen argumento se usan conectores como porque, ya que, por eso o lo que muestra que. Se cita la obra con precisión, se evita exagerar y se escribe en oraciones cortas. Si un argumento no convence, se puede mejorar agregando una evidencia más, explicando mejor la razón o ajustando la afirmación para que no sea demasiado grande.",
        "También conviene preguntarse: ¿qué diría alguien que piensa lo contrario? Anticipar una objeción fortalece el argumento, porque obliga a revisar si las evidencias son suficientes. Escribir con respeto es parte del argumento: se critica la obra o la idea, no a la persona.",
    ],
    vocab=[("afirmación", "lo que se valora o interpreta de una obra"), ("evidencia", "detalle visible que respalda la afirmación"), ("razón", "explicación de por qué la evidencia sostiene la afirmación"), ("conector", "palabra que une una idea con su razón"), ("objeción", "argumento contrario")],
    worked=[
        ("Reconocer los componentes", "Identifica la afirmación, la evidencia y la razón del borrador 2.", ["Afirmación: la obra comunica ausencia.", "Evidencia: tres sillas y una sola taza. Razón: la diferencia hace notar que faltan personas."], "Afirmación: comunica ausencia; evidencia: tres sillas y una taza; razón: faltan personas"),
        ("Detectar lo que falta", "El borrador 3 dice «Hay tres sillas y una taza». ¿Qué le falta?", ["Describe un detalle (evidencia).", "Falta una afirmación y la razón que une el detalle con ella."], "Le faltan la afirmación y la razón"),
    ],
    mistakes=[("Poner una evidencia y esperar que la razón se entienda sola.", "El lector no sabe por qué esa evidencia sostiene la afirmación.", "Agrega una frase que explique la razón con un conector."),
              ("Hacer afirmaciones enormes con una evidencia diminuta.", "No hay suficiente apoyo para algo tan grande.", "Reduce la afirmación o suma más evidencias.")],
    T=[
        ('abc', '¿Qué es la evidencia en un argumento estético?', 'Un detalle visible de la obra que respalda la afirmación', 'La opinión de alguien famoso', 'Una preferencia personal', 'La evidencia está en la obra y se puede señalar.'),
        ('abc', '{F} ¿Cuál es la evidencia del borrador 2?', 'Hay tres sillas y una sola taza', 'La luz de la ventana', 'El nombre de la obra', 'La ficha lo expresa en el borrador 2.'),
        ('abc', '{F} ¿Qué falta en el borrador 1?', 'Afirmación concreta, evidencia y razón', 'Nada, está completo', 'Solo la firma', 'Dice «es buena porque sí»: no hay evidencia ni razón.'),
        ('abc', '{F} ¿Qué le falta al borrador 3 para ser un argumento?', 'Una afirmación y una razón', 'Más sillas', 'Un nombre de autor', 'Solo presenta una evidencia, sin afirmación ni razón.'),
        ('=', '{F} Un argumento se arma con 3 componentes. Si un texto tiene 4 argumentos completos, ¿cuántos componentes hay?', '4*3', 'Se multiplica la cantidad de argumentos por los componentes de cada uno.', ' componentes'),
        ('abc', '{F} ¿Qué conector usa el borrador 2 para unir la afirmación con la evidencia?', 'Porque', 'Pero', 'Sin embargo', 'La palabra porque introduce la razón.'),
        ('abc', '{F} ¿Qué agregarías al borrador 3 para mejorarlo?', 'La afirmación «la obra comunica ausencia» y la razón «porque faltan personas»', 'Más adjetivos como lindo y bonito', 'Una frase que diga que es famosa', 'Se completa con afirmación y razón ligadas a la evidencia.'),
        ('abc', '{F} Alguien afirma que la fotografía muestra «la tristeza de toda una sociedad». ¿Cuál es el problema?', 'La afirmación es demasiado grande para la evidencia que da la obra', 'Es muy corta', 'Nadie puede opinar sobre sociedad', 'Una afirmación debe ser proporcional a la evidencia.'),
        ('=', 'Un estudiante tiene 2 evidencias para cada una de sus 3 afirmaciones. ¿Cuántas evidencias usa?', '2*3', 'Se multiplica el número de afirmaciones por las evidencias de cada una.', ' evidencias'),
        ('abc', '{F} Una objeción posible al borrador 2 es que una sola taza también podría sugerir soledad deseada. ¿Cómo se responde bien?', 'Reconociendo que es posible y agregando evidencia, como las tres sillas vacías, que sugiere ausencia', 'Ignorando la objeción', 'Diciendo que esa persona no entiende arte', 'Se responde con argumentos y evidencia, sin atacar a la persona.'),
        ('abc', 'Para escribir con respeto un argumento, ¿qué se hace?', 'Criticar la obra o la idea, no a la persona', 'Descalificar a quien piensa distinto', 'Usar sarcasmo hacia la autora', 'La crítica se dirige a la obra y a las ideas.'),
        ('abc', 'Al argumentar sobre una obra real que no está delante, ¿qué conviene?', 'Volver a mirar la obra y citar detalles verificables', 'Citar detalles de memoria sin revisar', 'Inventar detalles que suenen bien', 'Los detalles se citan desde la obra para no inventar.'),
        ('abc', '¿Cuál es un conector adecuado para unir una afirmación con su razón?', 'Ya que', 'Aunque nadie lo crea', 'De todos modos', 'Ya que introduce una razón; los otros no.'),
    ],
    ctx=('abc', 'Una estudiante escribe sobre «Mesa para tres»: «La luz de la ventana crea un ambiente cálido, ya que ilumina las sillas desde un solo lado, por eso la obra puede sentirse acogedora a pesar de la ausencia». ¿Qué cumple bien?', 'Tiene afirmación, evidencia (luz desde un lado) y razón con conectores', 'Solo describe la obra', 'Solo dice que le gustó', 'El texto organiza afirmación, evidencia y razón.'),
    sc=[
        ("En Artes: ¿qué es la razón en un argumento?", "La explicación de por qué la evidencia sostiene la afirmación", "Une la evidencia con la afirmación."),
        ("¿Cuáles son los tres componentes de un argumento?", "Afirmación, evidencia y razón", "Con ellos el argumento queda completo."),
        ("¿Qué conector sirve para introducir una razón?", "Porque", "Introduce la explicación de la afirmación."),
    ],
    op=("Elige una obra inventada tuya y escribe un argumento de tres frases con afirmación, evidencia y razón, usando al menos dos conectores. Escribe después una objeción posible y cómo la responderías.",
        "Obra: dibujo de una escalera que sube hasta una puerta cerrada. Afirmación: el dibujo comunica espera. Evidencia: la escalera llega a una puerta cerrada. Razón: ya que la puerta no se abre, la subida no termina en un destino. Objeción: la puerta podría abrirse después. Respuesta: la obra solo muestra el momento anterior.",
        ["afirmación, evidencia y razón", "usa conectores", "responde una objeción con respeto"],
        ["hoja con el argumento y la objeción"],
        ["no dar la razón", "afirmación demasiado grande"],
        "Pregunta: «¿qué razón une la evidencia con tu afirmación?». Si falta, pídele que la escriba."),
    reinforce="Escribe un argumento de dos frases sobre una imagen de tu cuaderno o de tu casa, con una afirmación y una evidencia.",
    extend="Explica por qué anticipar una objeción hace más sólido un argumento.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (obra inventada, descrita por escrito). «Mar de relojes»: dibujo ficticio de cientos de relojes pequeños, dibujados con trazo fino azul sobre fondo blanco, ordenados en olas; cada reloj marca una hora distinta. "
     "Propósito declarado de la autora ficticia: hablar del paso del tiempo. "
     "Criterios de valoración usados por el curso: COHERENCIA (las decisiones sirven al propósito), ORIGINALIDAD (propone algo propio), EXPRESIVIDAD (produce un efecto o una emoción), MANEJO DE RECURSOS (control del trazo, el color y la composición). "
     "Frases de estudiantes: F1: «Las horas distintas refuerzan la idea de tiempo que se mueve.» F2: «Pensé que dibujar relojes en olas es una combinación poco habitual en el curso.» F3: «El trazo azul es parejo y no se corre en ningún reloj.» F4: «Me recordó un día de lluvia y me dio calma.»")
build(
    O5, 3, F,
    use="Aprenderé a usar criterios estéticos (coherencia, originalidad, expresividad y manejo de recursos) para fundamentar un juicio, eligiendo criterios adecuados al propósito.",
    prior=["Sé armar un argumento con afirmación, evidencia y razón.", "Sé identificar el propósito de una obra.", "Sé separar gusto de juicio."],
    explain=[
        "Un criterio estético es una cualidad con la que se valora una obra. Algunos criterios frecuentes son la coherencia (las decisiones visuales sirven al propósito de la obra), la originalidad (la obra propone algo propio y no repite un modelo), la expresividad (produce un efecto o una emoción) y el manejo de recursos (control de la línea, el color, la composición o la técnica). Cada criterio se usa con una evidencia de la obra.",
        "Los criterios deben ser adecuados al propósito de la obra. Si una obra busca hablar del paso del tiempo, es razonable preguntar si sus decisiones lo refuerzan (coherencia). No es razonable criticarla por «no tener color» si el color no formaba parte de lo que quería lograr. Se pueden usar varios criterios y explicar cuál pesa más en el juicio.",
        "Un juicio completo puede decir, por ejemplo: «La obra es coherente porque las horas distintas refuerzan la idea de tiempo; su manejo del trazo es parejo, aunque la repetición reduce la originalidad». Reconocer fortalezas y debilidades hace al juicio más creíble. Los juicios sobre obras de otras personas se hacen con respeto.",
    ],
    vocab=[("coherencia", "relación entre las decisiones visuales y el propósito"), ("originalidad", "propuesta propia y no repetida de un modelo"), ("expresividad", "capacidad de producir un efecto o emoción"), ("manejo de recursos", "control de la línea, el color, la composición o la técnica"), ("fortaleza", "aspecto en que la obra se logra bien"), ("debilidad", "aspecto que podría mejorar")],
    worked=[
        ("Ubicar una frase en un criterio", "La frase F1 dice que las horas distintas refuerzan la idea de tiempo. ¿Qué criterio usa?", ["Relaciona una decisión (horas distintas) con el propósito (tiempo).", "Eso es coherencia."], "Coherencia"),
        ("Elegir un criterio adecuado", "Alguien critica «Mar de relojes» porque «no tiene color». ¿Por qué no es un criterio adecuado?", ["El propósito era hablar del paso del tiempo, y el trazo azul sobre blanco lo hace con pocos colores.", "La falta de color no contradice el propósito."], "No se relaciona con el propósito declarado"),
    ],
    mistakes=[("Juzgar una obra con criterios que no tienen que ver con su propósito.", "Se critica algo que la autora no se propuso.", "Elige criterios coherentes con lo que la obra quería lograr."),
              ("Dar solo elogios o solo críticas.", "Un juicio parcial resulta poco creíble.", "Reconoce una fortaleza y una debilidad, ambas con evidencia.")],
    T=[
        ('abc', '¿Qué es la coherencia como criterio?', 'La relación entre las decisiones visuales y el propósito de la obra', 'El parecido con otra obra famosa', 'El tamaño de la obra', 'La coherencia mide si las decisiones sirven al propósito.'),
        ('abc', '{F} ¿Qué criterio usa la frase F2?', 'Originalidad', 'Coherencia', 'Manejo de recursos', 'F2 habla de una combinación poco habitual, es decir, de originalidad.'),
        ('abc', '{F} ¿Qué criterio usa la frase F3?', 'Manejo de recursos', 'Originalidad', 'Expresividad', 'F3 valora el control del trazo, que es manejo de recursos.'),
        ('abc', '{F} ¿Qué criterio usa la frase F4?', 'Expresividad', 'Coherencia', 'Manejo de recursos', 'F4 habla del efecto emocional que produjo la obra.'),
        ('abc', '{F} ¿Qué decisión de la obra refuerza el propósito de hablar del tiempo?', 'Que cada reloj marque una hora distinta', 'Que el fondo sea blanco', 'Que el trazo sea fino', 'La variedad de horas remite al paso del tiempo.'),
        ('abc', '{F} Un estudiante critica la obra por no ser «divertida». ¿Qué problema tiene?', 'Usa un criterio que no tiene relación con su propósito', 'Ninguno, porque a todos nos gusta la diversión', 'Que no leyó el título', 'El propósito es hablar del tiempo, no divertir.'),
        ('=', '{F} El curso usa 4 criterios y cada estudiante escribe 2 frases por criterio. Si hay 6 estudiantes, ¿cuántas frases hay?', '6*4*2', 'Se multiplican estudiantes, criterios y frases por criterio.', ' frases'),
        ('abc', '{F} ¿Cuál es un juicio equilibrado?', 'La obra es coherente por las horas distintas y tiene trazo parejo; la repetición reduce algo su originalidad', 'La obra es perfecta en todo', 'La obra es mala en todo', 'Reconoce fortalezas y una debilidad con evidencia.'),
        ('abc', '{F} Un integrante dice que el criterio de expresividad no sirve porque «depende de cada persona». ¿Qué corresponde?', 'Aclarar que se puede usar si se explica qué detalle produce el efecto', 'Descartarlo siempre', 'Obligar a todos a sentir lo mismo', 'La expresividad se argumenta con detalles aunque cada persona sienta algo distinto.'),
        ('=', 'Una obra recibe 4 puntos en coherencia, 3 en originalidad, 2 en expresividad y 3 en manejo de recursos. ¿Cuántos puntos suma?', '4+3+2+3', 'Se suman los puntajes de los cuatro criterios.', ' puntos'),
        ('abc', 'Antes de juzgar una obra, ¿qué conviene conocer?', 'Su propósito declarado, si existe', 'El precio de venta', 'La edad de quien la hizo', 'El propósito ayuda a elegir criterios adecuados.'),
        ('abc', 'Una estudiante dice que su criterio principal es la originalidad. ¿Qué evidencia necesita?', 'Mostrar en qué se diferencia la obra de un modelo o de lo habitual', 'Decir que le gustó mucho', 'Citar el precio', 'La originalidad se argumenta con una comparación.'),
        ('abc', 'Cuando una obra no declara su propósito, ¿qué se hace?', 'Se propone un propósito probable con evidencias y se aclara que es una interpretación', 'Se inventa un propósito y se presenta como seguro', 'No se puede analizar', 'Se declara que el propósito es una interpretación.'),
    ],
    ctx=('abc', 'Un grupo valora una obra que quiere transmitir calma. Tiene colores suaves y formas redondeadas, pero repite un modelo muy conocido. ¿Qué juicio es coherente?', 'Es coherente con su propósito de calma, pero tiene poca originalidad por repetir un modelo', 'Es mala porque repite un modelo', 'Es perfecta porque transmite calma', 'Un juicio equilibrado considera varios criterios con evidencia.'),
    sc=[
        ("En Artes: ¿qué es la originalidad?", "Proponer algo propio y no repetir un modelo", "Se argumenta comparando con lo habitual."),
        ("¿Qué criterio mira si las decisiones sirven al propósito?", "Coherencia", "La coherencia relaciona decisiones y propósito."),
        ("¿Qué debe tener un juicio equilibrado?", "Fortalezas y debilidades con evidencia", "Así el juicio resulta más creíble y equilibrado."),
    ],
    op=("Elige una obra inventada o descrita por escrito, define su propósito y escribe un juicio de cuatro frases con dos criterios: una fortaleza y una debilidad, cada una con evidencia.",
        "Obra: un cartel de una función de teatro. Propósito: invitar. Fortaleza (coherencia): el título grande se lee desde lejos, lo que sirve para invitar. Debilidad (manejo de recursos): el fondo y las letras de color parecido dificultan leer la fecha.",
        ["propósito declarado", "dos criterios con evidencia", "fortaleza y debilidad"],
        ["hoja con el juicio"],
        ["criterios ajenos al propósito", "solo elogios"],
        "Pregunta: «¿qué criterio usaste en cada frase?». Si no puede decirlo, pídele que los marque."),
    reinforce="Elige un objeto de diseño de tu casa (un envase o una portada) y escribe una fortaleza y una debilidad con un criterio.",
    extend="Explica por qué un criterio puede ser adecuado para una obra e inadecuado para otra.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (obra y dos juicios inventados). Obra «Maletas»: instalación ficticia de tres maletas de cartón apiladas junto a una puerta cerrada, con etiquetas sin nombre. "
     "Juicio de Lía: «La obra sugiere partida; las etiquetas vacías muestran que nadie sabe a dónde va. Me parece potente porque el vacío de las etiquetas genera preguntas». "
     "Juicio de Mateo: «La obra sugiere llegada; las maletas apiladas junto a la puerta recuerdan que alguien se queda. Me parece potente porque es simple y se entiende rápido». "
     "Objeción posible a ambos: «El cartón se ve frágil».")
build(
    O5, 4, F,
    use="Aprenderé a relacionar el análisis con una interpretación personal, a comparar juicios distintos y a responder una objeción con respeto.",
    prior=["Sé armar un argumento.", "Sé usar criterios.", "Sé distinguir descripción e interpretación."],
    explain=[
        "Una interpretación personal es la lectura que cada persona hace de una obra a partir de su experiencia. No es un error que sea distinta de la de otra persona; lo importante es que se apoye en el análisis, es decir, en detalles de la obra. Un juicio estético une análisis e interpretación: describe, interpreta y valora con razones.",
        "Cuando dos juicios son diferentes se comparan sus argumentos: qué evidencias usan, qué criterios aplican, si consideran el contexto y si responden a posibles objeciones. Un argumento es más sólido cuanto más evidencia tiene, cuanto más cuidadosamente la razona y cuanto mejor se hace cargo de las objeciones. La discusión respetuosa permite aprender del otro punto de vista y, a veces, ajustar el propio juicio.",
        "Para responder una objeción se reconoce lo que tiene de válido y se muestra, con evidencia, por qué no cambia la valoración o cómo la modifica. Se evita descalificar a quien objeta. Si una conversación se vuelve agresiva, se pide pausa y se avisa a una persona adulta si hace falta.",
    ],
    vocab=[("interpretación personal", "lectura que una persona hace de una obra desde su experiencia"), ("objeción", "razón que cuestiona un argumento"), ("solidez", "fuerza de un argumento por su evidencia y razones"), ("punto de vista", "manera de mirar una obra"), ("matizar", "ajustar una afirmación para hacerla más precisa")],
    worked=[
        ("Comparar dos juicios", "En la ficha, ¿qué tienen en común los juicios de Lía y de Mateo?", ["Ambos usan un detalle de la obra (etiquetas y maletas).", "Ambos valoran la obra como potente con una razón."], "Ambos usan detalles de la obra y razones"),
        ("Responder una objeción", "Alguien dice «el cartón se ve frágil». Responde de forma respetuosa.", ["Se reconoce que el cartón es frágil.", "Se agrega que esa fragilidad puede reforzar la idea de partida o de llegada incierta."], "Es cierto, y esa fragilidad puede reforzar la idea de partida o llegada incierta"),
    ],
    mistakes=[("Dar por «equivocado» a quien interpreta distinto.", "Dos interpretaciones pueden estar bien apoyadas.", "Compara las evidencias y razones de cada una."),
              ("Responder a una objeción diciendo «tú no entiendes de arte».", "Se ataca a la persona y no se discute la idea.", "Reconoce lo válido y responde con evidencia.")],
    T=[
        ('abc', '¿Qué es una interpretación personal?', 'La lectura de una obra que cada persona hace desde su experiencia, apoyada en detalles', 'Una verdad que debe aceptar todo el curso', 'Una descripción exacta de la obra', 'Es personal y se apoya en detalles de la obra.'),
        ('abc', '{F} ¿Qué evidencia usa Lía?', 'Las etiquetas sin nombre', 'La puerta abierta', 'El color de las maletas', 'La ficha señala etiquetas vacías en el juicio de Lía.'),
        ('abc', '{F} ¿Qué interpretación hace Mateo?', 'Que la obra sugiere llegada', 'Que sugiere partida', 'Que no sugiere nada', 'Mateo ve las maletas junto a la puerta como una llegada.'),
        ('abc', '{F} ¿Cuál de los dos juicios tiene argumentos?', 'Ambos', 'Solo el de Lía', 'Ninguno', 'Cada uno usa evidencia y razón.'),
        ('abc', '{F} ¿Qué razón da Mateo para valorar la obra como potente?', 'Que es simple y se entiende rápido', 'Que es muy cara', 'Que es de cartón', 'La ficha indica esa razón en el juicio de Mateo.'),
        ('abc', '{F} ¿Cuál de las dos razones de valoración se refiere al efecto que la obra produce en quien la mira?', 'La de Lía: genera preguntas', 'La de Mateo: es simple', 'Ninguna', 'Generar preguntas describe un efecto sobre la mirada.'),
        ('=', '{F} Un curso de 32 estudiantes se divide en parejas para discutir las dos interpretaciones. ¿Cuántas parejas hay?', '32//2', 'Se reparte el curso en grupos de 2.', ' parejas'),
        ('abc', '{F} Un compañero dice que Mateo se equivoca porque «la obra solo puede ser de partida». ¿Qué corresponde?', 'Revisar las evidencias de ambos y aceptar que puede haber dos lecturas apoyadas', 'Aceptar sin discutir', 'Descalificar a Mateo', 'No hay una única lectura correcta si hay evidencia para varias.'),
        ('abc', '{F} Alguien objeta: «las etiquetas vacías no significan nada, solo falta de tiempo». ¿Cuál es una respuesta respetuosa?', 'Puede ser, pero tres etiquetas vacías junto a una puerta cerrada sugieren que no se sabe a dónde van las maletas', 'Eso no importa', 'Tú no entiendes de arte', 'Reconoce lo posible y responde con un argumento basado en la obra.'),
        ('abc', 'Cuando dos juicios chocan, ¿cuál es más sólido?', 'El que tiene más evidencias, razones claras y atiende las objeciones', 'El que lo dice con más fuerza', 'El que lo defiende más gente', 'La solidez depende de evidencia y razones, no de la fuerza.'),
        ('=', 'En una pareja, cada estudiante escribe 3 evidencias a favor de su lectura de la obra. ¿Cuántas evidencias hay en total?', '2*3', 'Se multiplican los estudiantes de la pareja por las evidencias de cada uno.', ' evidencias'),
        ('abc', 'Una discusión sobre una obra se vuelve agresiva. ¿Qué haces?', 'Pides una pausa y avisas a una persona adulta si hace falta', 'Subes la voz para imponerte', 'Dejas de ir a clases', 'Se cuida el trato respetuoso y se pide ayuda cuando es necesario.'),
        ('abc', 'Alguien cambia de juicio tras escuchar a otra persona. ¿Qué significa?', 'Que valoró un argumento mejor sustentado', 'Que no tenía una opinión propia', 'Que lo obligaron', 'Cambiar por mejores razones es parte de argumentar.'),
    ],
    ctx=('abc', 'En la discusión sobre «Maletas», una estudiante dice: «Entiendo tu lectura de llegada por las maletas junto a la puerta; yo veo partida porque las etiquetas no tienen nombre y no sabemos dónde van. Podríamos incluir ambas en el juicio». ¿Qué tiene de bueno?', 'Reconoce otra lectura, da una evidencia propia y propone integrarlas', 'Descalifica la otra lectura', 'Evita dar razones', 'Reconoce otra lectura y fundamenta la propia con respeto.'),
    sc=[
        ("En Artes: ¿qué es una objeción?", "Una razón que cuestiona un argumento", "Responderla con evidencia mejora el argumento."),
        ("¿Qué hace más sólido un argumento?", "Evidencias, razones claras y atención a las objeciones", "Esas partes sostienen la valoración que se hace de la obra."),
        ("¿Cómo se responde una objeción?", "Reconociendo lo válido y respondiendo con evidencia", "Así se discute la idea y no a la persona."),
    ],
    op=("Elige una obra inventada o descrita por escrito, escribe una interpretación tuya con un detalle, imagina una interpretación distinta y compara sus argumentos en cuatro frases. Termina con una objeción y su respuesta respetuosa.",
        "Obra: un dibujo de una ventana con una luz encendida. Mi lectura: compañía, por la luz. Otra lectura: espera, por la ventana cerrada. Ambas se apoyan en detalles. Objeción: «la luz también puede ser descuido». Respuesta: puede ser, pero la luz en un solo cuarto sugiere una presencia.",
        ["dos lecturas con evidencia", "comparación de argumentos", "objeción respondida con respeto"],
        ["hoja con la comparación"],
        ["descalificar la otra lectura", "no dar evidencia"],
        "Pregunta: «¿qué evidencia sostiene la otra lectura?». Si no la reconoce, pídele que la busque."),
    reinforce="Pregunta a una persona de tu casa qué ve en una imagen y escribe en tres frases en qué coincide con tu lectura y en qué no.",
    extend="Explica una situación en que cambiarías tu juicio sobre una obra al escuchar a otra persona.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (obra y borradores inventados). Obra «Puente de lana»: escultura ficticia de hilos de lana roja tensados entre dos mesas, de 2 metros de largo, con pequeños papeles colgando. "
     "Borrador 1: «Es una obra buena porque es famosa.» "
     "Borrador 2: «No sirve, me aburre.» "
     "Borrador 3: «Los hilos rojos tensados entre las mesas forman una línea que une dos puntos; por eso la obra comunica conexión de forma clara.» "
     "Borrador 4: «Seguro es excelente porque la hizo un artista reconocido.» "
     "Lista de revisión (5 preguntas): ¿Hay afirmación? ¿Hay criterio? ¿Hay evidencia de la obra? ¿Hay razón? ¿Se escribe con respeto?")
build(
    O5, 5, F,
    use="Aprenderé a escribir y revisar un juicio estético completo, evitando razones débiles como la fama, la autoridad o el gusto sin argumento.",
    prior=["Sé armar un argumento.", "Sé usar criterios.", "Sé responder objeciones."],
    explain=[
        "Un juicio estético escrito reúne afirmación, criterio, evidencia, razón y respeto. Antes de entregarlo se revisa con una lista de preguntas. Algunos errores frecuentes son apoyarse en la popularidad («es buena porque es famosa»), en la autoridad («es excelente porque la hizo un artista reconocido»), en el precio o en el gusto sin argumento («me aburre»). Esas razones no hablan de la obra misma.",
        "Para corregir un borrador débil se pregunta qué detalle de la obra puede servir de evidencia, qué criterio tiene sentido para su propósito y cómo se conectan ambos. Por ejemplo, «Es famosa» puede transformarse en «Los hilos rojos unen dos puntos y por eso comunica conexión». Se evita exagerar con palabras como «siempre», «nunca» o «perfecto».",
        "El juicio también se escribe con un tono respetuoso, sin ironías hacia la autora o el autor ni burlas. Si el juicio es sobre la obra de un compañero, se pide permiso para compartirlo y se cuida que nadie se sienta ofendido; si un comentario hiere, se avisa a una persona adulta.",
    ],
    vocab=[("falacia de popularidad", "creer que algo es bueno porque muchos lo dicen o es famoso"), ("falacia de autoridad", "creer que algo es bueno solo porque lo hizo alguien reconocido"), ("lista de revisión", "preguntas para comprobar un texto antes de entregarlo"), ("exagerar", "decir más de lo que la evidencia sostiene"), ("tono respetuoso", "manera de escribir que no ofende")],
    worked=[
        ("Detectar el error", "En el borrador 4 se dice «es excelente porque la hizo un artista reconocido». ¿Qué error comete?", ["Se apoya en quién hizo la obra y no en lo que muestra la obra.", "Es una falacia de autoridad."], "Falacia de autoridad"),
        ("Aplicar la lista", "¿Cuántas preguntas de la lista cumple el borrador 3?", ["Tiene afirmación (comunica conexión), evidencia (hilos rojos tensados) y razón (forman una línea que une dos puntos).", "Falta un criterio explícito, pero cumple el respeto; son 4 de 5."], "4 de 5")
    ],
    mistakes=[("Corregir un borrador solo cambiando adjetivos, como «buena» por «excelente».", "No agrega evidencia ni razón.", "Agrega un detalle de la obra y la razón que lo conecta."),
              ("Usar palabras absolutas como «siempre» o «perfecto».", "Exagera lo que la evidencia sostiene.", "Escribe afirmaciones ajustadas a lo que puedes mostrar.")],
    T=[
        ('abc', '¿Qué es la falacia de popularidad?', 'Creer que algo es bueno porque muchos lo dicen o es famoso', 'Creer que algo es bueno porque lo demuestra con evidencia', 'Creer que algo es malo porque cuesta caro', 'Se apoya en cuántos lo dicen y no en la obra.'),
        ('abc', '{F} ¿Qué error tiene el borrador 1?', 'Se apoya en la fama y no en la obra', 'Es demasiado largo', 'Cita muchos detalles', 'Usa «es famosa» como razón, que es una falacia de popularidad.'),
        ('abc', '{F} ¿Qué le falta al borrador 2?', 'Criterio, evidencia y razón', 'Nada, es una buena crítica', 'Más palabras negativas', 'Solo expresa un gusto, el aburrimiento, sin razones ni evidencia.'),
        ('abc', '{F} ¿Qué evidencia usa el borrador 3?', 'Los hilos rojos tensados entre las mesas', 'El nombre de la escultura', 'La lana', 'Cita los hilos rojos tensados entre las mesas.'),
        ('abc', '{F} ¿Qué conector del borrador 3 señala la conclusión?', 'Por eso', 'Pero', 'Aunque', 'Por eso anuncia lo que se concluye de la evidencia.'),
        ('=', '{F} Un borrador cumple 3 de las 5 preguntas de la lista. ¿Cuántas le faltan?', '5-3', 'Se restan las cumplidas al total de preguntas.', ' preguntas'),
        ('abc', '{F} ¿Cuál es una mejora del borrador 1?', 'Reemplazar «es famosa» por un detalle de la obra y una razón, como que los hilos unen dos puntos', 'Reemplazar «famosa» por «conocidísima»', 'Escribirlo en mayúsculas', 'Una mejora aporta evidencia y razón, no solo énfasis.'),
        ('abc', '{F} ¿Qué se corrige en el borrador 4?', 'Reemplazar el argumento de autoridad por un detalle de la obra', 'Agregar «seguro» más veces', 'Eliminar el título', 'La autoría no sustituye a la evidencia.'),
        ('abc', '{F} Quieres reescribir el borrador 2 sin cambiar tu gusto. ¿Cómo?', 'Mantienes que te aburrió, pero explicas qué detalle y qué criterio explican esa sensación, con respeto', 'Dices que es buena para evitar problemas', 'Dices que la autora no sabe', 'Se puede conservar el gusto y argumentar con evidencia y respeto.'),
        ('=', 'Una clase escribe 8 juicios y revisa que cada uno cumpla las 5 preguntas de la lista. ¿Cuántas revisiones individuales hay?', '8*5', 'Se multiplica la cantidad de juicios por las preguntas de la lista.', ' revisiones'),
        ('abc', 'Alguien escribe «es perfecta y siempre se entiende». ¿Qué problema tiene?', 'Exagera con palabras absolutas que la evidencia no sostiene', 'Es muy corto', 'No usa tilde', 'La evidencia rara vez permite afirmar «siempre» o «perfecto».'),
        ('abc', 'Quieres compartir un juicio sobre la obra de un compañero con el curso. ¿Qué haces?', 'Le pides permiso y cuidas el tono respetuoso', 'Lo compartes sin avisar', 'Lo compartes en redes sociales para que lo vean todos', 'Se pide permiso y se cuida a las personas.'),
        ('abc', 'Un comentario sobre tu obra te hiere. ¿Qué corresponde?', 'Avisar a una persona adulta de confianza y revisar si hay algo útil en el contenido', 'Responder con otro comentario hiriente', 'Guardártelo para no causar problemas', 'Se avisa a una persona adulta y se separa lo útil de lo que hiere.'),
    ],
    ctx=('abc', 'Para «Puente de lana», una estudiante quiere pasar del borrador «es famosa» a un juicio completo. ¿Cuál reescritura es la mejor?', 'La obra es coherente con la idea de conexión, porque los hilos rojos tensados unen dos mesas y los papeles que cuelgan sugieren mensajes', 'La obra es muy famosa, y por eso es excelente', 'La obra no me convence', 'La reescritura cita evidencias y razón con un criterio.'),
    sc=[
        ("En Artes: ¿qué es la falacia de autoridad?", "Creer que algo es bueno solo porque lo hizo alguien reconocido", "No habla de la obra misma."),
        ("¿Qué se revisa antes de entregar un juicio?", "Afirmación, criterio, evidencia, razón y respeto", "La lista asegura que el juicio sea completo."),
        ("¿Se pide permiso para compartir un juicio sobre la obra de un compañero?", "Sí", "Se cuida a la persona y su trabajo."),
    ],
    op=("Elige una obra inventada o descrita por escrito. Escribe un borrador débil (con una falacia) y luego un juicio mejorado de tres frases con afirmación, criterio, evidencia y razón. Aplica la lista de revisión.",
        "Obra: un mural escolar de colores vivos. Borrador débil: «Es lindo porque lo hizo el curso más famoso». Mejorado: el mural es expresivo porque los colores vivos del fondo generan energía, y por eso invita a quedarse mirando. Lista: afirmación sí, criterio sí, evidencia sí, razón sí, respeto sí.",
        ["identifica la falacia", "juicio mejorado completo", "aplica la lista"],
        ["hoja con borrador y versión mejorada"],
        ["cambiar solo adjetivos", "no aplicar la lista"],
        "Pregunta: «¿qué detalle de la obra sostiene tu juicio?». Si no hay, pídele que vuelva a la obra."),
    reinforce="Escribe una frase débil y una mejorada sobre una imagen que veas hoy, como un cartel de la calle.",
    extend="Explica por qué cambiar adjetivos no basta para mejorar un juicio débil.",
)

# ============================================================ OAC-06, clase 1
F = ("Ficha 6 (bitácora de ejemplo, inventada). Proyecto «Álbum de barrio» de una estudiante ficticia: un libro de 8 páginas con dibujos de su barrio. "
     "Semana 1: 3 bocetos y una lista de lugares. Semana 2: probó 2 técnicas (lápiz y tinta de témpera diluida) y eligió la tinta. "
     "Semana 3: recibió un comentario de un compañero («las páginas se parecen mucho entre sí») y cambió el tamaño de los dibujos en 3 páginas. "
     "Semana 4: terminó las 8 páginas; 2 tienen manchas de pegamento. "
     "Criterios de proceso: exploración, registro, uso de comentarios, manejo del tiempo. Criterios de resultado: mensaje claro, composición, terminación.")
build(
    O6, 1, F,
    use="Aprenderé a evaluar críticamente un proceso y un resultado por separado, usando evidencias de una bitácora y criterios definidos.",
    prior=["Sé registrar versiones y decisiones.", "Sé dar un juicio argumentado.", "Sé calcular cantidades pequeñas."],
    explain=[
        "Evaluar críticamente un proyecto es revisar con criterios y evidencias qué se hizo y qué resultó. Se separa el proceso (el camino: explorar, registrar, usar comentarios, manejar el tiempo) del resultado (la obra terminada: mensaje, composición, terminación). Un buen proceso no garantiza un buen resultado y a veces un buen resultado oculta un proceso débil.",
        "La evidencia del proceso está en la bitácora, los bocetos, las versiones y los comentarios recibidos. La evidencia del resultado está en la obra misma. Cada juicio se apoya en una evidencia concreta («en la semana 3 cambió el tamaño de 3 páginas por un comentario»). La evaluación se aplica tanto al propio trabajo como al de otras personas.",
        "La evaluación crítica no busca culpar, sino entender qué funcionó y qué se puede mejorar. Se escribe con datos, no con adjetivos vagos, y con respeto: se habla del trabajo, no de la persona.",
    ],
    vocab=[("evaluación crítica", "revisión con criterios y evidencias de un proceso y un resultado"), ("bitácora", "registro de lo que se hace y se decide"), ("criterio de proceso", "aspecto del camino que se evalúa"), ("criterio de resultado", "aspecto de la obra terminada que se evalúa"), ("evidencia", "dato concreto que respalda un juicio")],
    worked=[
        ("Separar proceso y resultado", "«Probó dos técnicas y eligió la tinta». ¿Es evidencia de proceso o de resultado?", ["Habla de explorar técnicas antes de decidir.", "Es evidencia de proceso: exploración."], "Evidencia de proceso"),
        ("Calcular", "¿Cuántas páginas del álbum no tienen manchas de pegamento?", ["El álbum tiene 8 páginas y 2 tienen manchas.", "8 − 2 = 6."], "6 páginas"),
    ],
    mistakes=[("Evaluar solo el resultado porque «es lo que se ve».", "Se pierde información sobre cómo se decidió y qué se aprendió.", "Revisa también la bitácora y las versiones."),
              ("Escribir «el proceso fue bueno» sin ningún dato.", "No hay evidencia y no se puede comprobar.", "Cita un hecho de la bitácora, como una prueba o un cambio tras un comentario.")],
    T=[
        ('abc', '¿Qué significa evaluar críticamente un proyecto?', 'Revisar con criterios y evidencias qué se hizo y qué resultó', 'Decir si me gustó o no', 'Ponerle una nota sin explicar', 'La evaluación crítica usa criterios y evidencias.'),
        ('abc', '{F} ¿Qué dos técnicas probó la estudiante en la semana 2?', 'Lápiz y tinta de témpera diluida', 'Acuarela y carboncillo', 'Fotografía y collage', 'La ficha indica lápiz y tinta de témpera diluida.'),
        ('abc', '{F} ¿Qué cambio hizo después del comentario del compañero?', 'Cambió el tamaño de los dibujos en 3 páginas', 'Eliminó 3 páginas', 'Cambió el título', 'La ficha dice que cambió el tamaño en 3 páginas.'),
        ('=', '{F} Si cada página lleva 3 dibujos pequeños, ¿cuántos dibujos hay en las 8 páginas?', '8*3', 'Se multiplica la cantidad de páginas por los dibujos de cada una.', ' dibujos'),
        ('abc', '{F} ¿Qué criterio de proceso muestra la semana 3?', 'Uso de comentarios', 'Terminación', 'Mensaje claro', 'Usó un comentario para cambiar el tamaño.'),
        ('abc', '{F} ¿Qué criterio de resultado se ve afectado por las manchas de pegamento?', 'Terminación', 'Exploración', 'Registro', 'Las manchas afectan el acabado de la obra.'),
        ('abc', '{F} ¿Cuál es evidencia de registro?', 'La lista de lugares de la semana 1', 'Las manchas de pegamento', 'El título del álbum', 'Una lista anotada es un registro del proceso.'),
        ('abc', '{F} Alguien afirma: «el proceso fue excelente». ¿Qué conviene preguntar?', '¿Qué evidencia de la bitácora lo muestra?', '¿Quién lo hizo?', '¿Cuánto costó?', 'Un juicio de proceso se apoya en un hecho de la bitácora.'),
        ('=', '{F} Si dedicó 3 horas por semana durante 4 semanas, ¿cuántas horas trabajó en total?', '3*4', 'Se multiplican las horas por semana por la cantidad de semanas.', ' horas'),
        ('abc', 'Un proyecto tiene un buen resultado pero no hay registro del proceso. ¿Qué se puede decir?', 'Que no hay evidencia suficiente para evaluar el proceso', 'Que el proceso fue excelente', 'Que el resultado es malo', 'Sin registro no se puede comprobar el proceso.'),
        ('abc', 'Un estudiante tuvo un proceso ordenado, pero el resultado no cumple el mensaje. ¿Qué conclusión es adecuada?', 'Que el proceso fue sólido, pero hay que revisar las decisiones que no sirvieron al mensaje', 'Que el proceso no sirve', 'Que el mensaje no importaba', 'Un buen proceso no garantiza un resultado logrado.'),
        ('abc', 'Al evaluar el proyecto de un compañero, ¿cómo conviene referirse?', 'Al trabajo y sus evidencias, no a la persona', 'A lo que cree que es su carácter', 'A las notas que saca en otras asignaturas', 'La evaluación se centra en el trabajo.'),
        ('abc', '{F} ¿Qué sugerencia de mejora es coherente con la evidencia?', 'Usar un pegamento en barra y probar con un papel de prueba antes de pegar las páginas finales', 'Rehacer todo el álbum sin probar', 'Quitar las páginas con manchas sin avisar', 'Una mejora responde a la evidencia y se prueba antes.'),
    ],
    ctx=('abc', 'Una estudiante evalúa su propio proyecto: «Proceso: exploré dos técnicas y registré las dos. Resultado: el mensaje se entiende, pero 2 páginas tienen manchas. Mejora: probar el pegamento antes». ¿Qué tiene de bueno?', 'Separa proceso y resultado, cita evidencias y propone una mejora concreta', 'Solo da una nota', 'No cita ninguna evidencia', 'La evaluación usa datos y una acción.'),
    sc=[
        ("En Artes: ¿qué se evalúa en el proceso?", "El camino: explorar, registrar, usar comentarios y manejar el tiempo", "El proceso se evalúa con bitácora y versiones."),
        ("¿Qué se evalúa en el resultado?", "La obra terminada: mensaje, composición y terminación", "El resultado se evalúa con la obra misma."),
        ("¿En qué se apoya un juicio de proceso?", "En evidencias de la bitácora", "Así otra persona puede comprobar lo que se afirma."),
    ],
    op=("Elige un proyecto tuyo o inventado y escribe una evaluación de cuatro frases: dos de proceso y dos de resultado, cada una con una evidencia concreta, y una mejora.",
        "Proyecto: cartel de la biblioteca. Proceso: probé dos tamaños de letra (evidencia: dos pruebas anotadas) y cambié el color tras un comentario. Resultado: el título se lee a 3 metros; el texto pequeño no se lee. Mejora: aumentar el tamaño del texto secundario.",
        ["separa proceso y resultado", "cada frase tiene evidencia", "propone una mejora"],
        ["hoja con la evaluación"],
        ["adjetivos vagos", "sin evidencia"],
        "Pregunta: «¿qué dato de la bitácora respalda esa frase?». Si no hay, pídele que lo anote."),
    reinforce="Escribe en tu cuaderno tres cosas que hiciste esta semana para avanzar en un trabajo y qué evidencia queda de cada una.",
    extend="Explica por qué evaluar solo el resultado puede ser injusto para un proyecto con un proceso rico.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 7 (caso de ejemplo, inventado). Proyecto «Cartel de la biblioteca» de un grupo ficticio. "
     "Propósito: invitar a estudiantes de 1.º a 4.º medio a leer en el recreo. "
     "Decisiones tomadas: (1) colores cálidos; (2) un personaje que lee sentado en el suelo; (3) un texto de 5 palabras; (4) letras pequeñas para la hora. "
     "Resultado observado por un compañero a 3 metros: el personaje y los colores se ven y atraen la mirada; el texto de 5 palabras se lee; la hora no se alcanza a leer. "
     "Escala de logro: «Se logra» / «Se logra a medias» / «No se logra».")
build(
    O6, 2, F,
    use="Aprenderé a evaluar si las decisiones estéticas de una obra son coherentes con su propósito expresivo o comunicativo y a calificar el logro con evidencia.",
    prior=["Sé separar proceso y resultado.", "Sé usar criterios.", "Sé que cada decisión visual tiene un efecto."],
    explain=[
        "Evaluar críticamente un trabajo implica relacionar tres elementos: el propósito (para qué se hizo), las decisiones estéticas (colores, formas, composición, tipografía) y el efecto que producen. Una decisión es coherente si su efecto contribuye al propósito. Para evaluarla se escribe una tabla con tres columnas: decisión, efecto observado y relación con el propósito.",
        "La escala de logro ayuda a resumir: «se logra» si el efecto cumple el propósito, «se logra a medias» si lo cumple en parte y «no se logra» si no lo cumple. Cada calificación se apoya con una evidencia, como lo que se alcanza a ver a cierta distancia o lo que dice el público. Lo que no se pudo comprobar se declara como pendiente.",
        "Evaluar con propósito evita opiniones sueltas: no se pregunta «¿es lindo?», sino «¿sirve para invitar a leer?». Luego se propone una mejora que mantenga lo que funcionó. Todo el análisis se hace sobre el trabajo y con respeto a quienes lo hicieron.",
    ],
    vocab=[("propósito", "para qué se hace la obra"), ("decisión estética", "elección de color, forma, composición o tipografía"), ("efecto", "lo que produce una decisión en quien mira"), ("coherente", "que contribuye al propósito"), ("escala de logro", "niveles para resumir si se cumplió algo")],
    worked=[
        ("Evaluar una decisión", "La decisión (3), un texto de 5 palabras, ¿es coherente con el propósito?", ["El texto de 5 palabras se lee desde 3 metros, según la ficha.", "Eso ayuda a invitar rápido; es coherente: se logra."], "Es coherente: se logra"),
        ("Calificar una decisión", "La decisión (4), letras pequeñas para la hora, ¿qué calificación recibe?", ["La hora no se alcanza a leer.", "No cumple el efecto que necesita el propósito (que se sepa cuándo ir): no se logra."], "No se logra")
    ],
    mistakes=[("Evaluar una decisión por si es «linda» y no por su efecto sobre el propósito.", "El gusto no dice si el trabajo cumple lo que busca.", "Pregunta si el efecto ayuda al propósito."),
              ("Calificar un logro sin evidencia, como «se logra porque creo que sí».", "No se puede comprobar.", "Cita lo observado, como lo que se ve a 3 metros.")],
    T=[
        ('abc', '¿Qué significa que una decisión estética sea coherente?', 'Que su efecto contribuye al propósito de la obra', 'Que a todos les gusta', 'Que es igual a otra obra', 'La coherencia relaciona decisión, efecto y propósito.'),
        ('abc', '{F} ¿Cuál es el propósito del cartel?', 'Invitar a estudiantes de 1.º a 4.º medio a leer en el recreo', 'Vender libros', 'Mostrar el trabajo del grupo', 'La ficha lo declara como propósito.'),
        ('abc', '{F} ¿Qué efecto tiene la decisión de usar colores cálidos?', 'Atraen la mirada a 3 metros', 'No se ven desde lejos', 'Dificultan la lectura del texto', 'La ficha dice que el personaje y los colores atraen la mirada.'),
        ('abc', '{F} Según el compañero, ¿cuáles de estos elementos se ven o se leen a 3 metros?', 'El personaje, los colores y el texto de 5 palabras', 'El personaje y la hora', 'La hora y los colores', 'La ficha dice que se ven el personaje y los colores y que se lee el texto; la hora no se alcanza a leer.'),
        ('abc', '{F} ¿Cómo se califica la decisión del personaje que lee sentado?', 'Se logra, porque se ve a 3 metros y se relaciona con leer', 'No se logra', 'No se puede calificar nunca', 'La ficha indica que el personaje se ve y remite al propósito.'),
        ('=', '{F} De las 4 decisiones, 3 se logran. Si otro cartel con 8 decisiones mantuviera la misma proporción, ¿cuántas se lograrían?', '3*8//4', 'Se calcula la misma proporción para 8 decisiones.', ' decisiones'),
        ('abc', '{F} ¿Qué conclusión global es adecuada?', 'En general es coherente con el propósito, pero falla el dato de la hora', 'No cumple en nada', 'Cumple completamente', 'Tres decisiones cumplen y una no.'),
        ('abc', '{F} ¿Qué mejora es coherente?', 'Aumentar el tamaño de las letras de la hora y probar de nuevo a 3 metros', 'Quitar el personaje', 'Cambiar todos los colores', 'La mejora corrige lo que no funcionó y mantiene lo que sí.'),
        ('=', 'Un cartel necesita leerse a 3 metros. El texto principal mide 6 cm de alto y se lee a 2 metros. Si se duplica el alto, ¿cuántos cm medirá?', '6*2', 'Se duplica la medida del texto.', ' cm'),
        ('abc', 'Quien evalúa dice «no me gusta el rojo». ¿Cómo se convierte en un juicio útil?', 'Preguntando qué efecto produce el rojo y si ayuda al propósito', 'Descartando el rojo sin más', 'Ignorando al evaluador', 'El juicio útil se centra en el efecto y el propósito.'),
        ('abc', 'No se puede comprobar si el cartel atrae a estudiantes de 1.º medio porque aún no se ha mostrado. ¿Qué se anota?', 'Pendiente de comprobar con una muestra de ese público', 'Se logra', 'No se logra', 'Lo que no se ha comprobado se declara pendiente.'),
        ('abc', 'Un grupo cambia el propósito del cartel después de ver los resultados para que «todo se logre». ¿Qué problema hay?', 'Cambia el criterio para favorecer el resultado', 'Ninguno', 'Que no usó colores cálidos', 'El propósito se define antes de evaluar.'),
        ('abc', '{F} Alguien dice que el cartel es «de baja calidad» sin más. ¿Qué respondes?', 'Que indique qué decisión no sirve al propósito y qué evidencia lo muestra', 'Que tiene razón', 'Que no puede opinar', 'La crítica útil nombra decisión y evidencia.'),
    ],
    ctx=('abc', 'Un grupo tiene un afiche para invitar a una función de teatro. El título es grande y de color contrastante, pero la fecha está en letra pequeña de color claro. ¿Qué evaluación es coherente?', 'Se logra a medias: el título invita, pero la fecha no se lee y se necesita mejorar', 'Se logra del todo', 'No se logra en nada', 'Una parte cumple el propósito y la otra no.'),
    sc=[
        ("En Artes: ¿qué es el efecto de una decisión?", "Lo que produce en quien mira", "Ese efecto se compara con el propósito de la obra."),
        ("¿Qué significa «se logra a medias»?", "Que el efecto cumple el propósito solo en parte", "La escala resume la evaluación en tres niveles claros."),
        ("¿Qué se hace con lo que no se pudo comprobar?", "Se declara como pendiente", "No se inventa un resultado que no se comprobó."),
    ],
    op=("Elige un proyecto tuyo o inventado y escribe una tabla de tres decisiones con su efecto y su calificación (se logra, a medias o no se logra), con evidencia. Escribe una mejora.",
        "Proyecto: invitación a una muestra. Propósito: que vengan familias. Decisión 1: fondo oscuro; efecto: el texto claro se lee; se logra. Decisión 2: letras de adorno; efecto: la fecha cuesta leer; a medias. Decisión 3: logotipo grande; efecto: se reconoce; se logra. Mejora: letras más simples para la fecha.",
        ["decisión, efecto y calificación", "evidencia", "mejora coherente"],
        ["hoja con la tabla"],
        ["evaluar por gusto", "no declarar lo pendiente"],
        "Pregunta: «¿qué efecto produce esa decisión?». Si responde con gusto, pídele el efecto."),
    reinforce="Elige un letrero de tu entorno y anota su propósito y si cada decisión visual lo ayuda.",
    extend="Explica por qué una decisión bonita puede no ser coherente con el propósito.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 8 (registro de decisiones de ejemplo, inventado). Proyecto: portada de un cuaderno de poemas de un curso ficticio. "
     "Decisión D1: usar témpera lavable en lugar de lápices de color. Razón: colores más intensos. Alternativa descartada: lápices de color. Costo adicional: $1.500. Efecto: los colores se ven intensos, pero se demoró 40 minutos más. "
     "Decisión D2: reducir la portada de 4 colores a 3. Razón: cumplir el plazo. Alternativa descartada: mantener 4 colores. Efecto: se terminó a tiempo; el contraste quedó algo menor. "
     "Decisión D3: pedir un comentario a un compañero antes de pegar el título. Razón: evitar errores de legibilidad. Alternativa descartada: pegar de inmediato. Efecto: se corrigió un error de legibilidad. "
     "Tiempo total planificado: 180 minutos.")
build(
    O6, 3, F,
    use="Aprenderé a registrar y evaluar las decisiones tomadas durante el proceso: razones, alternativas descartadas, costos y consecuencias.",
    prior=["Sé evaluar coherencia entre propósito y efecto.", "Sé usar una bitácora.", "Sé calcular costos y tiempos."],
    explain=[
        "Durante un proyecto se toman muchas decisiones. Registrar cada una incluye cuatro datos: la decisión, la razón, las alternativas que se descartaron y las consecuencias (efecto, costo y tiempo). Las alternativas descartadas son importantes porque muestran que se pensó y compararon opciones. Sin esos datos, es difícil evaluar el proceso.",
        "Una decisión puede evaluarse con tres preguntas: ¿tenía una razón relacionada con el propósito?, ¿qué ganó y qué perdió?, ¿habría sido mejor otra alternativa? Una decisión puede ser acertada aunque tenga un costo (por ejemplo, más tiempo) si el efecto compensa. También puede ser un error que se corrige: reconocerlo es parte de una evaluación honesta.",
        "Los costos y los tiempos se calculan sumando lo que cada decisión añade o ahorra. Si el total supera lo disponible, se revisa qué decisión conviene modificar. El registro se escribe de manera simple y respetuosa, sin culpar a nadie.",
    ],
    vocab=[("decisión", "elección entre alternativas durante el proceso"), ("alternativa descartada", "opción que se consideró y no se eligió"), ("consecuencia", "efecto, costo o tiempo que trae una decisión"), ("razón", "motivo de una decisión"), ("compensar", "equilibrar un costo con un beneficio")],
    worked=[
        ("Identificar la alternativa descartada", "En D1, ¿qué alternativa se descartó?", ["La ficha dice que se prefirió témpera.", "La alternativa descartada fue usar lápices de color."], "Lápices de color"),
        ("Calcular el tiempo", "D1 agregó 40 minutos al plan de 180. ¿Cuántos minutos suma el plan?", ["Se suma el tiempo extra al plan.", "180 + 40 = 220."], "220 minutos"),
    ],
    mistakes=[("Anotar solo lo que se hizo y no lo que se descartó.", "No se ve que hubo comparación de opciones.", "Anota al menos una alternativa descartada y por qué."),
              ("Ocultar una decisión que salió mal.", "Se pierde la oportunidad de aprender.", "Registra el efecto real y qué se haría distinto.")],
    T=[
        ('abc', '¿Qué es una alternativa descartada?', 'Una opción que se consideró y no se eligió', 'Una opción que nadie conoció', 'Una opción obligatoria', 'Es una opción comparada y no elegida.'),
        ('abc', '{F} ¿Cuál fue la razón de D2?', 'Cumplir el plazo', 'Gastar menos dinero', 'Que se vea más colorida', 'La ficha dice que se redujo para cumplir el plazo.'),
        ('abc', '{F} ¿Qué efecto tuvo D3?', 'Se corrigió un error de legibilidad', 'Se perdió tiempo sin ganar nada', 'Se cambió el color', 'Pedir un comentario evitó pegar con el error.'),
        ('abc', '{F} ¿Cuál fue el costo adicional de D1?', '$1.500', '$40', '$180', 'La ficha indica $1.500 de costo adicional.'),
        ('=', '{F} Si además D3 tomó 10 minutos, ¿cuántos minutos suma el plan con D1 y D3 sobre los 180 planificados?', '180+40+10', 'Se suman al plan los 40 minutos de D1 y los 10 de D3.', ' minutos'),
        ('abc', '{F} ¿Qué se perdió con D2?', 'Algo de contraste', 'La entrega a tiempo', 'El permiso', 'La ficha indica que el contraste quedó algo menor.'),
        ('abc', '{F} ¿Qué decisión compensó su costo con un beneficio claro?', 'D1, porque los colores intensos justifican el tiempo y el costo extra', 'Ninguna', 'D2, porque no tuvo efectos', 'D1 tuvo costo pero logró un efecto buscado.'),
        ('abc', '{F} ¿Cuál es un riesgo de D2?', 'Que el menor contraste afecte la lectura del título', 'Que el cuaderno no tenga portada', 'Que se gaste de más', 'Reducir colores bajó el contraste, que influye en la legibilidad.'),
        ('=', '{F} Si el plan era de 180 minutos y las decisiones D1 y D2 añadieron 40 y restaron 25 minutos, ¿cuántos minutos suma finalmente?', '180+40-25', 'Se suma lo que añadió D1 y se resta lo que ahorró D2.', ' minutos'),
        ('abc', 'Alguien dice: «no hace falta anotar las alternativas descartadas». ¿Qué respondes?', 'Anotarlas muestra que se compararon opciones y ayuda a evaluar el proceso', 'Tiene razón, es una pérdida de tiempo', 'Solo sirve a los docentes', 'Ayudan a evaluar y a aprender de las decisiones.'),
        ('abc', 'Una decisión salió mal. ¿Qué es lo más honesto y útil?', 'Anotar el efecto real y qué se haría distinto', 'Borrar el registro', 'Culpar a otra persona', 'Reconocer un error permite aprender y mejorar el trabajo.'),
        ('abc', 'Para evaluar una decisión, ¿qué pregunta es útil?', '¿Tenía una razón relacionada con el propósito?', '¿Quién la tomó primero?', '¿Cuánto me gusta?', 'La razón relacionada con el propósito permite evaluar la decisión.'),
        ('abc', '{F} Se pregunta si habría sido mejor mantener 4 colores y pedir más tiempo. ¿Qué se necesita para responder?', 'Comparar el efecto, el tiempo y el plazo de ambas alternativas', 'Elegir la que dice la mayoría', 'No responder', 'Para comparar alternativas se usan datos de efecto, costo y tiempo.'),
    ],
    ctx=('abc', 'Un grupo decidió usar papel reciclado en vez de cartulina nueva para ahorrar $800, pero el papel absorbió mal la pintura. ¿Cómo debe registrarse la decisión?', 'Con la razón (ahorro), la alternativa descartada, el efecto real (absorbe mal) y lo que haría distinto', 'Solo diciendo que se ahorró', 'Sin anotarla', 'El registro completo incluye razón, alternativa, efecto y aprendizaje.'),
    sc=[
        ("En Artes: ¿qué se anota de cada decisión?", "La razón, la alternativa descartada y las consecuencias", "Así se puede evaluar el proceso."),
        ("¿Una decisión con costo puede ser acertada?", "Sí, si el efecto lo compensa", "Se evalúa lo que se gana y lo que se pierde."),
        ("¿Se oculta una decisión que salió mal?", "No, se registra y se aprende de ella", "Reconocerlo es parte de una evaluación honesta."),
    ],
    op=("Elige un proyecto tuyo o inventado y registra tres decisiones con razón, alternativa descartada y consecuencia (efecto, costo o tiempo). Evalúa una de ellas con las preguntas de la clase.",
        "Proyecto: maqueta de papel. D1: usar cartón fino en vez de cartulina; razón: ahorrar $600; alternativa: cartulina; efecto: más frágil. D2: pedir un comentario; razón: evitar errores; efecto: detecté un error de medida. D3: reducir el tamaño; razón: plazo; efecto: terminé a tiempo. Evaluación de D1: ahorró dinero, pero perdió resistencia; habría sido mejor reforzar con doble capa.",
        ["tres decisiones con datos", "alternativa descartada", "evaluación con razón"],
        ["hoja con el registro"],
        ["omitir alternativas", "ocultar una decisión fallida"],
        "Pregunta: «¿qué alternativa descartaste y por qué?». Si no hay, pídele que la identifique."),
    reinforce="Anota una decisión que tomaste esta semana al hacer una tarea, la alternativa que descartaste y el efecto.",
    extend="Explica por qué reconocer una mala decisión mejora un proyecto.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 9 (comentarios de ejemplo sobre un trabajo ajeno, inventados). Trabajo del compañero: un cartel con una figura central en azul sobre fondo celeste y un título pequeño abajo. "
     "Comentario C1: «Está feo.» "
     "Comentario C2: «Veo que usaste solo tonos fríos; eso da calma, pero la figura central se pierde. Podrías probar un color cálido en la figura.» "
     "Comentario C3: «Yo lo habría hecho distinto.» "
     "Comentario C4: «Me gustó el espacio vacío porque dirige la mirada al centro; quizá el título pueda ser más grande.» "
     "Estructura de una buena retroalimentación: OBSERVO (lo que veo) + EFECTO (qué produce) + SUGERENCIA (una idea de cambio), con respeto.")
build(
    O6, 4, F,
    use="Aprenderé a dar y recibir retroalimentación sobre procesos y resultados de pares, con una estructura útil y respetuosa.",
    prior=["Sé evaluar con criterios.", "Sé registrar decisiones.", "Sé que el respeto es parte de la crítica."],
    explain=[
        "La retroalimentación entre pares es un comentario que una persona hace del trabajo de otra para ayudar a mejorar. Una retroalimentación útil sigue tres pasos: observo (describo lo que veo, sin juzgar), efecto (digo qué produce eso en quien mira o en el propósito) y sugerencia (propongo una idea de cambio posible). Decir «está feo» o «yo lo habría hecho distinto» no ayuda, porque no dice qué cambiar ni por qué.",
        "Quien recibe la retroalimentación escucha completa, pregunta si no entiende y decide qué cambios hará, anotando por qué. No todos los comentarios se aceptan: se escogen los que sirven al propósito. Quien da la retroalimentación habla del trabajo y no de la persona, y evita compararla con otras personas. Antes de mostrar o fotografiar el trabajo de alguien, se pide su permiso.",
        "Si un comentario hiere o hay burlas, se avisa a una persona adulta de confianza; no se responde con otro insulto ni se guarda en silencio. La retroalimentación se acepta como regalo para mejorar el trabajo y se agradece.",
    ],
    vocab=[("retroalimentación", "comentario para ayudar a mejorar un trabajo"), ("observo", "descripción de lo que se ve"), ("efecto", "lo que produce lo observado"), ("sugerencia", "idea de cambio propuesta"), ("pares", "personas del mismo curso o nivel")],
    worked=[
        ("Reconocer la estructura", "Identifica observo, efecto y sugerencia en C2.", ["Observo: usaste solo tonos fríos.", "Efecto: da calma pero la figura se pierde. Sugerencia: probar un color cálido en la figura."], "Observo: tonos fríos; efecto: calma y figura que se pierde; sugerencia: color cálido"),
        ("Corregir un comentario", "Mejora C1 («Está feo»).", ["Se describe qué se ve: «La figura azul sobre celeste tiene poco contraste».", "Se agrega efecto y sugerencia: «por eso se pierde; prueba un azul más oscuro»."], "La figura azul sobre celeste tiene poco contraste, por eso se pierde; prueba un azul más oscuro")
    ],
    mistakes=[("Decir «está feo» o «está lindo» sin más.", "No orienta el cambio.", "Observa, di el efecto y sugiere."),
              ("Comparar el trabajo con el de otra persona del curso.", "Hiere y no ayuda a mejorar.", "Habla del propósito y del trabajo.")],
    T=[
        ('abc', '¿Qué es una retroalimentación útil?', 'Un comentario con observación, efecto y sugerencia, hecho con respeto', 'Un comentario que dice «está feo»', 'Una nota sin explicación', 'La retroalimentación útil orienta la mejora.'),
        ('abc', '{F} ¿Qué comentario tiene la estructura completa?', 'C2', 'C1', 'C3', 'C2 observa, dice el efecto y sugiere.'),
        ('abc', '{F} ¿Por qué C1 no ayuda?', 'Porque no dice qué se ve, qué produce ni qué cambiar', 'Porque es demasiado largo', 'Porque es muy específico', 'No ofrece información útil para mejorar el trabajo.'),
        ('abc', '{F} ¿Por qué C3 no ayuda?', 'Se refiere a lo que haría otra persona y no al trabajo mismo', 'Porque tiene sugerencia', 'Porque es amable', 'No dice nada sobre el trabajo.'),
        ('abc', '{F} ¿Qué observa C4?', 'Que hay espacio vacío que dirige la mirada al centro', 'Que el color es muy cálido', 'Que hay mucho texto', 'C4 describe el uso del espacio vacío.'),
        ('abc', '{F} ¿Qué sugerencia da C4?', 'Que el título sea más grande', 'Que se quite la figura', 'Que se cambie el fondo', 'La ficha dice que el título podría ser más grande.'),
        ('abc', '{F} ¿Qué efecto señala C4 sobre el espacio vacío?', 'Que dirige la mirada al centro', 'Que hace que la figura se pierda', 'Que agranda el título', 'C4 dice que el espacio vacío dirige la mirada al centro.'),
        ('=', '{F} Hay 4 comentarios y 2 son útiles (con observación, efecto y sugerencia). ¿Qué porcentaje es útil?', '2*100//4', 'Se calcula cuántos de cada 100 comentarios son útiles.', ' %'),
        ('abc', '{F} Quien hizo el cartel recibe C2 y C4. ¿Qué hace bien?', 'Escoge los cambios que sirven al propósito y anota por qué', 'Los aplica todos sin pensar', 'Los ignora', 'Se aceptan los comentarios que sirven al propósito, y se justifica.'),
        ('abc', 'Antes de fotografiar el trabajo de un compañero para mostrarlo, ¿qué haces?', 'Le pides permiso', 'Lo fotografías sin avisar', 'Lo publicas en redes', 'Se pide consentimiento antes de mostrar el trabajo de otra persona.'),
        ('=', 'En una ronda, cada estudiante da 2 retroalimentaciones y recibe 2. Si son 25 estudiantes, ¿cuántas retroalimentaciones se dan?', '25*2', 'Se multiplica la cantidad de estudiantes por las que da cada uno.', ' retroalimentaciones'),
        ('abc', 'Un compañero escribe «tu cartel es tan malo como el de tu hermana». ¿Qué corresponde?', 'Avisar a una persona adulta de confianza y pedir que se hable del trabajo', 'Responder con un insulto', 'Quedarte callado y no avisar', 'Una comparación hiriente se informa a un adulto.'),
        ('abc', 'Recibes una crítica que no entiendes. ¿Qué haces?', 'Preguntas qué observó y qué efecto vio para entenderla', 'La descartas sin preguntar', 'La aceptas sin entender', 'Preguntar ayuda a aclarar el comentario.'),
    ],
    ctx=('abc', 'Un compañero muestra su cartel con título pequeño y pide opinión. ¿Cuál retroalimentación es la mejor?', 'Veo que el título es pequeño; a 3 metros no se alcanza a leer; prueba duplicar su tamaño', 'No me gusta el título', 'Mi título es mejor', 'Tiene observación, efecto y sugerencia concreta para mejorar.'),
    sc=[
        ("En Artes: ¿cuáles son los tres pasos de una retroalimentación útil?", "Observo, efecto y sugerencia", "Orientan el cambio de forma concreta."),
        ("¿Se pide permiso para mostrar el trabajo de un compañero?", "Sí", "Pedir permiso es parte del respeto a esa persona."),
        ("¿Qué se hace si un comentario hiere?", "Se avisa a una persona adulta de confianza", "Cuidar a las personas es parte del trabajo."),
    ],
    op=("Imagina el trabajo de un compañero (un cartel o un dibujo) y escribe dos retroalimentaciones con observo, efecto y sugerencia. Luego escribe cómo responderías tú si recibieras una de ellas.",
        "Trabajo: dibujo de un patio con colores muy parecidos. Retroalimentación 1: observo que los árboles y el pasto tienen el mismo verde; el efecto es que se confunden; sugiero un verde más oscuro para los árboles. Retroalimentación 2: observo el espacio vacío a la izquierda; el efecto es que guía la mirada; sugiero poner el título ahí. Respuesta: gracias, probaré el verde más oscuro.",
        ["usa observo, efecto y sugerencia", "habla del trabajo y no de la persona", "responde con apertura"],
        ["hoja con retroalimentaciones y respuesta"],
        ["comentarios vagos", "comparar con otras personas"],
        "Pregunta: «¿qué efecto produce lo que observaste?». Si no lo dice, pídele que lo agregue."),
    reinforce="Elige un afiche de tu entorno y escribe una retroalimentación de tres frases siguiendo la estructura de la clase.",
    extend="Explica por qué la retroalimentación fortalece al grupo cuando se da con respeto.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 10 (autoevaluación de ejemplo, inventada). Proyecto: serie de dos láminas para invitar a cuidar el patio. "
     "Criterios y puntajes (de 1 a 4): propósito 3; composición 2; proceso 4; comunicación 3. "
     "Evidencias: el propósito se cumple en una lámina y en la otra falta el mensaje; la composición deja la figura al borde; el proceso tiene 5 versiones registradas; la comunicación se entiende pero el texto es pequeño. "
     "Plan de mejora posible: acción A (reubicar la figura de la lámina 2) 20 minutos; acción B (agrandar el texto) 25 minutos; acción C (agregar el mensaje que falta) 15 minutos. "
     "Tiempo disponible: 90 minutos, de los cuales 30 se reservan para la revisión final.")
build(
    O6, 5, F,
    use="Aprenderé a hacer una autoevaluación completa de un proyecto y a convertirla en un plan de mejora priorizado con tiempos y una nueva revisión.",
    prior=["Sé separar proceso y resultado.", "Sé registrar decisiones.", "Sé dar y recibir retroalimentación."],
    explain=[
        "La autoevaluación es la revisión crítica del propio trabajo. Incluye criterios, puntajes con evidencia y un plan de mejora. Se parte de los criterios acordados, se asigna un puntaje a cada uno y se anota la evidencia que lo respalda. Después se decide qué mejorar primero: se prioriza lo que más afecta al propósito y lo que se puede lograr en el tiempo disponible.",
        "Un plan de mejora tiene acciones concretas, con tiempos y un responsable. Se suman los tiempos de las acciones y se compara con el tiempo disponible, reservando un tramo para la revisión final. Si no alcanza, se elige qué acciones hacer y se anota qué queda pendiente. La mejora se comprueba con una nueva revisión que use los mismos criterios.",
        "Al terminar se escribe un aprendizaje: qué haría igual y qué haría distinto en otro proyecto. Los comentarios de otras personas se integran a la autoevaluación si ayudan. La autoevaluación es honesta y sin castigo: reconoce logros, errores y avances.",
    ],
    vocab=[("autoevaluación", "revisión crítica del propio trabajo"), ("prioridad", "lo que se mejora primero"), ("plan de mejora", "acciones con tiempos para mejorar"), ("revisión final", "nueva revisión con los mismos criterios"), ("aprendizaje", "lo que se conserva para futuros proyectos")],
    worked=[
        ("Sumar puntajes", "¿Cuántos puntos suma la autoevaluación de la ficha?", ["Se suman 3, 2, 4 y 3.", "3 + 2 + 4 + 3 = 12."], "12 puntos"),
        ("Calcular el tiempo útil", "Con 90 minutos y 30 reservados, ¿cuántos minutos hay para las acciones?", ["Se restan los minutos reservados.", "90 − 30 = 60."], "60 minutos")
    ],
    mistakes=[("Poner puntajes sin evidencia.", "No se puede comprobar ni se sabe qué mejorar.", "Anota la evidencia que respalda cada puntaje."),
              ("Planificar más acciones de las que caben en el tiempo.", "No se terminan y se pierde la revisión final.", "Suma los tiempos y prioriza.")],
    T=[
        ('abc', '¿Qué incluye una autoevaluación completa?', 'Criterios, puntajes con evidencia y un plan de mejora', 'Solo una nota final', 'Solo los errores', 'Una autoevaluación completa organiza la revisión y la mejora.'),
        ('abc', '{F} ¿Qué criterio tiene el menor puntaje?', 'Composición', 'Proceso', 'Comunicación', 'Composición tiene 2 puntos, el menor de la ficha.'),
        ('abc', '{F} ¿Qué evidencia respalda el puntaje de proceso?', '5 versiones registradas', 'El texto pequeño', 'La figura al borde', 'La ficha lo indica para proceso.'),
        ('abc', '{F} ¿Qué falla en una de las dos láminas respecto del propósito?', 'Falta el mensaje', 'Falta la figura', 'Falta el fondo', 'La ficha dice que en una lámina falta el mensaje.'),
        ('=', '{F} ¿Cuántos puntos suma el proceso más la comunicación?', '4+3', 'Se suman los puntajes de esos dos criterios.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos del máximo posible faltan? (4 criterios, hasta 4 puntos cada uno, y la suma de la ficha)', '4*4-(3+2+4+3)', 'El máximo posible es 16 y se resta lo obtenido.', ' puntos'),
        ('=', '{F} Si se hacen las acciones A y B, ¿cuántos minutos se necesitan?', '20+25', 'Se suman los minutos de ambas acciones.', ' minutos'),
        ('abc', '{F} Con 60 minutos útiles, ¿qué plan es posible?', 'Hacer A, B y C, que suman 60 minutos, y dejar 30 para la revisión final', 'Hacer solo A y dejar 40 minutos sin usar', 'Hacer A, B y C y quitar la revisión', 'Las tres acciones suman exactamente 60 minutos, el tiempo disponible.'),
        ('abc', '{F} ¿Cuál acción tiene prioridad si solo hay tiempo para una?', 'La que cumple el propósito, como agregar el mensaje que falta', 'La que más se disfruta', 'La que aparece primero en la lista', 'Se prioriza lo que más afecta al propósito.'),
        ('abc', 'Después de mejorar, ¿cómo se comprueba la mejora?', 'Con una nueva revisión que usa los mismos criterios', 'Preguntando si le gusta a quien hizo el trabajo', 'No es necesario comprobarla', 'Los mismos criterios permiten comparar antes y después.'),
        ('=', 'Una acción A tarda 20 minutos, B 25 y C 15, pero solo hay 50. ¿Cuántos minutos faltan para hacer las tres?', '(20+25+15)-50', 'Se suman las tres acciones y se resta el tiempo disponible.', ' minutos'),
        ('abc', 'Un estudiante dice: «autoevaluarme es presumir». ¿Qué respondes?', 'Es una forma honesta de aprender, con logros y errores', 'Tiene razón, es mejor no hacerlo', 'Solo sirve para sacar buena nota', 'La autoevaluación busca mejorar con evidencia.'),
        ('abc', 'Al final del proyecto, ¿qué puede escribir una estudiante como aprendizaje?', 'Qué haría igual y qué haría distinto en otro proyecto', 'Una lista de quién no ayudó', 'Una queja sobre el tiempo', 'El aprendizaje se centra en mejorar el próximo trabajo.'),
    ],
    ctx=('abc', 'Una estudiante tiene 70 minutos útiles y tres acciones de mejora: de 30, 25 y 20 minutos. No caben las tres. ¿Qué decisión es coherente?', 'Priorizar las acciones que más afectan al propósito, anotar lo que quede pendiente y dejar tiempo para revisar', 'Hacer las tres y no revisar', 'No hacer ninguna', 'Priorizar y declarar lo pendiente es una decisión responsable.'),
    sc=[
        ("En Artes: ¿qué es un plan de mejora?", "Acciones con tiempos para mejorar el trabajo", "Orienta qué se hará y cuándo."),
        ("¿Cómo se prioriza la mejora?", "Primero lo que más afecta al propósito", "Así se aprovecha mejor el tiempo."),
        ("¿Qué se hace después de mejorar?", "Se revisa de nuevo con los mismos criterios", "Permite comprobar si realmente hubo una mejora."),
    ],
    op=("Haz una autoevaluación de un proyecto tuyo o inventado: cuatro criterios con puntaje de 1 a 4 y evidencia, una suma, un plan de mejora con tres acciones y tiempos, y un aprendizaje final.",
        "Proyecto: cartel. Propósito 3 (se entiende el mensaje), composición 3 (la figura está centrada), proceso 2 (solo dos versiones anotadas), comunicación 4 (se lee a 3 metros). Total: 12. Plan: anotar una versión más (10 min), mejorar el fondo (20 min), revisar con un compañero (15 min). Aprendizaje: registraría cada versión desde el inicio.",
        ["criterios con evidencia", "suma y tiempos correctos", "plan priorizado y aprendizaje"],
        ["hoja con la autoevaluación y el plan"],
        ["puntajes sin evidencia", "plan que no cabe en el tiempo"],
        "Pregunta: «¿qué mejora haces primero y por qué?». Si no responde con el propósito, pídele que vuelva a él."),
    reinforce="Escribe tres criterios para evaluar un trabajo tuyo de esta semana, con puntaje de 1 a 4 y una evidencia cada uno.",
    extend="Explica cómo cambiaría tu plan de mejora si el tiempo disponible se redujera a la mitad.",
)
