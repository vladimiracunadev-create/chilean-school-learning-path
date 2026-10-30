"""Cuaderno del estudiante, 2.º básico Ciencias Naturales: OA 01 (vertebrados) y OA 02 (animales sin columna)."""
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


OA1, OA2 = "CN02 OA 01", "CN02 OA 02"

# ---------------------------------------------------------------- OA 01
L(OA1, 1,
  materials="Este cuaderno con las tarjetas de animales, lápiz y lápices de colores. Para sentir tu propia columna: tu espalda y una mano.",
  use="Aprenderé qué es un animal vertebrado. Sirve para ordenar animales en grupos sin equivocarme por el tamaño o por el lugar donde viven.",
  prior=["Sé nombrar animales que conozco: perro, pez, araña, caracol.", "Sé que un esqueleto es el conjunto de huesos del cuerpo."],
  explain=[
      "Pasa tu mano por el centro de tu espalda, desde el cuello hacia abajo. Sientes una fila de huesitos. Esa fila se llama columna vertebral, y cada huesito de la fila se llama vértebra. Muchos animales también la tienen.",
      "Un animal vertebrado es un animal que tiene columna vertebral. Un perro, una gaviota, una lagartija, una rana y una trucha son vertebrados. Aunque se vean muy distintos por fuera, por dentro todos tienen esa fila de vértebras.",
      "Los animales que no tienen columna se llaman invertebrados. Una lombriz, un caracol o una mariposa no tienen vértebras. Para clasificar, no importa si el animal es grande o chico, ni si vive en el agua o en la tierra. Importa si tiene columna.",
  ],
  vocab=[("columna vertebral", "fila de huesitos en la espalda"), ("vértebra", "cada uno de los huesitos de la columna"), ("vertebrado", "animal que tiene columna vertebral"), ("invertebrado", "animal que no tiene columna vertebral"), ("criterio", "regla que uso para ordenar o clasificar")],
  worked=[
      ("Clasificar un animal con una tarjeta", "Tarjeta: «Gaviota. Tiene plumas y alas. Por dentro tiene una columna vertebral». ¿Es vertebrada?", ["Busco la pista importante: la columna vertebral.", "La tarjeta dice que la gaviota sí la tiene.", "Las plumas y las alas no deciden este grupo."], "Sí, la gaviota es vertebrada porque tiene columna vertebral"),
      ("Descartar el tamaño", "Un ratón es muy chiquito y una medusa es grande. La medusa no tiene columna. ¿Cuál es vertebrado?", ["El tamaño no es el criterio.", "El ratón tiene columna vertebral; la medusa no.", "Por eso el ratón es vertebrado, aunque sea más chico."], "El ratón es vertebrado; la medusa es invertebrada"),
  ],
  mistakes=[
      ("Decir «la hormiga es invertebrada porque es chica».", "Se usa el tamaño como criterio.", "El criterio es la columna. La hormiga es invertebrada porque no tiene columna, no por ser chica."),
      ("Decir «el pez no es vertebrado porque no tiene patas».", "Se cree que los vertebrados deben tener patas.", "Un pez tiene columna vertebral aunque no tenga patas, por eso es vertebrado."),
  ],
  rec=[
      ("Cada huesito de la columna vertebral se llama de una manera. ¿Cómo?", "Vértebra", "El nombre de cada huesito de la columna es vértebra."),
      ("Una trucha tiene columna vertebral. ¿Es vertebrada o invertebrada?", "Vertebrada", "Tener columna vertebral hace vertebrado a un animal."),
      ("Un caracol de jardín tiene el cuerpo blando y ninguna columna. ¿Es vertebrado?", "No", "Sin columna vertebral es invertebrado."),
  ],
  und=[
      ("¿Qué significa la palabra «vertebrado»?", "Animal que tiene columna vertebral", "Es la definición de vertebrado dada en esta clase."),
      ("Una gaviota y un perro se ven muy distintos por fuera. ¿Qué tienen en común por dentro?", "Los dos tienen columna vertebral", "Por eso ambos son vertebrados."),
      ("Explica por qué la lombriz de tierra no es vertebrada.", "Porque no tiene columna vertebral", "Su cuerpo es blando y no tiene vértebras."),
  ],
  app=[
      ("Tarjetas: A gaviota (con columna), B mariposa (sin columna), C lagartija (con columna), D araña (sin columna). Escribe las letras de los vertebrados.", "A y C", "La gaviota y la lagartija tienen columna."),
      arith("En una lámina hay 8 animales y 5 tienen columna vertebral. ¿Cuántos animales no tienen columna?", "8-5", "Se resta a los 8 animales los 5 que sí tienen columna."),
      ("Pasas la mano por el lomo de un gato y sientes una fila de huesitos. ¿Qué parte de su cuerpo estás sintiendo?", "La columna vertebral", "La fila de huesitos de la espalda es la columna."),
  ],
  rea=[
      ("Sofía dice: «Un animal chiquito siempre es invertebrado». Un ratón es chiquito y tiene columna. ¿Tiene razón Sofía?", "No", "El tamaño no decide: el ratón es chico y es vertebrado."),
      ("Un pez nada y una araña teje telarañas. Para saber si son vertebrados, ¿sirve más mirar dónde viven o si tienen columna?", "Si tienen columna", "El criterio de vertebrado es la columna, no el lugar."),
  ],
  cha=[
      ("Un colibrí (pequeño, con columna), una vaca (grande, con columna) y un caracol (pequeño, sin columna). ¿Los dos animales pequeños son del mismo grupo? Explica.", "No; el colibrí es vertebrado y el caracol no", "Aunque ambos son pequeños, solo el colibrí tiene columna."),
      ("Un museo muestra el esqueleto de un animal con cráneo y una fila de vértebras. No se sabe si tenía pelo o plumas. ¿Se puede decir que es vertebrado?", "Sí", "Las vértebras bastan para saber que tenía columna vertebral."),
  ],
  context=[("En una charca ves una rana, una libélula y un renacuajo. Sabes que la rana y el renacuajo tienen columna y que la libélula no. ¿Cuántos de los tres animales son vertebrados?", "2", "La rana y el renacuajo tienen columna; la libélula no.")],
  selfcheck=[("Completa: un animal con columna vertebral es un ______.", "vertebrado", "Es la definición de vertebrado."), ("¿Importa el tamaño para decidir si un animal es vertebrado?", "No", "Lo único que importa es si tiene columna."), ("¿Cómo se llama cada huesito de la columna?", "Vértebra", "Las vértebras forman la columna.")],
  open_task=task("Clasifica estos seis animales en dos columnas, «con columna» y «sin columna», usando su pista: perro (huesos en la espalda), caracol (cuerpo blando), rana (huesos en la espalda), lombriz (cuerpo blando), trucha (huesos en la espalda), mariposa (cuerpo cubierto, sin columna). Dibuja dos de ellos.", "Con columna: perro, rana, trucha. Sin columna: caracol, lombriz, mariposa. La clasifiqué por la columna y no por el tamaño.", ["pone cada animal en la columna correcta", "usa la columna como criterio", "dibuja dos animales"], ["tabla de dos columnas", "dibujo de dos animales"], ["clasificar por tamaño", "clasificar por si tiene patas"], "Reconoce el uso del criterio y pide que explique con sus palabras por qué la mariposa va en «sin columna»."),
  reinforce="Con ayuda de un adulto, toca tu columna vertebral y cuenta en voz alta tres animales que también la tengan.",
  extend="Piensa en un animal que no tenga patas pero sí columna. Explica por qué es vertebrado.")

