"""Student material for 3.º básico Matemática, OA 12 (patrones numéricos en tablas del 100) y OA 13 (ecuaciones aditivas de un paso)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA12, OA13 = "MA03 OA 12", "MA03 OA 13"

TABLE = "Tabla del 100: tiene 10 filas de 10 números, del 1 al 100. La fila 1 va del 1 al 10, la fila 2 del 11 al 20, y así hasta la fila 10, del 91 al 100."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 12
register(
    OA12, 1,
    materials=f"Lápiz, papel y lápices de colores. Si quieres, dibuja tu propia tabla del 100. {TABLE}",
    use="Aprenderé a descubrir la regla de un patrón cuando leo los números de izquierda a derecha. Sirve para seguir un patrón sin equivocarme.",
    prior=["Sé contar de 2 en 2, de 5 en 5 y de 10 en 10.", "Sé sumar números de hasta dos cifras."],
    explain=[
        f"Un patrón numérico es una lista de números que sigue una regla. La regla dice qué hacer para pasar de un número al siguiente. {TABLE} En una fila, leyendo hacia la derecha, cada número es 1 más que el anterior.",
        "Si pintas algunos casilleros siguiendo una regla, aparece un patrón. Por ejemplo, 2, 4, 6, 8, 10: cada número es 2 más que el anterior. La regla es «sumar 2». Si quieres seguir el patrón, aplicas la regla al último número.",
        "Describir los números no basta. Debes decir la regla. «Terminan en 2, 4, 6…» describe los números; «sumar 2 cada vez» es la regla. Para encontrarla, resta dos números seguidos y mira si siempre da lo mismo.",
    ],
    vocab=[("patrón", "lista de números que sigue una regla"), ("regla", "lo que se hace para pasar de un número al siguiente"), ("tabla del 100", "tabla con los números del 1 al 100 en 10 filas"), ("fila", "casilleros en línea de izquierda a derecha"), ("término", "cada número de un patrón")],
    worked=[
        {"title": "Encontrar la regla", "problem": "Un patrón empieza así: 5, 10, 15, 20. ¿Cuál es la regla y cuál es el número siguiente?", "steps": ["Resto números seguidos: 10 − 5 = 5, 15 − 10 = 5, 20 − 15 = 5.", "Siempre da 5: la regla es sumar 5.", "El siguiente es 20 + 5 = 25."], "answer": "La regla es sumar 5; el siguiente es 25"},
        {"title": "Leer una fila de la tabla", "problem": "En la fila del 21 al 30, ¿qué número está justo después del 27?", "steps": ["En una fila, leyendo hacia la derecha, se suma 1.", "27 + 1 = 28."], "answer": "28"},
    ],
    mistakes=[
        {"wrong": "Describir 7, 12, 17, 22 como «números que terminan en 2 y en 7».", "why": "Se describen los números, pero no se dice la regla.", "fix": "Resta números seguidos: 12 − 7 = 5. La regla es sumar 5."},
        {"wrong": "Continuar 3, 6, 9 con 11.", "why": "No se aplica la misma regla.", "fix": "La regla es sumar 3, así que el siguiente es 9 + 3 = 12."},
    ],
    tiers={
        "recovery": [
            ex("Completa el patrón: 2, 4, 6, 8, __", "10", "Cada número es 2 más que el anterior."),
            ex("En el patrón 5, 10, 15, 20, ¿cuál es la regla?", "Sumar 5", "Cada número es 5 más que el anterior."),
            ex("En la fila del 61 al 70 de la tabla del 100, ¿qué número está justo después del 64?", "65", "Leyendo hacia la derecha se suma 1."),
        ],
        "understand": [
            ex("En un patrón numérico, ¿qué dice la regla?", "Lo que se hace para pasar de un número al siguiente", "La regla se aplica una y otra vez."),
            ex("En la fila del 41 al 50, al moverte un casillero a la derecha, ¿cuánto cambia el número?", "Aumenta 1", "Cada casillero es 1 más que el anterior."),
            ex("El patrón 10, 20, 30, 40 ¿sube o baja, y cuánto cada vez?", "Sube 10 cada vez", "Cada número es 10 más que el anterior."),
        ],
        "apply": [
            ex("Escribe los cinco primeros números de un patrón que empieza en 3 y cuya regla es sumar 3.", "3, 6, 9, 12, 15", "Se suma 3 al último número cada vez."),
            ex("Completa el patrón: 15, 20, 25, __, 35", "30", "La regla es sumar 5."),
            ex("Pintas de 4 en 4 desde el 4 en la tabla del 100: 4, 8, 12, __, 20. ¿Qué número falta?", "16", "La regla es sumar 4."),
        ],
        "reason": [
            ex("Lucía mira 4, 9, 14, 19 y dice «son números que terminan en 4 o en 9». ¿Dijo la regla? ¿Cuál es?", "No; la regla es sumar 5", "Los números se describen, pero la regla es 9 − 4 = 5."),
            ex("Un patrón empieza en 6 y sube de 3 en 3: 6, 9, 12, 15. Tomás dice que el siguiente es 17. ¿Es correcto?", "No; el siguiente es 18", "15 + 3 = 18."),
        ],
        "challenge": [
            ex("Un patrón es 100, 90, 80. Escribe su regla y los tres números siguientes.", "Restar 10; 70, 60, 50", "Cada número es 10 menos que el anterior."),
            arith("Pintas de 5 en 5 desde el 5 en la tabla del 100. ¿Cuál es el décimo número pintado?", "10*5", "El décimo número es 10 veces 5."),
        ],
    },
    context=[ex("Una escalera tiene escalones numerados 10, 20, 30, 40. Si sigue la misma regla, ¿qué número lleva el siguiente escalón?", "50", "La regla es sumar 10.")],
    selfcheck=[
        ex("Completa el patrón: 12, 14, 16, __, 20", "18", "La regla es sumar 2."),
        ex("¿Cuál es la regla del patrón 90, 80, 70?", "Restar 10", "Cada número es 10 menos que el anterior."),
        ex("En una fila de la tabla del 100, ¿qué número está justo antes del 38?", "37", "A la izquierda hay 1 menos."),
    ],
    open_task=task(
        "Elige una regla: sumar 2, sumar 5 o sumar 10. En una tabla del 100 dibujada por ti, pinta los diez primeros números que siguen esa regla, desde el 2, desde el 5 o desde el 10. Escribe la lista de números pintados y la regla con tus palabras.",
        "Regla sumar 5. Pinto 5, 10, 15, 20, 25, 30, 35, 40, 45, 50. La regla es: a cada número le sumo 5 para tener el siguiente.",
        ["pinta los números correctos", "escribe la lista en orden", "dice la regla y no solo describe los números"],
        ["tabla pintada", "lista de números", "regla escrita"],
        ["describir sin dar la regla", "saltarse un término"],
        "Pide que reste dos números seguidos para comprobar la regla. Reconoce que la formule con sus palabras.",
    ),
    reinforce="Cuenta de 3 en 3 desde el 3 y escribe los diez primeros números. Di la regla.",
    extend="En la tabla del 100, pinta de 2 en 2 desde el 2 y de 5 en 5 desde el 5. Escribe un número que se pintó en ambas listas y explica cómo lo notaste.",
)

register(
    OA12, 2,
    materials=f"Lápiz y papel. {TABLE}",
    use="Aprenderé qué cambia cuando bajo o subo en la tabla del 100. Sirve para encontrar números sin contar uno por uno.",
    prior=["Sé que en una fila se suma 1 hacia la derecha.", "Sé sumar y restar 10 a un número."],
    explain=[
        f"En la tabla del 100, cada fila tiene 10 números. Por eso, al bajar un casillero, el número aumenta 10. Si estás en el 5 y bajas, llegas al 15. Si bajas otra vez, llegas al 25. {TABLE}",
        "Al subir un casillero, el número baja 10. Desde el 63 subes y llegas al 53. Observa los números de una columna: 8, 18, 28, 38. Siempre terminan en 8, porque no cambian las unidades. Solo cambia la cifra de las decenas: sube 1.",
        "Con eso puedes moverte rápido. Para bajar tres casilleros desde el 9, sumas 10 tres veces: 9 + 30 = 39. Para subir dos casilleros desde el 82, restas 20: 82 − 20 = 62.",
    ],
    vocab=[("columna", "casilleros en línea de arriba hacia abajo"), ("bajar", "pasar al casillero de la fila siguiente, justo debajo"), ("subir", "pasar al casillero de la fila anterior, justo arriba"), ("decena", "grupo de 10"), ("unidades", "cifra de la derecha de un número")],
    worked=[
        {"title": "Bajar casilleros", "problem": "Estás en el 37 de la tabla del 100 y bajas un casillero. ¿A qué número llegas?", "steps": ["Al bajar, el número aumenta 10.", "37 + 10 = 47."], "answer": "47"},
        {"title": "Subir varios casilleros", "problem": "Estás en el 82 y subes 2 casilleros. ¿A qué número llegas?", "steps": ["Cada casillero que subo resta 10.", "Dos casilleros restan 20.", "82 − 20 = 62."], "answer": "62"},
    ],
    mistakes=[
        {"wrong": "Bajar desde el 25 y decir que llegas al 26.", "why": "Se confunde bajar con moverse a la derecha.", "fix": "Al bajar se suma 10: 25 + 10 = 35."},
        {"wrong": "Decir que 4, 14, 24, 34 no están en la misma columna porque son números distintos.", "why": "Se mira el número completo y no que las unidades no cambian.", "fix": "Todos terminan en 4 y cada uno es 10 más: están en la misma columna."},
    ],
    tiers={
        "recovery": [
            arith("Estás en el 5 de la tabla del 100 y bajas un casillero. ¿A qué número llegas?", "5+10", "Al bajar se suma 10."),
            arith("Estás en el 48 y bajas un casillero. ¿A qué número llegas?", "48+10", "Al bajar se suma 10."),
            arith("Estás en el 74 y subes un casillero. ¿A qué número llegas?", "74-10", "Al subir se resta 10."),
        ],
        "understand": [
            ex("Al bajar un casillero en la tabla del 100, ¿el número sube o baja y cuánto?", "Sube 10", "Cada fila tiene 10 números."),
            ex("Mira la columna 8, 18, 28, 38. ¿Qué cifra no cambia y cuál sube 1 cada vez?", "No cambian las unidades (8); sube la cifra de las decenas", "Al sumar 10 solo cambia la decena."),
            ex("¿Por qué al bajar un casillero se suma 10 y no otro número?", "Porque cada fila tiene 10 números", "Para llegar al casillero de abajo se pasan los 10 números de la fila."),
        ],
        "apply": [
            ex("Completa la columna: 6, 16, 26, __, 46", "36", "Cada casillero que baja suma 10."),
            arith("Estás en el 2 y bajas 3 casilleros. ¿A qué número llegas?", "2+30", "Tres casilleros suman 3 × 10 = 30."),
            arith("Estás en el 76 y subes 2 casilleros. ¿A qué número llegas?", "76-20", "Dos casilleros restan 20."),
        ],
        "reason": [
            ex("Nico estaba en el 31, bajó un casillero y dijo que llegó al 32. ¿Cuál es su error y a qué número debió llegar?", "Se movió a la derecha; debió llegar al 41", "Bajar suma 10: 31 + 10 = 41."),
            ex("Pía dice que 5, 15, 25 y 35 no pueden estar en la misma columna porque son números distintos. ¿Qué le respondes?", "Están en la misma columna: terminan en 5 y cada uno es 10 más", "En una columna cambian las decenas y no las unidades."),
        ],
        "challenge": [
            ex("Desde el 14 de la tabla del 100 bajas un casillero y luego te mueves un casillero a la derecha. ¿A qué número llegas?", "25", "14 + 10 = 24 y 24 + 1 = 25.", calc="14+10+1"),
            ex("Estás en el 7 y bajas 4 casilleros. ¿A qué número llegas y en qué fila de la tabla (1 a 10) está?", "Al 47, en la fila 5", "7 + 40 = 47 y 47 está entre 41 y 50, que es la fila 5.", calc="7+40"),
        ],
    },
    context=[arith("Un estacionamiento tiene puestos numerados del 1 al 100, con 10 puestos por fila. El auto de Ana está en el puesto 23. El auto de Beto está en la misma posición, dos filas más abajo. ¿Qué número de puesto tiene?", "23+20", "Dos filas más abajo suman 20.")],
    selfcheck=[
        arith("Estás en el 51 y bajas un casillero. ¿A qué número llegas?", "51+10", "Al bajar se suma 10."),
        arith("Estás en el 90 y subes un casillero. ¿A qué número llegas?", "90-10", "Al subir se resta 10."),
        ex("¿Cuánto cambia un número cuando te mueves un casillero hacia abajo en la tabla del 100?", "Aumenta 10", "Es la cantidad de números de una fila."),
    ],
    open_task=task(
        "Dibuja las columnas de la tabla del 100 que empiezan en 3, 6 y 9 (anota los diez números de cada una, de arriba hacia abajo). Escribe qué nota en cada columna y qué cifra se repite.",
        "Columna del 3: 3, 13, 23, 33, 43, 53, 63, 73, 83, 93. Siempre termina en 3 y cada número es 10 más. Lo mismo pasa con la del 6 y la del 9.",
        ["escribe diez números por columna", "suma 10 cada vez", "dice qué cifra se repite y por qué"],
        ["tres columnas escritas", "explicación"],
        ["sumar 1 en vez de 10", "saltarse una fila"],
        "Pide que cuente cuántos números hay en una fila. Reconoce que relacione eso con el 10.",
    ),
    reinforce="Elige un número entre 1 y 10 y escribe su columna completa en la tabla del 100.",
    extend="Estás en el 32 de la tabla del 100. Escribe a qué número llegas si bajas un casillero y te mueves uno a la derecha, y a cuál llegas si bajas uno y te mueves uno a la izquierda. ¿Qué regla notas en cada caso?",
)

register(
    OA12, 3,
    materials="Lápiz y papel. Los patrones están escritos en cada ejercicio.",
    use="Aprenderé a escribir la regla de un patrón con símbolos y a registrar sus números. Sirve para anotar un patrón de manera corta y clara.",
    prior=["Sé encontrar la regla de un patrón restando números seguidos.", "Sé sumar y restar con números de hasta dos cifras."],
    explain=[
        "Una regla puede escribirse con símbolos. Para «sumar 5» escribimos +5. Para «restar 10» escribimos −10. Así la regla queda corta y clara.",
        "Para registrar un patrón escribimos dos datos: el número donde empieza y la regla. Por ejemplo, «Empieza en 3, regla +5» da 3, 8, 13, 18. También podemos usar flechas: 3 → 8 → 13 → 18, con +5 sobre cada flecha.",
        "Para encontrar la regla de una lista, resta cada número con el anterior. Si el resultado siempre es el mismo, esa es la regla. En 5, 12, 19, 26 las diferencias son 7, 7 y 7, así que la regla es +7. Si los números bajan, resta el mayor menos el menor, y la regla es una resta: en 50, 45, 40 baja 5 cada vez, así que la regla es −5.",
    ],
    vocab=[("símbolo", "marca o signo que representa una idea"), ("+5", "regla que significa sumar 5"), ("−10", "regla que significa restar 10"), ("registrar", "anotar para no olvidar"), ("flecha", "símbolo que muestra el paso de un número al siguiente")],
    worked=[
        {"title": "Registrar un patrón", "problem": "Escribe los cuatro primeros números de un patrón que empieza en 4 y tiene la regla +6.", "steps": ["Escribo el primer número: 4.", "Sumo 6: 4 + 6 = 10.", "Sumo 6: 10 + 6 = 16.", "Sumo 6: 16 + 6 = 22."], "answer": "4, 10, 16, 22"},
        {"title": "Encontrar la regla con símbolos", "problem": "¿Cuál es la regla del patrón 5, 12, 19, 26?", "steps": ["Resto números seguidos: 12 − 5 = 7, 19 − 12 = 7, 26 − 19 = 7.", "Siempre da 7.", "Los números suben, así que la regla es +7."], "answer": "+7"},
    ],
    mistakes=[
        {"wrong": "Escribir la regla +3 para el patrón 3, 8, 13, 18.", "why": "Se usa el primer número como regla.", "fix": "Resta números seguidos: 8 − 3 = 5. La regla es +5."},
        {"wrong": "Escribir +5 para el patrón 50, 45, 40.", "why": "Se olvida que los números bajan.", "fix": "Si los números bajan, la regla es una resta: −5."},
    ],
    tiers={
        "recovery": [
            ex("Escribe con símbolos la regla «sumar 4».", "+4", "El signo + y el número 4 muestran la regla."),
            ex("¿Qué regla con símbolos describe el patrón 50, 40, 30, 20?", "−10", "Cada número es 10 menos que el anterior."),
            ex("El patrón 2 → 7 → 12 tiene la regla +5. ¿Cuál es el número siguiente?", "17", "12 + 5 = 17."),
        ],
        "understand": [
            ex("En «Empieza en 10; regla +3: 10, 13, 16», ¿qué dice el +3?", "Que cada número es 3 más que el anterior", "+3 es sumar 3."),
            ex("Para registrar un patrón, ¿qué dos datos hay que escribir?", "El número donde empieza y la regla", "Con esos datos se puede escribir todo el patrón."),
            ex("En una regla, ¿qué significa −2?", "Restar 2 cada vez", "El signo − indica que se quita."),
        ],
        "apply": [
            ex("Escribe los cuatro primeros números de un patrón que empieza en 3 y tiene la regla +4.", "3, 7, 11, 15", "Se suma 4 cada vez."),
            ex("Escribe la regla del patrón 9, 15, 21, 27 con símbolos.", "+6", "Cada número es 6 más que el anterior."),
            ex("Un patrón empieza en 60 y tiene la regla −5. Escribe los tres números que siguen al 60.", "55, 50, 45", "Se resta 5 cada vez."),
        ],
        "reason": [
            ex("Dana escribió que el patrón 2, 9, 16, 23 tiene la regla +2. ¿Hay un error?", "Sí; la regla es +7", "9 − 2 = 7, 16 − 9 = 7 y 23 − 16 = 7."),
            ex("Dos patrones empiezan en 2. El A tiene la regla +2 y el B tiene la regla +3. ¿Cuál es mayor después de tres pasos?", "El B, con 11 contra 8", "B: 2, 5, 8, 11; A: 2, 4, 6, 8."),
        ],
        "challenge": [
            arith("Un patrón empieza en 1 y tiene la regla +10. ¿Cuál es su sexto número?", "1+5*10", "Del primer al sexto número se suma 10 cinco veces."),
            ex("Un patrón empieza en 50 y llega a 25 con 50, 45, 40, 35, 30, 25. Escribe su regla y cuántos números tiene.", "−5; 6 números", "Cada número es 5 menos y la lista tiene 6 números."),
        ],
    },
    context=[ex("Una niña sube una escalera de 3 en 3, pisando los escalones 3, 6 y 9. Escribe con símbolos la regla de su subida.", "+3", "Cada escalón que pisa es 3 más que el anterior.")],
    selfcheck=[
        ex("Escribe la regla de 8, 16, 24, 32 con símbolos.", "+8", "Cada número es 8 más que el anterior."),
        ex("Un patrón empieza en 20 y tiene la regla −2. Escribe los tres números que siguen al 20.", "18, 16, 14", "Se resta 2 cada vez."),
        ex("En la tabla del 100 pintas los números 9, 18, 27, 36. Escribe la regla con símbolos.", "+9", "Cada número pintado es 9 más que el anterior."),
    ],
    open_task=task(
        "Elige uno de estos patrones: A) 7, 14, 21, 28; B) 96, 91, 86, 81. Escribe la regla con símbolos, las diferencias que encontraste, los dos números siguientes y dibuja el patrón con flechas.",
        "Patrón B: 96 − 91 = 5, 91 − 86 = 5, 86 − 81 = 5. Los números bajan 5 cada vez, así que la regla es −5. Siguientes: 76 y 71. Con flechas: 96 → 91 → 86 → 81 → 76 → 71, con −5 sobre cada flecha.",
        ["calcula las diferencias", "escribe la regla con símbolo", "continúa el patrón", "dibuja las flechas"],
        ["diferencias escritas", "regla", "dos números siguientes", "flechas"],
        ["usar el primer número como regla", "confundir + con −"],
        "Pide que verifique con cada par de números seguidos. Reconoce el signo correcto en la regla.",
    ),
    reinforce="Escribe tres patrones con las reglas +2, +10 y −5, cada uno con cuatro números.",
    extend="Inventa un patrón de cinco números con una regla de suma y escribe la regla con símbolos. Pide a alguien que la descubra.",
)

register(
    OA12, 4,
    materials="Lápiz y papel. Los patrones están escritos en cada ejercicio.",
    use="Aprenderé a crear un patrón con una regla y a comprobar que de verdad la cumple. Sirve para estar seguro de que un patrón está bien hecho.",
    prior=["Sé escribir una regla con símbolos.", "Sé encontrar la regla restando números seguidos."],
    explain=[
        "Para crear un patrón, elige dónde empieza y una regla. Por ejemplo, empieza en 7 y la regla es +10. Entonces el patrón es 7, 17, 27, 37. Cada número se obtiene aplicando la regla al anterior.",
        "Para verificar un patrón, comprueba cada par de números seguidos. La diferencia debe ser siempre la misma que la regla. Si un par no la cumple, ese número está mal. Por ejemplo, en 10, 20, 30, 45, 50 con la regla +10, el 45 está mal; debería ser 40.",
        "Un patrón creado se explica con tres cosas: el número inicial, la regla y la lista de números. Así otra persona puede copiarlo o continuarlo sin equivocarse.",
    ],
    vocab=[("crear", "inventar algo nuevo"), ("verificar", "comprobar que algo está bien"), ("número inicial", "el número donde empieza el patrón"), ("diferencia", "resultado de restar dos números seguidos"), ("cumplir la regla", "seguir exactamente lo que dice la regla")],
    worked=[
        {"title": "Crear y escribir un patrón", "problem": "Crea un patrón de cuatro números que empiece en 5 con regla +5.", "steps": ["El primer número es 5.", "5 + 5 = 10.", "10 + 5 = 15.", "15 + 5 = 20."], "answer": "5, 10, 15, 20"},
        {"title": "Verificar un patrón", "problem": "¿La lista 8, 15, 22, 29 cumple la regla +7?", "steps": ["Calculo cada diferencia: 15 − 8 = 7, 22 − 15 = 7, 29 − 22 = 7.", "Todas dan 7.", "La lista cumple la regla +7."], "answer": "Sí, cumple la regla +7"},
    ],
    mistakes=[
        {"wrong": "Decir que 5, 10, 16, 20 cumple la regla +5 porque casi todos suben 5.", "why": "Se acepta un patrón sin revisar cada par.", "fix": "10 → 16 sube 6, no 5. Un solo par que falle ya rompe el patrón."},
        {"wrong": "Crear un patrón sin decir el número inicial ni la regla.", "why": "Otra persona no puede continuarlo.", "fix": "Anota siempre el inicio, la regla y los números."},
    ],
    tiers={
        "recovery": [
            ex("Un patrón empieza en 2 y tiene la regla +2. Escribe los cuatro primeros números.", "2, 4, 6, 8", "Se suma 2 cada vez."),
            ex("¿La lista 4, 9, 14, 20 cumple la regla +5?", "No; de 14 a 20 sube 6", "Una diferencia distinta rompe la regla."),
            ex("¿La lista 3, 6, 9, 12 cumple la regla +3?", "Sí", "Todas las diferencias son 3."),
        ],
        "understand": [
            ex("Para verificar un patrón, ¿qué revisas en cada par de números seguidos?", "Que la diferencia sea igual a la regla", "Todos los pares deben cumplir la misma regla."),
            ex("¿Por qué conviene anotar el número inicial y la regla de un patrón?", "Para que otra persona pueda copiarlo o continuarlo", "Con esos datos se reconstruye todo el patrón."),
            ex("Un patrón empieza en 7 y tiene la regla +10. ¿Cuál es el segundo número?", "17", "7 + 10 = 17."),
        ],
        "apply": [
            ex("Crea un patrón de cinco números que empiece en 8 y tenga la regla +2.", "8, 10, 12, 14, 16", "Se suma 2 cada vez."),
            ex("¿La lista 9, 13, 17, 21 cumple la regla +4?", "Sí", "13 − 9 = 4, 17 − 13 = 4 y 21 − 17 = 4."),
            ex("Completa el patrón de regla +4: 6, 10, __, 18", "14", "10 + 4 = 14 y 14 + 4 = 18."),
        ],
        "reason": [
            ex("Beto creó 12, 22, 32, 44, 52 con la regla +10. ¿Qué número rompe la regla y cuál debería ser?", "El 44; debería ser 42", "32 + 10 = 42."),
            ex("Rita dice que 6, 8, 11, 13 es un patrón de sumar 2. ¿Es verdad?", "No; los saltos son 2, 3 y 2", "Una regla de sumar 2 exige saltos siempre de 2."),
        ],
        "challenge": [
            ex("Crea un patrón de cinco números que tenga la regla +10 y cuyo cuarto número sea 40.", "10, 20, 30, 40, 50", "Si el cuarto es 40, el primero es 40 − 30 = 10."),
            ex("Un patrón de cinco números tiene la regla −3 y termina en 4. ¿En qué número empieza?", "16", "16, 13, 10, 7, 4 baja de 3 en 3."),
        ],
    },
    context=[ex("Tomás ahorra $50 la primera semana y cada semana agrega $50 más a lo que ya tenía. Los totales son $50, $100, $150… ¿Cuánto tendrá la semana 4?", "$200", "La regla es +50 y el cuarto número es 200.")],
    selfcheck=[
        ex("¿La lista 12, 18, 24, 30 cumple la regla +6?", "Sí", "Todas las diferencias son 6."),
        ex("Un patrón empieza en 9 y tiene la regla +9. Escribe el segundo y el tercer número.", "18 y 27", "9 + 9 = 18 y 18 + 9 = 27."),
        ex("Con la regla +4, ¿qué número rompe la lista 4, 8, 12, 15, 20?", "El 15", "12 + 4 = 16, no 15."),
    ],
    open_task=task(
        "Crea tu propio patrón de seis números. Elige un número inicial entre 1 y 20 y una regla de las siguientes: +2, +3, +5 o +10. Escribe el inicio, la regla con símbolos y la lista. Luego verifica cada par de números seguidos y anota las diferencias.",
        "Inicio 4, regla +3. Lista: 4, 7, 10, 13, 16, 19. Diferencias: 3, 3, 3, 3, 3. Cumple la regla.",
        ["escribe inicio y regla", "la lista cumple la regla", "calcula todas las diferencias", "las diferencias coinciden con la regla"],
        ["inicio y regla", "lista de seis números", "diferencias escritas"],
        ["un par que no cumple", "no anotar el inicio"],
        "Pide que lea las diferencias en voz alta. Reconoce que detecte y corrija un error.",
    ),
    reinforce="Crea un patrón de cuatro números con la regla +5 y cámbialo para que empiece en un número distinto. Verifica ambos.",
    extend="Crea un patrón de siete números con la regla −5 que parta en 100. Pinta los números en una tabla del 100 y escribe en qué dos columnas caen.",
)

# ================================================================ OA 13
BAL = "Una balanza de platillos está equilibrada cuando los dos platillos pesan lo mismo."

register(
    OA13, 1,
    materials=f"Lápiz y papel. Si quieres, 20 fichas, botones o semillas. {BAL}",
    use="Aprenderé que el signo = significa «vale lo mismo». Sirve para mantener una igualdad y para resolver ecuaciones.",
    prior=["Sé sumar y restar con números hasta 100.", "Sé qué significa el signo = en una suma."],
    explain=[
        BAL + " El signo = funciona igual: dice que lo de un lado vale lo mismo que lo del otro. En 4 + 3 = 5 + 2, los dos lados valen 7.",
        "El signo = no significa «escribe aquí el resultado». Puede haber operaciones a los dos lados. Para saber si es verdadera, calcula cada lado y compara. Si dan lo mismo, hay igualdad.",
        "Si agregas lo mismo a los dos lados, la igualdad se mantiene. Si agregas solo a un lado, se rompe. Para equilibrar de nuevo, haz lo mismo en el otro lado.",
    ],
    vocab=[("igualdad", "dos cantidades que valen lo mismo"), ("equilibrada", "con los dos lados iguales"), ("signo =", "se lee «es igual a»; los dos lados valen lo mismo"), ("lado", "cada parte de la igualdad, a la izquierda o a la derecha del =")],
    worked=[
        {"title": "Revisar una igualdad", "problem": "¿Es verdadera la igualdad 4 + 3 = 5 + 2?", "steps": ["Calculo el lado izquierdo: 4 + 3 = 7.", "Calculo el lado derecho: 5 + 2 = 7.", "Los dos lados valen 7."], "answer": "Sí, es verdadera"},
        {"title": "Completar una igualdad", "problem": "Completa 8 + 4 = □ + 5.", "steps": ["El lado izquierdo vale 8 + 4 = 12.", "El lado derecho debe valer 12 también.", "□ + 5 = 12, así que □ = 12 − 5 = 7."], "answer": "□ = 7"},
    ],
    mistakes=[
        {"wrong": "En 7 + 3 = □ + 4, escribir 10 porque 7 + 3 da 10.", "why": "Se piensa que el signo = pide el resultado.", "fix": "Los dos lados deben valer lo mismo: 10 = □ + 4, así que □ = 6."},
        {"wrong": "Agregar 3 fichas a un platillo y dejar el otro igual, esperando que siga equilibrada.", "why": "Se cambia un solo lado.", "fix": "Agrega 3 fichas también al otro platillo."},
    ],
    tiers={
        "recovery": [
            ex("Una balanza tiene 6 fichas en un platillo y 6 en el otro. ¿Está equilibrada?", "Sí", "Los dos platillos tienen lo mismo."),
            ex("¿Es verdadera la igualdad 3 + 6 = 5 + 4?", "Sí; los dos lados valen 9", "3 + 6 = 9 y 5 + 4 = 9."),
            ex("¿Es verdadera la igualdad 6 + 1 = 4 + 4?", "No; un lado vale 7 y el otro 8", "6 + 1 = 7 y 4 + 4 = 8."),
        ],
        "understand": [
            ex("¿Qué dice el signo = en una igualdad?", "Que los dos lados valen lo mismo", "Se lee «es igual a»."),
            ex("Una balanza equilibrada tiene 8 fichas a cada lado. Quitas 3 fichas del platillo izquierdo. ¿Hacia qué lado se inclina?", "Hacia el derecho", "El platillo derecho queda con más fichas."),
            ex("En esa balanza que quedó inclinada, ¿qué haces para equilibrarla de nuevo?", "Quitar 3 fichas del platillo derecho", "Se quita lo mismo de los dos lados."),
        ],
        "apply": [
            arith("Halla el número que falta: 9 + 3 = □ + 4", "9+3-4", "El lado izquierdo vale 12 y □ + 4 debe valer 12."),
            arith("Halla el número que falta: 15 = □ + 9", "15-9", "El lado derecho debe valer 15."),
            arith("Una balanza tiene 12 fichas a cada lado. Agregas 10 al platillo izquierdo. ¿Cuántas fichas agregas al derecho para equilibrar?", "10", "Se agrega lo mismo en los dos lados.", " fichas"),
        ],
        "reason": [
            ex("Lía dice que en 6 + 4 = □ + 3 el número que falta es 10, porque 6 + 4 da 10. ¿Qué error comete y cuál es el número correcto?", "Puso el resultado; el correcto es 7", "10 debe ser igual a □ + 3, así que □ = 7."),
            ex("Raúl dice que 9 − 4 = 3 + 2 es falsa porque «el resultado va al final». ¿Es falsa?", "No; es verdadera, los dos lados valen 5", "9 − 4 = 5 y 3 + 2 = 5."),
        ],
        "challenge": [
            arith("Halla el número que falta: 25 + 15 = 20 + □", "25+15-20", "El lado izquierdo vale 40."),
            arith("Halla el número que falta: 36 + 14 = □ + 40", "36+14-40", "El lado izquierdo vale 50."),
        ],
    },
    context=[arith("En una balanza, un platillo tiene 9 fichas rojas y 6 azules. El otro tiene 7 fichas verdes y algunas amarillas. Todas las fichas pesan lo mismo. ¿Cuántas amarillas se necesitan para equilibrarla?", "9+6-7", "Un lado tiene 15 fichas; el otro tiene 7 y le faltan 8.", " fichas")],
    selfcheck=[
        ex("¿Es verdadera la igualdad 10 + 5 = 9 + 6?", "Sí; los dos lados valen 15", "10 + 5 = 15 y 9 + 6 = 15."),
        arith("Halla el número que falta: 6 + □ = 10", "10-6", "Falta lo que lleva 6 a 10."),
        ex("Si agregas 4 fichas a un platillo de una balanza equilibrada, ¿qué haces en el otro platillo para mantenerla equilibrada?", "Agregar 4 fichas", "Hay que agregar lo mismo en los dos lados."),
    ],
    open_task=task(
        "Con 20 fichas o botones, arma una balanza dibujada con dos platillos. Pon 5 fichas en cada platillo. Agrega 3 a la izquierda y mira qué pasa. Luego equilibra la balanza y escribe las igualdades que obtuviste con números.",
        "5 = 5. Agrego 3 a la izquierda y queda 8 contra 5, desequilibrada. Agrego 3 a la derecha y queda 8 = 8, equilibrada.",
        ["usa 5 fichas por platillo", "agrega a un lado y observa el desequilibrio", "equilibra agregando lo mismo al otro lado", "escribe las igualdades"],
        ["dibujo de la balanza", "igualdades escritas"],
        ["agregar a un solo lado", "creer que = pide el resultado"],
        "Pide que diga qué debe valer cada lado. Reconoce que mantenga la igualdad.",
    ),
    reinforce="Escribe tres igualdades verdaderas que tengan una suma a cada lado, por ejemplo 5 + 4 = 6 + 3. Comprueba calculando cada lado.",
    extend="Escribe una igualdad falsa y cámbiale un número para que sea verdadera. Explica qué hiciste.",
)

register(
    OA13, 2,
    materials="Lápiz y papel. Todas las ecuaciones usan números del 0 al 100.",
    use="Aprenderé a hallar el número que falta en una suma. Sirve para resolver problemas donde sabemos el total y una parte.",
    prior=["Sé que el signo = significa «vale lo mismo».", "Sé sumar y restar con números hasta 100."],
    explain=[
        "Una ecuación es una igualdad con un número desconocido. Lo escribimos con un símbolo, como □ o △. En □ + 7 = 15 el cuadrado es el número que no conocemos y debemos descubrir.",
        "Puedes dibujarlo como una balanza: de un lado □ y 7 fichas, del otro 15 fichas. Para hallarlo en una suma, piensa: ¿qué número más 7 da 15? La suma y la resta se deshacen. Entonces restas: 15 − 7 = 8. El desconocido es 8. También funciona 35 + △ = 80: △ = 80 − 35 = 45.",
        "Siempre comprueba. Reemplaza el símbolo por tu respuesta y calcula: 8 + 7 = 15. Si los dos lados valen lo mismo, tu solución es correcta.",
    ],
    vocab=[("ecuación", "igualdad con un número desconocido"), ("incógnita", "número que no se conoce y se busca"), ("símbolo", "dibujo que representa el número desconocido, como □"), ("solución", "número que hace verdadera la ecuación"), ("comprobar", "reemplazar la solución y revisar que los dos lados valgan lo mismo")],
    worked=[
        {"title": "Resolver con resta", "problem": "Resuelve □ + 7 = 15.", "steps": ["Quiero un número que sumado a 7 dé 15.", "Resto: 15 − 7 = 8.", "Compruebo: 8 + 7 = 15."], "answer": "□ = 8"},
        {"title": "Desconocido al segundo lugar", "problem": "Resuelve 35 + △ = 80.", "steps": ["Necesito el número que se suma a 35 para llegar a 80.", "Resto: 80 − 35 = 45.", "Compruebo: 35 + 45 = 80."], "answer": "△ = 45"},
    ],
    mistakes=[
        {"wrong": "Resolver □ + 12 = 40 sumando 12 + 40 = 52.", "why": "Se suma porque la ecuación tiene un +.", "fix": "Para hallar una parte, resta: 40 − 12 = 28."},
        {"wrong": "Escribir □ = 20 en 20 + □ = 45 sin comprobar.", "why": "Se repite un número de la ecuación.", "fix": "Comprueba: 20 + 20 = 40, no 45. Resta 45 − 20 = 25."},
    ],
    tiers={
        "recovery": [
            arith("Halla el número desconocido: □ + 4 = 9", "9-4", "Se resta 4 del total."),
            arith("Halla el número desconocido: 7 + □ = 12", "12-7", "Se resta 7 del total."),
            arith("Una balanza está equilibrada. En un platillo hay △ y 5 fichas; en el otro hay 14 fichas. ¿Cuántas fichas vale △?", "14-5", "Se resta 5 del total.", " fichas"),
        ],
        "understand": [
            ex("En □ + 7 = 15, ¿qué representa el cuadrado?", "El número que no conocemos", "El símbolo ocupa el lugar del número desconocido."),
            ex("Para hallar □ en □ + 7 = 15, ¿qué operación haces con el 15 y el 7?", "Restar 15 − 7", "La resta deshace la suma."),
            ex("¿Cómo compruebas que □ = 8 es solución de □ + 7 = 15?", "Reemplazas el cuadrado: 8 + 7 = 15", "Si ambos lados valen lo mismo, es solución."),
        ],
        "apply": [
            arith("Resuelve la ecuación: □ + 24 = 60", "60-24", "Se resta 24 del total."),
            arith("Resuelve la ecuación: 28 + △ = 70", "70-28", "Se resta 28 del total."),
            arith("Ana tenía algunas figuritas y recibió 18 más. Ahora tiene 50. Escribe la ecuación □ + 18 = 50 y resuélvela. ¿Cuántas tenía?", "50-18", "Se resta lo que recibió del total.", " figuritas"),
        ],
        "reason": [
            ex("Teo resolvió □ + 15 = 60 con 15 + 60 = 75. ¿Qué error comete y cuál es el valor correcto?", "Sumó; debía restar 60 − 15 = 45", "Para hallar una parte, se resta la otra del total.", calc="60-15"),
            ex("Luz dice que □ = 30 en la ecuación 30 + □ = 70. ¿Tiene razón? Comprueba.", "No; 30 + 30 = 60; el valor correcto es 40", "Se necesita 70 − 30 = 40.", calc="70-30"),
        ],
        "challenge": [
            arith("Resuelve la ecuación: □ + 38 = 100", "100-38", "Se resta 38 del total."),
            arith("¿Cuánto hay que sumar a 67 para llegar a 100? Resuelve 67 + △ = 100", "100-67", "Se resta 67 de 100."),
        ],
    },
    context=[arith("En un álbum hay 56 figuritas pegadas y caben 80. Escribe 56 + □ = 80 y resuelve. ¿Cuántas faltan por pegar?", "80-56", "Faltan las que van de 56 a 80.", " figuritas")],
    selfcheck=[
        arith("Resuelve: □ + 9 = 21", "21-9", "Se resta 9 del total."),
        ex("¿△ = 14 es la solución de △ + 6 = 21?", "No; 14 + 6 = 20", "El lado izquierdo vale 20 y no 21."),
        ex("Escribe la ecuación «un número más 8 es 20» usando □.", "□ + 8 = 20", "El número desconocido se suma a 8 y da 20."),
    ],
    open_task=task(
        "Elige una situación y escribe su ecuación con □: A) Tenía algunos lápices, me regalaron 15 y ahora tengo 40; B) Tenía algunas monedas, encontré 23 más y ahora tengo 60. Resuélvela y comprueba reemplazando.",
        "Situación B: □ + 23 = 60. □ = 60 − 23 = 37. Comprobación: 37 + 23 = 60. Tenía 37 monedas.",
        ["escribe la ecuación con □", "resuelve con una resta", "comprueba reemplazando", "responde con una frase"],
        ["ecuación", "resta", "comprobación"],
        ["sumar en vez de restar", "no comprobar"],
        "Pide que diga qué significa el símbolo en la historia. Reconoce la comprobación.",
    ),
    reinforce="Escribe tres ecuaciones con □ cuya solución sea 10, 20 y 30, y usa una suma en cada una.",
    extend="Resuelve 23 + □ = 100 y 77 + △ = 100. ¿Qué notas en las dos soluciones?",
)

register(
    OA13, 3,
    materials="Lápiz y papel. Todas las ecuaciones usan números del 0 al 100.",
    use="Aprenderé a hallar el número que falta en una resta. Sirve para saber cuánto había antes de quitar algo o cuánto se quitó.",
    prior=["Sé resolver ecuaciones de suma con un número desconocido.", "Sé que sumar y restar se deshacen."],
    explain=[
        "En una resta, el número desconocido puede estar en dos lugares. En □ − 6 = 9, el desconocido es lo que había al principio. Antes de quitar 6, había más: es mayor que 9. Para hallarlo, suma: 9 + 6 = 15.",
        "En 20 − □ = 7, el desconocido es lo que se quitó. Si de 20 queda 7, se quitó la diferencia: 20 − 7 = 13. Aquí se resta, porque piensas «cuánto falta para llegar de 7 a 20».",
        "No siempre se hace la misma operación. Mira dónde está el desconocido y piensa en la historia. Después comprueba con el cálculo: 15 − 6 = 9 y 20 − 13 = 7.",
    ],
    vocab=[("restar", "quitar una cantidad a otra"), ("había al principio", "cantidad inicial antes de quitar"), ("se quitó", "cantidad que se retira"), ("quedó", "cantidad que sobra después de quitar"), ("comprobar", "reemplazar la solución y calcular de nuevo")],
    worked=[
        {"title": "Desconocido al comienzo", "problem": "Resuelve □ − 6 = 9.", "steps": ["Había un número, se quitaron 6 y quedaron 9.", "El número inicial es mayor que 9: debo sumar.", "9 + 6 = 15.", "Compruebo: 15 − 6 = 9."], "answer": "□ = 15"},
        {"title": "Desconocido en lo que se quita", "problem": "Resuelve 20 − △ = 7.", "steps": ["De 20 se quitó algo y quedaron 7.", "Se quitó la diferencia: 20 − 7 = 13.", "Compruebo: 20 − 13 = 7."], "answer": "△ = 13"},
    ],
    mistakes=[
        {"wrong": "Resolver □ − 15 = 20 con 20 − 15 = 5.", "why": "Se resta porque hay un signo −.", "fix": "El número inicial es mayor que 20. Suma: 20 + 15 = 35."},
        {"wrong": "Responder 80 para 50 − △ = 30.", "why": "Se suma sin pensar en la historia.", "fix": "Si de 50 queda 30, se quitaron 50 − 30 = 20."},
    ],
    tiers={
        "recovery": [
            arith("Halla el número desconocido: □ − 3 = 5", "5+3", "Se suma lo que se quitó."),
            arith("Halla el número desconocido: 10 − □ = 4", "10-4", "Se resta lo que quedó."),
            arith("Halla el número desconocido: △ − 2 = 7", "7+2", "Se suma lo que se quitó."),
        ],
        "understand": [
            ex("En □ − 6 = 9, ¿el número desconocido es mayor o menor que 9?", "Mayor", "Es la cantidad antes de quitar 6."),
            ex("Para hallar □ en □ − 6 = 9, ¿qué haces con 9 y 6: sumar o restar?", "Sumar", "Se vuelve al número inicial agregando lo quitado."),
            ex("Para hallar □ en 20 − □ = 7, ¿qué calculas: 20 − 7 o 20 + 7?", "20 − 7", "Se busca la diferencia entre 20 y lo que quedó."),
        ],
        "apply": [
            arith("Resuelve la ecuación: □ − 14 = 30", "30+14", "Se suma lo quitado."),
            arith("Resuelve la ecuación: 70 − △ = 25", "70-25", "Se resta lo que quedó."),
            arith("Mario tenía algunas bolitas, regaló 12 y le quedaron 28. Escribe □ − 12 = 28 y resuelve. ¿Cuántas tenía?", "28+12", "Se suma lo que regaló a lo que quedó.", " bolitas"),
        ],
        "reason": [
            ex("Pili resolvió □ − 18 = 30 con 30 − 18 = 12. ¿Qué error comete y cuál es el valor correcto?", "Restó; debía sumar 30 + 18 = 48", "El número inicial es mayor que 30.", calc="30+18"),
            ex("Dante dice que en 60 − △ = 40 el desconocido es 100. ¿Es posible? ¿Cuál es el correcto?", "No; es 20, porque 60 − 20 = 40", "Con 100 no se puede quitar de 60.", calc="60-40"),
        ],
        "challenge": [
            arith("Resuelve la ecuación: □ − 36 = 36", "36+36", "Se suma lo quitado."),
            arith("Un estanque tenía 100 peces. Se vendieron algunos y quedaron 64. Escribe 100 − □ = 64 y resuelve. ¿Cuántos se vendieron?", "100-64", "Se resta lo que quedó de lo que había.", " peces"),
        ],
    },
    context=[arith("En una caja había lápices. Se usaron 25 y quedan 45. Escribe □ − 25 = 45 y resuelve. ¿Cuántos lápices había al principio?", "45+25", "Se suma lo usado a lo que quedó.", " lápices")],
    selfcheck=[
        arith("Resuelve: □ − 8 = 12", "12+8", "Se suma lo quitado."),
        arith("Resuelve: 40 − △ = 15", "40-15", "Se resta lo que quedó."),
        ex("¿□ = 13 es la solución de □ − 6 = 9?", "No; 13 − 6 = 7", "El lado izquierdo vale 7 y no 9."),
    ],
    open_task=task(
        "Elige una situación y escribe su ecuación con □: A) Tenía algunas galletas, comí 14 y quedan 26; B) Había 90 cuentas, usé algunas y quedan 55. Resuélvela, comprueba y explica si sumaste o restaste.",
        "Situación B: 90 − □ = 55. □ = 90 − 55 = 35. Comprobación: 90 − 35 = 55. Resté porque busco la parte que se usó.",
        ["escribe la ecuación con □", "elige suma o resta según la historia", "comprueba reemplazando", "explica su decisión"],
        ["ecuación", "cálculo", "comprobación", "explicación"],
        ["restar siempre porque hay signo −", "no comprobar"],
        "Pide que cuente la historia con sus palabras antes de calcular. Reconoce la explicación.",
    ),
    reinforce="Resuelve □ − 10 = 40, 60 − □ = 25 y □ − 7 = 8. Para cada una, di si sumaste o restaste y por qué.",
    extend="Escribe dos ecuaciones de resta con la misma solución 30: una con el desconocido al principio y otra en lo que se quita.",
)

register(
    OA13, 4,
    materials="Lápiz y papel. Todas las ecuaciones usan números del 0 al 100.",
    use="Aprenderé a crear una ecuación a partir de una historia y a comprobar su solución. Sirve para resolver problemas con un número desconocido.",
    prior=["Sé resolver ecuaciones de suma y de resta con un símbolo.", "Sé comprobar reemplazando."],
    explain=[
        "Para crear una ecuación, lee la historia y busca el número que no conoces. Ponle un símbolo, como □. Luego escribe lo que pasa: si se agrega, usa +; si se quita, usa −; y termina con el resultado que sí conoces.",
        "Por ejemplo: «Tenía algunos lápices, me regalaron 14 y ahora tengo 40». Se escribe □ + 14 = 40. Se resuelve con 40 − 14 = 26. Comprueba: 26 + 14 = 40. La respuesta en palabras es: tenía 26 lápices.",
        "Comprobar es parte de resolver. Reemplaza el símbolo por la solución y calcula cada lado. Si dan lo mismo, la solución es correcta. Si no, revisa la operación.",
    ],
    vocab=[("crear una ecuación", "escribir con símbolos lo que cuenta una historia"), ("desconocido", "número que no se conoce"), ("solución", "número que hace verdadera la ecuación"), ("comprobación", "revisión que reemplaza la solución en la ecuación"), ("respuesta en palabras", "frase que responde la pregunta de la historia")],
    worked=[
        {"title": "De la historia a la ecuación", "problem": "Tenía algunos lápices, me regalaron 14 y ahora tengo 40. ¿Cuántos tenía?", "steps": ["Llamo □ a los lápices que tenía.", "Me regalaron 14, así que se suma: □ + 14 = 40.", "Resto: 40 − 14 = 26.", "Compruebo: 26 + 14 = 40."], "answer": "Tenía 26 lápices"},
        {"title": "Una ecuación de resta", "problem": "En un bus iban 38 personas y se bajaron algunas. Quedaron 21. ¿Cuántas se bajaron?", "steps": ["Llamo △ a las personas que se bajaron.", "Se quitan, así que escribo 38 − △ = 21.", "△ = 38 − 21 = 17.", "Compruebo: 38 − 17 = 21."], "answer": "Se bajaron 17 personas"},
    ],
    mistakes=[
        {"wrong": "Escribir □ = 26 para □ + 6 = 20 sin comprobar.", "why": "Se suma 6 + 20 en vez de restar.", "fix": "Comprueba: 26 + 6 = 32, no 20. Resta 20 − 6 = 14."},
        {"wrong": "Responder «26» y no decir qué significa.", "why": "Falta la respuesta en palabras.", "fix": "Escribe «tenía 26 lápices»."},
    ],
    tiers={
        "recovery": [
            ex("Escribe una ecuación con □ para: «un número más 5 es 12».", "□ + 5 = 12", "El número desconocido se suma a 5 y da 12."),
            ex("Comprueba si □ = 7 es la solución de □ + 5 = 12.", "Sí; 7 + 5 = 12", "Al reemplazar, los dos lados valen 12."),
            ex("¿Cuál ecuación tiene la solución 4: □ + 3 = 7 o □ + 3 = 8?", "□ + 3 = 7", "4 + 3 = 7."),
        ],
        "understand": [
            ex("¿Para qué sirve comprobar la solución de una ecuación?", "Para asegurarte de que los dos lados valen lo mismo", "Si no valen lo mismo, hay un error."),
            ex("Una ecuación tiene un □ y dos números conocidos. ¿Cuántos números debes encontrar?", "Uno", "Solo el símbolo representa un número que no se conoce."),
            ex("¿La ecuación □ − 4 = 6 es de suma o de resta?", "De resta", "Aparece el signo − entre el desconocido y el 4."),
        ],
        "apply": [
            arith("Resuelve la ecuación □ + 5 = 15 y comprueba reemplazando el cuadrado por tu respuesta.", "15-5", "Se resta 5 del total."),
            ex("Escribe la ecuación con △ para: «a un número le quito 8 y queda 12».", "△ − 8 = 12", "El número se resta con 8 y queda 12."),
            arith("Resuelve la ecuación y comprueba: 45 + □ = 90", "90-45", "Se resta 45 del total."),
        ],
        "reason": [
            ex("Quique escribió □ + 9 = 30 y resolvió □ = 39. ¿Cómo lo revisas y cuál es el valor correcto?", "39 + 9 = 48, que no es 30; el correcto es 21", "Se resta 30 − 9 = 21.", calc="30-9"),
            ex("Mira □ + 5 = 12 (A) y □ + 7 = 12 (B). ¿Cuál tiene la solución mayor?", "A, con 7 contra 5", "Se resta 12 − 5 = 7 y 12 − 7 = 5."),
        ],
        "challenge": [
            arith("Lola tenía □ lápices, le regalaron 17 y ahora tiene 52. Escribe la ecuación y resuélvela. ¿Cuántos tenía?", "52-17", "Se resta lo regalado del total.", " lápices"),
            arith("Escribe y resuelve la ecuación 80 − △ = 55. ¿Cuánto se quitó a 80?", "80-55", "Se resta lo que quedó de lo que había."),
        ],
    },
    context=[arith("En un estacionamiento había 46 autos y se fueron algunos. Quedaron 29. Escribe 46 − □ = 29 y resuelve. ¿Cuántos autos se fueron?", "46-29", "Se resta lo que quedó de lo que había.", " autos")],
    selfcheck=[
        arith("Resuelve: □ + 20 = 50", "50-20", "Se resta 20 del total."),
        ex("Escribe la ecuación para «un número menos 5 es 10» usando □.", "□ − 5 = 10", "El número desconocido se resta con 5 y da 10."),
        arith("Resuelve la ecuación □ − 5 = 10.", "10+5", "Se suma lo que se quitó."),
    ],
    open_task=task(
        "Elige una historia y resuélvela con una ecuación: A) Había algunos caramelos en una bolsa, saqué 18 y quedan 32; B) Tenía $40 y me regalaron algo de dinero, ahora tengo $90. Escribe la ecuación con □, resuélvela, comprueba y responde con una frase.",
        "Historia B: 40 + □ = 90. □ = 90 − 40 = 50. Comprobación: 40 + 50 = 90. Me regalaron $50.",
        ["escribe la ecuación con □", "elige la operación correcta", "comprueba la solución", "responde en palabras"],
        ["ecuación", "cálculo", "comprobación", "frase de respuesta"],
        ["elegir mal la operación", "olvidar la respuesta en palabras"],
        "Pide que cuente la historia sin mirar los números. Reconoce la respuesta completa en palabras.",
    ),
    reinforce="Inventa una historia de suma y otra de resta con un número desconocido, escribe sus ecuaciones y resuélvelas.",
    extend="Escribe una ecuación con □ cuya solución sea 35 y que tenga una resta. Comprueba reemplazando.",
)
