"""Cuaderno del estudiante de 4.º básico Matemática: OA 03 (adición y sustracción hasta 1.000) y OA 04 (propiedades del 0 y del 1)."""
from __future__ import annotations

from student_content_ma04_a import M, W, lesson, task
from student_lessons import arith, ex

OA3 = "MA04 OA 03"
OA4 = "MA04 OA 04"

# ------------------------------------------------------------------ OA 03
lesson(
    OA3, 1,
    use="Aprenderé a sumar y restar números de tres cifras con mis propias estrategias, separándolos en centenas, decenas y unidades. Sirve para calcular sin depender de una sola forma.",
    prior=["Sé sumar y restar números de dos cifras.", "Sé el valor posicional de centenas, decenas y unidades."],
    explain=[
        "Una estrategia personal es una forma propia de calcular que puedes explicar y comprobar. La más usada es descomponer: separar los números en centenas, decenas y unidades. Para 346 + 257 sumas por separado 300 + 200, 40 + 50 y 6 + 7, y después juntas los resultados.",
        "En la resta puedes quitar por partes. Para 625 − 238, parte de 625 y resta 200 (queda 425), luego 30 (queda 395) y al final 8 (queda 387). También puedes restar en otro orden. Lo importante es no olvidar ninguna parte y explicar cada paso.",
        "Dos estrategias distintas deben dar el mismo resultado. Comprueba con la operación inversa: si 625 − 238 = 387, entonces 387 + 238 debe dar 625. Si no coincide, revisa dónde se perdió una parte o se equivocó una suma pequeña.",
    ],
    vocab=[("estrategia personal", "forma propia de calcular que sé explicar"), ("descomponer", "separar un número en centenas, decenas y unidades"), ("sumando", "cada número que se suma"), ("diferencia", "resultado de una resta"), ("operación inversa", "la operación que deshace a la otra: la suma deshace la resta")],
    worked=[
        W("Sumar descomponiendo", "Calcula 346 + 257 separando en centenas, decenas y unidades.", ["Centenas: 300 + 200 = 500.", "Decenas: 40 + 50 = 90.", "Unidades: 6 + 7 = 13.", "Junto: 500 + 90 + 13 = 603."], "603"),
        W("Restar por partes", "Calcula 625 − 238 quitando por partes.", ["Resto las centenas: 625 − 200 = 425.", "Resto las decenas: 425 − 30 = 395.", "Resto las unidades: 395 − 8 = 387.", "Compruebo con la suma: 387 + 238 = 625."], "387"),
    ],
    mistakes=[
        M("Calcular 346 + 257 como 593.", "Se escribió 3 en vez de 13 al sumar las unidades 6 + 7.", "6 + 7 = 13. Junta todo: 500 + 90 + 13 = 603."),
        M("Calcular 625 − 238 como 413 por restar 200 y luego sumar 30 y 8 a 425.", "Se suma en vez de restar las partes pequeñas.", "Las tres partes se restan: 425 − 30 − 8 = 387."),
    ],
    rec=[
        arith("Calcula 120 + 135 separando en centenas, decenas y unidades.", "120+135", "100 + 100 = 200, 20 + 30 = 50 y 0 + 5 = 5."),
        arith("Calcula 450 − 120 quitando primero las centenas y después las decenas.", "450-120", "450 − 100 = 350 y 350 − 20 = 330."),
        arith("Calcula 300 + 250 de cabeza.", "300+250", "300 + 200 = 500 y 500 + 50 = 550."),
    ],
    und=[
        ex("Ana calcula 250 + 130 como 200 + 100 y 50 + 30. Beto lo calcula como 250 + 100 + 30. ¿Dan el mismo resultado?", "Sí, ambas dan 380", "Ana: 300 + 80 = 380. Beto: 350 + 30 = 380."),
        ex("Para comprobar que 625 − 238 = 387, ¿qué suma se calcula?", "387 + 238", "La suma es la operación inversa de la resta: debe dar 625."),
        ex("¿Qué número es el sumando que falta en 346 + __ = 603?", "257", "Se resta: 603 − 346 = 257."),
    ],
    app=[
        arith("En una biblioteca hay 238 libros de cuentos y 145 de ciencias. ¿Cuántos libros hay en total?", "238+145", "Se suman centenas, decenas y unidades."),
        arith("Una tienda tenía 700 lápices y vendió 256. ¿Cuántos lápices quedan?", "700-256", "Se resta por partes: 700 − 200 − 50 − 6."),
        arith("Un tren hizo un viaje de 465 km y otro de 289 km. ¿Cuántos kilómetros recorrió en total?", "465+289", "400 + 200 = 600, 60 + 80 = 140 y 5 + 9 = 14: en total 754."),
    ],
    rea=[
        ex("Teo calculó 346 + 257 sumando 500 + 90 + 3 = 593. ¿Qué error cometió y cuál es el resultado correcto?", "6 + 7 es 13, no 3; da 603", "500 + 90 + 13 = 603."),
        ex("Dos estrategias para 480 − 175: A) 480 − 100 = 380 y 380 − 75 = 305. B) 480 − 200 = 280 y 280 + 25 = 305. ¿Son correctas las dos?", "Sí, ambas dan 305", "En B se restó 25 de más, así que se devuelven 25."),
    ],
    cha=[
        ex("La suma de 237 y otro número es 500. ¿Cuál es el otro número? Usa la operación inversa.", "263", "500 − 237 = 263 y 237 + 263 = 500."),
        ex("Rafa calcula 398 + 275 así: 400 + 275 − 2. ¿Qué resultado obtiene?", "673", "400 + 275 = 675 y se quitan los 2 sumados de más: 673."),
    ],
    ctx=[ex("Un colegio tiene 345 estudiantes en la mañana y 278 en la tarde. ¿Cuántos estudiantes tiene en total?", "623", "300 + 200 = 500, 40 + 70 = 110 y 5 + 8 = 13: 623.")],
    sc=[
        arith("Calcula 214 + 335.", "214+335", "Se suman centenas, decenas y unidades."),
        arith("Calcula 540 − 270 quitando por partes.", "540-270", "540 − 200 = 340 y 340 − 70 = 270."),
        ex("¿Qué operación comprueba que 450 + 275 = 725?", "725 − 275", "La resta 725 − 275 debe dar 450."),
    ],
    op=task(
        "Calcula 367 + 258 y 804 − 346 con una estrategia propia. Escribe tus pasos y comprueba cada resultado con la operación inversa.",
        "367 + 258: 300 + 200 = 500, 60 + 50 = 110, 7 + 8 = 15, total 625. Compruebo: 625 − 258 = 367. 804 − 346: 804 − 300 = 504, 504 − 40 = 464, 464 − 6 = 458. Compruebo: 458 + 346 = 804.",
        ["resuelve bien las dos cuentas", "escribe pasos que se entienden", "comprueba con la operación inversa"],
        ["pasos escritos en el cuaderno", "comprobaciones escritas"],
        ["olvidar una de las partes", "sumar en vez de restar en la comprobación"],
        "Valora que explique la estrategia; si el resultado no coincide en la comprobación, pide que busque en qué paso falló.",
    ),
    reinforce="Con monedas dibujadas de $ 100, $ 10 y $ 1, representa 235 + 142 y cuenta cuántas piezas de cada tipo hay.",
    extend="Calcula 999 − 456 con dos estrategias distintas y comprueba que dan lo mismo.",
)

