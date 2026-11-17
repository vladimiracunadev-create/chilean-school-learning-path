"""Probabilidades y estadística descriptiva e inferencial (electivo HC, 3.º y 4.º medio): OAC-02 (media muestral, varianza, desviación estándar, coeficiente de variación y correlación muestral), clases 1 a 4. Todo a mano; las calculadoras y hojas de cálculo se describen por escrito."""
from __future__ import annotations

from hc_pedi_common import R, build

O2 = "MA-PEDI-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (de ejemplo). Se escogió una muestra aleatoria de 6 estudiantes de un liceo de 1.200 estudiantes y se registró cuántos libros leyó cada uno en el año: 2, 5, 4, 9, 6 y 10. "
     "La media muestral se escribe x̄ y se calcula como la suma de los datos dividida por el número de datos n. La desviación de un dato respecto de la media es x − x̄.")
build(
    O2, 1, F,
    use="Aprenderé a calcular e interpretar la media muestral, a distinguir muestra de población y a reconocer cuándo la media representa bien a los datos.",
    prior=["Sé calcular promedios.", "Sé qué es la mediana.", "Sé calcular con números enteros y negativos."],
    explain=[
        "En Estadística, la población es el conjunto completo que se quiere estudiar (por ejemplo, los 1.200 estudiantes de un liceo) y la muestra es una parte de ella. Una muestra es aleatoria cuando cada integrante tuvo la misma posibilidad de ser elegido; eso permite usarla para estimar características de la población. Un valor calculado con la muestra se llama estadístico y uno de la población, parámetro.",
        "La media muestral x̄ es la suma de los n datos dividida por n. Es el estadístico que se usa para estimar la media de la población, que se escribe μ. Si los datos vienen en una tabla con frecuencias f, se calcula como la suma de (dato × f) dividida por n. La media tiene dos propiedades útiles: la suma de las desviaciones (x − x̄) siempre es 0, y se ve arrastrada por valores extremos.",
        "Distintas muestras de la misma población dan distintas medias muestrales, y eso es normal: se llama variabilidad muestral. Por eso x̄ es una estimación, no el valor exacto de μ. Antes de resumir con una media, revisa que los datos sean numéricos y que no haya valores extremos o errores; si los hay, informa también la mediana.",
    ],
    vocab=[("población", "conjunto completo de casos que se quiere estudiar"), ("muestra aleatoria", "parte de la población elegida al azar"), ("media muestral x̄", "suma de los datos dividida por el número de datos"), ("parámetro", "valor que describe a la población, como μ"), ("estadístico", "valor calculado con una muestra, como x̄"), ("desviación", "diferencia entre un dato y la media")],
    worked=[
        ("Calcular la media muestral", "Una muestra de ejemplo tiene los datos 12, 15, 9, 14 y 10. Calcula x̄.", ["Suma: 12 + 15 + 9 + 14 + 10 = 60.", "Divide por n = 5: 60 ÷ 5 = 12."], "x̄ = 12"),
        ("Hallar un dato que falta", "Cuatro datos de ejemplo tienen media 8 y tres de ellos son 5, 9 y 10. ¿Cuál es el cuarto?", ["La suma total debe ser 8 × 4 = 32.", "Los tres conocidos suman 5 + 9 + 10 = 24, así que falta 32 − 24 = 8."], "El cuarto dato es 8"),
    ],
    mistakes=[("Creer que x̄ es exactamente la media de toda la población.", "x̄ viene de una sola muestra y otra muestra daría otro valor.", "Dilo como estimación de μ y recuerda que tiene variabilidad muestral."),
              ("Calcular la media sin dividir por el número de datos, o dividir por un número distinto de n.", "Cada dato cuenta una vez y la división debe ser por la cantidad de datos.", "Cuenta los datos antes de dividir y comprueba que n coincide.")],
    T=[
        ('abc', '{F} ¿Cuál es la media muestral de los 6 datos?', '6 libros', '5,5 libros', '10 libros', 'La suma es 36 y 36 ÷ 6 = 6; 5,5 es la mediana y 10 es el máximo.'),
        ('ab', '¿Para qué se usa la media muestral x̄?', 'Para estimar la media de la población a partir de una muestra', 'Para calcular exactamente la media de la población', 'Como es un valor calculado con una parte de la población, solo la estima y no es exacta.'),
        ('=', 'La suma de 8 datos de una muestra es 120. ¿Cuál es la media muestral?', '120/8', 'La media es la suma dividida por el número de datos, que aquí es 8.', ''),
        ('abc', '{F} ¿Cuánto suman las desviaciones (x − x̄) de los seis datos?', '0', '6', '46', 'Las desviaciones positivas y negativas se compensan exactamente alrededor de la media.'),
        ('=', '{F} ¿Cuál es la desviación (x − x̄) del dato 10?', '10-6', 'Se resta la media 6 al dato 10.', ' libros'),
        ('abc', 'Una muestra aleatoria de 50 estudiantes se usa para estudiar a los 1.200 de un liceo. ¿Cuál es la población?', 'Los 1.200 estudiantes del liceo', 'Los 50 estudiantes de la muestra', 'La media de los 50 estudiantes', 'La población es el conjunto completo que se estudia, y la muestra es solo una parte.'),
        ('=', 'En una muestra de 20 hogares, 5 tienen 2 personas, 9 tienen 3 y 6 tienen 4. ¿Cuál es la media de personas por hogar?', '(5*2+9*3+6*4)/20', 'Se multiplica cada dato por su frecuencia, se suma y se divide por los 20 hogares.', ' personas'),
        ('=', 'La media de 5 datos es 14 y se agrega un sexto dato igual a 20. ¿Cuál es la nueva media?', '(14*5+20)/6', 'La suma original es 70; se agrega 20 y se divide por los 6 datos.', ''),
        ('ab', '{F} Otra muestra aleatoria de 6 estudiantes del mismo liceo da una media de 5,5 libros. ¿Qué significa?', 'Es normal: distintas muestras dan distintas medias muestrales', 'Una de las dos muestras fue mal calculada', 'La variabilidad muestral hace que cada muestra produzca una media algo distinta sin que haya error.'),
        ('abc', 'Los datos 4, 5, 6, 5 y 5 tienen media 5. Si el 6 se cambia por 26, ¿qué ocurre con la media?', 'Sube a 9: un dato extremo la arrastra', 'Se mantiene en 5, porque la mayoría de los datos es 5', 'Sube a 26, que es el nuevo mayor valor', 'La nueva suma es 45 y 45 ÷ 5 = 9; la media es sensible a los valores extremos.'),
        ('abc', 'La muestra P tiene 10 datos con media 8 y la muestra Q tiene 30 datos con media 12. ¿Cuál es la media de los 40 datos juntos?', '11', '10', '12', 'La suma total es 80 + 360 = 440 y 440 ÷ 40 = 11; el promedio simple de 8 y 12 ignora los tamaños.'),
        ('=', '{F} Se descubre que el dato 10 estaba mal registrado y era 4. ¿Cuál es la media corregida?', '(36-6)/6', 'La suma baja de 36 a 30 al corregir el dato, y se divide por los mismos 6 datos.', ' libros'),
        ('=', 'Cinco datos tienen media 7 y cuatro de ellos son 3, 9, 4 y 10. ¿Cuál es el quinto?', '7*5-(3+9+4+10)', 'La suma total es 35 y se le resta lo que suman los cuatro datos conocidos.', ''),
    ],
    ctx=('abc', 'Una pastelería registra las tortas vendidas en una muestra aleatoria de 5 días: 24, 30, 27, 33 y 26. ¿Qué afirmación es correcta?', 'La media muestral es 28 y estima las ventas medias de todos los días, con algo de error', '28 es exactamente la venta media de todos los días del año', '28 es la cantidad que se vendió con más frecuencia', 'La suma es 140 y 140 ÷ 5 = 28; es una estimación basada en una muestra, no un valor exacto.'),
    sc=[
        ("En Estadística: ¿qué es la media muestral x̄?", "La suma de los datos de la muestra dividida por n", "Es el estadístico que resume el centro de los datos de la muestra."),
        ("¿Cuánto suman siempre las desviaciones respecto de la media?", "Cero", "Las desviaciones positivas se compensan con las negativas."),
        ("¿Para qué sirve una muestra aleatoria?", "Para estimar características de la población sin medirla toda", "La elección al azar permite generalizar a la población."),
    ],
    op=("Elige uno de estos dos casos de ejemplo. Caso 1: minutos de traslado de una muestra aleatoria de 8 estudiantes: 15, 25, 20, 35, 10, 30, 20 y 25. Caso 2: litros de agua usados en 8 días elegidos al azar: 12, 18, 15, 21, 9, 15, 18 y 12. Calcula la media muestral, haz una tabla con las desviaciones y comprueba que suman 0. Escribe una frase que diferencie la muestra de la población y explica qué pasaría con la media si se agregara un dato muy extremo.",
        "Caso 2: la suma es 120 y x̄ = 120 ÷ 8 = 15 litros. Desviaciones: −3, 3, 0, 6, −6, 0, 3 y −3, que suman 0. La población son todos los días; la muestra son 8 días. Un día de 60 litros subiría la media a 20, así que informaría también la mediana.",
        ["media muestral calculada correctamente", "tabla de desviaciones con suma 0", "distingue muestra y población", "explica el efecto de un valor extremo"],
        ["hoja con el cálculo de x̄, la tabla de desviaciones y las dos explicaciones"],
        ["dividir por un número distinto de n", "decir que x̄ es la media exacta de la población", "dejar sin comprobar que las desviaciones suman 0"],
        "Pregunta: «¿qué parte de tu cálculo te asegura que no hay un error?». Orienta hacia la suma de las desviaciones igual a cero."),
    reinforce="Con los datos del Caso 1, calcula la mediana y compárala con la media: ¿cuál de las dos cambiaría más si el 35 fuera 85?",
    extend="Explica por qué, al hacer varias muestras aleatorias del mismo tamaño, esperas que sus medias se parezcan entre sí pero no sean idénticas.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (de ejemplo). Muestra de 5 personas: minutos que tardan en llegar al trabajo: 7, 7, 10, 13 y 13 (x̄ = 10 minutos). "
     "Varianza muestral: s² = Σ(x − x̄)² ÷ (n − 1). Desviación estándar muestral: s = √(s²). Fórmula equivalente: s² = (Σx² − n·x̄²) ÷ (n − 1). Para estos datos, Σx² = 536.")
