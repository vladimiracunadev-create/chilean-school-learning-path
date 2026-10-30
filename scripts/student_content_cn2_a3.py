"""Cuaderno del estudiante, 2.º básico Ciencias Naturales: OA 05 (animales nativos en peligro) y OA 06 (actividad humana)."""
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


OA5, OA6 = "CN02 OA 05", "CN02 OA 06"

# ---------------------------------------------------------------- OA 05
L(OA5, 1,
  materials="Este cuaderno con las tarjetas de ocho animales y lápices de colores. No necesitas salir de casa.",
  use="Aprenderé qué significa que un animal sea nativo de Chile. Sirve para distinguir los animales que viven naturalmente en nuestro país de los que trajo la gente.",
  prior=["Sé nombrar animales de la granja y del campo.", "Sé que hábitat es el lugar donde vive un animal."],
  explain=[
      "Un animal nativo es un animal que vive de forma natural en un lugar, sin que la gente lo haya traído. El huemul, el puma, el zorro culpeo, el cóndor y el pudú son animales nativos de Chile. Llevan muchísimo tiempo viviendo aquí.",
      "Hay animales que viven en Chile pero no son nativos. La vaca, la oveja, el caballo y el gato llegaron con las personas desde otros países. Se llaman animales introducidos. Que un animal esté en Chile no basta para decir que es nativo.",
      "Que un animal sea nativo tampoco significa que haya muchos. Algunos animales nativos son muy comunes y otros son muy poco comunes. Para saber si un animal es nativo, hay que preguntar de dónde es y no cuántos hay.",
  ],
  vocab=[("nativo", "animal que vive de forma natural en un lugar"), ("introducido", "animal que llegó a un lugar traído por las personas"), ("huemul", "ciervo nativo de Chile que vive en el sur"), ("cóndor", "ave grande nativa de la cordillera de los Andes"), ("común", "animal del que hay muchos")],
  worked=[
      ("Decidir si es nativo", "El pudú es un ciervo pequeño que vive naturalmente en los bosques del sur de Chile. ¿Es nativo?", ["Pregunto: ¿vive aquí de forma natural?", "Sí, el pudú vive en los bosques del sur desde hace muchísimo tiempo.", "Nadie lo trajo."], "Sí, es nativo"),
      ("Un animal introducido", "La oveja llegó a Chile traída por personas desde otro continente. ¿Es nativa?", ["Pregunto de dónde viene.", "La gente la trajo.", "Entonces no es nativa."], "No, es introducida"),
  ],
  mistakes=[
      ("Decir «el caballo es nativo porque lo veo en el campo».", "Se confunde estar en un lugar con ser nativo.", "El caballo fue traído por personas; es introducido aunque viva en el campo."),
      ("Decir «nativo significa que hay muchos».", "Se mezcla nativo con común.", "Nativo habla del origen; hay animales nativos con muy pocos individuos."),
  ],
  rec=[
      ("El puma vive naturalmente en Chile. ¿Es nativo o introducido?", "Nativo", "Vive aquí desde siempre."),
      ("La vaca llegó con las personas. ¿Es nativa o introducida?", "Introducida", "Fue traída por las personas."),
      ("¿En qué parte de Chile vive el huemul, en el norte desierto o en el sur?", "En el sur", "Vive en el sur del país."),
  ],
  und=[
      ("¿Qué significa que un animal sea nativo?", "Que vive naturalmente en un lugar", "Es la definición de la clase."),
      ("¿Por qué una vaca en Chile no es un animal nativo?", "Porque la trajeron las personas", "No vivía aquí de forma natural."),
      ("¿Un animal nativo siempre es común? Explica.", "No; puede haber pocos", "Nativo habla del origen y no de la cantidad."),
  ],
  app=[
      ("Tarjetas: A cóndor, B oveja, C pudú, D gato, E huemul, F caballo. Escribe las letras de los nativos de Chile.", "A, C y E", "El cóndor, el pudú y el huemul viven naturalmente aquí."),
      arith("En una lámina hay 8 animales y 5 son nativos de Chile. ¿Cuántos son introducidos?", "8-5", "Se resta a los 8 animales los 5 nativos."),
      ("El zorro culpeo vive de forma natural en el campo de Chile. ¿Cómo lo clasificas: nativo o introducido?", "Nativo", "Vive aquí por naturaleza."),
  ],
  rea=[
      ("Un amigo dice: «El gato es nativo porque vive en todas las casas de Chile». ¿Qué le respondes?", "Que es introducido, porque lo trajeron las personas", "Estar en muchos lugares no lo hace nativo."),
      ("Un animal está en Chile hace solo 50 años porque lo trajeron barcos. ¿Es nativo? Explica.", "No; lo trajo la gente", "Los nativos viven aquí sin que los traigan."),
  ],
  cha=[
      ("Escribe dos animales nativos de Chile y uno introducido que conozcas.", "Por ejemplo: pudú y puma; vaca", "Los dos primeros viven aquí naturalmente."),
      ("Explica por qué preguntar «¿de dónde es?» es mejor que preguntar «¿cuántos hay?» para decidir si es nativo.", "Porque nativo habla del origen y no de la cantidad", "La cantidad puede cambiar y el origen no."),
  ],
  context=[("En una escuela del sur, los niños ven un pudú en el bosque, una vaca en el potrero y una oveja en el cerro. ¿Cuántos de los tres son animales nativos?", "1", "Solo el pudú es nativo; la vaca y la oveja son introducidas.")],
  selfcheck=[("¿El cóndor es nativo de Chile?", "Sí", "Vive de forma natural en los Andes."), ("¿La oveja es nativa?", "No", "Fue traída por las personas."), ("¿Nativo quiere decir que hay muchos?", "No", "Habla del origen.")],
  open_task=task("Clasifica estos seis animales en dos columnas, nativos e introducidos: huemul, caballo, cóndor, gato, pudú, vaca. Elige uno de los nativos, dibújalo y escribe en qué parte de Chile vive.", "Nativos: huemul, cóndor, pudú. Introducidos: caballo, gato, vaca. Dibujé el pudú, que vive en los bosques del sur.", ["clasifica los seis animales", "dibuja un nativo", "escribe dónde vive"], ["tabla de dos columnas", "dibujo con frase"], ["decir que un animal es nativo solo porque lo ve cerca"], "Valora la clasificación por origen y pide que explique por qué el gato no va en nativos."),
  reinforce="Con un adulto, nombra tres animales que veas cerca de tu casa y di si son nativos o introducidos.",
  extend="Pregunta en tu familia qué animales nativos de Chile conocen y anota dos.")

