"""Cuaderno del estudiante de 7.º básico Matemática: OA 02 (multiplicación y división de fracciones) y OA 03 (problemas con fracciones y decimales)."""
from __future__ import annotations

from student_lessons import ex
from student_content_ma07_a import M, W, cx, lesson, task

OA2 = "MA07 OA 02"
OA3 = "MA07 OA 03"

# ------------------------------------------------------------------ OA 02 clase 1
lesson(
    OA2, 1,
    use="Aprenderé a multiplicar una fracción por un número natural y a calcular la fracción de una cantidad. Sirve para ajustar recetas, medir tramos y repartir cosas.",
    prior=["Sé qué es una fracción y sé sumar fracciones con el mismo denominador.", "Sé simplificar fracciones y escribir números mixtos."],
    explain=[
        "Multiplicar un natural por una fracción es sumar la misma fracción varias veces. Por ejemplo, 3 × 2/5 = 2/5 + 2/5 + 2/5 = 6/5. Fíjate en lo que pasó: el numerador se multiplicó por 3 (2 × 3 = 6) y el denominador quedó igual, porque las partes siguen siendo quintos. La regla es n × a/b = (n × a)/b.",
        "El resultado puede ser mayor que 1. Entonces se puede escribir como número mixto: 6/5 = 1 y 1/5. Si se puede, simplifica: 4 × 3/8 = 12/8 = 3/2. También sirve para calcular la fracción de una cantidad. Para hallar 2/5 de 30, divide 30 en 5 partes iguales (6 cada una) y toma 2 partes: 12. Es lo mismo que 2/5 × 30.",
        "Una barra dibujada ayuda a ver el cálculo. Dibuja una barra, divídela en las partes que indica el denominador y pinta las que indica el numerador. La barra también sirve al revés: si 3 partes de 5 valen 18, cada parte vale 6 y toda la barra vale 30. Siempre pregúntate si el resultado es razonable: una fracción menor que 1 de una cantidad da menos que esa cantidad.",
    ],
    vocab=[("numerador", "número de arriba de una fracción; dice cuántas partes se toman"), ("denominador", "número de abajo; dice en cuántas partes iguales se dividió el entero"), ("fracción de una cantidad", "parte de una cantidad que se calcula con una fracción"), ("número mixto", "número escrito con un entero y una fracción, como 1 y 1/5"), ("simplificar", "dividir numerador y denominador por el mismo número")],
    worked=[
        W("Multiplicar y simplificar", "Calcula 4 × 3/8.", ["Multiplico el numerador por 4: 4 × 3 = 12, y el denominador queda igual: 12/8.", "Simplifico dividiendo por 4: 12/8 = 3/2, que es 1 y 1/2."], "3/2 (es decir, 1 y 1/2)"),
        W("Fracción de una cantidad", "Calcula 3/5 de 40.", ["Divido 40 en 5 partes iguales: 40 ÷ 5 = 8.", "Tomo 3 partes: 3 × 8 = 24."], "24"),
    ],
    mistakes=[
        M("Calcular 3 × 2/9 = 6/27.", "Se multiplicó también el denominador.", "El denominador no cambia, porque las partes siguen siendo novenos: 3 × 2/9 = 6/9 = 2/3."),
        M("Decir que 2/3 de 12 es 6 porque se dividió entre 2.", "Se usó el numerador como si fuera el número de partes.", "Primero se divide en 3 partes (12 ÷ 3 = 4) y luego se toman 2: 8."),
    ],
    rec=[
        ex("Escribe 3 × 1/4 como una suma repetida y da el resultado.", "1/4 + 1/4 + 1/4 = 3/4", "Se suma tres veces un cuarto, así que quedan tres cuartos."),
        cx("¿Cuánto es 5 × 1/6?", "5*F(1,6)", "Cinco veces un sexto son cinco sextos: el numerador se multiplica por 5."),
        ex("¿Cuánto es 1/5 de 20?", "4", "Se divide 20 en 5 partes iguales y cada parte vale 4."),
    ],
    und=[
        cx("Calcula 2 × 3/7.", "2*F(3,7)", "Se multiplica el numerador: 2 × 3 = 6, sobre 7."),
        cx("Calcula 4 × 5/6 y escribe el resultado simplificado.", "4*F(5,6)", "4 × 5 = 20, así que 20/6, y dividiendo por 2 queda 10/3.", form="both"),
        ex("Calcula 3/4 de 28.", "21", "28 ÷ 4 = 7 es cada cuarto y 3 × 7 = 21."),
    ],
    app=[
        cx("Una receta de ejemplo usa 3/4 de taza de harina por porción. ¿Cuántas tazas se necesitan para 6 porciones?", "6*F(3,4)", "6 × 3 = 18 cuartos de taza, que simplificado es 9/2.", unit=" tazas", form="both"),
        ex("Una cinta mide 56 cm y se usan 3/8 de ella para un lazo. ¿Cuántos centímetros se usan?", "21 cm", "56 ÷ 8 = 7 cm cada octavo, y 3 × 7 = 21 cm."),
        cx("Mariana trota 2/5 de kilómetro cada día durante 7 días. ¿Cuántos kilómetros trota en total?", "7*F(2,5)", "7 × 2 = 14 quintos de kilómetro, o sea 14/5.", unit=" km", form="both"),
    ],
    rea=[
        ex("Juan calculó 5 × 2/9 = 10/45. ¿Está bien? Si no, escribe el resultado correcto.", "No; es 10/9", "El denominador no se multiplica: son 10 novenos, que es 10/9."),
        ex("¿Verdadero o falso? «Al multiplicar 5 por una fracción menor que 1, el resultado es mayor que 5».", "Falso", "Tomar solo una parte de cada uno de los 5 enteros da menos de 5; por ejemplo 5 × 1/2 = 5/2."),
    ],
    cha=[
        cx("Un número x cumple que 6 × x = 3/2 y x es una fracción con numerador 1. ¿Cuál es x?", "F(1,4)", "Con numerador 1, 6 × 1/d = 6/d; para que sea 3/2 = 6/4, el denominador es 4."),
        ex("Se pintan 3 partes de 5 partes iguales de una cinta, y la parte pintada mide 18 cm. ¿Cuánto mide la cinta completa?", "30 cm", "Si 3 partes miden 18 cm, cada parte mide 6 cm; con 5 partes son 30 cm."),
    ],
    ctx=[cx("Para un pastel de ejemplo se necesitan 2/3 de taza de azúcar. Si se hacen 5 pasteles iguales, ¿cuántas tazas de azúcar se necesitan?", "5*F(2,3)", "5 × 2 = 10 tercios de taza, que son 10/3.", unit=" tazas", form="both")],
    sc=[
        cx("Calcula 3 × 2/5.", "3*F(2,5)", "Se multiplica el numerador: 3 × 2 = 6, sobre 5."),
        ex("¿Cuánto es 1/7 de 35?", "5", "35 ÷ 7 = 5."),
        ex("¿Cuánto es 3/8 de 24?", "9", "24 ÷ 8 = 3 y 3 × 3 = 9."),
    ],
    op=task(
        "Una pastelería de ejemplo hace una torta con estas cantidades por torta: 3/4 de taza de mantequilla, 2/3 de taza de azúcar y 5/6 de taza de leche. Calcula cuánto de cada ingrediente se necesita para 4 tortas. Escribe cada resultado simplificado y como número mixto, y dibuja una barra para uno de ellos.",
        "Mantequilla: 4 × 3/4 = 12/4 = 3 tazas. Azúcar: 4 × 2/3 = 8/3 = 2 y 2/3 tazas. Leche: 4 × 5/6 = 20/6 = 10/3 = 3 y 1/3 tazas.",
        ["multiplica bien los tres ingredientes", "simplifica y escribe el número mixto", "dibuja una barra que represente un cálculo"],
        ["tres cálculos en el cuaderno", "barra dibujada"],
        ["multiplicar también el denominador", "olvidar simplificar el resultado"],
        "Pide que compruebe cada resultado sumando la fracción cuatro veces.",
    ),
    reinforce="Calcula 3 × 1/5, 2 × 3/8 y 4 × 5/6, y dibuja una barra para el primero.",
    extend="Explica con una barra por qué 5 × 3/4 es mayor que 3. Escribe el resultado como número mixto.",
)

