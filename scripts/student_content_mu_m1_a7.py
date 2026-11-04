"""Student material for 1.º medio Música, OA 07 (evaluar la relevancia de la música, destacando el singular sentido que cumple en la construcción y preservación de identidades y culturas).

Todas las comunidades, músicas, fichas y datos de los ejercicios son inventados («de ejemplo»). No se usan ritos, lenguas ni piezas reales de pueblos originarios: esa música y su forma tradicional las enseñan las personas portadoras de la tradición y la comunidad.
"""
from __future__ import annotations

from student_content_mu_m1_a import L
from student_lessons import arith, ex

OA7 = "MU1M OA 07"

FI = ("Música 1 (de ejemplo): canto de trabajo de una caleta; lo cantan quienes arrastran las redes para coordinar el esfuerzo; ritmo regular a 72 pulsos por minuto; sus palabras hablan del mar. "
      "Música 2: himno de un club deportivo de barrio; lo cantan los hinchas de pie, todos juntos; melodía sencilla y fuerte. "
      "Música 3: arrullo familiar; una abuela lo canta a quien duerme; voz suave y sola")

# ---------------------------------------------------------------- OA 07 · clase 1 (funciones de la música en la identidad)
L(
    OA7, 1,
    f"Lápiz y papel. Fichas de ejemplo, que se repiten en los ejercicios: {FI}. Si una persona de tu casa te cuenta una canción que le importa, puedes usarla, con su permiso.",
    "Aprenderé qué es la identidad y la cultura y cómo la música ayuda a construirlas y a conservarlas: da sentido de pertenencia, guarda la memoria y cumple funciones en la vida de una comunidad. Sirve para evaluar por qué una música importa a un grupo, más allá de si me gusta.",
    ["Sé relacionar una música con su contexto y su propósito.", "Sé distinguir tradición oral, escrita y popular.", "Sé que las personas pertenecen a distintos grupos."],
    [
        "La identidad es aquello que hace que una persona o un grupo se reconozca como parte de algo: una familia, un barrio, un oficio, un pueblo. La cultura es el conjunto de costumbres, saberes, creencias y expresiones, como el idioma, las comidas, las fiestas y la música, que comparte un grupo. La música ayuda a construir la identidad porque reúne a las personas en torno a sonidos que sienten propios, de modo que cantar o tocar juntas refuerza el sentido de pertenencia.",
        "La música cumple varias funciones dentro de una comunidad. Coordina el trabajo, como un canto que marca el ritmo para arrastrar redes. Une a un grupo grande, como un himno de barrio. Cuida a las personas, como un arrullo. También guarda la memoria: recuerda hechos, personas y lugares que una comunidad no quiere olvidar. Y se transmite de una generación a otra, así que ayuda a preservar la cultura, es decir, a mantenerla viva.",
        "Para evaluar la relevancia de una música no basta con decir si gusta. Se pregunta quién la practica, para qué, qué significa para esa comunidad y qué pasaría si dejara de transmitirse. También se respeta: algunas músicas pertenecen a comunidades que tienen sus propias normas sobre cuándo y cómo se usan. En esos casos, quien enseña la forma tradicional es la propia comunidad o las personas portadoras de la tradición, y lo que se hace en la sala de clases solo es una aproximación respetuosa.",
    ],
    [("identidad", "lo que hace que una persona o un grupo se reconozca como parte de algo"), ("cultura", "conjunto de costumbres, saberes y expresiones que comparte un grupo"), ("pertenencia", "sentirse parte de un grupo"), ("memoria", "recuerdo compartido de hechos, personas y lugares"), ("preservar", "mantener viva una expresión cultural al transmitirla")],
    [
        ("Identificar una función", f"{FI}. ¿Qué función cumple la música 1 en el trabajo de la caleta?", ["Se canta al arrastrar las redes.", "El ritmo regular coordina el esfuerzo."], "Coordina el esfuerzo de quienes trabajan"),
        ("Pertenencia", f"{FI}. ¿Qué sentimiento refuerza el himno de la música 2 entre los hinchas?", ["Todos cantan juntos y de pie.", "Se sienten parte del mismo grupo."], "El sentido de pertenencia"),
    ],
    [
        ("Evaluar una música solo por si gusta.", "La relevancia se evalúa por lo que significa y hace para una comunidad.", "Pregunta quién la practica, para qué y qué sentido tiene."),
        ("Pensar que cualquier persona puede usar toda la música de una comunidad sin pedir permiso.", "Algunas músicas tienen normas propias de la comunidad.", "Pregunta a las personas portadoras y respeta sus indicaciones."),
    ],
    [
        ex(f"{FI}. ¿A cuántos pulsos por minuto se canta la música 1?", "72", "Así lo indica la ficha."),
        ex(f"{FI}. ¿Qué música se canta con una voz suave y sola?", "La música 3", "Esa es la descripción del arrullo."),
        ex("La cultura ¿es el conjunto de costumbres, saberes y expresiones de un grupo o solo las obras de arte que se exhiben en un museo?", "El conjunto de costumbres, saberes y expresiones de un grupo", "Incluye idioma, fiestas, comidas y música."),
    ],
    [
        ex(f"{FI}. ¿Qué música une a un grupo grande en un mismo canto? A) El himno del club. B) El arrullo familiar.", "A", "El himno lo cantan todos los hinchas juntos."),
        ex("¿Qué es la memoria colectiva? A) El recuerdo compartido de hechos, personas y lugares. B) La capacidad de recordar una melodía.", "A", "Es el recuerdo que comparte un grupo."),
        ex("¿Qué ayuda a preservar una música de tradición oral? A) Que se transmita de generación en generación. B) Que se guarde en un cajón sin cantarla.", "A", "La transmisión mantiene viva la tradición."),
    ],
    [
        arith(f"{FI}. Durante 5 minutos se canta la música 1 sin parar, con un tirón de red por pulso. ¿Cuántos tirones se dan?", "72*5", "Se multiplican los pulsos por minuto por los minutos.", " tirones"),
        ex(f"{FI}. ¿Qué cambia si la música 3 se canta a gritos en un estadio? A) Pierde el sentido de cuidado que tiene como arrullo. B) Gana más sentido de memoria.", "A", "Su función de cuidado depende de una voz suave y cercana."),
        ex("Un grupo de estudiantes quiere usar una canción de una comunidad sin preguntar a esa comunidad, porque «es patrimonio de todos». ¿Qué respuesta es más adecuada? A) Preguntar a las personas portadoras de la tradición y seguir sus indicaciones. B) Usarla igual y no decir nada.", "A", "Respetar a la comunidad es parte de valorar su cultura."),
    ],
    [
        ex(f"{FI}. Una profesora dice: «La música 2 tiene una melodía sencilla y fuerte, y por eso sirve como símbolo del club». ¿Qué rasgo audible sostiene su afirmación? A) La melodía sencilla y fuerte, que todos pueden cantar. B) El nombre del club.", "A", "Una melodía sencilla permite que muchas personas la canten juntas."),
        arith(f"{FI}. En un partido, 40 hinchas cantan el himno 3 veces cada uno. ¿Cuántas veces se canta en total, sumando las voces?", "40*3", "Se multiplican los hinchas por las veces que canta cada uno.", " cantos"),
    ],
    [
        arith("Una caleta tiene 24 pescadores. Si todos cantan el canto de trabajo y 8 se cambian a otro oficio y dejan de cantarlo, ¿cuántos siguen cantándolo?", "24-8", "Se restan quienes dejaron de cantarlo.", " pescadores"),
        ex(f"{FI}. Si los pescadores jóvenes ya no aprenden el canto de trabajo, ¿qué riesgo corre la música 1? A) Que deje de transmitirse y se pierda. B) Que se vuelva más rápida.", "A", "Sin transmisión, una tradición oral puede perderse."),
    ],
    [ex(f"{FI}. Para una feria escolar necesitas una música que haga sentir juntas a muchas personas. ¿Cuál eliges y por qué? A) La música 2, porque su melodía sencilla y fuerte la hace cantable por todos. B) La música 3, porque tiene una sola voz suave.", "A", "Una melodía sencilla y fuerte une a un grupo grande.")],
    [ex("En Música: ¿Qué es la identidad?", "Lo que hace que un grupo o una persona se reconozca como parte de algo", "Es la sensación de pertenencia."), ex("¿Qué función cumple un arrullo?", "Cuidar a quien duerme", "Calma con una voz suave."), ex("¿Quién enseña la forma tradicional de una música de una comunidad?", "La propia comunidad y sus personas portadoras", "Ellas saben cómo y cuándo se usa.")],
    (
        "Elige una de las tres músicas de ejemplo o una canción que te cuente una persona de tu casa (con su permiso; no anotes datos personales). Escribe: a) quiénes la practican, b) para qué se usa, c) dos rasgos audibles, d) qué sentido de pertenencia o memoria produce, e) qué pasaría si dejara de transmitirse.",
        "Música 1. a) Pescadores de una caleta. b) Coordinar el esfuerzo al arrastrar redes. c) Ritmo regular a 72 pulsos por minuto; palabras sobre el mar. d) Da sentido de pertenencia al oficio y guarda la memoria del trabajo. e) Los jóvenes perderían una parte de su historia.",
        ["identifica función y comunidad", "da rasgos audibles de la ficha", "explica pertenencia o memoria y qué pasaría si se perdiera"],
        ["cinco respuestas a) a e)", "rasgos audibles de la ficha"],
        ["evaluar solo por gusto", "incluir datos personales"],
        "Reconoce la ficha y pide indicar qué parte de la música es más importante conservar para la comunidad y por qué.",
    ),
    "Pregunta a una persona de tu casa qué canción le recuerda a su familia y anota qué sentimiento le produce (sin datos personales).",
    "Escribe tres músicas de tu barrio o de tu región y la función que cumple cada una.",
)

