"""Cuaderno del estudiante, 2.º básico Ciencias Naturales: OA 03 (ciclos de vida) y OA 04 (hábitats)."""
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


OA3, OA4 = "CN02 OA 03", "CN02 OA 04"

# ---------------------------------------------------------------- OA 03
L(OA3, 1,
  materials="Este cuaderno con las tarjetas de etapas y lápices de colores. Para jugar a ordenar: tres hojas pequeñas de papel.",
  use="Aprenderé que los animales cambian durante su vida en etapas ordenadas. Sirve para entender cómo un animal pasa de cría a adulto.",
  prior=["Sé que los animales nacen, crecen y cambian.", "Sé ordenar cosas de primero a último."],
  explain=[
      "Todos los animales pasan por etapas durante su vida. Primero nacen, después crecen, luego llegan a ser adultos y pueden tener crías. Cuando nacen nuevas crías, el ciclo vuelve a comenzar desde el principio.",
      "Por eso se llama ciclo de vida. Un ciclo es algo que da una vuelta y vuelve a empezar, como un círculo. Se dibuja con flechas: cada flecha lleva de una etapa a la siguiente, y la última flecha vuelve a la primera.",
      "Las etapas siempre van en el mismo orden. Una gallina adulta pone un huevo, del huevo sale un pollito, el pollito crece, se vuelve una gallina joven y después una gallina adulta. Nadie salta etapas ni las cambia de lugar. Ordenar bien las etapas muestra que entendiste el ciclo.",
  ],
  vocab=[("ciclo de vida", "serie de etapas que se repiten en la vida de un animal"), ("etapa", "momento de la vida con rasgos propios"), ("cría", "animal recién nacido o muy joven"), ("adulto", "animal que ya terminó de crecer y puede tener crías"), ("reproducirse", "tener crías")],
  worked=[
      ("Ordenar un ciclo", "Ordena las etapas de la gallina: pollito, huevo, gallina adulta.", ["La vida del pollito empieza con el huevo.", "Del huevo sale el pollito.", "El pollito crece y es gallina adulta."], "Huevo, pollito, gallina adulta"),
      ("Cerrar el ciclo", "¿Qué pasa después de la etapa de gallina adulta?", ["La gallina adulta puede poner huevos.", "Del huevo sale otro pollito.", "El ciclo vuelve a comenzar."], "Pone un huevo y el ciclo vuelve a empezar"),
  ],
  mistakes=[
      ("Poner el pollito antes del huevo.", "Se olvida el orden de las etapas.", "Antes del pollito hay un huevo: del huevo nace el pollito."),
      ("Pensar que el ciclo termina en el adulto.", "No se imagina que el adulto tiene crías.", "El adulto puede tener crías y el ciclo vuelve a empezar."),
  ],
  rec=[
      ("¿Qué etapa viene primero en la vida de una gallina: el huevo o la gallina adulta?", "El huevo", "La vida comienza con el huevo."),
      ("Escribe cómo se llama la cría de la gallina.", "Pollito", "El pollito es la cría de la gallina."),
      ("Un ciclo de vida, ¿termina o vuelve a empezar?", "Vuelve a empezar", "Las crías nuevas inician otra vez el ciclo."),
  ],
  und=[
      ("¿Qué quiere decir «etapa» en la vida de un animal?", "Un momento de la vida con rasgos propios", "Cada etapa tiene características distintas."),
      ("Explica con tus palabras por qué se llama «ciclo» de vida.", "Porque las etapas vuelven a comenzar", "Un ciclo da una vuelta completa y se repite."),
      ("¿Qué indica una flecha en un dibujo de ciclo de vida?", "Que sigue la siguiente etapa", "Marca el orden entre etapas."),
  ],
  app=[
      ("Ordena de primero a último: A pollito, B huevo, C gallina adulta. Escribe las letras.", "B, A, C", "Primero el huevo, luego el pollito y al final la gallina adulta."),
      ("Un perro adulto tiene cachorros. Los cachorros crecen. ¿Qué etapa viene después de que crecen?", "Son perros adultos", "El cachorro crece y se vuelve adulto."),
      ("Una tortuga sale de un huevo, crece y llega a ser adulta. Escribe la etapa que va entre el huevo y la tortuga adulta.", "La cría", "Del huevo sale una cría que crece hasta ser adulta."),
  ],
  rea=[
      ("Pablo dijo: «Primero está la gallina grande y después el huevo». ¿Está bien? Explica.", "No; antes de la gallina grande hubo un huevo y un pollito", "Cada animal nace de un huevo y crece."),
      ("Una cartulina muestra: huevo, gallina adulta, pollito, huevo. ¿Cuál etapa está mal puesta?", "La gallina adulta: debe ir después del pollito", "El pollito crece y recién después es gallina adulta."),
  ],
  cha=[
      ("Un compañero dice: «El ciclo termina cuando el animal es adulto». ¿Qué le respondes?", "Que el adulto puede tener crías y el ciclo vuelve a empezar", "Las crías inician otro ciclo."),
      ("Un ciclo del perro tiene tres etapas: cachorro, perro joven y perro adulto. Si cada etapa tiene una flecha hacia la siguiente y la última vuelve al cachorro, ¿cuántas flechas hay en total?", "3", "Cada etapa tiene una flecha que sale hacia la siguiente, y la tercera vuelve a la primera."),
  ],
  context=[("En un gallinero ves un huevo, un pollito, una gallina joven y una gallina adulta. Escribe el orden en que aparecen en la vida de una gallina.", "Huevo, pollito, gallina joven, gallina adulta", "Es el orden de las etapas de crecimiento.")],
  selfcheck=[("¿Qué etapa sigue al huevo en la gallina?", "El pollito", "Del huevo sale un pollito."), ("¿Un ciclo termina o se repite?", "Se repite", "Las crías inician otro ciclo."), ("¿Qué se llama «cría»?", "Un animal recién nacido", "Es el animal muy joven.")],
  open_task=task("Dibuja el ciclo de vida de la gallina con cuatro dibujos y flechas: huevo, pollito, gallina joven y gallina adulta. Escribe una frase que diga qué cambia entre el pollito y la gallina adulta.", "Dibujé cuatro cuadros con flechas y una última flecha que vuelve al huevo. El pollito es pequeño y con plumón; la gallina adulta es grande y tiene plumas.", ["dibuja cuatro etapas", "pone el orden correcto", "cierra el ciclo con una flecha", "escribe un cambio"], ["dibujo con flechas", "frase de cambio"], ["no cerrar el ciclo", "poner las etapas fuera de orden"], "Valora el orden y pide que explique qué flecha cierra el ciclo."),
  reinforce="Recorta cuatro papeles y escribe en cada uno una etapa de la gallina. Mézclalos y vuelve a ordenarlos.",
  extend="Piensa en otro animal que conozcas y escribe tres etapas de su vida en orden.")