# ------------------------------------------------------------------ OA 02 clase 2
lesson(
    OA2, 2,
    use="Aprenderé a multiplicar dos fracciones y a explicar el resultado con un rectángulo. Sirve para calcular «una parte de una parte», como la mitad de un tercio de pizza.",
    prior=["Sé multiplicar una fracción por un natural.", "Sé simplificar fracciones y convertir números mixtos en fracciones."],
    explain=[
        "Multiplicar dos fracciones es calcular una fracción de otra fracción. Para 1/2 × 1/3 (la mitad de un tercio), dibuja un cuadrado de lado 1. Divídelo en 3 columnas y toma una. Luego divide todo en 2 filas y toma una de ellas. La parte doble marcada es 1 de 6 celdas pequeñas, o sea 1/6. En el modelo de área, las celdas totales son denominador × denominador.",
        "La regla es a/b × c/d = (a × c)/(b × d): numerador por numerador y denominador por denominador. Por ejemplo, 2/3 × 3/5 = 6/15, y simplificando por 3 queda 2/5. Puedes simplificar antes de multiplicar: en 3/4 × 2/9 puedes dividir 3 y 9 por 3 y también 2 y 4 por 2, y queda 1/2 × 1/3 = 1/6.",
        "Si un factor es un número mixto, pásalo primero a fracción: 1 y 1/2 es 3/2. Al multiplicar por una fracción menor que 1 el resultado es menor que el otro factor, porque se toma solo una parte. Al multiplicar por una fracción mayor que 1 el resultado es mayor. Comprueba siempre si tu respuesta tiene ese comportamiento.",
    ],
    vocab=[("producto", "resultado de una multiplicación"), ("factor", "cada número que se multiplica"), ("modelo de área", "rectángulo dividido en filas y columnas que muestra un producto"), ("fracción impropia", "fracción con numerador mayor que el denominador, como 7/4"), ("cancelar", "simplificar un numerador con un denominador antes de multiplicar")],
    worked=[
        W("Producto con simplificación", "Calcula 2/3 × 3/5.", ["Multiplico numeradores: 2 × 3 = 6. Multiplico denominadores: 3 × 5 = 15.", "Simplifico 6/15 dividiendo por 3: 2/5."], "2/5"),
        W("Con número mixto", "Calcula 1 y 1/2 × 2/3.", ["Paso el mixto a fracción: 1 y 1/2 = 3/2.", "Multiplico: 3/2 × 2/3 = 6/6 = 1."], "1"),
    ],
    mistakes=[
        M("Calcular 1/2 × 1/4 = 1/2, porque «se deja el denominador mayor».", "Se confundió con la suma de fracciones con igual denominador.", "Los denominadores también se multiplican: 1/2 × 1/4 = 1/8."),
        M("Creer que 1/2 × 1/3 debe dar más que 1/3.", "Se pensó que multiplicar siempre agranda.", "Multiplicar por una fracción menor que 1 achica: la mitad de un tercio es 1/6."),
    ],
    rec=[
        ex("Un cuadrado se divide en 4 columnas y 3 filas iguales. ¿Qué fracción del cuadrado es una sola celda?", "1/12", "Hay 4 × 3 = 12 celdas iguales."),
        cx("Calcula 1/2 × 1/5.", "F(1,2)*F(1,5)", "Numerador 1 × 1 = 1 y denominador 2 × 5 = 10."),
        ex("¿Cuánto es la mitad de 1/4?", "1/8", "Partir en dos un cuarto da octavos: 1/2 × 1/4 = 1/8."),
    ],
    und=[
        cx("Calcula 2/5 × 3/7.", "F(2,5)*F(3,7)", "2 × 3 = 6 y 5 × 7 = 35."),
        cx("Calcula 3/4 × 2/9 y simplifica.", "F(3,4)*F(2,9)", "3 × 2 = 6 y 4 × 9 = 36; 6/36 = 1/6."),
        cx("Calcula 5/6 × 9/10 y simplifica.", "F(5,6)*F(9,10)", "5 × 9 = 45 y 6 × 10 = 60; dividiendo por 15 queda 3/4."),
    ],
    app=[
        cx("Sobran 3/4 de una pizza de ejemplo y alguien come 2/5 de lo que sobra. ¿Qué fracción de la pizza completa comió?", "F(3,4)*F(2,5)", "2/5 de 3/4 es 3/4 × 2/5 = 6/20, que simplificado es 3/10."),
        cx("Un frasco tiene 3/4 de litro de jugo y se usan 2/3 de ese contenido. ¿Cuántos litros se usan?", "F(3,4)*F(2,3)", "3 × 2 = 6 y 4 × 3 = 12; 6/12 = 1/2.", unit=" L"),
        cx("Un terreno rectangular de ejemplo mide 5/6 km de largo y 3/10 km de ancho. ¿Cuántos km² tiene?", "F(5,6)*F(3,10)", "El área es largo × ancho: 15/60 = 1/4.", unit=" km²"),
    ],
    rea=[
        ex("¿Verdadero o falso? «El producto de dos fracciones menores que 1 es siempre mayor que cada una de ellas».", "Falso", "Se toma una parte de una parte: 1/2 × 1/2 = 1/4, que es menor que 1/2."),
        ex("¿Qué es mayor, 3/4 o 3/4 × 2/3?", "3/4", "2/3 es menor que 1, así que el producto (1/2) es menor que 3/4."),
    ],
    cha=[
        cx("Calcula 2 y 1/2 × 1 y 1/5.", "F(5,2)*F(6,5)", "Los mixtos son 5/2 y 6/5; 30/10 = 3."),
        cx("Un cuadrado mide 3/4 m de lado. ¿Cuántos m² tiene?", "F(3,4)*F(3,4)", "El área del cuadrado es lado × lado: 9/16.", unit=" m²"),
    ],
    ctx=[cx("Una receta de ejemplo lleva 3/5 de taza de azúcar. Si solo se prepara la mitad de la receta, ¿cuánta azúcar se necesita?", "F(1,2)*F(3,5)", "La mitad de 3/5 es 1/2 × 3/5 = 3/10.", unit=" de taza")],
    sc=[
        cx("Calcula 3/7 × 1/2.", "F(3,7)*F(1,2)", "3 × 1 = 3 y 7 × 2 = 14."),
        cx("Calcula 4/5 × 5/8.", "F(4,5)*F(5,8)", "20/40 se simplifica a 1/2."),
        ex("¿Cuál es el denominador del producto 1/6 × 1/4?", "24", "Los denominadores se multiplican: 6 × 4 = 24."),
    ],
    op=task(
        "Dibuja un cuadrado de 6 cuadritos por 6 cuadritos. Pinta de azul 2/3 de las columnas y marca con rayas 3/6 de las filas. Usa el dibujo para calcular 2/3 × 1/2 (la parte donde se cruzan) y cuenta cuántas celdas hay en la zona doble. Después calcula con la regla y compara.",
        "Las columnas azules son 4 de 6; las filas rayadas son 3 de 6. La zona doble tiene 4 × 3 = 12 celdas de 36, o sea 12/36 = 1/3. Con la regla: 2/3 × 1/2 = 2/6 = 1/3.",
        ["dibuja el modelo de área con las divisiones correctas", "cuenta bien las celdas de la zona doble", "compara con el cálculo de la regla"],
        ["dibujo en cuadrícula", "cálculo con la regla", "frase de comparación"],
        ["dividir las filas y columnas en cantidades distintas a los denominadores", "sumar las fracciones en vez de multiplicarlas"],
        "Pide que cuente de nuevo las celdas y que simplifique 12/36 paso a paso.",
    ),
    reinforce="Calcula 1/3 × 1/4, 2/5 × 5/6 y 3/8 × 4/9. Simplifica cada resultado.",
    extend="Calcula 2/3 × 3/4 × 4/5 y busca la razón por la que el resultado es tan simple.",
)

