"""Cuaderno del estudiante, 1.º medio Inglés (oficial): IN1M OA 14, proceso de escritura en géneros con propósito.

Géneros: cuento, correo, folleto, rima, descripción, biografía, instrucciones, artículo, carta, resumen y diario.
Proceso: organizar ideas, redactar, revisar, editar y publicar, con procesador de textos y diccionario en línea.
Los textos de ejemplo son originales; las entradas de diccionario se escriben dentro del enunciado.
"""
from __future__ import annotations

from student_content_in_m1_b import MAT, lesson, mc, task
from student_lessons import arith, ex

OA = "IN1M OA 14"

# ============================================================ clase 1: géneros, propósito y audiencia
EMAIL = "«Dear Ms. Rojas, I am writing to ask if I can turn in my science project on Friday. I was sick on Monday. Thank you for your time. Best regards, Camila»"
GEMAIL = "(turn in = entregar; project = trabajo; sick = enferma; thank you for your time = gracias por su tiempo; best regards = saludos cordiales)"
JOUR = "«Tuesday, 7 p.m. Today I finally learned to ride my bike without help! I was scared at first, but then I felt proud. Tomorrow I want to ride to the park.»"
GJOUR = "(learned = aprendí; ride = andar; without help = sin ayuda; scared = con miedo; proud = orgulloso)"
BROCH = "«Visit the Butterfly House! Open every day from 10:00 to 17:00. Free for children under 12. Walk among hundreds of colorful butterflies. Come and see!»"
GBROCH = "(butterfly = mariposa; open = abierto; free = gratis; under = menores de; among = entre; hundreds = cientos)"
BEAN = "«How to plant a bean. First, fill a cup with soil. Next, push a bean into the soil. Then add a little water. Finally, put the cup near a window.»"
GBEAN = "(plant = plantar; bean = poroto; cup = vaso; soil = tierra; push = empujar; window = ventana)"
BIO = "«Gabriela Mistral was born in Vicuña, Chile, in 1889. She was a poet and a teacher. In 1945 she received the Nobel Prize in Literature.»"
GBIO = "(born = nació; poet = poeta; teacher = profesora; received = recibió; prize = premio)"
RHY = "«Ten red balloons up in the sky, / Ten red balloons are floating by. / Pop goes one, and what is the news? / Nine red balloons are left to choose!»"
GRHY = "(balloons = globos; floating = flotando; pop = revienta; left = quedan)"
NEWS = "«Headline: Students Win Science Award. A team from a school in Osorno won first prize at a regional science fair last Saturday. Their project turns used paper into plant pots. (Texto de ejemplo.)»"
GNEWS = "(award = premio; regional = regional; project = proyecto; turns = convierte; used paper = papel usado; plant pots = macetas)"
THANKS = "«Note 1: Dear Mr. Vera, We would like to ask permission to hold a book fair next month. Sincerely, Class 1B.»"
NOTE2 = "«Note 2: Lost: black backpack. Please return it to the office.»"
NOTE3 = "«Note 3: Tuesday. Dear diary, today I was nervous before the test.»"
GNOTES = "(permission = permiso; hold = organizar; sincerely = atentamente; lost = perdida; backpack = mochila; return = devolver; office = oficina; nervous = nervioso; test = prueba)"

