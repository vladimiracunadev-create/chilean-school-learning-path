"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 14 (sistema Tierra-Luna-Sol, eclipses y estaciones)."""
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


OA = "CN1M OA 14"

L(OA, 1,
  materials="Este cuaderno, lápiz y calculadora. Para el modelo puedes usar una pelota o fruta redonda con un adhesivo, un palito o lápiz, y la linterna de un celular en una pieza oscura (nunca la apuntes a los ojos).",
  use="Aprenderé cómo los movimientos de rotación y traslación de la Tierra y de la Luna explican el día, la noche y el año. Sirve para construir modelos con una linterna y una pelota.",
  prior=["Sé que la Tierra, la Luna y el Sol son cuerpos esféricos.", "Sé calcular una división y usar grados."],
  explain=[
      "La Tierra se mueve de dos formas. La rotación es el giro alrededor de su eje, una línea imaginaria que pasa por los polos; dura unas 24 horas y produce el día y la noche, porque en cada momento solo la mitad de la Tierra mira al Sol. Gira de oeste a este, por eso el Sol parece salir por el este y ponerse por el oeste. La traslación es el recorrido alrededor del Sol, su órbita, que dura unos 365 días y 6 horas; cada cuatro años esas horas suman un día extra y hay un año bisiesto de 366 días.",
      "El eje de la Tierra está inclinado unos 23,5° respecto del plano de su órbita. Esa inclinación se mantiene casi igual durante todo el año y será clave para entender las estaciones. La Luna gira alrededor de la Tierra en unos 27 días y, en el mismo tiempo, rota una vez sobre su eje; por eso siempre vemos la misma cara de la Luna. El ciclo de las fases dura unos 29 días y medio, porque la Tierra también avanza en su órbita.",
      "Un modelo es una representación simplificada que sirve para explicar y predecir. Con una linterna (el Sol) y una pelota (la Tierra) con un adhesivo (tu ciudad) puedes reproducir el día y la noche. Una buena pregunta investigable para este modelo es: «¿Cuánto debo girar la pelota para pasar del mediodía a la medianoche?», porque se contesta midiendo el giro.",
  ],
  vocab=[("rotación", "giro de un cuerpo alrededor de su eje"), ("traslación", "recorrido de un cuerpo alrededor de otro, a lo largo de su órbita"), ("eje", "línea imaginaria alrededor de la cual gira un cuerpo"), ("órbita", "trayectoria que sigue un cuerpo alrededor de otro"), ("año bisiesto", "año de 366 días que ocurre cada cuatro años"), ("modelo", "representación simplificada para explicar o predecir un fenómeno")],
  worked=[
      ("Giro por hora", "La Tierra gira 360° en 24 horas. ¿Cuántos grados gira en 1 hora?", ["Divido el giro total por las horas.", "Calculo 360 ÷ 24."], "15° por hora"),
      ("Mediodía y medianoche", "En una ciudad de Chile es mediodía. ¿Qué ocurre en el lado opuesto de la Tierra?", ["Cuando un lado mira al Sol, el opuesto no recibe su luz.", "El lado opuesto está a media vuelta, 12 horas de diferencia."], "Es medianoche"),
  ],
  mistakes=[
      ("Creer que la noche ocurre porque el Sol se apaga o se esconde detrás de la Tierra.", "El Sol sigue iluminando; el lado de la Tierra que no lo mira queda sin luz por la rotación.", "Dibuja el Sol, la Tierra y la mitad iluminada."),
      ("Confundir rotación con traslación.", "La rotación produce el día y la noche; la traslación dura un año.", "Asocia rotación con «giro» y traslación con «recorrido»."),
  ],
  rec=[
      ("¿Qué movimiento de la Tierra produce el día y la noche?", "La rotación", "Hace que cada lugar pase por la zona iluminada y la oscura."),
      ("¿Cuántos días dura, aproximadamente, la traslación de la Tierra?", "Unos 365 días", "Ese es el año."),
      ("Verdadero o falso: la Luna siempre muestra la misma cara a la Tierra.", "Verdadero", "Rota en el mismo tiempo que orbita."),
  ],
  und=[
      ("El Sol parece salir por el este porque: A) la Tierra gira de oeste a este B) el Sol se mueve de este a oeste alrededor de la Tierra", "A", "El movimiento aparente del Sol es producto de la rotación."),
      ("En un modelo con linterna y pelota, ¿qué representa la linterna?", "El Sol", "Es la fuente de luz del modelo."),
      ("Un año bisiesto tiene un día más que uno normal. ¿Cuántos días tiene en total?", "366", "El día extra reúne las horas sobrantes de cuatro años."),
  ],
  app=[
      arith("La Tierra gira 360° en 24 horas. ¿Cuántos grados gira en 6 horas?", "360/24*6", "Se calcula el giro por hora y se multiplica por 6.", "°"),
      arith("Un año no bisiesto tiene 365 días y uno bisiesto tiene 366. ¿Cuántos días suman 3 años no bisiestos y 1 bisiesto?", "365*3+366", "Se suman los días de cada año.", " días"),
      arith("Un lugar B está 45° al oeste de un lugar A. La Tierra gira 15° por hora, así que B tiene mediodía más tarde que A. ¿Cuántas horas después?", "45/15", "Se divide la diferencia de ángulo por el giro por hora.", " h"),
  ],
  rea=[
      ("Sofía dice: «Es de noche porque el Sol deja de iluminar la Tierra al alejarse». ¿Qué respuesta es correcta? A) Es de noche en el lado que no mira al Sol, por la rotación B) Tiene razón, porque el Sol se aleja", "A", "La distancia al Sol casi no cambia en un día."),
      ("Tienes una linterna, una pelota y un palito. ¿Qué pregunta es investigable? A) ¿Cómo cambia la sombra del palito en la pelota al girarla? B) ¿Es lindo el amanecer?", "A", "Se puede observar y medir cómo se mueve la sombra."),
  ],
  cha=[
      arith("Un planeta de ejemplo gira una vuelta completa en 12 horas. ¿Cuántos grados gira por hora?", "360/12", "Se divide una vuelta completa por las horas que dura.", "°"),
      ("En tu modelo mueves la pelota alrededor de la linterna sin hacerla girar sobre su eje. ¿Qué movimiento real representas: rotación o traslación?", "Traslación", "Solo recorres una órbita alrededor del Sol."),
  ],
  context=[arith("La traslación dura 365 días y unas 6 horas. ¿Cuántas horas sobrantes se acumulan en 4 años?", "6*4", "Se multiplica el sobrante de un año por 4: 24 horas son un día más.", " horas")],
  selfcheck=[("¿Qué produce la rotación de la Tierra?", "El día y la noche", "Cada lugar entra y sale de la zona iluminada."), ("¿Por qué existe el año bisiesto?", "Porque el año dura 365 días y unas 6 horas", "Las horas sobrantes suman un día cada cuatro años."), ("¿Qué inclinación tiene el eje terrestre?", "Unos 23,5°", "Se mantiene durante el año.")],
  open_task=task("Con la pelota, el adhesivo (tu ciudad) y la linterna, haz el modelo del día y la noche. Gira la pelota de oeste a este, es decir, en sentido contrario al de las agujas del reloj mirándola desde arriba, sobre el polo norte. Completa esta tabla: giro de 0 (adhesivo frente a la linterna, mediodía), un cuarto de vuelta, media vuelta y tres cuartos de vuelta; escribe la hora aproximada y qué ves. Si no tienes materiales, dibuja las cuatro posiciones.", "0: mediodía, el adhesivo está en pleno sol. Un cuarto: unas 18:00, atardece. Media vuelta: medianoche, el adhesivo está en la sombra. Tres cuartos: unas 6:00, amanece.", ["cuatro posiciones con hora", "describe luz o sombra en cada una", "gira de oeste a este", "explica que la rotación produce el ciclo"], ["tabla o dibujos de cuatro posiciones"], ["girar la pelota al revés", "decir que el Sol se mueve"], "Pregunta qué cambia en el modelo si quieres representar un año completo."),
  reinforce="Calcula cuántos grados gira la Tierra en 3 horas.",
  extend="Explica por qué el hecho de que la Luna rote y orbite en el mismo tiempo hace que veamos siempre la misma cara.")

