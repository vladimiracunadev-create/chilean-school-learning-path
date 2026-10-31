"""Cuaderno del estudiante de 7.º básico Matemática: OA 11 (círculo, circunferencia y lugar geométrico)."""
from __future__ import annotations

from student_lessons import ex
from student_content_ma07_a import M, W, cx, lesson, task

OA11 = "MA07 OA 11"

# ------------------------------------------------------------------ OA 11 clase 1
lesson(
    OA11, 1,
    use="Aprenderé a distinguir círculo y circunferencia, y a relacionar radio y diámetro. Sirve para hablar con precisión de ruedas, monedas, mesas y relojes.",
    prior=["Sé qué es un segmento y cómo medirlo con regla.", "Sé multiplicar y dividir por 2."],
    explain=[
        "La circunferencia es la línea curva cerrada que forma el borde de una figura redonda. El círculo es toda la superficie, con el borde y el interior. Por eso se dibuja una circunferencia con un lápiz y se pinta un círculo. En ambos hay un punto especial, el centro, que está a la misma distancia de todos los puntos de la circunferencia.",
        "El radio es un segmento que va desde el centro hasta cualquier punto de la circunferencia. Todos los radios de un círculo miden lo mismo. El diámetro es un segmento que une dos puntos de la circunferencia pasando por el centro. Por eso el diámetro mide el doble que el radio: d = 2r, y el radio es la mitad del diámetro: r = d ÷ 2.",
        "Una cuerda es cualquier segmento que une dos puntos de la circunferencia. El diámetro es la cuerda más larga, porque pasa por el centro. Ningún segmento dentro de un círculo puede ser más largo que el diámetro. Para medir un radio, mide desde el centro hasta el borde. Para medir un diámetro, mide de un borde a otro pasando por el centro.",
    ],
    vocab=[("circunferencia", "línea curva cerrada que forma el borde de una figura redonda"), ("círculo", "superficie limitada por una circunferencia, con su interior"), ("centro", "punto a igual distancia de todos los puntos de la circunferencia"), ("radio", "segmento que va del centro a la circunferencia"), ("diámetro", "segmento que une dos puntos de la circunferencia pasando por el centro")],
    worked=[
        W("Del radio al diámetro", "Un círculo tiene un radio de 7 cm. ¿Cuánto mide su diámetro?", ["El diámetro es el doble del radio.", "2 · 7 cm = 14 cm."], "14 cm"),
        W("Del diámetro al radio", "Un círculo tiene un diámetro de 18 cm. ¿Cuánto mide su radio?", ["El radio es la mitad del diámetro.", "18 cm ÷ 2 = 9 cm."], "9 cm"),
    ],
    mistakes=[
        M("Decir que el diámetro es la mitad del radio.", "Se invirtió la relación.", "El diámetro es el doble del radio: d = 2r."),
        M("Llamar «círculo» al borde de una moneda.", "Se confundió la línea con la superficie.", "El borde es la circunferencia; el círculo incluye el interior."),
    ],
    rec=[
        ex("Un círculo tiene radio de 6 cm. ¿Cuánto mide su diámetro?", "12 cm", "2 · 6."),
        ex("Un círculo tiene diámetro de 20 cm. ¿Cuánto mide su radio?", "10 cm", "20 ÷ 2."),
        ex("El borde de una moneda, ¿es un círculo o una circunferencia?", "Una circunferencia", "El borde es la línea; el círculo incluye el interior."),
    ],
    und=[
        ex("Un círculo tiene radio de 3,5 cm. ¿Cuánto mide su diámetro?", "7 cm", "2 · 3,5."),
        ex("¿Cuántos radios caben en un diámetro?", "2", "El diámetro es el doble del radio."),
        ex("¿Cuántos centros tiene un círculo?", "1", "Hay un solo punto a igual distancia de todo el borde."),
    ],
    app=[
        ex("Una mesa redonda de ejemplo mide 120 cm de diámetro. ¿Cuánto mide su radio?", "60 cm", "120 ÷ 2."),
        ex("La moneda A tiene un radio de 12 mm y la moneda B tiene un diámetro de 25 mm. ¿Cuál es más grande?", "La B", "A tiene diámetro 24 mm y B tiene 25 mm."),
        ex("Un reloj redondo de pared de ejemplo mide 30 cm de diámetro. ¿Cuál es el ancho mínimo de una caja cuadrada en que cabe?", "30 cm", "La caja debe ser al menos tan ancha como el diámetro."),
    ],
    rea=[
        ex("Ana dice que el diámetro es la mitad del radio. ¿Tiene razón?", "No", "El diámetro es el doble del radio."),
        ex("¿Puede una cuerda de un círculo medir más que el diámetro? Responde sí o no.", "No", "El diámetro es la cuerda más larga."),
    ],
    cha=[
        ex("Un círculo tiene un diámetro que mide 3 cm más que su radio. ¿Cuánto mide el radio?", "3 cm", "2r = r + 3 da r = 3."),
        ex("Dos circunferencias con el mismo centro tienen radios de 4 cm y 9 cm. ¿Cuánto mide el ancho del anillo entre ellas?", "5 cm", "9 − 4 = 5."),
    ],
    ctx=[ex("Una pizza de ejemplo tiene 36 cm de diámetro. Se sirven porciones que parten del centro hasta el borde. ¿Cuánto mide el largo de cada corte desde el centro?", "18 cm", "Es el radio: 36 ÷ 2.")],
    sc=[
        ex("Si el radio mide 9 cm, ¿cuánto mide el diámetro?", "18 cm", "2 · 9."),
        ex("Si el diámetro mide 50 cm, ¿cuánto mide el radio?", "25 cm", "50 ÷ 2."),
        ex("¿Cuál es la cuerda más larga de un círculo?", "El diámetro", "Pasa por el centro."),
    ],
    op=task(
        "Busca tres objetos redondos de tu casa, como una tapa, un plato y un vaso. Para cada uno mide con regla el diámetro en centímetros (de un borde a otro, pasando por el centro, que puedes estimar doblando un papel por la mitad). Escribe en una tabla el diámetro y el radio de cada uno. Si no tienes objetos redondos, usa estos datos de ejemplo: tapa 7 cm de diámetro, plato 24 cm, vaso 8 cm. Explica con una frase cómo supiste el radio.",
        "Datos de ejemplo: tapa d = 7 cm y r = 3,5 cm; plato d = 24 cm y r = 12 cm; vaso d = 8 cm y r = 4 cm. El radio es la mitad del diámetro, por eso se divide por 2.",
        ["mide o usa los datos de cada objeto", "calcula el radio como la mitad del diámetro", "explica la relación d = 2r"],
        ["tabla con tres objetos", "frase de explicación"],
        ["medir sin pasar por el centro", "duplicar en vez de dividir al calcular el radio"],
        "Pide que mida el diámetro dos veces desde posiciones distintas y compare.",
    ),
    reinforce="Completa: radio 5 cm, diámetro ___; diámetro 16 cm, radio ___; radio 2,5 cm, diámetro ___.",
    extend="Explica con un dibujo por qué ninguna cuerda puede ser más larga que el diámetro.",
)

