"""Student material for 2.º básico Matemática, OA 10 (familias de operaciones) y OA 11 (multiplicación y tablas del 2, 5 y 10)."""
from __future__ import annotations

from student_content_ma02_f import task
from student_lessons import arith, ex, register

OA10 = "MA02 OA 10"
OA11 = "MA02 OA 11"


def grp(groups: int, each: int) -> str:
    """Grupos iguales dibujados en texto: (●●) (●●) ..."""
    return " ".join("(" + "●" * each + ")" for _ in range(groups))


def rep(each: int, groups: int) -> str:
    return " + ".join(str(each) for _ in range(groups))


# ------------------------------------------------------------------ OA 10
register(
    OA10, 1,
    materials="Fichas o botones de dos colores, una hoja con un dibujo de todo y partes (un óvalo grande con dos óvalos pequeños) y lápiz. Los números están en los ejercicios.",
    use="Aprenderé a ver tres números como una familia: dos partes y un todo. Sirve para saber qué sumas y qué restas se relacionan.",
    prior=["Sé sumar y restar hasta 20.", "Sé que juntar dos partes forma un todo."],
    explain=[
        "Un todo se puede separar en dos partes. Si tienes 8 fichas rojas y 5 fichas azules, las partes son 8 y 5. El todo son las 13 fichas juntas. Los tres números, 8, 5 y 13, forman una familia.",
        "En una familia, el todo es el número más grande. Se obtiene sumando las dos partes: 8 + 5 = 13. Si conoces el todo y una parte, la otra parte se obtiene restando: 13 − 8 = 5.",
        "No todo trío de números es una familia. Para serlo, las dos partes deben sumar el todo. Los números 8, 5 y 14 no forman familia, porque 8 + 5 no es 14. Dibuja un óvalo grande para el todo y dos óvalos chicos para las partes.",
    ],
    vocab=[("todo", "la cantidad completa"), ("parte", "una de las dos cantidades que forman el todo"), ("familia de operaciones", "tres números que se relacionan con sumas y restas"), ("sumar", "juntar las partes para hallar el todo"), ("restar", "quitar una parte del todo para hallar la otra")],
    worked=[
        {"title": "Hallar el todo", "problem": "Hay 8 fichas rojas y 5 fichas azules. ¿Cuál es el todo?", "steps": ["Las partes son 8 y 5.", "El todo se obtiene sumando las partes: 8 + 5.", "8 + 5 = 13.", "La familia es 8, 5 y 13, y el todo es 13."], "answer": "El todo es 13"},
        {"title": "Hallar una parte", "problem": "El todo es 15 y una parte es 6. ¿Cuál es la otra parte?", "steps": ["Conozco el todo: 15, y una parte: 6.", "La otra parte se halla restando: 15 − 6.", "15 − 6 = 9.", "Compruebo: 6 + 9 = 15."], "answer": "La otra parte es 9"},
    ],
    mistakes=[
        {"wrong": "Decir que en la familia 9, 4 y 13 el todo es 9.", "why": "Se elige el primer número sin ver qué números suman cuál.", "fix": "El todo es el mayor: 9 + 4 = 13."},
        {"wrong": "Decir que 6, 7 y 15 son una familia.", "why": "No se comprueba que las partes sumen el todo.", "fix": "6 + 7 = 13 y no 15, entonces no es una familia."},
    ],
    tiers={
        "recovery": [
            arith("Las partes son 8 y 5. ¿Cuánto es el todo?", "8+5", "El todo se halla sumando las partes."),
            ex("En la familia 9, 4 y 13, ¿cuál es el todo?", "13", "El todo es el número mayor y 9 + 4 = 13."),
            arith("El todo es 15 y una parte es 6. ¿Cuánto es la otra parte?", "15-6", "La otra parte se halla restando."),
        ],
        "understand": [
            ex("¿Cuáles tres números forman una familia: 7, 6 y 13, o 7, 6 y 14?", "7, 6 y 13", "7 + 6 = 13."),
            ex("En la familia 5, 9 y 14, ¿cuáles son las partes?", "5 y 9", "Las partes suman el todo: 5 + 9 = 14."),
            ex("¿Cuál es el todo de la familia 4, 8 y 12?", "12", "El todo es el número mayor."),
        ],
        "apply": [
            arith("Las partes son 7 y 6. ¿Cuál es el todo?", "7+6", "Las partes se suman."),
            arith("El todo es 17 y una parte es 9. ¿Cuál es la otra parte?", "17-9", "Del todo se quita la parte conocida."),
            ex("Escribe los tres números de la familia con las partes 3 y 12.", "3, 12 y 15", "3 + 12 = 15."),
        ],
        "reason": [
            ex("Pablo dice que 6, 7 y 15 son una familia. ¿Tiene razón?", "No; 6 + 7 = 13 y no 15", "Las partes deben sumar el todo."),
            ex("En una familia, ¿el todo es el número mayor o el menor? Explica.", "El mayor, porque junta las dos partes", "El todo es siempre más grande que cada parte."),
        ],
        "challenge": [
            ex("Dos partes suman 18 y una parte es el doble de la otra. ¿Cuáles son las partes?", "6 y 12", "6 + 12 = 18 y 12 es el doble de 6."),
            ex("Escribe una familia con todo 10 que tenga las partes distintas.", "Por ejemplo 3, 7 y 10 (también 1, 9 y 10; 2, 8 y 10; 4, 6 y 10)", "Dos partes distintas deben sumar 10."),
        ],
    },
    context=[arith("En una caja hay 8 lápices rojos y 5 lápices azules. ¿Cuántos lápices hay en total? El total es el todo.", "8+5", "Se juntan las dos partes.")],
    selfcheck=[arith("Las partes son 9 y 6. ¿Cuánto es el todo?", "9+6", "El todo se halla sumando."), arith("El todo es 12 y una parte es 5. ¿Cuánto es la otra parte?", "12-5", "Se resta la parte conocida."), ex("¿Forman familia 5, 8 y 14?", "No", "5 + 8 = 13 y no 14.")],
    open_task=task(
        "En una caja hay 12 botones: 7 son rojos y el resto son azules. Dibuja un óvalo grande para el todo y dos óvalos pequeños para las partes. Escribe los tres números de la familia, cuántos botones azules hay y la suma que lo comprueba.",
        "Todo: 12. Partes: 7 y 5. Los botones azules son 12 − 7 = 5. Comprobación: 7 + 5 = 12. Familia: 7, 5 y 12.",
        ["escribe el todo y las dos partes", "obtiene 5 botones azules", "comprueba con la suma 7 + 5 = 12", "dibuja los óvalos"],
        ["dibujo del todo y las partes", "resta", "suma de comprobación"],
        ["elegir una parte como todo", "no comprobar que las partes sumen el todo"],
        "Pide que señale en el dibujo cuál es el todo y cuáles las partes; reconoce que comprueba con la suma.",
    ),
    reinforce="Con 10 fichas de dos colores, forma tres familias distintas y escribe cada una con sus tres números.",
    extend="Escribe cuatro familias con todo 14 y una parte entre 3 y 8.",
)

