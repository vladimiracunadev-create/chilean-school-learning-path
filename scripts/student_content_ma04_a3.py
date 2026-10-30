"""Cuaderno del estudiante de 4.º básico Matemática: OA 05 (multiplicación de tres dígitos por uno) y OA 06 (división de dos dígitos por uno)."""
from __future__ import annotations

from student_content_ma04_a import M, W, blk, lesson, task
from student_lessons import arith, ex

OA5 = "MA04 OA 05"
OA6 = "MA04 OA 06"

# ------------------------------------------------------------------ OA 05
lesson(
    OA5, 1,
    use="Aprenderé a multiplicar un número de tres cifras por uno de una cifra usando bloques y dibujos. Sirve para entender qué pasa con cada lugar antes de usar la cuenta en columnas.",
    prior=["Sé las tablas de multiplicar hasta 10 × 10.", "Sé canjear 10 unidades por 1 decena, 10 decenas por 1 centena y 10 centenas por 1 unidad de mil."],
    explain=[
        "Usaremos ◼ (1.000), ▣ (100), ▮ (10) y ● (1). Multiplicar 3 × 214 es juntar 3 grupos de 214. El número 214 es 2 ▣, 1 ▮ y 4 ●. En tres grupos hay 6 ▣, 3 ▮ y 12 ●. Se multiplica cada tipo de pieza por 3.",
        "Después se canjea. Diez ● se cambian por 1 ▮. Entonces 12 ● son 1 ▮ y 2 ●. Las ▮ pasan a ser 3 + 1 = 4. Quedan 6 ▣, 4 ▮ y 2 ●, que es 642. Si al canjear las ▮ se completan 10, se cambian por 1 ▣, y así con las ▣ por 1 ◼.",
        "Al terminar, revisa que cada lugar tenga menos de 10 piezas y que no se te haya olvidado ningún lugar. Un dibujo ordenado, con los lugares separados por barras, evita que se mezclen las piezas.",
    ],
    vocab=[("factor", "cada número que se multiplica"), ("producto", "resultado de una multiplicación"), ("canje", "cambiar 10 piezas de un lugar por 1 del lugar siguiente"), ("grupo", "cantidad que se repite al multiplicar"), ("material concreto", "objetos o bloques que se pueden tocar y mover")],
    worked=[
        W("Multiplicar con canje", "Calcula 3 × 214 con bloques.", ["214 es 2 ▣, 1 ▮ y 4 ●. En 3 grupos: 6 ▣, 3 ▮ y 12 ●.", "Canjeo 10 ● por 1 ▮: quedan 2 ● y las ▮ son 4.", "Ahora hay 6 ▣, 4 ▮ y 2 ●."], "642"),
        W("Multiplicar con un cero", "Calcula 2 × 135 con bloques.", ["135 es 1 ▣, 3 ▮ y 5 ●. En 2 grupos: 2 ▣, 6 ▮ y 10 ●.", "Canjeo 10 ● por 1 ▮: quedan 0 ● y las ▮ son 7.", "Quedan 2 ▣, 7 ▮ y 0 ●."], "270"),
    ],
    mistakes=[
        M("Escribir 3 × 214 = 6.312 (6 ▣, 3 ▮, 12 ●).", "No se canjearon las 12 unidades.", "10 ● se cambian por 1 ▮: quedan 2 ● y 4 ▮. El producto es 642."),
        M("Multiplicar solo las ▣ y dejar las otras piezas sin multiplicar.", "Se olvida que todos los lugares se repiten en cada grupo.", "En cada grupo hay ▣, ▮ y ●. Multiplica los tres."),
    ],
    rec=[
        arith("Cada bolsa tiene 1 ▣, 2 ▮ y 3 ● (123). ¿Cuánto hay en 3 bolsas?", "3*123", "3 ▣, 6 ▮ y 9 ●: no hay canje."),
        ex("¿Cuántas ● hay en 5 grupos de 3 ●?", "15 ●", "5 × 3 = 15."),
        ex("¿Cuántas ▣ hay en 2 grupos de 3 ▣? Escribe su valor.", "6 ▣; 600", "2 × 3 = 6 centenas, o sea 600."),
    ],
    und=[
        ex("Al calcular 4 × 3 ▮ obtienes 12 ▮. ¿Qué canje haces?", "10 ▮ por 1 ▣; quedan 1 ▣ y 2 ▮", "10 decenas forman 1 centena."),
        ex("En 3 × 214 salen 12 ●. ¿Cuántas ● y cuántas ▮ de más quedan después del canje?", "2 ● y 1 ▮ más", "12 ● = 1 ▮ y 2 ●."),
        ex("En 2 × 135 hay 10 ●. ¿Cuántas ● quedan tras el canje?", "0", "10 ● son 1 ▮ y 0 ●."),
    ],
    app=[
        arith("Calcula 3 × 214 con tus bloques.", "3*214", "6 ▣, 3 ▮ y 12 ●; después del canje, 6 ▣, 4 ▮ y 2 ●."),
        arith("Una caja trae 135 clips. ¿Cuántos clips hay en 2 cajas?", "2*135", "2 ▣, 6 ▮ y 10 ●."),
        arith("Calcula 4 × 306 con bloques (hay que canjear centenas por unidad de mil).", "4*306", "12 ▣ forman 1 ◼ y 2 ▣; 24 ● forman 2 ▮ y 4 ●."),
    ],
    rea=[
        ex("Eva multiplicó 3 × 214 y escribió 6.312 (6 centenas, 3 decenas y 12 unidades juntas). ¿Qué hizo mal?", "No canjeó las 12 unidades; es 642", "12 ● son 1 ▮ y 2 ●, así que quedan 6 ▣, 4 ▮ y 2 ●."),
        ex("Pablo dice que 4 × 250 = 1.000 porque 8 ▣ y 20 ▮ forman 1 ◼. ¿Tiene razón?", "Sí", "20 ▮ son 2 ▣; 8 ▣ + 2 ▣ = 10 ▣ = 1 ◼."),
    ],
    cha=[
        arith("Calcula 5 × 207 con bloques y canjes.", "5*207", "10 ▣ forman 1 ◼; 35 ● forman 3 ▮ y 5 ●."),
        ex("Un número de tres cifras multiplicado por 2 da 800. ¿Cuál es el número?", "400", "2 × 400 = 800, o 4 ▣ dobladas son 8 ▣."),
    ],
    ctx=[ex("Una caja tiene 125 clips. ¿Cuántos clips hay en 4 cajas?", "500", "4 ▣, 8 ▮ y 20 ●: 20 ● son 2 ▮, y 10 ▮ son 1 ▣; queda 5 ▣.")],
    sc=[
        arith("Calcula 2 × 113.", "2*113", "2 ▣, 2 ▮ y 6 ●."),
        arith("Calcula 3 × 200.", "3*200", "3 × 2 ▣ = 6 ▣."),
        ex("¿Por cuál pieza se cambian 10 ▮?", "Por 1 ▣", "Diez decenas son una centena."),
    ],
    op=task(
        "Calcula 3 × 248 con dibujos de ▣, ▮ y ●. Dibuja los tres grupos, junta las piezas, haz los canjes y escribe el producto. Luego explica en una frase qué canjes hiciste.",
        "248 es 2 ▣, 4 ▮ y 8 ●. En 3 grupos: 6 ▣, 12 ▮ y 24 ●. 24 ● son 2 ▮ y 4 ●: quedan 14 ▮. 14 ▮ son 1 ▣ y 4 ▮: quedan 7 ▣. Producto: 7 ▣, 4 ▮ y 4 ● = 744. Canjeé unidades a decenas y decenas a centenas.",
        ["dibuja los tres grupos", "multiplica cada lugar", "hace los canjes necesarios", "escribe el producto 744"],
        ["dibujo en el cuaderno", "producto escrito", "frase de explicación"],
        ["olvidar un canje", "multiplicar solo un lugar"],
        "Reconoce el dibujo correcto y pide que cuente las piezas finales para comprobar que ningún lugar tiene 10 o más.",
    ),
    reinforce="Con palitos y atados de 10, representa 3 × 14 y canjea 10 palitos sueltos por un atado.",
    extend="Calcula 5 × 126 con bloques y escribe cuántos canjes de cada tipo necesitaste.",
)

