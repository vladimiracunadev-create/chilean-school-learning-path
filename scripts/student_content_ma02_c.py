"""Student material for 2.º básico Matemática, OA 02 (lectura y representación) y OA 03 (comparación y orden)."""
from __future__ import annotations

from student_content_ma02_a import OA2, bars, words
from student_lessons import arith, ex, register

OA3 = "MA02 OA 03"
KEY = "Clave de dibujo: ▮ es una barra de 10 y ● es un cubo de 1."


def sign(a: int, b: int) -> str:
    return ">" if a > b else "<" if a < b else "="


def cmp_ex(a: int, b: int, why: str) -> dict:
    return ex(f"Escribe >, < o = entre los números: {a} __ {b}.", f"{a} {sign(a, b)} {b}", why)


register(
    OA2, 1,
    materials=f"40 fichas o botones por pareja y hoja con las colecciones de este cuaderno. {KEY}",
    use="Aprenderé a contar colecciones grandes organizándolas en grupos de 10. Sirve para contar rápido y sin perder la cuenta cuando hay muchas cosas.",
    prior=["Sé contar objetos hasta 20.", "Sé que diez unidades forman una decena."],
    explain=[
        "Cuando hay muchas cosas desordenadas, contar una por una es fácil de arruinar: puedes saltarte una o contar dos veces la misma. Una forma segura es formar grupos de 10 y contar cuántos grupos hay y cuántas sobran.",
        "Si agrupas 10 fichas, ya tienes una decena. Con tres grupos de diez y 4 fichas sueltas, cuentas: 10, 20, 30 y luego 31, 32, 33, 34. El número es 34. Las decenas se cuentan de 10 en 10 y las unidades sueltas de 1 en 1.",
        "Después de contar, escribe el número con cifras: la cifra de la izquierda dice cuántas decenas y la de la derecha cuántas unidades sueltas. En 34, el 3 son tres decenas y el 4 son cuatro unidades. También puedes leerlo en palabras: treinta y cuatro.",
    ],
    vocab=[("decena", "grupo de 10 objetos"), ("unidad", "un objeto suelto"), ("agrupar", "juntar objetos para contarlos más fácil"), ("colección", "conjunto de objetos que quiero contar"), ("cifra", "cada número que forma un número, como el 3 y el 4 en 34")],
    worked=[
        {"title": "Agrupar fichas", "problem": "Hay 3 grupos de 10 fichas y 4 fichas sueltas. ¿Cuántas fichas hay?", "steps": ["Cuento los grupos de 10: 10, 20, 30.", "Sigo con las sueltas: 31, 32, 33, 34.", "Escribo el número: 3 decenas y 4 unidades es 34.", "Lo leo: treinta y cuatro."], "answer": "34 fichas"},
        {"title": "Formar decenas en una colección desordenada", "problem": "Hay 27 botones revueltos. ¿Cuántos grupos de 10 puedo formar y cuántos quedan sueltos?", "steps": ["Con 27 botones separo grupos de 10: uno (10), dos (20).", "Con los 7 que quedan no alcanza a otro grupo.", "Tengo 2 grupos de 10 y 7 sueltos.", "Compruebo: 20 + 7 = 27."], "answer": "2 decenas y 7 unidades"},
    ],
    mistakes=[
        {"wrong": "Contar 3 grupos de 10 y 4 sueltas como 7.", "why": "Se suma la cantidad de grupos con las sueltas sin recordar que cada grupo vale 10.", "fix": "Cuenta de 10 en 10 los grupos y luego de 1 en 1 las sueltas: 10, 20, 30, 31, 32, 33, 34."},
        {"wrong": "Escribir 43 para 3 decenas y 4 unidades.", "why": "Se invierte el orden de las cifras.", "fix": "La cifra de las decenas va primero: 3 decenas y 4 unidades se escribe 34."},
    ],
    tiers={
        "recovery": [
            arith("Hay 2 grupos de 10 fichas y 3 fichas sueltas. ¿Cuántas fichas hay?", "2*10+3", "Dos decenas son 20 y con 3 sueltas son 23."),
            arith("Hay 4 grupos de 10 lápices y 1 lápiz suelto. ¿Cuántos lápices hay?", "4*10+1", "Cuatro decenas son 40 y con 1 más son 41."),
            arith("Hay 1 grupo de 10 tapas y 8 tapas sueltas. ¿Cuántas tapas hay?", "1*10+8", "Una decena son 10 y con 8 más son 18."),
        ],
        "understand": [
            ex("En 36, ¿cuántas decenas y cuántas unidades hay?", "3 decenas y 6 unidades", "La cifra de la izquierda dice las decenas y la derecha las unidades."),
            ex("Escribe en palabras el número 42.", words(42), "El 4 de la izquierda es cuarenta y el 2 es dos."),
            ex("Una colección tiene 5 decenas y 0 unidades sueltas. ¿Qué número es?", "50", "Cinco decenas son 50."),
        ],
        "apply": [
            ex("Tengo 28 botones. ¿Cuántos grupos de 10 puedo formar y cuántos sobran?", "2 grupos de 10 y 8 sueltos", "Dos grupos usan 20 botones y quedan 8."),
            ex("Tengo 45 fichas. Armo todos los grupos de 10 que puedo. ¿Cuántos grupos y cuántas sueltas hay?", "4 grupos y 5 sueltas", "Cuatro grupos usan 40 fichas y quedan 5."),
            arith("En una bandeja hay 3 filas de 10 galletas y 6 galletas en un plato. ¿Cuántas galletas hay?", "3*10+6", "Tres filas de 10 son 30 y con 6 galletas son 36."),
        ],
        "reason": [
            ex("Ana contó 3 decenas y 4 unidades y escribió 43. ¿Qué error cometió y cuál es el número correcto?", "Invirtió las cifras; el número es 34", "Las decenas se escriben primero: 3 decenas y 4 unidades es 34."),
            ex("Dos grupos de 10 y 12 sueltas. Juan dice que son 32. Julia dice que son 22. ¿Quién tiene razón?", "Juan", "Con 12 sueltas se puede formar otra decena: 20 + 12 = 32."),
        ],
        "challenge": [
            ex("Hay 50 fichas. Quiero hacer todos los grupos de 10 posibles. ¿Cuántos grupos obtengo y cuántas fichas sobran?", "5 grupos y 0 sueltas", "Cinco decenas son 50, y no sobra ninguna."),
            ex("Una caja tiene 4 grupos de 10 clips. Otra caja tiene 2 grupos de 10 clips y 15 clips sueltos. ¿Qué caja tiene más clips?", "La primera caja", "La primera tiene 40 clips y la segunda 20 + 15 = 35; 40 es mayor que 35."),
        ],
    },
    context=[arith("En el recreo se juntaron semillas de jacarandá en un frasco: 3 puñados de 10 y 7 semillas más. ¿Cuántas semillas hay en total?", "3*10+7", "Tres puñados de 10 son 30; sumando 7 suman 37.")],
    selfcheck=[ex("Hay 2 decenas y 9 unidades. ¿Qué número es?", "29", "20 + 9 = 29."), ex("¿Cuántas decenas hay en 47?", "4", "El 4 representa 4 decenas, es decir, 40."), ex("Escribe en palabras 31.", words(31), "Treinta es 3 decenas y se agrega «y uno».")],
    open_task={
        "statement": "Toma 37 fichas, botones o garbanzos (o dibújalos). Forma todos los grupos de 10 que puedas, anota cuántos grupos y cuántas sueltas quedan, escribe el número con cifras y en palabras.",
        "example": "Hice 3 grupos de 10 y quedaron 7 sueltas. El número es 37, en palabras treinta y siete. Comprobé: 10, 20, 30, 31, 32, 33, 34, 35, 36, 37.",
        "criteria": ["forma grupos de 10 correctos", "declara decenas y sueltas", "escribe cifras y palabras", "comprueba contando"],
        "evidence": ["foto o dibujo de los grupos", "registro de decenas y unidades", "número escrito con cifras y palabras"],
        "errors": ["contar los grupos como si valieran 1", "olvidar sueltas", "escribir las cifras al revés"],
        "feedback": "Reconoce el orden de los grupos y pide que cuente de 10 en 10 señalando cada grupo; si invirtió las cifras, que lea su número en voz alta y lo compare con los grupos.",
    },
    reinforce="Con 20 fichas arma grupos de 10 y practica agregando 1, 2, 3… sueltas hasta llegar a 29.",
    extend="Con 50 fichas, ¿cuántas formas distintas hay de repartirlas en dos montones de decenas completas? Escribe tus resultados.",
)

