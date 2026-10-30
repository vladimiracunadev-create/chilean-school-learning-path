"""Student material for 2.º básico Matemática, OA 08 (sumar y restar cero) y OA 09 (adición y sustracción hasta 100 sin reserva)."""
from __future__ import annotations

from student_content_ma02_a import bars
from student_content_ma02_c import KEY
from student_content_ma02_f import task
from student_lessons import arith, ex, register

OA8 = "MA02 OA 08"
OA9 = "MA02 OA 09"

# ------------------------------------------------------------------ OA 08
register(
    OA8, 1,
    materials="Una bandeja o plato, 14 fichas o botones y lápiz. Las cantidades están escritas en cada ejercicio.",
    use="Aprenderé qué pasa cuando sumo 0 a un número. Sirve para saber el resultado sin contar cuando no se agrega nada.",
    prior=["Sé que sumar es agregar.", "Sé qué es el número 0: ninguna cantidad."],
    explain=[
        "Sumar es agregar objetos. El número 0 significa que no hay nada. Si agregas 0 objetos, no agregas ninguno. Por eso la cantidad queda igual.",
        "Imagina una bandeja con 14 fichas. Agregas 0 fichas: la bandeja sigue con 14. Se escribe 14 + 0 = 14. También puedes empezar con 0 y agregar 14: 0 + 14 = 14. Es lo mismo, porque el total es la cantidad de fichas que hay al final.",
        "Siempre que sumes 0 a un número, el resultado es ese mismo número. No importa si es chico o grande: 6 + 0 = 6, y 58 + 0 = 58. El 0 no cambia la cantidad, y no la hace desaparecer.",
    ],
    vocab=[("cero (0)", "ninguna cantidad"), ("agregar", "poner más objetos"), ("cantidad inicial", "lo que hay antes de agregar"), ("cantidad final", "lo que hay después de agregar"), ("quedar igual", "no cambiar")],
    worked=[
        {"title": "Agregar 0 fichas", "problem": "En una bandeja hay 14 fichas. Agregas 0 fichas. ¿Cuántas hay ahora?", "steps": ["Cantidad inicial: 14 fichas.", "Agrego 0: no pongo ninguna.", "La bandeja no cambió y sigue con 14.", "Lo escribo: 14 + 0 = 14."], "answer": "14 + 0 = 14"},
        {"title": "Empezar en cero", "problem": "Una caja está vacía. Agregas 9 lápices. ¿Cuántos lápices hay?", "steps": ["Cantidad inicial: 0 lápices (caja vacía).", "Agrego 9 lápices.", "Ahora hay 9 lápices.", "Lo escribo: 0 + 9 = 9."], "answer": "0 + 9 = 9"},
    ],
    mistakes=[
        {"wrong": "Decir que 52 + 0 = 0.", "why": "Se piensa que sumar 0 borra el número.", "fix": "Sumar 0 es no agregar nada. La cantidad queda como estaba: 52 + 0 = 52."},
        {"wrong": "Decir que 7 + 0 = 70.", "why": "Se pone el 0 al lado del 7 como si formara otro número.", "fix": "Sumar 0 no agrega nada. 7 + 0 = 7."},
    ],
    tiers={
        "recovery": [
            arith("Hay 14 fichas en una bandeja y agregas 0 fichas. ¿Cuántas fichas hay ahora?", "14+0", "Agregar 0 no cambia la cantidad."),
            ex("¿Cuántas fichas agregas cuando sumas 0?", "Ninguna", "El 0 significa ninguna cantidad."),
            arith("Calcula 23 + 0.", "23+0", "Sumar 0 deja el mismo número."),
        ],
        "understand": [
            ex("Una bandeja tiene 29 cubos y sumas 0 cubos. ¿La cantidad aumentó, disminuyó o quedó igual?", "Quedó igual", "No se agregó nada."),
            ex("Completa: 34 + 0 = __.", "34", "Sumar 0 no cambia el número."),
            ex("¿Verdadero o falso? Al sumar 0 a un número, el resultado es 0.", "Falso; el resultado es el mismo número", "Sumar 0 no borra la cantidad."),
        ],
        "apply": [
            arith("Una caja tiene 45 lápices. Hoy llegan 0 lápices nuevos. ¿Cuántos lápices hay?", "45+0", "No llegó nada, la cantidad es la misma."),
            ex("Completa: __ + 0 = 67.", "67", "Si no se suma nada, el número queda igual."),
            arith("Calcula 0 + 38.", "0+38", "Empezar en 0 y agregar 38 da 38."),
        ],
        "reason": [
            ex("Pablo dice que 52 + 0 = 0 porque «sumar cero es no tener nada». ¿Qué error comete?", "Confunde sumar 0 con borrar la cantidad; 52 + 0 = 52", "Sumar 0 no quita lo que ya hay."),
            ex("¿Es lo mismo 0 + 17 que 17 + 0? Responde sí o no y di por qué.", "Sí; ambos dan 17 porque no se agrega nada", "En los dos casos el total es 17."),
        ],
        "challenge": [
            ex("Escribe las dos sumas con 0 que dan 21.", "21 + 0 y 0 + 21", "Una de las partes es 0 y la otra 21."),
            arith("Camila tiene 8 stickers. El lunes recibe 0, el martes recibe 0 y el miércoles recibe 0. ¿Cuántos stickers tiene el miércoles?", "8+0+0+0", "Sumar 0 varias veces tampoco cambia la cantidad."),
        ],
    },
    context=[arith("En el curso hay 26 sillas. Hoy traen 0 sillas nuevas. ¿Cuántas sillas hay en total?", "26+0", "No se agregó ninguna silla.")],
    selfcheck=[arith("Calcula 63 + 0.", "63+0", "Sumar 0 deja el mismo número."), ex("¿Cuánto es 0 + 0?", "0", "No hay nada y no se agrega nada."), ex("Si 19 + 0 = __, ¿qué número falta?", "19", "No se agregó nada.")],
    open_task=task(
        "Hay tres bandejas con 14, 27 y 40 fichas. Agrega 0 fichas a cada una. Dibuja cada bandeja antes y después con ▮ para 10 y ● para 1, y escribe la suma. Explica con una frase qué pasa cuando sumas 0.",
        "14 + 0 = 14: " + bars(14) + " antes y después. 27 + 0 = 27: " + bars(27) + ". 40 + 0 = 40: " + bars(40) + ". Cuando sumo 0 no agrego nada y la cantidad queda igual.",
        ["escribe las tres sumas correctas", "dibuja antes y después iguales", "explica que 0 no cambia la cantidad"],
        ["tres sumas", "dibujos", "frase de explicación"],
        ["creer que sumar 0 da 0", "cambiar el dibujo después de sumar"],
        "Pide que compare el dibujo antes y después y diga qué cambió; reconoce que la respuesta es «nada».",
    ),
    reinforce="Pon 12 fichas en un plato. Agrega 0 fichas y cuéntalas de nuevo. Escribe la suma.",
    extend="Escribe cinco sumas con 0 cuyo resultado sea mayor que 50 y explica por qué todas siguen la misma regla.",
)

