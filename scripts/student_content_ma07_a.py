"""Cuaderno del estudiante de 7.º básico Matemática: OA 01 (adición y sustracción de números enteros)."""
from __future__ import annotations

from fractions import Fraction as F

from student_lessons import ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


MATERIALS = "Cuaderno, lápiz, regla y, si quieres, una calculadora. Todos los datos que necesitas están escritos en cada ejercicio."


def _int(n: int) -> str:
    text = f"{abs(n):,}".replace(",", ".") if abs(n) >= 1000 else str(abs(n))
    return ("−" if n < 0 else "") + text


def _show(value, form: str) -> str:
    """Formatea un resultado exacto: entero, fracción, número mixto o decimal con coma."""
    if isinstance(value, (int, float)):
        value = F(value).limit_denominator(10**6)
    if value.denominator == 1:
        return _int(int(value))
    neg = value < 0
    value = abs(value)
    if form == "dec":
        den = value.denominator
        for p in (2, 5):
            while den % p == 0:
                den //= p
        assert den == 1, f"decimal no exacto: {value}"
        text = f"{float(value):.6f}".rstrip("0").rstrip(".").replace(".", ",")
    elif form == "both" and value > 1:
        whole = value.numerator // value.denominator
        rest = value - whole
        text = f"{value.numerator}/{value.denominator}" + (f" (es decir, {whole} y {rest.numerator}/{rest.denominator})" if rest else "")
    elif form == "mixed" and value > 1:
        whole = value.numerator // value.denominator
        rest = value - whole
        text = f"{whole} y {rest.numerator}/{rest.denominator}"
    else:
        text = f"{value.numerator}/{value.denominator}"
    return ("−" if neg else "") + text


def cx(q, expr, why, unit="", form="frac"):
    """Ejercicio cerrado cuya respuesta se calcula exactamente a partir de `expr` (sintaxis Python con F(n, d))."""
    value = eval(expr, {"__builtins__": {}}, {"F": F})
    return ex(q, _show(value, form) + unit, why)


def lesson(oa, n, *, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, ctx, sc, op, reinforce, extend, mat=MATERIALS):
    register(
        oa, n, materials=mat, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": rec, "understand": und, "apply": app, "reason": rea, "challenge": cha},
        context=ctx, selfcheck=sc, open_task=op, reinforce=reinforce, extend=extend,
    )


OA1 = "MA07 OA 01"

