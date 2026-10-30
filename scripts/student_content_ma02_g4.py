"""Student material for 2.º básico Matemática, OA 21 (tablas y gráficos de barra de juegos aleatorios) y OA 22 (pictogramas con escala y barras)."""
from __future__ import annotations

from collections import Counter

from student_content_ma02_g import task
from student_lessons import arith, ex, register

OA21, OA22 = "MA02 OA 21", "MA02 OA 22"


def barra(n: int) -> str:
    """Horizontal bar of n squares, one square per unit."""
    return "■" * n if n else "(vacía)"


def pic(symbol: str, n: int) -> str:
    return " ".join([symbol] * n) if n else "(nada)"


def filas(pairs: list[tuple[str, int]]) -> str:
    return " / ".join(f"{name}: {barra(value)} ({value})" for name, value in pairs)


DADO = [2, 6, 4, 4, 1, 6, 3, 4, 5, 6, 2, 4]
cd = Counter(DADO)
assert [cd[i] for i in range(1, 7)] == [1, 2, 1, 4, 1, 3] and sum(cd.values()) == 12
DADO_TXT = ", ".join(str(v) for v in DADO)
ESCALA = "Escala: cada cuadrito ■ vale 1 lanzamiento y las barras parten del 0."

# ================================================================ OA 21
register(
    OA21, 1,
    materials=f"Papel y lápiz. Lista de 12 lanzamientos de un dado: {DADO_TXT}. Con ella puedes hacer la tabla sin lanzar nada.",
    use="Aprenderé a ordenar los resultados de un juego en una tabla por categoría. Sirve para saber cuántas veces salió cada resultado y comprobar que no falta ninguno.",
    prior=["Sé hacer marcas de conteo.", "Sé qué es una frecuencia."],
    explain=[
        "Una tabla de resultados tiene una fila para cada categoría. En un dado, las categorías son los números del 1 al 6. En cada fila se anota cuántas veces salió ese número. Esa cantidad es la frecuencia.",
        "Para llenar la tabla, recorre la lista de lanzamientos de uno en uno. Por cada resultado, haz una marca en su fila. Al terminar, cuenta las marcas de cada fila y escribe el número.",
        "Siempre comprueba el total. La suma de todas las frecuencias debe ser igual al número de lanzamientos. Si tienes 12 lanzamientos, la suma debe dar 12. Si no da 12, revisa la lista de nuevo.",
    ],
    vocab=[("tabla", "forma ordenada de anotar datos en filas"), ("categoría", "cada grupo distinto, como el número 1 o el 2"), ("frecuencia", "cuántas veces salió una categoría"), ("total", "suma de todas las frecuencias"), ("aleatorio", "que depende del azar")],
    worked=[
        {"title": "Contar una categoría", "problem": f"En la lista {DADO_TXT}, ¿cuántas veces salió el 4?", "steps": ["Recorro la lista y marco cada 4.", f"Encuentro {cd[4]} cuatros.", f"Anoto {cd[4]} en la fila del 4."], "answer": f"{cd[4]} veces"},
        {"title": "Comprobar el total", "problem": f"La tabla completa dice 1:{cd[1]}, 2:{cd[2]}, 3:{cd[3]}, 4:{cd[4]}, 5:{cd[5]}, 6:{cd[6]}. ¿Está bien el total?", "steps": [f"Sumo: {cd[1]} + {cd[2]} + {cd[3]} + {cd[4]} + {cd[5]} + {cd[6]}.", "La suma es 12.", "Fueron 12 lanzamientos: coincide."], "answer": "Sí, el total es 12"},
    ],
    mistakes=[
        {"wrong": "Dejar de anotar un lanzamiento y no comprobar el total.", "why": "El total no coincide con los lanzamientos.", "fix": "Suma todas las frecuencias y compara con el número de lanzamientos."},
        {"wrong": "Anotar el mismo lanzamiento en dos filas.", "why": "Una marca por lanzamiento.", "fix": "Cada resultado va en una sola fila."},
    ],
    tiers={
        "recovery": [
            ex(f"En la lista {DADO_TXT}, ¿cuántas veces salió el 6?", str(cd[6]), "Se cuentan los 6 de la lista."),
            ex(f"En la lista {DADO_TXT}, ¿cuántas veces salió el 1?", str(cd[1]), "Se cuenta el único 1."),
            ex("En una tabla, el 5 tiene la marca |. ¿Cuántas veces salió el 5?", "1", "Una marca es una vez."),
        ],
        "understand": [
            ex("¿Cuántas filas necesita una tabla para los resultados de un dado común?", "6", "Una fila por cada número del 1 al 6."),
            ex("¿Qué indica el número que escribes en cada fila?", "La frecuencia", "Dice cuántas veces salió esa categoría."),
            ex("¿Con qué número debe coincidir la suma de las frecuencias?", "Con el número de lanzamientos", "Cada lanzamiento se anota una vez."),
        ],
        "apply": [
            ex(f"En la lista {DADO_TXT}, ¿cuántas veces salió el 2?", str(cd[2]), "Se cuentan los 2 de la lista."),
            ex(f"Completa: en la lista {DADO_TXT}, ¿cuántas veces salió el 3 y cuántas el 5?", f"3: {cd[3]} vez; 5: {cd[5]} vez", "Cada uno aparece una sola vez."),
            arith("Una tabla de una moneda lanzada 10 veces dice: cara 6. ¿Cuántos sellos salieron?", "10-6", "El total de lanzamientos menos las caras."),
        ],
        "reason": [
            ex("Una tabla dice 1:3, 2:2, 3:1, 4:2, 5:1, 6:2 para 10 lanzamientos. Rita dice que está bien. ¿Qué error ves?", "Suma 11, no 10; hay una marca de más", "3 + 2 + 1 + 2 + 1 + 2 = 11."),
            ex("Hugo cambió una marca del 5 al 4 para que el 4 «saliera más». ¿Qué hizo mal?", "Cambió el dato real", "Los resultados deben anotarse como salieron."),
        ],
        "challenge": [
            ex("Se lanzó un dado 15 veces. El 1 salió 2 veces, el 2 salió 3, el 3 salió 4, el 4 salió 2 y el 5 salió 1. ¿Cuántas veces salió el 6?", "3", "15 − (2 + 3 + 4 + 2 + 1) = 3."),
            ex(f"En la lista {DADO_TXT}, ¿cuántos lanzamientos fueron mayores que 4?", "4", "Son los 6 (3 veces) y el 5 (1 vez): 3 + 1 = 4."),
        ],
    },
    context=[ex("Un grupo anotó los resultados de 10 lanzamientos de moneda: cara 4 y sello 6. ¿Cuál categoría tiene la mayor frecuencia?", "Sello", "6 es mayor que 4.")],
    selfcheck=[
        ex("¿Qué se escribe en cada fila de la tabla?", "La categoría y su frecuencia", "Dice qué salió y cuántas veces."),
        ex("Si hubo 12 lanzamientos, ¿cuánto debe sumar la tabla?", "12", "Se anota un lanzamiento una sola vez."),
        ex(f"En la lista {DADO_TXT}, ¿qué número salió más veces?", "El 4", "Salió 4 veces."),
    ],
    open_task=task(
        f"Usa esta lista de 12 lanzamientos de un dado: {DADO_TXT}. Haz una tabla con las filas 1 a 6, anota las marcas, escribe la frecuencia de cada número y comprueba que el total sea 12.",
        f"1: 1 vez; 2: 2 veces; 3: 1 vez; 4: 4 veces; 5: 1 vez; 6: 3 veces. Total: 1 + 2 + 1 + 4 + 1 + 3 = 12.",
        ["hace una fila para cada número del 1 al 6", "cuenta bien las frecuencias", "comprueba que el total sea 12", "no cambia los datos"],
        ["tabla completa", "comprobación del total"],
        ["omitir un lanzamiento", "no comprobar el total"],
        "Pide releer la lista contando en voz alta. Reconoce la comprobación con la suma.",
    ),
    reinforce="Lanza un dado 10 veces y llena una tabla de 6 filas.",
    extend="Lanza una moneda 12 veces y haz su tabla. Compara cuántas veces salió cada una.",
)

