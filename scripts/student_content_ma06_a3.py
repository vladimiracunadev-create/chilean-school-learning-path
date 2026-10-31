"""Cuaderno del estudiante de 6.º básico Matemática: OA 05 (fracciones impropias y números mixtos) y OA 06 (adición y sustracción de fracciones)."""
from __future__ import annotations

from student_lessons import ex
from student_content_ma06_a import M, W, lesson, task

OA5 = "MA06 OA 05"

# ------------------------------------------------------------------ OA 05 clase 1
lesson(
    OA5, 1,
    use="Aprenderé qué es una fracción impropia y cómo se ve en un dibujo. Sirve para escribir cantidades mayores que un entero, como 7 cuartos de pizza.",
    prior=["Sé que una fracción tiene numerador y denominador.", "Sé representar fracciones propias en una barra."],
    explain=[
        "En una fracción, el denominador dice en cuántas partes iguales se dividió una unidad y el numerador dice cuántas de esas partes se toman. Si el numerador es menor que el denominador, la fracción es propia y es menor que 1 entero, como 3/5. Si el numerador es mayor o igual que el denominador, la fracción es impropia y vale 1 entero o más, como 7/4.",
        "Cuando una fracción es impropia, una sola unidad no alcanza para dibujarla. Para 7/4 necesitas dos barras divididas en 4 partes iguales: pintas las 4 partes de la primera barra y 3 partes de la segunda. Cuatro cuartos forman un entero, porque 4/4 = 1. Por eso 7/4 es 1 entero y 3 cuartos.",
        "Cuando el numerador y el denominador son iguales, la fracción es igual a 1, como 9/9. Si el numerador es el doble del denominador, vale 2 enteros, como 10/5. Una fracción impropia no es una fracción «mal escrita»: sirve para decir con exactitud una cantidad que pasa de un entero.",
    ],
    vocab=[("fracción propia", "fracción menor que 1; su numerador es menor que el denominador"), ("fracción impropia", "fracción mayor o igual que 1; su numerador es mayor o igual que el denominador"), ("numerador", "número de arriba: cuántas partes se toman"), ("denominador", "número de abajo: en cuántas partes iguales se divide la unidad"), ("unidad", "el entero que se divide en partes iguales")],
    worked=[
        W("Dibujar una fracción impropia", "Representa 11/8 de pizza con pizzas cortadas en 8 trozos iguales.", ["Una pizza completa tiene 8 trozos; 8/8 es 1 pizza entera.", "Quedan 11 − 8 = 3 trozos, que son 3/8 de otra pizza."], "1 pizza entera y 3/8 de otra"),
        W("Clasificar fracciones", "Clasifica 3/5, 9/9 y 12/7 como propia, impropia o igual a 1.", ["3/5: el numerador 3 es menor que 5, es propia.", "9/9: numerador y denominador iguales, vale 1.", "12/7: el numerador 12 es mayor que 7, es impropia."], "3/5 propia; 9/9 igual a 1; 12/7 impropia"),
    ],
    mistakes=[
        M("Decir que 3/2 es propia porque 3 y 2 son números chicos.", "Se miró el tamaño de los números en vez de comparar numerador con denominador.", "Como 3 es mayor que 2, 3/2 es impropia y vale más de 1."),
        M("Dibujar 7/4 solo con una barra de 4 partes.", "Una sola barra no tiene 7 partes.", "Dibuja dos barras de 4 partes: una completa y la otra con 3 partes pintadas."),
    ],
    rec=[
        ex("De 3/8 y 8/3, ¿cuál es la fracción impropia?", "8/3", "En 8/3 el numerador es mayor que el denominador."),
        ex("Una barra se divide en 4 partes iguales. ¿Cuántas de esas partes forman la barra completa?", "4", "Las 4 partes iguales forman el entero, es decir 4/4 = 1."),
        ex("¿Cuántos enteros vale la fracción 6/6?", "1", "Cuando numerador y denominador son iguales, la fracción vale 1."),
    ],
    und=[
        ex("Cada barra tiene 5 cuadritos iguales. Se pintan 7 cuadritos en total. ¿Qué fracción de una barra se pintó?", "7/5", "Cada cuadrito es 1/5 de barra y hay 7 cuadritos."),
        ex("¿Cuál de estas fracciones es igual a un entero: 4/7, 7/7 o 9/7?", "7/7", "Solo 7/7 tiene numerador igual al denominador."),
        ex("Para tener 10/8 de pizza, ¿cuántas pizzas enteras hay que comprar como mínimo?", "2", "10/8 es más que 1 pizza, pero menos que 2; con una no alcanza."),
    ],
    app=[
        ex("Una jarra se llena con 3 vasos iguales. Se sirvieron 8 vasos de agua. ¿Qué fracción de jarra se sirvió?", "8/3", "Cada vaso es 1/3 de jarra y se sirvieron 8 vasos."),
        ex("De las fracciones 5/9, 11/6, 4/4, 2/7 y 15/8, ¿cuántas son mayores o iguales que 1?", "3", "Cumplen 11/6, 4/4 y 15/8, porque su numerador no es menor que el denominador."),
        ex("Ana comió 5/4 de una barra de chocolate. Para completar 2 barras enteras, ¿cuántos cuartos más necesita?", "3", "2 barras son 8/4 y 8 − 5 = 3 cuartos."),
    ],
    rea=[
        ex("Beto dice que 3/2 es una fracción propia porque 3 y 2 son números pequeños. ¿Qué tipo de fracción es?", "Impropia", "El numerador 3 es mayor que el denominador 2, así que vale más de 1."),
        ex("¿7/7 es una fracción impropia, si impropia significa que el numerador es mayor o igual que el denominador? Responde sí o no.", "Sí", "7 es igual a 7, y 7/7 vale exactamente 1."),
    ],
    cha=[
        ex("¿Cuál es el menor numerador natural que hace que la fracción ?/9 sea impropia?", "9", "Con 9 la fracción 9/9 ya vale 1; con 8 sería menor que 1."),
        ex("Se escriben las fracciones con denominador 4 y numeradores desde 1 hasta 10. ¿Cuántas de ellas son impropias?", "7", "Los numeradores 4, 5, 6, 7, 8, 9 y 10 dan fracciones mayores o iguales que 1."),
    ],
    ctx=[ex("Una receta pide 1/4 de taza de azúcar y se repite 9 veces para una fiesta. ¿Cuántos cuartos de taza se usan en total?", "9/4", "Son 9 veces 1/4, es decir 9 cuartos.")],
    sc=[
        ex("¿13/10 es propia o impropia?", "Impropia", "13 es mayor que 10."),
        ex("Hay 2 barras completas divididas en 3 partes cada una y 1 parte más de otra barra. ¿Cuántos tercios hay?", "7/3", "Cada barra tiene 3 tercios: 3 + 3 + 1 = 7."),
        ex("¿Cuál de 6/6, 6/7 y 7/6 es mayor que 1?", "7/6", "En 7/6 el numerador supera al denominador."),
    ],
    op=task(
        "Dibuja en tu cuaderno barras iguales divididas en 5 partes. Pinta partes para representar 8/5. Escribe cuántas barras necesitaste, cuántas partes pintaste en cada una y si la fracción es propia o impropia. Explica por qué.",
        "Se necesitan 2 barras: la primera con las 5 partes pintadas y la segunda con 3. 8/5 es impropia porque 8 es mayor que 5.",
        ["dibuja barras de partes iguales", "pinta la cantidad correcta", "clasifica y explica con numerador y denominador"],
        ["dibujo de las barras", "frase de clasificación"],
        ["dibujar solo una barra", "confundir numerador y denominador"],
        "Pide que cuente las partes pintadas y compruebe que son 8 en total.",
    ),
    reinforce="Dibuja barras de 3 partes y pinta 5/3. Escribe cuántas barras necesitaste.",
    extend="Explica con un dibujo por qué 12/4 es igual a 3 enteros.",
)

