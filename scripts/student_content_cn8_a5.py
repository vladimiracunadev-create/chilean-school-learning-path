"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 05 (interacción de sistemas para el equilibrio corporal)."""
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


OA5 = "CN08 OA 05"

L(OA5, 1,
  materials="Este cuaderno y lápiz. Para la actividad opcional: una galleta de soda y un reloj con segundero. No la hagas si tienes alergia a algún ingrediente.",
  use="Aprenderé cómo las enzimas digestivas descomponen los alimentos y cómo los nutrientes pasan a la sangre. Sirve para explicar qué pasa con la comida desde que la comes.",
  prior=["Sé qué órganos forman el sistema digestivo.", "Sé que los nutrientes son carbohidratos, proteínas, grasas, vitaminas, minerales y agua."],
  explain=[
      "La digestión descompone los alimentos en partículas muy pequeñas que se pueden absorber. Lo hacen las enzimas digestivas: proteínas que aceleran reacciones y que son específicas, porque cada una actúa sobre un tipo de nutriente. La amilasa de la saliva empieza a digerir el almidón de la boca. La pepsina, en el estómago, digiere proteínas. En el intestino delgado actúan enzimas del páncreas y del propio intestino sobre almidón, proteínas y grasas.",
      "Los carbohidratos terminan como glucosa, las proteínas como aminoácidos y las grasas como ácidos grasos y glicerol. El hígado produce bilis, que no es una enzima: separa la grasa en gotitas pequeñas para que las enzimas actúen mejor. Las enzimas funcionan a cierta temperatura y pH, y con calor excesivo pierden su forma y dejan de funcionar.",
      "La absorción es el paso de los nutrientes a la sangre. Ocurre sobre todo en el intestino delgado, cuyas paredes tienen vellosidades que aumentan la superficie de contacto. El intestino grueso absorbe agua y forma las heces. Una pregunta investigable sería: «¿Cuántos segundos tarda en sentirse dulce una galleta de soda masticada sin tragar?». Se mide el tiempo y se puede repetir.",
  ],
  vocab=[("enzima digestiva", "proteína que acelera la descomposición de un nutriente"), ("absorción", "paso de nutrientes desde el intestino a la sangre"), ("vellosidades", "pliegues del intestino delgado que aumentan la superficie de absorción"), ("bilis", "líquido del hígado que separa la grasa en gotitas"), ("específica", "que actúa sobre un solo tipo de sustancia")],
  worked=[
      ("Producto final", "¿En qué se convierten las proteínas al final de la digestión?", ["Las proteínas se descomponen en piezas más pequeñas.", "Esas piezas se llaman aminoácidos."], "En aminoácidos"),
      ("Camino de un alimento", "Un trozo de pan sigue este camino: boca, estómago, intestino delgado. ¿Dónde empieza la digestión del almidón y dónde se absorben los nutrientes?", ["En la boca, la amilasa empieza con el almidón.", "La absorción ocurre sobre todo en el intestino delgado."], "Empieza en la boca y se absorbe en el intestino delgado"),
  ],
  mistakes=[
      ("Pensar que la bilis es una enzima.", "Solo separa la grasa en gotitas; no la descompone químicamente.", "Recuerda que las enzimas son proteínas específicas."),
      ("Creer que todo se absorbe en el estómago.", "La mayor parte de la absorción ocurre en el intestino delgado.", "Relaciona las vellosidades con la absorción."),
  ],
  rec=[
      ("¿Dónde empieza la digestión del almidón: en la boca o en el estómago?", "En la boca", "La amilasa de la saliva actúa sobre el almidón."),
      ("¿Qué órgano produce la bilis: el hígado o el estómago?", "El hígado", "La bilis ayuda a separar las grasas."),
      ("Verdadero o falso: la mayor parte de los nutrientes se absorbe en el intestino delgado.", "Verdadero", "Sus vellosidades aumentan la superficie de absorción."),
  ],
  und=[
      ("¿Qué es una enzima digestiva? A) Una proteína que acelera la descomposición de un nutriente; B) Un nutriente que se absorbe sin cambios.", "A", "Es un catalizador biológico y es específica."),
      ("¿Qué digiere la pepsina? A) Proteínas en el estómago; B) Almidón en la boca.", "A", "La amilasa actúa sobre el almidón."),
      ("¿Para qué sirven las vellosidades del intestino delgado? A) Para aumentar la superficie de absorción; B) Para triturar el alimento.", "A", "A mayor superficie, mayor absorción."),
  ],
  app=[
      ("Se mastica una galleta de soda sin tragar durante dos minutos y se siente dulce. ¿Qué explica el dulzor? A) La amilasa transformó almidón en azúcares simples; B) La galleta tenía azúcar agregada en grandes cantidades.", "A", "El almidón se descompone en azúcares con la acción de la enzima."),
      arith("Tres personas de ejemplo sintieron el dulzor a los 40, 60 y 80 segundos. ¿Cuál es el promedio en segundos?", "(40+60+80)//3", "Se suman los tiempos y se divide por 3."),
      ("Un huevo cocido es rico en proteínas. ¿Qué enzima del estómago actúa sobre esas proteínas?", "La pepsina", "Es la enzima gástrica que digiere proteínas."),
  ],
  rea=[
      ("Alguien afirma: «La bilis digiere las grasas como una enzima». ¿Cuál es la corrección? A) La bilis separa la grasa en gotitas para que las enzimas actúen; B) La bilis digiere proteínas.", "A", "La bilis facilita la digestión pero no es una enzima."),
      ("Una enzima de ejemplo funciona bien a 37 °C y deja de funcionar si se calienta mucho. ¿Por qué ocurre esto? Responde en una frase.", "Porque la enzima es una proteína que pierde su forma con el calor excesivo", "La forma de la enzima es la que le permite actuar."),
  ],
  cha=[
      ("¿Cuál pregunta es investigable? A) ¿Cuántos segundos tarda en sentirse dulce un pan masticado sin tragar? B) ¿Es rico el pan?", "A", "Se contesta midiendo un tiempo."),
      arith("Un alimento de ejemplo pesa 200 g y tiene 60 g de proteínas. ¿Qué porcentaje de su masa son proteínas?", "60*100//200", "Se divide el peso de las proteínas por el total y se multiplica por 100.", " %"),
  ],
  context=[("Una persona de ejemplo no produce enzimas pancreáticas. ¿Qué dificultad tendrá? A) Digerir bien proteínas, grasas y almidón en el intestino; B) Absorber agua en la boca.", "A", "Esas enzimas actúan en el intestino delgado.")],
  selfcheck=[("¿En qué se convierten los carbohidratos?", "En glucosa", "Es el producto final de su digestión."), ("¿Dónde ocurre la mayor parte de la absorción?", "En el intestino delgado", "Allí hay vellosidades que aumentan la superficie."), ("¿Por qué una enzima es específica?", "Porque actúa sobre un solo tipo de nutriente", "Su forma calza con una sustancia.")],
  open_task=task("Completa una tabla con tres filas: boca, estómago e intestino delgado. En cada fila escribe qué enzima o sustancia actúa, qué nutriente digiere y qué producto resulta. Luego escribe una pregunta investigable sobre la amilasa que se pueda contestar con una galleta de soda.", "Boca: amilasa; almidón; azúcares. Estómago: pepsina; proteínas; trozos más pequeños. Intestino delgado: enzimas del páncreas; almidón, proteínas y grasas; glucosa, aminoácidos y ácidos grasos. Pregunta: ¿Cuántos segundos tarda en sentirse dulce una galleta masticada sin tragar?", ["tres filas completas", "enzima y nutriente correctos", "pregunta con algo que se mide"], ["tabla y pregunta"], ["decir que la pepsina digiere almidón", "no indicar qué se mide"], "Pregunta qué cambiaría si se mastica una galleta más tiempo."),
  reinforce="Escribe una enzima digestiva y el nutriente sobre el que actúa.",
  extend="Explica por qué las vellosidades hacen más eficiente la absorción.")

