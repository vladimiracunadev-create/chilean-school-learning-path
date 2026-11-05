"""Cuaderno del estudiante, 2.º medio Ciencias Naturales: OA 03 (sexualidad humana), OA 04 (fecundación y desarrollo prenatal) y OA 05 (regulación de la fertilidad)."""
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


OA3 = "CN2M OA 03"
OA4 = "CN2M OA 04"
OA5 = "CN2M OA 05"

MAT = "Este cuaderno y lápiz. Todos los casos y datos están escritos aquí; todos son ficticios y no necesitas contar nada personal."
ADULTO = "Si algo de este tema te preocupa o te incomoda, puedes conversarlo con una persona adulta de confianza o con un profesional de salud."

# ---------------------------------------------------------------- OA 03

L(OA3, 1,
  materials=MAT,
  use="Aprenderé qué abarca la sexualidad humana y cómo formular una pregunta que se pueda investigar sobre ella. Sirve para distinguir lo que se puede comprobar con datos de lo que es una opinión. " + ADULTO,
  prior=["Sé que el cuerpo cambia en la pubertad por acción de las hormonas.", "Sé que una pregunta investigable indica qué se mide y qué se compara."],
  explain=[
      "La sexualidad es parte de la vida de todas las personas durante toda su vida; no es lo mismo que tener relaciones sexuales. Tiene cuatro dimensiones que se influyen entre sí: la biológica (cuerpo, hormonas y reproducción), la afectiva (sentimientos y vínculos con otras personas), la social (familia, normas, medios de comunicación y cultura) y la psicológica (identidad, autoestima y toma de decisiones).",
      "La reproducción es una función biológica y es solo una parte de la sexualidad. La responsabilidad individual significa cuidar de sí mismo y de las demás personas: informarse en fuentes confiables, respetar los límites ajenos y los propios, y pedir ayuda a una persona adulta de confianza cuando algo preocupa. El consentimiento es un acuerdo libre, informado y que se puede retirar en cualquier momento; el silencio no es un sí.",
      "Un porcentaje es la parte de cada 100: se calcula dividiendo la parte en el total y multiplicando por 100. Una pregunta investigable nombra algo que se puede medir y qué se compara, y no depende de una opinión. «¿Cuántos estudiantes de un curso de ejemplo nombran correctamente las cuatro dimensiones antes y después de una clase?» se puede investigar contando. «¿Es malo que los jóvenes hablen poco del tema?» no, porque «malo» es un juicio y no indica qué medir.",
  ],
  vocab=[("dimensión", "aspecto de un tema que se puede estudiar por separado"), ("consentimiento", "acuerdo libre, informado y retirable en cualquier momento"), ("responsabilidad individual", "cuidarse y cuidar a las demás personas"), ("fuente confiable", "origen de información que se puede verificar, como un profesional de salud")],
  worked=[
      ("Ubicar una situación en su dimensión", "Un estudiante ficticio dice: «Me da vergüenza hablar de esto porque en mi grupo se burlan». ¿Qué dimensión destaca más?", ["La vergüenza se debe a lo que hace o dice el grupo.", "Las normas y reacciones del grupo pertenecen a la dimensión social."], "Dimensión social"),
      ("Mejorar una pregunta", "Mejora «¿Es injusto que en clase se hable poco de sexualidad?» para que se pueda investigar.", ["Quito la palabra de juicio: «injusto».", "Indico qué cuento: cuántas de las 12 clases de ejemplo de un semestre incluyen el tema.", "Indico qué comparo: dos cursos ficticios, el 2.º A y el 2.º B."], "«¿Cuántas de las 12 clases del semestre incluyen el tema en el 2.º A y cuántas en el 2.º B?»"),
  ],
  mistakes=[
      ("Decir que sexualidad es lo mismo que tener relaciones sexuales.", "Incluye también afectos, identidad, cultura y cuidado del cuerpo, desde el nacimiento.", "Piensa en las cuatro dimensiones antes de responder."),
      ("Interpretar el silencio como consentimiento.", "El consentimiento debe ser claro, libre y puede retirarse.", "Si no hay un sí claro, no hay consentimiento."),
  ],
  rec=[
      ("¿Cuáles son las cuatro dimensiones de la sexualidad que estudiamos?", "Biológica, afectiva, social y psicológica", "Son las cuatro que nombra la explicación."),
      ("Verdadero o falso: la sexualidad humana es lo mismo que la reproducción.", "Falso", "La reproducción es solo una función biológica; la sexualidad es más amplia."),
      ("Las hormonas y el desarrollo del cuerpo pertenecen a la dimensión: A) Biológica; B) Social.", "A", "Son procesos del cuerpo."),
  ],
  und=[
      ("Una persona siente cariño y confianza hacia un amigo. ¿Qué dimensión destaca? A) Afectiva; B) Biológica.", "A", "Los sentimientos y los vínculos son lo afectivo."),
      ("Una persona dice «no sé» y se queda callada cuando le proponen algo. ¿Hay consentimiento? A) No, un silencio no es un sí claro; B) Sí, porque no dijo que no.", "A", "El consentimiento debe ser un acuerdo claro y libre."),
      ("Una serie muestra siempre los mismos roles para hombres y para mujeres. ¿Qué dimensión influye aquí? A) Social; B) Biológica.", "A", "Los medios y las normas culturales son parte de lo social."),
  ],
  app=[
      ("¿Cuál pregunta se puede investigar? A) ¿Cuántos de 30 estudiantes de ejemplo nombran una fuente confiable de información antes y después de una charla?; B) ¿Es feo hablar de sexualidad?", "A", "Indica qué contar y qué comparar; la otra es un juicio."),
      arith("En una encuesta de ejemplo, 30 de 50 estudiantes dicen que se informan primero en internet. ¿Qué porcentaje es?", "30*100//50", "Se divide la parte en el total y se multiplica por 100."),
      ("Una estudiante ficticia duda de su autoestima y de si puede decir que no. ¿Qué dimensión destaca? A) Psicológica; B) Social.", "A", "La autoestima y la toma de decisiones son psicológicas."),
  ],
  rea=[
      ("Un compañero dice: «La sexualidad es solo biológica porque se estudia en Ciencias». ¿Qué le respondes? A) También tiene dimensiones afectiva, social y psicológica; B) Tiene razón.", "A", "El tema incluye las cuatro dimensiones, aunque Ciencias estudie la biológica."),
      ("Una persona recibe un mensaje de alguien que insiste en que envíe una foto íntima. ¿Qué es lo más seguro? A) No enviarla, bloquear, guardar el mensaje como evidencia y contarlo a una persona adulta de confianza; B) Enviarla para evitar el conflicto.", "A", "Proteger la privacidad y avisar a una persona adulta es lo recomendable."),
  ],
  cha=[
      ("¿Qué dato permitiría comparar dos fuentes de información sobre sexualidad? A) Cuántas de 10 afirmaciones de ejemplo son correctas en cada fuente; B) Cuál fuente es más conocida.", "A", "Un conteo de afirmaciones correctas permite comparar con evidencia."),
      ("Un curso ficticio de 40 estudiantes responde un cuestionario: 26 contestan bien las preguntas sobre consentimiento. ¿Cuántos no contestaron bien?", "14", "Se resta 26 de 40.", "40-26"),
  ],
  context=[("En una charla ficticia se pide una pregunta para investigar en el liceo. ¿Cuál sirve mejor? A) ¿Cuántos estudiantes de 2.º medio saben a qué profesional de salud acudir?; B) ¿Por qué los adultos no hablan claro?", "A", "Indica qué contar y no depende de una opinión.")],
  selfcheck=[("¿Qué dimensión incluye la autoestima y la identidad?", "La psicológica", "Se refiere a cómo se ve y decide una persona."), ("¿Cómo se llama el acuerdo libre, informado y retirable?", "Consentimiento", "Es la definición de la clase."), ("¿Por qué «¿es malo…?» no es investigable?", "Porque es un juicio y no indica qué medir", "Una pregunta investigable nombra algo medible.")],
  open_task=task("Elige una de estas ideas y conviértela en una pregunta investigable que diga qué se mide y qué se compara: (1) cómo se informan los jóvenes; (2) cuánto se habla del tema en los medios; (3) cuánto se conoce de los servicios de salud. Escribe además a qué dimensión pertenece tu pregunta. No uses datos personales.", "«¿Cuántas de 10 afirmaciones de ejemplo sobre pubertad reconocen correctamente 20 estudiantes ficticios de dos cursos?» Dimensión: biológica.", ["nombra qué se mide", "indica qué se compara", "no contiene juicios", "indica una dimensión"], ["una pregunta escrita con su dimensión"], ["usar palabras como «bueno» o «malo»", "no decir qué medir"], "Pregunta qué dato recogerías primero."),
  reinforce="Escribe una situación ficticia para cada dimensión y nómbrala.",
  extend="Explica con tus palabras por qué la responsabilidad incluye cuidar a otras personas.")