lesson(
    OA5, 2,
    use="Aprenderé a multiplicar separando el número de tres cifras en centenas, decenas y unidades (propiedad distributiva). Sirve para calcular de a partes y sumar al final.",
    prior=["Sé multiplicar con bloques y canjes.", "Sé multiplicar un número de una cifra por 10 y por 100."],
    explain=[
        "La propiedad distributiva dice que multiplicar una suma es lo mismo que multiplicar cada sumando y luego sumar. Para 4 × 235, separa 235 = 200 + 30 + 5. Entonces 4 × 235 = 4 × 200 + 4 × 30 + 4 × 5.",
        "Calcula cada producto parcial: 4 × 200 = 800, 4 × 30 = 120 y 4 × 5 = 20. Se llaman parciales porque son partes del producto total. Ahora suma: 800 + 120 + 20 = 940. Es el mismo resultado que con bloques.",
        "Esta estrategia se puede escribir de forma ordenada. Si un número tiene un cero, ese lugar no aporta: 7 × 306 = 7 × 300 + 7 × 6 = 2.100 + 42 = 2.142. Siempre comprueba que hayas multiplicado todos los sumandos.",
    ],
    vocab=[("propiedad distributiva", "multiplicar una suma es lo mismo que multiplicar cada sumando y sumar los resultados"), ("producto parcial", "producto de una parte del número; al sumarlos se obtiene el total"), ("descomponer", "separar un número en centenas, decenas y unidades"), ("sumando", "cada parte que se suma"), ("producto", "resultado de multiplicar")],
    worked=[
        W("Descomponer y multiplicar", "Calcula 4 × 235 con la propiedad distributiva.", ["Separo: 235 = 200 + 30 + 5.", "Multiplico cada parte: 4 × 200 = 800, 4 × 30 = 120, 4 × 5 = 20.", "Sumo los productos parciales: 800 + 120 + 20."], "940"),
        W("Otro número", "Calcula 6 × 148 con la propiedad distributiva.", ["Separo: 148 = 100 + 40 + 8.", "6 × 100 = 600, 6 × 40 = 240, 6 × 8 = 48.", "Sumo: 600 + 240 + 48."], "888"),
    ],
    mistakes=[
        M("Calcular 4 × 235 como 800 + 120 + 5 = 925.", "Se olvida multiplicar el último sumando por 4.", "Cada sumando se multiplica: 4 × 5 = 20, entonces 800 + 120 + 20 = 940."),
        M("Calcular 4 × 30 = 12.", "Se pierde el cero al multiplicar la decena.", "30 son 3 decenas: 4 × 3 decenas = 12 decenas = 120."),
    ],
    rec=[
        ex("Descompón 235 en centenas, decenas y unidades.", "200 + 30 + 5", "2 centenas, 3 decenas y 5 unidades."),
        arith("Calcula 4 × 200.", "4*200", "4 × 2 centenas = 8 centenas."),
        arith("Calcula 4 × 30.", "4*30", "4 × 3 decenas = 12 decenas."),
    ],
    und=[
        ex("Para 6 × 148, ¿cuáles son los tres productos parciales?", "600, 240 y 48", "6 × 100, 6 × 40 y 6 × 8."),
        arith("Calcula 5 × (20 + 3) multiplicando cada parte.", "5*20+5*3", "5 × 20 = 100 y 5 × 3 = 15."),
        ex("En 7 × 306, ¿por qué no hay un producto parcial de decenas?", "Porque hay 0 decenas", "306 = 300 + 6."),
    ],
    app=[
        arith("Calcula 5 × 123 con la propiedad distributiva.", "5*123", "5 × 100 + 5 × 20 + 5 × 3."),
        arith("Una caja tiene 315 hojas. ¿Cuántas hojas hay en 3 cajas?", "3*315", "3 × 300 + 3 × 10 + 3 × 5."),
        arith("Calcula 8 × 107.", "8*107", "8 × 100 = 800 y 8 × 7 = 56."),
    ],
    rea=[
        ex("Lía calculó 4 × 235 como 800 + 120 + 5 = 925. ¿Qué error cometió y cuál es el resultado?", "No multiplicó 5 por 4; es 940", "4 × 5 = 20 y 800 + 120 + 20 = 940."),
        ex("Beto dice que 3 × 41 se puede calcular como 3 × 40 + 3 × 1. ¿Tiene razón? ¿Cuánto da?", "Sí, 123", "3 × 40 = 120 y 3 × 1 = 3."),
    ],
    cha=[
        arith("Calcula 7 × 306 separando en 300 y 6.", "7*300+7*6", "7 × 300 = 2.100 y 7 × 6 = 42."),
        ex("Si 6 × 150 = 900, ¿cuánto es 6 × 152?", "912", "152 = 150 + 2, y 6 × 2 = 12; 900 + 12 = 912."),
    ],
    ctx=[ex("Una bodega guarda 5 cajas con 148 tornillos cada una. ¿Cuántos tornillos hay?", "740", "500 + 200 + 40 = 740.")],
    sc=[
        arith("Calcula 3 × 212 separando en partes.", "3*212", "3 × 200 + 3 × 10 + 3 × 2."),
        arith("Calcula 2 × 450.", "2*450", "2 × 400 = 800 y 2 × 50 = 100."),
        ex("¿Cómo se llama cada producto de una parte del número?", "Producto parcial", "Los productos parciales se suman para obtener el total."),
    ],
    op=task(
        "Calcula 5 × 236 y 7 × 405 con la propiedad distributiva. Escribe la descomposición, los productos parciales y la suma final de cada uno.",
        "5 × 236: 236 = 200 + 30 + 6; 5 × 200 = 1.000, 5 × 30 = 150, 5 × 6 = 30; 1.000 + 150 + 30 = 1.180. 7 × 405: 405 = 400 + 5; 7 × 400 = 2.800 y 7 × 5 = 35; 2.800 + 35 = 2.835.",
        ["descompone bien", "calcula los productos parciales", "suma al final"],
        ["dos cálculos escritos con sus partes"],
        ["olvidar un producto parcial", "perder un cero"],
        "Si el total no coincide, pide que revise primero que haya multiplicado todos los sumandos.",
    ),
    reinforce="Calcula 3 × 24 separando 24 en 20 + 4 y sumando los productos parciales.",
    extend="Calcula 9 × 198 de dos formas: separando en 100 + 90 + 8, y como 9 × 200 menos 9 × 2.",
)