lesson(
    OA3, 2,
    use="Aprenderé a estimar sumas y restas redondeando los números. Sirve para saber si un resultado es razonable antes o después de calcular.",
    prior=["Sé sumar y restar números de tres cifras.", "Sé qué es una decena y una centena."],
    explain=[
        "Estimar es calcular un resultado aproximado, cercano al exacto. Para estimar, redondeas cada número a la decena o a la centena más cercana. Para redondear a la centena, mira la cifra de las decenas: si es 5 o más, la centena sube; si es menos de 5, queda igual.",
        "Por ejemplo, 489 redondeado a la centena es 500, y 312 es 300. Entonces 489 + 312 es aproximadamente 500 + 300 = 800. El cálculo exacto es 801, muy cerca. Se usa el signo ≈ que significa «aproximadamente».",
        "La estimación sirve para revisar resultados. Si estimas 800 y tu cálculo exacto da 1.801, algo salió mal. También ayuda a decidir rápido, por ejemplo si te alcanza el dinero. Elige a qué lugar redondear: a la centena es más fácil, a la decena es más preciso.",
    ],
    vocab=[("estimar", "calcular un resultado cercano sin hacer la cuenta exacta"), ("redondear", "cambiar un número por el más cercano terminado en 0 o 00"), ("aproximadamente (≈)", "casi igual, no exacto"), ("resultado razonable", "resultado cercano a lo que se espera"), ("centena más cercana", "número terminado en 00 al que está más cerca, como 300 o 700")],
    worked=[
        W("Estimar una suma", "Estima 489 + 312 redondeando a la centena.", ["489 está más cerca de 500 (decenas: 8, sube).", "312 está más cerca de 300 (decenas: 1, queda).", "500 + 300 = 800."], "≈ 800"),
        W("Estimar una resta", "Estima 623 − 198 redondeando a la centena.", ["623 queda en 600 (decenas: 2).", "198 queda en 200 (decenas: 9, sube).", "600 − 200 = 400."], "≈ 400"),
    ],
    mistakes=[
        M("Redondear 650 a 600.", "Se olvida que con 5 en las decenas el número sube a la centena siguiente.", "650 redondeado a la centena es 700."),
        M("Decir que la estimación 800 es incorrecta porque el resultado exacto es 801.", "Se confunde estimar con calcular exacto.", "Una estimación es aproximada. Sirve que el exacto esté cerca."),
    ],
    rec=[
        ex("Redondea 487 a la centena más cercana.", "500", "Las decenas son 8, que es 5 o más: la centena sube."),
        ex("Redondea 342 a la decena más cercana.", "340", "Las unidades son 2, menos de 5: la decena queda igual."),
        ex("Redondea 650 a la centena más cercana.", "700", "Las decenas son 5: sube a la centena siguiente."),
    ],
    und=[
        ex("Estima 298 + 405 redondeando a la centena.", "700", "298 ≈ 300 y 405 ≈ 400; 300 + 400 = 700."),
        ex("Al sumar 314 + 589 el resultado exacto es 903 o 1.903. ¿Cuál es razonable si la estimación es 300 + 600?", "903", "La estimación es 900, cerca de 903."),
        ex("¿Qué significa el signo ≈?", "Aproximadamente", "Se usa cuando el resultado es cercano, pero no exacto."),
    ],
    app=[
        ex("Estima 412 + 389 redondeando a la centena.", "800", "412 ≈ 400 y 389 ≈ 400; 400 + 400 = 800."),
        ex("Estima 748 − 251 redondeando a la decena.", "500", "748 ≈ 750 y 251 ≈ 250; 750 − 250 = 500."),
        ex("Estima 836 − 412 redondeando a la centena.", "400", "836 ≈ 800 y 412 ≈ 400; 800 − 400 = 400."),
    ],
    rea=[
        ex("Pía estimó 489 + 312 como 500 + 300 y dijo que 801 no puede ser el resultado exacto. ¿Tiene razón?", "No", "801 está muy cerca de la estimación 800, así que es razonable."),
        ex("Una estimación da 800 pero un compañero calculó 1.801. ¿Qué conviene hacer?", "Revisar el cálculo", "1.801 está muy lejos de 800, así que hay un error en la cuenta."),
    ],
    cha=[
        ex("Estima 248 + 252 a la centena y calcula el resultado exacto. ¿Coinciden?", "Sí, ambos dan 500", "248 ≈ 200 (decenas 4, no sube) y 252 ≈ 300 (decenas 5, sube). 200 + 300 = 500 y el exacto 248 + 252 también es 500."),
        ex("Estima 802 − 395 a la centena. El resultado exacto es 407. ¿Cuánto se diferencia la estimación del exacto?", "7", "802 ≈ 800 y 395 ≈ 400; 800 − 400 = 400. Y 407 − 400 = 7."),
    ],
    ctx=[ex("Mario tiene $ 800. Quiere comprar un libro de $ 489 y una carpeta de $ 205. Estima con centenas si le alcanza.", "Sí, le alcanza", "500 + 200 = 700, que es menos que 800. El total exacto es 694.")],
    sc=[
        ex("Redondea 276 a la centena.", "300", "Las decenas son 7: la centena sube."),
        ex("Estima 197 + 304 a la centena.", "500", "200 + 300 = 500."),
        ex("Estima 905 − 498 a la centena.", "400", "900 − 500 = 400."),
    ],
    op=task(
        "Estima a la centena cada cuenta y luego calcula el resultado exacto: 327 + 418, 692 − 305 y 144 + 556. Escribe cuánto se diferencia la estimación del exacto.",
        "327 + 418 ≈ 300 + 400 = 700; exacto 745. 692 − 305 ≈ 700 − 300 = 400; exacto 387. 144 + 556 ≈ 100 + 600 = 700; exacto 700.",
        ["redondea bien", "estima las tres", "calcula el exacto y compara"],
        ["tres estimaciones y tres resultados exactos", "diferencia anotada"],
        ["redondear 5 hacia abajo", "calcular exacto en vez de estimar"],
        "Pide que diga si la estimación fue cercana y que explique por qué a veces se aleja más del exacto.",
    ),
    reinforce="Redondea a la centena los números 143, 250, 678 y 951 y escríbelos en una tabla.",
    extend="Busca dos números de tres cifras cuya suma exacta sea 700 pero cuya estimación a la centena dé 800. Pista: prueba con números que terminen en 50. Explica por qué pasa.",
)