# ------------------------------------------------------------------ OA 05 clase 2
lesson(
    OA5, 2,
    use="Aprenderé a escribir una fracción impropia como número mixto. Sirve para decir cantidades como «2 enteros y 3 cuartos» de manera más fácil de imaginar.",
    prior=["Sé qué es una fracción impropia.", "Sé dividir con cociente y resto."],
    explain=[
        "Un número mixto está formado por un número entero y una fracción propia, como 2 3/4 («dos enteros y tres cuartos»). Cuando escribas un mixto, el entero va a la izquierda de la fracción. Un mixto y una fracción impropia pueden representar la misma cantidad.",
        "Para pasar una fracción impropia a mixto, divide el numerador por el denominador. El cociente es el número de enteros y el resto es el numerador de la fracción que sobra. El denominador no cambia. Por ejemplo, 11/4: 11 ÷ 4 = 2 y sobran 3, entonces 11/4 = 2 3/4.",
        "Si el resto es cero, no queda fracción y el resultado es un entero: 24/6 = 4. Para comprobar, calcula entero × denominador + resto. Con 2 3/4: 2 × 4 + 3 = 11, y el numerador original era 11. Si no coincide, hubo un error.",
    ],
    vocab=[("número mixto", "número formado por un entero y una fracción propia"), ("cociente", "resultado de una división: aquí, el número de enteros"), ("resto", "lo que sobra al dividir: aquí, el numerador de la fracción"), ("entero", "unidad completa"), ("comprobar", "revisar que el resultado es correcto")],
    worked=[
        W("De impropia a mixto", "Escribe 17/5 como número mixto.", ["Divido 17 ÷ 5: el cociente es 3 y el resto es 2.", "Hay 3 enteros y sobran 2 quintos: 3 2/5.", "Compruebo: 3 × 5 + 2 = 17."], "3 2/5"),
        W("Cuando el resto es cero", "Escribe 24/6 como número mixto o entero.", ["Divido 24 ÷ 6: el cociente es 4 y el resto es 0.", "No sobran partes: el resultado es un entero."], "4"),
    ],
    mistakes=[
        M("Escribir 11/3 como 3 1/3.", "Se equivocó el resto: 11 ÷ 3 da 3 y sobran 2, no 1.", "11/3 = 3 2/3. Comprueba: 3 × 3 + 2 = 11."),
        M("Cambiar el denominador al pasar a mixto.", "Se creyó que el denominador es el cociente.", "El denominador no cambia: las partes siguen siendo del mismo tamaño."),
    ],
    rec=[
        ex("¿Cuántos enteros completos hay en 5/4?", "1", "5 ÷ 4 = 1 y sobra 1."),
        ex("Al dividir 7 ÷ 3, ¿cuál es el cociente y cuál es el resto?", "Cociente 2 y resto 1", "3 × 2 = 6 y 7 − 6 = 1."),
        ex("Escribe 7/3 como número mixto.", "2 1/3", "El cociente 2 son los enteros y el resto 1 es el numerador."),
    ],
    und=[
        ex("Escribe 13/5 como número mixto.", "2 3/5", "13 ÷ 5 = 2 y sobran 3."),
        ex("Escribe 19/4 como número mixto.", "4 3/4", "19 ÷ 4 = 4 y sobran 3."),
        ex("Escribe 20/5 como número mixto o entero.", "4", "20 ÷ 5 = 4 y no sobra nada."),
    ],
    app=[
        ex("Escribe 23/6 como número mixto.", "3 5/6", "23 ÷ 6 = 3 y sobran 5."),
        ex("Escribe 31/8 como número mixto.", "3 7/8", "31 ÷ 8 = 3 y sobran 7."),
        ex("Una cinta mide 14/3 metros. Escribe esa medida como número mixto.", "4 2/3 metros", "14 ÷ 3 = 4 y sobran 2."),
    ],
    rea=[
        ex("Mía dice que 11/3 es 3 1/3. ¿Cuál es el número mixto correcto?", "3 2/3", "11 ÷ 3 = 3 y sobran 2; comprobación: 3 × 3 + 2 = 11."),
        ex("¿15/4 y 3 3/4 representan la misma cantidad? Responde sí o no.", "Sí", "3 × 4 + 3 = 15."),
    ],
    cha=[
        ex("¿Entre qué dos enteros consecutivos está la fracción 47/9?", "Entre 5 y 6", "9 × 5 = 45 y 9 × 6 = 54; 47 queda entre ambos."),
        ex("¿Cuál es el mayor numerador menor que 30 para que ?/6 sea un número entero?", "24", "Debe ser múltiplo de 6 y el mayor menor que 30 es 24."),
    ],
    ctx=[ex("Una jarra contiene 17/4 litros de jugo. Escribe esa cantidad como número mixto de litros.", "4 1/4 litros", "17 ÷ 4 = 4 y sobra 1.")],
    sc=[
        ex("Escribe 8/3 como número mixto.", "2 2/3", "8 ÷ 3 = 2 y sobran 2."),
        ex("Escribe 25/5 como número mixto o entero.", "5", "25 ÷ 5 = 5 y no sobra nada."),
        ex("Escribe 22/7 como número mixto.", "3 1/7", "22 ÷ 7 = 3 y sobra 1."),
    ],
    op=task(
        "Elige tres de estas fracciones impropias: 9/2, 14/5, 17/6, 26/8 o 30/7. Escríbelas como números mixtos mostrando la división (cociente y resto). Comprueba con entero × denominador + resto.",
        "Para 14/5: 14 ÷ 5 = 2, resto 4, entonces 2 4/5. Compruebo: 2 × 5 + 4 = 14.",
        ["divide bien el numerador", "usa el resto como numerador", "comprueba el resultado"],
        ["tres divisiones escritas", "tres números mixtos con comprobación"],
        ["equivocarse en el resto", "cambiar el denominador"],
        "Pide que repita la comprobación y que revise que el resto sea menor que el denominador.",
    ),
    reinforce="Escribe 7/2, 9/4 y 11/6 como números mixtos y comprueba cada uno.",
    extend="Busca dos fracciones impropias distintas que den el número mixto 2 1/3 y 3 1/3. Explica cómo las encontraste.",
)