L(OA, 2,
  materials="Este cuaderno, lápiz y calculadora. Para el modelo, una pelota clara y una linterna en una pieza oscura (nunca la apuntes a los ojos). Los datos de observaciones son de ejemplo.",
  use="Aprenderé por qué la Luna muestra fases y cuánto dura el ciclo. Sirve para explicar el calendario lunar y predecir cómo se verá la Luna.",
  prior=["Sé que la Luna orbita la Tierra y que la Tierra orbita el Sol.", "Sé que la luz viaja en línea recta y forma sombras."],
  explain=[
      "La Luna no emite luz propia: refleja la luz del Sol. Siempre está iluminada la mitad que mira al Sol. Mientras la Luna orbita la Tierra, desde aquí vemos una parte distinta de esa mitad iluminada. Eso produce las fases lunares. No son la sombra de la Tierra: esa sombra produce los eclipses lunares.",
      "Las fases principales son cuatro. En luna nueva, la Luna está entre la Tierra y el Sol; su cara iluminada mira hacia el Sol y no la vemos. En cuarto creciente vemos la mitad iluminada y la parte visible aumenta cada noche. En luna llena, la Tierra está entre el Sol y la Luna, y vemos toda la cara iluminada. En cuarto menguante vemos de nuevo la mitad iluminada y la parte visible disminuye cada noche.",
      "El ciclo completo de una luna nueva a la siguiente dura unos 29 días y medio, aproximadamente 30 días. Cada fase principal ocurre aproximadamente cada 7 días. La luna llena sale al atardecer, cuando el Sol se pone, y se oculta al amanecer. La Luna nueva sale y se pone casi con el Sol, por eso no se ve.",
  ],
  vocab=[("fase lunar", "aspecto de la Luna según la parte iluminada que vemos"), ("luna nueva", "fase en que la Luna está entre la Tierra y el Sol y no se ve iluminada"), ("cuarto creciente", "fase en que vemos la mitad iluminada y la parte visible aumenta"), ("luna llena", "fase en que vemos toda la cara iluminada"), ("cuarto menguante", "fase en que vemos la mitad iluminada y la parte visible disminuye"), ("ciclo lunar", "tiempo entre dos fases iguales, de unos 29 días y medio")],
  worked=[
      ("Posición y fase", "La Luna está entre la Tierra y el Sol. ¿Qué fase tiene?", ["La cara iluminada mira al Sol, lejos de la Tierra.", "Desde la Tierra vemos la cara oscura."], "Luna nueva"),
      ("Días del ciclo", "Hoy hay luna nueva. ¿Aproximadamente cuántos días faltan para luna llena?", ["El ciclo completo dura unos 30 días.", "La luna llena queda a la mitad del ciclo: 30 ÷ 2."], "Unos 15 días"),
  ],
  mistakes=[
      ("Decir que las fases se deben a la sombra de la Tierra sobre la Luna.", "La sombra de la Tierra produce los eclipses; las fases se deben al ángulo desde el cual vemos la mitad iluminada.", "Dibuja Sol, Tierra y Luna y marca la mitad iluminada."),
      ("Creer que la parte oscura de la Luna no recibe nunca luz.", "Siempre se ilumina la mitad que mira al Sol; la «oscura» es la mitad que no vemos desde la Tierra en ese momento.", "Recuerda que la Luna tiene día y noche."),
  ],
  rec=[
      ("¿Qué fase se ve cuando la Tierra está entre el Sol y la Luna?", "Luna llena", "Vemos toda la cara iluminada."),
      ("Verdadero o falso: la Luna emite luz propia.", "Falso", "Solo refleja la luz del Sol."),
      ("¿Aproximadamente cuántos días hay entre dos lunas nuevas?", "Unos 30 días", "El ciclo dura unos 29 días y medio."),
  ],
  und=[
      ("Las fases de la Luna se deben a: A) la posición de la Luna respecto del Sol y la Tierra, que muestra una parte distinta de su cara iluminada B) la sombra de la Tierra sobre la Luna", "A", "La sombra de la Tierra produce eclipses, no fases."),
      ("En cuarto menguante, la parte iluminada que vemos cada noche: A) disminuye B) aumenta", "A", "La Luna avanza hacia la luna nueva."),
      ("¿Qué mitad de la Luna está siempre iluminada?", "La que mira al Sol", "El Sol ilumina siempre una mitad."),
  ],
  app=[
      arith("Si cada ciclo lunar dura unos 30 días y hoy hay luna nueva, ¿cuántas lunas nuevas más se esperan en los próximos 90 días?", "90/30", "Se divide el tiempo total por la duración de un ciclo.", " lunas nuevas"),
      arith("Una luna llena ocurre el día 1 de un mes. La luna nueva ocurre unos 15 días después. ¿En qué día del mes ocurre?", "1+15", "Se suman los días que faltan a la fecha de la luna llena.", ""),
      ("Si la luna llena sale cuando el Sol se pone, ¿cómo está hacia el amanecer? A) Poniéndose B) Saliendo", "A", "Su recorrido dura toda la noche."),
  ],
  rea=[
      ("Un compañero dice que la luna creciente es la sombra de la Tierra. ¿Qué respuesta es correcta? A) No: las fases se deben al ángulo desde donde vemos la mitad iluminada B) Sí: la Tierra tapa parte de la luz del Sol", "A", "La sombra de la Tierra tapa a la Luna solo durante los eclipses."),
      ("Un registro de ejemplo muestra: día 1, luna nueva; día 8, cuarto creciente; día 15, luna llena; día 22, cuarto menguante. ¿Alrededor de qué día se espera la siguiente luna nueva?", "Alrededor del día 30", "Cada fase principal se repite a intervalos de unos 7 días."),
  ],
  cha=[
      arith("Un año tiene 365 días y un ciclo lunar dura unos 30 días. ¿Cuántos ciclos completos caben en un año, aproximadamente?", "365//30", "Se divide el año por la duración del ciclo y se toma la parte entera.", " ciclos"),
      ("La Luna está en un punto de su órbita 7 días después de la luna nueva y su parte iluminada aumenta. ¿Qué fase es?", "Cuarto creciente", "Pasaron una cuarta parte del ciclo y la parte visible crece."),
  ],
  context=[ex("Una persona anota que hoy ve media Luna iluminada y que cada noche se ve más grande la parte iluminada. ¿En cuántos días aproximadamente habrá luna llena?", "Unos 7 días", "Del cuarto creciente a la luna llena pasa más o menos una semana.")],
  selfcheck=[("¿Por qué vemos fases de la Luna?", "Porque vemos desde la Tierra distintas partes de su mitad iluminada", "Depende de dónde está la Luna en su órbita."), ("¿Qué fase sigue a la luna llena en el ciclo lunar?", "Cuarto menguante", "Después de la luna llena la parte visible empieza a disminuir."), ("¿Cuántos días dura el ciclo lunar?", "Unos 29 días y medio", "Es aproximadamente un mes.")],
  open_task=task("En una pieza oscura, usa una linterna fija, una pelota clara (la Luna) y tu cabeza (la Tierra). Sostén la pelota con el brazo estirado, un poco más alta que tu cabeza para que tu sombra no la tape, y gira lentamente sobre ti en sentido contrario al de las agujas del reloj (mirado desde arriba), sin apuntar la linterna a los ojos. Dibuja y nombra las cuatro fases que ves en la pelota: cuando la pelota está entre tú y la linterna, a un lado, detrás de ti respecto de la linterna y al otro lado. Escribe cuántos días aproximados separan cada posición.", "Pelota entre tú y la linterna: luna nueva (día 0). A un lado: cuarto creciente (día 7). Detrás de ti: luna llena (día 15). Al otro lado: cuarto menguante (día 22). La mitad iluminada siempre mira a la linterna.", ["cuatro fases nombradas y dibujadas", "días aproximados 0, 7, 15 y 22", "explica que la mitad iluminada mira al Sol"], ["dibujos con rótulos"], ["decir que la pelota proyecta sombra sobre sí misma", "invertir luna nueva y llena"], "Pregunta cuál sería la fase si tu cabeza tapara la luz de la linterna."),
  reinforce="Escribe en orden las cuatro fases de la Luna durante un ciclo, empezando por la luna nueva.",
  extend="Explica por qué en luna nueva no se puede ver la Luna en el cielo nocturno.")