# ------------------------------------------------------------------ OA 11 clase 2
lesson(
    OA11, 2,
    use="Aprenderé a descubrir cuántas veces cabe el diámetro en el perímetro de una circunferencia. Sirve para calcular el largo del borde de objetos redondos, como ruedas y mesas.",
    prior=["Sé la relación entre radio y diámetro.", "Sé multiplicar y dividir números decimales."],
    explain=[
        "El perímetro de una circunferencia es el largo de su borde, como si lo estiraras. Se puede medir con un hilo y una regla. Si mides el perímetro C y el diámetro d de varios objetos redondos y divides C ÷ d, el resultado siempre es cercano a 3,14, sin importar el tamaño. Ese número constante se llama pi y se escribe con la letra griega π.",
        "El valor de π tiene decimales que no terminan y no se repiten; para cálculos usamos la aproximación 3,14. Así, el perímetro de la circunferencia es C = π · d, o con el radio, C = 2 · π · r. Por ejemplo, para d = 10 cm: C ≈ 3,14 · 10 = 31,4 cm. Al medir en la vida real el cociente varía un poco, como 3,13 o 3,16, por los errores de medición.",
        "Como C = 3,14 · d, si el diámetro se duplica, el perímetro también se duplica: son proporcionales. El perímetro de una circunferencia es un poco más que 3 diámetros. Si conoces C y quieres d, divide: d = C ÷ 3,14. Escribe siempre la unidad, por ejemplo, centímetros.",
    ],
    vocab=[("perímetro de la circunferencia", "largo de su borde"), ("pi (π)", "número que resulta de dividir el perímetro entre el diámetro; vale casi 3,14"), ("aproximación", "valor cercano pero no exacto"), ("razón", "comparación de dos cantidades mediante una división"), ("error de medición", "pequeña diferencia por medir con instrumentos")],
    worked=[
        W("Descubrir pi con datos", "Medidas de ejemplo: tapa con d = 6 cm y C = 18,8 cm; plato con d = 20 cm y C = 62,8 cm. Calcula C ÷ d.", ["Tapa: 18,8 ÷ 6 ≈ 3,13.", "Plato: 62,8 ÷ 20 = 3,14."], "Ambos cercanos a 3,14"),
        W("Calcular el perímetro", "Calcula el perímetro de una circunferencia de diámetro 10 cm.", ["C = π · d ≈ 3,14 · 10.", "3,14 · 10 = 31,4."], "31,4 cm"),
    ],
    mistakes=[
        M("Calcular el perímetro de una circunferencia de radio 6 cm como 3,14 · 6.", "Se usó el radio donde se necesitaba el diámetro.", "C = 3,14 · 12 = 37,68 cm, porque el diámetro es 12 cm."),
        M("Creer que pi vale exactamente 3,14.", "Se confundió la aproximación con el valor.", "π tiene infinitos decimales; 3,14 es una aproximación."),
    ],
    rec=[
        ex("Al dividir el perímetro de una circunferencia entre su diámetro, ¿qué número se obtiene aproximadamente?", "3,14", "Ese número es π."),
        cx("Calcula el perímetro de una circunferencia de diámetro 25 cm usando π ≈ 3,14.", "F('3.14')*25", "C = 3,14 · 25 = 78,5.", unit=" cm", form="dec"),
        cx("Calcula el perímetro de una circunferencia de radio 4 cm. (Primero halla el diámetro.)", "F('3.14')*8", "d = 8 cm y C = 3,14 · 8.", unit=" cm", form="dec"),
    ],
    und=[
        cx("Calcula el perímetro de una circunferencia de diámetro 7 cm.", "F('3.14')*7", "3,14 · 7 = 21,98.", unit=" cm", form="dec"),
        cx("Un objeto redondo de ejemplo tiene C = 56,52 cm y d = 18 cm. ¿Cuánto vale C ÷ d?", "F('56.52')/18", "56,52 ÷ 18 = 3,14.", form="dec"),
        cx("Calcula el perímetro de una circunferencia de radio 12 cm.", "F('3.14')*24", "d = 24 cm y C = 3,14 · 24 = 75,36.", unit=" cm", form="dec"),
    ],
    app=[
        cx("Una rueda de bicicleta de ejemplo tiene 60 cm de diámetro. ¿Cuántos cm mide su borde?", "F('3.14')*60", "3,14 · 60 = 188,4.", unit=" cm", form="dec"),
        cx("Un anillo de ejemplo tiene 2 cm de diámetro. ¿Cuánto mide su borde?", "F('3.14')*2", "3,14 · 2 = 6,28.", unit=" cm", form="dec"),
        cx("El borde de una tapa de ejemplo mide 157 cm. ¿Cuál es su diámetro?", "F(157)/F('3.14')", "157 ÷ 3,14 = 50.", unit=" cm"),
    ],
    rea=[
        ex("Pablo midió una tapa y calculó C ÷ d = 2. ¿Es razonable ese resultado?", "No", "Debería ser cercano a 3,14; probablemente midió mal."),
        ex("Si el diámetro de una circunferencia se duplica, ¿qué pasa con su perímetro?", "Se duplica", "C = 3,14 · d es proporcional al diámetro."),
    ],
    cha=[
        cx("Un hilo de 251,2 cm rodea exactamente el borde de un círculo. ¿Cuál es su diámetro?", "F('251.2')/F('3.14')", "251,2 ÷ 3,14 = 80.", unit=" cm"),
        ex("Una rueda tiene 40 cm de diámetro y otra tiene 80 cm. ¿Cuántas veces mayor es el perímetro de la segunda?", "2", "El perímetro es proporcional al diámetro."),
    ],
    ctx=[cx("Se quiere pegar una cinta decorativa en el borde de una mesa redonda de ejemplo de 100 cm de diámetro. ¿Cuántos cm de cinta se necesitan, como mínimo?", "F('3.14')*100", "3,14 · 100 = 314.", unit=" cm")],
    sc=[
        cx("Calcula el perímetro de una circunferencia de 40 cm de diámetro.", "F('3.14')*40", "3,14 · 40 = 125,6.", unit=" cm", form="dec"),
        ex("¿Cuál es el valor aproximado de π que se usa en este cuaderno?", "3,14", "Es una aproximación con dos decimales."),
        ex("Si el perímetro es C y el diámetro es d, ¿cómo se calcula d?", "d = C ÷ 3,14", "Se divide el perímetro entre π."),
    ],
    op=task(
        "Esta es una tabla de ejemplo con tres objetos redondos medidos con hilo: tapa de frasco, d = 5 cm y C = 15,7 cm; plato de postre, d = 15 cm y C = 47,1 cm; fuente grande, d = 30 cm y C = 94,2 cm. (a) Calcula C ÷ d para cada objeto. (b) Escribe qué número obtienes y cómo se llama. (c) Si puedes, mide un objeto redondo de tu casa con un hilo y una regla y repite el cálculo. (d) Calcula el perímetro de una circunferencia de 12 cm de diámetro.",
        "(a) 15,7 ÷ 5 = 3,14; 47,1 ÷ 15 = 3,14; 94,2 ÷ 30 = 3,14. (b) Se obtiene 3,14, que es el valor aproximado de π. (d) 3,14 · 12 = 37,68 cm.",
        ["calcula los tres cocientes", "identifica el número como π", "usa C = π · d"],
        ["tres divisiones", "frase de conclusión", "cálculo de C"],
        ["usar el radio en lugar del diámetro", "redondear sin decir que es aproximación"],
        "Pide que compare sus cocientes con los de otra persona; si varían un poco, que explique por qué.",
    ),
    reinforce="Calcula el perímetro de circunferencias de diámetro 5 cm, 10 cm y 15 cm. ¿Qué observas?",
    extend="Explica por qué los perímetros del ejercicio de reforzamiento forman una proporcionalidad directa con los diámetros.",
)

