"""Student material for 1.º básico Matemática, OA 01 (conteo), OA 02 (ordinales) y OA 03 (números hasta 20)."""
from __future__ import annotations

from student_content_ma02_a import fill, seq, words
from student_lessons import arith, ex, register

OA1, OA2, OA3 = "MA01 OA 01", "MA01 OA 02", "MA01 OA 03"
ORD = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto", "séptimo", "octavo", "noveno", "décimo"]


def dots(n: int) -> str:
    return " ".join("●" for _ in range(n)) if n else "(ninguno)"


def frame(n: int) -> str:
    """Ten-frame as two rows of five: filled ● and empty ○."""
    cells = ["●"] * n + ["○"] * (10 - n)
    return " ".join(cells[:5]) + " / " + " ".join(cells[5:])


def ordinal(n: int) -> str:
    return f"{n}º ({ORD[n - 1]})"


register(
    OA1, 1,
    materials="Hasta 15 fichas, tapas o botones; una hoja con las colecciones dibujadas en este cuaderno. Todas las cantidades están escritas.",
    use="Aprenderé a contar objetos de uno en uno sin saltarme ninguno ni repetir. Sirve para saber cuántos hay de algo, como lápices, galletas o amigos.",
    prior=["Sé decir los números en orden: 1, 2, 3…", "Sé señalar un objeto con el dedo."],
    explain=[
        "Contar es decir una palabra número por cada objeto. Al primer objeto le toca «uno», al segundo «dos», al tercero «tres» y así hasta el último. Cada objeto recibe una sola palabra, y cada palabra se usa una sola vez.",
        "La última palabra que dices es la que dice cuántos hay. Si cuentas ● ● ● ● ● y terminas en «cinco», hay cinco. No hay que volver a contar desde el principio: ese número ya responde la pregunta.",
        "Para no equivocarte, mueve cada objeto a un lado al contarlo, o tócalo con el dedo y avanza en una dirección. Si los objetos están en fila, empieza por un extremo. Si están desordenados, ve marcándolos con un lápiz.",
    ],
    vocab=[("contar", "decir un número por cada objeto"), ("cantidad", "cuántos objetos hay"), ("último número", "el número con que termino de contar; dice cuántos hay"), ("señalar", "tocar un objeto con el dedo"), ("de uno en uno", "un objeto por cada número")],
    worked=[
        {"title": "Contar una fila", "problem": f"¿Cuántas fichas hay? {dots(6)}", "steps": ["Empiezo por la primera de la izquierda.", "Toco una por una y digo: uno, dos, tres, cuatro, cinco, seis.", "La última palabra que dije es seis."], "answer": "6 fichas"},
        {"title": "Contar sin repetir", "problem": "Hay 4 tapas desordenadas en la mesa. ¿Cómo las cuento sin repetir?", "steps": ["Pongo las tapas en un lado a medida que las cuento.", "Digo: uno, dos, tres, cuatro.", "Al final no queda ninguna en el lugar de origen, así que no me salté ninguna."], "answer": "4 tapas"},
    ],
    mistakes=[
        {"wrong": "Decir dos números para un mismo objeto.", "why": "Se cuenta más rápido que lo que se señala.", "fix": "Toca un objeto y di una palabra; luego pasa al siguiente."},
        {"wrong": "Volver a contar desde 1 para responder cuántos hay.", "why": "No se sabe que el último número da la cantidad.", "fix": "Cuando terminas, el último número dicho es el total."},
    ],
    tiers={
        "recovery": [ex(f"Cuenta: {dots(3)}. ¿Cuántas hay?", "3", "Se dice uno, dos, tres y el último número es 3."), ex(f"Cuenta: {dots(5)}. ¿Cuántas hay?", "5", "El último número que digo es cinco."), ex(f"Cuenta: {dots(8)}. ¿Cuántas hay?", "8", "Se señala una por una hasta llegar a ocho.")],
        "understand": [
            ex("Conté 7 fichas y la última palabra fue «siete». ¿Cuántas fichas hay?", "7", "El último número dice cuántas hay."),
            ex("Si cuento una ficha con dos números, ¿mi cuenta quedará bien?", "No", "Cada objeto debe tener una sola palabra número."),
            ex("¿Dónde conviene empezar a contar una fila de fichas?", "En un extremo", "Así se sabe dónde empezó y dónde termina."),
        ],
        "apply": [ex(f"Cuenta las manzanas: {dots(9)}.", "9", "Nueve señalamientos, nueve palabras."), ex(f"Cuenta las estrellas: {dots(12)}.", "12", "Después de diez vienen once y doce."), ex("Pon 6 tapas sobre la mesa y cuéntalas. ¿Cuál es la última palabra que dices?", "Seis", "Seis tapas se cuentan hasta el seis.")],
        "reason": [
            ex("Ana contó ● ● ● ● y dijo «uno, dos, tres, cuatro, cinco». ¿Qué hizo mal?", "Dijo un número de más; hay 4", "Hay cuatro objetos y debe haber cuatro palabras."),
            ex("Beto contó 5 fichas y luego las movió de lugar. ¿Cuántas hay ahora?", "5", "Mover los objetos no cambia cuántos son."),
        ],
        "challenge": [
            ex("Tengo 7 fichas y me dan 1 más. Sin empezar de nuevo, ¿qué número digo después de siete?", "Ocho", "Ocho viene justo después de siete."),
            ex("Hay 10 lápices en una caja y 3 afuera. ¿Cuántos hay si cuento todos?", "13", "Después de diez digo once, doce, trece."),
        ],
    },
    context=[ex(f"En el patio hay niños jugando: {dots(11)}. Cuéntalos y escribe cuántos son.", "11", "Se cuenta uno por uno hasta once.")],
    selfcheck=[ex(f"Cuenta: {dots(4)}.", "4", "Cuento cuatro puntos."), ex("¿Qué número viene después de nueve?", "Diez", "Diez va justo después de nueve."), ex("¿Qué dice cuántos hay: el primer número o el último?", "El último", "Se llega a la cantidad al terminar de contar.")],
    open_task={
        "statement": "Junta 9 objetos pequeños de tu casa (por ejemplo, 9 botones, tapas o lápices). Cuéntalos tocando uno por uno, dibújalos y escribe cuántos son. Cuenta otra vez en otra dirección para comprobar.",
        "example": "Conté 9 tapas de izquierda a derecha. Dibujé 9 círculos. Volví a contar de derecha a izquierda y también me dio 9.",
        "criteria": ["toca un objeto por cada número", "dice el último número como total", "comprueba contando de nuevo"],
        "evidence": ["dibujo con los objetos", "número escrito", "explicación oral"],
        "errors": ["saltarse un objeto", "contar uno dos veces"],
        "feedback": "Reconoce que el conteo fue ordenado y pide que muestre con el dedo dónde empezó; si el segundo conteo difiere, que lo repita despacio.",
    },
    reinforce="Cuenta de 1 a 10 con 10 fichas, moviendo cada una a un lado.",
    extend="Cuenta tus 10 dedos y luego los dedos de dos personas; explica cómo seguiste después del diez.",
)

