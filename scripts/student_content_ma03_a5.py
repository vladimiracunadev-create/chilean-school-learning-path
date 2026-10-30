"""Student material for 3.º básico Matemática, OA 08 (multiplicación y tablas hasta 10)."""
from __future__ import annotations

from student_content_ma03_a import task
from student_lessons import arith, ex, register

OA8 = "MA03 OA 08"


def arr(rows: int, cols: int) -> str:
    """Arreglo de puntos: cada fila separada por «/»."""
    return " / ".join(" ".join(["●"] * cols) for _ in range(rows))


register(
    OA8, 1,
    materials="Lápiz, cuaderno y 24 tapas o porotos para armar grupos. Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé que una multiplicación es una suma de grupos iguales. Sirve para contar rápido cuando hay muchos grupos con la misma cantidad.",
    prior=["Sé sumar números de una y dos cifras.", "Sé contar de 2 en 2, de 5 en 5 y de 10 en 10."],
    explain=[
        "Un grupo igual es un conjunto con la misma cantidad de objetos que otro. Si hay 4 bolsas con 3 naranjas cada una, hay 4 grupos de 3. Para saber el total puedes sumar: 3 + 3 + 3 + 3 = 12. Esto se llama adición repetida.",
        "La multiplicación escribe lo mismo de forma corta. Se escribe 4 × 3 = 12 y se lee «cuatro por tres es igual a doce». El primer número dice cuántos grupos hay, y el segundo cuántos objetos hay en cada grupo.",
        "Ojo: 4 × 3 no es 4 + 3. Significa sumar el 3 cuatro veces. Solo se puede escribir como suma repetida cuando todos los sumandos son iguales: 5 + 5 + 5 sí, pero 5 + 6 + 7 no. Si dudas, arma los grupos con tapas.",
    ],
    vocab=[("grupo", "conjunto de objetos que se miran juntos"), ("grupos iguales", "grupos con la misma cantidad de objetos"), ("adición repetida", "suma en que se repite el mismo sumando"), ("multiplicación", "operación que cuenta grupos iguales, se escribe con ×"), ("por", "se lee así el signo × en una multiplicación")],
    worked=[
        {"title": "De grupos a multiplicación", "problem": "Hay 4 bolsas con 3 naranjas cada una. ¿Cuántas naranjas hay?", "steps": ["Son 4 grupos de 3.", "Adición repetida: 3 + 3 + 3 + 3 = 12.", "Multiplicación: 4 × 3 = 12."], "answer": "12 naranjas"},
        {"title": "De suma repetida a multiplicación", "problem": "Escribe 6 + 6 + 6 como multiplicación.", "steps": ["El sumando que se repite es 6.", "Se repite 3 veces, hay 3 grupos de 6.", "Entonces es 3 × 6 y 6 + 6 + 6 = 18."], "answer": "3 × 6 = 18"},
    ],
    mistakes=[
        {"wrong": "Escribir 4 × 5 = 4 + 5 = 9.", "why": "Se suman los dos números en vez de repetir uno de ellos.", "fix": "4 × 5 es 5 + 5 + 5 + 5 = 20."},
        {"wrong": "Escribir 5 + 6 + 7 como 3 × 6.", "why": "Los sumandos no son iguales, no son grupos iguales.", "fix": "Solo se escribe como multiplicación cuando todos los sumandos son iguales."},
    ],
    tiers={
        "recovery": [
            ex("Escribe como suma repetida: 4 grupos de 3.", "3 + 3 + 3 + 3 = 12", "Se repite 3 cuatro veces."),
            arith("Hay 5 platos con 2 galletas cada uno. ¿Cuántas galletas hay en total?", "2+2+2+2+2", "Se suma 2 cinco veces."),
            ex("Escribe 6 + 6 + 6 como multiplicación.", "3 × 6 = 18", "Son 3 grupos de 6."),
        ],
        "understand": [
            ex("En 4 × 3, ¿qué indica el 4 y qué indica el 3?", "El 4 son los grupos y el 3 lo que hay en cada grupo", "El primer número cuenta grupos y el segundo, objetos por grupo."),
            ex("¿Dan lo mismo 3 + 3 + 3 + 3 y 4 × 3?", "Sí, 12", "La multiplicación es esa suma repetida."),
            ex("¿Es 5 + 5 + 5 una suma repetida? ¿Y 5 + 6 + 7?", "La primera sí, la segunda no", "Solo la primera repite el mismo sumando."),
        ],
        "apply": [
            arith("Una caja tiene 4 lápices. ¿Cuántos lápices hay en 6 cajas?", "4*6", "Son 6 grupos de 4, o sea 4 + 4 + 4 + 4 + 4 + 4."),
            arith("Cada mesa tiene 5 sillas y hay 7 mesas. ¿Cuántas sillas hay?", "5*7", "Son 7 grupos de 5."),
            arith("Hay 9 pares de calcetines, con 2 calcetines cada par. ¿Cuántos calcetines hay?", "9*2", "Son 9 grupos de 2."),
        ],
        "reason": [
            ex("Tomás escribió 4 × 5 = 4 + 5 = 9. ¿Qué error cometió y cuál es el resultado?", "No repitió el 5; es 20", "4 × 5 = 5 + 5 + 5 + 5."),
            ex("¿Cuál es mayor: 5 grupos de 4 o 4 grupos de 4?", "5 grupos de 4", "20 es mayor que 16."),
        ],
        "challenge": [
            ex("Escribe 7 × 3 como suma repetida y calcula.", "3 + 3 + 3 + 3 + 3 + 3 + 3 = 21", "Siete grupos de 3."),
            arith("Un tren tiene 8 vagones con 9 personas cada uno. ¿Cuántas personas hay?", "8*9", "Son 8 grupos de 9."),
        ],
    },
    context=[arith("Una panadería pone 4 panes en cada bolsa y vende 5 bolsas. ¿Cuántos panes vendió?", "4*5", "Son 5 grupos de 4 panes.")],
    selfcheck=[
        ex("2 + 2 + 2 es lo mismo que ___ × 2.", "3", "Hay tres veces el 2."),
        ex("¿Cuánto es 5 + 5 + 5?", "15", "Tres grupos de 5."),
        ex("¿Cuánto es 10 + 10 + 10 + 10?", "40", "Cuatro grupos de 10."),
    ],
    open_task=task(
        "Con 24 tapas arma grupos iguales de tres tamaños distintos, usando todas las tapas cada vez y sin que sobre ninguna. Para cada forma escribe la suma repetida y la multiplicación.",
        "Una posibilidad: 6 grupos de 4: 4+4+4+4+4+4 = 24, 6 × 4 = 24. 4 grupos de 6: 6+6+6+6 = 24, 4 × 6 = 24. 3 grupos de 8: 8+8+8 = 24, 3 × 8 = 24.",
        ["arma grupos iguales", "escribe la suma repetida", "escribe la multiplicación", "el total es 24"],
        ["grupos armados o dibujados", "sumas y multiplicaciones escritas"],
        ["grupos desiguales", "sumar los dos factores"],
        "Reconoce los grupos formados y pregunta qué dice cada número; si hay error, que cuente las tapas de cada grupo.",
    ),
    reinforce="Dibuja 3 grupos de 5 puntos y 5 grupos de 3 puntos y escribe la multiplicación de cada uno.",
    extend="Con 12 tapas, ¿puedes armar grupos iguales de 5 sin que sobre ninguna? ¿Y grupos de 4? Explica y escribe la multiplicación que sirva.",
)

