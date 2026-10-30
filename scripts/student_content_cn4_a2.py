"""Cuaderno del estudiante, 4.º básico Ciencias Naturales: OA 04 (actividad humana y protección de ecosistemas), OA 05 (sistema esquelético) y OA 06 (sistema musculoesquelético)."""
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


OA4, OA5, OA6 = "CN04 OA 04", "CN04 OA 05", "CN04 OA 06"

# ---------------------------------------------------------------- OA 04
L(OA4, 1,
  materials="Este cuaderno y lápiz. Opcional: una bolsa para recoger basura de una plaza, con guantes y ayuda de una persona adulta.",
  use="Aprenderé a describir cómo las personas cambian los ecosistemas, separando lo que se ve de lo que se supone. Sirve para proponer cuidados con evidencia.",
  prior=["Sé qué es un ecosistema.", "Sé que una observación se puede ver o contar."],
  explain=[
      "Las personas usamos los ecosistemas: sacamos agua, madera y peces, construimos casas y caminos, y producimos basura. Estas acciones se llaman actividad humana. Pueden cambiar los ecosistemas de forma pequeña o muy grande.",
      "Algunos efectos dañinos son: la basura que contamina el agua y el suelo, la tala excesiva de árboles, los incendios forestales y la pesca de más peces de los que pueden reponerse. Los seres vivos que dependen de ese lugar pueden quedarse sin alimento o sin refugio.",
      "Para estudiarlo, observo y anoto: «hay 12 botellas en la orilla de la laguna». Esa es una observación. Decir «la gente es mala» es una interpretación y no ayuda a resolver el problema. Primero la evidencia, después las propuestas.",
  ],
  vocab=[("actividad humana", "lo que hacen las personas y que puede cambiar el ambiente"), ("contaminación", "presencia de basura u otras sustancias que dañan el ambiente"), ("tala", "corte de árboles"), ("incendio forestal", "fuego que se propaga y quema bosques o pastizales"), ("sobrepesca", "pesca de más peces de los que la naturaleza puede reponer")],
  worked=[
      ("Efecto de una acción", "Un grupo deja basura en una playa. ¿Qué efecto puede tener en las aves?", ["Pienso qué pasa con la basura.", "Las aves pueden enredarse o confundirla con alimento.", "Su salud queda en riesgo."], "Las aves pueden enredarse o comer basura y enfermar"),
      ("Observación o interpretación", "«Hay 12 botellas en la orilla» y «A los visitantes no les importa la laguna». ¿Cuál es la evidencia?", ["Reviso qué se puede contar.", "Las botellas se cuentan.", "Lo que importa a los visitantes es una suposición."], "Hay 12 botellas en la orilla"),
  ],
  mistakes=[
      ("Pensar que toda actividad humana daña el ecosistema.", "También hay acciones que lo cuidan, como plantar árboles o limpiar una playa.", "Distingue acciones que dañan de las que protegen."),
      ("Culpar a una persona sin evidencia.", "Una acusación no es un dato.", "Anota lo que ves y propón soluciones."),
  ],
  rec=[
      ("Cortar muchos árboles sin reponerlos, ¿es una acción que daña o que protege?", "Daña", "El bosque pierde refugio y alimento."),
      ("Limpiar una playa, ¿es una acción que daña o que protege?", "Protege", "Retira la basura que daña al ecosistema."),
      ("Completa con «contaminación» o «adaptación»: dejar basura en un río causa ______.", "Contaminación", "La basura ensucia y daña el agua."),
  ],
  und=[
      ("¿Qué es una observación? A) 'Hay 5 bolsas en la laguna.' B) 'A nadie le importa la laguna.'", "A", "A se puede contar; B es una suposición."),
      ("¿Por qué la sobrepesca puede dañar el mar?", "Porque se sacan más peces de los que pueden reponerse", "Con pocos peces, los animales que los comen tienen menos alimento."),
      ("¿Qué le puede pasar a un bosque si hay un incendio forestal?", "Pierde árboles y refugios de los animales", "El fuego quema plantas y hogares de animales."),
  ],
  app=[
      arith("En una playa se contaron 14 botellas, 9 bolsas y 7 envases. ¿Cuántos residuos hay en total?", "14+9+7", "Se suman todos los residuos contados."),
      ("Datos de ejemplo. Antes de una limpieza había 40 bolsas en una orilla. Después de la limpieza quedaron 6. ¿Cuántas bolsas se retiraron?", "34", "40 − 6 = 34."),
      ("Ordena con letras para investigar un problema: A) Propongo una solución. B) Anoto lo que veo. C) Reviso las causas. ¿Cuál es el mejor orden?", "B, C, A", "Primero se observa, luego se buscan causas y al final se propone."),
  ],
  rea=[
      ("Ana ve un charco con basura y dice: «Seguro la dejaron los turistas». ¿Tiene evidencia? Responde Sí o No y explica.", "No; solo vio basura, no sabe quién la dejó", "Quien la dejó no se observó."),
      ("Un niño cuenta 3 peces en una orilla donde antes veía 10. Dice: «Fue por la pesca». ¿Qué le falta para estar seguro?", "Más datos sobre otras posibles causas", "Pudo haber otras causas, como la contaminación."),
  ],
  cha=[
      ("Escribe una acción humana que daña un ecosistema y una que lo protege, para un río.", "Daña: botar basura al río. Protege: limpiar la orilla", "Una acción afecta al río de forma distinta."),
      ("Datos de ejemplo. Un lago tenía 60 aves, ahora tiene 35. ¿Cuántas aves menos hay? ¿Prueba el dato que fueron las personas?", "25 menos; no, el dato por sí solo no prueba la causa", "La cifra muestra el cambio, no su causa."),
  ],
  context=[("En una limpieza de playa 5 niñas y niños recogen 8 bolsas cada uno. ¿Cuántas bolsas recogen en total?", "40", "5 × 8 = 40.")],
  selfcheck=[("¿Qué es actividad humana?", "Lo que hacen las personas y puede cambiar el ambiente", "Puede dañar o proteger."), ("Nombra dos efectos dañinos de las personas en un ecosistema.", "Dos entre contaminación, tala excesiva, incendios o sobrepesca", "Son los ejemplos de la clase."), ("¿Qué va primero: la evidencia o la propuesta?", "La evidencia", "Sin evidencia la propuesta no se apoya en nada.")],
  open_task=task("Observa con una persona de tu casa un lugar de tu barrio (una plaza, una acequia, una calle con árboles). Anota en una tabla tres observaciones de cómo las personas lo usan o lo cambian (por ejemplo, 'hay 4 latas', 'hay 2 árboles nuevos'). Después escribe una interpretación y una propuesta. No recojas objetos peligrosos ni toques animales.", "Plaza: 4 latas junto a la banca; 2 árboles plantados. Interpretación: algunas personas dejan basura. Propuesta: poner un basurero.", ["tres observaciones", "una interpretación marcada", "una propuesta"], ["tabla de observaciones"], ["culpar sin datos", "olvidar acciones positivas"], "Pregunta qué parte de lo anotado se puede comprobar con otra persona."),
  reinforce="Anota cuántos residuos ves en una calle durante 5 minutos, sin tocarlos.",
  extend="Investiga una acción que cuide un ecosistema de Chile y escríbela con una frase.")