lesson(
    OA5, 3,
    use="Aprenderé a estimar un producto antes de calcularlo. Sirve para saber si mi resultado es razonable y detectar errores.",
    prior=["Sé redondear números a la centena.", "Sé multiplicar por 10, 100 y por una cifra."],
    explain=[
        "Para estimar un producto, redondea el número de tres cifras a la centena más cercana y luego multiplica por el factor de una cifra. Por ejemplo, 312 × 6: 312 queda en 300 y 300 × 6 = 1.800. El producto exacto es 1.872, cercano a 1.800.",
        "Mira siempre la cifra de las decenas. 489 queda en 500 porque las decenas son 8. Entonces 489 × 4 ≈ 500 × 4 = 2.000. El exacto es 1.956. La estimación no tiene que ser igual al exacto, solo cercana.",
        "Usa la estimación antes de calcular para saber el tamaño del resultado y después para revisar. Si calculas 489 × 4 y te da 3.956, mira la estimación 2.000: está muy lejos, hay un error. La estimación te avisa.",
    ],
    vocab=[("estimar", "calcular un resultado cercano sin hacer la cuenta exacta"), ("redondear", "cambiar un número por el más cercano terminado en 0 o 00"), ("aproximadamente (≈)", "casi igual"), ("razonable", "cercano a lo que se espera"), ("producto", "resultado de multiplicar")],
    worked=[
        W("Estimar y comparar", "Estima 312 × 6 y compárala con el producto exacto, que es 1.872.", ["Redondeo 312 a la centena: 300.", "Multiplico: 300 × 6 = 1.800.", "Comparo: 1.872 está cerca de 1.800."], "≈ 1.800"),
        W("Redondear hacia arriba", "Estima 489 × 4.", ["Las decenas de 489 son 8: sube a 500.", "500 × 4 = 2.000."], "≈ 2.000"),
    ],
    mistakes=[
        M("Estimar 489 × 4 como 400 × 4 = 1.600.", "No se redondea a la centena más cercana: 489 está más cerca de 500.", "Mira las decenas: 8 es 5 o más, entonces 489 ≈ 500."),
        M("Creer que la estimación debe dar igual al producto exacto.", "Se confunde estimar con calcular.", "La estimación es solo cercana; sirve para revisar."),
    ],
    rec=[
        ex("Redondea 312 a la centena más cercana.", "300", "Las decenas son 1, menos de 5."),
        ex("Redondea 489 a la centena más cercana.", "500", "Las decenas son 8, sube."),
        ex("Redondea 650 a la centena más cercana.", "700", "Las decenas son 5, sube."),
    ],
    und=[
        arith("Estima 312 × 6 redondeando a la centena.", "300*6", "312 ≈ 300 y 300 × 6 = 1.800."),
        ex("Si estimas un producto como 2.000 y tu cálculo da 3.956, ¿es razonable?", "No", "3.956 está muy lejos de 2.000."),
        ex("¿Qué se estima primero: el factor de tres cifras o el de una cifra?", "El de tres cifras", "Solo el de tres cifras se redondea a la centena; el de una cifra queda igual."),
    ],
    app=[
        arith("Estima 689 × 3 redondeando a la centena.", "700*3", "689 ≈ 700 y 700 × 3 = 2.100."),
        arith("Estima 398 × 5 redondeando a la centena.", "400*5", "398 ≈ 400 y 400 × 5 = 2.000."),
        arith("Estima 252 × 4 redondeando a la centena.", "300*4", "252 ≈ 300 porque las decenas son 5. 300 × 4 = 1.200."),
    ],
    rea=[
        ex("Ana calculó 312 × 6 = 1.872 y su estimación fue 1.800. ¿Es razonable el resultado?", "Sí", "1.872 está cerca de 1.800."),
        ex("Un compañero calculó 489 × 4 = 3.956. Usa la estimación 500 × 4 para decir si es razonable.", "No", "La estimación es 2.000, muy lejos de 3.956. El exacto es 1.956."),
    ],
    cha=[
        ex("¿Puede ser 1.480 el producto de 196 × 5? Usa una estimación.", "No", "196 ≈ 200 y 200 × 5 = 1.000, lejos de 1.480. El exacto es 980."),
        arith("Estima 408 × 7 redondeando a la centena.", "400*7", "408 ≈ 400 y 400 × 7 = 2.800."),
    ],
    ctx=[ex("Un camión lleva 7 cajas con 198 botellas cada una. Estima cuántas botellas lleva.", "≈ 1.400", "198 ≈ 200 y 200 × 7 = 1.400. El exacto es 1.386.")],
    sc=[
        arith("Estima 297 × 3.", "300*3", "297 ≈ 300 y 300 × 3 = 900."),
        arith("Estima 506 × 2.", "500*2", "506 ≈ 500 y 500 × 2 = 1.000."),
        ex("Redondea 749 a la centena.", "700", "Las decenas son 4, no sube."),
    ],
    op=task(
        "Estima y luego calcula el producto exacto de 4 × 387, de 6 × 214 y de 3 × 505. Escribe cuánto se diferencian la estimación y el resultado exacto en cada una.",
        "4 × 387: 400 × 4 = 1.600; exacto 1.548; diferencia 52. 6 × 214: 200 × 6 = 1.200; exacto 1.284; diferencia 84. 3 × 505: 500 × 3 = 1.500; exacto 1.515; diferencia 15.",
        ["redondea bien", "estima las tres", "calcula el exacto", "compara"],
        ["tres estimaciones y tres cálculos exactos", "diferencias anotadas"],
        ["redondear mal las decenas", "confundir estimación con resultado exacto"],
        "Si una estimación queda lejos, pide revisar el redondeo antes de revisar el cálculo exacto.",
    ),
    reinforce="Estima 5 × 198 y 3 × 304 y compara con el cálculo exacto.",
    extend="Estima 6 × 349 y 6 × 351 con centenas. ¿Por qué los resultados son distintos aunque los números son tan cercanos?",
)

lesson(
    OA5, 4,
    use="Aprenderé el algoritmo de la multiplicación y cómo se relaciona con los productos parciales. Sirve para multiplicar rápido y entender lo que se hace en cada paso.",
    prior=["Sé multiplicar con la propiedad distributiva.", "Sé reagrupar al sumar."],
    explain=[
        "El algoritmo de la multiplicación ordena el cálculo en columnas. Escribe el número de tres cifras arriba y el de una cifra abajo. Multiplica de derecha a izquierda: primero las unidades, luego las decenas y por último las centenas. Si un producto pasa de 9, escribes la cifra de las unidades y llevas la otra.",
        "Veamos 234 × 3. Unidades: 4 × 3 = 12, escribo 2 y llevo 1. Decenas: 3 × 3 = 9 y sumo el 1 que llevo: 10, escribo 0 y llevo 1. Centenas: 2 × 3 = 6 y sumo 1: 7. El producto es 702.",
        "Es lo mismo que los productos parciales: 4 × 3 = 12, 30 × 3 = 90 y 200 × 3 = 600, y 12 + 90 + 600 = 702. En el algoritmo los parciales están escondidos en lo que escribes y lo que llevas. Comprueba con una estimación: 234 × 3 ≈ 200 × 3 = 600.",
    ],
    vocab=[("algoritmo", "pasos ordenados para hacer una cuenta"), ("llevar", "pasar a la columna siguiente lo que sobra de un producto"), ("producto parcial", "producto de una parte del número"), ("columna", "números alineados de arriba hacia abajo"), ("comprobar", "revisar con una estimación o con otro método")],
    worked=[
        W("Con llevadas", "Calcula 234 × 3 con el algoritmo.", ["Unidades: 4 × 3 = 12. Escribo 2 y llevo 1.", "Decenas: 3 × 3 = 9, más 1 que llevo = 10. Escribo 0 y llevo 1.", "Centenas: 2 × 3 = 6, más 1 = 7.", "Compruebo con parciales: 12 + 90 + 600 = 702."], "702"),
        W("Con una llevada", "Calcula 152 × 4 con el algoritmo.", ["Unidades: 2 × 4 = 8. Escribo 8.", "Decenas: 5 × 4 = 20. Escribo 0 y llevo 2.", "Centenas: 1 × 4 = 4, más 2 = 6."], "608"),
    ],
    mistakes=[
        M("Escribir 234 × 3 = 692.", "No se sumó la llevada 1 de las unidades a las decenas.", "Decenas: 3 × 3 = 9 y sumo 1: 10. El resultado es 702."),
        M("Sumar la llevada antes de multiplicar: (3 + 1) × 3.", "Se mezcla el orden de las operaciones.", "Primero multiplica la cifra y después suma lo que llevas."),
    ],
    rec=[
        arith("Calcula 111 × 3.", "111*3", "Cada lugar da 3, sin llevadas."),
        arith("Calcula 212 × 4.", "212*4", "Unidades 8, decenas 4, centenas 8."),
        arith("Calcula 320 × 3.", "320*3", "0 × 3 = 0, 2 × 3 = 6 y 3 × 3 = 9."),
    ],
    und=[
        ex("En 234 × 3, el producto de las unidades es 4 × 3 = 12. ¿Qué se escribe y qué se lleva?", "Se escribe 2 y se lleva 1", "12 unidades son 1 decena y 2 unidades."),
        ex("En 234 × 3, ¿cuánto es 3 × 3 más la llevada?", "10", "3 × 3 = 9 y 9 + 1 = 10."),
        ex("En 234 × 3, ¿qué producto parcial corresponde a las centenas?", "600", "200 × 3 = 600."),
    ],
    app=[
        arith("Calcula 456 × 2.", "456*2", "6 × 2 = 12, 5 × 2 + 1 = 11, 4 × 2 + 1 = 9."),
        arith("Un álbum tiene 275 fotos. ¿Cuántas fotos hay en 3 álbumes?", "275*3", "5 × 3 = 15, 7 × 3 + 1 = 22, 2 × 3 + 2 = 8."),
        arith("Una escuela compra 6 cajas de 308 lápices. ¿Cuántos lápices compra?", "308*6", "8 × 6 = 48, 0 × 6 + 4 = 4, 3 × 6 = 18."),
    ],
    rea=[
        ex("Marcos escribió 234 × 3 = 692. ¿Qué olvidó y cuál es el resultado correcto?", "No llevó el 1; es 702", "Decenas: 9 + 1 = 10; las centenas quedan 7."),
        ex("Camila dice que los productos parciales de 152 × 4 son 8, 200 y 400 y que suman 608. ¿Tiene razón?", "Sí", "2 × 4 = 8, 50 × 4 = 200, 100 × 4 = 400 y 8 + 200 + 400 = 608."),
    ],
    cha=[
        ex("Falta una cifra: 2_3 × 3 = 699. ¿Qué cifra falta?", "3", "699 ÷ 3 = 233."),
        ex("Falta una cifra: 14_ × 3 = 426. ¿Qué cifra falta?", "2", "Las unidades de 14_ × 3 deben terminar en 6: 2 × 3 = 6. Comprueba: 142 × 3 = 426."),
    ],
    ctx=[ex("Un rollo de cinta mide 275 cm. ¿Cuántos centímetros miden 3 rollos?", "825 cm", "5 × 3 = 15, 7 × 3 + 1 = 22, 2 × 3 + 2 = 8: 825.")],
    sc=[
        arith("Calcula 123 × 3.", "123*3", "Cada lugar se multiplica por 3 sin llevar."),
        arith("Calcula 148 × 2.", "148*2", "8 × 2 = 16, 4 × 2 + 1 = 9 y 1 × 2 = 2."),
        ex("¿Qué se hace cuando un producto de una columna pasa de 9?", "Se escribe la cifra de las unidades y se lleva la otra", "Así cada lugar queda con una sola cifra."),
    ],
    op=task(
        "Calcula 367 × 4 con el algoritmo y también con productos parciales. Estima antes y compara los tres resultados.",
        "Estimación: 400 × 4 = 1.600. Algoritmo: 7 × 4 = 28 (escribo 8, llevo 2); 6 × 4 + 2 = 26 (escribo 6, llevo 2); 3 × 4 + 2 = 14: 1.468. Parciales: 300 × 4 = 1.200, 60 × 4 = 240, 7 × 4 = 28; 1.200 + 240 + 28 = 1.468.",
        ["usa el algoritmo", "calcula los parciales", "estima antes", "compara los resultados"],
        ["cuenta en columnas", "parciales escritos", "estimación escrita"],
        ["no sumar la llevada", "olvidar un parcial"],
        "Si los dos métodos no coinciden, pide revisar la columna donde aparece la primera diferencia.",
    ),
    reinforce="Calcula 213 × 3 y 124 × 2 y revisa con la estimación.",
    extend="Explica con dibujos por qué 12 unidades se escriben como 2 y se lleva 1 decena.",
)

