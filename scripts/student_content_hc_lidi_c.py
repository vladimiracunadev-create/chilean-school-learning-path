"""Límites, derivadas e integrales (electivo 3.º y 4.º medio HC): OAC-03, rapidez instantánea de cambio y ajuste de modelos, clases 1 a 5."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, cuaderno y calculadora simple para dividir y comparar. "
             "Todas las funciones, tablas y datos están escritos en cada ejercicio y son de ejemplo, inventados para este cuaderno; no necesitas internet. "
             "Un graficador o una hoja de cálculo son opcionales: sirven para ver la curva, no reemplazan el razonamiento escrito.")
build = make_build(MATERIALS)

O3 = "MA-LIDI-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (modelo de ejemplo). Un objeto avanza según s(t) = 5t² metros, con t en segundos: s(0) = 0, s(1) = 5, s(2) = 20, s(3) = 45. "
     "Además, s(1,5) = 11,25; s(1,1) = 6,05; s(1,01) = 5,1005 y s(2,1) = 22,05.")
build(
    O3, 1, F,
    use="Aprenderé a distinguir la rapidez media de la rapidez instantánea de cambio y a ver la segunda como lo que ocurre cuando los intervalos se hacen muy pequeños. Sirve para describir qué tan rápido cambia algo en un instante preciso.",
    prior=["Sé calcular un cociente entre cambios (por ejemplo, km por hora).", "Sé estimar un límite con una tabla.", "Sé evaluar funciones."],
    explain=[
        "La rapidez media de cambio de una función entre t = a y t = b es el cambio de la función dividido por el cambio de t: (s(b) − s(a))/(b − a). Con s(t) = 5t², entre 1 y 2 segundos es (20 − 5)/1 = 15 metros por segundo. Es un promedio de todo el intervalo; durante ese tiempo el objeto puede ir más lento o más rápido que 15.",
        "La rapidez instantánea en t = a responde cuánto cambia la función justo en ese instante. Se estima con rapideces medias en intervalos cada vez más pequeños que parten de a. Desde t = 1: entre 1 y 1,5 es 12,5; entre 1 y 1,1 es 10,5; entre 1 y 1,01 es 10,05. Los valores se acercan a 10, que es la rapidez instantánea en t = 1.",
        "En lenguaje de límites, la rapidez instantánea es el límite de las rapideces medias cuando el largo del intervalo tiende a 0. Se mide en las unidades de la función por las unidades de t, aquí metros por segundo. Una rapidez media es exacta para su intervalo; una instantánea solo se aproxima con tablas, y se confirma con álgebra.",
    ],
    vocab=[("rapidez media", "cambio de la función dividido por el cambio de la variable en un intervalo"), ("rapidez instantánea", "límite de las rapideces medias al achicarse el intervalo"), ("intervalo", "tramo entre dos valores de t"), ("tasa de cambio", "cuánto cambia una cantidad por cada unidad de otra"), ("m/s", "metros por segundo")],
    worked=[
        ("Calcular una rapidez media", "Con s(t) = 5t², halla la rapidez media entre t = 0 y t = 2.",
         ["s(0) = 0 y s(2) = 20, así que el cambio de posición es 20 − 0 = 20 m.", "El cambio de tiempo es 2 − 0 = 2 s, entonces 20/2 = 10."],
         "La rapidez media es 10 m/s"),
        ("Estimar una rapidez instantánea", "Con s(t) = 5t², estima la rapidez en t = 3 con las medias entre 3 y 3,1 (s(3,1) = 48,05) y entre 3 y 3,01 (s(3,01) = 45,3005).",
         ["Entre 3 y 3,1: (48,05 − 45)/0,1 = 30,5.", "Entre 3 y 3,01: (45,3005 − 45)/0,01 = 30,05, que se acerca a 30."],
         "La rapidez instantánea en t = 3 se acerca a 30 m/s"),
    ],
    mistakes=[("Decir que la rapidez media en [1; 2] es la rapidez en t = 1.", "Se confunde un promedio de intervalo con un instante.", "Achica el intervalo hacia t = 1 y observa a qué valor se acercan las medias."),
              ("Dividir mal: calcular (s(b) − s(a)) sin dividir por (b − a).", "Se olvida que la rapidez compara cambio con tiempo.", "Divide siempre el cambio de la función por el cambio de t.")],
    T=[
        ("=", "{F} Calcula s(2).", "5*2*2", "s(2) = 5·2² = 20."),
        ("=", "{F} Calcula la rapidez media entre t = 1 y t = 2, en m/s: (s(2) − s(1))/(2 − 1).", "(20-5)//(2-1)", "El cambio es 15 m en 1 s."),
        ("abc", "¿Qué mide la rapidez media en un intervalo?", "El cambio de la función dividido por el tiempo transcurrido", "El valor de la función al final del intervalo", "La rapidez en el último instante del intervalo", "La rapidez media es un cociente entre cambios y resume todo el intervalo."),
        ("=", "{F} Calcula la rapidez media entre t = 2 y t = 3, en m/s.", "(45-20)//(3-2)", "El cambio es 25 m en 1 s."),
        ("ab", "{F} ¿Por qué la rapidez media entre t = 1 y t = 2 no es la rapidez en el instante t = 1?", "Porque promedia todo el intervalo y la rapidez cambia dentro de él", "Porque el objeto está quieto en t = 1", "En el modelo la rapidez aumenta con el tiempo, por lo que un promedio difiere de un instante."),
        ("{F} Con s(2,5) = 31,25, calcula la rapidez media entre t = 2 y t = 2,5, en m/s.", "22,5", "Se divide el cambio de posición entre el tiempo: (31,25 − 20)/0,5 = 11,25/0,5."),
        ("{F} Con s(2,01) = 20,2005, calcula la rapidez media entre t = 2 y t = 2,01, en m/s.", "20,05", "Se divide el cambio de posición entre el tiempo: (20,2005 − 20)/0,01 = 0,2005/0,01."),
        ("{F} Con s(3,5) = 61,25, calcula la rapidez media entre t = 3 y t = 3,5, en m/s.", "32,5", "Se divide el cambio de posición entre el tiempo: (61,25 − 45)/0,5 = 16,25/0,5."),
        ("abc", "{F} Las rapideces medias desde t = 1 son 12,5; 10,5 y 10,05 en intervalos cada vez más cortos. ¿A qué valor se acercan?", "10", "5", "12,5", "Los valores bajan acercándose a 10 cuando el intervalo se achica."),
        ("ab", "{F} Las rapideces medias desde t = 1 en intervalos cada vez más cortos se acercan a 10 m/s. ¿Qué representa ese valor?", "La rapidez instantánea del objeto en t = 1", "La rapidez media entre t = 0 y t = 2", "Es el límite de las medias al achicar el intervalo, es decir, la rapidez en el instante."),
        ("abc", "Un estudiante dice que la rapidez instantánea es la media en un intervalo de 1 segundo. ¿Qué respuesta es mejor?", "Solo se aproxima; la instantánea es el límite cuando el intervalo se hace muy pequeño", "Es exacta siempre", "Es igual al tiempo", "Un intervalo de 1 s sigue siendo un promedio; hace falta achicarlo."),
        ("{F} Con s(2,1) = 22,05, calcula la rapidez media entre t = 2 y t = 2,1, en m/s.", "20,5", "Se divide el cambio de posición entre el tiempo: (22,05 − 20)/0,1 = 2,05/0,1."),
        ("abc", "{F} Las medias desde t = 1 y desde t = 2 con intervalos de 0,1 s son 10,5 y 20,5 m/s. ¿Qué se concluye del objeto?", "Va más rápido cerca de t = 2 que cerca de t = 1", "Va más lento cerca de t = 2", "Va a la misma rapidez siempre", "La rapidez aumenta con el tiempo en este modelo."),
    ],
    ctx=("=", "Un carrito de ejemplo recorre d(t) = 2t² metros en t segundos, con d(3) = 18 y d(4) = 32. ¿Cuál es su rapidez media entre los 3 y los 4 segundos?", "(32-18)//(4-3)", "El cambio de distancia es 14 m en 1 s.", " m/s"),
    sc=[
        ("En Matemática: ¿qué es la rapidez media de cambio?", "El cambio de la función dividido por el cambio de la variable", "Es un promedio de todo el intervalo."),
        ("¿Cómo se estima la rapidez instantánea con tablas?", "Con rapideces medias en intervalos cada vez más cortos", "Si las medias se acercan a un valor, ese es el estimado."),
        ("=", "Si una función cambia 12 unidades en 3 segundos, ¿cuál es su rapidez media en unidades por segundo?", "12//3", "Se divide el cambio por el tiempo transcurrido."),
    ],
    op=("Con el modelo s(t) = 5t², estima la rapidez instantánea en t = 4. Calcula las rapideces medias entre 4 y 4,1 (s(4,1) = 84,05) y entre 4 y 4,01 (s(4,01) = 80,4005), con s(4) = 80, y explica con una frase qué significa el valor al que se acercan.",
        "Entre 4 y 4,1: (84,05 − 80)/0,1 = 40,5. Entre 4 y 4,01: (80,4005 − 80)/0,01 = 40,05. Se acercan a 40, así que la rapidez instantánea en t = 4 es de 40 m/s: justo a los 4 segundos el objeto avanza a 40 metros por cada segundo.",
        ["calcula las dos rapideces medias con el cociente correcto", "estima el valor al que se acercan", "interpreta el resultado con unidades"],
        ["hoja con dos cálculos, estimación e interpretación"],
        ["no dividir por el largo del intervalo", "tomar la media como la instantánea", "olvidar las unidades"],
        "Pregunta: «¿qué pasa con las medias al achicar el intervalo?». Debe decir que se acercan a 40."),
    reinforce="Con s(t) = 5t² y s(0,5) = 1,25, calcula la rapidez media entre t = 0 y t = 0,5 y compárala con la media entre 0 y 1.",
    extend="Explica por qué la rapidez media entre dos instantes puede ser igual a cero aunque el objeto se haya movido durante el intervalo.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (modelo de ejemplo). f(x) = x². Puntos de la parábola: (1; 1), (1,01; 1,0201), (1,1; 1,21), (1,5; 2,25) y (2; 4). "
     "Tabla del cociente (f(1 + h) − f(1))/h: con h = 1 da 3; h = 0,5 da 2,5; h = 0,1 da 2,1; h = 0,01 da 2,01.")
build(
    O3, 2, F,
    use="Aprenderé a representar la rapidez instantánea de dos maneras: como pendiente de la recta tangente en una gráfica y como límite del cociente incremental en una tabla o fórmula. Sirve para conectar gráfico, tabla y álgebra.",
    prior=["Sé calcular la pendiente de una recta por dos puntos.", "Sé estimar límites con tablas.", "Sé evaluar f(x) = x²."],
    explain=[
        "Una recta secante corta una curva en dos puntos. Su pendiente es la rapidez media de cambio entre esos puntos: (f(b) − f(a))/(b − a). Si el segundo punto es b = a + h, la pendiente se escribe (f(a + h) − f(a))/h y se llama cociente incremental. Para f(x) = x² en a = 1 con h = 1 es (4 − 1)/1 = 3.",
        "Al hacer h cada vez más pequeña, el segundo punto se acerca al primero y la secante se acerca a la recta tangente, que toca la curva en un punto con su misma dirección. Las pendientes 3; 2,5; 2,1; 2,01 se acercan a 2. Ese 2 es la pendiente de la tangente en x = 1 y la rapidez instantánea de cambio de f en 1.",
        "A ese límite se le llama derivada de f en a: f'(a) es el límite de (f(a + h) − f(a))/h cuando h tiende a 0. No se puede reemplazar h por 0 desde el inicio, porque queda 0/0; primero se simplifica. Con f(x) = x²: ((1 + h)² − 1)/h = (2h + h²)/h = 2 + h, y cuando h tiende a 0 el resultado es 2.",
    ],
    vocab=[("recta secante", "recta que corta la curva en dos puntos"), ("recta tangente", "recta que toca la curva en un punto con su misma dirección"), ("cociente incremental", "(f(a + h) − f(a))/h"), ("derivada en a", "límite del cociente incremental cuando h tiende a 0"), ("pendiente", "cuánto sube la recta por cada unidad horizontal")],
    worked=[
        ("Pendiente de una secante", "Halla la pendiente de la secante a f(x) = x² por (2; 4) y (3; 9).",
         ["Cambio vertical: 9 − 4 = 5.", "Cambio horizontal: 3 − 2 = 1, y 5/1 = 5."],
         "La pendiente es 5"),
        ("Pasar de la secante a la tangente", "Con f(x) = x² en a = 2, simplifica ((2 + h)² − 4)/h y halla su límite cuando h tiende a 0.",
         ["(2 + h)² = 4 + 4h + h², así que el numerador es 4h + h².", "Se divide por h: 4 + h, que tiende a 4."],
         "La pendiente de la tangente en x = 2 es 4"),
    ],
    mistakes=[("Reemplazar h por 0 al inicio del cociente incremental.", "Resulta 0/0, que no es un valor.", "Simplifica primero y recién después deja que h tienda a 0."),
              ("Calcular la pendiente de la secante restando mal: (x₂ − x₁)/(y₂ − y₁).", "Se invierte el cociente.", "La pendiente es cambio vertical dividido por cambio horizontal.")],
    T=[
        ("=", "{F} Calcula f(3).", "3*3", "f(3) = 3² = 9."),
        ("=", "{F} Calcula la pendiente de la secante por (1; 1) y (2; 4).", "(4-1)//(2-1)", "Cambio vertical 3 dividido por cambio horizontal 1."),
        ("abc", "¿Qué es una recta secante a una curva?", "Una recta que corta la curva en dos puntos", "Una recta que toca la curva en un solo punto con su misma dirección", "Una recta horizontal que pasa por el origen", "La secante corta en dos puntos; la que toca con la misma dirección es la tangente."),
        ("Sobre la parábola y = x², calcula la pendiente de la secante por (2; 4) y (2,5; 6,25).", "4,5", "(6,25 − 4)/(2,5 − 2) = 2,25/0,5."),
        ("Sobre la parábola y = x², calcula la pendiente de la secante por (2; 4) y (2,1; 4,41).", "4,1", "(4,41 − 4)/(2,1 − 2) = 0,41/0,1."),
        ("abc", "{F} Al acercarse el segundo punto a (1; 1), ¿a qué valor se acercan las pendientes 3; 2,5; 2,1 y 2,01?", "2", "3", "1", "Las pendientes van bajando y se acercan a 2."),
        ("=", "{F} Calcula el cociente incremental de f en a = 3 con h = 1, es decir (f(4) − f(3))/1.", "(16-9)//1", "f(4) = 16, f(3) = 9 y h = 1."),
        ("{F} Simplifica ((5 + h)² − 25)/h para h distinto de 0.", "10 + h", "(25 + 10h + h² − 25)/h = (10h + h²)/h = 10 + h."),
        ("{F} Con el resultado 10 + h, ¿a qué valor tiende cuando h tiende a 0?", "10", "Al achicar h, el término h se acerca a 0 y queda 10."),
        ("ab", "{F} ¿Qué representa el valor 2 en la gráfica de f(x) = x² en el punto (1; 1)?", "La pendiente de la recta tangente en ese punto", "La altura de la parábola en x = 1", "La altura es f(1) = 1; el 2 es el límite de las pendientes de las secantes."),
        ("abc", "¿Por qué la tabla del cociente se hace con h cada vez más pequeña y no con h = 0?", "Porque con h = 0 queda 0/0, que no tiene valor", "Porque 0 no es un número", "Porque la tangente no existe", "El cociente incremental no está definido en h = 0, por eso se estudia el límite."),
        ("Con f(x) = x² en a = 3, simplifica ((3 + h)² − 9)/h y halla su límite cuando h tiende a 0.", "6", "(6h + h²)/h = 6 + h, que tiende a 6."),
        ("abc", "{F} La pendiente de la tangente a f en x = 3 es 6 y en x = 1 es 2. ¿Qué indica?", "La curva sube más rápido cerca de x = 3 que cerca de x = 1", "La curva sube más rápido cerca de x = 1", "La curva sube igual en ambos", "Mayor pendiente significa que la función crece más rápido."),
    ],
    ctx=("abc", "Un tobogán de ejemplo tiene perfil y = x² (x e y en metros). En x = 2, la pendiente de la tangente es 4. ¿Cuántos metros sube el tobogán por cada metro horizontal justo en ese punto?", "4 metros", "2 metros", "8 metros", "La pendiente de la tangente da cuántas unidades verticales por cada unidad horizontal."),
    sc=[
        ("En Matemática: ¿qué es la recta tangente a una curva en un punto?", "La recta que toca la curva en ese punto con su misma dirección", "Es el límite de las secantes."),
        ("¿Qué representa la derivada de f en a?", "La pendiente de la tangente y la rapidez instantánea de cambio", "Es el límite del cociente incremental."),
        ("=", "Si el cociente incremental simplificado es 4 + h, ¿cuánto vale su límite cuando h tiende a 0?", "4", "Al desaparecer h queda solo 4."),
    ],
    op=("Con f(x) = x² y a = 4, completa una tabla con h = 1; 0,1; 0,01 para el cociente incremental (f(4 + h) − f(4))/h, estima la pendiente de la tangente y comprueba el resultado simplificando ((4 + h)² − 16)/h. Escribe qué significa en una frase.",
        "h = 1: (25 − 16)/1 = 9. h = 0,1: (4,1)² = 16,81 y (16,81 − 16)/0,1 = 0,81/0,1 = 8,1. h = 0,01: (4,01)² = 16,0801 y 0,0801/0,01 = 8,01. Se acercan a 8. Simplificando: (8h + h²)/h = 8 + h, que tiende a 8. La tangente en x = 4 tiene pendiente 8.",
        ["calcula tres cocientes con h cada vez menor", "simplifica y halla el límite", "interpreta como pendiente de la tangente"],
        ["tabla de tres filas, simplificación y frase"],
        ["reemplazar h por 0 al inicio", "no simplificar el numerador", "no interpretar el 8"],
        "Pregunta: «¿qué pasa con 8 + h cuando h se achica?». Debe decir que se acerca a 8."),
    reinforce="Con f(x) = x², calcula la pendiente de la secante por (3; 9) y (3,1; 9,61) y compárala con 6.",
    extend="Explica con tus palabras por qué la pendiente de la tangente sirve para describir qué tan rápido cambia una cantidad en un instante.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (funciones de ejemplo). f(x) = x², g(x) = 3x + 2, k(x) = 5 y m(x) = x² + 2x. "
     "La derivada de f en x se define como el límite, con h tendiendo a 0, de (f(x + h) − f(x))/h.")
build(
    O3, 3, F,
    use="Aprenderé a calcular la derivada de funciones simples con la definición, usando una estrategia de tres pasos. Sirve para hallar la rapidez instantánea de cambio con exactitud, sin depender de tablas.",
    prior=["Sé expandir (x + h)².", "Sé simplificar fracciones algebraicas.", "Sé que la derivada es el límite del cociente incremental."],
    explain=[
        "Para derivar por definición se siguen tres pasos. Primero, escribir el cociente (f(x + h) − f(x))/h. Segundo, simplificar el numerador, expandiendo y cancelando términos hasta poder dividir por h. Tercero, hacer que h tienda a 0 en lo que queda. Si se salta el segundo paso y se sustituye h = 0 de inmediato, se obtiene 0/0.",
        "Con f(x) = x²: (f(x + h) − f(x))/h = ((x + h)² − x²)/h = (2xh + h²)/h = 2x + h. Cuando h tiende a 0, queda f'(x) = 2x. Con g(x) = 3x + 2: (3(x + h) + 2 − (3x + 2))/h = 3h/h = 3, entonces g'(x) = 3: la derivada de una recta es su pendiente. Con una constante como k(x) = 5, el numerador siempre es 5 − 5 = 0, así que k'(x) = 0.",
        "La notación f'(x) se lee «f prima de x». Una vez que se tiene f'(x), se evalúa en cualquier punto: si f'(x) = 2x, entonces f'(5) = 10. El resultado debe revisarse: si la función es una recta, la derivada debe ser constante; si f'(a) = 0, la tangente en a es horizontal. Comprobar con una tabla de cocientes ayuda a detectar errores de álgebra.",
    ],
    vocab=[("derivar", "calcular la derivada de una función"), ("f'(x)", "derivada de f en x"), ("expandir", "desarrollar un producto o potencia en una suma de términos"), ("tangente horizontal", "tangente de pendiente 0"), ("por definición", "usando el límite del cociente incremental")],
    worked=[
        ("Derivar una función cuadrática por definición", "Halla n'(x) para n(x) = x² + 3x.",
         ["Cociente: ((x + h)² + 3(x + h) − x² − 3x)/h = (2xh + h² + 3h)/h = 2x + h + 3.", "Cuando h tiende a 0, queda 2x + 3."],
         "n'(x) = 2x + 3"),
        ("Derivada de una recta", "Halla r'(x) para r(x) = 4x − 1.",
         ["Numerador: 4(x + h) − 1 − (4x − 1) = 4h.", "Cociente: 4h/h = 4."],
         "r'(x) = 4, la pendiente de la recta"),
    ],
    mistakes=[("Sustituir h = 0 antes de simplificar y concluir que f'(x) = 0.", "Aparece 0/0, que no es un valor.", "Expande y cancela h antes de dejarla tender a 0."),
              ("Expandir (x + h)² como x² + h².", "Se omite el término doble 2xh.", "Recuerda (a + b)² = a² + 2ab + b².")],
    T=[
        ("=", "{F} Calcula g(4).", "3*4+2", "g(4) = 3·4 + 2."),
        ("abc", "¿Cuál es el primer paso para calcular f'(x) por definición?", "Escribir el cociente (f(x + h) − f(x))/h", "Sustituir h = 0 de inmediato", "Elegir un valor numérico para x", "Primero se plantea el cociente; la sustitución de h va al final."),
        ("{F} Expande (x + h)².", "x² + 2xh + h²", "(a + b)² = a² + 2ab + b²."),
        ("Para u(x) = x² + 4x, simplifica ((x + h)² + 4(x + h) − x² − 4x)/h con h distinto de 0.", "2x + 4 + h", "El numerador es 2xh + h² + 4h, y se divide por h."),
        ("Halla u'(x) para u(x) = x² + 4x.", "2x + 4", "Al tender h a 0 en 2x + 4 + h, queda 2x + 4."),
        ("=", "Calcula u'(5), con u'(x) = 2x + 4.", "2*5+4", "Se evalúa la derivada en x = 5."),
        ("Simplifica (w(x + h) − w(x))/h para w(x) = 6x − 7.", "6", "Numerador: 6(x + h) − 7 − 6x + 7 = 6h, y 6h/h = 6."),
        ("Halla d'(x) para d(x) = 9 y di qué significa.", "0: una constante no cambia", "El numerador d(x + h) − d(x) siempre es 9 − 9 = 0."),
        ("{F} Simplifica ((x + h)² + 2(x + h) − x² − 2x)/h para m.", "2x + 2 + h", "El numerador queda 2xh + h² + 2h, dividido por h."),
        ("ab", "¿Por qué la derivada de una recta es su pendiente?", "Porque el cociente incremental de una recta siempre da el mismo valor, su pendiente", "Porque una recta no tiene derivada", "En una recta la secante coincide con la tangente en todo tramo."),
        ("abc", "Un estudiante sustituye h = 0 en ((x + h)² − x²)/h antes de simplificar y obtiene 0/0. ¿Qué debe hacer?", "Expandir, cancelar h y recién después dejar h tender a 0", "Concluir que la derivada vale 0", "Dividir el numerador por 0", "La indeterminación se resuelve simplificando; no se concluye nada de ella."),
        ("Con m'(x) = 2x + 2, calcula m'(1).", "4", "Se reemplaza x por 1: 2·1 + 2."),
        ("¿En qué valor de x la recta tangente a f(x) = x² es horizontal, es decir, f'(x) = 0?", "x = 0", "2x = 0 solo cuando x vale 0."),
    ],
    ctx=("=", "Un dron de ejemplo recorre s(t) = t² metros en t segundos. Como s'(t) = 2t, ¿cuál es su rapidez instantánea a los 4 segundos?", "2*4", "Se evalúa s'(4) = 2·4.", " m/s"),
    sc=[
        ("En Matemática: ¿qué se hace en el segundo paso de la derivación por definición?", "Simplificar el numerador hasta poder dividir por h", "Sin ese paso el cociente queda 0/0."),
        ("¿Cuánto vale la derivada de una función constante?", "0", "Una constante no cambia, así que su tasa es nula."),
        ("=", "Si f'(x) = 2x, ¿cuánto vale f'(7)?", "2*7", "Se reemplaza x por 7 en la derivada."),
    ],
    op=("Deriva por definición la función p(x) = x² + 5x. Escribe los tres pasos (cociente, simplificación y límite), evalúa p'(2) y comprueba con una tabla de cocientes incrementales en a = 2 usando h = 0,1 y h = 0,01.",
        "Cociente: ((x + h)² + 5(x + h) − x² − 5x)/h = (2xh + h² + 5h)/h = 2x + h + 5. Límite: p'(x) = 2x + 5. p'(2) = 9. Tabla: h = 0,1: (p(2,1) − p(2))/0,1 = (14,91 − 14)/0,1 = 9,1; h = 0,01: (14,0901 − 14)/0,01 = 9,01. Se acercan a 9.",
        ["escribe los tres pasos sin saltar la simplificación", "evalúa la derivada en el punto", "comprueba con la tabla"],
        ["hoja con tres pasos, p'(2) y tabla de dos filas"],
        ["sustituir h = 0 de inmediato", "olvidar el término 5h", "no comparar la tabla con el resultado"],
        "Pregunta: «¿qué pasó con h al final?». Debe decir que tiende a 0 y desaparece."),
    reinforce="Deriva por definición q(x) = 2x² y evalúa q'(3).",
    extend="Explica por qué la derivada de x² + 5x es la suma de la derivada de x² y la de 5x, usando los pasos de la definición.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (modelos de ejemplo). Un corredor avanza s(t) = t² + 2t metros a los t segundos, con s'(t) = 2t + 2 m/s. "
     "Una taza se enfría según T(t) = 80 − t² grados Celsius a los t minutos, con T'(t) = −2t °C/min. "
     "Una fábrica tiene costo C(x) = 2x² + 100 pesos por x unidades, con C'(x) = 4x pesos por unidad.")
build(
    O3, 4, F,
    use="Aprenderé a interpretar la rapidez instantánea de cambio con unidades y signo en modelos de movimiento, temperatura y costos, y a distinguirla de la rapidez media. Sirve para justificar conclusiones sobre cómo cambia una cantidad.",
    prior=["Sé calcular la derivada de funciones simples.", "Sé calcular rapidez media.", "Sé interpretar unidades de una tasa."],
    explain=[
        "La derivada f'(a) mide cuánto cambia f por cada unidad de la variable en el punto a. Sus unidades son las de f divididas por las de x: si s está en metros y t en segundos, s' está en metros por segundo. Con s(t) = t² + 2t, s'(3) = 8 significa que a los 3 segundos el corredor avanza a 8 metros por segundo en ese instante.",
        "El signo da la dirección del cambio. Si f'(a) es positiva, la cantidad aumenta en ese instante; si es negativa, disminuye; si es cero, no cambia momentáneamente. Con T'(2) = −4 °C/min, la taza se está enfriando a 4 grados por minuto en t = 2. Para estimar un cambio pequeño se usa f(a + Δx) ≈ f(a) + f'(a)·Δx, con Δx pequeño.",
        "La rapidez media resume un intervalo y la instantánea describe un punto. Entre t = 2 y t = 4, s(4) − s(2) = 24 − 8 = 16 m en 2 s, es decir 8 m/s de media, mientras que s'(2) = 6 y s'(4) = 10: la media está entre ambas. Para argumentar, se debe nombrar el instante, el valor, la unidad y qué significa en la situación.",
    ],
    vocab=[("unidad de la derivada", "unidades de f divididas por unidades de x"), ("signo de la derivada", "indica si la cantidad aumenta (+) o disminuye (−)"), ("estimar", "calcular un valor aproximado con un modelo"), ("interpretar", "explicar qué significa un resultado en la situación"), ("instante", "valor puntual del tiempo")],
    worked=[
        ("Interpretar un valor y su unidad", "Con C(x) = 2x² + 100 y C'(x) = 4x, interpreta C'(20).",
         ["C'(20) = 4·20 = 80.", "La unidad es pesos por unidad producida."],
         "Cuando se producen 20 unidades, producir una unidad más cuesta aproximadamente 80 pesos"),
        ("Interpretar el signo", "Con T'(t) = −2t, interpreta T'(3).",
         ["T'(3) = −6 °C/min.", "El signo negativo indica que la temperatura baja."],
         "A los 3 minutos la taza se enfría a 6 °C por minuto"),
    ],
    mistakes=[("Interpretar s'(3) = 8 como «en 3 segundos recorre 8 metros».", "Se confunde la rapidez en un instante con la distancia recorrida.", "Escribe la unidad: 8 metros por segundo en ese instante."),
              ("Decir que una derivada negativa significa que la cantidad es negativa.", "Se confunde la dirección del cambio con el valor.", "El signo de la derivada indica si aumenta o disminuye, no el signo de la función.")],
    T=[
        ("=", "{F} Calcula s(6).", "6*6+2*6", "s(6) = 36 + 12."),
        ("=", "{F} Calcula s'(6).", "2*6+2", "Se reemplaza t por 6 en 2t + 2."),
        ("abc", "{F} ¿En qué unidades se mide s'(t)?", "Metros por segundo", "Metros", "Segundos por metro", "La derivada divide metros entre segundos."),
        ("abc", "{F} Si s'(6) = 14, ¿qué significa?", "A los 6 segundos el corredor avanza a 14 m/s en ese instante", "En 6 segundos recorre 14 metros", "Siempre avanza a 14 m/s", "La derivada habla de la rapidez en un instante, no de una distancia."),
        ("ab", "{F} Si T'(5) = −10 °C/min, ¿qué indica el signo negativo?", "Que la temperatura está bajando en ese instante", "Que la temperatura de la taza es negativa", "Una derivada negativa indica que la función disminuye."),
        ("{F} Calcula T'(4) y escribe el resultado con su unidad.", "−8 °C/min", "T'(4) = −2·4 = −8 °C por minuto."),
        ("=", "{F} Usa s'(6) = 14 m/s para estimar cuántos metros avanza en los siguientes 0,5 segundos (14 por 0,5).", "14/2", "Cambio aproximado = rapidez × tiempo = 8 × 0,5.", " m"),
        ("{F} Se sabe que s'(0) = 2. ¿Está quieto el corredor en t = 0?", "No: parte con rapidez 2 m/s", "Una derivada distinta de cero indica que la posición cambia en ese instante."),
        ("abc", "{F} ¿Cuánto vale C'(10) y con qué unidad?", "40 pesos por unidad", "40 pesos", "10 unidades", "C'(10) = 4·10 y la unidad es pesos por unidad producida."),
        ("=", "{F} Calcula la rapidez media del corredor entre t = 1 y t = 3, en m/s, con s(1) = 3 y s(3) = 15.", "(15-3)//(3-1)", "El cambio es 12 m en 2 s."),
        ("abc", "{F} Un compañero dice que, como la media entre t = 1 y t = 3 es 6 m/s, a 1 segundo el corredor iba a 6 m/s. ¿Qué respuesta es correcta?", "No: s'(1) = 4 y s'(3) = 8; la media 6 resume todo el intervalo", "Sí: la media siempre coincide con el inicio", "No: la rapidez es siempre 8", "La rapidez instantánea en t = 1 es 4 y la media del intervalo es otra cosa."),
        ("¿En qué instante t el corredor tiene rapidez instantánea de 12 m/s?", "t = 5", "2t + 2 = 12 lleva a 2t = 10 y t = 5."),
        ("abc", "{F} Como T'(t) = −2t se hace más negativa al avanzar t, ¿qué dice el modelo de la taza?", "Que se enfría cada vez más rápido, lo cual no concuerda con una taza real", "Que se calienta", "Que se enfría cada vez más lento", "T' es cada vez más negativa: la bajada se acelera, algo que un modelo real no suele mostrar."),
    ],
    ctx=("=", "En la fábrica de la ficha, ¿cuántos pesos cuesta aproximadamente producir una unidad adicional cuando ya se producen 25 unidades? Es C'(25) = 4·25.", "4*25", "Se evalúa la derivada de costo en x = 25.", " pesos"),
    sc=[
        ("En Matemática: ¿qué unidades tiene la derivada de una función?", "Las de la función divididas por las de la variable", "Es una tasa: cuánto cambia por cada unidad de x."),
        ("¿Qué indica una derivada positiva en un punto?", "Que la cantidad aumenta en ese instante", "El signo positivo corresponde a un cambio creciente."),
        ("=", "Si una función tiene derivada constante 3 unidades por segundo, ¿cuánto cambia en 5 segundos?", "3*5", "Cambio = tasa por tiempo."),
    ],
    op=("Con la función de la ficha s(t) = t² + 2t, completa: calcula s'(1), s'(4) y la rapidez media entre t = 1 y t = 4 (s(1) = 3 y s(4) = 24). Escribe una frase que interprete cada resultado con su unidad y explica por qué la media no coincide con ninguna de las dos derivadas.",
        "s'(1) = 4 m/s; s'(4) = 10 m/s; media: (24 − 3)/3 = 7 m/s. En t = 1 avanza a 4 m/s, en t = 4 a 10 m/s, y en promedio durante el intervalo a 7 m/s. La media resume todo el tramo y queda entre los valores extremos porque la rapidez crece.",
        ["calcula las tres tasas con unidad", "interpreta cada una en una frase", "explica la diferencia entre instantánea y media"],
        ["hoja con tres valores, tres frases y una explicación"],
        ["omitir las unidades", "confundir la media con la rapidez en un instante", "olvidar el significado del signo"],
        "Pregunta: «¿qué mide cada número?». Debe separar instante de intervalo."),
    reinforce="Con T(t) = 80 − t², calcula T'(1) y T'(4) y escribe qué te dicen sobre el enfriamiento.",
    extend="Explica por qué el modelo T(t) = 80 − t² deja de ser razonable cuando t es grande, y qué dato lo mostraría.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (datos y modelos de ejemplo, inventados). Una taza se enfría en una sala a 20 °C. Datos: con t = 0, 1, 2, 3 minutos la temperatura T es 80, 50, 40, 35 °C. "
     "Modelo A: A(t) = 80 − 30t. Modelo B: B(t) = 20 + 60/(1 + t), con B'(t) = −60/(1 + t)².")
build(
    O3, 5, F,
    use="Aprenderé a comparar un modelo con datos mediante la rapidez de cambio y a decidir si hay que ajustarlo. Sirve para evaluar si un modelo describe bien una situación y mejorarlo cuando no.",
    prior=["Sé calcular rapideces medias.", "Sé interpretar una derivada con unidades.", "Sé evaluar un modelo en valores dados."],
    explain=[
        "Un modelo es una función que describe una situación de forma aproximada. Para evaluarlo se compara lo que predice con los datos. Una forma es calcular el error en cada punto, es decir, la diferencia entre el valor predicho y el dato. Otra forma es comparar la rapidez de cambio del modelo con las rapideces medias que se calculan con los datos en cada intervalo.",
        "Con los datos de la ficha, las rapideces medias son −30 °C/min entre 0 y 1, −10 entre 1 y 2, y −5 entre 2 y 3. La taza se enfría cada vez más lento. El modelo A supone una rapidez constante de −30 °C/min, y por eso predice A(3) = −10 °C, algo imposible en una sala a 20 °C. El modelo B da B(2) = 40 y B(3) = 35, coincidiendo con los datos, y su derivada B'(1) = −15 muestra el enfriamiento que se hace más lento.",
        "Ajustar un modelo significa cambiar su forma o sus constantes cuando los datos lo contradicen. Si aparece un dato nuevo que difiere poco de la predicción, se puede ajustar una constante; si la diferencia es grande y sistemática, hay que cambiar el tipo de modelo. También se deben declarar los límites: un modelo vale solo en el rango de datos con que se probó, y hay que revisar de nuevo con datos nuevos.",
    ],
    vocab=[("error de un modelo", "diferencia entre el valor predicho y el dato real"), ("ajustar", "cambiar constantes o forma del modelo para que concuerde mejor con los datos"), ("rango de validez", "valores de x donde el modelo se probó y puede usarse"), ("dato nuevo", "medición adicional que sirve para probar el modelo"), ("tasa media por intervalo", "cambio dividido por el tiempo entre dos datos")],
    worked=[
        ("Calcular el error de un modelo", "Con el modelo A y el dato T(2) = 40, calcula el error.",
         ["A(2) = 80 − 60 = 20.", "El error es 40 − 20 = 20 °C."],
         "El modelo A se equivoca en 20 °C"),
        ("Comparar la rapidez del modelo con los datos", "Los datos dan una media de −5 °C/min entre 2 y 3. Compara con el modelo A.",
         ["El modelo A tiene rapidez constante −30 °C/min.", "−30 es muy distinto de −5."],
         "El modelo A no refleja que la taza se enfría cada vez más lento"),
    ],
    mistakes=[("Elegir un modelo porque coincide con un solo dato.", "Con un punto muchos modelos coinciden.", "Compara el modelo con todos los datos y con las tasas de cambio."),
              ("Usar un modelo fuera del rango de los datos sin avisar.", "No se sabe si sigue valiendo.", "Declara el rango probado y evita extrapolar sin revisar.")],
    T=[
        ("=", "{F} Calcula A(1).", "80-30*1", "A(1) = 80 − 30."),
        ("=", "{F} Calcula B(2).", "20+60//(1+2)", "B(2) = 20 + 60/3."),
        ("abc", "{F} ¿Cuál modelo coincide con el dato T(2) = 40?", "El modelo B", "El modelo A", "Ambos", "B(2) vale 40 y A(2) vale 20."),
        ("abc", "{F} A(3) = −10 °C. ¿Qué problema muestra eso en una taza dentro de una sala a 20 °C?", "Predice una temperatura bajo la de la sala, algo imposible para una bebida que se enfría", "Ninguno: es posible", "Predice que la taza se calienta", "Una bebida que se enfría no puede bajar de la temperatura ambiente."),
        ("=", "{F} Calcula el error del modelo A en t = 3, es decir, el dato 35 menos el valor A(3).", "35-(80-30*3)", "El valor predicho es −10 y el dato es 35."),
        ("=", "{F} Calcula el error del modelo B en t = 3, es decir, el dato 35 menos B(3).", "35-(20+60//(1+3))", "B(3) = 20 + 15 = 35, igual al dato."),
        ("{F} Calcula la tasa media entre t = 1 y t = 2 con los datos.", "−10 °C/min", "(40 − 50)/(2 − 1) = −10."),
        ("{F} Calcula la tasa media entre t = 2 y t = 3 con los datos.", "−5 °C/min", "(35 − 40)/(3 − 2) = −5."),
        ("abc", "{F} Las tasas medias −30, −10 y −5 °C/min, ¿qué indican?", "La taza se enfría cada vez más lento", "La taza se enfría cada vez más rápido", "La taza se enfría a ritmo constante", "El valor absoluto de la tasa baja de 30 a 5."),
        ("ab", "{F} El modelo A supone una tasa constante de −30 °C/min. ¿Concuerda con los datos?", "No: los datos muestran tasas cada vez menos negativas", "Sí: porque la primera tasa es −30", "Las tasas −30, −10 y −5 no son constantes."),
        ("{F} Con B'(t) = −60/(1 + t)², calcula B'(0) con su unidad.", "−60 °C/min", "Se reemplaza t por 0: B'(0) = −60/1 = −60."),
        ("abc", "{F} Considerando datos y tasas, ¿qué conviene hacer con los dos modelos?", "Descartar o ajustar el A, porque su tasa constante contradice los datos", "Descartar el B", "Conservar los dos sin cambios", "El B coincide con datos y tasas; el A no."),
        ("abc", "{F} Se mide un nuevo dato: t = 3 da 33 °C, mientras B(3) = 35. ¿Qué decisión es razonable?", "Notar el desvío de 2 °C y, si se repite, ajustar una constante del modelo", "Descartar todos los datos anteriores", "Concluir que B es perfecto", "Un desvío pequeño se revisa con más datos antes de cambiar el modelo."),
    ],
    ctx=("=", "Un depósito de ejemplo se vacía y un modelo dice N(t) = 100 − 10t litros a los t minutos. En t = 4 se mide 66 litros. ¿Cuántos litros más hay en el depósito que lo que predice el modelo?", "66-(100-10*4)", "El modelo predice 60 y se midió 66.", " litros"),
    sc=[
        ("En Matemática: ¿qué es el error de un modelo en un punto?", "La diferencia entre el valor predicho y el dato", "Mide cuánto se aleja el modelo del dato."),
        ("¿Qué se hace cuando un modelo contradice los datos?", "Se ajusta o se cambia el modelo", "Los datos nuevos obligan a revisarlo."),
        ("¿Qué es el rango de validez de un modelo?", "Los valores de x en que se probó y puede usarse", "Fuera de él no se sabe si sirve."),
    ],
    op=("Se observa una planta de ejemplo: su altura H en cm medida cada semana es 10, 14, 16, 17 con t = 0, 1, 2, 3. Calcula las tasas medias por intervalo, di si la planta crece a ritmo constante, compara con el modelo P(t) = 10 + 4t (da 22 en t = 3) y escribe cómo ajustarías el modelo.",
        "Tasas medias: 4, 2 y 1 cm por semana. No crece a ritmo constante: cada semana crece menos. El modelo P supone 4 cm por semana siempre, y en t = 3 da 22 en lugar de 17, con error de 5 cm. Habría que cambiar el tipo de modelo por uno cuya tasa disminuya, y probarlo con nuevos datos.",
        ["calcula las tres tasas medias con unidad", "compara con el modelo usando el error en t = 3", "propone un ajuste y declara su límite"],
        ["hoja con tasas, error y propuesta de ajuste"],
        ["aceptar el modelo por un solo dato", "no comparar las tasas", "no declarar el rango de validez"],
        "Pregunta: «¿crece igual cada semana?». Debe responder que no, usando las tasas."),
    reinforce="Con la tabla de la planta (10, 14, 16, 17 cm), calcula el error del modelo P(t) = 10 + 4t en t = 2 y escribe qué indica.",
    extend="Propón un tercer modelo para la taza de la ficha y explica con qué datos nuevos lo pondrías a prueba antes de usarlo.",
)
