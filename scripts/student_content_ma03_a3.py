"""Student material for 3.º básico Matemática, OA 04 (cálculo mental aditivo hasta 100) y OA 05 (valor posicional hasta 1.000)."""
from __future__ import annotations

from student_content_ma03_a import task
from student_lessons import arith, ex, register

OA4 = "MA03 OA 04"
OA5 = "MA03 OA 05"


def cdu(c: int, d: int, u: int) -> str:
    return f"C = {c}, D = {d}, U = {u}"


# ---------------------------------------------------------------- OA 04
register(
    OA4, 1,
    materials="Lápiz y cuaderno. Los números están escritos en cada ejercicio. Puedes usar dibujos de ▮ (decenas) y ● (unidades) para apoyarte.",
    use="Aprenderé a sumar y restar de memoria separando los números en decenas y unidades. Sirve para calcular rápido sin escribir una cuenta larga.",
    prior=["Sé sumar y restar con números hasta 100.", "Sé que 47 son 4 decenas y 7 unidades."],
    explain=[
        "Descomponer un número es separarlo en decenas y unidades. El 47 es 40 + 7. Para sumar 47 + 25 puedes separar los dos: 40 + 7 y 20 + 5. Luego sumas las decenas, 40 + 20 = 60, y las unidades, 7 + 5 = 12.",
        "Al final juntas los resultados: 60 + 12 = 72. Fíjate que las unidades pueden dar más de 10, como 12, y entonces hay que sumar esa parte completa. Esta estrategia también sirve para restar: 85 − 32 es 80 − 30 = 50 y 5 − 2 = 3, o sea 53.",
        "La resta por partes es fácil cuando cada cifra de las unidades del primer número es mayor o igual que la que se resta. Si no, usa otra estrategia de esta unidad. Para comprobar, haz el cálculo de otra forma o estima: 47 + 25 es cerca de 50 + 25 = 75, y 72 es parecido.",
    ],
    vocab=[("descomponer", "separar un número en partes, como 47 = 40 + 7"), ("cálculo mental", "calcular de memoria, pensando"), ("estrategia", "manera de resolver un cálculo"), ("sumandos", "los números que se suman"), ("estimar", "calcular una respuesta cercana sin hacerlo exacto")],
    worked=[
        {"title": "Sumar por descomposición", "problem": "Calcula mentalmente 47 + 25.", "steps": ["Separo en decenas y unidades: 40 + 7 y 20 + 5.", "Sumo las decenas: 40 + 20 = 60.", "Sumo las unidades: 7 + 5 = 12.", "Junto los resultados: 60 + 12 = 72."], "answer": "72"},
        {"title": "Restar por descomposición", "problem": "Calcula mentalmente 85 − 32.", "steps": ["Separo: 85 = 80 + 5 y 32 = 30 + 2.", "Resto las decenas: 80 − 30 = 50.", "Resto las unidades: 5 − 2 = 3.", "Junto: 50 + 3 = 53."], "answer": "53"},
    ],
    mistakes=[
        {"wrong": "Calcular 47 + 25 como 60 y 12, y escribir 6012.", "why": "Se pegan los resultados en vez de sumarlos.", "fix": "Después de sumar por partes, suma los resultados: 60 + 12 = 72."},
        {"wrong": "Restar 62 − 28 como 60 − 20 = 40 y 2 − 8 = 6.", "why": "Se resta la cifra menor de la mayor en las unidades.", "fix": "Si no se puede restar 8 de 2, usa otra estrategia. Aquí no conviene descomponer."},
    ],
    tiers={
        "recovery": [
            ex("Descompón 46 en decenas y unidades.", "40 + 6", "46 tiene 4 decenas, que son 40, y 6 unidades."),
            arith("Calcula 34 + 25 separando decenas y unidades.", "34+25", "30 + 20 = 50 y 4 + 5 = 9, y 50 + 9 = 59."),
            arith("Calcula 52 + 17 por partes.", "52+17", "50 + 10 = 60 y 2 + 7 = 9, y 60 + 9 = 69."),
        ],
        "understand": [
            ex("Para sumar 47 + 25, ¿cuánto suman las decenas 40 + 20 y cuánto las unidades 7 + 5?", "60 y 12", "40 + 20 = 60 y 7 + 5 = 12; luego 60 + 12 = 72."),
            ex("¿Es correcto decir que 38 + 24 = 50 + 12?", "Sí, ambos son 62", "30 + 20 = 50 y 8 + 4 = 12; 50 + 12 = 62."),
            ex("Para restar 85 − 32, ¿qué se resta en las decenas y qué en las unidades?", "80 − 30 y 5 − 2", "Se separa 85 = 80 + 5 y 32 = 30 + 2; el resultado es 53."),
        ],
        "apply": [
            arith("Ema tiene 48 stickers y gana 35 más. ¿Cuántos tiene en total?", "48+35", "40 + 30 = 70 y 8 + 5 = 13, entonces 70 + 13."),
            arith("Un bus lleva 76 pasajeros y bajan 43. ¿Cuántos pasajeros quedan?", "76-43", "70 − 40 = 30 y 6 − 3 = 3, entonces 30 + 3."),
            arith("Sin escribir una cuenta larga, ¿cuánto es 57 + 36?", "57+36", "50 + 30 = 80 y 7 + 6 = 13, entonces 80 + 13."),
        ],
        "reason": [
            ex("Luis calculó 47 + 25 así: 40 + 20 = 60 y 7 + 5 = 12, y escribió 612. ¿Qué le faltó hacer?", "Sumar 60 + 12 = 72", "Los dos resultados se suman, no se escriben pegados."),
            ex("Ana calcula 56 + 27 como 50 + 20 = 70, 6 + 7 = 13 y 70 + 13. Beto calcula 56 + 20 = 76 y 76 + 7. ¿Ambos llegan al mismo número?", "Sí, 83", "70 + 13 = 83 y 76 + 7 = 83."),
        ],
        "challenge": [
            arith("Descompón solo el segundo sumando: 64 + 29 = 64 + 20 + 9. ¿Cuánto da?", "64+20+9", "64 + 20 = 84 y 84 + 9 = 93."),
            arith("Calcula 99 − 45 por partes: decenas con decenas y unidades con unidades.", "99-45", "90 − 40 = 50 y 9 − 5 = 4."),
        ],
    },
    context=[arith("En un colegio hay 45 niñas y 37 niños. ¿Cuántos estudiantes hay en total?", "45+37", "40 + 30 = 70 y 5 + 7 = 12.")],
    selfcheck=[
        arith("¿Cuánto es 23 + 14?", "23+14", "20 + 10 = 30 y 3 + 4 = 7."),
        arith("¿Cuánto es 68 − 25?", "68-25", "60 − 20 = 40 y 8 − 5 = 3."),
        ex("Separando decenas y unidades, ¿cuánto es 35 + 27?", "62", "30 + 20 = 50 y 5 + 7 = 12; 50 + 12 = 62."),
    ],
    open_task=task(
        "Resuelve mentalmente estas tres operaciones separando decenas y unidades: 43 + 28, 36 + 57 y 79 − 34. Escribe las partes que usaste para cada una.",
        "43 + 28: 40 + 20 = 60, 3 + 8 = 11, 60 + 11 = 71. 36 + 57: 30 + 50 = 80, 6 + 7 = 13, 80 + 13 = 93. 79 − 34: 70 − 30 = 40, 9 − 4 = 5, 40 + 5 = 45.",
        ["resuelve las tres operaciones", "muestra las partes de cada una", "suma o resta al final los resultados"],
        ["cálculos escritos en el cuaderno", "partes de cada cálculo"],
        ["pegar los resultados", "restar cifras al revés"],
        "Reconoce las partes bien separadas y pide explicar en voz alta cómo juntó los resultados; si hay error, que use dibujos de ▮ y ●.",
    ),
    reinforce="Escribe 5 sumas de dos números de dos cifras, resuélvelas separando decenas y unidades y revisa con una calculadora si hay una en tu casa.",
    extend="Resuelve 68 + 29 separando en decenas y unidades. Las unidades suman más de 10: explica cómo juntaste los resultados.",
)

