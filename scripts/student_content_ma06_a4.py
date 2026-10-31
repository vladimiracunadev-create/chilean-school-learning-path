"""Cuaderno del estudiante de 6.º básico Matemática: OA 07 (multiplicación y división de decimales) y OA 08 (problemas con fracciones y decimales)."""
from __future__ import annotations

from student_lessons import ex
from student_content_ma06_a import M, W, lesson, task

OA7 = "MA06 OA 07"

# ------------------------------------------------------------------ OA 07 clase 1
lesson(
    OA7, 1,
    use="Aprenderé a multiplicar un número decimal por un número natural de una cifra. Sirve para calcular medidas, capacidades y repeticiones, como 6 botellas de 0,75 litros.",
    prior=["Sé qué son las décimas, centésimas y milésimas.", "Sé multiplicar números naturales."],
    explain=[
        "Multiplicar un decimal por un natural es repetir una suma. 0,3 × 4 es 0,3 + 0,3 + 0,3 + 0,3. Pensado en décimos: 3 décimos por 4 son 12 décimos, que es 1,2. Por eso 0,3 × 4 = 1,2.",
        "El procedimiento es: multiplica como si no hubiera coma y luego pon la coma de modo que el resultado tenga tantos decimales como el factor decimal. En 2,35 × 3 multiplicas 235 × 3 = 705. Como 2,35 tiene dos decimales, el resultado también: 7,05.",
        "Para comprobar, estima. 2,35 es casi 2 y 2 × 3 = 6, así que el resultado debe estar cerca de 6 o 7; 7,05 es razonable. Si el resultado final termina en ceros decimales, como 3,0 o 5,00, se puede escribir sin ellos: 3 y 5.",
    ],
    vocab=[("decimal", "número con coma que separa la parte entera de la parte decimal"), ("décimo", "una de 10 partes iguales de la unidad: 0,1"), ("centésimo", "una de 100 partes iguales de la unidad: 0,01"), ("milésimo", "una de 1.000 partes iguales de la unidad: 0,001"), ("factor", "cada número que se multiplica")],
    worked=[
        W("Decimales con un decimal", "Calcula 0,6 × 5.", ["Multiplico sin coma: 6 × 5 = 30.", "0,6 tiene un decimal, así que pongo la coma con un decimal: 3,0, que es 3."], "3"),
        W("Decimales con dos decimales", "Calcula 1,25 × 4.", ["Multiplico sin coma: 125 × 4 = 500.", "1,25 tiene dos decimales: 5,00, que es 5."], "5"),
    ],
    mistakes=[
        M("Calcular 0,4 × 5 = 0,20.", "Se puso la coma en un lugar equivocado después de multiplicar 4 × 5 = 20.", "0,4 tiene un decimal, entonces 20 se escribe 2,0, es decir 2."),
        M("Calcular 4,9 × 3 = 1,47.", "Se contaron dos decimales en vez de uno.", "49 × 3 = 147 y con un decimal es 14,7."),
    ],
    rec=[
        ex("¿Cuánto es 0,2 × 3?", "0,6", "2 décimos por 3 son 6 décimos."),
        ex("Resuelve 0,5 × 4.", "2", "5 décimos por 4 son 20 décimos, que es 2."),
        ex("Halla el producto de 1,5 y 2.", "3", "15 × 2 = 30, con un decimal es 3,0."),
    ],
    und=[
        ex("Multiplica 3,4 por 2.", "6,8", "34 × 2 = 68, con un decimal."),
        ex("Calcula 2,15 × 3.", "6,45", "215 × 3 = 645, con dos decimales."),
        ex("¿Cuánto es 0,07 × 8?", "0,56", "7 × 8 = 56, con dos decimales."),
    ],
    app=[
        ex("Una cinta mide 2,35 m y se necesitan 4 cintas iguales. ¿Cuántos metros de cinta se necesitan en total?", "9,4 m", "235 × 4 = 940, con dos decimales es 9,40."),
        ex("Cada paso de una caminata mide 0,75 m. ¿Cuántos metros se avanzan con 8 pasos?", "6 m", "75 × 8 = 600, con dos decimales es 6,00."),
        ex("Un tren recorre 3,6 km cada minuto. ¿Cuántos km recorre en 5 minutos?", "18 km", "36 × 5 = 180, con un decimal es 18,0."),
    ],
    rea=[
        ex("Pablo calculó 0,4 × 5 = 0,20. ¿Cuál es el resultado correcto?", "2", "20 décimos son 2 enteros."),
        ex("Ema calculó 4,9 × 3 = 1,47. Estima y escribe el resultado correcto.", "14,7", "4,9 es casi 5 y 5 × 3 = 15; 49 × 3 = 147 con un decimal."),
    ],
    cha=[
        ex("Resuelve 0,125 × 8.", "1", "125 × 8 = 1.000, con tres decimales es 1,000."),
        ex("Un decimal multiplicado por 5 da 4,5. ¿Cuál es ese decimal?", "0,9", "Se busca el número que, multiplicado por 5, da 4,5: 0,9 × 5 = 4,5."),
    ],
    ctx=[ex("Una tienda ficticia vende botellas de 0,75 litros. ¿Cuántos litros hay en 7 botellas?", "5,25 litros", "75 × 7 = 525, con dos decimales.")],
    sc=[
        ex("Halla el producto de 0,8 y 6.", "4,8", "8 × 6 = 48, con un decimal."),
        ex("Multiplica 1,6 por 5.", "8", "16 × 5 = 80, con un decimal es 8,0."),
        ex("Calcula 3,05 × 2.", "6,1", "305 × 2 = 610, con dos decimales es 6,10."),
    ],
    op=task(
        "Una camioneta ficticia carga 1,35 toneladas por viaje y hace 6 viajes. Calcula las toneladas en total. Antes de calcular, estima redondeando 1,35 a un entero y escribe si tu resultado es razonable. Muestra la multiplicación sin coma y dónde pones la coma.",
        "Estimación: 1 × 6 = 6 (un poco más porque 1,35 es mayor que 1). Cálculo: 135 × 6 = 810; con dos decimales es 8,10 = 8,1 toneladas. Es razonable porque está cerca de 6 a 9.",
        ["multiplica sin coma correctamente", "ubica bien la coma", "estima y compara"],
        ["multiplicación escrita", "estimación y respuesta con unidad"],
        ["mover mal la coma", "no estimar"],
        "Pide que compruebe con la suma repetida de 1,35 seis veces.",
    ),
    reinforce="Calcula 0,3 × 7, 1,2 × 4 y 2,5 × 6. Estima cada resultado antes de calcular.",
    extend="Explica con tus palabras por qué 0,25 × 4 = 1, usando que 0,25 es un cuarto.",
)

