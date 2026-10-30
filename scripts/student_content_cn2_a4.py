"""Cuaderno del estudiante, 2.º básico Ciencias Naturales: OA 07 (partes del cuerpo) y OA 08 (actividad física)."""
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


OA7, OA8 = "CN02 OA 07", "CN02 OA 08"

# ---------------------------------------------------------------- OA 07
L(OA7, 1,
  materials="Este cuaderno con el dibujo de un cuerpo para completar, lápices de colores y tus propias manos para tocar el pecho y la barriga.",
  use="Aprenderé dónde están en el cuerpo el corazón, los pulmones, el estómago, el esqueleto y los músculos. Sirve para entender cómo funciona tu cuerpo por dentro.",
  prior=["Sé nombrar partes externas como cabeza, brazos, piernas y pecho.", "Sé que dentro del cuerpo hay partes que no se ven."],
  explain=[
      "Dentro de tu cuerpo hay partes que no se ven, pero que son muy importantes para vivir. Hoy conocerás cinco: el corazón, los pulmones, el estómago, el esqueleto y los músculos. Cada una está en un lugar del cuerpo y hace un trabajo.",
      "Pon una mano en el centro del pecho. Ahí están los pulmones y el corazón, protegidos por las costillas. Los pulmones son dos, uno a cada lado. El corazón queda entre los dos, un poquito hacia la izquierda. El estómago está más abajo, en la parte de arriba de la barriga.",
      "El esqueleto son todos los huesos y está por todo el cuerpo. Los músculos están debajo de la piel y también están por todo el cuerpo. Un dibujo del interior del cuerpo es un modelo aproximado: muestra dónde están las partes, pero no es exacto en tamaño ni en forma.",
  ],
  vocab=[("corazón", "órgano del pecho que mueve la sangre"), ("pulmones", "dos órganos del pecho que usamos para respirar"), ("estómago", "órgano de la parte alta de la barriga que recibe la comida"), ("esqueleto", "conjunto de todos los huesos del cuerpo"), ("músculos", "partes blandas bajo la piel que permiten mover el cuerpo")],
  worked=[
      ("Ubicar una parte", "¿Dónde está el estómago: en la cabeza o en la barriga?", ["El estómago recibe la comida.", "La comida baja desde la boca.", "Está en la parte de arriba de la barriga."], "En la barriga"),
      ("Ubicar el corazón", "¿Dónde está el corazón respecto de los pulmones?", ["Los pulmones son dos.", "El corazón queda entre los dos.", "Está un poquito hacia la izquierda."], "Entre los pulmones, un poco hacia la izquierda"),
  ],
  mistakes=[
      ("Decir «el corazón está en la mano».", "Se confunde el pulso con la ubicación del corazón.", "El corazón está en el pecho. En la muñeca sientes su pulso, pero el corazón no está ahí."),
      ("Decir «los huesos están solo en los brazos y piernas».", "Se olvidan costillas, columna y cráneo.", "El esqueleto está por todo el cuerpo."),
  ],
  rec=[
      ("¿En qué parte del cuerpo están el corazón y los pulmones: en el pecho o en la cabeza?", "En el pecho", "Las costillas los protegen."),
      ("¿Cuántos pulmones tenemos?", "Dos", "Hay uno a cada lado del pecho."),
      ("¿Dónde está el estómago: arriba o abajo de la barriga?", "En la parte de arriba", "Está en la parte alta del abdomen."),
  ],
  und=[
      ("¿Por qué decimos que un dibujo del cuerpo es un modelo aproximado?", "Porque muestra dónde están las partes pero no es exacto", "Es una ayuda para entender."),
      ("¿Qué partes protegen las costillas?", "El corazón y los pulmones", "Las costillas rodean el pecho."),
      ("Nombra las cinco partes del cuerpo de hoy.", "Corazón, pulmones, estómago, esqueleto y músculos", "Son las partes de la clase."),
  ],
  app=[
      ("Une cada parte con su lugar: A estómago, B pulmones, C corazón. Lugares: 1 entre los pulmones, 2 a los lados del pecho, 3 parte alta de la barriga. Escribe los pares.", "A3, B2, C1", "Cada parte está en el lugar indicado."),
      arith("Tienes 2 pulmones, 1 corazón y 1 estómago. ¿Cuántos órganos de esas tres partes tienes en total?", "2+1+1", "Se suman los pulmones, el corazón y el estómago."),
      ("Pones una mano en el pecho y sientes que sube y baja al respirar. ¿Qué partes se mueven dentro?", "Los pulmones", "Se llenan y vacían de aire."),
  ],
  rea=[
      ("Un niño dibuja el estómago en la cabeza. ¿Dónde debe dibujarlo?", "En la parte alta de la barriga", "El estómago recibe la comida y está en la barriga."),
      ("¿Por qué las costillas son importantes para los pulmones y el corazón?", "Porque los protegen", "Forman una jaula alrededor del pecho."),
  ],
  cha=[
      ("Un dibujo muestra el corazón en la barriga. ¿Qué corrección harías?", "Lo pondría en el pecho, entre los pulmones", "El corazón está en el pecho, protegido por las costillas."),
      ("¿Por qué conviene decir «aproximado» al hablar de un dibujo del interior del cuerpo?", "Porque no muestra todo exacto", "Los dibujos simplifican."),
  ],
  context=[("En el consultorio, un médico apoya un aparato en el pecho de un niño para oír su corazón. ¿Por qué lo apoya en el pecho y no en la mano?", "Porque el corazón está en el pecho", "Allí se oye mejor su latido.")],
  selfcheck=[("¿Dónde está el estómago?", "En la barriga", "Recibe la comida."), ("¿Cuántos pulmones hay?", "Dos", "Uno a cada lado."), ("¿Los huesos forman el esqueleto?", "Sí", "El esqueleto es el conjunto de huesos.")],
  open_task=task("Dibuja un cuerpo sencillo y ubica con flechas las cinco partes: corazón, pulmones, estómago, esqueleto y músculos. Escribe una frase que diga por qué tu dibujo es un modelo aproximado.", "Dibujé un cuerpo con el corazón entre los pulmones, el estómago abajo, huesos dibujados como líneas y músculos pintados en el brazo. Mi dibujo es aproximado porque no está a tamaño real.", ["ubica las cinco partes", "usa flechas con nombres", "explica por qué es aproximado"], ["dibujo con flechas", "frase"], ["poner el estómago en el pecho", "dibujar solo una parte"], "Valora la ubicación y pide que explique una parte que puso en otro lugar al comienzo."),
  reinforce="Ponte la mano en el pecho y respira lento tres veces. Dibuja qué partes crees que se mueven.",
  extend="Pregunta a un adulto cuál de estas partes puede oír o sentir en su cuerpo y cómo.")

