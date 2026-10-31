"""Cuaderno del estudiante de 5.º básico Matemática: OA 10 (fracciones y decimales) y OA 11 (comparar y ordenar decimales hasta la milésima)."""
from __future__ import annotations

from student_content_ma05_a import M, W, f, lesson, task
from student_lessons import arith, ex

OA10 = "MA05 OA 10"
OA11 = "MA05 OA 11"

# ------------------------------------------------------------------ OA 10 clase 1
lesson(
    OA10, 1,
    use="Aprenderé a escribir fracciones con denominador 10 como decimales y a leerlas como décimas. Sirve para pasar de una fracción a un número con coma.",
    prior=["Sé representar fracciones propias.", "Sé que un entero tiene 10 décimas."],
    explain=[
        "Un decimal es otra forma de escribir una fracción. Cuando un entero se divide en 10 partes iguales, cada parte es una décima y se escribe 1/10 o 0,1. La coma decimal separa los enteros de las partes más pequeñas que un entero. Antes de la coma están los enteros, y después están las décimas.",
        "Una fracción con denominador 10 se escribe como decimal poniendo el numerador en el lugar de las décimas: 3/10 = 0,3 y 7/10 = 0,7. Se lee «tres décimas» y «siete décimas». El cero antes de la coma muestra que no hay enteros completos. Si el numerador es 10, 10/10 = 1 entero.",
        "En un dibujo, una barra de 10 partes iguales con 4 sombreadas, ■■■■□□□□□□, representa 4/10 y se escribe 0,4. Revisa siempre que el denominador sea 10 antes de usar este atajo. Con otros denominadores hay que amplificar o simplificar primero, que verás en las siguientes clases.",
    ],
    vocab=[("decimal", "número que usa una coma para separar enteros de partes de un entero"), ("décima", "una de las 10 partes iguales de un entero, se escribe 0,1"), ("coma decimal", "signo que separa la parte entera de la parte decimal"), ("entero", "la unidad completa"), ("lugar de las décimas", "primer lugar a la derecha de la coma")],
    worked=[
        W("De fracción a decimal", "Escribe 7/10 como decimal.", ["El denominador es 10: son décimas.", "Pongo el 7 en el lugar de las décimas.", "0,7 y se lee «siete décimas»."], "0,7"),
        W("De un dibujo a decimal", "Una barra de 10 partes iguales tiene 4 sombreadas: ■■■■□□□□□□. ¿Qué decimal representa?", ["Fracción: 4/10.", "Décimas: 4.", "Decimal: 0,4."], "0,4"),
    ],
    mistakes=[
        M("Escribir 3/10 como 0,03.", "El 3 se puso en el lugar de las centésimas.", "Las décimas van justo después de la coma: 3/10 = 0,3."),
        M("Escribir 3/10 como 3,10.", "Se copió el numerador y el denominador separados por una coma.", "El denominador 10 indica décimas: 3/10 = 0,3."),
    ],
    rec=[
        ex("En 0,3, ¿cuántas décimas hay?", "3", "El 3 está en el lugar de las décimas."),
        ex("Escribe 7/10 como decimal.", "0,7", "Son siete décimas, 0,7."),
        ex("Una barra de 10 partes iguales tiene 4 sombreadas: ■■■■□□□□□□. ¿Qué decimal es?", "0,4", "4/10 = 0,4."),
    ],
    und=[
        ex("Escribe 9/10 como decimal.", "0,9", "Son nueve décimas, 0,9."),
        ex("Escribe 0,6 como fracción con denominador 10.", "6/10", "Son seis décimas, 6/10."),
        ex("¿Cómo se lee 0,8?", "Ocho décimas", "El 8 está en el lugar de las décimas."),
    ],
    app=[
        ex("Una botella de un litro está dividida en 10 partes iguales y se bebieron 3. ¿Cuántos litros se bebieron, como decimal?", "0,3 litros", "3/10 de litro."),
        ex("Un cuaderno de 10 hojas tiene 7 hojas usadas. ¿Qué decimal del cuaderno se usó?", "0,7", "Son 7 décimas del cuaderno."),
        ex("Una cinta de un metro se divide en 10 trozos iguales y se toman 5. ¿Qué decimal de metro es?", "0,5 metros", "5/10 de metro."),
    ],
    rea=[
        ex("Teo dice que 3/10 = 0,03. ¿Está bien?", "No, es 0,3", "Las décimas van en el primer lugar después de la coma."),
        ex("¿Cuántas fracciones con denominador 10 menores que 1 se escriben con una sola cifra decimal distinta de cero?", "9", "Son 1/10 hasta 9/10."),
    ],
    cha=[
        ex("¿Qué número entero es 10/10?", "1", "Diez décimas forman un entero."),
        ex("Si 4/10 = 0,4, ¿qué número entero es 6/10 + 4/10?", "1", "10/10 es un entero."),
    ],
    ctx=[ex("Una pista de carreras ficticia mide 1 kilómetro y está dividida en 10 tramos iguales. Pía corrió 8 tramos. ¿Cuántos kilómetros corrió, como decimal?", "0,8 kilómetros", "8/10 = 0,8.")],
    sc=[
        ex("Escribe 5/10 como decimal.", "0,5", "Son cinco décimas, 0,5."),
        ex("Escribe 0,2 como fracción.", "2/10", "Son dos décimas, 2/10."),
        ex("¿Qué decimal tiene 1 décima y ningún entero?", "0,1", "Una décima es 1/10."),
    ],
    op=task(
        "Elige: 3/10, 6/10 u 8/10. Dibuja una barra de 10 partes iguales, sombrea la fracción, escribe el decimal y su lectura con palabras. Luego da un ejemplo de algo que mida esa cantidad (como litros o metros).",
        "6/10: dibujo una barra de 10 partes y sombreo 6. Es 0,6, «seis décimas». Un ejemplo: una cinta de 0,6 metros.",
        ["divide la barra en 10 partes iguales", "escribe el decimal correcto", "lee con palabras"],
        ["dibujo", "decimal", "lectura"],
        ["poner el numerador en el lugar de las centésimas", "escribir 3,10"],
        "Pide que cuente las partes de la barra y que diga en qué lugar después de la coma puso el numerador.",
    ),
    reinforce="Dibuja tres barras de 10 partes y sombrea 2, 5 y 9. Escribe cada fracción y cada decimal.",
    extend="Explica por qué 0,5 y 5/10 son lo mismo, con un dibujo.",
)