lesson(
    OA5, 5,
    use="Aprenderé a resolver problemas con multiplicaciones de tres cifras por una cifra y a comprobar mis respuestas. Sirve para calcular totales cuando hay grupos iguales.",
    prior=["Sé multiplicar con algoritmo y con parciales.", "Sé estimar productos."],
    explain=[
        "Un problema de grupos iguales tiene dos datos: cuántos grupos hay y cuántos elementos tiene cada grupo. Se multiplica para saber el total. Por ejemplo, 8 cajas con 125 lápices cada una: 8 × 125 = 1.000 lápices.",
        "Para resolver, sigue pasos: leer, decir qué se busca, escribir la multiplicación, estimar, calcular y comprobar. Comprueba con la estimación o repitiendo la cuenta con otro método, como los productos parciales. Anota la respuesta con unidad.",
        "A veces el problema pide dos pasos. Primero multiplicas y después sumas o restas. Escribe cada paso para no mezclar los datos. Si el resultado no se parece a tu estimación, revisa si multiplicaste todos los lugares y si no olvidaste una llevada.",
    ],
    vocab=[("grupos iguales", "grupos con la misma cantidad de elementos"), ("total", "resultado de juntar todos los grupos"), ("dato", "número o información que da el problema"), ("estimación", "resultado cercano, no exacto"), ("comprobar", "revisar la respuesta con otro método")],
    worked=[
        W("Grupos iguales", "Una librería compra 8 cajas con 125 lápices cada una. ¿Cuántos lápices compra?", ["Hay 8 grupos de 125 lápices: 8 × 125.", "Estimo: 8 × 100 = 800; como 125 es más que 100, el total será algo más que 800.", "8 × 100 = 800, 8 × 20 = 160 y 8 × 5 = 40; 800 + 160 + 40 = 1.000."], "1.000 lápices"),
        W("Dos pasos", "Un bus recorre 346 km por día durante 3 días y después 120 km más. ¿Cuántos km recorre?", ["Primero 3 días: 3 × 346 = 1.038.", "Luego sumo los 120 km más: 1.038 + 120.", "Total: 1.158. Estimación: 350 × 3 = 1.050 y 1.050 + 120 = 1.170, cercano."], "1.158 km"),
    ],
    mistakes=[
        M("Sumar 8 + 125 en el problema de las cajas.", "Se elige la suma por tener dos números, sin ver que son grupos iguales.", "Cuando hay grupos iguales, se multiplica."),
        M("Dar la respuesta sin unidad: «1.000».", "No queda claro qué se contó.", "Escribe «1.000 lápices»."),
    ],
    rec=[
        arith("Cada caja trae 125 clips. ¿Cuántos clips hay en 2 cajas?", "2*125", "2 grupos de 125."),
        arith("Un álbum tiene 215 láminas. ¿Cuántas láminas hay en 4 álbumes?", "4*215", "4 grupos de 215."),
        arith("Un tren tiene 3 carros con 146 asientos cada uno. ¿Cuántos asientos hay?", "3*146", "3 grupos de 146."),
    ],
    und=[
        ex("En «6 estantes con 215 libros cada uno», ¿qué operación sirve para el total?", "Multiplicación 6 × 215", "Hay 6 grupos iguales."),
        ex("¿Qué datos necesitas para saber cuántos zapatos hay en 7 cajas?", "Cuántos zapatos hay en cada caja", "Además de las 7 cajas, falta el tamaño de cada grupo."),
        ex("Antes de calcular 8 × 125, estimas 8 × 100 = 800. ¿Qué indica?", "Que el resultado será un poco más que 800", "125 es más que 100, así que el producto es mayor que 800."),
    ],
    app=[
        arith("Una tienda vende 248 poleras al día durante 3 días. ¿Cuántas poleras vende?", "3*248", "3 grupos de 248."),
        arith("Un depósito tiene 6 bolsas con 134 tornillos cada una. ¿Cuántos tornillos hay?", "6*134", "6 × 100 + 6 × 30 + 6 × 4."),
        arith("Una escuela compra 5 cajas con 206 hojas cada una. ¿Cuántas hojas compra?", "5*206", "5 × 200 = 1.000 y 5 × 6 = 30."),
    ],
    rea=[
        ex("Marta dice que 7 cajas con 198 botellas cada una dan 1.386 botellas. Revisa con la estimación 200 × 7.", "Sí es razonable", "200 × 7 = 1.400, y 1.386 está cerca."),
        ex("Un problema dice «Hay 5 bolsas con 124 caramelos y se regalan 100». ¿Cuántos pasos tiene y qué operaciones usa?", "Dos pasos: multiplicar y restar", "Primero 5 × 124 = 620 y luego 620 − 100 = 520."),
    ],
    cha=[
        ex("Un número de tres cifras multiplicado por 5 da 1.000. ¿Cuál es el número?", "200", "5 × 200 = 1.000."),
        ex("Multiplico un número por 3 y luego sumo 20. Obtengo 710. ¿Cuál era el número?", "230", "710 − 20 = 690 y 690 ÷ 3 = 230, porque 3 × 230 = 690."),
    ],
    ctx=[ex("En un juego, cada nivel da 250 puntos. ¿Cuántos puntos se juntan al pasar 6 niveles?", "1.500 puntos", "6 × 250 = 6 × 200 + 6 × 50 = 1.200 + 300.")],
    sc=[
        arith("Un parque recibe 215 visitantes cada día durante 4 días. ¿Cuántos recibe?", "4*215", "Son 4 grupos iguales."),
        arith("En 3 salas hay 132 sillas en cada una. ¿Cuántas sillas hay?", "3*132", "3 × 132."),
        ex("¿Qué se escribe junto al número en la respuesta final de un problema?", "La unidad", "Por ejemplo, lápices o kilómetros."),
    ],
    op=task(
        "Resuelve este problema y compruébalo: «Una panadería hace 4 tandas de 235 panes en un día y ese mismo día hace además 120 panes especiales. ¿Cuántos panes hace en total ese día?». Haz una estimación, calcula con algoritmo o con parciales y escribe la respuesta con unidad.",
        "4 × 235 = 940 (parciales: 800 + 120 + 20). Estimación: 4 × 200 = 800 y 4 × 250 = 1.000, entonces 940 es razonable. Total con los 120: 940 + 120 = 1.060. Respuesta: ese día la panadería hace 1.060 panes.",
        ["elige las operaciones correctas", "estima", "calcula bien", "respuesta con unidad"],
        ["cálculos escritos", "estimación escrita", "respuesta en oración"],
        ["sumar en vez de multiplicar", "olvidar la unidad"],
        "Pide que explique con sus palabras qué representa cada número del problema antes de calcular.",
    ),
    reinforce="Resuelve «Hay 3 estuches con 124 lápices cada uno. ¿Cuántos lápices hay?» y revisa con la estimación.",
    extend="Inventa un problema con 5 grupos de 3 cifras y resuélvelo con dos métodos distintos.",
)

