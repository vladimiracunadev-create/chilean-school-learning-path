"""Student material for 4.º básico Matemática, OA 12 (adición y sustracción de decimales) y OA 13 (patrones numéricos en tablas)."""
from __future__ import annotations

import re
from decimal import Decimal

from student_lessons import arith, ex, register

OA12, OA13 = "MA04 OA 12", "MA04 OA 13"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _show(value: Decimal) -> str:
    text = format(value.normalize(), "f")
    return text.replace(".", ",")


def dec(q: str, expr: str, why: str, unit: str = "") -> dict:
    """Closed exercise whose answer is a decimal computed exactly with Decimal arithmetic."""
    value = eval(re.sub(r"\d+(?:\.\d+)?", lambda m: f"Decimal('{m.group()}')", expr), {"Decimal": Decimal})
    shown = " ".join(expr.replace("*", " × ").replace("-", " − ").replace("+", " + ").replace(".", ",").split())
    return ex(q, f"{_show(value)}{unit}", f"{why} Cálculo: {shown} = {_show(value)}.")


TABLA = "Tabla de valor posicional: U (unidades), d (décimos) y c (centésimos), con la coma entre U y d."

# ================================================================ OA 12
register(
    OA12, 1,
    materials=f"Lápiz y papel cuadriculado. {TABLA}",
    use="Aprenderé a escribir decimales en una tabla de valor posicional antes de sumar o restar. Sirve para no mezclar décimos con centésimos.",
    prior=["Sé leer décimos y centésimos.", "Sé sumar y restar números naturales."],
    explain=[
        "El valor posicional dice cuánto vale cada dígito según su lugar. Para decimales usamos tres columnas: unidades (U), décimos (d) y centésimos (c). La coma separa U de d.",
        "El número 2,35 se escribe con U = 2, d = 3 y c = 5. Para sumar o restar, escribe los números uno bajo el otro con las comas alineadas. Así, décimos quedan con décimos y centésimos con centésimos.",
        "Si un número tiene menos cifras, completa con ceros que no cambian su valor. Por ejemplo, 0,5 se escribe 0,50 para compararlo con 0,25. Diez centésimos forman un décimo, y diez décimos forman una unidad.",
    ],
    vocab=[("valor posicional", "lo que vale un dígito según el lugar en que está"), ("décimo", "una de 10 partes iguales de un entero"), ("centésimo", "una de 100 partes iguales de un entero"), ("alinear", "poner los números de modo que las comas queden en una misma línea"), ("canje", "cambiar 10 de una posición por 1 de la posición siguiente")],
    worked=[
        {"title": "Escribir en la tabla", "problem": "Escribe 2,35 en la tabla de valor posicional.", "steps": ["Antes de la coma está el 2: U = 2.", "Después de la coma están el 3 y el 5: d = 3 y c = 5."], "answer": "U = 2, d = 3, c = 5"},
        {"title": "Sumar con la tabla", "problem": "Suma 0,4 + 0,3 usando la tabla.", "steps": ["Pongo 0,4 como U = 0, d = 4 y 0,3 como U = 0, d = 3.", "Sumo los décimos: 4 + 3 = 7.", "El resultado es 0 unidades y 7 décimos."], "answer": "0,7"},
    ],
    mistakes=[
        {"wrong": "Sumar 0,5 + 0,25 como 5 + 25 y escribir 0,30.", "why": "Se alinean los últimos dígitos y no los lugares.", "fix": "Escribe 0,50 + 0,25. Alineadas las comas, el resultado es 0,75."},
        {"wrong": "Poner el 7 de 0,67 en la columna de los décimos.", "why": "Se leen los dígitos sin mirar su lugar.", "fix": "En 0,67 el 6 es d y el 7 es c: 6 décimos y 7 centésimos."},
    ],
    tiers={
        "recovery": [
            ex("En la tabla U, d, c, ¿qué dígito va en cada lugar al escribir 2,35?", "U = 2, d = 3, c = 5", "El 2 está antes de la coma y los otros dos están después."),
            ex("¿Cuántos centésimos hay en 3 décimos?", "30", "Cada décimo son 10 centésimos y 3 × 10 = 30."),
            ex("Escribe el decimal que tiene 1 en U, 4 en d y 6 en c.", "1,46", "Se escribe U, coma, d y c."),
        ],
        "understand": [
            ex("Al sumar decimales en una tabla, ¿qué debe quedar una bajo la otra?", "Las comas y los lugares iguales", "Así se suman décimos con décimos y centésimos con centésimos."),
            ex("¿Por qué conviene escribir 0,5 como 0,50 para sumarlo con 0,25?", "Para que los dos tengan centésimos", "0,5 son 5 décimos y 50 centésimos."),
            ex("¿Cuántos décimos hay en 1,4?", "14", "Un entero son 10 décimos y se suman 4 más."),
        ],
        "apply": [
            dec("Con la tabla, calcula 0,4 + 0,3.", "0.4+0.3", "Se suman 4 décimos y 3 décimos."),
            dec("Calcula la resta 0,8 − 0,3 usando décimos.", "0.8-0.3", "Se restan 3 décimos a 8 décimos."),
            dec("Escribe 0,25 y 0,10 en la tabla y súmalos.", "0.25+0.1", "Se suman décimos con décimos y centésimos con centésimos."),
        ],
        "reason": [
            ex("Pedro suma 0,5 + 0,25 y obtiene 0,30 porque 5 + 25 = 30. ¿Cuál es su error y cuál es el resultado correcto?", "No alineó los lugares; el resultado es 0,75", "5 décimos son 50 centésimos y 50 + 25 = 75."),
            ex("Lucía, al sumar 0,6 + 0,07, pone el 7 en los décimos. ¿Está bien? ¿Cuál es el resultado?", "No; el 7 va en centésimos y el resultado es 0,67", "0,07 son 7 centésimos."),
        ],
        "challenge": [
            ex("Un decimal tiene 2 en U, 0 en d y 9 en c. Si le sumas 0,01, ¿qué decimal queda?", "2,10", "9 + 1 = 10 centésimos forman 1 décimo."),
            dec("¿Qué número hay que sumar a 0,45 para llegar a 0,5?", "0.5-0.45", "La diferencia con 0,50 es lo que falta."),
        ],
    },
    context=[dec("Una cinta mide 0,4 m y otra mide 0,35 m. ¿Cuántos metros miden juntas?", "0.4+0.35", "Se suman 40 centésimos y 35 centésimos.", " m")],
    selfcheck=[
        dec("Calcula 0,3 + 0,6.", "0.3+0.6", "Se suman 3 décimos y 6 décimos."),
        ex("¿Cuántos centésimos son 0,2?", "20", "Dos décimos son 20 centésimos."),
        dec("Calcula 0,07 + 0,02.", "0.07+0.02", "Se suman 7 y 2 centésimos."),
    ],
    open_task=task(
        "Elige una suma y resuélvela en una tabla de U, d y c. Opción A: 0,35 + 0,40. Opción B: 0,6 + 0,18. Escribe cómo alineaste y qué hiciste con el cero faltante.",
        "Opción B: escribí 0,60 + 0,18. Los centésimos: 0 + 8 = 8; los décimos: 6 + 1 = 7. Resultado: 0,78.",
        ["alinea las comas", "completa con cero cuando falta", "suma bien cada columna", "escribe el resultado con coma"],
        ["tabla", "resultado"],
        ["alinear por el último dígito", "no completar con ceros"],
        "Pide que lea cada columna en voz alta (décimos, centésimos). Reconoce completar con ceros como valor posicional.",
    ),
    reinforce="Dibuja una tabla U, d, c y escribe en ella tres números como 1,23; 0,5 y 2,07. Léelos con palabras.",
    extend="Escribe dos decimales cuya suma sea 1 y muéstralos en la tabla.",
)

