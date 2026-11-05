"""Cuaderno del estudiante, 2.º medio Ciencias Naturales: OA 12 (impulso, momentum y colisiones), OA 13 (modelos del Universo) y OA 14 (gravitación, leyes de Kepler y estructuras cósmicas)."""
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


OA12 = "CN2M OA 12"
OA13 = "CN2M OA 13"
OA14 = "CN2M OA 14"
MAT = "Este cuaderno y lápiz. Todos los datos están escritos en el cuaderno; no necesitas salir de tu casa."

# ================================================================ OA 12

L(OA12, 1,
  materials=MAT,
  use="Aprenderé qué es la cantidad de movimiento (momentum), cómo se calcula y cómo escribir una pregunta que se pueda investigar sobre choques. Sirve para comparar el efecto de choques distintos con números y no con impresiones.",
  prior=["Sé que la rapidez y la masa se pueden medir.", "Sé que una pregunta investigable indica qué se mide y qué se compara."],
  explain=[
      "La cantidad de movimiento, o momentum, de un cuerpo es el producto de su masa por su velocidad: p = m · v. Se mide en kilogramos por metro sobre segundo (kg·m/s). Un cuerpo detenido tiene momentum cero. A igual velocidad, el cuerpo de mayor masa tiene más momentum, y a igual masa, el de mayor velocidad tiene más.",
      "El momentum es una magnitud vectorial: además de su valor tiene dirección y sentido, que son los mismos de la velocidad. Si un cuerpo va hacia la derecha, su momentum apunta hacia la derecha. Por eso un cuerpo liviano y muy rápido puede tener más momentum que uno pesado y lento: una pelota de 1 kg a 20 m/s supera a un bloque de 10 kg a 1 m/s.",
      "Para investigar choques conviene una pregunta que nombre lo que se cambia y lo que se mide. «¿Qué choque es más emocionante?» depende de la opinión de cada persona. «¿Cuántos centímetros se desplaza un vaso plástico al ser golpeado por una bolita liviana y por una pesada que bajan por la misma rampa?» se contesta con una regla.",
  ],
  vocab=[("momentum", "producto de la masa por la velocidad de un cuerpo"), ("magnitud vectorial", "magnitud que tiene valor, dirección y sentido"), ("kg·m/s", "unidad del momentum"), ("variable", "dato que se cambia o se mide en una investigación")],
  worked=[
      ("Calcular un momentum", "Un carrito de 4 kg se mueve a 5 m/s hacia la derecha. ¿Cuál es su momentum?", ["Escribo la fórmula: p = m · v.", "Reemplazo: p = 4 kg · 5 m/s.", "Multiplico y agrego la unidad y el sentido."], "20 kg·m/s hacia la derecha"),
      ("Mejorar una pregunta", "Mejora la pregunta «¿Qué choque de bolitas es más bonito?» para que se pueda investigar.", ["Quito la palabra de opinión: «bonito».", "Indico qué se mide: los centímetros que se desplaza un vaso plástico después del golpe.", "Indico qué se compara: una bolita liviana y una pesada soltadas desde la misma altura de la rampa."], "«¿Se desplaza más un vaso plástico golpeado por una bolita pesada que por una liviana soltadas desde la misma altura?»"),
  ],
  mistakes=[
      ("Calcular el momentum con la masa o con la velocidad sola.", "El momentum necesita las dos magnitudes multiplicadas.", "Escribe siempre p = m · v antes de reemplazar."),
      ("Decir que un cuerpo muy liviano nunca tiene más momentum que uno pesado.", "Si la velocidad es mucho mayor, el producto puede ser mayor.", "Calcula los dos productos y compáralos."),
  ],
  rec=[
      ("¿Qué magnitud se calcula multiplicando la masa por la velocidad de un cuerpo?", "Cantidad de movimiento (momentum)", "p = m · v."),
      ("¿Qué letra se usa para el momentum en la fórmula p = m · v?", "p", "La fórmula del momentum se escribe con la letra p."),
      ("Verdadero o falso: un cuerpo detenido tiene momentum igual a cero.", "Verdadero", "Su velocidad es 0 y el producto m · v también."),
  ],
  und=[
      ("Dos cuerpos van a la misma velocidad. ¿Cuál tiene más momentum? A) El de mayor masa; B) El de menor masa.", "A", "Con la misma velocidad, el producto crece con la masa."),
      ("Un cuerpo va hacia la derecha. ¿Hacia dónde apunta su momentum? A) Hacia la derecha; B) Hacia la izquierda.", "A", "El momentum tiene el mismo sentido que la velocidad."),
      ("¿Qué unidad corresponde al momentum? A) kg·m/s; B) m/s².", "A", "Es masa en kg por velocidad en m/s."),
  ],
  app=[
      arith("Un balón de ejemplo de 6 kg rueda a 7 m/s. ¿Cuántos kg·m/s de momentum tiene?", "6*7", "Se multiplica la masa por la velocidad.", " kg·m/s"),
      arith("Una bicicleta con su ciclista suma 60 kg y avanza a 5 m/s. ¿Cuál es su momentum en kg·m/s?", "60*5", "Se usa la masa total del sistema por la velocidad.", " kg·m/s"),
      arith("Un carrito de 6 kg tiene un momentum de 24 kg·m/s. ¿A qué velocidad, en m/s, se mueve?", "24//6", "La velocidad es el momentum dividido por la masa.", " m/s"),
  ],
  rea=[
      ("Una pelota de 2 kg va a 15 m/s y un bloque de 10 kg va a 2 m/s. ¿Cuál tiene más momentum? Responde «pelota» o «bloque».", "Pelota", "La pelota tiene 30 kg·m/s y el bloque 20 kg·m/s."),
      ("¿Cuál es una pregunta investigable sobre momentum? A) ¿Cuántos centímetros retrocede un carrito liviano al ser golpeado por otro, según la masa del que golpea?; B) ¿Qué choque es más emocionante?", "A", "Indica qué se mide y qué se compara; la otra depende de la opinión."),
  ],
  cha=[
      ("Una patinadora de 50 kg y un patinador de 60 kg tienen el mismo momentum. ¿Quién va más rápido?", "La patinadora de 50 kg", "Con igual producto m · v, la menor masa exige mayor velocidad."),
      arith("Un carrito de 3 kg va a 8 m/s y otro de 4 kg va a 6 m/s. ¿Cuántos kg·m/s de diferencia hay entre sus momentum?", "3*8-4*6", "Ambos productos valen 24, así que la diferencia es 0.", " kg·m/s"),
  ],
  context=[arith("En un riel de ejemplo, un carrito de 2 kg avanza a 9 m/s. ¿Cuál es su momentum en kg·m/s?", "2*9", "Se multiplica masa por velocidad.", " kg·m/s")],
  selfcheck=[("¿Cómo se calcula el momentum?", "Multiplicando la masa por la velocidad", "p = m · v."), ("¿Qué tiene un momentum además de su valor?", "Dirección y sentido", "Es una magnitud vectorial."), ("¿Qué hace investigable una pregunta sobre un choque?", "Que indica qué se mide y qué se compara", "Así se puede contestar con datos.")],
  open_task=task("Imagina esta investigación: una bolita liviana y una pesada bajan por la misma rampa de cartón y golpean un vaso plástico vacío. Escribe la pregunta investigable completa, indica qué cambias, qué mides con una regla y qué mantienes igual. Añade una predicción con su razón usando la palabra momentum.", "Pregunta: «¿Se desplaza más el vaso al ser golpeado por la bolita pesada?». Cambio: la masa de la bolita. Mido: centímetros de desplazamiento. Mantengo: altura de la rampa y el mismo vaso. Predicción: se desplazará más con la pesada porque tiene más momentum.", ["la pregunta indica qué se mide", "separa lo que cambia de lo que se mantiene", "la predicción usa el momentum"], ["pregunta, tres variables y predicción"], ["no mantener igual la altura de la rampa", "predecir sin dar una razón"], "Pregunta cómo cambiaría tu predicción si la bolita liviana fuera mucho más rápida."),
  reinforce="Calcula el momentum de tres objetos de tu casa usando masas y velocidades que inventes y rotula «de ejemplo».",
  extend="Explica por qué dos cuerpos con masas muy distintas pueden tener el mismo momentum.")

L(OA12, 2,
  materials=MAT,
  use="Aprenderé qué es el impulso, cómo se calcula con fuerza y tiempo y cómo se relaciona con el cambio de momentum. Sirve para leer datos y gráficos de choques.",
  prior=["Sé calcular el momentum con p = m · v.", "Sé que la fuerza se mide en newton (N)."],
  explain=[
      "El impulso es el efecto de una fuerza que actúa durante un tiempo: I = F · t. Se mide en newton por segundo (N·s). Si la misma fuerza actúa más tiempo, el impulso es mayor. El impulso tiene la dirección y el sentido de la fuerza.",
      "El impulso que recibe un cuerpo es igual al cambio de su momentum: I = Δp, donde Δp es el momentum final menos el inicial. Por eso N·s equivale a kg·m/s. Si un carrito de masa m cambia su velocidad de v1 a v2, el cambio de momentum es Δp = m · (v2 − v1).",
      "En un gráfico de fuerza contra tiempo, el impulso es el área bajo la línea. Si la fuerza es constante, el área es un rectángulo de altura F y base t. Si el sentido se invierte, se usa un signo menos: pasar de 4 m/s hacia la derecha a 4 m/s hacia la izquierda es pasar de +4 a −4 m/s.",
  ],
  vocab=[("impulso", "fuerza multiplicada por el tiempo en que actúa"), ("N·s", "unidad del impulso, igual a kg·m/s"), ("Δp", "cambio de momentum: momentum final menos inicial"), ("área bajo la línea", "en un gráfico fuerza-tiempo, representa el impulso")],
  worked=[
      ("Impulso de una fuerza constante", "Una fuerza de 10 N empuja un carrito durante 3 s. ¿Qué impulso recibe?", ["Escribo I = F · t.", "Reemplazo: I = 10 N · 3 s.", "Multiplico y agrego la unidad."], "30 N·s"),
      ("Cambio de momentum", "Un carrito de 2 kg pasa de 1 m/s a 4 m/s en línea recta. ¿Cuánto cambia su momentum?", ["Momentum inicial: 2 · 1 = 2 kg·m/s.", "Momentum final: 2 · 4 = 8 kg·m/s.", "Resto: 8 − 2."], "Δp = 6 kg·m/s, que es el impulso recibido"),
  ],
  mistakes=[
      ("Sumar la fuerza y el tiempo.", "El impulso es el producto F · t, no la suma.", "Multiplica y revisa que la unidad sea N·s."),
      ("Olvidar el signo cuando el cuerpo invierte su sentido.", "El momentum cambia más si el sentido se invierte.", "Elige un sentido positivo y usa el signo menos para el contrario."),
  ],
  rec=[
      ("¿Qué unidad se usa para el impulso?", "N·s", "Es fuerza en newton por tiempo en segundos."),
      ("¿Qué dos magnitudes se multiplican para obtener el impulso?", "La fuerza y el tiempo", "I = F · t."),
      ("Verdadero o falso: el impulso que recibe un cuerpo es igual al cambio de su momentum.", "Verdadero", "I = Δp."),
  ],
  und=[
      ("La misma fuerza actúa 2 s sobre un carrito y 5 s sobre otro idéntico. ¿Cuál recibe mayor impulso? A) El que recibe 5 s; B) El que recibe 2 s.", "A", "A igual fuerza, más tiempo da más impulso."),
      ("¿Con qué otra magnitud es igual el impulso recibido por un cuerpo? A) Con el cambio de su momentum; B) Con su masa.", "A", "I = Δp."),
      ("Un impulso de 20 N·s actúa sobre un carrito detenido en línea recta. ¿Qué ocurre con su momentum? A) Aumenta en 20 kg·m/s; B) Se mantiene en cero.", "A", "El impulso es igual al cambio de momentum."),
  ],
  app=[
      arith("Una fuerza de 15 N actúa 4 s sobre una caja. ¿Qué impulso recibe en N·s?", "15*4", "Se multiplica la fuerza por el tiempo.", " N·s"),
      arith("Un carrito de 5 kg pasa de 2 m/s a 6 m/s. ¿Cuántos kg·m/s cambia su momentum?", "5*(6-2)", "Se multiplica la masa por el cambio de velocidad.", " kg·m/s"),
      arith("Un carrito recibe un impulso de 48 N·s mientras actúa una fuerza constante durante 6 s. ¿Cuántos newton vale la fuerza?", "48//6", "La fuerza es el impulso dividido por el tiempo.", " N"),
  ],
  rea=[
      ("Ensayo A: fuerza de 10 N durante 2 s. Ensayo B: fuerza de 5 N durante 6 s. ¿Cuál ensayo da mayor impulso? Responde «A» o «B».", "B", "A da 20 N·s y B da 30 N·s."),
      ("En un gráfico de ejemplo la fuerza vale 5 N constante entre 0 y 4 s. Un estudiante calcula 5 + 4 = 9 N·s. ¿Qué error cometió? A) Sumó en vez de multiplicar la fuerza por el tiempo; B) Usó mal la unidad de masa.", "A", "El impulso es el área del rectángulo, 5 · 4 = 20 N·s."),
  ],
  cha=[
      arith("Una pelota de 1 kg llega a 10 m/s hacia la derecha y rebota a 10 m/s hacia la izquierda. Con la derecha positiva, ¿cuántos kg·m/s cambia su momentum?", "1*(-10-10)", "Pasa de +10 a −10 m/s, un cambio de −20 m/s multiplicado por 1 kg.", " kg·m/s"),
      arith("Una fuerza de 6 N actúa 2 s y luego una fuerza de 2 N actúa 3 s en el mismo sentido. ¿Qué impulso total recibe el cuerpo en N·s?", "6*2+2*3", "Se calcula cada rectángulo y se suman.", " N·s"),
  ],
  context=[arith("Una persona empuja un carrito de compras de ejemplo con 9 N durante 7 s. ¿Qué impulso entrega en N·s?", "9*7", "Se multiplica la fuerza por el tiempo.", " N·s")],
  selfcheck=[("¿Cómo se calcula el impulso de una fuerza constante?", "Multiplicando la fuerza por el tiempo", "I = F · t."), ("¿Con qué es igual el impulso?", "Con el cambio de momentum", "I = Δp."), ("¿Qué representa el área bajo la línea de un gráfico fuerza-tiempo?", "El impulso", "Es F · t cuando la fuerza es constante.")],
  open_task=task("Datos de ejemplo de un carrito de 4 kg: ensayo 1, fuerza de 8 N durante 3 s; ensayo 2, fuerza de 6 N durante 5 s; ensayo 3, fuerza de 12 N durante 2 s. Ordena los ensayos de mayor a menor impulso mostrando los cálculos. Escribe una oración que diga qué ensayo cambia más la velocidad del carrito y por qué.", "Ensayo 1: 8 · 3 = 24 N·s; ensayo 2: 6 · 5 = 30 N·s; ensayo 3: 12 · 2 = 24 N·s. Mayor impulso: el ensayo 2, porque a igual masa el mayor impulso produce el mayor cambio de momentum y de velocidad.", ["calcula los tres impulsos", "ordena de mayor a menor", "relaciona el impulso con el cambio de velocidad"], ["tres cálculos, orden y una oración"], ["pensar que la fuerza mayor siempre da el mayor impulso", "olvidar la unidad N·s"], "Pregunta qué tiempo necesitaría el ensayo 3 para igualar al ensayo 2."),
  reinforce="Calcula tres impulsos distintos con fuerzas y tiempos enteros de tu elección y escribe su unidad.",
  extend="Explica con un ejemplo por qué una fuerza pequeña puede dar un impulso grande.")

