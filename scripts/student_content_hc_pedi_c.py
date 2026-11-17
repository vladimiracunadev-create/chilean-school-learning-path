"""Probabilidades y estadística descriptiva e inferencial (electivo HC, 3.º y 4.º medio): OAC-03 (modelación con probabilidades, distribución binomial y distribución normal), clases 1 a 4. Todo a mano, con tablas escritas en la ficha; el software se describe por escrito."""
from __future__ import annotations

from hc_pedi_common import R, build

O3 = "MA-PEDI-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (de ejemplo). En una prueba de 5 preguntas de alternativas, cada una con 4 opciones y una sola correcta, un estudiante responde totalmente al azar. En cada pregunta la probabilidad de acertar es p = 1/4 = 0,25 "
     "y la de errar es q = 1 − p = 0,75; las respuestas son independientes. X es el número de aciertos. Fórmula binomial: P(X = k) = C(n, k) · p^k · q^(n−k), con C(n, k) = n! ÷ (k! · (n−k)!).")
build(
    O3, 1, F,
    use="Aprenderé a reconocer cuándo una situación se modela con una distribución binomial y a calcular la probabilidad de obtener exactamente k éxitos.",
    prior=["Sé calcular probabilidades simples como casos favorables sobre casos posibles.", "Sé multiplicar y operar con decimales.", "Sé calcular productos como 4 · 3 · 2 · 1."],
    explain=[
        "En Probabilidades, la probabilidad de un suceso es un número entre 0 y 1. El complemento de un suceso, es decir, que no ocurra, tiene probabilidad 1 − p. Dos sucesos son independientes si saber que uno ocurrió no cambia la probabilidad del otro; entonces la probabilidad de que ocurran ambos se calcula multiplicando: P(A y B) = P(A) · P(B). Un ensayo de Bernoulli es un experimento con solo dos resultados, éxito (con probabilidad p) o fracaso (con probabilidad q = 1 − p).",
        "Si repites un ensayo de Bernoulli y cuentas los éxitos, la variable X que obtienes es binomial, X ~ B(n, p), cuando se cumplen cuatro condiciones: el número de ensayos n está fijado de antemano; cada ensayo tiene solo dos resultados; la probabilidad de éxito p es la misma en todos; y los ensayos son independientes. Si una de ellas falla (por ejemplo, sacar bolas sin devolverlas, que cambia p), el modelo binomial no es adecuado.",
        "Para calcular la probabilidad de exactamente k éxitos, un orden concreto de éxitos y fracasos tiene probabilidad p^k · q^(n−k). Pero hay C(n, k) órdenes posibles, que se cuentan con el número combinatorio C(n, k) = n! ÷ (k! · (n−k)!), donde n! es el producto de los números de 1 a n. Entonces P(X = k) = C(n, k) · p^k · q^(n−k). Los eventos pasados no «compensan»: si respondes al azar, aunque aciertes cuatro seguidas, la siguiente sigue teniendo probabilidad p.",
    ],
    vocab=[("ensayo de Bernoulli", "experimento con solo dos resultados: éxito o fracaso"), ("variable binomial", "número de éxitos en n ensayos independientes con la misma probabilidad p"), ("independencia", "un suceso no cambia la probabilidad del otro"), ("complemento", "que el suceso no ocurra: probabilidad 1 − p"), ("C(n, k)", "cantidad de formas de elegir en cuáles k de los n ensayos ocurre el éxito"), ("n!", "producto de los números enteros de 1 hasta n")],
    worked=[
        ("Probabilidad de dos éxitos seguidos", "En la prueba de la ficha, ¿cuál es la probabilidad de acertar al azar las dos primeras preguntas?", ["Los aciertos son independientes, así que se multiplica: 0,25 × 0,25.", "0,25 × 0,25 = 0,0625."], "0,0625, es decir, 6,25 %"),
        ("Aplicar la fórmula", "Una variable tiene n = 3 y p = 0,2. Calcula P(X = 1).", ["C(3, 1) = 3; p¹ = 0,2; q² = 0,8² = 0,64.", "P = 3 × 0,2 × 0,64 = 0,384."], "P(X = 1) = 0,384"),
    ],
    mistakes=[("Calcular P(X = k) como solo p^k, sin el combinatorio ni el factor de los fracasos.", "Faltan los fracasos q^(n−k) y las C(n, k) formas de ordenar los éxitos.", "Escribe siempre los tres factores: C(n, k), p^k y q^(n−k)."),
              ("Creer que después de muchos aciertos «toca fallar».", "Los ensayos son independientes y no tienen memoria.", "Usa p en cada ensayo, sin importar lo que pasó antes.")],
    T=[
        ('abc', '{F} ¿Cuál es la probabilidad de errar una pregunta?', '0,75', '0,25', '0,5', 'El complemento de acertar es 1 − 0,25 = 0,75; 0,25 es la probabilidad de acertar.'),
        ('ab', '¿Qué es un ensayo de Bernoulli?', 'Un experimento con solo dos resultados: éxito o fracaso', 'Un experimento con cualquier cantidad de resultados igual de probables', 'Se llama así a un experimento aleatorio con exactamente dos resultados, éxito o fracaso.'),
        ('=', '{F} ¿Cuál es la probabilidad de errar las dos primeras preguntas?', '3*3/(4*4)', 'Como son independientes, se multiplica 3/4 por 3/4.', ''),
        ('abc', '¿Cuál de estas es una condición del modelo binomial?', 'El número de ensayos n está fijado de antemano', 'Cada ensayo debe tener una probabilidad distinta', 'Debe haber al menos tres resultados posibles en cada ensayo', 'El modelo exige n fijo, dos resultados, p constante e independencia.'),
        ('abc', '¿Cuál de estas variables es binomial?', 'El número de 6 que salen en 10 lanzamientos independientes de un dado', 'El número de lanzamientos que hacen falta hasta obtener el primer 6', 'El tiempo de espera de un bus, en minutos', 'Con n = 10 fijo, éxito «sale 6» con p = 1/6 y ensayos independientes, se cumplen las cuatro condiciones.'),
        ('abc', 'De una urna con 3 bolas rojas y 2 azules se sacan 2 bolas, una tras otra y sin devolverlas. X cuenta las rojas. ¿Es binomial?', 'No: al no devolver las bolas, la probabilidad de roja cambia y los ensayos no son independientes', 'Sí: hay solo dos colores', 'Sí: n = 2 está fijado de antemano', 'Que haya dos colores y n fijo no basta: si la probabilidad cambia entre extracciones, falla la independencia.'),
        ('=', 'Calcula el número combinatorio C(6, 2) = 6! ÷ (2! · 4!).', '(6*5*4*3*2*1)/((2*1)*(4*3*2*1))', 'Se desarrollan los factoriales y se divide el producto del numerador por el del denominador.', ''),
        ('abc', '{F} ¿Cuál es la probabilidad de no acertar ninguna de las 5 preguntas, P(X = 0)?', 'Aproximadamente 0,2373', '0,75', '0,25', 'P(X = 0) = 0,75 elevado a 5, que es 0,2373 aproximadamente; 0,75 es solo una pregunta.'),
        ('{F} Calcula P(X = 2) con la fórmula binomial.', R("10*0.25**2*0.75**3", 4), 'C(5, 2) = 10 y 10 × 0,0625 × 0,421875 da el valor, que sale aproximadamente 0,2637.'),
        ('ab', 'Una persona respondió al azar y acertó cuatro preguntas seguidas. Dice: «ahora me toca fallar la siguiente». ¿Es correcto?', 'No: las respuestas son independientes y la probabilidad de acertar sigue siendo 0,25', 'Sí: ya acertó mucho y el azar tiene que compensar', 'La independencia significa que los resultados anteriores no cambian la probabilidad de la siguiente pregunta.'),
        ('abc', 'Un estudiante calcula P(X = 1) con n = 4 y p = 0,5 como 0,5. ¿Cuál es su error y el valor correcto?', 'Olvidó C(4, 1) = 4 y los fracasos; el valor correcto es 0,25', 'Olvidó dividir por n; el valor correcto es 0,125', 'No hay error: 0,5 es el valor correcto', 'P(X = 1) = 4 × 0,5 × 0,5³ = 0,25; el 0,5 solo es la probabilidad de un ensayo.'),
        ('{F} Calcula la probabilidad de acertar al menos una de las 5 preguntas (usa el complemento de no acertar ninguna).', R("1-0.75**5", 4), 'Al menos una es lo contrario de ninguna: 1 − 0,2373 da aproximadamente 0,7627.'),
        ('=', 'Un examen de 6 preguntas de verdadero o falso se responde al azar (p = 0,5). ¿Cuál es la probabilidad de acertar exactamente 3?', '20/64', 'C(6, 3) = 20 y 0,5 elevado a 6 es 1/64, así que la probabilidad es 20/64.', ''),
    ],
    ctx=('abc', 'En una línea de producción de ejemplo, el 10 % de las piezas sale con un defecto, de forma independiente. Se revisan 3 piezas. ¿Cuál es la probabilidad de que exactamente 1 sea defectuosa?', '0,243', '0,1', '0,3', 'P = C(3, 1) × 0,1 × 0,9² = 3 × 0,1 × 0,81 = 0,243; 0,1 es la de una pieza y 0,3 suma sin multiplicar.'),
    sc=[
        ("En Probabilidades: ¿cuál es la probabilidad del complemento de un suceso con probabilidad p?", "1 − p", "El suceso y su complemento cubren todos los casos y suman 1."),
        ("¿Cómo se calcula la probabilidad de que ocurran dos sucesos independientes?", "Multiplicando sus probabilidades", "Si son independientes, P(A y B) = P(A) · P(B)."),
        ("¿Cuáles son las cuatro condiciones del modelo binomial?", "n fijo, dos resultados, p constante e independencia", "Si falla alguna, el modelo binomial no representa bien la situación."),
    ],
    op=("Para cada una de estas tres situaciones de ejemplo decide si se puede modelar con una binomial. A: se lanza 5 veces una moneda equilibrada y se cuentan las caras. B: de una bolsa de 10 caramelos (4 de limón y 6 de naranja) se sacan 3 sin devolverlos y se cuentan los de limón. C: se pregunta a 10 personas elegidas al azar en una ciudad muy grande si les gusta cierto deporte, sabiendo que a un 30 % le gusta, y se cuentan las que dicen que sí (como la ciudad es muy grande, puedes tratar las respuestas como independientes y con p constante). Si es binomial, indica n, p y X, y calcula la probabilidad de que ningún ensayo sea éxito; si no lo es, explica qué condición falla.",
        "A es binomial con n = 5, p = 0,5 y X = número de caras; P(ninguna cara) = 0,5⁵ = 0,03125. B no es binomial: al no devolver los caramelos, la probabilidad de limón cambia en cada extracción. C se acepta como binomial con n = 10 y p = 0,3, porque la ciudad es muy grande; P(ninguna) = 0,7¹⁰ ≈ 0,0282.",
        ["decide correctamente cada situación", "nombra n, p y X cuando es binomial", "identifica la condición que falla en B", "calcula bien la probabilidad de ningún éxito"],
        ["hoja con tres decisiones justificadas y los cálculos de P(X = 0)"],
        ["aceptar como binomial una situación sin reposición", "olvidar elevar q a la potencia n", "no explicar la condición que falla"],
        "Pregunta: «¿qué condición del modelo comprobaste primero?». Si no nombra ninguna, pide que las repase una por una."),
    reinforce="Calcula P(X = 4) para la prueba de la ficha (n = 5, p = 0,25) y explica por qué es mucho menor que P(X = 1).",
    extend="Explica por qué, al sacar 3 bolas con devolución de una urna, el modelo sí es binomial, y qué cambia cuando no hay devolución.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (de ejemplo). Un jugador encesta el 40 % de sus lanzamientos libres, de forma independiente, y lanza 5 veces; X es el número de encestes, X ~ B(5; 0,4). "
     "Tabla (de ejemplo, redondeada a 5 decimales como máximo): P(0) = 0,07776; P(1) = 0,2592; P(2) = 0,3456; P(3) = 0,2304; P(4) = 0,0768; P(5) = 0,01024. "
     "Para una binomial, la media (valor esperado) es μ = n·p, la varianza es σ² = n·p·q y la desviación estándar es σ = √(n·p·q).")