L(OA7, 2,
  materials="Este cuaderno y un reloj o cronómetro con segundos. Para sentir el pulso: dos dedos y una muñeca en reposo, sentado y tranquilo.",
  use="Aprenderé qué hacen el corazón y los pulmones. Sirve para entender por qué respiras todo el día y por qué sientes latidos.",
  prior=["Sé ubicar el corazón y los pulmones.", "Sé contar hasta 60."],
  explain=[
      "El corazón es un músculo del tamaño de tu puño. Late sin parar: se aprieta y se suelta y así empuja la sangre por todo el cuerpo. La sangre lleva por todo el cuerpo lo que necesita, como el oxígeno. El oxígeno es la parte del aire que el cuerpo necesita para vivir.",
      "Los pulmones sirven para respirar. Cuando inspiras, el aire entra por la nariz o la boca y llena los pulmones. Cuando espiras, el aire sale. Del aire, los pulmones toman el oxígeno, y la sangre lo lleva a todas partes.",
      "Puedes sentir el pulso poniendo dos dedos en la muñeca, bajo el pulgar. Cada golpecito es un latido del corazón. Si cuentas los latidos en 15 segundos, sabes cómo trabaja tu corazón en reposo. El corazón y los pulmones trabajan juntos.",
  ],
  vocab=[("latido", "cada vez que el corazón se aprieta y se suelta"), ("sangre", "líquido que lleva lo que el cuerpo necesita"), ("inspirar", "meter aire a los pulmones"), ("espirar", "sacar aire de los pulmones"), ("pulso", "golpecito que sientes en la muñeca por los latidos"), ("oxígeno", "parte del aire que el cuerpo necesita para vivir")],
  worked=[
      ("Función del corazón", "¿Qué hace el corazón?", ["El corazón se aprieta y se suelta.", "Al apretarse empuja la sangre.", "La sangre llega a todo el cuerpo."], "Empuja la sangre por todo el cuerpo"),
      ("Función de los pulmones", "¿Qué hacen los pulmones?", ["Al inspirar entra aire.", "Los pulmones toman el oxígeno del aire.", "Al espirar sale aire."], "Permiten respirar el aire"),
  ],
  mistakes=[
      ("Decir «el corazón respira».", "Se confunde la función del corazón con la de los pulmones.", "El corazón mueve la sangre; los pulmones son los que respiran."),
      ("Decir «los pulmones empujan la sangre».", "Se mezclan las funciones.", "Los pulmones toman aire y el corazón empuja la sangre."),
  ],
  rec=[
      ("¿Qué empuja el corazón por el cuerpo?", "La sangre", "Es su trabajo."),
      ("¿Qué parte del cuerpo usas para respirar?", "Los pulmones", "Se llenan de aire."),
      ("Cada golpecito del corazón se llama...", "Latido", "Es un latido."),
  ],
  und=[
      ("¿Por qué decimos que el corazón es un músculo?", "Porque se aprieta y se suelta", "Los músculos se acortan y se alargan."),
      ("¿Qué pasa con el aire cuando espiras?", "Sale de los pulmones", "Espirar es sacar aire."),
      ("¿Para qué sirve contar el pulso?", "Para saber cómo late el corazón", "Cada golpecito es un latido."),
  ],
  app=[
      arith("En reposo, Ana cuenta 20 latidos en 15 segundos. ¿Cuántos latidos son en 30 segundos si late igual?", "20*2", "30 segundos son dos veces 15 segundos."),
      ("Ordena: A el aire sale, B el aire entra, C el aire llega a los pulmones. Escribe las letras en el orden de una respiración.", "B, C, A", "Primero entra, llena los pulmones y luego sale."),
      ("Cuando corres, sientes golpecitos más rápidos en el pecho. ¿Qué parte del cuerpo late más rápido?", "El corazón", "Es el órgano que late."),
  ],
  rea=[
      ("Teo dice: «Respiramos con el corazón». ¿Qué le dices?", "Que respiramos con los pulmones", "El corazón mueve sangre."),
      ("Si el pulso de un niño en reposo es 22 latidos en 15 segundos y el de otro es 18, ¿cuál es mayor y cuánto?", "El primero, por 4 latidos", "22 − 18 = 4."),
  ],
  cha=[
      arith("Un niño cuenta 18 latidos en 15 segundos. ¿Cuántos latidos serían en 60 segundos?", "18*4", "60 segundos son cuatro veces 15 segundos."),
      ("¿Por qué el corazón y los pulmones trabajan juntos?", "Porque los pulmones toman el aire y el corazón lo reparte con la sangre", "Cada uno hace una parte del trabajo."),
  ],
  context=[("En una pausa de la clase de educación física, Rocío se toma el pulso: 24 latidos en 15 segundos. ¿Cuántos latidos tendrá en 30 segundos si late igual?", "48", "24 por 2 son 48.")],
  selfcheck=[("¿Qué hace el corazón?", "Empuja la sangre", "Reparte la sangre por el cuerpo."), ("¿Qué hacen los pulmones?", "Permiten respirar", "Llenan el cuerpo de aire."), ("¿Dónde se siente el pulso?", "En la muñeca", "Allí se sienten los latidos.")],
  open_task=task("Siéntate tranquilo 2 minutos. Busca tu pulso en la muñeca y cuenta los latidos en 15 segundos. Anota el número. Dibuja el camino del aire por tus pulmones y escribe qué hace el corazón con la sangre.", "Conté 21 latidos en 15 segundos. Dibujé el aire entrando por la nariz a los pulmones. El corazón empuja la sangre por el cuerpo.", ["anota los latidos en 15 segundos", "dibuja el camino del aire", "explica la función del corazón"], ["número anotado", "dibujo", "frase"], ["contar mal el tiempo", "mezclar las funciones de corazón y pulmones"], "Valora el número anotado y pide que explique qué haría cambiar su pulso."),
  reinforce="Cuenta cuántas veces respiras en 30 segundos sentado y sin hablar.",
  extend="Averigua con un adulto por qué el médico escucha el pecho con un aparato.")

