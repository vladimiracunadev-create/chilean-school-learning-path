"""Cuaderno del estudiante de 6.º básico Matemática: OA 09 (relaciones en tablas) y OA 10 (generalizaciones con expresiones algebraicas)."""
from __future__ import annotations

from student_lessons import ex
from student_content_ma06_a import M, W, lesson, task

OA9 = "MA06 OA 09"

# ------------------------------------------------------------------ OA 09 clase 1
lesson(
    OA9, 1,
    use="Aprenderé a descubrir patrones en tablas de valores. Sirve para predecir qué viene después sin tener que contar todo desde el principio.",
    prior=["Sé las tablas de multiplicar.", "Sé continuar patrones numéricos sencillos."],
    explain=[
        "Una tabla de valores ordena dos conjuntos de números que se relacionan. En una fila va la posición o la entrada, que llamaremos n, y en la otra el valor que le corresponde. Por ejemplo: n = 1, 2, 3, 4 y valor = 5, 8, 11, 14. Cada columna dice «cuando n es 1 el valor es 5, cuando n es 2 el valor es 8».",
        "Para descubrir el patrón, fíjate en cuánto cambia el valor cuando n aumenta de 1 en 1. En el ejemplo sube 3 cada vez (5, 8, 11, 14): es un patrón aditivo, se suma siempre lo mismo. En otras tablas, el valor se obtiene multiplicando n por un número, como 12, 24, 36, 48, que son los múltiplos de 12.",
        "Cuando conoces el patrón, puedes completar la tabla hacia adelante. Si el valor sube 3 cada vez y para n = 4 es 14, entonces para n = 5 es 14 + 3 = 17. Siempre comprueba el patrón en todas las columnas y no solo en las dos primeras.",
    ],
    vocab=[("tabla de valores", "cuadro que relaciona cada n con un valor"), ("patrón", "regularidad que se repite"), ("valor", "número que le corresponde a cada n"), ("aditivo", "que cambia sumando siempre lo mismo"), ("múltiplo", "resultado de multiplicar un número por 1, 2, 3…")],
    worked=[
        W("Patrón que suma", "En una tabla, n = 1, 2, 3, 4 y valor = 5, 8, 11, 14. ¿Cuál es el valor cuando n = 5?", ["El valor sube 3 cada vez: 8 − 5 = 3, 11 − 8 = 3, 14 − 11 = 3.", "Para n = 5 sumo 3 a 14."], "17"),
        W("Patrón que multiplica", "En una tabla, n = 1, 2, 3, 4 y valor = 12, 24, 36, 48. ¿Cuál es el valor cuando n = 5?", ["Los valores son los múltiplos de 12: 12 × 1, 12 × 2, 12 × 3 y 12 × 4.", "Para n = 5 el valor es 12 × 5."], "60"),
    ],
    mistakes=[
        M("Decir que 5, 8, 11, 14 sube de 5 en 5 por mirar solo el primer número.", "No se calculó cuánto aumenta cada valor.", "Resta valores consecutivos: 8 − 5 = 3, entonces sube de 3 en 3."),
        M("Revisar el patrón solo en las dos primeras columnas.", "Dos columnas pueden cumplir varios patrones.", "Comprueba el patrón en toda la tabla."),
    ],
    rec=[
        ex("En una tabla, n = 1, 2, 3 y el valor es 3, 6, 9. ¿Cuánto sube el valor cada vez que n sube 1?", "3", "6 − 3 = 3 y 9 − 6 = 3."),
        ex("Sigue el patrón 2, 4, 6, 8. ¿Qué número viene después?", "10", "Sube de 2 en 2."),
        ex("En una tabla, n = 1, 2, 3 y el valor es 10, 20, 30. ¿Cuánto vale cuando n = 4?", "40", "Sigue la tabla del 10."),
    ],
    und=[
        ex("n = 1, 2, 3, 4 y valor = 7, 9, 11, 13. ¿Cuánto vale cuando n = 5?", "15", "Sube de 2 en 2: 13 + 2."),
        ex("n = 1, 2, 3, 4 y valor = 6, 12, 18, 24. ¿Cuánto vale cuando n = 6?", "36", "Es la tabla del 6: 6 × 6."),
        ex("n = 1, 2, 3, 4 y valor = 10, 15, 20, 25. ¿Cuánto vale cuando n = 7?", "40", "Sube de 5 en 5 desde 10: 10 + 6 × 5 = 40."),
    ],
    app=[
        ex("Cada carpa de un campamento aloja a 4 personas: 1 carpa, 4 personas; 2 carpas, 8 personas; 3 carpas, 12 personas. ¿Cuántas personas se alojan en 7 carpas?", "28", "Es la tabla del 4: 4 × 7."),
        ex("Una niña ahorra: en la semana 1 tiene $2.000, en la 2 tiene $3.500 y en la 3 tiene $5.000. Si sigue igual, ¿cuánto tiene en la semana 5?", "$8.000", "Sube $1.500 cada semana: 5.000 + 1.500 + 1.500."),
        ex("Con palitos se arma una fila de triángulos: 1 triángulo usa 3 palitos, 2 triángulos usan 5 palitos y 3 triángulos usan 7. ¿Cuántos palitos usan 6 triángulos?", "13", "Sube de 2 en 2: 3, 5, 7, 9, 11, 13."),
    ],
    rea=[
        ex("En la tabla n = 1, 2, 3, 4 y valor = 4, 6, 8, 10, Lía dice que cada valor es n × 4. ¿Cuánto vale realmente cuando n = 5?", "12", "El valor sube de 2 en 2 y 10 + 2 = 12; con n × 4 la tabla no coincide."),
        ex("Una tabla dice que n = 1 vale 3, n = 2 vale 6 y n = 4 vale 12. ¿Cuánto vale n = 3?", "9", "Es la tabla del 3."),
    ],
    cha=[
        ex("n = 1, 2, 3, 4 y valor = 2, 5, 8, 11. ¿Cuánto vale cuando n = 10?", "29", "Sube de 3 en 3: 2 + 9 × 3 = 29."),
        ex("n = 1, 2, 3 y valor = 5, 10, 15. ¿Para qué n el valor es 50?", "10", "El valor es 5 × n y 5 × 10 = 50."),
    ],
    ctx=[ex("Un taxi ficticio cobra por 1 km $1.500, por 2 km $2.000 y por 3 km $2.500. Si sigue igual, ¿cuánto cobra por 6 km?", "$4.000", "Sube $500 por km: 2.500 + 500 + 500 + 500.")],
    sc=[
        ex("n = 1, 2, 3 y valor = 9, 18, 27. ¿Cuánto vale cuando n = 5?", "45", "Es la tabla del 9."),
        ex("n = 1, 2, 3 y valor = 1, 4, 7. ¿Cuánto sube el valor cada vez?", "3", "4 − 1 = 3 y 7 − 4 = 3."),
        ex("Tabla A: valores 5, 10, 15. Tabla B: valores 5, 6, 7. ¿Cuál sube de 5 en 5?", "La tabla A", "5, 10, 15 aumenta 5 cada vez."),
    ],
    op=task(
        "Mira esta tabla de un patrón con baldosas: figura 1 usa 6 baldosas, figura 2 usa 10, figura 3 usa 14 y figura 4 usa 18. Escribe cuánto sube cada vez, completa la tabla hasta la figura 7 y explica cómo lo hiciste.",
        "Sube 4 cada vez. Figura 5: 22, figura 6: 26, figura 7: 30. Sumé 4 al valor anterior.",
        ["identifica cuánto sube", "completa la tabla hasta la figura 7", "explica el patrón"],
        ["tabla completada", "frase de explicación"],
        ["mirar solo dos columnas", "equivocarse al sumar"],
        "Pide que compruebe que cada paso suma lo mismo.",
    ),
    reinforce="Completa hasta n = 8: n = 1, 2, 3, 4 y valor = 3, 7, 11, 15. Escribe cuánto sube.",
    extend="Inventa una tabla con 5 valores que suba de 6 en 6 y otra que sea la tabla del 6. Explica en qué se diferencian.",
)

