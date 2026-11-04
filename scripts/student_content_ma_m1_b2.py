"""Cuaderno del estudiante de 1.º medio Matemática, OA 13 (comparar poblaciones con gráficos xy y separar con una recta): clases 1 a 4."""
from __future__ import annotations

from student_content_ma_m1_b import L, MAT
from student_lessons import arith, ex

OA13 = "MA1M OA 13"


def pts(data):
    """Escribe una lista de pares como «(x, y), (x, y)»."""
    return ", ".join(f"({x}, {y})" for x, y in data)


def recta(a, b):
    """Texto de la recta y = a·x + b con a y b enteros."""
    if a == 0:
        return f"y = {b}"
    base = "y = x" if a == 1 else f"y = {a}x"
    return base if b == 0 else f"{base} {'+' if b > 0 else '−'} {abs(b)}"


def lado(data, a, b, where):
    """Cuántos puntos quedan arriba, sobre o debajo de la recta y = a·x + b."""
    if where == "arriba":
        return sum(1 for x, y in data if y > a * x + b)
    if where == "sobre":
        return sum(1 for x, y in data if y == a * x + b)
    return sum(1 for x, y in data if y < a * x + b)


def aciertos(rojos, azules, a, b):
    """Rojos arriba más azules abajo: puntos bien clasificados por la recta."""
    return lado(rojos, a, b, "arriba") + lado(azules, a, b, "abajo")


# ---------------------------------------------------------------- datos
LECT_A = [(10, 1), (15, 2), (20, 3), (30, 4), (35, 5)]            # 1.º A: minutos de lectura al día, libros leídos
LECT_B = [(5, 0), (10, 1), (15, 1), (20, 2), (25, 2)]             # 1.º B
MANANA = [(22, 20), (25, 35), (28, 50), (31, 60)]                  # temperatura (°C), helados vendidos
TARDE = [(22, 25), (25, 40), (28, 60), (31, 75)]
M1 = [(6, 20), (12, 18), (18, 15), (24, 13), (30, 10)]             # meses de uso, horas de batería (modelo 1)
M2 = [(6, 26), (12, 24), (18, 20), (24, 19), (30, 16)]
CURSO_A = [(1, 9), (2, 7), (3, 6), (5, 4), (6, 2)]                 # horas de práctica, errores
CURSO_B = [(1, 6), (2, 5), (4, 3), (5, 2), (7, 1)]
ROJOS_T = [(2, 8), (3, 9), (4, 7), (5, 10), (6, 9), (3, 6)]
AZULES_T = [(6, 3), (7, 4), (8, 2), (9, 5), (10, 3), (7, 1)]
ROJOS_Q = [(1, 7), (2, 8), (3, 6), (4, 9), (2, 10)]
AZULES_Q = [(5, 2), (6, 4), (7, 3), (8, 1), (9, 4)]
W_ROJOS = [(1, 4), (2, 6), (3, 5), (4, 8), (5, 7), (6, 9), (7, 6), (8, 10), (3, 8), (5, 9)]
W_AZULES = [(2, 1), (3, 2), (4, 3), (5, 3), (6, 5), (7, 4), (8, 5), (9, 7), (1, 0), (6, 2)]

assert aciertos(ROJOS_T, AZULES_T, 1, 0) == 12 and aciertos(ROJOS_T, AZULES_T, 0, 5) == 11
assert [aciertos(W_ROJOS, W_AZULES, a, b) for a, b in ((1, 0), (0, 5), (1, 2))] == [19, 15, 16]