lesson(
    OA, 1, MAT,
    "Aprenderé a reconocer once géneros de escritura (cuento, correo, diario, folleto, instrucciones, biografía, rima, descripción, artículo, carta y resumen) y a decidir cuál sirve para cada propósito y audiencia. Sirve para elegir cómo escribir antes de empezar.",
    ["Sé escribir oraciones y párrafos cortos en inglés.", "Conozco palabras como letter, story y title."],
    [
        "Cada género (genre) tiene un propósito y rasgos propios. Un correo electrónico (email) o una carta (letter) comunica un mensaje a una persona y lleva saludo (Dear…) y despedida (Best regards, Sincerely). Un diario personal (journal) cuenta lo que sientes y vives, en primera persona, con la fecha. Un folleto (brochure) invita a visitar o a comprar, con datos prácticos y frases cortas. Las instrucciones (instructions) enseñan pasos en orden con first, next, then y finally.",
        "Una biografía (biography) cuenta la vida de una persona real, con fechas y logros, en tercera persona y pasado. Una rima (rhyme) usa versos cortos cuyos finales suenan parecido. Una descripción (description) dice cómo es algo, con adjetivos y detalles de los sentidos. Un artículo (article) informa de un hecho con un titular y datos. Un resumen (summary) cuenta lo más importante de otro texto en pocas palabras. Un cuento (story) narra hechos con personajes.",
        "Para elegir el género, pregúntate para qué escribes y para quién. Un correo a una profesora usa un registro formal: saludo, cortesía y sin abreviaturas. Una nota a un amigo puede ser informal. El mismo tema puede escribirse en géneros distintos, pero cada uno tiene su forma.",
    ],
    [("email / letter", "correo / carta"), ("journal", "diario personal"), ("brochure", "folleto"), ("instructions", "instrucciones"), ("biography", "biografía"), ("rhyme", "rima"), ("description", "descripción"), ("article", "artículo"), ("summary", "resumen"), ("story", "cuento"), ("formal / informal", "formal / informal")],
    [
        ("Reconocer un correo formal", f"Texto: {EMAIL} {GEMAIL} ¿Qué género es, cuál es su propósito y por qué es formal?",
         ["Empieza con Dear Ms. Rojas y termina con Best regards.", "Pide permiso para entregar un trabajo otro día: eso es el propósito.", "Es formal porque saluda con cortesía y da las gracias."], "Es un correo; su propósito es pedir entregar un trabajo otro día; es formal por el saludo y la cortesía"),
        ("Reconocer un diario", f"Texto: {JOUR} {GJOUR} ¿Qué rasgos muestran que es un diario?",
         ["Empieza con el día y la hora: Tuesday, 7 p.m.", "Habla en primera persona (I) y cuenta emociones.", "Termina con un plan personal para mañana."], "Fecha, primera persona y sentimientos personales"),
    ],
    [
        ("Escribir una nota para tu profesora como si fuera para un amigo, con «hey» y signos de exclamación.", "No se adapta a la audiencia ni al registro formal.", "Usa saludo, cortesía y una despedida formal."),
        ("Llamar biografía a un texto sobre una persona inventada.", "Una biografía trata de una persona real.", "Si es inventada, es un cuento."),
    ],
    [
        mc("Las instrucciones (instructions) enseñan", "pasos para hacer algo, en orden", ["la vida de una persona", "qué sintió alguien hoy"], "Usan first, next, then y finally."),
        mc("Lee: «One night, Teo heard a noise in the attic. He took a flashlight and climbed the stairs. It was only the wind, and Teo laughed.» (attic = entretecho; flashlight = linterna; climbed = subió; stairs = escalera; wind = viento) ¿Qué género es?", "Un cuento, porque narra hechos con un personaje", ["Una descripción, porque dice cómo es un lugar", "Un artículo, porque informa un hecho real"], "Narra una secuencia de hechos con un personaje, Teo, que sube la escalera y se ríe."),
        mc("Un diario personal (journal) se escribe en", "primera persona y con la fecha", ["tercera persona sin fecha", "un registro formal de empresa"], "Cuenta lo que vive el autor."),
    ],
    [
        mc(f"Lee: {BROCH} {GBROCH} ¿Qué género es?", "Un folleto", ["Una biografía", "Un diario"], "Invita a visitar, con horario y datos prácticos."),
        mc(f"Lee: {BROCH} {GBROCH} ¿Cuál es su propósito?", "Invitar a las personas a visitar la casa de mariposas", ["Contar la vida de una persona", "Enseñar a plantar un poroto"], "Dice Come and see! e incluye horario y precio."),
        mc(f"Lee: {BROCH} {GBROCH} ¿Quiénes son su audiencia más probable?", "Familias con niños", ["Solo científicos", "Solo jubilados"], "Menciona que es gratis para niños menores de 12."),
    ],
    [
        mc(f"Lee: {BIO} {GBIO} ¿Qué pista muestra que es una biografía?", "Cuenta una vida real con fechas y logros en tercera persona", ["Tiene versos que riman", "Da pasos numerados"], "Born, 1889, 1945 y She son marcas de biografía."),
        mc(f"Lee: {RHY} {GRHY} ¿Qué género es?", "Una rima", ["Un artículo", "Una carta"], "Tiene versos cortos cuyos finales suenan parecido (sky con by)."),
        mc(f"Lee: {NEWS} {GNEWS} ¿Qué rasgo muestra que es un artículo?", "Tiene un titular y datos de un hecho reciente", ["Termina con saludo", "Tiene viñetas con diálogo"], "Un artículo informa un hecho con titular y datos."),
    ],
    [
        mc("Debes escribir al director del colegio. ¿Qué saludo conviene?", "Dear Mr. Vera,", ["Hey dude!", "Yo, Vera!"], "Un saludo formal respeta el registro del destinatario."),
        mc("Para enseñar a un compañero a plantar un poroto, ¿qué género sirve mejor?", "Instrucciones, porque hay pasos en orden", ["Una rima, porque suena bonito", "Una biografía, porque es una acción"], "El propósito es enseñar pasos."),
    ],
    [
        mc("El tema es la huerta del colegio. ¿Cuál de estos textos es una descripción?", "«The school garden is small and green. It has twelve tomato plants.»", ["«First, fill a pot with soil. Next, add a seed.»", "«Dear Mayor, please give us money for tools.»"], "Dice cómo es la huerta; las otras dos son instrucciones y una carta."),
        mc("¿Qué frase NO pertenece a un folleto de museo?", "Dear diary, I feel sleepy today", ["Open from 10:00 to 17:00", "Free for children"], "Es una frase de diario, no de folleto."),
    ],
    [mc(f"Encuentras tres notas en la cartelera. {THANKS} {NOTE2} {NOTE3} {GNOTES} ¿Cuál es una carta que pide permiso?", "La nota 1", ["La nota 2", "La nota 3"], "La nota 1 saluda, pide permiso y se despide.")],
    [
        mc("¿Qué género usa saludo y despedida?", "Un correo o una carta", ["Una rima"], "Dear y Best regards son marcas de correo."),
        mc("Original: «A small library in our town has a free reading club for children. Volunteers read stories aloud every Saturday. At first, ten children came, and now fifty come each week.» (volunteers = voluntarios; aloud = en voz alta) ¿Cuál es el mejor resumen (summary)?", "A town library's free reading club grew from ten to fifty children", ["Volunteers read stories aloud every Saturday", "The town library is very big and has many books for adults"], "Un resumen dice la idea principal sin agregar datos; la segunda opción es solo un detalle y la tercera inventa información."),
        ("Escribe en inglés la palabra que significa «folleto».", "Brochure", "Brochure es un folleto informativo."),
    ],
    task("Lee estos cuatro textos y escribe el género de cada uno y una pista: Texto A: «First, wash your hands. Next, wet them with water. Then rub them with soap. Finally, rinse and dry.» Texto B: «Dear Ana, thank you for the invitation. See you on Saturday! Love, Eva» Texto C: «The beach is wide and quiet. The sand is warm and the waves are gentle.» Texto D: «Pablo Neruda was born in 1904. He was a poet from Chile.» (wash = lavar; rub = frotar; soap = jabón; rinse = enjuagar; dry = secar; wide = ancha; waves = olas; gentle = suaves)",
         "A: instrucciones (first, next, then, finally). B: carta o correo informal (Dear Ana, Love). C: descripción (adjetivos como wide, quiet, warm). D: biografía (nació en 1904, tercera persona).",
         ["identifica el género de los cuatro textos", "da una pista distinta para cada uno", "usa el nombre del género en inglés o en español"],
         ["cuatro líneas en la hoja con género y pista"],
         ["confundir una descripción con instrucciones", "dar el género sin ninguna pista"],
         "Pide que cambie el propósito de un texto y diga cómo cambiaría el género."),
    "Copia los once géneros con su propósito y dibuja un símbolo para cada uno.",
    "Elige un género que no practicaste (cuento, rima, biografía, resumen o artículo) y escribe en inglés tres o cuatro oraciones o versos con sus rasgos.",
)