L(OA3, 2,
  materials="Este cuaderno con las tarjetas del ciclo de la gallina y del perro. Lápiz y lápices de colores.",
  use="Aprenderé a comparar el ciclo de vida de un ave y el de un mamífero. Sirve para ver qué se parece y qué es distinto entre dos animales.",
  prior=["Sé que el ciclo de vida tiene etapas ordenadas.", "Sé que las aves ponen huevos y que los mamíferos dan leche."],
  explain=[
      "El ciclo de un ave comienza con un huevo. La gallina cuida el huevo hasta que se rompe la cáscara y sale el pollito. Un huevo de gallina necesita unos 21 días, o tres semanas, para que el pollito esté listo para salir.",
      "En el ciclo de un mamífero, como el perro, la cría crece dentro del cuerpo de su madre y nace ya formada. Después toma leche de las mamas. Cuando crece, deja de tomar leche y come otros alimentos. Después es un perro joven y por último un perro adulto, que puede tener crías.",
      "Comparar es buscar qué es igual y qué es distinto. En los dos ciclos hay nacimiento, crecimiento y adulto que tiene crías. La diferencia más importante está en el comienzo: el ave nace de un huevo y el perro nace del cuerpo de su madre.",
  ],
  vocab=[("huevo", "estructura con cáscara de donde sale la cría de un ave"), ("cachorro", "cría del perro"), ("leche", "alimento que toman las crías de los mamíferos"), ("comparar", "buscar qué se parece y qué es distinto"), ("nacimiento", "momento en que la cría sale al mundo")],
  worked=[
      ("Comparar el comienzo", "¿Cómo comienza la vida de un pollito y la de un cachorro?", ["El pollito comienza dentro de un huevo.", "El cachorro crece dentro del cuerpo de su madre.", "Se parecen en que ambos nacen, pero el comienzo es distinto."], "El pollito, en un huevo; el cachorro, dentro de su madre"),
      ("Comparar lo que comen las crías", "¿Qué toma el cachorro cuando nace?", ["El cachorro es un mamífero.", "Los mamíferos tienen mamas.", "Las crías toman leche de la madre."], "Leche"),
  ],
  mistakes=[
      ("Decir «el cachorro nace de un huevo».", "Se olvida que los mamíferos no ponen huevos.", "El cachorro crece dentro de su madre y nace ya formado."),
      ("Decir «el pollito toma leche de su madre».", "Se mezcla el ciclo del ave con el del mamífero.", "El pollito no toma leche, porque las aves no tienen mamas."),
  ],
  rec=[
      ("¿De dónde sale un pollito?", "De un huevo", "Las aves nacen de un huevo."),
      ("¿Qué toma un cachorro cuando es muy pequeño?", "Leche", "Los mamíferos toman leche."),
      ("¿Cuántas semanas necesita un huevo de gallina para que salga el pollito, si necesita 21 días?", "3", "21 días son 3 semanas de 7 días."),
  ],
  und=[
      ("Escribe una semejanza entre el ciclo de la gallina y el del perro.", "Los dos nacen, crecen y se vuelven adultos con crías", "Ambos ciclos tienen las mismas grandes etapas."),
      ("Escribe una diferencia entre el comienzo del ciclo de un ave y el de un mamífero.", "El ave nace de un huevo y el mamífero nace de su madre", "Es la diferencia principal del comienzo."),
      ("¿Para qué sirven las mamas de la perra?", "Para dar leche a los cachorros", "Los cachorros se alimentan con esa leche."),
  ],
  app=[
      arith("Un huevo de gallina necesita 21 días. Ya pasaron 9 días. ¿Cuántos días faltan?", "21-9", "Se resta a los 21 días los 9 días que pasaron."),
      ("Completa: el pollito sale de un ______ y el cachorro nace del cuerpo de su ______.", "huevo; madre", "Cada cría empieza su vida de forma distinta."),
      ("Un mamífero adulto tiene crías y las alimenta con su leche. ¿Qué etapa viene después de que la cría deja la leche y crece?", "La etapa de adulto", "La cría crece hasta ser adulta."),
  ],
  rea=[
      ("Sara dice: «Los ciclos de gallina y perro son iguales en todo». ¿Qué diferencia le muestras?", "El pollito sale de un huevo y el cachorro nace de su madre", "Esa diferencia está al comienzo del ciclo."),
      ("Una gallina empieza a cuidar su huevo un lunes. Si el pollito sale 21 días después, ¿en qué día de la semana sale?", "Lunes", "21 días son 3 semanas justas, así que cae en el mismo día de la semana."),
  ],
  cha=[
      ("¿Necesita cuidado de su madre el cachorro que toma leche, el huevo del pollito o los dos? Explica una razón.", "Los dos; el cachorro toma leche y el huevo necesita calor", "Las dos crías dependen de su madre en el comienzo."),
      ("Ordena este ciclo del perro: A cachorro toma leche, B perro adulto, C cachorro nace, D perro joven.", "C, A, D, B", "Nace, toma leche, crece como joven y luego es adulto."),
  ],
  context=[("En la granja, Luna la perra tuvo 4 cachorros y la gallina Pinta tiene 3 huevos. ¿Cuántas crías habrá en total cuando nazcan todos los pollitos?", "7", "4 cachorros más 3 pollitos son 7 crías.")],
  selfcheck=[("¿Qué animal nace de un huevo: el perro o la gallina?", "La gallina", "Es un ave."), ("¿Qué toman los cachorros?", "Leche", "Los mamíferos toman leche."), ("¿Se parecen los dos ciclos en que hay adulto con crías?", "Sí", "Ambos ciclos vuelven a comenzar.")],
  open_task=task("Haz una tabla con dos columnas, gallina y perro. Escribe cómo comienza cada vida, qué toma o come la cría, y el nombre de la cría. Termina con una frase que diga qué se parece.", "Gallina: comienza en un huevo, el pollito come granos más tarde. Perro: comienza dentro de su madre, el cachorro toma leche. Se parecen en que ambos crecen y se vuelven adultos con crías.", ["escribe el comienzo de cada ciclo", "nombra la cría de cada animal", "escribe una semejanza"], ["tabla completa", "frase de semejanza"], ["decir que el perro nace de huevo"], "Revisa que la diferencia esté en el comienzo y pide que explique una semejanza con sus palabras."),
  reinforce="Dibuja una gallina con su pollito y una perra con su cachorro. Escribe qué come cada cría.",
  extend="Pregunta a un adulto qué animales ha visto nacer y cuenta si salieron de un huevo o del cuerpo de su madre.")

