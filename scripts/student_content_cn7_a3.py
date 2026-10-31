"""Cuaderno del estudiante, 7.º básico Ciencias Naturales: OA 05 (virus, bacterias y hongos) y OA 06 (microorganismos y biotecnología)."""
from __future__ import annotations

from student_content_cn7_a import L, task
from student_lessons import arith

OA5, OA6 = "CN07 OA 05", "CN07 OA 06"

# ---------------------------------------------------------------- OA 05
L(OA5, 1,
  materials="Este cuaderno y lápiz. Las medidas están escritas en cada ejercicio; no necesitas microscopio.",
  use="Aprenderé a comparar el tamaño y la estructura de virus, bacterias y hongos usando unidades muy pequeñas. Sirve para entender por qué algunos se ven con microscopio óptico y otros no.",
  prior=["Sé que los microorganismos son seres muy pequeños.", "Sé que la célula es la unidad básica de los seres vivos."],
  explain=[
      "Los microorganismos son tan pequeños que se miden en micrómetros (µm) y nanómetros (nm). Un milímetro (mm) tiene 1.000 µm, y un micrómetro tiene 1.000 nm. Un virus mide cerca de 100 nm, una bacteria como Escherichia coli mide unos 2 µm de largo y una levadura (hongo de una sola célula) mide entre 5 y 10 µm. Los virus se ven solo con microscopio electrónico.",
      "Cada grupo tiene una estructura distinta. Un virus no es una célula: tiene material genético protegido por una cubierta de proteínas llamada cápside. Una bacteria es una célula procarionte: su material genético está suelto en el citoplasma, sin núcleo, y tiene pared celular. Un hongo es una célula eucarionte: tiene núcleo y una pared de quitina. Hay hongos de una sola célula, como las levaduras, y de muchas, como el moho.",
      "Para comparar tamaños hay que usar la misma unidad. Si un virus mide 100 nm y una bacteria 2 µm (2.000 nm), la bacteria es 20 veces más larga. Un dibujo que muestre ambos del mismo tamaño tiene un error de escala.",
  ],
  vocab=[("micrómetro (µm)", "milésima parte de un milímetro"), ("nanómetro (nm)", "milésima parte de un micrómetro"), ("cápside", "cubierta de proteínas de un virus"), ("procarionte", "célula sin núcleo, con el material genético suelto"), ("eucarionte", "célula con núcleo")],
  worked=[
      ("Cuántos virus caben", "Un virus mide 100 nm. ¿Cuántos caben en fila en 1 µm (1.000 nm)?", ["Divido el largo disponible entre el tamaño de uno.", "1.000 ÷ 100 = 10."], "10 virus"),
      ("Comparar dos tamaños", "Una bacteria mide 3 µm y una levadura 9 µm. ¿Cuántas veces más larga es la levadura?", ["Las unidades ya son iguales (µm).", "9 ÷ 3 = 3."], "3 veces más larga"),
  ],
  mistakes=[
      ("Comparar 100 nm con 2 µm sin convertir.", "Son unidades distintas y el número engaña.", "Convierte: 2 µm = 2.000 nm."),
      ("Decir que un virus es una célula.", "Tiene material genético y cápside, pero no es una célula.", "Recuerda que no tiene citoplasma ni núcleo."),
  ],
  rec=[
      ("¿Cuál es más pequeño: un virus o una bacteria?", "Un virus", "Mide cerca de 100 nm frente a unos 2 µm."),
      ("¿Tienen núcleo las bacterias: sí o no?", "No", "Son células procariontes sin núcleo."),
      ("¿Qué grupo tiene pared de quitina: los hongos o las bacterias?", "Los hongos", "La quitina es propia de la pared de los hongos."),
  ],
  und=[
      ("Un microorganismo tiene material genético dentro de una cápside y no es una célula. ¿Es un virus, una bacteria o un hongo?", "Un virus", "La cápside y la ausencia de célula son rasgos de los virus."),
      ("¿Qué significa que una célula sea eucarionte? A) Tiene núcleo; B) Tiene cápside.", "A", "El núcleo guarda el material genético."),
      ("¿Por qué no se ve un virus con un microscopio óptico común? A) Porque es demasiado pequeño; B) Porque es transparente por dentro.", "A", "Mide cerca de 100 nm, menos de lo que resuelve ese microscopio."),
  ],
  app=[
      arith("Una bacteria mide 2 µm. ¿Cuántas bacterias en fila caben en 1 mm (1.000 µm)?", "1000//2", "Se divide el largo disponible entre el de una."),
      arith("Una levadura mide 8 µm y una bacteria 2 µm. ¿Cuántas bacterias en fila miden lo mismo que una levadura?", "8//2", "Se divide un largo entre otro."),
      arith("Un virus mide 100 nm y una bacteria 2 µm. ¿Cuántas veces más larga es la bacteria? (Recuerda: 2 µm = 2.000 nm.)", "2000//100", "Se divide 2.000 nm entre 100 nm."),
  ],
  rea=[
      ("Un esquema dibuja un virus del mismo tamaño que una bacteria. Explica en una frase el error.", "El virus es unas 20 veces más pequeño que la bacteria", "El esquema no respeta la escala."),
      ("Alguien dice: «Todos los hongos son más pequeños que las bacterias». Usa las medidas de la clase para corregirlo.", "Una levadura mide 5 a 10 µm, más que una bacteria de 2 µm", "El dato contradice la generalización."),
  ],
  cha=[
      ("Tres microorganismos de ejemplo: X mide 90 nm y no es célula; Y mide 8 µm, tiene núcleo y pared de quitina; Z mide 3 µm y no tiene núcleo. ¿Cuál es el hongo?", "Y", "Tiene núcleo y quitina, rasgos de los hongos."),
      ("Con los mismos tres microorganismos (X de 90 nm sin célula, Y de 8 µm con núcleo, Z de 3 µm sin núcleo), ¿cuál es la bacteria?", "Z", "Es una célula sin núcleo de tamaño de micrómetros."),
  ],
  context=[("Dato de ejemplo. Una gota de agua contiene 400 bacterias de 2 µm; otra contiene 650. ¿Cuántas bacterias más hay en la segunda gota?", "250", "650 − 400 = 250.")],
  selfcheck=[("¿Cuántos µm tiene 1 mm?", "1.000", "Cada micrómetro es la milésima parte de un milímetro."), ("¿Qué estructura diferencia a un virus de una bacteria?", "El virus no es una célula y tiene cápside", "La bacteria es una célula procarionte."), ("¿Qué grupo tiene núcleo?", "Los hongos", "Los hongos son células eucariontes.")],
  open_task=task("Dibuja a escala una fila de 1 µm dividida en 10 espacios iguales: en cada espacio dibuja un virus (100 nm). Al lado, dibuja una barra que represente una bacteria de 2 µm y escribe cuántos virus caben en su largo.", "Fila de 10 virus en 1 µm; la bacteria mide 20 virus de largo. Respuesta: caben 20 virus en la bacteria.", ["fila de 10 espacios", "bacteria con el doble de largo de la fila", "respuesta de 20 virus"], ["dibujo y una frase"], ["dibujar el virus del tamaño de la bacteria", "no convertir unidades"], "Pregunta qué cambiaría si el virus midiera 200 nm."),
  reinforce="Escribe en orden de menor a mayor: bacteria de 2 µm, virus de 100 nm, levadura de 8 µm.",
  extend="Explica por qué se necesita otro tipo de microscopio para ver virus.")