# ------------------------------------------------------------------ OA 09 clase 2
lesson(
    OA9, 2,
    use="Aprenderé a describir con palabras la regla que relaciona los valores de una tabla. Sirve para explicar un patrón a otra persona y para calcular cualquier valor.",
    prior=["Sé descubrir cuánto sube un patrón.", "Sé multiplicar y sumar números naturales."],
    explain=[
        "Una regla dice qué hay que hacer con n para obtener el valor. Puede ser «suma 5 a n», «multiplica n por 4» o «multiplica n por 3 y suma 1». Con la regla puedes calcular el valor de cualquier n, aunque sea muy grande.",
        "Para encontrarla, mira primero cuánto sube el valor cuando n sube 1. Ese número es por el que se multiplica n. Después compara con n = 1 y ajusta. En n = 1, 2, 3, 4 y valor = 4, 7, 10, 13 el valor sube 3, así que se multiplica por 3: 3, 6, 9, 12. Faltan 1 en cada uno: la regla es «multiplica por 3 y suma 1».",
        "Si el valor sube 1 cada vez, la regla es solo sumar un número a n, como n + 5. Si el primer valor es igual al que sube cada vez, la regla es solo multiplicar. Siempre comprueba la regla con todas las columnas de la tabla antes de decidir.",
    ],
    vocab=[("regla", "instrucción que dice cómo obtener el valor a partir de n"), ("entrada", "número n con que se empieza"), ("salida", "valor que se obtiene al aplicar la regla"), ("comprobar", "revisar que la regla funciona en toda la tabla"), ("ajustar", "sumar o restar lo que falta después de multiplicar")],
    worked=[
        W("Regla que multiplica y suma", "En una tabla, n = 1, 2, 3, 4 y valor = 4, 7, 10, 13. ¿Cuál es la regla?", ["El valor sube 3 cada vez: multiplico n por 3 (3, 6, 9, 12).", "Falta 1 en cada valor (4 − 3 = 1), entonces sumo 1.", "Comprobación: n = 4 da 3 × 4 + 1 = 13."], "Multiplica n por 3 y suma 1"),
        W("Regla que solo suma", "En una tabla, n = 1, 2, 3 y valor = 6, 7, 8. ¿Cuál es la regla?", ["El valor sube 1 cada vez: no hay que multiplicar.", "6 − 1 = 5, entonces se suma 5."], "Suma 5 a n"),
    ],
    mistakes=[
        M("Decir que la regla de 5, 8, 11 es «suma 3 a n».", "Sumar 3 a n = 1 da 4 y no 5.", "La regla es «multiplica n por 3 y suma 2»."),
        M("Elegir una regla mirando solo la primera columna.", "Varias reglas funcionan con n = 1 y no con las otras.", "Comprueba con otra columna, por ejemplo n = 3."),
    ],
    rec=[
        ex("La regla es «suma 5 a n». ¿Cuánto vale cuando n = 3?", "8", "3 + 5 = 8."),
        ex("La regla es «multiplica n por 4». ¿Cuánto vale cuando n = 6?", "24", "4 × 6 = 24."),
        ex("En una tabla, n = 1, 2, 3 y valor = 2, 3, 4. ¿Cuánto se suma a n?", "1", "2 − 1 = 1 y 3 − 2 = 1."),
    ],
    und=[
        ex("n = 1, 2, 3 y valor = 5, 8, 11. Escribe la regla.", "Multiplica n por 3 y suma 2", "El valor sube 3 y 3 × 1 + 2 = 5."),
        ex("La regla es «el doble de n más 1». ¿Cuánto vale cuando n = 7?", "15", "2 × 7 + 1 = 15."),
        ex("La regla es «n por 5 menos 2». ¿Cuánto vale cuando n = 4?", "18", "5 × 4 − 2 = 18."),
    ],
    app=[
        ex("Una entrada al cine cuesta $3.000: 1 entrada, $3.000; 2 entradas, $6.000; 3 entradas, $9.000. ¿Cuánto cuestan 10 entradas?", "$30.000", "La regla es multiplicar n por 3.000."),
        ex("Se pegan mesas cuadradas en fila: 1 mesa tiene 4 sillas, 2 mesas tienen 6 y 3 mesas tienen 8. La regla es «el doble de n más 2». ¿Cuántas sillas hay con 10 mesas?", "22", "2 × 10 + 2 = 22."),
        ex("n = 1, 2, 3 y valor = 7, 12, 17. Usa la regla «multiplica por 5 y suma 2». ¿Cuánto vale cuando n = 8?", "42", "5 × 8 + 2 = 42."),
    ],
    rea=[
        ex("En la tabla n = 1, 2, 3 y valor = 5, 7, 9, Beto dice que la regla es «suma 4 a n». ¿Cuál de las dos reglas es correcta: «n + 4» o «el doble de n más 3»?", "El doble de n más 3", "Con n = 2: n + 4 da 6 y no 7; 2 × 2 + 3 da 7."),
        ex("Las reglas «n + 3» y «2n + 2» dan el mismo valor para n = 1. ¿Dan el mismo valor para n = 2? Responde sí o no.", "No", "Con n = 2 dan 5 y 6."),
    ],
    cha=[
        ex("La regla es «el triple de n menos 1». ¿Para qué n el valor es 20?", "7", "3 × 7 − 1 = 20."),
        ex("n = 2, 3, 4 y valor = 7, 10, 13. Con la regla «multiplica por 3 y suma 1», ¿cuánto vale cuando n = 1?", "4", "3 × 1 + 1 = 4."),
    ],
    ctx=[ex("Una imprenta ficticia cobra por 1 hoja $700, por 2 hojas $900 y por 3 hojas $1.100. La regla es «multiplica n por 200 y suma 500». ¿Cuánto cobra por 10 hojas?", "$2.500", "200 × 10 + 500 = 2.500.")],
    sc=[
        ex("La regla es «n por 6». ¿Cuánto vale cuando n = 5?", "30", "6 × 5 = 30."),
        ex("n = 3, 4, 5 y valor = 8, 9, 10. ¿Cuánto vale cuando n = 8 con esa regla?", "13", "La regla es n + 5: 8 + 5 = 13."),
        ex("La regla es «multiplica por 2 y resta 1». ¿Cuánto vale cuando n = 6?", "11", "2 × 6 − 1 = 11."),
    ],
    op=task(
        "Con estas dos tablas, escribe la regla de cada una con palabras y comprueba en todas las columnas: Tabla A: n = 1, 2, 3, 4 y valor = 3, 5, 7, 9. Tabla B: n = 1, 2, 3, 4 y valor = 8, 16, 24, 32. Luego usa cada regla para calcular el valor de n = 10.",
        "Tabla A: multiplica n por 2 y suma 1; n = 10 da 21. Tabla B: multiplica n por 8; n = 10 da 80.",
        ["encuentra cuánto sube el valor", "escribe la regla con palabras", "comprueba y calcula n = 10"],
        ["dos reglas", "comprobación y dos valores"],
        ["olvidar el ajuste", "no comprobar todas las columnas"],
        "Pide que verifique la regla con la última columna de cada tabla.",
    ),
    reinforce="Escribe la regla de n = 1, 2, 3 y valor = 4, 8, 12. Usa la regla para calcular n = 9.",
    extend="Inventa una regla de la forma «multiplica por … y suma …», construye su tabla hasta n = 5 y pide a otra persona que la descubra.",
)