# ------------------------------------------------------------------ OA 10 clase 2
lesson(
    OA10, 2,
    use="Aprenderé a pasar a decimal las fracciones con denominador 2 y 5 amplificándolas a denominador 10. Sirve para escribir medios y quintos con coma.",
    prior=["Sé escribir fracciones con denominador 10 como decimales.", "Sé amplificar fracciones."],
    explain=[
        "Un medio y un quinto no tienen denominador 10, pero se pueden amplificar para tenerlo. Como 2 × 5 = 10, la fracción con denominador 2 se amplifica por 5: 1/2 = 5/10 = 0,5. Como 5 × 2 = 10, la fracción con denominador 5 se amplifica por 2: 2/5 = 4/10 = 0,4.",
        "Los pasos son siempre los mismos. Primero, amplifica la fracción hasta que el denominador sea 10. Segundo, escribe el numerador en el lugar de las décimas. Tercero, lee el decimal y revisa con un dibujo. Con los quintos: 1/5 = 0,2; 2/5 = 0,4; 3/5 = 0,6 y 4/5 = 0,8.",
        "Estas equivalencias son muy usadas. Medio litro es 0,5 litros. Un quinto de un metro es 0,2 metros. Fíjate que el denominador pequeño, 2 o 5, se multiplica por el número que lo lleva a 10. El numerador se multiplica por el mismo número, nunca se suma.",
    ],
    vocab=[("amplificar", "multiplicar numerador y denominador por el mismo número"), ("fracción equivalente", "fracción que vale lo mismo"), ("décima", "una de las 10 partes iguales de un entero"), ("quinto", "una de las 5 partes iguales de un entero"), ("medio", "una de las 2 partes iguales de un entero")],
    worked=[
        W("Medios a decimal", "Escribe 1/2 como decimal.", ["Amplifico por 5 para que el denominador sea 10.", "1/2 = 5/10.", "5/10 = 0,5."], "0,5"),
        W("Quintos a decimal", "Escribe 3/5 como decimal.", ["Amplifico por 2: 3 × 2 = 6 y 5 × 2 = 10.", "3/5 = 6/10.", "6/10 = 0,6."], "0,6"),
    ],
    mistakes=[
        M("Escribir 1/2 como 0,12.", "Se juntaron el numerador y el denominador.", "Se amplifica a 5/10 y se escribe 0,5."),
        M("Escribir 2/5 como 0,25.", "Se escribieron las dos cifras del fraccionario seguidas.", "2/5 = 4/10 = 0,4."),
    ],
    rec=[
        ex("Amplifica 1/2 multiplicando numerador y denominador por 5.", "5/10", "1 × 5 = 5 y 2 × 5 = 10."),
        ex("Completa: 1/2 = __/10.", "5", "Se multiplicó por 5."),
        ex("¿Cómo se escribe 5/10 como decimal?", "0,5", "Son cinco décimas, 0,5."),
    ],
    und=[
        ex("Escribe 2/5 como decimal.", "0,4", "2/5 = 4/10."),
        ex("Escribe 4/5 como decimal.", "0,8", "4/5 = 8/10."),
        ex("Escribe 1/5 como decimal.", "0,2", "1/5 = 2/10."),
    ],
    app=[
        ex("Un vaso contiene 1/2 litro de jugo. ¿Cuántos litros son, como decimal?", "0,5 litros", "1/2 = 5/10."),
        ex("Se pintó 3/5 de una pared. ¿Qué decimal de la pared se pintó?", "0,6", "3/5 = 6/10."),
        ex("Una tira mide 1/5 de metro. ¿Cuántos metros mide, como decimal?", "0,2 metros", "1/5 = 2/10."),
    ],
    rea=[
        ex("Ana escribió 1/2 = 0,12. ¿Cuál es el error y cuál es el decimal correcto?", "Juntó 1 y 2; es 0,5", "1/2 = 5/10."),
        ex("¿Qué es mayor, 1/2 o 0,4?", "1/2", "1/2 = 0,5 y 0,5 > 0,4."),
    ],
    cha=[
        ex("De las fracciones 1/5, 2/5, 3/5 y 4/5, ¿cuántas tienen un decimal menor o igual que 0,6?", "3", "Son 1/5 = 0,2; 2/5 = 0,4 y 3/5 = 0,6."),
        ex("Si 1/2 = 0,5, ¿cuánto es 3/2 como decimal?", "1,5", "3/2 = 1 1/2 = 1,5."),
    ],
    ctx=[ex("Una receta ficticia pide 3/5 de kilogramo de harina. ¿Cuántos kilogramos son, como decimal?", "0,6 kilogramos", "3/5 = 6/10.")],
    sc=[
        ex("Escribe 1/2 como decimal.", "0,5", "Medio es cinco décimas."),
        ex("Escribe 3/5 como decimal.", "0,6", "3/5 = 6/10."),
        ex("¿Por qué número se amplifica una fracción con denominador 5 para llegar a denominador 10?", "Por 2", "5 × 2 = 10."),
    ],
    op=task(
        "Elige: 1/2, 2/5 o 4/5. Amplifícala hasta denominador 10, escribe el decimal y dibuja una barra de 10 partes para comprobar. Explica en una frase cómo pasaste de la fracción al decimal.",
        "4/5: multiplico por 2 arriba y abajo y queda 8/10. Dibujo 10 partes y sombreo 8. Es 0,8.",
        ["amplifica a denominador 10", "escribe el decimal", "comprueba con dibujo"],
        ["fracción equivalente", "decimal", "dibujo"],
        ["sumar en vez de multiplicar", "juntar numerador y denominador"],
        "Pide que verifique que arriba y abajo se multiplicó por el mismo número.",
    ),
    reinforce="Escribe los decimales de 1/5, 2/5, 3/5 y 4/5 en una tabla.",
    extend="Explica por qué 1/2 y 5/10 son iguales usando una barra.",
)

