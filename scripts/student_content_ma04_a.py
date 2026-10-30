"""Cuaderno del estudiante de 4.º básico Matemática: OA 01 (números hasta 10.000) y OA 02 (cálculo mental)."""
from __future__ import annotations

from student_lessons import arith, ex, fmt, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


MATERIALS = "Cuaderno, lápiz y, si quieres, tapas o palitos para representar. Todos los datos que necesitas están escritos en cada ejercicio."


def lesson(oa, n, *, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, ctx, sc, op, reinforce, extend, mat=MATERIALS):
    register(
        oa, n, materials=mat, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": rec, "understand": und, "apply": app, "reason": rea, "challenge": cha},
        context=ctx, selfcheck=sc, open_task=op, reinforce=reinforce, extend=extend,
    )


def fill(start, step, count, blanks, why, lead="Completa la secuencia"):
    values = [start + step * i for i in range(count)]
    shown = ", ".join("__" if i in blanks else fmt(v) for i, v in enumerate(values))
    return ex(f"{lead}: {shown}.", ", ".join(fmt(values[i]) for i in blanks), why)


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


def words(n):
    """Número del 1 al 10.000 escrito con palabras."""
    if n == 10000:
        return "diez mil"
    m, r = divmod(n, 1000)
    head = "" if m == 0 else ("mil" if m == 1 else f"{_U[m]} mil")
    tail = "" if r == 0 else _lt1000(r)
    return f"{head} {tail}".strip()


def blk(m, c, d, u):
    """Bloques: ◼ unidad de mil, ▣ centena, ▮ decena, ● unidad."""
    parts = [" ".join([sym] * q) for sym, q in (("◼", m), ("▣", c), ("▮", d), ("●", u)) if q]
    return " | ".join(parts) or "(nada)"


OA1 = "MA04 OA 01"
OA2 = "MA04 OA 02"

# ------------------------------------------------------------------ OA 01
lesson(
    OA1, 1,
    use="Aprenderé a contar de 10 en 10, de 100 en 100 y de 1.000 en 1.000 hasta 10.000. Sirve para contar cantidades grandes sin perder el lugar.",
    prior=["Sé contar de 10 en 10 y de 100 en 100 hasta 1.000.", "Sé que 10 decenas forman 1 centena y 10 centenas forman 1 unidad de mil."],
    explain=[
        "Contar de 10 en 10 es sumar 10 en cada salto. Cambia la cifra de las decenas y las unidades quedan iguales: 2.345, 2.355, 2.365. Contar de 100 en 100 cambia la cifra de las centenas. Contar de 1.000 en 1.000 cambia la cifra de las unidades de mil.",
        "Cuando una cifra llega a 9 y sumas uno más, la cifra siguiente sube. En 2.390 + 10 = 2.400 las decenas pasan de 9 a 0 y las centenas suben de 3 a 4. Lo mismo ocurre en 9.900 + 100 = 10.000, que es el número más grande de esta unidad.",
        "Hacia atrás se resta en cada salto. De 5.200 restando 100 llegas a 5.100, 5.000 y 4.900. Para revisar tu secuencia, mira la cifra que debe cambiar y comprueba que las demás cifras se mantengan.",
    ],
    vocab=[("salto", "lo que sumo o resto en cada paso al contar"), ("secuencia", "lista de números que sigue una regla"), ("unidad de mil", "grupo de 1.000 unidades, el cuarto lugar desde la derecha"), ("centena", "grupo de 100 unidades"), ("decena", "grupo de 10 unidades")],
    worked=[
        W("Contar de 10 en 10 pasando una centena", "Cuenta de 10 en 10 desde 3.380 y escribe cuatro números más.", ["Sumo 10: 3.380 + 10 = 3.390.", "3.390 + 10 = 3.400: las decenas llegaron a 10 y forman una centena más.", "Sigo: 3.410 y 3.420.", "Compruebo: las unidades siempre fueron 0."], "3.380, 3.390, 3.400, 3.410, 3.420"),
        W("Contar hacia atrás de 1.000 en 1.000", "Cuenta hacia atrás de 1.000 en 1.000 desde 8.450 y escribe tres números más.", ["Hacia atrás se resta 1.000.", "8.450 − 1.000 = 7.450.", "7.450 − 1.000 = 6.450 y 6.450 − 1.000 = 5.450.", "Solo cambió la cifra de las unidades de mil."], "8.450, 7.450, 6.450, 5.450"),
    ],
    mistakes=[
        M("Escribir 2.390, 2.400, 2.500 al contar de 10 en 10.", "Se cambia el salto a 100 sin darse cuenta.", "Después de 2.400 viene 2.410. Revisa que entre vecinos la diferencia sea siempre 10."),
        M("Escribir 6.900, 6.1000 al contar de 100 en 100.", "Se sigue sumando a la cifra de las centenas sin reagrupar.", "10 centenas forman 1 unidad de mil: después de 6.900 viene 7.000."),
    ],
    rec=[
        fill(2340, 10, 5, (2, 4), "Cada número es 10 más que el anterior: 2.340, 2.350, 2.360, 2.370, 2.380.", "Completa la secuencia de 10 en 10"),
        fill(5200, 100, 5, (1, 3), "Cada número es 100 más: 5.200, 5.300, 5.400, 5.500, 5.600.", "Escribe los números que faltan al contar de 100 en 100"),
        fill(3000, 1000, 5, (2, 4), "Cada número es 1.000 más: 3.000, 4.000, 5.000, 6.000, 7.000.", "Completa la secuencia de 1.000 en 1.000"),
    ],
    und=[
        ex("Julia contó 6.450, 6.550, 6.650, 6.750. ¿De cuánto en cuánto contó?", "De 100 en 100", "6.550 − 6.450 = 100 y 6.650 − 6.550 = 100: la diferencia siempre es 100."),
        ex("Al contar de 10 en 10 desde 2.375, ¿qué cifra no cambia en los primeros saltos: la de las unidades o la de las decenas?", "La de las unidades", "Sumar 10 solo agrega una decena; las unidades se quedan en 5."),
        ex("¿Qué número viene después de 9.990 si cuentas de 10 en 10?", "10.000", "9.990 + 10 = 10.000: las decenas llegan a 10 y se forma una nueva unidad de mil."),
    ],
    app=[
        arith("Un contador marca 3.470 y sube de 100 en 100. Después de 4 saltos, ¿qué número marca?", "3470+100+100+100+100", "Se suma 100 cuatro veces."),
        fill(9700, -100, 5, (1, 3), "Hacia atrás se resta 100: 9.700, 9.600, 9.500, 9.400, 9.300.", "Completa la cuenta hacia atrás de 100 en 100"),
        arith("Una bodega cuenta cajas de 1.000 en 1.000. Partió en 2.000 y dio 6 saltos. ¿En qué número quedó?", "2000+6*1000", "Cada salto suma 1.000 y son 6 saltos."),
    ],
    rea=[
        ex("Pedro cuenta de 100 en 100 desde 1.950 y escribe 2.050, 2.150, 2.350. ¿Cuál es el error y cómo se corrige?", "Después de 2.150 va 2.250, no 2.350", "2.150 + 100 = 2.250. Pedro saltó 200 en ese paso."),
        ex("Luisa dice: «Contando de 1.000 en 1.000 desde 4.200, llegaré a 9.000». ¿Tiene razón?", "No", "Todos los números que dice terminan en 200: 4.200, 5.200, 6.200. Nunca aparece 9.000."),
    ],
    cha=[
        ex("Contando de 10 en 10 desde 9.940, ¿cuántos saltos hay que dar para llegar a 10.000?", "6 saltos", "9.950, 9.960, 9.970, 9.980, 9.990 y 10.000 son 6 números nuevos."),
        ex("Ema cuenta de 100 en 100 desde 3.250 y Leo desde 3.080. ¿Dirán alguna vez el mismo número?", "No", "Los números de Ema terminan en 50 y los de Leo en 80, así que nunca coinciden."),
    ],
    ctx=[ex("El contador de un camión marca 7.490 y sube de 10 en 10. ¿Qué tres números marcará después?", "7.500, 7.510, 7.520", "7.490 + 10 = 7.500, luego 7.510 y 7.520.")],
    sc=[
        ex("Completa: 6.300, 6.400, __, 6.600.", "6.500", "6.400 + 100 = 6.500."),
        ex("Cuenta de 1.000 en 1.000 desde 2.500. ¿Qué número sigue?", "3.500", "2.500 + 1.000 = 3.500."),
        ex("¿Qué número viene después de 9.900 si cuentas de 10 en 10?", "9.910", "9.900 + 10 = 9.910; solo cambia la cifra de las decenas."),
    ],
    op=task(
        "Elige una de estas tres cuentas, todas con partida en 4.760: de 10 en 10, de 100 en 100 o de 1.000 en 1.000. Escribe seis números de la secuencia y explica qué cifra cambia en cada salto.",
        "De 100 en 100 desde 4.760: 4.760, 4.860, 4.960, 5.060, 5.160, 5.260. Cambia la cifra de las centenas; al pasar de 4.960 a 5.060 también subió la unidad de mil.",
        ["escribe seis números", "mantiene el mismo salto", "explica qué cifra cambia"],
        ["secuencia escrita en el cuaderno", "frase de explicación propia"],
        ["cambiar el salto a mitad de la secuencia", "no reagrupar al pasar de 9 a 0"],
        "Reconoce que la secuencia sigue la regla y pide revisar la diferencia entre vecinos; si hay un error, que el estudiante encuentre dónde cambió el salto.",
    ),
    reinforce="Dibuja 10 rayas y a cada una ponle 100. Cuenta de 100 en 100 desde 300 hasta 1.000 y escribe cada número.",
    extend="Si cuentas de 1.000 en 1.000 desde 1.250, ¿cuál es el último número que dices sin pasar de 10.000? Explica cómo lo sabes.",
)

