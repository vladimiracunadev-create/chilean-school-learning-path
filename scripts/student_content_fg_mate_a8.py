"""Cuaderno del estudiante de 4.º medio Matemática FG: OAC 04 (rectas y circunferencias en el plano cartesiano)."""
from __future__ import annotations

import math
from fractions import Fraction as F

from fg_mate_common import L, chk, ex

OA4 = "FG-MATE-4M-OAC-04"


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


# ================================================================ OAC 04 clase 1
chk(dist((1, 2), (7, 10)) == 10 and dist((0, 0), (3, 4)) == 5 and dist((-1, 2), (4, 14)) == 13 and dist((1, 2), (4, 6)) == 5)
chk(F(8 - 2, 7 - 1) == 1 and F(10 - 2, 7 - 1) == F(4, 3) and F(8 - 2, 3 - 1) == 3 and F(1 - 5, 4 - 0) == -1 and (3 * 2 - (-1), 1 * 2 - 4) == (7, -2))
chk(F(5 - 1, 2 - 0) == 2 and F(11 - 5, 5 - 2) == 2 and F(10 - 2, 5 - 1) == 2 and (6 - 2) / 2 == 2 and (1 - 1) ** 2 + 16 == 16)
chk(all(abs(dist((1, 1), (x, 5)) - 5) < 1e-9 for x in (4, -2)) and dist((0, 0), (6, 0)) + dist((6, 0), (0, 8)) + dist((0, 8), (0, 0)) == 24)
L(OA4, 1,
  use="Aprenderé a describir puntos y segmentos del plano con coordenadas: distancia, punto medio y pendiente. Sirve para resolver problemas de rectas con cálculos y no solo con dibujos.",
  prior=["Sé ubicar puntos (x, y) en el plano.", "Sé usar el teorema de Pitágoras."],
  explain=[
      "En el plano cartesiano, la distancia entre A(x₁, y₁) y B(x₂, y₂) sale de Pitágoras: d = √((x₂ − x₁)² + (y₂ − y₁)²). El punto medio del segmento AB tiene coordenadas M = ((x₁ + x₂) ÷ 2, (y₁ + y₂) ÷ 2), es decir, el promedio de cada coordenada.",
      "La pendiente de la recta que pasa por A y B mide cuánto sube y por cada unidad que avanza x: m = (y₂ − y₁) ÷ (x₂ − x₁), con x₁ distinto de x₂. Si m > 0 la recta sube, si m < 0 baja y si m = 0 es horizontal. Una recta vertical (x₁ = x₂) tiene pendiente no definida. Tres puntos están alineados si las pendientes entre ellos son iguales.",
      "Antes de calcular, identifica qué objeto es cada cosa: puntos, segmentos y rectas. Una distancia no es una pendiente, y el punto medio es un punto, no un número. Dibujar un esquema rápido en el plano ayuda a detectar un error de signo o una resta al revés.",
  ],
  vocab=[("distancia entre puntos", "longitud del segmento que los une"), ("punto medio", "punto que divide un segmento en dos partes iguales"), ("pendiente", "razón entre el cambio de y y el cambio de x"), ("colineales", "puntos que están en una misma recta"), ("recta vertical", "recta paralela al eje y, con x constante")],
  worked=[
      ("Tres cálculos", "Dados A(1, 2) y B(7, 10), calcula la distancia AB, el punto medio y la pendiente.",
       ["d = √((7 − 1)² + (10 − 2)²) = √(36 + 64) = 10.", "M = ((1 + 7) ÷ 2, (2 + 10) ÷ 2) = (4, 6).", "m = (10 − 2) ÷ (7 − 1) = 8/6 = 4/3."],
       "d = 10; M = (4, 6); m = 4/3"),
      ("Recta vertical", "Para C(−2, 3) y D(−2, 9), calcula la distancia y la pendiente.",
       ["Las dos x son iguales, entonces la recta es vertical.", "d = 9 − 3 = 6. La pendiente tendría denominador 0."],
       "d = 6; la pendiente no está definida"),
  ],
  mist=[
      ("Calcular la distancia como (x₂ − x₁) + (y₂ − y₁).", "Se suman las diferencias en lugar de usar Pitágoras.", "Eleva al cuadrado cada diferencia, suma y saca la raíz."),
      ("Escribir la pendiente como (x₂ − x₁) ÷ (y₂ − y₁).", "Se invirtió el cociente.", "La pendiente es cambio de y sobre cambio de x."),
  ],
  R=[ex("Calcula la distancia entre (0, 0) y (3, 4).", "5", "√(9 + 16) = 5."),
     ex("Calcula el punto medio entre (2, 4) y (6, 10).", "(4, 7)", "(2 + 6) ÷ 2 = 4 y (4 + 10) ÷ 2 = 7."),
     ex("Calcula la pendiente de la recta por (1, 2) y (3, 8).", "3", "(8 − 2) ÷ (3 − 1) = 6 ÷ 2.")],
  C=[ex("Calcula la distancia entre (−1, 2) y (4, 14).", "13", "√(25 + 144) = 13."),
     ex("Calcula el punto medio entre (−3, 5) y (7, −1).", "(2, 2)", "(−3 + 7) ÷ 2 = 2 y (5 − 1) ÷ 2 = 2."),
     ex("Calcula la pendiente de la recta por (0, 5) y (4, 1).", "−1", "(1 − 5) ÷ (4 − 0) = −4 ÷ 4.")],
  A=[ex("El punto M(3, 1) es el punto medio de AB y A es (−1, 4). ¿Cuáles son las coordenadas de B?", "(7, −2)", "2 · 3 − (−1) = 7 y 2 · 1 − 4 = −2."),
     ex("Un triángulo tiene vértices (0, 0), (6, 0) y (0, 8). ¿Cuál es su perímetro?", "24", "Los lados miden 6, 8 y 10."),
     ex("Calcula la pendiente de la recta por (2, 3) y (9, 3).", "0", "Las dos y son iguales: la recta es horizontal.")],
  Z=[ex("¿Están alineados A(0, 1), B(2, 5) y C(5, 11)? A) Sí B) No", "A", "Las pendientes AB y BC valen 2."),
     ex("Marta dice que la pendiente de la recta por (1, 3) y (1, 9) es 0. ¿Qué es correcto? A) Es 0 B) No está definida, la recta es vertical", "B", "El denominador x₂ − x₁ vale 0.")],
  D=[ex("¿Qué valor de k hace que A(1, 2), B(3, k) y C(5, 10) estén alineados?", "6", "La pendiente AC es 2 y (k − 2) ÷ 2 = 2."),
     ex("La distancia entre (1, 1) y (x, 5) es 5. ¿Cuánto vale x?", "x = 4 o x = −2", "(x − 1)² + 16 = 25 da x − 1 = 3 o x − 1 = −3.")],
  ctx=[ex("En un mapa cuadriculado de ejemplo (1 unidad = 1 km), una escuela está en (1, 2) y un parque en (4, 6). ¿Cuál es la distancia en línea recta?", "5 km", "√(9 + 16) = 5.")],
  chk=[ex("¿Qué pendiente tiene una recta horizontal?", "0", "No cambia la altura."),
       ex("¿Qué es el punto medio de (0, 0) y (10, 6)?", "(5, 3)", "Promedio de cada coordenada."),
       ex("¿Cuánto mide el segmento entre (2, 2) y (5, 6)?", "5", "√(9 + 16) = 5.")],
  op=("En un plano de ejemplo, un dron sale de A(−4, 1), pasa por B(2, 9) y llega a C(8, 17). Calcula las distancias AB y BC, el punto medio de AC y las pendientes de AB y BC. Decide si los tres puntos están alineados y, si no, explica cómo lo sabes. Dibuja los puntos en el plano o usa una aplicación de gráficos para comprobar.",
      "AB = √(36 + 64) = 10; BC = √(36 + 64) = 10. Punto medio de AC = (2, 9), que es B. Pendientes: AB = 8/6 = 4/3; BC = 8/6 = 4/3. Están alineados y B es el punto medio de AC.",
      ["calcula distancias, punto medio y pendientes", "compara las pendientes para decidir", "comprueba con el dibujo o la aplicación"],
      ["tabla de cálculos", "dibujo en el plano"],
      ["restar al revés", "sumar las diferencias sin Pitágoras"],
      "Si una distancia sale negativa, pide que revise que usó cuadrados antes de la raíz."),
  reinforce="Calcula distancia, punto medio y pendiente para P(−2, −1) y Q(4, 7).",
  extend="Muestra con coordenadas que las diagonales de un rectángulo tienen el mismo punto medio.",
)