L(OA3, 3,
  materials="Este cuaderno con las tarjetas de mariposa y rana. Lápices de colores. No necesitas tocar animales.",
  use="Aprenderé la metamorfosis, un cambio muy grande del cuerpo durante el ciclo de vida. Sirve para saber que una oruga y una mariposa son el mismo animal.",
  prior=["Sé ordenar las etapas de un ciclo de vida.", "Sé que la mariposa es un insecto y que la rana es un anfibio."],
  explain=[
      "Algunos animales cambian tanto de forma que, al comienzo, no se parecen a sus padres. Ese cambio grande se llama metamorfosis. La mariposa y la rana pasan por una metamorfosis.",
      "La mariposa tiene cuatro etapas. Primero hay un huevo. De él sale una oruga, que come hojas y crece. Después la oruga forma una crisálida, una cubierta donde su cuerpo se transforma. Al final sale la mariposa adulta, con alas.",
      "La rana también tiene cuatro etapas. De un huevo sale un renacuajo, que vive en el agua y tiene cola. Luego le salen patas, su cola se achica y se hace una rana joven. Al final la rana adulta vive en el agua y cerca de ella, y respira con pulmones.",
  ],
  vocab=[("metamorfosis", "cambio grande del cuerpo durante la vida de un animal"), ("oruga", "cría de la mariposa que come hojas"), ("crisálida", "cubierta donde la oruga se transforma en mariposa"), ("renacuajo", "cría de la rana que vive en el agua y tiene cola"), ("transformarse", "cambiar de forma")],
  worked=[
      ("Ordenar la mariposa", "Ordena: crisálida, huevo, mariposa, oruga.", ["La vida comienza en un huevo.", "Del huevo sale la oruga.", "La oruga forma la crisálida y de ella sale la mariposa."], "Huevo, oruga, crisálida, mariposa"),
      ("Ordenar la rana", "Ordena: rana adulta, huevo, renacuajo, rana joven.", ["Primero hay un huevo.", "Del huevo sale el renacuajo, con cola.", "Le salen patas: rana joven y luego rana adulta."], "Huevo, renacuajo, rana joven, rana adulta"),
  ],
  mistakes=[
      ("Decir «la oruga y la mariposa son dos animales distintos».", "Se mira solo la forma del cuerpo.", "Son el mismo animal en dos etapas: la oruga se transforma en mariposa."),
      ("Decir «el perro tiene metamorfosis».", "Se piensa que cualquier cambio de tamaño es metamorfosis.", "El cachorro crece pero se parece al perro adulto: no hay un cambio tan grande."),
  ],
  rec=[
      ("¿Cómo se llama la cría de la mariposa?", "Oruga", "La oruga sale del huevo."),
      ("¿Cómo se llama la cría de la rana que vive en el agua?", "Renacuajo", "El renacuajo tiene cola y vive en el agua."),
      ("¿Cuántas etapas tiene el ciclo de la mariposa en esta clase?", "4", "Huevo, oruga, crisálida y mariposa."),
  ],
  und=[
      ("¿Qué significa «metamorfosis»?", "Un cambio muy grande del cuerpo", "Es la definición de la clase."),
      ("¿Por qué una oruga y una mariposa son el mismo animal?", "Porque la oruga se transforma en mariposa", "Son etapas del mismo ciclo."),
      ("¿Qué le pasa al renacuajo antes de ser rana joven?", "Le salen patas", "El renacuajo cambia su cuerpo."),
  ],
  app=[
      ("Ordena el ciclo de la mariposa: A mariposa, B huevo, C crisálida, D oruga. Escribe las letras.", "B, D, C, A", "Huevo, oruga, crisálida y mariposa."),
      ("Ordena el ciclo de la rana: A renacuajo, B rana adulta, C huevo, D rana joven. Escribe las letras.", "C, A, D, B", "Huevo, renacuajo, rana joven y rana adulta."),
      arith("Una oruga come 3 hojas cada día durante 6 días. ¿Cuántas hojas come en total?", "3*6", "Se multiplican las hojas de cada día por los 6 días."),
  ],
  rea=[
      ("Un niño dice: «Los renacuajos son peces porque viven en el agua». Tienen cola y se transforman en ranas. ¿Qué responde?", "Son crías de rana que se transforman", "Después de la metamorfosis serán ranas adultas."),
      ("¿Cuál de estos animales tiene metamorfosis: el gato, la mariposa o la gallina?", "La mariposa", "Sus etapas cambian mucho de forma."),
  ],
  cha=[
      ("La oruga no tiene alas y la mariposa sí. ¿En qué etapa el cuerpo se transforma y termina con alas?", "En la crisálida", "Allí el cuerpo se transforma y sale la mariposa con alas."),
      ("Una oruga mide 2 cm el día 1 y 5 cm el día 8. ¿Cuántos centímetros creció la oruga entre el día 1 y el día 8?", "3", "5 − 2 = 3 centímetros."),
  ],
  context=[("En el patio hay una oruga sobre una hoja, un renacuajo en una poza y un cachorro de perro. ¿Cuál de los tres no tiene metamorfosis?", "El cachorro", "La oruga y el renacuajo cambian mucho su cuerpo; el cachorro solo crece.")],
  selfcheck=[("¿Cómo se llama la cubierta donde la oruga se transforma?", "Crisálida", "Es la etapa antes de la mariposa."), ("¿Cuántas etapas tiene la rana en esta clase?", "4", "Huevo, renacuajo, rana joven y rana adulta."), ("¿El renacuajo vive en el agua o en la tierra?", "En el agua", "Respira con branquias.")],
  open_task=task("Elige uno de estos dos ciclos, mariposa o rana, y dibújalo con cuatro cuadros y flechas. Escribe el nombre de cada etapa. Debajo escribe una frase que diga qué cambia más entre la primera y la última etapa.", "Dibujé la rana: huevo, renacuajo, rana joven y rana adulta. El renacuajo tiene cola y la rana adulta tiene patas.", ["dibuja cuatro etapas", "escribe el nombre de cada etapa", "cierra con una frase de cambio"], ["dibujo con flechas", "frase de cambio"], ["poner una etapa fuera de orden", "decir que son animales distintos"], "Valora el orden y el uso de la palabra metamorfosis para explicar el cambio."),
  reinforce="Recorta cuatro papeles con las etapas de la mariposa y ordénalos. Pide a un adulto que mezcle y que tú los ordenes de nuevo.",
  extend="Piensa en qué se parecen las metamorfosis de la mariposa y de la rana. Escribe una semejanza.")

