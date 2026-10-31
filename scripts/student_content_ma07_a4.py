"""Cuaderno del estudiante de 7.º básico Matemática: OA 06 (lenguaje algebraico) y OA 07 (reducción de términos semejantes)."""
from __future__ import annotations

from student_lessons import ex
from student_content_ma07_a import M, W, lesson, task

OA6 = "MA07 OA 06"
OA7 = "MA07 OA 07"

# ------------------------------------------------------------------ OA 06 clase 1
lesson(
    OA6, 1,
    use="Aprenderé a escribir con letras y números relaciones que se dicen con palabras, como «el doble de un número más 7». Sirve para describir reglas, precios y medidas que cambian.",
    prior=["Sé operar con números naturales y enteros.", "Sé qué significan «doble», «triple», «mitad», «más que» y «menos que»."],
    explain=[
        "Una variable es una letra que representa un número que puede cambiar, como n, x o m. Una expresión algebraica combina números, letras y operaciones. En el álgebra se omite el signo de multiplicar entre un número y una letra: 2 · n se escribe 2n. Así, «el doble de n» es 2n, «el triple de x» es 3x y «la mitad de m» es m/2.",
        "Para traducir una frase, busca las palabras clave. «Más», «aumentado en» y «suma» llevan +. «Menos», «disminuido en» y «diferencia» llevan −. Cuidado con el orden: «5 menos que x» se escribe x − 5, no 5 − x, porque se le quitan 5 a x. Y no es lo mismo «el doble de n, más 3», que se escribe 2n + 3, que «el doble de (n más 3)», que se escribe 2(n + 3).",
        "Una expresión sirve para muchos casos. Si una entrada cuesta $3.500, el costo de n entradas es 3.500n. Para saber el costo de 4 entradas se reemplaza n por 4: 3.500 · 4 = 14.000. Reemplazar la letra por un número se llama evaluar o sustituir. Siempre indica qué significa la letra antes de usarla.",
    ],
    vocab=[("variable", "letra que representa un número que puede cambiar"), ("expresión algebraica", "combinación de números, letras y operaciones, como 2n + 7"), ("evaluar", "reemplazar la letra por un número y calcular"), ("lenguaje algebraico", "forma de escribir relaciones con letras y números"), ("sustituir", "poner un número en el lugar de una letra")],
    worked=[
        W("Traducir una frase", "Escribe en lenguaje algebraico: «el doble de un número, aumentado en 7».", ["Llamo n al número. El doble de n es 2n.", "Aumentado en 7 significa sumar 7: 2n + 7."], "2n + 7"),
        W("Costo de varias entradas", "Una entrada de ejemplo cuesta $3.500. Escribe el costo de n entradas y calcula el de 4 entradas.", ["El costo es 3.500 por cada entrada: 3.500n.", "Sustituyo n = 4: 3.500 · 4 = 14.000."], "3.500n; $14.000"),
    ],
    mistakes=[
        M("Escribir «5 menos que x» como 5 − x.", "Se mantuvo el orden en que aparecen las palabras.", "«5 menos que x» es x − 5. Con x = 8: 5 menos que 8 es 3 = 8 − 5."),
        M("Escribir «el doble de n más 3» como 2(n + 3).", "Se agrupó todo dentro del doble.", "El doble se aplica solo a n: 2n + 3."),
    ],
    rec=[
        ex("Escribe en lenguaje algebraico: «un número x aumentado en 6».", "x + 6", "Aumentado en 6 significa sumar 6."),
        ex("Escribe en lenguaje algebraico: «el triple de x».", "3x", "El triple es 3 veces x."),
        ex("Si n = 4, ¿cuánto vale n + 9?", "13", "Se sustituye n por 4: 4 + 9."),
    ],
    und=[
        ex("Escribe en lenguaje algebraico: «5 menos que un número x».", "x − 5", "Se le quitan 5 a x."),
        ex("Escribe en lenguaje algebraico: «la mitad de un número m».", "m/2", "La mitad es dividir entre 2."),
        ex("Si x = 6, ¿cuánto vale 4x − 3?", "21", "4 · 6 = 24 y 24 − 3 = 21."),
    ],
    app=[
        ex("Una bolsa de ejemplo pesa b kg y una caja pesa el doble de la bolsa más 3 kg. Escribe una expresión para el peso de la caja.", "2b + 3", "El doble de b es 2b y se suman 3 kg."),
        ex("Un pan cuesta $900. Escribe el costo de p panes y calcula el de 7 panes.", "900p; $6.300", "900 · 7 = 6.300."),
        ex("Ana tiene a años y Pedro tiene 4 años más que ella. Si Ana tiene 12 años, ¿cuántos años tiene Pedro?", "16", "Pedro tiene a + 4 = 12 + 4."),
    ],
    rea=[
        ex("Luis tradujo «5 menos que x» como 5 − x. Con x = 8, ¿qué valor da su expresión y cuál debería dar?", "Da −3 y debería dar 3", "5 − 8 = −3, pero 5 menos que 8 es 3, o sea x − 5."),
        ex("¿Son iguales 2n + 3 y 2(n + 3) cuando n = 1? Responde con los dos valores.", "No; dan 5 y 8", "2 · 1 + 3 = 5 y 2 · (1 + 3) = 8."),
    ],
    cha=[
        ex("Un rectángulo tiene ancho a y largo 3 cm más que el ancho. Escribe una expresión para su perímetro y calcúlalo cuando a = 5.", "2a + 2(a + 3); 26 cm", "El largo es a + 3 = 8; perímetro 2 · 5 + 2 · 8 = 26."),
        ex("Un número x cumple que el doble de x más 1 es 11. ¿Cuánto vale x?", "5", "2x + 1 = 11 se cumple con x = 5 porque 2 · 5 + 1 = 11."),
    ],
    ctx=[ex("Un viaje en taxi de ejemplo cuesta $1.000 fijos más $300 por kilómetro. Escribe el costo para k km y calcula el costo de un viaje de 6 km.", "1.000 + 300k; $2.800", "Para 6 km: 1.000 + 300 · 6 = 2.800.")],
    sc=[
        ex("Escribe en lenguaje algebraico: «un número n disminuido en 8».", "n − 8", "Disminuido en 8 significa restar 8."),
        ex("Si m = 10, ¿cuánto vale m/2 + 1?", "6", "10/2 = 5 y 5 + 1 = 6."),
        ex("Escribe «el doble de y» en lenguaje algebraico.", "2y", "El doble es 2 veces y."),
    ],
    op=task(
        "Traduce a lenguaje algebraico estas cinco frases, indicando qué significa la letra: (1) el triple de un número, aumentado en 2; (2) 7 menos que un número; (3) la mitad de un número, más 4; (4) el costo de c cuadernos de $1.200 cada uno; (5) la edad de Rosa dentro de 5 años si hoy tiene r años. Después evalúa cada una cuando la letra vale 6.",
        "(1) 3n + 2 = 20. (2) n − 7 = −1. (3) n/2 + 4 = 7. (4) 1.200c = 7.200. (5) r + 5 = 11.",
        ["traduce bien las cinco frases", "cuida el orden de «menos que»", "evalúa correctamente"],
        ["cinco expresiones", "cinco valores"],
        ["invertir el orden en «menos que»", "no omitir el signo de multiplicar entre número y letra"],
        "Pide que explique en voz alta qué representa la letra en cada caso y que compruebe con un número fácil.",
    ),
    reinforce="Escribe en lenguaje algebraico: el doble de n, n más 10, 3 menos que n y la mitad de n.",
    extend="Escribe dos frases distintas con palabras que correspondan a la expresión 3x − 4.",
)

