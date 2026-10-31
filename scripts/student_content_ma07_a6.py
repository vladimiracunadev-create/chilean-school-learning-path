"""Cuaderno del estudiante de 7.º básico Matemática: OA 09 (ecuaciones e inecuaciones lineales)."""
from __future__ import annotations

from student_lessons import ex
from student_content_ma07_a import M, W, lesson, task

OA9 = "MA07 OA 09"

# ------------------------------------------------------------------ OA 09 clase 1
lesson(
    OA9, 1,
    use="Aprenderé a escribir ecuaciones de las formas ax = b y x/a = b a partir de situaciones. Sirve para encontrar un valor desconocido en problemas de compras, repartos y medidas.",
    prior=["Sé qué es una ecuación y una incógnita.", "Sé multiplicar y dividir números naturales."],
    explain=[
        "Una ecuación es una igualdad que contiene una incógnita, una letra que representa un valor que no conocemos. En este cuaderno los números a, b y las soluciones serán naturales (1, 2, 3, …) y a nunca es 0. Hay dos formas que se repiten mucho: ax = b y x/a = b. La primera dice «a veces x es igual a b»; la segunda, «x repartido en a partes iguales es b».",
        "Para modelar, primero decide qué es la incógnita y escríbelo: «x es el precio de un cuaderno». Después busca la relación. Si hay una cantidad que se repite varias veces, usa ax = b. Si hay algo que se reparte en partes iguales, usa x/a = b. Por ejemplo, 5 entradas iguales que cuestan $12.500 se escriben 5x = 12.500. Un monto que se reparte entre 6 personas y toca $8.000 a cada una se escribe x/6 = 8.000.",
        "Las palabras ayudan: «el doble», «el triple» y «veces» llevan multiplicación (2x, 3x); «la mitad», «la tercera parte» y «repartido en» llevan división (x/2, x/3). Una vez planteada, la ecuación se puede revisar probando valores: el valor correcto hace que los dos lados valgan lo mismo. Por ejemplo, para 9x = 72 prueba x = 8: 9 · 8 = 72, es correcto.",
    ],
    vocab=[("ecuación", "igualdad con un valor desconocido"), ("incógnita", "letra que representa el valor que se busca"), ("ax = b", "ecuación en que a veces la incógnita es igual a b"), ("x/a = b", "ecuación en que la incógnita dividida entre a es igual a b"), ("modelar", "traducir una situación a una ecuación")],
    worked=[
        W("Modelar una compra", "Carlos compra 6 cuadernos iguales y paga $5.400. Escribe una ecuación para el precio de un cuaderno.", ["Sea c el precio de un cuaderno. Seis cuadernos cuestan 6 veces c.", "La ecuación es 6c = 5.400."], "6c = 5.400"),
        W("Modelar un reparto", "Una cinta se corta en 5 trozos iguales y cada trozo mide 12 cm. Escribe una ecuación para el largo de la cinta.", ["Sea x el largo de la cinta. Al repartirla en 5 partes iguales, x/5 es lo que mide cada trozo.", "La ecuación es x/5 = 12."], "x/5 = 12"),
    ],
    mistakes=[
        M("Escribir «el triple de un número es 21» como x + 3 = 21.", "Se tradujo «triple» como sumar 3.", "El triple es 3 veces el número: 3x = 21."),
        M("Plantear un reparto entre 4 personas como 4x = 100.", "Se usó multiplicación en un reparto.", "Repartir en partes iguales es dividir: x/4 = 100 si cada una recibe 100."),
    ],
    rec=[
        ex("Escribe la ecuación: «el doble de un número es 18».", "2x = 18", "El doble es 2 veces el número."),
        ex("Escribe la ecuación: «un número dividido entre 3 es 7».", "x/3 = 7", "Dividir entre 3 se escribe x/3."),
        ex("En 4x = 20, ¿qué significa 4x?", "4 veces x", "Entre el número y la letra se omite el signo de multiplicar."),
    ],
    und=[
        ex("Siete paquetes de ejemplo con x galletas cada uno suman 56 galletas. Escribe la ecuación.", "7x = 56", "Siete veces x galletas es 56."),
        ex("Una suma x de dinero se reparte entre 5 personas y cada una recibe $3.000. Escribe la ecuación.", "x/5 = 3.000", "El reparto en partes iguales es una división."),
        ex("Escribe la ecuación: «la cuarta parte de un número es 6».", "x/4 = 6", "La cuarta parte es dividir entre 4."),
    ],
    app=[
        ex("9 filas iguales con x sillas cada una suman 72 sillas. Escribe la ecuación y di cuál valor la cumple: 6, 8 o 9.", "9x = 72; x = 8", "9 · 8 = 72."),
        ex("Un premio de ejemplo se reparte entre 4 ganadores y cada uno recibe $15.000. Escribe la ecuación y di cuál valor de x la cumple: 45.000, 60.000 o 75.000.", "x/4 = 15.000; x = 60.000", "60.000 ÷ 4 = 15.000."),
        ex("Una caja de ejemplo tiene 12 lápices. Hay x cajas iguales y en total 84 lápices. Escribe la ecuación y di cuál valor la cumple: 6, 7 u 8.", "12x = 84; x = 7", "12 · 7 = 84."),
    ],
    rea=[
        ex("Tomás planteó «el triple de un número es 21» como x + 3 = 21. ¿Está bien? Si no, escribe la ecuación correcta.", "No; es 3x = 21", "El triple es 3 veces el número, no sumar 3."),
        ex("¿Dicen lo mismo x/4 = 5 y 4x = 5? Responde sí o no.", "No", "La primera tiene solución x = 20; la segunda, 4x = 5, no tiene solución natural."),
    ],
    cha=[
        ex("¿Tienen la misma solución las ecuaciones x/6 = 7 y 7x = 42?", "No", "La primera da x = 42 y la segunda da x = 6."),
        ex("Un terreno rectangular de ejemplo mide 8 m de ancho y x m de largo y su área es 96 m². Escribe la ecuación y encuentra x.", "8x = 96; x = 12", "El área es ancho por largo y 8 · 12 = 96."),
    ],
    ctx=[ex("Un curso de ejemplo se divide en 5 grupos iguales de 6 estudiantes. Escribe la ecuación con x como el total de estudiantes y encuentra x.", "x/5 = 6; x = 30", "30 estudiantes divididos en 5 grupos dan 6 por grupo.")],
    sc=[
        ex("Escribe la ecuación: «5 veces un número es 40».", "5x = 40", "5 veces x se escribe 5x."),
        ex("Escribe la ecuación: «la mitad de un número es 9».", "x/2 = 9", "La mitad es dividir entre 2."),
        ex("¿Cuál valor cumple 3x = 21: 6 o 7?", "7", "3 · 7 = 21."),
    ],
    op=task(
        "Lee estas cuatro situaciones de ejemplo. (a) Ocho amigos pagan en total $24.000 por entradas iguales. (b) Un jugo de x mL se sirve en 6 vasos iguales y cada vaso tiene 250 mL. (c) El triple de la edad de Pía es 36. (d) Una cuerda de x metros se corta en 4 trozos iguales de 3 m. Para cada una define la incógnita, escribe la ecuación y prueba un valor para comprobar que la cumple.",
        "(a) 8x = 24.000, x = 3.000 (precio de una entrada). (b) x/6 = 250, x = 1.500. (c) 3x = 36, x = 12. (d) x/4 = 3, x = 12.",
        ["define la incógnita en cada caso", "escribe ecuaciones del tipo correcto", "prueba un valor"],
        ["cuatro ecuaciones", "pruebas numéricas"],
        ["usar multiplicación cuando se reparte", "no decir qué significa la letra"],
        "Pide que lea cada ecuación en voz alta con palabras y compare con el enunciado.",
    ),
    reinforce="Escribe una ecuación del tipo ax = b y otra del tipo x/a = b a partir de situaciones con dinero.",
    extend="Escribe un problema cuya ecuación sea 15x = 450 y otro cuya ecuación sea x/15 = 450. Explica por qué los resultados son tan distintos.",
)