register(
    OA8, 2,
    materials="Lápiz, cuaderno cuadriculado y tapas. Los arreglos están dibujados con ● en los ejercicios: cada fila se separa con «/».",
    use="Aprenderé a ordenar objetos en filas y columnas y a ver que 3 × 5 y 5 × 3 dan lo mismo. Sirve para calcular rápido y para recordar las tablas.",
    prior=["Sé que una multiplicación cuenta grupos iguales.", "Sé contar de 2 en 2, de 5 en 5 y de 10 en 10."],
    explain=[
        "Un arreglo ordena objetos en filas y columnas. Las filas van de lado a lado y las columnas de arriba hacia abajo. Un arreglo de 3 filas con 5 puntos cada una se escribe 3 × 5 y tiene 15 puntos.",
        "Si giras el arreglo, las 3 filas pasan a ser 3 columnas, y hay 5 filas de 3. Es el mismo arreglo, con los mismos 15 puntos. Por eso 3 × 5 = 5 × 3. Cambiar el orden de los números no cambia el resultado.",
        "Esta propiedad se llama conmutatividad. Sirve para recordar menos tablas: si sabes que 8 × 6 = 48, sabes que 6 × 8 = 48. Pero cuidado: el significado cambia, porque 8 × 6 son 8 grupos de 6 y 6 × 8 son 6 grupos de 8.",
    ],
    vocab=[("arreglo", "objetos ordenados en filas y columnas"), ("fila", "línea de objetos de lado a lado"), ("columna", "línea de objetos de arriba hacia abajo"), ("conmutatividad", "propiedad: cambiar el orden de los números no cambia el producto"), ("producto", "resultado de una multiplicación")],
    worked=[
        {"title": "Contar un arreglo", "problem": f"Cuenta los puntos del arreglo: {arr(3, 4)}.", "steps": ["Hay 3 filas y 4 puntos en cada una.", "Escribo 3 × 4.", "4 + 4 + 4 = 12."], "answer": "3 × 4 = 12"},
        {"title": "Girar el arreglo", "problem": "Si 3 × 5 = 15, ¿cuánto es 5 × 3?", "steps": ["Un arreglo de 3 filas de 5 tiene 15 puntos.", "Al girarlo hay 5 filas de 3.", "Tiene los mismos puntos."], "answer": "5 × 3 = 15"},
    ],
    mistakes=[
        {"wrong": "Decir que 3 × 5 y 5 × 3 son resultados distintos.", "why": "Se piensa que el orden cambia el total.", "fix": "Gira el arreglo: los puntos son los mismos, 15."},
        {"wrong": "Contar un arreglo de 3 filas y 4 columnas como 3 + 4 = 7.", "why": "Se suman filas y columnas en vez de contar los puntos.", "fix": "Cada fila tiene 4 puntos y hay 3 filas: 3 × 4 = 12."},
    ],
    tiers={
        "recovery": [
            ex(f"Cuenta los puntos del arreglo: {arr(3, 4)}.", "12", "Hay 3 filas de 4 puntos."),
            ex("Un arreglo tiene 2 filas de 6 puntos. ¿Cuántos puntos tiene?", "12", "6 + 6 = 12."),
            ex("Si 3 × 5 = 15, ¿cuánto es 5 × 3?", "15", "Es el mismo arreglo girado."),
        ],
        "understand": [
            ex("Un arreglo de 3 filas de 5 puntos se gira y queda con 5 filas de 3. ¿Cambió la cantidad de puntos?", "No, siguen siendo 15", "Girar no agrega ni quita puntos."),
            ex("¿Dan lo mismo 3 × 7 y 7 × 3?", "Sí, 21", "Es la conmutatividad."),
            ex(f"Escribe la multiplicación (filas × columnas) del arreglo {arr(2, 4)}.", "2 × 4 = 8", "2 filas de 4 puntos."),
        ],
        "apply": [
            arith("Un patio tiene baldosas en 5 filas de 4 baldosas cada una. ¿Cuántas baldosas hay?", "5*4", "Son 5 grupos de 4."),
            ex("Si 8 × 6 = 48, ¿cuánto es 6 × 8?", "48", "El orden no cambia el producto."),
            arith("Un cine tiene 9 filas de 7 asientos. ¿Cuántos asientos hay?", "9*7", "Son 9 grupos de 7."),
        ],
        "reason": [
            ex("Ana dice que 4 × 9 es mayor que 9 × 4. ¿Tiene razón?", "No, ambos son 36", "El orden no cambia el producto."),
            ex("Un arreglo tiene 3 filas de 4 puntos. Al girarlo, ¿cuántas filas y cuántos puntos por fila tiene?", "4 filas de 3 puntos", "Las filas pasan a ser columnas."),
        ],
        "challenge": [
            ex("Con 12 puntos se pueden formar arreglos en filas y columnas, por ejemplo 2 × 6 o 3 × 4. Si un arreglo girado se cuenta como el mismo, ¿cuántos arreglos distintos hay con 12 puntos?", "3", "Son 1 × 12, 2 × 6 y 3 × 4; 4 × 3, 6 × 2 y 12 × 1 son los mismos girados."),
            arith("Un arreglo tiene 6 filas y 10 columnas. ¿Cuántos puntos tiene?", "6*10", "Son 6 grupos de 10."),
        ],
    },
    context=[arith("Un huerto tiene 7 hileras con 3 lechugas cada una. ¿Cuántas lechugas hay?", "7*3", "Son 7 grupos de 3. También se puede ver como 3 grupos de 7.")],
    selfcheck=[
        ex("¿Cuánto es 2 × 9? ¿Y 9 × 2?", "18 y 18", "Dan el mismo producto."),
        ex("Un arreglo tiene 4 filas de 5. ¿Cuántos puntos?", "20", "5 + 5 + 5 + 5."),
        ex("En un arreglo, ¿las filas van de lado a lado o de arriba hacia abajo?", "De lado a lado", "Las columnas van de arriba hacia abajo."),
    ],
    open_task=task(
        "Con 18 tapas arma un arreglo de 3 filas y 6 columnas. Dibújalo, escribe su multiplicación, gíralo y escribe la nueva multiplicación. Explica qué cambió y qué no.",
        "3 filas de 6: 3 × 6 = 18. Al girarlo hay 6 filas de 3: 6 × 3 = 18. Cambió el orden de las filas y columnas, pero siguen siendo 18 tapas.",
        ["arma o dibuja el arreglo", "escribe 3 × 6 y 6 × 3", "el total es 18 en ambos", "explica qué cambió y qué no"],
        ["arreglo dibujado", "multiplicaciones escritas", "frase de explicación"],
        ["pensar que el total cambia", "confundir filas y columnas"],
        "Reconoce el arreglo y pregunta cuántas tapas hay; si hay error, que cuente fila por fila.",
    ),
    reinforce="Dibuja un arreglo de 2 × 7 y otro de 7 × 2 y comprueba que tienen los mismos puntos.",
    extend="¿Cuántos puntos tiene un arreglo de 10 filas y 10 columnas? ¿Cómo lo supiste?",
)