L(OA7, 3,
  materials="Este cuaderno y lápices de colores. Lápiz para dibujar el camino de la comida.",
  use="Aprenderé qué hace el estómago con la comida. Sirve para entender por qué masticar bien ayuda.",
  prior=["Sé que el estómago está en la parte alta de la barriga.", "Sé que comemos para tener energía."],
  explain=[
      "El estómago es una bolsa blanda de músculo que está en la parte alta de la barriga. Cuando tragas, la comida baja hasta el estómago. Allí se queda un rato y el estómago la mueve y la aprieta.",
      "En el estómago, la comida se mezcla con jugos y se deshace en trozos muy chiquitos. Por eso comer despacio y masticar bien ayuda: llegan trozos más chicos y el estómago trabaja menos. Cuando la comida está muy chiquita, pasa a otras partes del cuerpo.",
      "De la comida, el cuerpo toma lo que necesita para crecer y para tener energía. Lo que no necesita sale del cuerpo. Para ayudar al estómago, come despacio, mastica bien y toma agua. Si te duele la guata, avisa a un adulto.",
  ],
  vocab=[("estómago", "órgano en forma de bolsa que recibe la comida"), ("masticar", "moler la comida con los dientes"), ("jugos", "líquidos del cuerpo que ayudan a deshacer la comida"), ("energía", "fuerza que te permite moverte y crecer"), ("tragar", "hacer pasar la comida hacia el estómago")],
  worked=[
      ("Seguir la comida", "Ordena: la comida se deshace, se mastica, llega al estómago.", ["Primero se mastica con los dientes.", "Luego se traga y llega al estómago.", "En el estómago se deshace en trozos chicos."], "Se mastica, llega al estómago, se deshace"),
      ("Por qué masticar", "¿Por qué ayuda masticar bien?", ["Masticar deshace la comida en trozos chicos.", "El estómago recibe trozos más fáciles.", "Trabaja menos."], "Porque llegan trozos más chicos al estómago"),
  ],
  mistakes=[
      ("Decir «el estómago está en el pecho».", "Se confunde con los pulmones.", "El estómago está en la parte alta de la barriga."),
      ("Decir «el estómago guarda la comida para siempre».", "No se piensa que la comida sigue su camino.", "La comida se deshace y luego pasa a otras partes del cuerpo."),
  ],
  rec=[
      ("¿Dónde llega la comida después de tragar?", "Al estómago", "Está en la barriga."),
      ("¿Con qué parte del cuerpo se mastica la comida?", "Con los dientes", "Muelen la comida."),
      ("En el estómago, ¿la comida queda entera o se deshace?", "Se deshace", "Se mezcla con jugos."),
  ],
  und=[
      ("¿Qué hace el estómago con la comida?", "La mezcla y la deshace en trozos chicos", "Es su función en esta clase."),
      ("¿Por qué conviene comer despacio?", "Porque se mastica mejor y el estómago trabaja menos", "Llegan trozos más chicos."),
      ("¿Para qué toma el cuerpo lo que hay en la comida?", "Para crecer y tener energía", "Es lo que necesita para vivir."),
  ],
  app=[
      ("Ordena el camino de un trozo de pan: A estómago, B boca, C se deshace. Escribe las letras.", "B, A, C", "El pan se mastica en la boca, llega al estómago y se deshace."),
      arith("Un niño come 4 cucharadas de lentejas y mastica cada una 10 veces. ¿Cuántas veces mastica en total?", "4*10", "Se multiplican las cucharadas por 10."),
      ("Dos niños comen el mismo pan: Ana lo traga entero y Beto lo mastica bien. ¿A quién le llega al estómago el pan en trozos más chicos?", "A Beto", "Masticar deshace el pan."),
  ],
  rea=[
      ("Una niña dice que no necesita masticar porque el estómago hace todo. ¿Qué le dices?", "Que masticar ayuda al estómago a trabajar menos", "Los trozos chicos se mezclan más fácil."),
      ("Un compañero cree que el estómago guarda la comida sin cambiarla. ¿Qué le muestras con lo aprendido?", "Que la mezcla con jugos y la deshace", "Cambia la comida."),
  ],
  cha=[
      ("Explica por qué conviene esperar un rato antes de correr después de comer.", "Porque el estómago está trabajando y correr puede dar molestias", "Es mejor dejarlo trabajar tranquilo."),
      ("Escribe dos hábitos que ayudan al estómago.", "Comer despacio y masticar bien", "Hacen más fácil su trabajo."),
  ],
  context=[("En el almuerzo, Valentina come arroz con pollo. ¿Por cuáles dos lugares pasa su comida, en orden, hasta deshacerse?", "Primero la boca y luego el estómago", "Primero se mastica y luego se deshace en el estómago.")],
  selfcheck=[("¿Dónde está el estómago?", "En la parte alta de la barriga", "Es el órgano que recibe la comida."), ("¿Qué hace masticar?", "Deshace la comida en trozos chicos", "Ayuda al estómago."), ("¿Se deshace la comida en el estómago?", "Sí", "Se mezcla con jugos.")],
  open_task=task("Dibuja el camino de una manzana desde la boca hasta el estómago en tres cuadros con flechas. Escribe una frase que diga qué pasa en cada cuadro y un hábito que ayuda al estómago.", "Cuadro 1: la muerdo y la mastico. Cuadro 2: la trago y llega al estómago. Cuadro 3: se deshace en trozos chicos. Hábito: comer despacio.", ["dibuja tres cuadros en orden", "explica cada cuadro", "nombra un hábito"], ["dibujo con flechas", "tres frases"], ["poner el estómago en el pecho", "olvidar masticar"], "Valora el orden y pide que explique por qué masticar ayuda."),
  reinforce="En tu próxima comida, cuenta cuántas veces masticas el primer trozo y pasa a masticar más despacio.",
  extend="Escribe tres alimentos que te gusten y di qué parte del cuerpo los recibe primero.")