register(
    OA4, 2,
    materials="Lápiz, cuaderno y una recta numérica dibujada con marcas de 10 en 10 hasta 100. Los números están escritos en cada ejercicio.",
    use="Aprenderé a completar la decena más cercana para sumar y restar rápido. Sirve para calcular 38 + 7 pensando en 40.",
    prior=["Sé contar de 10 en 10 hasta 100.", "Sé separar un número en decenas y unidades."],
    explain=[
        "Completar la decena es usar un paso fácil: llegar a un número terminado en 0. Para sumar 38 + 7, primero ves cuánto falta para 40. Faltan 2. Entonces separas el 7 en 2 y 5: 38 + 2 = 40 y luego 40 + 5 = 45.",
        "Funciona también con números más grandes. En 56 + 19, a 56 le faltan 4 para 60. Separas 19 en 4 y 15: 56 + 4 = 60 y 60 + 15 = 75. Cada paso es fácil porque terminas en una decena.",
        "En una resta haces lo mismo hacia atrás. Para 62 − 5, primero baja hasta 60 restando 2: 62 − 2 = 60. Luego te faltan 3 por restar: 60 − 3 = 57. Dibuja saltos en una recta si lo necesitas.",
    ],
    vocab=[("decena más cercana", "número terminado en 0 al que llego con un paso corto"), ("completar", "agregar lo que falta para llegar a otro número"), ("salto", "paso en la recta numérica"), ("separar", "dividir un número en dos partes que lo forman"), ("hacia atrás", "restar en la recta numérica")],
    worked=[
        {"title": "Completar hacia arriba", "problem": "Calcula 38 + 7 completando la decena.", "steps": ["Para llegar a 40, a 38 le faltan 2.", "Separo 7 en 2 y 5.", "38 + 2 = 40 y 40 + 5 = 45."], "answer": "45"},
        {"title": "Completar hacia abajo", "problem": "Calcula 62 − 5 llegando primero a 60.", "steps": ["De 62 a 60 hay que restar 2.", "5 es 2 + 3; ya resté 2 y faltan 3.", "60 − 3 = 57."], "answer": "57"},
    ],
    mistakes=[
        {"wrong": "Calcular 38 + 7 como 38 + 2 = 40 y 40 + 7 = 47.", "why": "Se vuelve a sumar el 7 completo después de haber usado 2.", "fix": "Si usaste 2 del 7, quedan 5 por sumar: 40 + 5 = 45."},
        {"wrong": "Calcular 62 − 5 como 62 − 2 = 60 y 60 − 2 = 58.", "why": "Se resta otra vez 2 y no lo que falta del 5.", "fix": "Del 5 ya restaste 2; falta restar 3: 60 − 3 = 57."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuánto falta para llegar a la decena siguiente desde 38?", "2", "38 + 2 = 40."),
            ex("Desde 76, ¿cuánto falta para llegar a 80?", "4", "76 + 4 = 80."),
            arith("Calcula 38 + 7 pasando primero por 40.", "38+7", "38 + 2 = 40 y 40 + 5 = 45."),
        ],
        "understand": [
            ex("Para sumar 47 + 6, ¿cómo separas el 6 para completar la decena?", "3 y 3", "47 + 3 = 50 y 50 + 3 = 53."),
            ex("¿Cuál es la siguiente decena, hacia arriba, que viene después de 64?", "70", "Después de 64 la primera decena que se alcanza es 70."),
            ex("Para restar 62 − 5 se resta primero 2 y se llega a 60. ¿Cuánto falta restar?", "3", "5 − 2 = 3, entonces 60 − 3 = 57."),
        ],
        "apply": [
            arith("Calcula 56 + 19 completando la decena de 56.", "56+19", "56 + 4 = 60 y 60 + 15 = 75."),
            arith("Una pastelería tiene 73 galletas y vende 8. ¿Cuántas quedan?", "73-8", "73 − 3 = 70 y 70 − 5 = 65."),
            ex("¿Cuánto es 84 + 11 si llegas primero a 90?", "95", "84 + 6 = 90 y 90 + 5 = 95."),
        ],
        "reason": [
            ex("Marcos calculó 38 + 7 así: 38 + 2 = 40 y 40 + 7 = 47. ¿Qué error cometió y cuál es el resultado?", "Sumó 7 en vez de 5; el resultado es 45", "Ya usó 2 del 7, entonces quedan 5 por sumar."),
            ex("Dos formas de calcular 49 + 23: A) 49 + 1 = 50 y 50 + 22; B) 40 + 20 = 60 y 9 + 3 = 12. ¿Cuál completa la decena?", "A", "En A se llega a 50, que es una decena exacta."),
        ],
        "challenge": [
            arith("Calcula 69 + 28 llegando primero a 70.", "69+28", "69 + 1 = 70 y 70 + 27 = 97."),
            arith("Calcula 91 − 6 pasando por 90.", "91-6", "91 − 1 = 90 y 90 − 5 = 85."),
        ],
    },
    context=[arith("En una fila hay 47 niños y llegan 8 más. ¿Cuántos niños hay ahora?", "47+8", "47 + 3 = 50 y 50 + 5 = 55.")],
    selfcheck=[
        arith("¿Cuánto es 27 + 5?", "27+5", "27 + 3 = 30 y 30 + 2 = 32."),
        ex("¿Cuánto falta para llegar a 50 desde 46?", "4", "46 + 4 = 50."),
        arith("¿Cuánto es 83 − 4?", "83-4", "83 − 3 = 80 y 80 − 1 = 79."),
    ],
    open_task=task(
        "Resuelve completando la decena: 28 + 6, 65 + 17 y 71 − 8. Para cada una escribe los dos pasos que diste y dibuja los saltos en una recta numérica.",
        "28 + 6: 28 + 2 = 30 y 30 + 4 = 34. 65 + 17: 65 + 5 = 70 y 70 + 12 = 82. 71 − 8: 71 − 1 = 70 y 70 − 7 = 63. En la recta dibujo un salto hasta la decena y otro con lo que falta.",
        ["resuelve las tres operaciones", "escribe los dos pasos de cada una", "pasa por una decena exacta", "dibuja los saltos"],
        ["cálculos escritos", "rectas con saltos dibujados"],
        ["repetir el número completo después de completar", "no dibujar el salto hasta la decena"],
        "Reconoce los pasos y pregunta de dónde sacó los números de cada salto; si hay error, que revise con tapas cuánto falta para la decena.",
    ),
    reinforce="Con una recta de 10 en 10, practica hasta la decena: de 18, 27, 36 y 45 escribe cuánto falta para la siguiente decena.",
    extend="Calcula 67 + 9 y 67 + 19 completando la decena de 67. ¿Qué parecido ves entre los dos pasos y los dos resultados?",
)