L(OA, 3,
  materials="Este cuaderno, lápiz y regla. Para observar un eclipse solar parcial, usa solo proyección con una cartulina con un agujero pequeño; nunca mires el Sol directamente. Los datos son de ejemplo.",
  use="Aprenderé cómo se producen los eclipses solares y lunares y cómo observarlos con seguridad. Sirve para predecir eclipses y cuidar la vista.",
  prior=["Sé las fases de la Luna.", "Sé que una fuente de luz y un objeto opaco forman una sombra."],
  explain=[
      "Un eclipse solar ocurre cuando la Luna se interpone entre el Sol y la Tierra, en luna nueva, y su sombra cae sobre una zona de la Tierra. Quien está en la umbra, la sombra más oscura, ve un eclipse total; quien está en la penumbra, la sombra parcial, ve uno parcial. Un eclipse lunar ocurre cuando la Tierra se interpone entre el Sol y la Luna, en luna llena, y la Luna entra en la sombra terrestre; la Luna se ve rojiza porque la atmósfera terrestre desvía luz roja hacia ella.",
      "No hay un eclipse cada mes porque la órbita de la Luna está inclinada unos 5° respecto del plano de la órbita de la Tierra. La mayoría de las lunas nuevas y llenas pasan por encima o por debajo de la sombra, y solo hay eclipse cuando Sol, Tierra y Luna quedan alineados. El eclipse solar total se ve desde una franja angosta y dura pocos minutos. El eclipse lunar se ve desde todo el lado nocturno y dura horas. Por una coincidencia, el Sol es unas 400 veces más grande que la Luna y está unas 400 veces más lejos, así que ambos se ven casi del mismo tamaño.",
      "Seguridad: nunca mires el Sol directamente, ni con lentes de sol, binoculares o telescopio sin filtro especial. La luz solar puede quemar la retina y causar daño permanente, aunque no duela. Una forma segura es la proyección con agujero: una cartulina con un agujero pequeño proyecta la imagen del Sol sobre el suelo o sobre una hoja. En Chile hubo eclipses solares totales el 2 de julio de 2019 y el 14 de diciembre de 2020.",
  ],
  vocab=[("eclipse solar", "fenómeno en que la Luna tapa total o parcialmente al Sol visto desde la Tierra"), ("eclipse lunar", "fenómeno en que la Luna entra en la sombra de la Tierra"), ("umbra", "parte más oscura de la sombra, donde el eclipse es total"), ("penumbra", "parte de la sombra con luz parcial, donde el eclipse es parcial"), ("alineación", "posición de tres cuerpos casi en línea recta"), ("proyección con agujero", "método seguro que forma la imagen del Sol sobre una superficie con un agujero pequeño")],
  worked=[
      ("Orden de los cuerpos", "El orden es Sol, Luna, Tierra. ¿Qué eclipse ocurre?", ["La Luna está en medio, entre el Sol y la Tierra.", "Su sombra cae sobre la Tierra."], "Eclipse solar"),
      ("Por qué no cada mes", "¿Por qué no hay eclipse en todas las lunas nuevas?", ["La órbita de la Luna está inclinada respecto de la órbita terrestre.", "Casi siempre la sombra pasa por arriba o por abajo de la Tierra."], "Porque la inclinación de la órbita lunar rara vez permite la alineación"),
  ],
  mistakes=[
      ("Mirar un eclipse solar parcial con lentes de sol comunes.", "Los lentes de sol no protegen la retina de la luz directa del Sol.", "Usa proyección con agujero o filtros especiales para eclipse."),
      ("Confundir eclipse lunar con fase lunar.", "El eclipse lunar es la sombra de la Tierra sobre la Luna; la fase es el ángulo de vista.", "Pregunta si la Luna entra en la sombra de la Tierra."),
  ],
  rec=[
      ("¿Qué cuerpo está en el medio durante un eclipse solar?", "La Luna", "Se interpone entre el Sol y la Tierra."),
      ("Verdadero o falso: el eclipse lunar ocurre en luna llena.", "Verdadero", "La Tierra está entre el Sol y la Luna."),
      ("¿Qué objeto proyecta la sombra en un eclipse lunar?", "La Tierra", "Su sombra cae sobre la Luna."),
  ],
  und=[
      ("Un eclipse solar total se ve desde: A) la zona donde cae la umbra B) toda la Tierra", "A", "La umbra cubre una franja angosta."),
      ("La Luna entra en la sombra de la Tierra durante: A) un eclipse lunar B) un eclipse solar", "A", "En el eclipse solar es la sombra de la Luna la que cae sobre la Tierra."),
      ("¿Cómo se puede mirar un eclipse solar parcial sin dañar los ojos? A) Con proyección de la imagen a través de un agujero pequeño B) Con lentes de sol comunes", "A", "La proyección evita mirar directamente al Sol."),
  ],
  app=[
      ("El orden de los cuerpos es Sol, Tierra, Luna, casi en línea recta. ¿Qué eclipse ocurre?", "Eclipse lunar", "La Luna entra en la sombra de la Tierra."),
      arith("Hubo eclipses solares totales en Chile en julio de 2019 y en diciembre de 2020. ¿Cuántos meses pasaron entre ambos?", "12+5", "De julio de 2019 a julio de 2020 hay 12 meses y de ahí a diciembre, 5 más.", " meses"),
      ("Un amigo quiere mirar un eclipse solar con binoculares sin filtro. ¿Qué corresponde responderle?", "Que no lo haga: puede dañar la retina de forma permanente", "La luz concentrada por los binoculares es aún más peligrosa."),
  ],
  rea=[
      ("¿Por qué el eclipse lunar se ve desde todo el lado nocturno, pero el solar total solo desde una franja? A) La sombra de la Luna sobre la Tierra es pequeña y la de la Tierra sobre la Luna es grande B) El eclipse lunar ocurre más cerca de la Tierra", "A", "La Luna es más pequeña que la Tierra y proyecta una sombra angosta."),
      ("Una compañera dice que siempre hay eclipse solar en luna nueva. ¿Qué respuesta es correcta? A) No: la órbita inclinada hace que la sombra suela pasar de largo B) Sí: en luna nueva la Luna siempre tapa el Sol", "A", "Solo hay eclipse si hay alineación."),
  ],
  cha=[
      ("El Sol es unas 400 veces más grande que la Luna y está unas 400 veces más lejos. ¿Cómo se ven sus tamaños desde la Tierra? A) Casi iguales B) El Sol mucho mayor", "A", "Las dos razones se compensan."),
      ("Hay luna llena el 3 de mayo y luna nueva el 18 de mayo (fechas de ejemplo). ¿Qué es cierto? A) El 3 de mayo puede haber un eclipse lunar y el 18 uno solar, si hay alineación B) No puede haber ningún eclipse", "A", "Los eclipses solo ocurren en luna nueva y los lunares en luna llena, si hay alineación."),
  ],
  context=[ex("Durante un eclipse solar parcial, una cartulina con un agujero pequeño proyecta la imagen del Sol sobre el suelo. ¿Qué forma tiene la imagen? A) La de un círculo al que le falta una parte, como una luna creciente B) La de un círculo completo", "A", "La imagen proyectada tiene la forma del Sol parcialmente tapado.")],
  selfcheck=[("¿Cuándo ocurre un eclipse lunar?", "Cuando la Tierra está entre el Sol y la Luna", "La Luna entra en la sombra de la Tierra."), ("¿Qué es la umbra?", "La sombra más oscura, donde el eclipse es total", "En la penumbra es parcial."), ("¿Cómo se mira un eclipse solar de forma segura?", "Con proyección de la imagen a través de un agujero", "Nunca se mira el Sol directamente.")],
  open_task=task("Dibuja dos esquemas con el Sol, la Tierra y la Luna en línea: uno para un eclipse solar y otro para uno lunar. En cada uno, marca la sombra, la umbra y la penumbra, la fase lunar y desde dónde se ve el eclipse total. Luego escribe tres pasos para observar un eclipse solar parcial con una cartulina que tenga un agujero pequeño hecho con la punta de un lápiz, sin mirar el Sol.", "Solar: Sol, Luna, Tierra; luna nueva; umbra sobre una franja de la Tierra. Lunar: Sol, Tierra, Luna; luna llena; la Luna entra en la sombra terrestre. Pasos: de espaldas al Sol, sostener la cartulina; dejar que la luz pase por el agujero; mirar la imagen en el suelo o en una hoja.", ["dos esquemas con el orden correcto", "umbra y penumbra marcadas", "fase en cada caso", "pasos que no implican mirar el Sol"], ["esquemas y tres pasos"], ["poner la Tierra en medio en el eclipse solar", "proponer mirar con lentes de sol"], "Pregunta por qué el eclipse total solar se ve desde una franja angosta."),
  reinforce="Escribe la fase lunar de un eclipse solar y la de un eclipse lunar.",
  extend="Explica por qué la Luna se ve rojiza durante un eclipse lunar total.")