# ------------------------------------------------------------------ OA 06
lesson(
    OA6, 1,
    use="Aprenderé a repartir y agrupar cantidades de dos cifras entre un número de una cifra usando fichas. Sirve para entender qué es dividir y qué es el resto.",
    prior=["Sé las tablas de multiplicar hasta 10 × 10.", "Sé que multiplicar y dividir se relacionan."],
    explain=[
        "Dividir es repartir en partes iguales o agrupar. Si repartes 48 fichas entre 4 niños, cada uno recibe 12: 48 ÷ 4 = 12. Si agrupas 48 fichas de a 4, formas 12 grupos: también 48 ÷ 4 = 12. El número que se divide es el dividendo, y el que divide es el divisor.",
        "A veces sobra algo. Si repartes 17 fichas entre 4 niños, cada uno recibe 4 y sobra 1. Se escribe 17 ÷ 4 = 4 y resto 1. El resto es lo que sobra y siempre es menor que el divisor, porque si fuera igual o mayor, se podría repartir otra vez.",
        "Usa ▮ para 10 y ● para 1. El 48 es 4 ▮ y 8 ●. Entre 4 niños, cada uno recibe 1 ▮ y 2 ●, que es 12. Comprueba con la multiplicación: 12 × 4 = 48. Si hay resto, comprueba así: cociente × divisor + resto = dividendo.",
    ],
    vocab=[("dividendo", "número que se reparte"), ("divisor", "número entre el que se reparte"), ("cociente", "resultado de la división"), ("resto", "lo que sobra al repartir"), ("agrupar", "formar grupos del mismo tamaño")],
    worked=[
        W("Repartir", "Reparte 48 fichas entre 4 niños en partes iguales.", ["48 es 4 ▮ y 8 ●. Doy 1 ▮ a cada niño: 4 ▮ repartidas.", "Reparto las 8 ●: 2 a cada niño.", "Cada niño tiene 1 ▮ y 2 ●, o sea 12. Compruebo: 12 × 4 = 48."], "12 fichas cada uno"),
        W("Repartir con resto", "Reparte 17 fichas entre 4 niños en partes iguales.", ["Doy 1 ficha a cada niño: 4 usadas. Repito hasta no poder.", "Cada niño recibe 4: 4 × 4 = 16 fichas usadas.", "Sobra 1 ficha, que es menor que 4. Compruebo: 4 × 4 + 1 = 17."], "4 cada uno y resto 1"),
    ],
    mistakes=[
        M("Decir que 17 ÷ 4 = 3 resto 5.", "El resto es mayor que el divisor.", "Si sobran 5, se puede dar 1 más a cada uno. El resto debe ser menor que 4: 17 ÷ 4 = 4 resto 1."),
        M("Decir que 20 fichas agrupadas de a 4 forman 4 grupos.", "Se confunde repartir entre 4 con agrupar de a 4.", "Agrupar de a 4: 20 ÷ 4 = 5 grupos. Repartir entre 4: cada uno recibe 5."),
    ],
    rec=[
        arith("Reparte 24 fichas entre 4 niños. ¿Cuántas recibe cada uno?", "24//4", "4 × 6 = 24."),
        arith("Reparte 30 manzanas entre 5 canastos. ¿Cuántas hay en cada canasto?", "30//5", "5 × 6 = 30."),
        arith("Reparte 16 lápices entre 2 estuches. ¿Cuántos hay en cada estuche?", "16//2", "2 × 8 = 16."),
    ],
    und=[
        ex("Repartes 20 fichas entre 4 niños. ¿Cuántas fichas recibe cada niño?", "5", "20 ÷ 4 = 5 porque 4 × 5 = 20."),
        ex("Agrupas 20 fichas de a 4. ¿Cuántos grupos se forman?", "5", "20 ÷ 4 = 5 porque 4 × 5 = 20."),
        ex("Repartes 17 fichas entre 4 niños. ¿Cuántas sobran?", "1", "Cada uno recibe 4 (16 fichas) y sobra 1."),
    ],
    app=[
        arith("Un profesor reparte 56 cuadernos entre 4 cursos por igual. ¿Cuántos recibe cada curso?", "56//4", "56 es 5 ▮ y 6 ●; se canjea una ▮ y se reparte."),
        arith("Una panadería pone 63 panes en 3 bolsas iguales. ¿Cuántos hay en cada bolsa?", "63//3", "3 × 21 = 63."),
        arith("Se agrupan 72 pelotas en cajas de a 6. ¿Cuántas cajas se forman?", "72//6", "6 × 12 = 72."),
    ],
    rea=[
        ex("Sofía dice que 19 ÷ 6 = 2 resto 7. Revisa con cociente × divisor + resto.", "No, es 3 resto 1", "2 × 6 + 7 = 19 funciona, pero el resto 7 es mayor que 6; se puede repartir una vuelta más: 3 × 6 + 1 = 19."),
        ex("Pía divide 36 fichas entre 4 niños y dice que cada uno recibe 8. Comprueba con la multiplicación.", "No, reciben 9", "8 × 4 = 32 y 9 × 4 = 36."),
    ],
    cha=[
        ex("Reparto 50 fichas entre 6 niños. ¿Cuántas recibe cada uno y cuántas sobran?", "8 cada uno y sobran 2", "6 × 8 = 48 y 50 − 48 = 2."),
        ex("En una división el dividendo es 38, el divisor es 5 y el cociente es 7. ¿Cuál es el resto?", "3", "7 × 5 = 35 y 38 − 35 = 3."),
    ],
    ctx=[ex("Una profesora reparte 45 lápices en 5 estuches con la misma cantidad. ¿Cuántos lápices hay en cada estuche?", "9", "5 × 9 = 45.")],
    sc=[
        arith("Calcula 36 ÷ 3.", "36//3", "3 × 12 = 36."),
        ex("En 17 ÷ 4 = 4 y resto 1, ¿cuál es el resto?", "1", "Lo que sobra es 1."),
        ex("¿El resto de una división puede ser mayor que el divisor?", "No", "Si lo fuera, se podría repartir otra vez."),
    ],
    op=task(
        "Con 38 fichas (dibújalas o usa tapas), reparte entre 3 niños y escribe cuántas recibe cada uno y cuántas sobran. Luego agrúpalas de a 4 y escribe cuántos grupos salen y cuántas sobran. Comprueba ambos resultados con cociente × divisor + resto.",
        "Entre 3 niños: 12 cada uno y sobran 2 (12 × 3 + 2 = 38). De a 4: 9 grupos y sobran 2 (9 × 4 + 2 = 38).",
        ["reparte bien", "agrupa bien", "identifica el resto", "comprueba"],
        ["dibujo o fichas", "resultados y comprobación escritos"],
        ["resto mayor que el divisor", "confundir repartir con agrupar"],
        "Pide que cuente de nuevo las fichas para comprobar que cociente × divisor + resto da 38.",
    ),
    reinforce="Reparte 14 tapas entre 3 vasos y escribe cuántas hay en cada vaso y cuántas sobran.",
    extend="Reparte 90 fichas entre 7 niños. ¿Cuántas recibe cada uno y cuántas sobran?",
)

