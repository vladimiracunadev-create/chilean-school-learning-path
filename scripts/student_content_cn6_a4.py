"""Cuaderno del estudiante, 6.º básico Ciencias Naturales: OA 07 (efectos nocivos de las drogas) y OA 08 (energía y Sol)."""
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


OA7, OA8 = "CN06 OA 07", "CN06 OA 08"

# ---------------------------------------------------------------- OA 07
L(OA7, 1,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y están escritos en los ejercicios. Nunca se hacen pruebas con drogas: solo se analiza información.",
  use="Aprenderé qué es una droga, qué daños puede causar el tabaco, el alcohol y la marihuana, y a separar los datos de las suposiciones. Sirve para cuidarme con información confiable.",
  prior=["Sé que el cuerpo tiene sistemas, como el nervioso y el respiratorio.", "Sé que una observación es lo que se mide o se cuenta."],
  explain=[
      "Una droga es una sustancia que cambia el funcionamiento del cuerpo, sobre todo del sistema nervioso. Algunas son legales para personas adultas, como el tabaco y el alcohol, pero hacen daño y no se pueden vender a menores de 18 años. Otras están prohibidas por la ley, como la marihuana y la cocaína (por ejemplo, su venta y su tráfico). También los medicamentos pueden dañar si se usan sin indicación de un médico.",
      "El tabaco contiene nicotina, que genera dependencia, y muchas otras sustancias que dañan los pulmones y el corazón. El alcohol enlentece el sistema nervioso: baja la coordinación, los reflejos y el juicio, y con el tiempo daña el hígado y el cerebro. La marihuana afecta la atención, la memoria y la coordinación, y en la adolescencia puede dificultar el aprendizaje. La dependencia es la necesidad intensa de seguir consumiendo aunque haga daño.",
      "Al leer información sobre drogas hay que separar datos de suposiciones. Una observación es «de 120 adultos que fuman, 90 dicen que quieren dejarlo». Una interpretación es «dejarlo es fácil». Una frase puede sonar convincente sin tener evidencia. Siempre conviene preguntar: ¿qué dato la apoya y quién la dijo?",
  ],
  vocab=[("droga", "sustancia que cambia el funcionamiento del cuerpo"), ("nicotina", "sustancia del tabaco que genera dependencia"), ("dependencia", "necesidad intensa de seguir consumiendo aunque dañe"), ("sistema nervioso", "conjunto de órganos que controlan y coordinan el cuerpo"), ("evidencia", "datos que apoyan una afirmación")],
  worked=[
      ("Observación o interpretación", "Dos frases de un informe de ejemplo: (1) «De 120 adultos que fuman, 90 dicen que quieren dejarlo». (2) «Dejar de fumar es muy fácil». ¿Cuál es una observación?", ["Pregunto qué frase tiene un dato.", "La frase 1 tiene números.", "La frase 2 es una idea sin dato."], "La frase 1"),
      ("Calcular una parte", "De 120 adultos de ejemplo que fuman, 90 quieren dejarlo. ¿Cuántos no lo quieren o no lo dicen?", ["Total: 120.", "Quieren dejarlo: 90.", "Resto 120 − 90."], "30 adultos"),
  ],
  mistakes=[
      ("Pensar que, como el tabaco y el alcohol son legales para adultos, no hacen daño.", "Que sea legal no quiere decir que sea seguro.", "Revisa los efectos en la salud con fuentes confiables."),
      ("Creer una frase solo porque sale en un video o la dice un amigo.", "Una afirmación necesita datos y una fuente confiable.", "Pregunta qué dato la apoya."),
  ],
  rec=[
      ("¿El tabaco contiene nicotina: Sí o No?", "Sí", "La nicotina genera dependencia."),
      ("La necesidad intensa de seguir consumiendo aunque haga daño se llama ______. Completa con «dependencia» o «descanso».", "Dependencia", "Es una de las consecuencias del consumo."),
      ("¿En Chile se puede vender tabaco a menores de 18 años: Sí o No?", "No", "La ley lo prohíbe."),
  ],
  und=[
      ("¿Cuál es una interpretación? A) De 120 adultos que fuman, 90 quieren dejarlo. B) Dejarlo es muy fácil.", "B", "No tiene un dato que la apoye."),
      ("¿Qué órgano daña principalmente el humo del tabaco?", "Los pulmones", "El humo entra por la vía respiratoria."),
      ("¿Qué sistema afecta el alcohol al enlentecer reflejos y juicio?", "El sistema nervioso", "Coordina los movimientos y las decisiones."),
  ],
  app=[
      arith("En una encuesta de ejemplo, 200 adultos fuman y 140 quieren dejarlo. ¿Cuántos no lo han dicho?", "200-140", "Se resta los que quieren dejarlo del total."),
      arith("Una persona de ejemplo fuma 10 cigarrillos al día. ¿Cuántos fuma en 30 días?", "10*30", "Se multiplica por los días."),
      ("De estas sustancias, ¿cuántas son legales para adultos: tabaco, alcohol, marihuana, cocaína?", "2", "Son el tabaco y el alcohol."),
  ],
  rea=[
      ("Un afiche dice: «Un poco de alcohol no daña a nadie». ¿Qué pregunta harías primero? A) ¿Qué dato lo apoya y quién lo dice? B) ¿De qué color es el afiche?", "A", "Una afirmación debe tener evidencia."),
      ("Un amigo dice que como su vecino fuma y no se ha enfermado, el tabaco no daña. ¿Es una conclusión válida? Responde Sí o No y explica.", "No; un caso no representa a todos", "Los datos de una sola persona no bastan."),
  ],
  cha=[
      ("En un registro de ejemplo, 300 personas fuman y 270 sienten que no pueden dejarlo. ¿Cuántas de cada 10 sienten que no pueden dejarlo?", "9", "270 de 300 equivale a 9 de cada 10."),
      ("¿Qué pregunta ayuda a revisar si un dato sobre drogas es confiable? A) ¿Quién lo dice y qué evidencia entrega? B) ¿Cuántas personas lo compartieron?", "A", "Revisar la fuente y la evidencia protege de errores."),
  ],
  context=[("Dato de ejemplo. Una escuela hizo una charla sobre el tabaco con 80 estudiantes y 56 dijeron haber aprendido algo nuevo. ¿Cuántos no?", "24", "80 − 56 = 24.")],
  selfcheck=[("¿Qué es una droga?", "Una sustancia que cambia el funcionamiento del cuerpo", "Afecta sobre todo al sistema nervioso."), ("¿Qué es la dependencia?", "La necesidad intensa de seguir consumiendo aunque haga daño", "Hace difícil dejar el consumo."), ("¿Cómo se reconoce una interpretación?", "No tiene un dato medible que la apoye", "Se debe contrastar con evidencia.")],
  open_task=task("Lee estos datos de ejemplo de un cartel: «De cada 10 adultos que fuman, 7 quieren dejarlo. Muchos dicen que es relajante». Escribe una observación con números, una interpretación y una pregunta que harías para comprobar la frase «es relajante».", "Observación: 7 de cada 10 quieren dejarlo. Interpretación: se siente relajante. Pregunta: ¿qué dato mide si el tabaco relaja o solo calma la ansiedad de no tener nicotina?", ["una observación con números", "una interpretación rotulada", "una pregunta de verificación"], ["tres frases escritas"], ["tratar la opinión como dato", "no pedir evidencia"], "Pregunta qué fuente confiable consultaría para comprobar."),
  reinforce="Escribe dos datos que podrías buscar para saber si algo daña la salud.",
  extend="Explica por qué «es legal» no significa «es seguro».")