build(
    O2, 2, F,
    use="Aprenderé a calcular e interpretar la varianza y la desviación estándar muestrales, con la tabla de desviaciones y con la fórmula equivalente.",
    prior=["Sé calcular la media muestral y las desviaciones.", "Sé calcular cuadrados y raíces cuadradas exactas simples.", "Sé qué significa dispersión."],
    explain=[
        "La media no dice cuán separados están los datos. Para medir esa dispersión se miran las desviaciones x − x̄. Como suman 0, se elevan al cuadrado antes de sumar: así todas quedan positivas y las desviaciones grandes pesan más. La varianza muestral s² es la suma de esos cuadrados dividida por n − 1; la desviación estándar s es su raíz cuadrada.",
        "Se divide por n − 1 y no por n porque la media muestral se calculó con los mismos datos, lo que hace que los datos queden un poco más cerca de x̄ que de la media real. Dividir por n tendería a quedar bajo la varianza de la población; n − 1 corrige ese sesgo. Las unidades importan: s² queda en unidades al cuadrado (minutos²) y s en las mismas unidades que los datos (minutos), por eso s es más fácil de interpretar.",
        "Interpreta s como una distancia típica de los datos a la media: si s es pequeña, los datos están cerca de x̄; si es grande, están dispersos; si todos los datos son iguales, s es 0. Hay dos formas de calcularla: la tabla de desviaciones (clara para entender) y la fórmula equivalente con Σx² (más corta con calculadora). Una calculadora científica o una hoja de cálculo entrega s con una tecla o función, pero aquí la calculas a mano para entender qué mide.",
    ],
    vocab=[("varianza muestral s²", "suma de las desviaciones al cuadrado dividida por n − 1"), ("desviación estándar s", "raíz cuadrada de la varianza; se mide en las unidades de los datos"), ("dispersión", "qué tan separados están los datos entre sí"), ("n − 1", "divisor que corrige la varianza cuando se estima con una muestra"), ("Σ", "símbolo de suma de todos los términos"), ("sesgo", "error sistemático de un estimador")],
    worked=[
        ("Varianza con la tabla de desviaciones", "Una muestra de ejemplo tiene los datos 2, 4 y 6. Calcula s² y s.", ["Media: 4. Desviaciones: −2, 0 y 2; cuadrados: 4, 0 y 4, que suman 8.", "Divide por n − 1 = 2: s² = 4, y la raíz da s = 2."], "s² = 4 y s = 2"),
        ("Desde la suma de cuadrados", "En una muestra de n = 5, la suma de los cuadrados de las desviaciones es 64. Calcula s² y s.", ["s² = 64 ÷ (5 − 1) = 16.", "s = √16 = 4."], "s² = 16 y s = 4"),
    ],
    mistakes=[("Dividir la suma de cuadrados por n en una muestra.", "Con la media muestral el divisor correcto para estimar la varianza de la población es n − 1.", "Usa n − 1 siempre que trabajes con una muestra."),
              ("Informar s² como si fuera la desviación estándar.", "s² está en unidades al cuadrado; falta la raíz cuadrada.", "Saca la raíz y escribe la unidad original.")],
    T=[
        ('abc', '{F} ¿Cuál es la desviación (x − x̄) del dato 13?', '3 minutos', '13 minutos', '10 minutos', 'Se resta la media 10 al dato 13; 13 es el dato y 10 es la media.'),
        ('=', '{F} ¿Cuánto suman los cuadrados de las desviaciones de los cinco datos?', '9+9+0+9+9', 'Las desviaciones son −3, −3, 0, 3 y 3, y sus cuadrados son 9, 9, 0, 9 y 9.', ' minutos²'),
        ('abc', '¿Por qué se elevan al cuadrado las desviaciones al calcular la varianza?', 'Porque suman 0 y se cancelarían; al cuadrado todas son positivas', 'Para que la varianza quede en las mismas unidades que los datos', 'Para que los datos más grandes pesen menos', 'Sin elevar al cuadrado, las desviaciones positivas y negativas se compensan y no medirían dispersión.'),
        ('=', '{F} Calcula la varianza muestral s² dividiendo la suma de cuadrados (36) por n − 1.', '36/4', 'Con n = 5 el divisor es 4, y 36 ÷ 4 da la varianza muestral.', ' minutos²'),
        ('{F} Con s² = 9 minutos², ¿cuánto vale la desviación estándar s?', '3 minutos', 'La desviación estándar es la raíz cuadrada de 9 y queda en las unidades de los datos.'),
        ('ab', 'Una persona divide la suma de cuadrados por n en vez de n − 1 al trabajar con una muestra. ¿Qué efecto tiene?', 'Tiende a subestimar la varianza de la población', 'Obtiene el mismo valor, porque n y n − 1 son casi iguales siempre', 'Dividir por n da un valor algo menor que dividir por n − 1, y por eso queda bajo la varianza de la población.'),
        ('=', 'Una muestra de 4 datos tiene suma de cuadrados de desviaciones igual a 48. ¿Cuál es su varianza muestral?', '48/3', 'Con n = 4 el divisor es 3, y 48 ÷ 3 da la varianza.', ''),
        ('Una muestra tiene s² = 2,25 unidades². ¿Cuánto vale s?', '1,5 unidades', 'La raíz cuadrada de 2,25 es 1,5, porque 1,5 × 1,5 = 2,25.'),
        ('=', 'Una muestra tiene los datos 2, 6 y 10, cuya media es 6. ¿Cuál es su varianza muestral?', '(16+0+16)/2', 'Las desviaciones son −4, 0 y 4; sus cuadrados suman 32 y se divide por n − 1 = 2.', ''),
        ('abc', 'Dos muestras de notas tienen media 5,0. La muestra X tiene s = 0,3 y la muestra Y tiene s = 1,2. ¿Qué se concluye?', 'En X las notas están más cerca de la media; en Y están más dispersas', 'En Y las notas son mejores porque s es mayor', 'En X las notas son más altas porque s es menor', 'Con la misma media, una s menor significa datos más agrupados en torno a ella.'),
        ('ab', 'A todos los datos de una muestra se les suma 5 unidades. ¿Qué ocurre con s?', 'No cambia, porque las distancias entre los datos se mantienen', 'Aumenta en 5 unidades', 'Sumar lo mismo a todos corre la media pero no cambia las desviaciones, así que s queda igual.'),
        ('=', '{F} Comprueba con la fórmula equivalente: calcula (Σx² − n·x̄²) ÷ (n − 1) con Σx² = 536, n = 5 y x̄ = 10.', '(536-5*10*10)/(5-1)', 'Se resta n·x̄² = 500 a 536 y el resultado, 36, se divide por 4.', ' minutos²'),
        ('abc', '{F} Los tiempos de la ficha se pasan de minutos a segundos (cada dato se multiplica por 60). ¿Qué ocurre con s?', 'Se multiplica por 60: pasa de 3 minutos a 180 segundos', 'Se multiplica por 3.600', 'No cambia, porque la dispersión es la misma', 'Un cambio de unidades multiplica las distancias por 60; el factor 3.600 corresponde a la varianza.'),
    ],
    ctx=('abc', 'Dos máquinas llenan botellas de 500 mL. En muestras de 5 botellas, la máquina 1 llenó 498, 499, 500, 501 y 502 mL, y la máquina 2 llenó 490, 495, 500, 505 y 510 mL. ¿Cuál es más regular?', 'La máquina 1: s ≈ 1,6 mL frente a s ≈ 7,9 mL', 'La máquina 2, porque sus valores abarcan un rango más amplio', 'Las dos por igual, porque ambas tienen media 500 mL', 'Con igual media, la máquina 1 tiene s ≈ 1,6 y la 2 tiene s ≈ 7,9; la media no mide regularidad.'),
    sc=[
        ("En Estadística: ¿por qué se divide por n − 1 en la varianza muestral?", "Para no subestimar la varianza de la población al estimarla con una muestra", "Con la media muestral los datos quedan algo más cerca de x̄ que de μ."),
        ("¿En qué unidades queda la desviación estándar?", "En las mismas unidades que los datos", "La raíz cuadrada deshace el cuadrado de las unidades."),
        ("¿Cuánto vale s si todos los datos son iguales?", "Cero", "Si no hay desviaciones, no hay dispersión."),
    ],
    op=("Elige uno de estos dos casos de ejemplo. Caso 1: puntajes de una muestra de 5 estudiantes: 40, 40, 50, 60 y 60. Caso 2: mensajes recibidos en 5 días: 2, 2, 8, 14 y 14. Haz la tabla de desviaciones, calcula s² y s, interpreta s con una frase y comprueba con la fórmula equivalente. Luego explica qué pasa con s si a todos los datos se les suma 10.",
        "Caso 2: x̄ = 8; desviaciones −6, −6, 0, 6, 6; cuadrados suman 144; s² = 144 ÷ 4 = 36 y s = 6 mensajes. Los días se alejan en promedio unos 6 mensajes de la media. Con la fórmula: Σx² = 4 + 4 + 64 + 196 + 196 = 464; (464 − 5 · 64) ÷ 4 = 36. Sumar 10 a todos no cambia s.",
        ["tabla de desviaciones correcta", "división por n − 1", "raíz cuadrada y unidad correctas", "comprobación con la fórmula equivalente y efecto de sumar 10"],
        ["hoja con la tabla, el cálculo de s² y s, la comprobación y la explicación"],
        ["dividir por n", "olvidar la raíz cuadrada", "afirmar que s cambia al sumar una constante"],
        "Pregunta: «¿qué mide s en una frase?». Si dice «cuánto varía todo», pide que lo exprese como distancia típica a la media."),
    reinforce="Calcula s para los datos 3, 5 y 7 con la tabla de desviaciones y luego para 6, 10 y 14; compara y explica qué relación ves entre los dos resultados.",
    extend="Explica con un ejemplo por qué dos muestras con la misma media pueden tener desviaciones estándar muy distintas y cuál conviene elegir si necesitas resultados parejos.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (de ejemplo). Ventas diarias de dos kioscos, resumidas con una muestra de cada uno. Kiosco A: media x̄ = 80 unidades y s = 12 unidades. Kiosco B: media x̄ = 250 unidades y s = 25 unidades. "
     "El coeficiente de variación es CV = (s ÷ x̄) × 100 %: la desviación estándar como porcentaje de la media.")