# ------------------------------------------------------------------ OA 07 clase 2
lesson(
    OA7, 2,
    use="Aprenderé a dividir un número decimal por un natural de una cifra. Sirve para repartir cantidades como litros, metros o kilos en partes iguales.",
    prior=["Sé dividir números naturales.", "Sé que la división y la multiplicación son operaciones inversas."],
    explain=[
        "Dividir es repartir en partes iguales. Para dividir 7,2 ÷ 3, piensa en décimos: 72 décimos repartidos en 3 son 24 décimos, que es 2,4. Dividir un decimal por un natural da un resultado más pequeño que el decimal original.",
        "Procedimiento: divide la parte entera, pon la coma en el cociente cuando bajes la primera cifra decimal y sigue dividiendo. Si queda resto, agrega ceros al decimal y sigue. Para 5,1 ÷ 2: 5 ÷ 2 = 2 y sobra 1; 11 ÷ 2 = 5 y sobra 1; 10 ÷ 2 = 5. Queda 2,55.",
        "Siempre comprueba multiplicando: el cociente por el divisor debe dar el número del que partiste. En 7,2 ÷ 3 = 2,4, comprueba 2,4 × 3 = 7,2. Si no da, hubo un error al poner la coma o al dividir.",
    ],
    vocab=[("dividendo", "número que se reparte"), ("divisor", "número entre el que se reparte"), ("cociente", "resultado de la división"), ("resto", "lo que sobra al dividir"), ("comprobar", "multiplicar el cociente por el divisor para ver si da el dividendo")],
    worked=[
        W("División exacta", "Calcula 8,4 ÷ 4.", ["8 ÷ 4 = 2; bajo la coma y 4 décimos ÷ 4 = 1 décimo.", "Cociente: 2,1.", "Compruebo: 2,1 × 4 = 8,4."], "2,1"),
        W("División con ceros agregados", "Calcula 5,1 ÷ 2.", ["5 ÷ 2 = 2 y sobra 1; 11 décimos ÷ 2 = 5 décimos y sobra 1.", "Agrego un cero: 10 centésimos ÷ 2 = 5 centésimos.", "Cociente: 2,55."], "2,55"),
    ],
    mistakes=[
        M("Calcular 0,9 ÷ 3 = 3.", "Se ignoró la coma al dividir.", "9 décimos entre 3 son 3 décimos: 0,3."),
        M("Terminar 7 ÷ 2 en 3 con resto 1 cuando el dividendo es 7,0.", "Se detuvo antes de seguir con los decimales.", "7 ÷ 2 = 3,5: se agrega un cero al resto."),
    ],
    rec=[
        ex("¿Cuánto es 0,6 ÷ 2?", "0,3", "6 décimos entre 2 son 3 décimos."),
        ex("Divide 4,8 entre 4.", "1,2", "4 ÷ 4 = 1 y 8 décimos ÷ 4 = 2 décimos."),
        ex("Halla el cociente de 9,3 ÷ 3.", "3,1", "9 ÷ 3 = 3 y 3 décimos ÷ 3 = 1 décimo."),
    ],
    und=[
        ex("Resuelve 8,1 ÷ 3.", "2,7", "81 décimos entre 3 son 27 décimos."),
        ex("Calcula 1,26 ÷ 6.", "0,21", "126 centésimos entre 6 son 21 centésimos."),
        ex("¿Cuánto es 4,5 ÷ 5?", "0,9", "45 décimos entre 5 son 9 décimos."),
    ],
    app=[
        ex("Se reparten 15,6 kg de manzanas en 4 cajas iguales. ¿Cuántos kg lleva cada caja?", "3,9 kg", "156 décimos entre 4 son 39 décimos."),
        ex("Una botella de 2,4 litros se reparte en 8 vasos iguales. ¿Cuántos litros hay en cada vaso?", "0,3 litros", "24 décimos entre 8 son 3 décimos."),
        ex("Una cinta de 7,5 m se corta en 6 partes iguales. ¿Cuánto mide cada parte?", "1,25 m", "7,5 ÷ 6 = 1,25; comprobación: 1,25 × 6 = 7,5."),
    ],
    rea=[
        ex("Luis dice que 0,9 ÷ 3 = 3. ¿Cuál es el resultado correcto?", "0,3", "0,3 × 3 = 0,9."),
        ex("Sol dice que 7,2 ÷ 4 = 1,8. ¿Es correcto? Responde sí o no.", "Sí", "1,8 × 4 = 7,2."),
    ],
    cha=[
        ex("Calcula 1 ÷ 8 agregando ceros al dividendo.", "0,125", "10 ÷ 8 = 1 resto 2; 20 ÷ 8 = 2 resto 4; 40 ÷ 8 = 5."),
        ex("Un número dividido por 6 da 0,25. ¿Cuál es el número?", "1,5", "Se busca el número que al repartirlo en 6 da 0,25: 0,25 × 6 = 1,5."),
    ],
    ctx=[ex("Una persona camina 18,4 km repartidos en partes iguales durante 8 días. ¿Cuántos km camina cada día?", "2,3 km", "184 décimos entre 8 son 23 décimos.")],
    sc=[
        ex("Divide 6,4 entre 2.", "3,2", "64 décimos entre 2 son 32 décimos."),
        ex("Halla el cociente de 0,35 ÷ 5.", "0,07", "35 centésimos entre 5 son 7 centésimos."),
        ex("Resuelve 12,6 ÷ 9.", "1,4", "126 décimos entre 9 son 14 décimos."),
    ],
    op=task(
        "Se reparten 9,6 litros de jugo en 8 jarras iguales. Calcula cuánto lleva cada jarra, muestra la división paso a paso y comprueba multiplicando. Después reparte 2,5 litros entre 4 vasos y explica qué haces cuando sobra resto.",
        "9,6 ÷ 8 = 1,2 litros; comprobación 1,2 × 8 = 9,6. 2,5 ÷ 4: 2,5 = 2,50 y 250 centésimos ÷ 4 = 62 y sobran 2, con otro cero 20 milésimos ÷ 4 = 5: 0,625 litros.",
        ["divide con la coma bien ubicada", "agrega ceros cuando hay resto", "comprueba con multiplicación"],
        ["división escrita", "comprobación"],
        ["olvidar la coma", "detener la división con resto"],
        "Pide que multiplique el cociente por el divisor y compare con el dividendo.",
    ),
    reinforce="Calcula 8,4 ÷ 7, 1,5 ÷ 3 y 3,6 ÷ 9. Comprueba multiplicando.",
    extend="Explica por qué 3 ÷ 4 = 0,75 usando la idea de agregar ceros al dividendo.",
)