# ------------------------------------------------------------------ OA 10 clase 3
lesson(
    OA10, 3,
    use="Aprenderé a pasar a decimal las fracciones con denominador 4, usando centésimas. Sirve para escribir cuartos como 0,25 y 0,75.",
    prior=["Sé pasar a decimal fracciones con denominador 2, 5 y 10.", "Sé que una centésima es una de las 100 partes iguales de un entero."],
    explain=[
        "Si un entero se divide en 100 partes iguales, cada parte es una centésima y se escribe 1/100 o 0,01. Las centésimas ocupan el segundo lugar después de la coma. Así 25/100 se escribe 0,25 y se lee «veinticinco centésimas». También es 2 décimas y 5 centésimas.",
        "Para pasar 1/4 a decimal, amplifica la fracción por 25 para que el denominador sea 100: 1/4 = 25/100 = 0,25. Para 3/4, amplifica también por 25: 75/100 = 0,75. Los dos cuartos, 2/4, son la mitad: 2/4 = 1/2 = 0,5.",
        "Revisa con el dinero: un cuarto de $100 son $25 y tres cuartos son $75. Así 1/4 = 0,25 y 3/4 = 0,75. Cuando lees un decimal con dos cifras, el primer lugar son las décimas y el segundo las centésimas. Un cero entre la coma y la cifra, como 0,05, cambia el valor.",
    ],
    vocab=[("centésima", "una de las 100 partes iguales de un entero, se escribe 0,01"), ("lugar de las centésimas", "segundo lugar a la derecha de la coma"), ("cuarto", "una de las 4 partes iguales de un entero"), ("amplificar por 25", "multiplicar arriba y abajo por 25"), ("decimal", "número que usa una coma")],
    worked=[
        W("Un cuarto a decimal", "Escribe 1/4 como decimal.", ["Amplifico por 25: 1 × 25 = 25 y 4 × 25 = 100.", "1/4 = 25/100.", "25/100 = 0,25."], "0,25"),
        W("Tres cuartos a decimal", "Escribe 3/4 como decimal.", ["Amplifico por 25: 3 × 25 = 75 y 4 × 25 = 100.", "3/4 = 75/100.", "75/100 = 0,75."], "0,75"),
    ],
    mistakes=[
        M("Escribir 1/4 como 0,4.", "Se tomó el 4 como si fueran décimas.", "1/4 = 25/100 = 0,25."),
        M("Escribir 25/100 como 0,025.", "Se puso un cero de más antes del 25.", "Las centésimas son el segundo lugar: 0,25."),
    ],
    rec=[
        ex("Amplifica 1/4 multiplicando numerador y denominador por 25.", "25/100", "1 × 25 = 25 y 4 × 25 = 100."),
        ex("Escribe 25/100 como decimal.", "0,25", "Son veinticinco centésimas, 0,25."),
        ex("¿Cuántas centésimas hay en 0,75?", "75", "0,75 = 75/100."),
    ],
    und=[
        ex("Escribe 3/4 como decimal.", "0,75", "3/4 = 75/100."),
        ex("Escribe 2/4 como decimal.", "0,5", "2/4 = 1/2 = 5/10."),
        ex("Escribe 1/4 y 3/4 como decimales.", "0,25 y 0,75", "25/100 y 75/100."),
    ],
    app=[
        ex("Una caja de queso tiene 1/4 de kilogramo. ¿Cuántos kilogramos son, como decimal?", "0,25 kilogramos", "1/4 = 25/100."),
        ex("Un recipiente tiene 3/4 de litro de jugo. ¿Cuántos litros son, como decimal?", "0,75 litros", "3/4 = 75/100."),
        ex("En un monedero hay $100 y se gasta 1/4. ¿Cuántos pesos se gastan?", "$25", "1/4 de 100 es 25, y 0,25 de 100 también."),
    ],
    rea=[
        ex("Ema dice que 1/4 = 0,4 porque son los números 1 y 4. ¿Está bien?", "No, es 0,25", "1/4 = 25/100."),
        ex("¿Es 0,25 mayor o menor que 0,3?", "Menor", "0,25 es 25 centésimas y 0,3 es 30 centésimas."),
    ],
    cha=[
        ex("Escribe 1/2, 1/4 y 3/4 como decimales y ordénalos de menor a mayor.", "0,25 < 0,5 < 0,75", "1/4 = 0,25; 1/2 = 0,5; 3/4 = 0,75."),
        ex("Si 1/4 = 0,25, ¿cuánto es 1/4 + 1/4 en decimal?", "0,5", "0,25 + 0,25 = 0,50."),
    ],
    ctx=[ex("Una tabla ficticia mide 3/4 de metro. ¿Cuántos metros mide, como decimal?", "0,75 metros", "3/4 = 75/100.")],
    sc=[
        ex("¿Qué decimal es un cuarto?", "0,25", "1/4 son 25 centésimas."),
        ex("Escribe 0,75 como fracción con denominador 100.", "75/100", "Setenta y cinco centésimas."),
        ex("¿Por qué número se amplifica 1/4 para llegar a denominador 100?", "Por 25", "4 × 25 = 100."),
    ],
    op=task(
        "Elige: 1/4 o 3/4. Amplifica a denominador 100, escribe el decimal, di cuántas décimas y cuántas centésimas tiene y comprueba con $100: ¿cuántos pesos son esa fracción de $100?",
        "3/4: 3/4 = 75/100 = 0,75. Tiene 7 décimas y 5 centésimas. De $100, 3/4 son $75.",
        ["amplifica a denominador 100", "escribe el decimal", "comprueba con $100"],
        ["amplificación", "decimal", "comprobación con dinero"],
        ["escribir 0,4 en vez de 0,25", "poner un cero de más"],
        "Pide que lea el decimal en voz alta como centésimas y que compruebe con el dinero.",
    ),
    reinforce="Escribe los decimales de 1/4, 2/4, 3/4 y 4/4 en una tabla.",
    extend="Explica por qué 0,5 y 0,50 son el mismo número.",
)

