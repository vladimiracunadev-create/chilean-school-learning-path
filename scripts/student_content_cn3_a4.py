"""Cuaderno del estudiante, 3.º básico Ciencias Naturales: OA 07 (higiene y manipulación segura de alimentos)."""
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


OA7 = "CN03 OA 07"

L(OA7, 1,
  materials="Este cuaderno, lápiz y lápices de colores. Para la actividad, con una persona adulta: un poco de harina (maicena si alguien tiene alergia al trigo), una mesa limpia y un paño o papel.",
  use="Aprenderé cómo un alimento puede ensuciarse con cosas que no se ven. Sirve para entender por qué la higiene en la cocina evita enfermedades.",
  prior=["Sé que debo lavarme las manos antes de comer.", "Sé que hay seres vivos muy pequeños que no se ven."],
  explain=[
      "Los microorganismos son seres vivos tan pequeños que solo se ven con un microscopio. Hay muchos tipos, como las bacterias. La mayoría no nos hace daño, y algunos hasta ayudan, como los que se usan para hacer el yogur. Pero algunos pueden enfermarnos si llegan a los alimentos que comemos.",
      "La contaminación ocurre cuando un alimento recibe suciedad o microorganismos que pueden hacer daño. Puede pasar por manos sucias, por una tabla o un cuchillo sin lavar, por moscas, por agua que no es segura, o por toser o estornudar sobre la comida. Una contaminación puede ir de un lugar a otro en varios pasos, como una cadena.",
      "Como no se ve, puedes imitar la contaminación con harina. Con una persona adulta, ponte un poco de harina en las manos, que representa a los microorganismos. Toca una taza, una llave o una mesa y mira las marcas blancas. Verás que la harina pasó de tus manos a los objetos. No te acerques la harina a la cara ni la soples, y no la comas. Así se mueve la suciedad en la cocina. Si un alimento enferma a alguien, puede dar dolor de estómago, vómitos o diarrea, y hay que avisar a una persona adulta.",
  ],
  vocab=[("microorganismo", "ser vivo tan pequeño que solo se ve con microscopio"), ("contaminación", "cuando un alimento recibe suciedad o microorganismos dañinos"), ("cadena de contaminación", "serie de pasos por donde viaja la suciedad"), ("superficie", "parte de afuera de un objeto, como una mesa o una tabla"), ("prevención", "acciones para evitar que algo malo ocurra")],
  worked=[
      ("Seguir la ruta", "Una niña toca la basura y sin lavarse las manos toca un pan. ¿Qué ruta de contaminación hay?", ["Las manos tocan la basura y se ensucian.", "Con las manos sucias toca el pan.", "La suciedad pasó de las manos al pan."], "De la basura a las manos y de las manos al pan"),
      ("Cortar la cadena", "Un niño sabe que sus manos están sucias antes de tocar fruta. ¿Qué paso corta la cadena?", ["La cadena pasa por las manos.", "Si las lavo antes, la suciedad no llega a la fruta.", "Lavarse las manos corta la cadena."], "Lavarse las manos antes de tocar la fruta"),
  ],
  mistakes=[
      ("Decir «si se ve limpio, está limpio».", "Los microorganismos no se ven a simple vista.", "Lava las manos y los utensilios aunque se vean limpios."),
      ("Decir «todos los microorganismos son dañinos».", "Muchos no hacen daño y algunos ayudan.", "Solo algunos pueden enfermarnos; por eso se previene la contaminación."),
  ],
  rec=[
      ("Un ser vivo tan pequeño que solo se ve con microscopio, ¿es un microorganismo o un insecto?", "Un microorganismo", "Es la definición de la clase."),
      ("Si un alimento se ensucia con microorganismos dañinos, ¿hay contaminación? Responde Sí o No.", "Sí", "Eso es contaminación."),
      ("¿Se ven los microorganismos con los ojos solos? Responde Sí o No.", "No", "Solo se ven con microscopio."),
  ],
  und=[
      ("Nombra dos formas en que se puede contaminar un alimento.", "Manos sucias, tabla sin lavar, moscas, agua no segura o estornudar sobre él (dos de ellas)", "Son rutas vistas en la clase."),
      ("¿Para qué se usa la harina en el modelo de la actividad?", "Para imitar los microorganismos y ver cómo pasan de un lugar a otro", "La harina representa lo que no se ve."),
      ("¿Qué es la prevención?", "Acciones para evitar que algo malo ocurra", "Por ejemplo, lavarse las manos."),
  ],
  app=[
      ("Casos: A) alguien toca el pan con las manos limpias, B) una mosca camina sobre el pan, C) una persona estornuda sobre el pan. ¿Cuáles son rutas de contaminación?", "B y C", "La mosca y el estornudo pueden llevar microorganismos."),
      arith("En la actividad de harina, una niña dejó 7 marcas blancas en la mesa, 3 en la llave y 2 en una taza. ¿Cuántas marcas dejó en total?", "7+3+2", "Se suman las marcas de cada objeto."),
      ("Un niño ve que su mascota lamió su plato. ¿Es mejor lavar el plato antes de usarlo o usarlo así?", "Lavarlo antes de usarlo", "La mascota puede dejar microorganismos."),
  ],
  rea=[
      ("Una cocinera corta carne cruda y luego fruta con el mismo cuchillo sin lavarlo. ¿Qué ruta de contaminación hay?", "Del cuchillo a la fruta", "El cuchillo sin lavar pasa microorganismos de la carne a la fruta."),
      ("Un niño dice: «Si no veo suciedad en mis manos, no hace falta lavarlas». ¿Qué le respondes?", "Que los microorganismos no se ven", "Lavar las manos sigue siendo necesario."),
  ],
  cha=[
      ("Dibuja con palabras una cadena de contaminación de cuatro lugares u objetos que empiece en la basura y termine en una ensalada.", "Basura → manos → tabla → ensalada", "Cada paso lleva la suciedad al siguiente."),
      ("Escribe dos pasos que cortarían esa cadena.", "Lavarse las manos y lavar la tabla", "Cortan el paso de la suciedad."),
  ],
  context=[("En la cocina de una escuela se usan 3 tablas, 4 cuchillos y 2 ollas. Ninguno se lavó después de usarlo. ¿Cuántos objetos pueden pasar suciedad al próximo alimento?", "9", "Se suman los objetos sin lavar. Cálculo: 3 + 4 + 2 = 9.")],
  selfcheck=[("¿Qué es la contaminación de un alimento?", "Cuando recibe suciedad o microorganismos dañinos", "Puede enfermar a quien lo come."), ("Nombra una ruta de contaminación.", "Manos sucias, tabla sin lavar, moscas, estornudos o agua no segura (una de ellas)", "Son rutas vistas en la clase."), ("¿Lavarse las manos corta la cadena de contaminación? Responde Sí o No.", "Sí", "Evita que la suciedad pase al alimento.")],
  open_task=task("Con una persona adulta, haz la prueba de la harina: ponte harina en las manos, toca tres objetos de la cocina y cuenta las marcas blancas. Dibuja la ruta de la harina con flechas y escribe un paso que cortaría la cadena. Si no puedes hacerlo, usa este ejemplo: harina en las manos, 7 marcas en la mesa, 3 en la llave y 2 en una taza. Después limpia todo con un paño.", "Ruta: manos → mesa, llave y taza. 12 marcas. Para cortar la cadena: lavarse las manos antes de tocar los objetos.", ["cuenta las marcas", "dibuja la ruta con flechas", "propone un paso que corta la cadena"], ["dibujo de la ruta", "conteo de marcas"], ["comer la harina usada", "no escribir un paso de prevención"], "Revisa el conteo y que el paso propuesto interrumpa realmente la ruta."),
  reinforce="Dibuja tres rutas por las que se puede contaminar un alimento.",
  extend="Piensa en tu cocina y escribe dos lugares donde podría haber microorganismos aunque se vean limpios.")

