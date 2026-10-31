"""Cuaderno del estudiante de 5.º básico Matemática: OA 02 (cálculo mental de multiplicaciones) y OA 03 (multiplicación 2 x 2 dígitos)."""
from __future__ import annotations

from student_content_ma05_a import M, W, f, lesson, task
from student_lessons import arith, ex

OA2 = "MA05 OA 02"
OA3 = "MA05 OA 03"

# ------------------------------------------------------------------ OA 02 clase 1
lesson(
    OA2, 1,
    use="Aprenderé a multiplicar mentalmente por 10, 100, 1.000 y por múltiplos de 10 anexando ceros. Sirve para calcular rápido cantidades grandes sin lápiz.",
    prior=["Sé las tablas de multiplicar hasta el 10.", "Sé que 10 decenas forman una centena y 10 centenas forman un mil."],
    explain=[
        "Al multiplicar un número por 10, por 100 o por 1.000, se anexan (se agregan a la derecha) uno, dos o tres ceros. Así 35 × 10 = 350, 35 × 100 = 3.500 y 35 × 1.000 = 35.000. Cada cero hace que el número sea diez veces mayor.",
        "Un múltiplo de 10 es un número como 40, 300 o 2.000. Se puede ver como un dígito por 10, 100 o 1.000: 40 = 4 × 10. Para calcular 6 × 40, multiplica 6 × 4 = 24 y anexa un cero: 240. Para 35 × 200, haz 35 × 2 = 70 y anexa dos ceros: 7.000.",
        "Cuando los dos factores terminan en ceros, cuenta todos los ceros finales de ambos. En 50 × 60 haces 5 × 6 = 30 y anexas dos ceros: 3.000. Cuidado: el 0 de 30 también se queda, por eso el resultado tiene tres ceros en total. Revisa siempre cuántos ceros anexaste.",
    ],
    vocab=[("anexar", "agregar ceros a la derecha de un número"), ("múltiplo de 10", "número que se forma al multiplicar 10 por otro número, como 70 o 500"), ("factor", "cada número que se multiplica"), ("producto", "resultado de una multiplicación"), ("cálculo mental", "calcular pensando, sin escribir el procedimiento")],
    worked=[
        W("Multiplicar por un múltiplo de 10", "Calcula 7 × 60 mentalmente.", ["60 es 6 × 10.", "Multiplico 7 × 6 = 42.", "Anexo un cero: 420."], "420"),
        W("Dos factores con ceros", "Calcula 50 × 400 mentalmente.", ["Los dígitos son 5 y 4: 5 × 4 = 20.", "Los factores tienen 1 + 2 = 3 ceros finales.", "Anexo tres ceros a 20: 20.000."], "20.000"),
    ],
    mistakes=[
        M("Calcular 40 × 50 como 200.", "Se multiplicó 4 × 5 = 20 y se anexó solo un cero.", "Hay un cero en 40 y uno en 50: se anexan dos ceros y queda 2.000."),
        M("Calcular 25 × 100 como 250.", "Se anexó un solo cero.", "Multiplicar por 100 anexa dos ceros: 2.500."),
    ],
    rec=[
        arith("Calcula 35 × 10.", "35*10", "Multiplicar por 10 anexa un cero."),
        arith("Calcula 8 × 100.", "8*100", "Multiplicar por 100 anexa dos ceros."),
        ex("¿Cuántos ceros se anexan al multiplicar un número por 1.000?", "3", "El factor 1.000 tiene tres ceros."),
    ],
    und=[
        arith("Multiplica mentalmente 6 × 40.", "6*40", "6 × 4 = 24 y se anexa un cero."),
        arith("Multiplica mentalmente 25 × 300.", "25*300", "25 × 3 = 75 y se anexan dos ceros."),
        arith("Multiplica mentalmente 70 × 50.", "70*50", "7 × 5 = 35 y se anexan dos ceros."),
    ],
    app=[
        arith("Un paquete tiene 20 láminas. ¿Cuántas láminas hay en 45 paquetes iguales?", "20*45", "45 × 2 = 90 y se anexa un cero."),
        arith("Una bodega guarda 60 cajas y en cada caja hay 50 frascos. ¿Cuántos frascos hay en total?", "60*50", "6 × 5 = 30 y se anexan dos ceros."),
        arith("Un tren hace un recorrido de 120 kilómetros cada día. ¿Cuántos kilómetros recorre en 300 días?", "120*300", "12 × 3 = 36 y se anexan tres ceros (uno de 120 y dos de 300).", unit=" km"),
    ],
    rea=[
        ex("Mari calculó 40 × 50 = 200. ¿Cuál es el error y cuál es el resultado correcto?", "Anexó un cero de menos; es 2.000", "4 × 5 = 20 y hay dos ceros en los factores: 2.000."),
        ex("¿Cuántos ceros tiene el producto de 500 × 4.000?", "6", "5 × 4 = 20 y se anexan cinco ceros: 2.000.000 tiene seis ceros."),
    ],
    cha=[
        ex("Un número multiplicado por 300 da 18.000. ¿Qué número es?", "60", "60 × 300: 6 × 3 = 18 y se anexan tres ceros, que da 18.000."),
        ex("Se multiplicó 25 por un número y se obtuvo 25.000. ¿Por qué número se multiplicó?", "1.000", "25 × 1.000 = 25.000: se anexaron tres ceros."),
    ],
    ctx=[arith("En una feria ficticia se arman 80 stands y cada uno recibe 600 entradas. ¿Cuántas entradas se reparten?", "80*600", "8 × 6 = 48 y se anexan tres ceros.")],
    sc=[
        arith("Calcula 9 × 70.", "9*70", "9 × 7 = 63 y se anexa un cero."),
        arith("Calcula 15 × 1.000.", "15*1000", "Se anexan tres ceros."),
        arith("Calcula 30 × 30.", "30*30", "3 × 3 = 9 y se anexan dos ceros."),
    ],
    op=task(
        "Elige uno de estos casos: 45 cajas con 20 cuadernos cada una, 600 bolsas con 30 caramelos cada una o 1.000 hojas en cada una de 12 resmas. Escribe la multiplicación, el producto calculado anexando ceros y cómo supiste cuántos ceros anexar.",
        "600 bolsas con 30 caramelos: 600 × 30. 6 × 3 = 18 y hay tres ceros en los factores, así que el producto es 18.000 caramelos.",
        ["escribe la multiplicación correcta", "calcula con el dígito y los ceros", "explica cuántos ceros anexó"],
        ["multiplicación y resultado en el cuaderno", "frase sobre los ceros"],
        ["olvidar ceros de uno de los factores", "anexar los ceros del producto parcial dos veces"],
        "Pide que cuente los ceros finales de cada factor y que compruebe con una estimación.",
    ),
    reinforce="Calcula en tu cuaderno 4 × 10, 4 × 100, 4 × 1.000 y 4 × 40. Fíjate cómo crece el número de ceros.",
    extend="Explica con un ejemplo por qué 200 × 300 tiene 4 ceros en el producto y no 5.",
)