# ------------------------------------------------------------------ OA 10 clase 4
lesson(
    OA10, 4,
    use="Aprenderé a elegir la mejor forma de pasar entre fracciones y decimales, y a resolver problemas de medidas con ambas. Sirve para leer una balanza o una receta.",
    prior=["Sé pasar a decimal fracciones con denominador 2, 4, 5 y 10."],
    explain=[
        "Para pasar una fracción a decimal con denominador 2, 4, 5 o 10, amplifica hasta tener denominador 10 o 100. 1/2 y 1/5 pasan por décimas; 1/4 pasa por centésimas. Para pasar de decimal a fracción haz el camino contrario: 0,6 = 6/10, y se puede simplificar a 3/5.",
        "Estas equivalencias sirven en la vida diaria. Una balanza digital muestra 0,75 kilogramos y una receta pide 3/4 de kilogramo: es lo mismo. Una regla en metros marca 0,5 y una tabla mide 1/2 metro: también es lo mismo.",
        "Para comparar una fracción con un decimal, pasa la fracción a decimal, o el decimal a fracción, y compara. Revisa siempre que la coma esté bien puesta, y que hayas usado el denominador correcto (10 para décimas y 100 para centésimas).",
    ],
    vocab=[("equivalencia", "dos números distintos que valen lo mismo"), ("balanza", "aparato que mide el peso"), ("decimal exacto", "decimal que termina, como 0,25"), ("fracción simplificada", "fracción escrita con los números más pequeños"), ("medida", "cantidad con unidad, como kilogramos o metros")],
    worked=[
        W("De decimal a fracción", "Escribe 0,6 como fracción simplificada.", ["0,6 = 6/10.", "Simplifico por 2: 3/5."], "3/5"),
        W("Comparar fracción con decimal", "¿Qué es mayor: 4/5 de litro o 0,75 litros?", ["4/5 = 8/10 = 0,8.", "0,8 > 0,75."], "4/5 de litro"),
    ],
    mistakes=[
        M("Escribir 3/5 como 0,35.", "Se escribieron las cifras de la fracción juntas.", "3/5 = 6/10 = 0,6."),
        M("Escribir 0,75 como 7/5.", "Se separaron las cifras como si fueran numerador y denominador.", "0,75 = 75/100 = 3/4."),
    ],
    rec=[
        ex("Escribe 0,6 como fracción con denominador 10.", "6/10", "Son seis décimas, 6/10."),
        ex("Simplifica 6/10.", "3/5", "Se divide por 2."),
        ex("¿Cuál es el decimal de 1/2?", "0,5", "1/2 = 5/10."),
    ],
    und=[
        ex("Escribe 0,25 como fracción simplificada.", "1/4", "25/100 se divide por 25."),
        ex("Escribe 0,8 como fracción simplificada.", "4/5", "8/10 se divide por 2."),
        ex("Escribe 3/5 como decimal.", "0,6", "3/5 = 6/10."),
    ],
    app=[
        ex("Una receta pide 3/4 de kilogramo de harina. ¿Qué número debe marcar la balanza digital?", "0,75 kilogramos", "3/4 = 75/100."),
        ex("Una cinta mide 0,6 metros. Escríbelo como fracción simplificada.", "3/5 de metro", "6/10 se divide por 2."),
        ex("¿Qué es mayor: 3/5 de kilogramo o 0,55 kilogramos?", "3/5 de kilogramo", "3/5 = 0,6 y 0,6 > 0,55."),
    ],
    rea=[
        ex("Beto escribe 3/5 = 0,35. ¿Cuál es el error y cuál es el decimal correcto?", "Juntó 3 y 5; es 0,6", "3/5 = 6/10."),
        ex("Carla dice que 0,5 de litro y 1/2 litro son lo mismo. ¿Es correcto?", "Sí", "1/2 = 5/10 = 0,5."),
    ],
    cha=[
        ex("Ordena de menor a mayor 1/4, 0,3 y 1/2.", "1/4 < 0,3 < 1/2", "En decimales: 0,25; 0,3 y 0,5."),
        ex("¿Qué decimal es 7/2?", "3,5", "7/2 = 3 1/2 y 1/2 = 0,5."),
    ],
    ctx=[ex("Una jarra ficticia contiene 0,3 litros y otra 1/4 de litro. ¿Cuál contiene más?", "La de 0,3 litros", "1/4 = 0,25 y 0,3 = 0,30 > 0,25.")],
    sc=[
        ex("Escribe 0,5 como fracción simplificada.", "1/2", "5/10 se divide por 5."),
        ex("Escribe 1/4 de kilogramo como decimal.", "0,25", "1/4 = 25/100 = 0,25."),
        ex("¿Qué es mayor, 0,4 o 1/2?", "1/2", "1/2 = 0,5."),
    ],
    op=task(
        "Elige un caso: (a) una receta que pide 3/4 de kilogramo de azúcar y una balanza digital; (b) una tabla de 0,6 metros y una regla marcada en quintos; (c) una botella de 1/2 litro y una jarra graduada en décimas. Escribe la medida como fracción y como decimal, explica cómo pasaste de una a otra y di dónde usarías cada forma.",
        "(a) 3/4 = 75/100 = 0,75. La balanza digital marcará 0,75 kilogramos. En la receta uso 3/4 porque se escribe así.",
        ["escribe la fracción y el decimal", "explica el paso de una a otra", "dice cuándo usaría cada una"],
        ["fracción y decimal escritos", "explicación"],
        ["juntar cifras", "olvidar la unidad"],
        "Pide que verifique con un dibujo y que explique por qué ambos números valen lo mismo.",
    ),
    reinforce="Escribe las equivalencias de 1/2, 1/4, 3/4, 1/5 y 3/5 en una tabla con fracción y decimal.",
    extend="Explica por qué 0,5 y 5/10 se pueden simplificar hasta 1/2.",
)