register(
    OA21, 2,
    materials="Cubos, fichas o cuadraditos de papel del mismo tamaño. Si no tienes, dibuja cuadraditos iguales. Las frecuencias están escritas en cada ejercicio.",
    use="Aprenderé a construir un gráfico de barras con bloques desde una tabla. Sirve para ver de un vistazo qué categoría tiene más.",
    prior=["Sé hacer una tabla de frecuencias.", "Sé comparar números."],
    explain=[
        "Un gráfico de barras muestra la frecuencia de cada categoría con una torre o una barra. Cuanto más alta es la torre, más veces salió esa categoría. Una barra de 5 bloques significa 5 veces.",
        "Para construirlo, todas las torres deben partir desde la misma base, como el piso. Deja el mismo espacio entre una torre y la siguiente. Cada bloque debe ser del mismo tamaño.",
        "Si las frecuencias son 2, 5 y 3, haces una torre de 2, otra de 5 y otra de 3 bloques. Escribe debajo el nombre de cada categoría. Así puedes comparar las alturas.",
    ],
    vocab=[("barra", "torre o rectángulo que muestra una frecuencia"), ("base", "línea desde donde parten todas las barras"), ("bloque", "cuadrito que vale una unidad"), ("categoría", "nombre de lo que se cuenta"), ("altura", "cuán alta es una barra")],
    worked=[
        {"title": "Torres desde una tabla", "problem": "La tabla de un juego con tres colores dice Rojo 2, Azul 5, Verde 3. Haz las torres.", "steps": ["Tomo 2 bloques para Rojo.", "Tomo 5 bloques para Azul.", "Tomo 3 bloques para Verde.", "Las pongo en la misma base y con el mismo espacio."], "answer": f"{filas([('Rojo', 2), ('Azul', 5), ('Verde', 3)])}"},
        {"title": "Leer las torres", "problem": f"Un gráfico muestra: {filas([('A', 4), ('B', 1), ('C', 6)])}. ¿Cuál categoría tiene más?", "steps": ["Comparo las alturas.", "C tiene 6 bloques.", "6 es el mayor número."], "answer": "La categoría C, con 6"},
    ],
    mistakes=[
        {"wrong": "Hacer las torres sin partir desde la misma base.", "why": "No se pueden comparar alturas.", "fix": "Todas las torres parten del mismo piso."},
        {"wrong": "Usar bloques de distinto tamaño.", "why": "Una torre puede parecer más alta aunque tenga menos bloques.", "fix": "Todos los bloques son iguales."},
    ],
    tiers={
        "recovery": [
            ex("Una barra tiene 4 bloques. ¿Cuántas veces salió esa categoría?", "4", "Un bloque por cada vez."),
            ex("En una tabla, el 3 salió 2 veces. ¿Cuántos bloques lleva su torre?", "2", "Un bloque por frecuencia."),
            ex(f"Gráfico: {filas([('Cara', 3), ('Sello', 5)])}. ¿Cuál torre es más alta?", "La de Sello", "5 es mayor que 3."),
        ],
        "understand": [
            ex("¿Desde dónde deben partir todas las torres?", "Desde la misma base", "Así se pueden comparar."),
            ex("¿Qué significa que una torre sea más alta que otra?", "Que esa categoría tiene mayor frecuencia", "Más bloques es más veces."),
            ex("¿Por qué todos los bloques deben ser iguales?", "Para que la altura muestre la frecuencia", "Bloques distintos engañan."),
        ],
        "apply": [
            ex("Para las frecuencias 4, 1 y 6, escribe cuántos bloques lleva cada torre en orden.", "4, 1 y 6 bloques", "Cada torre usa tantos bloques como su frecuencia."),
            arith("Un gráfico de bloques tiene torres de 3, 5 y 2. ¿Cuántos bloques hay en total?", "3+5+2", "Se suman las alturas."),
            ex(f"Gráfico: {filas([('X', 5), ('Y', 2), ('Z', 7)])}. ¿Cuál es la diferencia entre la torre más alta y la más baja?", "5", "7 − 2 = 5."),
        ],
        "reason": [
            ex("Ema hizo una torre de 3 bloques que parte más arriba que otra de 3 bloques. ¿Es correcto?", "No; todas deben partir de la misma base", "Si no, parecen de distinta altura."),
            ex("Teo dice que una torre de 6 bloques gruesos es más alta que una de 7 bloques delgados. ¿Qué error comete?", "Los bloques deben ser del mismo tamaño", "Con bloques distintos no se puede comparar."),
        ],
        "challenge": [
            ex("Representa 4, 1 y 6 con barras de bloques. Escribe cada fila de bloques con ■ y el nombre A, B y C.", f"A: {barra(4)} / B: {barra(1)} / C: {barra(6)}", "Cada ■ es un bloque."),
            ex("Un gráfico tiene dos torres: una de 8 bloques y otra de 3. Quieres que midan lo mismo. ¿Cuántos bloques debes agregar a la menor?", "5", "8 − 3 = 5."),
        ],
    },
    context=[ex("En un juego se anotó: Rojo 5 veces, Azul 2 veces y Verde 4 veces. ¿Cuántos bloques hay en total en las tres torres?", "11", "5 + 2 + 4 = 11.")],
    selfcheck=[
        ex("¿Cuántos bloques lleva una torre para una frecuencia de 7?", "7", "Un bloque por vez."),
        ex("¿Qué torre es la más alta en 2, 5 y 3?", "La de 5", "5 es el mayor número."),
        ex("¿Qué nombre debe llevar cada torre?", "El de su categoría", "Así se sabe qué muestra."),
    ],
    open_task=task(
        "Representa estos datos con barras de bloques (o cuadritos dibujados): Rojo 4, Azul 1, Verde 6. Dibuja cada barra desde la misma base, deja el mismo espacio y escribe el nombre debajo. Luego responde: ¿cuántos bloques más tiene la barra Verde que la Azul?",
        f"{filas([('Rojo', 4), ('Azul', 1), ('Verde', 6)])}. Verde tiene 6 − 1 = 5 bloques más que Azul.",
        ["dibuja tres barras con las alturas correctas", "las barras parten de la misma base", "escribe los nombres", "calcula la diferencia 5"],
        ["gráfico con bloques", "respuesta"],
        ["barras con base distinta", "bloques de distinto tamaño"],
        "Pide contar los bloques de cada barra. Reconoce el cuidado con la base común.",
    ),
    reinforce="Con 12 fichas, arma torres para 5, 3 y 4 y di cuál es más alta.",
    extend="Arma las torres para tu tabla de dado y escribe tres cosas que puedes decir al mirarlas.",
)

