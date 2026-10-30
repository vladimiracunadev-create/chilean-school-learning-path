"""Student material for 2.º básico Matemática, OA 12 (patrones numéricos) y OA 13 (igualdad y desigualdad hasta 20)."""
from __future__ import annotations

from student_content_ma02_f import task
from student_lessons import arith, ex, register

OA12 = "MA02 OA 12"
OA13 = "MA02 OA 13"


def sq(start: int, step: int, count: int) -> list[int]:
    return [start + step * index for index in range(count)]


def show(values: list[int], blanks: tuple[int, ...] = ()) -> str:
    return ", ".join("__" if index in blanks else str(value) for index, value in enumerate(values))


def towers(start: int, step: int, count: int) -> str:
    return " | ".join(f"Torre {i + 1}: {'■' * (start + step * i)} ({start + step * i})" for i in range(count))


# ------------------------------------------------------------------ OA 12
register(
    OA12, 1,
    materials="Una tira de papel con casillas, lápiz y una tabla de números del 1 al 100 dibujada por ti. Todos los patrones están escritos en los ejercicios.",
    use="Aprenderé a descubrir la regla de un patrón que aumenta y a continuarlo. Sirve para predecir qué número viene sin contar desde el principio.",
    prior=["Sé contar de 2 en 2, de 5 en 5 y de 10 en 10.", "Sé sumar números pequeños."],
    explain=[
        "Un patrón numérico es una lista de números que sigue una regla. Cada número se llama término. Si cada término es mayor que el anterior, el patrón aumenta. La regla dice cuánto se suma cada vez.",
        f"Mira {show(sq(12, 5, 4))}. Del 12 al 17 hay 5. Del 17 al 22 hay 5. Del 22 al 27 hay 5. Todas las diferencias son iguales, entonces la regla es «+5». El término que sigue es 27 + 5 = 32.",
        "Para descubrir la regla, resta cada término menos el anterior y mira si siempre da lo mismo. Si no da lo mismo, no es un patrón de suma constante. Después usa la regla para escribir los términos que siguen.",
    ],
    vocab=[("patrón", "lista de números que sigue una regla"), ("regla", "lo que se suma o se resta cada vez"), ("término", "cada número del patrón"), ("aumentar", "ser cada vez mayor"), ("diferencia", "cuánto hay entre un término y el siguiente")],
    worked=[
        {"title": "Descubrir la regla", "problem": f"Mira el patrón {show(sq(12, 5, 4))}. ¿Cuál es la regla y cuál es el siguiente término?", "steps": ["Calculo diferencias: 17 − 12 = 5, 22 − 17 = 5, 27 − 22 = 5.", "Todas son 5: la regla es +5.", "Siguiente término: 27 + 5 = 32.", "Compruebo: 32 − 27 = 5."], "answer": "Regla +5; siguiente 32"},
        {"title": "Usar una regla", "problem": "Un patrón parte en 7 y su regla es +3. Escribe los cuatro primeros términos.", "steps": ["Primer término: 7.", "Segundo: 7 + 3 = 10.", "Tercero: 10 + 3 = 13.", "Cuarto: 13 + 3 = 16."], "answer": "7, 10, 13, 16"},
    ],
    mistakes=[
        {"wrong": "Decir que 2, 5, 9, 12 tiene la regla +3.", "why": "No se revisan todas las diferencias.", "fix": "Las diferencias son 3, 4 y 3. No es un patrón de suma constante."},
        {"wrong": "Continuar 5, 10, 15 con 25.", "why": "Se cambia la regla en el medio.", "fix": "La regla es +5: 15 + 5 = 20."},
    ],
    tiers={
        "recovery": [
            ex(f"Mira el patrón {show(sq(12, 5, 4))}. ¿Cuánto se suma cada vez?", "5", "Cada término es 5 más que el anterior."),
            ex("Continúa el patrón con los dos números que siguen: 3, 6, 9, 12, __, __.", "15 y 18", "Se suma 3 cada vez."),
            ex("Escribe la regla del patrón 10, 20, 30, 40.", "+10", "Cada término es 10 más que el anterior."),
        ],
        "understand": [
            ex("¿El patrón 5, 10, 15, 20 aumenta o disminuye?", "Aumenta", "Cada término es mayor que el anterior."),
            ex("En 2, 4, 6, 8, ¿cuánto hay entre cada par de términos seguidos?", "2", "Las diferencias son todas 2."),
            ex("En 12, 17, 22, 28, ¿qué término no sigue la regla +5?", "28; debía ser 27", "22 + 5 = 27."),
        ],
        "apply": [
            ex("Escribe los cuatro primeros términos de un patrón que parte en 7 con la regla +3.", "7, 10, 13, 16", "Se suma 3 cada vez."),
            ex("Escribe los cinco primeros términos de un patrón que parte en 35 con la regla +10.", "35, 45, 55, 65, 75", "Se suma 10 cada vez."),
            ex("Continúa el patrón: 40, 45, 50, __, __.", "55 y 60", "La regla es +5."),
        ],
        "reason": [
            ex("Ana dice que 2, 5, 9, 12 es un patrón de regla +3. ¿Qué error comete?", "Las diferencias son 3, 4 y 3; el 9 debía ser 8", "Una regla constante suma siempre lo mismo."),
            ex("Un patrón parte en 4 y suma 5 cada vez. ¿Está el 20 en el patrón? Explica.", "No; los términos son 4, 9, 14, 19, 24", "El 19 pasa a 24 sin pasar por 20."),
        ],
        "challenge": [
            ex("Un patrón suma 6 cada vez y el tercer término es 20. ¿Cuáles son los dos primeros términos?", "8 y 14", "14 + 6 = 20 y 8 + 6 = 14."),
            ex("Escribe un patrón de 5 términos que parta en 3 y termine en 23.", "3, 8, 13, 18, 23 (regla +5)", "Entre 3 y 23 hay 20. Con 4 saltos iguales de 5: 5 + 5 + 5 + 5 = 20."),
        ],
    },
    context=[arith("Cada semana Lía pega 5 figuritas más en su álbum. En la semana 1 tiene 12. ¿Cuántas figuritas tiene en la semana 4?", "12+5+5+5", "Se suma 5 por cada semana que pasa después de la primera.")],
    selfcheck=[ex("¿Qué regla tiene 6, 9, 12, 15?", "+3", "Cada término es 3 más que el anterior."), ex("Continúa 20, 25, 30, __.", "35", "La regla es +5."), ex("¿Cómo se llama cada número de un patrón?", "Término", "Los números de la lista son los términos.")],
    open_task=task(
        "Mira estos tres patrones: A) 8, 11, 14, 17. B) 25, 35, 45, 55. C) 6, 10, 15, 21. Para cada uno calcula las diferencias, di si hay regla de suma constante, y si la hay, escribe los dos términos siguientes.",
        "A) Diferencias 3, 3, 3: regla +3, siguen 20 y 23. B) Diferencias 10, 10, 10: regla +10, siguen 65 y 75. C) Diferencias 4, 5, 6: no hay regla de suma constante.",
        ["calcula las diferencias", "reconoce A y B como patrones y C como no constante", "continúa A y B correctamente"],
        ["diferencias escritas", "reglas", "términos siguientes"],
        ["no revisar todas las diferencias", "cambiar la regla a mitad del patrón"],
        "Pide que muestre las diferencias en una tira de papel; reconoce cuando explica por qué C no tiene regla.",
    ),
    reinforce="Escribe en una tira de papel los números 2, 4, 6, 8 y 10 y pinta los términos de un patrón con regla +2.",
    extend="Inventa un patrón con regla +4 que parta en 9 y escribe los seis primeros términos.",
)