L(OA7, 2,
  materials="Este cuaderno, lápiz y lápices de colores. Para la prueba, con una persona adulta: harina (maicena si alguien tiene alergia al trigo), jabón, agua y toalla limpia.",
  use="Aprenderé a lavarme las manos con un procedimiento de pasos. Sirve para sacar la suciedad que no se ve antes de tocar o comer alimentos.",
  prior=["Sé que los microorganismos no se ven y pueden pasar de las manos a los alimentos.", "Sé que lavarse las manos corta la cadena de contaminación."],
  explain=[
      "Hay momentos en que hay que lavarse las manos: antes de preparar o comer alimentos, después de ir al baño, después de tocar basura o mascotas, y después de toser, estornudar o sonarse la nariz. El agua sola no sirve tanto. El jabón ayuda a despegar la suciedad de la piel, y el agua se la lleva al enjuagar.",
      "El procedimiento tiene ocho pasos. Uno: mójate las manos con agua limpia. Dos: pon jabón. Tres: frota las palmas. Cuatro: frota el dorso de cada mano. Cinco: frota entre los dedos. Seis: frota los pulgares y las uñas. Siete: enjuaga con agua. Ocho: seca con una toalla limpia o con papel. Los pasos de frotar deben durar al menos 20 segundos; cuenta despacio hasta 20.",
      "Puedes comprobarlo con harina. Con una persona adulta, ponte harina en las dos manos. Lava una mano solo con agua, frotando 20 segundos. Lava la otra con agua y jabón, frotando también 20 segundos. Así solo cambia el jabón. Mira cuánta harina queda en cada una. Con jabón queda mucho menos. Esa diferencia es la evidencia de que el jabón ayuda. Repite la prueba otro día para ver si sale parecido.",
  ],
  vocab=[("procedimiento", "serie de pasos que se hacen en orden"), ("jabón", "producto que ayuda a despegar la suciedad de la piel"), ("dorso", "parte de la mano que se ve cuando la cierras"), ("enjuagar", "sacar el jabón con agua"), ("evidencia", "datos que muestran si algo funciona")],
  worked=[
      ("Ordenar los pasos", "Pasos: A) enjuagar, B) mojar las manos, C) poner jabón, D) frotar. ¿En qué orden va?", ["Primero se mojan las manos.", "Luego se pone jabón y se frota.", "Después se enjuaga."], "B, C, D, A"),
      ("Leer una prueba", "En una prueba de ejemplo con harina, la mano lavada solo con agua tenía 14 motas y la mano lavada con jabón tenía 2. Las dos se frotaron 20 segundos. ¿Cuántas motas menos tenía la segunda?", ["Busco los datos: 14 y 2.", "Resto: 14 − 2 = 12.", "La mano lavada con jabón tenía 12 motas menos."], "12 motas menos"),
  ],
  mistakes=[
      ("Mojar las manos y secarlas enseguida.", "Sin jabón y sin frotar no se saca la suciedad.", "Usa jabón y frota todas las partes de las manos."),
      ("Frotar solo las palmas.", "Se quedan sucios el dorso, entre los dedos y las uñas.", "Sigue los ocho pasos, incluida la zona entre los dedos."),
  ],
  rec=[
      ("¿Hay que lavarse las manos antes de preparar alimentos? Responde Sí o No.", "Sí", "Así no se pasan microorganismos a la comida."),
      ("¿Qué ayuda a despegar la suciedad: el jabón o el aire?", "El jabón", "Despega la suciedad de la piel."),
      ("¿Cuánto debe durar como mínimo el frotado: 5 o 20 segundos?", "20 segundos", "Es el tiempo mínimo recomendado."),
  ],
  und=[
      ("Nombra dos momentos en que hay que lavarse las manos.", "Antes de comer, después del baño, después de tocar mascotas o basura (dos de ellos)", "Son momentos vistos en la clase."),
      ("¿Por qué el agua sola no sirve tanto?", "Porque no despega bien la suciedad sin jabón", "El jabón ayuda a despegarla."),
      ("¿Para qué se seca con una toalla limpia?", "Para no volver a ensuciar las manos", "Una toalla sucia las contamina otra vez."),
  ],
  app=[
      ("Ordena con letras los pasos: A) secar, B) poner jabón, C) mojar las manos, D) enjuagar, E) frotar.", "C, B, E, D, A", "Mojar, jabón, frotar, enjuagar y secar."),
      arith("Una niña cuenta hasta 20 al frotar sus manos cuatro veces en un día. ¿Cuántos segundos frotó en total?", "20*4", "Se multiplican los segundos por las veces."),
      ("Un niño se lavó el dorso y las palmas, pero no entre los dedos. ¿Qué parte quedó sin lavar?", "Entre los dedos", "No frotó esa zona."),
  ],
  rea=[
      ("Mano A lavada solo con agua, 20 segundos: 14 motas. Mano B lavada con agua y jabón, 20 segundos: 2 motas. ¿Qué evidencia hay de que el jabón ayuda?", "La mano B tiene mucho menos harina que la A y solo cambió el jabón", "Menos harina quiere decir más suciedad sacada."),
      ("Una niña se lava las manos con jabón, pero se las seca con un paño que cayó al suelo. ¿Qué puede pasar?", "Las manos pueden volver a ensuciarse", "El paño sucio contamina."),
  ],
  cha=[
      ("En la prueba de harina, nombra dos cosas que deben ser iguales en las dos manos para que sea justa.", "La cantidad de harina y el tiempo de frotado", "Solo debe cambiar el jabón."),
      ("Escribe un lugar de la casa donde conviene tener jabón y toalla limpia y por qué.", "Cerca del lavamanos de la cocina, para lavarse antes de preparar alimentos", "Así es fácil lavarse antes de cocinar."),
  ],
  context=[("Un curso de 3.º cuenta cuántas veces se lavan las manos antes de comer: lunes, 18 niños; martes, 21 niños. ¿Cuántos niños más se lavaron el martes que el lunes?", "3", "Se resta lo del lunes a lo del martes. Cálculo: 21 − 18 = 3.")],
  selfcheck=[("¿Cuántos pasos tiene el procedimiento de lavado de manos de la clase?", "Ocho", "Son ocho pasos."), ("¿Qué paso va justo después de poner jabón?", "Frotar las palmas", "Se frota con jabón."), ("¿Se secan las manos con una toalla sucia? Responde Sí o No.", "No", "Se ensuciarían otra vez.")],
  open_task=task("Con una persona adulta, haz la prueba de la harina. Ponte harina en las dos manos. Lava una mano solo con agua, frotando 20 segundos, y la otra con agua y jabón, frotando también 20 segundos. Cuenta o mira cuánta harina queda y anota los resultados. Escribe una conclusión. Si no puedes, usa el ejemplo: solo agua, 14 motas; con jabón, 2 motas. Dibuja los ocho pasos con números.", "Solo agua: 14 motas. Con jabón: 2 motas. Conclusión: el jabón saca más suciedad que solo el agua.", ["registra los dos resultados", "escribe una conclusión con números", "dibuja los ocho pasos en orden"], ["tabla con dos manos", "dibujo con ocho pasos"], ["cambiar más de una cosa entre las dos manos", "olvidar un paso"], "Pregunta qué cambió entre las dos manos y cuál es la conclusión."),
  reinforce="Escribe los ocho pasos del lavado de manos con tus palabras y dibuja uno de ellos.",
  extend="Escribe una canción corta o un conteo para acordarte de los ocho pasos, sin copiar letras de otras canciones.")

