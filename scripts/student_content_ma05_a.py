"""Cuaderno del estudiante de 5.º básico Matemática: OA 01 (números naturales hasta 1.000 millones)."""
from __future__ import annotations

from student_lessons import arith, ex, fmt, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


MATERIALS = "Cuaderno, lápiz y calculadora si la tienes. Todos los datos que necesitas están escritos en cada ejercicio."


def lesson(oa, n, *, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, ctx, sc, op, reinforce, extend, mat=MATERIALS):
    register(
        oa, n, materials=mat, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": rec, "understand": und, "apply": app, "reason": rea, "challenge": cha},
        context=ctx, selfcheck=sc, open_task=op, reinforce=reinforce, extend=extend,
    )


def f(n):
    return fmt(n)


_U = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince",
      "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco",
      "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
_T = {3: "treinta", 4: "cuarenta", 5: "cincuenta", 6: "sesenta", 7: "setenta", 8: "ochenta", 9: "noventa"}
_H = {1: "ciento", 2: "doscientos", 3: "trescientos", 4: "cuatrocientos", 5: "quinientos", 6: "seiscientos", 7: "setecientos", 8: "ochocientos", 9: "novecientos"}


def _lt100(n):
    if n < 30:
        return _U[n]
    t, u = divmod(n, 10)
    return _T[t] if u == 0 else f"{_T[t]} y {_U[u]}"


def _lt1000(n):
    c, r = divmod(n, 100)
    if c == 0:
        return _lt100(r)
    if r == 0:
        return "cien" if c == 1 else _H[c]
    return f"{_H[c]} {_lt100(r)}"


def _apoc(text):
    if text.endswith("veintiuno"):
        return text[:-9] + "veintiún"
    if text.endswith("uno"):
        return text[:-3] + "un"
    return text


def words(n):
    """Número del 1 al 999.999.999 escrito con palabras."""
    m, rest = divmod(n, 1_000_000)
    t, u = divmod(rest, 1000)
    parts = []
    if m:
        parts.append("un millón" if m == 1 else f"{_apoc(_lt1000(m))} millones")
    if t:
        parts.append("mil" if t == 1 else f"{_apoc(_lt1000(t))} mil")
    if u:
        parts.append(_lt1000(u))
    return " ".join(parts)


