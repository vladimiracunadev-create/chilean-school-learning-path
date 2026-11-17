"""Artes visuales, audiovisuales y multimediales 3.º y 4.º medio HC: OAC-01 (innovar al resolver desafíos) y OAC-02 (crear obras y proyectos). Fichas y obras inventadas; sin imágenes ni software reales."""
from __future__ import annotations

from hc_avam_common import build

O1 = "AR-AVAM-3y4-OAC-01"
O2 = "AR-AVAM-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (desafío de ejemplo, inventado). Desafío: crear un afiche para la feria del libro de un liceo ficticio. "
     "Propósito: invitar a estudiantes de 1.º a 4.º medio. Restricciones: formato vertical de 40 cm de ancho por 60 cm de alto, dos colores más negro y máximo 12 palabras. "
     "Referente A (afiche ficticio): una sola letra gigante en el centro y mucho espacio vacío. "
     "Referente B (afiche ficticio): collage de recortes de papel de colores con letras de distintos tamaños.")
build(
    O1, 1, F,
    use="Aprenderé a leer un desafío artístico (propósito, público y restricciones) y a observar un referente para entender sus decisiones, sin copiarlo.",
    prior=["Reconozco color, forma y composición.", "Sé describir lo que veo antes de opinar.", "Sé trabajar con límites de tamaño y de tiempo."],
    explain=[
        "Innovar en artes visuales es resolver un desafío con una solución propia que responde a un propósito. Un desafío tiene tres datos que se subrayan antes de crear: el propósito (para qué se hace), el público (para quién) y las restricciones (límites de formato, colores, tiempo o materiales).",
        "Un referente es una obra o un ejemplo que se observa para aprender de las decisiones de quien lo hizo. Observarlo no es copiarlo: se identifica qué decisión tomó (por ejemplo, dejar mucho espacio vacío), qué efecto produce (calma, atención) y si esa idea sirve al propósito propio. Copiar es repetir el resultado sin entender la decisión; innovar es tomar una decisión del referente y cambiarla para resolver tu propio desafío.",
        "En artes visuales se anotan por separado los aspectos expresivos (lo que la obra quiere transmitir) y los estéticos (cómo se ve y se siente: composición, color, forma). Al observar un referente conviene escribir tres cosas: qué veo, qué decisión parece haber tomado su autor y qué efecto produce. Todo se puede hacer en sala con papel y lápiz.",
    ],
    vocab=[("desafío", "problema o encargo que se resuelve con una obra"), ("propósito", "para qué se hace la obra"), ("público", "personas a quienes va dirigida"), ("restricción", "límite de formato, color, tiempo o material"), ("referente", "obra o ejemplo que se observa para aprender de sus decisiones"), ("innovar", "resolver con una solución propia y nueva para quien la crea")],
    worked=[
        ("Leer un desafío", "Un panel ficticio pide: «un cartel para invitar a un taller de fotografía a estudiantes de 3.º medio; tamaño A4; solo blanco y negro». Identifica propósito, público y restricciones.", ["El propósito es invitar al taller.", "El público son estudiantes de 3.º medio; las restricciones son el tamaño A4 y el uso de solo blanco y negro."], "Propósito: invitar; público: 3.º medio; restricciones: A4 y blanco y negro"),
        ("De la observación a la decisión", "El referente A usa una letra gigante y espacio vacío. ¿Qué decisión tomó y qué efecto produce?", ["La decisión es usar una escala muy grande para un solo elemento y dejar el resto vacío.", "El efecto es que la mirada va directo a la letra y el afiche se siente calmado."], "Usó gran escala y vacío; produce foco y calma"),
    ],
    mistakes=[("Copiar la distribución del referente A y solo cambiar la letra.", "No hay una decisión propia: se repitió el resultado sin entender qué lo hacía funcionar.", "Toma la decisión del referente (escala y vacío) y adáptala a tu propósito con un cambio tuyo."),
              ("Empezar a dibujar sin leer las restricciones.", "Después el trabajo puede no caber en el formato o pasarse de colores.", "Subraya propósito, público y restricciones antes de hacer el primer boceto.")],
    T=[
        ('abc', '¿Qué es un referente en artes visuales?', 'Una obra o ejemplo que se observa para aprender de sus decisiones', 'Una copia exacta que se entrega como trabajo propio', 'La nota que el docente pone al terminar el trabajo', 'Un referente se observa para entender decisiones; copiarlo o evaluarlo son otras cosas.'),
        ('abc', '{F} ¿Cuál es el propósito del afiche de la ficha?', 'Invitar a estudiantes de 1.º a 4.º medio a la feria del libro', 'Vender libros al mejor precio de la ciudad', 'Mostrar toda la colección de la biblioteca del liceo', 'La ficha dice que el afiche invita a estudiantes; no habla de vender ni de mostrar la colección.'),
        ('abc', '{F} ¿Cuál de estos datos es una restricción del desafío?', 'Máximo 12 palabras', 'Que el liceo es ficticio', 'Que el referente A tiene una letra gigante', 'Una restricción es un límite del encargo, como el máximo de palabras; los otros datos no limitan la creación.'),
        ('=', '{F} ¿Cuántos centímetros cuadrados tiene la superficie del afiche (ancho por alto)?', '40*60', 'La superficie de un rectángulo se calcula multiplicando ancho por alto.', ' cm²'),
        ('abc', '¿Cuál frase describe innovar a partir de un referente?', 'Entender una decisión del referente y cambiarla para resolver mi propio desafío', 'Reproducir el referente con otros colores', 'Evitar mirar referentes para no parecerme a nadie', 'Innovar usa lo aprendido del referente para una solución propia; reproducir no cambia la decisión.'),
        ('abc', '{F} El referente B combina recortes de colores y letras de varios tamaños. ¿Qué efecto es probable?', 'Se siente movido y juguetón, porque hay muchas formas y tamaños', 'Se siente silencioso y calmo, porque hay poco contenido', 'No produce ningún efecto, porque los recortes son de papel', 'Muchos elementos distintos dan sensación de movimiento; el vacío del referente A es el que da calma.'),
        ('abc', '{F} Un estudiante propone usar cuatro colores más negro. ¿Qué corresponde?', 'Ajustar la propuesta a dos colores, o consultar al docente si cree que se justifica un cambio', 'Dejarla así, porque las restricciones son solo sugerencias', 'Dejarla así si los colores se ven lindos', 'La ficha limita a dos colores más negro; una restricción se cumple o se conversa antes de cambiarla.'),
        ('abc', 'Una estudiante anota «el referente me gustó porque es lindo». ¿Qué le falta para que sea una observación útil?', 'Indicar qué decisión se ve (por ejemplo, el espacio vacío) y qué efecto produce', 'Agregar más adjetivos como «genial» o «increíble»', 'Indicar cuánto costó hacerlo', 'Una observación útil nombra una decisión y su efecto; los adjetivos no se pueden comprobar.'),
        ('=', '{F} Un borrador tiene un título de 4 palabras, una invitación de 6 palabras y la fecha con 3 palabras. ¿Cuántas palabras sobran respecto del máximo?', '4+6+3-12', 'Se suman las palabras del borrador y se restan las 12 permitidas.', ' palabra'),
        ('abc', '{F} ¿Qué propuesta usa el referente A para innovar y no para copiar?', 'Conservar la idea de mucho espacio vacío, pero con un dibujo pequeño de un libro abierto en lugar de una letra', 'Poner la misma letra gigante en el mismo lugar, solo que con otra letra del abecedario', 'Calcar el afiche A y pintarlo con otro color', 'Mantiene la decisión del vacío y cambia el elemento principal; las otras dos solo repiten el resultado.'),
        ('abc', 'El desafío pide «un cartel para un taller de fotografía» y no dice el tamaño. ¿Qué es lo más adecuado?', 'Preguntar al docente o anotar un supuesto razonable y declararlo en el trabajo', 'Inventar un tamaño y no mencionarlo', 'Dejar el trabajo sin hacer hasta que alguien lo decida', 'Cuando falta un dato se pregunta o se declara el supuesto; así quien evalúa entiende la decisión.'),
        ('abc', '{F} Para comparar los referentes A y B con el propósito, ¿qué pregunta es la más útil?', '¿Cuál invita mejor a estudiantes de 1.º a 4.º medio, y por qué decisión visual?', '¿Cuál de los dos tiene más elementos?', '¿Cuál de los dos me gusta más?', 'La pregunta útil conecta el referente con el propósito; contar elementos o el gusto personal no lo hacen.'),
        ('abc', 'Un compañero dice que un referente se mira solo al final, cuando la obra ya está terminada. ¿Qué respondes?', 'Se observa al comienzo para decidir con información y se vuelve a mirar al revisar', 'Tiene razón, porque mirarlo antes limita la creatividad', 'Nunca hay que mirar referentes', 'Observar referentes al inicio aporta ideas y criterios; al final sirve para comparar y revisar.'),
    ],
    ctx=('abc', 'Una estudiante escribe sobre la ficha: «Propósito: invitar. Público: 1.º a 4.º medio. Del referente A tomo el espacio vacío para destacar una palabra, y mi cambio es escribirla en dos colores». ¿Qué cumple bien su registro?', 'Nombra propósito y público, una decisión del referente y un cambio propio', 'Copia el referente completo y solo cambia el color', 'Ignora el propósito y se centra en lo que le gusta', 'El registro identifica propósito, público, decisión tomada del referente y una modificación propia.'),
    sc=[
        ("En Artes visuales: ¿qué es una restricción de un desafío?", "Un límite de formato, color, tiempo o material", "Las restricciones se leen antes de crear para que la propuesta sea posible."),
        ("¿Qué se anota al observar un referente?", "Qué veo, qué decisión tomó su autor y qué efecto produce", "Así se aprende de la decisión y no solo del resultado."),
        ("¿Qué diferencia hay entre copiar e innovar?", "Copiar repite el resultado; innovar toma una decisión y la cambia para el propio desafío", "Innovar exige entender la decisión del referente y adaptarla."),
    ],
    op=("Inventa un desafío breve (por ejemplo, un cartel para invitar a una actividad de tu curso) y escribe su propósito, público y dos restricciones. Luego describe un referente imaginario en dos líneas y anota qué decisión tomó, qué efecto produce y qué cambio propio harías.",
        "Desafío: cartel para invitar a la muestra de arte del curso. Propósito: invitar. Público: estudiantes y familias. Restricciones: tamaño A3 y tres colores. Referente imaginario: cartel con una figura grande y fondo liso. Decisión: escala grande; efecto: foco. Cambio propio: la figura estará formada por palabras pequeñas.",
        ["identifica propósito, público y restricciones", "describe una decisión del referente y su efecto", "propone un cambio propio, no una copia"],
        ["hoja con el desafío, el referente y el cambio propuesto"],
        ["usar solo adjetivos como «lindo»", "no incluir restricciones", "repetir el referente sin cambio"],
        "Pregunta: «¿qué decisión del referente tomaste y qué cambiaste tú?». Si no distingue ambas, pídele que las separe."),
    reinforce="Elige un afiche o paquete que tengas en casa y anota su propósito probable, su público y una decisión visual que veas. No necesitas copiarlo.",
    extend="Explica con un ejemplo inventado por qué dos personas pueden resolver el mismo desafío con soluciones distintas y ambas innovar.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (registro de pruebas de ejemplo, inventado). Desafío: un cartel que se lea a 3 metros. "
     "Prueba 1: soporte cartulina blanca, procedimiento lápiz grafito, 10 minutos; resultado: línea fina y precisa, no se lee a 3 metros. "
     "Prueba 2: soporte papel kraft (café), procedimiento recorte y pegado de papel blanco, 25 minutos; resultado: formas claras, se leen a 3 metros. "
     "Prueba 3: soporte cartulina blanca, procedimiento estampado con goma eva pegada en un cartón y témpera lavable, 20 minutos; resultado: texturas repetidas, borde algo manchado, se lee bien solo de cerca.")