register(
    OA21, 3,
    materials=f"Papel cuadriculado o cuadrícula dibujada, regla y lápices. {ESCALA}",
    use="Aprenderé a dibujar un gráfico de barras en una cuadrícula con título, nombres y escala de uno. Sirve para presentar datos de forma clara.",
    prior=["Sé hacer barras con bloques.", "Sé leer tablas de frecuencias."],
    explain=[
        "Un gráfico de barras en cuadrícula tiene un eje de abajo con los nombres de las categorías y un eje del lado con una escala, que son números: 0, 1, 2, 3 y así. En nuestra escala de uno, cada cuadro vale 1.",
        "Para dibujar una barra, parte desde el 0 y pinta tantos cuadros como diga la frecuencia. Si la frecuencia es 7, pintas 7 cuadros hacia arriba. Todas las barras tienen el mismo ancho.",
        "No olvides el título, que dice de qué trata el gráfico. Un buen gráfico tiene título, nombres de categorías, escala con números y barras que parten del 0.",
    ],
    vocab=[("eje", "línea del gráfico con nombres o números"), ("escala", "números que dicen cuánto vale cada cuadro"), ("barra", "rectángulo que muestra una frecuencia"), ("título", "nombre del gráfico"), ("cuadro", "cada cuadradito de la cuadrícula")],
    worked=[
        {"title": "Dibujar una barra", "problem": "En un dado, el 5 salió 7 veces. ¿Cuántos cuadros pintas en su barra?", "steps": ["La escala vale 1 por cuadro.", "Parto desde el 0.", "Pinto 7 cuadros."], "answer": "7 cuadros"},
        {"title": "Revisar un gráfico", "problem": f"Un gráfico de moneda: {filas([('Cara', 6), ('Sello', 4)])}. Falta el título. ¿Qué título sirve?", "steps": ["El título dice qué se mide.", "Se trata de lanzar una moneda.", "Se puede escribir «Resultados de lanzar una moneda 10 veces»."], "answer": "Resultados de lanzar una moneda 10 veces"},
    ],
    mistakes=[
        {"wrong": "Empezar una barra desde el 1 en vez del 0.", "why": "La barra queda un cuadro más corta de lo debido.", "fix": "Todas las barras parten del 0."},
        {"wrong": "Olvidar el título o los nombres.", "why": "No se entiende de qué trata el gráfico.", "fix": "Escribe siempre un título y los nombres de las categorías."},
    ],
    tiers={
        "recovery": [
            ex("En la escala de uno, ¿cuántos cuadros pintas para una frecuencia de 4?", "4", "Cada cuadro vale 1."),
            ex("¿Desde qué número parte una barra?", "Desde el 0", "Todas parten de la base."),
            ex("¿Cuántos cuadros pintas para una frecuencia de 9?", "9", "Un cuadro por unidad."),
        ],
        "understand": [
            ex("¿Qué dice la escala de un gráfico?", "Cuánto vale cada cuadro", "En este caso vale 1."),
            ex("¿Para qué sirve el título?", "Para decir de qué trata el gráfico", "Sin título no se sabe qué muestra."),
            ex("¿Qué va en el eje de abajo?", "Los nombres de las categorías", "Así se sabe qué muestra cada barra."),
        ],
        "apply": [
            ex("Una tabla dice 1: 3, 2: 5, 3: 2. Escribe cuántos cuadros pinta cada barra, en orden.", "3, 5 y 2 cuadros", "Un cuadro por cada frecuencia."),
            ex("Hay que dibujar la barra de «Sello» con frecuencia 7. ¿Hasta qué número de la escala llega?", "Hasta el 7", "La barra parte del 0 y sube 7 cuadros."),
            arith("Una barra llega hasta el 8 y otra hasta el 3. ¿Cuántos cuadros más pintaste en la primera?", "8-3", "Se resta la menor a la mayor."),
        ],
        "reason": [
            ex("Pía comenzó la barra del 4 desde el 1 y la pintó hasta el 5. Dice que el 4 salió 5 veces. ¿Qué error hay?", "Comenzó en 1; sólo pintó 4 cuadros, por lo tanto salió 4 veces", "5 − 1 = 4."),
            ex("Un gráfico no tiene título. ¿Qué problema trae?", "No se sabe qué datos muestra", "El título explica el tema."),
        ],
        "challenge": [
            ex("Tabla: Cara 6, Sello 4. Dibuja el gráfico: escribe hasta qué número llega cada barra y cuál sería un buen título.", "Cara llega al 6, Sello al 4; título: «Resultados de 10 lanzamientos de moneda»", "6 + 4 = 10 lanzamientos."),
            ex("Una escala va de 0 a 8. Si hay una frecuencia de 9, ¿qué debes hacer?", "Agregar más números a la escala hasta el 9 o más", "La escala debe cubrir la barra más alta."),
        ],
    },
    context=[ex("Tabla del recreo: Rojo 5, Azul 2, Verde 6. ¿Hasta qué número de la escala llega la barra más alta?", "6", "6 es la mayor frecuencia.")],
    selfcheck=[
        ex("¿Desde qué número parte cada barra?", "Desde el 0", "Es la base del gráfico."),
        ex("¿Cuántos cuadros vale una frecuencia de 7 en escala de uno?", "7", "Cada cuadro vale 1."),
        ex("Nombra tres cosas que debe tener un gráfico de barras.", "Título, categorías y escala", "Esas partes lo hacen claro."),
    ],
    open_task=task(
        "Dibuja un gráfico de barras en una cuadrícula con esta tabla de 10 lanzamientos de un dado: el 2 salió 3 veces, el 4 salió 5 veces y el 6 salió 2 veces. Usa escala de uno y parte desde el 0. Escribe título, nombres de categorías y números de la escala.",
        "Título: Lanzamientos de un dado. Barras: 2 llega al 3, 4 llega al 5, 6 llega al 2. Escala: 0, 1, 2, 3, 4, 5. Total: 3 + 5 + 2 = 10.",
        ["usa escala de uno", "las barras parten del 0", "las alturas son 3, 5 y 2", "pone título, nombres y escala"],
        ["gráfico de barras", "título y escala"],
        ["comenzar en el 1", "olvidar el título"],
        "Pide contar los cuadros de cada barra. Reconoce el título claro y la escala completa.",
    ),
    reinforce="Pinta en una cuadrícula una barra de 5 cuadros, otra de 2 y otra de 7.",
    extend="Haz el gráfico de tu tabla de lanzamientos de dado y escribe qué categoría tiene la barra más alta.",
)