register(
    OA1, 2,
    materials="20 fichas, la recta numérica de 0 a 20 de este cuaderno y lápiz de color.",
    use="Aprenderé a contar de 2 en 2 formando parejas. Sirve para contar pares de zapatos, ojos o guantes más rápido.",
    prior=["Sé contar de 1 en 1 hasta 20.", "Sé qué es una pareja."],
    explain=[
        "Contar de 2 en 2 es saltarse un número cada vez. En vez de decir 1, 2, 3, 4, dices 2, 4. Cada salto avanza dos lugares. Es útil cuando los objetos vienen en parejas, como los zapatos.",
        "Los números que dices al contar de 2 en 2 desde 0 son 2, 4, 6, 8, 10, 12, 14, 16, 18 y 20. Se llaman pares. Si haces parejas con fichas y cada ficha tiene su compañera, ese número es par.",
        "Para anticipar el siguiente número, suma 2 al último que dijiste. Después de 6 viene 8; después de 12 viene 14. Puedes comprobar dibujando una pareja nueva en la fila.",
    ],
    vocab=[("pareja", "dos objetos que van juntos"), ("de 2 en 2", "sumar 2 en cada salto"), ("par", "número que se puede formar con parejas sin que sobre ninguno"), ("salto", "lo que avanzo al contar"), ("siguiente", "el que viene después")],
    worked=[
        {"title": "Contar pares de zapatos", "problem": "Hay 5 pares de zapatos. ¿Cuántos zapatos hay?", "steps": ["Cuento una pareja por vez: 2, 4, 6, 8, 10.", "Cinco parejas son cinco saltos.", "El último número es 10."], "answer": "10 zapatos"},
        {"title": "Predecir el siguiente", "problem": "Contamos 2, 4, 6, 8. ¿Qué número viene?", "steps": ["Sumo 2 al último: 8 + 2.", "8 + 2 = 10.", "Compruebo: 8 y 10 están separados por dos lugares."], "answer": "10"},
    ],
    mistakes=[
        {"wrong": "Contar 2, 3, 4, 5.", "why": "Se avanza de 1 en 1 en vez de 2 en 2.", "fix": "Cada salto suma 2: 2, 4, 6, 8."},
        {"wrong": "Terminar en 9 al contar parejas.", "why": "Se pierde una ficha en una pareja.", "fix": "Revisa que cada ficha tenga compañera; con parejas completas el total es par."},
    ],
    tiers={
        "recovery": [fill(0, 2, 6, (1, 3), "Cada número es 2 más que el anterior."), fill(2, 2, 6, (2, 4), "Se suma 2 en cada paso."), fill(10, 2, 5, (1, 3), "10, 12, 14, 16, 18.")],
        "understand": [
            ex("¿Cuántas fichas hay en 3 parejas?", "6", "Cuento 2, 4, 6."),
            ex("¿Qué número viene después de 12 al contar de 2 en 2?", "14", "12 + 2 = 14."),
            ex("¿Es 8 un número par?", "Sí", "8 se forma con 4 parejas completas."),
        ],
        "apply": [
            arith("Hay 4 pares de calcetines. ¿Cuántos calcetines hay?", "4*2", "Cuatro parejas de 2 son 8."),
            ex("Cuenta de 2 en 2 hasta llegar a 14, escribiendo todos los números.", "2, 4, 6, 8, 10, 12, 14", "Siete saltos de 2 llegan a 14."),
            arith("En una mesa hay 6 niños. Cada uno tiene 2 manos. ¿Cuántas manos hay?", "6*2", "Seis parejas de manos son 12."),
        ],
        "reason": [
            ex("Marta dice que 2, 4, 5, 8 sigue el salto de 2. ¿Dónde está el error?", "El 5 debe ser 6", "Entre 4 y el siguiente debe haber 2: 4 + 2 = 6."),
            ex("Hay 7 fichas. ¿Puedo formar parejas sin que sobre ninguna?", "No; sobra 1", "3 parejas usan 6 fichas y sobra una."),
        ],
        "challenge": [
            ex("Cuento de 2 en 2 y llego a 16. ¿Cuántos saltos di?", "8 saltos", "2, 4, 6, 8, 10, 12, 14, 16 son 8 números."),
            ex("Si tengo 9 fichas y consigo 1 más, ¿puedo hacer parejas sin que sobre ninguna? Explica.", "Sí, con 10 hay 5 parejas", "9 + 1 = 10 y 10 se forma con 5 parejas."),
        ],
    },
    context=[arith("En una caja hay 8 guantes sueltos para formar parejas. ¿Cuántas parejas de guantes se forman?", "8//2", "Contando de 2 en 2 hasta 8 hay 4 saltos: 4 parejas.")],
    selfcheck=[fill(4, 2, 5, (1, 3), "4, 6, 8, 10, 12."), ex("¿Cuántas fichas son 5 parejas?", "10", "2, 4, 6, 8, 10: cinco saltos de 2 llegan a 10."), ex("¿Qué número sigue: 14, 16, __?", "18", "16 + 2 = 18.")],
    open_task={
        "statement": "Dibuja 6 pares de zapatos (o 6 pares de círculos). Cuenta de 2 en 2 y escribe cada número debajo de su pareja. ¿Cuántos zapatos hay?",
        "example": "Dibujé 6 parejas y escribí debajo: 2, 4, 6, 8, 10, 12. Hay 12 zapatos.",
        "criteria": ["dibuja 6 parejas", "escribe números de 2 en 2", "responde con el último número"],
        "evidence": ["dibujo", "secuencia 2 a 12", "respuesta escrita"],
        "errors": ["contar de 1 en 1 los zapatos", "no cerrar una pareja"],
        "feedback": "Reconoce las parejas bien formadas y pide que explique por qué el número final es par.",
    },
    reinforce="Haz parejas con 12 fichas y cuenta de 2 en 2 mientras las mueves.",
    extend="Descubre qué pasa si cuentas de 2 en 2 empezando en 1. ¿Qué números dices hasta 11?",
)

register(
    OA1, 3,
    materials="Tabla del 1 al 100 en el cuaderno, 10 palitos por grupo y lápiz de color.",
    use="Aprenderé a contar de 5 en 5 y de 10 en 10 hasta 100. Sirve para contar grupos grandes con rapidez, como paquetes de lápices o dedos de muchas manos.",
    prior=["Sé contar de 2 en 2 hasta 20.", "Sé que una mano tiene 5 dedos."],
    explain=[
        "Si cuentas de 5 en 5, cada salto suma 5: 5, 10, 15, 20, 25. Así cuentas los dedos de varias manos. Los números terminan en 5 o en 0, uno después del otro.",
        "Si cuentas de 10 en 10, cada salto suma 10: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100. Todos terminan en 0. Con paquetes de 10 palitos, cada paquete es un salto.",
        "Para llegar a 100 de 10 en 10 necesitas 10 saltos; de 5 en 5, necesitas 20. Marca en la tabla del 100 los números que dices y verás un camino ordenado, de columnas, que te ayuda a seguir.",
    ],
    vocab=[("de 5 en 5", "sumar 5 en cada salto"), ("de 10 en 10", "sumar 10 en cada salto"), ("paquete", "grupo de 10 objetos"), ("tabla del 100", "tabla con los números de 1 a 100"), ("terminar en", "cuál es la última cifra del número")],
    worked=[
        {"title": "Contar manos", "problem": "Hay 4 manos con todos sus dedos. ¿Cuántos dedos hay?", "steps": ["Cada mano son 5 dedos.", "Cuento de 5 en 5: 5, 10, 15, 20.", "Cuatro manos son cuatro saltos."], "answer": "20 dedos"},
        {"title": "Contar paquetes de 10", "problem": "Hay 7 paquetes de 10 palitos. ¿Cuántos palitos hay?", "steps": ["Cada paquete son 10 palitos.", "Cuento de 10 en 10: 10, 20, 30, 40, 50, 60, 70.", "Siete paquetes, siete saltos."], "answer": "70 palitos"},
    ],
    mistakes=[
        {"wrong": "Contar 5, 10, 14, 20.", "why": "Se pierde el salto exacto de 5.", "fix": "Suma 5 al número anterior: 10 + 5 = 15."},
        {"wrong": "Contar 10, 20, 30, 35.", "why": "Se mezcla el salto de 5 con el de 10.", "fix": "Mantén el mismo salto en toda la secuencia."},
    ],
    tiers={
        "recovery": [fill(0, 5, 6, (1, 3), "Se suma 5 cada vez."), fill(10, 10, 6, (1, 3), "Se suma 10 cada vez."), fill(5, 5, 6, (2, 4), "5, 10, 15, 20, 25, 30.")],
        "understand": [
            ex("¿En qué cifra terminan los números cuando cuentas de 10 en 10?", "En 0", "10, 20, 30… todos terminan en 0."),
            ex("¿Qué número viene después de 25 al contar de 5 en 5?", "30", "25 + 5 = 30."),
            ex("¿Cuántos saltos de 10 hacen falta para llegar a 100 desde 0?", "10 saltos", "10, 20, 30, 40, 50, 60, 70, 80, 90, 100."),
        ],
        "apply": [
            arith("Hay 3 manos. ¿Cuántos dedos hay si cuento de 5 en 5?", "3*5", "Tres saltos de 5 son 15."),
            arith("Hay 9 paquetes de 10 lápices. ¿Cuántos lápices hay?", "9*10", "Nueve saltos de 10 llegan a 90."),
            fill(35, 5, 6, (1, 3, 5), "35, 40, 45, 50, 55, 60."),
        ],
        "reason": [
            ex("Pía contó 10, 20, 25, 40. ¿Dónde está el error?", "25 debe ser 30", "El salto debe ser 10: 20 + 10 = 30."),
            ex("¿Por qué es más rápido contar de 10 en 10 que de 1 en 1 hasta 100?", "Porque se necesitan 10 saltos y no 100", "Cada salto cubre 10 números."),
        ],
        "challenge": [
            ex("Cuento de 5 en 5 desde 0 y llego a 50. ¿Cuántos saltos di?", "10 saltos", "5, 10, 15, 20, 25, 30, 35, 40, 45, 50."),
            ex("Tengo 2 paquetes de 10 palitos y 5 palitos sueltos. ¿Cuántos palitos hay?", "25", "Primero 10, 20 y luego 21, 22, 23, 24, 25."),
        ],
    },
    context=[arith("En la sala hay 5 niños. Cada niño tiene 10 palitos de helado. ¿Cuántos palitos hay en total?", "5*10", "Cinco paquetes de 10 son 50 palitos.")],
    selfcheck=[fill(20, 10, 5, (1, 3), "20, 30, 40, 50, 60."), ex("¿Cuántos dedos hay en 2 manos?", "10", "5 + 5 = 10."), ex("¿Qué número sigue: 40, 45, __?", "50", "45 + 5 = 50.")],
    open_task={
        "statement": "En tu tabla del 100, pinta de rojo los números que dices al contar de 10 en 10 y de azul los que dices al contar de 5 en 5 desde 5 hasta 50. Describe qué ves.",
        "example": "Los rojos son 10, 20, 30, 40, 50… y los azules son 5, 10, 15 … 50. Algunos números quedaron con los dos colores: 10, 20, 30, 40 y 50. Los rojos siempre terminan en 0.",
        "criteria": ["pinta los números correctos", "usa dos colores", "describe lo que observa"],
        "evidence": ["tabla pintada", "descripción escrita"],
        "errors": ["pintar de 1 en 1", "mezclar los saltos"],
        "feedback": "Reconoce la tabla ordenada y pide que explique por qué algunos números tienen los dos colores.",
    },
    reinforce="Cuenta dedos de 5 en 5 usando las manos de cuatro personas.",
    extend="Descubre cuántos saltos de 5 hay en 100 y compáralos con los saltos de 10.",
)