register(
    OA8, 2,
    materials="Una bandeja con 19 cubos o botones y lápiz. Las cantidades están escritas en cada ejercicio.",
    use="Aprenderé qué pasa cuando resto 0 a un número. Sirve para saber cuánto queda cuando no se quita nada.",
    prior=["Sé que restar es quitar.", "Sé que sumar 0 no cambia el número."],
    explain=[
        "Restar es quitar objetos. Si quitas 0 objetos, no sacas ninguno. Entonces todos los objetos siguen donde estaban. La cantidad que queda es la misma que había al comienzo.",
        "Piensa en 19 cubos en una bandeja. Retiras 0 cubos: ningún cubo se mueve y quedan 19. Se escribe 19 − 0 = 19. Se lee: diecinueve menos cero es diecinueve.",
        "Siempre que restes 0 a un número, el resultado es ese mismo número. 8 − 0 = 8 y 75 − 0 = 75. No se quita nada, por eso no queda menos. Puedes comprobarlo sumando: 19 + 0 = 19, que vuelve al número del comienzo.",
    ],
    vocab=[("restar", "quitar una cantidad"), ("cero (0)", "ninguna cantidad"), ("quedan", "los objetos que siguen después de quitar"), ("cantidad inicial", "lo que hay antes de quitar"), ("comprobar", "revisar el resultado con otra operación")],
    worked=[
        {"title": "Quitar 0 cubos", "problem": "En una bandeja hay 19 cubos. Quitas 0 cubos. ¿Cuántos quedan?", "steps": ["Cantidad inicial: 19 cubos.", "Quito 0: no saco ninguno.", "Quedan los 19 cubos.", "Compruebo: 19 + 0 = 19."], "answer": "19 − 0 = 19"},
        {"title": "Restar 0 a un número grande", "problem": "Una caja tiene 75 hojas. Sacas 0 hojas. ¿Cuántas hojas quedan?", "steps": ["Cantidad inicial: 75 hojas.", "No saco ninguna hoja.", "Quedan 75 hojas.", "Compruebo: 75 + 0 = 75."], "answer": "75 − 0 = 75"},
    ],
    mistakes=[
        {"wrong": "Decir que 19 − 0 = 0.", "why": "Se cree que restar 0 deja cero.", "fix": "Restar 0 es no quitar nada. Quedan los 19 objetos."},
        {"wrong": "Decir que 30 − 0 = 3.", "why": "Se saca el 0 del número 30 como si fuera parte de la resta.", "fix": "El número es 30 y no se quita nada. 30 − 0 = 30."},
    ],
    tiers={
        "recovery": [
            arith("Una bandeja tiene 19 cubos y quitas 0. ¿Cuántos cubos quedan?", "19-0", "Quitar 0 no saca ningún cubo."),
            ex("¿Cuántos objetos quitas cuando restas 0?", "Ninguno", "El 0 significa ninguna cantidad."),
            arith("Calcula 22 − 0.", "22-0", "Restar 0 deja el mismo número."),
        ],
        "understand": [
            ex("Hay 24 manzanas y quitas 0. ¿Quedan más, menos o las mismas manzanas?", "Las mismas", "No se quitó ninguna."),
            ex("Completa: 36 − 0 = __.", "36", "Restar 0 no cambia el número."),
            ex("¿Verdadero o falso? Si restas 0 a 48, el resultado es 0.", "Falso; el resultado es 48", "No se quitó nada de 48."),
        ],
        "apply": [
            arith("Una caja tiene 57 lápices. Hoy se sacan 0 lápices. ¿Cuántos lápices quedan?", "57-0", "No se sacó ningún lápiz."),
            ex("Completa: __ − 0 = 84.", "84", "Si no se quita nada, queda el mismo número."),
            arith("Un tren llevaba 61 personas. En la estación bajaron 0. ¿Cuántas personas siguen en el tren?", "61-0", "Nadie bajó, todos siguen."),
        ],
        "reason": [
            ex("Rocío calcula 40 − 0 y escribe 4. ¿Qué error comete y cuál es la respuesta?", "Quita el 0 del número 40; la respuesta es 40", "No se quita nada de 40."),
            ex("Después de restar 0 a 35 queda 35. ¿Cómo comprobarías con una suma?", "35 + 0 = 35", "La suma contraria vuelve al número del comienzo."),
        ],
        "challenge": [
            ex("Escribe una resta con 0 cuyo resultado sea 90.", "90 − 0 = 90", "Solo sirve 90 − 0, porque no se quita nada."),
            arith("Inés tiene 16 globos. Le quitan 0 el lunes, 0 el martes y 0 el miércoles. ¿Cuántos globos tiene el miércoles?", "16-0-0-0", "Restar 0 muchas veces tampoco cambia la cantidad."),
        ],
    },
    context=[arith("La biblioteca tiene 83 libros. Hoy nadie se lleva ninguno: se retiran 0 libros. ¿Cuántos libros hay?", "83-0", "No se quitó ningún libro.")],
    selfcheck=[arith("Calcula 72 − 0.", "72-0", "Restar 0 deja el mismo número."), ex("¿Cuánto es 0 − 0?", "0", "No hay nada y no se quita nada."), ex("Si 29 − 0 = __, ¿qué número falta?", "29", "No se quitó nada.")],
    open_task=task(
        "Hay tres cajas con 19, 34 y 50 fichas. Quita 0 fichas de cada caja. Dibuja cada caja antes y después con ▮ para 10 y ● para 1, y escribe la resta. Comprueba cada una con una suma.",
        "19 − 0 = 19: " + bars(19) + "; comprobación 19 + 0 = 19. 34 − 0 = 34: " + bars(34) + "; 34 + 0 = 34. 50 − 0 = 50: " + bars(50) + "; 50 + 0 = 50.",
        ["escribe las tres restas correctas", "dibuja antes y después iguales", "comprueba con una suma cada vez"],
        ["tres restas", "dibujos", "tres comprobaciones"],
        ["creer que restar 0 da 0", "quitar el 0 del número"],
        "Pide que explique en voz alta por qué la cantidad no cambió; reconoce que usa la comprobación con la suma.",
    ),
    reinforce="Pon 15 fichas en un plato. Quita 0 fichas, cuéntalas y escribe la resta.",
    extend="Explica con tus palabras por qué sumar 0 y restar 0 dejan igual el número, y da un ejemplo de cada uno con un número mayor que 60.",
)