register(
    OA12, 2,
    materials=f"Lápiz y papel cuadriculado. {TABLA}",
    use="Aprenderé a sumar decimales hasta los centésimos con canje. Sirve para sumar medidas, pesos y tiempos.",
    prior=["Sé escribir decimales en una tabla posicional.", "Sé que 10 centésimos forman 1 décimo."],
    explain=[
        "Para sumar decimales, alinea las comas y suma desde la derecha, como con los números naturales. Primero los centésimos, luego los décimos y al final las unidades. Escribe la coma en el resultado debajo de las otras.",
        "Si una columna suma 10 o más, haces un canje. Por ejemplo, en 0,48 + 0,27: 8 + 7 = 15 centésimos. Quedan 5 centésimos y 10 centésimos pasan a ser 1 décimo. Luego 4 + 2 + 1 = 7 décimos. El resultado es 0,75.",
        "Si un número tiene menos cifras, completa con ceros: 1,25 + 0,8 se calcula como 1,25 + 0,80 = 2,05. Antes de dar la respuesta, mira si el resultado es mayor que cada sumando. En una suma siempre lo es.",
    ],
    vocab=[("sumando", "cada número que se suma"), ("suma o total", "resultado de una adición"), ("canje", "cambiar 10 de una posición por 1 de la posición de la izquierda"), ("alinear las comas", "escribir los números con las comas una bajo otra"), ("cero de relleno", "cero que se escribe sin cambiar el valor")],
    worked=[
        {"title": "Suma con canje", "problem": "Calcula 0,48 + 0,27.", "steps": ["Centésimos: 8 + 7 = 15. Escribo 5 y canjeo 10 centésimos por 1 décimo.", "Décimos: 4 + 2 + 1 = 7.", "Unidades: 0. Resultado: 0,75."], "answer": "0,75"},
        {"title": "Completar con cero", "problem": "Calcula 1,25 + 0,8.", "steps": ["Escribo 0,8 como 0,80 para alinear.", "Centésimos: 5 + 0 = 5. Décimos: 2 + 8 = 10 → escribo 0 y canjeo por 1 unidad.", "Unidades: 1 + 0 + 1 = 2. Resultado: 2,05."], "answer": "2,05"},
    ],
    mistakes=[
        {"wrong": "Sumar 0,7 + 0,5 y escribir 0,12.", "why": "Se suman los dígitos 7 + 5 sin pensar que son 12 décimos.", "fix": "12 décimos son 1 entero y 2 décimos: 1,2."},
        {"wrong": "Sumar 1,25 + 0,8 como 1,25 + 8 y escribir 1,33.", "why": "No se alinean los lugares: 8 décimos no es 8 centésimos.", "fix": "Escribe 0,80. Entonces 1,25 + 0,80 = 2,05."},
    ],
    tiers={
        "recovery": [
            dec("Calcula 0,6 + 0,2.", "0.6+0.2", "Se suman 6 y 2 décimos."),
            dec("Calcula 0,35 + 0,24.", "0.35+0.24", "Se suman centésimos con centésimos y décimos con décimos."),
            ex("Al sumar 0,5 + 0,5, ¿cuántos décimos hay en total y cuántos enteros forman?", "10 décimos; forman 1 entero", "Diez décimos se canjean por una unidad."),
        ],
        "understand": [
            ex("Cuando 10 centésimos se juntan, ¿qué se forma?", "1 décimo", "Diez centésimos es un décimo."),
            ex("Escribe 2,4 con centésimos para sumarlo con 1,25.", "2,40", "Así los dos números tienen dos decimales."),
            ex("En 0,48 + 0,27, ¿cuánto suman los centésimos de ambos números (8 + 7)?", "15", "15 centésimos forman 1 décimo y 5 centésimos."),
        ],
        "apply": [
            dec("Calcula 0,48 + 0,27.", "0.48+0.27", "Los 15 centésimos se canjean: 5 centésimos y 1 décimo."),
            dec("Calcula 1,25 + 0,8.", "1.25+0.8", "0,8 se escribe 0,80 para alinear."),
            dec("Calcula 3,6 + 1,75.", "3.6+1.75", "3,6 se escribe 3,60 para sumar centésimos."),
        ],
        "reason": [
            ex("Sara suma 0,7 + 0,5 y obtiene 0,12 porque 7 + 5 = 12. ¿Cuál es su error y el resultado correcto?", "12 son décimos y forman 1,2", "Doce décimos son 1 entero y 2 décimos."),
            ex("Tomás suma 1,25 + 0,8 y obtiene 1,33 porque 25 + 8 = 33. ¿Cuál es el resultado correcto?", "2,05", "0,8 son 80 centésimos y 125 + 80 = 205 centésimos."),
        ],
        "challenge": [
            dec("¿Qué número sumado a 0,75 da 1,2?", "1.2-0.75", "Lo que falta es la diferencia entre 1,20 y 0,75."),
            dec("Calcula la suma de tres números: 0,25 + 0,5 + 0,75.", "0.25+0.5+0.75", "Se suman uno a uno con las comas alineadas."),
        ],
    },
    context=[dec("Compras 1,5 kg de manzanas y 0,75 kg de peras. ¿Cuántos kilogramos compraste en total?", "1.5+0.75", "1,5 se escribe 1,50 y se suma con 0,75.", " kg")],
    selfcheck=[
        dec("Calcula 0,9 + 0,3.", "0.9+0.3", "Doce décimos son 1,2."),
        dec("Calcula 2,05 + 0,95.", "2.05+0.95", "5 + 5 = 10 centésimos canjean 1 décimo, y 0 + 9 + 1 = 10 décimos canjean 1 unidad."),
        ex("En 3,46 + 2,2, ¿cómo se escribe 2,2 para alinear los lugares?", "2,20", "Se agrega un cero de relleno en los centésimos."),
    ],
    open_task=task(
        "Resuelve una suma con canje, escrita en columnas con las comas alineadas. Opción A: 0,56 + 0,38. Opción B: 1,7 + 0,65. Muestra dónde hiciste el canje.",
        "Opción A: centésimos 6 + 8 = 14 (queda 4, canjeo 1 décimo). Décimos 5 + 3 + 1 = 9. Resultado: 0,94.",
        ["alinea las comas", "hace el canje cuando corresponde", "escribe el resultado con coma"],
        ["suma en columnas", "marca del canje"],
        ["sumar 8 décimos con 8 centésimos", "olvidar el canje"],
        "Pide que explique de dónde sale el dígito que \"se lleva\". Reconoce el canje como 10 de una posición por 1 de la siguiente.",
    ),
    reinforce="Con dos medidas decimales de objetos de tu casa (por ejemplo, 0,45 m y 0,38 m), calcula cuántos metros miden juntos.",
    extend="Inventa una suma de dos decimales con canje en los centésimos y otra con canje en los décimos. Resuélvelas.",
)

