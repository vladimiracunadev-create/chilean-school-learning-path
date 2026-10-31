"""Student material for 6.º básico Música, OA 08 (reflexionar sobre fortalezas y áreas de mejora en audición, interpretación y creación, propia y de otros, con respeto y autocrítica).

Todos los casos, tablas y registros de los ejercicios son inventados para esta clase. La autoevaluación es personal: no se compara públicamente a nadie y los comentarios hablan de la música, no de las personas.
"""
from __future__ import annotations

from student_content_mu6_a import L
from student_lessons import arith, ex

OA8 = "MU06 OA 08"
RUB = ("rúbrica de la clase: cinco criterios (pulso estable, precisión de notas, dinámica coherente, final claro, concentración); cada uno se valora de 1 a 4 "
       "(1 = aún no, 2 = a veces, 3 = casi siempre, 4 = siempre); 3 o 4 es una fortaleza y 1 o 2 es un área de mejora")

# ---------------------------------------------------------------- OA 08 · clase 1 (fortalezas y áreas de mejora con evidencia)
L(
    OA8, 1,
    f"Lápiz y papel. {RUB.capitalize()}. Todos los casos están escritos en los ejercicios. Tu autoevaluación es personal y no se compara con la de otras personas.",
    "Aprenderé a reconocer mis fortalezas y mis áreas de mejora como oyente, intérprete y creador, usando una rúbrica y evidencia. Sirve para saber qué ya hago bien y qué practicar sin compararme con nadie.",
    ["Sé interpretar con pulso y dinámica.", "Sé qué es la evidencia audible.", "Sé contar y comparar números pequeños."],
    [
        f"Reflexionar sobre tu trabajo musical es mirar con calma qué haces bien y qué puedes mejorar. Una fortaleza es algo que ya haces de forma segura y un área de mejora es algo que todavía puedes practicar. Usamos esta {RUB}. Reconocer un área de mejora no es un fracaso: es la información que necesitas para progresar.",
        "Toda afirmación sobre tu trabajo necesita evidencia: un dato observable, como «de 8 compases, 7 salieron a tiempo» o «mantuve el pulso en las dos vueltas». «Soy malo» o «soy bueno» no son evidencia, porque no dicen qué se oyó. Una buena frase es: «Mi fortaleza es el pulso estable porque lo mantuve en toda la obra; mi área de mejora es el final claro porque terminé con un golpe a destiempo».",
        "Reflexionar sirve para la audición (qué escucho con atención y qué rasgos me cuesta reconocer), para la interpretación (cómo toco o canto) y para la creación (si cumplí el propósito de mi obra). No se trata de compararte con otra persona, sino con tu propio punto de partida, y de hacerlo con respeto hacia ti mismo y hacia quienes te rodean.",
    ],
    [("fortaleza", "algo que ya haces de forma segura"), ("área de mejora", "algo que aún puedes practicar para progresar"), ("evidencia", "dato observable que respalda lo que dices"), ("rúbrica", "tabla con criterios y niveles para valorar un trabajo"), ("autocrítica", "mirar tu propio trabajo con honestidad y respeto")],
    [
        ("Leer una rúbrica", "Una estudiante se valoró así: pulso 4, precisión 2, dinámica 3, final 1, concentración 3. ¿Cuántas fortalezas tiene según la regla (3 o 4)?", ["Pulso 4: fortaleza.", "Dinámica 3: fortaleza.", "Concentración 3: fortaleza.", "Precisión 2 y final 1: áreas de mejora."], "3 fortalezas"),
        ("Escribir con evidencia", "Convierte «toco mal el final» en una frase con evidencia, sabiendo que en 2 de 3 vueltas terminó a destiempo.", ["Digo el criterio: final claro.", "Agrego el dato: en 2 de 3 vueltas terminé a destiempo."], "Mi área de mejora es el final claro porque en 2 de 3 vueltas terminé a destiempo"),
    ],
    [
        ("Decir «soy malo» o «soy bueno» sin decir en qué.", "No dice qué se oyó; no sirve para mejorar.", "Escribe el criterio y un dato observable."),
        ("Esconder las áreas de mejora para parecer perfecto.", "Sin reconocerlas no se puede progresar.", "Escríbelas con calma y úsalas para planear la práctica."),
    ],
    [
        ex("Una fortaleza, ¿es algo que haces de forma segura o algo que aún practicas?", "Algo que haces de forma segura", "Es lo que ya dominas."),
        ex("Un área de mejora, ¿es un fracaso o una información para progresar?", "Una información para progresar", "Dice qué practicar."),
        ex("En la rúbrica de la clase, ¿qué valores hacen que un criterio sea una fortaleza: 1 y 2 o 3 y 4?", "3 y 4", "Esa es la regla de la clase."),
    ],
    [
        ex("Un criterio vale 2. ¿Es fortaleza o área de mejora?", "Área de mejora", "Los valores 1 y 2 son áreas de mejora."),
        ex("Una estudiante se valoró 4, 3, 3, 2 y 1 en los cinco criterios. ¿Cuántas áreas de mejora tiene?", "2", "Los valores 2 y 1 son áreas de mejora."),
        ex("¿Cuál frase tiene evidencia: (a) «Soy malo en el ritmo» o (b) «En 3 de 8 compases entré a destiempo»?", "(b)", "Tiene un dato observable."),
    ],
    [
        arith("Una estudiante se valoró 3, 4, 2, 4 y 3 en los cinco criterios. ¿Cuántos puntos suma?", "3+4+2+4+3", "Se suman las valoraciones de los cinco criterios.", " puntos"),
        ex("Si el máximo posible son 4 puntos por criterio en 5 criterios, ¿cuántos puntos es el máximo?", "20", "5 × 4 = 20."),
        ex("De 12 compases, un grupo tocó 9 a tiempo. ¿Cuántos compases salieron fuera de tiempo?", "3", "12 − 9 = 3."),
    ],
    [
        ex("Pedro dice que su fortaleza es el pulso porque su amigo toca peor. ¿Qué está mal en su razonamiento?", "Se compara con otra persona y no usa evidencia propia", "La fortaleza se apoya en datos propios."),
        ex("Una persona se valoró con puros 4 y dice que no tiene nada que mejorar, aunque su grupo dice que a veces se adelanta. ¿Qué podría hacer: revisar con evidencia o ignorar el comentario?", "Revisar con evidencia", "La autocrítica usa datos, incluidos los comentarios de otros."),
    ],
    [
        arith("En dos intentos, una estudiante valoró sus cinco criterios así: intento 1 suma 12 puntos, intento 2 suma 16 puntos. ¿Cuántos puntos subió?", "16-12", "Se resta el primer intento del segundo.", " puntos"),
        ex("Para un grupo, las fortalezas fueron pulso y dinámica y las áreas de mejora fueron final y precisión. ¿Qué criterio quedó sin clasificar si son los cinco de la rúbrica?", "La concentración", "Los cinco criterios son pulso, precisión, dinámica, final y concentración."),
    ],
    [ex("Una estudiante escribe: «Mi creación cumple su propósito de calma porque usé dinámica p y tempo lento; mi mejora es el final porque no tiene silencio». ¿Qué criterio de la rúbrica trata la mejora: el final claro o el pulso estable?", "El final claro", "Habla de cómo termina la obra.")],
    [ex("¿Qué necesita una afirmación sobre tu trabajo?", "Evidencia observable", "Un dato audible o contable."), ex("¿Qué es una rúbrica?", "Una tabla con criterios y niveles para valorar un trabajo", "Ordena la valoración."), ex("¿Con quién te comparas al reflexionar?", "Con tu propio punto de partida", "La reflexión es personal.")],
    (
        f"Elige una obra breve que hayas cantado, tocado o creado (por ejemplo una de las rondas de las clases anteriores). Valora cada criterio de la rúbrica ({RUB}) con un número del 1 al 4 y escribe una frase con evidencia por criterio. Luego escribe tu fortaleza principal y tu área de mejora principal. Esta tabla es personal; no tienes que mostrársela a nadie.",
        "Pulso 4 (mantuve el pulso en las dos vueltas). Precisión 3 (fallé una nota de 16). Dinámica 3 (hice el crescendo, pero no el diminuendo). Final 2 (terminé a destiempo en una de dos vueltas). Concentración 4. Fortaleza principal: pulso estable. Área de mejora: final claro.",
        ["valora los cinco criterios", "da evidencia en cada uno", "identifica una fortaleza y un área de mejora"],
        ["tabla de valoración", "frases con evidencia"],
        ["decir «soy malo» sin evidencia", "compararse con otras personas"],
        "Reconoce la valoración honesta y pide mostrar un ejemplo concreto de la obra que respalde la mayor fortaleza.",
    ),
    "Escribe una fortaleza tuya como oyente de música con una evidencia.",
    "Escribe qué evidencia reunirías para convencer a otra persona de que mejoraste en un criterio.",
)