L(OA12, 3,
  materials=MAT,
  use="Aprenderé el modelo de conservación del momentum: en un sistema aislado, el momentum total antes de un choque es igual al de después. Sirve para predecir velocidades sin conocer la fuerza.",
  prior=["Sé calcular momentum e impulso.", "Sé que una fuerza entre dos cuerpos actúa sobre ambos en sentidos opuestos."],
  explain=[
      "Un sistema aislado es un conjunto de cuerpos sobre el que no actúan fuerzas externas que cambien su movimiento. En él, el momentum total se conserva: la suma de los momentum antes de un choque es igual a la suma después. Un cuerpo puede perder momentum, pero otro lo gana.",
      "Esto ocurre porque, durante el choque, las dos fuerzas son de igual valor y sentido contrario y actúan el mismo tiempo. Los impulsos son opuestos y el cambio total es cero. Si los cuerpos quedan pegados, la velocidad final se calcula como el momentum total dividido por la masa total.",
      "El mismo modelo explica los empujones desde el reposo. Si dos patinadores parten detenidos, el momentum total inicial es cero. Al empujarse, salen en sentidos opuestos y sus momentum suman cero. El modelo tiene límites: si hay roce con el suelo, esa fuerza externa cambia el momentum total.",
  ],
  vocab=[("sistema aislado", "conjunto de cuerpos sin fuerzas externas que cambien su movimiento"), ("conservación", "una cantidad total no cambia en el tiempo"), ("choque inelástico", "choque en que los cuerpos quedan pegados o se deforman"), ("fuerza externa", "fuerza que viene de fuera del sistema")],
  worked=[
      ("Choque con cuerpos pegados", "Un carrito de 2 kg a 3 m/s choca con otro de 1 kg detenido y quedan pegados. ¿A qué velocidad siguen?", ["Momentum antes: 2 · 3 + 1 · 0 = 6 kg·m/s.", "Masa total: 2 + 1 = 3 kg.", "Velocidad: 6 ÷ 3."], "2 m/s"),
      ("Empujón desde el reposo", "Una patinadora de 60 kg sale a 3 m/s empujando a un patinador de 90 kg, ambos detenidos al inicio. ¿Con qué rapidez sale él?", ["Momentum total inicial: 0.", "La patinadora tiene 60 · 3 = 180 kg·m/s; él tiene el mismo valor en sentido opuesto.", "Rapidez de él: 180 ÷ 90."], "2 m/s en sentido opuesto"),
  ],
  mistakes=[
      ("Pensar que cada cuerpo conserva su propio momentum.", "Se conserva el total del sistema; cada cuerpo puede ganar o perder.", "Suma los momentum antes y después y compara los totales."),
      ("Aplicar el modelo cuando hay una fuerza externa grande, como el roce.", "El roce cambia el momentum total.", "Declara si el sistema es aislado antes de usar el modelo."),
  ],
  rec=[
      ("¿Qué nombre recibe un conjunto de cuerpos sobre el que no actúan fuerzas externas que cambien su movimiento?", "Sistema aislado", "En él se conserva el momentum total."),
      ("Verdadero o falso: en un sistema aislado, el momentum total antes del choque es igual al de después.", "Verdadero", "Es la conservación del momentum."),
      ("¿Cómo se llama el choque en que los cuerpos quedan pegados?", "Choque inelástico", "Se pegan o se deforman después de chocar."),
  ],
  und=[
      ("En un choque dentro de un sistema aislado, ¿qué se conserva? A) El momentum total; B) El momentum de cada cuerpo por separado.", "A", "Un cuerpo puede perder momentum y otro lo gana."),
      ("Dos carritos detenidos unidos por un resorte comprimido se sueltan. ¿Cuánto vale el momentum total antes y después? A) Cero antes y cero después; B) Cero antes y mayor que cero después.", "A", "Salen en sentidos opuestos y sus momentum se anulan."),
      ("Dos patinadores se empujan desde el reposo y uno sale hacia la derecha. ¿Hacia dónde sale el otro? A) Hacia la izquierda; B) Hacia la derecha.", "A", "El momentum total debe seguir siendo cero."),
  ],
  app=[
      arith("Un carrito de 3 kg a 4 m/s choca con otro de 3 kg detenido y quedan pegados. ¿A qué velocidad, en m/s, siguen?", "12//6", "El momentum 12 se reparte en 6 kg de masa total.", " m/s"),
      arith("Un carro de 5 kg va a 2 m/s y otro de 4 kg va a 3 m/s en el mismo sentido. ¿Cuántos kg·m/s suma su momentum total?", "5*2+4*3", "Se suman los dos productos masa por velocidad.", " kg·m/s"),
      arith("Un carrito de 3 kg a 8 m/s choca con otro de 6 kg detenido. El de 3 kg queda detenido. ¿A qué velocidad sale el de 6 kg, en m/s?", "24//6", "Todo el momentum de 24 kg·m/s pasa al carrito de 6 kg.", " m/s"),
  ],
  rea=[
      ("Un estudiante dice: «Si el carrito A pierde momentum en el choque, el momentum total desapareció». ¿Qué le respondes? A) El momentum que pierde A lo gana B y el total se conserva; B) Tiene razón, el momentum se gasta.", "A", "En un sistema aislado el total no cambia."),
      ("Dos carritos chocan sobre una mesa con mucho roce. ¿Por qué falla el modelo? A) Porque el roce es una fuerza externa que cambia el momentum total; B) Porque el roce aumenta la masa.", "A", "El sistema deja de ser aislado."),
  ],
  cha=[
      arith("Dos carritos detenidos con un resorte entre ellos se sueltan. El de 2 kg sale a 6 m/s hacia la izquierda. ¿A qué velocidad, en m/s, sale hacia la derecha el de 3 kg?", "2*6//3", "Los momentum son iguales y opuestos: 12 kg·m/s dividido por 3 kg.", " m/s"),
      arith("Un sistema aislado tiene 40 kg·m/s antes del choque. Después, un cuerpo tiene 25 kg·m/s en el mismo sentido. ¿Cuántos kg·m/s tiene el otro?", "40-25", "La suma después debe seguir siendo 40.", " kg·m/s"),
  ],
  context=[arith("Un vagón de ejemplo de 30 kg a 5 m/s se acopla con otro de 20 kg detenido. ¿A qué velocidad, en m/s, siguen juntos?", "30*5//50", "El momentum 150 se reparte en 50 kg.", " m/s")],
  selfcheck=[("¿Qué se conserva en un choque dentro de un sistema aislado?", "El momentum total", "La suma antes es igual a la suma después."), ("¿Cómo se calcula la velocidad de dos cuerpos que quedan pegados?", "Con el momentum total dividido por la masa total", "Es la conservación del momentum aplicada."), ("¿Qué puede romper la conservación del momentum total?", "Una fuerza externa, como el roce", "El sistema deja de estar aislado.")],
  open_task=task("Dibuja el esquema «antes» y «después» de este caso de ejemplo: un carrito de 4 kg a 3 m/s choca con otro de 2 kg detenido y quedan pegados. Calcula el momentum total antes, la masa total y la velocidad final. Escribe una limitación del modelo para una mesa real.", "Antes: 4 · 3 = 12 kg·m/s. Masa total: 6 kg. Velocidad final: 12 ÷ 6 = 2 m/s. Limitación: el roce de la mesa es una fuerza externa y frena a los carritos.", ["esquema antes y después", "calcula el momentum total y la velocidad", "declara una limitación del modelo"], ["dibujo y tres cálculos"], ["usar solo la masa de un carrito", "no declarar la limitación"], "Pregunta qué cambia si el segundo carrito también se mueve."),
  reinforce="Resuelve un choque de ejemplo con cuerpos pegados de tu elección usando enteros.",
  extend="Explica por qué el momentum total se conserva aunque cada cuerpo cambie de momentum.")