build(
    O3, 2, F,
    use="Aprenderé a leer una distribución binomial en tabla y en gráfico de barras, a calcular probabilidades acumuladas con complementos y a usar μ y σ para decidir.",
    prior=["Sé calcular P(X = k) con la fórmula binomial.", "Sé sumar y restar decimales.", "Sé qué es una media y una desviación estándar."],
    explain=[
        "Una distribución binomial se puede representar de dos maneras: con la fórmula y con una tabla o un gráfico de barras que muestra P(X = k) para cada k. Todas las probabilidades suman 1. Si p = 0,5, el gráfico es simétrico; si p es menor que 0,5, la barra más alta está en valores bajos y la cola se alarga hacia la derecha; si p es mayor que 0,5, ocurre lo contrario.",
        "Muchas preguntas piden probabilidades acumuladas. «A lo más k» significa X ≤ k y se calcula sumando P(0), P(1), …, P(k). «Al menos k» significa X ≥ k; conviene usar el complemento: P(X ≥ k) = 1 − P(X ≤ k − 1). «Entre a y b, inclusive» suma las probabilidades de a a b. Como la tabla ya trae los valores, no es necesario volver a aplicar la fórmula.",
        "El valor esperado μ = n·p es el promedio de éxitos a largo plazo si repites todo el experimento muchas veces; no tiene por qué ser un valor posible de X. La desviación estándar σ = √(n·p·q) indica cuánto se alejan típicamente los resultados de μ. Con estas medidas y las probabilidades se pueden tomar decisiones: por ejemplo, un resultado cuya probabilidad es menor que 5 % se puede considerar poco probable bajo el modelo, y eso hace dudar de él.",
    ],
    vocab=[("distribución", "tabla o gráfico con las probabilidades de cada valor de X"), ("probabilidad acumulada", "probabilidad de que X sea menor o igual que un valor"), ("valor esperado μ", "promedio a largo plazo de la variable, n·p en la binomial"), ("varianza σ²", "medida de dispersión de la variable, n·p·q en la binomial"), ("complemento", "regla P(X ≥ k) = 1 − P(X ≤ k − 1)"), ("poco probable", "con probabilidad menor que un umbral acordado, como 5 %")],
    worked=[
        ("A lo más y al menos", "Una variable de ejemplo toma los valores 0, 1, 2 y 3 con probabilidades 0,1; 0,3; 0,4 y 0,2. Calcula P(X ≤ 1) y P(X ≥ 2).", ["P(X ≤ 1) = 0,1 + 0,3 = 0,4.", "P(X ≥ 2) = 1 − P(X ≤ 1) = 1 − 0,4 = 0,6, que coincide con 0,4 + 0,2."], "P(X ≤ 1) = 0,4 y P(X ≥ 2) = 0,6"),
        ("Media y desviación", "Una binomial de ejemplo tiene n = 20 y p = 0,1. Calcula μ y σ².", ["μ = n·p = 20 × 0,1 = 2.", "σ² = n·p·q = 20 × 0,1 × 0,9 = 1,8."], "μ = 2 y σ² = 1,8"),
    ],
    mistakes=[("Calcular P(X ≥ 3) como 1 − P(X ≤ 3).", "Eso deja fuera el valor 3: «al menos 3» incluye el 3.", "Usa 1 − P(X ≤ 2) o suma P(3) + P(4) + P(5)."),
              ("Pensar que μ = 2 significa que siempre se obtienen 2 éxitos.", "μ es un promedio a largo plazo, no un resultado garantizado.", "Interprétalo como el valor típico alrededor del cual varían los resultados.")],
    T=[
        ('abc', '{F} ¿Cuál es el valor más probable de X?', '2 encestes', '3 encestes', '1 enceste', 'La barra más alta de la tabla es P(2) = 0,3456, el mayor de los seis valores.'),
        ('{F} Calcula P(X ≤ 1), la probabilidad de a lo más 1 enceste.', R("0.07776+0.2592", 5), 'Se suman P(0) y P(1), que da 0,33696.'),
        ('abc', 'Con n = 5 y p = 0,1, ¿en qué valor de X esperas la barra más alta del gráfico?', 'En X = 0, porque los éxitos son poco probables', 'En X = 5, porque n es 5', 'En X = 2 o 3, porque la barra más alta siempre está en el centro', 'Con p pequeña lo más probable es obtener pocos éxitos, y el gráfico se alarga hacia la derecha.'),
        ('{F} Calcula P(X ≥ 4), la probabilidad de al menos 4 encestes.', R("0.0768+0.01024", 5), 'Se suman P(4) y P(5), que da 0,08704.'),
        ('=', '{F} ¿Cuántos encestes se esperan en promedio? Calcula μ = n · p.', '5*4/10', 'Se multiplica el número de lanzamientos 5 por la probabilidad 0,4, que es 4/10.', ' encestes'),
        ('{F} Calcula P(X ≥ 3) usando el complemento 1 − P(X ≤ 2).', R("1-(0.07776+0.2592+0.3456)", 5), 'La suma P(0) + P(1) + P(2) es 0,68256 y su complemento es 0,31744.'),
        ('ab', 'El valor esperado de una binomial es μ = 2 encestes. ¿Significa que siempre se enceste 2 veces?', 'No: es el promedio a largo plazo; en un grupo de lanzamientos puede salir otro valor', 'Sí: μ es el único resultado posible', 'El valor esperado resume lo que se obtiene en promedio al repetir muchas veces, pero cada repetición varía.'),
        ('=', '{F} Calcula la varianza σ² = n · p · q.', '5*4*6/100', 'Con q = 0,6 se multiplica 5 por 0,4 y por 0,6, o sea 5 × 4 × 6 ÷ 100.', ''),
        ('Una binomial tiene n = 12 y p = 0,25. Calcula μ y σ.', 'μ = 3 y σ = 1,5', 'μ = 12 × 0,25 = 3; σ² = 12 × 0,25 × 0,75 = 2,25 y la raíz cuadrada de 2,25 es 1,5.'),
        ('abc', '{F} Una regla acordada dice que un resultado con probabilidad menor que 5 % se considera poco probable bajo el modelo. Si el jugador encesta los 5 lanzamientos, ¿qué se concluye?', 'Es poco probable: P(X = 5) = 0,01024, cerca de 1 %, menos de 5 %', 'Es lo normal para quien lanza bien, así que no hay nada que concluir', 'No es poco probable, porque 0,01024 es mayor que 5 %', 'El valor 0,01024 equivale a 1,024 %, menor que 5 %, y por eso el resultado es poco probable bajo p = 0,4.'),
        ('abc', '¿Por qué conviene calcular P(X ≥ 1) como 1 − P(X = 0)?', 'Porque el complemento de «al menos 1» es «ninguno», que es un solo término', 'Porque P(X = 0) siempre es 0,5', 'Porque P(X ≥ 1) siempre es mayor que 1', 'Sumar todos los casos desde 1 es largo; el complemento solo necesita calcular P(0).'),
        ('{F} Si el jugador lanzara 10 veces con el mismo 40 %, ¿cuál sería μ y cuál σ?', f'μ = 4 y σ ≈ {R("sqrt(10*0.4*0.6)", 2)}', 'μ = 10 × 0,4 = 4 y σ es la raíz cuadrada de 10 × 0,4 × 0,6 = 2,4, que da aproximadamente 1,55.'),
        ('{F} Calcula la probabilidad de que enceste de 1 a 3 veces (inclusive).', R("0.2592+0.3456+0.2304", 4), 'Se suman P(1), P(2) y P(3), y el resultado es 0,8352.'),
    ],
    ctx=('abc', 'Una tienda de ejemplo sabe que 1 de cada 5 clientes (p = 0,2) paga con tarjeta, de forma independiente, y atiende a 4 clientes. ¿Cuántos pagos con tarjeta espera y cómo se interpreta?', '0,8: es el promedio a largo plazo; en 4 clientes pueden ser 0, 1, 2 o más', '0,8: exactamente un cliente pagará con tarjeta', '2: la mitad de los clientes pagará con tarjeta', 'μ = 4 × 0,2 = 0,8; no es un resultado posible de un día, sino un promedio a largo plazo.'),
    sc=[
        ("En Probabilidades: ¿cómo se calcula P(X ≥ k) usando el complemento?", "1 − P(X ≤ k − 1)", "«Al menos k» es lo contrario de «a lo más k − 1»."),
        ("¿Qué fórmulas dan la media y la varianza de una binomial?", "μ = n·p y σ² = n·p·q", "Son las fórmulas del valor esperado y la varianza del modelo binomial."),
        ("¿Es μ siempre un valor posible de X?", "No, puede ser decimal", "Es un promedio a largo plazo y no tiene por qué ser un entero."),
    ],
    op=("Elige uno de estos casos de ejemplo. Caso 1: cada semilla germina con p = 0,8, de forma independiente, y se siembran 4; las probabilidades de X = 0, 1, 2, 3 y 4 son 0,0016; 0,0256; 0,1536; 0,4096 y 0,4096. Caso 2: de 5 personas, cada una prefiere cierto jugo con p = 0,3, y las probabilidades de X = 0 a 5 son 0,16807; 0,36015; 0,3087; 0,1323; 0,02835 y 0,00243. Comprueba que las probabilidades suman 1, dibuja el gráfico de barras, calcula P(X ≥ 3), μ y σ, y escribe una decisión usando el umbral de 5 %.",
        "Caso 1: suman 1. P(X ≥ 3) = 0,4096 + 0,4096 = 0,8192; μ = 4 × 0,8 = 3,2; σ² = 4 × 0,8 × 0,2 = 0,64 y σ = 0,8. Como P(X ≥ 2) = 1 − 0,0272 = 0,9728, mayor que 90 %, con 4 semillas es muy probable que germinen al menos 2.",
        ["comprueba que la suma de probabilidades es 1", "gráfico de barras con ejes rotulados", "calcula P(X ≥ 3), μ y σ correctamente", "decisión que cita una probabilidad y el umbral"],
        ["hoja con la verificación, el gráfico y los cálculos de P, μ y σ"],
        ["usar 1 − P(X ≤ 3) para «al menos 3»", "interpretar μ como resultado seguro", "decidir sin citar la probabilidad"],
        "Pregunta: «¿qué suma hiciste para P(X ≥ 3)?». Si suma desde 4, pide que escriba qué valores incluye «al menos 3»."),
    reinforce="Con los datos del Caso 2, calcula P(X ≤ 1) y compara con P(X ≥ 4): ¿cuál de los dos extremos es más probable?",
    extend="Explica por qué el gráfico de una binomial con p = 0,9 es el «espejo» del gráfico con p = 0,1, y qué ocurre con μ.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (de ejemplo). La duración de un tipo de batería se distribuye normal con media μ = 40 horas y desviación estándar σ = 8 horas, X ~ N(40; 8). Estandarización: z = (x − μ) ÷ σ. "
     "Tabla de la normal estándar, Φ(z) = proporción de datos con valor menor o igual que z: Φ(0) = 0,5000; Φ(0,25) = 0,5987; Φ(0,50) = 0,6915; Φ(0,75) = 0,7734; Φ(1,00) = 0,8413; Φ(1,25) = 0,8944; "
     "Φ(1,50) = 0,9332; Φ(1,75) = 0,9599; Φ(2,00) = 0,9772; Φ(2,50) = 0,9938; Φ(3,00) = 0,9987. Para z negativo: Φ(−z) = 1 − Φ(z). Regla empírica: alrededor de 68 %, 95 % y 99,7 % de los datos están a menos de 1, 2 y 3 desviaciones estándar de la media.")