L(OA5, 2,
  materials="Este cuaderno y lápiz. Los datos de crecimiento están escritos en cada ejercicio.",
  use="Aprenderé cómo se reproducen los virus, las bacterias y los hongos. Sirve para entender por qué una infección puede crecer rápido y por qué se controla de formas distintas.",
  prior=["Sé que los virus no son células.", "Sé comparar tamaños de microorganismos."],
  explain=[
      "Los virus no se reproducen solos. Entran en una célula huésped y usan sus materiales para fabricar copias de sí mismos. Al final, la célula puede romperse y liberar muchos virus nuevos. Esto se llama replicación. Por eso los antibióticos, que actúan contra bacterias, no sirven contra los virus.",
      "Las bacterias se reproducen por fisión binaria: copian su material genético y se dividen en dos células iguales. En condiciones ideales, E. coli puede dividirse cada 20 minutos. El número se duplica en cada división: 1, 2, 4, 8, 16… En la realidad el crecimiento se frena cuando faltan alimento y espacio.",
      "Los hongos se reproducen principalmente por esporas, células pequeñas y resistentes que viajan por el aire y germinan donde hay humedad y alimento. Las levaduras, además, pueden hacerlo por gemación: forman un brote que crece y se separa. Una espora o un brote origina un nuevo hongo.",
  ],
  vocab=[("replicación", "fabricación de copias de un virus dentro de una célula huésped"), ("fisión binaria", "división de una bacteria en dos células iguales"), ("espora", "célula pequeña y resistente de los hongos"), ("gemación", "formación de un brote que se separa de una levadura"), ("célula huésped", "célula en que se multiplica un virus")],
  worked=[
      ("Duplicaciones de una bacteria", "Una bacteria se divide cada 20 minutos. ¿Cuántas hay después de 1 hora, partiendo de 1?", ["1 hora son 3 divisiones de 20 minutos.", "1 → 2 → 4 → 8."], "8 bacterias"),
      ("Replicación de virus", "Un virus infecta una célula y esta libera 50 virus nuevos (dato de ejemplo). ¿Cuántos se liberan si se infectan 4 células?", ["Cada célula libera 50.", "4 × 50 = 200."], "200 virus"),
  ],
  mistakes=[
      ("Creer que los virus se dividen como las bacterias.", "No pueden hacerlo solos; necesitan una célula huésped.", "Recuerda: replicación dentro de una célula."),
      ("Pensar que las bacterias crecen sin límite.", "Se acaban el alimento y el espacio.", "El crecimiento ideal es solo un modelo."),
  ],
  rec=[
      ("¿Un virus se reproduce solo, sin una célula huésped: sí o no?", "No", "Necesita una célula huésped."),
      ("¿Cómo se llama la división de una bacteria en dos: fisión binaria o gemación?", "Fisión binaria", "La gemación es de las levaduras."),
      ("¿Con qué se reproducen principalmente los hongos: con esporas o con cápsides?", "Con esporas", "Las esporas viajan por el aire."),
  ],
  und=[
      ("¿Qué le pasa a una célula huésped cuando los virus nuevos se liberan? A) Puede romperse; B) Se transforma en bacteria.", "A", "Muchos virus salen y la dañan."),
      ("En la fisión binaria, ¿cuántas células hay después de una división si se parte de 1?", "2", "Una célula se divide en dos."),
      ("¿Qué es la gemación? A) Un brote que se separa de una levadura; B) La liberación de virus.", "A", "Es una forma de reproducción de las levaduras."),
  ],
  app=[
      arith("Una bacteria se divide cada 20 minutos y se parte de 1. ¿Cuántas hay después de 2 horas (6 divisiones)?", "2*2*2*2*2*2", "Se duplica seis veces."),
      arith("Cada célula infectada libera 80 virus (dato de ejemplo). ¿Cuántos virus se liberan si se infectan 5 células?", "5*80", "Se multiplica."),
      arith("Dato de ejemplo: una levadura forma un brote cada 90 minutos. ¿Cuántos brotes forma en 6 horas (360 minutos)?", "360//90", "Se divide el tiempo entre el intervalo."),
  ],
  rea=[
      ("¿Por qué un antibiótico no sirve contra la gripe? Responde en una frase.", "Porque la gripe es causada por un virus, no por una bacteria", "Los antibióticos actúan sobre bacterias."),
      ("En el modelo de duplicación cada 20 minutos aparecen miles de bacterias en pocas horas. ¿Por qué en la vida real no ocurre siempre así?", "Porque se acaban el alimento y el espacio", "El modelo supone condiciones ideales."),
  ],
  cha=[
      ("Una bacteria se divide cada 30 minutos. Si se parte de 3 bacterias, ¿cuántas hay después de 2 horas (4 divisiones)?", "48", "3 × 2 × 2 × 2 × 2 = 48."),
      ("Un hongo libera 1.000 esporas y solo germina el 2 %. ¿Cuántas esporas germinan?", "20", "2 % de 1.000 es 20."),
  ],
  context=[("Dato de ejemplo. Un cultivo comienza con 5 bacterias y después de una hora hay 40. ¿Cuántas veces se duplicó el número de bacterias?", "3", "5 → 10 → 20 → 40 son 3 duplicaciones.")],
  selfcheck=[("¿Cómo se reproduce un virus?", "Dentro de una célula huésped, fabricando copias", "No lo hace solo."), ("¿Cómo se reproducen las bacterias?", "Por fisión binaria", "Se dividen en dos."), ("¿Qué son las esporas?", "Células pequeñas y resistentes de los hongos", "Viajan por el aire y germinan.")],
  open_task=task("Completa una tabla de tres filas (virus, bacteria, hongo) con tres columnas: cómo se reproduce, un dato numérico del modelo y una condición necesaria. Usa estos datos de ejemplo: virus, 60 copias por célula; bacteria, división cada 20 minutos; hongo, esporas con humedad.", "Virus: replicación en célula huésped, 60 copias, necesita célula. Bacteria: fisión binaria, 8 en 1 hora, necesita alimento. Hongo: esporas, miles, necesita humedad.", ["tabla completa", "dato numérico en el modelo", "condición en cada fila"], ["tabla de 3 filas"], ["decir que los virus se dividen solos", "olvidar la condición"], "Pregunta qué frenaría el crecimiento en cada caso."),
  reinforce="Escribe cómo se reproduce cada grupo con una palabra clave.",
  extend="Explica por qué la replicación de los virus daña a la célula huésped.")

