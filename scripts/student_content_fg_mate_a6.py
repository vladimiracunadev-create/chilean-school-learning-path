"""Cuaderno del estudiante de 4.º medio Matemática FG: OAC 02 (decisiones bajo incerteza con modelos binomial y normal)."""
from __future__ import annotations

import math
from fractions import Fraction as F

from fg_mate_common import L, binom, chk, ex

OA2 = "FG-MATE-4M-OAC-02"

# ================================================================ OAC 02 clase 1
chk(F(5, 10) ** 0 == 1 and 12 * F(1, 6) == 2 and 10 * F(1, 2) == 5 and 30 * F(7, 10) == 21 and 1000 * 0 == 0)
L(OA2, 1,
  use="Aprenderé a reconocer cuándo una situación se puede modelar con una distribución binomial, identificando n, p y la variable X. Sirve para no aplicar el modelo donde no corresponde.",
  prior=["Sé calcular probabilidades de sucesos simples.", "Sé qué significa que dos sucesos sean independientes."],
  explain=[
      "Un ensayo de Bernoulli es un experimento con solo dos resultados: éxito (probabilidad p) o fracaso (probabilidad q = 1 − p). Una variable binomial X cuenta cuántos éxitos hay en n ensayos. Se escribe X ~ B(n, p). Sus valores posibles son 0, 1, 2, …, n.",
      "El modelo binomial exige cuatro condiciones: hay un número fijo n de ensayos, cada ensayo tiene solo éxito o fracaso, la probabilidad de éxito p es la misma en todos los ensayos y los ensayos son independientes. Si se extrae sin reposición de una población pequeña, p cambia y no es binomial exacto.",
      "El promedio esperado de éxitos es E(X) = n · p. Por ejemplo, con n = 50 y p = 0,2 se esperan 10 éxitos. Antes de calcular, escribe qué es un éxito, cuánto valen n y p, y comprueba una a una las condiciones. Aclara también qué datos de la situación son supuestos.",
  ],
  vocab=[("ensayo de Bernoulli", "experimento con solo dos resultados: éxito o fracaso"), ("variable binomial", "variable que cuenta los éxitos en n ensayos"), ("independientes", "sin que un resultado cambie la probabilidad de otro"), ("esperanza", "promedio de éxitos que se espera, igual a n · p"), ("reposición", "devolver lo extraído antes de volver a extraer")],
  worked=[
      ("Reconocer una binomial", "Se lanza 5 veces una moneda y se cuenta el número de caras. ¿Es binomial? Identifica n, p y los valores de X.",
       ["Hay 5 ensayos fijos y cada uno tiene dos resultados: cara o sello.", "La probabilidad de cara es 1/2 en todos los lanzamientos y son independientes."],
       "Sí: n = 5, p = 1/2 y X toma valores de 0 a 5"),
      ("Un caso que no lo es", "Se sacan 3 cartas sin reposición de un mazo de 10 cartas (5 rojas y 5 negras) y se cuenta cuántas son rojas. ¿Es binomial?",
       ["Cada carta que se saca cambia la composición del mazo.", "Entonces la probabilidad de roja no es la misma en cada extracción y los ensayos no son independientes."],
       "No es binomial exacta, porque p cambia"),
  ],
  mist=[
      ("Usar el modelo binomial sin revisar si p es constante.", "Si p cambia entre ensayos, la fórmula no es válida.", "Revisa las cuatro condiciones antes de calcular."),
      ("Confundir n con el número de éxitos.", "n es el número total de ensayos; X cuenta los éxitos.", "Escribe «n = total de ensayos» y «X = éxitos»."),
  ],
  R=[ex("En un ensayo de Bernoulli la probabilidad de éxito es 0,3. ¿Cuál es la probabilidad de fracaso?", "0,7", "q = 1 − 0,3."),
     ex("Si X cuenta los éxitos en n = 8 ensayos, ¿cuáles son sus valores posibles?", "De 0 a 8", "Puede haber desde ningún éxito hasta los 8 ensayos."),
     ex("¿A qué es igual la esperanza E(X) de una binomial? A) n · q B) n · p", "B", "El promedio es el número de ensayos por la probabilidad de éxito.")],
  C=[ex("Se eligen al azar 20 personas de una ciudad grande y el 40 % tiene bicicleta. Si X cuenta quiénes tienen bicicleta, ¿cuánto valen n y p?", "n = 20 y p = 0,4", "n es el número de personas elegidas y p la proporción con bicicleta."),
     ex("Calcula E(X) para n = 50 y p = 0,2.", "10", "50 · 0,2."),
     ex("Un jugador acierta cada tiro con probabilidad 0,6, de forma independiente. ¿Es binomial contar los aciertos en 10 tiros? A) Sí B) No", "A", "Hay 10 ensayos, dos resultados, p constante e independencia.")],
  A=[ex("Se lanza 12 veces un dado y X cuenta cuántas veces sale 6. ¿Cuánto valen n, p y E(X)?", "n = 12, p = 1/6 y E(X) = 2", "12 · 1/6 = 2."),
     ex("Una urna tiene 2 bolas rojas y 2 azules. Se sacan 2 sin reposición y X cuenta las rojas. ¿Es binomial? A) Sí B) No", "B", "Sin reposición la probabilidad de la segunda bola depende de la primera."),
     ex("Una prueba de 10 preguntas con 5 alternativas cada una se responde al azar. ¿Cuántas respuestas correctas se esperan?", "2", "p = 1/5 y 10 · 1/5 = 2.")],
  Z=[ex("Ana dice que contar los días de lluvia de un mes es binomial con n = 30 y p fija. ¿Qué condición es dudosa? A) Que haya solo dos resultados, lluvia o no lluvia B) La independencia, porque los días seguidos se parecen", "B", "El clima de un día influye en el siguiente."),
     ex("Si la probabilidad de acierto de un jugador baja a medida que se cansa, ¿qué condición del modelo binomial falla?", "Que p sea constante", "La probabilidad cambia entre ensayos.")],
  D=[ex("Una caja tiene 50 piezas y 10 defectuosas. Se sacan 3 piezas con reposición y X cuenta las defectuosas. ¿Cuánto valen n y p?", "n = 3 y p = 0,2", "Con reposición p = 10/50 = 0,2 en cada extracción."),
     ex("Un jugador acierta el 70 % de sus tiros. ¿Cuántos tiros debe lanzar para que se esperen 21 aciertos?", "30", "n · 0,7 = 21 da n = 30.")],
  ctx=[ex("En un liceo de ejemplo, el 30 % de los estudiantes llega en bus. Se eligen 10 al azar y X cuenta los que llegan en bus. ¿Cuántos se esperan, en promedio?", "3", "10 · 0,3 = 3.")],
  chk=[ex("¿Cuáles son los dos resultados de un ensayo de Bernoulli?", "Éxito y fracaso", "El modelo solo distingue estos dos resultados."),
       ex("Con n = 40 y p = 0,25, ¿cuánto vale E(X)?", "10", "40 · 0,25."),
       ex("¿Es binomial contar los éxitos si p cambia en cada ensayo? A) Sí B) No", "B", "La binomial exige p constante.")],
  op=("Se te dan tres situaciones de ejemplo: (1) Se lanza un dado 20 veces y se cuentan los números pares. (2) Se sacan 4 cartas sin reposición de un mazo de 12 cartas y se cuentan las rojas. (3) De un curso de 30 estudiantes se pregunta solo a 5 amigos del encuestador si les gusta cierta canción y se cuentan los que dicen sí. Para cada una decide si el modelo binomial es adecuado, escribe n y p si corresponde y qué condición falla si no corresponde.",
      "(1) Sí: n = 20, p = 1/2. (2) No: sin reposición, p cambia. (3) No es adecuado: la muestra de amigos no es aleatoria y sus respuestas pueden parecerse, así que no son independientes ni representan al curso.",
      ["revisa las cuatro condiciones", "identifica n y p cuando corresponde", "nombra la condición que falla"],
      ["tabla de tres situaciones", "condiciones verificadas"],
      ["aplicar el modelo sin revisar condiciones", "confundir n con X"],
      "Si acepta las tres, pide que explique cómo se obtiene el resultado de cada ensayo y si cambia la probabilidad."),
  reinforce="Escribe una situación cotidiana que sí sea binomial, con n y p, y una que no lo sea.",
  extend="Explica por qué, al sacar sin reposición pocos elementos de una población muy grande, el modelo binomial se puede usar como aproximación.",
)