register(
    OA4, 3,
    materials="Lápiz y cuaderno. Los números están escritos en cada ejercicio. Puedes dibujar dos filas de ● iguales para ver un doble.",
    use="Aprenderé a usar dobles y casi dobles para sumar de memoria. Sirve para calcular rápido cuando los dos números son iguales o casi iguales.",
    prior=["Sé sumar números de dos cifras.", "Sé que el doble de un número es sumarlo consigo mismo."],
    explain=[
        "Un doble es sumar un número consigo mismo: 8 + 8 = 16, y 25 + 25 = 50. Es fácil de recordar. Para dobles de dos cifras, dobla las decenas y dobla las unidades: el doble de 35 es 30 + 30 = 60 y 5 + 5 = 10, o sea 70.",
        "Un casi doble es una suma de números seguidos o muy cerca, como 35 + 36. Usas el doble de 35, que es 70, y agregas 1 más: 71. Si el casi doble es 24 + 25, el doble de 24 es 48 y sumas 1: 49.",
        "A veces el casi doble tiene dos números separados por 2, como 38 + 40. Piensa en 40 + 40 = 80 y quita 2: 78. Revisa que el resultado quede cerca del doble. Si no, algo salió mal.",
    ],
    vocab=[("doble", "un número sumado consigo mismo"), ("casi doble", "suma de dos números muy cercanos entre sí"), ("par de números seguidos", "dos números que se diferencian en 1"), ("estrategia", "manera de resolver un cálculo"), ("doblar", "calcular el doble de un número")],
    worked=[
        {"title": "Un doble de dos cifras", "problem": "Calcula 35 + 35.", "steps": ["Doble de las decenas: 30 + 30 = 60.", "Doble de las unidades: 5 + 5 = 10.", "Junto: 60 + 10 = 70."], "answer": "70"},
        {"title": "Un casi doble", "problem": "Calcula 35 + 36 usando un doble.", "steps": ["36 es 35 + 1.", "Entonces 35 + 36 = 35 + 35 + 1.", "35 + 35 = 70 y 70 + 1 = 71."], "answer": "71"},
    ],
    mistakes=[
        {"wrong": "Decir que 26 + 27 = 52 porque el doble de 26 es 52.", "why": "Se olvida sumar el 1 que sobra.", "fix": "27 es 26 + 1, entonces 26 + 27 = 52 + 1 = 53."},
        {"wrong": "Calcular 38 + 40 como 80 + 2 = 82.", "why": "Se suma lo que se debe quitar.", "fix": "Si usas 40 + 40 = 80, como 38 es 2 menos que 40, resta 2: 78."},
    ],
    tiers={
        "recovery": [
            ex("El doble de 8 es 8 + 8 = 16. ¿Cuál es el doble de 15?", "30", "15 + 15 = 30."),
            ex("¿Cuál es el doble de 40?", "80", "40 + 40 = 80."),
            ex("Calcula 7 + 8 usando 7 + 7.", "15", "7 + 7 = 14 y se suma 1 más."),
        ],
        "understand": [
            ex("35 + 36 es un casi doble. ¿De qué doble parte y cuánto se agrega?", "Del doble de 35 y se agrega 1", "36 es 35 + 1."),
            ex("¿Cuál es un casi doble: 25 + 26 o 25 + 30?", "25 + 26", "25 y 26 son seguidos; 25 y 30 se diferencian en 5."),
            ex("Si 30 + 30 = 60, ¿cuánto es 30 + 31?", "61", "31 es 30 + 1, entonces se agrega 1 al doble."),
        ],
        "apply": [
            arith("Camila lee 24 páginas el lunes y 25 el martes. ¿Cuántas páginas leyó?", "24+25", "El doble de 24 es 48 y se agrega 1."),
            arith("Una caja tiene 38 pelotas y otra caja tiene 38. ¿Cuántas hay en total?", "38+38", "30 + 30 = 60 y 8 + 8 = 16."),
            ex("Usando un casi doble, ¿cuánto es 46 + 47?", "93", "46 + 46 = 92 y se agrega 1."),
        ],
        "reason": [
            ex("Ana dice que 26 + 27 = 52 porque el doble de 26 es 52. ¿Qué le falta?", "Sumar 1; el resultado es 53", "27 es 26 + 1."),
            ex("¿Se puede usar el doble de 40 para calcular 40 + 38? Explica.", "Sí, el resultado es 78", "40 + 40 = 80 y 38 es 2 menos que 40, entonces 80 − 2 = 78."),
        ],
        "challenge": [
            ex("Calcula 49 + 51 usando el doble de 50.", "100", "49 es 1 menos que 50 y 51 es 1 más, entonces 50 + 50 = 100."),
            ex("¿Qué número sumado consigo mismo da 94?", "47", "40 + 40 = 80 y 7 + 7 = 14, y 80 + 14 = 94."),
        ],
    },
    context=[arith("Un panadero hornea 36 panes en una bandeja y 37 panes en otra. ¿Cuántos panes hornea en total?", "36+37", "El doble de 36 es 72 y se agrega 1.")],
    selfcheck=[
        ex("¿Cuál es el doble de 25?", "50", "25 + 25 = 50."),
        ex("¿Cuánto es 17 + 18 usando un casi doble?", "35", "17 + 17 = 34 y se agrega 1."),
        ex("¿Cuánto es 40 + 39 usando un casi doble?", "79", "40 + 40 = 80 y se quita 1."),
    ],
    open_task=task(
        "Resuelve con dobles y casi dobles: 27 + 27, 44 + 45 y 50 + 48. Escribe de qué doble partiste en cada caso y si sumaste o quitaste algo.",
        "27 + 27 = 54 (20 + 20 = 40 y 7 + 7 = 14). 44 + 45: parto de 44 + 44 = 88 y sumo 1, da 89. 50 + 48: parto de 50 + 50 = 100 y quito 2, da 98.",
        ["resuelve las tres operaciones", "nombra el doble del que partió", "dice si suma o quita", "los resultados quedan cerca del doble"],
        ["cálculos escritos", "frases con el doble elegido"],
        ["no sumar el 1 que sobra", "sumar en vez de quitar cuando el número es menor"],
        "Reconoce que usó el doble correcto y pregunta por qué sumó o quitó; si hay error, que dibuje dos filas de puntos y vea la diferencia.",
    ),
    reinforce="Haz una tabla con los dobles de 5, 10, 15, 20, 25, 30, 35 y 40 y apréndelos de memoria.",
    extend="Calcula 33 + 35 de dos maneras: con el doble de 33 y con el doble de 35. ¿Obtienes el mismo resultado?",
)