L(OA5, 3,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo. No necesitas hacer crecer moho: no abras bolsas con pan mohoso ni huelas alimentos en mal estado.",
  use="Aprenderé qué características de los seres vivos tienen virus, bacterias y hongos y de qué condiciones dependen. Sirve para entender por qué se conservan alimentos con frío y sequedad.",
  prior=["Sé que los seres vivos se nutren, respiran, crecen y se reproducen.", "Sé cómo se reproducen virus, bacterias y hongos."],
  explain=[
      "Los seres vivos obtienen alimento, obtienen energía, crecen, responden al ambiente y se reproducen. Las bacterias cumplen todo esto en una sola célula. Algunas se alimentan de materia orgánica y otras la fabrican, como las cianobacterias, que hacen fotosíntesis. Algunas necesitan oxígeno para respirar y otras viven sin él.",
      "Los hongos no fabrican su alimento. Absorben nutrientes de materia orgánica viva o muerta. Por eso son descomponedores del suelo y también pueden crecer en el pan o en la ropa húmeda. Necesitan humedad, materia orgánica y una temperatura moderada. La luz les importa poco.",
      "Los virus no se alimentan, no respiran y no crecen por sí solos. Solo se reproducen dentro de una célula huésped, de la que dependen por completo. Por eso se discute si son seres vivos. Las condiciones que alteran la vida de los microorganismos son la humedad, la temperatura, el alimento y el oxígeno: guardar alimentos en frío o secos frena su crecimiento.",
  ],
  vocab=[("heterótrofo", "ser que obtiene su alimento de otros seres o de materia orgánica"), ("descomponedor", "ser que obtiene nutrientes de restos de seres vivos"), ("cianobacteria", "bacteria que hace fotosíntesis"), ("dependencia", "necesidad de algo para sobrevivir o reproducirse"), ("condición ambiental", "factor del ambiente como humedad o temperatura")],
  worked=[
      ("Qué condición favorece", "Datos de ejemplo: a los 7 días el pan tibio y húmedo tenía 40 cm² de moho, el pan seco 0 cm² y el pan húmedo en un refrigerador 5 cm². ¿Qué condiciones favorecen más a los hongos?", ["Comparo los valores: 40, 0 y 5.", "El mayor valor es en pan tibio y húmedo.", "Con frío o sin humedad crece menos o nada."], "La humedad y una temperatura moderada o tibia"),
      ("Dependencia", "¿Cuál de estos no puede reproducirse sin una célula huésped: un virus, una bacteria o un hongo?", ["Las bacterias y los hongos son células.", "El virus no lo es."], "El virus"),
  ],
  mistakes=[
      ("Decir que los hongos hacen fotosíntesis como las plantas.", "Absorben nutrientes de materia orgánica.", "Son heterótrofos y absorben nutrientes."),
      ("Creer que todas las bacterias necesitan oxígeno.", "Hay bacterias que viven sin oxígeno.", "Distingue entre las que sí y las que no."),
  ],
  rec=[
      ("¿Los hongos fabrican su alimento o lo absorben?", "Lo absorben", "Son heterótrofos y absorben nutrientes."),
      ("¿Una bacteria que hace fotosíntesis se llama cianobacteria o levadura?", "Cianobacteria", "Es una bacteria con clorofila."),
      ("¿Un virus depende de una célula huésped: sí o no?", "Sí", "No se reproduce solo."),
  ],
  und=[
      ("¿Por qué los hongos crecen en el pan húmedo? A) Porque encuentran humedad y materia orgánica; B) Porque necesitan luz fuerte.", "A", "El pan es materia orgánica y la humedad la favorece."),
      ("¿Qué hace que se discuta si los virus son seres vivos? A) No se alimentan ni se reproducen solos; B) Son muy grandes.", "A", "Dependen de una célula."),
      ("¿Qué organismos descomponen los restos de hojas en el suelo? A) Descomponedores como hongos y bacterias; B) Cianobacterias que hacen fotosíntesis.", "A", "Absorben nutrientes de la materia orgánica muerta."),
  ],
  app=[
      ("Datos de ejemplo de 5 días: leche a 5 °C, 4 bacterias por gota; leche a 25 °C, 400 bacterias por gota. ¿Cuántas veces más bacterias hay a 25 °C?", "100", "400 ÷ 4 = 100."),
      ("Una persona guarda fruta seca en un frasco cerrado. ¿Qué condición evita el crecimiento de hongos? A) La sequedad; B) La oscuridad.", "A", "Sin humedad los hongos no crecen."),
      ("Tres organismos: cianobacteria (fotosíntesis), moho (absorbe), virus (necesita célula). ¿Cuántos fabrican su propio alimento?", "1", "Solo la cianobacteria."),
  ],
  rea=[
      ("Un alimento se guarda a 4 °C. ¿Por qué dura más? Responde en una frase.", "Porque el frío frena el crecimiento de bacterias y hongos", "Con baja temperatura se dividen más lento."),
      ("Un compañero dice: «Los virus respiran como las bacterias». Corrígelo.", "Los virus no respiran; dependen de la célula huésped", "No tienen metabolismo propio."),
  ],
  cha=[
      ("Datos de ejemplo: pan A en bolsa cerrada y húmedo, 30 cm² de moho; pan B igual pero seco, 0 cm²; pan C húmedo en refrigerador, 6 cm². ¿Qué conclusión está apoyada? A) La humedad es necesaria para que crezca el moho; B) La luz es necesaria para el moho.", "A", "Con pan seco no hay moho; la luz no se midió."),
      ("¿Qué limitación tiene concluir con un solo pan de cada tipo?", "Que un caso por condición no garantiza el resultado", "Habría que repetir."),
  ],
  context=[("Dato de ejemplo. En un frasco con fruta hay 12 manchas de moho a los 4 días y 30 a los 8 días. ¿Cuántas manchas más hay a los 8 días?", "18", "30 − 12 = 18.")],
  selfcheck=[("¿Cómo obtienen alimento los hongos?", "Absorben nutrientes de materia orgánica", "Son heterótrofos y absorben nutrientes."), ("¿Por qué se discute si los virus son seres vivos?", "Porque no se alimentan ni se reproducen solos", "Dependen de una célula."), ("¿Qué condiciones frenan a bacterias y hongos?", "Frío y sequedad", "Reducen su crecimiento.")],
  open_task=task("Tienes tres alimentos inventados: pan húmedo en la mesa, galletas secas en un frasco y yogurt en el refrigerador. Ordénalos del que más rápido se llena de microorganismos al que menos, y justifica con la humedad, la temperatura y los nutrientes.", "Pan húmedo (humedad y tibio), yogurt (nutrientes pero frío), galletas secas (sin humedad). Justificación según las condiciones.", ["orden razonado", "usa humedad y temperatura", "justifica con la clase"], ["orden y tres frases"], ["no justificar", "decir que la luz es la causa"], "Pregunta cómo cambiaría el orden si el yogurt quedara fuera del refrigerador."),
  reinforce="Escribe dos condiciones que frenan el crecimiento de hongos.",
  extend="Explica por qué las bacterias y los hongos son importantes como descomponedores.")

L(OA5, 4,
  materials="Este cuaderno y lápiz. Nunca pruebes hongos silvestres: algunos son tóxicos.",
  use="Aprenderé que los microorganismos tienen efectos positivos y negativos para la salud. Sirve para cuidarme sin creer que todos los microbios son dañinos.",
  prior=["Sé cómo viven virus, bacterias y hongos.", "Sé que algunas bacterias forman la flora normal."],
  explain=[
      "Muchos microorganismos son beneficiosos. La flora intestinal, formada por bacterias, ayuda a digerir y compite con las dañinas. Las bacterias lácticas hacen yogurt y la levadura hace subir el pan. El hongo Penicillium produce penicilina, el primer antibiótico, que descubrió Alexander Fleming en 1928.",
      "Otros causan enfermedades. Los virus producen gripe y resfrío. Algunas bacterias causan intoxicaciones por alimentos, como Salmonella, o faringitis por estreptococo. Hay hongos que producen infecciones en la piel, como el pie de atleta. Estos microorganismos son patógenos.",
      "Para cuidarnos: lavarse las manos, cocer bien los alimentos, vacunarse y tomar antibióticos solo si un profesional de salud los indica. Los antibióticos actúan contra bacterias, no contra virus, y usarlos mal ayuda a que las bacterias se vuelvan resistentes.",
  ],
  vocab=[("beneficioso", "que ayuda a la salud o a producir algo útil"), ("patógeno", "microorganismo que causa enfermedad"), ("antibiótico", "medicamento contra bacterias"), ("resistencia", "capacidad de una bacteria de sobrevivir a un antibiótico"), ("intoxicación alimentaria", "enfermedad por comer alimentos contaminados")],
  worked=[
      ("Beneficioso o perjudicial", "Clasifica: (1) levadura del pan, (2) virus de la gripe, (3) flora intestinal.", ["La levadura ayuda a hacer pan.", "El virus de la gripe causa enfermedad.", "La flora ayuda a digerir."], "1 beneficioso; 2 perjudicial; 3 beneficioso"),
      ("Antibiótico y gripe", "Una persona con gripe pide antibióticos. ¿Sirven?", ["La gripe la causa un virus.", "Los antibióticos actúan contra bacterias."], "No sirven contra la gripe"),
  ],
  mistakes=[
      ("Creer que todos los microbios son dañinos.", "Muchos son útiles para la salud o los alimentos.", "Distingue beneficiosos y patógenos."),
      ("Dejar un antibiótico a la mitad cuando uno se siente mejor.", "Las bacterias sobrevivientes pueden volverse resistentes.", "Sigue la indicación del profesional."),
  ],
  rec=[
      ("¿Qué microorganismo hace subir el pan: la levadura o el estreptococo?", "La levadura", "Hace subir la masa del pan."),
      ("¿La gripe la causa una bacteria o un virus?", "Un virus", "Por eso los antibióticos no la curan."),
      ("¿La flora intestinal es beneficiosa o perjudicial?", "Beneficiosa", "Ayuda a digerir y a protegerse."),
  ],
  und=[
      ("¿Quién descubrió la penicilina y de qué hongo se obtiene? A) Alexander Fleming, del hongo Penicillium; B) Louis Pasteur, de una levadura.", "A", "La penicilina viene de Penicillium."),
      ("¿Por qué es un problema usar mal los antibióticos? A) Puede volver resistentes a las bacterias; B) Hace desaparecer a los virus.", "A", "Las bacterias que sobreviven se multiplican."),
      ("¿Cuál es una forma de prevenir una intoxicación alimentaria? A) Cocer bien los alimentos; B) Dejar los alimentos varias horas fuera del refrigerador.", "A", "La cocción destruye muchos patógenos."),
  ],
  app=[
      ("Cinco microorganismos: levadura, Salmonella, bacteria láctica, hongo del pie de atleta, virus del resfrío. ¿Cuántos son perjudiciales?", "3", "Son Salmonella, el hongo del pie de atleta y el virus del resfrío."),
      arith("Un curso de 40 estudiantes: 12 faltaron por gripe y 5 por intoxicación alimentaria. ¿Cuántos faltaron en total por esas dos causas?", "12+5", "Se suman."),
      ("Un estudiante se lava las manos antes de comer. ¿Qué microbios reduce? A) Patógenos que podrían ingresar; B) Todos, incluida la flora intestinal.", "A", "El lavado reduce los de las manos; la flora está dentro del intestino."),
  ],
  rea=[
      ("Explica por qué tomar un antibiótico para la gripe puede ser un error doble.", "No sirve contra virus y puede favorecer bacterias resistentes", "Es un uso incorrecto."),
      ("¿Por qué la flora intestinal protege? Responde en una frase.", "Porque compite con bacterias dañinas", "Ocupa el espacio y los nutrientes."),
  ],
  cha=[
      ("Afirmación 1: «Todos los hongos son dañinos». Afirmación 2: «Algunos hongos producen medicamentos». ¿Cuál afirmación contradice el caso de la penicilina? Escribe 1 o 2.", "1", "La penicilina viene de un hongo útil, así que no todos son dañinos."),
      ("Un niño dice: «Mis manos están limpias si se ven limpias». ¿Qué error comete?", "Los microorganismos no se ven a simple vista", "Los microorganismos son microscópicos."),
  ],
  context=[("Dato de ejemplo. En un mes, un consultorio atendió 90 casos infecciosos: 60 virales y el resto bacterianos. ¿Cuántos fueron bacterianos?", "30", "90 − 60 = 30.")],
  selfcheck=[("¿Cuál es un efecto beneficioso de las bacterias?", "Producir yogurt o ayudar a digerir", "Son usos reales."), ("¿Sirve un antibiótico contra un virus?", "No", "Actúa sobre bacterias."), ("¿Por qué no se deben comer hongos silvestres?", "Porque algunos son tóxicos", "No se distinguen a simple vista.")],
  open_task=task("Haz una tabla de dos columnas: «Efectos beneficiosos» y «Efectos perjudiciales». Escribe al menos tres ejemplos en cada columna usando microorganismos de la clase y una medida de cuidado para uno de los perjudiciales.", "Beneficiosos: levadura, flora intestinal, Penicillium. Perjudiciales: virus de la gripe, Salmonella, hongo del pie de atleta. Cuidado: lavar las manos.", ["tres por columna", "ejemplos correctos", "una medida de cuidado"], ["tabla"], ["poner una levadura como perjudicial", "olvidar la medida"], "Pregunta qué microorganismo cambiaría de columna según el contexto."),
  reinforce="Escribe dos microorganismos beneficiosos y dos perjudiciales.",
  extend="Explica por qué es importante terminar un tratamiento con antibióticos indicado por un profesional.")