register(
    OA10, 2,
    materials="Fichas o botones de dos colores, una hoja con el dibujo de todo y partes y lápiz. Los números están en los ejercicios.",
    use="Aprenderé que desde una familia puedo escribir dos sumas. Sirve para ver que cambiar el orden de las partes no cambia el todo.",
    prior=["Sé que una familia tiene dos partes y un todo.", "Sé sumar hasta 20."],
    explain=[
        "Con una familia puedes escribir dos sumas. Si las partes son 6 y 4, y el todo es 10, puedes escribir 6 + 4 = 10 y también 4 + 6 = 10. Cambias el orden de las partes, pero el todo es el mismo.",
        "Esto pasa porque juntar 6 fichas rojas con 4 azules da lo mismo que juntar 4 azules con 6 rojas. Son las mismas fichas. Por eso las dos sumas dan 10.",
        "Cuando las dos partes son iguales, solo hay una suma. Por ejemplo, con 5 y 5 el todo es 10 y solo escribes 5 + 5 = 10. Siempre empieza por ver cuál es el todo, y luego escribe las sumas con las partes.",
    ],
    vocab=[("suma", "operación que junta las partes"), ("orden", "el lugar donde pones cada número"), ("partes iguales", "las dos partes valen lo mismo"), ("todo", "resultado de la suma"), ("familia", "tres números relacionados por sumas y restas")],
    worked=[
        {"title": "Dos sumas de la misma familia", "problem": "La familia es 6, 4 y 10. Escribe las sumas.", "steps": ["Las partes son 6 y 4. El todo es 10.", "Primera suma: 6 + 4 = 10.", "Cambio el orden de las partes: 4 + 6 = 10.", "Las dos dan el mismo todo."], "answer": "6 + 4 = 10 y 4 + 6 = 10"},
        {"title": "Partes iguales", "problem": "La familia es 5, 5 y 10. ¿Cuántas sumas distintas hay?", "steps": ["Las dos partes son iguales: 5 y 5.", "Si cambio el orden sigo escribiendo 5 + 5.", "Solo hay una suma: 5 + 5 = 10.", "Esa familia tiene una sola suma."], "answer": "Una suma: 5 + 5 = 10"},
    ],
    mistakes=[
        {"wrong": "Decir que 6 + 4 da 10 pero que 4 + 6 da 11.", "why": "Se cree que el orden cambia el resultado.", "fix": "Cambiar el orden no cambia el total: 4 + 6 = 10."},
        {"wrong": "Escribir 10 + 4 = 6 como suma de la familia.", "why": "Se pone el todo como si fuera una parte.", "fix": "En la suma, las partes van primero y el todo al final: 6 + 4 = 10."},
    ],
    tiers={
        "recovery": [
            arith("Calcula 6 + 4.", "6+4", "Las partes 6 y 4 forman 10."),
            arith("Calcula 4 + 6.", "4+6", "El orden no cambia el todo."),
            ex("En la familia 7, 3 y 10, ¿cuáles son las partes?", "7 y 3", "El todo es 10."),
        ],
        "understand": [
            ex("Si 8 + 7 = 15, ¿cuánto es 7 + 8?", "15", "Es la misma familia con las partes en otro orden."),
            ex("¿Qué dos sumas salen de la familia 9, 6 y 15?", "9 + 6 = 15 y 6 + 9 = 15", "Se cambia el orden de las partes."),
            ex("¿Cuántas sumas distintas tiene la familia 4, 4 y 8?", "Una", "Las dos partes son iguales."),
        ],
        "apply": [
            ex("Escribe las dos sumas de la familia 5, 9 y 14.", "5 + 9 = 14 y 9 + 5 = 14", "Se cambia el orden de las partes."),
            ex("Escribe las dos sumas de la familia 8, 3 y 11.", "8 + 3 = 11 y 3 + 8 = 11", "Se cambia el orden de las partes."),
            ex("Completa: 13 + 2 = 15 y 2 + __ = 15.", "13", "Es la misma familia con las partes cambiadas."),
        ],
        "reason": [
            ex("Marta dice que 6 + 9 es 15 y 9 + 6 es 16. ¿Qué error comete?", "Cree que el orden cambia el todo; las dos dan 15", "Son las mismas partes."),
            ex("¿Por qué la familia 7, 7 y 14 tiene una sola suma?", "Porque sus dos partes son iguales", "7 + 7 es la única suma posible."),
        ],
        "challenge": [
            ex("Escribe las dos sumas con las partes 12 y 8.", "12 + 8 = 20 y 8 + 12 = 20", "Cambiar el orden no cambia el todo."),
            ex("Una familia tiene el todo 16 y una parte 9. Escribe sus dos sumas.", "9 + 7 = 16 y 7 + 9 = 16", "La otra parte es 16 − 9 = 7."),
        ],
    },
    context=[ex("Tengo 6 canicas verdes y 4 canicas amarillas. Escribe dos sumas distintas que digan cuántas canicas tengo.", "6 + 4 = 10 y 4 + 6 = 10", "Es la misma familia con las partes en otro orden.")],
    selfcheck=[ex("Escribe las dos sumas de la familia 3, 9 y 12.", "3 + 9 = 12 y 9 + 3 = 12", "Se cambia el orden."), arith("Calcula 9 + 8.", "9+8", "Las partes 9 y 8 forman 17."), ex("¿Cuántas sumas distintas tiene 6, 6 y 12?", "Una", "Las partes son iguales.")],
    open_task=task(
        "Mira estas tres familias: 7, 4 y 11; 9, 9 y 18; 5, 8 y 13. Para cada una escribe las sumas que existen y explica en una frase por qué no cambia el todo al cambiar el orden. Dibuja con ● y ○ la familia 7, 4 y 11.",
        "7, 4 y 11: 7 + 4 = 11 y 4 + 7 = 11. 9, 9 y 18: solo 9 + 9 = 18. 5, 8 y 13: 5 + 8 = 13 y 8 + 5 = 13. No cambia porque son las mismas fichas. Dibujo: ●●●●●●● ○○○○ (7 y 4).",
        ["escribe dos sumas cuando las partes son distintas", "escribe una suma cuando las partes son iguales", "explica por qué el todo no cambia", "dibuja la familia 7, 4 y 11"],
        ["sumas escritas", "dibujo", "frase de explicación"],
        ["creer que el orden cambia el total", "escribir el todo como parte"],
        "Pide que junte las fichas dibujadas en los dos órdenes y confirme que el total es igual.",
    ),
    reinforce="Con 9 fichas rojas y 6 azules, cuéntalas juntas y escribe las dos sumas.",
    extend="Escribe cuatro familias con todo 18 y las dos sumas de cada una.",
)