# ------------------------------------------------------------------ OA 01 clase 1
lesson(
    OA1, 1,
    use="Aprenderé a ubicar números enteros en la recta numérica, a reconocer el opuesto de un número y a compararlos. Sirve para hablar de temperaturas bajo cero, pisos subterráneos o deudas.",
    prior=["Sé ubicar números naturales en una recta numérica.", "Sé comparar y ordenar números naturales."],
    explain=[
        "Los números enteros son los naturales (1, 2, 3…), el cero y los números negativos (−1, −2, −3…). En la recta numérica el cero está al medio, los positivos van hacia la derecha y los negativos hacia la izquierda. Los negativos sirven para medir cosas que están «bajo» una referencia: una temperatura bajo cero, un piso subterráneo o una deuda.",
        "Dos números enteros que están a la misma distancia del cero, pero a lados distintos, son opuestos. El opuesto de 5 es −5 y el opuesto de −5 es 5. El opuesto de 0 es 0. La distancia de un número al cero se llama valor absoluto y se escribe con barras: |−5| = 5 y |5| = 5. El valor absoluto nunca es negativo.",
        "Para comparar enteros usa la recta: de dos números, es mayor el que está más a la derecha. Por eso −2 es mayor que −9, aunque 9 sea mayor que 2. Todo número negativo es menor que cero y que cualquier número positivo. Para ordenar de menor a mayor, lee la recta de izquierda a derecha.",
    ],
    vocab=[("número entero", "número natural, cero o el opuesto de un natural"), ("opuesto", "número a la misma distancia del cero, pero al otro lado"), ("valor absoluto", "distancia de un número al cero; se escribe |−5| = 5"), ("negativo", "número menor que cero, a la izquierda del cero"), ("recta numérica", "línea donde cada número tiene su lugar y crece hacia la derecha")],
    worked=[
        W("Ordenar enteros", "Ordena de menor a mayor: 3, −4, 0, −1.", ["Ubico cada número en la recta: −4 y −1 a la izquierda del cero, 3 a la derecha.", "Leo de izquierda a derecha: primero −4, luego −1, luego 0 y al final 3."], "−4, −1, 0, 3"),
        W("Opuesto y valor absoluto", "Escribe el opuesto y el valor absoluto de −6.", ["El opuesto de −6 está a 6 unidades del cero hacia la derecha: es 6.", "El valor absoluto es la distancia al cero: |−6| = 6."], "Opuesto: 6; valor absoluto: 6"),
    ],
    mistakes=[
        M("Decir que −10 es mayor que −2 porque 10 es mayor que 2.", "Se comparó solo la parte numérica sin mirar el signo.", "Con negativos, el que está más a la izquierda es menor: −10 < −2."),
        M("Escribir que |−7| = −7.", "Se creyó que las barras no cambian el número.", "El valor absoluto es una distancia, no puede ser negativa: |−7| = 7."),
    ],
    rec=[
        ex("¿Cuál es el opuesto de 9?", "−9", "El opuesto de 9 está a 9 unidades del cero, hacia la izquierda."),
        ex("En la recta numérica, ¿qué entero está justo a la derecha de −4?", "−3", "Hacia la derecha los números crecen de uno en uno: −4, −3, −2…"),
        ex("En una recta están marcados −3, −2, −1, 0, 1, 2 y 3. ¿Cuántos pasos de una unidad hay que dar para ir de −3 a 0?", "3", "Se pasa por −2, −1 y se llega a 0: son tres pasos."),
    ],
    und=[
        ex("Ordena de menor a mayor: 2, −5, 0, −1.", "−5, −1, 0, 2", "De izquierda a derecha en la recta: −5 está más a la izquierda y 2 más a la derecha."),
        ex("¿Cuánto vale |−8|?", "8", "El valor absoluto es la distancia al cero y −8 está a 8 unidades."),
        ex("¿Cuál es mayor, −7 o −2?", "−2", "−2 está más a la derecha en la recta que −7."),
    ],
    app=[
        ex("Un ascensor está en el piso −3 (tercer subterráneo). El piso 0 es la entrada del edificio. ¿Cuántos pisos debe subir para llegar a la entrada?", "3", "De −3 a 0 hay 3 unidades: pasa por −2 y −1."),
        ex("Temperaturas de ejemplo de cuatro días: lunes −4 °C, martes 1 °C, miércoles −6 °C y jueves −1 °C. ¿Qué día fue el más frío?", "Miércoles", "−6 es el menor de los cuatro números: está más a la izquierda en la recta."),
        ex("Dos números enteros están a 6 unidades del cero y uno es el opuesto del otro. ¿Cuáles son?", "6 y −6", "A 6 unidades del cero hay dos lugares: 6 a la derecha y −6 a la izquierda."),
    ],
    rea=[
        ex("Ana afirma: «−12 es mayor que −3 porque 12 es mayor que 3». ¿Tiene razón?", "No", "−12 está más a la izquierda que −3, así que −12 es menor que −3."),
        ex("¿Cuántos números enteros hay entre −3 y 4, sin contar −3 ni 4?", "6", "Son −2, −1, 0, 1, 2 y 3: seis números."),
    ],
    cha=[
        ex("Un entero y su opuesto están separados por 14 unidades en la recta. ¿Cuál de los dos es positivo?", "7", "Cada uno está a la mitad de la distancia del cero: 14 ÷ 2 = 7 unidades; el positivo es 7."),
        ex("Un entero tiene valor absoluto 5 y es menor que el opuesto de −2. ¿Cuál es el entero?", "−5", "El opuesto de −2 es 2. Los enteros con valor absoluto 5 son 5 y −5, y solo −5 es menor que 2."),
    ],
    ctx=[ex("Un estacionamiento de ejemplo tiene el nivel −2 y el nivel −5, ambos bajo la calle (nivel 0). ¿Cuál de los dos niveles está más profundo?", "El nivel −5", "−5 está más lejos del cero hacia abajo que −2.")],
    sc=[
        ex("¿Cuál es el opuesto de −12?", "12", "El opuesto de un negativo es el positivo con el mismo valor absoluto."),
        ex("¿Cuál es mayor, −1 o −9?", "−1", "−1 está más a la derecha, más cerca del cero."),
        ex("¿Cuánto vale |−15|?", "15", "La distancia de −15 al cero es 15."),
    ],
    op=task(
        "Con estas temperaturas de ejemplo de una semana: lunes −2 °C, martes 5 °C, miércoles −7 °C, jueves 0 °C, viernes −1 °C. Dibuja una recta numérica de −8 a 6, marca los cinco valores y escribe los días ordenados del más frío al más cálido. Después explica con una frase por qué −7 °C es más frío que −1 °C.",
        "Del más frío al más cálido: miércoles (−7), lunes (−2), viernes (−1), jueves (0) y martes (5). −7 está más a la izquierda que −1, por eso es menor.",
        ["marca los cinco números en el lugar correcto", "ordena los días de menor a mayor", "explica la comparación usando la recta"],
        ["recta numérica dibujada", "lista de días ordenada", "frase de explicación"],
        ["ordenar por el tamaño del número sin mirar el signo", "marcar los negativos a la derecha del cero"],
        "Pide que lea la recta de izquierda a derecha y que compruebe que cada número es mayor que el anterior.",
    ),
    reinforce="Dibuja una recta de −6 a 6. Marca −5, −2, 0, 3 y 6, y escribe al lado de cada uno su opuesto.",
    extend="Escribe los tres enteros negativos que tienen valor absoluto menor que 4. Explica cómo sabes que cumplen y por qué no hay más.",
)

