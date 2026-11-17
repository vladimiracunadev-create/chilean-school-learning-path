"""Probabilidades y estadística descriptiva e inferencial (electivo HC, 3.º y 4.º medio): OAC-04 (inferencias sobre la media y la varianza bajo normalidad: intervalos de confianza y pruebas de hipótesis), clases 1 a 5. Todo a mano, con tablas escritas en la ficha."""
from __future__ import annotations

from hc_pedi_common import R, build

O4 = "MA-PEDI-3y4-OAC-04"

TABLA_Z = ("Tabla de la normal estándar (de ejemplo): Φ(0,5) = 0,6915; Φ(1,0) = 0,8413; Φ(1,5) = 0,9332; Φ(2,0) = 0,9772; Φ(2,5) = 0,9938; para z negativo, Φ(−z) = 1 − Φ(z).")

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (de ejemplo). La duración de un tipo de pieza, en horas, se supone normal con media μ desconocida y desviación estándar conocida σ = 12 horas. Se toma una muestra aleatoria de n = 36 piezas y se obtiene x̄ = 200 horas. "
     "Si X ~ N(μ; σ), entonces la media muestral x̄ tiene distribución normal con media μ y desviación estándar σ ÷ √n, llamada error estándar. " + TABLA_Z)
build(
    O4, 1, F,
    use="Aprenderé a distinguir parámetro de estadístico, a identificar los supuestos de una inferencia y a calcular y usar el error estándar de la media muestral.",
    prior=["Sé calcular la media y la desviación estándar de una muestra.", "Sé estandarizar y usar la tabla de la normal.", "Sé qué es una muestra aleatoria."],
    explain=[
        "Inferir es usar los datos de una muestra para sacar conclusiones sobre la población, aceptando que hay incertidumbre. El valor que describe a la población (como la media μ o la varianza σ²) es un parámetro y casi siempre es desconocido. El valor calculado con la muestra (como x̄ o s²) es un estadístico y sirve como estimación. Cada muestra aleatoria distinta da un estadístico distinto, por lo que x̄ tiene su propia distribución.",
        "Si la variable es normal con parámetros μ y σ, la media muestral de n datos independientes también es normal, con media μ y desviación estándar σ ÷ √n. Esa desviación se llama error estándar y mide cuánto varían las medias muestrales de un mismo tamaño. Como n está en el denominador dentro de una raíz, para reducir el error estándar a la mitad hay que cuadruplicar el tamaño de la muestra.",
        "Toda inferencia descansa en supuestos que hay que declarar: la muestra es aleatoria (cada integrante tuvo la misma posibilidad), los datos son independientes y la variable se distribuye de forma normal (se revisa, por ejemplo, con un histograma en forma de campana). Una muestra grande, pero escogida por conveniencia, no arregla un sesgo de selección: la aleatoriedad importa más que el tamaño.",
    ],
    vocab=[("parámetro", "valor que describe a la población, como μ"), ("estadístico", "valor calculado con la muestra, como x̄"), ("error estándar", "desviación estándar de la media muestral, σ ÷ √n"), ("muestra aleatoria", "muestra elegida al azar, donde todos tienen la misma posibilidad"), ("supuesto de normalidad", "condición de que la variable tiene distribución normal"), ("estimación", "valor de un estadístico usado para aproximar un parámetro")],
    worked=[
        ("Error estándar", "Una variable normal de ejemplo tiene σ = 20 y se toma una muestra de n = 25. ¿Cuál es el error estándar de x̄?", ["Calcula √n: √25 = 5.", "Divide: σ ÷ √n = 20 ÷ 5 = 4."], "Error estándar = 4"),
        ("Probabilidad para una media muestral", "X ~ N(50; 10) y n = 25. Calcula P(x̄ > 53).", ["Error estándar: 10 ÷ 5 = 2. Luego z = (53 − 50) ÷ 2 = 1,5.", "P(x̄ > 53) = 1 − Φ(1,5) = 1 − 0,9332 = 0,0668."], "P(x̄ > 53) = 0,0668"),
    ],
    mistakes=[("Usar σ en lugar de σ ÷ √n al estandarizar una media muestral.", "La media muestral varía menos que un dato individual.", "Calcula primero el error estándar y úsalo como denominador de z."),
              ("Creer que una muestra más grande siempre es mejor, aunque se haya elegido sin azar.", "El tamaño no corrige un sesgo de selección.", "Verifica primero que la muestra sea aleatoria.")],
    T=[
        ('abc', '{F} ¿Cuál es el error estándar de la media?', '2 horas', '12 horas', '6 horas', 'Es σ ÷ √n = 12 ÷ 6 = 2; 12 es solo σ y 6 es la raíz de n.'),
        ('ab', 'En Estadística, ¿qué es un parámetro?', 'Un valor que describe a la población, como μ, generalmente desconocido', 'Un valor calculado con los datos de la muestra', 'El parámetro describe a toda la población, mientras que lo calculado con la muestra se llama estadístico.'),
        ('=', 'Una variable normal tiene σ = 15 y se toma una muestra de n = 25. ¿Cuál es el error estándar de la media?', '15/5', 'La raíz cuadrada de 25 es 5, y el error estándar es 15 dividido por 5.', ' unidades'),
        ('abc', '¿Qué ocurre con el error estándar si se cuadruplica el tamaño de la muestra?', 'Se reduce a la mitad', 'Se reduce a la cuarta parte', 'No cambia', 'Como n está dentro de una raíz, multiplicar n por 4 divide el error estándar por 2.'),
        ('abc', '{F} ¿Qué supuestos permiten usar el modelo normal para x̄ con media μ y desviación σ ÷ √n?', 'Muestra aleatoria con datos independientes y variable normal', 'Que la muestra sea lo más grande posible', 'Que μ sea conocida', 'El modelo exige muestra aleatoria, independencia y normalidad; no es necesario conocer μ, que es lo que se quiere estimar.'),
        ('{F} Si la media real fuera μ = 198, ¿cuál es la probabilidad de que x̄ sea mayor que 200?', R("1-0.8413", 4), 'El error estándar es 2, z = (200 − 198) ÷ 2 = 1 y la cola derecha es 1 − Φ(1).'),
        ('Una variable es N(70; 8) y n = 16. Calcula P(x̄ ≥ 66).', '0,9772', 'El error estándar es 8 ÷ 4 = 2; z = (66 − 70) ÷ 2 = −2 y P(x̄ ≥ 66) = Φ(2).'),
        ('abc', 'Dos muestras aleatorias de la misma población dan x̄ = 198 y x̄ = 203. ¿Qué se concluye?', 'Es normal: x̄ varía de muestra en muestra alrededor de μ', 'Una de las dos muestras fue mal calculada', 'μ es exactamente el promedio de 198 y 203', 'Cada muestra produce una estimación distinta y esa variación es esperable.'),
        ('=', 'Si σ = 24, ¿qué tamaño de muestra se necesita para que el error estándar sea 3?', '(24/3)*(24/3)', 'De σ ÷ √n = 3 se despeja √n = 8, y n es 8 elevado al cuadrado.', ' datos'),
        ('abc', 'Un grupo encuesta a 400 personas, pero solo a amistades y familiares, para estimar la opinión de toda una ciudad. ¿Qué problema tiene?', 'La muestra no es aleatoria: el tamaño no corrige el sesgo de selección', 'La muestra es demasiado pequeña para cualquier ciudad', 'Las amistades no tienen opinión que se pueda medir', 'El problema es cómo se eligió la muestra, y no cuántas personas hay en ella.'),
        ('ab', '{F} Alguien dice: «como x̄ = 200, la media real de las piezas es exactamente 200 horas». ¿Es correcto?', 'No: x̄ solo estima μ y otra muestra daría otro valor', 'Sí: el estadístico es igual al parámetro', 'Una muestra solo entrega una estimación, que varía de una muestra a otra.'),
        ('=', 'Si σ = 12 y se quiere un error estándar de 1,5, ¿qué n se necesita?', '(12/1.5)*(12/1.5)', 'De 12 ÷ √n = 1,5 se obtiene √n = 8, y n = 64.', ' datos'),
        ('{F} Si la media real fuera μ = 200, ¿cuál es la probabilidad de que x̄ difiera de μ en más de 4 horas, hacia cualquier lado?', R("2*(1-0.9772)", 4), 'Con error estándar 2, la diferencia de 4 horas es z = 2, y se suman las dos colas: 2 × (1 − 0,9772).'),
    ],
    ctx=('abc', 'En una muestra aleatoria de 49 estudiantes de un liceo se mide el tiempo de estudio semanal: x̄ = 8 horas, con σ = 3,5 horas supuesta conocida. ¿Cuál es el error estándar y qué significa?', '0,5 horas: la desviación típica de las medias muestrales de 49 estudiantes', '3,5 horas: la dispersión de la media muestral', '7 horas: la raíz del tamaño de la muestra', 'Es 3,5 ÷ 7 = 0,5 horas; la dispersión de los datos individuales es σ, y la de las medias muestrales es menor.'),
    sc=[
        ("En Estadística: ¿cuál es la desviación estándar de la media muestral (error estándar)?", "σ ÷ √n", "Disminuye al aumentar el tamaño de la muestra."),
        ("¿Qué supuesto se hace sobre la variable en esta unidad?", "Que tiene distribución normal", "Es la condición bajo la que se razona en el OA."),
        ("¿Cuál es la diferencia entre parámetro y estadístico?", "El parámetro describe a la población; el estadístico se calcula con la muestra", "Uno suele ser desconocido y el otro es una estimación observable."),
    ],
    op=("Elige uno de estos casos de ejemplo. Caso 1: una variable normal con σ = 10, muestra de n = 25 y x̄ = 52. Caso 2: una variable normal con σ = 6, muestra de n = 9 y x̄ = 55. Supón que la media real fuera 50 en los dos casos. Calcula el error estándar, calcula la probabilidad de obtener una media muestral igual o mayor que la observada, di si es sorprendente y calcula qué tamaño de muestra daría un error estándar de 1. " + TABLA_Z,
        "Caso 1: error estándar 10 ÷ 5 = 2; z = (52 − 50) ÷ 2 = 1; P(x̄ ≥ 52) = 1 − 0,8413 = 0,1587, que no es sorprendente. Para error estándar 1 se necesita n = (10 ÷ 1)² = 100 datos.",
        ["calcula bien el error estándar", "estandariza con el error estándar y no con σ", "interpreta si la probabilidad es sorprendente", "calcula el n necesario"],
        ["hoja con el error estándar, el z, la probabilidad y el n necesario"],
        ["usar σ en lugar del error estándar", "olvidar el complemento en la cola derecha", "decir que x̄ es la media real"],
        "Pregunta: «¿por qué dividimos por √n?». Si no responde, pide que compare la variación de un dato con la de un promedio de varios datos."),
    reinforce="Con la ficha, calcula el error estándar si n fuera 144 en vez de 36, y explica cuántas veces más precisa es esa estimación.",
    extend="Explica con un ejemplo por qué es razonable que el promedio de 30 mediciones varíe menos que una sola medición.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (de ejemplo). El tiempo de espera en una oficina, en minutos, es normal con σ = 6 minutos conocida. Una muestra aleatoria de n = 36 clientes da x̄ = 20 minutos, así que el error estándar es 6 ÷ 6 = 1. "
     "Intervalo de confianza para μ con σ conocida: x̄ ± E, con margen de error E = z · σ ÷ √n. Valores de z: 90 % → 1,645; 95 % → 1,96; 99 % → 2,576. Para el tamaño de muestra: n ≥ (z · σ ÷ E)², redondeando hacia arriba.")
