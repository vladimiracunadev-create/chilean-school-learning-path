"""Student material for 4.º básico Matemática, OA 26 (experimentos aleatorios, tablas y gráficos)."""
from __future__ import annotations

from collections import Counter

from student_lessons import arith, ex, register

OA26 = "MA04 OA 26"

MONEDA = ["cara", "sello", "cara", "cara", "sello", "sello", "cara", "sello", "cara", "cara", "sello", "cara", "sello", "sello", "cara", "cara", "sello", "cara", "sello", "cara"]
DADO = [3, 5, 1, 6, 3, 2, 3, 6, 4, 3, 5, 6]
RULETA = ["rojo", "azul", "azul", "verde", "rojo", "amarillo", "azul", "rojo", "azul", "verde"]
M = Counter(MONEDA)
D = Counter(DADO)
R = Counter(RULETA)
assert (M["cara"], M["sello"], len(MONEDA)) == (11, 9, 20)
assert (D[1], D[2], D[3], D[4], D[5], D[6], len(DADO)) == (1, 1, 4, 1, 2, 3, 12)
assert (R["rojo"], R["azul"], R["verde"], R["amarillo"], len(RULETA)) == (3, 4, 2, 1, 10)
LMONEDA = ", ".join(MONEDA)
LDADO = ", ".join(str(x) for x in DADO)
LRULETA = ", ".join(RULETA)


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA26, 1,
    materials="Una moneda y un dado, si tienes, para jugar sobre una mesa (guárdalos después). Si no, todo está descrito en los ejercicios.",
    use="Aprenderé a decir cuáles son todos los resultados posibles de un juego de azar. Sirve para anotar bien lo que ocurre en cada prueba.",
    prior=["Sé hacer una tabla de conteo.", "Sé leer un gráfico de barras sencillo."],
    explain=[
        "Un experimento aleatorio es una prueba en que no sabes con seguridad qué va a salir. Lanzar una moneda, lanzar un dado o girar una ruleta son experimentos aleatorios. Cada vez que lo haces, se llama un ensayo.",
        "Los resultados posibles son todo lo que puede salir en un ensayo. En una moneda hay dos resultados: cara o sello. En un dado hay seis: 1, 2, 3, 4, 5 y 6. En una ruleta de cuatro colores hay cuatro resultados, uno por cada color.",
        "Antes de empezar, escribe la lista de resultados posibles. No pongas dos veces el mismo ni dejes uno afuera. Una frase como «sale un número par» no es un resultado, porque agrupa varios: 2, 4 y 6.",
    ],
    vocab=[("azar", "cuando no se puede saber con seguridad qué va a ocurrir"), ("ensayo", "cada vez que se hace el experimento"), ("resultado", "lo que sale en un ensayo"), ("resultados posibles", "lista de todo lo que puede salir")],
    worked=[
        {"title": "Resultados de una moneda", "problem": "Lanzas una moneda una vez. ¿Cuáles son los resultados posibles?", "steps": ["Una moneda tiene dos lados.", "Un lado se llama cara y el otro sello."], "answer": "Cara y sello"},
        {"title": "Resultados de un dado", "problem": "Lanzas un dado de 6 caras. ¿Cuántos resultados posibles hay y cuáles son?", "steps": ["Cada cara tiene un número del 1 al 6.", "Los resultados son 1, 2, 3, 4, 5 y 6."], "answer": "6 resultados: 1, 2, 3, 4, 5 y 6"},
    ],
    mistakes=[
        {"wrong": "Decir que un dado tiene 3 resultados: 1, 2 y 3.", "why": "Se escribe una parte y se olvidan las otras caras.", "fix": "Un dado tiene 6 caras: 1, 2, 3, 4, 5 y 6."},
        {"wrong": "Contar «sale un número par» como un resultado.", "why": "Agrupa varios resultados distintos.", "fix": "Los resultados son 2, 4 y 6; «par» agrupa varios."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos resultados posibles tiene lanzar una moneda?", "2", "Cara y sello."),
            ex("¿Cuántos resultados posibles tiene lanzar un dado de 6 caras?", "6", "Los números del 1 al 6."),
            ex("Cada vez que haces el experimento, ¿cómo se llama?", "Un ensayo", "Un ensayo es cada repetición."),
        ],
        "understand": [
            ex("Una ruleta tiene 4 sectores iguales: rojo, azul, verde y amarillo. ¿Cuántos resultados posibles hay?", "4", "Hay uno por cada color."),
            ex("¿«Sale un número par» es un resultado posible de un dado o agrupa varios resultados?", "Agrupa varios resultados", "Par incluye 2, 4 y 6."),
            ex("Una bolsa tiene 2 bolitas rojas y 1 bolita azul. Sacas una sin mirar. ¿Cuáles son los colores posibles?", "Rojo y azul", "Son los colores que hay en la bolsa."),
        ],
        "apply": [
            ex("Giras una ruleta con los números 1, 2, 3, 4 y 5 en sectores. ¿Cuántos resultados posibles hay?", "5", "Hay un resultado por cada número."),
            ex("Lanzas una moneda dos veces seguidas. ¿Cuáles son los resultados posibles del primer lanzamiento?", "Cara y sello", "En cada lanzamiento hay dos resultados."),
            ex("Sacas una carta de una baraja de 4 cartas rojas, 3 azules y 1 verde. ¿Cuántos colores posibles hay?", "3", "Hay rojo, azul y verde."),
        ],
        "reason": [
            ex("Teo dice que en un dado el resultado «7» es posible. ¿Tiene razón?", "No; el dado solo tiene 1, 2, 3, 4, 5 y 6", "No hay cara con 7."),
            ex("Ana anota como resultados de la moneda: cara, sello y borde. ¿Es correcta su lista para un lanzamiento normal?", "No; solo cara y sello", "Normalmente no cae de canto."),
        ],
        "challenge": [
            ex("Un dado de 6 caras: ¿cuántos resultados posibles son números mayores que 4?", "2", "Son el 5 y el 6.", calc="2"),
            ex("En una ruleta con los colores rojo, azul y verde, ¿cuántos resultados posibles tienen un color que no es verde?", "2", "Son rojo y azul.", calc="2"),
        ],
    },
    context=[ex("Para un juego de mesa, un jugador lanza un dado y gira una ruleta de 3 colores. ¿Cuántos resultados posibles tiene el dado y cuántos la ruleta?", "6 y 3", "El dado tiene 6 y la ruleta 3.")],
    selfcheck=[
        ex("¿Cuáles son los resultados posibles de una moneda?", "Cara y sello", "Son los dos lados."),
        ex("¿Cuál es el mayor resultado posible de un dado de 6 caras?", "6", "Es la cara con más puntos."),
        ex("¿Qué es un ensayo?", "Cada vez que se hace el experimento", "Es una repetición."),
    ],
    open_task=task(
        "Elige un experimento: lanzar una moneda, lanzar un dado de 6 caras o girar una ruleta de 4 colores. Escribe la lista de resultados posibles y el número de ellos. Si tienes el objeto, haz 5 ensayos y anota qué sale cada vez.",
        "Moneda: resultados posibles cara y sello; son 2. En 5 ensayos salió: cara, sello, sello, cara, cara.",
        ["elige un experimento de la lista", "escribe todos los resultados posibles", "indica cuántos son", "anota los 5 ensayos si tiene el objeto"],
        ["lista de resultados", "número de resultados"],
        ["omitir un resultado", "repetir un resultado"],
        "Pide revisar que no falte ningún resultado. Reconoce que anote lo que sale sin cambiarlo.",
    ),
    reinforce="Elige un juego de azar que conozcas y escribe todos los resultados que puede dar.",
    extend="Explica por qué «sale un número menor que 3» agrupa más de un resultado en un dado de 6 caras.",
)