L(OA7, 2,
  materials="Este cuaderno, lápiz y una regla de 30 cm. Opcional: una persona de tu casa para la prueba de reflejos con regla. Los datos de las drogas son de estudios de ejemplo; nunca se prueban en personas.",
  use="Aprenderé a formular preguntas y predicciones sobre los efectos de las drogas usando datos de estudios. Sirve para entender cómo la ciencia investiga sin hacer daño.",
  prior=["Sé qué es una droga y qué es la dependencia.", "Sé que una predicción lleva una razón."],
  explain=[
      "La ciencia investiga los efectos de las drogas con estudios cuidadosos, nunca dándoselas a niños. Una forma es medir los reflejos. En la prueba de la regla, una persona suelta una regla y otra la atrapa con los dedos. Mientras menos centímetros cae la regla antes de atraparla, más rápidos son los reflejos. Puedes hacer esta prueba en casa sentado, descansado y luego distraído con una conversación.",
      "En estudios de ejemplo con personas adultas, se compara la distancia que cae la regla antes y después de que el cuerpo recibe alcohol. Una pregunta comprobable es: «¿Cuántos centímetros cae la regla en promedio con y sin alcohol?». Una predicción con razón es: «Con alcohol la regla caerá más, porque el alcohol enlentece el sistema nervioso».",
      "Como las drogas son peligrosas, los estudios solo se hacen con adultos, bajo control y con permiso. Un niño o niña nunca debe probar para comprobar. Los datos que ya existen alcanzan para decidir cuidarse. Una predicción es prudente cuando dice «probablemente» y reconoce que cada persona responde distinto.",
  ],
  vocab=[("reflejo", "respuesta rápida del cuerpo a algo que ocurre"), ("promedio", "valor que resulta de sumar y dividir por la cantidad de datos"), ("estudio", "investigación con método y datos"), ("enlentecer", "hacer más lento"), ("permiso informado", "aceptación de una persona adulta que sabe en qué consiste el estudio")],
  worked=[
      ("Leer el resultado", "En un estudio de ejemplo, la regla cayó 12 cm sin alcohol y 24 cm con alcohol. ¿Cuántos centímetros más cayó con alcohol?", ["Identifico los dos valores: 12 y 24.", "Resto 24 − 12.", "Interpreto: reflejos más lentos."], "12 cm más; los reflejos fueron más lentos"),
      ("Predicción con razón", "Antes de ver los datos, ¿qué predices sobre la distancia con alcohol y por qué?", ["El alcohol enlentece el sistema nervioso.", "Si reacciona más lento, la regla cae más.", "Escribo la predicción con razón."], "La regla caerá más, porque el alcohol enlentece el sistema nervioso"),
  ],
  mistakes=[
      ("Querer probar una droga «solo una vez» para comprobar un dato.", "Puede dañar y generar dependencia.", "Usa estudios y datos ya existentes."),
      ("Concluir con una sola medición.", "Una medición puede tener errores.", "Repite varias veces y calcula el promedio."),
  ],
  rec=[
      ("En la prueba de la regla, si la regla cae menos, ¿los reflejos son más rápidos o más lentos?", "Más rápidos", "Atrapó la regla antes."),
      ("¿Los estudios sobre drogas se hacen con niños: Sí o No?", "No", "Serían estudios peligrosos para ellos."),
      ("Una predicción lleva siempre una ______. Completa con «razón» o «sorpresa».", "Razón", "Dice por qué se espera el resultado."),
  ],
  und=[
      ("¿Qué mide la prueba de la regla?", "La rapidez de los reflejos", "Se mide cuánto cae la regla."),
      ("¿Cuál pregunta es comprobable? A) ¿Cuántos cm cae la regla en promedio en 3 intentos? B) ¿Qué reflejo es más lindo?", "A", "Los centímetros se miden."),
      ("¿Por qué se predice que con alcohol la regla caerá más?", "Porque el alcohol enlentece el sistema nervioso", "La reacción es más lenta."),
  ],
  app=[
      arith("Tres intentos de ejemplo sin alcohol: 10, 12 y 14 cm. ¿Cuál es el promedio?", "(10+12+14)//3", "Se suman y se divide por 3."),
      arith("Tres intentos de ejemplo con alcohol: 21, 24 y 27 cm. ¿Cuál es el promedio?", "(21+24+27)//3", "Se suman y se divide por 3."),
      ("Si el promedio sin alcohol es 13 cm y con alcohol 22 cm, ¿en qué condición los reflejos fueron más lentos?", "Con alcohol", "La regla cayó más."),
  ],
  rea=[
      ("Un compañero propone: «Probemos tabaco unas cuantas veces para ver qué pasa». ¿Es una buena idea? Responde Sí o No y explica.", "No; es peligroso y genera dependencia", "Se usan estudios con adultos, no con niños."),
      ("Un estudio de ejemplo midió solo una vez a una persona. ¿Qué falta para confiar más? A) Repetir la medición con varias personas. B) Cambiar el color de la regla.", "A", "Así se reducen los errores."),
  ],
  cha=[
      ("Resultados de ejemplo: con descanso, 11 cm; distraído, 19 cm. Una persona dice: «Me distraje y reaccioné más lento». ¿Cuántos centímetros más cayó cuando estaba distraído?", "8", "19 − 11 = 8."),
      ("Marca la mejor predicción. A) Con el alcohol la regla probablemente caerá más, porque se enlentecen los reflejos. B) Con el alcohol la regla caerá igual, porque sí.", "A", "La A tiene razón y dice «probablemente»."),
  ],
  context=[("Dato de ejemplo. En un estudio con adultos, la regla cayó 15 cm antes y 30 cm después. ¿Cuántos centímetros más cayó después?", "15", "30 − 15 = 15.")],
  selfcheck=[("¿Qué indica una regla que cae menos centímetros antes de ser atrapada?", "Reflejos más rápidos", "Menos distancia, reflejos más rápidos."), ("¿Por qué los estudios no se hacen con niños?", "Porque las drogas son peligrosas", "Las drogas pueden dañarlos."), ("¿Qué lleva una buena predicción?", "Lo que ocurrirá y su razón", "Así se puede comprobar.")],
  open_task=task("Haz la prueba de la regla, sin ninguna sustancia, con una persona de tu casa: una persona suelta la regla de 30 cm y la otra la atrapa. Anota la distancia en 3 intentos sentado y en 3 intentos mientras conversan de otro tema. Calcula el promedio de cada condición y escribe una predicción con razón. Si no puedes hacer la prueba, usa estos datos de ejemplo: sentado, 10, 11, 12; distraído, 18, 20, 19.", "Sentado: promedio 11. Distraído: promedio 19. Predicción: la distracción enlentece la reacción porque el cerebro atiende dos cosas.", ["tres intentos por condición", "promedios correctos", "predicción con razón"], ["tabla de datos", "frase de predicción"], ["usar un solo intento", "no comparar condiciones"], "Pregunta qué conclusión se puede dar con estos datos y cuál no."),
  reinforce="Calcula el promedio de 8, 10 y 12 centímetros.",
  extend="Explica por qué la ciencia usa estudios con adultos, bajo control, para conocer los efectos de las drogas.")