register(
    OA1, 4,
    materials="Recta numérica de 0 a 100 en el cuaderno, flechas +1, −1, +2, −2, +5, −5, +10 y −10 dibujadas y fichas.",
    use="Aprenderé a elegir el salto correcto y a contar hacia adelante o hacia atrás desde cualquier número. Sirve para llegar a una meta, como juntar un número de figuritas.",
    prior=["Sé contar de 1, 2, 5 y 10 en 10 hacia adelante.", "Sé qué significa hacia atrás."],
    explain=[
        "Para llegar de un número a otro, primero elige el salto. Si el salto es de 10 y partes en 30, el siguiente es 40. Hacia atrás es lo contrario: desde 30 con salto de 10 vas a 20.",
        "Puedes empezar en cualquier número, no sólo en 0. Si partes en 27 y cuentas de 1 en 1 llegas a 28, 29, 30. Si cuentas de 10 en 10 llegas a 37, 47, 57. Fíjate en el último número de cada uno: en los saltos de 10 no cambia (siempre termina en 7).",
        "Con una flecha puedes marcar lo que haces: «+5» avanza cinco, «−5» retrocede cinco. Elige el salto que te lleve a la meta con menos pasos y comprueba que la meta coincida.",
    ],
    vocab=[("hacia adelante", "sumar al contar"), ("hacia atrás", "restar al contar"), ("meta", "el número al que quiero llegar"), ("punto de partida", "el número desde el que empiezo"), ("flecha", "dibujo que muestra un salto en la recta")],
    worked=[
        {"title": "Elegir el salto", "problem": "Parto en 20 y quiero llegar a 50. ¿Qué salto me conviene?", "steps": ["De 20 a 50 hay que avanzar 30 lugares.", "Con saltos de 10: 30, 40, 50. Son 3 saltos.", "Con saltos de 1 serían 30 saltos."], "answer": "Saltos de 10; 3 saltos"},
        {"title": "Contar hacia atrás", "problem": "Parto en 45 y retrocedo 3 saltos de 5. ¿A qué número llego?", "steps": ["45 − 5 = 40.", "40 − 5 = 35.", "35 − 5 = 30."], "answer": "30"},
    ],
    mistakes=[
        {"wrong": "Sumar cuando se pide retroceder.", "why": "Se confunde la dirección.", "fix": "Hacia atrás se resta y el número se hace menor."},
        {"wrong": "Cambiar el salto en medio del camino.", "why": "No se mantiene la regla.", "fix": "Elige un salto y úsalo hasta llegar a la meta."},
    ],
    tiers={
        "recovery": [fill(30, 10, 5, (1, 3), "30, 40, 50, 60, 70."), fill(50, -10, 5, (1, 3), "50, 40, 30, 20, 10."), fill(15, 5, 5, (2, 4), "15, 20, 25, 30, 35.")],
        "understand": [
            ex("Parto en 30 y cuento hacia atrás de 10 en 10. ¿A qué número llego primero?", "20", "30 − 10 = 20."),
            ex("¿Qué salto me lleva de 5 a 15 en dos saltos iguales?", "De 5 en 5", "5 + 5 = 10 y 10 + 5 = 15."),
            ex("¿Cómo sé que debo retroceder para ir de 40 a 25?", "Porque 25 es menor que 40", "La meta es un número más pequeño."),
        ],
        "apply": [
            ex("Parto en 12 y cuento de 1 en 1 hacia atrás tres veces. ¿Dónde llego?", "9", "11, 10, 9."),
            ex("Parto en 60 y cuento de 10 en 10 hacia adelante dos veces. ¿Dónde llego?", "80", "70 y 80."),
            ex("Parto en 25 y retrocedo dos saltos de 5. ¿Dónde llego?", "15", "20 y 15."),
        ],
        "reason": [
            ex("Paula parte en 40 y quiere llegar a 70. Dice que con saltos de 5 son 3 saltos. ¿Es correcto?", "No; con saltos de 5 son 6 saltos", "De 40 a 70 hay 30 lugares, y 5 + 5 + 5 + 5 + 5 + 5 = 30: son 6 saltos de 5."),
            ex("Mateo dice que contando de 10 en 10 desde 23 se llega a 33, 43, 53. ¿Está bien?", "Sí", "Se suma 10 y las unidades quedan en 3."),
        ],
        "challenge": [
            ex("Parto en 15. Hago un salto de 5 y luego saltos de 10 hasta llegar a 60. ¿Cuántos saltos hago en total?", "5 saltos", "15 + 5 = 20 y luego 30, 40, 50, 60 son 4 saltos de 10; en total 5."),
            ex("Parto en 100 y retrocedo de 10 en 10. ¿Después de cuántos saltos llego a 40?", "6 saltos", "90, 80, 70, 60, 50, 40."),
        ],
    },
    context=[ex("Tengo 35 figuritas y quiero llegar a 60. Si las junto de a 5, ¿cuántos paquetes de 5 necesito agregar?", "5 paquetes", "40, 45, 50, 55, 60 son 5 saltos.")],
    selfcheck=[fill(20, 5, 5, (1, 3), "20, 25, 30, 35, 40."), ex("¿Qué número queda si retrocedo 10 desde 60?", "50", "60 − 10 = 50."), ex("¿Qué número sigue: 7, 8, __?", "9", "8 + 1 = 9.")],
    open_task={
        "statement": "Parte en 15. Escribe cómo llegarías a 45 usando saltos de 5 y luego usando saltos de 10. Cuenta los saltos de cada forma y di cuál usa menos.",
        "example": "Con saltos de 5: 20, 25, 30, 35, 40, 45 (6 saltos). Con saltos de 10: 25, 35, 45 (3 saltos). Usa menos saltos el de 10.",
        "criteria": ["mantiene el salto elegido", "cuenta bien los saltos", "compara las dos formas"],
        "evidence": ["secuencias escritas", "número de saltos", "frase de comparación"],
        "errors": ["mezclar los saltos", "contar los números y no los saltos"],
        "feedback": "Pide dibujar las flechas en la recta; reconoce que se comparó cuántos saltos usa cada camino.",
    },
    reinforce="Con una recta y una ficha, salta de 5 en 5 de 0 a 50 y vuelve.",
    extend="Busca un camino de 3 saltos distintos para llegar de 10 a 40 y explica cuál elegirías.",
)