# ------------------------------------------------------------------ OA 11 clase 3
lesson(
    OA11, 3,
    use="Aprenderé a estimar de manera intuitiva el perímetro y el área de un círculo y a mejorar la estimación. Sirve para saber rápido si un resultado tiene sentido.",
    prior=["Sé que el perímetro de la circunferencia es casi 3 veces el diámetro.", "Sé calcular el área de cuadrados."],
    explain=[
        "Para estimar el perímetro, usa que la circunferencia mide un poco más que 3 diámetros: C ≈ 3 · d. Si el diámetro mide 10 cm, el perímetro es cerca de 30 cm. La estimación queda un poco corta, porque 3 es menor que 3,14, pero sirve para controlar un cálculo hecho con 3,14.",
        "Para estimar el área, compara el círculo con cuadrados. Un cuadrado de lado r (el radio) tiene área r². El círculo cabe dentro de un cuadrado de lado 2r, que tiene área 4r², y contiene un cuadrado de área 2r². Entonces el área del círculo está entre 2r² y 4r², y un valor intuitivo es cerca de 3r². Por ejemplo, con r = 10 cm: A ≈ 3 · 100 = 300 cm².",
        "Para una cifra más precisa, usa A ≈ 3,14 · r². Con r = 10 cm: 3,14 · 100 = 314 cm². También se puede estimar contando cuadritos de una cuadrícula: cuenta los cuadritos completos dentro del círculo y suma la mitad de los que quedan partidos por el borde. Recuerda que el área se mide en unidades cuadradas, como cm².",
    ],
    vocab=[("estimar", "calcular de forma aproximada con números fáciles"), ("área", "medida de la superficie; se expresa en unidades cuadradas"), ("r²", "r · r; el área de un cuadrado de lado r"), ("cm²", "centímetro cuadrado, unidad de área"), ("cuadrícula", "red de cuadrados iguales usada para medir áreas")],
    worked=[
        W("Estimar el perímetro", "Estima el perímetro de un círculo de 20 cm de diámetro con 3 · d y compáralo con 3,14 · d.", ["Estimación: 3 · 20 = 60 cm.", "Con 3,14: 3,14 · 20 = 62,8 cm. Están cerca."], "Cerca de 60 cm; 62,8 cm con 3,14"),
        W("Estimar el área", "Estima el área de un círculo de radio 10 cm con 3 · r² y con 3,14 · r².", ["Con 3: 3 · 100 = 300 cm².", "Con 3,14: 3,14 · 100 = 314 cm²."], "300 cm² y 314 cm²"),
    ],
    mistakes=[
        M("Estimar el área de un círculo de diámetro 10 cm como 3 · 10².", "Se usó el diámetro en lugar del radio.", "El radio es 5 cm: 3 · 5² = 75 cm²."),
        M("Escribir el área en cm en vez de cm².", "Se confundió longitud con superficie.", "El área se expresa en unidades cuadradas: cm²."),
    ],
    rec=[
        ex("Estima el perímetro de un círculo de 10 cm de diámetro usando 3 · d.", "30 cm", "3 · 10."),
        ex("Si el radio es 2, ¿cuánto vale 3 · r²?", "12", "r² = 4 y 3 · 4 = 12."),
        ex("¿Cuánto vale r² si r = 6?", "36", "6 · 6."),
    ],
    und=[
        ex("Estima el área de un círculo de radio 5 cm usando 3 · r².", "75 cm²", "3 · 25."),
        ex("Estima con 3 · d el perímetro de un círculo de 40 cm de diámetro.", "120 cm", "3 · 40."),
        ex("El área de un círculo de radio 3 está entre 2r² y 4r². ¿Entre qué dos números está?", "Entre 18 y 36", "2 · 9 = 18 y 4 · 9 = 36."),
    ],
    app=[
        ex("Un patio circular de ejemplo tiene 4 m de radio. Estima su área con 3 · r².", "48 m²", "3 · 16."),
        ex("Un círculo de 2 m de diámetro se rodea con una cinta. Estima cuántos metros de cinta se necesitan con 3 · d.", "6 m", "3 · 2."),
        cx("Una alfombra redonda de ejemplo tiene 1 m de radio. ¿Cuántos m² tiene, usando 3,14 · r²?", "F('3.14')*1", "3,14 · 1 = 3,14.", unit=" m²", form="dec"),
    ],
    rea=[
        ex("Juan estimó el área de una pizza de 30 cm de diámetro como 3 · 30² = 2.700 cm². ¿Cuál es la estimación correcta con el radio?", "675 cm²", "El radio es 15 cm y 3 · 225 = 675."),
        ex("¿La estimación C ≈ 3 · d da un valor menor o mayor que el real?", "Menor", "El valor real usa 3,14, que es mayor que 3."),
    ],
    cha=[
        ex("Un círculo tiene un área estimada con 3 · r² de 108 cm². ¿Cuánto mide su radio?", "6 cm", "r² = 36 y r = 6."),
        cx("Calcula el área de un círculo de 14 cm de diámetro usando 3,14 · r².", "F('3.14')*49", "r = 7 y 3,14 · 49 = 153,86.", unit=" cm²", form="dec"),
    ],
    ctx=[ex("Una mesa redonda de ejemplo tiene 1 m de diámetro. Estima el área de su cubierta con 3 · r². (r = 0,5 m)", "0,75 m²", "r² = 0,25 y 3 · 0,25 = 0,75.")],
    sc=[
        ex("Estima el perímetro de un círculo de 50 cm de diámetro.", "150 cm", "3 · 50."),
        ex("Estima el área de un círculo de radio 8 cm con 3 · r².", "192 cm²", "3 · 64."),
        ex("¿Qué unidad usa el área: cm o cm²?", "cm²", "El área mide superficie."),
    ],
    op=task(
        "Dibuja en una hoja cuadriculada un círculo de 10 cuadritos de diámetro (radio de 5 cuadritos) con un compás o rodeando una tapa grande. (a) Cuenta los cuadritos completos dentro del círculo y suma la mitad de los partidos. (b) Compara con la estimación 3 · r² y con 3,14 · r². (c) Estima el perímetro con 3 · d. Si no puedes dibujar, usa estos datos de ejemplo: 60 cuadritos completos y 28 cuadritos partidos.",
        "Con los datos de ejemplo: 60 + 14 = 74 cuadritos. Estimación 3 · 25 = 75. Con 3,14: 3,14 · 25 = 78,5. El conteo da un valor cercano a ambos. Perímetro estimado: 3 · 10 = 30 cuadritos de largo.",
        ["cuenta cuadritos con criterio", "compara con ambas estimaciones", "estima el perímetro"],
        ["dibujo con cuadrícula", "cálculos", "frase de comparación"],
        ["contar los partidos como completos", "usar el diámetro en lugar del radio"],
        "Pide que repita el conteo y compare con 75 y con 78,5.",
    ),
    reinforce="Estima el perímetro y el área de un círculo de 6 cm de diámetro.",
    extend="Explica con un dibujo por qué el área de un círculo de radio r está entre 2r² y 4r².",
)