L(OA7, 3,
  materials="Este cuaderno y lápiz. Opcional: lápices de colores.",
  use="Aprenderé a modelar cómo una sustancia llega al cerebro y cómo tomar decisiones de protección. Sirve para saber cómo decir que no y buscar ayuda.",
  prior=["Sé que las drogas afectan el sistema nervioso.", "Sé que un modelo simplifica y tiene límites."],
  explain=[
      "Un modelo de cómo actúa una droga: la sustancia entra al cuerpo, por ejemplo por los pulmones en el humo o por el estómago en una bebida. Pasa a la sangre y viaja por todo el cuerpo. Llega al cerebro y a otros órganos, y cambia su funcionamiento. En el caso del tabaco, el humo también daña directamente los pulmones. El esquema es: entrada → sangre → cerebro y otros órganos → efectos.",
      "Otro modelo sirve para decidir. Si te ofrecen una droga, puedes seguir estos pasos: 1) Di «no» con voz firme. 2) Da una razón corta, por ejemplo «no me interesa». 3) Propón otra actividad. 4) Aléjate del lugar. 5) Cuéntaselo a una persona adulta de confianza, como un familiar, un profesor o personal del consultorio. No es necesario dar explicaciones largas ni discutir.",
      "Estos modelos tienen límites. El esquema de la sangre no muestra cuánto tarda cada droga ni cuánto cambia según la persona. El modelo de decisión no cubre todos los casos, como cuando la presión viene de alguien conocido. Por eso siempre se puede pedir ayuda a una persona adulta.",
  ],
  vocab=[("presión de grupo", "empuje de otras personas para que hagas algo"), ("asertivo", "que dice lo que piensa con firmeza y respeto"), ("persona adulta de confianza", "adulto al que puedes contarle algo y pedirle ayuda"), ("consultorio", "centro de salud cercano"), ("límite del modelo", "algo que el modelo no muestra")],
  worked=[
      ("Ordenar el camino de una sustancia", "Ordena: cerebro, entrada al cuerpo, sangre.", ["La sustancia primero entra al cuerpo.", "Luego pasa a la sangre.", "La sangre la lleva al cerebro."], "Entrada al cuerpo → sangre → cerebro"),
      ("Elegir la respuesta asertiva", "Un compañero te ofrece algo dañino. ¿Qué respuesta es asertiva? A) «No, gracias, no me interesa». B) «Bueno, solo esta vez».", ["Busco la respuesta firme y respetuosa.", "A dice no con una razón corta.", "B cede a la presión."], "A"),
  ],
  mistakes=[
      ("Pensar que hay que discutir hasta convencer al otro.", "No necesitas convencer, solo cuidarte.", "Di no, aléjate y busca a un adulto."),
      ("Creer que contar lo que pasó es «acusar».", "Pedir ayuda es una forma de cuidarte.", "Cuéntalo a una persona adulta de confianza."),
  ],
  rec=[
      ("¿La sustancia viaja por la sangre: Sí o No?", "Sí", "La sangre la reparte por el cuerpo."),
      ("¿Decir «no» con firmeza es una respuesta asertiva o agresiva?", "Asertiva", "Es firme pero respetuosa."),
      ("¿A quién puedes contarle: a una persona adulta de confianza o a nadie?", "A una persona adulta de confianza", "Pedir ayuda protege."),
  ],
  und=[
      ("¿Cuál es el primer paso al recibir una oferta dañina?", "Decir no con voz firme", "Es el paso 1 del modelo."),
      ("¿Para qué sirve proponer otra actividad?", "Para cambiar la situación sin discutir", "Ayuda a salir de la presión."),
      ("¿Qué límite tiene el esquema de la sangre?", "No muestra cuánto tarda ni cómo cambia según la persona", "Es un modelo simple."),
  ],
  app=[
      ("Ordena los pasos con letras: A) Aléjate. B) Di «no». C) Cuéntaselo a un adulto de confianza. D) Da una razón corta.", "B, D, A, C", "Es el orden del modelo."),
      arith("Un curso de 40 estudiantes practicó decir no. Si 28 lo hicieron bien en el primer intento, ¿cuántos necesitaron otro intento?", "40-28", "Se resta los que lo hicieron bien."),
      ("¿Cuál de estas frases no es asertiva? «No, gracias», «No me interesa», «Ya, dame, igual todos lo hacen», «Voy a otro lado».", "Ya, dame, igual todos lo hacen", "Cede a la presión."),
  ],
  rea=[
      ("Un estudiante cree que, si alguien conocido le ofrece algo dañino, no debe contarlo para no acusar. ¿Qué es lo mejor? A) Contarlo a un adulto de confianza. B) Guardar el secreto.", "A", "Pedir ayuda es una forma de cuidarse."),
      ("¿Qué órgano falta nombrar en «entrada → sangre → efectos» para explicar por qué cambian la atención y las emociones?", "El cerebro", "Allí actúan las sustancias que generan dependencia."),
  ],
  cha=[
      ("¿Cuál frase es asertiva y corta? A) «No, gracias, no me interesa». B) «Bueno, pero no se lo cuentes a nadie».", "A", "Es firme, corta y respetuosa."),
      ("Un modelo dice «entrada → sangre → cerebro». ¿Qué órgano recibe primero el humo del tabaco antes de pasar a la sangre?", "Los pulmones", "El humo se inhala."),
  ],
  context=[("Dato de ejemplo. En una dramatización, 5 grupos de 6 estudiantes practicaron decir no. ¿Cuántos estudiantes participaron?", "30", "5 × 6 = 30.")],
  selfcheck=[("¿Qué camino sigue una sustancia en el cuerpo?", "Entra, pasa a la sangre y llega al cerebro y otros órganos", "Es el esquema."), ("¿Cuáles son los pasos para rechazar una oferta?", "Decir no, dar una razón corta, proponer otra actividad, alejarse y contárselo a un adulto", "Es el modelo de decisión."), ("¿Por qué pedir ayuda no es acusar?", "Porque es una forma de cuidarse", "Los adultos de confianza pueden ayudar.")],
  open_task=task("Escribe un guion de 4 líneas de una situación en que un compañero te ofrece tabaco en el recreo. Incluye: tu respuesta firme, una razón corta, una propuesta de otra actividad y a quién se lo contarías. Puedes practicarlo con una persona de tu casa.", "Compañero: «Toma, prueba». Yo: «No, gracias, no me interesa». «Mejor juguemos a la pelota». Después se lo cuento a mi profesora.", ["respuesta firme y respetuosa", "razón corta", "propuesta y adulto de confianza"], ["guion escrito"], ["ceder a la presión", "no incluir a un adulto"], "Pregunta qué haría si la presión viniera de alguien conocido."),
  reinforce="Escribe tres personas adultas de confianza a las que podrías contarles.",
  extend="Explica por qué practicar en voz alta ayuda a responder cuando hay presión.")