register(
    OA4, 4,
    materials="Lápiz, cuaderno y una recta numérica dibujada de 0 a 100. Los números están escritos en cada ejercicio.",
    use="Aprenderé a resolver una resta pensando en una suma que falta. Sirve para saber cuánto falta para llegar de un número a otro.",
    prior=["Sé que restar es quitar y también encontrar lo que falta.", "Sé completar hasta la decena más cercana."],
    explain=[
        "Una resta se puede pensar como una suma. En 83 − 76 pregunta: ¿qué número sumo a 76 para llegar a 83? Parte en 76 y cuenta hacia arriba: 76 + 4 = 80 y 80 + 3 = 83. Sumaste 4 y 3, o sea 7. Entonces 83 − 76 = 7.",
        "Esta estrategia es muy útil cuando los dos números están cerca. Para 100 − 87, cuentas desde 87 hasta 100: 87 + 3 = 90 y 90 + 10 = 100. Son 13. No necesitas hacer una cuenta larga.",
        "Para comprobar, suma el resultado al número menor: 76 + 7 = 83. Si llegas al número mayor, la resta está bien. Eso es porque restar y sumar se deshacen entre sí.",
    ],
    vocab=[("diferencia", "lo que falta entre dos números, resultado de una resta"), ("completar", "agregar lo que falta para llegar a un número"), ("sumar para restar", "buscar qué número sumo para llegar al mayor"), ("comprobar", "revisar si un resultado es correcto"), ("hacia arriba", "contar sumando en la recta numérica")],
    worked=[
        {"title": "Restar contando hacia arriba", "problem": "Calcula 83 − 76 sumando.", "steps": ["Parto en 76 y quiero llegar a 83.", "76 + 4 = 80.", "80 + 3 = 83.", "Sumé 4 + 3 = 7."], "answer": "7"},
        {"title": "Cuánto falta para 100", "problem": "Un libro tiene 100 páginas y ya leí 87. ¿Cuántas faltan?", "steps": ["Parto en 87 y quiero llegar a 100.", "87 + 3 = 90.", "90 + 10 = 100.", "Sumé 3 + 10 = 13."], "answer": "13 páginas"},
    ],
    mistakes=[
        {"wrong": "Calcular 83 − 76 y responder 13.", "why": "Se resta la cifra menor de la mayor en cada lugar: 8 − 7 = 1 y 6 − 3 = 3.", "fix": "Cuenta hacia arriba desde 76 hasta 83: son 7."},
        {"wrong": "Contar desde 76 hasta 83 y decir 8.", "why": "Se cuenta también el número de partida.", "fix": "Los saltos son los que sumas: 4 + 3 = 7. El número de partida no se cuenta."},
    ],
    tiers={
        "recovery": [
            ex("Completa: 76 + __ = 83.", "7", "76 + 4 = 80 y 80 + 3 = 83; 4 + 3 = 7."),
            ex("¿Cuánto le falta a 45 para llegar a 50?", "5", "45 + 5 = 50."),
            ex("Para calcular 52 − 48, ¿qué número se suma a 48 para llegar a 52?", "4", "48 + 2 = 50 y 50 + 2 = 52."),
        ],
        "understand": [
            ex("La resta 90 − 67 se puede resolver con 67 + __ = 90. ¿Qué número va?", "23", "67 + 3 = 70 y 70 + 20 = 90; 3 + 20 = 23."),
            ex("¿Qué resta corresponde a 38 + __ = 61: 61 − 38 o 38 − 61?", "61 − 38", "Se busca lo que falta de 38 para llegar a 61."),
            ex("En 82 − 79 los números están muy cerca. ¿Conviene contar hacia arriba desde 79? ¿Cuánto es?", "Sí; 3", "79 + 1 = 80 y 80 + 2 = 82; 1 + 2 = 3."),
        ],
        "apply": [
            arith("Un libro tiene 100 páginas y ya leí 87. ¿Cuántas páginas me faltan?", "100-87", "87 + 3 = 90 y 90 + 10 = 100."),
            arith("Hay 91 invitados y ya llegaron 85. ¿Cuántos faltan por llegar?", "91-85", "85 + 6 = 91."),
            ex("Calcula 72 − 58 sumando desde 58 hasta 72.", "14", "58 + 2 = 60 y 60 + 12 = 72; 2 + 12 = 14."),
        ],
        "reason": [
            ex("Sofía no sabe cuánto es 63 − 59. ¿Cuál es el resultado y cómo lo puede ver sumando desde 59?", "4; 59 + 1 = 60 y 60 + 3 = 63", "1 + 3 = 4."),
            ex("Tomás dice que 100 − 37 es 63 porque 37 + 63 = 100. ¿Tiene razón?", "Sí", "Si 37 + 63 = 100, falta 63 para llegar a 100."),
        ],
        "challenge": [
            ex("Calcula 95 − 68 sumando hasta 70 y luego hasta 95.", "27", "68 + 2 = 70 y 70 + 25 = 95; 2 + 25 = 27."),
            ex("En un tren viajaban 88 personas. En una estación bajaron algunas y quedaron 59. ¿Cuántas bajaron?", "29", "59 + 1 = 60 y 60 + 28 = 88; 1 + 28 = 29."),
        ],
    },
    context=[arith("Sol tiene 67 stickers y quiere llegar a 90 para completar su álbum. ¿Cuántos le faltan?", "90-67", "67 + 3 = 70 y 70 + 20 = 90.")],
    selfcheck=[
        ex("Completa: 45 + __ = 60.", "15", "45 + 5 = 50 y 50 + 10 = 60."),
        arith("¿Cuánto es 100 − 94?", "100-94", "94 + 6 = 100."),
        arith("¿Cuánto es 72 − 68?", "72-68", "68 + 4 = 72."),
    ],
    open_task=task(
        "Resuelve contando hacia arriba estas tres restas: 81 − 76, 100 − 63 y 94 − 58. Para cada una, dibuja los saltos en una recta y escribe cuánto sumaste en total.",
        "81 − 76: 76 + 4 = 80 y 80 + 1 = 81, suma 5. 100 − 63: 63 + 7 = 70 y 70 + 30 = 100, suma 37. 94 − 58: 58 + 2 = 60 y 60 + 34 = 94, suma 36.",
        ["resuelve las tres restas", "dibuja los saltos en una recta", "suma bien los saltos", "comprueba sumando al número menor"],
        ["cálculos escritos", "rectas con saltos dibujados"],
        ["contar también el número de partida", "restar cifra por cifra sin cuidado"],
        "Reconoce los saltos y pide comprobar sumando el resultado al número menor; si hay error, que cuente con tapas cuánto falta.",
    ),
    reinforce="Con 100 tapas o una tabla del 100, practica cuánto falta para llegar a 100 desde 90, 75, 62, 48 y 31.",
    extend="Resuelve 100 − 38 de dos maneras: contando hacia arriba y restando por partes. ¿Cuál te pareció más fácil?",
)