L(OA5, 5,
  materials="Este cuaderno y lápiz. Los microorganismos de los ejercicios son inventados y solo usan los rasgos de la clase.",
  use="Aprenderé a construir una tabla comparativa de virus, bacterias y hongos y a declarar sus límites. Sirve para resumir con evidencia sin exagerar.",
  prior=["Sé comparar estructura, reproducción y efectos de estos tres grupos.", "Sé que un modelo simplifica."],
  explain=[
      "Una comparación ordenada usa los mismos criterios para todos los grupos. Por ejemplo: tamaño, estructura, reproducción, nutrición y efecto en la salud. En un virus: unos 100 nm, cápside y material genético, replicación en células huésped, no se nutre solo. En una bacteria: unos 2 µm, célula sin núcleo, fisión binaria, se nutre. En un hongo: 5 a 10 µm en levaduras, célula con núcleo, esporas o gemación, absorbe nutrientes.",
      "Para decidir a qué grupo pertenece un organismo se usan rasgos que lo distinguen, como tener núcleo, pared de quitina o cápside. El tamaño solo no basta, porque los tamaños de hongos y bacterias se traslapan.",
      "Toda tabla tiene límites. Resume lo común y deja afuera excepciones, como las bacterias que hacen fotosíntesis o los hongos de gran tamaño. Una conclusión debe decir qué criterio usó y que hay excepciones.",
  ],
  vocab=[("criterio", "regla usada para comparar"), ("rasgo distintivo", "característica que permite distinguir un grupo de otro"), ("traslape", "zona en que dos rangos de tamaño coinciden"), ("excepción", "caso que no cumple la regla general"), ("síntesis", "resumen de lo más importante")],
  worked=[
      ("Clasificar por un rasgo", "Un microorganismo mide 6 µm, tiene núcleo y pared de quitina, y forma brotes. ¿A qué grupo pertenece?", ["El núcleo lo distingue de las bacterias.", "La quitina y los brotes indican hongo."], "Hongo (una levadura)"),
      ("Por qué no basta el tamaño", "Un microorganismo mide 5 µm. ¿Es bacteria o hongo?", ["Una bacteria mide entre 1 y 5 µm.", "Una levadura mide entre 5 y 10 µm.", "5 µm está en los dos rangos; falta saber si tiene núcleo."], "No se puede asegurar solo con el tamaño"),
  ],
  mistakes=[
      ("Clasificar solo por el tamaño.", "Los rangos de tamaño se traslapan.", "Usa un rasgo estructural, como el núcleo."),
      ("Decir que la tabla describe a todos los casos.", "Hay excepciones.", "Declara los límites."),
  ],
  rec=[
      ("¿Qué rasgo distingue a un virus de los otros dos grupos: la cápside o el núcleo?", "La cápside", "Es la cubierta de proteínas del virus."),
      ("¿Qué grupo tiene células con núcleo: bacterias u hongos?", "Hongos", "Los hongos son células eucariontes."),
      ("¿Una tabla comparativa tiene límites: sí o no?", "Sí", "Resume y deja excepciones."),
  ],
  und=[
      ("Un microorganismo no es una célula y se multiplica dentro de otra. ¿Qué grupo es? A) Virus; B) Bacteria.", "A", "Una bacteria sí es una célula."),
      ("¿Por qué el tamaño no basta para clasificar? A) Porque los rangos se traslapan; B) Porque las medidas no importan.", "A", "Una levadura de 5 µm y una bacteria de 5 µm podrían coincidir."),
      ("Una cianobacteria hace fotosíntesis. ¿Es una excepción a «las bacterias se alimentan de materia orgánica»?", "Sí", "No se ajusta a la regla general."),
  ],
  app=[
      ("Cinco microorganismos inventados: P (100 nm, sin célula), Q (2 µm, sin núcleo, se divide en dos), R (6 µm, con núcleo, forma brotes), S (80 nm, sin célula), T (3 µm, sin núcleo, se divide en dos). ¿Cuántos son virus?", "2", "Son P y S."),
      ("Con los mismos cinco microorganismos (P: 100 nm, sin célula; Q: 2 µm, sin núcleo, se divide en dos; R: 6 µm, con núcleo, forma brotes; S: 80 nm, sin célula; T: 3 µm, sin núcleo, se divide en dos), ¿cuántos son bacterias?", "2", "Son Q y T: células sin núcleo que se dividen en dos."),
      ("Con los mismos cinco microorganismos (P: 100 nm, sin célula; Q: 2 µm, sin núcleo; R: 6 µm, con núcleo, forma brotes; S: 80 nm, sin célula; T: 3 µm, sin núcleo), ¿cuál es el hongo? Escribe la letra.", "R", "Es el único con núcleo y brotes."),
  ],
  rea=[
      ("En una tabla se afirma: «Los hongos se reproducen por esporas». ¿Qué excepción habría que declarar?", "Las levaduras también se reproducen por gemación", "No todos los hongos usan esporas."),
      ("Dos estudiantes clasifican un microorganismo de 4 µm sin núcleo. Uno dice hongo y otro bacteria. ¿Quién tiene razón?", "La bacteria", "Los hongos tienen núcleo."),
  ],
  cha=[
      ("Redacta una conclusión con límite para una tabla que compara virus, bacterias y hongos, de máximo dos frases.", "Los tres grupos se distinguen por estructura y reproducción, pero la tabla no incluye excepciones como las bacterias fotosintéticas", "Declara criterio y límite."),
      ("Un compañero propone usar solo el color para clasificar. ¿Por qué es mala idea?", "Porque el color no indica estructura ni grupo", "No es un rasgo distintivo."),
  ],
  context=[("Dato de ejemplo. Un laboratorio clasificó 50 muestras: 18 eran virus, 20 bacterias y el resto hongos. ¿Cuántas eran hongos?", "12", "50 − 18 − 20 = 12.")],
  selfcheck=[("¿Qué rasgo distingue a un virus?", "No ser una célula y tener cápside", "Los otros dos son células."), ("¿Por qué conviene un criterio común en una tabla?", "Para comparar de forma justa", "Se aplica el mismo criterio a todos."), ("¿Qué límite tiene la tabla?", "Resume y deja excepciones", "Hay casos que no encajan.")],
  open_task=task("Construye una tabla con tres columnas (virus, bacterias, hongos) y cuatro filas (tamaño, estructura, reproducción, efecto en la salud). Escribe debajo una conclusión con un límite.", "Virus: 100 nm, cápside, replicación, causa gripe. Bacterias: 2 µm, sin núcleo, fisión binaria, flora o infecciones. Hongos: 5 a 10 µm, núcleo, esporas o gemación, pan o pie de atleta. Conclusión con límite: hay excepciones.", ["tabla completa", "datos correctos", "límite declarado"], ["tabla y una frase"], ["clasificar solo por tamaño", "no declarar excepciones"], "Pregunta qué fila es la más segura para distinguir."),
  reinforce="Escribe dos rasgos que distinguen a los virus de las bacterias.",
  extend="Explica por qué una tabla comparativa no puede incluirlo todo.")