register(
    OA12, 2,
    materials="Una tira de papel con casillas, lápiz y una tabla de números del 1 al 100 dibujada por ti. Los patrones están escritos en los ejercicios.",
    use="Aprenderé a descubrir la regla de un patrón que disminuye y a continuarlo sin pasarme de cero. Sirve para predecir cuánto queda cuando algo se gasta de a poco.",
    prior=["Sé continuar un patrón que aumenta.", "Sé restar números pequeños."],
    explain=[
        "Un patrón disminuye cuando cada término es menor que el anterior. La regla dice cuánto se resta cada vez. Por ejemplo, 84, 79, 74, 69 tiene la regla «−5», porque 84 − 5 = 79, 79 − 5 = 74 y 74 − 5 = 69.",
        "Para continuar, resta la regla al último término: 69 − 5 = 64. Para revisar, retrocede en la tabla del 100 de 5 en 5 y mira que caigas en los mismos números. Si en un término la resta no es igual a las anteriores, la regla no es constante.",
        "En estos patrones hay un límite: no escribimos números menores que 0. Si el patrón es 12, 9, 6, 3, el siguiente es 0. Si volvemos a restar 3, el resultado ya sería menor que 0 y el patrón se detiene en 0.",
    ],
    vocab=[("disminuir", "ser cada vez menor"), ("regla de resta", "lo que se quita cada vez"), ("límite", "el número donde el patrón debe detenerse, aquí el 0"), ("término", "cada número del patrón"), ("retroceder", "contar hacia atrás")],
    worked=[
        {"title": "Continuar un patrón que baja", "problem": "Mira 84, 79, 74, 69. ¿Cuál es la regla y qué término sigue?", "steps": ["Calculo: 84 − 79 = 5, 79 − 74 = 5, 74 − 69 = 5.", "La regla es −5.", "Siguiente: 69 − 5 = 64.", "Compruebo: 64 + 5 = 69."], "answer": "Regla −5; siguiente 64"},
        {"title": "Detenerse en el límite", "problem": "En el patrón 12, 9, 6, 3, ¿qué término sigue si no se puede bajar de 0?", "steps": ["La regla es −3.", "3 − 3 = 0, así que el siguiente término es 0.", "Si restara 3 otra vez, ya sería menor que 0.", "El patrón termina en 0."], "answer": "0; allí termina"},
    ],
    mistakes=[
        {"wrong": "Continuar 20, 15, 10 con 5, 0, −5.", "why": "Se sigue restando pasando el límite de 0.", "fix": "El patrón llega a 0 y ahí se detiene."},
        {"wrong": "Continuar 15, 12, 9 con 6, 4, 2.", "why": "Se cambia la regla al restar.", "fix": "La regla es −3: 9 − 3 = 6, 6 − 3 = 3 y 3 − 3 = 0."},
    ],
    tiers={
        "recovery": [
            ex("Mira el patrón 84, 79, 74, 69. ¿Cuánto se resta cada vez?", "5", "Cada término es 5 menos que el anterior."),
            ex("Continúa el patrón: 50, 45, 40, 35, __.", "30", "La regla es −5."),
            ex("¿Qué regla tiene 20, 18, 16, 14?", "−2", "Cada término es 2 menos que el anterior."),
        ],
        "understand": [
            ex("¿El patrón 90, 80, 70, 60 aumenta o disminuye?", "Disminuye", "Cada término es menor que el anterior."),
            ex("En el patrón 84, 79, 74, 69, ¿qué término viene después del 69?", "64", "69 − 5 = 64."),
            ex("Para comprobar que 74 sigue a 79 en el patrón −5, ¿qué cuenta haces?", "79 − 5 = 74", "Se resta la regla al término anterior."),
        ],
        "apply": [
            ex("Escribe los cuatro primeros términos de un patrón que parte en 30 con la regla −3.", "30, 27, 24, 21", "Se resta 3 cada vez."),
            ex("Continúa el patrón: 100, 90, 80, __, __.", "70 y 60", "La regla es −10."),
            ex("Escribe los cuatro primeros términos de un patrón que parte en 40 con la regla −4.", "40, 36, 32, 28", "Se resta 4 cada vez."),
        ],
        "reason": [
            ex("En el patrón 12, 9, 6, 3, ¿cuál es el siguiente término si no puedes escribir números menores que 0?", "0; después ya no se puede seguir", "3 − 3 = 0 y otro paso sería menor que 0."),
            ex("Marta continuó 15, 12, 9 con 6, 4, 2. ¿Qué error cometió y cuáles son los términos correctos?", "Cambió la regla; debía restar 3 y escribir 6, 3 y 0", "La regla es −3."),
        ],
        "challenge": [
            ex("Un patrón resta 7 desde 50. ¿Cuántos términos tiene hasta no pasar de 0 (cuenta el 50)?", "8: 50, 43, 36, 29, 22, 15, 8 y 1", "Después de 1 el siguiente sería menor que 0."),
            ex("Un patrón disminuye 10 cada vez y su cuarto término es 20. ¿En qué número empezó?", "50", "50, 40, 30, 20."),
        ],
    },
    context=[arith("Un tarro tiene 84 galletas y cada día se comen 5. ¿Cuántas galletas hay después de 3 días?", "84-5-5-5", "Cada día se resta 5.")],
    selfcheck=[ex("¿Qué regla tiene 36, 33, 30, 27?", "−3", "Cada término es 3 menos."), ex("Continúa 60, 55, 50, __.", "45", "La regla es −5."), ex("¿Hasta qué número bajamos en estos patrones como máximo?", "Hasta 0", "No escribimos números menores que 0.")],
    open_task=task(
        "Mira estos patrones: A) 60, 54, 48, 42. B) 25, 20, 15. C) 18, 14, 11, 8. Para cada uno calcula las diferencias, di la regla si existe, y escribe los términos siguientes sin pasar de 0.",
        "A) Diferencias 6, 6, 6: regla −6, siguen 36, 30, 24, 18, 12, 6 y 0. B) Diferencias 5 y 5: regla −5, siguen 10, 5 y 0. C) Diferencias 4, 3, 3: no hay regla constante.",
        ["calcula las diferencias", "reconoce que C no tiene regla constante", "continúa A y B hasta 0 sin pasarse"],
        ["diferencias", "reglas", "términos siguientes"],
        ["pasar de 0", "cambiar la regla a mitad"],
        "Pide que cuente hacia atrás en la tabla del 100 para comprobar; reconoce que se detiene en 0.",
    ),
    reinforce="En una tabla del 100, marca con un color 90, 85, 80 y sigue hasta 0 restando 5.",
    extend="Inventa un patrón con regla −6 que parta en 50 y escribe sus términos hasta 2.",
)