# ------------------------------------------------------------------ OA 09 clase 3
lesson(
    OA9, 3,
    use="Aprenderé a escribir la regla de una tabla con lenguaje matemático, usando una letra. Sirve para escribir en poco espacio algo que se puede aplicar siempre.",
    prior=["Sé describir una regla con palabras.", "Sé qué significa que una letra represente un número."],
    explain=[
        "En lenguaje matemático, la entrada se representa con una letra, por ejemplo n, y el valor con otra, por ejemplo V. «Multiplica n por 3 y suma 1» se escribe V = 3n + 1. Cuando un número y una letra están juntos, como 3n, significa 3 por n.",
        "Para usar la regla, reemplazas n por un número y calculas. Si V = 3n + 1 y n = 4, entonces V = 3 × 4 + 1 = 13. Primero se multiplica y después se suma. Para escribir una regla desde una tabla, busca cuánto sube el valor (ese número va antes de la n) y luego cuánto falta para llegar al primer valor.",
        "Una regla escrita así sirve para cualquier n. Con ella puedes completar tablas largas sin repetir el patrón. Para comprobar, calcula uno o dos valores de la tabla con la regla. Si coinciden con la tabla, es probable que la regla esté bien.",
    ],
    vocab=[("variable", "letra que puede representar muchos números"), ("regla simbólica", "regla escrita con letras y números"), ("reemplazar", "poner un número en el lugar de la letra"), ("3n", "se lee «tres por n»"), ("V", "letra que usamos aquí para el valor")],
    worked=[
        W("Usar una regla simbólica", "Si V = 3n + 1, ¿cuánto vale V cuando n = 4?", ["Reemplazo n por 4: V = 3 × 4 + 1.", "Primero multiplico: 12. Luego sumo 1."], "13"),
        W("Escribir la regla de una tabla", "En una tabla, n = 1, 2, 3 y V = 2, 4, 6. Escribe la regla.", ["V sube 2 cada vez y 2 × 1 = 2, no falta nada.", "La regla es multiplicar n por 2."], "V = 2n"),
    ],
    mistakes=[
        M("Leer 3n como «30 + n» o «3 + n».", "Se confunde el número pegado a la letra con una suma.", "3n es 3 por n. Con n = 5 vale 15."),
        M("Calcular V = 3n + 1 con n = 4 como 3 × (4 + 1).", "Se sumó antes de multiplicar.", "Primero se multiplica 3 × 4 = 12 y luego se suma 1."),
    ],
    rec=[
        ex("Si V = n + 7, ¿cuánto vale V cuando n = 3?", "10", "3 + 7 = 10."),
        ex("Si V = 5n, ¿cuánto vale V cuando n = 4?", "20", "5 × 4 = 20."),
        ex("Si V = 2n + 1, ¿cuánto vale V cuando n = 1?", "3", "2 × 1 + 1 = 3."),
    ],
    und=[
        ex("Escribe con letras la regla «el triple de n menos 2».", "V = 3n − 2", "El triple de n es 3n y luego se resta 2."),
        ex("Si V = 4n − 3, ¿cuánto vale V cuando n = 5?", "17", "4 × 5 = 20 y 20 − 3 = 17."),
        ex("En una tabla, n = 1, 2, 3 y V = 3, 5, 7. Escribe la regla.", "V = 2n + 1", "V sube 2 y 2 × 1 + 1 = 3."),
    ],
    app=[
        ex("Si V = 6n + 4, ¿cuánto vale V cuando n = 10?", "64", "6 × 10 + 4 = 64."),
        ex("Con palitos se arman cuadrados en fila. n = 1, 2, 3 y V = 4, 7, 10. Con la regla V = 3n + 1, ¿cuántos palitos se necesitan para 8 cuadrados?", "25", "3 × 8 + 1 = 25."),
        ex("Un cuaderno cuesta $1.500. Si V = 1.500 × n es lo que se paga por n cuadernos, ¿cuánto se paga por 12 cuadernos?", "$18.000", "1.500 × 12 = 18.000."),
    ],
    rea=[
        ex("Ana escribió V = n + 3 para la tabla n = 1, 2, 3 y V = 5, 7, 9. ¿Cuál es la regla correcta?", "V = 2n + 3", "V sube 2 y 2 × 1 + 3 = 5."),
        ex("Las reglas V = 2n y V = n + 2 dan el mismo valor para n = 2. ¿Son la misma regla? Responde sí o no.", "No", "Con n = 3 dan 6 y 5."),
    ],
    cha=[
        ex("Si V = 3n + 2 y V vale 29, ¿cuánto vale n?", "9", "3 × 9 + 2 = 29."),
        ex("¿Cuál regla es equivalente a V = n + n + n?", "V = 3n", "Sumar tres veces n es multiplicar n por 3."),
    ],
    ctx=[ex("Un club ficticio cobra $2.000 de inscripción más $500 por cada clase. Si V = 500n + 2.000, ¿cuánto se paga por 8 clases?", "$6.000", "500 × 8 + 2.000 = 6.000.")],
    sc=[
        ex("Si V = n + 9, ¿cuánto vale V cuando n = 6?", "15", "6 + 9."),
        ex("Si V = 7n − 4, ¿cuánto vale V cuando n = 3?", "17", "7 × 3 − 4."),
        ex("Escribe con letras la regla «el doble de n más 5».", "V = 2n + 5", "El doble de n es 2n y luego se suma 5."),
    ],
    op=task(
        "Observa el patrón de mesas: 1 mesa tiene 5 sillas, 2 mesas tienen 8 sillas, 3 mesas tienen 11 sillas y 4 mesas tienen 14 sillas. Escribe la regla con una letra, calcula las sillas para 10 mesas y comprueba la regla con una columna de la tabla.",
        "V = 3n + 2. Con n = 10: V = 3 × 10 + 2 = 32 sillas. Compruebo con n = 4: 3 × 4 + 2 = 14, que coincide.",
        ["escribe una regla simbólica correcta", "reemplaza y calcula", "comprueba con la tabla"],
        ["regla con letras", "cálculo y comprobación"],
        ["leer 3n como suma", "sumar antes de multiplicar"],
        "Pide que calcule otro valor de la tabla con la regla y compare.",
    ),
    reinforce="Con V = 4n + 2 calcula V para n = 1, 2, 3 y 4. Escribe la tabla.",
    extend="Inventa una regla simbólica de la forma V = an + b, escribe su tabla hasta n = 5 y pide a alguien que la descubra.",
)