# ------------------------------------------------------------------ OA 02 clase 3
lesson(
    OA2, 3,
    use="Aprenderé a dividir con fracciones de dos formas: preguntando «cuántas veces cabe» y repartiendo en partes iguales. Sirve para cortar cintas, servir líquidos y repartir cantidades.",
    prior=["Sé multiplicar fracciones.", "Sé que dividir es repartir o medir cuántas veces cabe una cantidad en otra."],
    explain=[
        "Hay dos significados de dividir. Como medida: 3/4 ÷ 1/8 pregunta cuántos octavos caben en tres cuartos. Como 3/4 = 6/8, caben 6. Como reparto: 3/4 ÷ 3 pregunta cuánto toca a cada uno si se reparten tres cuartos entre 3 personas; cada una recibe 1/4. En los dos casos, la división se puede dibujar con una barra.",
        "La regla práctica usa el recíproco. El recíproco de una fracción se obtiene intercambiando numerador y denominador: el recíproco de 2/5 es 5/2, y el de 4 es 1/4. Dividir es multiplicar por el recíproco del divisor: a/b ÷ c/d = a/b × d/c. Por eso 3/5 ÷ 1/10 = 3/5 × 10/1 = 30/5 = 6. Se invierte el segundo número, no el primero.",
        "Dividir por una fracción menor que 1 agranda el resultado, porque caben muchas veces: 2 ÷ 1/3 = 6. Dividir una fracción entre un natural la achica: 1/2 ÷ 2 = 1/4. Para dividir entre un natural n, usa que n = n/1 y su recíproco es 1/n. Comprueba el resultado multiplicando: si 3/5 ÷ 1/10 = 6, entonces 6 × 1/10 debe dar 3/5.",
    ],
    vocab=[("división como medida", "pregunta cuántas veces cabe el divisor en el dividendo"), ("división como reparto", "pregunta cuánto le toca a cada parte al repartir en partes iguales"), ("recíproco", "fracción con numerador y denominador intercambiados; 2/5 y 5/2 son recíprocos"), ("dividendo", "cantidad que se divide"), ("divisor", "cantidad por la que se divide")],
    worked=[
        W("División como medida", "¿Cuántos trozos de 1/10 m se obtienen de una cinta de 3/5 m?", ["Planteo 3/5 ÷ 1/10 y multiplico por el recíproco: 3/5 × 10/1.", "30/5 = 6. Compruebo: 6 × 1/10 = 6/10 = 3/5."], "6 trozos"),
        W("División como reparto", "Se reparten 2/3 de un queque entre 4 personas. ¿Qué fracción del queque recibe cada una?", ["Planteo 2/3 ÷ 4 = 2/3 × 1/4.", "2/12 = 1/6."], "1/6 del queque"),
    ],
    mistakes=[
        M("Calcular 1/2 ÷ 1/4 = 1/8.", "Se multiplicaron las fracciones sin invertir el divisor.", "1/2 ÷ 1/4 = 1/2 × 4/1 = 2: en medio caben dos cuartos."),
        M("Invertir la primera fracción: 3/4 ÷ 1/8 = 4/3 × 1/8.", "Se confundió cuál fracción se invierte.", "Se invierte el divisor, que es la segunda: 3/4 × 8/1 = 6."),
    ],
    rec=[
        ex("¿Cuántos cuartos (1/4) caben en 1 entero?", "4", "Un entero se divide en 4 cuartos."),
        ex("¿Cuál es el recíproco de 3/7?", "7/3", "Se intercambian numerador y denominador."),
        ex("Se reparte 1/2 de pan en 2 partes iguales. ¿Qué fracción del pan es cada parte?", "1/4", "La mitad partida en dos da cuartos: 1/2 ÷ 2 = 1/4."),
    ],
    und=[
        cx("Calcula 5/6 ÷ 1/12.", "F(5,6)/F(1,12)", "5/6 × 12/1 = 60/6 = 10."),
        cx("Calcula 4/5 ÷ 2.", "F(4,5)/2", "4/5 × 1/2 = 4/10 = 2/5."),
        cx("Calcula 2/3 ÷ 4/9.", "F(2,3)/F(4,9)", "2/3 × 9/4 = 18/12 = 3/2.", form="both"),
    ],
    app=[
        ex("Un listón de 3/4 m se corta en trozos de 1/8 m. ¿Cuántos trozos salen?", "6", "3/4 ÷ 1/8 = 3/4 × 8 = 24/4 = 6."),
        ex("Se tienen 3 litros de jugo y se sirven vasos de 1/4 de litro. ¿Cuántos vasos se llenan?", "12", "3 ÷ 1/4 = 3 × 4 = 12."),
        cx("Una barra de chocolate de ejemplo pesa 2/3 de kg y se reparte entre 4 personas en partes iguales. ¿Cuánto recibe cada una?", "F(2,3)/4", "2/3 ÷ 4 = 2/12 = 1/6.", unit=" kg"),
    ],
    rea=[
        ex("Pablo calculó 1/2 ÷ 1/4 = 1/8. ¿Cuál es el resultado correcto?", "2", "En medio caben dos cuartos: 1/2 × 4 = 2."),
        ex("¿Verdadero o falso? «Dividir por una fracción menor que 1 da un resultado mayor que el número que se divide».", "Verdadero", "Caben muchas veces: 3 ÷ 1/2 = 6, que es mayor que 3."),
    ],
    cha=[
        cx("Un número x cumple x ÷ 2/5 = 10. ¿Cuál es x?", "10*F(2,5)", "Si dividir por 2/5 da 10, entonces x = 10 × 2/5 = 4."),
        cx("Un rollo de cinta mide 9/2 m y se corta en trozos de 3/4 m. ¿Cuántos trozos salen?", "F(9,2)/F(3,4)", "9/2 × 4/3 = 36/6 = 6.", unit=" trozos"),
    ],
    ctx=[cx("Un tanque de ejemplo contiene 3/2 de litro de agua y se llenan botellitas de 1/6 de litro. ¿Cuántas botellitas se llenan?", "F(3,2)/F(1,6)", "3/2 × 6 = 18/2 = 9.", unit=" botellitas")],
    sc=[
        cx("Calcula 1/3 ÷ 1/6.", "F(1,3)/F(1,6)", "1/3 × 6 = 2."),
        cx("Calcula 3/5 ÷ 3.", "F(3,5)/3", "3/5 × 1/3 = 1/5."),
        ex("¿Cuál es el recíproco de 5?", "1/5", "Se escribe 5 = 5/1 y se invierte."),
    ],
    op=task(
        "Tienes una cinta de 3/4 m. (a) Dibuja una barra de 3/4 y úsala para mostrar cuántos trozos de 1/8 m salen. (b) Dibuja otra barra de 3/4 y repártela en 3 partes iguales. Escribe las dos divisiones con fracciones, calcula con el recíproco y explica en una frase la diferencia entre medir y repartir.",
        "(a) 3/4 ÷ 1/8 = 3/4 × 8 = 6 trozos. (b) 3/4 ÷ 3 = 3/4 × 1/3 = 1/4 m cada parte. Medir pregunta cuántas veces cabe; repartir pregunta cuánto toca a cada parte.",
        ["dibuja barras bien divididas", "calcula con el recíproco del divisor", "explica la diferencia entre medida y reparto"],
        ["dos barras dibujadas", "dos divisiones calculadas", "frase de explicación"],
        ["invertir la primera fracción", "no interpretar el resultado con su unidad"],
        "Pide que compruebe cada resultado multiplicando por el divisor.",
    ),
    reinforce="Calcula 1/2 ÷ 1/8, 2/3 ÷ 2 y 5 ÷ 1/3. Dibuja una barra para el primero.",
    extend="Escribe un problema de medida cuya división sea 3/2 ÷ 1/4 y otro de reparto cuya división sea 3/2 ÷ 3. Resuélvelos.",
)