lesson(
    OA1, 2,
    use="Aprenderé a leer y escribir números de cuatro cifras, también los que tienen ceros. Sirve para leer precios y cantidades sin confundir 3.094 con 3.940.",
    prior=["Sé leer y escribir números hasta 1.000.", "Conozco las unidades, decenas y centenas."],
    explain=[
        "Un número de cuatro cifras tiene unidades de mil, centenas, decenas y unidades. Para leerlo, di primero las unidades de mil y la palabra «mil». Después lee el resto como un número de tres cifras. Por ejemplo, 3.940 se lee «tres mil novecientos cuarenta».",
        "El cero ocupa un lugar cuando no hay nada en esa posición. En 3.094 no hay centenas: la cifra de las centenas es 0. Por eso se lee «tres mil noventa y cuatro» y no se nombran las centenas. Si quitas el cero y escribes 394, cambias el número por completo.",
        "Al escribir con cifras, pon una cifra en cada lugar. «Cuatro mil seis» tiene 4 unidades de mil, 0 centenas, 0 decenas y 6 unidades: 4.006. Los ceros guardan el lugar de lo que falta. Se escribe un punto después de las unidades de mil.",
    ],
    vocab=[("unidad de mil", "grupo de 1.000; la primera cifra de un número de cuatro cifras"), ("cero", "cifra que guarda un lugar cuando no hay nada en él"), ("tabla posicional", "tabla con una columna para cada lugar: UM, C, D y U"), ("cifra", "cada uno de los símbolos de un número, del 0 al 9"), ("valor posicional", "lo que vale una cifra según el lugar donde está")],
    worked=[
        W("Leer un número con cero", "Lee 5.307.", ["Miro la tabla: UM = 5, C = 3, D = 0, U = 7.", "Digo las unidades de mil y «mil»: cinco mil.", "Leo el resto como número de tres cifras: 307, trescientos siete. No hay decenas, así que no las nombro."], "cinco mil trescientos siete"),
        W("Escribir con cifras", "Escribe con cifras: cuatro mil veinte.", ["«Cuatro mil»: UM = 4.", "«Veinte»: 2 decenas, 0 unidades.", "No se nombran las centenas: C = 0. Escribo 4, 0, 2, 0."], "4.020"),
    ],
    mistakes=[
        M("Escribir «tres mil noventa y cuatro» como 3.94.", "Se olvida que el cero guarda el lugar de las centenas.", "Pon una cifra en cada lugar: 3 UM, 0 C, 9 D, 4 U = 3.094."),
        M("Leer 8.007 como «ocho mil setenta».", "Se corre el 7 al lugar de las decenas.", "El 7 está en las unidades: se lee «ocho mil siete»."),
    ],
    rec=[
        ex("Escribe con cifras: tres mil noventa y cuatro.", "3.094", "3 unidades de mil, 0 centenas, 9 decenas y 4 unidades."),
        ex("Escribe con palabras: 4.020.", words(4020), "4 unidades de mil, 0 centenas, 2 decenas y 0 unidades."),
        ex("¿Qué cifra está en el lugar de las centenas en 5.307?", "3", "En 5.307: 5 UM, 3 C, 0 D, 7 U."),
    ],
    und=[
        ex("En 6.050, ¿qué cifra está en el lugar de las centenas y qué valor tiene?", "El 0; vale 0 centenas", "6.050 tiene 6 UM, 0 C, 5 D y 0 U: en las centenas no hay nada."),
        ex("¿Cuál de estos números se lee «ocho mil siete»: 8.700, 8.070 u 8.007?", "8.007", "8 UM, 0 C, 0 D y 7 U."),
        ex("¿Cuántos ceros lleva «cuatro mil seis» escrito con cifras?", "2", "Se escribe 4.006: hay un cero en las centenas y otro en las decenas."),
    ],
    app=[
        ex("Una tabla posicional dice UM = 2, C = 0, D = 5, U = 0. ¿Qué número es?", "2.050", "Se escribe cada cifra en su lugar: 2, 0, 5, 0."),
        ex("Escribe con cifras: siete mil trescientos cinco.", "7.305", "7 UM, 3 C, 0 D y 5 U."),
        ex("Escribe con palabras: 9.040.", words(9040), "9 UM, 0 C, 4 D y 0 U."),
    ],
    rea=[
        ex("Rosa escribió «dos mil cincuenta» como 2.500. ¿Está bien? Si no, escribe el número correcto.", "No, es 2.050", "En 2.500 el 5 está en las centenas (quinientos). Cincuenta son 5 decenas: 2.050."),
        ex("Ana lee 3.094 como «tres mil noventa y cuatro» y Beto lo lee «tres mil cuarenta y nueve». ¿Quién lo lee bien?", "Ana", "3.094 tiene 9 decenas y 4 unidades: noventa y cuatro. «Cuarenta y nueve» sería 3.049."),
    ],
    cha=[
        ex("Con las cifras 7, 0, 0 y 4, usando cada una una vez, escribe el mayor número que no termina en 0.", "7.004", "Para que sea el mayor va el 7 al inicio. Para no terminar en 0, el 4 va al final: 7, 0, 0, 4."),
        ex("Un número tiene 5 unidades de mil, 0 centenas, 0 decenas y 9 unidades. Escríbelo con palabras.", words(5009), "Es 5.009: se lee «cinco mil nueve», sin nombrar centenas ni decenas."),
    ],
    ctx=[ex("En una boleta aparece «$ 2.050». ¿Cómo se lee ese precio?", "dos mil cincuenta pesos", "2 UM, 0 C, 5 D y 0 U: dos mil cincuenta.")],
    sc=[
        ex("Escribe con cifras: seis mil ocho.", "6.008", "6 UM, 0 C, 0 D y 8 U."),
        ex("Escribe con palabras: 1.205.", words(1205), "1 UM, 2 C, 0 D y 5 U: mil doscientos cinco."),
        ex("¿Qué número se lee «nueve mil novecientos»?", "9.900", "9 UM, 9 C, 0 D y 0 U."),
    ],
    op=task(
        "Escribe con palabras estos tres precios: $ 3.094, $ 3.940 y $ 3.904. Léelos en voz alta. Luego explica en una frase qué cambia entre ellos y por qué el cero es importante.",
        "tres mil noventa y cuatro; tres mil novecientos cuarenta; tres mil novecientos cuatro. En los tres están las cifras 3, 9, 4 y 0, pero en lugares distintos, y el cero guarda el lugar que está vacío.",
        ["escribe bien los tres números con palabras", "nombra el lugar vacío del cero", "explica que cambiar de lugar cambia el valor"],
        ["tres números escritos con palabras", "frase de explicación propia"],
        ["olvidar el cero y escribir números de tres cifras", "leer las cifras sueltas: tres, nueve, cuatro"],
        "Señala los números bien leídos y pide que ubique cada cifra en una tabla posicional para corregir el que falle.",
    ),
    reinforce="Escribe en una tabla posicional los números 4.050, 4.500 y 4.005 y léelos en voz alta.",
    extend="Escribe cuatro números de cuatro cifras que usen las cifras 2, 0 y 7 y tengan al menos un cero. Léelos con palabras.",
)

