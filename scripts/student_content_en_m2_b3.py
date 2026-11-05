"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 13: proceso de escritura (organizar, redactar, revisar, editar,
publicar) con herramientas (procesador de textos y diccionario en línea).

Textos originales y ficticios, con pista en español; todo lo que una pregunta nombra está escrito en el enunciado.
Las 6 clases del plan tienen títulos genéricos; aquí cada una recorre un paso del proceso: organizar ideas; redactar con variedad;
revisar contenido y organización; editar ortografía y puntuación (comillas); publicar con un procesador de textos; y transferir
el proceso a cuatro propósitos (informar, analizar, opinar, narrar). Los ejercicios con herramientas describen la herramienta
en el enunciado (pantalla de ejemplo), porque el estudiante puede no tener computador; la tarea abierta se hace en papel o,
si hay, en un procesador de textos. VACÍO: el uso real de un procesador de textos y de un diccionario en línea depende del
equipamiento del establecimiento y del docente.
"""
from __future__ import annotations

from en_m2_a_common import MAT_READ, arith, lesson, task

OA = "EN2M OA 13"

# ================================================== clase 1: organizar ideas
BR = "Lluvia de ideas de ejemplo para un texto sobre «Why teenagers need hobbies». Ideas sueltas: relax, make friends, learn new skills, spend too much time on phones, sports, music, reduce stress, cooking. Propósito: informar a familias en un boletín escolar. Audiencia: adultos. Extensión: 5 oraciones."
OUT = "Esquema de ejemplo: Introduction: one sentence with the topic. Body 1: hobbies help teenagers relax. Body 2: hobbies help them make friends. Conclusion: hobbies are useful for health and friendship."

lesson(
    OA, 1, MAT_READ,
    "Aprenderé a organizar mis ideas antes de escribir: definir propósito y audiencia, hacer una lluvia de ideas y armar un esquema. Sirve para empezar a escribir con un plan claro, sea para informar, analizar, opinar o narrar.",
    ["Sé que un texto tiene inicio, desarrollo y cierre.", "Sé los conectores simples."],
    [
        "El proceso de escritura (writing process) tiene cinco pasos: organizar ideas (plan), redactar (draft), revisar (revise), editar (edit) y publicar (publish). El primer paso, organizar, responde tres preguntas: ¿para qué escribo (purpose)?, ¿quién lo leerá (audience)? y ¿cuánto debe medir (length)? Puedes escribir para informar (inform), analizar (analyse), expresar opiniones (express opinions) o narrar (narrate).",
        "La lluvia de ideas (brainstorm) es anotar rápido todas las ideas que se te ocurran, sin juzgarlas. Después seleccionas las que sirven al propósito y las agrupas. Un esquema (outline) ordena las ideas en introducción, desarrollo y conclusión. Cada párrafo del desarrollo tiene una idea principal y uno o dos ejemplos. Quita lo que no se relaciona con el propósito.",
        "Elige las palabras y expresiones que usarás: vocabulario del tema, conectores como first, also, however, as a result y expresiones de uso frecuente. Si tu propósito es narrar, necesitas personajes, lugar y orden de los hechos; si es opinar, una postura y razones; si es analizar, causas y consecuencias; si es informar, datos exactos. Con un buen plan, escribir es más rápido.",
    ],
    [("writing process", "proceso de escritura"), ("purpose", "propósito"), ("audience", "audiencia"), ("brainstorm", "lluvia de ideas"), ("outline", "esquema"), ("inform / analyse / narrate", "informar / analizar / narrar")],
    [
        ("Elegir una idea", BR + " ¿Qué idea no se relaciona con el propósito? A) cooking B) relax", ["El texto es sobre por qué los hobbies sirven a los adolescentes.", "Cooking puede ser un hobby, pero es un ejemplo y no una razón.", "La A no es una razón; las otras sí."], "A"),
        ("Esquema", OUT + " ¿Cuál es la idea del cuerpo 1? A) hobbies help teenagers relax B) hobbies are expensive", ["Leo la línea Body 1.", "Dice hobbies help teenagers relax.", "La A."], "A"),
    ],
    [
        ("Empezar a redactar sin pensar en la audiencia.", "No se sabe qué tono y qué datos usar.", "Define primero propósito y audiencia."),
        ("Incluir todas las ideas de la lluvia de ideas.", "El texto pierde foco.", "Selecciona solo las que apoyan el propósito."),
    ],
    [
        ("Lee: " + BR + " ¿Cuál es el propósito? A) informar a familias B) vender un producto", "A", "El texto dice informar a familias en un boletín."),
        ("Lee: " + BR + " ¿Cuántas oraciones debe tener el texto? A) cinco B) diez", "A", "Dice Extensión: 5 oraciones."),
        ("Lee: " + OUT + " ¿Cuál es la idea del cuerpo 2? A) hacer amigos B) ahorrar dinero", "A", "Dice help them make friends."),
    ],
    [
        ("Lee: " + BR + " ¿Cuál de estas ideas es una razón para tener un hobby? A) reduce stress B) cooking", "A", "Reducir el estrés es un beneficio."),
        ("Lee: " + BR + " ¿Quién es la audiencia? A) adultos B) niños pequeños", "A", "Dice Audiencia: adultos."),
        ("Lee: " + OUT + " ¿Dónde va la idea de que los hobbies son útiles para la salud y la amistad? A) en la conclusión B) en la introducción", "A", "Es el cierre del esquema."),
    ],
    [
        ("Lee: " + BR + " Se agrupan las ideas «make friends» y «relax». ¿Qué grupo conviene crear? A) beneficios personales y sociales B) tipos de comida", "A", "Ambos son beneficios."),
        ("Lee: " + OUT + " Si el propósito fuera opinar, ¿qué agregarías? A) una postura y una razón B) solo datos de fechas", "A", "Opinar necesita postura y razones."),
        arith("Un esquema tiene 1 párrafo de introducción, 2 de desarrollo y 1 de conclusión. Cada párrafo tendrá 3 oraciones. ¿Cuántas oraciones tendrá el texto en total?", "(1+2+1)*3", "Se multiplican los párrafos totales por las oraciones de cada uno."),
    ],
    [
        ("Lee: " + BR + " Una compañera agrega «spend too much time on phones» como ventaja. ¿Qué problema tiene? A) es un problema, no una ventaja de tener hobbies B) es una idea repetida", "A", "Se opone al propósito del texto, a menos que se use como contraste."),
        ("Lee: " + BR + " ¿Qué conector sirve para sumar una segunda razón? A) also B) however", "A", "Also agrega una idea."),
    ],
    [
        ("Ordena los pasos del proceso: a) revisar b) organizar ideas c) editar d) redactar e) publicar", "b, d, a, c, e", "El proceso empieza con organizar y termina con publicar."),
        ("Ordena el esquema: a) conclusión b) introducción c) desarrollo", "b, c, a", "Primero se presenta el tema, luego se desarrolla y al final se cierra."),
    ],
    [("Lee: «Purpose: narrate. Audience: classmates. Idea list: a rainy day, a lost umbrella, a friend who helps.» (umbrella = paraguas). ¿Cuántas ideas hay en la lista?", "3", "Hay tres ideas: lluvia, paraguas perdido y un amigo.")],
    [
        ("¿Cuáles son los cinco pasos del proceso de escritura (en Inglés, 2.º medio)?", "Organizar, redactar, revisar, editar y publicar", "Se hacen en ese orden."),
        ("¿Qué es una lluvia de ideas (en Inglés, 2.º medio)?", "Anotar rápido todas las ideas", "Luego se seleccionan."),
        ("¿Qué es un esquema (en Inglés, 2.º medio)?", "Un plan que ordena las ideas", "Tiene introducción, desarrollo y conclusión."),
    ],
    task("Elige un propósito: A) informar sobre un deporte, B) opinar sobre el uso del celular en el colegio, C) narrar un día especial. Escribe en tu hoja: propósito, audiencia, extensión, una lluvia de ocho ideas, un esquema de tres partes y tres expresiones o conectores que usarás.", "Ejemplo (B): Opinar; audiencia: el director; extensión: 6 oraciones; ideas: contacto con la familia, distracción, emergencias, etc.; esquema: intro (postura), 2 razones, conclusión; conectores: because, also, however.", ["define propósito, audiencia y extensión", "agrupa las ideas en un esquema", "elige conectores y expresiones"], ["hoja con el plan completo"], ["escribir sin definir audiencia", "incluir ideas que no apoyan el propósito"], "Explica tu plan a una persona de tu casa y escucha si entiende lo que escribirás."),
    "Haz una lluvia de ideas de diez palabras sobre tu pasatiempo favorito.",
    "Arma dos esquemas distintos para el mismo tema con propósitos diferentes.",
)

# ================================================== clase 2: redactar con variedad
DR1 = "Borrador de ejemplo: «I like music. Music is good. Music is fun. Music is relaxing. I listen to music every day.»"
DR2 = "Borrador mejorado de ejemplo: «I really enjoy music, because it helps me relax after school. Although I like many styles, I prefer calm songs when I study. In addition, I often listen to music with my friends, so we share new artists.»"

lesson(
    OA, 2, MAT_READ,
    "Aprenderé a redactar un primer borrador (draft) con variedad de palabras, de oraciones y de estructuras del nivel, y con conectores variados. Sirve para que mi texto sea claro, interesante y fluido, sin repetir siempre lo mismo.",
    ["Sé organizar ideas en un esquema.", "Sé oraciones simples y compuestas."],
    [
        "Redactar (draft) es transformar el esquema en párrafos. No busques que quede perfecto: lo importante es escribir todas las ideas. Un párrafo tiene una oración temática (topic sentence), que dice la idea principal, oraciones de apoyo (supporting sentences), con razones o ejemplos, y un cierre. Mantén el orden del esquema y escribe en el tiempo verbal adecuado.",
        "La variedad hace que un texto no sea monótono. Varía las palabras (enjoy, like, love; good, useful, relaxing), las estructuras (I prefer… because…, Although…, If I could…) y la longitud de las oraciones: mezcla oraciones cortas con otras más largas. Usa palabras de uso frecuente y también otras menos frecuentes cuando las conoces bien. No repitas siempre el mismo sujeto ni la misma estructura (Music is…).",
        "Los conectores variados unen las ideas: because (causa), so (consecuencia), although y though (contraste), in addition y also (suma), first, then y finally (orden), as a result (resultado) y unless (condición). Evita empezar todas las oraciones con and o but. Después de escribir un borrador, no lo corrijas todavía: déjalo reposar y vuelve a leerlo para revisar.",
    ],
    [("draft", "borrador"), ("topic sentence", "oración temática"), ("supporting sentence", "oración de apoyo"), ("variety", "variedad"), ("in addition", "además"), ("although", "aunque")],
    [
        ("Variar", "Para no repetir like, ¿qué verbo es sinónimo? A) enjoy B) hate", ["Busco una palabra con significado parecido.", "Enjoy significa disfrutar.", "La A."], "A"),
        ("Conector", "Completa: «I like football, ___ I am not good at it.» A) although B) so", ["Hay un contraste.", "Although introduce un contraste.", "La A."], "A"),
    ],
    [
        ("Empezar todas las oraciones con el mismo sujeto (Music is…).", "El texto suena repetitivo.", "Varía el inicio y la estructura."),
        ("Corregir cada oración antes de terminar el borrador.", "Se pierde el hilo de las ideas.", "Escribe primero todo y revisa después."),
    ],
    [
        ("Lee: " + DR1 + " ¿Qué problema tiene el borrador? A) repite Music is… en casi todas las oraciones B) tiene demasiada variedad", "A", "Music aparece al inicio de tres de las cinco oraciones."),
        ("Lee: " + DR2 + " ¿Qué conector usa para dar una causa? A) because B) although", "A", "Dice because it helps me relax."),
        ("Lee: " + DR2 + " ¿Qué palabra suma una idea? A) in addition B) so", "A", "In addition significa además."),
    ],
    [
        ("Lee: " + DR2 + " ¿Qué verbo reemplaza a like en el borrador mejorado? A) enjoy B) listen", "A", "Dice I really enjoy music."),
        ("Lee: " + DR2 + " ¿Cuál es la oración temática? A) I really enjoy music, because it helps me relax after school. B) In addition, I often listen to music with my friends.", "A", "La primera oración presenta la idea principal."),
        ("Lee: " + DR2 + " ¿Qué muestra although? A) un contraste B) una causa", "A", "Muestra que le gustan muchos estilos, pero prefiere los tranquilos."),
    ],
    [
        ("Lee: " + DR1 + " ¿Cuál de estas es una mejor versión de I like music. Music is good.? A) I like music because it is fun. B) Music, music, music.", "A", "Une dos ideas con because."),
        ("Lee: " + DR1 + " Une las ideas con un conector adecuado: «Music is relaxing. I listen to it every day.» A) Music is relaxing, so I listen to it every day. B) Music is relaxing, although I listen to it every day.", "A", "So muestra consecuencia."),
        ("Lee: " + DR2 + " ¿Cuántas oraciones tiene el borrador mejorado? A) tres B) cinco", "A", "Hay tres oraciones separadas por puntos."),
    ],
    [
        ("Lee: " + DR2 + " Una compañera dice que el borrador mejorado es demasiado largo. ¿Qué responde? A) tiene tres oraciones bien conectadas con ideas distintas B) tiene solo una idea", "A", "Cada oración aporta una idea."),
        ("Lee: " + DR1 + " ¿Qué se debe mejorar primero? A) variar estructuras y conectores B) agregar dibujos", "A", "El texto repite las oraciones cortas."),
    ],
    [
        ("Ordena un párrafo: a) Finally, I listen to music with friends. b) I enjoy music for three reasons. c) First, it helps me relax.", "b, c, a", "Primero la oración temática, luego la razón y por último el cierre."),
        ("Elige la oración más variada: A) Although it was raining, we played outside. B) We played. It was raining. We played.", "A", "Combina las ideas con un conector."),
    ],
    [("Lee: «My friend is good, my friend is nice, my friend is kind.» (kind = amable). ¿Qué palabra se repite?", "my friend is", "La misma estructura se repite tres veces.")],
    [
        ("¿Qué es un borrador (en Inglés, 2.º medio)?", "Un primer texto sin corregir", "Se revisa después."),
        ("¿Qué es una oración temática (en Inglés, 2.º medio)?", "La que dice la idea principal del párrafo", "Va al inicio."),
        ("¿Qué muestra although?", "Un contraste", "Une ideas opuestas."),
    ],
    task("Usa el esquema de la clase 1 (o crea uno nuevo) y escribe un borrador de cuatro oraciones: una oración temática, dos de apoyo con conectores distintos (because, although, in addition, so…) y un cierre. Usa al menos tres palabras distintas para expresar gusto o utilidad (enjoy, like, love, useful, helpful).", "Ejemplo: I enjoy cooking for three reasons. First, it helps me relax. Although it takes time, I like learning new recipes. Finally, cooking is useful because I can help at home.", ["incluye oración temática y cierre", "usa al menos dos conectores distintos", "varía el vocabulario"], ["borrador de cuatro oraciones"], ["repetir la misma estructura", "no usar conectores"], "Lee tu borrador a una persona de tu casa y pregunta qué idea quedó más clara."),
    "Escribe tres versiones de la misma oración con conectores distintos.",
    "Toma un párrafo repetitivo y reescríbelo con variedad de palabras y conectores.",
)

# ================================================== clase 3: revisar contenido y organización
REV1 = "Texto de ejemplo para revisar: «My neighbourhood is nice. There are many shops. I like the park because it is big. The bakery opens at seven. Also, my cousin lives near. The bakery sells the best bread. The park has a basketball court. I like it. My neighbourhood is quiet at night.»\n(neighbourhood = barrio, shops = tiendas, bakery = panadería, near = cerca, court = cancha, quiet = tranquilo)"
CHECK = "Lista de revisión de ejemplo: 1) El texto tiene una idea principal clara. 2) Cada párrafo trata una sola idea. 3) Las ideas siguen un orden lógico. 4) No hay ideas repetidas ni sobrantes. 5) Los datos son correctos. 6) Los conectores unen las ideas."

lesson(
    OA, 3, MAT_READ,
    "Aprenderé a revisar (revise) mi borrador con una lista de verificación para mejorar el contenido y la organización: claridad de la idea principal, orden, unidad y conectores. Sirve para que mi texto sea coherente antes de corregir la ortografía.",
    ["Sé redactar un borrador.", "Sé usar conectores."],
    [
        "Revisar (revise) es mirar el texto como lector y mejorarlo. Se revisan primero el contenido (content) y la organización (organisation), y recién después la ortografía y la puntuación. Para el contenido pregúntate: ¿mi idea principal está clara?, ¿tengo suficientes razones o ejemplos?, ¿hay algo que no tiene relación? Para la organización: ¿el orden es lógico?, ¿cada párrafo tiene una sola idea?",
        "Una lista de verificación (checklist) te guía: marca sí o no en cada punto. Si algo es no, mejóralo: agrega un ejemplo, cambia el orden, elimina una idea repetida o suma un conector. También puedes recibir comentarios (feedback) de un compañero: ¿qué entendió?, ¿qué le faltó?, ¿qué parte le gustó? Agradece y decide qué cambios hacer.",
        "Los cambios típicos son: reordenar oraciones, quitar las que se repiten, agregar una oración temática, unir ideas con conectores y reemplazar palabras repetidas. Revisa el texto en voz alta; si te trabas, probablemente hay un problema de orden o claridad. Guarda la versión anterior para comparar.",
    ],
    [("revise", "revisar"), ("checklist", "lista de verificación"), ("feedback", "comentarios para mejorar"), ("content", "contenido"), ("organisation", "organización"), ("unity", "unidad: una idea por párrafo")],
    [
        ("Contenido u ortografía", "Quieres cambiar el orden de dos párrafos. ¿Es contenido o ortografía? A) organización B) ortografía", ["Se cambia el orden de las ideas.", "Es organización.", "La A."], "A"),
        ("Unidad", "Un párrafo habla del parque y de la panadería. ¿Qué conviene? A) separar las ideas en dos párrafos B) borrar el texto", ["Cada párrafo tiene una idea.", "Se separan.", "La A."], "A"),
    ],
    [
        ("Corregir solo la ortografía y no revisar las ideas.", "El texto puede seguir confuso.", "Revisa primero contenido y organización."),
        ("Cambiar todo el texto después de un comentario.", "Se pierde la idea original.", "Elige los cambios que mejoran la claridad."),
    ],
    [
        ("Lee: " + REV1 + " ¿Cuál es la idea principal del texto? A) cómo es el barrio B) cómo cocinar", "A", "Dice My neighbourhood is nice."),
        ("Lee: " + REV1 + " ¿A qué hora abre la panadería? A) a las siete B) a las ocho", "A", "Dice The bakery opens at seven."),
        ("Lee: " + CHECK + " ¿Qué punto trata del orden? A) el 3 B) el 5", "A", "El 3 dice Las ideas siguen un orden lógico."),
    ],
    [
        ("Lee: " + REV1 + " ¿Qué oración parece fuera de lugar? A) Also, my cousin lives near. B) The park has a basketball court.", "A", "El primo no se relaciona con las tiendas ni el parque."),
        ("Lee: " + REV1 + " ¿Qué oraciones del texto, contando desde la primera, hablan de la panadería? A) la 4 y la 6 B) la 2 y la 7", "A", "The bakery opens at seven y The bakery sells the best bread."),
        ("Lee: " + CHECK + " ¿Qué punto se refiere a los datos? A) el 5 B) el 6", "A", "El punto 5 dice Los datos son correctos."),
    ],
    [
        ("Lee: " + REV1 + " ¿Cómo mejorarías el orden? A) agrupar las ideas del parque y las de la panadería B) dejar las ideas mezcladas", "A", "Agrupar da unidad."),
        ("Lee: " + REV1 + " La oración I like it. es poco clara. ¿Qué se debe aclarar? A) a qué se refiere it B) la hora", "A", "El pronombre no tiene referencia clara."),
        ("Lee: " + REV1 + " ¿Qué conector uniría The bakery opens at seven y The bakery sells the best bread? A) and B) unless", "A", "Se suman dos ideas sobre la panadería."),
    ],
    [
        ("Lee: " + REV1 + " Un compañero dice que falta una conclusión. ¿Qué agregarías? A) una oración que cierre la idea del barrio B) un chiste", "A", "La conclusión cierra la idea principal."),
        ("Lee: " + CHECK + " El texto repite la misma idea en dos oraciones. ¿Qué punto no se cumple? A) el 4 B) el 5", "A", "El punto 4 dice No hay ideas repetidas ni sobrantes."),
    ],
    [
        ("Ordena los pasos de la revisión: a) leer en voz alta b) usar la lista de verificación c) hacer los cambios d) comparar con la versión anterior", "a, b, c, d", "Se lee, se marca, se cambia y se compara."),
        ("Reordena para dar unidad: a) Finally, I love the park because it is quiet. b) First, the park has a basketball court. c) My neighbourhood has a great park.", "c, b, a", "Primero se presenta el parque, luego First y al final Finally."),
    ],
    [("Lee: «My room is small. It has a bed, a desk and a shelf. My brother’s room is bigger. I like my room because it is cosy.» (shelf = repisa, cosy = acogedor). ¿Qué oración habla de otra habitación y puede sobrar?", "My brother’s room is bigger.", "Rompe la unidad del párrafo sobre mi habitación.")],
    [
        ("¿Qué se revisa primero?", "El contenido y la organización", "La ortografía va después."),
        ("¿Para qué sirve una lista de verificación (en Inglés, 2.º medio)?", "Para marcar si el texto cumple cada punto", "Guía la revisión."),
        ("¿Qué es la unidad de un párrafo?", "Que trate una sola idea", "Hace el texto más claro."),
    ],
    task("Toma el borrador de la clase 2 (o el texto de ejemplo REV1) y revísalo con una lista de seis puntos. Marca sí o no en cada uno, anota tres cambios que harías (por ejemplo: reordenar, quitar una oración, agregar un conector) y escribe la versión revisada. Pide a una persona de tu casa que te dé un comentario.", "Ejemplo: Sí: idea principal clara. No: había una oración repetida. Cambios: quitar I like it; agrupar las ideas del parque; agregar However entre las ideas. Versión revisada: My neighbourhood is quiet and nice. The park is big and has a court. The bakery opens at seven…", ["marca la lista con sí o no", "anota tres cambios concretos", "escribe una versión revisada"], ["lista marcada", "versión revisada", "comentario de la persona"], ["corregir solo la ortografía", "no incluir los cambios"], "Compara la versión antigua y la nueva y subraya la mejora principal."),
    "Pide a un compañero que lea tu texto y te diga cuál es la idea principal.",
    "Crea tu propia lista de revisión de ocho puntos para un texto de opinión.",
)

# ================================================== clase 4: editar ortografía y puntuación
ED1 = "Texto de ejemplo con errores: «My frend said, I recieve a letter tomorow. We was very exited becuase it was diferent. She told me, Its beautifull.»"
ED2 = "Texto corregido de ejemplo: «My friend said, “I will receive a letter tomorrow.” We were very excited because it was different. She told me, “It’s beautiful.”»"
DICT = "Pantalla de ejemplo de un diccionario en línea. Palabra buscada: «necessary». Clase: adjetivo. Significado: «que se necesita o es indispensable». Ejemplo: «A passport is necessary to travel abroad.» Pronunciación: /ˈnesəseri/. Sinónimo: essential."

lesson(
    OA, 4, MAT_READ,
    "Aprenderé a editar (edit) un texto: corregir la ortografía de palabras de uso frecuente, la puntuación (comillas) y la gramática, y a usar un diccionario en línea. Sirve para entregar un texto correcto y fácil de leer.",
    ["Sé revisar el contenido y la organización.", "Sé usar un diccionario."],
    [
        "Editar (edit) es corregir la forma: ortografía (spelling), puntuación (punctuation), mayúsculas y gramática. Pon especial atención en las palabras de uso frecuente, porque se repiten mucho: because, friend, different, beautiful, receive, tomorrow, necessary, separate, definitely, though, through, until, address, Wednesday. Escríbelas siempre igual: la consistencia (consistency) muestra cuidado.",
        "Las comillas (quotation marks) se usan para citar lo que alguien dice: She said, “I am ready.” Antes de la cita va una coma, las comillas abren y cierran la cita, y el punto final queda dentro de las comillas en este cuaderno. También se usan para títulos cortos: “The Last Bus”. El apóstrofo (’) forma contracciones (It’s = it is) y posesión (Diego’s). No confundas its (de él/ello) con it’s (it is).",
        "Un diccionario en línea (online dictionary) te da el significado, la clase de palabra, ejemplos, pronunciación y a veces sinónimos. Úsalo para comprobar la ortografía, elegir la palabra adecuada y ver cómo se usa en una oración. No copies la primera definición sin leer el ejemplo. Después de editar, lee el texto una vez más, de atrás hacia adelante o en voz alta, para encontrar errores que se escapan.",
    ],
    [("spelling", "ortografía"), ("punctuation", "puntuación"), ("quotation marks", "comillas"), ("edit", "editar"), ("online dictionary", "diccionario en línea"), ("consistency", "consistencia")],
    [
        ("Ortografía", "¿Cuál es la ortografía correcta? A) friend B) freind", ["Reviso la palabra.", "Se escribe friend.", "La A."], "A"),
        ("Comillas", "¿Cuál está bien escrita? A) She said, “I am ready.” B) She said I am ready.”", ["La cita lleva comillas de apertura y cierre.", "La A.", "La B no abre comillas."], "A"),
    ],
    [
        ("Escribir recieve o becuase.", "Se cambia el orden de las letras.", "Escribe receive y because; revisa en el diccionario."),
        ("Confundir its con it’s.", "It’s significa it is; its indica posesión.", "Prueba reemplazando por it is."),
    ],
    [
        ("Lee: " + ED1 + " ¿Cuál es la escritura correcta de tomorow? A) tomorrow B) tomorow", "A", "Se escribe con dos r."),
        ("Lee: " + ED1 + " ¿Cuál es la escritura correcta de exited? A) excited B) exciting", "A", "La palabra pedida es excited."),
        ("Lee: " + DICT + " ¿Qué sinónimo da el diccionario? A) essential B) necessity", "A", "El diccionario dice Sinónimo: essential."),
    ],
    [
        ("Lee: " + ED1 + " ¿Qué falta en la cita de la primera oración? A) comillas B) tildes", "A", "La cita necesita comillas."),
        ("Lee: " + ED2 + " ¿Qué verbo se corrigió en We was? A) were B) are", "A", "Con we se usa were."),
        ("Lee: " + DICT + " ¿Qué clase de palabra es necessary? A) adjetivo B) verbo", "A", "El diccionario dice adjetivo."),
    ],
    [
        ("Lee: " + ED1 + " ¿Cuál es la corrección de Its beautifull? A) It’s beautiful B) Its beautifull", "A", "It’s es it is y beautiful se escribe con un l final."),
        ("Lee: " + ED2 + " ¿Dónde queda el punto final de la cita? A) dentro de las comillas B) fuera de las comillas", "A", "En este cuaderno el punto va dentro."),
        ("Lee: " + DICT + " ¿Para qué sirve el ejemplo del diccionario? A) para ver cómo se usa la palabra B) para llenar espacio", "A", "Muestra el uso en una oración."),
    ],
    [
        ("Lee: " + ED1 + " La oración We was very exited tiene un error de gramática y uno de ortografía. ¿Cuál es el de gramática? A) was, debe ser were B) very", "A", "Con we se usa were; exited es el error de ortografía."),
        ("Lee: " + ED2 + " ¿Qué palabra cambió de diferent a different? A) se agregó una f B) se quitó una i", "A", "La palabra correcta lleva dos f."),
    ],
    [
        ("Ordena los pasos de edición: a) buscar dudas en el diccionario b) corregir los errores c) leer el texto de nuevo", "a, b, c", "Primero se busca, luego se corrige y por último se vuelve a leer."),
        ("Elige la oración con puntuación correcta: A) My teacher said, “Hand in your work.” B) My teacher said “Hand in, your work.”", "A", "La coma va antes de la cita."),
    ],
    [("Lee: «Wednesday» y «Wensday». ¿Cuál es la ortografía correcta?", "Wednesday", "Se escribe con una d antes de nes.")],
    [
        ("¿Qué se corrige al editar (en Inglés, 2.º medio)?", "La ortografía, la puntuación y la gramática", "Es la forma del texto."),
        ("¿Para qué se usan las comillas?", "Para citar lo que dice alguien", "Se abren y se cierran."),
        ("¿Qué diferencia hay entre its e it’s?", "It’s es it is; its indica posesión", "Se prueban con it is."),
    ],
    task("Corrige este texto en una hoja: «My frend said, I recieve a message tomorow. We was exited becuase it was diferent. She told me, Its beautifull.» Escríbelo corregido, con comillas, tres palabras de ortografía comprobadas y una explicación de dos errores de gramática o puntuación. Si puedes, comprueba una palabra en un diccionario en línea.", "Texto: My friend said, “I will receive a message tomorrow.” We were excited because it was different. She told me, “It’s beautiful.” Explicaciones: We was → We were (concordancia); Its → It’s (contracción).", ["corrige las palabras y las comillas", "explica dos errores", "revisa la versión final"], ["texto corregido en la hoja"], ["escribir recieve o becuase", "no cerrar las comillas"], "Léele el texto corregido a una persona de tu casa y pídele que marque algún error que haya pasado desapercibido."),
    "Haz una lista de diez palabras que escribes mal y escribe la forma correcta.",
    "Busca cinco palabras nuevas en un diccionario en línea y escribe una oración con cada una.",
)

# ================================================== clase 5: publicar con procesador de textos
WP = "Pantalla de ejemplo de un procesador de textos. Barra de herramientas: Bold (negrita), Italic (cursiva), Font size (tamaño de letra), Spell check (corrector ortográfico), Insert image (insertar imagen), Print (imprimir). El documento tiene el título «My City» en tamaño 16, un párrafo de 5 oraciones en tamaño 12, una imagen y la firma del autor. El corrector subraya en rojo la palabra «tomorow» y propone «tomorrow»."

lesson(
    OA, 5, MAT_READ,
    "Aprenderé a publicar (publish) mi texto final con una presentación cuidada, usando un procesador de textos y otras herramientas. Sirve para entregar un texto claro, atractivo y listo para que otras personas lo lean.",
    ["Sé revisar y editar un texto.", "Sé usar un procesador de textos básico."],
    [
        "Publicar (publish) es compartir tu texto final con una audiencia real: la profesora, tu curso, tu familia o un boletín. Antes de publicar, el texto debe estar revisado y editado. Decide el formato: un documento impreso, una presentación, un afiche, un blog o un correo. Cada formato tiene reglas: un afiche usa letra grande y pocas palabras; un correo, saludo y cierre.",
        "Un procesador de textos (word processor) tiene herramientas útiles: negrita (bold) para títulos, cursiva (italic) para títulos de obras, tamaño de letra, márgenes, corrector ortográfico (spell check) e imágenes. El corrector marca errores, pero no siempre acierta: puede aceptar una palabra correcta usada en el lugar equivocado (there en vez de their). Revisa tú mismo después de usarlo.",
        "Una buena presentación tiene un título claro, un tamaño de letra legible (por ejemplo, 12 para el texto), párrafos separados, poco color, imágenes que apoyan el contenido y tu nombre. Lee el texto impreso o en pantalla una última vez antes de entregarlo. Si trabajas en papel, usa letra clara, márgenes y espacios entre párrafos.",
    ],
    [("publish", "publicar"), ("word processor", "procesador de textos"), ("spell check", "corrector ortográfico"), ("bold", "negrita"), ("italic", "cursiva"), ("format", "formato")],
    [
        ("Herramienta", "Quieres resaltar el título. ¿Qué herramienta usas? A) negrita B) corrector ortográfico", ["Quiero destacar el título.", "La negrita lo hace.", "La A."], "A"),
        ("Corrector", "El corrector no marca there en vez de their. ¿Por qué? A) porque ambas existen y están bien escritas B) porque no sabe inglés", ["Ambas palabras existen.", "El corrector no sabe cuál debes usar.", "La A."], "A"),
    ],
    [
        ("Confiar solo en el corrector.", "Puede aceptar palabras correctas en el lugar equivocado.", "Después del corrector, lee tú mismo."),
        ("Usar letra pequeña y muchos colores.", "El texto se hace difícil de leer.", "Elige un tamaño legible y pocos colores."),
    ],
    [
        ("Lee: " + WP + " ¿Qué tamaño tiene el título? A) 16 B) 12", "A", "Dice el título en tamaño 16."),
        ("Lee: " + WP + " ¿Qué palabra subraya el corrector en rojo? A) tomorow B) tomorrow", "A", "Subraya tomorow y propone tomorrow."),
        ("Lee: " + WP + " ¿Cuántas oraciones tiene el párrafo? A) cinco B) diez", "A", "Dice un párrafo de 5 oraciones."),
    ],
    [
        ("Lee: " + WP + " ¿Para qué sirve el botón Insert image? A) para agregar una imagen B) para imprimir", "A", "Image significa imagen."),
        ("Lee: " + WP + " ¿Qué botón usarías para escribir un título de obra en cursiva? A) Italic B) Bold", "A", "Italic es cursiva."),
        ("Lee: " + WP + " ¿Qué pasa si aceptas la sugerencia del corrector? A) la palabra queda bien escrita B) el texto se borra", "A", "El corrector propone tomorrow."),
    ],
    [
        ("Lee: " + WP + " ¿Qué falta en el documento para publicarlo en un boletín? A) comprobar que el contenido esté revisado y editado B) cambiar el color", "A", "La revisión va antes de publicar."),
        ("Lee: " + WP + " El título está en tamaño 16 y el texto en 12. ¿Por qué es una buena decisión? A) el título se distingue del texto B) el texto es muy grande", "A", "Un tamaño distinto destaca el título."),
        arith("Un documento tiene 3 párrafos de 4 oraciones cada uno y una conclusión de 2 oraciones. ¿Cuántas oraciones tiene en total?", "3*4+2", "Se multiplican los párrafos por sus oraciones y se suma la conclusión."),
    ],
    [
        ("Lee: " + WP + " Una compañera dice que no hace falta leer el texto si el corrector no marcó errores. ¿Qué respondes? A) el corrector no detecta todos los errores B) el corrector detecta todo", "A", "No detecta errores de uso, como there y their."),
        ("¿Cuál es el mejor formato para anunciar una actividad en el pasillo? A) un afiche con letra grande B) un párrafo largo", "A", "Un afiche se lee desde lejos."),
    ],
    [
        ("Ordena los pasos antes de publicar: a) elegir el formato b) revisar y editar c) darle formato al documento d) entregar o compartir", "b, a, c, d", "Primero el texto debe estar listo y luego se elige el formato."),
        ("Elige una presentación mejor: A) título claro, letra 12, párrafos separados B) letra 6 con muchos colores", "A", "La claridad ayuda al lector."),
    ],
    [("Lee: «To publish a short story for the school website, Ana chooses letter size 12, a title in bold and one image.» (website = sitio web). ¿Qué tamaño de letra elige?", "12", "Dice letter size 12.")],
    [
        ("¿Qué es publicar un texto?", "Compartirlo con una audiencia real", "Se hace después de editar."),
        ("¿Para qué sirve la negrita (en Inglés, 2.º medio)?", "Para destacar", "Se usa en títulos."),
        ("¿Por qué no basta el corrector ortográfico?", "No detecta todos los errores de uso", "Hay que leer el texto."),
    ],
    task("Elige un texto corto que hayas escrito en esta unidad (o escribe uno nuevo de cuatro oraciones). Prepara su versión final en papel o en un procesador de textos: título, tamaño de letra legible, párrafos, nombre y, si quieres, un dibujo o una imagen. Anota las tres herramientas o decisiones de formato que usaste y a quién se lo compartirás.", "Ejemplo: Título en grande, letra 12, dos párrafos, dibujo de mi barrio y mi nombre. Herramientas: negrita en el título, corrector ortográfico, imagen. Audiencia: mi familia.", ["texto revisado y editado", "tres decisiones de formato", "audiencia real"], ["versión final del texto"], ["usar letra muy pequeña", "publicar sin revisar"], "Comparte el texto con la audiencia elegida y pregunta qué parte les gustó más."),
    "Diseña un afiche de ejemplo con título, tres palabras clave y una imagen para anunciar un evento del colegio.",
    "Compara dos versiones de un mismo texto y escribe qué hace más legible a una de ellas.",
)

# ================================================== clase 6: repasar, reparar y transferir a cuatro propósitos
TEXT_INF = "Texto A: «The school library has 3,000 books. It opens from Monday to Friday at eight. Students can borrow two books for two weeks.»"
TEXT_ANA = "Texto B: «Many students arrive late because the bus is slow. As a result, they lose the first lesson. The council should buy a faster bus.»"
TEXT_OPI = "Texto C: «I believe that school should start later, because teenagers need more sleep. Although some parents disagree, I think the change will help.»"
TEXT_NAR = "Texto D: «Last Saturday, I forgot my keys. I waited outside for an hour. Finally, my neighbour opened the door and gave me a hot tea.»"

lesson(
    OA, 6, MAT_READ,
    "Aprenderé a aplicar todo el proceso de escritura a cuatro propósitos distintos (informar, analizar, opinar y narrar), a reparar un texto con problemas y a transferir lo aprendido a un caso nuevo. Sirve para escribir con autonomía en inglés.",
    ["Sé organizar, redactar, revisar, editar y publicar.", "Sé conectores y comillas."],
    [
        "El proceso de escritura es el mismo en todos los textos: organizar, redactar, revisar, editar y publicar. Lo que cambia es el propósito. Para informar (inform), usas datos exactos y un orden claro: The library has 3,000 books. Para analizar (analyse), explicas causas y consecuencias con conectores como because y as a result. Para opinar (express an opinion), das una postura con razones: I believe that… because… Para narrar (narrate), cuentas hechos en orden con pasado y palabras como last Saturday, finally.",
        "Reparar (repair) un texto significa encontrar qué falla y arreglarlo. Si el propósito no está claro, reescribe la primera oración. Si hay ideas fuera de lugar, reordénalas. Si faltan conectores, agrégalos. Si hay errores de ortografía o de puntuación, edítalos. Piensa en el lector: ¿entiende qué quieres lograr?",
        "Transferir es usar lo aprendido en una situación nueva: cambiar el tema, la audiencia o el formato. Un mismo tema (el transporte, por ejemplo) puede servir para informar, analizar, opinar o narrar. Antes de escribir, define el propósito con una oración: My purpose is to… Al terminar, evalúa tu texto con una lista y decide qué mejorarías la próxima vez.",
    ],
    [("inform", "informar: dar datos"), ("analyse", "analizar: explicar causas y consecuencias"), ("express an opinion", "opinar: dar una postura con razones"), ("narrate", "narrar: contar hechos en orden"), ("repair", "reparar"), ("transfer", "transferir: usar lo aprendido en un caso nuevo")],
    [
        ("Reconocer propósito", TEXT_INF + " ¿Qué propósito tiene? A) informar B) narrar", ["Da datos exactos.", "No cuenta una historia ni opina.", "La A."], "A"),
        ("Reconocer propósito", TEXT_NAR + " ¿Qué propósito tiene? A) narrar B) analizar", ["Cuenta hechos pasados en orden.", "Usa Last Saturday y Finally.", "La A."], "A"),
    ],
    [
        ("Usar los mismos recursos para todos los propósitos.", "Cada propósito pide recursos distintos.", "Elige datos, causas, razones o hechos según el propósito."),
        ("Pensar que corregir la ortografía basta para mejorar un texto.", "Pueden fallar el propósito y la organización.", "Revisa primero la idea y el orden."),
    ],
    [
        ("Lee: " + TEXT_INF + " ¿Cuántos libros tiene la biblioteca? A) 3.000 B) 300", "A", "Dice 3,000 books."),
        ("Lee: " + TEXT_ANA + " ¿Por qué llegan tarde los estudiantes? A) porque el bus es lento B) porque se levantan tarde", "A", "Dice because the bus is slow."),
        ("Lee: " + TEXT_OPI + " ¿Qué postura expresa? A) que el colegio debería empezar más tarde B) que debería empezar más temprano", "A", "Dice school should start later."),
    ],
    [
        ("Lee: " + TEXT_ANA + " ¿Qué conector muestra la consecuencia? A) as a result B) although", "A", "As a result introduce la consecuencia."),
        ("Lee: " + TEXT_OPI + " ¿Qué razón da? A) que los adolescentes necesitan más sueño B) que los padres lo piden", "A", "Dice because teenagers need more sleep."),
        ("Lee: " + TEXT_NAR + " ¿Qué ocurrió al final? A) el vecino abrió la puerta y le dio té B) encontró las llaves", "A", "Dice Finally, my neighbour opened the door and gave me a hot tea."),
    ],
    [
        ("Lee: " + TEXT_INF + " ¿Cuántos libros puede pedir prestados cada estudiante? A) dos B) tres", "A", "Dice borrow two books for two weeks."),
        ("Lee: " + TEXT_ANA + " ¿Qué tipo de oración es The council should buy a faster bus? A) una propuesta de solución B) un hecho", "A", "Should plantea una solución posible, no un dato comprobado."),
        ("Lee: " + TEXT_NAR + " ¿Qué palabras ordenan los hechos? A) Last Saturday y Finally B) outside y door", "A", "Marcan el orden temporal."),
    ],
    [
        ("Lee: " + TEXT_OPI + " Un compañero dice que el texto C no tiene argumentos. ¿Qué lo contradice? A) hay una razón con because y un contraste con although B) tiene más de dos oraciones", "A", "La razón y el contraste son argumentos."),
        ("Lee: " + TEXT_ANA + " ¿Qué dato haría más sólido este análisis? A) cuántos estudiantes llegan tarde cada semana B) el color del bus", "A", "Una cifra apoya la causa y la consecuencia."),
    ],
    [
        ("Une cada propósito con su recurso principal. 1) informar 2) analizar 3) opinar 4) narrar. Recursos: a) razones con because b) datos exactos c) orden de hechos en pasado d) causas y consecuencias", "1-b, 2-d, 3-a, 4-c", "Cada propósito usa recursos distintos."),
        ("Repara la oración: «Bus slow, student late.» A) The bus is slow, so students arrive late. B) Bus, student, slow, late.", "A", "Se restauran verbos, artículos y conectores."),
    ],
    [("Lee: «Purpose: inform. Text: Our school has 24 classrooms and 6 labs.» (classrooms = salas, labs = laboratorios). ¿Cuántas salas y laboratorios hay en total?", "30", "24 más 6 son 30.")],
    [
        ("¿Qué recursos usa un texto de opinión?", "Una postura y razones", "Se apoyan con because."),
        ("¿Qué muestra as a result (en proceso de escritura)?", "Una consecuencia", "Se usa al analizar."),
        ("¿Qué significa transferir lo aprendido?", "Usarlo en una situación nueva", "Cambia el tema o la audiencia."),
    ],
    task("Elige un mismo tema (por ejemplo, el transporte para ir al colegio) y escribe cuatro mini textos de dos oraciones: uno para informar, uno para analizar (causa y consecuencia), uno para opinar (postura y razón) y uno para narrar (hechos en pasado). Luego elige el que quieras publicar, revísalo con una lista de seis puntos, edítalo y escribe la versión final.", "Ejemplo: Inform: 120 students take the bus. Analyse: The bus is slow, so many students arrive late. Opinion: I believe that we need a faster bus because time is important. Narrate: Last Monday, the bus arrived late. I ran to school and arrived five minutes after the bell.", ["escribe los cuatro propósitos con recursos distintos", "revisa y edita uno", "la versión final se entiende"], ["cuatro mini textos y una versión final"], ["usar los mismos recursos en los cuatro", "no revisar antes de publicar"], "Lee tus cuatro textos a una persona de tu casa y pídele que adivine el propósito de cada uno."),
    "Escribe un mismo tema de cuatro formas distintas, una por propósito.",
    "Crea una lista de verificación final para tus textos con diez puntos.",
)