L(OA12, 4,
  materials="Este cuaderno y lápiz. Si quieres comprobarlo en casa: una pelota blanda, una toalla doblada y el suelo; suéltala siempre desde la misma altura baja y con una persona cerca.",
  use="Aprenderé cómo el tiempo de contacto cambia la fuerza de un choque cuando el cambio de momentum es el mismo. Sirve para entender cascos, cojines y flexionar las rodillas al caer.",
  prior=["Sé que I = F · t y que I = Δp.", "Sé distinguir qué se cambia, qué se mide y qué se mantiene en una investigación."],
  explain=[
      "Como I = F · t y I = Δp, la fuerza media de un choque es F = Δp ÷ t. Si el cambio de momentum es fijo, al aumentar el tiempo de contacto la fuerza media disminuye. Si el tiempo se duplica, la fuerza baja a la mitad; si se triplica, a la tercera parte.",
      "Esto explica objetos de seguridad. Un casco, un cojín o un colchón alargan el tiempo en que el cuerpo se detiene y bajan la fuerza sobre él. Al caer, flexionar las rodillas hace lo mismo. El cambio de momentum es igual, pero la fuerza es menor.",
      "Para comprobarlo se compara una pelota soltada desde la misma altura sobre una superficie dura y sobre una toalla doblada. Se cambia la superficie, se mide la altura del rebote o el sonido del golpe y se mantienen iguales la pelota y la altura. Un cojín no reduce el impulso necesario para detener: reduce la fuerza al alargar el tiempo.",
  ],
  vocab=[("fuerza media", "valor promedio de la fuerza durante un choque"), ("tiempo de contacto", "tiempo que dura el choque entre los cuerpos"), ("variable controlada", "dato que se mantiene igual para comparar bien"), ("F = Δp ÷ t", "fuerza media a partir del cambio de momentum y del tiempo")],
  worked=[
      ("Fuerza según el tiempo", "Un cuerpo debe cambiar su momentum en 40 kg·m/s. ¿Qué fuerza media se necesita si se detiene en 2 s y en 4 s?", ["Uso F = Δp ÷ t.", "Con 2 s: 40 ÷ 2 = 20 N.", "Con 4 s: 40 ÷ 4 = 10 N."], "20 N en 2 s y 10 N en 4 s: al doble de tiempo, la mitad de fuerza"),
      ("Detener una pelota", "Una pelota de 2 kg que llega a 5 m/s se detiene. ¿Qué fuerza media actúa si tarda 1 s y si tarda 5 s?", ["Cambio de momentum: 2 · 5 = 10 kg·m/s.", "Con 1 s: 10 ÷ 1 = 10 N.", "Con 5 s: 10 ÷ 5 = 2 N."], "10 N en 1 s y 2 N en 5 s"),
  ],
  mistakes=[
      ("Creer que un cojín reduce el cambio de momentum.", "El cambio de momentum necesario es el mismo.", "Un cojín alarga el tiempo y por eso baja la fuerza."),
      ("Cambiar dos variables a la vez al comparar superficies.", "No se sabe cuál produjo la diferencia.", "Cambia solo la superficie y mantén igual la pelota y la altura."),
  ],
  rec=[
      ("¿Qué fórmula da la fuerza media a partir del cambio de momentum y del tiempo?", "F = Δp ÷ t", "Sale de I = F · t y I = Δp."),
      ("Verdadero o falso: con el mismo cambio de momentum, más tiempo de contacto da menos fuerza media.", "Verdadero", "F = Δp ÷ t disminuye cuando t aumenta."),
      ("¿Qué variable aumenta un cojín al frenar un golpe?", "El tiempo de contacto", "Alarga el tiempo en que se detiene el cuerpo."),
  ],
  und=[
      ("¿Por qué conviene flexionar las rodillas al caer? A) Porque alarga el tiempo de frenado y baja la fuerza; B) Porque el cuerpo cambia menos su momentum.", "A", "El cambio de momentum es igual, pero la fuerza es menor."),
      ("En ensayos con el mismo cambio de momentum, al duplicar el tiempo de contacto la fuerza media A) se reduce a la mitad; B) se duplica.", "A", "F = Δp ÷ t es inversamente proporcional al tiempo."),
      ("¿Qué tiene en común un casco y un colchón? A) Alargan el tiempo del choque; B) Aumentan la velocidad del cuerpo.", "A", "Al alargar el tiempo bajan la fuerza sobre el cuerpo."),
  ],
  app=[
      arith("Un cambio de momentum de 60 kg·m/s ocurre en 5 s. ¿Qué fuerza media actúa, en newton?", "60//5", "Se divide el cambio de momentum por el tiempo.", " N"),
      arith("Con un cambio de momentum de 80 N·s, ¿cuántos newton vale la fuerza media si el choque dura 4 s?", "80//4", "F = Δp ÷ t.", " N"),
      arith("Una fuerza constante de 18 N actúa durante 5 s. ¿Cuántos N·s de impulso entrega?", "18*5", "El impulso es fuerza por tiempo.", " N·s"),
  ],
  rea=[
      ("Se suelta una pelota blanda desde una altura baja sobre el piso y luego sobre una toalla doblada para comparar el golpe. ¿Qué debe mantenerse igual? A) La pelota y la altura de caída; B) La superficie.", "A", "Solo debe cambiar la superficie; lo demás se controla."),
      ("Un compañero dice: «El cojín reduce el impulso». ¿Qué le respondes? A) El impulso necesario para detenerse es igual, el cojín baja la fuerza al alargar el tiempo; B) Tiene razón, el cojín elimina el impulso.", "A", "I = Δp no cambia, cambian F y t."),
  ],
  cha=[
      arith("Con el mismo cambio de momentum, el tiempo de contacto pasa de 2 s a 6 s. ¿Por qué factor se divide la fuerza media?", "6//2", "El tiempo se triplica, así que la fuerza baja a la tercera parte."),
      arith("Un cambio de momentum de 120 N·s debe frenarse con una fuerza máxima de 40 N. ¿Cuántos segundos como mínimo debe durar el frenado?", "120//40", "t = Δp ÷ F.", " s"),
  ],
  context=[arith("Un ciclista de ejemplo debe cambiar 100 N·s de momentum. ¿Cuántos newton menos actúan si frena en 5 s en vez de en 2 s?", "100//2-100//5", "Con 2 s la fuerza es 50 N y con 5 s es 20 N; la diferencia es 30 N.", " N")],
  selfcheck=[("¿Qué ocurre con la fuerza media si el tiempo de contacto aumenta y Δp es igual?", "Disminuye", "F = Δp ÷ t."), ("¿Por qué sirve un casco?", "Porque alarga el tiempo del golpe y baja la fuerza", "El cambio de momentum es igual pero dura más."), ("¿Qué se debe cambiar en una comparación justa?", "Solo una variable", "Así se sabe qué produjo la diferencia.")],
  open_task=task("Planifica una comparación segura: dejas caer una pelota blanda desde la misma altura baja sobre el piso y sobre una toalla doblada. Escribe la pregunta, qué cambias, qué mides y qué mantienes igual. Usa los datos de ejemplo «piso: el golpe dura 0,01 s; toalla: el golpe dura 0,03 s» para explicar con F = Δp ÷ t cuál superficie da menos fuerza.", "Pregunta: «¿Rebota más y suena más fuerte en el piso que en la toalla?». Cambio: la superficie. Mido: altura del rebote. Mantengo: pelota y altura. Con el mismo Δp, la toalla tarda más y por F = Δp ÷ t da menos fuerza.", ["pregunta con qué se mide", "una sola variable cambia", "usa F = Δp ÷ t"], ["pregunta, variables y explicación"], ["cambiar la pelota y la superficie a la vez", "decir que la toalla cambia el momentum"], "Pregunta qué otro objeto de seguridad se explica con la misma idea."),
  reinforce="Calcula la fuerza media de un cambio de momentum de 30 N·s si dura 1 s y si dura 3 s.",
  extend="Explica por qué un airbag y un cinturón se diseñan para alargar el tiempo de frenado.")

L(OA12, 5,
  materials=MAT,
  use="Aprenderé a explicar con evidencia la diferencia entre choques elásticos e inelásticos: el momentum se conserva siempre, la energía cinética no. Sirve para interpretar datos de colisiones.",
  prior=["Sé que el momentum total se conserva en un sistema aislado.", "Sé que una evidencia es un dato que apoya o contradice una explicación."],
  explain=[
      "La energía cinética es la energía que tiene un cuerpo por moverse: Ec = ½ · m · v², y se mide en joule (J). En un choque elástico se conservan el momentum total y la energía cinética total; los cuerpos rebotan sin deformarse de modo permanente. En un choque inelástico se conserva el momentum total, pero la energía cinética disminuye.",
      "La energía cinética que falta no desaparece: se transforma en deformación, sonido y calor. Si los cuerpos quedan pegados, es un choque inelástico. El choque elástico perfecto es un modelo: en la realidad siempre se pierde algo, aunque las bolas de billar se acercan bastante.",
      "Para decidir qué tipo de choque ocurrió se comparan los datos antes y después. Si el momentum total cambia, el sistema no era aislado o hay un error de medición. Si el momentum es igual y la energía cinética también, el choque fue elástico. Si el momentum es igual y la energía cinética bajó, fue inelástico.",
  ],
  vocab=[("energía cinética", "energía de un cuerpo por estar en movimiento"), ("joule (J)", "unidad de energía"), ("choque elástico", "choque en que se conservan el momentum y la energía cinética"), ("choque inelástico", "choque en que se conserva el momentum pero baja la energía cinética")],
  worked=[
      ("Choque con cuerpos pegados", "Un carrito de 2 kg a 4 m/s choca con otro de 2 kg detenido y quedan pegados. Compara la energía cinética antes y después.", ["Velocidad final: 8 ÷ 4 = 2 m/s.", "Antes: ½ · 2 · 4² = 16 J.", "Después: ½ · 4 · 2² = 8 J."], "Inelástico: pierde 8 J de energía cinética y conserva el momentum"),
      ("Clasificar con datos", "Dos bolas iguales chocan. Antes, una se mueve y la otra está detenida. Después, la primera queda detenida y la segunda sale con la misma rapidez. ¿Qué tipo de choque es?", ["El momentum total es igual antes y después.", "La energía cinética total también es igual porque las masas son iguales y la rapidez que sale es la misma.", "Se cumplen las dos conservaciones."], "Choque elástico"),
  ],
  mistakes=[
      ("Decir que en un choque inelástico el momentum no se conserva.", "El momentum total se conserva en cualquier choque de un sistema aislado.", "Revisa el momentum primero y la energía cinética después."),
      ("Decir que la energía cinética perdida desaparece.", "Se transforma en deformación, sonido y calor.", "Nombra en qué se transformó."),
  ],
  rec=[
      ("¿Qué unidad se usa para la energía?", "Joule", "Es la unidad de energía en el sistema internacional."),
      ("¿Qué tipo de choque conserva el momentum y la energía cinética?", "Elástico", "Es su definición."),
      ("Verdadero o falso: en un choque inelástico el momentum total de un sistema aislado no se conserva.", "Falso", "El momentum total se conserva en todo choque de un sistema aislado."),
  ],
  und=[
      ("En un choque inelástico, ¿qué ocurre con la energía cinética total? A) Disminuye; B) Aumenta.", "A", "Parte se transforma en deformación, sonido y calor."),
      ("Dos cuerpos chocan y quedan pegados. ¿Qué tipo de choque es? A) Inelástico; B) Elástico.", "A", "Al pegarse se pierde energía cinética."),
      ("¿En qué se transforma parte de la energía cinética perdida en un choque? A) En calor y sonido; B) En momentum.", "A", "La energía cambia de forma, no desaparece."),
  ],
  app=[
      arith("¿Cuántos joule de energía cinética tiene un carrito de 3 kg que va a 4 m/s? Usa Ec = ½ · m · v².", "3*4*4//2", "Se calcula la mitad de la masa por la velocidad al cuadrado.", " J"),
      arith("Un carrito de 1 kg a 6 m/s choca con otro de 1 kg detenido y quedan pegados. ¿A qué velocidad, en m/s, siguen?", "1*6//2", "El momentum 6 se reparte en 2 kg.", " m/s"),
      arith("En un choque de ejemplo la energía cinética antes es 18 J (1 kg a 6 m/s) y después 9 J (2 kg a 3 m/s). ¿Cuántos joule se transformaron?", "(1*6*6)//2-(2*3*3)//2", "Se restan las dos energías cinéticas.", " J"),
  ],
  rea=[
      ("Datos de ejemplo: momentum total antes 20 kg·m/s y después 20 kg·m/s. Energía cinética total antes 50 J y después 30 J. ¿Qué tipo de choque fue? A) Inelástico; B) Elástico.", "A", "El momentum se conservó y la energía cinética bajó."),
      ("Datos de ejemplo: momentum total antes 15 kg·m/s y después 9 kg·m/s en una mesa con mucho roce. ¿Cómo se explica? A) El roce es una fuerza externa que cambió el momentum total; B) Todos los choques inelásticos pierden momentum.", "A", "El sistema no estaba aislado."),
  ],
  cha=[
      ("Dos bolas iguales de 1 kg chocan. Antes, una va a 4 m/s y la otra está detenida. Después, la primera queda detenida y la otra sale a 4 m/s. ¿Qué tipo de choque es? A) Elástico; B) Inelástico.", "A", "Ec antes = ½ · 1 · 16 = 8 J y después también 8 J, además se conserva el momentum."),
      ("¿Por qué el momentum se conserva en un choque inelástico pero la energía cinética no? A) Porque las fuerzas del choque son iguales y opuestas y la energía cinética se transforma en otras formas; B) Porque la energía cinética no se puede medir.", "A", "Los impulsos se anulan, pero parte de la energía cambia de forma."),
  ],
  context=[arith("En un choque de ejemplo entre dos carritos la energía cinética total pasa de 50 J a 30 J. ¿Cuántos joule se transformaron en calor, sonido y deformación?", "50-30", "Se resta la energía final a la inicial.", " J")],
  selfcheck=[("¿Qué se conserva en un choque inelástico?", "El momentum total", "La energía cinética total baja."), ("¿Qué se conserva en un choque elástico?", "El momentum total y la energía cinética total", "Esa es su definición."), ("¿Adónde va la energía cinética que baja?", "Se transforma en deformación, sonido y calor", "No desaparece, cambia de forma.")],
  open_task=task("Con los datos de ejemplo: carrito A de 2 kg a 5 m/s choca con carrito B de 3 kg detenido y quedan pegados. Calcula el momentum total, la velocidad final y la energía cinética antes y después. Concluye si fue elástico o inelástico y qué evidencia lo apoya.", "Momentum: 10 kg·m/s. Velocidad final: 10 ÷ 5 = 2 m/s. Ec antes: ½ · 2 · 25 = 25 J. Ec después: ½ · 5 · 4 = 10 J. Fue inelástico porque el momentum se conservó y la energía cinética bajó 15 J.", ["calcula momentum y velocidad final", "compara la energía cinética", "concluye con la evidencia"], ["cuatro cálculos y una conclusión"], ["afirmar que se perdió momentum", "no usar los datos para concluir"], "Pregunta qué dato cambiaría la conclusión a elástico."),
  reinforce="Clasifica dos choques de ejemplo con tus propios datos: uno elástico y uno inelástico.",
  extend="Explica por qué el choque elástico perfecto es un modelo y no ocurre exactamente en la vida real.")

# ================================================================ OA 13