# ================================================================ OAC 02 clase 2
chk(math.comb(4, 2) == 6 and binom(3, 1, F(1, 5)) == F(384, 1000) and binom(4, 0, F(3, 10)) == F(2401, 10000))
chk(binom(3, 2, F(7, 10)) == F(441, 1000) and binom(5, 3, F(1, 2)) == F(5, 16) and binom(6, 3, F(1, 2)) == F(5, 16))
chk(1 - F(1, 8) == F(7, 8) and binom(4, 1, F(1, 10)) == F(2916, 10000) and 1 - F(4, 5) ** 5 == F(67232, 100000) and F(1, 2) ** 5 == F(1, 32))
chk(sum(math.comb(5, k) for k in range(6)) == 32 and math.comb(5, 4) + math.comb(5, 5) == 6)
L(OA2, 2,
  use="Aprenderé a calcular probabilidades binomiales P(X = k) con la fórmula y a representarlas en una tabla o un gráfico de barras. Sirve para ver toda la distribución y responder preguntas como «al menos uno».",
  prior=["Conozco el modelo binomial y sus condiciones.", "Sé calcular combinaciones C(n, k) con calculadora o con el triángulo de Pascal."],
  explain=[
      "La probabilidad de obtener exactamente k éxitos en n ensayos es P(X = k) = C(n, k) · pᵏ · qⁿ⁻ᵏ, donde C(n, k) cuenta de cuántas maneras se pueden ubicar los k éxitos entre los n ensayos. Por ejemplo, C(4, 2) = 6. El factor pᵏ · qⁿ⁻ᵏ es la probabilidad de cada una de esas maneras.",
      "Una misma distribución se puede representar de dos formas: con una tabla de valores de k y P(X = k), o con un gráfico de barras. Para n = 4 y p = 1/2 la tabla es 1/16, 4/16, 6/16, 4/16 y 1/16. Las probabilidades de todos los valores suman siempre 1. Cuando p = 1/2 la distribución es simétrica.",
      "Para probabilidades como «al menos uno» se usa el complemento: P(X ≥ 1) = 1 − P(X = 0). Para «a lo más» o «entre» se suman las filas de la tabla que corresponden. Revisa siempre que el resultado esté entre 0 y 1 y que tenga sentido con la tabla.",
  ],
  vocab=[("combinación", "número de maneras de elegir k de n elementos sin importar el orden"), ("distribución", "lista de valores de X con sus probabilidades"), ("complemento", "suceso contrario; su probabilidad es 1 menos la del suceso"), ("gráfico de barras", "gráfico con una barra por cada valor de X"), ("simétrica", "con forma igual a ambos lados del centro")],
  worked=[
      ("Un valor con la fórmula", "En 3 ensayos con p = 0,2, calcula P(X = 1).",
       ["C(3, 1) = 3, p¹ = 0,2 y q² = 0,8² = 0,64.", "P(X = 1) = 3 · 0,2 · 0,64 = 0,384."],
       "0,384"),
      ("Tabla y gráfico", "Con n = 5 y p = 1/2, construye la tabla de P(X = k) y calcula P(X ≥ 4).",
       ["Las combinaciones C(5, k) para k = 0 a 5 son 1, 5, 10, 10, 5, 1 y p⁵ = 1/32.", "Tabla: 1/32, 5/32, 10/32, 10/32, 5/32, 1/32.", "P(X ≥ 4) = 5/32 + 1/32 = 6/32 = 3/16."],
       "P(X ≥ 4) = 3/16"),
  ],
  mist=[
      ("Calcular P(X = 2) como p² sin el factor C(n, 2) ni qⁿ⁻².", "Se olvidan las maneras de ordenar los éxitos y los fracasos.", "Usa la fórmula completa C(n, k) · pᵏ · qⁿ⁻ᵏ."),
      ("Sumar P(X = 0) para «al menos uno».", "«Al menos uno» incluye todos los valores desde 1.", "Usa el complemento: 1 − P(X = 0)."),
  ],
  R=[ex("En Matemática: Calcula C(4, 2).", "6", "Hay 6 maneras de ubicar 2 éxitos entre 4 ensayos."),
     ex("Si p = 0,2, ¿cuánto vale q?", "0,8", "q = 1 − 0,2."),
     ex("En 2 ensayos con p = 1/2, ¿cuánto vale P(X = 0)?", "1/4", "Es q² = (1/2)².")],
  C=[ex("Con n = 4 y p = 1/2, calcula P(X = 2).", "3/8", "6 · (1/2)⁴ = 6/16."),
     ex("Con n = 4 y p = 0,3, calcula P(X = 0).", "0,2401", "0,7⁴ = 0,2401."),
     ex("¿Cuánto suman las probabilidades de todos los valores de una binomial?", "1", "Entre todos los valores cubren todas las posibilidades.")],
  A=[ex("En 3 ensayos con p = 1/2, ¿cuánto vale P(al menos un éxito)?", "7/8", "1 − P(X = 0) = 1 − 1/8."),
     ex("Se lanza 5 veces una moneda. ¿Cuál es la probabilidad de exactamente 3 caras?", "5/16", "C(5, 3) = 10 y 10 ÷ 32 = 5/16."),
     ex("Con n = 4 y p = 0,2, calcula P(X = 1).", "0,4096", "4 · 0,2 · 0,8³ = 4 · 0,2 · 0,512.")],
  Z=[ex("Tomás calculó P(X = 2) para n = 4 y p = 0,3 como 0,3² = 0,09. ¿Qué le falta a su cálculo? A) Solo el factor C(4, 2) B) El factor C(4, 2) y la probabilidad de los fracasos, 0,7²", "B", "Hay que contar las maneras de ubicar los éxitos y los fracasos."),
     ex("En una binomial con n = 6 y p = 1/2, ¿por qué P(X = 2) = P(X = 4)? A) Por simetría: éxito y fracaso son igual de probables B) Porque 2 + 4 = 6 y las probabilidades suman 1", "A", "C(6, 2) = C(6, 4) y p = q.")],
  D=[ex("Con n = 5 y p = 0,2, calcula P(X ≥ 1) (con tres decimales).", "0,672", "1 − 0,8⁵ = 1 − 0,32768."),
     ex("En una binomial con p = 1/2 se sabe que P(X = 0) = 1/32. ¿Cuánto vale n?", "5", "(1/2)ⁿ = 1/32 da n = 5.")],
  ctx=[ex("Un jugador de ejemplo acierta un penal con probabilidad 0,7. En 3 penales, ¿cuál es la probabilidad de que acierte exactamente 2?", "0,441", "3 · 0,7² · 0,3 = 3 · 0,49 · 0,3.")],
  chk=[ex("Con n = 6 y p = 1/2, calcula P(X = 3).", "5/16", "C(6, 3) = 20 y 20 ÷ 64 = 5/16."),
       ex("Para n = 5 y p = 1/2, ¿cuánto vale C(5, 4) + C(5, 5)?", "6", "5 + 1."),
       ex("¿Qué se usa para calcular «al menos uno»? A) La suma de P(X = 0) y P(X = 1) B) El complemento", "B", "P(X ≥ 1) = 1 − P(X = 0).")],
  op=("Una máquina de ejemplo fabrica piezas y cada una sale defectuosa con probabilidad 0,1, de forma independiente. En un lote de 4 piezas, X cuenta las defectuosas. Construye la tabla de P(X = k) para k = 0 a 4 con la fórmula, comprueba que suman 1 y dibuja el gráfico de barras. Responde: P(al menos una defectuosa) y qué valor de X es más probable.",
      "k = 0: 0,6561; k = 1: 0,2916; k = 2: 0,0486; k = 3: 0,0036; k = 4: 0,0001; suman 1. P(al menos una) = 1 − 0,6561 = 0,3439. El valor más probable es 0.",
      ["usa la fórmula completa en cada fila", "comprueba que las probabilidades suman 1", "usa el complemento para «al menos una»"],
      ["tabla de cinco filas", "gráfico de barras"],
      ["olvidar el factor C(n, k)", "sumar mal las filas"],
      "Si las filas no suman 1, pide que revise primero C(4, k) y luego las potencias."),
  reinforce="Calcula P(X = 1) y P(X = 3) para n = 3 y p = 1/2.",
  extend="Explica por qué la distribución binomial con p = 1/2 es simétrica y con p = 0,1 no lo es.",
)

