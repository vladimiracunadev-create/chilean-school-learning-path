"""Cuaderno del estudiante de 4.º medio Matemática FG: OAC 01 (decisiones financieras con porcentajes, tasas e índices)."""
from __future__ import annotations

from fractions import Fraction as F

from fg_mate_common import L, chk, ex

OA1 = "FG-MATE-4M-OAC-01"

# ================================================================ OAC 01 clase 1
chk(50000 * F(6, 5) * F(4, 5) == 48000 and F(450000 - 400000, 400000) == F(1, 8) and F(105, 100) ** 2 == F(11025, 10000))
chk(120000 * F(3, 4) * F(9, 10) == 81000 and 500000 * F(11, 10) * F(9, 10) == 495000 and 25000 * F(119, 100) == 29750)
chk(F(8, 10) * F(9, 10) == F(72, 100) and 64000 / F(4, 5) == 80000 and 1 / F(5, 4) == F(4, 5) and 40000 * F(85, 100) + 3000 == 37000)
L(OA1, 1,
  use="Aprenderé a precisar sobre qué cantidad se calcula un porcentaje y a distinguir porcentajes, variaciones y puntos porcentuales. Sirve para entender bien una oferta, un descuento o un reajuste antes de decidir.",
  prior=["Sé calcular un porcentaje de una cantidad.", "Sé usar decimales y fracciones."],
  explain=[
      "Un porcentaje es una razón sobre 100 y siempre se calcula sobre una base. El 20 % de 80.000 es 0,20 · 80.000 = 16.000. Un aumento de p % equivale a multiplicar por (1 + p/100) y un descuento de p % equivale a multiplicar por (1 − p/100).",
      "La variación porcentual compara el valor nuevo con el inicial: variación = (nuevo − inicial) ÷ inicial · 100. Si un sueldo pasa de 400.000 a 450.000, la variación es 50.000 ÷ 400.000 = 12,5 %. Cuando hay varios cambios seguidos, los factores se multiplican; no se suman los porcentajes, porque cada uno se calcula sobre una base distinta.",
      "No hay que confundir porcentaje con puntos porcentuales. Si una tasa pasa de 4 % a 6 %, sube 2 puntos porcentuales, pero su variación relativa es 2 ÷ 4 = 50 %. En decisiones financieras siempre pregunta: ¿qué porcentaje es?, ¿de qué cantidad?, ¿antes o después de otros cambios?",
  ],
  vocab=[("base", "cantidad sobre la que se calcula el porcentaje"), ("variación porcentual", "cambio relativo entre un valor inicial y uno nuevo"), ("factor", "número por el que se multiplica, como 1,2 para un aumento de 20 %"), ("puntos porcentuales", "diferencia directa entre dos porcentajes"), ("descuento", "rebaja de un porcentaje del precio")],
  worked=[
      ("Cambios sucesivos", "Un artículo de $50.000 sube 20 % y después baja 20 %. ¿Cuánto cuesta al final y qué variación total hubo?",
       ["Después del aumento: 50.000 · 1,2 = 60.000.", "Después del descuento: 60.000 · 0,8 = 48.000.", "Variación: (48.000 − 50.000) ÷ 50.000 = −4 %."],
       "$48.000; variación total de −4 %"),
      ("Variación porcentual", "Un sueldo de ejemplo pasa de $400.000 a $450.000. ¿Cuál es la variación?",
       ["Diferencia: 450.000 − 400.000 = 50.000.", "Base: el valor inicial, 400.000. Variación: 50.000 ÷ 400.000 = 0,125."],
       "12,5 %"),
  ],
  mist=[
      ("Pensar que +20 % y −20 % se anulan y vuelven al valor inicial.", "El segundo porcentaje se calcula sobre un valor distinto.", "Multiplica los factores: 1,2 · 0,8 = 0,96, que es −4 %."),
      ("Decir que una tasa subió 2 % cuando pasó de 4 % a 6 %.", "Se confunden puntos porcentuales con variación relativa.", "Sube 2 puntos porcentuales, que es un 50 % de aumento relativo."),
  ],
  R=[ex("Calcula el 20 % de $80.000.", "$16.000", "0,20 · 80.000 = 16.000."),
     ex("Un valor pasa de 200 a 250. ¿Cuál es la variación porcentual?", "25 %", "50 ÷ 200 = 0,25."),
     ex("Un producto de $30.000 tiene 10 % de descuento. ¿Cuánto se paga?", "$27.000", "30.000 · 0,9 = 27.000.")],
  C=[ex("Un precio sube 5 % y luego otro 5 %. ¿Cuál es la variación total?", "10,25 %", "1,05 · 1,05 = 1,1025."),
     ex("Una tasa pasa de 8 % a 11 %. ¿Cuántos puntos porcentuales subió?", "3 puntos", "11 − 8 = 3."),
     ex("Un precio baja de $80.000 a $68.000. ¿Qué porcentaje de descuento tuvo?", "15 %", "12.000 ÷ 80.000 = 0,15.")],
  A=[ex("Una chaqueta de lista cuesta $120.000. Tiene 25 % de descuento y, sobre el precio ya rebajado, un cupón de 10 %. ¿Cuánto se paga?", "$81.000", "120.000 · 0,75 · 0,9 = 81.000."),
     ex("Un sueldo de $500.000 sube 10 % y después baja 10 %. ¿Cuánto es el sueldo final?", "$495.000", "500.000 · 1,1 · 0,9 = 495.000."),
     ex("Un producto neto cuesta $25.000 y se le agrega 19 % de IVA. ¿Cuál es el precio con IVA?", "$29.750", "25.000 · 1,19.")],
  Z=[ex("Una tienda ofrece 20 % de descuento y después 10 % adicional sobre el precio rebajado. ¿Cuál es el descuento total?", "28 %", "0,8 · 0,9 = 0,72, es decir, se paga el 72 %."),
     ex("Una tasa de ejemplo baja de 5 % a 4 %. ¿Cuántos puntos porcentuales bajó y cuánto bajó en términos relativos?", "1 punto; 20 %", "5 − 4 = 1 punto, y 1 ÷ 5 = 0,20 sobre la base de 5.")],
  D=[ex("Después de un descuento de 20 %, un producto cuesta $64.000. ¿Cuál era su precio original?", "$80.000", "64.000 ÷ 0,8 = 80.000."),
     ex("Un precio sube 25 %. ¿Qué porcentaje de descuento lo devuelve al valor original?", "20 %", "1 ÷ 1,25 = 0,8, así que debe bajar 20 %.")],
  ctx=[ex("Una mochila de ejemplo cuesta $40.000 y tiene 15 % de descuento. El despacho cuesta $3.000 adicionales y no tiene descuento. ¿Cuánto se paga en total?", "$37.000", "40.000 · 0,85 = 34.000 y 34.000 + 3.000 = 37.000.")],
  chk=[ex("Calcula el 15 % de $2.000.", "$300", "0,15 · 2.000."),
       ex("Un valor pasa de 100 a 130. ¿Cuál es la variación porcentual?", "30 %", "30 ÷ 100."),
       ex("Una tasa baja de 12 % a 9 %. ¿Cuántos puntos porcentuales bajó?", "3 puntos", "12 − 9 = 3.")],
  op=("Una tienda de ejemplo anuncia: «Todo con 30 % de descuento» y en caja ofrece «10 % extra con tarjeta de la tienda». Un televisor de lista cuesta $300.000 y un parlante $60.000. Calcula el precio final de cada uno con ambos descuentos, el descuento total en % y explica por qué no es 40 %.",
      "Televisor: 300.000 · 0,7 · 0,9 = 189.000. Parlante: 60.000 · 0,7 · 0,9 = 37.800. El descuento total es 1 − 0,63 = 37 %, no 40 %, porque el 10 % se calcula sobre el precio ya rebajado.",
      ["usa factores multiplicativos", "calcula el descuento total en % con la base correcta", "explica por qué no se suman"],
      ["dos precios finales", "explicación escrita"],
      ["sumar los porcentajes", "calcular el segundo descuento sobre el precio de lista"],
      "Si suma los porcentajes, pide que calcule el 10 % de cada precio ya rebajado y lo compare con el 10 % del precio de lista."),
  reinforce="Calcula el precio final de $90.000 con 10 % de descuento y luego 20 % de descuento adicional.",
  extend="Explica por qué un aumento de 50 % requiere una baja de aproximadamente 33,3 % para volver al valor inicial.",
)