# ---------------------------------------------------------------- OA 08 · clase 2 (comentar el trabajo de otros con respeto)
FOR = "fórmula del comentario respetuoso: 1) algo que se oyó bien y por qué (evidencia); 2) una sugerencia concreta para mejorar; 3) hablar de la música, nunca de la persona"

L(
    OA8, 2,
    f"Lápiz y papel. {FOR.capitalize()}. Los trabajos que se comentan están descritos en los ejercicios. Si comentas el trabajo de alguien real, hazlo solo si esa persona quiere recibir el comentario.",
    "Aprenderé a comentar el trabajo musical de otras personas con respeto: decir qué se oyó bien, sugerir una mejora concreta y hablar de la música. Sirve para ayudar a otros a progresar y para aprender a recibir comentarios.",
    ["Sé que una afirmación necesita evidencia.", "Sé reconocer fortalezas y áreas de mejora.", "Sé qué es una sugerencia concreta."],
    [
        f"Comentar el trabajo de otras personas es parte de aprender música juntos. {FOR}. Un comentario sirve cuando dice algo que se pueda oír, como «mantuvieron el pulso en toda la ronda», y cuando propone un cambio que la otra persona pueda probar, como «prueben bajar el volumen en la parte B para que se oiga la flauta».",
        "Hay comentarios que no ayudan: los que hablan de la persona («tú siempre desafinas»), los que comparan («lo hacen peor que el otro curso») y los vagos («estuvo bien», «estuvo mal»). Un comentario respetuoso pregunta primero qué buscaba la persona con su obra, y se hace en un tono amable y en el momento adecuado, no delante de todos si la persona no quiere.",
        "Recibir un comentario también se aprende. Escuchas sin interrumpir, agradeces, preguntas si no entendiste y decides qué usar. No estás obligado a cambiar todo; basta con elegir lo que te ayuda. Cuando tú comentas y cuando recibes, practicas la autocrítica y el respeto, que es el centro de este objetivo.",
    ],
    [("comentario respetuoso", "opinión sobre la música con evidencia y una sugerencia"), ("sugerencia concreta", "cambio específico que se puede probar"), ("comentario vago", "comentario que no dice qué se oyó"), ("tono amable", "forma de hablar que cuida a la otra persona"), ("recibir un comentario", "escuchar, agradecer y decidir qué usar")],
    [
        ("Elegir el comentario", "¿Qué comentario sigue la fórmula: (a) «Estuvo mal» o (b) «Se oyó bien el pulso porque todos entraron juntos; prueben cantar más suave en la segunda estrofa»?", ["La (a) es vaga.", "La (b) dice qué se oyó bien con evidencia y propone un cambio."], "(b)"),
        ("Cambiar un comentario", "Cambia «tú siempre desafinas» por un comentario sobre la música, sabiendo que en los compases 5 y 6 se oyó una nota más aguda de lo que debía.", ["Hablo de la música, no de la persona.", "Digo dónde se oyó y propongo algo."], "En los compases 5 y 6 una nota sonó más aguda; prueben cantarlos lento para afinar"),
    ],
    [
        ("Responder a un comentario con enojo o explicaciones largas.", "Así no se escucha lo que puede servir.", "Escucha, agradece y luego decide."),
        ("Elogiar solo para quedar bien, sin evidencia.", "Un elogio sin evidencia no ayuda a mejorar.", "Di qué se oyó y por qué estuvo bien."),
    ],
    [
        ex("¿De qué debe hablar un comentario respetuoso sobre un trabajo musical?", "De la música, no de la persona", "Es la tercera parte de la fórmula."),
        ex("¿Cuántas partes tiene la fórmula del comentario respetuoso?", "3", "Son evidencia positiva, sugerencia y hablar de la música."),
        ex("Si recibes un comentario que no entiendes, ¿qué haces: preguntar o ignorarlo?", "Preguntar", "Preguntar ayuda a entenderlo."),
    ],
    [
        ex("¿Cuál comentario es vago: (a) «Estuvo bien» o (b) «Se oyó el crescendo en los compases 5 a 8»?", "(a)", "No dice qué se oyó."),
        ex("¿Cuál es una sugerencia concreta: (a) «Toquen mejor» o (b) «Prueben bajar el volumen de los panderos en la segunda parte»?", "(b)", "Se puede probar."),
        ex("«Lo hacen peor que el otro curso» es un comentario que compara. ¿Sigue la fórmula?", "No", "Compara con otros y no dice qué se oyó."),
    ],
    [
        ex("Un grupo tocó una ronda de 8 compases. Se oyó el pulso estable, pero en el compás 5 el volumen tapó la flauta. Escribe qué evidencia positiva y qué sugerencia darías. Responde con la sugerencia.", "Prueben bajar el volumen en el compás 5 para que se oiga la flauta", "La sugerencia es concreta y se refiere al compás 5."),
        ex("¿Qué es mejor decir a una compañera después de su presentación si ella no quiere comentarios: «Si quieres, te cuento lo que escuché» o dar el comentario delante de todos?", "«Si quieres, te cuento lo que escuché»", "Se respeta su decisión."),
        ex("Un comentario dice «tu parte estuvo bien porque mantuviste el pulso en las dos vueltas». ¿Tiene evidencia?", "Sí", "Dice qué se oyó: pulso en dos vueltas."),
    ],
    [
        ex("Ana dice que decir lo que está mal es faltar el respeto. ¿Qué responderías?", "Que se puede decir con evidencia y una sugerencia, hablando de la música", "El respeto está en cómo se dice."),
        ex("Dos comentarios al mismo trabajo: A «La flauta empezó a tiempo, pero en el final los panderos sonaron muy fuertes y taparon la melodía; prueben p en el final». B «Qué mala la ronda». ¿Cuál es más útil y por qué?", "A, porque da evidencia y una sugerencia", "B no dice qué se oyó ni cómo mejorar."),
    ],
    [
        arith("Un curso se divide en 5 grupos. Cada grupo recibe 3 comentarios de otros grupos. ¿Cuántos comentarios se dan en total?", "5*3", "Se multiplica por los grupos.", " comentarios"),
        arith("Un grupo recibió 6 comentarios: 4 siguen la fórmula y el resto son vagos. ¿Cuántos son vagos?", "6-4", "Se restan los que siguen la fórmula.", " comentarios"),
    ],
    [ex("Escuchas la creación de un compañero y piensas «me aburrió». ¿Cuál es el comentario más útil: (a) «Me aburrió», (b) «Tu melodía repite la misma idea en los cuatro compases; prueba cambiar la última nota de uno»?", "(b)", "Dice qué se oyó y propone un cambio.")],
    [ex("¿Qué debe llevar un comentario además de una sugerencia?", "Algo que se oyó bien con evidencia", "La fórmula pide ambas."), ex("Cuando alguien comenta tu trabajo, ¿qué conviene hacer?", "Escuchar, agradecer y decidir qué usar", "Así se aprende de él."), ex("¿Se comenta a la persona o a la música?", "A la música", "La persona se respeta.")],
    (
        "Lee esta ficha de un trabajo inventado: «Ronda de 8 compases cantada por 4 estudiantes. Mantuvieron el pulso. En el compás 6 uno se adelantó. El final fue suave y claro.» Escribe tres comentarios respetuosos siguiendo la fórmula (uno sobre lo que salió bien, otro sobre el compás 6 con sugerencia y otro sobre el final). Luego escribe cómo responderías si recibes un comentario sobre tu parte.",
        "1) Mantuvieron el pulso en toda la ronda, y eso se oyó firme. 2) En el compás 6 uno se adelantó; prueben cantarlo lento mirándose para entrar juntos. 3) El final fue suave y claro, y eso cerró la ronda con calma; para mantenerlo, prueben cantar el último compás igual de tranquilo en cada vuelta. Al recibir un comentario: escucharía sin interrumpir, diría gracias, preguntaría si no entiendo y elegiría lo que me ayude.",
        ["los tres comentarios siguen la fórmula", "hablan de la música y no de las personas", "incluyen cómo recibir un comentario"],
        ["tres comentarios escritos"],
        ["comentarios vagos", "hablar de la persona"],
        "Reconoce los comentarios y pide señalar la evidencia de cada uno en la ficha.",
    ),
    "Reescribe un comentario vago que hayas recibido para que siga la fórmula.",
    "Escribe una frase con la que pedirías respetuosamente un comentario sobre tu trabajo.",
)