# ------------------------------------------------------------------ OA 06 clase 2
lesson(
    OA6, 2,
    use="Aprenderé a descubrir la regla de un patrón de números o de figuras y a escribirla con una letra. Sirve para predecir cuántos elementos habrá en una figura lejana sin dibujarla.",
    prior=["Sé continuar secuencias de números.", "Sé escribir expresiones con letras."],
    explain=[
        "Un patrón es una secuencia que sigue una regla. En 5, 8, 11, 14… cada número sube 3. La posición se llama n (n = 1, 2, 3…) y el valor es el término. Cuando la diferencia es constante, la regla tiene la forma dn + c, donde d es la diferencia. Aquí d = 3 y la regla es 3n + 2, porque para n = 1 se obtiene 3 + 2 = 5.",
        "Para encontrar la regla: calcula la diferencia entre términos seguidos (d), multiplica d por la posición y ajusta con un número para llegar al primer término. Comprueba con otro término: con n = 4, 3 · 4 + 2 = 14. Si la regla funciona en todos, es correcta. Con una regla puedes predecir el término de cualquier posición, como el 20, sin escribirlos todos.",
        "Los patrones también aparecen en figuras. Si la figura 1 tiene 4 palitos, la figura 2 tiene 7 y la figura 3 tiene 10, cada figura agrega 3 palitos: la regla es 3n + 1. Un patrón puede decir cuántas piezas necesitas para la figura 50. Para decidir si un número es término del patrón, plantea la regla igual a ese número y mira si la posición sale un natural.",
    ],
    vocab=[("patrón", "secuencia que sigue una regla"), ("término", "cada número de una secuencia"), ("posición", "lugar que ocupa un término: 1.º, 2.º, 3.º…"), ("regla", "expresión que da el término de cualquier posición n"), ("diferencia constante", "aumento igual entre dos términos seguidos")],
    worked=[
        W("Regla de una secuencia", "Encuentra la regla de 5, 8, 11, 14…", ["La diferencia es 3, así que la regla empieza con 3n.", "Para n = 1 necesito 5, y 3 · 1 = 3, falta 2: la regla es 3n + 2. Compruebo con n = 4: 14."], "3n + 2"),
        W("Patrón con figuras", "Una figura de ejemplo tiene 4 palitos si n = 1, 7 si n = 2 y 10 si n = 3. ¿Cuántos palitos tiene con n = 20?", ["Cada figura agrega 3 palitos: regla 3n + 1.", "Con n = 20: 3 · 20 + 1 = 61."], "61 palitos"),
    ],
    mistakes=[
        M("Decir que la regla de 5, 9, 13, 17 es 5n.", "Se miró solo el primer término.", "La diferencia es 4, la regla es 4n + 1. Con n = 2, 4 · 2 + 1 = 9."),
        M("Decir que 50 es un término de 4n + 1 porque «está cerca de 49».", "No se comprobó con la regla.", "4n + 1 = 50 daría n = 49/4, que no es natural. No es término."),
    ],
    rec=[
        ex("Continúa la secuencia 2, 4, 6, 8 con el siguiente número.", "10", "Cada término sube 2."),
        ex("En la secuencia 7, 12, 17, 22, ¿cuánto aumenta cada término?", "5", "12 − 7 = 5."),
        ex("Si la regla es 2n, ¿cuál es el cuarto término?", "8", "2 · 4."),
    ],
    und=[
        ex("Con la regla 4n + 1, ¿cuál es el tercer término?", "13", "4 · 3 + 1."),
        ex("Encuentra la regla de la secuencia 3, 7, 11, 15…", "4n − 1", "La diferencia es 4 y con n = 1: 4 − 1 = 3."),
        ex("Con la regla 3n + 1, ¿en qué posición está el término 25?", "8", "3n + 1 = 25 da 3n = 24 y n = 8."),
    ],
    app=[
        ex("Una figura de ejemplo con azulejos tiene 6 azulejos si n = 1, 10 si n = 2 y 14 si n = 3. ¿Cuántos azulejos tiene con n = 10?", "42", "La regla es 4n + 2; con n = 10: 4 · 10 + 2."),
        ex("En un patrón de mesas cuadradas juntas, 1 mesa sienta 4 personas, 2 mesas sientan 6 y 3 mesas sientan 8. ¿Cuántas personas se sientan con 12 mesas?", "26", "La regla es 2n + 2; con n = 12: 24 + 2."),
        ex("Una cuenta de ahorro de ejemplo parte con $2.000 y cada semana suma $500. Su regla es 2.000 + 500n. ¿Cuánto hay después de 6 semanas?", "$5.000", "2.000 + 500 · 6 = 2.000 + 3.000."),
    ],
    rea=[
        ex("Pía dice que la regla de 3, 5, 7, 9 es 3n. ¿Está bien? Si no, escribe la regla correcta.", "No; es 2n + 1", "Con 3n el segundo término sería 6 y no 5; la diferencia es 2 y 2 · 1 + 1 = 3."),
        ex("¿La secuencia de regla 3n + 2 tiene el término 40? Responde sí o no.", "No", "Sus términos son 5, 8, 11… 38, 41…; 3n + 2 = 40 daría n = 38/3, que no es natural."),
    ],
    cha=[
        ex("Las reglas 3n + 1 y 2n + 4 dan el mismo valor en una posición. ¿En cuál?", "n = 3", "En n = 3, ambas dan 10."),
        ex("En la secuencia 1, 4, 7, 10… ¿cuál es el primer término mayor que 100?", "103", "La regla es 3n − 2; con n = 34 da 100 y con n = 35 da 103."),
    ],
    ctx=[ex("Una feria de ejemplo arma puestos en fila: con 1 puesto se usan 6 palos, con 2 puestos 9 palos y con 3 puestos 12 palos. ¿Cuántos palos se necesitan para 8 puestos?", "27", "La regla es 3n + 3; con n = 8: 24 + 3.")],
    sc=[
        ex("Con la regla 5n − 2, ¿cuál es el segundo término?", "8", "5 · 2 − 2."),
        ex("Continúa la secuencia 20, 17, 14, 11 con el siguiente número.", "8", "Cada término baja 3."),
        ex("Con la regla 2n + 5, ¿cuál es el término de la posición 10?", "25", "2 · 10 + 5."),
    ],
    op=task(
        "Observa esta secuencia de ejemplo: figura 1 tiene 5 cuadritos, figura 2 tiene 9, figura 3 tiene 13 y figura 4 tiene 17. (a) Dibuja las figuras 1 y 2 en una cuadrícula con una forma que explique el crecimiento. (b) Escribe la regla. (c) Calcula cuántos cuadritos tiene la figura 15. (d) Decide si la figura con 101 cuadritos existe y explica cómo lo supiste.",
        "Regla: 4n + 1 (cada figura agrega 4). Figura 15: 61 cuadritos. 4n + 1 = 101 da n = 25, así que existe la figura 25.",
        ["dibuja un crecimiento coherente", "encuentra la regla", "usa la regla para predecir y para decidir"],
        ["dibujo en cuadrícula", "regla escrita", "cálculos y explicación"],
        ["usar solo el primer término para la regla", "no comprobar con otro término"],
        "Pide que compruebe la regla con las cuatro figuras dadas.",
    ),
    reinforce="Escribe la regla de la secuencia 4, 6, 8, 10 y calcula el término número 12.",
    extend="Inventa una secuencia con regla 5n + 3, escribe sus cuatro primeros términos y dibuja una figura que la represente.",
)

