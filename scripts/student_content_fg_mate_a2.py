"""Cuaderno del estudiante de 3.º medio Matemática FG: OAC 02 (dispersión, incerteza y probabilidad condicional)."""
from __future__ import annotations

from fractions import Fraction as F

from fg_mate_common import L, chk, ex, mean, var_pop

OA2 = "FG-MATE-3M-OAC-02"

# ================================================================ OAC 02 clase 1
D1 = [2, 4, 4, 4, 5, 5, 7, 9]
chk(mean(D1) == 5 and var_pop(D1) == 4)
chk(mean([4, 6, 6, 8]) == 6 and var_pop([4, 6, 6, 8]) == 2)
chk(mean([5, 9, 7, 3, 11]) == 7 and var_pop([1, 3, 5, 7]) == 5 and var_pop([12, 14, 14, 16, 19]) == F(28, 5) and mean([12, 14, 14, 16, 19]) == 15)
chk(var_pop([3, 3, 7, 7]) == 4 and var_pop([5, 15]) == 25 and var_pop([11, 13, 15, 17]) == 5 and var_pop([2, 8, 8]) == 8)
L(OA2, 1,
  use="Aprenderé a calcular el rango, la varianza y la desviación estándar de un conjunto de datos. Sirve para comparar qué tan parecidos o dispersos son dos grupos que tienen la misma media.",
  prior=["Sé calcular la media y la mediana.", "Sé calcular cuadrados y raíces cuadradas con calculadora."],
  explain=[
      "El rango es la diferencia entre el dato mayor y el menor. Es fácil de calcular, pero usa solo dos datos. La varianza mide, en promedio, cuánto se alejan los datos de la media: se calcula la desviación de cada dato respecto de la media, se eleva al cuadrado y se promedian esos cuadrados. En este cuaderno dividimos por la cantidad de datos n.",
      "La desviación estándar es la raíz cuadrada de la varianza y tiene la misma unidad que los datos. Si la varianza de unos tiempos es 4 min², la desviación estándar es 2 min. Cuanto mayor es la desviación estándar, más dispersos están los datos; si es 0, todos los datos son iguales.",
      "Dos grupos pueden tener la misma media y ser muy distintos. Por eso comparar solo medias puede llevar a una mala decisión. Al sumar o restar una constante a todos los datos, la dispersión no cambia; al multiplicar todos por un número positivo k, la desviación estándar queda multiplicada por k.",
  ],
  vocab=[("rango", "dato mayor menos dato menor"), ("varianza", "promedio de los cuadrados de las desviaciones respecto de la media"), ("desviación estándar", "raíz cuadrada de la varianza"), ("dispersión", "qué tan separados están los datos entre sí"), ("desviación", "diferencia entre un dato y la media")],
  worked=[
      ("Desviación estándar paso a paso", "Calcula la varianza y la desviación estándar de 2, 4, 4, 4, 5, 5, 7, 9.",
       ["Media: 40 ÷ 8 = 5.", "Desviaciones al cuadrado: 9, 1, 1, 1, 0, 0, 4, 16, que suman 32.", "Varianza: 32 ÷ 8 = 4. Desviación estándar: √4 = 2."],
       "Varianza 4; desviación estándar 2"),
      ("Comparar con el rango", "Las notas 4, 6, 6, 8 tienen media 6. Calcula el rango y la varianza.",
       ["Rango: 8 − 4 = 4.", "Desviaciones al cuadrado: 4, 0, 0, 4, que suman 8.", "Varianza: 8 ÷ 4 = 2."],
       "Rango 4; varianza 2"),
  ],
  mist=[
      ("Calcular la varianza sin elevar al cuadrado las desviaciones.", "Las desviaciones positivas y negativas se anulan y siempre da 0.", "Eleva cada desviación al cuadrado antes de promediar."),
      ("Decir que dos grupos son iguales porque tienen la misma media.", "La media no dice nada de qué tan separados están los datos.", "Compara también el rango o la desviación estándar."),
  ],
  R=[ex("Calcula la media de 5, 9, 7, 3 y 11.", "7", "La suma es 35 y 35 ÷ 5 = 7."),
     ex("Calcula el rango de 12, 7, 15, 9 y 20.", "13", "El mayor es 20 y el menor es 7: 20 − 7 = 13."),
     ex("Un dato vale 11 y la media del grupo es 7. ¿Cuál es su desviación (dato − media)?", "4", "11 − 7 = 4: está 4 unidades sobre la media.")],
  C=[ex("Calcula la varianza de 1, 3, 5 y 7 (la media es 4).", "5", "Desviaciones al cuadrado: 9, 1, 1, 9; suman 20 y 20 ÷ 4 = 5."),
     ex("Calcula la varianza de 6, 6, 6 y 6.", "0", "Todos los datos son iguales a la media: las desviaciones son 0."),
     ex("¿Cuántos cm mide la desviación estándar de un grupo con varianza 49 cm²?", "7 cm", "La desviación estándar es la raíz de la varianza: √49 = 7.")],
  A=[ex("Los tiempos 12, 14, 14, 16 y 19 min tienen media 15 min. ¿Cuál es su varianza?", "5,6", "Desviaciones al cuadrado: 9, 1, 1, 1, 16; suman 28 y 28 ÷ 5 = 5,6."),
     ex("Una máquina llena botellas con 490, 500 y 510 ml. ¿Cuál es el rango de los llenados?", "20 ml", "El mayor es 510 y el menor 490: 510 − 490 = 20."),
     ex("Calcula la desviación estándar de 3, 3, 7 y 7.", "2", "La media es 5, las desviaciones al cuadrado suman 16, la varianza es 4 y su raíz es 2.")],
  Z=[ex("A los datos 1, 3, 5 y 7 (varianza 5) se les suma 10 a cada uno. ¿Cuál es la nueva varianza?", "5", "Sumar una constante mueve la media igual que a los datos y las desviaciones no cambian."),
     ex("Los datos 1 y 3 tienen desviación estándar 1. Si cada dato se multiplica por 5, ¿cuál es la nueva desviación estándar?", "5", "Los datos pasan a 5 y 15, con media 10 y desviaciones de 5.")],
  D=[ex("Cuatro datos tienen media 10 y varianza 0. ¿Cuáles son?", "10, 10, 10 y 10", "Varianza 0 significa que todos los datos son iguales a la media."),
     ex("Los datos 2, 8 y x tienen media 6. Calcula x y la varianza.", "x = 8; varianza 8", "2 + 8 + x = 18 da x = 8; desviaciones al cuadrado 16, 4, 4 suman 24 y 24 ÷ 3 = 8.")],
  ctx=[ex("Dos ciudades de ejemplo registraron en 5 días estas temperaturas máximas (°C). Ciudad P: 18, 19, 20, 21, 22. Ciudad Q: 10, 15, 20, 25, 30. Ambas tienen media 20 °C. ¿Cuál es el rango de la ciudad Q y cuál ciudad es más variable?", "Rango 20 °C; Q es más variable", "En Q el rango es 30 − 10 = 20, mientras que en P es 4.")],
  chk=[ex("Calcula el rango de 4, 18, 9 y 11.", "14", "18 − 4 = 14."),
       ex("¿Cuál es la desviación estándar de un grupo con varianza 36?", "6", "√36 = 6."),
       ex("Si una desviación estándar es 0, ¿qué se sabe de los datos?", "Son todos iguales", "No hay ninguna distancia a la media.")],
  op=("Dos cursos de ejemplo tienen 5 notas cada uno. Curso A: 5,0 5,5 6,0 6,5 7,0. Curso B: 4,0 5,0 6,0 7,0 7,0. Calcula la media, el rango y la desviación estándar de cada curso (puedes usar calculadora) y escribe una conclusión sobre cuál curso es más parejo.",
      "Curso A: media 6,0; rango 2,0; varianza (1+0,25+0+0,25+1)/5 = 0,5; desviación estándar ≈ 0,71. Curso B: media 5,8; rango 3,0; varianza (3,24+0,64+0,04+1,44+1,44)/5 = 1,36; desviación estándar ≈ 1,17. El curso A es más parejo.",
      ["calcula media, rango y desviación estándar de cada curso", "muestra la tabla de desviaciones", "concluye con la desviación estándar"],
      ["tabla de desviaciones al cuadrado", "conclusión escrita"],
      ["no elevar las desviaciones al cuadrado", "comparar solo las medias"],
      "Si las desviaciones no suman cero al calcular la media, pide que revise primero la media."),
  reinforce="Calcula rango, varianza y desviación estándar de 2, 6, 6 y 10.",
  extend="Explica por qué la desviación estándar es más útil que el rango cuando hay un dato muy extremo.",
)