L(OA5, 2,
  materials="Este cuaderno con las tarjetas de cuatro animales y una tabla de conteos de práctica. Lápiz y lápices de colores.",
  use="Aprenderé qué significa que un animal esté en peligro de extinción. Sirve para entender por qué algunos animales nativos necesitan que los protejamos.",
  prior=["Sé qué es un animal nativo.", "Sé leer una tabla de números."],
  explain=[
      "Un animal está en peligro de extinción cuando quedan muy pocos y podrían desaparecer para siempre. Extinguirse significa que ya no queda ningún animal de esa especie en el mundo. Una vez extinto, no se puede recuperar.",
      "En Chile, algunos animales nativos están en peligro. El huemul, la chinchilla de cola corta, el picaflor de Arica y la ranita de Darwin son ejemplos. Son animales nativos de nuestro país y necesitan ayuda para sobrevivir.",
      "Para saber si un animal está en peligro, los especialistas cuentan cuántos quedan y miran si el número baja con los años. Si el número baja mucho, hay peligro. Los números de esta clase son de práctica y sirven para aprender a leer una tabla.",
  ],
  vocab=[("extinción", "desaparición total de una especie de animal"), ("en peligro", "animal del que quedan muy pocos y podría desaparecer"), ("especie", "tipo de animal, como el huemul o el puma"), ("especialista", "persona que estudia un tema a fondo"), ("conteo", "números que se anotan al contar animales")],
  worked=[
      ("Leer un conteo", "Conteo de práctica de un animal nativo: año 1: 40, año 2: 30, año 3: 18. ¿Está subiendo o bajando?", ["Los números son 40, 30 y 18.", "Cada número es menor que el anterior.", "El número baja con los años."], "Está bajando, hay peligro"),
      ("Qué es extinguirse", "¿Qué significa que una especie se extinga?", ["Es que quedan muy pocos y luego ninguno.", "Ya no queda ningún animal de esa especie en el mundo.", "Es para siempre."], "Que desaparece para siempre"),
  ],
  mistakes=[
      ("Decir «si un animal está en peligro, se puede traer otro igual desde otro país».", "Se piensa que se reemplaza fácilmente.", "Si se extingue una especie nativa, desaparece para siempre."),
      ("Decir «en peligro quiere decir que ataca a las personas».", "Se confunde peligro con ser peligroso.", "En peligro de extinción significa que el animal puede desaparecer."),
  ],
  rec=[
      ("¿Qué significa «extinción»?", "Que la especie desaparece para siempre", "Es la definición de la clase."),
      ("Quedan muy pocos huemules. ¿Está el huemul en peligro?", "Sí", "Quedan pocos y podría desaparecer."),
      ("¿El huemul es un animal nativo de Chile?", "Sí", "Vive naturalmente en el sur de Chile."),
  ],
  und=[
      ("Explica con tus palabras qué es «estar en peligro de extinción».", "Que quedan muy pocos y puede desaparecer", "Es la definición."),
      ("Nombra dos animales nativos de Chile que están en peligro.", "Por ejemplo: huemul y ranita de Darwin", "Son ejemplos de la clase."),
      ("¿Por qué los especialistas cuentan los animales cada cierto tiempo?", "Para ver si el número sube o baja", "Así saben si hay peligro."),
  ],
  app=[
      ("Conteo de práctica: año 1: 50, año 2: 38, año 3: 22. ¿El número sube o baja?", "Baja", "Cada año es menor."),
      arith("Un animal tenía 50 individuos en el año 1 y 22 en el año 3 en un conteo de práctica. ¿Cuántos individuos menos hay?", "50-22", "Se resta el número del año 3 al del año 1."),
      ("Conteo de práctica: año 1: 15, año 2: 20, año 3: 28. ¿Está en más o menos peligro con los años?", "En menos peligro", "El número sube."),
  ],
  rea=[
      ("Ema dice: «Si un animal tiene crías, ya no está en peligro». ¿Qué datos necesita mirar?", "Cuántos quedan en total y si el número sube o baja", "Una cría no basta si hay muy pocos."),
      ("Dos animales de práctica: A pasó de 30 a 10 y B pasó de 30 a 28. ¿Cuál preocupa más y por qué?", "El A, porque su número bajó mucho", "A perdió 20 y B perdió 2."),
  ],
  cha=[
      arith("En un conteo de práctica de la chinchilla de cola corta, en el año 1 se anotaron 90 y en el año 4 se anotaron 60. ¿Cuántos menos hay?", "90-60", "Se resta el número del año 4 al del año 1."),
      ("¿Por qué es importante cuidar a un animal nativo antes de que queden muy pocos?", "Porque si desaparece no se puede recuperar", "Una extinción es para siempre."),
  ],
  context=[("Una guía de un parque dice: «Este año vimos 12 huemules; el año pasado vimos 9». Son datos de práctica. ¿El número subió o bajó?", "Subió", "12 es mayor que 9.")],
  selfcheck=[("¿Qué es la extinción?", "Que una especie desaparece", "Ya no queda ninguna."), ("Si el número de animales baja cada año, ¿crees que hay más o menos peligro?", "Más peligro", "Cada vez quedan menos."), ("¿El huemul es nativo?", "Sí", "Vive en el sur de Chile.")],
  open_task=task("Mira este conteo de práctica de un animal nativo: año 1: 60, año 2: 48, año 3: 35, año 4: 20. Haz un gráfico de barras sencillo con cuatro barras. Escribe una frase que diga si está en peligro y por qué.", "Las barras bajan de 60 a 20. Creo que está en peligro porque cada año hay menos animales.", ["dibuja cuatro barras de distinta altura", "escribe si el número sube o baja", "da una razón con números"], ["gráfico de barras", "frase con números"], ["no usar los números", "decir que sube"], "Valora que cite al menos dos números del conteo y pide que explique qué ayudaría al animal."),
  reinforce="Dibuja un huemul y escribe debajo la palabra «nativo» y la frase «necesita protección».",
  extend="Averigua con un adulto qué cuidado hay en un parque nacional cercano para los animales nativos.")