L(OA1, 2,
  materials="Este cuaderno con las tarjetas de rasgos de mamíferos y aves, y lápices de colores. En casa puedes mirar una pluma limpia o la foto de un animal que tengas.",
  use="Aprenderé a reconocer mamíferos y aves por más de un rasgo. Sirve para no confundir un murciélago con un ave o un pingüino con un pez.",
  prior=["Sé que un vertebrado tiene columna vertebral.", "Sé nombrar partes del cuerpo como alas, pico y patas."],
  explain=[
      "Los mamíferos son vertebrados con pelo en el cuerpo. Las hembras tienen mamas, y con ellas dan leche a sus crías. Respiran con pulmones. Un perro, una vaca, un gato y un murciélago son mamíferos.",
      "Las aves son vertebradas con plumas en el cuerpo, un pico y dos alas. Ponen huevos y también respiran con pulmones. Una gallina, una gaviota y un cóndor son aves. No todas las aves vuelan: el pingüino y la gallina casi no vuelan.",
      "Un solo rasgo puede engañar. El murciélago vuela, pero tiene pelo y da leche, así que es mamífero. Por eso hay que mirar varios rasgos: cubierta del cuerpo, mamas o huevos, pico y pulmones.",
  ],
  vocab=[("mamífero", "vertebrado con pelo cuyas crías toman leche de las mamas"), ("ave", "vertebrado con plumas, pico y alas que pone huevos"), ("cubierta corporal", "lo que cubre la piel del animal: pelo, plumas, escamas"), ("mamas", "partes del cuerpo de la madre que producen leche"), ("pulmones", "órganos que usan los animales para respirar aire")],
  worked=[
      ("Clasificar un animal con dos rasgos", "Un animal tiene pelo y sus crías toman leche. ¿Es mamífero o ave?", ["El pelo es rasgo de mamíferos, no de aves.", "La leche de las mamas también lo es.", "Con dos rasgos del mismo grupo estoy más seguro."], "Es un mamífero"),
      ("Un animal que vuela", "El murciélago vuela, tiene pelo y da leche a sus crías. ¿Es ave?", ["Volar no es un rasgo que defina a las aves.", "Las aves tienen plumas, y el murciélago tiene pelo.", "Tiene pelo y da leche: eso lo hace mamífero."], "No, es un mamífero que vuela"),
  ],
  mistakes=[
      ("Decir «todo lo que vuela es ave».", "Se usa un solo rasgo, volar.", "Mira la cubierta del cuerpo. El murciélago vuela, pero tiene pelo, así que es mamífero."),
      ("Decir «el pingüino es un pez porque nada».", "Se mira dónde vive y no el cuerpo.", "El pingüino tiene plumas, pico y pone huevos: es un ave que nada."),
  ],
  rec=[
      ("¿Qué cubre el cuerpo de un mamífero: pelo o plumas?", "Pelo", "Los mamíferos tienen pelo."),
      ("¿Qué cubre el cuerpo de un ave: plumas o escamas?", "Plumas", "Las aves tienen plumas."),
      ("Una vaca da leche a su ternero con las mamas. ¿Es mamífero?", "Sí", "Tener mamas y dar leche es rasgo de mamíferos."),
  ],
  und=[
      ("Nombra dos rasgos que tienen las aves.", "Plumas, pico, alas o ponen huevos (dos de ellos)", "Son rasgos de las aves vistos en la clase."),
      ("¿Para qué sirven las mamas de un mamífero?", "Para dar leche a las crías", "La leche alimenta a las crías de los mamíferos."),
      ("Un murciélago vuela. ¿Por qué no es un ave?", "Porque tiene pelo y da leche en vez de plumas", "Sus rasgos son de mamífero."),
  ],
  app=[
      ("Tarjetas: A gato (pelo, mamas), B gallina (plumas, pico), C zorro (pelo, mamas), D gaviota (plumas, alas). Escribe las letras de los mamíferos.", "A y C", "El gato y el zorro tienen pelo y mamas."),
      arith("En un corral hay 6 gallinas y cada una tiene 2 alas. ¿Cuántas alas hay en total?", "6*2", "Se multiplica el número de gallinas por las 2 alas de cada una."),
      ("Un animal tiene plumas y pone huevos, pero no vuela y nada muy bien. ¿Es mamífero o ave?", "Ave", "Plumas y huevos son rasgos de ave, aunque no vuele."),
  ],
  rea=[
      ("Pedro dice: «La ballena vive en el agua, así que es un pez». Una ballena respira con pulmones y da leche a su cría. ¿Qué rasgos muestran que Pedro se equivoca?", "Respira con pulmones y da leche, rasgos de mamífero", "Los peces no dan leche; las ballenas sí."),
      ("Un animal tiene plumas y pico, y sus crías nacen de huevos. ¿Es mamífero o ave? Explica.", "Ave, porque tiene plumas, pico y pone huevos", "Plumas, pico y huevos son rasgos de las aves."),
  ],
  cha=[
      ("Un animal tiene plumas y no vuela. Otro tiene pelo y vuela. ¿Cuál es ave y cuál es mamífero?", "El de plumas es ave; el de pelo es mamífero", "La cubierta del cuerpo decide, y no el vuelo."),
      ("Escribe una pregunta con respuesta Sí o No que sirva para separar mamíferos de aves.", "Por ejemplo: ¿tiene pelo?", "Cualquier pregunta sobre pelo, plumas, mamas o pico separa los dos grupos."),
  ],
  context=[("En el campo ves una vaca con su ternero y una gallina con sus pollitos. El ternero toma leche de su madre; los pollitos nacieron de huevos. ¿Cuál animal es mamífero?", "La vaca", "El ternero toma leche de las mamas de su madre.")],
  selfcheck=[("¿Las aves tienen pelo o plumas?", "Plumas", "Las plumas cubren el cuerpo de las aves."), ("¿Un murciélago es ave o mamífero?", "Mamífero", "Tiene pelo y da leche a sus crías."), ("¿Con qué órgano respiran mamíferos y aves?", "Con pulmones", "Ambos grupos respiran aire con pulmones.")],
  open_task=task("Clasifica estos cuatro animales como mamífero o ave y escribe dos rasgos de cada uno. Perro: pelo, mamas. Cóndor: plumas, pone huevos. Murciélago: pelo, vuela, da leche. Pingüino: plumas, pico, nada.", "Perro: mamífero, pelo y mamas. Cóndor: ave, plumas y huevos. Murciélago: mamífero, pelo y leche. Pingüino: ave, plumas y pico.", ["clasifica los cuatro animales", "escribe dos rasgos de cada uno", "no usa solo «vuela» o «nada»"], ["tabla con animal, grupo y dos rasgos"], ["decidir solo por volar o nadar"], "Valora el uso de dos rasgos y pregunta qué rasgo cambiaría si el animal fuera de otro grupo."),
  reinforce="Dibuja un mamífero y un ave, y pinta su cubierta corporal con el color que corresponde a cada una.",
  extend="Piensa en otro mamífero que viva en el agua y explica con un rasgo por qué no es un pez.")

