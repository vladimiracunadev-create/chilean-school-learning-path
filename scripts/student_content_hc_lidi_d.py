"""Límites, derivadas e integrales (electivo 3.º y 4.º medio HC): OAC-04, primera y segunda derivada, crecimiento, concavidad y extremos, clases 1 a 4."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, cuaderno y calculadora simple. Todas las funciones y datos están escritos en cada ejercicio y son de ejemplo, inventados para este cuaderno; no necesitas internet. "
             "Un graficador digital es opcional y sirve para comprobar la forma de la curva, pero la tabla de signos y la derivada se escriben a mano.")
build = make_build(MATERIALS)

O4 = "MA-LIDI-3y4-OAC-04"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (funciones de ejemplo y reglas que se usan). Reglas: la derivada de una constante es 0; la de xⁿ es n·xⁿ⁻¹; la de c·f es c·f'; la de una suma es la suma de las derivadas. "
     "f(x) = x³ + 2x² − 5x + 4, g(x) = 4x² − 6x + 1 y h(x) = x⁴.")
build(
    O4, 1, F,
    use="Aprenderé a calcular la primera y la segunda derivada de funciones polinómicas con reglas. Sirve para obtener rápido la pendiente de la tangente y cómo cambia esa pendiente.",
    prior=["Sé que la derivada mide la rapidez instantánea de cambio.", "Sé operar con potencias.", "Sé expandir productos de binomios."],
    explain=[
        "Derivar con la definición es lento, por eso se usan reglas que salen de ella. La derivada de una constante es 0. La de xⁿ es n·xⁿ⁻¹: se baja el exponente multiplicando y se resta 1 al exponente. La derivada de un múltiplo c·f es c·f', y la de una suma es la suma de las derivadas. Por ejemplo, la derivada de 4x² es 4·2x = 8x.",
        "Con f(x) = x³ + 2x² − 5x + 4 se deriva término a término: 3x² + 4x − 5 + 0. Así f'(x) = 3x² + 4x − 5. Con g(x) = 4x² − 6x + 1 se obtiene g'(x) = 8x − 6, y con h(x) = x⁴ se obtiene h'(x) = 4x³. Se evalúa en un punto reemplazando x: g'(2) = 16 − 6 = 10.",
        "La segunda derivada es la derivada de la derivada y se escribe f''(x). Con f'(x) = 3x² + 4x − 5 se tiene f''(x) = 6x + 4. La segunda derivada mide cómo cambia la rapidez de cambio: si f' es la rapidez, f'' dice si esa rapidez aumenta o disminuye. Si una función es un producto como (x + 2)(x − 1), conviene expandirla antes de derivar.",
    ],
    vocab=[("regla de la potencia", "la derivada de xⁿ es n·xⁿ⁻¹"), ("primera derivada", "f', la rapidez de cambio de f"), ("segunda derivada", "f'', la derivada de f'"), ("término", "cada sumando de un polinomio"), ("coeficiente", "número que multiplica a la variable")],
    worked=[
        ("Derivar un polinomio término a término", "Halla la derivada de p(x) = 5x³ − 2x² + 7x − 9.",
         ["Se deriva cada término: 5·3x² = 15x², −2·2x = −4x, 7 y la constante −9 da 0.", "Se suman los resultados."],
         "p'(x) = 15x² − 4x + 7"),
        ("Primera y segunda derivada", "Halla q'(x) y q''(x) para q(x) = x⁴ − 3x².",
         ["q'(x) = 4x³ − 6x.", "q''(x) = 12x² − 6, derivando de nuevo."],
         "q'(x) = 4x³ − 6x y q''(x) = 12x² − 6"),
    ],
    mistakes=[("Derivar 5x³ como 5·3·x³ = 15x³.", "Se olvida restar 1 al exponente.", "Baja el exponente y réstale 1: 15x²."),
              ("Derivar una constante como si fuera la variable: 7 se vuelve 7x.", "Se confunde constante con término en x.", "La derivada de una constante es 0.")],
    T=[
        ("abc", "{F} ¿Cuál es la derivada de x⁴ según la regla de la potencia?", "4x³", "x³", "4x⁴", "Se baja el 4 como factor y se resta 1 al exponente."),
        ("=", "{F} Con g'(x) = 8x − 6, calcula g'(3).", "8*3-6", "Se reemplaza x por 3."),
        ("{F} ¿Cuánto vale la derivada de la constante 7?", "0", "Una constante no cambia, así que su derivada es cero."),
        ("Halla k'(x) para k(x) = 2x³ − 5x² + x − 8.", "6x² − 10x + 1", "Se deriva término a término: 6x², −10x, 1 y la constante −8 da 0."),
        ("Halla m'(x) para m(x) = 3x⁴ − 2x + 6.", "12x³ − 2", "La derivada de 3x⁴ es 12x³, la de −2x es −2 y la de 6 es 0."),
        ("Halla k''(x), derivando k'(x) = 6x² − 10x + 1.", "12x − 10", "La derivada de 6x² es 12x, la de −10x es −10 y la de 1 es 0."),
        ("=", "{F} Calcula f'(2) con f'(x) = 3x² + 4x − 5.", "3*2*2+4*2-5", "Se reemplaza x por 2: 12 + 8 − 5."),
        ("{F} ¿Cuánto vale g''(x)?", "8", "g'(x) = 8x − 6 y su derivada es 8."),
        ("=", "{F} Calcula h'(2) con h'(x) = 4x³.", "4*2*2*2", "4·2³ = 4·8."),
        ("abc", "Un estudiante deriva 5x³ y escribe 15x³. ¿Cuál es el error?", "No restó 1 al exponente: es 15x²", "No multiplicó por 5", "Debió escribir 5x²", "La regla de la potencia baja el exponente y le resta 1."),
        ("ab", "¿Qué indica la segunda derivada f''?", "Cómo cambia la rapidez de cambio de f", "La pendiente de f en un punto", "La pendiente de f en un punto es f'; f'' es la derivada de f'."),
        ("Halla la derivada de p(x) = (x + 4)(x − 1), expandiendo primero.", "2x + 3", "p(x) = x² + 3x − 4, y su derivada es 2x + 3."),
        ("Halla r''(x) para r(x) = 2x⁵ − x².", "40x³ − 2", "r'(x) = 10x⁴ − 2x y su derivada es 40x³ − 2."),
    ],
    ctx=("=", "La altura de un cohete de ejemplo es s(t) = t³ − 3t² + 10 metros a los t segundos, con s'(t) = 3t² − 6t. ¿Cuál es su rapidez a los 4 segundos?", "3*4*4-6*4", "Se evalúa s'(4) = 48 − 24.", " m/s"),
    sc=[
        ("En Matemática: ¿qué dice la regla de la potencia?", "La derivada de xⁿ es n·xⁿ⁻¹", "Se baja el exponente y se resta 1."),
        ("¿Qué es la segunda derivada de una función?", "La derivada de su primera derivada", "Se deriva la función y luego se deriva su derivada."),
        ("=", "Si f'(x) = 6x + 1, ¿cuánto vale f'(3)?", "6*3+1", "Se reemplaza x por 3."),
    ],
    op=("Para u(x) = x³ − 6x² + 5x + 2, halla u'(x) y u''(x). Calcula u'(1) y u''(1) e interpreta con una frase cada resultado (pendiente de la tangente y cómo cambia esa pendiente).",
        "u'(x) = 3x² − 12x + 5 y u''(x) = 6x − 12. u'(1) = 3 − 12 + 5 = −4: la tangente en x = 1 baja con pendiente −4. u''(1) = −6: la pendiente está disminuyendo en x = 1.",
        ["deriva término a término con la regla de la potencia", "evalúa ambas derivadas en x = 1", "interpreta cada resultado con una frase"],
        ["hoja con dos derivadas, dos evaluaciones y dos frases"],
        ["no restar 1 al exponente", "derivar la constante como variable", "no interpretar el signo"],
        "Pregunta: «¿qué mide u'(1)?». Debe decir pendiente de la tangente."),
    reinforce="Halla la primera y la segunda derivada de v(x) = 2x³ − x² + 4x y evalúa ambas en x = 1.",
    extend="Explica por qué la derivada de una función lineal es constante y su segunda derivada es 0.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (funciones de ejemplo). f(x) = x³ − 12x + 5, con f'(x) = 3x² − 12 = 3(x − 2)(x + 2). "
     "g(x) = −x² + 6x. h(x) = x² − 4x + 7, con h'(x) = 2x − 4.")
build(
    O4, 2, F,
    use="Aprenderé a decidir dónde una función crece o decrece usando el signo de la primera derivada y a encontrar máximos y mínimos locales con una tabla de signos. Sirve para resolver problemas de aumento y disminución.",
    prior=["Sé derivar polinomios.", "Sé resolver ecuaciones cuadráticas simples.", "Sé evaluar el signo de una expresión."],
    explain=[
        "Si f'(x) > 0 en un intervalo, la función crece allí; si f'(x) < 0, decrece. Los puntos donde f'(x) = 0 se llaman puntos críticos: la tangente es horizontal. Con f(x) = x³ − 12x + 5, f'(x) = 3x² − 12 se anula en x = −2 y en x = 2. Estos dos puntos dividen la recta en tres intervalos.",
        "Se hace una tabla de signos: se elige un valor de prueba en cada intervalo y se evalúa f'. En x = −3, f'(−3) = 15 es positiva y f crece. En x = 0, f'(0) = −12 es negativa y f decrece. En x = 3, f'(3) = 15 es positiva y f crece. Entonces f crece para x < −2, decrece entre −2 y 2, y crece para x > 2.",
        "Si f' cambia de positivo a negativo en un punto crítico, hay un máximo local; si cambia de negativo a positivo, hay un mínimo local. En x = −2 hay un máximo local y f(−2) = 21; en x = 2 hay un mínimo local y f(2) = −11. No todo punto con f' = 0 es máximo o mínimo: si f' no cambia de signo, no lo es.",
    ],
    vocab=[("punto crítico", "punto donde la derivada vale 0"), ("tabla de signos", "tabla que muestra el signo de f' en cada intervalo"), ("máximo local", "punto más alto en su entorno"), ("mínimo local", "punto más bajo en su entorno"), ("valor de prueba", "número de un intervalo que se evalúa para conocer el signo")],
    worked=[
        ("Tabla de signos", "Para m(x) = x² − 6x + 1, con m'(x) = 2x − 6, estudia crecimiento.",
         ["m'(x) = 0 en x = 3. Prueba en x = 0: m'(0) = −6, negativo. Prueba en x = 4: m'(4) = 2, positivo.", "La función decrece antes de 3 y crece después."],
         "Decrece para x < 3, crece para x > 3, y hay un mínimo local en x = 3"),
        ("Máximo o mínimo local", "Con m(x) = x² − 6x + 1, calcula el valor del mínimo.",
         ["En x = 3: m(3) = 9 − 18 + 1.", "El resultado es −8."],
         "El mínimo local vale −8 en x = 3"),
    ],
    mistakes=[("Decir que todo punto con f'(x) = 0 es máximo o mínimo.", "Falta comprobar que la derivada cambia de signo.", "Haz la tabla de signos antes de concluir."),
              ("Concluir que f crece porque f es positiva.", "Se confunde el signo de f con el de f'.", "El crecimiento depende del signo de f', no de f.")],
    T=[
        ("abc", "Si f'(x) > 0 en un intervalo, ¿qué hace f en ese intervalo?", "Crece", "Decrece", "Se mantiene constante", "Una derivada positiva significa pendiente positiva y la función sube."),
        ("=", "{F} Calcula f'(4).", "3*4*4-12", "f'(4) = 3·16 − 12."),
        ("Resuelve 2x² − 18 = 0.", "x = 3 y x = −3", "2x² = 18 lleva a x² = 9, que tiene dos soluciones."),
        ("abc", "{F} Se sabe que f'(1) = −9. ¿Qué hace f cerca de x = 1, que está entre −2 y 2?", "Decrece, porque su derivada es negativa allí", "Crece", "Tiene un máximo", "El signo negativo de f'(1) indica pendiente negativa."),
        ("abc", "{F} ¿Qué hace f cerca de x = 5, donde f'(5) = 63?", "Crece", "Decrece", "Tiene un mínimo en 5", "f'(5) es positiva y la función sube."),
        ("ab", "{F} En x = −2, f' cambia de positivo a negativo. ¿Qué hay allí?", "Un máximo local", "Un mínimo local", "Si la función pasa de subir a bajar, el punto es un máximo local."),
        ("{F} Para g(x) = −x² + 6x, halla g'(x) y el punto crítico.", "g'(x) = −2x + 6; x = 3", "−2x + 6 = 0 lleva a x = 3."),
        ("{F} ¿En qué intervalos crece y decrece g?", "Crece para x < 3 y decrece para x > 3", "g'(0) = 6 es positiva y g'(4) = −2 es negativa."),
        ("=", "{F} Calcula g(3), el valor máximo de g.", "-3*3+6*3", "g(3) = −9 + 18."),
        ("abc", "{F} Con h'(x) = 2x − 4 y h'(2) = 0, ¿qué hay en x = 2?", "Un mínimo local, porque h' pasa de negativa a positiva", "Un máximo local", "Un punto donde h vale 0", "h'(1) = −2 y h'(3) = 2: la función baja y luego sube."),
        ("ab", "Si f'(a) = 0, ¿hay siempre un máximo o un mínimo en a?", "No: hace falta que la derivada cambie de signo", "Sí: siempre", "Es posible que f' valga 0 sin cambiar de signo, y entonces no hay extremo."),
        ("=", "{F} Calcula f(−3), un valor a la izquierda del máximo local.", "(-3)*(-3)*(-3)-12*(-3)+5", "−27 + 36 + 5."),
        ("{F} Calcula f(3), un valor a la derecha del mínimo local.", "−4", "27 − 36 + 5 = −4."),
    ],
    ctx=("=", "La ganancia de un puesto de ejemplo, en miles de pesos, es G(p) = −p² + 40p − 100 según el precio p. Como G'(p) = −2p + 40, ¿para qué precio p es G'(p) = 0 y la ganancia es máxima?", "40//2", "Se resuelve −2p + 40 = 0; G' pasa de positiva a negativa.", " (en las unidades del precio)"),
    sc=[
        ("En Matemática: ¿qué es un punto crítico?", "Un punto donde la derivada vale 0", "Allí la tangente es horizontal, con pendiente cero."),
        ("¿Cómo se sabe que hay un máximo local en un punto crítico?", "Porque f' cambia de positivo a negativo", "La función pasa de subir a bajar."),
        ("¿Para qué sirve la tabla de signos de f'?", "Para saber dónde f crece y dónde decrece", "El signo de f' en cada intervalo da el comportamiento."),
    ],
    op=("Con la función w(x) = x² − 8x + 3, cuya derivada es w'(x) = 2x − 8, haz una tabla de signos con valores de prueba, escribe dónde crece y decrece, y calcula el valor del extremo local. Indica si es máximo o mínimo y por qué.",
        "w'(x) = 0 en x = 4. Prueba x = 0: w'(0) = −8 (decrece). Prueba x = 5: w'(5) = 2 (crece). Hay un mínimo local en x = 4, con w(4) = 16 − 32 + 3 = −13. Es mínimo porque w' pasa de negativa a positiva.",
        ["encuentra el punto crítico y hace la tabla", "determina crecimiento y decrecimiento", "calcula el valor y justifica máximo o mínimo"],
        ["hoja con tabla de signos, intervalos y valor del extremo"],
        ["no elegir valores de prueba", "decir que es máximo sin mirar el cambio de signo", "calcular el valor de w' en vez de w"],
        "Pregunta: «¿qué signo tiene w' antes y después de 4?». Debe decir negativo y positivo."),
    reinforce="Con k(x) = x² − 10x, halla el punto crítico, la tabla de signos y el valor del extremo.",
    extend="Explica por qué en f(x) = x³ la derivada vale 0 en x = 0 pero no hay máximo ni mínimo allí.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (funciones de ejemplo). f(x) = x³ − 6x² + 9x + 1, con f'(x) = 3x² − 12x + 9 = 3(x − 1)(x − 3) y f''(x) = 6x − 12. "
     "g(x) = x⁴, con g''(x) = 12x². h(x) = −x² + 4x, con h''(x) = −2.")
build(
    O4, 3, F,
    use="Aprenderé a usar la segunda derivada para estudiar la concavidad, hallar puntos de inflexión y clasificar máximos y mínimos. Sirve para describir la forma completa de una curva.",
    prior=["Sé calcular f' y f''.", "Sé hacer una tabla de signos.", "Sé que f' = 0 da puntos críticos."],
    explain=[
        "La segunda derivada dice cómo se curva la gráfica. Si f''(x) > 0, la función es cóncava hacia arriba (forma de U) y la pendiente aumenta. Si f''(x) < 0, es cóncava hacia abajo (forma de ∩) y la pendiente disminuye. Con f''(x) = 6x − 12, la concavidad es hacia abajo para x < 2 y hacia arriba para x > 2.",
        "Un punto de inflexión es donde la gráfica cambia de concavidad, es decir, donde f'' cambia de signo. Se busca resolviendo f''(x) = 0 y comprobando el cambio de signo. En f, 6x − 12 = 0 da x = 2, y f'' pasa de negativa a positiva, así que hay inflexión en x = 2 con f(2) = 3. Si f''(a) = 0 pero no cambia de signo, como g(x) = x⁴ en 0, no hay inflexión.",
        "El criterio de la segunda derivada clasifica puntos críticos: si f'(a) = 0 y f''(a) > 0, hay un mínimo local; si f''(a) < 0, hay un máximo local; si f''(a) = 0, el criterio no decide y se usa la tabla de signos. En f: f'(1) = 0 y f''(1) = −6, máximo local con f(1) = 5; f'(3) = 0 y f''(3) = 6, mínimo local con f(3) = 1.",
    ],
    vocab=[("concavidad", "forma en que se curva la gráfica"), ("cóncava hacia arriba", "f'' positiva, forma de U"), ("cóncava hacia abajo", "f'' negativa, forma de ∩"), ("punto de inflexión", "punto donde cambia la concavidad"), ("criterio de la segunda derivada", "regla que clasifica un punto crítico con el signo de f''")],
    worked=[
        ("Clasificar un punto crítico", "Para p(x) = x² − 4x, con p'(2) = 0 y p''(x) = 2, clasifica x = 2.",
         ["p''(2) = 2 es positiva.", "Por el criterio, es un mínimo local."],
         "Hay un mínimo local en x = 2"),
        ("Hallar una inflexión", "Para q(x) = x³ − 3x² con q''(x) = 6x − 6, halla el punto de inflexión.",
         ["6x − 6 = 0 lleva a x = 1.", "q'' es negativa antes de 1 y positiva después, así que cambia de signo."],
         "Hay un punto de inflexión en x = 1"),
    ],
    mistakes=[("Decir que hay inflexión siempre que f''(a) = 0.", "Se omite el cambio de signo.", "Comprueba el signo de f'' a ambos lados."),
              ("Confundir f'' > 0 con función creciente.", "f'' habla de concavidad y no de crecimiento.", "Usa f' para crecer o decrecer y f'' para la concavidad.")],
    T=[
        ("abc", "Si f''(x) > 0 en un intervalo, ¿cómo es la gráfica de f allí?", "Cóncava hacia arriba, con forma de U", "Cóncava hacia abajo", "Una recta", "Una segunda derivada positiva indica que la pendiente aumenta."),
        ("=", "{F} Calcula f''(4) con f''(x) = 6x − 12.", "6*4-12", "Se reemplaza x por 4."),
        ("Si k''(x) = 6x − 18, ¿para qué x se anula k''?", "x = 3", "6x = 18 lleva a x = 3."),
        ("abc", "Con k''(x) = 6x − 18, al pasar por x = 3, k'' cambia de negativa a positiva. ¿Qué ocurre allí?", "Hay un punto de inflexión", "Hay un máximo local", "Hay un mínimo local", "El cambio de signo de f'' indica cambio de concavidad."),
        ("ab", "{F} ¿Cómo es el signo de f''(0) y qué indica?", "Negativo: la gráfica es cóncava hacia abajo", "Positivo: la gráfica es cóncava hacia arriba", "f''(0) = −12, que es negativo."),
        ("Halla los puntos críticos de t(x) = x³ − 27x, con t'(x) = 3x² − 27.", "x = 3 y x = −3", "3x² = 27 lleva a x² = 9."),
        ("Para t(x) = x³ − 27x, t''(x) = 6x. Calcula t''(−3) y decide qué hay en x = −3.", "−18, máximo local", "t''(−3) = −18 es negativa, así que la curva se abre hacia abajo."),
        ("Para t(x) = x³ − 27x, t''(x) = 6x. Calcula t''(3) y decide qué hay en x = 3.", "18, mínimo local", "t''(3) = 18 es positiva, así que la curva se abre hacia arriba."),
        ("=", "Calcula t(−3), el valor del máximo local de t(x) = x³ − 27x.", "(-3)*(-3)*(-3)-27*(-3)", "−27 + 81."),
        ("ab", "{F} Con g(x) = x⁴, g''(0) = 0. ¿Hay inflexión en x = 0?", "No: g'' = 12x² no cambia de signo", "Sí: porque g''(0) = 0", "g'' es positiva a ambos lados de 0, así que la concavidad no cambia."),
        ("abc", "{F} Para h(x) = −x² + 4x, h''(x) = −2 y el punto crítico es x = 2. ¿Qué indica el criterio de la segunda derivada?", "Máximo local en x = 2", "Mínimo local en x = 2", "Punto de inflexión en x = 2", "h'' negativa en un punto crítico indica máximo local."),
        ("Para t(x) = x³ − 27x, con t''(x) = 6x, ¿en qué x hay punto de inflexión?", "x = 0, donde t'' pasa de negativa a positiva", "6x = 0 da x = 0, y t'' cambia de signo allí."),
        ("abc", "Un estudiante dice que como f''(2) = 0 hay inflexión. ¿Qué falta comprobar?", "Que f'' cambie de signo a cada lado de x = 2", "Que f(2) sea cero", "Nada más", "Una segunda derivada nula no basta sin el cambio de signo."),
    ],
    ctx=("abc", "La altura de agua de un depósito de ejemplo es A(t) = t³ − 6t² + 9t + 1 centímetros a los t minutos, con A'(t) = 3t² − 12t + 9 y A''(t) = 6t − 12. ¿En qué instante la rapidez de cambio A' alcanza su valor mínimo?", "t = 2 minutos, donde A'' cambia de negativa a positiva", "t = 1 minuto, donde A' vale 0", "t = 3 minutos, donde A' vale 0", "A'' = 0 en t = 2 y A' deja de decrecer para empezar a crecer, así que A' es mínima allí."),
    sc=[
        ("En Matemática: ¿qué es un punto de inflexión?", "Un punto donde la gráfica cambia de concavidad", "La segunda derivada cambia de signo en ese punto."),
        ("¿Qué indica f'' < 0 en un punto crítico?", "Un máximo local", "La curva se abre hacia abajo."),
        ("¿Qué indica f'' > 0 en un punto crítico?", "Un mínimo local", "La curva se abre hacia arriba."),
    ],
    op=("Para s(x) = x³ − 3x² − 9x + 5, con s'(x) = 3x² − 6x − 9 y s''(x) = 6x − 6, halla los puntos críticos, clasifícalos con el criterio de la segunda derivada y halla el punto de inflexión. Calcula el valor de s en cada punto importante.",
        "s'(x) = 3(x − 3)(x + 1) = 0 en x = −1 y x = 3. s''(−1) = −12 (máximo local, s(−1) = 10). s''(3) = 12 (mínimo local, s(3) = −22). Inflexión: s'' = 0 en x = 1, con cambio de signo; s(1) = −6.",
        ["halla los puntos críticos y los clasifica", "halla la inflexión y comprueba el cambio de signo", "calcula los valores de la función en esos puntos"],
        ["hoja con puntos críticos, clasificación, inflexión y valores"],
        ["confundir f' con f''", "no comprobar el cambio de signo", "calcular el valor de s'' en vez de s"],
        "Pregunta: «¿qué dice el signo de s'' en cada punto crítico?». Debe asociar signo con máximo o mínimo."),
    reinforce="Para t(x) = x³ − 3x, halla los puntos críticos con t'(x) = 3x² − 3, clasifícalos con t''(x) = 6x y halla la inflexión.",
    extend="Explica con un dibujo por qué una gráfica cóncava hacia arriba tiene tangentes que quedan por debajo de la curva.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (problemas de ejemplo). Problema 1: un rectángulo tiene perímetro 40 m, con ancho x y largo 20 − x; su área es A(x) = 20x − x², con A'(x) = 20 − 2x y A''(x) = −2. "
     "Problema 2: una huerta de ejemplo usa 60 m de malla en tres lados (el cuarto lado es un muro); con ancho x y largo 60 − 2x, el área es B(x) = 60x − 2x², con B'(x) = 60 − 4x y B''(x) = −4.")
build(
    O4, 4, F,
    use="Aprenderé a resolver problemas de máximos y mínimos con primera y segunda derivada y a justificar que la solución tiene sentido en el contexto. Sirve para decidir mejor en situaciones reales.",
    prior=["Sé derivar polinomios.", "Sé clasificar puntos críticos.", "Sé plantear fórmulas de áreas y perímetros."],
    explain=[
        "En un problema de optimización se quiere el mayor o el menor valor de una cantidad. Los pasos son cuatro: escribir la cantidad como función de una sola variable, indicar el dominio con sentido (por ejemplo, longitudes positivas), derivar e igualar a cero, y comprobar con la segunda derivada o una tabla de signos que sea un máximo o un mínimo. Al final se responde en palabras con unidades.",
        "En el problema 1, con A(x) = 20x − x², A'(x) = 20 − 2x = 0 da x = 10. Como A''(x) = −2 es negativa, es un máximo: el rectángulo de mayor área es el cuadrado de 10 m por 10 m, con 100 m². En el problema 2, B'(x) = 60 − 4x = 0 da x = 15, y el largo es 60 − 30 = 30. Como B'' = −4, es máximo y el área es 15·30 = 450 m².",
        "Hay que revisar que la respuesta tenga sentido: un valor como x = 35 daría un largo negativo (60 − 70), así que queda fuera del dominio. También es útil comparar con valores cercanos: B(14) = 448 y B(16) = 448 son menores que B(15) = 450. Herramientas digitales, como un graficador, permiten ver la parábola, pero el argumento con la derivada es el que se escribe.",
    ],
    vocab=[("optimización", "buscar el mayor o menor valor de una cantidad"), ("dominio con sentido", "valores de la variable que tienen sentido en el problema"), ("función objetivo", "la cantidad que se quiere maximizar o minimizar"), ("restricción", "condición que limita las variables"), ("justificar", "dar la razón que sostiene la conclusión")],
    worked=[
        ("Maximizar un área", "Con 36 m de cerca para un rectángulo, el área es C(x) = x(18 − x) = 18x − x². Halla las dimensiones de mayor área.",
         ["C'(x) = 18 − 2x = 0 da x = 9. C''(x) = −2 es negativa: es máximo.", "El otro lado es 18 − 9 = 9."],
         "Un cuadrado de 9 m por 9 m, con área 81 m²"),
        ("Revisar el dominio", "En el mismo problema, ¿qué valores de x tienen sentido?",
         ["Los lados deben ser positivos: x > 0 y 18 − x > 0.", "Por tanto, x está entre 0 y 18."],
         "x entre 0 y 18"),
    ],
    mistakes=[("Dar solo el x del punto crítico y no responder la pregunta.", "No se calcula el otro lado ni el área.", "Responde en palabras con todas las dimensiones y unidades."),
              ("Aceptar un punto crítico sin comprobar si es máximo o mínimo.", "f' = 0 también ocurre en mínimos.", "Usa f'' o la tabla de signos antes de concluir.")],
    T=[
        ("=", "{F} Calcula A(5) del problema 1, con A(x) = x(20 − x).", "5*(20-5)", "El largo es 15 y el ancho 5."),
        ("Con 44 m de malla para un rectángulo, el ancho es x y el largo 22 − x, de modo que C(x) = 22x − x² y C'(x) = 22 − 2x. ¿Para qué x se anula C'(x)?", "x = 11", "2x = 22 lleva a x = 11."),
        ("abc", "¿Qué conviene hacer primero en un problema de optimización?", "Escribir la cantidad a optimizar como función de una variable", "Derivar sin escribir la función", "Elegir un valor al azar", "Sin una función de una variable no se puede derivar ni comparar."),
        ("En el rectángulo de 44 m de malla (ancho x, largo 22 − x), ¿qué dimensiones dan el área máxima?", "11 m por 11 m", "x = 11 y el largo es 22 − 11 = 11."),
        ("=", "Calcula el área máxima del rectángulo de 44 m de malla, en m².", "11*11", "El área máxima es 11 por 11.", " m²"),
        ("ab", "{F} Como A''(x) = −2 es negativa, ¿qué indica?", "Que el punto crítico es un máximo", "Que el punto crítico es un mínimo", "Segunda derivada negativa significa cóncava hacia abajo y un máximo."),
        ("Una huerta usa 80 m de malla en tres lados (el cuarto es un muro): ancho x, largo 80 − 2x, área D(x) = 80x − 2x², con D'(x) = 80 − 4x. ¿Para qué x se anula D'(x)?", "x = 20", "4x = 80 lleva a x = 20."),
        ("=", "En la huerta con D(x) = 80x − 2x², calcula el largo 80 − 2x cuando x = 20.", "80-2*20", "El largo es 80 menos 40.", " m"),
        ("=", "Calcula el área máxima de esa huerta, en m², con 20 por 40.", "20*40", "Área = ancho por largo.", " m²"),
        ("abc", "{F} ¿Por qué hay que comprobar que x = 15 es un máximo y no un mínimo?", "Porque B'(x) = 0 también ocurre en mínimos y por eso se usa B''(15) = −4", "Porque 15 es un número grande", "Porque la derivada no sirve", "El signo de B'' decide si el punto crítico es máximo o mínimo."),
        ("ab", "En la huerta con largo 80 − 2x, ¿tiene sentido x = 45?", "No: daría un largo negativo, 80 − 90", "Sí: es un valor posible", "El largo 80 − 2x debe ser positivo, así que x debe ser menor que 40."),
        ("abc", "Un estudiante prueba x = 19 y x = 21 en la huerta con D(x) = 80x − 2x² y obtiene 798 en ambos, y dice que 798 es el máximo. ¿Qué responde mejor?", "Que x = 20 da 800, mayor que 798, y la derivada lo justifica", "Que tiene razón porque probó dos valores", "Que no se puede saber", "Probar dos valores no demuestra el máximo; la derivada sí."),
        ("Con 100 m de malla se cerca un rectángulo de área A(x) = x(50 − x). ¿Qué x da el área máxima?", "x = 25, un cuadrado de 25 m", "A'(x) = 50 − 2x = 0 da x = 25, y A'' = −2 asegura un máximo."),
    ],
    ctx=("=", "Una tienda de ejemplo tiene ingresos I(p) = −2p² + 60p miles de pesos según el precio p. Como I'(p) = −4p + 60 y I'' = −4, ¿qué precio p maximiza el ingreso?", "60//4", "Se resuelve −4p + 60 = 0, y I'' negativa indica máximo.", " (en las unidades del precio)"),
    sc=[
        ("En Matemática: ¿qué es la función objetivo en un problema de optimización?", "La cantidad que se quiere maximizar o minimizar", "Es la función que se deriva."),
        ("¿Qué se hace después de hallar un punto crítico?", "Se comprueba con f'' o con una tabla si es máximo o mínimo", "El punto crítico no basta para clasificar."),
        ("¿Cómo se responde un problema de optimización?", "En palabras, con todas las dimensiones y unidades", "La respuesta debe contestar la pregunta del enunciado."),
    ],
    op=("Se dispone de 24 m de malla para cercar un rectángulo. Con ancho x, el largo es 12 − x. Escribe la función de área, derívala, halla el punto crítico, verifica con la segunda derivada, revisa el dominio y responde con dimensiones y área máxima.",
        "A(x) = x(12 − x) = 12x − x². A'(x) = 12 − 2x = 0 en x = 6. A''(x) = −2 es negativa: máximo. Dominio: 0 < x < 12. Dimensiones: 6 m por 6 m, área máxima 36 m².",
        ["escribe la función y su dominio", "deriva, halla el punto crítico y lo clasifica", "responde con dimensiones y unidades"],
        ["hoja con función, derivada, clasificación, dominio y respuesta"],
        ["olvidar el dominio", "no usar la segunda derivada", "dar solo x"],
        "Pregunta: «¿cuánto mide el otro lado?». Debe calcular 12 − 6."),
    reinforce="Con 48 m de malla, escribe A(x) = x(24 − x), halla el máximo y responde con dimensiones.",
    extend="Explica por qué, entre los rectángulos de igual perímetro, el cuadrado tiene el área mayor, usando A'' y el dominio.",
)