# ------------------------------------------------------------------ OA 05 clase 3
lesson(
    OA5, 3,
    use="Aprenderé a escribir un número mixto como fracción impropia. Sirve para operar con números mixtos y para comprobar equivalencias.",
    prior=["Sé pasar una fracción impropia a número mixto.", "Sé que un entero se puede escribir como fracción."],
    explain=[
        "Un número mixto como 3 2/5 tiene 3 enteros y 2 quintos. Cada entero equivale a 5 quintos, porque 5/5 = 1. Entonces los 3 enteros son 3 × 5 = 15 quintos, y con los 2 quintos más tenemos 17 quintos. Así, 3 2/5 = 17/5.",
        "La regla es: multiplica el entero por el denominador, suma el numerador y deja el mismo denominador. En 3 2/5 haces 3 × 5 + 2 = 17 y escribes 17/5. Esta regla es lo contrario de pasar de impropia a mixto: ahí dividías, aquí multiplicas y sumas.",
        "Esta conversión permite comparar y operar. También permite comprobar: si pasas el mixto a impropia y luego divides, vuelves al mixto de partida. Recuerda que el denominador nunca cambia, porque las partes siguen siendo del mismo tamaño.",
    ],
    vocab=[("equivalente", "que representa la misma cantidad"), ("multiplicar y sumar", "operaciones de la regla: entero × denominador + numerador"), ("quinto", "una de 5 partes iguales"), ("conversión", "cambio de una forma de escribir a otra, sin cambiar el valor"), ("regla", "pasos que siempre se repiten para resolver algo")],
    worked=[
        W("De mixto a impropia", "Escribe 2 3/4 como fracción impropia.", ["Cada entero tiene 4 cuartos; 2 enteros son 2 × 4 = 8 cuartos.", "Sumo los 3 cuartos que ya había: 8 + 3 = 11.", "El denominador se mantiene."], "11/4"),
        W("Otro mixto a impropia", "Escribe 5 1/3 como fracción impropia.", ["5 × 3 = 15, y 15 + 1 = 16.", "Denominador 3."], "16/3"),
    ],
    mistakes=[
        M("Escribir 2 3/5 como 5/5 sumando 2 + 3.", "Se sumó el entero con el numerador sin multiplicar.", "Se multiplica el entero por el denominador y luego se suma: 2 × 5 + 3 = 13, entonces 13/5."),
        M("Cambiar el denominador al convertir.", "Se creyó que el denominador se suma al entero.", "El denominador no cambia: 2 3/5 = 13/5."),
    ],
    rec=[
        ex("¿Cuántos medios hay en 1 entero?", "2", "2/2 = 1."),
        ex("¿Cuántos tercios hay en 2 enteros?", "6", "Cada entero tiene 3 tercios y 2 × 3 = 6."),
        ex("Escribe 1 3/4 como suma 4/4 + 3/4 y da el resultado como una sola fracción.", "7/4", "4 + 3 = 7 cuartos."),
    ],
    und=[
        ex("Escribe 3 2/7 como fracción impropia.", "23/7", "3 × 7 + 2 = 23."),
        ex("Escribe 4 1/5 como fracción impropia.", "21/5", "4 × 5 + 1 = 21."),
        ex("Escribe 6 3/8 como fracción impropia.", "51/8", "6 × 8 + 3 = 51."),
    ],
    app=[
        ex("Escribe 2 5/6 como fracción impropia.", "17/6", "2 × 6 + 5 = 17."),
        ex("Escribe 7 2/9 como fracción impropia.", "65/9", "7 × 9 + 2 = 65."),
        ex("Una receta usa 3 1/2 tazas de harina. ¿Cuántas medias tazas son?", "7", "3 × 2 + 1 = 7 medias tazas."),
    ],
    rea=[
        ex("Tomás dice que 2 3/5 es 5/5 porque 2 + 3 = 5. ¿Cuál es la fracción impropia correcta?", "13/5", "2 × 5 + 3 = 13."),
        ex("¿2 1/4 es igual a 9/4 o a 6/4?", "9/4", "2 × 4 + 1 = 9."),
    ],
    cha=[
        ex("Un número mixto tiene entero 4 y su equivalente impropia es 29/6. ¿Cuál es el número mixto?", "4 5/6", "29 ÷ 6 = 4 y sobran 5."),
        ex("¿Cuál es mayor: 5 1/2 o 10/2?", "5 1/2", "5 1/2 = 11/2, mayor que 10/2."),
    ],
    ctx=[ex("Un bidón contiene 3 3/4 litros de agua y se sirve en vasos de 1/4 de litro. ¿Cuántos vasos se llenan?", "15", "3 × 4 + 3 = 15 cuartos.")],
    sc=[
        ex("Escribe 1 4/5 como fracción impropia.", "9/5", "1 × 5 + 4 = 9."),
        ex("Escribe 8 1/2 como fracción impropia.", "17/2", "8 × 2 + 1 = 17."),
        ex("Escribe 2 7/8 como fracción impropia.", "23/8", "2 × 8 + 7 = 23."),
    ],
    op=task(
        "Elige tres números mixtos de esta lista: 3 1/2, 4 2/3, 2 5/8, 6 3/5 o 1 7/9. Escríbelos como fracciones impropias mostrando la multiplicación y la suma. Luego vuelve a mixto uno de ellos para comprobar.",
        "Para 4 2/3: 4 × 3 + 2 = 14, entonces 14/3. Compruebo: 14 ÷ 3 = 4 y sobran 2, o sea 4 2/3.",
        ["multiplica el entero por el denominador", "suma el numerador", "comprueba volviendo a mixto"],
        ["tres conversiones con cálculo", "una comprobación"],
        ["sumar sin multiplicar", "cambiar el denominador"],
        "Pide que verifique con la división que volvió al mixto del inicio.",
    ),
    reinforce="Escribe 3 1/4, 2 2/3 y 5 1/2 como fracciones impropias. Comprueba cada una dividiendo.",
    extend="Explica con un dibujo de barras por qué 2 3/4 es igual a 11/4.",
)