# ================================================================ OA 13 · clase 1
L(OA13, 1,
  use="Aprenderé a organizar los datos de dos grupos en una tabla y a dibujarlos como un gráfico xy con puntos de dos colores, para poder compararlos.",
  prior=["Sé construir una nube de puntos con dos datos numéricos.", "Sé elegir una escala adecuada para un eje."],
  explain=[
      "Un gráfico xy muestra dos atributos de cada elemento: el atributo x en el eje horizontal y el atributo y en el vertical. Cuando quieres comparar dos poblaciones, por ejemplo dos cursos, marcas los puntos de una con un color y los de la otra con otro. Si no tienes dos colores, usa dos símbolos distintos, como círculos y triángulos.",
      "Primero se ordena la información en una tabla con tres columnas: grupo, valor de x y valor de y. Así cada fila es un punto. Después se eligen los mismos ejes y la misma escala para los dos grupos, porque con escalas distintas la comparación se distorsiona. Por último se agrega una leyenda que diga qué color es cada grupo.",
      "Cada punto sigue siendo un elemento distinto, así que no se unen. Los puntos de los dos grupos pueden quedar mezclados o separados; eso se analiza en las clases siguientes. Hoy lo importante es construir el gráfico completo, con ejes rotulados, escala, leyenda y todos los puntos de las dos tablas.",
  ],
  vocab=[("gráfico xy", "gráfico que ubica cada elemento según dos atributos, x e y"), ("atributo", "característica medible de un elemento"), ("leyenda", "recuadro que explica qué color o símbolo corresponde a cada grupo"), ("población", "grupo de elementos que se estudia")],
  worked=[
      ("De la tabla al gráfico", f"Se compara a 1.º A (rojo) con 1.º B (azul) con datos de ejemplo de (minutos de lectura al día, libros leídos en el semestre). 1.º A: {pts(LECT_A)}. 1.º B: {pts(LECT_B)}. ¿Cuántos puntos tendrá el gráfico y cómo se arma?",
       ["Se arma una tabla con columnas grupo, minutos y libros: 5 filas de 1.º A y 5 de 1.º B.", "Se eligen ejes comunes: minutos de 0 a 35 y libros de 0 a 5.", "Se marcan los 5 puntos rojos y los 5 azules, y se agrega la leyenda."], "El gráfico tiene 5 + 5 = 10 puntos, en dos colores, con los mismos ejes"),
      ("Leer un punto de un grupo", "En el mismo gráfico, ¿qué dice el punto rojo (30, 4)?",
       ["Es rojo, así que pertenece a 1.º A.", "El valor x es 30 minutos y el valor y es 4 libros."], "Un estudiante de 1.º A que lee 30 minutos al día leyó 4 libros"),
  ],
  mist=[
      ("Dibujar cada grupo con una escala distinta en el eje vertical.", "Con escalas distintas, los dos grupos no se pueden comparar a simple vista.", "Elige una sola escala que sirva para los dos grupos."),
      ("Olvidar la leyenda, o usar el mismo color en los dos grupos.", "Sin leyenda y sin diferencia de color, nadie sabe a qué grupo pertenece cada punto.", "Agrega una leyenda y revisa que cada punto tenga el color de su grupo."),
  ],
  R=[ex("En un gráfico xy con dos poblaciones, ¿qué indica el color de cada punto?", "A qué grupo pertenece el elemento", "El color permite distinguir a qué población corresponde cada punto."),
     arith("Un gráfico tiene 5 puntos rojos y 4 puntos azules. ¿Cuántos puntos tiene en total?", "5+4", "Cada elemento de cada grupo es un punto.", " puntos"),
     ex("El punto triangular (28, 60) pertenece al turno tarde de una heladería. ¿Qué temperatura representa el valor x?", "28 °C", "El primer número del par es el valor x, que aquí es la temperatura.")],
  C=[arith(f"Una heladería registra (temperatura en °C, helados vendidos). Turno mañana: {pts(MANANA)}. Turno tarde: {pts(TARDE)}. ¿Cuántos puntos tiene el gráfico completo con los dos turnos?", "4+4", "Cada turno aporta 4 puntos.", " puntos"),
     ex(f"En la heladería, turno mañana: {pts(MANANA)}. ¿Cuál es el mayor número de helados vendidos en el turno mañana?", "60", "Se busca el mayor valor y entre los puntos de ese turno."),
     ex("¿Por qué se usan los mismos ejes y la misma escala para los dos grupos? A) Para poder comparar las posiciones de los puntos. B) Para que el gráfico ocupe menos espacio. C) Para que los grupos tengan igual cantidad de puntos.", "A", "Solo con la misma escala la posición de un punto significa lo mismo en los dos grupos.")],
  A=[arith("En la heladería, a 25 °C se vendieron 35 helados en el turno mañana y 40 en el turno tarde. ¿Cuántos helados más se vendieron en la tarde?", "40-35", "Se restan los dos valores y del mismo valor x.", " helados"),
     ex(f"Turno tarde de la heladería: {pts(TARDE)}. ¿Cuántos de sus puntos están sobre los 50 helados?", str(sum(1 for _x, y in TARDE if y > 50)), "Superan 50 los puntos con y igual a 60 y 75."),
     arith("En el eje vertical los valores van de 20 a 75 helados y cada cuadrito vale 5. ¿Cuántos cuadritos se necesitan para cubrir ese tramo?", "(75-20)//5", "Se divide la longitud del tramo por el valor de cada cuadrito.", " cuadritos")],
  Z=[ex("Marta dibuja el turno mañana con 5 helados por cuadrito y el turno tarde con 10 helados por cuadrito, en el mismo gráfico. ¿Se pueden comparar bien los dos turnos? Responde sí o no.", "No", "Una misma altura del gráfico significaría cantidades distintas en cada turno."),
     ex("En un gráfico, un círculo está en (25, 35) y un triángulo en (25, 40). Los círculos son el turno mañana y los triángulos el turno tarde. ¿Son dos elementos del mismo grupo? Responde sí o no.", "No", "Los símbolos distintos representan grupos distintos.")],
  D=[ex(f"Turno mañana: {pts(MANANA)}. Turno tarde: {pts(TARDE)}. ¿Cuántos puntos de la tarde quedan por encima del punto más alto de la mañana?", "1", "El punto más alto de la mañana es (31, 60) y solo (31, 75) lo supera."),
     arith("Suma los helados de cada turno: mañana 20, 35, 50 y 60; tarde 25, 40, 60 y 75. ¿Cuántos helados más se vendieron en total en la tarde que en la mañana?", "(25+40+60+75)-(20+35+50+60)", "El total de la tarde es 200 y el de la mañana 165; se restan.", " helados")],
  ctx=[ex("Dos puestos de una feria anotaron (precio de un producto en cientos de pesos, cantidad vendida en la jornada). Puesto de frutas: (5, 30), (8, 24), (10, 18). Puesto de verduras: (5, 26), (8, 20), (10, 15). ¿Cuántos puntos tendrá un gráfico xy con ambos puestos?", "6", "Cada puesto aporta 3 puntos: 3 + 3 = 6.")],
  chk=[ex("¿Cómo se distinguen dos grupos en un gráfico xy?", "Con colores o símbolos distintos y una leyenda", "La leyenda indica qué color o símbolo corresponde a cada grupo."),
       ex("¿Se unen con una línea los puntos de un gráfico xy de dos grupos? Responde sí o no.", "No", "Cada punto es un elemento distinto y no hay orden entre ellos."),
       arith("Un gráfico tiene 7 puntos de un grupo y 6 del otro. ¿Cuántos puntos tiene?", "7+6", "Se suman los puntos de ambos grupos.", " puntos")],
  op=("Con estos datos de ejemplo de dos cursos (minutos de caminata diaria, pasos contados en una prueba de 10 minutos): curso P: (10, 800), (20, 900), (30, 950), (40, 1.100). Curso Q: (10, 700), (20, 780), (30, 820), (40, 900). Arma la tabla con tres columnas, dibuja el gráfico xy con círculos para P y triángulos para Q con ejes comunes, agrega la leyenda y escribe cuántos puntos tiene el gráfico.",
      "Tabla de 8 filas (4 de P y 4 de Q). Eje x: minutos de 0 a 40; eje y: pasos de 600 a 1.200. 4 círculos y 4 triángulos, leyenda al lado. El gráfico tiene 8 puntos.",
      ["tabla con grupo, x e y", "ejes rotulados con unidades", "misma escala para los dos grupos", "símbolos distintos y leyenda", "8 puntos sin unir"],
      ["tabla de 8 filas", "gráfico con leyenda", "frase con el número de puntos"],
      ["usar una escala distinta para cada grupo", "olvidar la leyenda", "unir los puntos con líneas"],
      "Pide que identifique en el gráfico a qué curso corresponde un punto elegido. Reconoce que los dos grupos compartan ejes."),
  reinforce="Dibuja los dos turnos de la heladería (mañana con círculos y tarde con triángulos) y cuenta cuántos puntos tiene el gráfico.",
  extend="Explica con tus palabras por qué dos grupos necesitan los mismos ejes para compararse.")

