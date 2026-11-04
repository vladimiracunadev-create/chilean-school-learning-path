"""Cuaderno del estudiante de 1.º medio Matemática, OA 14 (reglas aditiva y multiplicativa de probabilidad): clases 1 a 4."""
from __future__ import annotations

from fractions import Fraction as F

from student_content_ma_m1_b import L
from student_lessons import arith, ex

OA14 = "MA1M OA 14"


def fr(value) -> str:
    """Fracción irreductible como texto: 3/10; un entero se escribe sin denominador."""
    return str(F(value))


FRAC = " Responde como fracción irreductible."

# ================================================================ OA 14 · clase 1
L(OA14, 1,
  use="Aprenderé a escribir todos los resultados posibles de un experimento aleatorio, a organizarlos en una tabla o en un árbol y a calcular probabilidades contando casos favorables y posibles.",
  prior=["Sé que la probabilidad de un evento con resultados igualmente probables es casos favorables dividido por casos posibles.", "Sé simplificar fracciones."],
  explain=[
      "Un experimento aleatorio es uno cuyo resultado no se puede saber con seguridad antes de hacerlo, como lanzar un dado. El espacio muestral es la lista de todos los resultados posibles, por ejemplo {1, 2, 3, 4, 5, 6}. Un evento es un conjunto de resultados que nos interesa, como «sale par» = {2, 4, 6}.",
      "Si todos los resultados son igualmente probables, la probabilidad de un evento es los casos favorables divididos por los casos posibles. Va de 0 (imposible) a 1 (seguro). La probabilidad de que un evento no ocurra es 1 menos la probabilidad de que ocurra; se llama complemento. Si P(lluvia) = 2/5, entonces P(no lluvia) = 1 − 2/5 = 3/5.",
      "Cuando el experimento tiene dos etapas, como lanzar una moneda y un dado, conviene listar los resultados con una tabla de doble entrada o con un árbol: cada rama es un resultado de la primera etapa y de ella salen las ramas de la segunda. Así no se olvida ningún resultado ni se cuenta dos veces. Cuidado: «0, 1 o 2 caras» no son resultados igualmente probables en dos monedas.",
  ],
  vocab=[("espacio muestral", "lista de todos los resultados posibles de un experimento"), ("evento", "conjunto de resultados que nos interesa"), ("casos favorables", "resultados del espacio muestral que cumplen el evento"), ("complemento", "evento «no ocurre»; su probabilidad es 1 menos la del evento")],
  worked=[
      ("Dos monedas", "Se lanzan dos monedas. Escribe el espacio muestral y calcula la probabilidad de obtener exactamente una cara.",
       ["Resultados, en orden de primera y segunda moneda: CC, CS, SC, SS (C es cara y S es sello). Son 4 posibles e igualmente probables.", "Con exactamente una cara: CS y SC, o sea 2 favorables.", "P = 2 ÷ 4 = 1/2."], "P(exactamente una cara) = 1/2"),
      ("Moneda y dado", "Se lanza una moneda y un dado. ¿Cuál es la probabilidad de obtener cara y un número par?",
       ["El espacio muestral tiene 2 × 6 = 12 resultados, como C1, C2, …, S6.", "Favorables: C2, C4 y C6, o sea 3.", "P = 3 ÷ 12 = 1/4."], "P(cara y par) = 1/4"),
  ],
  mist=[
      ("Decir que al lanzar dos monedas hay 3 resultados: 0, 1 o 2 caras, y que cada uno tiene probabilidad 1/3.", "Los tres no son igualmente probables: «una cara» ocurre de dos formas, CS y SC.", "Lista los resultados por orden de moneda: CC, CS, SC, SS."),
      ("Dar una probabilidad mayor que 1, como 7/5.", "Los favorables nunca superan a los posibles; la probabilidad está entre 0 y 1.", "Revisa que el numerador sea menor o igual que el denominador."),
  ],
  R=[ex("Una bolsa tiene 3 fichas rojas y 5 azules. Se saca una al azar. ¿Cuál es la probabilidad de que sea roja?" + FRAC, fr(F(3, 8)), "Hay 3 favorables de 8 posibles."),
     ex("¿Cuántos resultados posibles tiene el lanzamiento de un dado de seis caras?", "6", "El espacio muestral es {1, 2, 3, 4, 5, 6}."),
     ex("Se lanza un dado de seis caras. ¿Cuál es la probabilidad de obtener un número par?" + FRAC, fr(F(3, 6)), "Los favorables son 2, 4 y 6, o sea 3 de 6.")],
  C=[arith("Se lanzan dos dados de seis caras, uno rojo y uno azul, y se anota el par (rojo, azul). ¿Cuántos pares distintos hay?", "6*6", "Cada resultado del primer dado se combina con los 6 del segundo.", " pares"),
     ex("Se lanzan un dado rojo y uno azul. Los pares que suman 7 son (1, 6), (2, 5), (3, 4), (4, 3), (5, 2) y (6, 1). ¿Cuál es la probabilidad de que sumen 7?" + FRAC, fr(F(6, 36)), "Hay 6 favorables de 36 posibles, y 6/36 se simplifica a 1/6."),
     ex("La probabilidad de que mañana llueva es 2/5. ¿Cuál es la probabilidad de que no llueva?" + FRAC, fr(1 - F(2, 5)), "Es el complemento: 1 − 2/5 = 3/5.")],
  A=[ex("Una ruleta tiene 8 sectores iguales numerados del 1 al 8. Se hace girar. ¿Cuál es la probabilidad de caer en un múltiplo de 3?" + FRAC, fr(F(2, 8)), "Los múltiplos de 3 son 3 y 6, o sea 2 de 8."),
     ex("Se lanzan un dado rojo y uno azul. Los pares que suman 8 son (2, 6), (3, 5), (4, 4), (5, 3) y (6, 2). ¿Cuál es la probabilidad de que sumen 8?" + FRAC, fr(F(5, 36)), "Hay 5 favorables de 36 posibles y la fracción ya no se simplifica."),
     ex("Se lanza una moneda y gira una ruleta con tres sectores iguales: rojo, verde y amarillo. ¿Cuál es la probabilidad de obtener cara y que la ruleta no caiga en amarillo?" + FRAC, fr(F(2, 6)), "El espacio muestral tiene 6 resultados; favorables: cara-rojo y cara-verde, o sea 2.")],
  Z=[ex("Julia dice: «Al lanzar dos dados la suma puede ser 2, 3, …, 12, o sea 11 resultados, así que la probabilidad de sumar 7 es 1/11». ¿Tiene razón? Responde sí o no.", "No", "Las 11 sumas no son igualmente probables: sumar 7 ocurre de 6 formas entre los 36 pares posibles, o sea 1/6."),
     ex("Daniel dice que la probabilidad de sacar una ficha roja de una bolsa con 3 rojas y 5 azules es 1/2 porque «o sale roja o no sale». ¿Tiene razón? Responde sí o no.", "No", "Los dos resultados no son igualmente probables: hay más fichas azules que rojas.")],
  D=[ex("Una bolsa tiene 12 fichas: 5 rojas, 4 azules y el resto verdes. Se saca una al azar. ¿Cuál es la probabilidad de que no sea verde?" + FRAC, fr(F(9, 12)), "Hay 12 − 5 − 4 = 3 verdes, así que no verdes son 9 de 12, que es 3/4."),
     ex("Una bolsa tiene 3 fichas rojas y 5 azules. ¿Cuántas fichas rojas hay que agregar para que la probabilidad de sacar una roja sea 1/2?", "2", "Con 2 más hay 5 rojas de 10 fichas, que es 1/2.")],
  ctx=[ex("En un curso de 30 estudiantes, 12 llegan en bicicleta. Se elige a un estudiante al azar para una encuesta. ¿Cuál es la probabilidad de que llegue en bicicleta?" + FRAC, fr(F(12, 30)), "Hay 12 favorables de 30 posibles y 12/30 se simplifica a 2/5.")],
  chk=[ex("En probabilidad, ¿qué es el espacio muestral?", "La lista de todos los resultados posibles", "Es el conjunto de resultados del experimento."),
       ex("Una probabilidad se calcula como 3/2. ¿Puede estar bien? Responde sí o no.", "No", "Una probabilidad no supera 1."),
       ex("P(que un día sea lunes al elegir al azar un día de la semana) = 1/7. ¿Cuál es la probabilidad de que no sea lunes?" + FRAC, fr(1 - F(1, 7)), "Es el complemento: 1 − 1/7 = 6/7.")],
  op=("Escribe en tu cuaderno los 12 resultados de lanzar una moneda (C o S) y un dado (1 al 6), ordenados en una tabla de doble entrada. Calcula la probabilidad de «sello y un número mayor que 4» y la de «sale el 1, sea cara o sello». Si tienes moneda y dado, lánzalos 24 veces y anota cuántas veces salió «sello y mayor que 4»; si no los tienes, haz solo la parte escrita.",
      "Los 12 resultados son C1 a C6 y S1 a S6. «Sello y mayor que 4»: S5 y S6, o sea 2 de 12, que es 1/6. «El 1 con cara o sello»: C1 y S1, o sea 2 de 12, que es 1/6.",
      ["tabla con los 12 resultados", "cuenta bien los favorables", "simplifica las fracciones", "verifica que ninguna probabilidad sea mayor que 1"],
      ["tabla completa", "dos probabilidades calculadas", "registro de lanzamientos si tenía materiales"],
      ["olvidar algún resultado", "contar «dos caras» como un solo resultado", "no simplificar la fracción"],
      "Pide que explique por qué hay 12 resultados. Reconoce que haya contado los favorables sobre la tabla."),
  reinforce="Escribe el espacio muestral de lanzar tres monedas (8 resultados) y calcula la probabilidad de tres caras.",
  extend="Explica con tus palabras por qué la probabilidad de un evento y la de su complemento suman 1.")