# ---------------------------------------------------------------- OA 07 · clase 2 (lenguaje, contexto y significado cultural)
PLAYA = ("Comunidad de ejemplo «Playa Azul» (inventada). Música A: canto de trabajo de la pesca; se canta con palabras del oficio; ritmo regular de remo, 72 pulsos por minuto; solo con voz y palmas. "
         "Música B: baile de fiesta del pueblo; se baila en pareja; ritmo animado, 120 pulsos por minuto; guitarra, tambor y voces. "
         "Música C: canción de despedida a quien se va del pueblo; lenta, 60 pulsos por minuto; una guitarra y voces suaves")
L(
    OA7, 2,
    f"Lápiz y papel. Datos de ejemplo, que se repiten en los ejercicios: {PLAYA}.",
    "Aprenderé a relacionar los rasgos de una música (idioma, instrumentos, ritmo y manera de interpretarla) con la cultura y el contexto de una comunidad, y a explicar qué significa para quienes la practican. Sirve para evaluar por qué una música es relevante para una comunidad concreta.",
    ["Sé qué son identidad y cultura.", "Sé relacionar rasgos con propósito.", "Sé calcular pulsos y compases."],
    [
        "Los rasgos de una música suelen estar ligados a la vida de la comunidad que la practica. El idioma o las palabras de una canción cuentan lo que importa a ese grupo: su oficio, su territorio, sus costumbres. El ritmo se relaciona con la actividad: un ritmo regular acompaña el remo o el trabajo; uno animado acompaña el baile. Los instrumentos suelen ser los que la comunidad tiene a su alcance o ha heredado. Y la manera de interpretar, en grupo o en solitario, dice quién participa.",
        "Por eso una misma melodía puede significar cosas distintas en comunidades diferentes. Para evaluar su relevancia se relacionan tres cosas: el contexto (dónde y cuándo se canta), el propósito (para qué sirve) y los rasgos que se oyen. Por ejemplo, la música C de Playa Azul, lenta y suave, sirve para despedir a quien se va y así cuida los vínculos de la comunidad; la música B, animada, une al pueblo en la fiesta.",
        "Hay que cuidar el modo de hablar de otras culturas. No se dice que una música es «más simple» o «más atrasada» que otra: cada una responde a necesidades distintas. Tampoco se generaliza: «todas las personas de ese pueblo cantan así» es una afirmación que casi nunca es verdadera. Cuando no se conoce una tradición, se pregunta a quienes la portan y se usan fuentes cuidadas. Aprender de otras culturas es una forma de respeto.",
    ],
    [("contexto cultural", "lugar, momento y costumbres donde se practica una música"), ("significado", "lo que una música representa para quienes la practican"), ("vínculo", "relación que une a las personas"), ("generalizar", "afirmar algo de todo un grupo sin pruebas"), ("fuente", "persona o documento de donde se obtiene información")],
    [
        ("Relacionar ritmo y actividad", f"{PLAYA}. ¿Por qué el canto A tiene un ritmo regular de 72 pulsos por minuto?", ["El canto A acompaña el remo.", "El remo exige golpes parejos."], "Porque acompaña el remo, que se hace con golpes parejos"),
        ("Explicar un significado", f"{PLAYA}. ¿Qué significa la música C para la comunidad?", ["Es una despedida lenta y suave.", "Cuida el vínculo con quien se va."], "Cuida el vínculo con quien se va del pueblo"),
    ],
    [
        ("Decir que una música es «más simple» o «más atrasada».", "Cada música responde a necesidades distintas y no hay una superior.", "Describe sus rasgos y su función sin jerarquías."),
        ("Afirmar «todas las personas de ese pueblo cantan así».", "Es una generalización que suele ser falsa.", "Di «en la comunidad de ejemplo se canta así» y busca fuentes."),
    ],
    [
        ex(f"{PLAYA}. ¿Qué instrumentos suenan en la música B?", "Guitarra, tambor y voces", "Así lo indica la ficha."),
        ex(f"{PLAYA}. ¿Cuál de las tres músicas es la más lenta?", "La música C", "Tiene 60 pulsos por minuto, menos que 72 y 120."),
        ex(f"{PLAYA}. ¿En qué actividad se canta la música A?", "En la pesca", "Es un canto de trabajo de la pesca."),
    ],
    [
        ex(f"{PLAYA}. ¿Qué rasgo de la música B sirve para el baile en pareja? A) Su ritmo animado de 120 pulsos por minuto. B) Su voz sola y suave.", "A", "Un ritmo animado da apoyo para bailar."),
        ex("¿Cuál afirmación es una generalización incorrecta? A) «Todas las personas de ese pueblo cantan así.» B) «En la comunidad de ejemplo se canta así en las fiestas.»", "A", "La primera dice algo de todos sin pruebas."),
        ex("Una persona dice que una música de otra cultura es «atrasada». ¿Qué respuesta es adecuada? A) Cada música responde a las necesidades de su comunidad y no se mide con jerarquías. B) Tiene razón, porque suena distinto.", "A", "No hay música superior; cada una cumple su función."),
    ],
    [
        arith(f"{PLAYA}. ¿Cuántos pulsos más por minuto tiene la música B que la música A?", "120-72", "Se restan los pulsos de la música A a los de la B.", " pulsos"),
        arith(f"{PLAYA}. La música B se baila durante 3 minutos. ¿Cuántos pulsos suenan?", "120*3", "Se multiplican los pulsos por minuto por los minutos.", " pulsos"),
        ex(f"{PLAYA}. Si la música C se tocara rápido y fuerte, ¿seguiría sirviendo para despedir con afecto, según lo que cuenta su ficha? Responde sí o no.", "No", "La despedida usa un tempo lento de 60 pulsos por minuto y voces suaves para cuidar el vínculo."),
    ],
    [
        ex(f"{PLAYA}. Un grupo escolar adapta la música A y la toca a 120 pulsos por minuto con guitarra eléctrica. ¿Qué pierde? A) La relación del tempo de 72 pulsos por minuto con el remo y el trabajo. B) Las palabras del oficio.", "A", "El tempo de 72 acompaña el remo; las palabras no se cambiaron."),
        arith(f"{PLAYA}. La jornada de pesca dura 4 horas y en ella hay 1 hora de pausas. Si la música A se canta solo mientras se trabaja, ¿cuántos minutos suena?", "(4-1)*60", "Se restan las horas de pausa y se pasa a minutos.", " minutos"),
    ],
    [
        ex(f"{PLAYA}. Una investigadora quiere escribir sobre la música A. ¿Cuál es una buena fuente? A) Preguntar a quienes la cantan y registrar sus indicaciones. B) Inventar el significado sin consultar.", "A", "Las personas portadoras son la fuente más confiable."),
        arith(f"{PLAYA}. En una celebración se tocan 2 veces la música A (3 minutos cada vez), 3 veces la B (4 minutos cada vez) y 1 vez la C (5 minutos). ¿Cuántos minutos de música hay?", "2*3+3*4+5", "Se suman los minutos de cada música.", " minutos"),
    ],
    [ex(f"{PLAYA}. Una profesora quiere comparar los significados de las músicas A y B en un cuadro. ¿Qué dato incluye en la fila «función»? A) Coordinar el trabajo (A) y reunir al pueblo en la fiesta (B). B) El precio de los instrumentos.", "A", "La función se refiere a lo que cumple cada música en la comunidad.")],
    [ex("En Música y cultura: ¿qué es una generalización?", "Afirmar algo de todo un grupo sin pruebas", "Suele ser falsa."), ex("¿Qué se hace cuando no se conoce una tradición?", "Se pregunta a quienes la portan", "Ellos son la fuente más confiable."), ex(f"{PLAYA}. ¿A cuántos pulsos por minuto va la música C?", "60", "Así lo indica la ficha.")],
    (
        "Usa la comunidad de ejemplo «Playa Azul». Escribe un cuadro con tres filas (A, B y C) y tres columnas: contexto, rasgos audibles y significado. Luego escribe una frase que explique por qué la música C es relevante para la comunidad, con un rasgo audible, y una frase de respeto hacia otra cultura que cumplirías al hablar de ella.",
        "A: pesca; ritmo regular a 72 y solo voces y palmas; coordina y da identidad de oficio. B: fiesta; ritmo animado a 120; reúne al pueblo. C: despedida; lenta a 60 y voces suaves; cuida el vínculo. Frase: «La música C es relevante porque, con su tempo lento de 60 pulsos por minuto, permite despedir con afecto». Respeto: no diré que una música es más atrasada que otra.",
        ["relaciona rasgos con significado en las tres filas", "usa un rasgo audible en la frase", "incluye una frase de respeto"],
        ["cuadro de 3 filas y 3 columnas", "frase de relevancia y frase de respeto"],
        ["afirmar que una música es más atrasada", "generalizar sobre todas las personas"],
        "Reconoce el cuadro y pide explicar qué cambiaría en el significado si una música se tocara en otro contexto.",
    ),
    "Anota dos rasgos de una música de tu familia (palabras, ritmo, instrumentos) y qué significan para ella.",
    "Escribe tres preguntas respetuosas que harías a una persona portadora de una tradición musical.",
)