L(OA3, 4,
  materials="Este cuaderno con la tabla de etapas y lugares. Lápiz y lápices de colores.",
  use="Aprenderé que cada etapa del ciclo de vida ocurre en un lugar que ayuda a la cría. Sirve para entender por qué la rana pone sus huevos en el agua y la gallina en un nido.",
  prior=["Conozco el ciclo de la mariposa, de la rana y de la gallina.", "Sé que hábitat es el lugar donde vive un animal."],
  explain=[
      "Un hábitat es el lugar donde vive un animal y donde encuentra lo que necesita. En cada etapa de su ciclo de vida, un animal puede necesitar un lugar distinto. El hábitat ayuda a que las crías sobrevivan.",
      "La rana pone sus huevos en el agua, porque el renacuajo respira con branquias y debe vivir en el agua. Cuando es adulta, la rana respira con pulmones y puede vivir cerca del agua y también en la tierra húmeda.",
      "La oruga vive sobre las hojas porque come hojas. La mariposa adulta vuela de flor en flor, porque toma néctar de las flores. La gallina pone sus huevos en un nido seco y abrigado. La perra prepara un rincón abrigado y tranquilo para sus cachorros recién nacidos, que necesitan calor y la leche de su madre. Cada etapa necesita un lugar útil.",
  ],
  vocab=[("hábitat", "lugar donde vive un animal y encuentra lo que necesita"), ("néctar", "líquido dulce que producen las flores"), ("nido", "lugar donde un ave pone sus huevos y cuida a sus crías"), ("sobrevivir", "seguir con vida"), ("relacionar", "unir dos cosas que se conectan")],
  worked=[
      ("Relacionar etapa y lugar", "¿Dónde vive el renacuajo y por qué?", ["El renacuajo respira con branquias.", "Las branquias toman el oxígeno del agua.", "Por eso necesita vivir en el agua."], "En el agua, porque respira con branquias"),
      ("Etapa y alimento", "¿Por qué la oruga vive sobre hojas?", ["La oruga come hojas.", "Si está sobre ellas, tiene alimento al lado.", "Su lugar sirve para su alimento."], "Porque las hojas son su alimento"),
  ],
  mistakes=[
      ("Decir «el renacuajo vive en la tierra».", "Se piensa que la cría vive donde vive el adulto.", "El renacuajo respira con branquias y debe vivir en el agua; la rana adulta ya usa pulmones."),
      ("Decir «todas las etapas de un animal viven en el mismo lugar».", "No se compara etapa por etapa.", "Cada etapa necesita lo suyo: el renacuajo, agua; la rana adulta, agua y tierra húmeda."),
  ],
  rec=[
      ("¿Dónde pone sus huevos la rana: en el agua o en el desierto?", "En el agua", "Allí vive el renacuajo."),
      ("¿Qué come la oruga?", "Hojas", "La oruga come hojas."),
      ("¿Qué toma la mariposa de las flores?", "Néctar", "El néctar es su alimento."),
  ],
  und=[
      ("¿Por qué es importante el lugar donde vive una cría?", "Porque ahí encuentra lo que necesita para sobrevivir", "El hábitat da alimento, agua y refugio."),
      ("¿Por qué la rana adulta puede estar fuera del agua y el renacuajo no?", "Porque la rana adulta respira con pulmones y el renacuajo con branquias", "Cada etapa respira distinto."),
      ("¿Para qué sirve un nido?", "Para poner huevos y cuidar a las crías", "Protege los huevos de las aves."),
  ],
  app=[
      ("Une cada etapa con su lugar: A renacuajo, B oruga, C mariposa adulta. Lugares: 1 flores, 2 agua, 3 hojas. Escribe los pares.", "A2, B3, C1", "El renacuajo vive en el agua, la oruga en las hojas y la mariposa en las flores."),
      arith("Una rana puso 40 huevos en una poza y nacieron 28 renacuajos. ¿Cuántos huevos no dieron renacuajos?", "40-28", "Se resta a los 40 huevos los 28 renacuajos."),
      ("Un ave pone sus huevos en un nido hecho de pasto y ramitas. ¿Cómo ayuda el nido a las crías?", "Protege los huevos y los mantiene abrigados", "El nido cuida el comienzo de la vida."),
  ],
  rea=[
      ("Nico dice: «Si la poza se seca, los renacuajos igual sobreviven». ¿Qué le respondes con un dato del ciclo?", "No, porque necesitan agua para respirar con branquias", "Sin agua no pueden respirar."),
      ("Una hoja con huevos de mariposa está en una planta con muchas hojas. ¿Por qué ese lugar es bueno para la oruga que saldrá?", "Porque tendrá hojas para comer", "La oruga come hojas desde que nace."),
  ],
  cha=[
      ("Un charco de la plaza se seca en verano. ¿Qué etapa de la rana es más difícil que sobreviva allí y por qué?", "El renacuajo, porque necesita agua", "Sin agua no respira con branquias."),
      ("Una perra va a tener cachorros. ¿Qué lugar les sirve más: un rincón abrigado y tranquilo o un patio con viento y frío? Explica.", "Un rincón abrigado y tranquilo, porque los cachorros recién nacidos necesitan calor y a su madre", "El lugar ayuda a que las crías sobrevivan."),
  ],
  context=[("En una laguna, un niño ve huevos de rana en el agua, una oruga en una hoja al borde y un nido con tres huevos. ¿Cuántos lugares distintos nombra?", "3", "Agua, hoja y nido son tres lugares distintos.")],
  selfcheck=[("¿Dónde vive el renacuajo?", "En el agua", "Respira con branquias."), ("¿Sobre qué vive la oruga mientras come?", "Sobre hojas", "Allí tiene su alimento."), ("¿Quién usa un nido para cuidar sus huevos?", "Las aves", "Las aves ponen huevos en nidos.")],
  open_task=task("Haz una tabla con tres filas: renacuajo, oruga y pollito. En cada fila escribe dónde vive esa cría, qué necesita de ese lugar y un dibujo del lugar.", "Renacuajo: en el agua, necesita agua para respirar. Oruga: sobre hojas, necesita hojas para comer. Pollito: en el nido, necesita abrigo.", ["escribe el lugar de cada cría", "explica qué necesita", "dibuja los lugares"], ["tabla con tres filas", "dibujos"], ["poner a todas las crías en el mismo lugar"], "Valora la relación entre etapa y lugar y pide un ejemplo en que el lugar de la etapa adulta sea distinto."),
  reinforce="Dibuja la poza donde vive el renacuajo y la tierra húmeda donde puede estar la rana adulta.",
  extend="Piensa en un animal que conozcas y explica en qué lugar vive su cría y en qué lugar vive su adulto.")