register(
    OA12, 3,
    materials=f"Lápiz y papel cuadriculado. {TABLA}",
    use="Aprenderé a restar decimales hasta los centésimos con canje. Sirve para saber cuánto queda o cuánto falta.",
    prior=["Sé sumar decimales con canje.", "Sé restar números naturales con canje."],
    explain=[
        "Para restar decimales, alinea las comas y resta desde la derecha. Si el dígito de arriba es menor que el de abajo, haces un canje: 1 décimo se cambia por 10 centésimos, o 1 unidad por 10 décimos.",
        "Por ejemplo, 0,52 − 0,27: no se pueden quitar 7 centésimos de 2. Canjeas 1 décimo por 10 centésimos: quedan 4 décimos y 12 centésimos. Ahora 12 − 7 = 5 y 4 − 2 = 2. El resultado es 0,25.",
        "Para restar 1 − 0,35, escribe 1 como 1,00. Es 10 décimos y 0 centésimos, o 100 centésimos. Entonces 100 − 35 = 65 centésimos: 0,65. Puedes comprobar sumando: 0,65 + 0,35 = 1.",
    ],
    vocab=[("minuendo", "el número del que se quita"), ("sustraendo", "el número que se quita"), ("diferencia", "resultado de una resta"), ("canje", "cambiar 1 de una posición por 10 de la posición siguiente a la derecha"), ("comprobar", "revisar con la operación contraria")],
    worked=[
        {"title": "Resta con canje", "problem": "Calcula 0,52 − 0,27.", "steps": ["Centésimos: 2 − 7 no se puede. Canjeo 1 décimo por 10 centésimos: queda 4 décimos y 12 centésimos.", "12 − 7 = 5 centésimos y 4 − 2 = 2 décimos.", "Resultado: 0,25. Compruebo: 0,25 + 0,27 = 0,52."], "answer": "0,25"},
        {"title": "Restar a un entero", "problem": "Calcula 1 − 0,35.", "steps": ["Escribo 1 como 1,00 y lo veo como 100 centésimos.", "100 − 35 = 65 centésimos.", "Compruebo: 0,65 + 0,35 = 1,00."], "answer": "0,65"},
    ],
    mistakes=[
        {"wrong": "Restar 0,52 − 0,27 y obtener 0,35 porque 5 − 2 = 3 y 7 − 2 = 5 (resta el menor al mayor en cada columna).", "why": "No se hace el canje; se invierte la resta de una columna.", "fix": "Canjea 1 décimo por 10 centésimos: 12 − 7 = 5 y 4 − 2 = 2. Resultado: 0,25."},
        {"wrong": "Restar 3 − 1,25 como 3 − 1 = 2 y 0 − 25.", "why": "No se escribe el 3 con ceros para alinear.", "fix": "Escribe 3,00 − 1,25 = 1,75."},
    ],
    tiers={
        "recovery": [
            dec("Calcula 0,9 − 0,4.", "0.9-0.4", "Se restan 4 décimos a 9 décimos."),
            dec("Calcula 0,75 − 0,25.", "0.75-0.25", "Se restan centésimos con centésimos y décimos con décimos."),
            dec("Calcula 1 − 0,4 sabiendo que 1 son 10 décimos.", "1-0.4", "10 décimos menos 4 décimos son 6 décimos."),
        ],
        "understand": [
            ex("Para restar 0,52 − 0,27, ¿se pueden quitar 7 centésimos de 2 centésimos? ¿Qué se hace?", "No; se canjea 1 décimo por 10 centésimos", "Así quedan 12 centésimos para restar."),
            ex("¿Cuántos centésimos hay en 1 entero?", "100", "Un entero tiene 10 décimos y cada décimo son 10 centésimos."),
            ex("Escribe 1 como decimal con centésimos para restarle 0,35.", "1,00", "Así se alinean décimos y centésimos."),
        ],
        "apply": [
            dec("Calcula 1 − 0,35.", "1-0.35", "1 son 100 centésimos y 100 − 35 = 65."),
            dec("Calcula 2,4 − 0,75.", "2.4-0.75", "2,4 se escribe 2,40 y se canjea en las dos posiciones."),
            dec("Calcula 0,52 − 0,27.", "0.52-0.27", "Se canjea 1 décimo por 10 centésimos."),
        ],
        "reason": [
            ex("Pía calculó 0,52 − 0,27 = 0,35 porque en cada columna restó el menor al mayor. ¿Cuál es el resultado correcto y cómo lo comprobarías?", "0,25; se comprueba con 0,25 + 0,27 = 0,52", "La suma del resultado con el sustraendo debe dar el minuendo."),
            ex("Juan dice que 1 − 0,35 = 0,65 porque 0,65 + 0,35 = 1. ¿Es correcta su comprobación?", "Sí", "La suma inversa de la resta recupera el número inicial."),
        ],
        "challenge": [
            dec("Un número menos 0,38 es igual a 0,41. ¿Cuál es el número?", "0.41+0.38", "Se suma el resultado con el número restado."),
            dec("Calcula 3 − 1,25.", "3-1.25", "3 se escribe 3,00 para restar con centésimos."),
        ],
    },
    context=[dec("Tienes una cuerda de 2 m y cortas 0,75 m. ¿Cuántos metros de cuerda quedan?", "2-0.75", "2 son 2,00 y se resta con canje.", " m")],
    selfcheck=[
        dec("Calcula 0,8 − 0,35.", "0.8-0.35", "0,8 se escribe 0,80 para restar."),
        dec("Calcula 1,5 − 0,6.", "1.5-0.6", "15 décimos menos 6 décimos son 9 décimos."),
        ex("Si 0,63 + 0,27 = 0,90, ¿cuánto es 0,90 − 0,27?", "0,63", "La resta deshace la suma."),
    ],
    open_task=task(
        "Resuelve una resta con canje y compruébala con una suma. Opción A: 0,71 − 0,36. Opción B: 1 − 0,48. Escribe las dos operaciones.",
        "Opción A: 0,71 − 0,36 = 0,35 (canjeo 1 décimo por 10 centésimos). Comprobación: 0,35 + 0,36 = 0,71.",
        ["alinea las comas", "hace el canje cuando corresponde", "comprueba con una suma"],
        ["resta en columnas", "comprobación"],
        ["restar el menor al mayor en cada columna", "no escribir 1 como 1,00"],
        "Pide que muestre dónde canjeó. Reconoce la comprobación con la operación inversa.",
    ),
    reinforce="Elige un número decimal de 2 cifras y réstalo de 1. Comprueba sumando el resultado con el número que restaste.",
    extend="Inventa una resta de decimales que necesite canje en décimos y en centésimos a la vez, y resuélvela.",
)

