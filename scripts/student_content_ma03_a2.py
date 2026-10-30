"""Student material for 3.º básico Matemática, OA 02 (representaciones hasta 1.000) y OA 03 (comparar y ordenar)."""
from __future__ import annotations

from student_content_ma03_a import blk, task, words3
from student_lessons import arith, ex, register

OA2 = "MA03 OA 02"
OA3 = "MA03 OA 03"

# ---------------------------------------------------------------- OA 02
register(
    OA2, 1,
    materials="Lápiz y cuaderno. Las palabras y los números que necesitas están escritos en cada ejercicio.",
    use="Aprenderé a leer y escribir con palabras los números hasta 1.000. Sirve para entender precios, fechas y cantidades escritas en letras.",
    prior=["Sé leer y escribir números hasta 100.", "Sé que un número de tres cifras tiene centenas, decenas y unidades."],
    explain=[
        "Los números de tres cifras se leen empezando por las centenas: 300 es «trescientos», 500 es «quinientos» y 700 es «setecientos». Después se leen las decenas y las unidades como en un número de dos cifras: 345 es «trescientos cuarenta y cinco».",
        "Cuando falta una cifra, esa parte no se dice. En 305 no hay decenas, entonces se lee «trescientos cinco». En 340 no hay unidades, entonces se lee «trescientos cuarenta». El cero guarda el lugar, pero no se pronuncia.",
        "El 100 tiene dos formas: se dice «cien» si está solo, y «ciento» si hay algo más, como en 120, «ciento veinte». El 1.000 se lee «mil». Estas palabras son largas, así que léelas por partes: primero la centena, luego lo demás.",
    ],
    vocab=[("centena completa", "número como 300, 500 o 700, sin decenas ni unidades"), ("centena incompleta", "número de tres cifras con decenas o unidades, como 345"), ("cifra", "uno de los dígitos del 0 al 9 con que se escribe un número"), ("cero", "cifra que guarda un lugar vacío"), ("mil", "diez centenas, se escribe 1.000")],
    worked=[
        {"title": "De cifras a palabras", "problem": "Escribe con palabras el número 468.", "steps": ["Centenas: 4 centenas son «cuatrocientos».", "Lo que queda es 68: «sesenta y ocho».", "Junto las partes: «cuatrocientos sesenta y ocho»."], "answer": "cuatrocientos sesenta y ocho"},
        {"title": "Un cero que guarda lugar", "problem": "Escribe con cifras «seiscientos cinco».", "steps": ["«Seiscientos» son 6 centenas: 6 _ _.", "Después sigue «cinco»: son 5 unidades y no se nombran decenas.", "Las decenas valen 0, entonces escribo 6 0 5."], "answer": "605"},
    ],
    mistakes=[
        {"wrong": "Escribir 65 para «seiscientos cinco».", "why": "Se olvida la cifra de las centenas y el cero que guarda las decenas.", "fix": "Escribe tres lugares: 6 (centenas), 0 (decenas), 5 (unidades): 605."},
        {"wrong": "Leer 120 como «cien veinte».", "why": "Se usa «cien» cuando hay más números después.", "fix": "Si hay decenas o unidades, se dice «ciento»: «ciento veinte»."},
    ],
    tiers={
        "recovery": [
            ex("Escribe con cifras: quinientos.", "500", "«Quinientos» son 5 centenas, sin decenas ni unidades."),
            ex("Escribe con palabras el número 700.", "setecientos", "7 centenas se dicen «setecientos»."),
            ex("Escribe con cifras: ciento veinte.", "120", "«Ciento» es 100 y «veinte» es 20."),
        ],
        "understand": [
            ex("¿Cómo se lee 250?", "doscientos cincuenta", "2 centenas son «doscientos» y 5 decenas son «cincuenta»."),
            ex("¿Qué número es «cuatrocientos cinco»: 450 o 405?", "405", "No se nombran decenas, así que las decenas son 0: 4 0 5."),
            ex("¿Cómo se dice el 100 cuando está solo? ¿Y el 130?", "Cien; ciento treinta", "Solo se dice «cien»; si hay algo más, «ciento»."),
        ],
        "apply": [
            ex("Escribe con cifras: seiscientos setenta y ocho.", "678", "600 + 70 + 8 = 678."),
            ex("Escribe con palabras el número 903.", "novecientos tres", "9 centenas son «novecientos»; no hay decenas y las unidades son 3."),
            ex("Una etiqueta dice «ochocientos cuarenta». Escribe el número con cifras.", "840", "8 centenas, 4 decenas y 0 unidades."),
        ],
        "reason": [
            ex("Leo escribió 350 para «trescientos cinco». ¿Qué error cometió y cuál es el número correcto?", "305", "«Cinco» son unidades; las decenas valen 0, no 5."),
            ex("Ordena de menor a mayor: doscientos diez, ciento noventa, doscientos uno.", "190, 201, 210", "Ciento noventa es 190; doscientos uno es 201 y doscientos diez es 210."),
        ],
        "challenge": [
            ex("Escribe con cifras el número que viene justo después de «novecientos noventa y nueve».", "1.000", "999 + 1 = 1.000, que se lee «mil»."),
            ex("Escribe con palabras los números 1.000 y 999.", "mil; novecientos noventa y nueve", "1.000 se lee «mil» y 999 son 9 centenas, 9 decenas y 9 unidades."),
        ],
    },
    context=[ex("Un cartel de una feria dice: «Entrada para ciento cincuenta personas». ¿Cuántas personas son, escritas con cifras?", "150", "«Ciento» es 100 y «cincuenta» es 50.")],
    selfcheck=[
        ex("Escribe con cifras: doscientos.", "200", "«Doscientos» son 2 centenas."),
        ex("Escribe con palabras: 560.", "quinientos sesenta", "5 centenas son «quinientos» y 6 decenas son «sesenta»."),
        ex("¿330 se lee «trescientos treinta» o «trece treinta»?", "trescientos treinta", "3 centenas son «trescientos» y 3 decenas son «treinta»."),
    ],
    open_task=task(
        "Escribe con palabras estos tres números: 408, 570 y 115. Luego dibuja una tarjeta para el número 650 y escribe debajo cómo se lee.",
        "408: cuatrocientos ocho. 570: quinientos setenta. 115: ciento quince. En la tarjeta de 650 escribo: seiscientos cincuenta.",
        ["escribe correctamente los tres números con palabras", "no nombra el cero", "usa «ciento» o «cien» bien cuando corresponde", "lee el número de la tarjeta"],
        ["palabras escritas en el cuaderno", "tarjeta dibujada con el número y su nombre"],
        ["escribir «cuatrocientos y ocho»", "olvidar la palabra de las centenas"],
        "Reconoce los números bien escritos y pide que lea en voz alta la tarjeta; si hay error, que escriba primero las cifras y luego las palabras.",
    ),
    reinforce="Con tarjetas de papel, escribe en cada una un número entre 100 y 999 y en el reverso su nombre. Léelos y revisa dándolos vuelta.",
    extend="Escribe con palabras los números 101, 110 y 111. ¿Qué pasa con la palabra «ciento» en ellos?",
)