register(
    OA8, 3,
    materials="Lápiz, cuaderno y una tabla de números hasta 100 si la tienes. Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé a construir las tablas del 2, del 5 y del 10 contando de a saltos. Sirve para multiplicar rápido sin hacer cuentas largas.",
    prior=["Sé contar de 2 en 2, de 5 en 5 y de 10 en 10.", "Sé que una multiplicación es una suma repetida."],
    explain=[
        "La tabla del 2 se construye sumando 2 cada vez: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. Cada número es el resultado de 2 × 1, 2 × 2, hasta 2 × 10. Los resultados son los números pares.",
        "La tabla del 5 va de 5 en 5: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50. Todos terminan en 0 o en 5. La tabla del 10 va de 10 en 10: 10, 20, 30, hasta 100, y todos terminan en 0.",
        "Las tablas se relacionan: 5 × 6 = 30 y 10 × 6 = 60, el doble. Para recordar, cuenta de a saltos con los dedos o con una recta. Con el tiempo, aprenderás los resultados de memoria sin contar.",
    ],
    vocab=[("tabla de multiplicar", "lista de los productos de un número por 1, 2, 3 hasta 10"), ("producto", "resultado de una multiplicación"), ("factor", "cada número que se multiplica"), ("par", "número que termina en 0, 2, 4, 6 u 8"), ("saltos", "pasos de igual tamaño al contar")],
    worked=[
        {"title": "Construir la tabla del 5", "problem": "Escribe 5 × 1 hasta 5 × 5.", "steps": ["Cuento de 5 en 5.", "5 × 1 = 5, 5 × 2 = 10, 5 × 3 = 15.", "5 × 4 = 20 y 5 × 5 = 25."], "answer": "5, 10, 15, 20, 25"},
        {"title": "Usar la tabla", "problem": "Hay 6 bolsas con 5 manzanas cada una. ¿Cuántas manzanas hay?", "steps": ["Son 6 grupos de 5: 5 × 6.", "Cuento de 5 en 5 seis veces: 5, 10, 15, 20, 25, 30."], "answer": "30 manzanas"},
    ],
    mistakes=[
        {"wrong": "Decir que 5 × 8 = 35.", "why": "Se perdió un salto al contar de 5 en 5.", "fix": "Cuenta de nuevo: 5, 10, 15, 20, 25, 30, 35, 40; el 8.º salto es 40."},
        {"wrong": "Decir que 10 × 7 = 17.", "why": "Se suma 10 + 7 en vez de repetir 10 siete veces.", "fix": "Cuenta de 10 en 10: 70."},
    ],
    tiers={
        "recovery": [
            ex("Completa la tabla del 5: 5, 10, __, 20, __.", "15 y 25", "Se suma 5 cada vez."),
            ex("Completa la tabla del 2: 2, 4, __, 8, __.", "6 y 10", "Se suma 2 cada vez."),
            arith("¿Cuánto es 10 × 6?", "10*6", "Seis saltos de 10."),
        ],
        "understand": [
            ex("¿Con qué cifra terminan todos los resultados de la tabla del 10?", "Con 0", "Se cuenta de 10 en 10."),
            ex("Los resultados de la tabla del 5 terminan en ¿qué cifras?", "En 0 o en 5", "5, 10, 15, 20, ..."),
            ex("¿Está el 14 en la tabla del 2?", "Sí, 2 × 7", "Se llega a 14 contando de 2 en 2."),
        ],
        "apply": [
            arith("Un paquete trae 5 galletas. ¿Cuántas galletas hay en 9 paquetes?", "5*9", "Nueve saltos de 5."),
            arith("Hay 8 pares de guantes. Cada par tiene 2 guantes. ¿Cuántos guantes hay?", "2*8", "Ocho saltos de 2."),
            arith("Cada caja tiene 10 lápices y hay 7 cajas. ¿Cuántos lápices hay?", "10*7", "Siete saltos de 10."),
        ],
        "reason": [
            ex("Pía dice que 5 × 8 = 35. Cuenta de 5 en 5 ocho veces y corrige.", "40", "5, 10, 15, 20, 25, 30, 35, 40."),
            ex("¿Es 30 (5 × 6) la mitad de 60 (10 × 6)?", "Sí", "5 es la mitad de 10, entonces el producto también."),
        ],
        "challenge": [
            ex("Si 5 × 4 = 20, ¿cuánto es 10 × 4?", "40", "10 es el doble de 5, entonces el resultado es el doble."),
            ex("En la tabla del 5, ¿qué número impar está entre 40 y 50?", "45", "5 × 9 = 45."),
        ],
    },
    context=[arith("En una feria cada puesto tiene 5 mesas y hay 6 puestos. ¿Cuántas mesas hay?", "5*6", "Seis saltos de 5.")],
    selfcheck=[
        arith("¿Cuánto es 2 × 8?", "2*8", "Ocho saltos de 2."),
        arith("¿Cuánto es 5 × 7?", "5*7", "Siete saltos de 5."),
        arith("¿Cuánto es 10 × 9?", "10*9", "Nueve saltos de 10."),
    ],
    open_task=task(
        "Escribe en una tabla las multiplicaciones del 2, del 5 y del 10, de ×1 a ×10. Subraya los resultados que aparecen en las tres tablas y escribe qué notas.",
        "Tabla del 2: 2, 4, ..., 20. Tabla del 5: 5, 10, ..., 50. Tabla del 10: 10, 20, ..., 100. En las tres aparecen 10 y 20. Noto que los de la tabla del 10 terminan en 0 y los del 5 en 0 o 5.",
        ["escribe las tres tablas", "los resultados son correctos", "subraya los comunes", "escribe lo que nota"],
        ["tablas escritas en el cuaderno", "resultados subrayados"],
        ["perder un salto", "mezclar los resultados"],
        "Reconoce las tablas completas y pregunta qué patrón ve; si hay error, que cuente de a saltos en la recta.",
    ),
    reinforce="Recita la tabla del 2 y la del 10 hacia adelante y hacia atrás.",
    extend="Compara la tabla del 5 con la del 10: ¿cómo se relacionan sus resultados?",
)