# ------------------------------------------------------------------ OA 02 clase 2
lesson(
    OA2, 2,
    use="Aprenderé a multiplicar doblando un factor y dividiendo por 2 el otro, o doblando varias veces. Sirve para calcular mentalmente productos con 4, 5, 8, 25 y 50.",
    prior=["Sé calcular el doble y la mitad de números de dos cifras.", "Sé multiplicar por 10 y por 100."],
    explain=[
        "El doble de un número es multiplicarlo por 2. Multiplicar por 4 es doblar dos veces: 35 × 4 es 35, 70, 140. Multiplicar por 8 es doblar tres veces: 15, 30, 60, 120. Cada vez que doblas, multiplicas por 2 una vez más.",
        "También puedes dividir un factor por 2 y doblar el otro, y el producto no cambia. Por ejemplo, 16 × 25 = 8 × 50 = 4 × 100 = 400. Dividiste 16 a la mitad y doblaste 25 las veces necesarias hasta llegar a un número fácil como 100.",
        "Este método funciona bien cuando un factor es par y el otro termina en 5 o es 25, 50 o 125. Para multiplicar por 5 puedes hacer la mitad y anexar un cero: 46 × 5 es la mitad de 46 (23) y un cero, 230. Para multiplicar por 50, la mitad y dos ceros.",
    ],
    vocab=[("doble", "una cantidad multiplicada por 2"), ("mitad", "una cantidad dividida por 2"), ("doblar", "multiplicar por 2"), ("factor par", "factor que se puede dividir por 2 de forma exacta"), ("producto", "resultado de una multiplicación")],
    worked=[
        W("Doblar repetidamente", "Calcula 15 × 8 doblando.", ["8 = 2 × 2 × 2, así que doblo tres veces.", "15 → 30 → 60 → 120."], "120"),
        W("Mitad y doble", "Calcula 25 × 12 dividiendo 12 por 2 y doblando 25.", ["12 ÷ 2 = 6 y 25 × 2 = 50: 25 × 12 = 50 × 6.", "6 ÷ 2 = 3 y 50 × 2 = 100: 50 × 6 = 100 × 3.", "100 × 3 = 300."], "300"),
    ],
    mistakes=[
        M("Calcular 18 × 4 doblando una sola vez: 36.", "Multiplicar por 4 es doblar dos veces, no una.", "18 → 36 → 72. El producto es 72."),
        M("Calcular 14 × 50 dividiendo 14 por 2 pero sin doblar 50: 7 × 50 = 350.", "Si se divide un factor por 2, el otro debe doblarse.", "14 × 50 = 7 × 100 = 700."),
    ],
    rec=[
        ex("¿Cuál es el doble de 35?", "70", "35 + 35 = 70."),
        ex("¿Cuál es la mitad de 48?", "24", "24 + 24 = 48."),
        ex("Calcula 35 × 4 doblando dos veces.", "140", "35 → 70 → 140."),
    ],
    und=[
        ex("Calcula 16 × 8 doblando tres veces.", f(16 * 8), "16 → 32 → 64 → 128."),
        ex("Calcula 25 × 12 dividiendo 12 por 2 y doblando 25 las veces necesarias.", "300", "25 × 12 = 50 × 6 = 100 × 3 = 300."),
        ex("Calcula 45 × 6 dividiendo 6 por 2 y doblando 45.", f(45 * 6), "6 ÷ 2 = 3 y 45 × 2 = 90; luego 90 × 3 = 270."),
    ],
    app=[
        arith("Calcula 125 × 8 doblando 125 tres veces (125, 250, 500 y el siguiente doble).", "125*8", "Cada doble multiplica por 2; tres dobles equivalen a × 8."),
        ex("Calcula 14 × 50 dividiendo 14 por 2 y doblando 50 hasta obtener una multiplicación por 100.", "700", "14 ÷ 2 = 7 y 50 × 2 = 100; entonces 14 × 50 = 7 × 100 = 700."),
        ex("Una bolsa trae 25 galletas y se compran 12 bolsas. ¿Cuántas galletas son en total?", "300", "25 × 12: la mitad de 12 es 6 y el doble de 25 es 50; luego 100 × 3 = 300."),
    ],
    rea=[
        ex("Ana quiere calcular 18 × 4 y escribe 18 → 36 como respuesta. ¿Cuántas veces debió doblar y cuál es el producto?", "Dos veces; 72", "Multiplicar por 4 es doblar dos veces: 18, 36, 72."),
        ex("¿Cuántas veces hay que doblar un número para multiplicarlo por 16?", "4", "2 × 2 × 2 × 2 = 16, así que se dobla cuatro veces."),
    ],
    cha=[
        ex("Calcula 32 × 125 dividiendo 32 por 2 y doblando 125 repetidamente hasta que quede un factor múltiplo de 1.000.", "4.000", "32 × 125 = 16 × 250 = 8 × 500 = 4 × 1.000 = 4.000."),
        ex("Al multiplicar un número por 8 se obtiene 96. ¿Qué número es? Usa mitades repetidas.", "12", "96 → 48 → 24 → 12: se dividió tres veces por 2."),
    ],
    ctx=[ex("Un cine ficticio tiene 16 filas con 25 butacas cada una. ¿Cuántas butacas hay? Usa mitades y dobles.", "400", "25 × 16 = 50 × 8 = 100 × 4 = 400.")],
    sc=[
        ex("Calcula 15 × 4 doblando.", "60", "15 → 30 → 60."),
        ex("Calcula 18 × 5: la mitad de 18 y anexa un cero.", "90", "Mitad de 18 es 9 y se anexa un cero."),
        ex("Calcula 24 × 25 con mitades y dobles hasta llegar a 100.", "600", "24 × 25 = 12 × 50 = 6 × 100 = 600."),
    ],
    op=task(
        "Elige uno: 18 × 5, 24 × 25 o 16 × 125. Calcúlalo mentalmente usando dobles o mitades repetidas, escribe cada paso de la cadena y comprueba con otra forma, por ejemplo con una multiplicación por escrito.",
        "24 × 25: 24 → 12 y 25 → 50; 12 → 6 y 50 → 100; 6 × 100 = 600. Comprobación: 24 × 25 = 20 × 25 + 4 × 25 = 500 + 100 = 600.",
        ["escribe la cadena de pasos", "el producto es correcto", "comprueba con otro método"],
        ["pasos escritos", "comprobación"],
        ["dividir un factor sin doblar el otro", "doblar menos veces"],
        "Pide que verifique que en cada paso el producto sea el mismo y que reconozca el factor que se volvió fácil.",
    ),
    reinforce="Escribe una lista con el doble de 6, 12, 24 y 48. Luego escribe la lista de las mitades de 96, 48, 24 y 12.",
    extend="Explica por qué 16 × 25 y 4 × 100 dan el mismo resultado usando mitades y dobles.",
)