build(
    O1, 2, F,
    use="Aprenderé a explorar soportes y procedimientos con pruebas pequeñas y a registrar sus resultados para decidir con evidencia.",
    prior=["Sé leer un desafío y sus restricciones.", "Sé observar un referente.", "Reconozco materiales escolares seguros."],
    explain=[
        "Un soporte es la superficie o el medio donde se hace la obra: papel, cartulina, tela, un muro o una pantalla. Un procedimiento es la manera de trabajar sobre el soporte: dibujo, collage, estampado, fotografía o edición digital. El material es lo que se usa para hacerlo, como el grafito o la témpera. Un mismo diseño cambia mucho de aspecto si cambian el soporte o el procedimiento.",
        "Explorar es probar en pequeño antes de decidir. Cada prueba se registra con cuatro datos: soporte, procedimiento, tiempo y resultado. Para saber qué produjo una diferencia, se cambia una sola variable por prueba y se deja todo lo demás igual. El resultado se juzga con el propósito del desafío (por ejemplo, que se lea a 3 metros) y no solo con el gusto.",
        "La exploración en sala usa materiales escolares seguros: témpera lavable, pegamento en barra, papel y tijeras de punta roma, en un lugar ventilado. No se usan solventes, aerosoles, calor ni objetos cortantes. Si un material irrita o hay dudas sobre él, se detiene el trabajo y se avisa a una persona adulta.",
    ],
    vocab=[("soporte", "superficie o medio donde se hace la obra"), ("procedimiento", "manera de trabajar sobre el soporte"), ("material", "lo que se usa para hacer la obra"), ("prueba", "ensayo pequeño para ver qué resulta"), ("variable", "aspecto que se cambia en una prueba"), ("registro", "anotación de lo que se probó y resultó")],
    worked=[
        ("Elegir según el propósito", "Con la ficha, ¿qué prueba cumple el propósito de leerse a 3 metros?", ["Se buscan resultados que digan «se lee a 3 metros».", "Solo la prueba 2 lo dice; la 1 no se lee y la 3 solo de cerca."], "La prueba 2"),
        ("Sumar tiempos", "¿Cuántos minutos suman las pruebas 1 y 3?", ["La prueba 1 dura 10 minutos y la prueba 3 dura 20.", "10 + 20 = 30."], "30 minutos"),
    ],
    mistakes=[("Cambiar soporte, procedimiento y material a la vez y atribuir el resultado a uno solo.", "No se sabe cuál de los cambios produjo la diferencia.", "Cambia una variable por prueba y deja el resto igual."),
              ("Elegir el procedimiento solo porque fue el más rápido.", "La rapidez no garantiza que cumpla el propósito del desafío.", "Compara cada resultado con el propósito y luego considera el tiempo disponible.")],
    T=[
        ('abc', '¿Qué es un soporte?', 'La superficie o el medio donde se hace la obra', 'La manera de trabajar, como dibujar o estampar', 'El tiempo que demora hacer la obra', 'El soporte es donde se hace la obra; la manera de trabajar es el procedimiento.'),
        ('abc', '{F} ¿Qué procedimiento se usó en la prueba 3?', 'Estampado con goma eva y témpera', 'Recorte y pegado de papel blanco', 'Dibujo con lápiz grafito', 'La ficha dice que la prueba 3 estampó con goma eva pegada en un cartón y témpera lavable.'),
        ('abc', '{F} ¿Qué soporte tuvo la prueba 2?', 'Papel kraft', 'Cartulina blanca', 'Pantalla de computador', 'La ficha indica papel kraft en la prueba 2; la cartulina blanca fue el soporte de las pruebas 1 y 3.'),
        ('=', '{F} ¿Cuántos minutos suman las tres pruebas de la ficha?', '10+25+20', 'Se suman los minutos de cada prueba.', ' minutos'),
        ('abc', '¿Por qué se cambia una sola variable por prueba?', 'Para saber qué cambio produjo la diferencia en el resultado', 'Para gastar menos papel y terminar antes de la hora', 'Porque las reglas de la sala no permiten cambiar más', 'Con un solo cambio por prueba se puede atribuir el resultado a esa variable.'),
        ('abc', '{F} Quieres saber si el soporte influye en el estampado. ¿Qué haces?', 'Repetir la prueba 3 sobre papel kraft, con el mismo procedimiento y el mismo tiempo', 'Repetir la prueba 3 con otro procedimiento y otro soporte a la vez', 'Repetir la prueba 1 con lápiz y comparar con la 3', 'Para aislar el soporte se cambia solo el soporte y todo lo demás se mantiene.'),
        ('abc', '¿Cuál es un material adecuado para explorar en sala?', 'Témpera lavable y tijeras de punta roma', 'Pintura en aerosol en una sala cerrada', 'Un cuchillo cortante para recortar rápido', 'La témpera lavable y las tijeras de punta roma son seguras; los aerosoles y el cuchillo no lo son.'),
        ('abc', '{F} Una compañera anota «la prueba 2 quedó mejor». ¿Qué le falta a su registro?', 'Un criterio ligado al propósito, como que se lee a 3 metros', 'Más adjetivos sobre lo bonito que quedó', 'El nombre de la marca de papel', 'Sin criterio, «mejor» es una opinión; el propósito del cartel da el criterio para decidir.'),
        ('=', 'La clase dura 90 minutos y se reservan 30 para ordenar y registrar. Cada prueba demora 15 minutos. ¿Cuántas pruebas caben?', '(90-30)//15', 'Se restan los minutos reservados y se divide por lo que dura cada prueba.', ' pruebas'),
        ('abc', '¿Qué diferencia hay entre material y procedimiento?', 'El material es lo que se usa (témpera) y el procedimiento es cómo se trabaja (estampar)', 'Son lo mismo con dos nombres', 'El material es la manera de trabajar y el procedimiento es el objeto que se usa', 'El material es el objeto o sustancia; el procedimiento es la manera de trabajar con él.'),
        ('abc', '{F} La prueba 1 no sirve para el cartel de 3 metros. ¿Qué conclusión es correcta?', 'Sirve para bocetos de cerca, pero no para ese cartel', 'No sirve para ningún trabajo artístico', 'Sirve para el cartel porque es la más rápida', 'Su resultado se juzga con el propósito: no cumple el de lectura a distancia, pero puede servir para otros usos.'),
        ('abc', 'Para registrar una prueba con claridad, ¿qué anotas?', 'Soporte, procedimiento, tiempo y resultado', 'Solo si te gustó o no', 'Solo el nombre del material', 'Cuatro datos permiten repetir y comparar la prueba; el gusto no basta.'),
        ('abc', 'Un estudiante dice que probar es perder tiempo y usa el primer procedimiento que se le ocurre. ¿Qué riesgo corre?', 'Descubrir tarde que su elección no cumple el propósito o las restricciones', 'Ninguno, porque la primera idea siempre es la mejor', 'Gastar demasiado papel y nada más', 'Sin pruebas no hay evidencia para decidir, y los problemas aparecen cuando ya es difícil corregir.'),
    ],
    ctx=('abc', 'Un grupo debe lograr un cartel para leerse a 3 metros en 45 minutos. Tienen los resultados de la ficha. ¿Qué decisión es coherente?', 'Elegir la prueba 2, que cumple la lectura a distancia y cabe en 45 minutos', 'Elegir la prueba 3, porque tiene más textura aunque solo se lee de cerca', 'Elegir la prueba 1, porque es la más rápida aunque no se lee a 3 metros', 'La prueba 2 cumple el propósito y tarda 25 minutos; las otras no cumplen la lectura a distancia.'),
    sc=[
        ("En Artes visuales: ¿qué es un procedimiento?", "La manera de trabajar sobre un soporte", "Dibujar, estampar o recortar son procedimientos."),
        ("¿Cuántas variables se cambian por prueba?", "Una", "Así se sabe qué produjo la diferencia."),
        ("¿Con qué se juzga el resultado de una prueba?", "Con el propósito del desafío", "El propósito da un criterio común para comparar."),
    ],
    op=("Elige un desafío sencillo (por ejemplo, un cartel que se lea a 2 metros) y planifica dos pruebas que cambien solo una variable. Escribe un registro de cada una con soporte, procedimiento, tiempo y resultado esperado. Si puedes, hazlas con materiales escolares seguros.",
        "Desafío: cartel legible a 2 metros. Prueba A: cartulina, letras con marcador grueso, 8 minutos, resultado esperado: se lee. Prueba B: igual pero con marcador fino, 8 minutos, resultado esperado: se lee peor. Variable cambiada: grosor del marcador.",
        ["cambia una sola variable", "registra los cuatro datos", "juzga con el propósito"],
        ["hoja con dos registros de prueba"],
        ["cambiar varias variables", "juzgar solo por gusto"],
        "Pregunta: «¿qué cambiaste entre las dos pruebas?». Si nombra más de una variable, pídele que deje una."),
    reinforce="Con una hoja de papel y un lápiz, dibuja una misma figura simple con presión suave y con presión fuerte. Anota qué cambia a una distancia de 2 metros.",
    extend="Explica por qué un procedimiento puede ser excelente para un propósito y mala idea para otro.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (matriz de decisión de ejemplo, inventada). Desafío: portada para el diario mural de un curso ficticio. "
     "Criterios y pesos: se lee de lejos (peso 3), cumple la restricción de 3 colores (peso 2), es original (peso 1). "
     "Cada idea recibe un puntaje de 1 a 3 en cada criterio. "
     "Idea X (letras grandes en bloques de color): se lee de lejos 3, colores 3, original 1. "
     "Idea Y (collage de fotografías recortadas de revistas viejas): se lee de lejos 1, colores 2, original 3. "
     "Idea Z (figura central grande con una sola palabra): se lee de lejos 3, colores 3, original 2.")
