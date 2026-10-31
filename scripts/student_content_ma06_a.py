"""Cuaderno del estudiante de 6.º básico Matemática: OA 01 (factores, múltiplos y primos) y OA 02 (operaciones combinadas)."""
from __future__ import annotations

from student_lessons import arith, ex, fmt, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


MATERIALS = "Cuaderno, lápiz y, si la tienes, calculadora. Todos los datos que necesitas están escritos en cada ejercicio."


def lesson(oa, n, *, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, ctx, sc, op, reinforce, extend, mat=MATERIALS):
    register(
        oa, n, materials=mat, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": rec, "understand": und, "apply": app, "reason": rea, "challenge": cha},
        context=ctx, selfcheck=sc, open_task=op, reinforce=reinforce, extend=extend,
    )


OA1 = "MA06 OA 01"

# ------------------------------------------------------------------ OA 01 clase 1
lesson(
    OA1, 1,
    use="Aprenderé qué es un múltiplo y qué es un factor de un número natural menor que 100. Sirve para repartir cosas en grupos iguales y para saber cuándo algo se repite.",
    prior=["Me sé las tablas de multiplicar.", "Sé que dividir es repartir en partes iguales."],
    explain=[
        "Un múltiplo de un número es el resultado de multiplicarlo por 1, por 2, por 3 y así sucesivamente. Los múltiplos de 6 son 6, 12, 18, 24, 30… Son los números de la tabla del 6. Un número tiene infinitos múltiplos, por eso en los ejercicios se pone un límite, como «menores que 50».",
        "Un factor de un número es un número natural que lo divide exactamente, sin dejar resto. También es cada número que se multiplica para formar el otro: como 3 × 4 = 12, el 3 y el 4 son factores de 12. Los factores de 12 son 1, 2, 3, 4, 6 y 12. El 1 y el número mismo siempre son factores.",
        "Factor y múltiplo son nombres que se dan en pareja. Si 5 × 7 = 35, entonces 5 y 7 son factores de 35, y 35 es múltiplo de 5 y de 7. Un número tiene una cantidad pequeña de factores, pero muchos múltiplos. Los factores nunca son mayores que el número; los múltiplos nunca son menores.",
    ],
    vocab=[("múltiplo", "resultado de multiplicar un número por 1, 2, 3, 4…"), ("factor", "número natural que divide exactamente a otro; también, cada número de una multiplicación"), ("divisor", "otro nombre para un factor"), ("divisible", "que se puede dividir sin que sobre nada"), ("natural", "número que se usa para contar: 1, 2, 3…")],
    worked=[
        W("Listar múltiplos con un límite", "Escribe los múltiplos de 7 menores que 50.", ["Multiplico 7 por 1, 2, 3… : 7, 14, 21, 28, 35, 42, 49.", "7 × 8 = 56 ya pasa de 50, así que me detengo en 49."], "7, 14, 21, 28, 35, 42 y 49"),
        W("Listar factores en parejas", "Escribe todos los factores de 18.", ["Busco parejas que multiplicadas den 18: 1 × 18, 2 × 9, 3 × 6.", "Junto los números de las parejas, de menor a mayor."], "1, 2, 3, 6, 9 y 18"),
    ],
    mistakes=[
        M("Decir que los factores de 12 son 1, 2, 3, 4, 6, 12 y 24.", "Se incluyó 24, que es un múltiplo de 12 y no un factor.", "Los factores no pueden ser mayores que el número: terminan en 12."),
        M("Escribir los múltiplos de 5 como 1 y 5.", "Se confundió factor con múltiplo.", "Los múltiplos de 5 son 5, 10, 15, 20…; 1 y 5 son sus factores."),
    ],
    rec=[
        ex("¿Cuál es el tercer múltiplo de 8? El primer múltiplo es 8 × 1.", "24", "Tercer múltiplo: 8 × 3 = 24."),
        ex("Sabes que 4 × 6 = 24. Nombra dos factores de 24 que salgan de esa multiplicación.", "4 y 6", "Los dos números que se multiplican son factores del resultado."),
        ex("¿Es 12 múltiplo de 4? Responde sí o no.", "Sí", "4 × 3 = 12, así que 12 está en la tabla del 4."),
    ],
    und=[
        ex("Escribe todos los múltiplos de 9 menores que 60.", "9, 18, 27, 36, 45 y 54", "Se multiplica 9 por 1, 2, 3, 4, 5 y 6; 9 × 7 = 63 ya pasa de 60."),
        ex("Escribe todos los factores de 20, de menor a mayor.", "1, 2, 4, 5, 10 y 20", "Las parejas son 1 × 20, 2 × 10 y 4 × 5."),
        ex("¿7 es factor o múltiplo de 35?", "Factor", "7 × 5 = 35: el 7 divide a 35, por eso es factor."),
    ],
    app=[
        ex("Escribe todos los factores de 36, de menor a mayor.", "1, 2, 3, 4, 6, 9, 12, 18 y 36", "Parejas: 1 × 36, 2 × 18, 3 × 12, 4 × 9 y 6 × 6; el 6 se escribe una sola vez."),
        ex("¿Cuántos múltiplos de 12 hay menores que 100?", "8", "12, 24, 36, 48, 60, 72, 84 y 96 son ocho; 12 × 9 = 108 ya pasa de 100."),
        ex("Una caja tiene 28 chocolates y se reparten en bolsitas con igual cantidad, sin que sobre ninguno. Cada bolsita lleva más de 1 y menos de 28 chocolates. ¿Cuántas cantidades distintas por bolsita se pueden usar?", "4", "Los factores de 28 son 1, 2, 4, 7, 14 y 28; sin el 1 y el 28 quedan 2, 4, 7 y 14."),
    ],
    rea=[
        ex("Pía dice: «15 es factor de 5 porque 15 es el número más grande». ¿Qué debería decir?", "5 es factor de 15", "15 = 5 × 3, así que 5 divide a 15; el factor es el que divide y 15 es el múltiplo."),
        ex("Mario escribió los factores de 10: 1, 2, 5, 10 y 20. ¿Cuál número sobra?", "20", "20 es múltiplo de 10; ningún factor puede ser mayor que el número."),
    ],
    cha=[
        ex("Hay un único número menor que 100 que es múltiplo de 9 y de 11 a la vez. ¿Cuál es?", "99", "Múltiplos de 11: 11, 22, 33… hasta 99; solo 99 está en la tabla del 9 (9 × 11)."),
        ex("Un número menor que 20 es múltiplo de 7 y tiene exactamente 4 factores. ¿Cuál es?", "14", "Los múltiplos de 7 menores que 20 son 7 y 14; 7 tiene 2 factores y 14 tiene 4 (1, 2, 7, 14)."),
    ],
    ctx=[ex("Una profesora tiene 30 lápices y los reparte en bolsitas con la misma cantidad, sin que sobre ninguno. ¿Cuántas cantidades distintas por bolsita puede usar, contando 1 y 30?", "8", "Los factores de 30 son 1, 2, 3, 5, 6, 10, 15 y 30.")],
    sc=[
        ex("¿Cuál es el quinto múltiplo de 7?", "35", "7 × 5 = 35."),
        ex("¿Es 6 factor de 54?", "Sí", "6 × 9 = 54, así que 6 divide a 54 sin resto."),
        ex("¿Cuántos factores tiene el 16?", "5", "1, 2, 4, 8 y 16."),
    ],
    op=task(
        "Elige uno de estos números: 24, 30 o 45. Escribe todos sus factores y sus tres primeros múltiplos. Después explica con una frase la diferencia entre un factor y un múltiplo.",
        "Para 24: factores 1, 2, 3, 4, 6, 8, 12 y 24; primeros múltiplos 24, 48 y 72. Un factor divide al número y un múltiplo es el número multiplicado.",
        ["lista completa de factores", "múltiplos bien calculados", "explica la diferencia entre factor y múltiplo"],
        ["listas escritas en el cuaderno", "frase de explicación"],
        ["incluir múltiplos entre los factores", "olvidar el 1 o el mismo número"],
        "Pide que compruebe cada factor dividiendo el número entre él y viendo que no sobra nada.",
    ),
    reinforce="Escribe los factores de 15 y los primeros cinco múltiplos de 15. Subraya con un color los factores y con otro los múltiplos.",
    extend="Busca un número menor que 100 que tenga más de 8 factores. Escribe todos sus factores y explica cómo los encontraste.",
)

