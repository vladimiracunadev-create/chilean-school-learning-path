"""Cuaderno del estudiante, 8.º básico Inglés (oficial): IN08 OA 12, estrategias de comprensión lectora.

Los textos en inglés son originales, breves y llevan glosario en español dentro del enunciado. Cada estrategia se enseña
en la clase antes de usarla. Las imágenes y los organizadores gráficos se describen con palabras dentro del enunciado,
para poder resolverlos sin material externo. Sin audio.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "IN08 OA 12"


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ============================================================ clase 1: antes de leer (propósito, predicción, conocimientos previos)
H1A = "Título: «Night Bus to the South». Subtítulo: «A boy travels alone for the first time». Imagen: un niño con mochila mira por la ventana del bus el camino oscuro."
H1B = "Título: «Library Rules». Subtítulo: «Please read before you borrow a book». Imagen: una lista con tres casillas marcadas."
H1C = "Título: «A Quiet Morning». Primera línea: «At six o'clock, a loud alarm woke the whole street.» (alarm = alarma; woke = despertó; whole = toda)"

lesson(
    OA, 1,
    "Los títulos, subtítulos e imágenes descritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé tres estrategias para antes de leer: fijar un propósito, hacer predicciones y usar lo que ya sé. Sirve para entrar a un texto en inglés con una idea clara de qué buscar.",
    ["Sé leer títulos y oraciones simples en inglés.", "Conozco palabras como title, image y story."],
    [
        "Antes de leer, pregúntate para qué vas a leer. Este es el propósito (purpose). Hay cuatro frecuentes: para encontrar un dato (a timetable, un horario), para seguir pasos (a recipe, una receta), para disfrutar (a story, un cuento) y para aprender sobre un tema (an article, un artículo). El propósito decide cómo lees: despacio, rápido o buscando una palabra.",
        "Luego haz una predicción (prediction): una idea de lo que el texto tratará, usando el título (title), el subtítulo (subtitle, línea bajo el título que da más datos), las imágenes y la primera línea. Escríbela con la fórmula «I think the text is about… because…». Una predicción no es una respuesta fija: se confirma o se cambia mientras lees.",
        "Por último, activa tus conocimientos previos (prior knowledge): lo que ya sabes del tema. Si el título habla del ciclo del agua, ya sabes que la lluvia viene de las nubes. Eso te ayuda a entender palabras nuevas y a notar qué información es nueva. Estas tres estrategias se hacen en pocos minutos y mejoran mucho la comprensión.",
    ],
    [("purpose", "propósito: para qué leo"), ("predict / prediction", "predecir / predicción"), ("prior knowledge", "conocimientos previos"), ("title / subtitle", "título / subtítulo"), ("image", "imagen"), ("I think… because…", "creo que… porque…")],
    [
        ("Fijar el propósito y predecir", "Título: «How to Make a Paper Plane». Subtítulo: «Five easy steps». Imagen: dos manos doblando una hoja. ¿Cuál es el propósito de leerlo y qué predices?",
         ["El subtítulo habla de cinco pasos fáciles: son instrucciones.", "El propósito es seguir pasos para hacer algo.", "Predicción: veré una lista numerada con verbos como fold (doblar)."], "Propósito: seguir pasos. Predicción: instrucciones numeradas para hacer un avión de papel."),
        ("Usar los conocimientos previos", "Título: «The Moon and the Tides». Ya sabes que el mar sube y baja durante el día. ¿Qué conocimiento previo usas y qué predices? (tides = mareas)",
         ["Lo que sabes: el nivel del mar sube y baja.", "El título junta la Luna con las mareas.", "Predicción: el texto explicará cómo se relacionan."], "Conocimiento previo: el mar sube y baja. Predicción: el texto explicará la relación entre la Luna y las mareas."),
    ],
    [
        ("Decidir que una predicción es siempre correcta.", "Una predicción es una idea inicial, no un dato.", "Confírmala o cámbiala con lo que dice el texto."),
        ("Leer sin preguntarse para qué se lee.", "Sin propósito no sabes qué buscar ni a qué velocidad leer.", "Antes de leer, elige uno de los cuatro propósitos."),
    ],
    [
        ("Para seguir los pasos de una receta, tu propósito es: a) seguir instrucciones b) disfrutar un poema", "a", "Una receta se lee para hacer algo paso a paso."),
        ("«Predict» significa: a) decir qué creo que tratará el texto antes de leer b) copiar el texto en la hoja", "a", "Predecir es anticipar con pistas como el título o las imágenes."),
        ("El subtítulo es: a) la línea bajo el título que da más información b) la última palabra del texto", "a", "Está justo debajo del título y amplía su idea."),
    ],
    [
        (f"{H1A} ¿Qué tipo de texto predices? a) A story b) A timetable", "a", "El subtítulo cuenta lo que hace un niño; una historia sobre un viaje."),
        (f"{H1A} ¿Cuál es una predicción razonable? a) The boy will feel excited or nervous on the trip b) The boy will cook dinner", "a", "El título y el subtítulo hablan de un viaje solo por primera vez."),
        (f"{H1B} ¿Cuál es el propósito más probable? a) Learn what to do when you borrow books b) Enjoy a funny story", "a", "El subtítulo pide leer antes de pedir prestado un libro."),
    ],
    [
        ("Título: «Recycle Your Phone: Where and How». ¿Qué predices del contenido? (recycle = reciclar) a) Places and steps to recycle old phones b) A funny story about a phone", "a", "El título pregunta dónde y cómo, así que contendrá lugares y pasos."),
        ("Título: «The Water Cycle». ¿Qué conocimiento previo ayuda más? a) Rain comes from clouds b) Cats are mammals", "a", "Sabes de la lluvia y las nubes, y se relaciona con el agua."),
        ("Cartel: «Ticket prices: adults $3.000, children $1.500. Open 10:00 to 18:00.» (ticket = entrada) ¿Cuál es tu propósito si quieres saber cuánto pagas por una entrada? a) Find a specific piece of information b) Enjoy a poem", "a", "Buscas un dato, el precio."),
    ],
    [
        (f"{H1C} Predijiste que sería una mañana tranquila por el título. ¿Qué haces con tu predicción al leer la primera línea? a) La cambias, porque la alarma fuerte despierta toda la calle b) La mantienes, porque el título decide siempre de qué trata el texto", "a", "La primera línea trae información nueva que contradice la predicción."),
        ("Título: «The Last Day of Summer Camp». Imagen: niños y niñas se despiden con la mano frente a un bus. Ana predice: «It will be about goodbyes and memories». Bruno predice: «It will explain how to build a tent». ¿Qué predicción tiene más pistas? Escribe Ana o Bruno. (camp = campamento)", "Ana", "El título habla del último día y la imagen muestra una despedida; nada habla de construir carpas."),
    ],
    [
        ("Elige la predicción mejor escrita. Título: «Eruption!», imagen de una montaña con humo. a) I think the text is about volcanoes because the image shows a mountain with smoke and the title says eruption. b) I think the text is about volcanoes.", "a", "La primera da la razón con pistas; la segunda no."),
        ("Quieres saber a qué hora cierra el museo. Hay dos textos: texto 1, «A poem about museums»; texto 2, «Visit guide: open Tuesday to Sunday, 10:00 to 17:00». ¿Cuál lees? Escribe 1 o 2.", "2", "La guía de visita contiene los horarios que buscas."),
    ],
    [("Un amigo te muestra un afiche: «Free Chess Workshop» y debajo, el subtítulo: «Saturday, school library, 11:00». (workshop = taller; library = biblioteca) Para saber cuándo y dónde es, ¿qué parte lees primero? a) El subtítulo b) La imagen del tablero", "a", "El subtítulo trae el día, el lugar y la hora.")],
    [
        ("En Inglés (oficial): ¿Qué es el propósito de lectura?", "Para qué leo", "Define si busco un dato, sigo pasos, disfruto o aprendo."),
        ("¿Qué fórmula sirve para escribir una predicción: I think… because… o I am…?", "I think… because…", "Une la idea con una razón."),
        ("Lo que ya sabes de un tema se llama: a) conocimientos previos b) subtítulo", "a", "Son los conocimientos previos o prior knowledge."),
    ],
    task("Lee esta información de un afiche: Título: «Sea Turtles: Guardians of the Ocean». Subtítulo: «Why they need our help». Imagen: una tortuga marina nada cerca de una bolsa de plástico. (sea turtles = tortugas marinas; guardians = guardianas; help = ayuda; bag = bolsa) En tu hoja escribe: tu propósito de lectura, una predicción con «I think… because…» y un conocimiento previo que tengas.", "Propósito: aprender sobre las tortugas marinas. I think the text is about the problem of plastic in the sea because the image shows a bag near a turtle. Conocimiento previo: las tortugas viven en el mar.", ["nombra uno de los cuatro propósitos", "escribe la predicción con la fórmula y una razón del afiche", "añade un conocimiento previo relacionado"], ["tres líneas en la hoja"], ["predicción sin razón", "conocimiento previo que no tiene relación con el tema"], "Pide que cambie la predicción si el texto empieza con «Turtles eat jellyfish», y que explique por qué la cambió."),
    "Copia los cuatro propósitos de lectura y escribe un ejemplo de texto para cada uno.",
    "Elige un libro de tu casa, lee el título y la portada, y escribe una predicción con I think… because….",
)

# ============================================================ clase 2: durante la lectura (lectura rápida, focalizada y elementos del texto)
ART2 = "Title: Green Point, a New Recycling Centre. Subtitle: Open to all neighbours. Caption of the photo: Volunteers sort paper and plastic. Paragraph 1: Green Point opened in March in the north of the city. Neighbours bring paper, plastic and cans. Paragraph 2: The centre is open from Tuesday to Saturday, from 9:00 to 17:00. It is closed on Sunday and Monday. Paragraph 3: Entry is free. Children under twelve must come with an adult. There is also a small garden where families learn to make compost."
G_ART2 = "(recycling centre = centro de reciclaje; neighbours = vecinos; sort = clasifican; cans = latas; closed = cerrado; entry = entrada; compost = abono natural)"
MUS2 = "Museum of Sea Stories. Open: Wednesday to Sunday, 10:00 to 18:00. Tickets: adults $4.000, students $2.000, children under six free. Guided tours at 11:00 and at 15:00."
G_MUS2 = "(museum = museo; tickets = entradas; guided tours = visitas guiadas)"

lesson(
    OA, 2,
    "Los textos y avisos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer rápido para captar la idea general (skimming), a leer focalizado para encontrar un dato (scanning) y a usar los elementos del texto como título, subtítulo e imágenes. Sirve para leer en inglés con más rapidez y menos miedo.",
    ["Conozco los propósitos de lectura y sé predecir con el título.", "Sé leer números, días y horas en inglés."],
    [
        "Durante la lectura (while reading) usas dos tipos de lectura. La lectura rápida (skimming) sirve para captar la idea general: lees el título, el subtítulo, las imágenes y la primera oración de cada párrafo, sin detenerte en palabras difíciles. La lectura focalizada (scanning) sirve para encontrar un dato exacto: tu mirada recorre el texto y se detiene solo en números, nombres, días u otras palabras que buscas.",
        "Los elementos organizacionales (organizational features) te muestran cómo está organizado un texto: el título, el subtítulo, las imágenes con su leyenda (caption), las palabras en negrita (bold) y los párrafos numerados. Dicen de qué trata cada parte antes de leerla. Por ejemplo, una leyenda que dice «Students plant a tree in the schoolyard» te cuenta qué muestra la foto.",
        "Para decidir cuál usar, mira tu propósito. Si quieres saber de qué trata un artículo, haz skimming. Si quieres saber a qué hora abre un lugar, haz scanning y busca la hora. No necesitas leer todo con la misma atención. Primero ubica dónde está lo que buscas, luego lee esa parte con cuidado y comprueba tu respuesta.",
    ],
    [("skimming", "lectura rápida para la idea general"), ("scanning", "lectura focalizada para buscar un dato"), ("caption", "leyenda de una imagen"), ("bold", "negrita: palabras destacadas"), ("gist", "idea general"), ("paragraph", "párrafo"), ("organizational features", "elementos que organizan un texto")],
    [
        ("Hacer skimming para la idea general", "Texto: «Title: Our Library Opens on Saturdays. Subtitle: New hours for students. Paragraph 1: From now on, the school library opens on Saturdays from 10:00 to 13:00. Paragraph 2: Students can read, borrow books and use the computers.» (opens = abre; hours = horario; borrow = pedir prestado) ¿Cuál es la idea general?",
         ["Lee el título y el subtítulo: nuevo horario para estudiantes.", "La primera oración del párrafo 1 repite la idea.", "La idea general: la biblioteca abre ahora los sábados."], "La biblioteca del colegio ahora abre los sábados."),
        ("Hacer scanning para un dato", "Texto: «Weather in Punta Arenas. Monday: rain, 7 degrees. Tuesday: wind, 5 degrees. Wednesday: sun, 9 degrees.» (rain = lluvia; wind = viento; sun = sol; degrees = grados) ¿Qué día hace 9 grados?",
         ["Busca el número 9 sin leer todo.", "El 9 está al lado de Wednesday.", "Responde con ese día."], "Wednesday"),
    ],
    [
        ("Leer todas las palabras con la misma atención para hallar un número.", "Se pierde tiempo y se mezcla skimming con scanning.", "Recorre el texto con la vista y detente solo en cifras."),
        ("Ignorar el título y la leyenda de la foto.", "Esos elementos entregan la idea de cada parte.", "Léelos primero, antes de los párrafos."),
    ],
    [
        ("Si buscas un dato exacto como una hora, usas: a) scanning b) skimming", "a", "Scanning es buscar un dato específico."),
        ("Una leyenda (caption) es: a) un texto breve junto a una imagen b) un párrafo largo de un cuento", "a", "Explica lo que muestra la imagen."),
        ("«Skimming» sirve para: a) captar la idea general b) calcular un precio", "a", "Se lee rápido para saber de qué trata el texto."),
    ],
    [
        (f"Lee: «{ART2}» {G_ART2} ¿Qué estrategia usas para saber de qué trata el texto? a) Skimming b) Scanning", "a", "Con el título, el subtítulo y la foto basta para la idea general."),
        (f"Lee: «{ART2}» {G_ART2} ¿Cuál es la idea general? a) There is a new centre where neighbours can recycle b) A school has a new library", "a", "El título y el párrafo 1 hablan de un nuevo centro de reciclaje."),
        (f"Lee: «{ART2}» {G_ART2} ¿Qué dice la leyenda de la foto? a) Volunteers sort paper and plastic b) Children make compost", "a", "Esa frase está en el caption."),
    ],
    [
        (f"Lee: «{ART2}» {G_ART2} Haz scanning. ¿A qué hora abre el centro? a) 9:00 b) 17:00", "a", "El párrafo 2 dice from 9:00 to 17:00; 9:00 es la apertura."),
        (f"Lee: «{ART2}» {G_ART2} Haz scanning. ¿Qué días está cerrado? a) Sunday and Monday b) Tuesday and Saturday", "a", "El párrafo 2 dice It is closed on Sunday and Monday."),
        (f"Lee: «{MUS2}» {G_MUS2} Haz scanning. ¿Cuánto cuesta la entrada de un estudiante? a) $2.000 b) $4.000", "a", "El texto indica students $2.000; $4.000 es para adultos."),
    ],
    [
        (f"Lee: «{MUS2}» {G_MUS2} Haz scanning. ¿A qué horas hay visitas guiadas? a) 11:00 and 15:00 b) 10:00 and 18:00", "a", "Las horas de apertura y cierre son otras; las visitas están indicadas con at."),
        (f"Un compañero quiere saber si el centro de reciclaje cobra entrada. Usó skimming y respondió «no sé». ¿Qué debería usar para hallar la respuesta en «{ART2}»? {G_ART2} a) Scanning, buscando la palabra entry b) Skimming otra vez", "a", "Es un dato específico, que se encuentra con scanning."),
    ],
    [
        (f"Lee: «{ART2}» {G_ART2} Pregunta: ¿Pueden entrar solos los niños de diez años? Haz scanning. a) No, children under twelve must come with an adult b) Yes, entry is free", "a", "Diez es menor que doce, así que necesitan ir con una persona adulta."),
        (f"Lee: «{MUS2}» {G_MUS2} Pau tiene cinco años, su hermana tiene catorce y es estudiante. ¿Cuánto paga cada una por la entrada? a) Pau $0 and her sister $2.000 b) Pau $2.000 and her sister $4.000", "a", "Menores de seis años no pagan y la estudiante paga la tarifa de students."),
    ],
    [("En el aviso de una feria del libro de tu comuna aparece: «Book Fair. Subtitle: Meet a local writer. Paragraph 1: The fair is on Friday and Saturday, 11:00 to 19:00. Paragraph 2: Entry is free.» (fair = feria; writer = escritor) Tu amiga pregunta si la feria cobra entrada. ¿Qué estrategia usas y qué respondes? a) Scanning: entry is free b) Skimming: the fair is expensive", "a", "Buscas un dato exacto y el texto dice que la entrada es gratis.")],
    [
        ("¿Qué estrategia sirve para buscar un número exacto?", "Scanning", "Scanning es lectura focalizada."),
        ("¿Qué elemento del texto está junto a una foto y explica lo que muestra?", "Caption", "La leyenda o caption describe la imagen."),
        ("Para saber de qué trata un artículo, ¿qué lees primero: el título o el último párrafo?", "El título", "El título y el subtítulo anuncian la idea general."),
    ],
    task("Lee este aviso: «Title: Swimming Pool Winter Schedule. Subtitle: Open for families. Paragraph 1: The pool is open on Tuesday, Thursday and Saturday. Paragraph 2: On Tuesday and Thursday it opens at 16:00 and closes at 20:00. On Saturday it opens at 10:00 and closes at 14:00. Paragraph 3: Children under ten must come with an adult.» (pool = piscina; opens = abre; closes = cierra; schedule = horario) En tu hoja anota: la idea general (skimming) y dos datos exactos que encuentres con scanning.", "Idea general: horario de invierno de la piscina. Datos: el sábado abre a las 10:00; los menores de diez años van con una persona adulta.", ["resume la idea general en una oración", "encuentra dos datos exactos del aviso", "indica en qué párrafo está cada dato"], ["tres líneas con idea y datos en la hoja"], ["copiar el texto completo en lugar de resumir", "dar un dato que no está en el aviso"], "Pide que cuente cuánto tiempo tardó en hallar cada dato y qué estrategia usó."),
    "Copia la tabla de vocabulario y dibuja una flecha de cada estrategia (skimming, scanning) a un ejemplo de cuándo la usas.",
    "Elige un aviso de tu casa o tu colegio con letras y números, escribe la idea general y un dato exacto en una hoja.",
)

# ============================================================ clase 3: visualizar y organizadores gráficos
V3 = "The market is full of colours. Red tomatoes and green peppers are on the left table. Yellow lemons are in a blue box next to the door. An old man with a straw hat sells honey in the centre."
G_V3 = "(market = feria; peppers = pimentones; lemons = limones; straw hat = sombrero de paja; sells = vende; honey = miel; centre = centro)"
S3 = "A bean seed goes into wet soil. After a few days, the seed opens and small roots grow down. Then a green stem grows up. Finally two small leaves appear."
G_S3 = "(bean seed = semilla de poroto; soil = tierra; roots = raíces; stem = tallo; leaves = hojas)"
CAT3 = "Cats: have fur, sleep a lot, say meow, climb trees. Dogs: have fur, like walks, say woof, learn tricks."
G_CAT3 = "(fur = pelaje; walks = paseos; woof = guau; tricks = trucos)"

lesson(
    OA, 3,
    "Los textos y los organizadores descritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a visualizar lo que leo, es decir, a imaginar una imagen mental, y a usar organizadores gráficos como la cadena de secuencia, el diagrama de Venn y el mapa de idea principal. Sirve para entender y recordar mejor un texto en inglés.",
    ["Conozco la lectura rápida y la focalizada.", "Sé la diferencia entre idea principal y detalle."],
    [
        "Visualizar (to visualize) es crear una imagen en tu mente con lo que dice el texto. Lee una descripción y pregúntate: ¿qué veo? ¿dónde está cada cosa? ¿de qué color es? Las palabras de lugar (left, next to, in the centre) y los colores son pistas. Si puedes dibujar lo que leíste, lo entendiste. Si algo no calza con tu dibujo, vuelve a leer esa parte.",
        "Un organizador gráfico (graphic organizer) ordena la información después de leer. La cadena de secuencia (sequence chain) pone cajas con flechas y sirve para pasos: first, then, finally. El diagrama de Venn (Venn diagram) tiene dos círculos que se cruzan: lo común va al centro y lo diferente a cada lado. El mapa de idea principal (main idea web) pone la idea al centro y los detalles alrededor.",
        "Para elegir el organizador mira el tipo de texto. Si hay pasos en orden, usa secuencia. Si se comparan dos cosas, usa Venn. Si hay una idea con muchos datos, usa el mapa de idea principal. Escribe palabras clave y no oraciones completas: el organizador es un resumen visual, no una copia del texto.",
    ],
    [("visualize", "visualizar: imaginar una imagen"), ("graphic organizer", "organizador gráfico"), ("sequence chain", "cadena de secuencia"), ("Venn diagram", "diagrama de Venn: dos círculos"), ("main idea web", "mapa de la idea principal"), ("next to", "junto a"), ("left", "izquierda")],
    [
        ("Visualizar una descripción", "Texto: «On the desk there is a red lamp on the right. A green book is next to the lamp. A blue pen is in front of the book.» (desk = escritorio; lamp = lámpara; pen = lápiz pasta; in front of = delante de) ¿Dónde está el libro?",
         ["Primero ubica la lámpara: a la derecha del escritorio.", "El libro verde está junto a la lámpara.", "Imagina el libro cerca de la lámpara roja."], "El libro verde está junto a la lámpara roja."),
        ("Elegir un organizador", "Texto: «Tom's bike is red and has two wheels. Ana's scooter is blue and has two wheels. Both are fast, but the bike is bigger.» (wheels = ruedas; scooter = monopatín; bigger = más grande) ¿Qué organizador sirve para comparar los dos?",
         ["El texto compara dos objetos.", "Lo común: dos ruedas y rápidos.", "Para comparar dos cosas se usa el diagrama de Venn."], "El diagrama de Venn."),
    ],
    [
        ("Copiar todo el texto en las cajas de la cadena.", "El organizador debe resumir y no repetir.", "Escribe solo palabras clave en cada caja."),
        ("Usar un diagrama de Venn para pasos en orden.", "Los pasos necesitan una secuencia, no una comparación.", "Para pasos, usa la cadena de secuencia."),
    ],
    [
        ("«Visualize» significa: a) imaginar una imagen mental del texto b) cantar el texto", "a", "Es crear imágenes en la mente."),
        ("Para pasos en orden usas: a) una cadena de secuencia b) un diagrama de Venn", "a", "La cadena muestra el orden con flechas."),
        ("«Next to» significa: a) junto a b) lejos de", "a", "Indica que algo está muy cerca."),
    ],
    [
        (f"Lee: «{V3}» {G_V3} ¿Dónde están los limones? a) In a blue box next to the door b) On the left table", "a", "El texto dice Yellow lemons are in a blue box next to the door."),
        (f"Lee: «{V3}» {G_V3} ¿Qué lleva puesto el hombre mayor? a) A straw hat b) A blue box", "a", "Lleva un sombrero de paja y vende miel."),
        (f"Lee: «{V3}» {G_V3} ¿De qué color son los pimentones? a) Green b) Red", "a", "Los pimentones son verdes y los tomates son rojos."),
    ],
    [
        (f"Lee: «{S3}» {G_S3} Cadena de secuencia: [Seed in wet soil] → [Roots grow down] → [?] → [Two leaves appear]. ¿Qué va en la caja que falta? a) A green stem grows up b) The seed dries", "a", "Después de las raíces crece el tallo, antes de las hojas."),
        (f"Lee: «{CAT3}» {G_CAT3} En un diagrama de Venn de gatos y perros, ¿qué va en el centro? a) Have fur b) Say meow", "a", "Los dos tienen pelaje, así que es común."),
        (f"Lee: «{CAT3}» {G_CAT3} ¿En qué círculo va «learn tricks»? a) Dogs b) Cats", "a", "El texto dice que los perros aprenden trucos."),
    ],
    [
        (f"Lee: «{V3}» {G_V3} Un compañero dibuja los tomates en la mesa de la derecha. ¿Qué parte del texto muestra que se equivocó? a) The text says red tomatoes are on the left table b) The man sells honey", "a", "La palabra left indica la mesa de la izquierda."),
        ("Texto: «Ema has a notebook, a pencil case and a bottle of water in her bag. She also carries a blue folder.» (carries = lleva; folder = carpeta) Quieres hacer un mapa de idea principal. ¿Qué escribes en el centro? a) Things in Ema's bag b) Ema's blue folder", "a", "La idea principal reúne todos los objetos; la carpeta es un detalle."),
    ],
    [
        ("Texto: «To make lemonade, first squeeze three lemons. Then add water and sugar. Finally add ice.» (squeeze = exprimir; lemonade = limonada; add = agregar; ice = hielo) Una cadena de secuencia tiene tres cajas. ¿Qué escribes en la última? a) Add ice b) Squeeze lemons", "a", "Finally indica el último paso: agregar hielo."),
        (f"Lee: «{S3}» {G_S3} Un compañero dice que un diagrama de Venn sirve para este texto. ¿Qué organizador es mejor? a) Sequence chain b) Venn diagram", "a", "El texto cuenta etapas en orden, no compara dos cosas."),
    ],
    [("Tu profesora entrega este texto sobre dos cuadernos: «Notebook A has 80 pages and a red cover. Notebook B has 100 pages and a red cover. Both are good for Maths.» (pages = páginas; cover = tapa) Para hacer un diagrama de Venn, ¿qué dato va en el centro? a) Red cover b) 100 pages", "a", "Los dos tienen tapa roja; las páginas son distintas.")],
    [
        ("¿Qué organizador usarías para una receta con pasos?", "Cadena de secuencia", "La cadena muestra el orden de los pasos."),
        ("¿Cuántos círculos tiene un diagrama de Venn de dos temas?", "Dos", "Cada círculo corresponde a un tema y el cruce a lo común."),
        ("¿Qué palabras escribes en un organizador: oraciones completas o palabras clave?", "Palabras clave", "El organizador es un resumen."),
    ],
    task("Lee este texto: «Ines and her brother both like fruit. Ines likes apples and bananas. Her brother likes bananas and oranges. They both eat fruit every day after school.» (fruit = fruta; apples = manzanas; oranges = naranjas; every day = todos los días) En tu hoja dibuja un diagrama de Venn con dos círculos, escribe qué fruta va en cada lado y cuál en el centro.", "Ines: apples. Centro: bananas. Hermano: oranges.", ["dibuja dos círculos que se cruzan", "pone la fruta común en el centro", "usa solo palabras clave"], ["diagrama de Venn dibujado en la hoja"], ["poner el dato común en un lado", "escribir oraciones completas"], "Pide que cambie el organizador a una lista de dos columnas y explique en qué se parece y en qué no."),
    "Copia el vocabulario y dibuja un ejemplo pequeño de una cadena de secuencia con tres cajas.",
    "Lee una receta de tu casa y dibuja su cadena de secuencia con tres palabras clave.",
)

# ============================================================ clase 4: después de leer (confirmar, releer, recontar con apoyo)
L4 = "Bruno's Key. Paragraph 1: On Tuesday, Bruno comes home and cannot find his house key. Paragraph 2: He looks in his bag, in his pockets and under the bench. Paragraph 3: Then he remembers that he left it in the school library. Paragraph 4: He runs back to school and the librarian gives him the key."
G_L4 = "(key = llave; bag = mochila; pockets = bolsillos; bench = banca; remembers = recuerda; left = dejó; librarian = bibliotecaria)"
NA4 = "Notas de A: Maya wants a pet. Her mother says no. Maya writes a list of reasons."
NB4 = "Notas de B: Maya's mother reads the list. They agree to adopt a rabbit. Maya promises to clean the cage."
G_NAB4 = "(pet = mascota; reasons = razones; adopt = adoptar; rabbit = conejo; promises = promete; cage = jaula)"

lesson(
    OA, 4,
    "Los textos, las notas y los modelos de frase escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a confirmar mis predicciones, a releer para aclarar dudas y a recontar un texto con apoyo de palabras clave. Sirve para comprobar si entendí y para contárselo a otra persona en inglés.",
    ["Sé predecir antes de leer y usar un organizador.", "Conozco first, then y finally."],
    [
        "Después de leer (after reading) vuelves a tu predicción y la comparas con el texto: confirm (confirmar) si coincide, change (cambiar) si no. Por ejemplo: «I predicted the key was at home, but the text says it was at school». También puedes releer (reread): volver a un párrafo concreto cuando algo no quedó claro. Usa el número de párrafo para saber dónde mirar.",
        "Recontar (retell) es contar con tus palabras lo que leíste, en orden y sin copiar. Ayuda usar apoyos: palabras clave anotadas y comienzos de oración como «At the beginning…, Then…, In the end…». Un buen recuento tiene los hechos principales, respeta el orden y no agrega datos que el texto no tenga.",
        "Cuando dos personas tienen partes distintas de una misma historia, puedes completar la información juntando sus notas. Lee la nota A, lee la nota B, confirma qué pasó primero y cuenta la historia completa. Si hay un dato que no aparece en ninguna nota, no lo inventes: di «I do not know», es decir, «No lo sé».",
    ],
    [("confirm", "confirmar"), ("change", "cambiar"), ("reread", "releer"), ("retell", "recontar"), ("keywords", "palabras clave"), ("I do not know", "no lo sé"), ("sentence starter", "comienzo de oración")],
    [
        ("Confirmar o cambiar una predicción", "Predicción antes de leer «Bruno's Key»: «Bruno loses his key at home.» Texto: «Bruno cannot find his key. He remembers that he left it in the school library.» (left = dejó) ¿Confirmas o cambias la predicción?",
         ["La predicción decía que estaba en casa.", "El texto dice que estaba en la biblioteca del colegio.", "La predicción no coincide: hay que cambiarla."], "Se cambia: la llave estaba en la biblioteca del colegio."),
        ("Recontar con apoyo", "Palabras clave: Pia, rain, umbrella, neighbour. Comienzos: At the beginning… In the end… Cuenta en una oración el inicio si Pia espera la micro bajo la lluvia sin paraguas.",
         ["Usa la palabra clave rain y el nombre Pia.", "Agrega que no tiene paraguas.", "Escribe: At the beginning, Pia waits for the bus in the rain without an umbrella."], "At the beginning, Pia waits for the bus in the rain without an umbrella."),
    ],
    [
        ("Copiar el texto entero cuando recuentas.", "Recontar es resumir con tus palabras.", "Usa palabras clave y un comienzo de oración para cada parte."),
        ("Inventar un dato que no está en el texto para completar el recuento.", "Cambia lo que cuenta el autor.", "Si no lo sabes, di I do not know o relee el párrafo."),
    ],
    [
        ("«Reread» significa: a) releer b) escribir", "a", "Re- indica repetir la lectura."),
        ("Si tu predicción coincide con el texto, la: a) confirmas b) borras sin motivo", "a", "Confirmar es comprobar que acertaste."),
        ("«Retell» significa: a) recontar con tus palabras b) copiar sin cambios", "a", "Recontar es explicar lo leído en tus palabras."),
    ],
    [
        (f"Lee: «{L4}» {G_L4} ¿En qué párrafo busca Bruno la llave en su mochila? a) Paragraph 2 b) Paragraph 4", "a", "El párrafo 2 enumera la mochila, los bolsillos y la banca."),
        (f"Lee: «{L4}» {G_L4} Un compañero predijo que la llave estaba bajo la banca. ¿Qué haces con esa predicción? a) La cambias, porque estaba en la biblioteca b) La confirmas, porque la busca bajo la banca", "a", "Busca bajo la banca, pero no la encuentra allí."),
        (f"Lee: «{L4}» {G_L4} ¿Cómo termina la historia? a) The librarian gives him the key b) Bruno buys a new key", "a", "Esa es la última oración del texto."),
    ],
    [
        (f"Lee: «{L4}» {G_L4} Recuento: «At the beginning, Bruno cannot find his key. In the end, ___.» ¿Qué completa mejor? a) the librarian gives him the key b) he sleeps", "a", "Resume el final correcto del texto."),
        (f"Lee: «{L4}» {G_L4} Quieres confirmar dónde estaba la llave. ¿Qué párrafo relees? a) Paragraph 3 b) Paragraph 1", "a", "El párrafo 3 dice que la dejó en la biblioteca."),
        (f"{NA4} {NB4} {G_NAB4} ¿Cuál es el problema de la historia? a) Maya wants a pet but her mother says no b) Maya wants a bike", "a", "La nota A cuenta que Maya quiere una mascota y su mamá dice que no."),
    ],
    [
        (f"{NA4} {NB4} {G_NAB4} ¿Qué mascota adoptan? a) A rabbit b) A dog", "a", "La nota B dice que acuerdan adoptar un conejo."),
        (f"{NA4} {NB4} {G_NAB4} Pregunta: ¿Cómo se llama el conejo? a) I do not know, the notes do not say it b) Pelusa", "a", "Ninguna nota da el nombre y no debes inventarlo."),
    ],
    [
        (f"{NA4} {NB4} {G_NAB4} ¿Cuál es el recuento más completo y fiel? a) Maya wants a pet. She writes reasons, her mother reads them, and they adopt a rabbit. b) Maya buys a rabbit.", "a", "Incluye problema, acción y final sin agregar datos."),
        ("Ana dice que su predicción de «Bruno's Key» era acertada porque predijo «Bruno loses something». Texto: «Bruno loses his key.» Si predijo eso antes de leer el texto, ¿la confirmas? a) Sí, porque coincide con lo que dice b) No, porque faltan detalles", "a", "La predicción general coincide con el texto aunque no tenga todos los detalles."),
    ],
    [("Tu curso arma un periódico mural con recuentos de cuentos. Una compañera escribe: «At the beginning, Bruno loses his key. Then he looks in his bag. In the end, the librarian gives him the key.» ¿Respeta el orden de los hechos? Responde sí o no.", "Sí", "Los tres hechos están en el mismo orden que el texto.")],
    [
        ("Si algo no queda claro, ¿qué haces con el párrafo?", "Lo relees", "Releer aclara dudas."),
        ("¿Qué escribes si el texto no da un dato: invento el dato o digo I do not know?", "Digo I do not know", "No se inventa información."),
        ("Un recuento, ¿debe copiar el texto o usar tus palabras?", "Usar tus palabras", "Recontar es explicar con tus palabras."),
    ],
    task("Lee estas dos notas. Nota A: «Teo is nervous before the school play. He forgets one line.» Nota B: «His friend whispers the line. The audience claps at the end.» (school play = obra de teatro del colegio; line = parte del diálogo; whispers = susurra; audience = público; claps = aplaude) En tu hoja escribe un recuento de tres oraciones con At the beginning…, Then… e In the end…, y marca si cambiaste o confirmaste esta predicción: «Teo will stop the play».", "At the beginning, Teo is nervous before the school play. Then he forgets one line. In the end, his friend whispers the line and the audience claps. Predicción: se cambia, porque la obra continúa.", ["tres oraciones en orden con los comienzos", "usa solo datos de las notas", "decide si confirma o cambia la predicción y da la razón"], ["recuento de tres oraciones en la hoja"], ["agregar datos que no están en las notas", "olvidar el orden"], "Pide que lea su recuento en voz alta a otra persona y que esa persona diga si entendió la historia."),
    "Copia los tres comienzos de oración y escribe un ejemplo con cada uno.",
    "Recuenta en tres oraciones en inglés un cuento breve que conozcas con At the beginning, Then e In the end.",
)

# ============================================================ clase 5: preguntar para confirmar y lectura independiente
BUS5 = "Title: The Library Bus. Subtitle: Books travel to small villages. Paragraph 1: Every Wednesday, a blue bus full of books visits three small villages in the south. Paragraph 2: The bus stops for two hours in each village. Children and adults can borrow up to three books. Paragraph 3: A librarian named Mr. Cruz reads a story aloud at 11:00. Paragraph 4: Next month, the bus will carry more books about animals."
G_BUS5 = "(bus full of = bus lleno de; villages = pueblos; stops = se detiene; borrow = pedir prestado; up to = hasta; aloud = en voz alta; carry = llevar)"
Q5 = "Title: A Drop of Honey. Paragraph 1: Bees visit many flowers every day. Paragraph 2: With each visit, a bee collects nectar, a sweet liquid. Paragraph 3: Back in the hive, other bees turn the nectar into honey. Paragraph 4: It takes many bees and many flowers to make a small jar of honey."
G_Q5 = "(bees = abejas; flowers = flores; collects = recoge; nectar = néctar; liquid = líquido; hive = colmena; jar = frasco)"

lesson(
    OA, 5,
    "Los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a hacer preguntas para confirmar información de un texto y usaré todas las estrategias, antes, durante y después de leer, en una lectura independiente. Sirve para leer por mi cuenta en inglés y comprobar que entendí.",
    ["Conozco las estrategias de antes, durante y después de la lectura.", "Sé usar Who, What, Where, When y Why."],
    [
        "Para confirmar información, hazte preguntas sobre el texto. Las preguntas con palabras interrogativas piden un dato: Who? (¿quién?), What? (¿qué?), Where? (¿dónde?), When? (¿cuándo?), Why? (¿por qué?) y How many? (¿cuántos?). Las de sí o no empiezan con Does, Is o Are: «Does the bus visit three villages?». Cada pregunta debe poder responderse con el texto.",
        "Después de formular la pregunta, busca la respuesta con scanning y márcala o apunta el número de párrafo. Para estar seguro, relee esa parte y comprueba que tu respuesta coincide palabra por palabra con los datos. Si el texto no da la respuesta, escribe «The text does not say». Preguntar también sirve para pedir ayuda a otra persona: «Can you repeat paragraph 2, please?».",
        "En una lectura independiente usa la secuencia completa. Antes: fija el propósito y predice con el título. Durante: haz skimming para la idea general, scanning para los datos y visualiza. Después: confirma o cambia tu predicción, completa un organizador, recuenta con palabras clave y haz dos preguntas para confirmar. Practica con un texto breve y resuelve cada paso por tu cuenta.",
    ],
    [("Who / What / Where", "quién / qué / dónde"), ("When / Why", "cuándo / por qué"), ("How many", "cuántos"), ("Does / Is / Are", "preguntas de sí o no"), ("The text does not say", "el texto no lo dice"), ("Can you repeat…?", "¿puedes repetir…?")],
    [
        ("Formular una pregunta que el texto responde", "Texto: «Every Friday, Doña Rosa sells tomatoes at the market. She arrives at 7:00.» (sells = vende; arrives = llega) Elige la pregunta para confirmar el horario: a) What time does Doña Rosa arrive? b) Where does she live?",
         ["Busca la pregunta que se responde con el texto.", "El texto dice cuándo llega: 7:00.", "What time does she arrive? confirma esa hora."], "What time does Doña Rosa arrive? (a las 7:00)"),
        ("Reconocer cuando el texto no responde", "Texto: «Joaquin plays chess every Sunday at the library.» (plays = juega; chess = ajedrez) Pregunta: Why does Joaquin like chess? ¿Qué respondes?",
         ["Busca una razón en el texto: no la hay.", "No debes inventarla.", "Respuesta: The text does not say."], "The text does not say."),
    ],
    [
        ("Hacer una pregunta cuya respuesta no está en el texto y responderla igual.", "Se inventa información.", "Si no está, responde The text does not say."),
        ("Elegir where cuando la pregunta es sobre la hora.", "Se confunden las palabras interrogativas.", "Hora o momento: When o What time."),
    ],
    [
        ("«Where» pregunta por: a) un lugar b) una hora", "a", "Where? significa ¿dónde?"),
        ("«How many» pregunta por: a) una cantidad b) una razón", "a", "How many? significa ¿cuántos?"),
        ("Si el texto no da la respuesta, escribes: a) The text does not say b) Yes", "a", "Así no inventas información."),
    ],
    [
        (f"Lee: «{BUS5}» {G_BUS5} Pregunta para confirmar: ¿Cuándo visita el bus los pueblos? a) Every Wednesday b) Every Friday", "a", "El párrafo 1 indica Every Wednesday."),
        (f"Lee: «{BUS5}» {G_BUS5} How many books can a person borrow? a) Up to three b) Up to two", "a", "El párrafo 2 dice up to three books."),
        (f"Lee: «{BUS5}» {G_BUS5} Who reads a story aloud? a) Mr. Cruz b) A child", "a", "El párrafo 3 nombra al bibliotecario Mr. Cruz."),
    ],
    [
        (f"Lee: «{BUS5}» {G_BUS5} Pregunta: How many hours does the bus stop in each village? a) Two hours b) Three hours", "a", "El párrafo 2 dice for two hours in each village."),
        (f"Lee: «{BUS5}» {G_BUS5} Pregunta: What is the name of the bus driver? a) The text does not say b) Mr. Cruz", "a", "Mr. Cruz es el bibliotecario; el texto no nombra a quien conduce."),
        (f"Lee: «{BUS5}» {G_BUS5} ¿Qué pregunta confirma lo que pasará el próximo mes? a) What will the bus carry next month? b) Who is the librarian?", "a", "Pregunta por el párrafo 4 que habla del mes siguiente."),
    ],
    [
        (f"Lee: «{Q5}» {G_Q5} Antes de leer, predijiste que «A Drop of Honey» trataba de cocinar. ¿Qué haces con esa predicción? a) La cambias: trata de cómo las abejas hacen miel b) La confirmas: trata de cocinar", "a", "El párrafo 1 y el 2 hablan de abejas y néctar."),
        (f"Lee: «{Q5}» {G_Q5} Pregunta: Where do other bees turn the nectar into honey? a) In the hive b) In the flowers", "a", "El párrafo 3 dice Back in the hive."),
    ],
    [
        (f"Lee: «{Q5}» {G_Q5} Cadena de secuencia: [Bees visit flowers] → [?] → [Other bees turn nectar into honey]. ¿Qué falta en el medio? a) A bee collects nectar b) A bee drinks water", "a", "Antes de hacer miel, la abeja recoge el néctar de la flor."),
        (f"Lee: «{Q5}» {G_Q5} ¿Cuál es la mejor idea general? a) Making honey needs many bees and flowers b) Honey is always expensive", "a", "El último párrafo resume el esfuerzo de muchas abejas y flores."),
    ],
    [("Un aviso de tu colegio dice: «Title: Science Fair. Subtitle: Friday at 15:00 in the gym. Paragraph 1: Students show projects about water and energy. Paragraph 2: Parents can visit from 16:00.» (gym = gimnasio; projects = proyectos; parents = apoderados) Tu compañero pregunta: Where is the science fair? ¿Qué respondes y qué estrategia usas? a) In the gym, using scanning b) In the library, using skimming", "a", "Es un dato exacto; está en el subtítulo.")],
    [
        ("¿Qué pregunta usas para un lugar: Where o When?", "Where", "Where pregunta por un lugar."),
        ("¿Qué haces con tu predicción después de leer?", "La confirmas o la cambias", "La comparas con lo que dice el texto."),
        ("Si no entiendes, ¿qué frase puedes decir en inglés para pedir que repitan? a) Can you repeat, please? b) I have a pen.", "a", "Pide ayuda de forma cortés."),
    ],
    task("Lee este texto: «Title: Winter Garden. Subtitle: Plants for cold days. Paragraph 1: In June, Sara and her grandfather plant lettuce and spinach in boxes. Paragraph 2: They water the plants every two days. Paragraph 3: In August they eat a green salad.» (lettuce = lechuga; spinach = espinaca; boxes = cajones; salad = ensalada; water = regar) En tu hoja escribe: tu propósito y tu predicción antes de leer; la idea general; dos preguntas para confirmar con su respuesta; y si cambiaste o confirmaste tu predicción.", "Propósito: aprender cómo se cultiva en invierno. Predicción: I think it is about growing plants because the title says garden. Idea general: Sara y su abuelo cultivan verduras en invierno. Preguntas: When do they plant? In June. What do they eat in August? A salad.", ["fija propósito y predicción antes de leer", "resume la idea general", "escribe dos preguntas con sus respuestas del texto"], ["cuatro apartados breves en la hoja"], ["hacer preguntas que el texto no responde", "olvidar confirmar o cambiar la predicción"], "Pide que intercambie sus preguntas con otra persona y que la otra persona las responda sin mirar las respuestas."),
    "Copia las palabras interrogativas y escribe un ejemplo de pregunta con cada una.",
    "Haz dos preguntas con Who y When sobre el último texto que leíste en cualquier asignatura y responde con el texto.",
)