# ============================================================ clase 2: organizar ideas y redactar
PARA = "«My neighborhood is friendly and lively. In the morning, the baker sells warm bread. In the afternoon, children play soccer in the square. At night, neighbors chat on their doorsteps. I love living here.»"
GPARA = "(neighborhood = barrio; friendly = amistoso; lively = animado; baker = panadero; warm = tibio; square = plaza; chat = conversar; doorsteps = entradas de las casas)"
STUDY = "«A good study place needs three things. First, it needs silence, so you can think. Second, it needs good light, so your eyes do not get tired. Finally, it needs a clean desk, so you can find your things. With these three things, studying is easier.»"
GSTUDY = "(study = estudio; silence = silencio; light = luz; tired = cansados; desk = escritorio; find = encontrar)"
WINT = "«Winter in the south is cold and wet. Rain falls almost every day. People wear thick coats and boots. My cousin has a red bike. Many families stay indoors with hot tea.»"
GWINT = "(winter = invierno; wet = húmedo; thick = gruesos; coats = abrigos; boots = botas; indoors = bajo techo; tea = té)"
SHORT = "«My room is small.»"

lesson(
    OA, 2, MAT,
    "Aprenderé a organizar mis ideas antes de escribir y a redactar un párrafo con oración temática, detalles y cierre. Sirve para que mi texto tenga orden y cumpla un criterio de evaluación.",
    ["Sé reconocer el género de un texto.", "Conozco conectores como first, then y because."],
    [
        "El proceso de escritura (writing process) tiene cinco pasos: organizar ideas (plan), redactar (draft), revisar (revise), editar (edit) y publicar (publish). Hoy trabajamos los dos primeros. Para organizar las ideas, haz una lluvia de ideas (brainstorm): anota palabras sin juzgarlas. Luego agrúpalas en un mapa de ideas o en un esquema (outline) y elige un orden lógico.",
        "Al redactar un párrafo, empieza con una oración temática (topic sentence) que dice la idea principal. Sigue con detalles de apoyo (supporting details): ejemplos, datos o razones. Cierra con una oración final (closing sentence) que repite o completa la idea. Los conectores como first, second, finally, because y so ayudan a unir las ideas. Toda oración debe hablar del mismo tema; si una no calza, se elimina.",
        "Muchas veces un profesor da un criterio (criterion) para evaluar, por ejemplo: un párrafo con una oración temática, tres detalles y un cierre. Revisa tu borrador contra ese criterio, punto por punto, y marca la evidencia en tu texto. Así sabes qué cumple y qué falta.",
    ],
    [("writing process", "proceso de escritura"), ("brainstorm", "lluvia de ideas"), ("outline", "esquema"), ("topic sentence", "oración temática: idea principal del párrafo"), ("supporting detail", "detalle de apoyo"), ("closing sentence", "oración de cierre"), ("criterion", "criterio de evaluación")],
    [
        ("Agrupar ideas en un mapa", "Lluvia de ideas para un folleto de la biblioteca: open Monday to Friday 8:00–16:00; borrow two books; comics and novels; quiet reading corner; ask the librarian. (borrow = pedir prestado; librarian = bibliotecaria) Agrúpalas en When, What y Rules.",
         ["When responde cuándo está abierta: Monday to Friday 8:00–16:00.", "What responde qué hay: comics and novels; quiet reading corner.", "Rules son las normas: borrow two books; ask the librarian."], "When: open Monday to Friday 8:00–16:00. What: comics and novels; quiet reading corner. Rules: borrow two books; ask the librarian"),
        ("Revisar un párrafo contra un criterio", f"Texto: {PARA} {GPARA} Criterio: una oración temática, tres detalles y un cierre. ¿Lo cumple?",
         ["La primera oración dice la idea principal: friendly and lively.", "Los detalles son el panadero, los niños que juegan y los vecinos que conversan, tres en total.", "La última oración I love living here cierra el párrafo."], "Sí cumple: oración temática, tres detalles y cierre"),
    ],
    [
        ("Empezar el párrafo con un detalle sin decir la idea principal.", "Falta la oración temática.", "Primero escribe la idea principal."),
        ("Dejar una oración que no tiene que ver con el tema.", "Rompe la unidad del párrafo.", "Elimínala o cambia el tema."),
    ],
    [
        mc("Una oración temática (topic sentence) dice", "la idea principal del párrafo", ["el nombre del autor", "la última palabra"], "Es la idea que los detalles apoyan."),
        mc("Hacer una lluvia de ideas (brainstorm) es", "anotar ideas sin juzgarlas", ["corregir ortografía", "imprimir el texto"], "Es el primer paso para organizar."),
        mc("Un detalle de apoyo (supporting detail) es", "información que apoya la idea principal", ["una opinión sin relación", "el título del libro"], "Aporta ejemplos o razones."),
    ],
    [
        mc(f"Lee: {STUDY} {GSTUDY} ¿Cuál es la oración temática?", "A good study place needs three things", ["Finally, it needs a clean desk", "With these three things, studying is easier"], "Anuncia la idea principal del párrafo."),
        mc(f"Lee: {STUDY} {GSTUDY} ¿Cuántos detalles de apoyo tiene?", "Tres: silence, light y a clean desk", ["Uno", "Dos"], "Son first, second y finally."),
        mc(f"Lee: {STUDY} {GSTUDY} ¿Qué conector introduce el último detalle?", "Finally", ["Because", "But"], "Finally presenta el tercer y último detalle."),
    ],
    [
        mc(f"Lee: {WINT} {GWINT} ¿Qué oración NO pertenece al párrafo?", "My cousin has a red bike", ["Rain falls almost every day", "People wear thick coats and boots"], "No tiene relación con el invierno en el sur."),
        mc(f"Lee: {WINT} ¿Cuál es la idea principal?", "El invierno en el sur es frío y húmedo", ["Los primos tienen bicicletas", "Las familias toman té en verano"], "La primera oración la dice."),
        mc(f"Lee: {WINT} ¿Qué oración agrega un buen detalle de apoyo para «Rain falls almost every day»?", "The streets are wet and the rivers are full", ["The bakery sells bread", "A red bike costs a lot"], "Es una consecuencia coherente con la lluvia."),
    ],
    [
        mc(f"Criterio: una oración temática, tres detalles y un cierre. Texto: {SHORT} ¿Qué falta?", "Detalles de apoyo y un cierre", ["Un título en inglés", "Más colores"], "Solo hay una oración, que es la idea principal; faltan los detalles y el cierre."),
        mc("Un borrador A tiene oración temática, tres detalles y cierre. Un borrador B es una lista de tres detalles sin idea principal. Criterio: debe haber una oración temática. ¿Cuál lo cumple?", "El borrador A", ["El borrador B", "Ambos"], "B no dice la idea principal."),
    ],
    [
        mc("Ordena el procedimiento: (1) Finally, add a little water. (2) First, put soil in a cup. (3) Next, push a seed into the soil. ¿Qué orden es el correcto?", "2, 3, 1", ["1, 2, 3", "3, 1, 2"], "First va primero, next lo sigue y finally cierra."),
        mc("Los detalles son: «Fruit is sweet. Fruit has vitamins. Fruit is easy to carry.» (sweet = dulce; vitamins = vitaminas; carry = llevar) ¿Cuál es la mejor oración temática?", "Fruit is a good snack for school", ["I ate fruit yesterday", "Vegetables are green"], "Resume los tres detalles."),
    ],
    [mc("Escribirás un párrafo para el diario del curso sobre el recreo. ¿Qué plan de ideas es el mejor?", "Una idea principal, tres detalles ordenados y una oración de cierre", ["Tres oraciones sin relación entre sí", "Solo el título"], "Un plan claro cumple con el criterio de un párrafo.")],
    [
        mc("¿Cuál es el orden de los dos primeros pasos del proceso de escritura?", "Organizar ideas y redactar", ["Publicar y revisar"], "Primero se planifica, luego se redacta."),
        mc("¿Para qué sirve un criterio de evaluación?", "Para revisar si el texto cumple lo pedido", ["Para decorar"], "Marca lo que debe tener el texto."),
        ("Escribe en inglés la palabra que significa «detalle de apoyo» (dos palabras).", "Supporting detail", "Supporting detail apoya la idea principal."),
    ],
    task("Escribe un párrafo de cinco oraciones sobre un día en la playa con esta lluvia de ideas: sand, waves, sunscreen, build a sandcastle, seagulls. (sand = arena; waves = olas; sunscreen = bloqueador solar; sandcastle = castillo de arena; seagulls = gaviotas) Elige una oración temática, tres de las ideas como detalles y un cierre.",
         "A day at the beach is relaxing and fun. First, we put on sunscreen. Then we build a sandcastle near the waves. After that, we watch the seagulls. I love beach days.",
         ["empieza con una oración temática", "usa tres detalles de la lluvia de ideas", "termina con una oración de cierre"],
         ["párrafo de cinco oraciones en la hoja"],
         ["usar ideas que no están en la lista", "no incluir una oración de cierre"],
         "Pide que subraye con colores la oración temática, los detalles y el cierre."),
    "Copia los siete términos y escribe un ejemplo breve de cada uno.",
    "Haz una lluvia de ideas de seis palabras sobre tu comida favorita y agrúpalas en dos categorías.",
)