# ---------------------------------------------------------------- OA 06
L(OA6, 1,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo. Los productos con alcohol (vino, cerveza) son solo para personas adultas.",
  use="Aprenderé cómo bacterias y hongos se usan para producir alimentos como pan, yogurt y vinagre. Sirve para entender qué es la fermentación.",
  prior=["Sé que algunos microorganismos son beneficiosos.", "Sé que las levaduras son hongos de una célula."],
  explain=[
      "La biotecnología es el uso de seres vivos o de sus procesos para obtener productos o resolver problemas. En los alimentos se usa la fermentación, un proceso en que los microorganismos transforman azúcares y liberan nuevas sustancias, en muchos casos con poco o nada de oxígeno.",
      "Las levaduras fermentan el azúcar y producen dióxido de carbono y alcohol. El gas forma burbujas que hacen subir la masa del pan; al hornear, el alcohol se evapora. Las bacterias lácticas fermentan la lactosa, el azúcar de la leche, y producen ácido láctico, que espesa la leche y forma yogurt y queso. Las bacterias acéticas transforman el alcohol en ácido acético, y se obtiene vinagre; estas bacterias sí necesitan oxígeno y un ambiente tibio.",
      "Cada proceso necesita condiciones. La levadura trabaja mejor con calor suave, unos 25 a 35 °C; con mucho calor muere y con frío casi no trabaja. Las bacterias del yogurt prefieren cerca de 40 °C. Cuando la fermentación termina, el producto se enfría y se guarda.",
  ],
  vocab=[("biotecnología", "uso de seres vivos o sus procesos para obtener productos"), ("fermentación", "transformación de azúcares por microorganismos"), ("lactosa", "azúcar de la leche"), ("ácido láctico", "sustancia que espesa la leche en el yogurt"), ("dióxido de carbono", "gas que forma burbujas en la masa del pan")],
  worked=[
      ("Por qué sube el pan", "¿Qué gas hace subir la masa del pan y quién lo produce?", ["La levadura fermenta el azúcar.", "Libera dióxido de carbono.", "El gas queda atrapado en la masa."], "El dióxido de carbono, producido por la levadura"),
      ("Yogurt", "¿Qué transforman las bacterias lácticas y qué producen en el yogurt?", ["Fermentan la lactosa.", "Producen ácido láctico."], "Fermentan la lactosa y producen ácido láctico"),
  ],
  mistakes=[
      ("Pensar que el pan sube porque se calienta el aire.", "Sube por el gas que produce la levadura.", "Revisa la fermentación."),
      ("Creer que el yogurt se hace con levadura.", "Lo hacen bacterias lácticas.", "Distingue levaduras y bacterias."),
  ],
  rec=[
      ("¿Qué microorganismo hace subir el pan: la levadura o una bacteria láctica?", "La levadura", "Produce dióxido de carbono."),
      ("¿Qué azúcar fermentan las bacterias lácticas: la lactosa o la sacarosa?", "La lactosa", "Es el azúcar de la leche."),
      ("¿La fermentación transforma azúcares: verdadero o falso?", "Verdadero", "Es su definición."),
  ],
  und=[
      ("¿Qué producto se obtiene cuando las bacterias acéticas transforman el alcohol? A) Vinagre; B) Pan.", "A", "Producen ácido acético."),
      ("¿Por qué el pan queda esponjoso? A) Por el gas atrapado en la masa; B) Por el alcohol de la masa.", "A", "El alcohol se evapora al hornear."),
      ("Si la masa se calienta a 70 °C antes de hornear, ¿qué ocurre con la levadura? ¿Muere o se multiplica?", "Muere", "Con mucho calor deja de vivir."),
  ],
  app=[
      ("Datos de ejemplo: una masa de pan mide 4 cm de alto al inicio, 6 cm a la 1 h y 9 cm a las 2 h. ¿Cuántos centímetros subió en la segunda hora?", "3", "9 − 6 = 3 cm."),
      ("Con la misma masa (4 cm al inicio y 9 cm a las 2 horas), ¿cuántos centímetros subió en total?", "5", "9 − 4 = 5 cm."),
      arith("Un yogurt comienza a fermentar a las 8 h y necesita 7 horas. ¿A qué hora (formato 24 h) está listo?", "8+7", "Se suman las horas."),
  ],
  rea=[
      ("Una persona deja leche con fermento en el refrigerador a 5 °C y no se espesa. Explica por qué.", "Porque el frío frena a las bacterias", "Las bacterias del yogurt prefieren unos 40 °C."),
      ("¿Por qué una masa sin azúcar no sube aunque tenga levadura viva?", "Porque la levadura necesita azúcar para fermentar", "Sin alimento no produce gas."),
  ],
  cha=[
      ("Tres masas con levadura: a 5 °C sube 1 cm, a 30 °C sube 6 cm, a 70 °C sube 0 cm. ¿A qué temperatura trabaja mejor la levadura?", "30 °C", "Tiene el mayor aumento."),
      ("Explica con tus palabras por qué el yogurt y el pan son ejemplos de biotecnología.", "Porque se obtienen usando microorganismos y su fermentación", "Son procesos con seres vivos."),
  ],
  context=[("Dato de ejemplo. Un taller prepara 6 jarros de yogurt de 250 mL cada uno. ¿Cuántos mililitros hay en total?", "1.500", "6 × 250 = 1.500 mL.")],
  selfcheck=[("¿Qué es la biotecnología?", "El uso de seres vivos o sus procesos para obtener productos", "Incluye alimentos y medicamentos."), ("¿Qué produce la levadura en la masa?", "Dióxido de carbono", "Hace subir el pan."), ("¿Qué producen las bacterias lácticas?", "Ácido láctico", "Espesa la leche.")],
  open_task=task("Completa una tabla con tres alimentos inventados para una feria escolar: pan, yogurt y vinagre. Indica en cada uno qué microorganismo actúa, qué transforma y qué temperatura aproximada necesita.", "Pan: levadura, azúcar, 25 a 35 °C. Yogurt: bacterias lácticas, lactosa, unos 40 °C. Vinagre: bacterias acéticas, alcohol, ambiente tibio.", ["tres filas", "microorganismo correcto", "sustancia transformada"], ["tabla"], ["decir que el yogurt se hace con levadura", "olvidar la temperatura"], "Pregunta qué pasa si la temperatura es demasiado alta."),
  reinforce="Escribe qué producen las levaduras y las bacterias lácticas.",
  extend="Explica por qué un alimento fermentado se enfría al terminar el proceso.")