register(
    OA21, 4,
    materials="Papel y lápiz. Los gráficos están descritos con palabras y números en cada ejercicio.",
    use="Aprenderé a leer un gráfico de barras y a detectar errores que lo hacen engañoso. Sirve para no creer un gráfico mal hecho.",
    prior=["Sé dibujar barras desde el 0.", "Sé que el título y la escala son importantes."],
    explain=[
        "Un gráfico bien hecho muestra con claridad los datos. Tiene título, nombres de categorías, una escala con números y barras que parten del 0. La altura de cada barra es igual a su frecuencia.",
        "Un gráfico engaña cuando las barras parten de alturas distintas. Si una barra parte del 0 y otra del 3, aunque las dos terminen en 5, la segunda tiene menos cuadros pintados: sólo 5 − 3 = 2. Si miras sólo dónde terminan, parecen iguales. Los gráficos también engañan si faltan números en la escala.",
        "Al leer un gráfico, haz tres preguntas: ¿de qué trata?, ¿desde dónde parten las barras? y ¿qué dice la escala? Luego compara los números para responder.",
    ],
    vocab=[("engañoso", "que hace creer algo que no es cierto"), ("base", "línea desde donde parten las barras"), ("escala", "números del eje"), ("comparar", "decir cuál es mayor o menor"), ("error", "algo mal hecho")],
    worked=[
        {"title": "Detectar un error", "problem": "En un gráfico, una barra de «Cara» va del 0 al 5 y una barra de «Sello» va del 3 al 5. ¿Qué error hay?", "steps": ["Las dos terminan en el 5.", "Pero Sello parte del 3 y no del 0.", "Sello sólo tiene 5 − 3 = 2 cuadros pintados, aunque termine en el 5."], "answer": "Sello no parte desde el 0: parece valer 5, pero vale 2"},
        {"title": "Leer un gráfico", "problem": f"Gráfico: {filas([('1', 2), ('2', 4), ('3', 6)])}. ¿Cuántas veces más salió el 3 que el 1?", "steps": ["El 3 salió 6 veces.", "El 1 salió 2 veces.", "6 − 2 = 4."], "answer": "4 veces más"},
    ],
    mistakes=[
        {"wrong": "Decir que dos barras valen lo mismo sólo porque llegan a la misma altura, aunque parten de bases distintas.", "why": "No se mira dónde parte cada barra.", "fix": "Revisa que todas partan del 0 antes de comparar."},
        {"wrong": "Leer una barra sin mirar la escala.", "why": "La escala dice cuánto vale cada cuadro.", "fix": "Mira primero la escala."},
    ],
    tiers={
        "recovery": [
            ex(f"Gráfico: {filas([('Cara', 7), ('Sello', 3)])}. ¿Cuántas veces salió cara?", "7", "Se lee el número de la barra."),
            ex(f"En ese mismo gráfico, ¿cuántas veces salió sello?", "3", "Se lee el número de la barra."),
            ex("¿Desde dónde deben partir todas las barras?", "Desde el 0", "Es la base común."),
        ],
        "understand": [
            ex("¿Qué dos cosas ayudan a entender un gráfico antes de leer las barras?", "El título y la escala", "Dicen de qué trata y cuánto vale cada cuadro."),
            ex("¿Por qué engaña una barra que no parte desde el 0?", "Porque el número donde termina no dice cuánto vale", "Hay que contar los cuadros desde el 0."),
            ex("¿Qué debes revisar antes de comparar dos barras?", "Que partan de la misma base", "Si no, no son comparables."),
        ],
        "apply": [
            ex(f"Gráfico: {filas([('A', 5), ('B', 8), ('C', 3)])}. ¿Cuál tiene la barra más alta y por cuánto supera a la más baja?", "B; por 5", "8 − 3 = 5."),
            arith(f"Gráfico de dado: el 1 tiene 4, el 2 tiene 6 y el 3 tiene 2. ¿Cuántos lanzamientos hubo?", "4+6+2", "Se suman las frecuencias."),
            ex("Una barra dibujada va del 2 al 7. Si la dibujas bien, desde el 0, con los mismos cuadros pintados, ¿hasta qué número llega?", "Hasta el 5", "Tiene 7 − 2 = 5 cuadros pintados."),
        ],
        "reason": [
            ex("Un gráfico muestra dos barras que llegan a 5. Una parte del 0 y la otra del 3. Ana dice que valen lo mismo. ¿Está bien?", "No; la segunda vale 2 (5 − 3) y la otra vale 5", "Con bases distintas la altura no es la frecuencia."),
            ex("Un gráfico no tiene números en la escala. Beto dice que puede leer cualquier barra. ¿Qué responderías?", "Que sin la escala no sabe cuánto valen las barras", "Los números dicen la frecuencia."),
        ],
        "challenge": [
            ex("Explica dos errores de este gráfico: no tiene título y la barra de «Verde» parte del 2 y llega al 6.", "Falta el título; la barra Verde no parte del 0", "El título y la base común son necesarios."),
            ex("Una barra mal dibujada parte del 3 y llega al 8. ¿Cuántos cuadros debe pintar la barra corregida, si parte del 0?", "5 cuadros", "La frecuencia real es 8 − 3 = 5."),
        ],
    },
    context=[ex("En el diario mural apareció un gráfico de goles: Equipo 1 barra de 4 y Equipo 2 barra de 7, las dos partiendo del 0. ¿Cuántos goles más hizo el Equipo 2?", "3", "7 − 4 = 3.")],
    selfcheck=[
        ex("¿Qué dos cosas debe tener todo gráfico?", "Título y escala", "Sin ellas no se entiende."),
        ex(f"Gráfico: {filas([('X', 2), ('Y', 6)])}. ¿Cuál es la categoría mayor?", "Y", "6 es mayor que 2."),
        ex("¿Qué haces si una barra no parte del 0?", "La corriges para que parta del 0", "Así muestra la frecuencia real."),
    ],
    open_task=task(
        "Un compañero dibujó un gráfico de lanzamientos de un dado: la barra del 2 va del 0 al 4, la barra del 5 va del 3 al 8 y no tiene título. Escribe dos errores del gráfico. Luego redibuja la barra del 5 correctamente, sabiendo que salió 5 veces (8 − 3 = 5).",
        "Errores: falta el título y la barra del 5 parte del 3 y no del 0. Corrección: la barra del 5 debe partir del 0 y llegar al 5, con 5 cuadros. Título posible: Lanzamientos de un dado.",
        ["nombra dos errores", "corrige la barra para que parta del 0", "propone un título", "explica por qué importa la base"],
        ["lista de errores", "barra corregida"],
        ["no ver que parte del 3", "dibujar 8 cuadros en vez de 5"],
        "Pide mostrar en el dibujo dónde parte la barra. Reconoce la corrección con 5 cuadros.",
    ),
    reinforce="Mira un gráfico de barras en una revista o libro y di qué dice su título y su escala.",
    extend="Dibuja a propósito un gráfico engañoso y otro correcto con los mismos datos. Explica la diferencia.",
)

# ================================================================ OA 22
register(
    OA22, 1,
    materials="Papel y lápiz. Los pictogramas están dibujados en cada ejercicio con símbolos ★. La clave dice cuánto vale cada símbolo.",
    use="Aprenderé a leer un pictograma donde cada símbolo vale más de uno. Sirve para entender gráficos con muchos datos.",
    prior=["Sé leer un pictograma de uno en uno.", "Sé contar de 2 en 2."],
    explain=[
        "En un pictograma, la clave dice cuánto vale cada símbolo. Si la clave dice «★ = 2 votos», cada estrella vale 2 votos. Para saber la frecuencia de una fila, cuenta las estrellas y multiplica por 2.",
        "Por ejemplo, 4 estrellas valen 2 + 2 + 2 + 2 = 8 votos. También puedes decir 4 × 2 = 8. Sin mirar la clave, uno se confundiría y diría que son 4 votos.",
        "Por eso, lo primero que haces al leer un pictograma es leer la clave. Luego cuentas los símbolos de cada fila y los conviertes en datos usando la clave. La clave puede ser otro número, como ◆ = 5: entonces 3 símbolos valen 5 + 5 + 5 = 15.",
    ],
    vocab=[("pictograma", "gráfico hecho con símbolos"), ("clave", "frase que dice cuánto vale un símbolo"), ("escala", "valor de cada símbolo, como 2"), ("símbolo", "dibujo que representa varios datos"), ("frecuencia", "cuántos datos hay en una fila")],
    worked=[
        {"title": "Convertir símbolos en votos", "problem": f"Clave: ★ = 2 votos. Fila Rojo: {pic('★', 4)}. ¿Cuántos votos tiene Rojo?", "steps": ["Cuento las estrellas: 4.", "Cada estrella vale 2.", "Sumo 2 + 2 + 2 + 2 o calculo 4 × 2 = 8."], "answer": "8 votos"},
        {"title": "Tres bicicletas", "problem": "Clave: una bicicleta = 2 viajes. Hay 3 bicicletas dibujadas. ¿Cuántos viajes son?", "steps": ["Cuento 3 bicicletas.", "Cada una vale 2 viajes.", "3 × 2 = 6."], "answer": "6 viajes"},
    ],
    mistakes=[
        {"wrong": "Contar 4 estrellas y decir que son 4 votos.", "why": "No se usó la clave.", "fix": "Multiplica el número de símbolos por el valor de cada uno: 4 × 2 = 8."},
        {"wrong": "No leer la clave antes de contar.", "why": "Se puede confundir el valor de los símbolos.", "fix": "Lee la clave primero."},
    ],
    tiers={
        "recovery": [
            arith(f"Clave: ★ = 2 votos. Una fila tiene {pic('★', 3)}. ¿Cuántos votos son?", "3*2", "Tres estrellas de 2 votos cada una."),
            arith(f"Clave: ★ = 2 votos. Una fila tiene {pic('★', 5)}. ¿Cuántos votos son?", "5*2", "Cinco estrellas de 2 cada una."),
            ex("¿Qué debes leer primero en un pictograma?", "La clave", "Dice cuánto vale cada símbolo."),
        ],
        "understand": [
            ex("Si la clave dice ★ = 2, ¿cuántos datos representa una estrella?", "2", "Esa es la escala."),
            ex("¿Por qué hay que multiplicar los símbolos por la clave?", "Porque cada símbolo representa más de un dato", "Una estrella vale 2, no 1."),
            ex("Una fila tiene 6 símbolos con clave de 2. ¿Se puede decir que tiene 6 datos?", "No; tiene 12", "6 × 2 = 12."),
        ],
        "apply": [
            arith(f"Clave: ★ = 2 viajes. Una fila tiene {pic('★', 6)}. ¿Cuántos viajes son?", "6*2", "Seis símbolos valen 2 cada uno."),
            arith("Clave: ★ = 2 votos. Las filas son Azul con 5 estrellas y Verde con 3. ¿Cuántos votos hay entre las dos filas?", "(5+3)*2", "Se suman las estrellas y se multiplican por 2."),
            ex(f"Pictograma con clave ★ = 2. Fila A: {pic('★', 4)}. Fila B: {pic('★', 1)}. ¿Cuál tiene más datos y cuántos tiene cada una?", "A: 8 datos; B: 2 datos; A tiene más", "4 × 2 = 8 y 1 × 2 = 2."),
        ],
        "reason": [
            ex("Daniela dice que 4 estrellas con clave de 2 son 4 votos. ¿Qué error comete?", "No usó la clave; son 8 votos", "4 × 2 = 8."),
            ex("Dos filas tienen 3 símbolos. Una tiene clave de 2 y la otra de 5. ¿Tienen los mismos datos?", "No; 6 y 15", "3 × 2 = 6 y 3 × 5 = 15."),
        ],
        "challenge": [
            ex("Tres bicicletas representan dos viajes cada una. ¿Cuántos viajes son? Explica el cálculo.", "6 viajes; 3 × 2 = 6", "Cada bicicleta cuenta como dos."),
            ex("Una fila tiene 10 votos y la clave es ★ = 2. ¿Cuántas estrellas dibujas?", "5", "Contando de 2 en 2: 2, 4, 6, 8 y 10 son 5 estrellas."),
        ],
    },
    context=[arith(f"En una votación de cursos, la clave dice ★ = 2 votos. El 2.º A tiene {pic('★', 7)}. ¿Cuántos votos tiene?", "7*2", "Siete estrellas de dos votos cada una.")],
    selfcheck=[
        ex("¿Qué dice la clave de un pictograma?", "Cuánto vale cada símbolo", "Es lo primero que se lee."),
        arith(f"Clave ★ = 2. Fila: {pic('★', 2)}. ¿Cuántos datos hay?", "2*2", "Dos estrellas de dos datos cada una."),
        ex("Con clave de 2, ¿cuántos datos valen 8 estrellas?", "16", "8 × 2 = 16."),
    ],
    open_task=task(
        f"Lee este pictograma de votos por frutas. Clave: ★ = 2 votos. Manzana: {pic('★', 5)}. Plátano: {pic('★', 3)}. Naranja: {pic('★', 4)}. Escribe cuántos votos tiene cada fruta y cuántos votos hay en total. Explica cómo usaste la clave.",
        "Manzana: 5 × 2 = 10 votos. Plátano: 3 × 2 = 6 votos. Naranja: 4 × 2 = 8 votos. Total: 10 + 6 + 8 = 24 votos. Usé la clave: cada estrella vale 2 votos.",
        ["convierte cada fila con la clave", "calcula el total 24", "explica la clave", "no cuenta cada símbolo como uno"],
        ["votos por fruta", "total", "explicación"],
        ["no usar la clave", "sumar mal las filas"],
        "Pide mostrar con el dedo cada símbolo y decir «dos, cuatro, seis…». Reconoce la mención de la clave.",
    ),
    reinforce="Cuenta de 2 en 2 hasta 20 y relaciónalo con estrellas dibujadas.",
    extend="Dibuja un pictograma con clave de 2 para 6, 10 y 4 datos.",
)