# ------------------------------------------------------------------ OA 02 clase 3
lesson(
    OA2, 3,
    use="Aprenderé a usar las propiedades conmutativa y asociativa de la multiplicación para agrupar factores y calcular más fácil. Sirve para cambiar el orden y hacer cuentas como 25 × 7 × 4 de cabeza.",
    prior=["Sé las tablas de multiplicar.", "Sé multiplicar por 10, 100 y múltiplos de 10."],
    explain=[
        "La propiedad conmutativa dice que cambiar el orden de los factores no cambia el producto. Por ejemplo, 4 × 13 = 13 × 4 = 52. La propiedad asociativa dice que, al multiplicar tres o más factores, puedes agrupar como quieras: (2 × 5) × 13 = 2 × (5 × 13) = 130.",
        "Juntas esas propiedades permiten buscar parejas fáciles. Hay parejas que forman 10, 100 o 1.000: 2 × 5 = 10, 4 × 25 = 100, 8 × 125 = 1.000. En 25 × 7 × 4 puedes cambiar el orden a 25 × 4 × 7 = 100 × 7 = 700, que es mucho más fácil.",
        "Estas propiedades sirven para la multiplicación, pero no para la resta ni la división. Por ejemplo, 8 − 3 no es igual a 3 − 8, y 12 ÷ 4 no es igual a 4 ÷ 12. Antes de reordenar, comprueba que todas las operaciones sean multiplicaciones.",
    ],
    vocab=[("propiedad conmutativa", "cambiar el orden de los factores no cambia el producto"), ("propiedad asociativa", "agrupar los factores de distinta forma no cambia el producto"), ("agrupar", "juntar factores con paréntesis"), ("factor", "cada número que se multiplica"), ("pareja fácil", "dos factores cuyo producto es 10, 100 o 1.000")],
    worked=[
        W("Buscar una pareja que forma 100", "Calcula 25 × 7 × 4.", ["Cambio el orden: 25 × 4 × 7.", "25 × 4 = 100.", "100 × 7 = 700."], "700"),
        W("Agrupar para formar 10", "Calcula 2 × 37 × 5.", ["Agrupo 2 × 5 = 10.", "10 × 37 = 370."], "370"),
    ],
    mistakes=[
        M("Decir que 12 − 5 es igual a 5 − 12 por la propiedad conmutativa.", "La conmutativa de esta clase vale para la multiplicación, no para la resta.", "12 − 5 = 7, pero 5 − 12 no da 7. Antes de reordenar, comprueba que todas las operaciones sean multiplicaciones."),
        M("Pensar que 2 × (3 × 4) = (2 × 3) + 4.", "Se cambió una multiplicación por una suma al agrupar.", "Al agrupar la operación sigue siendo multiplicar: (2 × 3) × 4 = 24."),
    ],
    rec=[
        ex("Completa: 8 × 5 = __ × 8.", "5", "Cambiar el orden de los factores no cambia el producto."),
        ex("¿Cuál es el producto de 2 × 5 ?", "10", "2 veces 5 son 10."),
        arith("Calcula 2 × 15 × 5 juntando 2 × 5 primero.", "(2*5)*15", "2 × 5 = 10 y 10 × 15 = 150."),
    ],
    und=[
        arith("Calcula 4 × 13 × 25 juntando 4 × 25.", "(4*25)*13", "4 × 25 = 100 y 100 × 13 = 1.300."),
        arith("Calcula 50 × 9 × 2 juntando 50 × 2.", "(50*2)*9", "50 × 2 = 100 y 100 × 9 = 900."),
        ex("¿Qué propiedad se usa al escribir 6 × 14 = 14 × 6?", "Conmutativa", "Se cambió el orden de los factores."),
    ],
    app=[
        arith("Una caja tiene 25 filas de 4 chocolates. Hay 8 cajas. ¿Cuántos chocolates hay, agrupando 25 × 4 primero?", "(25*4)*8", "25 × 4 = 100 y 100 × 8 = 800."),
        arith("Calcula 5 × 17 × 20 con la pareja 5 × 20.", "(5*20)*17", "5 × 20 = 100 y 100 × 17 = 1.700."),
        arith("Calcula 125 × 3 × 8 con la pareja 125 × 8.", "(125*8)*3", "125 × 8 = 1.000 y 1.000 × 3 = 3.000."),
    ],
    rea=[
        ex("Lalo calcula (4 × 12) × 25 = 48 × 25 = 1.200 y Sofi hace 4 × 25 primero y luego × 12. ¿Obtiene lo mismo?", "Sí, 1.200", "4 × 25 = 100 y 100 × 12 = 1.200: es la misma multiplicación agrupada distinto."),
        ex("Rita dice que 10 − 4 es igual que 4 − 10 por la propiedad conmutativa. ¿Tiene razón?", "No", "La conmutativa es de la multiplicación; en la resta el orden sí cambia el resultado."),
    ],
    cha=[
        ex("Completa: 8 × 25 × __ = 2.000.", "10", "8 × 25 = 200 y 200 × 10 = 2.000."),
        ex("¿Cuál es el producto 2 × 5 × 2 × 5 × 2 × 5?", "1.000", "Cada pareja 2 × 5 da 10 y hay tres: 10 × 10 × 10 = 1.000."),
    ],
    ctx=[arith("Un taller tiene 9 mesas. Cada mesa tiene 4 cajones y en cada cajón hay 25 lápices. ¿Cuántos lápices hay, agrupando 4 × 25 primero?", "(4*25)*9", "4 × 25 = 100 lápices por mesa y 100 × 9 = 900.")],
    sc=[
        arith("Calcula 2 × 23 × 5.", "(2*5)*23", "2 × 5 = 10 y 10 × 23 = 230."),
        ex("Completa: 7 × 4 × 25 = 7 × __.", "100", "4 × 25 = 100, luego 7 × 100."),
        ex("¿Cuál propiedad dice que (2 × 3) × 5 = 2 × (3 × 5)?", "Asociativa", "Se cambió la forma de agrupar los factores."),
    ],
    op=task(
        "Elige uno de estos cálculos: 25 × 9 × 4, 5 × 38 × 2 o 125 × 7 × 8. Reordénalo para formar una pareja fácil (10, 100 o 1.000), escribe los dos pasos y nombra la propiedad que usaste.",
        "25 × 9 × 4 = 25 × 4 × 9 = 100 × 9 = 900. Usé la propiedad conmutativa para cambiar el orden y juntar 25 × 4.",
        ["reordena o agrupa", "el producto es correcto", "nombra la propiedad"],
        ["pasos escritos", "nombre de la propiedad"],
        ["aplicar la propiedad a una resta", "no revisar que todas las operaciones sean multiplicaciones"],
        "Pide que verifique con calculadora o con otro orden y que identifique qué pareja fácil encontró.",
    ),
    reinforce="Escribe tres parejas de factores cuyo producto sea 10, 100 y 1.000. Usa una de ellas para calcular algo de tu casa, como filas de tarros por estantes.",
    extend="Inventa un cálculo con tres factores en el que reordenes para formar 1.000 y resuélvelo.",
)