register(
    OA2, 2,
    materials="Papel, lápiz y, si quieres, tapas o fichas. Las cantidades están escritas en cada ejercicio. Usamos ▣ para una centena, ▮ para una decena y ● para una unidad.",
    use="Aprenderé a formar un número de tres cifras con centenas, decenas y unidades. Sirve para escribir cuántas cosas hay cuando vienen en cajas, bolsas y sueltas.",
    prior=["Sé que 10 unidades forman una decena y 10 decenas forman una centena.", "Sé leer números de tres cifras."],
    explain=[
        "Un número de tres cifras se arma con tres partes: las centenas, las decenas y las unidades. Si hay 3 centenas, 2 decenas y 4 unidades, el número es 324. La primera cifra dice cuántas centenas, la segunda cuántas decenas y la tercera cuántas unidades.",
        "Si en un lugar no hay nada, escribes 0. Con 5 centenas, 0 decenas y 7 unidades, el número es 507. Sin el cero escribirías 57, que es otro número. El cero guarda el lugar de las decenas.",
        "También puedes ir al revés: en 482 hay 4 centenas, 8 decenas y 2 unidades. Con las cifras 4, 8 y 2 se pueden formar otros números, como 248 o 824. Cambiar el orden cambia el número, porque cada lugar vale distinto.",
    ],
    vocab=[("numeral", "el número escrito con cifras"), ("centena", "100 unidades, se dibuja con ▣"), ("decena", "10 unidades, se dibuja con ▮"), ("unidad", "una cosa sola, se dibuja con ●"), ("lugar", "posición de una cifra: centenas, decenas o unidades")],
    worked=[
        {"title": "Armar un numeral", "problem": "Hay 2 centenas, 4 decenas y 6 unidades. ¿Qué número se forma?", "steps": ["Escribo el lugar de cada parte: centenas 2, decenas 4, unidades 6.", "Junto las cifras en ese orden: 2 4 6."], "answer": "246"},
        {"title": "Un lugar vacío", "problem": f"Mira los bloques: {blk(5, 0, 7)}. ¿Qué número muestran?", "steps": ["Cuento las centenas ▣: 5.", "No hay decenas ▮, entonces hay 0.", "Cuento las unidades ●: 7. El número es 5 0 7."], "answer": "507"},
    ],
    mistakes=[
        {"wrong": "Escribir 57 para 5 centenas y 7 unidades.", "why": "Se omite el cero de las decenas y el número queda con solo dos cifras.", "fix": "Escribe 0 en el lugar vacío: 507."},
        {"wrong": "Escribir 423 para 3 centenas, 2 decenas y 4 unidades.", "why": "Se escribieron las cifras en el orden en que se nombraron las cantidades, no en el orden de los lugares.", "fix": "Primero centenas, luego decenas, luego unidades: 324."},
    ],
    tiers={
        "recovery": [
            ex("Hay 2 centenas, 4 decenas y 6 unidades. ¿Qué número se forma?", "246", "Se escriben las cifras en orden: centenas 2, decenas 4, unidades 6."),
            ex(f"Cuenta los bloques y escribe el número: {blk(1, 5, 3)}.", "153", "Hay 1 ▣, 5 ▮ y 3 ●."),
            ex("Forma el número con 5 centenas, 0 decenas y 7 unidades.", "507", "El 0 guarda el lugar de las decenas."),
        ],
        "understand": [
            ex("En el número 482, ¿cuántas centenas, decenas y unidades hay?", "4 centenas, 8 decenas y 2 unidades", "Cada cifra ocupa un lugar: centenas 4, decenas 8, unidades 2."),
            ex("¿Cuál número es mayor: el de 3 centenas y 2 decenas o el de 2 centenas y 9 decenas?", "El de 3 centenas y 2 decenas", "Valen 320 y 290; 320 es mayor."),
            ex(f"¿Qué número muestran estos bloques: {blk(6, 0, 0)}?", "600", "6 centenas, 0 decenas y 0 unidades."),
        ],
        "apply": [
            ex("Con las cifras 7, 2 y 5, usando cada una una vez, forma el mayor número posible.", "752", "La cifra más grande, 7, va en las centenas; luego 5 y 2."),
            ex("Con las cifras 7, 2 y 5, usando cada una una vez, forma el menor número posible.", "257", "La cifra más pequeña, 2, va en las centenas; luego 5 y 7."),
            ex("Un número tiene 4 en las centenas, 0 en las decenas y 9 en las unidades. ¿Cuál es?", "409", "Se escriben en orden las cifras 4, 0 y 9."),
        ],
        "reason": [
            ex("Nico escribió 63 para 6 centenas y 3 unidades. ¿Qué error cometió y cuál es el número correcto?", "Olvidó el 0 de las decenas; es 603", "Con 6 centenas, 0 decenas y 3 unidades se escribe 6 0 3."),
            ex("Un número tiene 2 centenas, 4 decenas y tantas unidades como decenas. ¿Cuál es?", "244", "Las unidades son 4, igual que las decenas."),
        ],
        "challenge": [
            ex("¿Cuántos números distintos de tres cifras puedes formar con las cifras 1, 2 y 3, usando cada una una vez?", "6", "Son 123, 132, 213, 231, 312 y 321."),
            ex("Con las cifras 3, 0 y 8, sin repetir, escribe el mayor y el menor número de tres cifras.", "830 y 308", "El mayor es 830. El menor no puede empezar en 0 (038 no tiene tres cifras), así que es 308."),
        ],
    },
    context=[arith("En una bodega hay 3 cajas con 100 lápices cada una, 5 paquetes con 10 lápices cada uno y 2 lápices sueltos. ¿Cuántos lápices hay?", "300+50+2", "3 centenas son 300, 5 decenas son 50 y 2 unidades son 2.")],
    selfcheck=[
        ex("2 centenas, 3 decenas y 1 unidad: ¿qué número es?", "231", "Se escriben en orden las cifras 2, 3 y 1."),
        ex("¿Cuántas decenas tiene el número 506?", "0", "En 506 el lugar de las decenas tiene un 0."),
        ex("Escribe el número que es 800 + 40 + 5.", "845", "8 centenas, 4 decenas y 5 unidades."),
    ],
    open_task=task(
        "Escoge uno de estos tres números: 273, 306 o 840. Escribe cuántas centenas, decenas y unidades tiene. Luego dibuja los bloques con ▣, ▮ y ●, o con cuadrados, palitos y puntos.",
        "Elijo 306: 3 centenas, 0 decenas y 6 unidades. Dibujo ▣ ▣ ▣ y ● ● ● ● ● ●. No dibujo palitos porque hay 0 decenas.",
        ["escribe bien la cantidad de cada lugar", "no dibuja decenas cuando hay 0", "el dibujo coincide con el número", "usa los símbolos acordados"],
        ["números descompuestos en el cuaderno", "dibujo de bloques"],
        ["olvidar el cero", "mezclar centenas con decenas"],
        "Reconoce el número descompuesto y el dibujo; pregunta qué lugar quedó vacío y por qué se escribe 0. Si hay error, que cuente los dibujos con tapas.",
    ),
    reinforce="Con 10 tapas rojas (centenas), 10 azules (decenas) y 10 verdes (unidades), arma el número 234 y luego el 304.",
    extend="¿Cuántos números de tres cifras hay con 3 centenas y 0 decenas? Escríbelos todos.",
)

