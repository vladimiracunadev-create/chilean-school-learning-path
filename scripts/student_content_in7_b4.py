"""Cuaderno del estudiante, 7.º básico Inglés (oficial): IN07 OA 14, textos breves funcionales y creativos.

Los modelos en inglés son originales y breves, con glosario en español dentro del enunciado. El proceso de escritura
(organizar, redactar, revisar, editar y publicar) se practica con textos ya escritos en cada ejercicio.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "IN07 OA 14"


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


# ============================================================ clase 1: convenciones de cada género
EM1 = "Subject: Art club on Tuesday. Hi Lucia, our art club meets on Tuesday at 4:00 in Room 5. Please bring a pencil and a notebook. See you there! Best, Pablo"
GEM1 = "(subject = asunto; meets = se reúne; bring = traer)"
BR1 = "Visit the Green Park! Open every day. Things to do: • Ride a bike • Feed the ducks • Have a picnic. Come and enjoy!"
GBR1 = "(feed = dar de comer; ducks = patos; picnic = merienda al aire libre)"
RH1 = "Little snail, little snail, / Slowly moving with your tail. / Little snail, little snail, / Leave a shiny silver trail."
GRH1 = "(snail = caracol; tail = cola; shiny = brillante; trail = huella)"
DE1 = "My grandmother's kitchen is small but warm. It has a yellow table, a blue window and a smell of fresh bread."
GDE1 = "(grandmother = abuela; warm = cálida; smell = olor; fresh = recién hecho)"

lesson(
    OA, 1,
    "Los modelos de textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a reconocer cómo es un correo electrónico, un folleto, una rima, una descripción y un cuento breve. Sirve para escribir cada texto con su forma y su tono propios.",
    ["Sé elegir propósito y audiencia.", "Sé escribir oraciones completas en inglés."],
    [
        "Cada tipo de texto (genre) tiene sus convenciones, es decir, rasgos que se esperan. Un correo electrónico (email) lleva un asunto (subject), un saludo (Hi Lucia,), un mensaje breve y una despedida con tu nombre (Best, Pablo). Un folleto (brochure) tiene un título llamativo, frases cortas y listas con viñetas para invitar o informar.",
        "Una rima (rhyme) es un texto corto en versos que terminan con sonidos parecidos y tienen ritmo. Una descripción (description) dice cómo es algo con adjetivos y detalles de los sentidos: yellow, small, warm. Un cuento breve (short story) tiene personajes, lugar, un problema y un final, y casi siempre se cuenta en pasado: «Mia opened the door and saw a cat.»",
        "Para escribir bien, mira un modelo (model) y anota qué partes tiene y para quién está escrito. Un correo a un amigo es informal; uno a un director es formal. Un folleto usa lenguaje que atrae; una descripción usa adjetivos; un cuento usa verbos de acción. Elegir mal las convenciones hace que el texto confunda.",
    ],
    [("email", "correo electrónico"), ("subject", "asunto"), ("brochure", "folleto"), ("rhyme", "rima"), ("description", "descripción"), ("short story", "cuento breve"), ("model", "modelo")],
    [
        ("Reconocer un correo electrónico", "Texto: «Subject: Football on Friday. Hi Tom, we play at 5:00 in the yard. Bye, Diego.» (yard = patio) ¿Qué rasgos muestran que es un correo?",
         ["Tiene la palabra Subject al comienzo.", "Empieza con un saludo: Hi Tom.", "Termina con una despedida y el nombre de quien escribe."], "Tiene asunto (Subject), saludo (Hi Tom) y despedida con nombre (Bye, Diego)."),
        ("Reconocer una descripción", "Texto: «The old lighthouse is tall and white. It has a red door and a round window.» (lighthouse = faro; round = redonda) ¿Es un cuento o una descripción?",
         ["No hay problema ni acciones que cambien la situación.", "Hay adjetivos: tall, white, red, round.", "Dice cómo es algo: es una descripción."], "Es una descripción."),
    ],
    [
        ("Escribir un correo sin asunto ni despedida.", "Se confunde con un mensaje sin forma.", "Agrega Subject, saludo, mensaje breve y despedida con tu nombre."),
        ("Usar el mismo tono en todos los textos.", "No se piensa en la audiencia ni en el género.", "Mira el modelo: un folleto atrae; una descripción detalla; un cuento narra."),
    ],
    [
        ("¿Qué parte de un correo resume el tema? a) El asunto (subject) b) La despedida", "a", "El asunto dice de qué trata el correo."),
        ("¿Qué rasgo tiene una rima? a) Versos que terminan con sonidos parecidos b) Párrafos largos sin ritmo", "a", "La rima repite sonidos al final."),
        ("¿Qué usa una descripción? a) Adjetivos y detalles b) Solo verbos de acción", "a", "Un adjetivo dice cómo es algo."),
    ],
    [
        (f"Lee: «{EM1}» {GEM1} ¿Dónde se reúne el club? Opciones: Room 5, the yard.", "Room 5", "El correo dice in Room 5."),
        (f"Lee: «{BR1}» {GBR1} ¿Qué rasgo del folleto aparece? a) Una lista con viñetas b) Una despedida con nombre", "a", "Things to do: va con tres viñetas."),
        (f"Lee: «{RH1}» {GRH1} ¿Qué dos palabras riman en los versos 1 y 2? a) snail - tail b) little - slowly", "a", "Snail y tail terminan con el mismo sonido."),
    ],
    [
        (f"Lee: «{DE1}» {GDE1} ¿Qué género es? a) Descripción b) Correo", "a", "Describe cómo es un lugar con adjetivos."),
        ("Texto: «Last night, Ana heard a noise. She opened the door and found a small cat. She gave it milk.» (heard = oyó; found = encontró) ¿Qué género es? a) Cuento breve b) Folleto", "a", "Cuenta sucesos en pasado con un personaje."),
        (f"Lee: «{BR1}» {GBR1} ¿Cuántas actividades se listan en el folleto?", "3", "Hay tres viñetas: bike, ducks y picnic."),
    ],
    [
        ("Un compañero escribe un correo al director y comienza con «Yo, what's up?» ¿Qué error de convención comete? a) Saludo informal para una audiencia formal b) Falta un título", "a", "Con un director conviene un saludo formal como Dear Mr. Silva."),
        (f"Lee: «{EM1}» {GEM1} Falta el asunto. ¿Cuál sirve? a) Subject: Art club on Tuesday b) Subject: Tuesday Tuesday Tuesday", "a", "Resume claramente de qué trata el correo."),
    ],
    [
        ("Lee: «Come to the school fair! Music, games and food. Saturday at 11:00.» (fair = feria) ¿Qué género es? a) Folleto o afiche b) Cuento breve", "a", "Invita y usa frases cortas con datos."),
        ("Lee: «Roses are red, / Violets are blue, / The sky is high, / I love you.» Escribe la palabra del poema que rima con blue. Opciones: you, red.", "you", "Blue y you terminan con el mismo sonido."),
    ],
    [("Tu profesora te pide escribir un texto para invitar a las familias a una exposición de arte. ¿Qué género y rasgo conviene? a) Folleto con título y datos b) Rima sin información de día ni hora", "a", "Un folleto da título, día y hora, y atrae a las familias.")],
    [
        ("¿Qué partes tiene un correo electrónico?", "Asunto, saludo, mensaje y despedida", "Son sus convenciones."),
        ("¿Qué tiempo verbal usa casi siempre un cuento breve? a) Pasado b) Futuro", "a", "Narra sucesos que ya ocurrieron."),
        ("¿Qué rasgo ayuda a distinguir un folleto? a) Título llamativo y viñetas b) Versos con rima", "a", "Los folletos atraen con frases cortas."),
    ],
    task("Lee estos cuatro textos: 1) «Subject: Homework. Hi Maya, please send me the math exercises. Thanks, Leo.» 2) «Fun at the Beach! Swim • Build sand castles • Play volleyball.» 3) «The moon is round, the stars are bright, / We sing a song, we say goodnight.» 4) «The old oak tree has big green leaves and strong branches.» (castles = castillos; branches = ramas) En tu hoja escribe el género de cada uno y un rasgo que lo muestra.", "1) Correo: Subject y saludo. 2) Folleto: viñetas y frases cortas. 3) Rima: bright - goodnight. 4) Descripción: adjetivos.", ["identifica el género de los cuatro textos", "nombra un rasgo concreto de cada uno", "no confunde rima con descripción"], ["hoja con cuatro respuestas"], ["identificar solo por el tema", "no justificar"], "Pregunta qué cambiaría en el texto 1 si fuera para un director."),
    "Copia la tabla de vocabulario y escribe un rasgo de cada género.",
    "Escribe un correo de cuatro líneas a un amigo con asunto, saludo, mensaje y despedida.",
)

# ============================================================ clase 2: adaptar un modelo sin copiar
MOD2 = "Subject: Birthday party. Hi Sam, I am having a party on Saturday at 3:00 at my house. We will play games and eat cake. Can you come? Bye, Ana"
GMOD2 = "(birthday = cumpleaños; will play = jugaremos; cake = pastel)"

lesson(
    OA, 2,
    "El modelo y los ejemplos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a usar un modelo como guía y a adaptarlo con mis propias ideas, sin copiarlo. Sirve para escribir textos propios en inglés con una estructura que funciona.",
    ["Sé reconocer los rasgos de un correo, un folleto y una rima.", "Sé escribir oraciones con sujeto y verbo."],
    [
        "Un modelo (model) es un texto que muestra cómo se escribe un género. Adaptar un modelo significa conservar su estructura y cambiar el contenido. En un correo de invitación se conservan el asunto, el saludo, los datos del evento, la pregunta y la despedida. Se cambian la persona, el evento, el día, la hora y el lugar.",
        "Copiar es distinto: es escribir las mismas oraciones del modelo sin cambiar nada. Eso no es tu texto. Para adaptar, haz una tabla con dos columnas: «Keep» (lo que conservo) y «Change» (lo que cambio). Cambia al menos las personas, el evento, la fecha y los detalles, y escribe con tus propias palabras. Si usas una frase útil del modelo, como «Can you come?», está bien, pero cambia el resto.",
        "Un criterio de evaluación (criterion) es una regla para saber si el texto está bien. Por ejemplo: 1) mantiene la estructura del correo, 2) cambia al menos tres datos, 3) no copia oraciones completas, 4) tiene un cierre. Revisa tu texto con cada criterio antes de entregarlo.",
    ],
    [("model", "modelo"), ("adapt", "adaptar"), ("copy", "copiar"), ("keep / change", "conservar / cambiar"), ("criterion", "criterio"), ("structure", "estructura"), ("invitation", "invitación")],
    [
        ("Separar lo que se conserva y lo que se cambia", "Modelo: «Subject: Football match. Hi Leo, we play on Friday at 5:00 in the yard. Can you come? Bye, Tom.» (match = partido; yard = patio) Vas a invitar a una película. ¿Qué conservas y qué cambias?",
         ["Conservas: asunto, saludo, datos, pregunta y despedida.", "Cambias: el evento, los nombres, el día, la hora y el lugar.", "Escribes con tus propias palabras."], "Conservo la estructura del correo; cambio el evento, los nombres y los datos."),
        ("Distinguir copiar de adaptar", "Modelo: «We will play games and eat cake.» Versión 1: «We will play games and eat cake.» Versión 2: «We will watch a movie and eat popcorn.» (popcorn = cabritas) ¿Cuál adapta el modelo?",
         ["La versión 1 es idéntica.", "La versión 2 conserva la estructura y cambia las acciones.", "Adaptar es cambiar el contenido."], "La versión 2."),
    ],
    [
        ("Copiar el modelo completo y cambiar solo el nombre.", "Se cree que cambiar un dato basta.", "Cambia varios datos y escribe con tus palabras."),
        ("Cambiar tanto el modelo que desaparece la estructura.", "No se recuerda qué partes debían conservarse.", "Mantén asunto, saludo, datos, pregunta y despedida."),
    ],
    [
        ("¿Qué significa adaptar un modelo?", "Conservar la estructura y cambiar el contenido", "Así el texto es propio."),
        (f"Lee el modelo: «{MOD2}» {GMOD2} ¿Qué se conserva en un nuevo correo de invitación? a) El asunto, el saludo y la despedida b) El nombre del cumpleañero", "a", "Son parte de la estructura del género."),
        ("Copiar un texto es: a) escribir las mismas oraciones sin cambiar nada b) cambiar el evento y los datos", "a", "Eso no es un texto propio."),
    ],
    [
        (f"Lee el modelo: «{MOD2}» {GMOD2} ¿Qué dato debes cambiar si invitas a una función de teatro? a) El evento (party) b) El saludo (Hi)", "a", "El evento es el contenido propio."),
        (f"Lee el modelo: «{MOD2}» {GMOD2} Versión adaptada: «Subject: School play. Hi Rita, our school play is on Thursday at 6:00 in the hall. Can you come? Bye, Joaquín». Compara con el modelo. ¿Qué parte conservó igual? a) Can you come? b) La hora", "a", "La pregunta final se mantiene; la hora cambió de 3:00 a 6:00."),
        ("Un criterio dice: «No copia oraciones completas». ¿Cuál texto cumple? a) We will watch a movie at my house b) We will play games and eat cake.", "a", "La primera usa una idea nueva; la segunda repite el modelo."),
    ],
    [
        ("Completa con tu invitación a una caminata: «Subject: Walk in the park. Hi Rita, we ___ in the park on Sunday. Can you come? Bye, Joaquín.» Opciones: will walk, walks.", "will walk", "La actividad nueva requiere un verbo que calce."),
        ("Para adaptar el modelo del cumpleaños a una invitación a jugar básquetbol (basketball), ¿qué frase cambias? a) We will play games and eat cake. b) Can you come?", "a", "Cambia la actividad; la pregunta final se conserva."),
        ("Un compañero entrega el mismo texto del modelo con la única diferencia de que cambia «Sam» por «Pia». ¿Cumple el criterio «cambia al menos tres datos»? Responde sí o no.", "No", "Cambió un solo dato."),
    ],
    [
        ("Un criterio dice: «mantiene la estructura del correo». Esta versión: «Birthday party Saturday Ana house cake.» ¿Lo cumple? Responde sí o no.", "No", "No tiene saludo, mensaje en oraciones ni despedida."),
        ("Pablo dice que si usa «Can you come?» del modelo está copiando. ¿Tiene razón? Responde sí o no.", "No", "Una frase corta y útil del género puede usarse, siempre que el resto sea propio."),
    ],
    [
        ("Modelo breve: «Hi Ana, I like swimming because it is fun.» Adapta con otro deporte. Elige la mejor versión: a) Hi Ana, I like tennis because it is exciting b) Hi Ana, I like swimming because it is fun.", "a", "La primera cambia el deporte y la razón; la segunda copia."),
        ("Completa la tabla del modelo del cumpleaños. Keep = ___. Change = event, time, place. Elige lo que va en Keep. a) subject, greeting, closing b) cake, Saturday", "a", "La estructura se conserva; los datos cambian."),
    ],
    [("Tu profesor te da el modelo «Subject: Reading club. Hi Mara, we meet on Monday in the library. Can you join us? Best, Ian» (join = unirse) y quieres invitar a un club de ajedrez. ¿Qué cambio es correcto? a) Reading club por Chess club y library por Room 4 b) No cambiar nada", "a", "Se cambian el evento y el lugar, y se conserva la estructura.")],
    [
        ("En Inglés (oficial): ¿Qué es un criterio de evaluación?", "Una regla para saber si el texto está bien", "Sirve para revisar."),
        ("En una tabla Keep/Change, ¿dónde va el nombre del evento?", "En Change", "Es contenido que cambia."),
        ("Un texto adaptado: a) conserva la estructura y cambia datos b) cambia solo una letra", "a", "Así es un texto propio."),
    ],
    task("Usa este modelo: «Subject: Pizza night. Hi Dani, we will make pizza on Friday at 7:00 at my house. Can you come? Best, Luz.» (make = preparar) En tu hoja adáptalo para invitar a una tarde de pintura (painting afternoon): escribe una tabla Keep/Change y tu correo de cuatro oraciones con asunto, saludo, datos, pregunta y despedida. Revisa con tres criterios: mantiene la estructura, cambia al menos tres datos, no copia oraciones completas.", "Keep: asunto, saludo, pregunta, despedida. Change: evento, día, hora, lugar. Subject: Painting afternoon. Hi Ema, we will paint on Sunday at 4:00 in the yard. Can you come? Best, Rafa.", ["conserva la estructura", "cambia al menos tres datos", "no copia oraciones completas"], ["tabla Keep/Change y correo en la hoja"], ["copiar casi todo", "perder la estructura"], "Pide que compare su correo con el modelo y marque lo que cambió."),
    "Copia el modelo de la explicación y subraya con dos colores lo que conservarías y lo que cambiarías.",
    "Adapta el modelo de la clase 1 («Art club on Tuesday») para invitar a un club de lectura.",
)

# ============================================================ clase 3: desarrollar un texto coherente
lesson(
    OA, 3,
    "Los párrafos y listas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir un texto breve en el que todas las ideas se relacionan con una idea principal. Sirve para que quien lea entienda sin confundirse.",
    ["Sé adaptar un modelo.", "Sé distinguir una idea principal de un detalle."],
    [
        "Un texto es coherente (coherent) cuando todas sus oraciones hablan de la misma idea principal y siguen un orden lógico. Un párrafo (paragraph) tiene una oración tema (topic sentence) que presenta la idea, dos o tres oraciones de apoyo (supporting sentences) con detalles y, si hace falta, una oración final (closing sentence).",
        "Por ejemplo: «My cat is very special. It sleeps on my bed. It plays with a ball of wool. It always waits for me at the door.» La primera oración presenta la idea y las otras dan detalles. Una oración como «I like pizza» no calza ahí: rompe la coherencia. Al revisar, tacha las oraciones que no apoyan la idea principal.",
        "El orden también importa. En una descripción puedes ir de lo general a lo particular. En un relato, en orden de tiempo. Para una explicación, de lo más importante a lo menos. Si tu texto tiene varias ideas grandes, usa un párrafo para cada una. Antes de escribir, anota la idea principal en una línea.",
    ],
    [("coherent", "coherente: las ideas se relacionan"), ("topic sentence", "oración tema"), ("supporting sentence", "oración de apoyo"), ("paragraph", "párrafo"), ("main idea", "idea principal"), ("order", "orden"), ("irrelevant", "que no corresponde al tema")],
    [
        ("Encontrar la oración que no calza", "Párrafo: «My school has a big library. It has books about animals and space. The cafeteria sells sandwiches. Students can read there at recess.» (cafeteria = casino; space = espacio) ¿Qué oración rompe la coherencia?",
         ["La idea principal es la biblioteca.", "La oración de la cafetería habla de otra cosa.", "Esa oración no apoya la idea."], "The cafeteria sells sandwiches."),
        ("Elegir la oración tema", "Oraciones de apoyo: «We have a garden. We have a sports field. We have a music room.» ¿Cuál es la mejor oración tema? a) Our school has many fun places. b) I like Mondays.",
         ["Las tres oraciones hablan de lugares del colegio.", "La oración tema debe incluir esa idea.", "La primera presenta bien la idea."], "Our school has many fun places."),
    ],
    [
        ("Mezclar dos ideas en un solo párrafo.", "No se decide qué idea es la principal.", "Usa un párrafo para cada idea."),
        ("Escribir una lista de oraciones sin oración tema.", "Se salta la presentación.", "Empieza con una oración que diga de qué trata el párrafo."),
    ],
    [
        ("¿Qué es la oración tema?", "La que presenta la idea principal del párrafo", "Va al comienzo."),
        ("Las oraciones de apoyo: a) dan detalles de la idea principal b) cambian el tema", "a", "Apoyan lo que dice la oración tema."),
        ("Un texto es coherente cuando: a) todas las oraciones se relacionan con la misma idea b) tiene muchas palabras", "a", "La coherencia depende de la relación de las ideas."),
    ],
    [
        ("Párrafo: «My brother is very sporty. He plays football on Mondays. He swims on Wednesdays. My mom works at a bank.» (sporty = deportista; bank = banco) ¿Qué oración sobra? Opciones: My mom works at a bank, He swims on Wednesdays.", "My mom works at a bank", "No habla de los deportes del hermano."),
        ("Elige la mejor oración tema para: «She makes bread. She sells cakes. She opens at seven.» a) My aunt has a bakery b) The sea is blue.", "a", "Presenta el tema de las tres oraciones."),
        ("Ordena el relato con letras: x) Then she saw a small bird. y) Yesterday Ema went to the park. z) She gave it some water. Escribe el orden lógico.", "y, x, z", "Va al parque, ve el pájaro y luego le da agua."),
    ],
    [
        ("Idea principal: «Water is important.» ¿Qué oración de apoyo calza? a) We drink water every day b) My shoes are new.", "a", "Da un detalle del tema."),
        ("Idea principal: «My town is quiet.» ¿Qué oración la apoya mejor? a) There are few cars and many trees b) The school bus is yellow.", "a", "Pocos autos y muchos árboles dan sensación de tranquilidad."),
        ("Cuenta las oraciones de apoyo: «Pedro is a good friend. He shares his lunch. He helps with homework. He always listens.» ¿Cuántas hay?", "3", "Hay tres oraciones después de la oración tema."),
    ],
    [
        ("Un compañero escribe: «Winter is cold. I go to school. Penguins eat fish.» ¿Es coherente el párrafo? Responde sí o no.", "No", "Las oraciones hablan de tres temas distintos."),
        ("Tienes dos ideas: tu mascota y tu colegio. ¿Cuántos párrafos conviene escribir? a) 2 b) 1", "a", "Un párrafo por cada idea principal."),
    ],
    [
        ("Mini texto: «The beach is my favourite place. The sand is warm. The waves are loud. I do homework every night.» ¿Qué oración tachas? Escribe cuál.", "I do homework every night", "No habla de la playa."),
        ("Quieres describir tu pieza. ¿Cuál orden va de lo general a lo particular? a) My room is small. It has a bed and a lamp b) The lamp is yellow. My room is small. The bed.", "a", "Primero la idea general y luego los detalles."),
    ],
    [("Tu profesora te pide un párrafo de tres oraciones sobre tu deporte favorito. ¿Cuál es la mejor oración tema? a) I love swimming b) The weather is cloudy.", "a", "Presenta el tema que se desarrollará.")],
    [
        ("¿Cuántas ideas principales conviene tener en un párrafo?", "Una", "Así el párrafo es coherente."),
        ("¿Qué haces con una oración que no apoya la idea principal?", "La quitas", "Rompe la coherencia."),
        ("¿Cuál oración es una oración tema? a) My pet is lovely b) And dogs.", "a", "Presenta una idea completa."),
    ],
    task("Lee estas ideas desordenadas: «She drinks water.» «My sister is very healthy.» «She sleeps eight hours.» «She walks to school.» «My uncle likes tea.» En tu hoja escribe un párrafo coherente con la oración tema primero, las tres oraciones de apoyo y una oración final. Tacha la oración que sobra.", "My sister is very healthy. She drinks water. She sleeps eight hours. She walks to school. That is why she feels great. (Tachada: My uncle likes tea.)", ["la oración tema va primero", "usa solo ideas relacionadas", "tacha la oración que sobra"], ["párrafo ordenado en la hoja"], ["incluir la oración sobre el tío", "no tener oración tema"], "Pregunta por qué la oración del tío no calza."),
    "Copia el párrafo de ejemplo de la explicación y subraya la oración tema.",
    "Escribe un párrafo de cuatro oraciones sobre tu mejor amigo o amiga sin dar nombres.",
)

# ============================================================ clase 4: conectores y palabras de referencia
lesson(
    OA, 4,
    "Las oraciones y párrafos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a unir ideas con conectores y a usar palabras como he, she, it y they para no repetir. Sirve para que mi texto fluya y no suene entrecortado.",
    ["Sé armar un párrafo coherente.", "Conozco palabras como and, but y because."],
    [
        "Los conectores (connectors) unen ideas. And suma («I like tea and cake»), but contrasta («I like tea but I don't like coffee»), because da una razón («I stay home because it is raining»), so da un resultado («It is raining, so I stay home») y then, next y finally ordenan acciones en el tiempo. También sirve also (además).",
        "Las palabras de referencia (reference words) reemplazan algo ya mencionado para no repetirlo. He se refiere a un hombre o niño; she, a una mujer o niña; it, a una cosa o animal; they, a varias personas o cosas; this, a algo cercano. Ejemplo: «My cat is gray. It sleeps all day.» Aquí it reemplaza a my cat.",
        "Un error común es usar una referencia sin que se entienda a qué alude. «Ana and Mia went to the park. She was happy.» no deja claro quién es she. Mejor: «Ana and Mia went to the park. Ana was happy.» Después de escribir, pregunta por cada he, she, it o they: ¿a quién o a qué se refiere? Si la respuesta no es clara, repite el nombre.",
    ],
    [("connector", "conector"), ("and / but", "y / pero"), ("because / so", "porque / así que"), ("then / finally", "luego / finalmente"), ("also", "además"), ("reference word", "palabra de referencia"), ("they", "ellos, ellas")],
    [
        ("Elegir el conector", "Completa: «It was cold, ___ we wore coats.» Opciones: so, but. (wore = usamos; coats = abrigos)",
         ["La segunda parte es un resultado del frío.", "So marca un resultado.", "But marcaría una oposición."], "so"),
        ("Saber a qué se refiere una palabra", "Texto: «Tom and Luis play chess. They play every Friday.» ¿A quién se refiere they?",
         ["They es plural.", "En la oración anterior están Tom y Luis.", "They los reemplaza."], "A Tom y Luis."),
    ],
    [
        ("Usar but cuando la idea es una razón.", "Se cree que cualquier conector sirve.", "Si das un motivo, usa because; si contrastas, usa but."),
        ("Poner she cuando hay dos mujeres y no se sabe a cuál.", "No se piensa en la claridad.", "Repite el nombre cuando la referencia no es clara."),
    ],
    [
        ("«Because» sirve para: a) dar una razón b) sumar una acción", "a", "Because introduce una causa."),
        ("¿Qué palabra usas para una niña? a) she b) he", "a", "She se refiere a una niña o mujer."),
        ("Completa: «I like soccer ___ tennis.» Opciones: and, because.", "and", "And une dos cosas que te gustan."),
    ],
    [
        ("Completa: «I want to go out, ___ it is raining.» Opciones: but, so.", "but", "La lluvia contrasta con el deseo de salir."),
        ("Completa: «My bike is broken, ___ I walk to school.» Opciones: so, because.", "so", "Caminar es el resultado de que la bicicleta esté rota."),
        ("«The dog is hungry. ___ eats a lot.» Opciones: It, They.", "It", "Se refiere a un solo animal."),
    ],
    [
        ("Texto: «Pedro has two cats. They are black.» ¿A qué se refiere they? a) A los gatos b) A Pedro", "a", "They reemplaza two cats."),
        ("Une las oraciones con because: «I am happy. I have a new bike.» a) I am happy because I have a new bike b) I am happy so I have a new bike.", "a", "Because da la razón de la alegría."),
        ("Ordena con conectores: x) Finally, we ate. y) First, we cooked. z) Then, we set the table. Escribe el orden. (set the table = poner la mesa)", "y, z, x", "First, then y finally ordenan los pasos."),
    ],
    [
        ("«Ana and Mia went to the park. She was happy.» ¿Está claro a quién se refiere she? Responde sí o no.", "No", "Podría ser Ana o Mia."),
        ("Elige la mejor opción: «I like winter ___ I can drink hot chocolate.» a) because b) but", "a", "Because da una razón que explica por qué le gusta el invierno."),
    ],
    [
        ("Une las ideas con un conector: «The soup is hot. I wait.» Elige la mejor opción: a) The soup is hot, so I wait b) The soup is hot, but I wait.", "a", "Esperar es el resultado de que esté caliente."),
        ("Reduce repeticiones: «Luis is tall. Luis plays basketball. Luis likes it.» ¿Cuál queda mejor? a) Luis is tall. He plays basketball and likes it b) Luis is tall. Luis plays basketball. Luis likes it.", "a", "Usa he y it para no repetir el nombre, sin agregar ideas nuevas."),
    ],
    [("Una amiga lee tu texto: «My sister and I like painting. We paint on Saturdays because it is relaxing.» (relaxing = relajante) Te pregunta por we. ¿A quiénes se refiere? a) A tu hermana y a ti b) A tus amigos", "a", "We reemplaza my sister and I.")],
    [
        ("¿Qué indica «so»?", "Un resultado", "Es la consecuencia."),
        ("¿Qué indica «but»?", "Un contraste", "Une ideas que se oponen."),
        ("Completa: «Sara has a dog. ___ is brown.» Opciones: It, She.", "It", "Se refiere al perro."),
    ],
    task("Mejora este texto con conectores y palabras de referencia: «Nico likes rain. Nico plays inside. Nico reads a book. Nico is tired. Nico goes to bed.» (rain = lluvia; inside = adentro; tired = cansado) En tu hoja reescríbelo en tres oraciones usando because, so, then y al menos tres veces he. Revisa que se entienda a quién se refiere cada he.", "Nico likes rain because it is relaxing. He plays inside and then he reads a book. He is tired, so he goes to bed.", ["usa los cuatro conectores", "usa he sin confundir", "el texto sigue siendo coherente"], ["texto reescrito en la hoja"], ["usar un conector en vez de otro", "repetir el nombre en cada oración"], "Pregunta cómo cambia el sentido si pones but en vez de so."),
    "Copia la tabla del vocabulario y agrega un ejemplo corto de cada conector.",
    "Escribe un párrafo de cuatro oraciones sobre un fin de semana con and, but, because y so.",
)

# ============================================================ clase 5: editar para un lector real
lesson(
    OA, 5,
    "Los textos con errores escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a editar mi texto (mayúsculas, puntuación, ortografía y verbos) y a usar un procesador de texto y un diccionario en línea. Sirve para publicar un texto limpio que una persona real pueda leer sin tropezar.",
    ["Sé revisar el contenido de un texto.", "Sé que las oraciones empiezan con mayúscula."],
    [
        "Después de revisar el contenido, edita (to edit): corrige las formas del texto. Revisa cuatro cosas: mayúsculas (la palabra I, los nombres, los días y meses: Monday, May), puntuación (punto al final, coma en listas, signo de pregunta), ortografía (friend, because, school) y concordancia: he plays, she likes, they play.",
        "Hay herramientas útiles. El procesador de texto (word processor) subraya palabras con posibles errores, pero no ve todo: si escribes there en vez de their, no lo marca porque ambas existen. Un diccionario en línea (online dictionary) muestra el significado, la ortografía y ejemplos de uso. Úsalos para comprobar, no para copiar sin pensar.",
        "Publicar (to publish) es entregar una versión limpia a un lector real: tu curso, tu profesora o un amigo. Antes pregúntate: ¿entenderá esta persona mi texto? Lee en voz alta, pasa la lista de edición y entrega la versión final con un título. El proceso completo es: organizar ideas, redactar, revisar, editar y publicar.",
    ],
    [("edit", "editar: corregir la forma"), ("capital letter", "mayúscula"), ("punctuation", "puntuación"), ("spelling", "ortografía"), ("word processor", "procesador de texto"), ("online dictionary", "diccionario en línea"), ("publish", "publicar: entregar la versión final")],
    [
        ("Corregir mayúsculas y puntuación", "Oración: «on monday i play football with my friends» Corrígela.",
         ["Falta la mayúscula inicial y la de Monday.", "I siempre va en mayúscula.", "Falta el punto final."], "On Monday I play football with my friends."),
        ("Detectar un error que el corrector no ve", "Oración: «They put there bags on the table.» ¿Qué palabra está mal aunque exista en el diccionario?",
         ["There indica un lugar; their indica que algo les pertenece.", "Aquí se habla de las mochilas de ellos.", "Corresponde their."], "there; debe ser their: They put their bags on the table."),
    ],
    [
        ("Confiar solo en el corrector automático.", "No detecta palabras que existen pero están mal usadas.", "Relee con atención y consulta un diccionario."),
        ("Entregar sin leer en voz alta.", "Se cree que el borrador ya está listo.", "Lee en voz alta para notar errores y partes confusas."),
    ],
    [
        ("En Inglés (oficial): ¿Qué significa «edit»?", "Corregir la forma del texto", "Se hace después de revisar el contenido."),
        ("¿Cuál se escribe con mayúscula? a) Monday b) tomorrow", "a", "Los días de la semana empiezan con mayúscula."),
        ("¿Para qué sirve un diccionario en línea? a) Para ver significado y ortografía b) Para escribir el texto por ti", "a", "Sirve para comprobar, no para copiar."),
    ],
    [
        ("Corrige: «she play tennis on saturday.» a) She plays tennis on Saturday b) She play tennis on Saturday.", "a", "Con she el verbo lleva -s y Saturday va con mayúscula."),
        ("Elige la oración bien escrita. a) I have two brothers and one sister. b) i have two brother and one sister", "a", "Tiene mayúscula, plural y punto."),
        ("¿Qué falta en «Where do you live»? Opciones: signo de pregunta, coma.", "signo de pregunta", "Una pregunta termina con ?"),
    ],
    [
        ("Corrige la ortografía: «My frend plays soccer becase it is fun.» ¿Cuántas palabras están mal escritas?", "2", "Faltan friend y because."),
        ("Elige la versión correcta: a) We eat apples, bananas, and oranges. b) We eat apples bananas and oranges", "a", "En una lista se usan comas."),
        ("Corrige: «They plays football.» a) They play football b) They plays football.", "a", "Con they el verbo no lleva -s."),
    ],
    [
        ("Un compañero dice que si el procesador de texto no subraya «there» en «They love there dog.» ya está bien. ¿Tiene razón? Responde sí o no.", "No", "Puede estar usada de forma incorrecta aunque exista."),
        ("Entre editar y revisar el contenido, ¿cuál va primero? a) Revisar el contenido b) Editar la ortografía", "a", "No tiene sentido pulir la ortografía de una oración que luego se elimina."),
    ],
    [
        ("Edita: «my teacher is mrs. rojas she is kind» (kind = amable) ¿Cuántas palabras necesitan mayúscula inicial?", "4", "My, Mrs., Rojas y She."),
        ("Antes de publicar un afiche para tu curso, ¿qué haces? a) Leerlo en voz alta y pasar la lista de edición b) Cambiar el tema", "a", "Es el paso previo a publicar."),
    ],
    [("Escribes una nota para tus compañeros: «tomorow is friday we play footbal at 4» ¿Cuál es la edición correcta? a) Tomorrow is Friday. We play football at 4 b) Tomorow is friday we play footbal at 4.", "a", "Corrige ortografía, mayúsculas y puntuación.")],
    [
        ("En Inglés (oficial): ¿Cuáles son los cinco pasos del proceso de escritura?", "Organizar, redactar, revisar, editar y publicar", "Es el proceso completo."),
        ("¿Qué letra siempre va en mayúscula en inglés cuando hablas de ti?", "I", "El pronombre I siempre es mayúscula."),
        ("Un corrector automático: a) no detecta todos los errores b) detecta todos", "a", "Hay errores con palabras existentes que no marca."),
    ],
    task("Edita este texto: «my name is ana i live in a small town my town have a park and a library on saturday i go to the library with my friend we reads books». (small = pequeña; park = parque) En tu hoja: a) reescríbelo con mayúsculas, puntos y verbos corregidos, b) lee en voz alta y marca dos cambios que hiciste, c) escribe un título.", "My name is Ana. I live in a small town. My town has a park and a library. On Saturday I go to the library with my friend. We read books. (Título: My Town)", ["usa mayúsculas y puntos", "corrige have a has y reads a read", "agrega un título"], ["texto editado con cambios marcados"], ["dejar I sin mayúscula", "no corregir los verbos"], "Pide que explique por qué cambió has y read."),
    "Copia la lista de edición de la explicación y úsala con un texto tuyo de cinco líneas.",
    "Escribe una nota de cuatro oraciones con tres errores a propósito y pide a otra persona que los encuentre.",
)