register(
    OA8, 3,
    materials="Fichas, un plato y lápiz. Las cantidades están escritas en cada ejercicio.",
    use="Aprenderé la diferencia entre restar 0 a un número (8 − 0) y empezar con 0 y querer quitar (0 − 8). Sirve para entender cuándo una resta se puede hacer.",
    prior=["Sé que restar 0 deja el mismo número.", "Sé que no se puede quitar lo que no existe."],
    explain=[
        "Hay dos restas con 0 que se parecen pero son distintas. En 8 − 0 empiezas con 8 objetos y quitas ninguno. Quedan 8. Se puede hacer, y el resultado es 8.",
        "En 0 − 8 empiezas sin nada y quieres quitar 8. No tienes objetos para sacar. Con los números que conocemos, esa resta no se puede hacer. En cambio, 0 − 0 sí se puede: no hay nada, no quitas nada, y queda 0.",
        "También es útil recordar esto: si restas a un número el mismo número, el resultado es 0. Por ejemplo, 8 − 8 = 0, porque quitas todo. No confundas 8 − 8 = 0 con 8 − 0 = 8. En una quitas todo y en la otra no quitas nada.",
    ],
    vocab=[("cantidad inicial", "lo que hay antes de quitar"), ("quitar todo", "sacar todos los objetos que hay"), ("no se puede", "no hay suficientes objetos para quitar"), ("restar el mismo número", "quitar toda la cantidad, dejando 0"), ("distinguir", "reconocer que dos cosas son diferentes")],
    worked=[
        {"title": "Quitar nada y quitar todo", "problem": "Hay 8 fichas. Compara 8 − 0 con 8 − 8.", "steps": ["En 8 − 0 no quito ninguna: quedan 8.", "En 8 − 8 quito las 8: queda 0.", "Los resultados son distintos: 8 y 0.", "El número que se resta cambia lo que pasa."], "answer": "8 − 0 = 8 y 8 − 8 = 0"},
        {"title": "Empezar sin nada", "problem": "Una caja está vacía. ¿Se pueden sacar 5 lápices de ella?", "steps": ["Cantidad inicial: 0 lápices.", "Quiero sacar 5, pero no hay ninguno.", "No se puede quitar lo que no existe.", "Entonces 0 − 5 no se puede hacer con estos números."], "answer": "No se puede hacer 0 − 5"},
    ],
    mistakes=[
        {"wrong": "Decir que 0 − 8 = 8 porque «es igual que 8 − 0».", "why": "Se piensa que en la resta se pueden cambiar de lugar los números.", "fix": "En la resta el orden importa. 8 − 0 = 8, pero de una caja vacía no puedes quitar 8."},
        {"wrong": "Decir que 8 − 8 = 8.", "why": "Se confunde con restar 0.", "fix": "Si quitas las 8 fichas que hay, no queda ninguna: 8 − 8 = 0."},
    ],
    tiers={
        "recovery": [
            arith("Hay 8 fichas y quitas 0. ¿Cuántas quedan?", "8-0", "No se quita ninguna."),
            arith("Hay 8 fichas y quitas las 8. ¿Cuántas quedan?", "8-8", "Se quitan todas."),
            ex("Una caja está vacía. ¿Puedes sacar 3 lápices de ella?", "No", "No hay lápices que sacar."),
        ],
        "understand": [
            ex("¿Qué dice 6 − 0: que quedan 6 o que quedan 0?", "Quedan 6", "No se quita nada."),
            ex("¿Qué dice 6 − 6: que quedan 6 o que quedan 0?", "Quedan 0", "Se quita todo."),
            ex("¿Se puede hacer 0 − 4 con los números que conoces? Responde sí o no.", "No", "No se puede quitar de una colección vacía."),
        ],
        "apply": [
            arith("Calcula 15 − 0.", "15-0", "Restar 0 deja el mismo número."),
            arith("Calcula 15 − 15.", "15-15", "Quitar todo deja 0."),
            ex("Dos amigos tienen 0 y 7 fichas. ¿Cuál de los dos puede dar 7 fichas a otro?", "El que tiene 7", "El otro no tiene fichas para dar."),
        ],
        "reason": [
            ex("Teo dice que 0 − 9 = 9. ¿Qué error comete?", "Cambia el orden de la resta; de 0 no se pueden quitar 9", "No hay objetos para quitar."),
            ex("Explica la diferencia entre 12 − 0 y 12 − 12.", "En 12 − 0 no se quita nada y queda 12; en 12 − 12 se quita todo y queda 0", "Cambia cuánto se quita."),
        ],
        "challenge": [
            ex("De estas restas, escribe las que se pueden hacer: 0 − 5, 5 − 0, 5 − 5, 0 − 0.", "5 − 0, 5 − 5 y 0 − 0", "Solo falla 0 − 5, porque no hay nada para quitar."),
            ex("Escribe una resta que dé 0 usando el número 30 y otra resta con 30 que dé 30.", "30 − 30 = 0 y 30 − 0 = 30", "Quitar todo da 0; no quitar nada deja 30."),
        ],
    },
    context=[ex("Un estante tiene 11 libros. Si se llevan 0, ¿cuántos quedan? Si se llevan los 11, ¿cuántos quedan?", "11 y 0", "No quitar nada deja 11; quitar todo deja 0.")],
    selfcheck=[arith("Calcula 20 − 0.", "20-0", "Restar 0 deja igual."), arith("Calcula 20 − 20.", "20-20", "Quitar todo deja 0."), ex("¿Se puede hacer 0 − 1?", "No", "No hay nada para quitar.")],
    open_task=task(
        "Hay un plato con 9 fichas y otro vacío. Escribe qué pasa y el resultado de 9 − 0, 9 − 9 y 0 − 9. Dibuja los dos platos con ● para cada ficha. Explica por qué una de las tres no se puede.",
        "9 − 0 = 9: quedan " + "● " * 9 + ". 9 − 9 = 0: no queda ninguna. 0 − 9 no se puede, porque el plato vacío no tiene fichas para quitar.",
        ["resuelve 9 − 0 = 9 y 9 − 9 = 0", "explica que 0 − 9 no se puede", "dibuja los platos"],
        ["tres operaciones escritas", "dibujo", "frase de explicación"],
        ["cambiar el orden de la resta", "creer que 9 − 9 = 9"],
        "Pide que muestre con fichas reales o dibujadas por qué no se puede quitar de un plato vacío.",
    ),
    reinforce="Con 6 fichas, practica quitar 0, quitar 6 y tratar de quitar 6 de un plato vacío. Di qué pasa en cada caso.",
    extend="Escribe una historia corta para 7 − 0 y otra para 7 − 7. Escribe cuánto queda en cada una.",
)

register(
    OA8, 4,
    materials=f"Tarjetas con números dibujadas en este cuaderno y lápiz. {KEY}",
    use="Aprenderé a decir una regla que sirve para cualquier número al sumar o restar 0. Sirve para reconocer que algo es siempre cierto, y no solo en un caso.",
    prior=["Sé que n + 0 = n y n − 0 = n.", "Sé que 0 − n no se puede con estos números."],
    explain=[
        "Ya viste que 14 + 0 = 14 y 19 − 0 = 19. ¿Pasará lo mismo con otros números? Probemos con números chicos y grandes: 6 + 0 = 6, 40 + 0 = 40, 83 − 0 = 83 y 100 − 0 = 100. En todos el resultado es el número del comienzo.",
        "Cuando algo se repite en muchos casos y entendemos por qué, podemos escribir una regla. La regla es: si sumas 0 a un número, o restas 0 a un número, el número no cambia. Se cumple porque 0 significa que no agregas ni quitas nada.",
        "Para explicar bien una regla, muestra ejemplos y di por qué. Un buen ejemplo es un dibujo antes y después. Si el dibujo no cambia, la regla se cumple. No olvides la excepción: 0 − n no se puede hacer cuando n es mayor que 0.",
    ],
    vocab=[("regla", "algo que siempre se cumple"), ("regularidad", "lo que se repite en varios casos"), ("ejemplo", "un caso que muestra la regla"), ("explicar", "decir por qué algo es cierto"), ("excepción", "caso donde la regla no sirve")],
    worked=[
        {"title": "Mirar varios casos", "problem": "Compara 6 + 0, 40 + 0, 83 − 0 y 100 − 0. ¿Qué regla ves?", "steps": ["6 + 0 = 6: es el mismo número.", "40 + 0 = 40: es el mismo número.", "83 − 0 = 83 y 100 − 0 = 100: también es el mismo.", "Regla: sumar o restar 0 no cambia el número."], "answer": "Sumar o restar 0 deja igual el número"},
        {"title": "Usar la regla", "problem": "Sin hacer cuentas, ¿cuánto es 97 + 0 y cuánto es 97 − 0?", "steps": ["Aplico la regla: sumar o restar 0 no cambia el número.", "97 + 0 = 97.", "97 − 0 = 97.", "No necesito contar porque 0 no agrega ni quita."], "answer": "97 y 97"},
    ],
    mistakes=[
        {"wrong": "Decir que la regla solo sirve para números chicos.", "why": "Se prueba solo con unos pocos números.", "fix": "La regla vale para cualquier número, porque el 0 siempre significa «nada»."},
        {"wrong": "Decir que 0 − 6 = 6 por la misma regla.", "why": "Se aplica la regla de n − 0 a una resta distinta.", "fix": "La regla es para restar 0. Con 0 − 6 no hay qué quitar."},
    ],
    tiers={
        "recovery": [
            arith("Calcula 6 + 0.", "6+0", "Sumar 0 deja el mismo número."),
            arith("Calcula 40 + 0.", "40+0", "Sumar 0 deja el mismo número."),
            arith("Calcula 83 − 0.", "83-0", "Restar 0 deja el mismo número."),
        ],
        "understand": [
            ex("¿Qué número queda cuando restas 0 a 100?", "100", "No se quita nada."),
            ex("¿Verdadero o falso? La regla de sumar 0 también sirve con números de dos cifras.", "Verdadero", "El 0 no agrega nada, sin importar el número."),
            ex("Completa la regla: si sumas o restas 0 a un número, el número __.", "no cambia", "El 0 significa ninguna cantidad."),
        ],
        "apply": [
            arith("Sin contar, calcula 100 − 0.", "100-0", "Se aplica la regla."),
            arith("Sin contar, calcula 97 + 0.", "97+0", "Se aplica la regla."),
            ex("Completa: __ − 0 = 56 y 56 + __ = 56.", "56 y 0", "El número que sumas o restas es 0."),
        ],
        "reason": [
            ex("Gaby probó con 2, 5 y 8 y dice que la regla solo sirve para números menores que 10. ¿Qué le responderías?", "Que también sirve con 40, 83 o 100; el 0 no agrega ni quita nada en ningún número", "La razón no depende del tamaño del número."),
            ex("¿Cuál de estas restas no cumple la regla n − 0 = n: 12 − 0, 0 − 12 o 50 − 0?", "0 − 12", "En 0 − 12 el 0 es el número del que se parte, no el que se resta."),
        ],
        "challenge": [
            ex("Escribe una suma y una resta con 0 cuyo resultado sea 70.", "70 + 0 = 70 y 70 − 0 = 70 (también sirve 0 + 70 = 70)", "Sumar o restar 0 a 70 deja 70."),
            arith("Sin contar, calcula 45 + 0 − 0.", "45+0-0", "Cada paso deja el número igual."),
        ],
    },
    context=[arith("Un granjero tiene 100 huevos. Vende 0 y le regalan 0. ¿Cuántos huevos tiene al final?", "100-0+0", "No cambia la cantidad en ningún paso.")],
    selfcheck=[arith("Calcula 75 + 0.", "75+0", "Sumar 0 deja igual."), arith("Calcula 75 − 0.", "75-0", "Restar 0 deja igual."), ex("¿Se puede hacer 0 − 5?", "No", "No hay nada para quitar.")],
    open_task=task(
        "Resuelve estas cuatro operaciones y comprueba cada una con un dibujo de barras y cubos antes y después: 29 + 0, 34 + 0, 38 − 0 y 100 − 0. Escribe una regla con tus palabras y una excepción.",
        "29 + 0 = 29: " + bars(29) + ". 34 + 0 = 34: " + bars(34) + ". 38 − 0 = 38: " + bars(38) + ". 100 − 0 = 100: diez barras de 10. Regla: si sumo o resto 0, el número queda igual. Excepción: 0 − 5 no se puede hacer.",
        ["resuelve las cuatro operaciones", "dibuja antes y después", "escribe la regla y la excepción"],
        ["cuatro operaciones", "dibujos", "regla escrita"],
        ["decir que la regla solo sirve con números chicos", "aplicar la regla a 0 − n"],
        "Pide que lea su regla en voz alta con un ejemplo distinto al de su cuaderno; reconoce la excepción.",
    ),
    reinforce="Usa los números 23, 56 y 91. Escribe para cada uno el número más 0 y el número menos 0.",
    extend="Explica por qué sumar 0 no cambia un número, y por qué una resta como 0 − 5 no sigue la regla.",
)

