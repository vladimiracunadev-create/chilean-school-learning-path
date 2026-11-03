"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 07 (evidencia y decisiones para una vida saludable)."""
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


OA7 = "CN08 OA 07"

L(OA7, 1,
  materials="Este cuaderno y lápiz. Opcional: un reloj con segundero para medir tu pulso. Marchar en el lugar solo si no tienes indicación médica contraria, sin saltos y con una persona de tu casa cerca.",
  use="Aprenderé qué factores sostienen un cuerpo saludable y a formular preguntas investigables sobre ellos. Sirve para decidir con datos y no solo con opiniones.",
  prior=["Sé qué hacen los sistemas circulatorio y respiratorio.", "Sé que una pregunta investigable se contesta con mediciones."],
  explain=[
      "Un cuerpo saludable depende de varios factores que se pueden analizar con evidencia. En este tema se estudian tres: una alimentación balanceada (variada y en cantidades adecuadas), un ejercicio físico regular y evitar el consumo de alcohol, tabaco y drogas. Un plan de vida saludable combina los tres y se evalúa con datos.",
      "Para decidir con evidencia hay que preguntar de forma investigable. «¿Cuántos latidos por minuto aumenta el pulso después de marchar 2 minutos en el lugar?» es investigable, porque se mide. «¿Cuál deporte es más divertido?» no lo es, porque depende de gustos. El pulso se puede estimar contando los latidos en 15 segundos y multiplicando por 4.",
      "En una pregunta investigable se identifican las variables. Se cambia la actividad (reposo o marcha), se mide el pulso y se mantiene igual la duración y la persona. Medir antes y después a la misma persona hace la comparación más justa. La evidencia mejora si se repite la medición y se promedia.",
  ],
  vocab=[("vida saludable", "estilo de vida que cuida el cuerpo, con alimentación, ejercicio y sin consumo de sustancias dañinas"), ("pulso", "latidos del corazón que se sienten en una arteria"), ("alimentación balanceada", "variada y en cantidades adecuadas a cada persona"), ("evidencia", "datos medidos u observados que se pueden comprobar"), ("variable", "dato que cambia o se mide")],
  worked=[
      ("Calcular el pulso", "Una persona cuenta 19 latidos en 15 segundos. ¿Cuántos latidos por minuto tiene?", ["Un minuto tiene 4 veces 15 segundos.", "19 × 4 = 76."], "76 latidos por minuto"),
      ("Pregunta investigable", "¿Es investigable «¿Sube el pulso al marchar 2 minutos?»?", ["Pregunto si se mide.", "Se puede contar el pulso antes y después."], "Sí, porque se mide el pulso"),
  ],
  mistakes=[
      ("Contestar con opiniones una pregunta de salud.", "La opinión no se puede comprobar.", "Convierte la pregunta en una que se pueda medir."),
      ("Comparar personas distintas en vez de la misma antes y después.", "Cada persona tiene un pulso de reposo distinto.", "Mide a la misma persona en dos momentos."),
  ],
  rec=[
      ("Nombra los tres factores del plan de vida saludable que se estudian.", "Alimentación balanceada, ejercicio regular y evitar alcohol, tabaco y drogas", "Son los tres que nombra el objetivo."),
      arith("Una persona cuenta 20 latidos en 15 segundos. ¿Cuántos latidos por minuto tiene?", "20*4", "Un minuto equivale a 4 veces 15 segundos."),
      ("Verdadero o falso: «¿Cuál deporte es más divertido?» es una pregunta investigable.", "Falso", "Depende de gustos y no se puede medir."),
  ],
  und=[
      ("¿Cuál pregunta es investigable? A) ¿Cuánto sube el pulso tras marchar 2 minutos en el lugar? B) ¿Es mejor vivir sin hacer ejercicio?", "A", "Se responde midiendo el pulso."),
      ("En «¿Cambia el pulso después de marchar 2 minutos?», ¿qué variable se mide?", "El pulso", "Es el resultado que se registra."),
      ("¿Por qué se mide el pulso en reposo antes del ejercicio? A) Para tener un valor con el cual comparar; B) Para comprobar si la persona está enferma antes de empezar.", "A", "Sin el valor inicial no se puede ver el cambio."),
  ],
  app=[
      arith("En reposo una persona cuenta 22 latidos en 15 segundos y después de marchar cuenta 36. ¿Cuántos latidos por minuto aumentó?", "(36-22)*4", "Se calcula la diferencia en 15 segundos y se multiplica por 4."),
      arith("Datos de ejemplo: el pulso aumentó 40, 50 y 60 latidos por minuto en tres personas. ¿Cuál fue el aumento promedio?", "(40+50+60)//3", "Se suman los aumentos y se divide por 3."),
      ("Para que la comparación sea justa, ¿qué debe mantenerse igual? A) La duración de la marcha para todas las personas; B) El pulso de cada una.", "A", "El pulso es lo que se mide."),
  ],
  rea=[
      ("Alguien dice: «Mi pulso subió mucho al marchar, estoy enfermo». ¿Qué corrección haces? A) Es normal que el pulso suba con el ejercicio; B) El pulso nunca debe cambiar.", "A", "El corazón late más rápido para llevar oxígeno."),
      ("Un grupo mide el pulso de una persona que acaba de correr y de otra en reposo, y concluye que el ejercicio no importa. ¿Cuál sería una prueba mejor? A) Medir a la misma persona antes y después; B) Medir a personas distintas.", "A", "Se evita el efecto de las diferencias entre personas."),
  ],
  cha=[
      ("¿Cuál es la mejor forma investigable de «¿El ejercicio hace bien?»? A) ¿Cuánto baja el pulso en reposo de un grupo después de 4 semanas de actividad regular? B) ¿Es lindo hacer ejercicio?", "A", "Indica qué se mide y en cuánto tiempo."),
      arith("Un pulso en reposo de 72 latidos por minuto sube a 120 con la marcha. ¿Cuántos latidos por minuto aumentó?", "120-72", "Se resta el pulso de reposo al de marcha."),
  ],
  context=[arith("Una persona de ejemplo cuenta 17 latidos en 15 segundos en reposo. ¿Cuántos latidos por minuto tiene?", "17*4", "Se multiplica por 4.")],
  selfcheck=[("¿Qué hace investigable a una pregunta de salud?", "Que se puede responder midiendo", "No depende de opiniones."), ("¿Cómo se estima el pulso por minuto?", "Contando los latidos en 15 segundos y multiplicando por 4", "Un minuto tiene cuatro veces 15 segundos."), ("¿Por qué medir antes y después en la misma persona?", "Para comparar de forma justa", "Cada persona tiene un pulso de reposo propio.")],
  open_task=task("Plantea una pregunta investigable sobre el efecto de marchar en el lugar en el pulso. Escribe la variable que cambias, la que mides, tres que mantienes iguales y una predicción. Añade una medida de seguridad.", "Pregunta: ¿Cuántos latidos por minuto sube el pulso tras marchar 2 minutos en el lugar? Cambio: reposo o marcha. Mido: pulso. Igual: persona, duración, hora. Predicción: sube. Seguridad: sin saltos y con una persona adulta cerca.", ["pregunta con variable medida", "tres variables controladas", "seguridad"], ["plan breve"], ["pregunta de opinión", "no controlar la duración"], "Pregunta qué cambiaría si la marcha durara 4 minutos."),
  reinforce="Calcula el pulso por minuto si cuentas 18 latidos en 15 segundos.",
  extend="Explica por qué medir antes y después en la misma persona es una prueba más justa.")