L(OA13, 1,
  materials=MAT,
  use="Aprenderé qué es un modelo del Universo, en qué se diferencian el modelo geocéntrico y el heliocéntrico y cómo plantear una pregunta que permita compararlos con observaciones.",
  prior=["Sé que un modelo es una representación que explica y predice.", "Sé que una pregunta investigable se contesta con observaciones."],
  explain=[
      "Un modelo del Universo es una representación que explica cómo se mueven los astros y permite predecir lo que veremos en el cielo. En el modelo geocéntrico, la Tierra está inmóvil al centro y el Sol, la Luna, los planetas y las estrellas giran a su alrededor. Ptolomeo lo desarrolló en la Antigüedad.",
      "En el modelo heliocéntrico, el Sol está al centro, y la Tierra y los demás planetas giran a su alrededor. Copérnico lo propuso en el siglo XVI. A simple vista, el geocéntrico parece natural: vemos que el Sol y las estrellas salen y se ponen, y no sentimos que la Tierra se mueva.",
      "Para comparar modelos se necesita una pregunta que nombre una observación que cada modelo pueda predecir. «¿Cuál era el modelo más inteligente?» no se puede investigar. «¿Qué modelo explica mejor que un planeta parezca retroceder por unas semanas entre las estrellas?» sí, porque se compara lo que predice cada modelo con lo observado. Nunca se debe mirar el Sol directamente ni con instrumentos.",
  ],
  vocab=[("modelo geocéntrico", "modelo con la Tierra inmóvil al centro"), ("modelo heliocéntrico", "modelo con el Sol al centro"), ("predicción", "lo que un modelo dice que se observará"), ("observación", "dato obtenido al mirar o medir un fenómeno")],
  worked=[
      ("Clasificar afirmaciones", "Clasifica con G (geocéntrico) o H (heliocéntrico): 1) «La Tierra y los planetas giran alrededor del Sol». 2) «El Sol gira alrededor de la Tierra inmóvil».", ["La afirmación 1 pone al Sol al centro.", "La afirmación 2 pone a la Tierra al centro e inmóvil."], "1 es H y 2 es G"),
      ("Mejorar una pregunta", "Mejora la pregunta «¿Cuál modelo del Universo era más inteligente?».", ["Quito la opinión: «inteligente».", "Elijo una observación que ambos modelos deben explicar: un planeta que parece retroceder entre las estrellas.", "Pregunto qué modelo la explica mejor."], "«¿Qué modelo explica mejor que Marte parezca retroceder por unas semanas entre las estrellas?»"),
  ],
  mistakes=[
      ("Pensar que el modelo geocéntrico era una idea absurda.", "Explicaba bien muchas observaciones de su época.", "Evalúa un modelo por las observaciones que explicaba entonces."),
      ("Confundir modelo con opinión.", "Un modelo se compara con observaciones; una opinión no.", "Pregunta qué observación podría contradecir el modelo."),
  ],
  rec=[
      ("¿Qué cuerpo está al centro en el modelo geocéntrico?", "La Tierra", "Geocéntrico quiere decir centrado en la Tierra."),
      ("¿Qué cuerpo está al centro en el modelo heliocéntrico?", "El Sol", "Heliocéntrico quiere decir centrado en el Sol."),
      ("Verdadero o falso: Copérnico propuso el modelo heliocéntrico.", "Verdadero", "Lo propuso en el siglo XVI."),
  ],
  und=[
      ("¿Por qué el modelo geocéntrico parecía natural a simple vista? A) Porque vemos salir y ponerse al Sol y no sentimos que la Tierra se mueva; B) Porque los telescopios lo demostraron.", "A", "Coincidía con lo que se percibe sin instrumentos."),
      ("¿Qué es una predicción de un modelo? A) Lo que el modelo dice que se observará; B) Una opinión sobre el modelo.", "A", "Se puede contrastar con la observación."),
      ("Según el modelo heliocéntrico, ¿qué ocurre con la Tierra? A) Gira alrededor del Sol; B) Está inmóvil al centro.", "A", "En ese modelo la Tierra es un planeta más."),
  ],
  app=[
      ("Clasifica con G (geocéntrico) o H (heliocéntrico): 1) «Los planetas giran alrededor del Sol». 2) «La Luna, el Sol y los planetas giran alrededor de la Tierra». 3) «La Tierra es un planeta que orbita». Responde con las tres letras en orden.", "H, G, H", "Se mira qué cuerpo se pone al centro en cada frase."),
      ("¿Cuál es una pregunta investigable? A) ¿Qué modelo predice que Marte parezca retroceder entre las estrellas durante unas semanas?; B) ¿Qué modelo del Universo es más bonito?", "A", "Nombra una observación que se puede comparar con las predicciones."),
      ("Una persona anota durante varias noches que un astro brillante cambia de posición entre las estrellas, que mantienen su patrón. ¿Es más probable que sea una estrella o un planeta? Responde con una palabra.", "Planeta", "Los planetas se desplazan entre las estrellas de fondo."),
  ],
  rea=[
      ("Un compañero dice: «El modelo geocéntrico estaba mal porque nadie observaba nada». ¿Qué le respondes? A) Se basaba en observaciones del cielo y predecía bien muchos movimientos; B) Tiene razón.", "A", "Se evalúa con las observaciones de su época."),
      ("Un modelo nuevo aparece. ¿Qué se debe hacer primero? A) Comparar sus predicciones con observaciones; B) Elegir el que más gente prefiere.", "A", "Los modelos se aceptan por su acuerdo con la evidencia."),
  ],
  cha=[
      ("Dos modelos predicen lo mismo en una observación. ¿Qué se necesita para elegir? A) Otra observación en la que sus predicciones sean distintas; B) Repetir la misma observación muchas veces.", "A", "Si predicen igual, esa observación no los distingue."),
      ("¿Por qué la sensación de que la Tierra no se mueve no prueba el modelo geocéntrico? A) Porque una percepción no es una medición que distinga entre modelos; B) Porque la Tierra sí se siente moverse.", "A", "Hace falta evidencia medible."),
  ],
  context=[("Un grupo anota en una semana de ejemplo que el Sol sale por un lado del horizonte y se pone por el otro. ¿Esta observación basta por sí sola para decidir entre los dos modelos? Responde «sí» o «no».", "No", "Ambos modelos la explican: la Tierra gira o el cielo gira.")],
  selfcheck=[("¿Qué diferencia hay entre el modelo geocéntrico y el heliocéntrico?", "En el primero la Tierra está al centro y en el segundo el Sol", "Es la posición del centro."), ("¿Qué es una predicción?", "Lo que un modelo dice que se observará", "Se compara con la observación."), ("¿Se debe mirar el Sol directamente?", "No", "Puede dañar la vista de forma permanente.")],
  open_task=task("Escribe una pregunta investigable que compare los dos modelos usando una de estas observaciones: A) Venus cambia de forma en el cielo como la Luna. B) Un planeta parece retroceder entre las estrellas durante unas semanas. Para tu pregunta indica qué predice cada modelo con tus palabras y qué observación ayudaría a decidir.", "Pregunta: «¿Qué modelo explica mejor que Marte parezca retroceder?». Geocéntrico: hay que añadir movimientos extra para explicarlo. Heliocéntrico: se explica porque la Tierra adelanta al planeta. Ayudaría observar su posición cada semana.", ["la pregunta nombra una observación", "indica la predicción de cada modelo", "propone qué observar"], ["pregunta y dos predicciones"], ["hacer una pregunta de opinión", "no distinguir entre los modelos"], "Pregunta qué observación nueva podría dar una pista a favor de uno."),
  reinforce="Dibuja el modelo geocéntrico y el heliocéntrico y rotula el centro de cada uno.",
  extend="Explica por qué un modelo antiguo puede ser útil aunque hoy se prefiera otro.")

L(OA13, 2,
  materials=MAT,
  use="Aprenderé a leer tablas de posiciones de un planeta y a reconocer el movimiento retrógrado aparente. Sirve para ver qué datos deben explicar los modelos del Universo.",
  prior=["Conozco los modelos geocéntrico y heliocéntrico.", "Sé leer tablas y calcular diferencias."],
  explain=[
      "Un planeta se observa entre las estrellas de fondo. Si se anota su posición cada semana, normalmente avanza en un sentido. Pero durante unas semanas parece detenerse, retroceder y luego avanzar de nuevo. A este retroceso aparente se le llama movimiento retrógrado.",
      "El modelo heliocéntrico lo explica de forma simple: la Tierra, que está en una órbita más cercana al Sol y se mueve más rápido, adelanta a un planeta exterior como Marte. Visto desde la Tierra, el planeta parece ir hacia atrás, como cuando un auto que adelantas parece retroceder. El planeta no cambia de sentido en el espacio.",
      "El modelo geocéntrico de Ptolomeo también lo explicaba, pero añadiendo círculos pequeños, llamados epiciclos, sobre los círculos grandes. Por eso un solo conjunto de posiciones no basta para elegir entre ambos. Las tablas de este cuaderno son datos de ejemplo, no mediciones reales.",
  ],
  vocab=[("movimiento retrógrado", "retroceso aparente de un planeta entre las estrellas"), ("posición angular", "ubicación del planeta en el cielo medida en grados"), ("epiciclo", "círculo pequeño que el modelo geocéntrico añadía para explicar el retroceso"), ("aparente", "que se ve así desde un punto de vista, aunque no ocurra realmente")],
  worked=[
      ("Leer una tabla", "Datos de ejemplo de la posición de Marte en grados, semanas 1 a 6: 100, 104, 107, 108, 106, 103. ¿Cuándo comienza el retroceso?", ["Hasta la semana 4 la posición aumenta de 100 a 108.", "En la semana 5 baja a 106.", "El retroceso comienza después del máximo de la semana 4."], "El retroceso aparente comienza en la semana 5"),
      ("Cuantificar el retroceso", "Con los mismos datos, ¿cuántos grados retrocede de la semana 4 a la 6?", ["Posición en la semana 4: 108 grados.", "Posición en la semana 6: 103 grados.", "Resto: 108 − 103."], "5 grados"),
  ],
  mistakes=[
      ("Decir que el planeta realmente da marcha atrás en el espacio.", "El retroceso es aparente y depende de la posición de la Tierra.", "Escribe «aparente» cuando hables del retroceso."),
      ("Creer que una tabla de datos prueba un modelo por sí sola.", "Ambos modelos pueden reproducirla.", "Busca una observación que los distinga."),
  ],
  rec=[
      ("¿Cómo se llama el retroceso aparente de un planeta entre las estrellas?", "Movimiento retrógrado", "Es un efecto de la perspectiva desde la Tierra."),
      ("Verdadero o falso: el movimiento retrógrado es aparente y el planeta no da marcha atrás en el espacio.", "Verdadero", "Se debe a que la Tierra adelanta al planeta."),
      ("¿Qué añadía el modelo geocéntrico para explicar el retroceso?", "Epiciclos", "Eran círculos pequeños sobre círculos grandes."),
  ],
  und=[
      ("Datos de ejemplo de un planeta en grados, semanas 1 a 7: 50, 53, 55, 54, 51, 49, 50. ¿En qué semana está la posición más alta?", "En la semana 3", "El valor 55 es el máximo de la tabla."),
      ("Con los mismos datos (50, 53, 55, 54, 51, 49, 50), ¿entre qué semanas disminuye la posición? A) Entre la semana 3 y la 6; B) Entre la semana 1 y la 3.", "A", "Baja de 55 a 49."),
      ("¿Qué modelo explica de forma simple el retroceso aparente porque la Tierra adelanta al planeta? A) El heliocéntrico; B) El geocéntrico sin círculos adicionales.", "A", "La Tierra y el planeta orbitan el Sol a distintas rapideces."),
  ],
  app=[
      arith("Con los datos de ejemplo 50, 53, 55, 54, 51, 49, 50 (semanas 1 a 7), ¿cuántos grados retrocede el planeta de la semana 3 a la 6?", "55-49", "Se resta la posición de la semana 6 a la de la semana 3.", " grados"),
      arith("Con los mismos datos, ¿cuántos grados avanzó el planeta de la semana 1 a la semana 3?", "55-50", "Se resta la posición inicial a la de la semana 3.", " grados"),
      arith("Otro planeta de ejemplo tuvo estas posiciones: 80, 84, 86, 85, 82. ¿Cuántos grados retrocedió desde su máximo hasta el último dato?", "86-82", "El máximo es 86 y el último dato es 82.", " grados"),
  ],
  rea=[
      ("Un estudiante dice que los datos prueban que Marte da marcha atrás en el espacio. ¿Qué le respondes? A) Los datos muestran un cambio aparente visto desde la Tierra, no prueban que dé marcha atrás; B) Tiene razón, el planeta cambia de sentido.", "A", "La perspectiva desde una Tierra en movimiento puede explicarlo."),
      ("Un solo conjunto de posiciones puede ser explicado por ambos modelos. ¿Qué conclusión es prudente? A) No basta para decidir y se necesita otra observación; B) Gana el heliocéntrico.", "A", "Sin una predicción distinta no se distingue."),
  ],
  cha=[
      arith("Datos de ejemplo en grados: 30, 34, 37, 39, 38, 35, 33, 34 (semanas 1 a 8). ¿Cuántas semanas pasan desde el máximo hasta el mínimo posterior?", "7-4", "El máximo está en la semana 4 y el mínimo posterior en la 7.", " semanas"),
      ("¿Por qué la tabla del movimiento retrógrado no basta para elegir un modelo? A) Porque ambos modelos pueden reproducir esos datos y hace falta otra observación; B) Porque los datos eran inexactos.", "A", "El geocéntrico lo explicaba con epiciclos."),
  ],
  context=[arith("Un planeta de ejemplo estaba en 62 grados y 4 semanas después en 70 grados, siempre avanzando. ¿Cuántos grados avanzó?", "70-62", "Se resta la posición inicial a la final.", " grados")],
  selfcheck=[("¿Qué es el movimiento retrógrado?", "El retroceso aparente de un planeta entre las estrellas", "Es un efecto visto desde la Tierra."), ("¿Cómo lo explica el modelo heliocéntrico?", "La Tierra adelanta al planeta", "Por eso parece retroceder."), ("¿Por qué no basta con esos datos para elegir modelo?", "Porque ambos modelos los pueden explicar", "Se necesita otra observación.")],
  open_task=task("Con los datos de ejemplo de un planeta (semanas 1 a 8, en grados): 40, 44, 47, 49, 48, 45, 43, 44, haz un gráfico de puntos de posición contra semana. Marca la semana de máxima posición y el tramo de retroceso. Escribe cuántos grados retrocede y una oración que explique el fenómeno con el modelo heliocéntrico.", "Máximo: semana 4 con 49 grados. Retroceso: de la semana 4 a la 7, de 49 a 43, es decir 6 grados. Explicación: la Tierra adelanta al planeta y por perspectiva parece retroceder.", ["el gráfico lleva ejes y puntos", "marca máximo y retroceso", "explica con el modelo heliocéntrico"], ["gráfico, cálculo y oración"], ["decir que el retroceso es real", "olvidar nombrar los ejes"], "Pregunta qué observación adicional ayudaría a elegir entre modelos."),
  reinforce="Escribe con tus palabras por qué parece que un auto retrocede cuando lo adelantas.",
  extend="Explica por qué «aparente» no significa «falso».")

