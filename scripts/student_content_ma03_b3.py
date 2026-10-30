"""Student material for 3.º básico Matemática, OA 14 (localización en mapas y cuadrículas) y OA 15 (redes 2D y cuerpos 3D)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA14, OA15 = "MA03 OA 14", "MA03 OA 15"

CONV = "En una cuadrícula las columnas llevan letras (A, B, C…) de izquierda a derecha y las filas llevan números (1, 2, 3…) de arriba hacia abajo. Un lugar se escribe con la columna y luego la fila, como B3."
PARK = "Mapa del parque: columnas A a E (de izquierda a derecha) y filas 1 a 4 (de arriba hacia abajo). Portón: A1. Árbol: E1. Fuente: C2. Columpio: B3. Resbalín: D3. Banca: A4."
STEP = "Un paso mueve un casillero. Derecha va hacia la letra siguiente, izquierda hacia la letra anterior, abajo hacia el número siguiente y arriba hacia el número anterior, mirando el mapa en la hoja."
LAKE = "Mapa de columnas A a E y filas 1 a 3. El lago ocupa los casilleros B2 y C2: no se puede pasar por ellos."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 14
register(
    OA14, 1,
    materials=f"Lápiz y papel. Si quieres, dibuja una cuadrícula en una hoja cuadriculada. {CONV}",
    use="Aprenderé a nombrar las filas y las columnas de una cuadrícula. Sirve para decir exactamente dónde está algo en un mapa.",
    prior=["Sé la diferencia entre izquierda y derecha, arriba y abajo.", "Sé contar hasta 10."],
    explain=[
        "Una cuadrícula es un dibujo hecho de casilleros ordenados en líneas. Las líneas verticales, que van de arriba hacia abajo, son las columnas. Las líneas horizontales, que van de izquierda a derecha, son las filas.",
        "Para poder nombrar cada casillero, ponemos letras a las columnas y números a las filas. " + CONV + " Así, B3 es el casillero de la columna B y la fila 3.",
        "Escribe siempre primero la letra y después el número. Si cambias el orden, la otra persona puede confundirse. Un casillero queda bien nombrado cuando tiene su columna y su fila.",
    ],
    vocab=[("cuadrícula", "dibujo formado por casilleros en filas y columnas"), ("columna", "línea de casilleros de arriba hacia abajo, con una letra"), ("fila", "línea de casilleros de izquierda a derecha, con un número"), ("casillero", "cada cuadradito de la cuadrícula"), ("coordenada", "nombre de un casillero, como B3")],
    worked=[
        {"title": "Nombrar un casillero", "problem": "Hay una flor en la columna B y en la fila 2 de una cuadrícula. ¿Cómo se escribe su lugar?", "steps": ["Primero va la columna: B.", "Después va la fila: 2.", "El lugar es B2."], "answer": "B2"},
        {"title": "Leer un casillero", "problem": "En la cuadrícula, el gato está en D1. ¿En qué columna y en qué fila está?", "steps": ["La letra D es la columna.", "El número 1 es la fila.", "Entonces está en la columna D y en la fila 1."], "answer": "Columna D, fila 1"},
    ],
    mistakes=[
        {"wrong": "Escribir 2B para la columna B y la fila 2.", "why": "Se cambia el orden de las coordenadas.", "fix": "Escribe primero la letra de la columna y luego el número de la fila: B2."},
        {"wrong": "Decir que B3 y C3 están en la misma columna.", "why": "Se confunden columna y fila.", "fix": "Tienen la misma fila 3 y distinta columna: B y C."},
    ],
    tiers={
        "recovery": [
            ex("Una cuadrícula tiene las columnas A, B, C y D de izquierda a derecha. ¿Cuál columna queda más a la derecha?", "D", "La última letra está más a la derecha."),
            ex("Una cuadrícula tiene las filas 1, 2 y 3 de arriba hacia abajo. ¿Cuál fila queda más abajo?", "3", "Las filas se numeran hacia abajo."),
            ex("Un pez está en la columna C y en la fila 3. ¿Cómo se escribe su lugar?", "C3", "Se escribe primero la columna y luego la fila."),
        ],
        "understand": [
            ex("¿Una fila es una línea vertical o una línea horizontal?", "Horizontal", "Las filas van de izquierda a derecha."),
            ex("¿Una columna es una línea vertical o una línea horizontal?", "Vertical", "Las columnas van de arriba hacia abajo."),
            ex("En el lugar C3, ¿cuál es la columna y cuál es la fila?", "La columna es C y la fila es 3", "La letra nombra la columna y el número nombra la fila."),
        ],
        "apply": [
            ex("En una cuadrícula con columnas A a D y filas 1 a 3, una lupa está en C2. ¿En qué columna y en qué fila está?", "Columna C, fila 2", "La letra C es la columna y el 2 es la fila."),
            ex("En la columna A hay un perro en la fila 1, un gato en la fila 2 y un pez en la fila 3. ¿Qué animal está en A2?", "El gato", "A2 es la columna A, fila 2."),
            ex("El sol está en D3 y el árbol está en A1. ¿Cuál de los dos está más arriba?", "El árbol", "La fila 1 está más arriba que la fila 3."),
        ],
        "reason": [
            ex("Mía escribe 3C y Leo escribe C3 para la columna C y la fila 3. En este cuaderno, ¿quién lo escribe bien?", "Leo", "Primero va la letra de la columna y luego el número de la fila."),
            ex("Toño dice que A2 y A4 están en la misma fila. ¿Es cierto?", "No; están en la misma columna A y en filas distintas", "Las dos tienen la letra A y números distintos."),
        ],
        "challenge": [
            arith("Una cuadrícula tiene 4 columnas y 3 filas. ¿Cuántos casilleros tiene en total?", "4*3", "Hay 3 filas con 4 casilleros cada una.", " casilleros"),
            ex("Una cuadrícula tiene columnas A a D y filas 1 a 3. Un objeto está en la última fila y en la primera columna. ¿Cuál es su lugar?", "A3", "La última fila es la 3 y la primera columna es la A."),
        ],
    },
    context=[ex("En un estacionamiento con columnas A, B y C y filas 1 y 2, el auto rojo está en B2. ¿En qué fila está?", "En la fila 2", "El número de B2 es la fila.")],
    selfcheck=[
        ex("¿Cómo se llama la línea de casilleros que va de arriba hacia abajo?", "Columna", "Las columnas son verticales."),
        ex("Un lugar está en la columna D y en la fila 2. ¿Cómo se escribe?", "D2", "Primero la letra y luego el número."),
        ex("Una cuadrícula tiene las columnas A, B y C. ¿Cuántas columnas tiene?", "3", "Hay una columna por cada letra."),
    ],
    open_task=task(
        "Dibuja una cuadrícula de 4 columnas (A a D) y 3 filas (1 a 3). Dibuja una casa en B1, un árbol en D2 y un perro en A3. Escribe una frase por cada cosa que diga dónde está, usando columna y fila, y una pregunta que otra persona pueda responder.",
        "La casa está en B1: columna B, fila 1. El árbol está en D2: columna D, fila 2. El perro está en A3: columna A, fila 3. Pregunta: ¿Qué hay en la columna D?",
        ["cuadrícula con letras y números", "objetos en los lugares indicados", "frases con columna y fila", "pregunta que se puede responder"],
        ["cuadrícula dibujada", "frases escritas"],
        ["escribir primero la fila", "confundir fila y columna"],
        "Pide que pase el dedo por la columna y por la fila para ubicar el objeto. Reconoce el orden letra y luego número.",
    ),
    reinforce="Dibuja una cuadrícula de 3 columnas y 3 filas y escribe el nombre de los nueve casilleros.",
    extend="Dibuja una cuadrícula de 5 columnas (A a E) y 4 filas. ¿Cuántos casilleros tiene? Escribe la fila 4 completa.",
)

register(
    OA14, 2,
    materials=f"Lápiz y papel. {PARK}",
    use="Aprenderé a ubicar objetos de un mapa usando coordenadas. Sirve para decir con exactitud dónde está algo y encontrarlo.",
    prior=["Sé nombrar las filas y las columnas de una cuadrícula.", "Sé que una coordenada se escribe con letra y número."],
    explain=[
        CONV + " Esa forma de nombrar casilleros se llama coordenadas. Cada coordenada señala un solo lugar.",
        "Para encontrar un objeto, busca su letra y mira hacia abajo en esa columna. Luego busca su número y mira hacia la derecha en esa fila. El objeto está donde las dos líneas se cruzan. Por ejemplo, la fuente en C2 está donde la columna C y la fila 2 se cruzan.",
        "También puedes leer al revés: dado un casillero, dices qué hay en él. Si preguntan qué hay en B3, buscas la columna B, bajas hasta la fila 3 y lees: columpio.",
    ],
    vocab=[("coordenada", "letra y número que nombran un casillero"), ("mapa", "dibujo de un lugar visto desde arriba"), ("cruce", "punto donde se juntan una columna y una fila"), ("misma fila", "casilleros con el mismo número"), ("misma columna", "casilleros con la misma letra")],
    worked=[
        {"title": "Encontrar el lugar de un objeto", "problem": f"{PARK} ¿Cuál es el lugar del columpio?", "steps": ["Busco el columpio en el mapa: está en la columna B.", "Está en la fila 3.", "Escribo primero la letra y luego el número."], "answer": "B3"},
        {"title": "Decir qué hay en un lugar", "problem": f"{PARK} ¿Qué hay en D3?", "steps": ["Busco la columna D.", "Bajo hasta la fila 3.", "En ese casillero está el resbalín."], "answer": "El resbalín"},
    ],
    mistakes=[
        {"wrong": "Escribir 3B para el columpio.", "why": "Se pone la fila antes de la columna.", "fix": "Primero la letra de la columna: B3."},
        {"wrong": "Decir que el árbol (E1) y el portón (A1) no están en la misma fila porque están lejos.", "why": "Se confunde estar en la misma fila con estar juntos.", "fix": "Los dos están en la fila 1, aunque estén en columnas distintas."},
    ],
    tiers={
        "recovery": [
            ex(f"{PARK} ¿Qué hay en E1?", "El árbol", "E1 es la columna E, fila 1."),
            ex(f"{PARK} ¿Cuál es el lugar de la fuente?", "C2", "Está en la columna C y en la fila 2."),
            ex(f"{PARK} ¿Qué hay en A4?", "La banca", "A4 es la columna A, fila 4."),
        ],
        "understand": [
            ex("¿Qué dos datos necesita una coordenada como B3?", "La columna y la fila", "La letra es la columna y el número es la fila."),
            ex(f"{PARK} ¿Qué objeto está en la misma fila que el columpio?", "El resbalín", "Los dos están en la fila 3."),
            ex(f"{PARK} ¿Qué objeto está en la misma columna que la banca?", "El portón", "Los dos están en la columna A."),
        ],
        "apply": [
            ex(f"{PARK} ¿Qué objeto está en la columna C?", "La fuente", "Solo la fuente (C2) está en la columna C."),
            ex(f"{PARK} Se agrega un quiosco en la fila de la banca, dos columnas a la derecha de ella. ¿Qué coordenada tiene?", "C4", "La banca está en A4; dos columnas a la derecha es C."),
            ex(f"{PARK} ¿Qué objetos están en las filas 3 y 4?", "El columpio, el resbalín y la banca", "Fila 3: B3 y D3; fila 4: A4."),
        ],
        "reason": [
            ex("Ema dice que el resbalín está en 3D. ¿Qué error comete y cuál es la coordenada correcta?", "Pone la fila antes que la columna; es D3", "Primero se escribe la letra de la columna."),
            ex(f"{PARK} Ana dice que el columpio y el resbalín están en la misma columna. ¿Es cierto?", "No; están en la misma fila 3 y en columnas distintas", "El columpio es B3 y el resbalín es D3."),
        ],
        "challenge": [
            ex(f"{PARK} Un niño parte de la banca y sube en la misma columna hasta la fila 1. ¿A qué objeto llega?", "Al portón", "Sube por la columna A hasta A1."),
            ex(f"{PARK} ¿Qué objeto está una columna a la derecha de la fuente y una fila más abajo?", "El resbalín", "La fuente está en C2; una columna a la derecha y una fila abajo es D3."),
        ],
    },
    context=[ex("En un cine, una entrada dice D2: columna D y fila 2. ¿Cuál es la letra y cuál es el número de ese asiento?", "La letra es D y el número es 2", "La letra nombra la columna y el número nombra la fila.")],
    selfcheck=[
        ex(f"{PARK} ¿Qué hay en A1?", "El portón", "A1 es la columna A, fila 1."),
        ex(f"{PARK} ¿Cuál es el lugar de la banca?", "A4", "Está en la columna A y en la fila 4."),
        ex("En una coordenada, ¿qué se escribe primero: la columna o la fila?", "La columna", "Primero va la letra."),
    ],
    open_task=task(
        "Con el mapa del parque (portón A1, árbol E1, fuente C2, columpio B3, resbalín D3, banca A4), escribe las coordenadas de cuatro objetos y haz dos preguntas que se respondan con coordenadas. Luego escribe un objeto nuevo, con su coordenada, que no esté todavía en el mapa.",
        "Fuente: C2. Columpio: B3. Banca: A4. Árbol: E1. Pregunta 1: ¿Qué hay en D3? Pregunta 2: ¿Qué hay en la fila 1? Objeto nuevo: quiosco en E4.",
        ["escribe cuatro coordenadas correctas", "hace dos preguntas respondibles", "ubica un objeto nuevo en un casillero libre"],
        ["coordenadas escritas", "preguntas", "objeto nuevo"],
        ["escribir primero la fila", "usar un casillero ocupado"],
        "Pide que muestre con el dedo la columna y la fila. Reconoce el orden letra y número.",
    ),
    reinforce="Dibuja el mapa del parque en una hoja y marca los seis objetos. Dile a otra persona una coordenada y pide que diga qué hay.",
    extend="Con el mapa del parque, escribe las coordenadas de todos los casilleros de la fila 2 y de todos los de la columna C.",
)

register(
    OA14, 3,
    materials=f"Lápiz y papel. {STEP}",
    use="Aprenderé a describir un recorrido con pasos que no se presten a confusión. Sirve para dar indicaciones que otra persona entienda siempre igual.",
    prior=["Sé ubicar objetos con coordenadas.", "Sé contar pasos."],
    explain=[
        STEP + " Con estas palabras fijas podemos describir un recorrido en un mapa.",
        "Un recorrido sin ambigüedad dice dónde parte y cuántos pasos hay en cada dirección. Por ejemplo: «Parte en A1, 2 pasos a la derecha y 3 pasos hacia abajo». Eso lleva a C4: la letra pasa de A a C y el número de 1 a 4.",
        "Evita indicaciones como «allá», «a mi derecha» o «gira a tu izquierda». Dependen de hacia dónde mira cada persona. En un mapa usamos derecha, izquierda, arriba y abajo según la hoja. Así, todos llegan al mismo lugar.",
    ],
    vocab=[("recorrido", "camino hecho con varios pasos"), ("paso", "movimiento de un casillero"), ("dirección", "hacia dónde se mueve: derecha, izquierda, arriba o abajo"), ("punto de partida", "casillero donde empieza el recorrido"), ("ambiguo", "que se puede entender de más de una manera")],
    worked=[
        {"title": "Seguir un recorrido", "problem": f"{STEP} Parte en A1 y da 2 pasos a la derecha y 3 pasos hacia abajo. ¿Dónde llegas?", "steps": ["Parto en A1.", "Dos pasos a la derecha: A→B→C. Estoy en C1.", "Tres pasos hacia abajo: 1→2→3→4. Llego a C4."], "answer": "C4"},
        {"title": "Describir un recorrido", "problem": "Parte en D4 y debe llegar a B2. ¿Cómo se describe?", "steps": ["De la columna D a la B hay 2 pasos hacia la izquierda.", "De la fila 4 a la 2 hay 2 pasos hacia arriba.", "Digo desde dónde parto y cuántos pasos doy en cada dirección."], "answer": "Desde D4, 2 pasos a la izquierda y 2 pasos hacia arriba"},
    ],
    mistakes=[
        {"wrong": "Decir «gira a tu izquierda y avanza» sin decir hacia dónde se mira.", "why": "La indicación depende de hacia dónde mira quien escucha.", "fix": "Di «2 pasos a la izquierda en el mapa», con direcciones de la hoja."},
        {"wrong": "No decir el punto de partida del recorrido.", "why": "Sin partida no se sabe dónde termina.", "fix": "Comienza diciendo «parte en B2…»."},
    ],
    tiers={
        "recovery": [
            ex(f"{STEP} Partes de B2 y das 1 paso a la derecha. ¿Dónde llegas?", "C2", "Derecha cambia la letra a la siguiente."),
            ex(f"{STEP} Partes de C3 y das 2 pasos hacia arriba. ¿Dónde llegas?", "C1", "Arriba baja el número 3 a 1."),
            ex(f"{STEP} Partes de D4 y das 1 paso a la izquierda. ¿Dónde llegas?", "C4", "Izquierda cambia la letra D a C."),
        ],
        "understand": [
            ex("Un recorrido sin ambigüedad, ¿usa «allá» y «a mi derecha» o pasos con direcciones del mapa?", "Pasos con direcciones del mapa", "Las direcciones de la hoja se entienden igual para todos."),
            ex("¿Por qué «a mi derecha» puede causar confusión?", "Porque depende de hacia dónde mira quien habla", "Dos personas que miran distinto cambian lo que es la derecha."),
            ex("En un recorrido, ¿qué hay que decir primero?", "El lugar de partida", "Sin partida no se sabe dónde termina."),
        ],
        "apply": [
            ex(f"{STEP} Partes de B1, das 3 pasos a la derecha y 2 pasos hacia abajo. ¿Dónde llegas?", "E3", "De B a E son 3 pasos; de 1 a 3 son 2."),
            ex(f"{STEP} Partes en C4 y llegas a A1. Describe el recorrido con direcciones.", "2 pasos a la izquierda y 3 pasos hacia arriba", "De C a A son 2 columnas; de 4 a 1 son 3 filas."),
            ex(f"{STEP} Partes en B1, das 1 paso a la derecha, 2 hacia abajo y 1 a la izquierda. ¿Dónde terminas?", "B3", "B1 → C1 → C3 → B3."),
        ],
        "reason": [
            ex("Una persona dice «avanza dos pasos y gira a tu izquierda». ¿Qué problema tiene esta indicación en un mapa?", "No dice desde dónde parte ni hacia dónde mira; depende de quien la lee", "Las direcciones deben ser fijas, según la hoja."),
            ex("Dos niñas parten de A2 y llegan a C2. Una dice «2 pasos a la derecha» y la otra «3 pasos a la derecha». ¿Quién tiene razón?", "La que dice 2 pasos", "De A a C hay 2 pasos."),
        ],
        "challenge": [
            ex(f"{STEP} Partes en A4, das 3 pasos a la derecha y 3 pasos hacia arriba. ¿Dónde llegas?", "D1", "De A a D son 3 pasos y de 4 a 1 son 3."),
            arith("Para ir de A1 a D4 solo con pasos a la derecha o hacia abajo, ¿cuál es el menor número de pasos?", "3+3", "Hay 3 columnas y 3 filas de diferencia.", " pasos"),
        ],
    },
    context=[ex("En el mapa de una escuela (columnas A a D, filas 1 a 4), el patio está en B2 y la biblioteca en D2. Para ir del patio a la biblioteca, ¿cuántos pasos a la derecha das?", "2 pasos", "De la columna B a la D hay 2 columnas.")],
    selfcheck=[
        ex(f"{STEP} Partes en A2 y das 1 paso hacia abajo. ¿Dónde llegas?", "A3", "Abajo sube el número de 2 a 3."),
        ex(f"{STEP} Partes en C3 y das 2 pasos a la izquierda. ¿Dónde llegas?", "A3", "De C a A son 2 columnas."),
        ex("¿Un recorrido necesita decir dónde parte?", "Sí", "Sin el punto de partida no se sabe dónde llegar."),
    ],
    open_task=task(
        "En una cuadrícula de 4 columnas (A a D) y 4 filas (1 a 4), la entrada está en A1 y el tesoro en D3. Escribe un recorrido de la entrada al tesoro, usando solo pasos a la derecha y hacia abajo. Luego pide a otra persona que lo siga con el dedo y anota si llegó.",
        "Parte en A1. 3 pasos a la derecha (llego a D1) y 2 pasos hacia abajo (llego a D3). Otra persona lo siguió con el dedo y llegó al tesoro.",
        ["indica el punto de partida", "cuenta los pasos en cada dirección", "usa solo direcciones del mapa", "el recorrido lleva a D3"],
        ["recorrido escrito", "comprobación con otra persona"],
        ["usar «a tu izquierda»", "no decir la partida", "contar mal los pasos"],
        "Pide que lea su recorrido en voz alta y lo siga con el dedo. Reconoce que use direcciones del mapa.",
    ),
    reinforce="Dibuja una cuadrícula de 4 por 4 y marca tres recorridos distintos entre A1 y C3. Escribe los pasos.",
    extend="Escribe un recorrido de A4 a D1 y otro de D1 a A4. ¿Qué cambia en las direcciones?",
)

register(
    OA14, 4,
    materials=f"Lápiz y papel. {STEP}",
    use="Aprenderé a comparar rutas y a usar puntos de referencia. Sirve para elegir un camino claro y para decir dónde estás.",
    prior=["Sé describir recorridos con pasos y direcciones.", "Sé leer coordenadas."],
    explain=[
        "Entre dos lugares puede haber varias rutas. Una ruta es corta si tiene pocos pasos. Dos rutas distintas pueden tener la misma cantidad de pasos. Por ejemplo, de A1 a C3 puedes ir «2 a la derecha y 2 hacia abajo» o «2 hacia abajo y 2 a la derecha»: las dos tienen 4 pasos.",
        "A veces hay lugares donde no se puede pasar, como un lago. La ruta debe esquivarlo. Para revisar una ruta, sigue cada paso con el dedo y mira si pasas por un casillero prohibido.",
        "Un punto de referencia es un lugar conocido y fijo. Sirve para ubicar otros lugares: «desde la fuente (C2), 1 paso a la derecha» lleva a D2. Es mejor que decir «cerca de la fuente», porque da un lugar exacto.",
    ],
    vocab=[("ruta", "camino de un lugar a otro"), ("punto de referencia", "lugar conocido que ayuda a ubicar otro"), ("ruta más corta", "la que tiene menos pasos"), ("obstáculo", "lugar por el que no se puede pasar"), ("esquivar", "evitar pasar por un lugar")],
    worked=[
        {"title": "Comparar dos rutas", "problem": "Ruta X: 3 pasos a la derecha y 1 paso hacia abajo. Ruta Y: 1 paso hacia abajo y 3 pasos a la derecha. ¿Cuántos pasos tiene cada una?", "steps": ["Ruta X: 3 + 1 = 4 pasos.", "Ruta Y: 1 + 3 = 4 pasos.", "Tienen los mismos pasos, aunque cambie el orden."], "answer": "Las dos tienen 4 pasos"},
        {"title": "Esquivar un lago", "problem": f"{LAKE} Parte de A2: 1 paso hacia arriba, 4 pasos a la derecha y 1 paso hacia abajo. ¿Llegas a E2 sin pasar por el lago?", "steps": ["A2 → A1 con 1 paso hacia arriba.", "A1 → E1 con 4 pasos a la derecha (por la fila 1).", "E1 → E2 con 1 paso hacia abajo.", "Ninguno de los casilleros usados es B2 ni C2."], "answer": "Sí, llegas a E2"},
    ],
    mistakes=[
        {"wrong": "Cruzar por el lago porque «es más corto».", "why": "Se olvida que un obstáculo no se puede pasar.", "fix": "Elige una ruta que lo esquive, aunque tenga más pasos."},
        {"wrong": "Decir «ve cerca de la biblioteca».", "why": "Es una indicación poco exacta.", "fix": "Di «desde la biblioteca (D3), 1 paso hacia arriba»."},
    ],
    tiers={
        "recovery": [
            ex("Ruta P: 2 pasos a la derecha y 3 pasos hacia abajo. Ruta Q: 3 pasos hacia abajo y 2 pasos a la derecha. ¿Cuántos pasos tiene cada una?", "5 pasos cada una", "2 + 3 = 5 y 3 + 2 = 5."),
            ex(f"{STEP} La escuela está en B3. Desde la escuela das 2 pasos a la derecha. ¿Dónde llegas?", "D3", "De B a D hay 2 pasos."),
            ex("En Matemática: ¿Qué es un punto de referencia?", "Un lugar conocido que ayuda a ubicar otro", "Se usa para dar indicaciones exactas."),
        ],
        "understand": [
            ex("¿Por qué sirve decir «desde la fuente (C2)» en vez de «cerca de la fuente»?", "Porque da un lugar exacto", "Las coordenadas no dejan dudas."),
            ex("Dos rutas distintas de A1 a C3, ¿pueden tener la misma cantidad de pasos?", "Sí", "Por ejemplo, 2 a la derecha y 2 abajo, o 2 abajo y 2 a la derecha."),
            ex(f"{LAKE} ¿Puedes pasar por B2?", "No", "B2 es parte del lago."),
        ],
        "apply": [
            ex(f"{LAKE} Parte de A2: 1 paso hacia abajo, 4 pasos a la derecha y 1 paso hacia arriba. ¿Llegas a E2 sin pasar por el lago?", "Sí, llegas a E2", "La ruta pasa por A3, B3, C3, D3 y E3, que no son del lago."),
            ex(f"{LAKE} Parte de A2 y da 4 pasos a la derecha. ¿Es una ruta válida?", "No; pasa por B2 y C2", "Esos casilleros son parte del lago."),
            arith("Una ruta tiene 1 paso hacia arriba, 4 a la derecha y 1 hacia abajo. ¿Cuántos pasos tiene en total?", "1+4+1", "Se suman los pasos de cada tramo.", " pasos"),
        ],
        "reason": [
            ex(f"{LAKE} Ana y Beto parten de A2 hacia E2. Ana va 1 arriba, 4 a la derecha y 1 abajo. Beto va 1 abajo, 4 a la derecha y 1 arriba. ¿Cuál ruta es más corta?", "Ninguna; las dos tienen 6 pasos", "Cada ruta tiene 1 + 4 + 1 = 6 pasos."),
            ex("Carlos dice «ve cerca de la biblioteca». ¿Qué le falta a su indicación?", "Un lugar exacto, como una coordenada", "«Cerca» no dice con precisión dónde ir."),
        ],
        "challenge": [
            arith("Con el lago de B2 y C2, ¿cuál es el menor número de pasos para ir de A2 a E2?", "1+4+1", "Hay que dar la vuelta por arriba o por abajo, con 1 + 4 + 1 pasos.", " pasos"),
            ex(f"{STEP} El puente está en D3. Desde el puente das 2 pasos hacia arriba y 1 paso a la izquierda. ¿Dónde llegas?", "C1", "D3 → D1 con 2 arriba → C1 con 1 a la izquierda."),
        ],
    },
    context=[ex("En el mapa del colegio, la entrada está en B1 y la biblioteca en D4. Para ir de la entrada a la biblioteca solo con pasos a la derecha y hacia abajo, ¿cuántos pasos das a la derecha y cuántos hacia abajo?", "2 a la derecha y 3 hacia abajo", "De B a D son 2 columnas y de 1 a 4 son 3 filas.")],
    selfcheck=[
        ex("Si en una ruta no puedes pasar por un lago, ¿qué haces?", "Esquivarlo con otra ruta", "Se elige otro camino aunque tenga más pasos."),
        ex(f"{STEP} Desde un punto de referencia en B2 das 1 paso hacia abajo. ¿Dónde llegas?", "B3", "El número sube de 2 a 3."),
        ex("Una ruta tiene 2 pasos a la derecha y 3 hacia abajo. ¿Cuántos pasos tiene en total?", "5 pasos", "2 + 3 = 5.", calc="2+3"),
    ],
    open_task=task(
        f"Usa este mapa: {LAKE} Parte de A2 y debes llegar a E2. Escribe dos rutas distintas que esquiven el lago, cuenta los pasos de cada una y di cuál es más corta o si son iguales. Menciona un punto de referencia para explicar una de ellas.",
        "Ruta 1: 1 paso arriba, 4 a la derecha, 1 abajo (6 pasos). Ruta 2: 1 paso abajo, 4 a la derecha, 1 arriba (6 pasos). Son igual de cortas. Punto de referencia: desde A1 voy 4 pasos a la derecha hasta E1.",
        ["dos rutas válidas", "ninguna pasa por el lago", "cuenta los pasos", "usa un punto de referencia"],
        ["rutas escritas", "pasos contados"],
        ["pasar por el lago", "contar mal los pasos"],
        "Pide que siga cada ruta con el dedo y revise si toca el lago. Reconoce el punto de referencia bien usado.",
    ),
    reinforce="Dibuja un mapa de 5 por 4 con un obstáculo y escribe una ruta que lo esquive.",
    extend="En el mapa del lago, escribe todas las rutas de 6 pasos que van de A2 a E2. ¿Cuántas hay?",
)

# ================================================================ OA 15
SAFE = "Usa solo envases de cartón vacíos y limpios, sin bordes que corten, y pide ayuda a una persona adulta para abrirlos o cortar."

register(
    OA15, 1,
    materials=f"Una caja de cartón vacía (por ejemplo, de cereal o de zapatos), lápiz y regla. {SAFE} Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé qué pasa con las caras de un envase cuando lo despliego. Sirve para entender cómo se fabrican las cajas y los envases.",
    prior=["Reconozco rectángulos, cuadrados y círculos.", "Sé que una cara es una superficie del cuerpo."],
    explain=[
        "Los cuerpos geométricos, como una caja o una lata, son figuras 3D. Si despegas con cuidado las pestañas pegadas de una caja y la abres, queda una figura plana. Esa figura se llama red o plantilla. Desplegar es abrir un cuerpo hasta dejarlo plano.",
        "Una caja de zapatos es un paralelepípedo. Su red tiene 6 rectángulos, y las caras de enfrente son iguales entre sí. Un dado es un cubo y su red tiene 6 cuadrados iguales. Una lata es un cilindro y su red tiene 2 círculos y 1 rectángulo.",
        "Las caras de la red siguen unidas por algunos bordes. Al plegar por esos bordes vuelve a formarse el cuerpo. La red es como un «mapa plano» del cuerpo: muestra todas sus caras.",
    ],
    vocab=[("red (plantilla)", "figura plana que se pliega para formar un cuerpo"), ("desplegar", "abrir un cuerpo hasta dejarlo plano"), ("cara", "superficie de un cuerpo geométrico"), ("paralelepípedo", "cuerpo con 6 caras rectangulares, como una caja de zapatos"), ("cilindro", "cuerpo con dos círculos y una superficie curva, como una lata")],
    worked=[
        {"title": "Red de una caja", "problem": "Una caja de zapatos es un paralelepípedo. Al desplegarla, ¿cuántos rectángulos tiene su red?", "steps": ["La caja tiene 6 caras.", "Todas sus caras son rectángulos.", "La red tiene 6 rectángulos."], "answer": "6 rectángulos"},
        {"title": "Red de una lata", "problem": "Una lata cilíndrica se despliega. ¿Qué figuras forman su red?", "steps": ["La lata tiene una tapa y un fondo: 2 círculos.", "La parte que rodea es un rectángulo cuando se estira.", "Entonces: 2 círculos y 1 rectángulo."], "answer": "2 círculos y 1 rectángulo"},
    ],
    mistakes=[
        {"wrong": "Decir que la red de una lata tiene 3 círculos.", "why": "Se cuentan mal las caras planas.", "fix": "La lata tiene solo 2 círculos (tapa y fondo) y 1 rectángulo para el contorno."},
        {"wrong": "Pensar que un envase desplegado deja de tener 6 caras.", "why": "Se cree que desplegar cambia el número de caras.", "fix": "Desplegar solo las deja planas: el número de caras es el mismo."},
    ],
    tiers={
        "recovery": [
            ex("Una caja de zapatos tiene forma de paralelepípedo. Al desplegarla, ¿cuántos rectángulos tiene?", "6", "Un paralelepípedo tiene 6 caras rectangulares."),
            ex("Un dado con forma de cubo se despliega. ¿Cuántos cuadrados tiene su red?", "6", "Un cubo tiene 6 caras cuadradas."),
            ex("Una lata cilíndrica se despliega. ¿Cuántos círculos y cuántos rectángulos tiene su red?", "2 círculos y 1 rectángulo", "La tapa y el fondo son círculos; el contorno es un rectángulo."),
        ],
        "understand": [
            ex("¿Qué es una red (plantilla) de un cuerpo?", "Una figura plana que se pliega para formar el cuerpo", "Muestra todas las caras en el plano."),
            ex("Al desplegar un envase, ¿qué ocurre con sus caras?", "Quedan planas, unidas por algunos bordes", "Desplegar no las cambia, solo las deja planas."),
            ex("Se despliega una caja de zapatos. ¿Todas las caras de su red son rectángulos?", "Sí", "Un paralelepípedo tiene 6 caras rectangulares."),
        ],
        "apply": [
            arith("En la red de una caja de cereal (paralelepípedo) hay 6 rectángulos. Las caras que se enfrentan son iguales. ¿Cuántas parejas de caras iguales hay?", "6//2", "6 caras forman 3 parejas.", " parejas"),
            ex("Un cubo de 5 cm de arista se despliega. ¿Cuánto mide el lado de cada cuadrado de su red?", "5 cm", "Cada cara es un cuadrado del tamaño de la arista."),
            ex("Una lata tiene 2 círculos y 1 rectángulo en su red. ¿Tiene más círculos o más rectángulos?", "Más círculos", "Hay 2 círculos y 1 rectángulo."),
        ],
        "reason": [
            ex("Julia dice que al desplegar una lata salen 3 círculos. ¿Qué error comete?", "La lata tiene solo 2 círculos y 1 rectángulo", "La tapa y el fondo son los únicos círculos."),
            ex("Un envase desplegado muestra 6 cuadrados iguales. ¿Qué cuerpo era?", "Un cubo", "Un cubo tiene 6 caras cuadradas iguales."),
        ],
        "challenge": [
            ex("Un envase desplegado tiene 2 cuadrados y 4 rectángulos que no son cuadrados. ¿Cuántas caras tenía el envase y cuál es su forma?", "6 caras; era un paralelepípedo", "2 + 4 = 6 caras y todas son rectángulos, como una caja alargada.", calc="2+4"),
            arith("Una lata desplegada tiene 2 círculos y 1 rectángulo. ¿Cuántas figuras planas hay en total?", "2+1", "Se suman las figuras de la red.", " figuras"),
        ],
    },
    context=[arith("Quieres forrar una caja con 6 caras rectangulares y cubres cada cara con un solo trozo de papel. ¿Cuántos trozos necesitas?", "6", "Hay un trozo para cada cara.", " trozos")],
    selfcheck=[
        ex("¿Cuántos cuadrados tiene la red de un cubo?", "6", "El cubo tiene 6 caras cuadradas."),
        ex("¿Cuántos círculos tiene la red de un cilindro?", "2", "Tiene la tapa y el fondo."),
        ex("¿Qué cuerpo se forma al plegar una red?", "Un cuerpo geométrico, como una caja o una lata", "Plegar la red reconstruye el cuerpo."),
    ],
    open_task=task(
        f"Con ayuda de una persona adulta, elige una caja vacía de cartón que tenga forma de paralelepípedo. {SAFE} Desarma con cuidado la caja hasta dejarla plana. Cuenta cuántos rectángulos hay, mide con una regla dos de ellos y dibuja la red en tu cuaderno.",
        "Caja de cereal: 6 rectángulos. Medí dos: 20 cm por 7 cm y 20 cm por 30 cm. Dibujé la red con los 6 rectángulos unidos por algunos bordes. Las 6 caras formaban 3 parejas de caras iguales entre sí.",
        ["cuenta las caras", "mide al menos dos rectángulos", "dibuja la red con todas las caras", "dice cuáles caras son iguales"],
        ["red dibujada", "medidas", "conteo de caras"],
        ["dibujar menos de 6 caras", "creer que cambia el número de caras al desplegar"],
        "Pide que doble la red de papel para volver a armar la caja. Reconoce que cuente las caras.",
    ),
    reinforce="Mira una caja pequeña en tu casa y di cuántas caras tiene. Dibuja su red sin cortarla.",
    extend="Dibuja la red de una lata: dos círculos y un rectángulo. Explica con tus palabras cómo se une cada círculo al rectángulo.",
)

register(
    OA15, 2,
    materials="Lápiz y papel cuadriculado. Si quieres, 6 cuadrados de papel iguales y cinta. Todas las plantillas están descritas en cada ejercicio.",
    use="Aprenderé a reconocer qué conjuntos de cuadrados pueden plegarse para formar un cubo y cuáles no. Sirve para no equivocarme al diseñar una caja.",
    prior=["Sé que la red de un cubo está formada por cuadrados iguales.", "Sé contar hasta 10."],
    explain=[
        "No cualquier grupo de cuadrados unidos forma un cubo. La red de un cubo necesita exactamente 6 cuadrados iguales. Si hay 5, falta una cara; si hay 7, sobra una.",
        "Además, al plegarla ninguna cara debe quedar encima de otra y no deben quedar huecos. Por ejemplo, 4 cuadrados en una columna con un cuadrado a cada lado del segundo forman una cruz. La cruz sí se pliega y arma un cubo.",
        "En cambio, 6 cuadrados en una sola fila no sirven: al plegar, algunos cuadrados caen encima de otros. Tampoco sirven 2 filas de 3 cuadrados puestas una sobre otra. Para estar seguro, imagina que doblas la red paso a paso.",
    ],
    vocab=[("red de un cubo", "6 cuadrados iguales unidos que se pliegan para formar un cubo"), ("cruz", "red con 4 cuadrados en columna y uno a cada lado del segundo"), ("encimarse", "caer una cara sobre otra al plegar"), ("hueco", "lugar sin cara en el cuerpo armado"), ("plegar", "doblar por los bordes entre caras")],
    worked=[
        {"title": "Revisar la cantidad de cuadrados", "problem": "Una red tiene 5 cuadrados iguales unidos. ¿Puede formar un cubo?", "steps": ["Un cubo tiene 6 caras.", "La red tiene solo 5 cuadrados.", "Falta una cara y quedaría un hueco."], "answer": "No, porque falta 1 cuadrado"},
        {"title": "Revisar la red en cruz", "problem": "Una red tiene 4 cuadrados en una columna y un cuadrado a cada lado del segundo. ¿Forma un cubo?", "steps": ["Cuento los cuadrados: 4 + 1 + 1 = 6.", "Los 4 de la columna forman las caras de alrededor.", "Los cuadrados laterales son la tapa y el fondo.", "Al plegar no se encima ninguno."], "answer": "Sí, forma un cubo"},
    ],
    mistakes=[
        {"wrong": "Decir que cualquier grupo de 6 cuadrados forma un cubo.", "why": "Solo se cuenta la cantidad y no cómo están unidos.", "fix": "Imagina cómo se pliegan: 6 cuadrados en una fila quedan encimados."},
        {"wrong": "Dibujar una red de cubo con 7 cuadrados «por si acaso».", "why": "Se cree que más caras es mejor.", "fix": "Un cubo tiene exactamente 6 caras."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos cuadrados iguales necesita la red de un cubo?", "6", "Un cubo tiene 6 caras cuadradas."),
            ex("Una red tiene 5 cuadrados iguales unidos. ¿Puede formar un cubo?", "No; falta 1 cuadrado", "Un cubo necesita 6 caras."),
            ex("Una red tiene 7 cuadrados iguales unidos. ¿Puede formar un cubo?", "No; sobra 1 cuadrado", "Un cubo tiene solo 6 caras."),
        ],
        "understand": [
            ex("¿Qué significa que una red sea «posible» para un cubo?", "Que al plegarla se forma el cubo sin huecos ni caras encimadas", "Cada cara queda en un lugar distinto."),
            ex("¿Cuántos cuadrados tiene la red en cruz?", "6", "4 en columna más 1 a cada lado del segundo son 6.", calc="4+1+1"),
            ex("¿Deben ser iguales los cuadrados de la red de un cubo?", "Sí", "Todas las caras de un cubo son iguales."),
        ],
        "apply": [
            ex("Hay 6 cuadrados iguales puestos en una fila larga, uno al lado del otro. ¿Se pueden plegar para formar un cubo?", "No; algunos cuadrados caen encima de otros", "Al plegar la fila se encima."),
            ex("Hay 4 cuadrados iguales en una fila, uno arriba del segundo y uno abajo del tercero. ¿Se pueden plegar para formar un cubo?", "Sí", "Los 4 de la fila forman los lados; uno es la tapa y el otro, el fondo."),
            ex("Hay dos filas de 3 cuadrados iguales, una sobre la otra, formando un bloque de 2 por 3. ¿Forman un cubo al plegarlos?", "No", "Las caras de las puntas se encimarían."),
        ],
        "reason": [
            ex("Paula dice que cualquier grupo de 6 cuadrados unidos forma un cubo. ¿Cuál ejemplo muestra que está equivocada?", "6 cuadrados en una fila o un bloque de 2 por 3", "Esas redes no se pliegan en un cubo."),
            ex("Tomás tiene 4 cuadrados en fila, uno arriba del primero y uno abajo del último. ¿Forma un cubo?", "Sí", "Los 4 de la fila forman los lados; los otros son tapa y fondo."),
        ],
        "challenge": [
            ex("Una red tiene 7 cuadrados iguales unidos. ¿Cuántas caras tiene un cubo y cuántos cuadrados sobran?", "6 caras; sobra 1 cuadrado", "7 − 6 = 1.", calc="7-6"),
            ex("Una red de pirámide tiene 1 cuadrado y 4 triángulos. ¿Cuántas caras tiene la pirámide?", "5 caras", "1 + 4 = 5.", calc="1+4"),
        ],
    },
    context=[ex("Una amiga te muestra una red con 6 cuadrados iguales dispuestos en cruz. ¿Le dices que puede armar un cubo?", "Sí", "La red en cruz es una red posible de cubo.")],
    selfcheck=[
        ex("Para armar un dado, ¿cuántos cuadrados iguales tiene su plantilla?", "6", "Un dado tiene 6 caras cuadradas."),
        ex("¿Sirve como plantilla de cubo una fila de 6 cuadrados?", "No", "Al plegarla se encima."),
        ex("¿Alcanzan 5 cuadrados para cubrir un dado completo?", "No", "Falta una cara."),
    ],
    open_task=task(
        "Dibuja en papel cuadriculado dos plantillas: una cruz de 6 cuadrados de 2 cuadritos de lado, y una fila de 6 cuadrados del mismo tamaño. Corta con tijeras de punta redonda (con ayuda de una persona adulta) y trata de plegar cada una. Escribe cuál formó un cubo y por qué la otra no.",
        "La cruz formó un cubo: las 6 caras quedaron en lugares distintos. La fila de 6 no formó un cubo: los últimos cuadrados quedaron encimados con los primeros.",
        ["dibuja ambas plantillas con 6 cuadrados", "pliega y observa", "dice cuál forma el cubo", "explica la razón"],
        ["dibujos de las plantillas", "explicación"],
        ["decir que ambas sirven", "no contar los cuadrados"],
        "Pide que cuente 6 cuadrados y los pliegue paso a paso. Reconoce la explicación basada en lo observado.",
    ),
    reinforce="Con 6 cuadrados de papel, arma una cruz y plégala. Luego prueba con 6 cuadrados en fila y mira qué pasa.",
    extend="Dibuja otra plantilla de cubo distinta de la cruz: 4 cuadrados en fila, uno arriba del primero y uno abajo del último. Pliégala y comprueba.",
)

register(
    OA15, 3,
    materials=f"Una red de cubo dibujada en papel o cartulina (cruz de 6 cuadrados), regla, lápiz, cinta. {SAFE} Los datos de cada ejercicio están escritos.",
    use="Aprenderé a armar un cuerpo geométrico a partir de su red. Sirve para fabricar cajas y modelos.",
    prior=["Sé qué es una red (plantilla).", "Sé cuáles redes forman un cubo."],
    explain=[
        "Para construir un cuerpo desde una red, primero revisa que tenga la cantidad y la forma correctas de caras. Después marca las líneas por donde se dobla. Esas líneas son los bordes que se vuelven aristas del cuerpo.",
        "Pliega todas las caras hacia el mismo lado, hasta que sus bordes se junten. Une los bordes con cinta adhesiva o con pestañas pegadas. Una pestaña es una tira que se agrega a una cara para pegarla con la otra.",
        "Si al armar queda un hueco o una cara encimada, la red tenía un error. Revisa cuántas caras había y cómo estaban unidas. Un cubo armado tiene aristas iguales: el lado de cada cuadrado de la red es el mismo que la arista del cubo.",
    ],
    vocab=[("construir", "armar algo uniendo partes"), ("pestaña", "tira de papel que se pega para unir dos caras"), ("arista", "borde donde se juntan dos caras"), ("pliegue", "línea por donde se dobla la red"), ("cuerpo armado", "cuerpo que se forma al plegar y unir la red")],
    worked=[
        {"title": "Medida de la arista", "problem": "Una red de cubo tiene cuadrados de 4 cm de lado. ¿Cuánto mide cada arista del cubo armado?", "steps": ["Cada cuadrado es una cara del cubo.", "El lado de la cara es una arista.", "Entonces cada arista mide 4 cm."], "answer": "4 cm"},
        {"title": "Reconocer el cuerpo", "problem": "Una red tiene 2 círculos y 1 rectángulo. ¿Qué cuerpo se arma?", "steps": ["El rectángulo se enrolla y forma la parte curva.", "Los dos círculos son tapa y fondo.", "El cuerpo es un cilindro, como una lata."], "answer": "Un cilindro"},
    ],
    mistakes=[
        {"wrong": "Armar una red de 5 cuadrados y esperar que no tenga huecos.", "why": "Falta una cara.", "fix": "Cuenta las caras antes de armar: el cubo necesita 6."},
        {"wrong": "Doblar algunas caras hacia adentro y otras hacia afuera.", "why": "No se pliega todo hacia el mismo lado.", "fix": "Pliega todas las caras hacia el mismo lado."},
    ],
    tiers={
        "recovery": [
            ex("Una red de cubo tiene cuadrados de 7 cm de lado. ¿Cuánto mide cada arista del cubo armado?", "7 cm", "El lado del cuadrado es la arista del cubo."),
            ex("Para armar un cuerpo con su red, ¿plegas por las líneas entre las caras o cortas por ellas?", "Plegas por esas líneas", "Esos bordes son los que se vuelven aristas."),
            ex("¿Para qué sirven las pestañas de una plantilla?", "Para unir las caras con cinta o pegamento", "Una pestaña se pega a la cara vecina."),
        ],
        "understand": [
            ex("Al plegar una red de cubo, las líneas entre cuadrados, ¿se convierten en aristas?", "Sí", "Son los bordes donde se juntan dos caras."),
            ex("Un cubo ya armado descansa sobre la mesa. ¿Cuántas caras no tocan la mesa?", "5", "6 caras menos la que está apoyada.", calc="6-1"),
            ex("Si a una red de cubo le falta un cuadrado, ¿qué pasa al armarla?", "Queda un hueco", "Falta una cara."),
        ],
        "apply": [
            ex("Una red válida tiene 6 rectángulos unidos, de tres medidas distintas y con las caras que se enfrentan iguales. ¿Qué cuerpo se forma al armarla?", "Un paralelepípedo", "Es una caja de 6 caras rectangulares."),
            ex("Una red tiene 6 cuadrados iguales dispuestos en cruz. ¿Qué cuerpo se forma?", "Un cubo", "Los 6 cuadrados son las 6 caras del cubo."),
            ex("Una red tiene 1 cuadrado en el centro y 4 triángulos iguales unidos a sus lados. ¿Qué cuerpo se forma?", "Una pirámide de base cuadrada", "Los triángulos suben hasta juntarse en un punto."),
        ],
        "reason": [
            ex("Lía armó una red con 5 cuadrados iguales y quedó un hueco. ¿Por qué ocurrió?", "Porque falta 1 cuadrado; un cubo necesita 6", "5 cuadrados no cubren las 6 caras."),
            ex("Un cubo armado tiene aristas de 5 cm. ¿Cuánto debe medir el lado de los cuadrados de su red?", "5 cm", "La arista es el lado de una cara."),
        ],
        "challenge": [
            ex("Tienes una red de cubo con cuadrados de 4 cm y otra con cuadrados de 6 cm. ¿Cuál cubo armado es más grande?", "El de 6 cm", "Sus aristas son más largas."),
            ex("Armas una red en cruz con una cara de fondo en la mesa. ¿Cuántas caras son laterales (ni tapa ni fondo)?", "4", "Las 6 caras menos tapa y fondo.", calc="6-2"),
        ],
    },
    context=[ex("Una caja de regalo con forma de cubo debe medir 10 cm de arista. ¿Cuánto debe medir el lado de cada cuadrado de la red?", "10 cm", "El lado del cuadrado es la arista de la caja.")],
    selfcheck=[
        ex("¿Por dónde se pliega una red de cubo?", "Por las líneas entre los cuadrados", "Esas líneas se convierten en aristas."),
        ex("Si falta un cuadrado en la red de un cubo, ¿qué queda al armarla?", "Un hueco", "Falta una cara."),
        ex("¿Qué cuerpo se forma con un rectángulo enrollado y dos círculos?", "Un cilindro", "Los círculos son la tapa y el fondo."),
    ],
    open_task=task(
        f"Con ayuda de una persona adulta, dibuja en cartulina una red en cruz de 6 cuadrados de 4 cm de lado, agrega pestañas, corta con tijeras de punta redonda, pliega y arma el cubo con cinta. {SAFE} Luego escribe cuánto mide cada arista, cuántas caras tiene y qué hiciste para evitar huecos.",
        "Cada arista mide 4 cm. Tiene 6 caras. Conté los 6 cuadrados antes de cortar y doblé todo hacia el mismo lado. No quedaron huecos.",
        ["dibuja 6 cuadrados en cruz", "mide el lado con regla", "arma el cubo", "dice arista y número de caras"],
        ["cubo armado", "medidas", "descripción"],
        ["menos de 6 cuadrados", "doblar para lados distintos"],
        "Pide que cuente las caras antes de cortar. Reconoce que revise huecos al final.",
    ),
    reinforce="Con una cruz de 6 cuadrados de papel, arma un cubo. Cuenta sus caras con el dedo.",
    extend="Haz otra red de cubo con cuadrados de 6 cm y compara el tamaño de los dos cubos que armaste.",
)

register(
    OA15, 4,
    materials="Lápiz, regla y papel cuadriculado. Si quieres, tijeras de punta redonda con ayuda de una persona adulta. Todos los datos están en cada ejercicio.",
    use="Aprenderé a diseñar una plantilla y a justificar por qué sirve. Sirve para fabricar una caja propia y comprobar que se arma.",
    prior=["Sé cuáles redes forman un cubo.", "Sé armar un cuerpo desde su red."],
    explain=[
        "Diseñar una plantilla es decidir qué caras llevará y cómo estarán unidas. Primero decide el cuerpo, luego cuenta las caras que necesita. Un cubo necesita 6 cuadrados iguales. Una caja necesita 6 rectángulos.",
        "Después dibuja las caras unidas por sus bordes, sin dejar huecos ni caras encimadas. Revisa con la imaginación o con papel: ¿se pliega sin que una cara caiga sobre otra? También mide los lados: dos caras unidas deben tener un borde igual.",
        "Para justificar tu diseño, explica tres cosas. Cuántas caras hay, qué forma tienen y por qué no se encima ninguna al plegar. Una justificación clara convence a otra persona de que tu plantilla sirve.",
    ],
    vocab=[("diseñar", "planear y dibujar cómo será algo"), ("justificar", "dar razones de por qué algo está bien"), ("plantilla", "red que se usa para fabricar un cuerpo"), ("borde igual", "lado que mide lo mismo en dos caras unidas"), ("comprobar", "revisar que algo funciona")],
    worked=[
        {"title": "Elegir una plantilla", "problem": "¿Cuál plantilla sirve para un cubo: A) 6 cuadrados en una fila, o B) una cruz de 6 cuadrados?", "steps": ["Las dos tienen 6 cuadrados.", "La fila A se encima al plegarla.", "La cruz B no se encima."], "answer": "La B, la cruz"},
        {"title": "Medir una plantilla", "problem": "Una fila de la plantilla tiene 4 cuadrados de 3 cm de lado. ¿Cuánto mide la fila de largo?", "steps": ["Cada cuadrado mide 3 cm de largo.", "Hay 4 cuadrados juntos.", "4 × 3 = 12 cm."], "answer": "12 cm"},
    ],
    mistakes=[
        {"wrong": "Dibujar una plantilla de cubo con 6 cuadrados en una fila porque «tiene 6 caras».", "why": "Solo se cuenta la cantidad de caras.", "fix": "Revisa también cómo se pliega: la fila se encima. Usa una cruz."},
        {"wrong": "Justificar el diseño diciendo solamente «porque sí».", "why": "No se dan razones.", "fix": "Di cuántas caras hay, su forma y por qué no se encima ninguna."},
    ],
    tiers={
        "recovery": [
            arith("Diseñas una plantilla de cubo con cuadrados de 3 cm. ¿Cuántos cuadrados dibujas?", "6", "Un cubo tiene 6 caras.", " cuadrados"),
            arith("Una fila de la plantilla tiene 3 cuadrados de 4 cm de lado. ¿Cuánto mide la fila de largo?", "3*4", "Se suman 3 lados de 4 cm.", " cm"),
            ex("Para diseñar la red de una lata, ¿qué forma tiene la pieza que rodea?", "Un rectángulo", "Al enrollarse forma la parte curva."),
        ],
        "understand": [
            ex("Antes de cortar una plantilla, ¿qué debes revisar?", "Que tenga las caras necesarias y que no se encimen al plegar", "Así el cuerpo se arma sin huecos."),
            ex("¿Por qué conviene dibujar pestañas en una plantilla?", "Para poder pegar las caras entre sí", "Las pestañas unen las caras."),
            ex("Una plantilla de cubo tiene 6 cuadrados en una fila. ¿La aceptas?", "No", "Los cuadrados se encimarían al plegarla."),
        ],
        "apply": [
            ex("Elige la plantilla adecuada para un cubo: A) 2 filas de 3 cuadrados, o B) 4 cuadrados en una fila con uno arriba del segundo y uno abajo del tercero.", "B", "B se pliega sin encimar caras; A se encima."),
            ex("Una plantilla tiene 4 cuadrados en fila, uno arriba del primero y uno abajo del último. ¿Cuántas caras tendrá el cuerpo que arma?", "6 caras", "4 + 1 + 1 = 6 cuadrados.", calc="4+1+1"),
            arith("Una caja con tapa tiene 6 rectángulos. Si armas dos cajas iguales, ¿cuántos rectángulos necesitas?", "2*6", "Cada caja usa 6 rectángulos.", " rectángulos"),
        ],
        "reason": [
            ex("Una compañera dice que su plantilla de cubo es una cruz porque tiene 6 cuadrados. ¿Tiene razón?", "Sí; la cruz es una plantilla válida", "Se pliega sin encimar caras."),
            ex("Otro compañero dibuja 2 filas de 3 cuadrados y dice que sirve porque tiene 6. ¿Tiene razón?", "No; al plegar algunas caras se encimarían", "Tener 6 cuadrados no basta."),
        ],
        "challenge": [
            ex("Elige la plantilla válida para un cubo: A) 4 cuadrados en fila con 1 arriba del primero y 1 abajo del último; B) fila de 6; C) 2 filas de 3.", "A", "Es una de las redes que sí arman un cubo."),
            ex("La red de una pirámide tiene 1 cuadrado y 4 triángulos iguales. ¿Cuántas caras tiene la pirámide?", "5 caras", "1 + 4 = 5 caras.", calc="1+4"),
        ],
    },
    context=[arith("Quieres hacer un cubo de 5 cm de arista. Dibujas 4 cuadrados en fila. ¿Cuántos cm mide de largo esa fila?", "4*5", "Se suman 4 lados de 5 cm.", " cm")],
    selfcheck=[
        ex("¿Cuántas caras necesita la plantilla de un cubo?", "6", "Un cubo tiene 6 caras."),
        ex("¿La cruz de 6 cuadrados es una plantilla válida para un cubo?", "Sí", "Se pliega sin encimar caras."),
        ex("Una plantilla de cubo tiene 7 cuadrados. ¿Sirve?", "No; sobra 1", "Un cubo tiene 6 caras."),
    ],
    open_task=task(
        "Diseña una plantilla para una caja que tenga forma de cubo de 3 cm de arista. Dibújala en papel cuadriculado con cuadrados de 3 cm. Marca las pestañas, escribe cuántas caras tiene y justifica con tres razones por qué sirve. Si puedes, córtala con tijeras de punta redonda y arma el cubo con ayuda de una persona adulta.",
        "Mi plantilla es una cruz de 6 cuadrados de 3 cm. Tiene 6 caras. Sirve porque: tiene exactamente 6 cuadrados iguales, al plegar no se encima ninguna cara y todos los bordes que se unen miden 3 cm.",
        ["usa 6 cuadrados iguales de 3 cm", "la plantilla no se encima al plegar", "marca pestañas", "da al menos tres razones"],
        ["plantilla dibujada", "justificación", "cubo armado si se puede"],
        ["menos o más de 6 cuadrados", "justificar con «porque sí»"],
        "Pide que dé tres razones, una por una. Reconoce la comprobación plegando el papel.",
    ),
    reinforce="Dibuja dos plantillas distintas de cubo (una cruz y otra de 4 cuadrados en fila con uno arriba y uno abajo) y comprueba que ambas arman un cubo.",
    extend="Diseña una plantilla para un paralelepípedo con 4 caras de 2 por 4 cuadritos y 2 caras de 2 por 2 cuadritos. Dibuja los 6 rectángulos unidos y explica cuáles son iguales.",
)