# ------------------------------------------------------------------ OA 02 clase 4
lesson(
    OA2, 4,
    use="Aprenderé a usar la propiedad distributiva para multiplicar mentalmente, separando un factor en sumas o restas fáciles. Sirve para calcular 7 × 98 o 12 × 15 sin escribir.",
    prior=["Sé multiplicar por 10 y por 100.", "Sé sumar y restar mentalmente."],
    explain=[
        "La propiedad distributiva dice que multiplicar un número por una suma es lo mismo que multiplicar por cada sumando y luego sumar. Por ejemplo, 12 × 15 = 12 × (10 + 5) = 12 × 10 + 12 × 5 = 120 + 60 = 180. Separas el 15 en partes fáciles.",
        "También sirve con restas. Para 7 × 98 piensa 98 como 100 − 2. Entonces 7 × 98 = 7 × 100 − 7 × 2 = 700 − 14 = 686. Es útil cuando un factor está cerca de una decena, centena o mil.",
        "Al revés también sirve: si ves 8 × 13 + 8 × 7, puedes sacar el factor común 8: 8 × (13 + 7) = 8 × 20 = 160. Cuidado: debes multiplicar cada parte por el mismo factor. Si multiplicas solo una de las partes, el resultado cambia.",
    ],
    vocab=[("propiedad distributiva", "multiplicar una suma o resta por un número es multiplicar cada parte y luego sumar o restar"), ("descomponer", "separar un número en sumas o restas más fáciles"), ("factor común", "factor que se repite en dos multiplicaciones"), ("sumando", "cada número que se suma"), ("paréntesis", "signos que agrupan una operación")],
    worked=[
        W("Descomponer en una suma", "Calcula 6 × 47 mentalmente.", ["47 = 40 + 7.", "6 × 40 = 240 y 6 × 7 = 42.", "240 + 42 = 282."], "282"),
        W("Usar una resta cercana a 100", "Calcula 7 × 98 mentalmente.", ["98 = 100 − 2.", "7 × 100 = 700 y 7 × 2 = 14.", "700 − 14 = 686."], "686"),
    ],
    mistakes=[
        M("Calcular 6 × 47 como 6 × 40 + 7 = 247.", "Solo se multiplicó una de las partes.", "Cada parte se multiplica por 6: 6 × 40 + 6 × 7 = 282."),
        M("Calcular 7 × 98 como 7 × 100 + 7 × 2 = 714.", "El 98 es 100 − 2, y se sumó en vez de restar.", "Es 7 × 100 − 7 × 2 = 686."),
    ],
    rec=[
        ex("Completa: 6 × 12 = 6 × 10 + 6 × __.", "2", "12 = 10 + 2."),
        arith("Calcula 9 × 21 como 9 × 20 + 9 × 1.", "9*20+9*1", "Se multiplica cada parte por 9."),
        ex("Completa: 5 × 34 = 5 × 30 + 5 × __.", "4", "34 = 30 + 4."),
    ],
    und=[
        arith("Calcula 8 × 99 como 8 × 100 − 8 × 1.", "8*100-8*1", "99 es 100 − 1."),
        arith("Calcula 15 × 14 como 15 × 10 + 15 × 4.", "15*10+15*4", "14 = 10 + 4."),
        arith("Calcula 7 × 52 como 7 × 50 + 7 × 2.", "7*50+7*2", "52 = 50 + 2."),
    ],
    app=[
        arith("Calcula 8 × 13 + 8 × 7 sacando el factor común 8.", "8*(13+7)", "13 + 7 = 20 y 8 × 20 = 160."),
        arith("Calcula 25 × 18 como 25 × 20 − 25 × 2.", "25*20-25*2", "18 = 20 − 2."),
        arith("Una entrada cuesta $30. ¿Cuánto cuestan 19 entradas, pensando 19 como 20 − 1?", "30*20-30*1", "30 × 20 = 600 y se resta una entrada.", unit=" pesos"),
    ],
    rea=[
        ex("Pepe calculó 6 × 47 = 6 × 40 + 7 = 247. ¿Qué error cometió y cuál es el resultado correcto?", "No multiplicó el 7 por 6; es 282", "Debe ser 6 × 40 + 6 × 7 = 240 + 42."),
        ex("Cata dice que 8 × (10 + 5) = 8 × 10 + 5. ¿Es verdad?", "No", "Falta multiplicar el 5 por 8; lo correcto es 80 + 40 = 120."),
    ],
    cha=[
        arith("Calcula 99 × 48 pensando 99 como 100 − 1.", "100*48-1*48", "4.800 − 48 = 4.752."),
        ex("Si 13 × 34 = 13 × 30 + 13 × __, ¿qué número falta?", "4", "34 = 30 + 4."),
    ],
    ctx=[arith("Una escuela compra 12 cajas con 15 lápices cada una. ¿Cuántos lápices son en total, usando 12 × 10 + 12 × 5?", "12*10+12*5", "120 + 60 = 180 lápices.")],
    sc=[
        arith("Calcula 4 × 26 como 4 × 20 + 4 × 6.", "4*20+4*6", "Cada parte se multiplica por 4."),
        arith("Calcula 6 × 99 como 6 × 100 − 6 × 1.", "6*100-6*1", "99 = 100 − 1."),
        arith("Calcula 9 × 5 + 9 × 5 sacando el factor común.", "9*(5+5)", "9 × 10 = 90."),
    ],
    op=task(
        "Elige uno: 7 × 46, 6 × 98 o 12 × 25. Calcúlalo mentalmente usando la propiedad distributiva (con suma o con resta), escribe los pasos y comprueba con otra descomposición.",
        "12 × 25 = 12 × 20 + 12 × 5 = 240 + 60 = 300. Comprobación: 12 × 25 = 10 × 25 + 2 × 25 = 250 + 50 = 300.",
        ["descompone un factor", "multiplica cada parte", "comprueba con otra descomposición"],
        ["pasos escritos", "resultado comprobado"],
        ["multiplicar solo una parte", "sumar cuando había que restar"],
        "Pide que revise que cada parte se multiplicó por el mismo número y que compare los dos caminos.",
    ),
    reinforce="Calcula en tu cuaderno 5 × 12 con 5 × 10 + 5 × 2 y con 5 × 6 × 2. Mira que den lo mismo.",
    extend="Explica por qué 8 × 99 es fácil de calcular pensando en 8 × 100 y qué se debe restar.",
)