# ------------------------------------------------------------------ OA 05 clase 4
lesson(
    OA5, 4,
    use="Aprenderé a ubicar fracciones impropias y números mixtos en la recta numérica. Sirve para ver dónde está una cantidad entre dos enteros.",
    prior=["Sé ubicar fracciones propias en una recta.", "Sé pasar entre mixto e impropia."],
    explain=[
        "La recta numérica muestra los números de menor a mayor. Entre cada par de enteros se marcan partes iguales. Si el denominador es 4, cada entero se divide en 4 partes iguales. Para ubicar 7/4, cuenta 7 partes de 1/4 desde el 0: llegas después del 1 y antes del 2.",
        "Con un número mixto, parte del entero. Para 2 1/2, ubica el 2 y avanza una parte de medio hacia el 3. Quedas justo en la mitad entre 2 y 3. Con una fracción impropia, puedes pasarla a mixto: 9/4 = 2 1/4 está un cuarto después del 2.",
        "En la recta, un número está más a la derecha mientras mayor sea. Dos números equivalentes, como 3/2 y 1 1/2, ocupan el mismo punto. Para ubicar con exactitud, primero decide en cuántas partes dividirás cada entero según el denominador.",
    ],
    vocab=[("recta numérica", "línea donde se ubican los números de menor a mayor"), ("marca", "señal en la recta que indica un número"), ("partes iguales", "partes del mismo tamaño"), ("consecutivos", "que van uno después de otro"), ("avanzar", "moverse hacia la derecha en la recta")],
    worked=[
        W("Ubicar una impropia", "En una recta de 0 a 3, cada entero está dividido en 3 partes iguales. ¿Dónde se ubica 7/3?", ["Cada marca avanza 1/3. Cuento 7 marcas desde el 0.", "Tres marcas llegan al 1 y seis marcas al 2; la séptima está después del 2.", "Equivale a 2 1/3."], "Una marca después del 2: 2 1/3"),
        W("Ubicar un mixto", "¿Dónde se ubica 1 3/4 en una recta con cuartos?", ["Parto en el 1.", "Avanzo 3 cuartos hacia el 2, es decir, una marca antes del 2."], "Entre 1 y 2, una marca antes del 2"),
    ],
    mistakes=[
        M("Ubicar 5/3 en el 5 de la recta.", "Se usó el numerador como si fuera un entero.", "5/3 = 1 2/3; está entre 1 y 2."),
        M("Dividir cada entero en una cantidad distinta al denominador.", "Se contaron mal las partes.", "Con denominador 4, cada entero se divide en 4 partes iguales."),
    ],
    rec=[
        ex("En una recta con cada entero dividido en 4 partes iguales, ¿cuántas marcas de 1/4 hay desde el 0 hasta el 2, sin contar el 0?", "8", "Cada entero tiene 4 y hay 2 enteros: 4 + 4 = 8."),
        ex("Un punto está a 5 pasos de 1/4 desde el 0. ¿Qué fracción es?", "5/4", "5 pasos de 1/4 son 5 cuartos."),
        ex("¿Entre qué dos enteros consecutivos está 5/4?", "Entre 1 y 2", "5/4 = 1 1/4."),
    ],
    und=[
        ex("¿Entre qué dos enteros consecutivos está 7/3?", "Entre 2 y 3", "7/3 = 2 1/3."),
        ex("En una recta dividida en quintos, ¿qué número mixto está en la marca 8/5?", "1 3/5", "8 ÷ 5 = 1 y sobran 3."),
        ex("¿A cuántos cuartos del 0 está el punto 2 1/4?", "9", "2 × 4 + 1 = 9 cuartos."),
    ],
    app=[
        ex("En una recta con cada entero dividido en 6, la marca que está 4 partes después del 3 es 3 4/6. Escríbela como fracción impropia.", "22/6", "3 × 6 + 4 = 22."),
        ex("Lucas está en el kilómetro 2 1/2 de una ruta y avanza 3 saltos de 1/2 km. ¿En qué kilómetro queda? Escríbelo como mixto o entero.", "4", "2 1/2 más 3/2 llega a 4 km: 2 1/2 → 3 → 3 1/2 → 4."),
        ex("Ordena de menor a mayor en la recta: 9/4, 1 3/4 y 2.", "1 3/4, 2, 9/4", "1 3/4 = 7/4, 2 = 8/4 y 9/4."),
    ],
    rea=[
        ex("Pía ubicó 5/3 en el 5 de la recta. ¿Entre qué dos enteros debía ubicarla?", "Entre 1 y 2", "5/3 = 1 2/3."),
        ex("Entre el 3 y el 4 hay 4 partes iguales. Rafa dice que la segunda marca después del 3 es 3 1/2. ¿Tiene razón? Responde sí o no.", "Sí", "La segunda marca es 3 2/4, que equivale a 3 1/2."),
    ],
    cha=[
        ex("En una recta con medios, ¿cuántos saltos de 1/2 hay entre 1/2 y 7/2?", "6", "7/2 − 1/2 = 6/2, es decir 6 saltos de medio."),
        ex("¿Cuántos números mixtos con denominador 3 y parte fraccionaria hay entre 1 y 3, sin contar el 1 ni el 3?", "4", "Son 1 1/3, 1 2/3, 2 1/3 y 2 2/3."),
    ],
    ctx=[ex("Una cinta de tela tiene marcas cada 1/4 de metro. Una marca está en la posición 11/4 m. Escribe esa posición como número mixto de metros.", "2 3/4 m", "11 ÷ 4 = 2 y sobran 3.")],
    sc=[
        ex("¿Entre qué dos enteros consecutivos está 9/2?", "Entre 4 y 5", "9/2 = 4 1/2."),
        ex("En una recta dividida en tercios, la marca 1 2/3 corresponde a una fracción impropia. ¿Cuál?", "5/3", "1 × 3 + 2 = 5."),
        ex("¿Cuál está más cerca del 0: 3/2 o 5/4?", "5/4", "5/4 = 1 1/4 es menor que 3/2 = 1 2/4."),
    ],
    op=task(
        "Dibuja una recta numérica de 0 a 4 y divide cada entero en 4 partes iguales. Ubica y rotula los números 3/4, 5/4, 2 1/2 y 15/4. Debajo, escribe cada uno como número mixto o fracción impropia equivalente.",
        "3/4 está en la tercera marca. 5/4 = 1 1/4. 2 1/2 = 10/4 = 2 2/4. 15/4 = 3 3/4.",
        ["recta dividida en cuartos", "ubica correctamente los cuatro números", "escribe las equivalencias"],
        ["recta dibujada y rotulada", "lista de equivalencias"],
        ["dividir mal los enteros", "ubicar el numerador como entero"],
        "Pide que cuente las marcas desde el 0 para comprobar cada ubicación.",
    ),
    reinforce="Dibuja una recta de 0 a 3 con cada entero dividido en 2 partes. Ubica 1/2, 3/2 y 5/2.",
    extend="Ubica 7/3 y 2 1/3 en una misma recta. Explica por qué ocupan el mismo punto.",
)

# ------------------------------------------------------------------ OA 05 clase 5
lesson(
    OA5, 5,
    use="Aprenderé a comparar y ordenar fracciones impropias y números mixtos y a explicar cómo lo hice. Sirve para saber cuál cantidad es mayor y justificarlo.",
    prior=["Sé pasar entre mixto e impropia.", "Sé comparar fracciones con igual denominador."],
    explain=[
        "Para comparar números mixtos, primero compara los enteros. Si los enteros son distintos, el que tiene el entero mayor es mayor: 4 1/3 es mayor que 3 5/6. Si los enteros son iguales, compara las fracciones: 3 1/2 es mayor que 3 1/4 porque 1/2 es mayor que 1/4.",
        "Para comparar una fracción impropia con un mixto, pasa ambos al mismo formato. Puedes pasar todo a impropias, o todo a mixtos. Si las fracciones tienen distinto denominador, usa fracciones equivalentes: 2/5 = 4/10 y 1/2 = 5/10, entonces 1/2 es mayor que 2/5.",
        "Para comunicar tu decisión, escribe los números en el mismo formato y explica el criterio: «comparé los enteros» o «llevé todo a cuartos». Un buen argumento permite que otra persona repita tu razonamiento y llegue a la misma respuesta.",
    ],
    vocab=[("comparar", "decidir cuál número es mayor, menor o si son iguales"), ("mismo formato", "todos los números escritos como mixtos o todos como impropias"), ("fracciones equivalentes", "fracciones que valen lo mismo con distintos números"), ("criterio", "regla que se usa para decidir"), ("argumento", "explicación que muestra por qué algo es cierto")],
    worked=[
        W("Comparar mixtos", "Compara 3 1/4 y 3 1/2.", ["Los enteros son iguales: 3 y 3.", "Comparo las fracciones: 1/4 y 2/4. Como 2/4 es mayor, 3 1/2 es mayor."], "3 1/4 < 3 1/2"),
        W("Comparar impropia y mixto", "Compara 17/5 y 3 1/2.", ["17/5 = 3 2/5. Los enteros son iguales.", "Comparo 2/5 y 1/2: 4/10 y 5/10. Entonces 2/5 es menor.", "Entonces 3 2/5 < 3 1/2."], "17/5 < 3 1/2"),
    ],
    mistakes=[
        M("Decir que 7/3 es mayor que 3 porque 7 es mayor que 3.", "Se comparó el numerador con el entero.", "7/3 = 2 1/3 y es menor que 3."),
        M("Decir que 2 1/2 es mayor que 2 3/4 porque 2 es menor que 4.", "Se miraron solo los denominadores, sin llevar las fracciones a partes del mismo tamaño.", "1/2 = 2/4 es menor que 3/4, entonces 2 1/2 es menor que 2 3/4."),
    ],
    rec=[
        ex("¿Cuál es mayor, 2 3/4 o 1 3/4?", "2 3/4", "Los enteros son distintos: 2 es mayor que 1."),
        ex("¿Cuál es mayor, 9/5 o 7/5?", "9/5", "Tienen el mismo denominador y 9 es mayor que 7."),
        ex("¿1 1/2 y 3/2 son iguales? Responde sí o no.", "Sí", "1 × 2 + 1 = 3."),
    ],
    und=[
        ex("Ordena de menor a mayor: 7/4, 1 1/4 y 3/2.", "1 1/4, 3/2, 7/4", "En cuartos: 5/4, 6/4 y 7/4."),
        ex("Compara 4 1/3 y 4 2/3 con < o >.", "4 1/3 < 4 2/3", "Los enteros son iguales y 1/3 es menor que 2/3."),
        ex("Compara 13/4 y 3 1/2 con < o >.", "13/4 < 3 1/2", "13/4 = 3 1/4, que es menor que 3 2/4."),
    ],
    app=[
        ex("Una cinta mide 2 2/5 m y otra mide 11/5 m. ¿Cuál es más larga?", "La de 2 2/5 m", "11/5 = 2 1/5, que es menor que 2 2/5."),
        ex("Tres jarras tienen 5/2 L, 2 1/4 L y 11/4 L de jugo. ¿Cuál tiene más?", "La de 11/4 L", "En cuartos: 10/4, 9/4 y 11/4."),
        ex("Entre 1 5/6 y 13/6, ¿cuál es mayor?", "13/6", "13/6 = 2 1/6 y es mayor que 1 5/6."),
    ],
    rea=[
        ex("Eli dice que 7/3 es mayor que 3 porque 7 es mayor que 3. ¿Es verdadero? Responde sí o no.", "No", "7/3 = 2 1/3, que es menor que 3."),
        ex("Dani compara 2 1/2 con 2 3/4. ¿Cuál es mayor?", "2 3/4", "1/2 = 2/4 es menor que 3/4."),
    ],
    cha=[
        ex("¿Cuántas fracciones con denominador 4 hay estrictamente entre 7/4 y 11/4?", "3", "Son 8/4, 9/4 y 10/4."),
        ex("De 4 1/6, 25/6 y 4 1/3, ¿cuál es el mayor?", "4 1/3", "4 1/6 y 25/6 son iguales; 4 1/3 = 4 2/6 es mayor."),
    ],
    ctx=[ex("Tres amigos corrieron 2 1/4 km, 5/2 km y 7/4 km. ¿Cuál corrió más?", "El de 5/2 km", "En cuartos: 9/4, 10/4 y 7/4.")],
    sc=[
        ex("Escribe 10/3 como número mixto.", "3 1/3", "10 ÷ 3 = 3 y sobra 1."),
        ex("¿Qué es mayor, 9/4 o 2 1/2?", "2 1/2", "9/4 = 2 1/4 y 1/2 es mayor que 1/4."),
        ex("Escribe 2 2/3 como fracción impropia.", "8/3", "2 × 3 + 2 = 8."),
    ],
    op=task(
        "Ordena de menor a mayor estos cinco números: 11/4, 2 1/2, 7/3, 3 y 5/2. Escribe todos como números mixtos, ordénalos y explica en dos frases el criterio que usaste.",
        "En mixtos: 11/4 = 2 3/4; 2 1/2; 7/3 = 2 1/3; 3; 5/2 = 2 1/2. Orden: 2 1/3 < 2 1/2 = 5/2 < 2 3/4 < 3. Primero comparé los enteros y luego las fracciones.",
        ["pasa todo al mismo formato", "ordena bien, incluso los iguales", "explica el criterio"],
        ["lista de mixtos", "orden final", "frases de explicación"],
        ["comparar numeradores sin ver el entero", "pasar por alto números iguales"],
        "Pide que compruebe el orden ubicando los números en una recta con sextos o doceavos.",
    ),
    reinforce="Compara 2 1/3 con 2 1/2 y 7/3 con 5/2. Explica cómo decidiste.",
    extend="Escribe tres números entre 2 y 3, uno mixto, uno impropio y uno que puedas escribir de ambas formas. Ordénalos.",
)