register(
    OA4, 5,
    materials="Lápiz y cuaderno. Los números están escritos en cada ejercicio. Puedes marcar con un color los sumandos que se juntan.",
    use="Aprenderé a elegir qué sumandos juntar primero para que el cálculo sea más fácil. Sirve para sumar tres o más números de memoria.",
    prior=["Sé sumar números de dos cifras.", "Sé que al sumar dos números el orden no cambia el resultado."],
    explain=[
        "Cuando sumas tres números, puedes juntar primero los que quieras. 27 + 36 + 13 es lo mismo que (27 + 13) + 36. Como 27 + 13 = 40, queda 40 + 36 = 76. Esto se llama asociar los sumandos.",
        "Busca primero los que forman una decena exacta, como 8 y 2, 27 y 13, o 45 y 5. Esos son fáciles de sumar y dejan un número redondo, que es cómodo para seguir sumando. El resultado final es siempre el mismo.",
        "También puedes cambiar el orden de los sumandos, porque la suma no cambia: 12 + 8 + 30 es igual a 30 + 12 + 8. Marca con un círculo los sumandos que juntas y escribe el resultado parcial para no perderte.",
    ],
    vocab=[("asociar", "elegir qué sumandos juntar primero"), ("sumandos", "los números que se suman"), ("resultado parcial", "resultado de una parte del cálculo"), ("decena exacta", "número terminado en 0, como 40 o 90"), ("orden", "posición en que se escriben los sumandos")],
    worked=[
        {"title": "Juntar los que forman una decena", "problem": "Calcula 27 + 36 + 13.", "steps": ["Busco dos sumandos que formen una decena: 27 y 13.", "27 + 13 = 40.", "Sumo lo que queda: 40 + 36 = 76."], "answer": "76"},
        {"title": "Cuatro sumandos", "problem": "Calcula 17 + 28 + 3 + 12.", "steps": ["Junto 17 y 3: 17 + 3 = 20.", "Junto 28 y 12: 28 + 12 = 40.", "Sumo los dos resultados: 20 + 40 = 60."], "answer": "60"},
    ],
    mistakes=[
        {"wrong": "Calcular 27 + 36 + 13 como 27 + 13 = 40 y responder 40.", "why": "Se olvida sumar el sumando que quedó afuera.", "fix": "Después de juntar 27 + 13, suma lo que queda: 40 + 36 = 76."},
        {"wrong": "Pensar que juntar los sumandos en otro orden cambia el resultado.", "why": "Se cree que el resultado depende del orden.", "fix": "La suma no cambia con el orden ni con la forma de juntar: 27 + 36 + 13 siempre da 76."},
    ],
    tiers={
        "recovery": [
            ex("En 8 + 5 + 2, ¿qué dos sumandos se juntan para formar 10?", "8 y 2", "8 + 2 = 10."),
            arith("Calcula 15 + 5 + 20 juntando primero 15 y 5.", "15+5+20", "15 + 5 = 20 y 20 + 20 = 40."),
            arith("Calcula 6 + 14 + 9 juntando primero 6 y 14.", "6+14+9", "6 + 14 = 20 y 20 + 9 = 29."),
        ],
        "understand": [
            ex("En 38 + 45 + 2, ¿cuál se calcula más fácil primero: 38 + 45 o 38 + 2?", "38 + 2", "38 + 2 = 40 y 40 + 45 = 85."),
            ex("¿Es verdad que (23 + 7) + 18 = 23 + (7 + 18)?", "Sí; ambos dan 48", "30 + 18 = 48 y 23 + 25 = 48."),
            ex("¿Cambia el resultado si sumas 12 + 8 + 30 en otro orden?", "No; sigue siendo 50", "Cambiar el orden no cambia una suma."),
        ],
        "apply": [
            arith("Una profesora tiene 24 lápices rojos, 35 azules y 6 verdes. ¿Cuántos lápices hay?", "24+35+6", "24 + 6 = 30 y 30 + 35 = 65."),
            arith("Calcula 19 + 43 + 1 juntando primero lo que forma una decena.", "19+43+1", "19 + 1 = 20 y 20 + 43 = 63."),
            arith("Calcula 17 + 28 + 3 + 12 buscando decenas exactas.", "17+28+3+12", "17 + 3 = 20 y 28 + 12 = 40."),
        ],
        "reason": [
            ex("Tomás sumó 27 + 36 + 13 así: 27 + 36 = 63 y 63 + 13 = 76. ¿Qué forma más fácil había?", "Juntar primero 27 + 13 = 40 y luego 40 + 36", "27 y 13 forman una decena exacta; el resultado es el mismo, 76."),
            ex("Ana calcula 45 + 18 + 5 como 45 + (18 + 5) y Bea como 50 + 18. ¿Las dos llegan al mismo número?", "Sí, 68", "18 + 5 = 23 y 45 + 23 = 68; 45 + 5 = 50 y 50 + 18 = 68."),
        ],
        "challenge": [
            ex("¿Qué número falta en 36 + __ + 4 = 90?", "50", "36 + 4 = 40 y 40 + 50 = 90."),
            arith("Calcula 11 + 29 + 17 + 3 + 40 buscando decenas exactas.", "11+29+17+3+40", "11 + 29 = 40, 17 + 3 = 20 y 40 + 20 + 40."),
        ],
    },
    context=[arith("En una feria se venden 28 manzanas, 17 peras y 12 naranjas. ¿Cuántas frutas hay?", "28+17+12", "28 + 12 = 40 y 40 + 17.")],
    selfcheck=[
        arith("¿Cuánto es 9 + 4 + 1?", "9+4+1", "9 + 1 = 10 y 10 + 4."),
        ex("En 25 + 37 + 5, ¿qué dos sumandos conviene juntar primero?", "25 y 5", "25 + 5 = 30."),
        arith("¿Cuánto es 12 + 8 + 30?", "12+8+30", "12 + 8 = 20 y 20 + 30."),
    ],
    open_task=task(
        "Inventa y resuelve una suma de tres sumandos usando estos números: 14, 26, 38 y 22 (elige tres). Marca con un círculo los dos que juntas primero y explica por qué los elegiste.",
        "Elijo 14, 26 y 38. Junto 14 + 26 = 40, porque forman una decena exacta, y sumo 40 + 38 = 78.",
        ["elige tres de los cuatro números", "junta los que forman una decena", "escribe el resultado parcial", "explica la elección"],
        ["suma escrita en el cuaderno", "círculo y explicación"],
        ["olvidar el tercer sumando", "elegir sumandos sin un criterio"],
        "Reconoce la elección y pregunta si otro orden daría lo mismo; si hay error, que repita sumando de izquierda a derecha y compare.",
    ),
    reinforce="Con tarjetas 18, 7, 12, 3 y 40, junta las que forman decenas exactas y suma todas.",
    extend="Con los números 25, 15, 38 y 22, forma dos parejas que sumen decenas exactas y calcula el total.",
)

# ---------------------------------------------------------------- OA 05
register(
    OA5, 1,
    materials="Lápiz, cuaderno y, si quieres, 30 tapas. Usamos ▣ para una centena, ▮ para una decena y ● para una unidad.",
    use="Aprenderé que diez decenas forman una centena y diez unidades forman una decena. Sirve para saber cuánto vale cada lugar en un número de tres cifras.",
    prior=["Sé que 10 unidades forman una decena.", "Sé leer números de tres cifras."],
    explain=[
        "En nuestro sistema de numeración, diez piezas de un lugar forman una pieza del lugar siguiente. Diez unidades se cambian por una decena. Diez decenas se cambian por una centena. Una centena tiene 100 unidades.",
        "Imagina que tienes 10 palitos ▮, cada uno vale 10. Juntos valen 100, y puedes cambiarlos por un cuadrado ▣. Ese cambio se llama canje. Con 20 palitos harías 2 cuadrados, y con 30, 3 cuadrados.",
        "Si tienes 29 decenas, puedes cambiar 20 decenas por 2 centenas y te quedan 9 decenas. Entonces 29 decenas valen 2 centenas y 9 decenas, o sea 290. Lo importante es que el valor total no cambia cuando canjeas.",
    ],
    vocab=[("canje", "cambiar 10 piezas por 1 pieza del lugar siguiente"), ("valor posicional", "lo que vale una cifra según el lugar en que está"), ("centena", "100 unidades, o 10 decenas"), ("decena", "10 unidades"), ("sistema decimal", "forma de escribir los números con diez cifras, del 0 al 9")],
    worked=[
        {"title": "Canjear decenas por centenas", "problem": "Tienes 30 decenas. ¿Cuántas centenas son?", "steps": ["Cada 10 decenas se canjean por 1 centena.", "En 30 decenas hay 3 grupos de 10.", "Entonces son 3 centenas."], "answer": "3 centenas"},
        {"title": "Decenas que sobran", "problem": "Tienes 29 decenas. ¿Cuántas centenas completas hay y cuántas decenas sobran?", "steps": ["Formo grupos de 10 decenas: 10 + 10 = 20.", "Con 20 decenas hago 2 centenas.", "Sobran 29 − 20 = 9 decenas."], "answer": "2 centenas y 9 decenas"},
    ],
    mistakes=[
        {"wrong": "Decir que 10 decenas son 10.", "why": "Se cuentan las decenas como si fueran unidades.", "fix": "Cada decena vale 10, entonces 10 decenas valen 100."},
        {"wrong": "Cambiar 10 unidades por 1 centena.", "why": "Se confunde el lugar al que se canjea.", "fix": "10 unidades se cambian por 1 decena; 10 decenas se cambian por 1 centena."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas decenas forman 1 centena?", "10", "Cada decena vale 10 y 10 + 10 + ... diez veces es 100."),
            ex("Tienes 10 palitos ▮. ¿Por qué figura los puedes cambiar?", "Por 1 cuadrado ▣", "10 decenas forman 1 centena."),
            ex("Con 10 decenas y otras 10 decenas, ¿cuántas centenas hay?", "2", "Cada grupo de 10 decenas es 1 centena."),
        ],
        "understand": [
            ex("¿Cuántas unidades hay en 1 centena?", "100", "1 centena son 10 decenas y cada decena son 10 unidades."),
            ex("Tienes 9 decenas y cambias 10 unidades por 1 decena. ¿Cuántas decenas tienes ahora y por qué las puedes cambiar?", "10 decenas; por 1 centena", "9 + 1 = 10 decenas, que forman 1 centena."),
            ex("En 29 decenas, ¿cuántas centenas completas hay y cuántas decenas sobran?", "2 centenas y 9 decenas", "Se hacen 2 grupos de 10 decenas y sobran 9."),
        ],
        "apply": [
            ex("Hay 30 decenas. ¿Cuántas centenas son?", "3", "30 decenas son 3 grupos de 10 decenas."),
            ex("Una fábrica empaca clips en bolsas de 10. Hay 70 bolsas y cada 10 bolsas se juntan en una caja de 100. ¿Cuántas cajas se arman?", "7", "70 bolsas son 7 grupos de 10 bolsas."),
            ex("Cambia 120 unidades por decenas y centenas. ¿Cuántas de cada una?", "1 centena y 2 decenas", "120 = 100 + 20."),
        ],
        "reason": [
            ex("Ana dice que 10 decenas son 10. ¿Qué es lo correcto?", "Son 100", "Cada decena vale 10, entonces 10 decenas valen 100."),
            ex("Pablo tiene 8 decenas y recibe 2 decenas más. ¿Qué canje puede hacer?", "Cambiar las 10 decenas por 1 centena", "8 + 2 = 10 decenas forman 1 centena."),
        ],
        "challenge": [
            ex("¿Cuántas decenas hay en 3 centenas?", "30", "Cada centena tiene 10 decenas, entonces 3 centenas tienen 30."),
            ex("Tienes 14 decenas. ¿Cuántas centenas y decenas son?", "1 centena y 4 decenas", "10 decenas forman 1 centena y sobran 4."),
        ],
    },
    context=[ex("Hay 6 paquetes de 10 lápices y llegan 5 paquetes más. ¿Cuántos lápices hay y cuántas centenas y decenas son?", "110 lápices; 1 centena y 1 decena", "6 + 5 = 11 paquetes de 10; 10 paquetes forman 100 y queda 1 paquete.")],
    selfcheck=[
        ex("10 decenas, ¿cuántas centenas son?", "1", "10 decenas forman 1 centena."),
        ex("100 unidades, ¿cuántas decenas son?", "10", "Cada decena tiene 10 unidades."),
        ex("50 decenas, ¿qué número son?", "500", "50 decenas son 5 centenas."),
    ],
    open_task=task(
        "Con 25 tapas que representan decenas, arma grupos de 10 tapas para hacer centenas. Escribe cuántas centenas completas hiciste, cuántas decenas sobraron y qué número representa todo.",
        "Hago 2 grupos de 10 tapas, o sea 2 centenas. Sobran 5 tapas, 5 decenas. El número es 250.",
        ["forma grupos de 10 decenas", "dice cuántas centenas hizo", "dice cuántas decenas sobran", "escribe el número 250"],
        ["tapas agrupadas o dibujo", "frase escrita con el resultado"],
        ["decir que sobran 15", "no explicar el canje"],
        "Reconoce el canje bien hecho y pregunta qué valor tiene cada grupo; si hay error, que cuente de 10 en 10 las tapas.",
    ),
    reinforce="Dibuja 20 palitos ▮ y enciérralos de 10 en 10. ¿Cuántos cuadrados ▣ obtienes?",
    extend="Si tienes 47 decenas, ¿cuántas centenas y decenas son? ¿Qué número forman?",
)