register(
    OA12, 4,
    materials=f"Lápiz y papel cuadriculado. {TABLA}",
    use="Aprenderé a resolver problemas con sumas y restas de decimales y a estimar el resultado antes de calcular. Sirve para ver si una respuesta tiene sentido.",
    prior=["Sé sumar y restar decimales con canje.", "Sé qué significan «total» y «cuánto más»."],
    explain=[
        "En un problema, primero decide qué operación necesitas. Si juntas cantidades, sumas. Si quitas, o comparas «cuánto más» o «cuánto falta», restas. Luego alinea las comas y calcula.",
        "Antes de calcular exactamente, estima con números cercanos fáciles. Por ejemplo, 2,9 + 4,1 se parece a 3 + 4, que es 7. Si tu cálculo da un valor muy diferente, revísalo. La estimación no es la respuesta final, solo ayuda a detectar errores.",
        "Escribe la respuesta con su unidad: metros, litros, kilogramos o segundos. Comprueba con la operación contraria. Por ejemplo, si 3,5 − 1,25 = 2,25, entonces 2,25 + 1,25 debe dar 3,5.",
    ],
    vocab=[("estimar", "calcular una respuesta aproximada con números fáciles"), ("unidad de medida", "lo que se mide: m, kg, L, s"), ("comparar", "ver cuánto más o cuánto menos es una cantidad que otra"), ("razonable", "que tiene sentido con lo que se espera"), ("operación inversa", "operación que deshace a otra")],
    worked=[
        {"title": "Estimar y calcular", "problem": "Una botella tiene 2,9 L y otra tiene 4,1 L. ¿Cuántos litros hay? Estima y calcula.", "steps": ["Estimo: 2,9 es casi 3 y 4,1 es casi 4; la suma es cerca de 7.", "Calculo: 2,90 + 4,10 = 7,00.", "El resultado se parece a la estimación."], "answer": "7 L"},
        {"title": "Comparar con resta", "problem": "Ana mide 1,35 m y su hermano 1,08 m. ¿Cuánto más alta es Ana?", "steps": ["«Cuánto más» se resuelve con una resta.", "1,35 − 1,08 = 0,27.", "Compruebo: 0,27 + 1,08 = 1,35."], "answer": "0,27 m"},
    ],
    mistakes=[
        {"wrong": "Estimar 4,9 + 5,2 ≈ 15.", "why": "Se suman mal los números fáciles.", "fix": "4,9 es casi 5 y 5,2 es casi 5: la suma es cerca de 10."},
        {"wrong": "Calcular 3,5 − 1,25 = 2,35.", "why": "No se alinea 3,5 como 3,50.", "fix": "3,50 − 1,25 = 2,25. Se comprueba: 2,25 + 1,25 = 3,50."},
    ],
    tiers={
        "recovery": [
            ex("Sin calcular exacto, la suma 2,9 + 4,1, ¿se acerca más a 7 o a 9?", "A 7", "Es casi 3 + 4."),
            dec("Una botella tiene 1,5 L y otra tiene 0,75 L. ¿Cuántos litros hay en total?", "1.5+0.75", "1,5 se escribe 1,50 para sumar.", " L"),
            dec("Una cuerda de 3 m se usa en 1,2 m. ¿Cuántos metros quedan?", "3-1.2", "3 se escribe 3,0 para restar.", " m"),
        ],
        "understand": [
            ex("Para saber cuánto más alto es 1,45 m que 1,32 m, ¿qué operación haces?", "Una resta", "«Cuánto más» compara y se resuelve restando."),
            ex("¿Cuál es una buena estimación de 7,8 − 2,1: cerca de 6 o cerca de 10?", "Cerca de 6", "7,8 es casi 8 y 2,1 es casi 2; 8 − 2 = 6."),
            ex("Antes de sumar 4,5 + 0,75, ¿qué debes hacer con las comas?", "Alinearlas una bajo la otra", "Así se suman décimos con décimos."),
        ],
        "apply": [
            dec("Ana mide 1,35 m y su hermano 1,08 m. ¿Cuántos metros más alta es Ana?", "1.35-1.08", "Se compara restando las alturas.", " m"),
            dec("Tres tramos de una ruta miden 1,5 km, 2,25 km y 0,5 km. ¿Cuántos kilómetros son en total?", "1.5+2.25+0.5", "Se alinean las comas y se suman los tres.", " km"),
            dec("Una receta pide 0,75 kg de harina y ya tienes 0,5 kg. ¿Cuántos kilogramos te faltan?", "0.75-0.5", "Falta la diferencia entre lo pedido y lo que hay.", " kg"),
        ],
        "reason": [
            ex("Luis estimó 4,9 + 5,2 ≈ 15. ¿Es razonable su estimación?", "No; debería estar cerca de 10", "4,9 es casi 5 y 5,2 es casi 5."),
            ex("Rosa calculó 3,5 − 1,25 = 2,35. Compruébalo con una suma. ¿Está bien?", "No; 2,35 + 1,25 = 3,6, el resultado es 2,25", "La suma del resultado y 1,25 debe dar 3,5."),
        ],
        "challenge": [
            dec("Dos números suman 5 y uno de ellos es 2,35. ¿Cuál es el otro?", "5-2.35", "El otro es 5 menos el conocido."),
            dec("Un estanque tiene 8,5 L. Se sacan 2,75 L y luego se agregan 1,5 L. ¿Cuántos litros hay al final?", "8.5-2.75+1.5", "Se resta primero y luego se suma.", " L"),
        ],
    },
    context=[dec("Dos nadadores marcaron 31,4 s y 30,85 s. ¿Cuántos segundos de diferencia hay?", "31.4-30.85", "31,4 se escribe 31,40 para restar.", " s")],
    selfcheck=[
        ex("Estima: 6,1 + 3,9, ¿se parece a 10 o a 7?", "A 10", "6,1 es casi 6 y 3,9 es casi 4."),
        dec("Calcula 12,5 − 4,25.", "12.5-4.25", "12,5 se escribe 12,50 para restar con canje."),
        dec("Calcula 0,36 + 0,64.", "0.36+0.64", "36 + 64 = 100 centésimos, o sea 1."),
    ],
    open_task=task(
        "Elige un problema. A) Una cinta de 2,5 m se corta en un trozo de 1,35 m: ¿cuántos metros quedan? B) Dos paquetes pesan 1,75 kg y 2,6 kg: ¿cuántos kilogramos pesan juntos? Estima primero, calcula y compara con tu estimación.",
        "B) Estimo: 1,75 es casi 2 y 2,6 es casi 3: cerca de 5. Calculo: 1,75 + 2,60 = 4,35 kg. 4,35 está entre 4 y 5, cerca de mi estimación, así que es razonable.",
        ["escribe una estimación", "elige la operación correcta", "calcula con las comas alineadas", "responde con unidad"],
        ["estimación", "cálculo", "respuesta con unidad"],
        ["no alinear las comas", "no escribir la unidad"],
        "Pide que compare su estimación con el resultado. Reconoce revisar si el resultado es razonable.",
    ),
    reinforce="Mide dos objetos con una regla en metros o centímetros y calcula su suma y su diferencia usando decimales.",
    extend="Escribe un problema de dos pasos con decimales (por ejemplo, sumar y luego restar) y resuélvelo con estimación.",
)