# ------------------------------------------------------------------ OA 01 clase 2
lesson(
    OA1, 2,
    use="Aprenderé a leer el signo + y el signo − como cambios: subir o bajar, ganar o gastar. Sirve para entender qué significa cada número en un problema del día a día.",
    prior=["Sé ubicar enteros en la recta numérica.", "Conozco el opuesto de un número."],
    explain=[
        "Un número entero puede decir dónde estás (una posición) o cuánto cambiaste (un movimiento). Si un buzo está en −5 m, esa es su posición. Si sube 2 m, su cambio es +2. El signo + indica un cambio hacia la derecha de la recta: subir, ganar, recibir, avanzar. El signo − indica un cambio hacia la izquierda: bajar, perder, pagar, retroceder.",
        "Dos cambios opuestos se anulan. Si un ascensor sube 3 pisos y luego baja 3 pisos, el cambio total es 0 y queda en el mismo piso. Por eso +3 y −3 son opuestos: juntos no producen ningún cambio de posición. Para varios cambios seguidos, avanza en la recta uno por uno, o junta primero los que se anulan.",
        "El mismo signo cambia de significado según el contexto. En una cuenta, +4.000 es un depósito y −4.000 es un giro. En una temperatura, +4 es calentar y −4 es enfriar. Antes de operar, escribe con un entero cada cambio y di en una frase qué representa. Así no confundes la posición inicial con el cambio.",
    ],
    vocab=[("cambio", "lo que sube o baja una cantidad; se escribe con + o −"), ("posición", "lugar donde está algo en la recta, por ejemplo el piso −2"), ("desplazamiento", "movimiento de un lugar a otro, con dirección"), ("saldo", "dinero que queda en una cuenta; si es negativo, se debe"), ("cambio total", "resultado de juntar todos los cambios seguidos")],
    worked=[
        W("Escribir cambios con signo", "Escribe como entero: «la temperatura bajó 6 grados» y «un cambio de 4 grados hacia arriba».", ["«Bajó» es un movimiento hacia la izquierda: −6.", "«Hacia arriba» es un movimiento hacia la derecha: +4."], "−6 y +4"),
        W("Movimientos opuestos", "Un dron de juguete sube 5 m y después baja 5 m. ¿Cuál es el cambio total?", ["Subir 5 m es +5 y bajar 5 m es −5.", "Se anulan: queda en el mismo lugar."], "0 m"),
    ],
    mistakes=[
        M("Pensar que +5 y −5 dan un cambio de 10.", "Se sumaron los tamaños sin mirar la dirección.", "Son movimientos contrarios: se anulan y el cambio total es 0."),
        M("Escribir −3 para «el ascensor subió 3 pisos».", "Se asoció «piso» con el signo negativo.", "Subir es avanzar hacia la derecha, así que el cambio es +3."),
    ],
    rec=[
        ex("Escribe con un número entero: «la temperatura bajó 4 grados».", "−4", "Bajar es un cambio hacia la izquierda, por eso lleva signo menos."),
        ex("Un ascensor sube 3 pisos y luego baja 3 pisos. ¿Cuál es el cambio total de piso?", "0", "+3 y −3 son opuestos y se anulan."),
        ex("En una cuenta de ejemplo, «se depositaron 2.000 pesos» se escribe +2.000. ¿Cómo se escribe «se giraron 2.000 pesos»?", "−2.000", "Un giro saca dinero: es el cambio contrario al depósito."),
    ],
    und=[
        ex("Una temperatura de ejemplo era −2 °C y tuvo un cambio de +5 °C. ¿Cuál es la temperatura final?", "3 °C", "Desde −2 se avanzan 5 lugares a la derecha: −1, 0, 1, 2, 3."),
        ex("Una cuenta de ejemplo parte en saldo 0. Se anotan +4.000 y luego −7.000. ¿Cuál es el saldo final?", "−3.000", "Después del depósito hay 4.000; al sacar 7.000 faltan 3.000, o sea −3.000."),
        ex("Una secuencia de cambios es +6, −6 y +2. ¿Cuál es el cambio total?", "2", "+6 y −6 se anulan; solo queda +2."),
    ],
    app=[
        ex("Un dron de juguete sube 12 m y después baja 15 m. ¿Cuál es el cambio total de altura, con signo?", "−3 m", "Subió 12 y bajó 15: bajó 3 más de lo que subió."),
        ex("Un termómetro marca −7 °C y se quiere llegar a 0 °C. ¿Qué cambio, con signo, hay que hacer?", "+7 °C", "De −7 a 0 hay 7 pasos hacia la derecha."),
        ex("Un ascensor sale del piso 2 y termina en el piso −3 (el piso 0 es la entrada). ¿Qué cambio de pisos, con signo, tuvo?", "−5", "Del 2 al 0 son 2 bajadas y del 0 al −3 son 3 más: 5 pisos hacia abajo."),
    ],
    rea=[
        ex("Luis dice: «si el cambio fue +9 y después −9, el cambio total fue 18». ¿Tiene razón?", "No", "Los dos cambios son opuestos y se anulan; el cambio total es 0."),
        ex("Rosa dice que un saldo de −2.000 es mejor que uno de −500. ¿Tiene razón?", "No", "−2.000 está más a la izquierda: se debe más dinero que con −500."),
    ],
    cha=[
        ex("Un submarino de ejemplo está en la posición −40 m. Sube 25 m, baja 10 m y sube 5 m. ¿En qué posición queda?", "−20 m", "−40 + 25 = −15; −15 − 10 = −25; −25 + 5 = −20."),
        ex("Una secuencia de tres cambios es +8, −3 y un tercero desconocido. El cambio total es 0. ¿Cuál es el tercer cambio?", "−5", "+8 − 3 = +5; para volver a 0 hace falta −5."),
    ],
    ctx=[ex("Un ascensor está en el piso 4 y hace estos viajes seguidos: baja 6 pisos y sube 2 pisos. ¿En qué piso queda?", "0", "4 − 6 = −2 y −2 + 2 = 0: llega a la entrada.")],
    sc=[
        ex("¿Qué signo lleva el cambio «el buzo subió 3 metros»?", "+", "Subir es un cambio hacia la derecha de la recta."),
        ex("Si se gana $1.000 y luego se gasta $1.000, ¿cuál es el cambio total?", "0", "Ganar y gastar la misma cantidad se anula."),
        ex("Una temperatura cambia en −4 °C y luego en −2 °C. ¿Cuál es el cambio total?", "−6 °C", "Dos bajadas seguidas se juntan: bajó 6 grados en total."),
    ],
    op=task(
        "Lee esta historia de ejemplo: una mochila de excursión parte a las 0 m de altura relativa al campamento. Sube 40 m por el sendero, baja 15 m a un mirador, sube 30 m y baja 10 m. Escribe los cuatro cambios con su signo, dibújalos en una recta vertical y escribe la altura final.",
        "Cambios: +40, −15, +30 y −10. Altura: 40, 25, 55 y 45. Altura final: +45 m sobre el campamento.",
        ["escribe cada cambio con el signo correcto", "dibuja el recorrido en una recta", "calcula la altura final"],
        ["lista de cambios con signo", "recta con flechas", "resultado final con unidad"],
        ["escribir las bajadas con signo +", "sumar los tamaños sin considerar la dirección"],
        "Pide que lea en voz alta cada flecha («sube», «baja») y que compruebe que el signo coincide.",
    ),
    reinforce="Escribe cuatro cambios de temperatura de ejemplo con signo (dos positivos y dos negativos) y di con una frase qué significa cada uno.",
    extend="Inventa una situación con tres cambios seguidos que termine con un cambio total de 0. Muéstrala en una recta.",
)