L(OA5, 3,
  materials="Este cuaderno con las tarjetas de amenazas y de animales nativos. Lápices de colores.",
  use="Aprenderé cuáles son las amenazas que dañan el hábitat de los animales nativos. Sirve para entender qué cosas ponen en peligro a un animal.",
  prior=["Sé qué es un hábitat.", "Sé que algunos animales nativos están en peligro."],
  explain=[
      "Una amenaza es algo que puede dañar a un animal o a su hábitat. Si el hábitat se daña, el animal pierde su alimento, su agua o su refugio. Entonces le cuesta sobrevivir, y por eso el deterioro del hábitat es una causa de peligro.",
      "Algunas amenazas son: cortar o quemar árboles del bosque; construir casas y caminos donde viven animales; botar basura en ríos y playas; y cazar o capturar animales silvestres. Los perros sueltos también pueden dañar a animales nativos.",
      "Un ejemplo es el huemul. Vive en el sur, y su hábitat se pierde cuando se cortan o queman bosques y se abren caminos. Si desaparece su alimento y su refugio, quedan menos huemules. Entender las amenazas ayuda a pensar cómo protegerlos.",
  ],
  vocab=[("amenaza", "algo que puede dañar a un animal o a su hábitat"), ("deterioro", "daño que hace que algo esté peor"), ("tala", "corte de árboles de un bosque"), ("contaminación", "suciedad que daña el ambiente"), ("captura", "sacar un animal de su hábitat")],
  worked=[
      ("Relacionar amenaza y daño", "Se corta un bosque donde vive el pudú. ¿Qué pierde el animal?", ["Los árboles dan alimento y refugio al pudú.", "Si se cortan, desaparecen.", "El pudú pierde su hábitat."], "Pierde alimento y refugio"),
      ("Identificar amenazas", "En un río aparece mucha basura y el agua se ve sucia. Los peces pueden enfermar. ¿Qué amenaza hay?", ["La basura ensucia el agua.", "El agua sucia puede dañar a los peces.", "Es contaminación."], "Contaminación del agua"),
  ],
  mistakes=[
      ("Decir «cortar un árbol no cambia nada a los animales».", "No se piensa en el refugio y el alimento.", "Muchos animales viven y comen en los árboles; al cortarlos pierden su hábitat."),
      ("Decir «la basura no daña a los animales porque no se la comen».", "No se piensa en la contaminación ni en lo que traga el animal.", "La basura ensucia el agua y algunos animales la tragan o se enredan en ella."),
  ],
  rec=[
      ("¿Cómo se llama el corte de árboles de un bosque?", "Tala", "Es una amenaza para el hábitat."),
      ("Botar basura en un río, ¿ayuda o daña a los peces?", "Daña", "La basura contamina el agua."),
      ("Un camino nuevo cruza el bosque de un huemul. ¿Es una amenaza?", "Sí", "Divide y daña su hábitat."),
  ],
  und=[
      ("¿Qué es una amenaza para un animal?", "Algo que puede dañarlo a él o a su hábitat", "Es la definición de la clase."),
      ("¿Por qué perder el hábitat es peligroso para un animal?", "Porque pierde alimento, agua y refugio", "Un hábitat da esas tres cosas."),
      ("Nombra dos amenazas distintas.", "Por ejemplo: tala y contaminación", "Son ejemplos de la clase."),
  ],
  app=[
      ("Tarjetas: A plantar árboles nativos, B botar basura en el río, C cortar un bosque entero, D cuidar un parque. Escribe las letras de las amenazas.", "B y C", "Botar basura y cortar un bosque dañan el hábitat."),
      arith("Un bosque tenía 100 árboles y se talaron 35. ¿Cuántos árboles quedan?", "100-35", "Se resta a los 100 árboles los 35 talados."),
      ("Un incendio quema el bosque donde viven aves nativas. ¿Qué pierden las aves?", "Su hábitat, su alimento y su refugio", "El fuego destruye árboles y plantas."),
  ],
  rea=[
      ("Un niño dice: «Si un animal se va de su hábitat dañado, no pasa nada». ¿Qué le puede pasar al animal en otro lugar?", "Puede no encontrar alimento, agua ni refugio", "Otro lugar puede no tener lo que necesita."),
      ("Dos lugares: A con basura, B limpio. ¿En cuál es más probable que sobreviva un pez y por qué?", "En B, porque el agua está limpia", "La basura contamina el agua."),
  ],
  cha=[
      ("Elige una amenaza y escribe qué animal nativo sufre y qué pierde.", "Por ejemplo: la tala y el pudú, que pierde refugio", "Se une la amenaza con el daño."),
      ("¿Por qué las amenazas pueden ser peores si son varias al mismo tiempo?", "Porque se suman los daños al hábitat", "Cada amenaza quita algo más al animal."),
  ],
  context=[("Una familia de vacaciones en el sur deja basura cerca de un río donde vive la ranita de Darwin. ¿Qué amenaza hay y qué debería hacer la familia?", "Contaminación; debe llevarse su basura", "La basura daña el agua y el hábitat.")],
  selfcheck=[("¿Qué es la tala?", "Cortar árboles de un bosque", "Es una amenaza."), ("¿Qué pierde un animal cuando se daña su hábitat?", "Alimento, agua o refugio", "Eso le da su hábitat."), ("¿La basura en el río es una amenaza?", "Sí", "Contamina el agua.")],
  open_task=task("Mira esta lista de situaciones: A se corta un bosque, B se planta un bosque, C se bota basura en una playa, D se cuida un río limpio. Elige las dos que son amenazas, escribe qué animal nativo puede sufrir y qué pierde, y dibuja una de ellas.", "Amenazas: A y C. En A, el pudú pierde su refugio. En C, un ave de la playa puede enredarse. Dibujé la tala.", ["elige las dos amenazas correctas", "dice qué animal sufre", "dice qué pierde", "dibuja una"], ["lista con elecciones", "dibujo"], ["elegir B o D", "no decir qué pierde el animal"], "Valora que cada amenaza esté unida a un daño concreto y pide una acción para detenerla."),
  reinforce="Dibuja un bosque sano y al lado un bosque talado. Pinta de rojo lo que cambió.",
  extend="Piensa en una amenaza que haya cerca de tu casa o escuela y escribe qué animales podría dañar.")