# ================================================================== OA 06
OA6 = "MA06 OA 06"

# ------------------------------------------------------------------ OA 06 clase 1
lesson(
    OA6, 1,
    use="Aprenderé a sumar y restar fracciones que tienen el mismo denominador, aunque el resultado pase de un entero. Sirve para juntar o quitar partes del mismo tamaño.",
    prior=["Sé qué es una fracción propia e impropia.", "Sé pasar de impropia a número mixto."],
    explain=[
        "Cuando dos fracciones tienen el mismo denominador, las partes son del mismo tamaño. Entonces solo se suman o se restan los numeradores, y el denominador queda igual. 3/8 + 4/8 = 7/8, porque 3 octavos más 4 octavos son 7 octavos.",
        "El denominador no se suma: 3/8 + 4/8 no es 7/16. El denominador dice el tamaño de las partes y no cambia al juntarlas. En la resta es igual: 11/6 − 5/6 = 6/6, que es 1 entero.",
        "A veces el resultado es una fracción impropia. Entonces se puede dejar así o pasar a número mixto: 7/5 + 4/5 = 11/5 = 2 1/5. También se puede simplificar si es posible: 5/10 = 1/2, porque se divide numerador y denominador por 5. Siempre revisa si el resultado se puede escribir más simple.",
    ],
    vocab=[("sumar fracciones", "juntar partes del mismo tamaño"), ("restar fracciones", "quitar partes del mismo tamaño"), ("simplificar", "dividir numerador y denominador por el mismo número"), ("número mixto", "entero más una fracción propia"), ("denominador", "dice el tamaño de las partes")],
    worked=[
        W("Sumar con igual denominador", "Calcula 3/8 + 4/8.", ["Los denominadores son iguales, así que sumo los numeradores: 3 + 4 = 7.", "El denominador sigue siendo 8."], "7/8"),
        W("Resultado mayor que 1", "Calcula 7/5 + 4/5 y escribe el resultado como número mixto.", ["7 + 4 = 11, así que la suma es 11/5.", "11 ÷ 5 = 2 y sobra 1: 2 1/5."], "11/5 = 2 1/5"),
    ],
    mistakes=[
        M("Calcular 2/5 + 1/5 = 3/10.", "Se sumaron también los denominadores.", "El denominador no cambia: 2/5 + 1/5 = 3/5."),
        M("Dejar 5/10 sin simplificar cuando se pide la fracción más simple.", "Se olvidó revisar si se puede dividir.", "5/10 se divide por 5 y queda 1/2."),
    ],
    rec=[
        ex("Calcula 2/7 + 3/7.", "5/7", "Se suman los numeradores y el denominador queda igual."),
        ex("Calcula 9/10 − 4/10.", "5/10", "9 − 4 = 5 décimos, que equivale a 1/2."),
        ex("Calcula 4/9 + 5/9.", "9/9", "4 + 5 = 9, y 9/9 es 1 entero."),
    ],
    und=[
        ex("Calcula 5/12 + 11/12 y escribe el resultado como número mixto simplificado.", "1 1/3", "16/12 = 1 4/12 = 1 1/3."),
        ex("Calcula 13/8 − 5/8.", "1", "13 − 5 = 8, es decir 8/8 = 1."),
        ex("Calcula 7/9 + 8/9 y escribe el resultado como número mixto simplificado.", "1 2/3", "15/9 = 1 6/9 = 1 2/3."),
    ],
    app=[
        ex("Bebí 3/10 de litro de jugo en la mañana y 5/10 de litro en la tarde. ¿Cuánto bebí en total?", "8/10 de litro (4/5)", "3 + 5 = 8 décimos."),
        ex("Tengo 17/20 de metro de cinta y uso 9/20 de metro. ¿Cuánta cinta me queda?", "8/20 de metro (2/5)", "17 − 9 = 8 veinteavos."),
        ex("Una receta usa 7/6 de taza de agua y luego se agregan 5/6 de taza. ¿Cuántas tazas hay en total?", "2", "12/6 = 2 tazas."),
    ],
    rea=[
        ex("Nico calculó 2/5 + 1/5 = 3/10 sumando también los denominadores. ¿Cuál es el resultado correcto?", "3/5", "Las partes son quintos y siguen siendo quintos."),
        ex("¿La suma 3/4 + 3/4 es una fracción propia o impropia?", "Impropia", "El resultado es 6/4 = 1 1/2, mayor que 1."),
    ],
    cha=[
        ex("¿Qué fracción falta en 5/9 + ? = 14/9? Responde con una fracción.", "9/9", "14 − 5 = 9, que es 9/9 = 1."),
        ex("Dos fracciones con denominador 7 suman 11/7 y su diferencia es 3/7. ¿Cuáles son?", "7/7 y 4/7", "Los numeradores suman 11 y se diferencian en 3: 7 y 4."),
    ],
    ctx=[ex("Una botella tiene 9/12 de litro de agua y se toman 5/12 de litro. ¿Cuánta agua queda?", "4/12 de litro (1/3)", "9 − 5 = 4 doceavos, que se simplifican a 1/3.")],
    sc=[
        ex("Calcula 4/15 + 8/15 y simplifica el resultado.", "4/5", "12/15 se simplifica dividiendo por 3."),
        ex("Calcula 10/11 − 3/11.", "7/11", "10 − 3 = 7."),
        ex("Calcula 9/5 − 4/5.", "1", "5/5 es 1 entero."),
    ],
    op=task(
        "Inventa y resuelve tres cálculos: una suma de fracciones de igual denominador con resultado menor que 1, otra con resultado mayor que 1 (escríbelo como número mixto) y una resta. Usa denominadores entre 5 y 20 y comprueba cada resultado con un dibujo o con la operación inversa.",
        "5/8 + 2/8 = 7/8. 6/7 + 4/7 = 10/7 = 1 3/7. 11/12 − 5/12 = 6/12 = 1/2. Comprobación: 1/2 + 5/12 = 6/12 + 5/12 = 11/12.",
        ["mantiene el denominador", "pasa a mixto cuando corresponde", "comprueba cada resultado"],
        ["tres cálculos escritos", "comprobación"],
        ["sumar los denominadores", "no simplificar"],
        "Pide que compruebe una resta sumando al resultado la fracción que quitó.",
    ),
    reinforce="Calcula 2/9 + 5/9, 8/11 − 3/11 y 6/7 + 3/7. Pasa a mixto el resultado que sea mayor que 1.",
    extend="Explica con un dibujo de barras por qué 5/8 + 6/8 es mayor que 1 y calcula el resultado como mixto.",
)