# ============================================================ clase 3: revisar y editar
DRAFTA = "«i like my school becaus the teachers is kind.»"
FEED = "«My dog is nice.»"

lesson(
    OA, 3, MAT,
    "Aprenderé a revisar las ideas de un texto y a editar la gramática, la ortografía y la puntuación, y a dar sugerencias amables a un compañero. Sirve para mejorar mi borrador antes de entregarlo.",
    ["Sé organizar ideas y redactar un párrafo.", "Conozco el verbo to be y el presente simple."],
    [
        "Revisar (revise) y editar (edit) no son lo mismo. Revisar es mejorar el contenido: ¿la idea principal está clara?, ¿faltan detalles?, ¿las ideas están en orden?, ¿se entienden los conectores? Editar es corregir la forma: ortografía (spelling), puntuación (punctuation), mayúsculas (capital letters) y gramática (grammar). Primero se revisa y luego se edita.",
        "Errores frecuentes: olvidar la -s con he, she o it (She goes, no She go); usar el plural (I have two sisters, no two sister); usar I y no me como sujeto (My friend and I are happy); usar el pasado para lo que ya ocurrió (Yesterday I went to the park, we played); concordar there is con singular y there are con plural (There are many people); usar doesn't con he, she o it (He doesn't like fish); escribir bien palabras como friend, because, receive y tomorrow; y empezar con mayúscula las oraciones, los nombres, los días de la semana y la palabra I. El apóstrofe (') se usa en contracciones como don't, doesn't y can't. En preguntas se escribe el signo de interrogación al final.",
        "Cuando lees el texto de un compañero, da una sugerencia amable y concreta (feedback). Puedes decir: I like… because… (me gusta… porque…), You could add… (podrías agregar…) o Maybe you should change… (quizás deberías cambiar…). Evita frases que ofendan; habla del texto y no de la persona.",
    ],
    [("revise", "revisar el contenido"), ("edit", "editar la forma"), ("spelling", "ortografía"), ("punctuation", "puntuación"), ("capital letter", "mayúscula"), ("feedback", "comentario para mejorar"), ("apostrophe", "apóstrofe: el signo ' de don't"), ("You could add…", "podrías agregar…")],
    [
        ("Editar una oración", f"Corrige la ortografía, las mayúsculas y la gramática: {DRAFTA} (because = porque; kind = amables)",
         ["Falta la mayúscula en I y al comienzo.", "Becaus se escribe because.", "El sujeto teachers es plural: the teachers are kind."], "I like my school because the teachers are kind."),
        ("Dar feedback amable", f"Un compañero escribió: {FEED} (nice = simpático). Escribe un comentario con la forma «I like… You could add…».",
         ["Primero algo positivo sobre su texto.", "Luego una sugerencia concreta.", "Por ejemplo, agregar una razón con because."], "I like your topic. You could add a detail, such as: My dog is nice because he plays with children."),
    ],
    [
        ("Corregir solo la ortografía y pensar que ya se revisó el texto.", "Se editó la forma, pero no se mejoró el contenido.", "Revisa también las ideas, los detalles y el orden."),
        ("Dar feedback como «your text is bad».", "No es concreto ni ayuda a mejorar.", "Di algo positivo y una sugerencia específica."),
    ],
    [
        mc("Revisar (revise) un texto significa", "mejorar ideas, detalles y orden", ["corregir solo las tildes", "cambiar el tamaño de letra"], "Se trabaja el contenido."),
        mc("Editar (edit) un texto significa", "corregir ortografía, puntuación y gramática", ["agregar más ideas", "cambiar de tema"], "Se trabaja la forma."),
        mc("¿Qué se escribe con mayúscula en inglés?", "La palabra I, los nombres y el comienzo de una oración", ["Todos los verbos", "Todas las palabras de un párrafo"], "Esas son las reglas de mayúsculas."),
    ],
    [
        mc("¿Cuál es la oración corregida? «She go to school by bus.»", "She goes to school by bus", ["She going to school by bus", "She gos to school by bus"], "Con she, el verbo go lleva -es."),
        mc("¿Cuál es la oración corregida? «I have two sister.»", "I have two sisters", ["I has two sister", "I have two sisters's"], "Después de two el sustantivo va en plural."),
        mc("¿Cuál es la oración corregida? «There is many people in the park.»", "There are many people in the park", ["There is much people in the park", "There be many people in the park"], "People es plural, por lo que se usa there are."),
    ],
    [
        mc("¿Cómo se escribe bien la palabra «amigo»?", "Friend", ["Freind", "Frend"], "La regla frecuente es i antes de e en friend."),
        mc("¿Cuál es la oración corregida? «He don't like fish.»", "He doesn't like fish", ["He not like fish", "He doesn't likes fish"], "Con he se usa doesn't y el verbo va sin -s."),
        mc("¿Cuál oración tiene el apóstrofe bien puesto?", "I don't like fish", ["I do'nt like fish", "I dont' like fish"], "El apóstrofe reemplaza la o de not y va entre n y t: don't."),
    ],
    [
        mc("¿Cuál de estas acciones es revisar y no editar?", "Agregar un detalle al segundo párrafo", ["Cambiar «recieve» por «receive»", "Poner una coma que faltaba"], "Agregar un detalle mejora el contenido."),
        mc("Un compañero escribió un cuento breve. ¿Cuál es un comentario constructivo?", "I like the ending. You could add a sentence about the weather", ["Your story is boring", "You write badly"], "Es positivo y concreto."),
    ],
    [
        mc("¿Cuál es la versión completamente corregida? «yesterday i go to the park with my freind and we plays soccer»", "Yesterday I went to the park with my friend and we played soccer.", ["Yesterday I go to the park with my friend and we played soccer.", "Yesterday I went to the park with my freind and we plays soccer."], "Corrige mayúsculas, pasado, ortografía y puntuación."),
        mc("¿Cuál de estas oraciones no tiene errores?", "My brother and I are happy because we have a new dog.", ["My brother and me is happy because we have a new dog.", "My brother and I are happy becaus we has a new dog."], "Tiene concordancia, ortografía y verbos correctos."),
    ],
    [mc("En clase revisas el correo de un compañero a un profesor: «hi teacher, i cant come tomorow». (can't = no puedo; tomorrow = mañana) ¿Qué conjunto de correcciones es el más completo?", "Dear teacher, I can't come tomorrow.", ["Hi teacher, i can't come tomorow", "Dear teacher I cant come tomorrow"], "Corrige saludo formal, mayúscula en I, apóstrofe y ortografía de tomorrow.")],
    [
        mc("¿Qué se hace primero?", "Revisar las ideas y luego editar la forma", ["Editar y luego no revisar nada"], "Primero el contenido, después la forma."),
        mc("¿Qué frase sirve para dar una sugerencia amable?", "You could add a detail", ["Your text is bad"], "Es concreta y respetuosa."),
        ("Escribe correctamente en inglés la palabra «mañana» (tomorrow).", "Tomorrow", "Tomorrow se escribe con una m y dos r."),
    ],
    task("Corrige este borrador en tu hoja y escribe un comentario amable en inglés para quien lo escribió: «my friend and me goes to the library on saturday. We reads comics and we eat a snack.» (library = biblioteca; comics = cómics; snack = colación)",
         "My friend and I go to the library on Saturday. We read comics and we eat a snack. Feedback: I like your topic. You could add where you eat the snack.",
         ["corrige mayúsculas y nombres de días", "corrige la concordancia de los verbos", "escribe un comentario con algo positivo y una sugerencia"],
         ["texto corregido y comentario en la hoja"],
         ["dejar goes o reads sin corregir", "dar un comentario sin sugerencia concreta"],
         "Pide que explique cada corrección como revisión o como edición."),
    "Copia los errores frecuentes de la explicación con su corrección.",
    "Revisa un mensaje que hayas escrito en español y marca cuáles son errores de contenido y cuáles de forma.",
)