L(OA5, 2,
  materials="Este cuaderno y lápiz. Si quieres, un reloj con segundero para tomar tu pulso en reposo con una persona de tu casa cerca.",
  use="Aprenderé cómo el sistema circulatorio transporta nutrientes, gases, desechos y anticuerpos. Sirve para explicar cómo llegan las sustancias a cada célula.",
  prior=["Sé que el corazón es una bomba.", "Sé qué nutrientes se absorben en el intestino delgado."],
  explain=[
      "El sistema circulatorio está formado por el corazón, los vasos sanguíneos y la sangre. La sangre lleva nutrientes absorbidos en el intestino, oxígeno desde los pulmones, y recoge desechos metabólicos, como dióxido de carbono y urea, que lleva a pulmones y riñones. También transporta anticuerpos, proteínas de defensa que ayudan a combatir microorganismos.",
      "La sangre tiene plasma (parte líquida), glóbulos rojos con hemoglobina que transporta oxígeno, glóbulos blancos que defienden el cuerpo y plaquetas que ayudan a coagular. Los vasos son de tres tipos: las arterias salen del corazón, las venas regresan a él y los capilares son muy finos y permiten el intercambio con las células. El lado derecho del corazón envía la sangre a los pulmones y el izquierdo la envía al resto del cuerpo.",
      "Al examinar evidencia, como el pulso, se cuentan los latidos por minuto. Si una persona en reposo tiene 70 latidos por minuto y tras correr tiene 130, el aumento se relaciona con que las células necesitan más oxígeno. Un dato por sí solo no explica la causa, pero con el mecanismo del transporte de oxígeno hace una conclusión razonable.",
  ],
  vocab=[("capilar", "vaso muy fino donde se intercambian sustancias con las células"), ("hemoglobina", "proteína de los glóbulos rojos que transporta oxígeno"), ("anticuerpo", "proteína de defensa que ayuda a combatir microorganismos"), ("desecho metabólico", "sustancia que sobra del funcionamiento de las células"), ("arteria", "vaso que sale del corazón")],
  worked=[
      ("Qué transporta la sangre", "Una sustancia sale de las células y va por la sangre hacia los pulmones. ¿Puede ser dióxido de carbono?", ["El dióxido de carbono es un desecho metabólico.", "La sangre lo lleva a los pulmones para eliminarlo."], "Sí, es dióxido de carbono"),
      ("Cambio de pulso", "El pulso en reposo es de 66 latidos por minuto y tras trotar es de 120. ¿Cuánto aumentó?", ["Resto: 120 − 66.", "120 − 66 = 54."], "54 latidos por minuto"),
  ],
  mistakes=[
      ("Creer que las arterias siempre llevan sangre con oxígeno.", "Se definen por salir del corazón; la que va a los pulmones lleva poco oxígeno.", "Define arteria y vena por la dirección del flujo."),
      ("Pensar que la sangre solo transporta oxígeno.", "También lleva nutrientes, desechos y anticuerpos.", "Recuerda las cuatro cargas."),
  ],
  rec=[
      ("¿Qué vaso sale del corazón: la arteria o la vena?", "La arteria", "Las venas regresan al corazón."),
      ("¿Qué parte de la sangre transporta oxígeno: los glóbulos rojos o las plaquetas?", "Los glóbulos rojos", "Contienen hemoglobina, que se une al oxígeno."),
      ("Verdadero o falso: los capilares son los vasos donde se intercambian sustancias con las células.", "Verdadero", "Sus paredes son muy delgadas."),
  ],
  und=[
      ("¿Qué función tienen los anticuerpos? A) Ayudar a combatir microorganismos; B) Transportar oxígeno a los músculos.", "A", "Son proteínas de defensa que viajan en la sangre."),
      ("¿Hacia dónde envía la sangre el lado derecho del corazón? A) A los pulmones; B) A todo el cuerpo.", "A", "El lado izquierdo la envía al cuerpo."),
      ("¿Por qué los capilares son tan finos?", "Para permitir el intercambio con las células", "Sus paredes delgadas dejan pasar sustancias."),
  ],
  app=[
      arith("Datos de ejemplo: el pulso en reposo es de 72 latidos por minuto. ¿Cuántos latidos hay en 5 minutos?", "72*5", "Se multiplica el pulso por los minutos."),
      arith("Un estudiante tenía 68 latidos por minuto en reposo y 128 tras subir escaleras. ¿Cuántos latidos por minuto aumentó?", "128-68", "Se resta el valor de reposo al de ejercicio."),
      ("Un nutriente absorbido en el intestino llega a un músculo. ¿Qué lo transporta? A) La sangre; B) El hueso.", "A", "Los vasos sanguíneos reparten los nutrientes."),
  ],
  rea=[
      ("Una persona dice: «El pulso sube con el ejercicio porque la sangre fabrica más oxígeno». ¿Qué corrección haces? A) Las células gastan más oxígeno y el corazón late más rápido para llevarlo; B) El oxígeno viene de los huesos.", "A", "El corazón responde a la demanda de oxígeno."),
      ("Un compañero afirma que las venas llevan sangre sin oxígeno siempre. Da un ejemplo que lo contradiga.", "Las venas que llevan sangre de los pulmones al corazón tienen sangre con oxígeno", "Se definen por regresar al corazón."),
  ],
  cha=[
      ("Dato de ejemplo: la sangre de una persona tiene un desecho llamado urea. ¿A qué órgano lo lleva para eliminarlo? A) Los riñones; B) Los pulmones.", "A", "El riñón filtra la urea."),
      ("Datos de ejemplo: antes del ejercicio el pulso es 70 y a los 2 minutos de ejercicio es 120. A los 5 minutos de reposo vuelve a 80. ¿Cuántos latidos por minuto más tiene a los 5 minutos de reposo que antes del ejercicio?", "10", "80 − 70 = 10: aún no regresa del todo.", "80-70"),
  ],
  context=[("Una persona de ejemplo se hace un examen de sangre y le dicen que tiene pocos glóbulos rojos. ¿Qué podría afectarle? A) El transporte de oxígeno; B) La digestión del almidón.", "A", "Los glóbulos rojos llevan el oxígeno con la hemoglobina.")],
  selfcheck=[("¿Cuáles son las partes del sistema circulatorio?", "Corazón, vasos sanguíneos y sangre", "Forman el sistema."), ("¿Qué transporta la sangre?", "Nutrientes, gases, desechos y anticuerpos", "Cuatro tipos de carga."), ("¿Qué función tienen los glóbulos rojos?", "Transportar oxígeno", "Con la hemoglobina.")],
  open_task=task("Escribe un recorrido en cinco pasos de un nutriente (la glucosa del pan) desde el intestino hasta una célula muscular, incluyendo corazón, arterias y capilares. Agrega qué desecho vuelve de esa célula y a qué órgano llega.", "1. La glucosa se absorbe en el intestino. 2. Pasa a la sangre. 3. Llega al corazón. 4. Sale por arterias. 5. En los capilares pasa a la célula muscular. Vuelve dióxido de carbono por venas hacia los pulmones.", ["cinco pasos en orden", "nombra corazón, arterias y capilares", "incluye un desecho y su órgano"], ["recorrido escrito"], ["olvidar los capilares", "mezclar arterias con venas"], "Pregunta qué pasa si se bloquea una arteria."),
  reinforce="Escribe tres cosas que transporta la sangre.",
  extend="Explica por qué el pulso aumenta al hacer ejercicio.")