# ------------------------------------------------------------------ OA 11 clase 1
lesson(
    OA11, 1,
    use="Aprenderé el valor posicional de las décimas, centésimas y milésimas, y a leer y escribir decimales. Sirve para entender cuánto vale cada cifra después de la coma.",
    prior=["Sé que una décima es 1/10 y una centésima es 1/100.", "Sé que un entero tiene 10 décimas."],
    explain=[
        "Después de la coma decimal hay lugares que valen cada vez menos. El primer lugar son las décimas (1/10), el segundo las centésimas (1/100) y el tercero las milésimas (1/1.000). Cada lugar vale 10 veces menos que el anterior. En 0,305 hay 3 décimas, 0 centésimas y 5 milésimas.",
        "Para leer un decimal, lee el número como si no tuviera coma y di el nombre del último lugar. 0,6 son «seis décimas», 0,45 son «cuarenta y cinco centésimas» y 0,305 son «trescientas cinco milésimas». Un decimal con enteros, como 2,047, se lee «dos enteros cuarenta y siete milésimas».",
        "El cero ocupa un lugar y siempre importa. 0,05 y 0,5 no son iguales: 0,05 son 5 centésimas y 0,5 son 5 décimas. También 0,305 se puede descomponer como 3 décimas + 5 milésimas, o 0,3 + 0,005. Una milésima es 0,001; diez milésimas forman una centésima.",
    ],
    vocab=[("décima", "primer lugar después de la coma, vale 0,1"), ("centésima", "segundo lugar después de la coma, vale 0,01"), ("milésima", "tercer lugar después de la coma, vale 0,001"), ("valor posicional", "lo que vale una cifra según su lugar"), ("descomponer", "separar un número en partes que se suman")],
    worked=[
        W("Leer un decimal", "Lee 0,305.", ["Cifras: 3 décimas, 0 centésimas y 5 milésimas.", "Se lee como 305 y el último lugar son milésimas."], "Trescientas cinco milésimas"),
        W("Valor de una cifra", "¿Qué valor tiene el 7 en 0,172?", ["0,172: 1 décima, 7 centésimas, 2 milésimas.", "El 7 está en el lugar de las centésimas: 7/100."], "0,07"),
    ],
    mistakes=[
        M("Decir que 0,05 y 0,5 son iguales porque tienen un 5.", "El lugar del 5 es distinto: centésimas contra décimas.", "0,05 = 5 centésimas y 0,5 = 5 décimas."),
        M("Leer 0,305 como «tres cero cinco milésimas».", "Se leyeron las cifras sueltas.", "Se lee «trescientas cinco milésimas»."),
    ],
    rec=[
        ex("En 0,6, ¿cuántas décimas hay?", "6", "El 6 está en el lugar de las décimas."),
        ex("¿Cuántas milésimas forman una centésima?", "10", "0,01 = 10 × 0,001."),
        ex("¿Cuánto vale el 5 en 0,5?", "0,5", "Son cinco décimas."),
    ],
    und=[
        ex("¿Qué valor tiene el 7 en 0,172?", "0,07", "El 7 está en las centésimas."),
        ex("Escribe en cifras «ocho milésimas».", "0,008", "Las milésimas son el tercer lugar."),
        ex("¿Cómo se lee 0,45?", "Cuarenta y cinco centésimas", "El último lugar son centésimas."),
    ],
    app=[
        ex("Escribe 0,208 en palabras.", "Doscientas ocho milésimas", "208 en el tercer lugar decimal."),
        ex("Descompón 0,602 en décimas y milésimas.", "6 décimas + 2 milésimas", "Tiene 6 décimas, 0 centésimas y 2 milésimas."),
        ex("Escribe en cifras «tres enteros ciento doce milésimas».", "3,112", "3 enteros y 112 milésimas, que se escribe 0,112."),
    ],
    rea=[
        ex("Rita dice que 0,05 y 0,5 son iguales porque ambos tienen un 5. ¿Está bien?", "No", "0,05 son 5 centésimas y 0,5 son 5 décimas."),
        ex("En 3,478, ¿qué cifra está en el lugar de las milésimas?", "8", "El tercer lugar después de la coma."),
    ],
    cha=[
        ex("¿Cuántas milésimas forman una décima?", "100", "10 centésimas × 10 milésimas = 100."),
        ex("¿Qué decimal tiene 4 décimas, 0 centésimas y 7 milésimas?", "0,407", "Se ponen las tres cifras en orden."),
    ],
    ctx=[ex("Una balanza ficticia marca 1,085 kilogramos. ¿Cuántas milésimas tiene la parte decimal?", "85", "La parte decimal 0,085 son 85 milésimas.")],
    sc=[
        ex("¿Qué valor tiene el 4 en 0,043?", "0,04", "El 4 está en las centésimas."),
        ex("Escribe en cifras «seis centésimas».", "0,06", "Las centésimas son el segundo lugar."),
        ex("¿Cuántas centésimas hay en 0,7?", "70", "7 décimas son 70 centésimas."),
    ],
    op=task(
        "Elige: 0,305, 2,047 o 0,068. Léelo con palabras, indica cuántas décimas, centésimas y milésimas tiene y descompón en suma de sus valores.",
        "0,068: «sesenta y ocho milésimas». 0 décimas, 6 centésimas y 8 milésimas. 0,068 = 0,06 + 0,008.",
        ["lee con palabras", "indica décimas, centésimas y milésimas", "descompone en suma"],
        ["lectura", "descomposición"],
        ["leer cifras sueltas", "poner mal un cero"],
        "Pide que escriba una tabla con los tres lugares y que ubique cada cifra.",
    ),
    reinforce="Escribe una tabla con tres columnas (décimas, centésimas, milésimas) y ubica 0,305, 0,45 y 0,008.",
    extend="Explica por qué cada lugar decimal vale 10 veces menos que el de su izquierda.",
)