register(
    OA2, 3,
    materials="Lápiz, cuaderno y una regla. Usamos ▣ para una centena, ▮ para una decena y ● para una unidad; también puedes dibujar cuadrados, palitos y puntos.",
    use="Aprenderé a pasar de un dibujo de bloques a un número y de un número a un dibujo. Sirve para explicar un número de tres cifras sin palabras difíciles.",
    prior=["Sé armar un número con centenas, decenas y unidades.", "Sé leer números hasta 1.000."],
    explain=[
        "Un número se puede mostrar de tres formas. La forma concreta usa objetos, como cubos o tapas. La forma pictórica usa un dibujo, por ejemplo ▣ ▮ ●. La forma simbólica usa cifras, como 234. Las tres cuentan lo mismo.",
        "Para pasar del dibujo a las cifras, cuenta cuántos ▣, cuántos ▮ y cuántos ●. En ▣ ▣ | ▮ ▮ ▮ | ● ● ● ● hay 2 centenas, 3 decenas y 4 unidades, así que el número es 234.",
        "Para pasar de las cifras al dibujo, mira cada cifra. En 305 la primera cifra es 3: dibuja tres ▣. La segunda es 0: no dibujas ▮. La tercera es 5: dibujas cinco ●. Después cuenta tu dibujo para comprobarlo.",
    ],
    vocab=[("concreto", "hecho con objetos que se pueden tocar"), ("pictórico", "hecho con dibujos"), ("simbólico", "hecho con cifras"), ("representar", "mostrar un número de otra manera"), ("bloque", "figura que muestra una centena, una decena o una unidad")],
    worked=[
        {"title": "Del dibujo al símbolo", "problem": f"Mira el dibujo: {blk(2, 3, 4)}. Escribe el número.", "steps": ["Cuento los cuadrados ▣: 2 centenas.", "Cuento los palitos ▮: 3 decenas.", "Cuento los puntos ●: 4 unidades.", "Escribo 2 3 4."], "answer": "234"},
        {"title": "Del símbolo al dibujo", "problem": "Dibuja el número 143 con ▣, ▮ y ●.", "steps": ["La cifra 1 indica 1 centena: ▣.", "La cifra 4 indica 4 decenas: ▮ ▮ ▮ ▮.", "La cifra 3 indica 3 unidades: ● ● ●.", "Cuento mi dibujo y compruebo que dice 143."], "answer": f"{blk(1, 4, 3)}"},
    ],
    mistakes=[
        {"wrong": "Dibujar 4 ▣ para el número 4.", "why": "Se confunde la cifra con una centena en lugar de una unidad.", "fix": "Mira en qué lugar está la cifra: en 4 es una unidad, entonces ● ● ● ●."},
        {"wrong": "Contar 7 figuras y escribir 7.", "why": "Se cuenta cuántas figuras hay y no cuánto vale cada una.", "fix": "Cuenta por separado ▣, ▮ y ●, porque valen 100, 10 y 1."},
    ],
    tiers={
        "recovery": [
            ex(f"Mira el dibujo {blk(2, 3, 4)}. Escribe el número.", "234", "Hay 2 ▣, 3 ▮ y 4 ●."),
            ex("Dibujas 1 cuadrado, 6 palitos y 8 puntos. ¿Qué número representas?", "168", "1 centena, 6 decenas y 8 unidades."),
            ex("Para dibujar el número 305 con cuadrados, palitos y puntos, ¿cuántas figuras de cada tipo necesitas?", "3 cuadrados, 0 palitos y 5 puntos", "Cada cifra dice cuántas figuras de su tipo hay."),
        ],
        "understand": [
            ex("Un dibujo tiene 4 cuadrados y 7 puntos, sin palitos. ¿Qué número es?", "407", "No hay decenas, entonces ese lugar vale 0."),
            ex("¿Cuál dibujo muestra 260: A) 2 cuadrados y 6 palitos, o B) 2 cuadrados y 6 puntos?", "A", "Los palitos son decenas: 2 centenas y 6 decenas son 260."),
            ex("Un dibujo no tiene cuadrados, tiene 9 palitos y 1 punto. ¿Qué número muestra?", "91", "9 decenas y 1 unidad son 91."),
        ],
        "apply": [
            ex("Dibuja el número 143 con ▣, ▮ y ● y escribe cuántas figuras de cada tipo usaste.", f"{blk(1, 4, 3)}: 1, 4 y 3", "La cifra de cada lugar dice cuántas figuras de ese tipo se dibujan."),
            ex("Escribe con cifras el número que muestra: ▣ ▣ ▣ ▣ ▣ | ▮ | ●.", "511", "5 centenas, 1 decena y 1 unidad."),
            arith("Para dibujar el 999 usas cuadrados, palitos y puntos. ¿Cuántas figuras dibujas en total?", "9+9+9", "9 cuadrados, 9 palitos y 9 puntos."),
        ],
        "reason": [
            ex("Sara dibujó 3 cuadrados, 2 palitos y 5 puntos y escribió 325. Su compañero dice que es 523. ¿Quién tiene razón y por qué?", "Sara", "Los cuadrados son centenas: 3 centenas, 2 decenas y 5 unidades son 325."),
            ex("¿Qué número necesita más figuras para dibujarse, 199 o 301? Cuenta las figuras de cada uno.", "199", "199 usa 1 + 9 + 9 = 19 figuras. 301 usa 3 + 0 + 1 = 4."),
        ],
        "challenge": [
            ex("¿Cuál es el menor número de tres cifras cuyo dibujo usa exactamente 5 figuras (cuadrados, palitos y puntos juntos)?", "104", "Con 1 cuadrado y 4 puntos son 5 figuras. Un número menor, como 103, usa 4."),
            ex("¿Cuál es el mayor número menor que 1.000 cuyo dibujo usa exactamente 4 figuras?", "400", "Con 4 cuadrados son 4 figuras. Ningún otro dibujo de 4 figuras supera 400."),
        ],
    },
    context=[ex("Un almacén tiene 2 pilas de 100 hojas, 3 pilas de 10 hojas y 6 hojas sueltas. Dibuja con ▣, ▮ y ● y escribe cuántas hojas hay.", "236", "2 centenas, 3 decenas y 6 unidades.")],
    selfcheck=[
        ex("¿Qué número muestra ▣ ▣ | ▮ ▮ ▮ | ●?", "231", "2 centenas, 3 decenas y 1 unidad."),
        ex("¿Qué figura muestra 10 unidades juntas?", "Un palito ▮", "10 unidades forman 1 decena."),
        ex("Para dibujar 450, ¿cuántos palitos necesitas?", "5", "La cifra de las decenas es 5."),
    ],
    open_task=task(
        "Representa el número 328 de las tres formas: con fichas de colores, donde cada ficha azul vale 100, cada roja vale 10 y cada verde vale 1 (concreta), con un dibujo de cuadrados, palitos y puntos (pictórica) y con cifras (simbólica). Escribe una frase que diga qué cambió y qué quedó igual entre una forma y otra.",
        "Concreta: 3 fichas azules, 2 rojas y 8 verdes. Pictórica: ▣ ▣ ▣ | ▮ ▮ | ● ● ● ● ● ● ● ●. Simbólica: 328. En las tres hay 3 centenas, 2 decenas y 8 unidades.",
        ["usa las tres representaciones", "las tres coinciden con 328", "escribe la frase comparando", "cuenta las centenas, decenas y unidades"],
        ["fichas ordenadas por color o descripción de ellas", "dibujo con figuras", "cifras escritas"],
        ["dibujar mal la cantidad de decenas", "no explicar qué quedó igual"],
        "Pregunta cómo comprobó que las tres formas dicen lo mismo; si hay error, pide que cuente figura por figura.",
    ),
    reinforce="Dibuja con ▣, ▮ y ● los números 213 y 120, y escribe debajo cuántas figuras de cada tipo usaste.",
    extend="Dibuja un número de tres cifras que use exactamente 6 figuras en total y escribe cuál es.",
)