build(
    O1, 3, F,
    use="Aprenderé a tomar una decisión visual con criterios: comparar ideas con una matriz, ponderar lo importante y justificar la elección.",
    prior=["Sé explorar soportes y procedimientos.", "Sé multiplicar y sumar números pequeños.", "Sé distinguir propósito y gusto."],
    explain=[
        "Una decisión visual es una elección que cambia cómo se ve y se entiende una obra: color, composición, tamaño, tipografía o soporte. Para decidir con criterio se definen primero los criterios, que son las cualidades que la solución debe tener según el propósito (por ejemplo, que se lea de lejos). Los criterios se ordenan por importancia con un peso: un criterio de peso 3 importa más que uno de peso 1.",
        "Una matriz de decisión es una tabla donde cada idea recibe un puntaje en cada criterio. El puntaje de un criterio se multiplica por su peso y luego se suman todos los resultados: ese es el puntaje total de la idea. La matriz ayuda a comparar, pero no decide sola: si un resultado parece injusto, se revisan los criterios, los pesos o los puntajes y se explica el cambio.",
        "Toda decisión se justifica con una frase que une criterio, evidencia y efecto: «Elijo la idea Z porque se lee de lejos (3) y mantiene los tres colores, y su efecto es claridad». Justificar con «porque me gusta» no basta en un proyecto con propósito. Una decisión también se puede cambiar si una prueba posterior muestra que no funciona.",
    ],
    vocab=[("criterio", "cualidad que la solución debe tener según el propósito"), ("peso", "número que indica la importancia de un criterio"), ("matriz de decisión", "tabla que compara ideas según criterios"), ("puntaje total", "suma de puntaje por peso de cada criterio"), ("justificar", "explicar una decisión con criterio y evidencia")],
    worked=[
        ("Calcular un puntaje total", "Con la ficha, calcula el puntaje total de la idea X.", ["Se lee de lejos: 3 × 3 = 9. Colores: 3 × 2 = 6. Original: 1 × 1 = 1.", "Suma: 9 + 6 + 1 = 16."], "16 puntos"),
        ("Justificar con criterio", "La idea Y obtiene 1×3 + 2×2 + 3×1 = 10. ¿Por qué no es la elegida?", ["Su puntaje (10) es menor que el de X (16) y el de Z (17).", "Falla justo en el criterio de mayor peso: se lee de lejos solo 1."], "Porque falla en el criterio de mayor peso, leerse de lejos"),
    ],
    mistakes=[("Elegir la idea con el mejor puntaje en un solo criterio.", "Puede fallar en los criterios de más peso y no cumplir el propósito.", "Calcula el puntaje total ponderado y revisa los criterios importantes."),
              ("Cambiar los pesos después de ver los resultados para que gane la idea favorita.", "Se justifica la preferencia, no el propósito.", "Fija los criterios y pesos antes de puntuar; si los cambias, explica por qué.")],
    T=[
        ('abc', '¿Qué es un criterio en una decisión visual?', 'Una cualidad que la solución debe tener según el propósito', 'La opinión de la persona que más habla en el grupo', 'El material que se tiene más a mano', 'El criterio sale del propósito; no es una opinión ni una comodidad.'),
        ('abc', '{F} ¿Cuál criterio tiene más peso en la ficha?', 'Que se lea de lejos', 'Que sea original', 'Que use fotografías de revistas', 'El criterio de lectura a distancia tiene peso 3, el mayor de la ficha.'),
        ('abc', '{F} ¿Qué puntaje obtiene la idea Y en originalidad?', '3', '1', '2', 'La ficha le asigna 3 en originalidad a la idea Y.'),
        ('=', '{F} Calcula el puntaje total de la idea Z: puntaje por peso en cada criterio y suma.', '3*3+3*2+2*1', 'Se multiplica cada puntaje por su peso y se suman los tres resultados.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos más que la idea Y tiene la idea X en el total?', '(3*3+3*2+1*1)-(1*3+2*2+3*1)', 'X suma 16 e Y suma 10; se restan los totales.', ' puntos'),
        ('abc', '{F} ¿Qué idea tiene el mayor puntaje total?', 'La idea Z', 'La idea X', 'La idea Y', 'Z suma 9+6+2 = 17, X suma 16 e Y suma 10.'),
        ('abc', '{F} El curso decide que la originalidad pase a peso 3 y la lectura de lejos a peso 1, después de ver el resultado, porque le gusta la idea Y. ¿Qué problema tiene?', 'Cambia los pesos para favorecer una idea y no por el propósito', 'Ninguno, porque los pesos son libres', 'Que la originalidad no se puede puntuar', 'Cambiar los pesos al ver el resultado justifica una preferencia en vez de aplicar el propósito.'),
        ('abc', 'Una estudiante justifica: «Elijo mi idea porque me gusta». ¿Qué le falta?', 'Nombrar criterios del propósito y la evidencia que los cumple', 'Decir que a más personas también les gusta', 'Aumentar el tamaño de la letra', 'Una justificación une criterio y evidencia con el efecto buscado.'),
        ('abc', '{F} Dos ideas empatan en puntaje total. ¿Qué es lo más razonable?', 'Revisar cuál cumple mejor el criterio de mayor peso o hacer una prueba corta de las dos', 'Elegir al azar sin decir por qué', 'Elegir la que propuso la persona con más años', 'Un empate se resuelve con el criterio más importante o con evidencia adicional.'),
        ('=', 'Una matriz tiene dos criterios: claridad (peso 2) y color (peso 1). Una idea obtiene 3 en claridad y 2 en color. ¿Cuál es su puntaje total?', '3*2+2*1', 'Se multiplica cada puntaje por su peso y se suman.', ' puntos'),
        ('abc', 'Una decisión visual es', 'una elección que cambia cómo se ve y se entiende la obra', 'una opinión que no afecta el resultado de la obra', 'el nombre que se pone a la obra al final', 'Color, composición o soporte son decisiones visuales porque afectan la obra.'),
        ('abc', '{F} Después de elegir, una prueba muestra que la idea Z no se lee bien porque el papel brilla. ¿Qué corresponde?', 'Revisar la decisión y probar otro soporte o procedimiento, explicando el cambio', 'Mantenerla igual para no perder lo ya trabajado', 'Eliminar el criterio de lectura de lejos', 'Una decisión se puede revisar si la evidencia nueva la contradice, dejando registro del cambio.'),
        ('abc', 'Para justificar una decisión de forma completa, ¿qué orden sirve?', 'Criterio, evidencia y efecto', 'Gusto, tiempo y precio', 'Nombre de la obra, fecha y autora', 'Criterio, evidencia y efecto explican por qué la decisión cumple el propósito.'),
    ],
    ctx=('abc', 'Un grupo agrega un criterio: «es fácil de repetir en 10 carteles» con peso 2. La idea X lo cumple con 3, la Y con 1 y la Z con 2. ¿Cómo se actualiza la comparación?', 'Se suma a cada total el puntaje multiplicado por 2 y se comparan de nuevo los tres totales', 'Se ignora el criterio nuevo porque ya hay resultados', 'Se elige la idea X sin calcular, porque obtuvo 3', 'Un criterio nuevo se incorpora con su peso a todas las ideas, no solo a una.'),
    sc=[
        ("En Artes visuales: ¿qué es una matriz de decisión?", "Una tabla que compara ideas según criterios con pesos", "La matriz ordena la comparación, pero no decide sola."),
        ("¿Cómo se calcula el puntaje total de una idea?", "Multiplicando cada puntaje por su peso y sumando", "Así los criterios importantes pesan más."),
        ("¿Qué incluye una buena justificación?", "Criterio, evidencia y efecto", "Eso conecta la decisión con el propósito."),
    ],
    op=("Elige un desafío breve y escribe tres criterios con pesos (1 a 3). Propón dos ideas y puntúalas de 1 a 3. Calcula el puntaje total y escribe una justificación de una frase que use criterio, evidencia y efecto.",
        "Desafío: ilustración para una invitación. Criterios: se entiende rápido (peso 3), cabe en A5 (peso 2), usa dos colores (peso 1). Idea 1: 3, 3, 2 = 9+6+2 = 17. Idea 2: 2, 3, 3 = 6+6+3 = 15. Elijo la idea 1 porque se entiende rápido (3) y mantiene el formato.",
        ["define criterios con pesos", "calcula bien los totales", "justifica con criterio y evidencia"],
        ["hoja con la matriz y la justificación"],
        ["pesos cambiados a posteriori", "justificar solo con gusto"],
        "Pregunta: «¿qué criterio pesó más en tu elección?». Si no responde, pídele que lo señale en su matriz."),
    reinforce="Escribe una matriz con dos ideas para decorar un cuaderno y tres criterios con pesos. Calcula los totales dos veces.",
    extend="Explica una situación en que la matriz de decisión te llevaría a una elección que no te convence y qué harías con eso.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (plan de proyecto de ejemplo, inventado). Desafío: una serie de 3 láminas que inviten a cuidar el patio del liceo. "
     "Propósito: que estudiantes de 1.º a 4.º medio recojan su basura. Decisión visual tomada: una sola figura repetida en tres tamaños. "
     "Plan: boceto (30 minutos), prueba de color (20 minutos), lámina 1 (40 minutos), lámina 2 (40 minutos), lámina 3 (40 minutos), revisión con un compañero (20 minutos). "
     "Retroalimentación recibida de un compañero: «la figura se entiende, pero el texto es pequeño».")