register(
    OA22, 2,
    materials="Papel y lápiz. Los pictogramas están escritos con símbolos en cada ejercicio, con su clave.",
    use="Aprenderé a comparar las filas de un pictograma con escala y a calcular diferencias. Sirve para saber cuánto más tiene una categoría que otra.",
    prior=["Sé leer una clave de dos.", "Sé restar números de dos cifras."],
    explain=[
        "Para comparar dos filas de un pictograma, primero mira cuántos símbolos tiene cada una. Si una fila tiene 5 símbolos y otra 3, la primera tiene 2 símbolos más. Pero no son 2 datos: hay que mirar la clave.",
        "Con clave de 2, 2 símbolos más son 2 × 2 = 4 datos más. Con clave de 5, cuatro símbolos más son 4 × 5 = 20 datos más. La diferencia en símbolos se multiplica por el valor de la clave.",
        "Otra forma es convertir cada fila en datos y restar. Si una fila tiene 6 símbolos y otra 4, con clave de 5, tienen 30 y 20 datos. La diferencia es 30 − 20 = 10.",
    ],
    vocab=[("diferencia", "cuánto más tiene una fila que otra"), ("clave", "valor de cada símbolo"), ("comparar", "decir cuál tiene más o menos"), ("total", "suma de todas las filas"), ("convertir", "pasar de símbolos a datos")],
    worked=[
        {"title": "Diferencia en símbolos y en datos", "problem": f"Clave ★ = 2. Fila A: {pic('★', 5)}. Fila B: {pic('★', 3)}. ¿Cuánto más tiene A?", "steps": ["5 − 3 = 2 símbolos más.", "Cada símbolo vale 2.", "2 × 2 = 4 datos más."], "answer": "4 datos más"},
        {"title": "Clave de 5", "problem": "Clave: ◆ = 5 puntos. Una fila tiene 6 símbolos y otra 4. ¿Cuál es la diferencia?", "steps": ["6 × 5 = 30 puntos.", "4 × 5 = 20 puntos.", "30 − 20 = 10."], "answer": "10 puntos"},
    ],
    mistakes=[
        {"wrong": "Decir que 5 símbolos menos 3 símbolos son 2 datos con clave de 2.", "why": "Se olvidó multiplicar por la clave.", "fix": "2 símbolos de 2 datos cada uno son 4 datos."},
        {"wrong": "Restar los datos de una fila con los símbolos de otra.", "why": "Se mezclan símbolos y datos.", "fix": "Convierte ambas filas a datos antes de restar."},
    ],
    tiers={
        "recovery": [
            ex(f"Clave ★ = 2. Fila A tiene {pic('★', 4)} y fila B tiene {pic('★', 2)}. ¿Cuál tiene más símbolos?", "La fila A", "4 es mayor que 2."),
            arith("Clave ★ = 2. Fila A tiene 4 símbolos y fila B tiene 2. ¿Cuántos símbolos más tiene A?", "4-2", "Se resta la menor a la mayor."),
            arith("Clave ★ = 2. La fila C tiene 3 símbolos. ¿Cuántos datos son?", "3*2", "Tres símbolos de dos datos cada uno."),
        ],
        "understand": [
            ex("Si dos filas difieren en 3 símbolos y la clave es 2, ¿difieren en 3 datos?", "No; en 6 datos", "3 × 2 = 6."),
            ex("¿Qué se hace con la diferencia de símbolos para saber la diferencia de datos?", "Se multiplica por la clave", "Cada símbolo vale lo que dice la clave."),
            ex("¿Qué operación se usa para comparar cuánto más tiene una fila que otra?", "Una resta", "La diferencia se calcula restando."),
        ],
        "apply": [
            arith("Clave ★ = 2. Una fila tiene 7 símbolos y otra tiene 4. ¿Cuántos datos más tiene la primera?", "(7-4)*2", "Tres símbolos más, con valor 2 cada uno."),
            arith("Clave ◆ = 5. Una fila tiene 6 símbolos y otra 4. ¿Cuál es la diferencia en datos?", "(6-4)*5", "Dos símbolos más, con valor 5 cada uno."),
            arith("Clave ★ = 2. Tres filas tienen 3, 5 y 4 símbolos. ¿Cuántos datos hay en total?", "(3+5+4)*2", "Se suman los símbolos y se multiplica por 2."),
        ],
        "reason": [
            ex("Mía dice que 5 símbolos y 3 símbolos con clave de 2 difieren en 2 datos. ¿Qué error comete?", "No usó la clave; difieren en 4 datos", "2 símbolos × 2 = 4."),
            ex("Con clave ◆ = 5, una fila de 3 símbolos y otra de 2 símbolos. Pablo dice que la diferencia es 1. ¿Está bien?", "No; es 5", "1 símbolo × 5 = 5."),
        ],
        "challenge": [
            ex("Con clave ★ = 2, la fila A tiene 9 símbolos y la fila B tiene 6. ¿Cuántos datos tiene cada una y cuál es la diferencia?", "A: 18; B: 12; diferencia 6", "9 × 2 = 18, 6 × 2 = 12 y 18 − 12 = 6."),
            ex("Con clave ◆ = 5, una fila tiene 8 símbolos y otra fila más corta tiene 15 datos menos. ¿Cuántos símbolos tiene la fila más corta?", "5", "15 datos son 3 símbolos de 5 (5, 10 y 15), y 8 − 3 = 5."),
        ],
    },
    context=[arith("En un pictograma con clave ★ = 2 goles, el equipo Rayo tiene 6 estrellas y el equipo Trueno tiene 4. ¿Cuántos goles más metió Rayo?", "(6-4)*2", "Dos estrellas más de dos goles cada una.")],
    selfcheck=[
        ex("Clave ★ = 2. Una fila tiene 5 símbolos más que otra. ¿Cuántos datos más tiene?", "10", "5 × 2 = 10."),
        ex("¿Cómo se calcula la diferencia entre dos filas?", "Restando", "Se quita la menor a la mayor."),
        ex("Clave ◆ = 5. ¿Cuántos datos valen 4 símbolos?", "20", "4 × 5 = 20."),
    ],
    open_task=task(
        f"Pictograma de libros leídos con clave ★ = 2 libros. Ana: {pic('★', 6)}. Beto: {pic('★', 4)}. Carla: {pic('★', 5)}. Escribe cuántos libros leyó cada niño, quién leyó más, quién leyó menos y cuántos libros más leyó el que más leyó que el que menos leyó.",
        "Ana: 6 × 2 = 12 libros. Beto: 4 × 2 = 8 libros. Carla: 5 × 2 = 10 libros. Leyó más Ana (12) y menos Beto (8). La diferencia es 12 − 8 = 4 libros.",
        ["convierte cada fila con la clave", "identifica quién leyó más y menos", "calcula la diferencia 4", "explica el uso de la clave"],
        ["libros por niño", "diferencia"],
        ["comparar símbolos sin multiplicar", "restar mal"],
        "Pide decir cuántos símbolos más y cuántos libros más. Reconoce la conversión con la clave.",
    ),
    reinforce="Con clave de 2, dibuja 6 y 4 símbolos y calcula cuántos datos más tiene la primera fila.",
    extend="Repite el problema con clave de 5 y las mismas filas. ¿Cambió la diferencia?",
)