L(OA6, 2,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo.",
  use="Aprenderé cómo hongos y bacterias ayudan a limpiar el ambiente y a reciclar residuos. Sirve para entender el tratamiento de aguas, los derrames y el compostaje.",
  prior=["Sé que los descomponedores obtienen nutrientes de materia orgánica.", "Sé qué es la biotecnología."],
  explain=[
      "La biorremediación es el uso de microorganismos para limpiar sitios contaminados. Por ejemplo, algunas bacterias degradan el petróleo de un derrame y lo transforman en sustancias menos dañinas. Su eficacia depende de la temperatura, la humedad, el oxígeno y los nutrientes.",
      "En las plantas de tratamiento de aguas servidas, bacterias descomponen la materia orgánica que contiene el agua. Así, el agua sale menos contaminada. En el compostaje, hongos y bacterias descomponen restos de frutas, verduras y hojas y los convierten en compost, un abono. Para funcionar necesitan oxígeno, humedad moderada y una mezcla de restos húmedos y secos.",
      "Los microorganismos tienen límites. No degradan bien todos los contaminantes: metales pesados, como el plomo, no desaparecen. Además, el proceso puede ser lento, y su eficacia cambia con el clima.",
  ],
  vocab=[("biorremediación", "uso de microorganismos para limpiar sitios contaminados"), ("compost", "abono que se obtiene de restos orgánicos descompuestos"), ("planta de tratamiento", "instalación que limpia aguas servidas"), ("degradar", "descomponer una sustancia en otras más simples"), ("contaminante", "sustancia que daña el ambiente")],
  worked=[
      ("Elegir la aplicación", "Una playa tiene petróleo derramado. ¿Qué técnica con microorganismos podría ayudar?", ["Busco microorganismos que descompongan el petróleo.", "Esa técnica es la biorremediación."], "Biorremediación con bacterias que degradan el petróleo"),
      ("Compost", "Una pila de 100 kg de restos pierde peso mientras se descompone y a los 60 días pesa 45 kg (dato de ejemplo). ¿Cuántos kg se perdieron?", ["Resto el peso final al inicial.", "100 − 45 = 55."], "55 kg"),
  ],
  mistakes=[
      ("Creer que los microorganismos eliminan todos los contaminantes.", "Los metales pesados no se degradan.", "Revisa qué tipo de contaminante es."),
      ("Hacer compost con carne o grasas sin ayuda.", "Atraen animales y malos olores.", "Usa restos de frutas, verduras y hojas."),
  ],
  rec=[
      ("¿Qué hacen los microorganismos en el compostaje: descomponen restos o fabrican plástico?", "Descomponen restos", "Los convierten en abono."),
      ("¿La biorremediación sirve para limpiar contaminación: verdadero o falso?", "Verdadero", "Esa es su finalidad."),
      ("¿Qué obtiene el compostaje: abono o petróleo?", "Abono", "Se llama compost."),
  ],
  und=[
      ("¿Qué hacen las bacterias en una planta de tratamiento de aguas servidas? A) Descomponen la materia orgánica; B) Agregan sal.", "A", "Así baja la contaminación."),
      ("¿Por qué el compost necesita oxígeno? A) Porque los microorganismos que lo descomponen lo usan; B) Porque produce el agua del compost.", "A", "Esos microorganismos respiran oxígeno."),
      ("¿Los metales pesados se degradan fácilmente con microorganismos: sí o no?", "No", "Son un límite de la técnica."),
  ],
  app=[
      arith("Una pila de compost de 80 kg pierde 35 kg en 60 días. ¿Cuántos kg quedan?", "80-35", "Se resta."),
      ("Cuatro residuos: cáscara de manzana, hojas secas, plomo de baterías, pan duro. ¿Cuántos se pueden compostar?", "3", "Son la cáscara, las hojas y el pan; el plomo es un metal pesado."),
      ("Un derrame cubre 600 m² y un tratamiento con bacterias limpia 150 m² por semana. ¿Cuántas semanas tarda?", "4", "600 ÷ 150 = 4."),
  ],
  rea=[
      ("¿Por qué una pila de compost bajo mucha lluvia se descompone peor? Responde en una frase.", "Porque el exceso de agua quita oxígeno a los microorganismos", "Necesitan humedad moderada y oxígeno."),
      ("¿Por qué la biorremediación puede ser lenta en un lugar muy frío?", "Porque el frío frena a los microorganismos", "Trabajan mejor con temperaturas moderadas."),
  ],
  cha=[
      ("Un municipio quiere limpiar un suelo con petróleo y otro con plomo. ¿En cuál es más razonable usar bacterias? A) En el suelo con petróleo; B) En el suelo con plomo.", "A", "Algunas bacterias degradan el petróleo; el plomo no se degrada."),
      ("Explica un límite de las plantas de tratamiento con bacterias.", "No eliminan todos los contaminantes, como los metales pesados", "Dependen del tipo de contaminante."),
  ],
  context=[("Dato de ejemplo. Una comunidad recolecta 25 kg de restos al día durante 8 días para hacer compost. ¿Cuántos kg recolectó en total?", "200", "25 × 8 = 200 kg.")],
  selfcheck=[("¿Qué es la biorremediación?", "El uso de microorganismos para limpiar sitios contaminados", "Ejemplo: degradar petróleo."), ("¿Qué hacen los microorganismos en el compost?", "Descomponen restos orgánicos", "Así se obtiene abono."), ("¿Qué contaminantes no degradan bien?", "Los metales pesados", "Son un límite.")],
  open_task=task("Tienes cuatro problemas inventados: un derrame de petróleo en una playa, restos de cocina de un casino escolar, agua servida de un pueblo y un suelo con plomo. Indica cuáles podrían tratarse con microorganismos, cuál técnica usarías y cuál no, justificando.", "Petróleo: biorremediación. Restos de cocina: compostaje. Agua servida: bacterias de una planta de tratamiento. Plomo: no se degrada con microorganismos.", ["tres tratamientos correctos", "excluye el plomo", "justifica"], ["lista de cuatro respuestas"], ["incluir el plomo", "no justificar"], "Pregunta qué condiciones necesita cada técnica."),
  reinforce="Escribe tres aplicaciones ambientales de microorganismos.",
  extend="Explica por qué las aplicaciones con microorganismos necesitan seguimiento y control.")