lesson(
    OA3, 3,
    use="Aprenderé el algoritmo para sumar hasta cuatro sumandos en columnas, con reagrupación. Sirve para sumar varias cantidades sin perder ninguna.",
    prior=["Sé sumar dos números de tres cifras.", "Sé que 10 unidades forman 1 decena y 10 decenas forman 1 centena."],
    explain=[
        "El algoritmo de la suma ordena los números en columnas: unidades bajo unidades, decenas bajo decenas y centenas bajo centenas. Se suma de derecha a izquierda, columna por columna. Con cuatro sumandos haces lo mismo, solo que cada columna tiene más números.",
        "Si una columna suma 10 o más, se reagrupa. Si las unidades suman 26, escribes 6 abajo y llevas 2 decenas a la columna de las decenas. Después sumas las decenas con esa 2 que llevas. Lo mismo pasa con las centenas.",
        "Antes de sumar, estima para saber más o menos cuánto debe dar. Después de sumar, revisa que la cuenta tenga todos los sumandos y que los lleves bien. Una forma de comprobar es sumar de abajo hacia arriba y ver si da lo mismo.",
    ],
    vocab=[("algoritmo", "pasos ordenados para hacer una cuenta"), ("columna", "números alineados de arriba hacia abajo"), ("reagrupar (llevar)", "pasar 10 de un lugar como 1 al lugar siguiente"), ("sumando", "cada número que se suma"), ("total", "resultado de una suma")],
    worked=[
        W("Cuatro sumandos", "Calcula 245 + 318 + 127 + 206 en columnas.", ["Unidades: 5 + 8 + 7 + 6 = 26. Escribo 6 y llevo 2 decenas.", "Decenas: 4 + 1 + 2 + 0 + 2 que llevo = 9. Escribo 9.", "Centenas: 2 + 3 + 1 + 2 = 8. Escribo 8."], "896"),
        W("Tres sumandos con dos reagrupaciones", "Calcula 134 + 256 + 89 en columnas.", ["Unidades: 4 + 6 + 9 = 19. Escribo 9 y llevo 1 decena.", "Decenas: 3 + 5 + 8 + 1 que llevo = 17. Escribo 7 y llevo 1 centena.", "Centenas: 1 + 2 + 0 + 1 que llevo = 4."], "479"),
    ],
    mistakes=[
        M("Escribir 26 en la columna de las unidades al sumar 5 + 8 + 7 + 6.", "No se reagrupa cuando la columna suma 10 o más.", "Escribe solo 6 y lleva 2 decenas a la columna siguiente."),
        M("Alinear 89 bajo las centenas.", "Se alinea por la izquierda en vez de por la derecha.", "Alinea las unidades con las unidades: el 9 de 89 va bajo las unidades."),
    ],
    rec=[
        arith("Suma en columnas: 123 + 241 + 312 + 104.", "123+241+312+104", "Unidades: 3 + 1 + 2 + 4 = 10; se lleva 1 decena."),
        arith("Suma: 128 + 235.", "128+235", "Unidades: 8 + 5 = 13; escribe 3 y lleva 1."),
        arith("Suma: 146 + 52 + 301.", "146+52+301", "Unidades: 6 + 2 + 1 = 9. Decenas: 4 + 5 + 0 = 9. Centenas: 1 + 3 = 4."),
    ],
    und=[
        ex("En 245 + 318 + 127 + 206, las unidades suman 26. ¿Qué número se escribe en la columna y cuántas decenas se llevan?", "Se escribe 6 y se llevan 2", "26 unidades son 2 decenas y 6 unidades."),
        ex("¿Qué lugar de 89 queda bajo la columna de las decenas al sumar 134 + 256 + 89?", "El 8", "En 89, el 8 son decenas y el 9 son unidades."),
        ex("Si las decenas suman 17 y llevas 1 centena, ¿qué cifra escribes en la columna de las decenas?", "7", "17 decenas son 1 centena y 7 decenas."),
    ],
    app=[
        arith("Un almacén recibió cajas con 145, 238, 106 y 215 tornillos. ¿Cuántos tornillos son en total?", "145+238+106+215", "Unidades: 5 + 8 + 6 + 5 = 24; se lleva 2."),
        arith("En cuatro días un parque tuvo 120, 87, 156 y 205 visitantes. ¿Cuántos visitantes tuvo en total?", "120+87+156+205", "Se suman las columnas con reagrupación."),
        arith("Una ruta tiene tres tramos: 235 m, 164 m y 318 m. ¿Cuánto mide la ruta completa?", "235+164+318", "Unidades: 5 + 4 + 8 = 17; se lleva 1."),
    ],
    rea=[
        ex("Sara sumó 38 + 47 + 59 y obtuvo 134. ¿Está bien? Si no, escribe el resultado.", "No, es 144", "Unidades: 8 + 7 + 9 = 24, se lleva 2. Decenas: 3 + 4 + 5 + 2 = 14. Total 144."),
        ex("Nico dice que 245 + 318 + 127 + 206 da más de 1.000. Usa una estimación a la centena para revisar.", "No, da menos", "200 + 300 + 100 + 200 = 800, que es menos de 1.000. El exacto es 896."),
    ],
    cha=[
        ex("Cuatro sumandos iguales, todos de tres cifras, suman 400. ¿Cuál es el sumando?", "100", "400 ÷ 4 = 100, o 100 + 100 + 100 + 100 = 400."),
        ex("Falta una cifra: 2_5 + 168 = 413. ¿Qué cifra falta?", "4", "413 − 168 = 245, así que la cifra que falta es 4."),
    ],
    ctx=[ex("En una campaña juntaron 135 kilos de arroz el lunes, 208 el martes, 96 el miércoles y 147 el jueves. ¿Cuántos kilos juntaron?", "586", "Unidades: 5 + 8 + 6 + 7 = 26. Decenas: 3 + 0 + 9 + 4 + 2 = 18. Centenas: 1 + 2 + 0 + 1 + 1 = 5.")],
    sc=[
        arith("Suma: 214 + 135 + 342.", "214+135+342", "Unidades 4 + 5 + 2 = 11; se lleva 1."),
        arith("Suma: 78 + 96.", "78+96", "Unidades: 8 + 6 = 14; escribe 4 y lleva 1."),
        arith("Suma: 150 + 220 + 135 + 98.", "150+220+135+98", "Unidades: 0 + 0 + 5 + 8 = 13; se lleva 1."),
    ],
    op=task(
        "Calcula en columnas la suma 126 + 247 + 185 + 98. Antes estima a la centena. Después calcula el resultado exacto y comprueba sumando de abajo hacia arriba.",
        "Estimación: 100 + 200 + 200 + 100 = 600. Exacto: unidades 6 + 7 + 5 + 8 = 26 (6, llevo 2); decenas 2 + 4 + 8 + 9 + 2 = 25 (5, llevo 2); centenas 1 + 2 + 1 + 2 = 6: 656. Comprobación de abajo hacia arriba: 656.",
        ["alinea las columnas", "reagrupa bien", "estima antes", "comprueba"],
        ["suma en columnas escrita", "estimación y comprobación"],
        ["no llevar", "alinear mal el 98"],
        "Si no coincide con la estimación, pide que revise primero el alineamiento de columnas.",
    ),
    reinforce="Suma 35 + 48 + 17 en columnas, marcando con un círculo lo que llevas.",
    extend="Un cine tuvo 245, 318, 127 y 206 espectadores en cuatro funciones. Escribe otra lista de cuatro números que dé el mismo total.",
)

