"""Cuaderno del estudiante, 2.º medio Ciencias Naturales: OA 11 (trabajo, potencia y conservación de la energía mecánica)."""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _x(items):
    return [ex(*i) if isinstance(i, tuple) else i for i in items]


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": w[0], "problem": w[1], "steps": w[2], "answer": w[3]} for w in worked],
        mistakes=[{"wrong": m[0], "why": m[1], "fix": m[2]} for m in mistakes],
        tiers={"recovery": _x(rec), "understand": _x(und), "apply": _x(app), "reason": _x(rea), "challenge": _x(cha)},
        context=_x(context), selfcheck=_x(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


OA11 = "CN2M OA 11"

# ---------------------------------------------------------------- OA 11

L(OA11, 1,
  materials="Este cuaderno y lápiz. Para observar: un libro liviano que se sube de una mesa a una repisa baja, con cuidado. Los datos están escritos en los ejercicios.",
  use="Aprenderé qué es el trabajo en Física, cómo se calcula y cómo plantear una pregunta que se pueda investigar sobre trabajo y energía.",
  prior=["Sé que la fuerza se mide en newtons y la distancia en metros.", "Sé que el peso de un objeto es su masa por g, con g = 10 m/s²."],
  explain=[
      "En Física, el trabajo es la energía que una fuerza transfiere a un objeto al moverlo. Si la fuerza tiene la misma dirección que el movimiento, el trabajo es igual a la fuerza por la distancia, con la fuerza en newtons y la distancia en metros. Se mide en joules (J). Un joule es el trabajo de una fuerza de 1 N que mueve un objeto 1 m. Si el objeto no se desplaza, el trabajo es cero, aunque haya fuerza.",
      "La energía es la capacidad de realizar trabajo. La energía mecánica incluye la energía cinética, que depende del movimiento, y la energía potencial gravitatoria, que depende de la altura. Cuando una fuerza hace trabajo sobre un objeto, su energía cambia en esa cantidad. Al subir un objeto con rapidez constante, la fuerza necesaria es igual a su peso, que es masa por 10 en este cuaderno.",
      "Una pregunta investigable sobre trabajo dice qué se cambia y qué se mide. Por ejemplo: «¿Cuántos joules de trabajo se necesitan para subir un libro de 1 kg hasta una repisa a 1 m y hasta otra a 2 m de altura?». La pregunta «¿es cansador trabajar?» no se puede investigar, porque el cansancio no es una medición y mezcla el trabajo cotidiano con el trabajo físico.",
  ],
  vocab=[("trabajo", "energía transferida por una fuerza al mover un objeto; fuerza por distancia"), ("joule (J)", "unidad de trabajo y energía"), ("energía", "capacidad de realizar trabajo"), ("energía cinética", "energía del movimiento"), ("energía potencial gravitatoria", "energía que depende de la altura")],
  worked=[
      ("Calcular un trabajo", "Una persona empuja un cajón con una fuerza de 20 N a lo largo de 5 m en la misma dirección del empuje. ¿Cuánto trabajo realiza?", ["Trabajo = fuerza × distancia.", "20 × 5 = 100."], "100 J"),
      ("Fuerza sin desplazamiento", "Una persona sostiene una mochila quieta con una fuerza de 50 N durante un minuto. ¿Cuánto trabajo físico realiza sobre la mochila?", ["La distancia que se mueve la mochila es 0 m.", "Trabajo = 50 × 0."], "0 J"),
  ],
  mistakes=[
      ("Decir que hay trabajo siempre que hay esfuerzo o cansancio.", "En Física el trabajo exige que el objeto se desplace en la dirección de la fuerza.", "Pregunta: ¿se movió el objeto por la acción de la fuerza?"),
      ("Sumar la fuerza y la distancia.", "El trabajo es el producto de ambas.", "Multiplica newtons por metros para obtener joules."),
  ],
  rec=[
      ("¿En qué unidad se mide el trabajo?", "Joule (J)", "Es la unidad de trabajo y de energía."),
      ("Verdadero o falso: si el objeto no se desplaza, el trabajo es cero.", "Verdadero", "Sin distancia recorrida no hay transferencia de energía por esa fuerza."),
      ("Completa: trabajo = fuerza × ___.", "Distancia", "Es la distancia recorrida en la dirección de la fuerza."),
  ],
  und=[
      ("Una persona sostiene una caja quieta sobre sus brazos durante un minuto. ¿Cuánto trabajo físico hace sobre la caja? A) Cero, porque no hay desplazamiento; B) Positivo, porque hace fuerza.", "A", "Sin desplazamiento el trabajo es cero."),
      ("Una fuerza de 10 N mueve un objeto 3 m en su misma dirección. ¿Cuál es el trabajo? A) 30 J; B) 13 J.", "A", "Se multiplica fuerza por distancia."),
      ("¿Qué energía depende de la altura de un objeto?", "La energía potencial gravitatoria", "A mayor altura, mayor energía potencial."),
  ],
  app=[
      arith("Una fuerza de 25 N mueve un carro 6 m en la misma dirección. ¿Cuánto trabajo realiza?", "25*6", "Fuerza por distancia.", " J"),
      arith("Una persona sube una caja de 4 kg hasta una repisa a 2 m de altura con rapidez constante. ¿Cuánto trabajo hace? (El peso es 4 × 10 N).", "4*10*2", "La fuerza es el peso y la distancia es la altura.", " J"),
      arith("Una fuerza realizó 210 J de trabajo al mover un objeto 7 m en su dirección. ¿Cuál era el valor de la fuerza?", "210//7", "Se despeja la fuerza: trabajo dividido por distancia.", " N"),
  ],
  rea=[
      ("Un compañero dice: «Si empujo una pared con 100 N, hago 100 J de trabajo». ¿Qué le respondes? A) Es falso: la pared no se desplaza, así que el trabajo es 0 J; B) Es verdadero, porque hay fuerza.", "A", "El trabajo requiere desplazamiento."),
      ("Se sube el mismo libro de 1 kg a una repisa a 1 m y a otra a 2 m. ¿En qué caso se hace más trabajo y por qué? A) En la de 2 m, porque el desplazamiento es mayor con la misma fuerza; B) Igual en ambas, porque el libro es el mismo.", "A", "El trabajo crece con la altura a la que se sube el libro."),
  ],
  cha=[
      arith("Una persona arrastra una caja con 30 N a lo largo de 12 m y luego con 20 N otros 5 m, en la misma dirección. ¿Cuál es el trabajo total?", "30*12+20*5", "Se calcula el trabajo de cada tramo y se suman.", " J"),
      arith("Una persona sube un libro de 1 kg hasta 3 m y luego otro libro igual hasta 3 m. ¿Cuál es el trabajo total? (peso de cada libro: 10 N).", "10*3+10*3", "Cada libro requiere 10 × 3 J.", " J"),
  ],
  context=[arith("Una estudiante empuja un carro de supermercado de ejemplo 8 m con una fuerza de 25 N en la misma dirección. ¿Cuánto trabajo realiza?", "25*8", "Fuerza por distancia.", " J")],
  selfcheck=[("¿Cómo se calcula el trabajo cuando la fuerza va en la dirección del movimiento?", "Fuerza por distancia", "Se mide en joules."), ("¿Por qué sostener un peso quieto no es trabajo en Física?", "Porque no hay desplazamiento", "La distancia es cero."), ("¿Qué hace investigable a una pregunta sobre trabajo?", "Que indica qué se cambia y qué se mide", "Permite contestar con datos.")],
  open_task=task("Datos de ejemplo: un libro de 2 kg se sube desde la mesa hasta una repisa que está 1 m más arriba, y luego hasta otra repisa que está 3 m más arriba que la mesa (g = 10 m/s²). Calcula el trabajo en cada caso. Escribe una pregunta investigable que compare ambos casos, y explica por qué sostener el libro quieto en la repisa no agrega trabajo.", "Peso 20 N. Hasta 1 m: 20 × 1 = 20 J. Hasta 3 m: 20 × 3 = 60 J. Pregunta: «¿Cuántos joules de trabajo se necesitan para subir el mismo libro a 1 m y a 3 m?». Sostenerlo quieto no agrega trabajo porque no hay desplazamiento.", ["calcula el peso y los dos trabajos con unidad", "la pregunta indica qué se cambia y qué se mide", "justifica con el desplazamiento"], ["dos cálculos, una pregunta y una justificación"], ["confundir peso con masa", "decir que sostener es trabajo"], "Pregunta cómo cambiaría el trabajo con un libro de 4 kg."),
  reinforce="Calcula el trabajo de una fuerza de 15 N que mueve un objeto 4 m en su misma dirección.",
  extend="Explica por qué el trabajo cotidiano y el trabajo físico no significan lo mismo.")

L(OA11, 2,
  materials="Este cuaderno y lápiz. Las tablas de datos de ejemplo están escritas en los ejercicios. Calculadora opcional.",
  use="Aprenderé qué es la potencia, cómo se calcula con trabajo y tiempo, y cómo comparar datos de varias máquinas o personas.",
  prior=["Sé calcular el trabajo en joules.", "Sé pasar minutos a segundos."],
  explain=[
      "La potencia mide qué tan rápido se realiza un trabajo: potencia = trabajo ÷ tiempo. Se mide en watts (W): 1 W es 1 joule por segundo. Dos personas que hacen el mismo trabajo no tienen la misma potencia si una tarda menos tiempo. Un aparato de 60 W transforma 60 J de energía cada segundo.",
      "Los datos de potencia se leen en tablas con trabajo y tiempo. Si el trabajo es el mismo, mayor tiempo significa menor potencia. Si el tiempo es el mismo, mayor trabajo significa mayor potencia. Antes de comparar hay que usar las mismas unidades: si el tiempo viene en minutos, se pasa a segundos multiplicando por 60.",
      "Un resultado de potencia siempre lleva su unidad. Además, la potencia calculada con el trabajo útil suele ser menor que la potencia del aparato, porque una parte de la energía se pierde como calor. Por eso, al examinar datos, se debe decir si el trabajo considerado es el útil o el total.",
  ],
  vocab=[("potencia", "trabajo dividido por el tiempo"), ("watt (W)", "joule por segundo"), ("trabajo útil", "trabajo que cumple el objetivo buscado"), ("calor", "energía que se pierde como calentamiento"), ("unidades", "se deben convertir antes de comparar")],
  worked=[
      ("Calcular una potencia", "Un motor de ejemplo realiza 300 J de trabajo en 10 s. ¿Cuál es su potencia?", ["Potencia = trabajo ÷ tiempo.", "300 ÷ 10."], "30 W"),
      ("Pasar minutos a segundos", "Una bomba de ejemplo realiza 600 J de trabajo en 2 minutos. ¿Cuál es su potencia en watts?", ["2 minutos son 2 × 60 = 120 s.", "600 ÷ 120."], "5 W"),
  ],
  mistakes=[
      ("Dividir por el tiempo en minutos sin convertirlo a segundos.", "El watt es joule por segundo; con minutos el resultado queda en otra unidad.", "Convierte los minutos a segundos antes de dividir."),
      ("Creer que más potencia siempre significa más trabajo.", "Una potencia mayor puede venir de un tiempo menor.", "Mira trabajo y tiempo por separado."),
  ],
  rec=[
      ("¿En qué unidad se mide la potencia?", "Watt (W)", "Es joule por segundo."),
      ("Completa: potencia = trabajo ÷ ___.", "Tiempo", "Mide cuánto trabajo se hace por unidad de tiempo."),
      ("Verdadero o falso: con el mismo trabajo, quien tarda menos tiene mayor potencia.", "Verdadero", "Menor tiempo en el denominador da mayor potencia."),
  ],
  und=[
      ("¿Qué equivale a 1 W? A) 1 joule por segundo; B) 1 newton por metro.", "A", "El watt es una unidad de trabajo por tiempo."),
      ("Dos personas suben las mismas escaleras: la primera tarda 10 s y la segunda 20 s. ¿Quién tiene mayor potencia? A) La que tarda 10 s; B) La que tarda 20 s.", "A", "Hace el mismo trabajo en menos tiempo."),
      ("Un aparato tiene una potencia de 40 W. ¿Cuántos joules transforma en 1 s?", "40 J", "1 W es 1 J por segundo."),
  ],
  app=[
      arith("Una máquina de ejemplo realiza 900 J de trabajo en 15 s. ¿Cuál es su potencia?", "900//15", "Trabajo dividido por tiempo.", " W"),
      arith("Un motor de ejemplo hace 3.600 J de trabajo en 3 minutos. ¿Cuál es su potencia en watts? (3 minutos = 180 s).", "3600//180", "Primero se convierte el tiempo a segundos.", " W"),
      arith("Un aparato de ejemplo de 70 W funciona durante 9 s. ¿Cuánta energía transforma?", "70*9", "Energía = potencia por tiempo.", " J"),
  ],
  rea=[
      ("Un estudiante dice: «Más potencia siempre significa más trabajo». ¿Qué respondes? A) No necesariamente: la potencia también depende del tiempo que se tarda; B) Sí, porque son lo mismo.", "A", "Una potencia alta puede deberse a un tiempo corto."),
      ("Tabla de ejemplo: la persona P hizo 400 J en 8 s y la persona Q hizo 450 J en 10 s. ¿Quién tuvo mayor potencia? A) P, con 50 W; B) Q, con 45 W.", "A", "400 ÷ 8 = 50 y 450 ÷ 10 = 45."),
  ],
  cha=[
      arith("La máquina A tiene una potencia de 150 W. La máquina B realiza 3.600 J en 20 s. ¿Cuántos watts más tiene B que A?", "3600//20-150", "La potencia de B es 180 W; se resta la de A.", " W"),
      arith("Una persona sube una caja de 10 kg (peso 100 N) hasta 3 m de altura en 6 s. ¿Cuál es su potencia?", "100*3//6", "El trabajo es 300 J y se divide por 6 s.", " W"),
  ],
  context=[arith("Un ventilador de ejemplo tiene 25 W y funciona 40 s. ¿Cuánta energía transforma?", "25*40", "Potencia por tiempo.", " J")],
  selfcheck=[("¿Cómo se calcula la potencia?", "Trabajo dividido por tiempo", "Se mide en watts."), ("¿Qué equivale a 1 W?", "1 joule por segundo", "Es la unidad de potencia."), ("¿Por qué conviene pasar los minutos a segundos?", "Porque el watt usa segundos", "Así las unidades coinciden.")],
  open_task=task("Datos de ejemplo de dos personas que suben cajas iguales de 5 kg (peso 50 N) a una repisa de 2 m. La persona X tarda 5 s y la persona Y tarda 10 s. Calcula el trabajo de cada una, su potencia y escribe una conclusión que compare ambas. Agrega un límite: qué no considera este cálculo.", "Trabajo de cada una: 50 × 2 = 100 J. X: 100 ÷ 5 = 20 W. Y: 100 ÷ 10 = 10 W. X tiene el doble de potencia porque hizo el mismo trabajo en la mitad del tiempo. Límite: no considera el calor que pierde el cuerpo ni el cansancio.", ["calcula trabajo y las dos potencias", "concluye comparando", "declara un límite"], ["tres cálculos y una conclusión"], ["usar tiempos distintos como si fueran el mismo", "olvidar la unidad"], "Pregunta qué pasaría si Y subiera dos cajas en 10 s."),
  reinforce="Calcula la potencia de un aparato que realiza 500 J en 25 s.",
  extend="Explica por qué dos estufas de igual consumo total pueden tener potencias distintas.")

L(OA11, 3,
  materials="Este cuaderno y lápiz. Para pensar el modelo: una pelota de goma que baja por una rampa de cartón apoyada en libros. Los datos están escritos.",
  use="Aprenderé las energías potencial y cinética, el modelo de conservación de la energía mecánica y cómo contrastarlo con mediciones.",
  prior=["Sé calcular el trabajo.", "Sé usar g = 10 m/s²."],
  explain=[
      "La energía potencial gravitatoria depende de la masa, la altura y g: Ep = m × g × h, en joules, con g = 10 m/s². La energía cinética depende de la masa y de la velocidad: Ec = ½ × m × v², también en joules. La energía mecánica es la suma Ep + Ec.",
      "El modelo de conservación de la energía mecánica dice que, si solo actúa el peso y no hay roce, la energía mecánica total no cambia: lo que se pierde de Ep se gana en Ec. Una pelota que baja por una rampa lisa pierde altura y gana velocidad. Es un modelo ideal: en la realidad una parte de la energía se transforma en calor por el roce.",
      "Para contrastar el modelo se comparan sus predicciones con mediciones. Si la velocidad final medida es un poco menor que la calculada, la diferencia se atribuye al roce con la rampa y con el aire. Un modelo es útil si predice bien en ciertas condiciones, y se debe decir cuáles son.",
  ],
  vocab=[("energía potencial gravitatoria", "Ep = m × g × h"), ("energía cinética", "Ec = ½ × m × v²"), ("energía mecánica", "suma de energía potencial y cinética"), ("conservación", "la cantidad total no cambia"), ("modelo ideal", "modelo que ignora el roce")],
  worked=[
      ("Calcular una energía cinética", "Un objeto de 4 kg se mueve a 3 m/s. ¿Cuál es su energía cinética?", ["Ec = ½ × m × v² = ½ × 4 × 3 × 3.", "4 × 9 = 36 y la mitad es 18."], "18 J"),
      ("Aplicar la conservación", "Una pelota de 2 kg se suelta desde el reposo a 4 m de altura, sin roce. ¿Cuánta energía cinética tiene justo antes de llegar al suelo?", ["Ep arriba = 2 × 10 × 4 = 80 J y Ec = 0.", "Por conservación, abajo la Ep es 0, así que Ec = 80 J."], "80 J"),
  ],
  mistakes=[
      ("Calcular la Ec sin elevar al cuadrado la velocidad.", "La energía cinética depende de v por v, no de v.", "Multiplica v por v antes de multiplicar por la masa."),
      ("Decir que la energía se destruye cuando el objeto se detiene.", "La energía se transforma, por ejemplo en calor por el roce.", "Pregunta en qué forma de energía se transformó."),
  ],
  rec=[
      ("¿Qué energía depende de la altura?", "La potencial gravitatoria", "Ep = m × g × h."),
      ("Verdadero o falso: en el punto más alto de una caída desde el reposo, la energía cinética es 0.", "Verdadero", "Parte sin velocidad."),
      ("¿Qué se suma para obtener la energía mecánica?", "La energía potencial y la cinética", "Ep + Ec."),
  ],
  und=[
      ("Una pelota baja por una rampa lisa. ¿Qué ocurre con sus energías? A) La potencial disminuye y la cinética aumenta; B) Ambas aumentan.", "A", "Pierde altura y gana velocidad."),
      ("Si hay roce, ¿cómo es la energía mecánica final comparada con la inicial? A) Menor, porque parte se transforma en calor; B) Mayor, porque se suma el roce.", "A", "El roce transforma energía mecánica en calor."),
      ("Dos pelotas, de 1 kg y de 2 kg, se suben a la misma altura. ¿Cuál tiene más energía potencial?", "La de 2 kg", "Ep es proporcional a la masa."),
  ],
  app=[
      arith("¿Cuál es la energía potencial de un objeto de 3 kg que está a 6 m de altura? (g = 10 m/s²).", "3*10*6", "Ep = m × g × h.", " J"),
      arith("¿Cuál es la energía cinética de un objeto de 6 kg que se mueve a 4 m/s?", "6*4*4//2", "Ec = ½ × m × v × v.", " J"),
      arith("Un objeto de 5 kg está a 2 m de altura y se mueve a 2 m/s. ¿Cuál es su energía mecánica? (g = 10 m/s²).", "5*10*2+5*2*2//2", "Se suma la Ep (100 J) y la Ec (10 J).", " J"),
  ],
  rea=[
      ("Un estudiante dice: «La energía desaparece cuando la pelota se detiene». ¿Qué respondes? A) Se transforma, por ejemplo en calor por el roce; B) Desaparece sin dejar rastro.", "A", "La energía se conserva en el total, aunque cambie de forma."),
      ("Dos pelotas de 1 kg y 2 kg se sueltan desde la misma altura sin roce. ¿Qué afirmación es correcta sobre la Ep inicial? A) La de 2 kg tiene el doble; B) Ambas tienen la misma.", "A", "Ep depende de la masa, y el resto de los datos es igual."),
  ],
  cha=[
      arith("Un objeto de 2 kg se suelta desde 10 m de altura, sin roce. ¿Cuál es su energía cinética al llegar al suelo?", "2*10*10", "Toda la Ep se transforma en Ec.", " J"),
      arith("Un carrito de 2 kg parte del reposo en lo alto de una rampa lisa de 5 m. ¿Cuánta Ec tiene cuando está a 2 m de altura?", "2*10*5-2*10*2", "La Ec es la Ep inicial menos la Ep que le queda.", " J"),
  ],
  context=[arith("Una caja de ejemplo de 3 kg cae desde 5 m sin roce. ¿Cuál es su energía cinética justo antes de tocar el suelo?", "3*10*5", "La energía potencial inicial pasa a cinética.", " J")],
  selfcheck=[("¿Cuáles son las fórmulas de Ep y Ec?", "Ep = m × g × h y Ec = ½ × m × v²", "Ambas en joules."), ("¿Qué dice la conservación de la energía mecánica?", "Sin roce, la suma de Ep y Ec no cambia", "Una se transforma en la otra."), ("¿Por qué la velocidad medida suele ser menor que la calculada?", "Por el roce", "Parte de la energía se pierde como calor.")],
  open_task=task("Datos de ejemplo: una pelota de 1 kg baja por una rampa lisa y parte del reposo desde 5 m de altura. Calcula su Ep inicial, su Ec al final y, cuando la pelota está a 2 m de altura, su Ep y su Ec (usa la conservación) para comprobar que la suma se mantiene. Luego escribe una frase que explique por qué una pelota real llegaría con menos energía cinética.", "Ep inicial: 1 × 10 × 5 = 50 J. Ec final: 50 J. A 2 m: Ep = 20 J y Ec = 30 J; la suma es 50 J. Una pelota real llega con menos Ec porque el roce transforma parte de la energía en calor.", ["calcula Ep y Ec correctamente", "muestra que la suma se mantiene", "explica la pérdida con el roce"], ["tres cálculos y una frase"], ["no multiplicar por g", "decir que la energía desaparece"], "Pregunta cómo medirías el efecto del roce."),
  reinforce="Calcula la Ep de un objeto de 2 kg a 7 m de altura.",
  extend="Explica por qué el modelo de conservación es ideal y en qué casos se puede usar.")

L(OA11, 4,
  materials="Este cuaderno y lápiz. Para investigar en casa: una pelota de goma y una rampa de cartón; las alturas pequeñas se miden con una huincha. Los datos de los ejercicios están escritos.",
  use="Aprenderé a relacionar altura, velocidad y energía con la conservación de la energía mecánica, y a relacionar el trabajo neto con el cambio de la energía cinética.",
  prior=["Sé calcular Ep y Ec.", "Sé qué es el trabajo."],
  explain=[
      "En una caída sin roce, toda la energía potencial se transforma en cinética: m × g × h = ½ × m × v². La masa se simplifica, así que v × v = 2 × g × h. Con g = 10 queda v × v = 20 × h. Por ejemplo, desde h = 5 m se obtiene v × v = 100, y como 10 × 10 = 100, la velocidad es 10 m/s. Aquí v es el número que, multiplicado por sí mismo, da el resultado.",
      "Esta relación muestra que la velocidad final no depende de la masa y que crece con la altura, pero no en proporción directa: al cuadruplicar la altura, la velocidad solo se duplica. Además, el trabajo neto sobre un objeto es igual al cambio de su energía cinética. Si parte del reposo, el trabajo neto es igual a la energía cinética final.",
      "Para investigar estas relaciones se suelta una pelota de goma por una rampa desde distintas alturas pequeñas y se mide el tiempo en un tramo plano. Se cambia solo la altura, se controlan la rampa y la pelota y se repite cada medición. Los resultados reales dan velocidades algo menores que las calculadas, por el roce.",
  ],
  vocab=[("v × v", "velocidad multiplicada por sí misma"), ("trabajo neto", "trabajo de la fuerza neta sobre el objeto"), ("cambio de energía cinética", "Ec final menos Ec inicial"), ("relación no proporcional", "al multiplicar una variable por 4, la otra no se multiplica por 4"), ("variable independiente", "la que se cambia a propósito")],
  worked=[
      ("Velocidad desde la altura", "Un objeto cae sin roce desde 20 m (g = 10 m/s²). ¿Con qué velocidad llega al suelo?", ["v × v = 20 × 20 = 400.", "20 × 20 = 400, así que v = 20 m/s."], "20 m/s"),
      ("Trabajo neto y energía cinética", "Una fuerza neta de 25 N empuja 5 m a un objeto de 10 kg que parte del reposo, sobre una superficie lisa. ¿Qué velocidad alcanza?", ["Trabajo neto: 25 × 5 = 125 J, que es la Ec final.", "½ × 10 × v × v = 125, es decir, v × v = 25 y v = 5 m/s."], "5 m/s"),
  ],
  mistakes=[
      ("Creer que un objeto más pesado cae con más velocidad final.", "En el modelo sin roce la masa se simplifica en la ecuación.", "Escribe m × g × h = ½ × m × v² y simplifica la masa."),
      ("Pensar que al duplicar la altura se duplica la velocidad.", "Se duplica v × v, por lo que la velocidad crece menos.", "Calcula v × v primero y luego busca v."),
  ],
  rec=[
      ("Verdadero o falso: sin roce, la velocidad final de una caída no depende de la masa.", "Verdadero", "La masa se simplifica en la ecuación."),
      ("Si v × v = 100, ¿cuánto vale v?", "10", "10 × 10 = 100."),
      ("Verdadero o falso: sin roce, la energía potencial que se pierde es igual a la energía cinética que se gana.", "Verdadero", "Es la conservación de la energía mecánica."),
  ],
  und=[
      ("Si se cuadruplica la altura de caída, ¿qué pasa con la velocidad final? A) Se duplica; B) Se cuadruplica.", "A", "Se cuadruplica v × v, y la velocidad se duplica."),
      ("Si v × v = 400, ¿cuánto vale v? A) 20; B) 200.", "A", "20 × 20 = 400."),
      ("Un objeto parte del reposo y el trabajo neto sobre él es 50 J. ¿Cuál es su energía cinética final?", "50 J", "El trabajo neto es igual al cambio de energía cinética."),
  ],
  app=[
      arith("Un objeto cae sin roce desde 45 m. ¿Cuánto vale v × v? (v × v = 20 × h).", "20*45", "Se multiplica 20 por la altura.", ""),
      ("Con v × v = 900, ¿cuál es la velocidad en m/s?", "30 m/s", "30 × 30 = 900."),
      arith("Una fuerza neta de 30 N actúa 4 m sobre un objeto que parte del reposo en una superficie lisa. ¿Cuál es su energía cinética final?", "30*4", "El trabajo neto pasa a energía cinética.", " J"),
  ],
  rea=[
      ("Dos pelotas, de 1 kg y de 3 kg, se sueltan desde 5 m sin roce. ¿Cuál llega con mayor velocidad? A) Llegan con la misma velocidad; B) La de 3 kg llega más rápido.", "A", "La masa se simplifica en el modelo."),
      ("Un estudiante dice: «Si duplico la altura, duplico la velocidad». ¿Qué le respondes? A) Es falso: se duplica v × v y la velocidad crece menos que el doble; B) Es verdadero, son proporcionales.", "A", "v × v = 20 × h, así que v aumenta menos que h."),
  ],
  cha=[
      ("Un objeto cae sin roce desde 80 m (g = 10 m/s²). ¿Con qué velocidad llega al suelo?", "40 m/s", "v × v = 20 × 80 = 1.600 y 40 × 40 = 1.600."),
      arith("Una pelota de 2 kg cae desde 5 m. El modelo predice 10 m/s, pero se midieron 9 m/s. ¿Cuántos joules de Ec faltan respecto del modelo?", "2*10*10//2-2*9*9//2", "Con el modelo Ec = 100 J; con lo medido Ec = 81 J.", " J"),
  ],
  context=[arith("Una persona empuja un carro de 10 kg que parte del reposo con una fuerza neta de 20 N durante 5 m sobre un piso liso (dato de ejemplo). ¿Cuál es la energía cinética final?", "20*5", "El trabajo neto pasa a energía cinética.", " J")],
  selfcheck=[("¿Qué ecuación relaciona la velocidad final con la altura de caída sin roce?", "v × v = 2 × g × h", "Sale de igualar Ep y Ec."), ("¿Por qué la masa no afecta la velocidad final en el modelo?", "Porque se simplifica", "Aparece en Ep y en Ec."), ("¿Qué es igual al trabajo neto?", "El cambio de la energía cinética", "Es la relación entre trabajo y energía.")],
  open_task=task("Datos de ejemplo de una investigación con una pelota que baja por una rampa lisa. Alturas de salida: 5 m, 20 m y 45 m (valores de ejemplo para el modelo). Calcula v × v y la velocidad ideal para cada altura. Luego escribe cuál sería la variable independiente, cuál la dependiente y una razón por la que la velocidad medida sería menor.", "Alturas 5, 20 y 45 m dan v × v de 100, 400 y 900, es decir 10, 20 y 30 m/s. Independiente: altura; dependiente: velocidad; controladas: la pelota y la rampa. Mediría menos por el roce y por errores al medir el tiempo.", ["calcula bien las tres velocidades", "nombra las variables", "explica la diferencia con el roce"], ["tres cálculos y una explicación"], ["pensar que la velocidad es proporcional a la altura", "no nombrar variables"], "Pregunta qué alturas reales usarías en casa."),
  reinforce="Calcula v × v para una caída desde 10 m sin roce.",
  extend="Explica por qué cuadruplicar la altura solo duplica la velocidad final.")