# ------------------------------------------------------------------ OA 07 clase 3
lesson(
    OA7, 3,
    use="Aprenderé a multiplicar y dividir decimales por 10, 100, 1.000 y por múltiplos de 10. Sirve para cambiar de unidad y calcular rápido.",
    prior=["Sé multiplicar y dividir decimales por números de una cifra.", "Sé el valor posicional de décimos, centésimos y milésimos."],
    explain=[
        "Al multiplicar un decimal por 10, cada cifra pasa a un lugar 10 veces mayor, y la coma se corre un lugar a la derecha. Por 100, dos lugares; por 1.000, tres lugares. Si faltan cifras, se agregan ceros. Así, 4,56 × 100 = 456 y 0,4 × 1.000 = 400.",
        "Al dividir por 10, 100 o 1.000, la coma se corre a la izquierda uno, dos o tres lugares. Así 0,8 ÷ 10 = 0,08 y 62 ÷ 100 = 0,62. Si el número no tiene coma, la coma está al final: 62 = 62,0.",
        "Para multiplicar por un múltiplo de 10, como 20 o 30, multiplica primero por la cifra y luego por 10. 1,5 × 30 = 1,5 × 3 × 10 = 4,5 × 10 = 45. Para dividir por 20 o 40, divide por la cifra y luego por 10. Ten cuidado de correr la coma al lado correcto.",
    ],
    vocab=[("potencia de 10", "10, 100, 1.000…"), ("correr la coma", "cambiar la posición de la coma al multiplicar o dividir por 10, 100 o 1.000"), ("múltiplo de 10", "número como 20, 30 o 40"), ("cambio de unidad", "pasar de una unidad de medida a otra"), ("posición", "lugar que ocupa una cifra")],
    worked=[
        W("Multiplicar y dividir por potencias de 10", "Calcula 4,56 × 100 y 0,8 ÷ 10.", ["× 100: corro la coma 2 lugares a la derecha: 456.", "÷ 10: corro la coma 1 lugar a la izquierda y agrego un cero: 0,08."], "456 y 0,08"),
        W("Múltiplo de 10", "Calcula 1,5 × 30.", ["Primero × 3: 1,5 × 3 = 4,5.", "Luego × 10: 4,5 × 10 = 45."], "45"),
    ],
    mistakes=[
        M("Calcular 2,5 × 10 = 2,50.", "Se agregó un cero pero no se corrió la coma.", "Se corre la coma un lugar a la derecha: 25."),
        M("Calcular 7 ÷ 100 = 0,7.", "Se corrió la coma solo un lugar.", "Dividir por 100 corre la coma dos lugares: 0,07."),
    ],
    rec=[
        ex("Calcula 3,2 × 10.", "32", "La coma se corre un lugar a la derecha."),
        ex("Calcula 45 ÷ 10.", "4,5", "La coma se corre un lugar a la izquierda."),
        ex("Calcula 0,07 × 100.", "7", "La coma se corre dos lugares a la derecha."),
    ],
    und=[
        ex("Calcula 5,123 × 1.000.", "5.123", "La coma se corre tres lugares a la derecha."),
        ex("Calcula 62 ÷ 100.", "0,62", "La coma se corre dos lugares a la izquierda."),
        ex("Calcula 0,4 × 1.000.", "400", "Tres lugares a la derecha: 0,400 pasa a 400."),
    ],
    app=[
        ex("Una lámina de plástico mide 0,35 mm de grosor. ¿Cuánto mide el grosor de 20 láminas juntas?", "7 mm", "0,35 × 2 = 0,7 y × 10 = 7."),
        ex("Una caja pesa 2,4 kg y se apilan 30 cajas. ¿Cuánto pesa la pila?", "72 kg", "2,4 × 3 = 7,2 y × 10 = 72."),
        ex("Se reparten 9,6 litros en 20 botellas iguales. ¿Cuántos litros lleva cada botella?", "0,48 litros", "9,6 ÷ 2 = 4,8 y 4,8 ÷ 10 = 0,48."),
    ],
    rea=[
        ex("Tomás calculó 2,5 × 10 = 2,50. ¿Cuál es el resultado correcto?", "25", "La coma se corre a la derecha."),
        ex("Ana dice que 7 ÷ 100 = 0,7. ¿Cuál es el resultado correcto?", "0,07", "Dos lugares a la izquierda: 0,07."),
    ],
    cha=[
        ex("Calcula 0,06 × 500.", "30", "0,06 × 5 = 0,3 y × 100 = 30."),
        ex("Calcula 36 ÷ 400.", "0,09", "36 ÷ 4 = 9 y 9 ÷ 100 = 0,09."),
    ],
    ctx=[ex("Un fideo mide 0,18 m. Si se ponen 50 fideos uno tras otro, ¿cuántos metros miden juntos?", "9 m", "0,18 × 5 = 0,9 y × 10 = 9.")],
    sc=[
        ex("Calcula 7,8 × 10.", "78", "Un lugar a la derecha."),
        ex("Calcula 0,5 ÷ 10.", "0,05", "Un lugar a la izquierda."),
        ex("Calcula 1,2 × 40.", "48", "1,2 × 4 = 4,8 y × 10 = 48."),
    ],
    op=task(
        "Completa en tu cuaderno una tabla con estos cálculos: 3,25 × 10, 3,25 × 100, 3,25 × 1.000, 32,5 ÷ 10 y 32,5 ÷ 100. Escribe cada resultado y una frase que explique qué pasa con la coma cuando multiplicas y cuando divides.",
        "32,5; 325; 3.250; 3,25; 0,325. Al multiplicar la coma se corre a la derecha y al dividir se corre a la izquierda, tantos lugares como ceros tiene el 10, 100 o 1.000.",
        ["corre la coma al lado correcto", "completa con ceros", "explica la regla"],
        ["tabla con cinco resultados", "frase de regla"],
        ["correr la coma al lado equivocado", "agregar ceros sin correr la coma"],
        "Pide que compruebe uno de los resultados con la operación inversa.",
    ),
    reinforce="Calcula 6,4 × 10, 6,4 × 100 y 6,4 ÷ 10. Escribe en qué dirección se corre la coma.",
    extend="Explica cómo calcular 0,75 × 200 sin calculadora, usando la idea de múltiplo de 10.",
)