register(
    OA2, 1,
    materials="Cinco personajes dibujados en fila, tarjetas con 1º a 5º y cinta para marcar la fila. Todo viene escrito en este cuaderno.",
    use="Aprenderé a decir en qué lugar está alguien en una fila: primero, segundo, tercero… Sirve para saber quién llega primero o quién espera su turno.",
    prior=["Sé contar hasta 10.", "Sé qué significa una fila."],
    explain=[
        "Los números ordinales dicen el lugar que ocupa algo en una fila. El que está al comienzo es el primero (1º), el siguiente es el segundo (2º), luego el tercero (3º), el cuarto (4º) y el quinto (5º).",
        "No es lo mismo que contar cuántos hay. Si en una fila hay 5 niños, «cinco» dice cuántos son; «quinto» dice el lugar del último. Fíjate en el punto de partida: se empieza a contar desde donde dice la fila.",
        "Para usar bien los ordinales, mira siempre desde dónde empieza la fila. Si el primero está a la izquierda, el segundo está a su derecha. Si cambias el comienzo, cambian los lugares. Para una niña o una cosa femenina se dice primera, segunda, tercera… (1ª, 2ª, 3ª…).",
    ],
    vocab=[("ordinal", "palabra que dice el lugar: primero, segundo…"), ("primero (1º)", "el que está al comienzo de la fila"), ("último", "el que está al final de la fila"), ("fila", "personas u objetos puestos uno detrás de otro"), ("lugar", "posición dentro de la fila")],
    worked=[
        {"title": "Decir el lugar", "problem": "En la fila hay: gato, perro, pájaro, pez, conejo (de izquierda a derecha). ¿En qué lugar está el pájaro?", "steps": ["Empiezo por la izquierda: gato 1º, perro 2º, pájaro 3º.", "El pájaro es el tercero."], "answer": "Tercero (3º)"},
        {"title": "Distinguir cuántos de en qué lugar", "problem": "En una fila hay 4 niños. ¿Qué lugar ocupa el último?", "steps": ["Hay 4 niños: 1º, 2º, 3º y 4º.", "El último ocupa el cuarto lugar."], "answer": "Cuarto (4º)"},
    ],
    mistakes=[
        {"wrong": "Decir «dos» para el segundo lugar.", "why": "Se confunde cantidad con lugar.", "fix": "Para el lugar usa segundo (2º), no dos."},
        {"wrong": "Empezar a contar desde el lado equivocado.", "why": "No se fijó el comienzo de la fila.", "fix": "Pregunta desde dónde empieza la fila antes de decir el lugar."},
    ],
    tiers={
        "recovery": [ex("¿Cómo se llama el que está al comienzo de la fila?", "Primero (1º)", "El primer lugar es el del comienzo."), ex("¿Qué lugar viene después del primero?", "Segundo (2º)", "Segundo significa el que sigue al primero."), ex("Escribe el ordinal del número 3.", "Tercero (3º)", "3º se lee tercero.")],
        "understand": [
            ex("Fila de izquierda a derecha: sol, luna, estrella, nube, rayo. ¿En qué lugar está la estrella?", "Tercero (3º)", "Sol 1º, luna 2º, estrella 3º."),
            ex("En la misma fila, ¿qué hay en el quinto lugar?", "El rayo", "Sol 1º, luna 2º, estrella 3º, nube 4º, rayo 5º."),
            ex("En la misma fila, ¿quién está en el segundo lugar?", "La luna", "La luna está justo después del sol."),
        ],
        "apply": [
            ex("Fila: Ana, Beto, Carla, Diego. ¿Quién es el tercero?", "Carla", "Ana 1º, Beto 2º, Carla 3º."),
            ex("Fila: rojo, azul, verde, amarillo, negro. ¿De qué color es el cuarto?", "Amarillo", "El cuarto lugar es el amarillo."),
            ex("Fila: casa, árbol, auto. ¿En qué lugar está el auto?", "Tercero (3º)", "Casa 1º, árbol 2º, auto 3º."),
        ],
        "reason": [
            ex("Rosa dice que en una fila de 4 niños, «cuatro» es el último lugar. ¿Qué debe decir?", "Cuarto (4º)", "Para lugares se usan ordinales."),
            ex("Si la fila empieza por el otro lado, ¿el primero sigue siendo el mismo?", "No", "El primero es el que está al comienzo."),
        ],
        "challenge": [
            ex("Una fila tiene 5 personas. Si me ubico en el segundo lugar, ¿cuántas personas hay detrás de mí?", "3", "Después del segundo están el 3º, 4º y 5º."),
            ex("Si hay un niño primero y otro niño último en una fila de 5, ¿qué lugar ocupa el último?", "Quinto (5º)", "Hay 5 lugares."),
        ],
    },
    context=[ex("En la panadería hay una fila: Laura, Tomás, Nina, Pedro, Julia. Si Nina es la tercera, ¿qué lugar tiene Julia?", "Quinta (5ª)", "Laura 1ª, Tomás 2º, Nina 3ª, Pedro 4º, Julia 5ª.")],
    selfcheck=[ex("¿Cuál es el primer lugar?", "Primero (1º)", "Es el comienzo de la fila."), ex("Escribe el ordinal del número 5.", "Quinto (5º)", "5º se lee quinto."), ex("¿Qué lugar sigue después del tercero?", "Cuarto (4º)", "Después del 3º va el 4º.")],
    open_task={
        "statement": "Dibuja una fila de 5 objetos distintos (por ejemplo: pelota, lápiz, taza, llave, libro). Escribe debajo de cada uno su ordinal y responde: ¿qué está en el tercer lugar?",
        "example": "Fila: pelota 1º, lápiz 2º, taza 3º, llave 4º, libro 5º. En el tercer lugar está la taza.",
        "criteria": ["dibuja 5 objetos", "escribe 1º a 5º en orden", "responde la pregunta"],
        "evidence": ["dibujo de la fila", "ordinales escritos", "respuesta"],
        "errors": ["usar cantidades en vez de ordinales", "saltarse un lugar"],
        "feedback": "Pide que lea la fila de izquierda a derecha en voz alta; reconoce el uso correcto de los símbolos.",
    },
    reinforce="Haz una fila con 5 objetos de tu casa y di el lugar de cada uno.",
    extend="Descubre qué lugar ocupa cada persona si la fila se da vuelta (el último pasa a ser primero).",
)

register(
    OA2, 2,
    materials="Diez personajes dibujados en fila y tarjetas de 6º a 10º. Todo viene escrito en este cuaderno.",
    use="Aprenderé los ordinales del sexto al décimo. Sirve para ubicarme en filas largas, como las de un recreo o una carrera.",
    prior=["Sé decir primero a quinto.", "Sé contar hasta 10."],
    explain=[
        "Después del quinto vienen el sexto (6º), el séptimo (7º), el octavo (8º), el noveno (9º) y el décimo (10º). Con ellos puedes ubicar a alguien en una fila de hasta diez lugares.",
        "Los ordinales se escriben con el número y una pequeña «o» arriba: 6º, 7º, 8º, 9º, 10º. Se leen sexto, séptimo, octavo, noveno y décimo. Cuando hablas de una niña o de algo femenino, se dice sexta, séptima, octava, novena, décima (6ª, 7ª…).",
        "Para encontrar un lugar largo, no cuentes desde cero cada vez: cuenta desde el primero, apoyándote en los que ya sabes. El quinto lleva la mitad de la fila de diez delante; el sexto es el que viene justo después.",
    ],
    vocab=[("sexto (6º)", "el lugar después del quinto"), ("séptimo (7º)", "el lugar después del sexto"), ("octavo (8º)", "el lugar después del séptimo"), ("noveno (9º)", "el lugar antes del último en una fila de diez"), ("décimo (10º)", "el lugar después del noveno")],
    worked=[
        {"title": "Ubicar el octavo", "problem": "Fila: A, B, C, D, E, F, G, H, I, J. ¿Quién está en el octavo lugar?", "steps": ["A es 1º, B 2º, C 3º, D 4º.", "E es 5º, F 6º, G 7º, H 8º.", "El octavo es H."], "answer": "H"},
        {"title": "Del símbolo a la palabra", "problem": "Escribe cómo se lee 9º.", "steps": ["9º viene después de 8º.", "Se lee noveno."], "answer": "Noveno"},
    ],
    mistakes=[
        {"wrong": "Confundir sexto con séptimo.", "why": "Se mezclan los nombres.", "fix": "Repite en orden: sexto, séptimo, octavo, noveno, décimo."},
        {"wrong": "Pensar que 10º se lee diez.", "why": "Se confunde con el cardinal.", "fix": "10º se lee décimo."},
    ],
    tiers={
        "recovery": [ex("¿Qué ordinal viene después del quinto?", "Sexto (6º)", "Después del 5º viene el 6º."), ex("¿Qué ordinal es 7º?", "Séptimo", "7º se lee séptimo."), ex("¿Qué ordinal es el último de una fila de 10?", "Décimo (10º)", "Hay diez lugares.")],
        "understand": [
            ex("Escribe con el símbolo el octavo lugar.", "8º", "Octavo es 8º."),
            ex("¿Qué número ordinal viene justo antes del décimo?", "Noveno (9º)", "9º está justo antes de 10º."),
            ex("¿Qué lugar es más adelante: el sexto o el séptimo?", "El séptimo", "7º viene después de 6º."),
        ],
        "apply": [
            ex("Fila: 🍎 🍌 🍇 🍊 🍓 🍒 🍑 🍋 🍐 🍍. ¿Qué fruta es la sexta?", "🍒 (cereza)", "Manzana 1ª, plátano 2ª, uva 3ª, naranja 4ª, frutilla 5ª, cereza 6ª."),
            ex("En la misma fila, ¿qué fruta es la décima?", "🍍 (piña)", "La fila tiene diez frutas y la última es la piña."),
            ex("En la misma fila, ¿qué fruta ocupa el séptimo lugar?", "🍑 (durazno)", "Después de la cereza, la séptima es el durazno."),
        ],
        "reason": [
            ex("Ema dice que el noveno está después del décimo. ¿Es correcto?", "No", "El noveno está justo antes del décimo."),
            ex("En una carrera de 10 corredores, Pablo llegó octavo. ¿Cuántos corredores llegaron antes que él?", "7", "Los lugares 1º a 7º llegaron antes."),
        ],
        "challenge": [
            ex("En una fila de 10, ¿cuántos lugares hay entre el tercero y el octavo (sin contar esos dos)?", "4", "Entre el 3º y el 8º están el 4º, 5º, 6º y 7º."),
            ex("Si el primero pasa al final, ¿qué lugar ocupará el que antes era el décimo?", "Noveno (9º)", "Todos avanzan un lugar y el décimo pasa al noveno."),
        ],
    },
    context=[ex("En una carrera de 10 niños, Camila llegó séptima y Luis llegó noveno. ¿Quién llegó antes?", "Camila", "El 7º llega antes que el 9º.")],
    selfcheck=[ex("Escribe con símbolo el sexto lugar.", "6º", "Sexto es 6º."), ex("¿Qué ordinal sigue después del octavo?", "Noveno (9º)", "Después del 8º va el 9º."), ex("¿Cuál ordinal es 10º?", "Décimo", "10º se lee décimo.")],
    open_task={
        "statement": "Dibuja una fila de 10 círculos de colores y escribe debajo de cada uno 1º a 10º. Colorea el sexto de rojo y el décimo de azul, y escribe una frase que diga qué lugar ocupa cada uno.",
        "example": "Pinté de rojo el círculo 6º (sexto) y de azul el 10º (décimo). El rojo es el sexto y el azul es el último, el décimo.",
        "criteria": ["10 lugares en orden", "pinta los lugares pedidos", "escribe la frase con ordinales"],
        "evidence": ["fila dibujada", "ordinales escritos", "frase"],
        "errors": ["saltar el séptimo", "escribir 10 sin símbolo"],
        "feedback": "Pide que lea los ordinales de corrido; reconoce el orden correcto.",
    },
    reinforce="Recita primero a décimo señalando 10 fichas en fila.",
    extend="Inventa una carrera de 10 personajes y escribe quién llegó en cada lugar.",
)