register(
    OA12, 3,
    materials="Una tira de papel con casillas vacías, lápiz y una tabla del 100. Los patrones con huecos están escritos en los ejercicios.",
    use="Aprenderé a hallar el número que falta en un patrón usando los términos de al lado. Sirve para completar una lista rota o con partes borradas.",
    prior=["Sé hallar la regla de un patrón.", "Sé sumar y restar de 5 en 5 y de 10 en 10."],
    explain=[
        "A veces a un patrón le falta un término. Mira 24, __, 34 con la regla +5. Para hallar el hueco, puedes avanzar desde 24: 24 + 5 = 29. También puedes retroceder desde 34: 34 − 5 = 29. Los dos caminos dan el mismo número.",
        "Usa los términos vecinos: el que está antes del hueco y el que está después. Si conoces la regla, avanza desde el anterior. Si no la conoces, calcula cuánto hay entre dos términos que sí están. Luego busca qué número, repetido en cada salto, completa esa distancia.",
        "Siempre comprueba al final. Escribe el número en el hueco y revisa que cada diferencia sea igual a la regla. En 24, 29, 34 las diferencias son 5 y 5, entonces está bien.",
    ],
    vocab=[("término faltante", "número que falta en un patrón"), ("hueco", "lugar vacío donde va el término"), ("término vecino", "el término que está justo antes o justo después"), ("avanzar", "sumar la regla"), ("retroceder", "restar la regla")],
    worked=[
        {"title": "Un hueco en el medio", "problem": "En 24, __, 34 la regla es +5. ¿Qué número falta?", "steps": ["Avanzo desde 24: 24 + 5 = 29.", "Retrocedo desde 34: 34 − 5 = 29.", "Las dos formas dan 29.", "Compruebo: 24, 29, 34 tiene diferencias 5 y 5."], "answer": "29"},
        {"title": "Dos huecos juntos", "problem": "En 3, __, __, 12, ¿qué números faltan?", "steps": ["Del 3 al 12 hay 12 − 3 = 9 de diferencia.", "Hay 3 saltos iguales. Como 3 + 3 + 3 = 9, la regla es +3.", "3 + 3 = 6 y 6 + 3 = 9.", "El patrón es 3, 6, 9, 12."], "answer": "6 y 9"},
    ],
    mistakes=[
        {"wrong": "Escribir 30 en 24, __, 34 por «estar en el medio».", "why": "Se adivina el centro sin usar la regla.", "fix": "Se suma la regla al término anterior: 24 + 5 = 29."},
        {"wrong": "Contar mal los saltos en 3, __, __, 12 y creer que hay 2.", "why": "Entre cuatro términos hay tres saltos, no dos.", "fix": "Entre 4 términos seguidos hay 3 saltos."},
    ],
    tiers={
        "recovery": [
            ex("En 24, __, 34 la regla es +5. ¿Qué número va en el medio?", "29", "24 + 5 = 29."),
            ex("Completa el patrón: 10, 12, __, 16.", "14", "La regla es +2."),
            ex("Completa el patrón: 35, 40, __, 50.", "45", "La regla es +5."),
        ],
        "understand": [
            ex("Para hallar el hueco en 24, __, 34, ¿qué sirve: avanzar desde 24 o retroceder desde 34?", "Las dos formas sirven; dan 29", "Los dos términos vecinos llevan al mismo número."),
            ex("Falta un término entre 40 y 50 en un patrón de +5. ¿Cuál es?", "45", "40 + 5 = 45."),
            ex("En __, 18, 21 con la regla +3, ¿qué número falta?", "15", "18 − 3 = 15."),
        ],
        "apply": [
            ex("Completa los dos huecos: 7, __, 15, __, 23.", "11 y 19", "La regla es +4."),
            ex("Completa el hueco: 60, 54, __, 42.", "48", "La regla es −6."),
            ex("Completa el hueco: __, 25, 30, 35.", "20", "25 − 5 = 20."),
        ],
        "reason": [
            ex("En 3, __, __, 12 la regla es siempre la misma. ¿Cuál es la regla y cuáles son los números que faltan?", "Regla +3; faltan 6 y 9", "De 3 a 12 hay 9 en tres saltos iguales."),
            ex("Un compañero completó 8, __, 20 con el 13. ¿Está bien si la regla es la misma en los dos saltos?", "No; debe ir 14", "De 8 a 20 hay 12 en dos saltos iguales: 6 cada uno."),
        ],
        "challenge": [
            ex("Completa los tres huecos: 10, __, __, __, 30.", "15, 20 y 25", "De 10 a 30 hay 20 en cuatro saltos iguales: 5 cada uno."),
            ex("Completa los dos huecos de este patrón que baja: 45, __, __, 30.", "40 y 35", "De 45 a 30 hay 15 en tres saltos iguales: 5 cada uno."),
        ],
    },
    context=[ex("Los casilleros de un camino están numerados 25, 30, __, 40. ¿Qué número tiene el casillero que falta?", "35", "La regla es +5 y 30 + 5 = 35.")],
    selfcheck=[ex("Completa: 6, __, 14 con la regla +4.", "10", "6 + 4 = 10."), ex("Completa: 50, __, 30 con la regla −10.", "40", "50 − 10 = 40."), ex("¿Cuántos saltos hay entre 4 términos seguidos?", "3", "Entre dos términos hay un salto.")],
    open_task=task(
        "Completa estos patrones: A) 14, __, 24. B) 2, __, __, 11. C) 80, __, 60, __. Para cada uno escribe la regla, los números que faltan y cómo comprobaste.",
        "A) Regla +5: falta 19; compruebo 14 + 5 = 19 y 19 + 5 = 24. B) Regla +3: faltan 5 y 8; de 2 a 11 hay 9 en tres saltos de 3. C) Regla −10: faltan 70 y 50; compruebo 80 − 10 = 70, 70 − 10 = 60 y 60 − 10 = 50.",
        ["halla la regla de cada patrón", "completa 19, 5 y 8, 70 y 50", "comprueba cada diferencia"],
        ["reglas escritas", "términos faltantes", "comprobaciones"],
        ["adivinar el término sin usar la regla", "contar mal los saltos"],
        "Pide que muestre cómo comprobó con los dos vecinos; reconoce que revisa todas las diferencias.",
    ),
    reinforce="En una tira de papel, escribe 5, 10, 15, 20, 25, borra uno y pide a otra persona que lo encuentre.",
    extend="Crea un patrón con regla +6, borra dos términos y escribe cómo se pueden recuperar.",
)

