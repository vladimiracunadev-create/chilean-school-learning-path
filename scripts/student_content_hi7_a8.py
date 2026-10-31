"""Material del estudiante de 7.º básico, Historia, Geografía y Ciencias Sociales: OA 08 (canon cultural de la Antigüedad clásica)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI07 OA 08"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (hecha para este cuaderno). La palabra «canon» viene del griego kanón, que significa regla o vara de medir. "
     "Un canon cultural es un conjunto de obras, autores o modelos que una sociedad considera valiosos y transmite, por ejemplo, en la escuela. "
     "Caso de ejemplo: un club de lectura de 8 personas elige sus libros imprescindibles. Cada persona vota por 3 libros. Votos: libro 1, 6 votos; libro 2, 5 votos; libro 3, 5 votos; libro 4, 4 votos; libro 5, 2 votos; libro 6, 2 votos. El club decide que su canon serán los 3 libros más votados. "
     "Caso histórico: la lista de las Siete Maravillas del mundo antiguo la compilaron autores griegos; incluye las pirámides de Egipto, los Jardines Colgantes de Babilonia, la estatua de Zeus en Olimpia, el templo de Ártemis en Éfeso, el Mausoleo de Halicarnaso, el Coloso de Rodas y el Faro de Alejandría.")
build(
    OA, 1, F,
    use="Aprenderé qué es un canon cultural y cómo se construye. Sirve para entender por qué algunas obras de la Antigüedad se estudian y otras no.",
    prior=["Sé que Grecia y Roma fueron civilizaciones del Mediterráneo.", "Sé distinguir una fuente primaria de una secundaria.", "Sé hacer sumas y restas simples."],
    explain=[
        "Un canon cultural es un conjunto de obras, autores o modelos que una sociedad considera valiosos y transmite, por ejemplo, a través de la escuela, las bibliotecas y los museos. La palabra viene del griego kanón, que significa regla o vara de medir: el canon sirve como regla para decidir qué obras se estudian.",
        "Un canon no es una lista natural ni eterna: lo construyen personas, con criterios como la calidad, la influencia o la representatividad. Un ejemplo es la lista de las Siete Maravillas del mundo antiguo: la hicieron autores griegos y por eso incluye lugares del Mediterráneo y de Oriente cercano, pero no obras de China, de India o de América.",
        "Para entender un canon hay que preguntar quién lo hizo, con qué criterio y qué quedó fuera. Un club de lectura que vota sus libros y elige los más votados construye un canon pequeño. Con el tiempo, un canon cambia: se agregan obras nuevas y se reevalúan otras.",
    ],
    vocab=[("canon", "conjunto de obras o autores que una sociedad considera modelos y transmite"), ("criterio", "razón con la que se decide qué incluir"), ("influencia", "efecto que una obra tiene sobre otras o sobre las personas"), ("representatividad", "capacidad de una obra de representar a un grupo o una época"), ("compilar", "reunir en una lista o colección")],
    worked=[
        ("Aplicar un criterio", "{F} ¿Cuáles son los tres libros del canon del club?", ["Ordeno por votos: 6, 5, 5, 4, 2, 2.", "Los tres primeros son los libros 1, 2 y 3."], "Los libros 1, 2 y 3"),
        ("Contar votos", "{F} ¿Cuántos votos recibieron los libros 5 y 6 en total?", ["Cada uno recibió 2 votos.", "Sumo: 2 + 2 = 4."], "4 votos"),
    ],
    mistakes=[("Pensar que el canon es una lista natural y eterna.", "No se ve que lo construyen personas con criterios.", "Pregunta quién lo hizo, cuándo y con qué criterio."),
              ("Creer que lo que no está en el canon no tiene valor.", "Se confunde estar fuera de una lista con ser inferior.", "Una lista deja cosas fuera por sus criterios, no por ausencia de valor.")],
    T=[
        ("{F} ¿Qué significa la palabra griega kanón?", "Regla o vara de medir", "La ficha lo indica."),
        ("{F} ¿Cuántas personas votan en el club de lectura?", "8", "La ficha lo indica."),
        ("{F} ¿Cuántos libros del club forman el canon?", "3", "La ficha dice que serán los tres más votados."),
        ("=", "{F} ¿Cuántos votos se emitieron en total, con 8 personas que votan por 3 libros cada una?", "8*3", "Se multiplican las personas por los libros que vota cada una.", " votos"),
        ("=", "{F} ¿Cuántos votos más tuvo el libro 1 que el libro 4?", "6-4", "Se resta el número menor al mayor.", " votos"),
        ("{F} ¿Quiénes compilaron la lista de las Siete Maravillas?", "Autores griegos", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos votos recibieron en total los tres libros del canon?", "6+5+5", "Se suman los votos de los libros 1, 2 y 3.", " votos"),
        ("{F} ¿Qué criterio aplicó el club para formar su canon?", "Elegir los tres libros más votados", "La ficha lo indica."),
        ("{F} ¿Por qué la lista de las Siete Maravillas no incluye obras de China ni de América?", "Porque la hicieron autores griegos desde su mundo conocido", "La lista refleja la perspectiva de quien la hizo."),
        ("{F} Pedro dice: «La lista de las Siete Maravillas es la lista natural de lo más importante del mundo». Corrígelo.", "Fue compilada por autores griegos con su criterio; otras personas habrían hecho otra lista", "Un canon lo construyen personas."),
        ("{F} Si en otro club los seis libros recibieran 5, 5, 4, 4, 3 y 3 votos y el canon fuera de 3 libros, ¿habría empate para el último lugar? Explica.", "Sí: dos libros con 4 votos disputan el tercer lugar y haría falta otro criterio", "Los dos primeros tienen 5 votos y el tercer lugar queda dividido."),
        ("{F} Ana dice: «Lo que no entró al canon del club es malo». Corrígela.", "Solo tuvo menos votos; quedar fuera de una lista no significa que carezca de valor", "El criterio fue la cantidad de votos."),
        ("{F} Propón un criterio distinto para armar el canon de un club y di qué cambiaría.", "Por ejemplo: elegir libros de distintos países, lo que cambiaría la lista y mostraría más voces", "Un criterio distinto produce un canon distinto."),
    ],
    ctx=("Tu curso debe elegir tres canciones para el acto de fin de año y se decide por votos. ¿Por qué esa lista de tres es un tipo de canon y qué criterio usa? {F}", "Es un canon porque reúne obras valoradas por el grupo; su criterio son los votos", "Un grupo elige y transmite sus modelos."),
    sc=[("¿Qué es un canon cultural?", "Un conjunto de obras o autores que una sociedad considera valiosos y transmite", "Es la definición de la clase."),
        ("¿Quién construye un canon?", "Las personas, con criterios", "No es una lista natural."),
        ("=", "{F} ¿Cuántos votos sumaron los libros 5 y 6 del club?", "2+2", "Se suman los votos de ambos libros.", " votos")],
    op=("Arma un canon de cinco elementos sobre un tema que conozcas (por ejemplo, juegos, canciones o deportes). Escribe el criterio, los cinco elementos, uno que quedó fuera y por qué. {F}",
        "Criterio: los más jugados por mi curso; cinco juegos; quedó fuera uno por pocos jugadores.",
        ["explica el criterio", "los cinco elementos coinciden con el criterio", "justifica un elemento excluido"], ["lista escrita", "criterio y exclusión"], ["no explicar el criterio", "decir que lo excluido es malo"],
        "Pide que explique cómo cambiaría su canon con otro criterio."),
    reinforce="Explica con tus palabras qué es un canon y quién lo construye.",
    extend="Escribe una pregunta sobre qué obras de otros pueblos no están en la lista de las Siete Maravillas.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (resumen hecho para este cuaderno). "
     "Filosofía: Sócrates (470 a 399 a. C.) vivió en Atenas, hacía preguntas a la gente para examinar sus ideas y no escribió libros; Platón fundó la Academia hacia 387 a. C.; Aristóteles (384 a 322 a. C.) fundó el Liceo hacia 335 a. C. y estudió lógica, política y biología. "
     "Ciencias: Euclides (hacia 300 a. C.) reunió la geometría de su época en los Elementos. "
     "Historia: Heródoto (siglo V a. C.) escribió sobre las guerras entre griegos y persas; Tucídides (siglo V a. C.) narró la guerra del Peloponeso entre Atenas y Esparta. "
     "Literatura: la Ilíada y la Odisea, atribuidas a Homero, son poemas épicos de hacia el siglo VIII a. C.; Sófocles (siglo V a. C.) escribió tragedias, obras de teatro sobre conflictos graves. "
     "Arte: el Partenón, templo de Atenea en la Acrópolis de Atenas, se construyó entre 447 y 432 a. C.; el escultor Fidias dirigió su decoración.")
build(
    OA, 2, F,
    use="Aprenderé a analizar obras de filosofía, historia, arte y literatura de la Antigüedad como fuentes. Sirve para entender qué muestran de su época y qué no.",
    prior=["Sé qué es un canon.", "Sé qué fue la democracia ateniense.", "Sé calcular duraciones con años a. C."],
    explain=[
        "Las obras de la Antigüedad son fuentes: nos dicen cómo pensaban, qué les importaba y cómo veían el mundo. En filosofía, Sócrates, Platón y Aristóteles se preguntaron por la verdad, la justicia y la política. En ciencias, Aristóteles estudió la biología y Euclides reunió la geometría de su época en los Elementos. En historia, Heródoto y Tucídides narraron guerras e intentaron explicar sus causas.",
        "En literatura, la Ilíada y la Odisea son poemas épicos atribuidos a Homero, y Sófocles escribió tragedias sobre conflictos graves. En arte, el Partenón, templo de Atenea construido entre 447 y 432 a. C., muestra la proporción, la belleza y el poder de Atenas. Cada obra se interpreta con su contexto: quién la hizo, cuándo, para quién y con qué propósito.",
        "Una obra no es un reflejo completo de la sociedad. Heródoto escribió desde la perspectiva griega, y a Sócrates lo conocemos sobre todo por lo que escribieron otras personas. Para sacar conclusiones se usan varias fuentes y se distingue lo que la obra dice de lo que nosotros interpretamos.",
    ],
    vocab=[("filosofía", "reflexión sobre la verdad, la justicia, el conocimiento y la vida"), ("poema épico", "poema largo que narra hazañas de héroes"), ("tragedia", "obra de teatro sobre un conflicto grave que suele terminar mal"), ("templo", "edificio dedicado a un dios"), ("fuente", "obra o documento del que se obtiene información")],
    worked=[
        ("Calcular una duración", "{F} ¿Cuántos años duró la construcción del Partenón?", ["Fechas: 447 y 432 a. C.", "Resto: 447 − 432 = 15."], "15 años"),
        ("Clasificar una obra", "{F} ¿La Ilíada es una obra de historia o de literatura?", ["Es un poema épico atribuido a Homero.", "Los poemas son literatura."], "De literatura"),
    ],
    mistakes=[("Tomar un poema épico como un informe exacto de lo que ocurrió.", "Se confunde literatura con registro histórico.", "Úsalo como fuente de ideas y valores, y contrástalo con otras evidencias."),
              ("Creer que una sola obra cuenta toda la sociedad.", "Se generaliza desde una fuente.", "Compara varias fuentes de distinto tipo.")],
    T=[
        ("{F} ¿Quién fundó la Academia?", "Platón", "La ficha lo indica."),
        ("{F} ¿Qué escribió Tucídides?", "La historia de la guerra del Peloponeso", "La ficha lo indica."),
        ("{F} ¿Quién reunió la geometría de su época en los Elementos?", "Euclides", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años vivió Sócrates, de 470 a 399 a. C.?", "470-399", "Se restan los años a. C.", " años"),
        ("=", "{F} ¿Cuántos años vivió Aristóteles, de 384 a 322 a. C.?", "384-322", "Se restan los años a. C.", " años"),
        ("{F} Relaciona cada obra con su disciplina: Odisea, Partenón, obra de Heródoto sobre las guerras con los persas, Elementos de Euclides.", "Odisea: literatura; Partenón: arte; obra de Heródoto: historia; Elementos de Euclides: ciencias (geometría)", "Cada obra pertenece a un campo distinto."),
        ("=", "{F} ¿Cuántos años después de la fundación de la Academia (387 a. C.) se fundó el Liceo (335 a. C.)?", "387-335", "Se restan los años a. C.", " años"),
        ("{F} ¿Por qué conocemos las ideas de Sócrates a través de otras personas?", "Porque él no escribió libros", "La ficha lo dice."),
        ("{F} ¿Qué dos guerras narran Heródoto y Tucídides?", "Las guerras entre griegos y persas, y la guerra del Peloponeso entre Atenas y Esparta", "La ficha las nombra."),
        ("{F} Ana dice: «La Ilíada es un registro exacto de una guerra». Corrígela.", "Es un poema épico, no un informe; sirve para conocer valores y creencias, y se contrasta con otras evidencias", "La literatura no equivale a un registro."),
        ("{F} ¿Qué perspectiva tiene Heródoto cuando escribe sobre las guerras con los persas?", "La perspectiva griega", "Es un autor griego."),
        ("{F} ¿Qué muestra el Partenón sobre Atenas en el siglo V a. C.?", "Su riqueza, su poder y la importancia de su diosa Atenea", "Un templo grande indica recursos y valores."),
        ("{F} Un compañero dice: «Con Platón basta para conocer cómo pensaban los atenienses». ¿Qué le falta?", "Otras fuentes de otros autores y grupos, porque Platón no representa a toda la sociedad", "Una sola fuente da una sola perspectiva."),
    ],
    ctx=("Un guía de museo muestra una vasija con una escena de teatro y dice: «Esto prueba que todos los atenienses iban al teatro». ¿Qué le replicarías? {F}", "Que una vasija es una sola fuente y no prueba lo que hacían todos", "Una fuente no basta para generalizar."),
    sc=[("¿Qué es un poema épico?", "Un poema largo que narra hazañas de héroes", "La Ilíada es un ejemplo."),
        ("¿Qué es una tragedia?", "Una obra de teatro sobre un conflicto grave", "Sófocles escribió varias."),
        ("{F} ¿Dónde está el Partenón?", "En la Acrópolis de Atenas", "La ficha lo indica.")],
    op=("Elige una obra de la ficha y escribe una ficha de análisis de cuatro líneas: quién la hizo, cuándo, qué muestra de su época y qué no permite saber. {F}",
        "Partenón: arte de Atenas en el siglo V a. C.; muestra poder y religión; no dice cómo vivían las personas comunes.",
        ["indica autor y época", "señala qué muestra", "señala un límite"], ["ficha escrita"], ["tomar la obra como un registro completo", "olvidar el contexto"],
        "Pide que explique qué otra fuente completaría su análisis."),
    reinforce="Nombra una obra de cada campo: filosofía, historia, literatura y arte.",
    extend="Escribe una pregunta que un historiador haría al Partenón.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (resumen hecho para este cuaderno; los números del teatro son de ejemplo). "
     "Protágoras, un sofista del siglo V a. C., dijo que «el ser humano es la medida de todas las cosas». "
     "Aristóteles escribió que el ser humano es un animal político, es decir, vive en comunidad y participa en la ciudad. "
     "Escultura griega: cuerpos humanos de atletas representados con proporciones cuidadas. "
     "Tragedia Antígona, de Sófocles (hacia 441 a. C.): Antígona entierra a su hermano aunque el rey Creonte lo prohibió, porque cree que su deber familiar y religioso es más importante que la orden del rey. "
     "Deporte: los Juegos Olímpicos antiguos se celebraban en Olimpia cada cuatro años, desde 776 a. C. según la tradición; competían varones libres griegos, y se valoraban la fuerza y el cuerpo bien proporcionado. "
     "Un teatro de ejemplo tiene 20 filas de 150 asientos.")
build(
    OA, 3, F,
    use="Aprenderé a examinar la idea de ciudadanía y la centralidad del ser humano en la cultura clásica. Sirve para entender qué valores se expresan en sus obras.",
    prior=["Sé qué era un ciudadano en Atenas.", "Sé analizar una obra como fuente.", "Sé multiplicar con números de tres cifras."],
    explain=[
        "En la Antigüedad clásica, muchas obras ponen al ser humano en el centro. Protágoras dijo que «el ser humano es la medida de todas las cosas», y Aristóteles que somos animales políticos, es decir, vivimos en comunidad y participamos en la ciudad. La escultura griega representa cuerpos humanos cuidadosamente proporcionados, y los Juegos Olímpicos de Olimpia celebraban el cuerpo y la competencia entre varones libres: un ideal de belleza y de deporte centrado en el ser humano.",
        "La ciudadanía ocupaba un lugar importante: participar en la Asamblea, en tribunales y en el teatro era parte de la vida del ciudadano. La tragedia Antígona, de Sófocles, plantea un conflicto entre la orden del rey y el deber familiar y religioso, y llevaba a los ciudadanos a pensar en la justicia y las leyes.",
        "Pero esa «centralidad humana» tenía límites: los humanos que importaban eran, en gran medida, los ciudadanos varones. Las mujeres, los extranjeros y las personas esclavizadas quedaban fuera de esa participación. Al estudiar estas obras se reconoce su aporte y también a quiénes dejaban de lado.",
    ],
    vocab=[("centralidad humana", "idea que pone al ser humano y sus capacidades en el centro"), ("animal político", "ser que vive en comunidad y participa en la ciudad"), ("sofista", "maestro griego que enseñaba oratoria y argumentación a cambio de pago"), ("conflicto de valores", "situación en que dos deberes importantes chocan"), ("oratoria", "arte de hablar bien en público")],
    worked=[
        ("Calcular asientos", "{F} ¿Cuántos asientos tiene el teatro de ejemplo?", ["Hay 20 filas de 150 asientos.", "Multiplico: 20 × 150 = 3.000."], "3.000 asientos"),
        ("Identificar un conflicto de valores", "{F} ¿Qué dos deberes chocan en Antígona?", ["La orden del rey Creonte.", "El deber familiar y religioso de enterrar a su hermano."], "La orden del rey y el deber familiar"),
    ],
    mistakes=[("Creer que la «centralidad humana» incluía a todas las personas.", "Se olvida quiénes eran ciudadanos.", "Nombra a los excluidos: mujeres, extranjeros y personas esclavizadas."),
              ("Leer una tragedia como si dijera lo que pensaban todos los atenienses.", "Se confunde obra y sociedad.", "Una obra muestra preguntas de su época, no la opinión de todos.")],
    T=[
        ("{F} ¿Quién dijo que «el ser humano es la medida de todas las cosas»?", "Protágoras", "La ficha lo indica."),
        ("{F} ¿Quién escribió la tragedia Antígona?", "Sófocles", "La ficha lo indica."),
        ("{F} ¿Quién prohibió enterrar al hermano de Antígona?", "El rey Creonte", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos asientos tiene el teatro de ejemplo en 5 filas?", "5*150", "Se multiplican las filas por los asientos de cada una.", " asientos"),
        ("=", "{F} Si el teatro de ejemplo se llena con 2.400 espectadores, ¿cuántos asientos quedan vacíos?", "20*150-2400", "Se resta el público a los 3.000 asientos totales.", " asientos"),
        ("{F} ¿Qué significa que el ser humano es un animal político?", "Que vive en comunidad y participa en la ciudad", "Así lo explica la ficha."),
        ("{F} ¿Cada cuántos años se celebraban los Juegos Olímpicos antiguos y quiénes competían?", "Cada cuatro años; competían varones libres griegos", "La ficha lo indica."),
        ("{F} ¿Qué valor defiende Antígona al enterrar a su hermano?", "El deber familiar y religioso", "Lo pone por encima de la orden del rey."),
        ("{F} ¿Por qué se dice que Antígona ayudaba a pensar sobre la justicia y las leyes?", "Porque muestra un choque entre la orden del gobernante y un deber moral", "El conflicto invita a discutir qué ley debe obedecerse."),
        ("{F} Pedro dice: «En la Antigüedad clásica todas las personas eran el centro». Corrígelo.", "Eran el centro sobre todo los ciudadanos varones; las mujeres, los extranjeros y las personas esclavizadas quedaban fuera", "La centralidad humana tenía límites."),
        ("{F} Lucía dice: «Antígona muestra lo que pensaban todos los atenienses». Corrígela.", "Es una obra de Sófocles que plantea una pregunta; no prueba lo que pensaba cada persona", "Una obra no representa a toda la sociedad."),
        ("{F} ¿Qué relación hay entre participar en el teatro y la ciudadanía?", "Asistir al teatro era una actividad cívica, donde los ciudadanos pensaban sobre asuntos de la ciudad", "El teatro formaba parte de la vida ciudadana."),
        ("{F} ¿Qué diferencia hay entre decir que el ser humano es importante y decir que todas las personas tenían los mismos derechos en Atenas?", "La primera es una idea de la época; la segunda es falsa, porque había exclusiones", "Las ideas no siempre coincidían con las prácticas."),
    ],
    ctx=("Un escritor actual dice: «Los griegos inventaron el valor de cada persona». Con la ficha, ¿cómo matizarías esa frase? {F}", "Pusieron al ser humano en el centro, pero en la práctica solo valoraban plenamente a los ciudadanos varones", "Hubo una idea de centralidad humana, pero con exclusiones."),
    sc=[("¿Qué es la centralidad humana?", "La idea que pone al ser humano y sus capacidades en el centro", "Es un rasgo de la cultura clásica."),
        ("¿Qué conflicto plantea Antígona?", "El choque entre la orden del rey y el deber familiar y religioso", "Es el tema de la obra."),
        ("=", "{F} ¿Cuántos asientos tiene el teatro de ejemplo en 10 filas?", "10*150", "Se multiplican las filas por los asientos.", " asientos")],
    op=("Escribe un diálogo breve entre un ciudadano y una mujer de Atenas sobre si «el ser humano es la medida de todas las cosas». Usa una frase de la ficha y haz que el diálogo muestre al menos un límite de esa idea. {F}",
        "Ciudadano: el ser humano es la medida de las cosas. Mujer: pero yo no puedo votar. Ciudadano: es la costumbre.",
        ["usa una idea de la ficha", "muestra un límite o exclusión", "los personajes hablan según su época"], ["diálogo escrito"], ["poner ideas actuales en boca de los personajes sin explicarlas", "olvidar el límite"],
        "Pide que explique qué fuente real necesitaría para conocer la voz de las mujeres."),
    reinforce="Explica con tus palabras qué significa «animal político».",
    extend="Escribe una pregunta sobre qué opinaba una persona esclavizada de las ideas de Protágoras.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (resumen hecho para este cuaderno). "
     "Voces menos presentes: Safo, poeta de la isla de Lesbos (hacia 600 a. C.), de quien se conservan sobre todo fragmentos. "
     "Otras culturas: la Epopeya de Gilgamesh, de Mesopotamia, tiene versiones de más de 3.500 años; Confucio (551 a 479 a. C.) vivió en China. "
     "Transmisión: muchas obras griegas se copiaron en monasterios medievales; en el siglo IX, en la Casa de la Sabiduría de Bagdad, se tradujeron al árabe obras griegas; en el siglo XII se tradujeron al latín en Toledo; hacia 1450 la imprenta de Gutenberg multiplicó los libros. "
     "Sófocles escribió unas 120 obras de teatro y se conservan 7 completas.")
build(
    OA, 4, F,
    use="Aprenderé a identificar exclusiones en el canon clásico y cómo llegaron las obras hasta hoy. Sirve para entender que lo que conocemos depende de quiénes lo guardaron.",
    prior=["Sé qué es un canon y quién lo construye.", "Sé que Atenas excluía a mujeres, extranjeros y personas esclavizadas.", "Sé comparar años a. C."],
    explain=[
        "El canon de la Antigüedad clásica deja fuera muchas voces. Las mujeres escribieron poco o su obra se perdió, como la poeta Safo, de quien conservamos sobre todo fragmentos. Tampoco aparecen otras culturas: Mesopotamia tiene la Epopeya de Gilgamesh, de más de 3.500 años, y China tuvo a Confucio. Grecia y Roma no fueron las únicas fuentes culturales.",
        "Además, lo que conocemos depende de la transmisión. Las obras se copiaban a mano en monasterios; en el siglo IX, en la Casa de la Sabiduría de Bagdad, se tradujeron obras griegas al árabe; en el siglo XII se tradujeron al latín en Toledo; hacia 1450 la imprenta multiplicó los libros. Gracias a esas cadenas de copia y traducción llegaron muchas obras, pero otras se perdieron: de unas 120 obras de Sófocles, solo 7 se conservan completas.",
        "Por eso el canon es incompleto: refleja lo que se conservó, lo que se tradujo y lo que ciertas instituciones valoraron. Estudiarlo con atención implica preguntar quién decidió copiar o guardar una obra, y qué voces quedaron fuera.",
    ],
    vocab=[("transmisión", "paso de una obra o saber de una época a otra"), ("fragmento", "parte pequeña que se conserva de una obra"), ("copista", "persona que copia textos a mano"), ("traducción", "paso de un texto de una lengua a otra"), ("imprenta", "máquina que permite imprimir muchas copias de un libro")],
    worked=[
        ("Calcular obras perdidas", "{F} ¿Cuántas obras de Sófocles no se conservan completas?", ["Escribió unas 120 y se conservan 7.", "Resto: 120 − 7 = 113."], "Unas 113 obras"),
        ("Explicar una cadena de transmisión", "{F} ¿Qué pasó con las obras griegas en Bagdad en el siglo IX?", ["La ficha dice que se tradujeron.", "El idioma era el árabe."], "Se tradujeron al árabe"),
    ],
    mistakes=[("Pensar que todo lo que se escribió en la Antigüedad llegó a nosotros.", "Se ignora la pérdida de obras.", "Se conserva solo una parte: de unas 120 obras de Sófocles se conservan 7."),
              ("Creer que las obras llegaron a Europa solo desde Grecia y Roma.", "Se olvida la traducción árabe.", "Muchas obras llegaron a Europa a través de traducciones árabes y latinas.")],
    T=[
        ("{F} ¿Dónde vivió Safo?", "En la isla de Lesbos", "La ficha lo indica."),
        ("{F} ¿Dónde se tradujeron obras griegas al árabe en el siglo IX?", "En la Casa de la Sabiduría de Bagdad", "La ficha lo indica."),
        ("{F} ¿Dónde se tradujeron obras al latín en el siglo XII?", "En Toledo", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años vivió Confucio, de 551 a 479 a. C.?", "551-479", "Se restan los años a. C.", " años"),
        ("=", "{F} Si Sófocles escribió unas 120 obras y se conservan 7 completas, ¿cuántas se perdieron o no se conservan completas?", "120-7", "Se resta lo conservado al total.", " obras"),
        ("{F} ¿Qué se conserva sobre todo de la obra de Safo?", "Fragmentos", "La ficha lo indica."),
        ("{F} ¿Qué cultura produjo la Epopeya de Gilgamesh?", "Mesopotamia", "La ficha lo indica."),
        ("{F} Ordena las etapas de transmisión: imprenta de Gutenberg, traducción en Bagdad, traducción en Toledo.", "Traducción en Bagdad (siglo IX), traducción en Toledo (siglo XII), imprenta de Gutenberg (hacia 1450)", "Los siglos van del IX al XII y luego 1450."),
        ("{F} ¿Por qué se conserva solo una parte de las obras antiguas?", "Porque las copias se perdían o se destruían y no todas se copiaron o tradujeron", "La conservación dependía de quién copiaba y guardaba."),
        ("{F} Pedro dice: «Grecia y Roma fueron las únicas culturas con obras importantes». Corrígelo con dos datos de la ficha.", "También hay obras de Mesopotamia, como la Epopeya de Gilgamesh, y de China, como las ideas de Confucio", "La ficha nombra otras culturas."),
        ("{F} Ana dice: «Si de Safo solo hay fragmentos, no fue importante». Corrígela.", "Que se conserven fragmentos no mide su importancia; muchas obras se perdieron por la transmisión", "La pérdida no equivale a falta de valor."),
        ("{F} ¿Qué papel tuvieron las traducciones árabes en la historia del canon clásico?", "Conservaron y transmitieron obras griegas que luego llegaron a Europa por otras traducciones", "Fueron un eslabón entre épocas."),
        ("{F} Una persona dice que el canon clásico es completo. Da un argumento de la ficha que lo contradiga.", "Faltan voces como la de Safo y de otras culturas, y se perdieron muchas obras", "La ficha lo muestra con ejemplos."),
    ],
    ctx=("Una biblioteca escolar tiene solo traducciones de autores griegos varones. Una estudiante pregunta qué voces faltan. Usa la ficha para dar dos respuestas. {F}", "Mujeres como Safo y obras de otras culturas, como la Epopeya de Gilgamesh o las ideas de Confucio", "La ficha nombra voces ausentes."),
    sc=[("¿Qué es la transmisión de una obra?", "El paso de una obra de una época a otra", "Incluye copias y traducciones."),
        ("¿Qué es un fragmento?", "Una parte pequeña que se conserva de una obra", "Safo es un caso."),
        ("{F} ¿En qué país actual vivió Confucio?", "En China", "La ficha lo indica.")],
    op=("Dibuja un esquema de la cadena de transmisión de una obra griega hasta hoy con las etapas de la ficha y escribe, al lado, una voz o cultura que no aparece en el canon clásico y por qué importa. {F}",
        "Copias en monasterios, traducción en Bagdad, traducción en Toledo, imprenta; voz ausente: Safo.",
        ["incluye las etapas en orden", "nombra una voz o cultura ausente", "explica por qué importa"], ["esquema dibujado", "voz ausente explicada"], ["desordenar las etapas", "decir que lo ausente no importa"],
        "Pide que explique cómo se podría recuperar una voz que se perdió."),
    reinforce="Nombra dos voces o culturas que no aparecen en el canon clásico.",
    extend="Escribe una pregunta sobre qué obras de pueblos originarios de América se transmitieron oralmente.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (hecha para este cuaderno). "
     "Debate: ¿debe una escuela enseñar solo obras del canon clásico (Grecia y Roma) o ampliarlo? "
     "Postura 1: el canon da una base común y reconoce obras muy influyentes. "
     "Postura 2: el canon deja fuera voces y debe ampliarse con obras de otras culturas y de mujeres. "
     "Caso de ejemplo: una antología escolar tenía 20 autores de Grecia y Roma: 18 varones y 2 mujeres. La edición nueva tiene 30 autores: 20 de Grecia y Roma y 10 de otras culturas (Mesopotamia, Egipto, India, China y América). "
     "Ejemplo de mal argumento: «Es antiguo, por lo tanto es mejor».")
build(
    OA, 5, F,
    use="Aprenderé a debatir por qué el canon se construye y se revisa. Sirve para dar y evaluar argumentos sobre qué obras enseñar.",
    prior=["Sé qué es un canon.", "Sé que el canon deja fuera voces.", "Sé distinguir una opinión de un argumento."],
    explain=[
        "Un canon se construye y se revisa. Las escuelas, las universidades y las bibliotecas deciden qué obras se enseñan, y esas decisiones cambian con el tiempo. Por ejemplo, hoy se estudian con más frecuencia obras de mujeres y de otras culturas que antes no aparecían.",
        "En un debate sobre el canon se pueden defender posturas distintas. Una dice que el canon clásico da una base común y reconoce obras influyentes. Otra dice que deja fuera voces y debe ampliarse. Un buen argumento tiene una afirmación, una razón y una evidencia; un mal argumento, como «es antiguo, por lo tanto es mejor», confunde antigüedad con calidad.",
        "Revisar un canon no significa destruirlo ni dejar de leer a Homero o Platón. Significa preguntarse qué criterios usamos, a quiénes incluimos y qué efectos tiene eso. Muchas veces la mejor propuesta combina la tradición con nuevas obras, y reconoce el valor de ambas.",
    ],
    vocab=[("debate", "discusión ordenada donde se defienden posturas con argumentos"), ("argumento", "razón con evidencia para apoyar una afirmación"), ("postura", "opinión que se defiende sobre un tema"), ("revisar", "examinar de nuevo para mejorar o corregir"), ("antología", "colección de textos de distintos autores")],
    worked=[
        ("Calcular un cambio", "{F} ¿Cuántos autores más tiene la edición nueva que la antigua?", ["Antigua: 20. Nueva: 30.", "Resto: 30 − 20 = 10."], "10 autores más"),
        ("Distinguir argumento y opinión", "«Me gusta Homero» y «Homero influyó en muchos autores posteriores». ¿Cuál es un argumento?", ["La primera frase es una preferencia personal.", "La segunda es una razón que se puede comprobar."], "La segunda"),
    ],
    mistakes=[("Defender una obra solo porque es antigua.", "Se confunde antigüedad con calidad.", "Da razones como la influencia, la calidad o lo que revela de su época."),
              ("Creer que revisar el canon es lo mismo que eliminarlo.", "Se piensa que se descarta lo clásico.", "Revisar es agregar voces y reflexionar sobre criterios, sin descartar lo valioso.")],
    T=[
        ("=", "{F} ¿Qué porcentaje de los autores de la antología antigua eran mujeres?", "2*100//20", "Se divide 2 por 20 y se expresa en porcentaje.", " %"),
        ("{F} ¿Cuántos autores de otras culturas tiene la edición nueva?", "10", "La ficha lo indica."),
        ("{F} ¿Cuántas mujeres había en la antología antigua?", "2", "La ficha lo indica."),
        ("{F} ¿Cuántos varones había entre los autores de la antología antigua?", "18", "La ficha lo indica."),
        ("=", "{F} En la edición nueva, ¿cuántos autores de Grecia y Roma hay por cada autor de otras culturas?", "20//10", "Se divide los autores de Grecia y Roma por los de otras culturas.", " autores"),
        ("{F} Clasifica cada frase como argumento con razón comprobable (A) o como opinión o razón inválida (O): 1) «Me gusta más Sófocles»; 2) «Sófocles influyó en el teatro posterior»; 3) «Es antiguo, así que es mejor».", "1 O, 2 A, 3 O", "Solo la segunda ofrece una razón comprobable."),
        ("{F} ¿Cuál es la postura 1 del debate?", "Que el canon clásico da una base común y reconoce obras influyentes", "La ficha lo indica."),
        ("{F} ¿Cuál es la postura 2 del debate?", "Que el canon deja fuera voces y debe ampliarse", "La ficha lo indica."),
        ("=", "{F} Si la edición nueva agrega 10 autores a una antología de 20, ¿cuántos autores tiene en total?", "20+10", "Se suman los autores agregados a los anteriores.", " autores"),
        ("{F} Pedro dice: «Revisar el canon es lo mismo que eliminar a Platón». Corrígelo.", "Revisar el canon significa ampliar y reflexionar sobre los criterios, sin dejar de leer lo valioso", "La edición nueva mantiene 20 autores de Grecia y Roma."),
        ("{F} ¿Qué error tiene el argumento «es antiguo, por lo tanto es mejor»?", "Confunde la antigüedad con la calidad", "Una obra puede ser antigua y no ser mejor."),
        ("{F} Da un argumento a favor de ampliar el canon y uno a favor de mantener la base clásica.", "Ampliar: se incluyen voces que antes faltaban; mantener: las obras clásicas fueron muy influyentes", "Ambos argumentos tienen una razón."),
        ("{F} ¿Qué solución combinaría ambas posturas?", "Mantener obras clásicas influyentes y agregar obras de otras culturas y de mujeres", "La edición nueva lo ejemplifica."),
    ],
    ctx=("El centro de estudiantes debate si el libro de lectura del año debe ser siempre clásico o incluir autores de distintos lugares. ¿Qué dos preguntas del debate se pueden usar? {F}", "¿Qué criterios usamos para elegir? ¿A quiénes incluimos y a quiénes dejamos fuera?", "Son las preguntas centrales para revisar un canon."),
    sc=[("¿Qué es un argumento?", "Una razón con evidencia que apoya una afirmación", "No es solo una opinión."),
        ("¿Por qué se revisa el canon?", "Porque las sociedades cambian y se reconocen voces que antes faltaban", "El canon no es eterno."),
        ("=", "{F} ¿Cuántos autores suman la edición antigua y la nueva juntas?", "20+30", "Se suman ambas cantidades.", " autores")],
    op=("Escribe una intervención de 6 líneas para un debate: elige una postura, da dos argumentos con evidencia de la ficha, responde a un posible contraargumento y termina con una propuesta que combine ambas posturas. {F}",
        "Postura 2: ampliar el canon; argumentos: la nueva antología agrega 10 autores de otras culturas; contraargumento: no se eliminan los clásicos; propuesta: mantener 20 y agregar.",
        ["elige y defiende una postura", "usa dos argumentos", "responde a un contraargumento y propone"], ["intervención escrita"], ["usar «es antiguo, por lo tanto es mejor»", "no usar evidencia"],
        "Pide que explique qué le diría a quien defiende la postura contraria."),
    reinforce="Escribe un argumento a favor de ampliar el canon y uno a favor de mantener obras clásicas.",
    extend="Escribe una pregunta que ayude a decidir qué obras de Chile debería incluir un canon escolar.",
)

# ---------------------------------------------------------------- clase 6
F = ("Ficha 6 (dossier hecho para este cuaderno). "
     "Pieza 1: el Partenón, templo de Atenea construido entre 447 y 432 a. C. en la Acrópolis de Atenas. "
     "Pieza 2: Antígona, tragedia de Sófocles (hacia 441 a. C.), donde una mujer desobedece una orden del rey para cumplir un deber familiar. "
     "Pieza 3: la Epopeya de Gilgamesh, de Mesopotamia, con versiones de más de 3.500 años. "
     "Pieza 4: la lista de las Siete Maravillas, compilada por autores griegos. "
     "Pieza 5: de unas 120 obras de Sófocles, solo 7 se conservan completas. "
     "Estructura de una interpretación: afirmación (lo que sostienes), evidencia (datos de las piezas) y límite (lo que las piezas no permiten saber).")
build(
    OA, 6, F,
    use="Aprenderé a elaborar una interpretación fundamentada sobre el canon cultural de la Antigüedad clásica. Sirve para escribir una conclusión con evidencia y con sus límites.",
    prior=["Sé qué es un canon.", "Sé analizar obras como fuentes.", "Sé identificar voces ausentes."],
    explain=[
        "Una interpretación fundamentada es una explicación que se apoya en evidencia y reconoce sus límites. Tiene tres partes: una afirmación (lo que sostienes), evidencia (datos concretos de las fuentes) y un límite (lo que esas fuentes no permiten saber).",
        "Con el dossier se pueden formular afirmaciones como «el canon clásico es una construcción incompleta». La evidencia puede ser que la lista de las Siete Maravillas la compilaron autores griegos, que de unas 120 obras de Sófocles solo 7 se conservan completas y que existen otras obras importantes, como la Epopeya de Gilgamesh. El límite puede ser que no sabemos qué se perdió.",
        "Una buena interpretación evita afirmar más de lo que las piezas permiten. No dice «todos los griegos pensaban así» ni «todo lo antiguo es mejor». Usa expresiones prudentes, como «es probable que» o «las piezas sugieren», y muestra cómo se llegó a la conclusión paso a paso.",
    ],
    vocab=[("interpretación", "explicación que se propone a partir de evidencia"), ("afirmación", "idea que se sostiene"), ("evidencia", "dato concreto que apoya una afirmación"), ("límite", "aquello que las fuentes no permiten saber"), ("fundamentada", "apoyada en evidencia y razones")],
    worked=[
        ("Identificar una evidencia", "{F} ¿Qué pieza sirve de evidencia para decir que el canon deja fuera obras de otras culturas?", ["La pieza 3 es de Mesopotamia.", "Muestra una obra importante fuera de Grecia y Roma."], "La pieza 3"),
        ("Calcular lo perdido", "{F} ¿Cuántas obras de Sófocles no se conservan completas?", ["Escribió unas 120 y se conservan 7.", "Resto: 120 − 7 = 113."], "Unas 113 obras"),
    ],
    mistakes=[("Afirmar algo sin evidencia, por ejemplo «todos los griegos pensaban igual».", "Se generaliza sin datos.", "Cita una pieza concreta del dossier."),
              ("Olvidar el límite de la interpretación.", "Se escribe como si fuera una certeza.", "Agrega qué no permiten saber las piezas.")],
    T=[
        ("{F} ¿Qué pieza menciona un templo de Atenas?", "La pieza 1", "La ficha lo indica."),
        ("{F} ¿Qué pieza cuenta un conflicto entre una orden del rey y un deber familiar?", "La pieza 2", "Es la tragedia Antígona."),
        ("{F} ¿Qué pieza es de Mesopotamia?", "La pieza 3", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años duró la construcción del Partenón?", "447-432", "Se restan los años a. C.", " años"),
        ("=", "{F} Si de otro autor antiguo se escribieron 90 obras y se conservan 9 completas, ¿cuántas no se conservan completas?", "90-9", "Se resta lo conservado al total.", " obras"),
        ("{F} ¿Cuáles son las tres partes de una interpretación fundamentada?", "Afirmación, evidencia y límite", "La ficha lo indica."),
        ("{F} Clasifica cada frase como afirmación (A), evidencia (E) o límite (L): 1) «Solo 7 obras de Sófocles se conservan completas»; 2) «El canon clásico es incompleto»; 3) «No sabemos qué obras se perdieron»; 4) «Los autores griegos compilaron la lista de las Siete Maravillas».", "1 E, 2 A, 3 L, 4 E", "Los datos son evidencia; la idea sostenida es afirmación; lo que falta saber es límite."),
        ("{F} ¿Qué pieza sirve para decir que el canon refleja la perspectiva de quien lo hizo?", "La pieza 4", "La lista fue compilada por autores griegos."),
        ("{F} Ordena los pasos de una buena interpretación: dar el límite, plantear la afirmación, citar la evidencia.", "Plantear la afirmación, citar la evidencia, dar el límite", "Se sostiene una idea, se la apoya y se reconoce lo que falta."),
        ("{F} Pedro escribe: «Todos los griegos valoraban a las mujeres porque existió Antígona». Señala el error.", "Generaliza desde una obra; una tragedia no prueba lo que pensaban todos", "Falta evidencia que permita esa generalización."),
        ("{F} Ana escribe: «El canon es incompleto». ¿Qué evidencia de la ficha la apoya mejor?", "Que de unas 120 obras de Sófocles solo 7 se conservan completas", "Muestra pérdida de obras."),
        ("{F} Elige la conclusión más prudente: A) Las piezas sugieren que el canon clásico es una construcción incompleta; B) Las piezas prueban que Grecia fue superior a otras culturas.", "A) Las piezas sugieren que el canon clásico es una construcción incompleta", "La ficha no permite afirmar superioridad."),
        ("{F} ¿Qué límite tendría una interpretación basada solo en estas cinco piezas?", "No incluye muchas otras obras, voces y culturas, y no sabemos qué se perdió", "Cinco piezas son una muestra pequeña."),
    ],
    ctx=("Para una exposición escolar debes decidir qué rótulo ponerle al conjunto de las cinco piezas del dossier. ¿Cuál es el más adecuado: «Obras perfectas del mundo antiguo» o «Un canon construido, incompleto y revisable»? {F}", "«Un canon construido, incompleto y revisable»", "Las piezas muestran selección, pérdida y diversidad."),
    sc=[("¿Qué es el límite de una interpretación?", "Lo que las fuentes no permiten saber", "Reconocerlo evita exagerar."),
        ("En Historia: ¿Qué es una evidencia?", "Un dato concreto que apoya una afirmación", "Se toma de una fuente."),
        ("¿Qué parte de una interpretación dice lo que sostienes?", "La afirmación", "La evidencia la apoya y el límite la acota.")],
    op=("Escribe una interpretación de 8 líneas con el dossier: una afirmación sobre el canon, tres evidencias de piezas distintas, un límite y una pregunta que exigiría otra fuente. {F}",
        "Afirmación: el canon clásico es una construcción incompleta; evidencias: Siete Maravillas, 7 de 120 obras de Sófocles y Gilgamesh; límite: no sabemos qué se perdió; pregunta: ¿qué escribieron las mujeres?",
        ["afirmación clara", "tres evidencias de piezas distintas", "límite y pregunta"], ["interpretación escrita"], ["afirmar más de lo que muestran las piezas", "no citar piezas concretas"],
        "Pide que explique cómo cambiaría su interpretación con una pieza nueva."),
    reinforce="Escribe una afirmación, una evidencia y un límite sobre un tema de tu curso.",
    extend="Escribe una pregunta de investigación sobre el canon de la literatura de tu país.",
)