register(
    OA2, 4,
    materials="Lápiz, cuaderno y, si quieres, 30 tapas o fichas. Usamos ▣ para una centena, ▮ para una decena y ● para una unidad.",
    use="Aprenderé que un mismo número se puede mostrar de más de una manera, por ejemplo 250 como 25 decenas. Sirve para canjear y juntar cantidades.",
    prior=["Sé armar un número de tres cifras con centenas, decenas y unidades.", "Sé que 10 unidades forman una decena y 10 decenas forman una centena."],
    explain=[
        "La forma usual de mostrar un número usa pocas piezas: 250 son 2 centenas y 5 decenas. Pero 250 también son 25 decenas, o 2 centenas y 50 unidades. Son maneras distintas de mostrar la misma cantidad; el número no cambia.",
        "Para pasar de una forma a otra se canjea: 10 unidades se cambian por 1 decena, y 10 decenas se cambian por 1 centena. Así, 2 centenas y 13 decenas son 200 + 130 = 330. Para ver el número usual, cambia 10 decenas por 1 centena: queda 3 centenas y 3 decenas.",
        "Para comprobar que dos formas dicen lo mismo, calcula el valor de cada una. 3 centenas y 18 decenas valen 300 + 180 = 480. 4 centenas y 8 decenas valen 400 + 80 = 480. Como dan lo mismo, representan el mismo número.",
    ],
    vocab=[("canjear", "cambiar 10 piezas pequeñas por 1 pieza mayor, o al revés"), ("forma usual", "manera de mostrar un número con la menor cantidad de piezas"), ("forma no usual", "otra manera de mostrar el mismo número, con más piezas pequeñas"), ("equivalente", "que vale lo mismo"), ("valor", "cuánto representa una pieza o un número")],
    worked=[
        {"title": "Decenas de más", "problem": "Un número tiene 2 centenas, 13 decenas y 4 unidades. ¿Qué número es?", "steps": ["Valor de las centenas: 200.", "13 decenas valen 130 (10 decenas son 100 y 3 decenas son 30).", "Sumo: 200 + 130 + 4 = 334."], "answer": "334"},
        {"title": "Dos formas, mismo número", "problem": "Ana muestra 4 centenas y 8 decenas. Bea muestra 3 centenas y 18 decenas. ¿Es el mismo número?", "steps": ["Ana: 400 + 80 = 480.", "Bea: 300 + 180 = 480.", "Los dos valores son iguales."], "answer": "Sí, ambos son 480"},
    ],
    mistakes=[
        {"wrong": "Decir que 3 centenas y 25 decenas valen 325.", "why": "Se suman las cifras como si 25 fueran unidades.", "fix": "25 decenas valen 250: 300 + 250 = 550."},
        {"wrong": "Pensar que 25 decenas y 2 centenas con 5 decenas son números distintos.", "why": "Se compara la cantidad de piezas y no su valor.", "fix": "Calcula el valor de cada forma: ambos valen 250."},
    ],
    tiers={
        "recovery": [
            ex("10 unidades forman 1 decena. 23 unidades son ___ decenas y ___ unidades.", "2 decenas y 3 unidades", "En 23 unidades hay dos grupos de 10 y sobran 3."),
            ex("¿Es lo mismo 1 centena que 10 decenas?", "Sí", "10 decenas se canjean por 1 centena."),
            ex("El número 140 se puede escribir como 14 decenas. ¿Cuántas centenas y decenas tiene en su forma usual?", "1 centena y 4 decenas", "100 + 40 = 140."),
        ],
        "understand": [
            ex("¿Cuáles representan 250: A) 2 centenas y 5 decenas, B) 2 centenas y 50 unidades, C) 25 decenas?", "Las tres", "A: 200 + 50, B: 200 + 50 y C: 250. Las tres valen 250."),
            ex("¿Cuál no representa 340: 34 decenas, 3 centenas y 4 decenas, o 3 centenas y 14 decenas?", "3 centenas y 14 decenas", "Esa forma vale 300 + 140 = 440."),
            ex("Escribe el número que tiene 42 decenas y 5 unidades.", "425", "42 decenas son 420 y 420 + 5 = 425."),
        ],
        "apply": [
            arith("Un número se forma con 2 centenas, 13 decenas y 4 unidades. ¿Qué número es?", "200+130+4", "13 decenas valen 130."),
            ex("Una caja se llena con 10 lápices. Hay 47 lápices sueltos. ¿Cuántas cajas completas se pueden armar y cuántos lápices sobran?", "4 cajas y sobran 7", "En 47 caben cuatro grupos de 10 y sobran 7."),
            ex("Escribe el número 600 de dos maneras: con centenas y con decenas.", "6 centenas; 60 decenas", "6 centenas valen 600 y 60 decenas también."),
        ],
        "reason": [
            ex("Pedro dice: «Tengo 3 centenas y 25 decenas, o sea 325». ¿Es correcto?", "No, es 550", "25 decenas valen 250 y 300 + 250 = 550."),
            ex("Ana muestra 4 centenas y 8 decenas. Bea muestra 3 centenas y 18 decenas. ¿Representan el mismo número?", "Sí", "Los dos valen 480."),
        ],
        "challenge": [
            ex("Quiero mostrar 520 con 4 centenas y las decenas que faltan. ¿Cuántas decenas necesito?", "12 decenas", "4 centenas valen 400 y para llegar a 520 faltan 120, que son 12 decenas."),
            ex("¿Cuántas unidades tiene en total el número que tiene 3 centenas y 2 decenas?", "320", "300 + 20 = 320 unidades."),
        ],
    },
    context=[arith("En un almacén hay 5 cajas con 100 clips cada una, 14 bolsas con 10 clips cada una y 6 clips sueltos. ¿Cuántos clips hay?", "500+140+6", "14 bolsas de 10 clips son 140 clips.")],
    selfcheck=[
        ex("¿Cuántas decenas hay en 1 centena?", "10", "1 centena son 100 unidades, o sea 10 decenas."),
        ex("30 decenas, ¿qué número son?", "300", "30 decenas valen 300."),
        ex("1 centena y 15 decenas, ¿qué número son?", "250", "100 + 150 = 250."),
    ],
    open_task=task(
        "Muestra el número 360 de tres maneras distintas con centenas, decenas y unidades. Una manera posible es 3 centenas y 6 decenas. Para cada manera, escribe el cálculo que prueba que vale 360 y dibuja con ▣, ▮ y ● la primera.",
        "3 centenas y 6 decenas: 300 + 60 = 360. 36 decenas: 36 decenas son 360. 2 centenas y 16 decenas: 200 + 160 = 360. Dibujo: ▣ ▣ ▣ | ▮ ▮ ▮ ▮ ▮ ▮.",
        ["muestra tres maneras", "cada una vale 360", "escribe un cálculo por cada manera", "dibuja la primera"],
        ["tres formas escritas en el cuaderno", "cálculos", "dibujo"],
        ["decir que una forma vale otra cantidad", "olvidar el valor de las decenas"],
        "Reconoce la variedad de formas y pregunta cómo comprobó que valen lo mismo; si hay error, que cambie 10 decenas por 1 centena con tapas.",
    ),
    reinforce="Con 12 tapas de decena (cada una vale 10) arma un grupo de 10 tapas y cámbialo por una tapa de 100. ¿Cuántas decenas quedan?",
    extend="Escribe 1.000 como centenas, como decenas y como unidades.",
)