register(
    OA12, 4,
    materials="Cubos, bloques o cuadraditos de papel, lápiz y una hoja. Las torres están dibujadas con ■ en este cuaderno.",
    use="Aprenderé a mostrar una regla con torres de cubos, con una tabla y con números. Sirve para ver cómo crece un patrón y predecir la torre que sigue.",
    prior=["Sé hallar la regla de un patrón numérico.", "Sé contar de 2 en 2."],
    explain=[
        "Un patrón también se puede construir con objetos. Si haces torres de 2, 4, 6 y 8 cubos, cada torre tiene 2 cubos más que la anterior. La regla es +2. Se puede mostrar así: " + towers(2, 2, 4) + ".",
        "Una tabla ordena los datos: en una columna escribes el número de la torre y en la otra cuántos cubos tiene. Así ves que la torre 1 tiene 2 cubos, la 2 tiene 4, la 3 tiene 6 y la 4 tiene 8. La regla +2 se ve entre dos números seguidos de la columna de cubos.",
        "Con la regla puedes predecir. La torre 5 tiene 8 + 2 = 10 cubos. También notas que la torre 10 tiene 20 cubos, porque este patrón son los dobles del número de torre. Cada forma de mostrarlo ayuda a entender el patrón.",
    ],
    vocab=[("torre", "cubos apilados uno sobre otro"), ("tabla", "cuadro que ordena datos en columnas"), ("regla", "lo que se suma cada vez"), ("predecir", "decir qué va a pasar antes de que pase"), ("representar", "mostrar un patrón con dibujo, tabla o números")],
    worked=[
        {"title": "Torres que crecen de 2 en 2", "problem": "Torre 1 tiene 2 cubos, torre 2 tiene 4 y torre 3 tiene 6. ¿Cuántos cubos tiene la torre 5?", "steps": ["Diferencias: 4 − 2 = 2 y 6 − 4 = 2: la regla es +2.", "Torre 4: 6 + 2 = 8.", "Torre 5: 8 + 2 = 10.", "Dibujo la torre 5 con 10 cubos."], "answer": "10 cubos"},
        {"title": "Una tabla de torres", "problem": "Las torres tienen 3, 6 y 9 cubos. Completa la tabla hasta la torre 5.", "steps": ["Regla: +3.", "Torre 1: 3. Torre 2: 6. Torre 3: 9.", "Torre 4: 9 + 3 = 12.", "Torre 5: 12 + 3 = 15."], "answer": "3, 6, 9, 12, 15"},
    ],
    mistakes=[
        {"wrong": "Decir que la torre 4 tiene 7 cubos si las torres son 2, 4, 6.", "why": "Se suma 1 en lugar de la regla.", "fix": "La regla es +2: 6 + 2 = 8."},
        {"wrong": "Dibujar la torre 3 con 3 cubos porque «es la tercera».", "why": "Se confunde el número de torre con la cantidad de cubos.", "fix": "La torre 3 tiene 6 cubos en este patrón."},
    ],
    tiers={
        "recovery": [
            ex("Torre 1 tiene 2 cubos, torre 2 tiene 4 y torre 3 tiene 6. ¿Cuántos cubos se agregan en cada torre nueva?", "2", "Las diferencias son 2."),
            ex("Si la torre 4 tiene 8 cubos y se agregan 2 cada vez, ¿cuántos cubos tiene la torre 5?", "10", "8 + 2 = 10."),
            ex("Escribe con un signo la regla de las torres de 2, 4, 6 y 8 cubos.", "+2", "Cada torre tiene 2 cubos más."),
        ],
        "understand": [
            ex(f"Mira {towers(3, 3, 3)}. ¿Cuántos cubos más tiene cada torre que la anterior?", "3", "Las diferencias son 3."),
            ex("En una tabla, ¿qué columna muestra la regla: la del número de torre o la de los cubos?", "La de los cubos", "Entre cubos seguidos se ve cuánto se suma."),
            ex("¿Por qué la torre 4 del patrón 2, 4, 6, … tiene 8 cubos?", "Porque se suma 2 a los 6 de la torre 3", "La regla es +2."),
        ],
        "apply": [
            ex("Una regla +3 empieza en 1 cubo. Escribe los cubos de las torres 1 a 4.", "1, 4, 7, 10", "Se suma 3 cada vez."),
            ex("La tabla dice: torre 1 tiene 3 cubos, torre 2 tiene 6 y torre 3 tiene 9. ¿Cuántos cubos tiene la torre 6?", "18", "Los términos son 3, 6, 9, 12, 15, 18."),
            ex("Torre 1 tiene 4 cubos y cada torre tiene 4 más. ¿Cuántos cubos tiene la torre 5?", "20", "Los términos son 4, 8, 12, 16, 20."),
        ],
        "reason": [
            ex("Una niña construyó torres de 2, 4, 7 y 8 cubos para la regla +2. ¿Qué torre no cumple y cuántos cubos debería tener?", "La tercera; debía tener 6", "4 + 2 = 6."),
            ex("En las torres 2, 4, 6, 8, ¿por qué la torre 10 tendrá 20 cubos?", "Porque cada torre tiene 2 cubos por cada número de torre: 10 × 2 = 20", "Los términos son los dobles del número de torre."),
        ],
        "challenge": [
            ex("La torre 1 tiene 5 cubos y se agregan 5 en cada torre. ¿Qué torre tendrá 25 cubos?", "La torre 5", "Los términos son 5, 10, 15, 20, 25."),
            arith("Hay dos patrones de torres: A (2, 4, 6, 8) y B (1, 3, 5, 7). ¿Cuántos cubos hay juntas las torres 4 de A y de B?", "8+7", "La torre 4 de A tiene 8 y la torre 4 de B tiene 7."),
        ],
    },
    context=[arith("En una pared de bloques, la primera fila tiene 2 bloques y cada fila nueva tiene 2 más. ¿Cuántos bloques tiene la fila 6?", "2+2+2+2+2+2", "Los términos son 2, 4, 6, 8, 10, 12.")],
    selfcheck=[ex("Torres de 3, 5, 7, 9 cubos. ¿Cuál es la regla?", "+2", "Cada torre tiene 2 cubos más."), ex("Torre 1 tiene 6 cubos y la regla es +6. ¿Cuántos cubos tiene la torre 3?", "18", "6, 12, 18."), ex("¿Qué dato de una tabla ayuda a predecir la torre que sigue?", "La regla entre cubos seguidos", "Se suma la regla al último término.")],
    open_task=task(
        "Mira estas torres: Torre 1: ■■■ (3), Torre 2: ■■■■■ (5), Torre 3: ■■■■■■■ (7). Escribe la regla, dibuja con ■ las torres 4 y 5, completa una tabla con los cubos de las torres 1 a 6 y predice cuántos cubos tiene la torre 8.",
        "La regla es +2. Torre 4: ■■■■■■■■■ (9). Torre 5: ■■■■■■■■■■■ (11). Tabla: 3, 5, 7, 9, 11, 13. Torre 7: 15 y torre 8: 17 cubos.",
        ["halla la regla +2", "dibuja las torres 4 y 5 correctas", "completa la tabla con 3, 5, 7, 9, 11 y 13", "predice 17 para la torre 8"],
        ["regla", "dibujo", "tabla", "predicción"],
        ["confundir el número de torre con los cubos", "sumar 1 en vez de la regla"],
        "Pide que compare el dibujo con la tabla y diga si cada torre tiene la cantidad correcta de cubos.",
    ),
    reinforce="Con cubos o papelitos, construye las torres de 1, 3, 5 y 7 y di la regla.",
    extend="Construye un patrón de torres con regla +4 que parta en 2 cubos y escribe las 5 primeras torres en una tabla.",
)