# ---------------------------------------------------------------- OA 07 · clase 3 (evaluar la relevancia con criterios)
MATRIZ = ("Matriz de ejemplo, con cinco criterios y puntaje de 0 a 2 cada uno: permanencia (¿ha durado en el tiempo?), participación (¿mucha gente la practica?), transmisión (¿se enseña a nuevas generaciones?), "
          "significado (¿representa algo importante para la comunidad?) y respeto (¿se usa con permiso y sin burla?). Puntajes de ejemplo: Canto de trabajo de la caleta: 2, 1, 1, 2, 2. Himno del club: 1, 2, 2, 2, 2. Arrullo familiar: 2, 1, 2, 2, 2")
L(
    OA7, 3,
    f"Lápiz y papel. Matriz de ejemplo, que se repite en los ejercicios: {MATRIZ}.",
    "Aprenderé a evaluar la relevancia cultural de una música con criterios (permanencia, participación, transmisión, significado y respeto) y a justificar mi evaluación con evidencia, sin descalificar ninguna música. Sirve para tomar decisiones sobre qué músicas conviene cuidar y difundir.",
    ["Sé qué es identidad y cultura.", "Sé relacionar rasgos con significado cultural.", "Sé usar «porque» para justificar."],
    [
        "Evaluar la relevancia de una música es decir cuánto importa para una comunidad y por qué. Para hacerlo con orden se usan criterios, que son aspectos observables. La permanencia mira si la música ha durado en el tiempo. La participación, cuánta gente la practica. La transmisión, si se enseña a las nuevas generaciones. El significado, qué representa para la comunidad. Y el respeto, si se usa con permiso y sin burla. Cada criterio se puntúa de 0 a 2 y se suman los puntos.",
        "Un total alto muestra una música muy viva y valorada; un total bajo en un criterio, por ejemplo la transmisión, avisa de un riesgo y señala qué conviene cuidar. La suma no es una nota para premiar o castigar músicas: es una herramienta para comprender. Por eso siempre se acompaña de una justificación escrita con evidencia: «Transmisión 1, porque solo dos jóvenes han aprendido el canto».",
        "Hay que tener cuidado con los sesgos. Una música con pocos practicantes puede ser profundamente significativa, y una muy difundida puede tener poco significado local. Tampoco se compara una música con otra para decir cuál «vale más»: se evalúa cada una según su comunidad. Y si se trata de música de una comunidad que no es la propia, se consulta a sus portadores y se respeta su forma de decidir qué compartir.",
    ],
    [("criterio", "aspecto observable con que se evalúa"), ("permanencia", "que una música ha durado en el tiempo"), ("participación", "cantidad de personas que practican una música"), ("transmisión", "enseñanza de una música a nuevas generaciones"), ("sesgo", "idea previa que distorsiona una evaluación")],
    [
        ("Sumar puntajes", f"{MATRIZ}. ¿Cuántos puntos suma el canto de trabajo de la caleta, de un máximo de 10?", ["Los puntajes son 2, 1, 1, 2 y 2.", "2 + 1 + 1 + 2 + 2 = 8."], "8 de 10"),
        ("Detectar un riesgo", f"{MATRIZ}. ¿En qué criterios tiene puntaje 1 el canto de la caleta, y qué señala eso?", ["Participación 1 y transmisión 1.", "Son aspectos por cuidar."], "En participación y en transmisión; son aspectos por cuidar"),
    ],
    [
        ("Usar la suma como premio para decir «esta música vale más».", "La matriz sirve para comprender y cuidar, no para jerarquizar músicas.", "Acompaña los puntos con una justificación y un plan de cuidado."),
        ("Puntuar sin evidencia.", "Un puntaje sin razón no se puede discutir.", "Escribe un dato o una observación que sostenga cada puntaje."),
    ],
    [
        ex(f"{MATRIZ}. ¿Cuántos criterios tiene la matriz?", "5", "Son permanencia, participación, transmisión, significado y respeto."),
        ex(f"{MATRIZ}. ¿Cuál es el puntaje máximo posible de una música?", "10", "Son cinco criterios de hasta 2 puntos."),
        ex(f"{MATRIZ}. ¿Qué criterio mide si se enseña la música a las nuevas generaciones?", "La transmisión", "Es el criterio sobre la enseñanza a los jóvenes."),
    ],
    [
        ex(f"{MATRIZ}. ¿Qué música tiene el mayor puntaje en participación? A) El himno del club. B) El arrullo familiar.", "A", "El himno tiene 2 y el arrullo tiene 1."),
        ex("Una música tiene pocos practicantes, pero un enorme significado para su comunidad. ¿Cómo debe evaluarse? A) Se reconoce su significado, aunque la participación sea baja. B) Se descarta por tener pocos practicantes.", "A", "La relevancia no depende solo de la cantidad."),
        ex("¿Para qué sirve la matriz de criterios? A) Para comprender y decidir qué cuidar. B) Para decir qué música es la mejor del mundo.", "A", "Es una herramienta de comprensión."),
    ],
    [
        arith(f"{MATRIZ}. ¿Cuántos puntos suma el himno del club?", "1+2+2+2+2", "Se suman los cinco puntajes.", " puntos"),
        arith(f"{MATRIZ}. ¿Cuántos puntos suma el arrullo familiar?", "2+1+2+2+2", "Se suman los cinco puntajes.", " puntos"),
        ex(f"{MATRIZ}. ¿Qué música tiene el puntaje más bajo en la suma total? A) El canto de trabajo de la caleta. B) El himno del club.", "A", "Suma 8 y el himno suma 9."),
    ],
    [
        arith(f"{MATRIZ}. ¿Cuántos puntos le faltan al himno del club para el máximo de 10?", "10-9", "El himno suma 9 puntos; se restan del máximo.", " punto"),
        ex(f"{MATRIZ}. Para el canto de la caleta, ¿qué acción mejora la transmisión? A) Organizar talleres donde los pescadores mayores enseñen el canto a jóvenes. B) Subir el volumen.", "A", "Enseñar a nuevas generaciones es transmisión."),
    ],
    [
        ex(f"{MATRIZ}. Un estudiante dice: «El arrullo familiar vale menos porque lo canta menos gente que el himno». ¿Qué respuesta usa los criterios? A) El arrullo tiene participación 1, pero transmisión y significado 2; no se compara cuál vale más. B) Tiene razón, porque el himno suma más.", "A", "La matriz sirve para comprender cada música, no para jerarquizarla."),
        arith("Una música obtiene 2 en permanencia, 2 en participación, 0 en transmisión, 2 en significado y 2 en respeto. ¿Cuántos puntos le faltan para el máximo de 10?", "10-(2+2+0+2+2)", "La suma es 8; al máximo de 10 le faltan 2 puntos.", " puntos"),
    ],
    [ex(f"{MATRIZ}. La matriz muestra que la transmisión del canto de la caleta es 1. El municipio de ejemplo tiene recursos para una sola acción. ¿Cuál conviene? A) Un taller de enseñanza del canto. B) Un afiche con el puntaje total.", "A", "El taller trabaja el criterio más débil.")],
    [ex("¿Cuántos puntos puede tener cada criterio como máximo?", "2", "Va de 0 a 2."), ex("¿Qué se escribe junto a cada puntaje?", "Una justificación con evidencia", "Permite discutir el puntaje."), ex("¿Qué riesgo corre una música con transmisión baja?", "Corre el riesgo de dejar de transmitirse", "Hay que cuidarla.")],
    (
        "Usa la matriz de ejemplo para evaluar una música que conozcas (puede ser de tu familia o de tu barrio, sin datos personales). Escribe: a) el puntaje de 0 a 2 en cada criterio con una justificación breve, b) el total sobre 10, c) el criterio más bajo y una acción para cuidarlo, d) una frase de respeto hacia esa música.",
        "Música: cueca de las fiestas de mi barrio (de ejemplo). Permanencia 2 (se baila hace décadas); participación 2; transmisión 1 (solo algunos jóvenes la bailan); significado 2; respeto 2. Total 9. Criterio más bajo: transmisión; acción: talleres entre vecinos. Frase: es parte valiosa de mi comunidad.",
        ["cada puntaje tiene justificación", "el total se calcula bien", "propone una acción para el criterio más bajo"],
        ["matriz con cinco puntajes", "total, acción y frase de respeto"],
        ["puntajes sin evidencia", "jerarquizar músicas"],
        "Reconoce la matriz y pide justificar un puntaje con un dato distinto al escrito.",
    ),
    "Elige una música y dale un puntaje de 0 a 2 en transmisión, con una razón.",
    "Escribe qué otro criterio agregarías a la matriz y por qué.",
)