lesson(
    OA1, 3,
    use="Aprenderé a representar números de cuatro cifras con bloques y dibujos, y a canjear 10 de un lugar por 1 del siguiente. Sirve para entender cuánto vale cada cifra.",
    prior=["Sé que 10 unidades forman 1 decena y 10 decenas forman 1 centena.", "Sé leer números de cuatro cifras."],
    explain=[
        "Usaremos cuatro símbolos: ◼ vale 1.000, ▣ vale 100, ▮ vale 10 y ● vale 1. El número 2.305 se dibuja con 2 ◼, 3 ▣ y 5 ●. No se dibuja ninguna decena, porque tiene 0 decenas.",
        "Un canje cambia 10 de un lugar por 1 del lugar siguiente, sin cambiar el valor total. Diez ▣ se canjean por 1 ◼. Diez ▮ se canjean por 1 ▣. Diez ● se canjean por 1 ▮. También se puede canjear al revés: 1 ◼ se cambia por 10 ▣.",
        "El canje sirve para escribir bien un número. Si tienes 13 ▣ y 2 ●, cambias 10 ▣ por 1 ◼ y te quedan 1 ◼, 3 ▣ y 2 ●, que es 1.302. Siempre revisa que cada lugar tenga menos de 10 piezas al terminar.",
    ],
    vocab=[("canje", "cambiar 10 piezas de un lugar por 1 pieza del lugar siguiente, o al revés"), ("unidad de mil", "pieza que vale 1.000 y se dibuja ◼"), ("representar", "mostrar un número con bloques, dibujo o símbolos"), ("concreto", "con objetos que se pueden tocar"), ("pictórico", "con dibujos")],
    worked=[
        W("Leer un dibujo", "¿Qué número muestra ◼ ◼ ◼ | ▣ ▣ | ● ● ● ● ●?", ["Cuento ◼: 3, valen 3.000.", "Cuento ▣: 2, valen 200. No hay ▮, valen 0.", "Cuento ●: 5, valen 5. Sumo: 3.000 + 200 + 0 + 5."], "3.205"),
        W("Canjear para ordenar", "Hay 14 ▣ y 3 ▮. ¿Qué número es? Canjea para escribirlo.", ["Cambio 10 ▣ por 1 ◼: quedan 1 ◼ y 4 ▣.", "Las 3 ▮ no cambian.", "Ahora cada lugar tiene menos de 10: 1 ◼, 4 ▣, 3 ▮, 0 ●."], "1.430"),
    ],
    mistakes=[
        M("Escribir 3.25 para ◼ ◼ ◼ | ▣ ▣ | ● ● ● ● ●.", "Se olvida que no hay decenas y se pierde el cero.", "Escribe una cifra por lugar: 3 UM, 2 C, 0 D, 5 U = 3.205."),
        M("Decir que 12 ▣ son 12.000.", "Se confunde la centena con la unidad de mil.", "12 ▣ valen 1.200: se canjean 10 ▣ por 1 ◼ y quedan 1 ◼ y 2 ▣."),
    ],
    rec=[
        ex(f"¿Qué número muestra este dibujo? {blk(2, 3, 0, 5)}", "2.305", "2 unidades de mil, 3 centenas, 0 decenas y 5 unidades."),
        ex("¿Cuántas ▣ se canjean por 1 ◼?", "10", "10 centenas forman 1 unidad de mil."),
        ex("Dibuja con símbolos el número 1.420 y escribe cuántos ◼, ▣, ▮ y ● usaste.", "1 ◼, 4 ▣, 2 ▮ y 0 ●", "1.420 tiene 1 UM, 4 C, 2 D y 0 U."),
    ],
    und=[
        ex("Tengo 10 ▮. ¿Por cuál pieza las puedo canjear?", "Por 1 ▣", "10 decenas son 100, o sea 1 centena."),
        ex("¿Cuántas ▮ hay en 1 ◼?", "100", "1 ◼ son 10 ▣ y cada ▣ son 10 ▮: 10 × 10 = 100."),
        ex(f"En {blk(1, 0, 4, 6)} no hay ▣. ¿Qué número es?", "1.046", "1 UM, 0 C, 4 D y 6 U."),
    ],
    app=[
        ex("Hay 13 ▣ y 2 ●. Canjea y escribe el número.", "1.302", "10 ▣ se canjean por 1 ◼: quedan 1 ◼, 3 ▣ y 2 ●."),
        ex("Hay 4 ◼, 2 ▣ y 15 ▮. Canjea las ▮ y escribe el número.", "4.350", "10 ▮ forman 1 ▣; sobran 5 ▮. Quedan 4 ◼, 3 ▣, 5 ▮."),
        ex("Dibuja 5.030 con símbolos y escribe cuántas piezas de cada tipo usas.", "5 ◼, 0 ▣, 3 ▮ y 0 ●", "5.030 tiene 5 UM, 0 C, 3 D y 0 U."),
    ],
    rea=[
        ex("Eva canjeó 16 ▣ y 4 ● y escribió 1.604. ¿Está bien?", "Sí", "10 ▣ forman 1 ◼ y quedan 6 ▣: 1 ◼, 6 ▣ y 4 ●, o sea 1.604."),
        ex("Mauro canjeó 11 ▮ por 1 ▣ y dice que no sobra nada. ¿Está bien?", "No, sobra 1 ▮", "10 ▮ forman 1 ▣ y queda 1 ▮."),
    ],
    cha=[
        ex("Tengo 2 ◼, 9 ▣, 9 ▮ y 10 ●. Canjea hasta que cada lugar tenga menos de 10 y escribe el número.", "3.000", "10 ● dan 1 ▮ (10 ▮); 10 ▮ dan 1 ▣ (10 ▣); 10 ▣ dan 1 ◼: queda 3 ◼."),
        ex("Quiero mostrar 1.000 solo con ▮. ¿Cuántas necesito?", "100", "Cada ▮ vale 10; 1.000 ÷ 10 = 100."),
    ],
    ctx=[ex("Una tienda tiene 6 cajas de 1.000 clips, 12 bolsas de 100 clips y 4 clips sueltos. Canjea y escribe cuántos clips hay.", "7.204", "12 bolsas son 1 caja y 2 bolsas más: 7 cajas, 2 bolsas y 4 sueltos.")],
    sc=[
        ex("¿Por cuántas ▮ se canjea 1 ▣?", "10", "Una centena tiene 10 decenas."),
        ex(f"¿Qué número muestra {blk(4, 0, 2, 0)}?", "4.020", "4 UM, 0 C, 2 D y 0 U."),
        ex("Hay 12 ▮ y 3 ●. ¿Qué número es?", "123", "12 ▮ son 1 ▣ y 2 ▮: 1 C, 2 D y 3 U."),
    ],
    op=task(
        "Dibuja con ◼, ▣, ▮ y ● el número 3.408. Luego cambia 1 ◼ por ▣: dibuja cómo queda y escribe cuántas ▣ tiene ahora.",
        "3.408 = ◼ ◼ ◼ | ▣ ▣ ▣ ▣ | ● ● ● ● ● ● ● ●. Si cambio 1 ◼ por 10 ▣, quedan 2 ◼ y 14 ▣: sigue siendo 3.408 porque un canje no cambia el valor.",
        ["dibuja las piezas correctas", "no dibuja decenas porque hay 0", "hace el canje de 1 ◼ por 10 ▣", "explica que el valor no cambia"],
        ["dibujo en el cuaderno", "frase de explicación propia"],
        ["dibujar una decena donde hay 0", "olvidar que 1 ◼ son 10 ▣"],
        "Reconoce el dibujo correcto y pide que cuente el valor total antes y después del canje para comprobar que es igual.",
    ),
    reinforce="Con palitos y 10 cuadraditos de papel, practica cambiar 10 palitos por 1 cuadradito hasta ordenar 27 palitos.",
    extend="¿Cuántas ▣ hay en 4.000? ¿Cuántas ▮? Explica cómo lo calculaste con canjes.",
)