# ------------------------------------------------------------------ OA 09 clase 4
lesson(
    OA9, 4,
    use="Aprenderé a usar reglas de tablas para resolver problemas: calcular valores grandes, encontrar qué n da cierto valor y comparar dos situaciones. Sirve para tomar decisiones.",
    prior=["Sé escribir y usar una regla con letras.", "Sé multiplicar, sumar y restar números naturales."],
    explain=[
        "Con una regla puedes calcular valores muy grandes sin armar toda la tabla. Si V = 800n + 1.500, para n = 6 haces 800 × 6 + 1.500 = 6.300. También puedes ir al revés: si sabes el valor y buscas n, deshaces las operaciones en orden inverso. Si V = 800n + 1.500 = 6.300, primero restas 1.500 (4.800) y luego divides por 800 (n = 6).",
        "Para comparar dos situaciones, calcula los valores de las dos reglas con los mismos n y mira cuándo coinciden o cuál es mayor. Si un plan cobra $300 por clase y otro cobra $1.000 fijos más $200 por clase, se igualan cuando 300n = 1.000 + 200n. Probando, con n = 10 cuestan $3.000 los dos.",
        "Después de calcular, vuelve a la historia. Revisa que n tenga sentido: no puede haber 3,5 clases en un problema de clases completas. Escribe la respuesta con unidades, como pesos, personas o palitos.",
    ],
    vocab=[("operación inversa", "la que deshace a otra: sumar y restar, multiplicar y dividir"), ("plan", "forma de cobrar o de organizar algo"), ("igualarse", "tener el mismo valor"), ("fijo", "que no cambia con n"), ("predecir", "decir qué valor vendrá")],
    worked=[
        W("Buscar n a partir de V", "Un taxi cobra V = 1.000 + 500n pesos por n km. ¿Cuántos km se recorren con $5.000?", ["1.000 + 500n = 5.000.", "Resto 1.000: 500n = 4.000.", "Divido por 500: n = 8."], "8 km"),
        W("Cuando dos planes se igualan", "Plan A: $300 por clase. Plan B: $1.000 fijos más $200 por clase. ¿Con cuántas clases cuestan lo mismo?", ["Pruebo con n = 10: A cuesta 300 × 10 = 3.000.", "B cuesta 1.000 + 200 × 10 = 3.000.", "Con menos clases A es más barato y con más B es más barato."], "10 clases"),
    ],
    mistakes=[
        M("Resolver 1.000 + 500n = 5.000 dividiendo primero por 500.", "No se respetó el orden inverso de las operaciones.", "Primero se resta 1.000 y después se divide por 500."),
        M("Responder n = 3,5 clases en un problema de clases completas.", "No se revisó el sentido de la respuesta.", "Pregúntate si el resultado puede ser una cantidad entera."),
    ],
    rec=[
        ex("Si V = 2n + 1, ¿cuánto vale V cuando n = 10?", "21", "2 × 10 + 1."),
        ex("Si V = 5n y V = 35, ¿cuánto vale n?", "7", "5 × 7 = 35."),
        ex("Si V = 3n y n = 5, ¿cuánto vale V?", "15", "3 × 5."),
    ],
    und=[
        ex("Si V = 3n + 4 y V = 19, ¿cuánto vale n?", "5", "19 − 4 = 15 y 15 ÷ 3 = 5."),
        ex("Si V = 6n − 2, ¿cuánto vale V cuando n = 7?", "40", "6 × 7 − 2."),
        ex("Si V = 10n + 5, ¿cuánto vale V cuando n = 4?", "45", "10 × 4 + 5."),
    ],
    app=[
        ex("Un gimnasio ficticio cobra $10.000 de matrícula y $4.000 por mes. ¿Cuántos meses se pueden pagar con $50.000, incluida la matrícula?", "10 meses", "50.000 − 10.000 = 40.000 y 40.000 ÷ 4.000 = 10."),
        ex("Una escalera de palitos usa V = 2n + 3 palitos para n peldaños. ¿Cuántos palitos se usan con 15 peldaños?", "33", "2 × 15 + 3 = 33."),
        ex("Plan A: $400 por viaje. Plan B: $1.200 fijos más $200 por viaje. ¿Con cuántos viajes cuestan lo mismo?", "6 viajes", "Con 6 viajes A cuesta 2.400 y B cuesta 1.200 + 1.200 = 2.400."),
    ],
    rea=[
        ex("Eva compara V = 5n y V = 3n + 6 haciendo una tabla con n = 1, 2, 3, 4 y 5. ¿Para qué n coinciden los dos valores?", "n = 3", "Con n = 3, 5 × 3 = 15 y 3 × 3 + 6 = 15; con n = 2 dan 10 y 12, y con n = 4 dan 20 y 18."),
        ex("Con la regla V = 4n − 1, ¿para qué n el valor es 27?", "7", "4 × 7 − 1 = 27."),
    ],
    cha=[
        ex("Con V = 3n + 2, ¿cuál es el menor n entero para que V sea mayor que 50?", "17", "Con n = 16, V = 50 que no es mayor; con n = 17, V = 53."),
        ex("Una regla de la forma V = an + b da 11 cuando n = 3 y 17 cuando n = 5. ¿Cuánto vale V cuando n = 10?", "32", "Sube 3 por cada n, entonces V = 3n + 2 y 3 × 10 + 2 = 32."),
    ],
    ctx=[ex("Un parque ficticio cobra $1.500 de entrada y $800 por cada juego. Con $6.300, ¿cuántos juegos se pueden pagar?", "6 juegos", "6.300 − 1.500 = 4.800 y 4.800 ÷ 800 = 6.")],
    sc=[
        ex("Si V = 9n − 5, ¿cuánto vale V cuando n = 4?", "31", "9 × 4 − 5."),
        ex("Si V = 5n + 3 y V = 28, ¿cuánto vale n?", "5", "28 − 3 = 25 y 25 ÷ 5."),
        ex("Si V = 2n + 10, ¿cuánto vale V cuando n = 6?", "22", "2 × 6 + 10."),
    ],
    op=task(
        "Dos tiendas de arriendo de bicicletas (ficticias) cobran así: Tienda A, $2.000 por hora. Tienda B, $3.000 por la primera hora y $1.500 por cada hora más (en total V = 1.500n + 1.500). Haz una tabla para n = 1 hasta 6 horas con el costo de cada tienda y di cuántas horas conviene cada una.",
        "A: 2.000, 4.000, 6.000, 8.000, 10.000, 12.000. B (1.500n + 1.500): 3.000, 4.500, 6.000, 7.500, 9.000, 10.500. Con 1 y 2 horas conviene A, con 3 horas cuestan igual y con 4 o más horas conviene B.",
        ["calcula los valores de cada tienda", "compara en la tabla", "responde con las horas"],
        ["tabla con seis filas", "frase de decisión"],
        ["equivocarse con la hora inicial", "no comparar fila por fila"],
        "Pide que revise que cada valor de B sube $1.500 respecto del anterior.",
    ),
    reinforce="Con V = 3n + 5, calcula V para n = 1, 2, 3 y 4. Luego averigua para qué n el valor es 26.",
    extend="Crea dos planes de cobro con una regla cada uno y encuentra para qué n cuestan lo mismo. Explica cómo lo hallaste.",
)