L(OA7, 3,
  materials="Este cuaderno, lápiz y lápices de colores. Imagina una cocina con dos tablas de cortar de colores distintos. Los cuchillos y la cocina los usa una persona adulta.",
  use="Aprenderé a separar alimentos, tablas y utensilios para que no se pasen microorganismos. Sirve para cocinar con seguridad y guardar los alimentos de manera segura.",
  prior=["Sé que hay rutas de contaminación.", "Sé el procedimiento de lavado de manos."],
  explain=[
      "Hay alimentos crudos, como la carne, el pollo, el pescado y los huevos con cáscara, que pueden tener microorganismos dañinos. También hay alimentos listos para comer, como las frutas lavadas, las ensaladas y el pan. Si los crudos tocan a los listos, o si se usa la misma tabla o el mismo cuchillo sin lavar, se produce contaminación cruzada.",
      "Para evitarla, se usan tablas y utensilios separados: una tabla para crudos y otra para alimentos listos. Si hay una sola tabla, se prepara primero lo listo para comer y después lo crudo. Todo lo que tocó un alimento crudo se lava con agua y detergente antes de volver a usarlo. Un plato que tuvo carne cruda no sirve para la carne ya cocida. Las frutas y verduras se lavan con agua limpia.",
      "La temperatura también cuida los alimentos. El refrigerador mantiene el frío (5 °C o menos) y hace que los microorganismos crezcan más despacio; por eso los alimentos que se echan a perder se guardan ahí enseguida. No deben quedarse fuera del refrigerador más de dos horas, y menos si hace mucho calor. En el refrigerador, los alimentos crudos se guardan tapados y abajo, para que no goteen sobre los alimentos listos para comer. Cocinar bien los alimentos lo hace una persona adulta.",
  ],
  vocab=[("contaminación cruzada", "paso de microorganismos de un alimento a otro"), ("alimento crudo", "alimento que no se ha cocinado, como la carne o el pollo"), ("alimento listo para comer", "alimento que no se cocina antes de comer, como una ensalada"), ("utensilio", "objeto que se usa para cocinar o comer, como un cuchillo o un cucharón"), ("refrigerador", "aparato que mantiene fríos los alimentos")],
  worked=[
      ("Detectar contaminación cruzada", "Una persona corta pollo crudo en una tabla y luego corta tomates en esa misma tabla sin lavarla. ¿Qué error hay?", ["El pollo crudo puede tener microorganismos.", "La tabla se los pasa a los tomates.", "Los tomates se comen sin cocinar."], "Contaminación cruzada: hay que lavar la tabla o usar otra"),
      ("Decidir el orden", "Con una sola tabla hay que preparar ensalada y cortar carne cruda. ¿Qué se prepara primero?", ["Lo listo para comer no se vuelve a cocinar.", "Se prepara primero la ensalada.", "Después se corta la carne y se lava la tabla."], "Primero la ensalada"),
  ],
  mistakes=[
      ("Poner la carne cocida en el mismo plato donde estaba cruda.", "El plato tiene microorganismos de la carne cruda.", "Usa un plato limpio para la carne cocida."),
      ("Dejar la leche y el yogur fuera del refrigerador por toda la tarde.", "A temperatura ambiente los microorganismos crecen rápido.", "Guárdalos en el refrigerador enseguida."),
  ],
  rec=[
      ("El pollo crudo, ¿es un alimento crudo o listo para comer?", "Crudo", "No está cocinado."),
      ("Una ensalada de lechuga lavada, ¿es un alimento crudo o listo para comer?", "Listo para comer", "No se cocina antes de comer."),
      ("¿Los alimentos que se echan a perder se guardan en el refrigerador? Responde Sí o No.", "Sí", "El frío frena a los microorganismos."),
  ],
  und=[
      ("¿Qué es la contaminación cruzada?", "El paso de microorganismos de un alimento a otro", "Pasa por manos, tablas o utensilios."),
      ("¿Por qué se usan dos tablas, una para crudos y otra para listos?", "Para que los microorganismos de los crudos no pasen a los listos", "Así se evita la contaminación cruzada."),
      ("¿Cuánto tiempo, como máximo, pueden estar los alimentos que se echan a perder fuera del refrigerador?", "Dos horas", "Es el tiempo máximo de la clase."),
  ],
  app=[
      ("Tarjetas: A) pollo crudo, B) pan, C) tomate lavado, D) pescado crudo. Escribe las letras de los alimentos crudos.", "A y D", "Pollo y pescado sin cocinar son crudos."),
      arith("Una cocina tiene 2 tablas de cortar, 3 cuchillos y 4 platos. Después de preparar carne cruda hay que lavar todo con agua y detergente. ¿Cuántos objetos hay que lavar?", "2+3+4", "Se suman todos los objetos."),
      ("Una niña tiene una sola tabla. Va a cortar fruta y también carne cruda. ¿Qué corta primero: la fruta o la carne?", "La fruta", "Lo listo para comer va primero."),
  ],
  rea=[
      ("Un cuchillo que cortó pollo crudo se usa para cortar pan sin lavarlo. ¿Qué puede pasar con el pan?", "Puede contaminarse con los microorganismos del pollo", "El pan se come sin cocinar."),
      ("Una familia sale de un paseo y deja un pollo cocido sobre la mesa de la cocina por toda la tarde. ¿Qué debería haber hecho?", "Guardarlo en el refrigerador antes de las dos horas", "El frío frena el crecimiento."),
  ],
  cha=[
      ("Ordena con letras los pasos para preparar sin riesgos: A) lavar la tabla con agua y detergente, B) cortar la ensalada, C) cortar carne cruda.", "B, C, A", "Primero lo listo, luego lo crudo y al final se lava."),
      ("Explica por qué cocinar bien lo hace una persona adulta.", "Porque el fuego y los cuchillos son peligrosos para los niños", "La seguridad exige que lo haga una persona adulta."),
  ],
  context=[("En una cocina hay 6 huevos con cáscara, 4 trozos de pollo crudo y 5 tomates lavados. ¿Cuántos alimentos crudos hay que mantener separados de los tomates?", "10", "Los huevos con cáscara y el pollo son crudos. Cálculo: 6 + 4 = 10.")],
  selfcheck=[("¿Qué se hace antes de volver a usar una tabla que tocó carne cruda?", "Se lava con agua y detergente", "Así se saca la contaminación."), ("¿Dónde se guardan los alimentos que se echan a perder?", "En el refrigerador", "El frío frena a los microorganismos."), ("¿Puede un niño cocinar solo con fuego y cuchillos? Responde Sí o No.", "No", "Debe hacerlo una persona adulta.")],
  open_task=task("Mira esta lista de una cocina: pollo crudo, ensalada de lechuga lavada, tabla verde, tabla roja, pan y fruta lavada. Escribe en una tabla qué va en la tabla verde (alimentos listos para comer) y qué va en la tabla roja (alimentos crudos). Después ordena los pasos para preparar sin contaminación cruzada y dibuja la cocina con flechas.", "Tabla verde: ensalada, pan, fruta lavada. Tabla roja: pollo crudo. Pasos: preparar lo listo, luego lo crudo, lavar utensilios y tablas.", ["clasifica crudos y listos", "ordena los pasos", "dibuja la cocina con flechas"], ["tabla de clasificación", "dibujo con flechas"], ["poner el pollo en la tabla de lo listo", "no lavar después"], "Revisa que cada alimento esté en la tabla correcta y que el orden de los pasos evite la contaminación cruzada."),
  reinforce="Dibuja el refrigerador con tres alimentos que van ahí y un alimento crudo separado de los listos.",
  extend="Explica cómo organizarías el refrigerador de tu casa para que los crudos no toquen a los alimentos listos.")

