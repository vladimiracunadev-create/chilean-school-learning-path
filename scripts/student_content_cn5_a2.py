"""Cuaderno del estudiante, 5.º básico Ciencias Naturales: OA 03 (respiración e intercambio gaseoso) y OA 04 (sistema circulatorio)."""
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




OA3, OA4 = "CN05 OA 03", "CN05 OA 04"

# ---------------------------------------------------------------- OA 03
L(OA3, 1,
  materials="Este cuaderno, lápiz y reloj o cronómetro. Tu propia mano para sentir el movimiento del pecho.",
  use="Aprenderé qué estructuras forman el sistema respiratorio y a separar lo que observo de lo que supongo al respirar. Sirve para explicar cómo entra y sale el aire.",
  prior=["Sé que los órganos forman sistemas.", "Sé que una observación se puede contar o sentir."],
  explain=[
      "El sistema respiratorio permite que el aire entre y salga del cuerpo. El aire entra por la nariz, que lo filtra y lo entibia, y baja por la tráquea, un tubo con anillos. La tráquea se divide en dos bronquios, uno para cada pulmón. Dentro de los pulmones los bronquios se ramifican hasta terminar en alvéolos, unos sacos diminutos.",
      "Respirar tiene dos movimientos: la inspiración, cuando el aire entra a los pulmones, y la espiración, cuando el aire sale. El aire trae oxígeno, un gas que las células necesitan para obtener energía de los alimentos. Al salir, el aire lleva dióxido de carbono, un gas de desecho que produce el cuerpo.",
      "Puedes observar tu respiración: si pones una mano en el pecho, sientes que sube al inspirar y baja al espirar. Contar inspiraciones en 30 segundos es una medición. Decir «respiro porque estoy nervioso» es una interpretación. Con la medición puedes comparar; con la interpretación solo supones.",
  ],
  vocab=[("inspiración", "entrada de aire a los pulmones"), ("espiración", "salida de aire de los pulmones"), ("oxígeno", "gas del aire que las células necesitan"), ("dióxido de carbono", "gas de desecho que el cuerpo elimina al espirar"), ("alvéolo", "saco diminuto del pulmón donde ocurre el intercambio de gases")],
  worked=[
      ("Ordenar el camino del aire", "Ordena: bronquios, nariz, alvéolos, tráquea.", ["El aire entra por la nariz.", "Baja por la tráquea.", "Pasa a los bronquios y termina en los alvéolos."], "Nariz, tráquea, bronquios, alvéolos"),
      ("Pasar una medición a un minuto", "En 30 segundos se cuentan 9 inspiraciones. ¿Cuántas habría en 1 minuto si el ritmo es igual?", ["Un minuto tiene 60 segundos.", "60 segundos son dos veces 30 segundos.", "Multiplico 9 por 2."], "18 inspiraciones por minuto"),
  ],
  mistakes=[
      ("Pensar que los pulmones se llenan de aire como un globo que se mueve solo.", "Los pulmones no se mueven solos; un músculo debajo de ellos ayuda.", "Observa que el pecho se mueve al respirar."),
      ("Anotar «respiro más porque estoy feliz» como observación.", "El motivo es una suposición; solo el conteo es evidencia.", "Anota el número de inspiraciones."),
  ],
  rec=[
      ("¿Por dónde entra el aire al sistema respiratorio?", "Por la nariz", "Es el primer órgano del camino del aire."),
      ("¿Entra o sale aire cuando haces una inspiración?", "Entra", "La inspiración es la entrada de aire."),
      ("Completa con «oxígeno» o «dióxido de carbono»: el aire que inspiras trae ______ para las células.", "Oxígeno", "Las células lo necesitan para obtener energía."),
  ],
  und=[
      ("¿Cuántos bronquios salen de la tráquea?", "2", "Uno va a cada pulmón."),
      ("¿Dónde termina el camino del aire dentro del pulmón?", "En los alvéolos", "Los bronquios se ramifican hasta ellos."),
      ("Marca la observación: A) En 30 segundos conté 10 inspiraciones. B) Respiro mucho porque soy deportista.", "A", "El conteo es una medición; B es una explicación sin dato."),
  ],
  app=[
      arith("En 30 segundos Pía contó 10 inspiraciones (dato de ejemplo). ¿Cuántas habría en 1 minuto con el mismo ritmo?", "10*2", "Un minuto es el doble de 30 segundos."),
      ("Un niño cuenta 8 inspiraciones en 30 segundos y otro cuenta 11 en 30 segundos. ¿Quién respira más veces por minuto?", "El segundo niño", "11 es mayor que 8 con el mismo tiempo."),
      ("Ordena el camino de salida del aire: A) bronquios, B) alvéolos, C) nariz, D) tráquea. Escribe el orden cuando el aire sale.", "B, A, D, C", "El aire sale por el mismo camino pero al revés."),
  ],
  rea=[
      ("Marcos cuenta 12 inspiraciones en 30 segundos y dice: «Respiro así porque estoy enojado». ¿Qué parte es evidencia?", "Las 12 inspiraciones en 30 segundos", "El enojo es una suposición sin medición."),
      ("Carla dice que el dióxido de carbono entra con la inspiración y el oxígeno sale con la espiración. ¿Qué error tiene? Corrige.", "Está al revés: entra oxígeno y sale dióxido de carbono", "Las células usan el oxígeno y producen dióxido de carbono."),
  ],
  cha=[
      arith("Un niño midió 9 inspiraciones en 30 segundos (dato de ejemplo) y su hermana 7. ¿Cuántas inspiraciones más hace el niño en 1 minuto?", "(9-7)*2", "La diferencia en 30 segundos se duplica en 1 minuto."),
      ("Explica por qué el conteo en un minuto de una sola persona no sirve para decir cuántas veces respiran todos los niños.", "Porque cada persona y momento puede ser distinto", "Un solo caso no representa a todos."),
  ],
  context=[("Dato de ejemplo. Una clase contó inspiraciones en 30 segundos: 9, 10, 8, 11 y 10. ¿Cuántas inspiraciones contaron en total las 5 personas?", "48", "9 + 10 + 8 + 11 + 10 = 48.")],
  selfcheck=[("Nombra tres estructuras del sistema respiratorio.", "Tres entre nariz, tráquea, bronquios, alvéolos y pulmones", "Forman el camino del aire."), ("¿Qué gas trae la inspiración?", "Oxígeno", "Las células lo necesitan."), ("¿Una suposición es evidencia? Responde Sí o No.", "No", "Solo lo medido o visto es evidencia.")],
  open_task=task("Siéntate tranquilo/a con una persona de tu casa. Pon una mano en tu pecho y cuenta tus inspiraciones durante 30 segundos. Escribe el número, calcula cuántas serían en 1 minuto y escribe una interpretación sobre por qué respiraste así. Si te sientes mal, detente.", "Conté 9 inspiraciones en 30 segundos; en 1 minuto serían 18. Interpretación: estaba tranquilo/a.", ["número contado en 30 segundos", "cálculo del minuto", "interpretación marcada como suposición"], ["registro escrito", "frase de interpretación"], ["contar sin cronómetro", "anotar el motivo como si fuera un dato"], "Pregunta qué cambiaría si contara después de correr y qué dato necesitaría para comprobarlo."),
  reinforce="Dibuja el camino del aire desde la nariz hasta los alvéolos con cinco rótulos.",
  extend="Explica por qué el oxígeno que respiras es necesario para las células.")