# ------------------------------------------------------------------ OA 09
register(
    OA9, 1,
    materials=f"Barras y cubos dibujados en este cuaderno, lápiz y fichas. {KEY}",
    use="Aprenderé a juntar y separar cantidades de dos cifras hasta 100 usando decenas y unidades. Sirve para saber cuánto hay en total o cuánto queda.",
    prior=["Sé que 10 unidades forman una decena.", "Sé sumar y restar hasta 20."],
    explain=[
        "Para juntar dos números de dos cifras, junta decenas con decenas y unidades con unidades. Sumar es juntar. Por ejemplo, 32 y 25: las decenas son 3 y 2, que juntas son 5 decenas. Las unidades son 2 y 5, que juntas son 7 unidades. Entonces 32 + 25 = 57.",
        f"En dibujo: {bars(32)} y {bars(25)} se juntan en {bars(57)}. Para separar, haces lo contrario: de 57 quitas 25 y vuelves a 32. Restar es separar una parte del todo. Quitas decenas de las decenas y unidades de las unidades: 57 − 25 = 32.",
        "Para decir lo que hiciste, usa palabras como juntar, agregar, quitar, separar y total. En esta clase las unidades siempre alcanzan, sin tener que cambiar decenas. Escribe siempre el resultado con las palabras y con los números.",
        "Lo que sabes hasta 20 te ayuda con números más grandes, sin calcular otra vez. Como 4 + 3 = 7, entonces 40 + 30 = 70. Como 9 − 4 = 5, entonces 90 − 40 = 50. Con las unidades pasa igual: como 8 − 5 = 3, entonces 68 − 5 = 63.",
    ],
    vocab=[("juntar", "reunir dos cantidades en una"), ("separar", "sacar una parte de una cantidad"), ("total", "resultado de juntar todo"), ("adición", "operación que junta cantidades"), ("sustracción", "operación que quita o separa una parte")],
    worked=[
        {"title": "Juntar 32 y 25", "problem": "Juntas 32 fichas y 25 fichas. ¿Cuántas hay en total?", "steps": ["Junto las decenas: 3 decenas + 2 decenas = 5 decenas.", "Junto las unidades: 2 + 5 = 7 unidades.", "5 decenas y 7 unidades es 57.", "Compruebo: 57 − 25 = 32."], "answer": "57 fichas"},
        {"title": "Separar 25 de 57", "problem": "Hay 57 fichas y separas 25. ¿Cuántas quedan?", "steps": ["Resto las decenas: 5 − 2 = 3 decenas.", "Resto las unidades: 7 − 5 = 2 unidades.", "Quedan 3 decenas y 2 unidades: 32.", "Compruebo: 32 + 25 = 57."], "answer": "32 fichas"},
    ],
    mistakes=[
        {"wrong": "Calcular 32 + 25 como 3 + 2 + 2 + 5 = 12.", "why": "Se suman todas las cifras como si valieran lo mismo.", "fix": "Las decenas se juntan con las decenas: son 5 decenas. Las unidades dan 7. Se escribe 57."},
        {"wrong": "Restar las unidades al revés: 7 − 5 = 12.", "why": "Se suma en vez de restar.", "fix": "Restar es quitar: 7 − 5 = 2."},
    ],
    tiers={
        "recovery": [
            arith("Un grupo tiene 23 fichas y otro tiene 14. ¿Cuántas fichas hay si los juntas?", "23+14", "Se juntan decenas con decenas y unidades con unidades."),
            arith("Hay 36 fichas y separas 12. ¿Cuántas quedan?", "36-12", "Se quitan decenas de decenas y unidades de unidades."),
            ex("Juntas 3 decenas con 2 decenas y 4 unidades con 3 unidades. ¿Qué número formas?", "57", "5 decenas y 7 unidades es 57."),
        ],
        "understand": [
            ex("Para sumar 41 + 23, ¿qué se suma con qué?", "Las decenas con las decenas y las unidades con las unidades", "Cada cifra se junta con la del mismo valor."),
            ex("Si 32 + 25 = 57, ¿cuánto es 57 − 25?", "32", "La resta vuelve a la parte que había."),
            ex("Para restar 78 − 35, ¿cuántas decenas y cuántas unidades quedan?", "4 decenas y 3 unidades", "7 − 3 = 4 decenas y 8 − 5 = 3 unidades."),
        ],
        "apply": [
            arith("Calcula 54 + 25.", "54+25", "4 + 5 = 9 unidades y 5 + 2 = 7 decenas."),
            arith("Calcula 89 − 56.", "89-56", "9 − 6 = 3 unidades y 8 − 5 = 3 decenas."),
            arith("María tiene 45 stickers y recibe 32 más. ¿Cuántos stickers tiene ahora?", "45+32", "Recibir es agregar: 5 + 2 = 7 unidades y 4 + 3 = 7 decenas."),
        ],
        "reason": [
            ex("Luis calculó 32 + 25 = 12 sumando 3 + 2 + 2 + 5. ¿Qué error cometió y cuál es el resultado correcto?", "Sumó todas las cifras como unidades; 3 + 2 = 5 decenas y 2 + 5 = 7 unidades, o sea 57", "Las decenas valen 10 cada una, por eso no se suman con las unidades."),
            ex("Ana dice que 57 − 25 = 82. ¿Qué error cometió y cuál es el resultado correcto?", "Sumó en vez de restar; el resultado es 32", "Separar 25 de 57 deja 32."),
        ],
        "challenge": [
            ex("Sabes que 4 + 3 = 7. Sin hacer cuentas largas, ¿cuánto es 40 + 30?", "70", "4 decenas y 3 decenas son 7 decenas."),
            ex("Sabes que 9 − 4 = 5. Sin calcular otra vez, ¿cuánto es 90 − 40 y cuánto es 69 − 4?", "50 y 65", "9 decenas menos 4 decenas son 5 decenas, y 9 unidades menos 4 unidades son 5 unidades: 60 + 5."),
        ],
    },
    context=[arith("En una biblioteca hay 43 libros de cuentos y 25 libros de ciencias. ¿Cuántos libros hay en total?", "43+25", "Se juntan los dos grupos.")],
    selfcheck=[arith("Calcula 61 + 28.", "61+28", "1 + 8 = 9 unidades y 6 + 2 = 8 decenas."), arith("Calcula 96 − 54.", "96-54", "6 − 4 = 2 unidades y 9 − 5 = 4 decenas."), ex("Si 8 + 1 = 9, ¿cuánto es 80 + 10?", "90", "8 decenas y 1 decena son 9 decenas.")],
    open_task=task(
        "Hay dos bolsas: una con 34 botones y otra con 25 botones. Dibuja cada bolsa con ▮ y ●, junta las dos bolsas y escribe el total. Luego separa 25 del total y escribe cuánto queda. Usa las palabras juntar, separar y total.",
        "Bolsa 1: " + bars(34) + ". Bolsa 2: " + bars(25) + ". Junto: 3 + 2 = 5 decenas y 4 + 5 = 9 unidades, el total es 59 botones. Separo 25: 5 − 2 = 3 decenas y 9 − 5 = 4 unidades, quedan 34.",
        ["junta decenas con decenas y unidades con unidades", "obtiene 59 y luego 34", "dibuja las bolsas", "usa las palabras juntar, separar y total"],
        ["dibujos", "suma y resta escritas", "frase con el vocabulario"],
        ["escribir las sumas parciales sin ordenar posiciones", "sumar en lugar de restar"],
        "Pide que cuente las barras y cubos para comprobar el total; reconoce que usa lenguaje matemático.",
    ),
    reinforce="Con 20 fichas azules y 13 fichas rojas, junta y cuenta cuántas hay. Luego separa las rojas y comprueba que vuelven las azules.",
    extend="Escribe tres parejas de números de dos cifras que se puedan sumar sin cambiar decenas (las unidades suman menos de 10) y calcula cada suma.",
)