L(OA, 4,
  materials="Este cuaderno, lápiz y calculadora. Para el modelo, una pelota con un palito inclinado y una linterna en una pieza oscura. Los datos son aproximados y están escritos en los ejercicios.",
  use="Aprenderé por qué existen las estaciones y por qué no se deben a la distancia al Sol. Sirve para explicar cambios del clima y de la duración del día.",
  prior=["Sé que la Tierra se traslada alrededor del Sol y que su eje está inclinado.", "Sé que la energía de la luz se reparte sobre una superficie."],
  explain=[
      "Las estaciones se deben a la inclinación del eje terrestre (unos 23,5°) combinada con la traslación. El eje apunta siempre en la misma dirección, así que durante el año unas veces el hemisferio sur se inclina hacia el Sol y otras se inclina hacia el lado contrario. Cuando el hemisferio sur se inclina hacia el Sol, los rayos llegan más directos, los días son más largos y es verano; cuando se inclina al lado contrario, los rayos llegan más oblicuos, los días son más cortos y es invierno. En ese mismo momento, el hemisferio norte tiene la estación opuesta.",
      "Los rayos más oblicuos reparten la misma energía sobre una superficie mayor, y por eso calientan menos. Los solsticios son los días de mayor y menor duración del día: en Chile ocurren alrededor del 21 de diciembre (verano) y del 21 de junio (invierno). Los equinoccios son los días en que día y noche duran casi lo mismo, alrededor del 20 de marzo (otoño) y del 22 de septiembre (primavera).",
      "No es la distancia al Sol lo que causa las estaciones. La Tierra está más cerca del Sol en enero, a unos 147 millones de km, y más lejos en julio, a unos 152 millones de km. Si la distancia fuera la causa, enero sería verano en los dos hemisferios. Pero en Chile enero es verano y en el hemisferio norte es invierno, con la Tierra a la misma distancia del Sol.",
  ],
  vocab=[("estación", "cada una de las cuatro épocas del año con clima y duración del día distintos"), ("solsticio", "día del año con la mayor o menor duración de luz del día"), ("equinoccio", "día en que el día y la noche duran casi lo mismo"), ("hemisferio", "mitad de la Tierra: norte o sur"), ("incidencia de los rayos", "ángulo con que llega la luz a una superficie"), ("inclinación del eje", "ángulo del eje de la Tierra respecto del plano de su órbita")],
  worked=[
      ("Estaciones opuestas", "En diciembre es verano en Chile. ¿Qué estación es en Alemania, en el hemisferio norte?", ["Cuando el hemisferio sur se inclina hacia el Sol, el norte se inclina al lado contrario.", "La estación en el norte es la opuesta."], "Invierno"),
      ("Descartar la distancia", "La Tierra está a 147 millones de km del Sol en enero y a 152 millones de km en julio. ¿Basta la distancia al Sol para explicar por qué enero es verano en Chile?", ["En enero la Tierra está más cerca, y es verano en Chile.", "Pero ese mismo mes es invierno en el hemisferio norte con la misma distancia."], "No: la distancia no explica las estaciones"),
  ],
  mistakes=[
      ("Decir que es verano porque la Tierra está más cerca del Sol.", "En enero es verano en el sur e invierno en el norte, con la misma distancia.", "Busca la causa en la inclinación del eje."),
      ("Creer que el Sol sale por el mismo punto todo el año.", "La posición del Sol y la duración del día cambian con las estaciones.", "Compara la altura del Sol al mediodía en verano e invierno."),
  ],
  rec=[
      ("¿Qué causa las estaciones del año?", "La inclinación del eje terrestre", "Combinada con la traslación."),
      ("¿Alrededor de qué fecha ocurre el solsticio de verano en Chile?", "Alrededor del 21 de diciembre", "Es el día con más horas de luz."),
      ("Verdadero o falso: en junio es invierno en Chile.", "Verdadero", "El hemisferio sur se inclina lejos del Sol."),
  ],
  und=[
      ("En un equinoccio, ¿cómo son las duraciones del día y la noche?", "Casi iguales", "Son cercanas a 12 horas cada una."),
      ("¿Por qué hace más calor en verano? A) Los rayos llegan más directos y los días son más largos B) La Tierra está muy cerca del Sol", "A", "Esas dos condiciones aumentan la energía recibida."),
      ("Cuando es otoño en Chile, ¿qué estación es en el hemisferio norte?", "Primavera", "Los hemisferios tienen estaciones opuestas."),
  ],
  app=[
      arith("En una ciudad de ejemplo, el Sol al mediodía está a 80° de altura en verano y a 35° en invierno. ¿Cuántos grados más alto está en verano?", "80-35", "Se resta la altura de invierno a la de verano.", "°"),
      arith("En una ciudad de ejemplo, el día dura 15 horas en el solsticio de verano y 9 horas en el de invierno. ¿Cuántas horas más de luz hay en verano?", "15-9", "Se restan las horas de luz.", " horas"),
      ("Usa estas fechas aproximadas en Chile: 20 de marzo, 21 de junio, 22 de septiembre y 21 de diciembre. ¿Cuál es el inicio de la primavera?", "Alrededor del 22 de septiembre", "Es el equinoccio de primavera en el hemisferio sur."),
  ],
  rea=[
      ("Un estudiante dice que es verano porque la Tierra está más cerca del Sol. ¿Qué evidencia lo contradice? A) En julio, cuando la Tierra está más lejos, es verano en Canadá B) En enero, la Tierra está más lejos", "A", "El verano del norte ocurre con la Tierra más lejos del Sol."),
      ("En el ecuador el día dura casi lo mismo todo el año. ¿Cuál es la razón principal? A) El eje inclinado cambia poco la duración del día cerca del ecuador B) El ecuador está más cerca del Sol", "A", "La variación de duración del día crece al alejarse del ecuador."),
  ],
  cha=[
      ("Si el eje de la Tierra no estuviera inclinado, ¿habría estaciones como las conocemos?", "No", "Los rayos incidirían igual todo el año."),
      arith("Un haz de rayos que cubre 1 m² cuando llega perpendicular cubre 2 m² cuando llega inclinado (valores de ejemplo). Si el haz trae 1.000 W de energía, ¿cuántos W llegan por m² en el caso inclinado?", "1000/2", "La misma energía se reparte en una superficie dos veces mayor.", " W/m²"),
  ],
  context=[ex("Un poste proyecta sombra al mediodía en Santiago. ¿En qué mes la sombra es más corta: diciembre o junio? A) Diciembre B) Junio", "A", "En diciembre el Sol está más alto y la sombra es más corta.")],
  selfcheck=[("¿Qué diferencia hay entre solsticio y equinoccio?", "En el solsticio el día es más largo o más corto y en el equinoccio día y noche son casi iguales", "Marcan los extremos y el equilibrio de la duración del día."), ("¿Por qué la distancia al Sol no explica las estaciones?", "Porque cuando es verano en un hemisferio es invierno en el otro, a la misma distancia", "Ambos hemisferios están a la misma distancia."), ("¿Qué pasa con la energía de los rayos oblicuos?", "Se reparte en una superficie mayor y calienta menos", "Menos energía por metro cuadrado.")],
  open_task=task("Con una pelota (la Tierra) con un palito inclinado hacia una pared, y una linterna sobre una mesa (el Sol), camina con la pelota alrededor de la linterna sin cambiar hacia dónde apunta el palito. Observa en cuatro posiciones si el hemisferio sur (el extremo inferior del palito) queda más iluminado o menos. Dibuja las cuatro posiciones, rotula verano e invierno del sur y explica por qué no es la distancia la que cambia. Si no tienes materiales, dibújalo.", "Cuando el extremo sur del palito se inclina hacia la linterna, el hemisferio sur recibe rayos más directos: verano en el sur. Media vuelta después, se inclina hacia el lado contrario: invierno. En las posiciones intermedias están el otoño y la primavera. La distancia casi no cambia.", ["cuatro posiciones dibujadas", "verano e invierno correctamente rotulados", "explica con la inclinación", "descarta la distancia"], ["dibujo con cuatro posiciones"], ["cambiar la dirección del palito en cada posición", "explicar con la distancia"], "Pregunta qué cambiaría en el modelo si el palito estuviera derecho."),
  reinforce="Escribe la estación de Chile en cada solsticio y equinoccio.",
  extend="Explica por qué las estaciones del hemisferio norte son opuestas a las del sur.")