# ------------------------------------------------------------------ OA 02 clase 4
lesson(
    OA2, 4,
    use="Aprenderé a pasar entre fracciones y decimales para multiplicar y dividir, y a ver que dan el mismo resultado. Sirve para elegir la forma más cómoda en cada cálculo.",
    prior=["Sé multiplicar y dividir fracciones.", "Sé multiplicar y dividir decimales por números naturales."],
    explain=[
        "Un decimal es una fracción con denominador 10, 100, 1.000… Por eso 0,5 = 5/10 = 1/2 y 0,25 = 25/100 = 1/4. Para pasar una fracción a decimal, divide el numerador por el denominador: 3/5 = 3 ÷ 5 = 0,6. Algunas fracciones, como 1/3, no tienen decimal exacto: dan 0,333… y es mejor dejarlas como fracción.",
        "Para multiplicar decimales, ignora las comas, multiplica como si fueran naturales y luego pon la coma de modo que haya tantas cifras decimales como en los dos factores juntos. Por ejemplo, 0,4 × 0,7: 4 × 7 = 28, hay 2 cifras decimales, y queda 0,28. En fracciones es 4/10 × 7/10 = 28/100. Es el mismo resultado escrito de dos maneras.",
        "Para dividir decimales, multiplica el dividendo y el divisor por 10 o por 100 hasta que el divisor sea natural. Así 3,6 ÷ 0,9 se convierte en 36 ÷ 9 = 4. En fracciones es 36/10 ÷ 9/10 = 4. Antes de operar, decide qué forma te conviene: decimales con dinero y medidas, fracciones cuando hay tercios, sextos u otras partes que no terminan en decimal.",
    ],
    vocab=[("decimal", "número con coma, que expresa décimas, centésimas…"), ("cifra decimal", "cifra a la derecha de la coma"), ("fracción decimal", "fracción con denominador 10, 100, 1.000…"), ("equivalente", "que representa el mismo valor aunque se escriba distinto"), ("decimal exacto", "decimal que termina, como 0,25")],
    worked=[
        W("Multiplicar decimales y fracciones", "Calcula 0,6 × 0,5 y compruébalo con fracciones.", ["Sin comas: 6 × 5 = 30. Hay 2 cifras decimales: 0,30 = 0,3.", "Con fracciones: 3/5 × 1/2 = 3/10 = 0,3."], "0,3"),
        W("Dividir decimales", "Calcula 2,4 ÷ 0,6 y compruébalo con fracciones.", ["Multiplico por 10 ambos: 24 ÷ 6 = 4.", "Con fracciones: 12/5 ÷ 3/5 = 12/5 × 5/3 = 4."], "4"),
    ],
    mistakes=[
        M("Calcular 0,3 × 0,2 = 0,6.", "Se puso la coma como si hubiera solo una cifra decimal.", "Hay 2 cifras decimales entre los dos factores: 3 × 2 = 6 se escribe 0,06."),
        M("Creer que 1/3 = 0,3.", "Se confundió 3/10 con 1/3.", "1/3 es 0,333… y 3/10 es 0,3; por eso 1/3 se deja como fracción."),
    ],
    rec=[
        ex("Pasa 0,25 a fracción simplificada.", "1/4", "0,25 = 25/100 y dividiendo por 25 queda 1/4."),
        ex("Pasa 3/5 a decimal.", "0,6", "3 ÷ 5 = 0,6."),
        cx("Calcula 0,2 × 0,3.", "F('0.2')*F('0.3')", "2 × 3 = 6 con dos cifras decimales: 0,06.", form="dec"),
    ],
    und=[
        cx("Calcula 0,4 × 0,7.", "F('0.4')*F('0.7')", "4 × 7 = 28 con dos cifras decimales.", form="dec"),
        cx("Calcula 3,6 ÷ 0,9.", "F('3.6')/F('0.9')", "Multiplicando por 10: 36 ÷ 9 = 4."),
        cx("Calcula 1/2 × 0,8 y escribe el resultado como decimal.", "F(1,2)*F('0.8')", "La mitad de 0,8 es 0,4.", form="dec"),
    ],
    app=[
        cx("Cada bolsa de ejemplo pesa 0,75 kg. ¿Cuántos kg pesan 6 bolsas?", "6*F('0.75')", "6 × 75 = 450, con dos cifras decimales: 4,50 = 4,5.", unit=" kg", form="dec"),
        cx("Una cinta de 1,8 m se corta en trozos de 0,2 m. ¿Cuántos trozos salen?", "F('1.8')/F('0.2')", "Multiplicando por 10: 18 ÷ 2 = 9.", unit=" trozos"),
        cx("Una botella tiene 0,8 L y se bebe 3/4 de ella. ¿Cuántos litros se beben?", "F(3,4)*F('0.8')", "3/4 × 4/5 = 12/20 = 0,6.", unit=" L", form="dec"),
    ],
    rea=[
        ex("Ana calculó 0,5 × 0,04 = 0,2. ¿Cuál es el resultado correcto?", "0,02", "5 × 4 = 20 y entre los factores hay 3 cifras decimales: 0,020 = 0,02."),
        ex("¿Dan el mismo resultado 0,5 ÷ 2 y 1/2 ÷ 2?", "Sí; ambos dan 0,25 o 1/4", "0,5 es lo mismo que 1/2, y la mitad de la mitad es un cuarto."),
    ],
    cha=[
        cx("Calcula 1,2 × 3/4 y escribe el resultado como decimal.", "F('1.2')*F(3,4)", "1,2 = 6/5; 6/5 × 3/4 = 18/20 = 0,9.", form="dec"),
        cx("¿Por qué número decimal hay que multiplicar 0,5 para obtener 0,15?", "F('0.15')/F('0.5')", "0,15 ÷ 0,5 = 1,5 ÷ 5 = 0,3.", form="dec"),
    ],
    ctx=[cx("Una huerta de ejemplo mide 2,5 m de ancho y 1,2 m de largo. ¿Cuántos m² tiene?", "F('2.5')*F('1.2')", "25 × 12 = 300 con dos cifras decimales: 3,00 = 3.", unit=" m²")],
    sc=[
        cx("Calcula 0,1 × 0,9.", "F('0.1')*F('0.9')", "1 × 9 = 9 con dos cifras decimales.", form="dec"),
        cx("Calcula 0,8 ÷ 0,2.", "F('0.8')/F('0.2')", "8 ÷ 2 = 4."),
        ex("Pasa 1/4 a decimal.", "0,25", "1 ÷ 4 = 0,25."),
    ],
    op=task(
        "Resuelve estas dos operaciones de dos maneras: con decimales y con fracciones. (a) 0,75 × 0,4 (b) 1,5 ÷ 0,25. Después escribe si las dos maneras dieron lo mismo y cuál te pareció más cómoda en cada caso.",
        "(a) Decimales: 75 × 4 = 300 con 3 cifras decimales: 0,300 = 0,3. Fracciones: 3/4 × 2/5 = 6/20 = 3/10 = 0,3. (b) Decimales: 150 ÷ 25 = 6. Fracciones: 3/2 ÷ 1/4 = 6.",
        ["resuelve cada operación de dos maneras", "los resultados coinciden", "justifica cuál forma fue más cómoda"],
        ["operaciones escritas con ambos métodos", "frase de comparación"],
        ["mal ubicada la coma al multiplicar", "no multiplicar por 10 o 100 el divisor y el dividendo"],
        "Pide que revise cuántas cifras decimales tienen los factores y que compruebe con la estimación.",
    ),
    reinforce="Escribe 0,2, 0,75 y 0,4 como fracciones simplificadas y calcula 0,2 × 0,75.",
    extend="Calcula 1/3 × 0,3 pasando 0,3 a fracción (3/10) y explica por qué el resultado, 1/10, es exacto y no hace falta usar 0,333.",
)