L(OA5, 3,
  materials="Este cuaderno y lápiz. Opcional: pon tus manos sobre las costillas y respira lento.",
  use="Aprenderé cómo funciona la ventilación pulmonar y cómo ocurre el intercambio gaseoso en los alvéolos. Sirve para explicar por qué entra aire y cómo pasa el oxígeno a la sangre.",
  prior=["Sé que la sangre transporta gases.", "Sé qué es la difusión."],
  explain=[
      "La ventilación pulmonar es el movimiento del aire hacia dentro y fuera de los pulmones. En la inspiración, el diafragma (músculo bajo los pulmones) se contrae y baja, y las costillas suben. El volumen del tórax aumenta, la presión dentro baja y entra aire. En la espiración, el diafragma se relaja y sube, el volumen disminuye, la presión aumenta y el aire sale.",
      "El intercambio gaseoso ocurre en los alvéolos, que son sacos muy pequeños al final de los bronquiolos, rodeados de capilares. El oxígeno pasa por difusión del alvéolo (donde hay más) a la sangre (donde hay menos). El dióxido de carbono pasa de la sangre al alvéolo y sale al exhalar. Los alvéolos son cientos de millones, lo que da una gran superficie de intercambio.",
      "Un modelo sirve para predecir: si el volumen del tórax aumenta, la presión baja y entra aire. Un modelo de pulmón con una botella y globos muestra eso, pero tiene límites: no tiene alvéolos ni sangre. Datos de ejemplo: el aire inspirado tiene cerca de 21 % de oxígeno y el exhalado cerca de 16 %.",
  ],
  vocab=[("diafragma", "músculo que baja y sube para ventilar los pulmones"), ("inspiración", "entrada de aire a los pulmones"), ("espiración", "salida de aire de los pulmones"), ("alvéolo", "saco diminuto donde ocurre el intercambio gaseoso"), ("ventilación pulmonar", "movimiento del aire hacia dentro y fuera de los pulmones")],
  worked=[
      ("Qué pasa al inspirar", "Durante la inspiración, ¿el diafragma sube o baja? ¿La presión aumenta o disminuye?", ["El diafragma se contrae y baja.", "El tórax se agranda y la presión baja."], "El diafragma baja y la presión disminuye"),
      ("Dirección del oxígeno", "En el alvéolo hay más oxígeno que en el capilar. ¿Hacia dónde difunde el oxígeno?", ["La difusión va de mayor a menor concentración.", "Pasa del alvéolo al capilar."], "Del alvéolo a la sangre"),
  ],
  mistakes=[
      ("Creer que el diafragma sube al inspirar.", "Baja al contraerse y así agranda el tórax.", "Relaciona volumen y presión."),
      ("Decir que los pulmones tienen músculos que se contraen.", "Los pulmones no tienen músculos; el diafragma y los músculos de las costillas mueven el aire.", "Recuerda quién mueve el tórax."),
  ],
  rec=[
      ("En la inspiración, ¿el diafragma baja o sube?", "Baja", "Al contraerse aumenta el volumen del tórax."),
      ("¿Dónde ocurre el intercambio de gases: en los bronquios o en los alvéolos?", "En los alvéolos", "Son sacos con capilares alrededor."),
      ("Verdadero o falso: el oxígeno pasa del alvéolo a la sangre por difusión.", "Verdadero", "Va desde donde hay más hacia donde hay menos."),
  ],
  und=[
      ("Al espirar, ¿qué pasa con la presión en el tórax? A) Aumenta y sale el aire; B) Disminuye y entra aire.", "A", "El volumen se reduce."),
      ("¿Qué gas pasa de la sangre al alvéolo? A) Dióxido de carbono; B) Oxígeno.", "A", "Es un desecho que se elimina al exhalar."),
      ("¿Por qué es importante que los alvéolos sean muchísimos?", "Porque dan una gran superficie de intercambio", "A mayor superficie, más gas intercambiado."),
  ],
  app=[
      arith("Una persona de ejemplo inspira 500 mL de aire en cada respiración y respira 14 veces por minuto. ¿Cuántos mL de aire mueve por minuto?", "500*14", "Se multiplica el volumen por el número de respiraciones."),
      arith("Dato de ejemplo: el aire inspirado tiene 21 % de oxígeno y el exhalado 16 %. ¿Cuántos puntos porcentuales menos de oxígeno tiene el aire exhalado que el inspirado?", "21-16", "Se resta lo exhalado a lo inspirado."),
      ("Un modelo de pulmón con una botella y globos muestra que al agrandar el volumen interior el globo se llena. ¿A qué fase de la ventilación corresponde? A) Inspiración; B) Espiración.", "A", "Al agrandarse el volumen, entra aire."),
  ],
  rea=[
      ("Un estudiante afirma: «El aire entra porque los pulmones lo succionan como una esponja». ¿Qué explicación es mejor? A) El diafragma agranda el tórax y baja la presión, por eso entra aire; B) Los pulmones se contraen y atraen el aire.", "A", "Los pulmones no tienen músculos propios."),
      ("Explica en una frase por qué una persona con menos alvéolos sanos puede cansarse más fácil.", "Porque intercambia menos oxígeno por la menor superficie", "Con menos superficie pasa menos oxígeno a la sangre."),
  ],
  cha=[
      ("En un modelo de ejemplo, la botella representa el tórax, el globo interior el pulmón y la membrana de abajo el diafragma. Si se baja la membrana, ¿qué pasa con el globo? A) Se infla; B) Se desinfla.", "A", "Al bajar la membrana aumenta el volumen y baja la presión."),
      ("¿Cuál es un límite del modelo de la botella con globos? A) No representa alvéolos ni intercambio con la sangre; B) No usa aire.", "A", "El modelo muestra solo la ventilación."),
  ],
  context=[arith("Una persona de ejemplo respira 15 veces por minuto. ¿Cuántas respiraciones hace en 10 minutos?", "15*10", "Se multiplica el ritmo por los minutos.")],
  selfcheck=[("¿Qué pasa con el diafragma al inspirar?", "Se contrae y baja", "Aumenta el volumen del tórax."), ("¿Dónde ocurre el intercambio de gases?", "En los alvéolos", "Hay capilares alrededor."), ("¿Por qué difunde el oxígeno hacia la sangre?", "Porque hay más oxígeno en el alvéolo que en la sangre", "La difusión va de mayor a menor concentración.")],
  open_task=task("Dibuja el tórax en dos cuadros: inspiración y espiración. En cada uno marca el diafragma, las costillas y la dirección del aire, y escribe si el volumen y la presión aumentan o disminuyen. Debajo, dibuja un alvéolo con flechas para el oxígeno y el dióxido de carbono.", "Inspiración: diafragma baja, costillas suben, volumen aumenta, presión baja, entra aire. Espiración: lo contrario. Alvéolo: oxígeno del alvéolo a la sangre; dióxido de carbono de la sangre al alvéolo.", ["dos cuadros correctos", "volumen y presión coherentes", "flechas de gases correctas"], ["dibujos con rótulos"], ["invertir volumen y presión", "invertir las flechas de gases"], "Pregunta qué limita al modelo de botella y globos."),
  reinforce="Escribe qué hace el diafragma en la inspiración.",
  extend="Explica por qué la difusión mueve el oxígeno hacia la sangre.")