# ------------------------------------------------------------------ OA 06 clase 3
lesson(
    OA6, 3,
    use="Aprenderé a escribir con letras propiedades que valen para todos los números, como «sumar en cualquier orden da lo mismo». Sirve para explicar por qué un cálculo siempre funciona.",
    prior=["Sé usar letras para representar números.", "Conozco el orden de las operaciones."],
    explain=[
        "Con letras se pueden escribir propiedades que valen para cualquier número. La propiedad conmutativa de la suma dice que el orden no cambia el resultado: a + b = b + a. En la multiplicación, a · b = b · a. La propiedad asociativa dice que da lo mismo agrupar de distinta forma: (a + b) + c = a + (b + c). El cero y el uno son neutros: a + 0 = a y a · 1 = a.",
        "La propiedad distributiva une la suma y la multiplicación: a(b + c) = ab + ac. Por ejemplo, 4(5 + 2) = 4 · 5 + 4 · 2 = 28. Con letras también se describen familias de números: un número par es 2n (si n es entero), un número impar es 2n + 1 y el sucesor de n es n + 1. Dos números consecutivos son n y n + 1.",
        "Un ejemplo con números no demuestra que una propiedad siempre se cumple, pero un solo contraejemplo muestra que no es verdadera. Por ejemplo, a − b = b − a es falsa: con a = 5 y b = 2, da 3 y −3. Para probar que algo se cumple siempre se usa la letra. Cuando una propiedad se cumple, la letra se puede reemplazar por cualquier número.",
    ],
    vocab=[("propiedad conmutativa", "cambiar el orden no cambia el resultado: a + b = b + a"), ("propiedad distributiva", "a(b + c) = ab + ac"), ("neutro", "número que no cambia el resultado: 0 en la suma, 1 en la multiplicación"), ("contraejemplo", "ejemplo que muestra que una afirmación es falsa"), ("consecutivos", "números que se siguen: n y n + 1")],
    worked=[
        W("Escribir una propiedad", "Escribe con letras: «al sumar dos números, el resultado no cambia si se intercambian». Compruébalo con 3 y 8.", ["Con letras: a + b = b + a.", "Con 3 y 8: 3 + 8 = 11 y 8 + 3 = 11."], "a + b = b + a"),
        W("Propiedad distributiva", "Comprueba a(b + c) = ab + ac con a = 4, b = 5, c = 2.", ["Izquierda: 4 · (5 + 2) = 4 · 7 = 28.", "Derecha: 4 · 5 + 4 · 2 = 20 + 8 = 28."], "Las dos dan 28"),
    ],
    mistakes=[
        M("Decir que a − b = b − a siempre se cumple porque funciona con a = 4 y b = 4.", "Un caso particular no prueba una propiedad general.", "Con a = 5 y b = 2 da 3 y −3: un contraejemplo muestra que es falsa."),
        M("Escribir un número impar como 2n.", "Se confundió con el par.", "2n es par; el impar es 2n + 1."),
    ],
    rec=[
        ex("¿Qué propiedad expresa a + b = b + a?", "Conmutativa", "El orden de los sumandos no cambia el resultado."),
        ex("Escribe con una letra un número par (n es un entero).", "2n", "Un par se puede repartir en dos grupos iguales de n."),
        ex("Si a = 9, ¿cuánto vale a · 1?", "9", "El 1 es neutro de la multiplicación."),
    ],
    und=[
        ex("Verifica la propiedad distributiva con a = 3, b = 4 y c = 5. ¿Cuánto vale a(b + c)?", "27", "3 · (4 + 5) = 3 · 9 = 27, igual que 12 + 15."),
        ex("Escribe con una letra el sucesor de n.", "n + 1", "El sucesor es el número siguiente."),
        ex("Si n = 4, ¿qué número impar da la expresión 2n + 1?", "9", "2 · 4 + 1."),
    ],
    app=[
        ex("Clara compra 6 paquetes de 8 galletas y 6 paquetes de 5 galletas. Escribe el total como 6(8 + 5) y calcula cuántas galletas son.", "78", "6 · 13 = 78, igual que 48 + 30."),
        ex("Si n = 7, calcula la suma de los tres números consecutivos n, n + 1 y n + 2.", "24", "7 + 8 + 9."),
        ex("Si n = 10, ¿cuánto vale la expresión 2n + 1?", "21", "2 · 10 + 1."),
    ],
    rea=[
        ex("Tomás dice que a − b = b − a siempre. Prueba con a = 5 y b = 2: ¿qué resultados obtienes?", "3 y −3", "5 − 2 = 3 y 2 − 5 = −3, por eso la propiedad es falsa."),
        ex("¿Verdadero o falso? «Para cualquier número a, a · 0 = 0».", "Verdadero", "Multiplicar cualquier número por cero da cero."),
    ],
    cha=[
        ex("Marta dice que la suma de dos números consecutivos es siempre impar. Con n = 14, ¿cuánto vale n + (n + 1) y es impar?", "29; sí es impar", "14 + 15 = 29, y en general n + (n + 1) = 2n + 1."),
        ex("Comprueba que 2n + 2m = 2(n + m) con n = 3 y m = 5. ¿Cuánto da cada lado?", "16 en ambos", "2 · 3 + 2 · 5 = 16 y 2 · (3 + 5) = 16."),
    ],
    ctx=[ex("Un pastelero de ejemplo arma 4 bandejas con 6 pasteles y 4 bandejas con 3 pasteles. Calcula el total con 4(6 + 3).", "36", "4 · 9 = 36, igual que 24 + 12.")],
    sc=[
        ex("¿Cómo se escribe con letras que el cero es neutro en la suma?", "a + 0 = a", "Sumar cero no cambia el número."),
        ex("Si a = 2, b = 6 y c = 1, ¿cuánto vale a(b + c)?", "14", "2 · 7."),
        ex("¿Es 2n + 1 par o impar?", "Impar", "Es el siguiente de un par."),
    ],
    op=task(
        "Prueba estas tres afirmaciones con los valores a = 6, b = 4, c = 2: (1) a + b = b + a; (2) a − b = b − a; (3) a(b + c) = ab + ac. Para cada una escribe los dos lados con números y di si se cumple. Para la que no se cumple, explica por qué ese ejemplo es un contraejemplo.",
        "(1) 10 y 10: se cumple. (2) 2 y −2: no se cumple, es un contraejemplo. (3) 6 · 6 = 36 y 24 + 12 = 36: se cumple.",
        ["calcula correctamente los dos lados", "identifica la que no se cumple", "explica qué es un contraejemplo"],
        ["tres cálculos con dos lados", "frase de explicación"],
        ["creer que un solo caso basta para probar", "calcular mal el orden de operaciones"],
        "Pide que pruebe con otros valores para confirmar las que sí se cumplieron.",
    ),
    reinforce="Escribe con letras: la propiedad conmutativa de la multiplicación y la del neutro de la multiplicación.",
    extend="Escribe con letras el producto de dos números consecutivos y calcúlalo para n = 6. ¿Es par o impar?",
)