lesson(
    OA6, 2,
    use="Aprenderé a estimar el cociente antes de dividir. Sirve para saber el tamaño del resultado y revisar si mi división está bien.",
    prior=["Sé las tablas de multiplicar y sus divisiones relacionadas.", "Sé redondear a la decena."],
    explain=[
        "Estimar un cociente es buscar un resultado cercano sin hacer la división completa. Cambias el dividendo por un número cercano que sea fácil de dividir con el divisor. Para 78 ÷ 4, el 78 está cerca de 80, y 80 ÷ 4 = 20. El cociente es aproximadamente 20.",
        "El número que eliges debe estar en la tabla del divisor. Para 59 ÷ 6 usas 60 ÷ 6 = 10. Para 91 ÷ 3 usas 90 ÷ 3 = 30. El cociente exacto puede ser un poco menor o mayor. Por ejemplo, 78 ÷ 4 = 19 y resto 2: cercano a 20.",
        "Estimar sirve antes de dividir, para saber si el resultado tendrá una o dos cifras, y después para revisar. Si divides 78 entre 4 y obtienes 190, tu estimación 20 te avisa que hay un error.",
    ],
    vocab=[("estimar", "buscar un resultado cercano sin calcular exacto"), ("cociente", "resultado de una división"), ("aproximadamente (≈)", "casi igual"), ("dividendo", "número que se reparte"), ("razonable", "cercano a lo esperado")],
    worked=[
        W("Estimar con un número cercano", "Estima 78 ÷ 4.", ["78 está cerca de 80.", "80 ÷ 4 = 20, porque 4 × 20 = 80.", "El cociente de 78 ÷ 4 es aproximadamente 20."], "≈ 20"),
        W("Otro ejemplo", "Estima 59 ÷ 6.", ["59 está cerca de 60.", "60 ÷ 6 = 10.", "El cociente de 59 ÷ 6 es aproximadamente 10."], "≈ 10"),
    ],
    mistakes=[
        M("Estimar 78 ÷ 4 usando 70 ÷ 4.", "Se elige un número que no está en la tabla del 4 y no se divide exacto.", "Elige un número de la tabla del 4 que esté cerca: 80, y 80 ÷ 4 = 20."),
        M("Creer que el cociente exacto debe ser igual a la estimación.", "Se confunde estimar con calcular.", "La estimación solo debe estar cerca: 19 está cerca de 20."),
    ],
    rec=[
        ex("¿Qué número de la tabla del 4 está más cerca de 78?", "80", "4 × 20 = 80, y 80 está a 2 de 78."),
        arith("Calcula 80 ÷ 4.", "80//4", "4 × 20 = 80."),
        arith("Estima 59 ÷ 6 con 60 ÷ 6.", "60//6", "6 × 10 = 60."),
    ],
    und=[
        ex("Para estimar 91 ÷ 3, ¿qué dividendo cercano conviene usar?", "90", "90 está en la tabla del 3."),
        ex("Si estimas que 78 ÷ 4 es 20, ¿tendrá el cociente una o dos cifras?", "Dos cifras", "20 tiene dos cifras."),
        ex("78 ÷ 4 es 19 y resto 2. ¿La estimación 20 es cercana?", "Sí", "19 está a 1 de 20."),
    ],
    app=[
        arith("Estima 62 ÷ 3 usando 60 ÷ 3.", "60//3", "62 ≈ 60."),
        arith("Estima 97 ÷ 5 usando 100 ÷ 5.", "100//5", "97 ≈ 100."),
        arith("Estima 83 ÷ 4 usando 80 ÷ 4.", "80//4", "83 ≈ 80."),
    ],
    rea=[
        ex("Lola dice que 78 ÷ 4 es aproximadamente 200. Usa 80 ÷ 4 para decir si es razonable.", "No", "80 ÷ 4 = 20, muy lejos de 200."),
        ex("Un compañero calculó 97 ÷ 5 = 19 y resto 2. Con la estimación 100 ÷ 5 = 20, ¿es razonable?", "Sí", "19 está muy cerca de 20, y 19 × 5 + 2 = 97."),
    ],
    cha=[
        arith("Estima 95 ÷ 6 usando 96 ÷ 6.", "96//6", "96 está en la tabla del 6 y 95 está muy cerca."),
        ex("El cociente de 74 ÷ 2 está entre dos decenas. ¿Entre cuáles?", "Entre 30 y 40", "70 ÷ 2 = 35 y 80 ÷ 2 = 40; el cociente es 37."),
    ],
    ctx=[ex("Un bus lleva 58 pasajeros en 6 filas iguales. Estima cuántos pasajeros van en cada fila.", "≈ 10", "58 ≈ 60 y 60 ÷ 6 = 10.")],
    sc=[
        arith("Estima 41 ÷ 4 usando 40 ÷ 4.", "40//4", "41 ≈ 40."),
        arith("Estima 89 ÷ 3 usando 90 ÷ 3.", "90//3", "89 ≈ 90."),
        ex("¿Qué número de la tabla del 5 está más cerca de 48?", "50", "5 × 10 = 50."),
    ],
    op=task(
        "Estima el cociente de 71 ÷ 8, de 52 ÷ 5 y de 87 ÷ 9 buscando en cada caso un dividendo cercano de la tabla del divisor. Después calcula el cociente exacto con resto y compara.",
        "71 ÷ 8 ≈ 72 ÷ 8 = 9; exacto 8 resto 7. 52 ÷ 5 ≈ 50 ÷ 5 = 10; exacto 10 resto 2. 87 ÷ 9 ≈ 90 ÷ 9 = 10; exacto 9 resto 6.",
        ["elige un dividendo de la tabla", "estima las tres", "calcula el exacto", "compara"],
        ["tres estimaciones", "tres divisiones exactas"],
        ["elegir un número fuera de la tabla", "confundir cociente y resto"],
        "Si la estimación queda lejos, pide revisar si el dividendo elegido estaba en la tabla del divisor.",
    ),
    reinforce="Estima 47 ÷ 5 y 63 ÷ 7 con números cercanos de las tablas y comprueba con la multiplicación.",
    extend="Estima 90 ÷ 8 con dos números cercanos de la tabla del 8 (88 y 96). ¿Entre qué números está el cociente?",
)

lesson(
    OA6, 3,
    use="Aprenderé a dividir descomponiendo el dividendo en partes fáciles de dividir. Sirve para calcular divisiones sin el algoritmo completo.",
    prior=["Sé dividir con material y sé estimar cocientes.", "Sé descomponer números en decenas y unidades."],
    explain=[
        "Descomponer el dividendo es separarlo en partes que se dividan exacto entre el divisor. Para 84 ÷ 4, separa 84 en 80 + 4. Divide cada parte: 80 ÷ 4 = 20 y 4 ÷ 4 = 1. Suma los resultados: 20 + 1 = 21. Entonces 84 ÷ 4 = 21.",
        "No siempre se separa en decenas y unidades. Para 72 ÷ 3, separa 72 en 60 + 12, porque 12 también se divide exacto por 3: 60 ÷ 3 = 20 y 12 ÷ 3 = 4, así 24. Elige las partes según el divisor y las tablas que conoces.",
        "Si sobra algo, queda como resto. Para 85 ÷ 4, separa 85 en 80 + 5. 80 ÷ 4 = 20 y 5 ÷ 4 = 1 y resto 1. El cociente es 21 y el resto 1. Comprueba: 21 × 4 + 1 = 85.",
    ],
    vocab=[("descomponer el dividendo", "separarlo en partes fáciles de dividir"), ("dividendo", "número que se reparte"), ("cociente", "resultado de la división"), ("resto", "lo que sobra"), ("comprobar", "revisar multiplicando")],
    worked=[
        W("Separar en decenas y unidades", "Calcula 84 ÷ 4 descomponiendo el dividendo.", ["Separo 84 = 80 + 4.", "80 ÷ 4 = 20 y 4 ÷ 4 = 1.", "Sumo: 20 + 1 = 21. Compruebo: 21 × 4 = 84."], "21"),
        W("Otra descomposición", "Calcula 72 ÷ 3 descomponiendo el dividendo.", ["Separo 72 = 60 + 12, porque ambas se dividen exacto por 3.", "60 ÷ 3 = 20 y 12 ÷ 3 = 4.", "Sumo: 20 + 4 = 24. Compruebo: 24 × 3 = 72."], "24"),
    ],
    mistakes=[
        M("Calcular 84 ÷ 4 como 20, olvidando la parte 4 ÷ 4.", "Se divide solo una de las partes.", "Divide cada parte y suma: 20 + 1 = 21."),
        M("Separar 72 en 70 + 2 para dividir por 3.", "Las partes no se dividen exacto por 3.", "Busca partes que estén en la tabla del 3, como 60 + 12."),
    ],
    rec=[
        ex("Separa 84 en 80 y otro número.", "80 + 4", "80 + 4 = 84."),
        arith("Calcula 80 ÷ 4.", "80//4", "4 × 20 = 80."),
        arith("Calcula 4 ÷ 4.", "4//4", "Un número dividido por sí mismo da 1."),
    ],
    und=[
        ex("Para 72 ÷ 3, ¿por qué se separa en 60 + 12 y no en 70 + 2?", "Porque 60 y 12 se dividen exacto por 3", "70 y 2 no están en la tabla del 3."),
        ex("En 85 ÷ 4 = (80 + 5) ÷ 4, ¿cuál es el resto de la parte 5 ÷ 4?", "1", "5 ÷ 4 = 1 y sobra 1."),
        ex("Si 80 ÷ 4 = 20 y 4 ÷ 4 = 1, ¿cuánto es 84 ÷ 4?", "21", "20 + 1 = 21."),
    ],
    app=[
        arith("Calcula 96 ÷ 6 separando en 60 + 36.", "96//6", "60 ÷ 6 = 10 y 36 ÷ 6 = 6."),
        arith("Calcula 91 ÷ 7 separando en 70 + 21.", "91//7", "70 ÷ 7 = 10 y 21 ÷ 7 = 3."),
        arith("Calcula 65 ÷ 5 separando en 50 + 15.", "65//5", "50 ÷ 5 = 10 y 15 ÷ 5 = 3."),
    ],
    rea=[
        ex("Beto descompuso 75 ÷ 5 como 50 + 25, y dice que 10 + 5 = 15. ¿Está bien?", "Sí", "50 ÷ 5 = 10 y 25 ÷ 5 = 5; 15 × 5 = 75."),
        ex("Ana calculó 84 ÷ 4 como 20 + 4 = 24. ¿Qué error cometió?", "Sumó 4 en vez de 4 ÷ 4 = 1; es 21", "La parte 4 se divide: 4 ÷ 4 = 1."),
    ],
    cha=[
        arith("Calcula 87 ÷ 3 separando en 60 + 27.", "87//3", "60 ÷ 3 = 20 y 27 ÷ 3 = 9."),
        ex("Calcula 53 ÷ 4 separando en 40 + 13. Escribe el cociente y el resto.", "13 y resto 1", "40 ÷ 4 = 10 y 13 ÷ 4 = 3 resto 1; 10 + 3 = 13 y 13 × 4 + 1 = 53."),
    ],
    ctx=[ex("Se reparten 84 pegatinas entre 7 amigos en partes iguales. ¿Cuántas recibe cada uno?", "12", "70 ÷ 7 = 10 y 14 ÷ 7 = 2; 10 + 2 = 12.")],
    sc=[
        arith("Calcula 63 ÷ 3 separando en 60 + 3.", "63//3", "60 ÷ 3 = 20 y 3 ÷ 3 = 1."),
        arith("Calcula 48 ÷ 2 separando en 40 + 8.", "48//2", "40 ÷ 2 = 20 y 8 ÷ 2 = 4."),
        ex("Calcula 29 ÷ 4 separando en 20 + 9. Escribe cociente y resto.", "7 y resto 1", "20 ÷ 4 = 5 y 9 ÷ 4 = 2 resto 1; 5 + 2 = 7 y 7 × 4 + 1 = 29."),
    ],
    op=task(
        "Calcula 78 ÷ 6 y 95 ÷ 5 descomponiendo el dividendo. Escribe las partes que elegiste, cada división y la suma final. Comprueba multiplicando.",
        "78 ÷ 6: 60 + 18; 60 ÷ 6 = 10 y 18 ÷ 6 = 3; 13. Compruebo: 13 × 6 = 78. 95 ÷ 5: 50 + 45; 50 ÷ 5 = 10 y 45 ÷ 5 = 9; 19. Compruebo: 19 × 5 = 95.",
        ["elige partes que se dividen exacto", "divide cada parte", "suma bien", "comprueba"],
        ["dos cálculos escritos con sus partes"],
        ["olvidar dividir una parte", "elegir partes fuera de la tabla"],
        "Pide que explique por qué eligió esas partes y que revise con la multiplicación si el resultado no calza.",
    ),
    reinforce="Calcula 42 ÷ 3 separando 42 en 30 + 12 y comprueba multiplicando.",
    extend="Calcula 98 ÷ 7 separando en 70 + 28. ¿Qué otra descomposición sirve?",
)