# ================================================================ OA 13
register(
    OA13, 1,
    materials="Lápiz y papel.",
    use="Aprenderé a detectar cuánto cambia un patrón numérico de un paso a otro. Sirve para continuar listas de números y tablas.",
    prior=["Sé sumar y restar números hasta 1.000.", "Sé multiplicar con las tablas hasta el 10."],
    explain=[
        "Un patrón numérico es una lista de números que sigue una regla. En un patrón con cambio constante, de un número al siguiente se suma o se resta siempre la misma cantidad. Por ejemplo, 5, 8, 11, 14 aumenta de 3 en 3.",
        "Para descubrir la regla, resta cada número al siguiente. Si siempre da lo mismo, el cambio es constante. En 30, 27, 24, 21, cada resta da −3: el patrón baja de a 3.",
        "En una tabla, los números de una columna cambian de manera constante cuando la otra columna cambia de 1 en 1. Por ejemplo: 1 caja tiene 6 lápices, 2 cajas tienen 12, 3 cajas tienen 18. Por cada caja nueva, los lápices aumentan en 6.",
    ],
    vocab=[("patrón", "lista de números que sigue una regla"), ("cambio constante", "que siempre se suma o se resta la misma cantidad"), ("aumentar", "hacerse mayor"), ("disminuir", "hacerse menor"), ("término", "cada número de un patrón")],
    worked=[
        {"title": "Cambio en una lista", "problem": "En el patrón 5, 8, 11, 14, ¿cuánto cambia cada vez y cuál es el siguiente?", "steps": ["8 − 5 = 3, 11 − 8 = 3 y 14 − 11 = 3.", "El cambio es +3 siempre.", "El siguiente es 14 + 3 = 17."], "answer": "Aumenta 3; el siguiente es 17"},
        {"title": "Cambio en una tabla", "problem": "Cajas: 1, 2, 3, 4. Lápices: 6, 12, 18, 24. ¿Cuánto cambia el número de lápices al agregar una caja?", "steps": ["12 − 6 = 6, 18 − 12 = 6 y 24 − 18 = 6.", "Cada caja nueva agrega 6 lápices."], "answer": "Aumenta 6"},
    ],
    mistakes=[
        {"wrong": "Decir que 3, 6, 10, 15 aumenta siempre de a 3 porque el primer paso es 3.", "why": "Se mira solo el primer cambio.", "fix": "Los cambios son 3, 4 y 5. No es constante."},
        {"wrong": "Decir que 50, 45, 40, 35 aumenta de a 5.", "why": "No se mira si los números suben o bajan.", "fix": "Los números bajan: el cambio es −5."},
    ],
    tiers={
        "recovery": [
            ex("En el patrón 5, 8, 11, 14, ¿cuánto aumenta cada vez?", "3", "Cada término es 3 más que el anterior."),
            ex("¿Cuál es el siguiente número del patrón 10, 20, 30, 40?", "50", "Cada término es 10 más que el anterior."),
            ex("El patrón 30, 27, 24, 21 ¿sube o baja? ¿Cuánto en cada paso?", "Baja de a 3", "Cada término es 3 menos que el anterior."),
        ],
        "understand": [
            ex("Cajas: 1, 2, 3, 4. Lápices: 6, 12, 18, 24. ¿Cuántos lápices más hay al agregar una caja?", "6", "La diferencia entre términos es siempre 6."),
            ex("¿Qué significa «cambio constante» en un patrón numérico?", "Que siempre se suma o se resta la misma cantidad", "Los cambios entre términos son iguales."),
            ex("¿La lista 2, 4, 7, 11 tiene cambio constante?", "No; cambia 2, 3 y 4", "Los aumentos no son iguales."),
        ],
        "apply": [
            ex("Completa el patrón 100, 90, 80, __, 60.", "70", "Cada término baja 10."),
            arith("Mesas: 1, 2, 3. Sillas: 4, 8, 12. Si el patrón sigue, ¿cuántas sillas hay con 6 mesas?", "4*6", "Cada mesa agrega 4 sillas."),
            ex("¿Cuál es el siguiente número de 6, 12, 18, 24?", "30", "Cada término suma 6."),
        ],
        "reason": [
            ex("Pedro dice que 3, 6, 10, 15 aumenta de a 3 porque 6 − 3 = 3. ¿Tiene razón?", "No; aumenta 3, 4 y 5", "Un cambio constante debe ser igual en todos los pasos."),
            ex("Ana dice que en 50, 45, 40, 35 el cambio es +5. ¿Es correcto?", "No; es −5", "Los números bajan."),
        ],
        "challenge": [
            ex("Un patrón empieza en 7 y aumenta de a 4. ¿Cuál es el quinto número?", "23", "7, 11, 15, 19 y 23."),
            arith("Un patrón empieza en 12 y aumenta de a 5. ¿Cuál es el término del paso 6? (Al paso 1 le sumas 5 cinco veces.)", "12+5*5", "Desde el paso 1 hay 5 aumentos hasta el paso 6."),
        ],
    },
    context=[arith("Tienes $500 en una alcancía y cada semana agregas $200. ¿Cuánto dinero tendrás después de 4 semanas?", "500+200*4", "Cada semana suma el mismo monto.")],
    selfcheck=[
        ex("¿Cuánto cambia en cada paso el patrón 9, 14, 19, 24?", "Aumenta 5", "Cada término es 5 más."),
        ex("¿Cuál es el siguiente número de 40, 36, 32, 28?", "24", "Cada término baja 4."),
        ex("¿La tabla 1 → 3, 2 → 6, 3 → 9 tiene cambio constante en la segunda columna? Responde sí o no.", "Sí", "Sube 3 cada vez."),
    ],
    open_task=task(
        "Elige una de estas listas. A) 4, 9, 14, 19, 24. B) 100, 92, 84, 76, 68. Escribe la regla de cambio, calcula los tres términos siguientes y explica cómo supiste que el cambio es constante.",
        "Lista B: baja 8 cada vez. Siguientes: 60, 52 y 44. Restamos cada par vecino y siempre daba 8.",
        ["indica el cambio", "calcula tres términos siguientes", "comprueba que el cambio es igual en cada par"],
        ["regla", "términos nuevos", "comprobación"],
        ["fijarse solo en el primer cambio", "confundir subir con bajar"],
        "Pide que muestre las restas de los pares vecinos. Reconoce la verificación de todos los pasos.",
    ),
    reinforce="Con monedas o fichas, arma un patrón que aumente de a 2 y otro que aumente de a 5. Escribe los primeros seis términos.",
    extend="Crea un patrón con cambio constante de a 7 y otro con cambio constante de −6. Escribe seis términos de cada uno.",
)