# ================================================================ OAC 04 clase 2
chk(2 * 3 + 1 == 7 and 3 * 4 - 12 == 0 and 2 * 6 - 12 == 0 and 3 * 1 - 5 == -2 and 3 * 4 - 5 == 7 and 3 * 2 - 5 - 1 == 0 and 3 * 2 - 1 == 5 and -2 + 7 == 5)
chk(F(2) * F(-1, 2) == -1 and F(-2, 3) * F(3, 2) == -1 and 200 * 25 + 3000 == 8000 and F(6 - 0, 3) == 2)
L(OA4, 2,
  use="Aprenderé a representar una recta con su ecuación y con su gráfica, y a pasar de la forma y = mx + n a la forma general. Sirve para encontrar rectas paralelas y perpendiculares y puntos de corte.",
  prior=["Sé calcular la pendiente entre dos puntos.", "Sé despejar una variable en una ecuación."],
  explain=[
      "Toda recta no vertical se puede escribir como y = m·x + n, donde m es la pendiente y n es el intercepto con el eje y (el valor de y cuando x = 0). También se puede escribir en forma general Ax + By + C = 0. Pasar de una a otra es despejar y: de 3x + 2y − 12 = 0 se obtiene y = −(3/2)x + 6.",
      "Para encontrar la ecuación de una recta por dos puntos, se calcula m y se usa y − y₁ = m·(x − x₁). Para graficarla basta con dos puntos, por ejemplo los interceptos con los ejes: el de y se obtiene con x = 0 y el de x con y = 0. La ecuación y la gráfica deben coincidir en cada punto.",
      "Dos rectas con la misma pendiente son paralelas. Dos rectas son perpendiculares cuando el producto de sus pendientes es −1, por ejemplo 2 y −1/2. Para encontrar el punto de corte de dos rectas, se igualan sus expresiones de y y se resuelve la ecuación resultante.",
  ],
  vocab=[("ecuación de la recta", "igualdad que cumplen todos los puntos de una recta"), ("intercepto", "punto donde la recta cruza un eje"), ("forma general", "Ax + By + C = 0"), ("paralelas", "rectas con igual pendiente y distinto intercepto"), ("perpendiculares", "rectas que forman un ángulo recto")],
  worked=[
      ("Ecuación por dos puntos", "Encuentra la ecuación de la recta por (1, 3) y (3, 7) en las formas y = mx + n y general.",
       ["m = (7 − 3) ÷ (3 − 1) = 2.", "y − 3 = 2(x − 1) da y = 2x + 1.", "Forma general: 2x − y + 1 = 0."],
       "y = 2x + 1; 2x − y + 1 = 0"),
      ("De la forma general a la gráfica", "Grafica 3x + 2y − 12 = 0 usando sus interceptos.",
       ["Con x = 0: 2y = 12 y y = 6. Con y = 0: 3x = 12 y x = 4.", "Uno los puntos (0, 6) y (4, 0)."],
       "Pasa por (0, 6) y (4, 0); y = −(3/2)x + 6"),
  ],
  mist=[
      ("Decir que las rectas y = 2x + 1 y y = −2x + 5 son perpendiculares.", "El producto de sus pendientes es −4, no −1.", "Para ser perpendicular a pendiente 2 se necesita pendiente −1/2."),
      ("Confundir el intercepto con la pendiente en y = −3x + 4.", "El 4 es el valor de y en x = 0 y el −3 es la pendiente.", "Lee m = −3 y n = 4."),
  ],
  R=[ex("Si y = 2x + 1, ¿cuánto vale y cuando x = 3?", "7", "2 · 3 + 1."),
     ex("¿Cuál es la pendiente de y = −3x + 4?", "−3", "Es el número que multiplica a x."),
     ex("¿Cuál es el intercepto con el eje y de y = 5x − 2?", "−2", "Es el valor de y cuando x = 0.")],
  C=[ex("Escribe la ecuación de la recta de pendiente 3 que pasa por (0, 1).", "y = 3x + 1", "El intercepto es 1."),
     ex("Despeja y en 2x + y − 6 = 0.", "y = −2x + 6", "y = 6 − 2x."),
     ex("¿Cuál es el intercepto con el eje x de y = 2x − 6?", "3", "Con y = 0, 2x = 6.")],
  A=[ex("Encuentra la ecuación de la recta por (2, 1) y (4, 7).", "y = 3x − 5", "m = 6 ÷ 2 = 3 y 1 = 3 · 2 + n da n = −5."),
     ex("Escribe la recta paralela a y = 3x − 5 que pasa por (0, 2).", "y = 3x + 2", "Misma pendiente 3 e intercepto 2."),
     ex("¿Qué pendiente tiene una recta perpendicular a y = 2x + 1?", "−1/2", "2 · (−1/2) = −1.")],
  Z=[ex("¿Son perpendiculares y = 2x + 3 e y = −x/2 + 1? A) Sí B) No", "A", "2 · (−1/2) = −1."),
     ex("¿Se cortan las rectas y = 3x + 1 e y = 3x + 4? A) Sí B) No, son paralelas", "B", "Tienen la misma pendiente e interceptos distintos.")],
  D=[ex("Encuentra el punto donde se cortan 3x − y − 1 = 0 e y = −x + 7.", "(2, 5)", "3x − 1 = −x + 7 da x = 2 e y = 5."),
     ex("Escribe la recta perpendicular a 2x + 3y − 6 = 0 que pasa por el origen.", "y = (3/2)x", "La pendiente de la dada es −2/3 y la perpendicular es 3/2.")],
  ctx=[ex("Un plan de ejemplo cobra $3.000 fijos más $200 por minuto. Con y el costo y x los minutos, la ecuación es y = 200x + 3.000. ¿Cuánto se paga por 25 minutos?", "$8.000", "200 · 25 + 3.000.")],
  chk=[ex("Escribe 2x − y + 4 = 0 en la forma y = mx + n.", "y = 2x + 4", "Se despeja y: y = 2x + 4."),
       ex("Si dos rectas tienen pendientes 4 y 4, ¿cómo son?", "Paralelas", "Tienen la misma pendiente."),
       ex("¿Cuánto vale y en x = 0 para y = −2x + 9?", "9", "Es el intercepto.")],
  op=("Un sendero de ejemplo pasa por los puntos A(0, 2) y B(4, 10) de un plano (1 unidad = 100 m). Escribe su ecuación en las formas y = mx + n y general, encuentra sus interceptos con los ejes, y escribe la ecuación de otro sendero paralelo que pasa por (1, 0) y de uno perpendicular que pasa por A. Dibuja los tres senderos en un mismo plano, a mano o con una aplicación de gráficos.",
      "m = 8 ÷ 4 = 2, y = 2x + 2, forma general 2x − y + 2 = 0. Interceptos: (0, 2) y (−1, 0). Paralelo por (1, 0): y = 2x − 2. Perpendicular por A: pendiente −1/2, y = −(1/2)x + 2.",
      ["obtiene la pendiente y la ecuación por dos puntos", "escribe rectas paralela y perpendicular con el criterio correcto", "dibuja los tres senderos con coherencia"],
      ["ecuaciones escritas", "dibujo con los tres senderos"],
      ["confundir pendiente con intercepto", "usar la misma pendiente para perpendiculares"],
      "Si el dibujo no coincide con la ecuación, pide que marque dos puntos de la ecuación y compruebe que están en el dibujo."),
  reinforce="Encuentra la ecuación de la recta por (0, 4) y (2, 0) y su forma general.",
  extend="Explica por qué dos rectas perpendiculares con pendientes m y n cumplen m · n = −1, usando un giro de 90°.",
)