# ================================================================ OAC 01 clase 2
chk(100000 * F(105, 100) ** 3 == F(1157625, 10) and 50000 * F(104, 100) ** 2 == 54080 and 1000000 * F(103, 100) ** 2 == 1060900)
chk(300000 * F(102, 100) ** 2 == 312120 and round((1.015 ** 12 - 1) * 100, 1) == 19.6 and round((1.01 ** 12 - 1) * 100, 1) == 12.7)
chk(100000 * F(112, 100) == 112000 and 100000 * F(1055, 1000) ** 2 == F(1113025, 10) and round(1.055 ** 4, 3) < 1.24 < round(1.055 ** 5, 3) - 0.06 + 0.06 and 1.055 ** 4 < 1.24 and 1.055 ** 5 > 1.30)
chk(1.1 ** 7 < 2 < 1.1 ** 8 and 100000 * F(103, 100) ** 2 == 106090)
L(OA1, 2,
  use="Aprenderé a representar un ahorro o una deuda con una tabla y con una fórmula, y a comparar interés simple e interés compuesto. Sirve para saber cuánto crece de verdad un dinero según la tasa y el tiempo.",
  prior=["Sé calcular porcentajes y factores.", "Sé usar potencias con calculadora."],
  explain=[
      "El interés simple se calcula siempre sobre el capital inicial C: I = C · i · n, donde i es la tasa por período y n el número de períodos. El monto final es M = C · (1 + i · n). Cada período se agrega la misma cantidad, por lo que el crecimiento es lineal.",
      "En el interés compuesto, el interés de cada período se suma al capital y el período siguiente se calcula sobre el nuevo capital: M = C · (1 + i)ⁿ. El crecimiento es exponencial. Una tabla año por año y la fórmula son dos representaciones de lo mismo: la tabla muestra el proceso y la fórmula permite saltar al período n.",
      "La tasa y el período deben coincidir: una tasa mensual se aplica por meses, una anual por años. Una tasa de 1 % mensual compuesta durante 12 meses equivale a una tasa anual efectiva de 1,01¹² − 1 ≈ 12,7 %, no exactamente 12 %. Comparar siempre en el mismo período es clave para decidir.",
  ],
  vocab=[("capital", "dinero inicial que se ahorra o se debe"), ("tasa de interés", "porcentaje que se paga o gana por período"), ("interés simple", "interés calculado siempre sobre el capital inicial"), ("interés compuesto", "interés que se calcula también sobre los intereses anteriores"), ("tasa efectiva", "tasa equivalente medida en otro período, por ejemplo anual")],
  worked=[
      ("Simple y compuesto", "Se depositan $100.000 al 5 % anual durante 3 años. Calcula el monto con interés simple y con interés compuesto.",
       ["Simple: 100.000 + 100.000 · 0,05 · 3 = 115.000.", "Compuesto: 100.000 · 1,05³ = 100.000 · 1,157625 = 115.762,5."],
       "Simple $115.000; compuesto $115.762,5"),
      ("Tasa efectiva", "Una tasa de 1,5 % mensual se compone durante 12 meses. ¿Cuál es la tasa anual efectiva?",
       ["Factor de 12 meses: 1,015¹² ≈ 1,1956.", "Tasa efectiva: 1,1956 − 1 ≈ 0,1956."],
       "Aproximadamente 19,6 % anual (no 18 %)"),
  ],
  mist=[
      ("Calcular el interés compuesto multiplicando C · i · n.", "Esa es la fórmula del interés simple.", "En el compuesto se eleva el factor: C · (1 + i)ⁿ."),
      ("Aplicar una tasa mensual con el tiempo en años.", "Tasa y tiempo deben estar en la misma unidad.", "Convierte los años a meses o la tasa a anual efectiva."),
  ],
  R=[ex("Calcula el interés simple de $200.000 al 2 % mensual durante 3 meses.", "$12.000", "200.000 · 0,02 · 3."),
     ex("Se depositan $100.000 al 10 % anual simple durante 1 año. ¿Cuánto es el monto?", "$110.000", "100.000 + 10.000."),
     ex("¿Cuál es el factor de una tasa de 1,5 % por período?", "1,015", "1 + 0,015.")],
  C=[ex("Se depositan $50.000 al 4 % anual compuesto durante 2 años. ¿Cuánto es el monto?", "$54.080", "50.000 · 1,04² = 50.000 · 1,0816."),
     ex("Un capital de $1.000.000 crece 3 % anual compuesto. ¿Cuánto vale al final del año 2?", "$1.060.900", "1.000.000 · 1,03² = 1.000.000 · 1,0609."),
     ex("Con la misma tasa y 10 años, ¿cuál crece más? A) Interés simple B) Interés compuesto", "B", "El compuesto cobra interés sobre intereses.")],
  A=[ex("Una deuda de $300.000 tiene 2 % mensual compuesto. ¿Cuánto se debe después de 2 meses si no se paga nada?", "$312.120", "300.000 · 1,02² = 300.000 · 1,0404."),
     ex("Se ahorran $200.000 al 6 % anual simple durante 5 años. ¿Cuánto es la ganancia por intereses?", "$60.000", "200.000 · 0,06 · 5."),
     ex("Una tasa de 1 % mensual compuesta durante 12 meses, ¿cuál es la tasa anual efectiva con un decimal?", "12,7 %", "1,01¹² ≈ 1,1268.")],
  Z=[ex("Raúl dice que 1 % mensual compuesto es exactamente 12 % anual. ¿Es correcto? A) Sí, porque 1 % por 12 meses es 12 % B) No, es aproximadamente 12,7 %", "B", "Con interés compuesto el factor anual es 1,01¹², mayor que 1,12."),
     ex("Un banco ofrece 6 % anual simple y otro 5,5 % anual compuesto. Con $100.000 durante 2 años, ¿cuál rinde más y por cuánto aproximadamente?", "El simple, por unos $698", "112.000 contra 111.302,5; la diferencia es 697,5.")],
  D=[ex("Con 6 % anual simple y 5,5 % anual compuesto, ¿a partir de cuántos años el compuesto supera al simple?", "5 años", "En 4 años: 1,2388 contra 1,24; en 5 años: 1,3070 contra 1,30."),
     ex("Con interés compuesto de 10 % anual, ¿cuántos años enteros se necesitan para duplicar un capital?", "8 años", "1,1⁷ ≈ 1,95 y 1,1⁸ ≈ 2,14.")],
  ctx=[ex("Una deuda de tarjeta de ejemplo es de $100.000 y tiene 3 % mensual compuesto. Si no se paga, ¿cuánto se debe después de 2 meses?", "$106.090", "100.000 · 1,03² = 100.000 · 1,0609.")],
  chk=[ex("¿Qué tipo de interés crece de forma exponencial? A) Compuesto B) Simple", "A", "Cada período se calcula sobre un capital mayor."),
       ex("Calcula el monto de $10.000 al 10 % anual simple durante 3 años.", "$13.000", "10.000 + 10.000 · 0,1 · 3."),
       ex("¿Se puede aplicar una tasa mensual directamente a un tiempo en años?", "No", "Tasa y tiempo deben estar en la misma unidad.")],
  op=("Dos instituciones de ejemplo ofrecen un ahorro de $500.000 por 4 años. La institución A paga 3,2 % anual simple. La institución B paga 3 % anual compuesto. Haz una tabla año por año con el monto de cada una, escribe las fórmulas y decide cuál rinde más a los 4 años. Indica una condición que haría cambiar tu decisión.",
      "A: 500.000 · (1 + 0,032 · 4) = 564.000. B: 500.000 · 1,03⁴ = 562.754,4 aprox. A rinde más. La decisión cambiaría si el plazo fuera mucho más largo, porque el compuesto crece más rápido, o si hubiera comisiones.",
      ["completa la tabla con ambas fórmulas", "compara los montos finales", "indica una condición que cambia la decisión"],
      ["tabla de 4 años", "decisión justificada"],
      ["mezclar fórmulas simple y compuesta", "olvidar comisiones o plazo"],
      "Si los montos no coinciden con la tabla, pide que calcule año por año y compare con la fórmula."),
  reinforce="Calcula el monto de $80.000 al 5 % anual compuesto en 2 años y al 5 % anual simple en 2 años.",
  extend="Explica por qué dos tasas de 1 % mensual y 12 % anual no son equivalentes con interés compuesto.",
)