# ------------------------------------------------------------------ OA 03 clase 1
lesson(
    OA3, 1,
    use="Aprenderé a leer un problema con fracciones o decimales, a separar los datos de la pregunta y a estimar antes de calcular. Sirve para saber si un resultado es razonable.",
    prior=["Sé multiplicar y dividir fracciones y decimales.", "Sé redondear números decimales a la unidad más cercana."],
    explain=[
        "Un problema tiene datos (lo que se sabe), una pregunta (lo que se pide) y una unidad (cm, kg, litros). Antes de calcular, subraya los datos y escribe la pregunta con tus palabras. Luego decide la operación: multiplicar cuando hay una cantidad que se repite o una fracción de una cantidad; dividir cuando se reparte o cuando se pregunta cuántas veces cabe una cantidad en otra.",
        "Estimar es calcular de forma aproximada con números fáciles. Para 4,9 × 2,1 redondea a 5 × 2 = 10; el resultado exacto, 10,29, queda cerca. Para 19,8 ÷ 4,1 usa 20 ÷ 4 = 5. La estimación no reemplaza al cálculo, pero avisa si te equivocaste de coma o de operación.",
        "Dos reglas ayudan a juzgar un resultado. Multiplicar por un número menor que 1 achica: 0,9 × 60 es menor que 60. Dividir por un número menor que 1 agranda: 12 ÷ 0,5 es mayor que 12. Si tu respuesta no cumple eso, revisa la operación. Puedes calcular a mano, con calculadora o con una planilla; siempre estima primero para saber qué esperar.",
    ],
    vocab=[("dato", "información del problema que se conoce"), ("pregunta", "lo que el problema pide encontrar"), ("estimación", "cálculo aproximado con números redondeados"), ("redondear", "cambiar un número por otro cercano y más fácil"), ("razonable", "que tiene sentido en la situación")],
    worked=[
        W("Estimar y calcular", "Cada caja de ejemplo pesa 3,9 kg. ¿Cuánto pesan 6 cajas?", ["Estimo: 3,9 es casi 4, y 6 × 4 = 24.", "Calculo: 6 × 3,9 = 23,4. Está cerca de 24, así que es razonable."], "23,4 kg"),
        W("Datos, pregunta y operación", "Un camión de ejemplo carga 2 y 1/2 toneladas y cada caja pesa 1/4 de tonelada. ¿Cuántas cajas lleva?", ["Datos: 2 y 1/2 t y 1/4 t. Pregunta: cuántas cajas caben, es decir, cuántas veces cabe 1/4 en 2 y 1/2.", "Operación: dividir. 5/2 ÷ 1/4 = 5/2 × 4 = 10. Estimación: 2 y 1/2 son 10 cuartos."], "10 cajas"),
    ],
    mistakes=[
        M("Calcular 6,1 × 0,5 y escribir 30,5.", "No se estimó el resultado antes de poner la coma.", "0,5 es la mitad y la mitad de 6 es 3, así que el resultado es 3,05."),
        M("Multiplicar en un problema donde se pregunta cuántas veces cabe una cantidad en otra.", "Se eligió la operación sin analizar la pregunta.", "Cuántas veces cabe es una división."),
    ],
    rec=[
        ex("En «Un jugo de 2 L se reparte en vasos de 0,25 L», ¿qué operación sirve para saber cuántos vasos se llenan: multiplicar o dividir?", "Dividir", "Se pregunta cuántas veces cabe 0,25 L en 2 L."),
        ex("Redondea 4,8 a la unidad más cercana.", "5", "4,8 está más cerca de 5 que de 4."),
        ex("Sin calcular con exactitud: 3,9 × 2 ¿está más cerca de 8 o de 12?", "8", "3,9 es casi 4 y 4 × 2 = 8."),
    ],
    und=[
        ex("Elige la mejor estimación de 5,1 × 3,9: 15, 20 o 25.", "20", "5 × 4 = 20."),
        ex("Estima 19,8 ÷ 4,1 con números fáciles.", "5", "20 ÷ 4 = 5."),
        ex("Sin calcular: 0,9 × 60 ¿es mayor o menor que 60?", "Menor", "Se multiplica por un número menor que 1, así que achica."),
    ],
    app=[
        cx("Un paquete de ejemplo pesa 2,1 kg. ¿Cuánto pesan 8 paquetes iguales? (Estima primero: 8 × 2 = 16.)", "8*F('2.1')", "8 × 21 = 168 con una cifra decimal: 16,8; cerca de 16.", unit=" kg", form="dec"),
        cx("Una receta usa 3/4 de taza de leche por pan. ¿Cuántas tazas se necesitan para 5 panes?", "5*F(3,4)", "5 × 3/4 = 15/4, que son casi 4 tazas.", unit=" tazas", form="both"),
        cx("Un sendero de 4,5 km se recorre en etapas de 0,5 km. ¿Cuántas etapas son?", "F('4.5')/F('0.5')", "45 ÷ 5 = 9.", unit=" etapas"),
    ],
    rea=[
        ex("Sofía calculó 6,1 × 0,5 y le dio 30,5. Con la estimación 6 × 0,5 = 3, ¿cuál es el resultado correcto: 3,05 o 30,5?", "3,05", "El resultado debe estar cerca de 3."),
        ex("¿Verdadero o falso? «Si divides 12 por 0,5, el resultado es menor que 12».", "Falso", "Dividir por 0,5 duplica: 12 ÷ 0,5 = 24."),
    ],
    cha=[
        ex("Un pedido de 18,2 kg de harina se envasa en bolsas de 0,5 kg. ¿Cuántas bolsas completas se llenan?", "36", "18,2 ÷ 0,5 = 36,4; quedan 0,2 kg que no completan una bolsa."),
        ex("Se busca un número x múltiplo de 10 tal que 0,8 × x sea mayor que 40 y menor que 50. ¿Cuál es x?", "60", "0,8 × 60 = 48; con 50 daría 40 (no mayor que 40) y con 70 daría 56."),
    ],
    ctx=[cx("Un tablero de ejemplo de 3,2 m de largo se corta en trozos de 0,4 m. ¿Cuántos trozos salen?", "F('3.2')/F('0.4')", "32 ÷ 4 = 8.", unit=" trozos")],
    sc=[
        ex("Estima 9,8 × 2,1 con números fáciles.", "20", "10 × 2 = 20."),
        ex("Para repartir 2,4 kg entre 4 personas en partes iguales, ¿se multiplica o se divide?", "Se divide", "Repartir en partes iguales es dividir."),
        ex("Redondea 7,2 a la unidad más cercana.", "7", "7,2 está más cerca de 7 que de 8."),
    ],
    op=task(
        "Lee este problema de ejemplo: «Una pista mide 2,4 km. Lucía corrió 3/4 de la pista y Mateo corrió 0,9 de la pista. ¿Quién corrió más kilómetros?». (a) Anota los datos y la pregunta. (b) Estima la distancia de cada uno. (c) Calcula las dos distancias exactas y responde.",
        "Datos: pista 2,4 km; Lucía 3/4; Mateo 0,9. Pregunta: quién corrió más. Estimación: 3/4 de 2,4 es casi 2 km; 0,9 de 2,4 es casi 2 km. Exacto: Lucía 1,8 km; Mateo 2,16 km. Mateo corrió más.",
        ["separa datos y pregunta", "estima antes de calcular", "calcula y responde con unidades"],
        ["datos subrayados", "estimaciones", "cálculos y respuesta escrita"],
        ["saltarse la estimación", "comparar sin pasar a la misma forma"],
        "Pide que revise si cada resultado es menor que la pista completa, porque se recorrió una parte.",
    ),
    reinforce="Estima y luego calcula 4,2 × 3 y 7,5 ÷ 2,5. Escribe si tu estimación estuvo cerca.",
    extend="Inventa un problema de reparto con decimales cuya respuesta sea mayor que el dato inicial, y explica por qué ocurre.",
)

