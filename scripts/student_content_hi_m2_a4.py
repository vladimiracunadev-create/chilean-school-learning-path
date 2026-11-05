"""Material del estudiante de 2.º medio, Historia, Geografía y Ciencias Sociales: OA 07 (nuevos actores, cultura de masas y democratización) y OA 08 (Guerra Fría)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 07"

# ================================================================ OA 07, clase 1
F = ("Ficha 1 (mediados del siglo XX en Chile, años 1930 a 1960 aproximadamente). "
     "Hitos: primeras transmisiones de radio en Chile, 1922; se aprueba la ley que permite a las mujeres votar en elecciones municipales, 1934; se funda el MEMCH (Movimiento Pro Emancipación de la Mujer Chilena), 1935; "
     "Pedro Aguirre Cerda gana la presidencia con el Frente Popular y el lema «Gobernar es educar», 1938; se inaugura el Estadio Nacional, 1938; ley que otorga a las mujeres el pleno derecho a voto, 1949; "
     "primera elección presidencial en que votan mujeres, 1952. "
     "Actores: mujeres; clase media (empleados, profesores, profesionales); clase obrera (trabajadores de fábricas y minas, organizados en sindicatos); partidos políticos; público de la radio, el cine y el deporte.")
build(
    OA, 1, F,
    use="Aprenderé a situar en el tiempo y entre sus actores la democratización de la sociedad chilena a mediados del siglo XX: quiénes ganaron participación y qué papel tuvo la cultura de masas.",
    prior=["Sé que en el siglo XIX el voto estaba muy restringido.", "Sé calcular diferencias entre años.", "Sé que una fuente es una huella del pasado."],
    explain=[
        "Democratización es el proceso por el cual más personas participan en las decisiones de una sociedad y acceden a sus beneficios. En Chile, a mediados del siglo XX, ese proceso se vio en el voto, en la organización de los grupos sociales y en el acceso a bienes culturales. No ocurrió de golpe: avanzó por etapas y con desigualdades.",
        "Los nuevos actores fueron las mujeres, que lucharon por la ciudadanía política, es decir, por el derecho a votar y ser elegidas; la clase media, formada por empleados, profesores y profesionales que ganaban peso en la política; y la clase obrera, que se organizaba en sindicatos (asociaciones de trabajadores que defienden sus intereses). Cada grupo tenía demandas propias.",
        "A la vez creció la cultura de masas: la radio, el cine y el deporte llegaban a muchas personas, también a barrios populares. Esto permitió informarse, entretenerse y sentirse parte de una comunidad nacional. Para estudiarlo hay que situar cada hecho en su fecha y preguntar quién participaba y quién quedaba fuera.",
    ],
    vocab=[("democratización", "proceso por el cual más personas participan en las decisiones y en los beneficios de una sociedad"), ("ciudadanía política", "derecho a votar y a ser elegido"), ("clase media", "grupo de empleados, profesores y profesionales con ingresos estables, entre la clase alta y la obrera"), ("clase obrera", "trabajadores de fábricas, minas y otros oficios que viven de un salario"), ("sindicato", "asociación de trabajadores que defiende sus intereses")],
    worked=[
        ("Calcular una diferencia de años", "¿Cuántos años pasaron entre las primeras transmisiones de radio (1922) y la inauguración del Estadio Nacional (1938)?", ["Tomo los dos años de la ficha.", "Resto: 1938 − 1922 = 16."], "16 años"),
        ("Identificar un actor", "Trabajadores de una fábrica se reúnen para formar un sindicato y pedir mejores salarios. ¿Qué actor social son?", ["Viven de un salario en una fábrica.", "Se organizan en un sindicato, como indica el vocabulario."], "Clase obrera"),
    ],
    mistakes=[("Creer que las mujeres tuvieron voto pleno desde 1934.", "Se confunde el voto municipal con el derecho a votar en todas las elecciones.", "Distingue 1934 (municipal) de 1949 (pleno derecho) y de 1952 (primera presidencial con mujeres)."),
              ("Pensar que democratización es lo mismo que cultura de masas.", "Se mezcla el acceso a la radio o al deporte con la participación política.", "Pregunta si el hecho amplía la participación en decisiones (voto, organización) o el acceso a bienes culturales; puede ser ambas cosas.")],
    T=[
        ("{F} ¿En qué año se aprobó la ley que permitió a las mujeres votar en elecciones municipales?", "1934", "La ficha lo indica."),
        ("{F} ¿Qué organización de mujeres se funda en 1935?", "El MEMCH (Movimiento Pro Emancipación de la Mujer Chilena)", "La ficha la nombra con ese año."),
        ("{F} ¿Qué lema usó Pedro Aguirre Cerda en la campaña de 1938?", "«Gobernar es educar»", "Está escrito en la ficha."),
        ("=", "{F} ¿Cuántos años pasaron entre la ley del voto municipal de las mujeres y la ley de pleno derecho a voto?", "1949-1934", "Se resta el año del voto municipal al de la ley de pleno derecho.", " años"),
        ("{F} ¿Qué ocurrió en 1952, según la ficha?", "La primera elección presidencial en que votaron mujeres", "La ficha lo indica entre sus hitos."),
        ("{F} Un grupo de profesores y empleados públicos exige mejores sueldos y más escuelas. ¿Qué actor representa mejor? A) La clase media B) La clase obrera", "A) La clase media", "Empleados y profesores forman la clase media según la ficha."),
        ("{F} Una radio transmite un partido desde el Estadio Nacional a miles de hogares. ¿Qué proceso muestra? A) Expansión de la cultura de masas B) Ampliación del voto femenino", "A) Expansión de la cultura de masas", "Llegar a muchas personas por un medio de comunicación es cultura de masas."),
        ("{F} Una mujer de ejemplo, inscrita para votar, quiere hacerlo en la elección presidencial de 1952. ¿Podía? A) Sí, porque la ley de 1949 le dio pleno derecho B) No, porque en 1934 solo se permitió el voto municipal", "A) Sí, porque la ley de 1949 le dio pleno derecho", "La ley de 1949 reemplazó la restricción anterior; B ignora ese cambio posterior."),
        ("{F} ¿Qué hecho es anterior a 1930? A) Las primeras transmisiones de radio B) La inauguración del Estadio Nacional", "A) Las primeras transmisiones de radio", "La radio es de 1922 y el estadio de 1938."),
        ("{F} ¿Por qué no se puede decir que en 1934 las mujeres ya tenían plena ciudadanía política?", "Porque la ley de ese año solo les permitía votar en elecciones municipales y el pleno derecho llegó en 1949", "La ficha separa el voto municipal del pleno derecho a voto."),
        ("{F} Un compañero dice: «El Estadio Nacional prueba que en 1938 toda la población participaba por igual». ¿Qué respondes? A) Inaugurar un estadio no prueba igualdad de participación política B) Tiene razón, porque asistía mucha gente", "A) Inaugurar un estadio no prueba igualdad de participación política", "Un hecho cultural no demuestra por sí solo quiénes podían votar o decidir."),
        ("¿Cuál es la mejor pregunta para investigar este tema? A) ¿Cómo contribuyeron las mujeres, la clase media, la clase obrera y la cultura de masas a ampliar la participación en Chile a mediados del siglo XX? B) ¿Qué radio fue la mejor de esos años?", "A) ¿Cómo contribuyeron las mujeres, la clase media, la clase obrera y la cultura de masas a ampliar la participación en Chile a mediados del siglo XX?", "La pregunta A tiene actores, época y se responde con hechos; la B es una opinión."),
        ("{F} ¿Qué par de datos de la ficha sostiene mejor que el voto de las mujeres se amplió por etapas? A) Voto municipal en 1934 y pleno derecho en 1949 B) Estadio Nacional en 1938 y primera radio en 1922", "A) Voto municipal en 1934 y pleno derecho en 1949", "Dos fechas de una misma demanda muestran una ampliación gradual; B son hechos de otro tipo."),
    ],
    ctx=("Un afiche de museo de ejemplo dice: «Desde 1934 Chile era una democracia con participación completa». ¿Qué problema tiene? A) Ignora que el pleno voto de las mujeres llegó en 1949 B) Usa una fecha municipal", "A) Ignora que el pleno voto de las mujeres llegó en 1949", "La ficha muestra que en 1934 la participación femenina era parcial."),
    sc=[("En Historia: ¿qué es la democratización?", "El proceso por el cual más personas participan en las decisiones y en los beneficios de una sociedad", "Así se define en el vocabulario de la clase."),
        ("En Historia: ¿qué es un sindicato obrero?", "Una asociación de trabajadores que defiende sus intereses", "Así lo define el vocabulario."),
        ("En Historia: ¿qué es la ciudadanía política?", "El derecho a votar y a ser elegido", "Así se define en el vocabulario.")],
    op=("Dibuja una línea de tiempo de 1920 a 1955. Marca con una raya el año y el nombre de estos hitos: radio (1922), voto municipal de las mujeres (1934), MEMCH (1935), Frente Popular y Estadio Nacional (1938), ley de pleno voto (1949) y elección presidencial con mujeres (1952). Pinta de un color los hitos de participación política y de otro los de cultura de masas. {F}",
        "Participación política: 1934, 1935, 1938 (Frente Popular), 1949, 1952. Cultura de masas: 1922 y 1938 (Estadio Nacional). El año 1938 aparece dos veces porque tiene hitos de ambos tipos.",
        ["ubica los hitos en su año", "usa dos colores bien distribuidos", "no confunde el voto municipal con el pleno"], ["línea de tiempo dibujada"], ["pintar el Estadio Nacional como hito de voto", "poner 1934 como voto pleno"],
        "Pide que explique por qué un mismo año puede tener hitos de dos tipos."),
    reinforce="Explica en voz alta la diferencia entre democratización y cultura de masas y da un hito con su año para cada una.",
    extend="Pregunta a una persona de tu casa qué medio de comunicación usaba para informarse cuando era joven y anótalo en una frase.",
)

# ================================================================ OA 07, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, editorial de un diario conservador, 1948: «Dar el voto a las mujeres confundirá a las familias; la política es asunto de los hombres.» "
     "Fuente B, acta de una reunión de una organización de mujeres, 1947: «Acordamos reunir firmas para exigir el voto en las elecciones presidenciales y parlamentarias, pues ya votamos en las municipales.» "
     "Fuente C, aviso de una tienda de radios, 1950: «Escuche cada noche el radioteatro y los discursos de los candidatos. Su radio, en cuotas mensuales.» "
     "Preguntas de procedencia: ¿quién la produjo?, ¿cuándo?, ¿para quién?, ¿con qué propósito?")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre la democratización con sus datos de procedencia (autor, fecha, destinatario y propósito) y a decir qué pueden y qué no pueden probar.",
    prior=["Sé situar los actores de la democratización chilena.", "Sé que una fuente es una huella del pasado.", "Sé distinguir un dato de una opinión."],
    explain=[
        "La procedencia de una fuente es su origen: quién la produjo, cuándo, para quién y con qué propósito. Antes de usarla como evidencia, un historiador responde esas cuatro preguntas. Un editorial expresa la opinión de un diario; un acta registra lo que una organización acordó; un aviso busca vender. Ninguna es un relato neutral de lo que pensaba toda la sociedad.",
        "Una fuente primaria es la creada en la época que se estudia, como las tres de la ficha. Sirve para conocer lo que ciertas personas pensaban o hacían, pero cada una muestra solo una parte. Por eso se contrastan: si dos fuentes dicen cosas opuestas, no se concluye que una sea falsa, sino que había opiniones enfrentadas.",
        "Hay que cuidar la conclusión: una fuente prueba lo que dice y nada más. Un aviso de radios muestra que se vendían en cuotas, no cuántos hogares las tenían. Un editorial muestra una oposición al voto femenino, no que toda la sociedad pensara igual. Si falta un dato, como el nombre del autor, se anota como un límite.",
    ],
    vocab=[("procedencia", "origen de una fuente: autor, fecha, destinatario y propósito"), ("fuente primaria", "documento creado en la época que se estudia"), ("editorial", "texto de un diario que expresa su opinión"), ("acta", "documento que registra lo discutido y acordado en una reunión"), ("propósito", "lo que busca lograr quien produce una fuente")],
    worked=[
        ("Preguntar por el propósito", "Un aviso de ejemplo de 1951 dice: «Compre su radio hoy». ¿Cuál es su propósito?", ["Los avisos los paga quien quiere vender.", "La frase invita a comprar."], "Vender radios"),
        ("Fijar el límite de una fuente", "Un acta de ejemplo dice que 20 mujeres asistieron a una reunión. ¿Prueba que todas las mujeres de Chile pensaban igual?", ["El acta registra solo esa reunión.", "No dice nada sobre el resto del país."], "No: solo muestra lo que pasó en esa reunión"),
    ],
    mistakes=[("Tratar un editorial como un relato neutral de lo que opinaba todo el país.", "Se olvida que un diario tiene una línea y un público.", "Pregunta quién escribe y para quién, y busca otra fuente que contraste."),
              ("Decir que una de dos fuentes opuestas es falsa.", "Se confunde una opinión distinta con una mentira.", "Concluye que había posiciones enfrentadas y busca más evidencia.")],
    T=[
        ("{F} ¿Qué tipo de documento es la Fuente B?", "Un acta de una reunión de una organización de mujeres", "La ficha la presenta como acta."),
        ("{F} ¿En qué año se publicó la Fuente C?", "1950", "La ficha lo señala."),
        ("{F} ¿Quién produjo la Fuente A?", "Un diario conservador", "La ficha indica su procedencia."),
        ("{F} ¿Para qué se escribió la Fuente B? A) Para organizar una petición de voto presidencial y parlamentario B) Para expresar la opinión de un diario contra el voto femenino", "A) Para organizar una petición de voto presidencial y parlamentario", "El acta registra un acuerdo de reunir firmas."),
        ("{F} ¿Qué propósito tiene la Fuente C? A) Vender radios en cuotas B) Informar sobre una ley del voto", "A) Vender radios en cuotas", "Es un aviso de una tienda y ofrece pago en cuotas."),
        ("{F} ¿Qué dato de procedencia de la Fuente A falta en la ficha? A) El nombre de quien escribió el editorial B) El año de publicación", "A) El nombre de quien escribió el editorial", "La ficha da el año y el tipo de diario, pero no el autor."),
        ("{F} Un compañero usa la Fuente A para afirmar: «En 1948 nadie quería el voto femenino». ¿Qué límite tiene? A) Es la opinión de un diario y la Fuente B muestra una posición contraria B) Es demasiado antigua", "A) Es la opinión de un diario y la Fuente B muestra una posición contraria", "Una opinión no representa a toda la sociedad y otra fuente la contradice."),
        ("{F} Para saber cuántos hogares tenían radio en 1950, ¿sirve la Fuente C? A) Solo muestra que se vendían radios en cuotas, no cuántos hogares las tenían B) Sí, prueba que todos los hogares tenían radio", "A) Solo muestra que se vendían radios en cuotas, no cuántos hogares las tenían", "Un aviso no entrega cifras de hogares."),
        ("{F} ¿Qué fuente muestra mejor la iniciativa organizada de las mujeres? A) La Fuente B B) La Fuente A", "A) La Fuente B", "El acta registra una decisión tomada por la propia organización."),
        ("{F} ¿Por qué hay que preguntar por el propósito antes de creer lo que dice un aviso?", "Porque quien lo paga quiere vender y puede mostrar solo lo que le conviene", "El propósito comercial limita lo que el aviso dice."),
        ("{F} Las Fuentes A y B se contradicen. ¿Qué conclusión es válida? A) Había opiniones enfrentadas sobre el voto femenino B) Una de las dos fuentes es falsa", "A) Había opiniones enfrentadas sobre el voto femenino", "Dos posiciones distintas no implican que una sea mentira."),
        ("{F} Quieres sostener que «entre 1947 y 1950 las mujeres y la radio ampliaron la participación». ¿Qué fuentes usas y qué límite declaras? A) B y C; son casos aislados y no prueban lo ocurrido en todo el país B) Solo A; no tiene límites", "A) B y C; son casos aislados y no prueban lo ocurrido en todo el país", "B muestra organización de mujeres y C difusión de la radio; ambas son ejemplos puntuales."),
        ("{F} ¿Qué fuente adicional ayudaría más a saber cuántas mujeres se inscribieron para votar? A) Un registro electoral de la época B) Un editorial de un diario sobre el voto de las mujeres", "A) Un registro electoral de la época", "Un registro cuenta personas inscritas; el afiche solo promociona una película."),
    ],
    ctx=("Una compañera cita solo el aviso de radios para explicar cómo se informaban los chilenos en 1950. ¿Qué le recomiendas? A) Contrastarlo con otras fuentes, porque un aviso busca vender y no mide el acceso B) Usarlo solo, porque tiene fecha", "A) Contrastarlo con otras fuentes, porque un aviso busca vender y no mide el acceso", "La fecha no basta: falta evidencia sobre cuántos hogares tenían radio."),
    sc=[("¿Qué son las preguntas de procedencia?", "Preguntas sobre quién produjo la fuente, cuándo, para quién y con qué propósito", "Así se explica en la clase."),
        ("En Historia: ¿qué es una fuente primaria?", "Un documento creado en la época que se estudia", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es un editorial?", "Un texto de un diario que expresa su opinión", "Así se define en el vocabulario.")],
    op=("Elige una de las tres fuentes de la ficha y haz una tarjeta con cuatro líneas: quién la produjo, cuándo, para quién y con qué propósito. Agrega una quinta línea con lo que NO puede probar. Luego escribe una frase que combine dos fuentes con «en cambio» o «sin embargo». {F}",
        "Fuente C: la produjo una tienda de radios; 1950; público que escucha radio; propósito vender. No prueba cuántos hogares tenían radio. Frase: «La Fuente B muestra a mujeres organizadas; en cambio, la Fuente A expresa oposición».",
        ["responde las cuatro preguntas de procedencia", "declara un límite real", "contrasta dos fuentes sin llamar falsa a ninguna"], ["tarjeta de cinco líneas", "frase de contraste"], ["copiar el contenido de la fuente en vez de su procedencia", "declarar falsa la fuente que no concuerda"],
        "Pide que explique qué otra fuente agregaría para ampliar la conclusión."),
    reinforce="Elige un aviso o un mensaje reciente que veas y di quién lo produjo, para quién y con qué propósito.",
    extend="Escribe una pregunta que ninguna de las tres fuentes puede responder y qué documento la respondería.",
)

# ================================================================ OA 07, clase 3
F = ("Ficha 3 (datos y testimonios de ejemplo, escritos para practicar; no son documentos históricos reales). "
     "Dato 1: en una ciudad de ejemplo se encuestaron 400 hogares y 280 tienen radio. "
     "Dato 2: en una localidad rural de ejemplo se encuestaron 200 hogares y 50 tienen radio. "
     "Testimonio 1, obrero de una fábrica, 1950: «El sindicato consiguió un día de descanso pagado; el domingo escucho el fútbol por radio.» "
     "Testimonio 2, profesora de un colegio fiscal, 1950: «Con mi sueldo estable compré una radio y mis hijos van al liceo.» "
     "Testimonio 3, campesina, 1950: «Aquí la señal llega mal y las noticias llegan tarde.» "
     "Escalas: nacional (todo el país), local (una ciudad, un barrio o una localidad).")
build(
    OA, 3, F,
    use="Aprenderé a comparar perspectivas de distintos grupos y a distinguir escalas, para evaluar en quiénes y dónde llegó la democratización y la cultura de masas.",
    prior=["Sé interrogar fuentes con su procedencia.", "Sé calcular un porcentaje con números enteros.", "Sé que un mismo hecho puede verse distinto según quién lo viva."],
    explain=[
        "Una perspectiva es el modo de ver un proceso desde la situación de un grupo. Un obrero, una profesora y una campesina vivieron la misma época, pero con condiciones distintas: sindicato y descanso pagado, sueldo estable y liceo, o mala señal de radio. Compararlas no significa decidir quién tiene razón, sino entender qué experiencias tuvo cada grupo.",
        "La escala es el tamaño del espacio que se mira: local, regional o nacional. Un dato de una ciudad no se puede aplicar a todo el país. Por eso un buen análisis dice a qué escala pertenece cada dato y no generaliza. Los porcentajes ayudan a comparar: 25 hogares de cada 100 es 25 %, sea cual sea el tamaño de la muestra.",
        "En la democratización de mediados del siglo XX hubo diferencias entre ciudad y campo, entre grupos sociales y entre hombres y mujeres. Comparar perspectivas y escalas permite ver avances y también quiénes quedaban atrás. Una conclusión sólida nombra el grupo y el lugar de donde viene cada evidencia.",
    ],
    vocab=[("perspectiva", "manera de ver un proceso desde la situación de un grupo"), ("escala", "tamaño del espacio que se estudia: local, regional o nacional"), ("generalizar", "extender una conclusión de un caso a todos los casos sin evidencia suficiente"), ("porcentaje", "parte de cada cien"), ("muestra", "grupo de casos que se mide para estudiar un conjunto mayor")],
    worked=[
        ("Calcular un porcentaje", "En un barrio de ejemplo se encuestaron 150 hogares y 90 tienen radio. ¿Qué porcentaje es?", ["Divido 90 en 150: 0,6.", "Multiplico por 100: 60."], "60 %"),
        ("Identificar la escala", "Un dato dice «en la población La Esperanza de ejemplo hay 30 radios». ¿Qué escala tiene?", ["Habla de un barrio o población.", "No habla de todo el país."], "Escala local"),
    ],
    mistakes=[("Aplicar el dato de una ciudad a todo el país.", "Se confunde una muestra local con la realidad nacional.", "Nombra la escala del dato y di solo lo que ese dato permite concluir."),
              ("Creer que si una perspectiva es distinta, está equivocada.", "Se piensa que solo hay una experiencia verdadera.", "Reconoce que cada grupo muestra una parte de la historia y contrástalas.")],
    T=[
        ("{F} ¿Qué actor habla en el Testimonio 1?", "Un obrero de una fábrica", "La ficha lo indica."),
        ("{F} ¿Qué escala tiene el Dato 2 (una localidad rural con 200 hogares encuestados)?", "Local", "Es una localidad, no todo el país."),
        ("{F} ¿Qué problema menciona la campesina del Testimonio 3?", "Que la señal llega mal y las noticias llegan tarde", "Lo dice la ficha."),
        ("=", "{F} ¿Qué porcentaje de los hogares encuestados de la ciudad tiene radio?", "280/400*100", "Se divide 280 por 400 y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de los hogares encuestados de la localidad rural tiene radio?", "50/200*100", "Se divide 50 por 200 y se multiplica por 100.", " %"),
        ("{F} ¿Qué perspectiva destaca la estabilidad del sueldo? A) La de la profesora B) La del obrero", "A) La de la profesora", "La profesora dice «con mi sueldo estable»."),
        ("{F} Una investigadora afirma: «En todo Chile el 70 % de los hogares tenía radio». ¿Qué error comete? A) Generaliza el dato de una ciudad a todo el país B) Calcula mal el porcentaje", "A) Generaliza el dato de una ciudad a todo el país", "El 70 % es de una ciudad de ejemplo y no representa la escala nacional."),
        ("=", "{F} ¿Cuántos puntos porcentuales más tiene la ciudad que la localidad rural en hogares con radio?", "280/400*100-50/200*100", "Se restan los dos porcentajes: 70 menos 25.", " puntos"),
        ("{F} ¿Qué comparación sirve para ver diferencias entre ciudad y campo? A) Comparar el dato de la ciudad con el de la localidad rural B) Comparar el testimonio del obrero con el de la profesora", "A) Comparar el dato de la ciudad con el de la localidad rural", "Los datos 1 y 2 enfrentan dos lugares; los testimonios 1 y 2 enfrentan dos grupos."),
        ("{F} ¿Por qué el testimonio del obrero y el de la campesina pueden no coincidir aunque hablen del mismo país?", "Porque viven en lugares y condiciones distintas, una ciudad con sindicato y un campo con mala señal", "La ficha muestra contextos diferentes para cada persona."),
        ("{F} Un compañero dice: «Como la profesora y el obrero tienen radio, el campo también». ¿Qué respuesta es correcta? A) Los datos y el testimonio rurales muestran menos acceso, así que no se puede generalizar B) Es correcto porque la radio llegaba a todas partes", "A) Los datos y el testimonio rurales muestran menos acceso, así que no se puede generalizar", "Dos casos urbanos no representan al campo y la ficha trae evidencia rural distinta."),
        ("{F} ¿Qué conclusión comparativa se sostiene con la ficha? A) En los datos de ejemplo, el acceso a la radio fue mayor en la ciudad que en la localidad rural B) La radio llegó a todos los grupos por igual", "A) En los datos de ejemplo, el acceso a la radio fue mayor en la ciudad que en la localidad rural", "70 % frente a 25 %; B contradice los datos."),
        ("{F} ¿Qué fuente agregarías para conocer la perspectiva de una mujer de ciudad sobre el voto? A) El testimonio de una mujer que vota por primera vez en una ciudad B) El testimonio de un obrero sobre su sindicato", "A) El testimonio de una mujer que vota por primera vez en una ciudad", "Aporta una perspectiva que la ficha no contiene."),
    ],
    ctx=("Un informe escolar concluye: «La democratización llegó a todos por igual porque había radios en la ciudad». ¿Qué comparación falta? A) Contrastar con datos y testimonios del campo y de otros grupos B) Agregar más datos de hogares de la ciudad", "A) Contrastar con datos y testimonios del campo y de otros grupos", "Sin otras escalas y perspectivas no se puede afirmar igualdad."),
    sc=[("En Historia: ¿qué es una escala en historia?", "El tamaño del espacio que se estudia, como local, regional o nacional", "Así se define en la clase."),
        ("En Historia: ¿qué significa generalizar?", "Extender una conclusión de un caso a todos sin evidencia suficiente", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es una muestra?", "Un grupo de casos que se mide para estudiar un conjunto mayor", "Así se define en el vocabulario.")],
    op=("Haz una tabla de dos columnas: «ciudad» y «campo». Escribe en cada una el porcentaje de hogares con radio de la ficha y la frase del testimonio que corresponde. Debajo escribe dos oraciones: una que compare las perspectivas del obrero y de la profesora, y otra que diga qué escala tiene tu conclusión y qué no puedes afirmar. {F}",
        "Ciudad: 70 % y «con mi sueldo estable compré una radio». Campo: 25 % y «la señal llega mal». Oraciones: «El obrero valora el descanso pagado que consiguió el sindicato y la profesora valora su sueldo estable»; «Mi conclusión es local y no permite afirmar cómo era todo el país».",
        ["calcula bien los dos porcentajes", "compara dos perspectivas sin decir que una es falsa", "declara la escala de su conclusión"], ["tabla completa", "dos oraciones"], ["generalizar los datos a todo Chile", "mezclar porcentajes de ciudad y campo"],
        "Pide que diga qué otro dato necesitaría para hablar de todo el país."),
    reinforce="Explica a alguien de tu casa por qué un dato de una ciudad no sirve para describir todo el país.",
    extend="Escribe una pregunta que puedas hacer a una persona mayor para conocer su perspectiva sobre cómo llegó la radio o el cine a su barrio.",
)

# ================================================================ OA 07, clase 4
F = ("Ficha 4 (causas, cambios y continuidades; hechos y un dato de ejemplo). "
     "Causas posibles de la democratización: crecimiento de las ciudades; más escuelas públicas; trabajadores organizados en sindicatos; partidos que buscan los votos de nuevos grupos; organizaciones de mujeres como el MEMCH, 1935. "
     "Cambios: las mujeres votan en las municipales, 1934, y con pleno derecho, 1949; la radio y el cine llegan a hogares y barrios; se inaugura el Estadio Nacional, 1938. "
     "Continuidades: desigualdad entre ciudad y campo; leyes civiles que seguían limitando a la mujer casada; menor organización y menor acceso a servicios en el campo. "
     "Dato de ejemplo: un liceo de ejemplo tenía 300 matrículas y pasa a tener 450.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar las causas de la democratización de mediados del siglo XX con sus cambios y continuidades, y a no confundir lo que ocurre antes con lo que causa.",
    prior=["Sé situar actores y fuentes de la democratización chilena.", "Sé comparar perspectivas y escalas.", "Sé calcular un aumento porcentual simple."],
    explain=[
        "Un proceso histórico tiene varias causas que actúan juntas. En la democratización de Chile influyeron el crecimiento de las ciudades, la ampliación de la educación, la organización de los sindicatos, la competencia de los partidos por nuevos votantes y la acción de organizaciones de mujeres. Decir que hubo una sola causa deja fuera la mayor parte de la explicación.",
        "Un cambio es algo que se transforma, como el voto femenino pleno en 1949 o la llegada de la radio a los barrios. Una continuidad es algo que sigue igual, como la desigualdad entre ciudad y campo o las leyes civiles que limitaban a la mujer casada. Casi todo proceso mezcla ambas: avanzó la participación política, pero no todas las desigualdades cambiaron.",
        "Cuidado con la causalidad: que un hecho ocurra antes de otro no prueba que sea su causa. Para sostener una relación causal se necesita evidencia que conecte los hechos, por ejemplo una fuente de la época que mencione la relación. Y conviene usar verbos prudentes como «contribuyó a» cuando la prueba es parcial.",
    ],
    vocab=[("causa", "hecho o condición que contribuye a que algo ocurra"), ("cambio", "aspecto de una sociedad que se transforma en un período"), ("continuidad", "aspecto que se mantiene igual en un período"), ("causalidad", "relación en que un hecho produce o favorece otro"), ("contribuyó a", "expresión prudente para decir que un factor ayudó sin ser el único")],
    worked=[
        ("Clasificar cambio o continuidad", "En 1949 se aprueba el pleno derecho a voto de las mujeres. ¿Es cambio o continuidad respecto de 1934?", ["En 1934 solo votaban en las municipales.", "En 1949 votan en todas las elecciones."], "Cambio"),
        ("Calcular un aumento", "Una escuela de ejemplo pasa de 200 a 260 estudiantes. ¿Cuántos estudiantes más tiene?", ["Resto el número inicial al final.", "260 − 200 = 60."], "60 estudiantes más"),
    ],
    mistakes=[("Decir que una cosa es causa de otra solo porque ocurrió antes.", "Se confunde orden en el tiempo con causalidad.", "Busca evidencia que conecte los hechos y usa «contribuyó a» si la prueba es parcial."),
              ("Pensar que, si hubo cambios, no quedó ninguna continuidad.", "Se imagina el proceso como una ruptura total.", "Pregunta qué sigue igual en cada ámbito: voto, trabajo, campo, leyes civiles.")],
    T=[
        ("{F} ¿Qué organización de mujeres se menciona entre las causas posibles?", "El MEMCH", "La ficha la nombra con el año 1935."),
        ("{F} ¿A quién seguían limitando las leyes civiles, según las continuidades de la ficha?", "A la mujer casada", "La ficha lo indica entre las continuidades."),
        ("{F} ¿Qué se inauguró en 1938 según los cambios?", "El Estadio Nacional", "La ficha lo incluye entre los cambios."),
        ("=", "{F} ¿Qué porcentaje aumentó la matrícula del liceo de ejemplo?", "(450-300)/300*100", "Se divide el aumento (150) por la cifra inicial y se multiplica por 100.", " %"),
        ("{F} Las leyes civiles seguían limitando a la mujer casada. ¿Qué es esto en la ficha? A) Una continuidad B) Un cambio", "A) Una continuidad", "La ficha la clasifica como algo que seguía igual."),
        ("{F} Los sindicatos presionaron para obtener mejoras laborales. ¿Qué es en la ficha? A) Una causa posible de la democratización B) Una continuidad", "A) Una causa posible de la democratización", "Los trabajadores organizados figuran entre las causas posibles."),
        ("{F} Una radio llega a los barrios obreros en 1950. ¿Cómo podría relacionarse con la democratización? A) Permite que más personas se informen sobre elecciones y debates B) Reemplaza el voto", "A) Permite que más personas se informen sobre elecciones y debates", "Informarse favorece la participación; la radio no sustituye el voto."),
        ("{F} Una historiadora dice: «El voto de 1949 no cambió nada porque las leyes civiles seguían limitando a la mujer casada». ¿Qué corrección haces? A) Hubo un cambio político, el voto, y a la vez continuidades en otros ámbitos B) El voto lo cambió todo", "A) Hubo un cambio político, el voto, y a la vez continuidades en otros ámbitos", "Un proceso mezcla cambios y continuidades; ni una ni otra afirmación extrema es exacta."),
        ("{F} ¿Qué par está bien ordenado en el tiempo y en la relación causal? A) Causa: organización de mujeres desde 1935; cambio: pleno voto en 1949 B) Causa: pleno voto en 1949; cambio: organización de mujeres en 1935", "A) Causa: organización de mujeres desde 1935; cambio: pleno voto en 1949", "La causa debe ocurrir antes que el cambio que ayuda a explicar."),
        ("{F} ¿Por qué no basta decir que la radio causó la democratización?", "Porque influyeron también el voto, los sindicatos, la educación y los partidos, así que hubo varias causas", "La ficha enumera varias causas que actuaron juntas."),
        ("{F} ¿Por qué la desigualdad entre ciudad y campo es una continuidad que limita la democratización?", "Porque quienes vivían en el campo tenían menos organización y menos acceso a servicios", "La ficha asocia el campo con menor organización y acceso."),
        ("{F} Un compañero propone: «El Estadio Nacional, 1938, causó el voto femenino de 1949». ¿Es razonable? A) No, ocurrir antes no prueba una causa y no hay evidencia que los conecte B) Sí, porque ocurrió antes", "A) No, ocurrir antes no prueba una causa y no hay evidencia que los conecte", "La causalidad exige evidencia, no solo orden temporal."),
        ("{F} ¿Cuál es la mejor síntesis? A) Varias causas produjeron cambios en la participación, pero continuaron desigualdades B) La democratización quedó completa en 1949", "A) Varias causas produjeron cambios en la participación, pero continuaron desigualdades", "Reúne causas, cambios y continuidades de la ficha."),
    ],
    ctx=("Un documental dice: «Gracias a la radio, Chile se hizo democrático». ¿Qué le falta según lo aprendido? A) Reconocer otras causas y las continuidades que seguían B) Citar la fecha de la primera transmisión de radio", "A) Reconocer otras causas y las continuidades que seguían", "Una sola causa y ninguna continuidad simplifica el proceso."),
    sc=[("En Historia: ¿qué es una continuidad?", "Un aspecto que se mantiene igual en un período", "Así se define en el vocabulario."),
        ("¿Qué expresión prudente sirve cuando la prueba de una causa es parcial?", "Contribuyó a", "El vocabulario la propone para no exagerar."),
        ("En Historia: ¿qué es una causa?", "Un hecho o condición que contribuye a que algo ocurra", "Así se define en el vocabulario.")],
    op=("Dibuja un esquema con «democratización en Chile» al centro. A la izquierda escribe tres causas de la ficha, a la derecha dos cambios y abajo dos continuidades. Después escribe una oración con «contribuyó a…» sobre una de las causas, sin decir que fue la única. {F}",
        "Causas: ciudades, sindicatos, MEMCH. Cambios: voto pleno de las mujeres (1949), radio y cine en barrios. Continuidades: desigualdad ciudad-campo, leyes civiles limitantes. Oración: «La organización de las mujeres contribuyó a lograr el pleno derecho a voto en 1949».",
        ["distingue causas, cambios y continuidades", "incluye al menos dos continuidades", "evita la causa única"], ["esquema", "oración con «contribuyó a…»"], ["poner un cambio como causa", "decir «la causa fue solo…»"],
        "Pide que explique por qué un orden en el tiempo no basta para probar una causa."),
    reinforce="Explica en voz alta un cambio y una continuidad de tu barrio en los últimos años.",
    extend="Elige una causa de la ficha y escribe qué fuente de la época servirá para comprobar su influencia.",
)

# ================================================================ OA 07, clase 5
F = ("Ficha 5 (dossier para construir una interpretación; hechos y fuentes de ejemplo). "
     "Hechos: voto municipal de las mujeres, 1934; MEMCH, 1935; Frente Popular, 1938; ley de pleno voto femenino, 1949; primera elección presidencial con mujeres, 1952; primeras transmisiones de radio, 1922. "
     "Fuente B de ejemplo, acta de una organización de mujeres, 1947: «Acordamos reunir firmas para exigir el voto en las elecciones presidenciales y parlamentarias.» "
     "Fuente D de ejemplo, carta de un profesor de liceo, 1951: «Con la radio, mis alumnos de barrio conocen debates que antes no escuchaban.» "
     "Fuente E de ejemplo, testimonio de una trabajadora agrícola, 1951: «Aquí nadie nos explicó cómo inscribirnos para votar.» "
     "Pregunta: ¿cómo contribuyeron nuevos actores y cultura de masas a democratizar Chile a mediados del siglo XX?")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada: una tesis clara, apoyada en dos evidencias, con un límite declarado y sin exagerar.",
    prior=["Sé interrogar fuentes y comparar perspectivas.", "Sé distinguir causas, cambios y continuidades.", "Sé que una conclusión debe ser proporcional a la evidencia."],
    explain=[
        "Una interpretación documentada es una respuesta a una pregunta histórica sostenida con evidencia. Tiene cuatro partes: una tesis (lo que afirmas), al menos dos evidencias (fuentes o hechos que la apoyan), un límite (lo que tus fuentes no permiten afirmar) y una conexión clara entre la evidencia y la tesis. Una tesis no es un dato: es una afirmación que se puede discutir.",
        "Una buena tesis es proporcional. «Las mujeres y la radio ampliaron la participación, aunque de forma desigual» se puede sostener con la ficha; «todos participaban por igual» no, porque la trabajadora agrícola dice que nadie le explicó cómo inscribirse. La evidencia contraria no se esconde: se usa para matizar la tesis.",
        "Para conectar tesis y evidencia se usan expresiones como «esto muestra que», «sin embargo», «aunque» y «en cambio». Se citan las fuentes con su procedencia. Y al final se declara el límite: qué otra fuente o qué escala falta. Una interpretación honesta reconoce que podría cambiar si aparece nueva evidencia.",
    ],
    vocab=[("tesis", "afirmación que se defiende con evidencia"), ("evidencia", "fuente o hecho que apoya una afirmación"), ("matizar", "precisar una afirmación para que no sea demasiado general"), ("proporcional", "que no dice más de lo que la evidencia permite"), ("límite", "lo que las fuentes disponibles no permiten afirmar")],
    worked=[
        ("Distinguir tesis y dato", "«El Estadio Nacional se inauguró en 1938». ¿Es una tesis o un dato?", ["Se puede comprobar en una fecha.", "No es una afirmación que haya que defender con argumentos."], "Es un dato"),
        ("Matizar una tesis", "«Todos los chilenos escuchaban radio». Reescríbela con más prudencia.", ["Agrego un grupo o un lugar.", "Uso «muchos» y un lugar: «En barrios de ciudad, muchas personas escuchaban radio»."], "«En barrios de ciudad, muchas personas escuchaban radio»"),
    ],
    mistakes=[("Escribir una tesis que es solo un dato.", "Se piensa que mencionar un hecho ya es interpretar.", "Formula una afirmación sobre cómo o por qué ocurrió algo y apóyala con evidencia."),
              ("Ocultar la fuente que contradice la tesis.", "Se cree que una evidencia contraria debilita el trabajo.", "Úsala para matizar la tesis y declarar un límite.")],
    T=[
        ("{F} ¿En qué año ocurrió la primera elección presidencial con mujeres votando?", "1952", "La ficha lo indica."),
        ("{F} ¿Qué dice la Fuente E sobre la inscripción para votar?", "Que nadie les explicó cómo inscribirse", "La trabajadora agrícola lo afirma en el testimonio."),
        ("{F} ¿Qué fuente muestra el efecto de la radio en alumnos de barrio?", "La Fuente D, carta de un profesor de liceo", "La carta dice que los alumnos conocen debates gracias a la radio."),
        ("{F} ¿Cuál es una tesis? A) Las organizaciones de mujeres y la radio ampliaron la participación, aunque de forma desigual B) La ley de pleno voto fue en 1949", "A) Las organizaciones de mujeres y la radio ampliaron la participación, aunque de forma desigual", "Es una afirmación que se puede discutir y apoyar con evidencia; B es un dato."),
        ("{F} ¿Qué evidencia apoya que las mujeres se organizaron para pedir el voto? A) La Fuente B B) La Fuente D", "A) La Fuente B", "El acta registra el acuerdo de reunir firmas."),
        ("{F} ¿Qué evidencia matiza que la participación fuera igual para todas las personas? A) La Fuente E B) La Fuente B", "A) La Fuente E", "La trabajadora agrícola describe una dificultad para inscribirse."),
        ("{F} Un compañero escribe: «Gracias a la radio, todos los chilenos conocían los debates». ¿Cómo la matizas? A) «En barrios de ciudad, la radio permitió a muchas personas conocer debates» B) «Nadie conocía los debates»", "A) «En barrios de ciudad, la radio permitió a muchas personas conocer debates»", "Delimita el lugar y la cantidad, como lo permite la Fuente D."),
        ("{F} ¿Qué conector sirve para introducir la Fuente E después de la Fuente D? A) Sin embargo B) Por ejemplo", "A) Sin embargo", "La Fuente E muestra un límite frente a la visión optimista de la D."),
        ("{F} ¿Qué límite es honesto declarar? A) Las fuentes son ejemplos aislados y no permiten afirmar cómo fue en todo el país B) Las fuentes prueban lo que ocurrió en todo el país", "A) Las fuentes son ejemplos aislados y no permiten afirmar cómo fue en todo el país", "Tres fuentes no representan la escala nacional."),
        ("{F} ¿Por qué no se debe ocultar la Fuente E si la tesis es optimista?", "Porque la evidencia contraria permite matizar la tesis y declarar un límite", "Ignorarla haría la interpretación menos honesta y menos precisa."),
        ("{F} ¿Por qué la tesis «todos participaban por igual» no se sostiene con el dossier?", "Porque la Fuente E muestra una persona sin información para inscribirse", "Basta una evidencia clara contraria para que una tesis universal no se sostenga."),
        ("{F} ¿Cuál es la interpretación mejor documentada? A) Organizaciones de mujeres (Fuente B) y la radio (Fuente D) ampliaron la participación, pero hubo exclusiones (Fuente E) B) La democratización fue completa porque en 1949 hubo una ley", "A) Organizaciones de mujeres (Fuente B) y la radio (Fuente D) ampliaron la participación, pero hubo exclusiones (Fuente E)", "Usa tres evidencias y reconoce un límite."),
        ("{F} ¿Qué fuente nueva reforzaría más la tesis sobre mujeres y voto? A) Cifras de mujeres inscritas en 1952 B) Un aviso de una radio de 1952", "A) Cifras de mujeres inscritas en 1952", "Una cifra de inscripción mide directamente la participación."),
    ],
    ctx=("Una compañera escribe: «El sistema fue totalmente democrático desde 1949 porque había una ley». ¿Cómo la ayudas con lo aprendido? A) Que agregue la Fuente E y declare que una ley no asegura el acceso real B) Que cite más leyes de la misma época", "A) Que agregue la Fuente E y declare que una ley no asegura el acceso real", "La evidencia de exclusión matiza una conclusión demasiado general."),
    sc=[("En Historia: ¿qué es una tesis?", "Una afirmación que se defiende con evidencia", "Así se define en la clase."),
        ("En Historia: ¿qué es matizar?", "Precisar una afirmación para que no sea demasiado general", "Así lo define el vocabulario."),
        ("¿Qué partes tiene una interpretación documentada?", "Tesis, evidencias, límite y conexión entre evidencia y tesis", "Son las cuatro partes de la explicación.")],
    op=("Escribe un párrafo de 5 líneas que responda la pregunta de la ficha. Línea 1: tu tesis. Líneas 2 y 3: dos evidencias con la fuente nombrada. Línea 4: una evidencia contraria o un matiz. Línea 5: un límite. Usa dos conectores como «esto muestra que» y «sin embargo». {F}",
        "Tesis: «Las organizaciones de mujeres y la radio contribuyeron a ampliar la participación». Evidencias: Fuente B y Fuente D. Matiz: Fuente E muestra exclusión. Límite: son tres fuentes y no representan todo el país.",
        ["tesis proporcional", "dos evidencias con fuente", "matiz o evidencia contraria", "límite declarado"], ["párrafo de cinco líneas"], ["escribir un dato como tesis", "no citar la fuente", "usar «todos» sin evidencia"],
        "Pide que subraye la tesis, las evidencias y el límite con tres colores."),
    reinforce="Cuenta en una frase tu tesis a alguien de tu casa y da una evidencia que la apoye.",
    extend="Busca qué otro actor social de mediados del siglo XX no aparece en la ficha y escribe cómo lo investigarías.",
)

# ================================================================ OA 07, clase 6
F = ("Ficha 6 (debate; posiciones de ejemplo escritas para este cuaderno). "
     "Tema: ¿la expansión de la radio, el cine y el deporte democratizó a Chile o solo entretuvo mientras seguían las desigualdades? "
     "Posición 1: «La radio informó a barrios que antes no recibían noticias y el deporte reunió a personas de distintos grupos; eso fortaleció la participación.» "
     "Posición 2: «La cultura de masas distraía de los problemas; mientras tanto, trabajadores del campo seguían sin organización ni acceso a servicios.» "
     "Hechos: las mujeres tuvieron pleno derecho a voto en 1949; el Estadio Nacional se inauguró en 1938; la desigualdad entre ciudad y campo se mantuvo. "
     "Reglas del debate: argumentar con evidencia, escuchar la posición contraria y reconocer los límites de la propia.")
build(
    OA, 6, F,
    use="Aprenderé a debatir con respeto las consecuencias y los límites de la democratización de mediados del siglo XX, con argumentos, evidencia y reconocimiento de la posición contraria.",
    prior=["Sé construir una tesis con evidencia.", "Sé distinguir causas, cambios y continuidades.", "Sé que opinar no es lo mismo que argumentar."],
    explain=[
        "Un argumento tiene una afirmación, una razón y una evidencia. «La radio fortaleció la participación (afirmación), porque informó a barrios que no recibían noticias (razón), como muestra el estadio inaugurado en 1938 (evidencia).» Un debate no busca ganar, sino comprender mejor un problema contrastando argumentos.",
        "Una contraargumentación responde a la posición contraria sin atacar a la persona. Se reconoce lo que la otra posición acierta («es cierto que el campo seguía desigual») y luego se matiza («pero la radio también llegó a algunos barrios populares»). Atacar a quien opina, por ejemplo diciendo «eres ingenuo», es una falacia: no responde a la idea.",
        "Evaluar consecuencias y límites significa decir qué logró un proceso y qué quedó pendiente. Para la democratización de mediados del siglo XX: el voto pleno de las mujeres y el acceso a medios de comunicación fueron avances reales; la desigualdad entre ciudad y campo fue un límite. Una postura madura puede combinar ambas ideas.",
    ],
    vocab=[("argumento", "afirmación apoyada en una razón y una evidencia"), ("contraargumento", "respuesta que cuestiona o matiza el argumento de otra posición"), ("falacia", "razonamiento engañoso, como atacar a la persona en vez de a su idea"), ("consecuencia", "efecto de un proceso"), ("matiz", "precisión que evita una afirmación extrema")],
    worked=[
        ("Armar un argumento", "Afirmación: «El deporte reunió a personas de distintos grupos». ¿Qué falta para que sea un argumento completo?", ["Tiene afirmación.", "Falta la razón y una evidencia."], "Una razón y una evidencia, por ejemplo el Estadio Nacional abierto al público"),
        ("Detectar una falacia", "Alguien responde: «Eso lo dice un ingenuo». ¿Es un buen contraargumento?", ["No discute la idea.", "Ataca a la persona."], "No, es una falacia contra la persona"),
    ],
    mistakes=[("Responder a una posición atacando a quien la dice.", "Se confunde ganar la discusión con comprender el problema.", "Responde a la idea con una razón y una evidencia."),
              ("Defender solo los avances sin mencionar los límites.", "Se cree que reconocer un límite debilita la postura.", "Incluye lo que quedó pendiente: eso la hace más sólida.")],
    T=[
        ("{F} ¿En qué año tuvieron las mujeres pleno derecho a voto?", "1949", "La ficha lo indica."),
        ("{F} ¿Qué dice la Posición 2 sobre los trabajadores del campo?", "Que seguían sin organización ni acceso a servicios", "La ficha lo indica."),
        ("{F} ¿Qué tres partes tiene un argumento?", "Afirmación, razón y evidencia", "Así se explica en la clase."),
        ("{F} La Posición 1 dice que la radio informó a barrios que antes no recibían noticias. ¿Qué parte del argumento es esa frase? A) La razón B) La afirmación final de todo el debate", "A) La razón", "Explica por qué la radio fortaleció la participación."),
        ("{F} ¿Qué hecho de la ficha usa la Posición 2 para sostener que persistían desigualdades? A) La desigualdad entre ciudad y campo B) El Estadio Nacional", "A) La desigualdad entre ciudad y campo", "Es el hecho que la ficha presenta como continuidad."),
        ("{F} Un participante responde: «Es cierto que el campo seguía desigual, pero la radio llegó a algunos barrios populares». ¿Qué hace? A) Reconoce un acierto y matiza B) Ataca a la persona", "A) Reconoce un acierto y matiza", "Acepta una parte de la posición contraria y agrega una precisión."),
        ("{F} Alguien dice: «Quien defiende la radio no sabe de historia». ¿Qué es eso? A) Una falacia contra la persona B) Un contraargumento con evidencia", "A) Una falacia contra la persona", "No discute la idea sino a quien opina."),
        ("{F} ¿Qué evidencia apoya mejor que hubo un avance real en participación? A) El pleno derecho a voto de las mujeres en 1949 B) La opinión de un locutor de radio", "A) El pleno derecho a voto de las mujeres en 1949", "Un derecho legal amplía directamente la participación política."),
        ("{F} ¿Qué evidencia usa mejor la Posición 2 para hablar de límites? A) La desigualdad entre ciudad y campo se mantuvo B) El Estadio Nacional se inauguró en 1938", "A) La desigualdad entre ciudad y campo se mantuvo", "Muestra algo que no cambió."),
        ("{F} ¿Por qué una postura que combina avances y límites es más sólida?", "Porque considera toda la evidencia y no oculta lo que quedó pendiente", "Reconocer los límites hace la conclusión más precisa."),
        ("{F} Un compañero afirma: «Como había radio, el campo ya era democrático». ¿Qué contraargumento sirve? A) La ficha dice que la desigualdad con la ciudad se mantuvo B) Pocas personas escuchaban radio, lo sé porque me lo dijeron", "A) La ficha dice que la desigualdad con la ciudad se mantuvo", "Usa evidencia verificable en lugar de una afirmación sin fuente."),
        ("{F} ¿Cuál de estas posturas final es más equilibrada? A) La cultura de masas y el voto amplió la participación, aunque persistieron desigualdades entre ciudad y campo B) La cultura de masas fue solo distracción", "A) La cultura de masas y el voto amplió la participación, aunque persistieron desigualdades entre ciudad y campo", "Reconoce avances y límites con base en los hechos de la ficha."),
        ("{F} ¿Qué haría más honesto un debate de ejemplo entre las Posiciones 1 y 2? A) Que cada una cite una fuente y reconozca un punto fuerte de la otra B) Que cada posición repita su tesis con más fuerza", "A) Que cada una cite una fuente y reconozca un punto fuerte de la otra", "Un debate de calidad se basa en evidencia y escucha, no en volumen."),
    ],
    ctx=("En un debate de curso, una persona dice: «La democratización fue un fracaso porque quedó desigualdad». ¿Qué respuesta usa mejor lo aprendido? A) Reconocer la desigualdad, pero mostrar avances como el voto pleno de 1949 B) Decir que quien opina eso exagera", "A) Reconocer la desigualdad, pero mostrar avances como el voto pleno de 1949", "Contrasta con evidencia y matiza sin atacar a la persona."),
    sc=[("En Historia: ¿qué es una falacia?", "Un razonamiento engañoso, como atacar a la persona en vez de a su idea", "Así se define en el vocabulario."),
        ("¿Qué partes tiene un argumento?", "Afirmación, razón y evidencia", "Son las tres partes de la explicación."),
        ("¿Qué hace un contraargumento respetuoso?", "Reconoce lo acertado de la otra posición y luego la matiza con evidencia", "Así se describe en la clase.")],
    op=("Prepara un mini debate escrito. Elige la Posición 1 o la 2 de la ficha y escribe un argumento de tres partes (afirmación, razón y evidencia). Luego escribe un contraargumento a la otra posición que reconozca algo cierto y lo matice. Cierra con una frase que diga qué avance y qué límite tuvo la democratización de mediados del siglo XX. {F}",
        "Posición 1: afirmación «la radio y el deporte fortalecieron la participación»; razón «informaron a barrios sin noticias y reunieron a personas de distintos grupos»; evidencia «el Estadio Nacional se inauguró en 1938». Contraargumento: «Es cierto que el campo seguía desigual, pero…». Cierre: avance, el pleno voto de 1949; límite, la desigualdad ciudad-campo.",
        ["argumento con tres partes", "contraargumento sin atacar a la persona", "avance y límite en el cierre"], ["argumento escrito", "contraargumento", "frase de cierre"], ["atacar a la persona", "omitir el límite", "usar una opinión como evidencia"],
        "Pide que lea el argumento a otra persona y que esa persona diga qué evidencia usó."),
    reinforce="Explica a alguien de tu casa la diferencia entre una opinión y un argumento con evidencia.",
    extend="Escribe un contraargumento a la frase «la cultura de masas solo entretiene» usando una evidencia de esta clase.",
)

OA = "HI2M OA 08"

# ================================================================ OA 08, clase 1
F = ("Ficha 1 (la Guerra Fría va de 1945 a 1991 aproximadamente: tensión entre dos superpotencias sin guerra directa entre ellas). "
     "Hitos: 1945 termina la Segunda Guerra Mundial y Estados Unidos lanza bombas atómicas sobre Hiroshima y Nagasaki; 1949 la URSS prueba su primera bomba atómica y se funda la OTAN, alianza militar liderada por Estados Unidos; "
     "1955 se crea el Pacto de Varsovia, alianza liderada por la URSS; 1962 crisis de los misiles en Cuba; 1991 desaparece la URSS. "
     "Dos proyectos: bloque occidental, con democracia liberal y economía de mercado; bloque soviético, con partido único y economía planificada por el Estado.")
build(
    OA, 1, F,
    use="Aprenderé a situar la Guerra Fría en el tiempo y entre sus actores: quiénes eran las superpotencias, qué proyectos opuestos defendían y por qué la amenaza nuclear la hizo distinta.",
    prior=["Sé que la Segunda Guerra Mundial terminó en 1945.", "Sé calcular diferencias entre años.", "Sé qué es una ideología."],
    explain=[
        "La Guerra Fría fue una confrontación entre dos superpotencias, Estados Unidos y la Unión Soviética (URSS), desde 1945 hasta 1991 aproximadamente. Se llama «fría» porque ellas nunca se enfrentaron directamente en una guerra abierta. Cada una lideraba un bloque, es decir, un grupo de países aliados: el occidental y el soviético.",
        "Los dos proyectos eran antagónicos, o sea, opuestos. El occidental defendía la democracia liberal y la economía de mercado; el soviético, un partido único y una economía planificada por el Estado. Una ideología es un conjunto de ideas sobre cómo debe organizarse la política y la economía. Cada bloque quería extender la suya.",
        "Lo nuevo fue la amenaza nuclear. Desde 1949 ambas potencias tenían bombas atómicas, y usarlas habría destruido a todos. Por eso la tensión se vivía como miedo permanente y se evitó el choque directo. Aun así, la rivalidad apareció en muchos lugares del mundo: en la política, la ciencia, el deporte y la cultura.",
    ],
    vocab=[("superpotencia", "país con enorme poder militar, económico y político a escala mundial"), ("bloque", "grupo de países aliados bajo el liderazgo de una superpotencia"), ("antagónico", "opuesto, que no puede convivir fácilmente con el otro"), ("ideología", "conjunto de ideas sobre cómo organizar la política y la economía"), ("amenaza nuclear", "riesgo de que se usen armas atómicas con efectos devastadores")],
    worked=[
        ("Calcular un intervalo", "¿Cuántos años pasaron entre la creación de la OTAN (1949) y la del Pacto de Varsovia (1955)?", ["Tomo los dos años de la ficha.", "Resto: 1955 − 1949 = 6."], "6 años"),
        ("Asignar un bloque", "Un país de ejemplo tiene partido único y economía planificada por el Estado. ¿A qué proyecto se parece?", ["Compara con las dos descripciones.", "Esa combinación es la del proyecto soviético."], "Bloque soviético"),
    ],
    mistakes=[("Creer que la Guerra Fría fue una guerra directa entre Estados Unidos y la URSS.", "Se interpreta «guerra» como combate entre ellas.", "Recuerda que fue una confrontación sin enfrentamiento directo."),
              ("Decir que la Guerra Fría fue solo una disputa militar.", "Se ignoran las ideologías y los demás ámbitos.", "Incluye también política, economía, ciencia, deporte y cultura.")],
    T=[
        ("{F} ¿Qué años delimitan aproximadamente la Guerra Fría?", "1945 y 1991", "La ficha la ubica entre el fin de la Segunda Guerra Mundial y la desaparición de la URSS."),
        ("{F} ¿Qué alianza militar fundó Estados Unidos en 1949?", "La OTAN", "La ficha la describe como alianza liderada por Estados Unidos."),
        ("{F} ¿Qué se creó en 1955 bajo el liderazgo de la URSS?", "El Pacto de Varsovia", "La ficha lo nombra como alianza militar soviética."),
        ("=", "{F} ¿Cuántos años duró la Guerra Fría, desde el fin de la Segunda Guerra hasta la desaparición de la URSS?", "1991-1945", "Se resta el año de inicio al año de término.", " años"),
        ("{F} ¿Qué dos rasgos tenía el proyecto soviético, según la ficha?", "Partido único y economía planificada por el Estado", "La ficha los describe así."),
        ("{F} ¿Por qué se llama «fría» a esta guerra? A) Porque las dos superpotencias no se enfrentaron directamente en una guerra abierta B) Porque fue una disputa solo económica, sin armas ni conflictos", "A) Porque las dos superpotencias no se enfrentaron directamente en una guerra abierta", "La ficha dice que fue una tensión sin guerra directa entre ellas."),
        ("{F} Un país de ejemplo tiene elecciones libres con varios partidos y economía de mercado. ¿Con qué bloque se identifica? A) Occidental B) Soviético", "A) Occidental", "Democracia liberal y economía de mercado son el proyecto occidental."),
        ("{F} Un país de ejemplo tiene un solo partido y el Estado planifica la economía. ¿Con qué bloque se identifica? A) Soviético B) Occidental", "A) Soviético", "Partido único y economía planificada son rasgos del proyecto soviético."),
        ("{F} ¿Qué hecho de 1962 muestra que la tensión llegó a su punto máximo en América? A) La crisis de los misiles en Cuba B) La creación de la OTAN", "A) La crisis de los misiles en Cuba", "Ocurrió en Cuba, en América, y es el momento de mayor riesgo nuclear de la ficha."),
        ("{F} ¿Por qué la amenaza nuclear impidió una guerra directa entre las superpotencias?", "Porque ambas tenían bombas atómicas y usarlas habría destruido a las dos", "Con armas nucleares en ambos lados, atacar significaba destruirse."),
        ("{F} Un compañero dice: «La Guerra Fría fue solo una disputa entre ejércitos». ¿Qué corrección haces? A) También fue ideológica y llegó a la política, la ciencia, el deporte y la cultura B) Tiene razón, porque había alianzas militares", "A) También fue ideológica y llegó a la política, la ciencia, el deporte y la cultura", "Las alianzas militares eran solo una parte de una confrontación de proyectos."),
        ("¿Cuál es la mejor pregunta para investigar este tema? A) ¿Cómo la rivalidad entre dos proyectos opuestos y la amenaza nuclear afectaron al mundo entre 1945 y 1991? B) ¿Qué superpotencia tenía más ciudades?", "A) ¿Cómo la rivalidad entre dos proyectos opuestos y la amenaza nuclear afectaron al mundo entre 1945 y 1991?", "La pregunta A tiene tiempo, actores y se responde con hechos; la B no ayuda a explicar el proceso."),
        ("{F} ¿Qué dato de la ficha sostiene mejor que la tensión se volvió nuclear desde 1949? A) La URSS prueba su primera bomba atómica B) Se crea el Pacto de Varsovia", "A) La URSS prueba su primera bomba atómica", "Desde ese año ambas superpotencias tenían armas atómicas."),
    ],
    ctx=("Un afiche escolar dice: «En 1945 comenzó una guerra entre soldados de Estados Unidos y la URSS». ¿Qué problema tiene? A) Presenta como guerra directa algo que fue una confrontación sin choque abierto B) Usa un año equivocado para el inicio", "A) Presenta como guerra directa algo que fue una confrontación sin choque abierto", "La ficha indica que las superpotencias no se enfrentaron directamente."),
    sc=[("En Historia: ¿qué es un bloque en la Guerra Fría?", "Un grupo de países aliados bajo el liderazgo de una superpotencia", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es una ideología?", "Un conjunto de ideas sobre cómo organizar la política y la economía", "Así se explica en la clase."),
        ("En Historia: ¿qué es una superpotencia?", "Un país con enorme poder militar, económico y político a escala mundial", "Así se define en el vocabulario.")],
    op=("Dibuja una línea de tiempo de 1945 a 1991 con escala 1 cm = 10 años (mide 4,6 cm). Marca con una raya los cinco hitos de la ficha. Debajo haz dos columnas, «bloque occidental» y «bloque soviético», y escribe en cada una su alianza y dos rasgos de su proyecto. {F}",
        "Posiciones desde 1945: 0 cm (1945); 0,4 cm (1949); 1 cm (1955); 1,7 cm (1962); 4,6 cm (1991). Occidental: OTAN, democracia liberal, economía de mercado. Soviético: Pacto de Varsovia, partido único, economía planificada.",
        ["respeta la escala", "ubica los cinco hitos", "asigna bien alianzas y rasgos a cada bloque"], ["línea de tiempo dibujada", "dos columnas completas"], ["poner los hitos sin medir", "mezclar rasgos de los dos bloques"],
        "Pide que explique por qué la ficha dice «sin guerra directa» y qué lo impidió."),
    reinforce="Explica en voz alta qué significa «fría» en la Guerra Fría y qué dos proyectos se enfrentaban.",
    extend="Escribe una frase que explique por qué la bomba atómica cambió la manera de pensar la guerra.",
)

# ================================================================ OA 08, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, afiche de un gobierno occidental, 1952: «Libertad y mercado libre: el camino del mundo libre. No deje que el comunismo avance.» "
     "Fuente B, afiche de un gobierno del bloque soviético, 1952: «El pueblo trabajador construye la paz. El capitalismo trae la guerra.» "
     "Fuente C, informe de un científico de un país que no pertenecía a ningún bloque (país no alineado), 1960: «Cada nueva bomba aumenta el riesgo para toda la humanidad, sin importar el bloque.» "
     "Preguntas de procedencia: ¿quién la produjo?, ¿cuándo?, ¿para quién?, ¿con qué propósito?")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes de la Guerra Fría con su procedencia, a reconocer la propaganda y a decir qué pueden probar y qué no.",
    prior=["Sé qué fueron los dos bloques de la Guerra Fría.", "Sé las cuatro preguntas de procedencia.", "Sé distinguir un dato de una opinión."],
    explain=[
        "En la Guerra Fría cada bloque trataba de convencer al mundo de que su proyecto era el mejor. Una forma era la propaganda: mensajes pensados para influir en la opinión pública, que muestran solo lo que conviene a quien los produce. Los afiches A y B de la ficha son propaganda de ejemplo: cada uno presenta al otro bloque como una amenaza.",
        "Al interrogar una fuente se pregunta quién la produjo, cuándo, para quién y con qué propósito. Un afiche de gobierno busca persuadir; no es un informe neutral. Observa también el lenguaje: palabras como «libertad» o «paz» suenan positivas y se usan para ganar apoyo. Eso no significa que sean falsas, sino que hay que contrastarlas con hechos.",
        "Un país no alineado es uno que no integraba ninguno de los dos bloques. La Fuente C fue escrita por un científico de un país no alineado, y por eso ofrece otra perspectiva: se preocupa por la humanidad, no por un bloque. Aun así, es una sola voz. Una buena conclusión usa varias fuentes de distinta procedencia y declara sus límites.",
    ],
    vocab=[("propaganda", "mensaje pensado para influir en la opinión pública y mostrar solo lo que conviene a quien lo produce"), ("persuadir", "convencer a alguien de una idea"), ("país no alineado", "país que no integraba ninguno de los dos bloques de la Guerra Fría"), ("lenguaje cargado", "palabras elegidas para provocar una emoción o ganar apoyo"), ("contrastar", "comparar varias fuentes para ver en qué coinciden y en qué no")],
    worked=[
        ("Reconocer el propósito", "Un afiche de ejemplo dice: «Apoye a nuestro bloque». ¿Cuál es su propósito?", ["Pide apoyo político.", "Intenta convencer, no informar con neutralidad."], "Persuadir"),
        ("Detectar lenguaje cargado", "En «el mundo libre frente a la amenaza roja», ¿qué palabra busca provocar miedo?", ["Busca una palabra con carga emocional.", "«Amenaza» provoca temor."], "«Amenaza»"),
    ],
    mistakes=[("Creer lo que dice un afiche porque tiene fecha y autor.", "Se confunde procedencia conocida con información neutral.", "Pregunta por el propósito y contrasta con hechos y otras fuentes."),
              ("Concluir que un solo bloque mentía y el otro decía la verdad.", "Se usa una fuente propagandística como juez final.", "Analiza qué dice cada una, qué omite y con qué propósito.")],
    T=[
        ("{F} ¿En qué año se produjeron los afiches A y B?", "1952", "La ficha lo indica."),
        ("{F} ¿Quién produjo la Fuente C?", "Un científico de un país no alineado", "La ficha da esa procedencia."),
        ("{F} ¿Qué dice la Fuente B sobre el capitalismo?", "Que trae la guerra", "La frase está en el afiche."),
        ("{F} ¿Cuál es el propósito principal de las Fuentes A y B? A) Persuadir al público de apoyar su proyecto B) Informar con neutralidad", "A) Persuadir al público de apoyar su proyecto", "Son afiches de gobiernos de cada bloque."),
        ("{F} ¿Qué es un país no alineado? A) Uno que no integraba ninguno de los dos bloques B) Uno que pertenecía a los dos bloques", "A) Uno que no integraba ninguno de los dos bloques", "Así se define en el vocabulario."),
        ("{F} ¿Qué palabra de la Fuente A busca sonar positiva para ganar apoyo? A) Libertad B) Comunismo", "A) Libertad", "Es una palabra con carga positiva que valida el mensaje."),
        ("{F} Un compañero dice: «La Fuente A prueba que el comunismo era una amenaza real». ¿Qué límite tiene su afirmación? A) Es propaganda de un gobierno y no una prueba neutral B) Es muy antigua", "A) Es propaganda de un gobierno y no una prueba neutral", "Un afiche muestra lo que el emisor quiere que se crea."),
        ("{F} ¿Qué perspectiva aporta la Fuente C que no tienen A y B? A) La preocupación por el riesgo para toda la humanidad B) La defensa de un bloque", "A) La preocupación por el riesgo para toda la humanidad", "El científico no habla desde un bloque."),
        ("{F} Para comparar cómo cada bloque se presentaba a sí mismo, ¿qué fuentes usas? A) A y B B) Solo C", "A) A y B", "Son los dos afiches, uno de cada bloque."),
        ("{F} ¿Por qué hay que contrastar una fuente de propaganda con otras antes de usarla como prueba?", "Porque muestra solo lo que conviene a quien la produce", "El emisor selecciona el mensaje con un propósito."),
        ("{F} Las Fuentes A y B se acusan mutuamente. ¿Qué conclusión es válida? A) Cada bloque presentaba al otro como amenaza para ganar apoyo B) Uno de los afiches dice la verdad completa", "A) Cada bloque presentaba al otro como amenaza para ganar apoyo", "La conclusión se limita a lo que ambas fuentes muestran."),
        ("{F} Quieres afirmar que «en la década de 1950 existía propaganda en ambos bloques». ¿Qué evidencia de la ficha usas y qué límite declaras? A) Los afiches A y B; son dos ejemplos y no muestran cuánta propaganda había B) Solo el afiche A; basta para demostrar que había propaganda en los dos bloques", "A) Los afiches A y B; son dos ejemplos y no muestran cuánta propaganda había", "Dos afiches ilustran la tesis pero no miden su alcance."),
        ("{F} ¿Qué fuente nueva ayudaría más a saber cuánto creía la gente en estos mensajes? A) Encuestas o testimonios de la época B) Otro afiche de 1952 de otro gobierno", "A) Encuestas o testimonios de la época", "Miden lo que pensaba el público, no lo que el gobierno decía."),
    ],
    ctx=("Una compañera cita el afiche A como prueba de cómo era la vida en el bloque soviético. ¿Qué le dices? A) Que un afiche del otro bloque no es una fuente confiable sobre ese tema sin contrastarla B) Que es mejor porque tiene fecha", "A) Que un afiche del otro bloque no es una fuente confiable sobre ese tema sin contrastarla", "El afiche A tiene un propósito y mira al otro bloque como adversario."),
    sc=[("En Historia: ¿qué es la propaganda?", "Un mensaje pensado para influir en la opinión pública y mostrar solo lo que conviene a quien lo produce", "Así se define en la clase."),
        ("En Historia: ¿qué es contrastar fuentes?", "Compararlas para ver en qué coinciden y en qué no", "Así se define en el vocabulario."),
        ("¿Qué preguntas de procedencia se hacen a una fuente?", "Quién la produjo, cuándo, para quién y con qué propósito", "Son las cuatro preguntas de la ficha.")],
    op=("Elige el afiche A o el B de la ficha y haz una tarjeta de análisis con: quién lo produjo, cuándo, para quién, con qué propósito, una palabra de lenguaje cargado y lo que NO puede probar. Luego escribe una frase que contraste ese afiche con la Fuente C. {F}",
        "Afiche A: gobierno occidental; 1952; público de su bloque; persuadir; palabra «libertad» o «comunismo avance»; no prueba cómo era la vida en el otro bloque. Frase: «A diferencia del afiche, el científico habla del riesgo para toda la humanidad».",
        ["responde las cuatro preguntas", "identifica lenguaje cargado", "declara un límite", "contrasta con la Fuente C"], ["tarjeta de análisis", "frase de contraste"], ["copiar el afiche sin analizarlo", "tomar la propaganda como prueba"],
        "Pide que explique por qué la Fuente C también es una sola voz y necesita contrastarse."),
    reinforce="Busca un aviso o mensaje actual y di su propósito y una palabra que busque persuadir.",
    extend="Escribe qué fuente de la época servirá para saber cuánta gente creía en los afiches de la ficha.",
)

# ================================================================ OA 08, clase 3
F = ("Ficha 3 (escalas global, regional y local; hechos). "
     "Escala global: la Guerra Fría enfrenta a Estados Unidos y la URSS. "
     "Escala regional: la guerra de Corea, 1950 a 1953, enfrenta a Corea del Norte, apoyada por la URSS y China, con Corea del Sur, apoyada por Estados Unidos y otros países; Cuba, 1959 revolución, 1962 crisis de los misiles; en 1961 Estados Unidos lanza la Alianza para el Progreso, un programa de ayuda a América Latina. "
     "Escala local, Chile: en 1948 una ley (Defensa Permanente de la Democracia) deja fuera de la ley al Partido Comunista, y se deroga en 1958; en 1964 Chile rompe relaciones con Cuba y las restablece en 1970. "
     "Perspectivas de ejemplo: Washington dice que busca contener el comunismo; Moscú dice que apoya a pueblos que luchan contra el capitalismo; el gobierno chileno de 1948 dice que defiende la democracia; críticos de la ley dicen que limitó libertades políticas.")
build(
    OA, 3, F,
    use="Aprenderé a comparar perspectivas y escalas de la Guerra Fría: cómo se vio desde las superpotencias, desde América Latina y desde Chile.",
    prior=["Sé qué fueron los dos bloques.", "Sé distinguir escalas local, regional y global.", "Sé interrogar fuentes con su procedencia."],
    explain=[
        "La Guerra Fría se vivió en distintas escalas. En la escala global, la rivalidad entre las superpotencias. En la regional, conflictos concretos como la guerra de Corea (1950 a 1953) o la crisis de los misiles en Cuba (1962). En la local, decisiones de cada país, como las leyes y relaciones diplomáticas de Chile. Un hecho local no se explica solo por lo local ni solo por lo global.",
        "A estos conflictos regionales se les llama a veces guerras por delegación o indirectas: las superpotencias no peleaban entre sí, sino que apoyaban a bandos contrarios en un tercer país. En algunos casos, como Corea, tropas de Estados Unidos combatieron directamente, pero ninguna de las dos superpotencias declaró la guerra a la otra. En América Latina, la rivalidad influyó en la política interna: gobiernos y partidos se alineaban o eran acusados de alinearse con un bloque.",
        "Cada actor tenía su perspectiva. Washington hablaba de contener el comunismo; Moscú, de apoyar a los pueblos contra el capitalismo; el gobierno chileno de 1948, de defender la democracia; y sus críticos, de libertades limitadas. Comparar no es elegir un bando, sino explicar qué argumento tenía cada uno y qué efecto tuvo.",
    ],
    vocab=[("guerra por delegación", "conflicto en un tercer país donde las superpotencias apoyan a bandos opuestos sin enfrentarse directamente"), ("contención", "política de Estados Unidos de frenar la expansión del comunismo"), ("proscribir", "declarar ilegal a un partido u organización"), ("relaciones diplomáticas", "vínculos oficiales entre los gobiernos de dos países"), ("escala regional", "nivel que abarca varios países de una zona")],
    worked=[
        ("Identificar la escala", "La ley chilena de 1948 que dejó fuera de la ley al Partido Comunista, ¿en qué escala se ubica?", ["Es una decisión de un solo país.", "Se aplica en Chile."], "Escala local"),
        ("Calcular una duración", "¿Cuántos años duró la guerra de Corea, según la ficha?", ["Tomo 1950 y 1953.", "1953 − 1950 = 3."], "3 años"),
    ],
    mistakes=[("Explicar un hecho chileno solo por decisiones de Chile.", "Se ignora la rivalidad global en que se inserta.", "Relaciona la escala local con la global sin perder las causas internas."),
              ("Pensar que las guerras por delegación eran guerras directas entre superpotencias.", "Se confunde apoyar con combatir entre sí.", "Recuerda que ellas apoyaban bandos en un tercer país.")],
    T=[
        ("{F} ¿Qué años abarcó la guerra de Corea según la ficha?", "De 1950 a 1953", "La ficha indica esas fechas."),
        ("{F} ¿Qué ley de 1948 aparece en la escala local?", "La Ley de Defensa Permanente de la Democracia", "La ficha la nombra y dice que dejó al Partido Comunista fuera de la ley."),
        ("{F} ¿Qué programa lanzó Estados Unidos en 1961 para América Latina?", "La Alianza para el Progreso", "La ficha lo describe como programa de ayuda."),
        ("{F} Según la ficha, ¿en qué escala se ubica la crisis de los misiles en Cuba? A) Regional, por ocurrir en América B) Local de Chile", "A) Regional, por ocurrir en América", "Afectó a una región, aunque involucró a las superpotencias."),
        ("{F} ¿Qué escala tiene la ruptura de relaciones de Chile con Cuba en 1964? A) Local B) Global", "A) Local", "Fue una decisión del Estado chileno."),
        ("{F} ¿A qué partido dejó fuera de la ley la ley chilena de 1948?", "Al Partido Comunista", "La ficha lo indica en la escala local."),
        ("{F} En Corea, la URSS y China apoyan a un bando y Estados Unidos al otro, sin enfrentarse entre sí. ¿Qué tipo de conflicto es? A) Una guerra por delegación B) Una guerra directa entre superpotencias", "A) Una guerra por delegación", "Las superpotencias apoyaban a bandos distintos en un tercer lugar."),
        ("{F} ¿Qué perspectiva de la ficha defiende la ley de 1948 como protección de la democracia? A) El gobierno chileno de 1948 B) Los críticos de la ley", "A) El gobierno chileno de 1948", "Así lo dice la ficha."),
        ("{F} Una frase dice: «Para frenar el comunismo, Estados Unidos ayuda a América Latina». ¿Qué perspectiva expresa? A) Washington B) Moscú", "A) Washington", "Contención del comunismo es la política de Estados Unidos."),
        ("{F} ¿Por qué no basta explicar la ley chilena de 1948 solo con causas internas?", "Porque también se insertó en la rivalidad global entre los bloques", "La ficha vincula decisiones locales con la Guerra Fría."),
        ("{F} Un compañero dice: «La guerra de Corea fue entre Estados Unidos y la URSS directamente». ¿Qué corrección haces? A) Las superpotencias apoyaron bandos, y no se enfrentaron directamente B) Tiene razón, porque ambas participaron", "A) Las superpotencias apoyaron bandos, y no se enfrentaron directamente", "La ficha muestra apoyos distintos a Corea del Norte y del Sur."),
        ("{F} ¿Qué comparación entre perspectivas es válida? A) Para el gobierno de 1948 la ley defendía la democracia; para sus críticos limitaba libertades B) La ley fue buena según todos", "A) Para el gobierno de 1948 la ley defendía la democracia; para sus críticos limitaba libertades", "Expone dos perspectivas distintas de la ficha."),
        ("{F} ¿Qué dato permite sostener que la política chilena hacia Cuba cambió con el tiempo? A) Se rompieron relaciones en 1964 y se restablecieron en 1970 B) Cuba hizo una revolución en 1959", "A) Se rompieron relaciones en 1964 y se restablecieron en 1970", "Muestra un cambio dentro de Chile en seis años."),
    ],
    ctx=("Una exposición dice: «La Guerra Fría fue algo que ocurría lejos de Chile». ¿Qué respuesta usa mejor la ficha? A) La ley de 1948 y la ruptura con Cuba en 1964 muestran efectos en Chile B) Chile era la potencia que dirigía uno de los bloques", "A) La ley de 1948 y la ruptura con Cuba en 1964 muestran efectos en Chile", "Hay decisiones chilenas ligadas a la rivalidad entre bloques."),
    sc=[("En Historia: ¿qué es una guerra por delegación?", "Un conflicto en un tercer país donde las superpotencias apoyan a bandos opuestos sin enfrentarse directamente", "Así se define en el vocabulario."),
        ("En Historia: ¿qué significa proscribir un partido?", "Declararlo ilegal", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es la contención?", "La política de Estados Unidos de frenar la expansión del comunismo", "Así se define en el vocabulario.")],
    op=("Haz un cuadro de tres filas: «global», «regional» y «local». En cada una escribe un hecho de la ficha. Luego elige dos perspectivas de la ficha y escribe una frase que las compare, por ejemplo el gobierno chileno de 1948 y sus críticos, sin decir cuál tiene la razón. {F}",
        "Global: rivalidad entre superpotencias. Regional: guerra de Corea o crisis de Cuba. Local: ley de 1948 o ruptura con Cuba en 1964. Frase: «El gobierno de 1948 defendió la democracia; en cambio, sus críticos dijeron que se limitaron libertades».",
        ["asigna bien las escalas", "compara dos perspectivas", "no toma partido sin evidencia"], ["cuadro de tres filas", "frase de comparación"], ["poner un hecho local en la escala global", "elegir el bando correcto sin evidencia"],
        "Pide que explique cómo un hecho local puede relacionarse con uno global."),
    reinforce="Explica en voz alta qué es una guerra por delegación y da un ejemplo de la ficha.",
    extend="Escribe una pregunta que le harías a una persona mayor sobre cómo se vivía la Guerra Fría en su barrio.",
)

# ================================================================ OA 08, clase 4
F = ("Ficha 4 (causas, cambios y continuidades; esferas de la vida afectadas). "
     "Causas: ideologías opuestas; desconfianza entre las superpotencias tras la Segunda Guerra; bombas atómicas desde 1945 y 1949. "
     "Ciencia: la URSS lanza el primer satélite artificial, Sputnik, en 1957; Yuri Gagarin es el primer ser humano en el espacio, 1961; Estados Unidos llega a la Luna con la misión Apolo 11, 1969. "
     "Deporte: Estados Unidos boicotea los Juegos Olímpicos de Moscú, 1980, y la URSS los de Los Ángeles, 1984. "
     "Política: el Muro de Berlín divide la ciudad entre 1961 y 1989. "
     "Cultura: películas, novelas y canciones usaron el miedo a un conflicto, o la crítica a uno de los bloques, como tema. "
     "Continuidades: la rivalidad ideológica y el riesgo nuclear se mantuvieron durante todo el período.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar las causas de la Guerra Fría con sus cambios y continuidades en la política, la ciencia, el deporte y la cultura.",
    prior=["Sé situar la Guerra Fría y sus bloques.", "Sé distinguir causa, cambio y continuidad.", "Sé que ocurrir antes no prueba una causa."],
    explain=[
        "Las causas de la Guerra Fría fueron la oposición entre dos ideologías, la desconfianza tras la Segunda Guerra Mundial y la existencia de armas atómicas. Cada bloque temía que el otro se expandiera. La carrera armamentista, es decir, la competencia por tener más y mejores armas, fue una consecuencia: cada avance de uno obligaba al otro a responder.",
        "La rivalidad cambió muchas esferas. En la ciencia, la carrera espacial: el Sputnik (1957), el vuelo de Gagarin (1961) y la llegada a la Luna (1969). En el deporte, los boicots olímpicos de 1980 y 1984. En la política, el Muro de Berlín (1961-1989). En la cultura, películas y novelas que trataban el miedo a la guerra. En todos los casos el prestigio del bloque estaba en juego.",
        "Hubo continuidades: la rivalidad ideológica y el riesgo nuclear acompañaron todo el período. Y hay que cuidar la causalidad: la carrera espacial no tuvo una sola causa, porque también movían la curiosidad científica y el prestigio. Decir que la Guerra Fría explica todo lo que pasó entre 1945 y 1991 es una exageración.",
    ],
    vocab=[("carrera armamentista", "competencia por tener más y mejores armas"), ("carrera espacial", "competencia entre superpotencias por logros en el espacio"), ("boicot", "negarse a participar en un evento como forma de protesta"), ("prestigio", "buena imagen y poder de influencia ante el mundo"), ("esfera", "ámbito de la vida social, como la política, la ciencia, el deporte o la cultura")],
    worked=[
        ("Calcular una distancia temporal", "¿Cuántos años pasaron entre el Sputnik (1957) y la llegada a la Luna (1969)?", ["Tomo los dos años de la ficha.", "Resto: 1969 − 1957 = 12."], "12 años"),
        ("Clasificar una esfera", "El boicot a unos Juegos Olímpicos, ¿en qué esfera se ubica?", ["Se trata de una competencia deportiva.", "Pero tiene motivo político."], "Deporte, con motivo político"),
    ],
    mistakes=[("Decir que la carrera espacial tuvo una sola causa: la Guerra Fría.", "Se ignoran otros factores, como el interés científico.", "Usa «contribuyó a» y menciona más de un factor."),
              ("Pensar que todo lo ocurrido entre 1945 y 1991 se explica por la Guerra Fría.", "Se atribuye a una causa todo un período.", "Distingue lo que la rivalidad explica de lo que tiene otras causas.")],
    T=[
        ("{F} ¿Qué logro científico soviético ocurrió en 1957?", "El lanzamiento del primer satélite artificial, Sputnik", "La ficha lo indica."),
        ("{F} ¿Quién fue el primer ser humano en el espacio según la ficha?", "Yuri Gagarin", "La ficha lo nombra en 1961."),
        ("{F} ¿Qué misión llegó a la Luna en 1969?", "Apolo 11", "La ficha la presenta como logro de Estados Unidos."),
        ("{F} ¿Qué dividió el Muro de Berlín, según la ficha?", "La ciudad de Berlín, entre 1961 y 1989", "La ficha lo indica en la esfera política."),
        ("{F} ¿Qué esfera muestra el boicot de 1980? A) El deporte B) La ciencia", "A) El deporte", "Se trata de los Juegos Olímpicos."),
        ("{F} ¿Qué esfera muestra el vuelo de Gagarin en 1961? A) La ciencia B) La cultura", "A) La ciencia", "Es un logro del programa espacial."),
        ("{F} Una novela de ejemplo cuenta cómo una familia vive con miedo a una guerra nuclear. ¿Qué esfera de la Guerra Fría muestra? A) La cultura B) La política", "A) La cultura", "Una novela es una obra cultural que usa el miedo a un conflicto."),
        ("{F} ¿Quién boicoteó los Juegos Olímpicos de Los Ángeles de 1984, según la ficha?", "La URSS", "La ficha lo indica en la esfera del deporte."),
        ("{F} ¿Qué es una continuidad según la ficha? A) El riesgo nuclear durante todo el período B) La llegada a la Luna en 1969", "A) El riesgo nuclear durante todo el período", "La ficha lo presenta como algo que se mantuvo."),
        ("{F} ¿Por qué se puede decir que la carrera espacial fue también una competencia de prestigio?", "Porque cada bloque quería mostrar que su sistema era superior ante el mundo", "El prestigio de cada proyecto estaba en juego en los logros científicos."),
        ("{F} Un compañero dice: «El Sputnik causó la Guerra Fría». ¿Qué corrección haces? A) No: la Guerra Fría empezó antes, en 1945, y el Sputnik fue una de sus manifestaciones B) Sí, porque ocurrió en el medio de la Guerra Fría", "A) No: la Guerra Fría empezó antes, en 1945, y el Sputnik fue una de sus manifestaciones", "La causa debe ocurrir antes que su efecto; el Sputnik es de 1957."),
        ("{F} ¿Qué relación causal es más sólida? A) La desconfianza entre las superpotencias contribuyó a la carrera armamentista B) La carrera armamentista causó que terminara la Segunda Guerra", "A) La desconfianza entre las superpotencias contribuyó a la carrera armamentista", "La causa ocurre antes y es coherente con la ficha."),
        ("{F} ¿Cuál es la mejor síntesis? A) La rivalidad cambió la ciencia, el deporte, la política y la cultura, pero sin explicar todo lo ocurrido en el período B) La Guerra Fría lo explica todo entre 1945 y 1991", "A) La rivalidad cambió la ciencia, el deporte, la política y la cultura, pero sin explicar todo lo ocurrido en el período", "Reconoce efectos en varias esferas y evita la causa única."),
    ],
    ctx=("Un noticiero de ejemplo dice: «Todo lo que pasó en el mundo entre 1945 y 1991 fue por la Guerra Fría». ¿Qué problema tiene? A) Atribuye a una sola causa un período entero B) Usa fechas incorrectas", "A) Atribuye a una sola causa un período entero", "La ficha muestra otros motivos, como la curiosidad científica."),
    sc=[("En Historia: ¿qué es una carrera armamentista?", "La competencia por tener más y mejores armas", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es un boicot?", "Negarse a participar en un evento como forma de protesta", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es la carrera espacial?", "La competencia entre superpotencias por logros en el espacio", "Así se define en el vocabulario.")],
    op=("Haz un cuadro con cuatro columnas: política, ciencia, deporte y cultura. En cada una escribe un hecho de la ficha (en cultura, una obra de ejemplo inventada por ti en una línea). Marca con una estrella una continuidad que aparezca en todas. Escribe una frase con «contribuyó a…» sobre una causa de la Guerra Fría. {F}",
        "Política: Muro de Berlín. Ciencia: Sputnik, Gagarin o Apolo 11. Deporte: boicots de 1980 y 1984. Cultura: una novela de ejemplo sobre el miedo. Continuidad: la rivalidad y el riesgo nuclear. Frase: «La desconfianza contribuyó a la carrera armamentista».",
        ["hecho correcto en cada columna", "continuidad bien identificada", "causa con verbo prudente"], ["cuadro completo", "frase con «contribuyó a…»"], ["poner una causa como hecho de la esfera", "decir que la Guerra Fría explica todo"],
        "Pide que explique otra causa del interés por el espacio además de la Guerra Fría."),
    reinforce="Explica en voz alta dos esferas en las que se notó la rivalidad entre las superpotencias.",
    extend="Busca en tu casa algo (juego, película, canción) que trate el miedo a una guerra y di a qué época pertenece.",
)

# ================================================================ OA 08, clase 5
F = ("Ficha 5 (dossier para construir una interpretación; hechos y fuentes de ejemplo). "
     "Hechos: la Guerra Fría va de 1945 a 1991 aproximadamente; la guerra de Corea, 1950 a 1953, y la guerra de Vietnam, que termina en 1975, fueron conflictos en que cada superpotencia respaldó a un bando distinto, sin declararse la guerra entre sí; "
     "crisis de los misiles en Cuba, 1962; la URSS y Estados Unidos nunca se enfrentaron en una guerra directa. "
     "Fuente F de ejemplo, informe de un periodista, 1953: «Las dos superpotencias se vigilan, pero los soldados mueren en Corea.» "
     "Fuente G de ejemplo, carta de una ciudadana de una gran ciudad, 1962: «Esta semana en mi barrio nadie dejó de hablar de un posible ataque; los niños practicaron cómo refugiarse en la escuela.» "
     "Pregunta: ¿fue «fría» la Guerra Fría?")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada sobre la Guerra Fría: una tesis proporcional, dos evidencias, un matiz y un límite.",
    prior=["Sé qué fue la Guerra Fría.", "Sé las partes de una interpretación documentada.", "Sé que una evidencia contraria sirve para matizar."],
    explain=[
        "Para responder si la Guerra Fría fue «fría» hay que usar evidencia. Una tesis posible: «Fue fría entre las superpotencias, que nunca se enfrentaron directamente, pero fue caliente para los países donde se combatió con su apoyo». Esa tesis tiene dos partes: lo que fue «frío» y lo que no lo fue, y por eso es más precisa que «fue fría» o «fue caliente».",
        "La evidencia de la ficha apoya la tesis. La ausencia de guerra directa y la crisis de 1962 muestran el riesgo sin choque abierto. Corea y Vietnam muestran guerras con muchas víctimas. La carta de la ciudadana (Fuente G) muestra otra dimensión: el miedo cotidiano, que no se mide solo con batallas. Todas las fuentes de ejemplo son voces aisladas.",
        "Una interpretación honesta declara sus límites: no sabemos cómo vivieron esos años todos los países ni cuántas personas sintieron miedo. Además, usa verbos prudentes («muestra», «sugiere») y evita expresiones como «todos» o «siempre». Si apareciera nueva evidencia, la tesis podría cambiar, y eso es normal en historia.",
    ],
    vocab=[("tesis", "afirmación que se defiende con evidencia"), ("proporcional", "que no dice más de lo que la evidencia permite"), ("matiz", "precisión que evita una afirmación extrema"), ("conflicto indirecto", "guerra donde las superpotencias apoyan bandos opuestos sin enfrentarse entre sí"), ("miedo cotidiano", "temor que las personas viven en su vida diaria")],
    worked=[
        ("Elegir una tesis más precisa", "¿Cuál es más precisa? A) «La Guerra Fría fue fría» B) «Fue fría entre las superpotencias y caliente donde se combatió con su apoyo»", ["La A no distingue lugares.", "La B reconoce dos situaciones."], "La B"),
        ("Calcular una duración", "¿Cuántos años pasaron entre el inicio de la guerra de Corea (1950) y el fin de la de Vietnam (1975)?", ["Tomo los dos años de la ficha.", "1975 − 1950 = 25."], "25 años"),
    ],
    mistakes=[("Usar una tesis tan general que nadie podría discutirla.", "Se cree que una frase segura es mejor.", "Haz una tesis que se pueda defender con evidencia y que diga algo concreto."),
              ("Generalizar una carta a todo el mundo.", "Se toma una voz como la de todos.", "Declara que es una fuente aislada y qué otra faltaría.")],
    T=[
        ("{F} ¿En qué años transcurrió la guerra de Corea?", "De 1950 a 1953", "La ficha lo indica."),
        ("{F} ¿En qué año ocurrió la crisis de los misiles?", "1962", "La ficha lo indica."),
        ("{F} ¿Qué dice la Fuente G sobre los niños?", "Que practicaron cómo refugiarse en la escuela", "La carta lo menciona."),
        ("{F} ¿Cuál es una tesis proporcional? A) Fue fría entre las superpotencias, que no se enfrentaron directamente, pero cálida para los países donde se combatió con su apoyo B) Fue fría en todas partes", "A) Fue fría entre las superpotencias, que no se enfrentaron directamente, pero cálida para los países donde se combatió con su apoyo", "Reconoce una parte «fría» y otra donde sí hubo combates."),
        ("{F} ¿Qué evidencia apoya que hubo guerras con víctimas bajo apoyo de las superpotencias? A) Corea y Vietnam B) La crisis de los misiles", "A) Corea y Vietnam", "La ficha las presenta como conflictos con apoyo a bandos opuestos."),
        ("{F} ¿Qué fuente muestra el miedo cotidiano? A) La Fuente G B) La Fuente F", "A) La Fuente G", "Describe cómo vivió una ciudadana la semana de la crisis."),
        ("{F} ¿Qué evidencia matiza la tesis de que fue una guerra solo «fría»? A) Los soldados que murieron en Corea, Fuente F B) La carta de la ciudadana", "A) Los soldados que murieron en Corea, Fuente F", "Muestra combates reales con víctimas."),
        ("{F} Un compañero escribe: «Todas las personas del mundo vivieron con miedo a un ataque en 1962». ¿Cómo lo matizas? A) «Una ciudadana de una gran ciudad cuenta que su barrio vivió miedo en 1962» B) «Nadie sintió miedo en 1962»", "A) «Una ciudadana de una gran ciudad cuenta que su barrio vivió miedo en 1962»", "Se limita a lo que la Fuente G permite afirmar."),
        ("{F} ¿Qué conector sirve para introducir la Fuente F después de decir que las superpotencias no se enfrentaron? A) Sin embargo B) Por lo tanto", "A) Sin embargo", "La Fuente F muestra un contraste: hubo muertes en otros lugares."),
        ("{F} ¿Por qué una tesis que solo dice «fue fría» sería poco precisa?", "Porque ignora los conflictos indirectos donde murió mucha gente", "La ficha incluye Corea y Vietnam."),
        ("{F} ¿Qué límite es honesto declarar? A) Una carta y un informe no permiten saber cómo lo vivió el mundo entero B) Las dos fuentes permiten conocer todos los países", "A) Una carta y un informe no permiten saber cómo lo vivió el mundo entero", "Son dos voces, no una muestra del mundo."),
        ("{F} ¿Cuál es la interpretación mejor documentada? A) Fue fría entre las superpotencias (sin guerra directa), cálida en Corea y Vietnam (Fuente F) y vivida con miedo en lo cotidiano (Fuente G) B) La Guerra Fría fue solo un miedo", "A) Fue fría entre las superpotencias (sin guerra directa), cálida en Corea y Vietnam (Fuente F) y vivida con miedo en lo cotidiano (Fuente G)", "Integra los hechos y las dos fuentes con un matiz."),
        ("{F} ¿Qué fuente nueva reforzaría más la tesis sobre el miedo cotidiano? A) Testimonios de personas de otras ciudades en 1962 B) Un informe técnico sobre misiles de 1962", "A) Testimonios de personas de otras ciudades en 1962", "Permitirían ver si el miedo era compartido."),
    ],
    ctx=("Un alumno escribe: «La Guerra Fría fue una época de paz porque no hubo guerra entre las superpotencias». ¿Qué le recomiendas? A) Agregar Corea y Vietnam y matizar su tesis B) Agregar más fechas del período", "A) Agregar Corea y Vietnam y matizar su tesis", "La paz entre las superpotencias no impidió guerras con su apoyo."),
    sc=[("En Historia: ¿qué es una tesis proporcional?", "Una afirmación que no dice más de lo que la evidencia permite", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es un conflicto indirecto?", "Una guerra donde las superpotencias apoyan bandos opuestos sin enfrentarse entre sí", "Así se define en la clase."),
        ("En Historia: ¿qué es un matiz?", "Una precisión que evita una afirmación extrema", "Así se define en el vocabulario.")],
    op=("Escribe un párrafo de 5 líneas que responda «¿fue fría la Guerra Fría?». Línea 1: tu tesis. Líneas 2 y 3: dos evidencias con su fuente. Línea 4: un matiz o evidencia contraria. Línea 5: un límite. Usa «sin embargo» y «esto muestra que». {F}",
        "Tesis: «Fue fría entre las superpotencias y cálida donde se combatió con su apoyo». Evidencias: no hubo guerra directa; Corea (Fuente F). Matiz: miedo cotidiano (Fuente G). Límite: son voces aisladas.",
        ["tesis proporcional", "dos evidencias con fuente", "matiz", "límite declarado"], ["párrafo de cinco líneas"], ["tesis demasiado general", "usar «todos» sin evidencia"],
        "Pide que cambie una palabra exagerada de su párrafo por una más prudente."),
    reinforce="Cuenta en una frase tu tesis a alguien de tu casa y da una evidencia que la apoye.",
    extend="Escribe qué segunda fuente buscarías para saber cómo se vivió la crisis de 1962 en América Latina.",
)

# ================================================================ OA 08, clase 6
F = ("Ficha 6 (debate; posiciones de ejemplo escritas para este cuaderno). "
     "Tema: ¿la amenaza nuclear evitó una guerra mundial o solo puso a la humanidad en riesgo? "
     "Posición 1: «Como ambas superpotencias podían destruirse, ninguna se atrevió a atacar; la amenaza nuclear mantuvo la paz entre ellas.» "
     "Posición 2: «Evitar el choque directo no fue paz: hubo guerras por delegación con muchas víctimas, y el mundo estuvo a un error de una catástrofe, como en 1962.» "
     "Hechos: las superpotencias no se enfrentaron directamente; Corea, 1950 a 1953; crisis de los misiles, 1962; la Guerra Fría termina hacia 1991. "
     "Reglas del debate: argumentar con evidencia, reconocer lo acertado de la otra posición y declarar los límites de la propia.")
build(
    OA, 6, F,
    use="Aprenderé a debatir con respeto las consecuencias y límites de la amenaza nuclear en la Guerra Fría, con argumentos, evidencia y reconocimiento de la posición contraria.",
    prior=["Sé construir una interpretación con evidencia.", "Sé distinguir causas, cambios y continuidades.", "Sé qué es una falacia."],
    explain=[
        "La disuasión nuclear es la idea de que un país no ataca a otro porque la respuesta sería devastadora. Para algunos, eso evitó una guerra directa entre las superpotencias; para otros, el costo fue demasiado alto: miedo permanente, gasto en armas, guerras en otros países y el riesgo de un accidente o error. El debate no tiene una respuesta única, pero sí mejores y peores argumentos.",
        "Un buen argumento tiene afirmación, razón y evidencia. «La amenaza nuclear evitó el choque directo (afirmación), porque ambas potencias sabían que se destruirían (razón), y nunca se enfrentaron directamente (evidencia).» Un buen contraargumento reconoce eso y matiza: «es cierto que no hubo choque directo, pero hubo guerras por delegación con muchas víctimas».",
        "Cuando se debaten consecuencias hay que separar corto y largo plazo, y quiénes pagaron el costo. Se evita atacar a las personas y se evita decir que algo era inevitable. Una postura madura puede decir: la amenaza nuclear contribuyó a evitar una guerra directa, y a la vez aumentó el riesgo y los costos para muchos países.",
    ],
    vocab=[("disuasión", "evitar que alguien actúe haciéndole temer una respuesta muy dañina"), ("argumento", "afirmación apoyada en una razón y una evidencia"), ("contraargumento", "respuesta que cuestiona o matiza el argumento de otra posición"), ("costo", "pérdida o daño que implica una decisión"), ("inevitable", "que no pudo haber ocurrido de otra manera")],
    worked=[
        ("Armar un argumento", "Afirmación: «La disuasión evitó el choque directo». ¿Qué falta para que sea un argumento completo?", ["Ya hay afirmación.", "Falta una razón y una evidencia."], "Una razón y una evidencia, como que ambas potencias podían destruirse y nunca se enfrentaron directamente"),
        ("Reconocer un buen contraargumento", "«Es cierto que no hubo choque directo, pero hubo guerras con muchas víctimas». ¿Qué hace?", ["Admite algo de la otra posición.", "Luego lo matiza con evidencia."], "Reconoce un acierto y matiza"),
    ],
    mistakes=[("Afirmar que la amenaza nuclear fue inevitablemente buena o mala.", "Se simplifica un problema complejo.", "Presenta avances y costos con evidencia."),
              ("Responder a una posición atacando a quien la sostiene.", "Se confunde ganar con comprender.", "Discute la idea con razones y datos.")],
    T=[
        ("{F} ¿Qué años abarcó la guerra de Corea?", "De 1950 a 1953", "La ficha lo indica."),
        ("{F} ¿Qué dice la Posición 1 sobre la amenaza nuclear?", "Que mantuvo la paz entre las superpotencias porque ambas podían destruirse", "Es su afirmación central."),
        ("{F} ¿Qué hecho de 1962 usa la Posición 2 como evidencia de riesgo?", "La crisis de los misiles", "La ficha la nombra en esa posición."),
        ("{F} ¿Qué tres partes tiene un argumento?", "Afirmación, razón y evidencia", "Así se explica en la clase."),
        ("{F} ¿Qué es disuasión? A) Evitar que alguien actúe haciéndole temer una respuesta muy dañina B) Aumentar las armas sin motivo", "A) Evitar que alguien actúe haciéndole temer una respuesta muy dañina", "Así se define en el vocabulario."),
        ("{F} La Posición 1 usa como evidencia que las superpotencias no se enfrentaron directamente. ¿Qué parte del argumento es? A) La evidencia B) La afirmación", "A) La evidencia", "Es el hecho que apoya la tesis."),
        ("{F} Un participante responde: «Es cierto que no hubo choque directo, pero hubo guerras por delegación». ¿Qué hace? A) Reconoce un acierto y matiza B) Ataca a la persona", "A) Reconoce un acierto y matiza", "Admite una parte y agrega una precisión."),
        ("{F} Alguien dice: «Quien defiende la disuasión no se preocupa por las víctimas». ¿Qué es eso? A) Una falacia contra la persona B) Un contraargumento con evidencia", "A) Una falacia contra la persona", "No discute la idea sino a quien opina."),
        ("{F} ¿Qué evidencia usa mejor la Posición 2 para hablar de costos? A) Los muertos en la guerra de Corea B) El fin de la Guerra Fría hacia 1991", "A) Los muertos en la guerra de Corea", "Corea fue una guerra por delegación con muchas víctimas."),
        ("{F} ¿Por qué es injusto decir que la disuasión «trajo paz» sin más?", "Porque hubo guerras indirectas con víctimas y el riesgo de una catástrofe", "La ficha muestra que la paz entre las superpotencias no fue paz para todos."),
        ("{F} Un compañero dice: «Era inevitable que no hubiera guerra directa». ¿Qué respuesta sirve? A) No hay evidencia de que fuera inevitable: la crisis de 1962 muestra riesgo real B) Tiene razón, porque no hubo guerra directa", "A) No hay evidencia de que fuera inevitable: la crisis de 1962 muestra riesgo real", "Que algo ocurra no prueba que no pudiera haber ocurrido otra cosa."),
        ("{F} ¿Cuál de estas posturas finales es más equilibrada? A) La amenaza nuclear contribuyó a evitar la guerra directa, pero aumentó el riesgo y los costos para muchos países B) La amenaza nuclear fue solo negativa", "A) La amenaza nuclear contribuyó a evitar la guerra directa, pero aumentó el riesgo y los costos para muchos países", "Combina avances y límites con base en los hechos."),
        ("{F} ¿Qué haría más honesto un debate de ejemplo entre las Posiciones 1 y 2? A) Que cada una cite un hecho de la ficha y reconozca un punto fuerte de la otra B) Que cada posición repita su tesis varias veces", "A) Que cada una cite un hecho de la ficha y reconozca un punto fuerte de la otra", "Un buen debate se apoya en evidencia y en escuchar."),
    ],
    ctx=("En un debate de curso, una persona dice: «La amenaza nuclear fue un fracaso porque hubo guerras». ¿Qué respuesta usa mejor lo aprendido? A) Reconocer las guerras por delegación, pero mostrar que no hubo guerra directa entre las superpotencias B) Decir que quien opina eso exagera", "A) Reconocer las guerras por delegación, pero mostrar que no hubo guerra directa entre las superpotencias", "Contrasta con evidencia y matiza sin atacar a la persona."),
    sc=[("En Historia: ¿qué es la disuasión?", "Evitar que alguien actúe haciéndole temer una respuesta muy dañina", "Así se define en el vocabulario."),
        ("¿Qué partes tiene un argumento?", "Afirmación, razón y evidencia", "Son las tres partes de la explicación."),
        ("¿Por qué conviene separar costos de corto y largo plazo en un debate?", "Porque permite ver quiénes pagaron un costo y cuándo", "Así se explica en la clase.")],
    op=("Prepara un mini debate escrito. Elige la Posición 1 o la 2 de la ficha y escribe un argumento de tres partes. Luego escribe un contraargumento a la otra posición que reconozca algo cierto y lo matice. Cierra con una frase que diga un efecto positivo y un costo de la amenaza nuclear durante la Guerra Fría. {F}",
        "Posición 2: afirmación «evitar el choque directo no fue paz»; razón «hubo guerras por delegación»; evidencia «Corea, 1950 a 1953». Contraargumento: «Es cierto que no hubo choque directo, pero…». Cierre: efecto, evitó la guerra directa; costo, riesgo y guerras indirectas.",
        ["argumento con tres partes", "contraargumento sin atacar a la persona", "efecto y costo en el cierre"], ["argumento escrito", "contraargumento", "frase de cierre"], ["atacar a la persona", "decir que algo fue inevitable", "omitir el costo"],
        "Pide que lea su argumento a otra persona y que esa persona diga qué evidencia usó."),
    reinforce="Explica a alguien de tu casa por qué la disuasión nuclear se puede ver como un beneficio y como un riesgo.",
    extend="Escribe un contraargumento a la frase «la amenaza nuclear no tuvo ningún efecto» usando un hecho de esta clase.",
)