L(OA3, 2,
  materials=MAT,
  use="Aprenderé a leer una tabla y un gráfico con datos de ejemplo sobre dónde se informan los jóvenes y a juzgar si la fuente es confiable. " + ADULTO,
  prior=["Sé que la sexualidad tiene cuatro dimensiones.", "Sé calcular un porcentaje con parte y total."],
  explain=[
      "Los datos de una encuesta se ordenan en una tabla con categorías y cantidades. Para comparar categorías conviene un gráfico de barras; para mostrar cómo se reparte un total, uno circular. Un porcentaje se calcula dividiendo la parte en el total y multiplicando por 100. Antes de sacar una conclusión, hay que revisar cuántas personas respondieron, porque una encuesta pequeña dice poco sobre todas las personas.",
      "No todas las fuentes de información valen lo mismo. Una fuente confiable indica quién la escribe, se puede verificar y la respaldan profesionales de salud o instituciones públicas. Una cuenta anónima o un mensaje que circula sin autor puede mezclar datos correctos con errores. Contrastar significa buscar la misma información en dos o más fuentes confiables.",
      "Un dato describe lo que ocurrió en un grupo; no dice por qué ocurrió ni lo que es correcto. Que muchas personas usen una fuente no la hace confiable. Los datos de esta clase son de ejemplo y no representan a ningún grupo real.",
  ],
  vocab=[("categoría", "grupo en que se clasifican los datos"), ("porcentaje", "parte de 100 que representa una cantidad"), ("fuente confiable", "origen de información verificable y con autor identificable"), ("contrastar", "comparar la misma información en varias fuentes")],
  worked=[
      ("Calcular un porcentaje", "En una encuesta de ejemplo de 80 estudiantes ficticios, 20 dicen que se informan con su familia. ¿Qué porcentaje es?", ["Parte: 20; total: 80.", "20 dividido en 80 es 0,25; multiplicado por 100 da 25."], "25 %"),
      ("Elegir el gráfico", "Quiero comparar cuántas personas eligieron cada una de 4 fuentes. ¿Qué gráfico uso?", ["Son categorías separadas que quiero comparar entre sí.", "El gráfico de barras permite comparar las alturas."], "Gráfico de barras"),
  ],
  mistakes=[
      ("Creer que una fuente es confiable porque muchas personas la usan.", "La popularidad no prueba que la información sea correcta.", "Revisa autor, respaldo y contraste con otras fuentes."),
      ("Sacar conclusiones de una encuesta con muy pocas respuestas.", "Un grupo pequeño no representa a todos.", "Indica siempre cuántas personas respondieron."),
  ],
  rec=[
      ("¿Qué tipo de gráfico sirve para comparar cantidades de categorías separadas?", "Gráfico de barras", "Las barras se comparan por su altura."),
      ("Verdadero o falso: una cuenta anónima que no cita fuentes es automáticamente confiable.", "Falso", "Sin autor ni respaldo no se puede verificar."),
      ("¿Cómo se llama comparar la misma información en varias fuentes?", "Contrastar", "Así se detectan errores."),
  ],
  und=[
      ("Tabla de ejemplo de 60 estudiantes ficticios: familia 24, profesionales de salud 18, internet y redes 12, amigos 6. ¿Qué fuente tiene más respuestas? A) La familia; B) Los amigos.", "A", "24 es la cantidad mayor de la tabla."),
      ("¿Cuál es una señal de fuente confiable? A) Indica autor y respaldo de profesionales de salud; B) Promete «el secreto que nadie te cuenta».", "A", "El autor y el respaldo permiten verificar."),
      ("Una encuesta ficticia a 5 personas muestra que 4 prefieren cierta fuente. ¿Qué limitación tiene? A) Son muy pocas respuestas para generalizar; B) Los porcentajes siempre son falsos.", "A", "Un grupo pequeño no representa a todos."),
  ],
  app=[
      arith("En la tabla de ejemplo de 60 estudiantes, 18 se informan con profesionales de salud. ¿Qué porcentaje es?", "18*100//60", "Se divide 18 en 60 y se multiplica por 100."),
      arith("En otra encuesta ficticia, 45 de 60 estudiantes dicen que han visto información dudosa en redes sociales. ¿Cuántos no la han visto?", "60-45", "Se resta la parte del total."),
      ("Quiero mostrar cómo se reparte el 100 % de las respuestas entre 4 fuentes. ¿Qué gráfico conviene más? A) Circular; B) De dispersión.", "A", "El gráfico circular muestra partes de un total."),
  ],
  rea=[
      ("Un gráfico de ejemplo muestra que 12 de 60 se informan en internet. Alguien concluye: «Internet es una fuente confiable». ¿Es válida la conclusión? A) No, el gráfico muestra cuántos la usan, no si es confiable; B) Sí, porque es un dato.", "A", "Usar una fuente no prueba que sea confiable."),
      ("Dos fuentes dan datos distintos sobre un mismo tema. ¿Qué haces primero? A) Revisar el autor y buscar una tercera fuente confiable; B) Quedarme con la que dice lo que me gusta.", "A", "Contrastar con fuentes verificables reduce errores."),
  ],
  cha=[
      arith("Curso 1 de ejemplo: 36 de 40 estudiantes identifican a qué profesional acudir; curso 2: 21 de 30. ¿Cuántos puntos de porcentaje (diferencia entre los dos porcentajes) tiene de ventaja el curso 1?", "36*100//40-21*100//30", "Curso 1: 90 %; curso 2: 70 %; se restan."),
      ("Una tabla ficticia suma 24 + 18 + 12 + 6 = 60 respuestas, pero se dice que se encuestó a 70 estudiantes. ¿Qué indica esta diferencia? A) Que 10 personas no respondieron o falta una categoría; B) Que la suma está mal calculada siempre.", "A", "Si el total no coincide, faltan datos o hay respuestas sin registrar."),
  ],
  context=[("Una profesora ficticia muestra un gráfico donde 'redes sociales' tiene la barra más alta. ¿Qué pregunta de seguimiento es la mejor? A) ¿Qué información de las redes se pudo verificar con profesionales de salud?; B) ¿Por qué esos estudiantes no leen libros?", "A", "Pregunta por la confiabilidad, que es lo que el gráfico no muestra.")],
  selfcheck=[("¿Cómo se calcula un porcentaje?", "Parte dividida en total por 100", "Es la definición de la clase."), ("¿Qué gráfico conviene para comparar categorías?", "El de barras", "Permite comparar alturas."), ("¿Qué debes revisar antes de confiar en una fuente?", "El autor y su respaldo", "Así se puede verificar.")],
  open_task=task("Con estos datos de ejemplo de 50 estudiantes ficticios: familia 20, profesionales de salud 15, internet 10, amigos 5, calcula el porcentaje de cada categoría, elige el gráfico adecuado y escribe una conclusión de dos oraciones que incluya una limitación.", "Familia 40 %, profesionales 30 %, internet 20 %, amigos 10 %. Gráfico de barras. «La familia es la fuente más nombrada. Son datos de ejemplo de 50 personas y no dicen si la información era correcta.»", ["calcula bien los porcentajes", "elige gráfico justificado", "incluye una limitación"], ["tabla de porcentajes y conclusión"], ["no declarar el número de respuestas", "tomar «más usada» como «más confiable»"], "Pregunta qué dato necesitarías para saber si la información era correcta."),
  reinforce="Calcula el porcentaje de una categoría de una tabla de 40 respuestas ficticias.",
  extend="Explica por qué una encuesta pequeña no permite generalizar.")

L(OA3, 3,
  materials=MAT,
  use="Aprenderé a usar el modelo de las cuatro dimensiones para analizar situaciones y a reconocer sus límites. " + ADULTO,
  prior=["Sé nombrar las cuatro dimensiones de la sexualidad.", "Sé que un modelo simplifica la realidad."],
  explain=[
      "Un modelo es una representación simplificada que ayuda a explicar algo. El modelo de las cuatro dimensiones se puede dibujar como cuatro círculos que se superponen: biológica, afectiva, social y psicológica. La zona donde se cruzan indica que las dimensiones se influyen. Por ejemplo, un cambio hormonal (biológico) puede modificar el ánimo (psicológico) y la relación con los amigos (social).",
      "Para usar el modelo, se lee una situación, se subrayan los datos y se asigna cada uno a una dimensión. Casi nunca interviene una sola: la mayoría de las situaciones reales mezclan varias. Usar el modelo permite ver aspectos que se olvidan, como las normas del grupo o los sentimientos.",
      "Todo modelo tiene límites. Este separa las dimensiones para estudiarlas, pero en la vida real están mezcladas y no se pueden medir por separado. Además, no dice qué decisión tomar: ayuda a pensar, y las decisiones requieren información, respeto, consentimiento y consulta a una persona adulta de confianza.",
  ],
  vocab=[("modelo", "representación simplificada que ayuda a explicar algo"), ("superponer", "poner una cosa sobre otra de modo que se cruzan"), ("influir", "producir efecto sobre otra cosa"), ("límite del modelo", "aspecto de la realidad que el modelo no muestra")],
  worked=[
      ("Analizar una situación con el modelo", "Un estudiante ficticio nota cambios en su voz (a), le da vergüenza que lo comenten (b) y se pregunta cómo quiere ser (c). Asigna a cada dato una dimensión.", ["Cambios en la voz: son del cuerpo, dimensión biológica.", "La vergüenza ante comentarios del grupo: dimensión social (y afectiva).", "Preguntarse cómo quiere ser: identidad, dimensión psicológica."], "(a) Biológica; (b) Social; (c) Psicológica"),
      ("Reconocer un límite", "¿Qué límite tiene dibujar las dimensiones como círculos separados?", ["Los círculos separados sugieren que no se mezclan.", "En la realidad las dimensiones se influyen entre sí."], "Muestra separadas dimensiones que en la realidad están conectadas"),
  ],
  mistakes=[
      ("Asignar una sola dimensión a toda situación.", "Las situaciones reales mezclan varias.", "Subraya cada dato y asigna una dimensión a cada uno."),
      ("Creer que el modelo dice qué decisión tomar.", "Solo ayuda a analizar; la decisión requiere información y consulta.", "Usa el modelo para pensar y consulta a una persona adulta de confianza."),
  ],
  rec=[
      ("¿Qué es un modelo en ciencias?", "Una representación simplificada que ayuda a explicar algo", "Es la definición de la clase."),
      ("Verdadero o falso: en una situación real casi siempre interviene una sola dimensión.", "Falso", "Las situaciones reales suelen mezclar varias."),
      ("Un cambio hormonal que altera el ánimo, ¿qué dos dimensiones conecta? A) Biológica y psicológica; B) Social y biológica solamente.", "A", "La hormona es biológica y el ánimo es psicológico."),
  ],
  und=[
      ("«Mi familia dice que no se habla de esto en la mesa». ¿Qué dimensión representa este dato? A) Social; B) Biológica.", "A", "Las normas de una familia son parte de lo social."),
      ("«Me siento tranquilo con mi amiga porque confío en ella». ¿Qué dimensión representa? A) Afectiva; B) Biológica.", "A", "Confiar y sentir tranquilidad son aspectos afectivos."),
      ("¿Qué muestra la zona en que se cruzan los círculos del modelo? A) Que las dimensiones se influyen entre sí; B) Que una dimensión no existe.", "A", "La superposición indica relación."),
  ],
  app=[
      ("Situación ficticia: una joven nota que su cuerpo cambia, extraña el cariño de sus amigas, siente la presión de las normas de su nuevo colegio y duda de sí misma. ¿Cuántas dimensiones distintas aparecen en total?", "4", "Cambio corporal (biológica), cariño (afectiva), normas del colegio (social) y duda de sí misma (psicológica)."),
      ("«Me preocupa mi autoestima porque comparo mi cuerpo con fotos de internet». ¿Qué dimensión social influye aquí? A) Los medios de comunicación; B) Las hormonas.", "A", "Las imágenes de los medios son parte de lo social."),
      ("En un curso de 36 estudiantes ficticios se encuesta qué dimensión les resulta más difícil de hablar: 9 dicen la afectiva. ¿Qué porcentaje es?", "25 %", "9 dividido en 36 es 0,25.", "9*100//36"),
  ],
  rea=[
      ("Alguien dice: «Si conozco las cuatro dimensiones ya sé qué decisión tomar». ¿Qué falla en esa idea? A) El modelo ayuda a analizar, pero la decisión necesita información y consulta; B) El modelo está mal.", "A", "Un modelo no entrega decisiones."),
      ("Un modelo que muestra solo la dimensión biológica deja fuera: A) Afectos, normas sociales e identidad; B) El cuerpo.", "A", "Falta lo que no es biológico."),
  ],
  cha=[
      ("Un estudiante ficticio dice: «Mis amigos me presionan, tengo ganas de pertenecer y no estoy seguro de querer». ¿Qué conviene hacer según lo aprendido? A) Reconocer que es su decisión, informarse en fuentes confiables y conversar con una persona adulta de confianza; B) Hacer lo que el grupo diga.", "A", "La responsabilidad individual incluye informarse y pedir apoyo."),
      ("Para evaluar si el modelo sirve, ¿qué podrías comparar? A) Cuántas situaciones de ejemplo se pueden analizar con él frente a cuántas no; B) Cuántos círculos dibujó cada persona.", "A", "Evaluar un modelo es ver qué logra explicar."),
  ],
  context=[("Una profesora ficticia propone analizar con el modelo una noticia sobre jóvenes y redes sociales. ¿Qué dimensión social debería aparecer? A) Cómo las redes influyen en la imagen que se tiene del cuerpo; B) Cuántas horas duerme un joven.", "A", "El efecto de las redes es parte de lo social.")],
  selfcheck=[("¿Qué indica la superposición de los círculos?", "Que las dimensiones se influyen", "Se relacionan entre sí."), ("¿Para qué sirve el modelo?", "Para analizar situaciones", "Ayuda a pensar, no decide."), ("Nombra un límite del modelo.", "Muestra separadas dimensiones que están conectadas", "Simplifica la realidad.")],
  open_task=task("Analiza esta situación ficticia con el modelo: «Un joven de 15 años siente cambios en su cuerpo, le gusta alguien de su curso, sus amigos hacen bromas y no sabe si está listo para hablar de sus sentimientos». Escribe qué dato corresponde a cada dimensión y un límite del modelo.", "Cambios del cuerpo: biológica; le gusta alguien: afectiva; bromas de amigos: social; no sabe si está listo: psicológica. Límite: separa dimensiones que en realidad se mezclan.", ["asigna las cuatro dimensiones", "justifica cada una", "declara un límite"], ["tabla de dato y dimensión"], ["asignar una sola dimensión", "tomar el modelo como una receta"], "Pregunta a quién puede pedir ayuda el joven del caso."),
  reinforce="Dibuja los cuatro círculos y anota un dato de ejemplo en cada uno.",
  extend="Explica con un ejemplo cómo una dimensión influye en otra.")

