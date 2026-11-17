"""Límites, derivadas e integrales (electivo 3.º y 4.º medio HC): OAC-02, límites en un punto y en el infinito, convergencia y continuidad, clases 1 a 6."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, cuaderno y calculadora simple para armar tablas de valores. "
             "Todas las funciones y tablas están escritas en cada ejercicio; no necesitas internet. "
             "Una hoja de cálculo o un graficador digital son opcionales: sirven para ver tendencias, no reemplazan el argumento escrito. Los datos son de ejemplo.")
build = make_build(MATERIALS)

O2 = "MA-LIDI-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (funciones de ejemplo). f(x) = 2x + 1: con x = 2,9 da 6,8; x = 2,99 da 6,98; x = 3,01 da 7,02; x = 3,1 da 7,2. "
     "g(x) = (x² − 4)/(x − 2), no definida en x = 2: con x = 1,9 da 3,9; x = 1,99 da 3,99; x = 2,01 da 4,01; x = 2,1 da 4,1.")
build(
    O2, 1, F,
    use="Aprenderé a explicar qué significa el límite de una función en un punto y a estimarlo con tablas. Sirve para describir a qué valor se acerca un resultado aunque no se pueda calcular justo en ese punto.",
    prior=["Sé evaluar funciones y armar tablas de valores.", "Sé operar con decimales.", "Sé que no se puede dividir por 0."],
    explain=[
        "El límite de f(x) cuando x se acerca a a es el número L al que se acerca f(x) cuando x toma valores cada vez más cercanos a a, por ambos lados. Se escribe lim f(x) = L (con x → a). Lo importante es la tendencia: el valor de f en el propio punto a puede ser distinto de L, o incluso no existir.",
        "Con tablas se estima un límite. Para f(x) = 2x + 1 y x → 3, los valores 6,8; 6,98 por la izquierda y 7,02; 7,2 por la derecha se acercan a 7. Para g(x) = (x² − 4)/(x − 2) y x → 2, aunque g(2) no existe (el denominador es 0), los valores 3,9; 3,99 y 4,01; 4,1 se acercan a 4, así que el límite es 4.",
        "Una tabla es evidencia, no una demostración: muestra una tendencia con algunos valores. Se debe mirar ambos lados del punto y valores muy cercanos. Si los valores crecen sin parar (como 1/x cerca de 0) o se acercan a números distintos desde cada lado, el límite no existe como número. En las próximas clases se verán métodos algebraicos que confirman lo que sugiere la tabla.",
    ],
    vocab=[("límite", "valor al que se acerca f(x) cuando x se acerca a un punto"), ("tendencia", "comportamiento de los valores al acercarse a un punto"), ("lim", "abreviatura de límite"), ("x → a", "se lee «x tiende a a»: x se acerca a a"), ("indefinida", "función sin valor en un punto, por ejemplo por dividir por 0")],
    worked=[
        ("Estimar un límite con una tabla", "Para m(x) = 3x − 1 y x → 2, se tienen m(1,9) = 4,7; m(1,99) = 4,97; m(2,01) = 5,03; m(2,1) = 5,3. Estima el límite.",
         ["Por la izquierda los valores 4,7 y 4,97 se acercan a 5.", "Por la derecha 5,3 y 5,03 se acercan a 5."],
         "El límite estimado es 5"),
        ("Límite donde la función no está definida", "Para n(x) = (x² − 1)/(x − 1), con n(0,9) = 1,9; n(0,99) = 1,99; n(1,01) = 2,01, estima el límite en x = 1 y di si n(1) existe.",
         ["Los valores se acercan a 2 desde ambos lados.", "En x = 1 el denominador es 0, por lo que n(1) no existe."],
         "El límite estimado es 2, aunque n(1) no existe"),
    ],
    mistakes=[("Pensar que el límite es siempre el valor de la función en el punto.", "Se confunde acercarse con llegar.", "Mira los valores cerca del punto; el valor en el punto puede ser otro o no existir."),
              ("Estimar un límite con valores de un solo lado.", "Un lado puede acercarse a un número y el otro a otro.", "Revisa tendencias por la izquierda y por la derecha.")],
    T=[
        ("abc", "{F} Según la tabla de f, ¿a qué valor se acerca f(x) cuando x se acerca a 3?", "7", "3", "6,8", "Los valores 6,98 y 7,02 se acercan a 7, no a 3 ni se quedan en 6,8."),
        ("=", "{F} Calcula f(3).", "2*3+1", "Se reemplaza x por 3 en f(x) = 2x + 1."),
        ("abc", "{F} ¿Qué significa decir que el límite de g(x) cuando x se acerca a 2 es 4?", "Que g(x) se acerca a 4 al acercarse x a 2, aunque g(2) no exista", "Que g(2) vale 4", "Que x vale 4", "El límite describe la tendencia cerca del punto, no el valor en él."),
        ("ab", "{F} g(2) no existe porque el denominador x − 2 vale 0. ¿Impide eso que el límite exista?", "No: el límite mira los valores cerca de 2, no el valor en 2", "Sí: sin g(2) no puede existir el límite", "El límite solo depende de los valores cercanos a 2, y esos sí están definidos."),
        ("{F} ¿Cuánto le falta a 3,99 para llegar a 4?", "0,01", "4 − 3,99 es 0,01, una distancia que se hace más pequeña al acercarse x a 2."),
        ("{F} Cuando x se acerca a 2 por la derecha, con los valores 2,1 y 2,01, ¿a qué valor se acerca g(x)?", "4", "La tabla da 4,1 y 4,01, que se acercan a 4."),
        ("abc", "Para s(x) = 4x − 2 y x → 1, la tabla da s(0,9) = 1,6; s(0,99) = 1,96; s(1,01) = 2,04; s(1,1) = 2,4. ¿Cuál es el límite estimado?", "2", "1", "1,6", "Los valores de ambos lados se acercan a 2."),
        ("=", "Calcula el límite de 5x − 1 cuando x → 2 sustituyendo directamente x = 2, porque es una recta.", "5*2-1", "Para rectas, el límite en un punto coincide con el valor de la función."),
        ("abc", "Para s(x) = x² con x → 2, la tabla da s(1,9) = 3,61; s(1,99) = 3,9601; s(2,01) = 4,0401; s(2,1) = 4,41. ¿Cuál es el límite estimado?", "4", "2", "3,61", "Los valores de ambos lados se acercan a 4."),
        ("ab", "Una tabla con x = 2,9 y 2,99 da valores que se acercan a 7, pero no se ha probado ningún valor mayor que 3. ¿Basta para afirmar que el límite en x = 3 es 7?", "No: falta revisar la tendencia por la derecha", "Sí: con un lado alcanza", "El límite exige que ambos lados lleven al mismo número, así que hay que revisar los dos."),
        ("abc", "Para t(x) = 1/x con x → 0, la tabla da t(0,1) = 10; t(0,01) = 100; t(0,001) = 1.000. ¿Qué se concluye?", "Los valores crecen sin acercarse a un número: no hay límite finito", "El límite es 1.000", "El límite es 0", "Los valores aumentan sin parar y no se acercan a ningún número fijo."),
        ("La función k vale k(x) = x + 1 para x distinto de 5, y k(5) = 0. ¿Cuál es el límite de k cuando x → 5 y cuánto vale k(5)?", "El límite es 6 y k(5) es 0", "Cerca de 5 la función vale x + 1, que se acerca a 6; el valor puntual k(5) = 0 no cambia la tendencia."),
        ("abc", "Una tabla muestra que f(x) se acerca a 7 con x = 2,99 y x = 3,01. ¿Cómo se debe calificar esa tabla?", "Evidencia numérica útil, que luego se confirma con álgebra o gráfica", "Una demostración completa", "Información inútil", "Una tabla muestra la tendencia con pocos valores y por eso se complementa."),
    ],
    ctx=("abc", "Una feria de ejemplo cobra C(x) = (x² − 9)/(x − 3) pesos por kilo (x distinto de 3). Con x = 2,9 el cobro es 5,9; con x = 2,99 es 5,99; con x = 3,01 es 6,01. ¿Valor al que se acerca el cobro cuando x se acerca a 3?", "6", "3", "5,9", "Los valores de ambos lados se acercan a 6."),
    sc=[
        ("En Matemática: ¿qué describe el límite de una función en un punto?", "El valor al que se acerca la función cerca del punto", "El límite resume la tendencia, no el valor puntual."),
        ("¿Una tabla de valores demuestra un límite?", "No: da evidencia de la tendencia, que luego se confirma", "Con pocos valores no se cubren todos los casos."),
        ("¿Puede existir el límite en un punto donde la función no está definida?", "Sí, si los valores cercanos se acercan a un número", "El límite no usa el valor en el punto."),
    ],
    op=("Considera h(x) = (x² − 25)/(x − 5) con x → 5. Arma una tabla con x = 4,9; 4,99; 5,01; 5,1 (calcula cada h(x) simplificando la fracción), estima el límite y escribe una frase que explique por qué h(5) no existe pero el límite sí.",
        "x = 4,9 da 9,9; x = 4,99 da 9,99; x = 5,01 da 10,01; x = 5,1 da 10,1 (porque h(x) = x + 5 cerca de 5). El límite estimado es 10. h(5) no existe porque el denominador vale 0, pero los valores cercanos sí se acercan a 10.",
        ["calcula los cuatro valores correctamente", "estima el límite mirando ambos lados", "explica la diferencia entre límite y valor en el punto"],
        ["tabla de cuatro filas, límite estimado y frase explicativa"],
        ["tomar solo valores de un lado", "afirmar que el límite es h(5)", "no simplificar la fracción antes de calcular"],
        "Pregunta: «¿qué número se acerca por la izquierda y cuál por la derecha?». Deben coincidir en 10."),
    reinforce="Con f(x) = 4x − 3, arma una tabla con x = 1,9; 1,99; 2,01; 2,1 y estima el límite cuando x → 2.",
    extend="Explica con tus palabras por qué, para estimar un límite, no importa el valor de la función exactamente en el punto.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (funciones de ejemplo). p(x) = x + 1 si x < 2, y p(x) = x + 3 si x ≥ 2. "
     "Gráfica de r (descrita): una curva continua que pasa cerca del punto (1, 4) por ambos lados, pero el punto de x = 1 está vacío; "
     "hay un punto aislado lleno en (1, 6).")
build(
    O2, 2, F,
    use="Aprenderé a representar límites con gráficas y a usar límites laterales para decidir si el límite existe. Sirve para argumentar con la gráfica y con números a la vez.",
    prior=["Sé estimar un límite con una tabla.", "Sé leer una gráfica y un punto vacío o lleno.", "Sé evaluar funciones por tramos."],
    explain=[
        "El límite por la izquierda, lim f(x) con x → a⁻, es el valor al que se acerca f(x) con x menores que a. El límite por la derecha, con x → a⁺, usa x mayores que a. Se llaman límites laterales. El límite lim f(x) con x → a existe solo si ambos laterales existen y son iguales; en ese caso, el límite es ese valor común.",
        "En una gráfica, el límite se lee siguiendo la curva hacia x = a desde cada lado y viendo a qué altura llega. Un punto vacío significa que la función no toma ese valor ahí, pero la curva puede igual apuntar a una altura. Un punto lleno aislado muestra el valor f(a), que puede ser distinto del límite.",
        "En funciones por tramos se calcula cada lateral con la fórmula del tramo correspondiente. Para p(x) = x + 1 si x < 2 y p(x) = x + 3 si x ≥ 2, el lateral izquierdo en 2 es 2 + 1 = 3 y el derecho es 2 + 3 = 5. Como 3 y 5 son distintos, el límite en 2 no existe; la gráfica tiene un salto.",
    ],
    vocab=[("límite lateral izquierdo", "valor al que se acerca f con x menores que a"), ("límite lateral derecho", "valor al que se acerca f con x mayores que a"), ("por tramos", "función con distintas fórmulas en distintos intervalos"), ("salto", "diferencia entre los límites laterales en un punto"), ("punto vacío", "punto de la gráfica que no pertenece a la función")],
    worked=[
        ("Límites laterales de una función por tramos", "Sea w(x) = 2x si x < 3 y w(x) = x + 4 si x ≥ 3. Calcula los laterales en x = 3 y di si el límite existe.",
         ["Por la izquierda se usa 2x: 2·3 = 6.", "Por la derecha se usa x + 4: 3 + 4 = 7. Como 6 ≠ 7, no coinciden."],
         "El límite no existe, porque los laterales son 6 y 7"),
        ("Leer una gráfica", "En una gráfica, la curva se acerca a la altura 2 por ambos lados de x = 4, hay un punto vacío en (4, 2) y un punto lleno en (4, 5). Da el límite y el valor de la función.",
         ["Ambos lados llevan a la altura 2: el límite es 2.", "El punto lleno en (4, 5) indica que f(4) = 5."],
         "El límite es 2 y f(4) = 5"),
    ],
    mistakes=[("Declarar que el límite existe porque calculaste solo un lateral.", "Se olvida que ambos lados deben coincidir.", "Calcula siempre los dos laterales y compáralos."),
              ("Leer el límite en el punto lleno aislado de la gráfica.", "Se confunde el valor f(a) con la altura hacia la que apunta la curva.", "Sigue la curva desde ambos lados e ignora el punto aislado.")],
    T=[
        ("=", "{F} Calcula p(1).", "1+1", "Como 1 < 2, se usa x + 1."),
        ("=", "{F} Calcula p(3).", "3+3", "Como 3 ≥ 2, se usa x + 3."),
        ("abc", "¿Qué significa el límite de f(x) cuando x se acerca a 2 por la izquierda?", "El valor al que se acerca f(x) con x menores que 2", "El valor al que se acerca f(x) con x mayores que 2", "El valor f(2)", "El lateral izquierdo usa solo valores de x menores que 2."),
        ("=", "{F} Calcula el límite de p(x) cuando x se acerca a 2 por la izquierda, usando x + 1.", "2+1", "A la izquierda de 2 se usa la fórmula x + 1."),
        ("=", "{F} Calcula el límite de p(x) cuando x se acerca a 2 por la derecha, usando x + 3.", "2+3", "A la derecha de 2 se usa la fórmula x + 3."),
        ("ab", "{F} ¿Existe el límite de p(x) cuando x se acerca a 2?", "No: los laterales son 3 y 5, distintos", "Sí: vale 5 porque p(2) = 5", "El límite exige laterales iguales, y aquí 3 y 5 difieren."),
        ("{F} En la gráfica de r, ¿a qué valor se acerca r(x) cuando x se acerca a 1?", "4", "La curva pasa cerca de (1, 4) por ambos lados."),
        ("{F} En la gráfica de r, ¿cuánto vale r(1)?", "6", "El punto lleno aislado en (1, 6) marca el valor de la función."),
        ("abc", "{F} Sobre r en x = 1, ¿cuál afirmación es verdadera?", "El límite es 4 y r(1) vale 6", "El límite es 6 porque r(1) vale 6", "El límite no existe porque r(1) es distinto de 4", "El límite viene de la curva alrededor, no del punto aislado."),
        ("ab", "Si ambos límites laterales de f en x = 3 valen 8 y f(3) = 2, ¿qué afirmación es correcta?", "El límite en 3 es 8, aunque f(3) sea 2", "El límite en 3 es 2 porque f(3) es 2", "Los laterales iguales a 8 determinan el límite, y f(3) puede ser distinto."),
        ("abc", "Un estudiante calcula solo el límite por la izquierda de p en 2, que es 3, y dice que el límite en 2 es 3. ¿Qué le falta?", "Calcular el lateral derecho y compararlo con el izquierdo", "Calcular p(0)", "Nada, basta un lado", "Sin el lateral derecho no se sabe si coinciden."),
        ("Sea s(x) = x + 1 si x < 4 y s(x) = a − x si x ≥ 4. ¿Qué valor de a hace que los laterales en x = 4 coincidan?", "a = 9", "El lateral izquierdo es 4 + 1 = 5, y el derecho a − 4 debe ser 5, entonces a = 9."),
        ("Sea s(x) = x + 1 si x < 4 y s(x) = 9 − x si x ≥ 4. ¿Cuánto vale s(4) y cómo se compara con el límite en 4?", "s(4) = 5, igual al límite 5", "s(4) = 9 − 4 = 5 y el límite común es 5."),
    ],
    ctx=("abc", "Un estacionamiento de ejemplo cobra c(t) = 2.000 pesos si el tiempo t es menor que 3 horas, y c(t) = 500t + 1.000 pesos si t ≥ 3. ¿Qué ocurre con el límite del cobro cuando t se acerca a 3 horas?", "No existe: por la izquierda es 2.000 y por la derecha 2.500", "Existe y vale 2.000", "Existe y vale 2.500", "A la izquierda se cobra 2.000 y a la derecha 500·3 + 1.000 = 2.500; los laterales difieren."),
    sc=[
        ("En Matemática: ¿cuándo existe el límite de f en un punto?", "Cuando los dos límites laterales existen y son iguales", "Esa es la condición completa y suficiente para que exista."),
        ("¿Qué indica un punto vacío en una gráfica?", "Que la función no toma ese valor en ese punto", "El punto vacío se omite pero la curva puede apuntar a él."),
        ("=", "Si p(x) = x + 1 para x < 2, ¿cuánto vale el lateral izquierdo en x = 2?", "2+1", "Se reemplaza x por 2 en la fórmula del tramo izquierdo."),
    ],
    op=("Define una función por tramos con dos fórmulas distintas (por ejemplo, f(x) = 2x si x < 1 y f(x) = x + 3 si x ≥ 1). Calcula los dos laterales en x = 1, decide si el límite existe y dibuja o describe la gráfica con sus puntos llenos y vacíos.",
        "f(x) = 2x si x < 1 y f(x) = x + 3 si x ≥ 1. Lateral izquierdo: 2·1 = 2. Lateral derecho: 1 + 3 = 4. Como 2 y 4 son distintos, el límite no existe. Gráfica: la parte izquierda llega a (1, 2) con punto vacío y la derecha parte en (1, 4) con punto lleno.",
        ["calcula ambos laterales con la fórmula correcta", "decide la existencia comparando", "describe la gráfica con puntos llenos y vacíos"],
        ["hoja con fórmulas, dos laterales, conclusión y dibujo"],
        ["usar la misma fórmula para los dos lados", "decir que el límite es el valor en el punto", "olvidar el punto vacío"],
        "Pregunta: «¿por qué lado usas cada fórmula?». Debe decir que la de x < 1 va por la izquierda."),
    reinforce="Con w(x) = x + 2 si x < 1 y w(x) = 5 − x si x ≥ 1, calcula los dos laterales en x = 1 y decide si el límite existe.",
    extend="Busca un valor de b que haga que w(x) = x + 2 si x < 1 y w(x) = b − x si x ≥ 1 tenga límite en x = 1 y calcula ese límite.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (propiedades y funciones de ejemplo). Si cuando x tiende a a se tiene que lim f(x) = 4 y lim g(x) = 3, entonces "
     "lim (f + g) = 7, lim (f·g) = 12 y lim (f/g) = 4/3. "
     "Funciones: u(x) = (x² − 9)/(x − 3) y v(x) = (x² + x − 6)/(x − 2).")
build(
    O2, 3, F,
    use="Aprenderé a calcular límites con propiedades, sustitución y factorización, y a argumentar cada paso. Sirve para confirmar con álgebra lo que sugiere una tabla.",
    prior=["Sé factorizar diferencia de cuadrados y trinomios.", "Sé estimar límites con tablas.", "Sé simplificar fracciones algebraicas."],
    explain=[
        "Las propiedades de los límites dicen que, si los límites de f y g existen, el límite de una suma es la suma de los límites, el del producto es el producto de los límites y el del cociente es el cociente de los límites, siempre que el límite del denominador no sea 0. Con lim f = 4 y lim g = 3, la suma da 7, el producto 12 y el cociente 4/3.",
        "Cuando la función es un polinomio, el límite se calcula sustituyendo: lim (x² + 2x − 1) cuando x → 4 da 16 + 8 − 1 = 23. Si al sustituir aparece 0/0, es una indeterminación: no es un valor y no dice nada sobre el límite. Hay que simplificar antes, por ejemplo factorizando el numerador y el denominador.",
        "Con u(x) = (x² − 9)/(x − 3): x² − 9 = (x − 3)(x + 3), así que para x distinto de 3, u(x) = x + 3. El límite en x = 3 es 3 + 3 = 6. Se puede simplificar porque el límite mira valores cercanos a 3 y distintos de 3, donde x − 3 no vale 0. Siempre se verifica con una tabla.",
    ],
    vocab=[("indeterminación", "expresión como 0/0 que no tiene valor"), ("factorizar", "escribir una expresión como producto"), ("simplificar", "eliminar un factor común del numerador y del denominador"), ("propiedad del límite", "regla para calcular límites de sumas, productos y cocientes"), ("sustituir", "reemplazar x por el valor al que tiende")],
    worked=[
        ("Límite por factorización", "Calcula el límite de (x² − 16)/(x − 4) cuando x → 4.",
         ["Al sustituir da 0/0. Se factoriza x² − 16 = (x − 4)(x + 4).", "Se simplifica: (x + 4) para x distinto de 4, y se sustituye 4 + 4."],
         "El límite es 8"),
        ("Límite con propiedades", "Si lim f = 5 y lim g = 2 cuando x → 1, calcula el límite de 3f − g.",
         ["El límite de 3f es 3·5 = 15.", "Se resta el límite de g: 15 − 2."],
         "El límite es 13"),
    ],
    mistakes=[("Escribir 0/0 = 0 al sustituir.", "Se trata la indeterminación como un valor.", "Si sale 0/0, simplifica antes de calcular el límite."),
              ("Simplificar (x² − 9)/(x − 3) tachando las x² y las x.", "Solo se pueden cancelar factores completos, no términos.", "Factoriza primero y cancela el factor común (x − 3).")],
    T=[
        ("=", "{F} Con las propiedades, calcula lim (2f + g).", "2*4+3", "El límite de 2f es 2·4 y se suma el límite de g."),
        ("=", "{F} Con las propiedades, calcula lim (f·g + g).", "4*3+3", "El límite del producto es 12 y se le suma el límite de g, que es 3."),
        ("abc", "{F} Al sustituir x = 3 en u(x) = (x² − 9)/(x − 3) se obtiene 0/0. ¿Qué indica?", "Que es una indeterminación y hay que simplificar antes", "Que el límite vale 0", "Que el límite no existe", "El resultado 0/0 no es un valor ni una conclusión: es la señal de que se debe simplificar."),
        ("Factoriza x² − 36.", "(x − 6)(x + 6)", "Es una diferencia de cuadrados: a² − b² = (a − b)(a + b)."),
        ("{F} Simplifica u(x) para x distinto de 3.", "x + 3", "Se cancela el factor x − 3 del numerador y del denominador."),
        ("=", "{F} Calcula el límite de u(x) cuando x → 3, usando la forma simplificada.", "3+3", "Se sustituye x = 3 en x + 3."),
        ("=", "Calcula el límite de x² + 3x − 2 cuando x → 2 por sustitución.", "2*2+3*2-2", "Es un polinomio, así que se sustituye: 4 + 6 − 2."),
        ("{F} Factoriza x² + x − 6 y simplifica v(x) para x distinto de 2.", "x + 3", "x² + x − 6 = (x + 3)(x − 2) y se cancela x − 2."),
        ("=", "{F} Calcula el límite de v(x) cuando x → 2.", "2+3", "Con v(x) = x + 3 cerca de 2, se sustituye."),
        ("abc", "Un estudiante sustituye x = 2 en v(x) y escribe «0/0 = 0». ¿Cuál es el error?", "0/0 no es un valor: es una indeterminación que se simplifica", "Debió sustituir x = 3", "No hay error", "El 0/0 se resuelve factorizando, no se iguala a 0."),
        ("ab", "{F} ¿Puede usarse la propiedad del cociente cuando el límite del denominador es 0?", "No: esa propiedad exige que el límite del denominador no sea 0", "Sí: siempre se puede", "La propiedad del cociente pide un denominador cuyo límite sea distinto de 0."),
        ("Calcula el límite de (x² − 25)/(x − 5) cuando x → 5.", "10", "Se factoriza (x − 5)(x + 5), se cancela y se sustituye 5 + 5."),
        ("Calcula el límite de (x² − 1)/(x² + 3x − 4) cuando x → 1.", "2/5", "Numerador (x − 1)(x + 1), denominador (x + 4)(x − 1); queda (x + 1)/(x + 4), que en 1 vale 2/5."),
    ],
    ctx=("=", "Una mezcla de ejemplo tiene concentración c(x) = (x² − 36)/(x − 6) gramos por litro para x distinto de 6. ¿A qué valor se acerca la concentración cuando x se acerca a 6?", "6+6", "Se simplifica a x + 6 y se sustituye 6.", " gramos por litro"),
    sc=[
        ("En Matemática: ¿qué es una indeterminación como 0/0?", "Una expresión sin valor que obliga a simplificar", "No es un número, es señal de seguir trabajando."),
        ("¿Qué se hace con la factorización antes de calcular un límite?", "Se cancela el factor común que anula el denominador", "Así el denominador deja de valer 0 cerca del punto."),
        ("=", "Si lim f = 6 y lim g = 2, ¿cuánto vale lim (f − g)?", "6-2", "El límite de una resta es la resta de los límites."),
    ],
    op=("Calcula el límite de (x² − 49)/(x − 7) cuando x → 7. Escribe: la sustitución directa que da 0/0, la factorización, la forma simplificada, el límite y una tabla de cuatro valores que lo respalde (x = 6,9; 6,99; 7,01; 7,1).",
        "Sustituir da 0/0. x² − 49 = (x − 7)(x + 7), simplifica a x + 7. El límite es 14. Tabla: 13,9; 13,99; 14,01; 14,1; se acercan a 14.",
        ["muestra la indeterminación", "factoriza y simplifica correctamente", "respalda el límite con una tabla"],
        ["hoja con factorización, límite y tabla"],
        ["tachar términos en vez de factores", "afirmar 0/0 = 0", "no verificar con tabla"],
        "Pregunta: «¿por qué puedes cancelar x − 7?». Debe decir que x es distinto de 7 cerca del punto."),
    reinforce="Calcula el límite de (x² − 4)/(x − 2) cuando x → 2 y verifica con una tabla de cuatro valores.",
    extend="Explica por qué el límite de (x² − 9)/(x − 3) en 3 es 6 aunque la función no esté definida en 3.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (funciones y tablas de ejemplo). f(x) = 1/x: con x = 10 da 0,1; x = 100 da 0,01; x = 1.000 da 0,001. "
     "g(x) = (3x + 1)/(x + 2): con x = 10 da aproximadamente 2,58; x = 100 da 2,95; x = 1.000 da 2,995. "
     "h(x) = x²: con x = 10 da 100; x = 100 da 10.000; x = 1.000 da 1.000.000.")
build(
    O2, 4, F,
    use="Aprenderé a estudiar qué ocurre con una función cuando x se hace muy grande, a decidir si converge y a interpretar la asíntota horizontal. Sirve para predecir comportamientos a largo plazo.",
    prior=["Sé estimar límites con tablas.", "Sé dividir numerador y denominador por una potencia de x.", "Sé que 1/x se hace pequeño si x crece."],
    explain=[
        "El límite en el infinito, lim f(x) con x → ∞, es el valor al que se acerca f(x) cuando x se hace cada vez más grande. Si existe un número L, se dice que f converge a L y la recta y = L es una asíntota horizontal. Para f(x) = 1/x, los valores 0,1; 0,01; 0,001 se acercan a 0, así que el límite es 0.",
        "Para fracciones de polinomios, se divide numerador y denominador por la mayor potencia de x. En g(x) = (3x + 1)/(x + 2), al dividir por x queda (3 + 1/x)/(1 + 2/x). Como 1/x y 2/x se acercan a 0, el límite es 3/1 = 3. Regla: si los grados son iguales, el límite es el cociente de los coeficientes principales; si el grado del numerador es menor, el límite es 0.",
        "Si f(x) crece sin acercarse a ningún número, como h(x) = x², no hay convergencia: se dice que el límite no existe como número (tiende a infinito). Es importante distinguir tres comportamientos: converge a un número, crece sin parar o no se estabiliza. La tabla ayuda a ver la tendencia; el álgebra la confirma.",
    ],
    vocab=[("límite en el infinito", "valor al que se acerca f(x) cuando x crece mucho"), ("converger", "acercarse a un número fijo"), ("asíntota horizontal", "recta y = L a la que se acerca la gráfica"), ("coeficiente principal", "número que multiplica a la mayor potencia de x"), ("divergir", "crecer sin acercarse a un número")],
    worked=[
        ("Límite de una fracción con el mismo grado", "Calcula el límite de (5x + 2)/(2x − 1) cuando x → ∞.",
         ["Se divide numerador y denominador por x: (5 + 2/x)/(2 − 1/x).", "Los términos 2/x y 1/x tienden a 0, queda 5/2."],
         "El límite es 5/2 y la asíntota horizontal es y = 5/2"),
        ("Decidir si converge", "Con p(x) = x + 1 (valores 11, 101, 1.001 para x = 10, 100, 1.000), ¿converge cuando x → ∞?",
         ["Los valores crecen sin parar.", "No se acercan a ningún número fijo."],
         "No converge: crece sin acercarse a un número"),
    ],
    mistakes=[("Decir que el límite de 1/x en el infinito es 1.", "Se confunde 1/x con 1.", "Observa que los valores 0,1; 0,01 se hacen cada vez más pequeños y se acercan a 0."),
              ("Afirmar que (x² + 1)/x tiende a 1 porque «x² y x se parecen».", "No se compara el crecimiento: x² crece más rápido que x.", "Divide por x y mira x + 1/x, que crece sin parar.")],
    T=[
        ("abc", "{F} Según la tabla de f(x) = 1/x, ¿a qué valor se acerca f(x) cuando x crece?", "0", "1", "10", "Los valores 0,1; 0,01; 0,001 se acercan a 0."),
        ("=", "{F} Calcula g(3).", "(3*3+1)//(3+2)", "g(3) = (3·3 + 1)/(3 + 2) = 10/5."),
        ("abc", "¿Qué significa que el límite de f(x) cuando x → ∞ sea L?", "Que f(x) se acerca al número L cuando x se hace muy grande", "Que f(∞) es igual a L", "Que x se acerca a L", "El límite en el infinito describe la tendencia de f(x) cuando x crece."),
        ("ab", "{F} Según su tabla, ¿g(x) converge cuando x crece?", "Sí: se acerca a 3", "No: sus valores siempre cambian", "Los valores 2,58; 2,95; 2,995 se acercan a 3, aunque siempre cambien un poco."),
        ("{F} ¿Cuál es la asíntota horizontal de g, según el límite de su tabla?", "y = 3", "La gráfica se acerca a la recta de altura 3."),
        ("ab", "{F} ¿Converge h(x) = x² cuando x crece?", "No: crece sin acercarse a ningún número", "Sí: converge a 100", "Sus valores 100; 10.000; 1.000.000 crecen sin parar y no se acercan a un número."),
        ("Calcula el límite de 2 + 5/x cuando x → ∞.", "2", "El término 5/x se acerca a 0 y solo queda 2."),
        ("Calcula el límite de (4x + 1)/(x + 3) cuando x → ∞ dividiendo por x.", "4", "Queda (4 + 1/x)/(1 + 3/x), que se acerca a 4/1."),
        ("Calcula el límite de (x + 1)/(x² + 3) cuando x → ∞.", "0", "El grado del numerador es menor que el del denominador."),
        ("abc", "En una fracción de polinomios con el mismo grado en numerador y denominador, ¿cuánto vale el límite en el infinito?", "El cociente de los coeficientes principales", "Cero", "Infinito", "Al dividir por la mayor potencia solo quedan los coeficientes principales."),
        ("ab", "Si el grado del numerador es menor que el del denominador, ¿cuánto vale el límite en el infinito?", "0", "Infinito", "El denominador crece más rápido y el cociente tiende a 0."),
        ("Calcula el límite de (6x² − x)/(2x² + 5) cuando x → ∞.", "3", "Los coeficientes principales son 6 y 2, y 6/2 = 3."),
        ("abc", "Un estudiante afirma que (x² + 1)/x tiende a 1 cuando x → ∞ porque «x² y x se parecen». ¿Cuál es el error?", "Cuando x crece, x² domina y el cociente crece sin acercarse a un número", "Debió dar 0", "No hay error", "Al dividir por x queda x + 1/x, que crece sin parar."),
    ],
    ctx=("abc", "La concentración de sal en un estanque de ejemplo es C(t) = 20t/(t + 4) gramos por litro después de t horas. ¿Cuánto se predice que valdrá cuando t sea muy grande?", "20 gramos por litro", "4 gramos por litro", "Crece sin límite", "Al dividir por t queda 20/(1 + 4/t), que se acerca a 20."),
    sc=[
        ("En Matemática: ¿qué es una asíntota horizontal?", "Una recta y = L a la que se acerca la gráfica cuando x crece", "Resume el límite en el infinito."),
        ("¿Qué quiere decir que una función converge?", "Que se acerca a un número fijo", "Convergencia significa tener un límite que es un número finito."),
        ("=", "¿Cuánto vale el límite de 7 + 1/x cuando x → ∞?", "7", "El término 1/x tiende a 0."),
    ],
    op=("Estudia r(x) = (2x + 3)/(x + 1) cuando x → ∞. Haz una tabla con x = 10, 100, 1.000 (puedes usar calculadora), escribe el límite con la división por x, la asíntota horizontal y una frase que interprete el resultado.",
        "r(10) = 23/11 (aprox. 2,09), r(100) = 203/101 (aprox. 2,01), r(1.000) = 2.003/1.001 (aprox. 2,001). Dividiendo por x: (2 + 3/x)/(1 + 1/x) tiende a 2. Asíntota horizontal: y = 2. La función converge a 2 a largo plazo.",
        ["arma la tabla con tres valores", "calcula el límite dividiendo por x", "interpreta el resultado como convergencia y asíntota"],
        ["hoja con tabla, cálculo, asíntota e interpretación"],
        ["sustituir ∞ como si fuera un número", "olvidar dividir también el denominador", "no relacionar el límite con la asíntota"],
        "Pregunta: «¿qué pasa con 3/x cuando x crece?». Debe decir que se acerca a 0."),
    reinforce="Calcula el límite en el infinito de (3x − 2)/(x + 5) y escribe la asíntota horizontal.",
    extend="Compara el límite en el infinito de (x + 1)/(x² + 1), (x² + 1)/(x + 1) y (x² + 1)/(x² + 3) y explica cada resultado según los grados.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 5 (funciones de ejemplo). f(x) = x² + 1. g(x) = (x² − 4)/(x − 2) si x ≠ 2, y g(2) = 1. h(x) = 1/(x − 1). "
     "k(x) = x + 2 si x < 0 y k(x) = x² + 3 si x ≥ 0.")
build(
    O2, 5, F,
    use="Aprenderé a decidir si una función es continua en un punto con tres condiciones y a clasificar las discontinuidades. Sirve para saber cuándo un modelo se puede dibujar sin levantar el lápiz y cuándo no.",
    prior=["Sé calcular límites laterales y por factorización.", "Sé evaluar funciones por tramos.", "Sé leer gráficas con puntos vacíos y llenos."],
    explain=[
        "Una función f es continua en x = a si cumple tres condiciones: f(a) existe, el límite de f(x) cuando x → a existe, y ese límite es igual a f(a). Si falla alguna, f es discontinua en a. Los polinomios son continuos en todos los reales, y las fracciones de polinomios son continuas en todos los puntos donde el denominador no vale 0.",
        "Hay tres tipos de discontinuidad. Evitable: el límite existe, pero f(a) no existe o es distinto del límite (como g en x = 2, con límite 4 y g(2) = 1). De salto: los laterales existen pero son distintos (como k en x = 0, con 2 y 3). Infinita: la función crece sin parar cerca de a, como h(x) = 1/(x − 1) en x = 1.",
        "Para hacer continua una función por tramos, se igualan los límites laterales con el valor en el punto. Si m(x) = x + 1 para x < 3 y m(x) = a·x − 5 para x ≥ 3, el lateral izquierdo es 4 y el derecho es 3a − 5. Igualando, 3a − 5 = 4 y a = 3. Siempre se comprueba con las tres condiciones.",
    ],
    vocab=[("continua", "se puede trazar en ese punto sin levantar el lápiz, con las tres condiciones"), ("discontinuidad evitable", "límite existe pero no coincide con f(a) o f(a) no existe"), ("discontinuidad de salto", "laterales distintos"), ("discontinuidad infinita", "la función crece sin parar cerca de a"), ("parámetro", "letra que se ajusta para cumplir una condición")],
    worked=[
        ("Verificar las tres condiciones", "¿Es m(x) = x² continua en x = 3?",
         ["m(3) = 9 existe.", "El límite cuando x → 3 es 9, y coincide con m(3)."],
         "Sí, es continua en x = 3"),
        ("Clasificar una discontinuidad", "Sea n(x) = 2 si x < 1, y n(x) = 5 si x ≥ 1. Clasifica en x = 1.",
         ["Laterales: 2 por la izquierda y 5 por la derecha.", "Existen pero son distintos."],
         "Discontinuidad de salto"),
    ],
    mistakes=[("Decir que una función es continua porque su límite existe.", "Se olvida la condición f(a) = límite.", "Verifica las tres condiciones, una por una."),
              ("Confundir una discontinuidad evitable con una de salto.", "No se comparan los laterales.", "Calcula ambos laterales: si coinciden y f(a) difiere, es evitable.")],
    T=[
        ("abc", "¿Cuál es la primera condición para que f sea continua en x = a?", "Que f(a) exista", "Que el límite en a sea 0", "Que f(a) sea positivo", "Si f(a) no existe, no puede haber continuidad en a; el valor del límite o su signo no son la condición."),
        ("=", "{F} Calcula f(2).", "2*2+1", "f(2) = 2² + 1."),
        ("ab", "{F} ¿Está definida h(x) = 1/(x − 1) en x = 1?", "No: el denominador vale 0", "Sí: vale 1", "En x = 1 el denominador x − 1 vale 0 y la división no existe."),
        ("{F} Simplificando para x distinto de 2, ¿cuánto vale el límite de g(x) cuando x → 2?", "4", "(x² − 4)/(x − 2) = x + 2, que en x = 2 tiende a 4."),
        ("ab", "{F} ¿Es g continua en x = 2?", "No: el límite es 4 pero g(2) vale 1", "Sí: porque g(2) existe", "Para ser continua el límite debe coincidir con g(2), y 4 no es 1."),
        ("abc", "{F} ¿Qué tipo de discontinuidad tiene g en x = 2?", "Evitable: el límite existe y no coincide con g(2)", "De salto: los laterales son distintos", "Infinita: crece sin parar", "Los laterales coinciden en 4, así que no es de salto."),
        ("{F} ¿Cuáles son los límites laterales de k en x = 0?", "Por la izquierda 2 y por la derecha 3", "A la izquierda se usa x + 2, que da 2; a la derecha x² + 3, que da 3."),
        ("abc", "{F} ¿Qué tipo de discontinuidad tiene k en x = 0?", "De salto", "Evitable", "Infinita", "Los laterales 2 y 3 existen pero son distintos."),
        ("Halla a para que m(x) = x + 1 si x < 3 y m(x) = a·x − 2 si x ≥ 3 sea continua en x = 3.", "a = 2", "El lateral izquierdo es 4 y la ecuación 3a − 2 = 4 da a = 2."),
        ("abc", "{F} ¿En qué valor de x deja de ser continua h(x) = 1/(x − 1)?", "x = 1", "x = 0", "x = −1", "Solo en x = 1, donde el denominador vale 0."),
        ("ab", "{F} ¿Es f(x) = x² + 1 continua en todos los reales?", "Sí: es un polinomio y su límite coincide con su valor en cada punto", "No: tiene un salto en x = 0", "Los polinomios son continuos en todos los reales."),
        ("Para r(x) = (x² − 9)/(x − 3) con x distinto de 3, ¿qué valor se debe asignar a r(3) para que r sea continua en 3?", "6", "El límite en 3 es 3 + 3 = 6 y r(3) debe ser igual a ese límite."),
        ("abc", "Un estudiante dice «g es continua en 2 porque su límite existe». ¿Qué falta verificar?", "Que el límite coincida con g(2)", "Que g(2) sea igual a 0", "Nada más", "La continuidad exige que límite y valor sean iguales."),
    ],
    ctx=("abc", "Un taxímetro de ejemplo cobra c(d) = 600 + 100d pesos si la distancia d (en kilómetros) es hasta 2, y c(d) = 800 + 150(d − 2) pesos si d > 2. ¿Qué se puede decir del cobro en d = 2?", "Es continuo: ambos tramos dan 800 pesos en d = 2", "Tiene un salto de 800 a 950", "Tiene una discontinuidad infinita", "Por la izquierda 600 + 100·2 = 800 y por la derecha 800 + 0 = 800, y el valor c(2) = 800 coincide."),
    sc=[
        ("En Matemática: ¿cuáles son las tres condiciones de continuidad en a?", "f(a) existe, el límite existe y ambos son iguales", "Son las tres que se verifican en orden."),
        ("¿Dónde es continua una fracción de polinomios?", "En todos los puntos donde el denominador no vale 0", "Solo falla donde se anula el denominador."),
        ("¿Cómo se clasifica una discontinuidad con laterales distintos?", "De salto", "Los laterales existen pero no coinciden."),
    ],
    op=("Define dos funciones por tramos: una con una discontinuidad de salto en x = 2 y otra continua en x = 2. Para cada una, calcula los laterales y f(2), verifica las tres condiciones y escribe una frase que explique la diferencia entre ambas.",
        "Salto: p(x) = x si x < 2 y p(x) = x + 1 si x ≥ 2. Laterales 2 y 3, p(2) = 3; no coinciden. Continua: q(x) = x si x < 2 y q(x) = 2x − 2 si x ≥ 2. Laterales 2 y 2, q(2) = 2; coinciden. La diferencia está en que los laterales sean iguales.",
        ["calcula laterales y valor en el punto en cada función", "verifica las tres condiciones", "explica la diferencia con sus palabras"],
        ["hoja con dos funciones, laterales, valores y explicación"],
        ["no calcular el lateral derecho", "dejar f(2) sin calcular", "decir que la continuidad solo depende del límite"],
        "Pregunta: «¿qué número sale por cada lado?». Debe comparar los dos laterales."),
    reinforce="Halla b para que s(x) = 2x si x < 1 y s(x) = x + b si x ≥ 1 sea continua en x = 1, y verifica las tres condiciones.",
    extend="Inventa una función con una discontinuidad evitable y explica cómo redefinir su valor en ese punto para volverla continua.",
)

# ============================================================ OAC-02, clase 6
F = ("Ficha 6 (modelos de ejemplo, inventados). T(t) = 20 + 60/(t + 1): temperatura en °C de una taza t minutos después de servirla, en una sala a 20 °C. "
     "A(x) = (50x + 200)/x: costo medio en pesos por unidad al producir x unidades, con un costo fijo de 200 y 50 por unidad.")
build(
    O2, 6, F,
    use="Aprenderé a usar límites para interpretar modelos de ciencias y de la vida diaria y a juzgar con tablas o herramientas digitales si el modelo tiene sentido. Sirve para predecir comportamientos a largo plazo y revisar un modelo.",
    prior=["Sé calcular límites en el infinito.", "Sé evaluar un modelo con una calculadora.", "Sé interpretar unidades."],
    explain=[
        "Un límite en el infinito de un modelo responde qué ocurre a largo plazo. Con T(t) = 20 + 60/(t + 1), cuando t crece, 60/(t + 1) se acerca a 0 y T se acerca a 20 °C: la bebida se enfría hasta la temperatura de la sala. T nunca llega exactamente a 20, pero se acerca tanto como se quiera.",
        "Con A(x) = (50x + 200)/x, al dividir por x queda 50 + 200/x, y el límite en el infinito es 50. Significa que, al producir muchísimas unidades, el costo medio se acerca al costo variable de 50 pesos por unidad, porque el costo fijo de 200 se reparte entre muchas unidades. Los valores A(10) = 70, A(100) = 52 y A(1.000) = 50,2 muestran esa tendencia.",
        "Un modelo se compara con datos. Si el modelo dice que la temperatura final es 20 °C y la sala real está a 18 °C, hay que ajustar el modelo, por ejemplo cambiando el valor límite. Las herramientas digitales (calculadora, hoja de cálculo, graficador) permiten evaluar valores grandes, pero una tabla no prueba un límite: se respalda con el cálculo algebraico.",
    ],
    vocab=[("modelo", "función que representa una situación real de forma aproximada"), ("largo plazo", "valores de x muy grandes"), ("costo medio", "costo total dividido por el número de unidades"), ("ajustar un modelo", "cambiarlo para que concuerde mejor con los datos reales"), ("evidencia numérica", "valores de una tabla que sugieren una tendencia")],
    worked=[
        ("Interpretar un límite", "Con T(t) = 20 + 60/(t + 1), calcula T(59) y el límite cuando t → ∞ e interpreta.",
         ["T(59) = 20 + 60/60 = 21.", "60/(t + 1) tiende a 0, así que T tiende a 20."],
         "T(59) = 21 °C y, a largo plazo, la temperatura se acerca a 20 °C"),
        ("Ajustar un modelo", "Con la fórmula anterior se predice 20 °C a largo plazo, pero la sala real mide 18 °C. ¿Qué se ajusta?",
         ["El modelo debe tender a 18 °C.", "Se cambia el 20 por 18: T(t) = 18 + 60/(t + 1)."],
         "Se cambia la constante de 20 a 18"),
    ],
    mistakes=[("Decir que T llega exactamente a 20 °C en algún minuto.", "Se confunde acercarse con llegar.", "Observa que 60/(t + 1) nunca vale 0, solo se acerca a 0."),
              ("Dar por probado un límite porque una tabla con valores grandes lo sugiere.", "Una tabla no cubre todos los valores.", "Respáldalo con el cálculo algebraico.")],
    T=[
        ("=", "{F} Calcula T(0).", "20+60//(0+1)", "En t = 0 se tiene 60/1 = 60."),
        ("=", "{F} Calcula T(5).", "20+60//(5+1)", "T(5) = 20 + 60/6 = 30."),
        ("abc", "{F} ¿A qué temperatura se acerca T(t) cuando t crece mucho?", "20 °C", "80 °C", "0 °C", "El término 60/(t + 1) se acerca a 0 y queda 20."),
        ("{F} ¿Cuánto vale el límite de T(t) cuando t → ∞, en °C?", "20", "20 + 60/(t + 1) tiende a 20 + 0."),
        ("ab", "{F} ¿Llega T(t) a valer exactamente 20 °C en algún momento?", "No: 60/(t + 1) nunca es 0, solo se acerca", "Sí: en t = 59", "Una fracción con numerador 60 nunca vale 0."),
        ("=", "{F} Calcula A(10).", "(50*10+200)//10", "A(10) = 700/10."),
        ("{F} ¿Cuánto vale el límite de A(x) cuando x → ∞?", "50", "A(x) = 50 + 200/x y 200/x tiende a 0."),
        ("abc", "{F} ¿Qué significa en el contexto que el límite de A(x) sea 50?", "Que con muchísimas unidades el costo medio se acerca a 50 pesos por unidad", "Que el costo total es 50 pesos", "Que cada unidad cuesta siempre 70 pesos", "El costo fijo se reparte entre muchas unidades y queda solo el costo por unidad."),
        ("=", "{F} Calcula A(100).", "(50*100+200)//100", "A(100) = 5.200/100."),
        ("ab", "{F} Con A(10) = 70, A(100) = 52 y A(1.000) = 50,2, ¿qué tendencia muestra el costo medio?", "Baja acercándose a 50 sin llegar", "Sube sin parar", "Los valores decrecen y se estabilizan cerca de 50."),
        ("abc", "El modelo dice que la temperatura límite es 20 °C, pero tras muchas horas se mide una sala a 24 °C. ¿Qué se hace?", "Se ajusta el modelo porque el valor límite no concuerda", "Se ignora la medición", "Se concluye que el límite no existe", "Un modelo que contradice los datos debe revisarse."),
        ("Para que el límite de T(t) = a + 60/(t + 1) sea 22 °C, ¿cuánto debe valer a?", "22", "Como 60/(t + 1) tiende a 0, el límite es a, y debe ser 22."),
        ("abc", "Una tabla de 1/x muestra 0,000001 para x = 1.000.000. ¿Qué puede afirmarse?", "Hay evidencia numérica de que el límite es 0, que se confirma con álgebra", "Es una demostración completa", "La tabla prueba que 1/x llega a 0", "La tabla es evidencia, la prueba es el argumento algebraico."),
    ],
    ctx=("abc", "El nivel de agua de un depósito de ejemplo es N(t) = 8t/(t + 3) metros después de t horas. ¿Qué nivel máximo se acerca a predecir el modelo a largo plazo?", "8 metros", "3 metros", "No tiene máximo", "Al dividir por t queda 8/(1 + 3/t), que se acerca a 8."),
    sc=[
        ("En Matemática: ¿para qué sirve el límite en el infinito de un modelo?", "Para describir el comportamiento a largo plazo", "Resume qué ocurre cuando x es muy grande."),
        ("¿Una tabla con valores grandes prueba un límite?", "No: es evidencia que se respalda con álgebra", "Una tabla no cubre todos los valores posibles de x."),
        ("¿Qué se hace si un modelo no concuerda con las mediciones?", "Se ajusta el modelo", "Se corrigen constantes o la forma de la función."),
    ],
    op=("Elige un modelo: la cantidad de agua en un recipiente V(t) = 12t/(t + 2) litros (de ejemplo) o el costo medio B(x) = (30x + 90)/x pesos. Calcula tres valores, el límite en el infinito, escribe su significado en palabras con unidades y di qué dato real te haría ajustar el modelo.",
        "Con V(t) = 12t/(t + 2): V(2) = 6, V(8) = 9,6, V(98) = 11,76 litros. Límite: 12 litros. Significa que el recipiente se acerca a 12 litros y no los supera. Si se midiera que se llena hasta 10 litros, se ajustaría el 12.",
        ["calcula tres valores y el límite", "interpreta el límite con unidades", "propone un dato que obligaría a ajustar el modelo"],
        ["hoja con tabla, límite, interpretación y ajuste"],
        ["decir que el límite se alcanza en algún valor", "olvidar las unidades", "no proponer ningún criterio de ajuste"],
        "Pregunta: «¿qué dato real contradiría el límite?». Debe proponer una medición concreta."),
    reinforce="Con B(x) = (30x + 90)/x, calcula B(10), B(100) y el límite en el infinito, e interpreta el resultado con unidades.",
    extend="Explica por qué un modelo puede predecir bien a corto plazo y mal a largo plazo, y da un ejemplo con una constante de ajuste.",
)