register(
    OA12, 5,
    materials="Hojas, lápiz y una tabla del 100. Los datos para crear los patrones están escritos en los ejercicios.",
    use="Aprenderé a crear un patrón con mi propia regla y a probarlo con otra persona. Sirve para comprobar que mi regla se entiende y funciona.",
    prior=["Sé hallar la regla de un patrón.", "Sé completar términos faltantes."],
    explain=[
        "Para crear un patrón necesitas dos cosas: un primer término y una regla. Con inicio 7 y regla +6 se forma 7, 13, 19, 25. Después puedes seguir agregando términos con la misma regla.",
        "Para probar tu patrón, muestra solo algunos términos a otra persona, por ejemplo 7, 13 y 19. La otra persona tiene que descubrir la regla y escribir el siguiente número. Si dice +6 y 25, tu patrón se entendió. Si se equivoca, quizás hacen falta más términos.",
        "También puedes revisar tu patrón por tu cuenta. Resta cada término menos el anterior: si siempre da lo mismo, la regla es correcta. Así evitas errores antes de mostrárselo a alguien.",
    ],
    vocab=[("crear", "inventar algo nuevo"), ("primer término", "el número con que parte el patrón"), ("regla", "lo que se suma o resta cada vez"), ("probar", "ver si algo funciona"), ("diferencia constante", "la misma diferencia entre todos los términos seguidos")],
    worked=[
        {"title": "Crear un patrón", "problem": "Crea un patrón con inicio 7 y regla +6. Escribe cuatro términos.", "steps": ["Primer término: 7.", "Segundo: 7 + 6 = 13.", "Tercero: 13 + 6 = 19.", "Cuarto: 19 + 6 = 25."], "answer": "7, 13, 19, 25"},
        {"title": "Probar un patrón", "problem": "Un compañero ve solo 7, 13, 19. ¿Puede descubrir la regla y el siguiente término?", "steps": ["Diferencias: 13 − 7 = 6 y 19 − 13 = 6.", "La regla es +6.", "Siguiente: 19 + 6 = 25.", "Sí, tres términos alcanzan para descubrirla."], "answer": "Regla +6; siguiente 25"},
    ],
    mistakes=[
        {"wrong": "Escribir 6, 11, 17, 22 y decir que la regla es +5.", "why": "No se revisó cada diferencia: son 5, 6 y 5.", "fix": "Con regla +5 el patrón es 6, 11, 16, 21."},
        {"wrong": "Entregar solo dos términos y esperar que otro adivine la regla.", "why": "Con dos términos hay muchas reglas posibles.", "fix": "Muestra al menos tres términos."},
    ],
    tiers={
        "recovery": [
            arith("Inicio 7 y regla +6. ¿Cuál es el segundo término?", "7+6", "Se suma la regla al primer término."),
            arith("Inicio 7 y regla +6. ¿Cuál es el tercer término?", "7+6+6", "Se suma la regla dos veces."),
            ex("Escribe los cuatro primeros términos con inicio 7 y regla +6.", "7, 13, 19, 25", "Se suma 6 cada vez."),
        ],
        "understand": [
            ex("Para probar tu patrón, ¿qué debe cumplirse entre todos los términos seguidos?", "Que la diferencia sea siempre la misma", "Esa es la regla constante."),
            ex("Un compañero ve 7, 13, 19. ¿Alcanzan estos términos para descubrir la regla?", "Sí; las diferencias son 6 y 6", "Con tres términos se ven dos diferencias iguales."),
            ex("¿Qué dos datos necesitas para crear un patrón?", "El primer término y la regla", "Con eso se calculan todos los demás."),
        ],
        "apply": [
            ex("Crea un patrón con inicio 4 y regla +9. Escribe cuatro términos.", "4, 13, 22, 31", "Se suma 9 cada vez."),
            ex("Crea un patrón con inicio 50 y regla −8. Escribe cuatro términos.", "50, 42, 34, 26", "Se resta 8 cada vez."),
            ex("Crea un patrón con inicio 15 y regla +10. Escribe cinco términos.", "15, 25, 35, 45, 55", "Se suma 10 cada vez."),
        ],
        "reason": [
            ex("Julia creó 6, 11, 17, 22 con la regla +5. ¿Qué falla y cómo se corrige?", "Entre 11 y 17 hay 6; con regla +5 los términos son 6, 11, 16, 21", "Una regla constante suma siempre lo mismo."),
            ex("A un grupo le muestran 8, 14, 20. Uno dice que la regla es +6 y otro que es +14. ¿Quién tiene razón?", "El que dice +6", "La diferencia entre términos seguidos es 6."),
        ],
        "challenge": [
            ex("Crea un patrón de 4 términos que empiece en 5 y termine en 26.", "5, 12, 19, 26 (regla +7)", "De 5 a 26 hay 21 en tres saltos: 7 cada uno."),
            ex("Un patrón con regla −3 tiene 12 en el quinto término. ¿Cuál es el primer término?", "24", "24, 21, 18, 15, 12."),
        ],
    },
    context=[arith("Las casas de una calle tienen los números 7, 13, 19 y 25 con la regla +6. ¿Qué número tiene la quinta casa?", "25+6", "Se suma 6 al número de la cuarta casa.")],
    selfcheck=[ex("Crea 3 términos con inicio 2 y regla +4.", "2, 6, 10", "Se suma 4 cada vez."), ex("¿Cuántos términos conviene mostrar como mínimo para que otra persona descubra la regla?", "Tres", "Con dos términos hay muchas reglas posibles."), ex("¿Qué regla tiene 9, 15, 21?", "+6", "Las diferencias son 6.")],
    open_task=task(
        "Crea tu propio patrón con inicio 3 y regla +8 (o con inicio 40 y regla −6). Escribe seis términos, calcula las diferencias para probar que está bien, y escribe los tres primeros para que otra persona descubra la regla y el siguiente.",
        "Con inicio 3 y regla +8: 3, 11, 19, 27, 35, 43. Diferencias: 8, 8, 8, 8, 8. Para el compañero: 3, 11, 19; debe descubrir +8 y el siguiente, 27.",
        ["crea seis términos con la regla elegida", "calcula las diferencias y son iguales", "muestra tres términos y pide la regla y el siguiente"],
        ["seis términos", "diferencias", "tres términos para el compañero"],
        ["cambiar la regla a mitad", "mostrar solo dos términos"],
        "Pide que otra persona resuelva el patrón y que quien lo creó revise la respuesta; reconoce las diferencias bien calculadas.",
    ),
    reinforce="Con inicio 10 y regla +3, escribe seis términos y pide a otra persona que descubra la regla con los tres primeros.",
    extend="Crea un patrón de resta con inicio 60 y regla −7 y muestra hasta qué término puedes llegar sin pasar de 0. Si en tu colegio hay un programa o aplicación para crear patrones numéricos, repite el patrón ahí y compara.",
)

# ------------------------------------------------------------------ OA 13
register(
    OA13, 1,
    materials="Una balanza dibujada con dos platos, 20 fichas o cubos y lápiz. Las sumas están escritas en los ejercicios.",
    use="Aprenderé que una igualdad dice que dos lados valen lo mismo. Sirve para ver que sumas distintas pueden dar el mismo número.",
    prior=["Sé sumar hasta 20.", "Sé qué significa «es lo mismo que»."],
    explain=[
        "El signo = significa «es lo mismo que». En 7 + 3 = 6 + 4, el lado izquierdo y el lado derecho valen lo mismo. Si pones 7 cubos y 3 cubos en un plato de una balanza, y 6 cubos y 4 cubos en el otro, la balanza queda equilibrada. Cada plato tiene 10 cubos.",
        "Dos sumas distintas pueden valer lo mismo. 7 + 3 y 6 + 4 son diferentes, pero las dos dan 10. Una igualdad es verdadera cuando los dos lados dan el mismo número.",
        "Para revisar una igualdad, calcula cada lado por separado. Si 8 + 2 = 10 y 5 + 5 = 10, entonces 8 + 2 = 5 + 5 es verdadera. Si un lado da 11 y el otro 10, la igualdad es falsa.",
    ],
    vocab=[("igualdad", "dos lados que valen lo mismo"), ("signo igual (=)", "significa «es lo mismo que»"), ("lado", "cada parte a la izquierda o a la derecha del signo ="), ("equilibrada", "con el mismo peso o valor en los dos lados"), ("expresión", "una suma o resta escrita, como 7 + 3")],
    worked=[
        {"title": "Comprobar una igualdad", "problem": "¿Es verdadera la igualdad 7 + 3 = 6 + 4?", "steps": ["Calculo el lado izquierdo: 7 + 3 = 10.", "Calculo el lado derecho: 6 + 4 = 10.", "Los dos lados valen 10.", "La igualdad es verdadera."], "answer": "Verdadera"},
        {"title": "Una igualdad falsa", "problem": "¿Es verdadera la igualdad 4 + 5 = 5 + 5?", "steps": ["Lado izquierdo: 4 + 5 = 9.", "Lado derecho: 5 + 5 = 10.", "9 no es lo mismo que 10.", "La igualdad es falsa."], "answer": "Falsa"},
    ],
    mistakes=[
        {"wrong": "Decir que 4 + 5 = 5 + 5 porque «los dos tienen un 5».", "why": "Se mira una cifra en vez de calcular cada lado.", "fix": "Calcula: 4 + 5 = 9 y 5 + 5 = 10; no son iguales."},
        {"wrong": "Pensar que el signo = siempre significa «escribe el resultado».", "why": "Se cree que el signo solo anuncia una respuesta.", "fix": "Significa que los dos lados valen lo mismo."},
    ],
    tiers={
        "recovery": [
            arith("Calcula 7 + 3.", "7+3", "Siete y tres forman diez."),
            arith("Calcula 6 + 4.", "6+4", "Seis y cuatro forman diez."),
            ex("¿Valen lo mismo los dos lados de 7 + 3 = 6 + 4?", "Sí; los dos valen 10", "Ambos lados dan 10."),
        ],
        "understand": [
            ex("¿Cuál igualdad es verdadera: 8 + 2 = 5 + 5 o 8 + 2 = 6 + 5?", "8 + 2 = 5 + 5", "Los dos lados dan 10."),
            ex("¿Qué significa el signo = en 9 + 1 = 8 + 2?", "Que los dos lados valen lo mismo", "Ambos lados valen 10."),
            ex("Completa para que sea verdadera: 6 + 6 = 10 + __.", "2", "6 + 6 = 12 y 10 + 2 = 12."),
        ],
        "apply": [
            ex("Completa para que sea verdadera: 5 + 9 = 7 + __.", "7", "5 + 9 = 14 y 7 + 7 = 14."),
            ex("Completa para que sea verdadera: 12 = 5 + __.", "7", "5 + 7 = 12."),
            ex("Escribe una suma distinta que sea igual a 8 + 7.", "Por ejemplo 9 + 6 (también 10 + 5 u 11 + 4)", "8 + 7 = 15 y 9 + 6 = 15."),
        ],
        "reason": [
            ex("Dani dice que 4 + 5 = 5 + 5 porque los dos tienen un 5. ¿Qué error comete?", "Los lados valen 9 y 10; no son iguales", "Hay que calcular cada lado."),
            ex("¿Se puede cambiar el orden en 3 + 8 = 8 + 3? Explica.", "Sí; los dos lados valen 11", "Las mismas partes dan el mismo total."),
        ],
        "challenge": [
            ex("Escribe tres sumas distintas que sean iguales a 12.", "Por ejemplo 6 + 6, 5 + 7 y 4 + 8 (también 3 + 9 o 10 + 2)", "Todas dan 12."),
            ex("Completa para que sea verdadera: 8 + __ = 6 + 7.", "5", "6 + 7 = 13 y 8 + 5 = 13."),
        ],
    },
    context=[ex("Una balanza tiene 7 cubos y 3 cubos en un plato y 6 cubos y 4 cubos en el otro. ¿Está equilibrada?", "Sí; cada plato tiene 10 cubos", "7 + 3 = 6 + 4 = 10.")],
    selfcheck=[ex("¿Es verdadera 9 + 3 = 8 + 4?", "Sí", "Los dos lados dan 12."), ex("Completa: 10 + 2 = 7 + __.", "5", "10 + 2 = 12 y 7 + 5 = 12."), arith("Calcula 6 + 8.", "6+8", "Es parte de la igualdad 6 + 8 = 7 + 7.")],
    open_task=task(
        "Mira estas tres igualdades: A) 9 + 4 = 8 + 5. B) 6 + 7 = 7 + 7. C) 10 + 3 = 9 + 4. Calcula cada lado, di cuál es falsa y dibuja con ● los dos platos de una balanza para la A.",
        "A) 13 = 13, verdadera. B) 13 y 14, falsa. C) 13 = 13, verdadera. Balanza A: plato 1 con ●●●●●●●●● ●●●● (9 y 4) y plato 2 con ●●●●●●●● ●●●●● (8 y 5), 13 en cada plato.",
        ["calcula cada lado", "detecta que B es falsa", "dibuja dos platos equilibrados"],
        ["cálculos", "clasificación", "dibujo de la balanza"],
        ["decidir por una cifra repetida", "no calcular ambos lados"],
        "Pide que cuente las fichas de cada plato y diga cuánto hay en cada uno antes de decidir.",
    ),
    reinforce="Con 12 fichas, forma tres pares de grupos distintos que sumen 12 y escribe cada igualdad.",
    extend="Escribe una igualdad con una suma de dos números a la izquierda y una suma de tres números a la derecha.",
)