# ---------------------------------------------------------------- OA 07 · clase 4 (crear una forma de preservar y presentar)
CAPS = ("Plan de ejemplo de una «cápsula de memoria sonora» de 12 minutos: 1) entrevista breve a una persona de tu casa (con su permiso) sobre una canción que le importa: 3 minutos; "
        "2) cantar o tararear la canción dos veces: 2 minutos; 3) anotar la letra y rasgos audibles: 3 minutos; 4) escribir qué significa y cómo se transmitió: 2 minutos; 5) pedir permiso para compartirla con el curso: 2 minutos")
L(
    OA7, 4,
    f"Lápiz y papel. Plan de ejemplo, que se repite en los ejercicios: {CAPS}. Si lo practicas con una persona de tu casa, pídele permiso antes de anotar o grabar algo, y no escribas datos personales.",
    "Aprenderé a crear una forma de preservar y presentar una música significativa (una cápsula de memoria sonora) con una ficha de registro, y a respetar los permisos y las indicaciones de quienes la portan. Sirve para colaborar en la preservación de la cultura de manera respetuosa.",
    ["Sé evaluar la relevancia con criterios.", "Sé registrar versiones.", "Sé pedir permiso antes de grabar o compartir."],
    [
        "Preservar la música es ayudar a que siga viva y se transmita. Una forma sencilla de colaborar es hacer una cápsula de memoria sonora: un registro breve de una canción que importa a una persona o comunidad, con la canción, su contexto y lo que significa. La cápsula incluye una ficha: nombre de la canción, quién la comparte, para qué se usa, cómo se aprendió, rasgos audibles (tempo, voz, instrumentos) y el significado que le da la persona.",
        "La cápsula se hace con respeto. Antes de entrevistar, grabar o anotar, se pide permiso a la persona y se explica para qué sirve. Si la persona no quiere compartir algo, se respeta. No se escriben datos personales ni se publica nada sin permiso. Si la música pertenece a una comunidad con normas propias, se consulta a quienes la portan y se acepta lo que no se pueda compartir. La forma tradicional de una música de los pueblos originarios la enseña el educador o educadora tradicional o la comunidad, y el curso no la inventa ni la modifica.",
        "Al presentar la cápsula, se cuida la fidelidad: se cuenta con las palabras de la persona, sin adornar ni cambiar el sentido. Puede acompañarse con una frase de agradecimiento. También se puede preparar una versión nueva respetuosa, pero indicando siempre qué es lo original y qué se agregó. Así se preserva la cultura y se reconoce el trabajo de quienes la han cuidado.",
    ],
    [("cápsula de memoria sonora", "registro breve de una música con su contexto y significado"), ("ficha de registro", "hoja con los datos de una música: nombre, quién la comparte, uso, rasgos y significado"), ("permiso", "acuerdo de la persona antes de grabar, anotar o compartir"), ("fidelidad", "respeto al sentido original de lo que se registra"), ("portador", "persona que conserva y transmite una tradición")],
    [
        ("Sumar el tiempo", f"{CAPS}. ¿Cuántos minutos suman los cinco pasos?", ["3 + 2 + 3 + 2 + 2.", "Suman 12."], "12 minutos"),
        ("Aplicar el permiso", "Una compañera quiere grabar a su tío cantando, pero él dice «prefiero que no». ¿Qué hace ella?", ["El permiso es voluntario.", "Respeta su decisión y registra solo con anotaciones si él acepta."], "Respeta su decisión y no graba"),
    ],
    [
        ("Grabar o publicar sin avisar.", "Se necesita permiso de la persona y de la comunidad.", "Pide permiso y explica para qué será el registro."),
        ("Cambiar las palabras de la persona para que suenen mejor.", "Se pierde fidelidad y se altera el sentido original.", "Cuenta con las palabras de la persona y marca lo que agregas."),
    ],
    [
        ex(f"{CAPS}. ¿Cuántos pasos tiene el plan?", "5", "Están numerados del 1 al 5."),
        ex(f"{CAPS}. ¿Qué se hace en el último paso?", "Pedir permiso para compartir la canción con el curso", "Así lo dice el plan."),
        ex("Antes de anotar o grabar, ¿qué se debe pedir?", "El permiso de la persona", "Es una regla de respeto."),
    ],
    [
        ex("¿Qué datos lleva una ficha de registro? A) Nombre de la canción, quién la comparte, uso, rasgos audibles y significado. B) Dirección y teléfono de la persona.", "A", "Los datos personales no se anotan."),
        ex(f"{CAPS}. La persona entrevistada dice que una estrofa no se puede compartir. ¿Qué corresponde? A) Respetarlo y no incluir esa estrofa. B) Incluirla igual.", "A", "La persona decide qué compartir."),
        ex("¿Quién enseña la forma tradicional de una música de un pueblo originario? A) El educador o educadora tradicional o la comunidad. B) El curso a partir de lo que cree.", "A", "El curso no inventa ni modifica la tradición."),
    ],
    [
        arith(f"{CAPS}. Una estudiante repite el plan completo con 4 personas distintas, una después de otra. ¿Cuántos minutos necesita en total?", "12*4", "Se multiplican los minutos del plan por las personas.", " minutos"),
        ex("Una persona entrevistada cuenta que aprendió una canción de su abuela y la cantó 3 veces en la entrevista. ¿Cuántas veces conviene registrar la canción en la ficha? A) Una vez, con una nota de que se cantó 3 veces. B) Escribirla 3 veces con cambios.", "A", "La ficha registra la canción una vez, con su contexto."),
        ex("Un estudiante quiere subir la cápsula a una red pública. La persona entrevistada solo aceptó que se compartiera con el curso. ¿Qué hace? A) Respeta el acuerdo y la comparte solo con el curso. B) La sube igual.", "A", "El permiso se limita a lo acordado."),
    ],
    [
        arith(f"{CAPS}. Un grupo de 3 estudiantes hace una cápsula cada uno. ¿Cuántos minutos de plan suman entre los tres?", "12*3", "Se multiplican los minutos de una cápsula por las tres cápsulas.", " minutos"),
        ex("En la ficha una estudiante escribe: «Mi abuelo canta fatal y la letra no se entiende». ¿Qué problema tiene la anotación? A) Juzga a la persona en lugar de describir rasgos audibles. B) Es demasiado corta.", "A", "Una ficha describe lo que se oye y no emite juicios sobre quien canta."),
    ],
    [
        arith("Una cápsula de 12 minutos se amplía con 5 minutos más de entrevista y se quitan 2 minutos de anotación. ¿Cuántos minutos dura ahora?", "12+5-2", "Se suman y restan los cambios al total original.", " minutos"),
        ex("Un grupo quiere hacer una versión nueva de una canción de familia entrevistada. ¿Qué debe indicar para ser fiel? A) Qué parte es original y qué se agregó. B) Solo el nombre del grupo.", "A", "Marcar lo original y lo agregado respeta a la tradición."),
    ],
    [ex(f"{CAPS}. La persona entrevistada se emociona y se pone a llorar al recordar a quien le enseñó la canción. ¿Qué es lo más adecuado? A) Detener la entrevista con calma, agradecerle y dejar que decida si sigue. B) Seguir preguntando sin parar.", "A", "Cuidar a la persona es más importante que terminar el plan.")],
    [ex("¿Qué es una cápsula de memoria sonora?", "Un registro breve de una música con su contexto y significado", "Ayuda a preservar la música."), ex("¿Qué se hace si la persona no quiere compartir algo?", "Se respeta su decisión", "El permiso es voluntario."), ex("¿Qué dato no se anota en la ficha?", "Datos personales", "Se protege la privacidad.")],
    (
        "Prepara una ficha de registro para una cápsula de memoria sonora con una persona de tu casa o con un personaje imaginario (puedes inventar los datos de ejemplo). Escribe: a) nombre de la canción de ejemplo y para qué se usa, b) dos rasgos audibles, c) cómo se transmitió, d) qué significa para la persona, e) el permiso que pedirás y cómo lo pedirás.",
        "a) «Canción del cumpleaños»; se canta al soplar las velas. b) Melodía de cuatro notas; palmas suaves. c) La aprendió de su madre cantándola cada año. d) Le recuerda el cariño de su familia. e) «¿Puedo anotar y compartir con mi curso esta canción? Si prefieres, solo la anotaré para mí».",
        ["la ficha tiene todos los datos pedidos", "no incluye datos personales", "describe cómo se pide el permiso"],
        ["ficha con cinco partes a) a e)", "frase de permiso"],
        ["incluir datos personales", "juzgar a la persona"],
        "Reconoce la ficha y pide explicar qué harías si la persona acepta compartir solo una parte de la canción.",
    ),
    "Pregunta a una persona de tu casa si te cuenta una canción que le importa y pídele permiso antes de anotar algo.",
    "Escribe cinco preguntas respetuosas para una entrevista sobre una canción que importa a una persona.",
)