L(OA7, 2,
  materials="Este cuaderno y lápiz. Los estudios y tablas son inventados y de ejemplo.",
  use="Aprenderé a examinar evidencia sobre hábitos saludables: leer tablas, distinguir asociación de causa y evaluar la confiabilidad de una fuente. Sirve para no creer cualquier afirmación sobre salud.",
  prior=["Sé formular preguntas investigables.", "Sé calcular porcentajes."],
  explain=[
      "Para evaluar una afirmación de salud se mira la evidencia. Primero, la fuente: es más confiable un organismo de salud o un estudio publicado que un comentario en una red social. Segundo, el tamaño de la muestra: más personas dan más confianza. Tercero, si el resultado se repite en otros estudios.",
      "Una asociación indica que dos cosas ocurren juntas, pero no prueba que una cause la otra. Estudio de ejemplo: de 100 estudiantes que hacen 60 minutos o más de actividad al día, 80 dicen tener energía en clases; de 100 que hacen menos, 55. La diferencia es 25 puntos. Puede ser que la actividad dé energía, pero también que quienes duermen más hagan más deporte; esa otra variable se llama factor de confusión.",
      "Una conclusión prudente dice «se asocia con» y declara una limitación. Por ejemplo: «Hacer más actividad se asocia con sentirse con más energía; el estudio no controló las horas de sueño». Así se evita exagerar. La evidencia fuerte viene de varios estudios, con muestras grandes y variables controladas.",
  ],
  vocab=[("asociación", "relación entre dos variables que ocurren juntas"), ("causa", "factor que produce un efecto"), ("factor de confusión", "variable no controlada que puede explicar un resultado"), ("fuente confiable", "origen de información respaldado por métodos y expertos"), ("tamaño de la muestra", "número de personas del estudio")],
  worked=[
      ("Comparar porcentajes", "En un estudio de ejemplo, 70 de 100 estudiantes activos y 45 de 100 menos activos dicen sentirse con energía. ¿Cuántos puntos porcentuales de diferencia hay?", ["Cada grupo tiene 100 personas.", "70 − 45 = 25."], "25 puntos porcentuales"),
      ("Asociación o causa", "¿El estudio anterior prueba que la actividad produce energía?", ["Muestra una asociación.", "Puede haber otras variables, como las horas de sueño."], "No, solo muestra una asociación"),
  ],
  mistakes=[
      ("Concluir causa a partir de una asociación.", "Puede haber factores de confusión.", "Usa «se asocia con»."),
      ("Fiarse de una fuente por ser popular.", "La popularidad no prueba que sea cierta.", "Revisa quién la hizo y con qué datos."),
  ],
  rec=[
      ("¿Qué fuente es más confiable: un organismo de salud o un comentario anónimo en una red social?", "Un organismo de salud", "Su información se basa en revisión de evidencia."),
      ("¿Un tamaño de muestra mayor da más o menos confianza?", "Más confianza", "Reduce el efecto del azar."),
      ("Verdadero o falso: una asociación prueba por sí sola una causa.", "Falso", "Puede haber otros factores."),
  ],
  und=[
      ("¿Qué es un factor de confusión? A) Una variable no controlada que puede explicar el resultado; B) El resultado principal que mide el estudio.", "A", "Mezcla su efecto con el de la variable que se estudia."),
      ("¿Cuál es una conclusión prudente? A) La actividad se asocia con más energía; B) La actividad siempre da energía a todos.", "A", "Evita generalizar a todos los casos."),
      ("Un estudio tiene solo 6 personas. ¿Qué limitación tiene?", "La muestra es muy pequeña", "Con pocas personas el azar pesa mucho."),
  ],
  app=[
      arith("Estudio de ejemplo: 85 de 100 estudiantes con buen sueño y 58 de 100 con poco sueño dicen sentirse con energía. ¿Cuántos puntos porcentuales de diferencia hay?", "85-58", "Se resta el porcentaje menor al mayor."),
      arith("En otro estudio de ejemplo, 36 de 50 estudiantes activos tienen buen ánimo. ¿Qué porcentaje es?", "36*100//50", "Se divide por el total y se multiplica por 100.", " %"),
      ("Dos fuentes dicen cosas distintas: un folleto del consultorio y un video sin autor. ¿Cuál conviene revisar primero? A) El folleto del consultorio; B) El video sin autor.", "A", "Tiene una fuente identificable y respaldo de salud."),
  ],
  rea=[
      ("Alguien concluye: «Los que desayunan sacan mejores notas, entonces el desayuno sube las notas». ¿Qué falla ve? A) Podría haber otras variables, como el sueño o la rutina; B) No existen notas.", "A", "La asociación no prueba una causa."),
      ("Un estudio de ejemplo no dice cuántas personas participaron. ¿Por qué es un problema?", "No se puede saber si la muestra es suficiente", "Sin el tamaño de la muestra no se evalúa su confiabilidad."),
  ],
  cha=[
      ("Un estudio de ejemplo encuentra que quienes comen más frutas tienen menos resfríos. Otro estudio, con la misma pregunta y más personas, encuentra lo mismo. ¿Qué pasa con la confianza en el resultado? A) Aumenta porque se repitió; B) Disminuye porque se repitió.", "A", "La repetición con otra muestra refuerza la conclusión."),
      ("Escribe una conclusión prudente para el estudio de la actividad y la energía (80 de 100 frente a 55 de 100) con una limitación.", "La actividad se asocia con más energía; el estudio no controló las horas de sueño", "Se usa «se asocia» y se declara qué no se controló."),
  ],
  context=[("Una persona de ejemplo lee en una red social: «Este té quema la grasa en 3 días». No hay fuente ni datos. ¿Qué debe hacer primero? A) Buscar información en una fuente de salud confiable; B) Compartirla con su curso.", "A", "Hay que revisar la evidencia antes de creerla o compartirla.")],
  selfcheck=[("¿Qué es una asociación?", "Una relación entre dos variables que ocurren juntas", "No prueba una causa."), ("¿Qué es un factor de confusión?", "Una variable no controlada que puede explicar el resultado", "Puede alterar la conclusión."), ("¿Qué hace más confiable una fuente?", "Datos, método y expertos que la respaldan", "No la popularidad.")],
  open_task=task("Lee esta afirmación inventada: «Un estudio con 40 personas encontró que 30 de las que toman más agua se sienten con más energía y 20 de las que toman menos». Calcula los porcentajes si cada grupo tiene 40 personas, escribe una conclusión prudente y dos limitaciones.", "Más agua: 30 de 40 = 75 %. Menos agua: 20 de 40 = 50 %. Conclusión: tomar más agua se asocia con sentir más energía. Limitaciones: muestra pequeña y no se controlaron otras variables, como el sueño.", ["dos porcentajes correctos", "conclusión con «se asocia»", "dos limitaciones"], ["cálculos y conclusión"], ["afirmar causa", "no calcular los porcentajes"], "Pregunta qué dato nuevo te daría más confianza."),
  reinforce="Escribe una razón por la que una fuente puede ser poco confiable.",
  extend="Explica con un ejemplo por qué asociación y causa no son lo mismo.")