# ------------------------------------------------------------------ OA 06 clase 4
lesson(
    OA6, 4,
    use="Aprenderé a construir ecuaciones a partir de situaciones y a comprobar si un número es solución. Sirve para encontrar valores desconocidos en problemas de dinero, edades y medidas.",
    prior=["Sé escribir expresiones con letras.", "Sé evaluar una expresión."],
    explain=[
        "Una ecuación es una igualdad que tiene una incógnita, es decir, un valor desconocido que se representa con una letra. Por ejemplo, x + 7 = 15 dice: «un número más 7 es 15». La solución es el valor de la letra que hace verdadera la igualdad. Aquí x = 8, porque 8 + 7 = 15.",
        "Para construir una ecuación, define qué representa la letra, escribe una expresión para cada lado y une con un signo igual. Si 3 cuadernos iguales y un lápiz de $400 cuestan $3.100, y c es el precio de un cuaderno, la ecuación es 3c + 400 = 3.100. Para resolverla se deshace cada operación: 3.100 − 400 = 2.700 y 2.700 ÷ 3 = 900.",
        "Para validar, sustituye el valor encontrado en la ecuación original. Si los dos lados dan el mismo número, es solución. Con c = 900: 3 · 900 + 400 = 3.100. También sirve para revisar si un valor dado es o no es solución. Si los lados dan números distintos, ese valor no es solución.",
    ],
    vocab=[("ecuación", "igualdad que tiene un valor desconocido representado con una letra"), ("incógnita", "valor desconocido que se busca"), ("solución", "valor que hace verdadera la ecuación"), ("validar", "comprobar una solución sustituyéndola"), ("igualdad", "dos expresiones con el mismo valor unidas por =")],
    worked=[
        W("Plantear y validar", "Un número aumentado en 7 da 15. Escribe la ecuación, encuentra el número y valida.", ["Ecuación: x + 7 = 15. Para deshacer el + 7 resto 7: x = 15 − 7 = 8.", "Valido: 8 + 7 = 15, se cumple."], "x = 8"),
        W("Ecuación con dos operaciones", "Tres cuadernos iguales y un lápiz de $400 cuestan $3.100. ¿Cuánto cuesta un cuaderno?", ["Ecuación: 3c + 400 = 3.100. Resto 400: 3c = 2.700.", "Divido entre 3: c = 900. Valido: 3 · 900 + 400 = 3.100."], "$900"),
    ],
    mistakes=[
        M("Plantear «el doble de un número menos 5 es 11» como 2(x − 5) = 11.", "Se aplicó el doble al resultado de restar.", "El doble de x es 2x, y luego se resta 5: 2x − 5 = 11, con x = 8."),
        M("Dar x = 5 como solución de 3x − 2 = 10 sin comprobar.", "No se sustituyó el valor.", "3 · 5 − 2 = 13, que no es 10: x = 5 no es solución. La solución es x = 4."),
    ],
    rec=[
        ex("¿Es x = 4 solución de x + 9 = 13? Responde sí o no.", "Sí", "4 + 9 = 13."),
        ex("Escribe la ecuación: «un número más 5 es igual a 12».", "x + 5 = 12", "Se usa x para el número."),
        ex("¿Qué valor de x hace verdadera x − 3 = 7?", "10", "10 − 3 = 7."),
    ],
    und=[
        ex("¿Es x = 5 solución de 3x + 2 = 14? Responde sí o no.", "No", "3 · 5 + 2 = 17, no es 14."),
        ex("Resuelve 2x = 18.", "x = 9", "2 · 9 = 18."),
        ex("Escribe la ecuación: «el triple de un número, disminuido en 4, es 20».", "3x − 4 = 20", "El triple es 3x y se resta 4."),
    ],
    app=[
        ex("Dos helados iguales y un jugo de $700 cuestan $3.500 en total. Plantea la ecuación con h como precio de un helado y resuélvela.", "2h + 700 = 3.500; h = 1.400", "3.500 − 700 = 2.800 y 2.800 ÷ 2 = 1.400."),
        ex("Una caja tiene n lápices y hay 5 lápices sueltos aparte. En total hay 29 lápices. ¿Cuántos lápices hay en la caja?", "24", "n + 5 = 29 da n = 24."),
        ex("Diego tiene $4.000 ahorrados y suma $1.500 cada semana. ¿En cuántas semanas tendrá $13.000?", "6 semanas", "4.000 + 1.500s = 13.000 da 1.500s = 9.000 y s = 6."),
    ],
    rea=[
        ex("Eva dice que x = 9 es solución de 2x + 3 = 15. ¿Es cierto?", "No", "2 · 9 + 3 = 21, no 15."),
        ex("Ana plantea «el doble de un número, menos 5, es 11» como 2(x − 5) = 11. ¿Está bien planteada? Si no, escribe la ecuación correcta.", "No; es 2x − 5 = 11", "El doble se aplica a x y luego se resta 5."),
    ],
    cha=[
        ex("La suma de dos números consecutivos es 31. Si el menor es n, plantea la ecuación y encuentra los números.", "n + (n + 1) = 31; 15 y 16", "15 + 16 = 31."),
        ex("Un triángulo isósceles de ejemplo tiene dos lados iguales de x cm y la base mide x + 2 cm. Su perímetro es 26 cm. ¿Cuánto mide cada lado igual?", "8 cm", "x + x + (x + 2) = 26 da 3x = 24 y x = 8."),
    ],
    ctx=[ex("Un viaje en taxi de ejemplo cuesta $1.000 fijos más $300 por kilómetro. Si un viaje costó $3.400, ¿cuántos kilómetros fueron?", "8 km", "1.000 + 300k = 3.400 da 300k = 2.400 y k = 8.")],
    sc=[
        ex("¿Es x = 2 solución de 5x − 1 = 9?", "Sí", "5 · 2 − 1 = 9."),
        ex("Resuelve x + 12 = 20.", "x = 8", "20 − 12 = 8."),
        ex("Escribe la ecuación: «la mitad de un número es 6».", "x/2 = 6", "La mitad es x dividido entre 2."),
    ],
    op=task(
        "Lee esta situación de ejemplo: «En una feria, Sofía compró 4 entradas iguales y pagó además $1.200 por estacionamiento. En total pagó $9.200». (a) Define la letra y escribe la ecuación. (b) Resuélvela. (c) Valida la solución sustituyendo. (d) Escribe una respuesta en una oración.",
        "(a) Sea e el precio de una entrada: 4e + 1.200 = 9.200. (b) 4e = 8.000, e = 2.000. (c) 4 · 2.000 + 1.200 = 9.200. (d) Cada entrada costó $2.000.",
        ["define la incógnita", "escribe la ecuación correcta", "resuelve y valida", "responde con unidad"],
        ["ecuación escrita", "solución con validación", "respuesta en una oración"],
        ["no definir la letra", "no validar sustituyendo"],
        "Pide que lea la ecuación en voz alta con palabras y que compruebe que dice lo mismo que el problema.",
    ),
    reinforce="Escribe la ecuación y resuelve: «un número más 11 es igual a 30».",
    extend="Inventa un problema que se resuelva con la ecuación 5x − 3 = 22 y resuélvelo.",
)