# ---------------------------------------------------------------- OA 03
register(
    OA3, 1,
    materials="Lápiz y cuaderno. Usa una tabla con las columnas C (centenas), D (decenas) y U (unidades). Los números están escritos en cada ejercicio.",
    use="Aprenderé a decir cuál de dos números de tres cifras es mayor mirando primero las centenas. Sirve para comparar precios o cantidades sin contar todo.",
    prior=["Sé leer y escribir números de tres cifras.", "Sé usar los signos < (menor que), > (mayor que) y = (igual a)."],
    explain=[
        "Para comparar dos números de tres cifras, mira primero las centenas, porque valen más. En 523 y 481 las centenas son 5 y 4. Como 5 es mayor que 4, el número 523 es mayor, y no importa qué cifras vienen después.",
        "Los signos se leen así: el pico apunta al número menor. Escribimos 481 < 523, que se lee «cuatrocientos ochenta y uno es menor que quinientos veintitrés». También se puede escribir 523 > 481.",
        "Una tabla ayuda: pones cada número en columnas C, D, U y comparas de izquierda a derecha. Si las centenas son distintas, ya terminaste. Si son iguales, tendrías que mirar las decenas, eso lo verás en la próxima clase.",
    ],
    vocab=[("comparar", "decir cuál número es mayor, menor o si son iguales"), ("mayor que (>)", "signo para el número que vale más"), ("menor que (<)", "signo para el número que vale menos"), ("igual a (=)", "signo para dos números que valen lo mismo"), ("tabla posicional", "tabla con columnas de centenas, decenas y unidades")],
    worked=[
        {"title": "Centenas distintas", "problem": "Compara 523 y 481.", "steps": ["Pongo cada número en la tabla CDU: 5 2 3 y 4 8 1.", "Miro las centenas: 5 y 4.", "5 es mayor que 4, entonces 523 es mayor."], "answer": "523 > 481"},
        {"title": "Un número con menos cifras", "problem": "Compara 98 y 102.", "steps": ["98 tiene dos cifras, o sea 0 centenas.", "102 tiene 1 centena.", "1 centena es más que 0 centenas, entonces 102 es mayor."], "answer": "98 < 102"},
    ],
    mistakes=[
        {"wrong": "Decir que 98 es mayor que 102 porque 9 y 8 son cifras grandes.", "why": "Se miran las cifras sueltas y no cuántas cifras tiene el número.", "fix": "98 tiene 0 centenas y 102 tiene 1. Con tres cifras vale más."},
        {"wrong": "Decir que 799 es mayor que 800 porque tiene 9.", "why": "Se mira la última cifra en vez de la primera.", "fix": "Compara primero las centenas: 7 es menor que 8, entonces 799 < 800."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es mayor: 523 o 481?", "523", "Las centenas son 5 y 4, y 5 es mayor que 4."),
            ex("Escribe el signo < o > entre los números: 289 __ 312.", "<", "2 centenas es menos que 3 centenas."),
            ex("Compara las centenas: ¿qué número es menor, 745 o 654?", "654", "6 centenas es menos que 7 centenas."),
        ],
        "understand": [
            ex("Explica con las centenas por qué 901 es mayor que 789.", "9 centenas es más que 7 centenas", "901 tiene 9 centenas y 789 tiene 7."),
            ex("¿Alcanza con mirar solo las centenas para comparar 612 y 387?", "Sí", "Las centenas son distintas, 6 y 3, entonces ya se sabe cuál es mayor."),
            ex("De dos números de tres cifras, uno con 5 centenas y otro con 4 centenas, ¿cuál es mayor?", "El de 5 centenas", "Una centena más vale 100, más que cualquier diferencia en decenas y unidades."),
        ],
        "apply": [
            ex("Tres niñas juntaron figuritas: Ana 345, Bea 521 y Carla 298. ¿Quién juntó más?", "Bea", "Las centenas son 3, 5 y 2; la mayor es 5."),
            ex("¿Cuál es el menor de estos números: 864, 467 o 689?", "467", "Las centenas son 8, 4 y 6; la menor es 4."),
            ex("Escribe > o < entre los números: 750 __ 699.", ">", "7 centenas es más que 6 centenas."),
        ],
        "reason": [
            ex("Tomás dice que 98 es mayor que 102 porque 9 y 8 son cifras grandes. ¿Tiene razón?", "No", "98 tiene 0 centenas y 102 tiene 1 centena; 102 es mayor."),
            ex("Marta dice que 799 es mayor que 800 «porque tiene muchos nueves». ¿Tiene razón?", "No", "Las centenas son 7 y 8; 800 es mayor."),
        ],
        "challenge": [
            ex("¿Qué cifras pueden ir en el cuadrado para que ▢45 sea mayor que 645? Escribe todas las posibles.", "7, 8 y 9", "La cifra de las centenas debe ser mayor que 6."),
            ex("¿Qué cifras pueden ir en el cuadrado para que ▢12 sea menor que 412 y tenga tres cifras? Escribe todas.", "1, 2 y 3", "La cifra de las centenas debe ser menor que 4 y no puede ser 0."),
        ],
    },
    context=[ex("En una feria del libro la sala A recibió 412 visitas y la sala B recibió 389. ¿Qué sala recibió más y cuántas centenas tiene cada número?", "La sala A; 4 y 3 centenas", "4 centenas es más que 3 centenas.")],
    selfcheck=[
        ex("Escribe > o < entre los números: 405 __ 399.", ">", "4 centenas es más que 3 centenas."),
        ex("¿Cuál es el mayor: 250, 520 o 205?", "520", "Las centenas son 2, 5 y 2; la mayor es 5."),
        ex("¿Qué lugar se mira primero para comparar dos números de tres cifras?", "Las centenas", "Son las que más valen."),
    ],
    open_task=task(
        "Compara estos tres pares escribiendo el signo correcto: 357 y 428; 805 y 790; 611 y 163. Para cada par, escribe en una frase por qué lo sabes, mirando las centenas.",
        "357 < 428, porque 3 centenas es menos que 4 centenas. 805 > 790, porque 8 centenas es más que 7. 611 > 163, porque 6 centenas es más que 1.",
        ["usa el signo correcto en los tres pares", "explica con las centenas", "no mira las unidades primero"],
        ["pares comparados en el cuaderno", "frases de explicación"],
        ["comparar las unidades primero", "confundir < con >"],
        "Reconoce los pares bien comparados y pide leer cada signo en voz alta; si hay error, que ubique los números en una tabla CDU.",
    ),
    reinforce="Escribe 6 números de tres cifras en tarjetas, mézclalas y compara dos al azar con los signos.",
    extend="Escribe tres números distintos de tres cifras que tengan la misma cifra de las unidades y ordénalos por centenas.",
)

