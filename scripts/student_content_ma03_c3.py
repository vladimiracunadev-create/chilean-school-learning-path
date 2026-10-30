"""Student material for 3.º básico Matemática, OA 23 (encuestas, tablas y gráficos de barra) y OA 24 (datos de juegos aleatorios)."""
from __future__ import annotations

from collections import Counter

from student_lessons import arith, ex, register

OA23, OA24 = "MA03 OA 23", "MA03 OA 24"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def tally(n: int) -> str:
    """Marcas de conteo: grupos de 5 como «||||/»."""
    return " ".join(["||||/"] * (n // 5) + (["|" * (n % 5)] if n % 5 else [])) or "(ninguna)"


def lista(items) -> str:
    return ", ".join(str(i) for i in items)


FRUTAS = ["manzana", "plátano", "naranja", "manzana", "manzana", "plátano", "naranja", "naranja", "manzana", "plátano", "manzana", "manzana"]
FC = Counter(FRUTAS)  # manzana 6, plátano 3, naranja 3
MASC = ["perro", "gato", "ninguna", "perro", "pez", "gato", "perro", "perro", "ninguna", "gato", "perro", "pez", "gato", "perro", "ninguna"]
MC = Counter(MASC)  # perro 6, gato 4, ninguna 3, pez 2
assert (FC["manzana"], FC["plátano"], FC["naranja"], len(FRUTAS)) == (6, 3, 3, 12)
assert (MC["perro"], MC["gato"], MC["ninguna"], MC["pez"], len(MASC)) == (6, 4, 3, 2, 15)
TABLA_MASC = "Tabla de mascotas: perro " + str(MC["perro"]) + ", gato " + str(MC["gato"]) + ", pez " + str(MC["pez"]) + ", ninguna " + str(MC["ninguna"]) + "."


def barras(pares, unidad="▮") -> str:
    return " ".join(f"{nombre}: {unidad * n}" for nombre, n in pares) + "."


GRAF_MASC = "Gráfico de barras (cada ▮ vale 1 niño; el eje va de 1 en 1): " + barras([("perro", 6), ("gato", 4), ("ninguna", 3), ("pez", 2)])


# ================================================================ OA 23
register(
    OA23, 1,
    materials="Lápiz y papel. Las preguntas y las categorías de cada ejercicio están escritas.",
    use="Aprenderé a escribir una pregunta clara para una encuesta, con respuestas posibles bien definidas. Sirve para juntar datos que se puedan contar.",
    prior=["Sé contar objetos y personas.", "Sé agrupar cosas en categorías, por ejemplo por color."],
    explain=[
        "Una encuesta es una pregunta que se hace a un grupo de personas para juntar datos. Una buena pregunta es clara: dice qué se quiere saber y entrega las respuestas posibles, que se llaman categorías.",
        "Por ejemplo: «¿Qué fruta prefieres: manzana, plátano o naranja?». Cada persona elige una sola categoría. Las categorías no se mezclan: una respuesta no puede caber en dos categorías al mismo tiempo. Conviene agregar «otra» por si alguien prefiere algo distinto.",
        "Las categorías se deciden antes de preguntar. Si las cambias después de recoger los datos, no puedes comparar bien las respuestas. Cada persona responde una sola vez, para no repetir datos.",
    ],
    vocab=[("encuesta", "preguntas que se hacen a un grupo para juntar datos"), ("pregunta clara", "pregunta que se entiende y tiene respuestas posibles"), ("categoría", "una de las respuestas posibles"), ("dato", "una respuesta registrada"), ("otra", "categoría para las respuestas que no están en la lista")],
    worked=[
        {"title": "Elegir la pregunta clara", "problem": "Quieres saber el sabor de helado favorito del curso. ¿Cuál sirve: A «¿Cuántos helados comes?» o B «¿Qué sabor prefieres: chocolate, frutilla o vainilla?»", "steps": ["A pregunta una cantidad, no un sabor.", "B pregunta por el sabor y da tres categorías."], "answer": "Sirve la pregunta B"},
        {"title": "Categorías que se mezclan", "problem": "Las categorías son «perro», «gato» y «animal». ¿Qué falla?", "steps": ["«Animal» incluye al perro y al gato.", "Una respuesta cabría en dos categorías."], "answer": "«Animal» se mezcla con las otras; hay que quitarla"},
    ],
    mistakes=[
        {"wrong": "Hacer una pregunta sin decir las respuestas posibles.", "why": "Cada persona responde algo distinto y no se pueden contar.", "fix": "Escribe las categorías en la pregunta."},
        {"wrong": "Cambiar las categorías después de recoger los datos.", "why": "Las respuestas ya no se pueden comparar.", "fix": "Decide las categorías antes de preguntar."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál pregunta es clara? A «¿Te gustan cosas?» o B «¿Qué fruta prefieres: manzana, plátano o naranja?»", "B", "B dice qué se pregunta y da las respuestas."),
            ex("En «¿Qué fruta prefieres: manzana, plátano o naranja?», ¿cuántas categorías hay?", "3", "Las categorías son manzana, plátano y naranja."),
            ex("¿Cuántas veces responde cada persona en una encuesta?", "Una vez", "Así no se repiten datos."),
        ],
        "understand": [
            ex("La pregunta es «¿Qué mascota tienes: perro, gato o pez?». Un niño tiene perro y gato. ¿Qué problema aparece?", "No puede elegir una sola categoría", "La pregunta pide una sola respuesta."),
            ex("¿Para qué sirve agregar la categoría «otra»?", "Para las respuestas que no están en la lista", "Así nadie queda sin poder responder."),
            ex("¿Por qué cada persona responde una sola vez?", "Para no repetir datos", "Si responde dos veces, un dato se cuenta doble."),
        ],
        "apply": [
            ex("Quieres conocer la estación del año favorita del curso. ¿Cuál pregunta sirve? A «¿Qué estación prefieres: verano, otoño, invierno o primavera?» o B «¿Hace frío?»", "A", "A pregunta por la estación y da las categorías."),
            ex("Una pregunta sobre el sabor de helado tiene las categorías chocolate, frutilla y vainilla. Una niña prefiere lúcuma. ¿Qué categoría conviene agregar?", "Otro sabor", "Así su respuesta tiene lugar."),
            ex("Se quiere saber qué juego prefiere el curso en el recreo. ¿Cuál pregunta sirve? A «¿Qué juego prefieres: pillarse, cuerda o pelota?» o B «¿Juegas?»", "A", "A pregunta por el juego y da las respuestas."),
        ],
        "reason": [
            ex("La pregunta «¿Te gusta más el fútbol o el vóleibol que el ajedrez?» mezcla varias cosas. ¿Es clara?", "No", "Compara tres cosas y no se sabe qué elegir."),
            ex("Un curso cambia las categorías después de preguntar. ¿Qué problema trae?", "No se pueden comparar las respuestas", "Los datos se recogieron con otras categorías."),
        ],
        "challenge": [
            ex("La pregunta es «¿Qué comes en el recreo?» con las categorías «plátano», «fruta» y «galleta». ¿Qué categoría falla y por qué?", "«Fruta»; incluye al plátano", "Un plátano cabría en dos categorías."),
            ex("La pregunta es «¿Cuánto tardas en llegar al colegio: menos de 10 minutos, de 10 a 20 minutos o más de 20 minutos?». Un niño tarda exactamente 20 minutos. ¿Qué categoría marca?", "De 10 a 20 minutos", "Esa categoría incluye el 20."),
        ],
    },
    context=[ex("El curso elegirá un juego para el recreo. ¿Qué categorías conviene poner en la pregunta: A «pillarse, cuerda, pelota, otro» o B «jugar, divertirse, correr»?", "A", "A nombra juegos distintos que no se mezclan.")],
    selfcheck=[
        ex("¿Cómo se llaman las respuestas posibles de una encuesta?", "Categorías", "Son las opciones entre las que se elige."),
        ex("¿Cuándo se deciden las categorías: antes o después de preguntar?", "Antes", "Así los datos se pueden comparar."),
        ex("¿Una respuesta puede caber en dos categorías a la vez?", "No", "Las categorías no deben mezclarse."),
    ],
    open_task=task(
        "Elige uno de estos temas: color favorito, deporte favorito o postre favorito. Escribe una pregunta clara con 3 categorías y la categoría «otra». Explica por qué cada persona responde una sola vez.",
        "Pregunta: «¿Qué color prefieres: rojo, azul, verde u otro?». Cada persona elige uno solo, para no repetir datos.",
        ["escribe una pregunta clara", "pone 3 categorías y «otra»", "las categorías no se mezclan", "explica la respuesta única"],
        ["pregunta escrita", "lista de categorías", "explicación"],
        ["categorías que se mezclan", "olvidar decir cómo se responde"],
        "Pide leer la pregunta en voz alta a otra persona. Reconoce si la pregunta se entiende sin explicar.",
    ),
    reinforce="Pregunta a tres personas de tu casa tu pregunta y anota la categoría que elige cada una.",
    extend="Escribe otra pregunta con categorías numéricas, por ejemplo cuántos libros leíste este mes: 0, 1, 2 o más.",
)

register(
    OA23, 2,
    materials="Lápiz y papel. Las respuestas de la encuesta están escritas en los ejercicios. Para marcar se usan palitos: cuatro palitos y uno cruzado forman un grupo de 5 (||||/).",
    use="Aprenderé a clasificar las respuestas de una encuesta sin perder ni repetir ningún dato. Sirve para contar bien.",
    prior=["Sé qué es una categoría.", "Sé contar hasta 20."],
    explain=[
        "Después de preguntar tienes una lista de respuestas. Para contarlas, clasifícalas: pasa por la lista una sola vez y haz una marca en la categoría que corresponde a cada respuesta. Así no pierdes ningún dato.",
        "Las marcas se hacen con palitos. Cuatro palitos y uno cruzado forman un grupo de 5 (||||/). Después cuentas de 5 en 5. Por ejemplo, ||||/ || son 7.",
        "Al final, suma todas las marcas. Deben dar la misma cantidad que respuestas hay en la lista. Si no coincide, faltó o sobró alguna marca. Una respuesta que no está en ninguna categoría va a «otra».",
    ],
    vocab=[("clasificar", "poner cada dato en su categoría"), ("marca", "palito con que se anota un dato"), ("grupo de cinco", "cuatro palitos con uno cruzado: ||||/"), ("total", "suma de todas las marcas"), ("revisar", "comprobar que el total coincide con la lista")],
    worked=[
        {"title": "Clasificar con marcas", "problem": f"Respuestas: {lista(FRUTAS)}. Cuenta cada fruta con marcas.", "steps": ["Recorro la lista una vez y marco cada respuesta en su fruta.", f"Manzana: {tally(FC['manzana'])} ({FC['manzana']}). Plátano: {tally(FC['plátano'])} ({FC['plátano']}). Naranja: {tally(FC['naranja'])} ({FC['naranja']}).", f"Reviso: {FC['manzana']} + {FC['plátano']} + {FC['naranja']} = {len(FRUTAS)}, igual que la lista."], "answer": f"Manzana {FC['manzana']}, plátano {FC['plátano']} y naranja {FC['naranja']}"},
        {"title": "Una respuesta fuera de las categorías", "problem": "Las categorías son perro, gato y otra. Alguien responde «conejo». ¿Dónde se marca?", "steps": ["«Conejo» no es ni perro ni gato.", "Va en «otra»."], "answer": "En la categoría «otra»"},
    ],
    mistakes=[
        {"wrong": "Contar la lista varias veces, una por cada categoría, y saltarse respuestas.", "why": "Se pierde la cuenta de qué datos ya se marcaron.", "fix": "Recorre la lista una sola vez y marca cada dato al leerlo."},
        {"wrong": "No revisar el total.", "why": "No se detectan datos perdidos o repetidos.", "fix": "Suma las marcas y compáralas con la cantidad de respuestas."},
    ],
    tiers={
        "recovery": [
            ex(f"Respuestas: {lista(FRUTAS)}. ¿Cuántas respuestas hay en total?", str(len(FRUTAS)), "Se cuentan todas las palabras de la lista."),
            ex(f"Respuestas: {lista(FRUTAS)}. ¿Cuántas veces aparece «naranja»?", str(FC["naranja"]), "Se cuentan las veces que se repite esa palabra."),
            ex("¿Cuántos palitos forman un grupo de 5 en las marcas?", "5", "Cuatro palitos y uno cruzado son cinco."),
        ],
        "understand": [
            ex("¿Cuántos son ||||/ ||?", "7", "Un grupo de 5 y 2 palitos más.", calc="5+2"),
            ex(f"Respuestas: {lista(FRUTAS)}. ¿Cuántas veces aparece «manzana»?", str(FC["manzana"]), "Se cuentan las veces que se repite esa palabra."),
            ex("Al final de clasificar, ¿qué debe pasar con la suma de las marcas?", "Debe dar igual que la cantidad de respuestas", "Así sabes que no perdiste datos."),
        ],
        "apply": [
            ex(f"Respuestas: {lista(FRUTAS)}. Escribe las marcas del plátano con grupos de 5.", tally(FC["plátano"]) + f" ({FC['plátano']})", "Hay 3 plátanos y son menos de un grupo de 5."),
            ex(f"Respuestas: {lista(FRUTAS)}. ¿Cuántas más manzanas que naranjas hay?", str(FC["manzana"] - FC["naranja"]), f"{FC['manzana']} − {FC['naranja']} = {FC['manzana'] - FC['naranja']}."),
            ex("Categorías: rojo, azul y otro. Alguien responde «verde». ¿En qué categoría lo marcas?", "En «otro»", "Verde no está en las demás categorías."),
        ],
        "reason": [
            ex("Un niño cuenta 5 manzanas, 3 plátanos y 3 naranjas, que suman 11, pero la lista tiene 12 respuestas. ¿Qué debe hacer?", "Revisar la lista porque faltó una marca", "El total debe coincidir con las respuestas."),
            ex("Ana recorre la lista tres veces, una para cada fruta, y salta una respuesta. ¿Qué método de esta clase evita ese error?", "Recorrer la lista una sola vez marcando cada dato", "Se marca todo al leerlo."),
        ],
        "challenge": [
            ex(f"Respuestas: {lista(FRUTAS)}. ¿Qué fruta fue la más elegida y cuántas respuestas más tuvo que la segunda?", f"Manzana; {FC['manzana'] - FC['plátano']} más que plátano o naranja", f"{FC['manzana']} − {FC['plátano']} = {FC['manzana'] - FC['plátano']}."),
            ex("Se contaron 8 palitos así: ||||/ |||. Ahora llega una respuesta más. ¿Cómo queda la marca?", "||||/ ||||", "8 más 1 son 9: un grupo de 5 y 4 palitos."),
        ],
    },
    context=[ex("Seis niños responden a la pregunta «¿Qué prefieres: pillarse, cuerda o pelota?»: pelota, cuerda, pelota, pillarse, pelota, cuerda. ¿Cuántos eligieron pelota?", "3", "Pelota aparece 3 veces en la lista.")],
    selfcheck=[
        ex("Según el método de esta clase, ¿cuántas veces se recorre la lista al clasificar?", "Una vez", "Se marca cada dato al leerlo."),
        ex("¿Cuántos son ||||/ ||||/?", "10", "Dos grupos de 5.", calc="5+5"),
        ex("¿Dónde se marca una respuesta que no está en ninguna categoría?", "En «otra»", "Esa categoría guarda las respuestas distintas."),
    ],
    open_task=task(
        f"Usa estas respuestas a «¿Qué mascota tienes: perro, gato, pez o ninguna?»: {lista(MASC)}. Clasifícalas con marcas, escribe cuántas hay de cada una y comprueba que el total es {len(MASC)}.",
        f"Perro {tally(MC['perro'])} ({MC['perro']}), gato {tally(MC['gato'])} ({MC['gato']}), ninguna {tally(MC['ninguna'])} ({MC['ninguna']}), pez {tally(MC['pez'])} ({MC['pez']}). Total: {MC['perro']} + {MC['gato']} + {MC['ninguna']} + {MC['pez']} = {len(MASC)}.",
        ["recorre la lista una vez", "usa marcas de 5 en 5", "escribe el número de cada categoría", "comprueba el total"],
        ["marcas por categoría", "números", "suma de comprobación"],
        ["perder o repetir un dato", "no comprobar el total"],
        "Pide tachar cada respuesta al marcarla. Reconoce que el total coincide con la lista.",
    ),
    reinforce="Anota los colores de seis cosas de tu casa y clasifícalos con marcas.",
    extend="Inventa una lista de 10 respuestas con tres categorías y cuéntalas con marcas.",
)

register(
    OA23, 3,
    materials="Lápiz y papel. Los datos están escritos en los ejercicios.",
    use="Aprenderé a construir una tabla de frecuencias, que muestra cuántas veces aparece cada categoría. Sirve para ordenar los datos y leerlos rápido.",
    prior=["Sé clasificar respuestas con marcas.", "Sé sumar números hasta 100."],
    explain=[
        "Una tabla de frecuencias tiene dos columnas: una para la categoría y otra para la frecuencia. La frecuencia es cuántas veces aparece cada categoría. Se escribe con un número, no con palitos.",
        f"Por ejemplo, para las mascotas de 15 niños: perro {MC['perro']}, gato {MC['gato']}, pez {MC['pez']} y ninguna {MC['ninguna']}. Al sumar las frecuencias obtienes el total de datos: {MC['perro']} + {MC['gato']} + {MC['pez']} + {MC['ninguna']} = 15.",
        "La tabla permite responder preguntas. La categoría con la frecuencia mayor es la más elegida. Para saber cuántas más, resta las frecuencias. Siempre revisa que el total sea el número de personas que respondieron.",
    ],
    vocab=[("tabla de frecuencias", "tabla que muestra cuántas veces aparece cada categoría"), ("frecuencia", "número de veces que aparece una categoría"), ("total", "suma de todas las frecuencias"), ("la más elegida", "la categoría con mayor frecuencia"), ("la menos elegida", "la categoría con menor frecuencia")],
    worked=[
        {"title": "Leer una tabla", "problem": f"{TABLA_MASC} ¿Cuál fue la mascota más elegida?", "steps": ["Comparo las frecuencias: 6, 4, 2 y 3.", "La mayor es 6, que es perro."], "answer": "Perro"},
        {"title": "Calcular el total", "problem": f"{TABLA_MASC} ¿Cuántos niños respondieron?", "steps": [f"Sumo las frecuencias: {MC['perro']} + {MC['gato']} + {MC['pez']} + {MC['ninguna']}.", "La suma es 15."], "answer": "15 niños"},
    ],
    mistakes=[
        {"wrong": "Decir que la más elegida es la categoría que aparece primero en la tabla.", "why": "No se comparan las frecuencias.", "fix": "Busca el número mayor de la columna de frecuencias."},
        {"wrong": "Olvidar una categoría al sumar el total.", "why": "Se suman sólo algunas frecuencias.", "fix": "Suma todas las filas y compara con la lista."},
    ],
    tiers={
        "recovery": [
            ex(f"{TABLA_MASC} ¿Cuántos niños tienen un gato?", str(MC["gato"]), "Se lee la frecuencia de gato."),
            ex(f"{TABLA_MASC} ¿Cuántos niños tienen un pez?", str(MC["pez"]), "Se lee la frecuencia de pez."),
            ex("¿Cómo se llama el número de veces que aparece una categoría?", "Frecuencia", "Esa es la definición de frecuencia."),
        ],
        "understand": [
            ex(f"{TABLA_MASC} ¿Cuál es la mascota menos elegida?", "Pez", "Pez tiene la frecuencia menor, 2."),
            arith(f"{TABLA_MASC} ¿Cuántos niños tienen perro o gato?", f"{MC['perro']}+{MC['gato']}", "Se suman las frecuencias de perro y de gato."),
            ex("¿Qué se hace para saber cuántos más eligieron una categoría que otra?", "Se restan las frecuencias", "La diferencia se calcula con una resta."),
        ],
        "apply": [
            arith(f"{TABLA_MASC} ¿Cuántos niños más tienen perro que gato?", f"{MC['perro']}-{MC['gato']}", "Se resta la frecuencia menor a la mayor."),
            arith(f"{TABLA_MASC} ¿Cuántos niños tienen alguna mascota (perro, gato o pez)?", f"{MC['perro']}+{MC['gato']}+{MC['pez']}", "Se suman las categorías con mascota, sin «ninguna»."),
            ex(f"Respuestas: {lista(FRUTAS)}. Escribe la tabla de frecuencias en la forma «fruta número».", f"manzana {FC['manzana']}, plátano {FC['plátano']}, naranja {FC['naranja']}", "Se cuentan las veces de cada fruta."),
        ],
        "reason": [
            ex("Rosa dice que la mascota más elegida es «perro» sólo porque está primera en la tabla. ¿Qué debe hacer para estar segura?", "Comparar las frecuencias", "El orden no dice cuál es mayor."),
            ex("Una tabla suma 14, pero respondieron 15 niños. ¿Qué puede haber pasado?", "Faltó contar una respuesta o se olvidó una categoría", "El total debe ser igual a los que respondieron."),
        ],
        "challenge": [
            ex("Hay dos categorías con la misma frecuencia más alta. ¿Se puede decir cuál fue «la más elegida»?", "No; hay un empate", "Dos categorías comparten el mayor número."),
            ex(f"{TABLA_MASC} Si se agregan 3 niños más con pez, ¿cuál será entonces la frecuencia de pez?", "5", "2 + 3 = 5.", calc="2+3"),
        ],
    },
    context=[ex(f"{TABLA_MASC} La profesora quiere comprar premios del mismo tipo para la mascota más elegida. ¿Para qué mascota los compra?", "Para perro", "Perro tiene la frecuencia mayor.")],
    selfcheck=[
        ex(f"{TABLA_MASC} ¿Cuántos niños no tienen mascota?", str(MC["ninguna"]), "Se lee la frecuencia de ninguna."),
        arith(f"{TABLA_MASC} ¿Cuántos niños más tienen gato que pez?", f"{MC['gato']}-{MC['pez']}", "Se resta la frecuencia menor a la mayor."),
        ex("¿Qué se suma para obtener el total de una tabla de frecuencias?", "Todas las frecuencias", "El total es la suma de todas las filas."),
    ],
    open_task=task(
        "Usa estas respuestas a «¿Qué postre prefieres?»: helado, fruta, helado, torta, fruta, helado, fruta, fruta, torta, helado, helado, fruta. Construye una tabla de frecuencias con las categorías helado, fruta y torta. Escribe el total y cuál o cuáles fueron las más elegidas.",
        "Helado 5, fruta 5 y torta 2: hay 12 respuestas. Helado y fruta empatan como las más elegidas.",
        ["clasifica las 12 respuestas", "escribe una tabla con categoría y frecuencia", "suma el total y lo compara con 12", "responde cuál fue la más elegida"],
        ["tabla de frecuencias", "total", "respuesta a la pregunta"],
        ["perder respuestas", "no ver el empate"],
        "Pide revisar que el total sea 12. Reconoce que note el empate.",
    ),
    reinforce="Haz una tabla de frecuencias con los colores de seis lápices o juguetes de tu casa.",
    extend="Agrega una columna a tu tabla que diga cuántos más o cuántos menos tiene cada categoría que la más elegida.",
)

register(
    OA23, 4,
    materials="Lápiz, regla y papel cuadriculado. Los datos y la escala están escritos en los ejercicios. Cada cuadradito de la barra vale lo que dice la escala.",
    use="Aprenderé a dibujar un gráfico de barras desde una tabla y a sacar conclusiones. Sirve para comparar las categorías de un vistazo.",
    prior=["Sé armar una tabla de frecuencias.", "Sé contar de 1 en 1 y de 2 en 2."],
    explain=[
        "Un gráfico de barras muestra la tabla con barras. Cada categoría tiene una barra. Mientras más alta o larga es la barra, mayor es la frecuencia. Las barras tienen todas el mismo ancho.",
        "El gráfico necesita una escala: dice cuánto vale cada cuadradito de la barra o cada raya del eje. Si la escala es de 1 en 1, una barra de 6 cuadraditos vale 6. Sin escala no se sabe cuánto vale cada barra.",
        "Para concluir, lee el gráfico: la barra más larga es la categoría más elegida, la más corta es la menos elegida, y puedes restar para saber cuánto más. Una buena conclusión usa números del gráfico.",
    ],
    vocab=[("gráfico de barras", "dibujo que muestra la frecuencia de cada categoría con barras"), ("barra", "rectángulo cuyo largo muestra la frecuencia"), ("escala", "lo que vale cada cuadradito o raya"), ("eje", "línea con los números del gráfico"), ("conclusión", "lo que aprendo al leer el gráfico")],
    worked=[
        {"title": "Dibujar las barras", "problem": f"{TABLA_MASC} Dibuja un gráfico con escala de 1 en 1.", "steps": ["Dibujo una barra por categoría.", "Perro: 6 cuadraditos; gato: 4; pez: 2; ninguna: 3.", "Escribo la escala: cada cuadradito vale 1 niño."], "answer": GRAF_MASC},
        {"title": "Sacar una conclusión", "problem": f"{GRAF_MASC} ¿Qué se puede concluir?", "steps": ["La barra más larga es perro, con 6.", "La más corta es pez, con 2.", "6 − 2 = 4."], "answer": "Hay 4 niños más con perro que con pez"},
    ],
    mistakes=[
        {"wrong": "Dibujar las barras sin escala.", "why": "No se sabe cuánto vale cada barra.", "fix": "Escribe siempre cuánto vale cada cuadradito o raya."},
        {"wrong": "Hacer las barras con distinto ancho.", "why": "Una barra más ancha parece mayor sin serlo.", "fix": "Dibuja todas las barras con el mismo ancho."},
    ],
    tiers={
        "recovery": [
            ex(GRAF_MASC + " ¿Cuántos niños tienen un gato?", "4", "La barra de gato tiene 4 cuadraditos."),
            ex(GRAF_MASC + " ¿Qué barra es la más larga?", "Perro", "Tiene 6 cuadraditos."),
            ex("¿Qué dice la escala de un gráfico?", "Cuánto vale cada cuadradito o raya", "Sin escala no se puede leer."),
        ],
        "understand": [
            ex(GRAF_MASC + " ¿Cuál es la categoría menos elegida?", "Pez", "Su barra tiene solo 2 cuadraditos."),
            arith(GRAF_MASC + " ¿Cuántos niños más tienen perro que pez?", "6-2", "Se resta la frecuencia menor a la mayor."),
            ex("¿Por qué todas las barras deben tener el mismo ancho?", "Para que se comparen solo por el largo", "Si no, una barra ancha parece mayor."),
        ],
        "apply": [
            ex("Tabla: manzana 6, plátano 3, naranja 3. Con escala de 1 en 1, ¿cuántos cuadraditos tiene la barra de manzana?", "6", "Cada cuadradito vale 1."),
            ex("Tabla: helado 5, fruta 5, torta 2. Con escala de 1 en 1, ¿cuántos cuadraditos tiene la barra de torta?", "2", "Cada cuadradito vale 1."),
            arith("Tabla: manzana 6, plátano 3, naranja 3. ¿Cuántos niños eligieron plátano o naranja en total?", "3+3", "Se suman las dos frecuencias."),
        ],
        "reason": [
            ex("Un gráfico no tiene escala. Luis dice que la barra larga vale 10. ¿Se puede saber?", "No; sin escala no se sabe lo que vale", "La escala dice el valor de cada cuadradito."),
            ex(GRAF_MASC + " Pía concluye: «a la mayoría de los niños no les gustan las mascotas». ¿Es correcta?", "No; la barra de ninguna es de las más cortas, con 3", "Sólo 3 niños no tienen mascota."),
        ],
        "challenge": [
            ex("Tabla: manzana 6, plátano 3, naranja 3. Con escala de 2 en 2, ¿cuántos cuadraditos tiene la barra de manzana?", "3", "Cada cuadradito vale 2 y 6 ÷ 2 = 3.", calc="6//2"),
            arith(GRAF_MASC + " ¿Cuántos niños respondieron en total?", "6+4+3+2", "Se suman las cuatro barras."),
        ],
    },
    context=[ex("En un curso se pregunta el juego favorito: pelota 7, cuerda 4, pillarse 5. Con escala de 1 en 1, ¿cuál barra es la más corta?", "Cuerda", "Cuerda tiene 4 y es la menor.")],
    selfcheck=[
        ex("¿Qué muestra la barra más larga de un gráfico?", "La categoría con mayor frecuencia", "A mayor largo, mayor frecuencia."),
        ex("Con escala de 1 en 1, una barra de 5 cuadraditos, ¿cuánto vale?", "5", "Cada cuadradito vale 1."),
        ex("¿Qué debe llevar siempre un gráfico de barras para poder leerse bien?", "Escala", "La escala dice el valor de las barras."),
    ],
    open_task=task(
        "Con la tabla manzana 6, plátano 3 y naranja 3, dibuja en papel cuadriculado un gráfico de barras con escala de 1 en 1. Escribe la escala y una conclusión con números.",
        "Barras de 6, 3 y 3 cuadraditos del mismo ancho. Escala: cada cuadradito vale 1 niño. Conclusión: manzana fue la más elegida, con 3 votos más que plátano.",
        ["dibuja tres barras del mismo ancho", "usa los largos 6, 3 y 3", "escribe la escala", "concluye usando números"],
        ["gráfico dibujado", "escala escrita", "conclusión"],
        ["dibujar sin escala", "barras de distinto ancho"],
        "Pide leer el gráfico a otra persona. Reconoce la conclusión con números del gráfico.",
    ),
    reinforce="Dibuja un gráfico de barras con 3 cantidades de objetos de tu casa y escribe la escala.",
    extend="Haz el mismo gráfico con escala de 2 en 2 y explica qué cambia en el dibujo.",
)


# ================================================================ OA 24
DADO = [3, 5, 1, 3, 6, 2, 3, 5, 4, 1, 6, 3, 2, 5, 3, 4, 1, 6, 3, 5]
DC = Counter(DADO)  # 20 lanzamientos
assert len(DADO) == 20
DADO2 = [2, 4, 6, 4, 2, 5, 4, 6, 3, 4, 5, 6, 2, 4, 3]
D2C = Counter(DADO2)
assert len(DADO2) == 15 and min(DADO2) == 2 and max(DADO2) == 6
MONEDA_A = ["cara", "sello", "cara", "cara", "sello", "sello", "cara", "cara", "cara", "sello", "cara", "sello", "sello", "cara", "sello", "cara", "cara", "sello", "sello", "cara"]
MONEDA_B = ["sello", "sello", "cara", "sello", "cara", "cara", "sello", "cara", "sello", "sello", "cara", "sello", "cara", "sello", "sello", "cara", "cara", "sello", "cara", "sello"]
MA, MB = Counter(MONEDA_A), Counter(MONEDA_B)
assert len(MONEDA_A) == len(MONEDA_B) == 20

register(
    OA24, 1,
    materials="Lápiz y papel. Si tienes un dado y una moneda, puedes lanzarlos. Todos los resultados de los ejercicios están escritos.",
    use="Aprenderé a anotar los resultados de lanzar un dado o una moneda sin dejar ninguno afuera. Sirve para estudiar juegos de azar.",
    prior=["Sé contar con marcas de 5 en 5.", "Sé que un dado tiene caras con 1, 2, 3, 4, 5 y 6 puntos."],
    explain=[
        "Un juego de azar es uno donde no puedes saber de antemano qué saldrá, como lanzar un dado o una moneda. Cada lanzamiento da un resultado. Un dado puede dar 1, 2, 3, 4, 5 o 6. Una moneda da cara o sello.",
        "Para registrar, haz una tabla con todos los resultados posibles y marca un palito cada vez que sale uno. Así no dejas ninguno afuera. Al terminar, la frecuencia de un resultado es cuántos palitos tiene.",
        "Revisa que la suma de todas las frecuencias sea igual a la cantidad de lanzamientos. Si lanzaste 20 veces, el total debe ser 20. Si no cuadra, faltó anotar algún resultado o se anotó uno de más.",
    ],
    vocab=[("azar", "cuando no se sabe de antemano qué resultado saldrá"), ("lanzamiento", "cada vez que se lanza el dado o la moneda"), ("resultado", "lo que sale en un lanzamiento"), ("frecuencia", "cuántas veces salió un resultado"), ("registro", "tabla donde se anotan los resultados")],
    worked=[
        {"title": "Registrar los lanzamientos de un dado", "problem": f"Se lanzó un dado 20 veces: {lista(DADO)}. ¿Cuántas veces salió el 3?", "steps": ["Recorro la lista una vez y marco cada resultado.", f"El 3 aparece {DC[3]} veces: {tally(DC[3])}."], "answer": f"Salió {DC[3]} veces"},
        {"title": "Comprobar el total", "problem": f"Las frecuencias de los resultados 1 al 6 son {', '.join(str(DC[i]) for i in range(1, 7))}. ¿Suman 20?", "steps": ["Escribo la suma de las seis frecuencias.", " + ".join(str(DC[i]) for i in range(1, 7)) + f" = {sum(DC.values())}."], "answer": "Sí, suman 20"},
    ],
    mistakes=[
        {"wrong": "Anotar sólo los resultados que más salieron.", "why": "Se dejan datos afuera.", "fix": "Haz una fila para cada resultado posible y marca todos."},
        {"wrong": "No comprobar que el total coincide con los lanzamientos.", "why": "No se ven los datos perdidos.", "fix": "Suma las frecuencias y compara con la cantidad de lanzamientos."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué resultados puede dar un dado?", "1, 2, 3, 4, 5 y 6", "Son las seis caras del dado."),
            ex("¿Qué resultados puede dar una moneda?", "Cara o sello", "Una moneda tiene dos caras."),
            ex(f"Resultados de un dado: {lista(DADO)}. ¿Cuántos lanzamientos son?", "20", "Se cuentan todos los números de la lista."),
        ],
        "understand": [
            ex(f"Resultados de un dado: {lista(DADO)}. ¿Cuántas veces salió el 1?", str(DC[1]), "Se cuentan las veces que aparece el 1."),
            ex(f"Resultados de un dado: {lista(DADO)}. ¿Cuántas veces salió el 6?", str(DC[6]), "Se cuentan las veces que aparece el 6."),
            ex("¿Qué es la frecuencia de un resultado?", "Cuántas veces salió", "Es el número de marcas de ese resultado."),
        ],
        "apply": [
            ex(f"Resultados de un dado: {lista(DADO)}. Escribe con marcas cuántas veces salió el 5.", tally(DC[5]) + f" ({DC[5]})", "El 5 aparece " + str(DC[5]) + " veces."),
            ex(f"Resultados de un dado: {lista(DADO)}. ¿Cuántas veces salió el 2?", str(DC[2]), "Se cuentan las veces que aparece el 2."),
            ex(f"Resultados de un dado: {lista(DADO)}. ¿Cuántas veces salió el 4?", str(DC[4]), "Se cuentan las veces que aparece el 4."),
        ],
        "reason": [
            ex(f"Las frecuencias de un dado lanzado 20 veces son {', '.join(str(DC[i]) for i in range(1, 7) if i != 4)} y falta anotar el 4. ¿Cuánto debe valer la del 4 para que el total sea 20?", str(DC[4]), f"El resto suma {20 - DC[4]} y 20 − {20 - DC[4]} = {DC[4]}."),
            ex("Al registrar, Tomás anota sólo los resultados 6 y 5 porque son los más altos. ¿Qué error comete?", "Deja datos afuera; hay que anotar todos los resultados", "Todos los lanzamientos cuentan."),
        ],
        "challenge": [
            ex(f"Resultados de un dado: {lista(DADO)}. ¿Qué resultado salió más veces y cuántas?", f"El 3, {DC[3]} veces", "Tiene la frecuencia mayor."),
            ex(f"Resultados de una moneda en 20 lanzamientos: {lista(MONEDA_A)}. ¿Cuántas veces salió cara?", str(MA["cara"]), "Se cuentan las veces que aparece cara."),
        ],
    },
    context=[ex(f"Beto lanza una moneda 20 veces y anota: {lista(MONEDA_A)}. ¿Cuántas veces salió sello?", str(MA["sello"]), "Se cuentan las veces que aparece sello.")],
    selfcheck=[
        ex("Si lanzas un dado 12 veces, ¿cuánto debe sumar el total de las frecuencias?", "12", "Hay una marca por cada lanzamiento."),
        ex("¿Cuántos resultados distintos puede dar un dado?", "6", "Del 1 al 6."),
        ex("Si el total de marcas no coincide con los lanzamientos, ¿qué hay que hacer?", "Revisar el registro", "Faltó o sobró alguna marca."),
    ],
    open_task=task(
        f"Con estos resultados de un dado: {lista(DADO)}, arma una tabla de frecuencias para los resultados del 1 al 6. Usa marcas y números, y comprueba que el total es 20.",
        "Tabla: " + "; ".join(f"{i}: {tally(DC[i])} ({DC[i]})" for i in range(1, 7)) + f". Total: {sum(DC.values())}.",
        ["tiene una fila por cada resultado del 1 al 6", "marca todos los lanzamientos", "escribe las frecuencias", "comprueba el total"],
        ["tabla con marcas", "suma de las frecuencias"],
        ["omitir un resultado", "no comprobar el total"],
        "Pide tachar cada número de la lista al marcarlo. Reconoce que revise el total.",
    ),
    reinforce="Si tienes un dado, lánzalo 10 veces y anota los resultados con marcas. Si no, usa los datos de esta clase.",
    extend="Anota 12 lanzamientos de una moneda con marcas y escribe cuántas veces salió cara y cuántas sello.",
)

register(
    OA24, 2,
    materials="Lápiz y papel. Los registros de dado están escritos en los ejercicios.",
    use="Aprenderé a ordenar los resultados y sus frecuencias de menor a mayor. Sirve para ver qué resultado salió más y cuál menos.",
    prior=["Sé registrar los resultados de un dado con marcas.", "Sé ordenar números hasta 100."],
    explain=[
        "Los resultados de un dado se pueden ordenar de dos maneras. Una es por el número que salió: 1, 2, 3, 4, 5 y 6. La otra es por la frecuencia: del resultado que salió menos veces al que salió más veces.",
        "Para ordenar por frecuencia, escribe cada resultado con su frecuencia, por ejemplo «1 → 3 veces». Luego compara las frecuencias y ordénalas de menor a mayor. Si dos son iguales, hay un empate y puedes escribirlas juntas.",
        "Al ordenar, mantén cada resultado con su frecuencia. No cambies las frecuencias de lugar sin sus resultados, porque se mezclarían los datos.",
    ],
    vocab=[("ordenar", "poner en fila de menor a mayor o de mayor a menor"), ("de menor a mayor", "empezando por el valor más chico"), ("de mayor a menor", "empezando por el valor más grande"), ("empate", "dos resultados con la misma frecuencia"), ("más frecuente", "el resultado que salió más veces")],
    worked=[
        {"title": "Ordenar por número", "problem": f"Frecuencias de un dado: " + ", ".join(f"{i} → {D2C[i]}" for i in range(2, 7)) + ". Ordena los resultados por el número que salió.", "steps": ["Los resultados son 2, 3, 4, 5 y 6.", "Ya están de menor a mayor."], "answer": "2, 3, 4, 5, 6"},
        {"title": "Ordenar por frecuencia", "problem": "Frecuencias: 2 → 3, 3 → 2, 4 → 5, 5 → 2, 6 → 3. Ordena los resultados por frecuencia, de menor a mayor.", "steps": ["Las frecuencias son 3, 2, 5, 2, 3.", "De menor a mayor: 2, 2, 3, 3, 5.", "Los resultados correspondientes: 3 y 5 (2 veces), 2 y 6 (3 veces), 4 (5 veces)."], "answer": "3 y 5, luego 2 y 6, y al final 4"},
    ],
    mistakes=[
        {"wrong": "Ordenar las frecuencias pero perder qué resultado tiene cada una.", "why": "Se separa la frecuencia de su resultado.", "fix": "Escribe siempre pares: resultado y frecuencia."},
        {"wrong": "Ordenar de mayor a menor cuando se pidió de menor a mayor.", "why": "Se lee mal la instrucción.", "fix": "Subraya «menor a mayor» o «mayor a menor» antes de empezar."},
    ],
    tiers={
        "recovery": [
            ex("Ordena de menor a mayor las frecuencias 4, 1 y 3.", "1, 3, 4", "El 1 es el menor y el 4 el mayor."),
            ex("Ordena de mayor a menor las frecuencias 2, 5 y 3.", "5, 3, 2", "El 5 es el mayor y el 2 el menor."),
            ex("Frecuencias: 1 → 2, 2 → 4, 3 → 1. ¿Qué resultado salió más veces?", "El 2", "Tiene la frecuencia mayor, 4."),
        ],
        "understand": [
            ex("Frecuencias: 1 → 2, 2 → 4, 3 → 1. ¿Qué resultado salió menos veces?", "El 3", "Tiene la frecuencia menor, 1."),
            ex("Dos resultados salieron las mismas veces. ¿Cómo se llama eso?", "Empate", "Comparten la misma frecuencia."),
            ex("¿Por qué hay que escribir cada resultado junto a su frecuencia al ordenar?", "Para no mezclar los datos", "Cada frecuencia pertenece a un resultado."),
        ],
        "apply": [
            ex("Frecuencias: 1 → 4, 2 → 1, 3 → 3, 4 → 3, 5 → 5, 6 → 4. ¿Qué resultado salió más veces?", "El 5", "Tiene la frecuencia mayor, 5."),
            ex("Frecuencias: 1 → 4, 2 → 1, 3 → 3, 4 → 3, 5 → 5, 6 → 4. Ordena las frecuencias de menor a mayor.", "1, 3, 3, 4, 4, 5", "Se ordenan los números 4, 1, 3, 3, 5 y 4."),
            ex("Frecuencias: 1 → 4, 2 → 1, 3 → 3, 4 → 3, 5 → 5, 6 → 4. ¿Qué dos resultados empatan con 3 veces?", "El 3 y el 4", "Los dos tienen frecuencia 3."),
        ],
        "reason": [
            ex("Ana ordenó las frecuencias 2, 2, 3, 3, 5 pero ya no sabe qué resultado tenía cada una. ¿Qué error cometió?", "Separó la frecuencia de su resultado", "Hay que anotar los pares resultado y frecuencia."),
            ex("Pedro dice que el resultado más alto del dado es el que más veces salió. ¿Es correcto?", "No; la frecuencia no depende de cuán alto es el número", "El 6 puede salir pocas veces."),
        ],
        "challenge": [
            ex("Frecuencias de un dado: " + ", ".join(f"{i} → {DC[i]}" for i in range(1, 7)) + ". Ordena los resultados de menos a más veces. Si hay empate, escribe los resultados juntos.", "El 2 y el 4; luego el 1 y el 6; luego el 5; al final el 3", "Las frecuencias de menor a mayor son 2, 2, 3, 3, 4 y 6."),
            arith("Frecuencias de un dado: " + ", ".join(f"{i} → {DC[i]}" for i in range(1, 7)) + ". ¿Cuántas veces más salió el resultado más frecuente que el menos frecuente?", f"{max(DC.values())}-{min(DC.values())}", "Se resta la frecuencia menor a la mayor."),
        ],
    },
    context=[ex("En un juego se anotó: 1 → 3 veces, 2 → 5 veces, 3 → 4 veces. ¿Cuál resultado fue el más frecuente?", "El 2", "Tiene la frecuencia mayor, 5.")],
    selfcheck=[
        ex("Ordena de menor a mayor: 6, 2, 9.", "2, 6, 9", "El 2 es el menor y el 9 el mayor."),
        ex("Frecuencias: 1 → 4, 2 → 1, 3 → 2. ¿Cuál tiene la frecuencia menor?", "El 2", "Tiene frecuencia 1."),
        ex("¿Qué se hace si dos resultados tienen la misma frecuencia?", "Se dice que empatan y se escriben juntos", "Comparten el mismo lugar en el orden."),
    ],
    open_task=task(
        "Con estas frecuencias de un dado: 1 → 4, 2 → 2, 3 → 5, 4 → 3, 5 → 3, 6 → 3 (20 lanzamientos), ordena los resultados de menos a más veces y escribe cuál salió más. Anota los pares resultado y frecuencia.",
        "De menos a más: 2 (2 veces), luego 4, 5 y 6 (3 veces cada uno), luego 1 (4 veces) y por último 3 (5 veces). El 3 salió más.",
        ["escribe pares resultado y frecuencia", "ordena de menor a mayor", "indica el empate", "responde cuál salió más"],
        ["lista ordenada", "respuesta final"],
        ["perder el resultado de cada frecuencia", "no ver el empate"],
        "Pide subrayar el empate. Reconoce que mantenga los pares.",
    ),
    reinforce="Escribe las frecuencias de tres resultados inventados y ordénalas de menor a mayor.",
    extend="Con las frecuencias 1 → 5, 2 → 2, 3 → 4, 4 → 4, 5 → 3, 6 → 2 (20 lanzamientos), ordena los resultados del que salió menos al que salió más.",
)

register(
    OA24, 3,
    materials="Lápiz y papel. Los datos están escritos en los ejercicios.",
    use="Aprenderé a encontrar el menor y el mayor de los datos y a estimar el punto medio entre ambos. Sirve para ver la mitad del recorrido de los resultados.",
    prior=["Sé ordenar los resultados.", "Sé calcular la mitad de un número par."],
    explain=[
        "En una lista de resultados, el menor es el número más chico que salió y el mayor es el número más grande que salió. Si ordenas los resultados, el menor queda primero y el mayor queda al final.",
        "El punto medio es un número que queda a la mitad entre el menor y el mayor. Para estimarlo, suma el menor y el mayor y calcula la mitad. Si el menor es 2 y el mayor es 6, la suma es 8 y la mitad es 4. El punto medio es 4.",
        "A veces la mitad no es un número entero. Si el menor es 1 y el mayor es 6, la suma es 7 y la mitad está entre 3 y 4. Entonces decimos que el punto medio está más o menos entre 3 y 4.",
    ],
    vocab=[("menor", "el número más chico de los datos"), ("mayor", "el número más grande de los datos"), ("punto medio", "número que queda a la mitad entre el menor y el mayor"), ("estimar", "decir un valor aproximado"), ("recorrido", "distancia desde el menor al mayor")],
    worked=[
        {"title": "Menor, mayor y punto medio", "problem": f"Resultados de un dado: {lista(DADO2)}. Encuentra el menor, el mayor y el punto medio.", "steps": [f"Ordeno los datos: {lista(sorted(DADO2))}.", "El menor es 2 y el mayor es 6.", "2 + 6 = 8 y la mitad de 8 es 4."], "answer": "Menor 2, mayor 6 y punto medio 4"},
        {"title": "Punto medio entre dos números impares", "problem": "El menor es 1 y el mayor es 6. ¿Dónde está el punto medio?", "steps": ["1 + 6 = 7.", "La mitad de 7 está entre 3 y 4."], "answer": "Más o menos entre 3 y 4"},
    ],
    mistakes=[
        {"wrong": "Decir que el menor es el primer dato de la lista.", "why": "No se ordenan los datos ni se comparan todos.", "fix": "Revisa todos los datos o ordénalos primero."},
        {"wrong": "Decir que el punto medio entre 2 y 6 es 8.", "why": "Se queda con la suma y no calcula la mitad.", "fix": "Suma y luego divide por 2: la mitad de 8 es 4."},
    ],
    tiers={
        "recovery": [
            ex("Datos: 4, 2, 6. ¿Cuál es el menor?", "2", "Es el número más chico."),
            ex("Datos: 4, 2, 6. ¿Cuál es el mayor?", "6", "Es el número más grande."),
            ex("Datos: 3, 5, 1, 4. ¿Cuál es el mayor?", "5", "Es el número más grande."),
        ],
        "understand": [
            ex(f"Resultados de un dado: {lista(DADO2)}. ¿Cuál es el menor?", "2", "Ningún dato es más chico que 2."),
            ex(f"Resultados de un dado: {lista(DADO2)}. ¿Cuál es el mayor?", "6", "Ningún dato es más grande que 6."),
            ex("¿Cuál es el punto medio entre 2 y 8?", "5", "2 + 8 = 10 y la mitad de 10 es 5.", calc="(2+8)//2"),
        ],
        "apply": [
            ex("Los datos son 1, 3, 5. ¿Cuál es el punto medio entre el menor y el mayor?", "3", "1 + 5 = 6 y la mitad de 6 es 3.", calc="(1+5)//2"),
            ex("El menor es 4 y el mayor es 10. ¿Cuál es el punto medio?", "7", "4 + 10 = 14 y la mitad de 14 es 7.", calc="(4+10)//2"),
            ex("El menor de los datos es 2 y el mayor es 9. ¿Entre cuáles números está el punto medio?", "Entre 5 y 6", "2 + 9 = 11 y la mitad de 11 está entre 5 y 6."),
        ],
        "reason": [
            ex("Rosa dice que el punto medio entre 2 y 6 es 8. ¿Qué error comete?", "Sólo sumó; falta calcular la mitad, que es 4", "La mitad de 8 es 4."),
            ex("Luis dice que el menor de 5, 2, 6, 3 es el 5 porque es el primero. ¿Es correcto?", "No; el menor es el 2", "Hay que comparar todos los datos."),
        ],
        "challenge": [
            ex("Los resultados fueron 3, 7, 4 y 9. ¿Cuál es el menor, cuál el mayor y cuál el punto medio?", "Menor 3, mayor 9 y punto medio 6", "3 + 9 = 12 y la mitad de 12 es 6.", calc="(3+9)//2"),
            ex("El punto medio de dos datos es 5 y el menor es 2. ¿Cuál es el mayor?", "8", "De 2 a 5 hay 3, así que de 5 hay otros 3 más hasta 8.", calc="5+3"),
        ],
    },
    context=[ex("Se lanzó un dado y salieron los resultados 5, 2, 6, 3, 2 y 4. ¿Cuál es el menor y cuál el mayor?", "Menor 2 y mayor 6", "Son el número más chico y el más grande de la lista.")],
    selfcheck=[
        ex("Datos: 8, 3, 5. ¿Cuál es el menor?", "3", "Es el más chico."),
        ex("¿Cuál es el punto medio entre 4 y 8?", "6", "4 + 8 = 12 y la mitad es 6.", calc="(4+8)//2"),
        ex("¿Qué resultado es el mayor: 5, 9 o 7?", "9", "Es el más grande."),
    ],
    open_task=task(
        f"Con los resultados de un dado {lista(DADO2)}, ordénalos de menor a mayor. Escribe el menor, el mayor y el punto medio, y explica cómo lo calculaste.",
        f"Ordenados: {lista(sorted(DADO2))}. Menor 2, mayor 6. 2 + 6 = 8 y la mitad de 8 es 4: el punto medio es 4.",
        ["ordena los 15 datos", "identifica el menor y el mayor", "suma y calcula la mitad", "explica los pasos"],
        ["lista ordenada", "tres valores", "cálculo escrito"],
        ["olvidar la mitad", "usar el primer dato de la lista como menor"],
        "Pide marcar el menor y el mayor en la lista ordenada. Reconoce el cálculo de la mitad.",
    ),
    reinforce="Elige cinco números del 1 al 10 y encuentra el menor, el mayor y el punto medio.",
    extend="Busca dos números con punto medio 10 y escribe cómo lo comprobaste.",
)

register(
    OA24, 4,
    materials="Lápiz y papel. Los dos registros de monedas están escritos en los ejercicios.",
    use="Aprenderé a comparar dos experimentos de azar y a entender que un resultado anterior no asegura el siguiente. Sirve para no equivocarse con los juegos de suerte.",
    prior=["Sé registrar y contar resultados.", "Sé comparar números hasta 100."],
    explain=[
        "Dos experimentos de azar pueden dar resultados distintos aunque se hagan igual. Si Ana y Beto lanzan una moneda 20 veces cada uno, puede que a Ana le salgan 12 caras y a Beto 9. Se comparan las frecuencias de cada uno.",
        "El azar no recuerda. Si una moneda salió cara cuatro veces seguidas, la próxima vez puede salir cara o sello. Los resultados anteriores no aseguran el siguiente.",
        "Para comparar dos experimentos, haz una tabla con las frecuencias de cada uno, revisa que los totales sean iguales y luego di en qué se parecen y en qué se diferencian. Con los mismos lanzamientos, las diferencias se calculan restando.",
    ],
    vocab=[("experimento", "juego que se repite varias veces y se registra"), ("comparar", "decir en qué se parecen y se diferencian"), ("diferencia", "resultado de restar dos frecuencias"), ("asegurado", "que ocurre con certeza"), ("posible", "que puede ocurrir")],
    worked=[
        {"title": "Comparar dos registros", "problem": f"Ana lanzó una moneda 20 veces: {MA['cara']} caras y {MA['sello']} sellos. Beto lanzó 20 veces: {MB['cara']} caras y {MB['sello']} sellos. ¿Quién obtuvo más caras y cuántas más?", "steps": [f"Ana: {MA['cara']} caras. Beto: {MB['cara']} caras.", f"{max(MA['cara'], MB['cara'])} − {min(MA['cara'], MB['cara'])} = {abs(MA['cara'] - MB['cara'])}."], "answer": f"{'Ana' if MA['cara'] > MB['cara'] else 'Beto'} obtuvo {abs(MA['cara'] - MB['cara'])} caras más"},
        {"title": "El azar no asegura el siguiente resultado", "problem": "Una moneda salió cara 4 veces seguidas. ¿Se puede asegurar que ahora saldrá sello?", "steps": ["Cada lanzamiento es nuevo.", "Los resultados anteriores no cambian lo que puede salir."], "answer": "No; puede salir cara o sello"},
    ],
    mistakes=[
        {"wrong": "Pensar que después de varias caras seguidas «tiene que» salir sello.", "why": "Se cree que el azar corrige lo anterior.", "fix": "Cada lanzamiento es nuevo y los dos resultados son posibles."},
        {"wrong": "Comparar experimentos con distinta cantidad de lanzamientos sin decirlo.", "why": "Los totales no son iguales.", "fix": "Revisa primero que los dos experimentos tengan los mismos lanzamientos."},
    ],
    tiers={
        "recovery": [
            ex(f"Ana lanzó una moneda 20 veces: {MA['cara']} caras y {MA['sello']} sellos. ¿Cuántos sellos obtuvo?", str(MA["sello"]), "Se lee el dato de sellos."),
            ex(f"Beto lanzó una moneda 20 veces: {MB['cara']} caras y {MB['sello']} sellos. ¿Cuántas caras obtuvo?", str(MB["cara"]), "Se lee el dato de caras."),
            ex("Una moneda salió cara 3 veces seguidas. ¿Qué resultados son posibles en el siguiente lanzamiento?", "Cara o sello", "Los dos pueden salir."),
        ],
        "understand": [
            ex("Una moneda salió cara 4 veces seguidas. ¿Está asegurado que ahora sale sello?", "No", "Cada lanzamiento es nuevo."),
            ex(f"Ana: {MA['cara']} caras. Beto: {MB['cara']} caras. ¿Quién obtuvo menos caras?", "Beto", f"{MB['cara']} es menor que {MA['cara']}."),
            ex("¿Qué debes revisar antes de comparar dos experimentos?", "Que tengan la misma cantidad de lanzamientos", "Si no, la comparación no es justa."),
        ],
        "apply": [
            arith(f"Ana lanzó 20 veces: {MA['cara']} caras. ¿Cuántos sellos obtuvo?", f"20-{MA['cara']}", "Los lanzamientos que no son caras son sellos."),
            arith(f"Beto lanzó 20 veces: {MB['cara']} caras. ¿Cuántos sellos obtuvo?", f"20-{MB['cara']}", "Los lanzamientos que no son caras son sellos."),
            arith(f"Ana: {MA['sello']} sellos. Beto: {MB['sello']} sellos. ¿Cuántos sellos obtuvieron entre los dos?", f"{MA['sello']}+{MB['sello']}", "Se suman los sellos de los dos."),
        ],
        "reason": [
            ex("Tomás dice: «salió sello 5 veces seguidas, así que en el próximo lanzamiento seguro sale cara». ¿Tiene razón?", "No; puede salir cara o sello", "El resultado anterior no asegura el siguiente."),
            ex("Dos amigos lanzan una moneda 20 veces cada uno. Uno obtiene 12 caras y el otro 9. ¿Alguno hizo trampa?", "No; en el azar es normal que salgan resultados distintos", "El azar no da siempre el mismo resultado."),
        ],
        "challenge": [
            ex(f"Ana: {MA['cara']} caras y {MA['sello']} sellos. Beto: {MB['cara']} caras y {MB['sello']} sellos. ¿Quién tuvo más sellos y cuántos más?", f"{'Ana' if MA['sello'] > MB['sello'] else 'Beto'}; {abs(MA['sello'] - MB['sello'])} más", f"{max(MA['sello'], MB['sello'])} − {min(MA['sello'], MB['sello'])} = {abs(MA['sello'] - MB['sello'])}."),
            ex("Dos experimentos de 20 lanzamientos tienen frecuencias que suman 20 y 18. ¿Cuál tiene un error?", "El que suma 18", "Debe sumar 20 como los lanzamientos."),
        ],
    },
    context=[ex("Para decidir quién empieza un juego, Pía lanza una moneda. Salió cara 4 veces seguidas. Mía dice: «ahora seguro sale sello». ¿Qué le responderías?", "Que no está asegurado, puede salir cara o sello", "El azar no corrige lo que salió antes.")],
    selfcheck=[
        ex("¿Los resultados anteriores aseguran el siguiente lanzamiento de una moneda?", "No", "Cada lanzamiento es nuevo."),
        ex("Dos experimentos tienen 20 lanzamientos cada uno. ¿La comparación es justa?", "Sí", "Tienen la misma cantidad de lanzamientos."),
        ex("Si Ana tuvo 11 caras y Beto 8, ¿cuántas más tuvo Ana?", "3", "11 − 8 = 3.", calc="11-8"),
    ],
    open_task=task(
        f"Compara estos dos registros de 20 lanzamientos de una moneda. Ana: {lista(MONEDA_A)}. Beto: {lista(MONEDA_B)}. Cuenta caras y sellos de cada uno, escribe quién tuvo más caras y cuántas más, y explica si un resultado anterior asegura el siguiente.",
        f"Ana: {MA['cara']} caras y {MA['sello']} sellos. Beto: {MB['cara']} caras y {MB['sello']} sellos. Ana tuvo {abs(MA['cara'] - MB['cara'])} caras {'más' if MA['cara'] > MB['cara'] else 'menos'} que Beto. El resultado anterior no asegura el siguiente porque cada lanzamiento es nuevo.",
        ["cuenta caras y sellos de cada uno", "comprueba que cada total es 20", "resta para comparar", "explica que el azar no está asegurado"],
        ["dos tablas de frecuencias", "resta escrita", "explicación"],
        ["perder lanzamientos al contar", "creer que el siguiente resultado se puede asegurar"],
        "Pide revisar que cada total sea 20. Reconoce la explicación sobre el azar.",
    ),
    reinforce="Lanza una moneda 10 veces y anota cuántas caras y sellos salieron. Compáralo con alguien de tu casa.",
    extend="Explica con tus palabras por qué, aunque salga cara varias veces seguidas, el siguiente lanzamiento puede ser cara o sello.",
)