# ================================================================ OA 14 · clase 2
L(OA14, 2,
  use="Aprenderé la regla aditiva: cómo calcular la probabilidad de que ocurra un evento «o» otro, tanto cuando no pueden ocurrir a la vez como cuando sí.",
  prior=["Sé calcular probabilidades contando casos favorables y posibles.", "Sé sumar y restar fracciones con igual y distinto denominador."],
  explain=[
      "La regla aditiva se usa cuando se pregunta por A o B. Si A y B no pueden ocurrir a la vez, se llaman eventos incompatibles y la probabilidad es la suma: P(A o B) = P(A) + P(B). Ejemplo: en un dado, «sale 1» y «sale 2» no pueden ocurrir juntos, así que P(1 o 2) = 1/6 + 1/6 = 2/6 = 1/3.",
      "Si A y B sí pueden ocurrir a la vez, hay resultados que están en los dos eventos. Al sumar se contarían dos veces, así que se resta una vez la probabilidad de que ocurran juntos: P(A o B) = P(A) + P(B) − P(A y B). Ejemplo: en un dado, «par» = {2, 4, 6} y «mayor que 4» = {5, 6} comparten el 6.",
      "Antes de usar la regla pregúntate si hay resultados comunes. Un diagrama o una lista de los resultados de cada evento lo muestra rápido. En una tabla de doble entrada, los resultados comunes son los de la celda donde se cruzan las dos características. Siempre revisa que el resultado esté entre 0 y 1 y que no sea menor que P(A) ni que P(B).",
  ],
  vocab=[("eventos incompatibles", "eventos que no pueden ocurrir a la vez"), ("A o B", "ocurre A, ocurre B, o ocurren los dos"), ("A y B", "ocurren los dos a la vez"), ("regla aditiva", "P(A o B) = P(A) + P(B) − P(A y B)")],
  worked=[
      ("Eventos incompatibles", "Una ruleta tiene 10 sectores iguales numerados del 1 al 10. ¿Cuál es la probabilidad de caer en un múltiplo de 3 o en un múltiplo de 5?",
       ["Múltiplos de 3: {3, 6, 9}, con probabilidad 3/10. Múltiplos de 5: {5, 10}, con probabilidad 2/10.", "No tienen resultados comunes, así que son incompatibles.", "P = 3/10 + 2/10 = 5/10 = 1/2."], "P(múltiplo de 3 o de 5) = 1/2"),
      ("Eventos que pueden ocurrir a la vez", "Se lanza un dado. ¿Cuál es la probabilidad de obtener un número par o mayor que 4?",
       ["Par: {2, 4, 6}, con probabilidad 3/6. Mayor que 4: {5, 6}, con probabilidad 2/6.", "Comparten el 6, que tiene probabilidad 1/6.", "P = 3/6 + 2/6 − 1/6 = 4/6 = 2/3. Comprobación: los resultados son 2, 4, 5 y 6."], "P(par o mayor que 4) = 2/3"),
  ],
  mist=[
      ("Sumar siempre las dos probabilidades: 3/6 + 2/6 = 5/6 en el ejemplo del dado.", "El 6 estaba en los dos eventos y se contó dos veces.", "Resta la probabilidad de que ocurran juntos."),
      ("Restar P(A y B) cuando los eventos son incompatibles.", "Si no pueden ocurrir a la vez, P(A y B) es 0 y no hay nada que restar.", "Primero revisa si los eventos comparten algún resultado."),
  ],
  R=[ex("Se lanza un dado. ¿Cuál es la probabilidad de obtener 1 o 2?" + FRAC, fr(F(1, 6) + F(1, 6)), "Son eventos incompatibles: 1/6 + 1/6 = 2/6, o sea 1/3."),
     ex("Dos eventos que no pueden ocurrir a la vez, ¿cómo se llaman?", "Incompatibles", "Incompatibles significa que no tienen resultados en común."),
     ex("Una bolsa tiene 4 fichas rojas, 3 azules y 3 verdes. Se saca una al azar. ¿Cuál es la probabilidad de que sea roja o azul?" + FRAC, fr(F(4, 10) + F(3, 10)), "Son incompatibles: 4/10 + 3/10 = 7/10.")],
  C=[ex("Se lanza un dado. ¿Cuál es la probabilidad de obtener un número menor que 3 o mayor que 4?" + FRAC, fr(F(2, 6) + F(2, 6)), "{1, 2} y {5, 6} no comparten resultados: 2/6 + 2/6 = 4/6, o sea 2/3."),
     ex("Se lanza un dado. ¿Cuál es la probabilidad de obtener un número par o un múltiplo de 3?" + FRAC, fr(F(3, 6) + F(2, 6) - F(1, 6)), "Par {2, 4, 6}, múltiplo de 3 {3, 6}; comparten el 6: 3/6 + 2/6 − 1/6 = 4/6, o sea 2/3."),
     ex("Se lanza un dado. ¿Son incompatibles los eventos «sale 1» y «sale par»? Responde sí o no.", "Sí", "El 1 no es par, así que no hay resultados en común.")],
  A=[ex("Una ruleta tiene 12 sectores iguales numerados del 1 al 12. ¿Cuál es la probabilidad de caer en un múltiplo de 4 o en un múltiplo de 6?" + FRAC, fr(F(3, 12) + F(2, 12) - F(1, 12)), "Múltiplos de 4: 4, 8 y 12. Múltiplos de 6: 6 y 12. Comparten el 12: 3/12 + 2/12 − 1/12 = 4/12, o sea 1/3."),
     ex("En un curso de 25 estudiantes, 10 usan lentes, 8 participan en el taller de música y 3 hacen las dos cosas. Se elige un estudiante al azar. ¿Cuál es la probabilidad de que use lentes o participe en el taller?" + FRAC, fr(F(10, 25) + F(8, 25) - F(3, 25)), "10/25 + 8/25 − 3/25 = 15/25, o sea 3/5; se resta lo común para no contar dos veces."),
     ex("Se sabe que P(A) = 1/2, P(B) = 1/3 y P(A y B) = 1/6. ¿Cuánto vale P(A o B)?" + FRAC, fr(F(1, 2) + F(1, 3) - F(1, 6)), "1/2 + 1/3 − 1/6 = 3/6 + 2/6 − 1/6 = 4/6, o sea 2/3.")],
  Z=[ex("Sofía suma P(par) = 3/6 y P(mayor que 3) = 3/6 en un dado y obtiene 1, y dice que es seguro que ocurre uno de los dos. ¿Está bien? Responde sí o no.", "No", "Los resultados 4 y 6 están en los dos eventos; la probabilidad correcta es 3/6 + 3/6 − 2/6 = 4/6."),
     ex("¿Puede P(A o B) ser menor que P(A)? Responde sí o no.", "No", "Si ocurre A, entonces ya ocurre «A o B», así que P(A o B) es al menos P(A).")],
  D=[ex("En un curso de 30 estudiantes, 12 llegan en bus y 9 usan lentes; 5 estudiantes llegan en bus y usan lentes. Se elige uno al azar. ¿Cuál es la probabilidad de que llegue en bus o use lentes?" + FRAC, fr(F(12, 30) + F(9, 30) - F(5, 30)), "12/30 + 9/30 − 5/30 = 16/30, o sea 8/15."),
     ex("P(A) = 3/10, P(B) = 1/2 y P(A o B) = 3/5. ¿Cuánto vale P(A y B)?" + FRAC, fr(F(3, 10) + F(1, 2) - F(3, 5)), "Se despeja: P(A y B) = P(A) + P(B) − P(A o B) = 3/10 + 5/10 − 6/10 = 2/10, o sea 1/5.")],
  ctx=[ex("En una rifa con 50 números, ganan los múltiplos de 10 y los múltiplos de 25. ¿Cuál es la probabilidad de que un número elegido al azar gane?" + FRAC, fr(F(5, 50) + F(2, 50) - F(1, 50)), "Múltiplos de 10: 5. Múltiplos de 25: 2. Comparten el 50: 5/50 + 2/50 − 1/50 = 6/50, o sea 3/25.")],
  chk=[ex("¿Qué se resta en la regla aditiva cuando los eventos pueden ocurrir a la vez?", "La probabilidad de que ocurran juntos", "Se resta P(A y B) para no contar dos veces los resultados comunes."),
       ex("Se lanza un dado. ¿Cuál es la probabilidad de obtener 3, 4 o 5?" + FRAC, fr(F(1, 6) + F(1, 6) + F(1, 6)), "Son incompatibles: 1/6 + 1/6 + 1/6 = 3/6, o sea 1/2."),
       ex("Si dos eventos son incompatibles, ¿cuánto vale P(A y B)?", "0", "No pueden ocurrir a la vez.")],
  op=("Una bolsa de ejemplo tiene 10 fichas numeradas del 1 al 10. Sin sacar ninguna, escribe los resultados favorables y la probabilidad de cada uno de estos eventos: «número par o mayor que 7» y «número menor que 3 o mayor que 8». Indica en cada caso si los eventos son incompatibles y qué regla usaste. Si quieres comprobar, anota los números en papeles, sácalos de uno en uno, devolviendo cada papel antes de sacar el siguiente, 20 veces y compara.",
      "«Par o mayor que 7»: par {2, 4, 6, 8, 10}, mayor que 7 {8, 9, 10}, comparten 8 y 10. P = 5/10 + 3/10 − 2/10 = 6/10 = 3/5; no son incompatibles. «Menor que 3 o mayor que 8»: {1, 2} y {9, 10}, incompatibles: P = 2/10 + 2/10 = 4/10 = 2/5.",
      ["lista los resultados de cada evento", "busca resultados comunes", "elige la regla correcta", "simplifica las fracciones"],
      ["listas de resultados", "dos probabilidades con su regla", "comprobación con la lista"],
      ["sumar sin restar lo común", "restar cuando no hay nada común", "no simplificar"],
      "Pide que justifique cómo supo que los eventos eran compatibles o incompatibles. Reconoce que haya listado los resultados."),
  reinforce="Calcula, en un dado, la probabilidad de obtener un número impar o menor que 4 y comprueba tu resultado listando los resultados favorables.",
  extend="Explica con un ejemplo de tu curso por qué hay que restar lo que se cuenta dos veces.")