L(OA7, 4,
  materials="Este cuaderno y lápiz. Los mensajes están escritos en los ejercicios.",
  use="Aprenderé a comparar fuentes de información y estrategias de protección usando un criterio. Sirve para decidir en qué mensajes confiar.",
  prior=["Sé que una afirmación necesita evidencia.", "Conozco los pasos para rechazar una oferta."],
  explain=[
      "No toda la información sobre drogas es confiable. Un criterio para comparar fuentes es revisar cuatro preguntas: ¿quién lo dice?, ¿entrega datos?, ¿es una persona o institución de salud?, ¿es reciente? Un mensaje de un profesional de la salud con datos y fecha es más confiable que un rumor sin dueño. Un video que exagera o promete resultados mágicos suele ser poco confiable.",
      "Para comparar, se cuenta cuántas preguntas cumple cada mensaje. Si un mensaje cumple 4 de 4, es muy confiable; si cumple 1 de 4, es poco confiable. Algo parecido pasa con estrategias de protección: se prefiere la que es más segura y se puede aplicar en la vida real. Por ejemplo, alejarse y contar a un adulto es más seguro que discutir con quien presiona.",
      "El criterio tiene límites. Una fuente confiable puede equivocarse y una poco conocida puede tener razón. Por eso se contrastan varias fuentes. Una conclusión debe decir qué criterio se usó y qué no se pudo comprobar.",
  ],
  vocab=[("fuente", "origen de una información"), ("confiable", "que se puede creer porque tiene evidencia"), ("rumor", "información que circula sin saber quién la dijo"), ("contrastar", "comparar varias fuentes"), ("estrategia", "plan para lograr algo")],
  worked=[
      ("Aplicar el criterio", "Mensaje A: un médico del consultorio explica con datos y fecha de este año los daños del tabaco. Mensaje B: un rumor sin autor dice que el alcohol «limpia» el cuerpo. ¿Cuál es más confiable?", ["Reviso las cuatro preguntas en A: quién, datos, institución de salud y fecha.", "B no dice quién lo dijo ni da datos.", "A cumple más preguntas."], "El mensaje A"),
      ("Contar cumplimiento", "Un mensaje cumple 3 de las 4 preguntas. ¿Cuántas le faltan?", ["Total: 4.", "Cumple: 3.", "Resto 4 − 3."], "Le falta 1"),
  ],
  mistakes=[
      ("Confiar en un mensaje porque tiene muchas visitas o «me gusta».", "La popularidad no es evidencia.", "Revisa quién lo dice y qué datos entrega."),
      ("Descartar una fuente confiable porque no te gusta lo que dice.", "El criterio es la evidencia, no el gusto.", "Evalúa con las cuatro preguntas."),
  ],
  rec=[
      ("Una fuente confiable, ¿entrega datos o solo opiniones?", "Datos", "Los datos se pueden revisar."),
      ("¿Un rumor sin autor es confiable: Sí o No?", "No", "No se sabe quién lo dice."),
      ("¿Un profesional de la salud es una fuente más confiable que un video anónimo?", "Sí", "Tiene formación y entrega datos."),
  ],
  und=[
      ("¿Cuáles son las cuatro preguntas del criterio? Elige la lista correcta. A) Quién, datos, institución de salud y fecha. B) Color, tamaño, ruido y precio.", "A", "Son las preguntas de confiabilidad."),
      ("Un mensaje cumple 1 de 4 preguntas. ¿Es muy confiable o poco confiable?", "Poco confiable", "Cumple muy pocas."),
      ("¿Por qué conviene contrastar varias fuentes?", "Porque una sola puede equivocarse", "Compararlas da más seguridad."),
  ],
  app=[
      arith("Tres mensajes cumplieron 4, 2 y 1 preguntas del criterio. ¿Cuántas preguntas cumplieron en total?", "4+2+1", "Se suman los cumplimientos."),
      ("Mensaje X: 4 de 4. Mensaje Y: 2 de 4. Mensaje Z: 3 de 4. Ordénalos de más a menos confiable.", "X, Z, Y", "Se ordena según las preguntas cumplidas."),
      ("Estrategia 1: discutir con quien presiona. Estrategia 2: alejarse y contárselo a un adulto. ¿Cuál es más segura?", "La 2", "Evita el conflicto y busca ayuda."),
  ],
  rea=[
      ("Un video muy visto dice «el cigarrillo electrónico no tiene nicotina», pero no entrega datos ni fuente. ¿Es confiable? Responde Sí o No y explica.", "No; no entrega datos ni fuente", "Muchas visitas no son evidencia."),
      ("Alguien dice: «Mi tío es médico, así que seguro tiene razón en todo». ¿Qué debe hacer para estar más seguro? A) Contrastar con otras fuentes. B) Confiar sin preguntar.", "A", "Contrastar da más seguridad."),
  ],
  cha=[
      ("Un cartel cumple 3 de 4 preguntas y otro cumple 2. ¿Cuántas preguntas más cumple el primero?", "1", "3 − 2 = 1."),
      ("Marca la mejor conclusión. A) La fuente que cumple 4 de 4 es más confiable, pero conviene contrastarla. B) La fuente que cumple 4 de 4 nunca se equivoca.", "A", "La B afirma más de lo que prueba el criterio."),
  ],
  context=[("Dato de ejemplo. Un curso revisó 20 mensajes sobre drogas y 8 cumplieron las 4 preguntas. ¿Cuántos no las cumplieron todas?", "12", "20 − 8 = 12.")],
  selfcheck=[("¿Qué preguntas se hacen a una fuente?", "Quién lo dice, si entrega datos, si es de salud y si es reciente", "Son cuatro preguntas distintas."), ("¿Por qué no basta con que un mensaje sea popular?", "Porque la popularidad no es evidencia", "No prueba que sea cierto."), ("¿Qué estrategia es más segura ante la presión?", "Alejarse y contarlo a un adulto de confianza", "Evita el riesgo.")],
  open_task=task("Evalúa estos dos mensajes de ejemplo con las cuatro preguntas. Mensaje 1: «Un médico de un consultorio, en un informe de este año, explica con cifras que el alcohol afecta el cerebro en desarrollo». Mensaje 2: «Alguien en un chat dice que probar una vez no afecta, sin explicar por qué». Escribe cuántas preguntas cumple cada uno y cuál es más confiable.", "Mensaje 1 cumple 4 de 4. Mensaje 2 cumple 0 de 4. El mensaje 1 es más confiable; conviene contrastarlo con otra fuente de salud.", ["cuenta bien cada mensaje", "elige el más confiable", "menciona contrastar"], ["tabla con conteos", "frase de conclusión"], ["confiar por popularidad", "no contrastar"], "Pregunta qué otra fuente de salud revisaría."),
  reinforce="Escribe las cuatro preguntas para evaluar una fuente.",
  extend="Explica por qué conviene contrastar incluso fuentes confiables.")