L(OA7, 3,
  materials="Este cuaderno y lápiz. Los planes y las tablas son de ejemplo.",
  use="Aprenderé a construir y contrastar un modelo de plan de vida saludable que combine alimentación, ejercicio y evitar sustancias. Sirve para evaluar si un plan cumple recomendaciones.",
  prior=["Sé qué es una alimentación balanceada.", "Sé comparar datos con una meta."],
  explain=[
      "Un plan de vida saludable es un modelo: una representación simplificada de hábitos para un periodo, como una semana. Un buen plan es específico (dice qué, cuánto y cuándo), medible y realista. Debe incluir los tres factores: alimentación balanceada, ejercicio regular y evitar alcohol, tabaco y drogas.",
      "Las recomendaciones internacionales para personas de 5 a 17 años indican, en promedio, al menos 60 minutos al día de actividad física de moderada a vigorosa. En una semana son 7 × 60 = 420 minutos. También se recomienda comer frutas y verduras varias veces al día, tomar agua y evitar el consumo de alcohol, tabaco y drogas. En Chile está prohibido vender alcohol y tabaco a menores de 18 años.",
      "Contrastar un plan es compararlo con la meta. Un plan con 300 minutos semanales no llega a 420: le faltan 120. Un plan con 450 sí cumple. Todo plan tiene límites: no considera enfermedades, gustos ni los cambios de cada semana, y debe ajustarse. Las personas con una condición de salud deben consultar a un profesional antes de cambiar su actividad.",
  ],
  vocab=[("plan", "conjunto de acciones organizadas para lograr una meta"), ("específico", "que dice qué, cuánto y cuándo"), ("medible", "que se puede contar o comparar con una meta"), ("actividad moderada a vigorosa", "ejercicio que acelera la respiración y el pulso"), ("meta semanal", "cantidad que se quiere lograr en siete días")],
  worked=[
      ("Cumplir la meta", "Un plan suma 30 min de caminata de lunes a viernes. ¿Cumple 420 minutos semanales?", ["30 × 5 = 150 minutos.", "150 es menor que 420."], "No cumple; le faltan 270 minutos"),
      ("Plan específico", "¿Cuál es más específico: «hacer más ejercicio» o «caminar rápido 40 minutos los martes, jueves y sábado»?", ["Reviso si dice qué, cuánto y cuándo.", "El segundo dice qué, cuánto y cuándo."], "El segundo"),
  ],
  mistakes=[
      ("Hacer un plan solo de ejercicio.", "Debe incluir alimentación y evitar sustancias.", "Revisa los tres factores."),
      ("Creer que un plan sirve igual para todas las personas.", "Cada persona tiene necesidades distintas.", "Ajusta el plan y consulta si hay una condición de salud."),
  ],
  rec=[
      arith("¿Cuántos minutos son 60 minutos diarios durante 7 días?", "60*7", "Se multiplica por los siete días de la semana."),
      ("¿A qué edad está prohibido vender alcohol y tabaco en Chile: a menores de 18 o a menores de 12?", "Menores de 18", "Es la edad legal para comprarlos."),
      ("Verdadero o falso: un plan específico dice qué, cuánto y cuándo.", "Verdadero", "Así se puede evaluar si se cumplió."),
  ],
  und=[
      ("¿Cuál es un plan medible? A) Trotar 20 minutos el lunes y el jueves; B) Hacer más ejercicio un día de estos.", "A", "Tiene cantidad y días."),
      ("¿Qué tres factores debe incluir un plan de vida saludable?", "Alimentación balanceada, ejercicio regular y evitar alcohol, tabaco y drogas", "Son los tres factores del objetivo."),
      ("¿Por qué un plan es un modelo con límites? A) Porque no considera todos los cambios de cada semana; B) Porque no se puede escribir.", "A", "Simplifica la realidad."),
  ],
  app=[
      arith("Un plan suma 45 minutos de actividad los lunes, miércoles, viernes y sábado. ¿Cuántos minutos suma en la semana?", "45*4", "Son 4 días de 45 minutos."),
      arith("Un plan suma 350 minutos semanales. ¿Cuántos minutos le faltan para llegar a 420?", "420-350", "Se resta lo que tiene a la meta."),
      ("Un menú de ejemplo incluye pan, mantequilla y bebida azucarada en todas las comidas. ¿Qué factor del plan falla? A) La alimentación balanceada; B) Evitar el tabaco.", "A", "Falta variedad de verduras, frutas y proteínas."),
  ],
  rea=[
      ("Dos planes: P1 suma 450 minutos de actividad y no incluye verduras; P2 suma 300 minutos e incluye verduras. ¿Cuál cumple mejor la meta de actividad? Escribe P1 o P2.", "P1", "450 supera los 420 minutos."),
      ("Un compañero dice: «Mi plan es perfecto porque nunca lo cambiaré». ¿Qué corrección haces? A) Un plan debe ajustarse según los cambios y la evidencia; B) Un plan no puede cambiar.", "A", "Es un modelo y se revisa."),
  ],
  cha=[
      ("Un plan de ejemplo dice: «No tomar alcohol; si me presionan, me alejo y aviso a una persona adulta de confianza». ¿Qué fortaleza tiene? A) Incluye una acción concreta; B) Es solo una opinión.", "A", "Dice qué hacer ante la presión."),
      arith("Un plan de ejemplo reparte 420 minutos en 6 días iguales y descansa 1 día. ¿Cuántos minutos hay cada día de actividad?", "420//6", "Se divide la meta entre los días de actividad."),
  ],
  context=[arith("Una estudiante de ejemplo hizo 55 minutos de actividad el lunes, 65 el martes y 60 el miércoles. ¿Cuántos minutos acumuló en los tres días?", "55+65+60", "Se suman los minutos de cada día.")],
  selfcheck=[("¿Cuántos minutos semanales equivalen a 60 diarios?", "420", "60 × 7."), ("¿Qué hace un plan específico?", "Dice qué, cuánto y cuándo", "Así permite evaluarlo después."), ("¿Por qué ajustar un plan?", "Porque cambian las necesidades y la evidencia", "Es un modelo.")],
  open_task=task("Diseña un plan de una semana con tres partes: (1) tabla de actividad física por día con minutos y suma; (2) tres reglas de alimentación balanceada; (3) una acción concreta para evitar alcohol, tabaco y drogas, incluyendo a quién avisarías si te presionan. Compara tu suma con 420 minutos.", "Lunes 60, martes 60, miércoles 60, jueves 60, viernes 60, sábado 90, domingo 40: suma 430, cumple. Alimentación: verduras en el almuerzo, agua, fruta en vez de dulces. Evitar sustancias: decir no, alejarme y avisar a una persona adulta de confianza.", ["tabla con suma", "tres reglas de alimentación", "acción concreta y persona adulta de confianza"], ["plan escrito"], ["no sumar los minutos", "olvidar la acción ante la presión"], "Pregunta qué cambiarías si una semana no puedes entrenar."),
  reinforce="Escribe un objetivo de actividad que sea específico y medible.",
  extend="Explica por qué un plan debe ajustarse con el tiempo.")