register(
    OA13, 2,
    materials="Fichas o cubos, una balanza dibujada y lápiz. Las igualdades están escritas en los ejercicios.",
    use="Aprenderé que una igualdad se puede leer en los dos sentidos y que el signo = no siempre va antes del resultado. Sirve para no confundirme cuando el resultado está al comienzo.",
    prior=["Sé que el signo = significa «es lo mismo que».", "Sé comprobar si dos lados valen lo mismo."],
    explain=[
        "Muchas veces escribimos primero la suma y después el resultado: 7 + 5 = 12. Pero también se puede escribir al revés: 12 = 7 + 5. Ambas dicen lo mismo, porque 12 y 7 + 5 valen lo mismo.",
        "El signo = no es una orden de calcular. Es una señal de equilibrio entre los dos lados. Por eso puedes tener una suma a cada lado: 7 + 5 = 6 + 6. También puedes tener solo números: 12 = 12.",
        "Lee con cuidado de izquierda a derecha o de derecha a izquierda. Lo importante es que cada lado dé el mismo número. Si el resultado está primero, calcula la suma del otro lado y compara.",
    ],
    vocab=[("lado izquierdo", "lo que está antes del signo ="), ("lado derecho", "lo que está después del signo ="), ("equilibrio", "los dos lados valen lo mismo"), ("al revés", "leído desde el otro lado"), ("verdadera", "que se cumple, que es cierta")],
    worked=[
        {"title": "Leer al revés", "problem": "Escribe 7 + 5 = 12 de otra forma.", "steps": ["Cambio de lugar los dos lados.", "12 queda a la izquierda y 7 + 5 a la derecha.", "Escribo 12 = 7 + 5.", "Sigue siendo verdadera: 12 y 7 + 5 valen lo mismo."], "answer": "12 = 7 + 5"},
        {"title": "Una suma a cada lado", "problem": "¿Es verdadera 7 + 5 = 6 + 6?", "steps": ["Lado izquierdo: 7 + 5 = 12.", "Lado derecho: 6 + 6 = 12.", "Los dos valen 12.", "Es verdadera."], "answer": "Verdadera"},
    ],
    mistakes=[
        {"wrong": "Decir que 12 = 7 + 5 está mal porque «el resultado va al final».", "why": "Se cree que el signo = solo se escribe antes del resultado.", "fix": "El signo = dice que ambos lados valen lo mismo, en cualquier orden."},
        {"wrong": "Completar 12 = 7 + __ con 12.", "why": "Se copia el número sin pensar qué falta.", "fix": "7 + 5 = 12, entonces falta 5."},
    ],
    tiers={
        "recovery": [
            ex("Lee 12 = 7 + 5. ¿Dice lo mismo que 7 + 5 = 12?", "Sí", "Ambos lados valen lo mismo."),
            ex("Completa: 15 = 9 + __.", "6", "9 + 6 = 15."),
            arith("Calcula 8 + 8.", "8+8", "Es el lado derecho de 16 = 8 + 8."),
        ],
        "understand": [
            ex("¿Qué lado queda a la izquierda en 14 = 6 + 8?", "El 14", "Está antes del signo =."),
            ex("¿Es verdadera 13 = 9 + 4?", "Sí", "9 + 4 = 13."),
            ex("¿Es verdadera 11 = 5 + 5?", "No; 5 + 5 = 10", "10 no es 11."),
        ],
        "apply": [
            ex("Escribe 16 = 8 + 8 de la otra forma.", "8 + 8 = 16", "Se cambian los lados de lugar."),
            ex("Completa: 10 = __ + 4.", "6", "6 + 4 = 10."),
            ex("Completa: 7 + 5 = 6 + __.", "6", "7 + 5 = 12 y 6 + 6 = 12."),
        ],
        "reason": [
            ex("Mario dice que 18 = 9 + 9 está mal porque el resultado debería ir al final. ¿Qué le responderías?", "Es verdadera; el signo = significa que ambos lados valen lo mismo", "9 + 9 = 18."),
            ex("Explica por qué 8 + 4 = 12 y 12 = 8 + 4 dicen lo mismo.", "Porque 12 y 8 + 4 valen lo mismo y solo cambian de lado", "El signo = solo muestra equilibrio."),
        ],
        "challenge": [
            ex("Escribe dos igualdades que empiecen con 18 a la izquierda del signo.", "18 = 9 + 9 y 18 = 10 + 8 (también 18 = 11 + 7)", "Cada suma de la derecha debe dar 18."),
            ex("Completa la igualdad con un número del 0 al 20: 15 = 20 − __.", "5", "20 − 5 = 15."),
        ],
    },
    context=[ex("Una caja tiene 12 lápices: 7 azules y 5 rojos. Escribe la igualdad con el número total al comienzo.", "12 = 7 + 5", "El total vale lo mismo que las dos partes juntas.")],
    selfcheck=[ex("Escribe 9 + 6 = 15 al revés.", "15 = 9 + 6", "Se cambian los lados de lugar."), ex("¿Es verdadera 14 = 7 + 7?", "Sí", "7 + 7 = 14."), ex("Completa: 13 = 8 + __.", "5", "8 + 5 = 13.")],
    open_task=task(
        "Mira las igualdades: 17 = 9 + 8, 11 = 6 + 6 y 14 = 7 + 7. Revisa cuál es falsa y cámbiala para que sea verdadera. Luego escribe las dos verdaderas al revés y explica con una frase qué significa el signo =.",
        "17 = 9 + 8 es verdadera (17 = 17). 11 = 6 + 6 es falsa, porque 6 + 6 = 12; puede ser 12 = 6 + 6 o 11 = 6 + 5. 14 = 7 + 7 es verdadera. Al revés: 9 + 8 = 17 y 7 + 7 = 14. El signo = significa que los dos lados valen lo mismo.",
        ["revisa cada igualdad calculando el lado de la suma", "detecta que 11 = 6 + 6 es falsa", "escribe las verdaderas al revés", "explica el signo ="],
        ["cálculos", "corrección", "igualdades al revés", "frase"],
        ["creer que el resultado solo va al final", "no calcular el lado de la suma"],
        "Pide que lea cada igualdad en voz alta con las palabras «es lo mismo que»; reconoce que explica el signo.",
    ),
    reinforce="Escribe tres igualdades con el resultado al comienzo para sumas con el 10 como uno de los números.",
    extend="Explica por qué 8 + 4 = 12 y 5 + 7 = 12 permiten escribir 8 + 4 = 5 + 7.",
)