register(
    OA3, 2,
    materials="Lápiz y una tabla de tres columnas C, D y U en el cuaderno. Los números están escritos en cada ejercicio.",
    use="Aprenderé a comparar dos números que tienen las mismas centenas, mirando después las decenas y las unidades. Sirve para ordenar resultados muy parecidos.",
    prior=["Sé comparar números de tres cifras por sus centenas.", "Sé usar los signos <, > e =."],
    explain=[
        "A veces las centenas son iguales, como en 457 y 462. Entonces se mira el siguiente lugar, las decenas: 5 y 6. Como 6 es mayor que 5, 462 es mayor que 457, aunque las unidades sean 7 y 2.",
        "Si también las decenas son iguales, como en 634 y 639, se miran las unidades: 4 y 9. Como 9 es mayor, 639 es mayor. Siempre se avanza de izquierda a derecha: centenas, decenas y después unidades.",
        "Se para en la primera cifra que es distinta. Si todas las cifras son iguales, los números son iguales. Para ordenar varios números de menor a mayor, compáralos de a dos con esta regla.",
    ],
    vocab=[("empate", "cuando dos cifras del mismo lugar son iguales"), ("primera cifra distinta", "la primera cifra, de izquierda a derecha, que no coincide"), ("ordenar", "poner varios números del menor al mayor, o del mayor al menor"), ("ascendente", "de menor a mayor"), ("descendente", "de mayor a menor")],
    worked=[
        {"title": "Empate en centenas", "problem": "Compara 457 y 462.", "steps": ["Centenas: 4 y 4, son iguales.", "Decenas: 5 y 6. Son distintas y 6 es mayor.", "Me detengo aquí: 462 es mayor."], "answer": "457 < 462"},
        {"title": "Empate en centenas y decenas", "problem": "Compara 634 y 639.", "steps": ["Centenas: 6 y 6, iguales.", "Decenas: 3 y 3, iguales.", "Unidades: 4 y 9. 9 es mayor, entonces 639 es mayor."], "answer": "634 < 639"},
    ],
    mistakes=[
        {"wrong": "Decir que 504 es mayor que 540 porque 4 > 0.", "why": "Se mira la última cifra antes de las decenas.", "fix": "Las centenas son 5 y 5. Las decenas son 0 y 4. Como 4 es mayor que 0, 540 es mayor."},
        {"wrong": "Pensar que 355 y 358 son iguales porque las centenas coinciden.", "why": "Se detiene en las centenas aunque no sean distintas.", "fix": "Sigue hasta encontrar la primera cifra distinta: 5 y 8 en las unidades."},
    ],
    tiers={
        "recovery": [
            ex("345 y 349 tienen iguales las centenas y las decenas. ¿Cuál es mayor?", "349", "Las unidades son 5 y 9; 9 es mayor."),
            ex("Compara 572 y 538: ¿cuál es mayor?", "572", "Las centenas son iguales; las decenas son 7 y 3, y 7 es mayor."),
            ex("Escribe =, < o > entre los números: 610 __ 610.", "=", "Todas las cifras son iguales."),
        ],
        "understand": [
            ex("Para comparar 634 y 639, ¿qué cifra decide cuál es mayor?", "Las unidades", "Las centenas y las decenas coinciden; las unidades son 4 y 9."),
            ex("Para comparar 481 y 457, ¿qué lugar decide?", "Las decenas", "Las centenas son iguales, 4; las decenas son 8 y 5."),
            ex("¿Cuál es menor: 735 o 753?", "735", "Las decenas son 3 y 5; 3 es menor."),
        ],
        "apply": [
            ex("Ordena de menor a mayor: 438, 428, 478.", "428, 438, 478", "Las centenas son iguales; las decenas son 3, 2 y 7."),
            ex("Tres corredores dieron 356, 365 y 359 pasos. ¿Quién dio más pasos?", "El de 365", "Las decenas son 5, 6 y 5; la mayor es 6."),
            ex("¿Cuál es el mayor: 807, 870 o 780?", "870", "Con 8 centenas están 807 y 870; sus decenas son 0 y 7."),
        ],
        "reason": [
            ex("Pía comparó 540 y 504 mirando las unidades y dijo que 504 es mayor porque 4 > 0. ¿Qué error cometió y cuál es el mayor?", "Debió mirar las decenas; 540 es mayor", "Las decenas son 4 y 0, y 4 es mayor que 0."),
            ex("Los números 368 y 386 usan las mismas cifras: 3, 6 y 8. ¿Cuál es mayor?", "386", "Las decenas son 6 y 8; 8 es mayor."),
        ],
        "challenge": [
            ex("Escribe todos los números que hay entre 458 y 462.", "459, 460 y 461", "Son los números que quedan entre los dos."),
            ex("¿Qué cifra puede ir en el cuadrado para que 37▢ sea mayor que 378?", "9", "Las centenas y decenas coinciden; la unidad debe ser mayor que 8."),
        ],
    },
    context=[ex("Dos buses llevaron ese día 245 y 254 pasajeros. ¿Cuál llevó más?", "El de 254", "Las decenas son 4 y 5; 5 es mayor.")],
    selfcheck=[
        ex("Escribe < o > entre los números: 623 __ 632.", "<", "Las decenas son 2 y 3."),
        ex("Ordena de menor a mayor: 150, 105, 115.", "105, 115, 150", "Las decenas son 0, 1 y 5."),
        ex("Si las centenas y las decenas son iguales, ¿qué cifras se miran?", "Las unidades", "Es el único lugar que queda."),
    ],
    open_task=task(
        "Ordena de menor a mayor los números 372, 327, 377, 337 y 732. Escribe, junto a cada comparación, la cifra que decidió.",
        "327 < 337 (decenas 2 y 3), 337 < 372 (decenas 3 y 7), 372 < 377 (unidades 2 y 7), 377 < 732 (centenas 3 y 7). Orden: 327, 337, 372, 377, 732.",
        ["ordena los cinco números correctamente", "nombra la cifra que decidió", "compara de izquierda a derecha"],
        ["lista ordenada en el cuaderno", "comparaciones escritas"],
        ["empezar por las unidades", "olvidar uno de los cinco números"],
        "Reconoce el orden correcto y pregunta cuál cifra decidió en cada paso; si hay error, que ponga los números en una tabla CDU.",
    ),
    reinforce="Escribe 345, 354, 435 y 453 en tarjetas. Ordénalas de menor a mayor y di en voz alta qué cifra decidió.",
    extend="Con las cifras 4, 5 y 6 sin repetir, escribe los seis números posibles y ordénalos de menor a mayor.",
)