L(OA7, 4,
  materials="Este cuaderno y lápices de colores. En casa: tu codo y tu brazo para sentir cómo se mueve.",
  use="Aprenderé para qué sirven el esqueleto y los músculos. Sirve para entender cómo te mueves y cómo se protegen tus órganos.",
  prior=["Sé que los vertebrados tienen columna.", "Sé que los músculos están bajo la piel."],
  explain=[
      "El esqueleto está formado por todos los huesos del cuerpo. Sostiene el cuerpo para que no te caigas y protege partes blandas. El cráneo protege el cerebro. Las costillas protegen el corazón y los pulmones. La columna sostiene la espalda.",
      "Los músculos están pegados a los huesos. Un músculo se acorta y se pone duro cuando trabaja, y tira del hueso. Así se mueve esa parte del cuerpo. Cuando descansa, el músculo se suelta y se alarga. Por eso necesitamos músculos para caminar, saltar y agarrar. Los huesos se unen en las articulaciones, como el codo, y ahí el cuerpo se dobla.",
      "El esqueleto y los músculos trabajan juntos. Sin huesos, el cuerpo sería blando como una lombriz. Sin músculos, los huesos no se moverían. Prueba doblar el brazo: sientes que el músculo de arriba se pone duro. Ahí está tirando del hueso.",
  ],
  vocab=[("esqueleto", "conjunto de huesos que sostiene y protege el cuerpo"), ("hueso", "parte dura y firme del esqueleto"), ("músculo", "parte blanda que se acorta para mover los huesos"), ("cráneo", "hueso de la cabeza que protege el cerebro"), ("articulación", "lugar donde se unen dos huesos y el cuerpo se dobla")],
  worked=[
      ("Función del esqueleto", "¿Para qué sirven las costillas?", ["Las costillas rodean el pecho.", "Dentro están el corazón y los pulmones.", "Los protegen."], "Protegen el corazón y los pulmones"),
      ("Función del músculo", "¿Qué le pasa al músculo del brazo cuando doblas el codo?", ["El músculo se acorta.", "Tira del hueso.", "El brazo se dobla."], "Se acorta, se pone duro y tira del hueso"),
  ],
  mistakes=[
      ("Decir «los huesos se mueven solos».", "Se olvida el trabajo de los músculos.", "Los músculos tiran de los huesos para moverlos."),
      ("Decir «los músculos solo están en los brazos».", "No se piensa en el resto del cuerpo.", "Hay músculos en todo el cuerpo, como las piernas, la espalda y el corazón."),
  ],
  rec=[
      ("¿Qué parte del cuerpo protege el cráneo?", "El cerebro", "El cráneo es el hueso de la cabeza que rodea el cerebro."),
      ("¿Qué partes mueven los huesos: los músculos o las costillas?", "Los músculos", "Tiran de los huesos."),
      ("¿Cómo se llama el conjunto de todos los huesos?", "Esqueleto", "Es la definición."),
  ],
  und=[
      ("Nombra dos cosas que hace el esqueleto.", "Sostiene el cuerpo y protege órganos", "Son las funciones de la clase."),
      ("¿Qué le pasa a un músculo cuando trabaja?", "Se acorta y se pone duro", "Así tira del hueso."),
      ("¿Por qué necesitamos tanto huesos como músculos para movernos?", "Porque los músculos mueven los huesos", "Los músculos tiran de los huesos."),
  ],
  app=[
      ("Une cada hueso con su trabajo: A cráneo, B costillas, C columna. Trabajo: 1 protegen el corazón y los pulmones, 2 protege el cerebro, 3 sostiene la espalda. Escribe los pares.", "A2, B1, C3", "Cada hueso hace el trabajo indicado."),
      arith("Un brazo se dobla 8 veces en una rutina y otro brazo 7 veces. ¿Cuántas veces se doblaron los dos brazos en total?", "8+7", "Se suman las veces de cada brazo."),
      ("Doblas el brazo y sientes que se pone duro el músculo de arriba. ¿Qué está haciendo ese músculo?", "Se está acortando", "Un músculo trabaja acortándose."),
  ],
  rea=[
      ("Si no tuvieras huesos, ¿cómo sería tu cuerpo? Usa lo que aprendiste del esqueleto.", "Blando, sin sostén ni protección", "Los huesos sostienen y protegen."),
      ("Un compañero dice que las costillas solo sirven para respirar. ¿Qué otra función tienen?", "Proteger el corazón y los pulmones", "Rodean los órganos del pecho."),
  ],
  cha=[
      ("Explica con un ejemplo cómo trabajan juntos un músculo y un hueso al levantar una mochila.", "El músculo se acorta y tira del hueso del brazo", "El músculo mueve el hueso."),
      ("¿Por qué conviene usar casco al andar en bicicleta?", "Porque el cráneo protege el cerebro, pero un golpe fuerte puede dañarlo", "El casco cuida la cabeza."),
  ],
  context=[("Antes de jugar fútbol, el profe dice que muevas bien las piernas. ¿Qué parte del cuerpo tira de los huesos de la pierna para correr?", "Los músculos", "Se acortan y tiran de los huesos.")],
  selfcheck=[("¿Qué hueso de la cabeza protege al cerebro?", "El cráneo", "Rodea el cerebro como un casco."), ("¿Qué mueve los huesos?", "Los músculos", "Tiran de ellos."), ("¿Dónde se unen dos huesos?", "En la articulación", "Allí el cuerpo se dobla.")],
  open_task=task("Mira tu brazo. Dobla y estira tu codo cinco veces con la mano contraria en el músculo de arriba. Dibuja tu brazo doblado y estirado, y escribe qué sentiste en el músculo y qué huesos se mueven.", "Sentí que el músculo se puso duro al doblar. Dibujé el brazo doblado y estirado con el hueso del brazo y el del antebrazo.", ["dibuja el brazo en dos posiciones", "describe lo que siente el músculo", "nombra qué se mueve"], ["dos dibujos", "frase de observación"], ["decir que los huesos se mueven solos"], "Valora la descripción de la sensación y pide que explique con palabras de la clase cómo trabaja el músculo."),
  reinforce="Toca tu cráneo, tus costillas y tu columna con las manos y di en voz alta qué protege cada una.",
  extend="Averigua con un adulto cómo se llama el hueso del muslo y dibújalo en tu pierna.")