# ------------------------------------------------------------------ OA 09 clase 2
lesson(
    OA9, 2,
    use="Aprenderé a resolver ecuaciones de las formas ax = b y x/a = b usando operaciones inversas. Sirve para calcular precios, cantidades y medidas desconocidas.",
    prior=["Sé modelar situaciones con ecuaciones.", "Sé que la multiplicación y la división se deshacen entre sí."],
    explain=[
        "Una ecuación es como una balanza en equilibrio: lo que haces de un lado debes hacerlo del otro. En ax = b, la incógnita está multiplicada por a. Para dejar sola la x, divide ambos lados por a: x = b ÷ a. Por ejemplo, 6x = 48 se resuelve dividiendo por 6: x = 8.",
        "En x/a = b, la incógnita está dividida entre a. Para dejarla sola, multiplica ambos lados por a: x = b · a. Por ejemplo, x/7 = 5 da x = 5 · 7 = 35. En cada paso se usa la operación inversa de la que aparece en la ecuación: la inversa de multiplicar es dividir y la inversa de dividir es multiplicar.",
        "Después de resolver, comprueba. Sustituye el valor en la ecuación original: con x = 8 en 6x = 48 sale 6 · 8 = 48, correcto. Si un valor no la cumple, hubo un error. A veces b no se puede dividir exactamente entre a. En este cuaderno buscamos soluciones naturales, así que 5x = 12 no tiene solución natural, porque 12 ÷ 5 no es entero.",
    ],
    vocab=[("operación inversa", "operación que deshace otra"), ("equilibrio", "igualdad que se mantiene al hacer lo mismo en ambos lados"), ("despejar", "dejar la incógnita sola en un lado de la ecuación"), ("sustituir", "reemplazar la letra por un número"), ("solución", "valor que hace verdadera la ecuación")],
    worked=[
        W("Resolver ax = b", "Resuelve 6x = 48.", ["Divido ambos lados por 6: x = 48 ÷ 6 = 8.", "Compruebo: 6 · 8 = 48."], "x = 8"),
        W("Resolver x/a = b", "Resuelve x/7 = 5.", ["Multiplico ambos lados por 7: x = 5 · 7 = 35.", "Compruebo: 35 ÷ 7 = 5."], "x = 35"),
    ],
    mistakes=[
        M("Resolver x/5 = 9 como x = 9 ÷ 5.", "Se usó la operación equivocada.", "Se deshace una división multiplicando: x = 9 · 5 = 45."),
        M("Resolver 4x = 28 como x = 28 − 4 = 24.", "Se restó en vez de dividir.", "Se deshace una multiplicación dividiendo: x = 28 ÷ 4 = 7."),
    ],
    rec=[
        ex("Resuelve 2x = 14.", "x = 7", "14 ÷ 2 = 7."),
        ex("Resuelve x/3 = 4.", "x = 12", "4 · 3 = 12."),
        ex("Para resolver 5x = 30, ¿qué operación se hace en ambos lados?", "Dividir entre 5", "Dividir deshace la multiplicación por 5."),
    ],
    und=[
        ex("Resuelve 9x = 63.", "x = 7", "63 ÷ 9 = 7."),
        ex("Resuelve x/8 = 6.", "x = 48", "6 · 8 = 48."),
        ex("Resuelve 11x = 132.", "x = 12", "132 ÷ 11 = 12."),
    ],
    app=[
        ex("4 paquetes iguales de ejemplo contienen 240 hojas en total. Plantea 4x = 240 y encuentra cuántas hojas tiene un paquete.", "60", "240 ÷ 4 = 60."),
        ex("Un premio se reparte entre 6 personas y cada una recibe $15.000. Plantea x/6 = 15.000 y encuentra el premio total.", "$90.000", "15.000 · 6 = 90.000."),
        ex("7 entradas iguales cuestan $24.500. Plantea 7x = 24.500 y encuentra el precio de una entrada.", "$3.500", "24.500 ÷ 7 = 3.500."),
    ],
    rea=[
        ex("Eva resolvió x/4 = 9 y obtuvo x = 9 ÷ 4. ¿Está bien? Si no, escribe la solución correcta.", "No; x = 36", "Se multiplica por 4, no se divide."),
        ex("¿La ecuación 5x = 12 tiene solución natural?", "No", "12 ÷ 5 = 2,4, que no es natural."),
    ],
    cha=[
        ex("Resuelve 15x = 405.", "x = 27", "405 ÷ 15 = 27."),
        ex("Se sabe que x/12 = 25. ¿Cuánto vale x/6?", "50", "x = 300 y 300 ÷ 6 = 50."),
    ],
    ctx=[ex("Un estanque de ejemplo entrega 18 L en cada una de sus mangueras iguales y en total entrega 126 L. Plantea 18x = 126 y encuentra cuántas mangueras hay.", "7", "126 ÷ 18 = 7.")],
    sc=[
        ex("Resuelve 8x = 72.", "x = 9", "72 ÷ 8."),
        ex("Resuelve x/4 = 15.", "x = 60", "15 · 4."),
        ex("Comprueba si x = 6 es solución de 7x = 48.", "No", "7 · 6 = 42, no 48."),
    ],
    op=task(
        "Resuelve estas cuatro ecuaciones de ejemplo y comprueba cada una sustituyendo: (a) 12x = 108; (b) x/9 = 7; (c) 16x = 112; (d) x/15 = 4. Para cada una escribe qué operación hiciste en ambos lados y por qué. Después inventa una ecuación del tipo ax = b que no tenga solución natural y explica por qué.",
        "(a) x = 9. (b) x = 63. (c) x = 7. (d) x = 60. Ejemplo sin solución natural: 5x = 12, porque 12 no se puede dividir exactamente entre 5.",
        ["usa la operación inversa correcta", "comprueba cada solución", "inventa una ecuación sin solución natural y la justifica"],
        ["cuatro resoluciones", "cuatro comprobaciones", "ecuación inventada"],
        ["usar la misma operación del enunciado", "no comprobar"],
        "Pide que lea la ecuación como pregunta («¿qué número multiplicado por 12 da 108?») y que compruebe.",
    ),
    reinforce="Resuelve 4x = 36 y x/6 = 8. Comprueba las dos soluciones.",
    extend="Resuelve 7x = 91 y explica con la balanza dibujada qué hiciste en cada lado.",
)