# ------------------------------------------------------------------ OA 03 clase 1
lesson(
    OA3, 1,
    use="Aprenderé a estimar productos de números de dos cifras por números de dos cifras. Sirve para saber si un resultado es razonable antes de calcularlo exacto.",
    prior=["Sé redondear números a la decena.", "Sé multiplicar por 10 y múltiplos de 10."],
    explain=[
        "Estimar un producto es calcular un valor cercano al resultado exacto, sin hacer toda la multiplicación. Primero redondea cada factor a la decena más cercana. Luego multiplica los números redondeados, que son más fáciles. Por ejemplo, 38 × 52 se estima como 40 × 50 = 2.000.",
        "Una estimación sirve para tres cosas. Permite saber de cuántas cifras será el resultado, descubrir errores grandes y elegir entre varias respuestas posibles. El resultado exacto de 38 × 52 es 1.976, que está muy cerca de 2.000.",
        "Si un factor se aproxima hacia arriba, el producto estimado tiende a ser mayor que el exacto. Si se aproxima hacia abajo, tiende a ser menor. En 38 × 52, el 38 sube a 40 y el 52 baja a 50, por eso casi se compensan. Al comunicar una estimación usa la palabra «aproximadamente».",
    ],
    vocab=[("estimar", "calcular un valor cercano sin hacer la cuenta exacta"), ("redondear", "cambiar un número por la decena más cercana"), ("producto exacto", "resultado correcto de la multiplicación"), ("aproximadamente", "cerca de, no exactamente"), ("razonable", "que tiene sentido para la situación")],
    worked=[
        W("Estimar redondeando a la decena", "Estima 38 × 52.", ["38 se redondea a 40 y 52 a 50.", "40 × 50: 4 × 5 = 20 y se anexan dos ceros.", "Resultado: 2.000."], "Aproximadamente 2.000"),
        W("Descartar una respuesta", "Un estudiante escribe 29 × 71 = 20.590. ¿Es razonable?", ["29 es casi 30 y 71 es casi 70.", "30 × 70 = 2.100, así que el resultado debe estar cerca de 2.100.", "20.590 no tiene sentido; el exacto es 2.059."], "No es razonable; el exacto es 2.059"),
    ],
    mistakes=[
        M("Estimar 38 × 52 como 30 × 50.", "Se redondeó 38 hacia abajo en vez de a la decena más cercana.", "38 está más cerca de 40; la estimación correcta es 40 × 50 = 2.000."),
        M("Estimar 41 × 19 como 40 × 10.", "Se redondeó 19 a 10 y no a 20.", "19 está más cerca de 20: 40 × 20 = 800."),
    ],
    rec=[
        ex("Redondea 47 a la decena más cercana.", "50", "47 está más cerca de 50 que de 40."),
        ex("Redondea 63 a la decena más cercana.", "60", "63 está más cerca de 60."),
        arith("Calcula 40 × 30.", "40*30", "4 × 3 = 12 y se anexan dos ceros."),
    ],
    und=[
        arith("Estima 31 × 19 redondeando cada factor a la decena: calcula 30 × 20.", "30*20", "31 se redondea a 30 y 19 a 20."),
        arith("Estima 68 × 23 redondeando: calcula 70 × 20.", "70*20", "68 se redondea a 70 y 23 a 20."),
        ex("¿Cuántas cifras tendrá aproximadamente el producto de 82 × 47?", "4", "80 × 50 = 4.000, que tiene 4 cifras."),
    ],
    app=[
        arith("Una escuela tiene 28 salas con 32 sillas cada una. Estima las sillas calculando 30 × 30.", "30*30", "Se redondean ambos factores a 30."),
        ex("Estima 49 × 51 redondeando cada factor a la decena.", "2.500", "49 se redondea a 50 y 51 a 50; 50 × 50 = 2.500."),
        ex("Sara calculó 27 × 33 = 891. ¿Es razonable si estimó 30 × 30?", "Sí", "30 × 30 = 900, muy cerca de 891."),
    ],
    rea=[
        ex("Lola estimó 38 × 52 como 40 × 50 = 2.000. El producto exacto es 1.976. ¿La estimación es mayor o menor que el exacto?", "Mayor", "2.000 > 1.976."),
        ex("Pablo dice que 89 × 11 es casi 900 × 10 = 9.000. ¿Está bien estimado?", "No", "89 se redondea a 90 y no a 900; la estimación es 90 × 10 = 900."),
    ],
    cha=[
        ex("¿Cuál es el menor producto posible de dos números de dos cifras?", "100", "10 × 10 = 100."),
        ex("¿Cuál es el mayor producto posible de dos números de dos cifras?", "9.801", "99 × 99 = 9.801."),
    ],
    ctx=[arith("Una panadería ficticia hace 38 bandejas con 21 panes cada una. Estima el total calculando 40 × 20.", "40*20", "38 se redondea a 40 y 21 a 20.")],
    sc=[
        arith("Estima 52 × 48 calculando 50 × 50.", "50*50", "Se redondean ambos factores a 50."),
        ex("Redondea 75 a la decena más cercana (si termina en 5, sube).", "80", "Si la unidad es 5 o más, la decena sube."),
        ex("Estima 19 × 21 redondeando.", "400", "19 → 20 y 21 → 20; 20 × 20 = 400."),
    ],
    op=task(
        "Elige uno de estos casos: 32 mesas con 28 libros, 47 filas con 53 asientos o 19 cajas con 61 lápices. Escribe la multiplicación, estima redondeando cada factor a la decena y explica por qué tu estimación es razonable.",
        "47 filas con 53 asientos: 47 × 53. Redondeo a 50 × 50 = 2.500. Es razonable porque ambos factores están muy cerca de 50.",
        ["redondea cada factor", "calcula la estimación", "explica si es razonable"],
        ["estimación escrita", "frase de explicación"],
        ["redondear a la decena equivocada", "no justificar la razonabilidad"],
        "Pide que compare su estimación con un cálculo exacto para ver cuán cerca quedó.",
    ),
    reinforce="Redondea a la decena los números 14, 26, 38 y 85. Luego estima 26 × 38.",
    extend="Explica cuándo una estimación sale más grande que el producto exacto y da un ejemplo.",
)