# ---------------------------------------------------------------- OA 08
L(OA8, 1,
  materials="Este cuaderno, un reloj con segundos y espacio para saltar suave en el mismo lugar. Ejercicio suave, con un adulto cerca; detente si te mareas o te duele algo.",
  use="Aprenderé qué cambios notas en tu cuerpo cuando te mueves. Sirve para entender por qué el ejercicio te hace respirar más rápido y sentir calor.",
  prior=["Sé tomarme el pulso en la muñeca.", "Sé contar hasta 60."],
  explain=[
      "Cuando te mueves mucho, tu cuerpo cambia. Respiras más rápido, tu corazón late más fuerte y más rápido, y sientes calor. Algunas personas sudan. Estos cambios son normales y muestran que tu cuerpo está trabajando.",
      "La actividad física es cualquier movimiento que hace trabajar tus músculos, como correr, saltar, bailar, andar en bicicleta o jugar a la pelota. Es distinta de estar sentado o acostado, que se llama reposo.",
      "Para comparar antes y después, mide lo mismo en los dos momentos. Por ejemplo, el pulso en 15 segundos. Anota el número de reposo y el número después de moverte. Compara y escribe qué cambió. Si te sientes mal, para y descansa. No hagas ejercicio fuerte si un médico te dijo que no.",
  ],
  vocab=[("actividad física", "movimiento que hace trabajar los músculos"), ("reposo", "estar quieto, sentado o acostado"), ("pulso", "golpecito de la muñeca que muestra los latidos"), ("sudar", "soltar agua por la piel cuando hay calor"), ("descansar", "parar y recuperar fuerzas")],
  worked=[
      ("Comparar el pulso", "En reposo, Marta cuenta 20 latidos en 15 segundos. Después de 20 saltos suaves cuenta 30. ¿Cuántos latidos más tiene?", ["Resto el pulso de reposo al de después.", "30 − 20 = 10.", "Su corazón late más rápido."], "10 latidos más; el corazón late más rápido"),
      ("Describir los cambios", "Después de correr, Pablo respira más rápido y tiene calor. ¿Es normal?", ["El cuerpo trabaja más al moverse.", "Respirar más rápido y sentir calor son cambios esperables.", "Si se siente mal, debe parar."], "Sí, es normal"),
  ],
  mistakes=[
      ("Medir el pulso en reposo en un momento y el otro después de correr, pero con tiempos distintos.", "Se comparan datos medidos de forma distinta.", "Mide los dos pulsos durante el mismo tiempo, por ejemplo 15 segundos."),
      ("Seguir haciendo ejercicio aunque duela algo.", "No se escucha al cuerpo.", "Para, descansa y avisa a un adulto si duele o te mareas."),
  ],
  rec=[
      ("En reposo, ¿el pulso es más lento o más rápido que después de correr?", "Más lento", "Moverse hace latir más rápido."),
      ("Después de correr, ¿respiras más rápido o más lento?", "Más rápido", "El cuerpo necesita más aire."),
      ("¿Correr es actividad física?", "Sí", "Hace trabajar los músculos."),
  ],
  und=[
      ("¿Qué es el reposo?", "Estar quieto, sentado o acostado", "Es el estado sin movimiento."),
      ("Nombra tres cambios en tu cuerpo al hacer actividad física.", "Respiro más rápido, el corazón late más rápido y siento calor", "Son cambios esperables."),
      ("¿Por qué hay que medir igual antes y después?", "Para poder comparar bien", "Si se mide distinto no se puede comparar."),
  ],
  app=[
      arith("En reposo, Luis tiene 18 latidos en 15 segundos y después de saltar tiene 29. ¿Cuántos latidos más son?", "29-18", "Se resta el pulso de reposo al de después."),
      ("Registro: reposo 20 latidos; después de saltar 30 latidos (en 15 segundos). ¿Cuándo late más rápido el corazón?", "Después de saltar", "El número es mayor."),
      ("Ana siente calor y respira más rápido después de bailar 5 minutos. ¿Es una señal de que su cuerpo trabaja o de que está enferma?", "De que su cuerpo trabaja", "Son cambios normales del ejercicio."),
  ],
  rea=[
      ("Un niño midió 20 latidos en reposo durante 15 segundos y 31 latidos después de correr durante 30 segundos. ¿Por qué no se pueden comparar bien?", "Porque midió con tiempos distintos", "Hay que medir igual tiempo."),
      ("Si después de un juego te duele el pecho, ¿qué haces?", "Paro, descanso y aviso a un adulto", "Un dolor es una señal para parar."),
  ],
  cha=[
      ("Elige una actividad física y escribe dos cambios que notarás en tu cuerpo.", "Por ejemplo: correr y respirar más rápido y sentir calor", "Son cambios del ejercicio."),
      ("¿Por qué conviene tener agua cerca al hacer ejercicio?", "Porque el cuerpo pierde agua al sudar", "Hay que reponerla."),
  ],
  context=[("En la hora de recreo, Camila juega a la escondida y nota que respira más rápido. Se detiene a tomar agua. ¿Es buena idea parar y tomar agua? Explica.", "Sí, porque el cuerpo suda y necesita agua", "Beber agua ayuda al cuerpo.")],
  selfcheck=[("¿Respiras más rápido o más lento al moverte?", "Más rápido", "El cuerpo necesita más aire."), ("¿El pulso aumenta al hacer actividad?", "Sí", "El corazón late más rápido."), ("¿Qué haces si te mareas?", "Paro y aviso a un adulto", "Es lo más seguro.")],
  open_task=task("Con un adulto cerca, mide tu pulso en reposo durante 15 segundos. Luego salta suave 20 veces y mide de nuevo. Anota los dos números, la diferencia y dos cosas más que sientas en el cuerpo. Si te mareas o te duele algo, para y avisa.", "Reposo: 21 latidos. Después de saltar: 30 latidos. Diferencia: 9 latidos. Sentí calor y respiré más rápido.", ["anota dos pulsos medidos igual", "calcula la diferencia", "describe dos cambios más"], ["tabla con dos números", "diferencia", "frase de cambios"], ["medir en tiempos distintos", "seguir si hay dolor"], "Revisa que los tiempos sean iguales y que la resta esté bien hecha."),
  reinforce="Cuenta cuántas veces respiras en 30 segundos sentado y otra vez después de 15 saltitos suaves.",
  extend="Piensa en una actividad física que te guste y escribe cómo cambia tu respiración al hacerla.")

