"""Student material for 2.º básico Matemática, OA 01 clases 2 a 4 (lote 1)."""
from __future__ import annotations

from student_content_ma02_a import OA1, fill
from student_lessons import arith, ex, register

register(
    OA1, 2,
    materials="Tabla de números del 300 al 360 en este cuaderno, 8 tapas o fichas por estudiante y lápiz de color.",
    use="Aprenderé a contar de 5 en 5 hacia adelante y hacia atrás desde cualquier número. Sirve para contar monedas de $5, dedos de varias manos o puntos de un juego.",
    prior=["Sé contar de 2 en 2.", "Sé que un salto de 5 mueve el número cinco lugares."],
    explain=[
        "Contar de 5 en 5 significa sumar 5 cada vez. Si partes en 320, dices 325, 330, 335 y 340. Observa las unidades: 5, 0, 5, 0. Cuando partes en un número que termina en 0 o en 5, las unidades sólo pueden ser 0 y 5.",
        "Pero también puedes partir en un número distinto. Si partes en 468, dices 473, 478, 483 y 488. Ahora las unidades son 3, 8, 3, 8: se repiten dos cifras que están separadas por 5. Lo que se conserva siempre es el salto, no la terminación.",
        "Para ir hacia atrás, resta 5: desde 335 dices 330, 325 y 320. Una forma de comprobar es juntar tapas de a cinco: cada paquete es un salto. Si avanzas algunos saltos y vuelves la misma cantidad de saltos, llegas al punto de inicio.",
    ],
    vocab=[("de 5 en 5", "sumar 5 en cada salto"), ("hacia atrás", "restar en cada salto"), ("paquete", "grupo de 5 tapas que representa un salto"), ("terminación", "la cifra de las unidades del número"), ("comprobar", "revisar con otro método que el resultado es correcto")],
    worked=[
        {"title": "Partir en un múltiplo de 5", "problem": "Cuenta de 5 en 5 desde 320 y escribe cuatro números más.", "steps": ["Punto de inicio: 320.", "320 + 5 = 325; 325 + 5 = 330.", "330 + 5 = 335; 335 + 5 = 340.", "Reviso que las unidades alternan 5 y 0."], "answer": "320, 325, 330, 335, 340"},
        {"title": "Avanzar y volver", "problem": "Parte en 468, avanza cuatro saltos de 5 y luego retrocede dos saltos de 5. ¿En qué número quedas?", "steps": ["Avanzo: 473, 478, 483, 488.", "Retrocedo dos saltos: 488 − 5 = 483 y 483 − 5 = 478.", "Compruebo con una cuenta: 4 saltos adelante y 2 atrás equivalen a 2 saltos adelante; 468 + 10 = 478."], "answer": "478"},
    ],
    mistakes=[
        {"wrong": "Partir en 468 y escribir 470, 475, 480.", "why": "Se «arregla» el número para que termine en 0 o 5.", "fix": "Siempre se suma 5 al punto de inicio: 468 + 5 = 473, aunque no termine en 0 o 5."},
        {"wrong": "Contar hacia atrás desde 335 como 340, 345.", "why": "Se confunde retroceder con avanzar.", "fix": "Hacia atrás se resta 5: 335 − 5 = 330."},
    ],
    tiers={
        "recovery": [fill(320, 5, 6, (1, 3, 5), "Se suma 5 en cada paso: 325, 335, 345."), fill(100, 5, 6, (2, 3), "100, 105, 110, 115: se suma 5."), fill(635, -5, 5, (1, 3), "Se resta 5 en cada paso: 630 y 620.")],
        "understand": [
            ex("Si cuento de 5 en 5 desde 210, ¿cuáles dos terminaciones se repiten?", "0 y 5", "210, 215, 220, 225: las unidades alternan 0 y 5."),
            ex("Si cuento de 5 en 5 desde 468, ¿qué terminaciones se repiten?", "3 y 8", "468, 473, 478, 483: se alternan 3 y 8."),
            ex("Luis contó 450, 455, 460, 465. ¿Contó hacia adelante o hacia atrás?", "Hacia adelante", "Cada número es mayor que el anterior; se sumó 5."),
        ],
        "apply": [
            fill(468, 5, 6, (1, 2, 5), "Se parte en 468 y se suma 5: 473, 478, 493."),
            arith("Tengo 6 paquetes con 5 tapas cada uno. Cuento de 5 en 5: 5, 10, 15, 20, 25, 30. ¿Cuántas tapas hay?", "6*5", "Seis saltos de 5 son 30 tapas."),
            ex("Parto en 700 y retrocedo tres saltos de 5. ¿En qué número quedo?", "685", "700 − 5 = 695; 695 − 5 = 690; 690 − 5 = 685."),
        ],
        "reason": [
            ex("Sofía dice: «Si parto en 142 y cuento de 5 en 5, diré 145, 150». ¿Está bien? Explica.", "No; dirá 147 y 152", "142 + 5 = 147, luego 152. Los números se calculan desde el punto de inicio, no desde el siguiente múltiplo de 5."),
            ex("Una secuencia dice 255, 260, 266, 270. ¿Dónde está el error y cuál es el número correcto?", "266 debe ser 265", "El salto tenía que ser 5: 260 + 5 = 265."),
        ],
        "challenge": [
            ex("Parto en 596 y cuento de 5 en 5. ¿Cuál es el primer número que supera 600?", "601", "596 + 5 = 601, que ya pasó 600."),
            ex("Si cuento de 5 en 5 hacia atrás desde 203, ¿puedo llegar a 0? Explica.", "No", "203 termina en 3; al restar 5 las terminaciones son 3 y 8, y 0 termina en 0."),
        ],
    },
    context=[ex("En una alcancía hay monedas de $5. Cuento de 5 en 5: 5, 10, 15, 20, 25, 30, 35, 40. ¿Cuánto dinero hay si conté 8 monedas?", "$40", "Ocho monedas de $5 hacen 8 saltos de 5, que llegan a 40.")],
    selfcheck=[ex("Completa: 410, 415, __, 425.", "420", "415 + 5 = 420."), ex("Resta 5 a 775.", "770", "775 − 5 = 770."), ex("¿De cuánto en cuánto va 90, 95, 100, 105?", "De 5 en 5", "Cada número es 5 más que el anterior.")],
    open_task={
        "statement": "Parte en 273 y cuenta de 5 en 5 hasta tener siete números. Luego retrocede dos saltos y explica en una frase por qué las unidades se repiten.",
        "example": "273, 278, 283, 288, 293, 298, 303. Al retroceder dos saltos desde 303 quedo en 293. Las unidades se repiten (3 y 8) porque cada dos saltos sumo 10.",
        "criteria": ["escribe siete números", "mantiene el salto de 5", "retrocede correctamente", "explica la regularidad con sus palabras"],
        "evidence": ["secuencia escrita", "retroceso resuelto con resta", "frase de explicación"],
        "errors": ["ajustar el punto de inicio a un múltiplo de 5", "no retroceder, sino volver a avanzar"],
        "feedback": "Elogia la regularidad detectada y pide demostrar con tapas que dos saltos de 5 equivalen a 10; si hubo ajuste del punto de inicio, invita a volver a calcular 273 + 5.",
    },
    reinforce="Cuenta con tapas en paquetes de 5 desde 0 hasta 50 y escribe el número en cada paquete.",
    extend="Descubre qué terminaciones aparecen al contar de 5 en 5 desde un número que termina en 1. Prueba con 51 y con 161.",
)