# ================================================================ OA 13 · clase 2
L(OA13, 2,
  use="Aprenderé a comparar dos nubes de puntos de colores: su posición, su dirección y qué tan juntos o dispersos están sus puntos, sin afirmar más de lo que muestran.",
  prior=["Sé construir un gráfico xy con dos grupos.", "Sé describir la asociación positiva, negativa o nula de una nube."],
  explain=[
      "Para comparar dos poblaciones en un gráfico xy se miran tres cosas. La posición: si una nube está más arriba o más a la derecha que la otra. La dirección: si cada nube sube, baja o no tiene tendencia. La dispersión: si los puntos de cada grupo están pegados a una línea imaginaria o repartidos.",
      "Una buena comparación usa el mismo valor de x para los dos grupos. Si con x = 12 un grupo tiene y = 18 y el otro y = 24, la diferencia es 6, y se puede decir que el segundo grupo tiene valores mayores en ese x. Comparar un punto de un grupo con otro punto de un valor de x distinto no sirve.",
      "Las nubes pueden superponerse. Cuando dos nubes se mezclan, no se puede decir que un grupo siempre supera al otro. Lo correcto es decir «tiende a» y apoyarse en varios puntos. Y recuerda: ver que un grupo está más arriba describe a la muestra, pero no explica por qué ocurre.",
  ],
  vocab=[("posición", "lugar del gráfico donde se concentra la nube"), ("dirección", "si los puntos de la nube suben, bajan o no siguen un camino"), ("dispersión", "qué tan separados están los puntos entre sí o de una línea"), ("superposición", "mezcla de los puntos de las dos nubes")],
  worked=[
      ("Comparar dos nubes", f"Datos de ejemplo (horas de práctica, errores en una prueba). Curso A (rojo): {pts(CURSO_A)}. Curso B (azul): {pts(CURSO_B)}. Compara las dos nubes.",
       ["Dirección: en ambos cursos los errores bajan al aumentar las horas de práctica; las dos asociaciones son negativas.", "Posición: con 1 hora, A tiene 9 errores y B tiene 6; con 5 horas, A tiene 4 y B tiene 2. La nube A está más arriba.", "Conclusión: en esta muestra, a igual práctica el curso A tiende a cometer más errores."], "Ambas nubes bajan; la del curso A queda más arriba"),
      ("Diferencia con el mismo x", "En el mismo gráfico, ¿cuántos errores más tiene el curso A que el curso B con 1 hora de práctica?",
       ["Con x = 1, A tiene 9 errores y B tiene 6.", "La diferencia es 9 − 6 = 3."], "3 errores más"),
  ],
  mist=[
      ("Comparar un punto de un grupo con un punto de otro grupo con distinto x.", "Los dos puntos no corresponden a la misma condición, así que la diferencia no dice nada.", "Compara siempre valores de y con el mismo valor de x."),
      ("Decir que un grupo es siempre mayor porque su nube está más arriba.", "Si las nubes se superponen, hay casos en que ocurre lo contrario.", "Habla de tendencia y revisa si las nubes se mezclan."),
  ],
  R=[ex(f"Modelo 1 de celular (meses de uso, horas de batería): {pts(M1)}. ¿Qué dirección tiene su nube? Responde positiva o negativa.", "Negativa", "Al aumentar los meses de uso, las horas de batería bajan."),
     ex(f"Modelo 1: {pts(M1)}. Modelo 2: {pts(M2)}. ¿Cuál de las dos nubes queda más arriba en el gráfico?", "La del modelo 2", "Con los mismos meses, el modelo 2 tiene más horas de batería."),
     arith("A los 12 meses de uso, el modelo 1 tiene 18 horas de batería y el modelo 2 tiene 24 horas. ¿Cuántas horas más tiene el modelo 2?", "24-18", "Se restan los valores y con el mismo valor x.", " horas")],
  C=[ex(f"Modelo 1: {pts(M1)}. Modelo 2: {pts(M2)}. ¿Las dos nubes tienen la misma dirección? Responde sí o no.", "Sí", "En ambos modelos la batería baja al pasar de 6 a 30 meses."),
     arith("A los 30 meses de uso, el modelo 1 tiene 10 horas de batería y el modelo 2 tiene 16 horas. ¿Cuántas horas más tiene el modelo 2?", "16-10", "Se restan los valores y con x = 30.", " horas"),
     ex("¿Cuál es una comparación correcta de las nubes? A) A igual tiempo de uso, el modelo 2 tiende a tener más horas de batería. B) El modelo 2 siempre dura más en cualquier celular del mundo. C) El modelo 1 es mejor porque su nube queda más abajo.", "A", "La conclusión se limita a la muestra y compara con el mismo valor de x.")],
  A=[ex("Nube P: (1, 2), (2, 4), (3, 6), (4, 8), (5, 10). Nube Q: (1, 5), (2, 3), (3, 9), (4, 4), (5, 8). ¿Cuál nube está más dispersa? Responde P o Q.", "Q", "Los puntos de P están sobre una línea; los de Q se reparten sin seguir una línea."),
     arith(f"Se comparan los puntos de M1 y M2 con los mismos meses de uso. M1 tiene 20, 18, 15, 13 y 10 horas; M2 tiene 26, 24, 20, 19 y 16. ¿Cuántas horas de diferencia hay en total sumando las cinco comparaciones?", "(26+24+20+19+16)-(20+18+15+13+10)", "Se resta cada par con igual x; equivale a restar los totales, 105 y 76.", " horas"),
     ex(f"Modelo 2: {pts(M2)}. ¿Cuántos de sus puntos tienen más de 20 horas de batería?", "2", "Superan 20 horas los puntos con 26 y 24 horas.")],
  Z=[ex("Las nubes de dos grupos están tan mezcladas que muchos puntos de un grupo quedan entre los del otro. ¿Se puede decir que un grupo siempre supera al otro? Responde sí o no.", "No", "Si las nubes se superponen, hay casos que contradicen la afirmación."),
     ex("Pedro compara el punto (6, 20) del modelo 1 con el punto (30, 16) del modelo 2 y dice que el modelo 2 dura menos. ¿Es una buena comparación? Responde sí o no.", "No", "Los dos puntos tienen meses de uso distintos, así que no se comparan en igualdad de condiciones.")],
  D=[ex(f"Modelo 1: {pts(M1)}. Modelo 2: {pts(M2)}. Un modelo 3 tiene 18 horas de batería a los 18 meses de uso. ¿Entre cuáles dos nubes queda ese punto? A) Entre la del modelo 1 y la del modelo 2. B) Por debajo de las dos. C) Por encima de las dos.", "A", "A los 18 meses el modelo 1 tiene 15 horas y el modelo 2 tiene 20; 18 queda entre ambas."),
     arith("A los 6 meses el modelo 1 tiene 20 horas de batería y a los 30 meses tiene 10. ¿Qué porcentaje de la batería que tenía a los 6 meses le queda a los 30 meses?", "10*100//20", "Se divide lo que queda, 10, por lo que tenía a los 6 meses, 20, y se multiplica por 100.", "%")],
  ctx=[ex("Dos rutas de buses escolares registraron (distancia en km, minutos del viaje). Ruta 1: (4, 12), (8, 20), (12, 32). Ruta 2: (4, 10), (8, 15), (12, 21). A 8 km, ¿cuántos minutos más tarda la ruta 1 que la ruta 2?", "5", "20 − 15 = 5 minutos más con el mismo valor x.")],
  chk=[ex("Nombra una de las tres cosas que se miran al comparar dos nubes de puntos.", "Posición, dirección o dispersión", "Esas tres características describen cómo se ven y se comparan las nubes."),
       ex("Para comparar dos grupos, ¿se usa el mismo valor de x? Responde sí o no.", "Sí", "Así se comparan en igualdad de condiciones."),
       arith("El grupo rojo tiene 15 en x = 10 y el azul tiene 9 en x = 10. ¿Cuál es la diferencia?", "15-9", "Se restan los valores y con el mismo x.")],
  op=(f"Compara estos dos grupos de ejemplo (kilómetros recorridos en bicicleta en el mes, minutos que tarda una vuelta al parque). Grupo F: (20, 12), (40, 11), (60, 9), (80, 8). Grupo G: (20, 15), (40, 13), (60, 12), (80, 10). Dibuja los dos grupos con símbolos distintos y escribe frases breves que digan la dirección de cada nube, cuál queda más arriba y cuánto vale la diferencia en y cuando x = 60, y una conclusión con «tiende a».",
      "Ambas nubes bajan (asociación negativa). El grupo G queda más arriba. Con x = 60, G tiene 12 minutos y F tiene 9: la diferencia es 3 minutos. En esta muestra, a igual cantidad de kilómetros, G tiende a tardar más.",
      ["gráfico con los dos grupos y leyenda", "dirección de cada nube", "comparación con el mismo x", "diferencia correcta", "usa «tiende a»"],
      ["gráfico dibujado", "frases pedidas", "diferencia calculada"],
      ["comparar puntos con distinto x", "decir que G siempre tarda más", "no indicar la dirección"],
      "Pide que señale en el gráfico los dos puntos con x = 60. Reconoce que use «tiende a» y limite la conclusión a la muestra."),
  reinforce="Curso A (horas de práctica, errores): (1, 9), (2, 7), (3, 6), (5, 4), (6, 2). Curso B: (1, 6), (2, 5), (4, 3), (5, 2), (7, 1). Calcula la diferencia de errores entre A y B cuando x = 5.",
  extend="Describe dos grupos de datos reales de tu entorno que cruzarías en un gráfico xy y qué compararías.")