lesson(
    OA6, 4,
    use="Aprenderé el algoritmo de la división y cómo se relaciona con la multiplicación. Sirve para dividir de forma ordenada y comprobar el resultado.",
    prior=["Sé dividir descomponiendo el dividendo.", "Sé multiplicar y sumar para comprobar."],
    explain=[
        "El algoritmo de la división ordena los pasos. En 84 ÷ 4, divides primero las decenas: 8 decenas ÷ 4 = 2 decenas, sin sobrar. Después divides las unidades: 4 ÷ 4 = 1. El cociente es 21. Cada paso usa una tabla de multiplicar.",
        "Si sobran decenas, se convierten en unidades. En 75 ÷ 5, 7 decenas ÷ 5 = 1 decena y sobran 2 decenas. Esas 2 decenas son 20 unidades; con las 5 unidades hay 25. Entonces 25 ÷ 5 = 5. El cociente es 15.",
        "Para comprobar una división, usa la multiplicación: cociente × divisor + resto = dividendo. En 85 ÷ 4 = 21 y resto 1, comprueba 21 × 4 + 1 = 85. Recuerda que el resto siempre es menor que el divisor.",
    ],
    vocab=[("algoritmo", "pasos ordenados para hacer una cuenta"), ("resto", "lo que sobra al dividir"), ("cociente", "resultado de la división"), ("dividendo", "número que se divide"), ("divisor", "número entre el que se divide")],
    worked=[
        W("Dividir sin resto", "Calcula 84 ÷ 4 con el algoritmo.", ["Decenas: 8 decenas ÷ 4 = 2 decenas, resto 0.", "Unidades: 4 ÷ 4 = 1.", "Cociente: 21. Compruebo: 21 × 4 = 84."], "21"),
        W("Dividir con decenas que sobran", "Calcula 75 ÷ 5 con el algoritmo.", ["Decenas: 7 decenas ÷ 5 = 1 decena, sobran 2 decenas.", "2 decenas son 20 unidades; con las 5 unidades hay 25. 25 ÷ 5 = 5.", "Cociente: 15. Compruebo: 15 × 5 = 75."], "15"),
    ],
    mistakes=[
        M("Escribir 61 ÷ 5 = 11 y resto 6.", "El resto es mayor que el divisor.", "5 cabe una vez más: 61 ÷ 5 = 12 y resto 1. Compruebo: 12 × 5 + 1 = 61."),
        M("Olvidar bajar las unidades al dividir.", "Se divide solo la cifra de las decenas.", "Después de las decenas, baja las unidades y sigue dividiendo."),
    ],
    rec=[
        arith("Calcula 84 ÷ 4.", "84//4", "8 decenas ÷ 4 = 2 y 4 ÷ 4 = 1."),
        arith("Calcula 69 ÷ 3.", "69//3", "6 decenas ÷ 3 = 2 y 9 ÷ 3 = 3."),
        arith("Calcula 48 ÷ 2.", "48//2", "4 decenas ÷ 2 = 2 y 8 ÷ 2 = 4."),
    ],
    und=[
        ex("En 75 ÷ 5, ¿cuántas decenas sobran después de dividir las 7 decenas?", "2", "7 ÷ 5 = 1 y sobran 2 decenas."),
        ex("¿Cómo se comprueba que 85 ÷ 4 = 21 y resto 1?", "21 × 4 + 1 = 85", "Cociente × divisor + resto = dividendo."),
        ex("¿Puede el resto de una división por 5 ser 5?", "No", "El resto debe ser menor que el divisor."),
    ],
    app=[
        arith("Calcula 91 ÷ 7.", "91//7", "9 decenas ÷ 7 = 1, sobran 2; 21 ÷ 7 = 3."),
        arith("Calcula 92 ÷ 4.", "92//4", "9 decenas ÷ 4 = 2, sobra 1; 12 ÷ 4 = 3."),
        ex("Calcula 79 ÷ 6. Escribe el cociente y el resto.", "13 y resto 1", "7 decenas ÷ 6 = 1, sobra 1; 19 ÷ 6 = 3, sobra 1; 13 × 6 + 1 = 79."),
    ],
    rea=[
        ex("Tomás dice que 50 ÷ 6 = 7 y resto 8. ¿Puede ser?", "No, es 8 y resto 2", "El resto debe ser menor que 6. 8 × 6 = 48 y 50 − 48 = 2."),
        ex("Rosa dice que 61 ÷ 5 = 12 y resto 1. Compruébalo con la multiplicación.", "Sí", "12 × 5 + 1 = 61."),
    ],
    cha=[
        arith("En una división el cociente es 14, el divisor 6 y el resto 3. ¿Cuál es el dividendo?", "14*6+3", "Dividendo = cociente × divisor + resto."),
        ex("¿Cuál es el mayor resto posible al dividir por 7?", "6", "El resto debe ser menor que el divisor."),
    ],
    ctx=[ex("Una caja tiene 82 chocolates que se guardan en bolsas de 5. ¿Cuántas bolsas se llenan y cuántos chocolates sobran?", "16 bolsas y sobran 2", "16 × 5 = 80 y 82 − 80 = 2.")],
    sc=[
        arith("Calcula 96 ÷ 3.", "96//3", "9 decenas ÷ 3 = 3 y 6 ÷ 3 = 2."),
        ex("Calcula 47 ÷ 5. Escribe el cociente y el resto.", "9 y resto 2", "9 × 5 = 45 y 47 − 45 = 2."),
        ex("En 47 ÷ 5 = 9 y resto 2, ¿qué suma comprueba el resultado?", "9 × 5 + 2 = 47", "Cociente × divisor + resto = dividendo."),
    ],
    op=task(
        "Calcula 95 ÷ 4 y 72 ÷ 6 con el algoritmo. Escribe los pasos con decenas y unidades, el resto si lo hay, y comprueba con cociente × divisor + resto.",
        "95 ÷ 4: 9 decenas ÷ 4 = 2, sobra 1 decena; 15 ÷ 4 = 3, sobra 3: 23 y resto 3. Compruebo: 23 × 4 + 3 = 95. 72 ÷ 6: 7 decenas ÷ 6 = 1, sobra 1; 12 ÷ 6 = 2: 12. Compruebo: 12 × 6 = 72.",
        ["divide decenas y baja unidades", "identifica el resto", "comprueba con la multiplicación"],
        ["dos divisiones escritas con pasos", "comprobaciones"],
        ["resto mayor que el divisor", "olvidar bajar las unidades"],
        "Pide que verifique que el resto es menor que el divisor y luego que multiplique para comprobar.",
    ),
    reinforce="Calcula 58 ÷ 4 y comprueba con cociente × divisor + resto.",
    extend="Calcula 99 ÷ 8 y escribe todo lo que comprobaste para saber que el resto es correcto.",
)