# ---------------------------------------------------------------- OA 04
L(OA4, 1,
  materials="Este cuaderno con las tarjetas de hábitats: bosque, desierto, laguna y orilla del mar. Lápices de colores.",
  use="Aprenderé qué es un hábitat y qué condiciones ofrece. Sirve para entender por qué cada animal vive en un lugar y no en otro.",
  prior=["Sé que los animales necesitan alimento, agua y refugio.", "Sé nombrar lugares como bosque, desierto y mar."],
  explain=[
      "Un hábitat es el lugar donde vive un animal y donde encuentra lo que necesita. El bosque, el desierto, una laguna y la orilla del mar son hábitats. Un hábitat da alimento, agua y refugio.",
      "Cada hábitat también tiene condiciones que se pueden medir o describir. Tiene más o menos luz, que se llama luminosidad. Tiene más o menos agua en el aire y en el suelo, que se llama humedad. Y tiene más o menos calor o frío, que es la temperatura, y se mide en grados Celsius (°C).",
      "En el desierto hay mucha luz, poca humedad y calor de día y frío de noche. En un bosque del sur hay sombra, mucha humedad y temperatura fresca. Un animal sobrevive bien cuando las condiciones de su hábitat son las que necesita.",
  ],
  vocab=[("hábitat", "lugar donde vive un animal y encuentra lo que necesita"), ("luminosidad", "cantidad de luz que hay en un lugar"), ("humedad", "cantidad de agua que hay en el aire o en el suelo"), ("temperatura", "qué tan caliente o frío está un lugar"), ("refugio", "lugar donde un animal se protege")],
  worked=[
      ("Describir un hábitat", "Describe el desierto con tres condiciones.", ["Luminosidad: hay mucha luz del sol.", "Humedad: es muy seca.", "Temperatura: es caluroso durante el día."], "Mucha luz, poca humedad y calor de día"),
      ("Describir otro hábitat", "Describe el interior de un bosque con tres condiciones.", ["Luminosidad: hay sombra de los árboles.", "Humedad: el suelo y el aire tienen mucha agua.", "Temperatura: es fresco."], "Sombra, mucha humedad y temperatura fresca"),
  ],
  mistakes=[
      ("Decir «todos los hábitats tienen la misma luz».", "No se comparan las condiciones.", "El desierto tiene mucha luz y el interior de una cueva casi nada."),
      ("Confundir humedad con temperatura.", "Se cree que humedad es calor.", "La humedad es cuánta agua hay; la temperatura es qué tan caliente o frío está."),
  ],
  rec=[
      ("¿Cómo se llama la cantidad de luz de un lugar?", "Luminosidad", "Es una de las tres condiciones."),
      ("¿Cómo se llama el agua que hay en el aire o en el suelo?", "Humedad", "Es otra condición."),
      ("¿Cómo se llama qué tan caliente o frío está un lugar?", "Temperatura", "Es la tercera condición."),
  ],
  und=[
      ("Escribe qué es un hábitat.", "El lugar donde vive un animal y encuentra lo que necesita", "Es la definición de la clase."),
      ("Menciona tres cosas que da un hábitat.", "Alimento, agua y refugio", "Son las necesidades básicas."),
      ("¿Por qué un desierto es un hábitat distinto de un bosque?", "Porque tiene otras condiciones de luz, humedad y temperatura", "Cada hábitat tiene sus propias condiciones."),
  ],
  app=[
      ("Tabla: Desierto (luz mucha, humedad poca), Bosque del sur (luz poca, humedad mucha). ¿Cuál hábitat tiene más humedad?", "El bosque del sur", "Dice humedad mucha."),
      ("Un lugar tiene poca luz, mucha humedad y fresco. ¿Es más parecido a un desierto o a un bosque?", "A un bosque", "Un bosque tiene sombra, humedad y frescura."),
      arith("Un desierto tiene 35 °C de día y 10 °C de noche. ¿Cuántos grados baja la temperatura entre el día y la noche?", "35-10", "Se resta la temperatura de la noche a la del día."),
  ],
  rea=[
      ("Un compañero dice que todos los animales pueden vivir en cualquier hábitat. Da una razón para que no tenga razón.", "Porque cada animal necesita las condiciones de su hábitat", "Las condiciones de luz, humedad y temperatura cambian."),
      ("Dos hábitats tienen la misma temperatura, pero uno es muy húmedo y el otro muy seco. ¿Son iguales? Explica.", "No; cambia la humedad", "Los hábitats se comparan por varias condiciones."),
  ],
  cha=[
      ("Describe un hábitat que tenga poca luz, mucha humedad y frío. ¿Dónde crees que está?", "Por ejemplo, una cueva húmeda", "Poca luz, mucha humedad y frío calzan con ese lugar."),
      ("¿Por qué conviene medir y no solo adivinar las condiciones de un hábitat?", "Porque los datos ayudan a comparar", "Con datos se compara con justicia."),
  ],
  context=[("En un parque de tu ciudad hay una zona soleada y seca de pasto y otra zona con árboles, sombra y suelo húmedo. ¿Cuántos hábitats distintos describes?", "2", "Son dos lugares con condiciones diferentes.")],
  selfcheck=[("¿Qué condición mide la cantidad de luz?", "La luminosidad", "Es la cantidad de luz."), ("¿Qué mide la temperatura?", "Qué tan caliente o frío está un lugar", "Se mide en grados Celsius."), ("¿Un bosque es hábitat?", "Sí", "Da alimento, agua y refugio a animales.")],
  open_task=task("Elige un hábitat de la clase, desierto o bosque, y haz una tarjeta con su dibujo. Escribe sus condiciones de luz, humedad y temperatura, y el nombre de un animal que podría vivir allí.", "Bosque: poca luz porque hay sombra, mucha humedad, temperatura fresca. Allí puede vivir el pudú.", ["dibuja el hábitat", "escribe las tres condiciones", "nombra un animal"], ["tarjeta con dibujo", "tres condiciones"], ["mezclar humedad con temperatura"], "Valora que las tres condiciones sean coherentes con el hábitat y pide la razón por la que ese animal podría vivir allí."),
  reinforce="Mira por la ventana de tu casa y describe con tres condiciones el lugar que ves.",
  extend="Piensa en un hábitat con mucha humedad y mucha luz a la vez. ¿Dónde podría haber uno?")