# ------------------------------------------------------------------ OA 07 clase 4
lesson(
    OA7, 4,
    use="Aprenderé a multiplicar dos decimales, hasta milésimas, y a dividir por un decimal. Sirve para calcular áreas y partes de partes, como el 0,5 de 0,8 de un litro.",
    prior=["Sé multiplicar decimales por naturales.", "Sé el valor posicional de décimos, centésimos y milésimos."],
    explain=[
        "Para multiplicar dos decimales, multiplica como si fueran naturales y luego cuenta los decimales de los dos factores juntos. El resultado tiene esa cantidad de decimales. En 1,2 × 0,4: 12 × 4 = 48; 1,2 tiene un decimal y 0,4 tiene otro, en total 2; el resultado es 0,48.",
        "También se entiende con décimos: 0,3 × 0,2 es 3 décimos por 2 décimos, que son 6 centésimos: 0,06. Por eso el producto de dos números menores que 1 es menor que cada uno de ellos. Si un factor es mayor que 1, el producto es mayor que el otro factor.",
        "Para comprobar, estima. 2,5 × 1,2 es parecido a 2,5 × 1, es decir 2,5, y un poco más; el resultado 3 es razonable. Si terminas con ceros decimales al final, como 3,00 o 0,100, puedes escribirlo más simple: 3 y 0,1.",
        "Para dividir por un decimal, multiplica el dividendo y el divisor por 10, 100 o 1.000 hasta que el divisor sea un natural. El cociente no cambia. En 7,2 ÷ 0,4 multiplicas ambos por 10 y queda 72 ÷ 4 = 18. Comprueba multiplicando: 18 × 0,4 = 7,2.",
    ],
    vocab=[("producto", "resultado de una multiplicación"), ("factor", "cada número que se multiplica"), ("área", "medida de la superficie de una figura"), ("estimar", "calcular un valor aproximado"), ("cifra decimal", "cifra que está a la derecha de la coma")],
    worked=[
        W("Producto menor que los factores", "Calcula 0,3 × 0,2.", ["3 × 2 = 6.", "Cada factor tiene un decimal: dos en total. El producto es 0,06."], "0,06"),
        W("Un factor mayor que 1", "Calcula 2,5 × 1,2.", ["25 × 12 = 300.", "Los factores tienen un decimal cada uno: dos en total. 3,00 = 3."], "3"),
        W("Dividir por un decimal", "Calcula 1,5 ÷ 0,25.", ["Multiplico por 100 el dividendo y el divisor: 1,5 pasa a 150 y 0,25 pasa a 25.", "Divido 150 ÷ 25 = 6. Compruebo: 6 × 0,25 = 1,5."], "6"),
    ],
    mistakes=[
        M("Calcular 0,2 × 0,3 = 0,6.", "Se contó un solo decimal.", "Son dos decimales en total: 2 × 3 = 6, entonces 0,06."),
        M("Creer que multiplicar siempre agranda el número.", "Esto solo ocurre si se multiplica por un número mayor que 1.", "0,5 × 0,5 = 0,25, que es menor que 0,5."),
    ],
    rec=[
        ex("¿Cuánto es 0,5 × 0,2?", "0,1", "5 × 2 = 10, con dos decimales es 0,10."),
        ex("Resuelve 0,4 × 0,4.", "0,16", "4 × 4 = 16, con dos decimales."),
        ex("Halla el producto de 0,1 y 0,1.", "0,01", "1 décimo por 1 décimo es 1 centésimo."),
    ],
    und=[
        ex("Multiplica 1,3 por 0,4.", "0,52", "13 × 4 = 52, con dos decimales."),
        ex("Calcula 0,6 × 1,5.", "0,9", "6 × 15 = 90, con dos decimales es 0,90."),
        ex("Calcula 1,2 ÷ 0,3.", "4", "Multiplicando por 10 ambos: 12 ÷ 3 = 4. Compruebo: 4 × 0,3 = 1,2."),
    ],
    app=[
        ex("Un rectángulo mide 2,4 m de largo y 1,5 m de ancho. ¿Cuántos metros cuadrados tiene su área?", "3,6 m²", "24 × 15 = 360, con dos decimales es 3,60."),
        ex("Una tela mide 0,8 m de ancho y 2,5 m de largo. ¿Cuál es su área?", "2 m²", "8 × 25 = 200, con dos decimales es 2,00."),
        ex("Una baldosa mide 0,25 m por 0,4 m. ¿Cuántos metros cuadrados mide?", "0,1 m²", "25 × 4 = 100, con tres decimales es 0,100."),
    ],
    rea=[
        ex("Eva calculó 0,3 × 0,4 = 1,2. ¿Cuál es el resultado correcto?", "0,12", "3 × 4 = 12 y hay dos decimales en total."),
        ex("El producto de dos decimales menores que 1, ¿es mayor o menor que cada factor?", "Menor", "Por ejemplo, 0,5 × 0,5 = 0,25, que es menor que 0,5."),
    ],
    cha=[
        ex("Resuelve 0,125 × 0,8.", "0,1", "125 × 8 = 1.000, con cuatro decimales es 0,1000."),
        ex("Calcula 4,5 ÷ 0,05.", "90", "Multiplicando ambos por 100: 450 ÷ 5 = 90. Compruebo: 90 × 0,05 = 4,5."),
    ],
    ctx=[ex("Un huerto rectangular ficticio mide 3,2 m por 0,5 m. ¿Cuántos metros cuadrados mide?", "1,6 m²", "32 × 5 = 160, con dos decimales es 1,60.")],
    sc=[
        ex("Multiplica 0,3 por 0,3.", "0,09", "3 × 3 = 9, con dos decimales."),
        ex("Calcula 1,4 × 0,5.", "0,7", "14 × 5 = 70, con dos decimales es 0,70."),
        ex("¿Cuánto es 2,2 × 1,1?", "2,42", "22 × 11 = 242, con dos decimales."),
    ],
    op=task(
        "Una pieza de tela ficticia mide 1,6 m de largo y 0,75 m de ancho. Estima el área, calcula el valor exacto (largo por ancho) y compara. Después explica con una frase por qué 0,5 × 0,5 es menor que 0,5.",
        "Estimación: 1,6 × 0,75 es cerca de 2 × 0,75 = 1,5, y un poco menos. Cálculo: 16 × 75 = 1.200, con tres decimales es 1,200 = 1,2 m². Comparación: es menor que 1,5, como se esperaba. 0,5 × 0,5 = 0,25 porque tomo la mitad de 0,5.",
        ["multiplica sin coma", "ubica bien la coma", "estima y explica"],
        ["multiplicación escrita", "área con unidad", "frase de explicación"],
        ["contar mal los decimales", "pensar que multiplicar siempre agranda"],
        "Pide que cuente cuántos decimales tienen los dos factores juntos y compruebe que el producto tiene esa cantidad.",
    ),
    reinforce="Calcula 0,7 × 0,2, 1,3 × 0,6 y 0,15 × 0,4. Cuenta los decimales de los factores.",
    extend="Calcula 0,4 × 0,4 × 0,4 en dos pasos y explica cuántos decimales tiene el resultado.",
)