L(OA7, 5,
  materials="Este cuaderno y lápiz. Opcional: una hoja de cartulina o papel para el afiche.",
  use="Aprenderé a comunicar con evidencia los efectos nocivos de algunas drogas y a proponer conductas de protección. Sirve para hacer un mensaje claro que ayude a otros.",
  prior=["Conozco los efectos del tabaco, el alcohol y la marihuana.", "Sé evaluar una fuente con cuatro preguntas."],
  explain=[
      "Un buen mensaje para cuidar la salud tiene cuatro partes: un dato, el efecto, una conducta de protección y un límite. Por ejemplo: «El humo del tabaco contiene nicotina, que genera dependencia (dato). Daña los pulmones y el corazón (efecto). Si te ofrecen, di no, aléjate y cuéntaselo a un adulto de confianza (protección). Los efectos varían de persona a persona (límite)».",
      "Las conductas de protección pueden ser personales y colectivas. Personales: informarte en fuentes confiables, no aceptar nada de personas desconocidas, decir no con firmeza, no tomar medicamentos sin indicación médica. Colectivas: actividades deportivas y artísticas en el colegio, espacios libres de humo y apoyo entre compañeros. Si alguien necesita ayuda, puede acudir a su consultorio o a una persona adulta de confianza.",
      "Un buen mensaje no asusta con exageraciones ni juzga a las personas que tienen dependencia. Reconoce que la dependencia es una condición de salud que se puede tratar con ayuda profesional. Y dice cuál es su límite: por ejemplo, que los datos de una encuesta de ejemplo no representan a todas las personas.",
  ],
  vocab=[("conducta de protección", "acción que te cuida de un riesgo"), ("espacio libre de humo", "lugar donde no se puede fumar"), ("tratamiento", "ayuda profesional para recuperar la salud"), ("mensaje", "información que se entrega a otras personas"), ("límite", "lo que un dato o un mensaje no puede afirmar")],
  worked=[
      ("Armar el mensaje", "Datos: el alcohol enlentece el sistema nervioso. Escribe el efecto y una conducta de protección.", ["Efecto: baja la coordinación y los reflejos.", "Protección: decir no y contarlo a un adulto.", "Uno ambos."], "El alcohol baja la coordinación y los reflejos; si te ofrecen, di no y cuéntaselo a un adulto de confianza"),
      ("Identificar la protección", "¿Cuál es una conducta de protección? A) Informarme en una fuente de salud. B) Probar para saber cómo es.", ["Busco la acción que me cuida.", "A busca información confiable.", "B me expone al riesgo."], "A"),
  ],
  mistakes=[
      ("Hacer un mensaje que solo asusta, sin decir qué hacer.", "No ayuda a protegerse.", "Agrega una conducta de protección concreta."),
      ("Juzgar a las personas con dependencia.", "La dependencia es una condición de salud que se trata con ayuda.", "Usa un lenguaje respetuoso."),
  ],
  rec=[
      ("¿Un mensaje de salud necesita un dato: Sí o No?", "Sí", "El dato lo apoya."),
      ("Informarse en una fuente de salud, ¿es una conducta de protección: Sí o No?", "Sí", "Ayuda a decidir bien."),
      ("La dependencia, ¿se puede tratar con ayuda profesional: Sí o No?", "Sí", "Existe tratamiento profesional."),
  ],
  und=[
      ("¿Cuántas partes tiene un buen mensaje de salud?", "4", "Dato, efecto, protección y límite."),
      ("¿Qué es una conducta colectiva de protección? A) Un espacio libre de humo. B) Guardar un secreto.", "A", "Beneficia a todo el grupo."),
      ("¿Por qué un mensaje debe tener un límite?", "Porque los datos no representan a todos", "Evita afirmar de más."),
  ],
  app=[
      arith("Un afiche de ejemplo dice: «Cada cajetilla cuesta $6.000 (precio de ejemplo)». Si una persona compra una por semana durante 4 semanas, ¿cuánto gasta?", "6000*4", "Se multiplica el precio por las semanas."),
      ("Un mensaje tiene: dato, efecto y protección, pero no tiene límite. ¿Cuántas de las 4 partes tiene?", "3", "Le falta una."),
      ("Clasifica «hacer talleres de deporte en el colegio para todo el curso»: ¿protección personal o colectiva?", "Colectiva", "Es una actividad que beneficia al grupo."),
  ],
  rea=[
      ("Un afiche dice «Fumar es horrible, no lo hagas». ¿Qué parte le falta de las cuatro? A) Dato. B) Color.", "A", "No entrega un dato."),
      ("Alguien dice que las personas con dependencia son «débiles». ¿Qué afirmación es correcta? A) La dependencia es una condición de salud que se puede tratar. B) La dependencia es falta de voluntad.", "A", "No es debilidad sino una condición de salud."),
  ],
  cha=[
      ("Una persona gasta $5.000 a la semana en cajetillas (precio de ejemplo). ¿Cuánto gasta en 12 semanas?", "60.000", "5.000 × 12 = 60.000."),
      ("Marca el mensaje mejor. A) «El alcohol baja los reflejos. Si te ofrecen, di no y cuéntalo a un adulto». B) «El alcohol es horrible».", "A", "La A tiene efecto y conducta."),
  ],
  context=[("Dato de ejemplo. Un curso hizo 15 afiches y cada uno incluía 4 partes. ¿Cuántas partes escribieron en total?", "60", "15 × 4 = 60.")],
  selfcheck=[("¿Cuáles son las cuatro partes de un mensaje?", "Dato, efecto, conducta de protección y límite", "Son cuatro preguntas distintas."), ("¿Qué es una conducta de protección?", "Una acción que te cuida de un riesgo", "Por ejemplo, decir no."), ("¿Por qué no se debe juzgar a quien tiene dependencia?", "Porque es una condición de salud que se puede tratar", "Necesita ayuda y respeto.")],
  open_task=task("Escribe un mensaje de 4 líneas para un afiche sobre el alcohol con estas partes: un dato (el alcohol enlentece el sistema nervioso), un efecto (reflejos y coordinación), una conducta de protección y un límite. Puedes dibujar el afiche.", "Dato: el alcohol enlentece el sistema nervioso. Efecto: bajan los reflejos y la coordinación. Protección: si te ofrecen, di no y cuéntalo a un adulto de confianza. Límite: los efectos varían de persona a persona.", ["cuatro partes presentes", "lenguaje respetuoso", "conducta concreta"], ["afiche o texto"], ["solo asustar", "olvidar el límite"], "Pregunta quién debería leer el afiche y por qué."),
  reinforce="Escribe una conducta de protección personal y una colectiva.",
  extend="Explica por qué un buen mensaje de salud no debe exagerar.")