# ------------------------------------------------------------------ OA 01 clase 2
lesson(
    OA1, 2,
    use="Aprenderé a reconocer números primos y compuestos menores que 100. Sirve para saber cuándo un número se puede repartir en grupos iguales y cuándo no.",
    prior=["Sé listar los factores de un número.", "Conozco los múltiplos y las tablas de multiplicar."],
    explain=[
        "Un número primo es un número natural que tiene exactamente dos factores: el 1 y él mismo. Por ejemplo, 7 es primo porque solo se puede formar con 1 × 7. Un número compuesto tiene más de dos factores, como 12, que tiene seis. El número 1 no es primo ni compuesto, porque tiene un solo factor.",
        "Para decidir si un número es primo, busca un factor distinto de 1 y del número. Hay pistas rápidas: si termina en 0, 2, 4, 6 u 8 es divisible por 2; si termina en 0 o 5 es divisible por 5; si la suma de sus cifras es múltiplo de 3, es divisible por 3. En números menores que 100 basta probar con 2, 3, 5 y 7.",
        "El único primo par es el 2: todos los demás pares también se pueden dividir por 2. Los primos menores que 20 son 2, 3, 5, 7, 11, 13, 17 y 19. Que un número sea impar no asegura que sea primo: 9 = 3 × 3 y 15 = 3 × 5 son impares y compuestos.",
    ],
    vocab=[("número primo", "número natural con exactamente dos factores: 1 y él mismo"), ("número compuesto", "número natural con más de dos factores"), ("divisible por 3", "número cuyas cifras suman un múltiplo de 3"), ("criterio de divisibilidad", "regla rápida para saber si un número se divide exactamente por otro"), ("par", "número que termina en 0, 2, 4, 6 u 8")],
    worked=[
        W("Decidir si un número es compuesto", "¿Es 57 un número primo?", ["No termina en 0, 2, 4, 5, 6 ni 8.", "Sus cifras suman 5 + 7 = 12, que es múltiplo de 3, entonces 57 se divide por 3: 57 = 3 × 19.", "Tiene un factor distinto de 1 y de 57."], "No, es compuesto"),
        W("Decidir si un número es primo", "¿Es 41 un número primo?", ["No es par, no termina en 5 y sus cifras suman 5, que no es múltiplo de 3.", "Pruebo con 7: 7 × 5 = 35 y 7 × 6 = 42, así que no cae justo en 41.", "Ya probé 2, 3, 5 y 7: no tiene otros factores."], "Sí, 41 es primo"),
    ],
    mistakes=[
        M("Decir que 1 es un número primo.", "Se olvidó que un primo debe tener dos factores distintos y el 1 solo tiene uno.", "El 1 no es primo ni compuesto."),
        M("Decir que 21 es primo porque es impar.", "Se pensó que todos los impares son primos.", "21 = 3 × 7, tiene más de dos factores: es compuesto."),
    ],
    rec=[
        ex("¿Cuántos factores tiene un número primo?", "2", "Solo el 1 y el propio número."),
        ex("¿El número 1 es primo? Responde sí o no.", "No", "Tiene un solo factor, el 1, y un primo necesita dos."),
        ex("Entre 9, 13, 15 y 21, ¿cuál es primo?", "13", "9 = 3 × 3, 15 = 3 × 5 y 21 = 3 × 7; 13 solo se forma con 1 × 13."),
    ],
    und=[
        ex("Escribe todos los números primos menores que 20.", "2, 3, 5, 7, 11, 13, 17 y 19", "Cada uno tiene solo dos factores; 4, 6, 8, 9, 10, 12, 14, 15, 16 y 18 son compuestos."),
        ex("¿Es 51 primo o compuesto?", "Compuesto", "5 + 1 = 6 es múltiplo de 3, entonces 51 = 3 × 17."),
        ex("¿Es 49 primo o compuesto?", "Compuesto", "49 = 7 × 7, así que tiene tres factores: 1, 7 y 49."),
    ],
    app=[
        ex("De 61, 63, 65 y 67, ¿cuáles son primos?", "61 y 67", "63 = 7 × 9 y 65 = 5 × 13 son compuestos; 61 y 67 no tienen factores aparte del 1 y de sí mismos."),
        ex("¿Cuántos números primos hay entre 30 y 50?", "5", "Son 31, 37, 41, 43 y 47."),
        ex("¿Cuál es el mayor número primo menor que 90?", "89", "88 es par, 87 = 3 × 29 y 89 no tiene otros factores."),
    ],
    rea=[
        ex("Sol dice: «todos los números impares son primos». ¿Cuál es el menor número impar mayor que 1 que sirve para demostrar que se equivoca?", "9", "3, 5 y 7 son primos; 9 es impar y 9 = 3 × 3, así que no es primo y basta ese ejemplo para refutar la regla."),
        ex("Leo dice que 91 es primo porque es impar, no termina en 5 y sus cifras suman 10, que no es múltiplo de 3. ¿Tiene razón?", "No", "También hay que probar con 7: 7 × 13 = 91, así que es compuesto."),
    ],
    cha=[
        ex("Dos números primos distintos suman 24 y su diferencia es 14. ¿Cuáles son?", "5 y 19", "5 + 19 = 24 y 19 − 5 = 14; los dos son primos."),
        ex("Hay un único número primo entre 70 y 80 que termina en 3. ¿Cuál es?", "73", "Los primos entre 70 y 80 son 71, 73 y 79; solo 73 termina en 3."),
    ],
    ctx=[ex("En una escuela ficticia los casilleros están numerados del 1 al 30 y se pintan de rojo solo los que tienen número primo. ¿Cuántos casilleros quedan rojos?", "10", "Los primos hasta 30 son 2, 3, 5, 7, 11, 13, 17, 19, 23 y 29.")],
    sc=[
        ex("¿Es 83 primo o compuesto?", "Primo", "No es par, sus cifras suman 11, no termina en 5 y 7 × 12 = 84 no cae en 83."),
        ex("¿Es 87 primo o compuesto?", "Compuesto", "8 + 7 = 15, múltiplo de 3: 87 = 3 × 29."),
        ex("¿Cuántos números primos hay entre 1 y 10?", "4", "Son 2, 3, 5 y 7."),
    ],
    op=task(
        "Con estos números: 29, 33, 39, 47, 51 y 53, haz dos columnas, «primos» y «compuestos». En los compuestos escribe un factor distinto de 1 y del número. Explica con una frase cómo decidiste uno de ellos.",
        "29 y 47 y 53 son primos. 33 = 3 × 11, 39 = 3 × 13 y 51 = 3 × 17 son compuestos. Decidí 33 porque 3 + 3 = 6 es múltiplo de 3.",
        ["clasifica bien los seis números", "da un factor de cada compuesto", "explica el criterio usado"],
        ["tabla de dos columnas", "frase que explica un criterio"],
        ["creer que todo impar es primo", "olvidar probar con 7"],
        "Pide que revise cada compuesto multiplicando el factor que encontró por el otro para ver que da el número.",
    ),
    reinforce="Escribe los números del 1 al 30 en una tabla y tacha el 1, luego los múltiplos de 2 (menos el 2), de 3 (menos el 3) y de 5 (menos el 5). Los que quedan son primos.",
    extend="Busca dos primos que estén uno al lado del otro con una diferencia de solo 2 (como 11 y 13), mayores que 40. Escríbelos y explica cómo comprobaste que son primos.",
)