register(
    OA13, 3,
    materials="Fichas o cubos, una recta numérica del 0 al 20 dibujada por ti y lápiz. Los números están en los ejercicios.",
    use="Aprenderé a comparar dos cantidades con los signos > y <. Sirve para decir cuál número o suma es mayor o menor.",
    prior=["Sé que el signo = indica que dos lados son iguales.", "Sé contar hasta 20."],
    explain=[
        "Si dos lados no valen lo mismo, usamos los signos > y <. El signo > significa «mayor que» y el signo < significa «menor que». La boca del signo siempre se abre hacia el número mayor.",
        "Mira 16 y 11. El 16 es mayor, y se escribe 16 > 11. Se lee «dieciséis es mayor que once». También se puede leer al revés: 11 < 16, «once es menor que dieciséis». Es la misma verdad con los números en otro orden.",
        "Cuando uno de los lados es una suma o una resta, primero calcula su valor. Para 8 + 5 y 12, calcula 8 + 5 = 13. Como 13 es mayor que 12, escribes 8 + 5 > 12. No decidas mirando los números sueltos, sino los valores.",
    ],
    vocab=[("mayor que (>)", "tiene más cantidad"), ("menor que (<)", "tiene menos cantidad"), ("igual (=)", "tiene la misma cantidad"), ("comparar", "decidir si una cantidad es mayor, menor o igual a otra"), ("desigualdad", "relación en la que los dos lados no valen lo mismo")],
    worked=[
        {"title": "Comparar dos números", "problem": "Compara 16 y 11 con un signo.", "steps": ["16 es mayor que 11.", "La boca del signo se abre hacia el 16.", "Escribo 16 > 11.", "Leído al revés es 11 < 16."], "answer": "16 > 11"},
        {"title": "Comparar una suma con un número", "problem": "Compara 8 + 5 con 12.", "steps": ["Calculo 8 + 5 = 13.", "Comparo 13 con 12: 13 es mayor.", "Escribo 8 + 5 > 12.", "Compruebo con una recta: 13 está después de 12."], "answer": "8 + 5 > 12"},
    ],
    mistakes=[
        {"wrong": "Escribir 11 > 16.", "why": "Se invierte el signo.", "fix": "La boca se abre hacia el mayor: 16 > 11, o 11 < 16."},
        {"wrong": "Escribir 6 + 5 > 12 sin calcular la suma.", "why": "No se calcula el valor de cada lado antes de comparar.", "fix": "6 + 5 = 11 y 11 < 12, entonces 6 + 5 < 12."},
    ],
    tiers={
        "recovery": [
            ex("Escribe >, < o =: 16 __ 11.", "16 > 11", "16 es mayor que 11."),
            ex("Escribe >, < o =: 7 __ 12.", "7 < 12", "7 es menor que 12."),
            ex("Escribe >, < o =: 9 __ 9.", "9 = 9", "Son el mismo número."),
        ],
        "understand": [
            ex("¿Hacia qué número se abre la boca del signo?", "Hacia el número mayor", "Así se reconoce el signo > o <."),
            ex("¿Cómo se lee 11 < 16?", "Once es menor que dieciséis", "El signo < significa menor que."),
            ex("Si 16 > 11, ¿qué signo va en 11 __ 16?", "<", "Es la misma relación leída al revés."),
        ],
        "apply": [
            ex("Escribe >, < o =: 8 + 5 __ 12.", "8 + 5 > 12", "8 + 5 = 13 y 13 > 12."),
            ex("Escribe >, < o =: 15 − 6 __ 10.", "15 − 6 < 10", "15 − 6 = 9 y 9 < 10."),
            ex("Escribe >, < o =: 7 + 7 __ 14.", "7 + 7 = 14", "7 + 7 = 14."),
        ],
        "reason": [
            ex("Lía escribió 6 + 5 > 12. ¿Qué error cometió y cómo se corrige?", "6 + 5 = 11 y 11 < 12; debe ser 6 + 5 < 12", "Hay que calcular la suma antes de comparar."),
            ex("¿Qué número es mayor que 15 y menor que 17?", "16", "16 está entre 15 y 17."),
        ],
        "challenge": [
            ex("Escribe un número del 0 al 20 que sea mayor que 8 + 9 y menor que 19.", "18", "8 + 9 = 17 y el único número entre 17 y 19 es 18."),
            ex("Ordena de menor a mayor: 9 + 3, 20 − 9 y 14.", "20 − 9, 9 + 3 y 14", "Los valores son 11, 12 y 14."),
        ],
    },
    context=[ex("Ana tiene 16 figuritas y Beto tiene 11. Escribe la comparación con un signo.", "16 > 11", "Ana tiene más figuritas.")],
    selfcheck=[ex("Escribe >, < o =: 5 + 6 __ 10.", "5 + 6 > 10", "5 + 6 = 11 y 11 > 10."), ex("Escribe >, < o =: 18 __ 13.", "18 > 13", "18 es mayor que 13."), ex("Si 9 < 14, ¿qué signo va en 14 __ 9?", ">", "Es la misma relación leída al revés.")],
    open_task=task(
        "Compara estos tres pares con el signo correcto y explica cada decisión: 17 y 12; 9 + 4 y 15; 6 + 8 y 14. Construye 17 y 12 con fichas o dibújalos con ● y confirma el signo.",
        "17 > 12 porque 17 es mayor. 9 + 4 < 15 porque 13 es menor que 15. 6 + 8 = 14 porque 14 y 14 son iguales. Dibujo: ●●●●●●●●●●●●●●●●● (17) y ●●●●●●●●●●●● (12), el primero tiene más.",
        ["usa el signo correcto en los tres pares", "calcula las sumas antes de comparar", "dibuja y confirma el signo"],
        ["tres comparaciones", "explicaciones", "dibujo"],
        ["invertir el signo", "comparar sin calcular la suma"],
        "Pide que lea cada comparación con «mayor que», «menor que» o «igual a»; reconoce el cálculo previo de las sumas.",
    ),
    reinforce="Escribe en tarjetas los números 8, 13, 7 + 6, 10 + 3 y 12. Compara de a dos con >, < o =.",
    extend="Escribe tres comparaciones con una resta a un lado y un número al otro, y resuélvelas.",
)