register(
    OA1, 3,
    materials="Recta numérica abierta dibujada en el cuaderno; tabla con las filas 180–230 y 770–810; lápiz de color.",
    use="Aprenderé a contar de 10 en 10 aunque los números cambien de centena. Sirve para contar billetes de $10 o paquetes de diez sin perderme al pasar de 199 a 200.",
    prior=["Sé contar de 10 en 10 hasta 100.", "Sé que en un número de tres cifras la primera cifra son las centenas."],
    explain=[
        "Contar de 10 en 10 significa sumar 10: aumenta en 1 la cifra de las decenas y las unidades no cambian. Desde 186 dices 196, 206, 216. La cifra del 6 se mantiene en todos los números.",
        "Lo interesante ocurre cuando las decenas llegan a 9. En 196 hay 9 decenas. Si sumas 10 pasas a 206: las decenas vuelven a 0 y la centena sube de 1 a 2. Es igual que al pasar de 99 a 100, pero con una centena más.",
        "Para hacerlo bien, mira siempre las tres cifras: unidades (no cambian), decenas (suben 1) y centenas (suben 1 sólo cuando las decenas pasan de 9 a 0). Hacia atrás ocurre al revés: de 206 retrocedes a 196 y la centena baja.",
    ],
    vocab=[("decena", "grupo de 10 unidades"), ("centena", "grupo de 100 unidades, o 10 decenas"), ("cruzar una centena", "pasar de un número como 196 a uno como 206"), ("conservar", "dejar igual"), ("recta abierta", "recta donde yo escribo los números que necesito")],
    worked=[
        {"title": "Cruzar la centena 200", "problem": "Cuenta de 10 en 10 desde 186 y escribe cuatro números más.", "steps": ["186 + 10 = 196: las decenas pasan de 8 a 9.", "196 + 10 = 206: las decenas pasan de 9 a 0 y la centena de 1 a 2.", "206 + 10 = 216 y 216 + 10 = 226.", "Reviso que el 6 de las unidades no cambia."], "answer": "186, 196, 206, 216, 226"},
        {"title": "Retroceder cruzando una centena", "problem": "Cuenta hacia atrás de 10 en 10 desde 504, cuatro números más.", "steps": ["504 − 10 = 494: las decenas pasan de 0 a 9 y la centena baja de 5 a 4.", "494 − 10 = 484.", "484 − 10 = 474 y 474 − 10 = 464.", "Las unidades siguen siendo 4."], "answer": "504, 494, 484, 474, 464"},
    ],
    mistakes=[
        {"wrong": "Escribir 186, 196, 106, 116.", "why": "Se olvidó subir la centena al llegar a 9 decenas.", "fix": "196 + 10 = 206 porque 10 decenas forman 1 centena."},
        {"wrong": "Escribir 774, 784, 794, 704.", "why": "Se pensó que después de 9 decenas se vuelve a 0 sin cambiar la centena.", "fix": "794 + 10 = 804: la centena pasa de 7 a 8."},
    ],
    tiers={
        "recovery": [fill(186, 10, 6, (1, 3), "Se suma 10: 196 y 216."), fill(40, 10, 6, (2, 4), "Se suma 10 desde 40: 60 y 80."), fill(555, -10, 5, (1, 3), "Se resta 10: 545 y 525.")],
        "understand": [
            ex("En la secuencia 774, 784, 794, ¿qué cifra no cambia y cuál cambia?", "No cambia el 4; cambian las decenas", "Las unidades se mantienen en 4 y las decenas suben de 7 a 8 a 9."),
            ex("¿Qué número viene después de 794 al contar de 10 en 10?", "804", "794 + 10 = 804."),
            ex("¿Qué número viene antes de 306 al contar de 10 en 10?", "296", "306 − 10 = 296."),
        ],
        "apply": [
            fill(774, 10, 6, (3, 4, 5), "774, 784, 794, 804, 814, 824."),
            fill(912, 10, 6, (1, 2, 3), "912, 922, 932, 942."),
            arith("Una caja tiene 10 lápices. Hay 28 cajas llenas y 5 lápices sueltos. ¿Cuántos lápices hay en total?", "28*10+5", "28 cajas son 280 lápices y 5 más hacen 285."),
        ],
        "reason": [
            ex("Pedro escribió 186, 196, 106. ¿Dónde está su error y cuál es el número correcto?", "106 debe ser 206", "Al sumar 10 a 196 la centena sube a 2; el resultado es 206."),
            ex("Lucía dice que contar desde 495 de 10 en 10 da 505, 515, 525. ¿Tiene razón?", "Sí", "495 + 10 = 505, luego 515 y 525; las unidades se conservan en 5."),
        ],
        "challenge": [
            ex("Parto en 885 y cuento de 10 en 10. ¿Cuál es el primer número que digo que sea 1.000 o más?", "1.005", "885 + 10 doce veces es 1.005; antes llegué a 995, que todavía es menor que 1.000."),
            ex("¿Cuántos saltos de 10 hay entre 396 y 456?", "6 saltos", "396, 406, 416, 426, 436, 446, 456: son 6 saltos de 10."),
        ],
    },
    context=[ex("En una fábrica se arman fajos de 10 billetes. Hay 19 fajos y se agrega 1 más. ¿Cuántos billetes hay en total?", "200 billetes", "19 fajos son 190 billetes y un fajo más son 10: 190 + 10 = 200.")],
    selfcheck=[ex("Completa: 286, 296, __, 316.", "306", "296 + 10 = 306."), ex("Resta 10 a 400.", "390", "400 − 10 = 390."), ex("¿Cuál de estas secuencias salta de 10 en 10: 590, 600, 610 o 590, 595, 600?", "590, 600, 610", "Cada número es 10 más que el anterior.")],
    open_task={
        "statement": "Parte en 177 y cuenta de 10 en 10 hasta tener seis números, pasando por 200. Marca en tu secuencia el lugar donde cambia la centena y escribe una frase que explique por qué cambia.",
        "example": "177, 187, 197, 207, 217, 227. La centena cambia entre 197 y 207, porque 197 tiene 9 decenas y al sumar 10 se forma una centena completa.",
        "criteria": ["escribe seis números", "mantiene el salto de 10", "marca el cambio de centena", "justifica con decenas y centenas"],
        "evidence": ["secuencia escrita", "marca visible del cambio", "frase con explicación"],
        "errors": ["no cambiar la centena", "cambiar las unidades"],
        "feedback": "Si la centena no cambió, pide dibujar 10 decenas en un rectángulo y reconocer que forman una centena; luego que reescriba la secuencia.",
    },
    reinforce="Escribe en una tabla de 10 columnas los números del 770 al 870 contando de 10 en 10 y pinta la columna donde cambia la centena.",
    extend="Descubre cuántos saltos de 10 se necesitan para ir de 50 a 1.000. Explica cómo lo calculaste sin contarlos uno por uno.",
)