# ------------------------------------------------------------------ OA 01 clase 3
lesson(
    OA1, 3,
    use="Aprenderé a sumar números enteros usando la recta numérica y fichas de dos colores. Sirve para calcular saldos, temperaturas y posiciones sin equivocarme con los signos.",
    prior=["Sé qué significan + y − como cambios.", "Sé que un número y su opuesto se anulan."],
    explain=[
        "Sumar un número positivo es avanzar a la derecha en la recta. Sumar un negativo es retroceder a la izquierda. Para calcular −2 + 5, parte en −2 y avanza 5 lugares: llegas a 3. Para calcular 3 + (−7), parte en 3 y retrocede 7 lugares: llegas a −4. Los paréntesis separan el signo de la suma del signo del número.",
        "Con fichas, cada ficha roja vale −1 y cada ficha azul vale +1. Una roja con una azul forman un par cero y se pueden sacar. Para −3 + 5 se ponen 3 rojas y 5 azules, se sacan 3 pares cero y quedan 2 azules, o sea +2. Si los dos números tienen el mismo signo, no hay pares cero y se suman los tamaños: −3 + (−4) = −7.",
        "Regla corta. Mismo signo: se suman los valores absolutos y se deja el signo. Signo distinto: se restan los valores absolutos y se deja el signo del número con mayor valor absoluto. La suma de dos opuestos siempre es 0. Escribe el signo en cada paso y revisa en la recta si el resultado tiene sentido.",
    ],
    vocab=[("suma", "resultado de juntar dos o más cambios o cantidades"), ("sumando", "cada número que se suma"), ("ficha positiva", "ficha que vale +1"), ("ficha negativa", "ficha que vale −1"), ("par cero", "una ficha positiva y una negativa que se anulan")],
    worked=[
        W("Suma con signos distintos", "Calcula −9 + 4.", ["Signos distintos: resto los valores absolutos, 9 − 4 = 5.", "Gana el de mayor valor absoluto, que es −9: el resultado es negativo."], "−5"),
        W("Suma con fichas", "Calcula 3 + (−5) con fichas.", ["Pongo 3 fichas azules y 5 rojas.", "Saco 3 pares cero (azul con roja): quedan 2 rojas."], "−2"),
    ],
    mistakes=[
        M("Calcular −6 + 2 = −8.", "Se sumaron los valores absolutos aunque los signos eran distintos.", "Con signos distintos se resta: 6 − 2 = 4 y el signo es el de −6: −4."),
        M("Calcular −3 + (−4) = 1.", "Se restó pensando que había un signo distinto.", "Los dos son negativos: se suman los tamaños, 3 + 4 = 7, y se deja el signo: −7."),
    ],
    rec=[
        ex("Calcula −2 + 6 avanzando en la recta.", "4", "Parte en −2 y avanza 6 lugares a la derecha."),
        ex("Calcula −3 + (−4).", "−7", "Mismo signo: 3 + 4 = 7 y el resultado es negativo."),
        ex("Calcula 5 + (−5).", "0", "Son opuestos, se anulan."),
    ],
    und=[
        ex("Calcula −9 + 4.", "−5", "Signos distintos: 9 − 4 = 5 y gana el −9."),
        ex("Calcula 7 + (−2).", "5", "Signos distintos: 7 − 2 = 5 y gana el 7."),
        ex("Con fichas, tienes 4 rojas (−1 cada una) y 6 azules (+1 cada una). ¿Cuánto vale el conjunto?", "2", "Se anulan 4 pares cero y quedan 2 azules."),
    ],
    app=[
        ex("Calcula −15 + 8.", "−7", "15 − 8 = 7 y el mayor valor absoluto es −15."),
        ex("Calcula −12 + (−9).", "−21", "Mismo signo: 12 + 9 = 21 y se deja el signo menos."),
        ex("Calcula 14 + (−20).", "−6", "20 − 14 = 6 y gana el −20."),
    ],
    rea=[
        ex("Pía dice que −8 + 3 es 11. ¿Qué número es el correcto?", "−5", "Los signos son distintos: 8 − 3 = 5 y el resultado es negativo."),
        ex("Sin calcular, ¿el resultado de −20 + 7 es positivo o negativo?", "Negativo", "El valor absoluto de −20 es mayor que el de 7."),
    ],
    cha=[
        ex("Un número entero sumado con −9 da 4. ¿Qué número es?", "13", "Para llegar a 4 desde −9 hay que avanzar 13 lugares: −9 + 13 = 4."),
        ex("Calcula −6 + 10 + (−7) + 5.", "2", "−6 + 10 = 4; 4 − 7 = −3; −3 + 5 = 2."),
    ],
    ctx=[ex("Una cuenta de ejemplo tiene saldo −4.500 pesos (se debe esa cantidad). Se hace un depósito de 6.000 pesos. ¿Cuál es el saldo ahora?", "1.500 pesos", "−4.500 + 6.000: la diferencia es 1.500 y gana el positivo.")],
    sc=[
        ex("Calcula −5 + (−6).", "−11", "Mismo signo: 5 + 6 = 11 y signo menos."),
        ex("Calcula 9 + (−12).", "−3", "12 − 9 = 3 y gana el −12."),
        ex("¿Cuánto es −7 + 7?", "0", "Los opuestos suman cero."),
    ],
    op=task(
        "Un juego de ejemplo tiene cuatro rondas y en cada una se anota un puntaje: ronda 1: −8, ronda 2: +12, ronda 3: −5 y ronda 4: +3. Calcula el puntaje total de dos maneras: (a) avanzando en una recta numérica desde 0 y (b) con fichas rojas y azules. Escribe si los dos resultados coinciden.",
        "En la recta: 0, −8, 4, −1, 2. Con fichas: −8 y −5 son 13 fichas rojas; +12 y +3 son 15 fichas azules; se anulan 13 pares cero y quedan 2 azules. Total: +2.",
        ["usa correctamente la recta", "usa correctamente las fichas", "compara ambos resultados"],
        ["recta dibujada con saltos", "dibujo de fichas", "resultado final"],
        ["restar valores absolutos cuando los signos son iguales", "perder el signo del resultado"],
        "Pide que pruebe sumar los números en otro orden y compruebe que obtiene el mismo total.",
    ),
    reinforce="Calcula con la recta −4 + 9, 2 + (−6) y −5 + (−3). Dibuja las flechas de cada una.",
    extend="Busca dos enteros distintos, ambos negativos, cuya suma sea −10. Encuentra tres parejas diferentes.",
)