# ================================================================ OAC 02 clase 2
chk(sum([400, 420, 430, 440, 2310]) == 4000 and mean([8, 10, 12, 30]) == 15 and max([8, 10, 12, 30]) - 8 == 22)
chk(mean([3, 4, 5, 6, 90]) == F(108, 5) and F(10, 200) * 100 == 5 and F(2, 20) * 100 == 10 and F(5, 100) * 100 == 5)
L(OA2, 2,
  use="Aprenderé a interpretar la dispersión junto con el centro, la forma y el contexto de los datos. Sirve para no decidir mirando un solo número.",
  prior=["Sé calcular rango y desviación estándar.", "Sé qué es la mediana y qué es un dato extremo."],
  explain=[
      "Una medida de dispersión sola no basta: hay que leerla junto con el centro. Una desviación estándar de 2 kg es grande si el peso medio es 5 kg y pequeña si es 80 kg. Para comparar variabilidad entre datos de distinta escala se usa el coeficiente de variación: CV = (desviación estándar ÷ media) · 100, que se expresa en %.",
      "La forma de los datos también importa. Un dato extremo muy alejado sube mucho la media y la desviación estándar, pero casi no mueve la mediana. Si hay datos extremos o la distribución es muy asimétrica, la mediana describe mejor el valor típico que la media. Cuando los datos tienen forma de campana (simétrica, con más datos al centro), alrededor del 95 % queda entre la media − 2 y la media + 2 desviaciones estándar.",
      "El contexto decide qué dispersión es aceptable. Si necesitas llegar a un horario fijo, prefieres un tiempo de viaje con poca dispersión aunque la media sea parecida. Siempre pregunta de dónde vienen los datos, cuántos son y si representan a quienes quieres describir.",
  ],
  vocab=[("coeficiente de variación", "desviación estándar dividida por la media, en %"), ("dato extremo", "dato muy alejado del resto"), ("asimétrica", "con datos que se alargan más hacia un lado"), ("valor típico", "dato que representa bien al grupo"), ("homogéneo", "con datos parecidos entre sí")],
  worked=[
      ("Coeficiente de variación", "Un lote de pan tiene peso medio 200 g y desviación estándar 10 g. Calcula el CV.",
       ["Divido: 10 ÷ 200 = 0,05.", "Lo paso a porcentaje: 0,05 · 100 = 5 %."],
       "CV = 5 %"),
      ("Media o mediana", "Los sueldos de ejemplo de una empresa pequeña son 400, 420, 430, 440 y 2.310 (miles de pesos). ¿Qué medida describe mejor el sueldo típico?",
       ["Media: 4.000 ÷ 5 = 800. Mediana: el dato del medio es 430.", "Cuatro de cinco personas ganan entre 400 y 440, así que 800 no representa a casi nadie.", "El dato 2.310 es extremo y sube la media."],
       "La mediana, 430 mil pesos"),
  ],
  mist=[
      ("Decir que una desviación estándar de 2 es «pequeña» sin mirar la media.", "El tamaño de la dispersión depende de la escala de los datos.", "Compárala con la media, por ejemplo con el coeficiente de variación."),
      ("Usar siempre la media para describir el centro.", "Con datos extremos la media se aleja del valor típico.", "Mira la mediana cuando haya datos extremos."),
  ],
  R=[ex("Dos grupos tienen media 70. El primero tiene desviación estándar 3 y el segundo 12. ¿Cuál es más homogéneo?", "El primero", "Menor desviación estándar significa datos más cercanos a la media."),
     ex("Si un conjunto de datos tiene desviación estándar 0, ¿qué se sabe de los datos?", "Todos son iguales", "Ningún dato se aleja de la media."),
     ex("Un dato extremo muy alto, ¿sube o baja la desviación estándar? A) La baja B) La sube", "B", "Una desviación grande respecto de la media aumenta el promedio de cuadrados.")],
  C=[ex("Calcula el coeficiente de variación de un grupo con media 50 y desviación estándar 5.", "10 %", "5 ÷ 50 = 0,10, es decir 10 %."),
     ex("Los datos 3, 4, 5, 6 y 90 tienen media 21,6 y mediana 5. ¿Qué medida describe mejor el centro? A) La media B) La mediana", "B", "El dato 90 es extremo y la media queda lejos de los otros cuatro."),
     ex("Una temperatura media es 20 °C con desviación estándar de 2 °C. ¿Qué significa? A) Todos los días hay exactamente 22 °C B) Los días suelen estar a unos 2 °C de los 20 °C", "B", "La desviación estándar mide la distancia típica a la media.")],
  A=[ex("El pan P pesa 200 g con desviación estándar 10 g; el pan Q pesa 20 g con desviación estándar 2 g. ¿Cuál tiene mayor variabilidad relativa y con qué CV?", "Q, con 10 % (P tiene 5 %)", "2 ÷ 20 = 10 %, mayor que 10 ÷ 200 = 5 %."),
     ex("Los sueldos de ejemplo 400, 420, 430, 440 y 2.310 (miles de pesos) tienen mediana 430. ¿Cuál es la media?", "800 mil pesos", "La suma es 4.000 mil y 4.000 ÷ 5 = 800."),
     ex("Con media 20 °C y desviación estándar 2 °C, ¿qué intervalo forman la media − 1 desviación y la media + 1 desviación?", "18 °C a 22 °C", "20 − 2 = 18 y 20 + 2 = 22.")],
  Z=[ex("Dos tiendas tienen 40 clientes diarios de media. Una va de 38 a 42 y la otra de 10 a 70. ¿Qué medida las diferencia? A) La media B) La desviación estándar", "B", "La media es igual en ambas; cambia cuán separados están los datos."),
     ex("Un grupo tiene media 50 y desviación estándar 5. Si se suma 50 a cada dato, ¿el CV sube o baja?", "Baja", "La media pasa a 100 y la desviación sigue en 5: el CV baja de 10 % a 5 %.")],
  D=[ex("Un curso de ejemplo tiene notas con media 5,0 y desviación estándar 1,0, y forma de campana. Con media ± 2 desviaciones, ¿qué intervalo cubre casi todas las notas?", "3,0 a 7,0", "5,0 − 2,0 = 3,0 y 5,0 + 2,0 = 7,0."),
     ex("Los datos 8, 10 y 12 se amplían con un dato nuevo, 30. ¿Cuál es la nueva media y el nuevo rango?", "Media 15; rango 22", "La suma es 60 con 4 datos: media 15; rango 30 − 8 = 22.")],
  ctx=[ex("Dos líneas de buses de ejemplo tienen tiempo de espera medio de 10 min. En 5 días, la línea 1 tuvo esperas de 8, 10, 10, 12 y 10 min; la línea 2, de 2, 5, 10, 15 y 18 min. Si debes llegar a un horario fijo, ¿cuál conviene?", "La línea 1", "Tiene la misma media, pero esperas casi iguales (rango 4 frente a 16).")],
  chk=[ex("Calcula el CV de un grupo con media 80 y desviación estándar 4.", "5 %", "4 ÷ 80 = 0,05."),
       ex("¿Qué medida de centro cambia menos con un dato extremo? A) Media B) Mediana", "B", "La mediana depende del orden de los datos, no de su tamaño."),
       ex("Dos grupos tienen igual desviación estándar y medias de 10 y 100. ¿Cuál tiene menor variabilidad relativa?", "El de media 100", "Su CV es menor porque la misma desviación se divide entre una media mayor.")],
  op=("Dos fábricas de ejemplo producen tornillos. La fábrica 1 tiene longitud media 40 mm y desviación estándar 0,4 mm. La fábrica 2 tiene longitud media 8 mm y desviación estándar 0,4 mm. Calcula el CV de cada una, decide cuál es relativamente más variable y escribe tres preguntas que harías sobre los datos antes de elegir un proveedor.",
      "Fábrica 1: 0,4 ÷ 40 = 1 %. Fábrica 2: 0,4 ÷ 8 = 5 %. La fábrica 2 es relativamente más variable. Preguntas: cuántos tornillos se midieron, cómo se eligieron, qué tolerancia admite el uso.",
      ["calcula bien ambos CV", "decide con base en la dispersión relativa", "plantea preguntas sobre origen y tamaño de los datos"],
      ["dos cálculos de CV", "tres preguntas escritas"],
      ["comparar solo las desviaciones absolutas", "olvidar el contexto"],
      "Si compara solo 0,4 con 0,4, pide que compare cada desviación con su media."),
  reinforce="Calcula el CV de un grupo con media 25 y desviación estándar 2,5 y explica qué significa.",
  extend="Inventa dos conjuntos de cinco datos con la misma mediana, distinta media y un dato extremo, y explica cuál medida elegirías.",
)