register(
    OA13, 2,
    materials="Lápiz y papel.",
    use="Aprenderé a describir con una operación la regla de una tabla de entrada y salida. Sirve para predecir resultados sin escribirlos todos.",
    prior=["Sé encontrar el cambio constante de una lista.", "Sé las tablas de multiplicar y sus divisiones."],
    explain=[
        "Una tabla de entrada y salida tiene números que entran y números que salen. La regla es la operación que transforma cada entrada en su salida. Puede ser sumar, restar, multiplicar o dividir por un número.",
        "Para descubrir la regla, mira una pareja y prueba una operación. Si la entrada 2 da la salida 6, podría ser sumar 4 o multiplicar por 3. Luego prueba la otra pareja: con entrada 3 la salida es 9. Sumar 4 da 7, y multiplicar por 3 da 9. La regla es multiplicar por 3.",
        "Una regla sirve solo si funciona con todas las parejas de la tabla. Si falla en una, debes probar otra operación. Escribe la regla como «× 3», «+ 7», «− 2» o «÷ 2».",
    ],
    vocab=[("entrada", "número que se pone en la regla"), ("salida", "resultado que se obtiene con la regla"), ("regla", "operación que transforma cada entrada en su salida"), ("tabla", "cuadro con pares de números ordenados"), ("probar", "comprobar una regla con todas las parejas")],
    worked=[
        {"title": "Una regla de suma", "problem": "Entrada: 2, 3, 4. Salida: 9, 10, 11. ¿Cuál es la regla?", "steps": ["9 − 2 = 7, 10 − 3 = 7 y 11 − 4 = 7.", "La diferencia es siempre 7."], "answer": "Sumar 7"},
        {"title": "Probar dos reglas", "problem": "Entrada: 2, 3, 4. Salida: 6, 9, 12. ¿La regla es sumar 4 o multiplicar por 3?", "steps": ["Con sumar 4: 2 + 4 = 6 pero 3 + 4 = 7, no 9. Falla.", "Con × 3: 2 × 3 = 6, 3 × 3 = 9 y 4 × 3 = 12. Funciona."], "answer": "Multiplicar por 3"},
    ],
    mistakes=[
        {"wrong": "Elegir sumar 4 porque con entrada 2 sale 6, sin probar las otras parejas.", "why": "Se prueba solo la primera pareja.", "fix": "Prueba la regla con todas las parejas; con 3 da 7, no 9."},
        {"wrong": "Decir que la regla de 5 → 1, 10 → 2, 15 → 3 es «restar 4» porque 5 − 4 = 1.", "why": "No se comprueba con la segunda pareja.", "fix": "10 − 4 = 6, no 2. La regla es dividir por 5."},
    ],
    tiers={
        "recovery": [
            ex("Entrada: 2, 3, 4. Salida: 9, 10, 11. ¿Qué regla de una operación cumple la tabla?", "Sumar 7", "Cada salida es 7 más que su entrada."),
            ex("Entrada: 1, 2, 3. Salida: 4, 8, 12. ¿Cuál es la regla?", "Multiplicar por 4", "1 × 4 = 4, 2 × 4 = 8 y 3 × 4 = 12."),
            ex("Entrada: 10, 8, 6. Salida: 7, 5, 3. ¿Cuál es la regla?", "Restar 3", "Cada salida es 3 menos que su entrada."),
        ],
        "understand": [
            ex("¿Cómo se comprueba que una regla sirve para toda la tabla?", "Se prueba con todas las parejas de la tabla", "Una regla correcta funciona en cada pareja."),
            arith("La regla es «multiplicar por 3». Si la entrada es 5, ¿cuál es la salida?", "5*3", "Se multiplica la entrada por 3."),
            ex("La salida siempre es 4 más que la entrada. ¿Qué operación es la regla?", "Sumar 4", "Se agrega 4 a cada entrada."),
        ],
        "apply": [
            ex("Entrada: 3, 5, 7, 9. Salida: 6, 10, 14, 18. ¿Cuál es la regla?", "Multiplicar por 2", "3 × 2 = 6, 5 × 2 = 10, 7 × 2 = 14 y 9 × 2 = 18."),
            ex("Entrada: 20, 30, 40, 50. Salida: 14, 24, 34, 44. ¿Cuál es la regla?", "Restar 6", "Cada salida es 6 menos que su entrada."),
            ex("Entrada: 12, 16, 20. Salida: 3, 4, 5. ¿Cuál es la regla?", "Dividir por 4", "12 ÷ 4 = 3, 16 ÷ 4 = 4 y 20 ÷ 4 = 5."),
        ],
        "reason": [
            ex("Entrada: 2, 3, 4. Salida: 6, 9, 12. Dani dice que la regla es sumar 4 porque 2 + 4 = 6. ¿Tiene razón?", "No; la regla es multiplicar por 3", "Con 3, sumar 4 da 7 y no 9."),
            ex("Entrada: 5, 10, 15. Salida: 1, 2, 3. Eva dice que la regla es restar 4 porque 5 − 4 = 1. ¿Es correcto?", "No; es dividir por 5", "10 − 4 = 6, pero la salida es 2."),
        ],
        "challenge": [
            ex("La tabla Entrada: 1, 2, 3 → Salida: 3, 5, 7, ¿tiene una regla con una sola operación (sumar, restar, multiplicar o dividir un mismo número)?", "No", "Ni sumar un número (cambia 2 y 3) ni multiplicar uno (3 y 2,5) sirve en todas las parejas."),
            ex("La regla es «multiplicar por 6». ¿Qué entrada produce la salida 48?", "8", "6 × 8 = 48."),
        ],
    },
    context=[ex("Un panadero pone la misma cantidad de panes en cada bolsa. Bolsas: 2, 3, 5. Panes: 12, 18, 30. Escribe la regla.", "Multiplicar por 6", "12 ÷ 2 = 6, 18 ÷ 3 = 6 y 30 ÷ 5 = 6.")],
    selfcheck=[
        ex("Entrada: 4, 5, 6. Salida: 11, 12, 13. ¿Cuál es la regla?", "Sumar 7", "Cada salida es 7 más."),
        arith("Con la regla «restar 9», ¿cuál es la salida de la entrada 30?", "30-9", "Se resta 9 a la entrada."),
        ex("Entrada: 6, 8, 10. Salida: 3, 4, 5. ¿Cuál es la regla?", "Dividir por 2", "6 ÷ 2 = 3, 8 ÷ 2 = 4 y 10 ÷ 2 = 5."),
    ],
    open_task=task(
        "Elige una tabla y escribe su regla. A) Entrada 2, 4, 6 y salida 8, 10, 12. B) Entrada 1, 3, 5 y salida 5, 15, 25. Prueba la regla en todas las parejas y escribe cómo lo hiciste.",
        "B) La regla es multiplicar por 5: 1 × 5 = 5, 3 × 5 = 15 y 5 × 5 = 25.",
        ["identifica la operación", "la prueba en todas las parejas", "escribe la regla con símbolo"],
        ["regla", "pruebas por pareja"],
        ["probar la regla solo en la primera pareja", "confundir sumar con multiplicar"],
        "Pide que pruebe una segunda operación y la descarte. Reconoce la comprobación con todas las parejas.",
    ),
    reinforce="Crea una tabla de 4 parejas con la regla «× 3» y pide a una persona de tu casa que descubra la regla.",
    extend="Crea dos tablas distintas con la misma primera pareja (por ejemplo, 2 → 6). Escribe la regla de cada una.",
)