register(
    OA13, 4,
    materials="Fichas o cubos, una recta numérica del 0 al 20 dibujada por ti y lápiz. Las relaciones están escritas en los ejercicios.",
    use="Aprenderé a buscar los números que hacen verdadera una igualdad o una desigualdad con un hueco. Sirve para resolver «cuántos me faltan» y «cuántos pueden ser».",
    prior=["Sé usar =, > y <.", "Sé calcular sumas y restas hasta 20."],
    explain=[
        "A veces una relación tiene un hueco: __ + 5 < 12. Hay que probar números en el hueco y ver si la relación queda verdadera. Con 3: 3 + 5 = 8 y 8 < 12, es verdadera. Con 7: 7 + 5 = 12 y 12 no es menor que 12, es falsa.",
        "En una igualdad como __ + 5 = 12, solo un número sirve: el 7. En una desigualdad como __ + 5 < 12, sirven varios: 0, 1, 2, 3, 4, 5 y 6. El 7 ya produce una igualdad, y los números mayores producen sumas más grandes que 12.",
        "Para no perderte, prueba los números en orden desde el 0. Anota los que funcionan. Cuando un número deja de funcionar y los siguientes tampoco, puedes parar. Siempre comprueba calculando.",
    ],
    vocab=[("hueco", "lugar donde falta un número"), ("probar", "poner un número en el hueco para ver si sirve"), ("verdadera", "que se cumple"), ("falsa", "que no se cumple"), ("solución", "número que hace verdadera la relación")],
    worked=[
        {"title": "Una desigualdad con hueco", "problem": "¿Qué números del 0 al 20 hacen verdadera __ + 5 < 12?", "steps": ["Pruebo 0: 0 + 5 = 5 y 5 < 12, sirve.", "Pruebo 6: 6 + 5 = 11 y 11 < 12, sirve.", "Pruebo 7: 7 + 5 = 12 y 12 no es menor que 12, no sirve.", "Sirven 0, 1, 2, 3, 4, 5 y 6."], "answer": "0, 1, 2, 3, 4, 5 y 6"},
        {"title": "Una igualdad con hueco", "problem": "¿Qué número hace verdadera __ + 5 = 12?", "steps": ["Pregunto: ¿qué número más 5 da 12?", "12 − 5 = 7.", "Compruebo: 7 + 5 = 12.", "Solo sirve el 7."], "answer": "7"},
    ],
    mistakes=[
        {"wrong": "Decir que el 7 hace verdadera __ + 5 < 12.", "why": "7 + 5 = 12 y 12 no es menor que 12.", "fix": "Con 7 se forma una igualdad, no una desigualdad."},
        {"wrong": "Decir que en __ + 5 < 12 solo sirve un número.", "why": "Se piensa que todas las relaciones tienen una única solución.", "fix": "En una desigualdad pueden servir varios números."},
    ],
    tiers={
        "recovery": [
            ex("Prueba el 3 en __ + 5 < 12. ¿Es verdadera?", "Sí; 3 + 5 = 8 y 8 < 12", "8 es menor que 12."),
            ex("Prueba el 7 en __ + 5 = 12. ¿Es verdadera?", "Sí; 7 + 5 = 12", "Los dos lados valen 12."),
            ex("Prueba el 8 en __ + 5 < 12. ¿Es verdadera?", "No; 8 + 5 = 13 y 13 no es menor que 12", "13 es mayor que 12."),
        ],
        "understand": [
            ex("¿Cuál es el único número que hace verdadera __ + 5 = 12?", "7", "12 − 5 = 7."),
            ex("¿Cuántos números hacen verdadera 9 + __ = 15?", "Uno; el 6", "En una igualdad hay un solo número."),
            ex("¿Sirve el 7 en __ + 5 < 12?", "No; da 12 y 12 no es menor que 12", "Se forma una igualdad."),
        ],
        "apply": [
            ex("Escribe todos los números del 0 al 20 que hacen verdadera __ + 5 < 12.", "0, 1, 2, 3, 4, 5 y 6", "Con 7 la suma ya es 12."),
            ex("Escribe el número que hace verdadera __ − 4 = 9.", "13", "13 − 4 = 9."),
            ex("Escribe todos los números del 0 al 20 que hacen verdadera 15 > __ + 10.", "0, 1, 2, 3 y 4", "Con 5 se forma 10 + 5 = 15, que no es menor."),
        ],
        "reason": [
            ex("Pía dice que 6 y 7 hacen verdadera __ + 5 < 12. ¿Tiene razón?", "Con el 6 sí; con el 7 no", "6 + 5 = 11, pero 7 + 5 = 12."),
            ex("¿Por qué 7 ya forma una igualdad y no una desigualdad en __ + 5 < 12?", "Porque 7 + 5 = 12 y 12 no es menor que 12", "Menor que no incluye el igual."),
        ],
        "challenge": [
            ex("Escribe los números del 0 al 20 que hacen verdaderas 10 < __ + 4 y __ < 9 a la vez.", "7 y 8", "7 + 4 = 11 y 8 + 4 = 12 son mayores que 10, y 7 y 8 son menores que 9."),
            ex("¿Cuántos números del 0 al 20 hacen verdadera __ > 17?", "3: 18, 19 y 20", "Son los únicos mayores que 17."),
        ],
    },
    context=[ex("Un ascensor puede llevar menos de 12 personas. Ya hay 5. ¿Cuántas personas pueden subir como máximo sin llegar a 12?", "6", "5 + 6 = 11, que es menor que 12.")],
    selfcheck=[ex("¿Qué número hace verdadera __ + 3 = 10?", "7", "10 − 3 = 7."), ex("¿Sirve el 4 en __ + 6 < 11?", "Sí", "4 + 6 = 10 y 10 < 11."), ex("¿Cuántos números hacen verdadera 8 + __ = 14?", "Uno; el 6", "En una igualdad hay un solo número.")],
    open_task=task(
        "Busca los números del 0 al 20 que hacen verdaderas estas relaciones: A) __ + 6 = 14. B) __ + 6 < 14. C) 12 > __ + 5. Prueba en orden desde el 0, anota los que sirven y escribe cuál es el primero que ya no sirve en B y en C.",
        "A) 8, porque 8 + 6 = 14. B) 0, 1, 2, 3, 4, 5, 6 y 7; el primero que ya no sirve es el 8, porque 8 + 6 = 14 y 14 no es menor que 14. C) 0, 1, 2, 3, 4, 5 y 6; el primero que ya no sirve es el 7, porque 7 + 5 = 12 y 12 no es mayor que 12 sino igual.",
        ["prueba en orden", "halla 8 en A", "halla 0 a 7 en B", "halla 0 a 6 en C", "indica el 8 en B y el 7 en C como primeros que no sirven"],
        ["lista de números probados", "soluciones", "primer número que no sirve"],
        ["olvidar que menor que no incluye el igual", "buscar un solo número en una desigualdad"],
        "Pide que muestre las cuentas de los números que prueba; reconoce que distingue igualdad de desigualdad.",
    ),
    reinforce="Con 10 fichas, prueba qué números puedes poner en __ + 3 < 8 y comprueba cada uno con fichas.",
    extend="Escribe una desigualdad con hueco que tenga exactamente cuatro soluciones entre 0 y 20.",
)