# ================================================================== OA 08
OA8 = "MA06 OA 08"

# ------------------------------------------------------------------ OA 08 clase 1
lesson(
    OA8, 1,
    use="Aprenderé a entender un problema con decimales: qué datos hay, qué se pregunta y qué operación sirve. Sirve para sumar y restar medidas y cantidades con coma.",
    prior=["Sé el valor posicional de los decimales hasta milésimas.", "Sé sumar y restar números naturales."],
    explain=[
        "Para resolver un problema, primero lee con calma. Subraya los datos y la pregunta. Luego decide: si juntas cantidades, sumas; si quitas, comparas o buscas cuánto falta, restas. Escribe la operación y calcula.",
        "Para sumar o restar decimales, escribe los números uno bajo el otro con la coma bajo la coma. Si un número tiene menos cifras decimales, agrega ceros: 2,35 + 1,4 es 2,35 + 1,40 = 3,75. Así cada cifra queda en su lugar: décimos con décimos, centésimos con centésimos.",
        "Después, revisa la respuesta. ¿Tiene sentido? Una suma debe ser mayor que cada sumando; una resta debe ser menor que el número inicial. Escribe la respuesta con la unidad. Un error frecuente es alinear por la derecha como en los naturales; en los decimales se alinea por la coma.",
    ],
    vocab=[("dato", "información que da el problema"), ("alinear", "poner las cifras en columnas según su lugar"), ("coma decimal", "signo que separa la parte entera de la parte decimal"), ("sumando", "cada número que se suma"), ("minuendo", "número del que se quita")],
    worked=[
        W("Suma de decimales", "Calcula 3,45 + 2,8.", ["Alineo las comas: 3,45 y 2,80.", "Sumo centésimas: 5; décimas: 4 + 8 = 12, escribo 2 y llevo 1; unidades: 3 + 2 + 1 = 6.", "Resultado: 6,25."], "6,25"),
        W("Resta de decimales", "Calcula 8 − 2,375.", ["Escribo 8 como 8,000 y alineo las comas.", "8,000 − 2,375 = 5,625."], "5,625"),
    ],
    mistakes=[
        M("Calcular 2,5 + 0,25 = 2,30.", "Se alinearon los números por la derecha en vez de por la coma.", "2,50 + 0,25 = 2,75."),
        M("Sumar un número natural sin ponerle coma ni ceros.", "No se pensó el natural como decimal.", "8 = 8,000 y así la resta con 2,375 es ordenada."),
    ],
    rec=[
        ex("Calcula 0,5 + 0,25.", "0,75", "0,50 + 0,25."),
        ex("Calcula 1,2 − 0,7.", "0,5", "12 décimos − 7 décimos = 5 décimos."),
        ex("Calcula 2 + 0,3.", "2,3", "2 enteros y 3 décimos."),
    ],
    und=[
        ex("Calcula 4,6 + 3,75.", "8,35", "4,60 + 3,75."),
        ex("Calcula 7,2 − 4,85.", "2,35", "7,20 − 4,85."),
        ex("Calcula 0,125 + 0,5.", "0,625", "0,125 + 0,500."),
    ],
    app=[
        ex("Pedro corrió 2,5 km y Ana corrió 1,75 km. ¿Cuántos km corrieron entre los dos?", "4,25 km", "2,50 + 1,75."),
        ex("Pedro corrió 2,5 km y Ana corrió 1,75 km. ¿Cuántos km más corrió Pedro que Ana?", "0,75 km", "2,50 − 1,75 = 0,75."),
        ex("Una tela de 9 m se usa en parte: 3,45 m. ¿Cuántos metros quedan?", "5,55 m", "9,00 − 3,45."),
    ],
    rea=[
        ex("Pía calculó 2,5 + 0,25 = 2,30. ¿Cuál es el resultado correcto?", "2,75", "2,50 + 0,25."),
        ex("Teo dice que 3,25 es mayor que 3,4 porque 25 es mayor que 4. ¿Cuál es el mayor?", "3,4", "3,40 es mayor que 3,25."),
    ],
    cha=[
        ex("¿Qué número falta? 3,2 + ? = 5,05", "1,85", "5,05 − 3,20 = 1,85."),
        ex("Calcula 0,375 + 0,625.", "1", "375 + 625 = 1.000 milésimas, que es 1."),
    ],
    ctx=[ex("En una feria ficticia se compraron 1,35 kg de manzanas y 0,9 kg de peras. ¿Cuántos kg se compraron en total?", "2,25 kg", "1,35 + 0,90.")],
    sc=[
        ex("Calcula 1,5 + 2,25.", "3,75", "1,50 + 2,25."),
        ex("Calcula 6 − 1,4.", "4,6", "6,0 − 1,4."),
        ex("Calcula 0,9 − 0,45.", "0,45", "0,90 − 0,45."),
    ],
    op=task(
        "Resuelve este problema paso a paso: «En una carrera ficticia, Lía hizo 12,5 s; Raúl hizo 13,08 s y Mara hizo 12,75 s». Calcula cuánta diferencia hay entre Raúl y Lía y cuánto suman los tiempos de Lía y Mara. Alinea las comas y escribe cada respuesta con su unidad.",
        "Diferencia: 13,08 − 12,50 = 0,58 s. Suma: 12,50 + 12,75 = 25,25 s.",
        ["alinea por la coma", "agrega ceros cuando hace falta", "responde con unidad"],
        ["dos operaciones alineadas", "respuestas con unidad"],
        ["alinear por la derecha", "olvidar la unidad"],
        "Pide que sume el resultado de la resta con el sustraendo para comprobar.",
    ),
    reinforce="Calcula 3,6 + 2,45, 5 − 1,8 y 0,7 + 0,35. Alinea las comas.",
    extend="Inventa un problema con tres cantidades decimales que se sumen y una que se reste. Resuélvelo y comprueba.",
)