# ================================================================ OAC 04 clase 3
chk((3 - 2) ** 2 == 1 and (5 - 2) ** 2 + 0 == 9 and 12 + 4 + 9 == 25 and dist((1, 2), (7, 10)) / 2 == 5 and 3 ** 2 + 4 ** 2 == 25 and 4 ** 2 + 3 ** 2 > 9)
chk(all(x * x + (x + 1) ** 2 == 25 for x in (3, -4)) and all(abs(dist((x, y), (2, 1)) ** 2 - 5) < 1e-9 for x, y in ((0, 0), (4, 0), (0, 2))) and math.hypot(5 - 2, 7 - 3) == 5)
chk(4 * 2 ** 2 - 8 * (2 ** 2 - 2) == 0 and 4 * (-2) ** 2 - 8 * ((-2) ** 2 - 2) == 0)
L(OA4, 3,
  use="Aprenderé a escribir la ecuación de una circunferencia, a pasar de la forma general a la forma con centro y radio, y a encontrar dónde la corta una recta. Sirve para resolver problemas de alcance, cobertura y posición.",
  prior=["Sé calcular la distancia entre dos puntos.", "Sé completar el cuadrado de un binomio y resolver ecuaciones de segundo grado."],
  explain=[
      "Una circunferencia es el conjunto de puntos a una distancia r de un centro C(h, k). De la fórmula de distancia sale su ecuación: (x − h)² + (y − k)² = r². Si el centro es el origen, queda x² + y² = r². Fíjate en los signos: (x + 3)² corresponde a h = −3.",
      "La ecuación también puede venir en forma general x² + y² + Dx + Ey + F = 0. Para encontrar el centro y el radio se completan cuadrados en x y en y. Un punto P está dentro de la circunferencia si su distancia al centro es menor que r, sobre ella si es igual y fuera si es mayor.",
      "Para encontrar la intersección entre una recta y una circunferencia, se despeja y de la recta, se reemplaza en la ecuación de la circunferencia y se resuelve la ecuación de segundo grado. Si el discriminante es positivo hay dos puntos; si es cero hay uno (la recta es tangente); si es negativo no hay ninguno.",
  ],
  vocab=[("circunferencia", "puntos del plano a igual distancia de un centro"), ("radio", "distancia del centro a cualquier punto de la circunferencia"), ("completar cuadrados", "reescribir x² + bx como (x + b/2)² − (b/2)²"), ("discriminante", "valor b² − 4ac que indica cuántas soluciones reales tiene una ecuación de segundo grado"), ("tangente", "recta que toca la circunferencia en un solo punto")],
  worked=[
      ("Escribir y verificar una ecuación", "Escribe la ecuación de la circunferencia de centro (2, −1) y radio 3, y comprueba si (5, −1) está en ella.",
       ["(x − 2)² + (y − (−1))² = 3² da (x − 2)² + (y + 1)² = 9.", "Reemplazo (5, −1): 3² + 0² = 9, que cumple la ecuación."],
       "(x − 2)² + (y + 1)² = 9; el punto (5, −1) sí está en ella"),
      ("Completar cuadrados", "Encuentra el centro y el radio de x² + y² − 4x + 6y − 12 = 0.",
       ["Agrupo: (x² − 4x) + (y² + 6y) = 12.", "Completo: (x − 2)² − 4 + (y + 3)² − 9 = 12.", "Entonces (x − 2)² + (y + 3)² = 25."],
       "Centro (2, −3) y radio 5"),
  ],
  mist=[
      ("Decir que (x − 2)² + (y + 3)² = 25 tiene centro (2, 3).", "El signo de la ecuación es opuesto al de la coordenada del centro.", "(y + 3)² = (y − (−3))², por lo que k = −3."),
      ("Escribir el radio como 25 en la ecuación (x − 2)² + (y + 3)² = 25.", "El número de la derecha es r², no r.", "r = √25 = 5."),
  ],
  R=[ex("Escribe la ecuación de la circunferencia de centro (0, 0) y radio 5.", "x² + y² = 25", "r² = 25."),
     ex("¿Cuáles son el centro y el radio de (x − 1)² + (y − 4)² = 16?", "Centro (1, 4) y radio 4", "r² = 16 y r = 4."),
     ex("¿Está (3, 4) sobre x² + y² = 25?", "Sí", "9 + 16 = 25.")],
  C=[ex("¿Cuál es el centro de (x + 3)² + (y − 2)² = 49?", "(−3, 2)", "x + 3 = x − (−3)."),
     ex("Escribe la ecuación de la circunferencia de centro (1, −2) y radio 2.", "(x − 1)² + (y + 2)² = 4", "r² = 4."),
     ex("Respecto de x² + y² = 9, ¿el punto (4, 0) está dentro o fuera?", "Fuera", "16 es mayor que 9.")],
  A=[ex("Encuentra el centro y el radio de x² + y² − 6x + 8y = 0.", "Centro (3, −4) y radio 5", "(x − 3)² + (y + 4)² = 9 + 16."),
     ex("Una circunferencia tiene como diámetro el segmento de A(1, 2) a B(7, 10). ¿Cuáles son su centro y su radio?", "Centro (4, 6) y radio 5", "El centro es el punto medio y el diámetro mide 10."),
     ex("¿En qué puntos corta la recta y = x + 1 a la circunferencia x² + y² = 25?", "(3, 4) y (−4, −3)", "x² + (x + 1)² = 25 da x² + x − 12 = 0, con x = 3 o x = −4.")],
  Z=[ex("Mario completó cuadrados en x² + y² − 6x = 0 y escribió (x + 3)² + y² = 9. ¿Cuál es su error? A) El signo: debe ser (x − 3)² B) El lado derecho debe ser 3", "A", "x² − 6x = (x − 3)² − 9, por lo que queda (x − 3)² + y² = 9, con centro (3, 0)."),
     ex("¿Cuántos puntos comunes tienen x² + y² = 4 y la recta y = 3?", "0", "La distancia del centro a la recta es 3, mayor que el radio 2.")],
  D=[ex("¿Para qué valores de k la recta y = x + k es tangente a x² + y² = 2?", "k = 2 o k = −2", "x² + (x + k)² = 2 da 2x² + 2kx + k² − 2 = 0; su discriminante es 16 − 4k² = 0."),
     ex("Encuentra la ecuación de la circunferencia que pasa por (0, 0), (4, 0) y (0, 2).", "(x − 2)² + (y − 1)² = 5", "El centro (2, 1) está a la misma distancia √5 de los tres puntos.")],
  ctx=[ex("Una antena de ejemplo en (2, 3) tiene un alcance de 5 m (1 unidad = 1 m). Una casa está en (5, 7). ¿Queda dentro, en el borde o fuera del alcance?", "En el borde", "La distancia es √(9 + 16) = 5.")],
  chk=[ex("Escribe el radio de x² + y² = 36.", "6", "El radio es √36."),
       ex("Si el discriminante es 0, ¿cuántos puntos comunes tienen la recta y la circunferencia?", "1", "La recta es tangente."),
       ex("¿Cuál es el centro de x² + (y − 5)² = 9?", "(0, 5)", "x² = (x − 0)².")],
  op=("En un plano de ejemplo, una estación de radio está en (1, 2) y cubre hasta 5 km (1 unidad = 1 km). Escribe la ecuación de la zona de cobertura. Decide si las ciudades P(4, 6), Q(5, 5) y R(−3, 1) quedan dentro, en el borde o fuera. Una carretera recta es y = 2: encuentra dónde cruza el borde de la cobertura. Dibuja todo o usa una aplicación de gráficos para comprobar.",
      "(x − 1)² + (y − 2)² = 25. P: 9 + 16 = 25, en el borde. Q: 16 + 9 = 25, en el borde. R: 16 + 1 = 17, dentro. La carretera y = 2 da (x − 1)² = 25, con x = 6 o x = −4: cruza en (6, 2) y (−4, 2).",
      ["escribe correctamente la ecuación con signos", "clasifica cada punto con la distancia", "calcula la intersección y comprueba con el dibujo"],
      ["ecuación y tabla de ciudades", "dibujo con la carretera"],
      ["usar el signo del centro al revés", "olvidar elevar el radio al cuadrado"],
      "Si una ciudad queda mal clasificada, pide que calcule la distancia al centro con la fórmula y compare con 5."),
  reinforce="Encuentra el centro y el radio de x² + y² + 2x − 4y − 4 = 0.",
  extend="Muestra por qué x² + y² + 2x + 4y + 10 = 0 no representa ninguna circunferencia real.",
)