L(OA7, 4,
  materials="Este cuaderno, lápiz, lápices de colores y una cartulina o una hoja grande. Con una persona de tu casa, para probar tu mensaje.",
  use="Aprenderé a comunicar una práctica de higiene de manera clara. Sirve para que otras personas la entiendan y se animen a hacerla.",
  prior=["Sé las rutas de contaminación y el lavado de manos.", "Sé separar crudos y alimentos listos."],
  explain=[
      "Una práctica preventiva es una acción que se repite para evitar una enfermedad. Lavarse las manos antes de comer, usar tablas separadas y guardar los alimentos en el refrigerador son prácticas preventivas. Para que otras personas las hagan, hay que comunicarlas con claridad.",
      "Un buen mensaje tiene un título corto, tres pasos con verbos (lava, separa, guarda), una razón y un dibujo. Cada paso debe ser una acción posible. Se escribe con letras grandes y se evitan las palabras difíciles. La razón puede ser un dato, como: «El jabón saca la suciedad que no se ve».",
      "Después de hacer el mensaje, hay que probarlo. Se le muestra a otra persona y se le pide que diga qué entendió. Si no lo entendió, se mejora. Luego se registra si las personas hacen la práctica, por ejemplo cuántas se lavan las manos antes de comer, sin escribir nombres. Si después del mensaje la práctica se hace más veces, puede ser que el mensaje ayudó.",
  ],
  vocab=[("práctica preventiva", "acción que se repite para evitar una enfermedad"), ("mensaje", "información que se quiere comunicar a otros"), ("paso", "cada acción dentro de una serie"), ("razón", "dato que explica por qué se hace algo"), ("registro", "anotación de cuántas veces se hizo algo")],
  worked=[
      ("Mejorar un mensaje", "Un cartel dice: «Higiene es importante». ¿Qué le falta para ser un buen mensaje?", ["Tiene un título, pero no dice qué hacer.", "Falta una acción con un verbo y una razón.", "Podría decir: «Lava tus manos antes de comer»."], "Le faltan acciones concretas y una razón"),
      ("Revisar con datos", "Antes del cartel, 12 de 20 niños se lavaban las manos antes de comer. Después del cartel, 17 de 20. ¿Cuántos niños más se lavan ahora?", ["Antes: 12.", "Después: 17.", "Resto: 17 − 12 = 5."], "5 niños más"),
  ],
  mistakes=[
      ("Escribir un cartel con mucho texto pequeño.", "No se lee con facilidad.", "Usa un título corto, tres pasos y un dibujo."),
      ("Escribir los nombres de las personas que no se lavan las manos.", "Se las puede avergonzar y no es necesario.", "Anota solo cuántas personas lo hacen, sin nombres."),
  ],
  rec=[
      ("Lavarse las manos antes de comer, ¿es una práctica preventiva? Responde Sí o No.", "Sí", "Evita que se transmitan enfermedades."),
      ("¿Los pasos de un mensaje deben empezar con un verbo, como «lava»? Responde Sí o No.", "Sí", "Un verbo dice qué hacer."),
      ("¿Un cartel necesita un dibujo? Responde Sí o No.", "Sí", "Ayuda a entender el mensaje."),
  ],
  und=[
      ("¿Qué es una práctica preventiva?", "Una acción que se repite para evitar una enfermedad", "Por ejemplo, lavarse las manos."),
      ("¿Para qué sirve mostrarle el mensaje a otra persona antes de colgarlo?", "Para saber si lo entiende y poder mejorarlo", "Así se comprueba que es claro."),
      ("¿Por qué no se escriben nombres en el registro?", "Para no avergonzar a nadie", "Solo importa cuántos lo hacen."),
  ],
  app=[
      arith("Un registro dice que 14 de 20 personas se lavaron las manos antes de comer. ¿Cuántas personas no lo hicieron?", "20-14", "Se resta lo cumplido al total."),
      ("Cartel A: «¡Cuida tu salud!». Cartel B: «Lava tus manos con jabón antes de comer». ¿Cuál dice una acción concreta?", "B", "B dice qué hacer."),
      ("Cartel A: cinco líneas de texto pequeño sin dibujo. Cartel B: título corto, tres pasos con verbos y un dibujo. ¿Cuál se entiende mejor?", "B", "B sigue lo que pide un buen mensaje."),
  ],
  rea=[
      ("Antes del cartel se lavaban 8 de 20 niños. Después, 9 de 20. ¿Funcionó mucho el mensaje? Explica.", "Poco, porque solo mejoró en 1 niño", "Conviene mejorar el mensaje."),
      ("Un niño dice: «Si pongo el cartel, ya no necesito lavarme las manos». ¿Qué le respondes?", "Que el cartel recuerda la práctica, pero hay que hacerla", "La práctica protege, no el cartel."),
  ],
  cha=[
      ("Escribe un mensaje de tres pasos con verbos para prevenir la contaminación de los alimentos.", "Por ejemplo: 1) Lava tus manos. 2) Separa los crudos. 3) Guarda en el refrigerador", "Cada paso es una acción posible."),
      ("Escribe cómo comprobarías si tu mensaje funcionó durante una semana.", "Contando cuántas personas hacen la práctica antes y después", "Se compara el registro de antes y después."),
  ],
  context=[("En una escuela se registraron 10 niños que se lavaban las manos antes de comer el lunes y 16 el viernes. ¿Cuántos niños más lo hicieron el viernes?", "6", "Se resta lo del lunes a lo del viernes. Cálculo: 16 − 10 = 6.")],
  selfcheck=[("¿Qué debe tener un buen mensaje de higiene?", "Título corto, pasos con verbos, razón y dibujo", "Así se entiende y se anima a hacerlo."), ("¿Se anotan nombres en el registro? Responde Sí o No.", "No", "Solo se cuentan personas."), ("¿Para qué se prueba el mensaje con otra persona?", "Para ver si lo entiende", "Se puede mejorar.")],
  open_task=task("Elige una práctica: A) lavarse las manos antes de comer, B) usar tablas separadas para crudos y listos, o C) guardar los alimentos en el refrigerador. Haz un cartel con un título corto, tres pasos con verbos, una razón y un dibujo. Muéstraselo a una persona de tu casa y pídele que diga qué entendió. Durante tres días, anota cuántas personas hacen la práctica, sin escribir nombres. Si no puedes, usa este registro: lunes, 3 personas; martes, 4; miércoles, 5.", "Elegí A. Título: «Manos limpias». Pasos: moja, enjabona, frota. Razón: el jabón saca la suciedad que no se ve. Registro: 3, 4 y 5 personas.", ["incluye título, tres pasos, razón y dibujo", "prueba el mensaje con otra persona", "registra datos sin nombres"], ["cartel", "tabla de tres días"], ["escribir mucho texto", "anotar nombres"], "Revisa que los pasos sean acciones con verbos y que el registro compare días."),
  reinforce="Dibuja un cartel pequeño con el título «Manos limpias» y tres pasos.",
  extend="Escribe una pregunta que le harías a una persona de tu familia para saber si entendió tu mensaje.")