register(
    OA9, 2,
    materials="Una recta numérica abierta dibujada por ti (una línea con saltos), lápiz y regla. Todas las cuentas están escritas en los ejercicios.",
    use="Aprenderé a sumar y restar en una recta abierta con saltos de decenas y unidades. Sirve para calcular y mostrar el camino que seguí.",
    prior=["Sé juntar y separar decenas y unidades.", "Sé contar de 10 en 10."],
    explain=[
        "Una recta abierta es una línea sin todos los números escritos. Tú anotas solo los saltos que necesitas. Cada salto hacia la derecha suma, y cada salto hacia la izquierda resta.",
        "Para 46 + 31, empieza en 46. Primero avanza 30, que son tres saltos de decena: llegas a 76. Después avanza 1: llegas a 77. Entonces 46 + 31 = 77. Para restar, haces lo mismo hacia atrás: 58 − 23 es 58, retrocede 20 hasta 38 y retrocede 3 hasta 35.",
        "Haz primero los saltos de las decenas y después los de las unidades. Rotula cada salto con +30, +1, −20 o −3. Así otra persona puede entender tu camino. En esta clase los saltos no cruzan una decena.",
    ],
    vocab=[("recta numérica abierta", "línea donde solo anotas los números que usas"), ("salto", "movimiento que suma o resta en la recta"), ("avanzar", "saltar hacia la derecha para sumar"), ("retroceder", "saltar hacia la izquierda para restar"), ("rotular", "escribir qué hace cada salto")],
    worked=[
        {"title": "Avanzar con saltos", "problem": "Calcula 46 + 31 en una recta abierta.", "steps": ["Empiezo en 46.", "Salto +30: 46 → 76.", "Salto +1: 76 → 77.", "Entonces 46 + 31 = 77."], "answer": "46 + 31 = 77"},
        {"title": "Retroceder con saltos", "problem": "Calcula 58 − 23 en una recta abierta.", "steps": ["Empiezo en 58.", "Salto −20: 58 → 38.", "Salto −3: 38 → 35.", "Entonces 58 − 23 = 35."], "answer": "58 − 23 = 35"},
    ],
    mistakes=[
        {"wrong": "Saltar +3 en vez de +30 para sumar 31.", "why": "Se confunden decenas con unidades.", "fix": "3 decenas son 30. El salto es +30."},
        {"wrong": "Retroceder para sumar o avanzar para restar.", "why": "Se confunde la dirección.", "fix": "Sumar es avanzar a la derecha; restar es retroceder a la izquierda."},
    ],
    tiers={
        "recovery": [
            arith("Estás en 40 de la recta. Das un salto de +20. ¿En qué número caes?", "40+20", "Un salto de +20 suma 2 decenas."),
            arith("Estás en 35. Das un salto de +4. ¿En qué número caes?", "35+4", "Se avanza 4 unidades."),
            ex("En la recta quieres avanzar 31 desde 46. ¿Qué dos saltos das, primero el de las decenas?", "+30 y +1", "31 es 3 decenas y 1 unidad."),
        ],
        "understand": [
            ex("¿Qué salto cambia las decenas: +30 o +3?", "+30", "El salto de 3 decenas es 30."),
            arith("Estás en 77 y retrocedes −30. ¿Qué número tienes?", "77-30", "Retroceder resta."),
            ex("Para 58 − 23, ¿qué dos saltos haces hacia atrás?", "−20 y −3", "23 es 2 decenas y 3 unidades."),
        ],
        "apply": [
            arith("Calcula 62 + 27: +20 hasta 82 y luego +7.", "62+27", "Primero las decenas y luego las unidades."),
            arith("Calcula 58 − 23 con saltos de −20 y −3.", "58-23", "Se retrocede 2 decenas y luego 3 unidades."),
            arith("Calcula 84 − 51: salta −50 y luego −1.", "84-51", "Primero 5 decenas y luego 1 unidad."),
        ],
        "reason": [
            ex("Dani calcula 46 + 31 y salta +3 hasta 49 y +1 hasta 50. ¿Qué error comete y cuál es el resultado?", "Salta 3 unidades en vez de 30; debe saltar +30 hasta 76 y +1 hasta 77", "3 decenas son 30."),
            ex("¿Se llega al mismo número si en 46 + 31 saltas primero +1 y luego +30?", "Sí; se llega a 77", "El orden de los saltos no cambia el total."),
        ],
        "challenge": [
            ex("Empiezas en 20 y haces saltos de +10, +10 y +5. ¿A qué número llegas y qué suma representa?", "45; representa 20 + 25", "10 + 10 + 5 = 25 y 20 + 25 = 45."),
            ex("Llegaste a 68 después de un salto de −30 y otro de −1. ¿En qué número empezaste?", "99", "Se deshace el camino: 68 + 1 = 69 y 69 + 30 = 99."),
        ],
    },
    context=[arith("Un tren lleva 52 pasajeros y suben 36 más. Usa saltos de +30 y +6. ¿Cuántos pasajeros hay?", "52+36", "Se avanza 3 decenas y luego 6 unidades.")],
    selfcheck=[arith("Calcula 31 + 45 con saltos de +40 y +5.", "31+45", "Primero las decenas y luego las unidades."), arith("Calcula 97 − 34 con saltos de −30 y −4.", "97-34", "Se retrocede 3 decenas y 4 unidades."), ex("Para restar, ¿se avanza o se retrocede en la recta?", "Se retrocede", "Restar es ir hacia la izquierda.")],
    open_task=task(
        "Dibuja una recta abierta para cada cuenta: 43 + 25 y 79 − 34. Marca cada salto con su rótulo y escribe el resultado. Después comprueba con otra operación.",
        "43 + 25: empiezo en 43, +20 llego a 63, +5 llego a 68. Resultado 68; compruebo 68 − 25 = 43. 79 − 34: empiezo en 79, −30 llego a 49, −4 llego a 45. Resultado 45; compruebo 45 + 34 = 79.",
        ["marca los saltos con rótulos", "obtiene 68 y 45", "comprueba con la operación contraria"],
        ["dos rectas dibujadas", "resultados", "comprobaciones"],
        ["confundir saltos de decenas con unidades", "saltar en la dirección equivocada"],
        "Pide que cuente el camino de la recta en voz alta; reconoce los rótulos claros.",
    ),
    reinforce="Dibuja una recta y salta desde 25 sumando 10, 10 y 3. Anota en qué números caes.",
    extend="Calcula 36 + 42 con saltos de dos formas distintas y comprueba que llegas al mismo número. Si en tu colegio hay un programa o aplicación de rectas numéricas, repite la cuenta ahí y compara.",
)