register(
    OA1, 4,
    materials="Cinco billetes dibujados de $100, recta numérica con marcas de 100 en 100 del 0 al 1.000 en el cuaderno y lápiz.",
    use="Aprenderé a contar de 100 en 100 hacia adelante y hacia atrás hasta 1.000. Sirve para contar billetes o cajas grandes y para ubicarme en la recta.",
    prior=["Sé contar de 10 en 10 cruzando una centena.", "Sé que 10 decenas forman 1 centena."],
    explain=[
        "Contar de 100 en 100 significa sumar 100. Cambia sólo la cifra de las centenas: desde 350 dices 450, 550, 650. Las decenas y las unidades quedan iguales.",
        "Hacia atrás, restas 100: desde 650 dices 550, 450, 350. En la recta numérica, cada salto de 100 mueve el número una marca grande. Si llegas a 900 y sumas 100, llegas a 1.000, que se escribe con un punto: 1.000.",
        "Una forma de comprobar es usar billetes: cinco billetes de $100 forman $500. Contar de 100 en 100 es lo mismo que contar billetes. Si tienes 350 y sumas 3 billetes más, llegas a 650.",
    ],
    vocab=[("centena", "100 unidades"), ("mil", "diez centenas, se escribe 1.000"), ("salto grande", "salto de 100 en la recta"), ("avanzar", "sumar al contar"), ("retroceder", "restar al contar")],
    worked=[
        {"title": "Avanzar de 100 en 100", "problem": "Cuenta de 100 en 100 desde 350, cuatro números más.", "steps": ["350 + 100 = 450.", "450 + 100 = 550; 550 + 100 = 650.", "650 + 100 = 750.", "Reviso: sólo cambió la cifra de las centenas."], "answer": "350, 450, 550, 650, 750"},
        {"title": "Detenerse en 1.000", "problem": "Parte en 720 y cuenta hacia adelante de 100 en 100 sin pasar de 1.000.", "steps": ["720 + 100 = 820.", "820 + 100 = 920.", "920 + 100 = 1.020, que pasa de 1.000, así que me detengo en 920.", "Escribo sólo los números que no pasan de 1.000."], "answer": "720, 820, 920"},
    ],
    mistakes=[
        {"wrong": "Contar 350, 360, 370 en vez de 450, 550.", "why": "Se usa el salto de 10 en vez del de 100.", "fix": "Un salto de 100 cambia la cifra de las centenas."},
        {"wrong": "Escribir 1000 sin punto o como 100.", "why": "No se conoce la escritura de mil.", "fix": "Diez centenas forman mil: se escribe 1.000."},
    ],
    tiers={
        "recovery": [fill(350, 100, 6, (1, 3), "Se suma 100: 450 y 650."), fill(0, 100, 6, (2, 4), "0, 100, 200, 300, 400, 500."), fill(900, -100, 5, (1, 3), "Se resta 100: 800 y 600.")],
        "understand": [
            ex("En 450, 550, 650, ¿qué cifra cambia y cuáles no?", "Cambia la centena; decenas y unidades no", "La centena sube 4, 5, 6 y las otras cifras siguen en 5 y 0."),
            ex("¿Qué número viene después de 900 al contar de 100 en 100?", "1.000", "900 + 100 = 1.000."),
            ex("¿Qué número viene antes de 300 al contar de 100 en 100?", "200", "300 − 100 = 200."),
        ],
        "apply": [
            fill(127, 100, 6, (1, 3, 5), "127, 227, 327, 427, 527, 627."),
            arith("Tengo 3 billetes de $100 y consigo 4 billetes más de $100. ¿Cuánto dinero tengo?", "300+400", "Son 7 billetes de $100 y llegan a 700."),
            ex("Parto en 680 y retrocedo tres saltos de 100. ¿En qué número quedo?", "380", "680 − 100 = 580; 580 − 100 = 480; 480 − 100 = 380."),
        ],
        "reason": [
            ex("Julia dice: «Desde 640 el siguiente número es 740, luego 840». ¿Está bien?", "Sí", "640 + 100 = 740 y 740 + 100 = 840."),
            ex("Una secuencia dice 215, 315, 415, 515, 625. ¿Dónde está el error y cuál es el número correcto?", "625 debe ser 615", "515 + 100 = 615; las otras cifras no pueden cambiar."),
        ],
        "challenge": [
            ex("¿Cuántos saltos de 100 hay entre 140 y 940?", "8 saltos", "140, 240, 340, 440, 540, 640, 740, 840, 940: ocho saltos."),
            ex("Parto en 1.000 y retrocedo de 100 en 100. ¿Después de cuántos saltos llego a 400?", "6 saltos", "1.000, 900, 800, 700, 600, 500, 400: seis saltos."),
        ],
    },
    context=[ex("Una biblioteca guarda libros en cajas de 100. Hay 6 cajas llenas y llegan 3 cajas más. ¿Cuántos libros hay en las cajas?", "900 libros", "Nueve cajas de 100 libros hacen 900.")],
    selfcheck=[ex("Completa: 120, 220, __, 420.", "320", "220 + 100 = 320."), ex("Resta 100 a 805.", "705", "805 − 100 = 705."), ex("Escribe con cifras el número «mil».", "1.000", "Diez centenas forman mil.")],
    open_task={
        "statement": "Parte en 245 y cuenta de 100 en 100 hasta tener cinco números. Luego retrocede de 100 en 100 desde 845 hasta 245 y cuenta cuántos saltos diste.",
        "example": "245, 345, 445, 545, 645. De 845 a 245 hay 6 saltos: 845, 745, 645, 545, 445, 345, 245; son seis restas de 100.",
        "criteria": ["escribe cinco números", "mantiene el salto de 100", "retrocede hasta 245", "cuenta los saltos correctamente"],
        "evidence": ["secuencia escrita", "secuencia hacia atrás", "número de saltos con explicación"],
        "errors": ["mezclar saltos de 10 y 100", "contar los números en vez de los saltos"],
        "feedback": "Si contó siete saltos, invita a dibujarlos en la recta y notar que hay un número más que saltos; reconoce la secuencia correcta.",
    },
    reinforce="Haz una tira con la secuencia 0, 100, 200 ... 1.000 y pinta cada centena de un color.",
    extend="Descubre qué pasa con las decenas y las unidades si cuentas de 100 en 100 desde 358 y explica por qué no cambian.",
)