# ================================================================ OAC 02 clase 3
chk(F(18, 48) == F(3, 8) and F(18, 40) == F(9, 20) and F(12, 100) * 10 == F(12, 10))
chk(F(6, 10) * F(2, 100) + F(4, 10) * F(5, 100) == F(32, 1000) and F(6, 10) * F(2, 100) / F(32, 1000) == F(3, 8))
chk(F(1, 2) * F(3, 4) + F(1, 2) * F(1, 4) == F(1, 2) and F(1, 2) * F(3, 4) / F(1, 2) == F(3, 4))
chk(F(5, 100) * F(9, 10) / (F(5, 100) * F(9, 10) + F(95, 100) * F(1, 10)) == F(9, 28))
chk(F(6, 10) * F(5, 10) + F(2, 10) * F(5, 10) == F(4, 10) and F(7, 10) * F(2, 10) + F(3, 10) * F(5, 100) == F(155, 1000))
L(OA2, 3,
  use="Aprenderé a calcular probabilidades condicionales con tablas de doble entrada y con diagramas de árbol. Sirve para interpretar frases como «de los que usan bus, ¿cuántos llegan tarde?».",
  prior=["Sé calcular probabilidades como casos favorables sobre casos posibles.", "Sé multiplicar y sumar fracciones y decimales."],
  explain=[
      "La probabilidad condicional P(A | B) es la probabilidad de A cuando ya sabemos que B ocurrió. Se calcula como P(A | B) = P(A y B) ÷ P(B). En una tabla de doble entrada, es lo mismo que mirar solo la fila o columna de B y dividir los casos de A y B entre el total de B.",
      "En un diagrama de árbol cada rama lleva su probabilidad. Para el camino completo se multiplican las probabilidades de las ramas. Para la probabilidad total de un suceso se suman los caminos que lo contienen. Luego se puede invertir la condición: P(A | B) no es igual a P(B | A) en general.",
      "Dos sucesos son independientes si saber que uno ocurrió no cambia la probabilidad del otro, es decir, P(A y B) = P(A) · P(B). Si no se cumple esa igualdad, hay dependencia. Escribe siempre qué dato es la condición, porque eso decide el denominador.",
  ],
  vocab=[("probabilidad condicional", "probabilidad de A sabiendo que B ocurrió"), ("tabla de doble entrada", "tabla con dos características a la vez"), ("diagrama de árbol", "esquema con ramas y probabilidades por etapa"), ("sucesos independientes", "sucesos donde uno no cambia la probabilidad del otro"), ("probabilidad total", "suma de los caminos que llevan a un suceso")],
  worked=[
      ("Condicional en una tabla", "En un curso de ejemplo de 80 estudiantes: practican deporte 22 hombres y 18 mujeres; no practican 10 hombres y 30 mujeres. Calcula P(practica deporte | es mujer) y P(es mujer | practica deporte).",
       ["Hay 18 + 30 = 48 mujeres y 22 + 18 = 40 estudiantes que practican deporte.", "P(deporte | mujer) = 18 ÷ 48 = 3/8.", "P(mujer | deporte) = 18 ÷ 40 = 9/20."],
       "3/8 y 9/20 (no son iguales)"),
      ("Árbol y condición inversa", "La máquina A produce el 60 % de las piezas y el 2 % de ellas sale defectuosa. La máquina B produce el 40 % y el 5 % sale defectuosa. Si una pieza es defectuosa, ¿cuál es la probabilidad de que venga de A?",
       ["Camino A y defectuosa: 0,6 · 0,02 = 0,012. Camino B y defectuosa: 0,4 · 0,05 = 0,020.", "Probabilidad total de defectuosa: 0,012 + 0,020 = 0,032.", "P(A | defectuosa) = 0,012 ÷ 0,032 = 3/8."],
       "3/8 = 0,375"),
  ],
  mist=[
      ("Dividir entre el total de la tabla en vez de entre el total de la condición.", "El denominador de P(A | B) es B, no todos los casos.", "Pregunta: ¿cuántos casos cumplen la condición? Divide por esa cantidad."),
      ("Creer que P(A | B) = P(B | A).", "Cambian el denominador y la pregunta.", "Escribe cuál suceso es la condición antes de calcular."),
  ],
  R=[ex("¿Cuál es la fórmula de P(A | B)? A) P(A y B) ÷ P(A) B) P(A y B) ÷ P(B)", "B", "La condición B es la que queda en el denominador."),
     ex("De 50 estudiantes de ejemplo, 20 tienen bicicleta y 15 de esos 20 tienen casco. ¿Cuál es P(casco | bicicleta)?", "3/4", "Solo cuentan los 20 con bicicleta: 15 ÷ 20."),
     ex("Se lanza un dado. ¿Cuál es la probabilidad de que salga par si se sabe que salió mayor que 3?", "2/3", "Los resultados mayores que 3 son 4, 5 y 6, y de ellos son pares 4 y 6.")],
  C=[ex("En un grupo de ejemplo de 60 personas: tienen mascota 18 hombres y 22 mujeres; no tienen 12 hombres y 8 mujeres. ¿Cuál es P(tiene mascota | es hombre)?", "3/5", "Hay 30 hombres y 18 de ellos tienen mascota: 18 ÷ 30."),
     ex("En el mismo grupo de 60 personas (tienen mascota 18 hombres y 22 mujeres; no tienen 12 hombres y 8 mujeres), ¿cuál es P(es mujer | tiene mascota)?", "11/20", "Tienen mascota 40 personas y 22 son mujeres: 22 ÷ 40."),
     ex("Si P(A y B) = 0,12 y P(B) = 0,4, ¿cuánto vale P(A | B)?", "0,3", "0,12 ÷ 0,4 = 0,3.")],
  A=[ex("La bolsa 1 tiene 3 fichas rojas y 1 azul; la bolsa 2 tiene 1 roja y 3 azules. Se elige una bolsa al azar (1/2 cada una) y se saca una ficha. ¿Cuál es la probabilidad de sacar una roja?", "1/2", "(1/2)(3/4) + (1/2)(1/4) = 3/8 + 1/8 = 1/2."),
     ex("Con las mismas bolsas (bolsa 1: 3 rojas y 1 azul; bolsa 2: 1 roja y 3 azules; bolsa elegida al azar), salió una ficha roja. ¿Cuál es la probabilidad de que venga de la bolsa 1?", "3/4", "(3/8) ÷ (1/2) = 3/4."),
     ex("Una bolsa tiene 3 fichas negras y 2 blancas. Se sacan dos sin devolverlas. Si la primera fue negra, ¿cuál es la probabilidad de que la segunda sea negra?", "1/2", "Quedan 4 fichas, 2 de ellas negras: 2 ÷ 4.")],
  Z=[ex("Se sabe que P(A) = 0,5, P(B) = 0,4 y P(A y B) = 0,2. ¿Son independientes? A) Sí B) No", "A", "0,5 · 0,4 = 0,2, igual que P(A y B)."),
     ex("De 100 personas de ejemplo, 50 son mujeres, 20 usan lentes y 10 son mujeres con lentes. Calcula P(lentes | mujer) y P(mujer | lentes).", "1/5 y 1/2", "10 ÷ 50 = 1/5 y 10 ÷ 20 = 1/2: son distintas.")],
  D=[ex("Un detector de ejemplo marca alerta en el 90 % de los paquetes defectuosos y en el 10 % de los no defectuosos. El 5 % de los paquetes es defectuoso. Si marca alerta, ¿qué probabilidad hay de que sea defectuoso?", "9/28, aprox. 0,32", "0,045 de alerta con defecto y 0,095 de alerta sin defecto; 0,045 ÷ 0,14 = 9/28."),
     ex("Se sabe que P(A | B) = 0,6, P(B) = 0,5 y P(A | no B) = 0,2. Calcula P(A).", "0,4", "0,6 · 0,5 + 0,2 · 0,5 = 0,3 + 0,1.")],
  ctx=[ex("En un liceo de ejemplo, el 70 % de los estudiantes llega en bus. De los que llegan en bus, el 20 % llega tarde; de los demás, el 5 %. ¿Qué proporción del liceo llega tarde?", "0,155 (15,5 %)", "0,7 · 0,2 + 0,3 · 0,05 = 0,14 + 0,015.")],
  chk=[ex("Hay 60 casos con B y 15 de ellos también tienen A. ¿Cuánto vale P(A | B)?", "1/4", "15 ÷ 60 = 1/4."),
       ex("Si A y B son independientes, ¿a qué es igual P(A | B)? A) P(B) B) P(A)", "B", "Saber que B ocurrió no cambia la probabilidad de A."),
       ex("¿Cuánto vale P(B | B)?", "1", "Si B ya ocurrió, es seguro que B ocurre.")],
  op=("Un liceo de ejemplo encuesta a 100 estudiantes: 60 viven a más de 2 km del liceo, y de ellos 45 llegan en transporte. De los 40 que viven a 2 km o menos, 10 llegan en transporte. Arma una tabla de doble entrada y un árbol, y calcula P(transporte), P(vive lejos | transporte) y P(transporte | vive cerca).",
      "Transporte: 45 + 10 = 55, así que P(transporte) = 55/100 = 0,55. P(lejos | transporte) = 45/55 = 9/11. P(transporte | cerca) = 10/40 = 1/4.",
      ["construye una tabla o árbol con los datos", "identifica la condición en cada pregunta", "usa el denominador correcto"],
      ["tabla de doble entrada", "tres probabilidades calculadas"],
      ["dividir por el total en vez de por la condición", "confundir P(A | B) con P(B | A)"],
      "Si el denominador falla, pide que subraye la condición en la pregunta y cuente solo esos casos."),
  reinforce="Con la tabla del primer ejemplo resuelto (80 estudiantes y deporte) inventa otra pregunta condicional y respóndela.",
  extend="Explica con un ejemplo por qué P(A | B) y P(B | A) pueden ser muy distintas.",
)