# ================================================================ OAC 02 clase 3
chk((80 - 60) / 10 == 2 and (45 - 60) / 10 == -1.5 and (75 - 60) / 10 == 1.5 and round(1 - 0.93, 2) == 0.07 and round(0.93 - 0.5, 2) == 0.43)
chk((130 - 100) / 15 == 2 and (115 - 100) / 15 == 1 and round(0.84 - 0.5, 2) == 0.34 and round(1 - 0.84, 2) == 0.16 and round(1 - 0.98, 2) == 0.02)
chk((155 - 170) / 6 == -2.5 and 500 - 100 == 400 and 80 + (-2) * 4 == 72 and (140 - 120) / 10 == 2)
L(OA2, 3,
  use="Aprenderé a usar el modelo normal con su media, su desviación estándar y el puntaje z para calcular probabilidades. Sirve para decidir qué tan habitual o inusual es un valor.",
  prior=["Sé calcular media y desviación estándar.", "Sé interpretar un gráfico con forma de campana."],
  explain=[
      "La distribución normal tiene forma de campana simétrica alrededor de la media μ, y la desviación estándar σ indica qué tan ancha es. El área total bajo la curva es 1. Es un modelo continuo: la probabilidad de un valor exacto es 0 y solo tienen sentido las probabilidades de intervalos.",
      "La regla empírica dice que cerca del 68 % de los valores está entre μ − σ y μ + σ, cerca del 95 % entre μ − 2σ y μ + 2σ y cerca del 99,7 % entre μ − 3σ y μ + 3σ. El puntaje z, z = (x − μ) ÷ σ, indica a cuántas desviaciones estándar está x de la media, y permite usar una tabla de probabilidades acumuladas.",
      "En los ejercicios te damos los valores de tabla necesarios, redondeados a dos decimales: P(Z ≤ 1) = 0,84, P(Z ≤ 1,5) = 0,93 y P(Z ≤ 2) = 0,98. Por simetría, P(Z ≤ 0) = 0,5 y P(Z > a) = 1 − P(Z ≤ a). Dibuja siempre la campana y sombrea el área que buscas.",
  ],
  vocab=[("distribución normal", "modelo con forma de campana definido por μ y σ"), ("media", "centro de la distribución, representado por μ"), ("desviación estándar", "medida de dispersión, representada por σ"), ("puntaje z", "número de desviaciones estándar entre x y la media"), ("regla empírica", "regla 68 %, 95 % y 99,7 % para la distribución normal")],
  worked=[
      ("Calcular el puntaje z", "Los puntajes de un test de ejemplo siguen una normal con μ = 60 y σ = 10. Calcula el puntaje z de 80 y de 45.",
       ["z = (x − μ) ÷ σ.", "Para 80: (80 − 60) ÷ 10 = 2. Para 45: (45 − 60) ÷ 10 = −1,5."],
       "z = 2 y z = −1,5"),
      ("Usar la tabla", "Con μ = 60 y σ = 10 y sabiendo que P(Z ≤ 1,5) = 0,93, ¿cuánto vale P(X ≤ 75)?",
       ["Puntaje z de 75: (75 − 60) ÷ 10 = 1,5.", "P(X ≤ 75) = P(Z ≤ 1,5) = 0,93."],
       "0,93"),
  ],
  mist=[
      ("Calcular z como (μ − x) ÷ σ sin cuidar el signo.", "Un valor menor que la media debe tener z negativo.", "Usa z = (x − μ) ÷ σ."),
      ("Decir que P(X = 65) es el área de una barra.", "En una variable continua el valor exacto tiene probabilidad 0.", "Calcula probabilidades de intervalos."),
  ],
  R=[ex("¿Qué parte del área bajo la curva normal está bajo la media?", "50 %", "La curva es simétrica alrededor de μ."),
     ex("Con μ = 60 y σ = 10, ¿cuánto vale z para x = 70?", "1", "(70 − 60) ÷ 10."),
     ex("¿Qué porcentaje aproximado de los valores está entre μ − σ y μ + σ?", "68 %", "Es la regla empírica.")],
  C=[ex("Las estaturas de un grupo de ejemplo siguen una normal con μ = 170 cm y σ = 6 cm. ¿Qué porcentaje aproximado mide entre 164 y 176 cm?", "68 %", "Ese intervalo es μ ± σ."),
     ex("Con estaturas normales de μ = 170 cm y σ = 6 cm, ¿qué porcentaje aproximado mide entre 158 y 182 cm?", "95 %", "Ese intervalo es μ ± 2σ."),
     ex("En un grupo de ejemplo con estaturas normales de μ = 170 cm y σ = 6 cm, ¿cuánto vale z para 155 cm?", "−2,5", "(155 − 170) ÷ 6.")],
  A=[ex("Un test tiene μ = 100 y σ = 15. Con P(Z ≤ 2) = 0,98, ¿cuánto vale P(X ≤ 130)?", "0,98", "z = (130 − 100) ÷ 15 = 2."),
     ex("En un test normal con μ = 100 y σ = 15 y con P(Z ≤ 1) = 0,84, ¿cuánto vale P(100 < X < 115)?", "0,34", "z = 1 para 115 y 0,84 − 0,5."),
     ex("En un test normal con μ = 100 y σ = 15 y con P(Z ≤ 1) = 0,84, ¿cuánto vale P(X > 115)?", "0,16", "1 − P(Z ≤ 1) = 1 − 0,84.")],
  Z=[ex("En una variable normal, P(X ≤ 70) = 0,80. ¿Cuánto valen P(X < 70) y P(X > 70)?", "0,80 y 0,20", "Un valor exacto tiene probabilidad 0, así que P(X < 70) = 0,80; y P(X > 70) = 1 − 0,80."),
     ex("Dos grupos tienen la misma media, y sus desviaciones estándar son 5 y 15. ¿Cuál tiene la campana más ancha?", "El de desviación 15", "Mayor σ significa datos más dispersos.")],
  D=[ex("Una variable normal tiene μ = 500 y σ = 50. ¿Qué intervalo contiene aproximadamente el 95 % central?", "De 400 a 600", "μ ± 2σ es 500 ± 100."),
     ex("Un valor tiene z = −2 en una normal con μ = 80 y σ = 4. ¿Cuánto vale x?", "72", "x = μ + z · σ = 80 − 8.")],
  ctx=[ex("La duración de unas baterías de ejemplo sigue una normal con μ = 120 h y σ = 10 h. Con la regla empírica, ¿qué porcentaje aproximado dura más de 140 h?", "2,5 %", "140 h es μ + 2σ; fuera del 95 % central queda 5 % repartido en ambas colas.")],
  chk=[ex("Con μ = 50 y σ = 5, ¿cuánto vale z para x = 60?", "2", "(60 − 50) ÷ 5."),
       ex("¿Cuánto vale P(Z ≤ 0)?", "0,5", "La mitad del área está a cada lado de la media."),
       ex("¿Qué porcentaje aproximado de los valores está entre μ − 3σ y μ + 3σ?", "99,7 %", "Es la regla empírica.")],
  op=("Los tiempos de espera en una fila de ejemplo siguen una normal con μ = 12 min y σ = 3 min. Calcula el puntaje z de 18 min y de 9 min, el intervalo que contiene aproximadamente el 95 % de los tiempos y el porcentaje aproximado de personas que esperan más de 18 min. Dibuja la campana, marca μ, μ ± σ y μ ± 2σ y sombrea el área de la última pregunta.",
      "z(18) = 2 y z(9) = −1. Intervalo del 95 %: de 6 a 18 min. Más de 18 min es μ + 2σ, aproximadamente 2,5 %.",
      ["calcula bien los puntajes z", "usa la regla empírica para el 95 %", "dibuja y sombrea el área pedida"],
      ["dibujo de la campana", "cuatro respuestas calculadas"],
      ["invertir el signo de z", "confundir el 95 % central con el 95 % de un lado"],
      "Si confunde el área, pide que sombree primero y luego calcule."),
  reinforce="Calcula z para x = 40 en una normal con μ = 50 y σ = 4.",
  extend="Explica por qué en una normal la probabilidad de un valor exacto es 0 pero la de un intervalo no.",
)