# ------------------------------------------------------------------ OA 03 clase 2
lesson(
    OA3, 2,
    use="Aprenderé a multiplicar dos números de dos cifras con descomposición y con un rectángulo de áreas. Sirve para entender de dónde salen los productos parciales del algoritmo.",
    prior=["Sé multiplicar por múltiplos de 10.", "Sé usar la propiedad distributiva."],
    explain=[
        "Para multiplicar 23 × 14, descompón los dos factores: 23 = 20 + 3 y 14 = 10 + 4. Cada parte del primer factor se multiplica por cada parte del segundo: 20 × 10 = 200, 20 × 4 = 80, 3 × 10 = 30 y 3 × 4 = 12. Después se suman los cuatro productos.",
        "Un rectángulo de áreas ayuda a ordenar esos cuatro productos. Se dibuja un rectángulo dividido en cuatro partes, con 20 y 3 arriba y 10 y 4 al costado. Cada parte guarda uno de los productos. Se suman todas las partes: 200 + 80 + 30 + 12 = 322.",
        "Otra forma es multiplicar el primer factor por 10 y luego por 4, y sumar: 23 × 10 = 230 y 23 × 4 = 92, luego 230 + 92 = 322. Las dos formas son iguales, solo cambia la manera de ordenar. Siempre revisa con una estimación: 20 × 10 = 200 y 23 × 14 debe ser mayor que 200.",
    ],
    vocab=[("producto parcial", "cada multiplicación pequeña que se suma al final"), ("rectángulo de áreas", "dibujo que ordena los productos parciales"), ("descomponer", "separar un número en decenas y unidades"), ("área", "cantidad de superficie que cubre una figura"), ("factor", "cada número que se multiplica")],
    worked=[
        W("Usar descomposición completa", "Calcula 23 × 14 descomponiendo los dos factores.", ["23 = 20 + 3 y 14 = 10 + 4.", "20 × 10 = 200; 20 × 4 = 80; 3 × 10 = 30; 3 × 4 = 12.", "200 + 80 + 30 + 12 = 322."], "322"),
        W("Descomponer un solo factor", "Calcula 36 × 25 descomponiendo 25 en 20 + 5.", ["36 × 20 = 720.", "36 × 5 = 180.", "720 + 180 = 900."], "900"),
    ],
    mistakes=[
        M("Calcular 23 × 14 como 20 × 10 + 3 × 4 = 212.", "Se olvidaron dos productos parciales: 20 × 4 y 3 × 10.", "Cada parte de un factor se multiplica por cada parte del otro: 200 + 80 + 30 + 12 = 322."),
        M("Calcular 36 × 25 como 36 × 20 = 720 y olvidar el 36 × 5.", "Solo se multiplicó por una parte del factor.", "También hay que multiplicar por 5 y sumar: 720 + 180 = 900."),
    ],
    rec=[
        ex("Descompón 23 en decenas y unidades.", "20 + 3", "23 tiene 2 decenas y 3 unidades."),
        arith("Calcula 20 × 10.", "20*10", "2 × 1 = 2 y se anexan dos ceros."),
        arith("Calcula 3 × 12.", "3*12", "Es 3 × 10 + 3 × 2 = 36."),
    ],
    und=[
        arith("En 13 × 12 calcula los cuatro productos parciales sumados: 10 × 10 + 10 × 2 + 3 × 10 + 3 × 2.", "10*10+10*2+3*10+3*2", "Son 100 + 20 + 30 + 6."),
        arith("Calcula 25 × 14 como 25 × 10 + 25 × 4.", "25*10+25*4", "250 + 100."),
        ex("En un rectángulo de áreas de 31 × 22 se usan los lados 30 + 1 y 20 + 2. ¿Cuánto vale la parte de 30 × 20?", "600", "3 × 2 = 6 y se anexan dos ceros."),
    ],
    app=[
        arith("Calcula 32 × 15 descomponiendo 15 en 10 + 5.", "32*10+32*5", "320 + 160."),
        arith("Calcula 41 × 23 con los cuatro productos parciales: 40 × 20 + 40 × 3 + 1 × 20 + 1 × 3.", "40*20+40*3+1*20+1*3", "800 + 120 + 20 + 3."),
        arith("Un estacionamiento ficticio tiene 18 filas con 24 espacios cada una. ¿Cuántos espacios hay? Descompón 24 en 20 + 4.", "18*20+18*4", "360 + 72 espacios."),
    ],
    rea=[
        ex("Gabo calculó 23 × 14 como 200 + 12 = 212. ¿Qué productos parciales olvidó?", "20 × 4 y 3 × 10", "Esos dos productos suman 80 + 30 = 110; el total debe ser 322."),
        ex("¿Es cierto que 24 × 15 = 24 × 10 + 24 × 5?", "Sí", "15 = 10 + 5, y se multiplica cada parte por 24: 240 + 120 = 360."),
    ],
    cha=[
        ex("Un rectángulo de áreas tiene partes 600, 90, 40 y 6. ¿Qué multiplicación de dos cifras por dos cifras representa?", "32 × 23 (o 23 × 32)", "Las partes son 30 × 20, 30 × 3, 2 × 20 y 2 × 3, o sea (30 + 2) × (20 + 3) = 32 × 23."),
        ex("Si 35 × 12 = 420, ¿cuánto es 35 × 13?", "455", "35 × 13 es 35 más que 35 × 12: 420 + 35 = 455."),
    ],
    ctx=[arith("Un curso ficticio de 22 estudiantes reúne $15 cada uno para una colecta. ¿Cuánto reúnen? Usa 22 × 10 + 22 × 5.", "22*10+22*5", "220 + 110 pesos.")],
    sc=[
        arith("Calcula 12 × 13 con productos parciales: 10 × 10 + 10 × 3 + 2 × 10 + 2 × 3.", "10*10+10*3+2*10+2*3", "100 + 30 + 20 + 6."),
        arith("Calcula 45 × 11 como 45 × 10 + 45 × 1.", "45*10+45*1", "450 + 45."),
        arith("Calcula 16 × 20 + 16 × 4.", "16*20+16*4", "Es 16 × 24: 320 + 64."),
    ],
    op=task(
        "Elige uno: 26 × 14, 33 × 21 o 18 × 35. Calcúlalo con un rectángulo de áreas, dibuja las cuatro partes con sus productos y suma. Comprueba con una estimación.",
        "33 × 21: 30 × 20 = 600, 30 × 1 = 30, 3 × 20 = 60, 3 × 1 = 3. Total 693. Estimación 30 × 20 = 600, cerca de 693.",
        ["dibuja las cuatro partes", "calcula cada producto parcial", "suma y comprueba con estimación"],
        ["rectángulo dibujado", "suma final", "estimación"],
        ["olvidar un producto parcial", "sumar mal los productos"],
        "Pide que cuente las cuatro partes del rectángulo y que compare el resultado con la estimación.",
    ),
    reinforce="Dibuja un rectángulo para 12 × 11 y escribe los cuatro productos parciales. Suma para comprobar que sale 132.",
    extend="Explica por qué en 23 × 14 aparecen cuatro productos parciales y no dos.",
)

