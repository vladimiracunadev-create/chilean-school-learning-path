"""Cuaderno del estudiante de 5.º básico Matemática: OA 04 (división de tres cifras por una) y OA 05 (operaciones combinadas)."""
from __future__ import annotations

from student_content_ma05_a import M, W, f, lesson, task
from student_lessons import arith, ex

OA4 = "MA05 OA 04"
OA5 = "MA05 OA 05"


def dv(a, b):
    """Cociente y resto escritos como texto."""
    return f"{f(a // b)} resto {a % b}" if a % b else f(a // b)


# ------------------------------------------------------------------ OA 04 clase 1
lesson(
    OA4, 1,
    use="Aprenderé a dividir números de tres cifras por un número de una cifra, repartiendo y descomponiendo el dividendo. Sirve para repartir cantidades grandes en partes iguales.",
    prior=["Sé las tablas de multiplicar y sus divisiones.", "Sé dividir números de dos cifras por uno de una cifra."],
    explain=[
        "Dividir es repartir una cantidad en partes iguales o ver cuántas veces cabe un número en otro. En 396 ÷ 3, el 396 es el dividendo (lo que se reparte), el 3 es el divisor (en cuántas partes o de cuánto en cuánto) y el resultado es el cociente.",
        "Una forma fácil de dividir es descomponer el dividendo en partes que se dividen exacto. Para 396 ÷ 3: 396 = 300 + 90 + 6. Luego 300 ÷ 3 = 100, 90 ÷ 3 = 30 y 6 ÷ 3 = 2. Se suman los resultados: 100 + 30 + 2 = 132.",
        "A veces el reparto no es exacto y sobra algo. Lo que sobra se llama resto y siempre es menor que el divisor. Por ejemplo, 7 ÷ 2 = 3 y sobra 1. Se comprueba con la relación: divisor × cociente + resto = dividendo. Aquí 2 × 3 + 1 = 7.",
    ],
    vocab=[("dividendo", "la cantidad que se reparte"), ("divisor", "el número entre el que se reparte"), ("cociente", "el resultado de dividir"), ("resto", "lo que sobra cuando el reparto no es exacto"), ("descomponer", "separar un número en partes más fáciles")],
    worked=[
        W("Dividir descomponiendo", "Calcula 396 ÷ 3 descomponiendo el dividendo.", ["396 = 300 + 90 + 6.", "300 ÷ 3 = 100; 90 ÷ 3 = 30; 6 ÷ 3 = 2.", "100 + 30 + 2 = 132."], "132"),
        W("Un reparto con resto", "Reparte 7 caramelos entre 2 niños en partes iguales.", ["Cada niño recibe 3 caramelos: 2 × 3 = 6.", "7 − 6 = 1, sobra 1 caramelo.", "Compruebo: 2 × 3 + 1 = 7."], "Cociente 3, resto 1"),
    ],
    mistakes=[
        M("Calcular 408 ÷ 4 como 12 porque 4 ÷ 4 = 1, 0 ÷ 4 = 0 y 8 ÷ 4 = 2.", "No se respetó el valor de cada parte: 400 ÷ 4 es 100, no 1.", "408 = 400 + 8; 400 ÷ 4 = 100 y 8 ÷ 4 = 2: el cociente es 102."),
        M("Decir que 35 ÷ 6 da 5 resto 6.", "El resto no puede ser igual o mayor que el divisor.", "Como 6 cabe una vez más, queda 35 ÷ 6 = 5 resto 5: 6 × 5 + 5 = 35."),
    ],
    rec=[
        arith("Reparte 18 galletas en partes iguales entre 3 niños. ¿Cuántas recibe cada uno?", "18//3", "Cada niño recibe la tercera parte."),
        ex("Completa: 300 ÷ 3 = __.", "100", "3 × 100 = 300."),
        ex("En 56 ÷ 8 = 7, ¿cuál número es el divisor?", "8", "El divisor es el número por el que se divide."),
    ],
    und=[
        ex("Calcula 248 ÷ 2 descomponiendo 248 en 200 + 40 + 8.", "124", "200 ÷ 2 = 100, 40 ÷ 2 = 20 y 8 ÷ 2 = 4."),
        ex("Si repartes 7 caramelos entre 2 niños en partes iguales, ¿cuántos sobran?", "1", "Cada uno recibe 3 y quedan 7 − 6 = 1."),
        arith("Calcula 640 ÷ 4 descomponiendo 640 en 400 + 240.", "640//4", "400 ÷ 4 = 100 y 240 ÷ 4 = 60."),
    ],
    app=[
        arith("Una escuela reparte 486 hojas en partes iguales entre 6 cursos. ¿Cuántas hojas recibe cada curso?", "486//6", "480 ÷ 6 = 80 y 6 ÷ 6 = 1."),
        arith("Se guardan 525 libros en 5 cajas iguales. ¿Cuántos libros hay en cada caja?", "525//5", "500 ÷ 5 = 100 y 25 ÷ 5 = 5."),
        ex("Comprueba la división 487 ÷ 4 = 121 resto 3 con la fórmula divisor × cociente + resto.", "4 × 121 + 3 = 487", "484 + 3 = 487, que es el dividendo."),
    ],
    rea=[
        ex("Ema dice que 408 ÷ 4 = 12. ¿Está bien?", "No, es 102", "408 = 400 + 8 y 400 ÷ 4 = 100; 100 + 2 = 102."),
        ex("¿Puede tener resto 6 una división por 5?", "No", "El resto debe ser menor que el divisor."),
    ],
    cha=[
        ex("Al dividir un número por 7 se obtiene cociente 45 y resto 3. ¿Cuál es el número?", "318", "7 × 45 = 315 y 315 + 3 = 318."),
        ex("¿Cuántos restos distintos puede dejar una división por 6 (contando el 0)?", "6", "Pueden ser 0, 1, 2, 3, 4 y 5."),
    ],
    ctx=[arith("Un taller ficticio reparte 475 hojas en 5 carpetas iguales. ¿Cuántas hojas lleva cada carpeta?", "475//5", "500 ÷ 5 = 100, menos 25 ÷ 5 = 5.")],
    sc=[
        arith("Calcula 396 ÷ 3.", "396//3", "300 ÷ 3 = 100, 90 ÷ 3 = 30 y 6 ÷ 3 = 2."),
        ex("¿Cómo se llama el número que sobra en un reparto?", "Resto", "Es lo que queda sin repartir."),
        ex("¿Qué dividendo tiene divisor 5, cociente 8 y resto 3?", "43", "5 × 8 = 40 y 40 + 3 = 43."),
    ],
    op=task(
        "Elige uno de estos repartos: 324 láminas entre 3 álbumes, 285 fichas entre 5 bolsas o 135 galletas entre 2 bandejas. Divide descomponiendo el dividendo, indica el resto si lo hay y comprueba con divisor × cociente + resto.",
        "135 galletas entre 2 bandejas: 135 = 100 + 30 + 5. 100 ÷ 2 = 50, 30 ÷ 2 = 15 y 5 ÷ 2 = 2 resto 1. Total 67 resto 1. Compruebo: 2 × 67 + 1 = 135.",
        ["descompone el dividendo", "obtiene cociente y resto", "comprueba"],
        ["división descompuesta", "comprobación escrita"],
        ["dividir cifra a cifra sin respetar el valor", "resto mayor que el divisor"],
        "Pide que verifique con la relación divisor × cociente + resto y que revise que el resto sea menor que el divisor.",
    ),
    reinforce="Reparte 48 fichas entre 4 bolsas con tapitas u objetos pequeños de tu casa. Luego haz el mismo reparto con 49 fichas y anota qué sobra.",
    extend="Explica por qué el resto nunca puede ser igual al divisor.",
)

# ------------------------------------------------------------------ OA 04 clase 2
lesson(
    OA4, 2,
    use="Aprenderé el algoritmo de la división escrita con dividendos de tres cifras, incluso cuando hay resto. Sirve para dividir rápido y ordenado.",
    prior=["Sé dividir descomponiendo.", "Sé que el resto es menor que el divisor."],
    explain=[
        "El algoritmo escrito divide cifra por cifra, de izquierda a derecha. Se parte por la cifra de las centenas. Si esa cifra es menor que el divisor, se toman las dos primeras cifras. Cada vez se escribe cuántas veces cabe el divisor, se multiplica y se resta para ver qué sobra.",
        "Ejemplo, 487 ÷ 4: en 4 centenas el 4 cabe 1 vez y sobra 0. Se baja el 8: en 8 decenas el 4 cabe 2 veces y sobra 0. Se baja el 7: en 7 unidades el 4 cabe 1 vez y sobra 3. El cociente es 121 y el resto es 3.",
        "Siempre comprueba con divisor × cociente + resto. Aquí 4 × 121 + 3 = 487. Si el resto sale igual o mayor que el divisor, se puede repartir una vez más, así que algo está mal. También estima: 487 es cerca de 480 y 480 ÷ 4 = 120, cercano a 121.",
    ],
    vocab=[("algoritmo", "procedimiento ordenado de pasos para calcular"), ("bajar una cifra", "pasar la siguiente cifra del dividendo al resto"), ("cociente", "resultado de dividir"), ("resto", "lo que sobra"), ("estimar", "calcular un valor cercano sin hacer toda la cuenta")],
    worked=[
        W("División con resto", "Calcula 735 ÷ 6.", ["7 centenas: 6 cabe 1 vez (6) y sobra 1.", "Bajo el 3: 13 decenas; 6 cabe 2 veces (12) y sobra 1.", "Bajo el 5: 15 unidades; 6 cabe 2 veces (12) y sobra 3.", "Cociente 122, resto 3. Compruebo: 6 × 122 + 3 = 735."], "122 resto 3"),
        W("Cuando la primera cifra es menor que el divisor", "Calcula 365 ÷ 7.", ["3 es menor que 7: tomo 36.", "7 cabe 5 veces en 36 (35) y sobra 1.", "Bajo el 5: 15; 7 cabe 2 veces (14) y sobra 1.", "Cociente 52, resto 1. Compruebo: 7 × 52 + 1 = 365."], "52 resto 1"),
    ],
    mistakes=[
        M("Obtener 487 ÷ 4 = 120 resto 7.", "El resto 7 es mayor que el divisor 4.", "Si sobran 7, el 4 cabe una vez más. Es 121 resto 3."),
        M("Olvidar bajar un cero y escribir 640 ÷ 8 = 8.", "En el cociente faltó la cifra de las decenas.", "64 decenas ÷ 8 = 8 decenas, o sea 80: 640 ÷ 8 = 80."),
    ],
    rec=[
        ex("¿Cuántas veces cabe el 4 en 12?", "3", "4 × 3 = 12."),
        ex("En 365 ÷ 7, ¿con cuántas cifras empiezas la primera división?", "2", "3 es menor que 7; hay que tomar 36."),
        arith("Calcula 840 ÷ 4.", "840//4", "84 decenas ÷ 4 = 21 decenas."),
    ],
    und=[
        ex("Calcula 487 ÷ 4 con el algoritmo.", dv(487, 4), "Cociente 121; 4 × 121 = 484 y sobran 3."),
        ex("Calcula 904 ÷ 8 con el algoritmo.", dv(904, 8), "9 ÷ 8 = 1 y sobra 1; luego 10 ÷ 8 = 1 y sobran 2; luego 24 ÷ 8 = 3 y no sobra nada."),
        ex("Calcula 618 ÷ 9 con el algoritmo.", dv(618, 9), "9 × 68 = 612 y sobran 6."),
    ],
    app=[
        ex("Calcula 859 ÷ 7.", dv(859, 7), "7 × 122 = 854 y sobran 5."),
        ex("Un año común tiene 365 días. ¿Cuántas semanas completas hay y cuántos días sobran?", "52 semanas y 1 día", "365 ÷ 7 = 52 resto 1."),
        arith("Se empacan 756 manzanas en cajas de 9 manzanas. ¿Cuántas cajas se llenan?", "756//9", "9 × 84 = 756."),
    ],
    rea=[
        ex("Un estudiante escribe 487 ÷ 4 = 120 resto 7. ¿Qué error tiene y cuál es el resultado?", "El resto 7 es mayor que 4; es 121 resto 3", "Siempre el resto debe ser menor que el divisor."),
        ex("Rita comprueba 859 ÷ 7 = 122 resto 5 con 7 × 122 + 5. ¿El resultado es 859?", "Sí", "854 + 5 = 859."),
    ],
    cha=[
        ex("¿Cuál es el mayor resto posible al dividir por 8?", "7", "El resto es menor que 8."),
        ex("¿Qué cifra falta para que 4_5 ÷ 5 = 85 sea exacta?", "2", "5 × 85 = 425."),
    ],
    ctx=[ex("Una profesora reparte 365 láminas de modo igual entre 7 grupos. ¿Cuántas recibe cada grupo y cuántas sobran?", "52 y sobra 1", "365 ÷ 7 = 52 resto 1.")],
    sc=[
        ex("Calcula 735 ÷ 6.", dv(735, 6), "6 × 122 = 732 y sobran 3."),
        arith("Calcula 999 ÷ 9.", "999//9", "9 centenas, 9 decenas y 9 unidades se reparten en 1 cada una."),
        ex("Comprueba si 4 × 121 + 3 es 487.", "Sí", "484 + 3 = 487."),
    ],
    op=task(
        "Elige: 625 ÷ 4, 840 ÷ 7 o 503 ÷ 6. Resuelve con el algoritmo, escribe el cociente y el resto, comprueba con divisor × cociente + resto y explica qué hiciste cuando la primera cifra era menor que el divisor.",
        "503 ÷ 6: 5 es menor que 6, tomo 50; 6 cabe 8 veces (48) y sobran 2. Bajo el 3: 23; 6 cabe 3 veces (18) y sobran 5. Cociente 83, resto 5. Compruebo: 6 × 83 + 5 = 503.",
        ["usa el algoritmo", "indica cociente y resto", "comprueba con la fórmula"],
        ["división escrita", "comprobación"],
        ["resto mayor que el divisor", "olvidar bajar cifras"],
        "Pide que revise cada resta parcial y que verifique que cada resto sea menor que el divisor.",
    ),
    reinforce="Resuelve 468 ÷ 3 y 250 ÷ 4 con el algoritmo y comprueba con la fórmula.",
    extend="Explica cómo sabes cuántas cifras tendrá el cociente de 365 ÷ 7 antes de dividir.",
)

# ------------------------------------------------------------------ OA 04 clase 3
lesson(
    OA4, 3,
    use="Aprenderé a interpretar el resto de una división en el contexto del problema, decidiendo si se ignora, se muestra o se suma 1 al cociente. Sirve para dar respuestas que tengan sentido.",
    prior=["Sé dividir con resto usando el algoritmo.", "Sé comprobar con divisor × cociente + resto."],
    explain=[
        "El resto de una división puede significar cosas distintas según el problema. Antes de responder, relee la pregunta y piensa qué pasa con lo que sobra. Hay tres casos frecuentes que conviene reconocer con ejemplos de la vida diaria.",
        "Caso 1: la pregunta es cuántos cabe completos y lo que sobra no se usa. Con $250 y stickers de $6, 250 ÷ 6 = 41 resto 4: puedes comprar 41 stickers y sobran $4. Caso 2: hay que atender a todos. Para 100 personas en mesas de 6, 100 ÷ 6 = 16 resto 4, y las 4 personas necesitan otra mesa: 17 mesas.",
        "Caso 3: la pregunta es solo por lo que sobra. En 365 días hay 52 semanas y sobra 1 día; la respuesta es «1 día». En cada caso, escribe una frase completa con unidad. El resto no se redondea ni se pierde sin pensar: se interpreta.",
    ],
    vocab=[("interpretar", "darle sentido a un resultado según la situación"), ("resto", "lo que sobra al dividir"), ("completo", "que se llena del todo, sin partes incompletas"), ("sobrar", "quedar sin usar"), ("respuesta completa", "una frase que dice el resultado con su unidad")],
    worked=[
        W("El resto se descarta", "Con $250 se compran stickers de $6 cada uno. ¿Cuántos stickers se pueden comprar?", ["250 ÷ 6 = 41 resto 4.", "Los $4 que sobran no alcanzan para otro sticker.", "Se pueden comprar 41 stickers y sobran $4."], "41 stickers"),
        W("El resto obliga a agregar uno", "Hay que transportar 100 personas en minibuses de 8 asientos. ¿Cuántos minibuses se necesitan?", ["100 ÷ 8 = 12 resto 4.", "Las 4 personas que sobran también deben viajar.", "12 + 1 = 13."], "13 minibuses"),
    ],
    mistakes=[
        M("Responder «12 minibuses» para llevar 100 personas en minibuses de 8 asientos.", "Se ignoró el resto: 4 personas se quedarían sin viajar.", "Se necesita un minibús más: 13."),
        M("Responder «16 mesas y 4 personas» a «¿cuántas mesas se necesitan para 100 personas con 6 por mesa?».", "La pregunta pide mesas, no personas sobrantes.", "Las 4 personas ocupan una mesa más: 17 mesas."),
    ],
    rec=[
        ex("Al dividir 250 ÷ 6 sale cociente 41 y resto 4. ¿Cuántos stickers de $6 se pueden comprar con $250?", "41", "El resto $4 no alcanza para otro sticker de $6."),
        ex("Al dividir 100 ÷ 8 sale cociente 12 y resto 4. ¿Cuántos minibuses de 8 asientos se necesitan para 100 personas?", "13", "Las 4 personas restantes necesitan otro minibús."),
        ex("En 365 ÷ 7 = 52 resto 1, ¿qué significa el resto 1 al hablar de semanas y días?", "1 día", "Sobra un día después de 52 semanas completas."),
    ],
    und=[
        ex("Hay 87 estudiantes y se arman equipos de 4. ¿Cuántos equipos completos hay y cuántos estudiantes quedan sin equipo completo?", "21 equipos y 3 estudiantes", "87 ÷ 4 = 21 resto 3."),
        ex("Se deben guardar 61 libros en cajas que caben 9. ¿Cuántas cajas se necesitan?", "7", "61 ÷ 9 = 6 resto 7; los 7 libros que sobran necesitan una séptima caja."),
        ex("Con 150 hojas se hacen cuadernillos de 8 hojas. ¿Cuántos cuadernillos completos salen?", "18", "150 ÷ 8 = 18 resto 6; las 6 hojas no completan otro."),
    ],
    app=[
        ex("En una fiesta ficticia hay 135 invitados y cada mesa tiene 8 puestos. ¿Cuántas mesas se necesitan para que todos se sienten?", "17", "135 ÷ 8 = 16 resto 7; los 7 invitados necesitan una mesa más."),
        ex("Con $300 se compran cintas de $7 cada una. ¿Cuántas cintas se pueden comprar y cuánto dinero sobra?", "42 cintas y sobran $6", "300 ÷ 7 = 42 resto 6."),
        ex("Una cinta mide 250 centímetros y se cortan trozos de 6 centímetros. ¿Cuántos trozos completos salen y cuántos centímetros sobran?", "41 trozos y sobran 4 centímetros", "250 ÷ 6 = 41 resto 4."),
    ],
    rea=[
        ex("En el problema A hay 100 personas y mesas de 6. En el B se compran stickers de $6 con $100. ¿En cuál se suma 1 al cociente?", "En A", "En A las personas que sobran deben sentarse; en B el dinero que sobra no alcanza para otro sticker."),
        ex("Leo dice que 50 ÷ 6 = 8 resto 2, así que para 50 personas con 6 por mesa bastan 8 mesas. ¿Está bien?", "No, se necesitan 9", "Las 2 personas restantes necesitan otra mesa."),
    ],
    cha=[
        ex("Un grupo necesita 7 buses de 9 asientos y en el último bus viaja solo 1 persona. ¿Cuántas personas hay en el grupo?", "55", "6 buses llenos llevan 6 × 9 = 54 personas y el último lleva 1: 55."),
        ex("Una caja se llena con 12 huevos. Con 100 huevos, ¿cuántas cajas llenas se arman y cuántos huevos sobran?", "8 cajas y sobran 4", "100 ÷ 12 = 8 resto 4."),
    ],
    ctx=[ex("En un paseo escolar ficticio van 98 niños y niñas. En cada lancha caben 8. ¿Cuántas lanchas se necesitan para que todos vayan?", "13", "98 ÷ 8 = 12 resto 2; los 2 que sobran necesitan otra lancha.")],
    sc=[
        ex("Con $50 compras gomas de $6. ¿Cuántas gomas compras?", "8", "50 ÷ 6 = 8 resto 2."),
        ex("Hay 30 personas y los autos llevan 4. ¿Cuántos autos se necesitan?", "8", "30 ÷ 4 = 7 resto 2; los 2 que sobran necesitan otro auto."),
        ex("En 100 ÷ 7 = 14 resto 2, ¿es posible que el resto fuera 8?", "No", "El resto debe ser menor que 7."),
    ],
    op=task(
        "Elige una de estas situaciones: (a) 250 estudiantes y buses de 9 asientos; (b) $480 y cuadernos de $7 cada uno; (c) 200 manzanas y bolsas de 9. Escribe la división, interpreta el resto y responde con una frase completa explicando si sumas 1, descartas o informas el resto.",
        "(b) 480 ÷ 7 = 68 resto 4. Se pueden comprar 68 cuadernos y sobran $4. El resto no alcanza para otro cuaderno, por eso no se suma 1.",
        ["plantea la división", "interpreta el resto según la pregunta", "escribe una frase completa"],
        ["división", "frase de respuesta"],
        ["sumar 1 sin razón", "olvidar el resto cuando debía agregarse"],
        "Pide que relea la pregunta y que explique qué pasaría con la cantidad que sobra.",
    ),
    reinforce="Con 25 fichas y grupos de 4 fichas, escribe cuántos grupos completos se arman y qué haces con las fichas que sobran.",
    extend="Escribe dos enunciados con la división 100 ÷ 8: uno donde se suma 1 al cociente y otro donde se descarta el resto.",
)

# ------------------------------------------------------------------ OA 04 clase 4
lesson(
    OA4, 4,
    use="Aprenderé a resolver problemas rutinarios y no rutinarios con divisiones de tres cifras por una cifra. Sirve para decidir qué operación hacer y comprobar el resultado.",
    prior=["Sé dividir con el algoritmo.", "Sé interpretar el resto en el problema."],
    explain=[
        "Un problema rutinario se resuelve con una división conocida, como «reparte 456 caramelos entre 6 bolsas». Un problema no rutinario pide más pasos o preguntar por un dato oculto, como el dividendo cuando conoces el divisor, el cociente y el resto.",
        "Para resolver sigue estos pasos. Lee y subraya la pregunta. Elige las operaciones y estima el cociente. Calcula con el algoritmo. Interpreta el resto. Comprueba con divisor × cociente + resto y responde con una frase completa que lleve la unidad.",
        "Si faltan datos, calcula primero lo necesario. Si sobran datos, no los uses. Si conoces el cociente y el resto y quieres el dividendo, multiplica el divisor por el cociente y suma el resto. Es la operación inversa que usamos para comprobar.",
    ],
    vocab=[("problema rutinario", "problema que se resuelve con una operación conocida"), ("problema no rutinario", "problema que exige elegir una estrategia o varios pasos"), ("dividendo", "lo que se reparte"), ("operación inversa", "operación que deshace a otra"), ("unidad", "lo que se cuenta o se mide")],
    worked=[
        W("Problema de varios pasos", "345 hojas se reparten en 5 carpetas iguales. Luego se sacan 2 hojas de cada carpeta. ¿Cuántas hojas quedan en cada una?", ["345 ÷ 5 = 69.", "Quedan 69 − 2 = 67 hojas en cada carpeta."], "67 hojas"),
        W("Buscar el dividendo", "Un número dividido por 8 da cociente 53 y resto 5. ¿Cuál es el número?", ["Dividendo = divisor × cociente + resto.", "8 × 53 = 424.", "424 + 5 = 429."], "429"),
    ],
    mistakes=[
        M("En «345 hojas en 5 carpetas y se sacan 2 de cada una», responder 69.", "Se olvidó el segundo paso.", "Después de repartir, hay que restar las 2 hojas: 67."),
        M("Para buscar el dividendo con divisor 8, cociente 53 y resto 5, dividir 53 ÷ 8.", "Se usó la misma operación en vez de la inversa.", "Se multiplica 8 × 53 y se suma 5: 429."),
    ],
    rec=[
        arith("Reparte 456 caramelos en 6 bolsas iguales. ¿Cuántos hay en cada bolsa?", "456//6", "450 ÷ 6 = 75 y 6 ÷ 6 = 1."),
        arith("Calcula 8 × 53.", "8*53", "8 × 50 = 400 y 8 × 3 = 24."),
        ex("Para comprobar una división exacta, ¿se multiplica o se divide?", "Se multiplica", "Divisor × cociente debe dar el dividendo."),
    ],
    und=[
        arith("Se reparten 345 hojas entre 5 carpetas y se sacan 2 de cada una. ¿Cuántas quedan en cada carpeta?", "345//5-2", "Se reparte y luego se resta."),
        arith("Un número dividido por 8 da 53 y resto 5. ¿Cuál es el número?", "8*53+5", "Dividendo = divisor × cociente + resto."),
        ex("Para estimar 612 ÷ 7, ¿por cuál de estos números conviene reemplazar 612: 560, 630 o 700?", "630", "De las tres opciones, 630 es la más cercana a 612 y se divide exacto por 7 (7 × 90)."),
    ],
    app=[
        arith("Un tren ficticio recorre 384 kilómetros en 6 horas a la misma rapidez. ¿Cuántos kilómetros recorre por hora?", "384//6", "60 × 6 = 360 y 4 × 6 = 24.", unit=" km"),
        arith("Una huerta tiene 432 plantas en filas de 9 plantas. ¿Cuántas filas hay?", "432//9", "9 × 48 = 432."),
        arith("Un álbum ficticio tiene 5 páginas con la misma cantidad de fotos, 360 fotos en total, y cada página mide 20 centímetros de largo. ¿Cuántas fotos hay en cada página?", "360//5", "El largo de la página no se necesita: solo se reparten las fotos."),
    ],
    rea=[
        ex("Un número dividido por 9 deja cociente 40 y resto 8. Ana dice que es 40 ÷ 9 + 8. ¿Tiene razón?", "No, es 9 × 40 + 8 = 368", "El dividendo se obtiene multiplicando el divisor por el cociente y sumando el resto."),
        ex("Una estimación de 497 ÷ 5 es 500 ÷ 5 = 100. Un estudiante obtiene 9 resto 2. ¿Es razonable?", "No", "El cociente debe estar cerca de 100; el correcto es 99 resto 2."),
    ],
    cha=[
        ex("Se reparten 475 galletas entre 6 bandejas y las que sobran se las come el cocinero. ¿Cuántas galletas hay en cada bandeja y cuántas se come?", "79 por bandeja y 1 se come", "475 ÷ 6 = 79 resto 1."),
        ex("Un número tiene cociente 87 al dividirse por 4 y resto 3. ¿Cuál es el resto de dividir ese número por 2?", "1", "El número es 4 × 87 + 3 = 351, que es impar y deja resto 1 al dividir por 2."),
    ],
    ctx=[arith("Una cocina ficticia prepara 252 empanadas y las pone en cajas de 6. ¿Cuántas cajas llenas arma?", "252//6", "6 × 42 = 252.")],
    sc=[
        arith("Calcula 819 ÷ 9.", "819//9", "9 × 91 = 819."),
        arith("¿Cuál es el dividendo si el divisor es 7, el cociente 60 y el resto 4?", "7*60+4", "7 × 60 = 420 y se suma el resto."),
        arith("Calcula 252 ÷ 4.", "252//4", "240 ÷ 4 = 60 y 12 ÷ 4 = 3."),
    ],
    op=task(
        "Resuelve uno de estos problemas: (a) 468 caramelos en 6 frascos iguales; (b) se reparten 250 láminas entre 7 amigos y sobran algunas; (c) un número dividido por 6 da 72 y resto 5, ¿cuál es? Escribe la operación, la estimación, el cálculo, la comprobación y la respuesta con unidad.",
        "(a) 468 ÷ 6 = 78. Estimo 480 ÷ 6 = 80. Compruebo 6 × 78 = 468. Cada frasco tiene 78 caramelos.",
        ["plantea la operación", "estima y comprueba", "responde con unidad"],
        ["operación y cálculo", "comprobación", "respuesta"],
        ["usar la operación equivocada", "olvidar la comprobación"],
        "Pide que compare estimación y resultado y que revise el resto frente al divisor.",
    ),
    reinforce="Escribe una división con dividendo de 3 cifras sobre algo de tu casa (galletas, hojas, tapitas), resuélvela y comprueba con multiplicación.",
    extend="Inventa un problema no rutinario donde conozcas divisor, cociente y resto, y pide a otra persona que encuentre el dividendo.",
)

# ------------------------------------------------------------------ OA 05 clase 1
lesson(
    OA5, 1,
    use="Aprenderé la regla de que la multiplicación y la división se hacen antes que la suma y la resta. Sirve para que todos obtengan el mismo resultado al calcular expresiones con varias operaciones.",
    prior=["Sé sumar, restar, multiplicar y dividir.", "Sé las tablas de multiplicar."],
    explain=[
        "Una expresión combinada tiene más de una operación, como 5 + 3 × 4. Si cada persona calculara en un orden distinto, daría resultados distintos. Por eso se usa una regla común: la multiplicación y la división se hacen antes que la suma y la resta.",
        "En 5 + 3 × 4, primero se hace 3 × 4 = 12 y luego 5 + 12 = 17. Si se sumara primero, saldría 32, que es incorrecto. En 20 − 12 ÷ 4 se hace 12 ÷ 4 = 3 y luego 20 − 3 = 17.",
        "Esta regla se llama prevalencia de la multiplicación y la división sobre la suma y la resta. Para no equivocarte, subraya la multiplicación o división que hay que hacer, calcúlala y reescribe la expresión. Repite hasta que quede un solo número.",
    ],
    vocab=[("expresión combinada", "cálculo con dos o más operaciones distintas"), ("prevalencia", "que una operación se hace antes que otra"), ("multiplicación y división", "operaciones que se hacen primero"), ("suma y resta", "operaciones que se hacen después"), ("reescribir", "volver a escribir la expresión con el paso ya calculado")],
    worked=[
        W("Multiplicar antes de sumar", "Calcula 7 + 2 × 8.", ["Primero la multiplicación: 2 × 8 = 16.", "Reescribo: 7 + 16.", "7 + 16 = 23."], "23"),
        W("Dos multiplicaciones y una resta", "Calcula 6 × 4 − 2 × 5.", ["Primero las multiplicaciones: 6 × 4 = 24 y 2 × 5 = 10.", "Reescribo: 24 − 10.", "24 − 10 = 14."], "14"),
    ],
    mistakes=[
        M("Calcular 5 + 3 × 4 como 8 × 4 = 32.", "Se sumó primero aunque la multiplicación debía hacerse antes.", "3 × 4 = 12 y luego 5 + 12 = 17."),
        M("Calcular 12 − 4 ÷ 2 como 8 ÷ 2 = 4.", "Se restó primero aunque la división prevalece.", "4 ÷ 2 = 2 y luego 12 − 2 = 10."),
    ],
    rec=[
        ex("En 5 + 3 × 4, ¿qué operación se hace primero?", "La multiplicación 3 × 4", "La multiplicación prevalece sobre la suma."),
        arith("Calcula 5 + 3 × 4.", "5+3*4", "3 × 4 = 12 y luego 5 + 12."),
        ex("En 18 − 6 ÷ 3, ¿cuánto vale la parte que se calcula primero?", "2", "6 ÷ 3 = 2."),
    ],
    und=[
        arith("Calcula 7 + 2 × 8.", "7+2*8", "Primero 2 × 8 = 16."),
        arith("Calcula 30 − 4 × 5.", "30-4*5", "Primero 4 × 5 = 20."),
        arith("Calcula 6 × 4 − 2 × 5.", "6*4-2*5", "Primero las dos multiplicaciones: 24 y 10."),
    ],
    app=[
        arith("Ana compra 3 cuadernos de $1.200 cada uno y 2 lápices de $350 cada uno. ¿Cuánto paga en total?", "3*1200+2*350", "Primero las multiplicaciones y luego la suma.", unit=" pesos"),
        arith("Calcula 48 ÷ 6 + 4 × 5.", "48//6+4*5", "Se hacen la división y la multiplicación antes de sumar."),
        arith("Calcula 5 × 12 + 100 ÷ 4.", "5*12+100//4", "Primero 5 × 12 = 60 y 100 ÷ 4 = 25; luego se suman."),
    ],
    rea=[
        ex("Lía calculó 5 + 3 × 4 = 32. ¿Qué hizo mal y cuál es el resultado correcto?", "Sumó primero; es 17", "Debe multiplicar antes: 3 × 4 = 12 y 5 + 12 = 17."),
        ex("Pedro dice que 12 − 4 ÷ 2 = 4. ¿Cuál es el resultado correcto?", "10", "4 ÷ 2 = 2 y luego 12 − 2 = 10."),
    ],
    cha=[
        ex("Escribe + o − en el espacio para que 4 __ 3 × 5 = 19.", "+", "3 × 5 = 15 y 4 + 15 = 19."),
        ex("¿Qué número va en el cuadro para que 3 + __ × 4 = 23?", "5", "23 − 3 = 20 y 20 ÷ 4 = 5."),
    ],
    ctx=[arith("Un kiosco ficticio vende 4 jugos de $700 y 3 galletas de $500. ¿Cuánto dinero recibe?", "4*700+3*500", "Primero los dos productos y luego la suma.")],
    sc=[
        arith("Calcula 9 + 6 × 3.", "9+6*3", "6 × 3 = 18 y luego 9 + 18."),
        arith("Calcula 40 − 24 ÷ 6.", "40-24//6", "24 ÷ 6 = 4 y luego 40 − 4."),
        ex("En 2 + 3 × 4 + 5, ¿qué se calcula primero?", "3 × 4", "La multiplicación va antes que las sumas."),
    ],
    op=task(
        "Elige uno: 8 + 5 × 6, 50 − 36 ÷ 4 o 3 × 7 + 4 × 5. Resuélvelo escribiendo la expresión en cada paso y subrayando la operación que haces primero. Explica por qué no se puede calcular de izquierda a derecha.",
        "8 + 5 × 6: subrayo 5 × 6 = 30; reescribo 8 + 30 = 38. Si sumara primero, 8 + 5 = 13 y 13 × 6 = 78, que es otro resultado.",
        ["subraya la operación prioritaria", "reescribe cada paso", "explica la regla"],
        ["pasos escritos", "frase de explicación"],
        ["calcular de izquierda a derecha sin prioridad", "olvidar reescribir"],
        "Pide que identifique primero la multiplicación o división y que compare con el resultado de calcular en otro orden.",
    ),
    reinforce="Calcula 2 + 3 × 4 de dos formas: sumando primero y multiplicando primero. Mira cuál sigue la regla y por qué.",
    extend="Inventa una expresión con una suma, una resta y una multiplicación y calcúlala siguiendo la regla.",
)

# ------------------------------------------------------------------ OA 05 clase 2
lesson(
    OA5, 2,
    use="Aprenderé a usar paréntesis para cambiar el orden de las operaciones. Sirve para indicar qué parte de un cálculo se hace primero.",
    prior=["Sé que la multiplicación y la división prevalecen sobre la suma y la resta."],
    explain=[
        "Los paréntesis agrupan una parte de la expresión. Lo que está dentro de ellos se calcula primero, aunque sea una suma o una resta. Así, (5 + 3) × 4 significa primero 5 + 3 = 8 y luego 8 × 4 = 32. Sin paréntesis, 5 + 3 × 4 da 17.",
        "Los paréntesis cambian el resultado. En 40 ÷ (2 + 3) primero se suma 2 + 3 = 5 y luego 40 ÷ 5 = 8. Si no estuvieran, 40 ÷ 2 + 3 daría 23. Por eso son importantes: indican lo que el que escribe quiere calcular primero.",
        "El orden completo es: primero lo que está dentro de paréntesis, luego las multiplicaciones y divisiones, y por último las sumas y restas. Si hay un paréntesis dentro de otro, empieza por el más interno. Siempre reescribe la expresión después de cada paso.",
    ],
    vocab=[("paréntesis", "signos ( ) que agrupan una parte del cálculo"), ("agrupar", "juntar para calcular primero"), ("orden de las operaciones", "secuencia en que se calculan las operaciones"), ("reescribir", "volver a escribir la expresión con lo ya calculado"), ("expresión", "cálculo escrito con números y signos")],
    worked=[
        W("Paréntesis con suma", "Calcula (5 + 3) × 4.", ["Primero el paréntesis: 5 + 3 = 8.", "Reescribo: 8 × 4.", "8 × 4 = 32."], "32"),
        W("Paréntesis con división", "Calcula 40 ÷ (2 + 3).", ["Primero el paréntesis: 2 + 3 = 5.", "Reescribo: 40 ÷ 5.", "40 ÷ 5 = 8."], "8"),
    ],
    mistakes=[
        M("Calcular 2 × (15 − 6) como 2 × 15 − 6 = 24.", "No se calculó primero el paréntesis.", "15 − 6 = 9 y 2 × 9 = 18."),
        M("Pensar que 6 + 2 × 5 y (6 + 2) × 5 dan lo mismo.", "Los paréntesis cambian el orden de las operaciones.", "6 + 2 × 5 = 16, pero (6 + 2) × 5 = 40."),
    ],
    rec=[
        arith("Calcula (5 + 3) × 4.", "(5+3)*4", "Primero el paréntesis: 8."),
        arith("Calcula 2 × (15 − 6).", "2*(15-6)", "Primero el paréntesis: 9."),
        ex("En 40 ÷ (2 + 3), ¿qué se calcula primero?", "2 + 3", "Lo que está en paréntesis se calcula primero."),
    ],
    und=[
        arith("Calcula 40 ÷ (2 + 3).", "40//(2+3)", "El paréntesis vale 5."),
        arith("Calcula (9 − 3) × (2 + 4).", "(9-3)*(2+4)", "Los paréntesis valen 6 y 6."),
        ex("¿Dan el mismo resultado 6 + 2 × 5 y (6 + 2) × 5?", "No, 16 y 40", "En el primero se multiplica antes de sumar; en el segundo se suma primero."),
    ],
    app=[
        arith("Calcula 3 × (12 + 8) − 10.", "3*(12+8)-10", "El paréntesis vale 20; luego 3 × 20 y se resta 10."),
        arith("Calcula (100 − 40) ÷ 6 + 5.", "(100-40)//6+5", "El paréntesis vale 60; luego 60 ÷ 6 y se suma 5."),
        arith("Cuatro amigos pagan cada uno una entrada de $2.500 y un helado de $600. ¿Cuánto pagan entre todos?", "4*(2500+600)", "Cada uno paga 3.100 y son 4.", unit=" pesos"),
    ],
    rea=[
        ex("¿Dan el mismo resultado 12 + 6 ÷ 3 y (12 + 6) ÷ 3?", "No, 14 y 6", "Sin paréntesis se divide primero; con ellos se suma primero."),
        ex("Marta calculó 2 × (5 + 3) como 2 × 5 + 3 = 13. ¿Cuál es el resultado correcto?", "16", "5 + 3 = 8 y 2 × 8 = 16."),
    ],
    cha=[
        ex("Pon un paréntesis en 2 + 3 × 4 para que el resultado sea 20.", "(2 + 3) × 4", "5 × 4 = 20."),
        ex("Pon un paréntesis en 30 − 10 ÷ 2 para que el resultado sea 10.", "(30 − 10) ÷ 2", "20 ÷ 2 = 10."),
    ],
    ctx=[arith("En una excursión ficticia hay 3 buses con 25 estudiantes y 2 buses con 30 estudiantes. Se cobran $1.000 por estudiante. ¿Cuánto se cobra? Calcula (3 × 25 + 2 × 30) × 1.000.", "(3*25+2*30)*1000", "Hay 135 estudiantes y cada uno paga 1.000.", unit=" pesos")],
    sc=[
        arith("Calcula (7 + 5) × 3.", "(7+5)*3", "El paréntesis vale 12."),
        arith("Calcula 60 ÷ (4 + 6).", "60//(4+6)", "El paréntesis vale 10."),
        ex("¿Qué se calcula primero en 8 × (6 − 2) + 1?", "6 − 2", "El paréntesis va primero."),
    ],
    op=task(
        "Elige: (6 + 4) × 5 + 2, 3 × (14 − 6) − 5 o 100 ÷ (2 + 3) + 7. Resuélvelo escribiendo la expresión en cada paso. Luego quita los paréntesis, calcula de nuevo y compara los resultados.",
        "(6 + 4) × 5 + 2 = 10 × 5 + 2 = 50 + 2 = 52. Sin paréntesis, 6 + 4 × 5 + 2 = 6 + 20 + 2 = 28. Los paréntesis cambiaron el resultado.",
        ["calcula primero el paréntesis", "reescribe cada paso", "compara con y sin paréntesis"],
        ["pasos escritos", "frase comparando"],
        ["ignorar el paréntesis", "no reescribir"],
        "Pide que subraye el paréntesis antes de empezar y que compare los dos resultados.",
    ),
    reinforce="Calcula (2 + 3) × 4 y 2 + 3 × 4. Escribe una frase que diga por qué dan resultados distintos.",
    extend="Inventa una expresión en que poner o quitar paréntesis cambie el resultado y escribe ambos.",
)

# ------------------------------------------------------------------ OA 05 clase 3
lesson(
    OA5, 3,
    use="Aprenderé a escribir una expresión con operaciones combinadas para una situación con palabras, y a calcularla. Sirve para resolver problemas con varios pasos en un solo cálculo.",
    prior=["Sé la regla de prioridad entre operaciones.", "Sé usar paréntesis."],
    explain=[
        "Muchas situaciones de la vida real necesitan más de una operación. Para escribir la expresión, identifica cada parte de la situación y escribe qué operación le corresponde. Después une las partes con el signo que las relaciona. Los paréntesis se usan cuando una parte debe calcularse primero.",
        "Por ejemplo: «Compro 3 cuadernos de $800 y 1 lápiz de $350». Los cuadernos son 3 × 800 y el lápiz es 350. Se suman: 3 × 800 + 350 = 2.750. Aquí no hacen falta paréntesis porque la multiplicación ya prevalece.",
        "Otro ejemplo: «La suma de 5 y 4, multiplicada por 3». La suma debe calcularse antes, así que se escribe entre paréntesis: (5 + 4) × 3 = 27. Después de calcular, revisa que el resultado responda la pregunta y que tenga sentido en la situación, con su unidad.",
    ],
    vocab=[("expresión", "cálculo escrito con números y signos"), ("situación", "historia o problema donde se necesita calcular"), ("traducir", "pasar de palabras a una expresión matemática"), ("producto", "resultado de multiplicar"), ("suma", "resultado de sumar")],
    worked=[
        W("De palabras a expresión", "Tienes $5.000 y compras 3 pasajes de $1.200. ¿Cuánto te queda?", ["Los pasajes cuestan 3 × 1.200.", "Lo que queda es 5.000 menos eso.", "Expresión: 5.000 − 3 × 1.200 = 5.000 − 3.600 = 1.400."], "$1.400"),
        W("Con paréntesis", "Escribe «la suma de 5 y 4, multiplicada por 3» y calcula.", ["La suma va primero: 5 + 4.", "Para que se calcule primero, uso paréntesis: (5 + 4).", "(5 + 4) × 3 = 9 × 3 = 27."], "27"),
    ],
    mistakes=[
        M("Escribir 5 + 4 × 3 para «la suma de 5 y 4, multiplicada por 3».", "Sin paréntesis, la multiplicación se haría antes y daría 17.", "La suma debe ir entre paréntesis: (5 + 4) × 3 = 27."),
        M("Escribir 3 × 800 + 350 como (3 + 800) × 350.", "Se mezclaron las operaciones sin seguir la situación.", "Son 3 cuadernos de $800 y un lápiz de $350: 3 × 800 + 350."),
    ],
    rec=[
        ex("¿Qué expresión representa «el doble de 7, aumentado en 3»? Elige A: 2 × 7 + 3, B: 2 × (7 + 3).", "A", "El doble de 7 es 2 × 7 y luego se suman 3 a ese resultado."),
        ex("Escribe «la suma de 5 y 4, multiplicada por 3» con paréntesis.", "(5 + 4) × 3", "La suma debe calcularse antes."),
        arith("Calcula 3 × (5 + 4).", "3*(5+4)", "El paréntesis vale 9."),
    ],
    und=[
        arith("Tienes $5.000 y compras 3 pasajes de $1.200. ¿Cuánto te queda?", "5000-3*1200", "Primero 3 × 1.200 y luego la resta.", unit=" pesos"),
        arith("Se reparten 20 láminas entre 4 niños y luego cada niño recibe 3 más. ¿Cuántas tiene cada uno?", "20//4+3", "Primero el reparto y luego la suma."),
        ex("¿Qué expresión representa «el triple de la diferencia entre 9 y 4»?", "3 × (9 − 4)", "La resta va primero y por eso lleva paréntesis."),
    ],
    app=[
        arith("En un curso de 30 estudiantes, 12 llevan 2 lápices y el resto lleva 1. ¿Cuántos lápices hay en total?", "12*2+(30-12)*1", "Primero 12 × 2 y los demás son 30 − 12."),
        arith("Una tienda ficticia vende 3 cajas de 12 huevos y 2 cajas de 6 huevos. ¿Cuántos huevos vende?", "3*12+2*6", "Se multiplican y luego se suman."),
        arith("Tienes $20.000, compras 2 poleras de $6.500 y un gorro de $4.000. ¿Cuánto dinero te queda?", "20000-(2*6500+4000)", "Se calcula primero lo gastado entre paréntesis.", unit=" pesos"),
    ],
    rea=[
        ex("¿Cuál expresión corresponde a «a 50 le resto el producto de 6 y 4»? A: 50 − 6 × 4, B: (50 − 6) × 4.", "A", "El producto 6 × 4 se resta de 50."),
        ex("Para dividir 60 entre la suma de 4 y 6, ¿necesitas paréntesis?", "Sí: 60 ÷ (4 + 6)", "Sin paréntesis se calcularía 60 ÷ 4 + 6, que es otra cosa."),
    ],
    cha=[
        arith("Escribe y calcula «el triple de la suma de 7 y 5, menos 6».", "3*(7+5)-6", "La suma da 12; el triple es 36 y se resta 6."),
        arith("Un parque ficticio tiene 4 filas de 8 bancas y 3 filas de 5 bancas. Se retiran 7 bancas. ¿Cuántas quedan?", "4*8+3*5-7", "32 + 15 = 47 y luego 47 − 7."),
    ],
    ctx=[arith("Ema compra 2 pizzas de $7.500 y 3 bebidas de $1.500 y paga con $20.000. ¿Cuánto vuelto recibe?", "20000-(2*7500+3*1500)", "Gasta 15.000 + 4.500 = 19.500 y recibe el resto.", unit=" pesos")],
    sc=[
        ex("Escribe «el doble de la suma de 6 y 3» con paréntesis.", "2 × (6 + 3)", "La suma debe calcularse antes de duplicar."),
        arith("Calcula 4 × 5 + 3 × 6.", "4*5+3*6", "20 + 18."),
        arith("Tienes $1.000 y compras 2 gomas de $250. ¿Cuánto te queda?", "1000-2*250", "2 × 250 = 500.", unit=" pesos"),
    ],
    op=task(
        "Elige una situación: (a) compras 3 helados de $1.100 y 2 jugos de $800 y pagas con $10.000; (b) 4 grupos de 6 estudiantes y 3 grupos de 5 estudiantes; (c) a un total de 90 hojas le quitas 5 paquetes de 12 hojas. Escribe la expresión con paréntesis si hacen falta, calcula y responde con una frase y unidad.",
        "(a) 10.000 − (3 × 1.100 + 2 × 800) = 10.000 − (3.300 + 1.600) = 10.000 − 4.900 = 5.100. Recibo $5.100 de vuelto.",
        ["escribe la expresión", "usa paréntesis cuando corresponde", "responde con unidad"],
        ["expresión y cálculo", "frase de respuesta"],
        ["no usar paréntesis cuando hacen falta", "olvidar la unidad"],
        "Pide que lea la expresión en voz alta contando la historia de la situación.",
    ),
    reinforce="Escribe en palabras qué significa 2 × (8 + 3) y qué significa 2 × 8 + 3. Calcula ambas.",
    extend="Inventa una situación de compras que se resuelva con 5.000 − (2 × 1.200 + 800) y calcúlala.",
)

# ------------------------------------------------------------------ OA 05 clase 4
lesson(
    OA5, 4,
    use="Aprenderé a calcular expresiones con las cuatro operaciones cuando varias tienen la misma prioridad, y a revisar si un resultado está bien. Sirve para evitar errores en cálculos largos.",
    prior=["Sé el orden: paréntesis, multiplicación y división, suma y resta."],
    explain=[
        "Cuando una expresión tiene varias multiplicaciones y divisiones seguidas, se resuelven de izquierda a derecha. En 24 ÷ 4 × 3, primero 24 ÷ 4 = 6 y luego 6 × 3 = 18. Si hicieras 4 × 3 primero, saldría 2, que es incorrecto.",
        "Lo mismo vale para sumas y restas seguidas: se van haciendo de izquierda a derecha. En 20 − 8 + 3, primero 20 − 8 = 12 y luego 12 + 3 = 15. Si sumaras primero 8 + 3, obtendrías 9, que es un error.",
        "El orden completo es: paréntesis, luego multiplicaciones y divisiones de izquierda a derecha, y al final sumas y restas de izquierda a derecha. Para comprobar, estima cada parte o calcula con otra agrupación válida. Siempre escribe un paso por línea y no omitas reescribir.",
    ],
    vocab=[("izquierda a derecha", "orden en que se hacen operaciones de la misma prioridad"), ("misma prioridad", "operaciones que se hacen en el mismo nivel, como suma y resta"), ("comprobar", "revisar el resultado de otra forma"), ("paso", "una operación hecha y reescrita"), ("estimar", "calcular un valor cercano")],
    worked=[
        W("Mismo nivel de izquierda a derecha", "Calcula 24 ÷ 4 × 3.", ["La división y la multiplicación tienen la misma prioridad; se va de izquierda a derecha.", "24 ÷ 4 = 6.", "6 × 3 = 18."], "18"),
        W("Expresión larga", "Calcula (8 + 4) × 3 − 24 ÷ 6.", ["Paréntesis: 8 + 4 = 12.", "Reescribo: 12 × 3 − 24 ÷ 6; hago 12 × 3 = 36 y 24 ÷ 6 = 4.", "36 − 4 = 32."], "32"),
    ],
    mistakes=[
        M("Calcular 20 − 8 + 3 como 20 − 11 = 9.", "Se sumó primero 8 + 3, pero se debe ir de izquierda a derecha.", "20 − 8 = 12 y 12 + 3 = 15."),
        M("Calcular 24 ÷ 4 × 3 como 24 ÷ 12 = 2.", "Se hizo primero la multiplicación, y no se fue de izquierda a derecha.", "24 ÷ 4 = 6 y 6 × 3 = 18."),
    ],
    rec=[
        ex("En 24 ÷ 4 × 3, ¿qué operación se hace primero?", "24 ÷ 4", "Se va de izquierda a derecha."),
        arith("Calcula 24 ÷ 4 × 3.", "24//4*3", "24 ÷ 4 = 6 y 6 × 3."),
        arith("Calcula 20 − 8 + 3.", "20-8+3", "20 − 8 = 12 y 12 + 3."),
    ],
    und=[
        arith("Calcula 36 ÷ 6 × 2.", "36//6*2", "36 ÷ 6 = 6 y 6 × 2."),
        arith("Calcula 50 − 20 + 10 − 5.", "50-20+10-5", "De izquierda a derecha."),
        ex("¿Es correcto que 24 ÷ 4 × 3 = 2?", "No, es 18", "Se debe dividir primero y luego multiplicar."),
    ],
    app=[
        arith("Calcula 2 × 3 + 4 × 5 − 6.", "2*3+4*5-6", "6 + 20 − 6."),
        arith("Calcula (8 + 4) × 3 − 24 ÷ 6.", "(8+4)*3-24//6", "36 − 4."),
        arith("Se pagan 3 entradas de $2.500 con un billete de $10.000. ¿Cuánto es el vuelto?", "10000-3*2500", "3 × 2.500 = 7.500.", unit=" pesos"),
    ],
    rea=[
        ex("Ana calculó 20 − 8 + 3 = 9. ¿Está bien?", "No, es 15", "Debe ir de izquierda a derecha: 20 − 8 = 12 y 12 + 3 = 15."),
        ex("Beto calculó 6 + 4 ÷ 2 × 3 como 15 y dice que sumó primero. ¿Cuál es el valor correcto?", "12", "4 ÷ 2 = 2, 2 × 3 = 6 y 6 + 6."),
    ],
    cha=[
        ex("Escribe + o − en el espacio para que 18 __ 6 ÷ 3 = 16.", "−", "6 ÷ 3 = 2 y 18 − 2 = 16."),
        ex("Con los números 2, 3 y 4 en ese orden, usando solo + y ×, con o sin paréntesis, ¿cuál es el mayor resultado?", "24", "2 × 3 × 4 = 24; con sumas o paréntesis dan menos."),
    ],
    ctx=[arith("Un mini mercado ficticio tiene 5 cajas con 24 manzanas. Vende 3 cajas completas y regala 6 manzanas. ¿Cuántas manzanas quedan?", "5*24-3*24-6", "120 − 72 − 6 = 42.")],
    sc=[
        arith("Calcula 48 ÷ 6 ÷ 2.", "48//6//2", "48 ÷ 6 = 8 y 8 ÷ 2."),
        arith("Calcula 15 − 5 + 7 − 2.", "15-5+7-2", "De izquierda a derecha."),
        ex("En 18 ÷ 3 × 2, ¿cuánto vale la parte que se hace primero?", "6", "18 ÷ 3 = 6."),
    ],
    op=task(
        "Elige: 48 ÷ 6 × 2 + 5, 30 − 12 + 8 ÷ 2 o (7 + 5) × 2 − 36 ÷ 4. Resuélvelo escribiendo un paso por línea, estima el resultado antes y explica qué operación hiciste primero y por qué.",
        "48 ÷ 6 × 2 + 5: 48 ÷ 6 = 8; 8 × 2 = 16; 16 + 5 = 21. Estimo 50 ÷ 6 ≈ 8; 8 × 2 + 5 ≈ 21. Empecé por la división porque las operaciones de ×÷ van antes que la suma y de izquierda a derecha.",
        ["escribe un paso por línea", "respeta el orden", "estima antes de calcular"],
        ["pasos escritos", "estimación", "frase de explicación"],
        ["hacer primero la multiplicación y no la división de la izquierda", "sumar antes de restar"],
        "Pide que lea el orden en voz alta y que verifique con otra agrupación válida.",
    ),
    reinforce="Calcula 24 ÷ 4 × 3 y 24 ÷ (4 × 3). Anota por qué los resultados son distintos.",
    extend="Explica con un ejemplo por qué 20 − 8 + 3 no es lo mismo que 20 − (8 + 3).",
)