L(OA3, 2,
  materials="Este cuaderno, lápiz y reloj. Opcional: espacio libre para marchar en el lugar.",
  use="Aprenderé a hacer una pregunta y una predicción comprobables sobre cómo cambia la respiración. Sirve para relacionar el esfuerzo del cuerpo con el aire que necesita.",
  prior=["Sé contar inspiraciones en 30 segundos.", "Sé que una predicción lleva una razón."],
  explain=[
      "Cuando haces ejercicio, tus músculos trabajan más y sus células necesitan más oxígeno. También producen más dióxido de carbono. Por eso respiras más rápido y más profundo. Esto se puede comprobar contando tus inspiraciones antes y después de marchar en el lugar durante un minuto.",
      "Una pregunta comprobable puede ser: «¿Cuántas inspiraciones en 30 segundos hace una persona en reposo y cuántas después de marchar?». Una predicción es: «Después de marchar habrá más inspiraciones, porque los músculos necesitan más oxígeno». En la prueba cambia solo una cosa, el esfuerzo, y se mantiene igual el tiempo de conteo.",
      "Si el resultado no coincide con lo que predijiste, revisa tu idea. Una sola medición puede ser distinta si respiraste hondo o hablaste. Por eso conviene repetir la medición. Si te mareas o te falta el aire, detén el ejercicio y descansa.",
  ],
  vocab=[("reposo", "estar quieto y tranquilo, sin esfuerzo"), ("esfuerzo", "trabajo físico que hace el cuerpo"), ("pregunta comprobable", "pregunta que se responde midiendo o contando"), ("variable", "lo que cambia en una prueba"), ("repetir", "volver a medir para confirmar el resultado")],
  worked=[
      ("Elegir la pregunta comprobable", "¿Cuál se puede comprobar? A) ¿Es lindo respirar? B) ¿Cuántas inspiraciones en 30 segundos hay en reposo y después de marchar?", ["Pienso si puedo contar o medir.", "En B se cuentan inspiraciones.", "En A cada persona opina distinto."], "B"),
      ("Predicción con razón", "Predice si respirarás más o menos veces después de marchar un minuto.", ["Recuerdo que los músculos necesitan más oxígeno.", "Más oxígeno exige respirar más veces.", "Escribo la predicción con su razón."], "Más veces, porque los músculos necesitan más oxígeno"),
  ],
  mistakes=[
      ("Contar durante 30 segundos en reposo y durante 15 segundos después del ejercicio, y comparar los números.", "Los tiempos de conteo son distintos y no se pueden comparar.", "Cuenta siempre el mismo tiempo."),
      ("Hacer la predicción sin razón.", "No se aprende cuando no se sabe por qué se espera algo.", "Escribe «porque…» con una idea del cuerpo."),
  ],
  rec=[
      ("¿La predicción se hace antes o después de medir?", "Antes", "Es una idea previa que luego se comprueba."),
      ("Cuando haces ejercicio, ¿tus células necesitan más o menos oxígeno?", "Más", "Los músculos trabajan más y gastan más oxígeno."),
      ("Completa con «tiempo» o «color»: para comparar, el ______ de conteo debe ser igual.", "Tiempo", "Si el tiempo cambia, la comparación no es justa."),
  ],
  und=[
      ("¿Por qué respiras más rápido al correr?", "Porque tus músculos necesitan más oxígeno", "El esfuerzo aumenta el gasto de oxígeno."),
      ("En la prueba de marchar, ¿qué variable cambia: el esfuerzo o el tiempo de conteo?", "El esfuerzo", "Lo que se cambia a propósito es el esfuerzo."),
      ("¿Qué gas de desecho producen más las células de los músculos cuando haces ejercicio?", "El dióxido de carbono", "Las células lo producen al usar oxígeno para obtener energía."),
  ],
  app=[
      arith("Dato de ejemplo. En reposo, Luis hizo 9 inspiraciones en 30 segundos. Después de marchar hizo 15. ¿Cuántas inspiraciones más hizo?", "15-9", "Se resta el valor en reposo al valor tras el ejercicio."),
      ("Mina predijo que respiraría más veces después de marchar. Midió 8 en reposo y 14 después. ¿Se cumplió su predicción? Responde Sí o No.", "Sí", "14 es mayor que 8."),
      ("Una niña midió 3 veces en reposo, 30 segundos cada vez: 8, 10 y 9 inspiraciones. ¿Qué valor queda en el medio al ordenar los tres de menor a mayor?", "9", "Ordenados son 8, 9 y 10, y el del medio es 9."),
  ],
  rea=[
      ("Rafa cuenta 8 inspiraciones en 30 segundos en reposo y 10 inspiraciones en 15 segundos después de marchar. Dice: «Solo aumentó en 2». ¿Qué error tiene?", "Comparó 30 segundos con 15 segundos", "Con el mismo ritmo, 10 en 15 segundos serían unas 20 en 30 segundos, así que el aumento es mucho mayor."),
      ("Sara predice que, si baila durante un minuto, respirará más rápido. Su hermano dice que es solo una opinión. ¿Es una predicción comprobable? Responde Sí o No y explica.", "Sí; se puede contar antes y después", "Se compara un número con otro."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre respiración y esfuerzo, indicando qué contarás.", "¿Cuántas inspiraciones hago en 30 segundos en reposo y después de marchar un minuto?", "Nombra lo que se compara y lo que se cuenta."),
      ("Una persona midió una sola vez y dijo que su respiración cambió «muchísimo». ¿Qué le recomiendas para tener más confianza en el resultado?", "Repetir la medición varias veces", "Una medición puede salir distinta por azar."),
  ],
  context=[("Dato de ejemplo. En una clase de 6 personas, el conteo de inspiraciones en 30 segundos después de marchar fue 14 en todas. ¿Cuántas inspiraciones sumaron entre todas?", "84", "6 × 14 = 84.")],
  selfcheck=[("¿Por qué conviene mantener igual el tiempo de conteo?", "Para que la comparación sea justa", "Si cambia el tiempo, los números no se pueden comparar."), ("¿Qué lleva una buena predicción?", "Lo que pasará y la razón", "Así se puede comprobar."), ("¿Qué haces si te falta el aire en el ejercicio?", "Me detengo y descanso", "La seguridad va primero.")],
  open_task=task("Con una persona de tu casa, cuenta tus inspiraciones durante 30 segundos en reposo. Después marcha en el lugar durante 1 minuto con ritmo cómodo y cuenta otra vez 30 segundos. Antes escribe tu predicción con razón. Si te mareas o no te sientes bien, detente y avisa.", "Predicción: después de marchar respiraré más veces porque mis músculos necesitan más oxígeno. Resultado de ejemplo: reposo 9, después 15. La predicción se cumplió.", ["predicción con razón escrita antes", "dos conteos con el mismo tiempo", "conclusión con los números"], ["tabla con dos datos", "frase de conclusión"], ["cambiar el tiempo de conteo", "hacer ejercicio extremo"], "Pregunta cómo supo que el esfuerzo causó el cambio y qué podría explicar un resultado distinto."),
  reinforce="Escribe una predicción con razón sobre qué le pasa a tu respiración cuando subes una escalera.",
  extend="Explica por qué después de correr respiras más rápido aunque estés sentado/a.")

L(OA3, 3,
  materials="Este cuaderno y lápiz. Opcional: una botella plástica sin fondo (recortada por una persona adulta), un globo y una banda elástica.",
  use="Aprenderé a explicar la inspiración y la espiración con un modelo y a decir qué no muestra. Sirve para entender cómo se mueve el aire.",
  prior=["Sé las estructuras del sistema respiratorio.", "Sé que un modelo tiene límites."],
  explain=[
      "Para respirar, el pecho se mueve. Debajo de los pulmones hay un músculo llamado diafragma. En la inspiración el diafragma baja y las costillas se elevan: el espacio del pecho aumenta, los pulmones se llenan de aire y el aire entra. En la espiración el diafragma sube, el espacio se achica y el aire sale.",
      "Un modelo sencillo usa una botella sin fondo, un globo dentro que se une con un sorbete a la boca de la botella y otro globo estirado que cubre la base. La botella representa el pecho, el globo de dentro los pulmones y el globo de abajo el diafragma. Si tiras el globo de abajo, el globo de dentro se infla; si lo sueltas, se desinfla. El sorbete que une el globo con el aire representa la tráquea.",
      "Este modelo muestra el movimiento, pero tiene límites: los pulmones reales no son un globo, tienen millones de alvéolos y los bronquios se ramifican. Además el modelo no muestra el intercambio de oxígeno y dióxido de carbono. Siempre debes decir qué deja fuera.",
  ],
  vocab=[("diafragma", "músculo bajo los pulmones que baja y sube al respirar"), ("costillas", "huesos curvos que protegen el pecho"), ("modelo", "representación simple de algo real"), ("tráquea", "tubo que lleva el aire a los bronquios"), ("límite del modelo", "algo real que el modelo no muestra")],
  worked=[
      ("Leer el modelo", "En el modelo de la botella, tiras hacia abajo el globo de la base y el globo de dentro se infla. ¿Qué parte de la respiración representa?", ["Tirar hacia abajo equivale al diafragma que baja.", "Al bajar, el espacio aumenta.", "El globo de dentro se llena de aire."], "La inspiración"),
      ("Encontrar un límite", "El globo del modelo no tiene alvéolos. ¿Es un límite?", ["Los pulmones reales tienen alvéolos.", "El globo es liso y sin ramas.", "Eso real no está en el modelo."], "Sí, es un límite"),
  ],
  mistakes=[
      ("Pensar que los pulmones tienen músculos propios para inflarse.", "Los pulmones se llenan porque el diafragma y las costillas cambian el espacio del pecho.", "Observa el movimiento de la base del modelo."),
      ("Creer que el modelo muestra el intercambio de gases.", "El modelo solo muestra el movimiento del aire.", "Escribe ese límite."),
  ],
  rec=[
      ("¿Qué músculo está debajo de los pulmones y ayuda a respirar?", "El diafragma", "Baja y sube al respirar."),
      ("En el modelo, ¿qué representa el globo de dentro?", "Los pulmones", "Se llena y vacía de aire."),
      ("Completa con «baja» o «sube»: en la inspiración el diafragma ______.", "Baja", "Al bajar aumenta el espacio del pecho."),
  ],
  und=[
      ("¿Qué pasa con el diafragma en la espiración?", "Sube", "Al subir se achica el espacio y el aire sale."),
      ("En el modelo, ¿qué representa la botella?", "El pecho", "Es el espacio que contiene los pulmones."),
      ("¿Qué no muestra el modelo? A) El movimiento del aire. B) El intercambio de gases.", "B", "El modelo mueve aire, pero no oxígeno ni dióxido de carbono."),
  ],
  app=[
      ("Si sueltas el globo de la base, ¿qué pasa con el globo de dentro: se infla o se desinfla?", "Se desinfla", "Eso representa la espiración."),
      arith("Una niña dibuja un esquema con 5 rótulos. Ya escribió 3. ¿Cuántos rótulos le faltan?", "5-3", "Se resta lo escrito al total."),
      ("Un modelo tiene un sorbete entre el aire y el globo. ¿Qué estructura representa: la tráquea o los alvéolos?", "La tráquea", "Conduce el aire hasta los pulmones."),
  ],
  rea=[
      ("Teo dice que el modelo prueba que los pulmones son como globos. ¿Tiene razón? Responde Sí o No y explica.", "No; el modelo no tiene alvéolos ni bronquios ramificados", "Un modelo simplifica y deja cosas fuera."),
      ("En el modelo no se ve el dióxido de carbono. ¿Qué puedes decir sobre la espiración usando solo el modelo?", "Que el aire sale cuando el espacio se achica", "El modelo no muestra los gases, solo el movimiento."),
  ],
  cha=[
      ("Escribe dos límites del modelo de la botella con globos.", "No tiene alvéolos y no muestra el intercambio de gases", "El globo es liso y solo mueve aire."),
      ("Predice con el modelo: si tiras el globo de la base más fuerte, ¿el globo de dentro se inflará más o menos? Explica.", "Más, porque el espacio aumenta más", "Más espacio permite que entre más aire."),
  ],
  context=[("Dato de ejemplo. Una clase armó 7 modelos y en cada modelo contó 3 partes rotuladas. ¿Cuántas partes rotularon en total?", "21", "7 × 3 = 21.")],
  selfcheck=[("¿Qué hace el diafragma en la inspiración?", "Baja y aumenta el espacio del pecho", "Así el aire entra a los pulmones."), ("¿Qué muestra el modelo de la botella?", "El movimiento del aire al inspirar y espirar", "Representa el diafragma, el pecho y los pulmones."), ("¿Qué no muestra ese modelo?", "El intercambio de gases", "Solo mueve aire.")],
  open_task=task("Dibuja el modelo de la botella con globos: botella, globo de dentro, globo de la base y sorbete. Escribe qué representa cada parte. Después escribe una predicción sobre qué pasa si tiras de la base, y dos límites del modelo.", "Botella: pecho. Globo de dentro: pulmones. Globo de base: diafragma. Sorbete: tráquea. Predicción: si tiro de la base el globo se infla. Límites: no tiene alvéolos y no muestra el intercambio de gases.", ["cuatro partes con lo que representan", "predicción", "dos límites"], ["dibujo rotulado", "frases"], ["usar tijeras sin ayuda de una persona adulta", "no escribir límites"], "Pregunta qué parte del cuerpo representa cada objeto y qué mejoraría de su modelo."),
  reinforce="Explica con tus palabras qué pasa con el diafragma cuando inspiras.",
  extend="Piensa en otro objeto de tu casa que sirva de modelo de los pulmones y escribe su límite.")

L(OA3, 4,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar la inspiración con la espiración y a explicar el intercambio de gases en los alvéolos. Sirve para entender qué hace el aire en el cuerpo.",
  prior=["Sé las estructuras del sistema respiratorio.", "Sé usar un criterio común para comparar."],
  explain=[
      "En los alvéolos ocurre el intercambio gaseoso. Los alvéolos están rodeados de vasos muy finos llamados capilares. El oxígeno del aire pasa a la sangre y el dióxido de carbono pasa de la sangre al aire del alvéolo. Después, la espiración saca ese dióxido de carbono del cuerpo.",
      "Al comparar el aire que entra con el que sale, usamos un criterio: la cantidad de oxígeno y de dióxido de carbono. El aire que entra tiene más oxígeno y casi nada de dióxido de carbono. El aire que sale tiene menos oxígeno y más dióxido de carbono. Aproximadamente 21 de cada 100 partes del aire que entra son oxígeno, y en el aire que sale son unas 16 de cada 100.",
      "También puedes comparar la inspiración y la espiración con el mismo criterio: qué hace el diafragma, qué pasa con el espacio del pecho y hacia dónde va el aire. Una tabla ordena la comparación. Al final, escribe una conclusión y una limitación: los números del aire son aproximados.",
  ],
  vocab=[("intercambio gaseoso", "paso de oxígeno a la sangre y de dióxido de carbono al aire"), ("capilar", "vaso sanguíneo muy fino"), ("alvéolo", "saco diminuto del pulmón rodeado de capilares"), ("criterio", "característica que se mira igual en todos los casos"), ("aproximado", "cercano al valor real, pero no exacto")],
  worked=[
      ("Comparar con un criterio", "Criterio: ¿qué hace el diafragma? Compara inspiración y espiración.", ["En la inspiración el diafragma baja.", "En la espiración el diafragma sube.", "Pongo ambos en una tabla."], "Inspiración: baja. Espiración: sube"),
      ("Cuánto oxígeno se usa", "Aire que entra: 21 de cada 100 partes son oxígeno. Aire que sale: 16 de cada 100. ¿Cuántas partes de cada 100 se quedaron en el cuerpo?", ["Resto 21 − 16.", "Calculo la diferencia.", "Las partes que faltan las usó el cuerpo."], "5 de cada 100 partes"),
  ],
  mistakes=[
      ("Decir que el aire que sale no tiene nada de oxígeno.", "Sale con menos oxígeno, pero no sin oxígeno.", "Compara las cantidades."),
      ("Confundir el lugar del intercambio con la tráquea.", "Ocurre en los alvéolos, no en los tubos.", "Recuerda que los alvéolos tienen capilares."),
  ],
  rec=[
      ("¿Dónde ocurre el intercambio de gases?", "En los alvéolos", "Allí hay capilares muy finos."),
      ("¿El oxígeno pasa del aire a la sangre o de la sangre al aire?", "Del aire a la sangre", "Las células lo necesitan."),
      ("Completa con «oxígeno» o «dióxido de carbono»: el aire que sale trae más ______ que el que entra.", "Dióxido de carbono", "Las células lo produjeron y se elimina al espirar."),
  ],
  und=[
      ("¿Qué gas pasa de la sangre al aire del alvéolo?", "El dióxido de carbono", "Es el desecho que se elimina al espirar."),
      ("¿Qué vasos rodean a los alvéolos?", "Los capilares", "Son muy finos y permiten el intercambio."),
      ("¿Cuál criterio sirve para comparar el aire que entra y el que sale? A) La cantidad de oxígeno. B) El color del aire.", "A", "El oxígeno se puede comparar en ambos casos."),
  ],
  app=[
      arith("El aire que entra tiene unas 21 partes de oxígeno por cada 100 y el que sale unas 16. ¿Cuántas partes menos hay al salir?", "21-16", "Se resta el valor menor al mayor."),
      ("En la espiración, ¿el espacio del pecho aumenta o disminuye?", "Disminuye", "El diafragma sube y el aire sale."),
      arith("Dato de ejemplo. Dos personas contaron 9 y 12 espiraciones en 30 segundos. ¿Cuántas espiraciones contaron entre las dos?", "9+12", "Se suman las dos mediciones."),
  ],
  rea=[
      ("Joaquín dice que el aire que sale tiene más oxígeno que el que entra. ¿Es correcto? Responde Sí o No y explica.", "No; sale con menos oxígeno porque el cuerpo lo usó", "El oxígeno pasa a la sangre."),
      ("Daniela compara el aire que entra y el que sale midiendo una vez en un día. ¿Qué limitación tiene su comparación?", "Una sola medición puede no representar otros momentos", "Los valores pueden variar con la actividad."),
  ],
  cha=[
      ("Explica con tus palabras qué pasa en un alvéolo desde que llega aire hasta que sale.", "El oxígeno pasa a la sangre y el dióxido de carbono pasa al aire, que luego sale", "Ocurre el intercambio gaseoso entre alvéolo y capilares."),
      ("Un compañero dice: «La respiración y el intercambio gaseoso son lo mismo». Corrige con una frase.", "La respiración incluye inspirar y espirar; el intercambio es el paso de gases en los alvéolos", "El intercambio es una parte del proceso."),
  ],
  context=[("Dato de ejemplo. Un grupo hizo una tabla con 4 criterios y comparó la inspiración y la espiración en cada uno (2 casos por criterio). ¿Cuántas celdas llenaron?", "8", "4 × 2 = 8.")],
  selfcheck=[("¿Qué es el intercambio gaseoso?", "El paso de oxígeno a la sangre y de dióxido de carbono al aire en los alvéolos", "Ocurre en los capilares de los alvéolos."), ("¿Qué hace el diafragma en la espiración?", "Sube", "Reduce el espacio del pecho."), ("¿Por qué los números del aire son aproximados?", "Porque cambian según la persona y el momento", "Son valores cercanos.")],
  open_task=task("Haz una tabla con tres filas: diafragma, espacio del pecho y movimiento del aire. En dos columnas escribe qué pasa en la inspiración y en la espiración. Debajo escribe una conclusión sobre el intercambio de gases en los alvéolos y una limitación.", "Diafragma: baja / sube. Espacio: aumenta / disminuye. Aire: entra / sale. Conclusión: en los alvéolos el oxígeno pasa a la sangre y el dióxido de carbono sale. Limitación: la tabla no muestra el intercambio.", ["tabla completa", "conclusión con evidencia", "una limitación"], ["tabla", "frases"], ["poner el diafragma subiendo en la inspiración", "confundir tráquea con alvéolo"], "Pregunta qué criterio usó y cuál fila es más fácil de recordar."),
  reinforce="Escribe tres diferencias entre la inspiración y la espiración.",
  extend="Explica por qué respiramos más rápido cuando hacemos ejercicio usando lo que aprendiste del intercambio gaseoso.")

# ---------------------------------------------------------------- OA 04
L(OA4, 1,
  materials="Este cuaderno, lápiz y reloj. Tus dedos índice y medio para sentir el pulso.",
  use="Aprenderé qué estructuras forman el sistema circulatorio y a medir el pulso. Sirve para entender cómo se mueve la sangre por el cuerpo.",
  prior=["Sé que los órganos forman sistemas.", "Sé separar lo que se mide de lo que se supone."],
  explain=[
      "El sistema circulatorio transporta sustancias por todo el cuerpo. Sus estructuras básicas son el corazón, los vasos sanguíneos y la sangre. El corazón es un músculo del tamaño aproximado de un puño que funciona como una bomba. Los vasos sanguíneos son tubos por donde corre la sangre. La sangre es el líquido que lleva el oxígeno, los nutrientes y el dióxido de carbono.",
      "Cada vez que el corazón se contrae, empuja sangre por los vasos. Ese golpecito se puede sentir en la muñeca o en el cuello con dos dedos: es el pulso. Para medirlo, cuentas los latidos durante 15 segundos y multiplicas por 4 para saber cuántos son en un minuto. No se usa el pulgar porque tiene su propio pulso.",
      "Un registro del pulso es una observación medida. Decir «mi corazón late fuerte porque estoy emocionado» es una interpretación. Cuando comparas pulsos, siempre debes contar el mismo tiempo.",
  ],
  vocab=[("corazón", "músculo que bombea la sangre"), ("vaso sanguíneo", "tubo por donde circula la sangre"), ("sangre", "líquido que transporta oxígeno, nutrientes y dióxido de carbono"), ("pulso", "golpecito que se siente en un vaso sanguíneo cercano a la piel con cada latido"), ("latido", "contracción del corazón")],
  worked=[
      ("Calcular el pulso por minuto", "En 15 segundos se cuentan 19 latidos. ¿Cuántos serían en 1 minuto?", ["Un minuto tiene cuatro veces 15 segundos.", "Multiplico 19 por 4.", "Obtengo el valor por minuto."], "76 latidos por minuto"),
      ("Observación o interpretación", "«Conté 20 latidos en 15 segundos» y «Mi corazón late fuerte porque estoy feliz». ¿Cuál es observación?", ["Veo qué frase se midió.", "El conteo es un número.", "Estar feliz es una suposición."], "La primera frase"),
  ],
  mistakes=[
      ("Tomar el pulso con el dedo pulgar.", "El pulgar tiene su propio pulso y confunde el conteo.", "Usa el índice y el medio."),
      ("Comparar un conteo de 15 segundos con otro de 30 segundos sin ajustar.", "Los tiempos no coinciden.", "Cuenta siempre 15 segundos y multiplica por 4."),
  ],
  rec=[
      ("¿Qué estructura bombea la sangre?", "El corazón", "Se contrae y empuja la sangre."),
      ("¿Por dónde corre la sangre: por vasos sanguíneos o por huesos?", "Por vasos sanguíneos", "Son los tubos del sistema circulatorio."),
      ("Completa con «pulso» o «sueño»: el golpecito que se siente en la muñeca se llama ______.", "Pulso", "Aparece con cada latido."),
  ],
  und=[
      ("¿Cuáles son las tres estructuras básicas del sistema circulatorio?", "Corazón, vasos sanguíneos y sangre", "Forman el sistema de transporte del cuerpo."),
      ("¿Por qué se multiplica por 4 el conteo de 15 segundos?", "Porque un minuto tiene cuatro veces 15 segundos", "Así se obtiene el valor por minuto."),
      ("Marca la observación: A) Conté 18 latidos en 15 segundos. B) Mi corazón está contento.", "A", "El conteo se mide; B es una idea."),
  ],
  app=[
      arith("En 15 segundos Ema contó 18 latidos (dato de ejemplo). ¿Cuántos latidos por minuto son?", "18*4", "Se multiplica por 4 para obtener un minuto."),
      arith("Dato de ejemplo. Leo contó 20 latidos en 15 segundos y Tomás 17. ¿Cuántos latidos por minuto más tiene Leo?", "(20-17)*4", "La diferencia en 15 segundos se multiplica por 4."),
      ("Ordena el camino de la medida: A) multiplicar por 4, B) contar 15 segundos, C) anotar. ¿Cuál es el mejor orden?", "B, A, C", "Primero se cuenta, luego se calcula y se anota."),
  ],
  rea=[
      ("Bea dice: «Mi pulso es 20 latidos por minuto porque conté 20 latidos en 15 segundos». ¿Qué error tiene?", "No multiplicó por 4: serían 80 por minuto", "20 es el conteo de 15 segundos, no el de un minuto."),
      ("Un niño siente su pulso en la muñeca y dice: «Mi corazón está en mi muñeca». ¿Qué corrección haces?", "El pulso se siente en un vaso sanguíneo de la muñeca, pero el corazón está en el pecho", "El golpecito llega por los vasos."),
  ],
  cha=[
      arith("Dato de ejemplo. Una niña contó 17 latidos en los primeros 15 segundos y 19 en los 15 segundos siguientes. ¿Cuántos latidos contó en total en 30 segundos?", "17+19", "Se suman los dos intervalos de 15 segundos."),
      ("Explica por qué un solo pulso medido en un momento no sirve para decir cómo late el corazón de todo el día.", "Porque el pulso cambia según la actividad", "Con otro esfuerzo el valor sería distinto."),
  ],
  context=[("Dato de ejemplo. Una clase midió el pulso en 15 segundos: 18, 20, 19 y 21. ¿Cuántos latidos suman entre las 4 personas?", "78", "18 + 20 + 19 + 21 = 78.")],
  selfcheck=[("¿Qué hace el corazón?", "Bombea la sangre por los vasos", "Funciona como una bomba."), ("¿Qué transporta la sangre?", "Oxígeno, nutrientes y dióxido de carbono", "Son las sustancias que estudiamos."), ("¿Por qué multiplicas por 4?", "Porque 15 segundos son la cuarta parte de un minuto", "Así se calcula el pulso por minuto.")],
  open_task=task("Siéntate tranquilo/a. Con dos dedos busca tu pulso en la muñeca. Cuenta los latidos durante 15 segundos, multiplica por 4 y anota el resultado en latidos por minuto. Escribe una interpretación sobre por qué crees que tu pulso fue así.", "Conté 19 latidos en 15 segundos; 19 × 4 = 76 latidos por minuto. Interpretación: estaba tranquilo/a.", ["conteo en 15 segundos", "cálculo por minuto", "interpretación marcada como suposición"], ["registro escrito", "frase"], ["usar el pulgar", "no multiplicar por 4"], "Pregunta qué pasaría con su pulso si corriera y cómo lo comprobaría."),
  reinforce="Dibuja un corazón, tres vasos y una flecha que muestre el sentido de la sangre.",
  extend="Explica por qué se puede sentir el pulso en el cuello y en la muñeca.")

L(OA4, 2,
  materials="Este cuaderno, lápiz y reloj. Opcional: espacio para marchar en el lugar.",
  use="Aprenderé a plantear una pregunta y una predicción sobre el corazón y el esfuerzo. Sirve para entender por qué el pulso cambia.",
  prior=["Sé medir el pulso en 15 segundos.", "Sé que una predicción lleva una razón."],
  explain=[
      "Cuando haces ejercicio, tus músculos necesitan más oxígeno y más nutrientes. La sangre los lleva, así que el corazón late más rápido para enviar más sangre. Por eso el pulso sube después de correr o saltar y baja de nuevo al descansar.",
      "Una pregunta comprobable podría ser: «¿Cuántos latidos hay en 15 segundos en reposo y después de marchar un minuto?». Una predicción posible: «El pulso aumentará, porque los músculos necesitan más oxígeno que la sangre transporta». Para comparar de forma justa, el tiempo de conteo debe ser el mismo.",
      "Si el resultado es distinto de tu predicción, revisa si respiraste hondo, hablaste o te moviste antes de contar. Un solo registro puede variar, así que conviene repetir. Si sientes mareo o dolor, detén el ejercicio.",
  ],
  vocab=[("reposo", "estar quieto y tranquilo"), ("esfuerzo", "trabajo físico del cuerpo"), ("transportar", "llevar de un lugar a otro"), ("predicción", "lo que creo que pasará y por qué"), ("repetir", "volver a medir para confirmar")],
  worked=[
      ("Predicción con razón", "Predice si el pulso subirá o bajará después de marchar un minuto.", ["Recuerdo que el ejercicio exige más oxígeno.", "La sangre lo lleva y el corazón late más rápido.", "Escribo la predicción con su razón."], "Subirá, porque los músculos necesitan más oxígeno que lleva la sangre"),
      ("Comparar con el mismo tiempo", "Reposo: 18 latidos en 15 segundos. Después de marchar: 27 latidos en 15 segundos. ¿Aumentó el pulso?", ["Ambos son de 15 segundos.", "Comparo 27 con 18.", "27 es mayor."], "Sí, aumentó en 9 latidos"),
  ],
  mistakes=[
      ("Contar después del ejercicio durante más tiempo y comparar.", "Los tiempos distintos no se pueden comparar directamente.", "Usa siempre el mismo tiempo."),
      ("Predecir sin razón: «cambiará algo».", "No se aprende de una predicción vaga.", "Di qué pasará y por qué."),
  ],
  rec=[
      ("Después de correr, ¿el pulso sube o baja?", "Sube", "El corazón envía más sangre a los músculos."),
      ("¿Qué lleva la sangre a los músculos: oxígeno o ruido?", "Oxígeno", "También lleva nutrientes."),
      ("Completa con «repetir» o «adivinar»: para confirmar un resultado conviene ______ la medición.", "Repetir", "Una sola medición puede variar."),
  ],
  und=[
      ("¿Por qué el corazón late más rápido en el ejercicio?", "Para enviar más sangre con oxígeno a los músculos", "Los músculos necesitan más oxígeno y nutrientes."),
      ("¿Qué variable cambias en la prueba de marchar?", "El esfuerzo", "Lo demás, como el tiempo de conteo, se mantiene."),
      ("¿Qué pregunta se puede comprobar? A) ¿Cuántos latidos hay en 15 segundos tras marchar? B) ¿Es bonito el corazón?", "A", "Los latidos se cuentan."),
  ],
  app=[
      arith("Dato de ejemplo. Reposo: 18 latidos en 15 segundos. Tras marchar: 27 latidos. ¿Cuántos latidos más hubo?", "27-18", "Se resta el valor en reposo al valor tras marchar."),
      arith("Con los datos anteriores, ¿cuántos latidos por minuto fueron después de marchar?", "27*4", "Se multiplica por 4 el conteo de 15 segundos."),
      ("Gabi predijo que su pulso aumentaría tras saltar. Midió 17 en reposo y 25 después, en 15 segundos. ¿Se cumplió su predicción? Responde Sí o No.", "Sí", "25 es mayor que 17."),
  ],
  rea=[
      ("Hugo midió 15 segundos en reposo y 30 segundos tras el ejercicio y dice que su pulso se duplicó. ¿Qué problema tiene?", "Usó tiempos distintos para comparar", "Los conteos deben ser del mismo tiempo."),
      ("Al medir, Paula habló durante la prueba y su pulso salió distinto a lo esperado. ¿Qué puede hacer para mejorar la prueba?", "Quedarse en silencio y repetir", "Hablar puede cambiar el resultado."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre el pulso y el esfuerzo, indicando qué contarás.", "¿Cuántos latidos hay en 15 segundos en reposo y después de marchar un minuto?", "Nombra lo que se cambia y lo que se cuenta."),
      ("Una niña midió 3 veces el pulso tras marchar y obtuvo 25, 26 y 24 latidos en 15 segundos. ¿Por qué repetir ayuda a confiar en el resultado?", "Porque los valores son parecidos y no dependen de un solo azar", "La repetición muestra si el resultado es estable."),
  ],
  context=[("Dato de ejemplo. Cuatro estudiantes tuvieron estos latidos en 15 segundos tras marchar: 25, 26, 24 y 27. ¿Cuántos latidos suman?", "102", "25 + 26 + 24 + 27 = 102.")],
  selfcheck=[("¿Por qué el pulso sube con el ejercicio?", "Porque los músculos necesitan más oxígeno", "El corazón envía más sangre."), ("¿Qué mantienes igual al comparar pulsos?", "El tiempo de conteo", "Así la comparación es justa."), ("¿Qué haces si te mareas con el ejercicio?", "Me detengo y descanso", "La seguridad va primero.")],
  open_task=task("Con una persona de tu casa, mide tu pulso en reposo durante 15 segundos. Marcha en el lugar durante 1 minuto con ritmo cómodo y mide de nuevo 15 segundos. Antes escribe tu predicción con razón. Si te mareas, detente.", "Predicción: mi pulso subirá porque los músculos necesitan más oxígeno. Resultado de ejemplo: reposo 18, después 26. Se cumplió.", ["predicción con razón", "dos conteos de 15 segundos", "conclusión con los números"], ["tabla con dos datos", "frase de conclusión"], ["cambiar el tiempo de conteo", "hacer ejercicio extremo"], "Pregunta cómo supo que el aumento se debió al ejercicio y no a otra cosa."),
  reinforce="Escribe una predicción con razón sobre cómo cambiará tu pulso al subir una escalera.",
  extend="Explica por qué el pulso vuelve a bajar cuando descansas.")

L(OA4, 3,
  materials="Este cuaderno, lápiz y lápices rojo y azul. Opcional: una bolsa o botella de plástico flexible, una manguera pequeña y agua (en el patio).",
  use="Aprenderé a explicar con un modelo cómo el corazón y los vasos mueven la sangre. Sirve para entender el transporte de sustancias.",
  prior=["Sé las estructuras del sistema circulatorio.", "Sé que un modelo tiene límites."],
  explain=[
      "El sistema circulatorio puede modelarse con una bomba, tubos y un líquido. El corazón es la bomba, los vasos sanguíneos son los tubos y la sangre es el líquido. Cuando el corazón se contrae, empuja la sangre. Las arterias llevan la sangre desde el corazón hacia el cuerpo. Las venas la devuelven al corazón. Los capilares son vasos muy finos donde la sangre entrega y recibe sustancias.",
      "La sangre pasa por los pulmones, donde recoge oxígeno y deja dióxido de carbono. Luego vuelve al corazón y este la bombea al resto del cuerpo. En los capilares entrega oxígeno y nutrientes y recibe dióxido de carbono. Después regresa por las venas.",
      "El modelo de bomba y mangueras ayuda a ver el recorrido, pero tiene límites: la sangre real tiene células, los vasos se ramifican en millones y el corazón tiene cuatro cavidades. Un buen modelo dice qué muestra y qué no muestra.",
  ],
  vocab=[("arteria", "vaso que lleva sangre desde el corazón"), ("vena", "vaso que lleva sangre de vuelta al corazón"), ("capilar", "vaso muy fino donde la sangre entrega y recibe sustancias"), ("bomba", "objeto que empuja un líquido"), ("circulación", "recorrido de la sangre por el cuerpo")],
  worked=[
      ("Leer el modelo", "En el modelo, una botella flexible empuja agua por una manguera. ¿Qué representan la botella y la manguera?", ["La botella empuja el líquido.", "La manguera lo conduce.", "Relaciono con el cuerpo."], "La botella es el corazón y la manguera, un vaso sanguíneo"),
      ("Arterias y venas", "¿Cuál vaso lleva sangre desde el corazón hacia el cuerpo: arteria o vena?", ["Recuerdo la definición de arteria.", "Las arterias salen del corazón.", "Las venas regresan a él."], "La arteria"),
  ],
  mistakes=[
      ("Decir que las venas salen del corazón.", "Las venas llegan al corazón; las arterias salen.", "Recuerda: arteria sale y vena vuelve."),
      ("Pensar que el modelo muestra todos los vasos reales.", "En el cuerpo hay millones de capilares.", "Escribe ese límite."),
  ],
  rec=[
      ("En el modelo, ¿qué representa la bomba?", "El corazón", "Empuja la sangre."),
      ("¿Qué vasos llevan la sangre de vuelta al corazón?", "Las venas", "Llegan al corazón."),
      ("Completa con «arteria» o «vena»: el vaso que sale del corazón es una ______.", "Arteria", "Las arterias salen del corazón."),
  ],
  und=[
      ("¿Dónde la sangre entrega oxígeno y nutrientes?", "En los capilares", "Son los vasos más finos."),
      ("¿Qué recoge la sangre en los pulmones?", "Oxígeno", "Y deja dióxido de carbono."),
      ("¿Qué limita al modelo de bomba y mangueras? A) No muestra las células de la sangre. B) Muestra el corazón.", "A", "El modelo usa agua simple y no sangre real."),
  ],
  app=[
      ("En un esquema, una flecha sale del corazón. ¿Esa flecha es una arteria o una vena?", "Una arteria", "Sale del corazón."),
      arith("Un esquema tiene 6 flechas hacia el cuerpo y 6 flechas de regreso al corazón. ¿Cuántas flechas tiene en total?", "6+6", "Se suman las flechas de ida y de regreso."),
      ("En el modelo, si dejas de apretar la botella, ¿qué pasa con el movimiento del agua? Responde «se detiene» o «sigue igual».", "Se detiene", "Sin bomba no hay empuje."),
  ],
  rea=[
      ("Mateo dice que el modelo prueba que la sangre es agua. ¿Tiene razón? Responde Sí o No y explica.", "No; el agua solo representa el líquido, la sangre tiene células", "Un modelo simplifica."),
      ("Ana dibuja sangre que va del corazón a los pulmones y vuelve al corazón. ¿Qué gas recoge en los pulmones?", "Oxígeno", "Allí se hace el intercambio de gases."),
  ],
  cha=[
      ("Escribe dos límites del modelo de bomba y mangueras.", "No tiene células en la sangre y no muestra millones de capilares", "El modelo simplifica los vasos y el líquido."),
      ("Predice con el modelo: si el corazón se detiene, ¿qué pasa con la entrega de oxígeno a los músculos? Explica.", "Se detiene, porque la sangre ya no se mueve", "Sin bomba no llega sangre con oxígeno."),
  ],
  context=[("Dato de ejemplo. Un modelo tiene 3 corazones de papel y cada corazón se une con 4 vasos dibujados. ¿Cuántos vasos hay en total?", "12", "3 × 4 = 12.")],
  selfcheck=[("¿Qué representa la bomba en el modelo?", "El corazón", "Empuja la sangre."), ("¿Qué diferencia hay entre arteria y vena?", "La arteria sale del corazón y la vena llega a él", "Es el sentido de la sangre."), ("¿Qué límite tiene el modelo?", "No muestra las células de la sangre ni todos los vasos", "El modelo simplifica la sangre y los vasos.")],
  open_task=task("Dibuja un esquema del sistema circulatorio con un corazón, una arteria roja, una vena azul y un capilar (los colores son una convención de los dibujos). Escribe en cada parte su nombre y una flecha del sentido de la sangre. Agrega dos límites de tu esquema.", "Corazón en el centro, arteria roja hacia el cuerpo, vena azul de regreso, capilar entre ambos. Límites: no muestra las células de la sangre y no dibuja todos los vasos.", ["cuatro partes rotuladas", "sentido de la sangre con flechas", "dos límites"], ["dibujo rotulado", "frases"], ["invertir arteria y vena", "no escribir límites"], "Pregunta por qué las arterias van hacia el cuerpo y qué parte del dibujo es más simple que la realidad."),
  reinforce="Explica con tus palabras el recorrido de la sangre de un capilar a una vena y al corazón.",
  extend="Piensa en otro objeto que sirva de modelo de un vaso sanguíneo y escribe su límite.")

L(OA4, 4,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar qué transporta la sangre, desde dónde y hacia dónde. Sirve para explicar la función de transporte del sistema circulatorio.",
  prior=["Sé las estructuras del sistema circulatorio.", "Sé las funciones de los sistemas digestivo y respiratorio."],
  explain=[
      "La función de transporte del sistema circulatorio se entiende comparando con un mismo criterio: qué sustancia lleva la sangre, desde dónde y hacia dónde. El oxígeno va de los pulmones a las células. Los nutrientes van del intestino delgado a las células. El dióxido de carbono hace el camino contrario: va de las células a los pulmones para salir al espirar.",
      "Así se conectan los sistemas: el digestivo entrega nutrientes a la sangre, el respiratorio le entrega oxígeno y retira dióxido de carbono, y el circulatorio lleva todo a donde se necesita. Ningún sistema trabaja solo. Esto también explica por qué comer, respirar y hacer ejercicio afectan al corazón.",
      "Para comparar usa una tabla con las columnas sustancia, origen y destino. Después escribe una conclusión y una limitación. La tabla no muestra que la sangre también lleva otras sustancias, como las defensas del cuerpo.",
  ],
  vocab=[("origen", "lugar desde donde parte una sustancia"), ("destino", "lugar adonde llega una sustancia"), ("nutriente", "sustancia de los alimentos que el cuerpo aprovecha"), ("transporte", "traslado de una sustancia de un lugar a otro"), ("criterio", "característica que se mira igual en todos los casos")],
  worked=[
      ("Completar origen y destino", "Oxígeno: origen pulmones; destino ______.", ["La sangre lo recoge en los pulmones.", "Lo entrega a las células.", "Completo el destino."], "Las células"),
      ("Comparar dos sustancias", "Criterio: ¿hacia dónde viaja? Compara oxígeno y dióxido de carbono.", ["El oxígeno va a las células.", "El dióxido de carbono sale de las células hacia los pulmones.", "Los destinos son distintos."], "El oxígeno viaja a las células y el dióxido de carbono a los pulmones"),
  ],
  mistakes=[
      ("Pensar que la sangre lleva alimentos enteros como pan.", "Lleva nutrientes ya digeridos.", "Une el transporte con el sistema digestivo."),
      ("Decir que el dióxido de carbono va de los pulmones a las células.", "Va de las células a los pulmones.", "Recuerda que es un desecho."),
  ],
  rec=[
      ("¿Qué sustancia lleva la sangre desde los pulmones a las células?", "El oxígeno", "Las células lo necesitan."),
      ("¿De dónde recoge la sangre los nutrientes: del intestino delgado o de los pulmones?", "Del intestino delgado", "Allí se absorben."),
      ("Completa con «nutrientes» o «ruido»: el sistema digestivo entrega ______ a la sangre.", "Nutrientes", "La absorción los pasa a la sangre."),
  ],
  und=[
      ("¿Hacia dónde viaja el dióxido de carbono en la sangre?", "Hacia los pulmones", "Para salir al espirar."),
      ("¿Qué sistema entrega oxígeno a la sangre?", "El respiratorio", "Lo hace en los alvéolos."),
      ("¿Qué criterio sirve para la tabla? A) Sustancia, origen y destino. B) Color del vaso.", "A", "Esos datos describen el transporte."),
  ],
  app=[
      ("Completa la tabla: nutrientes, origen intestino delgado, destino ______.", "Las células", "La sangre los lleva a todo el cuerpo."),
      ("En la tabla de esta clase, ¿qué sustancia tiene como origen el intestino delgado?", "Los nutrientes", "Se absorben allí y pasan a la sangre."),
      ("Un compañero escribe que el oxígeno va de las células a los pulmones. Corrige: ¿hacia dónde va realmente el oxígeno?", "De los pulmones a las células", "El oxígeno entra por los pulmones y llega a las células."),
  ],
  rea=[
      ("Lía dice: «Si el corazón se detiene, las células siguen recibiendo oxígeno». ¿Tiene razón? Responde Sí o No y explica.", "No; sin bombeo la sangre no lleva oxígeno", "El transporte depende del corazón."),
      ("Un niño dice que el sistema digestivo, el respiratorio y el circulatorio trabajan por separado. ¿Qué evidencia de esta clase lo contradice?", "La sangre lleva nutrientes del digestivo y oxígeno del respiratorio", "Los sistemas se conectan por la sangre."),
  ],
  cha=[
      ("Escribe una conclusión con la tabla: ¿qué sustancia parte de las células y llega a los pulmones?", "El dióxido de carbono", "Es el desecho que se elimina al espirar."),
      ("¿Qué limitación tiene una tabla de solo tres sustancias para explicar todo lo que transporta la sangre?", "No incluye otras sustancias que también transporta", "La sangre lleva más cosas, como las defensas."),
  ],
  context=[("Dato de ejemplo. Una tabla de un grupo tenía 3 sustancias y para cada una se escribieron 2 datos (origen y destino). ¿Cuántos datos escribieron?", "6", "3 × 2 = 6.")],
  selfcheck=[("Nombra tres cosas que transporta la sangre.", "Oxígeno, nutrientes y dióxido de carbono", "Son las que trabajamos en esta clase."), ("¿De dónde viene el oxígeno que lleva la sangre?", "De los pulmones", "Entra por la respiración."), ("¿Por qué ningún sistema trabaja solo?", "Porque la sangre conecta a los sistemas", "Transporta lo que cada sistema entrega o retira.")],
  open_task=task("Haz una tabla con tres filas (oxígeno, nutrientes, dióxido de carbono) y tres columnas (sustancia, origen, destino). Complétala con lo aprendido y escribe una conclusión y una limitación.", "Oxígeno: pulmones → células. Nutrientes: intestino delgado → células. Dióxido de carbono: células → pulmones. Conclusión: la sangre transporta en ambos sentidos. Limitación: la tabla no incluye otras sustancias.", ["tabla completa", "conclusión", "limitación"], ["tabla", "frases"], ["invertir origen y destino", "olvidar la limitación"], "Pregunta qué fila se confunde más y qué sistema participa en cada fila."),
  reinforce="Escribe una oración que una el sistema digestivo, el respiratorio y el circulatorio.",
  extend="Explica por qué una persona con ejercicio intenso necesita que la sangre transporte más oxígeno.")