lesson(
    OA1, 4,
    use="Aprenderé a comparar y ordenar números hasta 10.000 con la tabla posicional y la recta numérica. Sirve para saber cuál precio o cantidad es mayor.",
    prior=["Sé comparar números de tres cifras.", "Conozco los signos > (mayor que) y < (menor que)."],
    explain=[
        "Para comparar dos números, primero mira cuántas cifras tienen. El que tiene más cifras es mayor: 1.000 es mayor que 999. Si tienen las mismas cifras, compara de izquierda a derecha, desde las unidades de mil.",
        "Si las unidades de mil son iguales, mira las centenas. Si también son iguales, mira las decenas, y así. En 4.321 y 4.312 las unidades de mil y las centenas son iguales, pero las decenas son 2 y 1. Por eso 4.321 > 4.312.",
        "En la recta numérica los números crecen hacia la derecha. El que queda más a la derecha es mayor. Para ordenar de menor a mayor, compara de a dos y ubica cada número en su lugar. El 10.000 es mayor que cualquier número de cuatro cifras.",
    ],
    vocab=[("comparar", "decidir cuál número es mayor, menor o si son iguales"), ("mayor que (>)", "signo que se abre hacia el número más grande"), ("menor que (<)", "signo que apunta al número más pequeño"), ("ordenar", "poner números en fila de menor a mayor o de mayor a menor"), ("recta numérica", "línea donde los números crecen hacia la derecha")],
    worked=[
        W("Comparar con la tabla", "Compara 5.482 y 5.428.", ["Las dos tienen 4 cifras. Unidades de mil: 5 y 5, iguales.", "Centenas: 4 y 4, iguales.", "Decenas: 8 y 2. Como 8 > 2, el primero es mayor."], "5.482 > 5.428"),
        W("Ordenar de menor a mayor", "Ordena de menor a mayor: 3.090, 3.009, 3.900, 3.099.", ["Todos tienen 3 unidades de mil. Miro las centenas: 0, 0, 9, 0. El mayor es 3.900.", "Entre 3.090, 3.009 y 3.099 comparo decenas: 9, 0 y 9. El menor es 3.009.", "Entre 3.090 y 3.099 miro las unidades: 0 y 9."], "3.009, 3.090, 3.099, 3.900"),
    ],
    mistakes=[
        M("Decir que 987 es mayor que 1.002 porque 9 es mayor que 1.", "Se compara la primera cifra sin mirar cuántas cifras tiene el número.", "Primero cuenta las cifras: 1.002 tiene cuatro cifras y 987 tres, así que 1.002 es mayor."),
        M("Decir que 4.099 es mayor que 4.109 porque 99 es mayor que 9.", "Se comparan las dos últimas cifras como si fueran un solo número, sin mirar el lugar.", "Compara lugar por lugar: las centenas son 0 y 1, así que 4.109 es mayor."),
    ],
    rec=[
        ex("¿Cuál número es mayor: 3.456 o 3.465?", "3.465", "UM y centenas son iguales; en las decenas 6 es mayor que 5."),
        ex("Escribe > o < : 7.120 __ 7.102.", ">", "En las decenas hay 2 y 0; 2 es mayor que 0, así que 7.120 es mayor."),
        ex("¿Cuál número es menor: 999 o 1.000?", "999", "999 tiene tres cifras y 1.000 tiene cuatro."),
    ],
    und=[
        ex("Para comparar 6.205 y 6.250, ¿qué lugar decide cuál es mayor?", "Las decenas", "UM y centenas son iguales; las decenas son 0 y 5."),
        ex("En una recta numérica, ¿el número mayor queda a la izquierda o a la derecha?", "A la derecha", "Los números crecen hacia la derecha en la recta."),
        ex("¿Es 10.000 mayor que 9.999?", "Sí", "10.000 tiene cinco cifras y 9.999 tiene cuatro."),
    ],
    app=[
        ex("Ordena de menor a mayor: 4.321, 4.231, 4.312, 4.132.", "4.132, 4.231, 4.312, 4.321", "Todos tienen 4 UM; se ordenan por las centenas (1, 2, 3, 3) y luego por las decenas."),
        ex("Ordena de mayor a menor: 8.090, 8.900, 8.009, 8.099.", "8.900, 8.099, 8.090, 8.009", "Las centenas dejan el 8.900 primero; luego 8.099 > 8.090 > 8.009 por decenas y unidades."),
        ex("Una recta va de 2.000 a 3.000 y está dividida en 10 partes iguales de 100. ¿Qué número queda justo en el medio?", "2.500", "El medio está después de 5 partes de 100: 2.000 + 500 = 2.500."),
    ],
    rea=[
        ex("Tomás dice: «6.099 es mayor que 6.100 porque 99 es mayor que 1». ¿Tiene razón?", "No", "Las centenas son 0 y 1; 6.100 es mayor. El 99 no se compara como un solo número."),
        ex("Una bicicleta cuesta $ 9.990 y un casco $ 10.000. ¿Cuál cuesta más?", "El casco", "10.000 tiene cinco cifras y 9.990 cuatro, así que $ 10.000 es mayor."),
    ],
    cha=[
        ex("Escribe en el espacio la cifra que hace verdadero 5.4_7 < 5.417.", "0", "Las UM y las centenas son iguales. Para que sea menor, las decenas deben ser menores que 1, y solo sirve 0."),
        ex("Con las cifras 3, 8, 0 y 5, usa cada una una vez: escribe el mayor y el menor número de cuatro cifras. El menor no puede empezar con 0.", "8.530 y 3.058", "El mayor ordena las cifras de mayor a menor. El menor empieza con la cifra más pequeña que no sea 0: 3, luego 0, 5 y 8."),
    ],
    ctx=[ex("Cuatro pueblos tienen estos habitantes: Alto 3.210, Bajo 3.021, Centro 3.120, Sur 3.012. ¿Cuál tiene más habitantes y cuál menos?", "Más: Alto; menos: Sur", "Con 3 UM igual, las centenas son 2, 0, 1 y 0. Alto es mayor. Entre Bajo y Sur, las decenas 2 y 1 dejan a Sur menor.")],
    sc=[
        ex("Escribe > o < : 2.987 __ 3.001.", "<", "2.987 tiene 2 UM y 3.001 tiene 3 UM."),
        ex("Ordena de menor a mayor: 5.050, 5.005, 5.500.", "5.005, 5.050, 5.500", "Las centenas dejan 5.500 al final; 5.005 < 5.050 por las decenas."),
        ex("¿Cuál es el mayor: 7.654 o 7.645?", "7.654", "En las decenas 5 es mayor que 4."),
    ],
    op=task(
        "Ordena de mayor a menor las alturas de cuatro cerros: Pico 2.310 m, Cumbre 2.130 m, Loma 2.301 m, Alto 2.103 m. Dibuja una recta de 2.100 a 2.400 y ubica los cuatro. Explica cómo decidiste cuál es el mayor.",
        "Orden: Pico 2.310 m, Loma 2.301 m, Cumbre 2.130 m, Alto 2.103 m. Todos tienen 2 UM. Las centenas son 3, 3, 1 y 1. Entre Pico y Loma, las decenas 1 y 0 dejan a Pico primero.",
        ["ordena bien los cuatro", "ubica los números en la recta de izquierda a derecha", "explica el lugar que decide"],
        ["lista ordenada", "recta dibujada", "frase de explicación propia"],
        ["comparar solo la primera cifra distinta sin mirar el lugar", "poner el mayor a la izquierda en la recta"],
        "Reconoce el orden correcto y pide que explique con la tabla posicional por qué 2.310 va antes que 2.301.",
    ),
    reinforce="Escribe en tarjetas 1.234, 1.324, 1.243 y 1.432 y ordénalas de menor a mayor comparando lugar por lugar.",
    extend="¿Cuántos números hay entre 5.098 y 5.103? Escríbelos.",
)

lesson(
    OA1, 5,
    use="Aprenderé a descomponer un número según el valor de sus cifras y a armarlo de nuevo. Sirve para entender qué vale cada cifra y calcular con más facilidad.",
    prior=["Sé el valor posicional de las cifras hasta las unidades de mil.", "Sé sumar varios sumandos."],
    explain=[
        "Descomponer un número en forma aditiva es escribirlo como una suma de lo que vale cada cifra. El número 5.382 vale 5.000 + 300 + 80 + 2. El 5 vale 5.000 porque está en las unidades de mil. El 3 vale 300 porque está en las centenas.",
        "Componer es hacer lo contrario: sumas los valores y obtienes el número. Si tienes 2.000 + 40 + 7, el resultado es 2.047. Fíjate que no hay centenas, así que el cero guarda su lugar. No se escribe «2.47».",
        "El número 10.000 se lee «diez mil» y tiene cinco cifras. Su 1 está en el quinto lugar desde la derecha, la decena de mil. Una decena de mil vale 10.000 y son 10 unidades de mil: por eso 9.999 + 1 = 10.000. La descomposición por valor posicional usa un sumando por cada cifra distinta de cero, así que 10.000 es solo 10.000.",
    ],
    vocab=[("descomponer", "separar un número en la suma de lo que vale cada cifra"), ("componer", "juntar los valores para formar el número"), ("forma aditiva", "escritura como suma, por ejemplo 400 + 20 + 5"), ("decena de mil", "grupo de 10.000; el quinto lugar desde la derecha"), ("valor de una cifra", "lo que vale esa cifra por el lugar donde está")],
    worked=[
        W("Descomponer", "Descompón 6.409 en forma aditiva.", ["Miro cada cifra: 6 UM, 4 C, 0 D, 9 U.", "6 UM valen 6.000; 4 C valen 400; 0 D valen 0; 9 U valen 9.", "Escribo la suma sin la parte que vale 0."], "6.000 + 400 + 9"),
        W("Componer", "Escribe el número: 7.000 + 30 + 2.", ["7.000 son 7 UM.", "No hay centenas: 0 C. 30 son 3 D. 2 son 2 U.", "Pongo una cifra por lugar: 7, 0, 3, 2."], "7.032"),
    ],
    mistakes=[
        M("Escribir 5.382 = 5 + 3 + 8 + 2.", "Se suman las cifras en vez de sus valores.", "Cada cifra vale según su lugar: 5.000 + 300 + 80 + 2."),
        M("Componer 2.000 + 40 + 7 como 2.47.", "No se pone el cero que guarda las centenas.", "Pon una cifra por lugar: 2 UM, 0 C, 4 D, 7 U = 2.047."),
    ],
    rec=[
        ex("Descompón 3.456 en forma aditiva.", "3.000 + 400 + 50 + 6", "3 UM = 3.000, 4 C = 400, 5 D = 50 y 6 U = 6."),
        ex("Compón el número: 4.000 + 700 + 20 + 1.", "4.721", "4 UM, 7 C, 2 D y 1 U."),
        ex("¿Cuánto vale el 8 en 8.215?", "8.000", "El 8 está en las unidades de mil."),
    ],
    und=[
        ex("¿Cuánto vale el 7 en 3.074?", "70", "El 7 está en el lugar de las decenas: 7 decenas son 70."),
        ex("En 5.309, ¿por qué no aparece ningún sumando de decenas al descomponer?", "Porque hay 0 decenas", "5.309 = 5.000 + 300 + 9; la cifra de las decenas es 0."),
        ex("¿Cuántas centenas hay en 2.700?", "27", "2.700 = 2.000 + 700. 2.000 son 20 centenas y 700 son 7 centenas."),
    ],
    app=[
        ex("Descompón 9.060 en forma aditiva.", "9.000 + 60", "9 UM, 0 C, 6 D, 0 U."),
        ex("Compón el número: 1.000 + 500 + 5.", "1.505", "1 UM, 5 C, 0 D y 5 U."),
        ex("Escribe con palabras el número 10.000 y di en qué lugar está su cifra 1.", words(10000) + "; en la decena de mil", "10.000 se lee «diez mil»; su 1 está en el quinto lugar, la decena de mil, y vale 10.000."),
    ],
    rea=[
        ex("Gabi descompuso 4.205 como 4.000 + 200 + 50. ¿Qué error cometió?", "Escribió 50 en lugar de 5", "El 5 está en las unidades, vale 5. Debe ser 4.000 + 200 + 5."),
        ex("Pía dice que 7.000 + 700 + 70 + 7 es 7.777. ¿Tiene razón?", "Sí", "7 UM, 7 C, 7 D y 7 U forman 7.777."),
    ],
    cha=[
        ex("Escribe 3.500 como suma de tres sumandos: 2.000, 1.000 y otro más. ¿Cuál es el otro?", "500", "2.000 + 1.000 = 3.000 y faltan 500 para llegar a 3.500."),
        ex("Un número tiene 2 UM, el doble de centenas que de unidades de mil, 0 decenas y 3 unidades. Escríbelo.", "2.403", "Centenas = 2 × 2 = 4: 2 UM, 4 C, 0 D y 3 U."),
    ],
    ctx=[ex("En una alcancía hay 4 billetes de $ 1.000, 3 monedas de $ 100 y 5 monedas de $ 10. ¿Cuánto dinero hay en total?", "$ 4.350", "4.000 + 300 + 50 = 4.350.")],
    sc=[
        ex("Descompón 7.208 en forma aditiva.", "7.000 + 200 + 8", "7 UM, 2 C, 0 D y 8 U."),
        ex("Compón: 8.000 + 90 + 4.", "8.094", "8 UM, 0 C, 9 D y 4 U."),
        ex("¿Cuánto vale el 4 en 4.903?", "4.000", "Está en las unidades de mil."),
    ],
    op=task(
        "Descompón en forma aditiva estos números: 5.382, 5.038 y 5.308. Luego escribe una frase que explique por qué tienen las mismas cifras pero valen distinto.",
        "5.382 = 5.000 + 300 + 80 + 2; 5.038 = 5.000 + 30 + 8; 5.308 = 5.000 + 300 + 8. Valen distinto porque cada cifra vale según el lugar donde está.",
        ["descompone bien los tres números", "no escribe sumandos con 0", "explica el valor según el lugar"],
        ["tres descomposiciones escritas", "frase de explicación propia"],
        ["sumar las cifras sin su valor", "poner 8 en vez de 80 o 800"],
        "Revisa cada sumando con la tabla posicional: pide que diga en qué lugar está la cifra antes de escribir su valor.",
    ),
    reinforce="Escribe un número de cuatro cifras de una boleta o de un cartel de tu casa y descompónlo en forma aditiva.",
    extend="Descompón 4.200 de dos formas distintas usando solo sumandos de 1.000 y de 100.",
)