# ================================================================ OAC 04 clase 4
chk(3 * 3 + 4 * 4 - 25 == 0 and F(4, 3) * F(-3, 4) == -1 and F(10, 5) == 2 and F(39, 13) == 3 and F(15, 5) == 3 and F(20, 5) == 4 and F(30, 5) == 6)
chk(F(3, 4) * F(-4, 3) == -1 and F(3 * 2 + 4 * 1 - 20, 5) == -2 and math.hypot(4 - 1, 6 - 2) == 5 and F(6 - 2, 4 - 1) == F(4, 3) and F(4, 8) == F(1, 2) and F(4, -2) == -2)
chk(F(1, 2) * -2 == -1 and F(10, 5) == 2 and math.isclose(2 * math.sqrt(5), 4.4721, abs_tol=1e-3) and 9 - 4 == 5)
L(OA4, 4,
  use="Aprenderé a justificar con cálculos relaciones entre rectas y circunferencias: la tangente es perpendicular al radio y la distancia del centro a una recta decide cuántos puntos tienen en común. Sirve para demostrar propiedades con coordenadas.",
  prior=["Sé la ecuación de una recta y de una circunferencia.", "Sé que rectas perpendiculares tienen pendientes de producto −1."],
  explain=[
      "La tangente a una circunferencia en un punto P es perpendicular al radio que llega a P. Si el radio tiene pendiente m, la tangente tiene pendiente −1/m. Por ejemplo, en x² + y² = 25 el punto (3, 4) tiene radio de pendiente 4/3 y la tangente tiene pendiente −3/4.",
      "La distancia de un punto (x₀, y₀) a la recta Ax + By + C = 0 es d = |A·x₀ + B·y₀ + C| ÷ √(A² + B²). Si d es mayor que el radio, la recta no toca a la circunferencia; si d es igual al radio, es tangente; si d es menor, la corta en dos puntos. En ese caso la mitad de la cuerda mide √(r² − d²).",
      "Para justificar una propiedad con coordenadas, escribe qué se supone, qué se calcula y qué se concluye. Por ejemplo, si un triángulo tiene un lado que es diámetro y el tercer vértice está en la circunferencia, las pendientes de los otros dos lados tienen producto −1: el ángulo es recto. Un ejemplo numérico respalda la propiedad pero no la demuestra en general.",
  ],
  vocab=[("tangente", "recta que toca la circunferencia en un solo punto"), ("perpendicular", "que forma un ángulo recto"), ("distancia punto-recta", "longitud del segmento perpendicular del punto a la recta"), ("cuerda", "segmento que une dos puntos de la circunferencia"), ("justificar", "dar razones que respaldan una afirmación")],
  worked=[
      ("Ecuación de una tangente", "Encuentra la ecuación de la tangente a x² + y² = 25 en (3, 4).",
       ["La pendiente del radio es 4/3, entonces la de la tangente es −3/4.", "y − 4 = −(3/4)(x − 3) da 4y − 16 = −3x + 9.", "Forma general: 3x + 4y − 25 = 0."],
       "3x + 4y − 25 = 0"),
      ("Posición de una recta", "¿Cuántos puntos comunes tienen 3x + 4y − 10 = 0 y x² + y² = 9?",
       ["d = |3·0 + 4·0 − 10| ÷ √(9 + 16) = 10 ÷ 5 = 2.", "Como 2 < 3, la recta corta a la circunferencia en dos puntos."],
       "Dos puntos"),
  ],
  mist=[
      ("Usar la misma pendiente del radio para la tangente.", "La tangente es perpendicular al radio, no paralela.", "Usa la pendiente −1/m."),
      ("Calcular la distancia a la recta sin el valor absoluto.", "Una distancia no puede ser negativa.", "Usa |A·x₀ + B·y₀ + C|."),
  ],
  R=[ex("¿Cuál es el producto de las pendientes de dos rectas perpendiculares?", "−1", "Es la condición de perpendicularidad."),
     ex("Calcula la distancia del origen a la recta 5x + 12y − 39 = 0.", "3", "|−39| ÷ √(25 + 144) = 39 ÷ 13."),
     ex("Si la distancia del centro a una recta es mayor que el radio, ¿cuántos puntos comunes hay?", "0", "La recta pasa lejos de la circunferencia.")],
  C=[ex("En x² + y² = 25, ¿cuál es la pendiente de la tangente en (4, 3)?", "−4/3", "El radio tiene pendiente 3/4."),
     ex("Calcula la distancia del punto (2, 1) a la recta 3x + 4y − 20 = 0.", "2", "|6 + 4 − 20| ÷ 5 = 10 ÷ 5."),
     ex("Una recta está a 2 unidades del centro de una circunferencia de radio 2. ¿Cómo es la recta?", "Tangente", "La distancia es igual al radio.")],
  A=[ex("¿Cuántos puntos comunes tienen 3x + 4y − 15 = 0 y x² + y² = 9?", "1", "d = 15 ÷ 5 = 3, igual al radio."),
     ex("¿Cuántos puntos comunes tienen 3x + 4y − 20 = 0 y x² + y² = 9?", "0", "d = 20 ÷ 5 = 4, mayor que 3."),
     ex("La circunferencia tiene centro (1, 2) y radio 5, y el punto (4, 6) está en ella. ¿Cuál es la pendiente de la tangente en ese punto?", "−3/4", "El radio tiene pendiente 4/3.")],
  Z=[ex("Un estudiante dice que dos rectas de pendientes 2 y −2 son perpendiculares. ¿Es correcto? A) Sí B) No: el producto es −4", "B", "Para ser perpendicular a 2 se necesita −1/2."),
     ex("Los puntos A(−5, 0), B(5, 0) y C(3, 4) están en x² + y² = 25. ¿Es recto el ángulo en C?", "Sí", "Las pendientes CA = 1/2 y CB = −2 tienen producto −1.")],
  D=[ex("¿Para qué valores de c la recta 3x + 4y + c = 0 es tangente a x² + y² = 4?", "c = 10 o c = −10", "|c| ÷ 5 = 2."),
     ex("La recta 3x + 4y − 10 = 0 corta a x² + y² = 9 (d = 2). ¿Cuánto mide la cuerda que determina, en forma exacta?", "2√5", "La mitad de la cuerda es √(9 − 4) = √5.")],
  ctx=[ex("Una laguna de ejemplo es la circunferencia x² + y² = 16 (1 unidad = 1 km). Un camino recto es 3x + 4y − 20 = 0. ¿El camino cruza la laguna o solo la toca?", "Solo la toca", "d = 20 ÷ 5 = 4, igual al radio.")],
  chk=[ex("¿Qué relación hay entre una tangente y el radio en el punto de tangencia?", "Son perpendiculares", "Forman un ángulo recto."),
       ex("Si d es menor que el radio, ¿cuántos puntos comunes hay?", "2", "La recta corta a la circunferencia."),
       ex("¿Puede ser negativa una distancia entre un punto y una recta?", "No", "Por eso se usa el valor absoluto.")],
  op=("Para la circunferencia x² + y² = 20 de un plano de ejemplo, encuentra la ecuación de la tangente en el punto (2, 4). Comprueba con dos argumentos: la distancia del origen a esa recta debe ser igual al radio y la tangente debe ser perpendicular al radio. Escribe también cuántos puntos comunes tiene la recta x + 2y − 15 = 0 con la circunferencia. Usa una aplicación de gráficos para verificar.",
      "El radio tiene pendiente 2 y la tangente −1/2: y − 4 = −(1/2)(x − 2), es decir, x + 2y − 10 = 0. Distancia: 10 ÷ √5 = 2√5 = √20, que es el radio. Para x + 2y − 15 = 0: d = 15 ÷ √5 = 3√5 ≈ 6,7, mayor que √20 ≈ 4,5, entonces no hay puntos comunes.",
      ["calcula la pendiente de la tangente", "comprueba con la distancia y la perpendicularidad", "decide la posición de la segunda recta"],
      ["ecuación de la tangente", "dos comprobaciones y conclusión"],
      ["usar la pendiente del radio para la tangente", "olvidar el valor absoluto"],
      "Si la distancia no coincide con el radio, pide que revise el cálculo de la ecuación general de la tangente."),
  reinforce="Encuentra la tangente a x² + y² = 13 en (2, 3).",
  extend="Demuestra con coordenadas que un triángulo con vértices A(−r, 0), B(r, 0) y C(x, y) sobre x² + y² = r² tiene un ángulo recto en C.",
)