L(OA13, 3,
  materials="Este cuaderno y lápiz. Nunca mires el Sol directamente ni con binoculares o telescopios. Toda observación del cielo se hace de noche y con una persona adulta cerca.",
  use="Aprenderé a contrastar el modelo geocéntrico y el heliocéntrico con evidencias como las observaciones de Galileo con telescopio. Sirve para entender cómo la evidencia hace cambiar un modelo.",
  prior=["Conozco los modelos geocéntrico y heliocéntrico.", "Sé que un modelo se evalúa por sus predicciones."],
  explain=[
      "Galileo usó el telescopio en el siglo XVII y observó hechos que el modelo geocéntrico simple no predecía. Vio cuatro lunas que giran alrededor de Júpiter: no todo gira alrededor de la Tierra. También vio que Venus muestra fases como la Luna, incluso casi llena, algo que el geocéntrico clásico no permitía.",
      "En el modelo heliocéntrico estas observaciones calzan con facilidad: las lunas de Júpiter orbitan su planeta, y Venus, que gira alrededor del Sol, puede verse iluminada de distintas formas desde la Tierra. Kepler propuso órbitas elípticas y Newton explicó el movimiento con la gravitación, lo que reforzó el modelo.",
      "Contrastar modelos significa comparar sus predicciones con la evidencia. Un modelo se descarta cuando sus predicciones fallan y no se puede ajustar sin volverlo muy complicado. La ciencia cambia de modelo por evidencia, no por autoridad: aunque un modelo sea muy aceptado, una observación nueva y repetible puede obligar a revisarlo.",
  ],
  vocab=[("fase de Venus", "cambio de la parte iluminada de Venus vista desde la Tierra"), ("evidencia", "dato u observación que apoya o contradice un modelo"), ("contrastar", "comparar lo que predice un modelo con lo observado"), ("telescopio", "instrumento que permite ver astros lejanos")],
  worked=[
      ("Contrastar con una observación", "Galileo observó lunas que giran alrededor de Júpiter. ¿Qué modelo se ve en problemas con esa evidencia y por qué?", ["El geocéntrico supone que todos los astros giran alrededor de la Tierra.", "Las lunas de Júpiter giran alrededor de otro planeta.", "Esa evidencia contradice la idea de que todo gira en torno a la Tierra."], "Afecta al geocéntrico simple: hay centros de giro distintos de la Tierra"),
      ("Tabla de predicciones", "Observación: Venus muestra fases casi llenas. Geocéntrico clásico: Venus se ve solo en fases delgadas. Heliocéntrico: Venus puede verse casi llena. ¿Qué modelo coincide con lo observado?", ["Comparo lo observado con cada predicción.", "El heliocéntrico predice fases casi llenas.", "El geocéntrico clásico predice solo fases delgadas."], "El heliocéntrico coincide con la observación"),
  ],
  mistakes=[
      ("Pensar que un modelo se acepta porque lo dice alguien importante.", "Un modelo se acepta por su acuerdo con la evidencia.", "Pregunta qué observación lo apoya."),
      ("Creer que una sola observación basta para cerrar toda la discusión.", "Se necesitan varias evidencias que coincidan y que otras personas puedan repetir.", "Reúne más de una observación."),
  ],
  rec=[
      ("¿Qué instrumento usó Galileo para observar las lunas de Júpiter y las fases de Venus?", "El telescopio", "Le permitió ver detalles invisibles a simple vista."),
      ("Verdadero o falso: las lunas de Júpiter giran alrededor de Júpiter y no de la Tierra.", "Verdadero", "Son evidencia de que hay otros centros de giro."),
      ("¿Qué científico propuso órbitas elípticas para los planetas?", "Kepler", "Sus leyes describen esas órbitas."),
  ],
  und=[
      ("¿Qué tienen en común las lunas de Júpiter y las fases de Venus? A) Son evidencias observadas con telescopio que desafían al geocéntrico simple; B) Son predicciones del geocéntrico simple.", "A", "El geocéntrico no las predecía."),
      ("¿Por qué las fases de Venus calzan con el heliocéntrico? A) Porque Venus orbita al Sol y se ve iluminado de distintas formas desde la Tierra; B) Porque Venus orbita la Tierra.", "A", "Su posición respecto del Sol y la Tierra cambia."),
      ("¿Qué significa contrastar un modelo? A) Comparar sus predicciones con la evidencia; B) Memorizar sus nombres.", "A", "Así se decide si el modelo describe lo observado."),
  ],
  app=[
      ("Clasifica con «apoya al heliocéntrico» o «no lo decide»: 1) Las lunas de Júpiter orbitan su planeta. 2) El Sol sale por el este cada día. Responde con las dos frases en orden.", "Apoya, no lo decide", "La primera contradice al geocéntrico simple y la segunda la explican ambos modelos."),
      ("Una tabla de ejemplo dice: observación X la explica solo el modelo 1, observación Y la explican ambos y observación Z la explica solo el modelo 1. ¿Qué modelo explica más observaciones? Responde «1» o «2».", "1", "Explica X, Y y Z, y el modelo 2 solo Y."),
      ("¿Qué dato permite distinguir entre dos modelos? A) Una observación en que sus predicciones sean distintas; B) Una observación en que ambos predicen lo mismo.", "A", "Solo una predicción distinta puede decidir."),
  ],
  rea=[
      ("Un compañero dice: «El modelo se cambió porque Galileo era famoso». ¿Qué le respondes? A) Se cambió porque las observaciones repetibles apoyaban otro modelo; B) Tiene razón.", "A", "La evidencia, no la fama, hace cambiar un modelo."),
      ("Una observación nueva contradice un modelo muy aceptado. ¿Qué es lo más científico? A) Revisar el modelo y repetir la observación; B) Ignorar la observación.", "A", "Los modelos se revisan con evidencia nueva."),
  ],
  cha=[
      ("¿Por qué las lunas de Júpiter no bastan para probar que la Tierra se mueve? A) Porque muestran que no todo gira alrededor de la Tierra, pero no dicen qué se mueve alrededor del Sol; B) Porque no son visibles.", "A", "Hacen falta más evidencias, como las fases de Venus."),
      ("¿Qué aporta Newton al modelo heliocéntrico? A) Una explicación de por qué los planetas orbitan, la gravitación; B) La invención del telescopio.", "A", "Dio un mecanismo físico para las órbitas."),
  ],
  context=[arith("Un cuadro de ejemplo evalúa 3 observaciones. El modelo A explica 1 y el modelo B explica las 3. ¿Cuántas observaciones más explica B que A?", "3-1", "Se resta lo que explica A a lo que explica B.")],
  selfcheck=[("¿Qué dos observaciones de Galileo cuestionaron el geocéntrico simple?", "Las lunas de Júpiter y las fases de Venus", "Ambas se vieron con telescopio."), ("¿Por qué cambia la ciencia de modelo?", "Por evidencia nueva", "No por autoridad."), ("¿Qué significa contrastar?", "Comparar predicciones con observaciones", "Así se evalúa un modelo.")],
  open_task=task("Completa una tabla de contraste con estas tres observaciones: (1) un planeta parece retroceder entre las estrellas, (2) Venus muestra fases casi llenas, (3) Júpiter tiene lunas que lo orbitan. Para cada una escribe qué predice el modelo geocéntrico simple y qué predice el heliocéntrico. Cierra con una conclusión de dos oraciones.", "(2) Geocéntrico simple: Venus solo en fases delgadas. Heliocéntrico: puede verse casi llena. Observado: casi llena. Conclusión: el heliocéntrico coincide con más observaciones; un modelo se elige por evidencia.", ["tres filas completas", "predicciones diferenciadas", "conclusión basada en evidencia"], ["tabla y conclusión"], ["escribir la misma predicción para ambos", "concluir por preferencia"], "Pregunta qué otra observación agregarías a la tabla."),
  reinforce="Escribe con tus palabras por qué el telescopio fue clave para contrastar los modelos.",
  extend="Explica por qué la ciencia acepta cambiar de modelo si aparece evidencia nueva.")

L(OA13, 4,
  materials=MAT,
  use="Aprenderé cómo la teoría del Big-Bang se apoya en evidencias, entre ellas que las galaxias se alejan más rápido mientras más lejos están. Sirve para ver cómo crece y cambia el conocimiento del Universo.",
  prior=["Sé que un modelo se contrasta con evidencias.", "Sé que dos magnitudes son proporcionales si su cociente es constante."],
  explain=[
      "La teoría del Big-Bang propone que el Universo se ha expandido a partir de un estado muy denso y muy caliente. No fue una explosión en un punto de un espacio ya existente: el espacio mismo se expande. En ciencia, una teoría es un conjunto de explicaciones que se ha puesto a prueba con muchas evidencias, no una simple suposición.",
      "Una evidencia es que la luz de las galaxias lejanas indica que se alejan de nosotros, y que mientras más lejos está una galaxia, mayor es su rapidez de alejamiento. Eso se parece a la ley de Hubble: la rapidez es proporcional a la distancia, v = k · d. Otra evidencia es una débil radiación llamada radiación cósmica de fondo, que llega desde todas partes y es un resto de la época caliente.",
      "El conocimiento del Universo aumenta con instrumentos mejores y datos nuevos, y puede cambiar. Para analizar una relación entre variables se calcula el cociente entre ellas. En las tablas de este cuaderno las unidades son de ejemplo, no mediciones reales.",
  ],
  vocab=[("Big-Bang", "teoría de que el Universo se expande desde un estado muy denso y caliente"), ("radiación cósmica de fondo", "radiación débil que llega desde todas direcciones del cielo"), ("proporcional", "que su cociente con otra magnitud es constante"), ("expansión", "aumento de las distancias entre galaxias lejanas")],
  worked=[
      ("Hallar la constante", "Tabla de ejemplo (distancia: rapidez de alejamiento): 10: 150, 20: 300, 30: 450. ¿Son proporcionales?", ["Calculo la rapidez ÷ distancia: 150 ÷ 10 = 15.", "300 ÷ 20 = 15 y 450 ÷ 30 = 15.", "El cociente es siempre el mismo."], "Sí, v = 15 · d"),
      ("Predecir un dato", "Con v = 15 · d, ¿qué rapidez se espera para una galaxia de ejemplo a distancia 50?", ["Escribo la relación: v = 15 · d.", "Reemplazo d = 50.", "Multiplico: 15 · 50."], "750 unidades de ejemplo"),
  ],
  mistakes=[
      ("Imaginar el Big-Bang como una explosión en un punto de un espacio vacío.", "Lo que se expande es el espacio mismo.", "Di «expansión del Universo» y no «explosión»."),
      ("Pensar que «teoría» significa «solo una suposición».", "Una teoría científica está respaldada por muchas evidencias.", "Pregunta qué evidencias la sostienen."),
  ],
  rec=[
      ("¿Cómo se llama la teoría que propone un Universo en expansión a partir de un estado muy denso y caliente?", "Big-Bang", "Es la teoría cosmológica más aceptada."),
      ("Verdadero o falso: según los datos, mientras más lejos está una galaxia, más rápido se aleja.", "Verdadero", "Es la relación entre rapidez y distancia."),
      ("¿Qué radiación llega débilmente desde todas direcciones y es un resto de la época caliente?", "La radiación cósmica de fondo", "Es una evidencia del Big-Bang."),
  ],
  und=[
      ("¿Qué significa que la rapidez de alejamiento sea proporcional a la distancia? A) Que su cociente es constante; B) Que son iguales.", "A", "La relación v = k · d tiene un cociente k fijo."),
      ("¿Qué se expande según el Big-Bang? A) El espacio mismo; B) Un punto en un espacio vacío.", "A", "No es una explosión en un lugar."),
      ("¿Para qué sirve la radiación cósmica de fondo? A) Es una evidencia de que el Universo fue muy caliente; B) Mide la rapidez con que se alejan las galaxias.", "A", "Es un resto de esa época."),
  ],
  app=[
      arith("Tabla de ejemplo: una galaxia a distancia 7 se aleja con rapidez 140. ¿Cuánto vale el cociente rapidez ÷ distancia?", "140//7", "Se divide la rapidez por la distancia.", ""),
      arith("Con v = 20 · d, ¿qué rapidez se espera para una galaxia de ejemplo a distancia 25?", "20*25", "Se multiplica la constante por la distancia.", ""),
      arith("Con v = 20 · d, ¿a qué distancia está una galaxia de ejemplo cuya rapidez es 360?", "360//20", "La distancia es la rapidez dividida por la constante.", ""),
  ],
  rea=[
      ("Un estudiante dice: «El Big-Bang fue una explosión en un lugar del espacio vacío». ¿Qué le respondes? A) La teoría habla de la expansión del espacio mismo, no de una explosión en un punto; B) Tiene razón.", "A", "Lo que aumenta es la distancia entre galaxias lejanas."),
      ("Tabla de ejemplo: 5: 100, 10: 200, 15: 300 (distancia: rapidez). ¿Qué relación se observa? A) A mayor distancia, mayor rapidez de alejamiento; B) La rapidez no cambia con la distancia.", "A", "Los tres cocientes valen 20."),
  ],
  cha=[
      ("Si todas las galaxias se alejaran con la misma rapidez sin importar su distancia, ¿se cumpliría la proporcionalidad? A) No, porque el cociente cambiaría con la distancia; B) Sí.", "A", "Con rapidez fija, el cociente baja al subir la distancia."),
      ("¿Por qué la ciencia sigue probando la teoría del Big-Bang aunque esté muy aceptada? A) Porque el conocimiento aumenta con datos nuevos y puede ajustarse; B) Porque nadie ha encontrado evidencia a su favor.", "A", "Las teorías se ponen siempre a prueba."),
  ],
  context=[arith("En una tabla de ejemplo, la galaxia P está a distancia 12 y la galaxia Q a distancia 30, con v = 10 · d. ¿Cuánto más rápido se aleja Q que P?", "10*30-10*12", "Se calcula la rapidez de cada una y se restan.")],
  selfcheck=[("¿Qué propone la teoría del Big-Bang?", "Un Universo en expansión desde un estado muy denso y caliente", "Es una teoría respaldada por evidencias."), ("Nombra una evidencia del Big-Bang.", "La radiación cósmica de fondo o el alejamiento de galaxias", "Ambas se observan."), ("¿Qué significa proporcional?", "Que el cociente entre las magnitudes es constante", "Por ejemplo v ÷ d.")],
  open_task=task("Con la tabla de ejemplo (distancia: rapidez de alejamiento) 4: 80, 8: 160, 12: 240 calcula el cociente de cada fila, escribe la relación v = k · d y predice la rapidez para distancia 20. Después escribe en dos oraciones qué evidencia apoya el Big-Bang y por qué una teoría puede cambiar con datos nuevos.", "Cocientes: 80 ÷ 4 = 20, 160 ÷ 8 = 20, 240 ÷ 12 = 20. Relación: v = 20 · d. Con d = 20, v = 400. Evidencia: el alejamiento de galaxias. Una teoría se ajusta cuando aparecen datos nuevos.", ["calcula los tres cocientes", "escribe la relación y predice", "nombra una evidencia"], ["tres cálculos, una predicción y dos oraciones"], ["restar en vez de dividir", "llamar «explosión» a la expansión del espacio"], "Pregunta qué pasaría con la predicción si el cociente fuera 25."),
  reinforce="Escribe la relación v = k · d con tus propios datos de ejemplo.",
  extend="Explica por qué se dice que el Universo no tiene un «centro» desde donde se expanda.")