L(OA4, 2,
  materials="Este cuaderno con la tabla de luz y humedad de cuatro animales. Lápiz y lápices de colores.",
  use="Aprenderé cómo la luz y la humedad ayudan a un animal a sobrevivir. Sirve para entender por qué una lombriz vive bajo la tierra y una lagartija toma sol.",
  prior=["Sé que hábitat es el lugar donde vive un animal.", "Sé que luminosidad es la cantidad de luz y humedad la cantidad de agua."],
  explain=[
      "Algunos animales necesitan mucha luz. La lagartija se calienta al sol sobre las piedras, y por eso vive en lugares con mucha luz. Otros animales necesitan poca luz. La lombriz vive bajo la tierra, en la oscuridad.",
      "La humedad también cambia. La rana tiene la piel húmeda, y se seca si está mucho rato en un lugar muy seco. Por eso vive cerca del agua. En cambio, algunos animales del desierto viven en lugares muy secos y soportan la falta de agua.",
      "Para saber qué necesita un animal, miramos su hábitat. Si vive en un lugar con sombra y suelo mojado, probablemente necesita poca luz y mucha humedad. Si vive donde hay sol y suelo seco, necesita mucha luz y poca humedad.",
  ],
  vocab=[("oscuridad", "lugar sin luz o con muy poca luz"), ("sombra", "lugar donde la luz del sol no llega directo"), ("seco", "con poca agua"), ("húmedo", "con mucha agua"), ("soportar", "aguantar una condición sin dañarse")],
  worked=[
      ("Leer una tabla", "Tabla: lombriz (luz poca, humedad mucha), lagartija (luz mucha, humedad poca). ¿Cuál necesita más luz?", ["Miro la columna de luz.", "La lagartija dice mucha.", "La lombriz dice poca."], "La lagartija"),
      ("Explicar un hábitat", "¿Por qué la rana vive cerca del agua?", ["La rana tiene la piel húmeda.", "En un lugar seco se seca.", "Cerca del agua mantiene su piel húmeda."], "Porque necesita humedad para su piel"),
  ],
  mistakes=[
      ("Decir «todos los animales necesitan sol».", "No se compara con animales de la oscuridad.", "La lombriz vive bajo la tierra con poca luz; la lagartija sí busca sol."),
      ("Decir «la rana vive en lugares muy secos».", "Se olvida que su piel necesita humedad.", "La rana vive cerca del agua para mantener su piel húmeda."),
  ],
  rec=[
      ("¿Qué animal vive bajo la tierra, la lombriz o la lagartija?", "La lombriz", "Allí hay oscuridad y humedad."),
      ("¿Dónde se calienta la lagartija: al sol o en una cueva oscura?", "Al sol", "Necesita mucha luz y calor."),
      ("¿Qué necesita la piel de una rana: humedad o sequedad?", "Humedad", "Su piel es húmeda."),
  ],
  und=[
      ("¿Por qué la lagartija toma sol?", "Porque necesita luz y calor", "El sol la calienta."),
      ("¿Por qué la lombriz vive bajo la tierra?", "Porque necesita oscuridad y humedad", "Bajo la tierra hay oscuridad y humedad."),
      ("¿Qué diferencia hay entre «seco» y «húmedo»?", "Seco tiene poca agua y húmedo tiene mucha", "Se compara la cantidad de agua."),
  ],
  app=[
      ("Tabla: A lombriz (luz poca, humedad mucha), B lagartija (luz mucha, humedad poca), C rana (luz media, humedad mucha), D lagarto del desierto (luz mucha, humedad poca). Escribe las letras de los animales que necesitan humedad mucha.", "A y C", "Dicen humedad mucha."),
      arith("En un día, una lagartija toma sol 3 horas en la mañana y 2 horas en la tarde. ¿Cuántas horas toma sol en total?", "3+2", "Se suman las horas de la mañana y de la tarde."),
      ("Un animal vive en un suelo seco con mucho sol. ¿Qué luz y humedad necesita?", "Mucha luz y poca humedad", "Su hábitat da esas condiciones."),
  ],
  rea=[
      ("Una lombriz quedó sobre una piedra al sol y se quedó quieta. ¿Qué le falta y qué debe hacer un adulto para ayudarla?", "Le falta humedad y sombra; hay que devolverla a tierra húmeda", "La lombriz necesita humedad y oscuridad."),
      ("Una rana está en un lugar con mucho sol y sin agua. ¿Qué le puede pasar y por qué?", "Se puede secar porque su piel necesita humedad", "Sin humedad su piel se seca."),
  ],
  cha=[
      ("Compara dos animales: la lombriz y la lagartija. Escribe una diferencia en luz y una diferencia en humedad.", "La lombriz necesita poca luz y mucha humedad; la lagartija mucha luz y poca humedad", "Se comparan las dos condiciones en cada animal."),
      ("¿Por qué conviene dejar una piedra en su lugar si debajo hay lombrices o insectos?", "Porque ahí tienen sombra y humedad", "Sacarlos los deja sin su hábitat."),
  ],
  context=[("En el patio hay una piedra grande, y debajo hay un caracol, una lombriz y un insecto. El suelo está oscuro y húmedo. ¿Qué condición de luz y humedad tiene ese lugar?", "Poca luz y mucha humedad", "Debajo de la piedra no llega el sol y el suelo se mantiene mojado.")],
  selfcheck=[("¿Qué animal necesita mucho sol?", "La lagartija", "Se calienta al sol."), ("¿Qué necesita la piel de la rana?", "Humedad", "Su piel se seca sin agua."), ("¿La lombriz vive con poca o mucha luz?", "Con poca luz", "Vive bajo la tierra.")],
  open_task=task("Mira esta tabla: lombriz (luz poca, humedad mucha), lagartija (luz mucha, humedad poca), rana (luz media, humedad mucha). Dibuja el hábitat de dos animales y escribe una frase para cada uno que diga por qué su hábitat le sirve.", "Lombriz: vive bajo la tierra porque allí hay poca luz y mucha humedad. Lagartija: vive sobre piedras porque allí hay sol que la calienta.", ["dibuja dos hábitats", "usa luz y humedad", "escribe una frase por animal"], ["dos dibujos", "dos frases"], ["decir que todos necesitan sol"], "Revisa que cada frase mencione luz o humedad y pide que explique por qué otro animal no sobreviviría en ese lugar."),
  reinforce="Mira una piedra levantada en el patio, con un adulto, y anota si el suelo debajo está más húmedo que alrededor. Devuélvela a su lugar.",
  extend="Explica por qué una rana no podría vivir en el desierto.")