# ------------------------------------------------------------------ OA 02
lesson(
    OA2, 1,
    use="Aprenderé a sumar y restar de cabeza contando hacia adelante y hacia atrás. Sirve para calcular rápido el vuelto o cuántos faltan sin escribir.",
    prior=["Sé contar de 1 en 1, de 10 en 10 y de 100 en 100.", "Conozco las sumas y restas básicas hasta 20."],
    explain=[
        "Contar hacia adelante sirve para sumar. Para 47 + 5, parto del 47 y cuento cinco números: 48, 49, 50, 51, 52. Es más rápido si primero llegas a la decena: 47 + 3 = 50 y quedan 2 más, entonces 52.",
        "Contar hacia atrás sirve para restar. Para 63 − 4, parto del 63 y retrocedo cuatro: 62, 61, 60, 59. También puedes saltar de 10 en 10: 63 − 20 = 43. Siempre parte del número más grande y retrocede.",
        "Otra forma es contar desde el menor hasta el mayor para ver cuánto falta. Para 82 − 78, cuenta desde 78 hasta 82: 79, 80, 81, 82. Son 4 pasos, entonces la diferencia es 4. Elige la forma que te cueste menos pasos.",
    ],
    vocab=[("conteo hacia adelante", "decir los números siguientes para sumar"), ("conteo hacia atrás", "decir los números anteriores para restar"), ("diferencia", "resultado de una resta; cuánto falta de un número a otro"), ("salto", "lo que avanzo o retrocedo en cada paso"), ("cálculo mental", "calcular de cabeza, sin escribir la cuenta")],
    worked=[
        W("Sumar contando hacia adelante", "Calcula 58 + 6 contando hacia adelante.", ["Parto de 58. Primero llego a 60: 58 + 2 = 60.", "Me quedan 4 por contar: 6 − 2 = 4.", "60 + 4 = 64."], "64"),
        W("Restar contando hacia atrás", "Calcula 300 − 40 contando hacia atrás de 10 en 10.", ["Parto de 300 y retrocedo de 10 en 10.", "290, 280, 270, 260: cuatro saltos de 10.", "Cuatro saltos de 10 restan 40."], "260"),
    ],
    mistakes=[
        M("Calcular 63 − 4 como 67.", "Se cuenta hacia adelante en vez de hacia atrás.", "Restar es retroceder: 62, 61, 60, 59. La respuesta es menor que 63."),
        M("Al contar 47 + 5 decir 47, 48, 49, 50, 51 y responder 51.", "Se cuenta el 47 como si fuera uno de los cinco pasos.", "El número de partida no se cuenta: 48, 49, 50, 51, 52."),
    ],
    rec=[
        ex("Calcula 47 + 5 contando hacia adelante.", "52", "48, 49, 50, 51, 52: cinco pasos desde 47."),
        ex("Calcula 63 − 4 contando hacia atrás.", "59", "62, 61, 60, 59: cuatro pasos hacia atrás."),
        ex("Calcula 200 + 30 contando de 10 en 10.", "230", "210, 220, 230: tres saltos de 10."),
    ],
    und=[
        ex("Para calcular 82 − 78 contando desde 78, ¿cuántos pasos hay que dar para llegar a 82?", "4", "79, 80, 81, 82: son 4 pasos, y esa es la diferencia."),
        ex("¿Qué es más corto para calcular 90 − 88: retroceder 88 pasos desde 90 o contar desde 88 hasta 90?", "Contar desde 88 hasta 90", "Desde 88 hasta 90 hay solo 2 pasos: 89 y 90."),
        ex("Al calcular 58 + 6, ¿a qué número conviene llegar primero?", "A 60", "58 + 2 = 60 y luego se suman los 4 que faltan."),
    ],
    app=[
        arith("Un contador marca 195 personas y entran 7 más. Cuenta hacia adelante y escribe cuántas hay.", "195+7", "Se llega a 200 con 5 y se suman 2 más."),
        arith("Una caja tiene 340 clips y se sacan 50. Cuenta hacia atrás de 10 en 10 y escribe cuántos quedan.", "340-50", "Se retrocede cinco saltos de 10."),
        ex("Cuenta hacia adelante desde 996 y escribe los cinco números siguientes.", "997, 998, 999, 1.000, 1.001", "Después de 999 viene 1.000 y luego 1.001."),
    ],
    rea=[
        ex("Raúl calculó 71 − 6 contando hacia atrás y dijo «64». ¿Está bien?", "No, es 65", "70, 69, 68, 67, 66, 65: seis pasos hacia atrás desde 71."),
        ex("Para calcular 503 − 498, ¿conviene contar hacia atrás 498 pasos o contar desde 498 hasta 503? Escribe el resultado.", "Contar desde 498; 5", "498 → 503 son 5 pasos: 499, 500, 501, 502, 503."),
    ],
    cha=[
        ex("Pía parte en 1.000 y retrocede de 100 en 100 hasta llegar a 600. ¿Cuántos saltos dio?", "4", "900, 800, 700 y 600 son 4 saltos."),
        ex("Dos niños cuentan de 10 en 10: Ana parte en 230 hacia adelante y Beto parte en 330 hacia atrás. ¿En qué número se encuentran?", "280", "Ana dice 240, 250, 260, 270, 280; Beto dice 320, 310, 300, 290, 280."),
    ],
    ctx=[ex("En la feria, Marta tiene $ 100 y gasta $ 45 en fruta. Cuenta hacia adelante desde 45 hasta 100 para saber cuánto le queda.", "$ 55", "45 + 5 = 50, 50 + 50 = 100: 5 + 50 = 55.")],
    sc=[
        ex("Calcula 38 + 5 contando hacia adelante.", "43", "38 + 2 = 40 y 3 más son 43."),
        ex("Calcula 500 − 30 contando hacia atrás de 10 en 10.", "470", "490, 480, 470."),
        ex("Calcula 61 − 3 contando hacia atrás.", "58", "60, 59, 58."),
    ],
    op=task(
        "Resuelve de cabeza y cuenta en voz alta cómo lo hiciste: 76 + 8, 94 − 7 y 402 − 398. Para cada uno escribe si contaste hacia adelante o hacia atrás y los números que dijiste.",
        "76 + 8: 76 → 80 (4) → 84 (4 más), contando hacia adelante. 94 − 7: 93, 92, 91, 90, 89, 88, 87 = 87 hacia atrás. 402 − 398: de 398 a 402 son 4 pasos = 4.",
        ["resuelve bien las tres", "explica la forma de contar", "elige una forma eficiente"],
        ["tres respuestas con su forma de contar escrita", "explicación en voz alta"],
        ["contar el número de partida", "restar contando hacia adelante"],
        "Comprueba la respuesta con la operación inversa y pide que describa dónde estuvo el paso más difícil.",
    ),
    reinforce="Con una recta numérica dibujada de 0 a 20, practica 9 + 6 y 17 − 5 saltando sobre ella.",
    extend="Calcula 1.002 − 998 contando. ¿Cuántos pasos hay? ¿Por qué es mejor contar hacia adelante?",
)