build(
    O2, 3, F,
    use="Aprenderé a calcular e interpretar el coeficiente de variación para comparar la variabilidad de grupos o variables que tienen medias o unidades distintas.",
    prior=["Sé calcular la media y la desviación estándar muestrales.", "Sé calcular porcentajes.", "Sé qué significa dispersión."],
    explain=[
        "La desviación estándar s depende de la unidad y del tamaño de los valores: una s de 25 unidades puede ser mucho en un grupo con media 50 y poco en uno con media 5.000. Para comparar la variabilidad de grupos distintos se usa el coeficiente de variación, CV = (s ÷ x̄) × 100 %. Expresa cuánto varían los datos en relación con su media y no tiene unidades.",
        "Con el CV puedes comparar incluso variables con unidades diferentes, como un tiempo en minutos y un gasto en pesos. Un CV menor significa datos relativamente más parejos. No existe un umbral universal: un CV de 10 % puede ser alto o bajo según lo que se mide, así que se interpreta siempre en su contexto. El CV solo tiene sentido cuando la media es positiva y no está cerca de 0, como en tiempos, precios o masas, pero no en temperaturas en grados Celsius.",
        "Hay propiedades que ayudan a razonar. Si multiplicas todos los datos por una constante positiva (por ejemplo, al pasar de metros a centímetros), la media y s se multiplican por esa constante, y el CV no cambia. Si sumas una constante a todos los datos, s no cambia pero la media sí, y por eso el CV cambia.",
    ],
    vocab=[("coeficiente de variación (CV)", "desviación estándar dividida por la media, en porcentaje"), ("variabilidad relativa", "dispersión medida en proporción a la media"), ("homogéneo", "con datos parecidos entre sí"), ("escala", "tamaño típico de los valores de una variable"), ("constante", "número fijo que no depende del dato"), ("unidad de medida", "patrón con que se expresa una variable, como minutos o gramos")],
    worked=[
        ("Calcular un CV", "Una muestra de ejemplo tiene x̄ = 40 y s = 6. ¿Cuál es el CV?", ["Divide s por la media: 6 ÷ 40 = 0,15.", "Exprésalo en porcentaje: 0,15 × 100 = 15 %."], "CV = 15 %"),
        ("Comparar variables distintas", "Paquetes de ejemplo: el peso tiene x̄ = 200 g y s = 10 g; el precio tiene x̄ = 1.000 pesos y s = 80 pesos. ¿Qué varía más en proporción?", ["CV del peso: 10 ÷ 200 × 100 = 5 %.", "CV del precio: 80 ÷ 1.000 × 100 = 8 %."], "El precio varía más en proporción (8 % frente a 5 %)"),
    ],
    mistakes=[("Comparar directamente las desviaciones estándar de variables con distinta unidad o escala.", "Una s mayor puede corresponder a una media mucho mayor y a menor variabilidad relativa.", "Calcula y compara los CV."),
              ("Entregar el cociente s ÷ x̄ sin multiplicar por 100 y sin indicar que es un porcentaje.", "Sin la conversión el valor 0,15 se confunde con otra cantidad.", "Escribe el CV como porcentaje.")],
    T=[
        ('abc', '{F} ¿Cuál es el CV del kiosco A?', '15 %', '12 %', '0,15 %', 'Se calcula 12 ÷ 80 = 0,15 y se multiplica por 100; 12 % copia el valor de s.'),
        ('=', '{F} Calcula el CV del kiosco B en porcentaje.', '25*100/250', 'Se divide s = 25 por la media 250 y se multiplica por 100.', ' %'),
        ('ab', '¿En qué unidades queda el coeficiente de variación?', 'No tiene unidades; se expresa como porcentaje', 'En las mismas unidades que los datos', 'Al dividir s por la media, las unidades se cancelan, así que el CV es un número puro.'),
        ('abc', '{F} ¿Qué kiosco tiene mayor variabilidad relativa a su media?', 'El kiosco A, con CV de 15 % frente a 10 %', 'El kiosco B, porque su s de 25 es mayor que 12', 'Ninguno: la variabilidad solo se compara con la desviación estándar', 'La variabilidad relativa se compara con el CV, que es mayor en el kiosco A.'),
        ('=', 'Una muestra de masas tiene media 50 kg y s = 4 kg. ¿Cuál es el CV?', '4*100/50', 'Se divide 4 por 50 y se expresa en porcentaje.', ' %'),
        ('abc', '¿Para qué sirve el CV?', 'Para comparar la variabilidad de grupos con medias o unidades distintas', 'Para calcular la media de la población', 'Para saber si hay valores atípicos', 'Al medir la dispersión en proporción a la media, el CV permite comparar grupos de distinta escala.'),
        ('=', 'Una variable tiene CV de 20 % y media 60. ¿Cuánto vale su desviación estándar s?', '60*20/100', 'Si CV = s ÷ x̄ × 100, entonces s es el 20 % de la media.', ''),
        ('abc', 'Los árboles de una muestra miden en promedio 8 m con s = 2 m, y sus edades promedian 25 años con s = 5 años. ¿Qué varía más en proporción?', 'Las alturas, con CV de 25 % frente a 20 %', 'Las edades, porque 5 es mayor que 2', 'Igual en ambas, porque las dos tienen unidades', 'El CV de las alturas es 25 % y el de las edades es 20 %, y la comparación debe hacerse con el CV.'),
        ('ab', 'Todos los datos de una muestra se multiplican por 10, por ejemplo al pasar de centímetros a milímetros. ¿Qué ocurre con el CV?', 'No cambia, porque la media y s se multiplican por 10', 'Se multiplica por 10', 'En el cociente s ÷ x̄ el factor 10 aparece arriba y abajo, y se cancela.'),
        ('abc', 'A todos los datos positivos de una muestra se les suma 100. ¿Qué ocurre con s y con el CV?', 's no cambia y el CV disminuye', 's y el CV no cambian', 's aumenta y el CV no cambia', 'La s se mantiene, pero la media crece y entonces el cociente s ÷ x̄ es menor.'),
        ('abc', 'Para elegir la máquina con paquetes que varíen menos en proporción, se miden muestras: la máquina P tiene media 500 g y s = 15 g, y la Q tiene media 250 g y s = 10 g. ¿Cuál conviene?', 'La máquina P, con CV de 3 %', 'La máquina Q, porque su s de 10 es menor', 'Da lo mismo, porque sus unidades son iguales', 'El CV de P es 3 % y el de Q es 4 %, así que P es relativamente más regular aunque su s sea mayor.'),
        ('=', 'En otra temporada, el kiosco A de la ficha tiene media 100 unidades, pero conserva s = 12 unidades. ¿Cuál es su CV en esa temporada?', '12*100/100', 'Con la media 100, la desviación 12 es el 12 % de la media; antes era 15 % con media 80.', ' %'),
        ('abc', 'La temperatura de una ciudad en grados Celsius tiene media cercana a 0. ¿Por qué no es adecuado calcular su CV?', 'Porque dividir por una media cercana a 0 hace que el CV sea enorme y sin sentido relativo', 'Porque la temperatura no tiene desviación estándar', 'Porque el CV solo se puede usar con porcentajes', 'El CV compara con la media; si esta es casi 0, el cociente pierde significado.'),
    ],
    ctx=('abc', 'En una muestra de estudiantes, el tiempo de traslado tiene media 30 min y s = 6 min, y el gasto semanal en pasajes tiene media 8.000 pesos y s = 1.200 pesos. ¿Qué variable es relativamente más variable?', 'El tiempo de traslado, con CV de 20 % frente a 15 %', 'El gasto, porque 1.200 es mayor que 6', 'No se pueden comparar, porque tienen unidades distintas', 'Los CV son 20 % y 15 %, y como no tienen unidades se pueden comparar aunque las variables sean distintas.'),
    sc=[
        ("En Estadística: ¿cómo se calcula el coeficiente de variación?", "Desviación estándar dividida por la media, multiplicada por 100", "Mide la dispersión en proporción a la media."),
        ("¿Por qué no basta comparar s entre variables de distinta unidad?", "Porque s depende de la unidad y de la escala de cada variable", "El mismo dato en otra unidad cambia el valor de s."),
        ("¿Qué pasa con el CV si todos los datos se multiplican por una constante positiva?", "No cambia", "La media y s se multiplican por el mismo número."),
    ],
    op=("Elige uno de estos casos de ejemplo. Caso 1: dos empresas de transporte, con tiempos de viaje: empresa A con media 40 min y s = 6 min; empresa B con media 90 min y s = 10 min. Caso 2: dos cursos, con puntajes: curso C con media 60 y s = 9; curso D con media 75 y s = 9. Calcula el CV de cada grupo, decide cuál es relativamente más variable y escribe una recomendación citando las cifras. Explica también qué ocurriría con el CV de C si todos sus puntajes subieran 10 puntos.",
        "Caso 2: CV de C = 9 ÷ 60 × 100 = 15 %; CV de D = 9 ÷ 75 × 100 = 12 %. Aunque s es igual en ambos, C es relativamente más variable. Si C sube 10 puntos, la media es 70, s sigue en 9 y el CV baja a casi 12,9 %.",
        ["CV calculado en porcentaje para ambos grupos", "comparación basada en el CV y no solo en s", "recomendación con cifras", "efecto de sumar una constante bien explicado"],
        ["hoja con los dos CV, la recomendación y la explicación del efecto de la constante"],
        ["comparar solo las desviaciones estándar", "olvidar multiplicar por 100", "decir que el CV no cambia al sumar una constante"],
        "Pregunta: «¿por qué comparas CV y no s?». Si no responde, pide un ejemplo con dos grupos de medias muy distintas."),
    reinforce="Con el kiosco A de la ficha, calcula el CV si sus ventas se expresaran en decenas de unidades (media 8 y s = 1,2) y verifica que da lo mismo.",
    extend="Busca una situación (en tu liceo o tu casa) en que compararías la variabilidad de dos variables con distinta unidad, y explica por qué el CV sería una buena herramienta.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (de ejemplo). Cinco estudiantes: x = horas de estudio semanales (1, 2, 3, 4 y 5) e y = puntaje en una prueba (6, 10, 8, 12 y 14). Las medias son x̄ = 3 e ȳ = 10. "
     "Correlación muestral: r = Sxy ÷ √(Sxx · Syy), donde Sxy = Σ(x − x̄)(y − ȳ), Sxx = Σ(x − x̄)² y Syy = Σ(y − ȳ)². Para estos datos, Syy = 40.")