# ================================================================ OA 14

L(OA14, 1,
  materials=MAT,
  use="Aprenderé la idea de gravitación universal de Newton: todos los cuerpos con masa se atraen, y la fuerza depende de las masas y de la distancia. Sirve para plantear preguntas sobre mareas, órbitas y satélites.",
  prior=["Sé que el peso es la fuerza con que la Tierra atrae un cuerpo.", "Sé que una pregunta investigable nombra algo que se puede medir."],
  explain=[
      "Según la ley de gravitación universal de Newton, dos cuerpos cualesquiera con masa se atraen con una fuerza. Esa fuerza es siempre de atracción y actúa en los dos cuerpos con el mismo valor y sentidos opuestos: la Tierra atrae a la Luna igual que la Luna atrae a la Tierra.",
      "La fuerza aumenta con las masas: si una masa se duplica, la fuerza se duplica. Y disminuye con la distancia, más rápido de lo que se podría pensar: si la distancia se duplica, la fuerza baja a la cuarta parte; si se triplica, baja a la novena parte. Por eso se dice que depende del cuadrado de la distancia.",
      "Con esta idea se pueden plantear preguntas investigables como «¿cómo cambia la fuerza de atracción entre dos cuerpos al duplicar la distancia?». «¿Por qué la gravedad es tan misteriosa?» no se puede investigar porque no indica qué medir. Los datos numéricos de este cuaderno son de ejemplo.",
  ],
  vocab=[("gravitación universal", "atracción mutua entre todos los cuerpos con masa"), ("masa", "cantidad de materia de un cuerpo"), ("cuadrado de la distancia", "la distancia multiplicada por sí misma"), ("fuerza de atracción", "fuerza que tiende a acercar dos cuerpos")],
  worked=[
      ("Cambiar la distancia", "La distancia entre dos cuerpos se hace 3 veces mayor. ¿Cómo cambia la fuerza de atracción?", ["Calculo el cuadrado del cambio de distancia: 3 · 3 = 9.", "La fuerza se divide por ese número.", "Queda la novena parte."], "La fuerza baja a 1/9 de su valor"),
      ("Mejorar una pregunta", "Mejora la pregunta «¿Por qué la gravedad es tan misteriosa?» para que se pueda investigar.", ["Quito la opinión: «misteriosa».", "Indico qué se mide: la fuerza de atracción.", "Indico qué se cambia: la distancia entre los cuerpos."], "«¿Cómo cambia la fuerza de atracción entre dos cuerpos al duplicar la distancia entre ellos?»"),
  ],
  mistakes=[
      ("Pensar que la gravedad solo la ejerce la Tierra.", "Todos los cuerpos con masa se atraen entre sí.", "Piensa en pares de cuerpos."),
      ("Creer que al duplicar la distancia la fuerza baja a la mitad.", "Baja a la cuarta parte porque depende del cuadrado de la distancia.", "Multiplica el cambio de distancia por sí mismo."),
  ],
  rec=[
      ("¿Cómo es siempre la fuerza gravitatoria entre dos cuerpos: de atracción o de repulsión?", "De atracción", "La gravitación solo atrae."),
      ("Verdadero o falso: la Tierra atrae a la Luna y la Luna atrae a la Tierra.", "Verdadero", "Es una atracción mutua."),
      ("Si una masa se duplica, ¿qué ocurre con la fuerza de atracción?", "Se duplica", "La fuerza aumenta en proporción a la masa."),
  ],
  und=[
      ("Si la distancia entre dos cuerpos se duplica, la fuerza de atracción A) baja a la cuarta parte; B) baja a la mitad.", "A", "Depende del cuadrado de la distancia."),
      ("La Tierra atrae a la Luna con una fuerza. ¿Cómo es la fuerza con que la Luna atrae a la Tierra? A) De igual valor y sentido opuesto; B) Mucho menor.", "A", "Las fuerzas entre dos cuerpos son de igual valor."),
      ("¿De qué dos cosas depende la fuerza de gravitación entre dos cuerpos? A) De sus masas y de la distancia entre ellos; B) De su color y su forma.", "A", "Esas son las variables de la ley de Newton."),
  ],
  app=[
      arith("La distancia entre dos cuerpos se hace 4 veces mayor. ¿Por cuánto se divide la fuerza de atracción?", "4*4", "Se multiplica el cambio de distancia por sí mismo."),
      ("Una de las dos masas se triplica y la distancia no cambia. ¿Por cuánto se multiplica la fuerza?", "3", "La fuerza es proporcional a la masa: si una masa se triplica, la fuerza se triplica."),
      ("¿Cuál es una pregunta investigable? A) ¿Cómo cambia la fuerza de atracción entre dos cuerpos cuando la distancia se hace 5 veces mayor?; B) ¿Es la gravedad lo más importante del Universo?", "A", "Indica qué se cambia y qué se mide."),
  ],
  rea=[
      ("Un estudiante dice: «Como la Tierra es enorme, atrae a un balón, pero el balón no atrae a la Tierra». ¿Qué le respondes? A) El balón también atrae a la Tierra con la misma fuerza, pero la Tierra casi no se mueve por su gran masa; B) Tiene razón.", "A", "Las dos fuerzas son iguales y opuestas."),
      ("¿Por qué la atracción entre dos personas no se nota? A) Porque sus masas son muy pequeñas y la fuerza es muy débil; B) Porque no existe atracción entre personas.", "A", "La fuerza existe, pero es minúscula."),
  ],
  cha=[
      arith("La distancia entre dos cuerpos pasa a ser 10 veces mayor. ¿Por cuánto se divide la fuerza?", "10*10", "Se multiplica 10 por 10."),
      ("Dos cuerpos se acercan hasta la mitad de la distancia inicial. ¿Qué pasa con la fuerza? A) Se multiplica por 4; B) Se multiplica por 2.", "A", "Con la mitad de distancia, el cuadrado inverso da 2 · 2 = 4."),
  ],
  context=[arith("Un satélite de ejemplo pasa de estar a una distancia del centro de la Tierra a estar al doble de esa distancia. ¿Por cuánto se divide la fuerza con que la Tierra lo atrae?", "2*2", "El doble de distancia da una fuerza cuatro veces menor.")],
  selfcheck=[("¿Cómo es la fuerza gravitatoria entre dos cuerpos?", "De atracción y mutua", "Actúa en ambos con el mismo valor."), ("¿Qué pasa con la fuerza si la distancia se duplica?", "Baja a la cuarta parte", "Depende del cuadrado de la distancia."), ("¿Qué pasa con la fuerza si una masa se duplica?", "Se duplica", "Es proporcional a la masa.")],
  open_task=task("Escribe una pregunta investigable sobre la gravitación que indique qué cambias y qué mides. Después completa esta tabla de ejemplo con los factores: distancia ×2 (fuerza ÷ ?), distancia ×3 (fuerza ÷ ?), una masa ×2 (fuerza × ?). Añade una oración que explique por qué dos personas no sienten atracción entre sí.", "Pregunta: «¿Cómo cambia la fuerza de atracción al triplicar la distancia?». Tabla: ×2: ÷4; ×3: ÷9; masa ×2: ×2. Dos personas tienen masas muy pequeñas y la fuerza es mínima.", ["la pregunta indica qué se mide", "los factores son correctos", "explica la atracción débil por la masa pequeña"], ["pregunta, tabla y oración"], ["dividir por 2 al duplicar la distancia", "negar que exista atracción entre personas"], "Pregunta qué pasaría con la fuerza si ambas masas se duplican."),
  reinforce="Escribe tres ejemplos de pares de cuerpos que se atraen por gravedad.",
  extend="Explica por qué la Luna también atrae a la Tierra aunque la Tierra tenga más masa.")