# ------------------------------------------------------------------ OA 11 clase 2
lesson(
    OA11, 2,
    use="Aprenderé a comparar dos decimales hasta la milésima. Sirve para saber cuál de dos medidas es mayor.",
    prior=["Sé leer y escribir decimales hasta la milésima.", "Conozco los símbolos < y >."],
    explain=[
        "Para comparar dos decimales, primero compara la parte entera. Si son iguales, compara las décimas, luego las centésimas y luego las milésimas, de izquierda a derecha. La primera cifra distinta decide. Así 0,45 > 0,405 porque 4 = 4, pero en las centésimas 5 > 0.",
        "Un truco útil es agregar ceros a la derecha para que ambos tengan la misma cantidad de cifras decimales. Los ceros a la derecha no cambian el valor: 0,5 = 0,50 = 0,500. Entonces 0,45 se escribe 0,450 y se compara con 0,405: 450 milésimas contra 405 milésimas.",
        "Un error muy común es creer que el decimal con más cifras es mayor. No es así: 0,5 es mayor que 0,125, aunque 125 sea mayor que 5. Para evitarlo, iguala las cifras decimales: 0,500 contra 0,125. Escribe después el símbolo < o > o =.",
    ],
    vocab=[("comparar", "decidir cuál es mayor, menor o igual"), ("cifra decimal", "cifra que está después de la coma"), ("cero a la derecha", "cero escrito al final de la parte decimal que no cambia el valor"), ("igualar", "dejar los dos decimales con la misma cantidad de cifras decimales"), ("primera cifra distinta", "la primera cifra, de izquierda a derecha, que no es igual en los dos números")],
    worked=[
        W("Igualar y comparar", "Compara 0,45 y 0,405.", ["Igualo cifras: 0,450 y 0,405.", "Décimas: 4 = 4. Centésimas: 5 > 0.", "0,450 > 0,405."], "0,45 > 0,405"),
        W("Con enteros distintos de cero", "Compara 1,2 y 1,09.", ["Enteros: 1 = 1.", "Igualo: 1,20 y 1,09. Décimas: 2 > 0.", "1,20 > 1,09."], "1,2 > 1,09"),
    ],
    mistakes=[
        M("Decir que 0,125 > 0,5 porque 125 > 5.", "Se compararon como si fueran naturales sin ver los lugares.", "0,500 > 0,125: las 5 décimas superan a 1 décima."),
        M("Decir que 0,5 < 0,50 porque 0,50 tiene más cifras.", "Los ceros a la derecha no cambian el valor.", "0,5 = 0,50."),
    ],
    rec=[
        ex("Escribe 0,5 con tres cifras decimales.", "0,500", "Se agregan ceros a la derecha sin cambiar el valor."),
        ex("¿Cuál es mayor, 0,5 o 0,05?", "0,5", "5 décimas son más que 5 centésimas."),
        ex("Escribe <, > o = : 0,3 __ 0,30.", "=", "0,3 y 0,30 valen lo mismo."),
    ],
    und=[
        ex("Compara 0,72 y 0,702 con < o >.", "0,72 > 0,702", "0,720 > 0,702."),
        ex("Compara 0,3 y 0,29 con < o >.", "0,3 > 0,29", "0,30 > 0,29."),
        ex("Compara 2,4 y 2,04 con < o >.", "2,4 > 2,04", "2,40 > 2,04."),
    ],
    app=[
        ex("Compara 2,305 y 2,35.", "2,305 < 2,35", "2,305 < 2,350."),
        ex("Una botella tiene 1,5 litros y otra 1,45 litros. ¿Cuál tiene más?", "La de 1,5 litros", "1,50 > 1,45."),
        ex("Dos tiras miden 0,8 metros y 0,75 metros. ¿Cuál es más larga?", "La de 0,8 metros", "0,80 > 0,75."),
    ],
    rea=[
        ex("Rita dice que 0,125 > 0,5 porque 125 > 5. ¿Está bien?", "No", "0,500 > 0,125."),
        ex("¿Son iguales 0,70 y 0,7?", "Sí", "Un cero a la derecha no cambia el valor."),
    ],
    cha=[
        ex("¿Qué cifra puede ir en 0,3_ para que el decimal sea mayor que 0,35 y menor que 0,37?", "6", "0,36 está entre 0,35 y 0,37."),
        ex("¿Cuántos decimales con tres cifras decimales hay entre 0,41 y 0,42, sin contarlos?", "9", "Son 0,411 hasta 0,419."),
    ],
    ctx=[ex("En una carrera ficticia, Ana tardó 12,48 segundos y Bea 12,5 segundos. ¿Quién tardó más?", "Bea", "12,50 > 12,48.")],
    sc=[
        ex("Compara 0,6 y 0,59.", "0,6 > 0,59", "0,60 > 0,59."),
        ex("Compara 3,07 y 3,7.", "3,07 < 3,7", "3,07 < 3,70."),
        ex("Escribe 0,8 con dos cifras decimales.", "0,80", "Se agrega un cero a la derecha."),
    ],
    op=task(
        "Elige uno de estos pares: 0,6 y 0,59; 0,405 y 0,45; 1,02 y 1,2. Iguala las cifras decimales con ceros, compara cifra a cifra, escribe el símbolo y explica por qué no basta con mirar cuántas cifras tienen.",
        "0,405 y 0,45: igualo a 0,405 y 0,450. Décimas iguales; centésimas 0 < 5. Entonces 0,405 < 0,45. No basta ver que 0,405 tiene más cifras porque cada lugar vale distinto.",
        ["iguala las cifras decimales", "compara de izquierda a derecha", "explica el error de contar cifras"],
        ["decimales igualados", "símbolo", "frase"],
        ["creer que más cifras es mayor", "comparar como naturales"],
        "Pide que escriba los dos decimales con las mismas cifras decimales y que subraye la primera cifra distinta.",
    ),
    reinforce="Compara 0,3 y 0,30; 0,4 y 0,04; 0,25 y 0,3 con < o > o =.",
    extend="Explica por qué agregar un cero a la derecha de un decimal no cambia su valor.",
)