L(OA3, 4,
  materials=MAT,
  use="Aprenderé cómo se relacionan la información, la comunicación y el consentimiento con decisiones responsables, y a reconocer que una relación entre datos no prueba una causa. " + ADULTO,
  prior=["Sé que el consentimiento es un acuerdo libre, informado y retirable.", "Sé calcular porcentajes."],
  explain=[
      "En una investigación se estudia cómo una variable se relaciona con otra. La variable independiente es la que se cambia o compara, y la dependiente es la que se mide. Por ejemplo: si un grupo recibe una charla con fuentes confiables (independiente), se mide cuántas personas reconocen bien una fuente (dependiente).",
      "La responsabilidad en la sexualidad se apoya en variables que sí se pueden analizar: información confiable, comunicación respetuosa, consentimiento y uso de medidas de cuidado. Más información verificable permite decisiones mejor pensadas, pero no garantiza un resultado. Los datos muestran tendencias en grupos y no predicen lo que hará una persona.",
      "Si dos variables cambian juntas, eso es una asociación, y no siempre una causa. Para sospechar una causa hay que controlar otras variables. Ante cualquier situación de presión, de riesgo o de violencia, la acción responsable es no quedarse con el secreto: contarlo a una persona adulta de confianza y, si hay peligro, pedir ayuda. Fono Niños 147 es una línea de orientación.",
  ],
  vocab=[("variable independiente", "la que se cambia o compara"), ("variable dependiente", "la que se mide como resultado"), ("asociación", "cambio conjunto de dos variables, que no prueba una causa"), ("tendencia", "comportamiento general de un grupo")],
  worked=[
      ("Identificar variables", "Se compara si un curso con una charla de fuentes confiables reconoce mejor las fuentes que otro sin charla. Identifica las variables.", ["Lo que se compara es tener o no la charla: variable independiente.", "Lo que se mide es cuántos reconocen bien las fuentes: variable dependiente."], "Independiente: la charla; dependiente: cuántos reconocen bien las fuentes"),
      ("Leer una asociación", "En datos de ejemplo, en el curso A con charla 24 de 30 reconocen una fuente confiable y en el curso B sin charla, 15 de 30. ¿Qué porcentaje reconoce en cada uno?", ["Curso A: 24 dividido en 30 por 100 es 80 %.", "Curso B: 15 dividido en 30 por 100 es 50 %."], "A: 80 %; B: 50 %. Hay una asociación; no prueba por sí sola que la charla sea la causa"),
  ],
  mistakes=[
      ("Concluir que una asociación prueba una causa.", "Otras variables, como el curso o los conocimientos previos, pueden influir.", "Di «se asocia» y revisa qué más pudo cambiar."),
      ("Quedarse con un secreto cuando alguien presiona o amenaza.", "El silencio permite que el riesgo continúe.", "Cuéntalo a una persona adulta de confianza."),
  ],
  rec=[
      ("¿Cuál variable se mide como resultado: la independiente o la dependiente?", "La dependiente", "Es el resultado que se mide."),
      ("Verdadero o falso: dos variables que cambian juntas prueban siempre una causa.", "Falso", "Solo muestran una asociación."),
      ("Ante una presión o amenaza, la acción responsable es: A) Contarlo a una persona adulta de confianza; B) Guardar el secreto.", "A", "Avisar protege a la persona."),
  ],
  und=[
      ("En un estudio ficticio se compara tener o no taller de comunicación. ¿Cuál es la variable independiente? A) Tener o no el taller; B) El resultado del cuestionario.", "A", "Es lo que se compara."),
      ("Datos de ejemplo muestran tendencia de que quienes se informan en fuentes confiables toman decisiones más informadas. Esto significa que: A) Es más probable en el grupo, sin garantizar lo que hará cada persona; B) Todas las personas decidirán igual.", "A", "Una tendencia describe al grupo."),
      ("¿Qué elemento debe estar presente en cualquier acuerdo entre dos personas en una relación? A) Consentimiento libre y retirable; B) Insistencia hasta que acepten.", "A", "La insistencia anula la libertad del acuerdo."),
  ],
  app=[
      arith("En el grupo X de ejemplo, 18 de 20 estudiantes dicen que conversan con una persona adulta de confianza; en el grupo Y, 12 de 20. ¿Cuántos estudiantes más lo hacen en X que en Y?", "18-12", "Se restan las dos cantidades."),
      arith("En un curso ficticio de 25 estudiantes, 20 reconocen cuándo se necesita consentimiento tras una clase. ¿Qué porcentaje es?", "20*100//25", "Se divide la parte en el total y se multiplica por 100."),
      ("Una estudiante ficticia recibe mensajes de un adulto desconocido que le pide secretos. ¿Qué hace? A) No responder, guardar los mensajes, bloquear y contarlo a una persona adulta de confianza; B) Responderle un tiempo para saber qué quiere.", "A", "Evitar el contacto y avisar protege."),
  ],
  rea=[
      ("Dos cursos de ejemplo: el que tuvo la charla obtuvo mejor resultado, pero también tiene estudiantes de más edad. ¿Qué se puede decir? A) Hay una asociación, y la edad pudo influir; B) Se probó que la charla es la causa.", "A", "Otra variable pudo influir."),
      ("Alguien dice: «Si conozco los datos del grupo, sé lo que hará mi amigo». ¿Es válido? A) No, los datos describen tendencias del grupo; B) Sí, los datos predicen a cada persona.", "A", "Los datos de grupo no predicen individuos."),
  ],
  cha=[
      arith("Un grupo ficticio de 60 estudiantes: 36 reconocen bien las fuentes después de la charla y 21 las reconocían antes. ¿Cuántos reconocen más después?", "36-21", "Se restan las cantidades."),
      ("Para saber si una charla causa el cambio, ¿qué debería hacerse? A) Comparar con un grupo similar sin charla y controlar otras variables; B) Preguntar solo a los que asistieron.", "A", "Hay que controlar las demás variables."),
  ],
  context=[("En una campaña ficticia del liceo se cuenta cuántos estudiantes saben que pueden pedir orientación en el centro de salud. ¿Qué conclusión es prudente si subió de 15 a 24 de 40? A) Se asocia con la campaña, pero otras variables también pudieron influir; B) La campaña es la única causa.", "A", "Con esta evidencia solo se puede hablar de asociación.")],
  selfcheck=[("¿Qué es una variable dependiente?", "La que se mide como resultado", "Es la que cambia según la independiente."), ("¿Qué hace una persona ante una presión de riesgo?", "Cuenta a una persona adulta de confianza", "No guarda el secreto."), ("¿Una asociación prueba una causa?", "No", "Hay que controlar otras variables.")],
  open_task=task("Con estos datos ficticios, curso A (con taller): 21 de 28 reconocen una fuente confiable; curso B (sin taller): 14 de 28. Calcula los porcentajes, nombra las variables y escribe una conclusión prudente en dos oraciones.", "A 75 %, B 50 %. Independiente: taller; dependiente: reconocen fuente. «Hay una asociación entre el taller y reconocer mejor las fuentes. No se prueba una causa porque los cursos pudieron diferir en otras cosas.»", ["calcula ambos porcentajes", "nombra las variables", "conclusión con límite"], ["porcentajes, variables y conclusión"], ["afirmar causa", "no nombrar variables"], "Pregunta qué otra variable podrías controlar."),
  reinforce="Escribe una situación ficticia con una variable independiente y una dependiente.",
  extend="Explica por qué avisar a una persona adulta de confianza es parte de la responsabilidad individual.")


# ---------------------------------------------------------------- OA 04

AD2 = "Los casos son ficticios. Si tienes dudas sobre embarazo o salud, consulta a una persona adulta de confianza o a un profesional de salud."

L(OA4, 1,
  materials=MAT,
  use="Aprenderé las etapas desde la fecundación hasta la implantación y a plantear una pregunta investigable sobre el desarrollo temprano. " + AD2,
  prior=["Sé que el óvulo se libera en la ovulación y que el endometrio es la pared interna del útero.", "Sé que una pregunta investigable indica qué se mide."],
  explain=[
      "La fecundación es la unión de un espermatozoide con un óvulo y ocurre, por lo general, en una trompa uterina. La célula que se forma se llama cigoto y contiene el material genético de ambos progenitores. Mientras viaja hacia el útero, el cigoto se divide una y otra vez por mitosis y forma un conjunto de células.",
      "Cerca de una semana después de la fecundación, el conjunto de células llamado blastocisto llega al útero y se une al endometrio: eso es la implantación. Si ocurre, el embarazo continúa y el embrión se desarrolla. Si no hay fecundación o no hay implantación, el embarazo no continúa. Durante las primeras ocho semanas se habla de embrión, y desde la novena, de feto.",
      "Una pregunta investigable nombra algo medible. En un modelo simplificado, en las primeras divisiones cada división duplica el número de células. Por eso se puede preguntar «¿Cuántas células hay después de cierto número de divisiones?». «¿Es hermoso el desarrollo del embrión?» no sirve, porque no se puede medir.",
  ],
  vocab=[("fecundación", "unión de un espermatozoide con un óvulo"), ("cigoto", "célula que resulta de la fecundación"), ("blastocisto", "conjunto de células que se implanta en el útero"), ("implantación", "unión del blastocisto al endometrio")],
  worked=[
      ("Ordenar etapas", "Ordena estas etapas: implantación, divisiones del cigoto, fecundación.", ["Primero se unen las dos células sexuales: fecundación.", "Luego el cigoto se divide mientras viaja al útero.", "Finalmente el blastocisto se une al endometrio: implantación."], "Fecundación, divisiones del cigoto, implantación"),
      ("Calcular células", "Modelo simplificado: cada división duplica las células. Parte de 1 célula. ¿Cuántas hay tras 4 divisiones?", ["Después de 1 división: 2. Después de 2: 4. Después de 3: 8.", "Después de 4: 16."], "16 células"),
  ],
  mistakes=[
      ("Confundir fecundación con implantación.", "La fecundación une dos células; la implantación fija el blastocisto en el útero.", "Pregunta: ¿se unen células o el blastocisto se fija?"),
      ("Pensar que el embrión y el feto son lo mismo.", "Se distinguen por la etapa: embrión hasta la semana ocho; feto desde la nueve.", "Revisa en qué semana de desarrollo está."),
  ],
  rec=[
      ("¿Cómo se llama la unión de un espermatozoide con un óvulo?", "Fecundación", "Es la definición de la clase."),
      ("¿Cómo se llama la célula que resulta de la fecundación?", "Cigoto", "Es la primera célula del nuevo organismo."),
      ("Verdadero o falso: la implantación ocurre en el endometrio.", "Verdadero", "El blastocisto se une a la pared interna del útero."),
  ],
  und=[
      ("¿Dónde ocurre, por lo general, la fecundación? A) En una trompa uterina; B) En la vagina.", "A", "El óvulo se encuentra con el espermatozoide en la trompa."),
      ("¿Qué le ocurre al cigoto mientras viaja hacia el útero? A) Se divide varias veces; B) Se convierte de inmediato en feto.", "A", "Se divide por mitosis y forma más células."),
      ("¿Qué es la implantación? A) El blastocisto se une al endometrio; B) El óvulo sale del ovario.", "A", "Es la fijación en el útero."),
  ],
  app=[
      arith("Modelo simplificado: cada división duplica las células. Partiendo de 1 célula, ¿cuántas hay tras 3 divisiones?", "2*2*2", "Cada división multiplica por 2."),
      arith("Con el mismo modelo, ¿cuántas células hay tras 5 divisiones?", "2*2*2*2*2", "Se multiplica por 2 cinco veces."),
      ("¿Cuál pregunta se puede investigar? A) ¿Cuántas células hay tras 6 divisiones, según el modelo?; B) ¿Es linda la etapa del blastocisto?", "A", "Nombra algo medible."),
  ],
  rea=[
      arith("Un estudiante dice que tras 6 divisiones hay 12 células, porque suma 2 cada vez. Según el modelo de duplicación, ¿cuántas hay?", "2*2*2*2*2*2", "Se duplica en cada división, no se suma 2."),
      ("Si hubo fecundación pero el blastocisto no se une al endometrio, ¿qué ocurre? A) El embarazo no continúa; B) El embarazo continúa igual.", "A", "Sin implantación no se sigue desarrollando."),
  ],
  cha=[
      ("Con el modelo de duplicación, partiendo de 1 célula, ¿cuántas divisiones se necesitan como mínimo para tener más de 20 células?", "5", "Con 4 divisiones hay 16 y con 5 hay 32."),
      ("El modelo de duplicación dice que tras 10 divisiones hay 1.024 células. ¿Qué límite tiene ese modelo? A) En la realidad no todas las células se dividen al mismo tiempo; B) En la realidad las células nunca se dividen.", "A", "El modelo supone divisiones parejas y simultáneas, que el embrión real no cumple."),
  ],
  context=[("Una estudiante ficticia lee que la implantación ocurre cerca de una semana después de la fecundación. Si la fecundación fue el día 14 de un ciclo, ¿qué día del ciclo es la implantación aproximada?", "21", "Se suman 7 días a 14.", "14+7")],
  selfcheck=[("¿Dónde ocurre, por lo general, la fecundación?", "En una trompa uterina", "Allí se encuentran las células."), ("¿Qué se forma tras la fecundación?", "El cigoto", "Es la primera célula."), ("¿Hasta qué semana se habla de embrión?", "Hasta la octava", "Desde la novena es feto.")],
  open_task=task("Escribe una pregunta investigable sobre las primeras divisiones del cigoto. Usa el modelo de duplicación (cada división duplica las células) y calcula la respuesta para 7 divisiones partiendo de 1 célula. Indica un límite del modelo.", "«¿Cuántas células hay tras 7 divisiones, según el modelo?» 128. Límite: en la realidad las células no se dividen todas al mismo tiempo ni exactamente en 2.", ["pregunta medible", "cálculo correcto", "declara un límite"], ["pregunta, cálculo y límite"], ["sumar en vez de duplicar", "no declarar límite"], "Pregunta qué cambiaría si no todas las células se dividieran a la vez."),
  reinforce="Escribe el orden de fecundación, divisiones e implantación con una frase para cada una.",
  extend="Explica por qué una pregunta sobre el desarrollo debe indicar qué se mide.")