register(
    OA5, 2,
    materials="Lápiz y una tabla de tres columnas C, D, U dibujada en el cuaderno. Los datos de cada ejercicio están escritos.",
    use="Aprenderé a leer y escribir números en una tabla de centenas, decenas y unidades. Sirve para ver de un vistazo qué vale cada cifra.",
    prior=["Sé que 10 unidades forman una decena y 10 decenas una centena.", "Sé leer números de tres cifras."],
    explain=[
        "La tabla CDU tiene tres columnas: C para centenas, D para decenas y U para unidades. Pones una cifra en cada columna. Si C = 4, D = 2 y U = 7, el número es 427. Se lee de izquierda a derecha, igual que un texto.",
        "Cada columna dice cuántas piezas de ese tipo hay. En 427 hay 4 centenas, 2 decenas y 7 unidades. Si una columna está vacía, se escribe 0. Para 705, C = 7, D = 0 y U = 5. El 0 indica que no hay decenas.",
        "La tabla ayuda a comparar y a no confundir lugares. Los números 717 y 771 usan las mismas cifras, pero en columnas distintas, y por eso son distintos. Lee siempre primero la columna C.",
    ],
    vocab=[("tabla CDU", "tabla con columnas de centenas, decenas y unidades"), ("columna", "espacio vertical de la tabla donde va una cifra"), ("C", "columna de las centenas"), ("D", "columna de las decenas"), ("U", "columna de las unidades")],
    worked=[
        {"title": "Leer la tabla", "problem": f"La tabla dice {cdu(4, 2, 7)}. ¿Qué número es?", "steps": ["Leo la columna C: 4 centenas.", "Leo la columna D: 2 decenas.", "Leo la columna U: 7 unidades.", "Junto las cifras en orden: 427."], "answer": "427"},
        {"title": "Escribir en la tabla", "problem": "Escribe 580 en una tabla CDU.", "steps": ["La primera cifra, 5, va en C.", "La segunda cifra, 8, va en D.", "La tercera cifra, 0, va en U."], "answer": cdu(5, 8, 0)},
    ],
    mistakes=[
        {"wrong": "Leer C = 5, D = 3, U = 2 como 235.", "why": "Se leen las columnas de derecha a izquierda.", "fix": "Se lee de izquierda a derecha, empezando por C: 532."},
        {"wrong": "Poner 58 en la tabla como C = 5, D = 8.", "why": "Se olvida que 58 tiene 0 centenas.", "fix": "58 es C = 0, D = 5, U = 8."},
    ],
    tiers={
        "recovery": [
            ex(f"En la tabla {cdu(4, 2, 7)}. ¿Qué número es?", "427", "Se leen C, D y U en orden."),
            ex("Escribe 270 en una tabla CDU.", cdu(2, 7, 0), "2 centenas, 7 decenas y 0 unidades."),
            ex(f"En la tabla {cdu(3, 0, 6)}. ¿Qué número es?", "306", "No hay decenas, entonces D vale 0."),
        ],
        "understand": [
            ex(f"En la tabla {cdu(2, 9, 1)}. ¿Cuántas decenas tiene el número?", "9", "La columna D dice cuántas decenas."),
            ex("En el número 705, ¿qué columna de la tabla CDU vale 0?", "La de las decenas", "705 = 7 centenas, 0 decenas y 5 unidades."),
            ex(f"¿Cuál tabla muestra 640: {cdu(6, 4, 0)} o {cdu(6, 0, 4)}?", cdu(6, 4, 0), "640 tiene 4 decenas y 0 unidades."),
        ],
        "apply": [
            ex("Escribe 392 en una tabla CDU.", cdu(3, 9, 2), "3 centenas, 9 decenas y 2 unidades."),
            ex(f"Una tabla muestra {cdu(7, 1, 7)} y otra {cdu(7, 7, 1)}. Escribe los dos números y di cuál es mayor.", "717 y 771; el mayor es 771", "Las centenas son iguales; las decenas son 1 y 7."),
            ex(f"En la tabla de 345 cambias U por 9. ¿Qué número queda?", "349", "C = 3, D = 4, U = 9."),
        ],
        "reason": [
            ex(f"Rosa puso {cdu(5, 3, 2)} y leyó 532. Juan dice que es 235. ¿Quién tiene razón?", "Rosa", "Se lee de izquierda a derecha: C, D, U."),
            ex("Una tabla tiene C = 4, D = ?, U = 6 y el número es 456. ¿Qué cifra va en D?", "5", "El número 456 tiene 5 decenas."),
        ],
        "challenge": [
            ex("¿Cuántos números tienen C = 3 y la misma cifra en D y en U? Escribe cuántos son.", "10", "Son 300, 311, 322, 333, 344, 355, 366, 377, 388 y 399."),
            ex("En una tabla C = 8 y la suma D + U es 3. ¿Cuál es el mayor número posible?", "830", "Con D = 3 y U = 0 se obtiene 830; con otras opciones sale menor."),
        ],
    },
    context=[ex(f"Un cuentakilómetros muestra {cdu(2, 0, 8)}. ¿Qué número se lee?", "208", "No hay decenas, entonces D vale 0.")],
    selfcheck=[
        ex(f"¿Qué número es {cdu(9, 1, 4)}?", "914", "Se leen C, D y U en orden."),
        ex("Escribe 450 en una tabla CDU.", cdu(4, 5, 0), "4 centenas, 5 decenas y 0 unidades."),
        ex("¿Qué columna de la tabla CDU está más a la izquierda?", "La de las centenas", "La primera columna es C."),
    ],
    open_task=task(
        "Dibuja una tabla CDU y escribe en ella estos números: 413, 650, 108 y 999. Después lee cada número en voz alta y escribe, junto a cada uno, cuántas centenas, decenas y unidades tiene.",
        "413: C = 4, D = 1, U = 3. 650: C = 6, D = 5, U = 0. 108: C = 1, D = 0, U = 8. 999: C = 9, D = 9, U = 9.",
        ["dibuja la tabla con las tres columnas", "pone cada cifra en su columna", "usa 0 donde corresponde", "dice cuántas centenas, decenas y unidades"],
        ["tabla dibujada", "números escritos en las columnas"],
        ["leer al revés", "olvidar el 0"],
        "Reconoce la tabla bien armada y pide leer cada número en voz alta; si hay error, que cuente las piezas ▣ ▮ ● de cada columna.",
    ),
    reinforce="Escribe en una tabla CDU los números 123, 321 y 213 y explica por qué son distintos.",
    extend="¿Cuál es el mayor número que cabe en la tabla CDU? ¿Y el menor de tres cifras?",
)