# ------------------------------------------------------------------ OA 03 clase 2
lesson(
    OA3, 2,
    use="Aprenderé a elegir si conviene trabajar con fracciones o con decimales en un problema. Sirve para calcular más rápido y sin perder exactitud.",
    prior=["Sé pasar de fracción a decimal y de decimal a fracción.", "Sé multiplicar y dividir fracciones y decimales."],
    explain=[
        "Un mismo número se puede escribir como fracción o como decimal. Algunas equivalencias son muy útiles: 1/2 = 0,5; 1/4 = 0,25; 3/4 = 0,75; 1/5 = 0,2; 1/10 = 0,1; 1/8 = 0,125. Para pasar una fracción a decimal, divide el numerador por el denominador. Para pasar un decimal a fracción, escribe las cifras sobre 10, 100 o 1.000 y simplifica.",
        "Para elegir, mira los datos. Si todos son decimales o hay unidades como kilos y litros con coma, el decimal suele ser más cómodo. Si aparecen tercios, sextos o séptimos, conviene la fracción, porque 1/3 no tiene decimal exacto y un redondeo como 0,33 da un resultado aproximado, no exacto. Si hay una mezcla, pasa todo a una misma forma antes de operar.",
        "Veamos un caso. Para calcular 2/5 de 3,5 kg, puedes convertir 2/5 en 0,4 y multiplicar 0,4 × 3,5 = 1,4. O puedes pasar 3,5 a 7/2 y calcular 2/5 × 7/2 = 14/10 = 1,4. Ambos caminos dan lo mismo. Elige el más corto, pero responde con la unidad que pide el problema.",
    ],
    vocab=[("equivalencia", "dos escrituras que representan el mismo número"), ("decimal periódico", "decimal que repite una cifra sin terminar, como 0,333…"), ("aproximación", "valor cercano al exacto, pero no igual"), ("unidad", "lo que se mide: kg, L, m, cm"), ("forma conveniente", "la escritura (fracción o decimal) que hace más fácil el cálculo")],
    worked=[
        W("Elegir la forma", "Calcula 2/5 de 3,5 kg.", ["Paso 2/5 a decimal: 2 ÷ 5 = 0,4.", "Multiplico: 0,4 × 3,5 = 1,4. Con fracciones: 2/5 × 7/2 = 14/10 = 1,4."], "1,4 kg"),
        W("Cuando conviene la fracción", "Se reparte 1 litro de jugo entre 3 niños en partes iguales. ¿Cuánto recibe cada uno?", ["Planteo 1 ÷ 3 = 1/3.", "Como 1/3 no tiene decimal exacto, dejo la respuesta como fracción."], "1/3 de litro"),
    ],
    mistakes=[
        M("Escribir 1/3 = 0,3 y calcular con eso.", "Se confundió 1/3 con 3/10.", "1/3 = 0,333…; conviene operar con la fracción 1/3."),
        M("Operar mezclando 3/4 y 0,5 sin convertir, como 3/4 × 0,5 = 3/20.", "Se trató 0,5 como si fuera 1/5.", "0,5 = 1/2; entonces 3/4 × 1/2 = 3/8 (o 0,75 × 0,5 = 0,375)."),
    ],
    rec=[
        ex("Pasa 3/4 a decimal.", "0,75", "3 ÷ 4 = 0,75."),
        ex("Escribe 0,2 como fracción simplificada.", "1/5", "0,2 = 2/10 = 1/5."),
        ex("¿Cuál de estos decimales es equivalente a 1/2: 0,2 o 0,5?", "0,5", "1/2 = 5/10 = 0,5."),
    ],
    und=[
        ex("Escribe 0,125 como fracción simplificada.", "1/8", "0,125 = 125/1.000 y dividiendo por 125 queda 1/8."),
        cx("Calcula 3/5 × 2,5 y escribe el resultado como decimal.", "F(3,5)*F('2.5')", "3/5 = 0,6 y 0,6 × 2,5 = 1,5.", form="dec"),
        ex("¿Se puede escribir 1/3 como decimal exacto (que termina)? Responde sí o no.", "No", "1/3 = 0,333… repite el 3 sin terminar."),
    ],
    app=[
        cx("Una jarra tiene 1,5 L y Carla bebe 1/3 de lo que hay. ¿Cuántos litros bebe?", "F(1,3)*F('1.5')", "1,5 = 3/2; 1/3 × 3/2 = 3/6 = 1/2.", unit=" L", form="dec"),
        cx("Una pista de ejemplo mide 2,4 km y Camila corrió 3/4 de ella. ¿Cuántos km corrió?", "F(3,4)*F('2.4')", "0,75 × 2,4 = 1,8.", unit=" km", form="dec"),
        cx("Un patio de ejemplo tiene 12,5 m² y 3/5 de su superficie son plantas. ¿Cuántos m² son plantas?", "F(3,5)*F('12.5')", "0,6 × 12,5 = 7,5.", unit=" m²", form="dec"),
    ],
    rea=[
        ex("Luis dice que para calcular 1/3 de 2,4 conviene usar 0,33 × 2,4 y que el resultado es exacto. ¿Tiene razón?", "No", "0,33 es una aproximación de 1/3; el resultado exacto es 0,8."),
        cx("Expresa 0,5 × 1/7 como fracción simplificada.", "F('0.5')*F(1,7)", "0,5 = 1/2 y 1/2 × 1/7 = 1/14."),
    ],
    cha=[
        cx("Un recipiente de ejemplo se llena con 1/5 de 2,5 L y luego se agregan 0,75 L. ¿Cuántos litros hay?", "F(1,5)*F('2.5')+F('0.75')", "1/5 de 2,5 es 0,5; 0,5 + 0,75 = 1,25.", unit=" L", form="dec"),
        cx("Calcula 5/8 de 3,2 kg.", "F(5,8)*F('3.2')", "3,2 ÷ 8 = 0,4 y 5 × 0,4 = 2.", unit=" kg"),
    ],
    ctx=[ex("Una receta de ejemplo pide 3/4 de kilo de harina y la balanza digital muestra decimales. ¿Qué número debe marcar la balanza?", "0,75 kg", "3/4 = 3 ÷ 4 = 0,75.")],
    sc=[
        ex("Pasa 1/5 a decimal.", "0,2", "1 ÷ 5 = 0,2."),
        ex("Escribe 0,4 como fracción simplificada.", "2/5", "0,4 = 4/10 = 2/5."),
        ex("Para calcular 1/6 de 3,6, ¿conviene dejar 1/6 como fracción o escribirlo como 0,16? Responde «fracción» o «0,16».", "Fracción", "1/6 no es 0,16; es un decimal periódico."),
    ],
    op=task(
        "Una familia de ejemplo prepara jugo. Tiene 2,4 L de jugo concentrado. La receta A usa 1/3 del concentrado y la receta B usa 0,35 del concentrado. (a) Escribe qué forma elegirás para cada receta y por qué. (b) Calcula cuántos litros usa cada receta. (c) Responde cuál usa más y cuánto más.",
        "A: 1/3 × 2,4 = 0,8 L (conviene fracción, porque 1/3 no es exacto como decimal). B: 0,35 × 2,4 = 0,84 L. B usa más: 0,84 − 0,8 = 0,04 L más.",
        ["elige y justifica la forma", "calcula bien ambos resultados", "compara y responde con unidad"],
        ["cálculos escritos", "respuesta con unidad"],
        ["usar 0,33 como si fuera 1/3 exacto", "olvidar la unidad en la respuesta"],
        "Pide que compruebe cada resultado con una estimación.",
    ),
    reinforce="Pasa 1/4, 3/5 y 1/8 a decimal y 0,6, 0,05 y 0,75 a fracción simplificada.",
    extend="Busca dos fracciones que no den decimal exacto y escribe sus primeras cinco cifras decimales.",
)