L(OA5, 4,
  materials="Este cuaderno con una lista de medidas y una tabla de ayuda. Lápiz y lápices de colores.",
  use="Aprenderé medidas que sí ayudan a proteger animales nativos. Sirve para saber qué puedes hacer tú, tu familia y tu escuela.",
  prior=["Sé qué es una amenaza para un animal.", "Sé que el hábitat da alimento, agua y refugio."],
  explain=[
      "Proteger a los animales nativos es cuidar sus hábitats y evitar dañarlos. Una medida es una acción que ayuda. Hay medidas simples que puedes hacer tú, como llevarte la basura de un paseo, y otras que hacen los adultos, como crear parques.",
      "Algunas medidas que sí ayudan son: no botar basura y reciclar; plantar árboles nativos con ayuda de adultos; cuidar el agua; no comprar ni capturar animales silvestres; y llevar a los perros con correa en lugares donde viven animales nativos.",
      "También ayuda informar a otras personas. Si cuentas lo que aprendiste, más gente cuida el hábitat. Los parques nacionales son lugares protegidos donde la naturaleza se cuida. Y si ves un animal silvestre herido, no lo toques: avisa a un adulto.",
  ],
  vocab=[("medida", "acción que ayuda a resolver un problema"), ("protección", "cuidado para evitar un daño"), ("parque nacional", "lugar protegido donde se cuida la naturaleza"), ("reciclar", "usar de nuevo materiales para no botarlos"), ("silvestre", "animal que vive libre en la naturaleza")],
  worked=[
      ("Elegir una medida que ayuda", "¿Qué medida ayuda al pudú: plantar árboles nativos o cortar el bosque?", ["El pudú vive en el bosque.", "Plantar árboles nativos le da refugio.", "Cortar el bosque le quita su hábitat."], "Plantar árboles nativos"),
      ("Descartar una medida que no ayuda", "Un niño quiere llevarse a casa una rana silvestre «para cuidarla». ¿Ayuda esa medida?", ["La rana silvestre vive mejor en su hábitat.", "En casa no tiene lo que necesita.", "Es mejor dejarla libre."], "No ayuda; hay que dejarla libre"),
  ],
  mistakes=[
      ("Llevarse a casa un animal silvestre para cuidarlo.", "Se piensa que sacarlo de su hábitat lo protege.", "El animal silvestre debe quedarse libre; si está herido, avisa a un adulto."),
      ("Pensar que un niño no puede ayudar.", "Se cree que solo ayudan los adultos.", "Los niños pueden llevarse la basura, cuidar el agua y contar lo que aprendieron."),
  ],
  rec=[
      ("¿Qué haces con la basura de un paseo: la dejas o te la llevas?", "Me la llevo", "Así no daña el hábitat."),
      ("Si ves un animal silvestre herido, ¿lo tocas o avisas a un adulto?", "Aviso a un adulto", "No se debe tocar a un animal silvestre."),
      ("¿Qué es un parque nacional?", "Un lugar protegido donde se cuida la naturaleza", "Protege a animales y plantas nativos."),
  ],
  und=[
      ("¿Qué es una medida de protección?", "Una acción que ayuda a cuidar", "Evita o repara un daño."),
      ("¿Por qué conviene llevar a los perros con correa en lugares con animales nativos?", "Para que no los dañen", "Un perro suelto puede asustar o dañar."),
      ("¿Por qué ayuda contar lo que aprendiste a otras personas?", "Porque más gente puede cuidar el hábitat", "Se suman más personas."),
  ],
  app=[
      ("Lista: A llevarse la basura, B comprar un animal silvestre, C plantar un árbol nativo, D dejar la basura en la playa. Escribe las letras de las medidas que ayudan.", "A y C", "Llevarse la basura y plantar un árbol nativo protegen el hábitat."),
      arith("Un curso plantó 4 árboles nativos cada semana durante 3 semanas. ¿Cuántos árboles plantó?", "4*3", "Se multiplican los árboles por semana por las 3 semanas."),
      ("Ves un cóndor joven en el suelo, parece herido. ¿Qué haces: lo tocas, o avisas a un adulto?", "Aviso a un adulto", "Un animal silvestre herido necesita ayuda de especialistas."),
  ],
  rea=[
      ("Un niño dice que ayudaría al huemul trayéndolo a su casa. ¿Por qué eso no ayuda?", "Porque el huemul necesita su hábitat y no puede vivir en una casa", "En casa no encuentra lo que necesita."),
      ("Un curso decide hacer un afiche para contar cómo cuidar un río. ¿Qué medida de protección es esa?", "Informar a otras personas", "Un afiche enseña a otros."),
  ],
  cha=[
      ("¿Cuál de estas medidas puede hacer un niño y cuál necesita a los adultos? A crear un parque, B llevarse la basura.", "B la puede hacer un niño; A la hacen los adultos", "Hay medidas que un niño hace solo y otras no."),
      ("Escribe una medida que ayude a la ranita de Darwin y diga cómo ayuda.", "Mantener limpio el agua del bosque, porque vive cerca del agua", "Una ranita del agua necesita agua limpia."),
  ],
  context=[("Tu familia va de paseo a un parque cerca de un humedal. ¿Qué tres cosas haces durante el paseo para cuidar a los animales?", "Llevarme la basura, no tocar animales y no dejar el fuego encendido", "Son medidas simples para cuidar el hábitat.")],
  selfcheck=[("¿Una medida sirve para ayudar o para dañar?", "Para ayudar", "Una medida es una acción que ayuda."), ("¿Debes tocar a un animal silvestre herido?", "No", "Hay que avisar a un adulto."), ("¿Plantar árboles nativos ayuda?", "Sí", "Da refugio y alimento.")],
  open_task=task("Haz un afiche pequeño con el título «Cuidemos a los animales nativos de Chile». Dibuja un animal nativo, escribe dos medidas que ayuden y una frase que diga qué puedes hacer tú esta semana.", "Afiche con un huemul. Medidas: llevar la basura y plantar un árbol nativo. Esta semana me llevaré la basura de mi paseo.", ["tiene título", "dibuja un animal nativo", "escribe dos medidas reales", "escribe una acción para esta semana"], ["afiche dibujado", "frase de acción"], ["proponer llevarse un animal silvestre"], "Valora que las medidas sean realistas y pide que diga quién las puede hacer."),
  reinforce="Cuenta a un familiar dos cosas que aprendiste sobre los animales nativos en peligro.",
  extend="Pregunta a un adulto cuál es el parque o la reserva más cercana donde se cuida la naturaleza y anótalo.")