L(OA1, 3,
  materials="Este cuaderno con las tarjetas de reptiles, anfibios y peces, y lápices de colores. No necesitas tocar animales vivos.",
  use="Aprenderé a reconocer reptiles, anfibios y peces. Sirve para distinguir una lagartija de una rana o un salmón de un delfín.",
  prior=["Sé que mamíferos y aves son vertebrados.", "Sé que mamíferos y aves respiran con pulmones."],
  explain=[
      "Los reptiles tienen la piel seca y cubierta de escamas. Respiran con pulmones y la mayoría pone huevos en la tierra. La lagartija, la culebra y la tortuga son reptiles. Una tortuga marina nada, pero igual respira aire con pulmones.",
      "Los anfibios tienen la piel húmeda y sin escamas. Las crías, como el renacuajo, viven en el agua y respiran con branquias. Los adultos, como la rana, respiran con pulmones y por la piel. La rana y el sapo son anfibios.",
      "Los peces tienen aletas para nadar y respiran con branquias dentro del agua. Las branquias toman el oxígeno que hay en el agua; el oxígeno es la parte del aire que todos necesitamos para vivir. Casi siempre su cuerpo tiene escamas. La trucha y el salmón son peces. Mira siempre la respiración y la piel juntas para no confundir los grupos.",
  ],
  vocab=[("reptil", "vertebrado de piel seca con escamas que respira con pulmones"), ("anfibio", "vertebrado de piel húmeda y sin escamas cuya cría vive en el agua"), ("pez", "vertebrado con aletas que respira con branquias"), ("branquias", "órganos que toman del agua el oxígeno que el pez necesita"), ("escamas", "placas pequeñas y duras que cubren la piel")],
  worked=[
      ("Reptil o anfibio", "Un animal tiene la piel seca, con escamas, y respira con pulmones. ¿Es reptil o anfibio?", ["La piel seca con escamas es de reptil.", "Los anfibios tienen piel húmeda y sin escamas.", "Los pulmones coinciden con el reptil."], "Es un reptil"),
      ("Un animal que nada", "Un animal nada, tiene aletas y respira con branquias. ¿Es pez?", ["Las aletas sirven para nadar.", "Respirar con branquias es rasgo de los peces.", "Dos rasgos coinciden con el grupo de los peces."], "Sí, es un pez"),
  ],
  mistakes=[
      ("Decir «la tortuga marina es un pez porque vive en el mar».", "Se mira el lugar y no la respiración ni la piel.", "La tortuga marina tiene piel seca, caparazón y respira aire con pulmones: es un reptil."),
      ("Decir «la rana tiene escamas».", "Se confunde la piel de los anfibios con la de reptiles y peces.", "La rana tiene piel húmeda y sin escamas."),
  ],
  rec=[
      ("¿Qué piel tienen los reptiles: seca con escamas o húmeda y sin escamas?", "Seca con escamas", "Es el rasgo propio de los reptiles."),
      ("¿Qué órganos usan los peces para respirar en el agua?", "Branquias", "Las branquias toman el oxígeno del agua."),
      ("La rana tiene piel húmeda y sin escamas. ¿Es anfibio o reptil?", "Anfibio", "Piel húmeda y sin escamas es rasgo de anfibio."),
  ],
  und=[
      ("Nombra dos rasgos de los peces.", "Aletas y branquias (también escamas)", "Son los rasgos de los peces de esta clase."),
      ("¿Dónde vive y cómo respira un renacuajo?", "En el agua y con branquias", "Las crías de anfibios viven en el agua."),
      ("Una tortuga marina nada en el mar. ¿Por qué sigue siendo reptil?", "Porque tiene piel seca y respira aire con pulmones", "Sus rasgos son de reptil aunque viva en el agua."),
  ],
  app=[
      ("Tarjetas: A lagartija (piel seca con escamas), B rana (piel húmeda y sin escamas), C trucha (aletas y branquias), D culebra (piel seca con escamas). Escribe las letras de los reptiles.", "A y D", "La lagartija y la culebra tienen piel seca con escamas."),
      arith("En un estanque hay 7 truchas y 4 ranas. ¿Cuántos animales hay en total?", "7+4", "Se suman los peces y los anfibios del estanque."),
      ("Un animal adulto vive cerca del agua, tiene piel húmeda y de pequeño era un renacuajo. ¿A qué grupo pertenece?", "Anfibios", "Haber sido renacuajo y tener piel húmeda es propio de anfibios."),
  ],
  rea=[
      ("Un delfín nada y tiene aletas, pero respira con pulmones y da leche a su cría. ¿Es pez? Usa un rasgo.", "No, es mamífero porque respira con pulmones y da leche", "Los peces respiran con branquias y no dan leche."),
      ("Ema dice que una culebra es anfibio porque anda cerca del río. ¿Qué rasgo del cuerpo debe revisar para decidir?", "La piel: la culebra tiene escamas secas", "La piel con escamas secas indica reptil."),
  ],
  cha=[
      ("¿Qué tienen en común un reptil, un anfibio adulto y un ave respecto de cómo respiran?", "Los tres respiran con pulmones", "Reptiles, aves y anfibios adultos usan pulmones."),
      ("Un animal tiene escamas y respira con pulmones. Otro tiene escamas y respira con branquias. ¿Cuál es pez y cuál es reptil?", "El de branquias es pez; el de pulmones es reptil", "La respiración separa a peces y reptiles con escamas."),
  ],
  context=[("En el río hay una trucha, una rana y una culebra de agua. Escribe en orden el grupo de cada una: pez, anfibio o reptil.", "Trucha: pez; rana: anfibio; culebra: reptil", "Cada animal tiene los rasgos de su grupo.")],
  selfcheck=[("¿Qué animal tiene piel húmeda y sin escamas: lagartija o rana?", "Rana", "La rana es anfibio y tiene piel húmeda."), ("¿Con qué respiran los peces?", "Con branquias", "Toman el oxígeno que hay en el agua."), ("¿Una tortuga es pez, anfibio o reptil?", "Reptil", "Tiene piel seca y respira con pulmones.")],
  open_task=task("Completa una tabla con tres columnas, reptil, anfibio y pez. Pon cada animal en su columna y escribe un rasgo: lagartija (piel seca con escamas), rana (piel húmeda y sin escamas), salmón (aletas y branquias), culebra (piel seca con escamas), sapo (piel húmeda), trucha (aletas y branquias).", "Reptil: lagartija y culebra, piel seca con escamas. Anfibio: rana y sapo, piel húmeda. Pez: salmón y trucha, aletas y branquias.", ["pone cada animal en su grupo", "escribe un rasgo por grupo", "usa la piel o la respiración"], ["tabla de tres columnas"], ["agrupar por el lugar donde vive", "confundir escamas de reptil con las de pez"], "Valora que cite la piel o la respiración y pide justificar un animal que estuvo a punto de poner en otra columna."),
  reinforce="Dibuja una rana adulta y un renacuajo. Escribe debajo cómo respira cada uno.",
  extend="Explica con dos rasgos por qué una trucha y una lagartija no están en el mismo grupo.")