build(
    O3, 3, F,
    use="Aprenderé a calcular probabilidades con la distribución normal: estandarizar, leer la tabla de Φ y usar la regla empírica, justificando que el modelo es razonable.",
    prior=["Sé leer un histograma y una desviación estándar.", "Sé calcular proporciones y complementos.", "Sé usar una tabla de valores."],
    explain=[
        "La distribución normal describe variables continuas, como una duración o una masa, cuyo histograma tiene forma de campana simétrica. Se determina con dos parámetros: la media μ, que es el centro y el eje de simetría, y la desviación estándar σ, que controla el ancho de la campana. El área total bajo la curva es 1; una probabilidad es el área sobre un intervalo. Como X es continua, la probabilidad de un valor exacto es 0 y solo tienen sentido las probabilidades de intervalos.",
        "Para calcular áreas se estandariza: z = (x − μ) ÷ σ cuenta cuántas desviaciones estándar está x de la media. Así toda normal se convierte en la normal estándar N(0; 1), cuya tabla da Φ(z). Para P(X ≤ x) se lee Φ(z); para P(X > x) se usa el complemento 1 − Φ(z); para P(a < X < b) se resta Φ(zb) − Φ(za). Si z es negativo, se usa la simetría: Φ(−z) = 1 − Φ(z). La regla empírica 68 – 95 – 99,7 permite estimar sin tabla.",
        "Usar el modelo normal es un supuesto que se debe justificar: el histograma de los datos debe ser simétrico y con forma de campana, sin muchos valores extremos. Si los datos son muy asimétricos, las probabilidades de la tabla pueden ser engañosas. Una hoja de cálculo o una calculadora estadística entrega Φ(z) con una función, pero aquí usas la tabla de la ficha para entender qué área estás midiendo.",
    ],
    vocab=[("distribución normal", "modelo en forma de campana simétrica determinado por μ y σ"), ("estandarización", "convertir x en z = (x − μ) ÷ σ"), ("normal estándar", "normal con media 0 y desviación estándar 1"), ("Φ(z)", "probabilidad de que la normal estándar sea menor o igual que z"), ("regla empírica", "68 %, 95 % y 99,7 % a 1, 2 y 3 desviaciones estándar de la media"), ("variable continua", "variable que puede tomar cualquier valor de un intervalo")],
    worked=[
        ("P(X ≤ x)", "X ~ N(100; 10). Calcula P(X ≤ 115) con la tabla de la ficha.", ["z = (115 − 100) ÷ 10 = 1,5.", "Se lee en la tabla: Φ(1,50) = 0,9332."], "P(X ≤ 115) = 0,9332"),
        ("P(a < X < b)", "X ~ N(100; 10). Calcula P(90 < X < 125).", ["z de 90: (90 − 100) ÷ 10 = −1, y Φ(−1) = 1 − 0,8413 = 0,1587; z de 125: 2,5 y Φ(2,5) = 0,9938.", "Se resta: 0,9938 − 0,1587 = 0,8351."], "P(90 < X < 125) = 0,8351"),
    ],
    mistakes=[("Buscar en la tabla el valor de x sin estandarizar.", "La tabla corresponde a la normal estándar y no a la variable con su media y su desviación.", "Calcula z = (x − μ) ÷ σ antes de leer la tabla."),
              ("Leer Φ(z) como la probabilidad de la cola derecha, o usar z negativo sin la simetría.", "Φ(z) es el área a la izquierda de z y para z negativo hay que usar 1 − Φ(|z|).", "Dibuja la campana, sombrea el área pedida y decide si restas o usas el complemento.")],
    T=[
        ('abc', '{F} ¿Cuál es el valor z de una batería que dura 52 horas?', '1,5', '12', '6,5', 'z = (52 − 40) ÷ 8 = 1,5; 12 es solo la diferencia con la media y 6,5 divide 52 por 8.'),
        ('{F} Calcula P(X ≤ 48), la proporción de baterías que duran 48 horas o menos.', '0,8413', 'z = (48 − 40) ÷ 8 = 1 y la tabla da Φ(1) = 0,8413.'),
        ('ab', 'La curva normal es simétrica respecto de...', 'La media μ', 'El valor más alto del eje horizontal', 'El centro de la campana coincide con μ, y a ambos lados hay la misma área.'),
        ('=', '{F} Calcula el valor z de una batería que dura 36 horas.', '(36-40)/8', 'Se resta la media 40 de 36 y se divide por 8, lo que da un z negativo.', ''),
        ('{F} Calcula P(X > 52), la proporción de baterías que duran más de 52 horas.', R("1-0.9332", 4), 'Con z = 1,5 se usa el complemento: 1 − Φ(1,5) = 1 − 0,9332.'),
        ('abc', '{F} Según la regla empírica, ¿entre qué valores está aproximadamente el 95 % de las baterías?', 'Entre 24 y 56 horas', 'Entre 32 y 48 horas', 'Entre 16 y 64 horas', 'El 95 % está a 2 desviaciones estándar de la media: 40 ± 16 da 24 y 56; los otros intervalos son 68 % y 99,7 %.'),
        ('{F} Calcula P(X ≤ 32), la proporción que dura 32 horas o menos.', R("1-0.8413", 4), 'z = −1 y se usa la simetría: Φ(−1) = 1 − Φ(1) = 1 − 0,8413.'),
        ('{F} Calcula P(44 < X < 54).', R("0.9599-0.6915", 4), 'z de 44 es 0,5 y z de 54 es 1,75; se resta Φ(1,75) − Φ(0,50) = 0,9599 − 0,6915.'),
        ('abc', '¿Por qué en una normal la probabilidad de que X valga exactamente 48 es 0?', 'Porque X es continua: las probabilidades son áreas sobre intervalos, no sobre un punto', 'Porque 48 está lejos de la media', 'Porque la tabla no tiene el valor 48', 'Un punto no tiene ancho y por eso su área es 0; solo se calculan probabilidades de intervalos.'),
        ('abc', '{F} Una batería tiene z = −2. ¿Qué significa?', 'Dura 2 desviaciones estándar menos que la media, es decir, 24 horas', 'Dura 2 horas menos que la media', 'Dura el doble de la media', 'z = −2 significa 2 desviaciones estándar bajo la media: 40 − 2 × 8 = 24 horas.'),
        ('abc', 'Ana obtuvo 80 en una prueba con media 70 y σ = 10; Luis obtuvo 72 en otra prueba con media 60 y σ = 8. Las dos notas son normales. ¿Quién tuvo mejor desempeño relativo?', 'Luis, con z = 1,5 frente al z = 1 de Ana', 'Ana, porque su puntaje 80 es mayor que 72', 'Los dos igual, porque ambos superan la media', 'El desempeño relativo se compara con z; aunque Ana tiene más puntos, Luis está más lejos de su media en desviaciones.'),
        ('{F} Calcula la proporción de baterías que duran entre 32 y 56 horas.', R("0.9772-(1-0.8413)", 4), 'z de 32 es −1 y z de 56 es 2; se resta Φ(2) − Φ(−1) = 0,9772 − 0,1587.'),
        ('=', 'Un histograma de 200 baterías de este tipo tiene forma de campana con media 40 y σ = 8. Aproximadamente, ¿cuántas duran entre 32 y 48 horas, según la regla empírica?', '68*200//100', 'Entre 32 y 48 horas hay una desviación estándar a cada lado de la media, que es cerca de 68 %.', ' baterías'),
    ],
    ctx=('abc', '{F} Un fabricante repone gratis las baterías que duran menos de 28 horas. ¿Qué proporción aproximada repondrá?', 'Cerca de 6,7 %', 'Cerca de 93,3 %', 'Cerca de 1,5 %', 'z = (28 − 40) ÷ 8 = −1,5 y Φ(−1,5) = 1 − 0,9332 = 0,0668, aproximadamente 6,7 %.'),
    sc=[
        ("En Estadística: ¿cómo se estandariza un valor x?", "z = (x − μ) ÷ σ", "El valor z indica cuántas desviaciones estándar está x de la media."),
        ("¿Cuánto vale el área total bajo la curva normal?", "1", "Es la probabilidad de todos los valores posibles."),
        ("Según la regla empírica, ¿qué porcentaje de los datos queda a menos de una desviación estándar de la media?", "Cerca de 68 %", "La regla empírica fija 68 % para 1σ, 95 % para 2σ y 99,7 % para 3σ."),
    ],
    op=("Elige uno de estos casos de ejemplo, ambos con distribución normal. Caso 1: el tiempo de reparto de pedidos es N(30; 5) minutos. Caso 2: el puntaje de un ensayo es N(500; 100). Para el Caso 1 calcula P(X < 35), P(X > 40) y P(27,5 < X < 37,5); para el Caso 2 calcula P(X < 650), P(X > 575) y P(400 < X < 750). Dibuja una campana para cada cálculo, sombrea el área, y escribe una decisión que use una de las probabilidades. Usa la tabla de la ficha.",
        "Caso 1: P(X < 35) = Φ(1) = 0,8413; P(X > 40) = 1 − Φ(2) = 0,0228; P(27,5 < X < 37,5) = Φ(1,5) − Φ(−0,5) = 0,9332 − 0,3085 = 0,6247. Decisión: si se promete entrega en 35 minutos, se cumple aproximadamente el 84 % de las veces.",
        ["estandariza antes de leer la tabla", "usa la simetría o el complemento cuando corresponde", "dibuja y sombrea el área de cada cálculo", "decisión que cita una probabilidad"],
        ["hoja con tres cálculos dibujados y la decisión escrita"],
        ["leer la tabla con x sin estandarizar", "olvidar el complemento en P(X > a)", "no justificar si el modelo normal es razonable"],
        "Pregunta: «¿qué área sombreaste y por qué restas?». Si no la dibujó, pide el esquema antes del cálculo."),
    reinforce="Con X ~ N(40; 8), calcula P(X ≤ 56) y P(X ≤ 24), y explica qué representa la diferencia entre ambas.",
    extend="Explica qué ocurriría con la probabilidad de duraciones entre 32 y 48 horas si σ fuera 4 en lugar de 8, sin hacer la tabla completa.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (de ejemplo). Se lanza 100 veces una moneda equilibrada y X es el número de caras: X ~ B(100; 0,5), con μ = n·p = 50 y σ = √(n·p·q) = √25 = 5. "
     "Aproximación normal: si n·p ≥ 5 y n·q ≥ 5, X se aproxima con una normal N(μ; σ). Corrección por continuidad: P(X ≤ k) ≈ Φ((k + 0,5 − μ) ÷ σ) y P(X ≥ k) ≈ 1 − Φ((k − 0,5 − μ) ÷ σ). "
     "Tabla: Φ(0,5) = 0,6915; Φ(1,0) = 0,8413; Φ(1,5) = 0,9332; Φ(2,0) = 0,9772; Φ(2,5) = 0,9938; para z negativo, Φ(−z) = 1 − Φ(z).")
