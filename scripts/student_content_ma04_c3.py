"""Student material for 4.º básico Matemática, OA 24 (volumen en unidades cúbicas), clases 2 a 5."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA24 = "MA04 OA 24"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA24, 2,
    materials="Cubos de juego iguales o cuadraditos de papel doblados como cubos, si los tienes. Los ejercicios describen cada cuerpo con números, así que también puedes resolver sin cubos.",
    use="Aprenderé a construir cuerpos con cubos y a compararlos por su volumen. Sirve para decidir cuál caja o construcción ocupa más espacio.",
    prior=["Sé que el volumen se mide con cubos iguales.", "Sé multiplicar números pequeños."],
    explain=[
        "Para construir un cuerpo con cubos, los pones en filas, las filas forman una capa y las capas se apilan. Todos los cubos deben ser iguales y tocar a otros cubos por sus caras, sin huecos escondidos.",
        "Para comparar dos cuerpos, cuenta cuántos cubos tiene cada uno. El que tiene más cubos tiene más volumen. No te dejes engañar por la forma: un cuerpo alto y delgado puede tener menos cubos que uno bajo y ancho.",
        "Por ejemplo, un cuerpo de 1 fila de 6 cubos y 3 capas tiene 18 cubos. Otro de 2 filas de 4 cubos y 2 capas tiene 16 cubos. Aunque el primero parece más alto, la diferencia se ve al contar: 18 − 16 = 2 cubos más.",
    ],
    vocab=[("capa", "piso de cubos que se apila sobre otro"), ("fila", "línea de cubos uno al lado del otro"), ("cara", "lado plano de un cubo"), ("comparar volúmenes", "contar cuántos cubos iguales tiene cada cuerpo")],
    worked=[
        {"title": "Comparar dos cuerpos", "problem": "El cuerpo A tiene 2 filas de 5 cubos en 2 capas. El cuerpo B tiene 1 fila de 8 cubos en 3 capas. ¿Cuál tiene más volumen?", "steps": ["A: 2 × 5 = 10 cubos por capa y 10 × 2 = 20 cubos.", "B: 1 × 8 = 8 cubos por capa y 8 × 3 = 24 cubos."], "answer": "B tiene más volumen: 24 cubos contra 20 cubos"},
        {"title": "Cuánto más", "problem": "Si A tiene 20 cubos y B tiene 24 cubos, ¿cuántos cubos más tiene B?", "steps": ["Resto la cantidad menor a la mayor.", "24 − 20 = 4."], "answer": "B tiene 4 cubos más"},
    ],
    mistakes=[
        {"wrong": "Decir que el cuerpo más alto es el de mayor volumen.", "why": "Se mira la altura y no el total de cubos.", "fix": "Cuenta todos los cubos de cada cuerpo y compara los totales."},
        {"wrong": "Contar solo los cubos que se ven por fuera.", "why": "Los cubos de adentro también ocupan espacio.", "fix": "Multiplica filas por cubos de cada fila por capas para incluir todos."},
    ],
    tiers={
        "recovery": [
            arith("Una capa tiene 2 filas de 3 cubos. ¿Cuántos cubos tiene la capa?", "2*3", "Se multiplica el número de filas por los cubos de cada fila.", " cubos"),
            arith("Una torre tiene 4 capas de 3 cubos cada una. ¿Cuántos cubos usa?", "4*3", "Se multiplica el número de capas por los cubos de cada capa.", " cubos"),
            ex("Entre un cuerpo de 14 cubos y otro de 16 cubos iguales, ¿cuál tiene más volumen?", "El de 16 cubos", "16 es mayor que 14."),
        ],
        "understand": [
            ex("¿Por qué un cuerpo alto puede tener menos volumen que uno bajo y ancho?", "Porque el volumen depende de todos los cubos, no solo de la altura", "El conteo total decide el volumen."),
            arith("El cuerpo A tiene 3 filas de 4 cubos en 2 capas. ¿Cuántos cubos tiene?", "3*4*2", "Se multiplican filas, cubos por fila y capas.", " cubos"),
            arith("El cuerpo B tiene 2 filas de 6 cubos en 2 capas. ¿Cuántos cubos tiene?", "2*6*2", "Se multiplican filas, cubos por fila y capas.", " cubos"),
        ],
        "apply": [
            ex("Un cuerpo C tiene 1 fila de 9 cubos en 2 capas y un cuerpo D tiene 3 filas de 3 cubos en 1 capa. ¿Cuál tiene más cubos?", "C, con 18 cubos contra 9", "C: 1 × 9 × 2 = 18; D: 3 × 3 × 1 = 9.", calc="1*9*2"),
            ex("Un cuerpo A tiene 24 cubos y otro B tiene 30 cubos iguales. ¿Cuántos cubos más tiene B?", "6", "30 − 24 = 6.", calc="30-24"),
            ex("Un cuerpo tiene 2 filas de 5 cubos y 3 capas, y otro tiene 5 filas de 2 cubos y 3 capas. ¿Tienen el mismo volumen?", "Sí, 30 cubos cada uno", "2 × 5 × 3 = 5 × 2 × 3 = 30.", calc="2*5*3"),
        ],
        "reason": [
            ex("Teo dice que un cuerpo de 3 capas siempre tiene más cubos que uno de 2 capas. Un cuerpo tiene 3 capas de 4 cubos y otro 2 capas de 9 cubos. ¿Teo tiene razón?", "No; el segundo tiene 18 cubos y el primero 12", "3 × 4 = 12 y 2 × 9 = 18.", calc="2*9"),
            ex("¿Por qué no basta contar los cubos que se ven por fuera?", "Porque los de adentro también ocupan espacio", "El volumen incluye todo el interior."),
        ],
        "challenge": [
            ex("Un cuerpo tiene 3 capas. La primera capa tiene 6 cubos, la segunda 6 y la tercera 4. ¿Cuántos cubos tiene en total?", "16 cubos", "6 + 6 + 4 = 16.", calc="6+6+4"),
            ex("Cuerpo A: 4 filas de 2 cubos en 3 capas. Cuerpo B: 3 filas de 3 cubos en 3 capas. ¿Cuál tiene más y por cuántos cubos?", "B, por 3 cubos", "A: 4 × 2 × 3 = 24; B: 3 × 3 × 3 = 27.", calc="3*3*3-4*2*3"),
        ],
    },
    context=[ex("En un taller, Mía arma una torre de 3 filas de 2 cubos en 4 capas y Beto arma una de 2 filas de 4 cubos en 3 capas. ¿Quién usa más cubos?", "Ninguno; los dos usan 24 cubos", "3 × 2 × 4 = 24 y 2 × 4 × 3 = 24; son iguales.", calc="3*2*4")],
    selfcheck=[
        ex("¿Cuántos cubos tiene un cuerpo de 2 filas de 4 cubos en 1 capa?", "8", "2 × 4 × 1 = 8.", calc="2*4*1"),
        ex("¿Cuántos cubos hay en 3 capas de 5 cubos cada una?", "15", "3 × 5 = 15.", calc="3*5"),
        ex("¿Qué cuerpo tiene más volumen: uno de 21 cubos o uno de 19 cubos iguales?", "El de 21 cubos", "21 es mayor que 19."),
    ],
    open_task=task(
        "Elige dos cuerpos de la lista: A (2 filas de 3 cubos en 2 capas), B (1 fila de 10 cubos en 1 capa), C (3 filas de 2 cubos en 3 capas). Calcula cuántos cubos tiene cada uno y di cuál ocupa más espacio. Si tienes cubos de juego, arma tus dos cuerpos para comprobar.",
        "A tiene 2 × 3 × 2 = 12 y C tiene 3 × 2 × 3 = 18. C ocupa más espacio.",
        ["elige dos cuerpos de la lista", "calcula los cubos de cada uno", "compara los totales", "usa la palabra volumen"],
        ["dos cálculos", "comparación"],
        ["comparar por altura", "olvidar una capa"],
        "Pide justificar con el número de cubos. Reconoce que compare totales y no formas.",
    ),
    reinforce="Con bloques o cubos, arma dos torres distintas con el mismo número de cubos y compáralas.",
    extend="Arma o dibuja un cuerpo de 18 cubos que sea más alto que ancho y otro de 18 cubos que sea más ancho que alto.",
)

register(
    OA24, 3,
    materials="Lápiz y papel. Los cuerpos están descritos con números de filas, de cubos por fila y de capas. Con cubos de juego puedes armarlos.",
    use="Aprenderé a contar cubos por capas sin contar uno por uno. Sirve para calcular el volumen de cajas llenas de cubos.",
    prior=["Sé multiplicar con las tablas.", "Sé que una capa es un piso de cubos."],
    explain=[
        "Un cuerpo hecho con cubos se puede contar por capas. Primero cuentas cuántos cubos hay en una capa: es el número de filas por el número de cubos de cada fila. Por ejemplo, 3 filas de 4 cubos son 3 × 4 = 12 cubos en una capa.",
        "Después multiplicas por el número de capas, si todas las capas son iguales. Con 5 capas, hay 12 × 5 = 60 cubos. Así se evita contar uno por uno y no se olvidan los cubos de adentro.",
        "Si las capas no son iguales, cuentas cada capa y sumas los totales. Por ejemplo, capas de 8, 8 y 5 cubos dan 8 + 8 + 5 = 21 cubos. Comprueba que tu respuesta sea razonable mirando las medidas.",
    ],
    vocab=[("capa", "piso de cubos que forma el cuerpo"), ("base", "capa de abajo del cuerpo"), ("altura (en cubos)", "cuántas capas tiene el cuerpo"), ("total de cubos", "cantidad de cubos de todo el cuerpo")],
    worked=[
        {"title": "Capas iguales", "problem": "Una caja se llena con 4 capas. Cada capa tiene 3 filas de 5 cubos. ¿Cuántos cubos caben?", "steps": ["Una capa tiene 3 × 5 = 15 cubos.", "Con 4 capas: 15 × 4 = 60."], "answer": "Caben 60 cubos"},
        {"title": "Capas distintas", "problem": "Una torre tiene una capa de 9 cubos, otra de 9 cubos y otra de 6 cubos. ¿Cuántos cubos tiene?", "steps": ["Sumo cada capa: 9 + 9 + 6.", "9 + 9 + 6 = 24."], "answer": "Tiene 24 cubos"},
    ],
    mistakes=[
        {"wrong": "Contar solo una capa y decir que ese es el volumen de todo el cuerpo.", "why": "Se olvidan las otras capas.", "fix": "Multiplica los cubos de una capa por el número de capas."},
        {"wrong": "Sumar 3 + 5 + 4 en vez de multiplicar filas, cubos por fila y capas.", "why": "Se suma lo que hay que multiplicar.", "fix": "Multiplica: 3 × 5 × 4 = 60."},
    ],
    tiers={
        "recovery": [
            arith("Una capa tiene 2 filas de 5 cubos. ¿Cuántos cubos tiene la capa?", "2*5", "Se multiplica filas por cubos de cada fila.", " cubos"),
            arith("Un cuerpo tiene 3 capas de 6 cubos cada una. ¿Cuántos cubos tiene?", "3*6", "Se multiplica el número de capas por los cubos de una capa.", " cubos"),
            ex("¿Cuántas capas tiene un cuerpo de 4 pisos de cubos?", "4", "Cada piso es una capa."),
        ],
        "understand": [
            ex("¿Qué se calcula primero para contar un cuerpo por capas?", "Los cubos de una capa", "Después se multiplica por el número de capas."),
            arith("Cada capa tiene 4 filas de 3 cubos y hay 2 capas. ¿Cuántos cubos hay?", "4*3*2", "Se multiplican filas, cubos por fila y capas.", " cubos"),
            ex("Una torre tiene capas de 6, 6 y 3 cubos. ¿Cuántos cubos tiene?", "15", "6 + 6 + 3 = 15.", calc="6+6+3"),
        ],
        "apply": [
            arith("Una caja tiene capas de 5 filas de 4 cubos, y hay 3 capas. ¿Cuántos cubos caben?", "5*4*3", "Se multiplican filas, cubos por fila y capas.", " cubos"),
            arith("Un cuerpo tiene 2 filas de 7 cubos en 4 capas. ¿Cuántos cubos tiene?", "2*7*4", "Se multiplican filas, cubos por fila y capas.", " cubos"),
            ex("La base tiene 12 cubos y el cuerpo tiene 5 capas iguales. ¿Cuántos cubos tiene?", "60", "12 × 5 = 60.", calc="12*5"),
        ],
        "reason": [
            ex("Sara dice que un cuerpo con una capa de 10 cubos y 3 capas tiene 13 cubos. ¿Qué hizo mal?", "Sumó en vez de multiplicar; tiene 30 cubos", "10 × 3 = 30.", calc="10*3"),
            ex("Una caja se llena con 6 cubos en la base y tiene 4 capas. Otro estudiante dice que tiene 24 cubos. ¿Estás de acuerdo? Explica.", "Sí, porque 6 × 4 = 24", "Cada capa tiene 6 y hay 4 capas.", calc="6*4"),
        ],
        "challenge": [
            ex("Un cuerpo tiene 48 cubos en 4 capas iguales. ¿Cuántos cubos tiene cada capa?", "12", "48 ÷ 4 = 12.", calc="48//4"),
            ex("Una torre tiene una base de 3 filas de 4 cubos y encima otra capa de 2 filas de 4 cubos. ¿Cuántos cubos tiene en total?", "20 cubos", "3 × 4 = 12 y 2 × 4 = 8; 12 + 8 = 20.", calc="3*4+2*4"),
        ],
    },
    context=[ex("Una caja se llena con cubos: tiene 5 filas de 4 cubos y 2 capas. Si se saca una capa completa, ¿cuántos cubos quedan en la caja?", "20 cubos", "Cada capa tiene 5 × 4 = 20 cubos y queda una capa.", calc="5*4")],
    selfcheck=[
        ex("¿Cuántos cubos tiene una capa de 3 filas de 8?", "24", "3 × 8 = 24.", calc="3*8"),
        ex("¿Cuántos cubos hay en 4 capas de 9 cubos?", "36", "4 × 9 = 36.", calc="4*9"),
        ex("Una torre tiene capas de 10, 8 y 5 cubos. ¿Cuántos cubos hay?", "23", "10 + 8 + 5 = 23.", calc="10+8+5"),
    ],
    open_task=task(
        "Elige un cuerpo de la lista: A tiene 3 filas de 4 cubos en 3 capas, B tiene 2 filas de 5 cubos en 4 capas, C tiene 4 filas de 4 cubos en 2 capas. Escribe cuántos cubos tiene una capa, cuántos cubos tiene todo el cuerpo y cómo lo calculaste.",
        "B: una capa tiene 2 × 5 = 10 cubos y con 4 capas hay 10 × 4 = 40 cubos.",
        ["elige un cuerpo de la lista", "calcula los cubos de una capa", "calcula el total", "explica el procedimiento"],
        ["cubos por capa", "total", "explicación"],
        ["sumar en vez de multiplicar", "olvidar capas"],
        "Pide comprobar contando de otra manera. Reconoce que calcule primero la capa.",
    ),
    reinforce="Con cuadritos de papel o bloques, arma una capa y apílala en dos capas. Cuenta los cubos por capas.",
    extend="Un cuerpo de 36 cubos tiene capas iguales. Escribe dos posibles formas de capas y su número de capas.",
)

register(
    OA24, 4,
    materials="Lápiz y papel. Si tienes acceso a un programa de geometría con cubos, un adulto puede ayudarte a probarlo; no es obligatorio.",
    use="Aprenderé a escribir bien el volumen en unidades cúbicas. Sirve para que otras personas entiendan cuánto espacio ocupa algo.",
    prior=["Sé contar cubos por capas.", "Sé que el volumen se mide con cubos iguales."],
    explain=[
        "Al registrar un volumen, escribes el número de cubos y la unidad. Si usas cubos pequeños de una misma medida, se escribe «unidades cúbicas». Por ejemplo, un cuerpo de 24 cubos tiene volumen de 24 unidades cúbicas.",
        "El área se mide con cuadrados y el volumen con cubos. El área cubre una superficie plana. El volumen llena un espacio de tres direcciones: largo, ancho y alto. Por eso el volumen necesita cubos y no cuadrados.",
        "Un programa de geometría puede mostrar un cuerpo con cubos y contar sus capas. También puedes registrar en una tabla el cuerpo, las filas, los cubos por fila, las capas y el volumen. Así otra persona puede comprobar tu trabajo.",
    ],
    vocab=[("unidad cúbica", "cubo que se usa como unidad para medir volumen"), ("registrar", "escribir un resultado con su unidad"), ("tabla", "organización de datos en filas y columnas"), ("software geométrico", "programa que permite construir y mover figuras y cuerpos")],
    worked=[
        {"title": "Registrar el volumen", "problem": "Un cuerpo tiene 4 filas de 3 cubos en 2 capas. Escribe su volumen con unidad.", "steps": ["Cubos: 4 × 3 × 2 = 24.", "Escribo el número y la unidad."], "answer": "El volumen es 24 unidades cúbicas"},
        {"title": "Elegir entre área y volumen", "problem": "Quieres saber cuánto cabe dentro de una caja. ¿Mides área o volumen?", "steps": ["Dentro de una caja cabe un espacio con largo, ancho y alto.", "Ese espacio se mide con cubos."], "answer": "Se mide el volumen"},
    ],
    mistakes=[
        {"wrong": "Escribir solo 24 sin la unidad.", "why": "Se olvida decir qué se contó.", "fix": "Escribe 24 unidades cúbicas."},
        {"wrong": "Medir el volumen con cuadrados.", "why": "Los cuadrados no ocupan espacio de tres direcciones.", "fix": "Usa cubos: el volumen se mide en unidades cúbicas."},
    ],
    tiers={
        "recovery": [
            ex("¿Con qué unidad se mide el volumen: cuadrados o cubos?", "Cubos", "El volumen es un espacio de tres direcciones."),
            arith("Un cuerpo tiene 2 filas de 5 cubos en 2 capas. ¿Cuántas unidades cúbicas ocupa?", "2*5*2", "Se multiplican filas, cubos por fila y capas.", " unidades cúbicas"),
            ex("¿Qué se escribe junto al número 18 cuando mides un volumen?", "Unidades cúbicas", "La unidad dice qué se contó."),
        ],
        "understand": [
            ex("¿Qué mide el área: una superficie plana o el espacio de un cuerpo?", "Una superficie plana", "El volumen es el que mide el espacio."),
            arith("Una tabla registra 3 filas, 4 cubos por fila y 3 capas. ¿Cuál es el volumen?", "3*4*3", "Se multiplican las tres cantidades.", " unidades cúbicas"),
            ex("¿Cuál se mide con cubos: el piso de una sala o el cuerpo de una caja?", "El cuerpo de una caja", "La caja ocupa espacio en tres direcciones; el piso es una superficie."),
        ],
        "apply": [
            ex("Completa el registro: filas 3, cubos por fila 5, capas 2. ¿Cuál es el volumen con su unidad?", "30 unidades cúbicas", "3 × 5 × 2 = 30.", calc="3*5*2"),
            ex("Una caja tiene capas de 12, 12 y 8 cubos. Escribe su volumen con unidad.", "32 unidades cúbicas", "12 + 12 + 8 = 32.", calc="12+12+8"),
            ex("Dos cuerpos: uno de 28 unidades cúbicas y otro de 25 unidades cúbicas. ¿Cuántas unidades cúbicas más tiene el primero?", "3 unidades cúbicas", "28 − 25 = 3.", calc="28-25"),
        ],
        "reason": [
            ex("Un estudiante escribió «El volumen es 24». ¿Qué le falta?", "La unidad: unidades cúbicas", "Sin unidad no se sabe qué se contó."),
            ex("Beto midió el volumen de una caja con cuadrados de papel. ¿Qué error hay?", "El volumen se mide con cubos, no con cuadrados", "Los cuadrados cubren superficie, no llenan espacio."),
        ],
        "challenge": [
            ex("Un cuerpo A tiene 3 filas de 3 cubos en 3 capas. Otro, B, tiene 2 filas de 7 cubos en 2 capas. ¿Cuál tiene mayor volumen y por cuánto?", "B, por 1 unidad cúbica", "A: 3 × 3 × 3 = 27; B: 2 × 7 × 2 = 28. Entonces B tiene 1 más.", calc="2*7*2-27"),
            ex("Se registran dos cuerpos: 4 filas de 2 cubos en 2 capas y 2 filas de 4 cubos en 2 capas. ¿Tienen el mismo volumen?", "Sí, 16 unidades cúbicas", "4 × 2 × 2 = 2 × 4 × 2 = 16.", calc="4*2*2"),
        ],
    },
    context=[ex("Ema registra tres cuerpos en su cuaderno: 12 unidades cúbicas, 18 unidades cúbicas y 15 unidades cúbicas. ¿Cuántas unidades cúbicas hay en total entre los tres?", "45 unidades cúbicas", "12 + 18 + 15 = 45.", calc="12+18+15")],
    selfcheck=[
        ex("Escribe el volumen de un cuerpo de 4 filas de 4 cubos en 1 capa.", "16 unidades cúbicas", "4 × 4 × 1 = 16.", calc="4*4*1"),
        ex("¿Qué dice la unidad «unidades cúbicas»?", "Que se contaron cubos iguales", "La unidad indica con qué se midió."),
        ex("¿Qué cuerpo tiene mayor volumen: 22 unidades cúbicas o 20 unidades cúbicas?", "El de 22 unidades cúbicas", "22 es mayor que 20."),
    ],
    open_task=task(
        "Completa una tabla en tu cuaderno con estos tres cuerpos: A (2 filas, 3 cubos por fila, 2 capas), B (3 filas, 3 cubos por fila, 2 capas) y C (2 filas, 4 cubos por fila, 3 capas). Escribe el volumen de cada uno con su unidad y di cuál es mayor. Si usas un programa de geometría, compara tu resultado con el que muestra.",
        "A: 2 × 3 × 2 = 12 unidades cúbicas. B: 18. C: 24. El mayor es C.",
        ["completa los tres cálculos", "escribe la unidad cúbica", "compara los resultados", "indica el mayor"],
        ["tabla o lista", "unidad", "comparación"],
        ["olvidar la unidad", "multiplicar mal"],
        "Pide revisar si cada resultado tiene unidad. Reconoce la comparación final.",
    ),
    reinforce="Elige una caja pequeña y estima cuántos cubos de juego cabrían. Anota tu estimación con unidad.",
    extend="Explica con tus palabras la diferencia entre registrar un área y registrar un volumen, con un ejemplo de cada uno.",
)

register(
    OA24, 5,
    materials="Cubos de juego iguales, si tienes. Si no, usa los números de los ejercicios y papel cuadriculado para dibujar capas.",
    use="Aprenderé a diseñar cuerpos distintos con el mismo volumen. Sirve para armar cajas de distinta forma que guardan lo mismo.",
    prior=["Sé calcular el volumen en cubos.", "Sé encontrar pares de números que multiplican un número dado."],
    explain=[
        "Dos cuerpos con formas distintas pueden tener el mismo volumen. Por ejemplo, 12 cubos se pueden ordenar en una fila larga de 12, en 2 filas de 6, en 3 filas de 4 o en 2 filas de 3 con 2 capas.",
        "Para diseñar un cuerpo de un volumen dado, busca tres números que multipliquen para dar ese volumen: filas, cubos por fila y capas. Para 12: 1 × 12 × 1, 2 × 6 × 1, 3 × 4 × 1 y 2 × 3 × 2 son todos buenos.",
        "El volumen no cambia si solo cambias la forma, siempre que uses los mismos cubos. Un cuerpo que se ve alto y delgado puede tener el mismo volumen que uno bajo y ancho. Para comprobar, calcula el producto de los tres números.",
    ],
    vocab=[("mismo volumen", "igual cantidad de cubos"), ("diseñar", "planear la forma de un cuerpo"), ("factores", "los números que se multiplican para obtener el volumen"), ("forma", "aspecto exterior de un cuerpo")],
    worked=[
        {"title": "Dos cuerpos de 12 cubos", "problem": "¿Tienen el mismo volumen un cuerpo de 3 filas de 4 cubos en 1 capa y otro de 2 filas de 3 cubos en 2 capas?", "steps": ["Primero: 3 × 4 × 1 = 12.", "Segundo: 2 × 3 × 2 = 12."], "answer": "Sí, ambos tienen 12 unidades cúbicas"},
        {"title": "Diseñar con 16 cubos", "problem": "Diseña un cuerpo de 16 cubos con 2 capas.", "steps": ["En cada capa debe haber 16 ÷ 2 = 8 cubos.", "Ordeno 8 cubos como 2 filas de 4."], "answer": "2 filas de 4 cubos en 2 capas"},
    ],
    mistakes=[
        {"wrong": "Creer que un cuerpo más alto tiene más cubos que uno más bajo.", "why": "Se compara solo una medida.", "fix": "Multiplica filas, cubos por fila y capas en cada cuerpo."},
        {"wrong": "Cambiar la cantidad de cubos al armar otra forma.", "why": "Se pierde la cuenta al mover cubos.", "fix": "Cuenta de nuevo y comprueba que el producto sea el mismo."},
    ],
    tiers={
        "recovery": [
            arith("Un cuerpo tiene 1 fila de 8 cubos en 1 capa. ¿Cuántos cubos tiene?", "1*8*1", "Se multiplican las tres cantidades.", " cubos"),
            arith("Otro cuerpo tiene 2 filas de 4 cubos en 1 capa. ¿Cuántos cubos tiene?", "2*4*1", "Se multiplican las tres cantidades.", " cubos"),
            ex("¿Los dos cuerpos anteriores (1 × 8 × 1 y 2 × 4 × 1) tienen el mismo volumen?", "Sí, 8 cubos cada uno", "Los dos productos son 8."),
        ],
        "understand": [
            ex("¿Pueden dos cuerpos con formas distintas tener el mismo volumen?", "Sí", "Lo que importa es la cantidad de cubos."),
            ex("Para 12 cubos, ¿sirve ordenarlos como 2 filas de 3 cubos en 2 capas?", "Sí", "2 × 3 × 2 = 12."),
            ex("Un cuerpo de 3 × 3 × 2 cubos, ¿tiene el mismo volumen que uno de 2 × 3 × 3?", "Sí, 18 cubos cada uno", "3 × 3 × 2 = 2 × 3 × 3 = 18.", calc="3*3*2"),
        ],
        "apply": [
            ex("Un cuerpo de 20 cubos tiene 2 filas iguales y 1 capa. ¿Cuántos cubos hay en cada fila?", "10", "20 ÷ 2 = 10.", calc="20//2"),
            ex("Un cuerpo de 24 cubos tiene 2 capas y 3 filas. ¿Cuántos cubos hay en cada fila?", "4", "24 ÷ 2 ÷ 3 = 4.", calc="24//2//3"),
            ex("Un cuerpo de 30 cubos tiene 5 filas de 3 cubos. ¿Cuántas capas tiene?", "2", "5 × 3 = 15 y 30 ÷ 15 = 2.", calc="30//(5*3)"),
        ],
        "reason": [
            ex("Luis armó un cuerpo de 3 filas de 3 cubos con 2 capas y otro con 2 filas de 9 cubos en 1 capa. ¿Tienen el mismo volumen?", "Sí, 18 cubos cada uno", "3 × 3 × 2 = 18 y 2 × 9 × 1 = 18.", calc="3*3*2"),
            ex("Pía dice que un cuerpo de 4 filas de 3 en 2 capas es más grande que uno de 3 filas de 4 en 2 capas. ¿Tiene razón?", "No; ambos tienen 24 cubos", "4 × 3 × 2 = 3 × 4 × 2 = 24.", calc="4*3*2"),
        ],
        "challenge": [
            ex("Un cuerpo de 36 cubos tiene 3 capas y 3 filas. ¿Cuántos cubos hay por fila?", "4", "36 ÷ 3 ÷ 3 = 4.", calc="36//3//3"),
            ex("Dos cuerpos: uno de 2 × 2 × 5 y otro de 4 × 1 × 5. ¿Tienen el mismo volumen?", "Sí, 20 cubos cada uno", "2 × 2 × 5 = 4 × 1 × 5 = 20.", calc="2*2*5"),
        ],
    },
    context=[ex("Un juguetero guarda 24 cubos en una caja. Cada capa tiene 2 filas de 4 cubos. ¿Cuántas capas necesita?", "3", "Cada capa tiene 8 cubos y 24 ÷ 8 = 3.", calc="24//(2*4)")],
    selfcheck=[
        ex("¿Qué volumen tiene un cuerpo de 2 filas de 5 cubos en 3 capas?", "30 unidades cúbicas", "2 × 5 × 3 = 30.", calc="2*5*3"),
        ex("Un cuerpo de 1 capa tiene 30 cubos en 5 filas iguales. ¿Cuántos cubos hay por fila?", "6", "30 ÷ 5 = 6.", calc="30//5"),
        ex("¿La forma de un cuerpo cambia su volumen si los cubos son los mismos?", "No", "El volumen es la cantidad de cubos iguales."),
    ],
    open_task=task(
        "Elige un volumen de la lista: 12, 16 o 18 unidades cúbicas. Diseña tres cuerpos distintos con ese volumen. Escribe las filas, los cubos por fila, las capas y el producto de cada uno. Si tienes un programa de geometría con cubos, puedes armarlos allí.",
        "Volumen 16: 4 × 4 × 1, 2 × 4 × 2 y 1 × 8 × 2; todos dan 16.",
        ["elige un volumen de la lista", "diseña tres cuerpos distintos", "escribe filas, cubos por fila y capas", "comprueba que cada producto dé el volumen elegido"],
        ["tres diseños", "tres productos"],
        ["repetir el mismo cuerpo girado", "no comprobar el producto"],
        "Pide explicar por qué las formas son distintas pero el volumen es igual. Reconoce que compruebe cada producto.",
    ),
    reinforce="Con cubos de juego, arma dos cuerpos distintos con 12 cubos cada uno. Compara sus formas.",
    extend="Busca tres cuerpos con formas distintas que puedas armar con 8 cubos y escribe las filas, cubos por fila y capas de cada uno.",
)