lesson(
    OA2, 2,
    use="Aprenderé a doblar y a sacar la mitad de un número de cabeza. Sirve para multiplicar por 2 y dividir por 2 rápido.",
    prior=["Sé la tabla del 2.", "Sé sumar números iguales, como 25 + 25."],
    explain=[
        "El doble de un número es ese número más sí mismo, o multiplicarlo por 2. El doble de 35 es 70, porque 35 + 35 = 70. Para doblar un número grande, dobla cada parte: el doble de 35 es el doble de 30 más el doble de 5, es decir 60 + 10 = 70.",
        "La mitad es lo contrario del doble: repartir en 2 partes iguales, o dividir por 2. La mitad de 86 es 43, porque 43 + 43 = 86. También se separa por partes: la mitad de 80 es 40 y la mitad de 6 es 3, entonces 43.",
        "Si el número es impar, la mitad no es exacta con números enteros. En esta unidad usaremos mitades exactas, que son las de números pares. Para comprobar la mitad, dóblala: si el doble vuelve al número original, está bien.",
    ],
    vocab=[("doble", "el número multiplicado por 2, o sumado consigo mismo"), ("mitad", "una de las dos partes iguales de un número; dividir por 2"), ("par", "número que termina en 0, 2, 4, 6 u 8"), ("dividir por 2", "repartir en dos partes iguales"), ("comprobar", "revisar con otra operación que el resultado está bien")],
    worked=[
        W("Doblar por partes", "Calcula el doble de 47.", ["Separo 47 en 40 y 7.", "El doble de 40 es 80 y el doble de 7 es 14.", "Sumo: 80 + 14."], "94"),
        W("Sacar la mitad por partes", "Calcula la mitad de 156.", ["Separo 156 en 100, 50 y 6.", "La mitad de 100 es 50, la de 50 es 25 y la de 6 es 3.", "Sumo: 50 + 25 + 3."], "78"),
    ],
    mistakes=[
        M("Decir que la mitad de 86 es 34.", "Se resta 52 en vez de repartir en dos partes iguales.", "Comprueba doblando: el doble de 34 es 68, no 86. La mitad de 86 es 43."),
        M("Calcular el doble de 35 como 65.", "Se suma 30 en vez de sumar el número consigo mismo.", "Doble de 35 = 35 + 35 = 70."),
    ],
    rec=[
        ex("¿Cuál es el doble de 25?", "50", "25 + 25 = 50."),
        ex("¿Cuál es la mitad de 18?", "9", "9 + 9 = 18."),
        ex("¿Cuál es el doble de 400?", "800", "El doble de 4 centenas son 8 centenas."),
    ],
    und=[
        ex("¿Por qué la mitad de 86 es 43? Escribe la suma que lo comprueba.", "43 + 43 = 86", "Si dos partes iguales de 43 forman 86, 43 es la mitad."),
        ex("Para doblar 68, ¿qué dos dobles se suman?", "El doble de 60 y el doble de 8", "Doble de 60 = 120 y doble de 8 = 16: 120 + 16 = 136."),
        ex("¿La mitad de 7 es exacta con números enteros?", "No", "7 es impar: no se puede repartir en dos partes iguales enteras."),
    ],
    app=[
        arith("Un paquete trae 135 hojas. ¿Cuántas hojas hay en 2 paquetes iguales?", "135*2", "Doblar 135: 100 + 100, 30 + 30 y 5 + 5."),
        arith("Se reparten 174 stickers en partes iguales entre 2 amigas. ¿Cuántos recibe cada una?", "174//2", "Mitad de 100 = 50, de 70 = 35, de 4 = 2."),
        ex("Dobla estos números: 15, 150 y 1.500.", "30, 300 y 3.000", "Cada doble es 2 veces el número: 15 × 2 = 30; 150 × 2 = 300; 1.500 × 2 = 3.000."),
    ],
    rea=[
        ex("Lola dice que la mitad de 1.000 es 50. Revisa con el doble: ¿tiene razón?", "No, es 500", "El doble de 50 es 100, no 1.000. El doble de 500 es 1.000."),
        ex("Marcos dice: «Para sacar la mitad de 90 puedo sacar la de 80 y la de 10». ¿Funciona? ¿Qué número obtiene?", "Sí, 45", "Mitad de 80 = 40, mitad de 10 = 5 y 40 + 5 = 45."),
    ],
    cha=[
        ex("El doble de un número es 168. ¿Cuál es el número?", "84", "La mitad de 168: mitad de 160 = 80 y mitad de 8 = 4, total 84."),
        ex("Tengo $ 480 y mi hermana tiene la mitad de lo que tengo yo. ¿Cuánto tienen entre las dos?", "$ 720", "Mitad de 480 = 240. 480 + 240 = 720."),
    ],
    ctx=[ex("Un cuaderno cuesta $ 650 y una amiga compra 2. ¿Cuánto paga en total?", "$ 1.300", "Doble de 600 = 1.200 y doble de 50 = 100; 1.200 + 100 = 1.300.")],
    sc=[
        ex("¿Cuál es el doble de 45?", "90", "40 + 40 = 80 y 5 + 5 = 10; 80 + 10 = 90."),
        ex("¿Cuál es la mitad de 120?", "60", "La mitad de 100 es 50 y la de 20 es 10."),
        ex("¿Cuál es el doble de 2.500?", "5.000", "Doble de 2.000 = 4.000 y doble de 500 = 1.000."),
    ],
    op=task(
        "Calcula de cabeza el doble de 36, el doble de 185 y la mitad de 94, la mitad de 210. Escribe cómo separaste cada número en partes y comprueba cada mitad doblándola.",
        "Doble de 36: 30 + 30 y 6 + 6 = 72. Doble de 185: 100 + 100, 80 + 80, 5 + 5 = 370. Mitad de 94: mitad de 90 = 45 y de 4 = 2 → 47 (47 × 2 = 94). Mitad de 210: 105 (105 × 2 = 210).",
        ["calcula bien los cuatro", "separa en partes", "comprueba las mitades doblando"],
        ["cuatro resultados escritos", "separaciones en partes escritas"],
        ["sumar en vez de doblar", "olvidar una parte al separar"],
        "Ayuda a ver que cada resultado se comprueba con la operación contraria: el doble de la mitad vuelve al número.",
    ),
    reinforce="Haz una tabla con los números 12, 24, 36 y 48: escribe el doble y la mitad de cada uno.",
    extend="Descubre una regla: ¿qué pasa con la cifra de las decenas cuando sacas la mitad de un número que termina en 0? Prueba con 70, 80 y 90.",
)