# ---------------------------------------------------------------- OA 06
L(OA6, 1,
  materials="Este cuaderno con las dos escenas descritas, la del humedal limpio y la del humedal con basura, y lápices de colores.",
  use="Aprenderé a mirar los cambios que hace la gente en un lugar sin adivinar. Sirve para anotar lo que se ve y separarlo de lo que se piensa.",
  prior=["Sé que hábitat es el lugar donde vive un animal.", "Sé describir lo que veo con palabras."],
  explain=[
      "La actividad humana es todo lo que hacen las personas, como construir casas, hacer caminos, cultivar, pescar, viajar y botar basura. Esas acciones pueden cambiar los lugares donde viven los animales.",
      "Para estudiar esos cambios, primero observamos. Observar es anotar lo que realmente vemos: «hay 12 botellas en la orilla». Eso se puede comprobar con los ojos. Pensar o suponer es otra cosa: «las botellas enfermaron a los peces». Eso necesita más evidencia.",
      "Un buen científico separa las dos cosas. Escribe en una columna lo que observa y en otra lo que piensa. Así no adivina. Cuando tiene más datos, puede comprobar si lo que pensaba era cierto.",
  ],
  vocab=[("actividad humana", "lo que hacen las personas y cambia el ambiente"), ("observación", "lo que veo y puedo comprobar"), ("suposición", "lo que pienso sin tener todavía la prueba"), ("cambio", "algo que antes era de una forma y ahora es de otra"), ("evidencia", "dato que muestra que algo es cierto")],
  worked=[
      ("Separar observación y suposición", "Escena: «hay 12 botellas en la orilla del humedal». ¿Es observación o suposición?", ["Se puede contar con los ojos.", "Se puede comprobar.", "Es una observación."], "Es una observación"),
      ("Una frase que adivina", "Frase: «las botellas hicieron que se fueran los patos». ¿Es observación o suposición?", ["No se ve directamente que las botellas hicieron que se fueran.", "Falta una prueba.", "Es una suposición."], "Es una suposición"),
  ],
  mistakes=[
      ("Escribir «los patos se fueron por la basura» como si se hubiera visto.", "Se mezcla una suposición con una observación.", "Escribe lo que viste («hay 12 botellas, no hay patos») y deja la explicación para después."),
      ("Pensar que cualquier cambio es culpa de las personas.", "No se piensa en otras causas, como la lluvia o el invierno.", "Anota el cambio y busca evidencia antes de decir quién lo causó."),
  ],
  rec=[
      ("«Hay 12 botellas en la orilla». ¿Es observación o suposición?", "Observación", "Se puede contar con los ojos."),
      ("«Los patos se fueron porque están tristes». ¿Es observación o suposición?", "Suposición", "No se puede comprobar."),
      ("Construir una casa, ¿es una actividad humana?", "Sí", "Es algo que hacen las personas."),
  ],
  und=[
      ("¿Qué es una observación?", "Lo que veo y puedo comprobar", "Se apoya en lo que se ve."),
      ("¿Por qué es mejor anotar observaciones antes de decir quién causó un cambio?", "Porque así no adivino", "Primero hay que tener datos."),
      ("Da un ejemplo de actividad humana en un humedal.", "Por ejemplo: botar basura o construir un camino", "Son acciones de las personas."),
  ],
  app=[
      ("Escena del humedal: 12 botellas, 5 patos, 3 bolsas plásticas. ¿Cuántos objetos de basura se cuentan en total (botellas y bolsas)?", "15", "12 botellas más 3 bolsas son 15."),
      arith("Antes había 9 patos en el humedal y hoy se ven 5. ¿Cuántos patos menos hay?", "9-5", "Se resta el número de hoy al de antes."),
      ("Escribe una frase que sea una observación sobre el humedal con basura.", "Hay 12 botellas en la orilla", "Se puede contar con los ojos."),
  ],
  rea=[
      ("Una niña escribe «los patos desaparecieron por culpa de las botellas». ¿Qué datos le faltan para saberlo?", "Más observaciones, como cuándo se fueron y si cambió el agua", "Falta evidencia que muestre la causa."),
      ("¿Se puede decir que un camino nuevo es la causa de que cambie el número de animales sin más datos? Explica.", "No; hay que anotar más observaciones", "Puede haber otras causas."),
  ],
  cha=[
      ("Escribe una observación y una suposición diferentes sobre un parque con mucha basura.", "Observación: hay muchas bolsas; suposición: los pájaros se fueron por la basura", "Una se puede comprobar y la otra necesita pruebas."),
      ("¿Por qué conviene medir y contar en vez de decir «mucha basura»?", "Porque los números se pueden comparar", "«Mucha» es una opinión; 12 es un dato."),
  ],
  context=[("Una niña visita un humedal el lunes y ve 8 patos y 2 botellas. El viernes ve 5 patos y 11 botellas. Escribe cuántas botellas más vio el viernes.", "9", "11 − 2 = 9 botellas más.")],
  selfcheck=[("¿Qué se puede comprobar con los ojos: una observación o una suposición?", "Una observación", "Se apoya en lo que se ve."), ("¿Qué es una actividad humana?", "Lo que hacen las personas", "Puede cambiar el ambiente."), ("¿Hay que buscar evidencia antes de decir quién causó un cambio?", "Sí", "Así no se adivina.")],
  open_task=task("Mira esta descripción de un humedal: lunes: 10 patos, 3 botellas; miércoles: 7 patos, 9 botellas; viernes: 4 patos, 15 botellas. Escribe una tabla con dos columnas, «lo que observo» y «lo que pienso», y completa dos frases en cada columna.", "Observo: los patos bajaron de 10 a 4. Observo: las botellas subieron de 3 a 15. Pienso: quizás los patos se van por la basura. Pienso: quizás las botellas ensucian el agua donde comen los patos.", ["pone dos observaciones con números", "pone dos suposiciones", "separa las dos columnas"], ["tabla de dos columnas"], ["poner suposiciones en la columna de observaciones"], "Valora que las observaciones tengan números y pide qué dato nuevo ayudaría a probar la suposición."),
  reinforce="Mira tu calle y escribe una observación con un número, como cuántos árboles ves.",
  extend="Piensa en un cambio de tu barrio que hizo la gente y escribe una observación y una suposición sobre él.")