register(
    OA13, 3,
    materials="Lápiz y papel.",
    use="Aprenderé a predecir términos de un patrón y a comprobar la predicción con la tabla. Sirve para calcular valores lejanos sin escribir todos.",
    prior=["Sé encontrar la regla de una tabla.", "Sé usar la regla para calcular una salida."],
    explain=[
        "Cuando conoces la regla, puedes predecir una salida sin completar toda la tabla. Si la regla es «× 4» y la entrada es 9, la salida es 9 × 4 = 36. No necesitas escribir las salidas anteriores.",
        "Para comprobar una predicción, revisa que respete lo que muestra la tabla. Si la tabla dice 1 → 5, 2 → 10 y 3 → 15, la regla es × 5. Entonces 10 → 50. Una predicción de 55 sería un error, porque 10 × 5 no da 55.",
        "También puedes ir hacia atrás: si la regla es + 12 y la salida es 40, la entrada es 40 − 12 = 28. Una operación y su inversa se deshacen. Siempre verifica con la regla original.",
    ],
    vocab=[("predecir", "decir un resultado antes de calcularlo, usando la regla"), ("comprobar", "revisar si un resultado cumple la regla"), ("entrada", "número que entra a la regla"), ("salida", "número que resulta de la regla"), ("operación inversa", "la que deshace a otra: suma y resta, multiplicación y división")],
    worked=[
        {"title": "Predecir lejos", "problem": "Tabla: 1 → 3, 2 → 6, 3 → 9. ¿Cuál es la salida de la entrada 12?", "steps": ["La regla es × 3.", "12 × 3 = 36."], "answer": "36"},
        {"title": "Ir hacia atrás", "problem": "La regla es + 12. ¿Qué entrada da la salida 40?", "steps": ["Para deshacer + 12 resto 12: 40 − 12 = 28.", "Compruebo: 28 + 12 = 40."], "answer": "28"},
    ],
    mistakes=[
        {"wrong": "Predecir que con regla + 5 y entrada 10 la salida es 50.", "why": "Se multiplica en lugar de sumar.", "fix": "La regla es + 5: 10 + 5 = 15."},
        {"wrong": "Decir que si 6 → 18 con × 3, entonces 7 → 24.", "why": "Se suma 6 al resultado en lugar de aplicar la regla.", "fix": "7 × 3 = 21."},
    ],
    tiers={
        "recovery": [
            arith("La regla es «+ 8». Si la entrada es 12, ¿cuál es la salida?", "12+8", "Se suma 8 a la entrada."),
            arith("La regla es «× 4». Si la entrada es 6, ¿cuál es la salida?", "6*4", "Se multiplica la entrada por 4."),
            arith("La regla es «− 5». Si la entrada es 31, ¿cuál es la salida?", "31-5", "Se resta 5 a la entrada."),
        ],
        "understand": [
            ex("Una tabla muestra 1 → 5, 2 → 10, 3 → 15. Siguiendo el patrón, ¿cuál es la salida de 4?", "20", "La regla es × 5."),
            ex("En esa tabla (1 → 5, 2 → 10, 3 → 15), ¿cuál es la salida de la entrada 10?", "50", "10 × 5 = 50."),
            ex("En una regla «+ 6», la entrada 20 da 26. ¿Cuál es la salida de la entrada 21?", "27", "Si la entrada sube 1, la salida también sube 1."),
        ],
        "apply": [
            arith("La regla es «× 7». ¿Cuál es la salida de la entrada 9?", "7*9", "Se multiplica 9 por 7."),
            arith("La regla es «+ 15». ¿Cuál es la salida de la entrada 85?", "85+15", "Se suma 15 a 85."),
            ex("Tabla: pasos 1, 2, 3, 4 → valores 3, 6, 9, 12. ¿Qué valor corresponde al paso 12?", "36", "La regla es × 3 y 12 × 3 = 36."),
        ],
        "reason": [
            ex("Joaquín dice que, con la regla «+ 5», la entrada 10 da salida 50. ¿Cuál es su error?", "Multiplicó en vez de sumar; la salida es 15", "Con regla + 5, 10 + 5 = 15."),
            ex("Sofía dice que, con × 3, si 6 → 18, entonces 7 → 24. ¿Es correcto?", "No; 7 → 21", "7 × 3 = 21."),
        ],
        "challenge": [
            arith("La regla es «+ 12». Se necesita salida 40. ¿Qué entrada hay que usar?", "40-12", "Para deshacer una suma se resta."),
            ex("Se sabe que 3 → 12 y 5 → 20 con una regla de multiplicar. ¿Cuál es la salida de 9?", "36", "La regla es × 4 y 9 × 4 = 36."),
        ],
    },
    context=[arith("En cada mesa caben 6 personas. ¿Cuántas personas caben en 9 mesas?", "6*9", "Cada mesa suma 6 personas.")],
    selfcheck=[
        arith("Con la regla «× 5», ¿cuál es la salida de 8?", "8*5", "Se multiplica la entrada por 5."),
        arith("La regla es «− 7». Si la salida es 20, ¿cuál fue la entrada?", "20+7", "Se suma para deshacer la resta."),
        ex("En la tabla 2 → 8, 3 → 12, ¿cuál es la regla?", "Multiplicar por 4", "2 × 4 = 8 y 3 × 4 = 12."),
    ],
    open_task=task(
        "Elige una tabla. A) 1 → 4, 2 → 8, 3 → 12. B) 10 → 3, 20 → 13, 30 → 23. Escribe la regla, predice la salida de la entrada 50 y comprueba tu predicción con la regla.",
        "B) La regla es restar 7. Entrada 50 → 50 − 7 = 43. Comprobación: 43 + 7 = 50.",
        ["escribe la regla", "predice con la regla", "comprueba la predicción"],
        ["regla", "predicción", "comprobación"],
        ["aplicar una operación equivocada", "no comprobar"],
        "Pide que muestre la comprobación con la operación inversa. Reconoce la regla antes del cálculo.",
    ),
    reinforce="Elige una regla y una entrada. Pide a una persona de tu casa que prediga la salida y compruébalo tú.",
    extend="Crea una tabla con la regla «÷ 3», escribe seis parejas y predice la salida de una entrada grande como 90.",
)