# ------------------------------------------------------------------ OA 11 clase 3
lesson(
    OA11, 3,
    use="Aprenderé a ordenar varios decimales de menor a mayor y de mayor a menor, y a ubicarlos en la recta numérica. Sirve para ordenar medidas y resultados.",
    prior=["Sé comparar dos decimales.", "Sé igualar cifras decimales con ceros."],
    explain=[
        "Para ordenar varios decimales, iguala la cantidad de cifras decimales de todos agregando ceros a la derecha. Luego compáralos de izquierda a derecha. Por ejemplo, 0,5; 0,45; 0,405 y 0,054 se escriben 0,500; 0,450; 0,405 y 0,054. Las milésimas se leen como números naturales: 500, 450, 405 y 54.",
        "El orden creciente va de menor a mayor: 0,054 < 0,405 < 0,45 < 0,5. El orden decreciente va de mayor a menor: 0,5 > 0,45 > 0,405 > 0,054. Escribe los símbolos < o > entre los números y revisa que todos apunten en el mismo sentido.",
        "También puedes ubicar los decimales en una recta numérica. Entre dos enteros consecutivos hay 10 décimas; entre dos décimas consecutivas hay 10 centésimas. Los números más pequeños quedan más a la izquierda y los mayores más a la derecha. Cuando dos decimales se parecen, mira la primera cifra distinta.",
    ],
    vocab=[("orden creciente", "de menor a mayor"), ("orden decreciente", "de mayor a menor"), ("recta numérica", "línea donde los números se ubican en orden"), ("igualar cifras", "agregar ceros a la derecha hasta que todos tengan las mismas cifras decimales"), ("primera cifra distinta", "la que decide cuál es mayor")],
    worked=[
        W("Ordenar de menor a mayor", "Ordena de menor a mayor 0,5; 0,45; 0,405 y 0,054.", ["Igualo a tres cifras: 0,500; 0,450; 0,405; 0,054.", "Comparo como 500, 450, 405 y 54.", "Menor 54, luego 405, 450 y 500."], "0,054 < 0,405 < 0,45 < 0,5"),
        W("Ordenar de mayor a menor", "Ordena de mayor a menor 1,2; 1,02; 1,002 y 1,21.", ["Igualo: 1,200; 1,020; 1,002; 1,210.", "Comparo como 1.200, 1.020, 1.002 y 1.210.", "El mayor es 1.210, luego 1.200, 1.020 y 1.002."], "1,21 > 1,2 > 1,02 > 1,002"),
    ],
    mistakes=[
        M("Ordenar 0,3; 0,25 y 0,125 de menor a mayor como 0,3 < 0,25 < 0,125 porque 3 < 25 < 125.", "Se comparó cada decimal como natural sin igualar cifras.", "0,300; 0,250 y 0,125: el orden es 0,125 < 0,25 < 0,3."),
        M("Escribir 0,6; 0,56; 0,506 como orden de menor a mayor.", "Esa lista va de mayor a menor.", "De menor a mayor es 0,506 < 0,56 < 0,6."),
    ],
    rec=[
        ex("Ordena de menor a mayor 0,2; 0,5 y 0,1.", "0,1 < 0,2 < 0,5", "1, 2 y 5 décimas."),
        ex("¿Cuál es el menor: 0,04; 0,4 o 0,14?", "0,04", "4 centésimas es lo menor."),
        ex("En orden decreciente, ¿el mayor va primero o último?", "Primero", "Decreciente es de mayor a menor."),
    ],
    und=[
        ex("Ordena de menor a mayor 0,9; 0,19; 0,109 y 0,91.", "0,109 < 0,19 < 0,9 < 0,91", "En milésimas: 109, 190, 900 y 910."),
        ex("Ordena de mayor a menor 2,3; 2,03; 2,33 y 2,303.", "2,33 > 2,303 > 2,3 > 2,03", "En milésimas: 2.330, 2.303, 2.300 y 2.030."),
        ex("Ordena de menor a mayor 0,6; 0,603 y 0,63.", "0,6 < 0,603 < 0,63", "En milésimas: 600, 603 y 630."),
    ],
    app=[
        ex("Cuatro paquetes pesan 1,25; 1,2; 1,205 y 1,52 kilogramos. Ordena de menor a mayor.", "1,2 < 1,205 < 1,25 < 1,52", "En milésimas: 1.200, 1.205, 1.250 y 1.520."),
        ex("Tres plantas miden 0,45 m, 0,5 m y 0,405 m. ¿Cuál es la más alta?", "La de 0,5 m", "0,500 es el mayor."),
        ex("Ordena de mayor a menor 3,5; 3,05; 3,55 y 3,005.", "3,55 > 3,5 > 3,05 > 3,005", "En milésimas: 3.550, 3.500, 3.050 y 3.005."),
    ],
    rea=[
        ex("Pablo ordenó 0,3; 0,25 y 0,125 de menor a mayor como 0,125 < 0,25 < 0,3. ¿Está bien?", "Sí", "En milésimas: 125, 250 y 300."),
        ex("Ana escribió 0,6 < 0,56 < 0,506. ¿Está bien ordenada?", "No", "0,6 no es menor que 0,56; de menor a mayor es 0,506 < 0,56 < 0,6."),
    ],
    cha=[
        ex("¿Cuál de estos decimales está entre 0,4 y 0,5: 0,39; 0,45; 0,5 o 0,51?", "0,45", "0,400 < 0,450 < 0,500."),
        ex("Escribe un decimal con exactamente dos cifras decimales que esté entre 0,3 y 0,32.", "0,31", "0,30 < 0,31 < 0,32."),
    ],
    ctx=[ex("Cuatro corredores ficticios registran 11,95; 12,05; 11,9 y 12,5 segundos. Ordénalos de menor a mayor tiempo.", "11,9 < 11,95 < 12,05 < 12,5", "En centésimas: 1.190, 1.195, 1.205 y 1.250.")],
    sc=[
        ex("Ordena de menor a mayor 0,7; 0,07 y 0,17.", "0,07 < 0,17 < 0,7", "En centésimas: 7, 17 y 70."),
        ex("¿Cuál es el mayor entre 2,31; 2,3 y 2,013?", "2,31", "2,310 > 2,300 > 2,013."),
        ex("Ordena de mayor a menor 0,9; 0,89 y 0,099.", "0,9 > 0,89 > 0,099", "En milésimas: 900, 890 y 99."),
    ],
    op=task(
        "Usa estas cuatro medidas ficticias de longitud: 0,4 m, 0,41 m, 0,041 m y 0,14 m. Ordénalas de menor a mayor, escribe el orden con símbolos, ubícalas en una recta de 0 a 0,5 y explica cómo igualaste las cifras.",
        "Igualo a tres cifras: 0,400; 0,410; 0,041; 0,140. Orden: 0,041 < 0,14 < 0,4 < 0,41. En la recta, 0,041 queda muy cerca del 0 y 0,41 cerca del 0,4.",
        ["iguala las cifras decimales", "ordena correctamente", "ubica en una recta"],
        ["orden con símbolos", "recta dibujada", "frase de explicación"],
        ["ordenar como naturales", "confundir creciente y decreciente"],
        "Pide que lea la lista final en voz alta como milésimas y que revise la recta.",
    ),
    reinforce="Escribe cinco decimales de tres cifras (como 0,3; 0,25; 0,125; 0,05; 0,5) y ordénalos de menor a mayor.",
    extend="Explica por qué 0,9 es mayor que 0,89 aunque 89 sea mayor que 9.",
)