register(
    OA10, 3,
    materials="Fichas o botones, una hoja con el dibujo de todo y partes y lápiz. Los números están en los ejercicios.",
    use="Aprenderé que desde una familia puedo escribir dos restas que parten del todo. Sirve para hallar una parte que no conozco.",
    prior=["Sé que una familia tiene dos sumas.", "Sé restar hasta 20."],
    explain=[
        "Con una familia puedes escribir dos restas. Parte siempre del todo. Si el todo es 15 y las partes son 7 y 8, entonces 15 − 7 = 8 y 15 − 8 = 7. En cada resta quitas una parte y queda la otra.",
        "Por eso una resta se puede pensar como una suma que falta. En 15 − 7 = 8, preguntas: 7 más, ¿cuánto, para llegar a 15? Faltan 8. La familia 7, 8 y 15 tiene dos sumas y dos restas.",
        "En una resta de la familia, el primer número es siempre el todo, porque no puedes quitar más de lo que tienes. Si las partes son iguales, como 6 y 6, solo hay una resta: 12 − 6 = 6.",
    ],
    vocab=[("resta", "operación que quita una parte del todo"), ("todo", "el número más grande de la familia"), ("parte", "uno de los dos números chicos de la familia"), ("falta", "lo que hay que sumar para llegar al todo"), ("familia completa", "las dos sumas y las dos restas")],
    worked=[
        {"title": "Dos restas desde el todo", "problem": "La familia es 7, 8 y 15. Escribe las restas.", "steps": ["El todo es 15, el número más grande.", "Quito una parte: 15 − 7 = 8.", "Quito la otra: 15 − 8 = 7.", "Cada resta recupera la otra parte."], "answer": "15 − 7 = 8 y 15 − 8 = 7"},
        {"title": "Una resta con partes iguales", "problem": "La familia es 6, 6 y 12. Escribe las restas.", "steps": ["El todo es 12 y las partes son 6 y 6.", "Quito una parte: 12 − 6 = 6.", "La otra resta sería la misma.", "Solo hay una resta distinta."], "answer": "12 − 6 = 6"},
    ],
    mistakes=[
        {"wrong": "Escribir 7 − 15 = 8 como resta de la familia.", "why": "Se pone una parte primero y no hay cómo quitar 15 de 7.", "fix": "La resta parte del todo: 15 − 7 = 8."},
        {"wrong": "Escribir 15 − 7 = 22 porque «las familias suman».", "why": "Se suma en lugar de restar.", "fix": "La resta quita una parte: 15 − 7 = 8."},
    ],
    tiers={
        "recovery": [
            arith("Calcula 15 − 7.", "15-7", "Se quita una parte del todo."),
            arith("Calcula 15 − 8.", "15-8", "Se quita la otra parte."),
            ex("En la familia 6, 9 y 15, ¿con qué número empiezan las restas?", "15", "Las restas parten del todo."),
        ],
        "understand": [
            ex("Si 6 + 9 = 15, ¿cuánto es 15 − 6?", "9", "La resta recupera la otra parte."),
            ex("¿Qué dos restas salen de la familia 5, 8 y 13?", "13 − 5 = 8 y 13 − 8 = 5", "Se parte del todo y se quita cada parte."),
            ex("¿Cuántas restas distintas tiene la familia 7, 7 y 14?", "Una", "Las dos partes son iguales."),
        ],
        "apply": [
            arith("Calcula 17 − 9 pensando que la familia es 9, 8 y 17.", "17-9", "Del todo se quita una parte."),
            arith("Calcula 14 − 6 pensando que la familia es 6, 8 y 14.", "14-6", "Del todo se quita una parte."),
            ex("Escribe las dos restas de la familia 4, 9 y 13.", "13 − 4 = 9 y 13 − 9 = 4", "Se parte del todo."),
        ],
        "reason": [
            ex("Beto escribió 7 − 15 = 8 para la familia 7, 8 y 15. ¿Qué error cometió y cómo se corrige?", "Empezó por una parte; se corrige a 15 − 7 = 8", "Las restas parten del todo."),
            ex("¿Cuántas sumas y cuántas restas tiene la familia 3, 9 y 12?", "Dos sumas y dos restas", "Las partes son distintas."),
        ],
        "challenge": [
            ex("La familia es 5, 12 y 17. Escribe sus dos sumas y sus dos restas.", "5 + 12 = 17, 12 + 5 = 17, 17 − 5 = 12 y 17 − 12 = 5", "Con partes distintas hay dos de cada una."),
            ex("Hay 20 hojas. Se gastan 11. Escribe la resta y la suma que comprueba.", "20 − 11 = 9 y 9 + 11 = 20", "La suma devuelve al todo."),
        ],
    },
    context=[arith("En un paquete hay 15 galletas. Te comes 7. ¿Cuántas galletas quedan?", "15-7", "Quedan las que no te comiste.")],
    selfcheck=[arith("Calcula 13 − 5.", "13-5", "5 + 8 = 13."), ex("¿Con qué número empiezan las restas de la familia 8, 6 y 14?", "14", "El todo va primero."), ex("Si 9 + 4 = 13, ¿cuánto es 13 − 4?", "9", "La resta recupera la otra parte.")],
    open_task=task(
        "Mira estas dos familias: 8, 6 y 14; y 9, 9 y 18. Para cada una escribe sus sumas y sus restas. Dibuja con ● el todo de la primera familia y tacha con una cruz una de las partes para mostrar la resta.",
        "8, 6 y 14: 8 + 6 = 14, 6 + 8 = 14, 14 − 8 = 6 y 14 − 6 = 8. 9, 9 y 18: 9 + 9 = 18 y 18 − 9 = 9. Dibujo: ●●●●●●●●●●●●●● y se tachan 8 para quedar 6.",
        ["escribe dos sumas y dos restas para la primera familia", "escribe una suma y una resta para la segunda", "dibuja y tacha la parte"],
        ["operaciones escritas", "dibujo con tachado"],
        ["empezar la resta por una parte", "no ver que las partes iguales dan una sola resta"],
        "Pide que explique en voz alta qué número queda cuando tacha cada parte.",
    ),
    reinforce="Con 12 fichas, quita 5 y cuenta las que quedan. Después vuelve a juntar y escribe la suma que lo comprueba.",
    extend="Escribe dos familias con todo 16 y sus dos sumas y dos restas.",
)