L(OA4, 2,
  materials=MAT,
  use="Aprenderé a leer fichas y tablas de datos de ejemplo sobre el embarazo y sobre el intercambio entre madre y embrión. " + AD2,
  prior=["Conozco las etapas de fecundación e implantación.", "Sé restar y leer una tabla."],
  explain=[
      "Un embarazo se cuenta en semanas. Suele decirse que dura unas 40 semanas contadas desde la última menstruación. Durante ese tiempo se hacen controles prenatales: una matrona o un médico mide, pregunta y registra datos en una ficha. Esos datos se comparan en el tiempo para ver cómo avanza el embarazo.",
      "La placenta es un órgano que se forma en el útero. Permite que pasen sustancias entre la sangre de la madre y la del embrión sin que las sangres se mezclen directamente. De la madre pasan al embrión el oxígeno y los nutrientes; del embrión a la madre pasan el dióxido de carbono y otros desechos, que la madre elimina. Algunas sustancias dañinas, como el alcohol y la nicotina, también pueden pasar.",
      "Los datos de una ficha no se interpretan solos. Cada persona tiene un ritmo distinto y solo un profesional puede decir si un valor es adecuado. En esta clase los datos son de ejemplo y sirven para practicar la lectura, no para evaluar a nadie.",
  ],
  vocab=[("control prenatal", "visita periódica para revisar el embarazo"), ("placenta", "órgano que permite el intercambio entre madre y embrión"), ("nutriente", "sustancia que aporta lo necesario para crecer"), ("desecho", "sustancia que el cuerpo debe eliminar")],
  worked=[
      ("Leer una ficha", "Ficha de ejemplo: semana 10, peso materno 56 kg; semana 28, 62 kg. ¿Cuánto aumentó el peso?", ["Se resta el valor inicial al final.", "62 menos 56 da 6."], "6 kg"),
      ("Clasificar la etapa", "Una ficha de ejemplo dice «semana 7 de desarrollo». ¿Embrión o feto?", ["Las primeras ocho semanas se llaman embrión.", "Siete está dentro de ese período."], "Embrión"),
  ],
  mistakes=[
      ("Creer que las sangres de madre y embrión se mezclan.", "El intercambio ocurre a través de la placenta, sin mezcla directa.", "Piensa en la placenta como un intercambiador."),
      ("Evaluar si un valor «está bien» solo con una tabla de ejemplo.", "Solo un profesional puede evaluar cada caso.", "Usa los datos para practicar y consulta a un profesional."),
  ],
  rec=[
      ("¿Cuántas semanas suele durar un embarazo, contadas desde la última menstruación?", "40", "Es la duración aproximada."),
      ("¿Qué órgano permite el intercambio entre la madre y el embrión?", "La placenta", "Intercambia sustancias sin mezclar las sangres."),
      ("Verdadero o falso: las sangres de la madre y del embrión se mezclan directamente.", "Falso", "El intercambio ocurre a través de la placenta."),
  ],
  und=[
      ("En el intercambio, ¿en qué sentido viaja el dióxido de carbono? A) Del embrión a la madre; B) De la madre al embrión.", "A", "Es un desecho que la madre elimina."),
      ("Una ficha ficticia dice «semana 20 de desarrollo». ¿Cómo se llama en esa etapa? A) Feto; B) Embrión.", "A", "Pasada la semana ocho se habla de feto."),
      ("¿Qué sustancias pasan de la madre al embrión por la placenta? A) Oxígeno y nutrientes; B) Solo desechos.", "A", "El embrión recibe lo que necesita para crecer."),
  ],
  app=[
      arith("Ficha de ejemplo: semana 12, 60 kg; semana 38, 70 kg. ¿Cuántos kilogramos aumentó el peso?", "70-60", "Se resta el valor inicial al final."),
      arith("Ficha de ejemplo: semana 20, 63 kg; semana 30, 67 kg. ¿Cuántos kilogramos aumentó?", "67-63", "Se resta el valor inicial al final."),
      arith("¿Cuántas semanas pasaron entre el control de la semana 12 y el de la semana 38?", "38-12", "Se restan los números de semana."),
  ],
  rea=[
      ("Un compañero ve que la persona de la ficha de ejemplo aumentó 10 kg y dice: «Eso está mal». ¿Qué respondes? A) No se puede concluir con un solo dato, lo evalúa un profesional; B) Tiene razón, es demasiado.", "A", "No hay criterio ni contexto para afirmarlo."),
      ("Si una tabla no indica cuántos controles se hicieron, ¿qué limitación tiene al comparar? A) Falta información para comparar; B) Nada, está completa.", "A", "Sin ese dato no se sabe si los grupos son comparables."),
  ],
  cha=[
      arith("Ficha A (ejemplo): 60 kg a 70 kg. Ficha B (ejemplo): 55 kg a 68 kg. ¿Cuántos kilogramos más aumentó B que A?", "(68-55)-(70-60)", "Aumento de B menos aumento de A."),
      ("Pesos de ejemplo: semana 12, 60 kg; semana 20, 63 kg; semana 30, 67 kg; semana 38, 70 kg. ¿Entre qué semanas fue mayor el aumento total en kilogramos? A) Entre la 20 y la 30; B) Entre la 12 y la 20.", "A", "Entre la 20 y la 30 aumentó 4 kg y entre la 12 y la 20, 3 kg."),
  ],
  context=[("Una estudiante ficticia ve este gráfico de barras de ejemplo: semana 12, 60 kg; semana 20, 63 kg; semana 30, 67 kg. ¿Qué tendencia muestra? A) El peso aumenta con las semanas; B) El peso disminuye.", "A", "Cada barra es mayor que la anterior.")],
  selfcheck=[("¿Qué órgano intercambia sustancias entre madre y embrión?", "La placenta", "Intercambia sin mezclar sangres."), ("¿Hasta qué semana se habla de embrión?", "Hasta la octava", "Después es feto."), ("¿Quién puede evaluar si un valor de la ficha es adecuado?", "Un profesional de salud", "Cada caso es distinto.")],
  open_task=task("Con la ficha de ejemplo: semana 10, 56 kg; semana 20, 59 kg; semana 30, 63 kg. Calcula el aumento entre cada par de controles, dibuja un gráfico de barras y escribe dos oraciones: una con la tendencia y otra con el límite de los datos.", "Aumentos: 3 y 4 kg. Gráfico de barras. «El peso aumenta en el tiempo. Son datos de ejemplo y un profesional debe evaluar cada caso.»", ["calcula aumentos", "gráfico adecuado", "incluye límite"], ["aumentos, gráfico y dos oraciones"], ["decir que un valor es bueno o malo", "no declarar que son datos de ejemplo"], "Pregunta qué otros datos agregaría un profesional."),
  reinforce="Calcula el aumento entre dos controles de una ficha ficticia que tú escribas.",
  extend="Explica por qué la placenta no mezcla las sangres.")

L(OA4, 3,
  materials=MAT,
  use="Aprenderé a usar un modelo de la implantación y de la placenta para predecir qué sustancias llegan al embrión y qué límites tiene el modelo. " + AD2,
  prior=["Conozco la función de la placenta.", "Sé que un modelo simplifica la realidad."],
  explain=[
      "El modelo del embarazo tiene tres partes: la placenta, que intercambia sustancias; el cordón umbilical, que conecta al embrión con la placenta; y el saco amniótico, una bolsa con líquido amniótico que amortigua los golpes y mantiene un ambiente estable. El embrión recibe oxígeno y nutrientes por el cordón y devuelve desechos por el mismo camino.",
      "El modelo permite predecir. Si una sustancia está en la sangre de la madre y es capaz de atravesar la placenta, puede llegar al embrión. Por eso el alcohol, el tabaco y algunos medicamentos son riesgosos durante el embarazo: la persona embarazada no debe tomar medicamentos sin indicación de un profesional de salud.",
      "Todo modelo tiene límites. Un dibujo de la placenta no está a escala, no muestra cómo crece el embrión ni todas las sustancias que pasan. Un modelo sirve para explicar y predecir, y se mejora cuando aparecen datos nuevos.",
  ],
  vocab=[("cordón umbilical", "conexión entre el embrión y la placenta"), ("saco amniótico", "bolsa que contiene al embrión y al líquido amniótico"), ("líquido amniótico", "líquido que amortigua y mantiene un ambiente estable"), ("predecir", "anticipar qué ocurrirá con base en un modelo")],
  worked=[
      ("Predecir con el modelo", "Una persona embarazada ficticia consume una sustancia que pasa a su sangre. ¿Puede llegar al embrión?", ["Según el modelo, la placenta deja pasar muchas sustancias de la sangre materna.", "Si la sustancia atraviesa la placenta, llega al embrión."], "Sí, puede llegar; por eso hay que consultar antes de consumir cualquier sustancia"),
      ("Relacionar parte y función", "¿Qué parte del modelo amortigua los golpes?", ["Las partes son placenta, cordón y saco amniótico.", "El saco amniótico contiene líquido que amortigua."], "El saco amniótico con su líquido"),
  ],
  mistakes=[
      ("Pensar que la placenta bloquea todas las sustancias dañinas.", "Deja pasar muchas, como el alcohol y la nicotina.", "Recuerda: lo que está en la sangre materna puede llegar al embrión."),
      ("Usar el dibujo del modelo como si tuviera las proporciones reales.", "Los modelos simplifican tamaños.", "Declara que el modelo no está a escala."),
  ],
  rec=[
      ("¿Qué parte del modelo conecta el embrión con la placenta?", "El cordón umbilical", "Lleva oxígeno y nutrientes y devuelve desechos."),
      ("¿Qué contiene el saco amniótico?", "Líquido amniótico", "Amortigua y mantiene el ambiente."),
      ("Verdadero o falso: la placenta bloquea todas las sustancias de la sangre materna.", "Falso", "Deja pasar muchas, incluido el alcohol."),
  ],
  und=[
      ("¿Qué función tiene el líquido amniótico? A) Amortiguar golpes y mantener un ambiente estable; B) Producir las hormonas del ciclo.", "A", "Protege al embrión."),
      ("Según el modelo, una sustancia que atraviesa la placenta: A) Puede llegar al embrión; B) Nunca llega.", "A", "Atravesar la placenta permite llegar al embrión."),
      ("¿Cuál es el papel de la placenta en el modelo? A) Intercambiar oxígeno, nutrientes y desechos; B) Producir espermatozoides.", "A", "Es el órgano de intercambio."),
  ],
  app=[
      arith("Si una persona embarazada lleva 13 semanas de embarazo, ¿cuántas semanas faltan para las 40 semanas aproximadas?", "40-13", "Se resta lo transcurrido de la duración total."),
      ("Una persona embarazada ficticia tiene dolor de cabeza. ¿Qué es lo más seguro? A) Consultar a un profesional de salud antes de tomar un medicamento; B) Tomar el medicamento que usa su amigo.", "A", "Algunos medicamentos pasan la placenta."),
      ("¿Qué parte del modelo transporta nutrientes hacia el embrión? A) El cordón umbilical; B) El saco amniótico.", "A", "Conduce sustancias entre la placenta y el embrión."),
  ],
  rea=[
      ("Alguien dice: «Si una sustancia es de venta libre, no puede pasar al embrión». ¿Qué falla? A) Que se venda libremente no impide que atraviese la placenta; B) Nada, es correcto.", "A", "Lo que importa es si llega a la sangre y atraviesa la placenta."),
      ("¿Qué límite tiene un dibujo del modelo que muestra la placenta con el mismo tamaño en todo el embarazo? A) No muestra que el tamaño cambia; B) No tiene límites.", "A", "Un dibujo fijo no representa el crecimiento."),
  ],
  cha=[
      ("Un grupo ficticio quiere ampliar el modelo: ¿qué dato nuevo permitiría mejorarlo? A) Qué sustancias específicas pasan y cuáles no, medido por profesionales; B) Cuántos colores usa el dibujo.", "A", "Un modelo se mejora con evidencia nueva."),
      ("Un modelo explica bien el intercambio de oxígeno pero no explica cómo crece el embrión. ¿Qué se puede decir? A) Explica una parte y tiene un límite; B) Es falso en todo.", "A", "Un modelo puede ser útil y limitado."),
  ],
  context=[("Una matrona ficticia explica a un curso la importancia de los controles prenatales. ¿Qué parte del modelo justifica evitar el alcohol en el embarazo? A) La placenta, porque el alcohol atraviesa y llega al embrión; B) El saco amniótico, porque guarda el alcohol.", "A", "El paso por la placenta explica el riesgo.")],
  selfcheck=[("¿Qué parte conecta embrión y placenta?", "El cordón umbilical", "Conduce las sustancias."), ("¿Qué limita al modelo?", "No está a escala ni muestra el crecimiento", "Simplifica la realidad."), ("¿Qué debes hacer antes de tomar un medicamento en el embarazo?", "Consultar a un profesional de salud", "Algunos pasan al embrión.")],
  open_task=task("Dibuja un esquema del modelo con placenta, cordón y saco amniótico. Rotula la función de cada parte y escribe una predicción sobre una sustancia que está en la sangre de la madre y atraviesa la placenta. Añade un límite del esquema.", "Placenta: intercambia; cordón: conecta; saco: amortigua. Predicción: la sustancia puede llegar al embrión. Límite: el dibujo no está a escala.", ["rotula tres partes", "predicción coherente", "límite declarado"], ["esquema con rótulos y predicción"], ["decir que la placenta bloquea todo", "olvidar el límite"], "Pregunta qué dato necesitarías para saber qué sustancia concreta pasa."),
  reinforce="Escribe la función de la placenta, del cordón y del saco amniótico.",
  extend="Explica con el modelo por qué se aconseja consultar antes de tomar medicamentos en el embarazo.")