register(
    OA2, 3,
    materials="Fila de 10 personajes en este cuaderno; tarjetas 1º a 10º; lápices de colores.",
    use="Aprenderé a decir quién está antes, después y entre otros en una fila. Sirve para dar indicaciones claras sobre dónde está alguien.",
    prior=["Sé los ordinales del primero al décimo.", "Sé qué es una fila."],
    explain=[
        "«Antes» y «después» sirven para comparar lugares. Si alguien está en el 4º lugar, el 3º está antes de él y el 5º está después. «Entre» sirve para ubicar a quien queda en el medio de dos lugares: entre el 3º y el 5º está el 4º.",
        "Para responder, mira dónde empieza la fila. Después busca el lugar y cuenta uno hacia adelante o uno hacia atrás. Dibujar la fila y escribir los ordinales debajo ayuda a no equivocarse.",
        "Cada pista te lleva a un lugar: «el que está antes del sexto» es el quinto, y «el que está entre el segundo y el cuarto» es el tercero. Lee la pista con calma y compruébala con la fila.",
    ],
    vocab=[("antes", "en un lugar anterior"), ("después", "en un lugar posterior"), ("entre", "en medio de dos lugares"), ("justo", "inmediatamente al lado"), ("pista", "dato que ayuda a encontrar un lugar")],
    worked=[
        {"title": "Antes y después", "problem": "¿Quién está justo antes del sexto y quién justo después?", "steps": ["Antes del 6º está el 5º.", "Después del 6º está el 7º."], "answer": "Quinto y séptimo"},
        {"title": "Entre dos lugares", "problem": "¿Quién está entre el segundo y el cuarto?", "steps": ["El 2º y el 4º están separados por un lugar.", "Ese lugar es el 3º."], "answer": "Tercero (3º)"},
    ],
    mistakes=[
        {"wrong": "Decir que entre el 2º y el 4º están el 2º y el 4º.", "why": "Se incluyen los extremos.", "fix": "Entre deja afuera los extremos: sólo el 3º."},
        {"wrong": "Confundir antes con después.", "why": "No se mira el sentido de la fila.", "fix": "Antes es hacia el primero; después es hacia el último."},
    ],
    tiers={
        "recovery": [ex("¿Qué lugar está justo después del 4º?", "Quinto (5º)", "4º y luego 5º."), ex("¿Qué lugar está justo antes del 7º?", "Sexto (6º)", "6º está antes del 7º."), ex("¿Qué lugar está entre el 1º y el 3º?", "Segundo (2º)", "El 2º queda en medio.")],
        "understand": [
            ex("Fila: perro, gato, pez, ave, vaca. ¿Quién está después del pez?", "El ave", "Pez es 3º, el 4º es el ave."),
            ex("En la misma fila, ¿quién está antes del gato?", "El perro", "Perro 1º, gato 2º."),
            ex("En la misma fila, ¿quién está entre el gato y el ave?", "El pez", "Gato 2º, pez 3º, ave 4º."),
        ],
        "apply": [
            ex("En una fila de 10, ¿qué lugares están entre el 5º y el 8º?", "6º y 7º", "Quedan dos lugares en medio."),
            ex("Fila: sol, luna, mar, cielo, monte, río. ¿Quién está entre luna y cielo?", "El mar", "Luna 2º, mar 3º, cielo 4º."),
            ex("¿Quién está justo después del último en una fila de 5?", "Nadie", "El último no tiene a nadie detrás."),
        ],
        "reason": [
            ex("Marco dice que entre el 3º y el 5º está el 3º. ¿Es correcto?", "No; está el 4º", "El 3º es un extremo, no está entre."),
            ex("¿Cuántos lugares hay entre el 2º y el 9º?", "6", "3º, 4º, 5º, 6º, 7º y 8º."),
        ],
        "challenge": [
            ex("Soy el que está después del 6º y antes del 8º. ¿Qué lugar ocupo?", "Séptimo (7º)", "Entre el 6º y el 8º está el 7º."),
            ex("Estoy dos lugares antes del 10º. ¿Qué lugar ocupo?", "Octavo (8º)", "10º, 9º, 8º."),
        ],
    },
    context=[ex("En la cola de un cumpleaños, Sofía es la 4ª y Pablo el 6º. ¿Quién está entre ellos?", "El 5º", "Entre el 4º y el 6º está el 5º.")],
    selfcheck=[ex("¿Qué lugar está justo después del 8º?", "Noveno (9º)", "Después del 8º va el 9º."), ex("¿Qué lugar está entre el 6º y el 8º?", "Séptimo (7º)", "El 7º queda en medio."), ex("¿Qué lugar está antes del 2º?", "Primero (1º)", "El 1º va antes.")],
    open_task={
        "statement": "En una fila de 10 casillas, pon una flecha en la casilla 5º. Escribe qué lugar está antes, cuál está después y cuáles están entre el 3º y el 7º.",
        "example": "Antes del 5º está el 4º; después está el 6º. Entre el 3º y el 7º están el 4º, 5º y 6º.",
        "criteria": ["ubica el 5º", "indica antes y después", "lista los lugares entre"],
        "evidence": ["fila con flecha", "respuesta escrita"],
        "errors": ["incluir los extremos", "invertir antes y después"],
        "feedback": "Pide que marque los extremos con color para ver cuáles quedan adentro.",
    },
    reinforce="Con 10 tapas numeradas, pide a un compañero que adivine el lugar con pistas de antes, después y entre.",
    extend="Escribe tres pistas para encontrar al 7º sin decir su número.",
)