# ================================================================ OAC 01 clase 3
chk(500000 * F(104, 100) == 520000 and round((F(104, 106) - 1) * 100, 1) == F(-19, 10) and 800000 * F(103, 100) == 824000)
chk(round((F(103, 105) - 1) * 100, 1) == F(-19, 10) and 2000 * F(150, 100) == 3000 and 11000 / F(110, 100) == 10000)
chk(F(110, 100) * F(110, 100) == F(121, 100) and round(F(20, 120) * 100, 1) == F(167, 10) and round((F(108, 105) - 1) * 100, 1) == F(29, 10) and 500000 * F(115, 100) == 575000)
chk(350000 * F(1042, 1000) == 364700 and 300000 * F(103, 100) == 309000 and 200000 * F(103, 100) == 206000)
L(OA1, 3,
  use="Aprenderé a leer un índice económico, a calcular la inflación y a comparar un reajuste con el poder adquisitivo. Sirve para saber si un sueldo o un arriendo realmente alcanza para comprar lo mismo.",
  prior=["Sé calcular variaciones porcentuales.", "Sé usar factores multiplicativos."],
  explain=[
      "Un índice es un número que muestra cómo cambia una cantidad respecto de un período base, al que se le asigna el valor 100. Un índice de precios al consumidor (IPC) sigue el precio de una canasta de bienes. Si pasa de 100 a 104, los precios subieron 4 %. La inflación es la variación porcentual del índice de precios: (I_nuevo − I_inicial) ÷ I_inicial · 100.",
      "Un reajuste de sueldo, arriendo o cuota ligado a un índice multiplica el valor por el factor del índice. Pero lo que importa para vivir es el poder adquisitivo: cuántos bienes alcanzo a comprar. Si el sueldo sube 4 % y los precios suben 6 %, el sueldo real cambia por el factor 1,04 ÷ 1,06 ≈ 0,981, es decir, baja 1,9 %.",
      "Para convertir un valor nominal (en pesos de hoy) a pesos de la base, se divide entre el índice dividido por 100: 11.000 con índice 110 equivale a 10.000 en pesos base. No se restan los porcentajes ni se suman las inflaciones de varios años: los factores se multiplican.",
  ],
  vocab=[("índice", "número que compara un valor con el de un período base igual a 100"), ("inflación", "alza general y sostenida de los precios"), ("poder adquisitivo", "cantidad de bienes que se pueden comprar con un ingreso"), ("valor nominal", "valor en pesos del momento"), ("reajuste", "cambio de un valor según un índice o un porcentaje")],
  worked=[
      ("Inflación y reajuste", "Un índice de precios de ejemplo pasa de 100 a 104 en un año. Calcula la inflación y el reajuste de un sueldo de $500.000 igual a ese índice.",
       ["Inflación: (104 − 100) ÷ 100 = 4 %.", "Sueldo reajustado: 500.000 · 1,04 = 520.000."],
       "Inflación 4 %; sueldo $520.000"),
      ("Poder adquisitivo", "Un sueldo de $600.000 sube 4 % y los precios suben 6 %. ¿Cómo cambia el poder adquisitivo?",
       ["Nuevo sueldo: 600.000 · 1,04 = 624.000.", "Cambio real: 1,04 ÷ 1,06 ≈ 0,981."],
       "Baja alrededor de 1,9 %"),
  ],
  mist=[
      ("Restar los porcentajes: sueldo +4 % y precios +6 % da −2 %.", "El cambio real es un cociente de factores, no una resta.", "Calcula 1,04 ÷ 1,06 ≈ 0,981, que es −1,9 %."),
      ("Sumar inflaciones de dos años (5 % + 5 % = 10 %).", "Los factores se multiplican.", "Calcula 1,05 · 1,05 = 1,1025, es decir, 10,25 %."),
  ],
  R=[ex("Un índice base 100 sube a 108. ¿Cuál es la inflación?", "8 %", "(108 − 100) ÷ 100."),
     ex("Un sueldo de $400.000 se reajusta 5 %. ¿Cuánto es el nuevo sueldo?", "$420.000", "400.000 · 1,05."),
     ex("Un arriendo de $200.000 se reajusta 3 %. ¿Cuánto es el nuevo arriendo?", "$206.000", "200.000 · 1,03.")],
  C=[ex("Un índice pasa de 125 a 130. ¿Cuál es la variación porcentual?", "4 %", "5 ÷ 125 = 0,04."),
     ex("Un arriendo de $300.000 se reajusta según un índice que subió 3 %. ¿Cuánto es el nuevo arriendo?", "$309.000", "300.000 · 1,03."),
     ex("Si el sueldo sube menos que el índice de precios, ¿el poder adquisitivo sube o baja?", "Baja", "Con el mismo sueldo se compra menos.")],
  A=[ex("Un sueldo de $800.000 sube 3 % y los precios suben 5 %. ¿Cuál es el cambio real del poder adquisitivo, con un decimal?", "−1,9 %", "1,03 ÷ 1,05 ≈ 0,981."),
     ex("Un producto cuesta $2.000 con índice 100. Si el producto sigue al índice y este llega a 150, ¿cuánto cuesta?", "$3.000", "2.000 · 1,5."),
     ex("Un producto cuesta $11.000 hoy, con índice 110 respecto de una base 100. ¿Cuánto equivale en pesos base?", "$10.000", "11.000 ÷ 1,10.")],
  Z=[ex("Un índice sube 10 % el primer año y 10 % el segundo. ¿Cuál es la variación total desde la base?", "21 %", "1,1 · 1,1 = 1,21."),
     ex("Un índice sube de 100 a 120 y luego baja de 120 a 100. ¿Qué porcentaje bajó en la segunda etapa, con un decimal?", "16,7 %", "20 ÷ 120 ≈ 0,167.")],
  D=[ex("Un sueldo sube 8 % y la inflación es 5 %. ¿Cuál es la variación real del poder adquisitivo, con un decimal?", "2,9 %", "1,08 ÷ 1,05 ≈ 1,029."),
     ex("Un sueldo era de $500.000 cuando el índice valía 100 y ahora el índice vale 115. ¿Cuánto debería ser el sueldo para mantener el poder adquisitivo?", "$575.000", "500.000 · 1,15.")],
  ctx=[ex("Un arriendo de ejemplo es de $350.000 y se reajusta con un índice que subió 4,2 % en el año. ¿Cuánto es el nuevo arriendo?", "$364.700", "350.000 · 1,042.")],
  chk=[ex("Si un índice vale 100 en la base, ¿qué significa que hoy valga 120?", "Los precios subieron 20 % desde la base", "120 respecto de 100 es un aumento de 20 %."),
       ex("Un sueldo sube 5 % y los precios suben 5 %. ¿Cambia el poder adquisitivo?", "No", "El cociente de factores es 1."),
       ex("¿Se suman las inflaciones de varios años para obtener la total?", "No, se multiplican los factores", "Cada año se calcula sobre un valor distinto.")],
  op=("Un trabajador de ejemplo ganaba $700.000. Durante tres años consecutivos su sueldo se reajustó 3 %, 4 % y 2 %, y la inflación de esos años fue 4 %, 5 % y 3 %. Calcula el sueldo final, la inflación acumulada, el sueldo que mantendría el poder adquisitivo y el cambio real. Escribe una conclusión en una frase.",
      "Sueldo final: 700.000 · 1,03 · 1,04 · 1,02 = aproximadamente 764.837. Inflación acumulada: 1,04 · 1,05 · 1,03 = 1,12476, es decir 12,5 %. Sueldo para mantener poder: 700.000 · 1,12476 = 787.332 aprox. Cambio real: 1,0927 ÷ 1,12476 ≈ 0,971, baja 2,9 %. Conclusión: el sueldo creció menos que los precios.",
      ["multiplica los factores en lugar de sumar", "calcula el cambio real con un cociente", "concluye con una frase clara"],
      ["tres cálculos con factores", "conclusión escrita"],
      ["sumar los porcentajes", "restar los porcentajes para el cambio real"],
      "Si suma porcentajes, pide que construya una tabla año por año con el valor al final de cada año."),
  reinforce="Calcula el poder adquisitivo cuando un sueldo sube 6 % y la inflación es 4 %.",
  extend="Explica por qué un reajuste igual a la inflación mantiene el poder adquisitivo pero no lo mejora.",
)