register(
    OA3, 3,
    materials="Una recta numérica dibujada en el cuaderno, lápiz de color y regla. Las posiciones están escritas en cada ejercicio.",
    use="Aprenderé a ordenar números hasta 1.000 poniéndolos en una recta numérica. Sirve para ver cuál está más lejos y cuál más cerca.",
    prior=["Sé comparar números de tres cifras.", "Sé contar de 10 en 10 y de 100 en 100."],
    explain=[
        "En una recta numérica los números crecen hacia la derecha. El que está más a la derecha es mayor, y el que está más a la izquierda es menor. Dos números que están cerca en la recta valen casi lo mismo.",
        "Una recta puede tener marcas de 100 en 100: 0, 100, 200, hasta 1.000. El número 340 queda entre 300 y 400. Como 340 está más cerca de 300 que de 400, lo dibujas un poco después del 300.",
        "Otra recta puede tener marcas de 10 en 10. Si empieza en 400, las marcas son 400, 410, 420, 430. Entonces 427 queda entre 420 y 430, más cerca de 430. Para ordenar, ubica cada número y lee de izquierda a derecha.",
    ],
    vocab=[("recta numérica", "línea con números ordenados de menor a mayor"), ("marca", "raya de la recta donde va un número"), ("entre", "después de uno y antes de otro"), ("más cerca", "con menos distancia"), ("izquierda y derecha", "los lados de la recta: a la derecha crecen los números")],
    worked=[
        {"title": "Ubicar entre dos marcas", "problem": "Una recta tiene marcas de 100 en 100 desde 0 hasta 1.000. ¿Entre qué marcas queda 340 y a cuál está más cerca?", "steps": ["300 es menor que 340 y 400 es mayor.", "340 está entre 300 y 400.", "340 − 300 = 40 y 400 − 340 = 60. Está más cerca de 300."], "answer": "Entre 300 y 400; más cerca de 300"},
        {"title": "Ordenar usando la recta", "problem": "Ubica en una recta 720, 270 y 702, y ordénalos de menor a mayor.", "steps": ["270 está entre 200 y 300.", "702 y 720 están entre 700 y 800; 702 está más cerca de 700.", "De izquierda a derecha: 270, 702, 720."], "answer": "270, 702, 720"},
    ],
    mistakes=[
        {"wrong": "Ubicar 340 más cerca de 400 porque «el 4 está en el 340».", "why": "Se mira solo la cifra 4 de las decenas en vez de comparar distancias.", "fix": "Calcula 340 − 300 = 40 y 400 − 340 = 60. Es menor la distancia a 300."},
        {"wrong": "Ubicar 702 a la derecha de 720.", "why": "Se mira la cifra final y no las decenas.", "fix": "Compara 0 y 2 en las decenas; 720 es mayor y va más a la derecha."},
    ],
    tiers={
        "recovery": [
            ex("En una recta numérica, ¿hacia qué lado están los números mayores: izquierda o derecha?", "Derecha", "Los números crecen hacia la derecha."),
            ex("En una recta con marcas 0, 100, 200, ..., 1.000, ¿entre qué dos marcas queda 340?", "Entre 300 y 400", "300 es menor que 340 y 400 es mayor."),
            ex("En una recta, ¿cuál queda más a la derecha: 215 o 251?", "251", "Las decenas son 1 y 5; 251 es mayor."),
        ],
        "understand": [
            ex("En una recta con marcas de 10 en 10 desde 400, ¿entre qué marcas queda 427?", "Entre 420 y 430", "420 es menor que 427 y 430 es mayor."),
            ex("¿380 está más cerca de 300 o de 400?", "De 400", "380 − 300 = 80 y 400 − 380 = 20."),
            ex("Un punto está entre 500 y 600. ¿Puede ser 650?", "No", "650 es mayor que 600."),
        ],
        "apply": [
            ex("Ordena de menor a mayor como si fueran puntos de una recta: 720, 270, 702, 207.", "207, 270, 702, 720", "Primero las centenas: 2, 2, 7, 7; luego las decenas."),
            ex("Una recta empieza en 600 y las marcas suben de 10 en 10. ¿Qué número va en la tercera marca después de 600?", "630", "610, 620 y 630."),
            ex("En una recta con marcas de 10 en 10 aparecen 290, __, 310, __, 330. Completa.", "300 y 320", "290 + 10 = 300 y 310 + 10 = 320."),
        ],
        "reason": [
            ex("Una niña ubicó 465 entre 400 y 500, pero más cerca de 400. ¿Está bien?", "No, está más cerca de 500", "465 − 400 = 65 y 500 − 465 = 35."),
            ex("En una recta están A = 380 y B = 308. ¿Cuál queda más a la izquierda?", "B", "308 es menor que 380."),
        ],
        "challenge": [
            ex("En una recta con marcas de 100 en 100, un punto está más cerca de 700 que de 800 y termina en 2. ¿Es 742 o 782?", "742", "742 − 700 = 42 y 800 − 742 = 58; 782 está más cerca de 800."),
            ex("Entre las marcas 300 y 400, con marcas de 10 en 10, ¿cuántas marcas hay en medio, sin contar 300 ni 400?", "9", "Son 310, 320, 330, 340, 350, 360, 370, 380 y 390."),
        ],
    },
    context=[ex("Una caminata tiene postes cada 100 m, desde 0 hasta 1.000 m. Dani está en el metro 640. ¿Entre qué postes está y a cuál está más cerca?", "Entre 600 y 700; más cerca de 600", "640 − 600 = 40 y 700 − 640 = 60.")],
    selfcheck=[
        ex("¿Qué queda más a la izquierda en una recta, 330 o 303?", "303", "Las decenas son 0 y 3; 303 es menor."),
        ex("¿Entre qué marcas de 100 en 100 queda 870?", "Entre 800 y 900", "800 es menor que 870 y 900 es mayor."),
        ex("Ordena de menor a mayor: 90, 900, 99.", "90, 99, 900", "90 y 99 tienen dos cifras; 900 tiene tres."),
    ],
    open_task=task(
        "Dibuja una recta con marcas de 100 en 100 desde 0 hasta 1.000. Ubica los números 85, 245, 450, 615 y 980 con un punto y escribe debajo de cada uno entre qué marcas queda.",
        "85: entre 0 y 100. 245: entre 200 y 300. 450: entre 400 y 500. 615: entre 600 y 700. 980: entre 900 y 1.000. Orden: 85, 245, 450, 615, 980.",
        ["dibuja la recta con marcas parejas", "ubica los cinco números", "dice entre qué marcas queda cada uno", "los lee de menor a mayor"],
        ["recta dibujada en el cuaderno", "puntos y frases escritas"],
        ["marcas desparejas", "ubicar un número en la marca equivocada"],
        "Reconoce las ubicaciones correctas y pide que explique por qué un punto está más cerca de una marca que de otra; si hay error, que mida con regla.",
    ),
    reinforce="Dibuja una recta con marcas cada 10 desde 300 hasta 400 y ubica 318, 352 y 397.",
    extend="Escribe tres números que queden entre 700 y 800 y más cerca de 800 que de 700.",
)

