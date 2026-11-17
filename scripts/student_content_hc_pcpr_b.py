"""Pensamiento computacional y programación (electivo HC, 3.º y 4.º medio): OAC-03 (algoritmos para procedimientos matemáticos y sucesiones), clases 1 a 4, y OAC-04 (procesadores simbólicos, geometría dinámica y análisis estadístico), clases 1 a 5. Todo en papel: las salidas de los programas se dan de ejemplo y se razonan a mano."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, papel, regla y calculadora simple opcional. No se necesita computador: el código y las salidas de los programas de ejemplo están escritos en cada enunciado y se siguen a mano, "
             "anotando los valores de las variables. En los enunciados, «↵» marca el fin de una línea y «··» marca una línea dentro de un bloque (cada «··» es un nivel). "
             "Si luego pruebas un programa o una herramienta en un computador, hazlo con la supervisión de tu docente.")
build = make_build(MATERIALS)

O3 = "MA-PCPR-3y4-OAC-03"
O4 = "MA-PCPR-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (de ejemplo). Programa A: suma = 0 ↵ for i in range(1, 5): ↵ ··suma = suma + i ↵ print(suma) (print muestra un valor en pantalla). "
     "(range(1, 5) recorre 1, 2, 3 y 4: incluye el inicio y excluye el final; range(inicio, fin, paso) avanza de a «paso».) "
     "Programa B: n = 4 ↵ f = 1 ↵ while n > 1: ↵ ··f = f * n ↵ ··n = n - 1 ↵ print(f). (while repite su bloque mientras la condición sea verdadera.)")
build(
    O3, 1, F,
    use="Aprenderé a escribir y seguir a mano algoritmos con repeticiones (for y while) que ejecutan un procedimiento matemático, como sumar una serie de números.",
    prior=["Sé qué es una variable y una condición.", "Sé sumar y multiplicar números enteros.", "Sé que un programa se ejecuta línea por línea."],
    explain=[
        "Un algoritmo es una secuencia finita de pasos precisos que realiza un procedimiento. Para un procedimiento matemático, como sumar 1 + 2 + 3 + 4, se define el valor inicial de un acumulador (suma = 0), qué valores se recorren y qué se hace en cada vuelta. El for repite un bloque una cantidad conocida de veces; el while lo repite mientras una condición sea verdadera.",
        "range(1, 5) entrega 1, 2, 3 y 4: incluye el primer número y excluye el último. Por eso para sumar hasta 10 se escribe range(1, 11). Con range(2, 11, 2) se recorren 2, 4, 6, 8 y 10, porque el tercer número es el paso. Un error común es olvidar iniciar el acumulador en 0 o escribir mal el final del rango.",
        "Para comprobar un algoritmo se sigue paso a paso en una tabla de seguimiento (traza), con una columna por variable y una fila por vuelta. En un while hay que asegurarse de que algo cambie dentro del bloque que haga falsa la condición; si no, el bucle nunca termina. Por ejemplo, en el programa B la línea n = n - 1 es la que permite que termine.",
    ],
    vocab=[("algoritmo", "secuencia finita de pasos precisos"), ("acumulador", "variable que va guardando un total"), ("for", "bucle que repite para cada valor de un rango"), ("while", "bucle que repite mientras la condición sea verdadera"), ("traza", "seguimiento paso a paso de los valores de las variables"), ("bucle infinito", "repetición que nunca termina")],
    worked=[
        ("Seguir el programa A", "¿Qué imprime el programa A?", ["En cada vuelta i toma 1, 2, 3 y 4, y suma pasa por 1, 3, 6 y 10.", "Al terminar el for, print entrega el valor de suma."], "Imprime 10"),
        ("Escribir un algoritmo", "Escribe un for que sume los números pares de 2 a 10 y calcula el resultado.", ["Inicia suma = 0 y usa range(2, 11, 2), que recorre 2, 4, 6, 8 y 10.", "Se suma 2 + 4 + 6 + 8 + 10."], "El resultado es 30"),
    ],
    mistakes=[("Creer que range(1, 5) incluye el 5.", "El final del rango se excluye.", "Para llegar hasta n escribe range(1, n + 1)."),
              ("No iniciar el acumulador en 0 antes del for.", "La variable no existe o tiene un valor viejo, y la suma sale mal.", "Escribe suma = 0 antes de empezar a sumar.")],
    T=[
        ('abc', '¿Qué valores recorre range(3, 8)?', '3, 4, 5, 6 y 7', '3, 4, 5, 6, 7 y 8', '4, 5, 6 y 7', 'El rango incluye el inicio (3) y excluye el final (8).'),
        ('abc', '{F} ¿Cuánto vale suma justo después de la segunda vuelta del programa A?', '3', '6', '2', 'En la primera vuelta suma = 1 y en la segunda suma = 1 + 2 = 3; 6 es el valor tras la tercera vuelta.'),
        ('ab', '{F} En el programa A, ¿para qué sirve la variable suma?', 'Acumular el total parcial', 'Guardar el último valor de i', 'suma va guardando el total de los valores que se han recorrido.'),
        ('abc', '{F} ¿Cuántas veces se repite el cuerpo del for en el programa A?', '4', '5', '10', 'El for recorre cuatro valores (1, 2, 3 y 4), así que el cuerpo se ejecuta cuatro veces.'),
        ('=', '{F} En el programa B, ¿cuánto vale f al terminar?', '4*3*2', 'f parte en 1 y se multiplica por 4, 3 y 2 mientras n sea mayor que 1.'),
        ('abc', '{F} ¿Cuántas vueltas da el while del programa B?', '3', '4', '24', 'n vale 4, 3 y 2 al evaluar la condición con éxito; cuando n llega a 1, la condición es falsa.'),
        ('=', 'Un programa hace suma = 0 y luego for i in range(1, 8): suma = suma + i. ¿Qué imprime al final?', '1+2+3+4+5+6+7', 'El rango llega hasta 7 porque el final, 8, se excluye.'),
        ('=', 'Un programa suma los valores de range(3, 12, 3). ¿Qué suma obtiene?', '3+6+9', 'Con paso 3 desde 3 recorre 3, 6 y 9; el 12 se excluye.'),
        ('abc', 'Se quiere calcular 1 + 2 + 3 + … + 10. ¿Qué línea de for es correcta?', 'for i in range(1, 11):', 'for i in range(1, 10):', 'for i in range(0, 10):', 'El final se excluye, por lo que para incluir el 10 hay que escribir 11; las otras opciones llegan solo a 9.'),
        ('abc', '{F} Una persona cambia la primera línea del programa A por suma = 5. ¿Qué imprime ahora?', '15', '10', '5', 'La acumulación parte desde 5 y se le suman 1, 2, 3 y 4, o sea 10 más: 15.'),
        ('abc', 'En el programa B, ¿qué pasa si se borra la línea n = n - 1?', 'Nunca termina, porque n siempre es mayor que 1', 'Termina en la primera vuelta', 'Imprime 0', 'Sin esa línea, n no cambia y la condición del while sigue siendo verdadera.'),
        ('=', 'total = 0 ↵ n = 10 ↵ while n > 0: ↵ ··total = total + n ↵ ··n = n - 3 ↵ print(total). ¿Qué imprime?', '10+7+4+1', 'n toma 10, 7, 4 y 1 dentro del bloque; con n = -2 la condición falla.'),
        ('saldo = 100 ↵ for i in range(3): ↵ ··saldo = saldo + saldo // 10 ↵ print(saldo). (range(3) recorre 0, 1 y 2.) ¿Qué imprime?', '133', 'El saldo pasa de 100 a 110, luego a 121 (110 + 11) y luego a 133 (121 + 12).'),
    ],
    ctx=('=', 'suma = 0 ↵ for semana in range(6): ↵ ··suma = suma + 500 ↵ print(suma). Una app de ahorro suma $500 cada semana. ¿Cuánto hay al terminar el for?', '500*6', 'range(6) repite seis veces el bloque, cada una suma 500.'),
    sc=[
        ("En Pensamiento computacional: ¿qué es un algoritmo?", "Una secuencia finita de pasos precisos que resuelve un problema", "Los pasos deben ser claros y terminar en algún momento."),
        ("¿Qué valores recorre range(2, 6)?", "2, 3, 4 y 5", "Incluye el inicio y excluye el final."),
        ("En Pensamiento computacional: ¿cómo se llama seguir un programa paso a paso anotando los valores de sus variables?", "Traza (o tabla de seguimiento)", "La traza permite comprobar un algoritmo sin ejecutarlo."),
    ],
    op=("Elige una opción. Opción 1: suma de los impares de 1 a 15. Opción 2: tabla de multiplicar del 7 hasta 7 · 6, mostrando cada producto. "
        "Escribe el algoritmo en Python con un for (con range correcto), arma la tabla de seguimiento con una fila por vuelta y anota el resultado final.",
        "Opción 1: suma = 0 ↵ for i in range(1, 16, 2): ↵ ··suma = suma + i. Valores de suma: 1, 4, 9, 16, 25, 36, 49 y 64. El resultado es 64.",
        ["inicia el acumulador y escribe un range correcto", "arma la tabla de seguimiento completa", "comprueba el resultado final"],
        ["hoja con el código y la tabla de seguimiento"],
        ["incluir el final del rango por error", "no iniciar el acumulador", "omitir una vuelta en la tabla"],
        "Pregunta: «¿cuántas filas debe tener tu tabla?». Si no coincide con las vueltas del for, revisa el range."),
    reinforce="Sigue a mano el programa A cambiando range(1, 5) por range(1, 7) y anota cuánto imprime.",
    extend="Escribe un while que sume 1 + 2 + … + 10 sin usar for y explica qué línea evita que se repita para siempre.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (de ejemplo). Algoritmo de Euclides para el máximo común divisor (mcd) de dos enteros positivos a y b. Pseudocódigo: mientras b sea distinto de 0: calcular resto = resto de dividir a por b; luego a toma el valor de b y b toma el valor de resto. Al terminar, el mcd es a. "
     "En Python: while b != 0: ↵ ··resto = a % b ↵ ··a = b ↵ ··b = resto ↵ print(a). (% entrega el resto de la división y != significa «distinto de».)")
build(
    O3, 2, F,
    use="Aprenderé a representar un mismo algoritmo de dos maneras, en pseudocódigo y en una tabla de seguimiento, y a ejecutarlo a mano para calcular un máximo común divisor.",
    prior=["Sé qué es un divisor y un múltiplo.", "Sé usar el resto de una división.", "Sé seguir un while a mano."],
    explain=[
        "El mismo algoritmo se puede representar de varias maneras. El pseudocódigo describe los pasos con palabras cercanas al lenguaje natural, sin las reglas estrictas de un lenguaje; el código en Python los escribe con esas reglas; y la tabla de seguimiento (traza) muestra los valores concretos de las variables en cada vuelta para un caso. Cada representación sirve para algo distinto: describir, ejecutar y comprobar.",
        "El máximo común divisor de dos números es el mayor número que divide a ambos. El algoritmo de Euclides se basa en que mcd(a, b) es igual a mcd(b, resto de a dividido por b). Se repite hasta que b vale 0, y entonces el mcd es a. Por ejemplo, con 12 y 8: el resto de 12 dividido por 8 es 4, luego se continúa con 8 y 4; el resto es 0, y el mcd es 4.",
        "El algoritmo siempre termina porque el resto es menor que b: en cada vuelta b disminuye, y como es un entero no negativo, tarde o temprano llega a 0. Aunque a sea menor que b, la primera vuelta los intercambia: el resto de 5 dividido por 15 es 5, y se continúa con 15 y 5. Para verificar el resultado se pueden listar los divisores de cada número y comprobar que el mayor común coincide.",
    ],
    vocab=[("máximo común divisor", "mayor número que divide a dos números"), ("resto", "lo que sobra al dividir"), ("pseudocódigo", "descripción de pasos sin reglas estrictas de un lenguaje"), ("traza", "tabla con los valores de las variables en cada vuelta"), ("operador %", "entrega el resto de una división")],
    worked=[
        ("Tabla de seguimiento", "Sigue el algoritmo con a = 12 y b = 8.", ["Vuelta 1: resto = 12 % 8 = 4; ahora a = 8 y b = 4.", "Vuelta 2: resto = 8 % 4 = 0; ahora a = 4 y b = 0. Como b es 0, termina."], "El mcd es 4"),
        ("Verificar con divisores", "Calcula el mcd de 30 y 18 y verifícalo listando divisores.", ["Euclides: 30 % 18 = 12; 18 % 12 = 6; 12 % 6 = 0. El mcd es 6.", "Divisores de 30: 1, 2, 3, 5, 6, 10, 15, 30. De 18: 1, 2, 3, 6, 9, 18. El mayor común es 6."], "mcd(30, 18) = 6, y coincide con los divisores"),
    ],
    mistakes=[("Usar la división entera // en vez de % para el resto.", "// entrega el cociente, no lo que sobra.", "Para el resto usa %."),
              ("Imprimir b al terminar el algoritmo.", "Cuando el while termina, b vale 0 y el mcd quedó guardado en a.", "Al final del while, imprime a.")],
    T=[
        ('abc', '{F} ¿Cuánto entrega 17 % 5?', '2', '3', '12', '17 = 3 · 5 + 2, así que el resto es 2; 3 es el cociente.'),
        ('abc', '{F} ¿Cuándo se detiene el algoritmo?', 'Cuando b vale 0', 'Cuando a vale 0', 'Cuando resto vale 1', 'La condición del while es b != 0; al volverse falsa, termina.'),
        ('ab', '{F} Al terminar, ¿qué variable contiene el mcd?', 'a', 'b', 'Cuando b llega a 0, el mcd quedó guardado en a.'),
        ('abc', '{F} Con a = 50 y b = 35, ¿cuánto vale resto en la primera vuelta?', '15', '1', '35', '50 % 35 = 15; 1 es el cociente y 35 es el valor de b.'),
        ('abc', '{F} Con a = 50 y b = 35, ¿qué valores tienen a y b después de la primera vuelta?', 'a = 35 y b = 15', 'a = 15 y b = 35', 'a = 50 y b = 15', 'a toma el valor de b (35) y b toma el resto (15).'),
        ('{F} ¿Qué imprime el programa con a = 54 y b = 24?', '6', 'Los restos son 6 y 0 (54 % 24 = 6 y 24 % 6 = 0), y el último valor de a es 6.'),
        ('{F} ¿Cuál es el mcd calculado con a = 35 y b = 14?', '7', '35 % 14 = 7; luego 14 % 7 = 0, y a vale 7.'),
        ('abc', '{F} Con a = 100 y b = 75, ¿cuántas vueltas da el while?', '2', '3', '25', 'En la primera el resto es 25 y en la segunda es 0; entonces b vale 0 y termina.'),
        ('abc', '{F} ¿Qué imprime con a = 14 y b = 21 (a menor que b)?', '7', '14', '21', 'La primera vuelta da resto 14, luego a = 21 y b = 14; después el resto es 7, a = 14 y b = 7; el siguiente resto es 0 y queda a = 7.'),
        ('abc', '{F} Se cambia resto = a % b por resto = a // b. Con a = 12 y b = 8, ¿qué imprime?', '8, que no es el mcd; el cociente no es el resto', '4, igual que antes', '1', 'Los valores sucesivos son (8, 1), (1, 8) y (8, 0): imprime 8, pero el mcd de 12 y 8 es 4.'),
        ('abc', 'Un mismo algoritmo tiene un pseudocódigo y una tabla de seguimiento. ¿Para qué sirve cada una?', 'El pseudocódigo describe los pasos en general; la tabla muestra los valores de un caso concreto', 'El pseudocódigo muestra los valores de un caso; la tabla describe los pasos en general', 'Son idénticas y no sirven para cosas distintas', 'Lo general se describe con pseudocódigo y la comprobación con un caso concreto se hace en la tabla.'),
        ('abc', '{F} ¿Por qué el algoritmo siempre termina?', 'Porque cada resto es menor que b, así que b va disminuyendo hasta llegar a 0', 'Porque a se hace cada vez más grande hasta superar a b', 'Porque el while siempre da tres vueltas, sean cuales sean a y b', 'El resto es menor que b y b es entero y no negativo, por lo que debe llegar a 0.'),
        ('abc', '{F} Con a = 17 y b = 5 (mcd 1), ¿cuántas vueltas da el while?', '3', '2', '1', 'Los restos son 2, 1 y 0, en tres vueltas.'),
    ],
    ctx=('abc', 'Una pastelería corta una plancha de 84 cm por 60 cm en cuadrados iguales, sin sobrantes y lo más grandes posible. Usando el algoritmo de la ficha, ¿cuánto mide el lado del cuadrado?', '12 cm', '24 cm', '6 cm', 'El mcd de 84 y 60 es 12 (restos 24, 12 y 0); 6 también divide a ambos pero no es el mayor, y 24 no divide a 60.'),
    sc=[
        ("En Pensamiento computacional: ¿qué entrega el operador % en Python?", "El resto de la división entera", "% entrega lo que sobra al dividir."),
        ("En Pensamiento computacional: ¿qué es una traza?", "El seguimiento paso a paso de los valores de las variables", "Permite verificar un algoritmo con un caso concreto."),
        ("En Pensamiento computacional: ¿qué es el pseudocódigo?", "Una descripción de los pasos en lenguaje cercano al natural, sin reglas estrictas", "Sirve para planificar antes de escribir en un lenguaje real."),
    ],
    op=("Elige uno de estos pares: (48, 36), (45, 20) o (56, 42). Escribe el algoritmo de Euclides en pseudocódigo, arma una tabla de seguimiento con las columnas a, b y resto, y verifica el resultado listando los divisores de cada número.",
        "Para (45, 20): vuelta 1: resto 5, ahora a = 20 y b = 5; vuelta 2: resto 0, ahora a = 5 y b = 0. El mcd es 5. Divisores de 45: 1, 3, 5, 9, 15, 45; de 20: 1, 2, 4, 5, 10, 20. El mayor común es 5.",
        ["completa la tabla sin saltar vueltas", "obtiene el mcd con el valor de a", "verifica con los divisores"],
        ["hoja con el pseudocódigo, la tabla de seguimiento y la lista de divisores"],
        ["usar // en vez de %", "dar b como resultado", "listar mal los divisores"],
        "Pregunta: «¿qué valor tiene b al terminar?». Si no es 0, revisa la última vuelta."),
    reinforce="Sigue a mano el algoritmo con a = 48 y b = 36 y anota los valores de a, b y resto en cada vuelta.",
    extend="Explica por qué el mcd de dos números primos distintos es 1 y cuántas vueltas esperas en ese caso.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (de ejemplo). Una sucesión puede definirse con una regla explícita o con una regla recursiva. Regla explícita: t(n) = 5·n − 3, para n = 1, 2, 3… (n es el número del término). Regla recursiva: el primer término es 2 y cada término suma 5 al anterior. "
     "Programa que genera los primeros términos: def terminos(cantidad): ↵ ··t = 2 ↵ ··lista = [] ↵ ··for i in range(cantidad): ↵ ····lista.append(t) ↵ ····t = t + 5 ↵ ··return lista. (lista.append(x) agrega x al final de la lista.)")
build(
    O3, 3, F,
    use="Aprenderé a obtener los términos de una sucesión definida por una regla o patrón, con una fórmula y con un programa, y a elegir el método que conviene.",
    prior=["Sé qué es una sucesión de números.", "Sé escribir listas y recorrerlas con un for.", "Sé reemplazar una letra por un valor en una fórmula."],
    explain=[
        "Una sucesión es una lista ordenada de números llamados términos. Puede definirse con una regla explícita, que da el término de la posición n directamente (por ejemplo t(n) = 5·n − 3), o con una regla recursiva, que indica el primer término y cómo obtener cada término a partir del anterior. Con la fórmula, t(1) = 2, t(2) = 7 y t(3) = 12; con la regla recursiva se obtienen los mismos números sumando 5 cada vez.",
        "Para programar una sucesión se escribe un bucle: se parte con el primer término, se agrega a una lista y se actualiza con la regla. Si cantidad vale 4, el programa de la ficha entrega [2, 7, 12, 17]. Hay que cuidar el número de vueltas: range(4) da cuatro términos, no los términos hasta el 4. Una regla de multiplicar por una constante, como duplicar, produce una sucesión que crece más rápido.",
        "Cada método tiene su ventaja. La fórmula explícita permite calcular un término lejano sin los anteriores: t(500) = 5 · 500 − 3 = 2.497. La regla recursiva es más fácil de programar cuando se conoce el paso entre términos. Para reconocer un patrón se miran las diferencias entre términos consecutivos: si son constantes, se suma siempre lo mismo; si no lo son, la regla es otra. También hay sucesiones donde cada término depende de los dos anteriores, como 1, 1, 2, 3, 5, 8…",
    ],
    vocab=[("sucesión", "lista ordenada de números llamados términos"), ("término", "cada número de la sucesión"), ("regla explícita", "fórmula que da el término n directamente"), ("regla recursiva", "indica el primer término y cómo pasar al siguiente"), ("diferencia", "resta entre términos consecutivos")],
    worked=[
        ("Término lejano", "Con la regla explícita de la ficha, ¿cuánto vale t(20)?", ["Reemplaza n por 20: 5 · 20 − 3.", "5 · 20 = 100 y 100 − 3 = 97."], "t(20) = 97"),
        ("Regla recursiva", "¿Cuál es el 6.º término de 3, 6, 12, 24, … si cada término es el doble del anterior?", ["Sigue duplicando: 24 · 2 = 48 y 48 · 2 = 96.", "Los términos son 3, 6, 12, 24, 48 y 96."], "El 6.º término es 96"),
    ],
    mistakes=[("Confundir el número del término con su valor, por ejemplo decir que t(3) = 3.", "n indica la posición; el valor lo da la regla.", "Reemplaza n en la fórmula y calcula."),
              ("Creer que range(4) genera los términos hasta el 4.", "range(4) hace cuatro vueltas y por tanto genera cuatro términos.", "Cuenta las vueltas, no el valor del último término.")],
    T=[
        ('abc', '{F} ¿Cuál es el cuarto término de la sucesión?', '17', '20', '22', 't(4) = 5 · 4 − 3 = 17; 20 olvida restar 3 y 22 es el quinto término.'),
        ('abc', '{F} ¿Qué entrega terminos(3)?', '[2, 7, 12]', '[7, 12, 17]', '[2, 7, 12, 17]', 'range(3) hace tres vueltas, generando los tres primeros términos.'),
        ('ab', '{F} ¿Cómo se llama la regla «cada término suma 5 al anterior»?', 'Recursiva', 'Explícita', 'Una regla que construye cada término a partir del anterior es recursiva.'),
        ('=', '{F} Con la regla explícita, ¿cuánto vale t(10)?', '5*10-3', 'Se reemplaza n por 10 en 5·n − 3.'),
        ('abc', '{F} ¿Qué diferencia hay entre dos términos consecutivos?', '5', '2', '3', 'Cada término suma 5 al anterior; por ejemplo 7 − 2 = 5.'),
        ('abc', '{F} Dentro del for de terminos, ¿qué representa la variable t?', 'El término actual, que se agrega a la lista', 'La cantidad de términos', 'El número de vueltas', 't guarda el valor del término en cada vuelta y luego se actualiza sumándole 5.'),
        ('=', '{F} Con la regla explícita, ¿en qué posición n está el término 52? (Resuelve 5·n − 3 = 52.)', '(52+3)//5', 'Si 5·n − 3 = 52, entonces 5·n = 55 y n = 11.'),
        ('Una sucesión parte en 4 y cada término es el triple del anterior. Escribe los cuatro primeros términos separados por comas.', '4, 12, 36, 108', 'Se multiplica por 3: 4 · 3 = 12, 12 · 3 = 36 y 36 · 3 = 108.'),
        ('abc', '{F} Se quiere cambiar el programa para generar 3, 7, 11, 15. ¿Qué valores de partida y de paso se usan?', 't = 3 y t = t + 4', 't = 3 y t = t + 3', 't = 4 y t = t + 3', 'La sucesión parte en 3 y la diferencia entre términos es 4.'),
        ('abc', '{F} Se quiere el término número 500 de la sucesión. ¿Qué método conviene?', 'La regla explícita: reemplazar n = 500 sin calcular los anteriores', 'Escribir los 500 términos a mano', 'Sumar 5 a 2 una sola vez', 'La fórmula entrega directamente t(500) = 2.497, sin tener que recorrer 499 pasos.'),
        ('abc', 'Una persona dice que la sucesión 2, 4, 8, 14… sigue la regla «suma 2 cada vez». ¿Por qué no es válida?', 'Las diferencias son 2, 4 y 6: no son constantes', 'Porque empieza en 2', 'Porque todos son pares', 'Los pasos entre términos crecen (2, 4, 6), de modo que la regla de sumar siempre 2 no se cumple.'),
        ('=', 'En la sucesión 1, 1, 2, 3, 5, 8… cada término es la suma de los dos anteriores. ¿Cuál es el 8.º término?', '13+8', 'Los términos son 1, 1, 2, 3, 5, 8, 13 y 21: el 8.º es 13 + 8.'),
        ('abc', 'Un programa debe mostrar los seis primeros múltiplos de 4 (4, 8, 12, 16, 20, 24). ¿Qué versión es correcta?', 'for i in range(1, 7): print(4 * i)', 'for i in range(1, 6): print(4 * i)', 'for i in range(6): print(4 * i)', 'range(1, 7) recorre 1 a 6; la segunda se queda en 20 y la tercera parte en 0 y llega solo a 20.'),
    ],
    ctx=('=', 'Un gimnasio cobra $15.000 de inscripción y $12.000 por cada mes. Con la regla costo(n) = 15000 + 12000 · n, ¿cuánto cuesta en total un año completo (12 meses)?', '15000+12000*12', 'Se suma la inscripción a doce mensualidades.'),
    sc=[
        ("En Pensamiento computacional: ¿qué es la regla explícita de una sucesión?", "Una fórmula que da el término n directamente", "Permite calcular cualquier término sin los anteriores."),
        ("¿Cuántas vueltas da un for con range(7)?", "7", "range(7) recorre 0, 1, 2, 3, 4, 5 y 6, que son siete valores."),
        ("¿Qué diferencia constante tiene una sucesión que parte en 10 y sube de 4 en 4?", "4", "Cada término menos el anterior vale 4."),
    ],
    op=("Elige una sucesión: A: 6, 10, 14, 18… o B: 2, 6, 18, 54… Escribe su regla recursiva, y para A también su regla explícita. Escribe un programa que genere sus primeros 6 términos, sigue el programa a mano y comprueba que los términos coinciden con los de la lista dada.",
        "Sucesión A: parte en 6 y suma 4 cada vez; t(n) = 4·n + 2. Programa: t = 6, repetir 6 veces agregando t y sumando 4. Términos: 6, 10, 14, 18, 22, 26. Comprobación: t(6) = 4 · 6 + 2 = 26.",
        ["escribe la regla recursiva correcta", "genera seis términos con un programa", "comprueba con la fórmula o con la lista dada"],
        ["hoja con las reglas, el programa y los seis términos"],
        ["generar un término de más o de menos", "cambiar la constante de paso", "no comprobar con la fórmula"],
        "Pregunta: «¿cuánto sumas o multiplicas en cada paso?». Si no coincide con la diferencia, revisa el paso."),
    reinforce="Escribe los cinco primeros términos de la sucesión con t(n) = 3·n + 1 y comprueba que cada uno suma 3 al anterior.",
    extend="Explica cómo cambiarías el programa de la ficha para que genere la sucesión 3, 6, 12, 24, … y calcula su 7.º término.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (de ejemplo). Dos programas deciden si un entero n ≥ 2 es primo (tiene solo dos divisores: 1 y él mismo). "
     "Programa 1: def primo1(n): ↵ ··for d in range(2, n): ↵ ····if n % d == 0: ↵ ······return False ↵ ··return True. "
     "Programa 2: def primo2(n): ↵ ··d = 2 ↵ ··while d * d <= n: ↵ ····if n % d == 0: ↵ ······return False ↵ ····d = d + 1 ↵ ··return True. "
     "(return termina la función de inmediato; n % d == 0 significa que d divide a n.)")
build(
    O3, 4, F,
    use="Aprenderé a justificar por qué un algoritmo es correcto y a comparar dos algoritmos para el mismo problema contando sus operaciones.",
    prior=["Sé que un primo tiene solo dos divisores.", "Sé usar % para saber si un número divide a otro.", "Sé seguir un for y un while a mano."],
    explain=[
        "Dos algoritmos pueden dar siempre la misma respuesta y aun así hacer muy distinta cantidad de trabajo. Para comparar se cuenta cuántas veces se repite la operación principal, aquí n % d. El programa 1 prueba todos los divisores de 2 a n − 1; el programa 2 prueba solo mientras d · d ≤ n. Para n = 97, que es primo, el programa 1 revisa 95 valores y el programa 2 revisa solo 8.",
        "El programa 2 funciona porque, si n = a · b con a ≤ b, entonces a · a ≤ n. Por eso, si n es compuesto (tiene algún divisor distinto de 1 y de n), tiene alguno que no supera la raíz cuadrada de n (el número que multiplicado por sí mismo da n), y basta probar hasta d · d ≤ n. El detalle importa: si se escribiera d · d < n, primo2(9) devolvería True aunque 9 = 3 · 3 no es primo, porque no probaría d = 3. Los errores en los bordes son típicos.",
        "Justificar un algoritmo significa explicar por qué da la respuesta correcta y por qué termina. En el programa 2, d aumenta de a uno, así que el while termina; y cada vez que continúa se sabe que ningún d probado dividió a n. Un algoritmo más eficiente puede ser más difícil de entender, y por eso se justifica con un argumento y se prueba con casos, incluidos 2, 4 y los cuadrados de primos.",
    ],
    vocab=[("número primo", "número mayor que 1 con solo dos divisores: 1 y él mismo"), ("eficiencia", "cantidad de trabajo que hace un algoritmo"), ("operación principal", "paso que más se repite y que se cuenta"), ("caso borde", "valor justo en el límite de una condición"), ("justificar", "explicar con argumentos por qué algo es correcto")],
    worked=[
        ("Contar operaciones", "Para n = 13 (primo), ¿cuántas veces calcula n % d cada programa?", ["primo1 prueba d = 2, 3, … 12: son 11 valores.", "primo2 prueba d = 2 y d = 3; con d = 4, 16 > 13 y se detiene: 2 valores."], "primo1 hace 11 cálculos y primo2 hace 2"),
        ("Un caso borde", "¿Qué devuelve primo2(9)?", ["d = 2: 4 <= 9 y 9 % 2 = 1, así que sigue con d = 3.", "d = 3: 9 <= 9 se cumple y 9 % 3 = 0, por lo que devuelve False."], "Devuelve False, porque 9 = 3 · 3 no es primo"),
    ],
    mistakes=[("Escribir d * d < n en vez de d * d <= n.", "Deja de probar justo en el divisor que es la raíz exacta, como el 3 en 9.", "Prueba el programa con cuadrados de primos, como 9, 25 o 49."),
              ("Creer que primo1 falla con n = 2 porque range(2, 2) está vacío.", "El for no se ejecuta y la función llega a return True, que es correcto.", "Sigue el programa a mano con los casos más pequeños.")],
    T=[
        ('abc', '{F} ¿Qué devuelve primo1(15)?', 'False', 'True', '3', 'Con d = 3, 15 % 3 es 0 y devuelve False; 3 es el divisor encontrado, no el resultado.'),
        ('abc', '{F} ¿Cuántos valores de d revisa primo1(7), que es primo?', '5', '7', '6', 'range(2, 7) recorre 2, 3, 4, 5 y 6, o sea 5 valores.'),
        ('ab', '{F} ¿Qué hace return False dentro del for de primo1?', 'Termina la función y entrega False', 'Solo salta a la siguiente vuelta del for', 'return termina la función en el acto, sin seguir con las demás vueltas.'),
        ('abc', '{F} ¿Cuántas veces se calcula n % d en primo2(37), que es primo?', '5', '6', '35', 'Prueba d = 2, 3, 4, 5 y 6; con d = 7, 7 · 7 = 49 supera a 37 y el while se detiene.'),
        ('=', '{F} ¿Cuántos valores de d revisa primo1(41), que es primo?', '41-2', 'range(2, 41) recorre desde 2 hasta 40.'),
        ('abc', '{F} ¿Qué devuelve primo2(21)?', 'False', 'True', '3', 'Con d = 3 se cumple 3 · 3 <= 21 y 21 % 3 es 0, así que devuelve False.'),
        ('{F} ¿Cuántas veces se calcula n % d en primo2(49)?', '6', 'Prueba d = 2, 3, 4, 5, 6 y 7; con d = 7 encuentra que divide a 49 y devuelve False.'),
        ('=', '{F} ¿Cuántos valores de d revisa primo1(71), que es primo?', '71-2', 'range(2, 71) recorre 2 hasta 70.'),
        ('{F} ¿Cuántos valores de d revisa primo2(71)?', '7', 'Prueba d = 2 hasta 8, porque 8 · 8 = 64 <= 71 y 9 · 9 = 81 supera a 71.'),
        ('abc', '{F} Una persona cambia <= por < en el while de primo2. ¿Qué falla?', 'primo2(9) devolvería True aunque 9 no es primo', 'primo2(13) devolvería False', 'El programa nunca terminaría', 'Con < no prueba d = 3 para n = 9 y concluye que es primo, lo cual es incorrecto.'),
        ('abc', 'primo1 revisa 95 valores para 97 y primo2 revisa 8. Un compañero concluye: «primo2 es mejor siempre, aunque sea más difícil de entender». ¿Qué juicio es más completo?', 'primo2 es más eficiente y sigue siendo correcto; su mayor complejidad se justifica con un argumento y pruebas', 'primo1 es mejor porque es más corto', 'No se pueden comparar porque dan resultados distintos', 'Entre algoritmos correctos se evalúa la eficiencia, siempre que la versión más compleja se justifique.'),
        ('abc', '{F} ¿Por qué basta probar los divisores d con d · d <= n?', 'Si n = a · b con a ≤ b, entonces a · a ≤ n: todo número compuesto tiene un divisor no mayor que su raíz', 'Porque los divisores mayores no existen', 'Porque n % d es siempre 0 para d grande', 'Si un divisor a es el menor de los dos factores, su cuadrado no supera a n.'),
        ('{F} ¿Qué devuelven primo2(2) y primo2(4)?', 'primo2(2) devuelve True y primo2(4) devuelve False', 'Para 2 el while no se ejecuta (4 > 2) y devuelve True; para 4, d = 2 cumple 4 <= 4 y 4 % 2 = 0.'),
    ],
    ctx=('abc', 'Un colegio comprueba con primo2 si 101 es primo (lo es). ¿Cuál es el mayor valor de d que revisa?', '10', '100', '11', '10 · 10 = 100 <= 101, pero 11 · 11 = 121 supera a 101, así que el último d es 10.'),
    sc=[
        ("En Matemática: ¿cuántos divisores tiene un número primo?", "Dos: 1 y él mismo", "Esa es la definición de número primo."),
        ("En Pensamiento computacional: ¿qué hace return dentro de una función?", "Termina la función y entrega un valor", "Las líneas que siguen a un return ejecutado ya no se leen."),
        ("En Pensamiento computacional: ¿para qué sirve contar las operaciones de un algoritmo?", "Para comparar su eficiencia con la de otro", "Menos operaciones para la misma respuesta indica un algoritmo más eficiente."),
    ],
    op=("Sigue primo2 con los números 29, 35 y 36. Para cada uno arma una tabla con d, n % d y la decisión, anota cuántas veces se calcula n % d y si el resultado es True o False. Compara con cuántas veces lo calcularía primo1 y escribe una frase de conclusión.",
        "Para 29: d = 2 (resto 1), 3 (resto 2), 4 (resto 1) y 5 (resto 4); con d = 6, 36 > 29. Son 4 cálculos y devuelve True. primo1 haría 27. Para 35 se detiene en d = 5 (resto 0) y devuelve False; para 36 en d = 2.",
        ["completa las tablas con los restos correctos", "cuenta las operaciones de cada programa", "concluye comparando con datos"],
        ["hoja con tres tablas de seguimiento y una conclusión"],
        ["parar una vuelta antes por usar <", "contar mal los valores de range", "no comparar con el otro programa"],
        "Pregunta: «¿hasta qué valor de d llegaste y por qué?». Si no usa d · d <= n, repasa la condición."),
    reinforce="Sigue a mano primo1 y primo2 con n = 25 y anota cuántos cálculos de n % d hace cada uno.",
    extend="Explica por qué el programa 2 no necesita probar divisores mayores que la raíz de n y qué pasaría con n = 10.007 en comparación con el programa 1.",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (de ejemplo). Un procesador simbólico (CAS, por «sistema de álgebra computacional») trabaja con expresiones con letras y entrega resultados exactos. "
     "Órdenes y salidas de ejemplo (formato inventado y simple): expandir((x + 3)^2) → x^2 + 6x + 9; factorizar(x^2 − 9) → (x − 3)(x + 3); resolver(2x + 6 = 0, x) → x = −3; evaluar(x^2 + 1, x = 4) → 17. "
     "El signo ^ es la potencia y los paréntesis ordenan las operaciones.")
build(
    O4, 1, F,
    use="Aprenderé qué hace un procesador simbólico, a interpretar sus órdenes y salidas, y a comprobar a mano que un resultado es correcto.",
    prior=["Sé expandir y factorizar expresiones algebraicas simples.", "Sé resolver una ecuación de primer grado.", "Sé reemplazar una letra por un valor."],
    explain=[
        "Un procesador simbólico (CAS) es un programa que opera con expresiones con letras, no solo con números: puede expandir, factorizar, resolver ecuaciones y evaluar. Se le da una orden (por ejemplo expandir((x + 3)^2)) y entrega una expresión exacta (x^2 + 6x + 9). Su resultado no es de fiar a ciegas: depende de lo que se escribió, y una expresión mal escrita produce una respuesta correcta para otra pregunta.",
        "La precedencia importa: x + 3^2 calcula primero 3^2 = 9 y entrega x + 9, mientras que (x + 3)^2 eleva al cuadrado todo el binomio (una suma de dos términos). Por eso se revisan los paréntesis y las potencias antes de ejecutar la orden. Cuando la entrada no tiene sentido, el programa debería mostrar un mensaje de error en vez de un resultado.",
        "Una aplicación que usa un CAS tiene entrada (la expresión), una orden, una salida y una validación. Los resultados se comprueban con la operación inversa o por sustitución. Para una factorización se expande el resultado y debe volver la expresión original; para una ecuación se reemplaza la solución y debe cumplirse la igualdad. Un valor de prueba nunca demuestra una identidad (una igualdad que se cumple para todos los valores de x), pero un valor que falla sí la refuta.",
    ],
    vocab=[("procesador simbólico", "programa que opera con expresiones con letras"), ("expandir", "quitar paréntesis multiplicando"), ("factorizar", "escribir como producto"), ("evaluar", "reemplazar letras por valores"), ("precedencia", "orden en que se calculan las operaciones"), ("verificar", "comprobar con otro camino que un resultado es correcto")],
    worked=[
        ("Verificar una expansión", "El CAS entrega expandir((x + 3)^2) → x^2 + 6x + 9. Verifícalo a mano.", ["(x + 3)^2 = x^2 + 2·x·3 + 3^2.", "Eso da x^2 + 6x + 9: coincide. El error frecuente es x^2 + 9."], "La salida del CAS es correcta"),
        ("Verificar una solución", "El CAS resuelve 3x − 12 = 0 y entrega x = 4. Compruébalo.", ["Reemplaza x = 4: 3 · 4 − 12 = 12 − 12.", "El resultado es 0, como pedía la ecuación."], "x = 4 es solución"),
    ],
    mistakes=[("Escribir x + 3^2 cuando se quería (x + 3)^2.", "Sin paréntesis, la potencia afecta solo al 3.", "Usa paréntesis y revisa cómo se ve la expresión antes de ejecutar."),
              ("Aceptar la salida del programa sin verificarla.", "Un error al escribir la entrada produce una respuesta bien calculada pero a otra pregunta.", "Comprueba por sustitución o con la operación inversa.")],
    T=[
        ('abc', 'Con la orden factorizar de la ficha, ¿qué debería entregar factorizar(x^2 − 16)?', '(x − 4)(x + 4)', '(x − 8)(x − 2)', '(x − 4)^2', 'Es una diferencia de cuadrados: x^2 − 4^2 = (x − 4)(x + 4); (x − 8)(x − 2) daría x^2 − 10x + 16.'),
        ('abc', '{F} ¿Qué entrega evaluar(x^2 + 1, x = 5)?', '26', '11', '36', 'Con x = 5: 5^2 + 1 = 26; 11 resulta de multiplicar por 2 en vez de elevar al cuadrado y 36 de elevar (5 + 1).'),
        ('ab', '¿Con qué trabaja un procesador simbólico?', 'Con expresiones con letras y resultados exactos', 'Solo con decimales aproximados', 'Opera con expresiones algebraicas completas, no solo con números aproximados.'),
        ('abc', '{F} ¿Qué debería entregar resolver(3x + 12 = 0, x)?', 'x = −4', 'x = 4', 'x = 12', '3x = −12, de modo que x = −4; x = 4 viene de olvidar el signo del 12.'),
        ('=', 'Para verificar a mano expandir((x + 6)^2), ¿cuánto vale el coeficiente de x, que sale de 2 · 6?', '2*6', 'El término cruzado del cuadrado de un binomio es el doble del producto de los dos términos.'),
        ('abc', 'En un CAS, escribir x + 3^2 en vez de (x + 3)^2 cambia el resultado. ¿Por qué?', 'Primero se calcula 3^2 = 9 y solo después se suma x; faltan los paréntesis', 'Porque el CAS no entiende el signo ^', 'No cambia: son lo mismo', 'La potencia tiene precedencia sobre la suma, y sin paréntesis solo afecta al 3.'),
        ('=', 'El CAS evalúa x^2 − 5x con x = 6. Calcula a mano el resultado que debe entregar.', '6*6-5*6', 'Se reemplaza x por 6: 36 menos 30.'),
        ('abc', 'Se quiere que un CAS desarrolle (x − 5)^2. ¿Qué salida es correcta?', 'x^2 − 10x + 25', 'x^2 + 25', 'x^2 + 10x + 25', 'El término cruzado es 2 · (−5) · x = −10x; x^2 + 25 lo omite y x^2 + 10x + 25 cambia su signo.'),
        ('El CAS resuelve 4x − 20 = 0. ¿Qué valor de x debe entregar?', 'x = 5', '4x = 20, y al dividir por 4 se obtiene 5; con x = 5: 4 · 5 − 20 = 0.'),
        ('abc', 'Un CAS entrega x = 2 como solución de 3x + 1 = 10 (puede que se haya escrito mal la ecuación). ¿Es correcta?', 'No: 3 · 2 + 1 = 7, no 10; la solución correcta es x = 3', 'Sí: el CAS nunca se equivoca', 'Sí: porque 2 es menor que 3', 'Al reemplazar 2 se obtiene 7, que no es 10; verificar permite detectar el error.'),
        ('abc', 'Una app de práctica recibe una expresión del estudiante y muestra su forma factorizada con un CAS. ¿Qué validación es esencial antes de ejecutar la orden?', 'Revisar que la expresión esté bien escrita (paréntesis, potencias) y avisar si no se puede interpretar', 'Ninguna, porque el CAS nunca falla', 'Convertir siempre la expresión a decimal', 'Una entrada mal escrita produce una salida válida para otra pregunta; la validación evita ese error.'),
        ('abc', '{F} El CAS factoriza x^2 − 9 como (x − 3)(x + 3). ¿Qué verificación comprueba esa salida?', 'Expandir (x − 3)(x + 3) y ver que vuelve x^2 − 9', 'Reemplazar x por 0 una sola vez', 'Confiar en la salida', 'La operación inversa de factorizar es expandir; si vuelve la expresión original, está bien.'),
        ('Una compañera dice que (x + 2)^2 = x^2 + 4. Reemplaza x = 1 en ambos lados. ¿Qué valores obtienes y qué concluyes?', '9 y 5: son distintos, así que la igualdad no es válida', 'Con x = 1: (1 + 2)^2 = 9 y 1^2 + 4 = 5; un solo valor que falla basta para refutarla.'),
    ],
    ctx=('abc', 'Una app de práctica pide factorizar x^2 − 49 y compara con la respuesta del CAS, (x − 7)(x + 7). Si el estudiante escribe (x − 7)^2, ¿qué diagnóstico debe mostrar la app?', 'Incorrecto: al expandir (x − 7)^2 resulta x^2 − 14x + 49, no x^2 − 49', 'Correcto', 'Incorrecto: debía ser x^2 + 49', 'Al expandir el cuadrado aparece el término −14x, que no está en x^2 − 49.'),
    sc=[
        ("En Pensamiento computacional: ¿qué entrega un procesador simbólico?", "Resultados exactos en forma de expresiones", "Opera con letras y entrega expresiones, no solo números aproximados."),
        ("En Matemática: ¿cómo se comprueba una solución de una ecuación?", "Reemplazando el valor en la ecuación original", "Si se cumple la igualdad, la solución es válida."),
        ("En Matemática: ¿qué operación comprueba una factorización?", "Expandir los factores", "Al multiplicar los factores debe volver la expresión original."),
    ],
    op=("Elige tres órdenes de este conjunto o usa las tres: (a) expandir((x − 2)^2), (b) factorizar(x^2 − 25), (c) resolver(5x − 15 = 0, x). Para cada una predice la salida que debería entregar un CAS, escribe cómo la verificarías a mano y anota un error de escritura posible (por ejemplo, un paréntesis olvidado).",
        "(a) x^2 − 4x + 4; se verifica con (x − 2)(x − 2) por distribución. (b) (x − 5)(x + 5); se expande para volver a x^2 − 25. (c) x = 3; se reemplaza: 5 · 3 − 15 = 0. Error posible: escribir x − 2^2, que daría x − 4.",
        ["predice las tres salidas correctamente", "propone una verificación para cada una", "identifica un error de escritura posible"],
        ["hoja con las predicciones, las verificaciones y el error posible"],
        ["olvidar el término cruzado", "no verificar por sustitución", "confundir x − 2^2 con (x − 2)^2"],
        "Pregunta: «¿cómo sabes que tu resultado es correcto?». Si no tiene verificación, pídele una."),
    reinforce="Expande a mano (x + 4)^2 y comprueba tu resultado reemplazando x = 1 en ambos lados.",
    extend="Explica por qué un CAS puede dar una respuesta distinta a la esperada sin estar equivocado, y qué debe revisar la persona usuaria.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (de ejemplo). En un programa de geometría dinámica se construye un triángulo con tres puntos libres A, B y C (se pueden arrastrar con el cursor) y el punto M, punto medio de AB, que depende de A y B y no se arrastra solo. "
     "El programa muestra medidas que se actualizan al arrastrar. Tabla de ejemplo con tres posiciones: posición 1: ángulos A = 50°, B = 60°, C = 70°; posición 2: A = 90°, B = 30°, C = 60°; posición 3: A = 35°, B = 35°, C = 110°. "
     "Coordenadas: A(2, 2) y B(8, 4); el punto medio es M = ((2 + 8)/2, (2 + 4)/2).")
build(
    O4, 2, F,
    use="Aprenderé a explorar una figura con geometría dinámica, a distinguir puntos libres y dependientes, a hallar invariantes y a representar el mismo resultado con coordenadas.",
    prior=["Sé ubicar puntos con coordenadas.", "Sé que los ángulos de un triángulo suman 180°.", "Sé calcular el punto medio de un segmento."],
    explain=[
        "En geometría dinámica una figura se construye con puntos y herramientas, y se puede mover. Un punto libre se arrastra con el cursor; un punto dependiente se calcula a partir de otros y se mueve cuando ellos se mueven. El punto medio M de AB es dependiente: si arrastras A o B, M se recalcula. Si M se dibujara a ojo, al arrastrar dejaría de estar en el medio.",
        "Arrastrar permite explorar: se observa qué cambia y qué no. Lo que no cambia al arrastrar se llama invariante. En la tabla de la ficha, los ángulos de las tres posiciones cambian, pero su suma siempre es 180°. Esa observación sugiere una conjetura, que es una afirmación que parece cierta. Una conjetura no está demostrada: tres posiciones, o cien, no la prueban para todos los triángulos.",
        "Una misma figura se puede representar de dos maneras: con la construcción dinámica y con coordenadas. El punto medio de (a, b) y (c, d) es ((a + c)/2, (b + d)/2); con A(2, 2) y B(8, 4) resulta M(5, 3). Si A se mueve a (4, 6), M se recalcula como ((4 + 8)/2, (6 + 4)/2) = (6, 5). El resultado se valida con los dos caminos y, para afirmar algo general, se necesita una demostración.",
    ],
    vocab=[("geometría dinámica", "programa para construir figuras que se pueden mover"), ("punto libre", "punto que se arrastra con el cursor"), ("punto dependiente", "punto que se calcula a partir de otros"), ("invariante", "propiedad que no cambia al arrastrar"), ("conjetura", "afirmación que parece cierta pero no está demostrada"), ("demostración", "argumento válido para todos los casos")],
    worked=[
        ("Punto medio con coordenadas", "Calcula las coordenadas de M, punto medio de A(2, 2) y B(8, 4).", ["Suma las x y divide por 2: (2 + 8)/2 = 5.", "Suma las y y divide por 2: (2 + 4)/2 = 3."], "M = (5, 3)"),
        ("Detectar un invariante", "En la tabla, ¿qué se mantiene igual en las tres posiciones?", ["Suma las medidas de cada fila: 50 + 60 + 70, 90 + 30 + 60 y 35 + 35 + 110.", "Las tres sumas dan 180."], "La suma de los ángulos es un invariante: 180°"),
    ],
    mistakes=[("Creer que probar tres posiciones demuestra una propiedad.", "Los ejemplos sugieren una conjetura, pero no cubren todos los casos.", "Escribe «conjetura» hasta tener un argumento válido para todos."),
              ("Construir un punto «a ojo» cerca del medio.", "Al arrastrar los extremos deja de estar en el medio.", "Usa la herramienta de punto medio, para que sea dependiente.")],
    T=[
        ('abc', 'Un segmento tiene extremos C(4, 0) y D(10, 8). ¿Cuáles son las coordenadas de su punto medio?', '(7, 4)', '(14, 8)', '(6, 8)', 'Se promedian las coordenadas: (4 + 10)/2 = 7 y (0 + 8)/2 = 4; (14, 8) las suma sin dividir.'),
        ('abc', '{F} ¿Cuál de estos puntos es libre?', 'A', 'M', 'Ninguno', 'A se puede arrastrar; M depende de A y B, así que no es libre.'),
        ('ab', '{F} ¿Qué es un invariante en geometría dinámica?', 'Una propiedad que no cambia al arrastrar los puntos libres', 'Un punto que no se puede ver', 'Es lo que permanece igual aunque se mueva la figura, como la suma de los ángulos.'),
        ('=', '{F} Se arrastra el triángulo a una cuarta posición y se miden A = 80° y B = 55°. Si la suma se mantiene, ¿cuánto mide C?', '180-80-55', 'Si la suma de los tres ángulos es un invariante de 180°, C = 180° − 80° − 55°.', '°'),
        ('abc', '{F} ¿Qué se mantiene igual en las tres posiciones de la tabla?', 'La suma de los tres ángulos', 'El valor del ángulo A', 'El ángulo mayor', 'Cada ángulo cambia de una posición a otra, pero las sumas siempre dan 180°.'),
        ('abc', '{F} Si se arrastra el punto A, ¿qué ocurre con M?', 'Se mueve, porque depende de A y B', 'No se mueve', 'Desaparece', 'Un punto dependiente se recalcula cuando cambian los puntos de los que depende.'),
        ('Un segmento tiene extremos P(−4, 2) y Q(6, −8). ¿Cuáles son las coordenadas de su punto medio?', '(1, −3)', '(−4 + 6)/2 = 1 y (2 + (−8))/2 = −3.'),
        ('El punto medio de AB es M(7, 3) y el extremo A es (2, −1). ¿Cuáles son las coordenadas de B?', '(12, 7)', 'Si (2 + x)/2 = 7, entonces x = 12; si (−1 + y)/2 = 3, entonces y = 7.'),
        ('abc', 'Se conjetura que los cuatro ángulos de un cuadrilátero suman 360°. Si tres ángulos miden 80°, 100° y 90°, ¿cuánto debe medir el cuarto?', '90°', '100°', '80°', 'Los tres suman 270° y 360° − 270° = 90°.'),
        ('abc', '{F} Un compañero afirma: «como probé tres posiciones y la suma dio 180°, ya está demostrado para todos los triángulos». ¿Qué respuesta es correcta?', 'Las posiciones sugieren una conjetura fuerte, pero una demostración requiere argumentos válidos para todos los casos', 'Está demostrado', 'La conjetura es falsa', 'Los ejemplos no cubren todos los triángulos posibles, por lo que no son una demostración.'),
        ('abc', 'Se construye M como «punto cualquiera cerca del medio» en vez de usar la herramienta de punto medio. Al arrastrar A, ¿qué ocurre?', 'M deja de estar en el medio: no depende de A y B', 'M se mantiene en el medio', 'M se vuelve libre pero sigue en el medio', 'Un punto puesto a ojo no está ligado a A y B, así que no se recalcula.'),
        ('abc', '{F} En tres posiciones se mide que AM = MB. ¿Es una conjetura o una consecuencia de la construcción?', 'Es una consecuencia de haber construido M como punto medio', 'Es una conjetura que hay que demostrar', 'Es un error de medición', 'M se definió como el punto medio, así que AM = MB se cumple por construcción.'),
        ('{F} Si A(2, 2) se arrastra a (6, 8) y B(8, 4) no se mueve, ¿dónde queda M?', '(7, 6)', 'M = ((6 + 8)/2, (8 + 4)/2) = (7, 6).'),
    ],
    ctx=('abc', 'Un estudiante mide las diagonales de tres rectángulos en un programa de geometría dinámica: 5 y 5, 10 y 10, y 13 y 13 (de ejemplo). ¿Qué puede concluir con prudencia?', 'Que las diagonales parecen ser iguales (conjetura) y que debe justificarlo con un argumento válido', 'Que ya está demostrado para todos los rectángulos', 'Que la propiedad es falsa', 'Tres mediciones sugieren la propiedad, pero la certeza exige una demostración.'),
    sc=[
        ("En geometría dinámica: ¿qué puntos se pueden arrastrar directamente?", "Los puntos libres", "Los puntos dependientes se recalculan solos."),
        ("En Matemática: ¿cómo se calcula el punto medio de (a, b) y (c, d)?", "((a + c)/2, (b + d)/2)", "Se promedian las coordenadas x y las coordenadas y."),
        ("En Matemática: ¿qué diferencia hay entre una conjetura y una demostración?", "La conjetura es una afirmación probable; la demostración la prueba para todos los casos", "Los ejemplos sugieren; solo la demostración asegura."),
    ],
    op=("Un cuadrilátero ABCD se midió en tres posiciones (de ejemplo): posición 1: 85°, 95°, 100°, 80°; posición 2: 90°, 90°, 90°, 90°; posición 3: 60°, 120°, 70°, 110°. "
        "Calcula la suma de cada posición, escribe una conjetura, explica por qué las tres posiciones no bastan para demostrarla y describe cómo comprobarías con coordenadas que el punto medio de una diagonal está entre sus extremos.",
        "Las sumas son 360°, 360° y 360°; conjetura: los ángulos de un cuadrilátero suman 360°. No basta porque son solo tres casos. Con coordenadas: para A(0, 0) y C(6, 4), el punto medio es (3, 2).",
        ["calcula las tres sumas correctamente", "formula una conjetura clara", "explica por qué no basta con ejemplos"],
        ["hoja con las sumas, la conjetura y la explicación"],
        ["afirmar que está demostrado", "sumar mal", "confundir punto libre con dependiente"],
        "Pregunta: «¿cuántos casos faltarían para demostrar?». Si responde un número, recuérdale que se necesita un argumento general."),
    reinforce="Calcula el punto medio de los segmentos de extremos (1, 1) y (7, 5), y de (−2, 0) y (4, 6).",
    extend="Explica por qué la suma de 180° en un triángulo se puede demostrar y por qué las medidas del programa solo la sugieren.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (de ejemplo). Minutos de uso diario de una app de cinco estudiantes (datos de ejemplo): datos = [20, 25, 25, 30, 100]. "
     "Programa de análisis: suma = 0 ↵ for d in datos: ↵ ··suma = suma + d ↵ media = suma // len(datos) ↵ ordenados = sorted(datos) ↵ mediana = ordenados[len(datos) // 2]. "
     "(sorted ordena de menor a mayor; la mediana es el valor central de los datos ordenados; la moda es el valor que más se repite; el rango es el máximo menos el mínimo.)")
build(
    O4, 3, F,
    use="Aprenderé a calcular media, mediana, moda y rango con un programa o una hoja de cálculo, a interpretar el efecto de un valor atípico y a elegir la medida adecuada.",
    prior=["Sé calcular un promedio.", "Sé ordenar una lista de menor a mayor.", "Sé leer una tabla de datos."],
    explain=[
        "El análisis estadístico describe un conjunto de datos con medidas. La media es la suma dividida por la cantidad de datos; la mediana es el valor central de los datos ordenados (si hay una cantidad par, es el promedio de los dos centrales); la moda es el valor que más se repite; y el rango es el máximo menos el mínimo. Un programa o una hoja de cálculo hace las cuentas, pero la persona elige la medida y la interpreta.",
        "Un valor atípico es un dato muy alejado de los demás. En la ficha, 100 minutos eleva la media a 40, aunque cuatro de los cinco estudiantes usan 30 minutos o menos. La mediana, 25, casi no cambia con ese valor. Por eso, con valores atípicos suele describir mejor el caso típico la mediana, mientras que la media los incluye. El rango también refleja ese dato: 100 − 20 = 80.",
        "En una hoja de cálculo o en un programa hay que cuidar la calidad de los datos: un número escrito como texto, una celda vacía o un error de digitación cambian los resultados. Antes de calcular se revisan los datos, y después se explica el resultado con palabras: «el estudiante típico usa unos 25 minutos, pero hay un caso extremo de 100».",
    ],
    vocab=[("media", "suma de los datos dividida por la cantidad"), ("mediana", "valor central de los datos ordenados"), ("moda", "valor que más se repite"), ("rango", "máximo menos mínimo"), ("valor atípico", "dato muy alejado de los demás"), ("hoja de cálculo", "programa que organiza datos en celdas y calcula con ellos")],
    worked=[
        ("Calcular las medidas", "Datos de ejemplo: 8, 10, 10, 12, 15. Calcula media, mediana, moda y rango.", ["Suma: 55; la media es 55 // 5 = 11. Los datos ya están ordenados: la mediana es el tercero, 10.", "La moda es 10 (aparece dos veces) y el rango es 15 − 8 = 7."], "Media 11, mediana 10, moda 10, rango 7"),
        ("Efecto de un valor atípico", "En la ficha, ¿qué ocurre con la media si se quita el 100?", ["Quedan 20, 25, 25 y 30, que suman 100.", "La media es 100 // 4 = 25."], "La media baja de 40 a 25, igual que la mediana"),
    ],
    mistakes=[("Calcular la mediana sin ordenar los datos.", "El valor central solo tiene sentido en datos ordenados.", "Ordena de menor a mayor antes de ubicar el centro."),
              ("Creer que la media siempre es la mejor medida.", "Un valor atípico la desplaza mucho.", "Compara media y mediana, y explica la diferencia.")],
    T=[
        ('abc', '{F} ¿Qué valor tendría media si los datos fueran [20, 25, 25, 30, 50]?', '30', '25', '150', 'La suma es 150 y 150 // 5 = 30; 25 sería la mediana y 150 es la suma.'),
        ('abc', '{F} ¿Qué índice de la lista ordenados usa el programa para la mediana?', '2', '3', '5', 'len(datos) // 2 = 5 // 2 = 2; el índice 2 es el tercer valor porque los índices parten en 0.'),
        ('ab', '{F} ¿Cuál es la moda?', '25, que se repite dos veces', '100, el mayor valor', 'La moda es el valor que más se repite, no el más grande.'),
        ('=', '{F} Si el valor 100 se cambiara por 60, ¿cuánto valdría el rango (máximo menos mínimo)?', '60-20', 'El rango resta el menor valor al mayor: 60 − 20.'),
        ('abc', '{F} ¿Qué medida describe mejor el uso típico, dado el valor de 100?', 'La mediana, porque el 100 casi no la afecta', 'La media, porque usa todos los datos y por eso siempre es la mejor', 'El rango', 'La mediana vale 25, cerca de la mayoría; la media 40 queda alejada por el valor atípico.'),
        ('=', '{F} Si el dato 100 se cambia por 40, ¿cuánto vale la nueva media?', '(20+25+25+30+40)//5', 'Los cinco datos suman 140 y 140 // 5 = 28.'),
        ('=', 'Datos de ejemplo: 6, 8, 8, 9, 14. ¿Cuánto vale la media?', '(6+8+8+9+14)//5', 'La suma es 45 y hay cinco datos.'),
        ('Datos de ejemplo: 6, 8, 8, 9, 14. ¿Cuál es la mediana?', '8', 'Con cinco datos ordenados, el central es el tercero, que vale 8.'),
        ('=', 'Datos de ejemplo: 3, 5, 7, 9 (cuatro valores ordenados). ¿Cuánto vale la mediana?', '(5+7)//2', 'Con cantidad par, la mediana es el promedio de los dos valores centrales.'),
        ('abc', 'Un curso tiene notas 40, 40, 45, 50 y 70 (escala de 10 a 70). Se afirma: «la media es 49, así que 49 representa bien al curso». ¿Qué comentario es válido?', 'La media es 49 y la mediana 45: el 70 sube la media, y la mediana describe mejor al curso típico', 'Es válido: la media siempre representa bien', 'La media debería ser 70', 'Una nota alta eleva la media; comparar con la mediana muestra que el curso típico está más abajo.'),
        ('abc', 'Una hoja de cálculo calcula la media de la columna «edad», pero una celda dice «dieciséis» escrito con letras. ¿Qué ocurre lo más probable?', 'El dato queda fuera del cálculo o produce un error: hay que corregirlo', 'La hoja lo convierte siempre bien', 'La media será 0', 'Un número escrito con letras no es un valor numérico para la hoja, y distorsiona el resultado.'),
        ('=', 'Cinco datos tienen media 12 (suma 60). Se agrega un sexto dato igual a 24. ¿Cuánto vale la nueva media?', '(60+24)//6', 'La nueva suma es 84 y hay seis datos.'),
        ('abc', 'Dos cursos tienen media 50 puntos: el curso A tiene 49, 50 y 51; el curso B tiene 10, 50 y 90. ¿Qué medida muestra la diferencia entre ellos?', 'El rango: 2 en A y 80 en B', 'La media', 'La moda', 'La media es igual en ambos, pero el rango mide cuán dispersos están los datos.'),
    ],
    ctx=('abc', 'Una app de pasos muestra los pasos de una semana (datos de ejemplo): 4.000, 5.000, 5.000, 6.000, 4.000, 5.000 y 15.000 (un día de excursión). ¿Cuál es la mediana?', '5.000', '15.000', '44.000', 'Ordenados: 4.000, 4.000, 5.000, 5.000, 5.000, 6.000, 15.000; el cuarto valor es 5.000.'),
    sc=[
        ("En Estadística: ¿qué medida se ve poco afectada por valores muy grandes o muy pequeños?", "La mediana", "La mediana depende del centro de los datos ordenados, no de los extremos."),
        ("En Estadística: ¿qué se calcula con máximo menos mínimo?", "El rango", "El rango mide cuánto se separan los extremos."),
        ("¿Qué hay que hacer con los datos antes de buscar la mediana?", "Ordenarlos de menor a mayor", "El valor central solo se ubica con los datos ordenados."),
    ],
    op=("Elige un conjunto de datos de ejemplo. Opción 1: minutos de lectura de cinco estudiantes: 10, 15, 15, 20, 90. Opción 2: goles por partido en siete partidos: 0, 1, 1, 2, 2, 2, 6. "
        "Calcula media (con //), mediana, moda y rango; identifica si hay un valor atípico y explica con palabras qué medida elegirías para describir un caso típico.",
        "Opción 1: suma 150, media 30, mediana 15, moda 15, rango 80. El 90 es atípico: la media (30) es mayor que casi todos los datos; para el caso típico conviene la mediana (15).",
        ["calcula las cuatro medidas correctamente", "identifica el valor atípico", "elige una medida con una explicación"],
        ["hoja con los cálculos y una explicación breve"],
        ["no ordenar antes de la mediana", "confundir moda con mediana", "elegir la media sin discutir el valor atípico"],
        "Pregunta: «¿qué pasa con cada medida si quitas el valor más grande?». Si no sabe, pídele que la recalcule."),
    reinforce="Calcula media, mediana, moda y rango de 5, 7, 7, 8, 13 (datos de ejemplo).",
    extend="Explica por qué en dos grupos con la misma media puede ser importante comparar también el rango.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (de ejemplo). Seis estudiantes (datos de ejemplo): horas de estudio semanales (x) y puntaje en una prueba de 0 a 100 (y): (1, 40), (2, 50), (3, 55), (4, 70), (5, 75), (6, 90). "
     "Un programa de análisis estadístico entrega la recta de ajuste y = 10x + 30, una línea que resume la tendencia (es aproximada). Gráfico de dispersión: cada estudiante es un punto (x, y).")
build(
    O4, 4, F,
    use="Aprenderé a interpretar un gráfico de dispersión y una recta de ajuste para estimar valores, y a distinguir asociación de causalidad y estimación de extrapolación.",
    prior=["Sé ubicar puntos en un plano.", "Sé reemplazar x en una fórmula y = ax + b.", "Sé calcular la media y el rango."],
    explain=[
        "Un gráfico de dispersión muestra dos variables a la vez: cada caso es un punto (x, y). Si al aumentar x tiende a aumentar y, la relación es positiva; si y tiende a bajar, es negativa; si no hay un patrón, no hay relación clara. Una recta de ajuste resume la tendencia con una fórmula, por ejemplo y = 10x + 30: por cada hora más de estudio, el puntaje estimado sube 10 puntos.",
        "Con la recta se estima. Para 4 horas, 10 · 4 + 30 = 70 puntos. La diferencia entre el valor real y el estimado muestra cuánto se aleja un caso de la tendencia: el estudiante de 5 horas obtuvo 75 y la recta estima 80. Estimar dentro del rango de los datos observados (aquí de 1 a 6 horas) es más confiable. Fuera de ese rango se extrapola: para 10 horas la recta da 130, lo que es imposible porque el máximo es 100.",
        "Una asociación entre dos variables no prueba que una cause la otra. Puede haber un tercer factor: si suben las ventas de helados y las quemaduras de sol, ambas suben por el calor, no una por la otra. Además, la recta describe una tendencia del grupo, no promete el resultado de una persona. Un dato muy alejado se revisa: puede ser un error o un caso especial, y puede cambiar la recta.",
    ],
    vocab=[("gráfico de dispersión", "gráfico de puntos (x, y) de dos variables"), ("recta de ajuste", "recta que resume la tendencia de los puntos"), ("tendencia", "dirección general en que cambian los datos"), ("extrapolar", "estimar fuera del rango de los datos observados"), ("causalidad", "relación en que una cosa produce la otra"), ("asociación", "relación entre dos variables que cambian juntas")],
    worked=[
        ("Estimar y extrapolar", "Con la recta de la ficha, ¿qué puntaje se estima para 7 horas y para 10 horas?", ["Para 7 horas: 10 · 7 + 30 = 100. Para 10 horas: 10 · 10 + 30 = 130.", "Los datos llegan hasta 6 horas y el puntaje máximo es 100."], "7 horas da 100 y 10 horas da 130, un valor imposible: no se debe extrapolar así"),
        ("Diferencia con el valor real", "El estudiante de 3 horas obtuvo 55. ¿Cuál es la diferencia con lo estimado?", ["La recta estima 10 · 3 + 30 = 60.", "La diferencia es 60 − 55 = 5 puntos menos de lo estimado."], "Obtuvo 5 puntos menos que lo estimado"),
    ],
    mistakes=[("Concluir que estudiar más horas «causa» exactamente 10 puntos más para cualquiera.", "La recta describe una tendencia del grupo, no una garantía individual ni una prueba de causa.", "Usa palabras como «tiende a» y «se estima»."),
              ("Estimar con la recta para valores muy fuera de los datos.", "No sabemos si la tendencia sigue igual fuera del rango observado.", "Usa estimaciones dentro del rango o avisa que es una extrapolación.")],
    T=[
        ('abc', '{F} ¿Qué tipo de relación muestran los datos?', 'Positiva: al aumentar las horas, el puntaje tiende a aumentar', 'Negativa: al aumentar las horas, el puntaje baja', 'Ninguna relación', 'Los puntajes suben de 40 a 90 a medida que aumentan las horas.'),
        ('=', '{F} Con la recta y = 10x + 30, ¿qué puntaje estima para 2 horas?', '10*2+30', 'Se reemplaza x por 2 en la fórmula.'),
        ('ab', 'En un gráfico de dispersión, ¿qué representa cada punto?', 'Un caso, con el valor de sus dos variables', 'El promedio de todos los casos', 'Cada punto corresponde a un estudiante con su par (x, y).'),
        ('=', '{F} ¿Qué puntaje estima la recta para 6 horas?', '10*6+30', 'Se reemplaza x por 6 en la fórmula.'),
        ('{F} Compara el puntaje real de cada estudiante con lo que estima la recta. ¿Cuántos de los seis obtuvieron menos puntaje que el estimado?', '2', 'La recta coincide con el puntaje real en 1, 2, 4 y 6 horas; con 3 horas estima 60 (real 55) y con 5 horas estima 80 (real 75).'),
        ('abc', '{F} En la recta y = 10x + 30, ¿qué significa el 10?', 'Por cada hora más de estudio, el puntaje estimado sube 10 puntos', 'El puntaje que se estima con 0 horas', 'El número de estudiantes', 'El 10 multiplica a x: cada unidad más de x suma 10 a la estimación.'),
        ('=', 'Para otro curso, la recta de ajuste de ejemplo es y = 8x + 20. ¿Qué estima para x = 7?', '8*7+20', 'Se reemplaza x por 7 en la fórmula.'),
        ('=', 'Una recta sube 10 puntos por cada hora más y pasa por el punto (2, 50). ¿Cuánto vale y en x = 5?', '50+10*3', 'Al pasar de 2 a 5 horas hay 3 horas más y cada una suma 10 puntos.'),
        ('abc', 'Una persona dice: «la recta predice 150 puntos para x = 12 horas». ¿Qué evaluación es correcta?', 'La cuenta es correcta (10 · 12 + 30 = 150), pero el puntaje máximo es 100: esa extrapolación no es válida', 'Es válida: se puede obtener 150', 'La cuenta es incorrecta', 'La fórmula da 150, pero un puntaje no puede superar 100; los datos solo llegan hasta 6 horas.'),
        ('abc', 'Un estudio de ejemplo encuentra que, en varios incendios, mientras más bomberos llegan, mayores son los daños. ¿Cuál es la conclusión más razonable?', 'Hay una asociación, pero un tercer factor, el tamaño del incendio, puede explicar ambas', 'Los bomberos causan los daños', 'Enviar menos bomberos reduciría los daños', 'Los incendios grandes reciben más bomberos y también causan más daños; la asociación no prueba que una variable cause la otra.'),
        ('abc', '{F} Las mediciones van de 1 a 6 horas. ¿Cuál estimación es más confiable?', 'Para 4 horas, porque está dentro del rango de los datos', 'Para 12 horas', 'Ambas igual', 'Dentro del rango observado la tendencia está respaldada por los datos.'),
        ('abc', '{F} Alguien dice: «la recta muestra que estudiar una hora más causa exactamente 10 puntos más a cualquier estudiante». ¿Qué corrección es adecuada?', 'La recta describe una tendencia promedio del grupo; no garantiza el resultado individual ni prueba causalidad', 'Tiene razón', 'La recta no sirve para nada', 'Una recta de ajuste resume una tendencia; las personas pueden alejarse de ella.'),
        ('abc', '{F} Se agrega un estudiante con (2, 95), muy alejado de la tendencia. ¿Qué es lo más adecuado?', 'Revisarlo: puede ser un error de dato o un caso especial, y puede cambiar la recta', 'Borrarlo sin mirar', 'Ignorar que existe', 'Un dato muy distinto se investiga antes de decidir qué hacer con él.'),
    ],
    ctx=('abc', 'Un club mide los minutos de calentamiento (x) y las lesiones del mes (y) en 12 deportistas (datos de ejemplo), y observa que más calentamiento se asocia con menos lesiones. ¿Cuál es el uso responsable del hallazgo?', 'Sugerir calentar más y seguir evaluando con más datos, sin afirmar una causa definitiva', 'Afirmar que el calentamiento es la única causa', 'Ignorar el hallazgo', 'La asociación es una pista útil; para hablar de causa se necesitan más datos y un diseño cuidadoso.'),
    sc=[
        ("En Estadística: ¿cómo se llama la relación en que, al subir x, tiende a bajar y?", "Negativa", "Una relación negativa va en sentidos contrarios."),
        ("En Estadística: ¿por qué es riesgoso predecir con valores de x fuera del rango medido?", "Porque la tendencia puede no seguir igual fuera de lo observado", "No hay datos que respalden la estimación fuera del rango."),
        ("¿Una asociación entre dos variables prueba que una causa a la otra?", "No", "Puede haber un tercer factor o coincidencia."),
    ],
    op=("Elige una tabla de datos de ejemplo. Tabla 1: distancia de la casa al colegio en km (x) y minutos de viaje (y): (1, 6), (2, 10), (3, 14), (4, 18), (5, 22), con la recta y = 4x + 2. "
        "Tabla 2: temperatura en °C (x) y vasos de chocolate caliente vendidos (y): (10, 40), (15, 30), (20, 20), (25, 10), con la recta y = −2x + 60. "
        "Describe el tipo de relación, estima un valor dentro del rango, explica por qué estimar uno fuera del rango es riesgoso y escribe una frase sobre causalidad.",
        "Tabla 1: relación positiva. Para 4 km: 4 · 4 + 2 = 18 minutos. Para 40 km la recta daría 162 minutos, pero no hay datos de viajes tan largos. Frase: la distancia se asocia con el tiempo, pero también influyen el tráfico y el medio de transporte.",
        ["describe la relación con el signo correcto", "estima un valor dentro del rango", "explica el riesgo de extrapolar y la limitación causal"],
        ["hoja con el tipo de relación, la estimación y las dos explicaciones"],
        ["estimar con la fórmula equivocada", "extrapolar sin advertir el riesgo", "afirmar una causa segura"],
        "Pregunta: «¿en qué rango de x tienes datos?». Si estima fuera de él, pídele que lo justifique o que lo evite."),
    reinforce="Con la recta y = 10x + 30, estima el puntaje para 1, 2 y 6 horas y compáralos con los datos de la ficha.",
    extend="Explica con tus palabras por qué una recta de ajuste puede ser útil aunque ningún punto caiga exactamente sobre ella.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 5 (de ejemplo). Mini-aplicación que calcula el total de un pedido: def total(cantidad, precio, envio): ↵ ··subtotal = cantidad * precio ↵ ··if subtotal >= 30000: ↵ ····envio = 0 ↵ ··return subtotal + envio. "
     "Versión con un error: def total2(cantidad, precio, envio): ↵ ··subtotal = cantidad * precio ↵ ··if subtotal > 30000: ↵ ····envio = 0 ↵ ··return subtotal + envio. "
     "La regla del enunciado del cliente: envío gratis desde $30.000 de subtotal.")
build(
    O4, 5, F,
    use="Aprenderé a crear y comprobar una pequeña aplicación que calcula y entrega resultados, validándola con casos calculados a mano, y a reconocer los límites de las herramientas.",
    prior=["Sé escribir y seguir una función con condiciones.", "Sé calcular media y mediana.", "Sé comprobar un resultado por sustitución."],
    explain=[
        "Una aplicación sencilla tiene entradas, un proceso y una salida, y se construye en ciclos: especificar la regla, programarla, probarla con casos cuyo resultado se calculó a mano y corregirla. La regla del enunciado del cliente es «envío gratis desde $30.000», así que total(5, 6000, 2500) debe valer 30.000, porque el subtotal exactamente 30.000 ya tiene envío gratis. Si una versión da 32.500, tiene un error de borde.",
        "Los casos de prueba deben incluir el valor justo en el límite de cada regla, valores por debajo y por encima, y datos no válidos (por ejemplo, cantidad 0 o negativa), para los cuales la aplicación debe avisar un error en vez de entregar un total absurdo. Las herramientas tienen límites: con decimales, Python entrega 0.1 + 0.2 = 0.30000000000000004; por eso el dinero en pesos se guarda en enteros.",
        "Al resumir datos de un grupo con un valor atípico, una aplicación responsable muestra más de una medida (media y mediana, y el rango), porque juntas revelan el efecto del dato extremo. Un procesador simbólico o una hoja de cálculo pueden servir para verificar las fórmulas de la aplicación. Al final se documentan las limitaciones: qué datos acepta, qué redondeos hace y qué no cubre.",
    ],
    vocab=[("aplicación", "programa con entradas, proceso y salida para una tarea"), ("caso de prueba", "entrada con resultado esperado calculado a mano"), ("caso de borde", "valor justo en el límite de una regla"), ("validación", "comprobación de que la entrada es aceptable"), ("limitación", "cosa que la aplicación no resuelve o resuelve con error"), ("versión", "forma particular de un programa, que puede corregirse")],
    worked=[
        ("Probar el límite", "Prueba total(5, 6000, 2500) y total2(5, 6000, 2500).", ["subtotal = 5 · 6000 = 30000. En total, 30000 >= 30000 es verdadero, así que envío 0 y devuelve 30000.", "En total2, 30000 > 30000 es falso, de modo que suma 2500 y devuelve 32500."], "total devuelve 30.000 y total2 devuelve 32.500: total2 no cumple la regla"),
        ("Validar datos", "¿Qué devuelve total(−2, 10000, 2500) y qué problema muestra?", ["subtotal = −2 · 10000 = −20000.", "No llega a 30000, así que devuelve −20000 + 2500 = −17500, un total absurdo."], "Devuelve −17.500: falta validar que cantidad sea mayor que 0"),
    ],
    mistakes=[("Probar solo con valores cómodos, lejos del límite de las reglas.", "Los errores de > contra >= solo aparecen justo en el límite.", "Incluye el valor exacto del límite entre los casos de prueba."),
              ("Aceptar el resultado del programa sin compararlo con un cálculo a mano.", "Sin referencia, un error pasa desapercibido.", "Calcula primero el resultado esperado y después compáralo.")],
    T=[
        ('abc', '{F} ¿Qué devuelve total(2, 10000, 2500)?', '22.500', '20.000', '25.000', 'El subtotal es 20.000, menor que 30.000, así que se suma el envío: 22.500.'),
        ('abc', '{F} ¿Qué devuelve total(3, 12000, 2500)?', '36.000', '38.500', '14.500', 'El subtotal 36.000 supera 30.000, el envío se vuelve 0 y el total es 36.000.'),
        ('ab', '{F} ¿Cuál es la regla del envío gratis en la versión total?', 'Subtotal de 30.000 o más', 'Subtotal mayor que 30.000', 'La condición es subtotal >= 30000, que incluye el valor 30.000.'),
        ('abc', '{F} ¿Qué devuelve total(3, 10000, 1800)?', '30.000', '31.800', '1.800', 'El subtotal es exactamente 30.000, cumple >= y el envío es 0.'),
        ('abc', '{F} ¿Qué devuelve total2(3, 10000, 1800)?', '31.800', '30.000', '0', 'Con > el valor 30.000 no cumple la condición y se suma el envío de 1.800.'),
        ('abc', '{F} ¿Qué prueba muestra la diferencia entre total y total2?', 'Un pedido con subtotal exactamente 30.000, como 3 unidades de 10.000', 'Un pedido con subtotal 20.000', 'Un pedido con subtotal 36.000', 'Solo en el valor límite difieren; en 20.000 y en 36.000 ambas versiones coinciden.'),
        ('=', '{F} Calcula a mano el total correcto para cantidad 3, precio 9000 y envío 2500.', '3*9000+2500', 'El subtotal es 27.000, menor que 30.000, por lo que se suma el envío.'),
        ('=', '{F} Con total, ¿cuánto devuelve total(1, 29990, 2500)?', '29990+2500', 'El subtotal 29.990 no llega a 30.000, así que se suma el envío.'),
        ('abc', 'Se agrega una validación: si cantidad es menor o igual que 0 la función debe avisar un error. ¿Qué entradas deberían probarse para esa validación?', 'cantidad = 0 y cantidad = −2', 'cantidad = 5 solamente', 'cantidad = 100', 'Para probar el rechazo hay que usar valores no válidos: el límite 0 y uno negativo.'),
        ('abc', '{F} Un compañero prueba total y total2 solo con subtotales de 20.000 y 36.000 y dice que son equivalentes. ¿Qué falla?', 'No probó el valor límite, 30.000, donde difieren', 'Nada: son equivalentes', 'Debió probar solo valores pequeños', 'Esas dos pruebas coinciden, pero en el valor límite las versiones dan resultados distintos.'),
        ('abc', 'En Python, 0.1 + 0.2 entrega 0.30000000000000004. Para una app de pagos en pesos chilenos, ¿qué decisión de diseño es razonable?', 'Guardar el dinero en números enteros (pesos) para evitar errores de redondeo', 'Usar siempre decimales', 'Ignorar el problema', 'Con enteros no aparecen los errores de representación de los decimales.'),
        ('abc', 'Una app resume los tiempos de un grupo en el que hay un dato atípico muy grande. ¿Qué diseño es más responsable?', 'Mostrar media y mediana (y el rango), porque juntas revelan el efecto del dato atípico', 'Mostrar solo la media', 'Mostrar solo el máximo', 'La diferencia entre media y mediana avisa de un valor extremo, que una sola medida oculta.'),
        ('abc', 'Para probar el límite del envío gratis con cantidad 6, ¿qué precio da un subtotal exactamente de 30.000?', '5.000', '6.000', '30.000', '6 · 5.000 = 30.000; con 6.000 el subtotal sería 36.000.'),
    ],
    ctx=('abc', 'Una rifa escolar entrega un número por cada $3.000 gastados, con la regla numeros = gasto // 3000. ¿Cuántos números recibe quien gastó $8.999?', '2', '3', '0', '8999 // 3000 = 2; con 9.000 recibiría 3, y esa es la prueba de borde que conviene hacer.'),
    sc=[
        ("En desarrollo de aplicaciones: ¿por qué se prueba el valor justo en el límite de una regla?", "Porque ahí suelen estar los errores entre > y >=", "El límite es donde se confunden las comparaciones estrictas y no estrictas."),
        ("En desarrollo de aplicaciones: ¿con qué se compara la salida de un programa para validarla?", "Con un cálculo hecho a mano (referencia)", "Sin una referencia independiente no se puede saber si el resultado es correcto."),
        ("En desarrollo de aplicaciones: ¿por qué el dinero en pesos se guarda en números enteros?", "Para evitar errores de redondeo de los decimales", "Los decimales binarios no representan exactamente algunos valores."),
    ],
    op=("Elige una aplicación. Aplicación 1: descuento por cantidad, con 10 % de descuento desde 10 unidades. Aplicación 2: nota de aprobación con el promedio de tres notas (escala de 10 a 70, con //) y aprobado desde 40. "
        "Escribe las entradas y la salida, programa la función, diseña cinco casos de prueba con el resultado calculado a mano (uno justo en el límite y uno no válido), escribe una versión con un error de borde y muestra el contraejemplo.",
        "Aplicación 2: promedio = (n1 + n2 + n3) // 3; aprobado si promedio >= 40. Pruebas: (40, 40, 40) aprueba; (39, 40, 40) promedio 39, reprueba; (70, 10, 40) promedio 40, aprueba. Versión con error: usar > 40; el contraejemplo es (40, 40, 40).",
        ["define entradas, salida y una función coherente", "diseña cinco casos con resultados a mano, incluido el límite", "muestra un contraejemplo de la versión con error"],
        ["hoja con la función, la tabla de cinco pruebas y la versión con error"],
        ["no probar el valor límite", "calcular mal el resultado esperado", "no incluir un caso no válido"],
        "Pregunta: «¿qué resultado esperabas para el valor justo del límite?». Si falta, pídele que lo calcule antes de seguir el código."),
    reinforce="Sigue a mano total y total2 con cantidad 4, precio 7500 y envío 2500 y anota si las dos versiones coinciden.",
    extend="Explica qué limitaciones declararías en la ficha de tu aplicación (datos que acepta, redondeos y casos que no cubre).",
)