lesson(
    OA2, 3,
    use="Aprenderé a sumar y restar de cabeza separando los números en partes y a compensar. Sirve para calcular cuentas de dos y tres cifras sin escribirlas.",
    prior=["Conozco el valor posicional de decenas y centenas.", "Sé sumar y restar números de dos cifras."],
    explain=[
        "Descomponer es separar un número por su valor posicional. Para 47 + 36, separa 47 en 40 + 7 y 36 en 30 + 6. Suma primero las decenas: 40 + 30 = 70. Luego las unidades: 7 + 6 = 13. Al final junta: 70 + 13 = 83.",
        "También puedes descomponer solo un número. Para 78 − 23 conserva el 78 y resta 23 por partes: 78 − 20 = 58 y luego 58 − 3 = 55. Resta primero la parte más grande y después la pequeña.",
        "Compensar es cambiar un número por otro más fácil y arreglar después. Para 49 + 27 sumas 50 + 27 = 77 y quitas 1, que agregaste de más: 76. Para 99 − 45 restas 100 − 45 = 55 y quitas el 1 que agregaste de más al cambiar 99 por 100: 54.",
    ],
    vocab=[("descomponer", "separar un número en partes según el valor de sus cifras"), ("compensar", "cambiar un número por otro más fácil y arreglar el resultado después"), ("sumando", "cada número que se suma"), ("redondear", "cambiar un número por el más cercano terminado en 0"), ("estrategia", "forma ordenada de resolver un cálculo")],
    worked=[
        W("Sumar descomponiendo", "Calcula 47 + 36 de cabeza.", ["Separo: 47 = 40 + 7 y 36 = 30 + 6.", "Decenas: 40 + 30 = 70. Unidades: 7 + 6 = 13.", "Junto: 70 + 13 = 83."], "83"),
        W("Compensar", "Calcula 199 + 45 de cabeza.", ["199 está a 1 de 200: uso 200 + 45 = 245.", "Sumé 1 de más, así que lo quito: 245 − 1.", "El resultado es 244."], "244"),
    ],
    mistakes=[
        M("Calcular 49 + 27 como 77 después de cambiarlo por 50 + 27.", "Se olvida arreglar lo que se agregó de más.", "Sumaste 1 de más al usar 50: quita 1 y queda 76."),
        M("Calcular 78 − 23 como 61 al hacer 78 − 20 = 58 y luego 58 + 3.", "Se suma en vez de restar la parte pequeña.", "Las dos partes se restan: 58 − 3 = 55."),
    ],
    rec=[
        ex("Calcula 34 + 25 separando en decenas y unidades.", "59", "30 + 20 = 50 y 4 + 5 = 9; 50 + 9 = 59."),
        ex("Calcula 78 − 23 restando primero 20 y luego 3.", "55", "78 − 20 = 58 y 58 − 3 = 55."),
        ex("Calcula 300 + 450 separando en centenas y decenas.", "750", "300 + 400 = 700 y 700 + 50 = 750."),
    ],
    und=[
        ex("Para 49 + 27 se calcula 50 + 27 = 77. ¿Qué hay que hacer después?", "Restar 1", "Se sumó 1 de más al cambiar 49 por 50: 77 − 1 = 76."),
        ex("En 99 − 45 se calcula 100 − 45 = 55. ¿Qué hay que hacer después?", "Restar 1", "Al cambiar 99 por 100 se partió con 1 de más; 55 − 1 = 54."),
        ex("Al sumar 58 + 25 separando, ¿qué suma de unidades se obtiene?", "13", "Las unidades son 8 y 5: 8 + 5 = 13."),
    ],
    app=[
        arith("Un álbum tiene 168 láminas y se agregan 125. ¿Cuántas láminas hay ahora?", "168+125", "100 + 100 = 200, 60 + 20 = 80 y 8 + 5 = 13."),
        arith("Un tren llevaba 240 pasajeros y se bajaron 78. ¿Cuántos quedan?", "240-78", "Se resta 80 y se devuelven 2 que sobraron."),
        arith("Calcula 599 + 120 usando que 599 está cerca de 600.", "599+120", "600 + 120 = 720; se quita 1 que se sumó de más."),
    ],
    rea=[
        ex("Teo calculó 38 + 47 como 30 + 40 = 70 y 8 + 7 = 15, y dijo que da 70. ¿Qué le falta?", "Falta sumar 15; da 85", "Hay que juntar las dos partes: 70 + 15 = 85."),
        ex("Ema dice que 99 + 99 se calcula como 100 + 100 − 2. ¿Tiene razón? ¿Cuánto da?", "Sí, 198", "Cada 99 está a 1 de 100, así que se agregan 2 de más: 200 − 2 = 198."),
    ],
    cha=[
        ex("Calcula 1.050 − 998 de cabeza usando que 998 está a 2 de 1.000.", "52", "1.050 − 1.000 = 50 y se devuelven 2 que se restaron de más: 52."),
        ex("Escribe el número que falta: 37 + __ = 100. Usa que 37 + 3 = 40.", "63", "37 + 3 = 40 y 40 + 60 = 100; 3 + 60 = 63."),
    ],
    ctx=[ex("Ana compra una polera de $ 1.990 y unos calcetines de $ 590. Usa 2.000 para compensar y calcula el total.", "$ 2.580", "2.000 + 590 = 2.590 y se quitan 10 de más: 2.580.")],
    sc=[
        ex("Calcula 56 + 27 separando en decenas y unidades.", "83", "50 + 20 = 70 y 6 + 7 = 13; 83."),
        ex("Calcula 89 + 40 con compensación (usa 90).", "129", "90 + 40 = 130 y se quita 1."),
        ex("Calcula 95 − 30 de cabeza.", "65", "95 − 30: se restan 3 decenas, 9 − 3 = 6 decenas y quedan 5 unidades."),
    ],
    op=task(
        "Calcula de cabeza 68 + 47 y 299 + 156. Escribe para cada cuenta cómo separaste o qué número cambiaste por otro más fácil, y qué hiciste para arreglar el resultado.",
        "68 + 47: 60 + 40 = 100 y 8 + 7 = 15 → 115. 299 + 156: 300 + 156 = 456, menos 1 de más → 455.",
        ["calcula bien las dos", "explica la estrategia", "arregla lo que compensó"],
        ["dos cálculos con pasos escritos"],
        ["olvidar compensar", "perder una parte al separar"],
        "Reconoce el cálculo correcto y pide comprobarlo con otra estrategia; si falla, ubica en qué paso se perdió una parte.",
    ),
    reinforce="Practica 29 + 36, 48 + 25 y 62 − 18 con la separación en decenas y unidades.",
    extend="Calcula 2.999 + 1.001 usando una compensación y explica por qué da un número redondo.",
)

lesson(
    OA2, 4,
    use="Aprenderé a multiplicar por 4 y por 8 usando el doble del doble. Sirve para recordar las tablas del 4 y del 8 a partir de la del 2.",
    prior=["Sé doblar números de dos cifras.", "Sé la tabla del 2 y la del 5."],
    explain=[
        "Multiplicar por 4 es lo mismo que doblar dos veces. Como 4 = 2 × 2, el doble del doble de un número es ese número por 4. Para 6 × 4: el doble de 6 es 12 y el doble de 12 es 24. Entonces 6 × 4 = 24.",
        "Multiplicar por 8 es doblar tres veces. Para 7 × 8: el doble de 7 es 14, el doble de 14 es 28 y el doble de 28 es 56. Entonces 7 × 8 = 56. Con esto reconstruyes las tablas del 4 y del 8 sin memorizar todo.",
        "El doble del doble también sirve para dividir. Dividir por 4 es sacar la mitad de la mitad. Para 36 ÷ 4: la mitad de 36 es 18 y la mitad de 18 es 9. Entonces 36 ÷ 4 = 9, porque 9 × 4 = 36.",
    ],
    vocab=[("doble del doble", "multiplicar por 2 y volver a multiplicar por 2, es decir, por 4"), ("mitad de la mitad", "dividir por 2 y volver a dividir por 2, es decir, por 4"), ("multiplicación", "operación que repite un número varias veces"), ("división", "operación que reparte en partes iguales"), ("tabla de multiplicar", "lista de los resultados de multiplicar un número por 1, 2, 3, hasta 10")],
    worked=[
        W("Multiplicar por 4", "Calcula 8 × 4 con el doble del doble.", ["El doble de 8 es 16.", "El doble de 16 es 32.", "Entonces 8 × 4 = 32."], "32"),
        W("Dividir por 4", "Calcula 48 ÷ 4 con la mitad de la mitad.", ["La mitad de 48 es 24.", "La mitad de 24 es 12.", "Compruebo: 12 × 4 = 48."], "12"),
    ],
    mistakes=[
        M("Calcular 7 × 4 como 14 porque «dobla una vez».", "Se dobla solo una vez, pero 4 pide dos dobles.", "Dobla dos veces: 7 → 14 → 28. Así 7 × 4 = 28."),
        M("Calcular 7 × 8 como 112.", "Se dobla una vez de más (cuatro dobles).", "8 es tres dobles: 7 → 14 → 28 → 56. Al llegar a 56 ya terminaste."),
    ],
    rec=[
        ex("Calcula 6 × 4 con el doble del doble.", "24", "El doble de 6 es 12 y el doble de 12 es 24."),
        ex("Calcula 9 × 4 con el doble del doble.", "36", "El doble de 9 es 18 y el doble de 18 es 36."),
        ex("Calcula 5 × 8 doblando tres veces.", "40", "5 → 10 → 20 → 40."),
    ],
    und=[
        ex("¿Por qué el doble del doble sirve para multiplicar por 4?", "Porque 2 × 2 = 4", "Doblar dos veces es multiplicar por 2 y otra vez por 2, o sea por 4."),
        ex("¿Cuántas veces se dobla un número para multiplicarlo por 8?", "3 veces", "2 × 2 × 2 = 8, así que son tres dobles."),
        ex("Para dividir 36 por 4, ¿cuántas veces se saca la mitad?", "2 veces", "Dividir por 4 es dividir por 2 y otra vez por 2."),
    ],
    app=[
        arith("Cada mesa tiene 4 patas. ¿Cuántas patas hay en 12 mesas? Usa el doble del doble.", "12*4", "Doble de 12 = 24 y doble de 24 = 48."),
        arith("Un paquete trae 8 galletas. ¿Cuántas galletas hay en 7 paquetes?", "7*8", "7 → 14 → 28 → 56 con tres dobles."),
        arith("Se reparten 52 láminas en partes iguales entre 4 niños. ¿Cuántas recibe cada uno?", "52//4", "Mitad de 52 = 26 y mitad de 26 = 13."),
    ],
    rea=[
        ex("Camilo calculó 6 × 8 como 6 → 12 → 24 y dijo que da 24. ¿Qué paso le falta?", "Un doble más: da 48", "8 es tres dobles. Falta doblar 24, que da 48."),
        ex("¿Cierto o falso? «Si 9 × 4 = 36, entonces 9 × 8 = 72».", "Cierto", "9 × 8 es el doble de 9 × 4: 36 × 2 = 72."),
    ],
    cha=[
        ex("Usa la tabla del 2 para obtener 12 × 8. ¿Cuánto es?", "96", "12 → 24 → 48 → 96."),
        ex("Un número multiplicado por 4 da 84. ¿Cuál es el número?", "21", "84 ÷ 4: la mitad de 84 es 42 y la mitad de 42 es 21."),
    ],
    ctx=[ex("En una pastelería hay 8 bandejas con 6 pasteles cada una. ¿Cuántos pasteles hay? Usa dobles.", "48", "6 → 12 → 24 → 48: tres dobles son × 8.")],
    sc=[
        ex("Calcula 7 × 4.", "28", "El doble de 7 es 14 y el doble de 14 es 28."),
        ex("Calcula 40 ÷ 4 con la mitad de la mitad.", "10", "La mitad de 40 es 20 y la mitad de 20 es 10."),
        ex("Calcula 4 × 8 doblando tres veces.", "32", "4 → 8 → 16 → 32."),
    ],
    op=task(
        "Completa la tabla del 4 y del 8 desde 1 hasta 10 usando solo dobles. Escribe en el cuaderno dos columnas y marca con un círculo un resultado que te cueste y explica cómo lo obtuviste con los dobles.",
        "Tabla del 4: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40. Tabla del 8: 8, 16, 24, 32, 40, 48, 56, 64, 72, 80. Me cuesta 8 × 7 = 56: 7 → 14 → 28 → 56.",
        ["completa las dos tablas", "cada resultado del 8 es el doble del 4", "explica con dobles un resultado"],
        ["dos columnas completas", "explicación escrita de un resultado"],
        ["doblar solo una vez para × 4", "no revisar con la tabla del 4"],
        "Pide que compare las dos tablas: cada resultado del 8 debe ser el doble del resultado del 4 en la misma fila.",
    ),
    reinforce="Escribe la tabla del 2 de 1 a 10, dóblala para obtener la tabla del 4 y dóblala otra vez para la del 8.",
    extend="Usa la mitad de la mitad para calcular 120 ÷ 4 y 800 ÷ 4. ¿Qué observas al dividir números terminados en 0?",
)