# ------------------------------------------------------------------ OA 03 clase 3
lesson(
    OA3, 3,
    use="Aprenderé el algoritmo de la multiplicación de dos cifras por dos cifras con productos parciales. Sirve para multiplicar rápido y ordenado números más grandes.",
    prior=["Sé multiplicar un número de dos cifras por uno de una cifra.", "Sé descomponer con rectángulos de áreas."],
    explain=[
        "El algoritmo escrito pone un factor sobre el otro y alinea las unidades. Primero multiplicas todo el número de arriba por la cifra de las unidades de abajo. Ese es el primer producto parcial. Por ejemplo, en 47 × 36, primero haces 47 × 6 = 282.",
        "Después multiplicas por la cifra de las decenas de abajo, que vale 30. Por eso escribes un cero en las unidades y continúas: 47 × 3 = 141, o sea 1.410. Ese es el segundo producto parcial. Si no pones el cero, el resultado queda diez veces más pequeño.",
        "Al final sumas los dos productos parciales: 282 + 1.410 = 1.692. Si hay llevadas, anótalas con cuidado y súmalas a la cifra siguiente. Para comprobar, estima: 47 × 36 es casi 50 × 40 = 2.000, y 1.692 es cercano. También puedes intercambiar factores y calcular 36 × 47.",
    ],
    vocab=[("algoritmo", "procedimiento ordenado de pasos para calcular"), ("producto parcial", "resultado de multiplicar por una sola cifra del otro factor"), ("llevada", "cantidad que se suma a la cifra de la izquierda"), ("alinear", "poner las cifras una bajo otra según su lugar"), ("comprobar", "revisar que el resultado tenga sentido")],
    worked=[
        W("Aplicar el algoritmo", "Calcula 47 × 36.", ["47 × 6 = 282 (primer producto parcial).", "47 × 30 = 1.410: escribo un cero y multiplico 47 × 3 = 141.", "Sumo 282 + 1.410 = 1.692.", "Estimo: 50 × 40 = 2.000, cercano a 1.692."], "1.692"),
        W("Detectar un resultado exagerado", "Un estudiante calcula 28 × 14 y obtiene 3.920. ¿Está bien?", ["Estimo: 28 es casi 30 y 14 es casi 15; 30 × 15 = 450.", "28 × 14 debe estar cerca de 400.", "3.920 es casi diez veces más: error en los lugares. El resultado es 392."], "392"),
    ],
    mistakes=[
        M("Calcular 47 × 36 y sumar 282 + 141 = 423.", "No se escribió el cero en el segundo producto parcial.", "Es 1.410: 282 + 1.410 = 1.692."),
        M("Calcular 24 × 13 como 72 + 24 = 96.", "El segundo producto parcial se multiplicó por 1 y no por 10.", "24 × 3 = 72 y 24 × 10 = 240; sumados dan 312."),
    ],
    rec=[
        arith("Calcula 47 × 6.", "47*6", "40 × 6 = 240 y 7 × 6 = 42."),
        arith("Calcula 47 × 30.", "47*30", "47 × 3 = 141 y se anexa un cero."),
        arith("Suma los productos parciales 282 + 1.410.", "282+1410", "Se suman los dos productos parciales."),
    ],
    und=[
        arith("Calcula 24 × 13 con el algoritmo.", "24*13", "24 × 3 = 72 y 24 × 10 = 240."),
        arith("Calcula 36 × 25 con el algoritmo.", "36*25", "36 × 5 = 180 y 36 × 20 = 720."),
        ex("En 52 × 41, ¿cuál es el segundo producto parcial?", "2.080", "52 × 40 = 2.080 (52 × 4 = 208 y un cero)."),
    ],
    app=[
        arith("Una sala tiene 28 filas con 35 sillas. ¿Cuántas sillas hay?", "28*35", "28 × 5 = 140 y 28 × 30 = 840."),
        arith("Un camión carga 64 cajas de 48 kilos cada una. ¿Cuántos kilos carga?", "64*48", "64 × 8 = 512 y 64 × 40 = 2.560.", unit=" kg"),
        arith("Calcula 73 × 56.", "73*56", "73 × 6 = 438 y 73 × 50 = 3.650."),
    ],
    rea=[
        ex("Nico calcula 47 × 36 y obtiene 423. ¿Cuál fue su error?", "No puso el cero en el segundo producto parcial", "Debió sumar 282 + 1.410 = 1.692."),
        ex("Una estimación de 62 × 38 es 60 × 40 = 2.400. Un estudiante obtuvo 23.560. ¿Está bien?", "No", "El resultado debe estar cerca de 2.400; el exacto es 2.356."),
    ],
    cha=[
        ex("Si 36 × 2_ = 36 × 20 + 180, ¿qué cifra va en el espacio?", "5", "36 × 5 = 180, así que el factor es 25."),
        ex("Si 45 × 18 = 810, ¿cuánto es 45 × 19 sin repetir toda la cuenta?", "855", "45 × 19 = 45 × 18 + 45 = 810 + 45."),
    ],
    ctx=[arith("Un taller ficticio fabrica 45 sillas al mes durante 12 meses. ¿Cuántas sillas hace en el año?", "45*12", "45 × 2 = 90 y 45 × 10 = 450.")],
    sc=[
        arith("Calcula 21 × 34.", "21*34", "34 × 1 = 34 y 34 × 20 = 680."),
        arith("Calcula 55 × 22.", "55*22", "55 × 2 = 110 y 55 × 20 = 1.100."),
        ex("En 36 × 24, ¿por qué se escribe un cero en el segundo producto parcial?", "Porque se multiplica por 20, no por 2", "El 2 de las decenas vale 20."),
    ],
    op=task(
        "Elige uno: 38 × 27, 54 × 63 o 76 × 41. Resuélvelo con el algoritmo, escribe los dos productos parciales y comprueba con una estimación y con el cambio de orden de los factores.",
        "38 × 27: 38 × 7 = 266; 38 × 20 = 760; suma 1.026. Estimación 40 × 30 = 1.200 (cercana). Cambio de orden: 27 × 38 = 27 × 8 + 27 × 30 = 216 + 810 = 1.026.",
        ["escribe dos productos parciales", "suma bien", "comprueba de dos formas"],
        ["algoritmo escrito", "estimación", "cambio de orden"],
        ["no escribir el cero", "errores de llevadas"],
        "Pide que revise cada producto parcial por separado y que compare su estimación con el resultado.",
    ),
    reinforce="Resuelve 14 × 12, 23 × 21 y 31 × 15 con el algoritmo y estima cada uno antes de calcular.",
    extend="Explica con tus palabras por qué el segundo producto parcial siempre termina en cero.",
)