# ------------------------------------------------------------------ OA 01 clase 3
lesson(
    OA1, 3,
    use="Aprenderé a escoger una estrategia para encontrar factores y múltiplos: parejas de factores y criterios de divisibilidad. Sirve para ahorrar tiempo y no olvidar ninguno.",
    prior=["Sé qué es un factor y un múltiplo.", "Sé distinguir primos de compuestos."],
    explain=[
        "Para encontrar todos los factores de un número, usa las parejas. Empieza con 1 y el número, luego prueba 2, 3, 4… Cada vez que un número divide exactamente, anota la pareja. Te detienes cuando los factores se juntan o se cruzan. Así, para 48: 1 × 48, 2 × 24, 3 × 16, 4 × 12 y 6 × 8. Después del 6 aparece el 8, que ya está.",
        "Los criterios de divisibilidad dicen si un número se divide sin hacer la división. Por 2: termina en cifra par. Por 5: termina en 0 o en 5. Por 10: termina en 0. Por 3: la suma de sus cifras es múltiplo de 3. Por 9: la suma de sus cifras es múltiplo de 9. Por 6: se divide por 2 y por 3 a la vez.",
        "Un factor común de dos números es un factor que aparece en la lista de los dos. Para hallarlo, escribe los factores de cada número y busca los repetidos. Si necesitas saber cuántos números de una lista son múltiplos de otro, cuenta con la tabla de ese número y detente cuando pases el límite.",
    ],
    vocab=[("pareja de factores", "dos números que multiplicados dan el número"), ("factor común", "factor que aparece en la lista de factores de dos o más números"), ("divisible por 9", "número cuyas cifras suman un múltiplo de 9"), ("divisible por 6", "número que se divide por 2 y por 3 a la vez"), ("múltiplo común", "número que es múltiplo de dos o más números a la vez")],
    worked=[
        W("Factores por parejas", "Encuentra todos los factores de 48.", ["Pruebo en orden: 1 × 48, 2 × 24, 3 × 16, 4 × 12. El 5 no divide a 48.", "6 × 8 = 48. Después del 6 viene el 8, que ya apareció, así que termino.", "Ordeno los números de las parejas."], "1, 2, 3, 4, 6, 8, 12, 16, 24 y 48"),
        W("Criterio de divisibilidad", "¿72 es divisible por 9?", ["Sumo las cifras: 7 + 2 = 9.", "9 es múltiplo de 9, entonces 72 se divide por 9 sin resto."], "Sí, 72 = 9 × 8"),
    ],
    mistakes=[
        M("Decir que 78 es divisible por 9 porque 7 + 8 = 15 es múltiplo de 3.", "Se usó el criterio del 3 en vez del criterio del 9.", "Para el 9 la suma debe ser múltiplo de 9. 15 no lo es; 78 solo se divide por 3."),
        M("Decir que todo número que termina en 4 es múltiplo de 4.", "Se miró solo la última cifra.", "14 termina en 4 y 4 × 3 = 12, 4 × 4 = 16: no es múltiplo de 4."),
    ],
    rec=[
        ex("¿135 es divisible por 5? Responde sí o no.", "Sí", "Termina en 5."),
        ex("Las parejas de 30 son 1 × 30, 2 × 15, 3 × 10 y 5 × 6. ¿Cuántos factores tiene 30?", "8", "Cada pareja aporta dos factores distintos: 4 × 2 = 8."),
        ex("Las cifras de 84 suman 12. ¿84 es divisible por 3? Responde sí o no.", "Sí", "12 es múltiplo de 3."),
    ],
    und=[
        ex("¿Cuáles de 45, 52, 70 y 81 son divisibles por 3?", "45 y 81", "45: 4 + 5 = 9 y 81: 8 + 1 = 9 son múltiplos de 3; 52 suma 7 y 70 suma 7."),
        ex("Escribe todos los factores de 40, de menor a mayor.", "1, 2, 4, 5, 8, 10, 20 y 40", "Parejas: 1 × 40, 2 × 20, 4 × 10 y 5 × 8; el 3, el 6 y el 7 no dividen a 40."),
        ex("De 50, 54, 56 y 63, ¿cuál es múltiplo de 6?", "54", "54 es par y sus cifras suman 9, múltiplo de 3; 50, 56 y 63 no cumplen las dos condiciones."),
    ],
    app=[
        ex("Escribe los factores comunes de 12 y 18.", "1, 2, 3 y 6", "Factores de 12: 1, 2, 3, 4, 6, 12. Factores de 18: 1, 2, 3, 6, 9, 18. Repetidos: 1, 2, 3 y 6."),
        ex("¿Cuántos números del 1 al 50 son múltiplos de 2 y de 5 a la vez?", "5", "Son los múltiplos de 10: 10, 20, 30, 40 y 50."),
        ex("Hay 54 galletas para poner en bandejas con la misma cantidad en cada una, sin que sobren. Cada bandeja lleva más de 2 galletas y menos de 20. ¿Cuántas cantidades distintas son posibles?", "4", "Los factores de 54 son 1, 2, 3, 6, 9, 18, 27 y 54; entre 3 y 19 quedan 3, 6, 9 y 18."),
    ],
    rea=[
        ex("Ana dice que 14 es múltiplo de 4 porque termina en 4. ¿Tiene razón?", "No", "4 × 3 = 12 y 4 × 4 = 16, 14 queda entre medio."),
        ex("Tito dice que 78 es divisible por 9 porque sus cifras suman 15, múltiplo de 3. ¿Tiene razón?", "No", "Para el 9 la suma debe ser múltiplo de 9; 9 × 8 = 72 y 9 × 9 = 81, no 78."),
    ],
    cha=[
        ex("Un número menor que 40, de dos cifras, es divisible por 2, por 3 y por 5 a la vez. ¿Cuál es?", "30", "Debe ser múltiplo de 30 y el único de dos cifras menor que 40 es 30."),
        ex("¿Cuál es el menor número de dos cifras que tiene exactamente 3 factores?", "25", "Sus factores son 1, 5 y 25; 9 tiene tres factores pero solo una cifra."),
    ],
    ctx=[ex("En un acto hay 72 estudiantes que forman filas con la misma cantidad en cada una. Cada fila debe tener entre 5 y 10 estudiantes, incluidos 5 y 10. ¿Cuántas cantidades distintas por fila sirven?", "3", "Los factores de 72 entre 5 y 10 son 6, 8 y 9.")],
    sc=[
        ex("¿210 es divisible por 10? Responde sí o no.", "Sí", "Termina en 0."),
        ex("¿Cuántos factores tiene 44?", "6", "1, 2, 4, 11, 22 y 44."),
        ex("¿111 es divisible por 3? Responde sí o no.", "Sí", "1 + 1 + 1 = 3, que es múltiplo de 3."),
    ],
    op=task(
        "Con el número 60, escribe todos sus factores usando parejas. Después anota, con el criterio de divisibilidad, si 60 se divide por 2, 3, 5, 9 y 10.",
        "Parejas: 1×60, 2×30, 3×20, 4×15, 5×12, 6×10. Se divide por 2 (par), por 3 (6+0=6), por 5 y por 10 (termina en 0), pero no por 9 (6 no es múltiplo de 9).",
        ["lista completa de factores", "usa parejas", "aplica bien los cinco criterios"],
        ["parejas escritas", "tabla de criterios con sí o no"],
        ["olvidar factores", "confundir los criterios del 3 y del 9"],
        "Pide que compruebe que cada pareja multiplicada da 60 y que cuente 12 factores.",
    ),
    reinforce="Con parejas, escribe los factores de 32 y los de 28. Luego marca los factores comunes.",
    extend="Busca un número menor que 100 que sea divisible por 2, 3, 5 y 9 a la vez. Explica con los criterios por qué sirve y si hay otro menor que 100.",
)