register(
    OA10, 4,
    materials="Hojas y lápiz. Todas las cuentas están escritas en los ejercicios. Los números llegan hasta 100 y no hay que cambiar decenas.",
    use="Aprenderé a comprobar una resta con una suma de su familia y a revisar mis resultados. Sirve para saber si me equivoqué antes de entregar mi trabajo.",
    prior=["Sé que una familia tiene dos sumas y dos restas.", "Sé sumar y restar números de dos cifras sin cambiar decenas."],
    explain=[
        "La familia te ayuda a revisar tus cuentas. Si hiciste 63 − 21 = 42, comprueba con la suma de la familia: 42 + 21 debe dar 63. Si da 63, tu resta está bien.",
        "Si la suma no devuelve el todo, hay un error. Por ejemplo, si escribes 63 − 21 = 52, calcula 52 + 21 = 73. Eso no es 63. Entonces 52 no puede ser el resultado y debes revisar la resta.",
        "También puedes comprobar una suma con una resta. Si hiciste 34 + 25 = 59, resta 59 − 25. Debe dar 34. Esta revisión funciona con cualquier familia, incluso con números de dos cifras.",
    ],
    vocab=[("comprobar", "revisar si un resultado es correcto"), ("operación contraria", "la que deshace a otra"), ("error", "resultado que no coincide con la comprobación"), ("revisar", "mirar de nuevo con cuidado"), ("familia", "tres números que se relacionan con sumas y restas")],
    worked=[
        {"title": "Comprobar una resta con una suma", "problem": "Resolviste 63 − 21 = 42. ¿Está bien?", "steps": ["La familia es 63, 21 y 42.", "Comprobación: 42 + 21.", "2 + 1 = 3 unidades y 4 + 2 = 6 decenas: 63.", "Volvió al todo, entonces 63 − 21 = 42 está bien."], "answer": "Está bien"},
        {"title": "Encontrar un error", "problem": "Resolviste 63 − 21 = 52. ¿Está bien?", "steps": ["Comprobación: 52 + 21.", "2 + 1 = 3 unidades y 5 + 2 = 7 decenas: 73.", "73 no es 63, el todo.", "Hay un error. El resultado correcto es 42."], "answer": "Está mal; es 42"},
    ],
    mistakes=[
        {"wrong": "Comprobar 63 − 21 = 42 con 42 − 21.", "why": "Se resta otra vez en vez de usar la suma de la familia.", "fix": "La comprobación es una suma: 42 + 21 = 63."},
        {"wrong": "Comprobar 34 + 25 = 59 con 59 + 25.", "why": "Se suma otra vez.", "fix": "La comprobación de una suma es una resta: 59 − 25 = 34."},
    ],
    tiers={
        "recovery": [
            arith("Comprueba 63 − 21 = 42 calculando 42 + 21.", "42+21", "Debe volver al 63."),
            arith("Comprueba 34 + 25 = 59 calculando 59 − 25.", "59-25", "Debe volver al 34."),
            ex("Si 45 − 12 = 33, ¿qué suma lo comprueba?", "33 + 12 = 45", "La suma devuelve al todo."),
        ],
        "understand": [
            ex("La suma de comprobación 52 + 21 da 73, y el todo era 63. ¿La resta estaba bien?", "No", "Debe dar el todo, 63."),
            ex("¿Con qué operación se comprueba 84 + 13 = 97?", "Con la resta 97 − 13 = 84", "La resta deshace la suma."),
            ex("Si 56 + 21 = 77, ¿cuánto es 77 − 21?", "56", "La resta recupera una parte."),
        ],
        "apply": [
            arith("Resuelve 78 − 35 y comprueba con la suma. Escribe solo el resultado de la resta.", "78-35", "8 − 5 = 3 unidades y 7 − 3 = 4 decenas."),
            arith("Resuelve 41 + 36 y comprueba con la resta. Escribe solo el resultado de la suma.", "41+36", "1 + 6 = 7 unidades y 4 + 3 = 7 decenas."),
            ex("Comprueba si 89 − 54 = 35 está bien. Escribe la suma de comprobación y di sí o no.", "35 + 54 = 89; sí está bien", "9 − 4 = 5 y 8 − 5 = 3 dan 35."),
        ],
        "reason": [
            ex("Pía resolvió 75 − 32 = 53 y comprobó con 53 + 32 = 85. ¿Qué descubrió y cuál es el resultado correcto?", "Que hay un error, porque 85 no es 75; el resultado correcto es 43", "5 − 2 = 3 unidades y 7 − 3 = 4 decenas."),
            ex("¿Por qué una suma de comprobación puede mostrar un error en una resta?", "Porque si la suma no devuelve el todo, la resta está mal", "La suma debe deshacer la resta."),
        ],
        "challenge": [
            ex("En una feria había 98 globos y se vendieron 36. ¿Cuántos globos quedan? Escribe la resta, su resultado y la suma de comprobación.", "98 − 36 = 62 y 62 + 36 = 98", "8 − 6 = 2 unidades y 9 − 3 = 6 decenas."),
            ex("Tres compañeros resolvieron 69 − 24: Ana dice 45, Beto dice 55 y Carla dice 35. ¿Quién tiene razón y cómo lo sabes?", "Ana; 45 + 24 = 69", "9 − 4 = 5 unidades y 6 − 2 = 4 decenas."),
        ],
    },
    context=[arith("Una tienda tenía 67 manzanas y vendió 23. Dice que quedan 44. Comprueba calculando 44 + 23. ¿Qué número obtienes?", "44+23", "Debe volver a las 67 manzanas.")],
    selfcheck=[ex("Si 52 − 31 = 21, ¿qué suma lo comprueba?", "21 + 31 = 52", "La suma devuelve el todo."), arith("Comprueba 46 + 23 = 69 calculando 69 − 23.", "69-23", "Debe volver al 46."), ex("¿Una resta está bien si la suma de comprobación no da el todo?", "No", "Debe dar el todo.")],
    open_task=task(
        "Resuelve estas dos cuentas y comprueba cada una con una operación de su familia: 86 − 43 y 32 + 45. Una compañera escribió 86 − 43 = 53; revisa si está bien y corrígela.",
        "86 − 43 = 43, y la comprobación es 43 + 43 = 86. 32 + 45 = 77, y la comprobación es 77 − 45 = 32. La compañera se equivocó: 53 + 43 = 96, que no es 86. El resultado correcto es 43.",
        ["resuelve ambas cuentas", "comprueba con la operación de la familia", "descubre el error de 53 con una suma"],
        ["resultados", "comprobaciones", "corrección"],
        ["comprobar con la misma operación", "no ver que la suma no devuelve el todo"],
        "Pide que explique cómo sabe que 53 está mal sin recalcular desde cero; reconoce el uso de la familia.",
    ),
    reinforce="Escribe una resta de dos cifras en una tarjeta, resuélvela y comprueba con la suma de su familia.",
    extend="Inventa una resta con un error y pide a otra persona que lo descubra con una suma de comprobación.",
)