# ================================================================ OAC 02 clase 4
chk(F(7, 10) * 20000 + F(3, 10) * 5000 == 15500 and F(7, 10) * 12000 + F(3, 10) * 14000 == 12600)
chk(F(4, 10) * 20000 + F(6, 10) * 5000 == 11000 and F(4, 10) * 12000 + F(6, 10) * 14000 == 13200)
chk(F(60, 1) * F(4, 7) - 10 * (1 - F(4, 7)) == 30 and F(2, 10) * 100 - F(4, 10) * 50 == 0 and F(4, 10) * 150000 - 50000 == 10000)
L(OA2, 4,
  use="Aprenderé a tomar una decisión cuando hay incerteza, calculando un valor esperado y declarando supuestos y límites. Sirve para justificar una elección sin fingir que el futuro es seguro.",
  prior=["Sé calcular probabilidades y que la suma de todas las probabilidades es 1.", "Sé interpretar rango y desviación estándar."],
  explain=[
      "El valor esperado de una situación con resultados x₁, x₂… y probabilidades p₁, p₂… es E = x₁·p₁ + x₂·p₂ + … Es el promedio a largo plazo si la situación se repitiera muchas veces. No es lo que ocurre en una sola vez: en una sola vez ocurre uno de los resultados.",
      "Para decidir se comparan los valores esperados, pero también la dispersión de los resultados (qué tan malo puede ser lo peor) y los supuestos: de dónde salen las probabilidades, si son estimaciones y si los sucesos se repiten con las mismas condiciones. Una decisión puede cambiar si cambia una probabilidad, por eso se hace un análisis de sensibilidad.",
      "Una buena respuesta escribe la decisión, el cálculo, los supuestos y los límites. Por ejemplo: «Elijo X porque su valor esperado es mayor, suponiendo que la probabilidad de lluvia es 0,3; si fuera 0,6, elegiría Y». Si los datos vienen de pocas personas o de una muestra no aleatoria, hay que decirlo.",
  ],
  vocab=[("valor esperado", "promedio de los resultados ponderado por sus probabilidades"), ("supuesto", "condición que se acepta para poder calcular"), ("análisis de sensibilidad", "revisar cómo cambia la decisión si cambian los datos"), ("muestra representativa", "grupo que refleja a toda la población"), ("riesgo", "posibilidad de un resultado desfavorable")],
  worked=[
      ("Elegir entre dos opciones", "En una feria de ejemplo, la probabilidad de sol es 0,7 y la de lluvia 0,3. Con sol, vender helados gana $20.000 y vender empanadas gana $12.000. Con lluvia, helados gana $5.000 y empanadas $14.000. ¿Cuál conviene según el valor esperado?",
       ["Helados: 0,7 · 20.000 + 0,3 · 5.000 = 14.000 + 1.500 = 15.500.", "Empanadas: 0,7 · 12.000 + 0,3 · 14.000 = 8.400 + 4.200 = 12.600.", "Los helados tienen mayor valor esperado, pero su peor caso ($5.000) es peor que el de las empanadas ($12.000)."],
       "Helados, con $15.500 esperados; empanadas dan $12.600"),
      ("Sensibilidad", "En la misma feria, ¿cambia la decisión si la probabilidad de lluvia fuera 0,6?",
       ["Helados: 0,4 · 20.000 + 0,6 · 5.000 = 8.000 + 3.000 = 11.000.", "Empanadas: 0,4 · 12.000 + 0,6 · 14.000 = 4.800 + 8.400 = 13.200."],
       "Sí: con lluvia 0,6 conviene vender empanadas"),
  ],
  mist=[
      ("Decidir solo por el valor esperado, sin mirar el peor caso.", "Una opción con buen promedio puede tener un resultado muy malo.", "Compara también el resultado más bajo y cuánto riesgo puedes asumir."),
      ("Decir que el valor esperado es lo que ocurrirá la próxima vez.", "Es un promedio a largo plazo, no una predicción de una sola vez.", "Escribe «en promedio, si se repite muchas veces»."),
  ],
  R=[ex("Se gana $100 con probabilidad 0,5 y $0 con probabilidad 0,5. ¿Cuál es el valor esperado?", "$50", "100 · 0,5 + 0 · 0,5 = 50."),
     ex("Tres resultados tienen probabilidades 0,2, 0,5 y x. ¿Cuánto vale x?", "0,3", "Las probabilidades suman 1: 1 − 0,2 − 0,5."),
     ex("Se lanza un dado y se ganan $6 solo si sale 6; en otro caso no se gana nada. ¿Cuál es el valor esperado, en pesos?", "1", "6 · (1/6) + 0 · (5/6) = 1.")],
  C=[ex("Resultados de 10, 20 y 40 con probabilidades 0,2, 0,5 y 0,3. Calcula el valor esperado.", "24", "10·0,2 + 20·0,5 + 40·0,3 = 2 + 10 + 12."),
     ex("Un plan gana 8 con probabilidad 0,75 y pierde 12 con probabilidad 0,25. ¿Cuál es el valor esperado?", "3", "8·0,75 − 12·0,25 = 6 − 3."),
     ex("Una rifa de ejemplo vende 1.000 boletos a $100 cada uno y tiene un solo premio de $50.000. ¿Cuál es la ganancia esperada por boleto, en pesos?", "−50", "El premio esperado es 50.000 ÷ 1.000 = 50, y el boleto cuesta 100: 50 − 100 = −50.")],
  A=[ex("El proyecto X gana $60.000 con probabilidad 0,5 y pierde $10.000 con probabilidad 0,5. ¿Cuál es su valor esperado, en miles de pesos?", "25", "60·0,5 − 10·0,5 = 30 − 5."),
     ex("Con el mismo proyecto X (gana $60.000 con probabilidad p y pierde $10.000 con probabilidad 1 − p), si p sube a 0,7, ¿cuál es el valor esperado en miles de pesos?", "39", "60·0,7 − 10·0,3 = 42 − 3."),
     ex("El proyecto Y da $30.000 seguros. Con p = 0,5, X vale 25 mil esperados. ¿Qué proyecto tiene mayor valor esperado?", "Y", "30 mil es mayor que 25 mil.")],
  Z=[ex("Daniela dice que el valor esperado sirve igual para una sola vez que para muchas. ¿Cuál es la mejor respuesta? A) Es igual de bueno para una sola vez B) Describe mejor el promedio de muchas repeticiones", "B", "En una sola vez ocurre un solo resultado, no el promedio."),
     ex("Una encuesta a 12 conocidos dice que 9 prefieren la opción X. ¿Qué falta para generalizar? A) Preguntar a más amigos, aunque no se elijan al azar B) Una muestra aleatoria y representativa", "B", "Sin muestra representativa no se puede generalizar a todos.")],
  D=[ex("X gana 60 con probabilidad p y pierde 10 con probabilidad 1 − p. ¿Para qué p el valor esperado de X iguala a 30?", "4/7", "60p − 10(1 − p) = 30 da 70p = 40."),
     ex("Un plan gana 100 con probabilidad p, gana 0 con probabilidad 2p y pierde 50 con probabilidad 0,4. Calcula p y el valor esperado.", "p = 0,2; valor esperado 0", "p + 2p + 0,4 = 1 da p = 0,2; 100·0,2 − 50·0,4 = 0.")],
  ctx=[ex("Un taller de ejemplo evalúa contratar un mecánico extra que cuesta $50.000 al mes. Con probabilidad 0,4 habrá mucha demanda y ganará $150.000 más; con probabilidad 0,6 no ganará nada extra. ¿Cuál es el resultado neto esperado, en pesos?", "$10.000", "0,4 · 150.000 − 50.000 = 60.000 − 50.000.")],
  chk=[ex("Un juego da 10 con probabilidad 0,3 y 0 con probabilidad 0,7. ¿Cuál es el valor esperado?", "3", "10 · 0,3 = 3."),
       ex("¿Qué es un análisis de sensibilidad? A) Medir cuánto confía la gente en el resultado B) Ver cómo cambia la decisión si cambian los datos", "B", "Se modifican probabilidades o costos para ver si la decisión se mantiene."),
       ex("Si un supuesto no se puede comprobar, ¿qué hay que hacer al comunicar la decisión?", "Declararlo", "Los supuestos y límites son parte de una buena respuesta.")],
  op=("Un negocio de ejemplo debe elegir entre dos promociones. Promoción A: con probabilidad 0,6 aumenta la ganancia en $80.000 y con probabilidad 0,4 la disminuye en $20.000. Promoción B: ganancia segura de $40.000. Calcula el valor esperado de cada una, el rango de la A y escribe una decisión con dos supuestos y un límite. Luego cambia 0,6 por 0,3 y repite.",
      "A: 0,6·80.000 − 0,4·20.000 = 48.000 − 8.000 = 40.000, igual que B; con 0,3: 24.000 − 14.000 = 10.000, menor que B. Rango de A: 100.000. Decisión: con 0,6 son equivalentes en promedio y B es sin riesgo; con 0,3 conviene B. Supuestos: probabilidades estimadas, mismas condiciones cada mes. Límite: son estimaciones de ejemplo.",
      ["calcula bien el valor esperado en ambos escenarios", "compara la dispersión o el peor caso", "declara supuestos y límites"],
      ["dos cálculos de valor esperado", "decisión escrita con supuestos"],
      ["decidir solo por el promedio", "no revisar qué pasa si cambia la probabilidad"],
      "Si omite los límites, pide que escriba qué dato está estimado y qué pasaría si estuviera equivocado."),
  reinforce="Calcula el valor esperado de ganar 20 con probabilidad 0,25 y perder 4 con probabilidad 0,75.",
  extend="Explica por qué una persona podría elegir una opción con menor valor esperado y menos riesgo.",
)