# ------------------------------------------------------------------ OA 01 clase 4
lesson(
    OA1, 4,
    use="Aprenderé a resolver problemas en que algo se repite cada cierto tiempo, usando múltiplos. Sirve para saber cuándo coinciden dos horarios o ciclos.",
    prior=["Sé listar múltiplos de un número.", "Sé reconocer un múltiplo común."],
    explain=[
        "Muchos problemas hablan de cosas que ocurren cada cierto tiempo: un bus que pasa cada 15 minutos o una luz que se enciende cada 4 segundos. Los momentos en que ocurren son los múltiplos de ese número. Si un bus pasa cada 15 minutos, pasa a los 15, 30, 45, 60… minutos.",
        "Para saber cuándo coinciden dos ciclos, escribe los múltiplos de cada número y busca los que se repiten. Esos son los múltiplos comunes. El menor de ellos indica la primera vez que coinciden. Si una luz parpadea cada 3 segundos y otra cada 5, los múltiplos de 3 son 3, 6, 9, 12, 15… y los de 5 son 5, 10, 15… Se juntan por primera vez a los 15 segundos.",
        "Después de la primera coincidencia, vuelven a coincidir en los siguientes múltiplos comunes. En el ejemplo, a los 15, 30, 45 segundos. No basta multiplicar los dos números: 4 y 6 no coinciden a los 24 segundos por primera vez, sino a los 12. Siempre conviene comprobar con las listas.",
    ],
    vocab=[("ciclo", "algo que se repite cada cierto tiempo"), ("múltiplo común", "número que es múltiplo de dos o más números a la vez"), ("coincidir", "ocurrir al mismo tiempo"), ("menor múltiplo común", "el primero de los múltiplos comunes, distinto de cero"), ("intervalo", "tiempo que pasa entre un suceso y el siguiente")],
    worked=[
        W("Dos luces que coinciden", "Una luz se enciende cada 3 segundos y otra cada 5 segundos. Se encienden juntas ahora. ¿Cuándo coinciden por primera vez?", ["Múltiplos de 3: 3, 6, 9, 12, 15, 18…", "Múltiplos de 5: 5, 10, 15, 20…", "El primer número que está en las dos listas es 15."], "A los 15 segundos"),
        W("Dos buses que salen juntos", "Un bus sale cada 9 minutos y otro cada 12 minutos. Salen juntos a las 10:00. ¿A qué hora vuelven a salir juntos?", ["Múltiplos de 9: 9, 18, 27, 36, 45…", "Múltiplos de 12: 12, 24, 36, 48…", "Se juntan a los 36 minutos: 10:00 + 36 min = 10:36."], "A las 10:36"),
    ],
    mistakes=[
        M("Decir que ciclos de 4 y 6 segundos coinciden a los 24 s porque 4 × 6 = 24.", "Se multiplicó sin buscar un múltiplo común menor.", "Múltiplos de 4: 4, 8, 12. Múltiplos de 6: 6, 12. Coinciden a los 12 s."),
        M("Contar desde el intervalo en vez de desde el momento inicial.", "Se olvidó sumar el intervalo al momento en que empezaron juntos.", "Calcula el tiempo transcurrido con múltiplos y súmalo a la hora de partida."),
    ],
    rec=[
        ex("Escribe los cuatro primeros múltiplos de 5.", "5, 10, 15 y 20", "5 × 1, 5 × 2, 5 × 3 y 5 × 4."),
        ex("Los múltiplos de 3 hasta 15 son 3, 6, 9, 12 y 15. Los de 5 hasta 15 son 5, 10 y 15. ¿Qué número aparece en las dos listas?", "15", "Es el único que está en las dos."),
        ex("Un reloj despertador suena cada 7 minutos. Suena por primera vez a los 7 minutos de ponerlo. ¿A los cuántos minutos suena por quinta vez?", "35", "Quinto múltiplo de 7: 7 × 5 = 35."),
    ],
    und=[
        ex("¿Cuál es el menor múltiplo común de 6 y 9?", "18", "Múltiplos de 6: 6, 12, 18. Múltiplos de 9: 9, 18."),
        ex("¿Cuál es el menor múltiplo común de 4 y 10?", "20", "Múltiplos de 4: 4, 8, 12, 16, 20. Múltiplos de 10: 10, 20."),
        ex("¿Cuántos múltiplos de 15 hay entre 1 y 100?", "6", "Son 15, 30, 45, 60, 75 y 90."),
    ],
    app=[
        ex("Un faro destella cada 10 segundos y otro cada 15 segundos. Destellan juntos ahora. ¿Dentro de cuántos segundos vuelven a destellar juntos?", "30", "Múltiplos de 10: 10, 20, 30. Múltiplos de 15: 15, 30."),
        ex("Marta va a la piscina cada 4 días y Luis cada 6 días. Hoy coinciden. ¿Dentro de cuántos días vuelven a coincidir?", "12", "Múltiplos de 4: 4, 8, 12. Múltiplos de 6: 6, 12."),
        ex("Un tren sale cada 14 minutos y otro cada 21 minutos. Salen juntos a las 8:00. ¿A qué hora vuelven a salir juntos?", "8:42", "Múltiplos de 14: 14, 28, 42. Múltiplos de 21: 21, 42. Pasan 42 minutos."),
    ],
    rea=[
        ex("Juan dice que dos luces, una cada 4 segundos y otra cada 6, coinciden primero a los 24 segundos porque 4 × 6 = 24. ¿Cuándo coinciden realmente por primera vez?", "A los 12 segundos", "12 es múltiplo de 4 y de 6 y es menor que 24."),
        ex("Ana dice: «si dos sucesos coinciden cada 20 días, también coinciden a los 60 días». ¿Es verdadero?", "Sí", "60 = 20 × 3, es múltiplo de 20, así que coincide en ese momento."),
    ],
    cha=[
        ex("Tres luces destellan cada 2, 3 y 5 segundos. Destellan juntas ahora. ¿Cuántos segundos pasan hasta que vuelven a destellar las tres juntas?", "30", "Es el menor número que es múltiplo de 2, 3 y 5: 30."),
        ex("¿Cuántos números del 1 al 100 son múltiplos de 6 y de 8 a la vez?", "4", "El menor múltiplo común es 24; entonces 24, 48, 72 y 96."),
    ],
    ctx=[ex("En una feria ficticia suena una campana cada 8 minutos y otra cada 12 minutos. A las 15:00 suenan juntas. ¿A qué hora vuelven a sonar juntas por segunda vez después de las 15:00?", "15:48", "Coinciden cada 24 minutos, es decir a los 24 y a los 48 minutos; la segunda vez es 15:48.")],
    sc=[
        ex("¿Cuál es el menor múltiplo común de 3 y 7?", "21", "3 × 7 = 21 y ninguno menor está en ambas tablas."),
        ex("¿Cuántos múltiplos de 9 hay entre 1 y 50?", "5", "Son 9, 18, 27, 36 y 45."),
        ex("¿Cuál es el primer número mayor que 0 que es múltiplo de 4 y de 5?", "20", "Múltiplos de 5: 5, 10, 15, 20; el primero en la tabla del 4 es 20."),
    ],
    op=task(
        "En una plaza ficticia, una fuente cambia de color cada 6 segundos y un letrero parpadea cada 8 segundos. Empiezan juntos. Escribe los múltiplos de 6 y de 8 hasta 48, marca los que coinciden y explica cuándo se vuelven a juntar.",
        "Múltiplos de 6: 6, 12, 18, 24, 30, 36, 42, 48. Múltiplos de 8: 8, 16, 24, 32, 40, 48. Coinciden en 24 y 48. La primera vez es a los 24 segundos.",
        ["lista completa de múltiplos", "identifica los comunes", "responde con unidad"],
        ["listas escritas", "frase con la respuesta y los segundos"],
        ["multiplicar 6 × 8 sin comprobar", "olvidar la segunda coincidencia"],
        "Pide que compruebe que 24 se divide exactamente por 6 y por 8.",
    ),
    reinforce="Escribe los múltiplos de 4 y de 6 hasta 36 y marca los que se repiten. ¿Cuál es el primero?",
    extend="Inventa y resuelve un problema de dos buses con intervalos distintos, menores que 30 minutos, y busca cuándo vuelven a salir juntos. Escribe las listas de múltiplos.",
)