# ------------------------------------------------------------------ OA 07 clase 1
lesson(
    OA7, 1,
    use="Aprenderé a reconocer los términos de una expresión, su coeficiente y su parte literal, y a ver cuáles son semejantes. Sirve para ordenar expresiones antes de simplificarlas.",
    prior=["Sé escribir expresiones con letras.", "Sé qué es un coeficiente y una variable."],
    explain=[
        "Una expresión algebraica se forma con términos separados por + o −. Un término es un número, una letra o un producto de ambos, como 5x, −3y, x o 7. El número que multiplica a la letra es el coeficiente: en 5x es 5, en −3y es −3, en x es 1 y en −x es −1. La letra se llama parte literal. Un término sin letra, como 7, es un término constante.",
        "Dos términos son semejantes cuando tienen la misma parte literal. Por ejemplo, 4x y −9x son semejantes porque ambos tienen x; solo cambian sus coeficientes. En cambio, 4x y 4y no son semejantes, porque sus letras son distintas. Todos los términos constantes son semejantes entre sí: 8 y −5 lo son.",
        "Para reconocerlos, mira solo la letra. No importa el coeficiente ni el signo. En 5x − 3y + 2x + 7 hay tres grupos: los términos con x (5x y 2x), los términos con y (−3y) y los constantes (7). Agrupar así es el primer paso para reducir una expresión.",
    ],
    vocab=[("término", "parte de una expresión separada por + o −"), ("coeficiente", "número que multiplica a la parte literal"), ("parte literal", "letra o letras de un término"), ("términos semejantes", "términos con la misma parte literal"), ("término constante", "término sin letra, solo un número")],
    worked=[
        W("Reconocer semejantes", "¿Son semejantes 6x y −2x?", ["Las partes literales son x y x: iguales.", "Solo cambian los coeficientes, 6 y −2."], "Sí, son semejantes"),
        W("Agrupar términos", "Agrupa los términos semejantes de 5x − 3y + 2x + 7.", ["Los de x: 5x y 2x. Los de y: −3y. Los constantes: 7.", "Tres grupos."], "(5x, 2x), (−3y), (7)"),
    ],
    mistakes=[
        M("Decir que 5x y 5 son semejantes porque ambos tienen un 5.", "Se miró el coeficiente en vez de la parte literal.", "5x tiene x y 5 no tiene letra: no son semejantes."),
        M("Decir que el coeficiente de x es 0.", "Se creyó que sin número no hay coeficiente.", "x es lo mismo que 1x, su coeficiente es 1."),
    ],
    rec=[
        ex("¿Cuál es el coeficiente de 7y?", "7", "Es el número que multiplica a la letra."),
        ex("¿Cuál es la parte literal de −4x?", "x", "Es la letra del término."),
        ex("¿Cuál es el coeficiente de x?", "1", "x es lo mismo que 1x."),
    ],
    und=[
        ex("De los términos 3x, −5z, z y 3, ¿cuáles son semejantes a 3z? Responde con los dos que lo son.", "−5z y z", "Tienen la misma parte literal z."),
        ex("¿Cuál es el coeficiente de −x?", "−1", "−x es lo mismo que −1x."),
        ex("¿Son semejantes 2x y 2y? Responde sí o no.", "No", "Las letras son distintas."),
    ],
    app=[
        ex("En la expresión 4x + 3y − x + 8 − 2y + 5, ¿cuántos términos son semejantes a 4x, contando el 4x?", "2", "Son 4x y −x."),
        ex("En la misma expresión 4x + 3y − x + 8 − 2y + 5, ¿cuántos términos constantes hay?", "2", "Son 8 y 5."),
        ex("En la misma expresión 4x + 3y − x + 8 − 2y + 5, ¿cuál es la suma de los coeficientes de los términos con y?", "1", "3 + (−2) = 1."),
    ],
    rea=[
        ex("Luis dice que 5x y 5 son semejantes porque tienen un 5. ¿Tiene razón?", "No", "La parte literal de 5x es x y la de 5 no tiene letra."),
        ex("¿Son semejantes x y −x? Responde sí o no.", "Sí", "Ambos tienen parte literal x; los coeficientes son 1 y −1."),
    ],
    cha=[
        ex("En 2x + 3y − 5x + 4y − y + 6, ¿cuántos grupos distintos de términos semejantes hay (x, y y constantes)?", "3", "Hay términos con x, términos con y y un término constante."),
        ex("En 2x + 3y − 5x + 4y − y + 6, ¿cuál es la suma de los coeficientes de los términos con y?", "6", "3 + 4 + (−1) = 6."),
    ],
    ctx=[ex("En una bodega de ejemplo hay 3x cajas azules, 2y cajas rojas, 5x cajas azules más y 4 cajas sueltas. ¿Qué términos son semejantes a 3x?", "5x", "Solo 5x tiene la parte literal x.")],
    sc=[
        ex("¿Cuál es el coeficiente de −9y?", "−9", "Es el número con su signo."),
        ex("¿Son semejantes 8 y −3? Responde sí o no.", "Sí", "Ambos son términos constantes."),
        ex("¿Son semejantes 4x y 4? Responde sí o no.", "No", "Uno tiene letra y el otro no."),
    ],
    op=task(
        "Esta es una expresión de ejemplo: 6x − 2y + 9 + 3x + 5y − 4. Haz una tabla con tres columnas: términos con x, términos con y y términos constantes. Escribe en cada columna los términos con su signo y subraya el coeficiente de cada uno. Después explica en una frase por qué 6x y 3x son semejantes y 6x y 5y no.",
        "Con x: 6x y 3x (coeficientes 6 y 3). Con y: −2y y 5y (coeficientes −2 y 5). Constantes: 9 y −4. 6x y 3x tienen la misma parte literal; 6x y 5y tienen letras distintas.",
        ["clasifica los seis términos", "identifica los coeficientes con su signo", "explica la semejanza por la parte literal"],
        ["tabla de tres columnas", "frase de explicación"],
        ["olvidar el signo del coeficiente", "agrupar por el coeficiente en vez de la letra"],
        "Pide que revise que cada término quedó en una sola columna y que no falte ninguno.",
    ),
    reinforce="En 7x − y + 2 − 3x + 4y, escribe el coeficiente de cada término y agrupa los semejantes.",
    extend="Escribe una expresión con seis términos que tenga exactamente tres grupos de términos semejantes, con coeficientes negativos en dos grupos.",
)