register(
    OA8, 4,
    materials="Lápiz y cuaderno. Todos los datos están escritos en cada ejercicio. Puedes dibujar arreglos para ver las partes.",
    use="Aprenderé a calcular tablas difíciles dividiendo un número en dos partes fáciles. Sirve para encontrar 7 × 6 si solo sé la tabla del 5 y la del 2.",
    prior=["Sé las tablas del 2, 5 y 10.", "Sé que 3 × 5 = 5 × 3."],
    explain=[
        "Para calcular una tabla difícil puedes partir uno de los factores. En 7 × 6, parte el 7 en 5 + 2. Entonces 7 × 6 = 5 × 6 + 2 × 6. Cada parte es una tabla que ya sabes: 5 × 6 = 30 y 2 × 6 = 12.",
        "Luego sumas: 30 + 12 = 42. Esto se llama distributividad: el 6 se reparte entre los dos sumandos del 7. En un arreglo de 7 filas de 6 puntos, separas 5 filas arriba y 2 abajo, y cuentas cada parte.",
        "Puedes partir de varias maneras: 9 × 4 = 5 × 4 + 4 × 4 = 20 + 16 = 36. Elige la que use tablas que sabes. Cuidado: hay que multiplicar las dos partes. No basta con 5 × 6 + 2, porque faltaría multiplicar el 2 por 6.",
    ],
    vocab=[("distributividad", "multiplicar cada parte de un número y luego sumar"), ("descomponer", "partir un número en dos o más sumandos"), ("producto parcial", "resultado de una de las partes"), ("factor", "cada número que se multiplica"), ("tabla fácil", "tabla que ya sé de memoria")],
    worked=[
        {"title": "Partir el 7", "problem": "Calcula 7 × 6 usando las tablas del 5 y del 2.", "steps": ["Parto 7 = 5 + 2.", "5 × 6 = 30 y 2 × 6 = 12.", "Sumo: 30 + 12 = 42."], "answer": "42"},
        {"title": "Partir el 9", "problem": "Calcula 9 × 4 usando 5 × 4 y 4 × 4.", "steps": ["Parto 9 = 5 + 4.", "5 × 4 = 20 y 4 × 4 = 16.", "Sumo: 20 + 16 = 36."], "answer": "36"},
    ],
    mistakes=[
        {"wrong": "Calcular 7 × 6 como 5 × 6 + 2 = 32.", "why": "Solo se multiplicó una parte del 7.", "fix": "Multiplica las dos partes: 5 × 6 + 2 × 6 = 30 + 12 = 42."},
        {"wrong": "Partir 7 como 5 + 3.", "why": "5 + 3 es 8, no 7.", "fix": "Las dos partes deben sumar el número que partes: 5 + 2 = 7."},
    ],
    tiers={
        "recovery": [
            ex("Completa: 7 × 6 = 5 × 6 + 2 × 6 = __ + __.", "30 + 12", "5 × 6 = 30 y 2 × 6 = 12."),
            ex("Completa: 6 × 4 = 5 × 4 + 1 × 4 = 20 + __.", "4", "1 × 4 = 4, entonces 6 × 4 = 24."),
            ex("Parte 8 como 5 + 3 para calcular 8 × 3: 5 × 3 + 3 × 3.", "24", "15 + 9 = 24."),
        ],
        "understand": [
            ex("¿Es correcto decir que 9 × 4 = 5 × 4 + 4 × 4?", "Sí; ambos son 36", "5 + 4 = 9, y 20 + 16 = 36."),
            ex("En 7 × 6 = 5 × 6 + 2 × 6, ¿por qué conviene partir el 7 en 5 + 2?", "Porque son tablas fáciles", "La del 5 y la del 2 ya se saben."),
            ex("¿Cuál partición del 8 es correcta: 5 + 3 o 5 + 4?", "5 + 3", "Las partes deben sumar 8."),
        ],
        "apply": [
            arith("Calcula 6 × 9 usando 5 × 9 y 1 × 9.", "6*9", "45 + 9 = 54."),
            arith("Calcula 8 × 8 usando 5 × 8 y 3 × 8.", "8*8", "40 + 24 = 64."),
            arith("Calcula 8 × 7 usando 5 × 7 y 3 × 7.", "8*7", "35 + 21 = 56."),
        ],
        "reason": [
            ex("Luis calculó 7 × 6 como 5 × 6 + 2 = 32. ¿Qué error cometió y cuál es el resultado?", "No multiplicó el 2 por 6; es 42", "2 × 6 = 12 y 30 + 12 = 42."),
            ex("Ana calcula 6 × 8 = 5 × 8 + 1 × 8 y Bea 6 × 8 = 3 × 8 + 3 × 8. ¿Ambas están bien?", "Sí, 48", "40 + 8 = 48 y 24 + 24 = 48."),
        ],
        "challenge": [
            ex("Calcula 9 × 8 partiendo el 9 en 5 + 4.", "72", "5 × 8 = 40 y 4 × 8 = 32; 40 + 32 = 72."),
            arith("Calcula 7 × 7 usando 5 × 7 y 2 × 7.", "7*7", "35 + 14 = 49."),
        ],
    },
    context=[arith("Una bandeja tiene 6 huevos y se llenan 8 bandejas. ¿Cuántos huevos hay?", "8*6", "8 × 6 = 5 × 6 + 3 × 6 = 30 + 18.")],
    selfcheck=[
        ex("Parte el 6 en 5 + 1 y calcula 6 × 3.", "18", "15 + 3 = 18."),
        ex("En 7 × 4 = 5 × 4 + 2 × 4, ¿cuánto es cada parte?", "20 y 8", "5 × 4 = 20 y 2 × 4 = 8."),
        ex("¿Cuánto es 8 × 4?", "32", "5 × 4 + 3 × 4 = 20 + 12."),
    ],
    open_task=task(
        "Calcula 6 × 7, 8 × 6 y 9 × 5 partiendo uno de los factores en dos partes fáciles. Para cada una escribe la partición, los dos productos parciales y la suma. Comprueba con un arreglo dibujado.",
        "6 × 7: 5 × 7 + 1 × 7 = 35 + 7 = 42. 8 × 6: 5 × 6 + 3 × 6 = 30 + 18 = 48. 9 × 5: 5 × 5 + 4 × 5 = 25 + 20 = 45.",
        ["parte un factor en dos sumandos", "calcula los dos productos parciales", "suma bien", "comprueba con un arreglo"],
        ["particiones escritas", "arreglo dibujado"],
        ["multiplicar solo una parte", "partir mal"],
        "Reconoce la partición y pregunta por qué eligió esas tablas; si hay error, que dibuje el arreglo y lo cuente.",
    ),
    reinforce="Con 7 filas de 4 puntos, separa 5 filas y 2 filas y cuenta cada parte. Escribe la suma.",
    extend="Calcula 9 × 6 de dos maneras distintas y comprueba que dan lo mismo.",
)