build(
    O2, 4, F,
    use="Aprenderé a calcular e interpretar el coeficiente de correlación muestral r entre dos variables, y a no confundirlo con causalidad ni con pendiente.",
    prior=["Sé leer una nube de puntos.", "Sé calcular medias y desviaciones.", "Sé multiplicar números negativos y calcular raíces simples."],
    explain=[
        "El coeficiente de correlación muestral r mide la fuerza y la dirección de la relación lineal entre dos variables. Se calcula con las desviaciones de cada variable: se multiplica cada par (x − x̄)(y − ȳ), se suman esos productos (Sxy) y se divide por la raíz del producto de Sxx y Syy. Una calculadora científica o una hoja de cálculo tiene una función para r, pero con pocos datos conviene calcularlo a mano para entender qué hace.",
        "El valor de r está siempre entre −1 y 1. El signo es la dirección: positivo si y tiende a subir cuando x sube, y negativo si tiende a bajar. El tamaño indica la fuerza: cerca de 1 o de −1 significa que los puntos están casi sobre una recta; cerca de 0, que no hay relación lineal. Como referencia orientativa, menos de 0,3 es débil, de 0,3 a 0,7 es moderada y más de 0,7 es fuerte. r no tiene unidades y no cambia si cambias las unidades de x o de y.",
        "Hay tres cuidados. Primero, r = 0 solo dice que no hay relación lineal; puede haber una relación curva, como una U. Segundo, r no es la pendiente ni un porcentaje de casos: r = 0,9 no significa que y suba 0,9 por cada unidad de x. Tercero, correlación no es causalidad: una tercera variable puede explicar ambas, y un solo punto muy alejado puede cambiar mucho el valor de r.",
    ],
    vocab=[("correlación muestral r", "número entre −1 y 1 que mide la relación lineal entre dos variables"), ("Sxy", "suma de los productos de las desviaciones de x y de y"), ("relación lineal", "relación en que los puntos siguen aproximadamente una recta"), ("fuerza", "qué tan cerca están los puntos de la recta"), ("dirección", "signo de la relación: positiva o negativa"), ("correlación no es causalidad", "que dos variables se asocien no prueba que una cause la otra")],
    worked=[
        ("Calcular r", "En una muestra de ejemplo, Sxy = −21, Sxx = 25 y Syy = 36. Calcula r.", ["Producto: Sxx · Syy = 25 · 36 = 900, y su raíz es 30.", "Divide: r = −21 ÷ 30 = −0,7."], "r = −0,7: relación lineal negativa y fuerte"),
        ("Interpretar un r cercano a 0", "Entre la talla de calzado y el puntaje en una prueba de una muestra de ejemplo, r = 0,05. ¿Qué se concluye?", ["El valor está muy cerca de 0, así que no hay relación lineal apreciable.", "No se puede afirmar nada sobre causas, ni descartar otras formas de relación."], "Casi no hay relación lineal entre ambas variables"),
    ],
    mistakes=[("Concluir que r = 0 significa que no existe ninguna relación entre las variables.", "r solo mide relación lineal; puede haber una relación curva.", "Mira siempre la nube de puntos además de r."),
              ("Interpretar r = 0,9 como «el 90 % de los casos sube» o «y sube 0,9 por cada unidad de x».", "r mide fuerza y dirección de la relación lineal, no un porcentaje de casos ni una pendiente.", "Dilo como «relación lineal positiva y fuerte».")],
    T=[
        ('=', '{F} ¿Cuál es la desviación (y − ȳ) del estudiante que obtuvo 6 puntos?', '6-10', 'Se resta la media ȳ = 10 al puntaje 6; el resultado es negativo porque queda bajo la media.', ' puntos'),
        ('=', '{F} Calcula Sxx sumando los cuadrados de las desviaciones de x: −2, −1, 0, 1 y 2.', '4+1+0+1+4', 'Cada desviación se eleva al cuadrado: 4, 1, 0, 1 y 4.', ''),
        ('abc', '¿Entre qué valores se mueve siempre r?', 'Entre −1 y 1', 'Entre 0 y 1', 'Entre −100 y 100', 'La correlación es un número sin unidades que nunca sale del intervalo de −1 a 1.'),
        ('=', '{F} Calcula Sxy con las desviaciones de x (−2, −1, 0, 1, 2) y de y (−4, 0, −2, 2, 4).', '(-2)*(-4)+(-1)*0+0*(-2)+1*2+2*4', 'Se multiplica cada par de desviaciones y se suman los cinco productos: 8, 0, 0, 2 y 8.', ''),
        ('=', '{F} Calcula r sabiendo que Sxy = 18 y que la raíz de Sxx · Syy es 20.', '18/20', 'Se divide Sxy entre la raíz del producto de Sxx y Syy.', ''),
        ('abc', '{F} ¿Cómo se interpreta r = 0,9?', 'Relación lineal positiva y fuerte', 'El 90 % de los estudiantes mejora al estudiar más', 'Una hora más de estudio produce 0,9 puntos más', 'r mide la fuerza y la dirección de la relación lineal, no un porcentaje de casos ni una pendiente.'),
        ('ab', 'Si r = −0,7, ¿qué indica?', 'Al aumentar x tiende a disminuir y, con una relación lineal bastante fuerte', 'Hay un error de medición, porque r no puede ser negativo', 'El signo negativo indica dirección descendente, y 0,7 es una fuerza alta.'),
        ('abc', 'Una nube de puntos tiene forma de U y r ≈ 0. ¿Qué se concluye?', 'No hay relación lineal, pero puede haber otra relación, de tipo curvo', 'No hay ninguna relación entre las variables', 'Hay una relación lineal negativa', 'r detecta solo relaciones lineales; una U tiene r cercano a 0 aunque haya relación.'),
        ('=', 'Una muestra tiene Sxy = −27, Sxx = 20 y Syy = 45, de modo que la raíz de Sxx · Syy es 30. ¿Cuánto vale r?', '-27/30', 'Se divide −27 entre 30, lo que da una relación negativa y fuerte.', ''),
        ('abc', 'Las horas de estudio se expresan ahora en minutos (cada x se multiplica por 60). ¿Qué ocurre con r?', 'No cambia', 'Se multiplica por 60', 'Cambia de signo', 'La correlación no depende de las unidades, porque el cambio de escala se cancela en el cociente.'),
        ('abc', 'Entre las pizzas y las bebidas vendidas cada día en un local, r = 0,95. ¿Qué afirmación es correcta?', 'Se asocian fuertemente, pero no se prueba que una cause la otra: ambas dependen de la cantidad de clientes', 'Vender pizzas hace que se vendan bebidas, porque r es casi 1', 'Cada pizza vendida produce 0,95 bebidas más', 'La asociación es fuerte, pero una tercera variable, la cantidad de clientes, puede explicar ambas.'),
        ('abc', '{F} Se agrega un sexto estudiante con x = 5 e y = 0. ¿Qué efecto probable tiene sobre r?', 'Disminuye bastante, porque el punto se aleja mucho de la tendencia', 'No cambia, porque x = 5 ya estaba en los datos', 'Aumenta hacia 1', 'Un punto con x alto y puntaje 0 contradice la tendencia, y puede bajar r de manera considerable.'),
        ('Dos nubes tienen r = 0,9 y r = −0,9. ¿Qué tienen en común y qué las distingue?', 'La misma fuerza; en una y sube y en la otra baja', 'El tamaño 0,9 indica igual fuerza, y el signo indica la dirección de la relación.'),
    ],
    ctx=('abc', '{F} Un docente dice: «con r = 0,9, cada hora más de estudio sube exactamente 0,9 puntos». ¿Qué respuesta es correcta?', 'No: r mide la fuerza y la dirección, no cuánto sube y por cada unidad de x', 'Sí: r = 0,9 es la pendiente de la recta', 'Sí, pero solo si los puntajes están en porcentaje', 'La pendiente se calcula aparte (aquí Sxy ÷ Sxx = 1,8); r es otra cosa.'),
    sc=[
        ("En Estadística: ¿qué indica el signo de r?", "La dirección de la relación: positiva si y sube con x y negativa si baja", "El signo muestra si las variables cambian en el mismo sentido o en sentido contrario."),
        ("¿Entre qué valores está r?", "Entre −1 y 1", "Es un coeficiente sin unidades y acotado por esos extremos."),
        ("Si r = 0, ¿significa que no hay ninguna relación entre las variables?", "No, solo que no hay relación lineal", "Puede existir una relación curva que r no detecta."),
    ],
    op=("Elige uno de estos casos de ejemplo. Caso 1: x = 2, 4, 6, 8, 10 (minutos de calentamiento) e y = 7, 8, 6, 4, 5 (errores en un ejercicio). Caso 2: x = 10, 20, 30, 40, 50 (minutos de práctica) e y = 4, 3, 5, 7, 6 (puntos en un juego). Calcula x̄ e ȳ, las desviaciones, Sxx, Syy, Sxy y r. Interpreta el signo y la fuerza, y escribe una advertencia sobre causalidad.",
        "Caso 1: x̄ = 6, ȳ = 6; desviaciones de x: −4, −2, 0, 2, 4; de y: 1, 2, 0, −2, −1. Sxx = 40, Syy = 10, Sxy = −4 − 4 + 0 − 4 − 4 = −16 y r = −16 ÷ √400 = −0,8. Relación lineal negativa y fuerte: a más calentamiento, tienden a bajar los errores. Advertencia: no se prueba que el calentamiento cause menos errores.",
        ["desviaciones y sumas calculadas correctamente", "r calculado con la fórmula", "interpretación de signo y fuerza", "advertencia de que correlación no es causalidad"],
        ["hoja con la tabla de desviaciones, el cálculo de r y las dos interpretaciones"],
        ["olvidar el signo de algún producto", "confundir r con la pendiente", "afirmar causalidad a partir de r"],
        "Pregunta: «¿qué dice el signo de r y qué dice su tamaño?». Si mezcla ambos, pide que los explique por separado."),
    reinforce="Con los datos de la ficha, invierte el orden de y (14, 12, 8, 10, 6) y calcula cómo cambia r; explica por qué cambia el signo y no el tamaño.",
    extend="Dibuja una nube de 6 puntos con r cercano a 0 que tenga una relación curva clara, y explica por qué r no la detecta.",
)