L(OA1, 4,
  materials="Este cuaderno con la clave de clasificación y las fichas de seis animales. Lápiz y tijeras si quieres recortar las fichas.",
  use="Aprenderé a usar una clave de clasificación con preguntas de Sí o No. Sirve para identificar el grupo de un animal paso a paso.",
  prior=["Conozco los cinco grupos de vertebrados.", "Sé responder preguntas con Sí o No."],
  explain=[
      "Una clave de clasificación es una lista de preguntas con respuesta Sí o No. Cada respuesta te lleva a otra pregunta o a un grupo. Así puedes ordenar un animal sin adivinar, siguiendo siempre los mismos pasos.",
      "Esta es la clave de hoy. Pregunta 1: ¿tiene pelo y las crías toman leche? Si es Sí, es mamífero; si es No, sigue. Pregunta 2: ¿tiene plumas? Sí es ave. Pregunta 3: ¿tiene aletas y branquias? Sí es pez. Pregunta 4: ¿su piel es húmeda y sin escamas? Sí es anfibio; si es No, es reptil.",
      "Para usar la clave, parte siempre en la pregunta 1 y no te saltes ninguna. Si dudas, vuelve a leer los datos del animal. Una clave bien usada llega a un solo grupo, y otra persona que use los mismos datos llega al mismo resultado.",
  ],
  vocab=[("clave de clasificación", "serie de preguntas Sí o No que lleva a un grupo"), ("rasgo", "característica del cuerpo que puedo observar"), ("grupo", "conjunto de animales con rasgos parecidos"), ("criterio", "regla que uso para separar los grupos"), ("evidencia", "dato que muestra que mi respuesta es correcta")],
  worked=[
      ("Usar la clave con un animal", "Animal X: tiene plumas y no tiene pelo. ¿Qué grupo señala la clave?", ["Pregunta 1: ¿tiene pelo? No, sigo.", "Pregunta 2: ¿tiene plumas? Sí.", "La clave se detiene aquí: es un ave."], "Ave"),
      ("Un animal que llega al final", "Animal Y: sin pelo, sin plumas, sin aletas ni branquias, piel seca con escamas. ¿Qué grupo señala la clave?", ["Pregunta 1: ¿pelo? No. Pregunta 2: ¿plumas? No.", "Pregunta 3: ¿aletas y branquias? No.", "Pregunta 4: ¿piel húmeda y sin escamas? No. Entonces es reptil."], "Reptil"),
  ],
  mistakes=[
      ("Empezar la clave por la pregunta 3.", "Se salta el orden y se puede llegar a un grupo incorrecto.", "Parte siempre en la pregunta 1 y avanza por orden."),
      ("Responder Sí a todo porque el animal «se parece».", "No se revisan los datos del animal.", "Responde solo con los datos de la ficha: si no está, la respuesta es No."),
  ],
  rec=[
      ("En la clave, ¿cuál es la primera pregunta?", "¿Tiene pelo y las crías toman leche?", "La clave siempre se empieza por la pregunta 1."),
      ("Un animal responde Sí a «¿tiene plumas?». ¿Qué grupo señala la clave?", "Ave", "Tener plumas lleva al grupo de las aves."),
      ("¿Qué tipo de respuestas tiene cada pregunta de una clave?", "Sí o No", "Una clave usa preguntas de dos respuestas."),
  ],
  und=[
      ("¿Para qué sirve una clave de clasificación?", "Para llegar a un grupo siguiendo preguntas", "Ordena la decisión en pasos."),
      ("Un animal tiene aletas y branquias y no tiene pelo ni plumas. ¿En qué pregunta se detiene la clave?", "En la pregunta 3", "Responde Sí a aletas y branquias y llega a pez."),
      ("Si una pregunta no tiene datos en la ficha, ¿qué se responde?", "No", "Solo se responde Sí con datos que aparecen en la ficha."),
  ],
  app=[
      ("Ficha 1: tiene pelo y sus crías toman leche. Usa la clave y escribe el grupo.", "Mamífero", "La pregunta 1 se responde Sí y la clave se detiene."),
      ("Ficha 2: sin pelo ni plumas; piel húmeda y sin escamas; sin aletas ni branquias de adulto. Usa la clave y escribe el grupo.", "Anfibio", "Responde No a 1, 2 y 3 y Sí a la pregunta 4 (piel húmeda y sin escamas)."),
      ("Ficha 3: sin pelo, sin plumas, con aletas y branquias. Usa la clave y escribe el grupo.", "Pez", "Responde No a las preguntas 1 y 2 y Sí a la pregunta 3."),
  ],
  rea=[
      ("Una ficha dice: «sin pelo, sin plumas, sin aletas, piel seca con escamas». Daniela escribió «anfibio». ¿Qué pregunta de la clave debió revisar y cuál es el grupo correcto?", "La pregunta 4; es reptil", "La piel seca con escamas no es húmeda, y la clave lleva a reptil."),
      ("Dos niños usan la clave con la misma ficha y llegan a grupos distintos. ¿Qué es lo más probable que haya pasado?", "Alguno se saltó un paso o leyó mal un dato", "Con los mismos datos y los mismos pasos el resultado es único."),
  ],
  cha=[
      ("Escribe qué ficha de animal haría que la clave se detenga en la pregunta 2.", "Una ficha de ave: sin pelo y con plumas", "Para que se detenga allí debe responder Sí a plumas y No a pelo."),
      ("¿Por qué conviene preguntar primero por el pelo antes que por vivir en el agua?", "Porque pelo es un rasgo del cuerpo y vivir en el agua no define el grupo", "Una clave usa rasgos del cuerpo y no el lugar donde vive."),
  ],
  context=[("Ficha del zorro culpeo, animal de Chile: «tiene pelo, sus crías toman leche, camina en cuatro patas». Usa la clave y escribe cuántas preguntas necesitas responder para clasificarlo.", "1 pregunta", "En la primera pregunta se responde Sí y llegas a mamífero.")],
  selfcheck=[("¿Dónde se parte siempre en una clave?", "En la pregunta 1", "El orden evita errores."), ("Un animal con piel seca y escamas, sin aletas, ¿qué grupo es?", "Reptil", "La clave llega a reptil al final."), ("¿Cada pregunta de la clave tiene respuesta Sí o No?", "Sí", "Así se llega a un grupo claro.")],
  open_task=task("Usa la clave con tres fichas. Ficha A: pelo y leche. Ficha B: piel húmeda y sin escamas, sin pelo ni plumas ni aletas. Ficha C: aletas y branquias. Escribe en cada caso el número de las preguntas que respondiste y el grupo final. Luego inventa una ficha tuya y clasifícala.", "A: pregunta 1 Sí, mamífero. B: preguntas 1, 2 y 3 No, pregunta 4 Sí, anfibio. C: preguntas 1 y 2 No, pregunta 3 Sí, pez.", ["usa la clave en orden", "llega al grupo correcto en las tres fichas", "crea una ficha propia con datos suficientes"], ["registro de preguntas y respuestas", "ficha propia clasificada"], ["saltarse preguntas", "ficha propia sin datos"], "Revisa el orden de las preguntas y pide que cambie un dato de su ficha para ver si cambia el grupo."),
  reinforce="Recorta las cuatro preguntas de la clave y ordénalas sobre la mesa. Usa una ficha cualquiera para recorrerlas.",
  extend="Escribe una pregunta que sirva para separar dos animales del mismo grupo de la clave, como una tortuga y una lagartija, que son reptiles.")