build(
    O1, 4, F,
    use="Aprenderé a desarrollar una propuesta propia: planificar los pasos, usar la retroalimentación de otros y evaluar críticamente mi proceso y mi resultado.",
    prior=["Sé decidir con criterios.", "Sé registrar pruebas.", "Sé que copiar no es innovar."],
    explain=[
        "Desarrollar una propuesta propia es pasar de la idea elegida a una obra terminada, con un plan. Un plan incluye pasos, tiempos y el propósito que guía cada decisión. Se escribe antes de empezar y se ajusta si algo cambia: un plan flexible no es un plan fallido. El tiempo total se calcula sumando los tiempos de cada paso, para saber si cabe en las clases disponibles.",
        "Innovar no exige inventar algo nunca visto; exige que la solución sea propia: toma decisiones sobre el propósito, no repite un referente. Una evaluación crítica revisa el proceso (cómo se decidió y qué se probó) y el resultado (si cumple el propósito). Se hace de dos formas: personal (autoevaluación) y de otros (retroalimentación de pares). La retroalimentación útil describe lo que se ve, dice qué efecto produce y sugiere un cambio.",
        "Las críticas se reciben como información sobre la obra, no como juicio sobre la persona. Quien recibe una crítica decide qué cambiar y lo justifica. Quien la da lo hace con respeto, sin comparaciones entre personas ni burlas. Si un comentario hiere o incomoda, se avisa a una persona adulta de confianza.",
    ],
    vocab=[("plan", "pasos y tiempos para llegar a la obra"), ("proceso", "camino de decisiones y pruebas hasta la obra"), ("resultado", "obra terminada"), ("autoevaluación", "revisión crítica del propio trabajo"), ("retroalimentación", "comentario de otra persona para mejorar"), ("evaluación crítica", "revisión con criterios del proceso y el resultado")],
    worked=[
        ("Calcular el tiempo total", "Con la ficha, ¿cuántos minutos suma el plan?", ["Se suman todos los pasos: 30 + 20 + 40 + 40 + 40 + 20.", "El total es 190 minutos."], "190 minutos"),
        ("Usar una crítica", "El compañero dice que el texto es pequeño. ¿Cómo responde bien quien hizo la lámina?", ["Se acepta como información sobre la obra y se mira el propósito: debe leerse en el patio.", "Se decide agrandar el texto y se anota el cambio en el registro."], "Agranda el texto y registra el cambio"),
    ],
    mistakes=[("Defender la obra y desechar la crítica sin revisarla.", "Se pierde información sobre cómo la ve el público.", "Revisa la crítica con el propósito y decide qué cambiar, anotando por qué."),
              ("Aceptar todas las críticas sin pensar si sirven al propósito.", "La obra puede dejar de ser propia y perder coherencia.", "Elige los cambios que mejoran el propósito y explica los que descartas.")],
    T=[
        ('abc', '¿Qué es una evaluación crítica?', 'Una revisión con criterios del proceso y del resultado', 'Una lista de defectos de la persona autora', 'Una nota final sin explicación', 'La evaluación crítica usa criterios para revisar lo hecho; no juzga a la persona.'),
        ('abc', '{F} ¿Qué decisión visual tomó el proyecto de la ficha?', 'Repetir una sola figura en tres tamaños', 'Usar fotografías de personas del liceo', 'Cambiar el soporte en cada lámina', 'La ficha indica una figura repetida en tres tamaños.'),
        ('abc', '{F} ¿Qué dijo el compañero que revisó el trabajo?', 'Que la figura se entiende pero el texto es pequeño', 'Que la figura es difícil de entender', 'Que faltan colores', 'La retroalimentación de la ficha valora la figura y pide mayor texto.'),
        ('=', '{F} ¿Cuántos minutos suman solo las tres láminas del plan?', '3*40', 'Cada lámina toma 40 minutos y son tres.', ' minutos'),
        ('=', '{F} Si hay 4 clases de 45 minutos, ¿cuántos minutos sobran o faltan? Escribe el resultado como sobra (positivo) o falta (negativo).', '4*45-(30+20+40+40+40+20)', 'Se restan los 190 minutos del plan a los 180 minutos disponibles, y el resultado negativo indica que faltan.', ' minutos'),
        ('abc', '{F} Con 180 minutos disponibles y un plan de 190, ¿qué decisión es razonable?', 'Reducir un paso o pedir diez minutos más, y anotar el ajuste', 'Ignorar los diez minutos y no cambiar nada', 'Eliminar la revisión con un compañero sin avisar', 'Un plan se ajusta cuando no cabe en el tiempo, cuidando los pasos que sostienen el propósito.'),
        ('abc', 'Un estudiante recibe una crítica y responde «tú no sabes nada de arte». ¿Qué problema hay?', 'Descarta la información y ataca a la persona, en vez de revisar la obra', 'Ninguno, porque tiene derecho a su opinión', 'Que no usó la palabra «crítica»', 'La crítica se revisa con el propósito; responder atacando bloquea la mejora.'),
        ('abc', '{F} ¿Cuál es una retroalimentación útil para la ficha?', 'La figura se entiende; el texto se lee mal desde lejos; prueba un tamaño mayor', 'Me gustó, está bien', 'Yo lo habría hecho mejor', 'Describe, indica el efecto y sugiere un cambio; las otras opciones no entregan información.'),
        ('abc', '{F} El compañero también dice: «el color es feo». ¿Cómo se usa ese comentario?', 'Se pregunta qué efecto produce y se revisa si cumple el propósito antes de cambiar', 'Se cambia el color de inmediato sin preguntar', 'Se ignora, porque todo gusto es subjetivo', 'Un juicio de gusto se vuelve útil si se pide la razón y se contrasta con el propósito.'),
        ('=', 'Una lámina requiere 40 minutos, pero una prueba corta muestra que se necesita un 25 % más de tiempo. ¿Cuántos minutos necesita?', '40*125//100', 'Se calcula el 125 % de 40 minutos.', ' minutos'),
        ('abc', 'Quien da una retroalimentación debe', 'describir lo que ve, decir el efecto y sugerir un cambio con respeto', 'comparar la obra con la de otra persona del curso', 'decir solo lo que le gusta para no incomodar', 'Una crítica útil es específica y respetuosa; comparar personas no ayuda a mejorar.'),
        ('abc', 'Un comentario de un compañero te hiere y te cuesta seguir trabajando. ¿Qué haces?', 'Avisas a una persona adulta de confianza y sigues revisando la obra con los comentarios útiles', 'Respondes con otro comentario hiriente', 'Abandonas el proyecto sin avisar', 'El respeto es parte de la crítica; avisar a un adulto cuida a las personas y permite continuar.'),
        ('abc', 'La evaluación personal de un proyecto revisa', 'tanto el proceso como el resultado, con criterios del propósito', 'solo la nota que se espera obtener', 'solo si la obra se parece a un referente', 'La autoevaluación examina decisiones y resultado; la nota o el parecido no bastan.'),
    ],
    ctx=('abc', 'Al terminar el proyecto, una estudiante escribe: «Cumplí el propósito en 2 de 3 láminas: el texto se lee a 3 metros en las láminas 2 y 3, pero no en la 1. Rehago el texto de la 1». ¿Qué tiene de bueno su evaluación?', 'Usa el propósito como criterio, da evidencia y define un cambio concreto', 'Dice que todo salió bien sin evidencia', 'Culpa a la persona que dio la crítica', 'La evaluación nombra criterio, evidencia (qué láminas se leen) y acción de mejora.'),
    sc=[
        ("En Artes visuales: ¿qué es retroalimentación?", "Un comentario de otra persona para mejorar el trabajo", "Describe, indica el efecto y sugiere un cambio."),
        ("¿Qué revisa una evaluación crítica?", "El proceso y el resultado, con criterios", "Ambos muestran si se cumplió el propósito."),
        ("¿Qué se hace con una crítica que hiere?", "Se avisa a una persona adulta de confianza", "El respeto es parte de trabajar en grupo."),
    ],
    op=("Planifica una serie de 2 láminas para un propósito que elijas. Escribe cuatro pasos con sus minutos, suma el total y escribe una autoevaluación de dos líneas con un criterio y un cambio para mejorar.",
        "Serie: 2 láminas para cuidar el agua. Pasos: boceto 25 min, prueba de color 15 min, lámina 1 35 min, lámina 2 35 min. Total: 110 min. Autoevaluación: se entiende el mensaje, pero el texto no se lee desde lejos. Cambio: texto de mayor tamaño.",
        ["plan con tiempos sumados bien", "autoevaluación con criterio", "propone un cambio concreto"],
        ["hoja con el plan y la autoevaluación"],
        ["no sumar tiempos", "evaluación sin criterio"],
        "Pregunta: «¿qué criterio usaste para evaluar tu trabajo?». Si no tiene uno, ayúdalo a partir del propósito."),
    reinforce="Escribe tres pasos y sus minutos para un trabajo artístico pequeño que quieras hacer. Suma el total y compáralo con el tiempo que tienes.",
    extend="Explica por qué una crítica útil puede venir de alguien que no es experto en arte y qué debe tener para serlo.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 5 (necesidades de ejemplo, inventadas). "
     "Caso A: un curso ficticio quiere un mural de papel para dar la bienvenida a estudiantes nuevos (comunicación grupal). "
     "Caso B: una estudiante ficticia quiere expresar su nostalgia por su barrio con una serie de fotografías en blanco y negro (expresión personal). "
     "Caso C: un grupo ficticio necesita un video corto de 60 segundos que explique cómo reciclar papel en el liceo (comunicación a una comunidad).")