lesson(
    OA3, 4,
    use="Aprenderé el algoritmo para restar con canjes, incluso cuando hay ceros. Sirve para calcular cuánto queda o cuánto falta con números de tres cifras.",
    prior=["Sé restar números de dos cifras.", "Sé que 1 centena son 10 decenas y 1 decena son 10 unidades."],
    explain=[
        "En la resta, el minuendo es el número del que se quita y el sustraendo es el número que se quita. Se restan las columnas de derecha a izquierda. Si en una columna el número de arriba es menor que el de abajo, necesitas un canje: pides 1 al lugar de la izquierda y lo conviertes en 10 del lugar actual.",
        "Cuando el lugar de la izquierda tiene 0, el canje es sucesivo. En 703 − 258, las unidades 3 no alcanzan para restar 8 y las decenas son 0. Pides 1 centena: queda 6 centenas y 10 decenas. De esas 10 decenas pides 1, quedan 9 decenas y las unidades pasan a 13. Ahora puedes restar.",
        "Para comprobar una resta, suma el resultado con el sustraendo: debe dar el minuendo. En 703 − 258 = 445 se comprueba con 445 + 258 = 703. Si no da, revisa los canjes.",
    ],
    vocab=[("minuendo", "número del que se resta"), ("sustraendo", "número que se resta"), ("canje", "cambiar 1 de un lugar por 10 del lugar de la derecha"), ("diferencia", "resultado de la resta"), ("comprobar", "revisar con la operación inversa")],
    worked=[
        W("Canje sucesivo con cero", "Calcula 703 − 258.", ["Unidades: 3 − 8 no se puede. Decenas es 0, así que pido a las centenas: 6 centenas y 10 decenas.", "Pido 1 decena: 9 decenas y las unidades quedan en 13. 13 − 8 = 5.", "Decenas: 9 − 5 = 4. Centenas: 6 − 2 = 4.", "Compruebo: 445 + 258 = 703."], "445"),
        W("Un canje simple", "Calcula 842 − 367.", ["Unidades: 2 − 7 no se puede. Pido 1 decena: quedan 3 decenas y 12 unidades. 12 − 7 = 5.", "Decenas: 3 − 6 no se puede. Pido 1 centena: quedan 7 centenas y 13 decenas. 13 − 6 = 7.", "Centenas: 7 − 3 = 4."], "475"),
    ],
    mistakes=[
        M("Calcular 842 − 367 restando siempre el número menor del mayor: 5, 2, 5 (525).", "En cada columna se resta el menor del mayor sin hacer canjes.", "La resta siempre es de arriba menos abajo. Si no alcanza, haz un canje."),
        M("En 703 − 258 poner 10 en las decenas sin quitar 1 a las centenas.", "Se convierten unidades sin bajar el lugar de donde se pidió.", "Al pedir 1 centena, esta queda en 6. Después de pedir 1 decena, las decenas quedan en 9."),
    ],
    rec=[
        arith("Calcula 756 − 321.", "756-321", "En cada columna se puede restar sin canje."),
        arith("Calcula 542 − 118.", "542-118", "Unidades: 12 − 8 = 4 con canje de 1 decena."),
        arith("Calcula 600 − 234.", "600-234", "Se necesita canje sucesivo: 5 centenas, 9 decenas y 10 unidades."),
    ],
    und=[
        ex("En 703 − 258, ¿cuántas unidades quedan después de los canjes sucesivos y cuántas decenas?", "13 unidades y 9 decenas", "Se pide 1 centena, luego 1 decena: decenas quedan 9 y unidades 13."),
        ex("En una resta, ¿cómo se llama el número del que se quita?", "Minuendo", "El sustraendo es el que se quita; el minuendo es el que queda arriba."),
        ex("¿Cómo compruebas que 445 es la respuesta de 703 − 258?", "445 + 258 = 703", "Se suma el resultado con el sustraendo y se obtiene el minuendo."),
    ],
    app=[
        arith("Una escuela tiene 503 estudiantes y 168 son de básica. ¿Cuántos no son de básica?", "503-168", "Unidades: 3 − 8 con canje sucesivo."),
        arith("Un estanque tiene 1.000 litros de agua y se usan 357. ¿Cuántos litros quedan?", "1000-357", "Canje sucesivo con tres ceros."),
        arith("Un tren llevaba 724 pasajeros y se bajaron 385. ¿Cuántos quedan?", "724-385", "Se hacen dos canjes."),
    ],
    rea=[
        ex("Lola calculó 800 − 365 y obtuvo 545. Usa la suma para comprobar si está bien.", "No, es 435", "545 + 365 = 910 y no 800; en cambio 435 + 365 = 800."),
        ex("Sofía dice que para 603 − 405 no hace falta canje. ¿Tiene razón?", "No, hace falta canje", "Las unidades 3 − 5 no se pueden restar, y las decenas son 0: hay que pedir a la centena. El resultado es 198."),
    ],
    cha=[
        ex("Falta una cifra: 5_2 − 283 = 249. ¿Qué cifra falta?", "3", "249 + 283 = 532. La cifra que falta es 3."),
        ex("Un número menos 358 da 499. ¿Cuál es el número?", "857", "499 + 358 = 857."),
    ],
    ctx=[ex("En una biblioteca había 910 libros y se prestaron 476. ¿Cuántos libros quedan en las estanterías?", "434", "Unidades: 10 − 6 = 4, decenas: 0 − 7 con canje, centenas: 8 − 4 = 4.")],
    sc=[
        arith("Calcula 905 − 378.", "905-378", "Canje sucesivo porque las decenas son 0."),
        arith("Calcula 640 − 275.", "640-275", "Unidades: 0 − 5 con canje."),
        ex("¿Cómo se llama el resultado de una resta?", "Diferencia", "La diferencia es lo que queda o lo que falta."),
    ],
    op=task(
        "Calcula 802 − 467 con canjes. Escribe cada canje que haces y comprueba con una suma. Luego inventa una historia corta para esa resta, con unidades.",
        "802 − 467: pido 1 centena (7 centenas y 10 decenas), pido 1 decena (9 decenas y 12 unidades); 12 − 7 = 5, 9 − 6 = 3, 7 − 4 = 3: 335. Comprobación: 335 + 467 = 802. Historia: había 802 hojas y se usaron 467; quedan 335 hojas.",
        ["hace los canjes sucesivos", "resuelve bien", "comprueba con la suma", "historia coherente con unidad"],
        ["resta escrita con canjes", "comprobación escrita", "historia escrita"],
        ["restar el menor del mayor en cada columna", "olvidar bajar el lugar que prestó"],
        "Pide que muestre dónde quedó cada cifra después de los canjes antes de revisar el resultado.",
    ),
    reinforce="Usa 8 centenas, 0 decenas y 2 unidades en bloques o dibujos y quita 4 centenas, 6 decenas y 7 unidades, canjeando cuando haga falta.",
    extend="Resuelve 1.000 − 1 y 1.000 − 999. ¿Qué observas en los canjes sucesivos?",
)

