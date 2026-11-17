"""Geometría 3D (electivo HC, 3.º y 4.º medio): OAC-02 (puntos, rectas y planos en el espacio con vectores), clases 1 a 4. Todo en papel; las representaciones digitales se describen por escrito."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel cuadriculado; calculadora simple opcional. No se necesita software: las representaciones digitales "
             "(geometría dinámica en 3D) se describen en la ficha y se razonan a mano. Si usas un programa, hazlo con la supervisión de tu docente.")
build = make_build(MATERIALS)

O2 = "MA-GE3D-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (de ejemplo). Un cuarto se modela con tres ejes: x e y sobre el suelo y z para la altura, todo en metros. "
     "Hay un anclaje en A(1, 2, 3) y una luminaria en B(3, 5, 9). El origen O(0, 0, 0) es una esquina del suelo.")
build(
    O2, 1, F,
    use="Aprenderé a ubicar puntos en el espacio con tres coordenadas, a calcular vectores, distancias y puntos medios, y a argumentar con ellos.",
    prior=["Sé ubicar puntos (x, y) en el plano.", "Sé aplicar el teorema de Pitágoras en el plano.", "Sé sumar vectores del plano componente a componente."],
    explain=[
        "En el espacio, un punto se ubica con tres coordenadas (x, y, z): x e y dicen dónde está sobre el suelo y z dice la altura. Un vector en el espacio tiene tres componentes (a, b, c). El vector que lleva el punto A al punto B se calcula restando: AB = B − A. El vector opuesto BA = A − B apunta al revés y tiene los mismos números con signo cambiado.",
        "El módulo de un vector es su longitud y se calcula con el teorema de Pitágoras aplicado dos veces: |(a, b, c)| = raíz de (a² + b² + c²). La distancia entre dos puntos es el módulo del vector que los une. Por ejemplo, el vector (1, 2, 2) tiene módulo raíz de (1 + 4 + 4) = 3. Sumar vectores se hace componente a componente, y multiplicar por un número cambia su tamaño sin cambiar la dirección.",
        "El punto medio de un segmento AB tiene como coordenadas el promedio de las coordenadas de A y de B, una por una. Para argumentar que un cálculo es correcto en el espacio se revisan las tres coordenadas, no solo dos; y el módulo se comprueba sumando cuadrados, nunca sumando las componentes. Un programa de geometría dinámica 3D dibujaría los puntos, pero la justificación sigue siendo el cálculo.",
    ],
    vocab=[("coordenadas (x, y, z)", "tres números que ubican un punto en el espacio"), ("vector en el espacio", "flecha con tres componentes (a, b, c)"), ("módulo", "longitud de un vector"), ("distancia entre puntos", "módulo del vector que los une"), ("punto medio", "punto del centro de un segmento; promedio de coordenadas"), ("vector opuesto", "vector con el mismo módulo y sentido contrario")],
    worked=[
        ("Vector y módulo", "Calcula el vector PQ y su módulo para P(2, −1, 4) y Q(4, 1, 5).", ["PQ = Q − P = (4 − 2, 1 − (−1), 5 − 4) = (2, 2, 1).", "Módulo: 4 + 4 + 1 = 9, y la raíz de 9 es 3."], "PQ = (2, 2, 1) y |PQ| = 3"),
        ("Punto medio", "Halla el punto medio de R(−2, 6, 0) y S(4, 2, 8).", ["Promedia x: (−2 + 4) ÷ 2 = 1.", "Promedia y: (6 + 2) ÷ 2 = 4, y z: (0 + 8) ÷ 2 = 4."], "El punto medio es (1, 4, 4)"),
    ],
    mistakes=[("Calcular el módulo sumando las componentes: |(2, 3, 6)| = 2 + 3 + 6.", "La longitud sale del teorema de Pitágoras: se suman los cuadrados y luego se saca la raíz.", "Eleva cada componente al cuadrado, suma y calcula la raíz."),
              ("Calcular AB como A − B.", "El vector hacia B se obtiene con «punto final menos punto inicial».", "Escribe B − A y revisa que la flecha apunte de A hacia B.")],
    T=[
        ('abc', '{F} ¿Cuál es el vector AB?', '(2, 3, 6)', '(−2, −3, −6)', '(4, 7, 12)', 'AB = B − A = (3 − 1, 5 − 2, 9 − 3); (−2, −3, −6) es BA y (4, 7, 12) suma los puntos.'),
        ('abc', '¿Qué indica la coordenada z de un punto en el modelo del cuarto?', 'La altura sobre el suelo', 'La distancia a la pared de la izquierda', 'El ancho del cuarto', 'En este modelo x e y ubican sobre el suelo y z mide la altura.'),
        ('ab', 'El módulo del vector (a, b, c) se calcula como:', 'La raíz de a² + b² + c²', 'La suma a + b + c', 'La longitud proviene de Pitágoras: se suman cuadrados y se extrae la raíz.'),
        ('{F} ¿Cuántos metros mide el segmento AB, la distancia entre el anclaje y la luminaria?', '7 m', 'El módulo de (2, 3, 6) es la raíz de 4 + 9 + 36 = 49, es decir, 7.'),
        ('Sean u = (1, −2, 4) y v = (3, 0, −1). ¿Cuál es u + v?', '(4, −2, 3)', 'La suma se hace componente a componente: 1 + 3, −2 + 0 y 4 − 1.'),
        ('Un vector tiene componentes (4, 4, 7). ¿Cuál es su módulo?', '9 unidades', 'Se calcula 16 + 16 + 49 = 81 y la raíz de 81 es 9.'),
        ('Calcula el punto medio de P(2, 4, 6) y Q(8, 0, 2).', '(5, 2, 4)', 'Se promedia cada coordenada: (2 + 8) ÷ 2, (4 + 0) ÷ 2 y (6 + 2) ÷ 2.'),
        ('abc', 'Un dron sale de A(1, 2, 3) y se desplaza con el vector (2, 3, 6). ¿Dónde llega?', '(3, 5, 9)', '(2, 6, 18)', '(−1, −1, −3)', 'La posición final es A + (2, 3, 6); (2, 6, 18) multiplica y (−1, −1, −3) resta.'),
        ('=', 'Un cable une el anclaje A y la luminaria B de la ficha, y mide lo mismo que el segmento AB (7 m). Cada metro de cable cuesta $2.000. ¿Cuánto cuesta el cable en pesos?', '7*2000', 'Se multiplica la longitud del segmento por el precio de cada metro.'),
        ('abc', 'Una estudiante calcula el módulo de (2, 3, 6) como 2 + 3 + 6 = 11. ¿Qué argumento muestra el error?', 'El módulo usa cuadrados: 4 + 9 + 36 = 49 y su raíz es 7, no 11', 'El módulo siempre es igual a la mayor componente', 'El módulo de un vector en el espacio debe ser negativo', 'Pitágoras suma cuadrados; sumar componentes ignora la geometría y da una longitud mayor que la real.'),
        ('abc', 'Si AB = (2, 3, 6), ¿qué relación tiene BA con AB?', 'Mismo módulo y sentido opuesto: BA = (−2, −3, −6)', 'Mismo módulo y mismo sentido', 'Distinto módulo y sentido opuesto', 'BA = A − B = −(B − A), así que invierte el sentido y conserva la longitud.'),
        ('El punto medio de AB es M(4, 1, 2) y A = (1, −2, 0). ¿Cuáles son las coordenadas de B?', '(7, 4, 4)', 'Como M es el promedio, B = 2M − A = (8 − 1, 2 + 2, 4 − 0).'),
        ('Un punto B(4, 4, z) con z > 0 está a 9 unidades del origen. ¿Cuánto vale z?', '7', 'Se cumple 16 + 16 + z² = 81, así que z² = 49 y z = 7.'),
    ],
    ctx=('abc', 'Un proyecto ubica un anclaje en el origen y una luminaria en L(2, 6, 9), en metros. ¿A qué distancia en línea recta están?', '11 m', '17 m', '9 m', 'El módulo es la raíz de 4 + 36 + 81 = 121, es decir, 11; 17 suma las componentes y 9 es solo la altura.'),
    sc=[
        ("En Geometría 3D: ¿cómo se calcula el vector que va de A a B?", "B − A", "Se resta el punto de partida al punto de llegada."),
        ("¿Qué se hace con las componentes para hallar el módulo?", "Se elevan al cuadrado, se suman y se saca la raíz", "Es el teorema de Pitágoras en tres dimensiones."),
        ("¿Cómo se obtiene el punto medio de un segmento?", "Promediando cada coordenada", "El centro queda a medio camino en x, en y y en z."),
    ],
    op=("Elige un caso: (a) un faro en A(0, 0, 4) y un barco en B(2, 4, 0) con vector AB, módulo y punto medio; (b) un dron en C(1, 1, 1) que se mueve con el vector (2, 4, 4) hasta D. Calcula el vector, su módulo (o la posición final y el módulo del desplazamiento) y el punto medio, y escribe una frase que justifique cada resultado.",
        "Caso (b): D = C + (2, 4, 4) = (3, 5, 5). El módulo del desplazamiento es la raíz de 4 + 16 + 16 = 36, es decir, 6. El punto medio de CD es (2, 3, 3), calculado promediando cada coordenada.",
        ["calcula el vector con punto final menos inicial", "usa Pitágoras con tres componentes", "obtiene el punto medio por promedio de coordenadas"],
        ["hoja con los cálculos y una frase por resultado"],
        ["sumar componentes en vez de cuadrados", "restar al revés", "olvidar la coordenada z"],
        "Pregunta: «¿qué punto resta a cuál?». Si el sentido es el opuesto, pídele que dibuje la flecha."),
    reinforce="Con una caja de zapatos como modelo, nombra tres esquinas con coordenadas (x, y, z) en cm y calcula la distancia entre dos de ellas.",
    extend="Explica por qué la distancia entre dos puntos del espacio se parece a la del plano y qué término se agrega.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (de ejemplo). Recta L: P(t) = (1, 2, 0) + t · (2, 3, 6), con t un número real. Recta M: Q(s) = (0, 0, 5) + s · (4, 6, 12). "
     "Recta N: R(u) = (1, 2, 0) + u · (1, −1, 0). El vector (2, 3, 6) tiene módulo 7.")
build(
    O2, 2, F,
    use="Aprenderé a describir una recta del espacio con un punto y un vector director, a decidir si un punto está en ella y a clasificar dos rectas.",
    prior=["Sé calcular vectores y módulos en el espacio.", "Sé multiplicar un vector por un número.", "Sé resolver ecuaciones lineales sencillas."],
    explain=[
        "Una recta del espacio se describe con un punto A y un vector director d: sus puntos son P(t) = A + t · d, donde t es cualquier número real. Cuando t = 0 se obtiene A; si t = 1 se obtiene A + d, y así sucesivamente. El vector director da la dirección; cualquier múltiplo distinto de cero del mismo vector describe la misma dirección.",
        "Para saber si un punto X está en la recta se resuelve X = A + t · d: la misma t debe servir en las tres coordenadas. Si una coordenada pide t = 3 y otra pide t = 1, el punto no pertenece. Dos rectas son paralelas si sus vectores directores son múltiplos entre sí. Si no son paralelas, pueden cortarse en un punto, o ser alabeadas: ni paralelas ni con puntos comunes, algo que solo ocurre en el espacio.",
        "Para argumentar la validez de una solución se muestra el valor de t (o de s y u) que se usó y se comprueban las tres coordenadas. Una representación en geometría dinámica 3D puede girar la figura para ver si las rectas parecen cortarse, pero «parecen» no basta: se resuelve el sistema con los números.",
    ],
    vocab=[("recta en el espacio", "conjunto de puntos A + t · d"), ("vector director", "vector que indica la dirección de la recta"), ("parámetro t", "número real que recorre los puntos de la recta"), ("paralelas", "rectas con vectores directores múltiplos entre sí"), ("secantes", "rectas que se cortan en un punto"), ("alabeadas", "rectas del espacio que ni son paralelas ni se cortan")],
    worked=[
        ("Punto de la recta", "Halla el punto de L con t = 2.", ["x: 1 + 2 · 2 = 5.", "y: 2 + 3 · 2 = 8, y z: 0 + 6 · 2 = 12."], "(5, 8, 12)"),
        ("Pertenencia", "¿Está (7, 11, 18) en L?", ["De x: 1 + 2t = 7, entonces t = 3.", "Con t = 3: y = 2 + 9 = 11 y z = 18, que coinciden."], "Sí, con t = 3 en las tres coordenadas"),
    ],
    mistakes=[("Usar un valor de t distinto para cada coordenada.", "La recta tiene un solo parámetro: el mismo t debe servir en x, y y z.", "Despeja t con una coordenada y comprueba las otras dos."),
              ("Decir que dos rectas no paralelas siempre se cortan.", "En el espacio pueden ser alabeadas.", "Para saber si se cortan, iguala las coordenadas y comprueba que haya solución.")],
    T=[
        ('abc', '{F} ¿Cuál es el vector director de la recta L?', '(2, 3, 6)', '(1, 2, 0)', '(3, 5, 6)', 'En P(t) = A + t · d el vector director es el que multiplica a t; (1, 2, 0) es el punto de partida.'),
        ('abc', '{F} ¿Qué punto de L corresponde a t = 0?', '(1, 2, 0)', '(2, 3, 6)', '(0, 0, 0)', 'Con t = 0 el término t · d vale cero y queda el punto A.'),
        ('ab', 'Dos rectas con vectores directores (1, 2, 3) y (3, 6, 9) son:', 'Paralelas o coincidentes, porque un vector es 3 veces el otro', 'Alabeadas, porque los vectores son distintos', 'Los vectores directores son múltiplos, lo que implica que las rectas tienen igual dirección.'),
        ('{F} Calcula el punto de L con t = −2.', '(−3, −4, −12)', 'Se calcula (1 − 4, 2 − 6, 0 − 12) usando t = −2 en cada componente.'),
        ('abc', '{F} ¿Pertenece el punto (3, 5, 6) a L?', 'Sí, con t = 1 en las tres coordenadas', 'No, porque x = 3 no es múltiplo de 2', 'Sí, porque tiene tres coordenadas', 'Con t = 1: 1 + 2 = 3, 2 + 3 = 5 y 0 + 6 = 6, así que coincide en todas.'),
        ('=', '{F} ¿Cuál es la coordenada z del punto de L con t = 5?', '0+6*5', 'La tercera componente es 0 + 6t y se evalúa en t = 5.'),
        ('{F} ¿Pertenece (4, 3, 5) a L? Responde sí o no y explica con t.', 'No: x pide t = 3/2 e y pide t = 1/3', 'De 1 + 2t = 4 sale t = 3/2 y de 2 + 3t = 3 sale t = 1/3; no coinciden.'),
        ('abc', '{F} ¿Qué relación tienen las rectas L y M?', 'Paralelas distintas', 'Secantes en (1, 2, 0)', 'Alabeadas', 'Sus directores (2, 3, 6) y (4, 6, 12) son múltiplos, y M no pasa por (1, 2, 0): x pide s = 1/4 e y pide s = 1/3, que no coinciden.'),
        ('=', '{F} El vector director de L tiene módulo 7. ¿Qué distancia hay entre los puntos de L con t = 0 y con t = 3?', '3*7', 'El desplazamiento entre ambos puntos es 3 · d, de módulo 3 por 7.', ' unidades'),
        ('abc', 'Para decidir si un punto está en una recta, un estudiante usa t = 1 en x, t = 2 en y y t = 3 en z. ¿Qué error comete?', 'Debe usar el mismo valor de t en las tres coordenadas', 'Debe usar solo la coordenada z', 'Debe usar valores de t negativos', 'La recta tiene un único parámetro, así que el mismo t debe cumplir las tres ecuaciones.'),
        ('abc', 'En el plano, dos rectas no paralelas siempre se cortan. ¿Qué ocurre en el espacio?', 'Pueden no cortarse y no ser paralelas: son alabeadas', 'Siempre se cortan igual que en el plano', 'Nunca se cortan', 'En 3D hay una dirección más, así que dos rectas pueden pasar una «por encima» de la otra sin tocarse.'),
        ('{F} ¿Se cortan las rectas L y N? Si es así, ¿en qué punto?', 'Sí: en (1, 2, 0), con t = 0 y u = 0', 'De z: 6t = 0 da t = 0; entonces x e y coinciden con u = 0 en el punto (1, 2, 0).'),
        ('{F} ¿Qué valor de a hace que el punto (a, 8, 12) esté en L?', '5', 'De y: 2 + 3t = 8 da t = 2; z: 6 · 2 = 12 coincide, y x: 1 + 4 = 5.'),
    ],
    ctx=('abc', 'Un dron parte de A(1, 2, 0) y avanza en la dirección (2, 3, 6) metros por minuto. ¿Dónde está a los 4 minutos?', '(9, 14, 24)', '(3, 5, 6)', '(8, 12, 24)', 'La posición es A + 4 · (2, 3, 6); (3, 5, 6) usa un solo minuto y (8, 12, 24) olvida sumar A.'),
    sc=[
        ("En Geometría 3D: ¿qué es el vector director de una recta?", "El vector que da la dirección de la recta", "Todos los puntos se obtienen avanzando múltiplos de ese vector."),
        ("¿Cuántos valores de t se usan para decidir si un punto está en la recta?", "Uno solo", "El mismo parámetro debe servir en las tres coordenadas."),
        ("¿Cómo se llaman las rectas que no son paralelas y no se cortan?", "Alabeadas", "Solo existen en el espacio, donde hay una dirección más."),
    ],
    op=("Elige un caso: (a) la recta que pasa por A(2, 0, 1) con director (1, 2, 2) y los puntos X(5, 6, 7) e Y(4, 3, 4); (b) las rectas (0, 0, 0) + t(1, 0, 0) y (0, 1, 1) + s(0, 1, 0). En (a) decide cuál de los puntos está en la recta; en (b) decide si son paralelas, secantes o alabeadas. Justifica con el valor del parámetro o con las coordenadas.",
        "Caso (b): los directores (1, 0, 0) y (0, 1, 0) no son múltiplos, así que no son paralelas. Si se cortaran, z = 0 y z = 1 deberían coincidir y no coinciden, por lo que no tienen punto común: son alabeadas.",
        ["usa la ecuación con parámetro", "revisa las tres coordenadas", "concluye con la clasificación o con sí/no"],
        ["hoja con las ecuaciones despejadas y la conclusión"],
        ["usar parámetros distintos en cada coordenada", "decir «se ven cortadas» sin cálculo", "olvidar revisar la tercera coordenada"],
        "Pregunta: «¿qué valor de t usaste?». Si usa varios, pídele que lo verifique con una sola t."),
    reinforce="Elige un punto y un vector director de coordenadas pequeñas y escribe cinco puntos de la recta (t = −1, 0, 1, 2, 3).",
    extend="Explica por qué la misma recta se puede escribir con distintos puntos de partida y vectores directores.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (de ejemplo). Plano π: 2x + 3y + 6z = 12. Su vector normal (perpendicular al plano) es n = (2, 3, 6), de módulo 7. "
     "El producto punto es (a, b, c) · (d, e, f) = ad + be + cf. Dos vectores son perpendiculares cuando su producto punto vale 0.")
build(
    O2, 3, F,
    use="Aprenderé a describir un plano con una ecuación y un vector normal, a decidir si un punto está en él y a comparar planos.",
    prior=["Sé calcular vectores y módulos en el espacio.", "Sé describir rectas con un vector director.", "Sé reemplazar valores en una ecuación."],
    explain=[
        "Un plano del espacio se describe con una ecuación ax + by + cz = d. El vector n = (a, b, c) se llama normal porque es perpendicular al plano. Un punto pertenece al plano si, al reemplazar sus coordenadas en la ecuación, se cumple la igualdad. Los puntos donde el plano corta los ejes se hallan haciendo cero las otras dos coordenadas.",
        "Para construir un plano que pasa por un punto A con normal n basta calcular d como el producto punto n · A. Por ejemplo, con A(1, 2, 3) y n = (1, 1, 2) se obtiene d = 1 + 2 + 6 = 9. Dos planos son paralelos cuando sus normales son múltiplos entre sí; son el mismo plano solo si, además, el número d guarda la misma proporción.",
        "El producto punto sirve para comprobar perpendicularidad: si vale 0, los vectores forman un ángulo recto. Un vector perpendicular a la normal es paralelo al plano. Para argumentar una solución se reemplazan las coordenadas, se comparan las normales y se declara qué se comprobó; una imagen 3D de un plano «inclinado» no entrega estas condiciones.",
    ],
    vocab=[("plano", "superficie plana infinita descrita por ax + by + cz = d"), ("vector normal", "vector perpendicular al plano"), ("producto punto", "ad + be + cf entre dos vectores"), ("perpendicular", "que forma un ángulo recto"), ("planos paralelos", "planos con normales múltiplos entre sí"), ("intersección con un eje", "punto donde el plano corta un eje coordenado")],
    worked=[
        ("Ecuación a partir de un punto y una normal", "Halla el plano que pasa por A(1, 2, 3) con normal (1, 1, 2).", ["Calcula d = 1 · 1 + 1 · 2 + 2 · 3 = 9.", "Escribe la ecuación con la normal como coeficientes."], "x + y + 2z = 9"),
        ("Pertenencia", "¿Pertenece Q(0, 2, 1) al plano 2x + 3y + 6z = 12?", ["Reemplaza: 2 · 0 + 3 · 2 + 6 · 1 = 12.", "El resultado coincide con 12."], "Sí, Q pertenece al plano"),
    ],
    mistakes=[("Creer que (a, b, c) de la ecuación es un punto del plano.", "Es el vector normal, que indica la inclinación; no es un punto.", "Para decidir si un punto está en el plano, reemplaza sus coordenadas."),
              ("Decir que dos planos con normales proporcionales siempre son el mismo plano.", "Pueden ser paralelos y distintos si el número d no guarda la proporción.", "Compara también el lado derecho de las ecuaciones.")],
    T=[
        ('abc', '{F} ¿Cuál es el vector normal del plano π?', '(2, 3, 6)', '(12, 12, 12)', '(1, 1, 1)', 'La normal es el vector de coeficientes de x, y, z; el 12 es el lado derecho.'),
        ('abc', '{F} ¿Pertenece el punto (3, 2, 0) a π?', 'Sí: 6 + 6 + 0 = 12', 'No: 3 + 2 + 0 = 5', 'No: x debe ser 2', 'Al reemplazar, 2 · 3 + 3 · 2 + 6 · 0 da 12, igual al lado derecho.'),
        ('ab', 'Dos planos con normales (1, −2, 3) y (2, −4, 6) son:', 'Paralelos (o iguales), porque una normal es el doble de la otra', 'Perpendiculares, porque las normales son distintas', 'Las normales proporcionales indican igual inclinación, es decir, planos paralelos.'),
        ('=', '{F} ¿Qué valor de z hace que el punto (0, 0, z) esté en π?', '12//6', 'Con x = 0 e y = 0 queda 6z = 12.'),
        ('{F} ¿En qué punto corta π al eje y?', '(0, 4, 0)', 'Con x = 0 y z = 0 queda 3y = 12, es decir, y = 4.'),
        ('abc', 'Un plano pasa por A(2, 0, 1) con normal (3, 1, 2). ¿Cuál es su ecuación?', '3x + y + 2z = 8', '3x + y + 2z = 3', '2x + z = 8', 'Se calcula d = 3 · 2 + 1 · 0 + 2 · 1 = 8; los coeficientes son los de la normal.'),
        ('¿Pertenece (3, 3, 3) al plano x + 2y + 2z = 15? Responde sí o no y explica.', 'Sí: 3 + 6 + 6 = 15', 'Al reemplazar, la suma da 15, igual al lado derecho.'),
        ('=', 'El punto (a, 6, 7) está en el plano x + y + z = 18. ¿Cuánto vale a?', '18-6-7', 'Se despeja a restando las otras dos coordenadas del 18.'),
        ('abc', '{F} El vector (3, −2, 0), ¿es perpendicular a la normal de π?', 'Sí: el producto punto es 6 − 6 + 0 = 0, así que es paralelo al plano', 'No: el producto punto es 6', 'Sí: sus componentes suman 1', 'Un producto punto 0 indica ángulo recto con la normal, lo que significa que el vector es paralelo al plano.'),
        ('abc', 'Una estudiante dice que los planos 2x + 3y + 6z = 12 y 4x + 6y + 12z = 30 son el mismo porque las normales son proporcionales. ¿Qué argumento la refuta?', 'El lado derecho no guarda la proporción: 12 · 2 = 24, no 30', 'Las normales no son proporcionales', 'Un plano no puede tener normal', 'Misma inclinación basta para paralelos, pero para ser el mismo plano 12 debe duplicarse a 24.'),
        ('abc', 'Un plano queda determinado por un punto y un vector normal. ¿Por qué un punto solo no basta?', 'Por un punto pasan infinitos planos con distinta inclinación', 'Porque un punto no tiene coordenadas', 'Porque el plano debe pasar por el origen', 'Sin la normal no se sabe cuál de los planos inclinados que pasan por ese punto se pide.'),
        ('Los planos x + 2y + 3z = 6 y 2x + 4y + 6z = k son el mismo plano. ¿Cuánto vale k?', '12', 'Si el segundo es el doble del primero, el lado derecho también se duplica: 2 · 6.'),
        ('{F} ¿Qué valor de m hace que (m, 6, −2) sea perpendicular a la normal de π?', '−3', 'El producto punto 2m + 18 − 12 debe valer 0, así que 2m = −6.'),
    ],
    ctx=('abc', 'Un panel solar plano se modela con x + y + 2z = 10 (metros). Un cable cae vertical desde el punto (0, 0, z) hasta tocarlo. ¿A qué altura lo toca?', '5 m', '10 m', '2,5 m', 'Con x = 0 e y = 0 queda 2z = 10; 10 m olvida el 2 y 2,5 m divide mal.'),
    sc=[
        ("En Geometría 3D: ¿qué vector da la inclinación de un plano ax + by + cz = d?", "El vector normal (a, b, c)", "Los coeficientes forman un vector perpendicular al plano."),
        ("¿Cómo se comprueba que un punto está en un plano?", "Reemplazando sus coordenadas en la ecuación", "Al reemplazar, debe cumplirse la igualdad de la ecuación."),
        ("¿Qué indica un producto punto igual a 0?", "Que los vectores son perpendiculares", "El ángulo entre ellos es recto."),
    ],
    op=("Elige un caso: (a) el plano que pasa por A(1, 1, 1) con normal (2, 1, 2); decide si los puntos (2, 2, 1) y (0, 0, 5) están en él. (b) Los planos x + y + z = 4 y 3x + 3y + 3z = 15; decide si son paralelos o iguales. Justifica con cálculos.",
        "Caso (a): d = 2 + 1 + 2 = 5, así que el plano es 2x + y + 2z = 5. El punto (2, 2, 1) da 4 + 2 + 2 = 8, no está; el punto (0, 0, 5) da 10, tampoco.",
        ["calcula d con punto y normal o compara normales", "reemplaza coordenadas con cuidado", "concluye con una frase"],
        ["hoja con la ecuación y las comprobaciones"],
        ["tomar la normal como punto", "olvidar comparar el lado derecho", "reemplazar solo dos coordenadas"],
        "Pregunta: «¿qué número quedó a cada lado?». Si no coinciden, el punto no está en el plano."),
    reinforce="Elige un plano de la forma x + y + z = d con d entero y encuentra cuatro puntos con coordenadas enteras que estén en él.",
    extend="Explica por qué dos planos con normales perpendiculares forman un ángulo recto entre ellos.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (de ejemplo). Plano π: x + 2y + 2z = 18, con normal n = (1, 2, 2) de módulo 3. Recta M: (2, 1, 3) + s · (2, 1, −1). Recta K: (0, 0, 0) + t · (2, −1, 0). "
     "Distancia de un punto (p, q, r) al plano: el valor absoluto de p + 2q + 2r − 18, dividido por el módulo de la normal (3). "
     "En un programa de geometría dinámica 3D se vería la recta atravesar el plano; aquí se calcula a mano.")
build(
    O2, 4, F,
    use="Aprenderé a resolver problemas que combinan puntos, rectas y planos: intersecciones, paralelismo y distancias, y a verificarlos con cálculos.",
    prior=["Sé describir rectas con punto y director.", "Sé describir planos con una ecuación y una normal.", "Sé calcular producto punto y módulo."],
    explain=[
        "Para hallar dónde una recta corta a un plano se sustituyen x, y, z de la recta (que dependen de t) en la ecuación del plano y se resuelve para t. Si sale un solo valor, hay un punto de intersección. Si el producto punto del vector director con la normal es 0, la recta es paralela al plano: o no lo toca nunca, o está contenida en él si un punto suyo cumple la ecuación.",
        "La distancia de un punto al plano se calcula con el valor absoluto de ax + by + cz − d dividido por el módulo de la normal. Esa distancia se mide siguiendo una recta perpendicular al plano, es decir, con director igual a la normal. Dos planos paralelos x + 2y + 2z = d₁ y x + 2y + 2z = d₂ están a distancia |d₁ − d₂| dividido por el módulo de la normal.",
        "Una buena solución indica qué se reemplazó, cuánto valió el parámetro y qué comprobación final se hizo, por ejemplo reemplazar el punto hallado en ambas descripciones. Las imágenes digitales ayudan a imaginar la situación, pero no sustituyen el cálculo y no muestran los límites del modelo, como que el plano es infinito mientras que una losa real tiene bordes.",
    ],
    vocab=[("intersección", "punto o conjunto común a dos objetos"), ("recta paralela al plano", "recta cuyo director es perpendicular a la normal"), ("recta contenida", "recta cuyos puntos están todos en el plano"), ("distancia punto-plano", "longitud del camino perpendicular"), ("sustitución", "reemplazar las coordenadas de la recta en la ecuación del plano"), ("modelo", "descripción matemática simplificada de una situación")],
    worked=[
        ("Recta y plano", "Halla dónde la recta (1, 0, 2) + t(1, 1, 1) corta al plano x + y + z = 12.", ["Sustituye: (1 + t) + t + (2 + t) = 3 + 3t = 12, entonces t = 3.", "Evalúa la recta en t = 3: (4, 3, 5)."], "Corta en (4, 3, 5)"),
        ("Distancia punto-plano", "Calcula la distancia de P(1, 2, 2) al plano de la ficha.", ["Reemplaza: 1 + 4 + 4 − 18 = −9, con valor absoluto 9.", "Divide por el módulo de la normal: 9 ÷ 3 = 3."], "La distancia es 3 unidades"),
    ],
    mistakes=[("Igualar los vectores directores en vez de sustituir en la ecuación del plano.", "La intersección pide los puntos que cumplen ambas descripciones a la vez.", "Reemplaza x, y, z de la recta en la ecuación del plano."),
              ("Olvidar el valor absoluto en la distancia.", "Una distancia no puede ser negativa.", "Calcula el valor y toma el valor absoluto antes de dividir.")],
    T=[
        ('abc', '{F} ¿Cuál es el vector normal del plano π?', '(1, 2, 2)', '(1, 2, 18)', '(2, 1, 3)', 'Los coeficientes de x, y, z forman la normal; el 18 es el lado derecho.'),
        ('abc', '{F} Para hallar dónde la recta M corta al plano π, ¿qué se hace?', 'Reemplazar x, y, z de M en la ecuación de π y resolver para s', 'Igualar el vector director de M con la normal', 'Restar la ecuación del plano a la de la recta', 'La intersección es el punto de la recta que cumple la ecuación del plano.'),
        ('ab', 'Si el producto punto entre el director de una recta y la normal de un plano es 0, la recta es:', 'Paralela al plano o contenida en él', 'Perpendicular al plano', 'Un producto punto 0 significa director perpendicular a la normal, es decir, paralelo al plano.'),
        ('{F} ¿Cuál es el punto de M con s = 4?', '(10, 5, −1)', 'Se calcula (2 + 8, 1 + 4, 3 − 4) con s = 4.'),
        ('=', '{F} El módulo de la normal es 3. ¿Qué distancia hay del origen al plano π?', '18//3', 'Con el origen, el valor de la expresión es −18, y se divide su valor absoluto por 3.', ' unidades'),
        ('{F} ¿Cuál es el producto punto entre el director de M y la normal de π?', '2', 'Se calcula 2 · 1 + 1 · 2 + (−1) · 2 = 2.'),
        ('Halla el punto en que la recta (0, 1, 0) + t(1, 2, 3) corta al plano x + y + z = 13.', '(2, 5, 6)', 'Se sustituye: t + (1 + 2t) + 3t = 1 + 6t = 13, entonces t = 2.'),
        ('abc', '{F} ¿Qué posición tiene la recta K respecto de π?', 'Paralela al plano, sin tocarlo', 'Contenida en el plano', 'Corta al plano en un punto', 'El director (2, −1, 0) da producto punto 0 con la normal, y el origen no cumple x + 2y + 2z = 18.'),
        ('=', '{F} ¿Qué distancia hay del punto (6, 6, 6) al plano π? Usa el módulo 3 de la normal.', '(6+2*6+2*6-18)//3', 'Se reemplaza el punto, se resta 18 y se divide por el módulo de la normal.', ' unidades'),
        ('abc', 'Una estudiante dice: «la recta M corta al plano, así que todos sus puntos están en el plano». ¿Cuál es el error?', 'Una recta que corta al plano comparte con él un solo punto', 'Una recta no puede cortar un plano', 'Todos los puntos de la recta tienen z = 0', 'La condición de pertenencia se cumple solo para el valor de s que se despejó.'),
        ('abc', 'Un programa de geometría 3D muestra la recta M atravesando el plano cerca de (10, 5, −1), pero no entrega las ecuaciones. ¿Cómo se argumenta que ese punto es correcto?', 'Se reemplaza en la ecuación del plano y se halla el s que lo da en la recta', 'Se confía en que se ve cerca', 'Se mide en pantalla con una regla', 'La imagen sugiere, pero la validez exige verificar que el punto cumple ambas descripciones.'),
        ('La recta (0, 0, 0) + t(1, 2, 2) es perpendicular a π. ¿En qué punto la corta?', '(2, 4, 4)', 'Se sustituye: t + 4t + 4t = 9t = 18, entonces t = 2.'),
        ('Los planos x + 2y + 2z = 18 y x + 2y + 2z = 3 son paralelos. ¿A qué distancia están?', '5 unidades', 'Se calcula |18 − 3| ÷ 3 usando el módulo de la normal.'),
    ],
    ctx=('abc', 'Un tubo sigue la recta (1, 0, 4) + s(1, 2, −1) (metros) y debe atravesar una losa modelada por x + 2y + 2z = 18. ¿Por dónde la atraviesa?', '(4, 6, 1)', '(3, 4, 2)', '(1, 0, 4)', 'La sustitución da 9 + 3s = 18 y s = 3; (1, 0, 4) es el punto inicial, que no está en la losa.'),
    sc=[
        ("En Geometría 3D: ¿qué se sustituye para hallar la intersección de una recta y un plano?", "x, y, z de la recta en la ecuación del plano", "Así se obtiene el único valor del parámetro."),
        ("¿Qué indica un producto punto 0 entre el director y la normal?", "Que la recta es paralela al plano", "El director es perpendicular a la normal."),
        ("¿Por qué se usa valor absoluto en la distancia punto-plano?", "Porque una distancia no es negativa", "El signo solo indica de qué lado del plano está el punto."),
    ],
    op=("Elige un caso: (a) la recta (0, 0, 3) + t(1, 1, 1) y el plano x + y + z = 12: halla la intersección; (b) el punto P(2, 3, 5) y el plano x + 2y + 2z = 3: calcula la distancia. Escribe qué sustituiste, cuánto valió el parámetro y cómo comprobaste el resultado.",
        "Caso (a): se sustituye t + t + (3 + t) = 3 + 3t = 12, entonces t = 3 y el punto es (3, 3, 6). Comprobación: 3 + 3 + 6 = 12.",
        ["sustituye en la ecuación del plano", "da el valor del parámetro", "comprueba el punto en el plano"],
        ["hoja con el cálculo y la comprobación"],
        ["igualar directores", "olvidar el valor absoluto", "no comprobar el resultado"],
        "Pregunta: «¿cómo sabes que el punto está en el plano?». Si no lo comprueba, pídele que lo reemplace."),
    reinforce="Elige un plano x + y + z = 9 y una recta con director (1, 1, 1) que pase por el origen; halla el punto de intersección.",
    extend="Explica por qué un modelo con planos infinitos puede dar una intersección que no existe en una losa real con bordes.",
)

O3 = "MA-GE3D-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (de ejemplo). Una construcción de cubos unitarios (1 cm de arista) se describe con una tabla de alturas: cada número es cuántos cubos hay apilados en esa casilla. "
     "Filas de adelante hacia atrás y columnas de izquierda a derecha. Fila 1 (frente): 2 1 0. Fila 2: 1 3 2. Fila 3 (fondo): 0 1 1. "
     "Convención de este cuaderno: la vista frontal da la altura máxima de cada columna, de izquierda a derecha; la vista lateral da la altura máxima de cada fila, de frente a fondo; la vista superior marca las casillas con al menos un cubo.")
build(
    O3, 1, F,
    use="Aprenderé a dibujar y leer vistas frontal, lateral y superior de una construcción de cubos, a contar cubos y a argumentar cuántos cubos puede haber.",
    prior=["Sé leer tablas de números.", "Sé calcular el volumen contando cubos unitarios.", "Sé que una vista es una representación plana."],
    explain=[
        "Una vista es la imagen plana de un cuerpo mirado desde una dirección. Las tres vistas habituales son la frontal (desde el frente), la lateral (desde un lado) y la superior (desde arriba). Cuando el cuerpo se arma con cubos, cada vista muestra solo lo que no queda tapado: en la frontal se ve la pila más alta de cada columna, y en la lateral la más alta de cada fila.",
        "La vista superior no dice las alturas: solo marca qué casillas tienen al menos un cubo. El número total de cubos se obtiene sumando todas las alturas de la tabla, y el volumen es ese número por el volumen de un cubo. Una vista puede ocultar cubos: dos construcciones distintas pueden dar las mismas vistas, así que con vistas incompletas hay un mínimo y un máximo de cubos posibles.",
        "Para hallar los límites se piensa casilla por casilla: la altura de cada casilla no puede superar ni la altura de su columna en la vista frontal ni la de su fila en la lateral. El máximo se alcanza usando en cada casilla el menor de esos dos valores; el mínimo, usando lo estrictamente necesario para que cada columna y cada fila muestre su altura.",
    ],
    vocab=[("vista frontal", "imagen del cuerpo mirado desde el frente"), ("vista lateral", "imagen del cuerpo mirado desde un lado"), ("vista superior", "imagen del cuerpo mirado desde arriba"), ("tabla de alturas", "número de cubos apilados en cada casilla"), ("cubo unitario", "cubo de arista 1 unidad y volumen 1"), ("cubo oculto", "cubo que no se ve en una vista porque lo tapa otro")],
    worked=[
        ("Vistas de una construcción", "Fila 1: 4 0. Fila 2: 1 1. Halla las vistas y el total de cubos.", ["Frontal: la columna 1 tiene alturas 4 y 1 (máximo 4), y la columna 2 tiene 0 y 1 (máximo 1): 4 1.", "Lateral: la fila 1 tiene máximo 4 y la fila 2 máximo 1: 4 1. Superior: 3 casillas; cubos: 4 + 0 + 1 + 1 = 6."], "Frontal 4 1, lateral 4 1, superior 3 casillas y 6 cubos"),
        ("Cubos ocultos", "Con vista frontal (2, 2) y vista superior de 4 casillas, ¿puede haber 6 y también 8 cubos?", ["Con alturas 2 2 / 2 2 hay 8 cubos y la frontal es (2, 2).", "Con alturas 2 1 / 1 2 hay 6 cubos, la frontal también es (2, 2) y la superior sigue con 4 casillas."], "Sí: las vistas no determinan el número de cubos"),
    ],
    mistakes=[("Sumar las alturas de una columna para la vista frontal.", "La vista muestra la pila más alta, no la suma.", "Toma el máximo de cada columna."),
              ("Creer que la vista superior dice cuántos cubos hay en total.", "Solo marca las casillas ocupadas, no las alturas.", "Para el total suma todas las alturas de la tabla.")],
    T=[
        ('abc', '{F} ¿Cuál es la vista frontal, de izquierda a derecha?', '2 3 2', '3 5 3', '2 1 0', 'Se toma el máximo de cada columna: 2, 3 y 2; 3 5 3 son sumas y 2 1 0 es solo la primera fila.'),
        ('abc', '¿Qué muestra la vista superior de una construcción de cubos?', 'Qué casillas tienen al menos un cubo', 'La altura de cada pila', 'El total de cubos', 'Mirando desde arriba solo se distingue si hay o no cubo en cada casilla.'),
        ('ab', 'Una columna tiene dos pilas, una de 2 cubos y otra de 3 cubos, en filas distintas. En la vista frontal esa columna se ve con altura:', '3', '5', 'Se ve la pila más alta, y la de 2 queda tapada detrás o delante.'),
        ('=', '{F} ¿Cuántos cubos tiene en total la construcción?', '2+1+0+1+3+2+0+1+1', 'Se suman todas las alturas de la tabla.', ' cubos'),
        ('{F} ¿Cuántas casillas se ven marcadas en la vista superior?', '7', 'Hay 2 casillas con cubos en la fila 1, 3 en la fila 2 y 2 en la fila 3.'),
        ('{F} ¿Cuál es la vista lateral, de frente a fondo?', '2 3 1', 'Se toma el máximo de cada fila: 2, 3 y 1.'),
        ('Una construcción tiene Fila 1: 1 2 y Fila 2: 3 1. ¿Cuál es su vista frontal, de izquierda a derecha?', '3 2', 'La columna 1 tiene 1 y 3, con máximo 3; la columna 2 tiene 2 y 1, con máximo 2.'),
        ('=', '{F} Cada cubo mide 2 cm de arista. ¿Cuál es el volumen total en cm³?', '11*2*2*2', 'Cada cubo de 2 cm tiene 8 cm³ y la construcción tiene 11 cubos.', ' cm³'),
        ('En una construcción de 2 × 2 casillas, la vista frontal es (2, 3) y la lateral, de frente a fondo, es (3, 2). ¿Cuál es la altura máxima posible de la casilla de la fila 2, columna 1?', '2', 'No puede superar el máximo de su fila (2) ni el de su columna (2).'),
        ('abc', 'Una estudiante dice que con la vista frontal y la superior siempre se reconstruye la construcción. ¿Qué argumento la refuta?', 'Con vista frontal (1, 3) y superior de 4 casillas caben construcciones de 6 y de 8 cubos', 'La vista frontal siempre muestra todos los cubos', 'La vista superior indica las alturas', 'Los cubos ocultos no cambian las vistas, así que pueden existir varias construcciones distintas.'),
        ('abc', 'Un estudiante dice que el número de cubos es igual al número de casillas de la vista superior. ¿Cuándo es cierto?', 'Solo si todas las pilas tienen exactamente 1 cubo', 'Siempre', 'Nunca', 'Cada casilla marcada tiene al menos 1 cubo y solo tiene exactamente 1 si ninguna pila es más alta.'),
        ('Una construcción de 2 × 2 tiene vista frontal (2, 3) y lateral, de frente a fondo, (3, 2). ¿Cuántos cubos puede tener como mínimo y como máximo?', 'Mínimo 5 y máximo 9', 'Máximo: casillas 2, 3, 2, 2 (min de fila y columna) suma 9. Mínimo: 3 en la fila 1 columna 2 y 2 en la fila 2 columna 1, suma 5.'),
        ('Una construcción de 2 × 2 tiene vista frontal (3, 1) y lateral, de frente a fondo, (3, 1). ¿Cuántos cubos puede tener como mínimo y como máximo?', 'Mínimo 4 y máximo 6', 'Máximo: 3, 1, 1, 1 suma 6. Mínimo: 3 en la fila 1 columna 1 y 1 en la fila 2 columna 2, suma 4.'),
    ],
    ctx=('abc', 'Una caja de bloques trae 12 cubos. ¿Alcanza para armar la construcción de la ficha?', 'Sí, porque la construcción usa 11 y sobra 1', 'No, porque necesita 13', 'No, porque necesita 12 más 3 de repuesto', 'La tabla suma 2 + 1 + 0 + 1 + 3 + 2 + 0 + 1 + 1 = 11 cubos, que son menos que 12.'),
    sc=[
        ("En Geometría 3D: ¿qué altura muestra una columna en la vista frontal?", "La de la pila más alta", "Las demás pilas quedan tapadas detrás de la más alta."),
        ("¿Qué se hace para obtener el total de cubos?", "Se suman todas las alturas de la tabla", "Cada número es una pila de cubos."),
        ("¿Pueden dos construcciones distintas tener las mismas vistas?", "Sí", "Por los cubos ocultos que ninguna vista muestra."),
    ],
    op=("Elige una tabla: A) Fila 1: 3 1; Fila 2: 2 2. B) Fila 1: 1 0 2; Fila 2: 3 1 1. Dibuja o escribe sus vistas frontal, lateral y superior con la convención de la ficha y calcula el total de cubos. Luego inventa una segunda tabla con las mismas vistas frontal y lateral y distinto número de cubos, y explica por qué es posible.",
        "Tabla A: frontal 3 2, lateral 3 2, superior 4 casillas, total 8. Otra tabla con las mismas vistas: Fila 1: 3 0; Fila 2: 0 2: frontal 3 2, lateral 3 2, total 5.",
        ["vistas correctas con máximos", "total por suma", "segunda tabla con vistas iguales y total distinto"],
        ["hoja con tabla, vistas, totales y la explicación"],
        ["sumar en vez de tomar el máximo", "confundir filas con columnas", "olvidar casillas vacías"],
        "Pregunta: «¿qué pila tapa a cuál?». Si confunde, pídele que dibuje la columna de lado."),
    reinforce="Arma con cubos de juguete o con dados una torre de tres pilas distintas y dibuja sus tres vistas en papel cuadriculado.",
    extend="Explica cómo cambiaría el máximo de cubos si la vista lateral tuviera una pila más alta.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (de ejemplo). Los cortes son imaginarios: no se corta ningún objeto real. Sólidos: cubo de arista 6 cm; cilindro de radio 3 cm y altura 8 cm; "
     "cono de radio 3 cm, altura 4 cm y generatriz 5 cm; esfera de radio 5 cm. El área del círculo es π · r²; deja π sin reemplazar.")
build(
    O3, 2, F,
    use="Aprenderé a describir y calcular las secciones que produce un plano al cortar un cubo, un cilindro, un cono y una esfera, y a argumentar qué figura resulta.",
    prior=["Sé calcular áreas de cuadrados, rectángulos, triángulos y círculos.", "Sé aplicar el teorema de Pitágoras.", "Sé reconocer sólidos geométricos."],
    explain=[
        "Un corte o sección es la figura plana que resulta al cruzar un sólido con un plano. Si el plano es paralelo a una cara de un cubo, la sección es un cuadrado igual a la cara. En un cilindro, un plano paralelo a la base da un círculo igual a la base, y uno que contiene el eje da un rectángulo de ancho 2r y alto h. En un cono, un plano paralelo a la base da un círculo más pequeño, y uno que contiene el eje da un triángulo isósceles.",
        "En la esfera, toda sección es un círculo (o un punto si el plano solo la toca). Si el plano está a distancia d del centro y el radio de la esfera es R, el radio de la sección sale del teorema de Pitágoras: r² = R² − d². Si d es mayor que R, el plano no toca la esfera y no hay sección. En el cono, los círculos paralelos a la base tienen radios proporcionales a la distancia al vértice.",
        "Para argumentar si una afirmación sobre cortes es cierta, se prueba con un plano concreto: un contraejemplo basta para refutar una frase como «cualquier corte da un círculo». Las secciones se relacionan con las vistas: un corte es una vista de lo que hay al interior. Las ideas se pueden representar en papel con dibujos sencillos sin cortar ningún objeto.",
    ],
    vocab=[("sección o corte", "figura plana que resulta de cortar un sólido con un plano"), ("plano de corte", "plano imaginario que atraviesa el sólido"), ("eje de un cilindro o cono", "recta que pasa por los centros de las bases o por el vértice"), ("generatriz", "segmento que une el vértice del cono con el borde de la base"), ("sección axial", "la que contiene el eje"), ("distancia al centro", "separación entre el plano de corte y el centro de la esfera")],
    worked=[
        ("Sección de una esfera", "Una esfera de radio 13 cm se corta con un plano a 5 cm del centro. ¿Cuánto mide el radio de la sección y cuál es su área?", ["Se calcula r² = 13² − 5² = 169 − 25 = 144, así que r = 12.", "El área es π · 12² = 144π."], "Radio 12 cm y área 144π cm²"),
        ("Sección axial de un cilindro", "Un cilindro tiene radio 2 cm y altura 5 cm. ¿Qué figura da un plano que contiene el eje y cuál es su área?", ["La figura es un rectángulo de ancho 2r = 4 y alto 5.", "El área es 4 · 5 = 20."], "Un rectángulo de 20 cm²"),
    ],
    mistakes=[("Creer que todo corte de un cilindro es un círculo.", "El corte paralelo a la base es un círculo, pero el que pasa por el eje es un rectángulo.", "Pregunta primero cómo está el plano respecto de la base y del eje."),
              ("Calcular el radio de la sección de una esfera como R − d.", "Los radios y la distancia forman un triángulo rectángulo con R como hipotenusa.", "Usa r² = R² − d².")],
    T=[
        ('abc', 'Un plano paralelo a la base corta un cilindro. ¿Qué sección resulta?', 'Un círculo igual a la base', 'Un rectángulo', 'Un triángulo', 'Al cortar paralelo a la base, la figura es idéntica a la base: un círculo del mismo radio.'),
        ('abc', '{F} ¿Qué sección se obtiene al cortar el cubo con un plano paralelo a una cara?', 'Un cuadrado de 6 cm de lado', 'Un círculo de radio 3 cm', 'Un triángulo de 6 cm de base', 'La sección es una copia de la cara, que es un cuadrado de la arista del cubo.'),
        ('ab', 'Un plano que contiene el eje de un cono corta una sección con forma de:', 'Un triángulo isósceles', 'Un círculo', 'El corte axial corta las dos generatrices opuestas y el diámetro de la base.'),
        ('=', '{F} El plano contiene el eje del cilindro y la sección es un rectángulo de 6 cm por 8 cm. ¿Cuál es su área?', '6*8', 'El ancho es el diámetro 6 y el alto es la altura 8.', ' cm²'),
        ('{F} Un plano corta la esfera a 3 cm del centro. ¿Cuánto mide el radio de la sección?', '4 cm', 'Se calcula r² = 25 − 9 = 16, y la raíz de 16 es 4.'),
        ('{F} Un plano pasa justo por el centro de la esfera. ¿Cuál es el área de la sección, en términos de π?', '25π cm²', 'Con distancia 0 al centro, el radio de la sección es el de la esfera, 5 cm, y el área es π · 5².'),
        ('{F} Un plano corta la esfera a 4 cm del centro. ¿Cuál es el área de la sección?', '9π cm²', 'El radio al cuadrado es 25 − 16 = 9, así que el área es π · 9.'),
        ('abc', 'Un cono tiene radio 6 cm y altura 8 cm. Un plano paralelo a la base lo corta a 4 cm del vértice. ¿Cuánto mide el radio de la sección?', '3 cm', '4 cm', '2 cm', 'A mitad de la altura el radio es la mitad: 6 · 4 ÷ 8 = 3.'),
        ('=', '{F} La sección axial del cono es un triángulo de base 6 cm y altura 4 cm. ¿Cuál es su área?', '6*4//2', 'El área de un triángulo es base por altura dividido en dos.', ' cm²'),
        ('abc', 'Un estudiante dice que cualquier corte de un cilindro da un círculo. ¿Qué contraejemplo lo refuta?', 'El corte por el eje da un rectángulo', 'Cortar paralelo a la base da un círculo', 'El corte nunca produce una figura plana', 'Basta un plano que contenga el eje para obtener un rectángulo y no un círculo.'),
        ('abc', 'La esfera tiene radio 5 cm. Un plano está a 7 cm del centro. ¿Qué sección se obtiene?', 'Ninguna: el plano no toca la esfera', 'Un círculo de radio 2 cm', 'Un círculo de radio 12 cm', 'Si la distancia al centro supera al radio, el plano pasa de largo y no hay sección.'),
        ('Una esfera se corta con un plano a 12 cm de su centro y la sección tiene área 25π cm². ¿Cuánto mide el radio de la esfera?', '13 cm', 'El radio de la sección es 5, y R² = 12² + 5² = 169, por lo que R = 13.'),
        ('Un cono de radio 6 cm y altura 8 cm se corta con un plano paralelo a la base a 4 cm del vértice. ¿Qué fracción del área de la base es el área de la sección?', '1/4', 'El radio de la sección es la mitad, así que el área es (1/2)² = 1/4 de la base.'),
    ],
    ctx=('abc', 'Una cúpula se modela como media esfera de radio 5 m. Una ventana circular plana se instala en un plano a 3 m del centro. ¿Qué radio tiene la ventana?', '4 m', '3 m', '2 m', 'El radio sale de 25 − 9 = 16, es decir, 4 m; 3 m es la distancia al centro y 2 m resta mal 5 − 3.'),
    sc=[
        ("En Geometría 3D: ¿qué es una sección de un sólido?", "La figura plana que resulta al cortarlo con un plano", "Es la intersección del sólido con el plano."),
        ("¿Qué figura es toda sección de una esfera?", "Un círculo", "Si el plano la toca en un solo punto, la sección es un punto."),
        ("¿Qué relación se usa para el radio de una sección de esfera?", "r² = R² − d²", "Es el teorema de Pitágoras con R como hipotenusa."),
    ],
    op=("Elige un caso: (a) una esfera de radio 10 cm cortada por planos a 6 cm y a 8 cm de su centro; calcula el radio y el área de cada sección. (b) Un cilindro de radio 4 cm y altura 9 cm cortado por un plano paralelo a la base y por otro que contiene el eje; dibuja o describe cada sección y calcula sus áreas. Justifica con los datos.",
        "Caso (a): a 6 cm, r² = 100 − 36 = 64, así que r = 8 y el área es 64π cm². A 8 cm, r² = 100 − 64 = 36, así que r = 6 y el área es 36π cm².",
        ["identifica la forma de cada sección", "calcula con Pitágoras o con las medidas", "indica unidades y deja π sin reemplazar"],
        ["hoja con dibujos esquemáticos y cálculos"],
        ["decir que todo corte es círculo", "usar R − d como radio", "olvidar el cuadrado en el área"],
        "Pregunta: «¿cómo está el plano respecto del eje?». Si no lo dice, pídele que lo dibuje."),
    reinforce="Dibuja un cilindro y marca dos planos de corte: uno paralelo a la base y uno por el eje; escribe qué figura resulta en cada uno.",
    extend="Explica por qué en un cono las secciones paralelas a la base son semejantes entre sí.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (de ejemplo). Proyección ortogonal sobre el suelo (plano z = 0): cada punto (x, y, z) pasa a (x, y, 0), como si se mirara desde arriba. "
     "Segmento AB con A(1, 2, 3) y B(4, 6, 3); segmento CD con C(0, 0, 0) y D(3, 4, 12). "
     "Rampa rectangular: largo inclinado 5 m, ancho 6 m; sube 3 m a lo largo de 4 m de recorrido horizontal.")
build(
    O3, 3, F,
    use="Aprenderé a proyectar puntos, segmentos y superficies sobre un plano, a calcular longitudes y áreas proyectadas y a argumentar qué se conserva y qué no.",
    prior=["Sé calcular distancias en el plano con Pitágoras.", "Sé calcular áreas de rectángulos.", "Sé leer coordenadas (x, y, z)."],
    explain=[
        "La proyección ortogonal sobre un plano lleva cada punto al punto más cercano del plano, siguiendo una recta perpendicular. Sobre el suelo (z = 0) basta olvidar la altura: (x, y, z) pasa a (x, y). Un segmento se proyecta como otro segmento, y su proyección es tan larga como el original solo si el segmento es paralelo al plano; si está inclinado, la proyección es más corta.",
        "Para calcular la longitud proyectada se usa Pitágoras en el plano con las diferencias de x y de y. El segmento real se calcula con Pitágoras en el espacio, usando también la diferencia de z, así que es mayor que su proyección cuando el segmento sube. Con las superficies pasa algo parecido: una cara inclinada tiene un área proyectada menor que su área real, y una cara vertical se proyecta como un segmento.",
        "Qué se conserva: segmentos paralelos se proyectan paralelos; los puntos de un segmento mantienen su orden. Qué no se conserva: longitudes, ángulos y áreas de figuras inclinadas. Para argumentar una solución se declara el plano de proyección y se comprueban los cálculos con coordenadas, no con la apariencia del dibujo.",
    ],
    vocab=[("proyección ortogonal", "proyección con rayos perpendiculares al plano"), ("plano de proyección", "plano sobre el que se proyecta"), ("segmento proyectado", "imagen de un segmento sobre el plano"), ("inclinado", "ni paralelo ni perpendicular al plano"), ("área real", "área de la superficie tal como es"), ("área proyectada", "área de su imagen sobre el plano")],
    worked=[
        ("Proyección de un punto", "Proyecta el punto P(2, −1, 5) sobre el suelo.", ["Se elimina la altura z.", "Quedan las coordenadas x e y."], "P′ = (2, −1)"),
        ("Longitud proyectada", "El segmento E(0, 0, 0), G(8, 6, 24) tiene longitud 26. ¿Cuánto mide su proyección sobre el suelo?", ["Las diferencias en el suelo son 8 y 6.", "La proyección mide la raíz de 64 + 36 = 100, es decir, 10."], "La proyección mide 10 y el segmento real mide 26"),
    ],
    mistakes=[("Creer que la proyección conserva la longitud de cualquier segmento.", "Solo la conserva si el segmento es paralelo al plano.", "Compara la altura que sube el segmento: si es 0, se conserva."),
              ("Proyectar al suelo cambiando la x o la y en vez de eliminar z.", "La proyección sobre z = 0 mantiene x e y.", "Pon z = 0 y conserva las otras dos coordenadas.")],
    T=[
        ('abc', '{F} ¿Cuál es la proyección del punto A(1, 2, 3) sobre el suelo?', '(1, 2)', '(1, 2, 3)', '(2, 3)', 'La proyección elimina la altura z y mantiene x e y.'),
        ('abc', 'La proyección ortogonal sobre el suelo de un punto (x, y, z) elimina:', 'La altura z', 'La coordenada x', 'La coordenada y', 'El suelo es el plano z = 0, así que solo se descarta la altura.'),
        ('ab', 'Un segmento paralelo al plano de proyección se proyecta con:', 'La misma longitud', 'Una longitud menor', 'No sube respecto del plano, así que no se acorta al proyectarlo.'),
        ('{F} Calcula la longitud de la proyección del segmento AB sobre el suelo.', '5', 'Las diferencias son 3 y 4 y la raíz de 9 + 16 es 5; AB es paralelo al suelo.'),
        ('{F} ¿Cuánto mide la proyección del segmento CD sobre el suelo?', '5', 'Las diferencias de x e y son 3 y 4, y la raíz de 9 + 16 es 5.'),
        ('{F} ¿Cuánto mide el segmento real CD?', '13', 'Se calcula 9 + 16 + 144 = 169 y la raíz de 169 es 13.'),
        ('=', '{F} ¿Cuál es el área de la proyección de la rampa sobre el suelo? Ocupa 4 m de recorrido por 6 m de ancho.', '4*6', 'La proyección es un rectángulo de 4 por 6.', ' m²'),
        ('abc', '{F} ¿Por qué el área proyectada de la rampa es menor que el área real?', 'Porque está inclinada: su largo horizontal es 4 m y no 5 m', 'Porque se pierde un lado al proyectar', 'Porque la proyección cambia el ancho', 'El largo inclinado mide 5 m, pero el largo horizontal es solo 4 m.'),
        ('abc', 'Una pared vertical de 5 m de largo y 3 m de alto se proyecta sobre el suelo. ¿Qué se obtiene?', 'Un segmento de 5 m', 'Un rectángulo de 5 por 3', 'Un punto', 'La altura desaparece al proyectar, y solo queda el largo de la pared.'),
        ('abc', 'Dos segmentos tienen la misma proyección sobre el suelo. ¿Tienen la misma longitud real?', 'No: pueden diferir en cuánto suben, como (0, 0, 0)-(3, 4, 0) y (0, 0, 0)-(3, 4, 12)', 'Sí, siempre', 'Sí, si ambos empiezan en el origen', 'La proyección omite la altura, por eso el real puede ser mayor.'),
        ('abc', 'En una proyección ortogonal sobre el suelo, ¿qué se conserva siempre?', 'El paralelismo entre segmentos paralelos', 'Las longitudes', 'Los ángulos', 'Las rectas paralelas se proyectan paralelas, aunque longitudes y ángulos pueden cambiar.'),
        ('Una rampa rectangular de 6 m de ancho tiene un largo inclinado de 13 m y sube 5 m, con 12 m de recorrido horizontal. ¿Cuál es la razón entre el área proyectada y el área real?', '12/13', 'El área proyectada es 12 · 6 = 72 y la real 13 · 6 = 78; la razón es 72/78 = 12/13.'),
        ('Un segmento tiene proyección de 12 m sobre el suelo y sube 5 m. ¿Cuánto mide el segmento?', '13 m', 'La longitud real es la raíz de 12² + 5² = 169, es decir, 13.'),
    ],
    ctx=('abc', 'En un plano de planta, un techo inclinado aparece con 24 m², pero su área real es 30 m². Para comprar láminas, ¿cuál área hay que usar?', 'El área real de 30 m²', 'El área de la planta, de 24 m²', 'El promedio de ambas', 'Las láminas cubren la superficie inclinada real, no su sombra en la planta.'),
    sc=[
        ("En Geometría 3D: ¿qué cambia en un punto al proyectarlo sobre el suelo?", "Se pierde la altura z", "Quedan las coordenadas x e y."),
        ("¿Cuándo una proyección conserva la longitud de un segmento?", "Cuando el segmento es paralelo al plano", "No sube ni baja respecto del plano."),
        ("¿En qué se proyecta una pared vertical sobre el suelo?", "En un segmento", "Su altura desaparece y solo queda su largo."),
    ],
    op=("Elige un caso: (a) un segmento de P(0, 0, 2) a Q(12, 16, 2) y otro de R(0, 0, 0) a S(12, 16, 15); calcula sus proyecciones y sus longitudes reales. (b) Una rampa de 3 m de ancho con largo inclinado 10 m que sube 6 m (recorrido horizontal 8 m); calcula el área real y el área proyectada. Explica qué se conserva y qué no.",
        "Caso (b): área real 10 · 3 = 30 m²; área proyectada 8 · 3 = 24 m²; el ancho se conserva y el largo se acorta porque la rampa está inclinada.",
        ["usa Pitágoras para longitudes", "distingue real y proyectado", "explica qué se conserva"],
        ["hoja con los cálculos y la explicación"],
        ["usar la longitud inclinada en el área proyectada", "olvidar la diferencia en z", "decir que la proyección conserva todo"],
        "Pregunta: «¿cuánto subió el segmento?». Si dice 0, el real y el proyectado coinciden."),
    reinforce="Con una regla y una escuadra, imagina la sombra de un lápiz sobre una mesa si lo miras desde arriba y describe cuándo se acorta.",
    extend="Explica por qué dos figuras distintas del espacio pueden tener la misma proyección sobre un plano.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (de ejemplo). Cubo de arista 6 cm con una esfera inscrita (toca las seis caras). Cilindro de radio 3 cm y altura 6 cm, también con una esfera inscrita, y un cono de radio 3 cm y altura 6 cm inscrito (comparte base y altura con el cilindro). "
     "Pirámide de base cuadrada inscrita en el cubo: su base es una cara y su vértice está en la cara opuesta. "
     "Volúmenes: cubo a³; esfera 4/3 · π · r³; cilindro π · r² · h; cono 1/3 · π · r² · h; pirámide 1/3 · área de la base · altura.")
build(
    O3, 4, F,
    use="Aprenderé a relacionar una figura 3D con otra que la contiene (inscrita), a calcular medidas y volúmenes de las dos y a comparar sus razones.",
    prior=["Sé calcular volúmenes de cubo, cilindro, cono, esfera y pirámide.", "Sé usar Pitágoras en el espacio.", "Sé calcular razones entre dos cantidades."],
    explain=[
        "Una figura está inscrita en otra cuando está dentro y la toca de una manera definida. Una esfera inscrita en un cubo toca el centro de cada una de sus seis caras, así que su diámetro es igual a la arista del cubo. Un cono inscrito en un cilindro comparte con él la base y la altura. Una pirámide inscrita en un cubo tiene por base una cara y su vértice en la cara opuesta.",
        "Un prisma recto de aristas a, b y c inscrito en una esfera tiene sus ocho vértices sobre la esfera, y el diámetro es la diagonal del prisma: raíz de (a² + b² + c²). Con esto se comparan volúmenes: el cono inscrito ocupa 1/3 del cilindro, y la esfera inscrita en un cilindro (de modo que toque la base, la tapa y el costado) ocupa 2/3 del cilindro.",
        "Para argumentar una relación se declara qué toca a qué, se dibuja una sección que muestre la situación y se calculan las medidas con esos datos. Al comparar volúmenes se usa una razón: si es la misma para distintas medidas, aparece una regla que se puede enunciar y verificar con otro caso.",
    ],
    vocab=[("figura inscrita", "figura dentro de otra que la toca de modo definido"), ("esfera inscrita en un cubo", "esfera que toca el centro de cada cara"), ("diagonal del prisma", "segmento entre dos vértices opuestos"), ("diámetro", "doble del radio de la esfera"), ("razón de volúmenes", "cociente entre dos volúmenes"), ("arista", "segmento donde se juntan dos caras")],
    worked=[
        ("Esfera en un cubo", "Un cubo de arista 4 cm tiene una esfera inscrita. ¿Cuánto mide el radio y cuál es el volumen de la esfera?", ["El diámetro es la arista, 4 cm, así que el radio es 2 cm.", "El volumen es 4/3 · π · 2³ = 32π/3."], "Radio 2 cm y volumen 32π/3 cm³"),
        ("Prisma en una esfera", "Un prisma de 2 cm por 3 cm por 6 cm está inscrito en una esfera. ¿Cuánto mide el diámetro?", ["El diámetro es la diagonal: raíz de 4 + 9 + 36 = 49.", "La raíz de 49 es 7."], "El diámetro es 7 cm"),
    ],
    mistakes=[("Decir que el diámetro de la esfera que rodea a un cubo es igual a su arista.", "Eso vale para la esfera inscrita en el cubo; la que lo rodea tiene como diámetro la diagonal.", "Revisa qué toca a qué antes de elegir la medida."),
              ("Olvidar el cuadrado o el cubo en las fórmulas de volumen.", "El volumen depende de tres longitudes.", "Escribe la fórmula con los exponentes antes de reemplazar.")],
    T=[
        ('abc', '{F} ¿Cuál es el radio de la esfera inscrita en el cubo?', '3 cm', '6 cm', '12 cm', 'El diámetro es la arista de 6 cm, así que el radio es la mitad.'),
        ('=', '{F} ¿Cuál es el volumen del cubo?', '6*6*6', 'El volumen es arista al cubo.', ' cm³'),
        ('ab', 'Un cono inscrito en un cilindro comparte con él:', 'La base y la altura', 'Solo el radio', 'Para estar inscrito debe apoyarse en la misma base y llegar a la misma altura.'),
        ('{F} ¿Cuál es el volumen de la esfera inscrita en el cubo?', '36π cm³', 'Con r = 3: 4/3 · π · 27 = 36π.'),
        ('{F} ¿Cuál es el volumen del cilindro de radio 3 cm y altura 6 cm?', '54π cm³', 'Se calcula π · 9 · 6.'),
        ('=', '{F} ¿Cuál es el volumen de la pirámide inscrita en el cubo? Su base mide 6 por 6 y su altura 6.', '6*6*6//3', 'El volumen es un tercio de la base por la altura.', ' cm³'),
        ('abc', '{F} ¿Qué fracción del volumen del cilindro ocupa el cono inscrito?', '1/3', '1/2', '2/3', 'Cono y cilindro comparten base y altura, así que el cono es 1/3 del cilindro.'),
        ('Un prisma de base 4 por 4 y altura 7 está inscrito en una esfera. ¿Cuál es el diámetro de la esfera?', '9 cm', 'Es la diagonal: 16 + 16 + 49 = 81 y su raíz es 9.'),
        ('{F} Con los volúmenes del cilindro y de la esfera inscrita, ¿qué fracción del cilindro ocupa la esfera?', '2/3', 'Se divide 36π entre 54π, que da 2/3.'),
        ('abc', 'Una estudiante dice que el diámetro de la esfera inscrita en un cubo de arista 6 cm es 6 cm. ¿Qué argumento lo justifica?', 'La esfera toca dos caras opuestas, separadas por 6 cm', 'La esfera siempre mide lo mismo que el lado', 'La esfera toca las aristas del cubo', 'El contacto con caras opuestas fija el diámetro en la distancia que las separa.'),
        ('abc', 'Un estudiante dice que un cubo inscrito en una esfera tiene arista igual al diámetro. ¿Cuál es el error?', 'El diámetro es la diagonal del cubo, que es mayor que la arista', 'El diámetro es la diagonal de una cara del cubo', 'La arista es la mitad del diámetro', 'Los vértices del cubo están sobre la esfera, y la distancia entre vértices opuestos es el diámetro.'),
        ('{F} ¿Cuál es la razón entre el volumen de la esfera inscrita y el volumen del cubo?', 'π/6', 'Se divide 36π entre 216, que da π/6.'),
        ('Un prisma de 2 cm por 6 cm por 9 cm está inscrito en una esfera. ¿Cuál es el diámetro?', '11 cm', 'Se calcula 4 + 36 + 81 = 121 y la raíz de 121 es 11.'),
    ],
    ctx=('abc', 'Un envase cilíndrico de radio 3 cm y altura 6 cm guarda una pelota esférica de radio 3 cm. ¿Cuánto volumen de aire queda libre?', '18π cm³', '36π cm³', '90π cm³', 'El cilindro tiene 54π y la pelota 36π, así que sobran 54π − 36π = 18π.'),
    sc=[
        ("En Geometría 3D: ¿qué relación hay entre el diámetro de una esfera inscrita en un cubo y su arista?", "Son iguales", "La esfera toca caras opuestas, separadas por la arista."),
        ("¿Qué fracción del cilindro ocupa un cono inscrito?", "1/3", "Comparten la misma base y la misma altura."),
        ("¿Qué mide el diámetro de la esfera que rodea a un prisma?", "Su diagonal", "Los vértices opuestos están sobre la esfera."),
    ],
    op=("Elige un caso: (a) un cubo de arista 10 cm con una esfera inscrita: calcula su radio y la fracción del volumen del cubo que ocupa (deja π). (b) Una caja de 3 cm por 4 cm por 12 cm dentro de una esfera: calcula el diámetro y explica qué toca a qué. Justifica con un esquema.",
        "Caso (b): la diagonal de la caja es la raíz de 9 + 16 + 144 = 169, es decir, 13 cm; los ocho vértices de la caja están sobre la esfera, así que el diámetro es 13 cm.",
        ["declara qué toca a qué", "calcula con la fórmula correcta", "justifica la medida con un esquema"],
        ["hoja con un esquema y cálculos"],
        ["confundir arista con diagonal", "olvidar exponentes", "no justificar el contacto"],
        "Pregunta: «¿cuál es la distancia entre los puntos de contacto?». Eso da el diámetro."),
    reinforce="Con una caja de cartón y una pelota pequeña, observa qué toca la pelota en la caja y explica por qué el diámetro coincide con la arista.",
    extend="Explica por qué la razón del volumen de la esfera inscrita en un cubo no depende de la arista elegida.",
)
