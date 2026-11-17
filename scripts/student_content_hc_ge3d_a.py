"""Geometría 3D (electivo HC, 3.º y 4.º medio): OAC-01 (isometrías y homotecias en el plano con vectores), clases 1 a 5. Todo en papel; las representaciones digitales se describen por escrito."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel cuadriculado; calculadora simple opcional. No se necesita software: las representaciones digitales "
             "(hoja de cálculo o geometría dinámica) se describen en la ficha y se razonan a mano. Si usas un programa, hazlo con la supervisión de tu docente.")
build = make_build(MATERIALS)

O1 = "MA-GE3D-3y4-OAC-01"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (de ejemplo). En un plano con ejes, el triángulo ABC tiene A(1, 2), B(4, 2) y C(4, 6). Se aplica la traslación dada por el vector v = (3, −2): "
     "a cada punto se le suma 3 a la coordenada x y se le resta 2 a la coordenada y. Los lados miden AB = 3, BC = 4 y AC = 5 unidades.")
build(
    O1, 1, F,
    use="Aprenderé a describir una traslación con un vector, a calcular imágenes de puntos y a argumentar si una solución es válida comprobando sus condiciones.",
    prior=["Sé ubicar puntos con coordenadas (x, y).", "Sé que una isometría conserva la forma y el tamaño de una figura.", "Sé sumar y restar números enteros."],
    explain=[
        "En Geometría 3D empezamos en el plano. Un vector es una flecha que indica un desplazamiento; se escribe con dos números, por ejemplo v = (3, −2): el primero mueve en horizontal (x) y el segundo en vertical (y). Una traslación mueve todos los puntos de una figura con el mismo vector: la imagen de P(x, y) es P′(x + 3, y − 2). Si conoces P y P′, el vector se obtiene restando: v = P′ − P.",
        "Una isometría es una transformación que conserva las longitudes y los ángulos, así que la figura imagen es congruente (idéntica en forma y tamaño) a la original. La traslación es una isometría porque, al sumar el mismo vector a dos puntos, la diferencia entre ellos no cambia. Por eso, además, conserva el área, el perímetro y el paralelismo.",
        "Argumentar la validez de una solución significa comprobar sus condiciones, no solo aplicar una regla. Se aplica el vector a todos los vértices (no solo a uno), se revisan las longitudes de los lados y se verifica que cada punto use el mismo vector. Un solo vértice que no cumpla basta para decir que la solución no es válida: eso se llama un contraejemplo.",
    ],
    vocab=[("vector", "flecha que indica un desplazamiento, escrita como (a, b)"), ("traslación", "movimiento que desplaza todos los puntos con el mismo vector"), ("imagen", "figura o punto que resulta de transformar"), ("isometría", "transformación que conserva longitudes y ángulos"), ("congruente", "de igual forma y tamaño"), ("contraejemplo", "caso que muestra que una afirmación es falsa")],
    worked=[
        ("Trasladar un punto", "Traslada D(−2, 5) con el vector w = (4, −7).", ["Suma 4 a la coordenada x: −2 + 4 = 2.", "Suma −7 a la coordenada y: 5 − 7 = −2."], "D′ = (2, −2)"),
        ("Validar una solución", "Alguien afirma que P(1, 1) → P′(6, 3) y Q(2, 4) → Q′(7, 6) son una misma traslación con v = (5, 2). ¿Es válido?", ["Calcula P′ − P = (6 − 1, 3 − 1) = (5, 2).", "Calcula Q′ − Q = (7 − 2, 6 − 4) = (5, 2): coincide con el primero."], "Sí es válido: los dos puntos usan el mismo vector (5, 2)"),
    ],
    mistakes=[("Aplicar el vector solo a la coordenada x y dejar la y igual.", "La traslación mueve el punto en las dos direcciones a la vez.", "Suma la primera componente a x y la segunda a y."),
              ("Restar el vector en vez de sumarlo, o invertir el orden P − P′.", "La imagen es P + v; el vector se calcula como P′ − P.", "Escribe siempre «punto final menos punto inicial» para hallar el vector.")],
    T=[
        ('abc', '{F} ¿Cuáles son las coordenadas de B′?', '(7, 0)', '(7, 4)', '(1, 4)', 'B(4, 2) más (3, −2) da (7, 0); (7, 4) suma el 2 en vez de restarlo y (1, 4) resta el vector completo.'),
        ('abc', '¿Qué conserva una traslación?', 'Longitudes, ángulos y área de la figura', 'Solo los ángulos, mientras las longitudes cambian según el vector', 'Solo el área, porque los lados se estiran y se encogen', 'La traslación es una isometría: no altera ni lados ni ángulos ni área.'),
        ('ab', 'Un vector (−2, 5) aplicado a un punto, ¿qué hace con sus coordenadas?', 'Resta 2 a x y suma 5 a y', 'Suma 2 a x y resta 5 a y', 'Cada componente se suma con su signo: −2 en x y +5 en y.'),
        ('{F} El triángulo ABC es rectángulo en B. ¿Cuánto mide el lado A′C′ de su imagen, en unidades?', '5 unidades', 'La traslación conserva las longitudes, y A′C′ corresponde al lado AC de 5 unidades.'),
        ('abc', 'Un punto P(2, 3) llega a P′(−1, 7). ¿Cuál es el vector de la traslación?', '(−3, 4)', '(3, −4)', '(1, 10)', 'Se calcula P′ − P = (−1 − 2, 7 − 3); (3, −4) es P − P′ y (1, 10) es una suma.'),
        ('=', 'El vector de una traslación es (5, −3) y un punto está en (−4, 9). ¿Cuál es la coordenada y de su imagen?', '9-3', 'Se suma la segunda componente del vector a la coordenada y.'),
        ('Aplica v = (3, −2) al punto D(−1, 6). ¿Cuál es D′?', '(2, 4)', 'Se calcula (−1 + 3, 6 − 2) para obtener la imagen D′.'),
        ('abc', '{F} Un estudiante escribió C′ = (7, 8). ¿Qué error cometió?', 'Sumó 2 en vez de restar 2 a la coordenada y', 'Restó 3 en vez de sumar 3 a la coordenada x', 'Aplicó una reflexión en vez de una traslación', 'C(4, 6) debe quedar en (7, 4); el 8 sale de 6 + 2, es decir, de usar el signo equivocado en y.'),
        ('=', 'Un rectángulo de vértices (0, 0), (6, 0), (6, 2) y (0, 2) se traslada con el vector (−4, 5). ¿Cuál es el área de la imagen?', '6*2', 'La traslación conserva el área, que es base por altura del rectángulo.', ' unidades cuadradas'),
        ('abc', 'Una estudiante afirma: «la traslación conserva las longitudes porque a todos los puntos se les suma el mismo vector». ¿Qué argumento lo justifica?', 'La diferencia entre las coordenadas de dos puntos no cambia al sumarles el mismo vector', 'El vector tiene una longitud fija y por eso nada puede variar', 'La figura gira un ángulo pequeño que no se alcanza a notar', 'Si P y Q suman el mismo v, (Q + v) − (P + v) = Q − P, así que la distancia entre ellos es idéntica.'),
        ('abc', 'Un diseñador mueve E(2, 2) a E′(5, 3) y F(4, 2) a F′(8, 4) y dice que usó una traslación. ¿Es válido?', 'No: E→E′ usa (3, 1) y F→F′ usa (4, 2), vectores distintos', 'Sí: los dos puntos se movieron hacia la derecha y hacia arriba', 'Sí: los dos puntos terminaron con coordenadas mayores', 'Una traslación exige un único vector para todos los puntos; aquí hay dos vectores diferentes.'),
        ('Una traslación lleva A(1, 2) a A′(4, 0) y otra lleva A′ a A″(2, 5). ¿Cuál es el vector de una sola traslación que lleva A directamente a A″?', '(1, 3)', 'Se calcula A″ − A = (2 − 1, 5 − 2); equivale a sumar (3, −2) y (−2, 5).'),
        ('=', '{F} Calcula el perímetro del triángulo A′B′C′ en unidades.', '3+4+5', 'La traslación conserva las longitudes, así que el perímetro es el del triángulo ABC.', ' unidades'),
    ],
    ctx=('abc', 'Una baldosa decorativa tiene un motivo con un vértice en (2, 1). Para repetir el patrón se aplica cuatro veces seguidas la traslación (4, 0). ¿Dónde queda ese vértice en la última copia?', '(18, 1)', '(16, 1)', '(6, 1)', 'Cuatro traslaciones suman 4 · 4 = 16 a x, y 2 + 16 = 18; (16, 1) olvida la posición inicial y (6, 1) cuenta una sola traslación.'),
    sc=[
        ("En Geometría: ¿cómo se obtiene el vector que lleva P a P′?", "Restando: P′ − P", "El vector es el punto final menos el punto inicial."),
        ("¿Cuántos vértices hay que revisar para validar que una figura se trasladó con un vector?", "Todos", "Un solo vértice con otro vector basta para invalidar la solución."),
        ("¿La traslación conserva el área?", "Sí", "Es una isometría y no cambia ni longitudes ni ángulos."),
    ],
    op=("Elige uno de estos dos casos. Caso 1: el cuadrado de vértices (0, 0), (2, 0), (2, 2) y (0, 2) se traslada con v = (5, 1). Caso 2: el segmento de extremos (−3, 4) y (1, 4) se traslada con v = (2, −6). Calcula las imágenes de todos sus vértices, comprueba que una longitud no cambió y escribe una frase que explique por qué tu solución es válida.",
        "Caso 1: las imágenes son (5, 1), (7, 1), (7, 3) y (5, 3). El lado de (0, 0) a (2, 0) mide 2 y el de (5, 1) a (7, 1) también mide 2. Es válida porque todos los vértices usan v = (5, 1).",
        ["calcula la imagen de todos los vértices con el mismo vector", "comprueba al menos una longitud", "justifica con la condición del vector único"],
        ["hoja con las imágenes, una comprobación de longitud y la frase de justificación"],
        ["aplicar el vector solo a un vértice", "invertir el signo de una componente", "decir «se ve igual» sin comprobar medidas"],
        "Pregunta: «¿con qué vector llegaste a cada vértice?». Si no coinciden, pide que reste imagen menos original."),
    reinforce="Dibuja en papel cuadriculado el triángulo de la ficha, traslada tres vértices con v = (−2, 3) y mide con regla un lado antes y después.",
    extend="Explica con tus palabras por qué la composición de dos traslaciones es otra traslación, y cómo se calcula su vector.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (de ejemplo). Triángulo MNR con M(1, 1), N(4, 1) y R(4, 3), recorrido M → N → R en sentido antihorario (contrario a las agujas del reloj). "
     "Reglas con centro en el origen O(0, 0): reflexión en el eje x: (x, y) → (x, −y); reflexión en el eje y: (x, y) → (−x, y); "
     "rotación de 90° antihoraria: (x, y) → (−y, x); rotación de 180°: (x, y) → (−x, −y).")
build(
    O1, 2, F,
    use="Aprenderé a aplicar reflexiones y rotaciones con coordenadas, y a comprobar si una imagen calculada es correcta usando distancias y el sentido del recorrido.",
    prior=["Sé que la traslación es una isometría.", "Sé calcular distancias con el teorema de Pitágoras.", "Sé ubicar puntos con signos en los cuatro cuadrantes."],
    explain=[
        "Una reflexión es un «espejo»: cada punto y su imagen quedan a la misma distancia de la recta de reflexión y a lados opuestos. Al reflejar en el eje x cambia el signo de y; al reflejar en el eje y cambia el signo de x. Una rotación gira la figura alrededor de un centro un cierto ángulo y en un sentido; con centro en el origen, el giro de 90° antihorario lleva (x, y) a (−y, x).",
        "Reflexión y rotación son isometrías: conservan longitudes y ángulos. Sin embargo, la reflexión invierte la orientación, es decir, el orden de los vértices que era antihorario pasa a ser horario, y la rotación no. En una rotación cada punto conserva su distancia al centro; en una reflexión, cada par punto-imagen es simétrico respecto de la recta.",
        "Para argumentar si una imagen está bien calculada no basta con una sola pista. Si un punto y su supuesta imagen están a igual distancia del centro, aún no sabes si giraron en el sentido correcto: hay que aplicar la regla o revisar el sentido del recorrido de los vértices. Siempre se comprueba con las condiciones del problema: el tipo de transformación, el centro y el sentido.",
    ],
    vocab=[("reflexión", "transformación que da la imagen en espejo respecto de una recta"), ("rotación", "giro de la figura alrededor de un centro"), ("centro de rotación", "punto fijo alrededor del cual se gira"), ("sentido antihorario", "contrario a las agujas del reloj"), ("orientación", "sentido en que se recorren los vértices"), ("simétrico", "al otro lado de una recta, a igual distancia")],
    worked=[
        ("Dos transformaciones seguidas", "Aplica a K(−2, 5) la reflexión en el eje x y luego la rotación de 90° antihoraria.", ["Reflexión en el eje x: (−2, 5) → (−2, −5).", "Rotación (x, y) → (−y, x): (−2, −5) → (5, −2)."], "K″ = (5, −2)"),
        ("Revisar una imagen", "Una estudiante dice que la rotación de 90° antihoraria de B(2, 5) es (5, −2) porque ambos están a la misma distancia del origen. ¿Es correcto?", ["La distancia al origen no distingue el sentido del giro.", "La regla da (−5, 2); el punto (5, −2) corresponde a un giro de 90° horario."], "No: la imagen correcta es (−5, 2)"),
    ],
    mistakes=[("Reflejar en el eje x y cambiar el signo de x.", "En el eje x se mantiene x y se cambia el signo de y.", "Pregunta «¿qué coordenada se aleja del eje?» y cambia solo esa."),
              ("Usar la rotación horaria cuando se pide antihoraria.", "Los dos giros terminan a igual distancia del centro, pero en puntos distintos.", "Aplica la regla (x, y) → (−y, x) y comprueba el cuadrante.")],
    T=[
        ('abc', 'Al reflejar en el eje x el punto (4, 7), ¿qué imagen resulta?', '(4, −7)', '(−4, 7)', '(−4, −7)', 'En el eje x solo cambia el signo de y; (−4, 7) corresponde al eje y y (−4, −7) a un giro de 180°.'),
        ('abc', 'La regla de una rotación de 180° con centro en el origen es:', '(x, y) → (−x, −y)', '(x, y) → (y, x)', '(x, y) → (−y, x)', 'El giro de 180° cambia el signo de ambas coordenadas; las otras reglas son una reflexión y un giro de 90°.'),
        ('ab', '¿Qué cambia en una reflexión respecto de una rotación?', 'La orientación: el recorrido de los vértices se invierte', 'Las longitudes: los lados de la imagen cambian de medida', 'Las dos conservan longitudes y ángulos; solo la reflexión invierte el sentido del recorrido.'),
        ('{F} Aplica la rotación de 90° antihoraria al vértice N. ¿Dónde queda N′?', '(−1, 4)', 'Con (x, y) → (−y, x) y N(4, 1) resulta (−1, 4).'),
        ('abc', '{F} ¿Cuál es la imagen de R por reflexión en el eje y?', '(−4, 3)', '(4, −3)', '(−3, 4)', 'En el eje y cambia el signo de x: R(4, 3) → (−4, 3).'),
        ('El punto (6, 8) se rota 180° con centro en el origen y queda en (−6, −8). ¿A cuántas unidades del origen queda la imagen? Usa Pitágoras.', '10 unidades', '(−6)² + (−8)² = 100, y la raíz de 100 es 10; la rotación conserva la distancia al centro.'),
        ('Aplica al vértice N(4, 1) primero la reflexión en el eje x y luego la rotación de 90° antihoraria. ¿Dónde queda?', '(1, 4)', 'La reflexión lleva N a (4, −1) y la rotación (x, y) → (−y, x) lo lleva a (1, 4).'),
        ('abc', '{F} Se rota el triángulo 180°. ¿Cuál es la imagen de R?', '(−4, −3)', '(−4, 3)', '(−3, 4)', 'Con (x, y) → (−x, −y), R(4, 3) → (−4, −3); (−4, 3) es la reflexión y (−3, 4) el giro de 90°.'),
        ('=', '{F} El triángulo MNR es rectángulo en N, con catetos MN = 3 y NR = 2. ¿Cuál es el área de su imagen por cualquier reflexión o rotación?', '3*2//2', 'Las isometrías conservan el área, que es cateto por cateto dividido en dos.', ' unidades cuadradas'),
        ('abc', 'Una estudiante rota A(3, 1) 90° en sentido antihorario con centro en el origen y obtiene (3, −1), «porque girar solo cambia un signo». ¿Qué ocurrió?', 'Aplicó una reflexión en el eje x; la rotación da (−1, 3)', 'Aplicó una reflexión en el eje y; la rotación da (−3, 1)', 'Tiene razón: la rotación de 90° solo cambia el signo de la coordenada y', 'Cambiar solo el signo de y es la reflexión en el eje x; la regla de la rotación (x, y) → (−y, x) da (−1, 3).'),
        ('abc', 'Los vértices de un triángulo se recorrían en sentido antihorario y en la imagen se recorren en sentido horario. ¿Qué transformación pudo ser?', 'Una reflexión', 'Una traslación', 'Una rotación de 90°', 'Solo la reflexión invierte la orientación; traslación y rotación la conservan.'),
        ('Una reflexión en el eje x seguida de una reflexión en el eje y equivale a una sola rotación. ¿De cuántos grados y con qué regla?', '180°: (x, y) → (−x, −y)', 'Primero (x, y) → (x, −y) y luego → (−x, −y), que es el giro de 180° con centro en el origen.'),
        ('Un punto (a, b) con a > 0 y b > 0 se rota 90° antihorario con centro en el origen y queda en (−4, 7). ¿Cuál era el punto original?', '(7, 4)', 'La regla da (−b, a) = (−4, 7), así que b = 4 y a = 7.'),
    ],
    ctx=('abc', 'Un logotipo tiene un vértice en (2, 5). Se dibuja un patrón con rotaciones sucesivas de 90° antihorarias respecto del origen. ¿Dónde queda ese vértice tras 3 rotaciones seguidas?', '(5, −2)', '(−5, 2)', '(−2, −5)', 'Los giros dan (−5, 2), luego (−2, −5) y luego (5, −2); (−5, 2) es solo la primera rotación.'),
    sc=[
        ("En Geometría: ¿qué coordenada cambia de signo en la reflexión en el eje x?", "La coordenada y", "El eje x queda fijo, así que x se mantiene."),
        ("¿Qué transformación invierte la orientación de una figura?", "La reflexión", "Traslación y rotación conservan el sentido del recorrido."),
        ("¿Basta comprobar que dos puntos están a igual distancia del centro para validar una rotación?", "No", "También hay que revisar el sentido y el ángulo del giro."),
    ],
    op=("Elige una figura: el segmento de extremos (1, 2) y (3, 6) o el triángulo de vértices (2, 0), (5, 0) y (2, 4). Aplícale una reflexión en el eje y y después una rotación de 90° antihoraria con centro en el origen. Escribe todas las imágenes y comprueba con una longitud que la figura final es congruente con la original.",
        "Segmento: reflexión en el eje y da (−1, 2) y (−3, 6); la rotación (x, y) → (−y, x) da (−2, −1) y (−6, −3). Las diferencias de coordenadas pasan de (2, 4) a (−4, −2), y 2² + 4² = 4² + 2², así que la longitud es la misma.",
        ["aplica las dos transformaciones a todos los puntos", "compara una longitud con Pitágoras", "indica qué se conserva y qué cambia"],
        ["hoja con la tabla de puntos originales, intermedios y finales"],
        ["cambiar el signo de la coordenada equivocada", "rotar en sentido horario", "olvidar un vértice"],
        "Pregunta: «¿qué regla usaste en cada paso?». Si falla el sentido, pídele que ubique el punto en el cuadrante esperado."),
    reinforce="Dibuja el triángulo de la ficha en papel cuadriculado y marca su imagen por la reflexión en el eje x; comprueba con regla que los lados miden igual.",
    extend="Explica por qué una reflexión seguida de otra reflexión en una recta distinta del eje conserva la orientación.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (de ejemplo). Triángulo PQR con P(2, 1), Q(6, 1) y R(6, 4); PQ = 4, QR = 3 y PR = 5 unidades, y su área es 6 unidades cuadradas. "
     "Homotecia con centro O(0, 0) y razón k: cada punto (x, y) pasa a (kx, ky). Con otro centro C se usa P′ = C + k · (P − C).")
build(
    O1, 3, F,
    use="Aprenderé a aplicar una homotecia con un vector desde su centro, a interpretar la razón k y a argumentar qué se conserva y qué cambia.",
    prior=["Sé que dos figuras semejantes tienen la misma forma y distinto tamaño.", "Sé multiplicar números enteros y fracciones simples.", "Sé restar puntos para obtener un vector."],
    explain=[
        "Una homotecia es una transformación con un centro C y una razón k (distinta de 0). Cada punto P pasa a P′ sobre la recta que une C con P, de modo que el vector CP′ es k veces el vector CP. Si |k| > 1 la figura se amplía; si 0 < |k| < 1 se reduce; si k < 0 la imagen queda al otro lado del centro.",
        "Con centro en el origen basta multiplicar: (x, y) → (kx, ky). Con otro centro C se hace en tres pasos: se calcula el vector P − C, se multiplica por k y se suma C. La homotecia no es una isometría, salvo si k = 1 o k = −1: las longitudes se multiplican por |k|, los ángulos se conservan, y el área se multiplica por k².",
        "Para argumentar si una solución con homotecia es válida, comprueba tres cosas: que el centro y la imagen estén alineados, que la razón de las longitudes sea |k| y que los ángulos no cambien. Las figuras que se relacionan por una homotecia son semejantes, pero que dos figuras sean semejantes no asegura que sean isometrías una de la otra.",
    ],
    vocab=[("homotecia", "transformación que amplía o reduce desde un centro con una razón k"), ("razón de homotecia", "número k por el que se multiplican las distancias al centro"), ("centro de homotecia", "punto fijo desde el cual se amplía o reduce"), ("semejantes", "de igual forma y tamaño distinto"), ("alineados", "sobre una misma recta"), ("ampliación", "homotecia con |k| mayor que 1")],
    worked=[
        ("Centro en el origen", "Aplica la homotecia de centro O y razón 3 al punto (1, −2).", ["Multiplica cada coordenada por 3: 1 · 3 = 3.", "Multiplica la otra: −2 · 3 = −6."], "La imagen es (3, −6)"),
        ("Centro distinto del origen", "Aplica la homotecia de centro C(1, 1) y razón 2 al punto P(3, 2).", ["Calcula P − C = (2, 1) y multiplica por 2: (4, 2).", "Suma el centro: (4 + 1, 2 + 1) = (5, 3)."], "P′ = (5, 3)"),
    ],
    mistakes=[("Multiplicar las coordenadas por k cuando el centro no es el origen.", "La fórmula con centro C parte del vector P − C, no de P.", "Resta el centro, multiplica por k y vuelve a sumar el centro."),
              ("Pensar que el área se multiplica por k.", "El área depende de dos longitudes, así que se multiplica por k · k.", "Para el área usa k²; para las longitudes, |k|.")],
    T=[
        ('abc', '¿Qué ocurre con los ángulos en una homotecia?', 'Se conservan igual que en el original', 'Se multiplican por la razón k', 'Se invierten siempre', 'La homotecia da figuras semejantes: cambia el tamaño, pero los ángulos no se alteran.'),
        ('abc', '{F} Con k = 2, ¿cuál es la imagen de Q?', '(12, 2)', '(8, 3)', '(12, 1)', 'Se multiplican las dos coordenadas: 6 · 2 y 1 · 2; (8, 3) suma k y (12, 1) olvida multiplicar la y.'),
        ('ab', 'Una homotecia de razón 1/2, ¿qué hace con las longitudes?', 'Las reduce a la mitad', 'Las duplica', 'Una razón entre 0 y 1 reduce, porque cada distancia al centro se multiplica por 1/2.'),
        ('=', '{F} Con k = 3, ¿cuánto mide P′Q′?', '4*3', 'Las longitudes se multiplican por la razón; PQ mide 4.', ' unidades'),
        ('{F} Con k = −1 y centro en el origen, ¿cuál es la imagen de R?', '(−6, −4)', 'La razón −1 cambia el signo de las dos coordenadas: R(6, 4) pasa a (−6, −4).'),
        ('=', '{F} Con k = 3, ¿cuál es el área del triángulo imagen?', '6*3*3', 'El área se multiplica por k al cuadrado, es decir, por 9.', ' unidades cuadradas'),
        ('Homotecia con centro C(1, 1) y razón 3. ¿Cuál es la imagen del punto A(2, 4)?', '(4, 10)', 'A − C = (1, 3); multiplicado por 3 da (3, 9); sumando C resulta (4, 10).'),
        ('abc', 'Con centro C(1, 1) y k = 2, un estudiante calculó la imagen de P(4, 3) y escribió (8, 6). ¿Qué error cometió?', 'Multiplicó las coordenadas de P sin restar ni sumar el centro', 'Sumó k a cada coordenada de P', 'Usó la razón −2 en lugar de 2', 'La imagen correcta es (7, 5); (8, 6) sale de 4 · 2 y 3 · 2, ignorando el centro.'),
        ('=', 'Una fachada real mide 12 m de ancho. Su maqueta es una homotecia de razón 1/4. ¿Cuántos metros de ancho mide la maqueta?', '12//4', 'La razón 1/4 divide las longitudes por 4.', ' m'),
        ('abc', 'Una estudiante dice que toda homotecia es una isometría porque conserva la forma, y otra que no lo es salvo si k = 1 o k = −1. ¿Quién tiene razón?', 'La segunda: las longitudes se multiplican por |k|', 'La primera: conservar la forma es lo mismo que conservar longitudes', 'Ninguna: la homotecia cambia los ángulos', 'Una isometría conserva longitudes; la homotecia solo conserva la forma y, si |k| ≠ 1, cambia las longitudes.'),
        ('abc', 'Los puntos O(0, 0), P(2, 1) y P′(6, 3) están alineados. ¿Pueden ser un punto y su imagen en una homotecia de centro O?', 'Sí, con k = 3, porque P′ = 3 · P', 'No, porque P′ tiene coordenadas mayores que P', 'Sí, pero solo si la razón es 6', 'Cada coordenada de P′ es 3 veces la de P, así que el centro, P y P′ están alineados con razón 3.'),
        ('Una homotecia amplía un triángulo y su área pasa de 5 a 45 unidades cuadradas. ¿Cuál es la razón positiva k?', '3', 'El área se multiplica por k²: 45 ÷ 5 = 9 y la raíz positiva de 9 es 3.'),
        ('Una homotecia de centro O lleva el punto (2, 6) al punto (−1, −3). ¿Cuál es la razón k?', '−1/2', 'Se cumple 2k = −1 y 6k = −3, y las dos ecuaciones dan k = −1/2.'),
    ],
    ctx=('=', 'Un editor digital amplía un rectángulo de 4 cm por 5 cm con una homotecia de razón 3 y centro en una esquina. ¿Cuál es el área de la imagen?', '4*5*3*3', 'El área original es 4 · 5 y se multiplica por la razón al cuadrado.', ' cm²'),
    sc=[
        ("En Geometría: ¿por cuánto se multiplican las longitudes en una homotecia de razón k?", "Por |k|", "La razón mide cuánto se alejan o se acercan las distancias al centro."),
        ("¿Por cuánto se multiplica el área?", "Por k²", "El área depende de dos longitudes."),
        ("¿Qué se hace primero para homotecia con centro C distinto del origen?", "Restar el centro al punto", "Se trabaja con el vector P − C antes de multiplicar."),
    ],
    op=("Elige el triángulo de vértices (1, 1), (3, 1) y (3, 2), o el segmento de extremos (−2, 0) y (2, 4). Aplica una homotecia de centro el origen y razón 2, y otra de razón −1. Escribe las imágenes y explica con una longitud y con el área (o con la longitud) qué se conserva y qué cambia.",
        "Segmento: con k = 2 quedan (−4, 0) y (4, 8); con k = −1 quedan (2, 0) y (−2, −4). La longitud original es la hipotenusa de 4 y 4; con k = 2 las diferencias son 8 y 8, el doble; con k = −1 las diferencias siguen siendo 4 y 4.",
        ["aplica la razón a todos los puntos", "compara longitudes antes y después", "distingue razón 2 (cambia tamaño) y razón −1 (no cambia tamaño)"],
        ["tabla con puntos originales e imágenes y dos frases de comparación"],
        ["sumar k en vez de multiplicar", "olvidar el signo de la razón negativa", "decir que el área se duplica con k = 2"],
        "Pregunta: «¿por cuánto se multiplicó la longitud?». Si dice 4 con k = 2 en una longitud, revisa qué mide."),
    reinforce="Dibuja en papel cuadriculado el triángulo de la ficha y su imagen con k = 2; verifica con regla que cada lado se duplica.",
    extend="Explica por qué la homotecia de razón −1 es una isometría y qué otra isometría produce el mismo resultado.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (de ejemplo). Punto A(2, 1). T es la traslación con vector (3, 0); G es la rotación de 90° antihoraria con centro O: (x, y) → (−y, x); "
     "H es la homotecia con centro O y razón 2. «X luego Y» significa aplicar primero X y después Y.")
build(
    O1, 4, F,
    use="Aprenderé a combinar transformaciones, a notar que el orden importa y a argumentar qué propiedades se conservan en cada composición.",
    prior=["Sé aplicar una traslación, una reflexión, una rotación y una homotecia a un punto.", "Sé que las isometrías conservan longitudes y ángulos.", "Sé que la homotecia multiplica las longitudes por |k|."],
    explain=[
        "Una composición es aplicar una transformación y, al resultado, aplicarle otra. Se escribe «T luego G» cuando primero se hace T. En general el orden importa: «T luego G» y «G luego T» suelen dar imágenes distintas. Por eso, al argumentar una solución con varios pasos, siempre se declara el orden.",
        "Para decidir qué propiedades se conservan en una composición, se analiza cada paso. Si todos los pasos son isometrías, la composición también lo es y conserva longitudes y ángulos. Si aparece una homotecia de razón k, las longitudes se multiplican por |k|, el área por k² y los ángulos se mantienen; la composición de homotecias con el mismo centro tiene como razón el producto de las razones.",
        "Una buena argumentación usa un contraejemplo cuando una afirmación general es falsa. Para mostrar que dos composiciones no son iguales basta un punto que termine en lugares distintos. Para mostrar que una composición es isometría hay que justificar que ningún paso cambia las longitudes.",
    ],
    vocab=[("composición", "aplicar una transformación y luego otra"), ("orden", "secuencia en que se aplican las transformaciones"), ("identidad", "transformación que deja todos los puntos en su lugar"), ("razón total", "producto de las razones de homotecias seguidas"), ("propiedad invariante", "propiedad que no cambia con la transformación"), ("contraejemplo", "caso que muestra que una afirmación general es falsa")],
    worked=[
        ("Composición paso a paso", "Aplica «T luego G» al punto B(0, 2), con T = traslación (3, 0) y G = rotación de 90° antihoraria con centro O.", ["T: (0 + 3, 2 + 0) = (3, 2).", "G: (x, y) → (−y, x) da (−2, 3)."], "B″ = (−2, 3)"),
        ("Contraejemplo del orden", "Alguien dice que «T luego H» da lo mismo que «H luego T» para el punto C(1, 0). Con T = (3, 0) y H = razón 2, ¿es cierto?", ["T luego H: (1, 0) → (4, 0) → (8, 0).", "H luego T: (1, 0) → (2, 0) → (5, 0)."], "No: (8, 0) ≠ (5, 0), el orden importa"),
    ],
    mistakes=[("Aplicar las transformaciones en el orden en que se leen sin fijarse en el «luego».", "«X luego Y» significa que X va primero.", "Escribe la imagen intermedia después de cada paso."),
              ("Creer que si un paso es homotecia, la composición completa conserva las longitudes.", "La homotecia multiplica las longitudes por |k|.", "Revisa cada paso: basta una homotecia con |k| ≠ 1 para cambiar el tamaño.")],
    T=[
        ('{F} ¿Cuál es la imagen de A por «T luego G»?', '(−1, 5)', 'T lleva A a (5, 1) y G lo lleva a (−1, 5).'),
        ('abc', '¿Cuál de estas transformaciones no conserva las longitudes?', 'Una homotecia de razón 3', 'Una rotación de 90°', 'Una reflexión en el eje x', 'La homotecia con |k| ≠ 1 multiplica las longitudes; rotación y reflexión son isometrías.'),
        ('ab', 'La composición de una traslación y una rotación, ¿es una isometría?', 'Sí, porque ninguno de los dos pasos cambia las longitudes', 'No, porque dos transformaciones distintas siempre deforman la figura', 'Una composición de isometrías conserva longitudes y ángulos paso a paso.'),
        ('{F} ¿Cuál es la imagen de A por «G luego T»?', '(2, 2)', 'G lleva A a (−1, 2) y T suma 3 a x, dando (2, 2).'),
        ('abc', '{F} ¿Cuál es la imagen de A por «H luego T»?', '(7, 2)', '(10, 2)', '(7, 4)', 'H lleva A a (4, 2) y T suma 3 a x: (7, 2); (10, 2) sería «T luego H».'),
        ('=', 'Una figura de área 7 pasa por una homotecia de razón 2 y luego por otra de razón 3, ambas con centro O. ¿Cuál es el área final?', '7*6*6', 'La razón total es 2 · 3 = 6 y el área se multiplica por 6².', ' unidades cuadradas'),
        ('Aplica «T luego H» al punto B(1, −1) con las definiciones de la ficha: traslación (3, 0) y homotecia de razón 2 con centro O. ¿Dónde queda?', '(8, −2)', 'T lleva B a (4, −1) y H duplica las coordenadas, dando (8, −2).'),
        ('abc', 'Una figura de 3 cm de lado queda con 9 cm de lado y la misma forma. ¿Qué transformación pudo usarse?', 'Una homotecia de razón 3', 'Una rotación de 90°', 'Una traslación', 'Solo una homotecia cambia el tamaño conservando la forma; las otras dos conservan las longitudes.'),
        ('=', 'Un triángulo de lados 5, 12 y 13 se rota, se traslada y luego se amplía con una homotecia de razón 2. ¿Cuál es el perímetro final?', '(5+12+13)*2', 'Rotación y traslación conservan el perímetro, y la homotecia lo multiplica por 2.', ' unidades'),
        ('abc', 'Una estudiante dice que «T luego G» es siempre igual a «G luego T» porque son las mismas dos transformaciones. ¿Qué argumento lo refuta?', 'Con A(2, 1) da (−1, 5) en un orden y (2, 2) en el otro', 'Que T y G son isometrías', 'Que G tiene su centro en el origen', 'Un contraejemplo basta: el mismo punto termina en lugares distintos según el orden.'),
        ('abc', 'Un programa muestra la figura transformada y afirma «es una isometría porque quedó semejante a la original». ¿Qué falta para sostener esa afirmación?', 'Comprobar que la razón de las longitudes es 1', 'Nada: semejante e isometría significan lo mismo', 'Comprobar que la figura cambió de posición', 'Semejante permite cambiar el tamaño; una isometría exige conservar las longitudes, razón 1.'),
        ('Dos homotecias con el mismo centro tienen razones 2 y −3 y se aplican una después de otra. ¿Cuál es la razón de la homotecia única equivalente?', '−6', 'Se multiplican las razones: 2 · (−3) = −6.'),
        ('La rotación de 90° antihoraria con centro O se aplica cuatro veces seguidas a A(2, 1). ¿Dónde queda A y a qué transformación equivale el conjunto?', '(2, 1): equivale a la identidad (giro de 360°)', 'Los giros dan (−1, 2), (−2, −1), (1, −2) y (2, 1); cuatro giros de 90° suman una vuelta completa.'),
    ],
    ctx=('abc', 'Un diseñador necesita llevar un logo triangular a otra posición, del mismo tamaño y con orientación en espejo. ¿Qué composición usa?', 'Una reflexión seguida de una traslación', 'Una homotecia de razón 2', 'Dos traslaciones seguidas', 'La reflexión invierte la orientación y la traslación cambia la posición sin alterar el tamaño; dos traslaciones no dan espejo.'),
    sc=[
        ("En Geometría: ¿qué significa «X luego Y»?", "Se aplica primero X y después Y", "El orden de lectura indica el orden de aplicación."),
        ("¿Qué razón total tienen dos homotecias seguidas con el mismo centro?", "El producto de sus razones", "Las distancias se multiplican paso a paso."),
        ("¿Cómo se refuta que dos composiciones sean iguales?", "Con un punto que termine en lugares distintos", "Un contraejemplo basta para invalidar una afirmación general."),
    ],
    op=("Elige el punto K(1, 2) o el punto L(−2, 1). Con la traslación (2, 3) y la rotación de 90° antihoraria con centro en el origen, calcula «traslación luego rotación» y «rotación luego traslación». Escribe si el resultado es igual y qué propiedad se conservó en cada composición.",
        "K(1, 2): traslación luego rotación: (3, 5) → (−5, 3). Rotación luego traslación: (−2, 1) → (0, 4). Son distintos, así que el orden importa. Ambas conservan las longitudes porque solo usan isometrías.",
        ["calcula los dos órdenes con imágenes intermedias", "concluye si coinciden", "nombra una propiedad conservada y por qué"],
        ["hoja con los dos recorridos y la conclusión"],
        ["aplicar los pasos en otro orden", "olvidar la imagen intermedia", "decir que son iguales sin calcular"],
        "Pregunta: «¿cuál fue tu punto después del primer paso?». Pídele esa imagen intermedia antes de seguir."),
    reinforce="Elige un punto de coordenadas enteras y calcula dos veces «reflexión luego traslación» y «traslación luego reflexión»; compara.",
    extend="Explica por qué la composición de dos rotaciones del mismo centro se puede escribir como una sola rotación.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (de ejemplo). Problema: llevar el triángulo ABC, con A(1, 1), B(5, 1) y C(5, 4), a un triángulo A″B″C″ con las mismas medidas y con A″(−1, 3) y B″(3, 3). "
     "Solución 1: traslación con v = (−2, 2). Solución 2: rotación de 90° antihoraria con centro O y luego traslación (0, 2). "
     "Solución 3: homotecia de razón 2 con centro O. Solución 4: reflexión en el eje x y luego traslación (−2, 4). "
     "Una hoja de cálculo tendría columnas x, y, x″, y″ y una columna con la distancia entre los puntos; aquí se calcula a mano.")
build(
    O1, 5, F,
    use="Aprenderé a comparar varias soluciones de un mismo problema, a validarlas con condiciones, vectores y tablas de coordenadas, y a declarar hasta dónde vale cada comprobación.",
    prior=["Sé aplicar traslaciones, reflexiones, rotaciones y homotecias.", "Sé calcular el vector entre dos puntos.", "Sé organizar coordenadas en una tabla."],
    explain=[
        "Un problema geométrico trae condiciones: qué figura se mueve, qué medidas deben conservarse, cuáles puntos deben quedar en un lugar dado. Una solución es válida solo si cumple todas esas condiciones. Para comprobar, se escribe una tabla con cada vértice original y su imagen, se calcula el vector o la regla que usa cada punto y se compara.",
        "Una representación digital, como una hoja de cálculo o un programa de geometría dinámica, permite repetir cálculos y ver la figura, pero no reemplaza la justificación. Una imagen en pantalla «se ve igual» aunque difiera en una fracción pequeña, y un programa redondea. Por eso se declara el alcance de la comprobación: qué puntos se revisaron y qué se supuso.",
        "Puede haber más de una solución válida si el problema no fija todas las condiciones, y puede no haber ninguna. Para descartar una solución basta un contraejemplo: un vértice que no llega donde se pide o una longitud que cambia. Para aceptar una solución hay que revisar todos los vértices y las medidas pedidas.",
    ],
    vocab=[("condición", "exigencia que debe cumplir una solución"), ("comprobación", "revisión de que una solución cumple las condiciones"), ("tabla de coordenadas", "lista de puntos originales e imágenes"), ("representación digital", "hoja de cálculo o programa de geometría dinámica"), ("alcance", "hasta dónde vale una comprobación"), ("solución válida", "la que cumple todas las condiciones")],
    worked=[
        ("Validar con una tabla", "El problema pide A → A″(0, 4) y B → B″(4, 4) para A(1, 1) y B(5, 1). Una persona propone la traslación (−1, 3). ¿Es válida?", ["Calcula A″ − A = (−1, 3) y B″ − B = (−1, 3): el mismo vector.", "Comprueba la longitud: AB = 4 y A″B″ = 4."], "Sí es válida: mismo vector en ambos puntos y misma longitud"),
        ("Descartar con un contraejemplo", "Para el mismo problema alguien propone una homotecia de razón 2 con centro O. ¿Qué punto la descarta?", ["A(1, 1) pasa a (2, 2), que no es (0, 4).", "Además AB mediría 8 y no 4."], "No es válida: A no llega a (0, 4)"),
    ],
    mistakes=[("Aceptar una solución porque coincide con el primer vértice.", "Una coincidencia en un punto no prueba que los demás también lleguen.", "Revisa todos los vértices y al menos una longitud."),
              ("Decir «en la pantalla se ve igual» como prueba.", "La vista puede ocultar diferencias pequeñas y no entrega las coordenadas.", "Respalda con cálculos, con la tabla de coordenadas o con distancias.")],
    T=[
        ('abc', '{F} ¿Qué vector lleva A a A″?', '(−2, 2)', '(2, −2)', '(−1, 3)', 'Se calcula A″ − A = (−1 − 1, 3 − 1); (2, −2) es el opuesto y (−1, 3) es el propio A″.'),
        ('abc', '{F} Una persona dice que la solución 1 es válida porque A llega a A″. ¿Qué debe revisarse además?', 'Que B y C usen el mismo vector y B llegue a B″', 'Nada más, porque un punto basta', 'Solo el color de la figura en pantalla', 'La traslación se valida con todos los vértices y con las condiciones pedidas, no con un punto.'),
        ('ab', 'En una comprobación, un solo vértice no cumple la regla. ¿Qué se concluye?', 'La solución no es válida: un contraejemplo basta', 'La solución es válida porque la mayoría coincide', 'Las condiciones del problema exigen todos los vértices, no la mayoría.'),
        ('{F} Aplica el vector (−2, 2) al vértice C. ¿Dónde queda C″?', '(3, 6)', 'C(5, 4) más (−2, 2) da (3, 6).'),
        ('=', '{F} En la solución 1, el triángulo A″B″C″ tiene catetos 4 y 3. ¿Cuál es su área?', '4*3//2', 'La traslación conserva el área: base por altura dividido en dos.', ' unidades cuadradas'),
        ('abc', '{F} La solución 3 deja A en (2, 2). ¿Por qué no puede ser válida?', 'Porque duplica las longitudes y el problema exige las mismas medidas', 'Porque la homotecia siempre invierte la orientación', 'Porque A no tiene coordenadas negativas', 'La homotecia de razón 2 cambia el tamaño; el problema pide una figura congruente a ABC.'),
        ('{F} Verifica la solución 2: ¿dónde queda B tras la rotación y la traslación?', '(−1, 7)', 'La rotación lleva B(5, 1) a (−1, 5) y la traslación (0, 2) lo lleva a (−1, 7).'),
        ('abc', '{F} Con el resultado de la pregunta anterior, ¿qué se concluye de la solución 2?', 'No es válida: B″ queda en (−1, 7) y se pedía (3, 3)', 'Es válida porque conserva las longitudes', 'Es válida porque A llega a A″', 'Una condición del problema es B″(3, 3); una isometría que no la cumple no resuelve el problema.'),
        ('{F} Aplica la solución 4 (reflexión en el eje x y luego traslación (−2, 4)) al vértice C. ¿Dónde queda C″?', '(3, 0)', 'La reflexión lleva C(5, 4) a (5, −4) y la traslación a (3, 0); en la solución 1 C″ quedaba en (3, 6), así que no dan la misma figura.'),
        ('abc', 'Un programa muestra que la figura original y la imagen «se ven iguales». ¿Basta para validar la solución?', 'No: hay que respaldar con coordenadas o distancias calculadas', 'Sí: si se ve igual, las medidas son iguales', 'Sí, siempre que la imagen se vea más grande', 'La vista puede ocultar diferencias pequeñas; la validez se argumenta con cálculos.'),
        ('abc', 'Si solo se pide que A llegue a A″(−1, 3) y que la imagen sea congruente a ABC, ¿cuántas soluciones válidas hay?', 'Muchas: la traslación y otras isometrías que lleven A a A″', 'Una sola: la traslación', 'Ninguna, porque falta un dato', 'Solo se fijó un punto, así que sirven muchas isometrías que lo cumplan, por ejemplo traslación o rotación más traslación.'),
        ('Un colega agrega a la solución 1 una homotecia final de razón 1 con centro O. ¿Sigue siendo válida? Responde sí o no y explica.', 'Sí: la razón 1 deja cada punto en su lugar', 'La homotecia de razón 1 es la identidad: no mueve los puntos ni altera el tamaño, así que A″ y B″ siguen donde se pedía.'),
        ('Se agrega al problema la condición «la orientación debe quedar invertida». ¿Qué transformación debe aparecer en la solución?', 'Una reflexión', 'Solo la reflexión (o un número impar de reflexiones) invierte el sentido del recorrido de los vértices.'),
    ],
    ctx=('abc', 'Un estudiante de diseño comprueba en una hoja de cálculo que la distancia entre dos puntos es 5 antes y 5 después, pero solo revisó ese par. ¿Qué debe hacer para argumentar que la transformación es una isometría?', 'Revisar más pares de puntos y declarar el alcance de su comprobación', 'Dar por válida la transformación porque ya hay una distancia que coincide', 'Cambiar la tabla hasta que todas las distancias coincidan', 'Una coincidencia aislada no prueba una isometría; se amplía la comprobación y se declara qué se revisó.'),
    sc=[
        ("En Geometría: ¿cuántos contraejemplos bastan para invalidar una solución?", "Uno", "Un vértice que no cumple la condición ya la descarta."),
        ("¿Qué condición revisas en una isometría, además de la posición?", "Que las longitudes se conserven", "Una isometría conserva las longitudes y los ángulos de la figura."),
        ("¿Una imagen que «se ve igual» en pantalla prueba que la solución es válida?", "No", "La vista puede ocultar diferencias; se respalda con cálculos."),
    ],
    op=("Resuelve este problema: llevar el triángulo con vértices (0, 0), (4, 0) y (4, 3) a otro con las mismas medidas que tenga como vértice (2, 5) en el lugar del (0, 0) y cuya imagen del (4, 0) sea (6, 5). Elige una de las dos soluciones siguientes y valídala o descártala con una tabla de coordenadas: Solución A: traslación (2, 5). Solución B: homotecia de razón 2 con centro O. Declara el alcance de tu comprobación.",
        "Solución A: (0, 0) → (2, 5), (4, 0) → (6, 5), (4, 3) → (6, 8). Todos usan (2, 5), así que cumple. La longitud del lado de (0, 0) a (4, 0) es 4 y la de (2, 5) a (6, 5) también. Alcance: revisé los tres vértices y una longitud; no usé programa.",
        ["calcula las imágenes de todos los vértices", "compara con las condiciones del problema", "declara qué comprobó y qué supuso"],
        ["tabla de coordenadas, conclusión y frase de alcance"],
        ["validar con un solo punto", "no comparar con las condiciones", "afirmar sin declarar el alcance"],
        "Pregunta: «¿qué condición del problema te asegura que la solución sirve?». Si no la nombra, pídele que la subraye en el enunciado."),
    reinforce="Elige un problema de las clases anteriores y escribe una tabla con sus puntos originales e imágenes; marca qué condiciones cumple.",
    extend="Explica por qué una comprobación digital con números redondeados puede dar un resultado que parece válido pero no lo es.",
)