# ---------------------------------------------------------------- OA 08
L(OA8, 1,
  materials="Este cuaderno y lápiz. Opcional: dos hielos pequeños de un congelador de casa y un día soleado para observar. Los datos están escritos en los ejercicios.",
  use="Aprenderé que la energía produce cambios y a separar lo observado de lo supuesto. Sirve para explicar por qué los objetos se mueven, se calientan o crecen.",
  prior=["Sé que el Sol da luz y calor.", "Sé que una observación es lo que se mide o se cuenta."],
  explain=[
      "La energía es lo que permite que los objetos cambien o que algo ocurra: moverse, calentarse, iluminarse o hacer sonido. Existen varias formas de energía. La luminosa es la de la luz, la térmica es la del calor, la cinética es la del movimiento, la eléctrica es la de las pilas y los enchufes, y la química es la que está guardada en los alimentos y los combustibles. Una forma de energía puede pasar a otra.",
      "Los seres vivos también necesitan energía para realizar sus procesos vitales, como crecer, moverse, respirar y mantener la temperatura. La obtienen del alimento. Las plantas, además, captan la energía del Sol para fabricar su alimento por medio de la fotosíntesis. Por eso casi toda la energía de los seres vivos viene, en último término, del Sol.",
      "Al observar un fenómeno de energía, una observación es «el hielo al sol se derritió en 12 minutos y en la sombra en 30». Una interpretación es «el Sol es muy poderoso». Solo la primera se midió. Con varias observaciones se puede interpretar, pero la interpretación debe apoyarse en datos.",
  ],
  vocab=[("energía", "lo que permite que algo cambie o se mueva"), ("energía térmica", "energía del calor"), ("energía cinética", "energía del movimiento"), ("proceso vital", "función que realiza un ser vivo, como crecer o respirar"), ("energía química", "energía guardada en alimentos y combustibles")],
  worked=[
      ("Identificar la forma de energía", "Un niño corre. ¿Qué energía tiene su movimiento y de dónde la obtuvo?", ["El movimiento es energía cinética.", "La obtuvo de los alimentos que comió.", "Los alimentos guardan energía química."], "Energía cinética; viene de la energía química del alimento"),
      ("Observación o interpretación", "Dos frases: (1) «El hielo al sol se derritió en 18 minutos». (2) «El Sol es muy poderoso». ¿Cuál es la observación?", ["Pregunto cuál se midió.", "La frase 1 tiene un tiempo.", "La frase 2 es una idea."], "La frase 1"),
  ],
  mistakes=[
      ("Pensar que la energía es algo que se ve, como un objeto.", "La energía se reconoce por los cambios que produce.", "Describe qué cambia, no «ver» la energía."),
      ("Decir que los alimentos no tienen energía.", "Los alimentos guardan energía química que usamos para vivir.", "Relaciona el alimento con los procesos vitales."),
  ],
  rec=[
      ("¿La energía permite que algo cambie o que nada cambie?", "Que algo cambie", "Es lo que produce cambios."),
      ("La energía del movimiento se llama energía ______. Completa con «cinética» o «sonora».", "Cinética", "Es la energía del movimiento."),
      ("¿De dónde obtienen la energía los seres vivos que se mueven: de los alimentos o de las piedras?", "De los alimentos", "Los alimentos tienen energía química."),
  ],
  und=[
      ("¿Cuál es una interpretación? A) El hielo al sol se derritió en 12 minutos. B) El Sol es muy poderoso.", "B", "No es una medición."),
      ("¿Qué hacen las plantas con la energía del Sol?", "La usan en la fotosíntesis para fabricar su alimento", "Así guardan energía en el azúcar."),
      ("Crecer, respirar y moverse son ejemplos de ______. Elige procesos vitales o juegos.", "Procesos vitales", "Son funciones de los seres vivos."),
  ],
  app=[
      arith("El hielo al sol se derritió en 12 minutos y en la sombra en 30. ¿Cuántos minutos más tardó en la sombra?", "30-12", "Se restan los tiempos."),
      arith("Un ciclista de ejemplo pedalea 45 minutos por día durante 6 días. ¿Cuántos minutos pedalea en total?", "45*6", "Se multiplican los minutos por los días."),
      ("De estas cosas, ¿cuántas necesitan energía para cambiar: un auto que avanza, una piedra quieta, un hielo que se derrite, una planta que crece?", "3", "Cambian el auto, el hielo y la planta."),
  ],
  rea=[
      ("Una niña dice: «El hielo se derritió porque el Sol lo asustó». ¿Qué parte es una interpretación sin dato?", "Que el Sol lo asustó", "Los sentimientos no se miden."),
      ("Un compañero dice que sin energía los seres vivos podrían crecer igual. ¿Es correcto? Responde Sí o No.", "No", "Crecer es un proceso vital que necesita energía."),
  ],
  cha=[
      ("Un hielo de ejemplo se derrite en 12 minutos al sol y en 30 en la sombra. ¿En qué lugar recibe más energía térmica?", "Al sol", "Se derritió más rápido."),
      ("¿Cuál es una observación con números? A) El hielo al sol se derritió en 12 minutos y en la sombra en 30. B) El Sol es más fuerte que la sombra.", "A", "Contiene datos medidos."),
  ],
  context=[("Dato de ejemplo. Una persona usa 2.000 unidades de energía al día de sus alimentos y gasta 1.800 en sus actividades. ¿Cuántas unidades le sobran?", "200", "2.000 − 1.800 = 200.")],
  selfcheck=[("¿Qué es la energía?", "Lo que permite que algo cambie o se mueva", "Se reconoce por sus efectos."), ("¿De dónde obtienen la energía los seres vivos?", "De los alimentos", "Guardan energía química."), ("¿Cómo se reconoce una interpretación?", "No se mide ni se cuenta", "Se debe contrastar con datos.")],
  open_task=task("Con una persona de tu casa o con estos datos de ejemplo, observa un hielo al sol y otro en la sombra: al sol 14 minutos, en la sombra 33 minutos. Escribe tres observaciones con números, una interpretación y dos ejemplos de cosas que cambian gracias a la energía.", "Observaciones: al sol 14 min; en sombra 33 min; la diferencia es 19 min. Interpretación: el Sol aporta más energía térmica. Cambios: una planta crece, un auto avanza.", ["tres observaciones con números", "una interpretación rotulada", "dos ejemplos de cambios"], ["lista escrita"], ["mezclar interpretación con dato", "olvidar la diferencia"], "Pregunta qué otra condición podría influir en el tiempo en que se derrite el hielo."),
  reinforce="Escribe tres cosas que cambian gracias a la energía.",
  extend="Explica por qué casi toda la energía de los seres vivos viene del Sol.")

L(OA8, 2,
  materials="Este cuaderno y lápiz. Los datos están escritos en los ejercicios.",
  use="Aprenderé a formular preguntas y predicciones sobre el papel del Sol como fuente de energía. Sirve para anticipar qué pasaría si falta o cambia la energía solar.",
  prior=["Sé que la energía produce cambios.", "Sé que las plantas usan la luz del Sol en la fotosíntesis."],
  explain=[
      "Una pregunta de energía se puede comprobar con mediciones. Por ejemplo: «¿Cuántos grados sube la temperatura del agua de una botella oscura tras una hora al sol?». Se responde con un termómetro. Una pregunta como «¿Es bonito el Sol?» no se comprueba porque depende de gustos.",
      "Una predicción dice lo que se espera y su razón. Por ejemplo: «Si una planta se deja sin luz, crecerá menos, porque no puede hacer fotosíntesis». O: «Una botella pintada de negro se calentará más al sol, porque los colores oscuros absorben más luz». Con el Sol como fuente principal de energía se pueden predecir efectos en los alimentos, el clima y el viento.",
      "Para comprobar una predicción se miden datos y se comparan con lo esperado. Si no coinciden, se revisa la idea. Una predicción prudente usa «probablemente» y reconoce que otros factores, como el viento o las nubes, también influyen.",
  ],
  vocab=[("termómetro", "instrumento que mide la temperatura"), ("grado Celsius", "unidad para medir temperatura, se escribe °C"), ("absorber", "tomar para sí la energía que llega"), ("fuente de energía", "origen de la energía que se usa"), ("clima", "estado habitual de la atmósfera en un lugar")],
  worked=[
      ("Pregunta comprobable", "¿Cuál se puede comprobar? A) ¿Cuántos °C sube el agua de una botella al sol en 1 hora? B) ¿Es bonita la mañana?", ["Busco un dato que se mida.", "En A se mide la temperatura.", "En B es una opinión."], "A"),
      ("Predecir con razón", "Una planta no recibe luz del Sol. ¿Qué predices sobre su crecimiento y por qué?", ["Sin luz no hay fotosíntesis.", "Sin fotosíntesis hay menos alimento.", "Escribo la predicción con su razón."], "Crecerá menos, porque no puede hacer fotosíntesis"),
  ],
  mistakes=[
      ("Predecir sin razón: «se calentará más porque sí».", "Sin razón no se puede comprobar.", "Agrega «porque» y usa lo que sabes."),
      ("Olvidar otros factores, como el viento o las nubes.", "También influyen en la temperatura.", "Usa «probablemente» y nómbralos."),
  ],
  rec=[
      ("¿Con qué instrumento se mide la temperatura: con una regla o con un termómetro?", "Con un termómetro", "Mide en grados Celsius."),
      ("¿Los colores oscuros absorben más o menos luz?", "Más", "Se calientan más al sol."),
      ("¿Una predicción lleva una razón: Sí o No?", "Sí", "Dice por qué se espera el resultado."),
  ],
  und=[
      ("¿Cuál es una predicción con razón? A) La botella negra se calentará más, porque absorbe más luz. B) La botella negra se calentará más.", "A", "La A da el motivo."),
      ("¿Qué mide un termómetro?", "La temperatura", "Se expresa en °C."),
      ("¿Por qué conviene usar «probablemente»?", "Porque influyen otros factores", "Evita afirmar demasiado."),
  ],
  app=[
      arith("El agua de una botella estaba a 18 °C y después de una hora al sol está a 34 °C. ¿Cuántos grados subió?", "34-18", "Se resta la temperatura inicial de la final."),
      arith("Otra botella subió 4 °C cada 15 minutos durante una hora. ¿Cuántos grados subió en total?", "4*4", "Una hora tiene cuatro períodos de 15 minutos."),
      ("Predice: una botella blanca y una negra, al sol, durante una hora. ¿Cuál se calentará más probablemente?", "La negra", "El color oscuro absorbe más luz."),
  ],
  rea=[
      ("Una niña predice: «El agua en la sombra subirá más que al sol». ¿Es compatible con lo que se sabe? Responde Sí o No.", "No", "El Sol aporta energía térmica."),
      ("Un compañero mide una botella al sol y otra en la sombra, pero una es chica y la otra grande. ¿Qué problema tiene la comparación?", "Cambian el tamaño y el lugar a la vez", "No se sabe cuál cambio causó la diferencia."),
  ],
  cha=[
      ("Datos de ejemplo: botella blanca, 20 → 28 °C; botella negra, 20 → 36 °C. ¿Cuántos grados más subió la negra?", "8", "16 − 8 = 8."),
      ("Marca la mejor pregunta comprobable. A) ¿Cuántos °C sube el agua de una botella negra tras 1 hora al sol? B) ¿Es lindo el color negro?", "A", "Se mide con un termómetro."),
  ],
  context=[("Dato de ejemplo. En un patio, la temperatura del suelo al sol fue 38 °C y en la sombra 26 °C. ¿Cuántos grados más hubo al sol?", "12", "38 − 26 = 12.")],
  selfcheck=[("¿Qué debe tener una predicción?", "Lo que ocurrirá y su razón", "Así se puede comprobar."), ("¿En qué unidad se expresa la temperatura que mide un termómetro?", "En grados Celsius", "Se escribe °C."), ("¿Por qué los colores oscuros se calientan más?", "Porque absorben más luz", "Reciben más energía.")],
  open_task=task("Escribe una pregunta comprobable y una predicción con razón sobre dos botellas, una pintada de negro y otra de blanco, con agua a 20 °C, una hora al sol. Luego completa con estos datos de ejemplo: negra 35 °C y blanca 29 °C, y calcula cuántos grados más subió la negra.", "Pregunta: ¿cuántos grados sube cada botella en una hora? Predicción: la negra subirá más, porque absorbe más luz. Cálculo: sube 15 y 9; la negra subió 6 °C más.", ["pregunta con algo medible", "predicción con razón", "cálculo correcto"], ["tres frases escritas"], ["predecir sin razón", "no usar números"], "Pregunta qué otra condición podría cambiar el resultado."),
  reinforce="Escribe una pregunta comprobable sobre la temperatura del agua al sol.",
  extend="Explica por qué la energía del Sol influye en el clima.")