# ================================================================== OA 10
OA10 = "MA06 OA 10"

# ------------------------------------------------------------------ OA 10 clase 1
lesson(
    OA10, 1,
    use="Aprenderé a usar letras para representar números y a escribir expresiones con letras. Sirve para hablar de cualquier número y no solo de uno.",
    prior=["Sé usar reglas de tablas.", "Sé que una letra puede representar un número."],
    explain=[
        "En matemática una letra puede representar un número que no conocemos o que puede cambiar. Se llama variable o incógnita según el caso. «Un número aumentado en 8» se puede escribir n + 8. «El triple de un número» se escribe 3n. «La mitad de un número» se escribe n ÷ 2.",
        "Una expresión con letras es como una receta de cálculo. Para saber cuánto vale, se reemplaza la letra por un número. Si n = 5, entonces n + 8 vale 13 y 3n vale 15. El valor cambia según el número que reemplace a la letra.",
        "Lee con cuidado las palabras. «5 menos que un número» es n − 5, y no 5 − n. «El doble de un número menos 1» es 2n − 1. Cuando un número se escribe junto a una letra sin signo, como 3n, se multiplican. Siempre puedes comprobar con un número de prueba, como 10.",
    ],
    vocab=[("variable", "letra que puede representar muchos números"), ("incógnita", "letra que representa un número que se quiere encontrar"), ("expresión algebraica", "combinación de números, letras y operaciones"), ("reemplazar", "poner un número en lugar de la letra"), ("doble, triple", "dos veces, tres veces")],
    worked=[
        W("Escribir y evaluar", "Escribe «un número aumentado en 8» y calcula su valor si el número es 5.", ["Si el número es n, la expresión es n + 8.", "Reemplazo n por 5: 5 + 8 = 13."], "n + 8; vale 13"),
        W("Expresión de dos pasos", "Escribe «el doble de un número, menos 1» y calcula su valor si el número es 6.", ["El doble de n es 2n y luego se resta 1: 2n − 1.", "Reemplazo n por 6: 2 × 6 − 1 = 11."], "2n − 1; vale 11"),
    ],
    mistakes=[
        M("Escribir «5 menos que un número» como 5 − n.", "Se invirtió el orden de la resta.", "5 menos que n es n − 5. Si n = 9, vale 4."),
        M("Leer 3n como 3 + n.", "Se confundió el número pegado a la letra con una suma.", "3n significa 3 por n."),
    ],
    rec=[
        ex("Escribe con una letra «un número más 6».", "n + 6", "Más indica suma."),
        ex("Calcula el valor de n + 6 cuando n = 4.", "10", "4 + 6 = 10."),
        ex("Calcula el valor de 3n cuando n = 5.", "15", "3 × 5 = 15."),
    ],
    und=[
        ex("Escribe con letras «el triple de un número, menos 4».", "3n − 4", "El triple de n es 3n."),
        ex("Calcula el valor de 2x + 1 cuando x = 7.", "15", "2 × 7 + 1."),
        ex("Escribe con letras «la mitad de un número».", "n ÷ 2", "La mitad es dividir entre 2."),
    ],
    app=[
        ex("Ana tiene n lápices y Bea tiene 5 más que Ana. Escribe lo que tiene Bea y calcula su valor si n = 12.", "n + 5; 17", "12 + 5 = 17."),
        ex("Una caja tiene x bombones. Si hay 4 cajas iguales, escribe la cantidad de bombones y calcúlala si x = 6.", "4x; 24", "4 × 6 = 24."),
        ex("Un cuaderno cuesta c pesos. Se compran 3 cuadernos y una regla de $800. Escribe el gasto total y calcúlalo si c = 1.200.", "3c + 800; $4.400", "3 × 1.200 + 800 = 4.400."),
    ],
    rea=[
        ex("Pía escribió «5 menos que un número» como 5 − n. ¿Cuál es la expresión correcta?", "n − 5", "5 menos que n es n − 5; con n = 9, vale 4."),
        ex("¿Las expresiones 4n y n + 4 valen lo mismo cuando n = 3? Responde sí o no.", "No", "4 × 3 = 12 y 3 + 4 = 7."),
    ],
    cha=[
        ex("Si n + n + n vale 21, ¿cuánto vale n?", "7", "3 × 7 = 21."),
        ex("La expresión 2n + 3 vale 13. ¿Cuánto vale n?", "5", "2 × 5 + 3 = 13."),
    ],
    ctx=[ex("Un panadero ficticio hace x panes por hora. Si trabaja 8 horas, escribe cuántos panes hace y calcúlalo si x = 35.", "8x; 280", "8 × 35 = 280.")],
    sc=[
        ex("Calcula el valor de n + 9 cuando n = 2.", "11", "2 + 9."),
        ex("Escribe con letras «el doble de un número».", "2n", "El doble es multiplicar por 2."),
        ex("Calcula el valor de 5x − 2 cuando x = 3.", "13", "5 × 3 − 2."),
    ],
    op=task(
        "Escribe una expresión con la letra n para cada frase y calcula su valor con n = 10: 1) un número aumentado en 15; 2) el triple de un número; 3) el doble de un número, más 7; 4) 3 menos que un número. Explica con una frase por qué 3 menos que n no es 3 − n.",
        "1) n + 15 = 25; 2) 3n = 30; 3) 2n + 7 = 27; 4) n − 3 = 7. 3 − n con n = 10 no se puede calcular entre números naturales, y «3 menos que n» significa que a n se le quitan 3.",
        ["escribe bien las cuatro expresiones", "reemplaza y calcula", "explica el orden de la resta"],
        ["cuatro expresiones con valor", "frase de explicación"],
        ["invertir la resta", "leer 3n como suma"],
        "Pide que pruebe con otro número, como 8, y verifique cada expresión con la frase.",
    ),
    reinforce="Escribe con letras: «un número más 12», «el doble de un número» y «un número menos 4». Calcula cada una con n = 6.",
    extend="Inventa tres frases con la palabra «número» que se escriban con letras y pide a alguien que las escriba. Compara sus respuestas.",
)