# ================================================================== OA 02
OA2 = "MA06 OA 02"

# ------------------------------------------------------------------ OA 02 clase 1
lesson(
    OA2, 1,
    use="Aprenderé el orden en que se hacen las operaciones cuando hay varias en un mismo cálculo. Sirve para que todas las personas lleguen al mismo resultado.",
    prior=["Sé sumar, restar, multiplicar y dividir números naturales.", "Sé qué significa un paréntesis."],
    explain=[
        "Cuando un cálculo tiene varias operaciones, hay un orden para resolverlas. Primero se hace lo que está dentro de los paréntesis. Después se hacen las multiplicaciones y las divisiones, de izquierda a derecha. Al final se hacen las sumas y las restas, también de izquierda a derecha.",
        "Por eso 8 + 6 × 3 no es 42, sino 26: primero se multiplica 6 × 3 = 18 y luego se suma 8 + 18. Si quieres sumar primero, debes usar paréntesis: (8 + 6) × 3 = 42. Los paréntesis cambian el orden normal y por eso son tan importantes.",
        "Cuando hay solo sumas y restas, o solo multiplicaciones y divisiones, se avanza de izquierda a derecha. Por ejemplo, 20 − 5 − 3 es 15 − 3 = 12, y no 20 − 2 = 18. Anotar el resultado de cada paso hacia abajo, sin saltarte nada, ayuda a no equivocarte.",
    ],
    vocab=[("operación combinada", "cálculo con dos o más operaciones distintas"), ("paréntesis", "signos ( ) que indican qué se calcula primero"), ("jerarquía", "orden de importancia con que se resuelven las operaciones"), ("expresión", "cálculo escrito con números y signos de operación"), ("de izquierda a derecha", "orden en que se resuelven operaciones del mismo nivel")],
    worked=[
        W("Multiplicar antes de sumar", "Calcula 8 + 6 × 3 y (8 + 6) × 3.", ["En la primera, primero 6 × 3 = 18; luego 8 + 18 = 26.", "En la segunda, primero el paréntesis: 8 + 6 = 14; luego 14 × 3 = 42."], "26 y 42"),
        W("Varias operaciones", "Calcula 40 − 12 ÷ 4 + 5.", ["Primero la división: 12 ÷ 4 = 3, y queda 40 − 3 + 5.", "Resto y sumo de izquierda a derecha: 40 − 3 = 37 y 37 + 5 = 42."], "42"),
    ],
    mistakes=[
        M("Calcular 5 + 4 × 2 como 9 × 2 = 18.", "Se fue de izquierda a derecha sin respetar que se multiplica primero.", "4 × 2 = 8 y luego 5 + 8 = 13."),
        M("Calcular 20 − 5 − 3 como 20 − 2 = 18.", "Se restó 5 − 3 antes de tiempo.", "Se avanza de izquierda a derecha: 20 − 5 = 15 y 15 − 3 = 12."),
    ],
    rec=[
        arith("Calcula 3 + 2 × 5.", "3+2*5", "Primero se multiplica 2 × 5 y luego se suma 3."),
        arith("Calcula 30 − 4 × 3.", "30-4*3", "Primero se multiplica 4 × 3 y luego se resta."),
        ex("En el cálculo 7 + 9 ÷ 3, ¿qué operación se hace primero?", "La división", "Las divisiones se hacen antes que las sumas."),
    ],
    und=[
        arith("Calcula (4 + 6) × 7.", "(4+6)*7", "Primero el paréntesis: 4 + 6 = 10."),
        arith("Calcula 48 ÷ 6 + 2 × 5.", "48//6+2*5", "Se hacen la división y la multiplicación y luego se suma."),
        arith("Calcula 50 − 12 − 8.", "50-12-8", "Solo hay restas: se avanza de izquierda a derecha."),
    ],
    app=[
        arith("Calcula 100 − 5 × (12 − 2).", "100-5*(12-2)", "Primero el paréntesis, luego la multiplicación y al final la resta."),
        arith("Ana compra 3 cuadernos de $1.500 y 4 lápices de $800. ¿Cuántos pesos gasta en total?", "3*1500+4*800", "Se multiplica cada compra y después se suman."),
        arith("Se reparten 2.400 stickers en partes iguales entre 6 niños y 2 niñas. ¿Cuántos stickers recibe cada uno?", "2400//(6+2)", "Primero se calcula cuántos son entre todos: 6 + 2 = 8."),
    ],
    rea=[
        ex("Pedro calculó 12 + 8 ÷ 4 = 5. ¿Cuál es el resultado correcto?", "14", "Primero 8 ÷ 4 = 2 y luego 12 + 2 = 14; Pedro sumó antes de dividir."),
        ex("Luisa dice que 6 + 2 × 5 y (6 + 2) × 5 dan lo mismo. ¿Tiene razón?", "No", "La primera da 16 y la segunda da 40; el paréntesis cambia el orden."),
    ],
    cha=[
        ex("Pon paréntesis en 2 + 3 × 4 + 1 para que el resultado sea 25.", "(2 + 3) × (4 + 1)", "(2 + 3) = 5 y (4 + 1) = 5, y 5 × 5 = 25; con otros paréntesis no resulta 25."),
        arith("Calcula 6 + 6 ÷ 6 × 6 − 6.", "6+6//6*6-6", "6 ÷ 6 = 1, luego 1 × 6 = 6, y queda 6 + 6 − 6."),
    ],
    ctx=[arith("Una pastelería hace 5 bandejas con 12 galletas y 3 bandejas con 8 galletas. Si vende 20 galletas, ¿cuántas quedan?", "5*12+3*8-20", "Se calculan las galletas de cada tipo de bandeja, se suman y se resta lo vendido.")],
    sc=[
        arith("Calcula 9 + 3 × 4.", "9+3*4", "Primero la multiplicación."),
        arith("Calcula (9 + 3) × 4.", "(9+3)*4", "Primero el paréntesis."),
        arith("Calcula 36 ÷ 4 − 2.", "36//4-2", "Primero la división y después la resta."),
    ],
    op=task(
        "Resuelve estos cálculos y escribe cada paso: 15 + 5 × 4, (15 + 5) × 4 y 60 ÷ 5 − 3 × 2. Luego explica con una frase por qué los dos primeros dan resultados distintos.",
        "15 + 5 × 4 = 15 + 20 = 35. (15 + 5) × 4 = 20 × 4 = 80. 60 ÷ 5 − 3 × 2 = 12 − 6 = 6. Cambian porque el paréntesis hace que la suma se haga primero.",
        ["respeta la jerarquía", "escribe los pasos", "explica el efecto del paréntesis"],
        ["tres cálculos con pasos", "frase de explicación"],
        ["calcular siempre de izquierda a derecha", "ignorar los paréntesis"],
        "Pide que subraye en cada cálculo la operación que hace primero y que compruebe por partes.",
    ),
    reinforce="Calcula 10 + 2 × 6, (10 + 2) × 6 y 10 + 12 ÷ 6. Escribe cada paso hacia abajo.",
    extend="Con los números 2, 3, 4 y 5 usa cada uno una vez y cualquier operación o paréntesis para obtener el resultado 14. Escribe tu expresión y compruébala.",
)