L(OA4, 3,
  materials="Este cuaderno con la tabla de temperaturas de práctica y tarjetas de tres animales. Lápiz.",
  use="Aprenderé cómo la temperatura de un hábitat decide si un animal sobrevive. Sirve para entender por qué algunos animales viven en lugares fríos y otros en lugares calurosos.",
  prior=["Sé leer números en grados (por ejemplo 20 °C).", "Sé que hábitat es el lugar donde vive un animal."],
  explain=[
      "La temperatura nos dice cuánto calor o frío hace. Se mide en grados Celsius, que se escriben °C. Por ejemplo, 5 °C es frío y 30 °C es caluroso. Cada animal soporta solo un rango de temperaturas, es decir, desde un número hasta otro.",
      "Si la temperatura de su hábitat está dentro de su rango, el animal sobrevive bien. Si es mucho más fría o más calurosa, el animal se puede enfermar o morir. Por eso algunos animales se cubren con pelo o grasa para el frío, y otros buscan sombra para el calor.",
      "Para saber si un animal puede vivir en un lugar, compara dos números: la temperatura del lugar y el rango del animal. Los datos de esta clase son de práctica y sirven para aprender a comparar, no son mediciones de especies reales.",
  ],
  vocab=[("temperatura", "qué tan caliente o frío está algo"), ("grado Celsius", "unidad para medir la temperatura (°C)"), ("rango", "desde un número hasta otro número"), ("sobrevivir", "seguir con vida"), ("dato de práctica", "número inventado para aprender, no una medición real")],
  worked=[
      ("Comparar con un rango", "Un animal de práctica vive bien entre 10 °C y 20 °C. Un lugar mide 15 °C. ¿Puede vivir allí?", ["El rango va de 10 a 20.", "15 está entre 10 y 20.", "La temperatura del lugar está dentro del rango."], "Sí, puede vivir allí"),
      ("Fuera del rango", "El mismo animal está en un lugar de 30 °C. ¿Puede vivir allí?", ["El rango llega hasta 20 °C.", "30 es mayor que 20.", "El lugar es demasiado caluroso."], "No, es demasiado caluroso"),
  ],
  mistakes=[
      ("Decir «15 °C es mayor que 20 °C».", "Se leen mal los números.", "Compara las decenas: 20 es mayor que 15."),
      ("Decir «si hace calor, todos los animales sobreviven».", "No se compara con el rango de cada animal.", "Cada animal tiene su rango: muchos no soportan el calor extremo."),
  ],
  rec=[
      ("¿Con qué unidad se mide la temperatura en esta clase?", "Grados Celsius (°C)", "Es la unidad de temperatura usada."),
      ("¿Qué número es mayor: 12 °C o 25 °C?", "25 °C", "25 es mayor que 12."),
      ("Un animal vive entre 10 °C y 20 °C. ¿18 °C está dentro de su rango?", "Sí", "18 está entre 10 y 20."),
  ],
  und=[
      ("¿Qué es un rango de temperatura?", "Desde un número hasta otro número", "Marca lo que soporta un animal."),
      ("¿Por qué algunos animales tienen pelo grueso?", "Para protegerse del frío", "El pelo abriga."),
      ("¿Por qué los datos de esta clase son «de práctica»?", "Porque son inventados para aprender", "No son mediciones reales."),
  ],
  app=[
      ("Un animal de práctica vive entre 10 °C y 20 °C. Lugar A: 8 °C, lugar B: 14 °C, lugar C: 25 °C. ¿En cuál puede vivir?", "En el lugar B", "14 °C está dentro del rango."),
      arith("Un lugar mide 30 °C de día y 12 °C de noche. ¿Cuántos grados baja de día a noche?", "30-12", "Se resta la temperatura de la noche a la del día."),
      ("Un animal de práctica vive entre 0 °C y 10 °C. ¿Está bien en un lugar de 5 °C?", "Sí", "5 °C está dentro del rango."),
  ],
  rea=[
      ("Un animal de práctica vive entre 10 °C y 20 °C. Un día el lugar baja a 4 °C. ¿Qué puede pasar y por qué?", "Puede enfermar porque hace más frío que su rango", "4 °C es menor que 10 °C."),
      ("Un animal de práctica soporta de 10 °C a 20 °C. Dos hábitats miden 5 °C y 28 °C. ¿Puede vivir en alguno? Explica.", "No; 5 °C es menor que 10 °C y 28 °C es mayor que 20 °C", "Uno es demasiado frío y el otro demasiado caluroso."),
  ],
  cha=[
      ("Un lugar tiene entre 12 °C y 18 °C todo el año. ¿Puede vivir allí un animal que soporta de 10 °C a 20 °C? Explica.", "Sí, porque todo el rango del lugar cabe en el del animal", "12 y 18 están entre 10 y 20."),
      ("¿Por qué conviene saber la temperatura mínima y la máxima de un hábitat?", "Para saber si el animal soporta todos los momentos", "El animal debe soportar el frío y el calor del lugar."),
  ],
  context=[("Un niño mide la temperatura de su patio: 9 °C en la mañana, 21 °C al mediodía y 14 °C en la tarde. ¿Cuál es la temperatura más alta que midió?", "21 °C", "21 es el mayor de los tres números.")],
  selfcheck=[("¿Qué símbolo se usa para grados Celsius?", "°C", "Es el símbolo de la unidad."), ("¿20 °C es mayor que 15 °C?", "Sí", "20 es mayor que 15."), ("¿Cada animal soporta cualquier temperatura?", "No", "Cada animal tiene su rango.")],
  open_task=task("Tienes un animal de práctica que vive entre 8 °C y 18 °C. Mira estos tres lugares: A 5 °C, B 12 °C, C 22 °C. Escribe en cuál puede vivir y en cuál no, con el número que usaste como evidencia.", "Puede vivir en B porque 12 °C está entre 8 y 18. No en A porque 5 °C es menor que 8, ni en C porque 22 °C es mayor que 18.", ["elige el lugar correcto", "usa los números del rango", "explica los lugares descartados"], ["tabla de tres lugares", "frases con números"], ["comparar mal los números", "no usar el rango"], "Valora la comparación con números y pide que invente un lugar donde el animal sí sobreviva y otro donde no."),
  reinforce="Con un adulto, mira un termómetro de pared y anota la temperatura de la mañana y de la tarde durante tres días.",
  extend="Escribe un rango de temperaturas para un animal de práctica que vive en un hábitat muy frío.")