# ---------------------------------------------------------------- OA 02
L(OA2, 1,
  materials="Este cuaderno con las tarjetas de observación. Si quieres mirar un animal pequeño en el patio, usa una lupa o un frasco transparente y devuélvelo donde estaba, con un adulto cerca.",
  use="Aprenderé a buscar pistas que muestren que un animal no tiene columna. Sirve para observar animales pequeños sin dañarlos.",
  prior=["Sé que los vertebrados tienen columna vertebral.", "Sé mirar con cuidado y no tocar animales que no conozco."],
  explain=[
      "Los animales sin columna vertebral se llaman invertebrados. Hay muchísimos: insectos, arañas, caracoles, lombrices y jaibas. Para saber si un animal no tiene columna, buscamos pistas que podamos observar sin hacerle daño.",
      "Una pista es el cuerpo. Un invertebrado tiene el cuerpo blando, como el caracol, o cubierto por una armadura dura por fuera, como la jaiba o el escarabajo. En un vertebrado, los huesos están por dentro y se pueden sentir bajo la piel.",
      "Otra pista es no sentir una fila de huesitos en el lomo. Pero cuidado: no hay que apretar a un animal vivo. Mira, dibuja y anota. Si la ficha dice que el animal tiene el cuerpo blando o una cubierta dura por fuera, eso es evidencia de que es invertebrado.",
  ],
  vocab=[("invertebrado", "animal que no tiene columna vertebral"), ("evidencia", "pista que observo y que sostiene mi respuesta"), ("cuerpo blando", "cuerpo sin huesos y fácil de doblar"), ("armadura externa", "cubierta dura que protege el cuerpo por fuera"), ("observar", "mirar con atención y anotar lo que veo")],
  worked=[
      ("Buscar evidencia con una ficha", "Ficha: «Lombriz de tierra. Cuerpo largo, blando, sin patas, sin huesos». ¿Es invertebrada?", ["Busco la evidencia: cuerpo blando y sin huesos.", "Un animal sin huesos no tiene columna.", "Concluyo con esa evidencia."], "Sí, es invertebrada"),
      ("Una armadura por fuera", "Ficha: «Escarabajo. Cuerpo cubierto por una capa dura por fuera. No tiene huesos por dentro». ¿Es invertebrado?", ["La capa dura está por fuera, no por dentro.", "No tiene huesos por dentro.", "Sin huesos por dentro no hay columna."], "Sí, es invertebrado"),
  ],
  mistakes=[
      ("Apretar al animal para sentir si tiene huesos.", "Se puede dañar al animal y no es necesario.", "Observa sin tocar y usa la ficha o la lupa."),
      ("Decir «tiene una cubierta dura, entonces tiene columna».", "Se confunde la cubierta externa con huesos por dentro.", "Una cubierta dura por fuera no es columna: la columna está por dentro."),
  ],
  rec=[
      ("Un animal sin columna vertebral, ¿se llama vertebrado o invertebrado?", "Invertebrado", "Sin columna se llama invertebrado."),
      ("Un caracol tiene el cuerpo blando. ¿Es una pista de que es invertebrado?", "Sí", "Un cuerpo blando y sin huesos indica que no hay columna."),
      ("Para observar un animal pequeño, ¿hay que mirarlo o apretarlo?", "Mirarlo", "Observar sin dañar es la regla."),
  ],
  und=[
      ("Explica con tus palabras qué es una evidencia.", "Una pista que observo y que sostiene mi respuesta", "La evidencia respalda lo que digo."),
      ("Una jaiba tiene una cubierta dura por fuera. ¿Esa cubierta es una columna vertebral?", "No", "La columna es de huesitos por dentro; la cubierta de la jaiba está por fuera."),
      ("¿Por qué no hay que apretar a un animal para saber si tiene columna?", "Porque se le puede hacer daño", "Mirar basta y cuida al animal."),
  ],
  app=[
      ("Fichas: A mariposa (sin huesos, cuerpo con cubierta fina), B perro (huesos por dentro), C caracol (cuerpo blando), D conejo (huesos por dentro). Escribe las letras de los invertebrados.", "A y C", "La mariposa y el caracol no tienen huesos por dentro."),
      arith("En el patio un niño anota 9 animales pequeños. 6 son invertebrados sin columna y el resto son lagartijas. ¿Cuántas lagartijas hay?", "9-6", "Se resta a los 9 animales los 6 invertebrados."),
      ("Una ficha dice: «Cuerpo muy largo, blando, sin patas y sin huesos». ¿Qué animal de este cuaderno es?", "Lombriz de tierra", "Es la descripción de la lombriz usada en la clase."),
  ],
  rea=[
      ("Joaquín vio una araña y dijo: «tiene un cuerpo duro, entonces tiene columna». ¿Qué evidencia necesita para saber si tiene columna?", "Que tenga huesos por dentro en el lomo, y no una cubierta por fuera", "La cubierta externa no es columna."),
      ("Una radiografía muestra huesos por dentro en un gato y ningún hueso en una hormiga. ¿Cuál de los dos es invertebrado?", "La hormiga", "No tiene huesos por dentro, entonces no tiene columna."),
  ],
  cha=[
      ("Un compañero dice: «Si un animal es muy grande, tiene columna». Una medusa grande no tiene huesos. ¿Qué respondes?", "Que no siempre; la medusa es grande y no tiene columna", "El tamaño no decide si hay columna."),
      ("Propón dos pistas distintas que se puedan observar sin tocar para decidir si un animal es invertebrado.", "Por ejemplo: cuerpo blando y cubierta dura por fuera", "Son pistas visibles que no dañan al animal."),
  ],
  context=[("En el jardín, Ema anota: «caracol: cuerpo blando; lombriz: cuerpo blando; gorrión: tiene huesos por dentro». ¿Cuántos de los animales que anotó son invertebrados?", "2", "El caracol y la lombriz son blandos y sin columna.")],
  selfcheck=[("¿Dónde está la columna de un vertebrado: por dentro o por fuera?", "Por dentro", "Está dentro del cuerpo, bajo la piel."), ("¿Se debe apretar a un animal para observarlo?", "No", "Se puede dañar."), ("¿Un cuerpo blando es pista de invertebrado?", "Sí", "No hay huesos en un cuerpo blando.")],
  open_task=task("Mira estas tres fichas y escribe si cada animal es invertebrado, con la evidencia. Ficha 1: caracol, cuerpo blando. Ficha 2: jaiba, cubierta dura por fuera. Ficha 3: trucha, huesos por dentro. Dibuja uno de los animales y marca la evidencia.", "Ficha 1: invertebrado, tiene cuerpo blando. Ficha 2: invertebrado, tiene una cubierta dura por fuera. Ficha 3: vertebrado, tiene huesos por dentro.", ["clasifica las tres fichas", "escribe una evidencia por ficha", "dibuja y marca la evidencia"], ["tabla con evidencia", "dibujo con flecha"], ["usar el tamaño como evidencia", "confundir cubierta externa con columna"], "Comprueba que cada evidencia sea una pista observable y pide que explique la diferencia entre cubierta externa y huesos internos."),
  reinforce="Si tienes un jardín, mira durante cinco minutos sin tocar y anota dos animales que veas. Dibuja si parecen blandos o con cubierta dura.",
  extend="Elige un animal sin columna que conozcas y escribe dos evidencias que se puedan observar sin dañarlo.")