register(
    OA9, 3,
    materials=f"Barras y cubos dibujados en este cuaderno y lápiz. {KEY} Las cuentas están escritas en los ejercicios.",
    use="Aprenderé a sumar y restar en columnas, poniendo unidades bajo unidades y decenas bajo decenas. Sirve para calcular con orden y sin equivocarme.",
    prior=["Sé juntar decenas con decenas y unidades con unidades.", "Sé qué es una columna de la tabla DU."],
    explain=[
        "El algoritmo es un orden fijo para calcular. Primero alinea los números: unidades bajo unidades y decenas bajo decenas. Así cada cifra se junta con otra que vale lo mismo.",
        "Para 53 + 26, escribe 53 arriba y 26 debajo. En la columna de las unidades sumas 3 + 6 = 9. En la columna de las decenas sumas 5 + 2 = 7. El resultado tiene 7 decenas y 9 unidades: 79. Para restar, 79 − 26, haces lo mismo: 9 − 6 = 3 unidades y 7 − 2 = 5 decenas, que da 53.",
        "Hay un buen hábito: empieza por las unidades. Escribe cada resultado en su columna. Comprueba con la operación contraria. En esta clase las unidades siempre alcanzan, así que no hay que cambiar decenas.",
    ],
    vocab=[("algoritmo", "pasos en orden para hacer una operación"), ("alinear", "poner las cifras de igual valor una bajo la otra"), ("columna", "fila vertical de cifras del mismo valor"), ("unidades", "cifras de la derecha"), ("decenas", "cifras de la izquierda")],
    worked=[
        {"title": "Sumar en columnas", "problem": "Calcula 53 + 26 con el algoritmo.", "steps": ["Alineo: 3 bajo 6 en unidades y 5 bajo 2 en decenas.", "Unidades: 3 + 6 = 9.", "Decenas: 5 + 2 = 7.", "Resultado: 79. Compruebo: 79 − 26 = 53."], "answer": "79"},
        {"title": "Restar en columnas", "problem": "Calcula 87 − 35 con el algoritmo.", "steps": ["Alineo: 7 bajo 5 en unidades y 8 bajo 3 en decenas.", "Unidades: 7 − 5 = 2.", "Decenas: 8 − 3 = 5.", "Resultado: 52. Compruebo: 52 + 35 = 87."], "answer": "52"},
    ],
    mistakes=[
        {"wrong": "Sumar 45 + 32 con 5 + 3 en una columna y 4 + 2 en otra.", "why": "Se mezclan unidades con decenas porque los números no están alineados.", "fix": "Unidades con unidades: 5 + 2 = 7. Decenas con decenas: 4 + 3 = 7. El resultado es 77."},
        {"wrong": "Restar 87 − 35 como 3 − 8.", "why": "Se resta el número menor del mayor cambiando el orden.", "fix": "Se resta siempre el de abajo del de arriba: 7 − 5 y 8 − 3."},
    ],
    tiers={
        "recovery": [
            ex("Para sumar 53 + 26, ¿qué cifras se suman en la columna de las unidades?", "3 y 6", "Las unidades son las cifras de la derecha."),
            arith("Suma las unidades de 53 + 26: 3 + 6.", "3+6", "Las unidades se suman primero."),
            arith("Suma las decenas de 53 + 26: 5 + 2.", "5+2", "Las decenas se suman después."),
        ],
        "understand": [
            ex("¿Por qué se alinean las unidades con las unidades?", "Porque cada cifra se junta con otra del mismo valor", "Sumar unidades con decenas daría un resultado incorrecto."),
            ex("En 79 − 26, ¿qué se resta en la columna de las decenas?", "7 − 2", "Las decenas son las cifras de la izquierda."),
            ex("En una suma sin reserva, ¿qué número escribes si las decenas dan 6 y las unidades dan 4?", "64", "6 decenas y 4 unidades forman 64."),
        ],
        "apply": [
            arith("Calcula 42 + 36 con el algoritmo.", "42+36", "2 + 6 = 8 unidades y 4 + 3 = 7 decenas."),
            arith("Calcula 65 − 24 con el algoritmo.", "65-24", "5 − 4 = 1 unidad y 6 − 2 = 4 decenas."),
            arith("Calcula 27 + 61 con el algoritmo.", "27+61", "7 + 1 = 8 unidades y 2 + 6 = 8 decenas."),
        ],
        "reason": [
            ex("Tere sumó 45 + 32 y escribió 68, sumando 5 + 3 y 4 + 2. ¿Qué error cometió y cuál es el resultado?", "No alineó: sumó unidades con decenas; el resultado es 77", "5 + 2 = 7 y 4 + 3 = 7."),
            ex("Un compañero escribe 47 − 23 = 70. ¿Cómo sabes que está mal y cuál es el resultado?", "Porque en una resta el resultado es menor que 47; es 24", "7 − 3 = 4 y 4 − 2 = 2."),
        ],
        "challenge": [
            ex("Escribe la cifra que falta: 4_ + 23 = 67.", "4", "44 + 23 = 67, porque 4 + 3 = 7 y 4 + 2 = 6."),
            ex("Escribe la cifra que falta: _8 − 35 = 43.", "7", "78 − 35 = 43, porque 8 − 5 = 3 y 7 − 3 = 4."),
        ],
    },
    context=[arith("Una panadería hizo 64 panes ayer y 35 hoy. ¿Cuántos panes hizo en total?", "64+35", "4 + 5 = 9 unidades y 6 + 3 = 9 decenas.")],
    selfcheck=[arith("Calcula 51 + 38.", "51+38", "1 + 8 = 9 unidades y 5 + 3 = 8 decenas."), arith("Calcula 98 − 47.", "98-47", "8 − 7 = 1 unidad y 9 − 4 = 5 decenas."), ex("¿Qué columna se calcula primero?", "La de las unidades", "Se comienza por la derecha.")],
    open_task=task(
        "Resuelve en columnas 34 + 52, 76 + 23 y 89 − 45. Escribe cada cuenta con los números alineados, el resultado de unidades, el de decenas, y comprueba con la operación contraria.",
        "34 + 52: unidades 4 + 2 = 6, decenas 3 + 5 = 8, resultado 86; compruebo 86 − 52 = 34. 76 + 23: unidades 6 + 3 = 9, decenas 7 + 2 = 9, resultado 99; compruebo 99 − 23 = 76. 89 − 45: unidades 9 − 5 = 4, decenas 8 − 4 = 4, resultado 44; compruebo 44 + 45 = 89.",
        ["alinea unidades y decenas", "obtiene 86, 99 y 44", "comprueba con la operación contraria"],
        ["tres cuentas en columnas", "comprobaciones"],
        ["no alinear las cifras", "sumar en vez de restar"],
        "Pide que explique en voz alta qué columna calcula primero y por qué; reconoce la comprobación.",
    ),
    reinforce="Escribe 23 + 45 en columnas, resuélvela y comprueba restando 45 del resultado.",
    extend="Escribe tres cuentas de suma y tres de resta en columnas, sin reserva, y comprueba cada una.",
)

