"""Student material for 4.º básico Matemática, OA 16 (vistas de cuerpos 3D) y OA 17 (simetría en figuras 2D)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA16, OA17 = "MA04 OA 16", "MA04 OA 17"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


CUERPOS = "Los cuerpos están apoyados sobre la mesa en una de sus caras planas (un cilindro «parado» y un cono se apoyan en su base)."

# ================================================================ OA 16
register(
    OA16, 1,
    materials=f"Lápiz y papel. Si quieres, objetos de tu casa con forma de caja, lata o pelota. {CUERPOS}",
    use="Aprenderé a decir qué figura se ve cuando miro un cuerpo de frente. Sirve para dibujar cosas y entender planos.",
    prior=["Conozco el cubo, el cilindro, el cono, la esfera y la pirámide.", "Conozco el cuadrado, el rectángulo, el triángulo y el círculo."],
    explain=[
        "Un cuerpo geométrico tiene tres dimensiones: alto, ancho y largo. Cuando lo miras desde un lugar, solo ves una figura plana. Esa figura se llama vista. La vista frontal es la que ves al mirar el cuerpo de frente.",
        "Por ejemplo, un cubo de frente se ve como un cuadrado. Un cilindro parado, más alto que ancho, se ve como un rectángulo. Un cono apoyado en su base se ve como un triángulo. Una esfera se ve como un círculo desde cualquier lado.",
        "Para imaginar la vista, piensa en la sombra del cuerpo sobre una pared que está detrás de él. Esa silueta es la vista frontal. Una misma figura plana puede ser la vista de cuerpos distintos, por eso a veces necesitamos mirar desde más de un lado.",
    ],
    vocab=[("vista", "figura plana que se ve al mirar un cuerpo desde un lugar"), ("vista frontal", "la que se ve al mirar el cuerpo de frente"), ("cuerpo geométrico", "objeto con tres dimensiones, como un cubo o una esfera"), ("silueta", "contorno de un cuerpo, como su sombra"), ("base", "cara en que se apoya el cuerpo")],
    worked=[
        {"title": "Vista frontal de un cubo", "problem": "¿Qué figura ves al mirar un cubo de frente?", "steps": ["El cubo tiene seis caras que son cuadrados iguales.", "De frente solo ves una cara.", "Esa cara es un cuadrado."], "answer": "Un cuadrado"},
        {"title": "Vista frontal de un cono", "problem": "Un cono está apoyado en su base. ¿Qué figura ves de frente?", "steps": ["La silueta es ancha abajo y termina en punta arriba.", "Esa figura tiene tres lados."], "answer": "Un triángulo"},
    ],
    mistakes=[
        {"wrong": "Decir que un cono visto de frente es un círculo porque su base es redonda.", "why": "Se confunde la forma de la base con la vista de frente.", "fix": "De frente el cono se ve como triángulo. El círculo se ve desde arriba."},
        {"wrong": "Decir que un cilindro parado y un cubo se ven igual de frente.", "why": "No se compara el alto con el ancho.", "fix": "Un cilindro más alto que ancho se ve como rectángulo; el cubo se ve como cuadrado."},
    ],
    tiers={
        "recovery": [
            ex("Mirando un cubo de frente, ¿qué figura ves?", "Un cuadrado", "Ves una de sus caras, que es un cuadrado."),
            ex("Un cilindro más alto que ancho está parado sobre una de sus bases. Visto de frente, ¿qué figura ves?", "Un rectángulo", "La silueta es alta y de lados rectos."),
            ex("Una pelota se mira de frente. ¿Qué figura ves?", "Un círculo", "La esfera se ve circular desde cualquier lado."),
        ],
        "understand": [
            ex("¿Qué es la vista frontal de un cuerpo?", "La figura que se ve al mirarlo de frente", "Es una figura plana, no el cuerpo entero."),
            ex("Un cono está apoyado en su base. Visto de frente, ¿qué figura ves?", "Un triángulo", "La silueta termina en punta."),
            ex("¿Por qué la esfera se ve como círculo desde todos los lados?", "Porque es redonda por igual en todas las direcciones", "No tiene caras ni aristas, todas las siluetas son iguales."),
        ],
        "apply": [
            ex("De estos cuerpos, ¿cuál se ve como triángulo de frente: cubo, cono apoyado en su base o esfera?", "El cono", "El cubo da cuadrado y la esfera, círculo."),
            ex("Un sombrero de fiesta con forma de cono se apoya en la mesa sobre su base. Visto de frente, ¿qué figura dibujas?", "Un triángulo", "Tiene una base ancha y termina en punta."),
            ex("Una pirámide de base cuadrada está apoyada en su base. Vista de frente, ¿qué figura ves?", "Un triángulo", "Las caras laterales son triángulos que terminan en punta."),
        ],
        "reason": [
            ex("Ana dice que un cono visto de frente es un círculo porque su base es redonda. ¿Tiene razón?", "No; de frente se ve un triángulo", "El círculo se ve solo desde arriba."),
            ex("Beto dice que un cilindro más alto que ancho y un cubo se ven igual de frente. ¿Tiene razón?", "No; el cilindro se ve como rectángulo y el cubo como cuadrado", "El rectángulo alto no es un cuadrado."),
        ],
        "challenge": [
            ex("Un cuerpo se ve como rectángulo de frente. ¿Cuál de estos puede ser: cono, cilindro parado o esfera?", "El cilindro parado", "El cono da triángulo y la esfera, círculo."),
            ex("De estos cuerpos, ¿cuántos se ven como círculo de frente: esfera, cono, cilindro parado y cubo?", "1", "Solo la esfera se ve círculo de frente."),
        ],
    },
    context=[ex("Una lata de conserva sin abrir está de pie sobre la mesa y es más alta que ancha. Dibujas lo que ves de frente. ¿Qué figura dibujas?", "Un rectángulo", "La lata es un cilindro parado y de frente se ve así.")],
    selfcheck=[
        ex("Un dado con forma de cubo se mira de frente. ¿Qué figura se ve?", "Un cuadrado", "La cara del cubo es un cuadrado."),
        ex("¿Qué figura es la vista frontal de una pirámide de base cuadrada apoyada en su base?", "Un triángulo", "Sus caras laterales terminan en punta."),
        ex("Una caja alargada se mira de frente por una cara larga. ¿Qué figura ves?", "Un rectángulo", "Esa cara es un rectángulo."),
    ],
    open_task=task(
        "Elige tres objetos que haya en tu casa: una caja, una lata y una pelota; o un dado, un rollo de cartón parado y un sombrero de fiesta. Dibuja la vista frontal de cada uno y escribe el nombre del cuerpo y de la figura que dibujaste.",
        "Caja: cuerpo = prisma rectangular, vista frontal = rectángulo. Lata: cilindro, rectángulo. Pelota: esfera, círculo.",
        ["dibuja una figura por objeto", "nombra el cuerpo y la figura", "las figuras coinciden con la vista frontal"],
        ["tres dibujos", "tres nombres"],
        ["dibujar la base en vez de la vista frontal", "confundir cuadrado con rectángulo"],
        "Pide que mire cada objeto con un ojo cerrado y de frente. Reconoce que dibuja lo que ve y no lo que sabe.",
    ),
    reinforce="Mira de frente una caja, una lata y una pelota y haz una lista con la figura que ves en cada una.",
    extend="Busca un objeto de tu casa cuya vista frontal sea un triángulo y otro cuya vista frontal sea un círculo.",
)

register(
    OA16, 2,
    materials="Lápiz y papel. Si quieres, cubos pequeños o bloques de armar (para niños de 9 años, sin piezas diminutas).",
    use="Aprenderé a decir qué se ve de una construcción de cubos cuando la miro desde un lado. Sirve para saber cuántos cubos se ven y cuáles quedan tapados.",
    prior=["Sé qué es la vista frontal.", "Sé contar cuadrados en una figura."],
    explain=[
        "La vista lateral es la que ves al mirar el cuerpo desde un costado. En esta clase miramos desde el lado derecho. Una construcción de cubos se ve como cuadrados. Cada cuadrado es la cara de un cubo.",
        "Algunos cubos quedan tapados por otros. Por ejemplo, una fila de 3 cubos puestos de izquierda a derecha, vista desde el lado, deja ver solo 1 cuadrado: el cubo de la punta tapa a los otros dos. Una torre de 4 cubos apilados se ve desde el lado como una columna de 4 cuadrados.",
        "Para una escalera de una fila con alturas 1, 2 y 3 (de izquierda a derecha), la vista frontal es la escalera. La vista lateral es una columna de 3 cuadrados: se ve el cubo más alto. Para saber la vista lateral, piensa en la altura más grande detrás de cada punto.",
    ],
    vocab=[("vista lateral", "la que se ve al mirar el cuerpo desde un costado"), ("tapado", "que no se ve porque otro cubo está delante"), ("altura", "cuántos cubos hay apilados"), ("fila", "cubos puestos uno al lado del otro"), ("torre", "cubos apilados uno sobre otro")],
    worked=[
        {"title": "Una fila vista de lado", "problem": "Una fila de 3 cubos va de izquierda a derecha. ¿Cuántos cuadrados tiene la vista desde el lado derecho?", "steps": ["Desde el lado derecho ves primero el cubo de la punta.", "Los otros dos cubos quedan detrás, tapados.", "Se ve 1 cuadrado."], "answer": "1 cuadrado"},
        {"title": "Una escalera vista de lado", "problem": "Una escalera de una fila tiene alturas 1, 2 y 3. ¿Cómo es su vista lateral?", "steps": ["Desde el lado se superponen las tres columnas.", "La más alta tiene 3 cubos y tapa a las otras.", "La vista es una columna de 3 cuadrados."], "answer": "Una columna de 3 cuadrados"},
    ],
    mistakes=[
        {"wrong": "Decir que la vista lateral de una fila de 3 cubos tiene 3 cuadrados porque hay 3 cubos.", "why": "Se cuentan los cubos que hay, no los que se ven.", "fix": "Desde el lado ves solo el cubo de la punta: 1 cuadrado."},
        {"wrong": "Contar todos los cubos de una escalera para su vista lateral.", "why": "No se considera que los cubos de atrás quedan tapados.", "fix": "La vista lateral muestra la altura mayor: columna de 3 cuadrados."},
    ],
    tiers={
        "recovery": [
            ex("Una torre tiene 4 cubos apilados. Mirada de frente, ¿cuántos cuadrados ves?", "4", "Los 4 cubos forman una columna de 4 cuadrados."),
            ex("La misma torre de 4 cubos se mira desde arriba. ¿Cuántos cuadrados ves?", "1", "Solo se ve la cara de arriba del cubo más alto."),
            ex("Una fila de 3 cubos va de izquierda a derecha. Vista desde el lado derecho, ¿cuántos cuadrados ves?", "1", "El cubo de la punta tapa a los otros dos."),
        ],
        "understand": [
            ex("¿Qué es la vista lateral de un cuerpo?", "La que se ve al mirarlo desde un costado", "Es la figura plana que se ve de lado."),
            ex("Una escalera de una fila tiene alturas 1, 2 y 3. ¿Cuántos cuadrados de alto tiene su vista lateral?", "3", "Se ve la columna más alta."),
            ex("¿Por qué algunos cubos no aparecen en una vista?", "Porque otros cubos los tapan", "Los cubos de atrás quedan detrás de los de adelante."),
        ],
        "apply": [
            arith("Una escalera de una fila tiene columnas de 1, 2 y 3 cubos. ¿Cuántos cubos tiene en total?", "1+2+3", "Se suman los cubos de las tres columnas."),
            ex("Una fila tiene tres torres de 2, 4 y 1 cubos, de izquierda a derecha. Vista desde el lado derecho, ¿cuántos cuadrados de alto tiene la figura?", "4", "Se ve la torre más alta, que tiene 4 cubos."),
            ex("Hay un cubo en el suelo, otro encima de él y un tercero pegado a la derecha del de abajo. Desde el lado derecho, ¿cuántos cuadrados de alto tiene la vista?", "2", "Se ve el cubo de la derecha y, detrás, la torre de 2 cubos."),
        ],
        "reason": [
            ex("Pía dice que la vista lateral de una fila de 3 cubos tiene 3 cuadrados porque hay 3 cubos. ¿Tiene razón?", "No; tiene 1 cuadrado", "Los otros cubos están tapados."),
            ex("Leo dice que una torre de 3 cubos se ve igual de frente que de lado. ¿Tiene razón?", "Sí; ambas vistas son una columna de 3 cuadrados", "La torre tiene un solo cubo de ancho y de largo."),
        ],
        "challenge": [
            ex("¿La escalera de alturas 1, 2 y 3 (una fila) se ve igual desde el lado derecho que desde el lado izquierdo?", "Sí", "En ambos casos se ve una columna de 3 cuadrados."),
            ex("Cuatro cubos forman un cuadrado de 2 por 2 en el suelo. Desde un costado, ¿cuántos cuadrados ves?", "2", "Los cubos de atrás quedan tapados por los de adelante."),
        ],
    },
    context=[ex("Un niño arma una torre de 5 cubos de colores. ¿Cuántos cuadrados tiene su vista lateral?", "5", "La torre se ve como una columna de 5 cuadrados.")],
    selfcheck=[
        ex("Una torre de 6 cubos se mira de frente. ¿Cuántos cuadrados ves?", "6", "Se ve una columna de 6 cuadrados."),
        ex("Una fila de 5 cubos de izquierda a derecha se mira de lado. ¿Cuántos cuadrados ves?", "1", "Los otros cuatro cubos están detrás."),
        ex("La escalera de alturas 1, 2 y 3 se mira de lado. ¿Cuál es la altura de la figura que ves?", "3 cuadrados", "Se ve la columna más alta."),
    ],
    open_task=task(
        "Con 6 cubos (reales o dibujados) arma una escalera de una fila con alturas 1, 2 y 3, o una torre de 6 cubos. Dibuja su vista frontal y su vista lateral derecha y escribe cuántos cuadrados tiene cada una.",
        "Escalera 1-2-3: vista frontal con columnas de 1, 2 y 3 cuadrados (6 en total); vista lateral con una columna de 3 cuadrados.",
        ["dibuja la vista frontal", "dibuja la vista lateral", "cuenta los cuadrados de cada vista"],
        ["dos dibujos", "conteos"],
        ["contar todos los cubos en la vista lateral", "confundir izquierda con derecha"],
        "Pide que ponga un dedo de lado para ver qué cubos tapan a otros. Reconoce el control de cubos tapados.",
    ),
    reinforce="Con bloques o cajitas, arma una torre de 3 cubos y una fila de 3 cubos y compara lo que ves de frente y de lado.",
    extend="Dibuja una construcción de 5 cubos cuya vista lateral tenga 2 cuadrados de alto y explica cuáles cubos quedan tapados.",
)

register(
    OA16, 3,
    materials="Lápiz y papel. Si quieres, cubos pequeños de armar.",
    use="Aprenderé a construir la vista desde arriba de un cuerpo. Sirve para dibujar el plano de una construcción.",
    prior=["Sé qué son la vista frontal y la lateral.", "Sé que algunos cubos quedan tapados."],
    explain=[
        "La vista superior es la que ves al mirar el cuerpo desde arriba, como un pájaro. Muestra el contorno de la base: la huella del cuerpo. La altura no se nota, porque solo ves lo de más arriba.",
        "Por ejemplo, una torre de 4 cubos se ve desde arriba como 1 cuadrado. Una fila de 3 cubos se ve como 3 cuadrados en fila. Un cilindro parado se ve como un círculo y una pirámide de base cuadrada, como un cuadrado.",
        "Para dibujar la vista superior de una construcción de cubos, dibuja un cuadrado por cada columna de cubos. No importa si la columna tiene 1 o 5 cubos de alto: igual es un cuadrado. Después comprueba que la cantidad de cuadrados coincide con las columnas que hay en el suelo.",
    ],
    vocab=[("vista superior", "la que se ve al mirar el cuerpo desde arriba"), ("huella", "figura que deja la base del cuerpo en el suelo"), ("columna", "cubos apilados uno sobre otro"), ("contorno", "línea que rodea una figura"), ("plano", "dibujo desde arriba")],
    worked=[
        {"title": "Vista superior de cuerpos", "problem": "¿Qué figura es la vista superior de un cono apoyado en su base?", "steps": ["Desde arriba ves la punta en el centro y la base redonda alrededor.", "El contorno es una figura redonda."], "answer": "Un círculo"},
        {"title": "Vista superior de cubos", "problem": "Cuatro cubos forman un cuadrado de 2 por 2 en el suelo y se pone una torre de 3 cubos sobre uno de ellos. ¿Cuántos cuadrados tiene la vista superior?", "steps": ["Hay 4 columnas en el suelo.", "La torre más alta sigue siendo una sola columna.", "Dibujo un cuadrado por columna: 4."], "answer": "4 cuadrados"},
    ],
    mistakes=[
        {"wrong": "Decir que la vista superior de una torre de 5 cubos tiene 5 cuadrados.", "why": "Se cuenta la altura en vez de las columnas.", "fix": "Desde arriba se ve solo la cara de arriba: 1 cuadrado."},
        {"wrong": "Decir que un cono visto desde arriba es un triángulo.", "why": "Se mezclan la vista frontal y la superior.", "fix": "Desde arriba se ve su base redonda: un círculo."},
    ],
    tiers={
        "recovery": [
            ex("Un cilindro está parado sobre una de sus bases. Visto desde arriba, ¿qué figura ves?", "Un círculo", "La tapa es circular."),
            ex("Un cono está apoyado en su base. Visto desde arriba, ¿qué figura ves?", "Un círculo", "El contorno es la base redonda."),
            ex("Una pirámide de base cuadrada se apoya en su base. Vista desde arriba, ¿qué figura ves?", "Un cuadrado", "El contorno es la base cuadrada."),
        ],
        "understand": [
            ex("¿Qué se ve de una torre de cubos al mirarla desde arriba?", "Un solo cuadrado", "Solo se ve la cara de arriba del cubo más alto."),
            ex("Una fila de 3 cubos se mira desde arriba. ¿Qué forma tiene la vista?", "Tres cuadrados en fila", "Cada cubo de la fila deja un cuadrado."),
            ex("¿La vista superior muestra la altura de los cubos?", "No", "Desde arriba solo se ve el contorno."),
        ],
        "apply": [
            ex("Tres cubos están en el suelo formando una L: dos van en fila y el tercero está detrás del primero. ¿Cuántos cuadrados tiene la vista superior?", "3", "Hay un cuadrado por cada cubo del suelo."),
            ex("Cinco cubos forman una fila en el suelo y sobre el primero de la fila se ponen dos cubos más. ¿Cuántos cuadrados tiene la vista superior?", "5", "Hay 5 columnas en el suelo."),
            ex("Una torre de 2 cubos está pegada a una torre de 3 cubos. ¿Cuántos cuadrados tiene la vista superior?", "2", "Hay 2 columnas."),
        ],
        "reason": [
            ex("Gael dice que la vista superior de una torre de 5 cubos tiene 5 cuadrados. ¿Tiene razón?", "No; tiene 1 cuadrado", "Desde arriba solo se ve la cara de arriba."),
            ex("Mía dice que desde arriba un cubo sobre otro se ve igual que un solo cubo. ¿Tiene razón?", "Sí", "La vista superior muestra solo el contorno de la base."),
        ],
        "challenge": [
            ex("Una vista superior es un cuadrado de 2 por 2 (4 cuadrados). ¿Cuál es la menor cantidad de cubos que puede tener la construcción?", "4", "Cada columna tiene al menos 1 cubo."),
            ex("La vista superior es un cuadrado de 2 por 2 y cada columna tiene 1 o 2 cubos. ¿Cuál es la mayor cantidad posible de cubos?", "8", "4 columnas por 2 cubos dan 8."),
        ],
    },
    context=[ex("Una casita de juguete tiene base cuadrada y techo en forma de pirámide. Vista desde arriba, ¿qué figura ves?", "Un cuadrado", "El contorno de la casita es cuadrado.")],
    selfcheck=[
        ex("Una fila de 5 cubos se mira desde arriba. ¿Cuántos cuadrados ves?", "5", "Cada cubo del suelo deja un cuadrado."),
        ex("Una lata de pie se mira desde arriba. ¿Qué figura ves?", "Un círculo", "La tapa de un cilindro es circular."),
        ex("Una torre de 7 cubos se mira desde arriba. ¿Cuántos cuadrados ves?", "1", "Solo se ve la cara de arriba."),
    ],
    open_task=task(
        "Elige una construcción: A) tres cubos en fila y, pegada al último, una torre de 2 cubos (una columna más); B) un cuadrado de 2 por 2 en el suelo donde la columna de una esquina tiene 3 cubos de alto. Dibuja su vista superior y escribe cuántos cuadrados tiene.",
        "B) La vista superior es un cuadrado de 2 por 2 con 4 cuadrados: la torre no agrega cuadrados.",
        ["dibuja un cuadrado por columna", "cuenta bien los cuadrados", "explica por qué la altura no se nota"],
        ["dibujo", "explicación"],
        ["contar la altura", "dibujar la vista frontal"],
        "Pide que cuente las columnas en el suelo. Reconoce que distingue columna de cubo.",
    ),
    reinforce="Mira desde arriba una caja, una lata y un cono de papel y haz una lista con las figuras que ves.",
    extend="Dibuja la vista superior de una construcción de 6 cubos que tenga exactamente 4 cuadrados.",
)

register(
    OA16, 4,
    materials="Lápiz y papel.",
    use="Aprenderé a descubrir de qué cuerpo se trata usando sus vistas de frente, de lado y desde arriba. Sirve porque una sola vista a veces no alcanza.",
    prior=["Sé dar las vistas frontal, lateral y superior de un cuerpo.", "Conozco cubo, cilindro, cono, esfera, pirámide y caja."],
    explain=[
        "Una sola vista puede venir de varios cuerpos. Un cilindro parado y una caja se ven como rectángulo de frente. Un cono y una pirámide de base cuadrada se ven como triángulo de frente. Por eso se usan varias vistas.",
        "Para identificar un cuerpo, compara las tres vistas. Frente rectángulo, lado rectángulo y arriba círculo es un cilindro. Frente triángulo, lado triángulo y arriba círculo es un cono. Con triángulos de frente y de lado, y un cuadrado arriba, es una pirámide de base cuadrada.",
        "Si las tres vistas son círculos, el cuerpo es una esfera. Si son cuadrados, es un cubo. Si son rectángulos, es una caja. Siempre revisa que ninguna vista contradiga al cuerpo que elegiste.",
    ],
    vocab=[("identificar", "reconocer qué es algo"), ("vista", "figura plana que se ve desde un lugar"), ("pirámide de base cuadrada", "cuerpo con base cuadrada y cuatro caras triangulares que se juntan en una punta"), ("caja (prisma rectangular)", "cuerpo con seis caras rectangulares"), ("contradecir", "no coincidir con otra información")],
    worked=[
        {"title": "Identificar con tres vistas", "problem": "Las vistas son: de frente, un rectángulo; de lado, un rectángulo; desde arriba, un círculo. ¿Qué cuerpo es?", "steps": ["Los rectángulos de frente y de lado tienen los lados rectos.", "El círculo de arriba indica una base redonda.", "El cuerpo con base redonda y lados rectos es el cilindro."], "answer": "Un cilindro"},
        {"title": "Una vista no alcanza", "problem": "Un cuerpo se ve como triángulo de frente. ¿Es seguro que es un cono?", "steps": ["La pirámide de base cuadrada también se ve como triángulo.", "Hay que mirar desde arriba: círculo para el cono y cuadrado para la pirámide."], "answer": "No es seguro; hay que mirar desde arriba"},
    ],
    mistakes=[
        {"wrong": "Decir que todo cuerpo con vista frontal de triángulo es un cono.", "why": "No se considera la pirámide.", "fix": "Mira la vista superior: círculo para el cono, cuadrado para la pirámide."},
        {"wrong": "Decir que si ves rectángulo de frente y círculo desde arriba es una caja.", "why": "Una caja se ve rectángulo desde arriba, no círculo.", "fix": "Un círculo arriba y un rectángulo de frente indican un cilindro."},
    ],
    tiers={
        "recovery": [
            ex("Vistas: de frente, un rectángulo; de lado, un rectángulo; desde arriba, un círculo. ¿Qué cuerpo es?", "Un cilindro", "La base redonda y los lados rectos son de un cilindro."),
            ex("Vistas: de frente, un triángulo; de lado, un triángulo; desde arriba, un círculo. ¿Qué cuerpo es?", "Un cono", "Termina en punta y tiene la base redonda."),
            ex("Las tres vistas de un cuerpo son círculos. ¿Qué cuerpo es?", "Una esfera", "Solo la esfera se ve círculo desde todos los lados."),
        ],
        "understand": [
            ex("Un cilindro parado y una caja se ven como rectángulo de frente. ¿Qué vista los distingue?", "La vista desde arriba", "El cilindro da círculo y la caja da rectángulo."),
            ex("Un cuerpo se ve como cuadrado de frente. ¿Alcanza esa vista para decir que es un cubo?", "No", "Una caja de base cuadrada también puede verse así."),
            ex("Dos cuerpos se ven como triángulo de frente. Uno se ve como círculo desde arriba y el otro como cuadrado. ¿Cuál es el cono?", "El que se ve como círculo desde arriba", "La base del cono es redonda."),
        ],
        "apply": [
            ex("Vistas: de frente, un triángulo; de lado, un triángulo; desde arriba, un cuadrado. ¿Qué cuerpo es?", "Una pirámide de base cuadrada", "Las caras laterales terminan en punta sobre una base cuadrada."),
            ex("Vistas: de frente, de lado y desde arriba, rectángulos. ¿Qué cuerpo es?", "Una caja (prisma rectangular)", "Todas sus caras son rectángulos."),
            ex("Vistas: de frente, de lado y desde arriba, cuadrados. ¿Qué cuerpo es?", "Un cubo", "Todas sus caras son cuadrados."),
        ],
        "reason": [
            ex("Nico ve un rectángulo de frente y dice «es una caja». Desde arriba ve un círculo. ¿Qué cuerpo es?", "Un cilindro", "Una caja se ve rectángulo desde arriba."),
            ex("Sara dice: «si de frente veo un triángulo, siempre es un cono». ¿Qué cuerpo muestra que se equivoca?", "La pirámide de base cuadrada", "También se ve triángulo de frente."),
        ],
        "challenge": [
            ex("Frente: columnas de 1, 2 y 3 cuadrados. Arriba: una fila de 3 cuadrados. Lado: una columna de 3 cuadrados. ¿Cuántos cubos tiene la escalera?", "6", "1 + 2 + 3 = 6."),
            ex("¿Una torre de 3 cubos y una fila de 3 cubos acostada tienen la misma vista superior?", "No", "La torre da 1 cuadrado y la fila da 3."),
        ],
    },
    context=[ex("Una carpa pequeña tiene base cuadrada y techo que termina en punta. Un sombrero de fiesta es un cono. Ambos se ven como triángulo de frente. ¿Qué vista usas para distinguirlos?", "La vista desde arriba", "Da cuadrado para la carpa y círculo para el cono.")],
    selfcheck=[
        ex("Frente: rectángulo. Lado: rectángulo. Arriba: rectángulo. ¿Qué cuerpo es?", "Una caja", "Todas las vistas son rectángulos."),
        ex("Frente: triángulo. Lado: triángulo. Arriba: círculo. ¿Qué cuerpo es?", "Un cono", "Tiene punta y base redonda."),
        ex("¿Qué cuerpo no cambia de vista aunque lo gires?", "La esfera", "Siempre se ve como círculo."),
    ],
    open_task=task(
        "Elige uno de estos cuerpos: cilindro, cono o pirámide de base cuadrada. Escribe cómo se ve de frente, de lado y desde arriba. Luego pide a una persona que adivine el cuerpo con tus tres vistas, sin decir el nombre.",
        "Cono: de frente, triángulo; de lado, triángulo; desde arriba, círculo.",
        ["escribe las tres vistas", "las vistas coinciden con el cuerpo", "se puede adivinar el cuerpo con ellas"],
        ["tres vistas", "cuerpo adivinado"],
        ["confundir cono y pirámide", "dar una sola vista"],
        "Pide que diga qué vista distingue su cuerpo de otro parecido. Reconoce la comparación de vistas.",
    ),
    reinforce="Elige tres objetos de tu casa y escribe sus tres vistas. Pide que alguien adivine los objetos.",
    extend="Busca dos cuerpos distintos que tengan la misma vista de frente y escribe cuál vista los distingue.",
)

# ================================================================ OA 17
register(
    OA17, 1,
    materials="Lápiz y papel. Una hoja de papel para doblar.",
    use="Aprenderé qué es una línea de simetría y a reconocer figuras simétricas. Sirve para ver cuándo una figura es igual a su reflejo.",
    prior=["Conozco el cuadrado, el rectángulo y el triángulo.", "Sé doblar una hoja por la mitad."],
    explain=[
        "Una figura es simétrica si una línea la divide en dos partes que son el reflejo de la otra, como en un espejo. Si doblas la figura por esa línea, las dos partes coinciden exactamente. La línea se llama línea de simetría.",
        "El cuadrado tiene 4 líneas de simetría. El rectángulo que no es cuadrado tiene 2. El triángulo con sus tres lados iguales tiene 3. El círculo tiene muchas, porque cualquier línea que pase por su centro sirve.",
        "Algunas figuras no son simétricas. La letra L mayúscula no lo es: no hay línea que la deje en dos mitades iguales. Cuidado: no toda línea que parte una figura en dos partes iguales es de simetría. En un rectángulo que no es cuadrado, la diagonal lo parte en dos triángulos iguales, pero al doblar no coinciden.",
    ],
    vocab=[("línea de simetría", "línea que divide una figura en dos partes que coinciden al doblar"), ("simétrica", "que tiene al menos una línea de simetría"), ("reflejo", "imagen como en un espejo"), ("coincidir", "quedar justo una sobre la otra"), ("mitad", "una de dos partes iguales")],
    worked=[
        {"title": "Letras simétricas", "problem": "De las letras mayúsculas de imprenta A, F, T y G, ¿cuáles son simétricas?", "steps": ["Imagina una línea vertical por el medio de cada letra.", "En la A y en la T, las mitades son el reflejo de la otra.", "En la F y en la G no ocurre en ninguna dirección."], "answer": "A y T"},
        {"title": "Contar líneas", "problem": "¿Cuántas líneas de simetría tiene un rectángulo que no es cuadrado?", "steps": ["Una línea vertical por el medio lo divide en dos rectángulos iguales que coinciden.", "Una línea horizontal por el medio también.", "Las diagonales no sirven."], "answer": "2"},
    ],
    mistakes=[
        {"wrong": "Decir que la diagonal de un rectángulo que no es cuadrado es una línea de simetría.", "why": "Se piensa que partir en dos partes iguales basta.", "fix": "Al doblar por la diagonal las partes no coinciden. No es de simetría."},
        {"wrong": "Decir que un círculo no tiene línea de simetría porque no tiene lados.", "why": "Se cree que hace falta tener lados.", "fix": "Cualquier línea que pase por el centro del círculo es de simetría."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué le pasa a una figura simétrica al doblarla por una línea de simetría?", "Las dos partes coinciden", "Una parte queda justo sobre la otra."),
            ex("¿Es simétrico un cuadrado?", "Sí", "Se puede doblar por varias líneas y las partes coinciden."),
            ex("¿Es simétrica la letra mayúscula L de imprenta?", "No", "Ninguna línea la deja en dos partes que coincidan."),
        ],
        "understand": [
            ex("¿Qué significa que dos mitades sean el reflejo de la otra?", "Que una es la imagen en espejo de la otra", "Al doblar por la línea, coinciden."),
            ex("Una figura tiene una línea de simetría vertical. ¿Las mitades izquierda y derecha son iguales en forma?", "Sí, se ven como en un espejo", "Esa es la definición de simetría."),
            ex("¿Todas las figuras tienen al menos una línea de simetría?", "No", "Por ejemplo, la letra L no tiene ninguna."),
        ],
        "apply": [
            ex("De las letras mayúsculas de imprenta M, P, H y S, ¿cuáles tienen una línea de simetría?", "M y H", "La M y la H tienen una línea que las divide en mitades que coinciden; la P y la S no."),
            ex("La letra mayúscula T de imprenta tiene una línea de simetría. ¿Es vertical u horizontal?", "Vertical", "Una línea vertical por el medio la deja en dos mitades que coinciden."),
            ex("¿Cuántas líneas de simetría tiene un triángulo con sus tres lados iguales?", "3", "Una por cada vértice hasta el punto medio del lado opuesto."),
        ],
        "reason": [
            ex("Luis dice que cualquier línea que parte un rectángulo (no cuadrado) en dos partes iguales es de simetría. Usa la diagonal para responder.", "No; al doblar por la diagonal las partes no coinciden", "La diagonal da dos triángulos iguales que no se superponen al doblar."),
            ex("Sara dice que el círculo no tiene líneas de simetría porque no tiene lados. ¿Tiene razón?", "No; tiene muchas", "Cualquier línea que pase por el centro sirve."),
        ],
        "challenge": [
            ex("¿Cuántas líneas de simetría tiene un cuadrado?", "4", "Dos que pasan por los puntos medios de lados opuestos y dos diagonales."),
            ex("La letra H mayúscula de imprenta tiene una línea vertical y una horizontal. ¿Cuántas líneas de simetría tiene?", "2", "Una vertical y una horizontal."),
        ],
    },
    context=[ex("Una diseñadora dibuja un corazón con una línea vertical en el centro. Las dos mitades coinciden al doblar. ¿Esa línea es una línea de simetría?", "Sí", "Dobla el corazón en mitades que coinciden.")],
    selfcheck=[
        ex("¿La letra mayúscula M de imprenta tiene una línea de simetría vertical?", "Sí", "Sus mitades son el reflejo de la otra."),
        ex("¿Cuántas líneas de simetría tiene la letra F mayúscula de imprenta?", "0", "No hay ninguna línea que la deje en dos partes que coincidan."),
        ex("Si al doblar una figura las partes coinciden, ¿la línea del doblez es de simetría?", "Sí", "Es la definición."),
    ],
    open_task=task(
        "Elige tres figuras o letras entre: cuadrado, rectángulo, triángulo con tres lados iguales, L, T, H, F. Di si son simétricas y, si lo son, cuántas líneas de simetría tienen. Dibuja las líneas.",
        "Cuadrado: 4 líneas. T: 1 línea. L: no es simétrica.",
        ["responde bien para las tres", "dibuja las líneas de simetría", "explica con el doblez"],
        ["tres dibujos", "cantidad de líneas"],
        ["contar la diagonal del rectángulo", "olvidar líneas horizontales"],
        "Pide que doble el dibujo por cada línea. Reconoce la comprobación con doblez.",
    ),
    reinforce="Dibuja un cuadrado en una hoja y dóblalo por todas las líneas que se te ocurran. Cuenta las que funcionan.",
    extend="Escribe cinco letras mayúsculas de imprenta que tengan línea de simetría y cinco que no.",
)

register(
    OA17, 2,
    materials="Lápiz, papel y una hoja que puedas doblar. No uses tijeras si no hay una persona adulta cerca.",
    use="Aprenderé a comprobar si una línea es de simetría doblando la figura. Sirve para estar seguro y no equivocarse a ojo.",
    prior=["Sé qué es una línea de simetría.", "Sé cuántas líneas tienen el cuadrado y el rectángulo."],
    explain=[
        "Para comprobar una línea de simetría, imagina que doblas la figura por esa línea. Si las dos partes coinciden por completo, la línea es de simetría. Si algún borde queda fuera o dentro, no lo es.",
        "En un cuadrado, doblar por la línea que une los puntos medios de dos lados opuestos funciona. Doblar por una diagonal también. En un rectángulo que no es cuadrado, la diagonal no funciona, pero las líneas por los puntos medios de lados opuestos sí.",
        "Una línea de simetría puede ser vertical, horizontal o inclinada. No siempre es vertical. En un triángulo con dos lados iguales hay una sola: va desde el punto donde se juntan los lados iguales hasta el punto medio del lado de abajo.",
    ],
    vocab=[("doblar", "plegar una figura por una línea"), ("coincidir", "quedar una parte justo sobre la otra"), ("vértice", "punto donde se juntan dos lados"), ("punto medio", "punto que divide un lado en dos partes iguales"), ("diagonal", "línea que une dos vértices que no están seguidos")],
    worked=[
        {"title": "Comprobar con el doblez", "problem": "Doblas un rectángulo que no es cuadrado por una diagonal. ¿Es línea de simetría?", "steps": ["Al doblar, las puntas de los lados sobresalen.", "Las dos partes no coinciden."], "answer": "No es línea de simetría"},
        {"title": "Un triángulo con dos lados iguales", "problem": "Un triángulo tiene dos lados iguales. Doblas por la línea desde donde se juntan esos lados hasta el punto medio del lado de abajo. ¿Cuántas líneas de simetría tiene?", "steps": ["Esa línea hace coincidir los dos lados iguales.", "No hay otra línea que lo logre."], "answer": "1"},
    ],
    mistakes=[
        {"wrong": "Decir que una línea de simetría siempre es vertical.", "why": "Solo se imaginan las líneas más conocidas.", "fix": "También hay horizontales e inclinadas, como las diagonales del cuadrado."},
        {"wrong": "Doblar un rectángulo por la diagonal y decir «coincide» sin mirar las puntas.", "why": "No se revisan los bordes.", "fix": "Si una punta sobresale, no coincide."},
    ],
    tiers={
        "recovery": [
            ex("Doblas un cuadrado por la línea que une los puntos medios de dos lados opuestos y las dos mitades coinciden. ¿Es línea de simetría?", "Sí", "Al doblar, las partes coinciden por completo."),
            ex("Doblas un rectángulo que no es cuadrado por una diagonal. Las partes no coinciden. ¿Es línea de simetría?", "No", "Los bordes sobresalen."),
            ex("Si al doblar por una línea las partes no coinciden, ¿esa línea es de simetría?", "No", "Debe haber coincidencia exacta."),
        ],
        "understand": [
            ex("¿Qué debe pasar al doblar por una línea de simetría?", "Las dos partes deben coincidir exactamente", "Ningún borde puede sobresalir."),
            ex("¿Cuántos dobleces por los puntos medios de lados opuestos sirven en un rectángulo que no es cuadrado?", "2", "Uno vertical y otro horizontal."),
            ex("¿Una línea de simetría puede ser inclinada?", "Sí", "Por ejemplo, las diagonales del cuadrado."),
        ],
        "apply": [
            ex("Doblas un cuadrado por una diagonal. ¿Las partes coinciden?", "Sí", "Los dos triángulos quedan uno sobre otro."),
            ex("¿Cuántas líneas de simetría tiene un triángulo con exactamente dos lados iguales?", "1", "Solo la que va del vértice de los lados iguales al punto medio de la base."),
            ex("¿Cuántas líneas de simetría tiene un triángulo con los tres lados de distinto largo?", "0", "Ningún doblez hace coincidir sus partes."),
        ],
        "reason": [
            ex("Ema dobló un rectángulo (no cuadrado) por la diagonal y dice que sí es simétrico. ¿Qué no observó?", "Que las puntas sobresalen y no coinciden", "Un doblez por la diagonal no hace coincidir las partes."),
            ex("Pedro dice que una línea de simetría debe ser vertical. ¿Tiene razón?", "No; también hay horizontales e inclinadas", "El cuadrado tiene líneas de las tres clases."),
        ],
        "challenge": [
            ex("Un cuadrado tiene dos líneas por los puntos medios de lados opuestos y dos diagonales. ¿Cuántas líneas de simetría tiene en total?", "4", "2 + 2 = 4."),
            ex("Un pentágono regular tiene tantas líneas de simetría como lados. ¿Cuántas tiene?", "5", "Un pentágono tiene 5 lados."),
        ],
    },
    context=[ex("Una tarjeta rectangular (no cuadrada) se dobla por la mitad a lo largo y por la mitad a lo ancho. ¿Cuántos de esos dos dobleces hacen coincidir las partes?", "2", "Ambos dobleces pasan por los puntos medios de lados opuestos.")],
    selfcheck=[
        ex("Doblas un rectángulo que no es cuadrado por la línea horizontal que pasa por el medio. ¿Las partes coinciden?", "Sí", "Esa línea pasa por los puntos medios de los lados cortos."),
        ex("Doblas un cuadrado por una línea que va de una esquina a un punto de un lado que no es ni el punto medio ni una esquina. Las partes no coinciden. ¿Es línea de simetría?", "No", "Debe haber coincidencia exacta."),
        ex("¿Cuántas líneas de simetría tiene un cuadrado?", "4", "Dos por los puntos medios y dos diagonales."),
    ],
    open_task=task(
        "Dibuja un cuadrado y un rectángulo (no cuadrado) en una hoja y recórtalos solo si hay una persona adulta cerca; si no, dibuja y dobla la hoja entera. Prueba doblar por una diagonal y por una línea por los puntos medios de lados opuestos. Escribe qué pasó en cada figura.",
        "Cuadrado: la diagonal sirve y la línea por los puntos medios también. Rectángulo: la línea por los puntos medios sirve, la diagonal no.",
        ["prueba al menos dos dobleces en cada figura", "observa si las partes coinciden", "escribe las conclusiones"],
        ["registro", "conclusiones"],
        ["mirar a ojo en vez de doblar", "decir que la diagonal del rectángulo sirve"],
        "Pide que muestre las puntas que sobresalen en el rectángulo. Reconoce la comprobación con doblez.",
    ),
    reinforce="Dibuja un triángulo con dos lados iguales y dóblalo para encontrar su línea de simetría.",
    extend="Dibuja un hexágono regular y busca cuántas líneas de simetría tiene doblando.",
)

register(
    OA17, 3,
    materials="Lápiz y papel cuadriculado (o cuadrícula dibujada).",
    use="Aprenderé a completar una figura simétrica en una cuadrícula. Sirve para dibujar la otra mitad de un diseño.",
    prior=["Sé qué es una línea de simetría.", "Sé ubicar cuadritos por fila y columna."],
    explain=[
        "En una cuadrícula puedes completar una figura simétrica. Primero ubica la línea de simetría, que llamaremos eje. Luego, para cada cuadrito pintado, pinta su simétrico al otro lado del eje, a la misma distancia.",
        "Para un eje vertical entre las columnas 3 y 4 en una cuadrícula de 6 columnas, la columna 3 se refleja en la 4, la 2 en la 5 y la 1 en la 6. En general, la columna c se refleja en la 7 − c. La fila no cambia.",
        "Para un eje horizontal, ocurre lo contrario: la columna no cambia y la fila se refleja. Con 4 filas y el eje entre las filas 2 y 3, la fila 1 se refleja en la 4. Al terminar, dobla mentalmente la figura por el eje y comprueba que todo coincide.",
    ],
    vocab=[("eje de simetría", "línea de simetría de una figura"), ("simétrico", "punto o cuadrito que es reflejo de otro respecto del eje"), ("cuadrícula", "cuadros iguales ordenados en filas y columnas"), ("reflejar", "dibujar la imagen como en un espejo"), ("misma distancia", "igual cantidad de cuadritos hasta el eje")],
    worked=[
        {"title": "Reflejar con eje vertical", "problem": "En una cuadrícula de 6 columnas, el eje vertical está entre las columnas 3 y 4. Un cuadrito está pintado en la fila 1, columna 2. ¿En qué columna queda su simétrico?", "steps": ["La columna 2 está a 2 cuadritos del eje (la 3 está a 1).", "El simétrico está a 2 cuadritos del eje, al otro lado.", "Contando desde el eje: la columna 4 es 1, la 5 es 2."], "answer": "Columna 5, en la misma fila 1"},
        {"title": "Reflejar con eje horizontal", "problem": "En una cuadrícula de 4 filas el eje horizontal está entre las filas 2 y 3. Un cuadrito está en la fila 1, columna 4. ¿Dónde queda su simétrico?", "steps": ["La fila 1 está a 2 cuadritos del eje.", "El simétrico está a 2 cuadritos al otro lado: fila 4.", "La columna no cambia."], "answer": "Fila 4, columna 4"},
    ],
    mistakes=[
        {"wrong": "Reflejar el cuadrito de la columna 1 en la columna 4, con el eje entre las columnas 3 y 4.", "why": "No se respeta la misma distancia al eje.", "fix": "La columna 1 está a 3 cuadritos del eje. Su simétrico está a 3 del otro lado: la columna 6."},
        {"wrong": "Cambiar también la fila al reflejar con un eje vertical.", "why": "Se mezclan los dos tipos de eje.", "fix": "Con eje vertical, la fila no cambia."},
    ],
    tiers={
        "recovery": [
            ex("Una cuadrícula tiene 6 columnas y el eje vertical está entre las columnas 3 y 4. Un cuadrito pintado está en la fila 1, columna 2. ¿En qué columna queda su simétrico?", "5", "Está a 2 cuadritos del eje, igual que la columna 5 del otro lado."),
            ex("Con ese mismo eje vertical (entre las columnas 3 y 4), un cuadrito está en la columna 3. ¿En qué columna queda su simétrico?", "4", "La 3 está pegada al eje y su simétrico también."),
            ex("Con ese eje, un cuadrito está en la columna 1. ¿En qué columna queda su simétrico?", "6", "Está a 3 cuadritos del eje, igual que la columna 6."),
        ],
        "understand": [
            ex("Al reflejar con un eje vertical, ¿qué se mantiene igual: la fila o la columna?", "La fila", "El reflejo ocurre de izquierda a derecha."),
            ex("¿A qué distancia del eje está el simétrico de un cuadrito?", "A la misma distancia, del otro lado", "Esa es la regla de la simetría."),
            ex("El eje vertical está entre las columnas 3 y 4 de una cuadrícula de 6 columnas. ¿En qué columna queda el simétrico de la columna 5?", "2", "La 5 está a 2 cuadritos del eje y la 2 también."),
        ],
        "apply": [
            ex("Hay cuadritos pintados en: fila 1, columna 1; fila 2, columna 2; fila 3, columna 3. El eje vertical está entre las columnas 3 y 4. ¿Qué cuadritos hay que pintar para completar la figura?", "Fila 1 columna 6; fila 2 columna 5; fila 3 columna 4", "Cada uno se refleja en la columna 7 − c y la fila se mantiene."),
            ex("Una cuadrícula tiene 6 filas y el eje horizontal está entre las filas 3 y 4. Un cuadrito está en la fila 2, columna 1. ¿En qué fila queda su simétrico?", "5", "La fila 2 está a 2 cuadritos del eje y la fila 5 también."),
            ex("La mitad de una figura tiene 5 cuadritos pintados y ninguno está sobre el eje. ¿Cuántos cuadritos pintados tiene la figura completa?", "10", "Cada cuadrito tiene un simétrico, así que se duplican."),
        ],
        "reason": [
            ex("Tomás dice que, con el eje entre las columnas 3 y 4, el simétrico de la fila 2 columna 1 es la fila 2 columna 4. ¿Qué error cometió y cuál es la columna correcta?", "No respetó la distancia; es la columna 6", "La columna 1 está a 3 cuadritos del eje y la 6 también."),
            ex("Rita dice que al reflejar con eje vertical la figura cambia de fila. ¿Tiene razón?", "No; la fila se mantiene", "El eje vertical refleja la izquierda con la derecha."),
        ],
        "challenge": [
            ex("El eje vertical está entre las columnas 3 y 4 de una cuadrícula de 6 columnas. Hay pintados la fila 1 columna 3; la fila 2 columna 2; y la fila 3 columna 1. Al completar la figura, ¿cuántos cuadritos pintados hay en la fila 2?", "2", "La fila 2 tiene los de las columnas 2 y 5."),
            ex("Una cuadrícula tiene 7 columnas y el eje vertical pasa por el centro de la columna 4. ¿En qué columna queda el simétrico de la columna 2?", "6", "La 2 está a 2 columnas del eje y la 6 también."),
        ],
    },
    context=[ex("Dibujas una casita con cuadritos. El techo en la mitad izquierda está en las columnas 2 y 3, y el eje vertical está entre las columnas 3 y 4 de una cuadrícula de 6 columnas. ¿En qué columnas va el techo de la mitad derecha?", "En las columnas 4 y 5", "La 3 se refleja en la 4 y la 2 en la 5.")],
    selfcheck=[
        ex("Con el eje vertical entre las columnas 3 y 4, ¿en qué columna queda el simétrico de la columna 2?", "5", "La 2 está a 2 cuadritos del eje."),
        ex("Con un eje horizontal entre las filas 2 y 3, ¿en qué fila queda el simétrico de la fila 2?", "3", "La fila 2 está pegada al eje y su simétrico también."),
        ex("Una cuadrícula tiene 7 columnas y el eje vertical pasa por el centro de la columna 4. Las columnas 1 a 3 tienen 6 cuadritos pintados y la columna 4 tiene 1. Al completar la figura con las columnas 5 a 7, ¿cuántos cuadritos pintados hay en total?", "13", "Los 6 de la izquierda se duplican a 12 y el de la columna 4 se cuenta una vez."),
    ],
    open_task=task(
        "Dibuja una cuadrícula de 6 columnas y 4 filas con un eje vertical entre las columnas 3 y 4. Pinta 5 cuadritos distintos en las columnas 1 a 3. Completa la figura reflejando cada uno. Escribe la lista de cuadritos que pintaste en el lado derecho.",
        "Pinté (fila 1, col 2), (fila 2, col 1), (fila 3, col 3), (fila 4, col 2) y (fila 4, col 3). Los reflejos son (1,5), (2,6), (3,4), (4,5) y (4,4).",
        ["pinta 5 cuadritos en la mitad izquierda", "refleja cada uno con la misma distancia al eje", "la fila no cambia"],
        ["cuadrícula", "lista de reflejos"],
        ["no respetar la distancia", "cambiar la fila"],
        "Pide que cuente la distancia al eje con el dedo. Reconoce el control de la distancia.",
    ),
    reinforce="En papel cuadriculado dibuja una línea vertical y pinta cuadritos a un lado. Pide a alguien que pinte los simétricos y revisa con un doblez.",
    extend="Dibuja una figura con eje horizontal y eje vertical al mismo tiempo, completando las cuatro partes.",
)

register(
    OA17, 4,
    materials="Lápiz y papel; si quieres, una hoja para doblar.",
    use="Aprenderé a crear figuras con una o más líneas de simetría. Sirve para diseñar adornos, letras y dibujos simétricos.",
    prior=["Sé comprobar una línea de simetría doblando.", "Sé completar figuras en una cuadrícula."],
    explain=[
        "Para crear una figura simétrica, dibuja una mitad pegada a la línea de simetría y luego dibuja su reflejo. También puedes doblar el papel, dibujar la mitad en un lado y copiar la forma al otro. Si la figura tiene una sola línea, es simétrica en un solo sentido.",
        "Algunas figuras tienen más de una línea. Un rectángulo que no es cuadrado tiene 2. Un cuadrado tiene 4. Un triángulo con tres lados iguales tiene 3. Un círculo tiene muchas. Al agregar partes a una figura, puedes perder líneas de simetría.",
        "Por ejemplo, dos círculos de distinto tamaño puestos lado a lado tienen solo una línea: la que pasa por sus dos centros. Si fueran del mismo tamaño tendrían dos líneas. Para saber cuántas líneas tiene tu figura, prueba doblando y cuenta solo las que funcionan.",
    ],
    vocab=[("crear", "hacer algo nuevo"), ("reflejo", "imagen como en un espejo"), ("una o más líneas", "una sola, o varias, líneas de simetría"), ("figura compuesta", "figura formada por varias figuras unidas"), ("doblez", "línea donde se dobla el papel")],
    worked=[
        {"title": "Crear con un doblez", "problem": "Dibujas la mitad de un corazón junto al doblez y copias la forma al otro lado. ¿Cuántas líneas de simetría tiene el corazón?", "steps": ["El doblez hace coincidir las dos mitades.", "No hay otra línea que lo logre."], "answer": "1"},
        {"title": "Perder una línea de simetría", "problem": "Se pega un círculo pequeño al lado de un círculo grande. ¿Cuántas líneas de simetría tiene la figura?", "steps": ["Dos círculos de distinto tamaño no son iguales a ambos lados de ninguna línea que los separe.", "Solo sirve la línea que pasa por los dos centros."], "answer": "1"},
    ],
    mistakes=[
        {"wrong": "Decir que dos círculos de distinto tamaño pegados tienen infinitas líneas de simetría.", "why": "Se piensa en el círculo solo.", "fix": "Solo queda 1 línea: la que pasa por los dos centros."},
        {"wrong": "Decir que un rectángulo con dos cuadrados unidos tiene 4 líneas de simetría.", "why": "Se cuentan las líneas del cuadrado.", "fix": "Un rectángulo que no es cuadrado tiene 2."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál tiene exactamente 1 línea de simetría: triángulo con dos lados iguales (no tres), cuadrado o círculo?", "El triángulo con dos lados iguales", "El cuadrado tiene 4 y el círculo tiene muchas."),
            ex("¿Cuál tiene exactamente 2 líneas de simetría: rectángulo (no cuadrado) o triángulo con tres lados iguales?", "El rectángulo", "El triángulo de tres lados iguales tiene 3."),
            ex("¿Qué figura tiene muchísimas líneas de simetría?", "El círculo", "Cualquier línea por el centro sirve."),
        ],
        "understand": [
            ex("Quieres crear una figura simétrica doblando un papel. ¿Qué dibujas junto al doblez?", "La mitad de la figura", "Después copias la forma al otro lado."),
            ex("Si dibujas una figura y su reflejo con un eje, ¿cuántas líneas de simetría tiene al menos?", "1", "El eje es una línea de simetría."),
            ex("Una figura tiene 2 líneas de simetría. ¿Cuántos dobleces distintos hacen coincidir sus partes?", "2", "Uno por cada línea."),
        ],
        "apply": [
            ex("¿Cuántas líneas de simetría tiene la letra E mayúscula de imprenta?", "1", "Solo una línea horizontal por el medio la deja en dos partes que coinciden."),
            ex("De las letras mayúsculas de imprenta A, H, M y T, ¿cuántas tienen exactamente 1 línea de simetría?", "3", "A, M y T tienen 1; la H tiene 2."),
            ex("Un hexágono regular tiene tantas líneas de simetría como lados. ¿Cuántas tiene?", "6", "Un hexágono tiene 6 lados."),
        ],
        "reason": [
            ex("Gabo pega un círculo pequeño al lado de un círculo grande y dice que la figura tiene muchas líneas de simetría. ¿Tiene razón?", "No; solo queda 1: la que pasa por los dos centros", "Los círculos no son iguales a ambos lados de las otras líneas."),
            ex("Camila une dos cuadrados iguales por un lado y forma un rectángulo. ¿Cuántas líneas de simetría tiene?", "2", "Es un rectángulo que no es cuadrado."),
        ],
        "challenge": [
            ex("Una figura tiene 3 líneas de simetría. ¿Cuál de estas puede ser: triángulo con tres lados iguales, rectángulo (no cuadrado) o cuadrado?", "El triángulo con tres lados iguales", "El rectángulo tiene 2 y el cuadrado 4."),
            ex("Una figura tiene 4 líneas de simetría. ¿Cuál de estas puede ser: cuadrado, rectángulo (no cuadrado) o triángulo con tres lados iguales?", "El cuadrado", "El rectángulo tiene 2 y el triángulo 3."),
        ],
    },
    context=[ex("Para decorar una guirnalda doblas la hoja, dibujas la mitad de una mariposa junto al doblez y copias al otro lado. Si queda bien, ¿cuántas líneas de simetría tiene la mariposa?", "1", "Solo el doblez la divide en dos mitades que coinciden.")],
    selfcheck=[
        ex("Un cuadrado se divide por una diagonal. ¿Esa diagonal es línea de simetría?", "Sí", "Los dos triángulos coinciden al doblar."),
        ex("¿Cuántas líneas de simetría tiene un cuadrado?", "4", "Dos por puntos medios y dos diagonales."),
        ex("¿Una figura puede tener más de una línea de simetría?", "Sí", "El cuadrado tiene 4."),
    ],
    open_task=task(
        "Diseña dos figuras simétricas en papel cuadriculado: una con una sola línea de simetría (por ejemplo, un triángulo con dos lados iguales o una letra T) y otra con dos o más líneas (por ejemplo, un cuadrado o una H). Dibuja las líneas de simetría y escribe cuántas tiene cada una.",
        "Triángulo con dos lados iguales: 1 línea. Cuadrado: 4 líneas.",
        ["crea una figura con 1 línea", "crea una figura con 2 o más líneas", "dibuja las líneas y las cuenta"],
        ["dos diseños", "cantidad de líneas"],
        ["contar mal las diagonales", "no comprobar con doblez"],
        "Pide que doble o refleje la figura para comprobar. Reconoce que el diseño cumple lo pedido.",
    ),
    reinforce="Con una hoja doblada, dibuja media mariposa pegada al doblez y copia la otra mitad. Revisa doblando.",
    extend="Diseña una figura con exactamente 3 líneas de simetría y compruébalo.",
)