L(OA2, 2,
  materials="Este cuaderno con las tarjetas de insectos y arañas. Si quieres comprobar en casa, mira una hormiga o una mosca con una lupa, sin tocarla, con un adulto cerca.",
  use="Aprenderé a reconocer un insecto por sus rasgos. Sirve para saber que una hormiga, una abeja y una mariposa son insectos y que una araña no lo es.",
  prior=["Sé que los invertebrados no tienen columna vertebral.", "Sé contar hasta 30."],
  explain=[
      "Los insectos son invertebrados con seis patas. Su cuerpo tiene tres partes: la cabeza, el tórax y el abdomen. En la cabeza tienen dos antenas, que les sirven para sentir el entorno. Muchos tienen alas, que salen del tórax.",
      "La hormiga, la abeja, la mariposa, la mosca y el escarabajo son insectos. Todos tienen seis patas, aunque algunos tengan alas y otros no. Una cubierta dura por fuera, que se llama exoesqueleto, protege su cuerpo.",
      "No todo animal pequeño con muchas patas es un insecto. La araña tiene ocho patas, así que no es insecto. Para decidir, cuenta las patas y mira las partes del cuerpo. Seis patas y tres partes: es un insecto.",
  ],
  vocab=[("insecto", "invertebrado con seis patas, tres partes del cuerpo y dos antenas"), ("antena", "parte de la cabeza que sirve para sentir el entorno"), ("tórax", "parte del medio del cuerpo, donde se unen las patas"), ("abdomen", "parte final del cuerpo"), ("exoesqueleto", "cubierta dura que protege el cuerpo por fuera")],
  worked=[
      ("Contar las patas", "Una hormiga tiene 6 patas. ¿Cuántas patas tienen 4 hormigas?", ["Cada hormiga tiene 6 patas.", "Hay 4 hormigas: sumo 6 + 6 + 6 + 6.", "6 + 6 = 12, 12 + 6 = 18 y 18 + 6 = 24."], "24 patas"),
      ("Insecto o no", "Un animal pequeño tiene 8 patas y dos partes en el cuerpo. ¿Es un insecto?", ["Los insectos tienen 6 patas.", "Este animal tiene 8, así que no encaja.", "Tampoco tiene tres partes en el cuerpo."], "No es insecto"),
  ],
  mistakes=[
      ("Decir «la araña es un insecto porque es chica y tiene patas».", "Se mira el tamaño y no el número de patas.", "Cuenta las patas: la araña tiene 8 y los insectos tienen 6."),
      ("Decir «sin alas no es insecto».", "Se cree que todos los insectos vuelan.", "Algunos insectos, como muchas hormigas, no tienen alas. Cuenta las patas y mira las tres partes del cuerpo."),
  ],
  rec=[
      ("¿Cuántas patas tiene un insecto?", "6", "Seis patas es el rasgo principal de los insectos."),
      ("¿Cómo se llaman las tres partes del cuerpo de un insecto? Escribe la primera.", "Cabeza", "El cuerpo se divide en cabeza, tórax y abdomen."),
      ("¿Qué parte de la cabeza usan para sentir el entorno?", "Antenas", "Los insectos tienen dos antenas."),
  ],
  und=[
      ("Nombra tres insectos.", "Por ejemplo: hormiga, abeja y mariposa", "Son insectos con seis patas."),
      ("¿Por qué el escarabajo, que tiene una cubierta dura, sigue siendo invertebrado?", "Porque la cubierta está por fuera y no tiene columna", "El exoesqueleto no es columna."),
      ("¿Para qué sirve el exoesqueleto de un insecto?", "Para proteger su cuerpo", "Es una cubierta dura por fuera."),
  ],
  app=[
      arith("Una abeja tiene 6 patas. ¿Cuántas patas tienen 5 abejas?", "5*6", "Se multiplican las abejas por las 6 patas de cada una."),
      ("Tarjetas: A mosca (6 patas), B araña (8 patas), C escarabajo (6 patas), D mariposa (6 patas). Escribe las letras de los insectos.", "A, C y D", "Tienen seis patas."),
      ("Un insecto tiene 2 antenas. ¿En qué parte del cuerpo están?", "En la cabeza", "Las antenas salen de la cabeza."),
  ],
  rea=[
      ("Carla vio un animal con alas y dijo «es insecto». El animal tenía plumas, pico y dos patas. ¿Qué datos muestran que Carla se equivoca?", "No tiene seis patas y tiene pico y plumas: es un ave", "Los insectos tienen seis patas y no tienen plumas."),
      ("Una hormiga sin alas y una mariposa con alas, ¿son los dos insectos? Usa el número de patas.", "Sí, ambos tienen seis patas", "Las alas no deciden: el número de patas sí."),
  ],
  cha=[
      arith("En un hormiguero de dibujo hay 3 hormigas y 2 escarabajos. Cada uno tiene 6 patas. ¿Cuántas patas hay en total?", "(3+2)*6", "Se suman los insectos y se multiplican por 6 patas."),
      ("Hay dos animales: uno con 6 patas y 2 antenas y otro con 8 patas y sin antenas. ¿Cuál es el insecto y cómo lo supiste?", "El de 6 patas y 2 antenas", "Las patas y las antenas son los rasgos del insecto."),
  ],
  context=[("En la plaza ves una abeja en una flor, una araña en su tela y una mariposa en una hoja. ¿Cuántos de los tres animales son insectos?", "2", "La abeja y la mariposa tienen seis patas; la araña tiene ocho.")],
  selfcheck=[("¿Cuántas partes tiene el cuerpo de un insecto?", "Tres", "Cabeza, tórax y abdomen."), ("¿La araña es insecto?", "No", "Tiene ocho patas."), ("¿Un insecto sin alas es insecto?", "Sí", "Lo decide el número de patas.")],
  open_task=task("Dibuja un insecto de tu elección entre estos: hormiga, mariposa o abeja. Pinta la cabeza, el tórax y el abdomen de colores distintos. Dibuja sus seis patas y sus dos antenas. Debajo escribe una frase que diga por qué no es una araña.", "Dibujé una hormiga con tres partes pintadas, seis patas y dos antenas. No es una araña porque tiene seis patas y la araña tiene ocho.", ["dibuja tres partes del cuerpo", "dibuja seis patas", "dibuja dos antenas", "explica la diferencia con la araña"], ["dibujo pintado", "frase de explicación"], ["dibujar ocho patas", "poner las antenas en el abdomen"], "Revisa que las patas salgan del tórax y que la frase use el número de patas como razón."),
  reinforce="Cuenta las patas de tres insectos que veas en un dibujo del cuaderno y confirma que son seis cada uno.",
  extend="Investiga con un adulto si una hormiga puede tener alas y escribe qué descubriste con una frase.")

