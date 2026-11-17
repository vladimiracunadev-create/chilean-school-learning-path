"""Límites, derivadas e integrales (electivo 3.º y 4.º medio HC): OAC-05, integral como área bajo la curva, clases 1 a 6."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, cuaderno, hojas cuadriculadas y calculadora simple. Todas las funciones, gráficas descritas y datos están escritos en cada ejercicio y son de ejemplo, inventados para este cuaderno; no necesitas internet. "
             "Una hoja de cálculo o un graficador digital son opcionales y sirven para repetir sumas con muchos rectángulos; todo lo que se pide se puede hacer a mano.")
build = make_build(MATERIALS)

O5 = "MA-LIDI-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (gráficas descritas, de ejemplo). La velocidad v(t) = 4 m/s es constante entre t = 0 y t = 5 s. "
     "La velocidad u(t) = 2t m/s crece en línea recta desde (0; 0) hasta (6; 12). "
     "La función w(t) = 3 + t va en línea recta desde (0; 3) hasta (4; 7).")
build(
    O5, 1, F,
    use="Aprenderé a ver la integral como el área entre una gráfica y el eje horizontal, calculándola con figuras conocidas y escribiéndola con la notación de integral. Sirve para obtener cantidades acumuladas, como distancia o volumen.",
    prior=["Sé calcular áreas de rectángulos, triángulos y trapecios.", "Sé leer una gráfica de velocidad contra tiempo.", "Sé que distancia = rapidez × tiempo si la rapidez es constante."],
    explain=[
        "El área bajo la curva de una función f entre x = a y x = b, cuando f no es negativa, es la región entre la gráfica y el eje horizontal. Esa área se llama integral definida de f entre a y b y se escribe ∫ₐᵇ f(x) dx. Si la gráfica es una figura conocida, el área se calcula con fórmulas: rectángulo (base por altura), triángulo (base por altura dividido por 2) y trapecio ((base mayor + base menor) por altura dividido por 2).",
        "El área tiene un significado según las unidades de los ejes. Si v está en metros por segundo y t en segundos, el área tiene unidades de metros por segundo por segundo, es decir, metros: la distancia recorrida. Para v(t) = 4 entre 0 y 5, el área es el rectángulo 4·5 = 20 m. Para u(t) = 2t entre 0 y 6, es un triángulo de base 6 y altura 12: 6·12/2 = 36 m.",
        "Para w(t) = 3 + t entre 0 y 4, la región es un trapecio con lados paralelos de 3 y 7 y altura 4: (3 + 7)·4/2 = 20. En general, el área acumula lo que la función aporta en cada instante. Cuando la función cambia de forma que no es una figura simple, se necesita aproximar o usar otras herramientas, que se verán en las próximas clases.",
    ],
    vocab=[("integral definida", "área bajo la curva de f entre a y b, escrita ∫ₐᵇ f(x) dx"), ("área bajo la curva", "región entre la gráfica y el eje horizontal"), ("base y altura", "medidas para calcular el área de una figura"), ("acumular", "sumar aportes pequeños a lo largo de un intervalo"), ("unidad del área", "producto de las unidades de los dos ejes")],
    worked=[
        ("Área de un rectángulo como distancia", "Una bicicleta de ejemplo va a 5 m/s entre t = 0 y t = 8 s. ¿Qué distancia recorre?",
         ["La gráfica de velocidad es un rectángulo de base 8 y altura 5.", "Área = 8·5 = 40, con unidades m/s por s, es decir, metros."],
         "Recorre 40 m"),
        ("Área de un triángulo", "Para y(x) = x entre 0 y 10, calcula el área bajo la curva.",
         ["La región es un triángulo de base 10 y altura 10.", "Área = 10·10/2 = 50."],
         "El área es 50, es decir, ∫₀¹⁰ x dx = 50"),
    ],
    mistakes=[("Calcular el área de un triángulo como base por altura sin dividir por 2.", "Se confunde con el rectángulo.", "Recuerda que un triángulo ocupa la mitad del rectángulo."),
              ("Dar el área sin unidad o con unidad equivocada.", "No se interpreta el significado de los ejes.", "Multiplica las unidades: m/s por s da m.")],
    T=[
        ("=", "Una velocidad constante de 6 m/s se mantiene entre t = 2 s y t = 7 s. Calcula el área del rectángulo bajo esa gráfica.", "6*(7-2)", "Base 5 s por altura 6 m/s.", " m"),
        ("abc", "El área bajo una gráfica de velocidad (m/s) contra tiempo (s), ¿qué unidad tiene?", "Metros", "Metros por segundo", "Segundos", "m/s multiplicado por s da m, la distancia recorrida."),
        ("=", "{F} Calcula u(3) con u(t) = 2t.", "2*3", "Se reemplaza t por 3."),
        ("=", "{F} Calcula el área del triángulo bajo u(t) = 2t entre 0 y 4, con base 4 y altura 8.", "4*8//2", "El triángulo es la mitad de base por altura.", " m"),
        ("ab", "{F} ¿Qué representa el área 16 bajo u(t) = 2t entre 0 y 4?", "La distancia recorrida en esos 4 segundos", "La velocidad final del móvil", "El área bajo una velocidad contra tiempo da metros, no m/s."),
        ("{F} Para w(t) = 3 + t entre 0 y 4, ¿cuánto valen w(0) y w(4)?", "3 y 7", "w(0) = 3 + 0 y w(4) = 3 + 4; son los lados paralelos del trapecio."),
        ("=", "{F} Calcula el área del trapecio bajo w(t) = 3 + t entre 0 y 2, con lados paralelos w(0) = 3 y w(2) = 5: (3 + 5)·2/2.", "(3+5)*2//2", "Lados paralelos 3 y 5, altura 2."),
        ("=", "{F} Con v(t) = 4 m/s entre 5 y 8 s, ¿qué distancia adicional recorre?", "4*(8-5)", "Base 3 s por altura 4 m/s.", " m"),
        ("{F} Escribe con notación de integral el área bajo u(t) = 2t entre 0 y 6.", "∫₀⁶ 2t dt", "La integral lleva los límites 0 y 6 y la función 2t."),
        ("abc", "Un estudiante calcula el área bajo u(t) = 2t entre 0 y 6 como 6·12 = 72. ¿Cuál es el error?", "Olvidó dividir por 2: el triángulo mide 36", "Debió sumar 6 y 12", "No hay error", "La región es un triángulo, la mitad del rectángulo 6 por 12."),
        ("abc", "{F} ¿Qué recorre más distancia: v(t) = 4 m/s durante 5 s o u(t) = 2t durante 6 s?", "El móvil de u(t) = 2t, con 36 m", "El móvil de v(t) = 4 m/s, con 20 m", "Recorren lo mismo", "36 m es mayor que 20 m."),
        ("=", "Calcula el área bajo f(x) = 5 entre x = 2 y x = 9.", "5*(9-2)", "Rectángulo de base 7 y altura 5."),
        ("=", "Calcula el área bajo f(x) = x entre x = 0 y x = 8, que es un triángulo.", "8*8//2", "Base 8 y altura 8, dividido por 2."),
    ],
    ctx=("=", "Una bomba de ejemplo entrega un caudal constante de 12 litros por minuto durante 15 minutos. ¿Cuántos litros entrega? Es el área bajo el gráfico del caudal.", "12*15", "El rectángulo tiene base 15 y altura 12.", " litros"),
    sc=[
        ("En Matemática: ¿qué representa la integral definida de f entre a y b cuando f no es negativa?", "El área bajo la curva entre a y b", "Es la región entre la gráfica y el eje horizontal."),
        ("¿Cómo se calcula el área de un triángulo bajo una gráfica?", "Base por altura dividido por 2", "El triángulo es la mitad de un rectángulo."),
        ("=", "Si un caudal es constante, 8 L/min durante 6 min, ¿cuántos litros son?", "8*6", "Es el área del rectángulo 6 por 8."),
    ],
    op=("Un ciclista de ejemplo parte de 0 m/s y aumenta su velocidad en línea recta hasta 10 m/s en 5 s, y luego mantiene 10 m/s durante 5 s más. Dibuja la gráfica, separa la región en un triángulo y un rectángulo, calcula la distancia total y escribe la integral que la representa.",
        "Triángulo: base 5, altura 10, área 25 m. Rectángulo: base 5, altura 10, área 50 m. Total 75 m, escrita como ∫₀¹⁰ v(t) dt = 75 con v dada por tramos.",
        ["dibuja o describe las dos regiones", "calcula las dos áreas con unidades", "escribe la integral y el total"],
        ["dibujo, dos áreas, suma y notación de integral"],
        ["olvidar dividir el triángulo por 2", "no sumar las dos regiones", "omitir las unidades"],
        "Pregunta: «¿qué mide cada área?». Debe responder distancia en metros."),
    reinforce="Calcula el área bajo f(x) = 3 entre 1 y 7 y el área bajo g(x) = x entre 0 y 6, e indica qué figura es cada una.",
    extend="Explica por qué el área bajo una función constante f(x) = k entre a y b es k·(b − a) y cómo se escribe con una integral.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (función de ejemplo). f(x) = x² en el intervalo de 0 a 4, con cuatro rectángulos de ancho 1. "
     "Valores: f(0) = 0, f(1) = 1, f(2) = 4, f(3) = 9, f(4) = 16.")
build(
    O5, 2, F,
    use="Aprenderé a aproximar el área bajo una curva con rectángulos, usando una tabla y una gráfica, y a distinguir la aproximación por la izquierda de la de por la derecha. Sirve para estimar áreas cuando la región no es una figura conocida.",
    prior=["Sé calcular áreas de rectángulos.", "Sé evaluar f(x) = x².", "Sé sumar varios términos con ayuda de la calculadora."],
    explain=[
        "Cuando la región bajo una curva no es una figura conocida, se aproxima con rectángulos de igual ancho. El ancho es Δx = (b − a)/n, donde n es el número de rectángulos. Con la función x² entre 0 y 4 y n = 4, el ancho es Δx = 1. La suma de las áreas de los rectángulos aproxima el área bajo la curva.",
        "En la suma izquierda, la altura de cada rectángulo es el valor de f en el extremo izquierdo de su base: f(0), f(1), f(2) y f(3). Su suma es 1·(0 + 1 + 4 + 9) = 14. En la suma derecha se usa el extremo derecho: f(1), f(2), f(3) y f(4), con suma 1·(1 + 4 + 9 + 16) = 30. Como f es creciente, la izquierda queda por debajo del área real y la derecha por encima.",
        "Por eso el área real está entre 14 y 30. Con n = 2 (Δx = 2), la suma izquierda es 2·(0 + 4) = 8 y la derecha es 2·(4 + 16) = 40: la distancia entre ellas es mayor. Cuantos más rectángulos, más cerca queda la aproximación. Una tabla con columnas x, f(x) y área de cada rectángulo ordena el trabajo.",
    ],
    vocab=[("rectángulo de aproximación", "rectángulo de ancho Δx y altura f en un extremo de su base"), ("Δx", "ancho de cada rectángulo, (b − a)/n"), ("suma izquierda", "suma de rectángulos con altura en el extremo izquierdo"), ("suma derecha", "suma de rectángulos con altura en el extremo derecho"), ("n", "número de rectángulos")],
    worked=[
        ("Suma izquierda", "Para f(x) = x en [0, 3] con n = 3 rectángulos, calcula la suma izquierda.",
         ["Δx = (3 − 0)/3 = 1 y las alturas izquierdas son f(0) = 0, f(1) = 1, f(2) = 2.", "Suma = 1·(0 + 1 + 2) = 3."],
         "La suma izquierda es 3"),
        ("Suma derecha", "Para la misma función y n = 3, calcula la suma derecha.",
         ["Las alturas derechas son f(1) = 1, f(2) = 2, f(3) = 3.", "Suma = 1·(1 + 2 + 3) = 6."],
         "La suma derecha es 6, y el área real (triángulo 4,5) queda entre 3 y 6"),
    ],
    mistakes=[("Usar un ancho distinto para cada rectángulo.", "Se confunde la altura con el ancho.", "Calcula una vez Δx = (b − a)/n y úsalo en todos."),
              ("Sumar las alturas sin multiplicar por Δx.", "Se olvida que el área es altura por ancho.", "Multiplica la suma de alturas por Δx.")],
    T=[
        ("=", "{F} Calcula el ancho Δx de cada rectángulo: (4 − 0)/4.", "(4-0)//4", "Se divide la longitud del intervalo entre n."),
        ("=", "{F} Calcula f(3).", "3*3", "f(3) = 3²."),
        ("abc", "¿Qué altura usa el rectángulo con base entre 2 y 3 en una suma izquierda?", "f(2)", "f(3)", "f(2,5)", "La suma izquierda toma el valor de f en el extremo izquierdo de la base."),
        ("=", "Para h(x) = x² + 1 en [0, 3] con n = 3 (Δx = 1), los valores son h(0) = 1, h(1) = 2, h(2) = 5 y h(3) = 10. Calcula la suma izquierda: 1·(1 + 2 + 5).", "1*(1+2+5)", "Suma de las alturas h(0), h(1) y h(2)."),
        ("=", "Con los mismos valores de h (1, 2, 5 y 10), calcula la suma derecha con n = 3: 1·(2 + 5 + 10).", "1*(2+5+10)", "Suma de las alturas h(1), h(2) y h(3)."),
        ("ab", "Como h(x) = x² + 1 es creciente en [0, 3] y sus sumas con n = 3 son 8 (izquierda) y 17 (derecha), ¿dónde está el área real bajo la curva?", "Entre 8 y 17", "Sobre 17", "La izquierda subestima y la derecha sobreestima, así que el área queda en medio."),
        ("=", "Calcula el promedio de las dos sumas de h con n = 3: (8 + 17)/2.", "(8+17)/2", "Es el punto medio entre ambas estimaciones."),
        ("=", "Para x² en [0, 6] con n = 3 (Δx = 2), los valores son f(0) = 0, f(2) = 4, f(4) = 16 y f(6) = 36. Calcula la suma izquierda: 2·(0 + 4 + 16).", "2*(0+4+16)", "Alturas 0, 4 y 16, ancho 2."),
        ("=", "Con los mismos valores de x² en [0, 6] y n = 3 (Δx = 2), calcula la suma derecha: 2·(4 + 16 + 36).", "2*(4+16+36)", "Alturas 4, 16 y 36, ancho 2."),
        ("abc", "Para x² en [0, 6], con n = 3 las sumas son 40 y 112; con n = 6 (Δx = 1) son 55 y 91. ¿Qué ocurre al aumentar n?", "La distancia entre las sumas disminuye, de 72 a 36", "La distancia aumenta", "La distancia no cambia", "112 − 40 = 72 y 91 − 55 = 36, así que las sumas se acercan."),
        ("ab", "{F} Si f fuera decreciente, ¿la suma izquierda subestimaría o sobreestimaría el área?", "La sobreestimaría, porque usa la altura mayor de cada tramo", "La subestimaría", "En una función decreciente, el extremo izquierdo es el más alto de cada base."),
        ("=", "Para g(x) = 2x + 1 en [0, 3] con 3 rectángulos de ancho 1, calcula la suma izquierda: 1·(g(0) + g(1) + g(2)).", "1*(1+3+5)", "Las alturas son 1, 3 y 5."),
        ("=", "Calcula el área exacta del trapecio bajo g(x) = 2x + 1 entre 0 y 3: (1 + 7)·3/2.", "(1+7)*3//2", "Lados paralelos 1 y 7, altura 3."),
    ],
    ctx=("=", "El caudal de un riachuelo de ejemplo, medido al inicio de cada minuto, es 2, 4, 6 y 8 litros por minuto en t = 0, 1, 2 y 3. Para estimar los litros que pasan en esos 3 minutos con lecturas al inicio de cada minuto, calcula 1·(2 + 4 + 6).", "1*(2+4+6)", "Es una suma izquierda con tres rectángulos de ancho 1 minuto.", " litros"),
    sc=[
        ("En Matemática: ¿qué es Δx en una suma de rectángulos?", "El ancho de cada rectángulo, (b − a)/n", "Se obtiene dividiendo el intervalo en partes iguales."),
        ("¿Qué altura usa la suma derecha?", "El valor de f en el extremo derecho de cada base", "La izquierda usa el extremo izquierdo."),
        ("=", "¿Cuánto es el ancho Δx si el intervalo va de 2 a 10 con n = 4?", "(10-2)//4", "Se divide 8 entre 4."),
    ],
    op=("Para f(x) = x² en [0, 2] con n = 4 rectángulos (Δx = 0,5), arma una tabla con x, f(x) y el área de cada rectángulo para la suma izquierda y la derecha, y escribe un intervalo donde debe estar el área real. Valores: f(0) = 0, f(0,5) = 0,25, f(1) = 1, f(1,5) = 2,25, f(2) = 4.",
        "Izquierda: 0,5·(0 + 0,25 + 1 + 2,25) = 1,75. Derecha: 0,5·(0,25 + 1 + 2,25 + 4) = 3,75. El área real está entre 1,75 y 3,75.",
        ["usa Δx = 0,5 y las alturas correctas", "calcula las dos sumas", "escribe el intervalo donde está el área"],
        ["tabla de cuatro filas, dos sumas e intervalo"],
        ["usar f(2) en la suma izquierda", "no multiplicar por Δx", "no concluir un intervalo"],
        "Pregunta: «¿por qué la izquierda queda más baja?». Debe decir que f crece."),
    reinforce="Con f(x) = x en [0, 4] y n = 4, calcula la suma izquierda y la derecha y compáralas con el área del triángulo.",
    extend="Explica por qué, para una función creciente, la suma izquierda siempre es menor o igual que el área real.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (función de ejemplo). f(x) = x en el intervalo de 0 a 4; el área exacta del triángulo es 8. "
     "Con n = 4 (Δx = 1): suma izquierda 6 y derecha 10. Con n = 8 (Δx = 0,5): izquierda 7 y derecha 9. Con n = 16 (Δx = 0,25): izquierda 7,5 y derecha 8,5.")
build(
    O5, 3, F,
    use="Aprenderé a mejorar la aproximación con más rectángulos y a ver la integral definida como el límite de las sumas de rectángulos. Sirve para entender por qué la integral da el área exacta.",
    prior=["Sé calcular sumas izquierda y derecha.", "Sé qué es un límite.", "Sé calcular el área de un triángulo."],
    explain=[
        "Si se duplica el número de rectángulos, cada uno es más delgado y la aproximación mejora. Con f(x) = x en [0, 4]: con n = 4 las sumas son 6 y 10; con n = 8, son 7 y 9; con n = 16, son 7,5 y 8,5. La distancia entre las dos sumas baja de 4 a 2 y a 1: se reduce a la mitad cada vez que se duplica n.",
        "Las dos sumas se acercan a un mismo valor, 8, que es el área exacta del triángulo (base 4 por altura 4 dividido por 2). Ese valor común es el límite de las sumas cuando n tiende a infinito. Para funciones continuas, el límite de las sumas izquierda y derecha existe y es el mismo; ese número es la integral definida ∫ₐᵇ f(x) dx.",
        "La notación ∫ₐᵇ f(x) dx recuerda que es una suma de productos f(x)·Δx cuando Δx se hace muy pequeño: el símbolo ∫ es una S alargada, de «suma». Así, ∫₀⁴ x dx = 8. Con tablas y herramientas digitales se pueden calcular sumas con muchos rectángulos, pero el valor exacto de la integral se confirma por otras vías, como una figura geométrica conocida.",
    ],
    vocab=[("límite de sumas", "valor al que se acercan las sumas de rectángulos al aumentar n"), ("integral definida", "límite de las sumas de f(x)·Δx cuando n tiende a infinito"), ("∫", "símbolo de integral, una S alargada de «suma»"), ("converger", "acercarse a un valor fijo"), ("función continua", "función sin saltos en el intervalo")],
    worked=[
        ("Ver la convergencia", "Para f(x) = x en [0, 2], las sumas izquierdas con n = 2, 4 y 8 son 1; 1,5 y 1,75, y las derechas son 3; 2,5 y 2,25. ¿A qué valor se acercan?",
         ["Las izquierdas suben: 1; 1,5; 1,75.", "Las derechas bajan: 3; 2,5; 2,25. Ambas se acercan a 2."],
         "Se acercan a 2, el área del triángulo de base 2 y altura 2"),
        ("Escribir la integral", "Escribe la integral que representa el área bajo f(x) = x entre 0 y 2 y su valor.",
         ["Los límites son 0 y 2 y la función es x.", "El valor es el triángulo: 2·2/2 = 2."],
         "∫₀² x dx = 2"),
    ],
    mistakes=[("Pensar que con más rectángulos las sumas se alejan del área real.", "Se confunde la forma de los rectángulos con su cantidad.", "Más rectángulos significa menor error, hasta que se acercan al límite."),
              ("Creer que la integral es la suma de unos pocos rectángulos.", "Se confunde la aproximación con el límite.", "La integral es el valor al que tienden las sumas cuando n crece sin límite.")],
    T=[
        ("=", "{F} Calcula el ancho Δx para n = 8 en [0, 4]: 4/8.", "4/8", "Se divide la longitud del intervalo entre n."),
        ("=", "Para f(x) = x en [0, 8] con n = 4 (Δx = 2), calcula la suma izquierda: 2·(0 + 2 + 4 + 6).", "2*(0+2+4+6)", "Alturas f(0), f(2), f(4), f(6), ancho 2."),
        ("=", "Para f(x) = x en [0, 8] con n = 4 (Δx = 2), calcula la suma derecha: 2·(2 + 4 + 6 + 8).", "2*(2+4+6+8)", "Alturas f(2), f(4), f(6), f(8), ancho 2."),
        ("=", "Para f(x) = x en [0, 8], con n = 4 las sumas son 24 y 40. Calcula la diferencia entre la derecha y la izquierda.", "40-24", "Es la distancia entre ambas estimaciones."),
        ("=", "Para f(x) = x en [0, 8], con n = 8 (Δx = 1) las sumas son 28 y 36. Calcula la diferencia entre la derecha y la izquierda.", "36-28", "La diferencia se reduce al aumentar n."),
        ("abc", "{F} ¿Qué ocurre con la diferencia entre ambas sumas cuando se duplica n?", "Se reduce a la mitad", "Se duplica", "Se mantiene igual", "Pasa de 4 a 2 y luego a 1."),
        ("Para f(x) = x en [0, 8], con n = 16 (Δx = 0,5) las sumas son 30 y 34. ¿Cuánto vale la diferencia entre ellas?", "4", "34 − 30 es 4, la mitad de la diferencia con n = 8."),
        ("abc", "Para f(x) = x en [0, 8], las sumas izquierdas con n = 4, 8 y 16 son 24; 28 y 30, y las derechas son 40; 36 y 34. ¿A qué valor se acercan?", "32", "28", "40", "Ambas sucesiones se acercan al valor común 32, el área del triángulo."),
        ("Escribe con notación de integral el área bajo f(x) = x entre 0 y 8 y su valor.", "∫₀⁸ x dx = 32", "El área exacta es la del triángulo, 8·8/2 = 32."),
        ("ab", "{F} ¿Por qué el valor límite 8 coincide con el área de la figura geométrica?", "Porque el área exacta del triángulo, base 4 y altura 4, es 8", "Porque las sumas con n = 4 ya valen 8", "El triángulo da 4·4/2 = 8, y las sumas se acercan a ese valor."),
        ("abc", "¿Qué significa el símbolo ∫ₐᵇ f(x) dx?", "El área bajo la curva entre a y b, como límite de sumas de rectángulos", "La derivada de f entre a y b", "El valor de f en b", "La integral definida es el límite de las sumas de f(x)·Δx."),
        ("=", "Para f(x) = x en [0, 10] con n = 5 (Δx = 2), calcula la suma izquierda: 2·(0 + 2 + 4 + 6 + 8).", "2*(0+2+4+6+8)", "Alturas f(0), f(2), f(4), f(6), f(8), ancho 2."),
        ("=", "Calcula el área exacta del triángulo bajo f(x) = x entre 0 y 12.", "12*12//2", "Base 12 y altura 12, dividido por 2."),
    ],
    ctx=("=", "Un ciclista de ejemplo aumenta su velocidad v(t) = t metros por segundo durante 10 segundos. ¿Qué distancia recorre? Es el área del triángulo bajo v entre 0 y 10.", "10*10//2", "Triángulo de base 10 y altura 10.", " m"),
    sc=[
        ("En Matemática: ¿qué ocurre con las sumas de rectángulos cuando n aumenta?", "Se acercan al área exacta", "Los rectángulos más delgados ajustan mejor la curva."),
        ("¿Qué es la integral definida en términos de sumas?", "El límite de las sumas de f(x)·Δx cuando n tiende a infinito", "Es el valor común al que tienden las sumas."),
        ("=", "Si las sumas izquierda y derecha son 7 y 9, ¿cuál es su promedio?", "(7+9)//2", "El promedio está entre ambas estimaciones."),
    ],
    op=("Para f(x) = x² en [0, 2], las sumas izquierdas con n = 2, 4 y 8 son 1; 1,75 y 2,1875, y las derechas con n = 2, 4 y 8 son 5; 3,75 y 3,1875. Haz una tabla, calcula en cada n la diferencia entre ambas sumas, describe a qué valor parecen acercarse y escribe la integral correspondiente.",
        "Diferencias: 4; 2; 1. Las izquierdas suben y las derechas bajan; parecen acercarse a un valor cercano a 2,67. Integral: ∫₀² x² dx. El valor exacto lo dará la antiderivada en la clase siguiente (8/3).",
        ["calcula las diferencias con cada n", "describe la tendencia de ambas sumas", "escribe la integral con límites correctos"],
        ["tabla con tres filas, descripción e integral"],
        ["decir que las sumas se alejan", "confundir los límites de la integral", "no mencionar el número de rectángulos"],
        "Pregunta: «¿qué pasa con la diferencia al duplicar n?». Debe decir que se reduce a la mitad."),
    reinforce="Con f(x) = x en [0, 6], calcula las sumas izquierda y derecha con n = 3 y n = 6, y compáralas con el triángulo.",
    extend="Explica por qué, si Δx se hace cada vez más pequeño, el error de la aproximación puede hacerse tan pequeño como se quiera.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (reglas y funciones de ejemplo). Una antiderivada de f es una función F tal que F'(x) = f(x). Reglas: una antiderivada de xⁿ es xⁿ⁺¹/(n + 1), y de una constante k es kx. "
     "Teorema fundamental: ∫ₐᵇ f(x) dx = F(b) − F(a). Ejemplos: a f(x) = 2x le corresponde F(x) = x²; a g(x) = 3x² le corresponde G(x) = x³; a h(x) = 4 le corresponde H(x) = 4x.")
build(
    O5, 4, F,
    use="Aprenderé a calcular integrales definidas de polinomios sencillos con una antiderivada y a comprobar el resultado con áreas conocidas. Sirve para obtener el área exacta sin sumar muchos rectángulos.",
    prior=["Sé derivar polinomios.", "Sé que la integral es el área bajo la curva.", "Sé evaluar funciones en un punto."],
    explain=[
        "Una antiderivada de f es una función F cuya derivada es f. Por ejemplo, x² es una antiderivada de 2x, porque la derivada de x² es 2x. También lo es x² + 5, porque la derivada de una constante es 0. Para xⁿ, una antiderivada es xⁿ⁺¹ dividido por n + 1; para una constante k, es kx. Siempre se puede comprobar derivando.",
        "El teorema fundamental del cálculo une derivadas e integrales: si F es una antiderivada de f, entonces ∫ₐᵇ f(x) dx = F(b) − F(a). Con f(x) = 2x entre 0 y 4: F(x) = x², F(4) − F(0) = 16 − 0 = 16. Ese resultado coincide con el área del triángulo bajo y = 2x, de base 4 y altura 8 (4·8/2 = 16). La constante que se agregue a F se cancela en la resta.",
        "Con g(x) = 3x² entre 0 y 3: G(x) = x³ y G(3) − G(0) = 27 − 0 = 27. Con x² entre 0 y 3: una antiderivada es x³/3, y el resultado es 27/3 − 0 = 9. Para una suma de términos se usa una antiderivada de cada término. Este método da el valor exacto al que tienden las sumas de rectángulos y se verifica con áreas de figuras cuando la gráfica es una recta.",
    ],
    vocab=[("antiderivada", "función cuya derivada es la función dada"), ("teorema fundamental", "∫ₐᵇ f = F(b) − F(a)"), ("evaluar", "reemplazar x por un número"), ("constante de integración", "constante que se agrega a una antiderivada y se cancela en la resta"), ("verificar derivando", "comprobar que la derivada de F es f")],
    worked=[
        ("Calcular una integral definida", "Calcula ∫₁³ 2x dx.",
         ["Una antiderivada de 2x es F(x) = x².", "F(3) − F(1) = 9 − 1 = 8."],
         "La integral vale 8"),
        ("Verificar la antiderivada", "¿Es x³/3 una antiderivada de x²?",
         ["Se deriva x³/3: 3x²/3 = x².", "La derivada coincide con la función."],
         "Sí, x³/3 es una antiderivada de x²"),
    ],
    mistakes=[("Calcular F(a) − F(b) en lugar de F(b) − F(a).", "Se invierte el orden de los límites.", "Resta siempre el valor en el límite inferior al del superior."),
              ("Decir que la antiderivada de x² es 2x.", "Se deriva en vez de integrar.", "Sube el exponente y divide por el nuevo exponente: x³/3.")],
    T=[
        ("{F} Se sabe que la derivada de x² es 2x. ¿Cuál es una antiderivada de 2x?", "x²", "Una antiderivada es una función cuya derivada da la función dada."),
        ("abc", "{F} ¿Cuál es una antiderivada de 4x³?", "x⁴", "4x⁴", "12x²", "La derivada de x⁴ es 4x³; las otras no."),
        ("=", "{F} Calcula G(5) con G(x) = x³.", "5*5*5", "G(5) = 5³."),
        ("=", "{F} Calcula ∫₀⁵ 2x dx con la fórmula F(5) − F(0), usando F(x) = x².", "5*5-0*0", "Se evalúa en los límites y se resta."),
        ("=", "{F} Calcula ∫₁² 3x² dx con la fórmula G(2) − G(1), usando G(x) = x³.", "2*2*2-1*1*1", "G(2) = 8 y G(1) = 1."),
        ("ab", "{F} La integral ∫₀⁵ 2x dx vale 25. ¿Coincide con el área del triángulo bajo y = 2x entre 0 y 5, de base 5 y altura 10?", "Sí: 5·10/2 también da 25", "No: el triángulo da 50", "La mitad de 5 por 10 es 25, igual que la integral."),
        ("=", "Calcula ∫₂⁴ 2x dx como F(4) − F(2) con F(x) = x².", "4*4-2*2", "Se resta el valor en 2 al valor en 4."),
        ("Según la regla, ¿cuál es una antiderivada de x³?", "x⁴/4", "Se sube el exponente a 4 y se divide por 4."),
        ("=", "Calcula ∫₀⁶ x² dx con la antiderivada x³/3: (6·6·6)/3 − 0.", "6*6*6//3", "216/3 = 72."),
        ("abc", "¿Por qué se resta F(a) en el teorema fundamental?", "Porque F(b) − F(a) mide cuánto cambia F entre a y b, que es el área", "Porque F(a) siempre vale 0", "Porque así el resultado es positivo", "La resta da el cambio acumulado entre los dos límites."),
        ("ab", "Un compañero dice que x² + 5 también es antiderivada de 2x. ¿Tiene razón?", "Sí: su derivada también es 2x y la constante se cancela al restar", "No: solo x² lo es", "La derivada de la constante 5 es 0, así que x² + 5 da la misma derivada."),
        ("=", "Calcula ∫₀² (3x² + 4) dx con la antiderivada x³ + 4x: (2·2·2 + 4·2) − 0.", "2*2*2+4*2", "Se evalúa x³ + 4x en 2 y se resta el valor en 0."),
        ("=", "Calcula ∫₂⁵ 4 dx con la antiderivada 4x: 4·5 − 4·2.", "4*5-4*2", "Coincide con un rectángulo de base 3 y altura 4."),
    ],
    ctx=("=", "El caudal de un grifo de ejemplo es q(t) = 2t litros por minuto, con t en minutos. ¿Cuántos litros salen entre t = 0 y t = 5? Usa la antiderivada t².", "5*5-0*0", "La integral se calcula con F(5) − F(0).", " litros"),
    sc=[
        ("En Matemática: ¿qué es una antiderivada de f?", "Una función cuya derivada es f", "Se comprueba derivando la función candidata."),
        ("¿Qué dice el teorema fundamental?", "La integral definida es F(b) − F(a) con F antiderivada de f", "Une derivadas e integrales en una sola fórmula."),
        ("=", "Si F(x) = x² es antiderivada de 2x, ¿cuánto vale ∫₀⁶ 2x dx?", "6*6-0*0", "Se evalúa F(6) − F(0)."),
    ],
    op=("Calcula ∫₀⁴ (x + 1) dx de dos maneras: con la antiderivada x²/2 + x y con el trapecio bajo y = x + 1 entre 0 y 4 (lados paralelos 1 y 5). Compara los resultados y escribe una frase sobre qué te dice la coincidencia.",
        "Antiderivada: F(4) − F(0) = (16/2 + 4) − 0 = 12. Trapecio: (1 + 5)·4/2 = 12. Coinciden, lo que respalda que la integral da el área exacta.",
        ["calcula la integral con la antiderivada", "calcula el área con la figura", "compara y explica la coincidencia"],
        ["hoja con dos cálculos y una frase"],
        ["invertir el orden de la resta F(b) − F(a)", "olvidar la antiderivada del término constante", "no comparar"],
        "Pregunta: «¿por qué dan lo mismo?». Debe decir que ambos miden el mismo área."),
    reinforce="Calcula ∫₀² 3x² dx con la antiderivada x³ y ∫₁⁴ 2 dx con la antiderivada 2x.",
    extend="Explica por qué dos antiderivadas de una misma función se diferencian solo en una constante y por qué eso no cambia la integral definida.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (función y datos de ejemplo). f(x) = x² en el intervalo de 0 a 3; el área exacta es ∫₀³ x² dx = 9, con antiderivada x³/3. "
     "Con n = 3 (Δx = 1): izquierda 5 y derecha 14. Con n = 6 (Δx = 0,5): izquierda 6,875 y derecha 11,375. "
     "Función s(x) = x − 1 en el intervalo de 0 a 2, con antiderivada x²/2 − x.")
build(
    O5, 5, F,
    use="Aprenderé a comparar aproximaciones con el valor exacto de una integral, a calcular el error y a entender el área con signo cuando la gráfica queda bajo el eje. Sirve para evaluar si una estimación es confiable.",
    prior=["Sé calcular sumas izquierda y derecha.", "Sé calcular una integral con antiderivada.", "Sé el significado de área con unidades."],
    explain=[
        "El error de una aproximación es la diferencia entre el valor exacto y el estimado. Con f(x) = x² en [0, 3], el área exacta es 9. Con n = 3, la suma izquierda 5 se equivoca en 4 y la derecha 14 en 5. Con n = 6, la izquierda 6,875 se equivoca en 2,125 y la derecha 11,375 en 2,375. Al doblar n los errores bajan, lo que confirma que las sumas se acercan al valor exacto.",
        "Un buen criterio es comprobar que el área exacta queda entre la suma izquierda y la derecha cuando la función es creciente, y que el promedio de ambas es una mejor estimación: (5 + 14)/2 = 9,5 y (6,875 + 11,375)/2 = 9,125, cada vez más cerca de 9. Compararlos con el valor exacto permite decidir si una estimación sirve o necesita más rectángulos.",
        "Si la función es negativa sobre un tramo, la integral cuenta esa parte con signo negativo. Con s(x) = x − 1 entre 0 y 2, los dos triángulos (uno bajo el eje y otro sobre él, cada uno de área 1/2) se compensan y la integral es F(2) − F(0) = 0. El área total sin signo es 1/2 + 1/2 = 1. Por eso hay que distinguir integral (con signo) y área total (sin signo).",
    ],
    vocab=[("error de aproximación", "diferencia entre el valor exacto y el estimado"), ("área con signo", "área sobre el eje positiva y bajo el eje negativa"), ("área total", "suma de las áreas sin considerar el signo"), ("compensar", "anularse una parte positiva con una negativa"), ("promedio de sumas", "(izquierda + derecha)/2, una estimación mejorada")],
    worked=[
        ("Calcular errores", "Para f(x) = x en [0, 4], el área exacta es 8, y con n = 4 las sumas son 6 y 10. Calcula los errores.",
         ["Error de la izquierda: 8 − 6 = 2.", "Error de la derecha: 10 − 8 = 2."],
         "Ambos errores son 2"),
        ("Integral con signo", "Calcula ∫₀² (x − 2) dx con la antiderivada x²/2 − 2x.",
         ["F(2) = 2 − 4 = −2 y F(0) = 0.", "F(2) − F(0) = −2."],
         "La integral vale −2: toda la región está bajo el eje"),
    ],
    mistakes=[("Interpretar una integral negativa como un error.", "Se ignora el signo del área.", "Una integral negativa indica que la región está bajo el eje."),
              ("Dar por exacta una suma con pocos rectángulos.", "Se confunde estimación con valor exacto.", "Compara con el valor exacto o con n mayor antes de concluir.")],
    T=[
        ("=", "{F} Calcula el área exacta con la antiderivada x³/3: 27/3.", "27//3", "Se evalúa x³/3 en 3 y se resta el valor en 0."),
        ("=", "Para x² en [0, 6], con n = 3 (Δx = 2), calcula la suma izquierda: 2·(0 + 4 + 16).", "2*(0+4+16)", "Alturas f(0), f(2), f(4), ancho 2."),
        ("=", "Para x² en [0, 6], con n = 3 (Δx = 2), calcula la suma derecha: 2·(4 + 16 + 36).", "2*(4+16+36)", "Alturas f(2), f(4), f(6), ancho 2."),
        ("=", "Para x² en [0, 6] el área exacta es 72 (antiderivada x³/3). Con n = 3 la suma izquierda es 40. Calcula su error.", "72-40", "Diferencia entre el valor exacto y la estimación."),
        ("=", "Para x² en [0, 6] el área exacta es 72. Con n = 3 la suma derecha es 112. Calcula su error.", "112-72", "La estimación excede el valor exacto."),
        ("abc", "Para x² en [0, 6], con n = 6 la izquierda es 55 y la derecha 91. ¿Cuál está más cerca del área exacta 72?", "La izquierda, que se equivoca en 17", "La derecha, que se equivoca en 17", "Ambas igual", "72 − 55 = 17 y 91 − 72 = 19, así que la izquierda queda más cerca."),
        ("Para x² en [0, 6], con n = 6 las sumas son 55 y 91. Calcula su promedio.", "73", "Se suman las dos sumas y se divide entre 2: 146/2."),
        ("abc", "Para x² en [0, 6], los promedios son 76 con n = 3 y 73 con n = 6, y el área exacta es 72. ¿Qué indica eso?", "Al aumentar n el promedio se acerca más a 72", "Al aumentar n el promedio se aleja de 72", "El promedio no depende de n", "73 está más cerca de 72 que 76."),
        ("Calcula ∫₀⁴ (x − 3) dx con la antiderivada x²/2 − 3x.", "−4", "F(4) = 8 − 12 = −4 y F(0) = 0."),
        ("abc", "{F} ¿Por qué la integral de x − 1 entre 0 y 2 da 0 si hay regiones sombreadas?", "Porque la parte bajo el eje cuenta negativa y cancela a la de arriba", "Porque no hay área", "Porque la función es constante", "Los dos triángulos tienen igual área y signos opuestos."),
        ("=", "Para y = x − 3 entre 0 y 4, hay un triángulo bajo el eje de área 9/2 y otro sobre el eje de área 1/2. Calcula el área total sin signo.", "9/2+1/2", "Se suman las dos áreas como positivas."),
        ("ab", "Si ∫ₐᵇ f(x) dx es negativa, ¿qué indica?", "Que predomina la región bajo el eje horizontal", "Que se calculó mal", "El área bajo el eje cuenta con signo negativo."),
        ("abc", "Para x² en [0, 6], un estudiante usa una suma izquierda con n = 3 y concluye que el área es 40. Otro usa la antiderivada y obtiene 72. ¿Cuál es más confiable y por qué?", "El segundo: es exacto, y el primero es una suma izquierda que subestima", "El primero: porque es una suma", "Ambos igual de confiables", "La antiderivada da el valor exacto y 40 es una cota inferior."),
    ],
    ctx=("abc", "Un modelo de ejemplo estima el volumen que entra a un tanque con una suma derecha de 3 rectángulos y obtiene 14 m³; con la integral exacta obtiene 9 m³. Si el tanque real se llenó con 8,8 m³, ¿cuál estimación es más cercana?", "La integral exacta, 9 m³", "La suma de 3 rectángulos, 14 m³", "Ambas igual de cercanas", "9 está a 0,2 de 8,8 y 14 está a 5,2."),
    sc=[
        ("En Matemática: ¿qué es el error de una aproximación?", "La diferencia entre el valor exacto y el estimado", "Mide cuánto se aleja la estimación del valor real."),
        ("¿Qué indica una integral definida negativa?", "Que predomina la región bajo el eje horizontal", "El área bajo el eje cuenta con signo negativo."),
        ("=", "Si el valor exacto es 9 y una estimación es 7, ¿cuánto vale el error?", "9-7", "Es la diferencia entre el valor exacto y la estimación."),
    ],
    op=("Para f(x) = x en [0, 4], el área exacta es 8. Con n = 4 las sumas son 6 y 10 y con n = 8, 7 y 9. Calcula los errores de cada suma, el promedio de cada par y di cuál estimación es la mejor y por qué. Luego explica si 7 serviría como estimación de 8 en una situación donde se aceptan errores de 0,5.",
        "Errores con n = 4: 2 y 2. Con n = 8: 1 y 1. Promedios: 8 y 8 (en esta función son exactos). La mejor estimación es la de n = 8 por tener menores errores. El valor 7 tiene error 1, mayor que 0,5, así que no serviría; haría falta n = 16 (error 0,5).",
        ["calcula errores y promedios", "compara estimaciones con criterio", "evalúa la tolerancia pedida"],
        ["hoja con errores, promedios y decisión"],
        ["comparar solo dos números sin calcular el error", "no relacionar el error con n", "no considerar la tolerancia"],
        "Pregunta: «¿cuánto se equivoca cada una?». Debe calcular el error."),
    reinforce="Con f(x) = x² en [0, 3], calcula el error del promedio de las sumas con n = 3 respecto de 9.",
    extend="Explica cuándo el promedio de las sumas izquierda y derecha sobreestima o subestima el área de una función creciente y cóncava hacia arriba.",
)

# ============================================================ OAC-05, clase 6
F = ("Ficha 6 (modelo de ejemplo, inventado). El caudal de una llave es q(t) = 12 − 2t litros por minuto, con t entre 0 y 6 minutos. "
     "Una antiderivada es F(t) = 12t − t². Con n = 3 (Δt = 2): q(0) = 12, q(2) = 8, q(4) = 4 y q(6) = 0. "
     "Se midió en un recipiente real 34 litros en esos 6 minutos.")
build(
    O5, 6, F,
    use="Aprenderé a modelar una situación con una integral como área bajo la curva, a interpretarla con unidades y a decidir si el modelo hay que ajustarlo con datos reales. Sirve para estimar acumulados en ciencias y en la vida diaria.",
    prior=["Sé calcular áreas bajo gráficas con figuras y con integrales.", "Sé estimar con sumas de rectángulos.", "Sé interpretar unidades."],
    explain=[
        "Una integral sirve para acumular. Si q(t) es un caudal en litros por minuto, el área bajo q entre dos tiempos es el volumen que pasó, en litros. Para q(t) = 12 − 2t entre 0 y 6, la región es un triángulo de base 6 y altura 12, con área 6·12/2 = 36 L. Con antiderivada: F(6) − F(0) = (72 − 36) − 0 = 36 L. Ambos métodos coinciden.",
        "Con sumas de rectángulos (Δt = 2), la izquierda da 2·(12 + 8 + 4) = 48 L y la derecha 2·(8 + 4 + 0) = 24 L. Como q decrece, la izquierda sobreestima y la derecha subestima el volumen 36. Con n = 6 (Δt = 1) la izquierda da 42 y la derecha 30: más cerca de 36. Una hoja de cálculo permite repetir esas sumas con muchos rectángulos.",
        "Un modelo hay que contrastarlo con datos. Si el recipiente real recibió 34 L y el modelo da 36 L, el error es 2 L: se puede aceptar si la tolerancia lo permite, o ajustar una constante, por ejemplo la pendiente. También hay que declarar el rango de validez: q(t) = 12 − 2t solo sirve hasta t = 6, porque después daría caudales negativos, algo que en esta llave no tiene sentido.",
    ],
    vocab=[("modelar", "representar una situación con funciones y cálculos"), ("acumulado", "total que resulta de sumar aportes a lo largo del tiempo"), ("rango de validez", "valores de t donde el modelo sirve"), ("tolerancia", "error máximo que se acepta"), ("ajustar", "cambiar constantes o forma del modelo para acercarlo a los datos")],
    worked=[
        ("Modelar un volumen acumulado", "Con q(t) = 12 − 2t, calcula el volumen entre t = 0 y t = 3.",
         ["Antiderivada F(t) = 12t − t².", "F(3) − F(0) = (36 − 9) − 0 = 27."],
         "Pasan 27 litros en los primeros 3 minutos"),
        ("Decidir si ajustar", "El modelo da 36 L pero se midieron 34 L. El error es 2 L. ¿Qué se hace si la tolerancia es 1 L?",
         ["El error 2 L supera la tolerancia de 1 L.", "Hay que ajustar el modelo, por ejemplo corrigiendo el caudal inicial."],
         "Conviene ajustar el modelo"),
    ],
    mistakes=[("Usar el modelo fuera del rango, por ejemplo t = 8 en q(t) = 12 − 2t.", "Se obtiene un caudal negativo sin sentido.", "Declara el rango de validez y no lo extiendas sin revisar."),
              ("Dar el volumen sin unidades.", "No se interpreta el significado de la integral.", "Escribe litros y explica que son el acumulado del caudal.")],
    T=[
        ("=", "{F} Calcula q(0).", "12-2*0", "Se reemplaza t por 0."),
        ("=", "{F} Calcula q(3).", "12-2*3", "Se reemplaza t por 3."),
        ("abc", "El área bajo una gráfica de caudal en litros por minuto contra tiempo en minutos, ¿qué unidad tiene?", "Litros", "Litros por minuto", "Minutos", "L/min multiplicado por min da L."),
        ("=", "{F} Calcula el volumen entre 0 y 4 minutos como el área del trapecio con lados paralelos q(0) = 12 y q(4) = 4 y altura 4: (12 + 4)·4/2.", "(12+4)*4//2", "La región bajo q entre 0 y 4 es un trapecio.", " litros"),
        ("=", "{F} Calcula el volumen entre 0 y 5 minutos con F(5) − F(0) con F(t) = 12t − t².", "(12*5-5*5)-(12*0-0*0)", "F(5) = 60 − 25 y F(0) = 0.", " litros"),
        ("=", "{F} Entre 0 y 4 minutos con n = 2 (Δt = 2), calcula la suma izquierda: 2·(12 + 8).", "2*(12+8)", "Alturas q(0) y q(2), ancho 2.", " litros"),
        ("=", "{F} Entre 0 y 4 minutos con n = 2 (Δt = 2), calcula la suma derecha: 2·(8 + 4).", "2*(8+4)", "Alturas q(2) y q(4), ancho 2.", " litros"),
        ("abc", "{F} Entre 0 y 4 minutos el volumen exacto es 32 L y las sumas con n = 2 son 40 y 24. Como q decrece, ¿qué ocurre con ellas?", "La izquierda sobreestima (40) y la derecha subestima (24)", "La izquierda subestima y la derecha sobreestima", "Ambas dan exactamente 32", "En una función decreciente el extremo izquierdo es el más alto."),
        ("=", "{F} Calcula el volumen entre 1 y 4 minutos: F(4) − F(1) = (12·4 − 4²) − (12·1 − 1²).", "(12*4-4*4)-(12*1-1*1)", "Se evalúa F en 4 y se resta F en 1.", " litros"),
        ("ab", "{F} El modelo da 36 L y se midieron 34 L. ¿Qué decisión es razonable?", "Aceptar el modelo con error de 2 L y ajustarlo si el error se repite o supera la tolerancia", "Descartar el modelo porque no da 34 exacto", "Un error pequeño no invalida el modelo, pero conviene revisarlo con más mediciones."),
        ("{F} ¿Hasta qué minuto vale el modelo q(t) = 12 − 2t como caudal?", "Hasta t = 6, porque después daría caudal negativo", "q(6) = 0 y para t mayor el valor resulta negativo."),
        ("=", "{F} Entre 0 y 4 minutos con n = 4 (Δt = 1), la suma izquierda es 12 + 10 + 8 + 6.", "12+10+8+6", "Cada altura es q(0), q(1), q(2) y q(3), con ancho 1.", " litros"),
        ("abc", "{F} Entre 0 y 4 minutos las sumas izquierdas son 40 con n = 2 y 36 con n = 4. ¿Qué ocurre al aumentar n?", "Se acerca al volumen exacto de 32", "Se aleja de 32", "No cambia", "36 está más cerca de 32 que 40."),
    ],
    ctx=("=", "Una fábrica de ejemplo produce p(t) = 4t unidades por hora al comenzar su turno, con t entre 0 y 5 horas. ¿Cuántas unidades produce en total? Es el área del triángulo bajo p, de base 5 y altura 20.", "5*20//2", "El total acumulado es el área bajo la tasa de producción.", " unidades"),
    sc=[
        ("En Matemática: ¿qué representa el área bajo la curva de una tasa?", "El total acumulado, como litros o unidades", "La tasa por el tiempo da la cantidad acumulada."),
        ("¿Qué es el rango de validez de un modelo?", "Los valores de la variable donde el modelo sirve", "Fuera de él puede dar resultados sin sentido."),
        ("=", "Si el modelo da 36 y la medición es 34, ¿cuánto vale el error?", "36-34", "Es la diferencia entre el modelo y la medición."),
    ],
    op=("Se modela el consumo de agua de una familia de ejemplo con c(t) = 5 + t litros por minuto durante una ducha de 4 minutos. Calcula el total con la antiderivada 5t + t²/2 y con el área del trapecio, interpreta el resultado con unidades, y compáralo con una medición de ejemplo de 28 litros decidiendo si ajustarías el modelo.",
        "Antiderivada: F(4) − F(0) = (20 + 8) − 0 = 28. Trapecio: (5 + 9)·4/2 = 28. Total: 28 litros de agua. La medición de 28 litros coincide con el modelo, así que no hace falta ajustarlo; igual conviene probarlo con más mediciones.",
        ["calcula el total por dos vías", "interpreta con unidades", "decide si ajustar con un criterio"],
        ["hoja con dos cálculos, interpretación y decisión"],
        ["omitir las unidades", "no comparar con la medición", "usar el modelo fuera del rango sin avisar"],
        "Pregunta: «¿qué significa el 28?». Debe decir litros acumulados en 4 minutos."),
    reinforce="Con q(t) = 12 − 2t, calcula el volumen entre t = 2 y t = 6 con F(t) = 12t − t².",
    extend="Propón un modelo de caudal que no pueda ser negativo en todo el intervalo de interés y explica cómo cambia el rango de validez.",
)