L(OA8, 3,
  materials="Este cuaderno, lápiz y lápices de colores.",
  use="Aprenderé a modelar cómo la energía del Sol llega a los alimentos, los combustibles y el viento. Sirve para explicar que la mayoría de los recursos energéticos vienen directa o indirectamente del Sol.",
  prior=["Sé que el Sol da luz y calor.", "Sé que las plantas hacen fotosíntesis."],
  explain=[
      "La energía solar llega a la Tierra como luz y calor. Se puede usar de forma directa, por ejemplo con paneles solares que producen electricidad o calentadores solares que calientan agua. También se usa de forma indirecta. Las plantas guardan la energía del Sol en sus azúcares. Quien come plantas o animales recibe esa energía. La leña y el carbón vegetal también vienen de plantas. El petróleo, el gas natural y el carbón mineral se formaron hace millones de años a partir de restos de seres vivos que habían captado energía solar.",
      "El Sol también calienta el aire y el agua de manera desigual. Las diferencias de calor mueven el aire y producen el viento, que mueve aerogeneradores. El calor evapora el agua y, al llover, el agua cae en las montañas y llena los ríos y embalses. Esa agua que cae mueve las turbinas de las centrales hidroeléctricas. Por eso el viento y el agua de los ríos también son formas indirectas de energía solar.",
      "No todas las fuentes vienen del Sol. La geotérmica viene del calor del interior de la Tierra y la de las mareas viene sobre todo de la atracción de la Luna. Un esquema de flechas muestra estos recorridos, pero no indica cuánta energía hay en cada paso ni cuánto tarda en formarse un combustible. Esos son límites del modelo.",
  ],
  vocab=[("energía solar", "energía que llega del Sol como luz y calor"), ("panel solar", "dispositivo que transforma la luz del Sol en electricidad"), ("combustible fósil", "combustible formado hace millones de años de restos de seres vivos"), ("aerogenerador", "máquina que usa el viento para producir electricidad"), ("hidroeléctrica", "central que usa agua en movimiento para producir electricidad")],
  worked=[
      ("Seguir la energía del Sol", "Arma el camino: Sol → pasto → vaca → persona. ¿Qué forma de energía guarda el pasto?", ["El pasto capta la luz del Sol.", "Guarda esa energía en azúcares.", "Es energía química."], "Energía química guardada en el pasto"),
      ("Directa o indirecta", "El Sol calienta una pared y esa pared calienta una persona. ¿Es uso directo o indirecto?", ["La energía llega del Sol sin pasar por otro recurso.", "No pasó por plantas ni viento.", "Es directa."], "Directa"),
  ],
  mistakes=[
      ("Pensar que el petróleo no tiene relación con el Sol.", "Se formó de restos de seres vivos que captaron energía solar.", "Sigue la energía hacia atrás hasta el Sol."),
      ("Creer que todas las fuentes vienen del Sol.", "La geotérmica viene del interior de la Tierra y las mareas de la Luna.", "Revisa el origen de cada fuente."),
  ],
  rec=[
      ("¿El viento se produce por diferencias de calor causadas por el Sol: Sí o No?", "Sí", "El Sol calienta el aire de forma desigual."),
      ("¿El carbón vegetal viene de plantas: Sí o No?", "Sí", "Las plantas captaron la energía del Sol."),
      ("¿La energía geotérmica viene del Sol o del interior de la Tierra?", "Del interior de la Tierra", "Es calor de la propia Tierra."),
  ],
  und=[
      ("¿Qué uso es directo? A) Un panel solar que da electricidad. B) Leña que se quema.", "A", "El panel usa la luz del Sol sin intermediarios."),
      ("¿Por qué el petróleo es una forma indirecta de energía solar?", "Se formó de restos de seres vivos que captaron energía del Sol", "El camino pasó por seres vivos."),
      ("¿Qué mueve las turbinas de una hidroeléctrica: el viento o el agua en movimiento?", "El agua en movimiento", "El agua cae o fluye."),
  ],
  app=[
      ("Ordena el camino de la energía: persona, pasto, Sol, vaca.", "Sol, pasto, vaca, persona", "Cada ser recibe energía del anterior."),
      arith("Un panel solar de ejemplo produce 3 unidades de energía por hora. ¿Cuántas produce en 8 horas de sol?", "3*8", "Se multiplica por las horas."),
      ("De estas fuentes, ¿cuántas vienen del Sol directa o indirectamente: solar, viento, leña, petróleo, geotérmica?", "4", "La geotérmica viene del interior de la Tierra."),
  ],
  rea=[
      ("Una compañera dice que la electricidad de un aerogenerador no tiene relación con el Sol. ¿Es correcta? Responde Sí o No y explica.", "No; el viento se forma por diferencias de calor del Sol", "Es energía solar indirecta."),
      ("Un modelo Sol → pasto → vaca no muestra cuánta energía se pierde en cada paso. ¿Eso es un límite del modelo? Responde Sí o No.", "Sí", "Un límite es algo que el modelo no representa."),
  ],
  cha=[
      ("Ordena el camino indirecto de la energía hasta un auto a bencina: auto, petróleo, seres vivos antiguos, Sol, bencina.", "Sol, seres vivos antiguos, petróleo, bencina, auto", "Se sigue el origen del combustible."),
      ("Datos de ejemplo: una central eólica produce 12 unidades por hora. ¿Cuántas produce en 5 horas con viento constante?", "60", "12 × 5 = 60."),
  ],
  context=[("Dato de ejemplo. Un hogar tiene paneles que producen 20 unidades al día y consume 28. ¿Cuántas unidades le faltan?", "8", "28 − 20 = 8.")],
  selfcheck=[("¿Qué es un uso directo de la energía solar?", "Usar la luz o el calor del Sol sin otro recurso", "Por ejemplo, un panel solar."), ("¿Qué fuentes son indirectas?", "Alimentos, leña, combustibles fósiles, viento y agua en movimiento", "Pasaron por seres vivos o por el aire y el agua."), ("¿Qué fuentes no vienen del Sol?", "La geotérmica y las mareas", "Vienen del interior de la Tierra y de la Luna.")],
  open_task=task("Dibuja dos caminos de la energía con flechas: uno desde el Sol hasta una persona que come pan y otro desde el Sol hasta un aerogenerador. Escribe debajo cuál es indirecto y por qué, y un límite de tus dibujos.", "Sol → trigo → pan → persona. Sol → aire calentado → viento → aerogenerador. Ambos son indirectos. Límite: no muestran cuánta energía hay en cada paso.", ["dos caminos con flechas", "explica lo indirecto", "un límite"], ["dibujo con flechas", "frases"], ["flechas al revés", "no nombrar el Sol"], "Pregunta por qué el pan es una forma indirecta de energía solar."),
  reinforce="Escribe el camino de la energía desde el Sol hasta una persona que come arroz.",
  extend="Explica por qué la leña se considera energía solar indirecta.")