build(
    O3, 4, F,
    use="Aprenderé a decidir entre la binomial y la normal, a aproximar una binomial con una normal comprobando condiciones, y a comunicar si un resultado es poco probable.",
    prior=["Sé calcular μ y σ de una binomial.", "Sé usar la tabla de la normal estándar.", "Sé estandarizar un valor."],
    explain=[
        "Cuando n es grande, calcular probabilidades binomiales con la fórmula es muy largo, pero la distribución binomial se parece mucho a una normal con la misma media y desviación: μ = n·p y σ = √(n·p·q). Esta aproximación es razonable si n·p y n·q son ambos al menos 5; si p está muy cerca de 0 o de 1 y n es pequeño, la binomial es muy asimétrica y la normal funciona mal.",
        "La binomial toma valores enteros y la normal es continua, así que se aplica una corrección por continuidad: cada entero k se representa por el intervalo de k − 0,5 a k + 0,5. Por eso P(X ≤ k) se calcula con k + 0,5, y P(X ≥ k) con k − 0,5. Después se estandariza y se usa la tabla. El resultado es una aproximación, no un valor exacto, y conviene decir «aproximadamente».",
        "Elegir el modelo es parte de la modelación. Si cuentas éxitos en pocos ensayos, usa la binomial exacta. Si cuentas éxitos en muchos ensayos y se cumplen las condiciones, puedes aproximar con la normal. Si mides una magnitud continua con histograma en forma de campana, usa la normal directamente. En todos los casos, un resultado con probabilidad menor que 5 % se considera poco probable bajo el modelo, lo que invita a revisar si el modelo (por ejemplo, que la moneda sea equilibrada) es correcto.",
    ],
    vocab=[("aproximación normal", "usar una normal para calcular probabilidades de una binomial"), ("corrección por continuidad", "sumar o restar 0,5 al pasar de un valor entero a uno continuo"), ("n·p y n·q", "valores que deben ser al menos 5 para aproximar"), ("modelación", "elegir un modelo matemático para una situación"), ("poco probable", "con probabilidad menor que un umbral acordado, como 5 %"), ("supuesto", "condición que se acepta para usar un modelo")],
    worked=[
        ("Comprobar condiciones", "Un taller de ejemplo revisa 40 piezas con p = 0,1 de defecto. ¿Se puede aproximar con una normal?", ["n·p = 40 × 0,1 = 4, que es menor que 5.", "Como no se cumple n·p ≥ 5, la aproximación no es recomendable."], "No: usa la binomial exacta"),
        ("Aproximar una probabilidad", "X ~ B(36; 0,5), con μ = 18 y σ = 3. Aproxima P(X ≤ 19).", ["Con la corrección: (19 + 0,5 − 18) ÷ 3 = 0,5.", "Φ(0,5) = 0,6915."], "P(X ≤ 19) ≈ 0,6915"),
    ],
    mistakes=[("Aproximar con la normal sin comprobar n·p y n·q.", "Con p cercana a 0 y n pequeña, la binomial es muy asimétrica y la normal falla.", "Verifica n·p ≥ 5 y n·q ≥ 5 antes de aproximar."),
              ("Olvidar la corrección por continuidad, usando k en vez de k ± 0,5.", "El entero k ocupa un intervalo de ancho 1 y la omisión sesga el resultado.", "Usa k + 0,5 para «a lo más» y k − 0,5 para «al menos».")],
    T=[
        ('abc', '{F} ¿Cuál es la media μ de X?', '50 caras', '100 caras', '25 caras', 'μ = n·p = 100 × 0,5 = 50; 100 es n y 25 es n·p·q.'),
        ('=', '{F} Calcula n · p · q con n = 100, p = 0,5 y q = 0,5.', '100*5*5/100', 'Se multiplica 100 por 0,5 y por 0,5, o sea 100 × 5 × 5 ÷ 100.', ''),
        ('abc', '¿Cuándo es razonable aproximar una binomial con una normal?', 'Cuando n·p y n·q son ambos al menos 5', 'Cuando n es menor que 10', 'Solo cuando p vale exactamente 0,5', 'La regla práctica exige que haya al menos 5 éxitos y 5 fracasos esperados.'),
        ('ab', 'Para aproximar P(X ≤ 52) con corrección de continuidad, ¿qué valor se estandariza?', '52,5', '52', 'Para «a lo más» se suma 0,5, porque el entero 52 ocupa el intervalo hasta 52,5.'),
        ('{F} Aproxima P(X ≤ 52) con la corrección de continuidad.', '≈ 0,6915', 'z = (52,5 − 50) ÷ 5 = 0,5 y la tabla da Φ(0,5) = 0,6915.'),
        ('{F} Aproxima P(X ≥ 58) con la corrección de continuidad.', f'≈ {R("1-0.9332", 4)}', 'Se usa 57,5: z = (57,5 − 50) ÷ 5 = 1,5 y se toma el complemento 1 − 0,9332.'),
        ('abc', 'Para aproximar P(X ≥ 58), ¿qué límite se usa en la normal?', '57,5', '58,5', '58', 'Para «al menos 58» el entero 58 ocupa desde 57,5, y por eso se parte de 57,5.'),
        ('{F} Aproxima P(X ≤ 47) con la corrección de continuidad.', f'≈ {R("1-0.6915", 4)}', 'z = (47,5 − 50) ÷ 5 = −0,5 y Φ(−0,5) = 1 − 0,6915.'),
        ('{F} Aproxima P(X ≤ 62) con la corrección de continuidad.', '≈ 0,9938', 'z = (62,5 − 50) ÷ 5 = 2,5 y la tabla da Φ(2,5) = 0,9938.'),
        ('abc', 'Con n = 30 y p = 0,05, ¿es adecuada la aproximación normal?', 'No: n·p = 1,5 es menor que 5 y la binomial es muy asimétrica', 'Sí: n = 30 es suficientemente grande', 'Sí: p pequeña siempre favorece la aproximación', 'Con n·p = 1,5 hay muy pocos éxitos esperados, así que la binomial no se parece a una campana.'),
        ('abc', 'El tiempo de espera, en minutos, de los clientes de una fila tiene un histograma simétrico en forma de campana. ¿Qué modelo conviene?', 'Normal, porque es una variable continua con forma de campana', 'Binomial, porque hay muchos clientes', 'Ninguno, porque no se puede modelar', 'La binomial cuenta éxitos; un tiempo continuo simétrico se modela con la normal, comprobando el histograma.'),
        ('abc', 'De un grupo de 12 estudiantes se cuenta cuántos usan bicicleta, con p = 0,3. ¿Qué modelo conviene?', 'Binomial B(12; 0,3), porque son pocos ensayos y n·p = 3,6 es menor que 5', 'Normal, porque 12 es mayor que 10', 'Ninguno de los dos', 'Con n·p = 3,6 no se cumple la condición para aproximar, así que se usa la binomial exacta.'),
        ('{F} Con la regla empírica, ¿entre qué valores está aproximadamente el 95 % del número de caras?', 'Entre 40 y 60 caras', 'El 95 % está a 2σ de la media: 50 ± 2 × 5 da 40 y 60.'),
    ],
    ctx=('abc', '{F} Una prueba de 100 preguntas de verdadero o falso se responde totalmente al azar y se aprueba con 63 aciertos o más. ¿Qué tan probable es aprobar solo por azar?', 'Muy poco probable: aproximadamente 0,6 %', 'Probable: cerca de 62 %', 'Imposible: la probabilidad es exactamente 0', 'P(X ≥ 63) ≈ 1 − Φ(2,5) = 0,0062, aproximadamente 0,6 %: poco probable, aunque no imposible.'),
    sc=[
        ("En Estadística: ¿qué condiciones permiten aproximar una binomial con una normal?", "n·p ≥ 5 y n·q ≥ 5", "Aseguran que haya suficientes éxitos y fracasos esperados."),
        ("¿Qué parámetros tiene la normal que reemplaza a la binomial?", "μ = n·p y σ = √(n·p·q)", "Son la media y la desviación estándar de la binomial."),
        ("¿Para qué sirve la corrección por continuidad?", "Para compensar que X toma valores enteros y la normal es continua", "Cada entero se representa por un intervalo de ancho 1."),
    ],
    op=("Elige uno de estos casos de ejemplo. Caso 1: en una encuesta de 36 personas elegidas al azar, cada una prefiere cierta bebida con p = 0,5; X ~ B(36; 0,5), con μ = 18 y σ = 3. Caso 2: en 100 lanzamientos de una moneda equilibrada, X ~ B(100; 0,5), con μ = 50 y σ = 5. Comprueba n·p y n·q, aproxima con la normal una probabilidad de «a lo más» y una de «al menos» (para el Caso 1 usa k = 16 y k = 23; para el Caso 2 usa k = 42 y k = 58) y escribe si el resultado es poco probable y qué dudarías del modelo.",
        "Caso 1: n·p = n·q = 18, se puede aproximar. P(X ≤ 16) ≈ Φ((16,5 − 18) ÷ 3) = Φ(−0,5) = 1 − 0,6915 = 0,3085; P(X ≥ 23) ≈ 1 − Φ((22,5 − 18) ÷ 3) = 1 − Φ(1,5) = 0,0668. Observar 23 o más es algo raro (cerca de 6,7 %) pero no baja del umbral de 5 %, así que no hay evidencia suficiente para dudar del modelo.",
        ["verifica las condiciones antes de aproximar", "usa la corrección por continuidad en el sentido correcto", "lee bien la tabla y usa complementos", "interpreta la probabilidad frente al umbral de 5 %"],
        ["hoja con las condiciones, las dos probabilidades aproximadas y la conclusión"],
        ["omitir la corrección por continuidad", "sumar 0,5 en vez de restarlo en «al menos»", "concluir con certeza a partir de una probabilidad pequeña"],
        "Pregunta: «¿por qué restaste (o sumaste) 0,5?». Si no lo explica, pide que dibuje el entero k como un intervalo de ancho 1."),
    reinforce="Aproxima P(X ≥ 53) para la ficha y compara con P(X ≤ 52) = 0,6915: ¿qué relación esperabas entre ambas?",
    extend="Explica por qué una binomial con n = 100 y p = 0,02 no se aproxima bien con una normal, y qué distribución de probabilidad (entre las que conoces) usarías en su lugar.",
)