register(
    OA8, 5,
    materials="Lápiz y cuaderno. Todos los datos de los problemas están escritos. Puedes dibujar arreglos o grupos.",
    use="Aprenderé a resolver y a inventar problemas que se resuelven con tablas de multiplicar. Sirve para calcular totales en la vida diaria.",
    prior=["Sé las tablas del 2, 5 y 10 y las estrategias para las otras.", "Sé distinguir cuándo hay grupos iguales."],
    explain=[
        "Un problema multiplicativo habla de grupos iguales: bolsas con la misma cantidad, filas con los mismos asientos, cajas con los mismos lápices. Para resolverlo, busca cuántos grupos hay y cuántos hay en cada grupo. Luego multiplica.",
        "Por ejemplo: «Hay 6 macetas con 5 flores cada una. ¿Cuántas flores hay?» Son 6 grupos de 5. 6 × 5 = 30. Si el problema tiene más pasos, resuelve en orden: «4 bolsas con 6 dulces y se cayeron 5» es 4 × 6 = 24 y luego 24 − 5 = 19.",
        "Para inventar un problema, elige una multiplicación y una historia con grupos iguales. Con 7 × 4 puedes decir: «Hay 7 bolsas con 4 manzanas cada una. ¿Cuántas manzanas hay?». Un buen problema tiene todos los datos y una pregunta clara.",
    ],
    vocab=[("problema multiplicativo", "problema que se resuelve con grupos iguales"), ("dato", "número o información que da el problema"), ("pregunta", "lo que se quiere saber"), ("total", "cantidad que resulta de juntar todos los grupos"), ("grupos iguales", "grupos con la misma cantidad")],
    worked=[
        {"title": "Un paso", "problem": "En un jardín hay 6 macetas con 5 flores cada una. ¿Cuántas flores hay?", "steps": ["Son 6 grupos de 5.", "6 × 5 = 30."], "answer": "30 flores"},
        {"title": "Dos pasos", "problem": "Hay 4 bolsas con 6 dulces cada una. Se cayeron 5 dulces. ¿Cuántos quedan?", "steps": ["Dulces en total: 4 × 6 = 24.", "Se cayeron 5: 24 − 5 = 19."], "answer": "19 dulces"},
    ],
    mistakes=[
        {"wrong": "Resolver «3 mesas con 6 sillas» con 3 + 6 = 9.", "why": "No se ve que hay grupos iguales.", "fix": "Son 3 grupos de 6: 3 × 6 = 18."},
        {"wrong": "Responder 24 en el problema de los dulces que se cayeron.", "why": "Se olvidó el segundo paso.", "fix": "Resta los que se cayeron: 24 − 5 = 19."},
    ],
    tiers={
        "recovery": [
            arith("Una caja tiene 5 chocolates y se compran 8 cajas. ¿Cuántos chocolates hay?", "8*5", "Son 8 grupos de 5."),
            arith("Un álbum tiene 8 páginas con 4 stickers cada una. ¿Cuántos stickers hay?", "8*4", "Son 8 grupos de 4."),
            arith("Cada niño recibe 3 lápices y hay 9 niños. ¿Cuántos lápices se reparten?", "9*3", "Son 9 grupos de 3."),
        ],
        "understand": [
            ex("¿Qué multiplicación resuelve «Hay 7 bolsas con 4 manzanas cada una»?", "7 × 4", "7 grupos de 4."),
            ex("«Hay 5 cajas.» ¿Falta algún dato para saber cuántos lápices hay en total?", "Sí, cuántos lápices tiene cada caja", "Sin ese dato no se pueden calcular los grupos."),
            ex("«Hay 6 mesas con 4 sillas cada una.» Escribe una pregunta que se resuelva con 6 × 4.", "¿Cuántas sillas hay en total?", "Pregunta por el total de los grupos."),
        ],
        "apply": [
            arith("Una pastelería hace 7 bandejas con 8 pasteles cada una. ¿Cuántos pasteles hace?", "7*8", "Son 7 grupos de 8."),
            arith("En un taller hay 9 cursos con 10 estudiantes cada uno. ¿Cuántos estudiantes hay?", "9*10", "Son 9 grupos de 10."),
            arith("Cada bicicleta tiene 2 ruedas y hay 9 bicicletas. ¿Cuántas ruedas hay?", "9*2", "Son 9 grupos de 2."),
        ],
        "reason": [
            ex("Hay 5 bolsas con 4 naranjas cada una y se comieron 6 naranjas. ¿Qué operaciones se hacen y cuántas naranjas quedan?", "5 × 4 = 20 y 20 − 6 = 14", "Primero el total, luego las que se comieron."),
            ex("Ana resolvió «3 mesas con 6 sillas» con 3 + 6 = 9. ¿Qué error cometió y cuál es el resultado?", "Sumó en vez de multiplicar; es 18", "3 × 6 = 18."),
        ],
        "challenge": [
            arith("Compré 4 paquetes de 5 lápices y 3 paquetes de 10 lápices. ¿Cuántos lápices compré?", "4*5+3*10", "20 + 30."),
            arith("Un tren tiene 3 vagones y cada vagón tiene 2 filas de 5 asientos. ¿Cuántos asientos hay en el tren?", "3*2*5", "Primero 2 × 5 = 10 asientos por vagón, luego 3 × 10 = 30."),
        ],
    },
    context=[arith("Una profesora arma 6 grupos de 5 estudiantes. ¿Cuántos estudiantes participan?", "6*5", "Seis grupos de 5.")],
    selfcheck=[
        arith("3 cajas con 10 lápices cada una: ¿cuántos lápices?", "3*10", "Tres grupos de 10."),
        ex("¿Qué multiplicación resuelve «5 filas de 6 sillas»?", "5 × 6", "5 grupos de 6."),
        arith("Una caja trae 2 galletas y hay 8 cajas. ¿Cuántas galletas?", "8*2", "Ocho grupos de 2."),
    ],
    open_task=task(
        "Inventa un problema para cada multiplicación: 6 × 4 y 8 × 5. Escribe los datos, la pregunta y la respuesta. Después resuelve este: «Hay 7 bolsas con 6 caramelos y se comieron 8. ¿Cuántos quedan?».",
        "6 × 4: «Hay 6 cajas con 4 lápices cada una. ¿Cuántos lápices hay?» 24. 8 × 5: «Hay 8 mesas con 5 sillas. ¿Cuántas sillas?» 40. El problema: 7 × 6 = 42 y 42 − 8 = 34 caramelos.",
        ["inventa dos problemas coherentes", "incluye datos y pregunta", "da las respuestas 24 y 40", "resuelve el problema con 34"],
        ["problemas escritos", "cálculos"],
        ["problemas sin pregunta", "olvidar el segundo paso"],
        "Reconoce los problemas inventados y pregunta si los datos alcanzan; si hay error, que dibuje los grupos.",
    ),
    reinforce="Escribe una historia con 3 grupos de 5 objetos y otra con 5 grupos de 3 objetos.",
    extend="Inventa un problema de dos pasos que use una multiplicación y una resta, y resuélvelo.",
)