# ---------------------------------------------------------------- OA 08 · clase 3 (autocrítica con datos)
REG = "registro de una práctica: cada vuelta se anota cuántos compases salieron sin error y qué tipo de error hubo (pulso, nota o volumen)"

L(
    OA8, 3,
    f"Lápiz y papel. {REG.capitalize()}. Los registros de práctica están escritos en los ejercicios; en tu práctica anota los tuyos. Cuida el volumen.",
    "Aprenderé a hacer autocrítica con datos: llevar un registro de mi práctica, contar errores, comparar intentos y descubrir qué error se repite más. Sirve para decidir con evidencia qué practicar primero.",
    ["Sé reconocer fortalezas y áreas de mejora.", "Sé formular un comentario con evidencia.", "Sé sumar y restar números pequeños."],
    [
        f"La autocrítica con datos significa usar un registro para revisar tu trabajo. En esta clase usamos este {REG}. Con ese registro puedes saber cuántos compases salen bien en cada intento y cuál es el error más frecuente. Los datos evitan juicios injustos como «todo me sale mal».",
        "Para comparar intentos se restan los errores: si en el intento 1 hubo 6 errores y en el intento 2 hubo 4, mejoraste en 2. También se cuenta qué tipo de error se repite más. Si hay 5 errores de pulso, 2 de nota y 1 de volumen, el error más frecuente es el de pulso, y conviene practicar eso primero. Se trabaja un solo tipo de error a la vez.",
        "La autocrítica es honesta y amable a la vez: reconoce lo que aún no sale y también lo que mejoró. Una frase de autocrítica clara dice el dato, la comparación y la decisión: «En el intento 2 bajé de 6 a 4 errores; el más frecuente es el pulso; la próxima semana practicaré con palmas el compás 6». No necesitas ser perfecto: necesitas ver avances reales.",
    ],
    [("registro de práctica", "tabla con compases sin error y tipos de error de cada intento"), ("error más frecuente", "el tipo de error que más se repite"), ("comparar intentos", "restar los errores de un intento y otro"), ("autocrítica con datos", "juzgar el propio trabajo con números y no solo con impresiones"), ("avance", "mejora que se puede medir")],
    [
        ("Comparar dos intentos", "Intento 1: 7 errores. Intento 2: 4 errores. ¿Cuántos errores menos hubo en el intento 2?", ["Resto los errores del intento 2 a los del intento 1.", "7 − 4 = 3."], "3 errores menos"),
        ("Hallar el error más frecuente", "En un registro hubo 3 errores de pulso, 5 de nota y 2 de volumen. ¿Cuál es el error más frecuente?", ["Comparo las tres cantidades: 3, 5 y 2.", "La mayor es 5."], "El error de nota"),
    ],
    [
        ("Corregir todos los errores a la vez.", "Se pierde el foco y cuesta ver qué mejoró.", "Elige el error más frecuente y trabaja ese."),
        ("Decir «todo me sale mal» sin mirar el registro.", "Los datos muestran avances que la impresión esconde.", "Revisa el registro y cuenta."),
    ],
    [
        ex("¿Qué anota un registro de práctica: errores y tipos o solo el nombre de la obra?", "Errores y tipos", "Eso es lo que define el registro de la clase."),
        ex("Intento 1: 5 errores. Intento 2: 2 errores. ¿Mejoró o empeoró?", "Mejoró", "Tuvo menos errores."),
        ex("¿Cuántos tipos de error considera la clase?", "3", "Pulso, nota y volumen."),
    ],
    [
        arith("Intento 1: 9 errores. Intento 2: 6 errores. ¿Cuántos errores menos hubo?", "9-6", "Se resta el segundo intento del primero.", " errores"),
        ex("En un registro hubo 4 errores de pulso, 1 de nota y 1 de volumen. ¿Qué error se practica primero?", "El de pulso", "Es el más frecuente."),
        ex("De 8 compases, 6 salieron sin error. ¿Cuántos tuvieron error?", "2", "8 − 6 = 2."),
    ],
    [
        arith("En tres intentos hubo 8, 5 y 3 errores. ¿Cuántos errores menos hubo en el tercero que en el primero?", "8-3", "Se compara el primero con el tercero.", " errores"),
        arith("Un registro tiene 4 errores de pulso, 3 de nota y 2 de volumen. ¿Cuántos errores hay en total?", "4+3+2", "Se suman los tres tipos.", " errores"),
        ex("Si los errores de volumen fueron 2 de un total de 9, ¿cuántos errores no fueron de volumen?", "7", "9 − 2 = 7."),
    ],
    [
        ex("Una estudiante dice que no mejora porque en el intento 3 tuvo 1 error más que en el intento 2, pero tuvo 5 menos que en el intento 1. ¿Qué dice el registro sobre su avance?", "Que mejoró respecto del primer intento aunque tuvo un tropiezo", "Comparar con el punto de partida muestra el avance."),
        ex("Un grupo anota 3 errores de pulso, 3 de nota y 1 de volumen. ¿Hay un único error más frecuente?", "No: hay dos con la misma cantidad", "El pulso y la nota empatan con 3."),
    ],
    [
        arith("En una semana, un grupo hizo 4 prácticas y tuvo 12 errores en total. Si cada práctica tuvo la misma cantidad, ¿cuántos errores hubo por práctica?", "12//4", "Se reparten los errores en las prácticas.", " errores"),
        ex("Si en la práctica 1 hubo 10 errores y cada práctica siguiente baja 2, ¿cuántos errores habrá en la práctica 4?", "4", "10 − 2 − 2 − 2 = 4."),
    ],
    [ex("Una cantante lleva este registro de cuatro compases del coro: compás 1 sin error, compás 2 con error de pulso, compás 3 con error de nota y compás 4 con error de pulso. ¿Cuál es su error más frecuente?", "El de pulso", "Hay 2 errores de pulso y 1 de nota.")],
    [ex("¿Qué se hace con el error más frecuente?", "Se practica primero", "Es donde más se gana."), ex("¿Cómo se comparan dos intentos?", "Restando los errores", "La diferencia muestra el avance."), ex("¿Qué evitan los datos?", "Juicios injustos como «todo me sale mal»", "Muestran lo que realmente pasó.")],
    (
        "Usa este registro inventado de una práctica de una obra de 8 compases. Intento 1: 3 errores de pulso, 2 de nota, 1 de volumen. Intento 2: 2 errores de pulso, 1 de nota, 1 de volumen. Calcula el total de errores de cada intento, cuántos menos hubo en el intento 2 y cuál es el error más frecuente en el intento 2. Después escribe una frase de autocrítica con el dato, la comparación y la decisión. Si practicas una obra tuya, haz tu propio registro.",
        "Intento 1: 3 + 2 + 1 = 6 errores. Intento 2: 2 + 1 + 1 = 4 errores. Hubo 2 menos. El error más frecuente en el intento 2 es el de pulso (2). Frase: «Bajé de 6 a 4 errores; el más frecuente es el pulso; practicaré con palmas los compases difíciles antes de la próxima vuelta».",
        ["calcula los totales y la diferencia", "identifica el error más frecuente", "escribe una frase con dato, comparación y decisión"],
        ["cálculos escritos", "frase de autocrítica"],
        ["no usar datos", "intentar corregirlo todo a la vez"],
        "Reconoce el uso de datos y pide mostrar cómo contó los errores.",
    ),
    "Anota cuántos compases de una canción tuya salen sin error en tres vueltas.",
    "Diseña un registro de práctica con tres columnas para una semana.",
)