L(OA7, 4,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo.",
  use="Aprenderé a relacionar variables de hábitos saludables: intensidad del ejercicio y pulso, tiempo de pantalla y actividad, y cantidad de agua. Sirve para analizar tablas y sacar conclusiones con datos.",
  prior=["Sé calcular el pulso y promedios.", "Sé que una asociación no prueba causa."],
  explain=[
      "Las variables de un hábito se pueden relacionar con una tabla. A mayor intensidad del ejercicio, mayor pulso. Datos de ejemplo: en reposo, 70 latidos por minuto; caminar, 95; trotar, 130; correr, 160. La relación es creciente: al aumentar la intensidad, sube el pulso. Con la práctica regular, el corazón se hace más eficiente y el pulso en reposo tiende a bajar.",
      "Otra relación es el tiempo de pantalla y la actividad física. En un registro de ejemplo de cinco estudiantes, quienes pasan más horas frente a pantallas hacen menos minutos de actividad. Es una relación decreciente: al aumentar una variable, la otra baja. Una relación no prueba causa, pero ayuda a plantear una pregunta.",
      "Para analizar una tabla se ordenan los datos, se calculan promedios o diferencias y se describe el patrón con palabras: «aumenta», «disminuye» o «no cambia». Después se escribe una limitación, por ejemplo: «son pocos estudiantes». También se puede calcular cuánto cambia una variable por cada paso de la otra.",
  ],
  vocab=[("relación creciente", "cuando una variable aumenta, la otra también"), ("relación decreciente", "cuando una variable aumenta, la otra disminuye"), ("intensidad", "qué tan exigente es el ejercicio"), ("tiempo de pantalla", "horas frente a celulares, computadores o televisión"), ("patrón", "regularidad que se ve en los datos")],
  worked=[
      ("Describir el patrón", "Datos de ejemplo: caminar 90, trotar 120, correr 150 latidos por minuto. ¿Qué patrón hay entre intensidad y pulso?", ["Al pasar de caminar a trotar sube.", "Al pasar de trotar a correr vuelve a subir."], "Relación creciente: a mayor intensidad, mayor pulso"),
      ("Calcular un aumento", "El pulso en reposo es 66 y al trotar 126. ¿Cuántos latidos por minuto aumentó?", ["Resto 126 − 66.", "126 − 66 = 60."], "60 latidos por minuto"),
  ],
  mistakes=[
      ("Decir que la relación es creciente cuando una variable baja.", "Creciente significa que ambas suben.", "Observa qué hace cada variable."),
      ("Concluir que la pantalla causa la inactividad solo con una tabla.", "La tabla muestra una relación, no una causa.", "Declara la limitación."),
  ],
  rec=[
      ("Si al aumentar la intensidad sube el pulso, la relación es ______ (creciente o decreciente).", "Creciente", "Ambas variables suben."),
      ("¿Qué pasa con el pulso en reposo con práctica regular de ejercicio: tiende a subir o a bajar?", "A bajar", "El corazón se hace más eficiente."),
      ("Verdadero o falso: una relación decreciente significa que una variable sube y la otra baja.", "Verdadero", "Así se define."),
  ],
  und=[
      ("En una tabla, a más horas de pantalla hay menos minutos de actividad. ¿Qué relación es? A) Decreciente; B) Creciente.", "A", "Una variable sube y la otra baja."),
      ("¿Cuál es una limitación de un registro con solo 5 estudiantes? A) La muestra es pequeña; B) Los estudiantes no se mueven.", "A", "Con pocos datos, el resultado puede ser azaroso."),
      ("¿Por qué un corazón entrenado puede latir menos veces en reposo?", "Porque bombea más sangre en cada latido", "Es más eficiente."),
  ],
  app=[
      arith("Datos de ejemplo: el pulso es 70 en reposo y 160 al correr. ¿Cuántos latidos por minuto aumenta?", "160-70", "Se resta el valor de reposo al de correr."),
      arith("Cinco estudiantes de ejemplo hicieron 40, 50, 60, 70 y 80 minutos de actividad. ¿Cuál es el promedio?", "(40+50+60+70+80)//5", "Se suman y se divide por 5."),
      arith("Un estudiante de ejemplo pasa 3 horas diarias frente a pantallas durante 7 días. ¿Cuántas horas son en la semana?", "3*7", "Se multiplican las horas diarias por 7."),
  ],
  rea=[
      ("Una tabla de ejemplo muestra que quienes toman más agua hacen más ejercicio. Alguien concluye que el agua causa más ejercicio. ¿Qué corrección haces? A) Puede ser asociación y haber otros factores; B) El agua da energía por sí sola.", "A", "Una relación no prueba una causa."),
      ("Explica en una frase cómo se ve una relación decreciente en una tabla.", "Una variable sube mientras la otra baja", "Los valores se mueven en sentidos opuestos."),
  ],
  cha=[
      ("Datos de ejemplo de cinco estudiantes: pantalla (h) 1, 2, 3, 4, 5; actividad (min) 90, 75, 60, 45, 30. ¿Cuántos minutos baja la actividad por cada hora más de pantalla?", "15", "Cada hora más baja 15 minutos.", "90-75"),
      ("Con esos datos de ejemplo, ¿cuántos minutos de actividad se esperarían con 6 horas de pantalla si el patrón continúa? Responde con el número.", "15", "30 − 15 = 15 minutos.", "30-15"),
  ],
  context=[("Un curso de ejemplo mide el pulso antes y después de una clase de Educación Física: antes 80 y después 120, en promedio. ¿Cuántos latidos por minuto aumentó el pulso promedio?", "40", "120 − 80 = 40.", "120-80")],
  selfcheck=[("¿Qué es una relación creciente?", "Cuando una variable aumenta y la otra también", "Las dos variables suben juntas."), ("¿Qué pasa con el pulso al aumentar la intensidad?", "Sube", "El corazón envía más oxígeno."), ("¿Qué limitación tienen los registros con pocos datos?", "Pueden no representar a los demás", "Hay que repetir con más personas.")],
  open_task=task("Con estos datos de ejemplo de cinco personas (horas de pantalla y minutos de actividad: 1 h-80 min; 2 h-70 min; 3 h-55 min; 4 h-40 min; 5 h-30 min) calcula los promedios de ambas variables, describe la relación con palabras y escribe una limitación.", "Promedio de pantalla: 3 h. Promedio de actividad: (80 + 70 + 55 + 40 + 30) ÷ 5 = 55 min. Relación decreciente: a más pantalla, menos actividad. Limitación: son solo cinco personas y no se sabe por qué.", ["dos promedios correctos", "relación decreciente", "una limitación"], ["cálculos y frase"], ["llamar creciente a la relación", "afirmar causa"], "Pregunta qué dato agregarías a la tabla."),
  reinforce="Calcula el aumento del pulso entre 72 en reposo y 118 al trotar.",
  extend="Explica por qué una relación en una tabla puede ayudar a formular una pregunta pero no prueba causa.")