L(OA4, 4,
  materials=MAT,
  use="Aprenderé cómo se relacionan la nutrición, los controles, el alcohol y la lactancia con el desarrollo, y cómo analizar la responsabilidad de los padres. " + AD2,
  prior=["Conozco la placenta y el intercambio.", "Sé que una asociación no prueba una causa."],
  explain=[
      "La nutrición prenatal es la alimentación de la persona embarazada durante el embarazo. Una alimentación variada aporta lo que el embrión necesita. Algunos profesionales indican ácido fólico, una vitamina que ayuda a formar el tubo neural, el que da origen al cerebro y a la médula espinal. La indicación y la cantidad las define un profesional de salud.",
      "El alcohol, el tabaco y las drogas pueden dañar el desarrollo, porque atraviesan la placenta. Los controles prenatales ayudan a detectar a tiempo posibles problemas. La lactancia materna entrega nutrientes y defensas, y se recomienda de forma exclusiva durante los primeros seis meses. Cuando no es posible amamantar, un profesional orienta alternativas seguras.",
      "La responsabilidad de los padres incluye a ambos: informarse, apoyar los controles, cuidar la alimentación y el entorno, y repartir el cuidado del recién nacido. Los datos muestran asociaciones entre estos cuidados y mejores resultados, pero a veces hay complicaciones aun cuando se cuida todo, y no corresponde culpar a nadie.",
  ],
  vocab=[("nutrición prenatal", "alimentación durante el embarazo"), ("lactancia", "alimentación del recién nacido con leche materna"), ("ácido fólico", "vitamina que ayuda a formar el tubo neural"), ("corresponsabilidad", "reparto del cuidado entre ambos progenitores")],
  worked=[
      ("Leer una asociación", "En datos de ejemplo, de 50 embarazos con controles regulares, 45 no tuvieron complicaciones. ¿Qué porcentaje es?", ["Parte: 45; total: 50.", "45 dividido en 50 por 100 es 90."], "90 %"),
      ("Identificar variables", "Se compara el número de controles prenatales (0, 3 o 6) con las complicaciones. ¿Cuál es la variable independiente?", ["Lo que se compara es el número de controles.", "Las complicaciones son lo que se mide."], "El número de controles prenatales"),
  ],
  mistakes=[
      ("Culpar a la madre por cualquier complicación.", "Pueden ocurrir complicaciones aun con todos los cuidados.", "Habla de factores de riesgo y de apoyo, sin culpar."),
      ("Pensar que la responsabilidad es solo de la madre.", "Ambos progenitores pueden informarse, apoyar y cuidar.", "Habla de corresponsabilidad."),
  ],
  rec=[
      ("¿Cómo se llama la alimentación del recién nacido con leche materna?", "Lactancia", "Es la definición de la clase."),
      ("Verdadero o falso: el alcohol y el tabaco pueden atravesar la placenta.", "Verdadero", "Por eso pueden afectar el desarrollo."),
      ("¿Quién define la indicación y la cantidad de ácido fólico? A) Un profesional de salud; B) Cualquier persona.", "A", "Es una indicación individual."),
  ],
  und=[
      ("¿Para qué sirven los controles prenatales? A) Para detectar a tiempo posibles problemas; B) Para saber el color de ojos del bebé.", "A", "Permiten seguimiento del embarazo."),
      ("¿Qué aporta la leche materna al recién nacido? A) Nutrientes y defensas; B) Solo agua.", "A", "Entrega nutrientes y defensas."),
      ("¿Qué significa corresponsabilidad en el cuidado? A) Que ambos progenitores se reparten el cuidado; B) Que solo uno decide.", "A", "Implica compartir tareas y decisiones."),
  ],
  app=[
      arith("En un grupo de ejemplo de 40 embarazos con controles desde el inicio, 36 no tuvieron complicaciones. ¿Qué porcentaje es?", "36*100//40", "Se divide la parte en el total y se multiplica por 100."),
      arith("En otro grupo de ejemplo de 40 embarazos sin controles, 28 no tuvieron complicaciones. ¿Cuántos más sin complicaciones hay en el primer grupo (36) que en este?", "36-28", "Se restan las dos cantidades."),
      ("Una pareja ficticia espera un bebé. ¿Qué acción es responsable? A) Ir juntos a los controles y repartirse las tareas de cuidado; B) Dejar todo en manos de una sola persona.", "A", "Eso es la corresponsabilidad en el cuidado."),
  ],
  rea=[
      ("Los datos de ejemplo muestran menos complicaciones con controles. Alguien afirma: «Con controles nunca hay complicaciones». ¿Es válido? A) No, son tendencias de grupo y aún puede haberlas; B) Sí.", "A", "Los datos de grupo no garantizan un caso."),
      ("Una estudiante dice: «Si hubo una complicación, la madre hizo algo mal». ¿Qué respondes? A) Puede ocurrir aun con todos los cuidados, y no se culpa; B) Tiene razón.", "A", "Las causas son múltiples."),
  ],
  cha=[
      ("Un estudio ficticio compara dos grupos y el que consumió alcohol tuvo más complicaciones. ¿Qué variable convendría controlar? A) La edad y los controles de ambos grupos; B) El color de la ropa.", "A", "Otras variables también pueden influir."),
      ("Una familia ficticia debe elegir cómo alimentar al recién nacido. ¿Qué paso es adecuado? A) Pedir orientación a un profesional del centro de salud; B) Decidirlo según un consejo de internet.", "A", "Un profesional orienta según cada caso."),
  ],
  context=[("Un centro de salud ficticio registra 20 consultas sobre lactancia en un mes y 15 sobre controles. ¿Cuántas consultas hay en total?", "35", "Se suman las consultas.", "20+15")],
  selfcheck=[("¿Cómo se llama el reparto del cuidado entre ambos progenitores?", "Corresponsabilidad", "Ambos progenitores participan en el cuidado."), ("¿Qué aporta la leche materna?", "Nutrientes y defensas", "Protege y alimenta."), ("¿Se debe culpar a la madre por una complicación?", "No", "Pueden ocurrir aun con cuidados.")],
  open_task=task("Con estos datos de ejemplo: 30 embarazos con controles regulares, 27 sin complicaciones; 30 sin controles, 21 sin complicaciones. Calcula los porcentajes y escribe una conclusión con la palabra «asociación» y una limitación. Agrega dos responsabilidades de ambos progenitores.", "90 % y 70 %. «Hay una asociación entre los controles y menos complicaciones. Son datos de ejemplo y otras variables pueden influir.» Responsabilidades: ir a los controles y repartir el cuidado.", ["calcula los dos porcentajes", "usa asociación sin hablar de causa", "dos responsabilidades"], ["porcentajes, conclusión y responsabilidades"], ["culpar a una persona", "afirmar causa"], "Pregunta qué otras variables podrían influir."),
  reinforce="Escribe tres cuidados de la persona embarazada y uno del otro progenitor.",
  extend="Explica por qué la responsabilidad en el cuidado prenatal es compartida.")