lesson(
    OA6, 5,
    use="Aprenderé a interpretar el cociente y el resto según la situación. Sirve para decidir si el resto se ignora, se reparte o pide una unidad más, por ejemplo cuántos buses se necesitan.",
    prior=["Sé dividir con resto.", "Sé que el resto es menor que el divisor."],
    explain=[
        "El cociente y el resto significan cosas según la historia. Si se reparten 47 stickers entre 5 amigos, cada uno recibe 9 (cociente) y sobran 2 (resto). Los 2 que sobran no se pueden repartir en partes iguales sin cortarlos, así que quedan sin repartir.",
        "A veces el resto obliga a usar una unidad más. Si 50 personas viajan en buses de 6 asientos, 50 ÷ 6 = 8 y resto 2. Con 8 buses viajan 48; las 2 personas que sobran necesitan otro bus. Se necesitan 9 buses.",
        "Para decidir, relee la pregunta. Si pregunta cuánto recibe cada uno o cuántos se llenan, responde con el cociente. Si pregunta cuánto sobra, responde con el resto. Si pregunta cuántos se necesitan para llevar o guardar todo, y hay resto, suma 1 al cociente.",
    ],
    vocab=[("cociente", "resultado de la división; cuánto toca a cada uno o cuántos grupos"), ("resto", "lo que sobra"), ("situación", "historia o problema donde se usa la división"), ("repartir", "dar partes iguales"), ("interpretar", "decir qué significa un resultado en la historia")],
    worked=[
        W("Responder con el cociente y el resto", "Se reparten 47 stickers entre 5 amigos en partes iguales. ¿Cuántos recibe cada uno y cuántos sobran?", ["47 ÷ 5 = 9 y resto 2, porque 9 × 5 = 45.", "Cada amigo recibe 9 stickers.", "Sobran 2 stickers."], "9 cada uno y sobran 2"),
        W("Resto que pide una unidad más", "50 personas viajan en buses de 6 asientos. ¿Cuántos buses se necesitan?", ["50 ÷ 6 = 8 y resto 2.", "8 buses llevan 48 personas; sobran 2 sin asiento.", "Se necesita 1 bus más: 8 + 1 = 9."], "9 buses"),
    ],
    mistakes=[
        M("Responder 8 buses para llevar 50 personas.", "Se ignora el resto de 2 personas que se quedan sin viajar.", "Cuando preguntan cuántos se necesitan para todos y hay resto, suma 1 al cociente."),
        M("Responder «sobran 9» en el reparto de stickers.", "Se confunde el resto con el cociente.", "El cociente (9) es lo que recibe cada uno. El resto (2) es lo que sobra."),
    ],
    rec=[
        ex("Se reparten 47 stickers entre 5 amigos. ¿Cuántos sobran?", "2", "9 × 5 = 45 y 47 − 45 = 2."),
        ex("Se reparten 47 stickers entre 5 amigos. ¿Cuántos recibe cada uno?", "9", "47 ÷ 5 = 9 y resto 2."),
        ex("¿Cuánto es 20 ÷ 6? Escribe el cociente y el resto.", "3 y resto 2", "3 × 6 = 18 y 20 − 18 = 2."),
    ],
    und=[
        ex("Si preguntan cuántos buses se necesitan para llevar a 50 personas en buses de 6, ¿qué hay que hacer con el resto 2?", "Sumar 1 al cociente", "Las 2 personas que sobran necesitan otro bus."),
        ex("Si preguntan cuánto recibe cada amigo, ¿se responde con el cociente o con el resto?", "Con el cociente", "El cociente es lo que toca a cada uno."),
        ex("Si preguntan cuánto sobra, ¿se responde con el cociente o con el resto?", "Con el resto", "El resto es lo que no se alcanzó a repartir."),
    ],
    app=[
        ex("Se guardan 62 manzanas en bolsas de 8. ¿Cuántas bolsas se llenan y cuántas manzanas sobran?", "7 bolsas y sobran 6", "7 × 8 = 56 y 62 − 56 = 6."),
        ex("Se guardan 62 manzanas en bolsas de 8 y se necesita guardar todas. ¿Cuántas bolsas se necesitan?", "8 bolsas", "7 bolsas llenas y 6 manzanas más necesitan otra bolsa."),
        ex("Un profesor tiene 38 lápices y los reparte entre 5 estudiantes por igual. ¿Cuántos lápices recibe cada uno y cuántos sobran?", "7 cada uno y sobran 3", "7 × 5 = 35 y 38 − 35 = 3."),
    ],
    rea=[
        ex("Para llevar a 50 personas en buses de 6 asientos, un estudiante dice 8 buses. ¿Alcanza?", "No, se necesitan 9", "8 buses llevan 48 personas; 2 quedan sin asiento."),
        ex("Una caja guarda 6 huevos. ¿Cuántas cajas hacen falta para guardar 40 huevos?", "7 cajas", "40 ÷ 6 = 6 y resto 4; los 4 huevos que sobran necesitan una caja más."),
    ],
    cha=[
        ex("Se reparten 95 dulces entre 4 cursos en partes iguales. Cada curso recibe la mayor cantidad posible. ¿Cuántos dulces recibe cada curso y cuántos sobran?", "23 cada uno y sobran 3", "23 × 4 = 92 y 95 − 92 = 3."),
        ex("En una división entre 7 el cociente es 12 y sobran 5. ¿Cuál era el dividendo?", "89", "12 × 7 + 5 = 84 + 5 = 89."),
    ],
    ctx=[ex("Un grupo de 33 estudiantes sale de paseo en autos de 4 asientos. ¿Cuántos autos se necesitan para que todos vayan sentados?", "9 autos", "33 ÷ 4 = 8 y resto 1; ese estudiante necesita otro auto.")],
    sc=[
        ex("Se reparten 30 caramelos entre 7 niños. ¿Cuántos recibe cada uno y cuántos sobran?", "4 cada uno y sobran 2", "4 × 7 = 28 y 30 − 28 = 2."),
        ex("Si 25 personas viajan en autos de 4 asientos, ¿cuántos autos se necesitan?", "7 autos", "25 ÷ 4 = 6 y resto 1; ese viajero necesita otro auto."),
        ex("Se guardan 20 pelotas en cajas de 6. ¿Cuántas cajas se llenan?", "3", "20 ÷ 6 = 3 y resto 2; solo 3 cajas quedan llenas."),
    ],
    op=task(
        "Resuelve estos tres problemas y escribe en cada uno qué significan el cociente y el resto en la historia: a) 58 galletas se reparten entre 7 niños. b) 58 personas viajan en vans de 7 asientos: ¿cuántas vans se necesitan? c) 58 hojas se guardan en carpetas de 7: ¿cuántas carpetas quedan llenas?",
        "58 ÷ 7 = 8 y resto 2. a) Cada niño recibe 8 galletas y sobran 2. b) Se necesitan 9 vans, porque las 2 personas restantes necesitan una van más. c) Quedan llenas 8 carpetas.",
        ["calcula bien 58 ÷ 7", "interpreta el cociente según cada historia", "suma 1 solo cuando corresponde"],
        ["división escrita", "tres respuestas con explicación"],
        ["ignorar el resto en el problema de las vans", "confundir el cociente con lo que sobra"],
        "Pide que relea la pregunta de cada problema y subraye si se busca lo que recibe cada uno, lo que sobra o lo que se necesita.",
    ),
    reinforce="Reparte 29 lápices entre 4 estuches y escribe cuántos hay en cada estuche y cuántos sobran.",
    extend="Inventa un problema con 53 ÷ 6 en que la respuesta sea el cociente más 1 y explica por qué.",
)