L(OA, 5,
  materials="Este cuaderno, lápiz y calculadora. La tabla de planetas es de datos aproximados y está escrita en los ejercicios.",
  use="Aprenderé a comparar los planetas del sistema solar con la Tierra por su distancia al Sol, su tamaño, su período orbital y su atmósfera. Sirve para encontrar patrones en datos.",
  prior=["Sé qué es una órbita.", "Sé leer y comparar números en una tabla."],
  explain=[
      "Datos aproximados de los planetas. Distancia media al Sol (millones de km), diámetro (km), período orbital (tiempo de una vuelta al Sol) y atmósfera: Mercurio, 58, 4.900, 88 días, casi inexistente. Venus, 108, 12.100, 225 días, muy densa de dióxido de carbono. Tierra, 150, 12.700, 365 días, nitrógeno y oxígeno. Marte, 228, 6.800, 687 días, muy delgada de dióxido de carbono. Júpiter, 778, 140.000, 12 años, hidrógeno y helio. Saturno, 1.430, 116.000, 29 años, hidrógeno y helio. Urano, 2.870, 51.000, 84 años, hidrógeno, helio y metano. Neptuno, 4.500, 49.000, 165 años, hidrógeno, helio y metano.",
      "Hay dos grupos. Los planetas rocosos, Mercurio, Venus, Tierra y Marte, son pequeños, tienen superficie sólida y están cerca del Sol. Los planetas gigantes, Júpiter, Saturno, Urano y Neptuno, son mucho mayores y no tienen superficie sólida como la Tierra: Júpiter y Saturno son gaseosos, y Urano y Neptuno, helados.",
      "Un patrón importante: mientras más lejos del Sol, mayor es el período orbital, porque la órbita es más larga y el planeta se mueve más lento. Otro dato clave: Venus tiene una atmósfera tan densa que atrapa el calor del Sol y su superficie supera los 400 °C y en promedio es más caliente que la de Mercurio, que está más cerca. La Tierra es el único planeta conocido con agua líquida en su superficie y con vida.",
  ],
  vocab=[("planeta rocoso", "planeta pequeño de superficie sólida"), ("planeta gigante", "planeta de gran tamaño sin superficie sólida como la Tierra"), ("período orbital", "tiempo que tarda un planeta en dar una vuelta al Sol"), ("atmósfera", "capa de gases que rodea a un planeta"), ("efecto invernadero", "calentamiento causado por gases que atrapan el calor"), ("distancia media", "valor promedio de la distancia de un planeta al Sol")],
  worked=[
      ("Comparar tamaños", "¿Cuántas veces cabe, aproximadamente, el diámetro de la Tierra (12.700 km) en el de Júpiter (140.000 km)?", ["Divido el diámetro mayor por el menor.", "Calculo 140.000 ÷ 12.700 y tomo la parte entera."], "Unas 11 veces"),
      ("Vueltas por año", "Mercurio da una vuelta al Sol en 88 días. ¿Cuántas vueltas completas da en un año terrestre de 365 días?", ["Divido 365 por 88.", "El resultado, 4,1..., indica 4 vueltas completas."], "4 vueltas"),
  ],
  mistakes=[
      ("Pensar que el planeta más caliente es el más cercano al Sol.", "Venus, más lejano que Mercurio, es en promedio más caliente por su atmósfera densa.", "Considera la atmósfera además de la distancia."),
      ("Creer que los años de todos los planetas duran 365 días.", "El período orbital aumenta con la distancia al Sol.", "Mira el período orbital de cada planeta."),
  ],
  rec=[
      ("¿Qué planeta de la tabla está más cerca del Sol?", "Mercurio", "Su distancia media es de unos 58 millones de km."),
      ("¿Cuál planeta de la tabla tiene el mayor período orbital?", "Neptuno", "Tarda unos 165 años."),
      ("Verdadero o falso: Venus tiene una atmósfera muy delgada.", "Falso", "Su atmósfera es muy densa."),
  ],
  und=[
      ("Mientras más lejos está un planeta del Sol, su período orbital es: A) mayor B) menor", "A", "Recorre una órbita más larga y más lentamente."),
      ("¿Júpiter es un planeta rocoso o gigante?", "Gigante", "No tiene superficie sólida y su diámetro supera 140.000 km."),
      ("¿Cómo es la atmósfera de Marte?", "Muy delgada, de dióxido de carbono", "Es mucho menos densa que la terrestre."),
  ],
  app=[
      arith("Marte está a 228 millones de km del Sol y la Tierra a 150 millones de km. ¿Cuántos millones de km más lejos del Sol está Marte?", "228-150", "Se resta la distancia de la Tierra a la de Marte.", " millones de km"),
      arith("Venus da una vuelta al Sol en 225 días. ¿Cuántas vueltas completas da en 700 días?", "700//225", "Se divide el tiempo por el período y se toma la parte entera.", " vueltas"),
      ("Usa la tabla: ¿qué planetas tienen un año más corto que el de la Tierra?", "Mercurio y Venus", "Sus períodos, 88 y 225 días, son menores que 365 días."),
  ],
  rea=[
      ("Venus es, en promedio, más caliente que Mercurio aunque está más lejos del Sol. ¿Cómo es posible? A) Su atmósfera densa de dióxido de carbono atrapa el calor B) Gira más rápido que Mercurio", "A", "El efecto invernadero eleva su temperatura."),
      ("Hipótesis: «Los planetas más cercanos al Sol son los más pequeños». Con la tabla, ¿se sostiene en general?", "Sí", "Los cuatro más cercanos son rocosos y pequeños, y los cuatro más lejanos son gigantes."),
  ],
  cha=[
      arith("La luz viaja a 300.000 km/s. Marte está a 228 millones de km del Sol (228.000.000 km). ¿Cuántos segundos tarda la luz del Sol en llegar a Marte?", "228000000/300000", "El tiempo es la distancia dividida por la rapidez.", " s"),
      ("Un planeta de ejemplo tarda 8 años terrestres en dar una vuelta al Sol. ¿Está más cerca o más lejos del Sol que la Tierra?", "Más lejos", "Su período orbital es mayor que el de la Tierra."),
  ],
  context=[arith("Una sonda viaja a 50.000 km/h. Con las distancias medias al Sol, cuando la Tierra y Marte están alineados, la distancia entre ellos es de 78 millones de km (78.000.000 km). ¿Cuántas horas tardaría la sonda?", "78000000/50000", "El tiempo es la distancia dividida por la rapidez.", " h")],
  selfcheck=[("¿Qué planetas son rocosos?", "Mercurio, Venus, Tierra y Marte", "Son pequeños, de superficie sólida y están cerca del Sol."), ("¿Qué patrón hay entre la distancia al Sol y el período orbital?", "A mayor distancia, mayor período", "La órbita es más larga y el planeta se mueve más lento."), ("¿Por qué Venus es tan caliente?", "Por su atmósfera densa que atrapa el calor", "Es un efecto invernadero.")],
  open_task=task("Con la tabla de datos de la explicación, haz lo siguiente: (1) ordena los ocho planetas por distancia al Sol; (2) clasifícalos en rocosos o gigantes; (3) calcula cuántas veces cabe el diámetro de la Tierra en el de Saturno (116.000 km), con parte entera; (4) escribe un patrón entre distancia y período orbital con dos ejemplos; (5) propone una pregunta investigable sobre atmósferas.", "(1) Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno. (2) Los cuatro primeros rocosos, los cuatro últimos gigantes. (3) 116.000 ÷ 12.700 da 9 (parte entera). (4) Más lejos, mayor período: Mercurio, 58 millones de km y 88 días; Neptuno, 4.500 millones de km y 165 años. (5) «¿Cómo cambia la temperatura de la superficie con la densidad de la atmósfera en Venus, la Tierra y Marte?»", ["orden correcto", "clasificación correcta", "9 veces", "patrón con dos ejemplos", "pregunta con algo medible"], ["lista, tabla y pregunta"], ["ordenar por tamaño en vez de distancia", "olvidar la parte entera"], "Pregunta qué dato necesitarías para comparar temperaturas de superficie."),
  reinforce="Escribe dos diferencias entre un planeta rocoso y uno gigante.",
  extend="Explica por qué la Tierra es el único planeta de la tabla con agua líquida en su superficie.")