# ------------------------------------------------------------------ OA 08 clase 2
lesson(
    OA8, 2,
    use="Aprenderé a pasar entre fracciones y decimales para resolver problemas que mezclan ambos. Sirve para calcular cuando los datos vienen escritos de maneras distintas.",
    prior=["Sé que 1/2 = 0,5 y 1/4 = 0,25.", "Sé sumar y restar decimales."],
    explain=[
        "Una fracción con denominador 10, 100 o 1.000 se escribe directamente como decimal: 3/10 = 0,3, 7/100 = 0,07, 125/1.000 = 0,125. Otras fracciones se pueden llevar a esos denominadores con fracciones equivalentes: 1/2 = 5/10 = 0,5, 1/4 = 25/100 = 0,25, 3/5 = 6/10 = 0,6 y 1/8 = 125/1.000 = 0,125.",
        "Para resolver un problema con fracciones y decimales juntos, elige un solo formato. Si los datos se pasan fácilmente a decimal, trabaja con decimales: 1/2 + 0,25 = 0,5 + 0,25 = 0,75. Si no, trabaja con fracciones.",
        "Después de calcular, vuelve a la historia y escribe la respuesta con unidad. Comprueba pasando el resultado al otro formato. Un resultado de 0,75 L también se puede escribir como 3/4 L. Así verificas que tiene sentido.",
    ],
    vocab=[("fracción decimal", "fracción con denominador 10, 100, 1.000…"), ("fracción equivalente", "fracción que vale lo mismo con otros números"), ("formato", "forma de escribir un número: fracción o decimal"), ("decimal exacto", "decimal que termina, como 0,25"), ("convertir", "cambiar la forma de escribir sin cambiar el valor")],
    worked=[
        W("Sumar fracción y decimal", "Calcula 1/2 + 0,25.", ["1/2 = 0,5.", "0,5 + 0,25 = 0,75."], "0,75 (o 3/4)"),
        W("Restar decimal a fracción", "Calcula 3/4 − 0,5.", ["3/4 = 0,75.", "0,75 − 0,50 = 0,25."], "0,25 (o 1/4)"),
    ],
    mistakes=[
        M("Escribir 1/4 = 0,4.", "Se usó el denominador como cifra decimal.", "1/4 = 25/100 = 0,25."),
        M("Sumar 1/2 + 0,25 como 1,25 / 2.", "Se mezclaron los formatos sin convertir.", "Convierte 1/2 a 0,5 y luego suma: 0,75."),
    ],
    rec=[
        ex("Escribe 1/2 como decimal.", "0,5", "1/2 = 5/10."),
        ex("Escribe 1/4 como decimal.", "0,25", "1/4 = 25/100."),
        ex("Escribe 0,75 como fracción simplificada.", "3/4", "75/100 se divide por 25."),
    ],
    und=[
        ex("Escribe 2/5 como decimal.", "0,4", "2/5 = 4/10."),
        ex("Escribe 1/8 como decimal.", "0,125", "1/8 = 125/1.000."),
        ex("Escribe 0,6 como fracción simplificada.", "3/5", "6/10 se divide por 2."),
    ],
    app=[
        ex("Se usan 3/5 de litro de agua y 0,2 litros de jugo. ¿Cuántos litros de mezcla hay?", "0,8 litros", "3/5 = 0,6 y 0,6 + 0,2."),
        ex("Una cinta mide 1 3/4 m y se corta 0,5 m. ¿Cuánto mide lo que queda?", "1,25 m", "1 3/4 = 1,75 y 1,75 − 0,5."),
        ex("Calcula 1/8 + 0,375.", "0,5", "1/8 = 0,125 y 0,125 + 0,375."),
    ],
    rea=[
        ex("Lola dice que 1/4 + 0,5 = 0,9 porque 1/4 = 0,4. ¿Cuál es el resultado correcto?", "0,75", "1/4 = 0,25 y 0,25 + 0,5."),
        ex("¿0,3 y 1/3 son iguales? Responde sí o no.", "No", "0,3 es 3/10 y 3/10 no es igual a 1/3."),
    ],
    cha=[
        ex("Calcula 2 1/2 + 1,75.", "4,25", "2,5 + 1,75."),
        ex("Calcula 3/8 + 0,125 + 1/2.", "1", "0,375 + 0,125 + 0,5 = 1."),
    ],
    ctx=[ex("Una receta ficticia usa 3/4 kg de harina y 0,35 kg de azúcar. ¿Cuántos kg de ingredientes secos hay?", "1,1 kg", "0,75 + 0,35 = 1,10.")],
    sc=[
        ex("Escribe 1/5 como decimal.", "0,2", "1/5 = 2/10."),
        ex("Calcula 0,25 + 1/2.", "0,75", "0,25 + 0,5."),
        ex("Calcula 1 1/2 − 0,25.", "1,25", "1,5 − 0,25."),
    ],
    op=task(
        "Tienes tres datos de una receta: 1/4 kg de mantequilla, 0,5 kg de harina y 3/8 kg de azúcar. Pasa todo a decimales, calcula el peso total y expresa el resultado también como fracción o número mixto.",
        "1/4 = 0,25; 0,5; 3/8 = 0,375. Total: 0,25 + 0,5 + 0,375 = 1,125 kg, que es 1 1/8 kg.",
        ["convierte todos los datos a decimal", "suma con las comas alineadas", "expresa el resultado en fracción"],
        ["conversiones escritas", "suma y resultado en dos formatos"],
        ["convertir mal 1/4", "no alinear las comas"],
        "Pide que pase 0,125 a fracción para comprobar que coincide con 1/8.",
    ),
    reinforce="Escribe 1/2, 1/4, 3/4, 1/5 y 1/8 como decimales y ordénalos de menor a mayor.",
    extend="Explica cuándo conviene trabajar con fracciones y cuándo con decimales, usando 1/3 + 0,5 como ejemplo.",
)