lesson(
    OA2, 5,
    use="Aprenderé a usar las multiplicaciones para encontrar divisiones y viceversa. Sirve para calcular divisiones sabiendo las tablas hasta 10 × 10.",
    prior=["Conozco varias tablas de multiplicar (las del 2, 4, 5 y 10) y puedo armar las otras con dobles y sumas.", "Sé que multiplicar es repetir un número."],
    explain=[
        "Cada multiplicación tiene hechos relacionados. Si sabes que 7 × 6 = 42, también sabes que 6 × 7 = 42, 42 ÷ 6 = 7 y 42 ÷ 7 = 6. Son cuatro cuentas que usan los mismos tres números.",
        "Para dividir, pregúntate: ¿qué número por el divisor da el dividendo? Para 56 ÷ 8, busca el número que al multiplicarlo por 8 dé 56. Como 7 × 8 = 56, entonces 56 ÷ 8 = 7. Así una tabla que sabes te ayuda a resolver divisiones.",
        "Si no recuerdas un resultado, usa lo que sabes: 6 × 8 es 5 × 8 más un 8 más, o el doble de 3 × 8. Con 40 + 8 = 48 obtienes 6 × 8, y luego 48 ÷ 8 = 6 y 48 ÷ 6 = 8. Siempre comprueba multiplicando.",
    ],
    vocab=[("hecho relacionado", "multiplicación o división que usa los mismos tres números"), ("dividendo", "el número que se reparte"), ("divisor", "el número entre el que se reparte"), ("cociente", "resultado de una división"), ("familia de operaciones", "las cuatro cuentas que usan tres números relacionados"), ("factor", "cada número que se multiplica"), ("producto", "resultado de una multiplicación")],
    worked=[
        W("Familia de operaciones", "Escribe las cuatro cuentas de la familia de 7, 6 y 42.", ["Multiplicaciones: 7 × 6 = 42 y 6 × 7 = 42.", "Divisiones: 42 ÷ 6 = 7 y 42 ÷ 7 = 6.", "Compruebo que todas usan 6, 7 y 42."], "7 × 6 = 42; 6 × 7 = 42; 42 ÷ 6 = 7; 42 ÷ 7 = 6"),
        W("Dividir con la tabla", "Calcula 72 ÷ 9.", ["Pregunto: ¿qué número por 9 da 72?", "Pruebo 8 × 9 = 72, que es la tabla del 9.", "Entonces 72 ÷ 9 = 8."], "8"),
    ],
    mistakes=[
        M("Decir que 42 ÷ 6 = 8 porque 6 × 8 = 48.", "Se usa una multiplicación que no da el dividendo.", "Busca la multiplicación que da 42: 6 × 7 = 42, así que 42 ÷ 6 = 7."),
        M("Escribir 6 ÷ 42 = 7.", "Se invierte el dividendo y el divisor.", "El número que se reparte va primero y es el mayor: 42 ÷ 6."),
    ],
    rec=[
        ex("Si 5 × 9 = 45, ¿cuánto es 45 ÷ 9?", "5", "Se busca el factor que falta: 5 × 9 = 45."),
        ex("Si 8 × 4 = 32, ¿cuánto es 32 ÷ 8?", "4", "4 × 8 = 32."),
        ex("Si 6 × 7 = 42, ¿cuánto es 7 × 6?", "42", "Se pueden cambiar el orden de los factores sin cambiar el producto."),
    ],
    und=[
        ex("¿Qué multiplicación te ayuda a calcular 56 ÷ 8?", "7 × 8 = 56", "El número que multiplicado por 8 da 56 es 7."),
        ex("Escribe las otras tres cuentas de la familia de 9 × 4 = 36.", "4 × 9 = 36; 36 ÷ 9 = 4; 36 ÷ 4 = 9", "Con 4, 9 y 36 se arman cuatro cuentas."),
        ex("En 48 ÷ 6 = 8, ¿cuál es el divisor?", "6", "El divisor es el número entre el que se reparte."),
    ],
    app=[
        arith("Se reparten 63 manzanas en cajas de 9. ¿Cuántas cajas se llenan?", "63//9", "9 × 7 = 63, así que 63 ÷ 9 = 7."),
        arith("Una tira tiene 72 cm y se corta en trozos de 8 cm. ¿Cuántos trozos salen?", "72//8", "8 × 9 = 72, así que 72 ÷ 8 = 9."),
        arith("¿Cuántas patas hay en 7 sillas de 4 patas cada una?", "7*4", "Se usa la tabla del 4: 7 × 4 = 28."),
    ],
    rea=[
        ex("Pablo dice: «Como 6 × 8 = 48, entonces 48 ÷ 8 = 6 y 48 ÷ 6 = 8». ¿Tiene razón?", "Sí", "Los hechos relacionados dividen el producto entre cada factor."),
        ex("Rosa dice que 36 ÷ 9 = 5 porque 5 × 9 = 36. Revisa: ¿está bien?", "No, es 4", "5 × 9 = 45. Con 4 × 9 = 36, entonces 36 ÷ 9 = 4."),
    ],
    cha=[
        ex("Sin usar la tabla del 7 completa, calcula 7 × 8 usando 5 × 8 y 2 × 8.", "56", "5 × 8 = 40 y 2 × 8 = 16; 40 + 16 = 56."),
        ex("Un número multiplicado por 6 da 54. ¿Cuál es el número y qué división lo muestra?", "9; 54 ÷ 6 = 9", "9 × 6 = 54, así que 54 ÷ 6 = 9."),
    ],
    ctx=[ex("Un curso de 40 estudiantes hace grupos de 5. ¿Cuántos grupos se forman? Escribe la multiplicación que usas.", "8 grupos; 8 × 5 = 40", "8 × 5 = 40, entonces 40 ÷ 5 = 8.")],
    sc=[
        ex("Si 9 × 8 = 72, ¿cuánto es 72 ÷ 8?", "9", "El factor que falta es 9."),
        ex("Calcula 45 ÷ 5 con la tabla del 5.", "9", "5 × 9 = 45."),
        ex("Escribe una división de la familia de 6 × 4 = 24.", "24 ÷ 4 = 6 o 24 ÷ 6 = 4", "Las dos divisiones usan los mismos tres números."),
    ],
    op=task(
        "Escribe la familia de operaciones de 8, 7 y 56 y la de 9, 3 y 27. Luego calcula 63 ÷ 7 y explica qué multiplicación te ayudó.",
        "8 × 7 = 56, 7 × 8 = 56, 56 ÷ 7 = 8, 56 ÷ 8 = 7; 9 × 3 = 27, 3 × 9 = 27, 27 ÷ 3 = 9, 27 ÷ 9 = 3. 63 ÷ 7 = 9 porque 9 × 7 = 63.",
        ["escribe las ocho cuentas", "calcula 63 ÷ 7", "explica la multiplicación usada"],
        ["ocho cuentas escritas", "explicación de la división"],
        ["poner el dividendo al final", "usar un producto que no es el dividendo"],
        "Pide que compruebe cada división multiplicando el cociente por el divisor.",
    ),
    reinforce="Elige tres multiplicaciones de la tabla del 6 y escribe sus divisiones relacionadas.",
    extend="Usa 12 × 6 = 72 para calcular 72 ÷ 6 y 72 ÷ 12. ¿Qué pasa con las divisiones relacionadas cuando uno de los factores tiene dos cifras?",
)