register(
    OA2, 4,
    materials="Filas de personajes y carreras escritas en cada ejercicio; lápiz.",
    use="Aprenderé a resolver problemas sobre el orden usando ordinales. Sirve para entender carreras, turnos y listas.",
    prior=["Sé usar los ordinales del primero al décimo.", "Sé decir antes, después y entre."],
    explain=[
        "En un problema de orden, primero identifica la fila y desde dónde empieza. Luego traduce cada pista a un lugar con ordinales. «Llegó antes que Ana» significa que su lugar es un número menor.",
        "Dibuja una tabla con los lugares 1º, 2º, 3º… y anota lo que ya sabes. Va completándose con cada pista. Si dos pistas llevan al mismo lugar, algo está mal y hay que revisar.",
        "Al final, comprueba que respondes lo que pregunta el problema: «¿quién?» pide un nombre y «¿qué lugar?» pide un ordinal. Lee la pregunta una vez más antes de escribir la respuesta.",
    ],
    vocab=[("turno", "el lugar en que le toca a alguien"), ("llegó antes", "ocupó un lugar menor"), ("llegó después", "ocupó un lugar mayor"), ("pista", "dato que ayuda a descubrir el orden"), ("comprobar", "revisar que la respuesta cumple todas las pistas")],
    worked=[
        {"title": "Una carrera", "problem": "Tres niños corren. Ana llegó antes que Beto, y Beto antes que Carla. ¿Quién ganó?", "steps": ["Ana está antes que Beto.", "Beto está antes que Carla.", "El orden es Ana 1ª, Beto 2º, Carla 3ª.", "Ganó la 1ª."], "answer": "Ana"},
        {"title": "Un turno", "problem": "Hay 5 niños. Dani es el 2º y Eva la 4ª. ¿Qué lugar está entre ellos?", "steps": ["Entre el 2º y el 4º queda un lugar.", "Ese lugar es el 3º."], "answer": "Tercer lugar (3º)"},
    ],
    mistakes=[
        {"wrong": "Decir que ganó el último.", "why": "Se confunde ganar con llegar último.", "fix": "Quien gana llega primero (1º)."},
        {"wrong": "Responder con un número cuando se pregunta un nombre.", "why": "No se lee la pregunta.", "fix": "Revisa si te piden quién o qué lugar."},
    ],
    tiers={
        "recovery": [ex("Luis llegó 1º y Mara 2ª. ¿Quién llegó primero?", "Luis", "El 1º llega primero."), ex("En una fila de 3, ¿qué lugar ocupa el último?", "Tercero (3º)", "Hay tres lugares."), ex("¿Quién ganó una carrera: el 1º o el 3º?", "El 1º", "Ganar es llegar primero.")],
        "understand": [
            ex("Pedro llegó 4º y Ema 2ª. ¿Quién llegó antes?", "Ema", "2º viene antes que 4º."),
            ex("Si una niña llegó 3ª, ¿cuántas personas llegaron antes?", "2", "Antes del 3º están el 1º y el 2º."),
            ex("Beto llegó justo después de Ana, que fue 5ª. ¿Qué lugar tuvo Beto?", "Sexto (6º)", "Después del 5º viene el 6º."),
        ],
        "apply": [
            ex("En una carrera de 6 corredores, ¿qué lugar tiene el que llegó justo antes del último?", "Quinto (5º)", "El último es el 6º y el anterior el 5º."),
            ex("Carla llegó 3ª, Diego 5º y Sara entre los dos. ¿Qué lugar tuvo Sara?", "Cuarto (4º)", "Entre el 3º y el 5º está el 4º."),
            ex("En una fila de 10 niños, Lucas está en el 7º lugar. ¿Cuántos niños hay detrás de él?", "3", "Detrás están el 8º, 9º y 10º."),
        ],
        "reason": [
            ex("Tomás dice que llegó 2º y que dos personas llegaron antes. ¿Es posible?", "No; antes de él llegó sólo una", "Antes del 2º sólo está el 1º."),
            ex("Nina llegó antes que Pía y Pía antes que Rosa. ¿Quién llegó última?", "Rosa", "El orden es Nina, Pía, Rosa."),
        ],
        "challenge": [
            ex("En una carrera de 5, Ana ganó, Bea llegó 3ª y Cris llegó justo antes de Dani, que fue último. ¿Qué lugar tuvo Cris?", "Cuarto (4º)", "El último es Dani, 5º, y Cris está justo antes: 4º."),
            ex("Hay 8 personas en una fila. ¿Cuántas hay entre la 2ª y la 7ª?", "4", "3ª, 4ª, 5ª y 6ª."),
        ],
    },
    context=[ex("En la feria de ciencias, 6 equipos se presentan por turnos. El equipo Sol va 3º y el equipo Luna va justo después. ¿Qué turno tiene Luna?", "Cuarto (4º)", "Después del 3º viene el 4º.")],
    selfcheck=[ex("¿Quién gana una carrera?", "El 1º", "Gana quien llega primero."), ex("Si soy el 5º, ¿qué lugar tiene el que está justo después?", "Sexto (6º)", "Después del 5º va el 6º."), ex("¿Cuántos lugares hay entre el 1º y el 4º?", "2", "Son el 2º y el 3º.")],
    open_task={
        "statement": "Cuatro amigos corrieron una carrera: Ana, Beto, Carla y Dani. Beto llegó antes que Ana. Carla llegó última. Dani llegó antes que Beto. Escribe el orden de llegada con ordinales y comprueba cada pista.",
        "example": "Orden: Dani 1º, Beto 2º, Ana 3ª, Carla 4ª. Comprobación: Beto llegó antes que Ana (2º antes de 3º), Carla llegó última (4ª), Dani llegó antes que Beto (1º antes de 2º).",
        "criteria": ["orden completo", "usa ordinales", "comprueba las tres pistas"],
        "evidence": ["lista ordenada", "comprobación escrita"],
        "errors": ["repetir un lugar", "olvidar una pista"],
        "feedback": "Pide dibujar una tabla con 4 lugares y completar pista por pista.",
    },
    reinforce="Juega con 4 amigos a ordenar una fila siguiendo una pista cada vez.",
    extend="Inventa un problema de carrera con 5 corredores y 4 pistas y pide que otra persona lo resuelva.",
)

register(
    OA3, 1,
    materials="Hasta 10 fichas, marco de diez (dos filas de cinco) dibujado en este cuaderno y tarjetas 0 a 10. Todas las cantidades están escritas.",
    use="Aprenderé a leer y escribir los números del 0 al 10 y a unirlos con la cantidad que representan. Sirve para saber cuántas cosas hay y escribirlo.",
    prior=["Sé contar objetos hasta 10.", "Reconozco algunos números escritos."],
    explain=[
        "Cada número del 0 al 10 tiene una cantidad y un símbolo. Si hay ● ● ● (tres puntos), la cantidad es tres y el símbolo es 3. El símbolo se llama numeral. Leer un numeral es decir su nombre; representarlo es mostrar cuántos hay.",
        "El 0 significa que no hay nada. Por ejemplo, si una caja está vacía hay cero lápices. Los números 1 a 10 se leen uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve y diez.",
        "Una ayuda es el marco de diez: dos filas de cinco casillas. Llenas tantas casillas como dice el número. Para 7, llenas una fila completa (5) y 2 de la segunda. Así ves de inmediato que 7 es 5 y 2 más.",
    ],
    vocab=[("numeral", "el número escrito con cifras"), ("cantidad", "cuántos objetos hay"), ("cero", "ninguno"), ("marco de diez", "dos filas de cinco casillas para mostrar números hasta 10"), ("representar", "mostrar un número con objetos o dibujos")],
    worked=[
        {"title": "Del dibujo al numeral", "problem": f"¿Qué numeral representa este marco? {frame(7)}", "steps": ["Cuento las casillas llenas: 5 en la primera fila y 2 en la segunda.", "5 y 2 forman 7.", "Escribo 7."], "answer": "7"},
        {"title": "Del numeral al dibujo", "problem": "Representa el 4 en un marco de diez.", "steps": ["Necesito 4 casillas llenas.", f"Dibujo: {frame(4)}.", "Compruebo: ● ● ● ● son cuatro."], "answer": frame(4)},
    ],
    mistakes=[
        {"wrong": "Escribir 6 cuando hay 9 puntos.", "why": "Se confunden los numerales 6 y 9.", "fix": "Cuenta de nuevo y compara con una tarjeta numérica."},
        {"wrong": "Decir que el 0 no existe.", "why": "Se piensa que «nada» no es un número.", "fix": "El 0 es el numeral de ninguno."},
    ],
    tiers={
        "recovery": [ex(f"Cuenta: {dots(2)}. ¿Qué numeral es?", "2", "Hay dos puntos."), ex(f"Cuenta: {dots(5)}. ¿Qué numeral es?", "5", "Cuento cinco puntos."), ex("Una caja vacía no tiene lápices. ¿Qué numeral usas?", "0", "Ninguno se escribe 0.")],
        "understand": [
            ex(f"¿Qué numeral muestra este marco? {frame(3)}", "3", "Hay tres casillas llenas."),
            ex(f"¿Qué numeral muestra este marco? {frame(8)}", "8", "Una fila llena y tres casillas de la otra."),
            ex("¿Cómo se lee el numeral 9?", "Nueve", "9 se lee nueve."),
        ],
        "apply": [
            ex("Representa 6 en un marco de diez.", frame(6), "Una fila llena (5) y una casilla más."),
            ex("Representa 10 en un marco de diez.", frame(10), "Las dos filas completas."),
            ex(f"Cuenta los puntos y escribe el numeral: {dots(9)}.", "9", "Cuento nueve puntos."),
        ],
        "reason": [
            ex(f"Ema contó {dots(6)} y escribió 9. ¿Qué error pudo cometer?", "Confundió 6 y 9; debe escribir 6", "Hay seis puntos."),
            ex("¿Por qué en el marco de diez siempre llenamos primero la fila de arriba?", "Porque se ve que 5 es una fila completa", "La primera fila de 5 ayuda a ver cuánto falta para 10."),
        ],
        "challenge": [
            ex(f"En el marco {frame(7)}, ¿cuántas casillas faltan para llegar a 10?", "3", "7 y 3 forman 10."),
            ex("Tengo 8 puntos. ¿Cuántos más necesito para tener 10?", "2", "8 y 2 forman 10."),
        ],
    },
    context=[ex("Un niño tiene 7 autitos. Escribe el numeral y dibuja el marco de diez.", f"7; {frame(7)}", "Siete autitos se muestran con 7 casillas llenas.")],
    selfcheck=[ex(f"¿Qué numeral muestra {frame(5)}?", "5", "Una fila completa."), ex("Escribe el numeral 'cero'.", "0", "Ninguno se escribe 0."), ex("¿Qué numeral viene después del 9?", "10", "Después del 9 viene el 10.")],
    open_task={
        "statement": "Elige los números 3, 6 y 9. Para cada uno dibuja un marco de diez, escribe el numeral y su nombre.",
        "example": f"3: {frame(3)} tres. 6: {frame(6)} seis. 9: {frame(9)} nueve.",
        "criteria": ["los marcos tienen la cantidad correcta", "escribe el numeral", "escribe el nombre"],
        "evidence": ["tres marcos", "numerales", "nombres"],
        "errors": ["llenar una casilla de más o de menos", "invertir 6 y 9"],
        "feedback": "Pide contar las casillas llenas en voz alta y compararlas con el numeral escrito.",
    },
    reinforce="Con 10 fichas, arma cada número del 0 al 10 en el marco de diez.",
    extend="Descubre cuántas casillas vacías quedan para cada número del 0 al 10 y completa una tabla.",
)