# ------------------------------------------------------------------ OA 06 clase 2
lesson(
    OA6, 2,
    use="Aprenderé a sumar y restar fracciones con denominadores distintos, de hasta dos dígitos. Sirve para juntar o quitar partes que no son del mismo tamaño.",
    prior=["Sé sumar y restar fracciones de igual denominador.", "Sé encontrar fracciones equivalentes y múltiplos comunes."],
    explain=[
        "Para sumar o restar fracciones con denominadores distintos, primero hay que convertirlas en fracciones equivalentes con el mismo denominador. Ese denominador común debe ser un múltiplo de los dos denominadores. Lo más cómodo es usar el menor múltiplo común.",
        "Para 1/2 + 1/3 el menor múltiplo común de 2 y 3 es 6. Convierto: 1/2 = 3/6 y 1/3 = 2/6. Ahora sí: 3/6 + 2/6 = 5/6. Para 3/4 − 1/6, el múltiplo común es 12: 3/4 = 9/12 y 1/6 = 2/12, y 9/12 − 2/12 = 7/12. Cuando multiplicas el denominador por un número, multiplica también el numerador por el mismo número.",
        "Funciona también con denominadores de dos cifras, como 10, 12, 15 o 20. Al final revisa si el resultado se puede simplificar o escribir como mixto. Una pista para comprobar: la suma debe ser mayor que cada sumando, y la resta menor que el minuendo, que es el número del que se quita.",
    ],
    vocab=[("denominador común", "denominador igual para dos fracciones, múltiplo de ambos denominadores"), ("menor múltiplo común", "el menor número que es múltiplo de dos números"), ("fracción equivalente", "fracción que vale lo mismo con otros números"), ("minuendo", "número del que se quita"), ("sustraendo", "número que se quita")],
    worked=[
        W("Suma con denominadores distintos", "Calcula 1/2 + 1/3.", ["El menor múltiplo común de 2 y 3 es 6.", "1/2 = 3/6 y 1/3 = 2/6.", "3/6 + 2/6 = 5/6."], "5/6"),
        W("Resta con denominadores distintos", "Calcula 3/4 − 1/6.", ["El menor múltiplo común de 4 y 6 es 12.", "3/4 = 9/12 y 1/6 = 2/12.", "9/12 − 2/12 = 7/12."], "7/12"),
    ],
    mistakes=[
        M("Calcular 1/2 + 1/3 = 2/5 sumando arriba y abajo.", "Se sumaron numeradores y denominadores.", "Con denominadores distintos hay que llevar a un denominador común: 1/2 + 1/3 = 5/6."),
        M("Cambiar solo el denominador al amplificar.", "Quedó una fracción que no es equivalente.", "Si multiplicas el denominador por 3, multiplica también el numerador por 3."),
    ],
    rec=[
        ex("Escribe 1/2 con denominador 6.", "3/6", "Se multiplica por 3 arriba y abajo."),
        ex("¿Cuál es el menor múltiplo común de 4 y 6?", "12", "Múltiplos de 4: 4, 8, 12. Múltiplos de 6: 6, 12."),
        ex("Escribe 1/4 con denominador 8.", "2/8", "Se multiplica por 2 arriba y abajo."),
    ],
    und=[
        ex("Calcula 1/4 + 1/8.", "3/8", "1/4 = 2/8, entonces 2/8 + 1/8."),
        ex("Calcula 2/3 + 1/6 y simplifica.", "5/6", "2/3 = 4/6, entonces 4/6 + 1/6 = 5/6."),
        ex("Calcula 5/6 − 1/3 y simplifica.", "1/2", "1/3 = 2/6; 5/6 − 2/6 = 3/6 = 1/2."),
    ],
    app=[
        ex("Calcula 3/10 + 2/5.", "7/10", "2/5 = 4/10, y 3/10 + 4/10 = 7/10."),
        ex("Calcula 7/8 − 1/4.", "5/8", "1/4 = 2/8, y 7/8 − 2/8 = 5/8."),
        ex("Calcula 5/12 + 1/3 y simplifica.", "3/4", "1/3 = 4/12; 5/12 + 4/12 = 9/12 = 3/4."),
    ],
    rea=[
        ex("Ana calculó 1/2 + 1/3 = 2/5 sumando arriba y abajo. ¿Cuál es el resultado correcto?", "5/6", "Con denominador común 6: 3/6 + 2/6."),
        ex("¿1/3 + 1/4 es igual a 7/12? Responde sí o no.", "Sí", "1/3 = 4/12 y 1/4 = 3/12; 4/12 + 3/12 = 7/12."),
    ],
    cha=[
        ex("Calcula 2/15 + 1/10.", "7/30", "El menor múltiplo común es 30: 4/30 + 3/30."),
        ex("Calcula 7/10 − 2/15.", "17/30", "7/10 = 21/30 y 2/15 = 4/30; 21 − 4 = 17."),
    ],
    ctx=[ex("En un estanque ficticio se llenan 2/5 de la capacidad por la mañana y 1/4 por la tarde. ¿Qué fracción de la capacidad quedó llena?", "13/20", "2/5 = 8/20 y 1/4 = 5/20; 8 + 5 = 13.")],
    sc=[
        ex("Calcula 1/2 + 1/6 y simplifica.", "2/3", "1/2 = 3/6; 3/6 + 1/6 = 4/6 = 2/3."),
        ex("Calcula 3/4 − 1/8.", "5/8", "3/4 = 6/8; 6/8 − 1/8."),
        ex("Calcula 5/6 + 1/4 y escribe el resultado como mixto.", "1 1/12", "10/12 + 3/12 = 13/12 = 1 1/12."),
    ],
    op=task(
        "Resuelve estas tres operaciones mostrando cómo encuentras el denominador común: 2/3 + 1/4, 5/6 − 3/8 y 7/10 + 1/15. Explica con una frase qué haces antes de sumar o restar si los denominadores son distintos.",
        "2/3 + 1/4 = 8/12 + 3/12 = 11/12. 5/6 − 3/8 = 20/24 − 9/24 = 11/24. 7/10 + 1/15 = 21/30 + 2/30 = 23/30. Primero busco un denominador común y convierto las fracciones.",
        ["busca un denominador común", "amplifica numerador y denominador", "calcula bien las tres operaciones"],
        ["tres cálculos con pasos", "frase de explicación"],
        ["sumar denominadores", "amplificar solo el denominador"],
        "Pide que compruebe cada resultado con una estimación: la suma debe superar cada sumando.",
    ),
    reinforce="Calcula 1/2 + 1/4, 3/5 − 1/10 y 1/3 + 1/6. Escribe cada denominador común.",
    extend="Busca dos fracciones con denominadores distintos que sumen exactamente 1. Explica cómo las encontraste.",
)