L(OA8, 4,
  materials="Este cuaderno y lápiz. La lista de fuentes está escrita en los ejercicios.",
  use="Aprenderé a comparar fuentes de energía con un criterio: si dependen del Sol de forma directa, indirecta o no dependen. Sirve para clasificar recursos y explicar su origen.",
  prior=["Sé que el Sol es la principal fuente de energía.", "Sé seguir caminos de energía con flechas."],
  explain=[
      "Para clasificar las fuentes de energía se usa un criterio: ¿de dónde viene la energía? Si viene del Sol directamente, como la luz y el calor, la fuente es solar directa. Si viene del Sol pero pasó por otro proceso, como el viento, el agua de los ríos, la leña, los alimentos y los combustibles fósiles, la fuente es solar indirecta. Si no viene del Sol, como el calor del interior de la Tierra, es de otro origen.",
      "Una tabla permite ordenar las fuentes. Por ejemplo, de estas siete: solar, viento, hidroeléctrica, leña, petróleo, geotérmica y mareas, cinco son solares (una directa y cuatro indirectas) y dos tienen otro origen. Esta clasificación es una de varias posibles; también se pueden clasificar según sean renovables o no.",
      "Comparar con un criterio no es decir qué fuente es mejor. Es decidir con una regla clara. Un límite de este criterio es que no dice cuánta energía entrega cada fuente ni cuánto daña el ambiente. Esas son otras preguntas que se verán con otros criterios.",
  ],
  vocab=[("clasificar", "ordenar según un criterio"), ("origen", "lugar o proceso de donde viene algo"), ("solar directa", "energía usada directamente del Sol"), ("solar indirecta", "energía que viene del Sol después de pasar por otros procesos"), ("geotérmica", "energía del calor del interior de la Tierra")],
  worked=[
      ("Clasificar con el criterio", "Clasifica: panel solar, viento, geotérmica. ¿Cuál es directa, cuál indirecta y cuál de otro origen?", ["El panel usa la luz del Sol: directa.", "El viento viene del calentamiento desigual del aire: indirecta.", "La geotérmica viene del interior de la Tierra: otro origen."], "Panel: directa. Viento: indirecta. Geotérmica: otro origen"),
      ("Contar por grupo", "De 7 fuentes, 1 es directa, 4 son indirectas y el resto son de otro origen. ¿Cuántas son de otro origen?", ["Suma las del Sol: 1 + 4.", "Resto 7 − 5.", "Queda el resultado."], "2 fuentes"),
  ],
  mistakes=[
      ("Clasificar la leña como «de otro origen».", "Viene de plantas que captaron energía del Sol.", "Sigue el origen hasta el Sol."),
      ("Pensar que clasificar es decir cuál fuente es mejor.", "El criterio solo indica el origen.", "Usa otro criterio para decidir cuál conviene."),
  ],
  rec=[
      ("¿El petróleo es solar indirecta: Sí o No?", "Sí", "Viene de restos de seres vivos."),
      ("¿La geotérmica viene del Sol: Sí o No?", "No", "Viene del interior de la Tierra."),
      ("¿El panel solar usa la energía del Sol de forma directa o indirecta?", "Directa", "Usa luz del Sol."),
  ],
  und=[
      ("¿Cuál fuente es solar indirecta? A) Leña. B) Mareas.", "A", "La leña viene de plantas; las mareas, de la Luna."),
      ("¿Qué criterio se usó para clasificar?", "El origen de la energía", "Si viene del Sol o no."),
      ("¿Por qué clasificar no dice cuál fuente es mejor?", "Porque el criterio solo indica el origen", "Hay otros criterios para decidir."),
  ],
  app=[
      arith("De 10 fuentes, 2 son directas y 6 son indirectas. ¿Cuántas son de otro origen?", "10-2-6", "Se restan las del Sol del total."),
      ("Cuenta cuántas son solares directas o indirectas: solar, hidroeléctrica, geotérmica, leña, mareas.", "3", "Son solar, hidroeléctrica y leña."),
      ("Clasifica con una letra: A) Solar directa. B) Solar indirecta. C) Otro origen. ¿Qué letra tiene el viento?", "B", "Viene del calentamiento desigual del aire."),
  ],
  rea=[
      ("Una compañera clasifica las mareas como solares. ¿Qué error tiene? Responde con una frase.", "Las mareas vienen sobre todo de la Luna", "Su causa principal no es el Sol."),
      ("Alguien dice que la leña y el petróleo se clasifican distinto porque uno es de plantas y otro de restos antiguos. ¿Se clasifican distinto con el criterio de origen? Responde Sí o No.", "No", "Ambos son solares indirectos."),
  ],
  cha=[
      ("Una tabla de ejemplo tiene 12 fuentes: 3 directas, 5 indirectas y las demás de otro origen. ¿Cuántas más son solares que de otro origen?", "4", "Solares: 8, otro origen: 4; 8 − 4 = 4."),
      ("Marca el criterio que permitiría decir cuál fuente produce más energía. A) El origen de la energía. B) La cantidad de energía que entrega cada fuente.", "B", "El origen no mide cantidades."),
  ],
  context=[("Dato de ejemplo. En un listado hay 18 fuentes de energía: 11 son solares directas o indirectas. ¿Cuántas son de otro origen?", "7", "18 − 11 = 7.")],
  selfcheck=[("¿Qué criterio se usó?", "El origen de la energía", "Si viene del Sol directa o indirectamente."), ("¿Cuáles fuentes no vienen del Sol?", "La geotérmica y las mareas", "Tienen otro origen."), ("¿Qué límite tiene el criterio?", "No dice cuánta energía entrega ni cuánto daña el ambiente", "Es solo de origen.")],
  open_task=task("Clasifica estas ocho fuentes en una tabla de tres columnas (solar directa, solar indirecta, otro origen): panel solar, viento, hidroeléctrica, leña, petróleo, geotérmica, mareas, calentador solar de agua. Cuenta cuántas hay en cada columna y escribe un límite del criterio.", "Directa: panel solar, calentador solar (2). Indirecta: viento, hidroeléctrica, leña, petróleo (4). Otro origen: geotérmica, mareas (2). Límite: no dice cuánta energía entrega cada fuente.", ["clasifica las ocho fuentes", "cuenta cada columna", "escribe un límite"], ["tabla de tres columnas"], ["clasificar la leña como otro origen", "olvidar el límite"], "Pregunta qué otro criterio usaría para decidir qué fuente conviene."),
  reinforce="Clasifica tres fuentes de energía según su origen.",
  extend="Explica por qué una fuente puede ser solar y también tener impactos en el ambiente.")