register(
    OA26, 2,
    materials="Lápiz y papel. Las listas de resultados están escritas en los ejercicios; si tienes moneda o dado, puedes repetir el experimento.",
    use="Aprenderé a registrar los ensayos de un experimento sin olvidar ninguno. Sirve para tener datos confiables.",
    prior=["Sé cuáles son los resultados posibles.", "Sé contar con marcas."],
    explain=[
        "Al repetir un experimento muchas veces, se anota cada resultado a medida que sale. Una buena forma es hacer una tabla con una fila para cada resultado posible y poner una marca cada vez que sale.",
        "Para no omitir ensayos, numera cada uno: ensayo 1, ensayo 2, ensayo 3. Al final, suma las marcas de todos los resultados. Esa suma debe ser igual al número de ensayos. Si hiciste 20 ensayos y sumaste 19, falta uno.",
        "La frecuencia de un resultado es cuántas veces salió. Por ejemplo, si en 20 lanzamientos de una moneda salió cara 11 veces, la frecuencia de cara es 11 y la de sello es 9, porque 20 − 11 = 9.",
    ],
    vocab=[("frecuencia", "cantidad de veces que salió un resultado"), ("marca de conteo", "rayita que se anota cada vez que sale un resultado"), ("registro", "anotación ordenada de lo que ocurre"), ("omitir", "dejar algo sin anotar")],
    worked=[
        {"title": "Contar caras y sellos", "problem": "En 20 lanzamientos de una moneda salió: " + LMONEDA + ". ¿Cuál es la frecuencia de cara y de sello?", "steps": ["Recorro la lista una vez contando cada resultado.", f"Cara: {M['cara']} veces; sello: {M['sello']} veces."], "answer": f"Cara {M['cara']} y sello {M['sello']}"},
        {"title": "Comprobar que no falta ningún ensayo", "problem": f"Cara {M['cara']} más sello {M['sello']}, ¿suman los 20 ensayos?", "steps": [f"{M['cara']} + {M['sello']} = 20.", "La suma coincide con el número de ensayos."], "answer": "Sí, no se omitió ningún ensayo"},
    ],
    mistakes=[
        {"wrong": "Anotar solo los resultados que llaman la atención.", "why": "Se omiten ensayos y los datos quedan incompletos.", "fix": "Anota todos los ensayos en orden."},
        {"wrong": "No comprobar que la suma de las frecuencias sea el número de ensayos.", "why": "Se pueden olvidar marcas.", "fix": "Suma las frecuencias y compara con el total."},
    ],
    tiers={
        "recovery": [
            ex("Si haces 10 ensayos, ¿cuánto deben sumar las frecuencias de todos los resultados?", "10", "Cada ensayo da un resultado."),
            ex("En una moneda: sello salió 3 veces en 5 ensayos. ¿Cuántas veces salió cara?", "2", "5 − 3 = 2.", calc="5-3"),
            ex("¿Qué es la frecuencia de un resultado?", "Cuántas veces salió", "Es la cantidad de veces."),
        ],
        "understand": [
            ex("Resultados de 6 lanzamientos de moneda: cara, sello, cara, cara, sello, cara. ¿Cuál es la frecuencia de cara?", "4", "Cara aparece en los lugares 1, 3, 4 y 6."),
            ex("En un registro, 7 + 6 + 4 = 17 pero se hicieron 18 ensayos. ¿Qué indica?", "Que falta anotar un ensayo", "La suma debe ser 18."),
            ex("¿Para qué se numeran los ensayos?", "Para no omitir ninguno", "Así se ve si falta alguno."),
        ],
        "apply": [
            ex("Resultados de una ruleta en 10 giros: " + LRULETA + ". ¿Cuántas veces salió azul?", str(R["azul"]), "Se cuentan los azules de la lista."),
            ex("En esa misma lista de 10 giros (" + LRULETA + "), ¿cuántas veces salió rojo?", str(R["rojo"]), "Se cuentan los rojos de la lista."),
            ex("En esa lista de 10 giros (" + LRULETA + "), ¿qué color salió una sola vez?", "Amarillo", "Amarillo aparece solo en el ensayo 6."),
        ],
        "reason": [
            ex("Pía hizo 15 lanzamientos y sumó 14 en su tabla. ¿Qué debe hacer?", "Revisar la lista para encontrar el ensayo que falta", "La suma debe ser igual al total."),
            ex("Luis dice que no necesita anotar los resultados que no le gustan. ¿Qué problema trae eso?", "Los datos quedan incompletos y engañosos", "Se omiten ensayos."),
        ],
        "challenge": [
            ex("Un dado se lanzó 12 veces y salió: " + LDADO + ". ¿Cuántas veces salió el 3?", str(D[3]), "Se cuentan los 3 de la lista."),
            ex("En esos mismos 12 lanzamientos (" + LDADO + "), ¿cuántas veces salió un número mayor que 4?", str(D[5] + D[6]), "Cuentan los 5 y los 6.", calc="2+3"),
        ],
    },
    context=[ex("En una feria se gira una ruleta 20 veces. Salió azul 8 veces, rojo 7 veces y verde el resto. ¿Cuántas veces salió verde?", "5", "20 − 8 − 7 = 5.", calc="20-8-7")],
    selfcheck=[
        ex("En 8 ensayos con moneda salió cara 5 veces. ¿Cuántas veces salió sello?", "3", "8 − 5 = 3.", calc="8-5"),
        ex("¿Qué suma deben dar todas las frecuencias en un registro completo?", "El número de ensayos", "Cada ensayo da un resultado."),
        ex("¿Se pueden anotar solo los resultados que sorprenden?", "No", "Todos los ensayos deben quedar anotados."),
    ],
    open_task=task(
        "Si tienes una moneda, lánzala 20 veces y anota cada resultado en una lista numerada. Si no la tienes, usa esta lista de 10 giros de ruleta: " + LRULETA + ". Haz una tabla de conteo con todos los resultados posibles y comprueba que la suma de frecuencias dé el número de ensayos.",
        "Ruleta 10 giros: rojo 3, azul 4, verde 2, amarillo 1. Total 10.",
        ["numera los ensayos", "cuenta cada resultado posible", "comprueba que la suma sea el total", "no omite ningún resultado"],
        ["lista numerada o lista dada", "tabla de conteo", "comprobación de la suma"],
        ["omitir ensayos", "no comprobar el total"],
        "Pide mostrar la suma de frecuencias. Reconoce que revise antes de entregar.",
    ),
    reinforce="Lanza una moneda 10 veces y anota cada resultado en una lista numerada. Cuenta caras y sellos.",
    extend="Explica por qué es útil numerar los ensayos al registrar un experimento.",
)