# ------------------------------------------------------------------ OA 09 clase 3
lesson(
    OA9, 3,
    use="Aprenderé a escribir y representar inecuaciones de las formas ax < b, ax > b, x/a < b y x/a > b. Sirve para describir límites, como «menos de 600 kg» o «más de $15.000».",
    prior=["Sé resolver ecuaciones ax = b y x/a = b.", "Sé ubicar números en la recta numérica."],
    explain=[
        "Una inecuación es una desigualdad con una incógnita. El signo < significa «menor que» y > significa «mayor que». Por ejemplo, 3x < 12 dice: «el triple de un número es menor que 12». A diferencia de una ecuación, una inecuación suele tener muchas soluciones. El conjunto solución son todos los valores que la hacen verdadera. Aquí trabajaremos con números naturales.",
        "Para resolverla, haz las mismas operaciones que en una ecuación: 3x < 12 se divide por 3 y queda x < 4. Los naturales que cumplen son 1, 2 y 3; el 4 no, porque 3 · 4 = 12 no es menor que 12. En x/2 > 5, se multiplica por 2 y queda x > 10; los naturales son 11, 12, 13… sin fin. Al multiplicar o dividir por un número positivo, el sentido de la desigualdad no cambia.",
        "En la recta numérica se marca un círculo vacío en el valor límite, que no es solución, y una flecha hacia donde están las soluciones. Para x < 4 la flecha va hacia la izquierda, y para x > 10 hacia la derecha. Revisa siempre probando: un número dentro de la zona debe cumplir la inecuación y el valor límite no debe cumplirla.",
    ],
    vocab=[("inecuación", "desigualdad con una incógnita"), ("<", "signo «menor que»"), (">", "signo «mayor que»"), ("conjunto solución", "todos los valores que cumplen la inecuación"), ("valor límite", "número que separa las soluciones de las que no lo son; no se incluye")],
    worked=[
        W("Resolver ax < b", "Resuelve 3x < 12 en los naturales.", ["Divido ambos lados entre 3: x < 4.", "Los naturales menores que 4 son 1, 2 y 3. Compruebo: 3 · 3 = 9 < 12 y 3 · 4 = 12 no es menor que 12."], "x < 4; soluciones 1, 2 y 3"),
        W("Resolver x/a > b", "Resuelve x/2 > 5 en los naturales.", ["Multiplico ambos lados por 2: x > 10.", "Los naturales mayores que 10 son 11, 12, 13… Compruebo: 11 ÷ 2 = 5,5 > 5."], "x > 10; soluciones 11, 12, 13…"),
    ],
    mistakes=[
        M("Decir que x = 6 es solución de 2x < 12.", "Se usó el valor límite.", "2 · 6 = 12 no es menor que 12. Con < no se incluye el límite."),
        M("Escribir la solución de x/2 > 5 como x > 5/2.", "Se dividió en vez de multiplicar.", "Se deshace la división multiplicando por 2: x > 10."),
    ],
    rec=[
        ex("¿Es x = 3 solución de 2x < 9? Responde sí o no.", "Sí", "2 · 3 = 6 y 6 < 9."),
        ex("¿Es x = 5 solución de x/5 > 2? Responde sí o no.", "No", "5 ÷ 5 = 1 y 1 no es mayor que 2."),
        ex("¿Qué signo corresponde a «menos de»: < o >?", "<", "Menos de significa menor que."),
    ],
    und=[
        ex("Resuelve 4x < 20 en los naturales y escribe la desigualdad que cumple x.", "x < 5", "20 ÷ 4 = 5."),
        ex("Resuelve x/3 > 4 y escribe la desigualdad que cumple x.", "x > 12", "4 · 3 = 12."),
        ex("Escribe todos los naturales que cumplen 5x < 23.", "1, 2, 3 y 4", "x < 4,6 y los naturales menores son 1, 2, 3 y 4."),
    ],
    app=[
        ex("Un ascensor de ejemplo soporta menos de 600 kg. Cada persona pesa 75 kg. ¿Cuántas personas como máximo pueden subir?", "7", "75x < 600 da x < 8; el mayor natural es 7."),
        ex("Se necesitan más de 30 L de agua y se usa un balde de 4 L. ¿Cuántos baldes llenos, como mínimo, hay que echar?", "8", "4x > 30 da x > 7,5 y el menor natural es 8."),
        ex("Una persona ahorra $2.000 cada semana y quiere reunir más de $15.000. ¿Cuántas semanas, como mínimo, necesita?", "8 semanas", "2.000x > 15.000 da x > 7,5; el menor natural es 8."),
    ],
    rea=[
        ex("Pablo dice que 4 es solución de 3x < 12 porque 3 · 4 = 12. ¿Tiene razón?", "No", "12 no es menor que 12."),
        ex("¿Es 10 solución de x/2 > 5? Responde sí o no.", "No", "10 ÷ 2 = 5 y 5 no es mayor que 5."),
    ],
    cha=[
        ex("¿Cuántos naturales cumplen 7x < 50?", "7", "x < 7,14…, así que son 1, 2, 3, 4, 5, 6 y 7."),
        ex("¿Cuántos naturales cumplen a la vez 3x > 10 y 2x < 17?", "5", "x > 3,33… y x < 8,5; son 4, 5, 6, 7 y 8."),
    ],
    ctx=[ex("Una caja de ejemplo puede llevar menos de 20 kg. Cada paquete pesa 3 kg. ¿Cuántos paquetes, como máximo, caben?", "6", "3x < 20 da x < 6,67 y el mayor natural es 6.")],
    sc=[
        ex("¿Es x = 4 solución de 6x < 30? Responde sí o no.", "Sí", "6 · 4 = 24 y 24 < 30."),
        ex("Resuelve 2x > 14.", "x > 7", "14 ÷ 2 = 7."),
        ex("En la recta numérica, ¿en x < 5 la flecha va hacia la izquierda o hacia la derecha?", "Izquierda", "Los valores menores están a la izquierda."),
    ],
    op=task(
        "Dibuja tres rectas numéricas del 0 al 14. En la primera representa x < 6; en la segunda, x > 9; en la tercera, la solución de 3x < 15. En cada una marca un círculo vacío en el valor límite, dibuja la flecha y escribe los primeros valores naturales que son solución. Luego prueba dos valores en cada inecuación: uno que la cumpla y uno que no.",
        "x < 6: soluciones 1, 2, 3, 4, 5; límite 6. x > 9: soluciones 10, 11, 12…; límite 9. 3x < 15 equivale a x < 5: soluciones 1, 2, 3, 4. Pruebas: 4 cumple 3x < 15 (12 < 15) y 5 no (15 no es menor que 15).",
        ["marca el círculo vacío en el límite", "dibuja la flecha en el sentido correcto", "prueba un valor que cumple y otro que no"],
        ["tres rectas numéricas", "dos pruebas por inecuación"],
        ["incluir el valor límite", "cambiar el sentido de la flecha"],
        "Pide que sustituya el valor límite y vea que no cumple la desigualdad.",
    ),
    reinforce="Resuelve 5x < 40 y x/4 > 3. Escribe tres naturales que cumplan cada una.",
    extend="Explica por qué la inecuación x/5 > 2 tiene infinitas soluciones naturales y 5x < 20 solo tiene un número finito.",
)