build(
    O2, 1, F,
    use="Aprenderé a partir de una necesidad de expresión o de comunicación, personal o grupal, y a convertirla en un proyecto con mensaje, destinatario y formato.",
    prior=["Sé leer un desafío y definir un propósito.", "Sé observar referentes.", "Sé explorar soportes y procedimientos."],
    explain=[
        "Toda obra nace de una necesidad. La necesidad de expresión surge cuando alguien quiere dar forma a una emoción, una idea o una experiencia propia (por ejemplo, la nostalgia por un lugar). La necesidad de comunicación surge cuando se quiere informar, invitar o convencer a otras personas. Muchas obras mezclan ambas, y pueden ser personales o grupales.",
        "Para convertir una necesidad en proyecto se responde tres preguntas: qué quiero decir (mensaje), a quién (destinatario) y con qué formato (afiche, mural, serie de fotografías, video, página interactiva). El formato se elige según el mensaje y el destinatario: un video de 60 segundos explica pasos; una serie de fotografías evoca un ambiente. Un mensaje claro se puede escribir en una frase.",
        "En los proyectos con otras personas se acuerda quién hace qué y se pide permiso para usar imágenes, nombres o lugares de terceros. Si el proyecto muestra a personas, se pide su consentimiento. Todo el trabajo de este curso puede hacerse con materiales seguros y obras propias.",
    ],
    vocab=[("necesidad de expresión", "querer dar forma a una emoción o idea propia"), ("necesidad de comunicación", "querer informar, invitar o convencer a otros"), ("mensaje", "idea central que la obra quiere transmitir"), ("destinatario", "persona o grupo a quien va dirigida la obra"), ("formato", "tipo de obra: afiche, mural, fotografía, video, página"), ("consentimiento", "permiso de una persona para usar su imagen")],
    worked=[
        ("Clasificar la necesidad", "En la ficha, ¿qué tipo de necesidad tiene el caso B?", ["La estudiante quiere dar forma a su nostalgia, una emoción propia.", "Es una necesidad de expresión personal."], "Expresión personal"),
        ("Escribir un mensaje", "Para el caso C, escribe el mensaje en una frase.", ["La idea central es cómo reciclar papel en el liceo.", "Una frase: «Separar el papel limpio y llevarlo al punto de reciclaje es fácil»."], "Separar el papel limpio y llevarlo al punto de reciclaje es fácil"),
    ],
    mistakes=[("Elegir primero el formato (por ejemplo, un video) sin pensar en el mensaje.", "El formato puede no servir al propósito ni al destinatario.", "Escribe primero el mensaje y el destinatario, y luego elige el formato."),
              ("Tomar fotografías de personas del barrio sin pedirles permiso.", "Se vulnera su privacidad y puede haber consecuencias.", "Pide consentimiento y, si no se puede, no muestres a las personas o usa un modelo que lo autorice.")],
    T=[
        ('abc', '¿Qué es una necesidad de expresión?', 'Querer dar forma a una emoción o experiencia propia', 'Querer informar horarios y fechas a una comunidad', 'Querer vender un producto', 'La expresión da forma a lo propio; informar es comunicación.'),
        ('abc', '{F} ¿Qué tipo de necesidad tiene el caso A?', 'De comunicación grupal', 'De expresión personal', 'De venta de un producto', 'Un curso quiere dar la bienvenida: es comunicación hecha en grupo.'),
        ('abc', '{F} ¿Cuál es el destinatario del caso C?', 'La comunidad del liceo', 'Una sola estudiante', 'Un museo ficticio', 'El video busca explicar el reciclaje a quienes están en el liceo.'),
        ('=', '{F} El video del caso C dura 60 segundos y se divide en 4 partes iguales. ¿Cuántos segundos dura cada parte?', '60//4', 'Se divide el tiempo total en partes iguales.', ' segundos'),
        ('abc', '¿Qué es un mensaje en un proyecto artístico?', 'La idea central que quiere transmitir la obra', 'El nombre del material usado', 'La cantidad de personas del grupo', 'El mensaje se puede decir en una frase; no es material ni cantidad.'),
        ('abc', '{F} ¿Qué formato es más coherente con la necesidad del caso B?', 'Una serie de fotografías en blanco y negro, porque evoca un ambiente', 'Un video explicativo de pasos numerados', 'Un afiche con instrucciones', 'La nostalgia por un lugar se evoca con imágenes; las instrucciones no la expresan.'),
        ('abc', '{F} El grupo del caso C quiere mostrar a compañeros reciclando. ¿Qué debe hacer primero?', 'Pedirles su consentimiento antes de grabarlos', 'Grabarlos y pedir permiso después', 'Grabarlos sin que lo sepan para que sea natural', 'El consentimiento va antes de grabar o fotografiar a una persona.'),
        ('abc', 'Una estudiante dice que primero eligió hacer un video y después verá qué decir. ¿Qué le recomiendas?', 'Escribir el mensaje y el destinatario y luego decidir si el video es el mejor formato', 'Seguir con el video porque el formato manda', 'Cambiar a un afiche sin pensarlo', 'El formato se elige según mensaje y destinatario, no al revés.'),
        ('abc', '{F} El mural del caso A debe ser entendido por estudiantes de 1.º medio. ¿Qué decisión ayuda?', 'Usar frases cortas y símbolos claros del liceo', 'Usar términos técnicos de arte que los recién llegados deban buscar', 'Hacerlo solo con colores oscuros', 'El destinatario guía las decisiones de lenguaje: frases cortas y símbolos reconocibles.'),
        ('=', 'Un mural mide 3 metros de ancho y 2 metros de alto. ¿Cuántos metros cuadrados tiene?', '3*2', 'Se multiplica ancho por alto.', ' m²'),
        ('abc', 'Una obra puede responder a', 'una necesidad de expresión, de comunicación o de ambas', 'solo a una necesidad de comunicación', 'solo a una necesidad de venta', 'Muchas obras expresan y comunican a la vez.'),
        ('abc', 'Para un proyecto grupal, ¿qué conviene acordar al comienzo?', 'Quién hace qué y cómo se tomarán las decisiones', 'Que una persona decida todo sin avisar', 'Que cada uno trabaje sin saber lo que hacen los demás', 'Acuerdos claros de roles y decisiones evitan conflictos.'),
        ('abc', '{F} El caso B muestra a personas del barrio en las fotografías. ¿Qué es una buena práctica?', 'Pedir consentimiento a cada persona que aparezca reconocible', 'No pedir nada, porque es un espacio público', 'Mostrar solo a quienes no lo noten', 'Aunque sea espacio público, se pide permiso para mostrar a personas reconocibles.'),
    ],
    ctx=('abc', 'Un grupo quiere un proyecto que exprese su orgullo por su liceo y comunique a las familias una invitación a la muestra de arte. ¿Qué plan es coherente?', 'Escribir un mensaje («Vengan a ver lo que hacemos») y elegir un formato adecuado, como un mural con una invitación', 'Elegir primero el material y después ver qué decir', 'Hacer una obra distinta cada persona sin acuerdo', 'El plan parte del mensaje y del destinatario y luego elige formato.'),
    sc=[
        ("En Artes: ¿qué es un destinatario?", "La persona o grupo a quien va dirigida la obra", "El destinatario guía las decisiones de lenguaje y formato."),
        ("¿Qué se pide antes de fotografiar a una persona reconocible?", "Su consentimiento", "Así se respeta su privacidad y su decisión sobre su imagen."),
        ("¿Qué se define primero: el mensaje o el formato?", "El mensaje", "El formato se elige según el mensaje."),
    ],
    op=("Describe una necesidad (de expresión, de comunicación o ambas) y conviértela en proyecto: escribe el mensaje en una frase, el destinatario y un formato, con una razón de por qué es coherente.",
        "Necesidad: expresar la calma de mi patio favorito. Mensaje: «Este rincón me tranquiliza». Destinatario: mis compañeros. Formato: una serie de tres dibujos con colores suaves, porque los colores suaves se asocian con calma.",
        ["distingue expresión y comunicación", "mensaje en una frase", "formato justificado"],
        ["hoja con necesidad, mensaje, destinatario y formato"],
        ["elegir el formato sin mensaje", "no pedir consentimiento si aparecen personas"],
        "Pregunta: «¿por qué ese formato y no otro?». Si no responde, vuelve al mensaje y al destinatario."),
    reinforce="Escribe en una frase el mensaje de un afiche o de una obra que hayas visto y a quién creas que va dirigida.",
    extend="Explica con un ejemplo inventado cómo una misma necesidad podría resolverse con dos formatos distintos.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 6 (bitácora de investigación de ejemplo, inventada). Proyecto: serie de 3 láminas sobre el cuidado de un humedal ficticio. "
     "Material 1: cartulina blanca, 3 hojas a $400 cada una. Material 2: témpera lavable, un set de 6 colores a $2.500. Material 3: papel kraft, 2 pliegos a $500 cada uno. "
     "Prueba con témpera sobre cartulina: se seca en 15 minutos y no se corre. Prueba con témpera sobre papel kraft: se seca en 15 minutos y el color se ve más apagado. "
     "Presupuesto máximo del grupo: $5.000.")