build(
    O4, 2, F,
    use="Aprenderé a construir e interpretar un intervalo de confianza para la media con σ conocida, y a ver cómo cambia con el nivel de confianza y el tamaño de la muestra.",
    prior=["Sé calcular el error estándar.", "Sé qué es el valor z de una normal.", "Sé calcular x̄ ± algo."],
    explain=[
        "Un intervalo de confianza es un rango de valores plausibles para un parámetro, construido con los datos de una muestra. Para la media μ con σ conocida, se calcula x̄ ± E, donde el margen de error es E = z · σ ÷ √n. El valor z depende del nivel de confianza: 1,645 para 90 %, 1,96 para 95 % y 2,576 para 99 %. El intervalo se puede escribir con la fórmula x̄ ± E o como un rango [a, b]; son dos formas de decir lo mismo, y el centro es siempre x̄.",
        "La interpretación correcta es cuidadosa. Un nivel de confianza de 95 % significa que si repitiéramos muchas veces el muestreo y construyéramos el intervalo de la misma forma, cerca del 95 % de esos intervalos contendría a μ. No significa que el 95 % de los datos esté dentro del intervalo ni que x̄ tenga 95 % de probabilidad de estar dentro (el centro siempre está dentro). μ es un valor fijo: lo que varía de muestra a muestra es el intervalo.",
        "El ancho del intervalo es 2E y depende de tres cosas: sube con el nivel de confianza (más confianza, más ancho), sube con σ y baja con n. Para dejar el margen de error en un valor E dado, se necesita al menos n = (z · σ ÷ E)² datos, redondeado hacia arriba. Como el error estándar baja con la raíz de n, reducir el margen a la mitad exige cuadruplicar la muestra.",
    ],
    vocab=[("intervalo de confianza", "rango de valores plausibles para un parámetro, construido con una muestra"), ("nivel de confianza", "porcentaje de intervalos construidos así que contendrían al parámetro"), ("margen de error E", "z · σ ÷ √n: distancia del centro a cada extremo"), ("valor crítico z", "número que depende del nivel de confianza: 1,645; 1,96 o 2,576"), ("ancho del intervalo", "distancia entre los extremos, que es 2E"), ("estimación puntual", "un solo valor, como x̄, usado para estimar μ")],
    worked=[
        ("Construir un intervalo", "Una variable normal de ejemplo tiene σ = 10; con n = 25 se obtiene x̄ = 50. Construye el IC al 95 %.", ["Error estándar: 10 ÷ 5 = 2. Margen: E = 1,96 × 2 = 3,92.", "Intervalo: 50 − 3,92 = 46,08 y 50 + 3,92 = 53,92."], "IC al 95 %: [46,08; 53,92]"),
        ("Recuperar la media y el margen", "Un IC al 95 % de ejemplo es [38, 46]. ¿Cuál fue x̄ y cuál el margen de error?", ["El centro es la media muestral: (38 + 46) ÷ 2 = 42.", "El margen es la mitad del ancho: (46 − 38) ÷ 2 = 4."], "x̄ = 42 y E = 4"),
    ],
    mistakes=[("Usar σ en vez de σ ÷ √n al calcular el margen de error.", "El margen depende del error estándar de la media, no de la dispersión de los datos individuales.", "Calcula primero σ ÷ √n y recién después multiplica por z."),
              ("Interpretar «95 %» como el porcentaje de los datos que cae dentro del intervalo.", "El intervalo es para la media μ, no para los datos individuales.", "Di: «el método captura a μ en cerca del 95 % de las muestras».")],
    T=[
        ('abc', '{F} ¿Qué valor z corresponde a un nivel de confianza de 95 %?', '1,96', '1,645', '2,576', 'El z de 95 % es 1,96; 1,645 corresponde a 90 % y 2,576 a 99 %.'),
        ('{F} Calcula el margen de error E para un nivel de confianza de 95 %.', R("1.96*6/6", 2), 'E = z · σ ÷ √n = 1,96 × 6 ÷ 6 = 1,96 minutos.'),
        ('abc', '{F} ¿Cuál es el intervalo de confianza al 95 % para μ?', '[18,04; 21,96]', '[8,24; 31,76]', '[19; 21]', 'Es 20 ± 1,96; [8,24; 31,76] usa σ en vez del error estándar y [19; 21] usa z = 1.'),
        ('{F} Construye el intervalo de confianza al 90 % para μ (con tres decimales).', f'[{R("20-1.645", 3)}; {R("20+1.645", 3)}]', 'E = 1,645 × 1 y el intervalo es 20 − 1,645 hasta 20 + 1,645.'),
        ('ab', '¿Qué valor ocupa el centro de un intervalo de confianza para μ?', 'La media muestral x̄', 'La media poblacional μ', 'El centro es siempre x̄, que es el valor observado; μ es el parámetro desconocido que se quiere estimar.'),
        ('{F} ¿Cuál es el ancho del intervalo de confianza al 95 %?', R("2*1.96*1", 2), 'El ancho es 2E, y E = 1,96 minutos.'),
        ('Una variable normal tiene σ = 15; con n = 25 se obtiene x̄ = 80. Construye el IC al 95 %.', f'[{R("80-1.96*3", 2)}; {R("80+1.96*3", 2)}]', 'El error estándar es 15 ÷ 5 = 3, E = 1,96 × 3 = 5,88 y el intervalo es 80 ± 5,88.'),
        ('Una variable normal tiene σ = 9; con n = 36 se obtiene x̄ = 100. Construye el IC al 99 % redondeando a dos decimales.', f'[{R("100-2.576*1.5", 2)}; {R("100+2.576*1.5", 2)}]', 'El error estándar es 9 ÷ 6 = 1,5, E = 2,576 × 1,5 = 3,864 y el intervalo es 100 ± 3,864.'),
        ('=', 'Un IC al 95 % de ejemplo es [62, 70]. ¿Cuál fue la media muestral x̄?', '(62+70)/2', 'La media muestral es el centro del intervalo, el promedio de sus extremos.', ''),
        ('abc', '{F} Se calcula el IC al 95 % para μ. ¿Qué interpretación es correcta?', 'Si se repitiera el muestreo muchas veces, cerca del 95 % de los intervalos así construidos contendría a μ', 'El 95 % de los tiempos de espera individuales está dentro del intervalo', 'Hay un 95 % de seguridad de que x̄ está dentro del intervalo', 'El nivel de confianza se refiere al método de construcción; x̄ siempre está en el centro y los datos individuales varían más.'),
        ('abc', 'Con el mismo n y σ, el nivel de confianza se sube de 95 % a 99 %. ¿Qué ocurre con el intervalo?', 'Se hace más ancho: se gana confianza a costa de precisión', 'Se hace más angosto', 'Se mantiene igual porque n no cambió', 'Un z mayor (2,576 en vez de 1,96) agranda el margen de error.'),
        ('{F} ¿Cuántos clientes se necesitan, como mínimo, para que el margen de error al 95 % sea 1 minuto o menos? Usa n ≥ (z · σ ÷ E)².', '139 clientes', '(1,96 × 6 ÷ 1)² = 11,76² = 138,3 aproximadamente, y se redondea hacia arriba.'),
        ('abc', 'Para reducir el margen de error a la mitad con la misma confianza, ¿qué se debe hacer con el tamaño de la muestra?', 'Cuadruplicarlo', 'Duplicarlo', 'Reducirlo a la mitad', 'El margen depende de σ ÷ √n, y para dividirlo por 2 hay que multiplicar n por 4.'),
    ],
    ctx=('abc', 'Una encuestadora de ejemplo estima el gasto mensual en transporte con una muestra aleatoria de n = 64 personas, con σ = 8.000 pesos conocida y x̄ = 30.000 pesos. ¿Cuál es el IC al 95 %?', '[28.040; 31.960] pesos', '[14.320; 45.680] pesos', '[29.000; 31.000] pesos', 'El error estándar es 1.000, E = 1,96 × 1.000 = 1.960 y el intervalo es 30.000 ± 1.960.'),
    sc=[
        ("En Estadística: ¿cuál es la fórmula del intervalo de confianza para μ con σ conocida?", "x̄ ± z · σ ÷ √n", "El margen de error es z veces el error estándar."),
        ("¿Cuánto vale z para un 95 % de confianza?", "1,96", "Es el valor crítico de la normal estándar para ese nivel."),
        ("¿Qué le ocurre al ancho del intervalo si aumenta n?", "Disminuye", "Un n mayor reduce el error estándar y el margen."),
    ],
    op=("Elige uno de estos casos de ejemplo. Caso 1: tiempo de carga de una aplicación, con σ = 0,8 s conocida, n = 64 y x̄ = 3,2 s. Caso 2: masa de paquetes, con σ = 20 g conocida, n = 100 y x̄ = 500 g; el fabricante afirma que la media real es 505 g. Calcula el IC al 95 % y al 99 %, interpreta uno de ellos con una frase correcta y decide si el valor afirmado (Caso 2: 505 g; Caso 1: 3,5 s) es plausible según cada intervalo.",
        "Caso 2: error estándar 2; IC 95 % = 500 ± 3,92 = [496,08; 503,92] y IC 99 % = 500 ± 5,152 = [494,85; 505,15]. Según el 95 %, 505 g no es plausible; según el 99 %, sí lo es. Interpretación: el método captura a la media real en cerca del 95 % de las muestras.",
        ["calcula bien el error estándar y el margen", "construye los dos intervalos", "interpreta sin decir que el 95 % de los datos está dentro", "decide la plausibilidad comparando con cada intervalo"],
        ["hoja con los dos intervalos, la interpretación y la decisión sobre el valor afirmado"],
        ["usar σ en vez del error estándar", "interpretar el nivel de confianza como porcentaje de datos", "decidir sin comparar el valor con el intervalo"],
        "Pregunta: «¿qué cambia entre tu intervalo al 95 % y al 99 %?». Si no lo explica, pide que compare los márgenes de error."),
    reinforce="Con la ficha, construye el IC al 95 % si el tamaño de la muestra fuera 144 en vez de 36, y compara su ancho con el original.",
    extend="Explica por qué un intervalo al 100 % de confianza no sería útil para una variable normal, y qué relación hay entre confianza y precisión.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (de ejemplo). Una fábrica afirma que sus baterías duran en promedio 500 horas. La duración se supone normal con σ = 40 horas conocida. Una muestra aleatoria de n = 64 baterías da x̄ = 490 horas. "
     "Hipótesis: H0: μ = 500 (afirmación que se pone a prueba) y H1: μ ≠ 500 (alternativa bilateral). Estadístico de prueba: z = (x̄ − μ0) ÷ (σ ÷ √n). Con nivel de significancia α = 0,05 bilateral, se rechaza H0 si |z| > 1,96; "
     "en una prueba unilateral con H1: μ < 500 al 5 %, se rechaza H0 si z < −1,645. Para α = 0,01 bilateral, el valor crítico es 2,576.")