register(
    OA22, 3,
    materials="Papel, lápiz y regla. Las tablas están escritas en cada ejercicio. Dibuja los símbolos ★ en tu cuaderno.",
    use="Aprenderé a transformar una tabla de datos en un pictograma, respetando la clave. Sirve para mostrar datos con símbolos y ahorrar espacio.",
    prior=["Sé leer una clave de dos.", "Sé encontrar la mitad de un número par pequeño y contar de 2 en 2."],
    explain=[
        "Para pasar una tabla a pictograma, primero decide la clave. Con clave de 2, cada ★ vale 2. Luego, para cada frecuencia, busca su mitad (o cuenta de 2 en 2 hasta llegar al dato) para saber cuántos símbolos dibujar.",
        "Por ejemplo, con frecuencias 4, 8 y 6, dibujas 2, 4 y 3 símbolos. Compruebas multiplicando: 2 × 2 = 4, 4 × 2 = 8 y 3 × 2 = 6. Si multiplicando no vuelves al dato, hay un error.",
        "Todos los símbolos de un pictograma deben ser del mismo tamaño, y la clave debe estar escrita. Si una frecuencia es impar, como 7, se necesita una convención: por ejemplo, «medio símbolo = 1 dato». Sin esa regla, el medio símbolo no se entiende.",
    ],
    vocab=[("tabla", "datos ordenados en filas"), ("clave", "valor de cada símbolo"), ("mitad", "una de las dos partes iguales de un número, como 3 en 6"), ("convención", "regla acordada, como «medio símbolo = 1»"), ("comprobar", "revisar multiplicando")],
    worked=[
        {"title": "De tabla a pictograma", "problem": "Tabla: Perros 4, Gatos 8, Peces 6. Clave ★ = 2. ¿Cuántos símbolos lleva cada fila?", "steps": ["La mitad de 4 es 2: 2 símbolos para Perros.", "La mitad de 8 es 4: 4 símbolos para Gatos.", "La mitad de 6 es 3: 3 símbolos para Peces.", "Compruebo: 2 × 2 = 4, 4 × 2 = 8 y 3 × 2 = 6."], "answer": f"Perros {pic('★', 2)}; Gatos {pic('★', 4)}; Peces {pic('★', 3)}"},
        {"title": "Un número impar", "problem": "La clave es ★ = 2 y medio símbolo (una estrella partida por la mitad) = 1. Una fila tiene 7 datos. ¿Cómo la dibujas?", "steps": ["7 = 6 + 1.", "La mitad de 6 es 3: 3 estrellas completas.", "El 1 que sobra se dibuja como medio símbolo."], "answer": "3 estrellas y 1 medio símbolo"},
    ],
    mistakes=[
        {"wrong": "Dibujar 8 estrellas para el dato 8 con clave de 2.", "why": "Se copió el dato sin usar la clave.", "fix": "Busca la mitad de 8: son 4 estrellas."},
        {"wrong": "Dibujar medio símbolo sin explicarlo en la clave.", "why": "El lector no sabe cuánto vale.", "fix": "Escribe la convención en la clave: medio símbolo = 1 dato."},
    ],
    tiers={
        "recovery": [
            ex("Clave ★ = 2. Un dato es 6. ¿Cuántas estrellas dibujas?", "3", "Contando de 2 en 2: 2, 4 y 6 son 3 estrellas."),
            ex("Clave ★ = 2. Un dato es 10. ¿Cuántas estrellas dibujas?", "5", "La mitad de 10 es 5."),
            ex("Clave ★ = 2. Un dato es 2. ¿Cuántas estrellas dibujas?", "1", "Una estrella vale 2."),
        ],
        "understand": [
            ex("Con clave ★ = 2, ¿se dibuja el mismo número de símbolos que el dato?", "No; la mitad", "Cada símbolo vale 2."),
            ex("¿Cómo compruebas que dibujaste bien?", "Multiplicando los símbolos por la clave", "Debes volver al dato."),
            ex("¿Por qué hay que escribir la clave en el pictograma?", "Para que el lector sepa cuánto vale cada símbolo", "Sin clave no se puede leer."),
        ],
        "apply": [
            ex("Tabla: Rojo 8, Azul 4, Verde 6. Clave ★ = 2. Escribe cuántos símbolos lleva cada fila.", "Rojo 4, Azul 2, Verde 3", "Se busca la mitad de cada dato."),
            ex("Construye dos filas para frecuencias 10 y 6 con clave de 2. ¿Cuántos símbolos lleva cada una?", "5 y 3", "La mitad de 10 es 5 y la mitad de 6 es 3."),
            ex("Con clave ★ = 2 y medio símbolo = 1, ¿cómo se representa un dato de 5?", "2 estrellas y 1 medio símbolo", "4 + 1 = 5."),
        ],
        "reason": [
            ex("Tomás dibujó 12 estrellas para un dato de 12, con clave de 2. ¿Qué error hay?", "Debe dibujar 6 estrellas", "La mitad de 12 es 6."),
            ex("Luna dibujó 3 estrellas y media para un dato de 7 sin escribir qué vale la media. ¿Qué falta?", "La convención: media estrella vale 1", "Sin ella no se entiende."),
        ],
        "challenge": [
            ex("Tabla: Lunes 14, Martes 8, Miércoles 12. Clave ★ = 2. ¿Cuántas estrellas dibujas en total?", "17", "7 + 4 + 6 = 17."),
            ex("Con clave ◆ = 5, ¿cuántos símbolos necesitas para un dato de 20?", "4", "Contando de 5 en 5: 5, 10, 15 y 20 son 4 símbolos."),
        ],
    },
    context=[ex("En una encuesta del curso, 12 niños prefieren el helado de chocolate y 8 prefieren el de frutilla. Con clave ★ = 2 niños, ¿cuántas estrellas lleva cada sabor?", "Chocolate 6, frutilla 4", "La mitad de 12 es 6 y la mitad de 8 es 4.")],
    selfcheck=[
        ex("Con clave de 2, ¿cuántos símbolos son 14 datos?", "7", "La mitad de 14 es 7."),
        ex("¿Qué se hace con una frecuencia para saber cuántos símbolos dibujar?", "Se busca cuántos símbolos caben (con clave 2, la mitad)", "Un símbolo reemplaza varios datos."),
        ex("¿Cómo compruebas el pictograma?", "Multiplicando los símbolos por la clave", "Debe dar el dato original."),
    ],
    open_task=task(
        "Con esta tabla de mascotas del curso: perros 6, gatos 10, conejos 4. Usa la clave ★ = 2 mascotas. Dibuja el pictograma con título, clave y una fila por mascota. Comprueba multiplicando cada fila.",
        f"Título: Mascotas del curso. Clave: ★ = 2 mascotas. Perros: {pic('★', 3)}. Gatos: {pic('★', 5)}. Conejos: {pic('★', 2)}. Comprobación: 3 × 2 = 6; 5 × 2 = 10; 2 × 2 = 4.",
        ["escribe título y clave", "dibuja 3, 5 y 2 símbolos", "símbolos del mismo tamaño", "comprueba multiplicando"],
        ["pictograma completo", "comprobación"],
        ["copiar el dato como número de símbolos", "olvidar la clave"],
        "Pide leer el pictograma de vuelta con la clave. Reconoce la comprobación.",
    ),
    reinforce="Con la tabla perros 4, gatos 6, dibuja un pictograma con clave de 2.",
    extend="Repite la tabla de mascotas con clave ◆ = 5 pero con datos 10, 15 y 5.",
)