L(OA6, 3,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y están en cada ejercicio.",
  use="Aprenderé cómo los microorganismos ayudan a fabricar fármacos, a obtener cobre y a generar biogás con metano. Sirve para entender aplicaciones importantes en Chile y en el mundo.",
  prior=["Sé que la biorremediación usa microorganismos.", "Sé que las bacterias pueden vivir sin oxígeno."],
  explain=[
      "En la producción de fármacos se usan hongos y bacterias. La penicilina viene del hongo Penicillium. La insulina, que necesitan las personas con diabetes, hoy se fabrica con bacterias a las que se les entregó el gen humano de la insulina. Las vacunas y otros medicamentos también se desarrollan con ayuda de microorganismos.",
      "En la minería del cobre se usa la biolixiviación: ciertas bacterias que viven en ambientes ácidos ayudan a disolver el cobre contenido en las rocas, y el cobre disuelto se recupera. Chile es el mayor productor de cobre del mundo, y este método sirve sobre todo para minerales de baja concentración.",
      "El biogás se produce en biodigestores, recipientes cerrados sin oxígeno donde bacterias descomponen residuos orgánicos como restos de alimentos o guano. Producen metano, un gas combustible, y un residuo que sirve de abono. El metano es un gas de efecto invernadero, por lo que debe captarse y no dejarse escapar; además es inflamable, por lo que estos sistemas los construye personal especializado.",
  ],
  vocab=[("biolixiviación", "uso de bacterias para disolver y recuperar cobre de rocas"), ("biodigestor", "recipiente cerrado sin oxígeno donde bacterias producen biogás"), ("biogás", "gas combustible con mucho metano"), ("fármaco", "medicamento"), ("metano", "gas combustible de efecto invernadero")],
  worked=[
      ("Recuperación de cobre", "Una tonelada de roca contiene 5 kg de cobre (dato de ejemplo) y las bacterias ayudan a recuperar el 60 %. ¿Cuántos kg se obtienen?", ["Calculo el 60 % de 5 kg.", "5 × 60 ÷ 100 = 3."], "3 kg"),
      ("Gas del biodigestor", "¿Qué gas combustible producen las bacterias en un biodigestor y en qué condición viven?", ["Descomponen residuos orgánicos.", "Producen metano.", "Viven sin oxígeno."], "Metano; sin oxígeno"),
  ],
  mistakes=[
      ("Pensar que el biogás es un gas inofensivo que no requiere cuidado.", "El metano es inflamable y de efecto invernadero.", "Se capta y se usa con sistemas diseñados por especialistas."),
      ("Creer que las bacterias «fabrican» el cobre.", "Ayudan a disolver el cobre que ya está en la roca.", "Dicen: «disuelven», no «crean»."),
  ],
  rec=[
      ("¿De qué hongo se obtiene la penicilina: Penicillium o la levadura del pan?", "Penicillium", "Es el hongo del antibiótico."),
      ("¿Qué gas combustible se obtiene en un biodigestor: metano u oxígeno?", "Metano", "Lo producen bacterias."),
      ("¿Para qué sirve la biolixiviación: para obtener cobre o para hacer yogurt?", "Para obtener cobre", "Bacterias disuelven el cobre."),
  ],
  und=[
      ("¿Dónde viven las bacterias productoras de metano? A) En ambientes sin oxígeno; B) En el aire libre.", "A", "El biodigestor está cerrado y sin oxígeno."),
      ("La insulina se fabrica hoy con bacterias. ¿Qué se les entrega? A) El gen humano de la insulina; B) Azúcar solamente.", "A", "Así producen la hormona."),
      ("¿Por qué el metano debe captarse y no escapar? A) Es un gas de efecto invernadero; B) Se acaba rápido.", "A", "Contribuye al calentamiento del planeta."),
  ],
  app=[
      arith("Un biodigestor de ejemplo recibe 50 kg de residuos al día y produce 4 m³ de biogás por cada 10 kg. ¿Cuántos m³ produce al día?", "50//10*4", "Cada 10 kg dan 4 m³."),
      arith("Una tonelada de roca contiene 8 kg de cobre y se recupera el 50 %. ¿Cuántos kg se obtienen?", "8*50//100", "Se calcula la mitad."),
      ("Cuatro productos: penicilina, metano, cobre y yogurt. ¿Cuál es un alimento?", "El yogurt", "Los otros tres son un fármaco, un combustible y un metal."),
  ],
  rea=[
      ("¿Por qué la biolixiviación se usa en minerales de baja concentración? Responde en una frase.", "Porque permite recuperar cobre que sería poco rentable por otros medios", "Aprovecha rocas pobres."),
      ("¿Por qué un biodigestor se cierra sin oxígeno?", "Porque las bacterias del metano viven sin oxígeno", "El oxígeno las detiene."),
  ],
  cha=[
      ("Una granja produce 120 m³ de biogás a la semana. ¿Cuántos m³ produce en 4 semanas?", "480", "120 × 4 = 480."),
      ("Alguien propone dejar escapar el metano del biodigestor «porque se va solo». ¿Qué le responderías?", "Que es un gas de efecto invernadero e inflamable y debe captarse", "El escape daña el ambiente y es peligroso."),
  ],
  context=[("Dato de ejemplo. Una planta recupera 3 kg de cobre por cada tonelada de roca tratada. ¿Cuántos kg recupera con 12 toneladas?", "36", "3 × 12 = 36 kg.")],
  selfcheck=[("¿Qué produce el biodigestor?", "Biogás con metano", "Las bacterias viven sin oxígeno."), ("¿Para qué se usan bacterias en la minería?", "Para disolver y recuperar cobre", "Se llama biolixiviación."), ("¿Qué fármaco viene de un hongo?", "La penicilina", "Es un antibiótico.")],
  open_task=task("Elige entre estas tres aplicaciones inventadas para un informe: (a) insulina fabricada con bacterias, (b) biolixiviación de cobre, (c) biodigestor para residuos de una feria. Escribe para cada una qué microorganismo actúa, qué producto se obtiene y un cuidado necesario.", "(a) Bacterias; insulina; control de calidad. (b) Bacterias de ambiente ácido; cobre disuelto; controlar el ácido. (c) Bacterias sin oxígeno; biogás; captar el metano.", ["tres aplicaciones", "producto correcto", "un cuidado en cada caso"], ["tabla o lista"], ["decir que las bacterias crean el cobre", "no mencionar cuidados"], "Pregunta cuál aplicación depende de un ambiente sin oxígeno."),
  reinforce="Escribe tres productos que se obtienen con ayuda de microorganismos.",
  extend="Explica por qué la insulina fabricada con bacterias es una aplicación de la biotecnología.")

L(OA6, 4,
  materials="Este cuaderno y lápiz. Las tablas son de ejemplo y están en cada ejercicio.",
  use="Aprenderé a relacionar las condiciones de un proceso con el producto que se obtiene. Sirve para predecir qué pasa cuando cambian la temperatura, el oxígeno o el tiempo.",
  prior=["Sé qué hacen los microorganismos en alimentos y en aplicaciones productivas.", "Sé que cambiar una condición puede cambiar el resultado."],
  explain=[
      "Todo proceso con microorganismos tiene condiciones, proceso y producto. Las condiciones incluyen el alimento, la temperatura, la presencia de oxígeno, la acidez y el tiempo. El proceso es lo que hacen los microorganismos. El producto es lo que se obtiene.",
      "Ejemplos: en el yogurt, bacterias lácticas, leche, poco oxígeno, unos 40 °C y entre 6 y 8 horas producen ácido láctico y espesan la leche. En el pan, levadura, masa con azúcar, poco oxígeno, 25 a 35 °C y algunas horas producen gas. En el biogás, bacterias, residuos orgánicos, 30 a 40 °C, sin oxígeno y varias semanas producen metano. En la biolixiviación, bacterias, mineral de cobre, medio ácido y oxígeno, y meses disuelven el cobre.",
      "Si cambia una condición, cambia el producto. Con mucho calor, los microorganismos mueren; con frío, trabajan muy lento; si entra oxígeno a un biodigestor, se detienen las bacterias del metano. Por eso se controlan y se registran las condiciones.",
  ],
  vocab=[("condición", "factor que debe cumplirse para que ocurra un proceso"), ("proceso", "serie de cambios que realizan los microorganismos"), ("producto", "lo que se obtiene al final"), ("anaerobio", "que vive sin oxígeno"), ("control de calidad", "revisión de que el producto sale como se espera")],
  worked=[
      ("Predecir con una condición", "Si se hornea la masa a 70 °C con levadura, ¿la masa seguirá subiendo?", ["A 70 °C la levadura muere.", "Sin levadura viva no hay gas."], "No, la levadura muere"),
      ("Cambiar el oxígeno", "Si entra oxígeno a un biodigestor, ¿qué ocurre con la producción de metano?", ["Las bacterias del metano viven sin oxígeno.", "El oxígeno las detiene."], "Disminuye o se detiene"),
  ],
  mistakes=[
      ("Cambiar dos condiciones a la vez y atribuir el resultado a una.", "No se sabe cuál causó el cambio.", "Cambia una condición a la vez."),
      ("Pensar que más temperatura siempre acelera la fermentación.", "Pasado un límite, los microorganismos mueren.", "Busca el rango adecuado."),
  ],
  rec=[
      ("¿Cuál es el producto de las bacterias lácticas en la leche: ácido láctico o dióxido de carbono?", "Ácido láctico", "Espesa la leche."),
      ("¿Un biodigestor necesita oxígeno: sí o no?", "No", "Sus bacterias son anaerobias."),
      ("¿Qué condición se cambia si se enfría el yogurt a 5 °C: la temperatura o el alimento?", "La temperatura", "El frío frena a las bacterias."),
  ],
  und=[
      ("¿Qué pasa si la masa del pan se enfría a 5 °C? A) La levadura trabaja muy lento; B) La levadura trabaja más rápido.", "A", "El frío frena a la levadura."),
      ("En un proceso, ¿qué es el producto? A) Lo que se obtiene al final; B) Lo que se necesita al inicio.", "A", "Las condiciones son lo que se necesita."),
      ("¿Para qué se registran las condiciones durante el proceso?", "Para comprobar que se mantienen en el rango adecuado", "Así el producto sale como se espera."),
  ],
  app=[
      ("Tabla de ejemplo: a 10 °C una masa sube 1 cm, a 25 °C sube 4 cm, a 35 °C sube 6 cm y a 60 °C sube 0 cm. ¿A qué temperatura sube más?", "35 °C", "Tiene el mayor aumento."),
      arith("Con esa tabla, ¿cuántos centímetros más sube a 35 °C que a 10 °C?", "6-1", "Se resta."),
      ("Con la misma tabla, ¿por qué sube 0 cm a 60 °C? A) Porque la levadura muere; B) Porque la masa no tenía azúcar.", "A", "El calor excesivo la mata."),
  ],
  rea=[
      ("Un grupo cambió a la vez la temperatura y la cantidad de azúcar de una masa y dice que el azúcar fue la causa. ¿Qué error cometió?", "Cambió dos condiciones a la vez", "No se sabe cuál causó el resultado."),
      ("Una persona quiere hacer yogurt con leche a 5 °C. ¿Qué condición debe cambiar? Escribe cuál.", "La temperatura", "Las bacterias prefieren unos 40 °C."),
  ],
  cha=[
      ("Dos biodigestores: A recibe 40 kg de residuos al día y produce 16 m³; B recibe 30 kg al día y produce 15 m³. ¿Cuál produce más por kilogramo? A) A; B) B.", "B", "A produce 0,4 m³/kg y B produce 0,5 m³/kg."),
      ("Predice: ¿qué ocurre con la biolixiviación si el medio deja de ser ácido? Responde en una frase.", "Las bacterias dejan de funcionar bien y se disuelve menos cobre", "Dependen de un medio ácido."),
  ],
  context=[("Dato de ejemplo. Un taller de yogurt registra la temperatura cada hora: 42, 41, 40, 40 y 39 °C. ¿Cuántos grados bajó entre el primer y el último registro?", "3", "42 − 39 = 3 °C.")],
  selfcheck=[("¿Qué incluyen las condiciones de un proceso?", "Alimento, temperatura, oxígeno, acidez y tiempo", "Determinan si funciona."), ("¿Qué ocurre si hay demasiado calor?", "Los microorganismos mueren", "Detiene el proceso."), ("¿Por qué se cambia una condición a la vez?", "Para saber cuál causó el cambio", "Así se atribuye bien.")],
  open_task=task("Completa una tabla con tres procesos inventados (pan, yogurt, biogás). Para cada uno escribe: condiciones (alimento, temperatura, oxígeno), proceso y producto. Luego predice qué pasa si la temperatura se sube a 70 °C en cada uno.", "Pan: azúcar, 30 °C, poco oxígeno, levadura → gas; a 70 °C muere. Yogurt: leche, 40 °C, sin oxígeno, bacterias → ácido láctico; a 70 °C mueren. Biogás: residuos, 35 °C, sin oxígeno, bacterias → metano; a 70 °C mueren.", ["tres filas", "condiciones, proceso, producto", "predicción para cada uno"], ["tabla y predicciones"], ["olvidar el oxígeno", "decir que más calor siempre mejora"], "Pregunta qué cambio de una sola condición probaría primero."),
  reinforce="Escribe una condición y el producto de un proceso con microorganismos.",
  extend="Explica por qué se llama anaerobio a un proceso que ocurre sin oxígeno.")