# ------------------------------------------------------------------ OA 09 clase 4
lesson(
    OA9, 4,
    use="Aprenderé a resolver problemas de la vida diaria y de otras asignaturas con ecuaciones e inecuaciones. Sirve para tomar decisiones con dinero, tiempo, distancias y capacidad.",
    prior=["Sé resolver ecuaciones e inecuaciones.", "Sé modelar situaciones con ecuaciones."],
    explain=[
        "Para resolver un problema sigue seis pasos. Primero, lee y define la incógnita. Segundo, decide si es una ecuación (un valor exacto) o una inecuación (más de, menos de). Tercero, plantea. Cuarto, resuelve con operaciones inversas. Quinto, interpreta la solución en el contexto. Sexto, comprueba y responde con unidad.",
        "Las palabras clave ayudan. «Exactamente», «es igual a» y «en total» indican una ecuación. «Más de» y «menos de» indican una inecuación. Si un problema pregunta «cuántos como máximo» o «como mínimo», hay que tomar el natural mayor que cumple (máximo) o el menor que cumple (mínimo). Por ejemplo, si 6x < 50, x < 8,33 y el máximo es 8.",
        "Esto aparece en otras asignaturas. En Ciencias, distancia = rapidez · tiempo es de la forma ax = b: si un tren va a 90 km/h y recorre 360 km, 90t = 360 y t = 4 horas. En Tecnología, la capacidad máxima de una caja se expresa con una inecuación. Revisa que la solución sea posible en el contexto, por ejemplo, no puede haber 3,5 personas.",
    ],
    vocab=[("contexto", "situación concreta del problema"), ("como máximo", "el mayor valor natural que cumple una desigualdad con <"), ("como mínimo", "el menor valor natural que cumple una desigualdad con >"), ("rapidez", "distancia recorrida por unidad de tiempo"), ("interpretar", "explicar qué significa la solución en la situación")],
    worked=[
        W("Problema con ecuación", "Una persona gana $4.500 por hora. ¿Cuántas horas debe trabajar para ganar exactamente $27.000?", ["Sea x las horas: 4.500x = 27.000.", "x = 27.000 ÷ 4.500 = 6. Compruebo: 4.500 · 6 = 27.000."], "6 horas"),
        W("Problema con inecuación", "Una caja soporta menos de 50 kg y cada paquete pesa 6 kg. ¿Cuántos paquetes caben como máximo?", ["Sea x los paquetes: 6x < 50, entonces x < 8,33…", "El mayor natural es 8. Compruebo: 6 · 8 = 48 < 50 y 6 · 9 = 54 no cumple."], "8 paquetes"),
    ],
    mistakes=[
        M("Responder 8,33 paquetes en el problema de la caja.", "No se interpretó la solución en el contexto.", "Los paquetes son enteros: el máximo es 8."),
        M("Escribir «una persona pesa menos de 60 kg» como x = 60.", "Se usó una ecuación para un límite.", "«Menos de» se escribe con una desigualdad: x < 60."),
    ],
    rec=[
        ex("Un cuaderno cuesta $900. ¿Cuántos cuadernos se pueden comprar con exactamente $4.500?", "5", "900x = 4.500 da x = 5."),
        ex("Si x/4 = 12, ¿cuánto vale x?", "48", "12 · 4."),
        ex("Se arman paquetes de 5 hojas con 40 hojas en total. ¿Cuántos paquetes se arman?", "8", "5x = 40 da x = 8."),
    ],
    und=[
        ex("Un tren de ejemplo va a 90 km/h. ¿En cuántas horas recorre 360 km?", "4 horas", "90t = 360 da t = 4."),
        ex("Una mochila puede llevar menos de 12 kg y cada libro pesa 2 kg. ¿Cuántos libros como máximo caben?", "5", "2x < 12 da x < 6 y el mayor natural es 5."),
        ex("Un premio se reparte entre 6 personas y cada una recibe $120.000 (x/6 = 120.000). ¿Cuánto era el premio?", "$720.000", "120.000 · 6."),
    ],
    app=[
        ex("Una persona ahorra $3.000 por semana. ¿Cuántas semanas necesita, como mínimo, para reunir más de $20.000?", "7 semanas", "3.000x > 20.000 da x > 6,67 y el menor natural es 7."),
        ex("Un jardinero reparte 144 plantas en macetas con 9 plantas cada una. ¿Cuántas macetas necesita?", "16", "9x = 144 da x = 16."),
        ex("Un jugo se sirve en 8 vasos iguales de 250 mL cada uno (x/8 = 250). ¿Cuántos mL de jugo había en total?", "2.000 mL", "250 · 8 = 2.000."),
    ],
    rea=[
        ex("Ema dice que para «más de 20 kg» con paquetes de 4 kg basta con resolver 4x = 20. ¿Cuántos paquetes, como mínimo, hay que juntar para pasar de 20 kg?", "6", "4x > 20 da x > 5, y el menor natural es 6."),
        ex("Una balanza de ejemplo exige un peso menor que 10 kg. Rosa dice que 10 kg está permitido. ¿Tiene razón?", "No", "El enunciado dice «menor que», así que 10 no cumple."),
    ],
    cha=[
        ex("Un estanque de 600 L se llena con una llave que entrega 25 L por minuto. ¿Cuántos minutos demora? Si solo se dispone de menos de 20 minutos, ¿alcanza?", "24 minutos; no alcanza", "25x = 600 da x = 24, que no es menor que 20."),
        ex("Daniel dice que x = 24 cumple x/4 > 6. ¿Tiene razón? Si no, ¿cuál es el menor natural que cumple?", "No; el menor es 25", "24 ÷ 4 = 6 no es mayor que 6; con 25, 25 ÷ 4 = 6,25."),
    ],
    ctx=[ex("En una clase de Ciencias de ejemplo, un ciclista va a 15 km/h. ¿Cuántas horas, como mínimo, necesita para recorrer más de 50 km?", "4 horas", "15t > 50 da t > 3,33 y el menor natural es 4.")],
    sc=[
        ex("En un curso de ejemplo se forman 2 filas iguales con 15 estudiantes cada una. Si x/2 = 15, ¿cuántos estudiantes hay en total?", "30", "15 · 2 = 30."),
        ex("Un lápiz cuesta $350. ¿Cuántos lápices se pueden comprar con menos de $2.000? Escribe el máximo.", "5", "350x < 2.000 da x < 5,71 y el máximo es 5."),
        ex("Resuelve 13x = 91.", "x = 7", "91 ÷ 13."),
    ],
    op=task(
        "Lee esta situación de ejemplo: una cooperativa tiene $96.000 para comprar pelotas que cuestan $4.000 cada una y quiere repartirlas en partes iguales entre 8 cursos. (a) Escribe y resuelve la ecuación para saber cuántas pelotas se compran con todo el dinero. (b) Escribe y resuelve la ecuación para saber cuántas pelotas recibe cada curso. (c) Si solo pueden gastar menos de $60.000, escribe la inecuación y di cuántas pelotas como máximo se pueden comprar.",
        "(a) 4.000x = 96.000, x = 24. (b) y/8 = 3 cuando y = 24: cada curso recibe 3. (c) 4.000x < 60.000 da x < 15, el máximo es 14.",
        ["plantea ecuaciones e inecuación correctas", "resuelve con operaciones inversas", "interpreta el máximo en el contexto"],
        ["tres planteamientos", "respuestas con unidad"],
        ["incluir el valor límite en la inecuación", "no interpretar la solución"],
        "Pide que explique por qué 15 pelotas no cumplen «menos de $60.000».",
    ),
    reinforce="Una entrada cuesta $2.500. ¿Cuántas entradas se pueden comprar con exactamente $17.500? ¿Y con menos de $10.000, como máximo?",
    extend="Escribe un problema que se resuelva con la inecuación 5x > 42 y que pida el menor natural que cumple.",
)