# ================================================================ OAC 02 clase 4
chk(abs(math.sqrt(100 * 0.1 * 0.9) - 3) < 1e-9 and 100 * F(1, 10) == 10 and (22 - 10) / 3 == 4 and (62 - 50) / 5 == 2.4 and 400 * 0.5 == 200 and math.sqrt(400 * 0.25) == 10)
chk(F(11, 1024) == F(math.comb(10, 9) + math.comb(10, 10), 2 ** 10) and 5 + 2 * math.sqrt(20 * 0.25 * 0.75) > 8.8 and 5 + 2 * math.sqrt(3.75) < 9)
chk(math.sqrt(100 * 0.5 * 0.5) == 5 and math.sqrt(400 * 0.5 * 0.5) == 10 and 100 * 0.2 == 20 and math.sqrt(100 * 0.2 * 0.8) == 4 and 20 * 0.1 == 2)
L(OA2, 4,
  use="Aprenderé a usar el modelo normal como aproximación de la binomial y a decidir con argumentos si un resultado es inusual o si una conclusión de datos es creíble. Sirve para tomar decisiones con evidencia y sin exagerar lo que los datos muestran.",
  prior=["Conozco los modelos binomial y normal.", "Sé calcular z."],
  explain=[
      "Para una binomial X ~ B(n, p) la media es μ = n · p y la desviación estándar es σ = √(n · p · q). Cuando n es grande, la distribución de X se parece a una normal con esa media y esa desviación. Como regla práctica se pide n · p ≥ 5 y n · q ≥ 5; si no se cumple, la aproximación no es buena.",
      "Con la aproximación se puede decidir si un resultado es inusual: si el puntaje z de lo observado está más allá de 2 o −2, ocurre menos del 5 % de las veces si el modelo es correcto. Eso no demuestra que el modelo esté malo, pero es una señal para revisar, por ejemplo, si p cambió. Un valor dentro de ±2 se considera habitual.",
      "Las conclusiones dependen de cómo se obtuvieron los datos. Si la muestra no es aleatoria o la pregunta influye en la respuesta, el modelo binomial no aplica aunque las cuentas salgan. Al comunicar una decisión, indica los supuestos (independencia, p constante), el cálculo y el límite: la evidencia sugiere, no prueba.",
  ],
  vocab=[("aproximación normal", "uso de una curva normal en lugar de la binomial para n grande"), ("inusual", "que ocurre menos del 5 % de las veces según el modelo"), ("muestra aleatoria", "muestra elegida al azar, sin sesgo"), ("sesgo", "error que inclina los datos hacia un lado"), ("evidencia", "datos que apoyan o debilitan una conclusión")],
  worked=[
      ("Media y desviación", "Una moneda se lanza 100 veces. Calcula μ y σ de la cantidad de caras y el intervalo μ ± 2σ.",
       ["μ = 100 · 0,5 = 50.", "σ = √(100 · 0,5 · 0,5) = √25 = 5.", "μ ± 2σ va de 40 a 60."],
       "μ = 50, σ = 5; intervalo de 40 a 60"),
      ("Decidir si es inusual", "Una máquina de ejemplo produce 10 % de piezas defectuosas. En una caja de 100 aparecen 22 defectuosas. ¿Es un resultado habitual?",
       ["μ = 100 · 0,1 = 10 y σ = √(100 · 0,1 · 0,9) = 3.", "z = (22 − 10) ÷ 3 = 4, muy por encima de 2.", "Es muy inusual si p = 0,1; conviene revisar la máquina."],
       "Inusual: z = 4"),
  ],
  mist=[
      ("Concluir que el modelo es falso solo porque un valor tiene z = 2,1.", "Un valor inusual puede ocurrir por azar un 5 % de las veces.", "Úsalo como una señal para revisar y recopila más datos."),
      ("Aplicar el modelo a una muestra elegida por conveniencia.", "Una muestra sesgada no representa a la población.", "Revisa cómo se eligieron los datos antes de calcular."),
  ],
  R=[ex("Para n = 100 y p = 0,2, ¿cuánto vale la media μ?", "20", "100 · 0,2."),
     ex("Para n = 100 y p = 0,2, ¿cuánto vale la desviación estándar σ?", "4", "√(100 · 0,2 · 0,8) = √16."),
     ex("¿Es razonable aproximar con una normal la binomial con n = 20 y p = 0,1? A) Sí, porque n = 20 ya es grande B) No, porque n · p = 2 es menor que 5", "B", "Se pide n · p ≥ 5.")],
  C=[ex("Una moneda se lanza 400 veces. Calcula μ y σ de la cantidad de caras.", "μ = 200 y σ = 10", "400 · 0,5 = 200 y √(400 · 0,25) = 10."),
     ex("En 400 lanzamientos de una moneda, la cantidad de caras tiene μ = 200 y σ = 10. ¿Qué intervalo μ ± 2σ cubre aproximadamente el 95 % de los resultados?", "De 180 a 220", "200 ± 20."),
     ex("Si z = 1,2, ¿el resultado es habitual o inusual?", "Habitual", "Está dentro de ±2.")],
  A=[ex("Se lanza 100 veces una moneda de ejemplo y salen 62 caras (μ = 50 y σ = 5). ¿Cuánto vale z y es un resultado inusual?", "z = 2,4; es inusual", "(62 − 50) ÷ 5 = 2,4, mayor que 2."),
     ex("Un dado de ejemplo se lanza 60 veces, con p = 1/6 de sacar 6. ¿Cuántos seises se esperan?", "10", "60 · 1/6."),
     ex("Para n = 400 y p = 0,5, ¿cuánto vale z de un resultado de 190 éxitos?", "−1", "(190 − 200) ÷ 10.")],
  Z=[ex("Una encuesta se hizo solo a quienes responden en una red social. ¿Se puede generalizar con el modelo binomial? A) Sí, porque son muchos B) No, la muestra no es aleatoria", "B", "Un gran tamaño no corrige una muestra sesgada."),
     ex("Si n pasa de 100 a 400 con p = 0,5, ¿por cuánto se multiplica σ y por cuánto μ?", "σ por 2 y μ por 4", "σ pasa de 5 a 10 y μ de 50 a 200.")],
  D=[ex("Una prueba tiene 20 preguntas con 4 alternativas y se responde al azar (p = 0,25, μ = 5 y σ ≈ 1,94). ¿Desde cuántas respuestas correctas el puntaje queda sobre μ + 2σ?", "9 o más", "5 + 2 · 1,94 ≈ 8,9."),
     ex("En 10 lanzamientos de una moneda, ¿cuál es la probabilidad de 9 o más caras? Escríbela como fracción.", "11/1024", "Hay 10 maneras de 9 caras y 1 de 10 caras, sobre 2¹⁰ = 1.024.")],
  ctx=[ex("Una fábrica de ejemplo sabe que el 10 % de sus piezas sale defectuosa. En un lote de 100 revisa y encuentra 14 defectuosas (μ = 10 y σ = 3). ¿Cuánto vale z y es inusual?", "z ≈ 1,33; no es inusual", "(14 − 10) ÷ 3 ≈ 1,33, dentro de ±2.")],
  chk=[ex("¿Cuándo se considera inusual un valor en el modelo normal?", "Cuando z es mayor que 2 o menor que −2", "Ocurre menos del 5 % de las veces."),
       ex("Calcula μ para n = 50 y p = 0,4.", "20", "50 · 0,4."),
       ex("¿Qué debe tener una muestra para generalizar? A) Ser aleatoria y representativa B) Ser rápida de obtener", "A", "Sin aleatoriedad hay sesgo.")],
  op=("Una pastelería de ejemplo asegura que el 90 % de sus pedidos llega a tiempo. Un curso revisa 100 pedidos de un mes y encuentra que 82 llegaron a tiempo. Con la aproximación normal calcula μ y σ de los pedidos a tiempo, el valor z de 82 y decide si el resultado es inusual. Escribe tu conclusión con dos supuestos y un límite.",
      "μ = 100 · 0,9 = 90 y σ = √(100 · 0,9 · 0,1) = 3. z = (82 − 90) ÷ 3 ≈ −2,67, inusual. Supuestos: p constante e independencia entre pedidos. Límite: no se sabe si los 100 pedidos fueron elegidos al azar; el resultado sugiere revisar la afirmación pero no la prueba falsa.",
      ["calcula μ y σ con la fórmula", "interpreta z con el criterio ±2", "declara supuestos y límites"],
      ["cálculos de μ, σ y z", "conclusión escrita"],
      ["afirmar que la pastelería miente", "olvidar la condición de muestra aleatoria"],
      "Si concluye con certeza, pide que cambie el verbo por «los datos sugieren»."),
  reinforce="Calcula μ y σ para n = 200 y p = 0,5 y el intervalo μ ± 2σ (deja σ con una raíz).",
  extend="Explica por qué un resultado con |z| mayor que 2 no demuestra que el modelo esté equivocado.",
)