# ------------------------------------------------------------------ OA 02 clase 2
lesson(
    OA2, 2,
    use="Aprenderé a escribir una expresión que represente un problema y a calcularla con el orden correcto. Sirve para resolver problemas de varios pasos sin perderse.",
    prior=["Sé el orden de las operaciones y el uso de paréntesis.", "Sé leer problemas con las cuatro operaciones."],
    explain=[
        "Un problema de varios pasos se puede escribir en una sola expresión. Primero lees la historia y decides qué se junta, qué se quita, qué se repite y qué se reparte. Luego traduces cada parte a una operación: «más» o «agregar» es una suma, «menos» o «quitar» es una resta, «veces» o «cada uno» es una multiplicación y «entre» es una división.",
        "Los paréntesis sirven para agrupar lo que debe calcularse junto antes de seguir. «El doble de la suma de 5 y 3» se escribe 2 × (5 + 3). Si escribieras 2 × 5 + 3 estarías diciendo «el doble de 5, más 3», que es otra cosa. Siempre lee la expresión en voz alta para ver si cuenta la misma historia.",
        "Después de calcular, comprueba que la respuesta tiene sentido: un vuelto no puede ser mayor que lo que pagaste. Escribe la respuesta con la unidad, como pesos o personas. Calcular bien no sirve si la expresión cuenta otra historia.",
    ],
    vocab=[("expresión", "cálculo escrito con números y signos"), ("agrupar", "poner juntos con un paréntesis lo que se calcula primero"), ("doble", "dos veces una cantidad"), ("triple", "tres veces una cantidad"), ("vuelto", "dinero que se devuelve al pagar con más de lo que cuesta")],
    worked=[
        W("Vuelto de una compra", "Compré 3 pares de calcetines de $2.500 cada uno y pagué con un billete de $10.000. ¿Cuánto me devolvieron?", ["Lo gastado es 3 × 2.500.", "El vuelto es lo que pagué menos lo gastado: 10.000 − 3 × 2.500.", "Calculo: 3 × 2.500 = 7.500 y 10.000 − 7.500 = 2.500."], "$2.500"),
        W("Pagar entre varios", "Cuatro amigos pagan en partes iguales una cuenta de $12.000 más $2.000 de propina. ¿Cuánto pone cada uno?", ["Primero se junta todo lo que se debe pagar: 12.000 + 2.000, y eso va entre paréntesis.", "Expresión: (12.000 + 2.000) ÷ 4.", "14.000 ÷ 4 = 3.500."], "$3.500"),
    ],
    mistakes=[
        M("Escribir 2 × 5 + 3 para «el doble de la suma de 5 y 3».", "Falta el paréntesis, así que el doble solo se aplica al 5.", "Se escribe 2 × (5 + 3) = 16."),
        M("Escribir 12.000 + 2.000 ÷ 4 para repartir cuenta y propina entre 4.", "La división solo afecta a la propina.", "Escribe (12.000 + 2.000) ÷ 4."),
    ],
    rec=[
        arith("Calcula «el doble de 7, más 3», es decir 2 × 7 + 3.", "2*7+3", "Primero la multiplicación y luego la suma."),
        arith("Calcula «la mitad de 18, menos 4», es decir 18 ÷ 2 − 4.", "18//2-4", "Primero la división y después la resta."),
        ex("¿Qué expresión representa «suma 5 y 3 y multiplica el resultado por 2»: 5 + 3 × 2 o (5 + 3) × 2?", "(5 + 3) × 2", "La suma debe hacerse primero, por eso necesita paréntesis."),
    ],
    und=[
        arith("Hay 5 cajas con 24 lápices cada una y 16 lápices sueltos. ¿Cuántos lápices hay en total?", "5*24+16", "Se multiplica y luego se suman los sueltos."),
        arith("Calcula «el triple de la suma de 4 y 6».", "3*(4+6)", "Primero la suma dentro del paréntesis y luego el triple."),
        arith("Calcula «a 90 le resto el producto de 7 y 8» (el producto es el resultado de multiplicar).", "90-7*8", "El producto es 7 × 8 y se resta de 90."),
    ],
    app=[
        arith("Carolina tiene $20.000 y compra 2 polleras de $7.500 cada una. ¿Cuántos pesos le sobran?", "20000-2*7500", "Se calcula el gasto y se resta del dinero que tenía."),
        arith("En un bus iban 45 pasajeros. En una parada bajan 12 y suben 8, y en la siguiente bajan 15. ¿Cuántos pasajeros quedan?", "45-12+8-15", "Se avanza de izquierda a derecha restando y sumando."),
        arith("Seis amigos pagan en partes iguales $18.000 de pizzas y $6.000 de bebidas. ¿Cuánto paga cada uno?", "(18000+6000)//6", "Primero se junta todo lo que se debe pagar."),
    ],
    rea=[
        ex("Ema escribió 2 × 5 + 3 para «el doble de la suma de 5 y 3». ¿Cuál es la expresión correcta?", "2 × (5 + 3)", "Falta el paréntesis: la suma debe hacerse antes del doble. Da 16 y no 13."),
        ex("¿Las expresiones 4 × 900 + 1.200 y (4 + 1) × 900 dan el mismo total? Responde sí o no.", "No", "La primera da 4.800 y la segunda 4.500; no cuentan la misma historia."),
    ],
    cha=[
        arith("Un estadio tiene 4 sectores de 2.500 asientos y 2 sectores de 1.800 asientos. Si hay 3.250 asientos ocupados, ¿cuántos están libres?", "4*2500+2*1800-3250", "Total de asientos menos los ocupados."),
        arith("Calcula 100 − (30 + 6 × 5) ÷ 2.", "100-(30+6*5)//2", "Dentro del paréntesis primero 6 × 5; luego se divide y al final se resta."),
    ],
    ctx=[arith("Una familia compra 2 entradas de adulto a $4.500 y 3 de niño a $2.800. Paga con $20.000. ¿Cuánto vuelto recibe?", "20000-(2*4500+3*2800)", "El vuelto es lo pagado menos el gasto total de las entradas.")],
    sc=[
        arith("A 50 le sumo el doble de 6. ¿Cuánto resulta?", "50+2*6", "El doble de 6 se calcula antes de sumar."),
        arith("Calcula «la mitad de la suma de 14 y 10».", "(14+10)//2", "La suma va primero, entre paréntesis."),
        arith("Calcula 7 × (10 − 4).", "7*(10-4)", "Primero el paréntesis."),
    ],
    op=task(
        "Lee este problema: «En una librería hay 6 estantes con 15 libros cada uno. Se venden 28 libros y llegan 40 libros nuevos». Escribe una sola expresión que cuente cuántos libros hay al final, calcúlala y explica en una frase qué representa cada parte.",
        "Expresión: 6 × 15 − 28 + 40 = 90 − 28 + 40 = 102. 6 × 15 son los libros de los estantes, 28 los vendidos y 40 los que llegan.",
        ["expresión coherente con el problema", "cálculo con el orden correcto", "explica cada parte"],
        ["expresión escrita", "cálculo con pasos y respuesta"],
        ["olvidar un paréntesis", "restar en vez de sumar un dato"],
        "Pide que lea la expresión en voz alta y compruebe que cuenta la misma historia del problema.",
    ),
    reinforce="Escribe una expresión para: «3 bolsas de 12 caramelos y 5 caramelos más». Calcúlala y comprueba el resultado contando por grupos.",
    extend="Inventa un problema de compra con dos productos y un vuelto. Escribe la expresión con paréntesis y resuélvelo.",
)