# ------------------------------------------------------------------ OA 03 clase 3
lesson(
    OA3, 3,
    use="Aprenderé a resolver problemas de varias etapas con multiplicaciones y divisiones de fracciones y decimales. Sirve para calcular precios, áreas, recetas y recorridos.",
    prior=["Sé elegir entre fracción y decimal.", "Sé estimar antes de calcular."],
    explain=[
        "Los problemas multiplicativos tienen formas conocidas. Cantidad por unidad: si 1 kg cuesta $2.400, 3/4 de kg cuesta 3/4 × 2.400. Fracción de una cantidad: 2/5 de 30 L. Área de un rectángulo: largo × ancho, con fracciones o decimales. Repartos y medidas se resuelven con división: se reparten 6 L en vasos de 1/2 L, cuántos vasos salen.",
        "Cuando hay dos o más etapas, resuelve una por una y escribe el resultado de cada etapa con su unidad. Por ejemplo, si compras 1,5 kg de uvas a $2.200 el kilo y 3/4 de kg de nueces a $12.000 el kilo, primero calcula el costo de cada producto y después súmalos. Si te piden una fracción de lo que queda, primero halla lo que queda.",
        "Una estrategia es dibujar. Una barra sirve para fracciones de una cantidad, y un rectángulo con medidas sirve para áreas. Otra es llevar los datos a una tabla con la cantidad por unidad. Al terminar, compara con tu estimación y revisa que la unidad de la respuesta (pesos, kg, L, m²) corresponda a lo que se pregunta.",
    ],
    vocab=[("cantidad por unidad", "valor de una unidad, como el precio de 1 kg"), ("etapa", "paso de un problema que se resuelve antes de pasar al siguiente"), ("área", "medida de la superficie; en un rectángulo es largo × ancho"), ("caudal", "cantidad de líquido que sale por minuto o por hora"), ("fracción de lo que queda", "parte que se toma una vez restado lo que ya se usó")],
    worked=[
        W("Cantidad por unidad con fracción", "Un kilo de pan de ejemplo cuesta $2.400. ¿Cuánto cuestan 3/4 de kilo?", ["Planteo 3/4 × 2.400.", "2.400 ÷ 4 = 600 y 3 × 600 = 1.800."], "$1.800"),
        W("Dos etapas", "Una tela cuesta $3.500 el metro. Para un cojín se usan 0,8 m y para otro 1 y 1/4 m. ¿Cuánto cuesta en total?", ["Paso 1 y 1/4 a decimal: 1,25 m. Metros totales: 0,8 + 1,25 = 2,05 m.", "Costo: 2,05 × 3.500 = 7.175."], "$7.175"),
    ],
    mistakes=[
        M("Dividir en vez de multiplicar para hallar el costo de 3/4 de kilo.", "Se asoció «de» con repartir.", "«Fracción de una cantidad» se calcula multiplicando: 3/4 × precio."),
        M("Calcular 1/3 de lo que queda usando el total.", "No se restó antes lo ya usado.", "Primero se halla lo que queda y después se toma la fracción de eso."),
    ],
    rec=[
        ex("Cada saco pesa 2,5 kg. ¿Cuántos kg pesan 4 sacos?", "10 kg", "4 × 2,5 = 10."),
        ex("¿Cuánto es 2/3 de 30?", "20", "30 ÷ 3 = 10 y 2 × 10 = 20."),
        ex("Se reparten 6 L de agua en vasos de 1/2 L. ¿Cuántos vasos se llenan?", "12", "6 ÷ 1/2 = 6 × 2 = 12."),
    ],
    und=[
        ex("El queso cuesta $6.400 el kilo. ¿Cuánto cuestan 5/8 de kilo?", "$4.000", "6.400 ÷ 8 = 800 y 5 × 800 = 4.000."),
        cx("Una mesa de ejemplo mide 3,5 m de largo y 2,4 m de ancho. ¿Cuál es su área?", "F('3.5')*F('2.4')", "35 × 24 = 840 con dos cifras decimales: 8,4.", unit=" m²", form="dec"),
        cx("Un gato de ejemplo come 1/4 de kg de alimento por día. ¿Cuántos kg come en 10 días?", "10*F(1,4)", "10 × 1/4 = 10/4 = 5/2 = 2,5.", unit=" kg", form="dec"),
    ],
    app=[
        ex("Marta compra 1,5 kg de uvas a $2.200 el kilo y 3/4 de kg de nueces a $12.000 el kilo. ¿Cuánto paga en total?", "$12.300", "Uvas: 1,5 × 2.200 = 3.300. Nueces: 3/4 × 12.000 = 9.000. Total: 3.300 + 9.000 = 12.300."),
        cx("Un grifo entrega 0,75 L por minuto. ¿Cuántos litros entrega en 8 minutos?", "8*F('0.75')", "8 × 0,75 = 6.", unit=" L"),
        cx("Un jardinero planta 2/5 de un jardín el lunes y 1/3 de lo que queda sin plantar el martes. ¿Qué fracción del jardín planta el martes?", "F(1,3)*(1-F(2,5))", "Queda 3/5 y 1/3 × 3/5 = 3/15 = 1/5."),
    ],
    rea=[
        ex("Pedro compró 0,5 kg de almendras a $9.000 el kilo y pagó $18.000. ¿Es razonable ese cobro? Responde sí o no.", "No", "La mitad de un kilo debería costar 4.500; 18.000 es el precio de 2 kg."),
        ex("Una receta para 4 personas usa 3/4 de taza de arroz. ¿Cuántas tazas se necesitan para 12 personas? Escribe el resultado como número mixto.", "2 y 1/4", "12 personas son 3 veces 4 personas: 3 × 3/4 = 9/4 = 2 y 1/4."),
    ],
    cha=[
        ex("Una tela de 3 y 1/2 m se corta en 7 trozos iguales y cada trozo se vende a $1.800. ¿Cuánto dinero se obtiene por todos los trozos?", "$12.600", "Cada trozo mide 1/2 m, pero se venden 7 trozos: 7 × 1.800 = 12.600."),
        ex("Un tanque de 120 L se llena 5/8 por la mañana y por la tarde se llena 1/4 de la parte que seguía vacía. ¿Cuántos litros hay al final?", "86,25 L", "Mañana: 5/8 × 120 = 75 L. Faltaban 45 L y 1/4 de 45 = 11,25 L. Total: 75 + 11,25 = 86,25 L."),
    ],
    ctx=[cx("Una pared de ejemplo mide 2,5 m de alto y 4 m de largo. Un litro de pintura rinde 8 m². ¿Cuántos litros se necesitan para pintarla una vez?", "F('2.5')*4/8", "Área: 2,5 × 4 = 10 m²; 10 ÷ 8 = 1,25 litros.", unit=" L", form="dec")],
    sc=[
        ex("¿Cuánto cuestan 3/4 de kilo de arroz a $2.000 el kilo?", "$1.500", "2.000 ÷ 4 = 500 y 3 × 500 = 1.500."),
        cx("Una cinta mide 2,4 m y se usan 5/6 de ella. ¿Cuántos metros se usan?", "F(5,6)*F('2.4')", "2,4 ÷ 6 = 0,4 y 5 × 0,4 = 2.", unit=" m"),
        cx("Se reparten 3/4 de litro entre 3 vasos iguales. ¿Cuánto cabe en cada vaso?", "F(3,4)/3", "3/4 ÷ 3 = 1/4.", unit=" de litro"),
    ],
    op=task(
        "Una feria de ejemplo vende estas cantidades. Manzanas: $1.600 el kilo. Queso: $7.200 el kilo. Una persona compra 2,5 kg de manzanas y 3/4 de kilo de queso. (a) Calcula el costo de cada producto. (b) Calcula el total. (c) Si paga con un billete de $20.000, ¿cuánto vuelto recibe? Escribe cada etapa con su unidad.",
        "Manzanas: 2,5 × 1.600 = 4.000. Queso: 3/4 × 7.200 = 5.400. Total: 9.400. Vuelto: 20.000 − 9.400 = 10.600 pesos.",
        ["calcula correctamente cada producto", "suma y resta en el orden correcto", "escribe unidades y respuesta completa"],
        ["cálculos por etapas", "frase de respuesta"],
        ["olvidar convertir 3/4 en cálculo", "no restar del billete"],
        "Pide que estime cada costo (2,5 kg es casi 3 kg, 3/4 es casi 1 kg) y compare.",
    ),
    reinforce="Calcula el costo de 1,5 kg de un producto a $2.000 el kilo y de 2/5 kg de otro a $5.000 el kilo.",
    extend="Escribe un problema de dos etapas que use una fracción de lo que queda y resuélvelo con una barra dibujada.",
)