register(
    OA22, 4,
    materials="Papel cuadriculado o cuadrícula dibujada, regla y lápices. Los pictogramas se describen en cada ejercicio.",
    use="Aprenderé a representar los mismos datos de un pictograma en un gráfico de barras. Sirve para comparar alturas desde una base común.",
    prior=["Sé hacer un pictograma con clave de 2.", "Sé dibujar barras desde el 0."],
    explain=[
        "Un pictograma con clave de 2 y un gráfico de barras pueden mostrar los mismos datos. En el pictograma, cuentas símbolos y multiplicas por 2. En las barras, la altura ya es el dato.",
        "Para pasar de pictograma a barras: primero convierte cada fila a datos con la clave. Si Rojo tiene 3 estrellas, son 6 datos. Entonces la barra de Rojo llega hasta el 6.",
        "En las barras, la escala puede ser de uno: cada cuadro vale 1 dato. Todas las barras parten del 0. La altura muestra la frecuencia, no la cantidad de símbolos del pictograma.",
    ],
    vocab=[("barra", "rectángulo que muestra una frecuencia"), ("altura", "hasta dónde llega la barra"), ("escala", "números del eje"), ("base", "el 0 desde donde parten las barras"), ("convertir", "pasar de símbolos a datos")],
    worked=[
        {"title": "Pasar a barras", "problem": "Frecuencias 6, 10 y 4. ¿Hasta qué número llega cada barra?", "steps": ["La altura de cada barra es la frecuencia.", "La primera llega al 6.", "La segunda al 10 y la tercera al 4."], "answer": "6, 10 y 4"},
        {"title": "Del pictograma a las barras", "problem": f"Pictograma con clave ★ = 2: Rojo {pic('★', 3)}, Azul {pic('★', 5)}. ¿Hasta qué número llegan las barras?", "steps": ["Rojo: 3 × 2 = 6.", "Azul: 5 × 2 = 10.", "Las barras llegan al 6 y al 10."], "answer": "Rojo al 6 y Azul al 10"},
    ],
    mistakes=[
        {"wrong": "Dibujar la barra de Rojo hasta el 3 porque tiene 3 estrellas.", "why": "No se usó la clave.", "fix": "3 estrellas valen 6 datos: la barra llega al 6."},
        {"wrong": "Hacer barras que no parten del 0.", "why": "Se pierde la comparación.", "fix": "Todas las barras parten del mismo 0."},
    ],
    tiers={
        "recovery": [
            ex("Una frecuencia es 8. ¿Hasta qué número llega su barra con escala de uno?", "Hasta el 8", "La altura es la frecuencia."),
            arith("Clave ★ = 2. Una fila tiene 4 estrellas. ¿Hasta qué número llega su barra?", "4*2", "Cuatro estrellas valen 8 datos."),
            ex("¿Desde dónde parten las barras?", "Desde el 0", "Es la base común."),
        ],
        "understand": [
            ex("¿Qué muestra la altura de una barra?", "La frecuencia", "Es el número de datos."),
            ex("¿Cambian los datos si pasas un pictograma a un gráfico de barras?", "No", "Sólo cambia la forma de mostrarlos."),
            ex("Con clave de 2, ¿qué haces primero para dibujar la barra de una fila?", "Convertir los símbolos en datos", "Multiplicas los símbolos por 2."),
        ],
        "apply": [
            ex(f"Pictograma con clave ★ = 2: A {pic('★', 2)}, B {pic('★', 4)}, C {pic('★', 3)}. ¿Hasta qué número llega cada barra?", "A al 4, B al 8, C al 6", "2 × 2 = 4, 4 × 2 = 8 y 3 × 2 = 6."),
            arith("Una barra llega al 10 y otra al 6. ¿Cuántos cuadros más tiene la primera?", "10-6", "Se resta la menor a la mayor."),
            arith("Un pictograma con clave de 2 tiene 6, 3 y 4 estrellas. ¿Cuántos datos hay en total?", "(6+3+4)*2", "Se suman las estrellas y se multiplica por 2."),
        ],
        "reason": [
            ex("Una barra llega al 5, pero la fila del pictograma tenía 5 estrellas con clave de 2. ¿Qué error hay?", "Debe llegar al 10", "5 × 2 = 10."),
            ex("Ale dice que las barras de un gráfico pueden partir de lugares distintos si llegan al mismo número. ¿Qué responderías?", "Que deben partir del 0", "Si no, la altura engaña."),
        ],
        "challenge": [
            ex("Dibuja las barras que corresponden a este pictograma con clave 2: Lunes 4 estrellas, Martes 2 estrellas, Miércoles 5 estrellas. Escribe las alturas.", "8, 4 y 10", "4 × 2 = 8, 2 × 2 = 4 y 5 × 2 = 10."),
            ex("Una barra llega al 12 y la clave del pictograma es 2. ¿Cuántas estrellas tenía la fila?", "6", "Contando de 2 en 2 hasta 12 hay 6 estrellas."),
        ],
    },
    context=[ex("En una encuesta del curso con clave ★ = 2 niños, la fila de fútbol tiene 7 estrellas. ¿Hasta qué número llega la barra de fútbol?", "14", "7 × 2 = 14.")],
    selfcheck=[
        ex("Con clave de 2, ¿hasta qué número llega una barra de 5 estrellas?", "10", "5 × 2 = 10."),
        ex("¿Qué debe tener un gráfico de barras además de las barras?", "Título, escala y nombres", "Así se entiende."),
        ex("¿Dónde parte cada barra?", "En el 0", "Es la base."),
    ],
    open_task=task(
        f"Pictograma de deportes del curso. Clave: ★ = 2 niños. Fútbol: {pic('★', 5)}. Básquetbol: {pic('★', 3)}. Natación: {pic('★', 4)}. Dibuja el gráfico de barras que corresponde, con escala de uno, título y nombres. Escribe hasta qué número llega cada barra.",
        "Fútbol: 5 × 2 = 10. Básquetbol: 3 × 2 = 6. Natación: 4 × 2 = 8. Título: Deporte preferido del curso. Escala de 0 a 10. Las barras parten del 0 y llegan a 10, 6 y 8.",
        ["convierte cada fila con la clave", "dibuja barras de 10, 6 y 8", "las barras parten del 0", "pone título y nombres"],
        ["gráfico de barras", "alturas escritas"],
        ["usar el número de estrellas como altura", "no empezar en 0"],
        "Pide mostrar con el dedo desde dónde parte cada barra. Reconoce el uso de la clave.",
    ),
    reinforce="Con la tabla 6, 8 y 4, dibuja las barras con escala de uno.",
    extend="Haz un pictograma y un gráfico de barras con los mismos datos y escribe una ventaja de cada uno.",
)