# ------------------------------------------------------------------ OA 08 clase 3
lesson(
    OA8, 3,
    use="Aprenderé a elegir una estrategia para resolver problemas con fracciones, números mixtos y decimales, y a comprobar el resultado. Sirve para decidir cómo calcular más fácil.",
    prior=["Sé sumar y restar fracciones, mixtos y decimales.", "Sé pasar entre fracciones y decimales."],
    explain=[
        "Un mismo problema puede resolverse de más de una manera. Si los datos son fracciones con denominadores como 2, 4, 5, 8 o 10, conviene pasar todo a decimales. Si hay fracciones como 1/3 o 1/6, que no terminan en un decimal exacto, conviene trabajar con fracciones y denominador común.",
        "Antes de calcular, estima. Si sumas 4,9 + 3 1/10, piensa 5 + 3 = 8. Después calcula: 3 1/10 = 3,1 y 4,9 + 3,1 = 8. Si tu resultado se aleja mucho de la estimación, revisa.",
        "Para comprobar, usa la operación inversa o resuelve con otro formato. En el problema de una cuerda de 5 m de la que se cortan 2 3/8 m, puedes calcular 5 − 2,375 = 2,625 m. Y comprobar sumando 2,625 + 2,375 = 5. También puedes escribir el resultado como 2 5/8.",
    ],
    vocab=[("estrategia", "plan para resolver un problema"), ("estimar", "calcular una respuesta aproximada"), ("operación inversa", "la que deshace a otra"), ("denominador común", "denominador igual para dos fracciones"), ("razonable", "que tiene sentido comparado con la estimación")],
    worked=[
        W("Elegir un formato", "Una cuerda mide 5 m y se cortan 2 3/8 m. ¿Cuánto queda?", ["3/8 = 0,375, entonces 2 3/8 = 2,375.", "5 − 2,375 = 2,625.", "Como fracción: 2,625 = 2 5/8. Compruebo: 2,625 + 2,375 = 5."], "2,625 m = 2 5/8 m"),
        W("Estimar y calcular", "Calcula 4,9 + 3 1/10.", ["Estimo: 5 + 3 = 8.", "3 1/10 = 3,1 y 4,9 + 3,1 = 8,0."], "8"),
    ],
    mistakes=[
        M("Convertir 1/3 a 0,3 y usarlo como exacto.", "1/3 no tiene un decimal exacto.", "Trabaja con fracciones y denominador común: 1/3 + 1/2 = 5/6."),
        M("No estimar y aceptar cualquier resultado de la calculadora.", "Un error al digitar pasa inadvertido.", "Estima primero y compara con el resultado."),
    ],
    rec=[
        ex("Escribe 3/4 de metro como decimal.", "0,75 m", "3/4 = 75/100."),
        ex("Escribe 1,5 como número mixto.", "1 1/2", "0,5 = 1/2."),
        ex("Estima 5,1 + 1,9 redondeando cada número a un entero.", "7", "5 + 2 = 7."),
    ],
    und=[
        ex("Calcula 2 1/2 + 0,75.", "3,25", "2,5 + 0,75."),
        ex("Calcula 4,2 − 1 3/4.", "2,45", "1 3/4 = 1,75 y 4,20 − 1,75."),
        ex("Calcula 1/4 + 3/8 + 0,125.", "0,75", "0,25 + 0,375 + 0,125."),
    ],
    app=[
        ex("Un jarro tiene 1 1/2 L de jugo y se agregan 0,75 L. ¿Cuántos litros hay?", "2,25 L", "1,5 + 0,75."),
        ex("Un sendero mide 3 3/4 km y una persona ya recorrió 1,5 km. ¿Cuántos km le faltan?", "2,25 km", "3,75 − 1,5."),
        ex("Una cinta de 6,5 m pierde 2 3/10 m por un corte. ¿Cuántos metros quedan?", "4,2 m", "2 3/10 = 2,3 y 6,5 − 2,3."),
    ],
    rea=[
        ex("Para calcular 1/3 + 1/2, ¿conviene pasar todo a decimales o trabajar con fracciones?", "Con fracciones", "1/3 no tiene un decimal exacto; con denominador 6 resulta 5/6."),
        ex("Mario estimó que 6,1 + 2 9/10 es cerca de 9 y la calculadora dio 9. ¿Es razonable? Responde sí o no.", "Sí", "2 9/10 = 2,9 y 6,1 + 2,9 = 9."),
    ],
    cha=[
        ex("Tres cintas miden 1 1/4 m, 0,5 m y 2,75 m. ¿Cuántos metros miden juntas?", "4,5 m", "1,25 + 0,5 + 2,75."),
        ex("Calcula 10 − (3 1/2 + 2,25).", "4,25", "3,5 + 2,25 = 5,75 y 10 − 5,75."),
    ],
    ctx=[ex("Una receta usa 1 1/2 tazas de leche y 0,75 tazas de agua. ¿Cuántas tazas de líquido hay en total?", "2,25 tazas", "1,5 + 0,75 = 2,25.")],
    sc=[
        ex("Escribe 2,25 como número mixto.", "2 1/4", "0,25 = 1/4."),
        ex("Calcula 1/2 + 1/3.", "5/6", "3/6 + 2/6."),
        ex("Estima 6,9 − 2,1 redondeando a enteros.", "5", "7 − 2 = 5."),
    ],
    op=task(
        "Un tablón mide 3,2 m. Se cortan primero 1 1/4 m y después 0,6 m. Resuelve de dos maneras distintas (con decimales y con fracciones o mixtos) cuánto queda y comprueba que ambas dan lo mismo.",
        "Con decimales: 3,2 − 1,25 − 0,6 = 1,35 m. Con fracciones: 3 1/5 − 1 1/4 − 3/5 = 3 4/20 − 1 5/20 − 12/20 = 1 7/20 = 1,35. Ambas dan 1,35 m.",
        ["resuelve con dos formatos", "obtiene el mismo resultado", "responde con unidad"],
        ["dos cálculos", "comprobación de que coinciden"],
        ["mezclar formatos sin convertir", "restar mal el segundo corte"],
        "Pide que pase el resultado decimal a fracción y compare con el otro cálculo.",
    ),
    reinforce="Calcula 2 3/4 − 1,5 y 0,5 + 3/10. Hazlo en decimales.",
    extend="Inventa un problema donde convenga trabajar con fracciones y otro donde convenga trabajar con decimales. Explica por qué.",
)