# ------------------------------------------------------------------ OA 06 clase 3
lesson(
    OA6, 3,
    use="Aprenderé a sumar y restar números mixtos. Sirve para operar con cantidades como 2 1/2 metros o 3 1/4 litros.",
    prior=["Sé pasar entre número mixto y fracción impropia.", "Sé sumar y restar fracciones, aun con distinto denominador."],
    explain=[
        "Para sumar números mixtos, suma por separado los enteros y las fracciones. Si la suma de las fracciones pasa de 1, conviértela en mixto y agrega ese entero. Por ejemplo, 2 3/5 + 1 4/5: los enteros suman 3 y las fracciones suman 7/5 = 1 2/5. Entonces el total es 3 + 1 2/5 = 4 2/5.",
        "Para restar números mixtos, resta enteros y fracciones. Si la fracción del primer número es menor que la que quieres restar, descompón un entero del primer número y conviértelo en fracción. En 5 1/4 − 2 3/4, como 1/4 es menor que 3/4, saca un entero de 5: 4 + 4/4 + 1/4 = 4 5/4. Ahora resta: 4 5/4 − 2 3/4 = 2 2/4 = 2 1/2.",
        "Otra manera es pasar los mixtos a fracciones impropias, operar y volver a mixto. Elige la que te resulte más cómoda. Si las fracciones tienen denominadores distintos, primero lleva todo a un denominador común. Comprueba siempre que el resultado tenga sentido con una estimación.",
    ],
    vocab=[("número mixto", "entero más una fracción propia"), ("reagrupar", "convertir un entero en fracción para poder restar"), ("entero", "unidad completa"), ("parte fraccionaria", "la fracción de un número mixto"), ("estimar", "calcular un valor aproximado")],
    worked=[
        W("Sumar mixtos", "Calcula 2 3/5 + 1 4/5.", ["Enteros: 2 + 1 = 3. Fracciones: 3/5 + 4/5 = 7/5 = 1 2/5.", "Junto: 3 + 1 2/5 = 4 2/5."], "4 2/5"),
        W("Restar mixtos con reagrupación", "Calcula 5 1/4 − 2 3/4.", ["Como 1/4 es menor que 3/4, reagrupo un entero: 5 1/4 = 4 5/4.", "Resto: 4 − 2 = 2 y 5/4 − 3/4 = 2/4.", "Resultado: 2 2/4 = 2 1/2."], "2 1/2"),
    ],
    mistakes=[
        M("Calcular 4 1/5 − 1 3/5 como 3 2/5 restando la fracción menor de la mayor.", "Se invirtió la resta de las fracciones.", "1/5 no alcanza para quitar 3/5: reagrupa 4 1/5 = 3 6/5 y resulta 2 3/5."),
        M("Dejar 3 6/4 como resultado final.", "Una parte fraccionaria no puede ser impropia en un mixto.", "6/4 = 1 2/4, entonces el resultado es 4 2/4 = 4 1/2."),
    ],
    rec=[
        ex("Calcula 1 1/5 + 2 2/5.", "3 3/5", "Enteros: 3. Fracciones: 3/5."),
        ex("Calcula 4 5/6 − 1 2/6 y simplifica.", "3 1/2", "Enteros: 3. Fracciones: 3/6 = 1/2."),
        ex("Escribe 7/5 como número mixto.", "1 2/5", "7 ÷ 5 = 1 y sobran 2."),
    ],
    und=[
        ex("Calcula 3 2/7 + 2 4/7.", "5 6/7", "Enteros: 5. Fracciones: 6/7."),
        ex("Calcula 2 5/8 + 1 7/8 y simplifica.", "4 1/2", "Fracciones: 12/8 = 1 4/8. Total: 3 + 1 4/8 = 4 1/2."),
        ex("Calcula 6 7/9 − 2 4/9 y simplifica.", "4 1/3", "Enteros: 4. Fracciones: 3/9 = 1/3."),
    ],
    app=[
        ex("Calcula 5 2/6 − 3 5/6 y simplifica.", "1 1/2", "5 2/6 = 4 8/6; 4 − 3 = 1 y 8/6 − 5/6 = 3/6 = 1/2."),
        ex("Calcula 1 1/2 + 2 1/3.", "3 5/6", "Enteros: 3. Fracciones: 3/6 + 2/6 = 5/6."),
        ex("Calcula 4 3/4 − 1 1/2.", "3 1/4", "1/2 = 2/4; enteros: 3; fracciones: 3/4 − 2/4 = 1/4."),
    ],
    rea=[
        ex("Lalo calculó 4 1/5 − 1 3/5 = 3 2/5. ¿Cuál es el resultado correcto?", "2 3/5", "4 1/5 = 3 6/5; 3 6/5 − 1 3/5 = 2 3/5."),
        ex("Sofi calculó 2 3/4 + 1 3/4 y obtuvo 3 6/4. Escribe el resultado como número mixto con la fracción propia y simplificada.", "4 1/2", "6/4 = 1 2/4, entonces 4 2/4 = 4 1/2."),
    ],
    cha=[
        ex("Calcula 7 − 2 3/8.", "4 5/8", "7 = 6 8/8; 6 8/8 − 2 3/8 = 4 5/8."),
        ex("¿Qué número mixto se suma a 1 3/5 para obtener 4?", "2 2/5", "4 − 1 3/5 = 3 5/5 − 1 3/5 = 2 2/5."),
    ],
    ctx=[ex("Una soga mide 6 1/2 m y se cortan 2 1/4 m. ¿Cuántos metros de soga quedan?", "4 1/4 m", "6 2/4 − 2 1/4 = 4 1/4.")],
    sc=[
        ex("Calcula 3 1/8 + 2 3/8 y simplifica.", "5 1/2", "Fracciones: 4/8 = 1/2."),
        ex("Calcula 5 2/3 − 1 1/3.", "4 1/3", "Enteros: 4. Fracciones: 1/3."),
        ex("Calcula 2 4/5 + 1 2/5.", "4 1/5", "Fracciones: 6/5 = 1 1/5. Total: 3 + 1 1/5."),
    ],
    op=task(
        "Resuelve y comprueba: 2 5/6 + 1 4/6; 5 1/8 − 2 5/8; y 3 1/2 + 1 1/3. En la segunda muestra cómo reagrupas. Estima primero cada resultado redondeando los números mixtos a enteros.",
        "2 5/6 + 1 4/6 = 3 9/6 = 4 1/2 (estimación: 3 + 2 = 5). 5 1/8 − 2 5/8 = 4 9/8 − 2 5/8 = 2 4/8 = 2 1/2 (estimación: 5 − 3 = 2). 3 1/2 + 1 1/3 = 4 5/6 (estimación: 4 + 1 = 5).",
        ["suma enteros y fracciones por separado", "reagrupa cuando hace falta", "estima antes de calcular"],
        ["tres cálculos con pasos", "estimaciones escritas"],
        ["restar al revés las fracciones", "dejar una fracción impropia en el mixto"],
        "Pide que compare la estimación con el resultado y que explique si la diferencia tiene sentido.",
    ),
    reinforce="Calcula 3 1/5 + 1 2/5 y 4 1/3 − 1 2/3. Para la resta reagrupa un entero.",
    extend="Inventa una resta de dos números mixtos con denominador 6 que necesite reagrupar. Resuélvela y compruébala sumando.",
)