register(
    OA26, 3,
    materials="Papel cuadriculado para el gráfico, o lápiz y papel. Las frecuencias están escritas en los ejercicios.",
    use="Aprenderé a hacer una tabla y un gráfico de barras con los resultados de un experimento. Sirve para ver de un vistazo qué resultado salió más veces.",
    prior=["Sé contar frecuencias.", "Sé qué son el eje y la escala."],
    explain=[
        "Para presentar los resultados de un experimento, haz una tabla con dos columnas: resultado y frecuencia. Después, dibuja un gráfico de barras: en el eje horizontal van los resultados y en el vertical una escala de números.",
        "La altura de cada barra es la frecuencia de ese resultado. Si en 12 lanzamientos de dado el 3 salió 4 veces, la barra del 3 llega hasta 4. Usa una escala igual para todas las barras, con marcas a igual distancia, y partiendo de 0.",
        "Pon un título que diga qué experimento es, como «Resultados de 12 lanzamientos de un dado», y nombre a los ejes. Si usas un software educativo, puedes escribir los datos y el programa dibuja las barras; igual debes revisar que las alturas coincidan con la tabla.",
    ],
    vocab=[("tabla de frecuencias", "tabla con cada resultado y las veces que salió"), ("gráfico de barras", "gráfico con barras cuya altura es la frecuencia"), ("eje", "línea del gráfico con los nombres o la escala"), ("software educativo", "programa para aprender y para dibujar gráficos")],
    worked=[
        {"title": "Armar la tabla", "problem": "En 12 lanzamientos de un dado salió: " + LDADO + ". Escribe la tabla de frecuencias.", "steps": ["Cuento cada número del 1 al 6.", f"1: {D[1]}, 2: {D[2]}, 3: {D[3]}, 4: {D[4]}, 5: {D[5]}, 6: {D[6]}."], "answer": f"1: {D[1]}, 2: {D[2]}, 3: {D[3]}, 4: {D[4]}, 5: {D[5]}, 6: {D[6]} (suman 12)"},
        {"title": "Leer la barra más alta", "problem": "En ese gráfico, ¿qué barra es la más alta?", "steps": [f"Comparo las frecuencias: la mayor es {D[3]}.", "Corresponde al número 3."], "answer": f"La barra del 3, que llega hasta {D[3]}"},
    ],
    mistakes=[
        {"wrong": "Dibujar las barras sin que su altura coincida con la tabla.", "why": "No se revisa el dibujo con los datos.", "fix": "Compara cada barra con su frecuencia."},
        {"wrong": "Empezar la escala en un número distinto de 0 y marcar espacios desiguales.", "why": "Las barras parecen más grandes o más chicas de lo que son.", "fix": "Empieza la escala en 0 y usa marcas a igual distancia."},
    ],
    tiers={
        "recovery": [
            ex("En una tabla de frecuencias, ¿qué dice la columna de frecuencia?", "Cuántas veces salió cada resultado", "Es el conteo de cada uno."),
            ex("En un gráfico de barras de un experimento, ¿qué indica la altura de una barra?", "La frecuencia", "La barra más alta salió más veces."),
            ex("¿Desde qué número debe empezar la escala del eje vertical?", "Desde 0", "Así las alturas son comparables."),
        ],
        "understand": [
            ex("Tabla de 12 lanzamientos de dado: 1→" + str(D[1]) + ", 2→" + str(D[2]) + ", 3→" + str(D[3]) + ", 4→" + str(D[4]) + ", 5→" + str(D[5]) + ", 6→" + str(D[6]) + ". ¿Cuántos ensayos suman?", "12", "Las frecuencias suman 12.", calc="1+1+4+1+2+3"),
            ex("En esa tabla, ¿qué resultado tiene la barra más alta?", "El 3", f"El 3 tiene la mayor frecuencia: {D[3]}."),
            ex("En esa tabla, ¿hasta qué número llega la barra del 6?", str(D[6]), "La altura es la frecuencia del 6."),
        ],
        "apply": [
            ex("Ruleta, 10 giros: rojo " + str(R["rojo"]) + ", azul " + str(R["azul"]) + ", verde " + str(R["verde"]) + ", amarillo " + str(R["amarillo"]) + ". ¿Qué color tiene la barra más alta?", "Azul", f"Azul tiene {R['azul']}, la mayor frecuencia."),
            ex("En esa misma ruleta (rojo " + str(R["rojo"]) + ", azul " + str(R["azul"]) + ", verde " + str(R["verde"]) + ", amarillo " + str(R["amarillo"]) + "), ¿cuántas unidades más alta es la barra de azul que la de verde?", str(R["azul"] - R["verde"]), "Se resta la frecuencia menor a la mayor.", calc="4-2"),
            ex("En un gráfico con escala de 1 en 1, la barra de amarillo llega a 1. ¿Cuántas veces salió amarillo?", "1", "La altura de la barra es la frecuencia."),
        ],
        "reason": [
            ex("Bea dibuja la barra del 6 más alta que la del 3 aunque en la tabla el 3 salió más veces. ¿Qué error hay?", "La altura no coincide con la frecuencia", "La barra del 3 debe ser la más alta."),
            ex("Un gráfico con escala que empieza en 3, ¿por qué puede confundir?", "Porque las barras parecen más diferentes de lo que son", "No parte de 0."),
        ],
        "challenge": [
            ex("Moneda, 20 lanzamientos: cara " + str(M["cara"]) + ", sello " + str(M["sello"]) + ". ¿Qué barra es más alta y por cuántas unidades?", f"Cara, por {M['cara'] - M['sello']}", "Se resta 11 − 9.", calc="11-9"),
            ex("Tabla: A 5, B 3, C 4, D 1. ¿Cuántas veces se hizo el experimento?", "13", "5 + 3 + 4 + 1 = 13.", calc="5+3+4+1"),
        ],
    },
    context=[ex("Un grupo gira una ruleta de 4 colores 20 veces. Hace la tabla: rojo 6, azul 5, verde 5, amarillo 4. ¿Qué barra es la más alta y cuántas veces salió?", "Rojo, 6 veces", "La mayor frecuencia es 6.")],
    selfcheck=[
        ex("En un gráfico de barras de frecuencias, ¿dónde van los resultados: en el eje horizontal o en el vertical?", "En el horizontal", "En el vertical va la escala de frecuencias."),
        ex("Una barra llega a 7. ¿Cuál es la frecuencia?", "7", "La altura es la frecuencia."),
        ex("¿Qué debe llevar un buen gráfico además de las barras?", "Título y nombres de los ejes", "Para saber qué muestra."),
    ],
    open_task=task(
        "Usa los 20 lanzamientos de moneda de esta clase: " + LMONEDA + ". Haz la tabla de frecuencias de cara y sello y dibuja un gráfico de barras con título, escala partiendo de 0 y nombres de ejes. Si tienes un software educativo, pide a un adulto que te ayude a repetirlo.",
        f"Cara {M['cara']}, sello {M['sello']}. La barra de cara llega a {M['cara']} y la de sello a {M['sello']}.",
        ["tabla con las dos frecuencias", "la suma es 20", "gráfico con título y ejes", "escala desde 0 y barras que coinciden"],
        ["tabla", "gráfico"],
        ["barras que no coinciden con la tabla", "escala sin 0"],
        "Pide comparar cada barra con la tabla. Reconoce título y ejes.",
    ),
    reinforce="Haz un gráfico de barras con los 10 giros de ruleta de la clase anterior.",
    extend="Explica qué te dice el gráfico y qué no te dice sobre el próximo lanzamiento.",
)