lesson(
    OA3, 5,
    use="Aprenderé a resolver problemas con sumas y restas, también problemas no rutinarios, y a comprobar mis respuestas. Sirve para decidir qué operación usar y revisar si tiene sentido.",
    prior=["Sé sumar hasta cuatro sumandos y restar con canjes.", "Sé estimar sumas y diferencias."],
    explain=[
        "Un problema rutinario se resuelve con una operación que ya conoces. Un problema no rutinario pide pensar más: puede haber más de un paso, datos que no se usan o hacer falta armar un esquema. Para ambos sirve el mismo camino: leer, decidir qué se busca, elegir la operación, calcular y comprobar.",
        "Para elegir la operación, pregúntate qué pasa en la historia. Si se juntan o se agregan cantidades, usa suma. Si se quita, se compara o se busca cuánto falta, usa resta. Un dibujo de barras ayuda: una barra para el total y partes marcadas con números.",
        "Siempre comprueba. Primero estima: ¿el resultado se parece a lo esperado? Después usa la operación inversa: suma para comprobar una resta y resta para comprobar una suma. Escribe la respuesta con la unidad, por ejemplo «118 stickers».",
    ],
    vocab=[("problema rutinario", "problema que se resuelve con una operación conocida"), ("problema no rutinario", "problema que pide más pasos o inventar un camino"), ("comprobar", "revisar la respuesta con una estimación o la operación inversa"), ("esquema de barras", "dibujo con una barra para el total y partes marcadas"), ("dato", "número o información que da el problema")],
    worked=[
        W("Problema de dos pasos", "Sofía tenía 250 stickers. Regaló algunos y le quedaron 118. Luego recibió 75. ¿Cuántos tiene ahora?", ["Primero: 118 es lo que le quedó. Ya sabemos el dato, no hay que calcular el regalo.", "Luego recibió 75: 118 + 75 = 193.", "Comprobación: 193 − 75 = 118."], "193 stickers"),
        W("Problema no rutinario", "Dos números suman 500. Uno es 120 más grande que el otro. ¿Cuáles son?", ["Si quito 120 del total, quedan dos partes iguales: 500 − 120 = 380.", "Cada parte igual es 380 ÷ 2 = 190. Ese es el menor.", "El mayor es 190 + 120 = 310.", "Compruebo: 190 + 310 = 500."], "190 y 310"),
    ],
    mistakes=[
        M("Sumar todos los números del problema sin pensar qué pasa en la historia.", "Se elige la operación por los números, no por la situación.", "Lee la historia y decide si se junta, se quita o se compara."),
        M("Escribir solo «193» como respuesta.", "Falta la unidad y no queda claro qué se contó.", "Escribe la respuesta como oración: «Sofía tiene 193 stickers»."),
    ],
    rec=[
        arith("En una caja hay 235 botones rojos y 148 azules. ¿Cuántos botones hay en total?", "235+148", "Se juntan las dos cantidades: es una suma."),
        arith("Un tanque tenía 600 litros y se sacaron 175. ¿Cuántos litros quedan?", "600-175", "Se quita una cantidad: es una resta."),
        arith("Lucas tiene 320 monedas y Ana 450. ¿Cuántas monedas más tiene Ana?", "450-320", "Comparar cuánto más es una resta."),
    ],
    und=[
        ex("En un problema se juntan dos cantidades. ¿Qué operación conviene usar?", "Suma", "Juntar o agregar es sumar."),
        ex("¿Qué operación comprueba una suma: la resta o la multiplicación?", "La resta", "Si 118 + 75 = 193, entonces 193 − 75 debe dar 118."),
        ex("En 500 = 190 + 310, ¿cuál es la diferencia entre los dos números?", "120", "310 − 190 = 120."),
    ],
    app=[
        arith("Sofía tenía 250 stickers, regaló 132 y luego recibió 75. ¿Cuántos tiene ahora?", "250-132+75", "Primero se resta lo regalado y luego se suma lo recibido."),
        arith("Un bus parte con 48 pasajeros, suben 27 y bajan 15. ¿Cuántos pasajeros hay?", "48+27-15", "Suben se suma y bajan se resta."),
        arith("Una escuela compró 3 paquetes de 100 hojas y usó 247 hojas. ¿Cuántas hojas le quedan?", "300-247", "Los paquetes dan 300 hojas; luego se resta lo usado."),
    ],
    rea=[
        ex("Dos números suman 500 y uno es 120 más grande que el otro. Un estudiante dice que son 250 y 250. ¿Tiene razón?", "No", "250 y 250 no se diferencian. Son 190 y 310."),
        ex("Pía dice que para saber cuántos le faltan a 250 para llegar a 400 debe sumar. ¿Qué operación da la respuesta?", "Resta: 400 − 250", "Se busca la diferencia: 150."),
    ],
    cha=[
        ex("Tres hermanos juntan $ 900. Ana puso $ 350 y Beto $ 280. ¿Cuánto puso Carla?", "$ 270", "350 + 280 = 630 y 900 − 630 = 270."),
        ex("La suma de tres números consecutivos de 10 en 10 es 300. ¿Cuáles son? (Pista: el del medio es la tercera parte de 300.)", "90, 100 y 110", "El del medio es 300 ÷ 3 = 100; los otros dos están a 10 de él."),
    ],
    ctx=[ex("Una panadería hizo 345 panes el sábado y 280 el domingo. Vendió 410 en total. ¿Cuántos panes quedaron?", "215", "345 + 280 = 625 y 625 − 410 = 215.")],
    sc=[
        arith("En una caja hay 125 lápices y se agregan 78. ¿Cuántos hay ahora?", "125+78", "Agregar es sumar."),
        arith("Pedro tiene 500 puntos y pierde 237. ¿Cuántos puntos le quedan?", "500-237", "Perder es restar."),
        ex("Si 346 + 257 = 603, ¿qué resta lo comprueba?", "603 − 257 = 346", "La resta con un sumando debe dar el otro."),
    ],
    op=task(
        "Resuelve este problema y compruébalo: «Una biblioteca tenía 640 libros. Prestó 285 y recibió 152 nuevos. ¿Cuántos libros tiene ahora?». Haz un esquema de barras, elige la operación de cada paso, estima y comprueba. Escribe la respuesta con unidad.",
        "640 − 285 = 355 y 355 + 152 = 507. Estimación a la centena: 640 ≈ 600, 285 ≈ 300 y 152 ≈ 200; 600 − 300 + 200 = 500, cercano a 507. Comprobación: 507 − 152 = 355 y 355 + 285 = 640. Respuesta: la biblioteca tiene 507 libros.",
        ["elige las operaciones correctas", "calcula bien", "estima y comprueba", "respuesta con unidad"],
        ["esquema de barras", "cálculos y comprobación", "respuesta en oración"],
        ["sumar todos los números", "olvidar la unidad"],
        "Pide que cuente la historia con sus palabras antes de elegir operación; si falla, revisa qué pasa con la cantidad en cada paso.",
    ),
    reinforce="Resuelve «Tengo 145 figuritas y regalo 68. ¿Cuántas me quedan?» y comprueba con la suma.",
    extend="Inventa un problema no rutinario sobre dos números que suman 600 y cuya diferencia es 80, y resuélvelo.",
)