# ------------------------------------------------------------------ OA 06 clase 4
lesson(
    OA6, 4,
    use="Aprenderé a resolver problemas con fracciones y números mixtos: cuánto falta, cuánto queda y varios pasos. Sirve para repartir, medir y cocinar.",
    prior=["Sé sumar y restar fracciones y números mixtos.", "Sé escribir un entero como fracción."],
    explain=[
        "En un problema, primero decide la operación. Juntar o agregar se resuelve con una suma. Quitar, comparar o preguntar cuánto falta se resuelve con una resta. Un entero se puede escribir como fracción, como 1 = 12/12, y eso ayuda a calcular lo que falta para completar un entero.",
        "Por ejemplo, si una jarra está llena hasta 3/4, falta 1 − 3/4 = 4/4 − 3/4 = 1/4. Para preguntas con dos o más pasos, resuelve de a un paso y escribe cada resultado. Si hay distintos denominadores, lleva todo a un denominador común.",
        "Al final, comprueba con una estimación y con la operación inversa. Si sumaste, resta uno de los sumandos del resultado; si restaste, suma el resultado con lo que quitaste. Escribe la respuesta con la unidad, como litros o metros.",
    ],
    vocab=[("cuánto falta", "pregunta que se resuelve restando lo que ya se tiene de lo que se necesita"), ("completar", "llegar al entero o a la cantidad total"), ("operación inversa", "la que deshace a otra: la resta deshace la suma"), ("paso", "cada cálculo que se hace dentro de un problema"), ("unidad", "palabra que indica de qué es la cantidad, como litros")],
    worked=[
        W("Cuánto falta", "Una jarra está llena hasta 3/4. ¿Qué fracción falta para llenarla?", ["La jarra llena es 1 entero, es decir 4/4.", "4/4 − 3/4 = 1/4."], "Falta 1/4 de la jarra"),
        W("Problema de dos pasos", "Camilo caminó 1 1/2 km en la mañana y 2 1/3 km en la tarde. Su meta era 5 km. ¿Cuánto le falta?", ["Total caminado: 1 1/2 + 2 1/3 = 1 3/6 + 2 2/6 = 3 5/6.", "Falta: 5 − 3 5/6 = 4 6/6 − 3 5/6 = 1 1/6."], "1 1/6 km"),
    ],
    mistakes=[
        M("Resolver «cuánto más» con una suma.", "No se identificó que comparar dos cantidades se resuelve con una resta.", "Cuánto más tiene A que B es A − B."),
        M("Calcular 1/2 + 1/4 = 2/6.", "Se sumaron arriba y abajo.", "1/2 = 2/4; 2/4 + 1/4 = 3/4."),
    ],
    rec=[
        ex("Si tengo 3/5 de una barra, ¿cuántos quintos me faltan para completarla?", "2/5", "5/5 − 3/5 = 2/5."),
        ex("Escribe 1 como fracción con denominador 8.", "8/8", "Un entero tiene 8 octavos."),
        ex("Calcula 1 − 1/3.", "2/3", "3/3 − 1/3 = 2/3."),
    ],
    und=[
        ex("Hay 5/8 de una pizza. ¿Qué fracción falta para completarla?", "3/8", "8/8 − 5/8 = 3/8."),
        ex("Calcula 2 − 1/4 y escribe el resultado como número mixto.", "1 3/4", "2 = 1 4/4; 1 4/4 − 1/4 = 1 3/4."),
        ex("Calcula 1/2 + 1/2 + 1/4 y escribe el resultado como número mixto.", "1 1/4", "1/2 + 1/2 = 1 y 1 + 1/4."),
    ],
    app=[
        ex("Un estanque está lleno hasta 7/12 de su capacidad y se agrega 1/4 más. ¿Qué fracción de la capacidad queda llena?", "5/6", "1/4 = 3/12; 7/12 + 3/12 = 10/12 = 5/6."),
        ex("Una tela de 3 1/2 m se usa así: primero 1 3/4 m y después 1/2 m. ¿Cuánta tela queda?", "1 1/4 m", "3 2/4 − 1 3/4 = 1 3/4; 1 3/4 − 2/4 = 1 1/4."),
        ex("Pablo corrió 2 2/3 km y Ana 3 1/6 km. ¿Cuántos kilómetros más corrió Ana?", "1/2 km", "3 1/6 − 2 4/6 = 2 7/6 − 2 4/6 = 3/6."),
    ],
    rea=[
        ex("Carla tiene 3/4 de litro de jugo y Diego tiene 1/2 litro. ¿Cuántos litros más tiene Carla?", "1/4 de litro", "Para comparar cuánto más se resta: 3/4 − 2/4."),
        ex("Pía calculó 1/2 + 1/4 = 2/6. ¿Cuál es el resultado correcto?", "3/4", "1/2 = 2/4 y 2/4 + 1/4 = 3/4."),
    ],
    cha=[
        ex("Ana come 1/4 de una torta, Beto 1/3 y Cata 1/6. ¿Qué fracción de la torta sobra?", "1/4", "Comen 3/12 + 4/12 + 2/12 = 9/12; sobra 3/12 = 1/4."),
        ex("Un tanque se llena 2/5 el lunes, 3/10 el martes y 1/4 el miércoles. ¿Qué fracción queda por llenar?", "1/20", "8/20 + 6/20 + 5/20 = 19/20, y faltan 1/20."),
    ],
    ctx=[ex("Una cuerda de 4 m se usa para dos columpios: uno usa 1 3/4 m y el otro 1 1/2 m. ¿Cuánta cuerda sobra?", "3/4 m", "Se usan 1 3/4 + 1 2/4 = 3 1/4 m; sobra 4 − 3 1/4 = 3/4.")],
    sc=[
        ex("Calcula 1 − 5/12.", "7/12", "12/12 − 5/12."),
        ex("Calcula 3/10 + 1/5 y simplifica.", "1/2", "1/5 = 2/10; 3/10 + 2/10 = 5/10 = 1/2."),
        ex("Calcula 2 1/2 − 1 1/4.", "1 1/4", "2 2/4 − 1 1/4."),
    ],
    op=task(
        "Resuelve este problema y explica cada paso: «Una receta de pan lleva 2 1/2 tazas de harina, 3/4 de taza de agua y 1/8 de taza de aceite. Hay una taza grande que mide 4 tazas. ¿Cuánto espacio libre queda en la taza grande si se mezclan todos los ingredientes?». Comprueba el resultado con la operación inversa.",
        "Total: 2 4/8 + 6/8 + 1/8 = 2 11/8 = 3 3/8 tazas. Espacio libre: 4 − 3 3/8 = 5/8 de taza. Comprobación: 3 3/8 + 5/8 = 4.",
        ["elige las operaciones correctas", "usa denominador común", "comprueba con la operación inversa"],
        ["pasos del cálculo", "respuesta con unidad y comprobación"],
        ["no usar denominador común", "olvidar uno de los ingredientes"],
        "Pide que sume el resultado con lo calculado antes y compruebe que da 4 tazas.",
    ),
    reinforce="Una cinta mide 3 m. Se cortan 1 1/2 m y luego 3/4 m. Calcula cuánto queda.",
    extend="Inventa un problema con tres cantidades fraccionarias donde debas sumar y luego restar. Resuélvelo y comprueba.",
)