# ------------------------------------------------------------------ OA 03 clase 4
lesson(
    OA3, 4,
    use="Aprenderé a comprobar mi solución, a revisar si es razonable y a comunicarla con una respuesta completa. Sirve para confiar en mis cálculos y explicarlos a otros.",
    prior=["Sé resolver problemas multiplicativos con fracciones y decimales.", "Sé estimar y usar operaciones inversas."],
    explain=[
        "Comprobar es revisar el resultado por otro camino. La multiplicación y la división se deshacen entre sí: si 7,5 ÷ 2,5 = 3, entonces 3 × 2,5 debe dar 7,5. Si 2/3 de una cantidad es 60, entonces 60 ÷ 2/3 = 60 × 3/2 = 90 debe ser la cantidad total. También puedes estimar o dibujar una barra para ver si el resultado se acerca.",
        "Un resultado es razonable si tiene sentido en la situación. Si una persona toma 3/4 de 20 L, no puede tomar más de 20 L. Si divides entre un número menor que 1, el resultado debe ser mayor. Si algo no cuadra, busca el error: la operación, la coma, la fracción invertida o la unidad.",
        "Comunicar bien es escribir una respuesta en una oración, con unidad y con el resultado relacionado con la pregunta: «Quedan 12 litros de jugo». Muestra el procedimiento ordenado: datos, operación, cálculo, comprobación y respuesta. Así otra persona entiende cómo pensaste y puede ayudarte si hay un error.",
    ],
    vocab=[("comprobación", "revisión de un resultado con otro camino"), ("operación inversa", "operación que deshace la anterior"), ("razonable", "que tiene sentido para la situación"), ("procedimiento", "pasos ordenados que se siguen para resolver"), ("respuesta completa", "oración con el resultado y su unidad")],
    worked=[
        W("Comprobar una división", "Una cinta de 4,8 m se corta en trozos de 0,6 m. Salen 8 trozos. ¿Es correcto?", ["Comprobación con la operación inversa: 8 × 0,6 = 4,8.", "Coincide con la longitud de la cinta."], "Sí, salen 8 trozos"),
        W("Comprobar una fracción de cantidad", "María dice que 2/3 de 90 L son 60 L. ¿Cómo se comprueba?", ["Si 60 L son 2/3, entonces 60 ÷ 2/3 = 60 × 3/2 = 90.", "Recuperamos el total, 90 L."], "Es correcto: 60 L"),
    ],
    mistakes=[
        M("Escribir solo «12» como respuesta a «¿cuántos litros quedan?».", "No se comunicó la unidad ni el contexto.", "Se escribe «Quedan 12 litros de jugo»."),
        M("Aceptar que 4,8 ÷ 0,6 = 0,8.", "No se revisó que dividir entre un número menor que 1 agranda.", "El resultado debe ser mayor que 4,8: 4,8 ÷ 0,6 = 8."),
    ],
    rec=[
        ex("Para comprobar 7,5 ÷ 2,5 = 3, ¿qué multiplicación hay que hacer y cuánto debe dar?", "3 × 2,5 = 7,5", "La multiplicación deshace la división y debe volver al dividendo."),
        ex("A la pregunta «¿cuántos metros de cinta sobran?», ¿cuál es la respuesta mejor comunicada: «5» o «Sobran 5 metros de cinta»?", "Sobran 5 metros de cinta", "La respuesta completa incluye la unidad y se relaciona con la pregunta."),
        ex("¿El producto 4,1 × 3,02 está más cerca de 12 o de 7?", "12", "4 × 3 = 12."),
    ],
    und=[
        cx("Rosa dice que 3/5 ÷ 1/10 = 6. Para comprobar, multiplica 6 × 1/10. ¿Qué resultado da y coincide?", "6*F(1,10)", "6/10 = 3/5, que es el dividendo; coincide."),
        ex("Estima 7,9 × 0,5.", "4", "8 × 0,5 = 4, la mitad de 8."),
        ex("Se reparten 3 kg de arroz en bolsas de 0,25 kg. ¿Cuántas bolsas se arman? Responde con una oración.", "Se arman 12 bolsas", "3 ÷ 0,25 = 12, porque en 1 kg caben 4 bolsas."),
    ],
    app=[
        ex("Un sendero de 6 y 1/4 km se recorre en etapas de 1 y 1/4 km. ¿Cuántas etapas hay? Comprueba multiplicando.", "5 etapas", "25/4 ÷ 5/4 = 5. Comprobación: 5 × 5/4 = 25/4."),
        ex("Se compran 3,6 kg de duraznos a $1.500 el kilo. ¿Cuánto se paga?", "$5.400", "3,6 × 1.500 = 5.400."),
        ex("Un depósito de 40 L pierde 3/8 el lunes y 0,25 del total el martes. ¿Cuántos litros quedan?", "15 L", "Lunes: 15 L. Martes: 10 L. Quedan 40 − 15 − 10 = 15."),
    ],
    rea=[
        ex("Camilo multiplicó 3/2 × 1/4 = 3/8 para saber cuántos vasos de 1/4 L se llenan con 3/2 L. ¿Cuántos vasos se llenan en realidad?", "6", "Es una división: 3/2 ÷ 1/4 = 3/2 × 4 = 6."),
        ex("¿Es razonable que 4,8 ÷ 0,6 dé 0,8? Responde sí o no.", "No", "Dividir entre un número menor que 1 agranda; el resultado es 8."),
    ],
    cha=[
        ex("La cinta A mide 2,5 m y se usan 2/5 de ella. La cinta B mide 1 y 1/2 m y se usan 3/4. ¿Cuál cinta se usa más y cuántos metros?", "La B, 9/8 m (1,125 m)", "A usa 2/5 × 2,5 = 1 m. B usa 3/4 × 3/2 = 9/8 m, que es mayor que 1 m."),
        ex("Un auto de ejemplo recorre 12,5 km en 1/4 de hora. Al mismo ritmo, ¿cuántos km recorre en 1 hora?", "50 km", "1 hora tiene 4 cuartos de hora: 4 × 12,5 = 50."),
    ],
    ctx=[ex("Una profesora de ejemplo reparte 4,5 L de jugo en vasos de 0,15 L. ¿Cuántos vasos llena? Comprueba con la operación inversa.", "30 vasos", "4,5 ÷ 0,15 = 450 ÷ 15 = 30. Comprobación: 30 × 0,15 = 4,5.")],
    sc=[
        ex("Si 12 ÷ 0,5 = 24, ¿qué multiplicación comprueba el resultado?", "24 × 0,5 = 12", "La multiplicación vuelve al dividendo."),
        ex("Una persona bebe 3/4 de una botella de 2 L. ¿Puede haber bebido 3 L?", "No", "Una parte de la botella no puede superar los 2 L; son 1,5 L."),
        ex("Una persona ahorra $2.500 por semana. Escribe una respuesta completa que diga cuánto ahorra en 1 y 1/2 semanas, sabiendo que el ahorro es parejo.", "Se ahorran $3.750", "1 y 1/2 × 2.500 = 2.500 + 1.250 = 3.750 pesos."),
    ],
    op=task(
        "Lee esta solución de ejemplo de Tomás: «Un terreno rectangular mide 3/4 km de largo y 0,6 km de ancho. Área = 3/4 + 0,6 = 1,35 km²». (a) Explica el error. (b) Calcula el área correcta. (c) Comprueba con una estimación. (d) Escribe una respuesta completa.",
        "Error: sumó en vez de multiplicar. Área = 3/4 × 0,6 = 0,75 × 0,6 = 0,45 km². Estimación: 0,75 es casi 1 y 1 × 0,6 = 0,6, así que 0,45 es razonable. Respuesta: el terreno tiene 0,45 km² de área.",
        ["detecta el error de operación", "calcula el área correcta", "comprueba con estimación", "responde con una oración y unidad"],
        ["explicación escrita", "cálculo y estimación", "respuesta completa"],
        ["confundir área con perímetro o con suma", "no incluir la unidad al cuadrado"],
        "Pide que revise que el área sea menor que 1 km², porque los dos lados miden menos de 1 km.",
    ),
    reinforce="Resuelve 1,2 ÷ 0,3 y comprueba con la multiplicación. Escribe una respuesta completa para el problema «¿cuántas bolsas de 0,3 kg salen de 1,2 kg?».",
    extend="Resuelve un problema propio con fracciones y decimales de dos etapas y pídele a otra persona que lo compruebe.",
)