# ------------------------------------------------------------------ OA 04
lesson(
    OA4, 1,
    use="Aprenderé qué pasa cuando multiplico un número por cero. Sirve para calcular rápido y no equivocarme en tablas y problemas.",
    prior=["Sé que multiplicar es sumar un número varias veces.", "Sé las tablas del 2, 5 y 10."],
    explain=[
        "Multiplicar es repetir un número. 4 × 3 significa 4 grupos de 3: 3 + 3 + 3 + 3 = 12. Cuando un factor es 0, el producto es 0. Si tienes 5 bolsas con 0 manzanas cada una, tienes 5 × 0 = 0 manzanas.",
        "También funciona al revés: 0 grupos de 6 son 0 × 6 = 0. Si no hay ninguna bolsa, no hay ninguna manzana, aunque cada bolsa tuviera muchas. Esto se llama propiedad del cero: cualquier número multiplicado por 0 da 0.",
        "La propiedad del 0 ayuda a ahorrar cálculo. Para 4.857 × 0 no hace falta multiplicar nada, el producto es 0. Pero cuidado: no se debe confundir con sumar 0. 8 + 0 = 8, pero 8 × 0 = 0.",
    ],
    vocab=[("factor", "cada número que se multiplica"), ("producto", "resultado de una multiplicación"), ("propiedad del cero", "todo número multiplicado por 0 da 0"), ("grupos iguales", "grupos con la misma cantidad cada uno"), ("cero", "número que significa que no hay nada")],
    worked=[
        W("Grupos vacíos", "Hay 5 platos con 0 galletas en cada uno. ¿Cuántas galletas hay?", ["Son 5 grupos de 0 galletas: 5 × 0.", "Sumo 0 cinco veces: 0 + 0 + 0 + 0 + 0 = 0."], "0 galletas"),
        W("Cero grupos", "Una caja tiene 0 bolsas con 6 caramelos cada una. ¿Cuántos caramelos hay?", ["Son 0 grupos de 6: 0 × 6.", "Si no hay ninguna bolsa, no hay ningún caramelo."], "0 caramelos"),
    ],
    mistakes=[
        M("Calcular 7 × 0 = 7.", "Se confunde multiplicar por 0 con sumar 0.", "7 + 0 = 7, pero 7 × 0 son 7 grupos de nada: 0."),
        M("Decir que 0 × 9 no se puede calcular.", "Se cree que 0 no sirve para multiplicar.", "0 × 9 son 0 grupos de 9: 0."),
    ],
    rec=[
        ex("Calcula 5 × 0.", "0", "Son 5 grupos de 0: 0 + 0 + 0 + 0 + 0 = 0."),
        ex("Calcula 0 × 8.", "0", "Son 0 grupos de 8: no hay nada."),
        ex("¿Cuánto es 9 × 0?", "0", "Cualquier número multiplicado por 0 da 0."),
    ],
    und=[
        ex("Hay 6 vasos con 0 jugos. ¿Cuántos jugos hay? Escribe la multiplicación.", "0 jugos; 6 × 0 = 0", "6 grupos de 0 es 0."),
        ex("¿Qué es mayor: 8 + 0 o 8 × 0?", "8 + 0", "8 + 0 = 8 y 8 × 0 = 0."),
        ex("¿Qué producto da siempre 0 sin importar el otro factor?", "Multiplicar por 0", "Todo número multiplicado por 0 da 0."),
    ],
    app=[
        arith("Calcula 125 × 0.", "125*0", "Propiedad del cero: el producto es 0."),
        arith("Una bodega tiene 8 estantes y 0 cajas en cada uno. ¿Cuántas cajas hay?", "8*0", "8 estantes con 0 cajas cada uno dan 0 cajas."),
        arith("Calcula 0 × 4.857.", "0*4857", "El producto con un factor 0 es 0."),
    ],
    rea=[
        ex("Camila dice: «9 × 0 es 9 porque es el mismo número». ¿Tiene razón? Explica con grupos.", "No, es 0", "9 grupos de 0 elementos no tienen elementos."),
        ex("Una vecina dice que 0 grupos de 12 galletas son 12 galletas. ¿Es correcto?", "No, son 0 galletas", "Si no hay grupos, no hay galletas."),
    ],
    cha=[
        ex("Si 3 × __ = 0, ¿qué número va en el espacio?", "0", "Solo 0 hace que el producto sea 0 cuando el otro factor es 3."),
        ex("Calcula 5 × 4 × 0 × 7.", "0", "Hay un factor 0; el producto total es 0."),
    ],
    ctx=[ex("En un juego de bolos, Ana hizo 6 lanzamientos y en cada uno tiró 0 bolos. ¿Cuántos bolos tiró en total?", "0 bolos", "6 × 0 = 0.")],
    sc=[
        ex("Calcula 0 × 17.", "0", "0 grupos de 17 son 0."),
        ex("Calcula 3 × 0.", "0", "3 grupos de 0 son 0."),
        ex("¿Cuánto es 8 + 0?", "8", "Sumar 0 no cambia el número, a diferencia de multiplicar por 0."),
    ],
    op=task(
        "Dibuja 4 platos sin ninguna galleta y escribe la multiplicación y su producto. Luego dibuja 0 platos con 5 galletas cada uno y escribe la multiplicación. Explica con una frase por qué ambos productos son 0.",
        "4 platos con 0 galletas: 4 × 0 = 0. 0 platos con 5 galletas: 0 × 5 = 0. En el primero hay platos pero están vacíos; en el segundo no hay platos. En los dos no hay galletas.",
        ["dibuja bien las dos situaciones", "escribe las multiplicaciones", "explica con sus palabras"],
        ["dibujo en el cuaderno", "multiplicaciones escritas", "frase de explicación"],
        ["confundir × 0 con + 0", "decir que 0 grupos dan 5"],
        "Reconoce el dibujo y pide que cuente cuántas galletas hay en total para confirmar el 0.",
    ),
    reinforce="Escribe cinco multiplicaciones por 0 con números distintos y calcula cada producto.",
    extend="Explica por qué 1.000 × 0 = 0 usando grupos. ¿Cambia el resultado si el número es muy grande?",
)

lesson(
    OA4, 2,
    use="Aprenderé qué pasa cuando multiplico un número por uno. Sirve para resolver multiplicaciones rápido y entender el uno como elemento neutro.",
    prior=["Sé que multiplicar es repetir un número.", "Sé que cualquier número por 0 da 0."],
    explain=[
        "Si multiplicas un número por 1, el resultado es el mismo número. 1 × 7 son 1 grupo de 7: es 7. 7 × 1 son 7 grupos de 1: 1 + 1 + 1 + 1 + 1 + 1 + 1 = 7. Se llama propiedad del 1: todo número multiplicado por 1 da el mismo número.",
        "Por eso el 1 es el elemento neutro de la multiplicación: no cambia al otro número. Algo parecido ocurre con el 0 en la suma: 8 + 0 = 8. Pero no confundas: en la suma el neutro es 0; en la multiplicación es 1.",
        "Esta propiedad sirve con números grandes: 1.250 × 1 = 1.250 sin hacer ninguna cuenta. También sirve para comprobar: si un producto por 1 no da el mismo número, hay un error. Distingue bien: × 1 conserva el número, × 0 lo transforma en 0.",
    ],
    vocab=[("propiedad del 1", "todo número multiplicado por 1 da el mismo número"), ("elemento neutro", "número que no cambia a otro al operar con él"), ("producto", "resultado de multiplicar"), ("factor", "cada número que se multiplica"), ("conservar", "mantener igual")],
    worked=[
        W("Grupos de uno", "Hay 6 platos con 1 galleta cada uno. ¿Cuántas galletas hay?", ["6 grupos de 1: 6 × 1.", "1 + 1 + 1 + 1 + 1 + 1 = 6."], "6 galletas"),
        W("Un solo grupo", "Hay 1 caja con 9 lápices. ¿Cuántos lápices hay?", ["Es 1 grupo de 9: 1 × 9.", "Un solo grupo de 9 son 9."], "9 lápices"),
    ],
    mistakes=[
        M("Calcular 7 × 1 = 8.", "Se confunde multiplicar por 1 con sumar 1.", "7 × 1 son 7 grupos de 1: da 7. Sumar 1 sería 7 + 1."),
        M("Decir que 5 × 1 = 0.", "Se aplica la propiedad del 0 al 1.", "El 1 conserva el número: 5 × 1 = 5."),
    ],
    rec=[
        ex("Calcula 7 × 1.", "7", "7 grupos de 1 son 7."),
        ex("Calcula 1 × 12.", "12", "1 grupo de 12 es 12."),
        ex("¿Cuánto es 9 × 1?", "9", "Todo número por 1 da el mismo número."),
    ],
    und=[
        ex("¿Cuál es el elemento neutro de la multiplicación: el 0 o el 1?", "El 1", "Multiplicar por 1 no cambia el número."),
        ex("¿Por qué 6 × 1 = 6? Explica con grupos.", "6 grupos de 1 son 6", "1 + 1 + 1 + 1 + 1 + 1 = 6."),
        ex("¿Cuál es el elemento neutro de la suma?", "El 0", "8 + 0 = 8: sumar 0 no cambia el número."),
    ],
    app=[
        arith("Calcula 1.250 × 1.", "1250*1", "Todo número multiplicado por 1 da el mismo número."),
        arith("En una caja hay 1 bolsa con 24 pelotas. ¿Cuántas pelotas hay?", "1*24", "1 grupo de 24 es 24."),
        arith("Una clase tiene 15 puestos con 1 estudiante cada uno. ¿Cuántos estudiantes hay?", "15*1", "15 grupos de 1 son 15."),
    ],
    rea=[
        ex("Ema dice que 8 × 1 es 9 porque «uno más». ¿Está bien?", "No, es 8", "× 1 conserva el número; no suma 1."),
        ex("Si 346 × __ = 346, ¿qué número va en el espacio?", "1", "Solo el 1 conserva el número al multiplicar."),
    ],
    cha=[
        ex("Calcula 1 × 1 × 1 × 25.", "25", "Multiplicar por 1 varias veces no cambia el número."),
        ex("¿Qué es mayor: 9 × 1 o 9 + 1?", "9 + 1", "9 × 1 = 9 y 9 + 1 = 10."),
    ],
    ctx=[ex("Marta pone 1 manzana en cada una de sus 18 bolsas. ¿Cuántas manzanas usa en total?", "18 manzanas", "18 × 1 = 18.")],
    sc=[
        ex("Calcula 1 × 100.", "100", "1 grupo de 100 es 100."),
        ex("Calcula 25 × 1.", "25", "25 grupos de 1 son 25."),
        ex("Calcula 0 × 25.", "0", "Aquí el factor 0 transforma el producto en 0; no confundas con × 1."),
    ],
    op=task(
        "Dibuja 5 cajas con 1 pelota cada una y escribe su multiplicación. Luego dibuja 1 caja con 5 pelotas y escribe su multiplicación. Explica por qué en ambos el producto es 5 y qué pasaría si fueran 0 pelotas.",
        "5 cajas con 1 pelota: 5 × 1 = 5. 1 caja con 5 pelotas: 1 × 5 = 5. En los dos hay 5 pelotas. Con 0 pelotas serían 5 × 0 = 0 y 0 × 5 = 0.",
        ["dibuja bien", "escribe las multiplicaciones", "explica con grupos", "contrasta con el 0"],
        ["dibujos", "multiplicaciones y explicación escrita"],
        ["confundir × 1 con + 1", "decir que × 1 da 0"],
        "Reconoce la comparación entre 1 y 0 y pide un ejemplo con números grandes para generalizar.",
    ),
    reinforce="Completa: 3 × 1, 1 × 14, 20 × 1 y 1 × 99 y explica qué notas.",
    extend="Explica con tus palabras por qué el 1 se llama «neutro» en la multiplicación y el 0 «neutro» en la suma.",
)

