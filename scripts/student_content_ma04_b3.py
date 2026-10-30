"""Student material for 4.º básico Matemática, OA 14 (ecuaciones e inecuaciones de un paso) y OA 15 (localización absoluta y relativa)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA14, OA15 = "MA04 OA 14", "MA04 OA 15"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


NATURALES = "En esta clase, la letra n es un número natural: puede valer 0, 1, 2, 3…"

# ================================================================ OA 14
register(
    OA14, 1,
    materials=f"Lápiz y papel. {NATURALES}",
    use="Aprenderé a leer igualdades y desigualdades como una balanza. Sirve para saber cuándo dos cantidades valen lo mismo y cuándo no.",
    prior=["Sé sumar y restar hasta 100.", "Conozco los signos <, > y =."],
    explain=[
        "Una igualdad dice que dos cantidades valen lo mismo. Se escribe con el signo =. Es como una balanza equilibrada: 6 + 3 = 8 + 1, porque los dos lados valen 9.",
        "Una desigualdad dice que dos cantidades son distintas. Se usa < (menor que) o > (mayor que). Por ejemplo, 8 + 5 > 12 porque 13 es mayor que 12. La balanza se inclina hacia el lado más grande.",
        "A veces falta un número y se usa una letra, por ejemplo n. En n + 4 = 10, la letra es un número que no conocemos. Si es una igualdad, se llama ecuación. Si lleva < o >, se llama inecuación. Para saber si un número sirve, lo reemplazas y comparas.",
    ],
    vocab=[("igualdad", "dos cantidades que valen lo mismo, unidas con ="), ("desigualdad", "dos cantidades que no valen lo mismo, unidas con < o >"), ("ecuación", "igualdad en la que falta un número"), ("inecuación", "desigualdad en la que falta un número"), ("incógnita", "letra que representa el número que no conocemos")],
    worked=[
        {"title": "Comparar con signos", "problem": "Completa con <, > o =: 8 + 5 ___ 12.", "steps": ["8 + 5 = 13.", "13 es mayor que 12."], "answer": ">"},
        {"title": "Escribir una ecuación", "problem": "Escribe «un número más 4 es igual a 10».", "steps": ["El número desconocido se llama n.", "«Más 4» es + 4 y «es igual a» es =."], "answer": "n + 4 = 10"},
    ],
    mistakes=[
        {"wrong": "Decir que 6 + 3 = 8 + 1 es falso porque a la derecha hay números más grandes.", "why": "Se comparan los números sueltos y no el valor de cada lado.", "fix": "6 + 3 = 9 y 8 + 1 = 9. Los dos lados valen lo mismo, así que es verdadero."},
        {"wrong": "Pensar que se puede sumar 3 solo a un lado de una igualdad y que siga igual.", "why": "No se mantiene el equilibrio de la balanza.", "fix": "Si cambias un lado, el otro debe cambiar igual. Si no, deja de ser igualdad."},
    ],
    tiers={
        "recovery": [
            ex("Una balanza está equilibrada: a la izquierda hay 7 y a la derecha hay 3 + 4. ¿Qué signo va entre ambos lados: =, < o >?", "=", "7 y 3 + 4 valen lo mismo."),
            ex("Completa con <, > o =: 8 + 5 ___ 12.", ">", "8 + 5 = 13 y 13 es mayor que 12."),
            ex("Completa con <, > o =: 20 − 6 ___ 15.", "<", "20 − 6 = 14 y 14 es menor que 15."),
        ],
        "understand": [
            ex("¿Qué indica el signo = entre dos cantidades?", "Que ambas valen lo mismo", "Es como una balanza en equilibrio."),
            ex("El lado izquierdo de una desigualdad vale más que el derecho. ¿Qué signo se usa?", ">", "El signo > se abre hacia el lado mayor."),
            ex("¿Cuál de las dos es una ecuación: «n + 3 < 8» o «5 + n = 9»?", "5 + n = 9", "Una ecuación lleva el signo =."),
        ],
        "apply": [
            ex("En una balanza equilibrada, a la izquierda hay 15 y a la derecha hay 9 + n. ¿Cuánto vale n?", "6", "9 + 6 = 15."),
            ex("Escribe con símbolos: «un número más 4 es igual a 10». Usa n.", "n + 4 = 10", "«Más 4» es + 4 y «es igual a» es =."),
            ex("Escribe con símbolos: «un número más 4 es menor que 10». Usa n.", "n + 4 < 10", "«Es menor que» se escribe con <."),
        ],
        "reason": [
            ex("Lucas dice que 6 + 3 = 8 + 1 es falso porque a la derecha hay números más grandes. ¿Tiene razón?", "No; los dos lados valen 9", "6 + 3 = 9 y 8 + 1 = 9."),
            ex("Una balanza equilibrada tiene 12 a la izquierda y 5 + n a la derecha. Se agregan 3 solo a la izquierda. ¿Sigue equilibrada?", "No", "Hay que agregar 3 también al otro lado para mantener el equilibrio."),
        ],
        "challenge": [
            ex("¿Qué número natural n hace verdadera la igualdad n + 7 = 7 + 5?", "5", "7 + 5 = 12 y 5 + 7 = 12."),
            ex("De los números 0, 1, 2, …, 10, ¿cuántos hacen verdadera la desigualdad 4 + n < 8?", "4", "Sirven 0, 1, 2 y 3."),
        ],
    },
    context=[ex("Ana tiene 25 figuritas y Beto tiene 18. ¿Cuántas figuritas necesita Beto para tener tantas como Ana?", "7", "Falta la diferencia: 25 − 18 = 7, y 18 + 7 = 25.")],
    selfcheck=[
        ex("Completa con <, > o =: 14 + 6 ___ 20.", "=", "14 + 6 = 20."),
        ex("Escribe con símbolos: «un número menos 5 es igual a 9». Usa n.", "n − 5 = 9", "«Menos 5» es − 5."),
        ex("¿Qué significa la letra n en una ecuación?", "Un número que no conocemos", "Representa el valor que buscamos."),
    ],
    open_task=task(
        "Dibuja una balanza con los números del enunciado y escribe el signo correcto. Elige: A) 9 + 8 y 17. B) 25 − 10 y 14. Después escribe una ecuación con n que se parezca (por ejemplo, n + 8 = 17).",
        "A) 9 + 8 = 17, la balanza está equilibrada. Ecuación: n + 8 = 17, así n = 9.",
        ["calcula cada lado", "escribe el signo correcto", "escribe una ecuación con n"],
        ["balanza dibujada", "signo", "ecuación"],
        ["comparar números sueltos", "usar mal el signo < o >"],
        "Pide que calcule los dos lados antes de poner el signo. Reconoce la balanza como modelo.",
    ),
    reinforce="Usa una balanza imaginaria con monedas: pon 5 monedas a un lado y pide a alguien que descubra cuántas poner del otro para que quede equilibrada.",
    extend="Escribe tres igualdades y tres desigualdades con sumas y restas hasta 100.",
)

register(
    OA14, 2,
    materials=f"Lápiz y papel. {NATURALES}",
    use="Aprenderé a resolver ecuaciones de suma y resta con una operación inversa. Sirve para encontrar el número que falta.",
    prior=["Sé qué es una ecuación.", "Sé que la suma y la resta se deshacen entre sí."],
    explain=[
        "Resolver una ecuación es encontrar el número que la hace verdadera. En n + 17 = 45 buscamos n. La suma se deshace con una resta: n = 45 − 17 = 28.",
        "En n − 12 = 30 pasa lo contrario. La resta se deshace con una suma: n = 30 + 12 = 42. Cuando la incógnita está al final, como en 100 − n = 64, piensa: ¿cuánto quito a 100 para que quede 64? Es 100 − 64 = 36.",
        "Siempre comprueba: reemplaza n por el resultado y revisa que se cumpla la igualdad. Con n = 28 queda 28 + 17 = 45, que es verdadero. Si no se cumple, revisa tu operación.",
    ],
    vocab=[("ecuación", "igualdad en la que falta un número"), ("incógnita", "letra que representa el número que falta"), ("operación inversa", "operación que deshace a otra: suma y resta"), ("solución", "valor que hace verdadera la ecuación"), ("reemplazar", "poner un número en lugar de la letra")],
    worked=[
        {"title": "Ecuación de suma", "problem": "Resuelve n + 17 = 45.", "steps": ["Para deshacer + 17, resto 17: 45 − 17 = 28.", "Compruebo: 28 + 17 = 45."], "answer": "n = 28"},
        {"title": "Ecuación de resta", "problem": "Resuelve n − 12 = 30.", "steps": ["Para deshacer − 12, sumo 12: 30 + 12 = 42.", "Compruebo: 42 − 12 = 30."], "answer": "n = 42"},
    ],
    mistakes=[
        {"wrong": "Resolver n + 17 = 45 sumando: 45 + 17 = 62.", "why": "Se usa la misma operación en lugar de la inversa.", "fix": "Como n se suma con 17, se resta: 45 − 17 = 28."},
        {"wrong": "Resolver 100 − n = 64 como n = 164.", "why": "Se suma 100 y 64 por costumbre.", "fix": "Piensa cuánto se quita a 100 para quedar 64: n = 100 − 64 = 36."},
    ],
    tiers={
        "recovery": [
            arith("Resuelve n + 5 = 12. ¿Cuánto vale n?", "12-5", "Se resta 5 para deshacer la suma."),
            arith("Resuelve n − 4 = 10. ¿Cuánto vale n?", "10+4", "Se suma 4 para deshacer la resta."),
            arith("Resuelve 9 + n = 15. ¿Cuánto vale n?", "15-9", "Falta lo que hay entre 9 y 15."),
        ],
        "understand": [
            ex("Para resolver n + 17 = 45, ¿qué operación haces con 45 y 17?", "Restar 17 a 45", "La resta deshace la suma."),
            ex("Para resolver n − 12 = 30, ¿qué operación haces con 30 y 12?", "Sumar 12 a 30", "La suma deshace la resta."),
            ex("¿Cómo compruebas que n = 28 es solución de n + 17 = 45?", "Reemplazando: 28 + 17 = 45", "Si la igualdad se cumple, la solución es correcta."),
        ],
        "apply": [
            arith("Resuelve n + 19 = 52.", "52-19", "Se resta 19 a 52."),
            arith("Resuelve n − 15 = 28.", "28+15", "Se suma 15 a 28."),
            arith("Resuelve 63 = n + 28. Busca el número que sumado a 28 da 63.", "63-28", "Se resta 28 a 63."),
        ],
        "reason": [
            ex("Eli resolvió n + 17 = 45 y escribió n = 62 porque sumó 45 + 17. ¿Cuál es su error y cuál es la solución?", "Usó la suma en vez de la resta; n = 28", "n + 17 = 45 se deshace con 45 − 17."),
            ex("Mauro resolvió 100 − n = 64 y escribió n = 164. ¿Es posible? Explica con una comprobación.", "No; n = 36", "100 − 164 no se puede en naturales y 100 − 36 = 64."),
        ],
        "challenge": [
            arith("Resuelve 90 − n = 47. Piensa: ¿cuánto quito a 90 para que quede 47?", "90-47", "Se resta 47 a 90."),
            arith("Resuelve n − 38 = 49.", "49+38", "Se suma 38 a 49."),
        ],
    },
    context=[arith("Tenías algunas figuritas, regalaste 15 y te quedaron 32. ¿Cuántas figuritas tenías al principio?", "32+15", "Se suma lo que quedó con lo que se regaló.")],
    selfcheck=[
        arith("Resuelve n + 24 = 70.", "70-24", "Se resta 24 a 70."),
        arith("Resuelve n − 9 = 41.", "41+9", "Se suma 9 a 41."),
        ex("Comprueba: ¿n = 35 es solución de n + 28 = 63?", "Sí", "35 + 28 = 63."),
    ],
    open_task=task(
        "Elige una ecuación y resuélvela con la operación inversa. A) n + 26 = 71. B) n − 18 = 40. Escribe la operación que usaste y comprueba reemplazando.",
        "B) n − 18 = 40. Sumo 18: n = 58. Compruebo: 58 − 18 = 40.",
        ["elige la operación inversa", "calcula el valor de n", "comprueba reemplazando"],
        ["operación", "valor de n", "comprobación"],
        ["usar la misma operación en lugar de la inversa", "no comprobar"],
        "Pide que diga por qué usa suma o resta. Reconoce la comprobación como verificación real.",
    ),
    reinforce="Inventa dos ecuaciones con n usando números de 2 cifras y pide a alguien que las resuelva. Tú compruebas.",
    extend="Escribe un problema de la vida diaria que se resuelva con n + 35 = 90 y resuélvelo.",
)

register(
    OA14, 3,
    materials=f"Lápiz y papel. {NATURALES}",
    use="Aprenderé a resolver inecuaciones de un paso en el rango de 0 a 100. Sirve para saber qué valores cumplen una condición como «menos de 30».",
    prior=["Sé resolver ecuaciones de suma y resta.", "Sé usar < y >."],
    explain=[
        "Una inecuación como n + 12 < 30 pide los números que, al sumarles 12, dan menos de 30. Puede tener varias soluciones. Primero busca el límite: 30 − 12 = 18. Entonces n debe ser menor que 18.",
        "Como n debe ser menor que 18, los valores posibles son 0, 1, 2, …, 17. El mayor es 17 y el 18 no sirve, porque 18 + 12 = 30 no es menor que 30. Siempre revisa el límite.",
        "En n − 6 > 14 el límite es 14 + 6 = 20. Se pide n mayor que 20, así que el menor valor posible es 21. Comprueba: 21 − 6 = 15, que es mayor que 14.",
    ],
    vocab=[("inecuación", "desigualdad con un número desconocido"), ("solución", "valor que hace verdadera la desigualdad"), ("límite", "número en que cambia la respuesta"), ("menor que (<)", "símbolo para decir que un valor es más pequeño"), ("mayor que (>)", "símbolo para decir que un valor es más grande")],
    worked=[
        {"title": "Mayor solución", "problem": "En n + 12 < 30, ¿cuál es el mayor número natural que sirve?", "steps": ["El límite es 30 − 12 = 18.", "n debe ser menor que 18, así que el mayor es 17.", "Compruebo: 17 + 12 = 29, menor que 30."], "answer": "17"},
        {"title": "Menor solución", "problem": "En n − 6 > 14, ¿cuál es el menor número natural que sirve?", "steps": ["El límite es 14 + 6 = 20.", "n debe ser mayor que 20, así que el menor es 21.", "Compruebo: 21 − 6 = 15, mayor que 14."], "answer": "21"},
    ],
    mistakes=[
        {"wrong": "Pablo dice que n = 18 sirve en n + 12 < 30 porque 18 + 12 = 30.", "why": "Confunde menor que con menor o igual que.", "fix": "30 no es menor que 30. El mayor valor es 17."},
        {"wrong": "Leti dice que n = 5 sirve en n + 4 > 10 porque 5 + 4 = 9 está cerca de 10.", "why": "Mira si se acerca al número en vez de comparar.", "fix": "9 no es mayor que 10. n tiene que ser mayor que 6."},
    ],
    tiers={
        "recovery": [
            ex("¿Se cumple n + 5 < 12 cuando n = 4?", "Sí", "4 + 5 = 9 y 9 es menor que 12."),
            ex("¿Se cumple n + 5 < 12 cuando n = 7?", "No", "7 + 5 = 12, y 12 no es menor que 12."),
            ex("¿Se cumple n − 3 > 10 cuando n = 20?", "Sí", "20 − 3 = 17 y 17 es mayor que 10."),
        ],
        "understand": [
            ex("En n + 9 < 25, ¿cuál es el mayor número natural que cumple?", "15", "15 + 9 = 24 y 16 + 9 = 25 ya no es menor."),
            ex("En n + 4 > 10, ¿cuál sirve: n = 6 o n = 7?", "n = 7", "7 + 4 = 11 es mayor que 10, pero 6 + 4 = 10 no."),
            ex("¿Una inecuación como n + 3 < 9 puede tener más de una solución?", "Sí", "Sirven 0, 1, 2, 3, 4 y 5."),
        ],
        "apply": [
            arith("En n + 20 < 50, ¿cuál es el mayor número natural que cumple? Busca el límite (50 − 20) y resta 1.", "50-20-1", "El límite es 30, que no sirve."),
            arith("En n − 9 > 31, ¿cuál es el menor número natural que cumple? Busca el límite (31 + 9) y suma 1.", "31+9+1", "El límite es 40, que no sirve."),
            ex("¿Cuántos números naturales cumplen n + 7 < 10?", "3", "Sirven 0, 1 y 2."),
        ],
        "reason": [
            ex("Pablo dice que n = 18 sirve en n + 12 < 30 porque 18 + 12 = 30. ¿Tiene razón?", "No; 30 no es menor que 30", "El mayor valor que sirve es 17."),
            ex("Leti dice que n = 5 sirve en n + 4 > 10 porque 5 + 4 = 9 está cerca de 10. ¿Tiene razón?", "No; 9 no es mayor que 10", "Una desigualdad exige comparar, no acercarse."),
        ],
        "challenge": [
            ex("¿Cuántos números naturales cumplen n + 8 < 30?", "22", "Sirven desde 0 hasta 21, o sea 22 números."),
            ex("Si n es natural y no es mayor que 100, ¿cuántos valores de n cumplen n − 5 > 90?", "5", "n debe ser mayor que 95; sirven 96, 97, 98, 99 y 100, o sea 5 valores."),
        ],
    },
    context=[arith("Una caja aguanta menos de 40 kg y ya tiene 25 kg. ¿Cuál es el mayor número entero de kilogramos que se puede agregar? Cuenta desde el límite 40 − 25 y resta 1.", "40-25-1", "El límite no sirve porque tiene que ser menor que 40.")],
    selfcheck=[
        ex("¿Se cumple n + 8 < 20 cuando n = 11?", "Sí", "11 + 8 = 19 y 19 es menor que 20."),
        arith("En n + 30 < 100, ¿cuál es el mayor número natural que cumple?", "100-30-1", "El límite es 70, que no sirve."),
        ex("¿n = 9 cumple n − 2 > 7?", "No", "9 − 2 = 7 y 7 no es mayor que 7."),
    ],
    open_task=task(
        "Elige una inecuación y busca el menor o el mayor valor que sirve, mostrando el límite. A) n + 15 < 40, el mayor. B) n − 8 > 20, el menor. Comprueba con una suma o una resta.",
        "B) El límite es 20 + 8 = 28. n debe ser mayor que 28, así que el menor es 29. Compruebo: 29 − 8 = 21, que es mayor que 20.",
        ["calcula el límite", "decide si incluye o no el límite", "comprueba el valor elegido"],
        ["límite", "valor", "comprobación"],
        ["incluir el límite", "no comprobar"],
        "Pide que pruebe el valor elegido y el siguiente. Reconoce la prueba de los dos lados del límite.",
    ),
    reinforce="Escribe tres números que cumplan n + 10 < 30 y tres que no. Comprueba cada uno.",
    extend="Escribe una inecuación de resta con límite 50 y encuentra el menor valor natural que la cumple.",
)

register(
    OA14, 4,
    materials=f"Lápiz y papel. {NATURALES}",
    use="Aprenderé a comprobar soluciones de ecuaciones e inecuaciones usando la relación inversa entre suma y resta. Sirve para estar seguro de una respuesta.",
    prior=["Sé resolver ecuaciones e inecuaciones de un paso.", "Sé que sumar y restar se deshacen."],
    explain=[
        "Las operaciones de una familia se relacionan: si 38 + 24 = 62, entonces 62 − 24 = 38 y 62 − 38 = 24. Esa relación inversa permite resolver y comprobar. Si resolviste n + 24 = 62 y obtuviste 38, comprueba con 38 + 24.",
        "Para comprobar una ecuación, reemplaza la letra por tu resultado y mira si la igualdad es verdadera. Para una inecuación, reemplaza y mira si la desigualdad se cumple, y prueba también el valor siguiente. Si el límite no cumple la desigualdad, no es solución.",
        "Para un problema escrito, primero escribe la ecuación. «Pedro tenía n lápices, compró 14 y ahora tiene 50» se escribe n + 14 = 50. Luego resuelves con la resta: n = 36, y comprueba: 36 + 14 = 50.",
    ],
    vocab=[("relación inversa", "relación en que una operación deshace a otra"), ("comprobar", "reemplazar y verificar que se cumpla"), ("solución", "valor que hace verdadera la ecuación o inecuación"), ("familia de operaciones", "sumas y restas con los mismos tres números"), ("reemplazar", "poner un número en lugar de la letra")],
    worked=[
        {"title": "Problema con ecuación", "problem": "Pedro tenía n lápices, compró 14 y ahora tiene 50. ¿Cuántos tenía?", "steps": ["Ecuación: n + 14 = 50.", "Resto: 50 − 14 = 36.", "Compruebo: 36 + 14 = 50."], "answer": "n = 36"},
        {"title": "Comprobar una inecuación", "problem": "¿n = 27 cumple n + 19 < 45?", "steps": ["Reemplazo: 27 + 19 = 46.", "46 no es menor que 45."], "answer": "No cumple"},
    ],
    mistakes=[
        {"wrong": "Decir que n = 74 resuelve 54 − n = 20.", "why": "No se reemplaza para comprobar.", "fix": "54 − 74 no es posible en naturales. Resuelve 54 − 20 = 34 y comprueba 54 − 34 = 20."},
        {"wrong": "Decir que n = 27 cumple n + 19 < 45 porque 27 es pequeño.", "why": "No se calcula el valor.", "fix": "27 + 19 = 46, que no es menor que 45."},
    ],
    tiers={
        "recovery": [
            ex("¿Con qué operación se deshace «sumar 15»?", "Con restar 15", "La resta es la operación inversa de la suma."),
            ex("¿Con qué operación se deshace «restar 8»?", "Con sumar 8", "La suma es la operación inversa de la resta."),
            arith("Resuelve n + 25 = 70.", "70-25", "Se resta 25 a 70."),
        ],
        "understand": [
            ex("Si 38 + 24 = 62, ¿cuánto es 62 − 24?", "38", "La resta deshace la suma."),
            ex("Para comprobar que n = 45 resuelve n + 25 = 70, ¿qué haces?", "Reemplazo: 45 + 25 = 70", "Si la igualdad se cumple, la solución sirve."),
            ex("Si 38 + 24 = 62, ¿cuánto es 62 − 38?", "24", "La resta de la otra parte también deshace la suma."),
        ],
        "apply": [
            ex("María resolvió n − 19 = 40 y obtuvo n = 59. Comprueba reemplazando. ¿Es correcto?", "Sí; 59 − 19 = 40", "El reemplazo cumple la igualdad."),
            arith("Ana tenía n globos, compró 17 y ahora tiene 62. Resuelve n + 17 = 62.", "62-17", "Se resta lo que compró."),
            arith("Resuelve n + 36 = 90.", "90-36", "Se resta 36 a 90."),
        ],
        "reason": [
            ex("Ítalo resolvió 54 − n = 20 y dijo n = 74. Comprueba y corrige.", "No; n = 34", "54 − 34 = 20."),
            ex("Sofía dice que n = 27 cumple n + 19 < 45. Compruébalo.", "No; 27 + 19 = 46 y 46 no es menor que 45", "Al reemplazar no se cumple la desigualdad."),
        ],
        "challenge": [
            arith("Si n + 28 = 100, ¿cuánto vale n?", "100-28", "Se resta 28 a 100."),
            arith("En 100 − n < 30, ¿cuál es el menor número natural n? Busca el límite 100 − 30 y suma 1.", "100-30+1", "n debe ser mayor que 70."),
        ],
    },
    context=[arith("En un álbum caben 100 figuritas y ya pegaste 64. ¿Cuántas figuritas faltan para llenarlo?", "100-64", "Se resta lo pegado al total.")],
    selfcheck=[
        ex("Si 45 + 18 = 63, ¿cuánto es 63 − 18?", "45", "La resta deshace la suma."),
        arith("Resuelve n − 21 = 60 y comprueba.", "60+21", "Se suma 21 a 60."),
        ex("¿n = 15 cumple n + 20 < 40?", "Sí", "15 + 20 = 35 y 35 es menor que 40."),
    ],
    open_task=task(
        "Elige un problema, escribe la ecuación con n, resuélvela y comprueba. A) Tenías n figuritas, regalaste 18 y te quedaron 42. B) En un bus había n personas, subieron 15 y ahora hay 60.",
        "B) n + 15 = 60. n = 60 − 15 = 45. Compruebo: 45 + 15 = 60.",
        ["escribe la ecuación", "usa la relación inversa", "comprueba reemplazando", "responde con una oración"],
        ["ecuación", "solución", "comprobación"],
        ["escribir mal la ecuación", "no comprobar"],
        "Pide que lea la ecuación con palabras. Reconoce que escribió la ecuación antes de calcular.",
    ),
    reinforce="Escribe una ecuación de suma y su familia de restas con los mismos números.",
    extend="Crea una inecuación de suma y encuentra los tres mayores valores naturales que la cumplen.",
)

# ================================================================ OA 15
MAPA = "Mapa con filas A, B, C y D (de arriba hacia abajo) y columnas 1, 2, 3 y 4 (de izquierda a derecha). A1 plaza, A3 escuela, B2 panadería, B4 farmacia, C1 biblioteca, C3 parque, D2 feria, D4 consultorio. Las demás casillas están vacías."
MAPA2 = "Mapa con filas A, B y C (de arriba hacia abajo) y columnas 1 a 4 (de izquierda a derecha). A1 casa, A2 plaza, A3 escuela, B1 panadería, B3 farmacia, B4 parque, C2 biblioteca, C3 feria, C4 consultorio. Las demás casillas están vacías."
PARQUE = "Parque con filas A, B, C y D (de arriba hacia abajo) y columnas 1 a 5 (de izquierda a derecha). A1 árbol, A4 resbalín, B2 columpio, C3 banca, C5 arenero, D1 fuente. Las demás casillas están vacías."

register(
    OA15, 1,
    materials="Lápiz y papel. Usa un mapa de casillas con letras para las filas y números para las columnas.",
    use="Aprenderé a leer coordenadas con una letra y un número. Sirve para encontrar un lugar en un mapa o un asiento en una sala.",
    prior=["Sé leer filas y columnas.", "Sé ordenar letras del abecedario y números."],
    explain=[
        "Un mapa de casillas se divide en filas y columnas. Las filas se nombran con letras y las columnas con números. Una coordenada es el nombre de una casilla. Se escribe primero la letra y luego el número, como B3.",
        "La letra dice la fila y la fila se cuenta de arriba hacia abajo. El número dice la columna y la columna se cuenta de izquierda a derecha. En B3 buscas la fila B y avanzas hasta la columna 3.",
        "La coordenada B3 no es lo mismo que C2. El orden importa: primero fila y después columna. Si una casilla no tiene nada, está vacía, pero igual tiene coordenada.",
    ],
    vocab=[("coordenada", "nombre de una casilla, con una letra y un número"), ("fila", "línea de casillas de izquierda a derecha, nombrada con una letra"), ("columna", "línea de casillas de arriba hacia abajo, nombrada con un número"), ("casilla", "cada cuadro del mapa"), ("mapa", "dibujo que muestra dónde están los lugares")],
    worked=[
        {"title": "Leer una coordenada", "problem": f"{MAPA} ¿Qué hay en la casilla C3?", "steps": ["C es la fila: la tercera de arriba hacia abajo.", "3 es la columna: la tercera de izquierda a derecha.", "En C3 está el parque."], "answer": "El parque"},
        {"title": "Escribir una coordenada", "problem": "En el mismo mapa, ¿cuál es la coordenada de la feria?", "steps": ["La feria está en la fila D.", "La feria está en la columna 2.", "Se escribe primero la letra y luego el número."], "answer": "D2"},
    ],
    mistakes=[
        {"wrong": "Buscar B4 en la fila 4 y columna B.", "why": "Se invierte el orden de la coordenada.", "fix": "La letra es la fila y el número es la columna: B4 es fila B, columna 4."},
        {"wrong": "Decir que una casilla vacía no tiene coordenada.", "why": "Se piensa que solo los lugares tienen nombre.", "fix": "Toda casilla tiene coordenada, aunque esté vacía."},
    ],
    tiers={
        "recovery": [
            ex(f"{MAPA} ¿Qué hay en la casilla A1?", "La plaza", "En A1 está la plaza."),
            ex(f"{MAPA} ¿Qué hay en la casilla B2?", "La panadería", "La fila B y la columna 2 se cruzan en la panadería."),
            ex(f"{MAPA} ¿En qué fila está la farmacia?", "En la fila B", "La farmacia está en B4."),
        ],
        "understand": [
            ex("En la coordenada B2, ¿qué indica la letra y qué indica el número?", "La letra indica la fila y el número indica la columna", "Primero va la fila y después la columna."),
            ex("En este mapa se escribe la letra primero. ¿La coordenada 2B sigue la regla?", "No", "La coordenada correcta es B2."),
            ex("En un mapa de 4 filas y 4 columnas, ¿cuántas casillas hay?", "16", "4 filas por 4 columnas dan 16."),
        ],
        "apply": [
            ex(f"{MAPA} Escribe la coordenada de la biblioteca.", "C1", "La biblioteca está en la fila C y columna 1."),
            ex(f"{MAPA} Escribe la coordenada del consultorio.", "D4", "El consultorio está en la fila D y columna 4."),
            ex(f"{MAPA} ¿Qué hay en la casilla B3?", "Nada; está vacía", "B3 no aparece en la lista de lugares."),
        ],
        "reason": [
            ex(f"{MAPA} Mario busca B4 en la fila 4 y la columna B, y no encuentra nada. ¿Cuál es su error y qué hay en B4?", "Invirtió el orden; en B4 está la farmacia", "B es la fila y 4 es la columna."),
            ex(f"{MAPA} Clara dice que la escuela está en A2. ¿Tiene razón?", "No; está en A3", "La escuela está en la fila A y columna 3."),
        ],
        "challenge": [
            ex(f"{MAPA} ¿Qué lugar está en la misma fila que la panadería?", "La farmacia", "La panadería está en B2 y la farmacia en B4, ambas en la fila B."),
            ex(f"{MAPA} ¿Qué lugares están en la columna 3?", "La escuela y el parque", "Están en A3 y C3."),
        ],
    },
    context=[ex(f"{MAPA} Una amiga te cita en D2. ¿Qué lugar del mapa es?", "La feria", "D2 es la feria.")],
    selfcheck=[
        ex(f"{MAPA} ¿Qué hay en la casilla A3?", "La escuela", "A3 es la escuela."),
        ex(f"{MAPA} ¿Cuál es la coordenada del parque?", "C3", "El parque está en la fila C, columna 3."),
        ex(f"{MAPA} ¿Cuántas casillas de la fila A están vacías?", "2", "La fila A tiene 4 casillas y solo A1 y A3 están ocupadas."),
    ],
    open_task=task(
        "Dibuja un mapa de 3 filas (A, B, C) y 3 columnas (1, 2, 3). Pon cuatro lugares que elijas entre: casa, escuela, plaza, kiosco, parque, almacén. Escribe la coordenada de cada uno y una pregunta con su respuesta.",
        "Casa A1, escuela B2, plaza C3, parque A3. Pregunta: ¿qué hay en B2? Respuesta: la escuela.",
        ["usa letra para la fila y número para la columna", "escribe cuatro coordenadas correctas", "escribe una pregunta con respuesta"],
        ["mapa dibujado", "lista de coordenadas", "pregunta"],
        ["invertir letra y número", "repetir una casilla"],
        "Pide que lea cada coordenada en voz alta indicando fila y columna. Reconoce el orden letra-número.",
    ),
    reinforce="Con papel cuadriculado, rotula las filas con letras y las columnas con números y marca tres casillas. Pide a alguien que las diga como coordenadas.",
    extend="Dibuja un mapa de 5 filas y 5 columnas y escribe las coordenadas de las cuatro esquinas.",
)

register(
    OA15, 2,
    materials="Lápiz y papel.",
    use="Aprenderé a describir con coordenadas dónde está un objeto, sin compararlo con otro. Sirve para que todos entiendan la misma ubicación.",
    prior=["Sé leer coordenadas con letra y número.", "Sé que la letra es la fila y el número es la columna."],
    explain=[
        "La localización absoluta dice dónde está un objeto con una coordenada. No necesita decir qué hay al lado. Por ejemplo, «la fuente está en D1» sirve para cualquiera que mire el mismo mapa.",
        "Para dar una ubicación absoluta, mira primero la fila del objeto y luego su columna. Escribe la letra y luego el número, sin espacios. Una coordenada identifica una sola casilla.",
        "Comprueba que la casilla exista. Si el mapa tiene filas A, B, C y D, la fila E no existe. Si tiene columnas 1 a 5, la columna 6 tampoco. Un mapa claro sirve cuando todos usan la misma regla.",
    ],
    vocab=[("localización absoluta", "dice dónde está un objeto usando una coordenada"), ("coordenada", "letra y número que nombran una casilla"), ("fila", "línea horizontal de casillas"), ("columna", "línea vertical de casillas"), ("existir", "estar en el mapa")],
    worked=[
        {"title": "Dar una coordenada", "problem": f"{PARQUE} Escribe la coordenada del columpio.", "steps": ["El columpio está en la fila B.", "Está en la columna 2.", "Se escribe B2."], "answer": "B2"},
        {"title": "Ver si una casilla existe", "problem": "En un mapa con filas A a D y columnas 1 a 5, ¿existe la casilla E2?", "steps": ["El mapa llega hasta la fila D.", "No hay fila E, así que E2 no existe."], "answer": "No existe"},
    ],
    mistakes=[
        {"wrong": "Escribir 5C para el arenero.", "why": "Se invierte el orden: número y luego letra.", "fix": "Se escribe C5: fila C y columna 5."},
        {"wrong": "Decir que la fuente está «cerca del árbol» y creer que eso es una coordenada.", "why": "Se confunde ubicación relativa con absoluta.", "fix": "La fuente está en D1."},
    ],
    tiers={
        "recovery": [
            ex(f"{PARQUE} Escribe la coordenada del árbol.", "A1", "El árbol está en la fila A y columna 1."),
            ex(f"{PARQUE} ¿Qué hay en la casilla C5?", "El arenero", "En C5 está el arenero."),
            ex(f"{PARQUE} Escribe la coordenada de la fuente.", "D1", "La fuente está en la fila D y columna 1."),
        ],
        "understand": [
            ex("¿Qué significa «localización absoluta»?", "Decir dónde está un objeto con una coordenada", "No necesita compararlo con otro objeto."),
            ex("¿Por qué una coordenada como B2 es entendida igual por todos?", "Porque nombra una sola casilla", "La letra y el número indican una única fila y columna."),
            ex("En un parque con filas A a D y columnas 1 a 5, ¿existe la casilla E2?", "No", "La última fila es la D."),
        ],
        "apply": [
            ex(f"{PARQUE} Pones un tobogán en la fila C y columna 1. Escribe su coordenada.", "C1", "Primero la fila y luego la columna."),
            ex(f"{PARQUE} Escribe las coordenadas de los objetos que están en la fila A.", "A1 y A4", "El árbol está en A1 y el resbalín en A4."),
            ex(f"{PARQUE} ¿Cuántos objetos hay en la columna 3?", "1", "Solo la banca está en la columna 3."),
        ],
        "reason": [
            ex(f"{PARQUE} Tomás escribe que el arenero está en 5C. ¿Qué debe cambiar para seguir la regla del mapa?", "Escribir C5", "Primero va la letra de la fila."),
            ex(f"{PARQUE} Una amiga dice que la fuente está en D1 y otra que está en 1D. ¿Quién sigue la regla letra primero?", "La que dijo D1", "La coordenada se escribe con la letra primero."),
        ],
        "challenge": [
            ex(f"{PARQUE} ¿Qué dos objetos están en la columna 1 y cuáles son sus coordenadas?", "El árbol en A1 y la fuente en D1", "Ambos están en la columna 1."),
            ex("En un parque con 5 columnas, ¿cuántas casillas distintas tiene la fila B?", "5", "Tiene una casilla por cada columna: B1, B2, B3, B4 y B5."),
        ],
    },
    context=[ex("Para ordenar el patio, el profesor marca filas A, B y C y columnas 1 a 6. Una silla va en la fila B, columna 4. ¿Cuál es su coordenada?", "B4", "Fila B y columna 4.")],
    selfcheck=[
        ex(f"{PARQUE} ¿Cuál es la coordenada de la banca?", "C3", "La banca está en la fila C y columna 3."),
        ex(f"{PARQUE} ¿Qué hay en A4?", "El resbalín", "En A4 está el resbalín."),
        ex("¿Existe la casilla A7 en un mapa con columnas 1 a 5?", "No", "La última columna es la 5."),
    ],
    open_task=task(
        "Usa el parque del enunciado. Elige tres objetos y escribe su coordenada. Después inventa un objeto nuevo, ponlo en una casilla vacía y escribe su coordenada: " + PARQUE,
        "Árbol A1, columpio B2, arenero C5. Pongo un balancín en D4.",
        ["escribe tres coordenadas correctas", "pone el objeto nuevo en una casilla vacía", "usa letra y número"],
        ["lista de coordenadas", "objeto nuevo"],
        ["usar una casilla ocupada", "invertir letra y número"],
        "Pide que verifique que la casilla elegida esté vacía. Reconoce la coordenada como identificador único.",
    ),
    reinforce="Dibuja el plano de tu pieza en una cuadrícula con filas con letras y columnas con números, y escribe la coordenada de cuatro objetos.",
    extend="Escribe una lista de coordenadas de un mapa y pide a alguien que dibuje los objetos.",
)

register(
    OA15, 3,
    materials="Lápiz y papel.",
    use="Aprenderé a describir dónde está un objeto en relación con otros: a la derecha, debajo, entre. Sirve para dar indicaciones cuando no hay coordenadas.",
    prior=["Sé leer y escribir coordenadas.", "Conozco izquierda, derecha, arriba y abajo."],
    explain=[
        "La localización relativa dice dónde está un objeto en relación con otro. «La escuela está justo a la derecha de la plaza» es relativa, porque necesita saber dónde está la plaza. En cambio, «la escuela está en A3» es absoluta.",
        "Las palabras de ubicación son: a la derecha, a la izquierda, arriba (encima), abajo (debajo) y entre. En el mapa, derecha e izquierda se miran como lo ves tú. «Justo» significa en la casilla vecina, sin ninguna otra entre medio.",
        "Para describir bien, nombra el objeto de referencia y la dirección. Si hay una casilla vacía entre dos objetos, no están «justo» uno al lado del otro. Puedes decir «dos casillas a la derecha».",
    ],
    vocab=[("localización relativa", "dice dónde está un objeto en relación con otro"), ("objeto de referencia", "el objeto desde el cual se describe la ubicación"), ("justo", "en la casilla vecina, sin nada entre medio"), ("encima", "en la casilla de arriba"), ("debajo", "en la casilla de abajo")],
    worked=[
        {"title": "Usar una referencia", "problem": f"{MAPA2} ¿Qué lugar está justo a la derecha de la plaza?", "steps": ["La plaza está en A2.", "Justo a la derecha está la casilla A3.", "En A3 está la escuela."], "answer": "La escuela"},
        {"title": "Absoluta o relativa", "problem": "«La farmacia está en B3» y «La farmacia está debajo de la escuela». ¿Cuál es relativa?", "steps": ["La primera usa una coordenada: es absoluta.", "La segunda usa otro lugar como referencia: es relativa."], "answer": "«La farmacia está debajo de la escuela»"},
    ],
    mistakes=[
        {"wrong": "Decir que la farmacia está justo a la derecha de la panadería (B1 y B3).", "why": "Hay una casilla vacía entre ellas.", "fix": "Justo significa la casilla vecina. La farmacia está dos casillas a la derecha."},
        {"wrong": "Decir que el parque está debajo de la plaza.", "why": "No se comprueba la columna.", "fix": "El parque (B4) está en otra columna que la plaza (A2)."},
    ],
    tiers={
        "recovery": [
            ex(f"{MAPA2} ¿Qué lugar está justo a la derecha de la farmacia?", "El parque", "La farmacia está en B3 y su vecina a la derecha es B4."),
            ex(f"{MAPA2} ¿Qué lugar está justo debajo de la casa?", "La panadería", "La casa está en A1 y debajo está B1."),
            ex(f"{MAPA2} ¿Qué lugar está justo a la derecha de la biblioteca?", "La feria", "La biblioteca está en C2 y a su derecha está C3."),
        ],
        "understand": [
            ex("¿Cuál es relativa: «la farmacia está en B3» o «la farmacia está debajo de la escuela»?", "«La farmacia está debajo de la escuela»", "Usa otro lugar como referencia."),
            ex(f"{MAPA2} ¿Qué lugar está justo a la izquierda del parque?", "La farmacia", "El parque está en B4 y a su izquierda está B3."),
            ex(f"{MAPA2} ¿Qué lugar está entre la casa y la escuela, en la fila A?", "La plaza", "La plaza está en A2, entre A1 y A3."),
        ],
        "apply": [
            ex(f"{MAPA2} ¿Qué lugar está justo encima de la feria?", "La farmacia", "La feria está en C3 y encima está B3."),
            ex(f"{MAPA2} Describe la ubicación del consultorio en relación con la feria.", "Justo a la derecha de la feria", "El consultorio está en C4 y la feria en C3."),
            ex(f"{MAPA2} ¿Qué hay justo debajo de la plaza?", "Nada; la casilla está vacía", "Debajo de A2 está B2, que no tiene lugar."),
        ],
        "reason": [
            ex(f"{MAPA2} Ema dice que la farmacia está justo a la derecha de la panadería. ¿Tiene razón?", "No; hay una casilla vacía entre ellas", "La panadería está en B1 y la farmacia en B3."),
            ex(f"{MAPA2} Hugo dice que el parque está debajo de la plaza. ¿Tiene razón?", "No; están en columnas distintas", "El parque está en B4 y la plaza en A2."),
        ],
        "challenge": [
            ex(f"{MAPA2} Da la ubicación absoluta de la feria y una ubicación relativa que use la farmacia como referencia.", "C3; justo debajo de la farmacia", "La coordenada es absoluta y la referencia a la farmacia es relativa."),
            ex(f"{MAPA2} ¿Cuántos lugares están en casillas vecinas de la farmacia (arriba, abajo, izquierda o derecha)?", "3", "Son la escuela (A3), la feria (C3) y el parque (B4); la casilla B2 está vacía."),
        ],
    },
    context=[ex(f"{MAPA2} Una niña dice: «Nos juntamos en el lugar que está justo a la derecha de la plaza». ¿En qué lugar y qué coordenada?", "En la escuela; A3", "La plaza está en A2 y la casilla vecina es A3.")],
    selfcheck=[
        ex(f"{MAPA2} ¿Qué lugar está justo debajo de la escuela?", "La farmacia", "La escuela está en A3 y debajo está B3."),
        ex(f"{MAPA2} ¿Qué lugar está justo a la izquierda de la feria?", "La biblioteca", "La feria está en C3 y a su izquierda está C2."),
        ex("Si dices «está a la derecha del parque», ¿qué debes nombrar para que se entienda?", "El objeto de referencia", "La ubicación relativa necesita un punto de comparación."),
    ],
    open_task=task(
        "Usa el mapa de este enunciado: " + MAPA2 + " Elige tres lugares y describe dónde está cada uno en relación con otro. Escribe además su coordenada. Una de tus frases debe usar «justo debajo» y otra «justo a la derecha».",
        "La escuela (A3) está justo a la derecha de la plaza. La panadería (B1) está justo debajo de la casa.",
        ["usa un objeto de referencia", "usa las palabras de ubicación", "escribe la coordenada de cada lugar"],
        ["tres frases", "tres coordenadas"],
        ["decir «justo» cuando hay casillas entre medio", "no nombrar la referencia"],
        "Pide que compruebe cada frase en el mapa. Reconoce la diferencia entre ubicación absoluta y relativa.",
    ),
    reinforce="Describe tres objetos de tu escritorio diciendo dónde están en relación con otro objeto.",
    extend="Escribe una frase relativa que sea falsa en el mapa y pide a alguien que encuentre el error.",
)

register(
    OA15, 4,
    materials="Lápiz y papel.",
    use="Aprenderé a escribir rutas claras y a comparar rutas distintas. Sirve para dar indicaciones que todos entiendan igual.",
    prior=["Sé ubicar objetos con coordenadas.", "Sé usar derecha, izquierda, arriba y abajo."],
    explain=[
        "Una ruta es una lista de pasos para ir de un lugar a otro. Una ruta es clara si cada paso dice dos cosas: la dirección y cuántas casillas avanzar. «Ve a la derecha» es ambiguo porque no dice cuántas casillas. «2 casillas a la derecha» es claro.",
        "En este mapa puedes pasar por cualquier casilla. Para ir de la casa (A1) a la biblioteca (C2), una ruta es: 2 casillas hacia abajo y 1 a la derecha. Otra ruta es: 1 a la derecha y 2 hacia abajo. Las dos son válidas y recorren 3 casillas.",
        "Para comparar rutas, cuenta las casillas recorridas. La ruta más corta tiene menos casillas. Al escribir la ruta, usa palabras como arriba, abajo, izquierda y derecha, y un número en cada paso. Revisa en el mapa que llegues al lugar pedido.",
    ],
    vocab=[("ruta", "lista de pasos para ir de un lugar a otro"), ("ambiguo", "que puede entenderse de más de una forma"), ("dirección", "hacia dónde se avanza: arriba, abajo, izquierda o derecha"), ("ruta más corta", "la que recorre menos casillas"), ("paso", "avance en una dirección")],
    worked=[
        {"title": "Seguir una ruta", "problem": f"{MAPA2} Desde la plaza (A2), avanza 1 casilla hacia abajo y 1 a la derecha. ¿Dónde llegas?", "steps": ["1 casilla hacia abajo desde A2 es B2.", "1 casilla a la derecha desde B2 es B3.", "En B3 está la farmacia."], "answer": "La farmacia"},
        {"title": "Detectar ambigüedad", "problem": "«Ve a la derecha y luego baja.» ¿Qué le falta a esta ruta?", "steps": ["No dice cuántas casillas a la derecha.", "Tampoco dice cuántas casillas hacia abajo."], "answer": "Faltan los números de casillas"},
    ],
    mistakes=[
        {"wrong": "Escribir «camina hacia el parque» como ruta.", "why": "No dice dirección ni cantidad de casillas.", "fix": "Escribe pasos como «1 casilla hacia abajo y 3 a la derecha»."},
        {"wrong": "Decir que solo existe una ruta de A1 a B2.", "why": "Se olvida cambiar el orden de los pasos.", "fix": "Hay dos rutas cortas: 1 abajo y 1 derecha, o 1 derecha y 1 abajo."},
    ],
    tiers={
        "recovery": [
            ex(f"{MAPA2} Desde la casa (A1), avanza 2 casillas a la derecha. ¿Dónde llegas?", "A la escuela", "A1 más 2 casillas a la derecha es A3."),
            ex(f"{MAPA2} Desde la biblioteca (C2), avanza 2 casillas a la derecha. ¿Dónde llegas?", "Al consultorio", "C2 más 2 casillas a la derecha es C4."),
            ex(f"{MAPA2} Desde la farmacia (B3), avanza 1 casilla hacia abajo. ¿Dónde llegas?", "A la feria", "Debajo de B3 está C3."),
        ],
        "understand": [
            ex("¿Por qué la instrucción «ve a la derecha» es ambigua?", "No dice cuántas casillas", "Falta la cantidad de casillas."),
            ex("¿Qué dos datos debe tener cada paso de una ruta clara?", "La dirección y la cantidad de casillas", "Con ambos datos se llega al mismo lugar."),
            ex("¿Dos rutas distintas pueden llegar al mismo lugar?", "Sí", "Se pueden cambiar el orden o la forma de los pasos."),
        ],
        "apply": [
            arith("Ruta de la panadería (B1) a la feria (C3): 1 casilla hacia abajo y 2 a la derecha. ¿Cuántas casillas se recorren en total?", "1+2", "Se suman las casillas de cada paso."),
            arith("¿Cuántas casillas tiene la ruta más corta de la plaza (A2) al consultorio (C4)? Son 2 hacia abajo y 2 a la derecha.", "2+2", "Se suman las casillas de cada paso."),
            arith("¿Cuántas casillas tiene la ruta más corta de la casa (A1) al parque (B4)? Son 1 hacia abajo y 3 a la derecha.", "1+3", "Se suman las casillas de cada paso."),
        ],
        "reason": [
            ex("Un compañero dice «sigue derecho un rato y gira». ¿Qué falta para que sea una ruta clara?", "Cuántas casillas y hacia dónde girar", "Una ruta clara indica dirección y cantidad."),
            ex(f"{MAPA2} Luis escribe «2 derecha, 1 abajo» y Ana escribe «1 abajo, 2 derecha» desde la casa (A1) hacia la farmacia. ¿Llegan las dos rutas?", "Sí, ambas llegan a B3", "Las dos suman 2 a la derecha y 1 hacia abajo."),
        ],
        "challenge": [
            arith("Desde la biblioteca (C2) hasta la casa (A1), la ruta más corta es 2 casillas hacia arriba y 1 a la izquierda. ¿Cuántas casillas son?", "2+1", "Se suman los pasos de la ruta."),
            ex("De la casa (A1) a la casilla B2 hay que ir 1 abajo y 1 a la derecha. ¿Cuántas rutas cortas distintas hay?", "2", "Puedes empezar con el paso hacia abajo o con el paso a la derecha."),
        ],
    },
    context=[ex("Para ir de la casa a la panadería (B1), un amigo dice dos instrucciones. A) «Camina un poco hacia abajo». B) «Avanza 1 casilla hacia abajo». ¿Cuál es la instrucción clara?", "B", "Dice dirección y cantidad de casillas.")],
    selfcheck=[
        ex(f"{MAPA2} Desde la escuela (A3), avanza 1 casilla hacia abajo y 1 a la derecha. ¿Dónde llegas?", "Al parque", "Llegas a B3 y luego a B4."),
        arith("¿Cuántas casillas tiene una ruta de 3 casillas a la derecha y 2 hacia abajo?", "3+2", "Se suman los dos pasos."),
        ex("¿La ruta «2 abajo y luego izquierda» es clara?", "No", "No dice cuántas casillas a la izquierda."),
    ],
    open_task=task(
        "Usa el mapa: " + MAPA2 + " Escribe una ruta clara de la casa (A1) al consultorio (C4) y otra ruta distinta al mismo lugar. Cuenta las casillas de cada una y di cuál es la más corta, o si son iguales.",
        "Ruta 1: 3 casillas a la derecha y 2 hacia abajo (5 casillas). Ruta 2: 2 hacia abajo y 3 a la derecha (5 casillas). Son iguales.",
        ["cada paso tiene dirección y número", "llega al lugar pedido", "cuenta las casillas de cada ruta", "compara las rutas"],
        ["dos rutas", "conteo"],
        ["pasos ambiguos", "contar mal las casillas"],
        "Pide que siga la ruta de otra persona con el dedo. Reconoce rutas sin ambigüedad.",
    ),
    reinforce="Escribe una ruta clara de tu cama a la puerta de tu casa, con pasos en casillas de baldosa o de pasos pequeños.",
    extend="Escribe una ruta que pase por dos lugares del mapa antes de llegar al tercero.",
)