# ------------------------------------------------------------------ OA 11 clase 4
lesson(
    OA11, 4,
    use="Aprenderé a resolver problemas con perímetros y áreas de círculos, como las vueltas de una rueda o el tamaño de una pizza. Sirve para situaciones de la vida diaria y de otras asignaturas.",
    prior=["Sé que C ≈ 3,14 · d y A ≈ 3,14 · r².", "Sé multiplicar y dividir decimales."],
    explain=[
        "Con π ≈ 3,14 hay dos fórmulas que usaremos. Perímetro de la circunferencia: C = 3,14 · d = 2 · 3,14 · r. Área del círculo: A = 3,14 · r · r. Al resolver, anota primero si te dan el radio o el diámetro y pasa de uno a otro si hace falta. El perímetro es una longitud (cm, m) y el área es una superficie (cm², m²).",
        "Los problemas típicos son: cuánto avanza una rueda en una vuelta (su perímetro); cuántas vueltas da para recorrer una distancia (distancia ÷ perímetro); cuánta cinta rodea un círculo (perímetro); cuánta pintura o tela cubre un círculo (área); y cuánto más grande es un círculo que otro. Si el radio se duplica, el perímetro se duplica, pero el área se multiplica por 4, porque r se multiplica por sí mismo.",
        "Para un anillo (un círculo con otro más pequeño sacado del centro), el área es el área del círculo mayor menos la del menor. Siempre estima antes (con 3) y compara. Responde con la unidad y con una frase completa. Si el problema usa medidas de distintas unidades, conviértelas antes de calcular.",
    ],
    vocab=[("vuelta", "giro completo de una rueda"), ("anillo", "región entre dos circunferencias con el mismo centro"), ("superficie", "parte plana que cubre algo"), ("distancia recorrida", "largo del camino que avanza algo"), ("rendimiento", "cuánta superficie cubre una cantidad de material")],
    worked=[
        W("Vueltas de una rueda", "Una rueda de ejemplo tiene 60 cm de diámetro. ¿Cuántos cm avanza en una vuelta?", ["Avanza lo que mide su borde: 3,14 · 60.", "3,14 · 60 = 188,4."], "188,4 cm"),
        W("Área de un círculo", "Calcula el área de una mesa redonda de ejemplo de radio 50 cm.", ["Mesa: A = 3,14 · 50 · 50 = 3,14 · 2.500.", "3,14 · 2.500 = 7.850."], "7.850 cm²"),
    ],
    mistakes=[
        M("Duplicar el radio y creer que el área también se duplica.", "Se razonó con una proporcionalidad directa.", "Con r doble, el área es 4 veces mayor, porque r se multiplica por sí mismo."),
        M("Calcular el área de una mesa con el diámetro de 80 cm como 3,14 · 80 · 80.", "Se usó el diámetro en vez del radio.", "El radio es 40 cm: 3,14 · 40 · 40 = 5.024 cm²."),
    ],
    rec=[
        cx("Calcula el perímetro de una rueda de 50 cm de diámetro con π ≈ 3,14.", "F('3.14')*50", "3,14 · 50 = 157.", unit=" cm"),
        cx("Calcula el área de un círculo de radio 3 cm con π ≈ 3,14.", "F('3.14')*9", "3,14 · 3 · 3 = 28,26.", unit=" cm²", form="dec"),
        ex("Un círculo tiene radio de 7 cm. ¿Cuánto mide su diámetro?", "14 cm", "2 · 7."),
    ],
    und=[
        cx("Calcula el área de un círculo de radio 8 cm.", "F('3.14')*64", "3,14 · 8 · 8 = 200,96.", unit=" cm²", form="dec"),
        cx("Un círculo tiene radio de 15 cm. Calcula su perímetro con C = 2 · 3,14 · r.", "F('3.14')*30", "2 · 3,14 · 15 = 94,2.", unit=" cm", form="dec"),
        ex("Una rueda de ejemplo tiene un perímetro de 3,14 m y recorre 314 m. ¿Cuántas vueltas da?", "100", "314 ÷ 3,14 = 100."),
    ],
    app=[
        cx("Una rueda de bicicleta de ejemplo tiene 70 cm de diámetro. ¿Cuántos cm avanza en una vuelta?", "F('3.14')*70", "3,14 · 70 = 219,8.", unit=" cm", form="dec"),
        cx("Una pista circular de ejemplo tiene 50 m de radio. ¿Cuántos metros recorre una persona que da 3 vueltas?", "F('3.14')*100*3", "Una vuelta es 3,14 · 100 = 314 m; tres vueltas: 942 m.", unit=" m"),
        cx("Una pizza de ejemplo tiene 40 cm de diámetro. ¿Cuántos cm² tiene su superficie?", "F('3.14')*400", "r = 20 cm y 3,14 · 400 = 1.256.", unit=" cm²"),
    ],
    rea=[
        ex("Una pizza tiene 20 cm de diámetro y otra tiene 40 cm de diámetro. ¿El área de la segunda es el doble, el triple o el cuádruple de la primera?", "El cuádruple", "314 cm² y 1.256 cm²: 1.256 ÷ 314 = 4."),
        ex("Ema dice que una rueda de 2 m de diámetro da el doble de vueltas que una de 1 m de diámetro en el mismo recorrido. ¿Tiene razón?", "No", "La rueda grande tiene el doble de perímetro, así que da la mitad de vueltas."),
    ],
    cha=[
        cx("Un jardín circular de ejemplo tiene 10 m de diámetro y se rodea con un camino de 1 m de ancho. ¿Cuántos m² tiene el camino? (Área del círculo de radio 6 m menos la del de radio 5 m.)", "F('3.14')*(36-25)", "3,14 · 36 − 3,14 · 25 = 3,14 · 11.", unit=" m²", form="dec"),
        cx("Una rueda de ejemplo da 50 vueltas y avanza 94,2 m. ¿Cuántos metros mide su perímetro?", "F('94.2')/50", "94,2 ÷ 50 = 1,884.", unit=" m", form="dec"),
    ],
    ctx=[cx("Un posavasos circular de ejemplo tiene 9 cm de radio. ¿Cuántos cm² tiene su superficie?", "F('3.14')*81", "3,14 · 9 · 9 = 254,34.", unit=" cm²", form="dec")],
    sc=[
        cx("Calcula el área de un círculo de radio 2 cm.", "F('3.14')*4", "3,14 · 4 = 12,56.", unit=" cm²", form="dec"),
        cx("Calcula el perímetro de una circunferencia de radio 5 cm.", "F('3.14')*10", "2 · 3,14 · 5 = 31,4.", unit=" cm", form="dec"),
        ex("Si el radio de un círculo se duplica, ¿por cuánto se multiplica su área?", "4", "El radio se multiplica por 2 y el área por 2 · 2."),
    ],
    op=task(
        "Una familia de ejemplo decide cercar una piscina circular de 6 m de diámetro y poner una cubierta circular. (a) Calcula el perímetro, que es lo que mide la cerca. (b) Calcula el área de la cubierta. (c) Si la cubierta cuesta $2.000 por m², ¿cuánto cuesta cubrir la piscina? (d) Si la piscina midiera 12 m de diámetro, ¿cuántas veces mayor sería su área? Explica tu respuesta.",
        "(a) 3,14 · 6 = 18,84 m. (b) r = 3 m y A = 3,14 · 9 = 28,26 m². (c) 28,26 · 2.000 = 56.520 pesos. (d) 4 veces, porque el radio se duplica y el área se multiplica por 2 · 2.",
        ["usa las fórmulas correctas", "pasa de diámetro a radio", "interpreta la duplicación"],
        ["cuatro cálculos", "respuestas con unidad"],
        ["usar el diámetro en la fórmula del área", "olvidar que el área se mide en m²"],
        "Pide que estime con 3 antes de calcular y compare.",
    ),
    reinforce="Calcula el área de un círculo de 10 cm de radio y el perímetro de otro de 10 cm de diámetro.",
    extend="Calcula las áreas de pizzas de 30 cm y de 40 cm de diámetro y escribe, aproximadamente, cuántas veces mayor es la segunda.",
)