build(
    O4, 3, F,
    use="Aprenderé a plantear y resolver una prueba de hipótesis para la media con σ conocida, y a escribir una conclusión que no diga más de lo que muestran los datos.",
    prior=["Sé calcular el error estándar.", "Sé estandarizar con z.", "Sé qué es un intervalo de confianza."],
    explain=[
        "Una prueba de hipótesis decide si los datos de una muestra son compatibles con una afirmación sobre la población. La afirmación que se evalúa es la hipótesis nula H0 y siempre incluye la igualdad (por ejemplo, μ = 500). La hipótesis alternativa H1 es lo que se acepta si los datos contradicen a H0: puede ser bilateral (μ ≠ 500) o unilateral (μ < 500 o μ > 500), según lo que interese detectar.",
        "El procedimiento tiene cinco pasos: plantear H0 y H1; fijar el nivel de significancia α (la probabilidad máxima que aceptamos de rechazar H0 cuando es verdadera, comúnmente 0,05); calcular el estadístico z = (x̄ − μ0) ÷ (σ ÷ √n); comparar con el valor crítico (1,96 para bilateral al 5 %); y decidir. Si |z| supera el valor crítico, se rechaza H0; si no, no se rechaza. Se rechaza cuando el resultado habría sido muy poco probable si H0 fuera verdadera.",
        "La conclusión se escribe en el contexto del problema y con cuidado. Rechazar H0 significa que hay evidencia en su contra al nivel α. No rechazar H0 no significa que sea verdadera: solo que los datos no dieron evidencia suficiente. Además, esto depende de los supuestos: muestra aleatoria, independencia y normalidad. Una hoja de cálculo o una calculadora estadística puede entregar z y el valor crítico, pero la decisión de qué hipótesis plantear y cómo concluir es tuya.",
    ],
    vocab=[("hipótesis nula H0", "afirmación con igualdad que se pone a prueba"), ("hipótesis alternativa H1", "afirmación que se acepta si se rechaza H0"), ("estadístico de prueba", "valor z calculado con la muestra"), ("nivel de significancia α", "probabilidad máxima de rechazar H0 siendo verdadera"), ("valor crítico", "límite que separa rechazar de no rechazar H0"), ("región de rechazo", "valores del estadístico para los que se rechaza H0")],
    worked=[
        ("Rechazar H0", "H0: μ = 60, con σ = 9 y n = 36; se observa x̄ = 63. Prueba bilateral al 5 %.", ["Error estándar: 9 ÷ 6 = 1,5. Estadístico: z = (63 − 60) ÷ 1,5 = 2.", "Como |2| > 1,96, se rechaza H0."], "Se rechaza H0: hay evidencia de que μ no es 60"),
        ("No rechazar H0", "H0: μ = 60, con σ = 9 y n = 36; se observa x̄ = 61. Prueba bilateral al 5 %.", ["Error estándar: 1,5. Estadístico: z = (61 − 60) ÷ 1,5 ≈ 0,67.", "Como 0,67 < 1,96, no se rechaza H0."], "No se rechaza H0: los datos no dan evidencia suficiente en su contra"),
    ],
    mistakes=[("Escribir «se acepta H0» cuando |z| no supera el valor crítico.", "No rechazar no demuestra que H0 sea verdadera, solo que faltó evidencia.", "Escribe «no hay evidencia suficiente para rechazar H0»."),
              ("Usar σ en vez de σ ÷ √n en el denominador de z.", "El estadístico compara x̄ y no un dato individual.", "Divide por el error estándar.")],
    T=[
        ('abc', '{F} ¿Cuál es la hipótesis nula H0 en esta situación?', 'μ = 500 horas', 'μ ≠ 500 horas', 'x̄ = 490 horas', 'H0 es la afirmación con igualdad sobre el parámetro, no sobre el estadístico de la muestra.'),
        ('ab', 'Si se quiere detectar cualquier diferencia con 500 horas, más alta o más baja, ¿cuál es la hipótesis alternativa?', 'μ ≠ 500', 'μ < 500', 'Una alternativa bilateral admite diferencias en los dos sentidos y se escribe con el signo distinto.'),
        ('=', '{F} Calcula el error estándar σ ÷ √n.', '40/8', 'La raíz cuadrada de 64 es 8, y el error estándar es 40 dividido por 8.', ' horas'),
        ('=', '{F} Calcula el estadístico z = (x̄ − μ0) ÷ error estándar.', '(490-500)/(40/8)', 'La diferencia es −10 horas y se divide por el error estándar de 5 horas.', ''),
        ('abc', '{F} En la prueba bilateral al 5 %, ¿cuál es la decisión?', 'Rechazar H0, porque |z| = 2 supera 1,96', 'No rechazar H0, porque x̄ está cerca de 500', 'Aceptar H0, porque z es negativo', 'Como 2 es mayor que el valor crítico 1,96, el resultado cae en la región de rechazo.'),
        ('abc', '¿Qué significa un nivel de significancia α = 0,05?', 'La probabilidad máxima aceptada de rechazar H0 cuando en realidad es verdadera', 'La probabilidad de que H0 sea verdadera', 'El porcentaje de datos que son atípicos', 'α fija cuánto riesgo se acepta de rechazar H0 siendo verdadera.'),
        ('Se prueba H0: μ = 120 con σ = 15, n = 100 y x̄ = 122, bilateral al 5 %. Calcula z (dos decimales) y decide.', f'z = {R("(122-120)/(15/10)", 2)}; no se rechaza H0', 'El error estándar es 1,5 y z = 2 ÷ 1,5 ≈ 1,33, que no supera 1,96.'),
        ('abc', '{F} Si la alternativa fuera H1: μ < 500 (unilateral) al 5 %, ¿qué se concluye con z = −2?', 'Rechazar H0, porque −2 es menor que −1,645', 'No rechazar H0, porque −2 es negativo', 'No rechazar H0, porque 1,645 es menor que 1,96', 'En la prueba unilateral izquierda se rechaza si z es menor que −1,645, y −2 lo es.'),
        ('Se prueba H0: μ = 12 con σ = 0,4, n = 16 y x̄ = 11,85, bilateral al 5 %. Calcula z (dos decimales) y decide.', f'z = {R("(11.85-12)/(0.4/4)", 2)}; no se rechaza H0', 'El error estándar es 0,1 y z = −0,15 ÷ 0,1 = −1,5, y |−1,5| < 1,96.'),
        ('abc', 'En una prueba, |z| no supera el valor crítico. ¿Qué se puede decir?', 'No hay evidencia suficiente para rechazar H0; eso no demuestra que sea verdadera', 'H0 queda demostrada como verdadera', 'H1 es falsa con certeza', 'No rechazar es una conclusión débil: los datos pudieron no ser suficientes para detectar una diferencia.'),
        ('abc', '{F} Con z = −2, ¿cambia la decisión si el nivel de significancia baja a α = 0,01 bilateral (valor crítico 2,576)?', 'Sí: ya no se rechaza H0, porque 2 < 2,576', 'No: 2 siempre supera el valor crítico', 'Sí: ahora se rechaza más fácilmente', 'Un α menor exige más evidencia, con un valor crítico mayor.'),
        ('{F} ¿Por debajo de qué valor de x̄ se rechazaría H0 en la prueba bilateral al 5 %, con n = 64? Responde con un decimal.', f'x̄ menor que {R("500-1.96*5", 1)}', 'Se rechaza si z < −1,96, es decir, si x̄ < 500 − 1,96 × 5.'),
        ('=', '{F} Si la misma diferencia de 10 horas se observara con n = 256 baterías, ¿cuánto valdría z?', '(490-500)/(40/16)', 'Con 256 datos el error estándar es 2,5 y la diferencia de −10 horas da un z más alejado de 0.', ''),
    ],
    ctx=('abc', 'Una empresa de reparto asegura que su tiempo medio de entrega es 30 minutos (σ = 5 minutos conocida). Una muestra de 100 entregas da x̄ = 31,4 minutos. En una prueba bilateral al 5 %, ¿qué conclusión corresponde?', 'Se rechaza H0: z = 2,8 supera 1,96 y hay evidencia de que el tiempo medio no es 30 minutos', 'No se rechaza H0: una diferencia de 1,4 minutos es pequeña', 'Se acepta H0: la media muestral es mayor que 30', 'El error estándar es 0,5 y z = 1,4 ÷ 0,5 = 2,8, que está en la región de rechazo.'),
    sc=[
        ("En Estadística: ¿qué afirmación se escribe en la hipótesis nula H0?", "La afirmación con igualdad que se pone a prueba, como μ = 500", "Es el punto de partida que los datos pueden contradecir."),
        ("¿Cómo se calcula el estadístico z de una prueba para la media con σ conocida?", "(x̄ − μ0) ÷ (σ ÷ √n)", "Mide a cuántos errores estándar está x̄ del valor de H0."),
        ("Si |z| supera el valor crítico, ¿qué se decide?", "Rechazar H0", "El resultado sería muy poco probable si H0 fuera verdadera."),
    ],
    op=("Elige uno de estos casos de ejemplo, ambos con σ conocida y variable normal. Caso 1: un envase dice contener 1.000 mL; σ = 12 mL; n = 36; x̄ = 996 mL. Caso 2: una pila dice durar 50 horas; σ = 10 horas; n = 25; x̄ = 53 horas. Realiza los cinco pasos (hipótesis, α = 0,05 bilateral, estadístico, valor crítico y decisión), escribe la conclusión en el contexto y agrega una frase sobre lo que no puedes concluir.",
        "Caso 1: H0: μ = 1.000 y H1: μ ≠ 1.000; error estándar 12 ÷ 6 = 2; z = (996 − 1.000) ÷ 2 = −2; |−2| > 1,96, se rechaza H0. Conclusión: hay evidencia de que el contenido medio no es 1.000 mL. No se puede concluir cuánto se desvía exactamente la media real ni que el proceso sea defectuoso.",
        ["plantea H0 y H1 correctamente", "calcula el error estándar y z", "compara con el valor crítico y decide", "conclusión en contexto con una limitación"],
        ["hoja con los cinco pasos y la conclusión"],
        ["escribir «se acepta H0»", "usar σ en vez del error estándar", "concluir más allá de lo que muestran los datos"],
        "Pregunta: «¿qué habría tenido que ocurrir para que no rechazaras H0?». Orienta hacia un z dentro de la zona entre −1,96 y 1,96."),
    reinforce="Con el Caso 2, plantea una prueba unilateral con H1: μ > 50 y compara el valor crítico 1,645 con tu z.",
    extend="Explica con tus palabras por qué no se escribe «se acepta H0» cuando los datos no dan evidencia contra ella.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (de ejemplo). Misma situación de baterías: H0: μ = 500 horas, σ = 40 horas conocida, n = 64 y x̄ = 490 horas, de modo que el error estándar es 5 y z = −2. "
     "Intervalo de confianza al 95 %: 490 ± 1,96 × 5. Error tipo I: rechazar H0 siendo verdadera (probabilidad α). Error tipo II: no rechazar H0 siendo falsa (probabilidad β). "
     "El valor p es la probabilidad, si H0 fuera verdadera, de obtener un resultado tan extremo como el observado o más; para una prueba bilateral con z conocido, p = 2 · (1 − Φ(|z|)). Se rechaza H0 si p < α. " + TABLA_Z)