# ============================================================ clase 4: publicar con procesador de textos y diccionario (brecha)
DIC_CROWD = "«crowded (adjective): with many people in a small space. Example: The bus was crowded.»"
DIC_LIVELY = "«lively (adjective): full of energy and activity. Example: The festival was lively.»"
DIC_SILENT = "«silent (adjective): without any sound. Example: The library is silent.»"
GDIC = "(adjective = adjetivo; space = espacio; energy = energía; activity = actividad; sound = sonido; example = ejemplo)"
CARD_A = "«Card A (draft): The festival was very ___ (1) and the music was ___ (2).»"
CARD_B = "«Card B (notes): (1) there were many people in a small space; (2) it made everyone move and smile.»"
GCARDS = "(festival = fiesta; space = espacio; move = moverse; smile = sonreír)"
CHEER = "«cheerful (adjective) /ˈtʃɪrfəl/: happy and positive. Example: She has a cheerful voice.»"
GCHEER = "(positive = positivo; voice = voz)"

lesson(
    OA, 4, MAT,
    "Aprenderé a usar un procesador de textos y un diccionario en línea para elegir palabras y dar formato a la versión final, y a trabajar en pareja con tarjetas. Sirve para publicar un texto claro y bien presentado.",
    ["Sé revisar y editar un borrador.", "Conozco las partes de la oración: sustantivo, verbo y adjetivo."],
    [
        "Publicar (publish) es compartir la versión final con una audiencia: pegarla en el diario mural, enviarla por correo del curso o imprimirla en un librito. Antes de publicar, el texto debe tener título, párrafos claros y buena presentación. No incluyas datos privados como dirección o teléfono, y usa solo nombres que tengas permiso de usar.",
        "El procesador de textos (word processor) ayuda a presentar y a revisar. Tiene corrector ortográfico (spell check), que subraya palabras dudosas; letra más grande o en negrita para los títulos (bold, heading); listas con viñetas (bullet list) para pasos o datos; y la opción de guardar (save) con frecuencia. El corrector no entiende el significado: una palabra bien escrita puede estar mal elegida.",
        "El diccionario en línea (online dictionary) da, para cada palabra, la clase de palabra (adjective, noun, verb), la definición (definition), un ejemplo (example) y a veces la pronunciación. Para elegir bien, lee la definición y comprueba que el ejemplo se parezca a tu oración. Con una brecha de información puedes unir una tarjeta con un borrador con espacios y otra con notas o entradas de diccionario.",
    ],
    [("publish", "publicar"), ("word processor", "procesador de textos"), ("spell check", "corrector ortográfico"), ("bullet list", "lista con viñetas"), ("online dictionary", "diccionario en línea"), ("definition", "definición"), ("example", "ejemplo")],
    [
        ("Leer una entrada de diccionario", f"Entrada: {CHEER} {GCHEER} Completa: «The ___ clown made the children laugh.» (clown = payaso; laugh = reír)",
         ["Cheerful significa feliz y positivo.", "Un payaso que hace reír es feliz y positivo.", "La palabra calza con el ejemplo de la entrada."], "cheerful"),
        ("Elegir herramientas del procesador", "Necesitas que el título sea más grande y que tres consejos aparezcan como una lista. ¿Qué herramientas usas?",
         ["Para el título uso letra más grande o encabezado (heading).", "Para los consejos uso una lista con viñetas.", "Después guardo el archivo."], "Heading o letra grande para el título y lista con viñetas para los consejos"),
    ],
    [
        ("Confiar solo en el corrector ortográfico.", "Una palabra bien escrita puede ser la palabra equivocada.", "Revisa también el significado con el diccionario."),
        ("Publicar el texto con el teléfono y la dirección del autor.", "Son datos privados.", "Publica solo la información necesaria y sin datos personales."),
    ],
    [
        mc("Publicar (publish) es", "compartir la versión final con una audiencia", ["borrar el borrador", "traducir al español"], "Es el último paso del proceso."),
        mc("El corrector ortográfico (spell check) sirve para", "detectar palabras mal escritas", ["inventar ideas", "elegir el género"], "Subraya las palabras dudosas."),
        mc("Una lista con viñetas (bullet list) sirve para", "mostrar pasos o datos de forma ordenada", ["cambiar el idioma", "guardar el archivo"], "Ordena la información."),
    ],
    [
        mc(f"Entradas: {DIC_CROWD} {DIC_LIVELY} {DIC_SILENT} {GDIC} Completa: «The bus was very ___ at eight o'clock.»", "crowded", ["silent", "lively"], "Crowded describe un lugar con muchas personas, como un bus."),
        mc(f"Entradas: {DIC_CROWD} {DIC_LIVELY} {DIC_SILENT} {GDIC} Completa: «The library is ___, so please do not talk.»", "silent", ["crowded", "lively"], "Silent significa sin ningún sonido."),
        mc(f"Entradas: {DIC_CROWD} {DIC_LIVELY} {DIC_SILENT} {GDIC} ¿Qué clase de palabra son las tres?", "Adjetivos", ["Verbos", "Sustantivos"], "Las tres entradas dicen adjective."),
    ],
    [
        mc(f"Tarjetas: {CARD_A} {CARD_B} {GCARDS} {DIC_CROWD} {DIC_LIVELY} ¿Qué palabra completa el espacio (1)?", "crowded", ["silent", "lively"], "La nota (1) dice que había muchas personas en un espacio pequeño, que calza con crowded."),
        mc(f"Tarjetas: {CARD_A} {CARD_B} {GCARDS} {DIC_CROWD} {DIC_LIVELY} ¿Qué palabra completa el espacio (2)?", "lively", ["crowded", "silent"], "La nota (2) habla de energía que hacía moverse y sonreír."),
        mc(f"Tarjetas: {CARD_A} {CARD_B} Solo tienes la tarjeta con el borrador. ¿Qué pregunta haces para completar el espacio (1)?", "What does your note say about number 1?", ["Where is the music?", "Who is the teacher?"], "La información que falta está en la tarjeta B."),
    ],
    [
        mc("Tu corrector no subraya nada en «The bus was very silent at eight o'clock, full of people». Una persona dice que está bien. ¿Qué respondes?", "Está bien escrito, pero silent no calza con un bus lleno de gente; crowded sería mejor", ["Está perfecto porque no hay errores", "Hay que cambiar el verbo"], "El corrector no evalúa el significado."),
        mc("Dos opciones para publicar un cuento en el diario mural. Opción 1: título, tres párrafos y tu nombre y tu dirección. Opción 2: título, tres párrafos y tu nombre. ¿Cuál es mejor?", "La opción 2, porque no incluye datos privados", ["La opción 1, porque da más información", "Las dos son iguales"], "La dirección es un dato privado y no debe publicarse."),
    ],
    [
        mc(f"Tarjetas: {CARD_A} {CARD_B} Una compañera escribe: «The festival was very silent and the music was crowded.» ¿Por qué es incorrecto?", "Porque silent y crowded no calzan con las notas ni con las definiciones", ["Porque festival se escribe con f", "Porque falta el título"], "Las notas hablan de mucha gente y de energía."),
        mc(f"Tarjetas: {CARD_A} {CARD_B} ¿Cuál es la oración final correcta y bien unida con ambas tarjetas?", "The festival was very crowded and the music was lively.", ["The festival was very lively and the music was crowded.", "The festival was very silent and the music was lively."], "Crowded va con la gente y lively con la música que movía a todos."),
    ],
    [mc("Debes publicar en el diario mural del curso un texto sobre una visita a un museo. ¿Qué lista de comprobación es la mejor?", "Título, párrafos claros, ortografía revisada y sin datos privados", ["Sin título, un solo párrafo largo y con el teléfono del autor", "Muchos colores y ninguna revisión"], "Reúne presentación, revisión y privacidad.")],
    [
        mc("Un buen texto publicado debe tener", "título y presentación clara", ["datos privados"], "Presentar bien ayuda a la lectura."),
        mc("En un diccionario en línea, el ejemplo sirve para", "ver cómo se usa la palabra en una oración", ["traducir todo el texto"], "El ejemplo muestra el uso."),
        ("Escribe en inglés la palabra que significa «procesador de textos» (dos palabras).", "Word processor", "Word processor es el programa para escribir y dar formato."),
    ],
    task("Completa esta oración con las entradas del diccionario y copia la versión final en tu hoja con un título. Entradas: «cheerful (adjective): happy and positive.» «gloomy (adjective): dark and sad.» Oración: «On the rainy day, the room was ___, but the singer was ___.» Nota: the room was dark and sad; the singer was happy and smiled. (rainy = lluvioso; singer = cantante; smiled = sonrió)",
         "On the rainy day, the room was gloomy, but the singer was cheerful. Título: A Rainy Day at the Theater.",
         ["usa gloomy y cheerful en el lugar correcto", "agrega un título", "no incluye datos privados"],
         ["oración final con título en la hoja"],
         ["poner las palabras al revés", "no escribir título"],
         "Pide que explique con la definición por qué eligió cada palabra."),
    "Copia las siete palabras del vocabulario y escribe para qué sirven.",
    "Elige tres palabras en inglés que conozcas y escribe una definición en español y un ejemplo de cada una.",
)