# ------------------------------------------------------------------ OA 11
register(
    OA11, 1,
    materials="12 fichas o botones, platos o papeles para agrupar y lápiz. Los grupos están dibujados en el cuaderno con ●.",
    use="Aprenderé a reconocer grupos iguales y a escribirlos como una suma repetida y como una multiplicación. Sirve para contar rápido cuando hay muchos grupos con lo mismo.",
    prior=["Sé sumar números pequeños.", "Sé contar de 2 en 2."],
    explain=[
        "Un grupo es un conjunto de objetos. Los grupos son iguales cuando cada uno tiene la misma cantidad. Cuatro platos con 2 fichas cada uno son grupos iguales. Platos con 2, 3, 2 y 1 fichas no lo son.",
        f"Con grupos iguales puedes sumar el mismo número varias veces: {grp(4, 2)}. Eso es 2 + 2 + 2 + 2 = 8. Una forma más corta es la multiplicación: 4 × 2 = 8. Se lee «cuatro veces dos es ocho». El primer número dice cuántos grupos y el segundo, cuántos hay en cada grupo.",
        "La multiplicación es una suma repetida de sumandos iguales. Si los grupos no son iguales, no sirve. Antes de multiplicar, mira que todos los grupos tengan lo mismo.",
    ],
    vocab=[("grupo", "conjunto de objetos"), ("grupos iguales", "cada grupo tiene la misma cantidad"), ("suma repetida", "sumar muchas veces el mismo número"), ("multiplicación", "operación que repite un grupo varias veces; se escribe con ×"), ("producto", "resultado de una multiplicación")],
    worked=[
        {"title": "Cuatro grupos iguales", "problem": f"Mira {grp(4, 2)}. ¿Son grupos iguales? ¿Cuántas fichas hay?", "steps": ["Cuento las fichas de cada grupo: 2, 2, 2 y 2.", "Todos tienen lo mismo: son grupos iguales.", "Sumo: 2 + 2 + 2 + 2 = 8.", "Escribo la multiplicación: 4 × 2 = 8."], "answer": "Sí; 4 × 2 = 8"},
        {"title": "Grupos desiguales", "problem": "Mira (●●) (●●●) (●●) (●). ¿Se puede escribir como multiplicación?", "steps": ["Cuento cada grupo: 2, 3, 2 y 1.", "No todos tienen lo mismo.", "Los grupos no son iguales.", "No se puede escribir como una multiplicación."], "answer": "No, los grupos no son iguales"},
    ],
    mistakes=[
        {"wrong": "Escribir 4 × 2 como 4 + 2 = 6.", "why": "Se suman los dos números en vez de repetir el grupo.", "fix": "4 × 2 es 4 grupos de 2: 2 + 2 + 2 + 2 = 8."},
        {"wrong": "Escribir 2 + 3 + 2 + 1 como 4 × 2.", "why": "Los sumandos no son iguales.", "fix": "La multiplicación solo sirve cuando todos los grupos son iguales."},
    ],
    tiers={
        "recovery": [
            ex(f"Mira {grp(4, 2)}. ¿Son grupos iguales? ¿Cuántos grupos hay y cuántas fichas en cada uno?", "Sí; 4 grupos de 2", "Todos los grupos tienen 2 fichas."),
            arith("Hay 4 grupos de 2 fichas. Calcula 2 + 2 + 2 + 2.", "2+2+2+2", "Se suma cuatro veces el 2."),
            ex("Escribe 3 + 3 + 3 como grupos. ¿Cuántos grupos y de cuánto?", "3 grupos de 3", "Hay tres veces el mismo número."),
        ],
        "understand": [
            ex("Mira (●●) (●●●) (●●) (●). ¿Son grupos iguales?", "No; tienen 2, 3, 2 y 1", "No todos los grupos tienen la misma cantidad."),
            ex("¿Cómo se escribe con una multiplicación 4 grupos de 2?", "4 × 2", "El primer número es la cantidad de grupos."),
            ex("¿Qué suma repetida representa 3 × 5?", "5 + 5 + 5", "Hay 3 grupos de 5."),
        ],
        "apply": [
            arith("Calcula 3 × 4 usando 4 + 4 + 4.", "3*4", "Hay 3 grupos de 4."),
            ex("Hay 5 platos con 3 galletas cada uno. Escribe la suma repetida y la multiplicación.", "3 + 3 + 3 + 3 + 3 = 15 y 5 × 3 = 15", "Son 5 grupos iguales de 3."),
            arith("En 6 bolsas hay 2 manzanas en cada una. ¿Cuántas manzanas hay?", "6*2", "Son 6 grupos iguales de 2."),
        ],
        "reason": [
            ex("Una niña dice que 2 + 3 + 2 es lo mismo que 3 × 2. ¿Qué error comete?", "Los sumandos no son iguales, así que no es multiplicación; 2 + 3 + 2 = 7 y 3 × 2 = 6", "Solo se puede multiplicar con sumandos iguales."),
            ex("¿Hay más fichas en 4 grupos de 3 o en 3 grupos de 4?", "Hay las mismas; en ambos casos son 12", "3 + 3 + 3 + 3 = 12 y 4 + 4 + 4 = 12."),
        ],
        "challenge": [
            ex("Escribe dos multiplicaciones distintas con grupos iguales cuyo producto sea 12.", "Por ejemplo 2 × 6 y 3 × 4 (también 4 × 3, 6 × 2)", "Los grupos iguales deben sumar 12."),
            arith("Hay 5 grupos de 2 fichas y 3 grupos más de 2 fichas. ¿Cuántas fichas hay en total?", "5*2+3*2", "Son 8 grupos de 2: 10 + 6."),
        ],
    },
    context=[arith("En una mesa hay 4 platos con 2 galletas cada uno. ¿Cuántas galletas hay?", "4*2", "Son 4 grupos iguales de 2.")],
    selfcheck=[arith("Calcula 3 × 2.", "3*2", "Son 3 grupos de 2."), ex("¿Qué debe cumplirse para escribir una suma como multiplicación?", "Que todos los sumandos sean iguales", "La multiplicación repite el mismo grupo."), ex("Escribe 2 + 2 + 2 + 2 + 2 como multiplicación.", "5 × 2", "Hay 5 grupos de 2.")],
    open_task=task(
        "Hay tres situaciones. A) 3 platos con 4 fichas cada uno. B) Platos con 2, 4 y 3 fichas. C) 5 vasos con 2 palitos cada uno. Dibuja cada situación con ●. Di cuál no es de grupos iguales. Para las otras escribe la suma repetida y la multiplicación.",
        "A) (●●●●) (●●●●) (●●●●): 4 + 4 + 4 = 12 y 3 × 4 = 12. B) (●●) (●●●●) (●●●): no son iguales (2, 4 y 3). C) (●●) (●●) (●●) (●●) (●●): 2 + 2 + 2 + 2 + 2 = 10 y 5 × 2 = 10.",
        ["dibuja los grupos", "detecta que B no es de grupos iguales", "escribe 3 × 4 = 12 y 5 × 2 = 10", "escribe las sumas repetidas"],
        ["dibujos", "sumas repetidas", "multiplicaciones"],
        ["multiplicar con grupos desiguales", "sumar los dos números de la multiplicación"],
        "Pide que cuente en voz alta las fichas de cada grupo antes de decidir; reconoce que revisa que sean iguales.",
    ),
    reinforce="Con 12 botones, haz 3 grupos iguales y luego 4 grupos iguales. Escribe cuántos botones hay en cada grupo.",
    extend="Escribe tres situaciones de tu casa con grupos iguales (por ejemplo, patas de sillas) y escribe cada una como suma repetida.",
)