# ------------------------------------------------------------------ OA 07 clase 2
lesson(
    OA7, 2,
    use="Aprenderé a representar sumas de expresiones con cajas y unidades sueltas, y a ver que solo se pueden juntar los términos semejantes. Sirve para entender por qué se reduce de esa manera.",
    prior=["Sé reconocer términos semejantes.", "Sé sumar y restar números enteros."],
    explain=[
        "Imagina que x es la cantidad de lápices que hay dentro de una caja. Una caja se representa con x, y un lápiz suelto con 1. La expresión 2x + 3 significa dos cajas y tres lápices sueltos. Si juntas 2x + 3 con x + 4, tienes tres cajas y siete lápices sueltos: 3x + 7. En el dibujo se juntan las cajas con las cajas y los sueltos con los sueltos.",
        "Con piezas, las cajas de x y las de y son de tipos distintos y no se pueden mezclar. Por eso 3x + 2y se queda así. Cuando un término es negativo, se dibuja como una pieza de deuda: x − 5 es una caja y cinco unidades que faltan. Una pieza positiva y una negativa del mismo tipo se anulan, igual que los pares cero con fichas.",
        "Para sumar expresiones, escribe cada una con sus paréntesis y junta los términos semejantes: (3x + 4) + (2x + 1) = 5x + 5. Revisa que cada término de la respuesta venga de piezas del mismo tipo. Puedes comprobar con un valor: si x = 10, 3x + 4 vale 34, 2x + 1 vale 21, y 5x + 5 vale 55 = 34 + 21.",
    ],
    vocab=[("suma algebraica", "suma de expresiones con letras"), ("pieza", "modelo de una caja x o de una unidad suelta"), ("pieza negativa", "modelo de un término con signo menos"), ("agrupar", "juntar piezas del mismo tipo"), ("paréntesis", "signos ( ) que encierran una expresión")],
    worked=[
        W("Sumar con cajas", "Suma (3x + 4) + (2x + 1).", ["Cajas con cajas: 3x + 2x = 5x.", "Sueltos con sueltos: 4 + 1 = 5."], "5x + 5"),
        W("Con una pieza negativa", "Suma (4x + 2) + (x − 5).", ["Cajas: 4x + x = 5x.", "Unidades: 2 + (−5) = −3."], "5x − 3"),
    ],
    mistakes=[
        M("Sumar (2x + 3) + (x + 4) y escribir 3x + 12.", "Se multiplicaron las unidades en vez de sumarlas.", "Las unidades se suman: 3 + 4 = 7. El resultado es 3x + 7."),
        M("Escribir 2x + 3y = 5xy.", "Se mezclaron piezas de tipos distintos.", "2x y 3y no son semejantes, la expresión no se puede reducir más."),
    ],
    rec=[
        ex("Dos cajas con x lápices cada una y 3 lápices sueltos. Escribe la expresión.", "2x + 3", "Dos cajas son 2x y los sueltos son 3."),
        ex("Suma (x + 2) + (x + 5).", "2x + 7", "Cajas: 2x; sueltos: 2 + 5."),
        ex("Si cada caja tiene 10 lápices (x = 10), ¿cuántos lápices representa 2x + 3?", "23", "2 · 10 + 3."),
    ],
    und=[
        ex("Suma (3x + 4) + (5x + 6).", "8x + 10", "3x + 5x = 8x y 4 + 6 = 10."),
        ex("Suma (6x + 2) + (x − 7).", "7x − 5", "6x + x = 7x y 2 − 7 = −5."),
        ex("Suma (2x + 3y) + (x + 4y).", "3x + 7y", "x con x y y con y."),
    ],
    app=[
        ex("Una bolsa tiene x caramelos más 3 sueltos y otra tiene 2x caramelos más 5 sueltos. Escribe el total de caramelos.", "3x + 8", "Cajas: x + 2x; sueltos: 3 + 5."),
        ex("Si x = 4 en el problema anterior, ¿cuántos caramelos hay en total?", "20", "3 · 4 + 8."),
        ex("Una tienda de ejemplo vende x poleras el lunes y 2x + 3 poleras el martes, además de 4x − 1 el miércoles. Escribe el total de poleras de los tres días.", "7x + 2", "x + 2x + 4x = 7x y 3 − 1 = 2."),
    ],
    rea=[
        ex("Lola sumó (4x + 1) + (x + 6) y obtuvo 5x + 6. ¿Cuál es el resultado correcto?", "5x + 7", "Las unidades se suman: 1 + 6 = 7."),
        ex("¿Se pueden juntar 2x y 3y en un solo término? Responde sí o no.", "No", "Son piezas de tipos distintos."),
    ],
    cha=[
        ex("Si (ax + 3) + (2x + b) = 5x + 9, ¿cuánto valen a y b?", "a = 3 y b = 6", "ax + 2x = 5x da a = 3 y 3 + b = 9 da b = 6."),
        ex("Suma (x + 2) + (2x − 1) + (3x + 4).", "6x + 5", "x + 2x + 3x = 6x y 2 − 1 + 4 = 5."),
    ],
    ctx=[ex("Una caja de ejemplo tiene x bolitas y hay 6 bolitas sueltas. Otra caja igual tiene x bolitas y 2 sueltas. Escribe el total.", "2x + 8", "Dos cajas: 2x; sueltas: 6 + 2.")],
    sc=[
        ex("Suma (4x + 1) + (2x + 3).", "6x + 4", "4x + 2x = 6x y 1 + 3 = 4."),
        ex("Suma (5y + 2) + (y − 2).", "6y", "Las unidades se anulan: 2 − 2 = 0."),
        ex("Suma (x + 3y) + (2x + y).", "3x + 4y", "x con x y y con y."),
    ],
    op=task(
        "Representa con cajas x y unidades sueltas la suma (3x + 2) + (x + 5). Dibuja las piezas de cada expresión, junta las del mismo tipo y escribe el resultado. Después haz lo mismo con (2x − 3) + (x + 7) usando piezas negativas para el −3. Finalmente comprueba con x = 10 que el valor total no cambia.",
        "(3x + 2) + (x + 5) = 4x + 7. (2x − 3) + (x + 7) = 3x + 4. Con x = 10: 32 + 15 = 47 y 4 · 10 + 7 = 47; 17 + 17 = 34 y 3 · 10 + 4 = 34.",
        ["dibuja las piezas con sus signos", "agrupa piezas del mismo tipo", "comprueba con un valor numérico"],
        ["dibujo de piezas", "resultado escrito", "comprobación con x = 10"],
        ["sumar cajas con unidades", "olvidar el signo de las unidades negativas"],
        "Pide que cuente piezas de cada tipo antes de escribir el resultado.",
    ),
    reinforce="Suma (5x + 1) + (x + 8) y representa el resultado con cajas y unidades.",
    extend="Explica con piezas por qué (x + 4) + (−x + 1) = 5 y qué pasa con las cajas.",
)