L(OA2, 3,
  materials="Este cuaderno con las fichas de arañas, escorpiones, jaibas y camarones. No hace falta tocar animales; las fichas traen los datos.",
  use="Aprenderé a reconocer arácnidos y crustáceos. Sirve para distinguir una araña de un insecto y una jaiba de un pez.",
  prior=["Sé que los insectos tienen seis patas.", "Sé que los invertebrados no tienen columna."],
  explain=[
      "Los arácnidos tienen ocho patas y el cuerpo en dos partes. No tienen antenas ni alas. La araña y el escorpión son arácnidos. Muchas arañas fabrican seda y tejen telas para atrapar su alimento.",
      "Los crustáceos tienen una cubierta dura por fuera, llamada caparazón, y varias patas. Tienen antenas y la mayoría vive en el agua. La jaiba, el camarón, la langosta y el picoroco son crustáceos. La jaiba tiene diez patas, incluidas las pinzas.",
      "Para diferenciar, cuenta las patas y mira las antenas. Seis patas y tres partes: insecto. Ocho patas y sin antenas: arácnido. Caparazón duro, muchas patas y antenas, casi siempre en el agua: crustáceo. Los tres grupos son invertebrados.",
  ],
  vocab=[("arácnido", "invertebrado con ocho patas y dos partes del cuerpo, sin antenas"), ("crustáceo", "invertebrado con caparazón duro, muchas patas y antenas"), ("caparazón", "cubierta dura que protege el cuerpo por fuera"), ("pinza", "pata final de la jaiba que sirve para sujetar"), ("seda", "hilo fino que fabrican las arañas")],
  worked=[
      ("Reconocer un arácnido", "Ficha: «8 patas, 2 partes del cuerpo, sin antenas». ¿Es arácnido?", ["Cuento: 8 patas.", "Las antenas faltan.", "Esos rasgos son de un arácnido."], "Sí, es un arácnido"),
      ("Reconocer un crustáceo", "Ficha: «caparazón duro, 10 patas, antenas, vive en el agua». ¿Es crustáceo?", ["El caparazón y las antenas son rasgos de crustáceo.", "Vive en el agua, como la mayoría.", "Coincide con la jaiba."], "Sí, es un crustáceo"),
  ],
  mistakes=[
      ("Decir «la jaiba es un pez porque vive en el agua».", "Se mira el lugar y no el cuerpo.", "La jaiba no tiene columna ni aletas; tiene caparazón y diez patas: es un crustáceo."),
      ("Decir «la araña es un insecto».", "No se cuentan las patas.", "La araña tiene ocho patas; los insectos tienen seis. Es un arácnido."),
  ],
  rec=[
      ("¿Cuántas patas tiene un arácnido?", "8", "Ocho patas es el rasgo de los arácnidos."),
      ("¿Qué cubierta dura protege el cuerpo de una jaiba?", "El caparazón", "El caparazón es su cubierta externa."),
      ("La araña, ¿es arácnido o crustáceo?", "Arácnido", "Tiene ocho patas y no tiene antenas."),
  ],
  und=[
      ("Nombra dos crustáceos.", "Por ejemplo: jaiba y camarón", "Son crustáceos de esta clase."),
      ("¿Qué diferencia hay entre un insecto y un arácnido en el número de patas?", "El insecto tiene seis y el arácnido ocho", "Se cuentan las patas."),
      ("¿Qué tienen en común los insectos, los arácnidos y los crustáceos?", "No tienen columna vertebral", "Los tres grupos son invertebrados."),
  ],
  app=[
      arith("Una jaiba tiene 10 patas. ¿Cuántas patas tienen 3 jaibas?", "3*10", "Se multiplica el número de jaibas por 10."),
      ("Fichas: A araña (8 patas, sin antenas), B abeja (6 patas), C jaiba (caparazón, 10 patas), D escorpión (8 patas, sin antenas). Escribe las letras de los arácnidos.", "A y D", "Ocho patas y sin antenas."),
      arith("Una araña tiene 8 patas y una hormiga 6. ¿Cuántas patas más tiene la araña?", "8-6", "Se resta el número de patas de la hormiga al de la araña."),
  ],
  rea=[
      ("Un niño vio un animal con ocho patas y sin antenas y escribió «es crustáceo». ¿Qué grupo es y qué dato lo muestra?", "Arácnido; tiene ocho patas y no tiene antenas", "Esos rasgos son de arácnido."),
      ("Un camarón vive en el agua, tiene antenas y caparazón. ¿Es pez? Explica con un rasgo.", "No, es crustáceo porque tiene caparazón y no tiene columna", "El caparazón es rasgo de crustáceo."),
  ],
  cha=[
      ("Hay tres animales: A con 6 patas, B con 8 patas y sin antenas, C con caparazón y 10 patas. Escribe el grupo de cada uno.", "A insecto, B arácnido, C crustáceo", "Cada animal cumple los rasgos de su grupo."),
      ("Tienes que explicar a un amigo cómo distinguir una araña de una hormiga sin tocarlas. ¿Qué dos cosas le pides que mire?", "El número de patas y si tienen antenas", "La araña tiene 8 patas y no tiene antenas; la hormiga 6 y sí."),
  ],
  context=[("En la playa, un niño mira una jaiba bajo una roca, una araña en la pared de una casa y una gaviota. ¿Cuántos de estos tres animales son invertebrados?", "2", "La jaiba y la araña no tienen columna; la gaviota sí.")],
  selfcheck=[("¿Cuántas patas tiene la araña?", "8", "La araña es un arácnido."), ("¿Dónde vive la mayoría de los crustáceos?", "En el agua", "Jaibas, camarones y picorocos viven en el agua."), ("¿Los arácnidos tienen antenas?", "No", "No tienen antenas.")],
  open_task=task("Elige uno de estos animales, araña o jaiba, y haz una ficha con su dibujo. Escribe el grupo, cuántas patas tiene y un rasgo que lo distingue de un insecto.", "Araña: arácnido, ocho patas, sin antenas, no es insecto porque tiene ocho patas.", ["dibuja el animal", "escribe el grupo", "escribe el número de patas", "da un rasgo que lo distingue"], ["dibujo", "ficha con tres datos"], ["decir que la araña tiene seis patas", "decir que la jaiba es un pez"], "Revisa que el número de patas sea correcto y pide que diga cómo cambiaría la ficha si fuera un insecto."),
  reinforce="Dibuja una araña y una jaiba una al lado de la otra y escribe cuántas patas tiene cada una.",
  extend="Piensa qué ventaja tiene un caparazón duro para un animal que vive entre las rocas del mar.")