register(
    OA3, 4,
    materials="Lápiz, cuaderno y una recta numérica dibujada. Los límites de cada ejercicio están escritos.",
    use="Aprenderé a encontrar los números que están entre dos límites. Sirve para decir qué números cumplen una condición, como «más de 120 y menos de 125».",
    prior=["Sé comparar y ordenar números hasta 1.000.", "Sé contar de 1 en 1 pasando por una decena."],
    explain=[
        "«Entre dos números» significa mayores que el primero y menores que el segundo. Los números del límite no cuentan. Entre 120 y 125 están 121, 122, 123 y 124. El 120 y el 125 se quedan afuera.",
        "Para encontrarlos, cuenta de 1 en 1 desde el primero, sin decir el primero, y para antes del segundo. Si no hay números en medio, como entre 450 y 451, la respuesta es «ninguno».",
        "También puedes usar pistas. Si el número está entre 780 y 790 y termina en 5, solo puede ser 785. Una pista da el rango, y otra termina de elegir. Comprueba siempre que tu número cumpla todas las pistas.",
    ],
    vocab=[("entre", "mayor que el primero y menor que el segundo"), ("límite", "número que cierra el rango por abajo o por arriba"), ("rango", "todos los números desde un límite hasta el otro"), ("pista", "dato que ayuda a encontrar un número"), ("ninguno", "no hay ningún número")],
    worked=[
        {"title": "Los números del medio", "problem": "Escribe todos los números que hay entre 398 y 403.", "steps": ["Parto del siguiente de 398: 399.", "Sigo contando: 400, 401, 402.", "Me detengo antes de 403."], "answer": "399, 400, 401, 402"},
        {"title": "Con una pista extra", "problem": "Un número está entre 250 y 260 y tiene 7 unidades. ¿Cuál es?", "steps": ["Entre 250 y 260 están 251, 252, ..., 259.", "El que tiene 7 unidades es 257.", "257 cumple las dos pistas."], "answer": "257"},
    ],
    mistakes=[
        {"wrong": "Escribir 120, 121, 122, 123, 124, 125 para los números entre 120 y 125.", "why": "Se incluyeron los límites.", "fix": "Los números del límite no cuentan: solo 121, 122, 123 y 124."},
        {"wrong": "Decir que entre 99 y 101 no hay números.", "why": "Se olvida que 100 existe.", "fix": "Cuenta de 1 en 1: 99, 100, 101. Entre medio está el 100."},
    ],
    tiers={
        "recovery": [
            ex("Escribe todos los números que hay entre 296 y 300.", "297, 298 y 299", "Son los que están después de 296 y antes de 300."),
            ex("¿Está el 450 entre 400 y 500?", "Sí", "450 es mayor que 400 y menor que 500."),
            ex("¿Está el 612 entre 300 y 600?", "No", "612 es mayor que 600."),
        ],
        "understand": [
            ex("¿Cuántos números hay entre 120 y 125, sin contar los límites?", "4", "Son 121, 122, 123 y 124."),
            ex("¿Es el 500 un número que está entre 500 y 510?", "No", "Los límites no cuentan."),
            ex("Un número está entre 480 y 490 y termina en 3. ¿Cuál es?", "483", "En ese rango, solo 483 termina en 3."),
        ],
        "apply": [
            ex("Escribe todos los números que hay entre 697 y 702.", "698, 699, 700 y 701", "Son los que están después de 697 y antes de 702."),
            ex("Un número está entre 360 y 370 y tiene 4 unidades. ¿Cuál es?", "364", "Es el único del rango con 4 unidades."),
            ex("Un número está entre 600 y 700 y sus tres cifras son iguales. ¿Cuál es?", "666", "Si las tres cifras son iguales y las centenas son 6, el número es 666."),
        ],
        "reason": [
            ex("Rita dice que entre 99 y 101 no hay ningún número. ¿Tiene razón?", "No", "Entre 99 y 101 está el 100."),
            ex("¿Qué número hay entre 450 y 452? ¿Y entre 450 y 451?", "451; ninguno", "Entre 450 y 452 solo está 451. Entre 450 y 451 no hay números naturales."),
        ],
        "challenge": [
            ex("Un número está entre 850 y 860 y la suma de sus decenas y unidades es 8. ¿Cuál es?", "853", "Las decenas son 5, entonces las unidades son 3."),
            ex("¿Cuántos números entre 100 y 200 tienen 5 decenas?", "10", "Son 150, 151, 152, 153, 154, 155, 156, 157, 158 y 159."),
        ],
    },
    context=[ex("Anita vive en una casa cuyo número está entre 411 y 413. ¿Qué número tiene?", "412", "Es el único número entre 411 y 413.")],
    selfcheck=[
        ex("Escribe el número que hay entre 89 y 91.", "90", "Es el único número entre 89 y 91."),
        ex("¿Hay números entre 700 y 701?", "No", "No hay números naturales entre dos números seguidos."),
        ex("Escribe todos los números entre 508 y 512.", "509, 510 y 511", "Son los que están después de 508 y antes de 512."),
    ],
    open_task=task(
        "Resuelve estas tres pistas. A: un número entre 340 y 350 que termine en 8. B: todos los números entre 995 y 1.000. C: el número par que está entre 704 y 708. Escribe cómo comprobaste cada uno.",
        "A: 348, porque está entre 340 y 350 y termina en 8. B: 996, 997, 998 y 999. C: 706, porque entre 704 y 708 solo están 705, 706 y 707, y el único par es 706.",
        ["resuelve las tres pistas", "no incluye los límites", "comprueba cada pista", "escribe una frase de comprobación"],
        ["respuestas en el cuaderno", "frases de comprobación"],
        ["incluir los límites", "olvidar una pista"],
        "Pide que repita cada pista y compruebe con el número encontrado; si hay error, que escriba la lista completa del rango y luego elija.",
    ),
    reinforce="Escribe todos los números entre 205 y 212 y subraya los que terminan en 0, 5 y 8.",
    extend="¿Cuántos números hay entre 300 y 400, sin contar los límites? Piensa en una forma de saberlo sin escribirlos todos.",
)