register(
    OA3, 2,
    materials="Fichas, hoja de papel y lápiz; las cantidades de cada ejercicio están escritas.",
    use="Aprenderé a pasar de objetos a dibujos simples. Sirve para guardar en un papel cuántas cosas había.",
    prior=["Sé leer y escribir los números del 0 al 10.", "Sé usar el marco de diez."],
    explain=[
        "Un dibujo simple representa una cantidad con puntos, rayitas o círculos. No hace falta dibujar cada objeto con detalle: si hay cinco manzanas, puedes dibujar cinco círculos. Lo importante es que la cantidad sea la misma.",
        "Para dibujar, cuenta los objetos y dibuja uno por uno el mismo número de marcas. Después cuenta tu dibujo para comprobar que coincide. También puedes agrupar las marcas de a cinco para contar más rápido.",
        "Del dibujo puedes pasar al numeral: cuenta las marcas y escribe el número. Así conectas lo concreto (objetos), lo pictórico (dibujo) y lo simbólico (numeral).",
    ],
    vocab=[("dibujo", "marcas que representan objetos"), ("marca", "punto, rayita o círculo que representa un objeto"), ("coincidir", "ser igual en cantidad"), ("concreto", "con objetos que puedo tocar"), ("simbólico", "con numerales")],
    worked=[
        {"title": "Dibujar objetos", "problem": "Hay 6 lápices sobre la mesa. Haz un dibujo simple.", "steps": ["Cuento los lápices: seis.", "Dibujo seis rayitas: | | | | | |.", "Cuento mis rayitas: seis."], "answer": "| | | | | |"},
        {"title": "Del dibujo al numeral", "problem": f"Mira el dibujo: {dots(8)}. ¿Qué numeral escribes?", "steps": ["Cuento los puntos: ocho.", "Escribo el numeral 8."], "answer": "8"},
    ],
    mistakes=[
        {"wrong": "Dibujar 5 marcas para 6 objetos.", "why": "Se salta un objeto al contar.", "fix": "Cuenta el dibujo y los objetos otra vez."},
        {"wrong": "Dibujar los objetos con tanto detalle que se pierde la cuenta.", "why": "Se dibuja más de lo necesario.", "fix": "Usa marcas simples que puedas contar."},
    ],
    tiers={
        "recovery": [ex("Hay 3 flores. Dibuja 3 marcas.", "● ● ●", "Se dibuja una marca por flor."), ex("Hay 5 gatos. Dibuja 5 marcas.", "● ● ● ● ●", "Dibujo cinco marcas."), ex("Hay 2 libros. Dibuja 2 marcas.", "● ●", "Dibujo dos marcas.")],
        "understand": [
            ex(f"¿Cuántos objetos muestra este dibujo? {dots(7)}", "7", "Hay siete puntos."),
            ex(f"¿Cuántos objetos muestra este dibujo? {dots(4)}", "4", "Hay cuatro puntos."),
            ex("¿El dibujo y los objetos deben tener la misma cantidad?", "Sí", "El dibujo representa la cantidad."),
        ],
        "apply": [
            ex("Hay 9 pelotas. Dibuja 9 marcas: una fila de 5 y otra fila con las que faltan.", f"{dots(5)} / {dots(4)}", "Cinco más cuatro son nueve."),
            ex("Hay 10 tapas. Dibuja 10 marcas en dos filas de cinco.", f"{dots(5)} / {dots(5)}", "Dos filas de cinco son diez."),
            ex(f"Escribe el numeral del dibujo: {dots(6)}.", "6", "Cuento seis puntos."),
        ],
        "reason": [
            ex(f"Raúl hizo este dibujo para 7 sillas: {dots(6)}. ¿Qué le falta?", "Una marca", "Seis marcas son una menos que siete."),
            ex("Ana dibujó 8 marcas para 5 galletas. ¿Es correcto?", "No", "Debe dibujar una marca por galleta: cinco."),
        ],
        "challenge": [
            ex("Dibuja 4 marcas y agrega 3 más. ¿Cuántas hay en total?", "7", "4 y 3 forman 7."),
            ex("Hay 10 casillas. Si dibujas 6, ¿cuántas quedan vacías?", "4", "6 y 4 forman 10."),
        ],
    },
    context=[ex("En la sala hay 8 sillas. Haz un dibujo simple de las sillas con marcas y escribe el numeral.", f"{dots(8)}; 8", "Ocho sillas, ocho marcas.")],
    selfcheck=[ex("Dibuja 4 marcas.", dots(4), "Dibujo cuatro marcas."), ex(f"¿Qué numeral es {dots(9)}?", "9", "Cuento nueve marcas."), ex("¿Qué es más fácil de contar: marcas simples o dibujos detallados?", "Marcas simples", "Se cuentan sin confundirse.")],
    open_task={
        "statement": "Mira tu mesa y junta 7 objetos. Haz un dibujo simple con marcas, escribe el numeral y cuenta tus marcas para comprobar.",
        "example": f"Junté 7 botones. Dibujé {dots(7)}. Escribí 7. Conté mis marcas: 7.",
        "criteria": ["dibuja la cantidad correcta", "escribe el numeral", "comprueba contando"],
        "evidence": ["dibujo", "numeral", "comprobación"],
        "errors": ["dibujar más o menos marcas", "olvidar el numeral"],
        "feedback": "Pide contar objetos y marcas al mismo tiempo; reconoce la comprobación.",
    },
    reinforce="Dibuja las cantidades 1 a 10 con marcas en una tira de papel.",
    extend="Dibuja un número de manera que se vea rápido cuántos hay, agrupándolo de a cinco.",
)