register(
    OA11, 2,
    materials="Parejas dibujadas con ●● en este cuaderno, lápiz y una lista de números del 2 al 20. Todo lo necesario está en los ejercicios.",
    use="Aprenderé la tabla del 2 como dobles de los números. Sirve para contar pares de zapatos, guantes u ojos sin ir de uno en uno.",
    prior=["Sé qué es el doble de un número.", "Sé escribir una multiplicación como suma repetida."],
    explain=[
        "La tabla del 2 sirve para contar cosas que vienen de a pares: zapatos, guantes, ojos, ruedas de bicicleta. Cada par tiene 2. Cinco pares son 5 grupos de 2: 2 + 2 + 2 + 2 + 2 = 10. Se escribe 5 × 2 = 10.",
        "Los resultados de la tabla del 2 son dobles. 1 × 2 = 2, 2 × 2 = 4, 3 × 2 = 6, 4 × 2 = 8, 5 × 2 = 10. Cada vez sumas 2 más. Por eso multiplicar un número por 2 da su doble: 6 × 2 es el doble de 6, que es 12.",
        "Para recordar la tabla, cuenta de 2 en 2: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. Todos los resultados son números pares: terminan en 0, 2, 4, 6 u 8. Si olvidas uno, usa el anterior y suma 2.",
    ],
    vocab=[("par", "grupo de dos objetos"), ("doble", "un número sumado consigo mismo"), ("tabla del 2", "los resultados de repetir grupos de 2"), ("número par", "número que se puede agrupar de a 2 sin que sobre nada"), ("contar de 2 en 2", "decir 2, 4, 6, 8…")],
    worked=[
        {"title": "Cinco parejas", "problem": "Hay 5 parejas de zapatos dibujadas así: (●●) (●●) (●●) (●●) (●●). ¿Cuántos zapatos hay?", "steps": ["Hay 5 grupos de 2.", "Sumo: 2 + 2 + 2 + 2 + 2 = 10.", "Escribo la multiplicación: 5 × 2 = 10.", "Compruebo con el doble de 5: 5 + 5 = 10."], "answer": "10 zapatos"},
        {"title": "Usar el resultado anterior", "problem": "Sabes que 6 × 2 = 12. ¿Cuánto es 7 × 2?", "steps": ["7 × 2 es un grupo de 2 más que 6 × 2.", "Sumo 2: 12 + 2 = 14.", "Compruebo con el doble de 7: 7 + 7 = 14.", "Entonces 7 × 2 = 14."], "answer": "7 × 2 = 14"},
    ],
    mistakes=[
        {"wrong": "Decir que 6 × 2 = 8 porque 6 + 2 = 8.", "why": "Se suman los números en vez de repetir el grupo.", "fix": "6 × 2 es 6 grupos de 2, que es el doble de 6: 12."},
        {"wrong": "Contar de 2 en 2 así: 2, 4, 6, 9.", "why": "Se pierde el ritmo de sumar siempre 2.", "fix": "Siempre sumas 2: 2, 4, 6, 8, 10."},
    ],
    tiers={
        "recovery": [
            arith("Calcula 5 × 2 sumando 2 + 2 + 2 + 2 + 2.", "5*2", "Son 5 grupos de 2."),
            arith("Calcula el doble de 6.", "6+6", "El doble repite el mismo número."),
            ex("Completa contando de 2 en 2: 2, 4, 6, __, 10.", "8", "Se suma siempre 2."),
        ],
        "understand": [
            ex("¿Cuánto es 3 × 2?", "6", "Son 3 grupos de 2: 2 + 2 + 2."),
            ex("¿Por qué los resultados de la tabla del 2 son dobles?", "Porque multiplicar por 2 es sumar el número consigo mismo", "Por ejemplo, 4 × 2 es 4 + 4."),
            ex("Si 4 × 2 = 8, ¿cuánto es 5 × 2?", "10", "Se agrega un grupo de 2 más."),
        ],
        "apply": [
            arith("Calcula 7 × 2.", "7*2", "Es el doble de 7."),
            arith("Hay 9 parejas de bailarines. ¿Cuántos bailarines hay?", "9*2", "Son 9 grupos de 2."),
            arith("Una bicicleta tiene 2 ruedas. ¿Cuántas ruedas hay en 8 bicicletas?", "8*2", "Son 8 grupos de 2."),
        ],
        "reason": [
            ex("Sofía dice que 6 × 2 = 8 porque 6 + 2 = 8. ¿Qué error comete y cuál es el resultado?", "Suma 6 + 2 en vez de 6 grupos de 2; el resultado es 12", "6 × 2 es el doble de 6."),
            ex("¿Es verdad que 10 × 2 = 20? Explica con un doble.", "Sí; el doble de 10 es 20", "10 + 10 = 20."),
        ],
        "challenge": [
            ex("Escribe los resultados de la tabla del 2 desde 1 × 2 hasta 10 × 2.", "2, 4, 6, 8, 10, 12, 14, 16, 18, 20", "Cada resultado suma 2 al anterior."),
            ex("¿Cuántos grupos de 2 hay en 14?", "7", "7 × 2 = 14."),
        ],
    },
    context=[arith("En un baile hay 8 parejas de estudiantes. ¿Cuántos estudiantes bailan?", "8*2", "Cada pareja son 2 estudiantes.")],
    selfcheck=[arith("Calcula 4 × 2.", "4*2", "Es el doble de 4."), arith("Calcula 10 × 2.", "10*2", "Es el doble de 10."), ex("¿Todos los resultados de la tabla del 2 son pares o impares?", "Pares", "Siempre sale un número que se agrupa de a 2.")],
    open_task=task(
        "Cuenta los zapatos de 6 niños (cada niño tiene 2). Dibuja 6 parejas con (●●) y escribe la suma repetida y la multiplicación. Luego completa la tabla del 2 desde 1 × 2 hasta 6 × 2.",
        "(●●) (●●) (●●) (●●) (●●) (●●): 2 + 2 + 2 + 2 + 2 + 2 = 12 y 6 × 2 = 12. Tabla: 1 × 2 = 2, 2 × 2 = 4, 3 × 2 = 6, 4 × 2 = 8, 5 × 2 = 10, 6 × 2 = 12.",
        ["dibuja 6 parejas", "escribe 6 × 2 = 12", "completa la tabla hasta 6 × 2"],
        ["dibujo", "suma repetida", "tabla"],
        ["sumar 6 + 2", "saltarse un número al contar de 2 en 2"],
        "Pide que cuente de 2 en 2 con el dedo sobre el dibujo; valora que explique cada paso.",
    ),
    reinforce="Cuenta de 2 en 2 hasta 20 en voz alta y marca cada número en un papel.",
    extend="Escribe la tabla del 2 hasta 10 × 2 y subraya los resultados que terminan en 4 o en 8.",
)

register(
    OA11, 3,
    materials="Manos dibujadas con 5 dedos en este cuaderno y lápiz. Todo lo necesario está en los ejercicios.",
    use="Aprenderé la tabla del 5 contando de 5 en 5. Sirve para contar dedos, minutos del reloj y monedas de 5 rápidamente.",
    prior=["Sé la tabla del 2.", "Sé contar de 5 en 5 hasta 50."],
    explain=[
        "La tabla del 5 son grupos de 5. Una mano tiene 5 dedos. Cuatro manos son 4 grupos de 5: 5 + 5 + 5 + 5 = 20. Se escribe 4 × 5 = 20.",
        "Cuenta de 5 en 5 para recordar los resultados: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50. Esos son 1 × 5, 2 × 5, y así hasta 10 × 5. Cada vez sumas 5 al resultado anterior.",
        "Hay un patrón fácil: los resultados siempre terminan en 5 o en 0. Si un número no termina en 5 ni en 0, no está en la tabla del 5. El minutero del reloj también cuenta de 5 en 5: cada número del reloj son 5 minutos.",
    ],
    vocab=[("tabla del 5", "los resultados de repetir grupos de 5"), ("de 5 en 5", "contar sumando 5 cada vez"), ("patrón", "algo que se repite siempre igual"), ("producto", "resultado de multiplicar"), ("grupo de 5", "cinco objetos juntos, como los dedos de una mano")],
    worked=[
        {"title": "Dedos de cuatro manos", "problem": "Cuatro manos dibujadas tienen 5 dedos cada una. ¿Cuántos dedos hay?", "steps": ["Hay 4 grupos de 5.", "Cuento de 5 en 5: 5, 10, 15, 20.", "Escribo 4 × 5 = 20.", "Compruebo: 5 + 5 + 5 + 5 = 20."], "answer": "20 dedos"},
        {"title": "Un resultado que no está", "problem": "¿Está 36 en la tabla del 5?", "steps": ["Los resultados de la tabla del 5 terminan en 5 o en 0.", "36 termina en 6.", "No termina en 5 ni en 0.", "36 no está en la tabla del 5."], "answer": "No"},
    ],
    mistakes=[
        {"wrong": "Contar 5, 10, 14, 19, 24.", "why": "Se pierde el salto de 5.", "fix": "Siempre sumas 5: 5, 10, 15, 20, 25."},
        {"wrong": "Decir que 7 × 5 = 12 porque 7 + 5 = 12.", "why": "Se suma en lugar de repetir el grupo.", "fix": "7 × 5 son 7 grupos de 5: 35."},
    ],
    tiers={
        "recovery": [
            arith("Calcula 3 × 5 sumando 5 + 5 + 5.", "3*5", "Son 3 grupos de 5."),
            ex("Cuenta de 5 en 5: 5, 10, 15, __, 25.", "20", "Se suma 5 cada vez."),
            arith("Una mano tiene 5 dedos. ¿Cuántos dedos hay en 2 manos?", "2*5", "Son 2 grupos de 5."),
        ],
        "understand": [
            ex("¿En qué cifras terminan los resultados de la tabla del 5?", "En 0 o en 5", "Al contar de 5 en 5 se alternan 5 y 0."),
            ex("Si 4 × 5 = 20, ¿cuánto es 5 × 5?", "25", "Se agrega un grupo de 5 más."),
            ex("¿Cuántos grupos de 5 hay en 30?", "6", "6 × 5 = 30."),
        ],
        "apply": [
            arith("Calcula 7 × 5.", "7*5", "Son 7 grupos de 5."),
            arith("Hay 6 sobres con 5 láminas cada uno. ¿Cuántas láminas hay?", "6*5", "Son 6 grupos de 5."),
            arith("Hay 9 manos dibujadas, cada una con 5 dedos. ¿Cuántos dedos hay?", "9*5", "Son 9 grupos de 5."),
        ],
        "reason": [
            ex("¿Está el 36 en la tabla del 5? Explica.", "No; los resultados terminan en 0 o en 5", "36 termina en 6."),
            ex("Tomás cuenta 5, 10, 15, 20, 25, 30, 35 para 8 × 5 y escribe 35. ¿Qué error cometió y cuál es el resultado?", "Contó solo 7 grupos; 8 × 5 = 40", "Faltó el octavo grupo de 5."),
        ],
        "challenge": [
            ex("Escribe los resultados de la tabla del 5 de 1 × 5 hasta 10 × 5.", "5, 10, 15, 20, 25, 30, 35, 40, 45, 50", "Cada resultado suma 5 al anterior."),
            arith("Un reloj marca los minutos de 5 en 5. Si el minutero avanza 7 saltos, ¿cuántos minutos pasaron?", "7*5", "Son 7 grupos de 5 minutos."),
        ],
    },
    context=[arith("Una tienda vende paquetes de 5 lápices. Compras 4 paquetes. ¿Cuántos lápices compras?", "4*5", "Son 4 grupos de 5.")],
    selfcheck=[arith("Calcula 6 × 5.", "6*5", "Son 6 grupos de 5."), ex("¿Cuántos grupos de 5 hay en 45?", "9", "9 × 5 = 45."), ex("¿Está el 28 en la tabla del 5?", "No", "No termina en 0 ni en 5.")],
    open_task=task(
        "Mira los grupos: (●●●●●) (●●●●●) (●●●●●) (●●●●●) (●●●●●) (●●●●●). Son 6 manos de 5 dedos cada una. Escribe la suma repetida y la multiplicación. Luego escribe la tabla del 5 hasta 10 × 5 y subraya los resultados que terminan en 0.",
        "6 manos: 5 + 5 + 5 + 5 + 5 + 5 = 30 y 6 × 5 = 30. Tabla: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50. Terminan en 0: 10, 20, 30, 40 y 50.",
        ["escribe 6 × 5 = 30", "completa la tabla del 5", "subraya los resultados que terminan en 0"],
        ["suma repetida", "tabla completa", "subrayado"],
        ["perder el salto de 5 al contar", "sumar 6 + 5"],
        "Pide que cuente de 5 en 5 mientras señala cada mano; reconoce el patrón del 5 y el 0.",
    ),
    reinforce="Cuenta de 5 en 5 hasta 50 y escribe cada número en una tira de papel.",
    extend="Escribe cinco números menores que 50 que estén en la tabla del 5 y cinco que no, y explica cómo lo sabes.",
)