# ================================================================ OA 14 · clase 3
L(OA14, 3,
  use="Aprenderé la regla multiplicativa: cómo calcular la probabilidad de que ocurran dos eventos seguidos, con y sin reposición, usando un árbol.",
  prior=["Sé listar el espacio muestral de dos etapas.", "Sé multiplicar fracciones y simplificar."],
  explain=[
      "La regla multiplicativa se usa cuando se pregunta por A y luego B. Si los dos eventos son independientes, es decir, que ocurra uno no cambia la probabilidad del otro, se multiplican las probabilidades: P(A y B) = P(A) × P(B). Ejemplo: P(cara) = 1/2 y P(6) = 1/6 en un dado, así que P(cara y 6) = 1/2 × 1/6 = 1/12.",
      "Los lanzamientos de una moneda o un dado son independientes: la moneda no recuerda cómo salió antes. En una bolsa, si se saca una ficha y se devuelve, la segunda extracción es independiente de la primera (con reposición). Si no se devuelve (sin reposición), cambia el total de fichas y la probabilidad de la segunda extracción: son eventos dependientes.",
      "Un árbol ayuda: en cada rama se escribe la probabilidad de ese paso, y para un camino completo se multiplican las probabilidades de sus ramas. En una bolsa con 3 rojas y 2 azules, sin reposición, la probabilidad de roja y luego roja es 3/5 × 2/4, porque quedan 4 fichas y 2 son rojas.",
  ],
  vocab=[("eventos independientes", "eventos en que uno no cambia la probabilidad del otro"), ("con reposición", "la ficha se devuelve a la bolsa antes de sacar otra"), ("sin reposición", "la ficha no se devuelve, así que cambia la bolsa"), ("árbol de probabilidades", "diagrama con ramas que muestran cada paso y su probabilidad")],
  worked=[
      ("Eventos independientes", "Se lanzan una moneda y un dado. ¿Cuál es la probabilidad de obtener cara y un 5?",
       ["P(cara) = 1/2 y P(5) = 1/6.", "Los lanzamientos son independientes, así que se multiplican.", "P = 1/2 × 1/6 = 1/12."], "P(cara y 5) = 1/12"),
      ("Sin reposición", "Una bolsa tiene 3 fichas rojas y 2 azules. Se sacan dos fichas sin devolverlas. ¿Cuál es la probabilidad de que las dos sean rojas? Compárala con el caso con reposición.",
       ["Primera ficha roja: 3/5.", "Si fue roja, quedan 4 fichas y 2 son rojas: la segunda es roja con probabilidad 2/4.", "Sin reposición: 3/5 × 2/4 = 6/20 = 3/10. Con reposición sería 3/5 × 3/5 = 9/25."], "Sin reposición 3/10; con reposición 9/25"),
  ],
  mist=[
      ("Multiplicar 3/5 × 3/5 en una extracción sin reposición.", "Al no devolver la ficha, el total y la cantidad de rojas cambian para la segunda extracción.", "Cuenta cuántas fichas quedan y cuántas son del color pedido."),
      ("Sumar las probabilidades de las ramas de un mismo camino.", "Para «A y luego B» se multiplica; sumar da un valor equivocado, a veces mayor que 1.", "Multiplica los pasos de un mismo camino del árbol."),
  ],
  R=[ex("Se lanzan dos monedas. ¿Cuál es la probabilidad de obtener sello y sello?" + FRAC, fr(F(1, 2) * F(1, 2)), "1/2 × 1/2 = 1/4."),
     ex("Dos lanzamientos de una moneda, ¿son eventos independientes? Responde sí o no.", "Sí", "El resultado de la primera moneda no cambia la probabilidad de la segunda."),
     ex("En un dado, P(6) = 1/6. Si lanzas el dado dos veces, ¿cuál es la probabilidad de obtener 6 y 6?" + FRAC, fr(F(1, 6) * F(1, 6)), "1/6 × 1/6 = 1/36.")],
  C=[ex("Una bolsa tiene 1 ficha roja y 4 azules. Se saca una, se devuelve y se saca otra. ¿Cuál es la probabilidad de que las dos sean azules?" + FRAC, fr(F(4, 5) * F(4, 5)), "Con reposición, cada extracción tiene 4/5: 4/5 × 4/5 = 16/25."),
     ex("En la misma bolsa de 1 roja y 4 azules se sacan dos fichas sin devolverlas. ¿Cuál es la probabilidad de que las dos sean azules?" + FRAC, fr(F(4, 5) * F(3, 4)), "Después de sacar una azul quedan 4 fichas, 3 azules: 4/5 × 3/4 = 12/20, o sea 3/5."),
     ex("En una extracción sin reposición, ¿por qué cambia la probabilidad de la segunda ficha? A) Porque el color cambia. B) Porque la bolsa tiene una ficha menos y puede haber una menos de ese color. C) Porque la primera ficha siempre es la más probable.", "B", "Al no devolver la ficha cambian el total y la composición de la bolsa.")],
  A=[ex("Una ruleta tiene 4 colores iguales: rojo, verde, azul y amarillo. Se hace girar dos veces. ¿Cuál es la probabilidad de obtener rojo la primera vez y verde la segunda?" + FRAC, fr(F(1, 4) * F(1, 4)), "Los giros son independientes: 1/4 × 1/4 = 1/16."),
     ex("Se lanzan una moneda y un dado. ¿Cuál es la probabilidad de obtener cara y un número par?" + FRAC, fr(F(1, 2) * F(3, 6)), "1/2 × 3/6 = 3/12, o sea 1/4; es el mismo resultado de contar 3 favorables de 12."),
     ex("Una bolsa tiene 10 fichas, 4 de ellas rojas. Se sacan dos sin devolverlas. ¿Cuál es la probabilidad de que las dos sean rojas?" + FRAC, fr(F(4, 10) * F(3, 9)), "La primera es roja con 4/10 y la segunda con 3/9: 12/90, o sea 2/15.")],
  Z=[ex("Ana lanzó una moneda tres veces y salió cara las tres. Dice: «La cuarta tiene más probabilidad de ser sello». ¿Tiene razón? Responde sí o no.", "No", "Los lanzamientos son independientes y la probabilidad de sello sigue siendo 1/2."),
     ex("Para calcular la probabilidad de «cara en una moneda y 6 en un dado», ¿qué operación se usa con las dos probabilidades? A) Sumarlas. B) Multiplicarlas. C) Restarlas.", "B", "Es «A y B» con eventos independientes, y se multiplican.")],
  D=[ex("Cada día de dos días seguidos puede llover con probabilidad 1/5, de forma independiente (datos de ejemplo). ¿Cuál es la probabilidad de que no llueva ninguno de los dos días?" + FRAC, fr(F(4, 5) * F(4, 5)), "No llover tiene probabilidad 4/5 cada día: 4/5 × 4/5 = 16/25."),
     ex("Se lanzan tres monedas. ¿Cuál es la probabilidad de que las tres sean cara?" + FRAC, fr(F(1, 2) ** 3), "1/2 × 1/2 × 1/2 = 1/8.")],
  ctx=[ex("En una caja hay 7 lápices azules y 3 rojos. Sin mirar, se sacan dos lápices seguidos sin devolverlos. ¿Cuál es la probabilidad de que los dos sean rojos?" + FRAC, fr(F(3, 10) * F(2, 9)), "3/10 × 2/9 = 6/90, o sea 1/15.")],
  chk=[ex("En «A y B» con eventos independientes, ¿se suman o se multiplican las probabilidades?", "Se multiplican", "La regla multiplicativa dice P(A y B) = P(A) × P(B)."),
       ex("Una bolsa tiene 2 fichas rojas y 3 azules; se saca una y se devuelve. ¿Cuál es la probabilidad de que la segunda sea roja?" + FRAC, fr(F(2, 5)), "Con reposición, la bolsa vuelve a tener 2 rojas de 5."),
       ex("Un dado se lanza dos veces. ¿Cuál es la probabilidad de que salga 1 y luego 2?" + FRAC, fr(F(1, 6) * F(1, 6)), "1/6 × 1/6 = 1/36.")],
  op=("Dibuja un árbol para una bolsa de ejemplo con 4 fichas: 2 rojas (R) y 2 azules (A), sacando dos fichas sin reposición. Escribe en cada rama su probabilidad y calcula la probabilidad de cada camino: RR, RA, AR y AA. Comprueba que las cuatro probabilidades suman 1. Si tienes cuatro papelitos o cartas de dos colores, haz 20 extracciones y compara.",
      "Camino RR: 2/4 × 1/3 = 1/6. RA: 2/4 × 2/3 = 1/3. AR: 2/4 × 2/3 = 1/3. AA: 2/4 × 1/3 = 1/6. Suma: 1/6 + 1/3 + 1/3 + 1/6 = 1.",
      ["árbol con ramas y probabilidades", "multiplica los pasos de cada camino", "cambia el total en la segunda extracción", "comprueba que la suma es 1"],
      ["árbol dibujado", "cuatro caminos calculados", "suma comprobada"],
      ["no cambiar el total en la segunda extracción", "sumar en vez de multiplicar", "olvidar comprobar la suma"],
      "Pide que explique por qué la segunda rama tiene denominador 3. Reconoce que compruebe que la suma de los caminos es 1."),
  reinforce="Calcula la probabilidad de sacar azul y luego azul de una bolsa con 2 azules y 3 rojas, con reposición.",
  extend="Explica con tus palabras por qué un árbol ayuda a no equivocarse con la segunda extracción sin reposición.")