register(
    OA3, 3,
    materials="Dos marcos de diez dibujados en este cuaderno; hasta 20 fichas; lápiz.",
    use="Aprenderé a leer y representar los números del 11 al 20. Sirve para contar cantidades mayores a 10, como los alumnos de una sala.",
    prior=["Sé representar números hasta 10.", "Sé que diez fichas llenan un marco de diez."],
    explain=[
        "Los números del 11 al 20 son un diez más algunas unidades. El 13 es diez y tres más. Se lee trece. Del 11 al 15 los nombres son especiales (once, doce, trece, catorce, quince), y del 16 al 19 son dieciséis, diecisiete, dieciocho y diecinueve.",
        "Para representar el 14, llena un marco de diez completo y en otro marco pon 4 fichas. Así ves que 14 es 10 y 4. El 20 son dos marcos de diez llenos.",
        "El numeral tiene dos cifras: la primera dice cuántos dieces (1 diez) y la segunda cuántas unidades sueltas. En 14, el 1 es un diez y el 4 son cuatro unidades. En 20, el 2 son dos dieces y el 0 dice que no hay unidades sueltas.",
    ],
    vocab=[("diez", "un marco lleno"), ("unidades sueltas", "las fichas que no completan otro diez"), ("trece", "13, diez y tres"), ("veinte", "dos dieces"), ("cifra", "cada número que forma un numeral")],
    worked=[
        {"title": "Representar 14", "problem": "Representa 14 con dos marcos de diez.", "steps": ["Lleno el primer marco con 10 fichas.", "En el segundo pongo 4 fichas.", f"Dibujo: {frame(10)} y {frame(4)}.", "Compruebo: 10 y 4 son 14."], "answer": f"{frame(10)} y {frame(4)}"},
        {"title": "Leer un numeral", "problem": "Lee el numeral 17.", "steps": ["17 tiene un diez y 7 unidades.", "10 y 7 se lee diecisiete."], "answer": "Diecisiete"},
    ],
    mistakes=[
        {"wrong": "Escribir 41 para catorce.", "why": "Se invierten las cifras.", "fix": "Catorce es un diez y cuatro: 14."},
        {"wrong": "Contar 10 y luego repetir el 10.", "why": "No se continúa desde el diez.", "fix": "Después del diez sigue once."},
    ],
    tiers={
        "recovery": [ex("Escribe el numeral 'once'.", "11", "Un diez y una unidad."), ex("Escribe el numeral 'quince'.", "15", "Un diez y cinco."), ex("Escribe el numeral 'veinte'.", "20", "Son dos dieces completos.")],
        "understand": [
            ex("En el numeral 13, ¿cuántos dieces y cuántas unidades sueltas hay?", "Un diez y tres unidades", "El 1 es un diez y el 3 son tres unidades."),
            ex("¿Cómo se lee 18?", "Dieciocho", "10 y 8."),
            ex("¿Cuántos marcos de diez llenos hay en 20?", "2", "Veinte son dos dieces."),
        ],
        "apply": [
            ex("Representa 12 con dos marcos de diez.", f"{frame(10)} y {frame(2)}", "Un marco lleno y dos fichas."),
            ex("Representa 16 con dos marcos de diez.", f"{frame(10)} y {frame(6)}", "Un marco lleno y seis fichas."),
            ex("Escribe con numerales: diecinueve.", "19", "Diez y nueve."),
        ],
        "reason": [
            ex("Pedro dice que 15 tiene 15 dieces. ¿Qué error comete?", "Confunde diez con unidades; tiene un diez y cinco unidades", "El 1 vale diez."),
            ex("¿Por qué 20 no tiene unidades sueltas?", "Porque son dos marcos de diez completos", "No sobra ninguna ficha."),
        ],
        "challenge": [
            ex("Tengo un marco lleno y 9 fichas en otro. ¿Qué numeral formo y qué le falta para llegar a 20?", "19; 1 más", "10 y 9 son 19; 19 y 1 son 20."),
            ex("Ordena de menor a mayor: 17, 12, 20, 15.", "12, 15, 17, 20", "Se comparan los dieces y las unidades."),
        ],
    },
    context=[ex("En un curso hay 16 estudiantes. Escribe cómo se lee ese número y represéntalo en dos marcos de diez.", f"Dieciséis; {frame(10)} y {frame(6)}", "Un marco lleno y seis fichas.")],
    selfcheck=[ex("Escribe 'trece' con numerales.", "13", "Un diez y tres."), ex("Representa 11 con dos marcos.", f"{frame(10)} y {frame(1)}", "Un marco lleno y una ficha."), ex("¿Qué numeral viene después de 19?", "20", "Después del 19 va el 20.")],
    open_task={
        "statement": "Elige los números 12, 15 y 19. Para cada uno dibuja dos marcos de diez, escribe el numeral y su nombre y di cuántos dieces y cuántas unidades tiene.",
        "example": f"12: {frame(10)} y {frame(2)}, doce, un diez y dos. 15: {frame(10)} y {frame(5)}, quince, un diez y cinco. 19: {frame(10)} y {frame(9)}, diecinueve, un diez y nueve.",
        "criteria": ["dibuja los marcos correctos", "escribe numeral y nombre", "indica dieces y unidades"],
        "evidence": ["marcos dibujados", "numerales y nombres", "descomposición"],
        "errors": ["no completar el primer marco", "invertir las cifras"],
        "feedback": "Pide comprobar que el primer marco está lleno; reconoce las descomposiciones correctas.",
    },
    reinforce="Con 20 fichas, arma cada número del 11 al 20 con dos marcos.",
    extend="Descubre qué números entre 11 y 20 usan exactamente 5 fichas en el segundo marco.",
)

register(
    OA3, 4,
    materials="Fichas, marcos de diez, tarjetas con numerales y lápiz; las cantidades están escritas en cada ejercicio.",
    use="Aprenderé a mostrar un mismo número de tres formas: con objetos, con dibujo y con el numeral. Sirve para entender de verdad un número y explicárselo a otra persona.",
    prior=["Sé representar números del 0 al 20.", "Sé leer y escribir numerales."],
    explain=[
        "Un número se puede mostrar de tres maneras. La forma concreta usa objetos (fichas). La forma pictórica usa dibujos (marcas o marcos de diez). La forma simbólica usa el numeral (la cifra). Las tres dicen la misma cantidad.",
        "Para pasar de una forma a otra, empieza por contar. Si cuentas 13 fichas, dibujas 13 marcas y escribes 13. Si ves un numeral, haces el camino contrario: cuentas hasta ese número con fichas y dibujas.",
        "Si las tres formas no coinciden, hay un error. Por ejemplo, 12 fichas y el numeral 21 no son lo mismo. Compara siempre los tres: la cantidad de objetos, la de marcas y el valor del numeral.",
    ],
    vocab=[("concreto", "con objetos"), ("pictórico", "con dibujos"), ("simbólico", "con numerales"), ("coincidir", "decir lo mismo"), ("representación", "una manera de mostrar un número")],
    worked=[
        {"title": "Tres formas para el 13", "problem": "Muestra el 13 de tres formas.", "steps": ["Concreta: 13 fichas.", f"Pictórica: {frame(10)} y {frame(3)}.", "Simbólica: 13.", "Verifico que las tres dicen trece."], "answer": f"13 fichas; {frame(10)} y {frame(3)}; 13"},
        {"title": "Detectar un error", "problem": "Una persona usó 12 fichas y escribió 21. ¿Hay error?", "steps": ["12 fichas es un diez y dos unidades.", "21 sería dos dieces y una unidad.", "No coinciden."], "answer": "Sí; debía escribir 12"},
    ],
    mistakes=[
        {"wrong": "Escribir el numeral al revés (21 en vez de 12).", "why": "Se invierten las cifras.", "fix": "La primera cifra cuenta los dieces: 12 es un diez y dos."},
        {"wrong": "Dibujar una cantidad distinta de la de las fichas.", "why": "No se comprueba el dibujo.", "fix": "Cuenta tus marcas y compara con las fichas."},
    ],
    tiers={
        "recovery": [ex("Muestra el numeral de 5 fichas.", "5", "Cinco fichas se escriben 5."), ex("Muestra el numeral de 10 fichas.", "10", "Diez se escribe 10."), ex(f"Cuenta y escribe: {dots(7)}.", "7", "Cuento siete marcas.")],
        "understand": [
            ex("¿Qué dos formas de representar 9 coinciden: 9 fichas y el numeral 9, o 9 fichas y el numeral 6?", "9 fichas y el numeral 9", "Las dos dicen nueve."),
            ex("¿Qué forma de representar un número usa objetos que puedo tocar?", "La concreta", "Concreta es con objetos."),
            ex("¿Qué forma de representar un número usa numerales?", "La simbólica", "Simbólica es con numerales."),
        ],
        "apply": [
            ex("Muestra 14 con dibujo y numeral.", f"{frame(10)} y {frame(4)}; 14", "Un marco lleno y cuatro fichas."),
            ex("Muestra 17 con dibujo y numeral.", f"{frame(10)} y {frame(7)}; 17", "Un marco lleno y siete."),
            ex("Muestra 20 con dibujo y numeral.", f"{frame(10)} y {frame(10)}; 20", "Dos marcos llenos."),
        ],
        "reason": [
            ex("Lola dice que 11 fichas y el numeral 11 son lo mismo. ¿Tiene razón?", "Sí", "Las dos formas dicen once."),
            ex("Tomás usó 15 fichas y escribió 51. ¿Cuál es el error y la corrección?", "Invirtió las cifras; es 15", "15 es un diez y cinco."),
        ],
        "challenge": [
            ex("Tengo la forma simbólica 18. ¿Cuántas fichas necesito y cuántas quedan en el segundo marco?", "18 fichas; 8 en el segundo marco", "Un marco lleno y 8 fichas."),
            ex("Ordena de mayor a menor y muestra el numeral: 13, 19, 16.", "19, 16, 13", "Se comparan los dieces y las unidades."),
        ],
    },
    context=[ex("En una sala hay 15 sillas. Muestra el 15 con fichas, con un dibujo y con el numeral.", f"15 fichas; {frame(10)} y {frame(5)}; 15", "Un marco lleno y cinco fichas.")],
    selfcheck=[ex("¿Qué numeral muestra 12 fichas?", "12", "Un diez y dos."), ex(f"¿Qué numeral muestra {frame(10)} y {frame(8)}?", "18", "10 y 8 son 18."), ex("¿Cómo se lee 20?", "Veinte", "Son dos dieces completos.")],
    open_task={
        "statement": "Elige un número entre 11 y 20. Muéstralo con fichas (o su dibujo), con marcos de diez y con el numeral. Escribe una frase que diga cómo sabes que las tres formas coinciden.",
        "example": f"Elegí 16: 16 fichas, {frame(10)} y {frame(6)}, y el numeral 16. Coinciden porque en las tres hay un diez y seis unidades.",
        "criteria": ["muestra las tres formas", "las tres coinciden", "explica cómo lo sabe"],
        "evidence": ["fichas o dibujo", "marcos", "numeral", "frase"],
        "errors": ["cantidades que no coinciden", "invertir las cifras"],
        "feedback": "Pide comprobar los tres con el dedo; reconoce la explicación con dieces y unidades.",
    },
    reinforce="Haz tarjetas con tres formas del mismo número y empareja.",
    extend="Explica a otra persona por qué en 16 la cifra 1 es un diez y la cifra 6 son seis unidades.",
)