build(
    O4, 4, F,
    use="Aprenderé a relacionar intervalos de confianza y pruebas de hipótesis, a interpretar el valor p y a reconocer los errores tipo I y tipo II al justificar una inferencia.",
    prior=["Sé construir un intervalo de confianza para μ.", "Sé realizar una prueba de hipótesis para μ.", "Sé leer la tabla de la normal."],
    explain=[
        "Un intervalo de confianza y una prueba de hipótesis bilateral cuentan la misma historia. Si el valor μ0 de H0 queda fuera del intervalo de confianza de nivel 1 − α, la prueba bilateral con nivel α rechaza H0; si queda dentro, no la rechaza. En la ficha, el intervalo al 95 % es [480,2; 499,8]; como 500 queda fuera, la prueba rechaza H0, igual que con z = −2. El intervalo, además, informa qué valores son plausibles.",
        "El valor p resume qué tan extremo es el resultado si H0 fuera verdadera. Con z = −2, p = 2 × (1 − 0,9772) = 0,0456. Como 0,0456 es menor que 0,05, se rechaza H0 al 5 %; pero con α = 0,01 no se rechazaría. El valor p no es la probabilidad de que H0 sea verdadera: es una probabilidad calculada suponiendo que H0 es verdadera.",
        "Toda decisión puede equivocarse. El error tipo I es rechazar H0 cuando era verdadera; su probabilidad es α. El error tipo II es no rechazar H0 cuando era falsa; su probabilidad es β. Bajar α reduce el error tipo I pero aumenta β si todo lo demás queda igual. La forma de reducir ambos errores a la vez es aumentar el tamaño de la muestra. Justificar una inferencia incluye decir qué error sería más grave en ese contexto.",
    ],
    vocab=[("valor p", "probabilidad de un resultado tan extremo o más, suponiendo H0 verdadera"), ("error tipo I", "rechazar H0 siendo verdadera; su probabilidad es α"), ("error tipo II", "no rechazar H0 siendo falsa; su probabilidad es β"), ("potencia", "probabilidad de rechazar H0 cuando es falsa, igual a 1 − β"), ("equivalencia IC–prueba", "μ0 fuera del IC de nivel 1 − α implica rechazar H0"), ("evidencia", "datos que respaldan o contradicen una afirmación")],
    worked=[
        ("Intervalo y prueba juntos", "H0: μ = 65, con σ = 10, n = 25 y x̄ = 62. Construye el IC al 95 % y decide la prueba bilateral al 5 %.", ["Error estándar: 2; margen 1,96 × 2 = 3,92; IC = [58,08; 65,92].", "El 65 está dentro del intervalo, así que no se rechaza H0."], "No se rechaza H0: 65 es plausible"),
        ("Calcular el valor p", "En una prueba bilateral, z = 1,5. Calcula p y decide al 5 %.", ["p = 2 × (1 − Φ(1,5)) = 2 × (1 − 0,9332) = 0,1336.", "Como 0,1336 > 0,05, no se rechaza H0."], "p = 0,1336: no se rechaza H0"),
    ],
    mistakes=[("Decir que un valor p de 0,03 significa que H0 tiene 3 % de probabilidad de ser verdadera.", "El valor p se calcula suponiendo que H0 es verdadera; no es la probabilidad de H0.", "Di: «si H0 fuera verdadera, un resultado así de extremo ocurriría cerca del 3 % de las veces»."),
              ("Creer que bajar α reduce todos los errores.", "Al exigir más evidencia, se rechaza menos y aumenta el error tipo II.", "Para reducir ambos errores, aumenta el tamaño de la muestra.")],
    T=[
        ('abc', '{F} ¿Cuál es el intervalo de confianza al 95 % para μ?', '[480,2; 499,8]', '[485; 495]', '[470,4; 509,6]', '490 ± 1,96 × 5 da 490 ± 9,8; [485; 495] usa solo el error estándar y el último intervalo usa el doble del margen.'),
        ('ab', '{F} ¿El valor 500 de H0 está dentro del intervalo de confianza al 95 %?', 'No: queda fuera, por encima de 499,8', 'Sí: está muy cerca de 499,8, así que está dentro', 'Un valor que supera el extremo superior del intervalo está fuera, aunque por poco.'),
        ('ab', '¿Qué es un error tipo I?', 'Rechazar H0 cuando en realidad es verdadera', 'No rechazar H0 cuando en realidad es falsa', 'El error tipo I consiste en rechazar una hipótesis nula verdadera, y su probabilidad es α.'),
        ('abc', '¿Qué es un error tipo II?', 'No rechazar H0 cuando en realidad es falsa', 'Rechazar H0 cuando en realidad es verdadera', 'Calcular mal el estadístico z', 'El error tipo II ocurre al no detectar que H0 era falsa, y su probabilidad se llama β.'),
        ('{F} Calcula el valor p de la prueba bilateral (z = −2).', R("2*(1-0.9772)", 4), 'p = 2 × (1 − Φ(2)) = 2 × (1 − 0,9772) = 0,0456.'),
        ('abc', '{F} Con p = 0,0456, ¿qué decisión se toma si α = 0,05?', 'Rechazar H0, porque 0,0456 < 0,05', 'No rechazar H0, porque 0,0456 es casi 5 %', 'Aceptar H0, porque p es pequeño', 'La regla es rechazar cuando p es menor que α, y aquí lo es.'),
        ('Se prueba H0: μ = 40 con σ = 6, n = 36 y x̄ = 43, bilateral al 5 %. Construye el IC al 95 % y decide.', f'IC = [{R("43-1.96*1", 2)}; {R("43+1.96*1", 2)}]; se rechaza H0 porque 40 queda fuera', 'El error estándar es 1 y E = 1,96; el intervalo es 43 ± 1,96 y no contiene a 40.'),
        ('En una prueba bilateral, z = 1. Calcula el valor p.', R("2*(1-0.8413)", 4), 'p = 2 × (1 − Φ(1)) = 2 × (1 − 0,8413) = 0,3174.'),
        ('=', 'Se realizan 100 pruebas independientes de una H0 verdadera, cada una con α = 0,05. ¿Cuántos rechazos erróneos se esperan?', '100*5/100', 'Con α = 5 %, en promedio cinco de cada cien pruebas rechazan por azar una H0 verdadera.', ' rechazos'),
        ('abc', 'Se baja α de 0,05 a 0,01 sin cambiar nada más. ¿Qué ocurre?', 'Disminuye la probabilidad de error tipo I, pero aumenta la de error tipo II', 'Disminuyen los dos errores', 'Aumenta el error tipo I y baja el tipo II', 'Exigir más evidencia para rechazar hace menos frecuentes los rechazos erróneos pero también los acertados.'),
        ('abc', '¿Cómo se puede reducir la probabilidad de error tipo II sin subir α?', 'Aumentando el tamaño de la muestra', 'Reduciendo el tamaño de la muestra', 'Eligiendo un valor crítico mayor', 'Con más datos el error estándar baja y se detectan mejor las diferencias reales.'),
        ('abc', 'Un IC al 95 % para μ es [48; 56]. Se prueba H0: μ = 58 al 5 % bilateral. ¿Qué se concluye?', 'Se rechaza H0, porque 58 queda fuera del intervalo', 'No se rechaza H0, porque 58 está cerca de 56', 'No se puede decidir sin recalcular z', 'Si el valor de H0 está fuera del IC del mismo nivel, la prueba bilateral lo rechaza.'),
        ('abc', 'En una prueba se obtiene p = 0,03. ¿Qué afirmación es correcta?', 'Si H0 fuera verdadera, un resultado tan extremo ocurriría cerca del 3 % de las veces; se rechaza con α = 0,05 pero no con α = 0,01', 'H0 tiene 3 % de probabilidad de ser verdadera', 'H1 tiene 97 % de probabilidad de ser verdadera', 'El valor p se calcula suponiendo H0 verdadera y se compara con α para decidir.'),
    ],
    ctx=('abc', 'Una empresa de ejemplo retira un lote de piezas si rechaza H0: «el lote cumple la norma». Retirar un lote que sí cumplía la norma, ¿qué error es?', 'Error tipo I: rechazar una H0 verdadera', 'Error tipo II: no rechazar una H0 falsa', 'No es un error, porque retirar es siempre más seguro', 'Rechazar H0 cuando era verdadera es exactamente el error tipo I.'),
    sc=[
        ("En Estadística: ¿qué regla relaciona el IC con una prueba bilateral?", "Si μ0 queda fuera del IC de nivel 1 − α, se rechaza H0", "Ambos procedimientos usan el mismo error estándar y valor crítico."),
        ("¿Cuándo se rechaza H0 usando el valor p?", "Cuando p es menor que α", "Un p pequeño indica un resultado muy poco probable si H0 fuera verdadera."),
        ("¿Qué es un error tipo II?", "No rechazar H0 siendo falsa", "Es no detectar una diferencia que sí existe."),
    ],
    op=("Elige uno de estos casos de ejemplo, con σ conocida y variable normal. Caso 1: H0: μ = 52 minutos de atención; σ = 12; n = 36; x̄ = 47. Caso 2: H0: μ = 100; σ = 20; n = 100; x̄ = 103. Construye el IC al 95 %, calcula z y el valor p, decide por los dos caminos (IC y valor p) con α = 0,05, comprueba que coinciden, y escribe qué error podrías estar cometiendo con tu decisión. " + TABLA_Z,
        "Caso 1: error estándar 2; IC = 47 ± 3,92 = [43,08; 50,92]; 52 queda fuera. z = (47 − 52) ÷ 2 = −2,5 y p = 2 × (1 − 0,9938) = 0,0124 < 0,05. Ambos caminos rechazan H0. Si rechazo y H0 era verdadera, cometería un error tipo I (probabilidad 5 %).",
        ["intervalo y z calculados correctamente", "valor p calculado con la tabla", "las dos decisiones coinciden y se explica por qué", "identifica el error posible"],
        ["hoja con el IC, el z, el valor p, las dos decisiones y el error posible"],
        ["interpretar p como la probabilidad de H0", "no comprobar que ambos caminos coinciden", "confundir error tipo I con tipo II"],
        "Pregunta: «¿qué error cometerías si tu decisión fuera equivocada?». Si no distingue, pide que complete: «rechazo, pero H0 era ...»."),
    reinforce="Con el Caso 2, calcula el IC al 99 % (usa z = 2,576) y decide si 100 sigue dentro; compara con el resultado al 95 %.",
    extend="Explica con un ejemplo cotidiano por qué a veces es preferible aceptar más riesgo de error tipo I que de error tipo II (o al revés).",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 5 (de ejemplo). Una muestra aleatoria de n = 16 mediciones de una variable normal, con σ desconocida, da x̄ = 70 y s = 8 (varianza muestral s² = 64). Con 15 grados de libertad (gl = n − 1): "
     "t para 95 % = 2,131 y t para 99 % = 2,947 (valores de tabla). IC para μ con σ desconocida: x̄ ± t · s ÷ √n. "
     "Para la varianza, con 15 gl, los valores de la distribución chi cuadrado son 27,488 (superior) y 6,262 (inferior), para un nivel de 95 %; IC para σ²: desde (n − 1) · s² ÷ 27,488 hasta (n − 1) · s² ÷ 6,262.")