register(
    OA13, 4,
    materials="Lápiz y papel.",
    use="Aprenderé a crear reglas de una operación y a compararlas. Sirve para ver cómo dos reglas distintas pueden dar resultados parecidos o muy diferentes.",
    prior=["Sé descubrir y usar reglas de una operación.", "Sé comprobar una predicción."],
    explain=[
        "Puedes crear tus propias reglas. Elige una operación y un número, por ejemplo « + 7 » o « × 2 », y aplica la regla a varias entradas para completar una tabla. Cada entrada debe tener una sola salida.",
        "Dos reglas distintas pueden dar la misma salida para una entrada, pero no para todas las entradas. Con entrada 2, « × 2 » y « + 2 » dan 4. Pero con entrada 3, « × 2 » da 6 y « + 2 » da 5. Por eso no basta mirar una pareja.",
        "Al comparar reglas, mira cómo crecen. « + 5 » aumenta de a 5. « × 5 » aumenta cada vez más rápido: con entrada 10 da 50, mientras que « + 5 » da 15. Para decidir cuál regla da una salida mayor, calcula con la misma entrada.",
    ],
    vocab=[("crear una regla", "elegir una operación y un número para transformar entradas"), ("comparar reglas", "calcular ambas con la misma entrada y ver cuál da más"), ("equivalentes", "que dan el mismo resultado para toda entrada"), ("crecer", "hacerse mayor al aumentar la entrada"), ("contraejemplo", "ejemplo que muestra que una afirmación no siempre es cierta")],
    worked=[
        {"title": "Crear una tabla", "problem": "Crea una tabla con la regla « + 7» para las entradas 1, 2 y 3.", "steps": ["1 + 7 = 8, 2 + 7 = 9 y 3 + 7 = 10.", "La tabla queda: 1 → 8, 2 → 9, 3 → 10."], "answer": "8, 9 y 10"},
        {"title": "Comparar dos reglas", "problem": "Regla A: « + 3». Regla B: « × 3». Con la entrada 5, ¿cuál da más?", "steps": ["A: 5 + 3 = 8.", "B: 5 × 3 = 15.", "15 es mayor que 8."], "answer": "La regla B, con 7 de ventaja"},
    ],
    mistakes=[
        {"wrong": "Decir que « × 2 » y « + 2 » son la misma regla porque con entrada 2 dan lo mismo.", "why": "Se prueba una sola entrada.", "fix": "Con entrada 3 dan 6 y 5. No son la misma regla."},
        {"wrong": "Decir que la regla « + 4 » da 20 con entrada 5 porque 5 × 4 = 20.", "why": "Se usa la operación equivocada.", "fix": "5 + 4 = 9."},
    ],
    tiers={
        "recovery": [
            ex("Calcula la salida de la entrada 4 con la regla « × 2» y con la regla « + 2».", "8 y 6", "4 × 2 = 8 y 4 + 2 = 6."),
            ex("Con la regla « × 10», completa las salidas de las entradas 3, 5 y 8.", "30, 50 y 80", "Multiplicar por 10 agrega un cero."),
            ex("Con la regla « − 3», completa las salidas de las entradas 9, 12 y 20.", "6, 9 y 17", "Se resta 3 a cada entrada."),
        ],
        "understand": [
            ex("Las reglas « × 2» y « + 4» ¿dan el mismo resultado para qué entrada?", "Para la entrada 4", "4 × 2 = 8 y 4 + 4 = 8."),
            ex("La regla « + 0», ¿cambia el número?", "No", "Sumar 0 deja el número igual."),
            ex("Para una entrada grande como 10, ¿cuál da una salida mayor: « + 5» o « × 5»?", "« × 5»", "10 + 5 = 15 y 10 × 5 = 50."),
        ],
        "apply": [
            ex("Crea una tabla con la regla « + 7». Escribe las salidas para las entradas 1, 2 y 3.", "8, 9 y 10", "Se suma 7 a cada entrada."),
            ex("Regla A: « + 3». Regla B: « × 3». Con la entrada 5, ¿cuál regla da una salida mayor y cuánto más?", "La B, con 7 más", "A da 8, B da 15 y 15 − 8 = 7."),
            ex("Con la regla « ÷ 2», escribe las salidas de las entradas 8, 12 y 20.", "4, 6 y 10", "Se divide cada entrada por 2."),
        ],
        "reason": [
            ex("Rita dice que « × 2» y « + 2» son la misma regla porque con la entrada 2 dan el mismo resultado. ¿Tiene razón?", "No; con 3 dan 6 y 5", "Una regla igual debe coincidir con toda entrada."),
            ex("Marco dice que « + 4» da 20 con la entrada 5 porque 5 × 4 = 20. ¿Qué error cometió?", "Multiplicó en vez de sumar; la salida es 9", "La regla es suma."),
        ],
        "challenge": [
            ex("Una regla suma y otra multiplica, y las dos convierten el 6 en 24. Escribe cada regla.", "« × 4» y « + 18»", "6 × 4 = 24 y 6 + 18 = 24."),
            ex("¿Para qué entrada dan el mismo resultado « × 3» y « + 6»?", "Para la entrada 3", "3 × 3 = 9 y 3 + 6 = 9."),
        ],
    },
    context=[ex("Plan A: pagas tantos pesos como lápices lleves más 6 pesos fijos (cantidad + 6). Plan B: pagas el doble de pesos que de lápices (cantidad × 2). ¿Con cuántos lápices los dos planes cuestan lo mismo?", "Con 6 lápices", "6 + 6 = 12 y 6 × 2 = 12.")],
    selfcheck=[
        ex("Con la entrada 4, ¿cuál da más: « + 9» o « × 3»?", "« + 9»", "4 + 9 = 13 y 4 × 3 = 12."),
        ex("Completa la tabla con « × 5» para las entradas 2, 4 y 6.", "10, 20 y 30", "Se multiplica cada entrada por 5."),
        ex("¿Para qué entrada « + 8» da lo mismo que « × 2»?", "Para la entrada 8", "8 + 8 = 16 y 8 × 2 = 16."),
    ],
    open_task=task(
        "Crea dos reglas, una de suma y una de multiplicación, y complétalas con las entradas 1, 2, 3 y 4. Elige entre: « + 6» y « × 3», o « + 10» y « × 5». Indica con qué entrada dan lo mismo, si lo hacen, y cuál regla da salidas más grandes para la entrada 4.",
        "Elegí « + 6» y « × 3». Salidas: 7, 8, 9, 10 y 3, 6, 9, 12. Dan lo mismo con la entrada 3 (9). Con la entrada 4, « × 3» da más.",
        ["completa las dos tablas", "señala dónde coinciden", "compara las salidas con la misma entrada"],
        ["dos tablas", "comparación"],
        ["pensar que coinciden en toda entrada", "usar la operación equivocada"],
        "Pide que pruebe una entrada nueva para ver si siguen coincidiendo. Reconoce el contraejemplo.",
    ),
    reinforce="Elige una regla de suma y una de multiplicación. Calcula las salidas de las entradas 1 a 5 y marca dónde se cruzan.",
    extend="Busca una entrada para la que « + 12» y « × 4» den lo mismo y comprueba que solo ocurre una vez.",
)