register(
    OA5, 3,
    materials="Lápiz y cuaderno. Todos los números están escritos en los ejercicios. Puedes dibujar la tabla CDU para ayudarte.",
    use="Aprenderé a explicar cuánto vale cada cifra de un número según el lugar donde está. Sirve para entender por qué 252 no tiene dos veces el mismo valor.",
    prior=["Sé armar números con centenas, decenas y unidades.", "Sé usar una tabla CDU."],
    explain=[
        "Una misma cifra puede valer cosas distintas según el lugar. En 575 hay dos cifras 5. La primera está en el lugar de las centenas y vale 500. La última está en las unidades y vale 5. El 7 está en las decenas y vale 70.",
        "Para saber el valor de una cifra, piensa cuánto vale su lugar: cada centena vale 100, cada decena vale 10 y cada unidad vale 1. Por eso 4 en las decenas vale 40, y 4 en las centenas vale 400. El cero vale 0 en cualquier lugar.",
        "Con eso puedes descomponer un número: 463 = 400 + 60 + 3. Cada sumando es el valor de una cifra. Para comprobar, suma los valores y debes obtener el número original.",
    ],
    vocab=[("valor posicional", "lo que vale una cifra según su lugar"), ("cifra", "uno de los dígitos del 0 al 9"), ("descomponer", "escribir un número como suma de los valores de sus cifras"), ("lugar", "posición de una cifra: unidades, decenas o centenas"), ("valor de la cifra", "la cantidad que representa en el número")],
    worked=[
        {"title": "Dos cifras iguales", "problem": "En 575, ¿cuánto vale cada cifra 5?", "steps": ["La primera cifra está en el lugar de las centenas: 5 centenas = 500.", "La última cifra está en las unidades: 5 unidades = 5.", "Las dos cifras son iguales, pero valen distinto."], "answer": "500 y 5"},
        {"title": "Descomponer", "problem": "Descompón 463 sumando los valores de sus cifras.", "steps": ["El 4 está en las centenas: vale 400.", "El 6 está en las decenas: vale 60.", "El 3 está en las unidades: vale 3."], "answer": "463 = 400 + 60 + 3"},
    ],
    mistakes=[
        {"wrong": "Decir que en 252 las dos cifras 2 valen lo mismo.", "why": "Se mira la cifra y no el lugar donde está.", "fix": "La primera vale 200 y la última vale 2."},
        {"wrong": "Decir que en 345 el 4 vale 4.", "why": "Se olvida que está en el lugar de las decenas.", "fix": "4 decenas valen 40."},
    ],
    tiers={
        "recovery": [
            ex("En 345, ¿qué valor tiene la cifra 4?", "40", "Está en las decenas: 4 decenas son 40."),
            ex("En 706, ¿qué valor tiene la cifra 7?", "700", "Está en las centenas: 7 centenas son 700."),
            ex("En 128, ¿cuánto vale la cifra 8?", "8", "Está en las unidades."),
        ],
        "understand": [
            ex("En 575 las dos cifras 5 valen distinto. ¿Cuánto vale cada una?", "500 y 5", "Una está en las centenas y la otra en las unidades."),
            ex("¿En cuál número el 9 vale 90: 904, 394 o 940?", "394", "Solo en 394 el 9 está en el lugar de las decenas."),
            ex("En 502, ¿cuál es el valor de la cifra 0?", "0", "El 0 está en las decenas y no hay decenas."),
        ],
        "apply": [
            ex("Descompón 463 como suma de los valores de sus cifras.", "400 + 60 + 3", "4 centenas, 6 decenas y 3 unidades."),
            ex("¿Qué número es 700 + 20 + 5?", "725", "7 centenas, 2 decenas y 5 unidades."),
            ex("En un número el 3 vale 300, el 8 vale 80 y el 1 vale 1. ¿Cuál es?", "381", "3 centenas, 8 decenas y 1 unidad."),
        ],
        "reason": [
            ex("Mía dice que en 252 las dos cifras 2 valen lo mismo. ¿Tiene razón?", "No; valen 200 y 2", "Una cifra vale según el lugar en que está."),
            ex("¿En cuál número la cifra 6 vale más: 612, 162 o 126?", "612", "En 612 el 6 vale 600, en 162 vale 60 y en 126 vale 6."),
        ],
        "challenge": [
            ex("Un número tiene dos cifras 4 y un 0 entre ellas. El primer 4 vale 400 y el segundo vale 4. ¿Qué número es?", "404", "400 + 0 + 4."),
            ex("En 777, ¿cuánto vale cada cifra 7, de izquierda a derecha?", "700, 70 y 7", "Están en centenas, decenas y unidades."),
        ],
    },
    context=[ex("Un marcador de una máquina muestra 358 puntos. Explica cuánto vale cada cifra.", "3 vale 300, 5 vale 50 y 8 vale 8", "Están en centenas, decenas y unidades.")],
    selfcheck=[
        ex("En 842, ¿cuánto vale la cifra 4?", "40", "Está en las decenas."),
        ex("¿Qué cifra está en el lugar de las centenas de 659?", "6", "La primera cifra es la de las centenas."),
        ex("Descompón 205 en los valores de sus cifras.", "200 + 0 + 5", "2 centenas, 0 decenas y 5 unidades."),
    ],
    open_task=task(
        "Escoge uno de los números 616, 838 o 404. Descomponlo en los valores de sus cifras y escribe una frase que explique por qué las dos cifras iguales valen distinto.",
        "Elijo 616: 600 + 10 + 6. Las dos cifras 6 son iguales, pero la primera está en las centenas y vale 600, y la última está en las unidades y vale 6.",
        ["descompone el número", "los valores suman el número", "explica por qué valen distinto", "nombra los lugares"],
        ["descomposición escrita en el cuaderno", "frase de explicación"],
        ["decir que las cifras iguales valen igual", "olvidar el valor de las decenas"],
        "Reconoce la explicación y pregunta qué pasaría si se cambiaran de lugar; si hay error, que use una tabla CDU.",
    ),
    reinforce="Escribe 536 en una tabla CDU y di cuánto vale cada cifra.",
    extend="Con las cifras 3, 3 y 5 forma tres números distintos y escribe cuánto vale el 5 en cada uno.",
)