L(OA2, 4,
  materials="Este cuaderno con una tabla de comparación y fichas de seis animales. Lápiz y lápices de colores.",
  use="Aprenderé a comparar vertebrados e invertebrados. Sirve para ordenar muchos animales en dos grandes grupos.",
  prior=["Conozco los cinco grupos de vertebrados.", "Conozco insectos, arácnidos y crustáceos."],
  explain=[
      "Los vertebrados tienen columna vertebral y un esqueleto de huesos por dentro. Son mamíferos, aves, reptiles, anfibios y peces. Los invertebrados no tienen columna. Su cuerpo puede ser blando, como el del caracol, o estar cubierto por una armadura por fuera.",
      "Hay más animales invertebrados que vertebrados. Entre los invertebrados están los insectos, los arácnidos y los crustáceos, y también los caracoles y las lombrices. Los invertebrados viven en tierra, en agua y en el aire.",
      "Cuando compares, usa el mismo criterio para todos: ¿tiene columna? Después mira otros rasgos, como el número de patas o la cubierta del cuerpo. Una tabla de dos columnas ayuda a ordenar lo que observas y a ver qué se parece y qué es distinto.",
  ],
  vocab=[("esqueleto interno", "huesos que están por dentro del cuerpo"), ("exoesqueleto", "cubierta dura que está por fuera del cuerpo"), ("comparar", "buscar qué se parece y qué es distinto"), ("tabla", "cuadro para ordenar datos en filas y columnas"), ("criterio", "regla que uso para ordenar")],
  worked=[
      ("Comparar dos animales", "Compara un gato y una hormiga. El gato tiene columna y pelo. La hormiga tiene seis patas y exoesqueleto.", ["Pregunta con el mismo criterio: ¿tiene columna?", "El gato sí es vertebrado.", "La hormiga no tiene columna: es invertebrada."], "El gato es vertebrado y la hormiga es invertebrada"),
      ("Ordenar en una tabla", "Ordena en vertebrado o invertebrado: gaviota, caracol, trucha, araña.", ["Gaviota tiene columna: vertebrado.", "Caracol no tiene: invertebrado.", "Trucha tiene: vertebrado. Araña no tiene: invertebrado."], "Vertebrados: gaviota y trucha; invertebrados: caracol y araña"),
  ],
  mistakes=[
      ("Decir «los animales con patas son vertebrados».", "Se usa un solo rasgo que no decide.", "Las arañas tienen ocho patas y son invertebradas. El criterio es la columna."),
      ("Poner a la jaiba con los peces.", "Se agrupa por el lugar donde vive.", "La jaiba no tiene columna; es invertebrada."),
  ],
  rec=[
      ("¿Qué animal tiene columna vertebral: el gato o el caracol?", "El gato", "El gato es vertebrado."),
      ("El caracol, ¿es vertebrado o invertebrado?", "Invertebrado", "No tiene columna."),
      ("¿Dónde están los huesos de un vertebrado: por dentro o por fuera?", "Por dentro", "Los vertebrados tienen esqueleto interno."),
  ],
  und=[
      ("¿Qué diferencia hay entre esqueleto interno y exoesqueleto?", "El interno está dentro del cuerpo y el exoesqueleto está por fuera", "La ubicación de la parte dura es la diferencia."),
      ("Nombra dos vertebrados y dos invertebrados.", "Por ejemplo: perro y rana; hormiga y jaiba", "Los primeros tienen columna y los segundos no."),
      ("¿Qué criterio usas primero para separar vertebrados e invertebrados?", "Si tienen columna vertebral", "Es el criterio que define los dos grupos."),
  ],
  app=[
      ("Ordena en vertebrado o invertebrado: A rana, B mariposa, C salmón, D escorpión. Escribe las letras de los invertebrados.", "B y D", "La mariposa y el escorpión no tienen columna."),
      arith("En una lámina hay 12 animales. 7 son invertebrados. ¿Cuántos son vertebrados?", "12-7", "Se resta a los 12 animales los 7 invertebrados."),
      arith("Un niño dibujó 3 insectos y 2 arañas. ¿Cuántas patas dibujó en total si cada insecto tiene 6 y cada araña 8?", "3*6+2*8", "Primero se calculan las patas de los insectos y de las arañas y luego se suman."),
  ],
  rea=[
      ("Una lagartija y una araña tienen cuatro y ocho patas. Ana dice que ambas son del mismo grupo porque tienen patas. ¿Tiene razón?", "No; la lagartija es vertebrada y la araña no", "Tener patas no decide: la columna sí."),
      ("¿Por qué una tabla con el mismo criterio para todos los animales es mejor que ordenarlos por tamaño?", "Porque el tamaño no decide si tienen columna", "El mismo criterio permite comparar con justicia."),
  ],
  cha=[
      ("Escribe una diferencia y una semejanza entre un perro y una jaiba.", "Diferencia: el perro tiene columna y la jaiba no. Semejanza: ambos tienen patas", "Se comparan los dos animales con datos."),
      ("Hay 10 animales y 4 son vertebrados. ¿Cuántos no tienen columna y cuál grupo es el más numeroso?", "6; los invertebrados", "10 − 4 = 6, y 6 es mayor que 4."),
  ],
  context=[("En una charca hay cuatro ranas, tres caracoles y cinco libélulas. Las ranas tienen columna; los caracoles y las libélulas no. ¿Cuántos animales invertebrados hay en la charca?", "8", "3 caracoles más 5 libélulas son 8 invertebrados.")],
  selfcheck=[("¿Qué grupo de animales tiene columna vertebral?", "Los vertebrados", "Es la definición."), ("¿Un caracol es vertebrado?", "No", "No tiene columna."), ("¿Qué criterio separa los dos grupos?", "La columna vertebral", "Es el criterio común.")],
  open_task=task("Haz una tabla con dos columnas, vertebrados e invertebrados. Ordena estos animales: perro, hormiga, rana, jaiba, trucha, araña. Escribe debajo una semejanza y una diferencia entre dos animales de distinta columna.", "Vertebrados: perro, rana, trucha. Invertebrados: hormiga, jaiba, araña. Semejanza: el perro y la araña tienen patas. Diferencia: el perro tiene columna y la araña no.", ["ordena los seis animales", "escribe una semejanza", "escribe una diferencia con columna"], ["tabla completa", "frases de comparación"], ["ordenar por el lugar donde viven"], "Valora el uso del criterio de la columna y pide que cambie un animal de columna y justifique."),
  reinforce="Usa dos hojas y pega en cada una dibujos de vertebrados e invertebrados de una revista.",
  extend="Escribe por qué crees que hay más invertebrados que vertebrados, usando un ejemplo de tu patio o parque.")