L(OA6, 2,
  materials="Este cuaderno con las cadenas de efectos y lápices de colores.",
  use="Aprenderé a escribir una cadena de efectos: una acción humana que produce un cambio y luego otro. Sirve para ver que un cambio puede tener varias consecuencias.",
  prior=["Sé separar observación y suposición.", "Sé qué es un hábitat."],
  explain=[
      "Una cadena de efectos muestra cómo una acción lleva a otra consecuencia, y esta a otra más. Se escribe con flechas. Por ejemplo: se corta un bosque, entonces desaparece el refugio de las aves, entonces las aves se van a otro lugar.",
      "En cada paso hay una causa y un efecto. La causa es lo que pasa primero. El efecto es lo que ocurre después por esa causa. Cuando el efecto de un paso es la causa del siguiente, la cadena se va alargando.",
      "Para que una cadena sea buena, cada flecha debe tener sentido. No se vale saltar pasos. Una cadena sirve para decidir qué cambiar: si evitamos la primera causa, no ocurren las otras. Por ejemplo, si no botamos basura en el río, el agua no se ensucia.",
  ],
  vocab=[("causa", "lo que hace que algo ocurra"), ("efecto", "lo que ocurre por una causa"), ("cadena de efectos", "serie de causas y efectos unidos con flechas"), ("consecuencia", "resultado de una acción"), ("evitar", "hacer que algo no ocurra")],
  worked=[
      ("Armar una cadena", "Se bota basura al río. Ordena: los peces se enferman, el agua se ensucia, se bota basura al río.", ["Lo primero es la causa: se bota basura.", "Por la basura, el agua se ensucia.", "Con agua sucia, los peces se enferman."], "Se bota basura, el agua se ensucia, los peces se enferman"),
      ("Cortar la cadena", "¿Qué se puede hacer para que los peces no se enfermen?", ["La primera causa es botar basura.", "Si no se bota basura, el agua no se ensucia.", "Entonces los peces no se enferman."], "No botar basura al río"),
  ],
  mistakes=[
      ("Poner el efecto antes de la causa.", "Se invierte el orden de la cadena.", "La causa va primero y el efecto después de la flecha."),
      ("Saltarse un paso de la cadena.", "Se une la primera causa con el último efecto.", "Escribe cada paso para que la cadena tenga sentido."),
  ],
  rec=[
      ("En «se corta un bosque, entonces las aves pierden refugio», ¿cuál es la causa?", "Se corta un bosque", "Es lo que ocurre primero."),
      ("En la misma frase, ¿cuál es el efecto?", "Las aves pierden refugio", "Es lo que ocurre por la causa."),
      ("¿Una cadena de efectos se lee de causa a efecto o de efecto a causa?", "De causa a efecto", "Las flechas van de la causa al efecto."),
  ],
  und=[
      ("¿Qué es una causa?", "Lo que hace que algo ocurra", "Es la definición."),
      ("¿Para qué sirve una cadena de efectos?", "Para ver cómo una acción lleva a varias consecuencias", "Muestra el orden de los cambios."),
      ("¿Por qué evitar la primera causa ayuda a cortar la cadena?", "Porque no ocurren los efectos siguientes", "Todo depende de la primera causa."),
  ],
  app=[
      ("Ordena la cadena: A los peces se enferman, B se bota basura al río, C el agua se ensucia. Escribe las letras.", "B, C, A", "La basura ensucia el agua y esta enferma a los peces."),
      ("Cadena: se construye un camino en el bosque, los animales no pueden cruzar, ... Escribe un posible efecto siguiente.", "Los animales quedan separados o en un lugar más chico", "Un camino divide el hábitat."),
      arith("Un camino divide un bosque. Antes había 50 aves en todo el bosque y ahora se cuentan 20 de un lado y 18 del otro. ¿Cuántas aves se cuentan ahora en total?", "20+18", "Se suman las aves de los dos lados."),
  ],
  rea=[
      ("Un niño dice: «Mucho ruido de autos, entonces las aves se van, entonces hay menos semillas esparcidas». ¿Dónde está la primera causa?", "El mucho ruido de autos", "Es lo que ocurre primero en la cadena."),
      ("Ana dice: «Si se acaba el bosque, los pájaros se van». ¿Falta un paso en su cadena? ¿Cuál?", "Sí; falta que pierden alimento y refugio", "Los pájaros se van porque pierden su hábitat."),
  ],
  cha=[
      ("Construye una cadena de tres pasos que parta con «se queman plantas del cerro».", "Se queman plantas, los animales pierden alimento, los animales se van", "Cada paso es consecuencia del anterior."),
      ("Escribe una acción de personas que corte una cadena dañina y explica cómo.", "No dejar fuego encendido; así no se queman las plantas", "Evita la primera causa."),
  ],
  context=[("Cerca de una laguna se hace una fiesta con mucha música muy fuerte. Escribe una cadena posible de dos efectos sobre los animales que viven allí.", "El ruido asusta a las aves y las aves se van", "El ruido es una causa de cambios en el hábitat.")],
  selfcheck=[("En una cadena, ¿qué va primero: causa o efecto?", "La causa", "Todo parte de ella."), ("¿Cómo se llama el resultado de una acción?", "Efecto o consecuencia", "Es lo que ocurre después."), ("¿Evitar la primera causa ayuda a cortar la cadena?", "Sí", "No ocurren los demás efectos.")],
  open_task=task("Elige una de estas acciones y arma una cadena de tres efectos con flechas: botar basura al río, cortar un bosque, hacer ruido cerca de un nido. Dibuja la cadena y marca con rojo la causa que se podría evitar.", "Se corta un bosque → el pudú pierde refugio → el pudú se va. Marqué en rojo «se corta un bosque».", ["elige una acción", "arma tres pasos con flechas", "marca la causa que se puede evitar"], ["cadena dibujada", "marca roja"], ["invertir causa y efecto", "saltar un paso"], "Valora el orden causa-efecto y pide que explique qué haría para cortar la cadena."),
  reinforce="Con tarjetas de papel, ordena una cadena de tres pasos y pídele a un familiar que la lea de causa a efecto.",
  extend="Piensa en una cadena de efectos positiva, que parta de una buena acción de las personas.")