register(
    OA11, 4,
    materials="Paquetes de 10 dibujados con ▮ en este cuaderno y lápiz. Todo lo necesario está en los ejercicios.",
    use="Aprenderé la tabla del 10 usando decenas. Sirve para contar paquetes de 10 y saber cuánto hay de una vez.",
    prior=["Sé que una decena son 10 unidades.", "Sé contar de 10 en 10."],
    explain=[
        "La tabla del 10 son grupos de 10, es decir, decenas. Ocho paquetes de 10 son 8 decenas: 8 × 10 = 80. Cada paquete es un grupo igual de 10.",
        "Los resultados se leen contando de 10 en 10: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100. Esos son 1 × 10, 2 × 10, y así hasta 10 × 10. Cada resultado es el número de decenas con un 0 al lado.",
        "Por eso todos los resultados terminan en 0. Si multiplicas 6 × 10, tienes 6 decenas: 60. Si tienes 90, sabes que son 9 decenas, y que 9 × 10 = 90. Puedes pensar siempre en cuántas decenas hay.",
    ],
    vocab=[("tabla del 10", "los resultados de repetir grupos de 10"), ("decena", "grupo de 10"), ("de 10 en 10", "contar sumando 10 cada vez"), ("paquete", "grupo de 10 objetos atados"), ("producto", "resultado de multiplicar")],
    worked=[
        {"title": "Ocho paquetes de 10", "problem": "Hay 8 paquetes y cada uno tiene 10 lápices. ¿Cuántos lápices hay?", "steps": ["Hay 8 grupos de 10: 8 decenas.", "Cuento de 10 en 10: 10, 20, 30, 40, 50, 60, 70, 80.", "Escribo 8 × 10 = 80.", "Compruebo: 8 decenas son 80."], "answer": "80 lápices"},
        {"title": "Hallar cuántos paquetes", "problem": "Hay 90 hojas y cada paquete tiene 10. ¿Cuántos paquetes hay?", "steps": ["Pregunto: ¿cuántos grupos de 10 hacen 90?", "Cuento de 10 en 10 hasta llegar a 90: son 9 saltos.", "9 × 10 = 90.", "Hay 9 paquetes."], "answer": "9 paquetes"},
    ],
    mistakes=[
        {"wrong": "Decir que 5 × 10 = 15 porque 5 + 10 = 15.", "why": "Se suman los números en vez de repetir el grupo.", "fix": "5 × 10 son 5 decenas, es decir 50."},
        {"wrong": "Escribir 60 como 6 decenas y 0 decenas.", "why": "Se confunde la cifra 0 con otra decena.", "fix": "60 son 6 decenas y 0 unidades."},
    ],
    tiers={
        "recovery": [
            arith("Calcula 3 × 10.", "3*10", "Son 3 grupos de 10."),
            ex("Cuenta de 10 en 10: 10, 20, 30, __, 50.", "40", "Se suma 10 cada vez."),
            arith("En una caja hay 10 lápices. ¿Cuántos lápices hay en 4 cajas?", "4*10", "Son 4 grupos de 10."),
        ],
        "understand": [
            ex("¿Cuántas decenas hay en 80?", "8", "8 × 10 = 80."),
            ex("6 × 10 es 60. ¿En qué lugar de 60 aparece el 6?", "En las decenas", "Son 6 decenas."),
            ex("Si 7 × 10 = 70, ¿cuánto es 8 × 10?", "80", "Se agrega una decena más."),
        ],
        "apply": [
            arith("Calcula 8 × 10.", "8*10", "Son 8 decenas."),
            arith("Hay 9 bolsas con 10 caramelos cada una. ¿Cuántos caramelos hay?", "9*10", "Son 9 grupos de 10."),
            arith("Cada paquete tiene 10 hojas. ¿Cuántas hojas hay en 6 paquetes?", "6*10", "Son 6 grupos de 10."),
        ],
        "reason": [
            ex("Rita dice que 5 × 10 = 15 porque 5 + 10 = 15. ¿Qué error comete y cuál es el resultado?", "Suma en vez de repetir el grupo; 5 × 10 = 50", "Son 5 decenas."),
            ex("¿Por qué todos los resultados de la tabla del 10 terminan en 0?", "Porque son decenas completas, sin unidades sueltas", "Cada grupo tiene exactamente 10."),
        ],
        "challenge": [
            ex("Escribe los resultados de la tabla del 10 desde 1 × 10 hasta 10 × 10.", "10, 20, 30, 40, 50, 60, 70, 80, 90, 100", "Cada resultado suma 10 al anterior."),
            arith("Tienes 3 paquetes de 10 y 5 hojas sueltas. ¿Cuántas hojas tienes?", "3*10+5", "Tres decenas son 30 y se suman 5."),
        ],
    },
    context=[arith("En el jardín hay 6 filas con 10 plantas cada una. ¿Cuántas plantas hay?", "6*10", "Son 6 grupos de 10.")],
    selfcheck=[arith("Calcula 7 × 10.", "7*10", "Son 7 decenas."), ex("¿Cuántos grupos de 10 hay en 60?", "6", "6 × 10 = 60."), ex("¿Con qué cifra terminan los resultados de la tabla del 10?", "Con 0", "Son decenas completas.")],
    open_task=task(
        "Hay 7 paquetes de 10 lápices. Dibuja los paquetes con ▮, escribe la suma repetida y la multiplicación. Después escribe la tabla del 10 hasta 10 × 10 y marca con un círculo el resultado de 7 × 10.",
        "▮ ▮ ▮ ▮ ▮ ▮ ▮: 10 + 10 + 10 + 10 + 10 + 10 + 10 = 70 y 7 × 10 = 70. Tabla: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100. El círculo va en 70.",
        ["dibuja los siete paquetes", "escribe 7 × 10 = 70", "completa la tabla del 10"],
        ["dibujo", "suma repetida", "tabla"],
        ["sumar 7 + 10", "olvidar el 0"],
        "Pide que lea la tabla en voz alta con la palabra «decenas»; reconoce que relaciona la multiplicación con las decenas.",
    ),
    reinforce="Cuenta de 10 en 10 hasta 100 mostrando una decena con ▮ cada vez.",
    extend="Explica por qué 9 × 10 es 90 usando decenas y dibújalo.",
)