L(OA4, 5,
  materials=MAT,
  use="Aprenderé el mecanismo del intercambio por la placenta, de la acción del ácido fólico y del alcohol, y de la producción de leche materna. " + AD2,
  prior=["Conozco la placenta y la lactancia.", "Sé que las hormonas son mensajeros químicos."],
  explain=[
      "El intercambio en la placenta se explica en parte por difusión: una sustancia pasa de donde hay más a donde hay menos. El oxígeno abunda en la sangre materna y pasa al embrión, que tiene menos; el dióxido de carbono abunda en el embrión y pasa a la sangre materna. Los nutrientes llegan desde la sangre materna y los desechos salen en sentido contrario.",
      "El ácido fólico participa en la formación de material genético y en la división celular, procesos intensos al inicio del embarazo; su falta se asocia con defectos en el cierre del tubo neural. El alcohol atraviesa la placenta y el hígado del feto aún no está maduro para eliminarlo, por eso puede afectar el desarrollo del cerebro.",
      "La producción de leche se regula por hormonas. La prolactina estimula a las glándulas mamarias a producir leche, y la oxitocina provoca la salida de la leche cuando el bebé succiona. La succión del bebé estimula la liberación de ambas, por lo que mientras más se amamanta, más leche se produce.",
  ],
  vocab=[("difusión", "paso de una sustancia desde donde hay más hacia donde hay menos"), ("prolactina", "hormona que estimula la producción de leche"), ("oxitocina", "hormona que provoca la salida de la leche"), ("succión", "acción de chupar que hace el bebé al amamantar")],
  worked=[
      ("Predecir el sentido de la difusión", "En la sangre de la madre el oxígeno es mayor que en el embrión. ¿Hacia dónde pasa?", ["La difusión va de donde hay más a donde hay menos.", "Hay más oxígeno en la madre."], "De la madre al embrión"),
      ("Relacionar hormona y efecto", "¿Qué hormona produce la salida de la leche cuando el bebé succiona?", ["La succión estimula la liberación de hormonas.", "La oxitocina provoca la salida de la leche."], "La oxitocina"),
  ],
  mistakes=[
      ("Creer que la difusión va siempre de la madre al embrión.", "Va de donde hay más a donde hay menos; el dióxido de carbono va del embrión a la madre.", "Revisa dónde hay más de cada sustancia."),
      ("Confundir prolactina con oxitocina.", "La prolactina produce la leche; la oxitocina la hace salir.", "Asocia prolactina con producir y oxitocina con salir."),
  ],
  rec=[
      ("¿Cómo se llama el paso de una sustancia desde donde hay más hacia donde hay menos?", "Difusión", "Es la definición de la clase."),
      ("¿Qué hormona estimula la producción de leche?", "La prolactina", "Estimula a las glándulas mamarias."),
      ("Verdadero o falso: la succión del bebé estimula la liberación de las hormonas de la lactancia.", "Verdadero", "Por eso mientras más se amamanta, más leche se produce."),
  ],
  und=[
      ("El dióxido de carbono abunda en el embrión. ¿Hacia dónde pasa por difusión? A) A la sangre materna; B) Se queda en el embrión.", "A", "Pasa de donde hay más a donde hay menos."),
      ("¿Qué hormona hace salir la leche? A) La oxitocina; B) La prolactina.", "A", "La oxitocina provoca la salida."),
      ("¿Por qué el alcohol puede afectar el desarrollo del cerebro del feto? A) Atraviesa la placenta y el hígado fetal es inmaduro; B) Porque el feto lo elimina más rápido que un adulto.", "A", "No se elimina bien y puede dañar."),
  ],
  app=[
      ("Un bebé ficticio mama con frecuencia durante el día. ¿Qué ocurre con la producción de leche? A) Se mantiene o aumenta por la succión; B) Se detiene.", "A", "La succión estimula la prolactina."),
      ("Si falta ácido fólico al inicio del embarazo, ¿qué proceso puede afectarse? A) El cierre del tubo neural; B) La formación de los huesos de las piernas.", "A", "La vitamina participa en la formación celular y del tubo neural."),
      arith("Una madre ficticia amamanta 8 veces al día. ¿Cuántas veces amamanta en 3 días?", "8*3", "Se multiplica por los días."),
  ],
  rea=[
      ("Alguien dice: «Si el bebé no mama, el cuerpo igual produce la misma leche». ¿Qué falla? A) La succión estimula las hormonas que regulan la producción; B) Nada.", "A", "Sin succión baja el estímulo."),
      ("Un compañero dice: «La difusión es un movimiento que el cuerpo impulsa con mucha energía». ¿Qué respondes? A) La difusión ocurre por diferencia de cantidad, sin que el cuerpo la impulse; B) Tiene razón.", "A", "Es un proceso espontáneo."),
  ],
  cha=[
      ("Datos ficticios muestran que mientras más veces se amamanta, más leche se produce. ¿Qué mecanismo lo explica? A) Mayor succión, más prolactina; B) Mayor producción de testosterona en la madre.", "A", "La succión estimula la hormona."),
      ("Una persona embarazada ficticia tiene dudas sobre el alcohol. ¿Qué consejo es el más prudente? A) Evitarlo durante el embarazo y consultar a un profesional; B) Tomar poco, porque nadie se daña.", "A", "Se evita porque atraviesa la placenta."),
  ],
  context=[("Una matrona ficticia dice que la oxitocina también ayuda a que el útero se contraiga después del parto. ¿Qué tipo de sustancia es la oxitocina? A) Una hormona; B) Una vitamina.", "A", "Es un mensajero químico del sistema endocrino.")],
  selfcheck=[("¿Qué hormona estimula producir leche?", "La prolactina", "Estimula las glándulas mamarias."), ("¿Hacia dónde difunde el oxígeno en la placenta?", "De la madre al embrión", "Hay más en la madre."), ("¿Qué es la difusión?", "Paso de una sustancia desde donde hay más hacia donde hay menos", "Es una definición.")],
  open_task=task("Escribe un párrafo de tres oraciones que explique cómo la succión del bebé lleva a la producción y salida de la leche, usando los nombres de las dos hormonas. Añade una oración que diga por qué los datos de ejemplo son solo una guía.", "La succión estimula la liberación de prolactina y oxitocina. La prolactina produce la leche y la oxitocina la hace salir. Mientras más se amamanta, más leche. Son datos de ejemplo.", ["nombra las dos hormonas", "explica el orden", "incluye limitación"], ["párrafo de tres oraciones"], ["confundir las hormonas", "no relacionar la succión"], "Pregunta qué pasaría con la producción si no hubiera succión."),
  reinforce="Escribe el sentido de difusión del oxígeno y del dióxido de carbono.",
  extend="Explica por qué se pide evitar el alcohol en el embarazo.")


# ---------------------------------------------------------------- OA 05

AD3 = "Los casos son ficticios. La elección de un método la hace cada persona con orientación de un profesional de salud (matrona o médico)."

L(OA5, 1,
  materials=MAT,
  use="Aprenderé qué tipos de métodos de regulación de la fertilidad existen y cómo plantear preguntas investigables para compararlos. " + AD3,
  prior=["Conozco el ciclo menstrual y la fecundación.", "Sé que una pregunta investigable indica qué se mide."],
  explain=[
      "Regular la fertilidad es decidir si se tendrá un hijo o una hija y cuándo, usando métodos que evitan el embarazo o ayudan a buscarlo. Los métodos para evitar un embarazo se agrupan en: de barrera (como el preservativo), hormonales (píldora, inyectables, implante), dispositivo intrauterino (DIU), quirúrgicos (vasectomía y ligadura de trompas) y naturales, basados en conocer el ciclo, que exigen constancia y son menos fiables.",
      "Para compararlos se usan criterios: si previenen infecciones de transmisión sexual (ITS), si son reversibles, si dependen de la persona cada día o en cada relación, y si necesitan un profesional. Entre los métodos de esta lista, solo el preservativo previene también las ITS. Ningún método es adecuado para todas las personas: la elección se hace con orientación de un profesional de salud.",
      "Una pregunta investigable usa esos criterios y se contesta con datos. «¿Cuántos de los cinco métodos de una tabla de ejemplo previenen ITS?» se puede responder contando. «¿Cuál es el mejor método?» no, porque depende de cada persona y de su situación, y no dice qué medir.",
  ],
  vocab=[("método de barrera", "impide que el espermatozoide llegue al óvulo, como el preservativo"), ("método hormonal", "usa hormonas para impedir la ovulación"), ("ITS", "infección de transmisión sexual"), ("reversible", "que se puede suspender y recuperar la fertilidad")],
  worked=[
      ("Clasificar un método", "Un implante bajo la piel libera una hormona de a poco. ¿A qué tipo pertenece?", ["Se coloca una pieza que libera una hormona.", "Los métodos que usan hormonas son hormonales."], "Hormonal"),
      ("Mejorar una pregunta", "Mejora «¿Cuál método es el mejor?» para que se pueda investigar.", ["Quito la palabra de juicio: «mejor».", "Indico un criterio medible: prevenir ITS.", "Indico dónde miro: los métodos de una tabla de ejemplo."], "«¿Cuántos de los 5 métodos de la tabla de ejemplo previenen ITS?»"),
  ],
  mistakes=[
      ("Creer que todos los métodos previenen las ITS.", "Entre los métodos de esta lista, solo el preservativo lo hace.", "Revisa siempre ese criterio en la tabla."),
      ("Buscar «el mejor método» para todas las personas.", "La elección depende de cada persona y de la orientación profesional.", "Compara por criterios y consulta."),
  ],
  rec=[
      ("¿Qué método de barrera previene también las ITS?", "El preservativo", "Es el único de la lista con esa propiedad."),
      ("Verdadero o falso: la vasectomía es un método quirúrgico.", "Verdadero", "Se hace mediante una intervención."),
      ("¿Qué significa que un método sea reversible? A) Que se puede suspender y se recupera la fertilidad; B) Que no se puede usar nunca más.", "A", "Es lo contrario de permanente."),
  ],
  und=[
      ("La píldora anticonceptiva es un método: A) Hormonal; B) De barrera.", "A", "Contiene hormonas que impiden la ovulación."),
      ("¿Quién orienta sobre qué método conviene a cada persona? A) Un profesional de salud; B) Cualquier compañero.", "A", "La elección requiere orientación profesional."),
      ("Un método natural basado en el ciclo requiere: A) Constancia y registro del ciclo; B) Una operación.", "A", "Depende de conocer y registrar el ciclo."),
  ],
  app=[
      ("¿Cuál pregunta se puede investigar? A) ¿Cuántos métodos de una tabla de ejemplo de 6 son permanentes?; B) ¿Cuál método es más lindo?", "A", "Nombra algo que se cuenta."),
      arith("En un centro de salud ficticio, 10 de 40 consultas del mes fueron de estudiantes de enseñanza media. ¿Qué porcentaje es?", "10*100//40", "Se divide la parte en el total y se multiplica por 100."),
      ("Un dispositivo pequeño que un profesional coloca en el útero es: A) Un DIU; B) Un método quirúrgico.", "A", "Es un dispositivo intrauterino."),
  ],
  rea=[
      ("Un compañero dice: «Usaré el método que usa mi amigo». ¿Qué le respondes? A) Conviene consultar a un profesional según cada situación; B) Es lo mejor.", "A", "No todos los métodos sirven igual a todas las personas."),
      ("Para decidir entre métodos, ¿qué dato es más útil? A) Si previene ITS y si es reversible; B) Si el método lo usa más gente en su curso.", "A", "Son criterios medibles."),
  ],
  cha=[
      arith("En una lista de ejemplo de 7 métodos, 2 son permanentes y 3 son reversibles de acción prolongada. ¿Cuántos quedan por clasificar?", "7-2-3", "Se restan los ya clasificados."),
      ("Una pareja ficticia quiere un método que también reduzca el riesgo de ITS. ¿Qué criterio debe revisar? A) Si es de barrera con preservativo; B) Si es permanente.", "A", "Entre los métodos de la lista, solo el preservativo previene ITS."),
  ],
  context=[("Un liceo ficticio invita a una matrona. ¿Qué pregunta le conviene preparar para investigar? A) ¿Qué criterios sirven para comparar métodos?; B) ¿Por qué es complicado el tema?", "A", "Pide criterios que se pueden usar con datos.")],
  selfcheck=[("¿Qué método previene también ITS?", "El preservativo", "Es de barrera."), ("¿Quién orienta la elección?", "Un profesional de salud", "Cada caso es distinto."), ("¿Qué es un método reversible?", "Uno que se puede suspender y se recupera la fertilidad", "No es permanente.")],
  open_task=task("Elige de esta lista de ejemplo (preservativo, píldora, DIU, vasectomía) dos métodos y escribe una pregunta investigable que los compare con un criterio medible (prevenir ITS, ser reversible o depender de la persona cada día). Escribe cómo la responderías con una tabla.", "«¿Cuál de la píldora y el DIU depende de la persona cada día?» Tabla: método y si depende de la persona (sí/no).", ["usa dos métodos de la lista", "usa un criterio medible", "indica una tabla"], ["pregunta y tabla"], ["usar «mejor»", "no indicar criterio"], "Pregunta qué profesional podría orientar sobre ese criterio."),
  reinforce="Clasifica cuatro métodos en barrera, hormonal, DIU, quirúrgico o natural.",
  extend="Explica por qué «el mejor método» no es una pregunta investigable.")