build(
    O4, 5, F,
    use="Aprenderé a hacer inferencias sobre la media cuando σ es desconocida (con t) y sobre la varianza (con chi cuadrado), y a comparar los resultados y sus supuestos.",
    prior=["Sé construir un IC para μ con σ conocida.", "Sé calcular s y s² de una muestra.", "Sé leer una tabla de valores críticos."],
    explain=[
        "En la práctica σ casi nunca se conoce y se estima con la desviación estándar muestral s. Entonces el estadístico (x̄ − μ) ÷ (s ÷ √n) ya no sigue una normal, sino una distribución t de Student con n − 1 grados de libertad (gl). La t es parecida a la normal, pero con colas más pesadas, para reflejar la incertidumbre extra de estimar σ; al aumentar n se acerca a la normal. El intervalo para μ queda x̄ ± t · s ÷ √n, con el valor t de una tabla, y es algo más ancho que el de σ conocida.",
        "Para estimar la varianza σ² (o la desviación σ), si los datos son normales, la cantidad (n − 1) · s² ÷ σ² sigue una distribución chi cuadrado con n − 1 grados de libertad. Esta distribución no es simétrica, así que el intervalo de confianza para σ² no está centrado en s²: va desde (n − 1) · s² ÷ χ²superior hasta (n − 1) · s² ÷ χ²inferior. Para obtener un intervalo para σ se saca raíz cuadrada a ambos extremos.",
        "Comprobar y comparar: antes de usar estos intervalos hay que revisar el supuesto de normalidad (por ejemplo, con un histograma sin asimetría fuerte ni valores extremos); si no se cumple, el intervalo puede ser engañoso. Un intervalo para σ que contiene un valor de referencia no permite afirmar que lo cumple ni que no lo cumple. Las tablas de t y de chi cuadrado, o una calculadora estadística, entregan los valores críticos, pero la interpretación sigue siendo tuya.",
    ],
    vocab=[("distribución t de Student", "modelo para la media cuando σ se estima con s; depende de los grados de libertad"), ("grados de libertad", "n − 1 en estos procedimientos"), ("chi cuadrado", "distribución usada para inferencias sobre la varianza"), ("IC para σ²", "intervalo de confianza para la varianza"), ("asimetría", "forma no simétrica de una distribución, como la chi cuadrado"), ("supuesto de normalidad", "condición que se revisa antes de usar t o chi cuadrado")],
    worked=[
        ("IC para la media con t", "n = 9, x̄ = 30 y s = 6. Con 8 gl, t para 95 % = 2,306. Construye el IC para μ.", ["Error estándar estimado: s ÷ √n = 6 ÷ 3 = 2. Margen: 2,306 × 2 = 4,612.", "Intervalo: 30 − 4,612 = 25,388 y 30 + 4,612 = 34,612."], "IC al 95 %: [25,388; 34,612]"),
        ("IC para la varianza", "n = 9 y s = 3, así que s² = 9. Con 8 gl, los valores chi cuadrado son 17,535 y 2,180. Construye el IC al 95 % para σ².", ["(n − 1) · s² = 8 × 9 = 72.", "Extremos: 72 ÷ 17,535 ≈ 4,106 y 72 ÷ 2,180 ≈ 33,028."], "IC al 95 % para σ²: [4,106; 33,028]"),
    ],
    mistakes=[("Usar z = 1,96 con una muestra pequeña y σ estimada con s.", "Ignora la incertidumbre extra de estimar σ y da un intervalo demasiado angosto.", "Usa t con n − 1 grados de libertad."),
              ("Centrar el IC de la varianza en s² sumando y restando un margen.", "La chi cuadrado es asimétrica y el intervalo no es simétrico.", "Calcula cada extremo con su valor chi cuadrado.")],
    T=[
        ('abc', '{F} ¿Cuántos grados de libertad hay?', '15', '16', '14', 'Los grados de libertad son n − 1 = 16 − 1 = 15.'),
        ('=', '{F} Calcula el error estándar estimado s ÷ √n.', '8/4', 'La raíz cuadrada de 16 es 4, y 8 dividido por 4 es el error estándar estimado.', ''),
        ('ab', '¿Cuándo se usa la distribución t en lugar de la normal para x̄?', 'Cuando σ es desconocida y se estima con s', 'Cuando σ es conocida y la muestra es muy grande', 'La t corrige la incertidumbre de usar s en lugar de σ, y por eso se usa cuando σ es desconocida.'),
        ('{F} Calcula el margen de error del IC al 95 % para μ, con t · s ÷ √n (tres decimales).', R("2.131*2", 3), 'El error estándar estimado es 2 y el margen es 2,131 × 2 = 4,262.'),
        ('{F} Construye el IC al 95 % para μ.', f'[{R("70-4.262", 3)}; {R("70+4.262", 3)}]', 'El margen es 4,262 y el intervalo es 70 ± 4,262.'),
        ('abc', '{F} Si σ fuera conocida e igual a 8, el IC al 95 % con z = 1,96 tendría margen 3,92. Comparado con el IC con t, ¿cómo es?', 'El IC con t es más ancho, porque refleja la incertidumbre de estimar σ con s', 'El IC con t es más angosto', 'Los dos intervalos son iguales', 'El valor t de 2,131 es mayor que 1,96 y por eso el margen es mayor.'),
        ('=', '{F} Calcula (n − 1) · s² para el intervalo de la varianza.', '15*8*8', 'Se multiplica 15 por el cuadrado de s, que es 64.', ''),
        ('{F} Construye el IC al 95 % para σ² (dos decimales).', f'[{R("960/27.488", 2)}; {R("960/6.262", 2)}]', 'Se divide 960 por 27,488 y por 6,262 para obtener los dos extremos.'),
        ('{F} Construye el IC al 95 % para σ sacando la raíz cuadrada de los extremos del IC para σ² (dos decimales).', f'[{R("sqrt(960/27.488)", 2)}; {R("sqrt(960/6.262)", 2)}]', 'Las raíces de 34,92 y de 153,31 dan los extremos para la desviación estándar.'),
        ('abc', '¿Por qué el IC para la varianza no queda centrado en s²?', 'Porque la distribución chi cuadrado es asimétrica', 'Porque s² es siempre mayor que σ²', 'Porque se usó z en vez de t', 'Los dos valores chi cuadrado no son simétricos, y por eso el intervalo no es s² ± algo.'),
        ('abc', 'Los datos de una muestra tienen un histograma con cola larga a la derecha y valores muy extremos. ¿Qué conviene hacer antes de usar el IC con t?', 'Revisar si el supuesto de normalidad es razonable; si no, el intervalo puede ser engañoso', 'Usarlo igual, porque t corrige cualquier forma', 'Cambiar el nivel de confianza a 99 %', 'La t supone datos normales; con una forma muy asimétrica, la cobertura real del intervalo puede ser menor que la anunciada.'),
        ('abc', 'Una máquina debe tener σ ≤ 10 según una norma. El IC al 95 % para σ de la ficha es [5,91; 12,38]. ¿Qué se concluye?', 'No se puede asegurar que cumpla ni que no cumpla, porque 10 queda dentro del intervalo', 'Cumple, porque s = 8 es menor que 10', 'No cumple, porque 12,38 es mayor que 10', 'Con 10 dentro de los valores plausibles, la muestra no basta para decidir.'),
        ('{F} Construye el IC al 99 % para μ usando t = 2,947 (tres decimales).', f'[{R("70-2.947*2", 3)}; {R("70+2.947*2", 3)}]', 'El margen es 2,947 × 2 = 5,894 y el intervalo es 70 ± 5,894.'),
    ],
    ctx=('abc', 'En una muestra aleatoria de 4 mediciones normales, x̄ = 40 y s = 4. Con 3 gl, t para 95 % = 3,182. ¿Cuál es el IC al 95 % para μ?', '[33,636; 46,364]', '[36,08; 43,92]', '[36; 44]', 'El error estándar estimado es 2 y el margen es 3,182 × 2 = 6,364; usar z = 1,96 daría un intervalo demasiado angosto.'),
    sc=[
        ("En Estadística: ¿cuántos grados de libertad tiene la t de una muestra de n datos?", "n − 1", "Se pierde un grado de libertad al estimar la media con los mismos datos."),
        ("¿Qué distribución se usa para el intervalo de confianza de la varianza?", "La chi cuadrado", "Describe (n − 1) · s² ÷ σ² cuando los datos son normales."),
        ("¿Qué supuesto se debe revisar antes de usar t o chi cuadrado?", "Que la variable sea aproximadamente normal", "Si no se cumple, los intervalos pueden ser engañosos."),
    ],
    op=("Elige uno de estos casos de ejemplo, ambos con n = 16 mediciones normales, 15 gl, t para 95 % = 2,131 y valores chi cuadrado 27,488 y 6,262. Caso 1: tiempos de reparto en minutos con x̄ = 24 y s = 4. Caso 2: masas de un producto en gramos con x̄ = 100 y s = 12. Construye el IC al 95 % para μ y para σ², y compara el IC de μ con uno hecho con z = 1,96 como si σ fuera conocida. Si tu caso es el 1, decide si la afirmación «el tiempo medio es 25 minutos» es plausible; si es el 2, decide si «la desviación estándar es 15 g» es plausible.",
        "Caso 1: error estándar estimado 4 ÷ 4 = 1; IC para μ = 24 ± 2,131 = [21,869; 26,131]. (n − 1) · s² = 15 × 16 = 240; IC para σ² = [240 ÷ 27,488; 240 ÷ 6,262] = [8,73; 38,33]. Con z = 1,96 el IC sería [22,04; 25,96], más angosto. El valor 25 está dentro de [21,869; 26,131], luego es plausible.",
        ["usa t con 15 gl para la media", "calcula (n − 1) · s² y los dos extremos para la varianza", "compara con el IC hecho con z", "decide la plausibilidad comparando el valor con el intervalo"],
        ["hoja con los dos intervalos, la comparación con z y la decisión de plausibilidad"],
        ["usar 1,96 en vez de 2,131", "centrar el IC de la varianza en s²", "afirmar que el valor se cumple sin que el intervalo lo permita"],
        "Pregunta: «¿por qué el IC con t es más ancho que el de z?». Si no responde, pide que explique qué incertidumbre extra aparece al estimar σ."),
    reinforce="Con la ficha, construye el IC al 95 % para σ² si s fuera 6 en vez de 8, y compara sus extremos con los originales.",
    extend="Explica por qué, cuando n es muy grande, el IC con t y el IC con z casi coinciden.",
)