# ================================================================ OA 13 · clase 3
L(OA13, 3,
  use="Aprenderé a separar dos nubes de puntos de colores con una recta trazada de forma intuitiva, a contar cuántos puntos quedan mal ubicados y a elegir la mejor recta.",
  prior=["Sé ubicar puntos en un gráfico xy.", "Sé evaluar una expresión como y = x + 2 para un valor de x."],
  explain=[
      "A veces dos grupos se ven en lugares distintos del gráfico, y se puede trazar una recta que deje, en lo posible, los puntos de un color a un lado y los del otro color al otro lado. Esa recta se llama recta separadora. Se traza de forma intuitiva: se mira la franja vacía entre las dos nubes y se apoya la regla en ella.",
      "Para saber en qué lado queda un punto respecto de una recta, como y = x + 2, calcula el valor de la recta con la x del punto. Si el y del punto es mayor, el punto queda arriba; si es menor, abajo; si es igual, está sobre la recta. Por ejemplo, el punto (3, 4) y la recta y = x + 2: la recta vale 5 en x = 3 y como 4 es menor que 5, el punto queda abajo.",
      "Una recta no siempre separa perfecto. Los puntos del lado equivocado, o sobre la recta, son los mal clasificados. Entre dos rectas, es mejor la que deja menos puntos mal clasificados. Y puede no existir ninguna que separe perfecto, cuando un grupo rodea al otro.",
  ],
  vocab=[("recta separadora", "recta que deja los puntos de un grupo a un lado y los del otro grupo al otro lado"), ("mal clasificado", "punto que queda del lado de la recta donde debería estar el otro grupo, o sobre la recta"), ("intuitivo", "hecho a ojo, mirando el gráfico, sin una fórmula única"), ("sobre la recta", "punto cuyo y es igual al valor de la recta en su x")],
  worked=[
      ("Una recta que separa", f"Datos de ejemplo. Grupo rojo: {pts(ROJOS_T)}. Grupo azul: {pts(AZULES_T)}. ¿Separa a los dos grupos la recta y = x?",
       ["Rojos: en cada uno el y es mayor que su x (8 > 2, 9 > 3, 7 > 4, 10 > 5, 9 > 6, 6 > 3), así que quedan todos arriba.", "Azules: en cada uno el y es menor que su x (3 < 6, 4 < 7, 2 < 8, 5 < 9, 3 < 10, 1 < 7), así que quedan todos abajo.", "Los 12 puntos están bien clasificados."], "Sí, separa perfecto: 12 de 12 puntos bien clasificados"),
      ("Contar los mal clasificados", "Con los mismos datos, ¿qué ocurre con la recta y = 5?",
       ["Rojos: todos tienen y mayor o igual que 6, así que quedan arriba.", "Azules: (6, 3), (7, 4), (8, 2), (10, 3) y (7, 1) tienen y menor que 5, y (9, 5) tiene y igual a 5, por lo que queda sobre la recta.", "El punto sobre la recta no queda clasificado."], "11 de 12 bien clasificados; 1 punto está sobre la recta"),
  ],
  mist=[
      ("Dar por buena una recta sin revisar los puntos que quedan cerca de ella.", "Un solo punto del lado equivocado ya cambia la calidad de la separación.", "Revisa cada punto calculando el valor de la recta en su x."),
      ("Pensar que siempre hay una recta que separa perfecto.", "Si un grupo rodea al otro, ninguna recta los separa sin errores.", "Cuenta los mal clasificados y elige la recta con menos errores."),
  ],
  R=[ex("¿Qué hace una recta separadora de dos nubes de puntos de colores?", "Deja los puntos de un grupo a un lado y los del otro grupo al otro lado", "Separa los dos grupos, en lo posible, sin dejar puntos en el lado equivocado."),
     ex("Un punto (4, 9) y la recta y = 5. ¿El punto queda arriba o abajo de la recta?", "Arriba", "Su y vale 9 y la recta vale 5; como 9 es mayor que 5, queda arriba."),
     ex("Un punto (3, 2) y la recta y = x. ¿El punto queda arriba o abajo de la recta?", "Abajo", "La recta vale 3 en x = 3 y como 2 es menor que 3, queda abajo.")],
  C=[ex("¿De qué lado queda el punto (2, 6) respecto de la recta y = x? A) Arriba. B) Abajo. C) Sobre la recta.", "A", "La recta vale 2 en x = 2 y 6 es mayor que 2."),
     ex("¿De qué lado queda el punto (5, 7) respecto de la recta y = x + 2? A) Arriba. B) Abajo. C) Sobre la recta.", "C", "La recta vale 5 + 2 = 7 en x = 5, igual que el y del punto."),
     arith(f"Grupo rojo: {pts(ROJOS_Q)}. Grupo azul: {pts(AZULES_Q)}. ¿Cuántos puntos rojos quedan arriba de la recta y = x + 3?", f"{lado(ROJOS_Q, 1, 3, 'arriba')}", "Se compara el y de cada punto rojo con x + 3: 7 > 4, 8 > 5, 6 = 6 (sobre la recta), 9 > 7 y 10 > 5.", " puntos")],
  A=[arith(f"Grupo rojo: {pts(ROJOS_Q)}. Grupo azul: {pts(AZULES_Q)}. Con la recta y = 8, ¿cuántos puntos quedan bien clasificados? Considera rojos arriba y azules abajo.", f"{aciertos(ROJOS_Q, AZULES_Q, 0, 8)}", "Rojos arriba: (4, 9) y (2, 10); azules debajo de 8: los cinco.", " puntos"),
     arith(f"Con los mismos grupos (rojos: {pts(ROJOS_Q)}; azules: {pts(AZULES_Q)}) y la recta y = x + 3, ¿cuántos puntos quedan bien clasificados? Considera rojos arriba y azules abajo.", f"{aciertos(ROJOS_Q, AZULES_Q, 1, 3)}", "Un rojo, el (3, 6), queda sobre la recta y por eso no cuenta; los otros nueve sí.", " puntos"),
     ex(f"Grupo rojo: {pts(ROJOS_Q)}. Grupo azul: {pts(AZULES_Q)}. ¿Cuál recta separa mejor? A) y = 8. B) y = x + 3. C) Las dos separan igual.", "B", "La recta y = x + 3 deja nueve puntos bien clasificados y la recta y = 8 solo siete.")],
  Z=[ex("Un grupo rojo tiene los puntos (1, 1), (5, 5), (1, 5) y (5, 1), y un grupo azul tiene el punto (3, 3), en el centro. ¿Existe una recta que deje los rojos de un lado y el azul del otro? Responde sí o no.", "No", "El punto azul está rodeado por los rojos y cualquier recta que lo deje solo deja rojos de su lado."),
     ex("Una recta deja 2 puntos mal clasificados y otra recta deja 5 puntos mal clasificados en los mismos datos. ¿Cuál separa mejor? Responde la primera o la segunda.", "La primera", "Es mejor la recta con menos puntos mal clasificados.")],
  D=[ex("Se separaron dos grupos con la recta y = x: los puntos rojos quedaron arriba y los azules abajo. Aparece un punto nuevo (6, 2) que no se sabe de qué grupo es. Con esa recta, ¿a qué color se parece? Responde rojo o azul.", "Azul", "En x = 6 la recta vale 6 y el punto tiene y = 2, que está abajo, donde están los azules."),
     ex("Un grupo rojo tiene valores y de al menos 7 y un grupo azul tiene valores y de a lo sumo 4. ¿Qué rectas horizontales y = k, con k entero, separan perfecto a los dos grupos sin tener puntos sobre la recta? A) k = 5 o k = 6. B) k = 4 o k = 7. C) k = 3 o k = 8.", "A", "k debe ser mayor que 4 y menor que 7, así que solo 5 y 6.")],
  ctx=[ex("Se pesan y miden semillas de dos tipos de ejemplo: tipo R (rojo) y tipo A (azul). Con la recta y = x + 1, los puntos (2, 5), (3, 6) y (4, 7) de R quedan arriba, y los puntos (5, 3), (6, 4) y (7, 5) de A quedan abajo. Una semilla nueva mide (4, 2): ¿a qué tipo se parece más? Responde R o A.", "A", "En x = 4 la recta vale 5 y el punto tiene y = 2, así que queda abajo, donde están las semillas A.")],
  chk=[ex("Un punto está sobre una recta. ¿Cuánto vale la diferencia entre su y y el valor de la recta en su x?", "0", "Si el punto está sobre la recta, su y es igual al valor de la recta."),
       ex("Para elegir entre dos rectas separadoras, ¿qué se cuenta?", "Los puntos mal clasificados", "Es mejor la recta que deja menos puntos mal clasificados."),
       ex("Un punto (6, 4) y la recta y = x − 1. ¿El punto queda arriba, abajo o sobre la recta?", "Abajo", "La recta vale 5 en x = 6 y como 4 es menor que 5, queda abajo.")],
  op=("Dibuja los siguientes puntos de ejemplo en una hoja cuadriculada. Rojos: (1, 7), (2, 8), (3, 6), (4, 9), (2, 10). Azules: (5, 2), (6, 4), (7, 3), (8, 1), (9, 4). Traza con regla una recta que separe los dos grupos, escribe dos puntos por los que pasa y cuenta cuántos puntos quedan mal clasificados. Después traza una segunda recta distinta y decide cuál es mejor.",
      "La recta y = 5 deja los cinco rojos arriba (todos tienen y de 6 o más) y los cinco azules abajo (todos tienen y de 4 o menos): 0 mal clasificados. Pasa por (0, 5) y (10, 5). La recta y = 8 deja 3 rojos mal clasificados, así que es peor.",
      ["dibuja los diez puntos", "traza una recta con regla", "indica dos puntos de la recta", "cuenta los mal clasificados", "compara dos rectas"],
      ["gráfico con dos rectas", "conteo de errores de cada recta", "decisión justificada"],
      ["contar un punto sobre la recta como bien clasificado", "trazar la recta sin la regla", "no comparar con una segunda recta"],
      "Pide que explique cómo comprobó que ningún punto cruza la recta. Reconoce que compare dos rectas con el conteo de errores."),
  reinforce="Con los datos del ejemplo resuelto, verifica que el punto rojo (3, 6) queda arriba de la recta y = x y calcula el valor de la recta en x = 3.",
  extend="Explica qué pasaría con la recta separadora si aparece un punto azul en medio de los rojos.")