L(OA5, 2,
  materials=MAT,
  use="Aprenderé a leer una tabla que compara métodos con criterios y a organizar datos de consultas en gráficos. " + AD3,
  prior=["Conozco los tipos de métodos.", "Sé calcular porcentajes."],
  explain=[
      "Una tabla de comparación ordena los métodos en filas y los criterios en columnas. Criterios útiles: tipo, si previene ITS, si es reversible o permanente y cada cuánto hay que actuar (en cada relación, cada día o de acción prolongada). Por ejemplo: el preservativo es de barrera, previene ITS y se usa en cada relación; la píldora es hormonal, no previene ITS y se toma cada día.",
      "El implante y el DIU son de acción prolongada: una vez colocados por un profesional, protegen por años, y se pueden retirar para recuperar la fertilidad. La vasectomía y la ligadura de trompas son métodos quirúrgicos que se consideran permanentes. Ninguno de estos cuatro previene ITS.",
      "Los datos de consultas se resumen con conteos y porcentajes. Una tabla muestra cantidades; un gráfico de barras permite comparar. Un dato de consultas dice qué método se pregunta más, y no qué método es mejor. Esta clase usa datos de ejemplo.",
  ],
  vocab=[("acción prolongada", "método que protege por mucho tiempo sin actuar cada día"), ("permanente", "método que se considera definitivo"), ("criterio", "característica que sirve para comparar"), ("consulta", "visita a un profesional para pedir orientación")],
  worked=[
      ("Leer una tabla", "Tabla de ejemplo: preservativo (previene ITS: sí), píldora (no), DIU (no), vasectomía (no), implante (no). ¿Cuántos métodos previenen ITS?", ["Recorro la columna «previene ITS».", "Solo el preservativo tiene «sí»."], "1 método"),
      ("Calcular un porcentaje", "En 30 consultas de ejemplo, 12 fueron por preservativo. ¿Qué porcentaje es?", ["Parte: 12; total: 30.", "12 dividido en 30 por 100 es 40."], "40 %"),
  ],
  mistakes=[
      ("Concluir que el método más consultado es el mejor.", "Las consultas muestran qué se pregunta, no cuál conviene.", "Describe el dato sin juzgarlo."),
      ("Pensar que un método de acción prolongada es siempre permanente.", "El implante y el DIU se retiran y se recupera la fertilidad.", "Distingue prolongado de permanente."),
  ],
  rec=[
      ("¿Cada cuánto se toma la píldora anticonceptiva?", "Cada día", "Es un método de uso diario."),
      ("Verdadero o falso: el DIU previene las ITS.", "Falso", "Solo el preservativo lo hace entre los métodos de la lista."),
      ("¿Qué tipo de método son la vasectomía y la ligadura de trompas?", "Quirúrgicos", "Se hacen por intervención y se consideran permanentes."),
  ],
  und=[
      ("Un método que se coloca una vez y protege por años, pero se puede retirar es de: A) Acción prolongada reversible; B) Acción diaria.", "A", "Eso describe al implante y al DIU."),
      ("En una tabla de ejemplo, ¿qué método se usa en cada relación? A) El preservativo; B) El implante.", "A", "Se usa cada vez que hay una relación."),
      ("¿Qué muestra un gráfico de barras de consultas? A) Qué método se consulta más; B) Qué método es mejor.", "A", "Muestra cantidades, no calidad."),
  ],
  app=[
      arith("En 50 consultas de ejemplo, 15 fueron por DIU. ¿Qué porcentaje es?", "15*100//50", "Se divide 15 en 50 y se multiplica por 100."),
      arith("Un cesfam ficticio registra consultas de ejemplo: 14 por píldora, 9 por preservativo y 7 por implante. ¿Cuántas consultas son en total?", "14+9+7", "Se suman las tres cantidades."),
      arith("De 40 consultas de ejemplo, 17 fueron por preservativo y 11 por píldora. ¿Cuántas más fueron por preservativo?", "17-11", "Se restan las dos cantidades."),
  ],
  rea=[
      ("Un gráfico de ejemplo muestra más consultas por píldora que por DIU. Alguien concluye: «La píldora es mejor». ¿Es válido? A) No, solo muestra qué se consulta más; B) Sí.", "A", "Más consultas no significan mejor método."),
      ("Una tabla dice que el implante «protege por años». ¿Qué significa para quien lo usa? A) No debe acordarse cada día, aunque se puede retirar; B) Es permanente.", "A", "Acción prolongada no es permanente."),
  ],
  cha=[
      arith("En 40 consultas de ejemplo, 18 fueron por preservativo y 10 por DIU. ¿Cuál es la diferencia entre ambos porcentajes?", "18*100//40-10*100//40", "Preservativo 45 % y DIU 25 %; se restan."),
      ("Se encuesta a 6 personas de ejemplo y 5 conocen el preservativo. ¿Qué limitación tiene la conclusión? A) Son muy pocas personas para generalizar; B) Ninguna.", "A", "Un grupo pequeño no representa a todas."),
  ],
  context=[("Una matrona ficticia muestra: preservativo 14 consultas, píldora 10, DIU 7, otros 5. ¿Cuántas consultas son en total?", "36", "Se suman las cuatro categorías.", "14+10+7+5")],
  selfcheck=[("¿Qué método se usa en cada relación y previene ITS?", "El preservativo", "Es el único de la lista."), ("¿Se pueden retirar el implante y el DIU?", "Sí", "Son métodos reversibles de acción prolongada."), ("¿Qué gráfico compara cantidades de categorías?", "El de barras", "Se comparan alturas.")],
  open_task=task("Con las consultas de ejemplo: preservativo 16, píldora 12, DIU 8, implante 4 (total 40), calcula el porcentaje de cada método, dibuja un gráfico de barras y escribe una conclusión con una limitación.", "40 %, 30 %, 20 %, 10 %. «El preservativo fue la consulta más frecuente. Son datos de ejemplo y no indican qué método conviene.»", ["calcula los cuatro porcentajes", "gráfico de barras", "limitación declarada"], ["porcentajes, gráfico y conclusión"], ["decir cuál es mejor", "no indicar que son datos de ejemplo"], "Pregunta qué otro dato permitiría saber qué método conviene."),
  reinforce="Completa una tabla con tipo, ITS y reversibilidad para tres métodos.",
  extend="Explica por qué las consultas no miden qué método conviene.")

L(OA5, 3,
  materials=MAT,
  use="Aprenderé un modelo que muestra en qué punto del camino al embarazo actúa cada método y a decidir con criterios, no con opiniones. " + AD3,
  prior=["Conozco ovulación, fecundación e implantación.", "Conozco los tipos de métodos."],
  explain=[
      "El modelo del camino al embarazo tiene tres puntos: la ovulación (el ovario libera un óvulo), el encuentro del espermatozoide con el óvulo (fecundación) y la implantación en el útero. Cada método actúa principalmente en un punto distinto, y eso explica cómo funciona.",
      "Los métodos hormonales actúan en la ovulación: impiden que se libere el óvulo. Los de barrera y los quirúrgicos actúan en el encuentro: el preservativo impide que los espermatozoides lleguen al óvulo; la ligadura de trompas bloquea las trompas, por donde pasa el óvulo; la vasectomía bloquea los conductos por donde viajan los espermatozoides, de modo que el semen no los contiene. El DIU dificulta que los espermatozoides lleguen al óvulo.",
      "El modelo ayuda a comprender, pero tiene límites: no muestra los efectos secundarios, que debe evaluar un profesional, ni la historia de cada persona. Tampoco muestra que los métodos solo funcionan si se usan bien. Para decidir se usan criterios y orientación profesional.",
  ],
  vocab=[("ovulación", "liberación del óvulo desde el ovario"), ("trompa uterina", "conducto por donde pasa el óvulo hacia el útero"), ("conducto deferente", "conducto por donde viajan los espermatozoides"), ("efecto secundario", "efecto adicional no buscado de un tratamiento")],
  worked=[
      ("Ubicar la acción del método", "¿En qué punto del camino actúa el preservativo?", ["El camino tiene ovulación, encuentro y implantación.", "El preservativo impide que los espermatozoides lleguen al óvulo."], "En el encuentro del espermatozoide con el óvulo"),
      ("Usar el modelo para explicar", "¿Por qué un método hormonal que impide la ovulación evita el embarazo?", ["Sin ovulación no hay óvulo.", "Sin óvulo no puede haber fecundación."], "Porque sin óvulo no hay fecundación"),
  ],
  mistakes=[
      ("Decir que todos los métodos actúan igual.", "Actúan en puntos distintos del camino.", "Pregunta: ¿en qué punto actúa este método?"),
      ("Creer que el modelo muestra todos los efectos.", "No muestra efectos secundarios ni historia personal.", "Declara el límite y consulta a un profesional."),
  ],
  rec=[
      ("¿En qué punto del camino actúan los métodos hormonales?", "En la ovulación", "Impiden que se libere el óvulo."),
      ("¿Por dónde pasa el óvulo hacia el útero?", "Por la trompa uterina", "Es el conducto entre el ovario y el útero."),
      ("Verdadero o falso: el preservativo actúa sobre la implantación.", "Falso", "Actúa en el encuentro de las células."),
  ],
  und=[
      ("¿Qué bloquea la ligadura de trompas? A) El paso del óvulo por las trompas; B) La producción de hormonas.", "A", "Impide el encuentro con el espermatozoide."),
      ("En una vasectomía se bloquean los conductos deferentes. ¿Qué efecto tiene? A) El semen no contiene espermatozoides; B) Se deja de producir semen.", "A", "Los espermatozoides ya no salen."),
      ("¿Cómo actúa el DIU en el modelo? A) Dificulta que los espermatozoides lleguen al óvulo; B) Reemplaza al ovario.", "A", "Actúa en el encuentro de las células."),
  ],
  app=[
      ("Un método que impide que se libere el óvulo actúa en: A) La ovulación; B) La implantación.", "A", "Esa es la acción de los hormonales."),
      ("En un ciclo de ejemplo de 28 días, la ovulación ocurre el día 14. ¿Cuántos días después de la ovulación termina el ciclo?", "14", "Se resta 14 de 28.", "28-14"),
      ("Un método de barrera impide el contacto de los espermatozoides con el óvulo. ¿En qué punto del camino actúa? A) En el encuentro; B) En la ovulación.", "A", "Impide el encuentro."),
  ],
  rea=[
      ("Alguien dice: «Si el método hormonal evita la ovulación, nunca hay efectos secundarios». ¿Qué falla? A) El modelo no muestra los efectos secundarios; B) Nada.", "A", "Eso lo evalúa un profesional."),
      ("Un compañero dice que el preservativo evita la ovulación. ¿Qué respondes? A) No, impide el encuentro de las células; B) Tiene razón.", "A", "No actúa sobre el ovario."),
  ],
  cha=[
      ("Un modelo que no muestra que el método debe usarse correctamente, ¿qué límite tiene? A) No indica que el uso incorrecto reduce la protección; B) Ninguno, porque el modelo ya muestra todo.", "A", "El uso correcto es parte de la protección."),
      ("Una persona ficticia quiere un método reversible que no dependa de actuar cada día. ¿Qué tipo conviene revisar con un profesional? A) De acción prolongada, como implante o DIU; B) Quirúrgico.", "A", "Son reversibles y no requieren acción diaria."),
  ],
  context=[("Una estudiante ficticia pregunta a una matrona por qué la ligadura se considera permanente. ¿Cuál es la respuesta correcta? A) Porque bloquea las trompas de forma definitiva; B) Porque se usa en cada relación sexual.", "A", "Es un procedimiento que no se revierte con facilidad.")],
  selfcheck=[("¿Dónde actúan los hormonales?", "En la ovulación", "Impiden liberar el óvulo."), ("¿Qué bloquea la vasectomía?", "Los conductos deferentes", "Por ahí viajan los espermatozoides."), ("Nombra un límite del modelo.", "No muestra los efectos secundarios", "Lo evalúa un profesional.")],
  open_task=task("Dibuja el camino del embarazo (ovulación, encuentro, implantación). Marca con una flecha el punto en que actúa cada uno de estos métodos: preservativo, método hormonal, ligadura de trompas. Escribe un límite del modelo.", "Preservativo: encuentro; hormonal: ovulación; ligadura: encuentro (trompas). Límite: no muestra los efectos secundarios.", ["tres métodos ubicados", "puntos correctos", "límite declarado"], ["esquema con flechas y límite"], ["ubicar hormonales en el encuentro", "no declarar el límite"], "Pregunta qué profesional puede explicar los efectos secundarios."),
  reinforce="Explica con tus palabras en qué punto actúa el DIU.",
  extend="Explica por qué un método quirúrgico se considera permanente.")