# ------------------------------------------------------------------ OA 10 clase 2
lesson(
    OA10, 2,
    use="Aprenderé a generalizar relaciones entre números naturales con expresiones que tienen letras, como los números pares, impares y múltiplos. Sirve para hablar de muchos casos a la vez.",
    prior=["Sé escribir expresiones con una letra.", "Sé qué son los números pares e impares."],
    explain=[
        "Una generalización es una expresión que sirve para muchos casos. Un número par es un múltiplo de 2, así que se escribe 2k, donde k es un natural. Si k = 5, el par es 10. Un número impar es un par más 1: 2k + 1. Si k = 3, el impar es 7.",
        "También se generalizan los múltiplos de otros números: 5k son los múltiplos de 5. Y los patrones de figuras: si una figura con n pasos usa 3n cuadritos, la figura 6 usa 18. Dos números consecutivos son n y n + 1.",
        "Para decidir si una expresión sirve, prueba con varios números. 3n + 1 no es siempre impar: con n = 1 da 4, que es par. Para demostrar que algo no siempre es cierto basta un ejemplo que falle. Para convencer de que sí lo es, hay que explicar con la expresión.",
    ],
    vocab=[("generalizar", "escribir una regla que vale para muchos casos"), ("par", "múltiplo de 2: 2k"), ("impar", "par más 1: 2k + 1"), ("consecutivos", "que van uno después de otro: n y n + 1"), ("contraejemplo", "ejemplo que muestra que una afirmación no siempre es cierta")],
    worked=[
        W("Patrón de figuras", "Con palitos se hacen cuadrados en fila. Con 1 cuadrado se usan 4 palitos, con 2 cuadrados 7 y con 3 cuadrados 10. Escribe la expresión para n cuadrados.", ["El número de palitos sube 3 cada vez.", "Con n = 1 son 4: 3 × 1 + 1 = 4.", "La expresión es 3n + 1."], "3n + 1"),
        W("Números pares e impares", "Escribe una expresión para los números impares y calcula el impar para k = 4.", ["Un número par es 2k.", "Un impar es el par más 1: 2k + 1.", "Con k = 4: 2 × 4 + 1 = 9."], "2k + 1; vale 9"),
    ],
    mistakes=[
        M("Decir que 3n + 1 es siempre impar.", "Se probó solo con n = 2.", "Con n = 1 da 4, que es par. Un caso que falla basta para rechazarlo."),
        M("Escribir 2k + 2 para un impar.", "Se sumó 2 al par y eso da otro par.", "Un impar es un par más 1: 2k + 1."),
    ],
    rec=[
        ex("Un número par se escribe 2k. ¿Qué par resulta con k = 5?", "10", "2 × 5."),
        ex("Un número impar se escribe 2k + 1. ¿Qué impar resulta con k = 3?", "7", "2 × 3 + 1."),
        ex("Un múltiplo de 5 se escribe 5k. ¿Qué número resulta con k = 4?", "20", "5 × 4."),
    ],
    und=[
        ex("El siguiente de un número par 2k es un número impar. Escribe una expresión para ese impar.", "2k + 1", "Al par se le suma 1."),
        ex("Una figura con n pasos usa 3n cuadritos. ¿Cuántos cuadritos usa la figura 6?", "18", "3 × 6."),
        ex("Un patrón es 2, 5, 8, 11 y su expresión es 3n − 1. ¿Cuál es el 10.º término?", "29", "3 × 10 − 1."),
    ],
    app=[
        ex("Torres de cubos: la torre 1 usa 5 cubos, la 2 usa 7 y la 3 usa 9. La expresión es 2n + 3. ¿Cuántos cubos usa la torre 10?", "23", "2 × 10 + 3."),
        ex("Cada mesa tiene 4 sillas. Escribe la expresión para m mesas y calcula las sillas de 9 mesas.", "4m; 36", "4 × 9."),
        ex("Ema tiene 3 años más que su hermano. Si el hermano tiene h años, escribe la edad de Ema y calcúlala si h = 9.", "h + 3; 12", "9 + 3."),
    ],
    rea=[
        ex("Dos números consecutivos son n y n + 1. ¿Cuánto suman cuando n = 8?", "17", "8 + 9."),
        ex("Luis dice que 3n + 1 es siempre impar. Prueba con n = 1. ¿Es cierto lo que dice? Responde sí o no.", "No", "Con n = 1 da 4, que es par."),
    ],
    cha=[
        ex("Un patrón es 5, 9, 13, 17 y su expresión es 4n + 1. ¿Cuál es el 20.º término?", "81", "4 × 20 + 1."),
        ex("Con la expresión 4n + 1, ¿para qué n el valor es 41?", "10", "4 × 10 + 1."),
    ],
    ctx=[ex("En un cine ficticio cada fila tiene 12 asientos. Escribe una expresión para f filas y calcula los asientos de 15 filas.", "12f; 180", "12 × 15 = 180.")],
    sc=[
        ex("Un par se escribe 2k. ¿Qué par resulta con k = 9?", "18", "2 × 9."),
        ex("Un impar se escribe 2k + 1. ¿Qué impar resulta con k = 6?", "13", "2 × 6 + 1."),
        ex("Si una figura usa 5n palitos, ¿cuántos usa la figura 7?", "35", "5 × 7."),
    ],
    op=task(
        "Observa la secuencia de baldosas: la figura 1 usa 4 baldosas, la figura 2 usa 6, la figura 3 usa 8 y la figura 4 usa 10. Escribe una expresión con n que dé las baldosas de la figura n, calcula las baldosas de la figura 12 y explica cómo sabes que tu expresión funciona.",
        "Sube 2 cada vez. La expresión es 2n + 2. Figura 12: 2 × 12 + 2 = 26. Funciona porque con n = 1 da 4, con n = 2 da 6, con n = 3 da 8 y con n = 4 da 10.",
        ["escribe una expresión correcta", "la usa para figuras más grandes", "la comprueba con la tabla"],
        ["expresión con letra", "valor de la figura 12 y comprobación"],
        ["no comprobar con todas las figuras", "confundir cuánto sube con el primer valor"],
        "Pide que pruebe la expresión con n = 3 y n = 4.",
    ),
    reinforce="Calcula los números pares 2k y los impares 2k + 1 para k = 1, 2, 3 y 4. Escríbelos en una tabla.",
    extend="Escribe una expresión para los múltiplos de 3 y otra para los números que dejan resto 1 al dividirse por 3. Calcula los tres primeros de cada una.",
)