register(
    OA22, 5,
    materials="Papel y lápiz. Los datos, pictogramas y gráficos están escritos en cada ejercicio.",
    use="Aprenderé a interpretar datos y a elegir si conviene un pictograma o un gráfico de barras para comunicar una conclusión. Sirve para explicar con datos lo que descubrí.",
    prior=["Sé construir pictogramas con clave.", "Sé dibujar gráficos de barras desde el 0."],
    explain=[
        "El pictograma y el gráfico de barras muestran los mismos datos de forma distinta. El pictograma usa símbolos y agrupa datos con una clave. Sirve para ver cuántas unidades tiene cada categoría de forma entretenida.",
        "El gráfico de barras compara las alturas desde una base común. Sirve para ver rápidamente cuál categoría es mayor. Con la escala, puedes leer cada frecuencia casi exacta.",
        "Para elegir la representación, piensa qué quieres mostrar. Si quieres mostrar qué categoría tiene mayor frecuencia, las barras la muestran con claridad. Después, defiende tu elección con datos: escribe cuál categoría es mayor y por cuánto.",
    ],
    vocab=[("interpretar", "explicar qué dicen los datos"), ("representación", "forma de mostrar datos, como una tabla o un gráfico"), ("conclusión", "frase que dice lo que muestran los datos"), ("defender", "dar razones con datos"), ("comparar", "decir cuál es mayor o menor")],
    worked=[
        {"title": "Interpretar un pictograma", "problem": f"Clave ★ = 2. Fútbol: {pic('★', 6)}. Natación: {pic('★', 4)}. ¿Qué puedes concluir?", "steps": ["Fútbol: 6 × 2 = 12.", "Natación: 4 × 2 = 8.", "12 − 8 = 4."], "answer": "Fútbol tiene 4 niños más que natación"},
        {"title": "Elegir una representación", "problem": "Quieres mostrar cuál de tres frutas es la más votada. ¿Qué gráfico eliges y por qué?", "steps": ["Quiero comparar tres frecuencias.", "En barras, las alturas parten del mismo 0.", "Se ve rápido cuál es la más alta."], "answer": "Un gráfico de barras, porque compara alturas desde una base común"},
    ],
    mistakes=[
        {"wrong": "Afirmar una conclusión que los datos no muestran.", "why": "Se inventa algo que no está en el gráfico.", "fix": "Usa sólo números del gráfico o de la tabla."},
        {"wrong": "Elegir una representación sin explicar por qué.", "why": "No se defiende con datos.", "fix": "Escribe una razón: cuál categoría tiene más y por cuánto."},
    ],
    tiers={
        "recovery": [
            arith(f"Clave ★ = 2. Una fila tiene {pic('★', 5)}. ¿Cuántos datos son?", "5*2", "Cinco estrellas de dos."),
            ex("Una barra llega al 9 y otra al 4. ¿Cuál categoría tiene más?", "La de 9", "9 es mayor que 4."),
            arith("Una categoría tiene 12 datos y otra tiene 7. ¿Cuántos datos más tiene la primera?", "12-7", "Se restan los datos."),
        ],
        "understand": [
            ex("¿Qué muestra un pictograma?", "Datos con símbolos y una clave", "Cada símbolo vale lo que dice la clave."),
            ex("¿Qué muestra un gráfico de barras?", "Datos con barras de altura igual a la frecuencia", "Compara alturas desde el 0."),
            ex("¿Pueden dos gráficos distintos mostrar los mismos datos?", "Sí", "Cambian sólo la forma de mostrarlos."),
        ],
        "apply": [
            ex(f"Pictograma clave ★ = 2: Manzana {pic('★', 4)}, Plátano {pic('★', 7)}, Naranja {pic('★', 2)}. ¿Cuál fruta tiene más datos y cuántos?", "Plátano; 14", "7 × 2 = 14."),
            arith(f"Con los mismos datos de Manzana 4 estrellas y Naranja 2 estrellas (clave ★ = 2), ¿cuántos datos más tiene Manzana que Naranja?", "(4-2)*2", "Dos estrellas más, con valor 2 cada una."),
            ex("Barras: Lunes 6, Martes 9, Miércoles 4. ¿Qué día tiene más y cuántos datos hay en total?", "Martes; 19", "6 + 9 + 4 = 19."),
        ],
        "reason": [
            ex("Lola dice que el pictograma es mejor que las barras para ver cuál categoría es mayor. ¿Qué ventaja tiene el gráfico de barras?", "Que las alturas parten de una base común y se comparan rápido", "La base común facilita ver cuál es mayor."),
            ex("Un gráfico muestra cuántos niños eligieron fútbol (12) y natación (6). Raúl dice «mañana todos elegirán fútbol». ¿Qué error comete?", "Los datos no permiten asegurar lo que pasará mañana", "Una conclusión habla de los datos que hay."),
        ],
        "challenge": [
            ex("Tabla: fútbol 12, básquetbol 8, natación 6. Elige una representación para mostrar cuál deporte es el más elegido y defiende con datos.", "Barras; fútbol 12 es el mayor, 4 más que básquetbol y 6 más que natación", "12 − 8 = 4 y 12 − 6 = 6."),
            ex("Con clave ★ = 2, un pictograma tiene 5, 8 y 3 estrellas. ¿Cuántos datos más tiene la fila mayor que la menor?", "10", "(8 − 3) × 2 = 10."),
        ],
    },
    context=[ex("El curso votó por el paseo: zoológico 14 votos, museo 10 votos, parque 6 votos. ¿Cuántos votos más tiene el zoológico que el parque?", "8", "14 − 6 = 8.")],
    selfcheck=[
        ex("¿Qué haces primero al leer un pictograma?", "Leo la clave", "Dice cuánto vale cada símbolo."),
        ex("¿Qué debe tener una conclusión?", "Datos del gráfico", "Se apoya en números reales."),
        ex("Barras: A 7 y B 3. ¿Cuántos más tiene A?", "4", "7 − 3 = 4."),
    ],
    open_task=task(
        f"El curso votó el juego del recreo. Pictograma con clave ★ = 2 votos. Pillarse: {pic('★', 6)}. Saltar cuerda: {pic('★', 4)}. Escondite: {pic('★', 3)}. Elige una representación (pictograma o barras) para mostrar cuál juego ganó. Escribe una conclusión con datos y explica por qué elegiste esa representación.",
        "Pillarse: 12 votos, saltar cuerda: 8 votos, escondite: 6 votos. Elijo las barras porque se comparan las alturas desde el 0. Pillarse ganó, con 4 votos más que saltar cuerda y 6 más que escondite.",
        ["convierte las filas con la clave", "elige una representación y la explica", "escribe una conclusión con números", "no afirma lo que los datos no dicen"],
        ["conversión de datos", "elección justificada", "conclusión"],
        ["no usar la clave", "dar una conclusión sin números"],
        "Pide mostrar los números de cada voto antes de elegir. Reconoce la razón de la elección.",
    ),
    reinforce="Pregunta a cinco personas cuál fruta prefieren y haz un pictograma con clave de uno.",
    extend="Haz un pictograma con clave de 2 y un gráfico de barras con los mismos datos de tu curso. Escribe cuál te ayuda más.",
)