L(OA5, 4,
  materials=MAT,
  use="Aprenderé cómo el uso correcto se relaciona con la protección y cómo analizar los elementos de una maternidad y una paternidad responsables con datos. " + AD3,
  prior=["Conozco cómo actúa cada tipo de método.", "Sé que una asociación no prueba una causa."],
  explain=[
      "La protección que da un método depende de su uso correcto y constante. Un método diario, como la píldora, falla más si se olvida; uno de acción prolongada depende menos de la memoria. Si ocurre un olvido o un fallo, como la rotura de un preservativo, se debe consultar pronto a un profesional de salud, porque existen opciones que se deben usar en un plazo breve.",
      "Una maternidad y una paternidad responsables implican una decisión informada y pensada. Algunos elementos: tener la salud necesaria, contar con apoyo, tiempo y recursos para criar, compartir el cuidado entre ambos progenitores, ofrecer afecto y protección, y tener un proyecto de vida propio. Estas decisiones no se juzgan: se planifican.",
      "Los datos permiten comparar situaciones. En un presupuesto de ejemplo, los gastos mensuales de un hijo incluyen alimentación, salud y educación. Calcular cuánto cuesta ayuda a planificar, pero no es lo único que importa: también cuentan el tiempo, el afecto y el apoyo. Ante cualquier duda o presión, se habla con una persona adulta de confianza.",
  ],
  vocab=[("uso correcto", "usar el método como lo indican el envase o el profesional"), ("proyecto de vida", "metas que una persona quiere lograr"), ("planificar", "pensar y organizar con anticipación"), ("corresponsabilidad", "reparto del cuidado entre ambos progenitores")],
  worked=[
      ("Relacionar uso y protección", "Una persona ficticia olvidó la píldora 3 días de un mes de 30. ¿Cuántos días sí la tomó?", ["El mes tiene 30 días.", "Restamos los días de olvido."], "27 días; conviene consultar a un profesional para saber qué hacer"),
      ("Calcular un presupuesto", "Presupuesto mensual de ejemplo: alimentación $60.000 y salud $20.000. ¿Cuánto suman?", ["Se suman los dos gastos.", "60.000 más 20.000 es 80.000."], "$80.000"),
  ],
  mistakes=[
      ("Pensar que la responsabilidad es solo de una persona.", "Ambos progenitores tienen responsabilidad.", "Habla de corresponsabilidad."),
      ("Seguir con el método tras un olvido sin consultar.", "Un olvido puede reducir la protección.", "Consulta pronto a un profesional de salud."),
  ],
  rec=[
      ("Verdadero o falso: el uso correcto y constante influye en la protección.", "Verdadero", "Un uso incorrecto puede reducirla."),
      ("¿Qué debe hacerse ante un olvido de la píldora o la rotura de un preservativo?", "Consultar pronto a un profesional de salud", "Existen opciones con plazo breve."),
      ("Un elemento de la paternidad responsable es: A) Compartir el cuidado; B) Dejar todo a una persona.", "A", "Compartir el cuidado es corresponsabilidad."),
  ],
  und=[
      ("¿Qué método depende menos de recordar algo cada día? A) El de acción prolongada; B) La píldora.", "A", "No requiere una acción diaria."),
      ("¿Qué incluye una maternidad responsable, además de los recursos? A) Salud, apoyo, afecto y tiempo; B) Solo dinero.", "A", "Cuidar implica más que dinero."),
      ("¿Qué se hace al planificar? A) Pensar y organizar con anticipación; B) Esperar a ver qué pasa.", "A", "Planificar es anticipar."),
  ],
  app=[
      arith("Presupuesto mensual de ejemplo: alimentación $90.000, salud $30.000 y educación $50.000. ¿Cuánto suman?", "90000+30000+50000", "Se suman los tres gastos."),
      arith("Si ese presupuesto mensual de ejemplo es de $170.000, ¿cuánto sería en 3 meses?", "170000*3", "Se multiplica por 3."),
      arith("Una persona ficticia anota 28 días de píldora y olvidó 4. ¿Cuántos días sí la tomó?", "28-4", "Se restan los olvidos."),
  ],
  rea=[
      ("Alguien dice: «Con tener el dinero ya basta para ser un padre responsable». ¿Qué falta? A) Tiempo, afecto, apoyo y salud también cuentan; B) Nada.", "A", "La paternidad responsable es más que dinero."),
      ("Un compañero dice: «Si olvido una dosis, no pasa nada». ¿Qué respondes? A) Puede reducir la protección y conviene consultar; B) Tiene razón.", "A", "Un olvido puede reducir la protección."),
  ],
  cha=[
      ("Una pareja ficticia de 16 años recibe una noticia de embarazo. ¿Qué paso es responsable? A) Buscar orientación en el centro de salud y conversar con una persona adulta de confianza; B) Ocultarlo.", "A", "Permite apoyo y decisiones informadas."),
      ("Para comparar el uso constante de dos métodos se registran olvidos. ¿Qué dato falta para concluir? A) Cuántos días se registraron en cada grupo; B) El color de los envases.", "A", "Sin ese dato no se pueden comparar."),
  ],
  context=[("Una familia ficticia anota gastos mensuales de ejemplo de un bebé: $60.000 en alimentación y $15.000 en salud. ¿Cuántos pesos más se gastan en alimentación que en salud?", "45000", "Se restan los dos gastos.", "60000-15000")],
  selfcheck=[("¿Qué debe hacerse tras un olvido del método?", "Consultar pronto a un profesional de salud", "El uso incorrecto puede reducir la protección."), ("¿Qué es la corresponsabilidad?", "Compartir el cuidado entre ambos progenitores", "Ambos progenitores participan en el cuidado."), ("¿Solo importa el dinero?", "No", "Cuentan afecto, tiempo y apoyo.")],
  open_task=task("Con el presupuesto de ejemplo: alimentación $80.000, salud $25.000, educación $45.000, calcula el total mensual y el de 6 meses. Después escribe cuatro elementos que no se miden en pesos de una paternidad o maternidad responsable.", "Total $150.000 al mes y $900.000 en 6 meses. Elementos: afecto, tiempo, apoyo y compartir el cuidado.", ["calcula ambos totales", "cuatro elementos sin dinero", "sin juicios"], ["cálculos y lista"], ["reducir todo al dinero", "juzgar a las personas"], "Pregunta qué apoyo podría ofrecer una persona adulta de confianza."),
  reinforce="Escribe tres elementos de una maternidad o paternidad responsable.",
  extend="Explica por qué un olvido o fallo requiere consultar a un profesional.")

L(OA5, 5,
  materials=MAT,
  use="Aprenderé con evidencia cómo actúan los métodos, por qué los hormonales evitan la ovulación y qué límites tiene la información que circula. " + AD3,
  prior=["Conozco la retroalimentación negativa de las hormonas del ciclo.", "Conozco los puntos de acción de los métodos."],
  explain=[
      "Los métodos hormonales mantienen en la sangre hormonas parecidas a las del ciclo. Por retroalimentación negativa, esos niveles frenan a la hipófisis, que libera menos FSH y LH. Sin el pico de LH no hay ovulación, y sin óvulo no hay fecundación. Además, algunas hormonas espesan el moco del cuello del útero y dificultan el paso de los espermatozoides.",
      "El preservativo es una barrera física: impide que los espermatozoides lleguen al óvulo y reduce el contacto con fluidos que pueden contener agentes de las ITS. La vasectomía y la ligadura de trompas bloquean conductos. Ninguno de los métodos es perfecto, y solo no tener relaciones sexuales evita por completo el embarazo; por eso la información debe ser clara y el uso, correcto.",
      "Para evaluar evidencia, se pregunta quién la escribe, si se puede verificar y qué dicen las fuentes de salud. Las redes pueden difundir mitos, como creer que un método natural es igual de fiable que otro. Si algo parece dudoso o se recibe presión, se conversa con un profesional de salud o con una persona adulta de confianza.",
  ],
  vocab=[("retroalimentación negativa", "mecanismo en que un exceso de hormona frena su propia producción"), ("barrera física", "obstáculo material que impide el paso"), ("moco cervical", "secreción del cuello del útero"), ("mito", "creencia sin evidencia que se repite")],
  worked=[
      ("Explicar con retroalimentación", "¿Cómo evita la ovulación un método hormonal?", ["Mantiene hormonas en la sangre.", "Eso frena la hipófisis, baja la FSH y la LH y no hay pico de LH."], "Sin pico de LH no hay ovulación"),
      ("Evaluar un mito", "Un mensaje dice: «El método del calendario es tan fiable como los demás». ¿Qué conviene hacer?", ["Reviso quién lo dice y si cita fuentes de salud.", "Los métodos naturales exigen constancia y son menos fiables."], "Dudar del mensaje y consultar a un profesional"),
  ],
  mistakes=[
      ("Decir que un método hormonal funciona porque mata espermatozoides.", "Actúa sobre la ovulación y el moco, no por daño directo a las células.", "Recuerda: frena la hipófisis."),
      ("Creer cualquier mensaje de redes sobre métodos.", "Puede contener mitos.", "Verifica con fuentes de salud."),
  ],
  rec=[
      ("¿Qué glándula frenan los niveles de hormona en la sangre por retroalimentación negativa?", "La hipófisis", "Libera menos FSH y LH."),
      ("Verdadero o falso: el preservativo es una barrera física.", "Verdadero", "Impide que los espermatozoides lleguen al óvulo."),
      ("¿Qué hormona hipofisaria provoca la ovulación? A) La LH; B) La prolactina.", "A", "Su pico desencadena la ovulación."),
  ],
  und=[
      ("¿Qué ocurre con la FSH y la LH cuando un método hormonal frena a la hipófisis? A) Disminuyen; B) Aumentan.", "A", "Se libera menos."),
      ("¿Por qué el preservativo ayuda a reducir las ITS? A) Reduce el contacto con fluidos; B) Elimina bacterias de la persona.", "A", "Actúa como barrera."),
      ("¿Qué hace el moco espesado del cuello del útero? A) Dificulta el paso de los espermatozoides; B) Aumenta la ovulación.", "A", "Es otro efecto de algunas hormonas."),
  ],
  app=[
      ("Datos de ejemplo: con un método hormonal, la LH no alcanza su pico. ¿Qué evento no ocurre? A) La ovulación; B) La menstruación.", "A", "El pico de LH desencadena la ovulación."),
      arith("Una persona ficticia toma una pastilla diaria durante 21 días de un ciclo de ejemplo de 28 días. ¿Cuántos días del ciclo no toma pastilla?", "28-21", "Se restan los días con pastilla."),
      ("Un mensaje dice «este método es 100 % seguro sin consultar a nadie». ¿Qué conviene? A) Dudar y verificar con un profesional; B) Compartirlo.", "A", "Ningún método es perfecto y requiere orientación."),
  ],
  rea=[
      ("Un compañero dice: «Si es hormonal, funciona aunque se olvide». ¿Qué respondes? A) El olvido puede permitir la ovulación y conviene consultar; B) Tiene razón.", "A", "La protección depende del uso correcto."),
      ("Alguien afirma: «Solo importa el método, no el uso». ¿Qué falla? A) El uso correcto y constante es parte de la protección; B) Nada.", "A", "Un mal uso reduce la protección."),
  ],
  cha=[
      ("Dos mensajes ficticios se contradicen sobre un método. ¿Qué haces? A) Contrastar con una fuente de salud verificable; B) Elegir el más entretenido.", "A", "Contrastar reduce errores."),
      ("Una estudiante ficticia sospecha que podría estar embarazada. ¿Qué paso es responsable? A) Acudir pronto a un centro de salud y conversar con una persona adulta de confianza; B) Esperar sin avisar a nadie.", "A", "Un profesional puede orientar a tiempo."),
  ],
  context=[("Un liceo ficticio organiza una charla con una matrona. ¿Qué evidencia es más confiable para preparar preguntas? A) Orientaciones de salud pública y profesionales; B) Un mensaje anónimo viral.", "A", "Se puede verificar.")],
  selfcheck=[("¿Qué evita la ovulación en un método hormonal?", "Menor FSH y LH por retroalimentación negativa", "Sin pico de LH no hay ovulación."), ("¿Qué hace el preservativo?", "Impide que los espermatozoides lleguen al óvulo", "Es una barrera física."), ("¿Qué haces ante un mensaje dudoso?", "Lo verifico con una fuente de salud", "Así se evitan mitos.")],
  open_task=task("Explica en cuatro oraciones cómo un método hormonal evita el embarazo, usando las palabras hipófisis, FSH, LH y ovulación. Añade una oración sobre por qué hay que consultar a un profesional ante un olvido.", "La hormona del método frena la hipófisis. Baja la FSH y la LH. Sin pico de LH no hay ovulación. Sin óvulo no hay fecundación. Ante un olvido se consulta porque puede reducirse la protección.", ["usa las cuatro palabras", "explica el orden", "incluye la consulta"], ["párrafo de cinco oraciones"], ["decir que mata espermatozoides", "omitir la consulta"], "Pregunta qué cambiaría si el pico de LH ocurriera."),
  reinforce="Escribe en orden los pasos con que un método hormonal evita la ovulación.",
  extend="Explica por qué la información sobre métodos debe verificarse.")