# ------------------------------------------------------------------ OA 07 clase 3
lesson(
    OA7, 3,
    use="Aprenderé a reducir expresiones con coeficientes enteros, positivos y negativos, hasta dejarlas de la forma ax + by + cz. Sirve para simplificar fórmulas y comparar expresiones.",
    prior=["Sé reconocer términos semejantes.", "Sé sumar y restar números enteros."],
    explain=[
        "Reducir una expresión es juntar los términos semejantes en uno solo. Se suman los coeficientes y la parte literal queda igual: 5x + 3x = 8x. Con coeficientes negativos, se aplican las reglas de enteros: 3x − 8x = (3 − 8)x = −5x y −2y − 4y = −6y. Si el resultado de los coeficientes es 0, el término desaparece: 5x − 5x = 0.",
        "Para reducir una expresión larga, agrupa por tipo y reduce cada grupo. Ejemplo: 6x − 2y + 3z − 4x + 5y − z. Con x: 6x − 4x = 2x. Con y: −2y + 5y = 3y. Con z: 3z − z = 2z. El resultado es 2x + 3y + 2z, que tiene la forma ax + by + cz con a, b y c enteros. Los términos con distinta letra no se juntan.",
        "Cuida los signos: cada término lleva el signo que tiene delante. En 5x + 7 − 2x − 10 los términos son 5x, 7, −2x y −10. Con x: 5x − 2x = 3x; constantes: 7 − 10 = −3. Queda 3x − 3. Es útil tachar o marcar cada grupo para no olvidar ningún término.",
    ],
    vocab=[("reducir", "juntar términos semejantes en uno solo"), ("coeficiente entero", "coeficiente que es un número entero, positivo, negativo o cero"), ("expresión reducida", "expresión sin términos semejantes repetidos"), ("término nulo", "término con coeficiente 0, que desaparece"), ("forma ax + by + cz", "suma de tres términos con letras distintas")],
    worked=[
        W("Reducir con negativos", "Reduce 3x − 8x + 2y − 7y.", ["Con x: 3 − 8 = −5, entonces −5x.", "Con y: 2 − 7 = −5, entonces −5y."], "−5x − 5y"),
        W("Reducir con tres letras", "Reduce 6x − 2y + 3z − 4x + 5y − z.", ["Con x: 6x − 4x = 2x. Con y: −2y + 5y = 3y.", "Con z: 3z − z = 2z."], "2x + 3y + 2z"),
    ],
    mistakes=[
        M("Reducir 5x − 2x y escribir 3.", "Se perdió la letra al restar los coeficientes.", "La parte literal se conserva: 5x − 2x = 3x."),
        M("Reducir 4x − 7x y escribir 3x.", "Se restó el menor del mayor sin cuidar el signo.", "4 − 7 = −3, entonces 4x − 7x = −3x."),
    ],
    rec=[
        ex("Reduce 3x + 5x.", "8x", "3 + 5 = 8."),
        ex("Reduce 9y − 4y.", "5y", "9 − 4 = 5."),
        ex("Reduce 7z − 7z.", "0", "Los coeficientes suman 0."),
    ],
    und=[
        ex("Reduce 2x − 9x.", "−7x", "2 − 9 = −7."),
        ex("Reduce 2x + 5y − x + 3y.", "x + 8y", "Con x: 2 − 1 = 1. Con y: 5 + 3 = 8."),
        ex("Reduce −4x − 6x.", "−10x", "−4 − 6 = −10."),
    ],
    app=[
        ex("Reduce 5x + 7 − 2x − 10.", "3x − 3", "Con x: 5 − 2 = 3. Constantes: 7 − 10 = −3."),
        ex("Reduce 4y − 9y + 3 + y.", "−4y + 3", "Con y: 4 − 9 + 1 = −4."),
        ex("Reduce 8x − 3y + 2z − 5x − y − 6z.", "3x − 4y − 4z", "Con x: 3. Con y: −3 − 1 = −4. Con z: 2 − 6 = −4."),
    ],
    rea=[
        ex("Ana quiso reducir 2x + 3y y escribió 5xy. ¿Se puede juntar? Si no, ¿cómo queda la expresión?", "No se puede; queda 2x + 3y", "x e y son letras distintas y sus términos no son semejantes."),
        ex("Pedro redujo 3x − 9x y obtuvo 6x. ¿Cuál es el resultado correcto?", "−6x", "3 − 9 = −6."),
    ],
    cha=[
        ex("Reduce −3x + 8y − 2z + x − 10y + 5z − 4x.", "−6x − 2y + 3z", "Con x: −3 + 1 − 4 = −6. Con y: 8 − 10 = −2. Con z: −2 + 5 = 3."),
        ex("¿Qué coeficiente entero hay que poner en k para que 7x + kx − 2y se reduzca a 2x − 2y?", "−5", "7 + k = 2 da k = −5."),
    ],
    ctx=[ex("Un negocio de ejemplo vende x sándwiches y y bebidas por día. En una semana, el lunes vendió 3x + 2y, el martes 5x − y y el miércoles 2x + 4y. Reduce la suma de los tres días.", "10x + 5y", "Con x: 3 + 5 + 2 = 10. Con y: 2 − 1 + 4 = 5.")],
    sc=[
        ex("Reduce 6x − 10x.", "−4x", "6 − 10 = −4."),
        ex("Reduce 3y + 2y − 8y.", "−3y", "3 + 2 − 8 = −3."),
        ex("Reduce 2x + 3y + 5x − 3y.", "7x", "Los términos con y se anulan."),
    ],
    op=task(
        "Reduce estas tres expresiones de ejemplo y escribe cada grupo de términos semejantes antes de dar el resultado: (a) 9x − 4y + 6 − 3x + 8y − 10; (b) −5x + 2y − 3z + 5x − 2y + 7z; (c) 4x − 11x + 3. Explica con una frase qué pasó con los términos de la expresión (b) que desaparecieron.",
        "(a) 6x + 4y − 4. (b) 4z (los términos con x y con y se anulan). (c) −7x + 3. Desaparecieron porque sus coeficientes sumaron 0.",
        ["reduce correctamente las tres expresiones", "agrupa antes de reducir", "explica los términos que se anulan"],
        ["agrupaciones escritas", "tres resultados", "frase de explicación"],
        ["olvidar el signo de un término", "juntar términos con letras distintas"],
        "Pide que compruebe cada resultado con x = 1, y = 1 y z = 1.",
    ),
    reinforce="Reduce 6x − 2x + 4y − 7y y 3z + 5 − 8z − 9.",
    extend="Escribe una expresión de seis términos que se reduzca a 2x − 3y y explica cómo la armaste.",
)