L(OA8, 2,
  materials="Este cuaderno y lápices de colores. Para sentir tus músculos: tus propias piernas y brazos.",
  use="Aprenderé cómo el ejercicio ayuda a que los músculos se desarrollen y se pongan más fuertes. Sirve para entender por qué moverte todos los días es bueno.",
  prior=["Sé que los músculos mueven los huesos.", "Sé que moverse hace respirar más rápido."],
  explain=[
      "Los músculos se hacen más fuertes cuando se usan. Si caminas, corres, saltas, trepas o nadas todos los días, tus músculos trabajan y se desarrollan. Un músculo que se usa poco se queda débil.",
      "Cada actividad ejercita músculos distintos. Correr y saltar trabajan las piernas. Trepar y colgarse trabajan los brazos y la espalda. Jugar a la pelota y nadar trabajan casi todo el cuerpo. Por eso conviene variar las actividades.",
      "Los músculos fuertes ayudan a que cargues tu mochila, subas escaleras y no te canses tan rápido. También ayudan a sostener bien la espalda. Para que el ejercicio sea seguro, calienta antes con movimientos suaves y descansa después.",
  ],
  vocab=[("fuerte", "con capacidad de hacer más trabajo"), ("desarrollarse", "crecer y mejorar con el tiempo"), ("ejercitar", "usar los músculos con una actividad física"), ("calentar", "mover el cuerpo suavemente antes del ejercicio"), ("variar", "hacer cosas distintas")],
  worked=[
      ("Relacionar actividad y músculo", "¿Qué músculos trabajan al trepar un juego de plaza?", ["Al trepar se usan los brazos para agarrarse.", "También se usan las piernas para empujar.", "Trabajan brazos, piernas y espalda."], "Brazos, piernas y espalda"),
      ("Usar o no usar", "Dos niños: uno camina todos los días 30 minutos y otro casi no se mueve. ¿Qué músculos serán más fuertes?", ["Los músculos se desarrollan al usarse.", "El primero los usa cada día.", "El segundo los usa poco."], "Los del niño que camina cada día"),
  ],
  mistakes=[
      ("Decir «los músculos se hacen fuertes descansando todo el día».", "Se olvida que se necesita usarlos.", "Los músculos se fortalecen al usarlos, y también necesitan descanso."),
      ("Hacer solo una actividad todos los días.", "No se trabajan todos los músculos.", "Varía: corre, salta, trepa, juega a la pelota."),
  ],
  rec=[
      ("¿Qué pasa con un músculo que se usa poco?", "Se queda débil", "Necesita usarse para fortalecerse."),
      ("¿Correr trabaja las piernas?", "Sí", "Las piernas empujan el cuerpo."),
      ("Antes de hacer ejercicio, ¿se calienta o se queda quieto?", "Se calienta", "Prepara los músculos."),
  ],
  und=[
      ("¿Cómo se ponen más fuertes los músculos?", "Usándolos con actividad física", "El ejercicio los desarrolla."),
      ("¿Por qué conviene variar las actividades?", "Porque trabajan músculos distintos", "Cada actividad ejercita partes distintas."),
      ("¿Para qué sirve calentar?", "Para preparar los músculos", "Evita molestias en los músculos."),
  ],
  app=[
      ("Une cada actividad con lo que más trabaja: A correr, B colgarse de una barra, C nadar. Lo que trabaja: 1 brazos y espalda, 2 casi todo el cuerpo, 3 piernas. Escribe los pares.", "A3, B1, C2", "Cada actividad ejercita esas partes."),
      arith("Un niño hace 10 sentadillas suaves en la mañana y 10 en la tarde, cada día durante 5 días. ¿Cuántas sentadillas hace en total?", "(10+10)*5", "Primero las del día y luego se multiplican por 5 días."),
      ("Un niño quiere ejercitar las piernas. ¿Qué actividad le sirve más: saltar la cuerda o mirar televisión?", "Saltar la cuerda", "Salta con las piernas."),
  ],
  rea=[
      ("Un compañero dice: «Para tener músculos fuertes, no tengo que moverme». ¿Qué le respondes?", "Que los músculos se fortalecen al usarlos", "Sin uso se quedan débiles."),
      ("Dos niños hacen ejercicio: uno solo corre y otro corre, trepa y nada. ¿Cuál ejercita más partes del cuerpo y por qué?", "El segundo, porque hace actividades distintas", "Variar trabaja más músculos."),
  ],
  cha=[
      ("Escribe una actividad para ejercitar los brazos y otra para las piernas que puedas hacer en una plaza.", "Brazos: colgarme de una barra; piernas: correr", "Cada una trabaja esas partes."),
      ("¿Por qué el descanso también es parte de hacer ejercicio?", "Porque los músculos se recuperan", "Después de usarlos necesitan descansar."),
  ],
  context=[("En la plaza hay un banco para sentarse, una barra para colgarse y una cancha para correr. Un niño quiere ejercitar brazos y piernas. Escribe dos de esas tres cosas que le sirven.", "La barra para los brazos y la cancha para las piernas", "Cada una ejercita partes distintas.")],
  selfcheck=[("¿Los músculos se fortalecen con uso o sin uso?", "Con uso", "El ejercicio los desarrolla."), ("¿Es bueno variar la actividad?", "Sí", "Se ejercitan más músculos."), ("¿Hay que calentar antes?", "Sí", "Prepara los músculos.")],
  open_task=task("Haz una tabla con cuatro actividades que te gusten: por ejemplo correr, saltar la cuerda, trepar y nadar. Escribe en cada una qué músculos usa y dibuja una de ellas. Escribe una regla de seguridad para hacerla.", "Correr: piernas. Saltar la cuerda: piernas y brazos. Trepar: brazos y espalda. Nadar: casi todo el cuerpo. Regla: calentar y tomar agua.", ["nombra cuatro actividades", "dice qué músculos usa", "dibuja una", "escribe una regla de seguridad"], ["tabla de cuatro filas", "dibujo"], ["no variar las actividades", "olvidar la seguridad"], "Valora la relación actividad-músculo y pide una regla de seguridad realista."),
  reinforce="Haz con un adulto tres movimientos suaves de calentamiento y nombra qué músculos usas.",
  extend="Elige un deporte que te guste y escribe qué músculos crees que trabaja.")