# ================================================================ OA 14 · clase 4
L(OA14, 4,
  use="Aprenderé a combinar las reglas aditiva y multiplicativa en un mismo problema, a evaluar afirmaciones sobre probabilidades y a contrastar la teoría con una simulación manual.",
  prior=["Sé usar la regla aditiva y la multiplicativa por separado.", "Sé leer un árbol de probabilidades."],
  explain=[
      "Muchos problemas necesitan las dos reglas. En un árbol, dentro de cada camino se multiplica (A y luego B) y, cuando hay varios caminos que cumplen lo pedido, se suman las probabilidades de esos caminos (este camino o aquel). Por ejemplo, sacar una ficha de cada color en dos extracciones se logra con rojo-azul o con azul-rojo.",
      "Otra herramienta es el complemento. «Al menos una cara» en dos lanzamientos es lo contrario de «ninguna cara», que tiene probabilidad 1/2 × 1/2 = 1/4. Entonces P(al menos una cara) = 1 − 1/4 = 3/4. Con frecuencia es más corto calcular el complemento que sumar muchos caminos.",
      "Para contrastar la teoría puedes hacer una simulación manual: repetir el experimento muchas veces, anotar los resultados por bloques y calcular la frecuencia relativa acumulada. Con pocas repeticiones los resultados varían mucho; con más repeticiones, la frecuencia suele acercarse a la probabilidad teórica, pero no coincide exactamente. Una simulación corta nunca refuta una probabilidad calculada con las reglas.",
  ],
  vocab=[("al menos uno", "uno o más; se calcula como 1 menos la probabilidad de ninguno"), ("camino de un árbol", "serie de ramas que lleva de la primera etapa al resultado final"), ("simulación", "repetir un experimento para ver qué tan seguido ocurre un evento"), ("frecuencia relativa", "veces que ocurrió un evento dividido por el total de repeticiones")],
  worked=[
      ("Complemento: al menos una", "Se lanzan dos monedas. ¿Cuál es la probabilidad de obtener al menos una cara?",
       ["El complemento es «ninguna cara», es decir, sello y sello: 1/2 × 1/2 = 1/4.", "P(al menos una cara) = 1 − 1/4."], "P(al menos una cara) = 3/4"),
      ("Dos caminos", "Una bolsa tiene 2 fichas rojas y 3 azules. Se saca una ficha, se devuelve y se saca otra. ¿Cuál es la probabilidad de obtener una de cada color, en cualquier orden?",
       ["Camino rojo y azul: 2/5 × 3/5 = 6/25.", "Camino azul y rojo: 3/5 × 2/5 = 6/25.", "Son caminos distintos, así que se suman: 6/25 + 6/25 = 12/25."], "P(una de cada color) = 12/25"),
  ],
  mist=[
      ("Calcular «al menos una cara» en dos monedas como 1/2 + 1/2 = 1.", "Se cuenta dos veces el caso en que sale cara en ambas.", "Usa el complemento: 1 − P(ninguna cara)."),
      ("Concluir que la probabilidad teórica está mal porque una simulación corta dio otro porcentaje.", "Con pocas repeticiones los resultados varían mucho por azar.", "Junta más bloques y mira la frecuencia acumulada."),
  ],
  R=[ex("Se lanzan tres monedas. ¿Cuál es la probabilidad de que no salga ninguna cara?" + FRAC, fr(F(1, 2) ** 3), "Sello tres veces: 1/2 × 1/2 × 1/2 = 1/8."),
     ex("Se lanzan tres monedas. ¿Cuál es la probabilidad de obtener al menos una cara?" + FRAC, fr(1 - F(1, 8)), "Es el complemento de «ninguna cara»: 1 − 1/8 = 7/8."),
     ex("En un árbol de probabilidades, ¿qué operación se hace con las ramas de un mismo camino?", "Se multiplican", "Un camino es una secuencia de pasos que ocurren uno tras otro, y «y» se multiplica.")],
  C=[ex("Una bolsa tiene 3 fichas rojas y 2 azules. Se sacan dos sin devolverlas. ¿Cuál es la probabilidad de obtener una ficha de cada color, en cualquier orden?" + FRAC, fr(F(3, 5) * F(2, 4) + F(2, 5) * F(3, 4)), "Rojo-azul: 3/5 × 2/4 = 3/10. Azul-rojo: 2/5 × 3/4 = 3/10. Se suman: 6/10, o sea 3/5."),
     ex("Se lanzan dos dados de seis caras. ¿Cuál es la probabilidad de obtener al menos un 6?" + FRAC, fr(1 - F(5, 6) * F(5, 6)), "Ningún 6 tiene probabilidad 5/6 × 5/6 = 25/36, y el complemento es 1 − 25/36 = 11/36."),
     ex("¿Cuál afirmación sobre una simulación corta es correcta? A) Si da un porcentaje distinto del teórico, el cálculo teórico está mal. B) Con pocas repeticiones es normal que el porcentaje varíe respecto del teórico. C) Con 20 repeticiones el porcentaje siempre coincide con el teórico.", "B", "El azar produce variación y las repeticiones son pocas.")],
  A=[ex("Se simularon 5 bloques de 20 lanzamientos de dos monedas y se contó cuántas veces salieron dos caras: 4, 7, 5, 6 y 3. ¿Cuál es la frecuencia relativa acumulada de «dos caras» al terminar los 5 bloques (100 lanzamientos)?", "25%", "4 + 7 + 5 + 6 + 3 = 25 veces de 100 lanzamientos, o sea 25 %."),
     arith("La probabilidad teórica de obtener dos caras con dos monedas es 1/4. ¿Cuántas veces se esperaría dos caras en 100 lanzamientos?", "100//4", "La cuarta parte de 100 lanzamientos.", " veces"),
     ex("En la simulación, el segundo bloque dio 7 veces dos caras en 20 lanzamientos. ¿Cuál es la frecuencia relativa de ese bloque?", "35%", "Se divide 7 por 20: 7 ÷ 20 = 0,35, o sea 35 %.")],
  Z=[ex("En 20 lanzamientos de dos monedas salió dos caras 8 veces (40 %). Ariel dice: «Esto prueba que la probabilidad teórica 1/4 está mal». ¿Tiene razón? Responde sí o no.", "No", "Con solo 20 repeticiones es normal que el resultado varíe respecto de 25 %."),
     ex("Claudia calcula la probabilidad de obtener al menos un 6 en dos lanzamientos de un dado como 1/6 + 1/6 = 1/3. ¿Está bien? Responde sí o no.", "No", "Sumó dos eventos que pueden ocurrir juntos sin restar lo común; el valor correcto es 1 − 25/36 = 11/36.")],
  D=[ex("Se lanzan tres monedas. ¿Cuál es la probabilidad de obtener exactamente una cara?" + FRAC, fr(3 * F(1, 8)), "Hay tres caminos (CSS, SCS, SSC) con probabilidad 1/8 cada uno; se suman: 3/8."),
     ex("Una bolsa tiene 4 fichas rojas y 6 azules. Se sacan dos sin devolverlas. ¿Cuál es la probabilidad de que las dos sean del mismo color?" + FRAC, fr(F(4, 10) * F(3, 9) + F(6, 10) * F(5, 9)), "Rojo-rojo: 4/10 × 3/9 = 12/90. Azul-azul: 6/10 × 5/9 = 30/90. Se suman: 42/90, o sea 7/15.")],
  ctx=[ex("En un juego de ejemplo se lanza una moneda cuatro veces y se gana si sale al menos un sello. ¿Cuál es la probabilidad de ganar?" + FRAC, fr(1 - F(1, 16)), "Perder es obtener cuatro caras: 1/16. Ganar es el complemento: 15/16.")],
  chk=[ex("En un problema, ¿cuándo se suman las probabilidades de dos caminos de un árbol?", "Cuando cualquiera de los dos caminos sirve", "La conjunción «o» entre caminos distintos se resuelve con la regla aditiva."),
       ex("Se lanzan dos monedas. ¿Cuál es la probabilidad de no obtener ninguna cara?" + FRAC, fr(F(1, 4)), "Es sello y sello: 1/2 × 1/2 = 1/4."),
       ex("¿Una simulación con pocas repeticiones puede dar una frecuencia distinta de la probabilidad? Responde sí o no.", "Sí", "El azar produce variación, sobre todo con pocas repeticiones.")],
  op=("Con una moneda, simula 5 bloques de 10 lanzamientos de dos monedas (lanza dos monedas a la vez, o la misma moneda dos veces) y anota cuántas veces sale al menos una cara en cada bloque. Si no tienes moneda, usa estos datos de ejemplo: 7, 8, 9, 7 y 8 veces. Calcula la frecuencia relativa de cada bloque, la acumulada de los 5 bloques y compárala con la probabilidad teórica 3/4.",
      "Con los datos de ejemplo, los bloques dan 70 %, 80 %, 90 %, 70 % y 80 %. En total 7 + 8 + 9 + 7 + 8 = 39 de 50, o sea 78 %. La probabilidad teórica 3/4 es 75 %; la simulación se acerca pero no coincide exactamente.",
      ["registra cada bloque", "calcula la frecuencia relativa de cada uno", "calcula la acumulada", "compara con 75 %", "explica la diferencia"],
      ["tabla de bloques", "frecuencias calculadas", "comparación con la teoría"],
      ["dividir por el número de bloques en vez de por los lanzamientos", "decir que la simulación debe coincidir exactamente", "no usar el total acumulado"],
      "Pide que explique por qué los bloques difieren entre sí. Reconoce que compare la acumulada con 3/4."),
  reinforce="Calcula la probabilidad de no obtener ningún 6 en tres lanzamientos de un dado y de obtener al menos un 6.",
  extend="Explica por qué «al menos uno» suele calcularse con el complemento y no sumando todos los caminos.")