register(
    OA2, 2,
    materials=f"Lápiz y cuaderno cuadriculado. {KEY} Se dibuja con ▮ y ● o con barras y puntos.",
    use="Aprenderé a pasar del material al dibujo con barras de decenas y cubos de unidades. Sirve para registrar cantidades y explicar cómo las armé.",
    prior=["Sé contar colecciones agrupando en 10.", "Sé que un número tiene decenas y unidades."],
    explain=[
        "Un dibujo bien hecho dice la misma cantidad que el material. Para no dibujar 34 puntos uno a uno, dibujamos una barra por cada grupo de 10 y un punto por cada unidad suelta. Así 34 se dibuja con 3 barras y 4 puntos.",
        "Para leer un dibujo hacemos lo contrario: contamos las barras de 10 en 10 y luego los puntos de 1 en 1. El dibujo ▮ ▮ | ● ● ● ● muestra 20 + 4, que es 24.",
        "Dibujar rápido tiene una regla: las barras se hacen todas iguales y los puntos se separan de las barras. Así se ve de inmediato cuántas decenas y cuántas unidades hay, y es más difícil equivocarse.",
    ],
    vocab=[("barra", "dibujo que vale 10"), ("punto o cubo", "dibujo que vale 1"), ("representar", "mostrar un número con material, dibujo o símbolo"), ("pictórico", "hecho con dibujos"), ("material concreto", "objetos que puedo tocar, como fichas o cubos")],
    worked=[
        {"title": "Dibujar un número", "problem": "Dibuja el número 23 con barras y puntos.", "steps": ["23 tiene 2 decenas y 3 unidades.", "Dibujo 2 barras: ▮ ▮.", "Dibujo 3 puntos: ● ● ●.", f"Mi dibujo queda así: {bars(23)}."], "answer": bars(23)},
        {"title": "Leer un dibujo", "problem": f"¿Qué número muestra este dibujo? {bars(41)}", "steps": ["Cuento las barras: 4 barras son 40.", "Cuento los puntos: hay 1.", "Sumo: 40 + 1 = 41.", "Verifico que todas las barras estén contadas."], "answer": "41"},
    ],
    mistakes=[
        {"wrong": "Dibujar 7 puntos para 17.", "why": "Se dibuja sólo la cifra de las unidades.", "fix": "17 tiene 1 decena y 7 unidades: una barra y 7 puntos."},
        {"wrong": "Contar cada barra como 1.", "why": "No se recuerda que una barra representa un grupo de 10.", "fix": "Cuenta las barras de 10 en 10: 10, 20, 30; luego suma los puntos."},
    ],
    tiers={
        "recovery": [
            ex(f"¿Qué número muestra este dibujo? {bars(32)}", "32", "Tres barras son 30 y dos puntos son 2."),
            ex(f"¿Qué número muestra este dibujo? {bars(15)}", "15", "Una barra es 10 y cinco puntos son 5."),
            ex(f"¿Qué número muestra este dibujo? {bars(50)}", "50", "Cinco barras son 50 y no hay puntos."),
        ],
        "understand": [
            ex("¿Cuántas barras y cuántos puntos necesito para dibujar 26?", "2 barras y 6 puntos", "26 tiene 2 decenas y 6 unidades."),
            ex("¿Qué representa cada barra y cada punto en estos dibujos?", "Barra = 10, punto = 1", "Una barra reúne un grupo de 10 unidades."),
            ex(f"Dibujo A: {bars(24)}. Dibujo B: {bars(42)}. ¿Muestran el mismo número?", "No", "A es 20 + 4 = 24 y B es 40 + 2 = 42."),
        ],
        "apply": [
            ex("Dibuja 38 con barras y puntos. Escribe cuántas barras y cuántos puntos usaste.", f"{bars(38)}; 3 barras y 8 puntos", "38 tiene 3 decenas y 8 unidades."),
            ex(f"Cuenta este dibujo y escribe el número: {bars(47)}.", "47", "Cuatro barras son 40 y siete puntos son 7."),
            ex("Tengo 45 fichas. Dibuja cómo las agruparías.", f"{bars(45)}", "Cuatro grupos de 10 y cinco sueltas."),
        ],
        "reason": [
            ex(f"Marta dibujó 5 puntos y 1 barra para el número 51. ¿Es correcto? {bars(15)}", "No; el dibujo muestra 15", "La barra vale 10 y los 5 puntos valen 5: 10 + 5 = 15."),
            ex("Pedro dice que 3 barras y 2 puntos es 5. ¿Qué error comete y cuál es la respuesta correcta?", "Suma las piezas; el número es 32", "Cada barra vale 10: 30 + 2 = 32."),
        ],
        "challenge": [
            ex("Dibuja 30 de dos maneras: una con 3 barras y otra con 2 barras y puntos. ¿Cuántos puntos necesitas en la segunda?", "10 puntos", "Dos barras son 20; para llegar a 30 faltan 10 unidades."),
            ex("Tengo 4 barras y 12 puntos. ¿Qué número es?", "52", "Cuatro barras son 40 y 12 puntos son 12: 40 + 12 = 52."),
        ],
    },
    context=[arith("En una bodega hay 3 cajas con 10 vasos cada una y 8 vasos sueltos. Dibuja una barra por cada caja y un punto por cada vaso suelto. ¿Cuántos vasos hay?", "3*10+8", "Tres cajas son 30 y 8 sueltos suman 38.")],
    selfcheck=[ex(f"¿Qué número muestra {bars(26)}?", "26", "Dos barras son 20 y 6 puntos son 6."), ex("¿Cuántas barras se usan para dibujar 40?", "4", "Cuatro decenas forman 40."), ex("¿Qué valor tiene un punto en estos dibujos?", "1", "Un punto es una unidad.")],
    open_task={
        "statement": "Elige uno de estos números: 31, 36 o 48. Dibújalo con barras y puntos, escribe cuántas decenas y unidades tiene y explica a otra persona cómo lo contaste.",
        "example": "Elegí 36. Dibujé ▮ ▮ ▮ | ● ● ● ● ● ●. Tiene 3 decenas y 6 unidades: 30 + 6 = 36. Conté las barras de 10 en 10 y luego los puntos.",
        "criteria": ["el dibujo tiene la cantidad de barras y puntos correcta", "separa decenas y unidades", "explica el conteo con 10 en 10 y de 1 en 1"],
        "evidence": ["dibujo en el cuaderno", "frase con decenas y unidades", "explicación oral o escrita"],
        "errors": ["usar sólo puntos", "no separar barras y puntos", "dibujar una barra por cada unidad"],
        "feedback": "Si el dibujo no coincide con el número, que cuente cada parte en voz alta y compare con la cifra; reconoce el esfuerzo de explicar.",
    },
    reinforce="Arma con cubos 14, 23 y 31 y dibuja cada uno con barras y puntos.",
    extend="Dibuja el mismo número con 4 barras y puntos de dos maneras diferentes (por ejemplo, 45 con 3 barras y 15 puntos).",
)