L(OA4, 4,
  materials="Este cuaderno con las tarjetas de tres animales y de tres hábitats con sus datos. Lápiz y lápices de colores.",
  use="Aprenderé a elegir el mejor hábitat para un animal usando datos de luz, humedad y temperatura. Sirve para dar una respuesta con evidencia y no adivinar.",
  prior=["Conozco las condiciones de luz, humedad y temperatura.", "Sé comparar números de grados."],
  explain=[
      "Para elegir un hábitat, no basta decir «me parece». Hay que usar evidencia: datos que se pueden leer y comparar. Primero miramos lo que necesita el animal. Luego miramos lo que ofrece cada hábitat. Por último, decidimos cuál calza mejor.",
      "Por ejemplo, un animal de práctica necesita poca luz, mucha humedad y entre 10 °C y 18 °C. Si un hábitat da poca luz, mucha humedad y 14 °C, calza con las tres condiciones. Si solo calza con una o con dos, hay que seguir buscando.",
      "Al terminar, escribe una frase con la forma «Elijo ... porque ...» y cita los datos. Si falta un dato, dilo: no inventes información. Una buena elección explica qué datos usó y por qué los otros hábitats no sirven.",
  ],
  vocab=[("evidencia", "datos que sostienen mi respuesta"), ("calzar", "coincidir con lo que se necesita"), ("condición", "característica de un hábitat, como luz, humedad o temperatura"), ("necesidad", "lo que un animal requiere para vivir"), ("justificar", "explicar una decisión con razones")],
  worked=[
      ("Elegir con tres datos", "Animal de práctica: poca luz, mucha humedad, 10 a 18 °C. Hábitat A: poca luz, mucha humedad, 14 °C. Hábitat B: mucha luz, poca humedad, 30 °C. ¿Cuál elige?", ["Reviso la luz: el A coincide.", "Reviso la humedad y la temperatura: el A coincide, 14 está entre 10 y 18.", "El B no coincide en ninguna."], "El hábitat A"),
      ("Descartar con un dato", "El mismo animal tiene el hábitat C: poca luz, mucha humedad, 25 °C. ¿Sirve?", ["La luz coincide.", "La humedad coincide.", "La temperatura 25 °C está fuera del rango de 10 a 18 °C."], "No sirve, porque está muy caluroso"),
  ],
  mistakes=[
      ("Elegir mirando solo una condición.", "Se ignoran las otras dos.", "Revisa luz, humedad y temperatura, y marca cada una con un visto."),
      ("Elegir porque «el dibujo es lindo».", "No se usa evidencia.", "Usa los datos de la tabla, no el aspecto del dibujo."),
  ],
  rec=[
      ("¿Qué tres condiciones debes revisar antes de elegir un hábitat?", "Luz, humedad y temperatura", "Son las condiciones de la clase."),
      ("Un animal necesita poca luz. ¿Sirve un lugar con mucha luz?", "No", "No coincide con lo que necesita."),
      ("Un animal soporta de 10 °C a 18 °C. ¿14 °C está en su rango?", "Sí", "14 está entre 10 y 18."),
  ],
  und=[
      ("¿Qué es la evidencia al elegir un hábitat?", "Los datos que muestran que la elección es buena", "Sostiene la respuesta."),
      ("¿Qué significa «calzar» con un hábitat?", "Que coincide con lo que el animal necesita", "Las condiciones sirven."),
      ("¿Qué debes hacer si falta un dato en la tabla?", "Decir que falta y no inventarlo", "Una conclusión necesita datos reales."),
  ],
  app=[
      ("Animal de práctica: mucha luz, poca humedad, 25 a 40 °C. Hábitat A: poca luz, mucha humedad, 12 °C. Hábitat B: mucha luz, poca humedad, 32 °C. ¿Cuál elige?", "El hábitat B", "Coincide en luz, humedad y temperatura."),
      arith("Un hábitat mide 14 °C y el rango del animal llega hasta 18 °C. ¿Cuántos grados le faltan al hábitat para llegar al tope del animal?", "18-14", "Se resta la temperatura del hábitat al máximo del rango."),
      ("Un animal necesita mucha humedad. Hábitat A: humedad poca. Hábitat B: humedad mucha. ¿Cuál es mejor solo por humedad?", "El hábitat B", "Coincide con la necesidad."),
  ],
  rea=[
      ("Un hábitat tiene la luz y la humedad que un animal necesita, pero está a 3 °C y el animal vive entre 10 °C y 18 °C. ¿Lo eliges? Explica.", "No; la temperatura es menor que su rango", "Dos condiciones no bastan si una falla."),
      ("Dos hábitats calzan con las tres condiciones. ¿Cómo decides entre ellos?", "Busco otra evidencia, como alimento o refugio", "Cuando las condiciones empatan, hay que mirar otros datos."),
  ],
  cha=[
      ("Escribe una frase «Elijo ... porque ...» para el animal de práctica de mucha luz, poca humedad y 25 a 40 °C, entre un hábitat A de 32 °C seco y soleado y otro B de 12 °C sombrío.", "Elijo el hábitat A porque tiene mucha luz, poca humedad y 32 °C", "Cita tres datos que coinciden."),
      ("¿Por qué es mejor usar datos medidos que opiniones al elegir un hábitat?", "Porque los datos se pueden comprobar", "Una opinión puede cambiar según quién la diga."),
  ],
  context=[("Una escuela quiere crear un rincón para lombrices. Con datos de práctica, necesitan poca luz, mucha humedad y entre 10 °C y 20 °C. El rincón A tiene 16 °C, sombra y suelo húmedo. El rincón B tiene 28 °C, sol y suelo seco. ¿Cuál elige la escuela?", "El rincón A", "Coincide en luz, humedad y temperatura.")],
  selfcheck=[("¿Cuántas condiciones debes revisar al elegir un hábitat?", "Tres", "Luz, humedad y temperatura."), ("¿Qué escribes si falta un dato?", "Que falta ese dato", "No se debe inventar."), ("¿Elegir con evidencia es adivinar?", "No", "Se usan datos.")],
  open_task=task("Un animal de práctica necesita mucha humedad, poca luz y 6 a 14 °C. Tienes tres hábitats: A seco, soleado, 30 °C. B húmedo, sombrío, 10 °C. C húmedo, soleado, 20 °C. Escribe cuál eliges y qué dato descarta a los otros.", "Elijo B porque es húmedo, tiene sombra y 10 °C está entre 6 y 14. A es seco y C tiene mucha luz y 20 °C.", ["elige el hábitat correcto", "cita tres datos", "descarta los otros con evidencia"], ["frase con «porque»", "tabla de comparación"], ["elegir con una sola condición"], "Valora que descarte A y C con un dato concreto cada uno."),
  reinforce="Haz una tabla de dos filas, necesidades del animal y lo que ofrece un hábitat, y marca con un visto las que coinciden.",
  extend="Inventa un animal de práctica con sus necesidades y pide a un familiar que elija el hábitat correcto entre dos que tú escribas.")