# ------------------------------------------------------------------ OA 01 clase 4
lesson(
    OA1, 4,
    use="Aprenderé a restar números enteros convirtiendo la resta en una suma del opuesto. Sirve para saber cuánto cambió una temperatura o cuánta diferencia hay entre dos alturas.",
    prior=["Sé sumar enteros con la recta y con fichas.", "Sé encontrar el opuesto de un número."],
    explain=[
        "Restar es lo contrario de sumar. La regla que usaremos dice que restar un número es lo mismo que sumar su opuesto: a − b = a + (−b). Por eso 5 − 3 = 5 + (−3) = 2 y también 5 − (−3) = 5 + 3 = 8. Restar un número negativo hace que el resultado aumente.",
        "Con fichas se ve bien. Para calcular 2 − (−3) necesitas quitar 3 fichas rojas, pero solo tienes 2 azules. Agrega 3 pares cero (3 azules y 3 rojas): el valor no cambia. Ahora quita las 3 rojas. Quedan 5 azules. Entonces 2 − (−3) = 5. En la recta, restar es ir en la dirección contraria a la de sumar.",
        "También puedes pensar la resta como la distancia con signo entre dos números: la diferencia a − b es lo que hay que sumar a b para llegar a a. Para saber cuánto cambió una temperatura que pasó de −4 °C a 3 °C, calculas 3 − (−4) = 3 + 4 = 7: subió 7 grados. Primero cambia la resta por una suma y luego aplica las reglas de la suma.",
    ],
    vocab=[("resta", "operación que quita una cantidad o calcula una diferencia"), ("diferencia", "resultado de una resta"), ("minuendo", "número del que se resta"), ("sustraendo", "número que se resta"), ("suma del opuesto", "convertir a − b en a + (−b)")],
    worked=[
        W("Resta de un negativo", "Calcula 4 − (−6).", ["Cambio la resta por la suma del opuesto: 4 + 6.", "Sumo números positivos: 10."], "10"),
        W("Diferencia entre temperaturas", "Una ciudad de ejemplo estaba a −5 °C y subió hasta 2 °C. ¿Cuánto cambió?", ["Cambio = final − inicial = 2 − (−5).", "Resto sumando el opuesto: 2 + 5 = 7."], "Subió 7 °C"),
    ],
    mistakes=[
        M("Calcular 3 − (−2) = 1.", "Se trató el signo menos doble como si no hiciera nada.", "Restar −2 es sumar 2: 3 + 2 = 5."),
        M("Calcular −4 − 3 = −1.", "Se restaron los valores absolutos sin cambiar la resta por suma del opuesto.", "−4 − 3 = −4 + (−3) = −7."),
    ],
    rec=[
        ex("¿Cuál es el opuesto de −8?", "8", "El opuesto de un negativo es el positivo con el mismo tamaño."),
        ex("Escribe 7 − 2 como suma del opuesto y calcula.", "7 + (−2) = 5", "Restar 2 es lo mismo que sumar −2."),
        ex("Calcula 6 − (−1).", "7", "Restar −1 equivale a sumar 1."),
    ],
    und=[
        ex("Calcula −3 − 5.", "−8", "−3 + (−5): mismo signo, 3 + 5 = 8 y signo menos."),
        ex("Calcula 8 − (−4).", "12", "Se cambia por 8 + 4."),
        ex("Calcula −6 − (−6).", "0", "Restar −6 es sumar 6, y −6 + 6 = 0."),
    ],
    app=[
        ex("Una piscina de ejemplo se midió a 0 m de profundidad en la orilla y a −3 m en el fondo. ¿Cuántos metros hay de diferencia entre la orilla y el fondo? (orilla − fondo)", "3", "0 − (−3) = 0 + 3 = 3."),
        ex("La temperatura pasó de −9 °C a −2 °C. ¿Cuántos grados cambió? (final − inicial)", "7", "−2 − (−9) = −2 + 9 = 7: subió 7 grados."),
        ex("Un buzo estaba a −12 m y bajó hasta −20 m. ¿Cuál es el cambio con signo? (final − inicial)", "−8", "−20 − (−12) = −20 + 12 = −8."),
    ],
    rea=[
        ex("Tomás calculó −2 − (−7) y escribió −9. ¿Cuál es el resultado correcto?", "5", "−2 − (−7) = −2 + 7 = 5; Tomás restó 7 en vez de sumarlo."),
        ex("¿Verdadero o falso? «Restar un número siempre disminuye el resultado».", "Falso", "Si se resta un negativo, el resultado aumenta: 3 − (−2) = 5, que es mayor que 3."),
    ],
    cha=[
        ex("¿Qué número hay que restar a 5 para obtener 12?", "−7", "5 − x = 12 se cumple con x = −7, porque 5 − (−7) = 5 + 7 = 12."),
        ex("Calcula −4 − (−9) − 6.", "−1", "−4 + 9 = 5 y 5 − 6 = −1."),
    ],
    ctx=[ex("En una ciudad de ejemplo, la temperatura mínima fue −6 °C y la máxima del día fue 11 °C. ¿Cuántos grados de diferencia hubo? (máxima − mínima)", "17", "11 − (−6) = 11 + 6 = 17 grados.")],
    sc=[
        ex("Calcula 10 − (−3).", "13", "Restar −3 es sumar 3."),
        ex("Calcula −7 − 2.", "−9", "−7 + (−2) = −9."),
        ex("Calcula −1 − (−8).", "7", "−1 + 8 = 7."),
    ],
    op=task(
        "Esta tabla de ejemplo muestra la temperatura de tres ciudades a las 8:00 y a las 15:00. Ciudad A: −4 °C y 3 °C. Ciudad B: 2 °C y −3 °C. Ciudad C: −8 °C y −5 °C. Para cada ciudad calcula el cambio (15:00 − 8:00) usando la suma del opuesto y escribe si la temperatura subió o bajó.",
        "A: 3 − (−4) = 3 + 4 = 7, subió. B: −3 − 2 = −3 + (−2) = −5, bajó. C: −5 − (−8) = −5 + 8 = 3, subió.",
        ["escribe la resta como suma del opuesto", "calcula bien el cambio de cada ciudad", "interpreta si subió o bajó"],
        ["tres cálculos escritos", "una frase por ciudad"],
        ["restar en el orden contrario", "ignorar el signo del sustraendo"],
        "Pide que compruebe cada resultado sumando el cambio a la temperatura inicial para llegar a la final.",
    ),
    reinforce="Convierte en sumas del opuesto y calcula: 9 − 4, 2 − 7, −3 − (−5) y −8 − 1.",
    extend="Explica con fichas por qué 1 − (−4) = 5. Haz el dibujo de las fichas antes y después de agregar los pares cero.",
)