L(OA, 6,
  materials="Este cuaderno, lápiz, regla y cinta métrica o huincha. Los datos son aproximados y están escritos en los ejercicios; para observar el cielo no necesitas instrumentos.",
  use="Aprenderé a evaluar qué puede y qué no puede mostrar un modelo del sistema solar, y a observar el cielo con seguridad. Sirve para decidir cuánto confiar en un modelo.",
  prior=["Sé que un modelo simplifica la realidad.", "Sé calcular escalas con multiplicaciones y divisiones."],
  explain=[
      "Un modelo es útil, pero siempre tiene límites. Un modelo a escala reduce todas las medidas con el mismo factor. En el sistema solar es imposible mostrar tamaños y distancias a la misma escala en una sala. Por ejemplo, si la Tierra se representa con una bolita de 1 cm, el Sol sería una esfera de unos 110 cm y estaría a unos 118 m de ella. Por eso muchos modelos muestran solo las distancias o solo los tamaños, y se debe declarar qué magnitud no está a escala.",
      "Un modelo se evalúa con evidencia: debe predecir observaciones. El modelo de linterna y pelota para las fases lunares es bueno porque predice qué fase se verá según la posición de la Luna. Un modelo también tiene simplificaciones: las órbitas son elípticas casi circulares, y la Luna orbita con una pequeña inclinación. Un buen modelo declara lo que simplifica.",
      "La observación del cielo tiene reglas de seguridad y cuidado. Nunca se mira el Sol directamente. La contaminación lumínica, que es el exceso de luz artificial en la noche, dificulta ver las estrellas y afecta a muchos animales; se reduce con luminarias que apuntan hacia abajo. El norte de Chile tiene cielos oscuros muy valiosos para la observación astronómica, y cuidarlos es una responsabilidad compartida.",
  ],
  vocab=[("escala", "razón fija entre una medida del modelo y la medida real"), ("simplificación", "aspecto de la realidad que un modelo deja de lado"), ("predicción", "resultado que un modelo anticipa y puede compararse con la observación"), ("contaminación lumínica", "exceso de luz artificial que dificulta ver el cielo nocturno"), ("limitación", "aspecto que un modelo no puede representar"), ("evidencia", "observación o medición que apoya o contradice un modelo")],
  worked=[
      ("Aplicar una escala", "En un modelo, 1 cm representa 10 millones de km. La Tierra está a 150 millones de km del Sol. ¿A qué distancia del Sol debe ir la Tierra en el modelo?", ["Divido la distancia real por lo que representa cada centímetro.", "Calculo 150 ÷ 10."], "15 cm"),
      ("Evaluar con evidencia", "Un modelo de linterna y pelota predice que cuando la Luna está detrás de la Tierra respecto del Sol se verá toda su cara iluminada. ¿Qué evidencia lo apoya?", ["Esa posición corresponde a luna llena.", "En el cielo se observa luna llena de noche, con la Tierra entre el Sol y la Luna."], "La observación de la luna llena"),
  ],
  mistakes=[
      ("Pensar que un modelo debe ser idéntico a la realidad para ser útil.", "Un modelo simplifica y se evalúa por lo que logra explicar o predecir.", "Declara qué simplifica y qué puede predecir."),
      ("Creer que los tamaños y las distancias de un dibujo del sistema solar están a escala.", "Casi siempre se dibujan los planetas mucho más grandes y más cerca.", "Busca la leyenda de escala."),
  ],
  rec=[
      ("Verdadero o falso: en una sala se pueden mostrar tamaños y distancias del sistema solar a la misma escala.", "Falso", "Las distancias son enormes frente a los tamaños."),
      ("Un modelo se evalúa comparando sus predicciones con ______ (observaciones o gustos).", "Observaciones", "La evidencia decide si el modelo sirve."),
      ("¿Se puede mirar el Sol directamente durante un eclipse parcial?", "No", "Puede dañar la retina de forma permanente."),
  ],
  und=[
      ("En un modelo con 1 cm por cada 10 millones de km, el diámetro de la Tierra sería de unos 0,001 cm. ¿Qué limitación tiene ese modelo? A) No permite mostrar tamaños y distancias a la vez B) Muestra las distancias demasiado cortas", "A", "Los planetas serían demasiado pequeños para dibujarlos."),
      ("¿Qué es la contaminación lumínica?", "El exceso de luz artificial que dificulta ver el cielo nocturno", "Afecta a la observación astronómica y a la fauna."),
      ("¿Cuál es la forma segura de observar un eclipse solar parcial? A) Proyección con un agujero en una cartulina B) Mirar el Sol por un instante", "A", "Evita la luz directa."),
  ],
  app=[
      arith("En un modelo, 1 cm representa 10 millones de km. Neptuno está a 4.500 millones de km del Sol. ¿A cuántos centímetros del Sol va en el modelo?", "4500/10", "Se divide la distancia real por 10 para obtener los centímetros.", " cm"),
      arith("En el mismo modelo, la Tierra va a 15 cm del Sol y Neptuno a 450 cm. ¿Cuántas veces más lejos está Neptuno que la Tierra?", "450/15", "Se divide la distancia del modelo de Neptuno por la de la Tierra.", " veces"),
      ("En un modelo con 1 cm por cada 10 millones de km, un estudiante usa una pelota de 15 cm de diámetro como Sol. ¿Qué problema tiene? A) El Sol real mide solo unos 0,14 cm a esa escala B) La pelota queda demasiado lejos", "A", "El tamaño no está a escala: los tamaños quedarían diminutos."),
  ],
  rea=[
      ("Gabriela dice que su modelo de linterna y pelota no sirve porque la linterna es más pequeña que el Sol. ¿Qué respuesta es correcta? A) El modelo sirve para lo que representa, como las sombras y las fases, y se declaran sus limitaciones B) Tiene razón: un modelo debe ser idéntico a la realidad", "A", "Un modelo es útil dentro de sus límites."),
      ("¿Qué evidencia muestra que un modelo de fases lunares es bueno? A) Que predice correctamente la fase de la Luna en los próximos días B) Que se ve bonito", "A", "Un modelo se evalúa por sus predicciones."),
  ],
  cha=[
      arith("En el modelo de 1 cm por cada 10 millones de km, Saturno está a 1.430 millones de km del Sol. ¿Cuántos centímetros debe medir la cuerda que lo ubique respecto del Sol?", "1430/10", "Se divide la distancia real por 10.", " cm"),
      ("Un pueblo del norte de Chile quiere reducir la contaminación lumínica. ¿Qué medida sirve? A) Usar luminarias que apunten hacia abajo B) Poner luces que apunten hacia arriba", "A", "La luz dirigida al suelo evita que ilumine el cielo."),
  ],
  context=[ex("Es seguro mirar la Luna llena con binoculares, pero nunca el Sol. ¿Por qué? A) La luz de la Luna es débil, un reflejo del Sol, mientras que la del Sol es intensa y daña la retina B) La Luna está más cerca que el Sol", "A", "La intensidad de la luz solar directa es muy alta.")],
  selfcheck=[("¿Por qué no se puede hacer un modelo a escala completa del sistema solar en una sala?", "Porque las distancias son mucho mayores que los tamaños", "No caben tamaños y distancias a la misma escala."), ("¿Cómo se evalúa un modelo científico?", "Comparando sus predicciones con observaciones", "La evidencia lo apoya o lo contradice."), ("Da una medida contra la contaminación lumínica.", "Usar luminarias que apunten hacia abajo", "Reduce la luz que sube al cielo.")],
  open_task=task("Con la escala de 1 cm por cada 10 millones de km, marca con cinta o dibuja en tu cuaderno, por tramos si es necesario, una línea con el Sol en un extremo. Ubica la Tierra (150 millones de km), Júpiter (780 millones de km), Saturno (1.430 millones de km) y Neptuno (4.500 millones de km). Calcula la posición de cada uno. Escribe dos limitaciones de tu modelo y una medida de seguridad para observar el cielo.", "Tierra, 15 cm; Júpiter, 78 cm; Saturno, 143 cm; Neptuno, 450 cm (4,5 m). Limitaciones: los tamaños de los planetas no están a escala y las órbitas se representan como una línea, no como elipses. Seguridad: nunca mirar el Sol directamente.", ["cuatro posiciones calculadas con la escala", "dos limitaciones", "una medida de seguridad"], ["línea con marcas y cálculos"], ["usar una escala distinta para cada planeta", "olvidar declarar que los tamaños no están a escala"], "Pregunta cómo representarías los tamaños de los planetas con otra escala."),
  reinforce="Escribe dos límites de un modelo a escala del sistema solar.",
  extend="Explica por qué cuidar el cielo oscuro del norte de Chile importa para la ciencia.")