register(
    OA11, 5,
    materials="Hojas y lápiz. Las multiplicaciones y los problemas están escritos en los ejercicios.",
    use="Aprenderé a separar una multiplicación en partes más fáciles y a resolver problemas con las tablas del 2, 5 y 10. Sirve para calcular productos que no recuerdo.",
    prior=["Sé las tablas del 2, 5 y 10.", "Sé sumar números de dos cifras."],
    explain=[
        "Cuando no recuerdas una multiplicación, puedes separarla en dos más fáciles. Esto se llama distribuir. Para 7 × 5, separa los 7 grupos en 5 grupos y 2 grupos: 5 × 5 = 25 y 2 × 5 = 10. Luego suma: 25 + 10 = 35.",
        "Funciona porque siguen siendo siete grupos de 5: cinco más dos. No cambia el total, solo lo calculas en partes que ya conoces. También sirve en la tabla del 2: 8 × 2 = 4 × 2 + 4 × 2 = 8 + 8 = 16.",
        "Para resolver un problema, lee los datos, mira si hay grupos iguales, elige la tabla y escribe la multiplicación. Después responde con una frase. Fíjate bien en qué es cada grupo y cuántos hay en cada uno.",
    ],
    vocab=[("distribuir", "separar los grupos en dos partes y multiplicar cada una"), ("separar", "dividir en partes más fáciles"), ("problema", "situación que se resuelve con operaciones"), ("grupo", "conjunto de objetos"), ("total", "resultado final")],
    worked=[
        {"title": "Distribuir 7 × 5", "problem": "Calcula 7 × 5 separando en 5 × 5 y 2 × 5.", "steps": ["5 × 5 = 25.", "2 × 5 = 10.", "Sumo las dos partes: 25 + 10 = 35.", "Siguen siendo 5 + 2 = 7 grupos de 5."], "answer": "7 × 5 = 35"},
        {"title": "Un problema con la tabla del 10", "problem": "Hay 6 cajas con 10 lápices cada una y 3 cajas con 2 lápices cada una. ¿Cuántos lápices hay?", "steps": ["Las cajas de 10: 6 × 10 = 60.", "Las cajas de 2: 3 × 2 = 6.", "Sumo: 60 + 6 = 66.", "Respuesta: hay 66 lápices."], "answer": "66 lápices"},
    ],
    mistakes=[
        {"wrong": "Calcular 7 × 5 como 5 × 5 + 2 = 27.", "why": "Se olvida multiplicar el 2 por 5.", "fix": "Los 2 grupos restantes son 2 × 5 = 10, entonces 25 + 10 = 35."},
        {"wrong": "Separar 7 grupos en 5 y 3.", "why": "5 + 3 no es 7.", "fix": "Los grupos separados deben sumar los grupos que había: 5 + 2 = 7."},
    ],
    tiers={
        "recovery": [
            arith("Calcula 5 × 5.", "5*5", "Son 5 grupos de 5."),
            arith("Calcula 2 × 5.", "2*5", "Son 2 grupos de 5."),
            arith("Suma las dos partes: 25 + 10.", "25+10", "Se juntan las dos multiplicaciones."),
        ],
        "understand": [
            ex("Para 7 × 5, se separa 7 en 5 y 2. ¿Qué dos multiplicaciones se hacen?", "5 × 5 y 2 × 5", "Los grupos se reparten en dos partes."),
            ex("Si 5 × 5 = 25 y 2 × 5 = 10, ¿cuánto es 7 × 5?", "35", "25 + 10 = 35."),
            ex("Para 9 × 2, ¿se puede calcular 5 × 2 y 4 × 2?", "Sí; porque 5 + 4 = 9 grupos", "Las partes deben sumar la cantidad de grupos."),
        ],
        "apply": [
            arith("Calcula 6 × 5 separando 5 × 5 y 1 × 5.", "5*5+1*5", "Seis grupos son 5 más 1."),
            arith("Calcula 8 × 2 separando 4 × 2 y 4 × 2.", "4*2+4*2", "Ocho grupos son 4 más 4."),
            arith("Calcula 7 × 10 separando 5 × 10 y 2 × 10.", "5*10+2*10", "Siete grupos son 5 más 2."),
        ],
        "reason": [
            ex("Luz calcula 7 × 5 como 5 × 5 y 2 × 5, pero suma 25 + 2. ¿Qué error comete y cuál es el resultado?", "Olvidó multiplicar el 2 por 5; es 25 + 10 = 35", "2 × 5 = 10."),
            ex("¿Se puede calcular 8 × 5 como 4 × 5 + 4 × 5? Explica.", "Sí; 20 + 20 = 40 y 4 + 4 = 8 grupos", "Las dos partes suman 8 grupos."),
        ],
        "challenge": [
            arith("Cada caja tiene 5 lápices y hay 9 cajas. Calcula con 5 cajas y 4 cajas.", "5*5+4*5", "Nueve cajas son 5 más 4."),
            arith("Una escuela compra 6 paquetes de 10 cuadernos y 3 paquetes de 2 cuadernos. ¿Cuántos cuadernos compra?", "6*10+3*2", "60 de los paquetes de 10 y 6 de los paquetes de 2."),
        ],
    },
    context=[arith("En un salón hay 8 mesas con 5 sillas cada una. ¿Cuántas sillas hay?", "8*5", "Son 8 grupos de 5.")],
    selfcheck=[arith("Calcula 6 × 2 separando 3 × 2 y 3 × 2.", "3*2+3*2", "Seis grupos son 3 más 3."), arith("Calcula 9 × 5 separando 5 × 5 y 4 × 5.", "5*5+4*5", "Nueve grupos son 5 más 4."), ex("¿Cuál es el resultado de 4 × 10?", "40", "Son 4 decenas.")],
    open_task=task(
        "Hay 7 bolsas con 5 caramelos cada una y 4 bolsas con 10 caramelos cada una. Calcula 7 × 5 separando 5 × 5 y 2 × 5. Calcula 4 × 10. Suma todo y responde con una frase.",
        "7 × 5 = 5 × 5 + 2 × 5 = 25 + 10 = 35. 4 × 10 = 40. Total: 35 + 40 = 75. Hay 75 caramelos.",
        ["separa 7 × 5 en 5 × 5 y 2 × 5", "obtiene 35 y 40", "suma y obtiene 75", "responde con una frase"],
        ["multiplicaciones separadas", "suma final", "frase de respuesta"],
        ["olvidar multiplicar una de las partes", "separar los grupos en partes que no suman lo correcto"],
        "Pide que explique por qué separar no cambia el total; reconoce la frase de respuesta clara.",
    ),
    reinforce="Calcula 6 × 10 y comprueba separándolo en 3 × 10 y 3 × 10.",
    extend="Inventa dos multiplicaciones difíciles con 5 o con 2 y resuélvelas separando en partes fáciles.",
)