L(OA8, 3,
  materials="Este cuaderno y lápices de colores. Para medir el pulso: reloj con segundos y tus dedos en la muñeca.",
  use="Aprenderé cómo el corazón se fortalece con el ejercicio. Sirve para entender por qué moverte todos los días cuida tu corazón.",
  prior=["Sé tomar el pulso en 15 segundos.", "Sé que el corazón es un músculo."],
  explain=[
      "El corazón es un músculo. Igual que otros músculos, se fortalece cuando se ejercita. Cuando haces actividad física, tu corazón late más rápido para llevar sangre a los músculos que trabajan. Con el ejercicio regular, el corazón se hace más fuerte.",
      "Un corazón fuerte necesita latir menos veces para mover la sangre. Por eso, muchas personas que hacen ejercicio con frecuencia tienen un pulso en reposo más bajo. Después de correr, el pulso sube, y al descansar vuelve poco a poco a su valor de reposo.",
      "El corazón también necesita descanso. Si te cansas mucho, para, siéntate y respira lento. Si el corazón late muy fuerte y tarda en calmarse, o sientes mareo o dolor, avisa a un adulto. Los números de esta clase son de práctica y sirven para aprender a leer un registro.",
  ],
  vocab=[("corazón fuerte", "corazón que mueve más sangre con cada latido"), ("pulso en reposo", "latidos cuando estás tranquilo y sentado"), ("recuperarse", "volver al estado normal después del esfuerzo"), ("regular", "que se hace seguido, con constancia"), ("mareo", "sensación de que todo da vueltas")],
  worked=[
      ("Leer un registro", "Registro de práctica: reposo 20 latidos, después de correr 34, tras 3 minutos de descanso 24. ¿Cuándo late más rápido?", ["Comparo los tres números.", "34 es el mayor.", "Es después de correr."], "Después de correr"),
      ("Recuperarse", "En el registro anterior, ¿el pulso vuelve a su valor de reposo después de 3 minutos?", ["El reposo era 20.", "A los 3 minutos es 24.", "Aún no vuelve, pero baja."], "Todavía no, pero baja"),
  ],
  mistakes=[
      ("Decir «mi corazón se hace más fuerte si no me muevo».", "Se piensa que el reposo basta.", "El corazón se fortalece con actividad regular y también necesita descanso."),
      ("Seguir corriendo aunque el corazón lata muy fuerte y estés mareado.", "No se escucha al cuerpo.", "Para, siéntate, respira lento y avisa a un adulto."),
  ],
  rec=[
      ("¿Qué órgano late más rápido cuando haces ejercicio?", "El corazón", "Lleva más sangre a los músculos."),
      ("¿El corazón es un músculo?", "Sí", "Se aprieta y se suelta."),
      ("Después de descansar, ¿el pulso baja o sube?", "Baja", "El corazón se recupera descansando."),
  ],
  und=[
      ("¿Por qué el corazón late más rápido cuando corres?", "Para llevar más sangre a los músculos", "Los músculos necesitan más."),
      ("¿Qué pasa con un corazón que se ejercita con frecuencia?", "Se hace más fuerte", "Es un músculo."),
      ("¿Por qué hay que descansar después del ejercicio?", "Para que el cuerpo se recupere", "El corazón vuelve a su ritmo."),
  ],
  app=[
      arith("Registro de práctica: reposo 22 latidos, después de correr 36. ¿Cuántos latidos más hay después de correr?", "36-22", "Se resta el pulso de reposo al de después."),
      ("Registro de práctica: reposo 20, después de saltar 32, a los 2 minutos 25. ¿Qué pasó entre saltar y descansar?", "El pulso bajó", "32 bajó a 25."),
      arith("Ema tiene 24 latidos en 15 segundos en reposo. ¿Cuántos latidos tiene en 1 minuto si late igual?", "24*4", "Un minuto tiene cuatro veces 15 segundos."),
  ],
  rea=[
      ("En un ejemplo de práctica, A no hace ejercicio y tiene pulso en reposo de 22; B hace ejercicio con frecuencia y tiene 18. Según lo aprendido, ¿cuál tiene probablemente el corazón más fuerte?", "B, porque su pulso en reposo es más bajo", "Un corazón fuerte late menos veces en reposo; es solo un ejemplo de práctica."),
      ("Un niño dice que su pulso no cambió después de correr 5 minutos: 20 antes y 20 después. ¿Qué podría haber pasado?", "Quizás midió mal o corrió muy suave", "El pulso suele subir con el ejercicio."),
  ],
  cha=[
      ("Un registro de práctica: reposo 19, después de correr 33, a los 3 min 23, a los 6 min 19. ¿Cuántos minutos tardó en volver al reposo?", "6 minutos", "A los 6 minutos volvió a 19."),
      ("¿Por qué es mejor hacer ejercicio un poco todos los días que mucho un solo día?", "Porque el cuerpo se acostumbra y se fortalece con constancia", "El ejercicio regular ayuda más."),
  ],
  context=[("En la clase de educación física, Tomás corre y su pulso sube de 21 a 33 latidos en 15 segundos. ¿Cuántos latidos subió?", "12", "33 − 21 = 12.")],
  selfcheck=[("¿El corazón se ejercita con actividad física?", "Sí", "Es un músculo."), ("¿Qué le pasa al pulso al descansar?", "Baja", "Vuelve a su valor normal."), ("¿Qué haces si estás muy cansado o mareado?", "Paro y aviso a un adulto", "Es lo más seguro.")],
  open_task=task("Observa este registro de práctica: reposo 20 latidos, después de correr 35 latidos, a 1 minuto 29, a 3 minutos 22. Haz un gráfico con cuatro barras. Escribe cuánto subió el pulso, cuánto bajó a los 3 minutos y una regla de seguridad.", "Subió 15 latidos (35 − 20). A los 3 minutos bajó 13 (35 − 22). Regla: si me mareo, paro.", ["dibuja cuatro barras", "calcula cuánto subió", "calcula cuánto bajó", "escribe una regla de seguridad"], ["gráfico de barras", "dos restas", "frase de seguridad"], ["restar al revés", "no escribir la regla"], "Revisa las dos restas y pide que explique qué significa que el pulso baje."),
  reinforce="Con un adulto cerca, mide tu pulso en reposo en 15 segundos tres días seguidos y anota los números.",
  extend="Averigua con un adulto por qué los atletas descansan entre una carrera y otra.")