# ------------------------------------------------------------------ OA 03 clase 4
lesson(
    OA3, 4,
    use="Aprenderé a resolver problemas rutinarios y no rutinarios que usan multiplicaciones de dos cifras por dos cifras, y a comprobar mis respuestas. Sirve para decidir qué operación usar en situaciones reales.",
    prior=["Sé estimar productos de dos cifras.", "Sé aplicar el algoritmo de la multiplicación."],
    explain=[
        "Un problema rutinario se resuelve aplicando directamente una operación conocida, como «hay 24 bolsas con 36 frutas cada una, ¿cuántas frutas hay?». Un problema no rutinario pide pensar más: puede tener un dato extra, pedir varios pasos o preguntar por un factor desconocido.",
        "Para resolver cualquier problema sigue cuatro pasos. Primero lee y subraya los datos y la pregunta. Segundo, decide la operación y estima el resultado. Tercero, calcula con el algoritmo, con descomposición o con una propiedad. Cuarto, comprueba si la respuesta es razonable y escríbela con su unidad.",
        "En los problemas no rutinarios conviene hacer un dibujo o una tabla. Si se pide un factor desconocido, usa la operación inversa: si 24 × __ = 864, divide 864 ÷ 24 = 36. Si un dato sobra, no lo uses. Siempre responde la pregunta con una frase completa.",
    ],
    vocab=[("problema rutinario", "problema que se resuelve con una operación conocida"), ("problema no rutinario", "problema que exige pensar la estrategia, con varios pasos o datos distintos"), ("dato", "información que entrega el problema"), ("operación inversa", "operación que deshace a otra, como dividir para deshacer una multiplicación"), ("unidad", "lo que se cuenta o mide en la respuesta")],
    worked=[
        W("Problema rutinario", "Una escuela compra 24 cajas con 36 libros cada una. ¿Cuántos libros compra?", ["Operación: 24 × 36.", "Estimo: 20 × 40 = 800.", "24 × 6 = 144 y 24 × 30 = 720; 144 + 720 = 864."], "864 libros"),
        W("Problema con dato que sobra", "Un curso tiene 32 estudiantes, cada uno lleva 15 láminas y 3 lápices. ¿Cuántas láminas llevan en total?", ["Los lápices no se usan para la pregunta.", "32 × 15 = 32 × 10 + 32 × 5 = 320 + 160.", "480 láminas."], "480 láminas"),
    ],
    mistakes=[
        M("En el problema de 32 estudiantes con 15 láminas y 3 lápices, calcular 32 × 15 × 3.", "Se usó un dato que no pedía la pregunta.", "Solo se piden las láminas: 32 × 15 = 480."),
        M("Responder solo «864» sin la unidad.", "La respuesta no dice qué se contó.", "Escribe «864 libros»."),
    ],
    rec=[
        ex("Hay 12 bolsas con 15 naranjas cada una. ¿Qué operación resuelve el total de naranjas?", "12 × 15", "Grupos iguales: bolsas por naranjas por bolsa."),
        arith("Calcula 12 × 15.", "12*15", "12 × 10 + 12 × 5."),
        ex("Marca el dato que sobra: «Una caja trae 24 galletas, cuesta $1.200 y se compran 15 cajas. ¿Cuántas galletas son?»", "$1.200", "El precio no se necesita para contar galletas."),
    ],
    und=[
        arith("Una biblioteca tiene 18 estantes con 24 libros cada uno. ¿Cuántos libros hay?", "18*24", "18 × 4 = 72 y 18 × 20 = 360."),
        ex("Estima 48 × 52 redondeando cada factor a la decena.", "2.500", "48 se redondea a 50 y 52 a 50; 50 × 50 = 2.500."),
        arith("Un bus recorre 48 kilómetros por viaje. ¿Cuántos kilómetros recorre en 25 viajes?", "48*25", "48 × 5 = 240 y 48 × 20 = 960.", unit=" km"),
    ],
    app=[
        arith("En un teatro ficticio hay 26 filas con 32 butacas. Si se venden todas, ¿cuántas entradas son?", "26*32", "26 × 2 = 52 y 26 × 30 = 780."),
        arith("Una fábrica pone 36 botellas en cada caja y arma 45 cajas. ¿Cuántas botellas empaca?", "36*45", "36 × 5 = 180 y 36 × 40 = 1.440."),
        arith("Un álbum tiene 18 páginas con 12 cuadros por página. ¿Cuántos cuadros hay en 3 álbumes iguales?", "18*12*3", "18 × 12 = 216 y 216 × 3 = 648."),
    ],
    rea=[
        ex("Si 24 × __ = 864, ¿qué número falta?", "36", "864 ÷ 24 = 36."),
        ex("Sofía dice que 37 × 22 es cercano a 800 porque 40 × 20 = 800. ¿Es razonable?", "Sí", "37 × 22 = 814, muy cerca de 800."),
    ],
    cha=[
        ex("Un agricultor ficticio tiene 25 huertos con 36 plantas en cada uno. Vende 120 plantas. ¿Cuántas le quedan?", "780", "25 × 36 = 900 y 900 − 120 = 780."),
        ex("Dos buses llevan 36 pasajeros cada uno en 12 viajes. ¿Cuántos pasajeros transportan en total?", "864", "2 × 36 = 72 y 72 × 12 = 864."),
    ],
    ctx=[arith("En un campeonato ficticio hay 14 equipos con 18 jugadores cada uno. ¿Cuántos jugadores participan?", "14*18", "14 × 8 = 112 y 14 × 10 = 140; suma 252.")],
    sc=[
        arith("Calcula 23 × 17.", "23*17", "23 × 7 = 161 y 23 × 10 = 230."),
        ex("Si cada caja tiene 24 bolsas y hay 16 cajas, ¿cuántas bolsas hay en total?", "384", "24 × 16 = 24 × 10 + 24 × 6 = 240 + 144."),
        ex("Si 30 × 40 = 1.200, ¿esta estimación sirve para 29 × 41 ?", "Sí", "Los factores son cercanos a 30 y 40."),
    ],
    op=task(
        "Resuelve uno de estos problemas y comprueba tu respuesta con una estimación: (a) 35 cajas con 24 lápices cada una; (b) un autobús de 42 asientos en 28 viajes llenos; (c) 52 semanas con 15 horas de estudio cada semana. Escribe operación, estimación, cálculo y respuesta con unidad.",
        "(a) 35 × 24. Estimación: 40 × 20 = 800. Cálculo: 35 × 4 = 140 y 35 × 20 = 700; 840. Respuesta: 840 lápices.",
        ["elige y escribe la operación", "estima antes de calcular", "responde con unidad"],
        ["operación y cálculo", "estimación", "frase de respuesta"],
        ["usar una operación equivocada", "no comprobar"],
        "Pide que compare estimación y resultado exacto y que reconozca si la unidad de la respuesta es la correcta.",
    ),
    reinforce="Escribe un problema de multiplicación con números de dos cifras sobre algo de tu casa, resuélvelo y estima antes.",
    extend="Inventa un problema no rutinario con un dato que sobre y pide a otra persona que lo resuelva.",
)