build(
    O2, 2, F,
    use="Aprenderé a investigar soportes, materiales y procedimientos con una bitácora, a calcular costos y tiempos y a elegir con evidencia para mi proyecto.",
    prior=["Sé explorar con pruebas.", "Sé registrar resultados.", "Sé sumar y multiplicar con dinero chileno."],
    explain=[
        "Investigar con soportes, materiales y procedimientos significa probar y anotar antes de elegir. La bitácora es un cuaderno de registro donde se anota qué se probó, con qué, cuánto demoró, cuánto costó y qué resultó. Con la bitácora se puede decidir por evidencia y no por costumbre, y otra persona puede entender qué se hizo.",
        "Cuando hay un presupuesto, es decir, un máximo de dinero, se calcula el costo de cada material (cantidad por precio) y se suma. El total se compara con el presupuesto. Los materiales también tienen características: opacidad, secado, resistencia, facilidad de uso. Se elige el que mejor cumple el propósito dentro del presupuesto y del tiempo.",
        "Se cuida la seguridad y el ambiente: se usan materiales no tóxicos de uso escolar, se ventila el lugar, se evita desperdiciar y se reutiliza lo que sea posible, como papel usado por un lado. No se mezclan sustancias ni se usa calor o solventes. Si un material desconocido produce picazón, mareo o mal olor, se detiene el trabajo y se avisa a una persona adulta.",
    ],
    vocab=[("bitácora", "cuaderno donde se registran pruebas y decisiones"), ("presupuesto", "máximo de dinero disponible"), ("costo", "dinero que cuesta un material por su cantidad"), ("opacidad", "qué tanto cubre un color lo que hay debajo"), ("secado", "tiempo que tarda un material en quedar seco"), ("reutilizar", "volver a usar un material en lugar de botarlo")],
    worked=[
        ("Calcular el costo", "Con la ficha, ¿cuánto cuestan las 3 hojas de cartulina?", ["Cada hoja cuesta $400.", "3 × 400 = 1.200."], "$1.200"),
        ("Comparar con el presupuesto", "¿El total de los tres materiales cabe en los $5.000?", ["Cartulina $1.200, témpera $2.500 y papel kraft 2 × 500 = $1.000.", "Suma: 1.200 + 2.500 + 1.000 = 4.700, que es menos de 5.000."], "Sí: $4.700 cabe en $5.000"),
    ],
    mistakes=[("Elegir el material más barato sin mirar si cumple el propósito.", "El ahorro no sirve si la obra no se ve o no resiste.", "Compara costo, resultado y propósito antes de elegir."),
              ("No anotar lo que se probó porque «se acuerda».", "Después no se puede comparar ni repetir la prueba.", "Anota soporte, material, tiempo, costo y resultado en la bitácora en el momento.")],
    T=[
        ('abc', '¿Para qué sirve una bitácora de investigación?', 'Para registrar pruebas y decisiones y poder volver a ellas', 'Para entregar una nota al docente sin explicación', 'Para decorar el cuaderno del proyecto', 'La bitácora ordena la evidencia que respalda las decisiones.'),
        ('abc', '{F} ¿Cuál es el presupuesto máximo del grupo?', '$5.000', '$4.700', '$2.500', 'La ficha indica un máximo de $5.000.'),
        ('abc', '{F} ¿Qué resultado tuvo la témpera sobre papel kraft?', 'Se seca en 15 minutos y el color se ve más apagado', 'Se corre y no se seca', 'Se seca en 5 minutos y brilla', 'La ficha dice que en el kraft el color se ve más apagado.'),
        ('=', '{F} ¿Cuánto cuestan los 2 pliegos de papel kraft?', '2*500', 'Se multiplica la cantidad por el precio.', ' pesos'),
        ('=', '{F} ¿Cuánto cuestan juntas la cartulina y la témpera?', '3*400+2500', 'Se suman los $1.200 de la cartulina y los $2.500 de la témpera.', ' pesos'),
        ('=', '{F} ¿Cuánto dinero queda del presupuesto después de comprar los tres materiales?', '5000-(3*400+2500+2*500)', 'Se resta el costo total al presupuesto.', ' pesos'),
        ('abc', '{F} Quieres comprobar en cuál de los dos soportes se ve más vivo el color. ¿Qué haces?', 'Repetir la prueba de témpera en ambos soportes con la misma cantidad de pintura y comparar', 'Elegir al azar', 'Comparar cuál es más barato únicamente', 'Para comparar el color se mantiene igual todo menos el soporte.'),
        ('abc', '{F} El proyecto necesita colores vivos. ¿Qué soporte elige con evidencia de la ficha?', 'La cartulina blanca, porque en el kraft el color se ve más apagado', 'El papel kraft, porque su color de fondo es café', 'Ninguno, porque ambos cuestan igual', 'La ficha muestra que en el kraft el color se ve más apagado; para colores vivos conviene la cartulina blanca.'),
        ('abc', 'Un material desconocido te produce picazón en la piel. ¿Qué haces?', 'Detienes el trabajo, te lavas con agua y avisas a una persona adulta', 'Sigues trabajando con guantes improvisados', 'Lo pruebas en un amigo para ver si le pasa lo mismo', 'La seguridad va primero: se detiene, se limpia y se avisa a un adulto.'),
        ('abc', '¿Qué es reutilizar un material?', 'Volver a usarlo en lugar de botarlo, por ejemplo papel usado por un lado', 'Comprarlo otra vez', 'Guardarlo para nunca usarlo', 'Reutilizar alarga la vida del material y reduce el gasto.'),
        ('=', 'Un grupo tiene $3.600 y quiere comprar 4 pliegos de cartulina a $650 cada uno. ¿Cuánto dinero les sobra?', '3600-4*650', 'Se resta el costo total al dinero disponible.', ' pesos'),
        ('abc', 'Un estudiante prueba tres materiales a la vez y anota «el segundo salió bien». ¿Qué le falta?', 'Anotar qué se probó, cuánto demoró, cuánto costó y por qué «bien» según el propósito', 'Nada más, porque lo importante es que salió bien', 'Probar más materiales sin anotar', 'Una bitácora completa permite decidir y repetir; «bien» sin criterio no informa.'),
        ('abc', '{F} El grupo agrega un cuarto material que cuesta $800 y el presupuesto sigue siendo $5.000. ¿Qué ocurre?', 'El total pasa del presupuesto y deben ajustar o renunciar a algo', 'No pasa nada, porque 4.700 y 800 caben en 5.000', 'El presupuesto aumenta solo', 'Con los $4.700 anteriores más $800 se llega a $5.500, que excede los $5.000.'),
    ],
    ctx=('abc', 'Un grupo debe elegir entre papel kraft y cartulina para una serie de láminas de colores vivos con un presupuesto ajustado. ¿Qué evidencia debe incluir en la bitácora para decidir bien?', 'Costo de cada opción, resultado del color en cada soporte y tiempo de secado', 'Solo el precio, porque el dinero es lo que manda', 'Solo el gusto personal de quien dibuja', 'La decisión combina costo, resultado visual y tiempo, no una sola variable.'),
    sc=[
        ("En Artes: ¿qué es un presupuesto?", "El máximo de dinero disponible", "El presupuesto limita cuánto se puede comprar para el proyecto."),
        ("¿Qué se anota en una bitácora?", "Qué se probó, con qué, cuánto demoró, cuánto costó y qué resultó", "Es la evidencia que respalda las decisiones del proyecto."),
        ("¿Qué haces si un material te produce picazón?", "Detenerte y avisar a una persona adulta", "La seguridad va antes que el trabajo."),
    ],
    op=("Elige un proyecto pequeño y define dos soportes o procedimientos posibles. Haz una bitácora con soporte, material, tiempo, costo estimado y resultado esperado de cada uno, calcula los totales y elige uno con una razón.",
        "Proyecto: 2 láminas de acuarela escolar. Opción A: cartulina, 2 hojas a $400 = $800, 30 minutos, resultado esperado: colores suaves. Opción B: papel kraft, 2 pliegos a $500 = $1.000, 30 minutos, colores apagados. Elijo la A porque cuesta menos y cumple colores suaves.",
        ["registra los datos en la bitácora", "calcula bien los costos", "elige con una razón"],
        ["hoja con dos registros y la decisión"],
        ["elegir solo por precio", "no registrar tiempos ni resultados"],
        "Pregunta: «¿qué evidencia de la bitácora usaste?». Si no la nombra, pídele que señale una."),
    reinforce="Haz una lista de tres materiales que tengas en casa para un trabajo artístico y anota para qué sirve cada uno.",
    extend="Explica cómo cambiaría tu elección de material si el presupuesto se redujera a la mitad.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 7 (referentes ficticios, inventados). Referente nacional ficticio: la muralista Marta Elgueta, que pinta murales de colores planos con figuras simples para plazas de barrio; su idea central es que el arte pertenece a la comunidad. "
     "Referente internacional ficticio: el fotógrafo Jun Okada, que fotografía calles vacías al amanecer en blanco y negro; su idea central es que el silencio también cuenta una historia. "
     "Proyecto del grupo: una serie de dibujos sobre el patio del liceo cuando está vacío. "
     "Cita permitida: «el arte pertenece a la comunidad» (idea de Marta Elgueta, ficticia), 6 palabras.")
build(
    O2, 3, F,
    use="Aprenderé a usar referentes artísticos nacionales e internacionales sin copiarlos: identificar su idea, tomar una decisión, citar y atribuir bien.",
    prior=["Sé observar un referente.", "Sé que copiar no es innovar.", "Sé escribir un mensaje en una frase."],
    explain=[
        "Los referentes artísticos pueden ser nacionales (de Chile) o internacionales (de otros países). Sirven para conocer cómo otras personas resolvieron problemas parecidos y para ampliar las ideas propias. Para usar un referente se identifica su idea central (lo que quiere decir), sus decisiones visuales (cómo lo dice) y su contexto (dónde y para quién se hizo).",
        "Usar un referente no es copiarlo. Se puede inspirar en una idea (por ejemplo, que el silencio cuenta una historia) y cambiarla para el propio tema. Si se usa una frase, una imagen o una obra de otra persona, se atribuye: se escribe quién la hizo, y si es una cita se pone entre comillas. Una obra protegida por derecho de autor no se copia ni se reproduce entera sin permiso; se puede describir, comentar y citar un fragmento breve con atribución.",
        "Cuando se mira un referente de otro país o de otro tiempo se evita juzgarlo con el gusto propio: se pregunta por su contexto y por su función. La ficha de esta clase usa personas ficticias para practicar; en un proyecto real el docente orientará sobre fuentes confiables y permisos.",
    ],
    vocab=[("referente nacional", "obra o artista de Chile que sirve de modelo"), ("referente internacional", "obra o artista de otros países que sirve de modelo"), ("idea central", "lo que la obra quiere decir"), ("atribuir", "indicar quién hizo una obra o una idea"), ("cita", "fragmento breve de otra persona, entre comillas y con su autor"), ("derecho de autor", "protección que tiene quien creó una obra")],
    worked=[
        ("Extraer la idea central", "Con la ficha, ¿cuál es la idea central de Jun Okada?", ["Se busca lo que quiere decir su obra, no cómo se ve.", "La ficha dice que el silencio también cuenta una historia."], "El silencio también cuenta una historia"),
        ("Atribuir bien", "El grupo quiere usar la frase de Marta Elgueta en su cartel. ¿Cómo la escribe?", ["Es una cita, así que va entre comillas.", "Además, se escribe quién la dijo: «el arte pertenece a la comunidad» (idea de Marta Elgueta)."], "Entre comillas y con atribución a Marta Elgueta"),
    ],
    mistakes=[("Hacer un dibujo calcado de un mural famoso y llamarlo «propio».", "Es copia y puede infringir derechos de autor.", "Toma una idea o decisión del referente, cámbiala para tu tema y atribuye."),
              ("Usar una frase de otra persona sin comillas ni autor.", "Parece de quien la usa y no reconoce a la autora.", "Pon la frase entre comillas y escribe a quién pertenece.")],
    T=[
        ('abc', '{F} ¿Qué referente es nacional en la ficha?', 'Marta Elgueta', 'Jun Okada', 'Ninguno', 'Marta Elgueta es presentada como muralista chilena ficticia.'),
        ('abc', '{F} ¿Cuál es la idea central de Marta Elgueta?', 'Que el arte pertenece a la comunidad', 'Que el color es más importante que la forma', 'Que solo se puede pintar en museos', 'La ficha lo indica de forma explícita.'),
        ('abc', '{F} ¿Qué decisión visual toma Jun Okada?', 'Fotografías de calles vacías en blanco y negro', 'Murales de colores planos', 'Dibujos con muchas figuras', 'Esa es la decisión visual de Okada; los colores planos son de Elgueta.'),
        ('=', '{F} La cita permitida tiene 6 palabras. Si el cartel tiene máximo 20 palabras y ya usa 9 sin la cita, ¿cuántas palabras quedan libres con la cita incluida?', '20-9-6', 'Se restan las palabras usadas y las de la cita al máximo.', ' palabras'),
        ('abc', '¿Qué significa atribuir?', 'Indicar quién hizo una obra o una idea', 'Cambiar el nombre de la obra', 'Esconder la fuente para que parezca propia', 'Atribuir es reconocer públicamente quién es la autora o el autor.'),
        ('abc', '{F} El proyecto del grupo es una serie de dibujos del patio vacío. ¿Qué toma bien de Okada?', 'La idea de que el vacío y el silencio cuentan una historia, aplicada a su tema', 'Sus fotografías exactas', 'Su nombre como autor', 'El grupo toma la idea y la aplica a su propio tema; no copia las fotografías.'),
        ('abc', '{F} Un integrante propone dibujar el mismo mural de Marta Elgueta con otro título. ¿Qué corresponde?', 'Tomar su idea de comunidad y crear un mural propio, atribuyendo la inspiración', 'Hacerlo igual, porque cambiar el título basta', 'Firmarlo como obra totalmente nueva', 'Cambiar el título no hace propia una obra copiada; se toma la idea y se crea.'),
        ('abc', 'Una obra con derechos de autor puede', 'describirse, comentarse y citarse con un fragmento breve y atribución', 'reproducirse completa y entregarse como propia', 'copiarse siempre que se cambie el color', 'Se puede comentar y citar brevemente; copiarla o presentarla como propia no.'),
        ('abc', '{F} Para atribuir la idea de Jun Okada en el cartel del grupo, ¿qué escribe?', '«Inspirado en la idea de Jun Okada (referente ficticio)»', 'Nada, porque la idea no se atribuye', '«Obra totalmente original del grupo, sin influencias»', 'Se reconoce la fuente de la inspiración.'),
        ('=', 'Un grupo registra 3 referentes nacionales y 4 internacionales. ¿Cuántos referentes registró?', '3+4', 'Se suman ambos tipos.', ' referentes'),
        ('abc', 'Un estudiante dice que una obra extranjera «no vale» porque no entiende su contexto. ¿Qué corresponde?', 'Preguntar por su contexto y su función antes de juzgarla', 'Descartarla si no le gusta', 'Compararla solo con obras chilenas', 'El contexto ayuda a comprender decisiones; juzgar sin él deja fuera información.'),
        ('abc', '{F} El grupo usa la cita de Marta Elgueta (6 palabras) entre comillas, con su nombre, y escribe 5 palabras más de explicación. ¿Qué puede decirse?', 'Que usó una cita breve y atribuida, con comentario propio', 'Que copió una obra completa', 'Que no hay cita', 'La cita es breve, está entre comillas con autora y se acompaña de comentario propio.'),
        ('abc', 'Antes de usar la fotografía de una persona desconocida en un proyecto, ¿qué corresponde?', 'Pedir permiso, o usar una imagen cuyo autor permita su uso, y atribuir', 'Usarla porque está en internet', 'Cambiarle el color para que parezca propia', 'Estar en internet no equivale a tener permiso; se usa con autorización de su autor.'),
    ],
    ctx=('abc', 'Un grupo quiere dibujar escenas de una plaza como lo hace Marta Elgueta, con colores planos y figuras simples, pero sobre su propio barrio. ¿Qué plan es coherente?', 'Usar la decisión de colores planos, cambiar el tema y las figuras por las de su barrio, y anotar la inspiración', 'Copiar sus figuras exactas', 'Evitar todo parecido y no mencionar al referente', 'Tomar una decisión visual del referente aplicada a un tema propio y atribuir es una inspiración legítima.'),
    sc=[
        ("En Artes: ¿qué es atribuir?", "Indicar quién hizo una obra o una idea", "Reconoce la autoría de quien creó la obra o la idea."),
        ("¿Cómo se escribe una cita?", "Entre comillas y con su autor", "Así se distingue de lo propio."),
        ("¿Puedes copiar una obra con derechos de autor?", "No; puedes comentarla o citar un fragmento breve con atribución", "El derecho de autor protege a quien la creó."),
    ],
    op=("Elige un referente ficticio (inventa su nombre, su país y una idea central) y escribe cómo tomarías una decisión suya para un tema propio sin copiarlo. Incluye una atribución escrita.",
        "Referente: Lía Montero, ilustradora ficticia de Chile, cuya idea central es que las cosas pequeñas importan. Decisión que tomo: dibujos en gran tamaño de objetos pequeños. Mi tema: objetos de mi mochila. Atribución: «inspirado en la idea de Lía Montero (referente ficticio)».",
        ["identifica la idea central", "toma una decisión sin copiar", "atribuye"],
        ["hoja con referente, decisión y atribución"],
        ["copiar la obra", "no atribuir"],
        "Pregunta: «¿qué tomaste y qué cambiaste?». Si no distingue, pídele que lo separe."),
    reinforce="Escribe una cita breve de una persona que admires (sin copiar textos largos), con su autor entre paréntesis.",
    extend="Explica por qué atribuir fortalece a quien hace una obra y no solo a quien la inspiró.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 8 (proceso de ejemplo, inventado). Proyecto: afiche para una muestra de arte del curso. "
     "Versión 1 (boceto en lápiz): figura central pequeña, texto largo; retroalimentación: «no se ve de lejos». "
     "Versión 2 (boceto corregido): figura central grande, texto de 8 palabras; retroalimentación: «se ve, pero el color de fondo cansa». "
     "Versión 3 (prueba de color): fondo claro y figura de dos colores; retroalimentación: «se ve y se lee bien». "
     "Obra final: versión 3 en cartulina de 50 por 70 centímetros. Registro de decisiones: un cambio anotado entre cada versión.")
