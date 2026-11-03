"""Cuaderno del estudiante de 8.º básico Artes Visuales: AR08 OA 05 (evaluación de trabajos visuales personales y de pares con materialidad, lenguaje visual y propósito expresivo)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA5 = "AR08 OA 05"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def w(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def m(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=[ctx], selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- Clase 1
lesson(
    OA5, 1,
    "Hojas y lápiz. Los tres trabajos de ejemplo están descritos en esta clase; no necesitas buscarlos.",
    "Aprenderé a evaluar un trabajo visual con tres criterios, evidencia y una retroalimentación respetuosa, sin quedarme en «me gusta» o «no me gusta». Sirve para mejorar mis trabajos y ayudar a mis compañeros.",
    ["Sé analizar una obra con contexto, materialidad, lenguaje visual y propósito.", "Sé separar descripción de opinión."],
    [
        "Evaluar un trabajo visual no es decir si me gusta. Es juzgarlo con criterios y con evidencia que se ve. Uso tres criterios: la materialidad, es decir, cómo se usaron los materiales y las técnicas; el lenguaje visual, es decir, cómo se usan línea, color, forma, textura y composición; y el propósito expresivo, es decir, si el trabajo comunica lo que quería comunicar.",
        "Una rúbrica es una tabla que describe cómo se ve cada criterio en distintos niveles. En esta clase uso tres niveles: por mejorar (1 punto, hay fallas), logrado (2 puntos, cumple) y destacado (3 puntos, cumple y además aporta algo más); en la clase 3 verás la rúbrica con sus descriptores completos. Para cada criterio busco una evidencia, algo que se ve en el trabajo, y elijo el nivel que mejor la describe. Mi retroalimentación, es decir, el comentario que ayuda a mejorar, sigue el modelo «veo… me pregunto… podrías…»: una observación, una pregunta y una sugerencia.",
        "Evalúo el trabajo, no a la persona. No digo «eres malo para el dibujo»; digo «el árbol tiene colores fuertes y los edificios pálidos, por eso el árbol destaca». Con trabajos de otras personas uso un lenguaje respetuoso. Y al observar sin copiar, tomo un criterio o un recurso que me sirve para mi propio trabajo, sin imitar el trabajo evaluado.",
    ],
    [("evaluar", "juzgar un trabajo con criterios y evidencia"), ("criterio", "aspecto que se revisa, como materialidad, lenguaje visual o propósito"), ("rúbrica", "tabla que describe cada criterio en distintos niveles"), ("evidencia", "algo que se ve en el trabajo y respalda el nivel"), ("retroalimentación", "comentario que ayuda a mejorar un trabajo")],
    [
        w("Aplicar la rúbrica", "Collage de ejemplo «Gotas»: fondo de papel de diario, gotas azules recortadas de revista, pegadas en diagonal y cada vez más pequeñas hacia abajo; una gota se despega por poca cola. La intención es mostrar que el agua se acaba. Evalúa los tres criterios.", ["Materialidad: una gota se despega por poca cola; nivel por mejorar.", "Lenguaje visual: la diagonal y las gotas que disminuyen ordenan la composición; nivel logrado.", "Propósito expresivo: las gotas que se achican muestran que el agua se acaba; nivel logrado."], "Materialidad 1, lenguaje visual 2 y propósito 2"),
        w("Reescribir un comentario", "Reescribe con el modelo «veo… me pregunto… podrías…» este comentario sobre un estampado de seis hojas verdes en fila: «Está feo».", ["Veo: seis hojas verdes estampadas en fila con tinta pareja.", "Me pregunto: ¿querías mostrar crecimiento?", "Podrías: hacer cada hoja un poco más grande que la anterior."], "«Veo seis hojas verdes en fila con tinta pareja; me pregunto si querías mostrar crecimiento; podrías hacer cada hoja un poco más grande»"),
    ],
    [
        m("Evaluar con frases como «me gusta» o «está feo».", "No hay criterio ni evidencia y el autor no sabe qué cambiar.", "Usa un criterio, una evidencia visible y una sugerencia."),
        m("Comentar a la persona y no al trabajo.", "Hiere y no ayuda a mejorar.", "Habla de lo que se ve en el trabajo."),
    ],
    [
        ex("¿Cuál comentario usa un criterio y una evidencia? A. «El azul de las gotas contrasta con el diario gris» B. «Me gusta mucho».", "A", "Señala algo que se ve: el contraste de color."),
        ex("Entre materialidad, lenguaje visual y propósito expresivo, ¿qué criterio revisa si el trabajo comunica lo que quería?", "El propósito expresivo", "Mide si el mensaje llega."),
        ex("En una rúbrica de tres niveles (por mejorar, logrado, destacado), ¿cuál es el nivel intermedio?", "Logrado", "Está entre por mejorar y destacado."),
    ],
    [
        ex("En un dibujo, los colores se corrieron porque la hoja estaba mojada. ¿Qué criterio muestra esa evidencia? A. Materialidad B. Propósito expresivo.", "A", "Habla de cómo se usó el material."),
        ex("Comentario: «Veo el árbol con colores fuertes y los edificios pálidos; me pregunto si querías que el árbol fuera el centro; podrías agregar sombras bajo el árbol». ¿Cuál es la pregunta?", "«Me pregunto si querías que el árbol fuera el centro»", "Es la parte que indaga la intención del autor."),
        ex("Alguien comenta: «Eres malo para dibujar». ¿A qué evalúa? A. A la persona B. Al trabajo.", "A", "No habla de lo que se ve en el trabajo."),
    ],
    [
        arith("En una rúbrica con 1, 2 y 3 puntos por criterio, un trabajo obtiene 2 en materialidad, 3 en lenguaje visual y 2 en propósito. ¿Cuántos puntos suma?", "2+3+2", "Se suman los puntos de los tres criterios."),
        arith("Con tres criterios de hasta 3 puntos cada uno, ¿cuántos puntos es el máximo posible?", "3*3", "Se multiplican los criterios por el puntaje máximo."),
        ex("Un estampado de seis hojas verdes tiene tinta pareja y sin manchas. ¿Qué nivel de materialidad describe mejor esa evidencia: por mejorar o logrado?", "Logrado", "El material está bien usado y sin fallas."),
    ],
    [
        ex("Dos comentarios sobre el dibujo de la calle gris con el árbol coloreado. X) «Está mal pintado». Y) «El árbol tiene colores fuertes y los edificios pálidos, por eso destaca». ¿Cuál sirve para el autor?", "Y", "Dice qué se ve y qué efecto produce."),
        ex("Quieres tomar un recurso del dibujo del árbol para tu trabajo sin imitarlo. ¿Qué plan lo hace? A. Usar el contraste de un elemento de color fuerte sobre fondo pálido en un tema propio B. Dibujar la misma calle con el mismo árbol.", "A", "Toma el recurso y cambia el tema."),
    ],
    [
        ex("Un trabajo suma 7 de 9 puntos. En materialidad obtuvo 2 y en lenguaje visual 2. ¿Qué puntaje tiene en propósito expresivo?", "3", "2 más 2 son 4; para llegar a 7 faltan 3 puntos."),
        ex("Un trabajo suma 9 de 9, pero la evaluación no anota ninguna evidencia. ¿Qué falta?", "La evidencia que respalde cada nivel", "Sin evidencia el puntaje no se puede comprobar."),
    ],
    ex("Tu curso evalúa el collage «Gotas». ¿Cuál es el mejor comentario? A. «Veo gotas azules cada vez más pequeñas hacia abajo; me pregunto si querías mostrar que el agua se acaba; podrías pegar la gota que se despega con más cola» B. «Está más o menos, mejora».", "A", "Tiene observación, pregunta y sugerencia concreta."),
    [
        ex("¿Cuáles son los tres criterios de evaluación de la clase?", "Materialidad, lenguaje visual y propósito expresivo", "Son los que se miden en cada trabajo."),
        ex("Verdadero o falso: evaluar es decir si algo me gusta.", "Falso", "Evaluar usa criterios y evidencia visible."),
        ex("¿Cuáles son las tres partes del comentario de retroalimentación?", "Veo, me pregunto y podrías", "Una observación, una pregunta y una sugerencia."),
    ],
    task(
        "Elige UN trabajo de ejemplo. A) Collage «Gotas»: fondo de diario, gotas azules recortadas de revista en diagonal y cada vez más pequeñas hacia abajo; una gota se despega. B) Estampado en tela: seis hojas verdes en fila, de igual tamaño, con tinta pareja, sobre fondo blanco; propósito, mostrar crecimiento. C) Dibujo de una calle gris con un árbol al centro con colores fuertes y edificios de colores pálidos; propósito, la naturaleza al centro. Evalúa los tres criterios con niveles de 1 a 3 y una evidencia en cada uno, escribe el comentario con «veo… me pregunto… podrías…» y haz un boceto que tome un recurso para tu propio trabajo sin imitar.",
        "Elegí la B. Materialidad 2: tinta pareja sin manchas. Lenguaje visual 2: las hojas están en fila ordenada. Propósito 1: las hojas son iguales, no se ve crecimiento. Comentario: «Veo seis hojas verdes de igual tamaño; me pregunto si querías mostrar crecimiento; podrías hacer cada hoja un poco más grande». Boceto: filas de círculos que crecen, con mi propio tema.",
        ["asigna un nivel con evidencia a los tres criterios", "escribe veo, me pregunto y podrías", "habla del trabajo y no de la persona", "hace un boceto propio que no imita el trabajo evaluado"],
        ["rúbrica con evidencias", "comentario de tres partes", "boceto"],
        ["decir solo «me gusta»", "imitar el trabajo evaluado"],
        "Pregunta qué evidencia sostiene el nivel más bajo y qué sugerencia concreta propuso.",
    ),
    "Mira un objeto decorado de tu casa y di en voz alta una evidencia visual y una sugerencia, sin decir si te gusta.",
    "Reescribe un comentario tuyo anterior de tipo «me gusta» con el modelo veo, me pregunto y podrías.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA5, 2,
    "Hojas y lápiz. Las tres declaraciones de autores están escritas en esta clase.",
    "Aprenderé a investigar el propósito, el material y el contexto de un trabajo antes de evaluarlo, para juzgar si cumple lo que su autor quería y con lo que tenía. Sirve para evaluar con justicia.",
    ["Sé los tres criterios de evaluación.", "Sé escribir un comentario con veo, me pregunto y podrías."],
    [
        "Antes de evaluar el trabajo de un compañero, le pregunto: ¿qué querías lograr?, ¿con qué materiales contabas? y ¿para quién es? Así conozco su propósito y su contexto. Evalúo si el trabajo cumple el propósito del autor con los materiales que tenía, no si cumple mi gusto. Si dijo «quise mostrar calma con tinta azul diluida», busco evidencia de calma, como los espacios vacíos y el azul suave.",
        "Las condiciones importan. Si el autor trabajó solo con diario, lápiz y cola porque no tenía colores, no le exijo pintura. Evalúo cómo usó lo que tenía. Un propósito declarado es una frase breve del autor que dice qué quiso lograr; la uso como punto de partida. No es una excusa: igual reviso si el trabajo muestra evidencia de ese propósito.",
        "Distingo «no cumple mi gusto» de «no cumple su propósito». «No me gustan los colores» habla de mí. «Quería alegría y el trabajo usa azules y grises apagados» habla del propósito. Si aún no conozco el propósito, lo pregunto antes de evaluar. Con esa información, mi comentario es más justo y más útil.",
    ],
    [("propósito declarado", "frase del autor que dice qué quiso lograr"), ("condición", "situación que limita un trabajo, como pocos materiales o poco tiempo"), ("justo", "que juzga según el propósito y las condiciones del autor"), ("gusto", "lo que a mí me agrada, que no es un criterio"), ("autor", "persona que hizo el trabajo")],
    [
        w("Leer un propósito", "Una autora de ejemplo escribe: «Quise mostrar que los árboles de mi plaza crecen entre autos. Usé solo diario, lápiz y cola; no tenía colores». Su collage tiene árboles de diario entre cuadrados grises que son autos. Identifica propósito y condición.", ["Propósito: mostrar que los árboles crecen entre autos.", "Condición: solo tenía diario, lápiz y cola."], "Propósito: árboles entre autos; condición: sin colores"),
        w("Evaluar con justicia", "El mismo collage no tiene colores. Un compañero escribe «le falta color». ¿Es un comentario justo?", ["La autora no tenía colores.", "El comentario no considera su condición ni su propósito."], "No es justo; debería evaluar cómo logra el propósito con diario, lápiz y cola"),
    ],
    [
        m("Evaluar según lo que a mí me gustaría ver.", "El autor tenía otro propósito y otras condiciones.", "Evalúa si cumple su propósito con lo que tenía."),
        m("Evaluar sin saber qué quería lograr el autor.", "No hay con qué comparar el resultado.", "Pregunta primero «¿qué querías lograr?»."),
    ],
    [
        ex("Antes de evaluar a un compañero, ¿qué le preguntas? A. «¿Qué querías lograr?» B. «¿Por qué no usaste los colores que a mí me gustan?»", "A", "Así conoces su propósito."),
        ex("Un autor solo tenía lápiz de grafito y hojas de cuaderno. ¿Qué condición consideras al evaluar su materialidad?", "Que trabajó solo con grafito, sin colores", "Se evalúa cómo usó lo que tenía."),
        ex("Un autor dice «quise mostrar calma». ¿Qué criterio revisas para saber si lo logró?", "El propósito expresivo", "Mide si el trabajo comunica lo que se quería."),
    ],
    [
        ex("Una autora quería mostrar calma con tinta azul diluida. El trabajo tiene azul muy diluido y muchos espacios vacíos. ¿Cumple su propósito? A. Sí, la tinta diluida y los espacios vacíos transmiten calma B. No, porque faltan colores.", "A", "La evidencia visible respalda el propósito."),
        ex("Tu evaluación dice «no me gustan los colores». ¿Qué problema tiene? A. Evalúa tu gusto y no el propósito del autor B. Es demasiado técnica.", "A", "El gusto no es un criterio."),
        ex("Un estampado de seis hojas en fila es para decorar una bolsa de pan. ¿Qué propósito evalúas? A. Que sirva como decoración de una bolsa B. Que sea una obra de museo.", "A", "Es el propósito que declara el autor."),
    ],
    [
        arith("Una autora hizo 3 pruebas de ejemplo y cada una le tomó 40 minutos. ¿Cuántos minutos trabajó en pruebas?", "3*40", "Se multiplican las pruebas por los minutos de cada una."),
        arith("Usó 14 hojas de diario para 7 árboles, con la misma cantidad de hojas en cada uno. ¿Cuántas hojas usó por árbol?", "14//7", "Se reparten las hojas en partes iguales."),
        ex("Una autora escribe: «Tenía solo 30 minutos y papel reciclado». ¿Es una condición del trabajo o un propósito?", "Una condición", "Dice con qué contaba, no qué quiso lograr."),
    ],
    [
        ex("Ema dice «no me gusta cómo quedó» sobre un collage de diario. Luis dice «con solo diario logra que el árbol destaque al dejar los autos en gris». ¿Quién considera el contexto y el propósito?", "Luis", "Evalúa lo logrado con los materiales dados."),
        ex("Un compañero te pide que evalúes su trabajo y tú no sabes su propósito. ¿Qué haces?", "Le pregunto su propósito antes de evaluar", "Sin propósito no hay con qué comparar."),
    ],
    [
        ex("Un autor quería mostrar alegría y su trabajo usa solo azules y grises apagados. ¿Qué comentario sirve? A. «Veo azul y gris apagados; me pregunto si querías alegría; podrías probar un color cálido» B. «Está mal».", "A", "Relaciona evidencia con propósito y sugiere un cambio."),
        ex("Dos trabajos tienen el mismo tema: uno con muchos materiales y otro con solo papel y lápiz. ¿Se espera lo mismo de ambos en cantidad de materiales?", "No", "Se evalúa cómo cada uno usa los materiales que tenía."),
    ],
    ex("Una compañera te muestra su estampado de seis hojas verdes para una bolsa de pan y dice que quiso mostrar crecimiento. ¿Qué haces primero? A. Buscar evidencia de crecimiento en el trabajo, como hojas que aumentan de tamaño B. Decirle que prefieres el rojo.", "A", "El propósito declarado guía qué evidencia buscar."),
    [
        ex("¿Qué es un propósito declarado?", "Una frase del autor que dice qué quiso lograr", "Es el punto de partida de la evaluación."),
        ex("Verdadero o falso: puedo exigir pintura a un trabajo hecho solo con diario.", "Falso", "Se evalúa con las condiciones del autor."),
        ex("¿Qué preguntas haces antes de evaluar?", "Qué querías lograr, con qué materiales contabas y para quién es", "Así evalúas con justicia."),
    ],
    task(
        "Elige UNA declaración de autor. A) «Quise mostrar que los árboles de mi plaza crecen entre autos. Usé solo diario, lápiz y cola.» B) «Quise mostrar calma con tinta azul diluida sobre papel reciclado.» C) «Mi estampado de hojas es para decorar una bolsa de pan.» Escribe qué evidencia visible buscarías en el trabajo, qué condiciones consideras y un comentario justo con veo, me pregunto y podrías.",
        "Elegí la B. Evidencia a buscar: azul muy diluido y espacios vacíos. Condición: papel reciclado, tinta de un solo color. Comentario: «Veo azul diluido y muchos espacios vacíos; me pregunto si querías mostrar calma; podrías dejar un espacio vacío aún más grande al centro».",
        ["identifica el propósito y las condiciones", "busca evidencia relacionada con el propósito", "escribe un comentario con tres partes", "no evalúa por su gusto"],
        ["propósito y condiciones anotados", "evidencia propuesta", "comentario"],
        ["evaluar por el gusto personal", "ignorar las condiciones del autor"],
        "Pregunta qué parte del comentario depende del propósito del autor y no del gusto de quien comenta.",
    ),
    "Cuéntale a una persona de tu casa para qué hiciste un dibujo tuyo y pídele que diga si ve evidencia de ese propósito.",
    "Escribe dos propósitos distintos para el mismo tema y explica cómo cambiaría la evidencia que buscarías.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA5, 3,
    "Hojas y lápiz. La rúbrica que usarás está escrita en esta clase.",
    "Aprenderé a usar una rúbrica de tres niveles, a diferenciar autoevaluación de coevaluación y a escribir un comentario con evidencia. Sirve para evaluar de forma ordenada y comprobable.",
    ["Sé evaluar con tres criterios y evidencia.", "Sé conocer el propósito del autor antes de evaluar."],
    [
        "Una rúbrica de ejemplo para esta clase. Materialidad: 1 punto si los materiales se despegan, manchan o rompen; 2 si están firmes y limpios; 3 si además el material aporta al mensaje. Lenguaje visual: 1 si los elementos no tienen orden y no se distingue la figura principal; 2 si la figura se distingue y los elementos están ordenados; 3 si además la composición dirige la vista. Propósito expresivo: 1 si no se entiende qué comunica; 2 si se entiende con una explicación; 3 si se entiende sin explicar.",
        "Con la rúbrica sigo tres pasos. Primero, anoto una evidencia visible por criterio. Segundo, elijo el nivel cuyo descriptor mejor calza con esa evidencia. Tercero, escribo el comentario con «veo… me pregunto… podrías…». La autoevaluación es evaluar mi propio trabajo; la coevaluación es evaluar el trabajo de un compañero con los mismos criterios. Ambas usan la misma rúbrica y piden evidencia.",
        "Un nivel sin evidencia no se puede comprobar. Si dos personas dan niveles distintos, vuelvo a leer los descriptores y comparo las evidencias, no cambio mi nota solo para igualarla. Sumo los puntos de los tres criterios: el máximo es 9. Pero el puntaje no reemplaza el comentario: el comentario es lo que ayuda al autor a mejorar.",
    ],
    [("descriptor", "frase que describe cómo se ve un criterio en un nivel"), ("autoevaluación", "evaluación del propio trabajo"), ("coevaluación", "evaluación del trabajo de un compañero con criterios acordados"), ("nivel", "grado de logro de un criterio: 1, 2 o 3 puntos"), ("puntaje", "suma de los puntos de los criterios")],
    [
        w("Elegir el nivel", "Un trabajo tiene la figura principal bien distinta y los elementos ordenados, pero la vista no sabe por dónde seguir. ¿Qué nivel de lenguaje visual tiene?", ["Descriptor 2: la figura se distingue y los elementos están ordenados.", "Descriptor 3 pide además que la composición dirija la vista.", "La evidencia calza con el 2."], "Nivel 2 (logrado)"),
        w("Sumar y comentar", "Un trabajo obtiene 3 en materialidad, 2 en lenguaje visual y 1 en propósito. ¿Cuánto suma y qué criterio mejorarías primero?", ["Sumo 3, 2 y 1.", "El criterio con menos puntos es el propósito."], "6 de 9 puntos; mejorar primero el propósito expresivo"),
    ],
    [
        m("Poner un nivel sin anotar ninguna evidencia.", "No se puede comprobar ni discutir.", "Escribe qué viste que justifica el nivel."),
        m("Cambiar mi nota solo para igualar la de otra persona.", "No resuelve la diferencia de evidencias.", "Relee los descriptores y compara evidencias."),
    ],
    [
        ex("Un material se despega y mancha. ¿Qué nivel de materialidad tiene según la rúbrica?", "Nivel 1 (por mejorar)", "El descriptor 1 habla de materiales que se despegan o manchan."),
        ex("El mensaje de un trabajo se entiende sin que el autor lo explique. ¿Qué nivel de propósito expresivo tiene?", "Nivel 3 (destacado)", "El descriptor 3 pide que se entienda sin explicar."),
        ex("¿Cómo se llama evaluar el trabajo de un compañero con los mismos criterios?", "Coevaluación", "Se hace entre pares."),
    ],
    [
        ex("La figura se distingue, los elementos están ordenados y además la composición lleva la vista de la figura al título. ¿Qué nivel de lenguaje visual describe eso?", "Nivel 3", "Cumple el descriptor de destacado."),
        ex("¿Qué debe acompañar cada nivel? A. Una evidencia visible B. Una opinión personal.", "A", "La evidencia permite comprobar el nivel."),
        ex("El material está firme y limpio, pero no aporta al mensaje. ¿Qué nivel de materialidad tiene?", "Nivel 2", "El 3 exige que además aporte al mensaje."),
    ],
    [
        arith("Un trabajo obtiene 1 en materialidad, 3 en lenguaje visual y 3 en propósito expresivo. ¿Cuántos puntos suma?", "1+3+3", "Se suman los puntos de los tres criterios."),
        arith("En una coevaluación, cuatro compañeros dieron 2, 3, 2 y 3 puntos en lenguaje visual. ¿Cuántos puntos suman entre los cuatro?", "2+3+2+3", "Se suman los cuatro puntajes."),
        ex("¿Cuál comentario sigue el modelo veo, me pregunto y podrías? A. «Veo letras grandes abajo; me pregunto si querías que se lean desde lejos; podrías agrandar la primera palabra» B. «Podrías mejorar todo».", "A", "Tiene una observación, una pregunta y una sugerencia."),
    ],
    [
        ex("Ana pone nivel 3 en materialidad y anota «el cartón forma parte del mensaje». Beto pone nivel 3 sin escribir nada. ¿Cuál evaluación se puede comprobar?", "La de Ana", "Tiene evidencia anotada."),
        ex("Tu coevaluación dio 3 en propósito y la del autor dio 1. ¿Qué haces primero? A. Pedirle la evidencia que usó y mostrarle la tuya B. Cambiar tu nota para igualarla.", "A", "Se comparan las evidencias."),
    ],
    [
        ex("Un trabajo suma 8 de 9 puntos con 3 en materialidad y 3 en lenguaje visual. ¿Qué nivel tiene en propósito expresivo?", "Nivel 2", "3 más 3 son 6; para llegar a 8 faltan 2."),
        arith("Un trabajo tenía 5 de 9 puntos y tras revisar sube a 8. ¿Cuántos puntos le faltan para el máximo?", "9-8", "El máximo es 9."),
    ],
    ex("Evalúas un estampado de seis hojas en fila donde cada hoja es más grande que la anterior y se entiende crecimiento sin explicación. ¿Qué nivel de propósito expresivo le pones?", "Nivel 3", "Se entiende sin explicar."),
    [
        ex("¿Qué diferencia hay entre autoevaluación y coevaluación?", "La primera evalúa el propio trabajo; la segunda, el de un compañero", "Las dos usan la misma rúbrica."),
        ex("Verdadero o falso: un nivel sin evidencia se puede comprobar igual.", "Falso", "La evidencia es lo que permite comprobar."),
        ex("¿Cuál es el máximo de puntos con tres criterios de hasta 3 puntos?", "9", "Tres criterios por 3 puntos."),
    ],
    task(
        "Usa la rúbrica de la clase para evaluar UN trabajo de ejemplo. A) Collage de gotas azules en diagonal que se achican hacia abajo, sobre diario; una gota se despega. B) Estampado de seis hojas verdes de igual tamaño, en fila, con tinta pareja. C) Dibujo con un árbol de color fuerte al centro y edificios pálidos. Anota una evidencia por criterio, elige el nivel, suma los puntos y escribe el comentario con veo, me pregunto y podrías. Después evalúa un trabajo tuyo reciente con la misma rúbrica y compara.",
        "Elegí la C. Materialidad 2: colores firmes y limpios. Lenguaje visual 3: el color fuerte lleva la vista al árbol. Propósito 2: se entiende naturaleza al centro con una explicación breve. Suma 7. Comentario: «Veo el árbol con color fuerte y edificios pálidos; me pregunto si querías que se entienda sin explicar; podrías poner sombra bajo el árbol».",
        ["anota una evidencia por criterio", "elige el nivel según el descriptor", "suma correctamente", "escribe un comentario de tres partes y compara con su autoevaluación"],
        ["rúbrica completa", "puntaje", "comentario", "comparación con la autoevaluación"],
        ["poner niveles sin evidencia", "cambiar la nota solo para igualar"],
        "Pregunta qué descriptor calzó con la evidencia del criterio con menos puntos.",
    ),
    "Evalúa en voz alta un envase de tu casa con un criterio de la rúbrica y di la evidencia que viste.",
    "Escribe dos descriptores propios para un cuarto criterio, como la limpieza del trabajo, en los niveles 1 y 3.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA5, 4,
    "Hojas, lápiz y, si los tienes, lápices de colores. El trabajo de ejemplo está descrito en esta clase.",
    "Aprenderé a escribir una retroalimentación completa para un trabajo, con rúbrica, comentario y un plan de mejora con acciones concretas. Sirve para ayudar a otra persona a mejorar y para mejorar mis propios trabajos.",
    ["Sé usar una rúbrica de tres niveles con evidencia.", "Sé escribir un comentario con veo, me pregunto y podrías."],
    [
        "Una retroalimentación completa tiene cinco pasos. Primero leo el propósito del autor. Segundo, completo la rúbrica con una evidencia por criterio. Tercero, escribo el comentario con «veo… me pregunto… podrías…». Cuarto, propongo un plan de mejora con acciones concretas. Quinto, acuerdo cuándo volveré a mirar el trabajo para reevaluarlo.",
        "Una acción concreta dice qué se hace, con qué material y cuándo. «Mejorar la composición» no es concreta. «Pegar la gota que se despega con más cola hoy y recortar tres gotas más pequeñas para el viernes» sí lo es. Las acciones deben poder hacerse con lo que el autor tiene: si solo tiene diario, no le sugiero acuarelas. Priorizo uno o dos cambios, porque cambiar todo a la vez no deja ver qué funcionó.",
        "El tono importa: hablo del trabajo, uso verbos como «podrías» o «te propongo» y explico la evidencia que sostiene cada sugerencia. Si el autor no acepta una sugerencia, respeto su decisión: el trabajo es suyo. Mi comentario es un aporte, no una orden. Con un plan claro, el autor sabe qué hacer y yo puedo comprobar después si el cambio funcionó.",
    ],
    [("plan de mejora", "lista de acciones concretas para mejorar un trabajo"), ("acción concreta", "paso que dice qué se hace, con qué y cuándo"), ("priorizar", "elegir los cambios más importantes primero"), ("reevaluar", "volver a evaluar después de un cambio"), ("sugerencia", "propuesta que ayuda a mejorar, no una orden")],
    [
        w("Armar un plan", "Trabajo de ejemplo: un collage de gotas azules en diagonal sobre diario; una gota se despega y las gotas son todas del mismo tamaño. El autor solo tiene diario, revistas y cola. Propón un plan de mejora con dos acciones concretas.", ["Acción 1: pegar la gota que se despega con más cola hoy.", "Acción 2: recortar de revista tres gotas más pequeñas para el viernes y pegarlas hacia abajo.", "Ambas se pueden hacer con sus materiales."], "Pegar la gota hoy y recortar tres gotas más pequeñas para el viernes"),
        w("Hacer concreta una acción", "Haz concreta esta acción: «Mejorar el color».", ["No dice qué cambio ni con qué.", "Agrego qué: repetir el verde del árbol en un arbusto pequeño.", "Agrego con qué y cuándo."], "«Pintar un arbusto pequeño con el mismo verde del árbol, con témpera, en la próxima clase»"),
    ],
    [
        m("Sugerir cambios que el autor no puede hacer con sus materiales.", "No se puede cumplir y desanima.", "Propón acciones con lo que tiene."),
        m("Pedir cambios en los tres criterios a la vez.", "Es demasiado y no se ve qué funcionó.", "Prioriza uno o dos cambios."),
    ],
    [
        ex("Según los cinco pasos, ¿qué paso va justo antes de escribir el comentario?", "Completar la rúbrica con evidencias", "El comentario se apoya en las evidencias."),
        ex("El plan dice «Estampar la segunda hoja con tinta más pareja el jueves». ¿Qué parte es el plazo?", "«El jueves»", "Dice cuándo se hace."),
        ex("¿Qué acción es concreta? A. «Estampar la hoja con menos tinta» B. «Esforzarse más».", "A", "Dice qué se hace."),
    ],
    [
        ex("El autor solo tiene diario, lápiz y cola. ¿Qué sugerencia puede hacer? A. «Recortar más gotas de diario y repetirlas en diagonal» B. «Comprar acuarelas».", "A", "Se hace con sus materiales."),
        ex("¿Qué comentario es respetuoso? A. «Veo gotas del mismo tamaño; podrías hacer algunas más pequeñas» B. «Eres lento».", "A", "Habla del trabajo y propone."),
        ex("Un plan dice «mejorar la composición». ¿Qué le falta? A. Una acción concreta y un plazo B. Más palabras.", "A", "No dice qué hacer ni cuándo."),
    ],
    [
        arith("Tu plan tiene 3 acciones y cada una toma 15 minutos. ¿Cuántos minutos necesitas?", "3*15", "Se multiplican las acciones por los minutos de cada una."),
        arith("Un trabajo tiene 7 de 9 puntos. Con el plan sube 1 punto en dos criterios. ¿Cuántos puntos tendrá?", "7+1+1", "Se suman los puntos que subió en cada criterio."),
        ex("¿Cuál comentario tiene observación, pregunta y sugerencia? A. «Veo un árbol con color fuerte; me pregunto si querías que sea el centro; podrías agregar sombra» B. «Bien, sigue así».", "A", "Tiene las tres partes."),
    ],
    [
        ex("Plan X: «Hacerlo mejor». Plan Y: «Recortar cartón en tres tamaños el martes y estampar las hojas el viernes». ¿Cuál se puede ejecutar y comprobar?", "Y", "Dice qué hacer y cuándo."),
        ex("Un compañero no acepta una de tus sugerencias. ¿Qué haces? A. Explicar la evidencia que la sostiene y respetar su decisión B. Insistir hasta que cambie.", "A", "El trabajo es suyo."),
    ],
    [
        ex("Tu comentario sugiere cambios en los tres criterios a la vez. ¿Qué problema tiene para el autor?", "Son demasiados cambios y no se ve cuál funcionó", "Conviene priorizar uno o dos."),
        ex("Un trabajo tiene materialidad 1, lenguaje visual 3 y propósito 2. ¿Qué criterio priorizarías para subir más puntos?", "La materialidad", "De 1 puede subir hasta 3, dos puntos más."),
    ],
    ex("Tu compañero te entrega un dibujo de una calle gris con un árbol coloreado; su propósito es poner la naturaleza al centro. ¿Qué sugerencia se apoya en la evidencia? A. «Veo el árbol con color fuerte y los edificios pálidos; podrías agregar sombras bajo el árbol para reforzar que es el centro» B. «Cambia el tema».", "A", "Parte de la evidencia y respeta el propósito."),
    [
        ex("¿Qué dice una acción concreta?", "Qué se hace, con qué material y cuándo", "Así se puede ejecutar y comprobar."),
        ex("Verdadero o falso: debo insistir hasta que el autor acepte mi sugerencia.", "Falso", "El trabajo es del autor."),
        ex("¿Por qué priorizar uno o dos cambios?", "Para ver qué cambio funcionó", "Cambiar todo a la vez lo impide."),
    ],
    task(
        "Elige UN trabajo de ejemplo. A) Collage de gotas azules del mismo tamaño en diagonal sobre diario; una gota se despega; el autor tiene diario, revistas y cola. B) Estampado de seis hojas verdes iguales en fila; el autor quiere mostrar crecimiento; tiene témpera y cartón. C) Dibujo de una calle gris con árbol de color fuerte y edificios pálidos; el autor tiene lápices de colores. Completa la rúbrica con evidencias, escribe el comentario con veo, me pregunto y podrías, y un plan de mejora con dos acciones concretas (qué, con qué y cuándo). Acuerda cuándo reevaluarás.",
        "Elegí la B. Materialidad 2, lenguaje visual 2, propósito 1. Comentario: «Veo seis hojas iguales; me pregunto si querías mostrar crecimiento; podrías hacer cada hoja más grande». Plan: 1) Recortar cartón en 6 tamaños crecientes hoy. 2) Estampar con témpera verde el viernes. Reevaluar el lunes.",
        ["completa la rúbrica con evidencia", "escribe el comentario de tres partes", "propone dos acciones concretas con lo que el autor tiene", "acuerda un momento para reevaluar"],
        ["rúbrica", "comentario", "plan de mejora"],
        ["acciones vagas", "sugerir materiales que el autor no tiene"],
        "Pregunta qué acción es la más importante y cómo se comprobará que funcionó.",
    ),
    "Dile a una persona de tu casa una sugerencia concreta para algo que hizo, con qué material y cuándo, hablando del trabajo y no de la persona.",
    "Reescribe un plan vago como «mejorar todo» en tres acciones concretas para un dibujo tuyo.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA5, 5,
    "Tu evaluación de la clase anterior, hojas y lápiz. Si no la tienes, usa el caso descrito en esta clase.",
    "Aprenderé a contrastar mi autoevaluación con la coevaluación de otra persona, a decidir qué cambio hacer con evidencia y a reevaluar el trabajo después del cambio. Sirve para mejorar sin quedarme con mi primera impresión.",
    ["Sé usar una rúbrica con evidencia.", "Sé escribir un plan de mejora concreto."],
    [
        "Cuando mi autoevaluación y la coevaluación no coinciden, no busco quién tiene razón: comparo las evidencias. Si me puse 3 en propósito y mi compañera me puso 1, le pregunto qué vio y le muestro lo que yo vi. Vuelvo a leer el descriptor del nivel. La diferencia me dice que el efecto del trabajo en otra persona no es igual a mi intención, y eso es información para mejorar.",
        "Luego decido qué sugerencia aceptar. Elijo las que se apoyan en evidencia y sirven a mi propósito, y dejo las que no. Hago el cambio, reevalúo con la misma rúbrica y comparo antes y después. Si el puntaje sube pero el propósito sigue sin entenderse, el cambio no fue suficiente. Si el comentario que di a otra persona no fue concreto, ella no cambia nada: eso me indica que debo mejorar mi comentario.",
        "Para evitar sesgos, uso la misma rúbrica y pido evidencia con todas las personas, sin importar si son amigas. Y soy cuidadoso al concluir: si tres de cuatro compañeros mejoraron, puedo decir que mi comentario ayudó a tres de esas cuatro personas, no a todos los estudiantes. Una evaluación honesta usa datos y dice hasta dónde llegan.",
    ],
    [("sesgo", "preferencia que hace evaluar sin evidencia, por simpatía o antipatía"), ("discrepancia", "diferencia entre dos evaluaciones del mismo trabajo"), ("antes y después", "comparación entre el trabajo original y el trabajo cambiado"), ("conclusión", "afirmación que se apoya en los datos que tengo"), ("honesto", "que dice lo que muestran los datos, sin exagerar")],
    [
        w("Comparar evaluaciones", "Te autoevalúas con 3 en propósito. Tres compañeros te ponen 2, 2 y 3. ¿Cuántos coinciden contigo y qué haces?", ["Solo uno puso 3.", "Dos pusieron 2: hay discrepancia.", "Pregunto qué evidencia vieron esos dos."], "Coincide 1 de 3; pregunto la evidencia de los otros dos"),
        w("Reevaluar", "Tras un cambio, tu trabajo pasó de 4 a 7 puntos. ¿Cuántos puntos subió y qué falta comprobar?", ["Resto 7 menos 4.", "Falta ver si el propósito se entiende mejor, con la misma rúbrica."], "Subió 3 puntos; falta comprobar con la misma rúbrica si el propósito se entiende"),
    ],
    [
        m("Cambiar mi nota para igualar la de otra persona.", "No se resuelve la diferencia de evidencias.", "Compara evidencias y relee los descriptores."),
        m("Decir que mi comentario ayuda a todos porque ayudó a tres compañeros.", "Tres personas no representan a todos.", "Concluye solo para las personas consultadas."),
    ],
    [
        ex("Tu autoevaluación en propósito es 3 y la coevaluación es 1. ¿Coinciden?", "No", "Hay una diferencia de dos niveles."),
        ex("Cuando las evaluaciones no coinciden, ¿qué comparas primero? A. La evidencia que usó cada persona B. Quién tiene más amigos.", "A", "La evidencia permite resolver la diferencia."),
        ex("Si dos evaluaciones del mismo trabajo son distintas, ¿cómo se llama esa diferencia?", "Discrepancia", "Es el término de la clase."),
    ],
    [
        ex("Tu autoevaluación en propósito es 2. Tres compañeros ponen 2, 1 y 2. ¿Cuántos coinciden contigo?", "2", "Coinciden quienes pusieron 2."),
        ex("La coevaluación dice que no se entiende el mensaje y tú creías que sí. ¿Qué información útil entrega? A. Que el efecto en quien mira difiere de tu intención B. Que el compañero se equivoca.", "A", "Es una diferencia entre intención y efecto."),
        ex("Dos personas dan niveles distintos a lenguaje visual con la misma evidencia. ¿Qué haces? A. Releer el descriptor del nivel junto a la evidencia B. Promediar sin mirar.", "A", "Los descriptores resuelven la diferencia."),
    ],
    [
        arith("Tu autoevaluación suma 8 puntos y la coevaluación suma 6. ¿Cuántos puntos de diferencia hay?", "8-6", "Se resta la menor de la mayor."),
        arith("Antes del cambio el trabajo tenía 5 puntos y después 9. ¿Cuántos puntos subió?", "9-5", "Se resta el puntaje de antes al de después."),
        ex("Tras hacer el cambio, ¿qué haces? A. Reevaluar con la misma rúbrica y comparar B. Cambiar la rúbrica para que salga mejor.", "A", "Con la misma rúbrica se compara antes y después."),
    ],
    [
        ex("Diego se autoevalúa 9 de 9 y dice que no hay nada que mejorar. Dos compañeros le dan 6 y 5. ¿Qué debería revisar primero?", "Las evidencias de los criterios en que difieren", "Ahí está la discrepancia."),
        ex("¿Qué reduce el sesgo al evaluar? A. Usar la misma rúbrica y pedir evidencia a todos B. Evaluar por simpatía.", "A", "Los criterios son iguales para todas las personas."),
    ],
    [
        ex("Tu comentario fue «mejora todo» y el autor no cambió nada. ¿Qué puede indicar?", "Que el comentario no fue lo bastante concreto", "Una sugerencia concreta permite actuar."),
        ex("Tres de cuatro compañeros mejoraron su trabajo tras tu comentario. ¿Qué conclusión es válida? A. Tu comentario ayudó a tres de esos cuatro compañeros B. Tus comentarios ayudan a todos los estudiantes.", "A", "Solo se habla de las personas consultadas."),
    ],
    ex("En tu curso, tú pones 3 en lenguaje visual y tu compañero pone 1. Al mirar el trabajo ves que los elementos están sin orden y no se distingue la figura principal. ¿Qué nivel describe esa evidencia según la rúbrica de la clase 3 (nivel 1: elementos sin orden y figura principal que no se distingue; nivel 2: figura que se distingue y elementos ordenados; nivel 3: además, la composición dirige la vista)?", "Nivel 1", "El descriptor 1 habla de elementos sin orden y figura no distinguible."),
    [
        ex("¿Qué haces cuando tu autoevaluación y la coevaluación no coinciden?", "Comparo las evidencias y releo los descriptores", "Así se resuelve la discrepancia."),
        ex("Verdadero o falso: si mejoran tres compañeros, mi comentario ayuda a todos.", "Falso", "Tres personas no representan a todos."),
        ex("¿Con qué rúbrica reevalúas después del cambio?", "Con la misma rúbrica", "Así se puede comparar antes y después."),
    ],
    task(
        "Usa tu evaluación de la clase anterior. Si no la tienes, usa este caso de ejemplo: un estampado de seis hojas iguales en fila, con la intención de mostrar crecimiento; tu autoevaluación fue 3 en propósito y la de un compañero fue 1. Compara las evidencias, decide qué sugerencia aceptas, haz el cambio (un boceto basta), reevalúa con la misma rúbrica y escribe una conclusión que diga hasta dónde llegan tus datos.",
        "Evidencias: yo vi hojas en fila; mi compañero vio hojas iguales sin crecimiento. Descriptor 1: no se entiende qué comunica. Acepto la sugerencia de agrandar cada hoja. Boceto: seis hojas de tamaño creciente. Reevaluación: propósito 3. Antes 4 puntos, después 6. Conclusión: el cambio funcionó según una persona consultada.",
        ["compara las evidencias de las dos evaluaciones", "decide qué sugerencia acepta con una razón", "reevalúa con la misma rúbrica", "escribe una conclusión honesta"],
        ["comparación de evidencias", "boceto del cambio", "reevaluación", "conclusión"],
        ["cambiar la nota para igualar", "concluir para más gente de la consultada"],
        "Pregunta qué evidencia explicó la discrepancia y qué dato prueba que el cambio funcionó.",
    ),
    "Cuéntale a una persona de tu casa cómo cambió tu opinión sobre un trabajo después de ver la evidencia de otra persona.",
    "Escribe una conclusión de tres frases sobre un cambio que hiciste, incluyendo hasta dónde llegan tus datos.",
)