lesson(
    OA4, 3,
    use="Aprenderé la propiedad del 1 en la división: dividir por 1 da el mismo número. Sirve para saber rápido cuánto toca a cada uno cuando se reparte en 1 grupo.",
    prior=["Sé que dividir es repartir en partes iguales.", "Sé que multiplicar por 1 deja el número igual."],
    explain=[
        "Dividir es repartir en grupos iguales. Si repartes 8 manzanas en 1 canasto, queda todo en el mismo canasto: 8 ÷ 1 = 8. Esta es la propiedad del 1 para la división: todo número dividido por 1 da el mismo número.",
        "Se explica con la multiplicación relacionada. Como 8 × 1 = 8, entonces 8 ÷ 1 = 8. El cociente es el resultado de la división; aquí es igual al dividendo, que es el número que se reparte. El divisor es 1, el número de grupos.",
        "Ten cuidado de no confundir dos ideas. Dividir por 1 deja el número igual. Dividir un número entre sí mismo también tiene un resultado fijo: 8 ÷ 8 = 1, porque cada uno recibe 1. Son dos hechos distintos y los dos son verdaderos.",
    ],
    vocab=[("dividendo", "número que se reparte"), ("divisor", "número entre el que se reparte"), ("cociente", "resultado de una división"), ("propiedad del 1 en la división", "todo número dividido por 1 da el mismo número"), ("repartir", "dividir en partes iguales")],
    worked=[
        W("Repartir en un grupo", "Repartes 12 galletas en 1 plato. ¿Cuántas galletas hay en el plato?", ["Se reparte entre 1 plato: 12 ÷ 1.", "Todo queda en ese plato: 12 galletas.", "Compruebo con la multiplicación: 12 × 1 = 12."], "12 galletas"),
        W("Dividir entre sí mismo", "Repartes 5 caramelos entre 5 amigos en partes iguales. ¿Cuántos recibe cada uno?", ["5 ÷ 5: cada amigo recibe lo mismo.", "Con 1 caramelo cada uno se reparten los 5.", "Compruebo: 5 × 1 = 5."], "1 caramelo"),
    ],
    mistakes=[
        M("Decir que 9 ÷ 1 = 1.", "Se confunde con dividir un número entre sí mismo.", "9 ÷ 1 = 9, porque todo queda en un solo grupo. Lo que da 1 es 9 ÷ 9."),
        M("Decir que 8 ÷ 1 = 0.", "Se aplica la propiedad del cero.", "Si hay 1 grupo, el grupo conserva todo: 8."),
    ],
    rec=[
        ex("Calcula 8 ÷ 1.", "8", "Un solo grupo recibe todo."),
        ex("Calcula 15 ÷ 1.", "15", "Todo número dividido por 1 da el mismo número."),
        ex("Calcula 100 ÷ 1.", "100", "Un grupo con todo: 100."),
    ],
    und=[
        ex("Repartes 20 lápices en 1 estuche. ¿Cuántos lápices tiene el estuche?", "20", "Es 20 ÷ 1 = 20."),
        ex("Si 8 × 1 = 8, ¿qué división con divisor 1 lo muestra?", "8 ÷ 1 = 8", "La división relacionada deshace la multiplicación."),
        ex("En 14 ÷ 1 = 14, ¿cuál es el divisor?", "1", "El divisor es el número entre el que se reparte."),
    ],
    app=[
        arith("Calcula 345 ÷ 1.", "345//1", "Todo número dividido por 1 da el mismo número."),
        arith("Una panadería pone 36 panes en 1 canasto. ¿Cuántos panes hay en el canasto?", "36//1", "Un solo grupo recibe todo."),
        arith("Repartes 1.000 pesos entre 1 persona. ¿Cuánto recibe?", "1000//1", "Dividir por 1 deja el número."),
    ],
    rea=[
        ex("Tomás dice: «Si divido 6 entre 1, cada parte es más pequeña». ¿Tiene razón?", "No", "6 ÷ 1 = 6: el grupo conserva todo."),
        ex("Nina dice que 7 ÷ 7 = 7 y Omar dice que 7 ÷ 7 = 1. ¿Quién tiene razón?", "Omar", "Al repartir 7 entre 7, cada uno recibe 1."),
    ],
    cha=[
        ex("Escribe el número que falta: __ ÷ 1 = 47.", "47", "Dividir por 1 da el mismo número."),
        ex("¿Cuánto es (6 × 1) ÷ 1?", "6", "6 × 1 = 6 y 6 ÷ 1 = 6."),
    ],
    ctx=[ex("En una fiesta hay 24 globos y se reparten en 1 bolsa. ¿Cuántos globos hay en la bolsa?", "24 globos", "24 ÷ 1 = 24.")],
    sc=[
        ex("Calcula 50 ÷ 1.", "50", "Un solo grupo recibe los 50."),
        ex("Calcula 9 ÷ 9.", "1", "Cada uno recibe 1."),
        ex("Si 12 × 1 = 12, ¿cuánto es 12 ÷ 1?", "12", "La división relacionada da el mismo número."),
    ],
    op=task(
        "Dibuja 9 galletas repartidas en 1 plato y escribe su división. Luego dibuja 9 galletas repartidas entre 9 platos y escribe su división. Explica qué es distinto en las dos divisiones.",
        "9 galletas en 1 plato: 9 ÷ 1 = 9. 9 galletas en 9 platos: 9 ÷ 9 = 1. En la primera hay un solo grupo y queda todo en él; en la segunda hay 9 grupos y cada uno recibe 1.",
        ["dibuja las dos situaciones", "escribe las divisiones y sus cocientes", "explica la diferencia"],
        ["dibujos", "divisiones y explicación escrita"],
        ["confundir ÷ 1 con ÷ el mismo número", "decir que 9 ÷ 1 = 1"],
        "Pide que compruebe cada división con su multiplicación para ver por qué los resultados difieren.",
    ),
    reinforce="Escribe tres divisiones por 1 con números distintos y comprueba cada una con su multiplicación.",
    extend="Explica con tus palabras por qué dividir por 1 y multiplicar por 1 dejan el número igual.",
)