build(
    O2, 4, F,
    use="Aprenderé a llevar un proyecto desde el boceto hasta la obra terminada, registrando versiones, decisiones y retroalimentación.",
    prior=["Sé investigar materiales.", "Sé usar referentes sin copiarlos.", "Sé registrar decisiones."],
    explain=[
        "Un proyecto artístico avanza por versiones: un boceto, una versión corregida, una prueba de color y la obra final. Cada versión se guarda y se anota qué cambió y por qué. El proceso es parte de la obra y se puede mostrar. Llevar el registro de versiones ayuda a ver cómo se tomaron las decisiones y a repetir lo que funcionó.",
        "La retroalimentación de otras personas orienta cada versión. Si el comentario indica un problema («no se ve de lejos»), se busca una decisión visual que lo resuelva (aumentar el tamaño de la figura o reducir el texto). Si hay dos comentarios que se contradicen, se vuelve al propósito para decidir. Cada cambio se comprueba en la versión siguiente.",
        "La obra final debe cumplir el propósito, respetar las restricciones y estar firmada con el nombre de quien la hizo o del grupo. Si hubo referentes, se atribuyen. Se guardan las versiones previas porque son evidencia del proceso. Todo se hace en sala con materiales escolares seguros y sin materiales que dañen la salud.",
    ],
    vocab=[("versión", "etapa de la obra que se guarda: boceto, corrección, prueba, final"), ("boceto", "dibujo rápido para probar una idea"), ("prueba de color", "ensayo de la combinación de colores antes de la obra final"), ("registro de decisiones", "lista de cambios y razones"), ("obra final", "versión terminada que se presenta")],
    worked=[
        ("Relacionar problema y decisión", "En la versión 1 «no se ve de lejos». ¿Qué decisión de la ficha lo resuelve?", ["El problema es el tamaño de la figura y el texto largo.", "En la versión 2 se agranda la figura y se reduce el texto a 8 palabras."], "Agrandar la figura y reducir el texto"),
        ("Calcular el área", "La obra final mide 50 por 70 centímetros. ¿Cuántos centímetros cuadrados tiene?", ["Se multiplica ancho por alto.", "50 × 70 = 3.500."], "3.500 cm²"),
    ],
    mistakes=[("Borrar los bocetos anteriores cuando se hace una versión nueva.", "Se pierde la evidencia del proceso y no se puede volver atrás.", "Guarda cada versión con su fecha y una nota de lo que cambió."),
              ("Cambiar muchas cosas entre versiones sin anotarlas.", "No se sabe qué cambio mejoró o empeoró la obra.", "Cambia pocas cosas por versión y anótalas en el registro.")],
    T=[
        ('abc', '¿Qué es un boceto?', 'Un dibujo rápido para probar una idea', 'La obra final enmarcada', 'Un informe de notas', 'El boceto sirve para probar ideas antes de la obra final.'),
        ('abc', '{F} ¿Qué problema señaló la retroalimentación de la versión 1?', 'Que no se ve de lejos', 'Que el color cansa', 'Que el texto es muy corto', 'La ficha dice que la versión 1 no se ve de lejos.'),
        ('abc', '{F} ¿Qué problema señaló la retroalimentación de la versión 2?', 'Que el color de fondo cansa', 'Que la figura es pequeña', 'Que el texto no se lee', 'La versión 2 se ve, pero el fondo cansa.'),
        ('=', '{F} ¿Cuántas palabras redujo el afiche si el texto de la versión 1 tenía 20 palabras y el de la versión 2 tiene 8?', '20-8', 'Se resta el texto nuevo al texto antiguo.', ' palabras'),
        ('=', '{F} La prueba de color se hizo en un papel de 25 por 35 centímetros. ¿Cuántos centímetros cuadrados tiene?', '25*35', 'Se multiplica ancho por alto.', ' cm²'),
        ('abc', '{F} ¿Qué cambió entre la versión 2 y la 3?', 'El fondo pasó a un color claro y la figura a dos colores', 'La figura se redujo de tamaño', 'El texto aumentó a 20 palabras', 'La ficha dice que la versión 3 usó fondo claro y figura de dos colores.'),
        ('abc', '{F} ¿Por qué la versión 3 es la obra final?', 'Porque su retroalimentación indica que se ve y se lee bien, cumpliendo el propósito', 'Porque es la última que se hizo', 'Porque es la más cara', 'Se elige por cumplir el propósito según la evidencia, no solo por el orden.'),
        ('abc', 'Un estudiante borra el boceto 1 al hacer el 2. ¿Qué consecuencia tiene?', 'Pierde evidencia de su proceso y no puede volver a una versión anterior', 'Ninguna, porque el boceto no importa', 'Gana tiempo y la obra mejora sola', 'Las versiones son evidencia y permiten volver atrás.'),
        ('abc', 'Dos compañeros dan comentarios opuestos: uno pide más color y otro menos. ¿Qué hace quien creó la obra?', 'Vuelve al propósito y decide, anotando la razón', 'Hace lo que diga la persona que habló más fuerte', 'Ignora a ambos', 'El propósito ayuda a decidir cuando los comentarios se contradicen.'),
        ('=', 'Un grupo hace 3 versiones y cada una toma 25 minutos de trabajo y 10 de revisión. ¿Cuántos minutos suman?', '3*(25+10)', 'Se suma el trabajo y la revisión de una versión y se multiplica por 3.', ' minutos'),
        ('abc', 'Para que el registro de decisiones sea útil, cada línea debe tener', 'qué cambió, por qué y qué efecto produjo', 'solo la fecha', 'solo el nombre de quien cambió algo', 'El registro vale por la razón y el efecto, no solo por la fecha.'),
        ('abc', 'La obra final debe', 'cumplir el propósito, respetar restricciones y estar firmada', 'ser idéntica al primer boceto', 'ser la más grande posible', 'El propósito y las restricciones definen si la obra final sirve.'),
        ('abc', '{F} El grupo agrega una fotografía de una compañera sin pedirle permiso. ¿Qué corresponde?', 'Quitarla hasta tener su consentimiento', 'Dejarla, porque es solo una foto', 'Cambiarle el color para que no se reconozca', 'Se necesita consentimiento para mostrar a una persona reconocible.'),
    ],
    ctx=('abc', 'En un afiche de ejemplo, la retroalimentación dice «el título se pierde entre las figuras». ¿Qué decisión es coherente para la siguiente versión?', 'Aumentar el tamaño del título y dejar espacio vacío a su alrededor, y comprobarlo en la versión siguiente', 'Agregar más figuras cerca del título', 'Borrar el título para que se vea mejor', 'Agrandar y dar espacio resuelve el problema y puede comprobarse en la nueva versión.'),
    sc=[
        ("En Artes: ¿qué es una versión?", "Una etapa guardada del proyecto, como un boceto o una prueba", "Las versiones guardadas muestran cómo avanzó el proceso del proyecto."),
        ("¿Qué se hace con los comentarios que se contradicen?", "Se vuelve al propósito para decidir", "El propósito ordena la elección cuando hay opiniones distintas."),
        ("¿Se pide permiso para mostrar a una persona en la obra?", "Sí", "Se necesita consentimiento para mostrar a una persona reconocible."),
    ],
    op=("Elige un proyecto pequeño y escribe tres versiones (boceto, corrección, versión final) con una línea cada una: qué cambió y por qué. Agrega una retroalimentación imaginaria por versión.",
        "Proyecto: invitación. V1 boceto: texto largo; comentario: no se lee. V2: texto de 6 palabras; comentario: falta contraste. V3: letras oscuras sobre fondo claro; comentario: se lee bien. Cambios: reducir texto, subir contraste.",
        ["tres versiones con cambios", "comentarios que orientan", "decisiones justificadas"],
        ["hoja con tres versiones y el registro"],
        ["cambiar demasiado sin anotar", "no incluir comentario"],
        "Pregunta: «¿qué cambio resolvió el problema de la versión anterior?». Si no lo identifica, pídele que lo busque."),
    reinforce="Haz un boceto rápido de una idea y otro con un cambio. Anota qué cambiaste y qué efecto tiene.",
    extend="Explica por qué guardar los bocetos puede ser útil aunque la obra final sea muy distinta.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 9 (rúbrica de ejemplo, inventada). Proyecto: serie de 3 láminas sobre el cuidado de un humedal ficticio. "
     "Criterios de la rúbrica (cada uno vale hasta 4 puntos): 1) El mensaje se entiende. 2) La composición guía la mirada. 3) Los materiales se usaron con cuidado. 4) El proceso está registrado. 5) Las fuentes y referentes están atribuidos. "
     "Autoevaluación de ejemplo: criterio 1: 4; criterio 2: 3; criterio 3: 2; criterio 4: 4; criterio 5: 1. "
     "Evaluación de un compañero: criterio 1: 3; criterio 2: 3; criterio 3: 3; criterio 4: 3; criterio 5: 2.")