# ------------------------------------------------------------------ OA 08 clase 4
lesson(
    OA8, 4,
    use="Aprenderé a resolver problemas no rutinarios con fracciones, números mixtos y decimales, con varios pasos y datos de más. Sirve para enfrentar situaciones reales donde no está dicho qué operación usar.",
    prior=["Sé elegir un formato y comprobar.", "Sé sumar y restar fracciones, mixtos y decimales."],
    explain=[
        "Un problema no rutinario no dice qué operación hacer. Tienes que leerlo con calma, hacer un esquema y decidir. A veces sobran datos y otras veces hay que calcular un dato intermedio antes de llegar a la respuesta.",
        "Una buena manera de empezar es escribir lo que sabes y lo que preguntan. Luego hacer un dibujo o una tabla. Resuelve de a un paso y escribe cada resultado con su unidad. Si la pregunta es «cuánto falta», piensa en una resta entre lo que se necesita y lo que ya se tiene.",
        "Al terminar, comprueba de dos formas: con una estimación y con una operación inversa. También conviene releer la pregunta y ver que la respuesta responde exactamente lo que se pidió, con la unidad correcta.",
    ],
    vocab=[("problema no rutinario", "problema donde hay que decidir qué hacer, no hay una receta directa"), ("dato intermedio", "resultado que se calcula en el camino a la respuesta"), ("dato de más", "información que no hace falta para responder"), ("esquema", "dibujo simple que ordena los datos"), ("verificar", "comprobar que la respuesta es correcta")],
    worked=[
        W("Dato intermedio", "Una botella de 2 L se usa así: se sirven 3/4 L y después 0,5 L. ¿Cuánto queda?", ["Lo servido: 3/4 + 0,5 = 0,75 + 0,5 = 1,25 L.", "Queda 2 − 1,25 = 0,75 L."], "0,75 L"),
        W("Cuánto falta", "Un carpintero tiene tablas de 2 1/2 m y de 1,8 m. Necesita 5 m en total. ¿Cuánto le falta?", ["2 1/2 = 2,5; 2,5 + 1,8 = 4,3 m.", "Falta 5 − 4,3 = 0,7 m."], "0,7 m"),
    ],
    mistakes=[
        M("Usar todos los datos aunque uno no se necesite.", "Se pensó que cada número debe entrar en una operación.", "Decide qué datos responden la pregunta."),
        M("Responder sin la unidad.", "Se olvidó que la respuesta es una medida.", "Escribe la unidad: L, m, kg…"),
    ],
    rec=[
        ex("Calcula 2 − 0,5.", "1,5", "2,0 − 0,5."),
        ex("Calcula 3/4 + 0,25.", "1", "0,75 + 0,25 = 1."),
        ex("Calcula 5 − 3,2.", "1,8", "5,0 − 3,2."),
    ],
    und=[
        ex("Una persona caminó 1 1/2 km, descansó y caminó 0,5 km más. ¿Cuántos km caminó en total?", "2 km", "1,5 + 0,5."),
        ex("Un bidón de 10 L tiene 7,25 L de agua. ¿Cuántos litros faltan para llenarlo?", "2,75 L", "10,00 − 7,25."),
        ex("Un trozo de cuerda mide 2,5 m y otro mide 1 3/4 m. ¿Cuánto más largo es el primero?", "0,75 m", "2,5 − 1,75."),
    ],
    app=[
        ex("Una jarra de 3 L se llena con 1 1/4 L de jugo y 0,5 L de agua. ¿Cuántos litros más caben?", "1,25 L", "1,25 + 0,5 = 1,75 y 3 − 1,75."),
        ex("En una carrera, Ana corrió 3 1/5 km, Beto 2,75 km y Carla 3,5 km. ¿Quién corrió menos y cuánto menos que Ana?", "Beto, 0,45 km menos", "3 1/5 = 3,2; 3,2 − 2,75 = 0,45."),
        ex("Una caja de 5 kg tiene 1 3/4 kg de frutas y 0,5 kg de nueces. ¿Cuánto espacio libre de peso queda?", "2,75 kg", "1,75 + 0,5 = 2,25 y 5 − 2,25."),
    ],
    rea=[
        ex("Un problema dice: «Marta tiene 3,5 m de cinta, gasta 1 1/4 m y compra una carpeta de $1.500». ¿Qué dato sobra para saber cuánta cinta queda?", "La carpeta de $1.500", "El precio de la carpeta no interviene en el cálculo de cinta."),
        ex("Un estudiante calculó 1/3 + 1/6 = 2/9 sumando arriba y abajo. ¿Cuál es el resultado correcto?", "1/2", "1/3 = 2/6, entonces 2/6 + 1/6 = 3/6 = 1/2."),
    ],
    cha=[
        ex("Un tanque tiene 8 L. El lunes se saca 1 3/4 L, el martes 2,5 L y el miércoles 1/2 L. ¿Cuántos litros quedan?", "3,25 L", "1,75 + 2,5 + 0,5 = 4,75 y 8 − 4,75."),
        ex("Dos listones suman 4 m. Uno mide 1 3/8 m. ¿Cuánto mide el otro?", "2,625 m", "1 3/8 = 1,375 y 4 − 1,375."),
    ],
    ctx=[ex("Una escuela ficticia usa 12,5 L de pintura en un salón y 8 3/4 L en otro. Tenía 25 L. ¿Cuántos litros le quedan?", "3,75 L", "12,5 + 8,75 = 21,25 y 25 − 21,25.")],
    sc=[
        ex("Calcula 1 − 0,35.", "0,65", "1,00 − 0,35."),
        ex("Una cinta de 4 m se corta en un trozo de 1 1/2 m. ¿Cuánto queda?", "2,5 m", "4 − 1,5."),
        ex("Calcula 0,5 + 1/4 + 0,125.", "0,875", "0,5 + 0,25 + 0,125."),
    ],
    op=task(
        "Resuelve este problema no rutinario y explica cada paso: «Para un afiche ficticio se compran 4 m de cinta. Se usan 1 1/2 m para el borde, 0,75 m para un lazo y 3/4 m para unas letras. Si cada metro cuesta $800, ¿cuánta cinta sobra?». Indica qué dato no necesitas.",
        "Cinta usada: 1,5 + 0,75 + 0,75 = 3 m. Sobra 4 − 3 = 1 m. El precio de $800 por metro no se necesita para esta pregunta.",
        ["suma los usos con un mismo formato", "calcula lo que sobra", "identifica el dato de más"],
        ["pasos con cálculos", "respuesta con unidad y dato que sobra"],
        ["usar el precio", "olvidar uno de los usos"],
        "Pide que sume lo usado con lo que sobra y compruebe que da 4 m.",
    ),
    reinforce="Una botella tiene 2 L. Se sirven 0,6 L y 3/10 L. Calcula cuánto queda.",
    extend="Escribe un problema de varios pasos con un dato de más que mezcle una fracción y un decimal. Resuélvelo e indica el dato que sobra.",
)