# ------------------------------------------------------------------ OA 01 clase 5
lesson(
    OA1, 5,
    use="Aprenderé a resolver problemas con sumas y restas de enteros, a elegir una estrategia y a comprobar el resultado. Sirve para tomar decisiones con saldos, alturas y temperaturas.",
    prior=["Sé sumar enteros.", "Sé restar enteros como suma del opuesto."],
    explain=[
        "Para resolver un problema con enteros sigue cuatro pasos. Primero, lee y anota los datos con su signo. Segundo, decide si hay que sumar cambios o restar para hallar una diferencia. Tercero, calcula con la recta, con fichas o con las reglas de signos. Cuarto, comprueba si el resultado tiene sentido en la situación y escríbelo con su unidad.",
        "Hay tres formas de comprobar. Estimar: si sumas −48 + 19, el resultado debe ser negativo porque el sumando de mayor valor absoluto es negativo. Operar al revés: si a − b = c, entonces c + b debe dar a. Dibujar: marcar el recorrido en la recta y ver si llegas al mismo lugar. Si dos formas dan lo mismo, puedes confiar en el resultado.",
        "Compara estrategias antes de decidir. La recta es clara para números pequeños. Las fichas muestran por qué se anulan los pares cero. Las reglas de signos son más rápidas con números grandes. Elige la que entiendas mejor y explica tu razonamiento. Si el resultado no coincide con tu estimación, revisa los signos primero.",
    ],
    vocab=[("estimar", "calcular de forma aproximada para saber si un resultado es razonable"), ("comprobar", "revisar un resultado con otro camino"), ("operación inversa", "operación que deshace otra: la suma deshace la resta"), ("estrategia", "manera elegida para resolver un problema"), ("expresión", "cálculo escrito con números y signos, como −3 + 5")],
    worked=[
        W("Problema de varias etapas", "Un avión de ejemplo vuela a 1.000 m, baja 350 m y luego sube 120 m. ¿A qué altura queda?", ["Escribo los cambios: 1.000 + (−350) + 120.", "1.000 − 350 = 650 y 650 + 120 = 770.", "Compruebo: de 770 restar 120 da 650 y sumar 350 da 1.000."], "770 m"),
        W("Comparar dos estrategias", "Calcula −7 − (−3) con la recta y con la regla.", ["Regla: −7 + 3 = −4.", "Recta: parto en −7 y avanzo 3 lugares a la derecha: llego a −4."], "−4, con ambas estrategias"),
    ],
    mistakes=[
        M("Dejar el resultado sin comprobar y escribir 11 para −18 + 7.", "No se estimó el signo del resultado.", "El número de mayor valor absoluto es negativo, así que el resultado es negativo: −11."),
        M("Restar en el orden equivocado y escribir −7 como cambio al pasar de 2 °C a 9 °C.", "Se hizo inicial − final en vez de final − inicial.", "El cambio es final − inicial: 9 − 2 = +7."),
    ],
    rec=[
        ex("Escribe como suma de cambios: «subió 8, bajó 3».", "8 + (−3)", "Bajar 3 es un cambio de −3."),
        ex("Calcula 8 + (−3).", "5", "8 − 3 = 5, gana el positivo."),
        ex("Para comprobar que 9 − 4 = 5, ¿qué suma se hace?", "5 + 4", "La suma deshace la resta y debe volver a dar 9."),
    ],
    und=[
        ex("Calcula −14 + 9 y di si el resultado es positivo o negativo.", "−5, negativo", "14 − 9 = 5 y gana −14."),
        ex("Calcula −2 − (−11).", "9", "−2 + 11 = 9."),
        ex("Un número menos −6 da 4. Comprueba cuál es: ¿−2 o 10?", "−2", "−2 − (−6) = −2 + 6 = 4; 10 − (−6) daría 16."),
    ],
    app=[
        ex("Un estanque de ejemplo tiene el agua a −45 cm respecto de la marca de referencia. Sube 20 cm con la lluvia y baja 8 cm por evaporación. ¿Dónde queda el nivel?", "−33 cm", "−45 + 20 = −25 y −25 − 8 = −33."),
        ex("En una cuenta de ejemplo hay 3.000 pesos. Se pagan 5.000, luego se depositan 1.500 y luego se pagan 2.000. ¿Cuál es el saldo final?", "−2.500 pesos", "3.000 − 5.000 = −2.000; −2.000 + 1.500 = −500; −500 − 2.000 = −2.500."),
        ex("La temperatura mínima fue −3 °C y la máxima fue 12 °C. ¿Cuántos grados de diferencia hubo?", "15 °C", "12 − (−3) = 12 + 3 = 15."),
    ],
    rea=[
        ex("Dani resolvió −30 + 12 y obtuvo 18. Estima: ¿el resultado debería ser positivo o negativo?", "Negativo", "−30 tiene mayor valor absoluto que 12, así que el resultado es negativo (el correcto es −18)."),
        ex("Se calculó 13 − (−5) = 18. Para comprobar, se le suma al resultado el número que se restó. Escribe esa suma y su valor.", "18 + (−5) = 13", "El número que se restó fue −5; al sumarlo al 18 se vuelve al 13 inicial."),
    ],
    cha=[
        ex("Una mina de ejemplo tiene tres niveles seguidos: la entrada en 0 m, el túnel A en −85 m y el túnel B en −140 m. Un carro baja de la entrada al túnel A y luego al túnel B. ¿Cuánto bajó en el segundo tramo?", "55 m", "−140 − (−85) = −140 + 85 = −55: bajó 55 m."),
        ex("Dos números enteros suman −3 y su diferencia (primero − segundo) es 9. ¿Cuáles son, primero y segundo?", "3 y −6", "3 + (−6) = −3 y 3 − (−6) = 9."),
    ],
    ctx=[ex("Un termómetro de ejemplo marcó −5 °C a las 7:00, subió 9 °C hasta el mediodía y bajó 4 °C en la tarde. ¿Qué marcó en la tarde?", "0 °C", "−5 + 9 = 4 y 4 − 4 = 0.")],
    sc=[
        ex("Calcula −10 + 4 − 3.", "−9", "−10 + 4 = −6 y −6 − 3 = −9."),
        ex("Calcula 6 − (−9).", "15", "6 + 9 = 15."),
        ex("Para comprobar que −5 + 8 = 3, ¿qué resta se puede hacer?", "3 − 8", "Si −5 + 8 = 3, entonces 3 − 8 debe dar −5."),
    ],
    op=task(
        "Resuelve este problema de ejemplo y compruébalo por una vía distinta: un edificio tiene pisos desde el −3 (subterráneo) hasta el 4, y el piso 0 es la entrada. Una persona en ascensor parte en el piso −2, sube 3 pisos, baja 4 pisos y vuelve a subir 5. Escribe la expresión, el piso final y cómo lo comprobaste (recta, fichas u operación inversa).",
        "Expresión: −2 + 3 + (−4) + 5 = 2. Comprobación en la recta: −2, 1, −3, 2. Llega al piso 2.",
        ["escribe la expresión con signos", "calcula el piso final", "comprueba por otra vía"],
        ["expresión escrita", "recta o fichas", "frase de comprobación"],
        ["no cambiar el orden de la resta", "no comprobar el resultado"],
        "Pide que cuente los pasos de la recta y que compare con el resultado de las reglas.",
    ),
    reinforce="Resuelve y comprueba: parte en 10, baja 15, sube 6 y baja 4. Escribe la expresión y el resultado final.",
    extend="Escribe un problema de tu propia invención con tres cambios (uno de ellos una resta de un negativo) y resuélvelo por dos estrategias.",
)