register(
    OA9, 4,
    materials="Hojas, lápiz y dibujos de barras y cubos hechos por ti. Todos los números están escritos en los problemas.",
    use="Aprenderé a resolver problemas en que algo cambia (se agrega o se quita) y problemas en que se comparan dos cantidades. Sirve para decidir si sumar o restar.",
    prior=["Sé sumar y restar con el algoritmo.", "Sé qué significa «cuántos más» y «cuántos menos»."],
    explain=[
        "En un problema de cambio, una cantidad aumenta o disminuye. Si «ganas», «recibes» o «llegan», se suma. Si «pierdes», «regalas» o «se van», se resta. Fíjate qué le ocurre a la cantidad inicial.",
        "En un problema de comparación, hay dos cantidades y se pregunta por la diferencia: cuántos más o cuántos menos. Si Beto tiene 68 láminas y Ana tiene 45, para saber cuántas más tiene Beto restas: 68 − 45 = 23. La respuesta no es 113, porque no se juntan, se comparan.",
        "Antes de calcular, dibuja una barra para cada cantidad o escribe qué quieres hallar. Después elige la operación. Al final escribe la respuesta con una frase y revisa si tiene sentido.",
    ],
    vocab=[("problema de cambio", "una cantidad aumenta o disminuye"), ("problema de comparación", "se comparan dos cantidades"), ("diferencia", "cuánto más o cuánto menos hay entre dos cantidades"), ("cantidad inicial", "lo que hay al comienzo"), ("respuesta", "frase que dice el resultado con su significado")],
    worked=[
        {"title": "Problema de cambio", "problem": "Jorge tenía 27 cartas y le regalaron 41. ¿Cuántas cartas tiene ahora?", "steps": ["Cantidad inicial: 27. «Le regalaron» significa que aumenta.", "Sumo: 27 + 41.", "Unidades: 7 + 1 = 8. Decenas: 2 + 4 = 6.", "Respuesta: Jorge tiene 68 cartas."], "answer": "68 cartas"},
        {"title": "Problema de comparación", "problem": "Beto tiene 68 láminas y Ana 45. ¿Cuántas más tiene Beto?", "steps": ["Comparo las dos cantidades: 68 y 45.", "Pregunto por la diferencia, entonces resto: 68 − 45.", "Unidades: 8 − 5 = 3. Decenas: 6 − 4 = 2.", "Respuesta: Beto tiene 23 láminas más."], "answer": "23 láminas más"},
    ],
    mistakes=[
        {"wrong": "Sumar 68 + 45 = 113 para saber cuántas más tiene Beto.", "why": "Se juntan las cantidades en vez de compararlas.", "fix": "Para saber cuántas más, se resta la menor de la mayor: 68 − 45 = 23."},
        {"wrong": "Restar siempre porque la pregunta dice «más».", "why": "Se confunde la palabra con la operación.", "fix": "Dibuja la situación: si la cantidad aumenta, se suma; si se comparan, se resta."},
    ],
    tiers={
        "recovery": [
            arith("Tenías 45 figuritas y ganaste 23. ¿Cuántas figuritas tienes ahora?", "45+23", "Ganar aumenta la cantidad."),
            arith("Tenías 58 botones y regalaste 24. ¿Cuántos botones te quedan?", "58-24", "Regalar disminuye la cantidad."),
            ex("Beto tiene 68 láminas y Ana 45. ¿Qué operación sirve para saber cuántas más tiene Beto: 68 − 45 o 68 + 45?", "68 − 45", "Para hallar la diferencia se resta."),
        ],
        "understand": [
            ex("«María tenía 36 bolitas y perdió 12». ¿La cantidad aumenta o disminuye?", "Disminuye", "Perder significa tener menos."),
            ex("En «Ana tiene 45 y Beto tiene 68», ¿qué significa 68 − 45?", "Cuántas más tiene Beto que Ana", "Es la diferencia entre las dos cantidades."),
            ex("¿Qué frase indica una comparación: «ganó 12», «cuántos más» o «regaló 5»?", "«Cuántos más»", "Pregunta por la diferencia entre dos cantidades."),
        ],
        "apply": [
            arith("Beto tiene 68 láminas y Ana tiene 45. ¿Cuántas láminas más tiene Beto?", "68-45", "La diferencia se halla restando."),
            arith("En un bus van 32 niños y 54 adultos. ¿Cuántas personas más son adultos que niños?", "54-32", "Se comparan los adultos con los niños."),
            arith("Jorge tenía 27 cartas y le regalaron 41. ¿Cuántas cartas tiene ahora?", "27+41", "Recibir cartas es agregar."),
        ],
        "reason": [
            ex("Camila compara 68 y 45 para saber cuántas más hay y responde 113. ¿Qué error comete y cuál es la respuesta?", "Sumó en lugar de restar; la diferencia es 23", "68 − 45 = 23."),
            ex("Luis tenía 45 y ahora tiene 78. Dice que ganó 33. ¿Cómo lo comprueba?", "45 + 33 = 78", "La suma de lo inicial más lo que ganó debe dar lo que tiene ahora."),
        ],
        "challenge": [
            arith("Pedro tiene 39 puntos y Sara tiene 20 puntos menos que Pedro. ¿Cuántos puntos tiene Sara?", "39-20", "«Menos que» indica quitar a Pedro."),
            arith("Ana tiene 36 stickers. Gana 22 y luego regala 40. ¿Cuántos stickers le quedan?", "36+22-40", "Primero gana y después regala: 58 − 40."),
        ],
    },
    context=[arith("En el patio hay 46 niños y 32 niñas. ¿Cuántos estudiantes hay?", "46+32", "Se juntan los dos grupos.")],
    selfcheck=[arith("Tenías 75 fichas y perdiste 31. ¿Cuántas te quedan?", "75-31", "Perder disminuye."), arith("Luis tiene 54 puntos y Rosa 23. ¿Cuántos puntos más tiene Luis?", "54-23", "Se compara con resta."), ex("¿Qué indica «recibió» en un problema: sumar o restar?", "Sumar", "Recibir aumenta la cantidad.")],
    open_task=task(
        "Resuelve estos dos problemas: A) Sara tenía 52 hojas y compró 36. ¿Cuántas hojas tiene ahora? B) Tomás tiene 77 canicas y Elena tiene 43. ¿Cuántas canicas más tiene Tomás? Para cada uno dibuja la situación, escribe la operación y responde con una frase.",
        "A) Cambio: 52 + 36 = 88. Sara tiene 88 hojas. B) Comparación: 77 − 43 = 34. Tomás tiene 34 canicas más que Elena.",
        ["distingue un problema de cambio de uno de comparación", "elige suma en A y resta en B", "obtiene 88 y 34", "escribe la respuesta en una frase"],
        ["dibujos", "operaciones", "respuestas en frases"],
        ["sumar las dos cantidades en una comparación", "responder sin frase"],
        "Pide que explique qué palabra del problema lo ayudó a elegir la operación; reconoce el dibujo previo al cálculo.",
    ),
    reinforce="Con 30 botones rojos y 20 botones azules, junta para saber el total y empareja para saber cuántos más hay de un color.",
    extend="Escribe un problema de cambio y uno de comparación que se resuelvan con 64 y 32, y resuélvelos.",
)