register(
    OA2, 3,
    materials=f"Tarjetas con los números 12, 27, 35, 46 y 50 en este cuaderno, lápiz y regla. {KEY}",
    use="Aprenderé a representar un mismo número de dos maneras y a leerlo en palabras. Sirve para entender un número cuando lo veo escrito y para decirlo bien.",
    prior=["Sé dibujar números con barras y puntos.", "Sé que un número tiene decenas y unidades."],
    explain=[
        "Un número puede mostrarse de muchas maneras: con cifras, con palabras, con material o con dibujo. Todas dicen lo mismo. Por ejemplo, 35 se escribe 35, se lee treinta y cinco, se arma con 3 grupos de 10 y 5 cubos, y se dibuja ▮ ▮ ▮ | ● ● ● ● ●.",
        "Para pasar del símbolo a dos representaciones, primero separa el número en decenas y unidades. En 35, el 3 está en el lugar de las decenas y el 5 en el de las unidades. Después elige dos maneras: por ejemplo, el dibujo y la expresión 30 + 5.",
        "Leer los números en palabras tiene reglas. Del 10 al 15 son palabras especiales (diez, once, doce, trece, catorce, quince). Del 16 al 19 se dice dieciséis, diecisiete, dieciocho, diecinueve. Desde el 31 se usa «y»: treinta y uno, cuarenta y dos.",
    ],
    vocab=[("símbolo", "el número escrito con cifras"), ("representación", "una manera de mostrar un número"), ("en palabras", "el número escrito con letras"), ("expresión aditiva", "suma que muestra las partes del número, como 30 + 5"), ("equivalente", "que vale lo mismo")],
    worked=[
        {"title": "Una cifra, dos representaciones", "problem": "Representa el número 46 de dos maneras.", "steps": ["46 tiene 4 decenas y 6 unidades.", f"Dibujo: {bars(46)}.", "Expresión: 40 + 6 = 46.", f"En palabras: {words(46)}."], "answer": f"{bars(46)}; 40 + 6; {words(46)}"},
        {"title": "Decir un número", "problem": "Lee en voz alta el número 17 y 31 y escríbelos con letras.", "steps": ["17 está entre 16 y 19, por lo que se dice diecisiete.", "31 está sobre el 30, así que se dice treinta y uno.", "Reviso que en 31 aparece «y»."], "answer": f"{words(17)}; {words(31)}"},
    ],
    mistakes=[
        {"wrong": "Escribir «treinta cinco» sin la «y» para 35.", "why": "Se omite la unión que se usa desde el 31.", "fix": "Desde el 31 se dice «treinta y cinco»."},
        {"wrong": "Representar 27 con 7 barras y 2 puntos.", "why": "Se intercambian decenas y unidades.", "fix": "La cifra de la izquierda indica las barras: 2 barras y 7 puntos."},
    ],
    tiers={
        "recovery": [
            ex("Escribe con letras el número 12.", words(12), "Del 10 al 15 los nombres son especiales."),
            ex("Escribe con letras el número 24.", words(24), "Del 21 al 29 se escribe en una palabra: veinticuatro."),
            ex("Escribe con letras el número 50.", words(50), "Cinco decenas se dicen cincuenta."),
        ],
        "understand": [
            ex(f"Une cada representación con su número: A) {bars(27)} B) {bars(35)}. ¿Qué número muestra A?", "27", "Dos barras y siete puntos: 20 + 7."),
            ex("¿Qué número escrito con cifras es «cuarenta y tres»?", "43", "Cuarenta son 4 decenas y tres son 3 unidades."),
            ex("¿Cuál es la expresión aditiva de 38?", "30 + 8", "38 tiene 3 decenas y 8 unidades."),
        ],
        "apply": [
            ex("Representa 42 con un dibujo y con una expresión aditiva.", f"{bars(42)}; 40 + 2", "Cuatro barras y dos puntos; 40 + 2 = 42."),
            ex("Escribe con cifras y con palabras el número que tiene 3 decenas y 9 unidades.", f"39; {words(39)}", "30 + 9 = 39."),
            ex("Dibuja 16 con barras y puntos y escríbelo con palabras.", f"{bars(16)}; {words(16)}", "Una barra y seis puntos; dieciséis."),
        ],
        "reason": [
            ex("Sandra escribió «veinte y tres» para 23. ¿Es correcto? ¿Cómo se escribe bien?", "No; se escribe veintitrés", "Del 21 al 29 se escribe en una palabra."),
            ex("Rodrigo dice que 40 + 5 y 5 + 40 representan números distintos. ¿Tiene razón?", "No", "Ambas expresiones suman 45; el orden de los sumandos no cambia el total."),
        ],
        "challenge": [
            ex("Un número tiene 4 decenas y su cifra de unidades es el doble de 3. ¿Cuál es el número?", "46", "El doble de 3 es 6; 4 decenas y 6 unidades es 46."),
            ex("Escribe tres representaciones distintas del número 29.", f"{bars(29)}; 20 + 9; {words(29)}", "Todas muestran 2 decenas y 9 unidades."),
        ],
    },
    context=[ex("El número de la camiseta de un jugador es 33. Escríbelo con palabras y dibújalo con barras y puntos.", f"{words(33)}; {bars(33)}", "33 tiene 3 decenas y 3 unidades; se dice treinta y tres.")],
    selfcheck=[ex("Escribe con cifras «quince».", "15", "Una decena y cinco unidades."), ex("¿Qué número se dibuja con 4 barras y 8 puntos?", "48", "40 + 8 = 48."), ex("Escribe con palabras 44.", words(44), "Cuarenta son 4 decenas y cuatro son 4 unidades.")],
    open_task={
        "statement": "Elige el número 28, el 39 o el 45. Muéstralo de tres maneras: con un dibujo de barras y puntos, con una expresión aditiva y con palabras. Explica en una frase cuál te resultó más fácil.",
        "example": f"Elegí 39. Dibujo: {bars(39)}. Expresión: 30 + 9. Palabras: {words(39)}. Me resultó más fácil el dibujo porque veo las decenas y las unidades.",
        "criteria": ["las tres representaciones muestran el mismo número", "usa 3 barras y 9 puntos (o las que correspondan)", "escribe bien el nombre del número"],
        "evidence": ["dibujo", "expresión aditiva", "palabras", "frase de reflexión"],
        "errors": ["omitir la «y» después de 30", "intercambiar decenas y unidades"],
        "feedback": "Pide leer las tres representaciones en voz alta y comprobar que dicen lo mismo; si una no coincide, que identifique cuál y la corrija.",
    },
    reinforce="Haz tarjetas con 10 números del 10 al 50 y escribe al reverso su nombre.",
    extend="Descubre qué números tienen el mismo dibujo si se agregan o quitan 10 puntos y agrupan en una barra. Usa 26 como ejemplo.",
)