# ------------------------------------------------------------------ OA 09 clase 5
lesson(
    OA9, 5,
    use="Aprenderé a comprobar mis soluciones y a comunicar el conjunto solución con símbolos, con la recta numérica y con palabras. Sirve para explicar mis resultados con claridad.",
    prior=["Sé resolver ecuaciones e inecuaciones.", "Sé representar desigualdades en la recta numérica."],
    explain=[
        "Comunicar bien una solución significa escribirla de tres maneras que dicen lo mismo. Con símbolos: x < 6. Con una lista (en los naturales): {1, 2, 3, 4, 5}. Con la recta numérica: círculo vacío en 6 y flecha hacia la izquierda. Una ecuación tiene un solo valor, por ejemplo x = 8; una inecuación tiene un conjunto de valores.",
        "Para comprobar una inecuación usa dos pruebas. Primero, un valor del conjunto debe cumplir: en 5x < 30, el 5 cumple, porque 25 < 30. Segundo, el valor límite y uno más allá no deben cumplir: el 6 da 30, que no es menor que 30. Con esas dos pruebas te aseguras de no haber olvidado ni agregado un valor. Para una ecuación basta sustituir el valor encontrado.",
        "Al responder un problema, di qué significa la solución: «Se pueden comprar como máximo 4 baldes» o «La solución son los números naturales mayores que 12». Si el conjunto es infinito, usa puntos suspensivos: {13, 14, 15, …}. Escribe siempre la desigualdad y la interpretación, no solo el número.",
    ],
    vocab=[("conjunto solución", "todos los valores que cumplen la ecuación o inecuación"), ("llaves { }", "símbolos para escribir un conjunto"), ("valor límite", "número que separa lo que cumple de lo que no cumple"), ("infinito", "que no termina"), ("comunicar", "explicar un resultado de modo claro")],
    worked=[
        W("Comunicar una inecuación", "Resuelve 5x < 30 y comunica el conjunto solución.", ["Divido entre 5: x < 6. Naturales: 1, 2, 3, 4 y 5.", "Compruebo: 5 · 5 = 25 < 30 cumple, 5 · 6 = 30 no cumple."], "x < 6; {1, 2, 3, 4, 5}"),
        W("Conjunto infinito", "Resuelve x/3 > 4 y comunica el conjunto solución.", ["Multiplico por 3: x > 12.", "Naturales: 13, 14, 15… Compruebo: 13 ÷ 3 = 4,33 > 4 cumple; 12 ÷ 3 = 4 no cumple."], "x > 12; {13, 14, 15, …}"),
    ],
    mistakes=[
        M("Escribir el conjunto solución de 4x < 20 como {1, 2, 3, 4, 5}.", "Se incluyó el valor límite 5.", "4 · 5 = 20 no es menor que 20. El conjunto es {1, 2, 3, 4}."),
        M("Escribir solo «x = 6» como respuesta de x < 6.", "Se confundió una inecuación con una ecuación.", "La solución de x < 6 es el conjunto {1, 2, 3, 4, 5}."),
    ],
    rec=[
        ex("Escribe con una lista el conjunto solución de x < 5 en los naturales.", "{1, 2, 3, 4}", "Son los naturales menores que 5."),
        ex("¿Cuál es el menor natural que cumple x > 7?", "8", "7 no es mayor que 7."),
        ex("¿Cuántos naturales cumplen 2x < 6?", "2", "x < 3, así que son 1 y 2."),
    ],
    und=[
        ex("Resuelve 6x < 40 y escribe el mayor natural que cumple.", "6", "x < 6,67 y el mayor natural es 6."),
        ex("Resuelve x/2 > 9 y escribe el menor natural que cumple.", "19", "x > 18 y el menor natural es 19."),
        ex("Resuelve 3x > 14 y escribe el menor natural que cumple.", "5", "x > 4,67 y el menor natural es 5."),
    ],
    app=[
        ex("Un museo de ejemplo permite menos de 120 personas por hora. Se entra en grupos de 8. ¿Cuántos grupos como máximo pueden entrar?", "14", "8x < 120 da x < 15 y el mayor natural es 14."),
        ex("Se quiere pagar más de $18.000 solo con billetes de $5.000. ¿Cuántos billetes, como mínimo, se necesitan?", "4", "5.000x > 18.000 da x > 3,6 y el menor natural es 4."),
        ex("Resuelve x/4 > 6 y escribe los tres menores naturales que cumplen.", "25, 26 y 27", "x > 24, así que los primeros son 25, 26 y 27."),
    ],
    rea=[
        ex("¿Pertenece 11 al conjunto solución de x/2 > 5? Responde sí o no.", "Sí", "11 ÷ 2 = 5,5 y 5,5 > 5."),
        ex("Luis escribió el conjunto solución de 3x < 12 como {1, 2, 3, 4}. ¿Cuál es el conjunto correcto?", "{1, 2, 3}", "El 4 da 12, que no es menor que 12."),
    ],
    cha=[
        ex("¿Cuántos naturales cumplen a la vez x > 3 y x < 8?", "4", "Son 4, 5, 6 y 7."),
        ex("¿Cuántos naturales cumplen a la vez 2x < 31 y x/3 > 2?", "9", "x < 15,5 y x > 6, así que son 7, 8, …, 15."),
    ],
    ctx=[ex("Una escuela de ejemplo abre un taller si se inscriben más de 25 estudiantes. Si cada curso aporta 6 estudiantes, ¿cuántos cursos, como mínimo, hacen falta?", "5", "6x > 25 da x > 4,17 y el menor natural es 5.")],
    sc=[
        ex("Resuelve 7x < 35 y escribe el mayor natural que cumple.", "4", "x < 5, así que el mayor es 4."),
        ex("¿Es x = 3 solución de x/3 > 1? Responde sí o no.", "No", "3 ÷ 3 = 1 y 1 no es mayor que 1."),
        ex("¿El conjunto solución de x > 10 en los naturales es finito o infinito?", "Infinito", "Siempre hay un natural mayor."),
    ],
    op=task(
        "Resuelve las tres relaciones de ejemplo y comunica cada solución con símbolos, lista (o primeros valores) y recta numérica: (a) 4x = 36; (b) 5x < 27; (c) x/6 > 3. Para (b) y (c), comprueba un valor que pertenece al conjunto y otro que no pertenece. Escribe una frase que interprete (b) como «máximo de cajas» si cada caja pesa 5 kg y el límite es 27 kg.",
        "(a) x = 9. (b) x < 5,4, es decir, {1, 2, 3, 4, 5}; 5 cumple (25 < 27) y 6 no (30). (c) x > 18, es decir, {19, 20, 21, …}; 19 cumple (3,17 > 3) y 18 no (3 no es mayor que 3). Interpretación: se pueden cargar como máximo 5 cajas.",
        ["resuelve las tres relaciones", "comprueba un valor dentro y otro fuera", "interpreta el resultado con una frase"],
        ["soluciones con símbolos y lista", "rectas numéricas", "frase de interpretación"],
        ["incluir el valor límite", "no dar el sentido de la flecha"],
        "Pide que lea el conjunto solución y que compruebe el valor límite.",
    ),
    reinforce="Resuelve 8x < 50 y x/5 > 4. Escribe el mayor natural de la primera y el menor de la segunda.",
    extend="Escribe una inecuación de la forma ax < b cuyo conjunto solución en los naturales sea exactamente {1, 2, 3, 4, 5, 6}.",
)