register(
    OA5, 4,
    materials="Lápiz, cuaderno y tapas de dos colores. Usamos ▣ para una centena, ▮ para una decena y ● para una unidad.",
    use="Aprenderé a canjear centenas, decenas y unidades sin cambiar el valor del número. Sirve para restar cuando no hay suficientes unidades.",
    prior=["Sé que 10 unidades forman 1 decena y 10 decenas forman 1 centena.", "Sé leer una tabla CDU."],
    explain=[
        "Un canje cambia una pieza por 10 piezas del lugar de la derecha, o 10 por una del lugar de la izquierda. El valor no cambia. 1 centena se canjea por 10 decenas, y 1 decena se canjea por 10 unidades.",
        "Un mismo número se puede mostrar de varias formas. 3 centenas y 4 decenas son 340. Si canjeas 1 centena por 10 decenas, queda 2 centenas y 14 decenas, que también es 340. Es otra forma de mostrar lo mismo.",
        "Estos canjes sirven en las restas. Para 302 − 145 no hay decenas ni unidades suficientes, así que canjeas: 302 = 2 centenas, 10 decenas y 2 unidades, y luego 2 centenas, 9 decenas y 12 unidades. El valor sigue siendo 302.",
    ],
    vocab=[("canje", "cambiar una pieza por 10 del lugar siguiente"), ("reagrupar", "volver a juntar las piezas en otra forma"), ("forma usual", "forma con menos piezas, como 2 centenas y 5 decenas"), ("forma no usual", "otra forma de mostrar el mismo número"), ("valor total", "cantidad que representa todo junto")],
    worked=[
        {"title": "Una centena por diez decenas", "problem": "Muestra 340 como 2 centenas y ___ decenas.", "steps": ["340 son 3 centenas y 4 decenas.", "Canjeo 1 centena por 10 decenas: quedan 2 centenas.", "Las decenas pasan de 4 a 4 + 10 = 14."], "answer": "2 centenas y 14 decenas"},
        {"title": "Canjes para restar", "problem": "Reagrupa 302 para poder restar 145: muestra el número con decenas y unidades suficientes.", "steps": ["302 = 3 centenas, 0 decenas y 2 unidades.", "Canjeo 1 centena por 10 decenas: 2 centenas, 10 decenas y 2 unidades.", "Canjeo 1 decena por 10 unidades: 2 centenas, 9 decenas y 12 unidades."], "answer": "2 centenas, 9 decenas y 12 unidades"},
    ],
    mistakes=[
        {"wrong": "Escribir 340 como 2 centenas y 4 decenas después de canjear una centena.", "why": "Se quita la centena pero no se agregan las 10 decenas.", "fix": "Al canjear 1 centena por 10 decenas suma 10 a las decenas: 2 centenas y 14 decenas."},
        {"wrong": "Decir que 2 centenas y 14 decenas y 3 unidades suman 2 + 14 + 3 = 19.", "why": "Se suman las cantidades de piezas y no sus valores.", "fix": "Calcula 200 + 140 + 3 = 343."},
    ],
    tiers={
        "recovery": [
            ex("1 centena = ___ decenas.", "10", "10 decenas forman 1 centena."),
            ex("3 decenas y 2 unidades = 2 decenas y ___ unidades.", "12", "Se canjea 1 decena por 10 unidades y quedan 12 unidades."),
            ex("A 4 centenas y 3 decenas le canjeas 1 centena por decenas. ¿Cuántas centenas y decenas quedan?", "3 centenas y 13 decenas", "4 − 1 = 3 centenas y 3 + 10 = 13 decenas."),
        ],
        "understand": [
            ex("¿Es 245 igual a 24 decenas y 5 unidades?", "Sí", "24 decenas valen 240 y 240 + 5 = 245."),
            ex("¿Cuál es el canje correcto de 3 centenas y 1 decena: 2 centenas y 11 decenas, o 2 centenas y 20 decenas?", "2 centenas y 11 decenas", "200 + 110 = 310."),
            ex("Con 150 unidades, ¿cuántas decenas puedes formar?", "15", "Cada 10 unidades forman una decena."),
        ],
        "apply": [
            ex("Escribe 5 centenas y 2 decenas como 4 centenas y ___ decenas.", "12", "Se canjea 1 centena por 10 decenas: 2 + 10 = 12."),
            ex("Un número tiene 5 centenas, 0 decenas y 2 unidades. Canjea 1 centena por decenas: ¿cuántas centenas, decenas y unidades quedan?", "4 centenas, 10 decenas y 2 unidades", "5 − 1 = 4 centenas y 0 + 10 = 10 decenas."),
            ex("Escribe 1 centena y 6 decenas usando solo decenas.", "16 decenas", "Una centena son 10 decenas y 10 + 6 = 16."),
        ],
        "reason": [
            ex("Lía quiere restar 302 − 145 y canjea 1 centena por decenas y luego 1 decena por unidades. ¿Cómo queda 302?", "2 centenas, 9 decenas y 12 unidades", "Primero 2 centenas, 10 decenas, 2 unidades; luego 9 decenas y 12 unidades."),
            ex("Ana dice que 2 centenas, 14 decenas y 3 unidades suman 2 + 14 + 3 = 19. ¿Qué número es en realidad?", "343", "200 + 140 + 3 = 343."),
        ],
        "challenge": [
            ex("Escribe 400 de dos formas canjeadas: con 3 centenas y con 2 centenas.", "3 centenas y 10 decenas; 2 centenas y 20 decenas", "300 + 100 = 400 y 200 + 200 = 400."),
            ex("Un número tiene 1 centena, 14 decenas y 12 unidades. ¿Cómo queda en su forma usual (centenas, decenas y unidades)?", "2 centenas, 5 decenas y 2 unidades", "100 + 140 + 12 = 252."),
        ],
    },
    context=[ex("Una tienda tiene 3 cajas de 100 tornillos, ninguna bolsa de 10 y 5 sueltos. Abre una caja y la cambia por 10 bolsas de 10. ¿Qué tiene ahora?", "2 cajas, 10 bolsas y 5 sueltos", "300 + 0 + 5 = 305 y 200 + 100 + 5 = 305.")],
    selfcheck=[
        ex("1 centena se cambia por ___ decenas.", "10", "Una centena tiene 10 decenas."),
        ex("2 centenas y 3 decenas = 1 centena y ___ decenas.", "13", "Se canjea 1 centena por 10 decenas."),
        ex("30 decenas son ___ centenas.", "3", "Cada 10 decenas forman 1 centena."),
    ],
    open_task=task(
        "Muestra el número 250 en tres formas: la usual (centenas y decenas), con 1 centena y decenas, y solo con decenas. Para cada forma escribe el cálculo que prueba que vale 250 y dibuja una de ellas con ▣ y ▮.",
        "Usual: 2 centenas y 5 decenas, 200 + 50. Con 1 centena: 1 centena y 15 decenas, 100 + 150. Solo decenas: 25 decenas, 250. Dibujo: ▣ ▣ | ▮ ▮ ▮ ▮ ▮.",
        ["muestra tres formas", "cada una vale 250", "escribe el cálculo de cada forma", "hace un dibujo"],
        ["tres formas escritas", "cálculos", "dibujo con ▣ y ▮"],
        ["no sumar 10 decenas al canjear", "sumar piezas en vez de valores"],
        "Reconoce las tres formas y pregunta cómo supo que el valor no cambia; si hay error, que cuente con tapas de dos colores.",
    ),
    reinforce="Con tapas azules (decenas) y rojas (unidades), muestra 53 de dos formas distintas y escríbelas.",
    extend="Muestra 1.000 como 10 centenas, como 100 decenas y como unidades. ¿Cuántas unidades son?",
)