def rnd(n, place):
    """Redondea n a la potencia de 10 `place` (mira la cifra siguiente a la derecha)."""
    return (n + place // 2) // place * place


OA1 = "MA05 OA 01"

# ------------------------------------------------------------------ clase 1
lesson(
    OA1, 1,
    use="Aprenderé a leer, escribir y dar el valor posicional de números de hasta nueve cifras. Sirve para entender cantidades muy grandes, como habitantes de una región o el costo de una obra.",
    prior=["Sé leer y escribir números de hasta seis cifras.", "Sé que 10 unidades de un lugar forman 1 unidad del lugar siguiente."],
    explain=[
        "Los números muy grandes se leen por periodos, que son grupos de tres cifras contados desde la derecha. El periodo de las unidades son las tres últimas cifras, el de los miles son las tres siguientes y el de los millones son las tres siguientes. El punto separa un periodo del otro.",
        "Dentro de cada periodo hay unidades, decenas y centenas. En 45.302.018 el periodo de los millones es 45, el de los miles es 302 y el de las unidades es 018. Se lee «cuarenta y cinco millones trescientos dos mil dieciocho». Cuando un periodo es 000 no se lee: 7.000.250 es «siete millones doscientos cincuenta».",
        "El valor posicional dice cuánto vale una cifra según el lugar donde está. En 45.302.018 el 5 está en las unidades de millón y vale 5.000.000. El cero también cuenta: es el que mantiene cada cifra en su lugar. Por eso 7.050.000 y 7.500.000 son números muy distintos.",
    ],
    vocab=[("periodo", "grupo de tres cifras, contado desde la derecha"), ("millón", "mil veces mil, es decir 1.000.000"), ("valor posicional", "lo que vale una cifra según el lugar que ocupa"), ("cifra", "cada símbolo del 0 al 9 que forma un número"), ("unidad de millón", "lugar que vale 1.000.000, el séptimo desde la derecha")],
    worked=[
        W("Leer un número con ceros interiores", "Escribe con palabras 30.040.600.", ["Separo los periodos: 30 | 040 | 600.", "Millones: «treinta millones». Miles: «cuarenta mil». Unidades: «seiscientos».", "Junto los periodos en orden."], "treinta millones cuarenta mil seiscientos"),
        W("Valor posicional de una cifra", "¿Qué valor tiene el 7 en 275.810.000?", ["Separo los periodos: 275 | 810 | 000.", "El 7 está en el periodo de los millones, en el lugar de las decenas (275: centena, decena, unidad).", "Decenas de millón: 7 × 10.000.000 = 70.000.000."], "70.000.000"),
    ],
    mistakes=[
        M("Escribir «cuatro millones trescientos mil» como 4.3000.000.", "Se pegaron los ceros sin respetar los periodos de tres cifras.", "Cada periodo lleva tres cifras: 4.300.000."),
        M("Decir que el 6 de 6.040.000 vale 6.000.", "Se confundió el lugar: el 6 está solo en el periodo de los millones.", "Cuenta las cifras desde la derecha: el 6 vale 6.000.000."),
    ],
    rec=[
        ex("¿Cuántas cifras tiene el número 52.480.000?", "8", "Los periodos son 52, 480 y 000: 2 + 3 + 3 = 8 cifras."),
        ex("En 3.405.200, ¿cuántos millones completos hay?", "3", "El periodo de los millones es solo la cifra 3."),
        ex("Escribe con cifras: dos millones trescientos mil.", "2.300.000", "Dos millones es 2.000.000 y trescientos mil es 300.000; juntos son 2.300.000."),
    ],
    und=[
        ex(f"Escribe con palabras el número {f(5_020_300)}.", words(5_020_300), "Millones: cinco; miles: veinte mil; unidades: trescientos."),
        ex("¿Qué número se escribe «ochenta millones cuarenta mil quince»?", "80.040.015", "Ochenta millones es 80.000.000, cuarenta mil es 40.000 y quince es 15."),
        ex("En 726.481.095, ¿qué lugar ocupa la cifra 4?", "Centena de mil", "El periodo de los miles es 481 y su primera cifra, el 4, está en las centenas de mil."),
    ],
    app=[
        ex(f"¿Cuánto vale la cifra 8 en el número {f(284_150_000)}?", "80.000.000", "Está en el periodo de los millones, lugar de las decenas: 8 × 10.000.000."),
        ex("Escribe con palabras el número 900.030.002.", words(900_030_002), "Millones: novecientos; miles: treinta mil; unidades: dos."),
        ex("Un museo recibió 2.005.060 visitas en el año. ¿Cuántas centenas de mil enteras tiene ese número?", "20", "2.005.060 es 2.000.000 más 5.060; los dos millones son 20 centenas de mil y 5.060 no completa otra."),
    ],
    rea=[
        ex("Rocío escribió «cuatro millones cinco mil» como 4.500.000. ¿Está bien?", "No, es 4.005.000", "Cinco mil es 5.000 y no 500.000: el periodo de los miles debe ser 005."),
        ex("Tomás dice que 9.000.909 se lee «nueve millones novecientos nueve mil». ¿Tiene razón?", "No, se lee nueve millones novecientos nueve", "El periodo de los miles es 000 y no se lee; 909 está en el periodo de las unidades."),
    ],
    cha=[
        ex("Con las cifras 7, 0 y 5, usando cada una una vez, forma el mayor número de tres cifras posible.", "750", "Se pone la cifra mayor primero (7), luego 5 y al final 0."),
        ex("Un número tiene 9 cifras y su periodo de los millones es 120. ¿Cuál es si las demás cifras son todas 0?", "120.000.000", "El 120 ocupa el periodo de los millones y los otros dos periodos son 000."),
    ],
    ctx=[ex("En una región ficticia viven 1.824.300 personas. Escribe con palabras ese número.", words(1_824_300), "Millones: un millón; miles: ochocientos veinticuatro mil; unidades: trescientos.")],
    sc=[
        ex("¿Cómo se escribe con cifras «treinta millones doscientos mil»?", "30.200.000", "Treinta millones es 30.000.000 y doscientos mil es 200.000."),
        ex("En 405.000.000, ¿qué cifra está en el lugar de las unidades de millón?", "5", "Los periodos son 405 | 000 | 000; la cifra 5 es la última del periodo de los millones."),
        ex("¿Cuántos periodos tiene un número de siete cifras?", "3", "Siete cifras forman un periodo de una cifra y dos de tres cifras."),
    ],
    op=task(
        "Elige uno de estos números: 6.070.400, 45.003.020 o 208.000.500. Escríbelo con palabras, indica el valor de su cifra más a la izquierda y explica por qué los ceros no se pueden quitar.",
        "Para 6.070.400: «seis millones setenta mil cuatrocientos». La cifra 6 vale 6.000.000. Si quitara los ceros quedaría 674, que es un número mucho menor.",
        ["separa los periodos", "lee bien los ceros interiores", "da el valor posicional de la primera cifra"],
        ["número escrito con palabras", "frase que explica el papel del cero"],
        ["no leer los periodos en orden", "quitar los ceros interiores"],
        "Pide que cuente las cifras y revise que cada periodo tenga tres; si hay un error, que lo corrija leyendo de derecha a izquierda.",
    ),
    reinforce="Escribe en tu cuaderno 345.678.912 y marca con una raya cada periodo. Lee en voz alta cada periodo con su nombre: millones, miles y unidades.",
    extend="Escribe un número de nueve cifras que tenga exactamente tres ceros y léelo con palabras. Explica dónde pusiste los ceros.",
)

# ------------------------------------------------------------------ clase 2
lesson(
    OA1, 2,
    use="Aprenderé a componer y descomponer números grandes en forma estándar y expandida. Sirve para comprobar que entiendo cuánto vale cada cifra.",
    prior=["Sé leer números de hasta nueve cifras.", "Conozco el valor posicional de cada cifra."],
    explain=[
        "La forma estándar es la manera habitual de escribir un número con cifras, como 4.205.300. La forma expandida lo separa en una suma donde cada cifra se escribe con su valor: 4.000.000 + 200.000 + 5.000 + 300. Los ceros no se escriben como sumandos porque no aportan nada.",
        "También puedes descomponer por periodos: 4.205.300 = 4 millones + 205 miles + 300 unidades. Otra forma usa multiplicaciones: 4 × 1.000.000 + 2 × 100.000 + 5 × 1.000 + 3 × 100. Las tres formas representan el mismo número.",
        "Para componer haces el camino inverso: sumas los valores y escribes el número. En 30.000.000 + 400.000 + 70 hay que fijarse bien en los lugares vacíos. Los lugares que faltan se llenan con ceros: 30.400.070. Revisa siempre que el resultado tenga la cantidad de cifras esperada.",
    ],
    vocab=[("forma estándar", "el número escrito con cifras de la manera habitual"), ("forma expandida", "el número escrito como suma del valor de cada cifra"), ("descomponer", "separar un número en partes que se suman"), ("componer", "juntar las partes para formar el número"), ("sumando", "cada número que se suma")],
    worked=[
        W("Escribir en forma expandida", "Escribe 62.040.805 en forma expandida.", ["Separo los periodos: 62 | 040 | 805.", "62.000.000 es 60.000.000 + 2.000.000; luego 40.000; luego 800 y 5.", "Los ceros no se escriben."], "60.000.000 + 2.000.000 + 40.000 + 800 + 5"),
        W("Componer en forma estándar", "¿Qué número es 700.000.000 + 5.000.000 + 300 + 9?", ["Ubico cada sumando: 700 millones, 5 millones, 300 y 9.", "Millones: 705; miles: 000; unidades: 309.", "Escribo los periodos juntos."], "705.000.309"),
    ],
    mistakes=[
        M("Escribir 3.050.200 como 3.000.000 + 50.000 + 2.000.", "Se cambió el valor de una cifra: el 2 está en las centenas, no en los miles.", "3.050.200 = 3.000.000 + 50.000 + 200."),
        M("Componer 40.000.000 + 6.000 como 4.006.000.", "Se perdió un cero y se escribieron 7 cifras en vez de 8.", "El 4 son decenas de millón: 40.006.000."),
    ],
    rec=[
        arith("Calcula la suma 2.000.000 + 300.000 + 5.000.", "2000000+300000+5000", "Cada sumando ocupa un lugar distinto."),
        ex("Escribe en forma expandida el número 8.400.000.", "8.000.000 + 400.000", "El 8 vale 8.000.000 y el 4 vale 400.000; los ceros no se escriben."),
        ex("En 4 × 1.000.000 + 3 × 1.000, ¿qué número se forma?", "4.003.000", "Son 4 millones y 3 mil; los demás lugares son ceros."),
    ],
    und=[
        ex("Escribe en forma expandida el número 90.060.200.", "90.000.000 + 60.000 + 200", "El 9 vale 90.000.000, el 6 vale 60.000 y el 2 vale 200."),
        arith("¿Qué número es 500.000.000 + 70.000 + 8?", "500000000+70000+8", "Se suman los valores y los lugares vacíos quedan en cero."),
        ex("Descompón 12.305.000 por periodos (millones, miles, unidades).", "12 millones + 305 miles", "Sus periodos son 12 | 305 | 000 y el último vale cero."),
    ],
    app=[
        ex("Escribe 408.020.036 en forma expandida.", "400.000.000 + 8.000.000 + 20.000 + 30 + 6", "Cada cifra distinta de cero se escribe con su valor posicional."),
        ex("Si un número es 6 × 10.000.000 + 2 × 100.000 + 9 × 10, ¿cuál es en forma estándar?", "60.200.090", "Son 60.000.000 más 200.000 más 90."),
        arith("Una constructora gastó $25.000.000 en materiales, $3.600.000 en sueldos y $400.000 en traslados. ¿Cuánto gastó en total?", "25000000+3600000+400000", "Se suman los tres gastos en pesos."),
    ],
    rea=[
        ex("Ana escribió 7.030.040 = 7.000.000 + 300.000 + 40. ¿Está bien?", "No, el 3 vale 30.000", "En 7.030.040 el 3 está en las decenas de mil, que valen 30.000."),
        ex("Diego dice que 5.000.000 + 60 + 700.000 y 5.700.060 son el mismo número. ¿Es cierto?", "Sí", "Ordenados, los sumandos son 5.000.000 + 700.000 + 60, que da 5.700.060."),
    ],
    cha=[
        ex("¿Cuántos sumandos tiene la forma expandida de 101.010.101?", "5", "Las cifras distintas de cero son cinco unos, con valores 100.000.000, 1.000.000, 10.000, 100 y 1."),
        ex("Un número tiene 9 cifras y su forma expandida tiene solo dos sumandos: 300.000.000 y 4.000. ¿Cuál es el número?", "300.004.000", "El 3 está en las centenas de millón y el 4 en las unidades de mil."),
    ],
    ctx=[ex("Una empresa ficticia ganó $120.000.000 en enero y $35.000.000 en febrero. Escribe en forma expandida lo ganado entre los dos meses.", "100.000.000 + 50.000.000 + 5.000.000", "La suma es 155.000.000 y tiene tres cifras distintas de cero: 1, 5 y 5.")],
    sc=[
        ex("Escribe en forma expandida el número 3.250.000.", "3.000.000 + 200.000 + 50.000", "Cada cifra 3, 2 y 5 se escribe con su valor."),
        arith("Calcula 400.000.000 + 20.000.000 + 5.000.", "400000000+20000000+5000", "Cada sumando es una cifra con su valor."),
        ex("¿Qué número es 8 millones + 14 miles + 9 unidades?", "8.014.009", "8 millones es 8.000.000, 14 miles es 14.000 y 9 es 9."),
    ],
    op=task(
        "Elige uno de estos números: 25.400.060, 130.002.500 o 7.090.003. Escríbelo en forma expandida y también por periodos (millones, miles y unidades). Luego inventa otro número parecido y haz lo mismo.",
        "Para 7.090.003: 7.000.000 + 90.000 + 3, y por periodos 7 millones + 90 miles + 3 unidades. Otro número parecido: 5.060.001.",
        ["usa los valores posicionales correctos", "no escribe sumandos con cero", "escribe las dos descomposiciones"],
        ["forma expandida en el cuaderno", "descomposición por periodos"],
        ["cambiar el valor de una cifra", "incluir ceros como sumandos"],
        "Pide que compruebe sumando todos los sumandos y que el resultado vuelva al número inicial.",
    ),
    reinforce="Toma el número 3.405.062. Escribe debajo de cada cifra su valor: 3.000.000, 400.000, 5.000, 60 y 2. Suma para comprobar.",
    extend="Escribe dos números distintos de nueve cifras que tengan casi la misma forma expandida, salvo por un sumando. Explica en qué se diferencian.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA1, 3,
    use="Aprenderé a comparar y ordenar números de hasta nueve cifras. Sirve para saber cuál cantidad es mayor, por ejemplo entre dos presupuestos o poblaciones.",
    prior=["Sé comparar números de hasta seis cifras.", "Conozco los símbolos < y > y la palabra «igual»."],
    explain=[
        "Para comparar dos números grandes primero cuenta las cifras. El que tiene más cifras es mayor, siempre que no empiece con cero. Así, 120.500.000 (9 cifras) es mayor que 99.999.999 (8 cifras) aunque todas las cifras de este último sean 9.",
        "Si tienen la misma cantidad de cifras, compara de izquierda a derecha. Se busca la primera cifra distinta y esa decide. Entre 482.310.500 y 482.390.100 las primeras cifras son iguales hasta 482.3, y luego viene 1 contra 9. Como 1 es menor que 9, 482.310.500 es menor.",
        "Para ordenar varios números, compáralos de a dos o ubica primero el mayor y el menor. Orden creciente es de menor a mayor. Orden decreciente es de mayor a menor. El símbolo < significa «es menor que», > significa «es mayor que» y = significa «es igual a». La punta del símbolo apunta al número menor.",
    ],
    vocab=[("comparar", "decidir cuál número es mayor, menor o si son iguales"), ("orden creciente", "de menor a mayor"), ("orden decreciente", "de mayor a menor"), ("<", "símbolo que significa «es menor que»"), (">", "símbolo que significa «es mayor que»")],
    worked=[
        W("Comparar con distinta cantidad de cifras", "Compara 98.760.000 y 102.000.000.", ["98.760.000 tiene 8 cifras y 102.000.000 tiene 9 cifras.", "El de 9 cifras es mayor."], "98.760.000 < 102.000.000"),
        W("Ordenar de menor a mayor", "Ordena de menor a mayor: 345.200.000, 345.020.000, 354.000.000, 34.520.000.", ["34.520.000 tiene 8 cifras y los demás 9: es el menor.", "Entre los de 9 cifras, 354.000.000 es mayor porque tras el 3 viene un 5 y en los otros un 4.", "Entre 345.200.000 y 345.020.000, la primera cifra distinta es 2 contra 0: el segundo es menor."], "34.520.000 < 345.020.000 < 345.200.000 < 354.000.000"),
    ],
    mistakes=[
        M("Decir que 9.999.999 es mayor que 10.000.000.", "Se comparó la cifra 9 con la cifra 1 sin contar las cifras de cada número.", "9.999.999 tiene 7 cifras y 10.000.000 tiene 8: el segundo es mayor."),
        M("Decir que 5.060.000 y 5.600.000 son iguales porque tienen las mismas cifras.", "Se ignoró que el lugar de cada cifra cambia el valor.", "Compara cifra a cifra: 5 = 5, luego 0 contra 6. Entonces 5.060.000 < 5.600.000."),
    ],
    rec=[
        ex("Escribe <, > o = : 4.500.000 __ 450.000.", ">", "4.500.000 tiene 7 cifras y 450.000 tiene 6."),
        ex("Escribe <, > o = : 300.000 + 5.000 __ 305.000.", "=", "300.000 + 5.000 es 305.000."),
        ex("¿Cuál es mayor: 61.000.000 o 6.100.000?", "61.000.000", "61.000.000 tiene 8 cifras y 6.100.000 tiene 7."),
    ],
    und=[
        ex("Compara 482.310.500 y 482.390.100 con < o >.", "482.310.500 < 482.390.100", "Las primeras cifras distintas son 1 y 9, y 1 es menor."),
        ex("Ordena de menor a mayor: 7.050.000, 7.005.000, 7.500.000.", "7.005.000 < 7.050.000 < 7.500.000", "Tras el 7 vienen 0 0 5, luego 0 5 0 y luego 5 0 0, de menor a mayor."),
        ex("Un número tiene 9 cifras y otro 8, sin ceros al inicio. ¿Cuál es mayor?", "El de 9 cifras", "Más cifras significa un número mayor."),
    ],
    app=[
        ex("Ordena de mayor a menor: 128.000.000, 98.500.000, 128.050.000, 12.900.000.", "128.050.000 > 128.000.000 > 98.500.000 > 12.900.000", "Los de 9 cifras van primero; entre ellos 128.050.000 supera a 128.000.000. Luego, entre los de 8 cifras, 98 > 12."),
        ex("Ciudad A tiene 2.340.000 habitantes y ciudad B tiene 2.304.000. ¿Cuál tiene más habitantes?", "Ciudad A", "Las cifras coinciden hasta 2.3; luego 4 contra 0, y 4 es mayor."),
        ex("¿Qué cifra puede ir en el cuadro para que 3.4_0.000 quede entre 3.460.000 y 3.480.000, sin ser igual a ninguno?", "7", "Con 7 queda 3.470.000. Con 6 o con 8 resultaría igual a un extremo."),
    ],
    rea=[
        ex("Lola dice: «11.111.111 es mayor que 99.999.999 porque tiene más unos». ¿Está en lo correcto?", "No", "Ambos tienen 8 cifras, así que se compara de izquierda a derecha: 1 < 9."),
        ex("Beto escribe 5.200.000 > 5.020.000 > 5.002.000. ¿Está bien ordenado de mayor a menor?", "Sí", "En cada par la primera cifra distinta es 2 contra 0, luego 2 contra 0, y siempre es mayor la de la izquierda."),
    ],
    cha=[
        ex("Con las cifras 4, 0, 7 y 2, usando cada una una vez, forma el menor número de cuatro cifras que no empiece con 0.", "2.047", "La primera cifra es la menor distinta de 0, que es 2; luego van 0, 4 y 7 en orden."),
        ex("¿Cuántos números naturales hay entre 99.999.998 y 100.000.002, sin contar los extremos?", "3", "Son 99.999.999, 100.000.000 y 100.000.001."),
    ],
    ctx=[ex("En una feria ficticia se vendieron entradas por $12.450.000 el sábado, $12.405.000 el domingo y $12.540.000 el lunes. ¿Qué día se vendió más?", "Lunes", "Tras el 12 vienen las cifras 4, 4 y 5; el 5 de 12.540.000 es la mayor.")],
    sc=[
        ex("Escribe <, > o = : 70.800.000 __ 7.080.000.", ">", "70.800.000 tiene 8 cifras y 7.080.000 tiene 7."),
        ex("Ordena de menor a mayor: 5.400.000, 5.040.000, 4.500.000.", "4.500.000 < 5.040.000 < 5.400.000", "4.500.000 empieza con 4; entre los otros dos, 0 < 4."),
        ex("¿Cuál es mayor, 300.000.001 o 300.000.010?", "300.000.010", "Cambia solo la penúltima cifra: 0 contra 1 a favor del segundo."),
    ],
    op=task(
        "Con estas cuatro poblaciones ficticias: 3.205.000, 3.250.000, 320.500 y 3.025.000, ordénalas de mayor a menor. Escribe los símbolos > entre ellas y explica cómo decidiste con una frase.",
        "Ordeno 3.250.000 > 3.205.000 > 3.025.000 > 320.500. Primero miré cuántas cifras tienen; después comparé las cifras de izquierda a derecha.",
        ["ordena correctamente", "usa los símbolos", "explica el criterio usado"],
        ["lista ordenada con símbolos", "frase explicativa"],
        ["no contar las cifras primero", "comparar sin respetar el lugar de cada cifra"],
        "Pide que cuente las cifras de cada número y subraye la primera cifra distinta en cada par.",
    ),
    reinforce="Escribe tres pares de números de siete cifras que empiecen igual. Subraya la primera cifra distinta y escribe < o >.",
    extend="Inventa dos números de nueve cifras que partan igual en sus primeras cinco cifras y explica cuál es mayor y por qué.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA1, 4,
    use="Aprenderé a aproximar (redondear) números grandes a la decena de mil, la centena de mil o la unidad de millón. Sirve para dar una cantidad fácil de recordar cuando no hace falta el valor exacto.",
    prior=["Sé redondear números de hasta cuatro cifras.", "Sé qué valor tiene cada lugar de un número grande."],
    explain=[
        "Aproximar es cambiar un número por otro cercano y más simple. Se usa cuando no necesitas el valor exacto, por ejemplo al decir «unos tres millones de personas». El número aproximado termina en ceros desde el lugar elegido.",
        "Para redondear, primero marca el lugar al que quieres aproximar. Luego mira la cifra que está justo a la derecha. Si es 5 o más, la cifra marcada sube 1. Si es 0, 1, 2, 3 o 4, la cifra marcada se queda igual. Todas las cifras a la derecha pasan a ser ceros.",
        "Ejemplo: 3.482.917 a la centena de mil. La centena de mil es el 4. La cifra a la derecha es 8, que es 5 o más, así que el 4 sube a 5. Resultado: 3.500.000. Si fuera 3.442.917, la cifra a la derecha es 4, el 4 se queda y el resultado es 3.400.000.",
    ],
    vocab=[("aproximar", "cambiar un número por otro cercano y más simple"), ("redondear", "aproximar a un lugar usando la cifra de su derecha"), ("cifra vecina", "la cifra que está justo a la derecha del lugar elegido"), ("centena de mil", "lugar que vale 100.000, el sexto desde la derecha"), ("decena de mil", "lugar que vale 10.000, el quinto desde la derecha")],
    worked=[
        W("Aproximar a la centena de mil", "Aproxima 6.749.300 a la centena de mil.", ["Separo periodos: 6 | 749 | 300. La centena de mil es el 7.", "La cifra vecina es 4, que es menor que 5: el 7 se queda.", "Las cifras a la derecha pasan a cero."], "6.700.000"),
        W("Aproximar a la unidad de millón", "Aproxima 48.512.000 a la unidad de millón.", ["La unidad de millón es el 8 (48 | 512 | 000).", "La cifra vecina es 5, así que el 8 sube.", "8 + 1 = 9; las cifras a la derecha pasan a cero."], "49.000.000"),
    ],
    mistakes=[
        M("Aproximar 6.749.300 a la centena de mil y escribir 6.800.000.", "Se miró el 9 en vez del 4, que es la cifra vecina inmediata.", "Solo se mira la cifra de la derecha. Es 4, luego queda 6.700.000."),
        M("Aproximar 2.960.000 a la centena de mil y escribir 2.900.000.", "No se subió la centena de mil aunque la cifra vecina es 6.", "La vecina es 6, así que el 9 sube a 10 y arrastra al millón: queda 3.000.000."),
    ],
    rec=[
        ex("¿Qué cifra se mira para aproximar 5.372.000 a la centena de mil?", "7", "La centena de mil es el 3, y la cifra a su derecha, la decena de mil, es 7."),
        ex("Si la cifra vecina es 4, ¿la cifra marcada sube o se queda igual?", "Se queda igual", "Para subir la cifra vecina debe ser 5 o más."),
        ex("Si la cifra vecina es 5, ¿la cifra marcada sube o se queda igual?", "Sube", "Cuando la cifra vecina es 5 o más, la cifra marcada sube 1."),
    ],
    und=[
        ex(f"Aproxima {f(3_482_917)} a la centena de mil.", f(rnd(3_482_917, 100_000)), "La centena de mil es 4; la cifra vecina es 8, así que sube a 5."),
        ex(f"Aproxima {f(25_340_000)} a la unidad de millón.", f(rnd(25_340_000, 1_000_000)), "La unidad de millón es 5; la vecina es 3, así que se queda."),
        ex(f"Aproxima {f(71_250_900)} a la decena de mil.", f(rnd(71_250_900, 10_000)), "La decena de mil es 5; la cifra vecina es 0, así que se queda."),
    ],
    app=[
        ex(f"Aproxima {f(687_450_000)} a la centena de millón.", f(rnd(687_450_000, 100_000_000)), "La centena de millón es 6; la vecina es 8, así que sube a 7."),
        ex(f"Una ciudad ficticia tiene {f(4_950_000)} habitantes. ¿Cuántos son, aproximando a la unidad de millón?", f(rnd(4_950_000, 1_000_000)), "La unidad de millón es 4, la vecina es 9, luego sube a 5."),
        ex(f"Aproxima {f(9_960_300)} a la centena de mil.", f(rnd(9_960_300, 100_000)), "La centena de mil es 9, la vecina es 6 y sube: 9 + 1 = 10, y cambia también el millón."),
    ],
    rea=[
        ex("Fer aproxima 12.449.999 a la decena de mil y escribe 12.500.000. ¿Está bien?", "No, es 12.450.000", "La decena de mil es la segunda cifra 4 y su vecina es 9: sube a 5 y queda 12.450.000."),
        ex("Un número aproximado a la centena de mil dio 5.300.000. ¿Puede el número original ser 5.352.000?", "No", "5.352.000 tiene vecina 5 después del 3, así que sube y da 5.400.000."),
    ],
    cha=[
        ex("¿Cuál es el menor número de siete cifras que se aproxima a 3.000.000 en la unidad de millón?", "2.500.000", "Todos los números desde 2.500.000 hasta 3.499.999 se aproximan a 3.000.000."),
        ex("¿Cuál es el mayor número de siete cifras que se aproxima a 3.000.000 en la unidad de millón?", "3.499.999", "Si pasara a 3.500.000, la vecina sería 5 y subiría a 4.000.000."),
    ],
    ctx=[ex("Un teatro ficticio vendió 1.275.600 entradas en un año. Aproxima esa cantidad a la centena de mil.", f(rnd(1_275_600, 100_000)), "La centena de mil es 2; la vecina es 7, así que sube a 3: 1.300.000.")],
    sc=[
        ex(f"Aproxima {f(5_261_000)} a la unidad de millón.", f(rnd(5_261_000, 1_000_000)), "La vecina es 2, el 5 se queda."),
        ex(f"Aproxima {f(48_990_000)} a la decena de mil.", f(rnd(48_990_000, 10_000)), "La decena de mil es 9 y su vecina es 0, así que no cambia."),
        ex(f"Aproxima {f(130_500_000)} a la centena de millón.", f(rnd(130_500_000, 100_000_000)), "La centena de millón es 1, la vecina es 3 y se queda."),
    ],
    op=task(
        "Elige el número 7.648.215 o 52.380.000. Aproxímalo a tres lugares distintos (decena de mil, centena de mil y unidad de millón) y explica en cada caso qué cifra miraste.",
        "Para 7.648.215: a la decena de mil queda 7.650.000 (miré el 8), a la centena de mil queda 7.600.000 (miré el 4) y a la unidad de millón queda 8.000.000 (miré el 6).",
        ["aproxima a tres lugares", "nombra la cifra vecina", "pone ceros a la derecha"],
        ["tres aproximaciones escritas", "frase sobre la cifra vecina"],
        ["mirar la cifra equivocada", "no arrastrar el aumento"],
        "Pide que subraye en cada caso el lugar y la cifra vecina antes de escribir el resultado.",
    ),
    reinforce="Redondea 3.456.789 a la unidad de millón, a la centena de mil y a la decena de mil. Cada vez subraya la cifra que miraste.",
    extend="Busca un número de siete cifras que, aproximado a la decena de mil y a la centena de mil, dé el mismo resultado. Explica cómo lo encontraste.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA1, 5,
    use="Aprenderé a usar números de hasta nueve cifras en situaciones reales, a compararlos y a revisar si una lectura o una aproximación tiene sentido. Sirve para entender datos de noticias, mapas y presupuestos.",
    prior=["Sé leer, componer, comparar y aproximar números de hasta nueve cifras."],
    explain=[
        "Los números grandes aparecen cuando se cuentan habitantes, se miden distancias o se calcula el presupuesto de una obra. Para trabajar con ellos conviene revisar cuatro cosas: cuántas cifras tienen, cómo se leen, cuánto vale cada cifra y si el resultado tiene sentido en la situación.",
        "Una buena comprobación es leer el número en voz alta y escribirlo de nuevo con palabras. Otra es aproximar y ver si el valor es parecido. Si una ciudad tiene 2.350.000 habitantes y lees «dos mil trescientos cincuenta», algo falló: el número tiene siete cifras y no cuatro.",
        "Al comparar cantidades también importa la unidad. No se pueden comparar 2.000.000 de personas con 2.000.000 de pesos. Primero compara solo cantidades del mismo tipo y luego decide. Al comunicar tu resultado, escribe el número con su unidad: «3.400.000 personas», «45.000.000 de pesos».",
    ],
    vocab=[("situación real", "un caso de la vida donde se usa un número"), ("unidad", "lo que se está contando o midiendo, como personas o pesos"), ("comprobar", "revisar que un resultado tenga sentido"), ("estimar", "calcular un valor aproximado"), ("magnitud", "tamaño de una cantidad, por ejemplo cuántas cifras tiene")],
    worked=[
        W("Detectar una lectura incorrecta", "Un afiche dice «Participaron 3.200.500 personas» y alguien lo leyó «tres mil doscientos quinientos». ¿Qué falló?", ["3.200.500 tiene 7 cifras: 3 | 200 | 500.", "Se debe leer «tres millones doscientos mil quinientos».", "La lectura omitió el periodo de los millones."], "Faltó leer los millones: son tres millones doscientos mil quinientos"),
        W("Ordenar datos con unidad", "Tres ferias ficticias tuvieron 1.450.000, 1.405.000 y 1.540.000 visitantes. Ordena de menor a mayor.", ["Todos tienen 7 cifras y empiezan en 1.", "Comparo la siguiente cifra: 4, 4 y 5, así que 1.540.000 es el mayor.", "Entre 1.450.000 y 1.405.000 la primera cifra distinta es 5 contra 0."], "1.405.000 < 1.450.000 < 1.540.000 visitantes"),
    ],
    mistakes=[
        M("Comparar 2.000.000 de personas con 2.000.000 de pesos y decir que son iguales.", "Se compararon unidades distintas.", "Solo se comparan cantidades de lo mismo, con su unidad."),
        M("Aceptar que la población de una ciudad grande es 235 porque «el número es chico y fácil».", "No se revisó la magnitud: una ciudad grande tiene muchos miles o millones de habitantes.", "Revisa cuántas cifras debería tener y compara con una aproximación."),
    ],
    rec=[
        ex("¿Cuántas cifras tiene 12.450.000?", "8", "Los periodos son 12, 450 y 000."),
        ex("Escribe con cifras: quince millones.", "15.000.000", "Quince millones es 15 seguido de seis ceros."),
        ex("¿Qué es más grande: 3.400.000 personas o 340.000 personas?", "3.400.000 personas", "El primero tiene 7 cifras y el segundo 6."),
    ],
    und=[
        ex("Lee con palabras la cantidad $20.050.000.", words(20_050_000) + " pesos", "Millones: veinte; miles: cincuenta mil."),
        ex("Una distancia ficticia es de 149.600.000 metros. ¿Cuánto vale la cifra 9?", "9.000.000", "El 9 está en las unidades de millón."),
        ex("Un cartel dice que un parque tuvo «cuarenta mil dos visitantes». Escríbelo con cifras.", "40.002", "Cuarenta mil es 40.000 y dos es 2."),
    ],
    app=[
        ex("Una ciudad ficticia tiene 1.208.000 habitantes y otra 1.280.000. ¿Cuál tiene más y cuántos millones enteros tiene cada una?", "La segunda; cada una tiene 1 millón entero", "1.280.000 supera a 1.208.000 y ninguna llega a 2.000.000."),
        arith("Una escuela recolectó $2.350.000 en una rifa y $1.480.000 en una venta. ¿Cuánto dinero reunió?", "2350000+1480000", "Se juntan las dos recaudaciones.", unit=" pesos"),
        ex(f"Un ministerio ficticio gastó ${f(18_648_000)} en un proyecto. Aproxima ese gasto a la unidad de millón.", f"${f(rnd(18_648_000, 1_000_000))}", "La unidad de millón es 8, la vecina es 6, y sube a 9."),
    ],
    rea=[
        ex("Leo lee 4.050.300 como «cuatro millones cincuenta mil trescientos». ¿Lo leyó bien?", "Sí", "Periodos: 4 | 050 | 300, es decir cuatro millones, cincuenta mil y trescientos."),
        ex("Pía dice que puede saber si 8.000.000 de personas es mayor que $9.000.000 mirando solo los números. ¿Tiene razón?", "No", "Una cantidad cuenta personas y la otra mide dinero; no se pueden comparar."),
    ],
    cha=[
        ex("Un número de 9 cifras tiene 105 en el periodo de los millones, 070 en el de los miles y 008 en el de las unidades. Escríbelo y aproxímalo a la centena de mil.", "105.070.008 y 105.100.000", "La centena de mil es 0 y su vecina es 7: sube a 1, y queda 105.100.000."),
        ex("¿Cuántas unidades de millón enteras hay entre 450.000.000 y 460.000.000, sin contar los extremos?", "9", "Son 451, 452, 453, 454, 455, 456, 457, 458 y 459 millones."),
    ],
    ctx=[ex("Un museo ficticio recibió 987.600 visitantes en un año y otro 1.025.400. ¿Cuál recibió más y cuántos más?", "El segundo, 37.800 más", "1.025.400 − 987.600 = 37.800 visitantes.")],
    sc=[
        ex("Escribe con cifras: ochenta y cinco millones doscientos mil.", "85.200.000", "85 millones y 200 mil."),
        ex("¿Cuál es mayor: 9.999.999 o 10.000.000?", "10.000.000", "10.000.000 tiene una cifra más."),
        ex(f"Aproxima {f(6_449_999)} a la unidad de millón.", f(rnd(6_449_999, 1_000_000)), "La vecina es 4, así que el 6 se queda."),
    ],
    op=task(
        "Usa estos datos ficticios de tres ciudades: Norte 2.480.000 habitantes, Centro 2.048.000 y Sur 2.408.000. Ordénalas de mayor a menor, aproxima cada población a la centena de mil y escribe una frase para comunicar el resultado con su unidad.",
        "Orden: Norte (2.480.000) > Sur (2.408.000) > Centro (2.048.000). Aproximadas: 2.500.000, 2.400.000 y 2.000.000. Norte es la más poblada, con unos 2.500.000 habitantes.",
        ["ordena bien", "aproxima a la centena de mil", "comunica con unidad"],
        ["lista ordenada", "aproximaciones", "frase con unidad"],
        ["ordenar por la última cifra", "olvidar la unidad"],
        "Pide que compare cifra a cifra de izquierda a derecha y que lea su respuesta final en voz alta.",
    ),
    reinforce="Anota tres cantidades grandes que veas en una noticia o un cartel (si no tienes, inventa tres de más de seis cifras) y escríbelas con palabras y con cifras.",
    extend="Explica con un ejemplo por qué 5.000.000 de pesos y 5.000.000 de personas no se pueden comparar directamente.",
)