register(
    OA2, 4,
    materials=f"Tarjetas con 30, 40, 60, 100 y 0 en este cuaderno; fichas y cuadro de decenas y unidades. {KEY}",
    use="Aprenderé qué significa el cero en un número y cómo se leen y representan los números con cero final. Sirve para no confundir 30 con 3 ni 0 con «nada».",
    prior=["Sé representar números con barras y puntos.", "Sé leer números hasta 50."],
    explain=[
        "El cero sirve para mostrar que no hay unidades en un lugar. En el número 30 hay 3 decenas y 0 unidades: tres barras y ningún punto. Si borras el 0, el número cambia a 3, que es muy distinto.",
        "Los números con cero final se cuentan sólo en decenas: 10, 20, 30, 40, 50, 60, 70, 80, 90 y 100. Se leen diez, veinte, treinta, cuarenta, cincuenta, sesenta, setenta, ochenta, noventa y cien. En el dibujo, son sólo barras.",
        "El número 0 se usa cuando no hay nada que contar. Si tienes 0 fichas, no tienes ninguna. Tampoco hay que confundir 0 con otras cifras: 05 no se usa para escribir 5, porque el cero a la izquierda no agrega valor.",
    ],
    vocab=[("cero", "la cifra que indica que no hay nada en ese lugar"), ("cero final", "cero en el lugar de las unidades, como en 40"), ("cien", "diez decenas"), ("ninguno", "cantidad cero"), ("lugar", "posición de una cifra: unidades o decenas")],
    worked=[
        {"title": "Un número con cero", "problem": "Representa 60 con barras y explica qué significa el 0.", "steps": ["60 tiene 6 decenas.", f"Dibujo: {bars(60)}.", "El 0 dice que no hay unidades sueltas.", "Lo leo: sesenta."], "answer": f"{bars(60)}; 6 decenas y 0 unidades"},
        {"title": "Cuando no hay nada", "problem": "Tengo 0 fichas y recibo 2 decenas completas. ¿Cuántas fichas tengo?", "steps": ["Empiezo con 0, que significa ninguna.", "Dos decenas son 2 grupos de 10: 10 + 10.", "0 + 20 = 20."], "answer": "20 fichas"},
    ],
    mistakes=[
        {"wrong": "Escribir 4 para cuarenta.", "why": "Se pierde el cero que indica 0 unidades.", "fix": "Cuarenta son 4 decenas y 0 unidades: se escribe 40."},
        {"wrong": "Pensar que 30 tiene 30 barras.", "why": "Se confunde el número con la cantidad de barras.", "fix": "30 se dibuja con 3 barras."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas barras tiene el número 40?", "4 barras", "Cuarenta son 4 decenas."),
            ex("Escribe en palabras el número 70.", words(70), "Siete decenas se dicen setenta."),
            ex("¿Cuántas unidades sueltas tiene el número 60?", "0 unidades", "El 0 de 60 significa que no hay unidades."),
        ],
        "understand": [
            ex("¿Cuál es la diferencia entre 3 y 30?", "3 son tres unidades y 30 son tres decenas", "El cero cambia el lugar del 3."),
            ex("Completa: 5 decenas y 0 unidades es __.", "50", "5 × 10 = 50."),
            ex("Escribe el número que viene después de 99.", "100", "Diez decenas forman cien."),
        ],
        "apply": [
            ex("Cuenta de 10 en 10 y completa: 10, 20, 30, __, 50, __.", "40 y 60", "Se suma 10 en cada paso."),
            arith("Tengo 3 billetes de $10 y recibo 2 billetes de $10. ¿Cuánto dinero tengo?", "30+20", "Cinco billetes de $10 son $50."),
            ex("Representa 80 con barras y escribe cuántos puntos necesitas.", f"{bars(80)}; 0 puntos", "Ocho decenas son 80 y no hay unidades sueltas."),
        ],
        "reason": [
            ex("Beto dice que 70 es lo mismo que 7. ¿Tiene razón?", "No", "70 son 7 decenas y 0 unidades; 7 son sólo 7 unidades."),
            ex("Ema escribió «cincuenta» con un 5. Corrígela.", "50", "Cincuenta son 5 decenas y 0 unidades; falta el cero."),
        ],
        "challenge": [
            ex("Si a 100 le quito 4 decenas, ¿cuánto queda?", "60", "100 − 40 = 60."),
            ex("Un número tiene 9 decenas y 0 unidades. Si le agrego una decena más, ¿qué número obtengo?", "100", "90 + 10 = 100."),
        ],
    },
    context=[ex("Un kiosco vende paquetes de 10 galletas. Si hay 9 paquetes llenos, ¿cuántas galletas hay? ¿Y si agregan 1 paquete más?", "90 galletas; con 1 paquete más, 100", "9 × 10 = 90 y 90 + 10 = 100.")],
    selfcheck=[ex("Escribe en cifras: ochenta.", "80", "Ocho decenas y cero unidades."), ex("¿Cuántas decenas hay en 100?", "10", "Cien son diez decenas."), ex("¿El 0 en 20 es nada?", "No; indica que hay 0 unidades", "El cero ocupa el lugar de las unidades.")],
    open_task={
        "statement": "Elige el 20, el 50 o el 90. Dibújalo con barras, escribe cuántas decenas y unidades tiene y explica con tus palabras por qué el 0 es necesario.",
        "example": f"Elegí 50: {bars(50)}. Tiene 5 decenas y 0 unidades. El 0 es necesario porque sin él el número sería 5 y no 50.",
        "criteria": ["el dibujo coincide con el número", "escribe decenas y unidades", "explica el papel del cero"],
        "evidence": ["dibujo", "registro de decenas y unidades", "explicación escrita"],
        "errors": ["dibujar puntos de más", "decir que el cero no sirve"],
        "feedback": "Comparar 5 y 50 con material ayuda a mostrar el valor del cero; reconoce las explicaciones que usan las barras.",
    },
    reinforce="Cuenta de 10 en 10 hasta 100 mostrando una barra por cada salto y escribe el número.",
    extend="Descubre qué pasa en la escritura de los números cuando se pasa de 99 a 100 y por qué aparece un tercer lugar.",
)