register(
    OA9, 5,
    materials="Hojas, lápiz y dibujos de barras y cubos hechos por ti. Los números están escritos en los ejercicios.",
    use="Aprenderé a crear un problema a partir de una cuenta, resolverlo y comprobar el resultado. Sirve para entender mejor qué significa cada operación.",
    prior=["Sé resolver problemas de cambio y de comparación.", "Sé comprobar una suma con una resta."],
    explain=[
        "Crear un problema es contar una historia que se resuelve con una cuenta. Para 72 − 40, puedes decir: «En un frutero había 72 frutas y se comieron 40. ¿Cuántas quedan?». La historia tiene datos, una acción y una pregunta.",
        "Resolver es calcular con lo que aprendiste: 72 − 40 = 32, porque 7 − 4 = 3 decenas y 2 − 0 = 2 unidades. Después escribe la respuesta con una frase: «Quedan 32 frutas».",
        "Comprobar es revisar con la operación contraria. Si 72 − 40 = 32, entonces 32 + 40 debe dar 72. Si no da, hay un error y hay que revisar. También puedes ver si tiene sentido: quedan menos frutas que antes, y eso es lo esperable al quitar.",
    ],
    vocab=[("crear un problema", "inventar una historia con datos y una pregunta"), ("dato", "número o información que da el problema"), ("pregunta", "lo que hay que averiguar"), ("operación contraria", "la que deshace a otra: la suma deshace la resta"), ("tener sentido", "ser posible y lógico en la historia")],
    worked=[
        {"title": "Crear, resolver y comprobar una resta", "problem": "Crea un problema para 72 − 40 y resuélvelo.", "steps": ["Historia: había 72 frutas y se comieron 40. ¿Cuántas quedan?", "Calculo 72 − 40: 7 − 4 = 3 decenas y 2 − 0 = 2 unidades, es 32.", "Respuesta: quedan 32 frutas.", "Compruebo: 32 + 40 = 72."], "answer": "32 frutas"},
        {"title": "Crear y resolver una suma", "problem": "Crea un problema para 45 + 23 y resuélvelo.", "steps": ["Historia: Ana tenía 45 láminas y compró 23. ¿Cuántas tiene ahora?", "Calculo 45 + 23: 5 + 3 = 8 unidades y 4 + 2 = 6 decenas, es 68.", "Respuesta: Ana tiene 68 láminas.", "Compruebo: 68 − 23 = 45."], "answer": "68 láminas"},
    ],
    mistakes=[
        {"wrong": "Comprobar 72 − 40 = 32 con 32 − 40.", "why": "Se resta otra vez en vez de usar la operación contraria.", "fix": "Se comprueba sumando: 32 + 40 = 72."},
        {"wrong": "Crear una historia donde se pierden 40 objetos pero se pregunta cuántos hay en total ahora sin decir cuántos había.", "why": "Falta un dato en el problema.", "fix": "Escribe siempre el dato inicial, la acción y la pregunta."},
    ],
    tiers={
        "recovery": [
            arith("Resuelve 72 − 40.", "72-40", "7 − 4 = 3 decenas y 2 − 0 = 2 unidades."),
            arith("Comprueba sumando: 32 + 40.", "32+40", "Debe volver al 72 del comienzo."),
            ex("Si 32 + 40 = 72, ¿cuánto es 72 − 32?", "40", "La resta deshace la suma."),
        ],
        "understand": [
            ex("Un problema se resuelve con 85 − 31. ¿Es una historia de quitar o de juntar?", "De quitar", "Una resta quita o compara."),
            ex("¿Cuál historia sirve para 56 + 23? A) Tenía 56 y regalé 23. B) Tenía 56 y gané 23.", "B", "Ganar aumenta la cantidad y se suma."),
            ex("¿Con qué operación se comprueba 85 − 31 = 54?", "Con la suma 54 + 31 = 85", "La suma deshace la resta."),
        ],
        "apply": [
            arith("Resuelve 63 + 25.", "63+25", "3 + 5 = 8 unidades y 6 + 2 = 8 decenas."),
            arith("Resuelve 97 − 54.", "97-54", "7 − 4 = 3 unidades y 9 − 5 = 4 decenas."),
            ex("Resuelve y comprueba 76 − 43. Escribe el resultado y la suma de comprobación.", "33; 33 + 43 = 76", "6 − 3 = 3 unidades y 7 − 4 = 3 decenas."),
        ],
        "reason": [
            ex("Mario resolvió 59 − 24 = 35 y comprobó con 35 − 24 = 11. ¿Está bien su comprobación?", "No; debe comprobar con 35 + 24 = 59", "La operación contraria de la resta es la suma."),
            ex("Una historia dice «Pablo tenía 58 y perdió 24, ¿cuántas tiene ahora?» y un niño escribe 58 + 24. ¿Qué operación debe usar?", "58 − 24, porque perdió", "Perder disminuye la cantidad."),
        ],
        "challenge": [
            ex("Escribe el número que falta: __ − 32 = 45.", "77", "45 + 32 = 77."),
            arith("Ana tenía 34 stickers, compró 25 y pegó 40. ¿Cuántos stickers le quedan?", "34+25-40", "Primero 34 + 25 = 59 y luego 59 − 40."),
        ],
    },
    context=[arith("Una tienda tenía 86 cuadernos y vendió 52. ¿Cuántos cuadernos le quedan?", "86-52", "Vender disminuye la cantidad.")],
    selfcheck=[arith("Resuelve 48 + 31.", "48+31", "8 + 1 = 9 unidades y 4 + 3 = 7 decenas."), ex("Comprueba 79 − 35 = 44 con una suma.", "44 + 35 = 79", "La suma deshace la resta."), ex("¿Qué debe tener un problema: datos, acción y pregunta, o solo la pregunta?", "Datos, acción y pregunta", "Sin datos no se puede resolver.")],
    open_task=task(
        "Usa estas cuentas: 64 − 23 y 31 + 56. Para cada una escribe un problema con datos, acción y pregunta, resuélvelo con una frase de respuesta y comprueba con la operación contraria.",
        "64 − 23: «Había 64 caramelos y se comieron 23. ¿Cuántos quedan?» 4 − 3 = 1 unidad y 6 − 2 = 4 decenas, quedan 41; compruebo 41 + 23 = 64. 31 + 56: «Luis tenía 31 cartas y le regalaron 56. ¿Cuántas tiene?» 1 + 6 = 7 y 3 + 5 = 8, tiene 87; compruebo 87 − 56 = 31.",
        ["escribe historias con datos, acción y pregunta", "obtiene 41 y 87", "escribe una frase de respuesta", "comprueba con la operación contraria"],
        ["dos problemas escritos", "resultados", "comprobaciones"],
        ["omitir el dato inicial", "comprobar con la misma operación"],
        "Pide que lea el problema a un compañero o familiar y que esa persona lo resuelva; reconoce las historias claras.",
    ),
    reinforce="Elige la cuenta 55 − 21 y escribe una historia con datos, acción y pregunta. Resuélvela y comprueba.",
    extend="Escribe un problema de comparación que se resuelva con 89 − 54 y un problema de cambio que se resuelva con 35 + 62, y resuélvelos.",
)
