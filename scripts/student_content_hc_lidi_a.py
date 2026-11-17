"""Límites, derivadas e integrales (electivo 3.º y 4.º medio HC): OAC-01, composición de funciones y función inversa, clases 1 a 5."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, cuaderno y calculadora simple (una calculadora científica ayuda, pero todo se puede hacer a mano). "
             "Todas las funciones, tablas y datos están escritos en cada ejercicio; no necesitas internet. "
             "Un graficador digital es opcional: sirve para comprobar, no para reemplazar el razonamiento. Los datos son de ejemplo.")
build = make_build(MATERIALS)

O1 = "MA-LIDI-3y4-OAC-01"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (funciones de ejemplo). f(x) = 2x + 3, g(x) = x² y h(x) = x − 5. "
     "Tabla de g: g(1) = 1, g(2) = 4, g(3) = 9.")
build(
    O1, 1, F,
    use="Aprenderé a componer funciones: aplicar una función al resultado de otra y escribir ese resultado con la notación f∘g. Sirve para describir procesos de varios pasos y para saber cuándo el orden cambia el resultado.",
    prior=["Sé evaluar una función en un número (f(2) = 7 si f(x) = 2x + 3).", "Sé operar con expresiones algebraicas simples.", "Sé leer una tabla de valores."],
    explain=[
        "Componer dos funciones es encadenarlas: el resultado de la primera pasa a ser la entrada de la segunda. La composición de f con g se escribe (f∘g)(x) = f(g(x)). Se lee «f después de g»: primero se calcula g(x) y luego se aplica f a ese número. Por ejemplo, con f(x) = 2x + 3 y g(x) = x², para x = 2 se calcula g(2) = 4 y luego f(4) = 11, de modo que (f∘g)(2) = 11.",
        "El orden importa. (g∘f)(x) = g(f(x)) significa primero f y luego g. Con los mismos números, f(2) = 7 y g(7) = 49, de modo que (g∘f)(2) = 49, que es distinto de 11. Por eso f∘g y g∘f son, en general, funciones distintas. Para refutar que dos composiciones sean iguales basta un solo valor de x donde den resultados distintos.",
        "Para que f(g(x)) exista, el número g(x) debe ser una entrada válida para f. Si f solo acepta números positivos y g(x) da un número negativo, ese x no puede entrar a la composición. Cuando se escribe la fórmula, se reemplaza la letra de f por toda la expresión de g, entre paréntesis: con f(x) = 2x + 3 y g(x) = x², queda (f∘g)(x) = 2·x² + 3.",
    ],
    vocab=[("composición", "aplicar una función al resultado de otra"), ("f∘g", "función que primero aplica g y después f"), ("entrada", "número que recibe una función"), ("salida", "número que entrega una función"), ("función interna", "la que se aplica primero en f(g(x)); aquí, g")],
    worked=[
        ("Evaluar una composición en un número", "Con f(x) = 3x − 1 y g(x) = x + 4, calcula (f∘g)(2) y (g∘f)(2).",
         ["Para (f∘g)(2): g(2) = 2 + 4 = 6 y luego f(6) = 3·6 − 1 = 17.", "Para (g∘f)(2): f(2) = 3·2 − 1 = 5 y luego g(5) = 5 + 4 = 9.", "Los resultados 17 y 9 son distintos: el orden cambia el resultado."],
         "(f∘g)(2) = 17 y (g∘f)(2) = 9"),
        ("Escribir la fórmula de una composición", "Con p(x) = x² y q(x) = x − 3, escribe la fórmula de (p∘q)(x).",
         ["(p∘q)(x) = p(q(x)): la función interna es q(x) = x − 3.", "Se reemplaza la x de p por (x − 3), con paréntesis: p(x − 3) = (x − 3)²."],
         "(p∘q)(x) = (x − 3)²"),
    ],
    mistakes=[("Calcular (f∘g)(x) como si fuera f(x)·g(x).", "Se confunde componer (encadenar) con multiplicar los resultados.", "Calcula primero g(x) y solo después aplica f a ese número."),
              ("Reemplazar sin paréntesis: escribir (x − 3)² como x − 3².", "Al sustituir se pierde que toda la expresión es la entrada.", "Escribe la entrada completa entre paréntesis antes de operar.")],
    T=[
        ("abc", "{F} ¿Cuánto vale g(3)?", "9", "6", "5", "g(3) = 3² = 9; 6 sale de multiplicar por 2 y 5 de sumar 2, que no son lo que pide g."),
        ("=", "{F} Calcula f(4).", "2*4+3", "Se reemplaza x por 4 en f(x) = 2x + 3."),
        ("abc", "En (f∘g)(x) = f(g(x)), ¿qué función se aplica primero al número x?", "g", "f", "Las dos a la vez", "En f(g(x)) el paréntesis interno g(x) se resuelve primero y f recibe su resultado."),
        ("=", "{F} Calcula (f∘g)(3): primero g(3) y luego f del resultado.", "2*(3*3)+3", "g(3) = 9 y f(9) = 2·9 + 3."),
        ("=", "{F} Calcula (g∘f)(3), es decir, g(f(3)).", "(2*3+3)*(2*3+3)", "f(3) = 9 y luego g(9) = 9² = 81."),
        ("ab", "{F} Sobre los resultados de (f∘g)(3), que vale 21, y de (g∘f)(3), que vale 81, ¿qué se concluye?", "Son distintos, así que el orden de la composición cambia el resultado", "Son iguales porque ambas usan las mismas funciones f y g", "Los resultados 21 y 81 son distintos, por eso el orden importa."),
        ("=", "{F} Calcula (h∘g)(4): primero g(4) y luego h del resultado.", "4*4-5", "g(4) = 16 y h(16) = 16 − 5."),
        ("{F} Escribe la fórmula de (f∘g)(x) reemplazando g(x) dentro de f.", "2x² + 3", "Se sustituye la x de f por x²: 2·x² + 3."),
        ("{F} Escribe la fórmula de (g∘h)(x) = g(h(x)).", "(x − 5)²", "Se sustituye la x de g por la expresión completa x − 5, entre paréntesis."),
        ("ab", "Con f y g de la ficha, alguien afirma que f(g(x)) = g(f(x)) para todo x. ¿Qué basta para refutarlo?", "Un solo valor de x donde den distinto, como x = 3 con 21 y 81", "Comprobar que ambas dan números positivos", "Un contraejemplo basta para refutar una afirmación general; que ambas den positivos no las vuelve iguales."),
        ("abc", "Sea u(x) = √x, que solo acepta x ≥ 0, y v(x) = x − 4. En u(v(x)), ¿cuál valor de x no puede usarse?", "x = 1, porque v(1) = −3 no es entrada válida de u", "x = 4, porque v(4) = 0 no es entrada válida de u", "x = 9, porque v(9) = 5 no es entrada válida de u", "u acepta 0 y 5 como entradas, pero no −3; por eso solo x = 1 queda fuera."),
        ("=", "{F} Calcula f(g(h(3))): primero h(3), luego g y por último f.", "2*((3-5)*(3-5))+3", "h(3) = −2, g(−2) = 4 y f(4) = 11."),
        ("{F} Halla todos los x tales que (f∘g)(x) = 35.", "x = 4 y x = −4", "2x² + 3 = 35 lleva a x² = 16, y 16 tiene dos raíces: 4 y −4."),
    ],
    ctx=("=", "Una panadería usa g(x) = 4x bandejas cuando recibe x kilos de harina, y f(b) = 6b panes con b bandejas. ¿Cuántos panes salen con 5 kilos de harina? Es (f∘g)(5).", "6*(4*5)", "g(5) = 20 bandejas y f(20) = 120 panes.", " panes"),
    sc=[
        ("En Matemática: ¿qué significa (f∘g)(x)?", "f(g(x)): se aplica g y después f", "La función de la derecha de la ∘ se aplica primero."),
        ("¿Se puede cambiar el orden de una composición sin cambiar el resultado?", "No en general: f∘g y g∘f suelen ser distintas", "Se vio con 21 y 81 que el orden cambia el resultado."),
        ("=", "Si g(2) = 7 y f(7) = 10, ¿cuánto vale (f∘g)(2)?", "10", "Se aplica g(2) = 7 y luego f(7) = 10; basta leer los dos datos en orden."),
    ],
    op=("Elige un proceso de dos pasos que conozcas: por ejemplo, «sumar 3 al número y luego duplicar», o «duplicar y luego sumar 3». Escribe las dos funciones, la fórmula de la composición en los dos órdenes y el resultado para x = 5 en cada orden. Di si coinciden.",
        "Funciones: s(x) = x + 3 y d(x) = 2x. (d∘s)(x) = 2(x + 3) = 2x + 6, que da 16 para x = 5. (s∘d)(x) = 2x + 3, que da 13 para x = 5. No coinciden, así que el orden importa.",
        ["escribe las dos funciones y las dos composiciones con paréntesis correctos", "calcula ambos resultados para x = 5", "concluye si el orden cambia el resultado"],
        ["hoja con dos fórmulas, dos resultados y una conclusión"],
        ["calcular s(x) + d(x) en vez de componer", "sustituir sin paréntesis", "concluir sin comparar los dos números"],
        "Pregunta: «¿cuál función aplicaste primero?». Si no puede decirlo, pídele que marque la función interna."),
    reinforce="Con f(x) = x + 1 y g(x) = 3x, calcula (f∘g)(2) y (g∘f)(2) y escribe una frase que explique por qué son distintos.",
    extend="Busca dos funciones f y g para las que f∘g y g∘f den lo mismo en todo x (por ejemplo, f(x) = x + 2 y g(x) = x + 5) y explica por qué ocurre.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (dos representaciones, de ejemplo). g(x) = 3x + 2 y f(u) = 2u. "
     "Tabla de g: x = 0 da 2, x = 1 da 5, x = 2 da 8, x = 3 da 11. "
     "Tabla de f: u = 2 da 4, u = 5 da 10, u = 8 da 16, u = 11 da 22, u = 14 da 28.")
build(
    O1, 2, F,
    use="Aprenderé a representar una composición de dos maneras, con tablas (diagrama de pasos) y con fórmula, y a comprobar que ambas dan lo mismo. Sirve para argumentar con más de una evidencia.",
    prior=["Sé componer funciones en un número (clase anterior).", "Sé leer valores en una tabla.", "Sé simplificar expresiones como 2(3x + 2)."],
    explain=[
        "Una composición se puede representar con un diagrama de pasos: x → g(x) → f(g(x)). Con tablas, se arma una tabla de tres columnas: x, g(x) y f(g(x)). La primera salida, g(x), se busca en la tabla de g; luego se usa como entrada en la tabla de f. Si un valor de g(x) no aparece en la tabla de f, esa fila no se puede completar.",
        "Con fórmulas, se reemplaza g(x) dentro de f y se simplifica. Si g(x) = 3x + 2 y f(u) = 2u, entonces (f∘g)(x) = 2(3x + 2) = 6x + 4. La letra de la variable no importa: f(u) = 2u y f(x) = 2x son la misma función. Lo que importa es qué se hace con la entrada.",
        "Dos representaciones de una misma composición deben coincidir. Si la tabla dice (f∘g)(2) = 16 y la fórmula 6x + 4 da 6·2 + 4 = 16, ambas se apoyan. Si no coinciden, hay un error en alguna de las dos. Usar dos representaciones es una forma de argumentar: no se afirma solo porque «salió», sino porque dos caminos independientes llegan al mismo número.",
    ],
    vocab=[("diagrama de pasos", "esquema x → g(x) → f(g(x)) que muestra el orden"), ("tabla compuesta", "tabla con las columnas x, g(x) y f(g(x))"), ("simplificar", "reducir una expresión a su forma más corta"), ("variable", "letra que representa la entrada de una función"), ("comprobar", "verificar un resultado por otro camino")],
    worked=[
        ("Armar una fila de la tabla compuesta", "Con la tabla de g (x = 1 da 5) y la de f (u = 5 da 10), completa la fila de x = 1 de f∘g.",
         ["Se busca g(1) en la tabla de g: vale 5.", "Se busca f(5) en la tabla de f: vale 10."],
         "(f∘g)(1) = 10"),
        ("Fórmula y comprobación", "Con g(x) = 3x + 2 y f(u) = 2u, halla la fórmula de f∘g y comprueba con x = 2.",
         ["(f∘g)(x) = f(3x + 2) = 2(3x + 2) = 6x + 4.", "Con x = 2: 6·2 + 4 = 16. Por tablas: g(2) = 8 y f(8) = 16."],
         "(f∘g)(x) = 6x + 4, y ambas vías dan 16"),
    ],
    mistakes=[("Mezclar las tablas: usar x directamente en la tabla de f.", "Se olvida que f recibe la salida de g, no el x original.", "Primero lee g(x) en su tabla y recién después entra con ese número a la tabla de f."),
              ("Escribir 2·3x + 2 como fórmula de f∘g.", "Falta el paréntesis: el 2 multiplica a toda la expresión 3x + 2.", "Escribe 2(3x + 2) y luego distribuye: 6x + 4.")],
    T=[
        ("abc", "{F} Según la tabla de g, ¿cuánto vale g(2)?", "8", "5", "3", "En la tabla de g, x = 2 da 8; 5 corresponde a x = 1."),
        ("abc", "{F} Según la tabla de f, ¿cuánto vale f(11)?", "22", "11", "28", "En la tabla de f, u = 11 da 22; 28 es el valor de u = 14."),
        ("=", "{F} Con la fórmula g(x) = 3x + 2, calcula g(4).", "3*4+2", "Se reemplaza x por 4."),
        ("{F} Usa las dos tablas para hallar (f∘g)(3).", "22", "En la tabla de g, x = 3 da 11, y en la de f, u = 11 da 22."),
        ("=", "{F} Con las fórmulas, calcula (f∘g)(4): primero g(4) y luego f.", "2*(3*4+2)", "g(4) = 14 y f(14) = 28."),
        ("ab", "{F} Para armar la tabla compuesta de f∘g, ¿qué columna se calcula primero a partir de cada x?", "La de g(x), porque f necesita ese resultado", "La de f(u), porque f es la primera letra de f∘g", "La función interna g se aplica primero, y f usa su salida."),
        ("{F} Escribe la fórmula simplificada de (f∘g)(x).", "6x + 4", "f(g(x)) = 2(3x + 2) = 6x + 4."),
        ("=", "{F} Usa la fórmula 6x + 4 para calcular (f∘g)(5).", "6*5+4", "Se reemplaza x por 5 en la fórmula simplificada."),
        ("{F} Escribe la fórmula simplificada de (g∘f)(u) = g(f(u)).", "6u + 2", "g(2u) = 3·2u + 2 = 6u + 2."),
        ("ab", "{F} Un estudiante calcula (f∘g)(2) con tablas y obtiene 16, y con la fórmula 6x + 4 obtiene también 16. ¿Qué aporta eso?", "Dos caminos distintos coinciden y se refuerzan entre sí", "Muestra que una de las dos representaciones sobra siempre", "Que dos vías independientes den lo mismo es evidencia de que ambas están bien calculadas."),
        ("abc", "{F} Si la tabla de f llegara solo hasta u = 11, ¿para qué x no se podría hallar (f∘g)(x) con esa tabla?", "x = 4, porque g(4) = 14 y la tabla no llega a 14", "x = 3, porque g(3) = 11 y la tabla no incluye 11", "x = 0, porque g(0) = 2 y la tabla no incluye 2", "Solo g(4) = 14 supera el máximo 11 de la tabla recortada; g(3) = 11 y g(0) = 2 sí están."),
        ("=", "{F} Halla x tal que (f∘g)(x) = 40 usando la ecuación 6x + 4 = 40.", "(40-4)//6", "Se resta 4 y se divide por 6."),
        ("{F} Con las dos tablas, ¿para qué x se cumple (f∘g)(x) = 4?", "x = 0", "f(2) = 4 y g(0) = 2, así que el x buscado es 0."),
    ],
    ctx=("=", "Una pastelería necesita g(x) = 3x + 2 huevos para x tortas, y cada huevo cuesta $200. El costo en pesos de u huevos es f(u) = 200u. ¿Cuánto cuestan los huevos de 5 tortas?", "200*(3*5+2)", "g(5) = 17 huevos y f(17) = 17·200.", " pesos"),
    sc=[
        ("En Matemática: ¿qué se compara para comprobar una composición?", "El resultado por tabla y el resultado por fórmula", "Dos representaciones independientes deben dar el mismo número."),
        ("¿Cómo se escribe f(g(x)) si f(u) = 2u y g(x) = x + 1?", "2(x + 1)", "Se reemplaza u por toda la expresión x + 1 entre paréntesis."),
        ("=", "Si la fórmula de una composición es 6x + 4, ¿cuánto vale en x = 1?", "6*1+4", "Se reemplaza x por 1 en la fórmula."),
    ],
    op=("Con g(x) = x + 2 y f(u) = 3u, arma una tabla compuesta para x = 0, 1, 2, 3 (columnas x, g(x), f(g(x))), escribe la fórmula de f∘g y comprueba dos filas con la fórmula.",
        "x = 0: g = 2, f(g) = 6. x = 1: g = 3, f(g) = 9. x = 2: g = 4, f(g) = 12. x = 3: g = 5, f(g) = 15. Fórmula: f(g(x)) = 3(x + 2) = 3x + 6. Comprobación: x = 2 da 12 y x = 3 da 15.",
        ["tabla con tres columnas y cuatro filas correctas", "fórmula simplificada con paréntesis bien usados", "comprueba al menos dos filas con la fórmula"],
        ["tabla, fórmula y dos comprobaciones escritas"],
        ["entrar a f con x en vez de con g(x)", "dejar 3x + 2 sin el paréntesis", "no comprobar con la fórmula"],
        "Pregunta: «¿de dónde sale el número de la tercera columna?». Debe mencionar la salida de g."),
    reinforce="Con g(x) = 2x + 1 y f(u) = u + 5, haz una tabla compuesta para x = 1, 2, 3 y escribe la fórmula de f∘g.",
    extend="Explica por qué cambiar la letra de la variable (u por x) no cambia la función, y da un ejemplo con f(u) = 2u.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (funciones de ejemplo). a(x) = x + 4, b(x) = 3x y c(x) = x². "
     "Funciones compuestas dadas: p(x) = (2x − 1)² y q(x) = 3(x + 4).")
build(
    O1, 3, F,
    use="Aprenderé a elegir una estrategia para componer en un orden u otro y para descomponer una función en pasos más simples. Sirve para analizar fórmulas complejas y explicar qué hacen.",
    prior=["Sé calcular f∘g en un número y en una fórmula.", "Sé que f∘g y g∘f suelen ser distintas.", "Sé expandir un cuadrado como (x + 1)²."],
    explain=[
        "Una estrategia para componer es escribir primero los pasos en orden. Para a(b(x)): b multiplica por 3 y luego a suma 4, así que (a∘b)(x) = 3x + 4. Para b(a(x)): a suma 4 y luego b multiplica por 3, de modo que (b∘a)(x) = 3(x + 4) = 3x + 12. Con los mismos pasos en otro orden, se obtienen fórmulas distintas.",
        "Descomponer es el camino contrario: dada una fórmula como p(x) = (2x − 1)², se pregunta qué se hace primero con x y qué se hace después. Primero se calcula 2x − 1 (función interna u(x) = 2x − 1) y después se eleva al cuadrado (función externa c(u) = u²). Entonces p = c∘u. Una misma fórmula puede tener varias descomposiciones, pero una buena separa los pasos de forma natural.",
        "Para resolver una ecuación con una composición, se deshacen los pasos desde el último hacia el primero. Si (b∘a)(x) = 21, entonces 3(x + 4) = 21, luego x + 4 = 7 y x = 3. Comprueba siempre volviendo al inicio: a(3) = 7 y b(7) = 21. Esta comprobación evita errores de orden.",
    ],
    vocab=[("descomponer", "escribir una función como composición de pasos más simples"), ("función externa", "la que se aplica al final, f en f(g(x))"), ("función interna", "la que se aplica primero, g en f(g(x))"), ("deshacer pasos", "resolver una ecuación desde el último paso hacia el primero"), ("contraejemplo", "caso que muestra que una afirmación general es falsa")],
    worked=[
        ("Componer en los dos órdenes", "Con r(x) = x − 2 y s(x) = 5x, halla (r∘s)(x) y (s∘r)(x).",
         ["(r∘s)(x) = r(5x) = 5x − 2.", "(s∘r)(x) = s(x − 2) = 5(x − 2) = 5x − 10."],
         "(r∘s)(x) = 5x − 2 y (s∘r)(x) = 5x − 10"),
        ("Descomponer una fórmula", "Descompón m(x) = (x + 6)³ en una función interna y una externa.",
         ["Con x primero se hace x + 6: función interna u(x) = x + 6.", "Después se eleva al cubo: función externa v(t) = t³."],
         "m = v∘u, con u(x) = x + 6 y v(t) = t³"),
    ],
    mistakes=[("Escribir (b∘a)(x) como 3x + 4, sumando después de multiplicar.", "Se invierte el orden: en b(a(x)) primero actúa a.", "Escribe b(a(x)) = 3·(x + 4) con paréntesis."),
              ("Descomponer p(x) = (2x − 1)² como u(x) = x², externa 2x − 1.", "Se confunde cuál paso ocurre antes.", "Pregunta qué se hace primero con x: calcular 2x − 1.")],
    T=[
        ("=", "{F} Calcula b(5).", "3*5", "Se reemplaza x por 5 en b(x) = 3x."),
        ("=", "{F} Calcula c(7).", "7*7", "c(7) = 7²."),
        ("abc", "{F} En p(x) = (2x − 1)², ¿qué operación se hace al final, después de calcular 2x − 1?", "Elevar al cuadrado", "Multiplicar por 2", "Restar 1", "El cuadrado afecta a todo el paréntesis y es el último paso aplicado."),
        ("{F} Escribe la fórmula de (a∘b)(x) = a(b(x)).", "3x + 4", "b(x) = 3x y a suma 4, así que da 3x + 4."),
        ("{F} Escribe la fórmula de (b∘a)(x) = b(a(x)) sin paréntesis.", "3x + 12", "a(x) = x + 4 y b lo multiplica por 3: 3(x + 4) = 3x + 12."),
        ("ab", "{F} ¿Qué se concluye al comparar a∘b y b∘a?", "Dan 3x + 4 y 3x + 12, que son funciones distintas", "Dan lo mismo porque sumar y multiplicar se pueden conmutar", "Las fórmulas 3x + 4 y 3x + 12 no coinciden en ningún x, por eso las funciones son distintas."),
        ("abc", "{F} La función q(x) = 3(x + 4) se puede ver como una composición. ¿Cuál es?", "b∘a: primero a (sumar 4) y luego b (multiplicar por 3)", "a∘b: primero b (multiplicar por 3) y luego a (sumar 4)", "c∘a: primero a y luego elevar al cuadrado", "En q primero se suma 4 dentro del paréntesis y después se multiplica por 3."),
        ("abc", "{F} Descompón p(x) = (2x − 1)² con p = c∘u. ¿Cuál es la función interna u(x)?", "2x − 1", "x²", "(2x − 1)²", "La interna es la que se calcula primero con x, que es 2x − 1."),
        ("=", "{F} Calcula (c∘a)(2), es decir, c(a(2)).", "(2+4)*(2+4)", "a(2) = 6 y c(6) = 36."),
        ("{F} Halla x tal que (b∘a)(x) = 33.", "x = 7", "3(x + 4) = 33 lleva a x + 4 = 11 y x = 7."),
        ("abc", "{F} Se pregunta si a(b(x)) = b(a(x)) para algún x. ¿Cuál es la conclusión correcta?", "Para ningún x, pues 3x + 4 y 3x + 12 difieren siempre en 8", "Solo para x = 0", "Para todo x", "Al restar 3x + 12 − (3x + 4) siempre queda 8, nunca 0; por eso nunca son iguales."),
        ("{F} Calcula (c∘b)(2) y (b∘c)(2) y di cuál es mayor.", "c∘b da 36 y b∘c da 12; es mayor c∘b", "c(b(2)) = c(6) = 36 y b(c(2)) = b(4) = 12."),
        ("Una función k(x) = 5(x − 3) + 1 se arma con tres pasos aplicados en orden a x. Escríbelos.", "Restar 3, multiplicar por 5 y sumar 1", "Se resuelve primero el paréntesis, luego se multiplica y al final se suma."),
    ],
    ctx=("abc", "Un taller cobra por x horas de trabajo así: primero se agregan 4 horas fijas de preparación y luego cada hora se cobra 3 unidades de ejemplo, de modo que el costo es q(x) = 3(x + 4). ¿Qué orden de pasos describe esa fórmula?", "Primero sumar 4 a x y luego multiplicar por 3", "Primero multiplicar x por 3 y luego sumar 4", "Primero elevar x al cuadrado y luego sumar 4", "El paréntesis x + 4 se calcula primero y luego se multiplica por 3."),
    sc=[
        ("En Matemática: ¿qué es descomponer una función?", "Escribirla como composición de pasos más simples", "Se separan los pasos que se aplican a x en orden."),
        ("Para resolver una ecuación con una composición, ¿en qué orden se deshacen los pasos?", "Desde el último paso aplicado hacia el primero", "El último paso es el que se desarma primero al despejar."),
        ("=", "Con a(x) = x + 4, ¿cuánto vale a(a(3))?", "(3+4)+4", "Se aplica a dos veces: a(3) = 7 y a(7) = 11."),
    ],
    op=("Dada la función w(x) = 2(x − 5)² + 1, escribe los pasos que se aplican a x en orden, define tres funciones simples y escribe w como composición de ellas. Comprueba con x = 7.",
        "Pasos: restar 5, elevar al cuadrado, multiplicar por 2 y sumar 1. Funciones: u(x) = x − 5, v(t) = t², k(s) = 2s + 1. w = k∘v∘u. Con x = 7: u = 2, v = 4, k = 9; y w(7) = 2·4 + 1 = 9.",
        ["lista los pasos en el orden correcto", "define funciones simples que reproducen cada paso", "comprueba con un valor concreto"],
        ["hoja con pasos, funciones, composición y comprobación"],
        ["invertir el orden de los pasos", "olvidar el paréntesis al sustituir", "no comprobar con un número"],
        "Pregunta: «¿qué haces primero con x?». Debe nombrar restar 5."),
    reinforce="Con f(x) = x + 3 y g(x) = 2x, escribe las fórmulas de f∘g y g∘f y calcula ambas en x = 4.",
    extend="Escribe una función que tenga cuatro pasos y descomponla. Pide a otra persona que adivine el orden de los pasos y comprueba si coincide.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (funciones de ejemplo). f(x) = 2x + 6, g(x) = x² (en todos los reales) y h(x) = x³. "
     "Tabla de k: x = −2 da 4, x = −1 da 1, x = 0 da 0, x = 1 da 1, x = 2 da 4.")
build(
    O1, 4, F,
    use="Aprenderé a argumentar si una función tiene inversa y a calcular la inversa de funciones simples. Sirve para deshacer un proceso, como pasar de grados Celsius a Fahrenheit y volver.",
    prior=["Sé evaluar funciones y componerlas.", "Sé despejar x en ecuaciones simples.", "Sé leer una gráfica o una tabla."],
    explain=[
        "La función inversa de f, escrita f⁻¹, deshace lo que hace f: si f(a) = b, entonces f⁻¹(b) = a. No es 1/f. Para que exista, cada salida de f debe venir de una sola entrada. Esa propiedad se llama ser inyectiva. En una gráfica se comprueba con la prueba de la recta horizontal: ninguna recta horizontal debe cortar la gráfica en más de un punto.",
        "g(x) = x² en todos los reales no tiene inversa: g(−3) = 9 y g(3) = 9, es decir, el 9 viene de dos entradas y no se sabe a cuál volver. En cambio, h(x) = x³ sí la tiene: cada valor sale de una sola entrada. Una función constante tampoco tiene inversa, porque todas las entradas dan la misma salida. Una recta no horizontal siempre pasa la prueba.",
        "Para hallar la fórmula de una inversa, se escribe y = f(x), se despeja x en función de y y se intercambian los papeles. Con y = 2x + 6 se resta 6 y se divide por 2: x = (y − 6)/2, es decir, f⁻¹(y) = (y − 6)/2. Se comprueba con un número: f(5) = 16 y f⁻¹(16) = (16 − 6)/2 = 5.",
    ],
    vocab=[("función inversa", "función que devuelve cada salida a su entrada"), ("inyectiva", "cada salida viene de una sola entrada"), ("recta horizontal", "recta de la forma y = constante"), ("despejar", "dejar x sola a un lado de la ecuación"), ("f⁻¹", "símbolo de la inversa de f; no significa 1/f")],
    worked=[
        ("Decidir si hay inversa", "Con la tabla t(−1) = 3, t(0) = 5, t(1) = 3, ¿t tiene inversa?",
         ["Se buscan salidas repetidas: 3 aparece dos veces.", "La salida 3 viene de x = −1 y de x = 1: no se puede volver."],
         "No tiene inversa"),
        ("Calcular la inversa de una recta", "Halla la inversa de m(x) = 4x − 8.",
         ["Se escribe y = 4x − 8 y se despeja: y + 8 = 4x.", "Se divide por 4: x = (y + 8)/4."],
         "m⁻¹(y) = (y + 8)/4"),
    ],
    mistakes=[("Escribir f⁻¹(x) como 1/f(x).", "Se confunde el símbolo −1 de la inversa con un exponente.", "Recuerda que f⁻¹ deshace f; 1/f(x) es otra cosa, el recíproco."),
              ("Decir que x² tiene inversa en todos los reales porque «se puede sacar la raíz».", "Se ignora que 9 viene de 3 y de −3.", "Mira si alguna salida se repite; si hay repetición, no hay inversa.")],
    T=[
        ("abc", "{F} En la tabla de k, ¿qué valores de x dan k(x) = 4?", "x = −2 y x = 2", "Solo x = 2", "x = 4", "k(−2) = 4 y k(2) = 4; ambas entradas llevan al mismo valor."),
        ("=", "{F} Calcula f(5).", "2*5+6", "Se reemplaza x por 5 en f(x) = 2x + 6."),
        ("abc", "¿Qué hace una función inversa?", "Devuelve cada salida a la entrada de la que vino", "Multiplica la salida por −1", "Repite la misma función dos veces", "La inversa deshace la función; no cambia el signo ni la repite."),
        ("ab", "{F} ¿Tiene función inversa la función de la tabla de k?", "No: k(−2) y k(2) dan 4, una salida con dos entradas", "Sí, porque toda tabla de valores tiene inversa", "La salida 4 se repite, por lo que no se sabe a qué entrada volver."),
        ("ab", "{F} Una recta horizontal corta la gráfica de g(x) = x² en dos puntos cuando y = 4. ¿Qué indica?", "Que g no es inyectiva y no tiene inversa en todos los reales", "Que g tiene inversa en todos los reales", "Cortar en dos puntos indica una salida con dos entradas, lo que impide la inversa."),
        ("=", "{F} Con f(x) = 2x + 6, calcula f⁻¹(30): el x que da 30.", "(30-6)//2", "Se resuelve 2x + 6 = 30."),
        ("Despeja x en y = 4x + 2 para escribir la fórmula de la inversa.", "(y − 2)/4", "Se resta 2 y se divide por 4."),
        ("Halla la fórmula de la inversa de r(x) = 3x − 9.", "r⁻¹(y) = (y + 9)/3", "Se suma 9 y se divide por 3."),
        ("=", "{F} Calcula h(3) con h(x) = x³.", "3*3*3", "h(3) = 3³ = 27."),
        ("abc", "{F} ¿Por qué h(x) = x³ sí tiene inversa en todos los reales y g(x) = x² no?", "Porque cada valor de h viene de una sola entrada y en g los positivos vienen de dos", "Porque h es una potencia mayor que g", "Porque h siempre da números positivos", "El criterio es la inyectividad: x³ no repite salidas y x² sí."),
        ("ab", "Una función constante como c(x) = 7, ¿tiene inversa?", "No: todas las entradas dan 7 y no se sabe cuál fue la entrada", "Sí: basta despejar x", "Si todas las entradas dan la misma salida no se puede volver a una entrada única."),
        ("{F} Se restringe g(x) = x² solo a x ≥ 0. Con esa restricción, ¿cuánto da su inversa en y = 49?", "7", "Con x ≥ 0 solo hay una entrada para 49, que es 7."),
        ("abc", "{F} ¿Qué se observa al trazar rectas horizontales sobre la gráfica de f(x) = 2x + 6?", "Cada una la corta en un solo punto, así que f tiene inversa", "Algunas la cortan en dos puntos", "Ninguna la corta", "Una recta no horizontal toma cada valor exactamente una vez."),
    ],
    ctx=("=", "Una cooperativa de ejemplo calcula con f(x) = 2x + 6 las bolsas que salen de x kilos de fruta. Si necesita 20 bolsas, ¿cuántos kilos x debe procesar? Es f⁻¹(20).", "(20-6)//2", "Se resuelve 2x + 6 = 20.", " kilos"),
    sc=[
        ("En Matemática: ¿qué significa que una función sea inyectiva?", "Cada salida viene de una sola entrada", "Es la propiedad que permite volver a la entrada."),
        ("¿Qué prueba gráfica ayuda a decidir si hay inversa?", "La prueba de la recta horizontal", "Si una horizontal corta dos veces, hay una salida con dos entradas."),
        ("=", "Si f⁻¹(y) = (y − 6)/2, ¿cuánto vale f⁻¹(12)?", "(12-6)//2", "Se reemplaza y por 12 en la fórmula de la inversa."),
    ],
    op=("Con la función d(x) = 5x + 10 (x en unidades, d(x) en pesos de ejemplo), escribe la fórmula de la inversa, di qué pregunta responde en palabras y calcula d⁻¹(60). Luego argumenta con la recta horizontal por qué existe.",
        "y = 5x + 10, entonces x = (y − 10)/5, d⁻¹(y) = (y − 10)/5. Responde: ¿cuántas unidades dan y pesos?. d⁻¹(60) = 50/5 = 10. Existe porque es una recta no horizontal y cada horizontal la corta una sola vez.",
        ["despeja x correctamente", "calcula d⁻¹(60) y lo comprueba con d", "argumenta la existencia con la recta horizontal"],
        ["hoja con fórmula, cálculo, comprobación y argumento"],
        ["dejar la fórmula sin despejar", "confundir f⁻¹ con 1/f", "no justificar la existencia"],
        "Pregunta: «¿qué ocurre si calculas d(10)?». Debe obtener 60 y ver que vuelve."),
    reinforce="Halla la inversa de m(x) = x + 7 y de n(x) = 2x. Comprueba con el número 4.",
    extend="Decide si t(x) = |x| (valor absoluto) tiene inversa en todos los reales y, si no, en qué conjunto de entradas la tendría.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (funciones de ejemplo). f(x) = 3x − 4 con inversa f⁻¹(y) = (y + 4)/3; "
     "g(x) = x² considerada solo para x ≥ 0, con inversa g⁻¹(y) = √y.")
build(
    O1, 5, F,
    use="Aprenderé a comprobar que dos funciones son inversas con la composición y con la gráfica, y a comparar argumentos. Sirve para validar una inversa y detectar errores.",
    prior=["Sé hallar f⁻¹ de una recta.", "Sé componer funciones.", "Sé ubicar puntos en el plano."],
    explain=[
        "Dos funciones f y g son inversas si al componerlas en cualquier orden queda el número de partida: f(g(y)) = y y g(f(x)) = x. Por eso se comprueba una inversa con dos composiciones. Con f(x) = 3x − 4 y f⁻¹(y) = (y + 4)/3: f(f⁻¹(11)) = f(5) = 11, y f⁻¹(f(7)) = f⁻¹(17) = 7.",
        "En la gráfica, si (a, b) está en la gráfica de f, entonces (b, a) está en la gráfica de f⁻¹. Por eso ambas gráficas son simétricas respecto de la recta y = x: se reflejan una en la otra como en un espejo. Esta propiedad permite comprobar visualmente una inversa y dibujar una a partir de otra.",
        "Una función sin inversa en todos los reales puede tener inversa si se restringe su conjunto de entradas. g(x) = x² con x ≥ 0 sí es inyectiva y su inversa es √y. Sin esa restricción, √(g(−3)) = 3, que no es −3, así que no se recupera la entrada. Argumentar bien significa combinar al menos dos evidencias: composición, gráfica o tabla.",
    ],
    vocab=[("simetría respecto de y = x", "reflejo de una gráfica en la recta y = x"), ("composición de comprobación", "f(f⁻¹(y)) = y o f⁻¹(f(x)) = x"), ("restringir", "limitar las entradas para que la función sea inyectiva"), ("contraejemplo", "caso que muestra que una afirmación es falsa"), ("conjunto de entradas", "números que se permiten como x")],
    worked=[
        ("Comprobar una inversa por composición", "Comprueba que p(x) = 2x + 1 y q(y) = (y − 1)/2 son inversas.",
         ["p(q(y)) = 2·(y − 1)/2 + 1 = y − 1 + 1 = y.", "q(p(x)) = (2x + 1 − 1)/2 = 2x/2 = x."],
         "Son inversas: ambas composiciones dan el número de partida"),
        ("Puntos de una inversa", "Si (2, 7) está en la gráfica de f y f tiene inversa, ¿qué punto está en la gráfica de f⁻¹?",
         ["f(2) = 7 significa que f⁻¹(7) = 2.", "Se intercambian las coordenadas."],
         "El punto (7, 2)"),
    ],
    mistakes=[("Comprobar solo con un número y declarar que dos funciones son inversas.", "Un caso no demuestra que valga siempre.", "Usa una composición general o varios valores más una gráfica."),
              ("Decir que √(x²) siempre es x.", "Con x negativo, √(x²) da el opuesto de x.", "Restringe a x ≥ 0 antes de usar la raíz como inversa.")],
    T=[
        ("=", "{F} Calcula f(10).", "3*10-4", "f(10) = 30 − 4."),
        ("=", "{F} Calcula f⁻¹(8).", "(8+4)//3", "Se usa f⁻¹(y) = (y + 4)/3."),
        ("abc", "Si un punto (a, b) está en la gráfica de una función con inversa, ¿qué punto está en la gráfica de la inversa?", "(b, a)", "(a, b)", "(−a, −b)", "La inversa intercambia entradas y salidas."),
        ("=", "{F} Calcula f(f⁻¹(14)): primero f⁻¹(14) y después f.", "3*((14+4)//3)-4", "f⁻¹(14) = 6 y f(6) = 14: se vuelve al número de partida."),
        ("=", "{F} Calcula f⁻¹(f(9)): primero f(9) y luego f⁻¹.", "(3*9-4+4)//3", "f(9) = 23 y f⁻¹(23) = 9."),
        ("ab", "{F} ¿Qué debe dar f(f⁻¹(y)) para cualquier y?", "El mismo número y", "El número 0", "Una inversa deshace a f, así que la composición deja el número de partida."),
        ("abc", "Un estudiante propone que la inversa de p(x) = 2x + 1 es q(y) = (y − 1)/2. ¿Cómo lo comprueba?", "Calculando p(q(y)) y verificando que da y", "Sumando p(y) y q(y)", "Viendo que ambas fórmulas tienen un 2", "Componer y obtener la identidad es el criterio; sumar o comparar coeficientes no prueba nada."),
        ("ab", "{F} Un compañero dice que la inversa de f es (y − 4)/3. Con y = 11 obtiene 7/3 y f(7/3) = 3, que no es 11. ¿Qué se concluye?", "Su fórmula es incorrecta: la composición no devuelve 11", "Su fórmula es correcta porque f(7/3) existe", "Para ser inversa debía devolver 11; como dio 3, la fórmula falla."),
        ("{F} Con g(x) = x² para x ≥ 0, ¿cuánto vale g⁻¹(81)?", "9", "Se busca el x ≥ 0 tal que x² = 81, que es 9."),
        ("ab", "{F} Sin la restricción x ≥ 0, ¿por qué √(g(−3)) no devuelve la entrada −3?", "Porque da 3, que no es −3", "Porque la raíz cuadrada de 9 vale 3 y −3 a la vez", "g(−3) = 9 y la raíz cuadrada de 9 es 3, no −3."),
        ("abc", "Se sabe que f(a) = b y f(c) = b con a distinto de c. ¿Qué se concluye sobre f⁻¹(b)?", "No está bien definida, porque habría dos entradas posibles", "Vale a + c", "Vale b", "Una inversa exige una sola entrada para cada salida, y aquí hay dos."),
        ("{F} Halla x tal que f⁻¹(x) = 6.", "14", "Si f⁻¹(x) = 6 entonces f(6) = x, y f(6) = 3·6 − 4 = 14."),
        ("abc", "Para argumentar que una función tiene inversa, ¿qué conjunto de evidencias es más sólido?", "Ninguna horizontal corta dos veces la gráfica y una fórmula inversa comprobada con f∘f⁻¹", "La fórmula tiene una x", "Un punto de la tabla coincide", "Dos evidencias independientes y generales pesan más que un caso aislado o rasgos superficiales."),
    ],
    ctx=("=", "Un termómetro de ejemplo convierte con c(x) = 3x − 4 (x en unidades A, resultado en unidades B). Si una lectura en B es 20, ¿cuánto marcó en A? Usa la inversa (y + 4)/3.", "(20+4)//3", "Se aplica la inversa a 20.", " unidades A"),
    sc=[
        ("En Matemática: ¿qué debe cumplirse para que f y g sean inversas?", "f(g(y)) = y y g(f(x)) = x", "Las dos composiciones deben devolver el número de partida."),
        ("¿Respecto de qué recta son simétricas las gráficas de f y f⁻¹?", "Respecto de la recta y = x", "Reflejar en y = x intercambia entradas y salidas."),
        ("=", "Si f(2) = 5 y f tiene inversa, ¿cuánto vale f⁻¹(5)?", "2", "La inversa devuelve la entrada de la que salió 5."),
    ],
    op=("Elige la función w(x) = 4x − 8. Halla su inversa, compruébala con una composición, ubica dos puntos de w y los de w⁻¹ y explica en una frase qué indica la simetría respecto de y = x.",
        "Inversa: w⁻¹(y) = (y + 8)/4. Comprobación: w(w⁻¹(y)) = 4(y + 8)/4 − 8 = y. Puntos de w: (2, 0) y (3, 4); de w⁻¹: (0, 2) y (4, 3). La simetría indica que las gráficas se reflejan una en la otra.",
        ["halla la inversa y comprueba con una composición", "usa dos puntos y los intercambia", "explica la simetría con sus palabras"],
        ["hoja con fórmula, composición, dos pares de puntos y explicación"],
        ["comprobar con un solo número", "no intercambiar las coordenadas", "decir que la simetría es respecto del eje x"],
        "Pregunta: «¿qué punto de w⁻¹ corresponde a (3, 4)?». Debe responder (4, 3)."),
    reinforce="Comprueba por composición que s(x) = x + 9 y t(y) = y − 9 son inversas y escribe dos puntos de cada una.",
    extend="Explica por qué una función creciente en todo su conjunto de entradas siempre pasa la prueba de la recta horizontal y da un ejemplo.",
)