# ------------------------------------------------------------------ OA 02 clase 3
lesson(
    OA2, 3,
    use="Aprenderé a usar la calculadora con números mayores que 10.000 y a comprobar el resultado con una estimación. Sirve para calcular rápido sin dejar pasar errores.",
    prior=["Sé el orden de las operaciones.", "Sé redondear números a la decena, centena o unidad de mil."],
    explain=[
        "Con números grandes, como 12.480 × 25, la calculadora ahorra tiempo, pero no piensa por ti. Antes de calcular, estima: redondea los números y haz el cálculo mental. 12.480 es casi 12.000 y 12.000 × 25 = 300.000. Así sabrás más o menos cuánto debe dar y te darás cuenta si digitaste algo mal.",
        "Algunas calculadoras sencillas hacen las operaciones en el orden en que las digitas, sin respetar que se multiplica antes de sumar. Si tecleas 2 + 3 × 4, una calculadora simple puede mostrar 20, pero el resultado correcto es 14. Para evitarlo, calcula las multiplicaciones por separado, anota el resultado y luego suma. Si tu calculadora tiene paréntesis, úsalos.",
        "Para un cálculo largo, divídelo en partes. Anota cada resultado parcial en el cuaderno, como se hizo antes. Al final compara tu respuesta con la estimación: si son parecidas, probablemente está bien. Si son muy distintas, vuelve a revisar los datos que digitaste y el orden de las operaciones.",
    ],
    vocab=[("estimar", "calcular un resultado aproximado, con números redondeados"), ("redondear", "cambiar un número por otro cercano más fácil de calcular"), ("resultado parcial", "resultado de una parte del cálculo"), ("calculadora", "aparato que hace operaciones con números"), ("razonable", "que tiene sentido comparado con la estimación")],
    worked=[
        W("Calcular con partes y estimar", "Calcula 12.480 × 25 + 3.600 ÷ 12.", ["Estimo: 12.000 × 25 = 300.000.", "Calculo por partes: 12.480 × 25 = 312.000 y 3.600 ÷ 12 = 300.", "Sumo: 312.000 + 300 = 312.300, que se parece a la estimación."], "312.300"),
        W("Restas encadenadas", "Calcula 154.200 − 48.750 − 32.480.", ["Estimo: 154.000 − 49.000 − 32.000 = 73.000.", "154.200 − 48.750 = 105.450.", "105.450 − 32.480 = 72.970, cercano a lo estimado."], "72.970"),
    ],
    mistakes=[
        M("Aceptar el resultado de la calculadora sin mirarlo, aunque 19.800 × 5 haya dado 9.900.", "No se estimó antes: 20.000 × 5 es 100.000.", "Estima antes y revisa si el resultado se parece."),
        M("Digitar 2 + 3 × 4 en una calculadora simple y aceptar 20.", "La calculadora hizo las operaciones en el orden digitado.", "Multiplica primero 3 × 4 = 12 y luego suma 2 + 12 = 14."),
    ],
    rec=[
        arith("Calcula 25.000 + 17.300.", "25000+17300", "Se suman unidades de mil y centenas con cuidado."),
        arith("Calcula 18.400 − 9.750.", "18400-9750", "Es una resta de números grandes."),
        ex("Estima 19.800 + 30.100 redondeando a las unidades de mil.", "50.000", "20.000 + 30.000 = 50.000."),
    ],
    und=[
        arith("Calcula 4.250 × 36.", "4250*36", "Multiplicación de un número de 4 cifras por uno de 2 cifras."),
        arith("Calcula 96.000 ÷ 32.", "96000//32", "División exacta de un número grande."),
        ex("Estima 4.870 × 21 redondeando 4.870 a 5.000 y 21 a 20.", "100.000", "5.000 × 20 = 100.000."),
    ],
    app=[
        arith("Un colegio recoge $13.500 por curso en 8 cursos y ya tenía $24.900. ¿Cuánto dinero tiene en total?", "13500*8+24900", "Primero se multiplica y después se suma lo que ya tenía."),
        arith("Un club tenía $250.000 y compró 9 balones de $12.500 cada uno. ¿Cuánto dinero le queda?", "250000-12500*9", "Se calcula el gasto en balones y se resta."),
        arith("Calcula 86.400 ÷ 12 + 5.150 × 4.", "86400//12+5150*4", "Se hacen la división y la multiplicación y luego se suma."),
    ],
    rea=[
        ex("Una calculadora simple muestra 20 al digitar 2 + 3 × 4 de izquierda a derecha. ¿Cuál es el resultado correcto del cálculo?", "14", "Primero 3 × 4 = 12 y luego 2 + 12 = 14; la calculadora sumó antes de multiplicar."),
        ex("Rosa calculó 19.800 × 5 y le dio 9.900. ¿Es un resultado razonable? Responde sí o no.", "No", "20.000 × 5 es 100.000; el valor correcto es 99.000."),
    ],
    cha=[
        arith("Calcula 125 × 8 × 12 × 5.", "125*8*12*5", "125 × 8 = 1.000; luego × 12 = 12.000 y × 5 = 60.000."),
        arith("Se calculan (15.000 + 3.000) × 4 y 15.000 + 3.000 × 4. ¿Cuál es el mayor de los dos resultados?", "(15000+3000)*4", "El primero da 72.000 y el segundo 27.000; el mayor es el que tiene paréntesis."),
    ],
    ctx=[arith("Una fábrica ficticia produce 1.250 botellas por hora durante 14 horas y descarta 1.875 por fallas. ¿Cuántas botellas buenas quedan?", "1250*14-1875", "Se multiplican las botellas por hora por las horas y se restan las descartadas.")],
    sc=[
        arith("Calcula 20.000 − 7.350.", "20000-7350", "Resta de números grandes."),
        arith("Calcula 8.200 × 15.", "8200*15", "Producto de un número de 4 cifras por uno de 2 cifras."),
        ex("Estima 48.700 + 31.200 redondeando a las decenas de mil.", "80.000", "50.000 + 30.000 = 80.000."),
    ],
    op=task(
        "Una librería ficticia vendió 1.480 libros a $9.500 cada uno y gastó $4.200.000 en arriendo y sueldos. Estima primero cuánto ganó, calcula después con la calculadora (ventas menos gastos) y compara tu estimación con el resultado.",
        "Estimación: 1.500 × 10.000 = 15.000.000 de ventas y menos 4.000.000 son unos 11.000.000. Cálculo: 1.480 × 9.500 = 14.060.000 y menos 4.200.000 son 9.860.000. Son valores cercanos, el cálculo es razonable.",
        ["estima antes de calcular", "calcula con el orden correcto", "compara estimación y resultado"],
        ["estimación escrita", "cálculo con resultados parciales", "frase de comparación"],
        ["no estimar", "no anotar el cálculo parcial"],
        "Pide que explique por qué el resultado de la calculadora tiene sentido a partir de la estimación.",
    ),
    reinforce="Estima y luego calcula 6.200 × 18. Escribe la estimación, el cálculo exacto y si se parecen.",
    extend="Inventa un cálculo con dos operaciones donde una calculadora simple dé un resultado distinto del correcto. Muestra los dos resultados y explica por qué.",
)

