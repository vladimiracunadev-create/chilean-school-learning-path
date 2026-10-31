"""Cuaderno del estudiante, 7.º básico Inglés (oficial): IN07 OA 12, estrategias de comprensión lectora.

Los textos en inglés son originales, breves y llevan glosario en español dentro del enunciado. Cada estrategia se enseña
en la clase antes de usarla. Sin audio externo: todo lo que hay que leer está escrito en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "IN07 OA 12"


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


# ============================================================ clase 1: propósito de lectura
POOL = "Swimming Pool. Open: Monday to Friday 7:00-20:00. Saturday 9:00-14:00. Closed on Sundays."
OCEAN = "Ocean Day: Beach clean-up on Saturday at 9:30. Bring gloves and a bag. Meet at the main gate."
GOCEAN = "(clean-up = limpieza; bring = traer; gloves = guantes; gate = portón)"

lesson(
    OA, 1,
    "Los avisos, textos y listas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a fijar un propósito antes de leer y a usar lo que ya sé del tema. Sirve para decidir cómo leer un texto en inglés y qué buscar.",
    ["Sé leer avisos y textos breves con ayuda de un glosario.", "Conozco palabras como open, closed, Monday y Saturday."],
    [
        "Antes de leer, conviene preguntarse: ¿para qué voy a leer este texto? Eso es el propósito de lectura (reading purpose). Puede ser disfrutar una historia (to enjoy), buscar un dato (to find a fact), aprender sobre un tema (to learn) o seguir instrucciones (to follow instructions). El propósito decide qué buscas y qué tan rápido lees.",
        "También ayuda usar el conocimiento previo (prior knowledge): lo que ya sabes del tema. Si el título es «Why Do Cats Purr?», ya sabes que los gatos son mascotas y hacen un sonido suave cuando están tranquilos. Eso te prepara para entender las palabras nuevas. La lectura tiene tres momentos: prelectura (antes), lectura (durante) y poslectura (después).",
        "Un buen lector cambia su manera de leer según el propósito. Para un horario o un aviso no hace falta leer todo palabra por palabra: busca solo el dato que necesitas, como un día o una hora. Para un cuento, en cambio, se lee con calma y se imagina la historia. Escribir el propósito en una línea antes de leer ayuda a no perderse.",
    ],
    [("reading purpose", "propósito de lectura"), ("prior knowledge", "conocimiento previo"), ("before / during / after reading", "antes / durante / después de leer"), ("to find a fact", "buscar un dato"), ("to enjoy", "disfrutar"), ("to follow instructions", "seguir instrucciones"), ("notice", "aviso")],
    [
        ("Elegir el propósito", "Tienes este volante: «Chess Club. Tuesdays at 4:30 in Room 6.» (club de ajedrez; martes) Quieres saber cuándo es. ¿Qué propósito tienes y qué buscas?",
         ["Quieres un dato: el día y la hora.", "El propósito es buscar un dato (to find a fact).", "Miras solo «Tuesdays at 4:30»."], "Propósito: buscar un dato. Respuesta: los martes a las 4:30."),
        ("Activar el conocimiento previo", "Vas a leer un texto titulado «How to Plant Beans». (plant = plantar; beans = porotos) ¿Qué sabes ya del tema que te ayude antes de leer?",
         ["Piensa en lo que sabes de plantas.", "Las plantas necesitan tierra, agua y sol.", "Esa idea te prepara para entender las instrucciones."], "Que las plantas necesitan tierra, agua y sol; así entiendo mejor las instrucciones."),
    ],
    [
        ("Leer todo palabra por palabra, siempre.", "Se cree que solo así se entiende un texto.", "Si buscas un dato, mira solo lo que responde a tu propósito."),
        ("Empezar a leer sin saber para qué.", "No se piensa en el propósito antes de leer.", "Escribe una línea: «Leo para…»."),
    ],
    [
        ("¿Qué es el propósito de lectura? a) Para qué voy a leer el texto b) Cuántas páginas tiene", "a", "El propósito responde para qué leo, no cuánto mide el texto."),
        ("Quieres saber a qué hora cierra una tienda. Tu propósito es: a) buscar un dato b) disfrutar un poema", "a", "Un horario se lee para encontrar un dato concreto."),
        ("Entre prelectura, lectura y poslectura, ¿qué momento va primero?", "La prelectura", "Prelectura significa antes de leer."),
    ],
    [
        ("Sam leerá una receta de muffins: «Mix flour and milk. Pour it in a pan.» (flour = harina; pour = verter) ¿Cuál es su propósito? a) Seguir instrucciones b) Disfrutar un cuento", "a", "Una receta se lee para hacer los pasos en orden."),
        ("Antes de leer «Why Do Cats Purr?», ¿qué conocimiento previo ayuda? a) Sé que los gatos son mascotas y hacen un sonido suave b) Sé andar en bicicleta", "a", "Lo que sabes de gatos se relaciona con el título."),
        ("Mirar el título para pensar de qué trata el texto ocurre en la: a) prelectura b) poslectura", "a", "Se hace antes de leer."),
    ],
    [
        (f"Lee el aviso: «{POOL}» (pool = piscina; closed = cerrado) Quieres nadar un domingo. ¿Se puede? Responde sí o no.", "No", "El aviso dice que está cerrada los domingos."),
        ("Vas a leer un cómic antes de dormir y no tienes tarea. Tu propósito es: a) disfrutar b) buscar un dato", "a", "Lees por gusto, sin necesidad de encontrar nada."),
        ("Quieres saber si una sopa lleva zanahoria. Tienes la lista: «onion, carrot, potato, salt». (onion = cebolla; carrot = zanahoria) ¿Lleva zanahoria? Responde sí o no.", "Sí", "La lista incluye carrot."),
    ],
    [
        ("Kai y Lola leen el aviso: «Science Fair: Friday, Room 3, 15:00.» (feria de ciencias) Kai quiere saber dónde. Lola quiere saber la hora. ¿Qué dato mira Lola?", "15:00", "La hora es el dato que ella busca."),
        ("Alguien dice: «Todos los textos se leen igual, palabra por palabra.» ¿Qué idea lo contradice mejor? a) Con otro propósito se lee distinto: para un dato se mira rápido b) Los textos siempre son largos", "a", "El propósito cambia la manera de leer."),
    ],
    [
        (f"Lee el aviso: «{OCEAN}» {GOCEAN} Tu propósito es saber qué llevar. ¿Qué dos cosas debes llevar?", "Gloves and a bag", "Bring gloves and a bag indica lo que se lleva."),
        (f"Lee el aviso: «{OCEAN}» {GOCEAN} Ahora tu propósito es saber dónde juntarse. ¿Qué frase lees? a) Meet at the main gate b) Bring gloves and a bag.", "a", "Meet at... indica el punto de encuentro."),
    ],
    [("Un amigo te escribe: «Movie night Friday 19:00 in the school hall.» (hall = salón) Quieres saber si llegas a las 18:30, antes de que empiece. ¿Qué dato necesitas? a) 19:00 b) school hall", "a", "La hora de inicio es el dato que responde si llegas antes.")],
    [
        ("¿Cuáles son los tres momentos de la lectura?", "Prelectura, lectura y poslectura", "Antes, durante y después de leer."),
        ("En Inglés (oficial): ¿Qué es el conocimiento previo?", "Lo que ya sé del tema", "Ayuda a entender un texto nuevo."),
        ("Para un horario de bus, ¿cómo conviene leer? a) Buscando el dato que necesito b) Palabra por palabra desde el inicio", "a", "El propósito es encontrar un dato."),
    ],
    task("Lee estos tres textos: 1) «Bakery. Bread at 7:00. Cakes at 10:00. Closed on Mondays.» 2) «A short poem about the moon.» 3) «To make tea: boil water, put the tea bag in a cup, add water.» (bakery = panadería; boil = hervir) En tu hoja escribe, para cada uno, tu propósito de lectura (to enjoy, to find a fact o to follow instructions) y qué harías antes de leer.", "1) Buscar un dato: hora del pan. 2) Disfrutar. 3) Seguir instrucciones. Antes de leer: pensar qué sé del tema.", ["elige un propósito distinto para cada texto", "justifica con una palabra del texto", "menciona una acción de prelectura"], ["tres líneas con propósito y acción de prelectura"], ["usar el mismo propósito para todo", "no explicar la elección"], "Pregunta qué parte del texto no necesitaría leer completa."),
    "Copia las cuatro frases de propósito de la tabla con su significado.",
    "Escribe un propósito de lectura y un conocimiento previo para un texto que se llama «Winter in the Mountains».",
)

# ============================================================ clase 2: explorar y predecir
BEE = "Title: Bees at Work. Subtitle: How bees make honey. Image caption: A bee on a yellow flower."
BEE_P = "Paragraph 1: Bees visit flowers and collect nectar. Paragraph 2: In the hive, they turn nectar into honey."
GBEE = "(bee = abeja; nectar = néctar; hive = colmena; honey = miel)"
CAMP = "Title: My First Day at Camp. Subtitle: A diary page. Image: a tent under tall pine trees."
GCAMP = "(camp = campamento; tent = carpa; pine trees = pinos)"

lesson(
    OA, 2,
    "Los títulos, subtítulos y textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a mirar el título, el subtítulo y las imágenes para predecir de qué trata un texto y a confirmar si acerté. Sirve para empezar a leer con una idea clara.",
    ["Sé fijar un propósito antes de leer.", "Sé que el título y las imágenes dan pistas."],
    [
        "Antes de leer todo, explora el texto. Mira los elementos organizacionales (organizational features): el título (title), el subtítulo (subtitle), las imágenes (images), los pies de foto (captions) y los números de párrafo. Estas partes dan pistas del tema sin leer cada palabra.",
        "Con esas pistas haz una predicción (prediction): una idea de lo que probablemente dice el texto. Se escribe como «I think the text is about…» (Creo que el texto trata de…). Una predicción no es una respuesta final: es una hipótesis. Después de leer, la confirmas (it was right), la cambias (I changed it) o la completas con datos nuevos.",
        "Para predecir bien, junta tres pistas: lo que dice el título, lo que muestra la imagen y lo que ya sabes del tema. Si dos pistas apuntan a lo mismo, tu predicción es más segura. Al terminar, compara tu idea con el texto: confirmar o corregir predicciones es una estrategia de poslectura.",
    ],
    [("title", "título"), ("subtitle", "subtítulo"), ("image / caption", "imagen / pie de foto"), ("predict", "predecir"), ("prediction", "predicción"), ("confirm", "confirmar"), ("paragraph", "párrafo")],
    [
        ("Predecir con título e imagen", "Elementos: «Title: A Night at the Lighthouse. Subtitle: Life by the sea. Image: a tall white tower and waves.» (lighthouse = faro; tower = torre; waves = olas) ¿Qué predices del texto?",
         ["El título habla de un faro de noche.", "El subtítulo habla de la vida junto al mar.", "La imagen muestra una torre y olas: apoya la idea."], "Predicción: el texto cuenta cómo es una noche en un faro junto al mar."),
        ("Confirmar o corregir", "Predicción: «The text is about a dog.» Después lees: «Max is a robot with four legs. He helps people cross the street.» (robot; legs = patas; cross = cruzar) ¿Se confirma la predicción?",
         ["Compara la predicción con lo leído.", "El texto habla de un robot que parece un perro, no de un perro.", "Se corrige la predicción."], "No se confirma: era un robot con cuatro patas, no un perro."),
    ],
    [
        ("Considerar la predicción como un hecho.", "Se cree que lo pensado antes siempre es correcto.", "Revísala al leer; cámbiala si el texto dice otra cosa."),
        ("Predecir sin usar el título ni la imagen.", "Se adivina sin pistas.", "Apóyate en al menos dos pistas visibles."),
    ],
    [
        (f"Lee los elementos: «{BEE}» {GBEE} ¿Cuál es el título? a) Bees at Work b) How bees make honey", "a", "Bees at Work está marcado como Title; la otra frase es el subtítulo."),
        (f"Lee los elementos: «{BEE}» {GBEE} ¿Qué dice el pie de foto? Opciones: A bee on a yellow flower, How bees make honey.", "A bee on a yellow flower", "El pie de foto describe la imagen."),
        ("Una predicción es: a) una idea de lo que probablemente dice el texto b) la respuesta final del texto", "a", "Es una hipótesis que luego se confirma."),
    ],
    [
        (f"Lee los elementos: «{BEE}» {GBEE} ¿Qué predicción es más segura? a) Habla de cómo las abejas hacen miel b) Habla de cómo los osos hacen miel", "a", "Título, subtítulo e imagen apuntan a las abejas y la miel."),
        (f"Lee: «{CAMP}» {GCAMP} ¿Qué tipo de texto parece? a) Una página de diario sobre un campamento b) Una receta", "a", "El subtítulo dice «A diary page»."),
        (f"Lee: «{CAMP}» {GCAMP} ¿Qué pista de la imagen apoya que el lugar es al aire libre? a) tent under tall pine trees b) A diary page", "a", "Una carpa bajo pinos indica un lugar al aire libre."),
    ],
    [
        (f"Predicción: «Bees collect honey from the hive and fly away.» Lee: «{BEE_P}» {GBEE} ¿Se confirma? Responde sí o no.", "No", "El texto dice que recolectan néctar y lo convierten en miel dentro de la colmena."),
        (f"Lee el texto: «{BEE_P}» {GBEE} ¿Qué párrafo explica dónde se hace la miel? Escribe el número.", "2", "El párrafo 2 menciona la colmena (hive)."),
        (f"Lee los elementos: «{CAMP}» {GCAMP} Completa la predicción: «I think the text is about ___.» Opciones: the first day at camp, a football match.", "the first day at camp", "El título y la imagen de la carpa bajo los pinos apuntan al campamento."),
    ],
    [
        ("Julia ve estos elementos: «Title: The Big Race. Image: runners at a finish line with a girl holding a medal.» (race = carrera; finish line = meta; medal = medalla) Predice: a) Una niña gana una carrera b) Una niña pierde su mochila. ¿Cuál se apoya mejor?", "a", "Medalla y meta apoyan que hay una ganadora."),
        ("Sofi predice que el texto «Snow in the Andes» (nieve en los Andes) trata de un día de mucho calor en verano. ¿Qué pista del título lo contradice? Opciones: Snow, Andes.", "Snow", "La nieve no combina con un día de mucho calor."),
    ],
    [
        ("Predicción de Ben para el título «The Lost Key»: «Habla de una llave perdida.» Lee: «Tina cannot find her key. She looks in her bag, under the sofa and in her coat.» (coat = abrigo) ¿Se confirma, se completa o se corrige? Responde con una de las tres opciones.", "Se confirma", "Tina no encuentra su llave y la busca: la predicción era correcta."),
        (f"Lee los elementos: «{BEE}» {GBEE} Un compañero dice que, como el pie de foto habla de una flor, el texto trata de flores. ¿Qué dato muestra que no es el tema principal? a) El título habla de abejas b) La flor es amarilla", "a", "El título indica el tema principal; la flor es solo un detalle de la imagen."),
    ],
    [("Tu profesor te muestra la portada de un libro con el título «Under the Sea», un subtítulo «Fish and Coral» y la imagen de un pez azul. (coral = coral) Quieres predecir el contenido. ¿Cuál es la predicción mejor apoyada? a) El libro habla de la vida bajo el mar b) El libro habla de las montañas", "a", "Título, subtítulo e imagen apuntan al mar.")],
    [
        ("¿Para qué sirve el subtítulo?", "Da más información sobre el tema", "Complementa al título."),
        ("En Inglés (oficial): ¿Qué haces con una predicción después de leer?", "La confirmas o la corriges", "Es una estrategia de poslectura."),
        ("¿Qué elemento es un pie de foto? a) Una frase corta bajo una imagen b) El nombre del autor", "a", "El caption explica la imagen."),
    ],
    task("Mira estos elementos: «Title: The Secret Garden of Grandma Rosa. Subtitle: A story of flowers and friends. Image: an old wall with a small green door.» (secret = secreto; wall = muro; door = puerta) En tu hoja escribe: a) qué predices que dice el texto, b) dos pistas que usaste, c) una pregunta que quisieras responder al leer.", "a) Es un cuento sobre un jardín escondido. b) Título y puerta verde. c) ¿Qué hay detrás de la puerta?", ["la predicción usa al menos dos pistas", "señala cuáles pistas usó", "la pregunta se relaciona con el tema"], ["hoja con predicción, pistas y pregunta"], ["predecir sin pistas", "no justificar"], "Pregunta qué parte de la predicción cambiaría si la imagen mostrara una cocina."),
    "Copia los siete términos del vocabulario con su significado en español.",
    "Busca la portada de un libro que tengas en casa y escribe en inglés una predicción de dos líneas usando su título.",
)

# ============================================================ clase 3: releer para una pregunta precisa
FAIR = "School Fair. Saturday. 10:00 Opening. 11:30 Music show. 13:00 Lunch. 14:30 Games in the yard. 16:00 Closing."
GFAIR = "(fair = feria; yard = patio; closing = cierre)"
RUN = "Paragraph 1: Mia likes to run. On Monday she runs 2 km. Paragraph 2: On Wednesday she rests. On Friday she runs 3 km in the park."
GRUN = "(rests = descansa; km = kilómetros)"

lesson(
    OA, 3,
    "Los horarios y textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer rápido para tener una idea general y a releer con atención para responder una pregunta precisa. Sirve para encontrar datos sin perderme en el texto.",
    ["Sé fijar un propósito y predecir.", "Sé leer horas y números en inglés."],
    [
        "Hay dos formas de lectura útiles. La lectura rápida (skimming) sirve para tener una idea general: miras el título, las primeras líneas y las palabras destacadas. La lectura focalizada (scanning) sirve para buscar un dato exacto, como una hora, un nombre o un número: recorres el texto con los ojos buscando solo esa palabra.",
        "Cuando una pregunta pide un dato preciso, relee la parte del texto donde está. Los números de párrafo ayudan: si la pregunta habla de lo que pasa el viernes, busca la palabra Friday y relee ese párrafo con calma. Después comprueba tu respuesta con el texto y no con tu memoria.",
        "Para responder bien, sigue estos pasos: 1) lee la pregunta, 2) subraya la palabra clave (por ejemplo lunch o 2 km), 3) recorre el texto hasta encontrarla, 4) relee esa parte con atención, 5) escribe la respuesta con las palabras del texto. Si la información no aparece, no la inventes: dices que el texto no la da.",
    ],
    [("skimming", "lectura rápida para la idea general"), ("scanning", "lectura focalizada para un dato"), ("reread", "releer"), ("keyword", "palabra clave"), ("detail", "detalle"), ("paragraph", "párrafo"), ("gist", "idea general")],
    [
        ("Buscar un dato con scanning", "Horario: «Music Club. Monday 3:00 Guitar. Tuesday 4:15 Drums. Friday 5:30 Choir.» (guitar = guitarra; drums = batería; choir = coro) ¿A qué hora es batería (Drums)?",
         ["La palabra clave es Drums.", "Recorre el texto hasta verla.", "Al lado dice Tuesday 4:15."], "A las 4:15 del martes."),
        ("Releer para un número", "Texto: «Tom reads 12 pages on Monday and 15 pages on Tuesday. On Wednesday he reads no pages.» (pages = páginas) ¿Cuántas páginas lee el martes?",
         ["Palabra clave: Tuesday.", "Relee esa oración: 15 pages.", "Comprueba que el número esté junto al día."], "15 páginas."),
    ],
    [
        ("Responder de memoria sin releer.", "Se confía en lo que se recuerda.", "Vuelve al texto y comprueba la respuesta con la palabra clave."),
        ("Leer todo palabra por palabra para encontrar un horario.", "No se distingue entre idea general y dato.", "Usa scanning: busca solo la palabra clave."),
    ],
    [
        ("¿Para qué sirve la lectura rápida (skimming)? a) Tener una idea general b) Encontrar un dato exacto", "a", "Skimming da la idea general; scanning busca un dato."),
        (f"Lee el horario: «{FAIR}» {GFAIR} ¿A qué hora empieza el almuerzo (Lunch)? Opciones: 13:00, 11:30.", "13:00", "La palabra clave Lunch está junto a 13:00."),
        ("¿Qué es una palabra clave? a) La palabra que buscas para responder una pregunta b) La palabra más larga", "a", "Es la guía para encontrar el dato."),
    ],
    [
        (f"Lee el horario: «{FAIR}» {GFAIR} ¿Qué actividad ocurre a las 14:30? a) Games in the yard b) Music show", "a", "A las 14:30 están los juegos en el patio."),
        (f"Lee el horario: «{FAIR}» {GFAIR} ¿Cuántas actividades tiene el programa desde Opening hasta Closing, contando ambas?", "5", "Opening, Music show, Lunch, Games y Closing son cinco."),
        (f"Lee el horario: «{FAIR}» {GFAIR} ¿Qué palabra clave buscas para saber a qué hora termina el evento? Opciones: Closing, Games.", "Closing", "Closing es el cierre del evento."),
    ],
    [
        (f"Lee el texto: «{RUN}» {GRUN} ¿Qué día descansa Mia? Escribe el día en inglés.", "Wednesday", "Relee el párrafo 2: On Wednesday she rests."),
        (f"Lee el texto: «{RUN}» {GRUN} ¿Cuántos kilómetros corre en total entre el lunes y el viernes?", "5", "Suma 2 km del lunes y 3 km del viernes.", "2+3"),
        (f"Lee el texto: «{RUN}» {GRUN} ¿En qué lugar corre el viernes? a) in the park b) at school", "a", "El párrafo 2 dice in the park."),
    ],
    [
        (f"Lee el horario: «{FAIR}» {GFAIR} Una compañera dice que hay un concurso de baile. ¿Qué respondes? a) El horario no lo menciona b) Es a las 16:00", "a", "No aparece; no se debe inventar información."),
        ("Texto: «The bus leaves at 8:15. The trip takes 45 minutes. The bus returns at 5:00 pm.» (trip = viaje; returns = vuelve) Julián dice que el bus sale a las 5:00. Relee. ¿Qué error cometió? a) Confundió la salida con el regreso b) Confundió la duración del viaje con la salida", "a", "8:15 es la salida; 5:00 pm es el regreso."),
    ],
    [
        ("Texto: «Paragraph 1: Lia has two cats called Nube and Sol. Paragraph 2: Nube is white and sleeps all day. Sol is orange and plays in the garden.» (sleeps = duerme; garden = jardín) La pregunta es: ¿Qué gato juega en el jardín? Escribe el nombre.", "Sol", "El párrafo 2 dice que Sol plays in the garden."),
        ("Mismo texto: «Paragraph 1: Lia has two cats called Nube and Sol. Paragraph 2: Nube is white and sleeps all day. Sol is orange and plays in the garden.» ¿De qué color es Nube? Responde en español.", "Blanca", "Nube is white indica el color."),
    ],
    [("Tienes este aviso del colegio: «Parents' meeting: Thursday 18:30, Room 4. Please arrive 10 minutes before.» (meeting = reunión; arrive = llegar) Una persona de tu casa quiere saber a qué hora conviene llegar. ¿Cuál es la respuesta? a) 18:20 b) 18:40", "a", "Debe llegar 10 minutos antes de las 18:30.")],
    [
        ("¿Qué tipo de lectura usas para buscar una hora exacta?", "Lectura focalizada (scanning)", "Buscas solo el dato."),
        ("¿Qué haces si el texto no da la información que te piden?", "Digo que el texto no la da", "No se inventan datos."),
        ("Para una idea general del texto, ¿qué lectura usas? a) Skimming b) Scanning", "a", "Skimming recorre el texto para la idea general."),
    ],
    task("Lee este programa: «Mountain Camp Day 2. 7:30 Breakfast. 9:00 Walk to the lake. 12:30 Picnic. 15:00 Painting. 18:00 Dinner.» (lake = lago; picnic = merienda; painting = pintura) En tu hoja responde: a) ¿Qué se hace a las 9:00? b) ¿A qué hora es la cena? c) ¿Cuántas comidas aparecen (breakfast, picnic, dinner)? d) Escribe la palabra clave que usaste en b).", "a) Caminar al lago. b) 18:00. c) 3. d) Dinner.", ["encuentra los datos exactos", "cuenta correctamente las comidas", "dice la palabra clave usada"], ["hoja con cuatro respuestas"], ["responder de memoria", "contar comidas que el texto no nombra"], "Pide que señale con el dedo la palabra clave en el programa."),
    "Copia el horario del Music Club de los ejemplos resueltos y subraya los días y las horas.",
    "Escribe un programa de tres actividades con horas en inglés y tres preguntas de scanning para otra persona.",
)

# ============================================================ clase 4: vocabulario por contexto y visualizar
lesson(
    OA, 4,
    "Las oraciones y textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a deducir el significado de una palabra nueva con las pistas de su oración y a visualizar lo que leo. Sirve para entender un texto aunque no conozca todas las palabras.",
    ["Sé buscar palabras clave en una oración.", "Conozco palabras como big, small, tired y happy."],
    [
        "Cuando aparece una palabra desconocida, no hace falta buscarla enseguida. Lee la oración completa y las oraciones de al lado: las otras palabras dan pistas de contexto (context clues). A veces la pista es un sinónimo («tiny, very small»), un contraste («but») o un ejemplo («for example…»), o una consecuencia («so she slept ten hours»).",
        "Los pasos son: 1) marca la palabra, 2) lee lo que dice antes y después, 3) imagina qué significa, 4) pruébalo en la oración para ver si tiene sentido, 5) confírmalo si puedes. Si solo adivinas por cómo se ve la palabra, puedes equivocarte: la pista debe estar en el texto.",
        "Visualizar (visualize) significa formar una imagen en la mente de lo que lees. Si lees «The room was tiny: a bed and a small desk fit», imaginas un cuarto muy pequeño. Dibujar o describir la imagen ayuda a comprobar que entendiste. Si la imagen no calza con el resto del texto, relee.",
    ],
    [("context clue", "pista de contexto"), ("infer", "deducir"), ("visualize", "formar una imagen mental"), ("tiny", "muy pequeño"), ("exhausted", "muy cansado"), ("synonym", "sinónimo"), ("meaning", "significado")],
    [
        ("Deducir una palabra con una consecuencia", "Oración: «She was exhausted after the long race, so she slept ten hours.» (race = carrera; slept = durmió) ¿Qué significa exhausted?",
         ["Mira lo que pasó después: durmió diez horas.", "Eso se hace cuando se está muy cansado.", "Probamos «muy cansada» en la oración y calza."], "Muy cansada."),
        ("Deducir con un sinónimo", "Oración: «It was a tiny room: only a bed and a small desk fit.» (desk = escritorio; fit = cabían) ¿Qué significa tiny?",
         ["Lee lo que viene después de los dos puntos.", "Solo cabían una cama y un escritorio pequeño.", "Tiny = muy pequeño."], "Muy pequeño."),
    ],
    [
        ("Adivinar por cómo se parece la palabra al español.", "Se cree que siempre se parecen.", "Busca la pista en el texto y pruébala en la oración."),
        ("Detenerse y no leer más cuando hay una palabra desconocida.", "Se piensa que hay que entender todo.", "Sigue leyendo: las oraciones siguientes pueden aclararla."),
    ],
    [
        ("¿Qué son las pistas de contexto?", "Las palabras alrededor que ayudan a entender una palabra nueva", "Están antes y después de la palabra desconocida."),
        ("«Visualize» significa: a) formar una imagen mental b) traducir palabra por palabra", "a", "Visualizar es imaginar lo que se lee."),
        ("«The elephant was enormous: it was bigger than a bus.» ¿Qué significa enormous? a) muy grande b) muy pequeño", "a", "Más grande que un bus indica un tamaño muy grande."),
    ],
    [
        ("«My socks are damp because I walked in the rain. Please dry them.» (socks = calcetines; dry = secar) ¿Qué significa damp? a) ligeramente mojado b) muy sucio", "a", "Caminó bajo la lluvia y hay que secarlos."),
        ("«The soup was delicious. I ate it all and asked for more.» (soup = sopa; asked for = pidió) ¿Qué significa delicious? a) muy rico b) muy caliente", "a", "Se lo comió todo y pidió más: le gustó mucho."),
        ("«The sky was gloomy and grey, and I wanted to stay in bed.» (sky = cielo) ¿Qué significa gloomy? a) oscuro y triste b) frío y con viento", "a", "El cielo gris y las ganas de quedarse en cama muestran un día triste."),
    ],
    [
        ("«He is timid: he never speaks in class and hides behind his friends.» (hides = se esconde) ¿Qué significa timid? Opciones: tímido, enojado.", "tímido", "No habla en clase y se esconde."),
        ("«The box was so heavy that I could not lift it.» (lift = levantar) ¿Qué significa heavy? Opciones: pesado, liviano.", "pesado", "No pudo levantarla, así que pesa mucho."),
        ("Lee y visualiza: «The cat jumped onto the tall shelf and looked down at the dog.» (shelf = repisa) ¿Dónde está el gato respecto del perro? Opciones: arriba, abajo.", "arriba", "Está en una repisa alta y mira hacia abajo."),
    ],
    [
        ("Un compañero lee: «Mario is fearless: he climbed the highest tree without stopping.» (climbed = trepó; highest = más alto) y dice que fearless significa «con miedo». ¿Qué pista muestra que se equivoca? a) Trepó el árbol más alto sin detenerse b) Mario es un nombre", "a", "Esa acción no calza con alguien que tiene miedo; significa sin miedo."),
        ("«It was freezing outside, so Ana wore two jackets and a hat.» (wore = usó) ¿Cuál es la mejor pista para deducir freezing? a) wore two jackets and a hat b) Ana", "a", "Se abriga mucho porque hace muchísimo frío."),
    ],
    [
        ("Lee: «Ema's room is a mess. Her clothes are on the floor, her books are under the bed and her toys are everywhere.» (mess = desorden; clothes = ropa; toys = juguetes) ¿Cuál es el mejor significado de a mess? a) un lugar desordenado b) un lugar limpio", "a", "Hay cosas tiradas por todos lados."),
        ("Lee: «The path was narrow: only one person could walk at a time.» (path = sendero; at a time = a la vez) ¿Qué significa narrow? Opciones: angosto, ancho.", "angosto", "Solo cabía una persona a la vez."),
    ],
    [("En una prueba aparece: «The old house was silent. No voices, no music, not even a clock ticking.» (voices = voces; ticking = haciendo tic-tac) No conoces silent. ¿Qué pista te ayuda más? a) No voices, no music b) The old house", "a", "Sin voces, música ni reloj indica que no hay ruido.")],
    [
        ("¿Qué haces cuando aparece una palabra desconocida?", "Leo alrededor y busco pistas", "El contexto ayuda a deducir el significado."),
        ("«Tiny» es lo contrario de: a) huge (enorme) b) small (pequeño)", "a", "Tiny es muy pequeño; huge es muy grande."),
        ("¿Para qué sirve visualizar? a) Para comprobar que entendí lo leído b) Para leer más rápido sin pensar", "a", "La imagen mental muestra si el texto tiene sentido."),
    ],
    task("Lee el texto: «The old bridge was fragile. When Pablo stepped on it, it shook. 'Careful!' shouted Dani. 'It could break!' They crossed one by one, very slowly.» (bridge = puente; stepped on = pisó; shook = se sacudió; break = romperse; one by one = uno a uno) En tu hoja escribe: a) qué crees que significa fragile, b) dos pistas del texto, c) un dibujo o una descripción de lo que visualizas.", "a) Frágil, que se rompe fácil. b) It shook; It could break. c) Un puente viejo que se mueve mientras cruzan despacio.", ["deduce el significado con pistas del texto", "cita dos pistas", "su imagen es coherente con el texto"], ["hoja con a), b) y c)"], ["adivinar sin pistas", "describir algo que el texto no dice"], "Pregunta si el significado calza si lo reemplaza en la oración."),
    "Copia el vocabulario de la tabla con su significado y una pista que recuerdes de cada palabra.",
    "Escribe dos oraciones en inglés con una palabra difícil y pistas claras para que otra persona deduzca su significado.",
)

# ============================================================ clase 5: resumir y comprobar
REC = "Recycling Day. Every Friday, students at Lago School bring clean plastic bottles and paper. Two students weigh the bags. Last month the school sent 40 kilos to a recycling centre. Now the class wants to plant flowers in the school garden."
GREC = "(bring = traen; weigh = pesan; recycling centre = centro de reciclaje; plant = plantar)"

lesson(
    OA, 5,
    "Los textos y organizadores escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a resumir un texto, a usar organizadores gráficos y a hacer preguntas para confirmar que entendí. Sirve para cerrar la lectura con seguridad.",
    ["Sé predecir, buscar datos y deducir palabras por contexto.", "Sé qué son una idea principal y un detalle."],
    [
        "Después de leer, un buen lector resume. Un resumen (summary) cuenta lo más importante con pocas palabras: la idea principal (main idea) y dos o tres detalles clave (key details). No copia todo ni agrega datos nuevos. Para recontar con apoyo (retell) puedes usar palabras como first, then, next y finally.",
        "Un organizador gráfico (graphic organizer) ordena la información: una tabla con «Main idea» y «Details», un esquema con una idea al centro y detalles alrededor, o una línea de tiempo con first, then, finally. Dibujarlo te ayuda a ver qué es lo central y qué es un detalle menor.",
        "Para confirmar información, pregunta o relee: «Do you mean…?» (¿Quieres decir…?), «Is it true that…?» (¿Es verdad que…?), «Can you repeat?» (¿Puedes repetir?). También puedes preguntarte: ¿mi resumen contesta quién, qué, dónde y cuándo? Si falta algo importante, relee y completa.",
    ],
    [("summary", "resumen"), ("main idea", "idea principal"), ("key detail", "detalle clave"), ("retell", "recontar"), ("graphic organizer", "organizador gráfico"), ("first / then / finally", "primero / luego / finalmente"), ("Do you mean…?", "¿Quieres decir…?")],
    [
        ("Separar idea principal y detalles", "Texto: «Bird Day. Every Saturday, a group of kids walks in the park to count birds. They write the names in a notebook. Last week they saw nine kinds of birds.» (count = contar; kinds = tipos) ¿Cuál es la idea principal y cuáles dos detalles la apoyan?",
         ["La idea principal: un grupo de niños cuenta aves los sábados.", "Detalle 1: anotan los nombres en un cuaderno.", "Detalle 2: la semana pasada vieron nueve tipos."], "Idea principal: niños cuentan aves los sábados. Detalles: anotan nombres y vieron nueve tipos."),
        ("Recontar con first, then, finally", "Texto: «Dani plants a seed in a pot. Every day she gives it water. After two weeks, a small green leaf appears.» (seed = semilla; pot = maceta; leaf = hoja) Recuenta con first, then y finally.",
         ["Primero planta la semilla.", "Luego le da agua cada día.", "Finalmente aparece una hoja verde."], "First, Dani plants a seed. Then she gives it water. Finally, a leaf appears."),
    ],
    [
        ("Copiar casi todo el texto como resumen.", "Se cree que más palabras dan más puntaje.", "Escribe solo la idea principal y dos detalles clave."),
        ("Agregar datos que el texto no dice.", "Se mezcla lo que uno sabe con lo que se leyó.", "Comprueba cada dato en el texto."),
    ],
    [
        ("¿Qué contiene un buen resumen? a) La idea principal y pocos detalles clave b) Todas las oraciones del texto", "a", "Un resumen es breve y central."),
        ("En Inglés (oficial): ¿Qué significa «retell»?", "Recontar", "Es volver a contar con tus palabras."),
        ("Para pedir que te aclaren algo, ¿qué dices? a) Do you mean…? b) Good morning.", "a", "Do you mean… confirma información."),
    ],
    [
        (f"Lee: «{REC}» {GREC} ¿Cuál es la idea principal? a) Los estudiantes reciclan cada viernes b) Hay un jardín muy grande", "a", "El texto trata del reciclaje semanal."),
        (f"Lee: «{REC}» {GREC} ¿Cuántos kilos se enviaron el mes pasado?", "40", "Last month the school sent 40 kilos."),
        (f"Lee: «{REC}» {GREC} ¿Qué quiere hacer el curso ahora? a) Plantar flores b) Pesar más botellas", "a", "Dice que quiere plantar flores en el jardín."),
    ],
    [
        (f"Lee: «{REC}» {GREC} Elige el mejor resumen. a) Every Friday the students bring bottles and paper to recycle, and now they want to plant flowers b) The school is called Lago School.", "a", "Incluye la idea principal y un detalle clave."),
        (f"Lee: «{REC}» {GREC} En un organizador, ¿es un detalle o la idea principal «Two students weigh the bags»? Escribe detalle o idea principal.", "detalle", "Apoya la idea, pero no es el tema central."),
        (f"Lee: «{REC}» {GREC} Ordena con letras: x) The school sends 40 kilos. y) Students bring bottles every Friday. z) The class wants to plant flowers. Escribe el orden en que aparecen en el texto.", "y, x, z", "Primero traen botellas, luego se mencionan los kilos y al final el plan de plantar."),
    ],
    [
        ("Un compañero resume «Bird Day» (niños que cuentan aves en el parque cada sábado) así: «Kids saw 90 birds and ate lunch.» Texto original: «Every Saturday, a group of kids walks in the park to count birds. They write the names in a notebook. Last week they saw nine kinds of birds.» (count = contar; kinds = tipos) ¿Qué problema tiene? a) Agrega datos que el texto no tiene b) Es muy breve", "a", "Cambia las cifras e inventa el almuerzo; un resumen debe ser fiel."),
        ("Texto: «Every Saturday, a group of kids walks in the park to count birds. They write the names in a notebook. Last week they saw nine kinds of birds.» (count = contar; kinds = tipos) Quieres comprobar si entendiste que los niños cuentan aves cada sábado. ¿Qué preguntas a tu compañero? a) Is it true that they count birds every Saturday? b) What time is it?", "a", "Es una pregunta para confirmar información."),
    ],
    [
        ("Texto: «Lia makes a paper boat. First she folds the paper. Then she draws a flag. Finally she puts the boat in a bowl of water.» (folds = dobla; flag = bandera; bowl = bol) ¿Qué ocurre en el medio, después de «First» y antes de «Finally»? a) Dibuja una bandera b) Dobla el papel", "a", "Then marca el segundo paso."),
        ("Mismo texto: «Lia makes a paper boat. First she folds the paper. Then she draws a flag. Finally she puts the boat in a bowl of water.» Completa el esquema: Idea principal = Lia makes ___. Escribe lo que falta.", "a paper boat", "La primera oración dice qué hace."),
    ],
    [("Tu profesor lee: «The library opens at 9:00. On Wednesdays it has a story hour for children at 4:00.» (story hour = hora del cuento) Quieres confirmar. ¿Qué preguntas? a) Do you mean the story hour is at 4:00 on Wednesdays? b) Where is the school?", "a", "Repite la información para confirmarla.")],
    [
        ("¿Cuáles dos partes tiene un resumen?", "La idea principal y los detalles clave", "Son lo central del texto."),
        ("¿Para qué sirve un organizador gráfico?", "Para ordenar la información de un texto", "Muestra qué es central y qué es detalle."),
        ("¿Qué palabra usas para el último paso al recontar? a) finally b) first", "a", "Finally cierra una secuencia."),
    ],
    task("Lee: «Helena gets a new bike for her birthday. First she learns to ride in the yard. Then she rides to school with her brother. On Sunday they go to the lake and have a picnic.» (learns = aprende; ride = andar; yard = patio) En tu hoja haz: a) un organizador con Main idea y dos Details, b) un recuento de tres oraciones con first, then y finally, c) una pregunta para confirmar un dato.", "a) Main idea: Helena aprende a andar en su bicicleta nueva. Details: va al colegio con su hermano; el domingo van al lago. b) First she learns... Then she rides... Finally they go to the lake. c) Is it true that they go to the lake on Sunday?", ["separa idea principal y detalles", "usa first, then y finally en orden", "la pregunta confirma un dato del texto"], ["hoja con organizador, recuento y pregunta"], ["agregar datos inventados", "confundir idea principal con detalle"], "Pide que lea su recuento y señale el dato en el texto."),
    "Copia el organizador de la explicación en tu hoja y llénalo con un texto breve de este cuaderno.",
    "Resume en dos oraciones en inglés una película o serie que conozcas, usando la idea principal y un detalle.",
)