# ------------------------------------------------------------------ OA 11 clase 4
lesson(
    OA11, 4,
    use="Aprenderé a comparar y ordenar decimales en situaciones nuevas, como tiempos de carrera, medidas y precios, y a encontrar decimales entre dos números. Sirve para decidir con datos reales.",
    prior=["Sé comparar y ordenar decimales hasta la milésima."],
    explain=[
        "En los problemas con decimales hay que leer bien qué se pide. En una carrera gana quien tiene el menor tiempo, no el mayor. En una medida de peso o de largo, «más pesado» o «más largo» es el mayor valor. Lee la pregunta antes de comparar.",
        "Para encontrar un decimal entre dos decimales, iguala las cifras decimales y agrega una cifra más si hace falta. Entre 0,3 y 0,4 hay muchos decimales, como 0,35. Entre 0,41 y 0,42 hay 9 decimales con tres cifras decimales: 0,411 hasta 0,419. Siempre se puede encontrar otro decimal entre dos decimales.",
        "Cuando falta una cifra, pruébalas todas comparando con los extremos. En 0,3_ > 0,35 y < 0,37, solo la cifra 6 cumple. Al final, comprueba tu respuesta con la recta numérica o con la lista ordenada y escribe una frase que responda a la pregunta con la unidad.",
    ],
    vocab=[("tiempo menor", "el que tardó menos y gana una carrera"), ("entre", "mayor que uno y menor que el otro"), ("cifra que falta", "dígito que hay que descubrir"), ("unidad", "lo que se mide, como segundos o metros"), ("comprobar", "revisar el resultado de otra forma")],
    worked=[
        W("Leer bien la pregunta", "Tres corredores tardan 12,48; 12,5 y 12,05 segundos. ¿Quién gana la carrera?", ["Gana el menor tiempo.", "Igualo: 12,48; 12,50; 12,05.", "El menor es 12,05."], "El de 12,05 segundos"),
        W("Decimal entre dos decimales", "Escribe un decimal entre 0,3 y 0,4.", ["Igualo a dos cifras: 0,30 y 0,40.", "Entre ellos está 0,35."], "0,35 (también sirven otros, como 0,31 hasta 0,39)"),
    ],
    mistakes=[
        M("Decir que gana el corredor con 12,5 segundos porque 12,5 es el mayor.", "En una carrera gana quien tarda menos.", "Gana el menor tiempo: 12,05 s."),
        M("Decir que no hay decimales entre 0,41 y 0,42.", "Se pensó que solo existen números de dos cifras decimales.", "Hay 0,411; 0,412; 0,413 y así hasta 0,419."),
    ],
    rec=[
        ex("En una carrera, ¿gana quien tiene el mayor o el menor tiempo?", "El menor tiempo", "Quien tarda menos llega primero."),
        ex("¿Cuál tiempo es menor: 12,5 s o 12,05 s?", "12,05 s", "12,50 > 12,05."),
        ex("¿Está 0,35 entre 0,3 y 0,4?", "Sí", "0,30 < 0,35 < 0,40."),
    ],
    und=[
        ex("Tres nadadores ficticios tardan 31,4; 31,04 y 31,44 segundos. ¿Quién gana?", "El de 31,04 segundos", "31,40; 31,04 y 31,44: el menor tiempo es 31,04."),
        ex("Escribe un decimal con dos cifras decimales que esté entre 0,3 y 0,4 y sea mayor que 0,38.", "0,39", "0,38 < 0,39 < 0,40."),
        ex("¿Qué cifra falta en 0,4_ para que 0,4_ sea mayor que 0,47 y menor que 0,49?", "8", "0,47 < 0,48 < 0,49."),
    ],
    app=[
        ex("Dos cintas miden 1,08 m y 1,8 m. ¿Cuál es más larga y cuánto mide la más corta?", "La de 1,8 m; la más corta mide 1,08 m", "1,80 > 1,08."),
        ex("Tres tramos de una ruta miden 2,5 km; 2,05 km y 2,15 km. Ordénalos de menor a mayor.", "2,05 < 2,15 < 2,5", "En centésimas: 205, 215 y 250."),
        ex("Ordena de mayor a menor las alturas 1,45 m; 1,5 m y 1,405 m.", "1,5 > 1,45 > 1,405", "En milésimas: 1.500, 1.450 y 1.405."),
    ],
    rea=[
        ex("Lola dice que gana la carrera quien tiene 12,5 segundos porque 12,5 es el mayor de 12,05; 12,48 y 12,5. ¿Está bien?", "No", "Gana el menor tiempo, 12,05 s."),
        ex("¿Cuántos decimales con dos cifras decimales hay entre 0,5 y 0,6, sin contarlos?", "9", "Son 0,51 hasta 0,59."),
    ],
    cha=[
        ex("Hay cuatro tarjetas con los decimales 0,3; 0,03; 0,303 y 0,33. ¿Cuál es el segundo menor?", "0,3", "Orden: 0,03 < 0,3 < 0,303 < 0,33."),
        ex("¿Qué cifra falta en 5,_07 para que sea mayor que 5,5 y menor que 5,6?", "5", "5,507 está entre 5,500 y 5,600."),
    ],
    ctx=[ex("Dos deportistas ficticios saltan 5,08 m y 5,8 m. ¿Quién saltó más lejos?", "El de 5,8 m", "5,80 > 5,08.")],
    sc=[
        ex("¿Cuál tiempo gana: 9,85 s o 9,8 s?", "9,8 s", "9,80 < 9,85."),
        ex("¿Está 1,25 entre 1,2 y 1,3?", "Sí", "1,20 < 1,25 < 1,30."),
        ex("Ordena de menor a mayor 2,5; 2,05 y 2,55.", "2,05 < 2,5 < 2,55", "En centésimas: 205, 250 y 255."),
    ],
    op=task(
        "Usa estos datos ficticios de un salto de longitud: 4,85 m, 4,8 m, 4,085 m y 4,58 m. Ordena de la menor a la mayor distancia, escribe quién ganó y encuentra un decimal que esté entre las dos marcas más grandes. Explica cómo comparaste.",
        "En milésimas: 4.850; 4.800; 4.085; 4.580. Orden: 4,085 < 4,58 < 4,8 < 4,85. Ganó quien saltó 4,85 m. Entre 4,8 y 4,85 está 4,82. Igualé las cifras decimales y comparé de izquierda a derecha.",
        ["ordena correctamente", "responde quién ganó", "encuentra un decimal entre dos"],
        ["orden", "frase", "decimal entre dos"],
        ["confundir menor y mayor en el contexto", "no igualar cifras"],
        "Pide que lea la pregunta antes de comparar y que compruebe el decimal intermedio con ceros a la derecha.",
    ),
    reinforce="Escribe tres tiempos de carrera ficticios con decimales y di cuál ganaría.",
    extend="Explica por qué siempre se puede encontrar otro decimal entre dos decimales distintos.",
)