L(OA14, 2,
  materials=MAT,
  use="Aprenderé a leer tablas de distancia y período de planetas para reconocer que los más lejanos del Sol tardan más en dar una vuelta. Sirve para entender la tercera ley de Kepler de forma cualitativa.",
  prior=["Conozco la ley de gravitación universal.", "Sé leer tablas y comparar datos."],
  explain=[
      "El período orbital de un planeta es el tiempo que tarda en dar una vuelta completa alrededor del Sol. Kepler descubrió, a partir de observaciones, que los planetas más lejanos del Sol tienen períodos más largos. No solo recorren una órbita mayor, sino que además se mueven más lento.",
      "Para ver esto con datos se arma una tabla con la distancia al Sol y el período. Si al aumentar la distancia el período aumenta siempre, hay una relación creciente. Además, el período aumenta más rápido que la distancia: duplicar la distancia más que duplica el período.",
      "En este cuaderno se usan planetas inventados y unidades de ejemplo para no confundir con mediciones reales. Una tabla se lee comparando filas, calculando diferencias y ordenando de menor a mayor. Es útil escribir una frase que resuma la relación observada.",
  ],
  vocab=[("período orbital", "tiempo que tarda un astro en dar una vuelta a su órbita"), ("distancia orbital", "distancia media entre el planeta y el Sol"), ("relación creciente", "cuando una magnitud aumenta si la otra aumenta"), ("unidad de ejemplo", "unidad inventada para practicar sin datos reales")],
  worked=[
      ("Leer una tabla", "Tabla de ejemplo (planeta: distancia, período): A: 1, 1; B: 4, 8; C: 9, 27. ¿Cuál tarda más en dar una vuelta?", ["Miro la columna del período: 1, 8 y 27.", "El mayor valor es 27.", "Ese valor es del planeta C, que está más lejos."], "El planeta C"),
      ("Comparar el aumento", "Con la misma tabla, ¿cuánto aumenta el período de A a C?", ["Período de A: 1.", "Período de C: 27.", "Resto: 27 − 1."], "26 unidades de ejemplo"),
  ],
  mistakes=[
      ("Pensar que un planeta lejano tarda lo mismo que uno cercano porque recorre una órbita parecida.", "A mayor distancia el recorrido es mayor y la rapidez menor.", "Ordena la tabla según la distancia."),
      ("Confundir distancia con período al leer una tabla.", "Son columnas distintas con significados distintos.", "Subraya la columna que se te pide."),
  ],
  rec=[
      ("¿Cómo se llama el tiempo que tarda un planeta en dar una vuelta completa al Sol?", "Período orbital", "Es el tiempo de una órbita completa."),
      ("Verdadero o falso: los planetas más lejanos del Sol tienen períodos más largos.", "Verdadero", "Es el resultado que encontró Kepler."),
      ("¿Quién descubrió, a partir de observaciones, la relación entre distancia y período de los planetas?", "Kepler", "Sus tres leyes describen el movimiento planetario."),
  ],
  und=[
      ("Tabla de ejemplo (planeta: distancia, período): P: 16, 64; Q: 25, 125; R: 36, 216. ¿Cuál tarda más en dar una vuelta?", "R", "Su período es el mayor, 216."),
      ("Con la misma tabla, ¿qué planeta está más cerca del Sol? A) P; B) R.", "A", "Su distancia es la menor, 16."),
      ("Con la misma tabla, ¿cómo cambia el período al aumentar la distancia? A) Aumenta; B) Disminuye.", "A", "De 64 a 125 y a 216."),
  ],
  app=[
      arith("Con la tabla de ejemplo P: 16, 64; Q: 25, 125; R: 36, 216, ¿cuántas unidades más tarda R que P en dar una vuelta?", "216-64", "Se resta el período de P al de R.", " unidades"),
      arith("Con la misma tabla, ¿cuántas unidades de distancia hay entre P y R?", "36-16", "Se resta la distancia de P a la de R.", " unidades"),
      arith("Tabla de ejemplo: el planeta S está a distancia 49 y su período es 343. ¿Cuántas unidades más que R en período, que tiene 216?", "343-216", "Se resta el período de R al de S.", " unidades"),
  ],
  rea=[
      ("Un estudiante dice: «Si el planeta T está más lejos que Q, su período debe ser menor». ¿Qué le respondes? A) Es lo contrario: más lejos implica período mayor; B) Tiene razón.", "A", "La tabla muestra que el período crece con la distancia."),
      ("Un compañero dice que con solo tres planetas no se puede estar seguro de la relación. ¿Qué opinas? A) Tiene razón, mientras más datos concuerdan, más confianza hay; B) Tres datos son suficientes para siempre.", "A", "Más datos coincidentes dan más evidencia."),
  ],
  cha=[
      ("Con la tabla P: 16, 64; R: 36, 216, ¿qué aumentó en más unidades de P a R: la distancia o el período?", "El período", "Aumentó 152, mientras que la distancia aumentó 20."),
      ("Al comparar P (distancia 16) con otro planeta de ejemplo U (distancia 4, período 8), ¿cuál se mueve más rápido en su órbita? A) U, porque está más cerca; B) P, porque tiene mayor período.", "A", "Más cerca del Sol, mayor rapidez orbital."),
  ],
  context=[arith("En un sistema de ejemplo, una estrella tiene dos planetas con períodos de 50 y 120 unidades de ejemplo. ¿Cuántas unidades más tarda el segundo?", "120-50", "Se restan los dos períodos.", " unidades")],
  selfcheck=[("¿Qué es el período orbital?", "El tiempo de una vuelta completa", "Se mide en unidades de tiempo."), ("¿Cómo cambia el período al alejarse del Sol?", "Aumenta", "Los planetas lejanos tardan más."), ("¿Por qué los datos son de ejemplo?", "Para practicar sin confundirlos con mediciones reales", "Los números fueron inventados.")],
  open_task=task("Con la tabla de ejemplo (planeta: distancia, período) K: 1, 1; L: 4, 8; M: 9, 27; N: 16, 64, ordena los planetas por distancia, calcula cuánto aumenta el período de K a N y escribe una frase que resuma la relación entre distancia y período. Indica que los datos son de ejemplo.", "Orden por distancia: K, L, M, N. Aumento del período de K a N: 64 − 1 = 63. Frase: al aumentar la distancia, el período aumenta. Los datos son de ejemplo.", ["ordena por distancia", "calcula la diferencia", "resume la relación"], ["orden, cálculo y frase"], ["restar mal", "olvidar que son datos de ejemplo"], "Pregunta qué período esperarías para un planeta más lejano que N."),
  reinforce="Inventa una tabla de tres planetas donde el período aumente con la distancia y rotúlala «de ejemplo».",
  extend="Explica por qué un planeta lejano se mueve más lento en su órbita.")

L(OA14, 3,
  materials="Este cuaderno y lápiz. Para la tarea abierta: un cartón, un hilo largo, dos monedas o tapas pegadas con cinta al cartón y un lápiz.",
  use="Aprenderé las tres leyes de Kepler como un modelo del movimiento de los planetas y cómo Newton las explica con la gravitación. Sirve para describir órbitas sin fórmulas complicadas.",
  prior=["Sé que los planetas orbitan el Sol y que la gravedad los atrae.", "Sé que los períodos aumentan con la distancia."],
  explain=[
      "Primera ley de Kepler: las órbitas de los planetas son elipses y el Sol está en uno de los dos puntos especiales de la elipse, llamados focos. Una elipse es un círculo estirado. Un círculo es una elipse con los dos focos en el mismo punto. Las órbitas de los planetas son muy parecidas a círculos.",
      "Segunda ley: la línea que une el Sol con un planeta barre áreas iguales en tiempos iguales. Por eso el planeta se mueve más rápido cuando está más cerca del Sol y más lento cuando está más lejos. Tercera ley: mientras más lejos del Sol está un planeta, más largo es su período.",
      "Newton explicó estas leyes con la gravitación: la fuerza del Sol es más intensa cerca, lo que acelera al planeta. Las leyes son un modelo: describen bien los movimientos, pero un modelo tiene límites, como no considerar la atracción entre planetas. Para dibujar una elipse con hilo se usan dos puntos fijos, que serán los focos.",
  ],
  vocab=[("elipse", "curva cerrada que parece un círculo estirado"), ("foco", "uno de los dos puntos especiales de una elipse"), ("áreas iguales", "regiones del mismo tamaño que la línea Sol-planeta recorre en tiempos iguales"), ("leyes de Kepler", "tres reglas que describen el movimiento de los planetas")],
  worked=[
      ("Rapidez según la posición", "Un planeta está en dos puntos de su órbita: uno cerca del Sol y otro lejos. ¿En cuál se mueve más rápido?", ["La segunda ley dice que barre áreas iguales en tiempos iguales.", "Cerca del Sol, para barrer la misma área hay que recorrer más arco.", "Recorrer más arco en el mismo tiempo exige más rapidez."], "Se mueve más rápido cerca del Sol"),
      ("Áreas iguales", "Un planeta de ejemplo barre 10 unidades de área en 1 mes. ¿Cuánta área barre en 3 meses?", ["En tiempos iguales barre áreas iguales.", "En 3 meses hay 3 tramos de 1 mes.", "Multiplico: 10 · 3."], "30 unidades de área"),
  ],
  mistakes=[
      ("Dibujar las órbitas como círculos perfectos con el Sol en el centro.", "Son elipses y el Sol ocupa un foco.", "Dibuja una elipse suave y marca un foco."),
      ("Creer que el planeta se mueve siempre con la misma rapidez.", "Es más rápido cerca del Sol y más lento lejos.", "Relaciona rapidez con cercanía al Sol."),
  ],
  rec=[
      ("¿Qué forma tienen las órbitas de los planetas según Kepler?", "Elipses", "Es la primera ley de Kepler."),
      ("¿Dónde está el Sol en la órbita elíptica de un planeta?", "En uno de los focos", "No está en el centro de la elipse."),
      ("Verdadero o falso: un planeta se mueve más lento cuando está más cerca del Sol.", "Falso", "Se mueve más rápido cerca del Sol."),
  ],
  und=[
      ("¿Qué afirma la segunda ley de Kepler? A) Que el planeta barre áreas iguales en tiempos iguales; B) Que el planeta se mueve a rapidez constante.", "A", "Por eso cambia su rapidez a lo largo de la órbita."),
      ("¿Qué relación hay entre un círculo y una elipse? A) Una elipse con los dos focos en el mismo punto; B) Una figura sin relación.", "A", "El círculo es un caso especial de elipse."),
      ("¿Qué afirma la tercera ley, de forma cualitativa? A) Mientras más lejos está un planeta, mayor es su período; B) Todos los planetas tienen el mismo período.", "A", "La distancia y el período crecen juntos."),
  ],
  app=[
      arith("Un planeta de ejemplo barre 12 unidades de área en 2 meses. ¿Cuántas unidades barre en 4 meses?", "12*2", "En el doble de tiempo barre el doble de área.", " unidades"),
      arith("Un planeta de ejemplo barre 8 unidades de área en 1 mes. ¿Cuántas barre en 5 meses?", "8*5", "Cada mes barre la misma área.", " unidades"),
      ("Un planeta de ejemplo va a 30 unidades de rapidez en el punto A y a 20 en el punto B. ¿Cuál punto está más cerca del Sol? A) El A; B) El B.", "A", "Se mueve más rápido cerca del Sol."),
  ],
  rea=[
      ("Un compañero dice: «Si el Sol está en un foco, entonces la distancia al planeta es siempre la misma». ¿Qué le respondes? A) Es falso: en una elipse la distancia cambia a lo largo de la órbita; B) Tiene razón.", "A", "Por eso hay un punto más cercano y otro más lejano."),
      ("¿Por qué la segunda ley y la gravitación son coherentes entre sí? A) Porque la atracción es más intensa cerca del Sol y acelera al planeta; B) Porque la atracción no depende de la distancia.", "A", "La fuerza mayor cerca explica la mayor rapidez."),
  ],
  cha=[
      arith("Un planeta de ejemplo barre 6 unidades de área por semana. ¿Cuántas unidades barre en 7 semanas?", "6*7", "Se multiplica el área semanal por 7.", " unidades"),
      ("Un modelo de órbita con círculos y rapidez constante, ¿qué observación no explicaría? A) Que los planetas se muevan más rápido al acercarse al Sol; B) Que los planetas orbiten.", "A", "Con rapidez constante no habría cambio al acercarse."),
  ],
  context=[arith("Un cometa de ejemplo barre 15 unidades de área en 3 días. ¿Cuántas unidades barre en 9 días?", "15*3", "9 días son 3 tramos de 3 días con la misma área.", " unidades")],
  selfcheck=[("¿Qué forma tienen las órbitas?", "Elipses", "Con el Sol en un foco."), ("¿Dónde se mueve más rápido un planeta?", "Cerca del Sol", "Para barrer áreas iguales."), ("¿Qué dice la tercera ley?", "Más lejos, período más largo", "Es una relación creciente.")],
  open_task=task("Con un cartón, un hilo atado en un lazo, dos monedas pegadas con cinta como focos y un lápiz que tense el hilo, dibuja una elipse. Luego dibuja otra con las monedas más juntas. Anota qué forma se parece más a un círculo y marca dónde pondrías el Sol. Escribe qué ley de Kepler aplicaste.", "Con monedas más juntas, la elipse se parece más a un círculo. El Sol va en una de las monedas. Apliqué la primera ley: las órbitas son elipses con el Sol en un foco.", ["dibuja dos elipses", "relaciona focos juntos con forma circular", "marca el Sol en un foco"], ["dos dibujos y una nota"], ["poner el Sol en el centro", "decir que la elipse es un óvalo cualquiera"], "Pregunta qué pasa con la forma cuando los focos se alejan."),
  reinforce="Dibuja una órbita elíptica con el Sol en un foco y marca los puntos de mayor y menor rapidez.",
  extend="Explica por qué las leyes de Kepler describen sin explicar, y cómo Newton las explica.")