L(OA5, 4,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo.",
  use="Aprenderé cómo el sistema excretor filtra la sangre, regula el agua del cuerpo y elimina desechos. Sirve para entender por qué el cuerpo mantiene su equilibrio.",
  prior=["Sé que la sangre transporta desechos metabólicos.", "Sé qué es la osmosis."],
  explain=[
      "El sistema excretor elimina desechos y mantiene el equilibrio del agua. Está formado por los riñones, los uréteres, la vejiga y la uretra. En los riñones hay millones de nefronas, que son unidades que filtran la sangre. Pasan a la nefrona agua, sales, glucosa y urea; los glóbulos rojos y las proteínas grandes no pasan.",
      "Después del filtrado, el cuerpo reabsorbe lo útil, como la glucosa y casi toda el agua, y lo devuelve a la sangre. Lo que no se reabsorbe forma la orina, que contiene agua, urea y sales. La urea es un desecho que resulta de usar las proteínas. La orina baja por los uréteres a la vejiga y sale por la uretra.",
      "Los riñones regulan la cantidad de agua. Si una persona bebe poco, el riñón reabsorbe más agua y la orina es escasa y oscura. Si bebe mucho, la orina es abundante y clara. Los balances se pueden calcular: lo que entra de agua debe ser igual a lo que sale para que el cuerpo esté en equilibrio. Otros órganos también eliminan desechos: los pulmones, el dióxido de carbono; la piel, sudor.",
  ],
  vocab=[("nefrona", "unidad del riñón que filtra la sangre"), ("filtración", "paso de agua y sustancias pequeñas de la sangre a la nefrona"), ("reabsorción", "retorno a la sangre de lo útil que se filtró"), ("urea", "desecho que resulta de usar las proteínas"), ("balance hídrico", "comparación entre el agua que entra y la que sale del cuerpo")],
  worked=[
      ("Qué pasa por el filtro", "Una nefrona filtra la sangre. ¿Cuál de estas pasa al filtrado: urea o glóbulos rojos?", ["Los glóbulos rojos son grandes y no pasan.", "La urea es pequeña y pasa."], "La urea"),
      ("Balance de agua", "En un día, una persona ingiere 2.000 mL de agua y pierde 1.200 mL por orina y 800 mL por sudor, respiración y heces. ¿Está en equilibrio?", ["Sumo lo que sale: 1.200 + 800 = 2.000.", "Entra 2.000 y sale 2.000."], "Sí, entra y sale lo mismo"),
  ],
  mistakes=[
      ("Pensar que la orina es sangre filtrada que se elimina completa.", "Casi toda el agua y los nutrientes se reabsorben.", "Distingue filtración y reabsorción."),
      ("Creer que solo los riñones eliminan desechos.", "Los pulmones eliminan dióxido de carbono y la piel, sudor.", "Piensa en varios órganos."),
  ],
  rec=[
      ("¿Qué órgano filtra la sangre: el riñón o la vejiga?", "El riñón", "Allí están las nefronas."),
      ("¿Qué desecho se produce al usar proteínas: la urea o la glucosa?", "La urea", "Se elimina con la orina."),
      ("Verdadero o falso: la orina baja a la vejiga por los uréteres.", "Verdadero", "Luego sale por la uretra."),
  ],
  und=[
      ("¿Qué no pasa por el filtro de la nefrona? A) Los glóbulos rojos; B) El agua.", "A", "Son demasiado grandes."),
      ("¿Por qué se reabsorbe la glucosa? A) Porque es útil para el cuerpo; B) Porque es un desecho.", "A", "El cuerpo recupera lo que necesita."),
      ("Una persona bebe poco. ¿Cómo será su orina?", "Escasa y oscura", "El riñón reabsorbe más agua."),
  ],
  app=[
      arith("Datos de ejemplo: una persona ingiere 1.800 mL de agua en un día. Pierde 1.100 mL por orina y 700 mL por sudor, respiración y heces. ¿Cuántos mL pierde en total?", "1100+700", "Se suman las pérdidas."),
      arith("Otra persona ingiere 2.400 mL y pierde 2.100 mL. ¿Cuántos mL más ingresan que salen?", "2400-2100", "Se resta lo que sale a lo que entra."),
      ("Si una persona ingiere 2.400 mL y pierde 2.100 mL cada día, ¿qué ocurre con el agua del cuerpo si el patrón se repite? A) Se acumula; B) Se agota.", "A", "Entra más agua de la que sale."),
  ],
  rea=[
      ("Si aparecen glóbulos rojos en la orina de una persona de ejemplo, ¿qué indica? A) Que el filtro puede estar dañado y conviene consultar a un profesional de salud; B) Que está bien hidratada.", "A", "En condiciones normales no pasan al filtrado."),
      ("En un día de calor, una persona de ejemplo suda mucho. ¿Qué espera que ocurra con su orina? Responde en una frase.", "Será más escasa y oscura", "El cuerpo ahorra agua."),
  ],
  cha=[
      ("Un compañero dice: «Si tomo más agua que lo necesario, no pasa nada porque sobra». ¿Qué respuesta es más completa? A) El riñón elimina el exceso formando más orina, pero beber de más tampoco es necesario; B) El agua se guarda siempre.", "A", "El riñón ajusta la cantidad de agua."),
      ("Datos de ejemplo de filtración: de 100 unidades de agua que se filtran, se reabsorben 99. ¿Cuántas salen como orina?", "1", "100 − 99 = 1.", "100-99"),
  ],
  context=[("En un clima seco, una persona de ejemplo que hace deporte debe reponer líquidos. ¿Qué ocurre con su sistema excretor si no lo hace? A) Los riñones ahorran agua y la orina es escasa; B) La orina es abundante y clara.", "A", "El equilibrio del agua se protege.")],
  selfcheck=[("¿Qué filtran las nefronas?", "La sangre", "Retienen lo grande y filtran lo pequeño."), ("¿Qué contiene la orina?", "Agua, urea y sales", "Son lo que no se reabsorbe."), ("¿Qué regulan los riñones además de eliminar desechos?", "La cantidad de agua", "Mantienen el equilibrio del cuerpo.")],
  open_task=task("Con estos datos de ejemplo de un día: ingresos de agua 1.500 mL por bebidas, 700 mL por alimentos y 300 mL por procesos del cuerpo; pérdidas 1.500 mL por orina, 500 mL por sudor, 400 mL por respiración y 100 mL por heces, haz un balance, di si hay equilibrio y explica qué regula el riñón.", "Ingresos: 1.500 + 700 + 300 = 2.500 mL. Pérdidas: 1.500 + 500 + 400 + 100 = 2.500 mL. Hay equilibrio. El riñón regula la cantidad de agua reabsorbiendo más o menos.", ["dos sumas correctas", "dice si hay equilibrio", "explica el rol del riñón"], ["balance y frase"], ["olvidar una pérdida", "no comparar ingresos y pérdidas"], "Pregunta qué pasaría un día de mucho calor."),
  reinforce="Escribe los órganos del sistema excretor en orden.",
  extend="Explica por qué la reabsorción es necesaria después de la filtración.")