L(OA6, 5,
  materials="Este cuaderno y lápiz. Las tablas y los puntajes son de ejemplo, escritos en los ejercicios.",
  use="Aprenderé a evaluar beneficios, riesgos y límites de una aplicación biotecnológica y a decidir con criterios. Sirve para tomar decisiones informadas sobre tecnologías que usan microorganismos.",
  prior=["Sé qué aplicaciones usan microorganismos.", "Sé que las condiciones determinan el resultado."],
  explain=[
      "Toda aplicación biotecnológica tiene beneficios, riesgos y límites. Un beneficio puede ser producir alimentos, energía o medicamentos, o reducir la contaminación. Un riesgo es algo que podría salir mal, como un escape de metano, un microorganismo que contamine, el uso inadecuado de antibióticos o el mal manejo de residuos.",
      "Un límite es lo que la técnica no puede hacer o requiere: tiempo, condiciones controladas o conocimientos. Por ejemplo, los microorganismos no degradan los metales pesados y su eficacia cambia con el clima.",
      "Para decidir se usa una matriz con criterios y puntajes. Se asigna un puntaje de 1 a 5, donde 5 es lo mejor, y se suman. Esa suma ayuda a comparar, pero no reemplaza el juicio: hay que mirar también la seguridad y a quiénes afecta.",
  ],
  vocab=[("beneficio", "ventaja que entrega una aplicación"), ("riesgo", "posibilidad de que algo salga mal"), ("límite", "aquello que la técnica no puede lograr"), ("matriz de decisión", "tabla con criterios y puntajes"), ("criterio", "regla para comparar opciones")],
  worked=[
      ("Sumar puntajes", "Opción A: costo 3, seguridad 5, beneficio 4. Opción B: costo 5, seguridad 2, beneficio 4. ¿Cuál suma más?", ["A: 3 + 5 + 4 = 12.", "B: 5 + 2 + 4 = 11."], "La opción A (12 contra 11)"),
      ("Mirar más allá del total", "Si B tuviera un 1 en seguridad, ¿convendría igual elegirla por su suma?", ["Un 1 en seguridad indica un riesgo alto.", "La suma no basta."], "No automáticamente; hay que revisar el riesgo"),
  ],
  mistakes=[
      ("Decidir solo por el puntaje total.", "Un puntaje bajo en seguridad puede ser decisivo.", "Revisa cada criterio."),
      ("Ver solo beneficios.", "Toda aplicación tiene riesgos y límites.", "Lista los tres."),
  ],
  rec=[
      ("¿Es un beneficio producir energía con biogás o un escape de metano?", "Producir energía", "El escape es un riesgo."),
      ("¿Es un riesgo dejar escapar metano: sí o no?", "Sí", "Es inflamable y de efecto invernadero."),
      ("¿Es un límite que los microorganismos no degraden metales pesados: sí o no?", "Sí", "La técnica no puede lograrlo."),
  ],
  und=[
      ("Clasifica «reducir la contaminación del agua»: ¿beneficio, riesgo o límite?", "Beneficio", "Es una ventaja de la aplicación."),
      ("Clasifica «necesita temperatura de 35 °C constante»: ¿beneficio, riesgo o límite?", "Límite", "Es un requisito de la técnica."),
      ("¿Para qué sirve una matriz de decisión? A) Para comparar opciones con criterios; B) Para evitar decidir.", "A", "Ordena la información."),
  ],
  app=[
      arith("Opción A: costo 4, seguridad 3, beneficio 5. Opción B: costo 3, seguridad 5, beneficio 4. ¿Cuántos puntos suma la opción A?", "4+3+5", "Se suman los tres criterios."),
      arith("Con la misma matriz, ¿cuántos puntos suma la opción B (costo 3, seguridad 5, beneficio 4)?", "3+5+4", "Se suman los tres criterios."),
      ("Con esas sumas (A y B iguales), ¿qué conviene hacer? A) Revisar cada criterio, en especial la seguridad; B) Elegir al azar.", "A", "Un empate no se resuelve al azar."),
  ],
  rea=[
      ("Una aplicación suma 14 puntos pero tiene un 1 en seguridad. ¿Qué sugieres?", "Revisar el riesgo antes de decidir", "Un puntaje bajo en seguridad es relevante."),
      ("Alguien dice: «Si funciona en el laboratorio, funcionará en todo el país». ¿Qué límite olvida?", "Que las condiciones reales pueden cambiar", "La escala y el clima influyen."),
  ],
  cha=[
      ("Un pueblo inventado evalúa un biodigestor para 600 kg de residuos al día. Si 1 kg produce 0,4 m³ (biogás) y la meta es 200 m³ al día, ¿lo logra? Responde Sí o No y da el valor.", "Sí; 240 m³", "600 × 0,4 = 240, que supera 200."),
      ("Redacta una recomendación de dos frases para el pueblo: un beneficio, un riesgo y un cuidado.", "El biodigestor aporta energía y reduce residuos; hay riesgo de fuga de metano y debe tener control", "Incluye beneficio, riesgo y cuidado."),
  ],
  context=[("Dato de ejemplo. Un pueblo genera 900 kg de residuos orgánicos a la semana y el biodigestor puede tratar 600 kg. ¿Cuántos kg quedan sin tratar?", "300", "900 − 600 = 300.")],
  selfcheck=[("¿Qué es un riesgo?", "La posibilidad de que algo salga mal", "Ejemplo: fuga de metano."), ("¿Qué es un límite?", "Lo que la técnica no puede lograr o requiere", "Ejemplo: no degrada metales pesados."), ("¿Para qué sirve la matriz?", "Para comparar opciones con criterios", "No reemplaza el juicio.")],
  open_task=task("Evalúa una aplicación inventada: «una escuela instala un compostaje con restos de su casino». Escribe dos beneficios, dos riesgos y dos límites, y completa una mini matriz con costo, seguridad y beneficio (1 a 5). Concluye si la recomendarías.", "Beneficios: abono y menos residuos. Riesgos: malos olores y animales. Límites: lento y necesita humedad y oxígeno. Matriz: costo 4, seguridad 4, beneficio 5. Recomendación: sí, con cuidados.", ["dos beneficios, dos riesgos, dos límites", "matriz completa", "conclusión coherente"], ["lista y mini matriz"], ["no incluir riesgos", "decidir solo por el total"], "Pregunta qué cambiaría si hubiera restos de carne."),
  reinforce="Escribe un beneficio, un riesgo y un límite de una aplicación a elegir de la clase.",
  extend="Explica por qué un puntaje total alto no siempre significa que una opción sea segura.")