L(OA6, 3,
  materials="Este cuaderno con la lista de acciones y una tabla de dos columnas, positivo y negativo. Lápiz y lápices de colores.",
  use="Aprenderé que la actividad humana puede ayudar o dañar a los animales y sus hábitats. Sirve para decidir qué acciones hacer y cuáles evitar.",
  prior=["Sé armar una cadena de efectos.", "Sé qué es una causa y un efecto."],
  explain=[
      "No toda la actividad humana daña a los animales. Algunas acciones tienen un impacto negativo: hacen daño. Por ejemplo, botar basura, talar un bosque sin cuidado, o dejar un fuego mal apagado.",
      "Otras acciones tienen un impacto positivo: ayudan. Por ejemplo, plantar árboles nativos, limpiar una playa, crear un parque, cuidar el agua y poner bebederos para aves en un jardín. Estas acciones mejoran la vida de los animales.",
      "Para clasificar una acción, pregunta: ¿qué le pasa al hábitat y a los animales por esta acción? Si pierden alimento, agua o refugio, el impacto es negativo. Si ganan alguna de esas cosas, el impacto es positivo. A veces una acción tiene las dos cosas, y hay que pensar más.",
  ],
  vocab=[("impacto", "efecto que una acción tiene sobre algo"), ("positivo", "que ayuda o mejora"), ("negativo", "que daña o empeora"), ("bebedero", "recipiente con agua para que beban aves"), ("reforestar", "plantar árboles donde se habían perdido")],
  worked=[
      ("Clasificar una acción", "Plantar árboles nativos en un cerro. ¿Impacto positivo o negativo?", ["Los árboles dan refugio y alimento.", "Los animales ganan hábitat.", "Ayuda."], "Impacto positivo"),
      ("Otra acción", "Dejar una fogata mal apagada en el bosque. ¿Impacto positivo o negativo?", ["El fuego puede quemar el bosque.", "Los animales pierden hábitat.", "Daña."], "Impacto negativo"),
  ],
  mistakes=[
      ("Decir «todo lo que hacen las personas daña a los animales».", "No se piensa en acciones que ayudan.", "Hay acciones positivas, como plantar árboles nativos o limpiar playas."),
      ("Decir «si una acción ayuda a las personas, ayuda a los animales».", "No se mira el efecto sobre los animales.", "Mira qué pasa con el hábitat de los animales."),
  ],
  rec=[
      ("Plantar un árbol nativo, ¿es positivo o negativo?", "Positivo", "Da refugio y alimento."),
      ("Botar basura en una playa, ¿es positivo o negativo?", "Negativo", "Contamina el hábitat."),
      ("Limpiar una playa, ¿ayuda o daña a los animales?", "Ayuda", "El hábitat queda más limpio."),
  ],
  und=[
      ("¿Qué es un impacto positivo?", "Un efecto que ayuda o mejora", "Mejora la vida de los animales."),
      ("¿Qué es un impacto negativo?", "Un efecto que daña o empeora", "Hace daño al hábitat."),
      ("¿Cómo sabes si una acción tiene impacto positivo en los animales?", "Si los animales ganan alimento, agua o refugio", "Eso mejora su hábitat."),
  ],
  app=[
      ("Clasifica: A reforestar un cerro, B cortar un bosque, C limpiar una laguna, D botar basura al río. Escribe las letras de las acciones positivas.", "A y C", "Reforestar y limpiar una laguna ayudan."),
      arith("Un curso limpia una playa y junta 14 bolsas de basura el lunes y 9 el martes. ¿Cuántas bolsas junta en total?", "14+9", "Se suman las bolsas de los dos días."),
      ("Un jardín tiene flores y un bebedero para aves. ¿Qué impacto tiene en las aves?", "Positivo", "Les da alimento y agua."),
  ],
  rea=[
      ("Un vecino construye una piscina en un terreno donde vivía un sapo. ¿Qué impacto tuvo para el sapo? Explica.", "Negativo, porque el sapo perdió su hábitat", "La piscina ocupó su lugar."),
      ("Una acción tiene un lado bueno y un lado malo: un camino lleva turistas pero divide un bosque. ¿Por qué hay que pensar más?", "Porque ayuda a las personas pero daña el hábitat", "Una acción puede tener dos impactos distintos."),
  ],
  cha=[
      ("Propón una acción con impacto positivo que pueda hacer un curso en su patio.", "Por ejemplo: plantar flores nativas para insectos", "Da alimento y refugio."),
      ("¿Cómo puedes cambiar una acción negativa en positiva? Usa el ejemplo de la basura.", "No botarla y reciclarla", "Se evita la contaminación."),
  ],
  context=[("Un barrio decide limpiar un humedal el sábado. Llegan 12 vecinos y cada uno junta 3 bolsas de basura. ¿Cuántas bolsas juntaron?", "36", "12 por 3 son 36 bolsas.")],
  selfcheck=[("¿Plantar árboles nativos es positivo o negativo?", "Positivo", "Da refugio a los animales."), ("¿La basura en un río es positiva o negativa?", "Negativa", "Daña el agua."), ("¿Reforestar es plantar árboles?", "Sí", "Se plantan en lugares sin árboles.")],
  open_task=task("Haz una tabla con dos columnas, impacto positivo e impacto negativo, y ordena estas seis acciones: plantar árboles nativos, botar basura, limpiar una playa, talar un bosque, poner un bebedero, hacer fogatas en el bosque. Elige una positiva y propón cómo hacerla en tu barrio.", "Positivo: plantar árboles nativos, limpiar una playa, poner un bebedero. Negativo: botar basura, talar un bosque, hacer fogatas. Pondré un bebedero en el patio de mi escuela.", ["ordena seis acciones", "elige una positiva", "propone cómo hacerla"], ["tabla de dos columnas", "frase de propuesta"], ["poner acciones en la columna equivocada"], "Valora la clasificación y pide que justifique una acción con el hábitat del animal."),
  reinforce="Dibuja una acción positiva y una negativa que veas en tu barrio y explica cada una.",
  extend="Piensa en una acción que ayude a las personas y a los animales a la vez. Escribe cuál es.")