# ------------------------------------------------------------------ OA 02 clase 4
lesson(
    OA2, 4,
    use="Aprenderé a resolver problemas de varios pasos con las cuatro operaciones, a interpretar el resto de una división y a detectar datos que sobran. Sirve para decidir bien en situaciones reales.",
    prior=["Sé escribir expresiones para problemas.", "Sé dividir con resto y usar la calculadora con estimación."],
    explain=[
        "En un problema de varios pasos, primero lee todo y subraya la pregunta. Luego decide qué pasos necesitas. A veces hay un dato que sobra, como el precio de un libro cuando la pregunta es cuántas páginas se leyeron. No todo número del problema se usa.",
        "Al dividir, a veces sobra algo. El resto se interpreta según la historia. Si reparto 2.350 personas en buses de 48 asientos, 2.350 ÷ 48 da 48 y sobran 46 personas. Esas 46 personas también necesitan bus, así que se necesita uno más: 49 buses. Si reparto objetos en cajas completas, el resto son los que no alcanzan para otra caja.",
        "Por eso la respuesta no siempre es el cociente. A veces hay que sumar 1 al cociente, a veces se usa solo el cociente y a veces la respuesta es el resto. Después de decidir, vuelve a la pregunta y escribe la respuesta con su unidad.",
    ],
    vocab=[("cociente", "resultado de una división"), ("resto", "lo que sobra al dividir"), ("dato que sobra", "número del problema que no se necesita para responder"), ("pasos", "cálculos que se hacen uno después de otro para llegar a la respuesta"), ("interpretar", "decidir qué significa un resultado en la historia")],
    worked=[
        W("Interpretar el resto", "Se quiere transportar a 2.350 personas en buses de 48 asientos. ¿Cuántos buses se necesitan?", ["Divido 2.350 ÷ 48: 48 × 48 = 2.304 y sobran 46.", "Las 46 personas que sobran también necesitan un bus.", "Se necesitan 48 + 1 buses."], "49 buses"),
        W("Problema de varios pasos", "Una empresa gana $12.600 por hora. Trabaja 8 horas al día durante 5 días y paga $150.000 en gastos. ¿Cuánto le queda?", ["Horas trabajadas: 8 × 5 = 40.", "Ganancia: 12.600 × 40 = 504.000.", "Queda 504.000 − 150.000 = 354.000."], "$354.000"),
    ],
    mistakes=[
        M("Responder 12 mesas para 100 personas en mesas de 8 porque 100 ÷ 8 = 12 con resto 4.", "Se ignoró el resto: 4 personas quedan sin mesa.", "Se necesita una mesa más: 13 mesas."),
        M("Usar todos los datos del problema aunque uno no sirva.", "Se creyó que cada número debe entrar en el cálculo.", "Decide qué dato responde la pregunta y deja los demás."),
    ],
    rec=[
        arith("Calcula 480 ÷ 24.", "480//24", "División exacta."),
        ex("Se reparten 50 láminas en grupos de 8. ¿Cuántos grupos completos se forman y cuántas láminas sobran?", "6 grupos y sobran 2", "8 × 6 = 48 y 50 − 48 = 2."),
        arith("Calcula 7 × 9 + 5.", "7*9+5", "Primero la multiplicación y luego la suma."),
    ],
    und=[
        ex("Hay 150 huevos y cada caja lleva 12. ¿Cuántas cajas completas se llenan y cuántos huevos sobran?", "12 cajas y sobran 6", "12 × 12 = 144 y 150 − 144 = 6."),
        ex("Se quiere transportar a 150 estudiantes en buses de 40 asientos. ¿Cuántos buses se necesitan?", "4", "Tres buses llevan 120; sobran 30 estudiantes que necesitan un cuarto bus."),
        arith("Calcula 3.600 + 4.800 ÷ 6.", "3600+4800//6", "Primero la división y después la suma."),
    ],
    app=[
        ex("Un camión carga 1.200 kg por viaje. Debe llevar 7.500 kg. ¿Cuántos viajes necesita como mínimo?", "7", "1.200 × 6 = 7.200 no alcanza; con 7 viajes se llevan 8.400 kg."),
        arith("Se juntan $45.000 y se gastan $12.600. El resto se reparte en partes iguales entre 9 personas. ¿Cuánto recibe cada una?", "(45000-12600)//9", "Primero se resta lo gastado y luego se divide."),
        arith("Una tienda compra 4 cajas a $18.500 cada una y vende 3 artículos a $5.250 y uno a $9.000. ¿Cuánto más gastó de lo que ganó?", "4*18500-(3*5250+9000)", "Se resta el total ganado del total gastado."),
    ],
    rea=[
        ex("Para 100 personas hay mesas de 8 sillas. Juan dice que bastan 12 mesas porque 100 ÷ 8 es 12 y algo. ¿Cuántas mesas se necesitan?", "13", "12 mesas acomodan a 96 personas y quedan 4 sin silla."),
        ex("María lee 25 páginas por día durante 12 días. El libro costó $9.000. ¿Cuántas páginas leyó y qué dato sobra?", "300 páginas; sobra el precio", "25 × 12 = 300; el precio no se necesita para saber las páginas."),
    ],
    cha=[
        ex("¿Cuántos números entre 8 y 100 dejan resto 2 al dividirse por 7?", "14", "Son 9, 16, 23, … , 100: 2 más múltiplos de 7, desde 1 × 7 = 7 hasta 14 × 7 = 98, es decir 14 números."),
        arith("Con $50.000 se compran 10 cuadernos de $3.200 y 6 reglas de $1.500. ¿Cuánto dinero sobra?", "50000-(10*3200+6*1500)", "Se resta el gasto total del dinero que había."),
    ],
    ctx=[ex("Un colegio ficticio de 1.325 estudiantes organiza una salida y arrienda buses de 45 asientos. ¿Cuántos buses necesita como mínimo?", "30", "1.325 ÷ 45 da 29 y sobran 20; 29 buses no alcanzan.")],
    sc=[
        arith("Calcula 60 ÷ 5 + 3 × 7.", "60//5+3*7", "División y multiplicación primero."),
        ex("Se guardan 250 manzanas en bolsas de 6. ¿Cuántas bolsas completas se llenan?", "41", "6 × 41 = 246 y sobran 4 manzanas."),
        arith("Calcula 9.000 − 3 × 1.250.", "9000-3*1250", "Primero la multiplicación."),
    ],
    op=task(
        "Resuelve y explica este problema: «Una escuela ficticia tiene 428 estudiantes y organiza un paseo. Los buses tienen 45 asientos y cada bus cuesta $85.000. Además, cada estudiante lleva una colación de $1.200». Calcula cuántos buses necesita y el costo de los buses. Indica qué dato sobra para esa pregunta.",
        "428 ÷ 45 da 9 y sobran 23, por lo tanto necesita 10 buses. Costo: 10 × 85.000 = $850.000. La colación de $1.200 sobra para esa pregunta.",
        ["interpreta el resto correctamente", "calcula el costo con la operación correcta", "identifica el dato que sobra"],
        ["división con cociente y resto", "costo calculado", "frase que nombra el dato que sobra"],
        ["dejar el cociente sin sumar 1", "usar la colación en el cálculo"],
        "Pide que compruebe que 9 buses llevan 405 personas, que no alcanzan para 428.",
    ),
    reinforce="Se reparten 95 lápices en cajas de 12. Calcula cuántas cajas completas se llenan, cuántos lápices sobran y cuántas cajas harían falta para guardar todos.",
    extend="Inventa un problema donde la respuesta sea el resto y otro donde la respuesta sea el cociente más 1. Resuélvelos.",
)