# ---------------------------------------------------------------- OA 08 · clase 4 (plan de mejora)
PLAN = "un plan de mejora tiene cuatro partes: una meta con número y plazo; acciones concretas; cuándo y cuánto se practica; y cómo se revisará el avance"

L(
    OA8, 4,
    f"Lápiz y papel. {PLAN.capitalize()}. Los planes del ejercicio son inventados; puedes armar el tuyo con lo que reflexionaste en las clases anteriores. Cuida el volumen y descansa los oídos y la voz.",
    "Aprenderé a armar un plan de mejora para mis fortalezas y áreas de mejora en audición, interpretación y creación, con una meta clara y una forma de revisar el avance. Sirve para convertir la reflexión en acciones que realmente se hagan.",
    ["Sé reconocer áreas de mejora con evidencia.", "Sé llevar un registro de práctica.", "Sé calcular tiempos con multiplicaciones."],
    [
        f"Después de reflexionar viene actuar. {PLAN.capitalize()}. Una meta buena es medible, como «bajar de 6 a 2 errores de pulso en las próximas 3 semanas», no vaga, como «tocar mejor». Una acción concreta es algo que se puede hacer, como «practicar con palmas los compases 5 a 8, lento, 3 veces».",
        "El plan debe ser realista. Si dispones de 10 minutos al día, un plan de 2 horas diarias no se cumple. Por ejemplo, 3 prácticas por semana de 10 minutos durante 4 semanas son 12 prácticas y 120 minutos. También se piensa qué hacer si algo falla: si un día no puedes practicar, lo recuperas el siguiente.",
        "El plan se revisa en una fecha fija con el registro de práctica: ¿llegué a la meta?, ¿mejoré aunque no llegara?, ¿qué cambiaría? Si la meta se cumple, se pone una nueva; si no, se ajusta el plan, no a la persona. Un plan de mejora también puede incluir una fortaleza que quieres usar para ayudar a otros, como acompañar el pulso del grupo.",
    ],
    [("plan de mejora", "pasos para mejorar un área con meta, acciones, tiempo y revisión"), ("meta medible", "objetivo con un número y un plazo"), ("acción concreta", "algo específico que se puede hacer y comprobar"), ("realista", "posible de cumplir con el tiempo que tienes"), ("revisión", "momento para comprobar el avance con datos")],
    [
        ("Distinguir la meta", "¿Cuál es una meta medible: (a) «tocar mejor» o (b) «bajar de 6 a 2 errores de pulso en 3 semanas»?", ["La (a) no tiene número ni plazo.", "La (b) tiene números y plazo."], "(b)"),
        ("Calcular el tiempo", "Un plan es 3 prácticas por semana de 10 minutos durante 4 semanas. ¿Cuántos minutos son en total?", ["Prácticas: 3 × 4 = 12.", "Minutos: 12 × 10 = 120."], "120 minutos"),
    ],
    [
        ("Hacer un plan demasiado grande para el tiempo que tienes.", "No se cumple y desanima.", "Calcula el tiempo disponible antes de decidir."),
        ("Cambiar la meta cada día.", "No se puede medir el avance.", "Mantén la meta hasta la fecha de revisión."),
    ],
    [
        ex("¿Cuántas partes tiene el plan de mejora de la clase?", "4", "Son meta, acciones, tiempo y revisión."),
        ex("Una meta con número y plazo, ¿es medible o vaga?", "Medible", "Se puede comprobar."),
        ex("¿Con qué se revisa el avance: con el registro de práctica o con la intuición?", "Con el registro de práctica", "Los datos muestran el avance."),
    ],
    [
        ex("¿Cuál es una acción concreta: (a) «Esforzarme más» o (b) «Practicar los compases 5 a 8 lento, 3 veces, con palmas»?", "(b)", "Se puede hacer y comprobar."),
        ex("Una persona tiene 10 minutos al día. ¿Es realista un plan de 2 horas diarias?", "No", "Supera por mucho el tiempo disponible."),
        ex("Si cumples tu meta, ¿qué haces: quedarte igual o poner una meta nueva?", "Poner una meta nueva", "El plan se renueva."),
    ],
    [
        arith("Un plan tiene 4 prácticas por semana de 15 minutos durante 3 semanas. ¿Cuántos minutos son?", "4*3*15", "Se calculan las prácticas y luego los minutos.", " minutos"),
        arith("Tu meta es bajar de 8 errores a 3. ¿Cuántos errores tienes que reducir?", "8-3", "Se resta la meta del punto de partida.", " errores"),
        ex("Si cada semana bajas 2 errores y partes de 8, ¿cuántas semanas necesitas para llegar a 2?", "3", "8 → 6 → 4 → 2 en 3 semanas."),
    ],
    [
        ex("Dos planes: A «Practicaré más». B «Practicaré 3 veces por semana 10 minutos el compás 6 lento para bajar de 5 a 2 errores de pulso en 3 semanas; revisaré el viernes de la tercera semana con mi registro». ¿Cuál es mejor y por qué?", "B, porque tiene meta medible, acciones, tiempo y revisión", "A no tiene ninguna de las cuatro partes."),
        ex("Ana dice que si no cumple la meta, el problema es ella. ¿Qué es más útil: ajustar el plan o culparse?", "Ajustar el plan", "El plan se revisa y se cambia, no se juzga a la persona."),
    ],
    [
        arith("Un plan de 5 semanas tiene 2 prácticas por semana de 20 minutos y un ensayo final de 30 minutos. ¿Cuántos minutos son?", "5*2*20+30", "Se suman las prácticas y el ensayo final.", " minutos"),
        ex("Una estudiante parte con 6 errores. En la revisión de la semana 2 tiene 4 y en la semana 4 tiene 2. ¿Cuántos errores bajó en total?", "4", "6 − 2 = 4."),
    ],
    [ex("Un grupo tiene como fortaleza el pulso estable y como área de mejora el final claro. ¿Qué puede incluir su plan de mejora: usar el pulso estable para ensayar el final lento o abandonar la obra?", "Usar el pulso estable para ensayar el final lento", "Una fortaleza puede apoyar la mejora.")],
    [ex("¿Qué característica tiene una meta medible?", "Tiene número y plazo", "Se puede comprobar."), ex("¿Qué debe ser un plan?", "Realista", "Se debe poder cumplir."), ex("¿Cuándo se revisa el plan?", "En una fecha fija, con el registro", "Así se ve el avance.")],
    (
        f"Arma tu plan de mejora para una obra (tuya o la ronda de las clases). Escribe: el área de mejora con su evidencia, una meta con número y plazo, dos acciones concretas, el calendario (cuántas prácticas por semana y de cuántos minutos) con el total de minutos, y cómo revisarás el avance con tu registro. Recuerda: {PLAN}.",
        "Área de mejora: el final claro (en 2 de 3 vueltas terminé a destiempo). Meta: terminar a tiempo en 3 de 3 vueltas en 3 semanas. Acciones: practicar los compases 7 y 8 lento con palmas y contar un silencio antes del último golpe. Calendario: 3 prácticas por semana de 10 minutos durante 3 semanas: 9 prácticas y 90 minutos. Revisión: el viernes de la tercera semana, con el registro de las tres vueltas.",
        ["tiene meta medible, acciones, calendario y revisión", "calcula bien los minutos", "es realista"],
        ["plan escrito"],
        ["metas vagas", "no revisar con datos"],
        "Reconoce el plan y pide mostrar cómo comprobará el avance con su registro.",
    ),
    "Escribe una meta medible para una de tus áreas de mejora.",
    "Escribe un plan de dos semanas para mejorar tu forma de escuchar música con atención.",
)