# ------------------------------------------------------------------ OA 10 clase 3
lesson(
    OA10, 3,
    use="Aprenderé qué es una ecuación y cómo comprobar si un número la hace verdadera. Sirve para escribir problemas en forma de igualdad.",
    prior=["Sé escribir expresiones con letras.", "Sé qué significa el signo igual."],
    explain=[
        "Una ecuación es una igualdad que tiene una letra. La letra se llama incógnita. Por ejemplo, x + 7 = 15 dice que un número más 7 es igual a 15. Resolver la ecuación es encontrar el valor de x que hace verdadera la igualdad. Aquí es x = 8, porque 8 + 7 = 15.",
        "Para comprobar si un número es la solución, reemplaza la letra y calcula los dos lados. Si los lados dan lo mismo, la igualdad es verdadera. Con x = 9 en x + 7 = 15 queda 16 = 15, que es falso. Con 3x = 27 y x = 9 queda 27 = 27, que es verdadero.",
        "Muchas situaciones se escriben como ecuaciones. «Tenía algunas figuritas, me regalaron 7 y ahora tengo 15» es x + 7 = 15. «El triple de un número es 27» es 3x = 27. Una balanza en equilibrio es una buena imagen: lo que hay en un lado pesa lo mismo que lo que hay en el otro.",
    ],
    vocab=[("ecuación", "igualdad con una letra que representa un número"), ("incógnita", "letra de la ecuación cuyo valor se busca"), ("solución", "número que hace verdadera la ecuación"), ("igualdad", "dos expresiones con el mismo valor"), ("comprobar", "reemplazar y ver que los dos lados dan lo mismo")],
    worked=[
        W("Escribir y resolver", "Escribe la ecuación «un número más 7 es 15» y encuentra la solución.", ["La ecuación es x + 7 = 15.", "Busco qué número sumado a 7 da 15: 8.", "Compruebo: 8 + 7 = 15."], "x + 7 = 15; x = 8"),
        W("Comprobar una solución", "¿Es x = 9 la solución de 3x = 27?", ["Reemplazo x por 9: 3 × 9 = 27.", "Los dos lados son 27, entonces es verdadero."], "Sí, x = 9"),
    ],
    mistakes=[
        M("Decir que x = 9 es solución de x + 7 = 15 porque 9 es mayor que 7.", "No se reemplazó para comprobar.", "9 + 7 = 16, que no es 15. La solución es 8."),
        M("Escribir «el doble de un número es 18» como x + 2 = 18.", "Se tradujo doble como suma de 2.", "El doble es 2x, entonces 2x = 18."),
    ],
    rec=[
        ex("¿Es x = 5 solución de x + 3 = 8? Responde sí o no.", "Sí", "5 + 3 = 8."),
        ex("¿Es x = 4 solución de x + 3 = 8? Responde sí o no.", "No", "4 + 3 = 7 y no 8."),
        ex("¿Qué número x cumple x + 2 = 10?", "8", "8 + 2 = 10."),
    ],
    und=[
        ex("Escribe la ecuación «el doble de un número es 18».", "2x = 18", "El doble de x es 2x."),
        ex("¿Qué número x cumple 4x = 20?", "5", "4 × 5 = 20."),
        ex("¿Es x = 6 solución de 2x + 1 = 13? Responde sí o no.", "Sí", "2 × 6 + 1 = 13."),
    ],
    app=[
        ex("Tenía algunas figuritas, me regalaron 9 y ahora tengo 24. Escribe la ecuación con x y encuentra x.", "x + 9 = 24; x = 15", "15 + 9 = 24."),
        ex("Una caja tiene x bombones. Cuatro cajas iguales tienen 36 bombones. Escribe la ecuación y encuentra x.", "4x = 36; x = 9", "4 × 9 = 36."),
        ex("Un libro tiene x páginas. Leí 28 y me faltan 47. Escribe la ecuación y encuentra x.", "x − 28 = 47; x = 75", "75 − 28 = 47."),
    ],
    rea=[
        ex("Ana dice que x = 10 es solución de 3x − 5 = 25. ¿Tiene razón? Responde sí o no.", "Sí", "3 × 10 − 5 = 25."),
        ex("Beto traduce «el triple de un número, más 4, es 19» como 3 + x + 4 = 19. ¿Cuál es la ecuación correcta?", "3x + 4 = 19", "El triple de x es 3x y luego se suma 4."),
    ],
    cha=[
        ex("¿Qué número x cumple 5x − 3 = 22?", "5", "5 × 5 − 3 = 22."),
        ex("Las ecuaciones x + 6 = 14 y 2x = 16 tienen la misma solución. ¿Cuál?", "8", "8 + 6 = 14 y 2 × 8 = 16."),
    ],
    ctx=[ex("Una escuela ficticia tenía x sillas, compró 18 y ahora tiene 65. Escribe la ecuación y encuentra cuántas tenía.", "x + 18 = 65; x = 47", "47 + 18 = 65.")],
    sc=[
        ex("¿Qué número x cumple x + 12 = 20?", "8", "8 + 12."),
        ex("¿Qué número x cumple 6x = 42?", "7", "6 × 7."),
        ex("Escribe la ecuación «un número menos 5 es 11».", "x − 5 = 11", "Menos indica resta."),
    ],
    op=task(
        "Escribe una ecuación para cada situación y encuentra la solución probando números: 1) «Pensé un número, le sumé 14 y obtuve 31». 2) «El doble de mi edad menos 3 es 21». Comprueba reemplazando la letra y explica con una frase qué significa que un número sea solución.",
        "1) x + 14 = 31, x = 17 porque 17 + 14 = 31. 2) 2x − 3 = 21, x = 12 porque 2 × 12 − 3 = 21. Un número es solución si al reemplazarlo los dos lados dan lo mismo.",
        ["escribe bien la ecuación", "encuentra y comprueba la solución", "explica qué es una solución"],
        ["dos ecuaciones con solución", "comprobación escrita"],
        ["traducir mal doble o triple", "no comprobar reemplazando"],
        "Pide que reemplace la solución en los dos lados y que muestre que son iguales.",
    ),
    reinforce="Comprueba si x = 6 es solución de x + 9 = 15, 2x = 14 y 3x − 2 = 16.",
    extend="Inventa una ecuación de la forma ax + b = c cuya solución sea x = 5 y explica cómo la construiste.",
)

