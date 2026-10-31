"""Student material for 5.º básico Matemática, OA 25 (comparar probabilidades de eventos sin calcularlas)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA25 = "MA05 OA 25"

BOLSA_V = "Una bolsa tiene 10 fichas: 6 verdes, 3 amarillas y 1 roja. Se saca una ficha sin mirar."
DADO = "Un dado normal tiene 6 caras con los números 1, 2, 3, 4, 5 y 6."
RUL12 = "Ruleta de 12 sectores iguales: 6 rojos, 4 azules y 2 verdes."
COMP = "Palabras para comparar: un evento es más probable si puede ocurrir en más resultados; menos probable si puede ocurrir en menos; igualmente probables si puede ocurrir en la misma cantidad."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA25, 1,
    materials="Lápiz y papel. Las bolsas, dados y ruletas están descritos con palabras y números dentro de cada ejercicio.",
    use="Aprenderé a decir qué evento es más probable, menos probable o igualmente probable, sin hacer cálculos de probabilidad. Sirve para decidir con razones qué conviene elegir en un juego de azar.",
    prior=["Sé las palabras seguro, posible, poco posible e imposible.", "Sé contar los resultados que cumplen un evento."],
    explain=[
        "Comparar dos eventos significa decir cuál tiene más posibilidades de ocurrir. No hay que calcular ningún número especial: basta contar en cuántos resultados ocurre cada evento. En una bolsa con 6 fichas verdes y 3 amarillas, sacar verde es más probable que sacar amarilla.",
        "Usamos tres expresiones. Más probable es el evento que ocurre en más resultados. Menos probable es el que ocurre en menos. Igualmente probables son dos eventos que ocurren en la misma cantidad de resultados, como sacar rojo o sacar azul de una bolsa con 5 de cada color.",
        "Esto solo vale cuando todos los resultados tienen las mismas posibilidades, como las fichas de una bolsa, las caras de un dado o los sectores iguales de una ruleta. El gusto de las personas no cambia el azar. " + COMP,
    ],
    vocab=[("más probable", "ocurre en más resultados que el otro evento"), ("menos probable", "ocurre en menos resultados que el otro evento"), ("igualmente probables", "ocurren en la misma cantidad de resultados"), ("comparar", "decir en qué se parecen o se diferencian dos cosas")],
    worked=[
        {"title": "Comparar dos colores de una bolsa", "problem": BOLSA_V + " Compara «sale verde» con «sale amarilla».", "steps": ["Hay 6 fichas verdes y 3 amarillas.", "6 es mayor que 3."], "answer": "Sacar verde es más probable que sacar amarilla"},
        {"title": "Eventos igualmente probables", "problem": "Una bolsa tiene 5 fichas azules y 5 rojas. Compara «sale azul» con «sale roja».", "steps": ["Azul ocurre en 5 resultados.", "Roja también ocurre en 5 resultados."], "answer": "Son igualmente probables"},
    ],
    mistakes=[
        {"wrong": "Decir que sacar roja es más probable porque es el color favorito.", "why": "Se usa el gusto y no la cantidad de fichas.", "fix": "Compara cuántas fichas hay de cada color."},
        {"wrong": "Decir que el color que está primero en la lista es más probable.", "why": "Se piensa que el orden de la lista influye.", "fix": "Solo importa la cantidad de resultados que cumplen cada evento."},
    ],
    tiers={
        "recovery": [
            ex(BOLSA_V + " ¿Qué es más probable: sacar verde o sacar amarilla?", "Sacar verde", "Hay 6 verdes y solo 3 amarillas."),
            ex(BOLSA_V + " ¿Qué es menos probable: sacar amarilla o sacar roja?", "Sacar roja", "Hay solo 1 roja y 3 amarillas."),
            ex("Dos eventos ocurren en la misma cantidad de resultados. ¿Cómo se llaman?", "Igualmente probables", "Ocurren en la misma cantidad de resultados."),
        ],
        "understand": [
            ex("Una bolsa tiene 4 fichas rojas y 4 azules. Compara «sale roja» con «sale azul».", "Son igualmente probables", "Cada color ocurre en 4 resultados."),
            ex(DADO + " Compara «sale un 6» con «sale un número par».", "Sale un número par es más probable", "El 6 es una cara; los pares son 3 caras: 2, 4 y 6."),
            ex(DADO + " Compara «sale un número menor que 3» con «sale un número mayor que 3».", "Sale un número mayor que 3 es más probable", "Menores que 3: 1 y 2. Mayores que 3: 4, 5 y 6."),
        ],
        "apply": [
            ex(DADO + " Compara «sale 3 o 6» con «sale un número impar».", "Sale un número impar es más probable", "3 o 6 son 2 caras; los impares 1, 3 y 5 son 3 caras."),
            ex("Una ruleta tiene 10 sectores iguales: 5 azules, 3 rojos y 2 verdes. Ordena los colores de más a menos probable.", "Azul, rojo, verde", "Azul 5, rojo 3 y verde 2."),
            ex("Una bolsa tiene 4 fichas rojas, 4 azules y 4 verdes. Compara «sale rojo o verde» con «sale azul».", "Sale rojo o verde es más probable", "Rojo o verde ocurre en 8 fichas; azul solo en 4."),
        ],
        "reason": [
            ex("Ema dice: «En una bolsa con 7 fichas azules y 3 rojas, sacar roja es más probable porque roja es mi color favorito». ¿Qué error tiene?", "Usa su gusto; hay más azules, entonces azul es más probable", "El color favorito no cambia la cantidad de fichas."),
            ex("Dani dice que en una bolsa con 4 rojas y 4 azules, sacar roja es más probable porque «roja está primero en la lista». ¿Tiene razón?", "No; son igualmente probables", "Ambos colores tienen 4 fichas."),
        ],
        "challenge": [
            ex("Una bolsa tiene 12 fichas: 6 rojas, 4 azules y 2 verdes. Compara «sale roja» con «sale azul o verde».", "Son igualmente probables", "Azul o verde son 4 + 2 = 6 fichas, igual que las rojas."),
            ex("Una bolsa tiene 3 fichas rojas y 3 azules. Agregas 1 ficha de un color. ¿De qué color para que sacar roja sea más probable que sacar azul?", "Roja", "Quedarían 4 rojas y 3 azules."),
        ],
    },
    context=[ex("En una canasta hay 8 manzanas y 3 peras. Sacas una fruta sin mirar. ¿Qué es más probable: sacar manzana o sacar pera?", "Sacar manzana", "Hay 8 manzanas y solo 3 peras.")],
    selfcheck=[
        ex("Una bolsa tiene 2 fichas verdes y 7 amarillas. ¿Qué es menos probable: sacar verde o sacar amarilla?", "Sacar verde", "Hay solo 2 verdes."),
        ex("Una bolsa tiene 6 fichas rojas y 6 azules. ¿Sacar roja y sacar azul son igualmente probables?", "Sí", "Ambos colores tienen 6 fichas."),
        ex(DADO + " ¿Qué es más probable: sale un 2 o sale un número menor que 5?", "Sale un número menor que 5", "Menores que 5: 1, 2, 3 y 4, que son 4 caras."),
    ],
    open_task=task(
        "Una bolsa tiene 9 fichas: 5 rojas, 3 azules y 1 verde. Escribe tres comparaciones entre colores, una con «más probable», una con «menos probable» y una con «igualmente probables» usando el color rojo, azul o verde. Para la tercera, imagina un cambio en la bolsa que haga a dos colores igualmente probables y descríbelo.",
        "Rojo es más probable que azul (5 y 3). Verde es menos probable que azul (1 y 3). Si agrego 2 fichas verdes, azul y verde quedan igualmente probables, con 3 cada uno.",
        ["tres comparaciones correctas", "usa las tres expresiones", "el cambio de la bolsa deja dos colores con igual cantidad"],
        ["tres comparaciones", "cambio descrito"],
        ["comparar por gusto", "no contar las fichas"],
        "Pide escribir cuántas fichas tiene cada color. Reconoce que compare cantidades.",
    ),
    reinforce="Con una bolsa de tapas de dos colores, di qué color es más probable al sacar una sin mirar.",
    extend="Escribe una bolsa con tres colores en que dos sean igualmente probables y el tercero sea menos probable.",
)

register(
    OA25, 2,
    materials="Lápiz y papel. Las ruletas y las bolsas están descritas con palabras y números en cada ejercicio; puedes dibujarlas.",
    use="Aprenderé a comparar probabilidades pasando de una bolsa a una ruleta o a una lista de resultados. Sirve para saber que distintas representaciones pueden mostrar lo mismo.",
    prior=["Sé decir qué evento es más probable, menos probable o igualmente probable.", "Sé qué es una ruleta con sectores iguales."],
    explain=[
        "Una misma situación se puede mostrar con una bolsa, una ruleta o una lista. La ruleta de 12 sectores iguales con 6 rojos, 4 azules y 2 verdes muestra lo mismo que una bolsa con 6 fichas rojas, 4 azules y 2 verdes. En ambas, rojo es el color más probable.",
        "También puedes escribir la lista de todos los resultados. Si la lista dice rojo, rojo, rojo, azul, azul, verde, entonces rojo aparece 3 veces, azul 2 y verde 1. Cuantas más veces aparece un color en la lista, más probable es.",
        "En una ruleta los sectores deben ser iguales para contarlos. Si no lo son, compara cuánto espacio del círculo ocupa cada color. Por ejemplo, un sector rojo que ocupa la mitad del círculo y varios azules chicos que ocupan la otra mitad hacen que ambos colores sean igualmente probables. " + COMP,
    ],
    vocab=[("sector", "cada parte de una ruleta"), ("representación", "forma de mostrar una situación, como una bolsa, una ruleta o una lista"), ("lista de resultados", "todos los resultados escritos uno por uno"), ("equivalente", "que muestra lo mismo con otra representación")],
    worked=[
        {"title": "De la ruleta a la bolsa", "problem": RUL12 + " ¿Qué bolsa muestra lo mismo?", "steps": ["Cada sector es una ficha del mismo color.", "Entonces la bolsa tiene 6 rojas, 4 azules y 2 verdes."], "answer": "La bolsa con 6 fichas rojas, 4 azules y 2 verdes"},
        {"title": "De la lista a la comparación", "problem": "La lista de resultados de una bolsa es: roja, roja, roja, azul, azul, verde. Compara «sale roja» con «sale azul».", "steps": ["Roja aparece 3 veces y azul aparece 2 veces.", "3 es mayor que 2."], "answer": "Sacar roja es más probable que sacar azul"},
    ],
    mistakes=[
        {"wrong": "Decir que en una ruleta con 7 sectores azules chicos y uno rojo que ocupa la mitad, azul es más probable porque hay más sectores.", "why": "Se cuentan los sectores sin ver que no son iguales.", "fix": "Si no son iguales, compara cuánto espacio ocupa cada color."},
        {"wrong": "Cambiar el número de fichas al pasar de la ruleta a la bolsa.", "why": "Se pierde la correspondencia entre sectores y fichas.", "fix": "Cada sector se cambia por una ficha del mismo color."},
    ],
    tiers={
        "recovery": [
            ex(RUL12 + " ¿Qué color es más probable?", "Rojo", "Tiene 6 sectores, más que los otros."),
            ex(RUL12 + " ¿Qué color es menos probable?", "Verde", "Tiene solo 2 sectores."),
            ex(RUL12 + " ¿Cuántas fichas azules tiene la bolsa que muestra lo mismo?", "4", "Cada sector azul se cambia por una ficha azul."),
        ],
        "understand": [
            ex("Una ruleta tiene 8 sectores iguales: 4 amarillos y 4 negros. Compara «cae en amarillo» con «cae en negro».", "Son igualmente probables", "Cada color tiene 4 sectores."),
            ex("Una bolsa tiene 9 fichas: 5 azules, 3 rojas y 1 verde. Si la muestras con una ruleta de 9 sectores iguales, ¿cuántos sectores azules lleva?", "5", "Cada ficha azul es un sector azul."),
            ex("La lista de resultados de una bolsa es: roja, roja, roja, azul, azul, verde. ¿Qué color es más probable?", "Roja", "Aparece 3 veces, más que los otros."),
        ],
        "apply": [
            ex("Una ruleta de 10 sectores iguales tiene 5 azules, 3 rojos y 2 verdes. Compara «cae en azul» con «cae en rojo o verde».", "Son igualmente probables", "Rojo o verde son 3 + 2 = 5 sectores, igual que azul."),
            ex("Bolsa 1: 3 rojas y 1 azul. Bolsa 2: 1 roja y 3 azules. ¿En cuál bolsa es más probable sacar roja?", "En la bolsa 1", "Tiene 3 rojas en 4 fichas; la otra tiene 1."),
            ex("Dos ruletas de 8 sectores iguales. En la primera hay 5 sectores verdes y en la segunda 3. ¿Es verdad que caer en verde es más probable en la primera?", "Sí", "5 sectores es mayor que 3 y el total es el mismo."),
        ],
        "reason": [
            ex("Julia dice que en una ruleta con 7 sectores azules chicos y 1 rojo que ocupa la mitad del círculo, caer en azul es más probable porque hay más sectores azules. ¿Está en lo correcto?", "No; el rojo ocupa la mitad y los azules la otra mitad, entonces son igualmente probables", "Los sectores no son iguales, así que se compara el espacio."),
            ex("Una bolsa, una ruleta de sectores iguales y una lista muestran 6 rojos, 4 azules y 2 verdes. ¿Cambia el color más probable según la representación?", "No; en las tres es el rojo", "Las tres muestran las mismas cantidades."),
        ],
        "challenge": [
            ex("Una ruleta de 6 sectores iguales tiene solo sectores azules, rojos y verdes, con al menos 1 de cada color. ¿Cuál es el menor número de sectores azules con que azul puede ser más probable que el rojo y que el verde?", "3", "Con 2 azules quedan 4 sectores para rojo y verde, y alguno tendría 2 o más; con 3 azules solo quedan 3, y ninguno llega a 3."),
            ex("¿Cuál ruleta de 8 sectores iguales cumple «amarillo es más probable y rojo y azul son igualmente probables»? A) 4 amarillos, 2 rojos, 2 azules B) 3 amarillos, 3 rojos, 2 azules C) 2 amarillos, 3 rojos, 3 azules D) 2 amarillos, 2 rojos, 4 azules", "A", "En A amarillo tiene 4 y los otros dos tienen 2 cada uno."),
        ],
    },
    context=[ex("Una caja de útiles tiene 6 lápices azules, 6 rojos y 3 negros. Sin mirar, sacas un lápiz. ¿Qué dos colores son igualmente probables?", "Azul y rojo", "Ambos tienen 6 lápices.")],
    selfcheck=[
        ex("Una ruleta de 5 sectores iguales tiene 4 verdes y 1 rojo. ¿Qué color es menos probable?", "Rojo", "Tiene solo 1 sector."),
        ex("La lista de una bolsa es: azul, azul, azul, azul, roja. ¿Qué color es más probable?", "Azul", "Aparece 4 veces."),
        ex("Una ruleta tiene 12 sectores iguales: 6 rojos, 4 azules y 2 verdes. ¿Verde es más probable que azul?", "No", "Verde tiene 2 sectores y azul tiene 4."),
    ],
    open_task=task(
        "Con esta ruleta de 10 sectores iguales: 4 rojos, 4 azules y 2 verdes. Escribe: la lista de los 10 resultados, la bolsa con fichas que muestra lo mismo y dos comparaciones entre colores con las palabras de la clase.",
        "Lista: rojo ×4, azul ×4, verde ×2. Bolsa: 4 rojas, 4 azules y 2 verdes. Rojo y azul son igualmente probables; verde es menos probable que rojo.",
        ["la lista tiene 10 resultados", "la bolsa tiene las mismas cantidades", "dos comparaciones correctas"],
        ["lista", "bolsa", "comparaciones"],
        ["cambiar las cantidades", "comparar sin contar"],
        "Pide contar que la lista tenga 10 resultados. Reconoce que las tres representaciones coincidan.",
    ),
    reinforce="Dibuja una ruleta de 8 sectores con 2 colores y escribe la bolsa que muestra lo mismo.",
    extend="Dibuja una ruleta con sectores desiguales y explica con palabras qué color es más probable según el espacio que ocupa.",
)

register(
    OA25, 3,
    materials="Lápiz y papel. Las bolsas están descritas con sus cantidades dentro de cada ejercicio.",
    use="Aprenderé tres estrategias para comparar sin calcular cuando las bolsas son distintas: comparar cantidades si el total es igual, mirar el total si las cantidades son iguales y comparar con la mitad. Sirve para elegir la mejor opción.",
    prior=["Sé comparar eventos en una misma bolsa.", "Sé encontrar la mitad de un número, incluso de uno impar: la mitad de 9 es 4 y medio."],
    explain=[
        "Si dos bolsas tienen el mismo total de fichas, tiene más posibilidades la que tiene más fichas del color pedido. En una bolsa de 10 fichas con 5 azules y otra de 10 con 3 azules, sacar azul es más probable en la primera.",
        "Si dos bolsas tienen la misma cantidad de fichas del color pedido pero distinto total, tiene más posibilidades la bolsa con menos fichas en total. Con 3 rojas, es más fácil sacar roja si la bolsa tiene 6 fichas que si tiene 12.",
        "Si los totales y las cantidades son distintos, compara cada bolsa con su mitad. Si el color tiene más de la mitad, es más probable que los otros colores juntos; si tiene exactamente la mitad, está en el medio; si tiene menos de la mitad, es menos probable. Para justificar, escribe los números que usaste. " + COMP,
    ],
    vocab=[("total", "cantidad de todas las fichas de la bolsa"), ("mitad", "una de las dos partes iguales de un número"), ("estrategia", "método para resolver un problema"), ("justificar", "explicar una decisión con razones")],
    worked=[
        {"title": "Misma cantidad, distinto total", "problem": "Bolsa X: 3 rojas entre 6 fichas. Bolsa Y: 3 rojas entre 12 fichas. ¿En cuál es más probable sacar roja?", "steps": ["Las dos bolsas tienen 3 rojas.", "En X hay menos fichas de otros colores que en Y."], "answer": "Es más probable en la bolsa X"},
        {"title": "Comparar con la mitad", "problem": "Bolsa M: 6 rojas entre 10 fichas. Bolsa N: 4 rojas entre 9 fichas. ¿En cuál es más probable sacar roja?", "steps": ["La mitad de 10 es 5 y 6 es más que 5.", "La mitad de 9 es 4 y medio, y 4 es menos que eso."], "answer": "Es más probable en la bolsa M"},
    ],
    mistakes=[
        {"wrong": "Decir que la bolsa con 8 fichas rojas de 100 es mejor que la de 3 rojas de 4 porque 8 es mayor que 3.", "why": "Se comparan solo las cantidades sin mirar el total.", "fix": "Mira cuántas fichas hay en total o compara con la mitad."},
        {"wrong": "Decir que dos bolsas con la mitad de fichas rojas son distintas porque tienen distinto total.", "why": "Se mira el total y no qué parte de la bolsa es roja.", "fix": "Si en ambas exactamente la mitad es roja, sacar roja es igualmente probable."},
    ],
    tiers={
        "recovery": [
            ex("Dos eventos en la misma bolsa de 10 fichas: A ocurre con 7 fichas y B con 2 fichas. ¿Cuál es más probable?", "A", "7 es mayor que 2."),
            ex("En la misma bolsa, A ocurre con 4 fichas y B también con 4. ¿Cómo son A y B?", "Igualmente probables", "Ocurren en la misma cantidad de resultados."),
            ex("En una bolsa hay más fichas rojas que azules. ¿Qué es más probable: sacar roja o sacar azul?", "Sacar roja", "Hay más rojas."),
        ],
        "understand": [
            ex("Bolsa X: 3 rojas entre 6 fichas. Bolsa Y: 3 rojas entre 12 fichas. ¿En cuál bolsa es más probable sacar roja?", "En la bolsa X", "Las dos tienen 3 rojas, pero X tiene menos fichas en total."),
            ex("Bolsa P: 5 azules entre 10 fichas. Bolsa Q: 3 azules entre 10 fichas. ¿En cuál es más probable sacar azul?", "En la bolsa P", "El total es el mismo y P tiene más azules."),
            ex("Bolsa M: 6 rojas entre 10 fichas. Bolsa N: 4 rojas entre 9 fichas. ¿En cuál es más probable sacar roja?", "En la bolsa M", "M tiene más que la mitad rojas y N tiene menos."),
        ],
        "apply": [
            ex("Bolsa K: 2 verdes entre 4 fichas. Bolsa L: 3 verdes entre 12 fichas. ¿En cuál es más probable sacar verde?", "En la bolsa K", "K tiene la mitad verdes; L tiene menos de la mitad."),
            ex("Bolsa A: 5 rojas entre 6 fichas. Bolsa B: 5 rojas entre 20 fichas. ¿En cuál es más probable sacar roja?", "En la bolsa A", "Las dos tienen 5 rojas, pero A tiene menos fichas en total."),
            ex("Bolsa 1: 4 azules entre 8 fichas. Bolsa 2: 5 azules entre 10 fichas. Compara sacar azul en ambas.", "Son igualmente probables", "En las dos, azul es exactamente la mitad."),
        ],
        "reason": [
            ex("Pedro dice: «En la bolsa A hay 2 rojas entre 4 fichas y en la B hay 3 rojas entre 10; sacar roja es más probable en B porque tiene más rojas». ¿Qué respondes?", "Se equivoca; en A hay la mitad rojas y en B menos de la mitad, por lo que es más probable en A", "La mitad de 10 es 5 y 3 es menos que 5."),
            ex("Lola dice que una bolsa con 8 rojas entre 100 fichas es mejor para sacar roja que una con 3 rojas entre 4. ¿Qué error tiene?", "Compara solo 8 y 3 sin ver el total; en la segunda casi todas son rojas", "En la primera 8 es mucho menos que la mitad de 100."),
        ],
        "challenge": [
            ex("Bolsa A: 5 rojas entre 9 fichas. Bolsa B: 4 rojas entre 8. Bolsa C: 3 rojas entre 7. Ordena las bolsas de la que más a la que menos favorece sacar roja.", "A, B, C", "A tiene más de la mitad rojas, B la mitad y C menos de la mitad."),
            ex("Una bolsa tiene 3 fichas rojas y, además, solo fichas azules. ¿Cuántas azules debe tener para que sacar roja y sacar azul sean igualmente probables?", "3", "Las dos cantidades deben ser iguales."),
        ],
    },
    context=[ex("La caja 1 tiene 2 tarjetas ganadoras entre 5. La caja 2 tiene 2 tarjetas ganadoras entre 20. ¿En cuál caja es más probable sacar una ganadora?", "En la caja 1", "Tienen las mismas ganadoras, y la caja 1 tiene menos tarjetas en total.")],
    selfcheck=[
        ex("Bolsa X: 1 azul entre 3 fichas. Bolsa Y: 1 azul entre 9 fichas. ¿En cuál es más probable sacar azul?", "En la bolsa X", "Misma cantidad de azules, pero X tiene menos fichas."),
        ex("Bolsa M: 7 verdes entre 10 fichas. Bolsa N: 2 verdes entre 10 fichas. ¿En cuál es más probable sacar verde?", "En la bolsa M", "Mismo total y M tiene más verdes."),
        ex("Bolsa U: 4 rojas entre 10 fichas. Bolsa V: 5 rojas entre 12 fichas. ¿Alguna de las dos tiene más de la mitad de fichas rojas?", "No, ninguna", "La mitad de 10 es 5 y 4 es menos; la mitad de 12 es 6 y 5 es menos."),
    ],
    open_task=task(
        "Compara estas dos bolsas para sacar una ficha roja: bolsa 1 con 4 rojas entre 12 fichas y bolsa 2 con 4 rojas entre 8 fichas. Escribe en cuál es más probable y justifica con dos estrategias distintas: comparar el total y comparar con la mitad.",
        "Es más probable en la bolsa 2. Total: las dos tienen 4 rojas, pero la bolsa 2 tiene menos fichas. Mitad: en la bolsa 2, 4 es la mitad de 8, y en la bolsa 1, 4 es menos que la mitad de 12.",
        ["elige la bolsa 2", "justifica con el total", "justifica con la mitad", "escribe los números"],
        ["elección", "dos justificaciones"],
        ["comparar solo las cantidades de rojas", "justificar sin números"],
        "Pide decir cuál es la mitad de cada total. Reconoce que use dos estrategias.",
    ),
    reinforce="Con dos bolsas de papel con fichas de dos colores, decide en cuál es más probable sacar un color y cuenta para comprobar.",
    extend="Inventa dos bolsas en que tengas que usar la mitad para decidir cuál es más probable y justifica.",
)

register(
    OA25, 4,
    materials="Lápiz y papel. Los dados, ruletas y bolsas están descritos con palabras y números en cada ejercicio.",
    use="Aprenderé a aplicar la comparación a juegos de dos jugadores y a decidir si un juego es justo o cómo cambiar sus reglas. Sirve para evaluar si un juego favorece a alguien.",
    prior=["Sé comparar eventos como más probable, menos probable o igualmente probables.", "Sé contar los resultados que cumplen un evento."],
    explain=[
        "Un juego de azar es justo cuando los dos jugadores tienen la misma posibilidad de ganar. Esto ocurre cuando sus eventos son igualmente probables. Si Ana gana con un número par y Beto con uno impar en un dado, ambos ganan en 3 caras, y el juego es justo.",
        "Si un jugador gana en más resultados que el otro, el juego no es justo y favorece a ese jugador. Si Ana gana con 1 o 2 y Beto con 3, 4, 5 o 6, Beto tiene ventaja porque gana en 4 caras y Ana en 2.",
        "Cuando el juego no es justo, se puede cambiar una regla. Por ejemplo, pasar un número de un jugador a otro, o agregar fichas al que tiene menos. Después de cualquier cambio hay que volver a contar los resultados de cada jugador. Quién empieza o quién gira primero no cambia la probabilidad.",
    ],
    vocab=[("juego justo", "juego en que los dos jugadores tienen la misma posibilidad de ganar"), ("ventaja", "mayor posibilidad de ganar que el otro jugador"), ("regla", "condición que dice cuándo gana cada jugador"), ("favorecer", "dar más posibilidades a un jugador")],
    worked=[
        {"title": "Un juego justo", "problem": DADO + " Ana gana si sale un número par y Beto gana si sale un número impar. ¿Es justo?", "steps": ["Los pares son 2, 4 y 6: 3 caras.", "Los impares son 1, 3 y 5: 3 caras."], "answer": "Es justo, porque ambos ganan en 3 caras"},
        {"title": "Cambiar una regla", "problem": DADO + " Ana gana con 1 o 2 y Beto gana con 3, 4, 5 o 6. ¿Cómo hacerlo justo?", "steps": ["Ana tiene 2 caras y Beto 4.", "Si Beto pasa una cara a Ana, cada uno queda con 3."], "answer": "Un número debe pasar de Beto a Ana"},
    ],
    mistakes=[
        {"wrong": "Decir que el juego es justo porque Ana tiene el número más grande.", "why": "Se mira el valor del número y no cuántos resultados le tocan.", "fix": "Cuenta en cuántos resultados gana cada jugador."},
        {"wrong": "Pensar que el que gira primero la ruleta tiene más probabilidad.", "why": "Se cree que el turno cambia el azar.", "fix": "Cada giro empieza igual para todos."},
    ],
    tiers={
        "recovery": [
            ex(DADO + " Ana gana si sale un número par y Beto si sale un número impar. ¿Quién tiene más probabilidad de ganar?", "Ninguno; son igualmente probables", "Cada uno gana con 3 caras."),
            ex("¿Cuándo es justo un juego de azar?", "Cuando los dos jugadores tienen la misma posibilidad de ganar", "Los eventos de ganar son igualmente probables."),
            ex(DADO + " Ana gana si sale 1 o 2 y Beto gana si sale 3, 4, 5 o 6. ¿A quién favorece el juego?", "A Beto", "Beto gana en 4 caras y Ana en 2."),
        ],
        "understand": [
            ex(DADO + " Ana gana con 1 o 2 y Beto con 3, 4, 5 o 6. ¿Es un juego justo?", "No", "Beto gana en más caras que Ana."),
            ex(DADO + " Ana gana con 1, 2 o 3 y Beto con 4, 5 o 6. ¿Es un juego justo?", "Sí", "Cada uno gana en 3 caras."),
            ex("Una ruleta tiene 8 sectores iguales. Luis gana si cae en rojo (3 sectores) y Mía si cae en azul (5 sectores). ¿Quién tiene más probabilidad de ganar?", "Mía", "5 sectores es mayor que 3."),
        ],
        "apply": [
            ex(DADO + " Ana gana con 1 o 2 y Beto con 3, 4, 5 o 6. Para que sea justo, ¿cuántos números de Beto deben pasar a Ana?", "1", "Así cada uno queda con 3 números."),
            ex("Una bolsa tiene 4 fichas rojas y 4 azules. Rosa gana si sale roja y Tito si sale azul. Agregas 2 fichas rojas. ¿Quién tiene ahora más posibilidades?", "Rosa", "Quedan 6 rojas y 4 azules."),
            ex("Después de agregar 2 rojas, la bolsa tiene 6 rojas y 4 azules. ¿Cuántas fichas azules hay que agregar para que el juego sea justo?", "2", "Con 6 azules y 6 rojas ambos ganan igual."),
        ],
        "reason": [
            ex("Gabo gana con el 6 y Eli gana con 1, 2, 3, 4 o 5. Gabo dice que es justo porque su número es el más grande. ¿Qué respondes?", "No es justo; Gabo gana en 1 cara y Eli en 5", "Importa cuántas caras gana cada uno, no el valor del número."),
            ex("En una ruleta de 10 sectores iguales, Ema gana con 5 sectores rojos y Fer con los 5 azules. Fer dice que tendrá ventaja si gira primero. ¿Es verdad?", "No; ambos tienen la misma posibilidad sin importar quién gira primero", "El orden del turno no cambia los sectores."),
        ],
        "challenge": [
            ex(DADO + " Ana gana con 4, 5 o 6. ¿Con qué números debe ganar Beto para que el juego sea justo?", "1, 2 y 3", "Son los tres números que quedan."),
            ex("Una ruleta tiene 12 sectores iguales: 5 rojos, 4 azules y 3 verdes. Ana gana si cae en rojo y Beto si cae en azul o verde. ¿Quién tiene ventaja?", "Beto", "Azul o verde son 4 + 3 = 7 sectores, más que los 5 rojos."),
        ],
    },
    context=[ex("En el recreo, Tomás y Ema juegan con una moneda: gana Tomás si sale cara y Ema si sale sello. ¿Es un juego justo?", "Sí", "Cara y sello son igualmente probables.")],
    selfcheck=[
        ex(DADO + " Ana gana con 1 y Beto con 2, 3, 4, 5 o 6. ¿A quién favorece?", "A Beto", "Gana en 5 caras y Ana en 1."),
        ex("Una ruleta tiene 6 sectores iguales: 3 rojos y 3 azules. Rosa gana con rojo y Tito con azul. ¿Es justo?", "Sí", "Cada uno gana en 3 sectores."),
        ex("Si un juego no es justo, ¿qué puedes hacer para arreglarlo?", "Cambiar la regla para que ambos ganen en la misma cantidad de resultados", "Hay que igualar los resultados de cada jugador."),
    ],
    open_task=task(
        "Con un dado normal, escribe las reglas de un juego de dos jugadores que sea justo y las de otro que no lo sea. En el segundo, explica quién tiene ventaja y cómo lo cambiarías para que sea justo.",
        "Justo: Ana gana con 1, 2 y 3 y Beto con 4, 5 y 6. No justo: Ana gana con 6 y Beto con los demás; Beto tiene ventaja porque gana en 5 caras. Para arreglarlo, Ana debe ganar con 3 números.",
        ["el primer juego da 3 números a cada jugador", "el segundo juego da distinta cantidad", "dice quién tiene ventaja y por qué", "propone un cambio que iguala"],
        ["dos juegos", "ventaja", "cambio"],
        ["mirar el valor del número", "no contar los resultados de cada jugador"],
        "Pide contar cuántas caras tiene cada jugador. Reconoce que repartió bien los resultados.",
    ),
    reinforce="Juega con una moneda o un dado y decide, contando, si las reglas son justas.",
    extend="Diseña un juego con una ruleta de 12 sectores en que un jugador tenga ventaja y explica cómo lo harías justo.",
)