L(OA14, 4,
  materials=MAT,
  use="Aprenderé cómo la atracción gravitatoria de la Luna y del Sol origina las mareas, y cómo las posiciones de estos astros cambian su altura. Sirve para interpretar datos de mareas de ejemplo.",
  prior=["Conozco la ley de gravitación universal.", "Sé que las fases de la Luna se deben a su posición respecto del Sol y la Tierra."],
  explain=[
      "Las mareas son subidas y bajadas periódicas del nivel del mar. Se originan sobre todo por la atracción gravitatoria de la Luna, que está cerca, y en menor medida por la del Sol. La atracción es distinta en distintos puntos de la Tierra, y esa diferencia estira el agua. En muchas costas hay aproximadamente dos pleamares (nivel más alto) y dos bajamares (nivel más bajo) al día.",
      "Cuando el Sol, la Tierra y la Luna están alineados, en luna nueva y en luna llena, sus efectos se suman y las mareas son más grandes: son las mareas vivas. Cuando el Sol y la Luna forman un ángulo recto, en cuarto creciente y en cuarto menguante, sus efectos se restan en parte y las mareas son más pequeñas: son las mareas muertas.",
      "La amplitud de marea es la diferencia entre la pleamar y la bajamar. Las tablas de este cuaderno son de ejemplo, en metros, y no corresponden a un lugar real. Ya sabes que la fuerza gravitatoria baja rápido con la distancia: por eso la Luna, mucho más cercana, pesa más en las mareas que el Sol aunque el Sol tenga mucha más masa.",
  ],
  vocab=[("pleamar", "nivel más alto del mar durante una marea"), ("bajamar", "nivel más bajo del mar durante una marea"), ("amplitud de marea", "diferencia de altura entre pleamar y bajamar"), ("marea viva", "marea de gran amplitud con Sol, Tierra y Luna alineados")],
  worked=[
      ("Amplitud de marea", "En una costa de ejemplo, la pleamar es de 4 m y la bajamar de 1 m. ¿Cuál es la amplitud de marea?", ["La amplitud es la diferencia entre pleamar y bajamar.", "Resto: 4 − 1."], "3 m"),
      ("Clasificar la marea", "En luna llena el Sol, la Tierra y la Luna están alineados. ¿Qué tipo de marea se espera?", ["Alineados, los efectos del Sol y la Luna se suman.", "Con efectos sumados, la amplitud es grande."], "Marea viva"),
  ],
  mistakes=[
      ("Decir que solo el Sol causa las mareas.", "La Luna, por estar más cerca, es la causa principal.", "Nombra primero a la Luna y luego al Sol."),
      ("Confundir amplitud con altura de la pleamar.", "La amplitud es la diferencia entre pleamar y bajamar.", "Resta bajamar a pleamar."),
  ],
  rec=[
      ("¿Cómo se llama el nivel más alto del mar durante una marea?", "Pleamar", "Es el máximo de la marea."),
      ("¿Qué astro tiene el efecto principal sobre las mareas?", "La Luna", "Está mucho más cerca que el Sol."),
      ("En muchas costas, ¿cuántas pleamares hay aproximadamente por día?", "Dos", "Hay dos subidas y dos bajadas al día."),
  ],
  und=[
      ("¿Cuándo se producen las mareas vivas? A) Con luna nueva y luna llena; B) Con cuarto creciente y cuarto menguante.", "A", "El Sol, la Tierra y la Luna están alineados."),
      ("¿Qué origina las mareas? A) La atracción gravitatoria de la Luna y del Sol; B) El viento y las olas.", "A", "La gravitación estira el agua."),
      ("¿Cuándo son más pequeñas las mareas? A) En cuarto creciente y menguante; B) En luna llena.", "A", "El Sol y la Luna forman un ángulo recto."),
  ],
  app=[
      arith("En una costa de ejemplo en luna llena, la pleamar es de 6 m y la bajamar de 1 m. ¿Cuál es la amplitud en metros?", "6-1", "Se resta la bajamar a la pleamar.", " m"),
      arith("En cuarto creciente, en la misma costa de ejemplo, la pleamar es de 4 m y la bajamar de 2 m. ¿Cuántos metros menor es la amplitud que en la luna llena de 5 m?", "5-(4-2)", "La amplitud en cuarto creciente es 2 m y se compara con 5 m.", " m"),
      arith("Si hay dos pleamares en 24 horas separadas por igual, de forma aproximada, ¿cada cuántas horas ocurre una?", "24//2", "Se divide el día en dos partes.", " horas"),
  ],
  rea=[
      ("¿Por qué la Luna influye más que el Sol en las mareas, aunque el Sol tenga más masa? A) Porque está mucho más cerca y la atracción baja rápido con la distancia; B) Porque tiene más masa que el Sol.", "A", "La distancia pesa más que la masa."),
      ("En luna nueva las mareas son más grandes. ¿Cuál es la mejor explicación? A) El Sol, la Tierra y la Luna están alineados y sus efectos se suman; B) Porque con luna nueva solo el Sol actúa sobre el mar.", "A", "La alineación suma los efectos."),
  ],
  cha=[
      ("La atracción de la Luna es mayor en el lado de la Tierra más cercano a ella. ¿Por qué eso estira el agua? A) Porque la atracción es distinta en distintos puntos de la Tierra; B) Porque la Luna toca el agua.", "A", "La diferencia de atracción produce el estiramiento."),
      ("Datos de ejemplo de amplitudes: luna nueva 5 m, cuarto creciente 2 m, luna llena 5 m, cuarto menguante 2 m. ¿Qué patrón se observa? A) Las amplitudes son mayores con alineación; B) Son iguales siempre.", "A", "5 m en luna nueva y llena, 2 m en los cuartos."),
  ],
  context=[arith("En un puerto de ejemplo la amplitud de marea es de 5 m en luna nueva y de 2 m en cuarto creciente. ¿Cuántos metros más amplia es la primera?", "5-2", "Se restan las dos amplitudes.", " m")],
  selfcheck=[("¿Qué astros originan las mareas?", "La Luna y el Sol", "Por su atracción gravitatoria."), ("¿Cuándo ocurren las mareas vivas?", "En luna nueva y en luna llena", "Hay alineación de los tres astros."), ("¿Qué es la amplitud de marea?", "La diferencia entre pleamar y bajamar", "Se mide en metros.")],
  open_task=task("Con esta tabla de ejemplo (fase: pleamar, bajamar en metros) luna nueva: 6, 1; cuarto creciente: 4, 2; luna llena: 6, 1; cuarto menguante: 4, 2, calcula la amplitud de cada fase y marca cuáles son mareas vivas y cuáles muertas. Escribe una explicación de dos oraciones con gravitación y alineación.", "Amplitudes: nueva 5, creciente 2, llena 5, menguante 2. Vivas: nueva y llena. Muertas: los cuartos. Con el Sol, la Tierra y la Luna alineados, las atracciones se suman y la marea sube más.", ["calcula las cuatro amplitudes", "clasifica vivas y muertas", "explica con alineación y gravitación"], ["tabla completa y dos oraciones"], ["restar al revés", "decir que la Luna crea el agua del mar"], "Pregunta qué cambiaría si la Luna estuviera más lejos."),
  reinforce="Dibuja Sol, Tierra y Luna alineados y otra vez en ángulo recto, y rotula cuál produce marea viva.",
  extend="Explica por qué un lago pequeño casi no muestra mareas.")

L(OA14, 5,
  materials=MAT,
  use="Aprenderé cómo la gravitación explica la formación del sistema solar, de estrellas y galaxias, y el movimiento de satélites y sondas. Sirve para explicar estructuras cósmicas con un mismo mecanismo.",
  prior=["Conozco la gravitación universal y las leyes de Kepler.", "Sé que una explicación necesita un mecanismo y evidencias."],
  explain=[
      "El modelo más aceptado para el sistema solar dice que se formó a partir de una nube de gas y polvo que se contrajo por la gravitación. La nube giró más rápido al contraerse, formó un disco, y en el centro se formó el Sol. En el disco, el material se unió y formó los planetas y otros cuerpos. Las estrellas se forman de manera parecida, cuando una nube de gas se contrae por la gravitación, y las galaxias, con sus miles de millones de estrellas, también se mantienen unidas por la gravitación. Los planetas orbitan en el mismo sentido y casi en un mismo plano, huella de ese disco.",
      "Un satélite artificial no está quieto: cae permanentemente hacia la Tierra, pero como tiene mucha velocidad lateral, nunca la alcanza y la rodea. Esta idea se explica con el cañón de Newton: mientras más rápido sale la bala, más lejos cae, y con la rapidez suficiente da toda la vuelta. Un satélite más cercano a la Tierra tiene período más corto que uno más lejano, como dice la tercera ley.",
      "Un satélite geoestacionario orbita sobre el ecuador con un período de aproximadamente un día, igual al de rotación de la Tierra, y por eso parece quieto sobre un punto. Las sondas espaciales pueden cambiar su rapidez al pasar cerca de un planeta, aprovechando su atracción. Los datos de este cuaderno son de ejemplo y no corresponden a satélites reales.",
  ],
  vocab=[("satélite", "cuerpo que orbita a otro, natural o artificial"), ("sonda espacial", "nave sin tripulación que viaja a explorar otros astros"), ("geoestacionario", "satélite con período de aproximadamente un día que parece quieto en el cielo"), ("nube de gas y polvo", "material del que se forman estrellas y sistemas planetarios")],
  worked=[
      ("Vueltas por día", "Un satélite de ejemplo da una vuelta cada 4 horas. ¿Cuántas vueltas da en un día de 24 horas?", ["Divido las 24 horas del día por el período.", "24 ÷ 4."], "6 vueltas por día"),
      ("El cañón de Newton", "En un esquema, una bala sale horizontalmente de una montaña muy alta con rapidez creciente. ¿Qué pasa si la rapidez es suficiente?", ["Con poca rapidez, la bala cae lejos pero choca con la Tierra.", "Al aumentar la rapidez, cae cada vez más lejos.", "Con la rapidez justa, la Tierra se curva debajo y la bala nunca llega al suelo."], "La bala queda en órbita: cae permanentemente alrededor de la Tierra"),
  ],
  mistakes=[
      ("Decir que los satélites no sienten la gravedad.", "La gravedad es justamente lo que los mantiene en órbita.", "Dilo así: están cayendo alrededor de la Tierra."),
      ("Pensar que un satélite lejano tiene el mismo período que uno cercano.", "El período aumenta con la distancia.", "Ordena los satélites por distancia antes de comparar."),
  ],
  rec=[
      ("¿Qué fuerza mantiene unidos a los planetas en el sistema solar y en órbita al Sol?", "La gravitación", "Es la atracción entre cuerpos con masa."),
      ("Verdadero o falso: el sistema solar se formó a partir de una nube de gas y polvo.", "Verdadero", "Es el modelo más aceptado."),
      ("¿Cómo se llama un satélite que parece quieto sobre un punto de la Tierra?", "Geoestacionario", "Su período es de aproximadamente un día."),
  ],
  und=[
      ("¿Por qué un satélite artificial no cae a la Tierra? A) Porque tiene mucha velocidad lateral y cae alrededor de ella; B) Porque no siente gravedad.", "A", "Cae todo el tiempo, pero la Tierra se curva debajo de él."),
      ("¿Qué mantiene unidas a las estrellas dentro de una galaxia? A) La gravitación; B) El viento solar.", "A", "La atracción mutua las mantiene ligadas."),
      ("¿Qué pasa con el período de un satélite cuanto más lejos de la Tierra está? A) Aumenta; B) Disminuye.", "A", "Es la tercera ley de Kepler."),
  ],
  app=[
      arith("Un satélite de ejemplo da una vuelta cada 8 horas. ¿Cuántas vueltas da en un día de 24 horas?", "24//8", "Se divide el día por el período.", " vueltas"),
      arith("Otro satélite de ejemplo da una vuelta cada 12 horas. ¿Cuántas vueltas da en 3 días de 24 horas?", "3*24//12", "En 3 días hay 72 horas.", " vueltas"),
      ("Tres satélites de ejemplo tienen períodos de 2, 12 y 24 horas. ¿Cuál es el más lejano de la Tierra? A) El de 24 horas; B) El de 2 horas.", "A", "A mayor período, mayor distancia."),
  ],
  rea=[
      ("Un compañero dice: «En el espacio no hay gravedad y por eso los satélites flotan». ¿Qué le respondes? A) Sí hay gravedad: los satélites caen todo el tiempo alrededor de la Tierra; B) Tiene razón.", "A", "La gravedad actúa a grandes distancias y es lo que los mantiene orbitando."),
      ("¿Qué evidencia apoya que el sistema solar se formó de una nube que giraba? A) Los planetas orbitan en el mismo sentido y casi en un mismo plano; B) Los planetas son de colores distintos.", "A", "Ese orden indica un disco giratorio de origen común."),
  ],
  cha=[
      ("Un satélite tiene período de aproximadamente un día y órbita sobre el ecuador. ¿Qué se verá desde un punto del suelo? A) Que parece quieto en el cielo; B) Que da muchas vueltas por hora.", "A", "Gira junto con la Tierra."),
      ("Una sonda pasa cerca de un planeta y cambia su rapidez. ¿Qué mecanismo explica el cambio? A) La atracción gravitatoria del planeta; B) El roce con el espacio vacío.", "A", "La gravitación del planeta modifica el movimiento de la sonda."),
  ],
  context=[arith("Un satélite de meteorología de ejemplo da una vuelta cada 6 horas. ¿Cuántas vueltas da en un día de 24 horas?", "24//6", "Se divide el día por el período.", " vueltas")],
  selfcheck=[("¿Cómo se formó el sistema solar según el modelo?", "De una nube de gas y polvo que se contrajo por gravitación", "Se formó un disco y luego el Sol y los planetas."), ("¿Por qué un satélite no cae al suelo?", "Porque cae alrededor de la Tierra con mucha velocidad lateral", "La Tierra se curva debajo de él."), ("¿Qué es un satélite geoestacionario?", "Uno con período de un día que parece quieto", "Gira junto con la Tierra.")],
  open_task=task("Elige uno de estos casos de ejemplo: A) un satélite que da una vuelta cada 6 horas; B) un satélite geoestacionario. Escribe cuántas vueltas da en un día, dibuja la Tierra y su órbita con una flecha de la gravedad, y explica con una frase por qué no cae al suelo. Indica que los datos son de ejemplo.", "Caso A: 24 ÷ 6 = 4 vueltas al día. Dibujo: Tierra en el centro, órbita alrededor y una flecha hacia la Tierra. No cae al suelo porque se mueve con mucha velocidad lateral y cae alrededor de la Tierra. Datos de ejemplo.", ["calcula las vueltas", "dibuja la flecha de gravedad", "explica por qué no cae"], ["cálculo, dibujo y frase"], ["decir que no hay gravedad", "dibujar la flecha de gravedad hacia afuera"], "Pregunta qué cambiaría si el satélite fuera más lento."),
  reinforce="Explica con tus palabras el cañón de Newton.",
  extend="Explica por qué una sonda puede ganar rapidez al pasar cerca de un planeta.")