# ------------------------------------------------------------------ OA 11 clase 5
lesson(
    OA11, 5,
    use="Aprenderé que la circunferencia es el lugar geométrico de los puntos que están a una misma distancia de un centro, y a usar esta idea para resolver problemas. Sirve para ubicar lugares, trazar con compás y describir zonas de alcance.",
    prior=["Sé qué es el radio y el diámetro.", "Sé usar regla y compás o una cuerda para trazar."],
    explain=[
        "Un lugar geométrico es el conjunto de todos los puntos que cumplen una condición. La circunferencia es el lugar geométrico de todos los puntos del plano que están a una misma distancia, el radio, de un punto fijo llamado centro. Si un punto está a 5 cm del centro, y el radio es 5 cm, está sobre la circunferencia. Si está a menos de 5 cm, está dentro. Si está a más, está fuera.",
        "El círculo es el lugar geométrico de los puntos que están a una distancia menor o igual que el radio desde el centro. Para trazar una circunferencia con compás, abre el compás con la medida del radio, apoya la punta en el centro y gira. Sin compás puedes usar una cuerda: una persona sujeta un extremo en el centro y otra estira la cuerda y dibuja con un lápiz en el otro extremo.",
        "Con esta idea se resuelven problemas de alcance: la antena que llega a 10 km, el aspersor que moja 3 m a la redonda. También sirve para ubicar puntos con dos condiciones. Si un punto debe estar a 4 cm de A y a 4 cm de B, está en la intersección de dos circunferencias, el lugar donde se cruzan. Dos circunferencias pueden cruzarse en 2 puntos, tocarse en 1 punto o no tocarse.",
    ],
    vocab=[("lugar geométrico", "conjunto de todos los puntos que cumplen una condición"), ("compás", "instrumento para trazar circunferencias con una abertura fija"), ("a la redonda", "en todas las direcciones desde un punto"), ("intersección", "punto o puntos donde se cruzan dos figuras"), ("alcance", "distancia máxima hasta donde llega algo")],
    worked=[
        W("Puntos a una distancia", "Un punto P está a 3 cm del centro O de un círculo de radio 5 cm. ¿Está dentro, fuera o sobre la circunferencia?", ["La distancia al centro es 3 cm, menor que el radio 5 cm.", "Los puntos a menos de 5 cm están dentro del círculo."], "Dentro"),
        W("Zona de alcance", "Un aspersor de ejemplo moja 3 m a la redonda en un terreno plano. ¿Qué figura es la zona mojada y cuántos m² tiene aproximadamente?", ["La zona es un círculo de radio 3 m.", "Área ≈ 3,14 · 3 · 3 = 28,26."], "Un círculo de 28,26 m²"),
    ],
    mistakes=[
        M("Decir que los puntos a 5 cm de O forman un círculo relleno.", "Se confundió la línea con la superficie.", "Los puntos a exactamente 5 cm forman la circunferencia; el círculo incluye los puntos más cercanos."),
        M("Creer que dos circunferencias siempre se cruzan en 2 puntos.", "Se supuso un solo caso.", "Pueden cruzarse en 2 puntos, tocarse en 1 o no tocarse."),
    ],
    rec=[
        ex("Todos los puntos de una circunferencia, ¿a qué distancia están del centro?", "A la misma distancia, el radio", "Es la definición de circunferencia."),
        ex("Un círculo tiene radio 6 cm. Un punto está a 2 cm del centro. ¿Está dentro, fuera o sobre la circunferencia?", "Dentro", "2 cm es menos que 6 cm."),
        ex("Si el radio es 4 cm, ¿a qué abertura se fija el compás para trazar la circunferencia?", "4 cm", "La abertura del compás es el radio."),
    ],
    und=[
        ex("Un círculo tiene radio 7 cm y un punto está a 7 cm del centro. ¿Está dentro, fuera o sobre la circunferencia?", "Sobre la circunferencia", "La distancia es igual al radio."),
        ex("Un círculo tiene radio 7 cm y un punto está a 10 cm del centro. ¿Está dentro, fuera o sobre la circunferencia?", "Fuera", "10 cm es más que el radio."),
        ex("Para trazar con compás una circunferencia de diámetro 8 cm, ¿a qué abertura se fija el compás?", "4 cm", "El radio es 8 ÷ 2."),
    ],
    app=[
        ex("Una antena de ejemplo llega 10 km a la redonda. ¿Recibe señal un pueblo a 7 km? ¿Y uno a 12 km?", "Sí; no", "7 km es menor que 10 km y 12 km es mayor."),
        cx("Un perro está atado con una cuerda de 4 m a un poste, en un patio plano sin obstáculos. ¿Cuántos m² puede recorrer, aproximadamente?", "F('3.14')*16", "Es un círculo de radio 4 m: 3,14 · 16 = 50,24.", unit=" m²", form="dec"),
        ex("Un faro de ejemplo ilumina hasta 6 km a la redonda. ¿Cuál es el diámetro de la zona iluminada?", "12 km", "El diámetro es el doble del radio."),
    ],
    rea=[
        ex("Ana dice que los puntos que están exactamente a 5 cm de un punto O forman un círculo relleno. ¿Qué figura forman en realidad?", "Una circunferencia", "Solo la línea del borde; el interior está a menos de 5 cm."),
        ex("¿Está sobre la misma circunferencia con centro O un punto a 4 cm de O y otro a 6 cm de O? Responde sí o no.", "No", "Están a distancias distintas del centro."),
    ],
    cha=[
        ex("Los puntos A y B están a 6 cm uno del otro. ¿Cuántos puntos hay a 4 cm de A y a 4 cm de B a la vez?", "2", "Las dos circunferencias de radio 4 cm se cruzan en dos puntos."),
        ex("Los puntos A y B están a 8 cm uno del otro. ¿Cuántos puntos hay a 4 cm de A y a 4 cm de B a la vez?", "1", "Las circunferencias solo se tocan en el punto medio de A y B."),
    ],
    ctx=[ex("En un juego de ejemplo, un tesoro está a 5 pasos de una palmera. ¿Qué figura forman todos los lugares posibles del tesoro si el terreno es plano?", "Una circunferencia de 5 pasos de radio con centro en la palmera", "Es el lugar geométrico de los puntos a 5 pasos de la palmera.")],
    sc=[
        ex("¿Cuál es la definición de circunferencia como lugar geométrico?", "Puntos a una misma distancia de un centro", "Esa distancia es el radio."),
        ex("Un punto está a 2 cm del centro de un círculo de radio 3 cm. ¿Está dentro del círculo?", "Sí", "2 cm es menor que 3 cm."),
        ex("¿Cuántos puntos tiene en común, como máximo, una circunferencia con otra distinta del mismo radio y distinto centro?", "2", "Dos circunferencias distintas pueden cruzarse como máximo en 2 puntos."),
    ],
    op=task(
        "En una hoja dibuja dos puntos A y B separados 6 cm. Con un compás (o con una cuerda de 4 cm sujeta en el punto y un lápiz) traza una circunferencia de radio 4 cm con centro en A y otra de radio 4 cm con centro en B. (a) Marca los puntos donde se cruzan. (b) Mide con regla la distancia de cada uno de esos puntos a A y a B. (c) Explica con una frase por qué esos puntos están a 4 cm de ambos. Si no puedes dibujar, escribe qué esperas obtener.",
        "Las circunferencias se cruzan en dos puntos. La distancia de cada uno de esos puntos a A y a B es 4 cm, porque ambos están sobre las dos circunferencias, cuyo radio es 4 cm. Los puntos son los lugares que cumplen las dos condiciones a la vez.",
        ["traza dos circunferencias con el radio indicado", "identifica y mide los puntos de intersección", "explica la condición doble"],
        ["dibujo con compás o cuerda", "medidas", "frase de explicación"],
        ["usar una abertura distinta del radio", "no unir las dos condiciones"],
        "Pide que cambie la distancia entre A y B a 8 cm y observe cuántos puntos se cruzan.",
    ),
    reinforce="Describe con palabras todos los puntos que están a 3 cm de un punto O y todos los que están a menos de 3 cm.",
    extend="Explica qué pasaría con la zona de alcance de una antena que llega 10 km a la redonda si se instala otra igual a 20 km de distancia: ¿se cruzan las zonas?",
)