# ================================================================ OAC 01 clase 4
chk(12 * 54000 + 10000 == 658000 and 18 * 38000 == 684000 and 12 * 54000 + 40000 == 688000 and 10 * 25000 + 5000 == 255000)
chk(6 * 55000 - 300000 == 30000 and 12 * 30000 == 360000 and 18 * 22000 == 396000 and 10 * 56000 == 560000 and 12 * 47000 + 15000 == 579000)
chk(36 * 20000 == 720000 and 15 * 25000 == 375000 and 12 * 30000 + 15000 == 375000 and F(15, 100) * 400000 == 60000 and 6 * 160000 == 960000 and 75000 * 12 == 900000)
chk(round(1000000 * 1.04 ** 5 - 1000000) == 216653 and 1000000 * 0.043 * 5 == 215000 and 120000 * F(108, 100) / 12 == 10800 and 120000 * F(110, 100) / 12 == 11000)
L(OA1, 4,
  use="Aprenderé a justificar una decisión financiera comparando el costo total de dos alternativas y revisando qué pasa si cambian los datos. Sirve para elegir con argumentos, sin dejarme llevar solo por la cuota más baja.",
  prior=["Sé calcular montos con porcentajes, tasas e índices.", "Sé comparar cantidades con una tabla."],
  explain=[
      "Para comparar dos alternativas de pago o ahorro se calcula el costo total: la suma de todas las cuotas más comisiones y otros cargos. Una cuota baja con muchas cuotas puede costar más en total que una cuota alta con pocas. El recargo es el costo total menos lo pedido, y se puede expresar como porcentaje de lo pedido.",
      "La decisión no depende solo del costo total. También cuenta si la cuota cabe en el presupuesto (por ejemplo, una regla de ejemplo es que la cuota no supere el 15 % del ingreso), el plazo y el riesgo. Una buena justificación escribe el cálculo, la regla de decisión, los supuestos y qué cambiaría la conclusión.",
      "El análisis de sensibilidad revisa cómo cambia la decisión si varía un dato, como una comisión o una tasa. Este cuaderno usa casos ficticios y no es asesoría financiera: antes de una decisión real hay que leer las condiciones y preguntar a una persona adulta de confianza o a la institución.",
  ],
  vocab=[("costo total", "suma de todas las cuotas, comisiones y cargos"), ("recargo", "costo total menos el monto pedido"), ("plazo", "tiempo en que se paga o se ahorra"), ("sensibilidad", "cuánto cambia una decisión si cambia un dato"), ("presupuesto", "ingresos y gastos previstos de una persona o grupo")],
  worked=[
      ("Comparar costos totales", "Crédito A: 12 cuotas de $54.000 más una comisión de $10.000. Crédito B: 18 cuotas de $38.000 sin comisión. ¿Cuál cuesta menos en total?",
       ["Costo de A: 12 · 54.000 + 10.000 = 648.000 + 10.000 = 658.000.", "Costo de B: 18 · 38.000 = 684.000.", "A cuesta $26.000 menos, aunque su cuota mensual es más alta."],
       "A: $658.000 contra $684.000 de B"),
      ("Sensibilidad", "Si la comisión del crédito A sube a $40.000, ¿cambia la decisión por costo total?",
       ["Nuevo costo de A: 648.000 + 40.000 = 688.000.", "Ahora B cuesta 684.000, que es menos."],
       "Sí; con esa comisión B resulta más barato"),
  ],
  mist=[
      ("Elegir la alternativa con la cuota más baja sin mirar el total.", "Una cuota baja puede venir con más cuotas y más costo.", "Calcula cuota × número de cuotas más comisiones."),
      ("Olvidar la comisión al comparar.", "La comisión forma parte del costo.", "Súmala al total de cada alternativa."),
  ],
  R=[ex("Un crédito tiene 10 cuotas de $25.000 y una comisión de $5.000. ¿Cuál es el costo total?", "$255.000", "10 · 25.000 + 5.000."),
     ex("Se pidieron $200.000 y se pagarán $255.000 en total. ¿Cuánto es el recargo?", "$55.000", "255.000 − 200.000."),
     ex("¿Cuánto se paga en 6 cuotas de $18.500?", "$111.000", "6 · 18.500.")],
  C=[ex("Se piden $300.000 y se pagan 6 cuotas de $55.000. ¿Qué porcentaje del monto pedido es el recargo?", "10 %", "Se pagan 330.000, el recargo es 30.000 y 30.000 ÷ 300.000 = 0,10."),
     ex("Se ahorran $40.000 al mes durante 12 meses sin interés. ¿Cuánto se junta?", "$480.000", "12 · 40.000."),
     ex("La alternativa 1 tiene 12 cuotas de $30.000 y la alternativa 2 tiene 18 cuotas de $22.000. ¿Cuál tiene menor costo total?", "La alternativa 1", "1: 360.000; 2: 396.000.")],
  A=[ex("La alternativa X tiene 10 cuotas de $56.000 sin comisión. La alternativa Y tiene 12 cuotas de $47.000 y una comisión de $15.000. ¿Cuál es el costo total de cada una?", "X $560.000; Y $579.000", "X: 10 · 56.000. Y: 12 · 47.000 + 15.000 = 564.000 + 15.000."),
     ex("Con un ingreso mensual de $400.000 y la regla de ejemplo «cuota de hasta 15 % del ingreso», ¿cuál es la cuota máxima?", "$60.000", "0,15 · 400.000."),
     ex("Con la misma regla y un ingreso de $250.000, ¿cumple una cuota de $35.000?", "Sí", "El máximo es 0,15 · 250.000 = 37.500 y 35.000 no lo supera.")],
  Z=[ex("Un aviso destaca «cuotas de solo $20.000» por un préstamo de $400.000 en 36 cuotas. ¿Cuánto se paga en total?", "$720.000", "36 · 20.000."),
     ex("La alternativa A tiene 12 cuotas de $30.000 más una comisión c y la alternativa B tiene 15 cuotas de $25.000. ¿Para qué comisión c los costos totales son iguales?", "$15.000", "12 · 30.000 + c = 375.000 da c = 15.000.")],
  D=[ex("Con $1.000.000 durante 5 años, el banco 1 paga 4 % anual compuesto y el banco 2 paga 4,3 % anual simple. ¿Cuál entrega más intereses y por cuánto aproximadamente?", "El banco 1, por unos $1.653", "1.000.000 · 1,04⁵ − 1.000.000 ≈ 216.653 y el simple da 215.000."),
     ex("Un crédito de $120.000 se paga en 12 cuotas iguales con un recargo total de 8 %. Si el recargo sube a 10 %, ¿cuánto sube la cuota?", "$200", "Con 8 %: 129.600 ÷ 12 = 10.800. Con 10 %: 132.000 ÷ 12 = 11.000.")],
  ctx=[ex("Un comité de vecinos de ejemplo quiere comprar un equipo de $900.000. La opción 1 es pagar 6 cuotas de $160.000. La opción 2 es ahorrar $75.000 al mes durante 12 meses y comprar sin interés. ¿Cuál cuesta menos en total?", "La opción 2: $900.000 contra $960.000", "6 · 160.000 = 960.000 y 12 · 75.000 = 900.000, aunque la opción 2 tarda más.")],
  chk=[ex("¿Qué se debe comparar además de la cuota?", "El costo total, el plazo y el presupuesto", "La cuota sola no muestra el costo ni si cabe en el presupuesto."),
       ex("Calcula 8 cuotas de $12.500 más una comisión de $2.000.", "$102.000", "8 · 12.500 = 100.000 y se suman 2.000."),
       ex("¿Qué hace un análisis de sensibilidad?", "Revisa si la decisión cambia al variar un dato", "Prueba, por ejemplo, otra comisión o tasa.")],
  op=("Un curso de ejemplo recauda fondos para un paseo de $1.200.000. Opción 1: un préstamo en 10 cuotas de $135.000 con una comisión de $20.000. Opción 2: un préstamo en 16 cuotas de $90.000 sin comisión. El curso puede pagar hasta $140.000 al mes. Calcula el costo total de cada opción, revisa la regla de cuota máxima, escribe una decisión y una sensibilidad (¿qué comisión de la opción 1 invierte la decisión?). Recuerda que es un caso de ejemplo y no asesoría financiera.",
      "Opción 1: 10 · 135.000 + 20.000 = 1.370.000. Opción 2: 16 · 90.000 = 1.440.000. Ambas cuotas caben en 140.000. La opción 1 cuesta $70.000 menos. La decisión se invierte si la comisión de la opción 1 supera 90.000, porque 1.350.000 + c > 1.440.000 cuando c > 90.000.",
      ["calcula ambos costos totales", "revisa la restricción de presupuesto", "indica una sensibilidad con un cálculo"],
      ["tabla comparativa", "decisión con supuestos"],
      ["comparar solo la cuota", "olvidar la comisión"],
      "Si omite la sensibilidad, pide que cambie un dato y recalcule el total de cada opción."),
  reinforce="Calcula el costo total de 9 cuotas de $22.000 más una comisión de $8.000.",
  extend="Explica por qué, con la misma cuota, un plazo más largo suele costar más en total.",
)
