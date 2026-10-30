"""Student material for 4.º básico Matemática, OA 10 (fracciones propias y números mixtos) y OA 11 (décimos y centésimos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA10, OA11 = "MA04 OA 10", "MA04 OA 11"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


MIXTO = "Los números mixtos se escriben así: 2 1/4 se lee «dos enteros y un cuarto»; no es 21/4."

# ================================================================ OA 10
register(
    OA10, 1,
    materials="Lápiz y papel. Si quieres, una hoja de papel para doblar en partes iguales.",
    use="Aprenderé a reconocer si una fracción es menor que un entero, igual a un entero o mayor que un entero. Sirve para saber si una cantidad es una parte o más de uno.",
    prior=["Sé leer fracciones como 1/2, 1/4 y 3/4.", "Sé que un entero se divide en partes iguales."],
    explain=[
        "Una fracción se escribe con dos números. El de abajo, el denominador, dice en cuántas partes iguales está dividido un entero. El de arriba, el numerador, dice cuántas de esas partes se toman.",
        "Si el numerador es menor que el denominador, la fracción es propia: es menos que un entero. Por ejemplo, 3/4 son tres partes de las cuatro de un entero. Si el numerador es igual al denominador, como 4/4, se tiene justo un entero.",
        "Si el numerador es mayor que el denominador, como 5/4, se toman más partes de las que tiene un entero. Entonces la cantidad es mayor que 1 y la fracción se llama impropia. En la recta numérica, 5/4 queda después del 1.",
    ],
    vocab=[("fracción propia", "fracción menor que un entero: el numerador es menor que el denominador"), ("fracción impropia", "fracción mayor que un entero: el numerador es mayor que el denominador"), ("numerador", "número de arriba: partes que se toman"), ("denominador", "número de abajo: partes iguales en que se divide un entero"), ("entero", "la unidad completa, sin partes que falten")],
    worked=[
        {"title": "Clasificar una fracción", "problem": "¿7/5 es menor que 1, igual a 1 o mayor que 1?", "steps": ["El denominador 5 dice que un entero tiene 5 partes.", "El numerador es 7: se toman 7 partes, más que las 5 de un entero.", "Como 7 es mayor que 5, la fracción es impropia."], "answer": "Es mayor que 1"},
        {"title": "Fracción propia", "problem": "Una pizza se corta en 8 trozos iguales y comes 3. ¿Qué fracción comiste y es propia?", "steps": ["La pizza completa tiene 8 trozos: el denominador es 8.", "Comiste 3 trozos: el numerador es 3.", "Como 3 es menor que 8, es una fracción propia."], "answer": "3/8; es propia porque es menos que una pizza entera"},
    ],
    mistakes=[
        {"wrong": "Decir que 6/5 es menor que 1 porque «5 es menor que 6, entonces es chico».", "why": "Se mira solo el tamaño de los números y no cuántas partes forman un entero.", "fix": "Un entero son 5/5. Como 6/5 tiene una parte más, es mayor que 1."},
        {"wrong": "Decir que 4/4 es una fracción propia.", "why": "No se compara el numerador con el denominador.", "fix": "4/4 es un entero completo. Para ser propia, el numerador debe ser menor que el denominador."},
    ],
    tiers={
        "recovery": [
            ex("Una pizza está cortada en 4 trozos iguales y te comes 3. ¿Qué fracción de la pizza comiste?", "3/4", "Se toman 3 de las 4 partes iguales."),
            ex("De las fracciones 5/4, 3/8 y 6/6, ¿cuál es propia?", "3/8", "Solo en 3/8 el numerador es menor que el denominador."),
            ex("Una barra dividida en 5 partes iguales se muestra así: ▮▮▮▯▯. Las partes ▮ están pintadas y las ▯ no. ¿Qué fracción está pintada?", "3/5", "Hay 3 partes pintadas de 5 iguales."),
        ],
        "understand": [
            ex("En la fracción 7/4, ¿qué número dice en cuántas partes iguales se divide un entero?", "4", "El denominador, el de abajo, dice en cuántas partes se divide."),
            ex("Una fracción tiene el numerador menor que el denominador. ¿Es menor que 1, igual a 1 o mayor que 1?", "Menor que 1", "Se toman menos partes de las que tiene un entero."),
            ex("Un entero está dividido en 8 partes iguales. ¿Qué fracción representa el entero completo?", "8/8", "Se toman las 8 partes de las 8."),
        ],
        "apply": [
            ex("Mira las fracciones 2/5, 5/5 y 7/5. ¿Cuál es menor que 1, cuál es igual a 1 y cuál es mayor que 1?", "2/5 menor que 1; 5/5 igual a 1; 7/5 mayor que 1", "Se compara cada numerador con el denominador 5."),
            ex("En una recta numérica, ¿en qué número entero queda justo la fracción 4/4?", "En el 1", "Cuatro cuartos forman un entero."),
            ex("¿Cuántas fracciones con denominador 6 son mayores que 1 y menores que 2? Cuenta 7/6, 8/6 y las demás hasta llegar a 2 enteros.", "5", "Los numeradores son 7, 8, 9, 10 y 11, porque 12/6 ya es 2."),
        ],
        "reason": [
            ex("Ana dice que 6/5 es menor que 1 porque «6 y 5 son números chicos». ¿Tiene razón? Explica con partes.", "No; 6/5 es mayor que 1", "Un entero son 5/5 y 6/5 tiene una parte más."),
            ex("Luz dice que 4/4 es una fracción propia porque tiene números pequeños. ¿Tiene razón?", "No; 4/4 es un entero", "Una propia tiene numerador menor que el denominador y aquí son iguales."),
        ],
        "challenge": [
            ex("Una fracción con denominador 5 es propia. ¿Cuál es el mayor numerador entero que puede tener?", "4", "El numerador debe ser menor que 5."),
            ex("En una recta se ubican 3/2, 1/2, 4/2 y 2/2. ¿Cuáles quedan a la derecha del 1?", "3/2 y 4/2", "Solo ellas tienen el numerador mayor que 2, o sea más de un entero."),
        ],
    },
    context=[ex("En una fiesta hay 2 tortas iguales, cada una cortada en 6 trozos. Se comieron 8 trozos. ¿Se comió más de una torta o menos de una torta?", "Más de una torta", "Una torta son 6 trozos y 8 trozos es 8/6, que es mayor que 1.")],
    selfcheck=[
        ex("¿La fracción 9/10 es propia o impropia?", "Propia", "El numerador 9 es menor que el denominador 10."),
        ex("¿Qué fracción con denominador 3 es igual a un entero?", "3/3", "Se toman las 3 partes de las 3."),
        ex("Un cartel dice 11/8 de pan. ¿Es menos que un pan o más que un pan?", "Más que un pan", "Con 8 octavos se forma un pan y 11 es más que 8."),
    ],
    open_task=task(
        "Elige una de estas listas y clasifica cada fracción en «menor que 1», «igual a 1» o «mayor que 1». Lista A: 1/3, 3/3, 5/3, 7/8. Lista B: 6/4, 2/4, 4/4, 9/10. Escribe una frase que explique cómo lo decidiste.",
        "Lista B: 6/4 mayor que 1; 2/4 menor que 1; 4/4 igual a 1; 9/10 menor que 1. Comparé cada numerador con el denominador.",
        ["clasifica bien cada fracción", "compara numerador y denominador", "explica con una frase"],
        ["lista clasificada", "frase de explicación"],
        ["decidir por el tamaño de los números", "creer que 4/4 es propia"],
        "Pide que dibuje una barra para una fracción dudosa. Reconoce la comparación con el denominador.",
    ),
    reinforce="Dobla una hoja en 4 partes iguales y pinta 3. Luego piensa cuántas partes necesitarías para tener más de una hoja.",
    extend="Escribe tres fracciones con denominador 7: una menor que 1, una igual a 1 y una mayor que 1.",
)

register(
    OA10, 2,
    materials=f"Lápiz y papel. {MIXTO}",
    use="Aprenderé a escribir cantidades mayores que un entero como número mixto. Sirve para decir «2 pizzas y media» con números.",
    prior=["Sé qué es una fracción propia.", "Sé que 4/4 es un entero."],
    explain=[
        "Un número mixto tiene dos partes: enteros y una fracción propia. Por ejemplo, 2 1/4 significa dos enteros y un cuarto más. Se lee «dos enteros y un cuarto».",
        "Para formar un número mixto desde una fracción impropia, junta las partes en enteros. En 7/4, cada 4 cuartos forman un entero. Con 7 cuartos se arma 1 entero (4/4) y sobran 3 cuartos. Entonces 7/4 = 1 3/4.",
        "La fracción de un número mixto debe ser propia. Si en la fracción cabe otro entero completo, ese entero se cuenta aparte. Cuidado: 2 1/4 no es lo mismo que 21/4. En 2 1/4 hay dos enteros; en 21/4 hay veintiún cuartos.",
    ],
    vocab=[("número mixto", "número formado por enteros y una fracción propia"), ("fracción impropia", "fracción mayor que un entero, como 7/4"), ("entero", "la unidad completa"), ("sobrar", "quedar partes que no alcanzan para otro entero"), ("agrupar", "juntar partes para formar enteros")],
    worked=[
        {"title": "De fracción a mixto", "problem": "Escribe 7/4 como número mixto.", "steps": ["Un entero tiene 4 cuartos.", "En 7 cuartos hay 1 grupo de 4 cuartos y sobran 3 cuartos.", "Escribo 1 entero y 3/4."], "answer": "1 3/4"},
        {"title": "Contar enteros y fracción", "problem": "Hay 2 pizzas enteras y 3/4 de otra. ¿Cómo se escribe la cantidad?", "steps": ["Hay 2 enteros.", "Sobra una fracción propia: 3/4.", "Junto ambas partes: 2 3/4."], "answer": "2 3/4"},
    ],
    mistakes=[
        {"wrong": "Escribir 7/4 = 1 7/4.", "why": "Se deja la fracción completa y no se separan los enteros.", "fix": "4/4 ya es un entero. Quedan 3/4, así que 7/4 = 1 3/4."},
        {"wrong": "Pensar que 2 1/3 es lo mismo que 21/3.", "why": "Se lee el número mixto como un solo número.", "fix": "2 1/3 son dos enteros y un tercio. 21/3 son veintiún tercios, que es mucho más."},
    ],
    tiers={
        "recovery": [
            ex("Una figura tiene 1 entero pintado y además 1/2 más. ¿Cómo se escribe como número mixto?", "1 1/2", "Hay 1 entero y una fracción propia de medio."),
            ex("En el número mixto 2 1/4, ¿cuántos enteros hay y qué fracción sobra?", "2 enteros y 1/4", "El número de la izquierda indica los enteros y la fracción es lo que sobra."),
            ex("Tienes 2 pizzas enteras y 3/4 de otra. Escribe esa cantidad como número mixto.", "2 3/4", "Se escriben los enteros y la fracción propia."),
        ],
        "understand": [
            ex("En el número mixto 3 2/5, ¿qué número indica los enteros?", "3", "El número grande de la izquierda cuenta enteros."),
            ex("¿Cuántos cuartos hay en 1 entero?", "4", "Un entero se forma con 4/4."),
            ex("Un número mixto debe tener una fracción propia. ¿Puede escribirse 1 5/4? Explica en una frase.", "No; 5/4 contiene otro entero", "En 5/4 hay 4/4, que es un entero, más 1/4."),
        ],
        "apply": [
            ex("Escribe 5/3 como número mixto. Recuerda que 3/3 forman un entero.", "1 2/3", "5 tercios son 1 entero (3/3) y sobran 2/3."),
            ex("Escribe 9/4 como número mixto.", "2 1/4", "9 cuartos son 2 grupos de 4 (8 cuartos) y sobra 1/4."),
            ex("Escribe 7/2 como número mixto.", "3 1/2", "7 medios son 3 enteros (6 medios) y sobra 1/2."),
        ],
        "reason": [
            ex("Teo escribió 7/4 = 1 7/4. ¿Qué error cometió y cómo se escribe bien?", "Dejó 7/4 completo; es 1 3/4", "4/4 ya es un entero y sobran 3/4."),
            ex("Kira dice que 2 1/3 y 21/3 son la misma cantidad. ¿Tiene razón?", "No; 21/3 es mucho mayor", "2 1/3 son 2 enteros y un tercio. 21/3 son 21 tercios, o sea 7 enteros."),
        ],
        "challenge": [
            ex("Un número mixto tiene 3 enteros y su fracción con denominador 4 es la mayor posible que es propia. ¿Cuál es?", "3 3/4", "La mayor fracción propia con cuartos es 3/4."),
            ex("¿Entre qué dos enteros consecutivos está la fracción 11/4? Primero escríbela como número mixto.", "Entre 2 y 3", "11/4 = 2 3/4, que está después del 2 y antes del 3."),
        ],
    },
    context=[ex("Un queque se corta en 6 trozos iguales. En un cumpleaños se comen 17 trozos de varios queques iguales. ¿Cuántos queques enteros y qué fracción de otro se comieron?", "2 enteros y 5/6", "17 sextos son 2 grupos de 6 (12 sextos) y sobran 5/6; 2 5/6.")],
    selfcheck=[
        ex("Escribe 6/5 como número mixto.", "1 1/5", "5/5 forman un entero y sobra 1/5."),
        ex("¿Cómo se lee el número mixto 4 1/2?", "Cuatro enteros y un medio", "Se nombra primero los enteros y luego la fracción."),
        ex("Escribe «tres enteros y dos quintos» con números.", "3 2/5", "Se escriben los enteros y luego la fracción."),
    ],
    open_task=task(
        "Elige uno de estos pedidos y escríbelo como número mixto: A) 10/3 de litro de jugo; B) 13/4 de metro de cinta. Haz un dibujo con rectángulos para mostrar cómo juntaste las partes en enteros.",
        "A) 10/3 = 3 1/3, porque 9/3 son 3 enteros y sobra 1/3. Dibujé 3 rectángulos completos y un tercio.",
        ["agrupa las partes en enteros", "escribe el número mixto correcto", "dibuja los enteros y la fracción"],
        ["dibujo", "número mixto"],
        ["dejar la fracción impropia", "confundir 2 1/4 con 21/4"],
        "Pide que cuente en voz alta los enteros que dibujó. Reconoce el agrupar antes del símbolo.",
    ),
    reinforce="Dobla una hoja en 3 partes iguales y recorta tiras de un tercio. Con 8 tiras, forma enteros y mira cuántas sobran.",
    extend="Escribe cuatro fracciones impropias con denominador 5 y transforma cada una a número mixto.",
)

register(
    OA10, 3,
    materials=f"Lápiz y papel. {MIXTO}",
    use="Aprenderé a pasar entre dibujos, la recta numérica, números mixtos y fracciones. Sirve para reconocer la misma cantidad escrita de varias formas.",
    prior=["Sé escribir una fracción impropia como número mixto.", "Sé leer una recta numérica con partes iguales."],
    explain=[
        "Una misma cantidad puede mostrarse con un dibujo, un punto en la recta numérica, un número mixto o una fracción. Por ejemplo, 2 1/4 y 9/4 son la misma cantidad escrita de dos formas.",
        "Para pasar de número mixto a fracción, cuenta cuántas partes hay en los enteros y suma las que sobran. En 2 1/4, cada entero tiene 4 cuartos. Dos enteros son 8 cuartos y con 1 cuarto más son 9 cuartos: 2 1/4 = 9/4.",
        "Para pasar de fracción a número mixto, agrupa en enteros, como ya hiciste. En la recta numérica, si cada entero está dividido en cuartos, 9/4 queda 1 espacio después del 2. Así comprobamos que ambas escrituras coinciden. Recuerda que medio entero es igual a 2 cuartos.",
    ],
    vocab=[("recta numérica", "línea con números ordenados a distancias iguales"), ("equivalente", "que representa la misma cantidad aunque se escriba distinto"), ("fracción impropia", "fracción mayor que un entero"), ("número mixto", "enteros y una fracción propia"), ("modelo", "dibujo o recta que muestra una cantidad")],
    worked=[
        {"title": "De mixto a fracción", "problem": "Escribe 2 1/4 como fracción de cuartos.", "steps": ["Cada entero tiene 4 cuartos y hay 2 enteros: 2 × 4 = 8 cuartos.", "Agrego el cuarto que sobra: 8 + 1 = 9.", "Son 9 cuartos."], "answer": "9/4"},
        {"title": "Leer la recta", "problem": "En una recta con cada entero dividido en 4 partes, un punto está 3 espacios después del 2. ¿Qué número es?", "steps": ["Pasó 2 enteros completos.", "Avanzó 3 espacios de cuarto más.", "Es 2 y 3/4. En cuartos son 8 + 3 = 11."], "answer": "2 3/4, que es igual a 11/4"},
    ],
    mistakes=[
        {"wrong": "Escribir 2 1/4 = 3/4.", "why": "Se suman los números sueltos 2 + 1 sin pensar en las partes.", "fix": "Cada entero son 4 cuartos. 2 enteros son 8 cuartos, más 1 cuarto: 9/4."},
        {"wrong": "Ubicar 9/4 antes del 2 en la recta.", "why": "Se ve el 9 y se cree que es un número menor.", "fix": "9/4 = 2 1/4, así que está después del 2."},
    ],
    tiers={
        "recovery": [
            ex("En una recta con cada entero dividido en 4 partes iguales, un punto está 3 espacios después del 2. ¿Qué número mixto es?", "2 3/4", "Pasó 2 enteros y 3 cuartos más."),
            ex("Dos barras iguales divididas en 4 partes. En la primera se pintan todas las partes y en la segunda, 2 partes. ¿Qué número mixto muestran? Escribe la fracción con cuartos.", "1 2/4", "Hay 1 entero completo y 2 de las 4 partes de otro."),
            ex("Un entero tiene 3 tercios. ¿Cuántos tercios hay en 1 1/3?", "4", "Hay 3 tercios del entero más 1 tercio."),
        ],
        "understand": [
            ex("¿Cuántos medios hay en 3 enteros?", "6", "Cada entero tiene 2 medios y 3 × 2 = 6."),
            ex("Para escribir 2 3/4 como fracción de cuartos, ¿cuántos cuartos forman los 2 enteros?", "8", "Cada entero tiene 4 cuartos y 2 × 4 = 8."),
            ex("En una recta con cuartos, ¿4/4 y el número 1 quedan en el mismo punto?", "Sí", "Cuatro cuartos forman un entero."),
        ],
        "apply": [
            ex("Escribe 2 2/5 como fracción con denominador 5.", "12/5", "Los 2 enteros son 10 quintos y se suman 2 quintos."),
            ex("Escribe 13/5 como número mixto.", "2 3/5", "13 quintos son 2 enteros (10 quintos) y sobran 3."),
            ex("Escribe 4 1/2 como fracción con denominador 2.", "9/2", "Los 4 enteros son 8 medios y se suma 1 medio."),
        ],
        "reason": [
            ex("Mari dice que 3 2/5 = 17/5. Comprueba si tiene razón.", "Sí; 3 enteros son 15 quintos y 15 + 2 = 17", "Cada entero son 5 quintos y quedan 2 quintos más."),
            ex("Rita escribió 2 3/4 = 11/4 y Sol escribió 2 3/4 = 9/4. ¿Quién tiene razón?", "Rita", "Los 2 enteros son 8 cuartos y 8 + 3 = 11."),
        ],
        "challenge": [
            ex("Un número mixto es igual a 14/3. ¿Cuál es?", "4 2/3", "14 tercios son 4 enteros (12 tercios) y sobran 2."),
            ex("Ordena de menor a mayor: 9/4, 2 1/2 y 7/4.", "7/4, 9/4, 2 1/2", "En cuartos son 7/4, 9/4 y 10/4."),
        ],
    },
    context=[ex("Una receta pide 2 1/2 vasos de agua. Para medirlos usas un jarro que mide medio vaso. ¿Cuántos jarros llenas?", "5", "Los 2 enteros son 4 medios y se suma 1 medio.")],
    selfcheck=[
        ex("Escribe 3 1/4 como fracción con denominador 4.", "13/4", "Los 3 enteros son 12 cuartos y se suma 1."),
        ex("Escribe 7/3 como número mixto.", "2 1/3", "7 tercios son 2 enteros (6 tercios) y sobra 1."),
        ex("¿Cuál es mayor: 5/2 o 2 1/2?", "Son iguales", "5 medios son 2 enteros (4 medios) y 1 medio: 2 1/2."),
    ],
    open_task=task(
        "Elige una cantidad y muéstrala de cuatro formas: dibujo con rectángulos, punto en una recta, número mixto y fracción. Opción A: 1 3/4. Opción B: 2 1/3.",
        "Opción A: dibujo de 1 rectángulo completo y 3 de 4 partes de otro; recta con el punto entre 1 y 2; 1 3/4; 7/4.",
        ["dibujo correcto", "punto bien ubicado en la recta", "número mixto", "fracción equivalente"],
        ["dibujo y recta", "las dos escrituras"],
        ["sumar solo los números sueltos", "ubicar la fracción antes del entero"],
        "Pide que explique cuántos cuartos o tercios hay en cada entero. Reconoce el paso entre modelo y símbolo.",
    ),
    reinforce="Dibuja una recta del 0 al 3 con cada entero dividido en 4 y escribe debajo de cada marca su fracción.",
    extend="Escribe cuatro números mixtos y su fracción impropia equivalente, usando solo medios y tercios.",
)

register(
    OA10, 4,
    materials=f"Lápiz y papel. {MIXTO}",
    use="Aprenderé a resolver situaciones con fracciones propias y números mixtos hasta el 5. Sirve para medir cantidades como 4 1/2 kilos.",
    prior=["Sé pasar entre fracción impropia y número mixto.", "Sé ubicar fracciones en una recta numérica."],
    explain=[
        "Las fracciones y los números mixtos aparecen al medir: litros, kilos, metros y trozos de pizza. En los problemas, primero decide cuántas partes iguales forman un entero. Luego cuenta los enteros y las partes que sobran.",
        "Si debes repartir una cantidad en partes, escríbela primero en la misma fracción. Por ejemplo, 2 1/2 litros y jarros de 1/2 litro: 2 enteros son 4 medios y con 1 más son 5 medios. Se llenan 5 jarros.",
        "Los números de esta clase llegan hasta el 5. Para comparar dos números mixtos, mira primero los enteros. Si son iguales, compara las fracciones. Siempre revisa tu respuesta con un dibujo o con la recta numérica.",
    ],
    vocab=[("comparar", "decidir cuál cantidad es mayor, menor o si son iguales"), ("medir", "averiguar cuánto mide o pesa algo"), ("parte sobrante", "fracción que queda después de formar enteros"), ("recta numérica", "línea con números ordenados"), ("comprobar", "revisar que una respuesta sea correcta")],
    worked=[
        {"title": "Comparar mixtos", "problem": "Un tablón mide 3 1/4 m y otro mide 3 3/4 m. ¿Cuál es más largo?", "steps": ["Los dos tienen 3 enteros.", "Comparo las fracciones: 3/4 es mayor que 1/4.", "El de 3 3/4 m es más largo."], "answer": "El de 3 3/4 m"},
        {"title": "Repartir en partes iguales", "problem": "Hay 4 1/2 kilos de papas y se arman bolsas de 1/2 kilo. ¿Cuántas bolsas salen?", "steps": ["Cada entero tiene 2 medios: 4 × 2 = 8 medios.", "Se suma el medio que sobra: 8 + 1 = 9.", "Salen 9 bolsas."], "answer": "9 bolsas"},
    ],
    mistakes=[
        {"wrong": "Decir que 4 5/4 es un buen número mixto.", "why": "La fracción 5/4 es impropia y contiene otro entero.", "fix": "5/4 = 1 1/4, así que 4 5/4 = 5 1/4."},
        {"wrong": "Pensar que 1 3/4 es menor que 1 1/4 porque 3/4 «tiene el 4 más grande».", "why": "Se compara el denominador en vez de las partes que se toman.", "fix": "Con el mismo denominador, más partes es más cantidad: 3/4 es mayor que 1/4."},
    ],
    tiers={
        "recovery": [
            ex("En una recta con cuartos, el punto P está justo en medio entre el 3 y el 4. ¿Qué número mixto es? Escríbelo en cuartos.", "3 2/4", "Medio entero son 2 cuartos."),
            ex("Un tablón mide 2 metros y 3/4 de metro. Escribe su medida como número mixto.", "2 3/4 m", "Se escriben los enteros y la fracción propia."),
            ex("¿Cuántos tercios hay en 2 enteros?", "6", "Cada entero tiene 3 tercios y 2 × 3 = 6."),
        ],
        "understand": [
            ex("Si el entero es 4 y la parte fraccionaria usa cuartos, ¿cuál es el mayor número mixto posible?", "4 3/4", "La mayor fracción propia con cuartos es 3/4."),
            ex("En el número mixto 3 2/5, ¿en cuántas partes iguales está dividido cada entero?", "5", "El denominador dice en cuántas partes se divide."),
            ex("Compara 3 1/4 y 3 3/4. ¿Cuál es mayor?", "3 3/4", "Con los mismos enteros, 3/4 es mayor que 1/4."),
        ],
        "apply": [
            ex("Hay 2 1/2 litros de jugo y se llenan jarros de 1/2 litro. ¿Cuántos jarros se llenan?", "5", "Los 2 enteros son 4 medios y se suma 1 medio."),
            ex("Tres cintas miden 2 3/4 m, 2 1/4 m y 3 m. ¿Cuál es la más larga?", "La de 3 m", "3 m tiene un entero más que 2 3/4 m."),
            ex("Una ruta mide 4 1/3 km. ¿Cuántos tercios de kilómetro son? Escribe la fracción.", "13/3", "4 enteros son 12 tercios y se suma 1."),
        ],
        "reason": [
            ex("Julia dice que como 5/4 es mayor que 1, la recta de 0 a 5 no alcanza para ubicarlo. ¿Es cierto?", "No; 5/4 = 1 1/4 y queda entre 1 y 2", "El número es pequeño y cabe entre los enteros 1 y 2 de la recta."),
            ex("Un estudiante escribe 4 5/4. ¿Cómo se corrige para que la fracción sea propia?", "5 1/4", "5/4 = 1 1/4, así que hay 1 entero más."),
        ],
        "challenge": [
            ex("¿Cuántos cuartos hay en 5 enteros?", "20", "Cada entero tiene 4 cuartos y 5 × 4 = 20."),
            ex("Hay 17 trozos de un cuarto de pizza. ¿Cuántas pizzas enteras se pueden armar y qué fracción queda?", "4 pizzas y 1/4", "17 cuartos son 4 grupos de 4 (16 cuartos) y sobra 1."),
        ],
    },
    context=[ex("Una feriante pesa 4 1/2 kilos de manzanas y las pone en bolsas de 1/2 kilo cada una. ¿Cuántas bolsas arma?", "9", "Los 4 enteros son 8 medios y se suma 1 medio.")],
    selfcheck=[
        ex("¿Cuál es mayor: 2 2/3 o 2 1/3?", "2 2/3", "Con los mismos enteros, 2/3 es mayor que 1/3."),
        ex("Escribe 11/2 como número mixto.", "5 1/2", "11 medios son 5 enteros (10 medios) y sobra 1."),
        ex("Un camino mide 3 3/4 km. ¿Entre qué enteros está su medida?", "Entre 3 y 4", "Tiene 3 enteros y una fracción propia."),
    ],
    open_task=task(
        "Elige un problema y resuélvelo con dibujo y símbolos. A) Se necesitan 3 1/2 vasos de leche y se mide con un jarro de 1/2 vaso: ¿cuántos jarros? B) Tres cintas miden 1 3/4 m, 2 1/4 m y 1 1/4 m: ordénalas de menor a mayor.",
        "B) Comparo enteros: 1 3/4 y 1 1/4 tienen 1 entero y 1/4 es menor que 3/4; 2 1/4 tiene 2 enteros. Orden: 1 1/4 m, 1 3/4 m, 2 1/4 m.",
        ["elige un problema y lo resuelve", "usa un dibujo o la recta", "escribe la respuesta con unidad", "comprueba el resultado"],
        ["dibujo o recta", "respuesta y comprobación"],
        ["comparar solo los denominadores", "dejar la fracción impropia dentro del mixto"],
        "Pide que muestre en el dibujo la comparación. Reconoce comprobar con otra forma de escribir.",
    ),
    reinforce="Usa una cuerda o cinta de papel de 1 metro y marca los cuartos. Mide objetos del hogar y escribe cuántos cuartos de metro miden.",
    extend="Crea un problema con un número mixto menor que 5 y su solución. Cambia el dato para que la respuesta sea una fracción impropia.",
)

# ================================================================ OA 11
register(
    OA11, 1,
    materials="Lápiz y papel. En decimales, la coma separa los enteros de la parte menor que 1: se escribe 0,3.",
    use="Aprenderé a construir y leer décimos. Sirve para escribir partes menores que 1, como 0,5 litros o 0,3 m.",
    prior=["Sé que un entero se divide en partes iguales.", "Sé leer fracciones con denominador 10."],
    explain=[
        "Un décimo es una de las 10 partes iguales en que se divide un entero. Se escribe 1/10 o 0,1. La coma decimal separa los enteros de las partes menores que 1.",
        "Si pintas 3 partes de una barra dividida en 10, pintaste 3 décimos. Se escribe 3/10 o 0,3 y se lee «tres décimos». Diez décimos forman un entero: 10/10 = 1,0.",
        "Si hay enteros y décimos, la coma queda entre ellos. Por ejemplo, 1,3 es un entero y tres décimos, o sea 13 décimos. Si la cantidad es menor que 1, antes de la coma va el 0, como en 0,3.",
    ],
    vocab=[("décimo", "una de las 10 partes iguales de un entero"), ("número decimal", "número que usa coma para mostrar partes del entero"), ("coma decimal", "signo que separa los enteros de los décimos"), ("fracción decimal", "fracción con denominador 10, 100, 1.000…"), ("entero", "la unidad completa")],
    worked=[
        {"title": "Barra de 10 partes", "problem": "Una barra tiene 10 partes iguales y 7 están pintadas. Escribe la parte pintada como fracción y como decimal.", "steps": ["Se pintan 7 partes de 10: la fracción es 7/10.", "Siete décimos se escriben 0,7."], "answer": "7/10 = 0,7"},
        {"title": "Enteros y décimos", "problem": "Escribe 1 entero y 3 décimos como decimal.", "steps": ["Los enteros van antes de la coma: 1.", "Los décimos van después: 3.", "Se escribe 1,3 (y son 13 décimos)."], "answer": "1,3"},
    ],
    mistakes=[
        {"wrong": "Escribir 3/10 como 10,3.", "why": "Se pone el 10 antes de la coma como si fueran enteros.", "fix": "3/10 es menor que 1. Se escribe 0,3: cero enteros y tres décimos."},
        {"wrong": "Decir que 0,1 es mayor que 1.", "why": "Se piensa en cuántos números hay, no en el valor.", "fix": "0,1 es una décima parte de un entero, menor que 1."},
    ],
    tiers={
        "recovery": [
            ex("Una barra se divide en 10 partes iguales y se pintan 3. ¿Qué fracción está pintada y cómo se escribe como decimal?", "3/10 = 0,3", "Se pintan 3 partes de 10."),
            ex("Escribe con palabras el decimal 0,7.", "Siete décimos", "El 7 está en el lugar de los décimos."),
            ex("¿Cuántos décimos forman un entero?", "10", "Un entero se divide en 10 partes iguales."),
        ],
        "understand": [
            ex("En el decimal 0,4, ¿qué dígito está en el lugar de los décimos?", "4", "El primer dígito después de la coma indica los décimos."),
            ex("¿Qué fracción con denominador 10 representa el decimal 0,9?", "9/10", "El 9 son nueve décimos."),
            ex("¿0,1 es mayor o menor que 1?", "Menor", "0,1 es una sola parte de las 10 de un entero."),
        ],
        "apply": [
            ex("Una regla tiene 10 cuadritos iguales y 6 están pintados. ¿Qué número decimal representa lo pintado?", "0,6", "Son 6 décimos de la regla."),
            ex("¿Cuántos décimos son la mitad de un entero?", "5", "La mitad de 10 partes iguales son 5 partes."),
            ex("Escribe como número decimal «ocho décimos».", "0,8", "Ocho décimos se escribe 0,8."),
        ],
        "reason": [
            ex("Lía escribe 3/10 = 10,3. ¿Dónde está el error y cuál es la escritura correcta?", "Pone 10 enteros; es 0,3", "3/10 es menos que 1 entero, entonces antes de la coma va 0."),
            ex("Hay dos barras iguales de 10 partes. En una se pintan 4 y en otra 7. ¿Cuál tiene más pintado y cómo se escriben?", "La segunda: 0,7 es mayor que 0,4", "7 décimos son más que 4 décimos."),
        ],
        "challenge": [
            ex("En una recta de 0 a 1 dividida en 10 partes, un punto está 2 partes después de 0,5. ¿Qué decimal es?", "0,7", "0,5 más 2 décimos da 7 décimos."),
            ex("¿Cuántos décimos hay en el decimal 1,3?", "13", "Un entero son 10 décimos y se suman 3 más."),
        ],
    },
    context=[ex("Una botella de un litro tiene 10 marcas iguales y el agua llega a la séptima marca. ¿Qué parte del litro hay? Escríbela como decimal.", "0,7 litro", "Hay 7 de las 10 marcas, o sea 7 décimos.")],
    selfcheck=[
        ex("Escribe 5/10 como número decimal.", "0,5", "Cinco décimos se escribe 0,5."),
        ex("¿Cuántos décimos son 2 enteros? Cuenta 10 por cada entero.", "20", "Cada entero tiene 10 décimos y 2 × 10 = 20."),
        ex("¿Cómo se lee 0,2?", "Dos décimos", "El 2 está en el lugar de los décimos."),
    ],
    open_task=task(
        "Dibuja una barra con 10 partes iguales. Elige 0,4 o 0,8. Pinta las partes que corresponden, escribe la fracción y el decimal, y escribe cuántas partes faltan para llegar a 1.",
        "Elegí 0,4: pinté 4 de 10 partes. Fracción: 4/10; decimal: 0,4. Faltan 6 partes para llegar a un entero.",
        ["divide la barra en 10 partes iguales", "pinta la cantidad correcta", "escribe la fracción y el decimal", "dice cuántas faltan"],
        ["dibujo", "fracción y decimal", "partes que faltan"],
        ["partes desiguales", "poner el número antes de la coma"],
        "Pide que cuente las partes pintadas y las que faltan. Reconoce que el denominador es el total de partes.",
    ),
    reinforce="Con una regla, mira los 10 milímetros de 1 cm. Piensa que cada uno es un décimo de centímetro.",
    extend="Escribe cinco decimales distintos con un solo dígito después de la coma y ordénalos de menor a mayor.",
)

register(
    OA11, 2,
    materials="Lápiz y papel; si quieres, una cuadrícula de 10 × 10 cuadritos dibujada por ti.",
    use="Aprenderé qué son los centésimos usando una cuadrícula de 100 cuadritos. Sirve para escribir cantidades más pequeñas que un décimo.",
    prior=["Sé que un décimo es una de 10 partes de un entero.", "Sé escribir décimos como decimales."],
    explain=[
        "Una cuadrícula de 10 por 10 tiene 100 cuadritos y representa un entero. Cada cuadrito es un centésimo: se escribe 1/100 o 0,01. Una columna de 10 cuadritos es un décimo, o sea 10 centésimos.",
        "Si pintas 25 cuadritos de los 100, pintaste 25 centésimos: 25/100 = 0,25. El primer dígito después de la coma cuenta los décimos (columnas completas) y el segundo cuenta los centésimos (cuadritos sueltos).",
        "Por eso 0,43 es 4 columnas y 3 cuadritos. También 0,5 es igual a 0,50: 5 columnas son 50 cuadritos. Cuidado: 0,07 son 7 cuadritos, no 7 columnas.",
    ],
    vocab=[("centésimo", "una de las 100 partes iguales de un entero"), ("cuadrícula", "figura con filas y columnas de cuadritos iguales"), ("décimo", "10 centésimos; una columna de 10 cuadritos"), ("fracción decimal", "fracción con denominador 10 o 100"), ("coma decimal", "signo que separa enteros de partes decimales")],
    worked=[
        {"title": "Leer una cuadrícula", "problem": "En una cuadrícula de 100 cuadritos, 4 columnas completas y 3 cuadritos sueltos están pintados. ¿Qué decimal es?", "steps": ["4 columnas son 4 décimos.", "3 cuadritos sueltos son 3 centésimos.", "Se escribe 0,43."], "answer": "0,43"},
        {"title": "Del decimal a los cuadritos", "problem": "¿Cuántos cuadritos se pintan para mostrar 0,06?", "steps": ["Cero décimos: ninguna columna completa.", "6 centésimos: 6 cuadritos sueltos."], "answer": "6 cuadritos"},
    ],
    mistakes=[
        {"wrong": "Escribir 7/100 como 0,7.", "why": "Se cree que el dígito va en el primer lugar después de la coma.", "fix": "7/100 son 7 cuadritos sueltos: 0,07. 0,7 serían 7 columnas completas."},
        {"wrong": "Decir que 0,5 y 0,50 son cantidades distintas.", "why": "Se piensa que más dígitos significa más cantidad.", "fix": "5 columnas son 50 cuadritos, así que 0,5 = 0,50."},
    ],
    tiers={
        "recovery": [
            ex("En una cuadrícula de 100 cuadritos se pintan 25. ¿Qué fracción y qué decimal representa lo pintado?", "25/100 = 0,25", "Son 25 centésimos del entero."),
            ex("¿Cuántos cuadritos tiene una cuadrícula de 10 × 10?", "100", "Hay 10 filas con 10 cuadritos cada una."),
            ex("Escribe con palabras el decimal 0,07.", "Siete centésimos", "El 7 está en el lugar de los centésimos."),
        ],
        "understand": [
            ex("En el decimal 0,36, ¿cuántos décimos y cuántos centésimos sueltos hay?", "3 décimos y 6 centésimos", "El 3 cuenta columnas completas y el 6 cuadritos sueltos."),
            ex("¿Es verdad que 0,5 y 0,50 representan la misma cantidad?", "Sí", "5 columnas son 50 cuadritos."),
            ex("¿Cuántos centésimos hay en un décimo?", "10", "Una columna tiene 10 cuadritos."),
        ],
        "apply": [
            ex("En una cuadrícula de 100 cuadritos hay 4 columnas completas y 3 cuadritos sueltos pintados. ¿Qué decimal representa?", "0,43", "4 décimos y 3 centésimos forman 0,43."),
            ex("Escribe 8 centésimos como fracción con denominador 100.", "8/100", "Se pintan 8 de las 100 partes."),
            ex("Se pintan 60 cuadritos de 100. Escribe el decimal con centésimos.", "0,60", "60 centésimos es 0,60 y equivale a 0,6."),
        ],
        "reason": [
            ex("Raúl escribe 7/100 = 0,7. ¿Tiene razón?", "No; 7/100 = 0,07", "7 cuadritos son centésimos, no columnas completas."),
            ex("Cuadrícula A: 3 columnas pintadas. Cuadrícula B: 30 cuadritos sueltos pintados. ¿Muestran la misma cantidad?", "Sí; ambas son 0,30", "3 columnas son 30 cuadritos."),
        ],
        "challenge": [
            ex("Se pinta 0,2 de una cuadrícula y luego 0,05 más. ¿Cuántos cuadritos hay pintados en total?", "25", "0,2 son 20 cuadritos y 0,05 son 5; 20 + 5 = 25."),
            ex("¿Cuántos centésimos hay en el decimal 0,4?", "40", "4 columnas son 40 cuadritos."),
        ],
    },
    context=[ex("Un jardín se dibuja como una cuadrícula de 100 cuadrados. Hay flores en 35 cuadrados. ¿Qué parte del jardín tiene flores? Escríbela como fracción y como decimal.", "35/100 = 0,35", "Son 35 de 100 partes, o sea 35 centésimos.")],
    selfcheck=[
        ex("En una cuadrícula de 100 cuadritos, ¿cuántos cuadritos representa 0,09?", "9", "0,09 son 9 centésimos."),
        ex("Escribe 12/100 como decimal.", "0,12", "Son 1 décimo y 2 centésimos."),
        ex("¿Cuántos cuadritos sueltos faltan para completar una columna si hay 7 pintados en ella?", "3", "Una columna completa tiene 10 cuadritos y 10 − 7 = 3."),
    ],
    open_task=task(
        "Dibuja una cuadrícula de 10 × 10. Elige 0,32 o 0,45 y pinta la cantidad con columnas completas y cuadritos sueltos. Escribe la fracción y el decimal, y explica cuántos décimos y cuántos centésimos pintaste.",
        "Elegí 0,32: pinté 3 columnas completas y 2 cuadritos sueltos. Fracción: 32/100. Son 3 décimos y 2 centésimos.",
        ["dibuja una cuadrícula de 10 × 10", "pinta la cantidad correcta", "escribe fracción y decimal", "explica décimos y centésimos"],
        ["cuadrícula", "fracción y decimal", "explicación"],
        ["pintar las columnas por los cuadritos sueltos", "escribir 0,7 para 7 centésimos"],
        "Pide que cuente los cuadritos pintados. Reconoce usar columnas para ahorrar conteo.",
    ),
    reinforce="Observa una baldosa o cuadrícula del hogar y cuenta sus cuadros. Piensa qué parte del total sería un cuadro.",
    extend="Escribe cinco decimales con dos cifras después de la coma y di cuántos cuadritos de una cuadrícula de 100 representa cada uno.",
)

register(
    OA11, 3,
    materials="Lápiz y papel. Un entero es 10/10 o 100/100.",
    use="Aprenderé a pasar entre fracciones decimales y números decimales. Sirve para leer medidas como 2,35 m de dos formas.",
    prior=["Sé qué es un décimo y un centésimo.", "Sé usar la coma decimal."],
    explain=[
        "Una fracción decimal tiene denominador 10 o 100. Se puede escribir como número decimal. La fracción 7/10 es 0,7 y la fracción 25/100 es 0,25. El denominador dice cuántos dígitos hay después de la coma: 10 usa uno y 100 usa dos.",
        "Para pasar de decimal a fracción, lee el decimal con palabras. 0,17 es diecisiete centésimos y se escribe 17/100. En 0,35, el 3 vale 3 décimos y el 5 vale 5 centésimos.",
        "Cuando hay enteros, se pueden escribir como número mixto: 1,5 es 1 5/10 y 2,07 es 2 7/100. Un cero detrás de los centésimos importa: 0,07 no es lo mismo que 0,7.",
    ],
    vocab=[("fracción decimal", "fracción con denominador 10 o 100"), ("valor posicional", "lo que vale un dígito según su lugar"), ("lugar de los décimos", "primer lugar a la derecha de la coma"), ("lugar de los centésimos", "segundo lugar a la derecha de la coma"), ("equivalente", "que vale lo mismo aunque se escriba distinto")],
    worked=[
        {"title": "De fracción a decimal", "problem": "Escribe 6/100 como número decimal.", "steps": ["El denominador 100 indica dos dígitos después de la coma.", "6 centésimos se escribe con un cero en los décimos: 0,06."], "answer": "0,06"},
        {"title": "De decimal a mixto", "problem": "Escribe 2,07 como número mixto con fracción decimal.", "steps": ["Hay 2 enteros.", "Después de la coma están 0 décimos y 7 centésimos: 7/100."], "answer": "2 7/100"},
    ],
    mistakes=[
        {"wrong": "Escribir 4 3/100 como 4,3.", "why": "Se coloca el 3 en el lugar de los décimos.", "fix": "3/100 son 3 centésimos: 4,03."},
        {"wrong": "Decir que 0,40 es distinto de 4/10.", "why": "Se piensa que la fracción y el decimal no se pueden comparar.", "fix": "0,40 = 40/100 y es lo mismo que 4/10."},
    ],
    tiers={
        "recovery": [
            ex("Escribe la fracción 4/10 como número decimal.", "0,4", "Cuatro décimos se escribe 0,4."),
            ex("Escribe el decimal 0,17 como fracción.", "17/100", "Son diecisiete centésimos."),
            ex("Escribe la fracción 6/100 como número decimal.", "0,06", "Seis centésimos llevan un cero en los décimos."),
        ],
        "understand": [
            ex("En el decimal 0,35, ¿qué valor tiene el 5?", "5 centésimos (0,05)", "Está en el segundo lugar después de la coma."),
            ex("En el decimal 0,35, ¿qué valor tiene el 3?", "3 décimos (0,3)", "Está en el primer lugar después de la coma."),
            ex("El decimal 0,3, ¿se lee tres décimos o tres centésimos?", "Tres décimos", "Tiene un solo dígito después de la coma."),
        ],
        "apply": [
            ex("Escribe el decimal 1,5 como número mixto con fracción decimal.", "1 5/10", "Un entero y cinco décimos."),
            ex("Escribe el número mixto 2 7/100 como número decimal.", "2,07", "Dos enteros y siete centésimos."),
            ex("Escribe 75/100 como decimal y di cuántos décimos y cuántos centésimos tiene.", "0,75: 7 décimos y 5 centésimos", "El 7 está en los décimos y el 5 en los centésimos."),
        ],
        "reason": [
            ex("Ema escribió 4 3/100 como 4,3. ¿Es correcto?", "No; es 4,03", "3/100 son 3 centésimos y no 3 décimos."),
            ex("Mateo dice que 0,40 y 4/10 son iguales. ¿Tiene razón?", "Sí", "0,40 son 40/100 y 40/100 es lo mismo que 4/10."),
        ],
        "challenge": [
            ex("Un decimal tiene 3 en los décimos y 7 en los centésimos, y 0 enteros. Escríbelo como fracción.", "37/100", "3 décimos y 7 centésimos forman 37 centésimos."),
            ex("Escribe la fracción 12/10 como número decimal. Piensa: un entero son 10/10.", "1,2", "12/10 es un entero y dos décimos."),
        ],
    },
    context=[ex("Una cinta mide 2,35 metros. Escríbelo como número mixto con una fracción decimal.", "2 35/100", "Son 2 enteros y 35 centésimos.")],
    selfcheck=[
        ex("Escribe 9/10 como decimal.", "0,9", "Nueve décimos se escribe 0,9."),
        ex("Escribe 0,08 como fracción.", "8/100", "Son ocho centésimos."),
        ex("Escribe 3 5/10 como número decimal.", "3,5", "Tres enteros y cinco décimos."),
    ],
    open_task=task(
        "Completa una tabla con tres filas: fracción, palabras y decimal. Elige uno de estos grupos. Grupo A: 3/10, 45/100, 8/100. Grupo B: 6/10, 23/100, 5/100. Escribe también cuál de las tres cantidades es la menor.",
        "Grupo B: 6/10 = seis décimos = 0,6; 23/100 = veintitrés centésimos = 0,23; 5/100 = cinco centésimos = 0,05. La menor es 0,05.",
        ["escribe las palabras de cada fracción", "escribe cada decimal correcto", "señala la menor"],
        ["tabla completa", "cantidad menor"],
        ["omitir el cero de 0,05", "mezclar décimos con centésimos"],
        "Pide que lea cada decimal en voz alta con palabras. Reconoce el cero como posición.",
    ),
    reinforce="Escribe un precio de $0,50 en una moneda ficticia y léelo como fracción para ver que 0,50 y 5/10 son iguales.",
    extend="Escribe seis decimales distintos y, para cada uno, su fracción decimal y su lectura con palabras.",
)

register(
    OA11, 4,
    materials="Lápiz y papel. Para comparar, escribe los decimales con la misma cantidad de cifras después de la coma.",
    use="Aprenderé a comparar y ordenar decimales hasta los centésimos. Sirve para saber quién llegó primero en una carrera o cuál medida es mayor.",
    prior=["Sé leer décimos y centésimos.", "Sé que 0,5 y 0,50 son iguales."],
    explain=[
        "Para comparar decimales, primero compara los enteros. Si son iguales, compara los décimos. Si también son iguales, compara los centésimos. Comparas de izquierda a derecha, como en los números naturales.",
        "Ayuda escribir los decimales con la misma cantidad de cifras. Para comparar 0,6 y 0,59, escribe 0,6 como 0,60. Ahora son 60 centésimos y 59 centésimos, así que 0,6 es mayor.",
        "Cuidado: tener más cifras no hace mayor un decimal. 0,8 es mayor que 0,25 porque 8 décimos son 80 centésimos. Para ordenar varios, compara de a dos y escribe los símbolos < (menor que), > (mayor que) o = (igual).",
    ],
    vocab=[("comparar", "decidir si un número es mayor, menor o igual a otro"), ("ordenar", "poner números de menor a mayor o de mayor a menor"), ("menor que (<)", "símbolo que apunta al número más pequeño"), ("mayor que (>)", "símbolo que se abre hacia el número más grande"), ("cifra", "cada dígito de un número")],
    worked=[
        {"title": "Comparar con distinta cantidad de cifras", "problem": "¿Cuál es mayor: 0,6 o 0,59?", "steps": ["Escribo 0,6 como 0,60.", "Comparo 60 centésimos con 59 centésimos.", "60 es mayor que 59."], "answer": "0,6 > 0,59"},
        {"title": "Ordenar", "problem": "Ordena de menor a mayor: 0,5; 0,05; 0,55.", "steps": ["Los escribo con dos cifras: 0,50; 0,05; 0,55.", "Ordeno 5, 50 y 55 centésimos."], "answer": "0,05; 0,5; 0,55"},
    ],
    mistakes=[
        {"wrong": "Decir que 0,8 es menor que 0,25 porque 8 es menor que 25.", "why": "Se comparan los números sin pensar en el lugar de cada dígito.", "fix": "0,8 = 0,80. Como 80 centésimos es mayor que 25 centésimos, 0,8 > 0,25."},
        {"wrong": "Decir que 0,30 es mayor que 0,3.", "why": "Se cree que más cifras es más cantidad.", "fix": "El cero final no cambia el valor: 0,30 = 0,3."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es mayor: 0,4 o 0,7?", "0,7", "7 décimos son más que 4 décimos."),
            ex("¿Cuál es menor: 0,25 o 0,52?", "0,25", "25 centésimos es menor que 52 centésimos."),
            ex("Completa con <, > o =: 0,30 ___ 0,3.", "=", "El cero final no cambia el valor."),
        ],
        "understand": [
            ex("Para comparar 0,6 con 0,59, escribe 0,6 con centésimos.", "0,60", "Así ambos tienen dos cifras después de la coma."),
            ex("¿Es mayor 1,2 o 0,98? Responde y explica con los enteros.", "1,2", "Tiene 1 entero y 0,98 tiene 0 enteros."),
            ex("Dos decimales tienen los mismos enteros. ¿Qué cifra se compara primero?", "Los décimos", "Se sigue de izquierda a derecha después de los enteros."),
        ],
        "apply": [
            ex("Ordena de menor a mayor: 0,5; 0,05 y 0,55.", "0,05; 0,5; 0,55", "En centésimos son 5, 50 y 55."),
            ex("Ordena de mayor a menor: 0,7; 0,07; 0,17 y 0,71.", "0,71; 0,7; 0,17; 0,07", "En centésimos son 71, 70, 17 y 7."),
            ex("Completa con <, > o =: 1,09 ___ 1,9.", "<", "1,09 es 1 entero y 9 centésimos; 1,9 es 1 entero y 90 centésimos."),
        ],
        "reason": [
            ex("Nico dice que 0,8 es menor que 0,25 porque 8 es menor que 25. ¿Tiene razón?", "No; 0,8 es mayor", "0,8 = 0,80, que es más que 0,25."),
            ex("Ana dice que 0,3 y 0,30 son iguales. Beto dice que 0,30 es mayor por tener más cifras. ¿Quién tiene razón?", "Ana", "Un cero al final no cambia el valor."),
        ],
        "challenge": [
            ex("Ordena de menor a mayor: 2,1; 1,99; 2,01 y 1,9.", "1,9; 1,99; 2,01; 2,1", "Primero los de 1 entero y luego los de 2."),
            ex("Con los dígitos 3 y 5, sin repetir, ¿cuál es el mayor decimal de la forma 0,□□?", "0,53", "Se pone el dígito mayor en los décimos."),
        ],
    },
    context=[ex("En una carrera escolar los tiempos fueron: Ana 14,25 s, Beto 14,3 s y Carla 14,2 s. Gana quien tarda menos. ¿Quién ganó?", "Carla", "En centésimos son 1425, 1430 y 1420; el menor es 14,20.")],
    selfcheck=[
        ex("¿Cuál es mayor: 0,09 o 0,1?", "0,1", "0,1 = 0,10 y es mayor que 0,09."),
        ex("Completa con <, > o =: 0,45 ___ 0,54.", "<", "45 centésimos es menor que 54 centésimos."),
        ex("Escribe 0,7 con centésimos para compararlo con 0,65.", "0,70", "Así los dos se leen en centésimos."),
    ],
    open_task=task(
        "Ordena de menor a mayor uno de estos grupos y muestra cómo los escribiste con centésimos. Grupo A: 0,6; 0,06; 0,66; 0,16. Grupo B: 0,2; 0,02; 0,22; 0,12.",
        "Grupo B: 0,20; 0,02; 0,22; 0,12. En orden: 0,02; 0,12; 0,2; 0,22.",
        ["escribe todos con la misma cantidad de cifras", "ordena correctamente", "usa símbolos < o >"],
        ["lista reescrita", "orden final"],
        ["decidir por la cantidad de cifras", "ignorar el lugar de cada dígito"],
        "Pide que explique en qué lugar compara cada par. Reconoce usar centésimos para igualar cifras.",
    ),
    reinforce="Anota cuatro medidas decimales de distancias (por ejemplo, 1,2 m; 1,25 m; 1,05 m; 1,5 m) y ordénalas de menor a mayor.",
    extend="Escribe cuatro decimales distintos entre 0,3 y 0,4 y ordénalos.",
)