# ------------------------------------------------------------------ OA 10 clase 4
lesson(
    OA10, 4,
    use="Aprenderé a representar con ecuaciones situaciones nuevas, incluso cuando hay dos cantidades relacionadas. Sirve para resolver problemas con una incógnita.",
    prior=["Sé escribir expresiones y ecuaciones sencillas.", "Sé comprobar una solución."],
    explain=[
        "Cuando un problema habla de dos cantidades relacionadas, elige una como incógnita y escribe la otra con ella. Si Ana tiene el doble de figuritas que Beto, y Beto tiene x, Ana tiene 2x. Si juntos tienen 18, la ecuación es x + 2x = 18, es decir 3x = 18, y entonces x = 6.",
        "Primero define la letra: «x es la cantidad de figuritas de Beto». Luego traduce cada frase a una expresión y escribe la igualdad que cuenta la historia. Después busca el valor que la hace verdadera y comprueba en el problema, no solo en la ecuación.",
        "Las expresiones equivalentes valen lo mismo: x + x + x es lo mismo que 3x. Reconocerlas ayuda a simplificar. Al final responde con las unidades y revisa que cada cantidad tenga sentido: no puede ser negativa ni quedar con coma si son personas.",
    ],
    vocab=[("definir la incógnita", "decir qué representa la letra"), ("expresión equivalente", "expresión que vale lo mismo que otra"), ("relación", "forma en que dos cantidades dependen una de otra"), ("situación", "historia o problema que se quiere resolver"), ("unidad", "palabra que dice de qué es la cantidad")],
    worked=[
        W("Dos cantidades relacionadas", "Ana tiene el doble de figuritas que Beto. Juntos tienen 18. ¿Cuántas tiene cada uno?", ["Sea x las figuritas de Beto. Ana tiene 2x.", "Ecuación: x + 2x = 18, o sea 3x = 18.", "x = 6. Beto tiene 6 y Ana 12."], "Beto 6 y Ana 12"),
        W("Perímetro como ecuación", "Un rectángulo tiene el largo 3 cm mayor que el ancho y su perímetro es 26 cm. ¿Cuánto mide el ancho?", ["Sea x el ancho. El largo es x + 3.", "Perímetro: 2x + 2(x + 3) = 26, o sea 4x + 6 = 26.", "4x = 20, entonces x = 5."], "Ancho 5 cm y largo 8 cm"),
    ],
    mistakes=[
        M("Escribir x + 2 = 18 para «Ana tiene el doble que Beto».", "Se confundió el doble con sumar 2.", "El doble de x es 2x."),
        M("Dar x = 6 como respuesta sin decir quién tiene 6.", "No se interpretó la solución en la historia.", "Beto tiene 6; Ana tiene 2 × 6 = 12."),
    ],
    rec=[
        ex("Si Beto tiene x figuritas y Ana tiene el doble, ¿cuántas tiene Ana?", "2x", "El doble de x es 2x."),
        ex("Simplifica x + x + x.", "3x", "Sumar tres veces x es 3 por x."),
        ex("Si 2x = 12, ¿cuánto vale x?", "6", "2 × 6 = 12."),
    ],
    und=[
        ex("Un hermano tiene x años y su hermana tiene 4 años más. Escribe la edad de la hermana.", "x + 4", "Más 4 indica suma."),
        ex("Si x + 2x = 21, ¿cuánto vale x?", "7", "3x = 21 y 3 × 7 = 21."),
        ex("Si 4x + 2 = 26, ¿cuánto vale x?", "6", "4 × 6 + 2 = 26."),
    ],
    app=[
        ex("Pía tiene el triple de lápices que Teo. Juntos tienen 20. ¿Cuántos lápices tiene Teo?", "5", "x + 3x = 4x = 20 y x = 5."),
        ex("Un rectángulo tiene el largo 4 cm mayor que el ancho y su perímetro es 32 cm. ¿Cuánto mide el ancho?", "6 cm", "2x + 2(x + 4) = 4x + 8 = 32 y x = 6."),
        ex("Un número y su doble suman 45. ¿Cuál es el número?", "15", "x + 2x = 3x = 45 y x = 15."),
    ],
    rea=[
        ex("Eva escribió x + 2 = 30 para «el doble de un número es 30». ¿Cuál es la ecuación correcta?", "2x = 30", "El doble de x es 2x."),
        ex("¿Las expresiones x + x + x + x y 4x son equivalentes? Responde sí o no.", "Sí", "Ambas valen lo mismo para cualquier x."),
    ],
    cha=[
        ex("La suma de tres números consecutivos es 36. Si el menor es x, la ecuación es x + (x + 1) + (x + 2) = 36. ¿Cuál es el menor?", "11", "3x + 3 = 36, entonces 3x = 33 y x = 11."),
        ex("Un padre tiene el triple de la edad de su hijo. Entre los dos suman 48 años. ¿Cuántos años tiene el hijo?", "12", "x + 3x = 4x = 48 y x = 12."),
    ],
    ctx=[ex("En una biblioteca ficticia hay el doble de libros de cuentos que de poesía. Entre los dos tipos hay 90 libros. ¿Cuántos libros de poesía hay?", "30", "x + 2x = 3x = 90 y x = 30.")],
    sc=[
        ex("Si 5x = 45, ¿cuánto vale x?", "9", "5 × 9 = 45."),
        ex("Si x + 3x = 28, ¿cuánto vale x?", "7", "4x = 28."),
        ex("Escribe «el doble de un número más 3 es 17».", "2x + 3 = 17", "El doble de x es 2x y se suma 3."),
    ],
    op=task(
        "Resuelve este problema con una ecuación: «Dos amigos juntan $30.000. Julia aporta $4.000 más que Mario». Define la letra, escribe la ecuación, encuentra cuánto aporta cada uno y comprueba que la suma da $30.000.",
        "Sea x lo que aporta Mario; Julia aporta x + 4.000. La ecuación es x + x + 4.000 = 30.000, o 2x + 4.000 = 30.000. Entonces 2x = 26.000 y x = 13.000. Mario aporta $13.000 y Julia $17.000. Suman $30.000.",
        ["define la letra", "escribe la ecuación correcta", "resuelve y comprueba en el problema"],
        ["definición de la incógnita", "ecuación y solución", "comprobación"],
        ["no definir la letra", "responder solo el valor de x"],
        "Pide que sume las dos cantidades y compare con el total antes de dar la respuesta.",
    ),
    reinforce="Pablo tiene x lápices y Sara tiene el doble. Si juntos tienen 24, escribe la ecuación y encuentra x.",
    extend="Inventa un problema con una cantidad que es el triple de otra y una suma total. Escribe la ecuación y resuélvelo.",
)