L(OA8, 4,
  materials="Este cuaderno, una hoja para hacer un calendario semanal y lápices de colores. Elige actividades seguras y con un adulto cerca.",
  use="Aprenderé a armar un plan de actividad física para toda la semana. Sirve para incorporar el movimiento en tus hábitos diarios.",
  prior=["Sé que el ejercicio ayuda a los músculos y al corazón.", "Sé leer un calendario de la semana."],
  explain=[
      "Un hábito es algo que haces seguido, casi sin pensarlo, como lavarte los dientes. La actividad física puede ser un hábito. Las personas de tu edad deberían hacer, en total, unos 60 minutos de actividad física al día, en promedio, según la Organización Mundial de la Salud. Es actividad que te hace respirar más rápido.",
      "No hace falta hacer todo junto. Puedes sumar 20 minutos de caminata al colegio, 20 de juego en el recreo y 20 de baile en casa. Elige actividades que te gusten y que sean seguras para tu espacio, como correr en una plaza o saltar la cuerda.",
      "Un buen plan tiene días, actividades y tiempos. También tiene reglas de seguridad: calentar, usar zapatillas, tomar agua, ir acompañado y descansar. Si un día no puedes, anota cuándo lo harás. Un plan posible es mejor que un plan perfecto.",
  ],
  vocab=[("hábito", "algo que haces seguido y se vuelve costumbre"), ("plan", "lista de qué, cuándo y cuánto voy a hacer"), ("minutos", "unidad de tiempo; 60 minutos son una hora"), ("seguridad", "cuidarse para no hacerse daño"), ("constancia", "hacer algo seguido, sin rendirse")],
  worked=[
      ("Sumar minutos", "Un niño camina 15 minutos al colegio, juega 25 en el recreo y baila 20 en casa. ¿Cuántos minutos hace en el día?", ["Sumo los minutos: 15 + 25.", "15 + 25 = 40.", "40 + 20 = 60."], "60 minutos"),
      ("Revisar la seguridad", "Un plan dice «correr en la calle sin adulto». ¿Es seguro?", ["Los autos pueden ser un peligro.", "Falta un adulto cerca.", "Es mejor correr en una plaza con un adulto."], "No es seguro; se cambia por una plaza con un adulto"),
  ],
  mistakes=[
      ("Hacer un plan con actividades que no puedo hacer en mi casa.", "Se elige sin pensar en el espacio.", "Elige actividades posibles en tu casa, tu plaza o tu escuela."),
      ("Olvidar la seguridad en el plan.", "No se piensa en los riesgos.", "Agrega calentar, tomar agua, ir acompañado y descansar."),
  ],
  rec=[
      ("¿Un hábito es algo que haces una sola vez o seguido?", "Seguido", "Una costumbre se repite."),
      ("¿Cuántos minutos son una hora?", "60", "Una hora tiene 60 minutos."),
      ("¿Hay que tomar agua al hacer ejercicio?", "Sí", "El cuerpo pierde agua al sudar."),
  ],
  und=[
      ("¿Por qué es mejor un plan posible que uno perfecto?", "Porque se puede cumplir", "Un plan irreal se abandona."),
      ("¿Qué partes tiene un buen plan de actividad física?", "Días, actividades, tiempos y seguridad", "Son las partes de la clase."),
      ("¿Por qué conviene elegir actividades que te gusten?", "Porque es más fácil hacerlas seguido", "Se vuelven hábito."),
  ],
  app=[
      arith("Un niño juega 20 minutos el lunes, 25 el martes y 15 el miércoles. ¿Cuántos minutos suma en esos tres días?", "20+25+15", "Se suman los minutos de los tres días."),
      arith("Se recomiendan 60 minutos al día. Hoy Nico hizo 35. ¿Cuántos minutos le faltan?", "60-35", "Se resta lo que hizo a lo recomendado."),
      ("Plan: lunes caminar 30 min, martes saltar la cuerda 20 min, miércoles descansar. ¿Qué día no tiene actividad?", "El miércoles", "El plan dice descansar ese día."),
  ],
  rea=[
      ("Un compañero propone «jugar a la pelota en la calle con autos pasando». ¿Es un plan seguro? Explica.", "No; hay peligro de autos", "Se busca una plaza o patio."),
      ("¿Por qué conviene incluir un día de descanso en la semana?", "Porque el cuerpo se recupera", "Los músculos y el corazón descansan."),
  ],
  cha=[
      ("Arma un día con tres actividades que sumen 60 minutos. Escribe las actividades y los minutos.", "Por ejemplo: caminar 20, jugar 25 y bailar 15", "20 + 25 + 15 = 60."),
      ("¿Cómo podrías sumar actividad física en un día de lluvia?", "Bailando o saltando la cuerda en casa", "Se puede mover dentro de casa."),
  ],
  context=[("Camila camina 10 minutos de ida y 10 de vuelta al colegio y juega 25 minutos en el recreo. ¿Cuántos minutos de actividad suma?", "45", "10 + 10 + 25 = 45.")],
  selfcheck=[("¿Cuántos minutos al día se recomiendan para niños de tu edad?", "60", "Es una recomendación de salud."), ("¿Un plan debe tener reglas de seguridad?", "Sí", "Para no hacerse daño."), ("¿Qué es un hábito?", "Algo que haces seguido", "Se vuelve costumbre.")],
  open_task=task("Arma tu plan de la semana en una tabla de siete días. Escribe en cada día una actividad que te guste y cuántos minutos. Marca un día de descanso. Al final escribe tres reglas de seguridad y suma los minutos de la semana.", "Lunes: caminar 30. Martes: saltar la cuerda 20. Miércoles: bailar 30. Jueves: descanso. Viernes: jugar 40. Sábado: andar en bici con casco y con un adulto 45. Domingo: pasear 30. Reglas: calentar, tomar agua, ir acompañado. Total: 195 minutos.", ["incluye siete días", "marca un día de descanso", "suma los minutos", "escribe tres reglas de seguridad"], ["tabla semanal", "suma total", "tres reglas"], ["plan sin seguridad", "actividades imposibles de hacer"], "Revisa la suma y la seguridad, y pide que cambie una actividad que no pueda hacer en su casa."),
  reinforce="Pega tu plan en un lugar visible de la casa y marca cada día que lo cumplas con un color.",
  extend="Habla con tu familia y propongan una actividad física que puedan hacer juntos una vez a la semana.")