# ---------------------------------------------------------------- OA 07 · clase 5 (contrastar versiones y concluir)
VZ = ("Registro de ejemplo de una canción de fiesta de un pueblo (inventada). Versión de los abuelos: 90 pulsos por minuto; guitarra y voces; 5 estrofas; palabras que hablan de la cosecha. "
      "Versión actual de los jóvenes: 110 pulsos por minuto; guitarra, bajo y percusión; 3 estrofas; palabras que hablan de la cosecha y del trabajo en la ciudad. "
      "En ambas versiones se conserva la misma melodía del estribillo")
L(
    OA7, 5,
    f"Lápiz y papel. Registro de ejemplo, que se repite en los ejercicios: {VZ}.",
    "Aprenderé a registrar y contrastar dos versiones de una música que se transmite en el tiempo, para ver qué se conserva y qué cambia, y a evaluar con argumentos su relevancia para la identidad de una comunidad. Sirve para entender que la cultura cambia y se preserva a la vez.",
    ["Sé evaluar la relevancia con criterios.", "Sé comparar versiones con datos.", "Sé crear una cápsula respetuosa."],
    [
        "Las músicas de una comunidad no son piezas congeladas: cambian con el tiempo y con las personas que las practican. Contrastar dos versiones de una misma canción, por ejemplo la de los abuelos y la de los jóvenes, permite ver qué se conserva (la melodía del estribillo, el tema de las palabras) y qué cambia (el tempo, los instrumentos, el número de estrofas, los temas nuevos). Lo que se conserva suele ser lo que sostiene la identidad.",
        "Para contrastar se arma una tabla con los mismos datos de cada versión y se calculan las diferencias. En el registro de ejemplo, el tempo sube de 90 a 110 pulsos por minuto, 20 más; se agrega un bajo y una percusión; y las estrofas bajan de 5 a 3. Pero el estribillo es igual. Con estos datos se puede argumentar: la versión actual cambió la forma, pero conservó la melodía que reconoce la comunidad, así que la canción sigue siendo un símbolo compartido.",
        "Al concluir, se evita decir que la versión nueva es «peor» o «mejor». Se evalúa si el cambio mantiene el sentido para la comunidad y si las personas portadoras lo aprueban. Una conclusión sólida tiene tres partes: lo que se conserva, lo que cambia y por qué la música sigue siendo relevante, apoyada en datos y en la voz de la comunidad. Si la música es de un pueblo originario, esa voz es la de sus educadores tradicionales y su comunidad.",
    ],
    [("conservar", "mantener algo sin cambio entre versiones"), ("cambiar", "modificar un rasgo entre versiones"), ("versión", "forma concreta en que se interpreta una música en un momento"), ("símbolo", "elemento que representa a un grupo"), ("argumentar", "defender una idea con razones y datos")],
    [
        ("Calcular una diferencia", f"{VZ}. ¿Cuántos pulsos por minuto más tiene la versión actual que la de los abuelos?", ["La actual tiene 110 y la de los abuelos 90.", "110 − 90 = 20."], "20 pulsos por minuto"),
        ("Qué se conserva", f"{VZ}. ¿Qué se conserva en las dos versiones?", ["El registro dice que se conserva la melodía del estribillo.", "También se conserva el tema de la cosecha."], "La melodía del estribillo y el tema de la cosecha"),
    ],
    [
        ("Decir que la versión nueva es «peor» porque cambió.", "Los cambios pueden mantener el sentido para la comunidad.", "Evalúa qué se conserva y si la comunidad lo aprueba."),
        ("Pensar que una música que cambia deja de ser parte de la cultura.", "La cultura es dinámica y se transmite cambiando.", "Compara qué se conserva y qué cambia."),
    ],
    [
        ex(f"{VZ}. ¿Cuántas estrofas tiene la versión de los abuelos?", "5", "Así lo indica el registro."),
        ex(f"{VZ}. ¿Qué instrumentos nuevos se agregan en la versión actual, además de la guitarra?", "El bajo y la percusión", "Así lo indica el registro."),
        ex(f"{VZ}. ¿Qué tema nuevo aparece en las palabras de la versión actual?", "El trabajo en la ciudad", "Se suma a la cosecha, que se conserva."),
    ],
    [
        ex(f"{VZ}. ¿Qué mantiene el vínculo entre las dos versiones? A) La misma melodía del estribillo. B) El mismo número de estrofas.", "A", "Las estrofas son 5 y 3: es la melodía lo que se mantiene."),
        ex("¿Por qué una música puede seguir siendo relevante aunque cambie? A) Porque conserva elementos que la comunidad reconoce como propios. B) Porque se toca más fuerte.", "A", "Lo conservado sostiene la identidad."),
        ex("¿Quién tiene la voz principal para decidir si una versión mantiene el sentido de una música tradicional? A) La comunidad y las personas portadoras. B) Cualquiera que la haya escuchado una vez.", "A", "Ellas conocen el sentido original."),
    ],
    [
        arith(f"{VZ}. ¿Cuántas estrofas menos tiene la versión actual que la de los abuelos?", "5-3", "Se restan las estrofas de la actual a las de los abuelos.", " estrofas"),
        arith(f"{VZ}. Si la versión de los abuelos se canta 4 minutos a 90 pulsos por minuto, ¿cuántos pulsos suenan?", "90*4", "Se multiplican los pulsos por minuto por los minutos.", " pulsos"),
        ex(f"{VZ}. Un estudiante dice: «La versión de los jóvenes es peor porque es más rápida». ¿Es un argumento con criterios? Responde sí o no.", "No", "Juzga sin considerar qué se conserva ni la opinión de la comunidad."),
    ],
    [
        arith(f"{VZ}. En cada versión hay 4 compases de 4 pulsos por estrofa. ¿Cuántos pulsos tienen las 5 estrofas de la versión de los abuelos?", "5*4*4", "Se multiplican estrofas, compases y pulsos por compás.", " pulsos"),
        ex(f"{VZ}. Los jóvenes proponen agregar una cuarta estrofa con palabras nuevas, pero los mayores piden que no se cambie la melodía del estribillo. ¿Cómo se respetan ambas ideas? A) Agregar la estrofa y mantener la melodía del estribillo. B) Cambiar la melodía y mantener las palabras.", "A", "Se incorpora lo nuevo conservando lo que sostiene la identidad."),
    ],
    [
        arith("Una canción tiene versión de abuelos con 5 estrofas de 40 segundos cada una, y versión actual con 3 estrofas de 50 segundos. ¿Cuál dura más y cuántos segundos más? Responde la diferencia absoluta.", "5*40-3*50", "La de los abuelos dura 200 segundos y la actual 150; se restan.", " segundos"),
        ex("En una conversación con tu curso, alguien dice «lo importante es solo que la música guste». Otra persona responde con un argumento sobre relevancia cultural. ¿Cuál argumento es mejor? A) «La música es relevante porque conserva la memoria de una comunidad y se transmite a las nuevas generaciones.» B) «Es relevante porque es famosa.»", "A", "Se apoya en criterios de memoria y transmisión."),
    ],
    [ex(f"{VZ}. Quieres escribir tu conclusión sobre la relevancia de la canción. ¿Cuál es una buena estructura? A) Lo que se conserva, lo que cambia y por qué sigue siendo relevante, con datos. B) Una opinión sobre qué versión te gusta más.", "A", "Esa estructura se apoya en evidencia y criterios.")],
    [ex("¿Cuáles son las tres partes de una conclusión sólida?", "Lo que se conserva, lo que cambia y por qué sigue siendo relevante", "Se apoyan en datos."), ex("¿La cultura cambia o permanece siempre igual?", "Cambia y se preserva a la vez", "Se transmite con transformaciones."), ex(f"{VZ}. ¿A cuántos pulsos por minuto va la versión actual?", "110", "Así lo indica el registro.")],
    (
        "Redacta una conclusión sobre la relevancia de la canción de ejemplo del enunciado para la identidad del pueblo. Debe tener: a) una frase sobre lo que se conserva, con un dato, b) una frase sobre lo que cambia, con dos datos, c) una frase sobre por qué sigue siendo relevante, d) una frase de respeto a la voz de la comunidad.",
        "a) Se conserva la melodía del estribillo y el tema de la cosecha. b) Cambia el tempo, de 90 a 110 pulsos por minuto, y las estrofas, de 5 a 3. c) Sigue siendo relevante porque la comunidad la reconoce y las nuevas generaciones la cantan. d) La decisión final sobre qué cambiar la tiene la comunidad.",
        ["usa datos del registro", "separa lo que se conserva y lo que cambia", "incluye una frase de respeto"],
        ["conclusión de cuatro frases", "datos del registro"],
        ["decir que la versión nueva es peor", "no usar datos"],
        "Reconoce la conclusión y pide indicar qué dato adicional le gustaría tener a la comunidad antes de decidir un nuevo cambio.",
    ),
    "Escribe dos cosas que se conservan y dos que cambian en una canción que se cante en tu familia desde hace años.",
    "Compara dos versiones de una misma canción tuyas con una tabla de tres datos.",
)
