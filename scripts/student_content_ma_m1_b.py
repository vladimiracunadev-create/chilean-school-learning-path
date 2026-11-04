"""Cuaderno del estudiante de 1.º medio Matemática, OA 12 (distribuciones bivariadas y nubes de puntos): clases 1 a 4."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA12 = "MA1M OA 12"

MAT = "Cuaderno cuadriculado, lápiz, regla y, si quieres, una calculadora. Todos los datos que necesitas están escritos en cada ejercicio."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def L(oa, n, use, prior, explain, vocab, worked, mist, R, C, A, Z, D, ctx, chk, op, reinforce, extend, mat=MAT):
    """Registra una clase con forma compacta (misma estructura que register)."""
    register(
        oa, n,
        materials=mat, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mist],
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=chk, open_task=task(*op), reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 12 · clase 1
L(OA12, 1,
  use="Aprenderé a organizar en una tabla de doble entrada dos características de las mismas personas o cosas, a leer sus celdas y totales y a comparar grupos con porcentajes.",
  prior=["Sé leer tablas de frecuencias de una sola característica.", "Sé calcular porcentajes sencillos de una cantidad."],
  explain=[
      "Una población es el grupo que se estudia, por ejemplo los 40 estudiantes de un nivel. De cada integrante puedes anotar dos características distintas, como su curso y cómo llega al colegio. Una tabla de doble entrada pone una característica en las filas y la otra en las columnas. Cada celda cuenta cuántos integrantes tienen las dos a la vez.",
      "Al final de cada fila y de cada columna se escriben los totales, que se llaman totales marginales. La suma de los totales de las filas debe ser igual a la suma de los totales de las columnas, y ambas dan el total de la población. Si no coinciden, hay un error de conteo. Ninguna celda puede ser mayor que el total de su fila ni que el total de su columna.",
      "Para comparar grupos de distinto tamaño no basta mirar cuántos hay: conviene usar el porcentaje dentro de cada fila. Se calcula dividiendo el valor de la celda por el total de su fila y multiplicando por 100. Así se compara cada grupo con su propio tamaño y no se confunde «más cantidad» con «más proporción».",
  ],
  vocab=[("población", "grupo completo de personas o cosas que se estudia"), ("característica", "dato que se anota de cada integrante, como el curso o el medio de transporte"), ("tabla de doble entrada", "tabla que cruza dos características, una en filas y otra en columnas"), ("total marginal", "total que se escribe al final de una fila o de una columna")],
  worked=[
      ("Leer una tabla de doble entrada", "Se anotó el curso y el medio de transporte de 40 estudiantes (datos de ejemplo). En 1.º A: 12 van en bus, 5 en bicicleta y 3 a pie. En 1.º B: 9 en bus, 4 en bicicleta y 7 a pie. ¿Cuántos estudiantes van en bus en total?",
       ["Se ordena la tabla: fila 1.º A con 12, 5 y 3 (total 20); fila 1.º B con 9, 4 y 7 (total 20).", "La columna «bus» tiene 12 y 9.", "Su total marginal es 12 + 9 = 21. Control: las filas suman 20 + 20 = 40 y las columnas 21 + 9 + 10 = 40."], "21 estudiantes van en bus"),
      ("Comparar con porcentajes", "Con la misma población, ¿qué porcentaje de 1.º B va en bus?",
       ["El total de la fila 1.º B es 20 y en bus van 9.", "Se calcula 9 ÷ 20 = 0,45, que es 45 de cada 100.", "El porcentaje es 45 %."], "45 % de 1.º B va en bus"),
  ],
  mist=[
      ("Leer la celda de la fila equivocada: decir que 12 estudiantes de 1.º B van en bus.", "Cada celda pertenece a una fila y a una columna a la vez; hay que mirar ambas.", "Marca con un dedo la fila y con otro la columna y lee donde se cruzan."),
      ("Decir que un grupo es más grande porque su celda es mayor, sin mirar el tamaño de cada grupo.", "Si los grupos tienen tamaños distintos, la comparación justa es con porcentajes.", "Divide cada celda por el total de su fila antes de comparar."),
  ],
  R=[ex("Una tabla cruza vivienda (casa o departamento) con mascota (perro, gato o ninguna), de 50 personas de un pasaje (datos de ejemplo). En casa: 14 perro, 6 gato, 5 ninguna. En departamento: 4 perro, 9 gato, 12 ninguna. ¿Cuántas personas viven en departamento y tienen gato?", "9", "La celda donde se cruzan la fila departamento y la columna gato dice 9."),
     arith("En la misma tabla de vivienda y mascota, en casa hay 14 con perro, 6 con gato y 5 sin mascota. ¿Cuántas personas viven en casa?", "14+6+5", "El total de una fila suma todas sus celdas.", " personas"),
     arith("En esa tabla, en departamento hay 4 con perro y en casa hay 14 con perro. ¿Cuántas personas tienen perro en total?", "14+4", "El total de la columna perro suma las celdas de las dos filas.", " personas")],
  C=[ex("En la tabla de vivienda y mascota, la celda departamento-ninguna vale 12. ¿Qué significa? A) Hay 12 departamentos en el pasaje. B) Hay 12 personas que viven en departamento y no tienen mascota. C) Hay 12 personas sin mascota en todo el pasaje.", "B", "La celda cuenta a quienes cumplen las dos características a la vez; las 12 de la celda son solo las de departamento."),
     ex("Una tabla tiene totales de fila 25 y 25 y totales de columna 18, 15 y 16. ¿Está bien hecha? Responde sí o no.", "No", "Las filas suman 50 y las columnas 18 + 15 + 16 = 49, así que no coinciden."),
     arith("En el pasaje, 5 personas de casa y 12 de departamento no tienen mascota. ¿Cuántas personas no tienen mascota?", "5+12", "Se suman las dos celdas de la columna «ninguna».", " personas")],
  A=[arith("De 60 estudiantes se anotó la jornada y si usan transporte escolar. Mañana con transporte: 18; mañana sin transporte: 12; tarde con transporte: 10. ¿Cuántos van en la tarde sin transporte?", "60-18-12-10", "El total es 60, así que a lo que hay se le resta lo ya contado.", " estudiantes"),
     arith("En el pasaje, 9 de las 25 personas que viven en departamento tienen gato. ¿Qué porcentaje es?", "9*100//25", "Se divide la celda por el total de su fila y se multiplica por 100; también sirve 9 × 4, porque 25 × 4 = 100.", "%"),
     ex("En 3.º A, 12 de 30 estudiantes llegan en bus. En 3.º C, 10 de 20 llegan en bus. ¿Qué curso tiene mayor porcentaje de estudiantes que llegan en bus?", "3.º C", "12 de 30 es 40 % y 10 de 20 es 50 %; aunque 3.º A tenga más estudiantes en bus, su proporción es menor.")],
  Z=[ex("Rocío dice: «En 2.º C van 15 en bus y en 2.º D van 12, así que el bus es más común en 2.º C». Los cursos tienen 25 y 16 estudiantes. ¿Tiene razón? Responde sí o no.", "No", "Los cursos tienen distinto tamaño; en proporción, 15 de 25 (60 %) es menos que 12 de 16 (75 %)."),
     ex("En una tabla, las dos filas suman 25 cada una. Una celda de la fila de departamentos dice 30. ¿Puede estar bien? Responde sí o no.", "No", "Una celda no puede superar el total de su fila, que es 25.")],
  D=[arith("Se preguntó a 80 personas si prefieren té o café. Menores de 30 años: 20 té y 15 café. Mayores de 30 años: son 45 en total. En la columna de café hay 45 personas en total. ¿Cuántos mayores de 30 años prefieren café?", "45-15", "En la columna café hay 45 y 15 son menores de 30, así que los otros 30 son mayores de 30.", " personas"),
     arith("Se supo que el 40 % de 50 estudiantes de 2.º A y el 60 % de 30 estudiantes de 2.º B van a pie. ¿Cuántos estudiantes de esos dos cursos van a pie en total?", "50*40//100+30*60//100", "Primero se calcula la parte de cada curso (20 y 18) y luego se suman.", " estudiantes")],
  ctx=[ex("Un kiosco anotó 30 ventas de ejemplo. En el recreo de la mañana: 9 bebidas y 6 snacks. En el de la tarde: 4 bebidas y 11 snacks. ¿Cuántos snacks se vendieron en total?", "17", "Se suman las dos celdas de la columna snack: 6 + 11.")],
  chk=[ex("En estadística: ¿qué significa que una tabla sea «de doble entrada»?", "Cruza dos características: una en las filas y otra en las columnas", "Cada celda cuenta los casos que tienen una característica de la fila y una de la columna."),
       arith("Una tabla tiene filas con totales 14 y 11. ¿Cuál es el total de la población?", "14+11", "El total de la población es la suma de los totales de las filas.", " personas"),
       arith("En un curso, 6 de 24 estudiantes tienen lentes. ¿Qué porcentaje es?", "6*100//24", "Se divide 6 por 24 y se multiplica por 100.", "%")],
  op=("Estas son las respuestas de 12 estudiantes (datos de ejemplo), escritas como curso y deporte: A-fútbol, A-vóleibol, A-fútbol, B-vóleibol, B-fútbol, A-natación, B-natación, B-vóleibol, A-fútbol, B-fútbol, A-vóleibol, B-natación. Arma una tabla de doble entrada con los cursos A y B en las filas y los tres deportes en las columnas, escribe los totales marginales y comprueba que ambas sumas den 12. Después escribe qué porcentaje del curso A eligió fútbol.",
      "Curso A: fútbol 3, vóleibol 2, natación 1 (total 6). Curso B: fútbol 2, vóleibol 2, natación 2 (total 6). Totales de columna: 5, 4 y 3; total 12. En el curso A, 3 de 6 eligen fútbol: 50 %.",
      ["cuenta cada par una sola vez", "ubica los conteos en la celda correcta", "escribe los totales de filas y columnas", "comprueba que ambas sumas dan 12", "calcula el porcentaje con el total de la fila"],
      ["tabla de 2 filas y 3 columnas con totales", "comprobación de la suma", "porcentaje calculado"],
      ["contar dos veces el mismo par", "poner un conteo en la fila equivocada", "dividir por 12 en vez de por el total del curso A"],
      "Pide que muestre dónde se cruzan la fila A y la columna fútbol. Reconoce que haya comprobado la suma de totales."),
  reinforce="Con la tabla del pasaje, calcula qué porcentaje de quienes viven en casa no tienen mascota (5 de 25).",
  extend="Escribe dos características que podrías cruzar en una tabla de doble entrada con tu curso y qué compararías con porcentajes.")

# ================================================================ OA 12 · clase 2
L(OA12, 2,
  use="Aprenderé a representar en una nube de puntos dos datos numéricos de cada persona: cómo ubicar un par, cómo leerlo y por qué los puntos no se unen.",
  prior=["Sé ubicar pares ordenados en un plano cartesiano.", "Sé elegir una escala para un eje."],
  explain=[
      "Cuando de cada integrante de una población tienes dos datos numéricos, como las horas de estudio y el puntaje de una prueba, puedes dibujar una nube de puntos. El eje horizontal muestra una característica y el eje vertical la otra. Cada integrante es un solo punto, escrito como par (x, y): primero el valor del eje horizontal y después el del vertical.",
      "Antes de dibujar hay que elegir la escala de cada eje, con la misma separación entre marcas y el nombre de la característica con su unidad. Por ejemplo, un cuadrito horizontal puede valer 1 hora y uno vertical 10 puntos. Para ubicar (4, 55) se avanza 4 hacia la derecha y se sube hasta la altura de 55.",
      "En una nube de puntos los puntos no se unen con líneas. Cada punto es una persona distinta, y no hay un orden ni un paso del uno al siguiente, como sí ocurre con una temperatura medida cada hora. Dos personas pueden tener el mismo valor en un eje: sus puntos quedan alineados en una misma línea, y eso es normal.",
  ],
  vocab=[("nube de puntos", "gráfico en que cada integrante se marca con un punto según dos datos numéricos"), ("par ordenado", "dos números (x, y): primero el horizontal, luego el vertical"), ("escala", "valor que representa cada marca o cuadrito de un eje"), ("eje", "recta numerada, horizontal o vertical, donde se mide una característica")],
  worked=[
      ("Ubicar un punto", "Una estudiante de ejemplo estudió 4 horas y obtuvo 55 puntos. Con escala de 1 hora por cuadrito horizontal y 10 puntos por cuadrito vertical, ¿cómo se ubica su punto?",
       ["Se escribe el par (horas, puntos) = (4, 55).", "Se avanza 4 cuadritos a la derecha desde el origen.", "Se sube hasta la altura de 55 puntos, que queda a medio camino entre 50 y 60, y se marca un punto."], "Punto en (4, 55): 4 a la derecha y 55 hacia arriba"),
      ("Leer un punto", "En la misma nube hay un punto sobre el 7 del eje horizontal, a la altura de 75. ¿Qué dice sobre esa persona?",
       ["El valor horizontal es 7 y el vertical es 75.", "El par es (7, 75)."], "Estudió 7 horas y obtuvo 75 puntos"),
  ],
  mist=[
      ("Invertir el par: ubicar (4, 55) con 55 a la derecha y 4 hacia arriba.", "Primero va el valor horizontal y después el vertical.", "Lee el par en voz alta: «primero me muevo a lo ancho, después a lo alto»."),
      ("Unir los puntos con una línea, como si fuera una serie en el tiempo.", "Cada punto es una persona distinta y no hay un orden entre ellos.", "Deja los puntos separados y observa la forma que dibuja la nube."),
  ],
  R=[ex("Un punto de una nube se escribe (6, 30). ¿Qué número se mide en el eje horizontal?", "6", "El primer número del par es el del eje horizontal."),
     ex("Una persona estudió 3 horas y obtuvo 45 puntos. Escribe su par (horas, puntos).", "(3, 45)", "Primero va el valor horizontal, que son las horas."),
     ex("Una tabla tiene los datos de 8 estudiantes, con dos datos de cada uno. ¿Cuántos puntos tendrá la nube?", "8", "Cada estudiante es un solo punto.")],
  C=[ex("Datos de ejemplo (horas, puntos): Ana (2, 40), Beto (5, 60), Caro (5, 70), Diego (9, 90). ¿Qué dos estudiantes estudiaron la misma cantidad de horas?", "Beto y Caro", "Ambos tienen 5 como primer valor, la hora de estudio."),
     ex("Puntos de una nube: A (1, 20), B (4, 35), C (6, 25), D (8, 50). ¿Qué punto queda más arriba?", "D", "Queda más arriba el que tiene mayor valor vertical, y 50 es el mayor."),
     ex("En una nube de puntos, ¿qué se hace con los puntos? A) Unirlos con segmentos en el orden de la tabla. B) Dejarlos separados, porque cada uno es una persona distinta. C) Unir solo el primero con el último.", "B", "No hay un paso de un punto al siguiente, así que no se unen.")],
  A=[arith("En un gráfico, cada cuadrito horizontal vale 2 horas. Un punto está a 4 cuadritos a la derecha del origen. ¿Cuántas horas representa?", "4*2", "Se multiplican los cuadritos por el valor de cada uno.", " horas"),
     ex("En un gráfico, cada cuadrito horizontal vale 2 horas y cada cuadrito vertical vale 10 puntos. Un punto está 3 cuadritos a la derecha y 6 hacia arriba del origen. Escribe su par (horas, puntos).", "(6, 60)", "3 × 2 = 6 horas y 6 × 10 = 60 puntos."),
     arith("El eje vertical parte en 0 y cada cuadrito vale 10 puntos. ¿Cuántos cuadritos se necesitan como mínimo para llegar hasta 100 puntos?", "100//10", "Cada 10 puntos ocupan un cuadrito.", " cuadritos")],
  Z=[ex("Leo une con una línea los 5 puntos de una nube de horas de estudio y puntaje de 5 estudiantes distintos. ¿Es correcto? Responde sí o no.", "No", "Son personas diferentes, sin orden entre ellas; unirlas sugiere un paso de una a otra que no existe."),
     ex("En una misma nube están los puntos (5, 60) y (5, 70). ¿Pueden ser de dos estudiantes distintos de la misma población? Responde sí o no.", "Sí", "Dos estudiantes pueden estudiar las mismas horas y obtener puntajes distintos.")],
  D=[arith("Datos de ejemplo (horas, puntos): (2, 40), (4, 55), (5, 60), (7, 75), (8, 80), (10, 90). ¿Cuántos puntos más obtuvo quien más estudió que quien menos estudió?", "90-40", "Quien más estudió tiene 10 horas y 90 puntos; quien menos, 2 horas y 40 puntos.", " puntos"),
     ex("Con los datos (horas, puntos): (2, 40), (4, 55), (5, 60), (7, 75), (8, 80), (10, 90), ¿cuántos puntos de la nube quedan por encima de 70 puntos?", "3", "Superan 70 los puntos (7, 75), (8, 80) y (10, 90).")],
  ctx=[ex("Una heladería anotó la temperatura máxima y los helados vendidos en cinco días distintos (datos de ejemplo): (20 °C, 30), (24 °C, 45), (26 °C, 50), (30 °C, 70), (32 °C, 80). ¿Cuántos helados se vendieron el día más caluroso?", "80", "El día de 32 °C es el más caluroso y su par dice 80 helados.")],
  chk=[ex("En el par (x, y), ¿cuál número va primero?", "El del eje horizontal", "Primero se escribe el valor horizontal y después el vertical."),
       ex("¿Se unen con una línea los puntos de una nube de puntos de personas distintas? Responde sí o no.", "No", "Cada punto es una persona y no hay un orden entre ellas."),
       arith("Cada cuadrito vertical vale 5 puntos. Un punto está a 8 cuadritos de altura. ¿Cuántos puntos representa?", "8*5", "Se multiplican los cuadritos por el valor de cada uno.", " puntos")],
  op=("Dibuja en tu cuaderno cuadriculado una nube de puntos con estos ocho trayectos de ejemplo, escritos como (minutos de viaje, kilómetros recorridos): (3, 1), (5, 2), (8, 3), (10, 5), (14, 6), (15, 8), (20, 9), (22, 11). Elige una escala para cada eje, rotula los ejes con su unidad y marca los puntos sin unirlos. Luego escribe cuántos puntos hay sobre los 6 km y cuál es el par del trayecto más largo.",
      "Eje horizontal: 2 minutos por cuadrito; eje vertical: 1 km por cuadrito. Hay 3 puntos sobre los 6 km: (15, 8), (20, 9) y (22, 11); el punto (14, 6) está justo en 6 km, no sobre 6. El trayecto más largo es (22, 11).",
      ["ejes rotulados con unidad", "escala uniforme en cada eje", "ocho puntos bien ubicados", "puntos sin unir", "respuestas escritas"],
      ["nube dibujada", "escala anotada", "dos respuestas"],
      ["invertir los ejes", "escala irregular", "unir los puntos con líneas"],
      "Pide que lea en voz alta un punto de su nube. Reconoce que haya dejado los puntos sin unir."),
  reinforce="Ubica en tu cuaderno los puntos (1, 20), (4, 35), (6, 25) y (8, 50) con escalas a tu elección y comprueba cuál queda más alto.",
  extend="Explica por qué unir los puntos tendría sentido con la temperatura de una ciudad medida cada hora, pero no con estudiantes distintos.")

# ================================================================ OA 12 · clase 3
L(OA12, 3,
  use="Aprenderé a describir la forma de una nube de puntos: si la asociación es positiva, negativa o inexistente, qué tan fuerte es y qué punto se aleja del resto.",
  prior=["Sé construir y leer una nube de puntos.", "Sé comparar cantidades y porcentajes."],
  explain=[
      "La forma de la nube dice cómo se relacionan las dos características. Si al aumentar x los valores de y tienden a aumentar, y los puntos suben de izquierda a derecha, la asociación es positiva. Si al aumentar x los valores de y tienden a disminuir, y los puntos bajan, la asociación es negativa. Si los puntos están repartidos sin patrón, no hay asociación.",
      "La palabra clave es tiende: una asociación no se cumple en todos los casos, sino en general. Que dos puntos se contradigan no la destruye. La asociación es más fuerte cuanto más cerca de una línea imaginaria están los puntos y más débil cuanto más dispersos se ven.",
      "Un punto muy alejado del resto se llama atípico y conviene revisarlo, porque puede ser un error de anotación o un caso especial. Dentro del rango de los datos, la tendencia permite estimar un valor aproximado: para x = 40, con puntos vecinos en 35 y 50, se espera un y entre los de esos dos puntos.",
  ],
  vocab=[("asociación positiva", "al aumentar x, y tiende a aumentar"), ("asociación negativa", "al aumentar x, y tiende a disminuir"), ("tendencia", "dirección general que siguen los puntos"), ("punto atípico", "punto muy alejado del resto de la nube")],
  worked=[
      ("Asociación positiva", "Datos de ejemplo (kilómetros recorridos, litros de bencina gastados) de seis viajes: (10, 1), (20, 2), (35, 3), (50, 5), (60, 6), (80, 8). Describe la asociación.",
       ["Al pasar de 10 km a 80 km, los litros pasan de 1 a 8: aumentan.", "Los seis puntos suben de izquierda a derecha, casi sobre una línea."], "Asociación positiva y bastante fuerte"),
      ("Asociación negativa", "Datos de ejemplo (años del auto, precio en millones de pesos): (1, 12), (3, 10), (5, 9), (8, 6), (10, 5), (12, 3). Describe la asociación.",
       ["Al pasar de 1 a 12 años, el precio baja de 12 a 3.", "Los puntos bajan de izquierda a derecha."], "Asociación negativa"),
  ],
  mist=[
      ("Decir que no hay asociación porque un par de puntos se contradicen.", "La asociación es una tendencia general, no una regla sin excepciones.", "Mira el conjunto de la nube y no solo dos puntos."),
      ("Llamar «negativa» a una asociación que significa algo malo.", "Negativa solo describe que, al subir x, y baja; no es un juicio de bueno o malo.", "Fíjate solo en si los puntos suben o bajan."),
  ],
  R=[ex("Si al aumentar x los valores de y tienden a aumentar, ¿la asociación es positiva o negativa?", "Positiva", "Los puntos suben de izquierda a derecha."),
     ex("Una nube tiene puntos que bajan de izquierda a derecha. ¿Qué asociación tiene?", "Negativa", "Al aumentar x, y tiende a disminuir."),
     ex("Los puntos de una nube están repartidos por todo el gráfico sin ningún patrón. ¿Qué asociación tiene?", "No hay asociación", "No se ve ninguna tendencia de subida ni de bajada.")],
  C=[ex("Datos de ejemplo (horas de práctica de básquetbol por semana, tiros convertidos de 10): (1, 2), (2, 3), (4, 5), (5, 6), (7, 8), (8, 9). ¿Qué asociación muestran?", "Positiva", "Al aumentar las horas de práctica, los tiros convertidos aumentan."),
     ex("Datos de ejemplo (altura sobre el nivel del mar en cientos de metros, temperatura en °C): (1, 18), (5, 14), (10, 10), (15, 5), (20, 2). ¿Qué asociación muestran?", "Negativa", "Al subir la altura, la temperatura baja."),
     ex("Datos de ejemplo (número de calzado, nota de matemática): (36, 4), (38, 6), (40, 6), (37, 7), (42, 5), (39, 5). ¿Qué asociación muestran?", "No hay asociación", "Las notas suben y bajan sin relación con el número de calzado.")],
  A=[ex("Con los datos (km, litros): (10, 1), (20, 2), (35, 3), (50, 5), (60, 6), (80, 8), ¿qué cantidad de litros es más razonable para un viaje de 40 km? A) 1 litro. B) 4 litros. C) 9 litros.", "B", "40 km está entre 35 km (3 litros) y 50 km (5 litros), así que lo razonable es un valor entre 3 y 5."),
     ex("Datos de ejemplo (edad en años, estatura en cm): (6, 115), (8, 128), (10, 138), (12, 149), (14, 160), (15, 110). ¿Cuál es el punto atípico?", "(15, 110)", "Todos los demás suben con la edad, pero este queda muy por debajo de lo esperado para 15 años."),
     ex("La nube A tiene sus puntos casi sobre una línea ascendente. La nube B tiene puntos ascendentes pero muy dispersos. ¿Cuál tiene asociación positiva más fuerte?", "La nube A", "Mientras más cerca de una línea están los puntos, más fuerte es la asociación.")],
  Z=[ex("Datos de ejemplo (horas de estudio, puntos): (2, 50), (3, 45), (6, 70), (8, 80). La asociación es positiva, pero los puntos (2, 50) y (3, 45) bajan. ¿Contradice esto la asociación positiva? Responde sí o no.", "No", "La asociación es una tendencia general; basta con que, en conjunto, los puntos suban."),
     ex("Todos los puntos de una nube tienen la misma y, para cualquier valor de x. ¿Puede tener asociación positiva? Responde sí o no.", "No", "Si y no cambia cuando x aumenta, no tiende ni a subir ni a bajar.")],
  D=[arith("Datos de ejemplo (años del auto, precio en millones): (2, 11), (4, 9), (6, 7), (8, 5), (10, 3), todos sobre una línea. ¿Cuántos millones baja el precio por cada año más de antigüedad?", "(11-3)//(10-2)", "El precio baja 8 millones en 8 años, o sea 1 millón por año.", " millón por año"),
     arith("En 12 estudiantes de ejemplo, en 9 de ellos la nota sube al aumentar las horas de estudio y en 3 no. ¿Qué porcentaje de los casos sigue la tendencia?", "9*100//12", "Se divide 9 por 12 y se multiplica por 100.", "%")],
  ctx=[ex("Una profesora anota (minutos que un curso de ejemplo entrena por semana, puntos obtenidos en un torneo): (30, 4), (60, 7), (90, 9), (120, 14), (150, 16). ¿Cómo es la asociación?", "Positiva", "Al aumentar los minutos de entrenamiento, los puntos aumentan.")],
  chk=[ex("Si al aumentar x, y tiende a disminuir, ¿qué asociación hay?", "Negativa", "Los puntos bajan de izquierda a derecha."),
       ex("¿Cómo se llama un punto muy alejado del resto de la nube?", "Atípico", "Atípico es el punto que se aleja de la tendencia."),
       ex("¿Una asociación positiva se cumple en todos los casos sin excepción? Responde sí o no.", "No", "Es una tendencia general y puede haber excepciones.")],
  op=("Estos son los datos de seis estudiantes de ejemplo, como (horas de sueño por noche, minutos que tardan en resolver una tarea): (6, 50), (7, 44), (8, 40), (9, 33), (10, 31), (8, 45). Dibuja la nube, escribe si la asociación es positiva, negativa o no hay, di si es fuerte o débil y estima cuántos minutos tardaría, aproximadamente, alguien que duerme 9 horas.",
      "Los puntos bajan de izquierda a derecha: asociación negativa y bastante fuerte. Para 9 horas, el dato más cercano es (9, 33); se estima unos 33 minutos.",
      ["nube bien dibujada", "describe la dirección de los puntos", "usa la palabra tendencia", "estima dentro del rango de los datos"],
      ["nube dibujada", "frase sobre la asociación", "estimación con su explicación"],
      ["invertir los ejes", "decir positiva solo por haber más horas de sueño", "estimar fuera del rango de los datos"],
      "Pide que explique por qué la asociación no es perfecta. Reconoce que estime con el rango."),
  reinforce="Con los datos del auto, indica cuántos años de antigüedad tiene el auto más barato de la lista y cuánto cuesta.",
  extend="Inventa una nube de siete puntos con asociación positiva débil y otra con asociación negativa fuerte y explica la diferencia.")

# ================================================================ OA 12 · clase 4
L(OA12, 4,
  use="Aprenderé a evaluar afirmaciones que se hacen a partir de una tabla o una nube de puntos: qué respalda la nube, qué no, y por qué asociación no es lo mismo que causa.",
  prior=["Sé describir la asociación de una nube de puntos.", "Sé leer tablas de doble entrada y calcular porcentajes."],
  explain=[
      "Una afirmación basada en datos tiene tres partes: lo que dicen los datos, lo que se concluye y lo que queda fuera. Para evaluarla, primero compara la afirmación con la tabla o la nube: ¿los datos muestran de verdad esa tendencia? Después revisa si la conclusión dice más de lo que los datos permiten.",
      "Que dos características estén asociadas no prueba que una cause la otra. A veces una tercera característica influye en las dos: en verano suben las ventas de helados y también las de bloqueador solar, pero vender helados no hace vender bloqueador; la causa común es el calor. También puede haber coincidencia.",
      "Hay otros límites. Una muestra pequeña o de un solo grupo no permite hablar de toda la población. Fuera del rango de los datos no se sabe si la tendencia continúa. Y nunca se unen los puntos de personas distintas como si fueran una evolución en el tiempo. Una buena conclusión usa palabras como «en esta muestra» y «tiende a».",
  ],
  vocab=[("causa", "hecho que produce otro"), ("variable de fondo", "característica que influye en las dos que se comparan"), ("muestra", "parte de la población que realmente se midió"), ("rango", "valores desde el menor hasta el mayor de los datos")],
  worked=[
      ("Evaluar si hay causa", "Datos de ejemplo: los días en que un puesto vende más helados, también vende más bloqueador solar. Una persona afirma: «Los helados hacen que se venda bloqueador». ¿Está respaldada?",
       ["Hay asociación positiva entre ambas ventas.", "Pero comer helado no obliga a comprar bloqueador.", "El calor explica que las dos ventas suban juntas."], "No: hay asociación, pero la causa probable es el calor, no los helados"),
      ("Evaluar con una tabla", "De 20 estudiantes que duermen 8 horas o más, 15 tienen buen puntaje. De 10 que duermen menos, 4 lo tienen (datos de ejemplo). ¿La tabla respalda que quienes duermen más tienden a tener mejor puntaje?",
       ["Primer grupo: 15 de 20, que es 75 %.", "Segundo grupo: 4 de 10, que es 40 %.", "75 % es mayor que 40 %."], "Sí, en esta muestra la tendencia aparece; no prueba que dormir cause el puntaje"),
  ],
  mist=[
      ("Concluir «A causa B» solo porque A y B suben juntas.", "La asociación no prueba causa: puede haber una tercera característica o coincidencia.", "Escribe «están asociadas» y busca si otro factor explica ambas."),
      ("Predecir con la nube valores muy fuera del rango medido.", "No se sabe si la tendencia continúa más allá de los datos.", "Usa la tendencia solo entre el menor y el mayor valor de x."),
  ],
  R=[ex("Dos características están asociadas. ¿Eso prueba que una cause la otra? Responde sí o no.", "No", "La asociación solo dice que varían juntas; puede haber una tercera característica."),
     ex("En invierno suben las ventas de bufandas y también las de té caliente. ¿Qué característica explica que ambas suban?", "El frío", "El frío influye en las dos ventas, por eso suben juntas, sin que una cause la otra."),
     ex("Para hablar de todo el país, ¿basta una muestra de 8 estudiantes de un solo curso? Responde sí o no.", "No", "Es una muestra pequeña y de un solo grupo; no representa a toda la población.")],
  C=[ex("Una nube muestra que quienes estudiaron más horas tienden a tener más puntos. ¿Qué conclusión está respaldada? A) Estudiar más horas siempre asegura más puntos. B) En esta muestra, quienes estudiaron más horas tendieron a tener más puntos. C) Cada hora de estudio causa exactamente 10 puntos más.", "B", "La nube solo muestra una tendencia en la muestra; no asegura casos ni causas exactas."),
     ex("Se observa que las ciudades con más bomberos tienen más incendios grandes. ¿Qué característica puede explicar ambas cosas? A) El tamaño de la ciudad. B) Que los bomberos provocan incendios. C) El color de los camiones.", "A", "Una ciudad más grande necesita más bomberos y también tiene más incendios; es una variable de fondo."),
     ex("Una nube cubre edades de 6 a 15 años. Julia la usa para decir la estatura que tendrá una persona a los 40 años. ¿Es una conclusión confiable? Responde sí o no.", "No", "40 años está fuera del rango de los datos y no se sabe si la tendencia continúa.")],
  A=[arith("De 40 estudiantes que viven a menos de 1 km del colegio, 32 llegan puntuales (datos de ejemplo). ¿Qué porcentaje de ese grupo llega puntual?", "32*100//40", "Se divide 32 por 40 y se multiplica por 100.", "%"),
     arith("De 20 estudiantes que viven a más de 1 km del colegio, 10 llegan puntuales (datos de ejemplo). ¿Qué porcentaje de ese grupo llega puntual?", "10*100//20", "Se divide 10 por 20 y se multiplica por 100.", "%"),
     ex("Con 80 % de puntualidad entre quienes viven a menos de 1 km y 50 % entre quienes viven a más de 1 km, ¿qué se puede afirmar? A) Vivir cerca causa llegar puntual. B) En esta muestra hay asociación, pero no se prueba que la distancia sea la única causa. C) No existe ninguna relación entre distancia y puntualidad.", "B", "Los porcentajes difieren, así que hay asociación, pero otros factores, como el medio de transporte, también pueden influir.")],
  Z=[ex("El grupo A tiene 6 estudiantes y el grupo B tiene 300; ambos muestran la misma asociación positiva. ¿En cuál es más sólida la conclusión? Responde A o B.", "B", "Una muestra más grande tiene menos probabilidad de deberse a coincidencias."),
     ex("Nico dice: «La nube de horas de pantalla y puntaje es negativa, así que apagar la pantalla me sube el puntaje». ¿Puede asegurarlo con esa nube? Responde sí o no.", "No", "La nube muestra asociación, no causa, y no habla de un cambio en una persona en particular.")],
  D=[ex("Datos de ejemplo (horas de práctica, errores cometidos): (1, 9), (2, 8), (4, 6), (5, 5), (7, 3), (9, 1). Afirmaciones: I) Quienes practican más tienden a cometer menos errores. II) Con 20 horas de práctica nadie cometerá ningún error. III) Hay un estudiante con 5 horas y 5 errores. ¿Cuántas afirmaciones están respaldadas por los datos?", "2", "I se ve en la nube y III es el par (5, 5); II está fuera del rango de los datos (1 a 9 horas) y no se puede asegurar."),
     arith("En una nube de 50 estudiantes, el 80 % de los puntos queda sobre la línea de 60 puntos. ¿Cuántos estudiantes tienen más de 60 puntos?", "50*80//100", "El 80 % de 50 se calcula como 50 × 80 ÷ 100.", " estudiantes")],
  ctx=[ex("Un diario titula: «Los jóvenes que andan en bicicleta son más felices». La encuesta fue a 12 estudiantes de un solo colegio. ¿Cuál es su limitación principal? A) La muestra es pequeña y de un solo colegio. B) Que la bicicleta es muy cara. C) Que los jóvenes no andan en bicicleta.", "A", "Con 12 estudiantes de un solo colegio no se puede generalizar a todos los jóvenes.")],
  chk=[ex("¿Qué palabras de cautela conviene usar al concluir: «siempre» o «tiende a»?", "Tiende a", "La asociación es una tendencia y no se cumple en todos los casos."),
       ex("¿Cuál es una razón por la que no se puede concluir causa solo con una nube de puntos? A) Puede haber una tercera característica que influya en las dos. B) Las nubes de puntos no sirven para ningún análisis. C) Los puntos siempre deben unirse con una línea.", "A", "La asociación puede venir de una variable de fondo o de una coincidencia."),
       arith("Una muestra tiene 40 estudiantes y el 25 % tiene lentes. ¿Cuántos tienen lentes?", "40*25//100", "El 25 % de 40 es 40 × 25 ÷ 100.", " estudiantes")],
  op=("Lee esta afirmación de ejemplo: «En un colegio, los cursos que tienen más computadores en la sala tienen mejores notas, así que comprar computadores sube las notas». Escribe en tres frases: qué asociación podría haber detrás, otra característica que explique ambas, y cómo cambiarías la afirmación para que sea correcta, usando «en esta muestra» y «tiende a».",
      "Hay una asociación positiva entre computadores y notas. Los colegios con más recursos tienen más computadores y también más apoyo, lo que puede explicar las notas. Correcto: «En esta muestra, los cursos con más computadores tienden a tener mejores notas».",
      ["distingue asociación de causa", "propone otra característica que explique ambas", "usa «tiende a» y «en esta muestra»"],
      ["tres frases", "otra característica propuesta", "afirmación reescrita"],
      ["afirmar que la compra de computadores causa el alza de notas", "proponer una característica que no se relaciona con ninguna de las dos", "olvidar limitar la conclusión a la muestra"],
      "Pide que justifique por qué el otro factor podría influir en las dos características. Reconoce el uso de palabras de cautela."),
  reinforce="Escribe una afirmación correcta sobre los 40 estudiantes que viven a menos de 1 km usando 80 % y las palabras «en esta muestra».",
  extend="Busca una asociación cotidiana en que una tercera característica explique las otras dos y descríbela en dos frases.")