L(OA4, 2,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a preguntar y predecir cómo cambia un ecosistema según lo que hacemos. Sirve para anticipar problemas y elegir medidas.",
  prior=["Sé que la actividad humana puede dañar o proteger.", "Sé hacer una predicción con razón."],
  explain=[
      "Una predicción sobre un ecosistema dice qué pasará si una acción continúa o cambia. Ejemplo: «Si se pescan demasiados peces cada año, quedarán menos peces, porque no alcanzan a reponerse». Siempre se da la razón.",
      "Una pregunta comprobable puede usar datos: «¿Cuántos residuos se juntan en una playa un fin de semana largo?». No sirve preguntar «¿es malo?» porque no se puede medir. Los datos pueden venir de conteos, registros o informes confiables.",
      "Una medida de protección es una acción para cuidar. Un parque nacional es un área que el Estado protege para conservar su naturaleza. Una veda es una prohibición temporal de pescar o recolectar una especie para que se recupere. Las medidas se eligen según el problema.",
  ],
  vocab=[("parque nacional", "área protegida por el Estado para conservar su naturaleza"), ("veda", "prohibición temporal de pescar o recolectar una especie"), ("medida de protección", "acción para cuidar un ecosistema"), ("reponerse", "volver a tener la cantidad que había"), ("registro", "anotación ordenada de datos")],
  worked=[
      ("Hacer una predicción", "Una laguna recibe basura todas las semanas. Predice qué pasará con los peces.", ["Pienso qué hace la basura al agua.", "Los peces pueden enfermar o irse.", "Escribo la predicción con razón."], "Habrá menos peces, porque el agua se ensucia"),
      ("Elegir una medida", "Se pescan demasiados peces de una especie. ¿Qué medida ayuda: una veda o más basureros?", ["Miro el problema: se pesca de más.", "La veda permite que la especie se recupere.", "Más basureros ayudan, pero a otro problema."], "Una veda"),
  ],
  mistakes=[
      ("Elegir una medida que no responde al problema.", "Una medida debe ayudar al problema que se observó.", "Primero nombra el problema y luego la medida."),
      ("Creer que una veda es para siempre.", "Una veda dura un tiempo, mientras la especie se recupera.", "Recuerda: veda = prohibición temporal."),
  ],
  rec=[
      ("¿Una veda es temporal o para siempre?", "Temporal", "Dura mientras la especie se recupera."),
      ("¿Un parque nacional protege o daña la naturaleza?", "Protege", "Es un área para conservarla."),
      ("Completa con «antes» o «después»: la predicción se hace ______ de ver el resultado.", "Antes", "Es una idea previa."),
  ],
  und=[
      ("¿Qué pregunta se puede comprobar? A) ¿Cuántas bolsas se juntan en una playa un domingo? B) ¿Es feo botar basura?", "A", "A se responde contando."),
      ("Hay una pesca excesiva de una especie del mar. ¿Qué medida es adecuada?", "Una veda", "Permite que la especie se reponga."),
      ("¿Qué es un parque nacional?", "Un área que el Estado protege para conservar su naturaleza", "Su objetivo es cuidar los ecosistemas."),
  ],
  app=[
      arith("Datos de ejemplo. Una playa tenía 120 residuos el sábado y 45 el domingo después de una limpieza. ¿Cuántos residuos se retiraron?", "120-45", "Se resta lo que quedó a lo que había."),
      ("Predice: si una zona de bosque se tala completamente, ¿qué pasa con los animales que viven en él? Escribe «menos refugios» o «más refugios».", "Menos refugios", "Sin árboles pierden su hogar."),
      ("Un río recibe aguas con restos de basura de una ciudad. ¿Qué medida ayuda más: limpiar la orilla o plantar flores en una plaza lejana?", "Limpiar la orilla", "Responde al problema del río."),
  ],
  rea=[
      ("Ema predice que una veda de dos años hará que haya más peces. ¿Está bien fundada? Responde Sí o No y explica.", "Sí; sin pesca, los peces se pueden reproducir y reponer", "Al no pescarlos, aumentan."),
      ("Datos de ejemplo. Un parque tiene 80 aves y está protegido; una zona vecina sin protección tiene 30 aves. Luis dice que el parque causa más aves. ¿Qué otro dato necesita?", "Saber si ambas zonas eran parecidas antes", "Podría haber otras diferencias entre los lugares."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre una medida de protección y qué dato necesitas.", "¿Aumentan los peces después de una veda? Necesito contar peces antes y después", "La pregunta se resuelve con conteos."),
      ("¿Puede una medida de protección funcionar sin que las personas la respeten? Responde Sí o No y explica.", "No; sin respeto la medida no se cumple", "Las medidas dependen de las personas."),
  ],
  context=[("Un parque nacional recibe 150 visitantes un sábado y 90 un domingo. Todos reciben información para no dejar basura. ¿Cuántos visitantes recibe el fin de semana?", "240", "150 + 90 = 240.")],
  selfcheck=[("¿Qué es una veda?", "Una prohibición temporal de pescar o recolectar", "Permite que la especie se recupere."), ("¿Qué medida temporal ayuda si hay sobrepesca?", "Una veda", "Permite que la especie se recupere."), ("¿Qué debe tener una predicción?", "Qué pasará y por qué", "Así se puede comprobar.")],
  open_task=task("Elige un problema: A) basura en una playa, B) sobrepesca de una especie, C) tala de un bosque. Escribe qué pasará si no se hace nada (predicción con razón), una medida de protección para cada problema (parque nacional, veda u otra) y qué dato medirías para saber si funciona.", "Elegí B. Si no se hace nada habrá menos peces. Medida: una veda. Mediré cuántos peces hay antes y después.", ["predicción con razón", "medida que responde al problema", "dato que se podría medir"], ["texto corto"], ["medida que no sirve para el problema", "no decir qué medir"], "Pregunta cómo sabría si la medida funcionó."),
  reinforce="Escribe una medida que puedas hacer en tu casa para cuidar el agua.",
  extend="Escribe una pregunta comprobable sobre el efecto de una veda.")

L(OA4, 3,
  materials="Este cuaderno, lápiz y regla.",
  use="Aprenderé a comparar dos casos de actividad humana con un mismo criterio. Sirve para decidir qué medida protege mejor.",
  prior=["Sé qué es una veda y un parque nacional.", "Sé comparar con un criterio común."],
  explain=[
      "Para comparar casos uso un criterio común: cuántos seres vivos hay, cuánta basura queda o cuánto tiempo tarda en recuperarse. Si comparo dos lugares, mido lo mismo en los dos y en el mismo momento.",
      "Un lugar sin protección puede cambiar rápido. Un lugar protegido, como un parque nacional, limita las actividades dañinas y permite que los seres vivos se recuperen. Una veda ayuda a que una especie aumente. Pero cada medida tiene sus límites: no soluciona todos los problemas.",
      "Al comparar, hay que fijarse en si hay otras diferencias, como el tamaño del lugar o el clima. Si hay más diferencias que la medida, no puedo estar seguro de que la medida causó el cambio. Por eso escribo conclusiones prudentes.",
  ],
  vocab=[("criterio", "característica que se mide igual en todos los casos"), ("zona protegida", "lugar con reglas para cuidarlo"), ("recuperarse", "volver a ser como antes"), ("conclusión prudente", "conclusión que no exagera lo que dicen los datos"), ("diferencia", "lo que cambia entre dos casos")],
  worked=[
      ("Comparar con datos", "Datos de ejemplo. Zona protegida: 90 aves. Zona sin protección: 55 aves. ¿Cuántas aves más hay en la zona protegida?", ["El criterio es 'cantidad de aves'.", "Resto 90 − 55.", "Escribo la diferencia."], "35 aves más"),
      ("Conclusión prudente", "Con esos datos, ¿qué conclusión es más prudente: A) La protección causó 35 aves más. B) Hay más aves en la zona protegida, pero pudieron influir otras diferencias.", ["Reviso qué dice el dato: hay más aves.", "No se probó la causa.", "B no exagera."], "B"),
  ],
  mistakes=[
      ("Comparar la cantidad de aves de un lugar y de peces de otro.", "No es un criterio común.", "Mide lo mismo en ambos."),
      ("Afirmar que la medida es la única causa del cambio.", "Pueden haber otras diferencias.", "Usa frases como 'puede haber influido'."),
  ],
  rec=[
      ("Una conclusión prudente, ¿exagera o no exagera?", "No exagera", "Dice solo lo que apoyan los datos."),
      ("Zona A: 20 aves. Zona B: 12 aves. ¿Cuál tiene más?", "Zona A", "20 es mayor que 12."),
      ("Completa con «igual» o «distinto»: para comparar mido el criterio de forma ______ en los dos lugares.", "Igual", "Así la comparación es justa."),
  ],
  und=[
      ("¿Cuál es un criterio común para comparar dos playas? A) Cantidad de residuos por 100 metros. B) Qué playa es más linda.", "A", "A se puede medir en ambas."),
      ("¿Por qué una zona protegida puede tener más seres vivos?", "Porque se limitan las actividades que los dañan", "Los seres vivos se reponen."),
      ("Si dos lugares difieren en tamaño y en protección, ¿puedo asegurar que la protección causó la diferencia?", "No", "El tamaño también pudo influir."),
  ],
  app=[
      arith("Datos de ejemplo. Playa A: 78 residuos. Playa B: 31 residuos. ¿Cuántos residuos más tiene la playa A?", "78-31", "Se resta el menor al mayor."),
      arith("Datos de ejemplo. Parque: 24 plantas de una especie en un año y 36 al año siguiente. ¿Cuántas más hay?", "36-24", "Se resta el valor inicial al final."),
      ("Datos de ejemplo. Río A tiene 14 peces y río B tiene 14 peces. ¿Qué río tiene más?", "Ninguno; tienen igual cantidad", "Los números son iguales."),
  ],
  rea=[
      ("Ana compara una playa pequeña y limpia con una gran playa sucia. Dice que la limpieza depende del tamaño. ¿Su conclusión es prudente? Responde Sí o No y explica.", "No; no tiene suficientes datos para asegurarlo", "Podría haber otras diferencias."),
      ("Datos de ejemplo. Zona protegida: 60 aves hoy y 40 hace 5 años. Zona sin protección: 25 hoy y 40 hace 5 años. ¿En cuál aumentó la cantidad de aves?", "En la zona protegida", "Subió de 40 a 60; la otra bajó."),
  ],
  cha=[
      ("Escribe una conclusión prudente con los datos de ejemplo: zona protegida 60 aves, zona sin protección 25 aves.", "Hay más aves en la zona protegida, pero otras diferencias pudieron influir", "No exagera lo que dicen los datos."),
      ("Datos de ejemplo. Una veda de 3 años: antes había 80 peces, después hay 140 peces. ¿Cuántos más hay y qué dato extra pedirías?", "60 más; pediría saber cuánta pesca había antes y si hubo otras causas", "El número muestra el cambio, no su causa."),
  ],
  context=[("Datos de ejemplo. En el parque 'A' se contaron 70 plantas nativas y en el parque 'B', 42. En el parque 'A' el recorrido es de 5 km y en el 'B' de 5 km. ¿Cuántas plantas más hay en A?", "28", "70 − 42 = 28. El recorrido es igual, por lo que la comparación es más justa.")],
  selfcheck=[("¿Qué es un criterio común?", "Algo que se mide igual en todos los casos", "Así la comparación es justa."), ("¿Por qué las conclusiones deben ser prudentes?", "Porque los datos pueden tener otras causas", "No hay que exagerar."), ("Nombra una medida de protección.", "Parque nacional o veda", "Son ejemplos de la clase.")],
  open_task=task("Compara dos lugares de tu barrio, por ejemplo una plaza con basureros y otra sin basureros. Cuenta residuos durante 5 minutos en cada una, sin tocarlos. Haz una tabla con el criterio 'residuos contados'. Escribe una conclusión prudente y una diferencia que pudo influir.", "Plaza con basurero: 3 residuos. Plaza sin basurero: 11 residuos. Conclusión: hay menos residuos donde hay basurero, aunque la otra plaza es más grande.", ["tabla con dos lugares", "mismo tiempo de conteo", "conclusión prudente"], ["tabla", "conclusión escrita"], ["contar a distintos tiempos", "afirmar una causa segura"], "Pregunta qué otra diferencia pudo haber entre las plazas."),
  reinforce="Cuenta cuántos árboles ves en dos calles distintas y compáralos.",
  extend="Escribe dos criterios distintos para comparar una zona protegida y una sin proteger.")

L(OA4, 4,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a explicar con un modelo cómo una acción humana llega a afectar a todo un ecosistema. Sirve para ver las conexiones entre componentes.",
  prior=["Sé hacer modelos con flechas.", "Sé que los cambios se transmiten en cadenas alimentarias."],
  explain=[
      "Un modelo de efecto humano usa flechas para mostrar cómo una acción se transmite. Ejemplo: más basura en el agua → menos plantas acuáticas → menos peces → menos aves que comen peces. Cada flecha dice «provoca» o «lleva a».",
      "Con el modelo puedo predecir qué pasará si cambio algo. Si quito la basura, las flechas hacia atrás se detienen y el ecosistema puede recuperarse con el tiempo. Así se entiende por qué una medida pequeña a veces tiene un efecto amplio.",
      "Pero el modelo tiene límites: no muestra todos los seres vivos, ni cuánto tarda cada cambio, ni otras causas como el clima. Un modelo es una ayuda para pensar, no una predicción exacta.",
  ],
  vocab=[("modelo causal", "esquema con flechas que muestra qué provoca qué"), ("efecto", "cambio producido por una acción"), ("causa", "lo que produce un efecto"), ("recuperación", "proceso de volver a ser como antes"), ("límite", "lo que el modelo no muestra")],
  worked=[
      ("Leer un modelo", "Basura en la laguna → agua sucia → menos plantas acuáticas → menos patos. ¿Qué efecto final se muestra?", ["Leo las flechas hasta el final.", "El último eslabón es 'menos patos'.", "Ese es el efecto final."], "Menos patos"),
      ("Cortar la cadena", "Si se limpia la basura de la laguna, ¿qué flecha se detiene primero?", ["Busco la primera causa: la basura.", "Sin basura no hay agua sucia por ella.", "Se detiene la flecha desde la basura."], "La que va de la basura al agua sucia"),
  ],
  mistakes=[
      ("Pensar que el efecto aparece de inmediato.", "Algunos efectos tardan meses o años.", "Escribe que el modelo no muestra el tiempo."),
      ("Creer que una sola causa explica todo el problema.", "Un ecosistema tiene muchas causas a la vez.", "Anota otras posibles causas."),
  ],
  rec=[
      ("En el modelo 'tala → menos árboles → menos refugios', ¿qué es lo primero que ocurre?", "La tala", "Es la causa inicial."),
      ("¿Un modelo de efectos muestra la realidad completa o una parte?", "Una parte", "Es una simplificación."),
      ("Completa con «causa» o «efecto»: la basura en el agua es la ______ del agua sucia.", "Causa", "Produce el agua sucia."),
  ],
  und=[
      ("En 'incendio → menos árboles → menos refugios → menos animales', ¿cuántos efectos hay?", "3", "Menos árboles, menos refugios y menos animales."),
      ("¿Por qué un modelo no muestra todo? A) Porque simplifica. B) Porque está mal hecho.", "A", "Un modelo siempre resume."),
      ("Si se planta un bosque, ¿qué pasa con la cantidad de árboles? Escribe 'más árboles' o 'menos árboles'.", "Más árboles", "Plantar aumenta los árboles."),
  ],
  app=[
      arith("Un modelo tiene una causa y 4 efectos en cadena. ¿Cuántos eslabones tiene en total?", "1+4", "Se suman causa y efectos."),
      ("Completa el modelo: sobrepesca → menos peces → menos ______ que se alimentan de ellos. Elige: pingüinos o pastos.", "Pingüinos", "Los pingüinos comen peces."),
      ("Un parque nacional impide cortar árboles. En el modelo, ¿qué efecto evita?", "Menos refugios", "Cuidar los árboles mantiene los refugios."),
  ],
  rea=[
      ("Beto dice que el modelo 'basura → agua sucia → menos peces' explica todo lo que pasa en una laguna. ¿Tiene razón? Responde Sí o No y explica.", "No; hay otras causas y seres vivos no mostrados", "El modelo es parcial."),
      ("Datos de ejemplo. Después de limpiar una laguna, los peces aumentaron en 2 años. ¿El modelo ayuda a explicar eso? Responde Sí o No y explica.", "Sí; sin basura, el agua mejora y los peces pueden reponerse", "Muestra la cadena inversa."),
  ],
  cha=[
      ("Dibuja con palabras un modelo causal con cuatro eslabones para una playa con basura.", "Basura en la playa → aves comen basura → aves enferman → menos aves", "Una acción con efectos en cadena."),
      ("Escribe un límite del modelo anterior y cómo lo mejorarías.", "No muestra cuánto tarda; agregaría tiempos", "Reconoce lo que falta."),
  ],
  context=[("Un modelo de una laguna muestra 5 pasos desde la basura hasta menos aves. Un estudiante agrega 2 pasos más sobre el clima. ¿Cuántos pasos tiene ahora?", "7", "5 + 2 = 7.")],
  selfcheck=[("¿Qué muestran las flechas de un modelo causal?", "Qué provoca qué", "Son relaciones de causa y efecto."), ("¿Qué límite tiene siempre un modelo?", "No muestra todo lo real", "Un modelo siempre simplifica la realidad."), ("¿Para qué sirve el modelo?", "Para predecir y explicar efectos", "Ayuda a pensar.")],
  open_task=task("Dibuja un modelo con al menos cuatro eslabones para uno de estos problemas: basura en una playa, tala en un bosque o sobrepesca. Usa flechas con verbo. Escribe qué eslabón cortarías con una medida de protección y un límite de tu modelo.", "Sobrepesca → menos peces → menos alimento para pingüinos → menos pingüinos. Corto el primer eslabón con una veda. Límite: no muestra otras causas.", ["cuatro eslabones", "medida que corta un eslabón", "un límite"], ["dibujo con flechas"], ["flechas sin verbo", "no decir qué se corta"], "Pregunta qué eslabón le parece más fácil de cambiar y por qué."),
  reinforce="Dibuja un modelo causal de tres pasos sobre la basura en una calle.",
  extend="Explica con tus palabras por qué es mejor evitar un problema que repararlo.")

L(OA4, 5,
  materials="Este cuaderno, lápiz y lápices de colores. Opcional: cartulina para un afiche.",
  use="Aprenderé a comunicar una conclusión y una medida de protección con razones. Sirve para convencer a otras personas de cuidar un ecosistema.",
  prior=["Sé qué es una veda y un parque nacional.", "Sé hacer conclusiones prudentes."],
  explain=[
      "Comunicar una conclusión significa explicarla con claridad para que otras personas la entiendan. Una buena comunicación tiene cuatro partes: el problema, la evidencia, la medida y la razón por la que la medida ayuda.",
      "Para cuidar un ecosistema podemos elegir medidas como una veda, un parque nacional, el reciclaje o campañas para no dejar basura. La mejor medida depende del problema y de las personas que viven cerca. Todas deben respetar a las personas y a la naturaleza.",
      "Un afiche o una exposición breve debe ser claro, no exagerar los datos y proponer acciones posibles de hacer. Se puede terminar con un compromiso concreto, como 'recogeré la basura de mi curso cada semana'.",
  ],
  vocab=[("comunicar", "dar a conocer una idea con claridad"), ("afiche", "cartel con un mensaje para otras personas"), ("compromiso", "promesa de hacer algo concreto"), ("evidencia", "datos que apoyan una idea"), ("propuesta", "idea de acción para resolver un problema")],
  worked=[
      ("Ordenar las partes", "Una niña escribe: A) medida, B) problema, C) evidencia. ¿Cuál orden es mejor para comunicar?", ["Primero se dice cuál es el problema.", "Luego se muestra la evidencia.", "Al final se propone la medida."], "B, C, A"),
      ("Evaluar una frase", "«Hay 25 latas en la laguna, por eso propongo un basurero.» ¿Tiene evidencia y propuesta?", ["Busco el dato: 25 latas.", "Busco la propuesta: un basurero.", "Están las dos."], "Sí, tiene evidencia y propuesta"),
  ],
  mistakes=[
      ("Mensajes que solo dicen 'no ensucies' sin razón.", "Sin razón, cuesta convencer.", "Explica qué pasa con los seres vivos si ensucias."),
      ("Exagerar con cifras inventadas.", "Una cifra falsa hace que no confíen en el mensaje.", "Usa solo los datos que tienes."),
  ],
  rec=[
      ("¿Una buena comunicación necesita evidencia o solo opiniones?", "Evidencia", "Los datos apoyan la idea."),
      ("¿Un compromiso es una promesa concreta o una idea vaga?", "Una promesa concreta", "Dice qué voy a hacer."),
      ("Completa con «dato» o «adorno»: el afiche debe incluir al menos un ______.", "Dato", "El dato apoya el mensaje."),
  ],
  und=[
      ("¿Qué incluye una buena comunicación? A) Problema, evidencia, medida y razón. B) Solo un dibujo.", "A", "A tiene las cuatro partes."),
      ("¿Por qué conviene dar una razón con la medida?", "Para que otras personas entiendan por qué ayuda", "Una razón convence mejor."),
      ("¿Cuál compromiso es concreto? A) 'Cuidaré el planeta.' B) 'Recogeré la basura de mi pasillo una vez por semana.'", "B", "B dice qué y cuándo."),
  ],
  app=[
      arith("Un curso de 30 estudiantes recoge 3 bolsas cada uno en una limpieza. ¿Cuántas bolsas recogen en total?", "30*3", "Se multiplica el número de estudiantes por las bolsas."),
      ("Ordena el afiche con letras: A) 'Pongamos basureros' B) '25 latas en la laguna' C) 'Si no hay basura, los peces viven mejor'. ¿Cuál es el orden más claro?", "B, A, C", "Primero el dato, luego la medida y luego la razón."),
      ("Un afiche dice: 'Hay muchísima basura en todo Chile'. ¿Es un dato concreto o una exageración?", "Una exageración", "No tiene un número ni un lugar."),
  ],
  rea=[
      ("Mario dice que basta con un afiche para resolver la contaminación. ¿Tiene razón? Responde Sí o No y explica.", "No; también se necesitan acciones", "Un afiche informa, pero hay que actuar."),
      ("Datos de ejemplo. Un curso redujo sus residuos de 50 a 20 bolsas en un mes. Dice: 'Resolvimos la contaminación del país'. ¿Qué conclusión sí está apoyada?", "Redujimos 30 bolsas en nuestro curso", "Los datos solo hablan del curso."),
  ],
  cha=[
      ("Escribe un mensaje de tres frases con problema, evidencia y medida sobre una laguna con 25 latas.", "Hay 25 latas en la laguna. Los peces corren riesgo. Propongo un basurero y una limpieza semanal", "Contiene las tres partes."),
      ("Escribe un compromiso personal para cuidar un ecosistema.", "Llevaré mi basura a un basurero cada vez que visite una plaza", "Es concreto y se puede cumplir."),
  ],
  context=[("Un curso quiere hacer 20 afiches. Cada afiche necesita 2 hojas de cartulina. ¿Cuántas hojas necesita?", "40", "20 × 2 = 40.")],
  selfcheck=[("Nombra las partes de una buena comunicación.", "Problema, evidencia, medida y razón", "Así el mensaje es claro."), ("¿Qué es un compromiso?", "Una promesa concreta de hacer algo", "Se puede cumplir."), ("¿Por qué no hay que exagerar los datos?", "Porque pierde credibilidad el mensaje", "La gente deja de creer.")],
  open_task=task("Haz un afiche o escribe una exposición de un minuto sobre un problema de un ecosistema de Chile. Puedes elegir: basura en una playa, tala en un bosque o sobrepesca. Incluye el problema, un dato de ejemplo, una medida (veda, parque nacional u otra), una razón y un compromiso personal. Muéstralo a una persona de tu casa.", "Problema: basura en una playa. Dato de ejemplo: 25 latas en 10 metros. Medida: basureros y limpieza. Razón: las aves no enferman. Compromiso: recogeré mi basura.", ["problema, dato, medida, razón y compromiso", "sin exagerar", "claro para otra persona"], ["afiche o texto"], ["omitir la razón", "inventar cifras"], "Pregunta qué parte quedó menos clara para quien lo vio."),
  reinforce="Escribe un mensaje de dos frases para tu curso sobre cuidar el agua.",
  extend="Elige una medida de protección y explica quién debería cumplirla.")

# ---------------------------------------------------------------- OA 05
L(OA5, 1,
  materials="Este cuaderno y lápiz. Tu propio cuerpo para tocar con suavidad la cabeza, las costillas y la espalda.",
  use="Aprenderé a observar mi esqueleto tocándolo y a separar lo que siento de lo que supongo. Sirve para conocer los huesos que protegen y sostienen mi cuerpo.",
  prior=["Sé que mi cuerpo tiene partes como cabeza, tronco y extremidades.", "Sé anotar lo que observo."],
  explain=[
      "El sistema esquelético es el conjunto de huesos del cuerpo. Los huesos son duros y sostienen el cuerpo. El cráneo es el hueso de la cabeza y protege el cerebro. Las costillas forman una jaula en el pecho que protege el corazón y los pulmones.",
      "La columna vertebral está en la espalda. Está formada por muchos huesos pequeños llamados vértebras, apilados uno sobre otro. Sostiene el cuerpo y permite agacharse y girar. La pelvis está en la cadera. El fémur es el hueso largo del muslo y es el más largo del cuerpo.",
      "Puedes observar tu esqueleto con suavidad: toca tu cabeza y siente un hueso duro; toca tu pecho y siente las costillas moverse al respirar; toca el centro de tu espalda y siente pequeñas protuberancias. Lo que sientes es evidencia. Decir «los huesos son feos» es una opinión.",
  ],
  vocab=[("esqueleto", "conjunto de huesos del cuerpo"), ("cráneo", "hueso de la cabeza que protege el cerebro"), ("costillas", "huesos del pecho que protegen el corazón y los pulmones"), ("vértebras", "huesos pequeños de la columna"), ("fémur", "hueso largo del muslo")],
  worked=[
      ("Unir hueso y función", "Costillas: ¿protegen el corazón o el estómago?", ["Pienso dónde están las costillas: en el pecho.", "En el pecho están el corazón y los pulmones.", "Las costillas los rodean como una jaula."], "Protegen el corazón y los pulmones"),
      ("Observación o interpretación", "«Siento mis costillas moverse al respirar» y «Mis costillas son las más importantes». ¿Cuál es la observación?", ["Veo qué frase se puede sentir.", "El movimiento al respirar se siente.", "'Las más importantes' es una opinión."], "Siento mis costillas moverse al respirar"),
  ],
  mistakes=[
      ("Pensar que los huesos son una sola pieza dura sin movimiento.", "El esqueleto tiene muchos huesos unidos que se mueven.", "Recuerda que la columna tiene muchas vértebras."),
      ("Creer que las costillas protegen el estómago.", "Protegen el corazón y los pulmones.", "Ubica las costillas en el pecho."),
  ],
  rec=[
      ("¿Qué hueso protege el cerebro: el cráneo o el fémur?", "El cráneo", "Cubre la cabeza."),
      ("¿Dónde están las costillas: en el pecho o en el pie?", "En el pecho", "Rodean el corazón y los pulmones."),
      ("Completa con «vértebras» o «costillas»: la columna está formada por ______.", "Vértebras", "Son huesos pequeños apilados."),
  ],
  und=[
      ("¿Qué órganos protegen las costillas? A) Corazón y pulmones. B) Cerebro.", "A", "Están en el pecho."),
      ("¿Qué hueso es el más largo del cuerpo?", "El fémur", "Es el hueso del muslo."),
      ("¿Para qué sirve la columna vertebral?", "Para sostener el cuerpo y permitir moverse", "Tiene vértebras que se articulan."),
  ],
  app=[
      ("Una niña toca su cabeza, sus costillas y su fémur. ¿Cuántas partes del esqueleto tocó?", "3", "Cráneo, costillas y fémur."),
      ("Clasifica con letras: A) cráneo, B) costillas, C) fémur. ¿Cuál protege órganos del pecho?", "B", "Las costillas protegen corazón y pulmones."),
      arith("Un modelo de columna tiene 24 piezas de cartón. Ya pegaste 10 piezas arriba y 8 piezas abajo. ¿Cuántas piezas faltan por pegar?", "24-10-8", "Se restan las piezas pegadas del total."),
  ],
  rea=[
      ("Ema dice: 'Las costillas son frágiles porque se mueven'. ¿Moverse prueba por sí solo que un hueso es frágil? Responde Sí o No.", "No", "Moverse no prueba fragilidad; haría falta una prueba."),
      ("Una niña respira hondo y siente que sus costillas se mueven un poquito. Con esa observación, ¿las costillas son un bloque inmóvil? Responde Sí o No.", "No", "Se mueven al respirar."),
  ],
  cha=[
      ("Escribe una observación y una interpretación sobre tu columna vertebral.", "Observación: siento pequeñas protuberancias en mi espalda. Interpretación: son las vértebras que me sostienen", "Una se siente; la otra explica."),
      ("Explica por qué se protegen el cerebro y el corazón con huesos distintos.", "Porque cada órgano necesita un hueso con la forma adecuada: el cráneo rodea el cerebro y las costillas el corazón", "Cada protección se adapta al órgano."),
  ],
  context=[("Una maqueta de cartón tiene 8 piezas para el cráneo y 24 piezas para las costillas. ¿Cuántas piezas tiene entre ambas partes?", "32", "8 + 24 = 32.")],
  selfcheck=[("¿Qué protege el cráneo?", "El cerebro", "Cubre la cabeza."), ("¿Qué son las vértebras?", "Huesos pequeños que forman la columna", "Se apilan unos sobre otros."), ("¿Dónde está el fémur?", "En el muslo", "Es el hueso más largo.")],
  open_task=task("Con una persona adulta, toca con suavidad tres partes de tu cuerpo: cráneo, costillas y espalda. Escribe una observación de cada una (lo que sientes) y una interpretación sobre su función. Hazlo sin presionar fuerte ni lastimarte.", "Cráneo: siento un hueso duro. Costillas: se mueven al respirar. Espalda: siento pequeñas protuberancias. Interpretación: la columna me sostiene.", ["tres observaciones", "una interpretación marcada"], ["lista de observaciones"], ["confundir sentir con suponer"], "Pregunta cómo sabe que son huesos y no músculos."),
  reinforce="Dibuja un esqueleto sencillo y rotula cráneo, costillas, columna y fémur.",
  extend="Averigua un dato curioso del fémur y escríbelo con tus palabras.")

L(OA5, 2,
  materials="Este cuaderno, lápiz y tiras de cartón o papel grueso. Cinta adhesiva.",
  use="Aprenderé a preguntar y predecir sobre la columna con un modelo de cartón. Sirve para entender por qué la columna tiene muchos huesos pequeños.",
  prior=["Sé qué son las vértebras.", "Sé hacer una predicción con razón."],
  explain=[
      "La columna vertebral no es un solo hueso largo: está formada por muchas vértebras unidas. Eso le permite doblarse hacia adelante, hacia atrás y hacia los lados sin romperse. Por dentro de las vértebras pasa un canal que protege la médula espinal.",
      "Para probar esta idea puedes hacer un modelo: una tira de cartón rígido y otra tira hecha con varios trozos pegados con un poco de cinta. Preguntas: «¿Cuál se dobla mejor?». Predices: «La de trozos se doblará más, porque tiene muchas uniones».",
      "Después anotas lo que pasó. Un modelo no es una columna real: no tiene discos ni músculos. Sirve para comprobar una idea simple. Una buena conclusión dice: «En este modelo, la tira de trozos se dobló más».",
  ],
  vocab=[("médula espinal", "cordón nervioso protegido dentro de la columna"), ("modelo", "objeto que representa algo real para probar una idea"), ("flexible", "que se dobla sin romperse"), ("rígido", "que no se dobla fácilmente"), ("unión", "lugar donde se juntan dos partes")],
  worked=[
      ("Predecir", "Tira A: un solo cartón rígido. Tira B: tres trozos de cartón pegados con cinta. ¿Cuál se doblará más?", ["Miro las uniones.", "La B tiene dos uniones.", "Las uniones permiten doblar."], "La B"),
      ("Leer un resultado", "Datos de ejemplo. Tira A se dobló 10 grados. Tira B se dobló 60 grados. ¿Cuántos grados más se dobló B?", ["Comparo 60 y 10.", "Resto 60 − 10.", "Escribo el resultado con unidad."], "50 grados más"),
  ],
  mistakes=[
      ("Pensar que la columna es un solo hueso largo.", "Son muchas vértebras.", "Cuenta las partes del modelo."),
      ("Pensar que el modelo es igual a la columna.", "El modelo no tiene discos ni músculos.", "Escribe un límite."),
  ],
  rec=[
      ("¿La columna tiene una o muchas piezas?", "Muchas", "Son las vértebras."),
      ("¿Qué protege la médula espinal: la columna o la rodilla?", "La columna", "Pasa por dentro de las vértebras."),
      ("Completa con «rígido» o «flexible»: un cartón de una sola pieza es ______.", "Rígido", "No se dobla fácilmente."),
  ],
  und=[
      ("¿Por qué la columna tiene vértebras? A) Para permitir doblarse. B) Para ser más pesada.", "A", "Las uniones permiten flexibilidad."),
      ("¿Cuál se dobla más: un cartón entero o uno con tres trozos unidos?", "El de tres trozos unidos", "Sus uniones permiten doblar."),
      ("¿Qué representan las uniones de cinta en el modelo?", "Las uniones entre vértebras", "Ambas uniones permiten el movimiento."),
  ],
  app=[
      arith("Datos de ejemplo. Tira entera: se dobló 8 grados. Tira con cinco trozos: se dobló 68 grados. ¿Cuántos grados más se dobló la de cinco trozos?", "68-8", "Se resta el menor al mayor."),
      ("Predice: si agregas más uniones a la tira de trozos, ¿se doblará más o menos?", "Más", "Más uniones permiten más doblez."),
      ("Un niño usa dos tiras: una de 20 cm y otra de 30 cm. Para que la comparación sea justa, ¿qué debe cuidar?", "Que midan lo mismo", "Si no, el largo influye."),
  ],
  rea=[
      ("Luis dice que su modelo prueba cuántas vértebras tenemos. ¿Es correcto? Responde Sí o No y explica.", "No; el modelo solo muestra que las uniones permiten doblar", "No sirve para contar."),
      ("Ana dobló la tira de trozos y se desarmó. ¿Qué limitación tiene su modelo?", "Las uniones de cinta no son tan firmes como las vértebras", "La cinta se despega, las vértebras no."),
  ],
  cha=[
      ("Escribe una pregunta comprobable y una predicción sobre la columna con un modelo de cartón.", "¿Se dobla más una tira con uniones que una sin ellas? Predigo que sí, porque las uniones permiten doblar", "Se compara con un modelo."),
      ("¿Por qué conviene que la médula espinal pase por dentro de las vértebras?", "Porque queda protegida", "Los huesos la rodean."),
  ],
  context=[("En clase se hacen 6 modelos de columna. Cada uno usa 4 trozos de cartón. ¿Cuántos trozos se necesitan?", "24", "6 × 4 = 24.")],
  selfcheck=[("¿De qué está formada la columna?", "De muchas vértebras unidas", "Eso la hace flexible."), ("¿Qué protege la columna por dentro?", "La médula espinal", "Pasa por un canal en las vértebras."), ("¿Qué límite tiene el modelo de cartón?", "No tiene discos ni músculos", "Es una simplificación.")],
  open_task=task("Con una persona adulta, haz dos tiras de cartón de 20 cm: una entera y otra hecha de cuatro trozos unidos con cinta. Escribe tu predicción: ¿cuál se dobla más y por qué? Dóblalas con suavidad y anota qué pasó. Escribe una conclusión y un límite del modelo. No uses tijeras sin ayuda.", "Predicción: se doblará más la de trozos. Resultado: la de trozos se dobló bien y la entera no. Conclusión: en este modelo las uniones permiten doblar. Límite: no tiene músculos.", ["predicción con razón", "resultado observado", "límite del modelo"], ["registro con dibujo"], ["no escribir el límite"], "Pregunta qué cambiaría si usara más trozos."),
  reinforce="Dobla una cadena de papel pegada y una tira entera y compáralas.",
  extend="Averigua qué es un disco intervertebral y escribe su función en una frase.")

L(OA5, 3,
  materials="Este cuaderno y lápiz.",
  use="Aprenderé a comparar huesos según su función: proteger, sostener y mover. Sirve para entender por qué cada hueso tiene su forma.",
  prior=["Sé nombrar cráneo, costillas, vértebras y fémur.", "Sé comparar con un criterio."],
  explain=[
      "Los huesos cumplen tres funciones principales. Proteger: el cráneo cubre el cerebro y las costillas cubren el corazón y los pulmones. Sostener: la columna vertebral mantiene el cuerpo erguido. Mover: la pelvis y el fémur ayudan a caminar y correr.",
      "La pelvis es un hueso grande en la cadera que une la columna con las piernas. Se une al fémur en la cadera. Gracias a esa unión podemos caminar, correr y agacharnos. El fémur es largo y fuerte porque soporta el peso del cuerpo.",
      "Para comparar los huesos usamos el criterio función: ¿protege, sostiene o permite mover? El cráneo es duro y curvo porque rodea y protege el cerebro. El fémur es largo porque ayuda a mover y soportar peso. La forma de un hueso se relaciona con su función.",
  ],
  vocab=[("pelvis", "hueso grande de la cadera"), ("función", "para qué sirve algo"), ("proteger", "cubrir para evitar daños"), ("sostener", "mantener algo en su lugar"), ("mover", "cambiar de posición el cuerpo")],
  worked=[
      ("Clasificar por función", "Cráneo, columna y fémur. ¿Cuál función principal tiene cada uno?", ["Cráneo cubre el cerebro: proteger.", "Columna mantiene erguido el cuerpo: sostener.", "Fémur permite caminar: mover."], "Cráneo: proteger; columna: sostener; fémur: mover"),
      ("Relacionar forma y función", "¿Por qué el fémur es largo y fuerte?", ["Pienso en lo que hace: sostiene el peso y permite caminar.", "Un hueso largo da pasos amplios.", "Un hueso fuerte aguanta el peso."], "Porque debe soportar el peso del cuerpo y permitir caminar"),
  ],
  mistakes=[
      ("Pensar que cada hueso tiene solo una función.", "Algunos cumplen más de una.", "Nombra la función principal y otras posibles."),
      ("Confundir la pelvis con el fémur.", "La pelvis está en la cadera y el fémur en el muslo.", "Ubica cada una en el cuerpo."),
  ],
  rec=[
      ("¿Qué función cumple el cráneo: proteger o mover?", "Proteger", "Cubre el cerebro."),
      ("¿Dónde está la pelvis: en la cadera o en el brazo?", "En la cadera", "Une la columna con las piernas."),
      ("Completa con «sostener» o «proteger»: la columna sirve para ______ el cuerpo.", "Sostener", "Mantiene el cuerpo erguido."),
  ],
  und=[
      ("¿Qué huesos ayudan a mover las piernas? A) Pelvis y fémur. B) Cráneo y costillas.", "A", "Se unen en la cadera."),
      ("¿Qué función cumplen las costillas?", "Proteger el corazón y los pulmones", "Forman una jaula."),
      ("¿Por qué el cráneo es curvo?", "Porque rodea y protege el cerebro", "La forma se relaciona con la función."),
  ],
  app=[
      ("Une función y hueso: proteger el cerebro. ¿Cuál es el hueso?", "El cráneo", "Cubre la cabeza."),
      ("Datos de ejemplo. Un esqueleto de modelo tiene 6 huesos que protegen, 5 que sostienen y 9 que ayudan a mover. ¿Cuántos huesos tiene?", "20", "6 + 5 + 9 = 20."),
      ("Ordena de arriba abajo en el cuerpo: A) fémur, B) cráneo, C) pelvis. ¿Cuál es el orden?", "B, C, A", "Cabeza, cadera y muslo."),
  ],
  rea=[
      ("Una niña dice que si no tuviéramos fémur no podríamos caminar bien. ¿Es una afirmación razonable? Responde Sí o No y explica.", "Sí; el fémur soporta el peso y se une a la pelvis para mover la pierna", "Es parte del movimiento de la pierna."),
      ("Dos huesos: uno duro y curvo que forma una especie de casco, otro largo y recto. ¿Cuál se parece más al cráneo? Explica.", "El curvo, porque rodea al cerebro", "La forma se relaciona con proteger."),
  ],
  cha=[
      ("Completa: 'El cráneo ______, las costillas ______ y la columna ______.' Usa: protege, protegen, sostiene.", "Protege; protegen; sostiene", "Cada hueso cumple su función."),
      ("Explica por qué sería un problema si la pelvis no se uniera al fémur.", "No podríamos mover bien las piernas", "La unión permite el movimiento."),
  ],
  context=[("En un museo hay 3 esqueletos y cada uno tiene 2 fémures. ¿Cuántos fémures hay en total?", "6", "3 × 2 = 6.")],
  selfcheck=[("Nombra las tres funciones de los huesos vistas.", "Proteger, sostener y mover", "Son las funciones principales."), ("¿Qué hueso une la columna con las piernas?", "La pelvis", "Está en la cadera."), ("¿Por qué la forma importa?", "Porque se relaciona con la función", "Cada hueso está adaptado.")],
  open_task=task("Haz una tabla con cinco huesos: cráneo, costillas, columna, pelvis y fémur. Columnas: dónde está, función principal y una característica de su forma. Escribe una frase que compare dos de ellos con el mismo criterio. Puedes usar un libro de la casa.", "Cráneo: cabeza; proteger; curvo. Fémur: muslo; mover; largo. Comparación: el cráneo protege y el fémur permite mover.", ["tabla completa", "criterio común", "una comparación"], ["tabla"], ["confundir ubicación", "olvidar la función"], "Pregunta cuál hueso tiene más de una función."),
  reinforce="Dibuja el esqueleto y pinta con un color los huesos que protegen y con otro los que mueven.",
  extend="Averigua en un libro otro hueso que proteja un órgano.")

L(OA5, 4,
  materials="Este cuaderno, lápiz y lápices de colores. Opcional: cartón y cinta.",
  use="Aprenderé a explicar con un modelo cómo los huesos protegen, sostienen y mueven, y a decir sus límites. Sirve para comunicar cómo funciona el esqueleto.",
  prior=["Sé las funciones de los huesos.", "Sé que un modelo tiene límites."],
  explain=[
      "Un modelo del esqueleto puede ser un dibujo con huesos rotulados, una maqueta de cartón o un esquema con flechas. En él marco qué huesos protegen (cráneo y costillas), cuáles sostienen (columna) y cuáles ayudan a mover (pelvis y fémur).",
      "Con el modelo puedo explicar: «Las costillas forman una jaula que protege el corazón; si faltara una parte de la jaula, el corazón quedaría expuesto». También puedo predecir: «Si la columna no tuviera vértebras, no podríamos doblarnos». Así uso el modelo para pensar.",
      "Los modelos tienen límites. Un dibujo no muestra los músculos que mueven los huesos ni cómo crecen con la edad. Los huesos reales se renuevan y están vivos. Siempre escribo qué no muestra mi modelo.",
  ],
  vocab=[("modelo", "representación simple de algo real"), ("rotular", "escribir nombres sobre un dibujo"), ("maqueta", "modelo tridimensional"), ("esquema", "dibujo simple con nombres y flechas"), ("límite", "lo que el modelo no muestra")],
  worked=[
      ("Rotular", "En un dibujo, la jaula del pecho debe llevar un nombre. ¿Cuál?", ["Miro su forma de jaula.", "Se trata de las costillas.", "Rotulo 'costillas'."], "Costillas"),
      ("Límite del modelo", "Un dibujo del esqueleto no muestra los músculos. ¿Es un límite?", ["Comparo con el cuerpo real.", "Los músculos mueven los huesos.", "El dibujo los deja fuera."], "Sí, es un límite"),
  ],
  mistakes=[
      ("Creer que el dibujo es igual al esqueleto real.", "El dibujo simplifica.", "Escribe qué no muestra."),
      ("Rotular sin decir la función.", "Un nombre no explica.", "Agrega para qué sirve cada hueso."),
  ],
  rec=[
      ("¿Un dibujo del esqueleto es el esqueleto real o un modelo?", "Un modelo", "Representa algo real."),
      ("¿Qué hueso rotularías en la cabeza: cráneo o fémur?", "Cráneo", "Cubre el cerebro."),
      ("Completa con «límite» o «nombre»: lo que el modelo no muestra es un ______.", "Límite", "Es algo real que falta."),
  ],
  und=[
      ("¿Qué muestra mejor las funciones? A) Un esquema con nombres y funciones. B) Solo los nombres.", "A", "Explica para qué sirve."),
      ("¿Por qué un modelo de huesos no explica el movimiento por sí solo?", "Porque faltan los músculos", "Los músculos mueven los huesos."),
      ("¿Qué se predice con el modelo: 'sin vértebras, no podríamos doblarnos'?", "Una consecuencia", "Dice qué pasaría si algo falta."),
  ],
  app=[
      arith("Un modelo de cartón usa 4 piezas para el cráneo y 12 para las costillas. ¿Cuántas piezas usa?", "4+12", "Se suman las piezas."),
      ("Rotula: la parte del dibujo que está en el muslo, ¿cuál es? Elige: fémur o pelvis.", "Fémur", "Está en el muslo."),
      ("En un esquema, una línea une el fémur con la pelvis. ¿Qué podría mostrar esa línea?", "Que se unen en la cadera", "La unión permite el movimiento de la pierna."),
  ],
  rea=[
      ("Mario dice que su maqueta explica todo el cuerpo. ¿Tiene razón? Responde Sí o No y explica.", "No; solo muestra los huesos", "No incluye músculos ni órganos."),
      ("Predice con el modelo: sin cráneo, ¿qué quedaría sin protección?", "El cerebro", "El cráneo lo rodea."),
  ],
  cha=[
      ("Escribe una explicación de tres frases usando un modelo del esqueleto.", "Las costillas protegen el corazón. La columna sostiene el cuerpo. El fémur y la pelvis permiten caminar", "Cubre las tres funciones."),
      ("Escribe un límite de tu maqueta y cómo lo mejorarías.", "No muestra los músculos; agregaría elásticos", "Reconoce lo que falta."),
  ],
  context=[("Para una maqueta se necesitan 1 cráneo, 12 costillas por lado y 1 columna. Si cada lado tiene 12 costillas, ¿cuántas costillas son?", "24", "12 × 2 = 24.")],
  selfcheck=[("¿Qué es un modelo?", "Una representación simple de algo real", "Ayuda a explicar."), ("¿Qué límite tiene un dibujo del esqueleto?", "No muestra los músculos", "Los músculos mueven los huesos."), ("¿Qué debe incluir tu explicación?", "El hueso y su función", "Así la explicación queda completa.")],
  open_task=task("Dibuja un esqueleto sencillo y rotula cráneo, costillas, columna, pelvis y fémur. Junto a cada nombre escribe su función. Escribe una predicción ('si faltara…') y un límite de tu dibujo.", "Cráneo: protege el cerebro. Costillas: protegen el corazón. Columna: sostiene. Pelvis y fémur: mueven. Predicción: sin vértebras no podría doblarme. Límite: no muestra músculos.", ["cinco huesos rotulados", "función de cada uno", "predicción y límite"], ["dibujo rotulado"], ["omitir funciones", "sin límite"], "Pregunta qué músculo faltaría para que se mueva."),
  reinforce="Dibuja tu mano y rotula los huesos que puedas.",
  extend="Averigua qué es una articulación y escribe un ejemplo.")

# ---------------------------------------------------------------- OA 06
L(OA6, 1,
  materials="Este cuaderno y lápiz. Tu brazo y tu pierna para moverlos con suavidad.",
  use="Aprenderé a observar cómo se mueve mi cuerpo y a nombrar músculos, huesos, tendones y articulaciones. Sirve para entender cómo me muevo.",
  prior=["Sé nombrar algunos huesos.", "Sé anotar lo que observo."],
  explain=[
      "El movimiento del cuerpo ocurre porque trabajan juntos cuatro tipos de partes. Los huesos dan estructura. Los músculos se contraen, es decir, se acortan y tiran de los huesos. Los tendones son cuerdas resistentes que unen los músculos a los huesos. Las articulaciones son los lugares donde se unen dos huesos, como el codo o la rodilla.",
      "Dobla tu brazo y toca con suavidad la parte de arriba: sentirás un músculo que se pone duro. Esa es una observación. El músculo bíceps se contrae y tira del hueso del antebrazo. En la rodilla ocurre algo parecido: los músculos del muslo tiran de los huesos de la pierna.",
      "Los músculos solo pueden tirar, no empujar. Por eso trabajan en pares: uno tira para doblar la articulación y otro tira para estirarla. Decir «mi músculo es fuerte» es una opinión; decir «mi bíceps se pone duro al doblar el brazo» es evidencia.",
  ],
  vocab=[("músculo", "parte del cuerpo que se contrae para producir movimiento"), ("tendón", "cuerda resistente que une un músculo con un hueso"), ("articulación", "lugar donde se unen dos huesos"), ("contraerse", "acortarse un músculo"), ("bíceps", "músculo de la parte delantera del brazo")],
  worked=[
      ("Identificar partes", "El codo une el hueso del brazo y los del antebrazo. ¿Es un músculo, un tendón o una articulación?", ["Veo que une dos huesos.", "Eso hacen las articulaciones.", "El codo es una articulación."], "Una articulación"),
      ("Observación o interpretación", "«Mi bíceps se pone duro al doblar el brazo» y «Mi bíceps es el mejor músculo». ¿Cuál es evidencia?", ["Reviso qué frase se puede sentir.", "Lo duro se siente.", "'El mejor' es opinión."], "Mi bíceps se pone duro al doblar el brazo"),
  ],
  mistakes=[
      ("Pensar que los huesos se mueven solos.", "Son los músculos los que tiran de ellos.", "Recuerda: músculo + tendón + hueso."),
      ("Creer que los músculos empujan.", "Los músculos solo tiran.", "Piensa en pares de músculos."),
  ],
  rec=[
      ("¿Qué une un tendón: un músculo con un hueso o dos huesos?", "Un músculo con un hueso", "Es una cuerda resistente."),
      ("¿El codo es una articulación o un músculo?", "Una articulación", "El codo une dos huesos."),
      ("Completa con «tira» o «empuja»: un músculo se contrae y ______ del hueso.", "Tira", "Los músculos solo tiran."),
  ],
  und=[
      ("¿Qué hace el bíceps al doblar el brazo? A) Se contrae. B) Se alarga y empuja.", "A", "Se acorta y tira."),
      ("¿Dónde están las articulaciones de la pierna? A) Cadera y rodilla. B) Solo en el pie.", "A", "Hay articulaciones en varios lugares."),
      ("¿Qué ocurre si un tendón se corta?", "El músculo ya no puede mover el hueso", "El tendón conecta ambos."),
  ],
  app=[
      ("Une cada parte con lo que hace: 1) músculo, 2) tendón, 3) articulación. A) une dos huesos, B) se contrae y tira, C) une el músculo con el hueso. Escribe las letras en orden: 1, 2, 3.", "B, C, A", "El músculo tira, el tendón lo une al hueso y la articulación une dos huesos."),
      arith("Una persona dobla el brazo 15 veces y la pierna 12 veces. ¿Cuántos movimientos hizo en total?", "15+12", "Se suman ambos."),
      ("Ordena: A) el músculo se contrae, B) el hueso se mueve, C) el tendón tira. ¿Cuál es el orden?", "A, C, B", "El músculo se acorta, el tendón tira y el hueso se mueve."),
  ],
  rea=[
      ("Ema dice que sus huesos se mueven solos porque ve su brazo doblarse. ¿Tiene razón? Responde Sí o No y explica.", "No; los músculos tiran de los huesos", "Los huesos no tienen forma de moverse por sí solos."),
      ("Una niña observa que al estirar el brazo el bíceps se relaja. ¿Qué sucede con otro músculo del brazo? Escribe 'se contrae' o 'se relaja'.", "Se contrae", "Los músculos trabajan en pares."),
  ],
  cha=[
      ("Escribe una observación y una interpretación sobre el movimiento de tu rodilla.", "Observación: la rodilla se dobla y se estira. Interpretación: los músculos del muslo la mueven", "Una se siente; la otra explica."),
      ("Explica por qué un músculo solo no puede empujar un hueso.", "Porque los músculos solo se acortan y tiran", "Su acción es contraerse."),
  ],
  context=[("Un entrenador cuenta que en un calentamiento un grupo dobla el brazo 10 veces y estira el brazo 10 veces. ¿Cuántos movimientos hacen?", "20", "10 + 10 = 20.")],
  selfcheck=[("¿Qué hace un músculo?", "Se contrae y tira del hueso", "Produce el movimiento."), ("¿Qué es un tendón?", "Una cuerda que une músculo y hueso", "Transmite la fuerza."), ("¿Qué es una articulación?", "Lugar donde se unen dos huesos", "Esa unión permite mover el cuerpo.")],
  open_task=task("Con tu brazo y tu pierna, haz estos movimientos suaves: doblar y estirar el codo, doblar y estirar la rodilla. Toca con suavidad el músculo del brazo y del muslo. Escribe dos observaciones y una interpretación. No fuerces las articulaciones.", "Observación: el bíceps se pone duro al doblar el codo. Observación: la rodilla se dobla hacia atrás. Interpretación: el músculo tira del hueso.", ["dos observaciones", "una interpretación marcada", "nombra músculo y articulación"], ["registro escrito"], ["mezclar sentir con suponer"], "Pregunta qué parte tira del hueso."),
  reinforce="Dibuja tu brazo doblado y rotula bíceps, hueso y codo.",
  extend="Averigua el nombre del músculo de la parte de atrás del brazo.")

L(OA6, 2,
  materials="Este cuaderno y lápiz. Tu brazo para observar y, si quieres, una regla y una banda elástica de papelería con ayuda de una persona adulta.",
  use="Aprenderé a preguntar y predecir sobre músculos que trabajan en pares y la actividad física. Sirve para entender cómo cuidar mi cuerpo.",
  prior=["Sé qué son músculos, tendones y articulaciones.", "Sé que una predicción tiene razón."],
  explain=[
      "Los músculos trabajan en pares. Cuando el bíceps se contrae, el codo se dobla. Cuando el tríceps, en la parte de atrás del brazo, se contrae, el codo se estira. Mientras uno se contrae, el otro se relaja. Así el brazo puede moverse en ambas direcciones.",
      "Una pregunta comprobable puede ser: «¿Se pone más duro el bíceps cuando sostengo un libro con el brazo doblado?». La predicción: «Sí, porque el músculo trabaja más para sostener el peso». Para probarla, tocas con suavidad el bíceps con y sin el libro.",
      "La actividad física regular fortalece los músculos y ayuda a que los huesos se mantengan firmes. También mejora la coordinación y la flexibilidad. Pero hay que hacerla con cuidado, calentar antes y no forzar el cuerpo.",
  ],
  vocab=[("tríceps", "músculo de la parte de atrás del brazo"), ("relajarse", "dejar de contraerse"), ("coordinación", "capacidad de mover el cuerpo de forma ordenada"), ("actividad física", "ejercicio o juego que mueve el cuerpo"), ("calentar", "mover el cuerpo con suavidad antes de hacer ejercicio")],
  worked=[
      ("Pares de músculos", "Para doblar el codo, ¿qué músculo se contrae: bíceps o tríceps?", ["El bíceps está al frente del brazo.", "Al contraerse tira del antebrazo hacia arriba.", "El codo se dobla."], "El bíceps"),
      ("Hacer una predicción", "Un niño sostiene un libro con el brazo doblado y toca su bíceps. Predice si estará más duro o más blando que sin libro.", ["Pienso en el trabajo del músculo.", "Con el libro el músculo trabaja más.", "Se pone más duro."], "Más duro, porque trabaja más al sostener el peso"),
  ],
  mistakes=[
      ("Creer que los dos músculos del par se contraen a la vez.", "Mientras uno se contrae, el otro se relaja.", "Piensa en 'uno tira, el otro se suelta'."),
      ("Hacer ejercicio sin calentar.", "Puede lastimar músculos y articulaciones.", "Calienta con movimientos suaves."),
  ],
  rec=[
      ("Cuando el bíceps se contrae, ¿el tríceps se contrae o se relaja?", "Se relaja", "Trabajan en pares."),
      ("¿La actividad física fortalece o debilita los músculos?", "Fortalece", "Ejercitarlos los hace más resistentes."),
      ("Completa con «antes» o «después»: se calienta ______ de hacer ejercicio.", "Antes", "Prepara los músculos."),
  ],
  und=[
      ("¿Qué músculo estira el codo? A) Tríceps. B) Bíceps.", "A", "Está en la parte de atrás del brazo."),
      ("¿Cuál es una pregunta comprobable? A) ¿Cuántas flexiones de brazo puedo hacer en 30 segundos? B) ¿Es lindo el bíceps?", "A", "Se puede contar."),
      ("¿Para qué sirve calentar antes de hacer ejercicio?", "Para preparar los músculos y evitar lesiones", "Los músculos fríos se lastiman más fácil."),
  ],
  app=[
      arith("Un niño hace 12 sentadillas el lunes y 18 el viernes. ¿Cuántas más hizo el viernes?", "18-12", "Se resta el valor menor al mayor."),
      ("Predice: si haces ejercicio de brazos cada día durante un mes, ¿qué pasará con la fuerza de tus músculos? Escribe 'aumentará' o 'disminuirá'.", "Aumentará", "La actividad regular fortalece."),
      ("Un niño estira el brazo. ¿Qué músculo se relaja: el bíceps o el tríceps?", "El bíceps", "El tríceps se contrae al estirar."),
  ],
  rea=[
      ("Luis dice que, si hace ejercicio un solo día, ya tendrá músculos fuertes. ¿Tiene razón? Responde Sí o No y explica.", "No; el cambio ocurre con ejercicio regular", "Los músculos se fortalecen con práctica constante."),
      ("Datos de ejemplo. Ana hizo 10 sentadillas el lunes y 14 el viernes. Dice: 'Mi cuerpo es más fuerte por la actividad'. ¿Bastan esos dos días para asegurarlo? Responde Sí o No.", "No", "Pocos días no prueban la causa."),
  ],
  cha=[
      ("Escribe una pregunta comprobable sobre los músculos y una forma de medir.", "¿Cuántas veces puedo subir y bajar un libro con el brazo en 30 segundos? Cuento las veces", "Se responde contando."),
      ("Explica por qué los huesos también se benefician de la actividad física.", "Porque se mantienen firmes y fuertes al usarse", "Ejercitar el cuerpo ayuda a los huesos."),
  ],
  context=[("Un curso hace actividad física 3 veces por semana durante 4 semanas. ¿Cuántas sesiones hacen en total?", "12", "3 × 4 = 12.")],
  selfcheck=[("¿Cómo trabajan los músculos?", "En pares: uno se contrae y el otro se relaja", "Así hay movimiento en ambas direcciones."), ("Nombra un beneficio de la actividad física.", "Fortalece músculos y huesos", "Es uno de los beneficios vistos."), ("¿Qué se hace antes de ejercitarse?", "Calentar", "Calentar previene lesiones musculares.")],
  open_task=task("Con cuidado, cuenta cuántas veces puedes subir y bajar una botella plástica pequeña llena de agua con un brazo en 30 segundos, en dos días distintos. Toca tu bíceps con suavidad mientras lo haces. Escribe una pregunta, tu predicción, tus conteos y una conclusión prudente. Para en cuanto sientas dolor.", "Pregunta: ¿cuántas veces subo la botella en 30 segundos? Predicción: unas 15. Lunes: 14 veces. Miércoles: 16 veces. Conclusión: este día hice más, pero hay pocos datos.", ["pregunta comprobable", "dos conteos", "conclusión prudente"], ["tabla de conteos"], ["forzar el cuerpo", "afirmar una causa segura"], "Pregunta qué más pudo cambiar entre los dos días."),
  reinforce="Anota qué actividad física haces en una semana y cuántos días.",
  extend="Escribe una pregunta comprobable sobre las piernas y cómo la medirías.")

L(OA6, 3,
  materials="Este cuaderno, lápiz y regla.",
  use="Aprenderé a comparar el movimiento del brazo y la pierna según sus articulaciones. Sirve para entender por qué cada articulación se mueve de cierta forma.",
  prior=["Sé qué son músculos, tendones y articulaciones.", "Sé comparar con un criterio."],
  explain=[
      "El brazo y la pierna se parecen. Ambos tienen un hueso largo arriba (húmero en el brazo, fémur en la pierna) y dos huesos abajo. Ambos tienen una articulación en el medio: el codo y la rodilla. Ambos se doblan y se estiran por la acción de pares de músculos.",
      "Pero se usan para cosas distintas. El brazo se mueve mucho para tomar, empujar y lanzar. La pierna soporta el peso del cuerpo y permite caminar y correr. Por eso la rodilla es fuerte y estable, y el hombro tiene un movimiento más amplio.",
      "Para comparar uso un criterio: qué articulación, cuántas direcciones de movimiento tiene o qué músculos intervienen. Un codo y una rodilla se mueven como una bisagra: se doblan y se estiran en un plano, como una puerta.",
  ],
  vocab=[("húmero", "hueso largo del brazo"), ("bisagra", "movimiento que se abre y cierra en un plano, como una puerta"), ("estable", "firme, que no se mueve fácilmente"), ("criterio", "característica que se mira igual en los dos casos"), ("hombro", "articulación que une el brazo al tronco")],
  worked=[
      ("Comparar articulaciones", "Codo y rodilla. ¿En qué se parecen?", ["Ambos están en el medio de una extremidad.", "Ambos se doblan y se estiran.", "Los dos se mueven como bisagra."], "Se doblan y se estiran como una bisagra"),
      ("Comparar funciones", "¿Qué extremidad soporta más peso del cuerpo: el brazo o la pierna?", ["Pienso en cuando estoy de pie.", "Son las piernas las que sostienen el cuerpo.", "Por eso son más fuertes."], "La pierna"),
  ],
  mistakes=[
      ("Pensar que el codo y la rodilla doblan hacia el mismo lado.", "El codo se dobla hacia adelante y la rodilla hacia atrás.", "Observa tu propio cuerpo con suavidad."),
      ("Decir que el brazo y la pierna son iguales.", "Se parecen, pero cumplen funciones distintas.", "Compara con un criterio."),
  ],
  rec=[
      ("¿El codo está en el brazo o en la pierna?", "En el brazo", "Une el hueso del brazo y los del antebrazo."),
      ("¿La rodilla está en el brazo o en la pierna?", "En la pierna", "Une el fémur y los huesos de abajo."),
      ("Completa con «bisagra» o «giro»: el codo se mueve como una ______.", "Bisagra", "Se dobla y estira en un plano."),
  ],
  und=[
      ("¿Qué tienen en común el codo y la rodilla? A) Ambos se doblan y se estiran. B) Ambos están en la cabeza.", "A", "Son articulaciones tipo bisagra."),
      ("¿Qué extremidad soporta el peso del cuerpo?", "La pierna", "Las piernas nos mantienen de pie."),
      ("¿Por qué la rodilla debe ser fuerte?", "Porque sostiene el peso del cuerpo", "Está en la pierna."),
  ],
  app=[
      arith("Datos de ejemplo. En una prueba, el codo se dobló 40 veces y la rodilla 25 veces en un minuto. ¿Cuántas más veces se dobló el codo?", "40-25", "Se resta el menor al mayor."),
      ("Une articulación y extremidad: rodilla. ¿Brazo o pierna?", "Pierna", "Está entre el fémur y los huesos de abajo."),
      ("Un niño dice que su codo se dobla hacia atrás. ¿Es correcto? Responde Sí o No.", "No", "El codo se dobla hacia adelante."),
  ],
  rea=[
      ("Ana dice que el brazo y la pierna hacen el mismo trabajo. ¿Tiene razón? Responde Sí o No y explica.", "No; la pierna sostiene el peso y el brazo se usa más para tomar y lanzar", "Cumplen funciones distintas."),
      ("Un niño quiere comparar su brazo y su pierna. Para que sea justo, ¿qué debe usar: el mismo criterio o criterios distintos?", "El mismo criterio", "Si no, la comparación no es justa."),
  ],
  cha=[
      ("Escribe un parecido y una diferencia entre el brazo y la pierna.", "Parecido: ambos tienen una articulación que se dobla. Diferencia: la pierna sostiene más peso", "Compara con un criterio."),
      ("¿Qué pasaría si la rodilla no se doblara?", "Sería difícil caminar y sentarse", "La rodilla permite flexionar la pierna."),
  ],
  context=[("En una clase de educación física se hacen 3 series de 10 flexiones de codo y 3 series de 10 flexiones de rodilla. ¿Cuántos movimientos se hacen en total?", "60", "3 × 10 = 30 y 3 × 10 = 30; 30 + 30 = 60.")],
  selfcheck=[("¿Cómo se mueve el codo?", "Como una bisagra", "Se dobla y se estira."), ("¿Qué extremidad soporta el peso?", "La pierna", "Mantiene el cuerpo de pie."), ("¿Qué hace un criterio?", "Permite comparar con justicia", "Se mide igual en ambos.")],
  open_task=task("Haz una tabla con dos columnas: brazo y pierna. Filas: hueso largo de arriba (húmero y fémur), articulación del medio (codo y rodilla), función principal. Escribe un parecido y una diferencia. Mueve con suavidad tu codo y tu rodilla para comprobar cómo se doblan.", "Brazo: húmero, codo, tomar y lanzar. Pierna: fémur, rodilla, sostener y caminar. Parecido: ambos se doblan como bisagra. Diferencia: la pierna sostiene el peso.", ["tabla completa", "un parecido", "una diferencia"], ["tabla"], ["mezclar criterios"], "Pregunta qué observó al mover su codo y su rodilla."),
  reinforce="Dibuja tu brazo y tu pierna doblados y rotula el codo y la rodilla.",
  extend="Averigua cómo se llama el hueso de la parte baja del brazo y de la pierna.")

L(OA6, 4,
  materials="Este cuaderno, lápiz, cartón, dos ligas y cinta adhesiva. Con una persona adulta si usas tijeras.",
  use="Aprenderé a explicar con un modelo de brazo cómo trabajan músculos, huesos, tendones y articulación, y por qué la actividad física ayuda. Sirve para comunicar mi aprendizaje.",
  prior=["Sé las partes del movimiento.", "Sé que un modelo tiene límites."],
  explain=[
      "Un modelo de brazo puede hacerse con dos tiras de cartón unidas en el medio por un clip o un cordel, como el codo. Se pegan dos ligas: una que va de arriba hacia el antebrazo por delante (bíceps) y otra por atrás (tríceps). Las ligas representan los músculos.",
      "Al tirar de la liga de adelante, el antebrazo sube y el codo se dobla. Al tirar de la de atrás, el brazo se estira. Así el modelo muestra que los músculos tiran y que trabajan en pares. Los tendones serían los puntos de pegado de las ligas a los cartones.",
      "El modelo tiene límites. Las ligas se estiran y vuelven; los músculos de verdad se contraen. El cartón no crece ni se repara. Pero el modelo permite explicar la idea. Además, la actividad física ayuda a mantener fuertes los músculos y los huesos.",
  ],
  vocab=[("modelo", "representación simple de algo real"), ("liga", "banda elástica que representa un músculo en el modelo"), ("antebrazo", "parte del brazo entre el codo y la muñeca"), ("repararse", "arreglarse un tejido dañado"), ("beneficio", "ventaja o ayuda")],
  worked=[
      ("Leer el modelo", "Las ligas del modelo representan: ¿músculos o huesos?", ["Miro qué se estira y tira.", "Los músculos tiran.", "Las ligas hacen eso."], "Músculos"),
      ("Beneficio", "¿Qué beneficio tiene la actividad física para los huesos?", ["Pienso en lo que usan los huesos.", "Al usarse se mantienen firmes.", "Esto ayuda a tener huesos fuertes."], "Ayuda a mantenerlos fuertes y firmes"),
  ],
  mistakes=[
      ("Creer que el modelo es igual al brazo real.", "Las ligas no son músculos reales.", "Escribe un límite."),
      ("Pensar que la actividad física solo sirve para los músculos.", "También beneficia a los huesos y a la coordinación.", "Nombra varios beneficios."),
  ],
  rec=[
      ("En el modelo, ¿qué representa el cartón: huesos o músculos?", "Huesos", "Es rígido como los huesos."),
      ("¿La actividad física ayuda a mantener fuertes los huesos?", "Sí", "Los huesos se mantienen firmes al usarse."),
      ("Completa con «tira» o «empuja»: la liga delantera ______ del antebrazo.", "Tira", "Los músculos tiran."),
  ],
  und=[
      ("¿Qué representa la liga de atrás? A) El tríceps. B) El cráneo.", "A", "Está en la parte de atrás del brazo."),
      ("¿Qué hace el modelo cuando tiras de la liga de adelante?", "El antebrazo sube y el codo se dobla", "Imita la acción del bíceps."),
      ("Menciona un beneficio de la actividad física para el sistema musculoesquelético.", "Fortalece músculos y huesos", "Es el beneficio visto."),
  ],
  app=[
      arith("Un modelo usa 2 tiras de cartón y 2 ligas. Si haces 5 modelos iguales, ¿cuántas ligas necesitas?", "5*2", "Se multiplican modelos por ligas."),
      ("Predice: si quitas la liga de atrás, ¿podrá el brazo estirarse por sí solo? Responde Sí o No.", "No", "No hay quien tire para estirar."),
      ("¿Cuál de estas actividades fortalece los músculos? A) Correr y saltar. B) Estar sentado todo el día.", "A", "Mover el cuerpo lo ejercita."),
  ],
  rea=[
      ("Mario dice que el modelo prueba que los músculos son ligas. ¿Tiene razón? Responde Sí o No y explica.", "No; el modelo solo imita cómo tiran", "Los músculos son tejidos vivos."),
      ("Datos de ejemplo. Una niña hace actividad física 4 días a la semana. Su amiga, 1 día. Ana dice que la primera tendrá siempre mejores huesos. ¿Qué conclusión es prudente?", "Hacer más ejercicio regular ayuda, pero influyen otros factores", "No hay certeza absoluta."),
  ],
  cha=[
      ("Escribe una explicación de cuatro frases con las palabras: músculo, tendón, hueso y articulación.", "El músculo se contrae y tira del tendón. El tendón mueve el hueso. La articulación une los huesos. Así se dobla el brazo", "Usa las cuatro partes."),
      ("Escribe un límite del modelo de cartón y ligas.", "Las ligas no se contraen como los músculos reales", "Reconoce la diferencia."),
  ],
  context=[("Una clase hace un modelo de brazo con 2 ligas por estudiante. Hay 24 estudiantes. ¿Cuántas ligas necesitan?", "48", "24 × 2 = 48.")],
  selfcheck=[("¿Qué representan las ligas del modelo?", "Los músculos", "Tiran de los cartones."), ("¿Qué beneficio tiene la actividad física?", "Fortalece músculos y huesos", "Ayuda al sistema musculoesquelético."), ("¿Qué límite tiene el modelo?", "Las ligas no se contraen como los músculos reales", "El modelo solo imita la acción.")],
  open_task=task("Con una persona adulta, construye un modelo de brazo con dos tiras de cartón unidas en el medio con cordel o clip y dos ligas (una por delante y otra por atrás). Tira de cada liga y observa. Dibuja el modelo, rotula músculo, hueso, tendón y articulación. Escribe un límite y un beneficio de la actividad física.", "Rotulé liga delantera = bíceps, cartón = hueso, clip = codo. Al tirar de la liga delantera, el brazo se dobló. Límite: las ligas no son músculos reales. Beneficio: la actividad fortalece los músculos.", ["modelo funcional", "cuatro partes rotuladas", "un límite y un beneficio"], ["dibujo", "texto corto"], ["olvidar los tendones", "no escribir un límite"], "Pregunta qué parte del modelo representa al tendón."),
  reinforce="Dibuja un brazo con las cuatro partes del movimiento y rotúlalas.",
  extend="Escribe una rutina corta y segura de calentamiento de tres movimientos.")