L(OA6, 4,
  materials="Este cuaderno con tres afiches de ejemplo, uno bueno y dos incompletos, y lápices de colores.",
  use="Aprenderé a comunicar una propuesta para cuidar a los animales y su hábitat. Sirve para convencer a otras personas con datos claros.",
  prior=["Sé separar observaciones y suposiciones.", "Sé clasificar acciones en positivas y negativas."],
  explain=[
      "Comunicar es contar algo a otras personas de forma que lo entiendan. Una buena propuesta tiene un título claro, un dato verdadero y una acción concreta. Por ejemplo: «Cuidemos la laguna. En la laguna hubo 15 bolsas de basura. Llévate tu basura».",
      "El dato puede ser un número que observaste. El número hace más creíble el mensaje que solo decir «hay mucha basura». La acción debe ser algo que las personas puedan hacer, como llevarse la basura, y no algo imposible, como «eliminar toda la basura del mundo».",
      "Un afiche también necesita un dibujo que apoye el mensaje y letras grandes que se vean de lejos. Al terminar, revisa con una lista: título, dato, acción y dibujo. Si falta algo, el mensaje puede confundir.",
  ],
  vocab=[("propuesta", "idea para resolver un problema"), ("afiche", "cartel con dibujos y letras grandes para comunicar un mensaje"), ("dato", "información comprobable, como un número"), ("acción concreta", "algo que una persona puede hacer de verdad"), ("mensaje", "lo que quiero que otras personas entiendan")],
  worked=[
      ("Revisar un afiche", "Afiche: «Cuidemos la laguna. Ayer hubo 15 bolsas de basura. Llévate tu basura». ¿Tiene título, dato y acción?", ["Título: «Cuidemos la laguna».", "Dato: 15 bolsas de basura.", "Acción: llevarse la basura."], "Sí, tiene título, dato y acción"),
      ("Completar un afiche", "Afiche: «Hay mucha basura». ¿Qué le falta?", ["«Mucha» no es un número.", "No dice qué hacer.", "Falta un título y una acción."], "Un título, un dato con número y una acción concreta"),
  ],
  mistakes=[
      ("Escribir «la gente es mala» en el afiche.", "Se critica a las personas en vez de proponer una acción.", "Escribe qué se puede hacer, como «lleva tu basura»."),
      ("Poner muchos textos pequeños.", "No se lee de lejos.", "Usa pocas palabras y letras grandes."),
  ],
  rec=[
      ("¿Debe un afiche llevar título, dato y acción?", "Sí", "Son las tres partes de una buena propuesta."),
      ("¿«Hay 15 bolsas de basura» es un dato o una opinión?", "Un dato", "Tiene un número comprobable."),
      ("¿«Lleva tu basura» es una acción concreta?", "Sí", "Una persona puede hacerla."),
  ],
  und=[
      ("¿Qué quiere decir «comunicar»?", "Contar algo a otras personas para que lo entiendan", "Es la definición."),
      ("¿Por qué un dato con número convence más que solo «mucho»?", "Porque se puede comprobar", "El número es exacto."),
      ("¿Para qué sirve el dibujo en un afiche?", "Para apoyar el mensaje", "Ayuda a entender de un vistazo."),
  ],
  app=[
      ("Afiche A: «Basta». Afiche B: «Cuidemos la playa. Hoy juntamos 20 bolsas. Llévate tu basura». ¿Cuál afiche tiene título, dato y acción?", "El B", "El A no tiene dato ni acción."),
      arith("Un curso cuenta 7 botellas en la mañana y 6 en la tarde y las pone en su afiche. ¿Qué número escribe como total?", "7+6", "Se suman las botellas de la mañana y de la tarde."),
      ("Un afiche dice «Hoy encontramos 9 botellas». ¿Qué parte del afiche es: título, dato o acción?", "Dato", "Es un número comprobable."),
  ],
  rea=[
      ("Marta quiere un afiche para proteger al huemul. Escribe un título posible.", "Por ejemplo: Cuidemos al huemul", "Un título claro nombra al animal y la idea."),
      ("Un afiche dice «Todos debemos hacer algo». ¿Por qué no es un buen mensaje?", "Porque no dice qué hacer", "Falta una acción concreta."),
  ],
  cha=[
      ("Escribe un mensaje con un dato, una acción y un título para una escuela que quiere cuidar a las aves de su patio.", "Cuidemos a las aves. Hay 3 nidos en el patio. No hagamos ruido cerca", "Tiene título, dato y acción."),
      ("¿Por qué conviene probar el afiche con otra persona antes de colgarlo?", "Para ver si lo entiende", "Así se descubren errores."),
  ],
  context=[("Un curso encontró 18 colillas y 12 botellas junto a un río y quiere avisar a las familias. ¿Cuántos objetos contaron en total para poner en el afiche?", "30", "18 más 12 son 30.")],
  selfcheck=[("¿Cuántas partes principales tiene la propuesta de hoy?", "Tres", "Título, dato y acción."), ("¿Una acción concreta se puede hacer?", "Sí", "Debe ser posible."), ("¿Un afiche usa letras grandes o muy chicas?", "Grandes", "Así se leen de lejos.")],
  open_task=task("Haz un afiche para cuidar un animal nativo de Chile o su hábitat. Usa este dato de práctica: en una laguna hay 20 bolsas de basura. Tu afiche debe tener título, el dato, una acción concreta y un dibujo.", "Título: Cuidemos nuestra laguna. Dato: hay 20 bolsas de basura. Acción: llévate tu basura. Dibujé una laguna con aves.", ["tiene título", "incluye el dato", "propone una acción concreta", "tiene dibujo"], ["afiche terminado", "lista de revisión marcada"], ["no poner dato", "acción imposible"], "Revisa las cuatro partes con una lista y pide que cambie lo que falte."),
  reinforce="Revisa un afiche que veas en tu calle y marca si tiene título, dato, acción y dibujo.",
  extend="Haz una segunda versión del afiche para otro lugar, como una plaza o una escuela.")