register(
    OA26, 4,
    materials="Lápiz y papel. Los datos de los experimentos están escritos en los ejercicios; si tienes moneda o dado, puedes repetirlos.",
    use="Aprenderé a comparar frecuencias y a no asegurar lo que saldrá en el próximo ensayo. Sirve para hablar del azar con cuidado.",
    prior=["Sé hacer tabla y gráfico de frecuencias.", "Sé comparar números."],
    explain=[
        "Después de hacer un experimento puedes comparar las frecuencias: qué resultado salió más veces, cuál menos y si hubo empates. Por ejemplo, en 20 lanzamientos de moneda salieron 11 caras y 9 sellos: salió más cara.",
        "Eso no significa que en el siguiente lanzamiento vaya a salir cara, ni que «ya le toca» a sello. Cada lanzamiento es independiente y no se puede asegurar qué saldrá. Si repites los 20 lanzamientos, puedes obtener otras frecuencias.",
        "Por eso se escriben conclusiones con cuidado: «En estos 20 lanzamientos salió más cara que sello». No se escribe «siempre saldrá cara». Si juntas más ensayos, el conjunto de datos es más grande, pero el próximo resultado sigue sin poder asegurarse.",
    ],
    vocab=[("comparar frecuencias", "ver qué resultado salió más veces, menos veces o igual"), ("asegurar", "decir con certeza que algo ocurrirá"), ("azar", "lo que no se puede predecir con seguridad"), ("conclusión prudente", "frase que dice lo observado sin prometer el futuro")],
    worked=[
        {"title": "Comparar sin asegurar", "problem": f"En 20 lanzamientos salió cara {M['cara']} veces y sello {M['sello']} veces. Escribe una conclusión prudente.", "steps": [f"Comparo: {M['cara']} es mayor que {M['sello']}.", "Digo qué ocurrió en esos ensayos sin hablar del futuro."], "answer": "En estos 20 lanzamientos salió más cara que sello"},
        {"title": "Una afirmación que no se puede hacer", "problem": f"Después de {M['cara']} caras y {M['sello']} sellos, Ana dice: «El próximo lanzamiento será cara». ¿Se puede asegurar?", "steps": ["El lanzamiento siguiente depende del azar.", "Antes salió más cara, pero eso no obliga al próximo resultado."], "answer": "No se puede asegurar"},
    ],
    mistakes=[
        {"wrong": "Pensar que después de varias caras seguidas «ya le toca» a sello.", "why": "Cada lanzamiento es independiente de los anteriores.", "fix": "No se puede asegurar qué sale; la moneda no recuerda."},
        {"wrong": "Concluir «siempre saldrá cara» porque salió más veces.", "why": "Se generaliza a partir de una repetición.", "fix": "Di solo lo que ocurrió en esos ensayos."},
    ],
    tiers={
        "recovery": [
            ex(f"En 20 lanzamientos salió cara {M['cara']} veces y sello {M['sello']} veces. ¿Cuál salió más veces?", "Cara", f"{M['cara']} es mayor que {M['sello']}."),
            ex("En un experimento, A salió 5 veces y B salió 5 veces. ¿Hay empate?", "Sí", "Las frecuencias son iguales."),
            ex("¿Se puede asegurar qué saldrá en el próximo lanzamiento de una moneda?", "No", "El resultado depende del azar."),
        ],
        "understand": [
            ex(f"En una ruleta, 10 giros dieron rojo {R['rojo']}, azul {R['azul']}, verde {R['verde']}, amarillo {R['amarillo']}. ¿Qué color salió menos veces?", "Amarillo", f"Amarillo tiene {R['amarillo']}, la frecuencia más baja."),
            ex("Una moneda salió cara cuatro veces seguidas. ¿Es seguro que la quinta vez será sello?", "No", "Cada lanzamiento es independiente."),
            ex("¿Qué frase es prudente: «En estos 20 lanzamientos salió más cara» o «siempre saldrá cara»?", "«En estos 20 lanzamientos salió más cara»", "Habla solo de lo observado."),
        ],
        "apply": [
            ex(f"Dado, 12 lanzamientos ({LDADO}). ¿Qué número salió más veces?", "El 3", f"El 3 salió {D[3]} veces, más que los otros."),
            ex(f"En esos 12 lanzamientos ({LDADO}), ¿cuántas veces más salió el 3 que el 4?", str(D[3] - D[4]), "Se restan las frecuencias.", calc="4-1"),
            ex("Dos amigos lanzan una moneda 10 veces cada uno. Uno obtiene 6 caras y el otro 4 caras. ¿Es raro que obtengan resultados distintos?", "No", "El azar puede dar resultados distintos en cada serie."),
        ],
        "reason": [
            ex("Teo dice: «Salió 3 muchas veces, así que en el próximo lanzamiento saldrá otra vez 3». ¿Qué error hay?", "No se puede asegurar el próximo resultado", "El dado no recuerda lo anterior."),
            ex("Dos series de 20 lanzamientos dieron 11 y 8 caras. ¿Por qué no sorprende?", "Porque con azar las series pueden dar resultados distintos", "El resultado de cada serie depende del azar."),
        ],
        "challenge": [
            ex("En un experimento, A salió 7 veces, B 5 veces y C 8 veces. Escribe una conclusión prudente con los nombres.", "En estos ensayos, C salió más veces y B menos", "Solo describe lo observado."),
            ex("Si juntas dos series de lanzamientos de 20 cada una, ¿cuántos ensayos tienes?", "40", "20 + 20 = 40.", calc="20+20"),
        ],
    },
    context=[ex("Mía y Pablo lanzan un dado 12 veces. En la serie de Mía salió el 6 cuatro veces; en la de Pablo salió el 6 una vez. ¿Se puede asegurar que el dado de Mía es distinto del de Pablo?", "No", "Series cortas pueden dar frecuencias distintas por azar.")],
    selfcheck=[
        ex("¿Qué significa comparar frecuencias?", "Ver qué resultado salió más veces, menos veces o igual", "Es comparar los conteos."),
        ex("Si en 10 lanzamientos salió cara 7 veces, ¿cuántas veces salió sello?", "3", "10 − 7 = 3.", calc="10-7"),
        ex("¿Se puede asegurar el próximo resultado de un experimento de azar?", "No", "Depende del azar."),
    ],
    open_task=task(
        "Usa una de estas series: A) 20 lanzamientos de moneda de esta clase: " + LMONEDA + ". B) 12 lanzamientos de dado: " + LDADO + ". Haz la tabla de frecuencias, di qué resultado salió más y cuál menos, y escribe una conclusión prudente. Escribe también una frase sobre qué NO se puede asegurar.",
        "Serie B: el 3 salió 4 veces y los números 1, 2 y 4 salieron 1 vez. En estos 12 lanzamientos salió más el 3. No se puede asegurar qué saldrá en el próximo.",
        ["elige una serie y hace la tabla", "compara las frecuencias", "escribe una conclusión prudente", "dice qué no se puede asegurar"],
        ["tabla", "comparación", "frase prudente"],
        ["asegurar el futuro", "contar mal"],
        "Pide leer en voz alta la frase de lo que no se puede asegurar. Reconoce la conclusión prudente.",
    ),
    reinforce="Lanza una moneda 10 veces y anota los resultados. Luego lánzala otras 10 veces y compara las frecuencias de las dos series.",
    extend="Explica con tus palabras por qué el azar no «compensa» los resultados de los lanzamientos anteriores.",
)