L(OA7, 5,
  materials="Este cuaderno y lápiz. Los casos son inventados y no corresponden a nadie real. Si alguien te presiona a consumir o algo te preocupa, cuéntaselo a una persona adulta de confianza.",
  use="Aprenderé el mecanismo por el cual el ejercicio, la alimentación y el consumo de alcohol, tabaco y drogas afectan el cuerpo, y a decidir con evidencia. Sirve para tomar decisiones informadas y saber qué hacer ante la presión.",
  prior=["Sé qué sistemas del cuerpo se afectan con el tabaco y el alcohol.", "Sé interpretar asociaciones."],
  explain=[
      "El ejercicio fortalece el corazón y los músculos, ayuda a mantener huesos fuertes y mejora el ánimo. La alimentación balanceada aporta la energía y los nutrientes para el crecimiento. Evitar tabaco, alcohol y drogas protege los órganos y el cerebro, que en la adolescencia sigue desarrollándose.",
      "El tabaco contiene nicotina, que genera dependencia, y monóxido de carbono, que se une a la hemoglobina y reduce el oxígeno que lleva la sangre. El alcohol deprime el sistema nervioso, altera el juicio y la coordinación, y daña el hígado con el uso excesivo. Las drogas alteran el sistema de recompensa del cerebro y pueden generar dependencia. Estas sustancias son especialmente riesgosas durante el crecimiento.",
      "Decidir con evidencia es elegir lo que la información respalda. Si alguien presiona a consumir, lo correcto es decir que no, alejarse y avisar a una persona adulta de confianza, como una persona de la familia, un docente o la orientadora. No es culpa de quien recibe la presión. Hablar con una persona adulta de confianza es una conducta valiente y segura.",
  ],
  vocab=[("dependencia", "necesidad de seguir consumiendo una sustancia"), ("nicotina", "sustancia del tabaco que genera dependencia"), ("monóxido de carbono", "gas del humo que reduce el oxígeno transportado por la sangre"), ("sistema de recompensa", "parte del cerebro que asocia una sensación con un placer"), ("presión de grupo", "influencia de otras personas para que alguien haga algo")],
  worked=[
      ("Mecanismo del monóxido de carbono", "¿Por qué el monóxido de carbono del humo del tabaco es dañino?", ["Se une a la hemoglobina.", "Así la sangre lleva menos oxígeno."], "Porque reduce el oxígeno que lleva la sangre"),
      ("Frente a la presión", "Alguien te ofrece cigarrillos en una fiesta. ¿Qué haces?", ["Digo que no con claridad.", "Me alejo y aviso a una persona adulta de confianza."], "Decir que no, alejarse y avisar a una persona adulta de confianza"),
  ],
  mistakes=[
      ("Creer que consumir una vez no tiene riesgo.", "Algunas sustancias generan dependencia y afectan el cerebro en desarrollo.", "Elige no consumir y busca ayuda de una persona adulta de confianza."),
      ("Pensar que contar una presión de grupo es «acusar».", "Avisar a una persona adulta de confianza te protege.", "Recuerda que no es culpa tuya."),
  ],
  rec=[
      ("¿Qué sustancia del tabaco genera dependencia: la nicotina o el agua?", "La nicotina", "Es la que causa adicción."),
      ("¿Qué órgano daña el alcohol con el uso excesivo: el hígado o el hueso?", "El hígado", "Debe procesar el alcohol."),
      ("Verdadero o falso: si alguien te presiona a consumir, debes avisar a una persona adulta de confianza.", "Verdadero", "Es la conducta más segura."),
  ],
  und=[
      ("¿Por qué el alcohol es peligroso para la coordinación? A) Deprime el sistema nervioso; B) Mejora la coordinación y los reflejos.", "A", "Disminuye la actividad del sistema nervioso."),
      ("¿Por qué es mejor no consumir durante la adolescencia? A) El cerebro sigue en desarrollo y puede dañarse; B) Porque la ley lo exige para cualquier edad.", "A", "El cerebro adolescente es más vulnerable."),
      ("¿Qué mejora el ejercicio regular en el corazón?", "Lo hace más fuerte y eficiente", "Bombea más sangre en cada latido."),
  ],
  app=[
      ("Cuatro hábitos de ejemplo: caminar 40 minutos, fumar, comer verduras, tomar alcohol. ¿Cuántos son factores de riesgo?", "2", "Fumar y tomar alcohol."),
      arith("Una persona de ejemplo hace 30 minutos de ejercicio los lunes, miércoles y viernes. ¿Cuántos minutos suma en la semana?", "30*3", "Se multiplica por los tres días."),
      ("Un compañero te dice: «Pruébalo, todos lo hacen». ¿Cuál es la mejor respuesta? A) «No, gracias», y luego avisar a una persona adulta de confianza; B) Probar para no quedar mal.", "A", "Protege tu salud y tu seguridad."),
  ],
  rea=[
      ("Alguien dice: «Si el alcohol fuera tan dañino, nadie lo tomaría». ¿Qué falla tiene su argumento? A) La popularidad no prueba que algo sea seguro; B) El alcohol es un nutriente.", "A", "Hay evidencia de daño aunque muchas personas lo consuman."),
      ("Explica en una frase por qué el humo de tabaco reduce la capacidad de hacer ejercicio.", "Porque la sangre lleva menos oxígeno a los músculos", "El monóxido de carbono ocupa la hemoglobina."),
  ],
  cha=[
      ("Un estudio de ejemplo muestra que entre 100 personas que empezaron a fumar a los 14 años, 40 siguen fumando 10 años después; entre quienes empezaron a los 20, 25. ¿Qué conclusión es prudente? A) Empezar antes se asocia con más probabilidad de continuar; B) Fumar a cualquier edad es igual.", "A", "Los datos de ejemplo muestran diferencia entre ambos grupos."),
      arith("Con esos datos de ejemplo, ¿cuántos puntos porcentuales más continúan entre quienes empezaron a los 14 años que a los 20?", "40-25", "Se resta el porcentaje menor al mayor."),
  ],
  context=[("En una fiesta, un amigo te dice: «Un poco no hace nada». Tú no quieres tomar. ¿Qué haces? A) Decir que no, quedarte con personas de confianza o irte, y avisar después a una persona adulta de confianza; B) Aceptar para no discutir.", "A", "Es una conducta segura y respetuosa contigo.")],
  selfcheck=[("¿Qué hace el monóxido de carbono?", "Reduce el oxígeno que lleva la sangre", "Se une a la hemoglobina."), ("¿Por qué el alcohol altera el juicio?", "Porque deprime el sistema nervioso", "Cambia el funcionamiento del cerebro."), ("¿Qué haces si te presionan a consumir?", "Digo que no, me alejo y aviso a una persona adulta de confianza", "Así te proteges.")],
  open_task=task("Escribe tres frases breves que puedas decir para negarte a consumir alcohol, tabaco o drogas sin ofender, y una acción posterior. Después explica en dos oraciones, con un mecanismo, por qué el ejercicio y la alimentación balanceada protegen al corazón.", "Frases: «No, gracias, no me interesa»; «Prefiero no hacerlo»; «Me voy a otro lado». Acción: avisar a una persona adulta de confianza. Mecanismo: el ejercicio fortalece el corazón, que bombea más sangre en cada latido; una alimentación balanceada evita depósitos en las arterias.", ["tres frases claras", "acción de avisar", "mecanismo correcto"], ["frases y explicación"], ["decir que se guarda en secreto", "explicación sin mecanismo"], "Pregunta qué persona adulta de confianza elegirías."),
  reinforce="Escribe una frase para decir que no a un cigarrillo.",
  extend="Explica por qué es riesgoso consumir sustancias mientras el cerebro aún se desarrolla.")