# ================================================================ OA 13 · clase 4
L(OA13, 4,
  use="Aprenderé a evaluar qué tan buena es una recta separadora con el porcentaje de aciertos, a usarla para clasificar un elemento nuevo y a decir qué no se puede concluir.",
  prior=["Sé trazar y evaluar una recta separadora.", "Sé calcular porcentajes de una cantidad."],
  explain=[
      "Una recta separadora se evalúa con su porcentaje de aciertos: los puntos bien clasificados divididos por el total de puntos, por 100. Si de 20 puntos la recta clasifica bien 19, el porcentaje es 95 %. Un puntaje alto no garantiza que funcione siempre: solo describe cómo funciona con la muestra que tienes.",
      "Con la recta se puede clasificar un elemento nuevo: se ve de qué lado queda su punto y se predice su grupo. Esa predicción puede fallar, sobre todo cerca de la recta o donde las nubes se mezclan. Por eso se dice «probablemente» y no «seguro». Y si el elemento tiene valores fuera del rango de la muestra, la predicción es todavía menos confiable.",
      "Una recta separadora no explica por qué los grupos son distintos: describe dónde se ubican. Dos rectas distintas pueden tener un porcentaje parecido, así que la recta intuitiva no es única. Una buena conclusión dice la recta usada, el porcentaje de aciertos, y la limitación: muestra pequeña, nubes que se superponen o puntos atípicos.",
  ],
  vocab=[("porcentaje de aciertos", "puntos bien clasificados dividido por el total, por 100"), ("clasificar", "decidir a qué grupo pertenece un elemento nuevo"), ("predicción", "decisión sobre un caso nuevo, que puede fallar"), ("limitación", "aspecto que impide extender la conclusión más allá de la muestra")],
  worked=[
      ("Porcentaje de aciertos", f"Datos de ejemplo. Rojos: {pts(W_ROJOS)}. Azules: {pts(W_AZULES)}. Se usa la recta y = x (rojos arriba, azules abajo). ¿Cuál es su porcentaje de aciertos?",
       ["Rojos arriba de y = x: 9 de 10; el punto (7, 6) queda abajo.", "Azules abajo de y = x: los 10.", "Aciertos: 9 + 10 = 19 de 20, o sea 19 ÷ 20 × 100 = 95 %."], "95 % de aciertos"),
      ("Clasificar un caso nuevo", "Con la misma recta y = x, aparece un elemento nuevo en (4, 6). ¿A qué grupo se parece y qué cuidado hay que tener?",
       ["La recta vale 4 en x = 4 y el y del punto es 6: queda arriba.", "Arriba están los rojos, pero la recta falló en 1 de 20 casos."], "Se parece a los rojos; es una predicción, no una certeza"),
  ],
  mist=[
      ("Decir «esta recta acierta siempre» por tener 100 % en la muestra.", "El 100 % describe solo los puntos medidos, no los casos nuevos.", "Escribe «en esta muestra» y comenta cuántos errores aparecen cerca de la recta."),
      ("Concluir que la altura (o el valor de x) causa que un elemento sea de un grupo.", "La recta describe la ubicación de los puntos, no explica por qué pertenecen al grupo.", "Habla de asociación y de ubicación, no de causa."),
  ],
  R=[ex("Para calcular el porcentaje de aciertos de una recta separadora, ¿qué se divide por el total de puntos?", "Los puntos bien clasificados", "Los aciertos son los puntos que quedaron del lado correcto."),
     arith("Una recta clasifica bien 18 de 20 puntos. ¿Cuántos puntos quedaron mal clasificados?", "20-18", "Se restan los bien clasificados del total.", " puntos"),
     ex("Un punto nuevo queda arriba de una recta que dejó a los rojos arriba. ¿A qué grupo se parece más? Responde rojo o azul.", "Rojo", "Se parece al grupo que queda de ese lado de la recta.")],
  C=[arith(f"Rojos: {pts(W_ROJOS)}. Azules: {pts(W_AZULES)}. Con la recta y = 5, 8 rojos quedan arriba y 7 azules quedan abajo. ¿Cuántos puntos quedan mal clasificados? (Incluye los que están sobre la recta.)", "20-8-7", "Hay 20 puntos y 8 + 7 = 15 están bien clasificados; los otros 5 quedan mal o sobre la recta.", " puntos"),
     arith("Una recta clasifica bien 15 de 20 puntos. ¿Qué porcentaje de aciertos tiene?", "15*100//20", "Se divide 15 por 20 y se multiplica por 100.", "%"),
     ex("Una recta tiene 100 % de aciertos en una muestra de 6 puntos. ¿Qué se puede afirmar? A) Que acertará siempre con elementos nuevos. B) Que en esa muestra no se equivoca, pero con 6 puntos la conclusión es débil. C) Que el valor de x causa el grupo.", "B", "El resultado describe solo la muestra y 6 puntos son pocos para generalizar.")],
  A=[arith(f"Con los mismos datos (rojos: {pts(W_ROJOS)}; azules: {pts(W_AZULES)}) y la recta y = x + 2, 6 rojos quedan arriba y los 10 azules quedan abajo. ¿Cuál es el porcentaje de aciertos?", "(6+10)*100//20", "Los aciertos son 6 + 10 = 16 de 20.", "%"),
     ex("La recta P clasifica bien 17 de 20 puntos de una muestra. La recta Q clasifica bien 24 de 30 puntos de otra muestra. ¿Cuál tiene mayor porcentaje de aciertos? A) La recta P. B) La recta Q. C) Tienen el mismo porcentaje.", "A", "P tiene 17 ÷ 20 = 85 % y Q tiene 24 ÷ 30 = 80 %; Q acierta más puntos, pero sobre más puntos."),
     ex("Un elemento nuevo queda justo sobre la recta que separa dos grupos. ¿Se puede predecir su grupo con seguridad? Responde sí o no.", "No", "Sobre la recta no queda de ningún lado, así que la predicción es incierta.")],
  Z=[ex("Dos rectas distintas tienen 90 % de aciertos en la misma muestra. ¿Puede haber más de una recta razonable? Responde sí o no.", "Sí", "La recta trazada de forma intuitiva no es única."),
     ex("Una recta separa muy bien las nubes de dos tipos de semilla de ejemplo según su peso y su largo. Alguien dice que el peso causa que una semilla sea del tipo R. ¿Es una conclusión correcta? Responde sí o no.", "No", "La recta describe dónde están los puntos, pero no demuestra una causa.")],
  D=[arith("Una recta clasifica bien 28 de 40 puntos. ¿Cuántos puntos más deberían acertarse para llegar a un 90 % de aciertos?", "40*90//100-28", "El 90 % de 40 es 36 y ya hay 28 aciertos.", " puntos"),
     ex("Un elemento nuevo tiene un valor de x que está muy por encima del mayor x de la muestra. ¿La predicción con la recta es más confiable, igual o menos confiable que dentro del rango?", "Menos confiable", "Fuera del rango de la muestra no se sabe si las nubes siguen igual.")],
  ctx=[ex("Un club de ejemplo compara (horas de entrenamiento a la semana, tiempo de una carrera en minutos) de sus corredores de 5 km (rojo) y de 10 km (azul). Una recta deja bien clasificados a 16 de 20 corredores. ¿Cuál es su porcentaje de aciertos?", "80%", "16 ÷ 20 × 100 = 80 %.")],
  chk=[ex("¿Qué dato se necesita, además de los bien clasificados, para calcular el porcentaje de aciertos?", "El total de puntos", "El porcentaje se calcula dividiendo los aciertos por el total."),
       arith("Una recta clasifica bien 9 de 10 puntos. ¿Qué porcentaje de aciertos tiene?", "9*100//10", "Se divide 9 por 10 y se multiplica por 100.", "%"),
       ex("Un elemento nuevo queda del lado de los azules de la recta. ¿Es una certeza o una predicción?", "Una predicción", "Un caso nuevo puede estar mal clasificado.")],
  op=("Usa estos puntos de ejemplo: rojos (1, 7), (2, 8), (3, 6), (4, 9), (2, 10); azules (5, 2), (6, 4), (7, 3), (8, 1), (9, 4). Elige una recta separadora, calcula su porcentaje de aciertos y clasifica un elemento nuevo en (4, 5). Escribe una frase de conclusión que incluya una limitación.",
      "La recta y = 5 clasifica bien 10 de 10 puntos (100 %). El elemento (4, 5) queda justo sobre la recta, así que no se puede predecir con seguridad. Conclusión: en esta muestra de solo 10 puntos la recta separa perfecto, pero el caso nuevo queda sobre la recta y la muestra es pequeña.",
      ["elige y escribe la recta", "calcula el porcentaje de aciertos", "clasifica el elemento nuevo", "usa «en esta muestra»", "nombra una limitación"],
      ["recta elegida", "porcentaje calculado", "frase de conclusión con limitación"],
      ["decir «acierta siempre»", "clasificar el caso sobre la recta sin advertir la duda", "no nombrar ninguna limitación"],
      "Pide que explique por qué el caso nuevo es dudoso. Reconoce que la conclusión nombre su limitación."),
  reinforce="Con los datos del ejemplo resuelto, calcula el porcentaje de aciertos si la recta clasificara bien 17 de 20 puntos.",
  extend="Explica por qué una recta con 100 % de aciertos en 6 puntos es menos convincente que una con 95 % en 200 puntos.")