L(OA5, 5,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo. Si algo de este tema te preocupa o alguien te presiona a consumir sustancias, avísale a una persona adulta de confianza.",
  use="Aprenderé cómo interactúan los sistemas y cómo el consumo excesivo de tabaco, alcohol, grasas y sodio afecta el equilibrio del cuerpo. Sirve para tomar decisiones informadas.",
  prior=["Sé qué hacen los sistemas digestivo, circulatorio, respiratorio y excretor.", "Sé leer tablas y comparar datos."],
  explain=[
      "Los sistemas trabajan juntos: el digestivo absorbe nutrientes, el circulatorio los reparte con el oxígeno que entregó el respiratorio, y las células producen desechos que la sangre lleva al excretor y a los pulmones. Si falla un sistema, los otros se afectan. Eso es el equilibrio del cuerpo.",
      "El consumo excesivo de algunas sustancias aumenta el riesgo de enfermedades. El tabaco daña las vías respiratorias y los alvéolos, y también las arterias; se relaciona con cáncer pulmonar y enfermedades del corazón. El alcohol daña el hígado y otros órganos y afecta el cerebro. Las grasas en exceso, sobre todo saturadas, se relacionan con depósitos en las arterias. El exceso de sodio (sal) se relaciona con presión arterial alta, que daña corazón y riñones.",
      "Para analizar evidencia hay que leer los datos con cuidado: una asociación en una tabla muestra un riesgo mayor, no un destino seguro. La prevención incluye no fumar, no consumir alcohol, moderar las grasas saturadas y la sal, y mantener una vida activa. Si alguien siente presión para consumir, lo mejor es decir que no, alejarse y avisar a una persona adulta de confianza.",
  ],
  vocab=[("equilibrio corporal", "estado en que los sistemas del cuerpo funcionan de manera coordinada"), ("factor de riesgo", "condición que aumenta la probabilidad de una enfermedad"), ("presión arterial alta", "fuerza excesiva de la sangre sobre las paredes de las arterias"), ("sodio", "mineral que está en la sal de mesa"), ("prevención", "acciones que reducen el riesgo de enfermar")],
  worked=[
      ("Sistemas que interactúan", "Una persona corre. ¿Qué sistemas trabajan juntos para que sus músculos tengan oxígeno?", ["El respiratorio incorpora oxígeno.", "El circulatorio lo lleva a los músculos."], "Los sistemas respiratorio y circulatorio"),
      ("Leer una asociación", "En una tabla de ejemplo, 8 de cada 100 personas que fuman tienen cierta enfermedad y 2 de cada 100 que no fuman la tienen. ¿Cuántas veces mayor es el riesgo en quienes fuman?", ["Divido 8 entre 2.", "8 ÷ 2 = 4."], "4 veces mayor"),
  ],
  mistakes=[
      ("Creer que una asociación significa que todas las personas se enfermarán.", "Indica un mayor riesgo, no una certeza.", "Usa palabras como «aumenta el riesgo»."),
      ("Pensar que cada sistema funciona solo.", "Los sistemas dependen unos de otros.", "Piensa en el recorrido de una sustancia por varios sistemas."),
  ],
  rec=[
      ("¿Qué órgano daña especialmente el alcohol en exceso: el hígado o el hueso?", "El hígado", "Debe procesar el alcohol."),
      ("¿Qué mineral de la sal de mesa se relaciona con la presión arterial alta?", "El sodio", "El exceso eleva la presión."),
      ("Verdadero o falso: el tabaco daña las vías respiratorias.", "Verdadero", "Se relaciona con enfermedades pulmonares."),
  ],
  und=[
      ("¿Qué sistemas se ven afectados por el tabaco? A) Respiratorio y circulatorio; B) Solo el óseo.", "A", "Daña pulmones y arterias."),
      ("¿Por qué una dieta con exceso de grasas saturadas aumenta el riesgo cardiovascular? A) Porque se relaciona con depósitos en las arterias; B) Porque las grasas son un desecho.", "A", "Esos depósitos estrechan las arterias."),
      ("Si alguien te presiona a consumir alcohol, ¿qué es lo más seguro? A) Decir que no, alejarte y avisar a una persona adulta de confianza; B) Aceptar para no quedar mal.", "A", "Protege tu salud y tu seguridad."),
  ],
  app=[
      arith("Dato de ejemplo: de 200 personas que consumen mucha sal, 30 tienen presión alta. ¿Qué porcentaje es?", "30*100//200", "Se divide por el total y se multiplica por 100.", " %"),
      arith("Dato de ejemplo: de 100 personas que no fuman, 3 tienen un problema respiratorio; de 100 que fuman, 12. ¿Cuántas personas más tienen el problema en el grupo que fuma?", "12-3", "Se resta el menor al mayor."),
      ("Cuatro hábitos de ejemplo: caminar 30 minutos, fumar, comer con poca sal, tomar alcohol. ¿Cuántos son factores de riesgo?", "2", "Fumar y tomar alcohol aumentan el riesgo."),
  ],
  rea=[
      ("Alguien afirma: «Mi tío fuma y no se ha enfermado; entonces el tabaco no es peligroso». ¿Qué falla tiene? A) Un caso aislado no desmiente un riesgo estadístico; B) Los datos de muchas personas no sirven como evidencia.", "A", "Los datos de muchas personas muestran el riesgo."),
      ("Explica en una frase cómo el exceso de sodio puede afectar al corazón y a los riñones.", "Eleva la presión arterial, que daña ambos", "La presión alta daña las arterias y el filtro renal."),
  ],
  cha=[
      ("Una tabla de ejemplo dice que quienes hacen ejercicio y comen poca sal tienen menos presión alta. ¿Qué conclusión es prudente? A) Son hábitos asociados a menor riesgo; B) Aseguran que nunca habrá enfermedad.", "A", "Una asociación no es una garantía."),
      ("¿Cuál afirmación es más prudente? A) El alcohol en exceso aumenta el riesgo de daño al hígado y a otros órganos; B) El alcohol en exceso daña de la misma forma a todas las personas sin excepción.", "A", "Los datos muestran riesgo mayor, no un daño igual y seguro."),
  ],
  context=[("Un curso de ejemplo hace un afiche sobre cuidar los pulmones. ¿Qué mensaje basado en evidencia sirve? A) No fumar ni respirar humo de tabaco ajeno; B) Fumar poco no tiene efecto.", "A", "El tabaco daña los alvéolos y las vías respiratorias.")],
  selfcheck=[("¿Qué es un factor de riesgo?", "Una condición que aumenta la probabilidad de enfermar", "No es una certeza."), ("¿Qué hace el exceso de sodio?", "Aumenta la presión arterial", "Daña corazón y riñones."), ("¿Qué haces si alguien te presiona a consumir?", "Digo que no, me alejo y aviso a una persona adulta de confianza", "Es la acción más segura.")],
  open_task=task("Escribe un mensaje breve de prevención de cuatro oraciones dirigido a tu curso, con una acción para cuidar cada una de estas partes: pulmones, hígado, arterias y riñones. Usa las palabras «aumenta el riesgo» y «persona adulta de confianza».", "Evita fumar, porque el tabaco aumenta el riesgo de enfermedad pulmonar. No consumas alcohol: daña el hígado. Come menos grasas saturadas para cuidar las arterias. Modera la sal para proteger los riñones. Si alguien te presiona, avisa a una persona adulta de confianza.", ["cuatro acciones correctas", "usa «aumenta el riesgo»", "menciona a una persona adulta de confianza"], ["mensaje de cuatro oraciones"], ["culpar a una persona que consume", "afirmar certezas absolutas"], "Pregunta qué dato apoyaría cada recomendación."),
  reinforce="Escribe dos factores de riesgo para el sistema circulatorio.",
  extend="Explica por qué dos sistemas pueden afectarse con la misma sustancia.")