lesson(
    OA4, 4,
    use="Aprenderé a distinguir cuándo usar la propiedad del 0 y la del 1, y por qué no se puede dividir por 0. Sirve para no confundirme en multiplicaciones y divisiones.",
    prior=["Sé que × 0 da 0 y × 1 deja el número igual.", "Sé que ÷ 1 deja el número igual."],
    explain=[
        "Resumamos. Multiplicar por 0 da 0: 8 × 0 = 0. Multiplicar por 1 da el mismo número: 8 × 1 = 8. Dividir por 1 da el mismo número: 8 ÷ 1 = 8. Antes de calcular, mira si hay un 0 o un 1 entre los factores: puedes ahorrar mucho cálculo.",
        "También existe 0 ÷ 8 = 0: repartir nada entre 8 personas deja 0 para cada una. Pero lo contrario no se puede: 8 ÷ 0 no tiene respuesta. No se puede repartir 8 en 0 grupos, porque no hay a quién darle.",
        "Si intentas comprobar 8 ÷ 0 con la multiplicación, no hay ningún número que multiplicado por 0 dé 8, porque cualquier número por 0 da 0. Por eso se dice que dividir por 0 no se puede. Es un caso imposible, no un resultado de 0.",
    ],
    vocab=[("propiedad del 0", "todo número multiplicado por 0 da 0"), ("propiedad del 1", "multiplicar o dividir por 1 deja el número igual"), ("caso imposible", "operación que no tiene resultado"), ("división por cero", "dividir un número entre 0; no se puede"), ("cociente", "resultado de una división")],
    worked=[
        W("Elegir la propiedad", "Calcula 346 × 0, 346 × 1 y 346 ÷ 1.", ["346 × 0: factor 0, el producto es 0.", "346 × 1: factor 1, el producto es 346.", "346 ÷ 1: divisor 1, el cociente es 346."], "0, 346 y 346"),
        W("Un caso imposible", "¿Se puede calcular 8 ÷ 0? Explica.", ["Pregunto: ¿qué número por 0 da 8?", "Todo número por 0 da 0, nunca 8.", "No hay respuesta: no se puede."], "No se puede dividir por 0"),
    ],
    mistakes=[
        M("Decir que 8 ÷ 0 = 0.", "Se confunde con 0 ÷ 8 = 0.", "0 ÷ 8 = 0 porque 0 × 8 = 0. En 8 ÷ 0 ningún número por 0 da 8, por eso no se puede."),
        M("Decir que 8 × 1 = 0.", "Se aplica la propiedad del cero.", "× 1 deja el número igual: 8."),
    ],
    rec=[
        ex("Calcula 9 × 0.", "0", "Propiedad del 0."),
        ex("Calcula 9 × 1.", "9", "Propiedad del 1."),
        ex("Calcula 9 ÷ 1.", "9", "Propiedad del 1 en la división."),
    ],
    und=[
        ex("¿Se puede calcular 5 ÷ 0?", "No", "Ningún número multiplicado por 0 da 5."),
        ex("¿Cuánto es 0 ÷ 5?", "0", "Al repartir nada entre 5, a cada uno le toca 0."),
        ex("¿Qué propiedad usas para calcular 1.250 × 1: la del 0 o la del 1?", "La del 1", "× 1 deja el número igual."),
    ],
    app=[
        arith("Calcula 7.346 × 1.", "7346*1", "Propiedad del 1."),
        arith("Calcula 0 ÷ 12.", "0//12", "0 repartido en grupos da 0."),
        ex("Clasifica estas operaciones en «da 0», «da el mismo número» o «no se puede»: 6 × 0, 6 × 1, 6 ÷ 1, 6 ÷ 0.", "6 × 0 da 0; 6 × 1 y 6 ÷ 1 dan el mismo número; 6 ÷ 0 no se puede", "Se aplican las propiedades del 0 y del 1 y el caso imposible."),
    ],
    rea=[
        ex("Pía dice que 12 ÷ 0 = 12 «porque no se reparte». ¿Tiene razón?", "No", "No hay número que multiplicado por 0 dé 12; la división por 0 no se puede."),
        ex("Leo dice que 0 ÷ 9 = 9. Compruébalo con la multiplicación.", "No, es 0", "0 ÷ 9 = 0 porque 0 × 9 = 0."),
    ],
    cha=[
        ex("¿Cuánto es 25 × 1 × 0 × 3?", "0", "Hay un factor 0; el producto es 0."),
        ex("Si 1 persona recibe todos los dulces y son 30, ¿qué división y qué cociente representan eso?", "30 ÷ 1 = 30", "El divisor es 1 y el cociente es 30."),
    ],
    ctx=[ex("Una tienda tiene 0 cajas con 20 zapatos y otra tiene 20 cajas con 0 zapatos. ¿Cuántos zapatos hay entre las dos?", "0 zapatos", "0 × 20 = 0 y 20 × 0 = 0; 0 + 0 = 0.")],
    sc=[
        ex("Calcula 0 × 345.", "0", "Propiedad del 0."),
        ex("Calcula 1 × 345.", "345", "Propiedad del 1."),
        ex("¿Se puede calcular 345 ÷ 0?", "No", "Dividir por 0 no tiene respuesta."),
    ],
    op=task(
        "Explica a un compañero con ejemplos cuándo una operación da 0, cuándo da el mismo número y cuándo no se puede hacer. Usa las cuentas 15 × 0, 15 × 1, 15 ÷ 1, 0 ÷ 15 y 15 ÷ 0. Escribe el resultado de cada una y una frase de justificación.",
        "15 × 0 = 0 (propiedad del 0); 15 × 1 = 15 y 15 ÷ 1 = 15 (propiedad del 1); 0 ÷ 15 = 0 porque 0 repartido da 0; 15 ÷ 0 no se puede porque ningún número por 0 da 15.",
        ["resuelve bien las cinco", "justifica con la propiedad", "reconoce el caso imposible"],
        ["cinco resultados escritos", "frases de justificación"],
        ["decir que 15 ÷ 0 = 0", "decir que 15 × 1 = 1"],
        "Pide que compruebe cada división con su multiplicación para ver por qué 15 ÷ 0 no tiene resultado.",
    ),
    reinforce="Haz una tabla con tres columnas, «da 0», «da el mismo número» y «no se puede», y ubica 8 × 0, 8 × 1, 8 ÷ 1, 8 ÷ 0 y 0 ÷ 8.",
    extend="Busca una frase que explique por qué 0 ÷ 8 = 0 pero 8 ÷ 0 no se puede, usando la multiplicación.",
)