# ------------------------------------------------------------------ OA 07 clase 4
lesson(
    OA7, 4,
    use="Aprenderé a comprobar si una reducción está bien reemplazando las letras por números. Sirve para detectar errores y para decidir si dos expresiones son equivalentes.",
    prior=["Sé reducir expresiones con coeficientes enteros.", "Sé evaluar una expresión."],
    explain=[
        "Dos expresiones son equivalentes si dan el mismo valor para cualquier número que se ponga en lugar de la letra. Para comprobar una reducción, sustituye la letra por un número en la expresión original y en la reducida. Si los valores son distintos, hay un error. Por ejemplo, si reduces 6x − 2x + 3 a 4x + 3, con x = 5 ambas dan 23: coinciden.",
        "Un solo valor no basta para asegurar que son equivalentes. Las expresiones 2x + 3 y 5x coinciden en x = 1 (ambas valen 5), pero con x = 2 valen 7 y 10: no son equivalentes. Por eso conviene probar con dos o tres valores distintos, incluyendo valores negativos o el cero. Un valor que muestre una diferencia basta para saber que no son equivalentes.",
        "Cuando sustituyes, escribe cada paso: reemplaza la letra, calcula las multiplicaciones y luego suma y resta. Cuida los números negativos: con x = −2, 3x vale −6. Esta comprobación no reemplaza al razonamiento de agrupar términos semejantes, pero ayuda a encontrar el error cuando la respuesta no cuadra.",
    ],
    vocab=[("equivalentes", "expresiones que dan el mismo valor para cualquier número"), ("sustitución", "reemplazar la letra por un número"), ("contraejemplo", "valor que muestra que dos expresiones no son equivalentes"), ("comprobar", "revisar un resultado con otro camino"), ("valor numérico", "número que resulta al sustituir y calcular")],
    worked=[
        W("Comprobar una reducción", "Se redujo 3x + 5x − 2 como 8x − 2. Compruébalo con x = 4.", ["Original: 3 · 4 + 5 · 4 − 2 = 12 + 20 − 2 = 30.", "Reducida: 8 · 4 − 2 = 32 − 2 = 30. Coinciden."], "Es correcta"),
        W("Un contraejemplo", "¿Es 2x + 3 equivalente a 5x? Prueba con x = 1 y con x = 2.", ["Con x = 1: 2 + 3 = 5 y 5 · 1 = 5, coinciden.", "Con x = 2: 2 · 2 + 3 = 7 y 5 · 2 = 10, no coinciden."], "No son equivalentes"),
    ],
    mistakes=[
        M("Decir que dos expresiones son equivalentes porque coinciden con x = 0.", "Con 0 muchas expresiones distintas coinciden.", "Hay que probar varios valores; si uno no coincide, no son equivalentes."),
        M("Evaluar 3x con x = −2 y obtener 6.", "Se perdió el signo negativo.", "3 · (−2) = −6."),
    ],
    rec=[
        ex("Evalúa 3x + 2 con x = 4.", "14", "3 · 4 = 12 y 12 + 2 = 14."),
        ex("Evalúa 5x − x con x = 3.", "12", "15 − 3 = 12."),
        ex("Evalúa 2x + x con x = 5 y compara con 3x. ¿Coinciden?", "Sí; ambos valen 15", "10 + 5 = 15 y 3 · 5 = 15."),
    ],
    und=[
        ex("¿Dan el mismo valor 4x + 2x y 6x cuando x = 2? Responde con los valores.", "Sí; ambos valen 12", "8 + 4 = 12 y 6 · 2 = 12."),
        ex("Evalúa 5x − 3y con x = 2 e y = 1.", "7", "10 − 3 = 7."),
        ex("Evalúa 4 − 2x con x = −3.", "10", "4 − 2 · (−3) = 4 + 6."),
    ],
    app=[
        ex("Se redujo 6x − 2x + 3 como 4x + 3. Comprueba con x = 5: ¿qué valor da cada expresión?", "23 en ambas", "30 − 10 + 3 = 23 y 20 + 3 = 23."),
        ex("Se redujo 3x + 2y − x como 2x + 2y. Comprueba con x = 3 e y = 2: ¿qué valor da?", "10", "9 + 4 − 3 = 10 y 6 + 4 = 10."),
        ex("Se redujo 7x − 3x + 2 como 4x + 2. Comprueba con x = −2: ¿qué valor da?", "−6", "−14 + 6 + 2 = −6 y −8 + 2 = −6."),
    ],
    rea=[
        ex("Dani compara x + 2 con 2x y ve que con x = 2 ambas valen 4, así que dice que son equivalentes. ¿Qué valores dan con x = 3 y qué concluyes?", "5 y 6; no son equivalentes", "Con x = 3, x + 2 = 5 y 2x = 6: ese valor lo desmiente."),
        ex("Marta redujo 4x − x − 2x como 5x. Prueba con x = 1: ¿qué valores obtienes y es correcta?", "1 y 5; no es correcta", "4 − 1 − 2 = 1 y 5 · 1 = 5. El resultado correcto es x."),
    ],
    cha=[
        ex("Para las expresiones 5x + 1 y 3x + 7, ¿existe un valor de x en que valen lo mismo? Pruébalo con x = 3 y explica por qué no son equivalentes.", "Sí, x = 3 (ambas 16); no son equivalentes porque con x = 0 valen 1 y 7", "Para ser equivalentes deberían coincidir con todos los valores."),
        ex("Reduce 6x + 4 − 2x − 1 + y − y y comprueba con x = 2. Escribe la expresión reducida y su valor.", "4x + 3; 11", "6x − 2x = 4x, 4 − 1 = 3 y los términos con y se anulan. Con x = 2: 8 + 3 = 11."),
    ],
    ctx=[ex("Una tienda de ejemplo anota ventas como 5x + 3 + 2x − 1 y reduce a 7x + 2. Comprueba con x = 4: ¿qué valor da?", "30", "20 + 3 + 8 − 1 = 30 y 28 + 2 = 30.")],
    sc=[
        ex("Evalúa 2x + 7 con x = −1.", "5", "−2 + 7 = 5."),
        ex("¿Es 3x + 4x equivalente a 7x? Prueba con x = 2.", "Sí; ambas valen 14", "6 + 8 = 14 y 7 · 2 = 14."),
        ex("Si dos expresiones valen distinto con x = 5, ¿pueden ser equivalentes?", "No", "Un valor distinto es un contraejemplo."),
    ],
    op=task(
        "Una compañera de ejemplo redujo así: (a) 5x + 2x − 3 = 7x − 3; (b) 6x − 4x + 5 = 10x + 5; (c) 3x + 2y − x = 2x + 2y. Comprueba cada una sustituyendo x = 2 e y = 3 en la expresión original y en la reducida. Escribe cuál está mal, qué error cometió y cuál es la reducción correcta.",
        "(a) 14 − 3 = 11 y 14 − 3 = 11: correcta. (b) 12 − 8 + 5 = 9 pero 20 + 5 = 25: incorrecta; la correcta es 2x + 5 (4 + 5 = 9). (c) 6 + 6 − 2 = 10 y 4 + 6 = 10: correcta.",
        ["sustituye los mismos valores en ambas expresiones", "detecta la reducción incorrecta", "da la reducción correcta"],
        ["tres comprobaciones", "reducción corregida"],
        ["errores de signo al sustituir", "comprobar con un solo valor"],
        "Pide que pruebe con otro valor para confirmar la reducción corregida.",
    ),
    reinforce="Reduce 4x + 6 − x y comprueba con x = 2 y con x = −1.",
    extend="Inventa una reducción incorrecta que dé el mismo valor que la original con x = 1 pero falle con x = 2. Verifica con los dos valores.",
)