# ============================================================ clase 5: proceso completo y escritura independiente
PENP = "«Hi Alex! My name is Sofía. I start school at 8:00 and I have lunch at 13:00. My favorite subject is science because we do experiments. What is your favorite subject? Write soon! Sofía»"
GPENP = "(pen pal = amigo por correspondencia; start = empiezo; lunch = almuerzo; favorite = favorita; experiments = experimentos; write soon = escribe pronto)"
BADMAIL = "«hi alex. i start school at 8 oclock. i like science. bye»"

lesson(
    OA, 5, MAT,
    "Aprenderé a recorrer todo el proceso de escritura (planear, redactar, revisar, editar y publicar) para un correo a un amigo por correspondencia, con un criterio de evaluación. Sirve para producir un texto completo por mi cuenta.",
    ["Sé planear, redactar, revisar y publicar un texto corto."],
    [
        "Para escribir un texto completo por tu cuenta, usa el proceso en orden. Primero planea: elige el género, el propósito y la audiencia, y anota las ideas en un esquema. Segundo, redacta un borrador sin preocuparte demasiado por los errores. Tercero, revisa el contenido con el criterio. Cuarto, edita ortografía, puntuación y gramática. Quinto, publica la versión final con buena presentación.",
        "El criterio para un correo informal a un amigo por correspondencia puede ser: un saludo (Hi Alex!), una presentación breve, tres datos sobre ti o tu día, una pregunta para el lector y una despedida con tu nombre. La pregunta final muestra interés y permite que el amigo responda. Para un destinatario que no conoces, no incluyas datos privados como dirección, teléfono o nombre del colegio.",
        "Después de escribir, compara el texto con el criterio punto por punto. Marca el saludo, cada dato, la pregunta y la despedida. Si falta uno, agrégalo. Si hay una oración que no sirve al propósito, quítala. Revisar contra un criterio es más seguro que corregir al azar.",
    ],
    [("pen pal", "amigo por correspondencia"), ("greeting", "saludo"), ("closing", "despedida"), ("question", "pregunta"), ("final version", "versión final"), ("criterion", "criterio"), ("private information", "datos privados")],
    [
        ("Comparar con un criterio", f"Texto: {PENP} {GPENP} Criterio: saludo, tres datos, una pregunta y despedida con nombre. ¿Cumple?",
         ["Saludo: Hi Alex!", "Datos: empieza a las 8:00, almuerza a las 13:00 y su materia favorita es ciencias.", "Pregunta: What is your favorite subject? Despedida con nombre: Sofía."], "Sí cumple: saludo, tres datos, pregunta y despedida con nombre"),
        ("Corregir un borrador", f"Borrador: {BADMAIL} (o'clock = en punto; bye = chao) ¿Qué falta para cumplir el criterio de la lección?",
         ["Tiene un saludo, pero sin mayúsculas ni coma.", "Tiene dos datos y falta uno, y falta la pregunta.", "Falta la despedida con el nombre."], "Faltan un dato, una pregunta, la despedida con nombre y la edición (mayúsculas y signos)"),
    ],
    [
        ("Incluir en el correo a un amigo por correspondencia la dirección de tu casa.", "Es un dato privado y no hace falta para el propósito.", "Escribe solo datos generales como tu materia favorita."),
        ("Corregir solo la ortografía y no comparar con el criterio.", "Se puede cumplir la ortografía y aun así faltar partes del texto.", "Revisa el criterio punto por punto."),
    ],
    [
        mc(f"Lee: {PENP} {GPENP} ¿Cuál es el saludo?", "Hi Alex!", ["Write soon!", "Sofía"], "El saludo abre el correo."),
        mc(f"Lee: {PENP} {GPENP} ¿Cuál es la pregunta para el lector?", "What is your favorite subject?", ["I have lunch at 13:00", "My name is Sofía"], "Es la única oración que le pide una respuesta."),
        mc(f"Lee: {PENP} {GPENP} ¿A qué hora empieza el colegio Sofía?", "At 8:00", ["At 13:00", "At 18:00"], "Dice I start school at 8:00."),
    ],
    [
        mc(f"Lee: {PENP} {GPENP} ¿Qué razón da Sofía para su materia favorita?", "Porque hacen experimentos", ["Porque termina temprano", "Porque tiene buenos amigos"], "Dice because we do experiments."),
        mc(f"Lee: {PENP} ¿Qué género es y cuál es su registro?", "Un correo informal a un amigo", ["Una biografía formal", "Un folleto"], "Saluda con Hi y habla de sí misma."),
        mc("Para un destinatario que no conoces, ¿qué dato NO debes incluir?", "Tu dirección", ["Tu materia favorita", "Una pregunta para el lector"], "La dirección es un dato privado."),
    ],
    [
        mc(f"Lee el borrador: {BADMAIL} ¿Cuál es la versión editada de la primera línea?", "Hi Alex! I start school at 8 o'clock.", ["hi alex. I start school at 8 o clock", "Hi alex I start school at 8 oclock"], "Corrige mayúsculas, signos y el apóstrofe de o'clock."),
        mc(f"Lee el borrador: {BADMAIL} ¿Qué pregunta natural podrías agregar al final?", "What time do you start school?", ["Where is your address?", "How much is your phone?"], "Mantiene el tema y no pide datos privados."),
        mc("Para el cierre de un correo a un amigo, ¿cuál es el más apropiado?", "Write soon! Sofía", ["Sincerely yours, Mr. President", "Bye bye bye bye"], "Es breve, cordial y con el nombre."),
    ],
    [
        mc(f"Un compañero dice que {PENP} está perfecto sin cambiar nada porque no tiene errores de ortografía. ¿Qué respondes?", "Que además hay que comparar con el criterio, y este texto sí cumple todos los puntos", ["Que está mal porque faltan más párrafos", "Que está mal porque no tiene dibujos"], "El texto cumple el criterio y no necesita cambios importantes."),
        mc("Dos borradores. Borrador 1 tiene saludo, tres datos, pregunta y despedida con nombre. Borrador 2 tiene saludo, dos datos y despedida. Criterio: saludo, tres datos, pregunta y despedida. ¿Cuál cumple?", "El borrador 1", ["El borrador 2", "Los dos"], "El borrador 2 no tiene tres datos ni pregunta."),
    ],
    [
        mc("Un correo informal tiene siete oraciones y la cuarta no tiene relación con el propósito: «I like blue cars.» (cars = autos). ¿Qué haces al revisar?", "La quito, porque no aporta al propósito", ["La dejo porque me gusta", "Elimino el saludo"], "Cada oración debe servir al propósito."),
        mc("Ya planeaste, redactaste y revisaste el contenido de tu correo. ¿Qué pasos te faltan?", "Editar la forma y publicar", ["Solo publicar", "Planear y redactar"], "Después de revisar el contenido se edita la forma y luego se publica."),
    ],
    [mc("Antes de publicar en la página del curso, revisas un texto con estas líneas: título, saludo, tres datos generales, una pregunta y una despedida con el nombre «Sofía». ¿Qué decides?", "Publicarlo, porque cumple el criterio y no incluye datos privados", ["No publicarlo, porque tiene nombre", "No publicarlo, porque tiene una pregunta"], "Un nombre de pila y datos generales son aceptables.")],
    [
        mc("¿Cuál es el último paso del proceso de escritura?", "Publicar", ["Planear"], "Publicar es compartir la versión final."),
        mc("¿Qué se compara punto por punto al revisar?", "El texto con el criterio", ["El texto con otro idioma"], "Así se detecta lo que falta."),
        ("Escribe en inglés la palabra para «saludo».", "Greeting", "Greeting es la frase con que se empieza un correo."),
    ],
    task("Eres Mateo y escribes un correo informal a Lucy, tu amiga por correspondencia. Usa estos datos: «I play the guitar on Mondays; I have a small dog; my favorite food is pizza.» (play = toco; small = pequeño; favorite food = comida favorita) Sigue el criterio: saludo, tres datos, una pregunta, despedida con tu nombre. Haz tu plan, tu borrador y la versión final en tu hoja.",
         "Hi Lucy! I play the guitar on Mondays. I have a small dog. My favorite food is pizza. What is your favorite food? Write soon! Mateo",
         ["incluye saludo, tres datos, pregunta y despedida con nombre", "usa los tres datos del enunciado", "corrige mayúsculas y puntuación"],
         ["plan, borrador y versión final en la hoja"],
         ["omitir la pregunta", "agregar datos privados"],
         "Pide que marque con colores el saludo, los datos, la pregunta y la despedida."),
    "Copia los siete términos y haz una lista de comprobación de cinco puntos para tus correos.",
    "Escribe un correo en inglés de cinco oraciones a un amigo imaginario de otro país, con saludo, tres datos, pregunta y despedida.",
)