build(
    O2, 5, F,
    use="Aprenderé a revisar un proyecto con una rúbrica, comparar la autoevaluación con la mirada de otras personas y decidir qué mejorar primero.",
    prior=["Sé evaluar con criterios.", "Sé dar y recibir retroalimentación.", "Sé sumar y comparar puntajes."],
    explain=[
        "Una rúbrica es una tabla de criterios con niveles de logro. Cada criterio dice qué se espera de la obra o del proceso y cuántos puntos vale. Se usa para revisar con claridad y para que quien evalúa y quien es evaluado entiendan lo mismo. Los criterios se redactan según el propósito: mensaje, composición, uso de materiales, registro y atribución.",
        "La autoevaluación (la mirada propia) y la evaluación de un par (la mirada de otra persona) se comparan. Si coinciden, se confirma un logro o un problema; si difieren, se busca evidencia en la obra y en la bitácora. Una diferencia de un punto es normal; una diferencia grande indica que hay que mirar mejor. Se priorizan los criterios con menor puntaje y mayor importancia para el propósito.",
        "La mejora se planifica con una acción concreta y un plazo: «agregar las fuentes en la lámina 3 en la próxima clase». Se vuelve a revisar con la misma rúbrica. La revisión es respetuosa: se habla de la obra y no de la persona.",
    ],
    vocab=[("rúbrica", "tabla de criterios con puntajes para evaluar"), ("autoevaluación", "evaluación del propio trabajo"), ("evaluación de pares", "evaluación hecha por un compañero"), ("prioridad", "lo que se mejora primero"), ("acción de mejora", "cambio concreto con plazo")],
    worked=[
        ("Sumar puntajes", "¿Cuántos puntos suma la autoevaluación de la ficha?", ["4 + 3 + 2 + 4 + 1.", "El total es 14."], "14 puntos"),
        ("Priorizar", "¿Qué criterio de la autoevaluación tiene menor puntaje y qué acción propones?", ["El criterio 5 tiene 1 punto: fuentes y referentes atribuidos.", "Acción: agregar la atribución de cada referente antes de la próxima clase."], "Criterio 5; agregar las atribuciones"),
    ],
    mistakes=[("Ponerse el puntaje máximo en todo sin evidencia.", "No sirve para mejorar y no coincide con lo que se ve.", "Para cada puntaje escribe la evidencia que lo respalda."),
              ("Mejorar primero lo que más gusta y no lo que más importa.", "Se pierde el propósito de la rúbrica.", "Prioriza los criterios con menor puntaje e importantes para el propósito.")],
    T=[
        ('abc', '¿Qué es una rúbrica?', 'Una tabla de criterios con puntajes para evaluar', 'Una lista de materiales', 'Un boceto final', 'La rúbrica define criterios y niveles de logro.'),
        ('abc', '{F} ¿Cuáles criterios obtuvieron 4 puntos en la autoevaluación?', 'Los criterios 1 y 4', 'Los criterios 1 y 2', 'Los criterios 3 y 5', 'En la autoevaluación, el mensaje (criterio 1) y el proceso (criterio 4) tienen 4 puntos.'),
        ('abc', '{F} ¿Cuál criterio obtuvo el mismo puntaje en la autoevaluación y en la evaluación del compañero?', 'El criterio 2', 'El criterio 1', 'El criterio 4', 'En el criterio 2 ambos puntajes son 3.'),
        ('=', '{F} ¿Cuántos puntos suma la evaluación del compañero?', '3+3+3+3+2', 'Se suman los cinco puntajes.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos más tiene la autoevaluación que la del compañero?', '(4+3+2+4+1)-(3+3+3+3+2)', 'Se restan los totales: 14 y 14 dan diferencia 0.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos más dio el compañero que la autoevaluación en el criterio 3?', '3-2', 'La autoevaluación puso 2 y el compañero 3; se restan.', ' punto'),
        ('abc', 'Una diferencia grande entre autoevaluación y evaluación del par significa que', 'hay que buscar evidencia en la obra y la bitácora', 'una de las dos personas se equivocó y debe cambiar el puntaje', 'se promedian los puntajes sin mirar la obra', 'Una diferencia grande indica que hay que mirar mejor con evidencia.'),
        ('abc', '{F} ¿Qué acción de mejora es concreta?', 'Agregar la atribución de cada referente en las láminas antes de la próxima clase', 'Esforzarse más', 'Mejorar todo', 'Una acción concreta dice qué, dónde y cuándo.'),
        ('abc', '{F} Con 14 puntos en la autoevaluación, ¿qué porcentaje del puntaje máximo de la rúbrica alcanza?', '70 %', '14 %', '40 %', 'El máximo es 5 × 4 = 20 y 14 de 20 es 70 de cada 100.'),
        ('=', 'Una rúbrica tiene 5 criterios de hasta 4 puntos. ¿Cuál es el puntaje máximo?', '5*4', 'Se multiplica la cantidad de criterios por el puntaje máximo de cada uno.', ' puntos'),
        ('abc', 'Un estudiante escribe «4 en todo» sin explicar. ¿Qué falta?', 'Evidencia en la obra o en la bitácora para cada puntaje', 'Nada, porque el puntaje es personal', 'Un puntaje más alto', 'Cada puntaje se respalda con evidencia.'),
        ('abc', 'Para priorizar la mejora, ¿qué criterios conviene mirar primero?', 'Los de menor puntaje e importantes para el propósito', 'Los que más le gustan a quien evalúa', 'Los de mayor puntaje', 'Se mejora lo que más falla y más importa.'),
        ('abc', 'Al revisar la obra de un compañero, ¿qué es adecuado?', 'Hablar de la obra con evidencia y sugerir un cambio, sin referirse a la persona', 'Compararlo con otros del curso', 'Evitar decir lo que no funciona', 'La revisión respetuosa se centra en la obra.'),
    ],
    ctx=('abc', 'En la ficha, el criterio «Las fuentes y referentes están atribuidos» tiene 1 punto en la autoevaluación y 2 en la del compañero. ¿Qué plan de mejora es coherente?', 'Listar los referentes usados, escribir la atribución de cada uno y pedir una nueva revisión', 'Bajar el puntaje de los demás criterios', 'Quitar el criterio de la rúbrica', 'La mejora apunta al criterio más débil con una acción concreta.'),
    sc=[
        ("En Artes: ¿qué es una rúbrica?", "Una tabla de criterios con puntajes para evaluar", "Permite revisar con claridad y con los mismos criterios para todos."),
        ("¿Qué se hace si la autoevaluación y la del compañero difieren mucho?", "Buscar evidencia en la obra y en la bitácora", "La evidencia ayuda a resolver la diferencia."),
        ("¿Qué criterios se mejoran primero?", "Los de menor puntaje e importantes para el propósito", "Se prioriza lo que más importa."),
    ],
    op=("Crea una rúbrica de 3 criterios (hasta 4 puntos cada uno) para un proyecto que elijas, aplícala a un trabajo imaginario con evidencia breve y escribe una acción de mejora con plazo.",
        "Criterios: mensaje (4), composición (4), registro (4). Autoevaluación: mensaje 3 porque se entiende pero falta una palabra; composición 2 porque la mirada se pierde; registro 4 porque anoté todas las versiones. Total: 9 de 12. Mejora: reubicar la figura principal en la próxima clase.",
        ["criterios claros", "puntajes con evidencia", "acción de mejora con plazo"],
        ["hoja con la rúbrica y la autoevaluación"],
        ["puntajes sin evidencia", "acción sin plazo"],
        "Pregunta: «¿qué evidencia respalda este puntaje?». Si no la hay, pídele que la busque."),
    reinforce="Escribe tres criterios para evaluar un cartel y aplícalos a uno que veas en tu entorno.",
    extend="Explica por qué una rúbrica compartida antes de empezar puede mejorar un proyecto.",
)
