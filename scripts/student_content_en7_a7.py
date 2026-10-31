"""Cuaderno del estudiante, 7.º básico Inglés (propuesta), EN07 OA 07 (respuesta personal fundamentada a textos).

Todos los textos son originales y están escritos en el enunciado, con pista en español. Las respuestas abiertas (opiniones,
sentimientos) se evalúan con criterios; los ejercicios cerrados comprueban la forma y la fundamentación.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_en7_a import lesson

OA7 = "EN07 OA 07"

# ---------------------------------------------------------------- clase 1: hacer conexiones
MOON = "«The Moon does not make its own light. It reflects light from the Sun. The Moon takes about twenty-seven days to go around the Earth. Its shape seems to change: we see a new moon, a half moon and a full moon.» (reflects = refleja, shape = forma, seems = parece, new moon = luna nueva, half moon = media luna, full moon = luna llena)"
TEA = "«In England, many people have afternoon tea at about four o'clock: tea, sandwiches and cake. In Chile, we have once, a similar meal with tea, bread and spreads. Both are moments to rest and talk with other people.» (afternoon tea = té de la tarde, similar = parecida, spreads = untables, rest = descansar)"
LANES = "«More cities are building bike lanes. A bike lane is a part of the street only for bicycles. With bike lanes, cyclists are safer and the air is cleaner because there are fewer cars. Some students ride to school every day.» (lane = vía, cyclists = ciclistas, safer = más seguros, cleaner = más limpio, fewer = menos)"

lesson(
    OA7, 1,
    "Los textos breves escritos en cada ejercicio y lápiz.",
    "Aprenderé a hacer conexiones entre un texto y otras asignaturas, mi lengua materna y mi cultura, la vida cotidiana, mis experiencias y otras culturas, usando frases como I learned about… in… y I read about… when…. Sirve para dar una respuesta personal y fundamentada después de leer o escuchar.",
    ["Sé que el pasado simple se usa para contar lo que ya ocurrió.", "Conozco palabras como science, class y culture."],
    [
        "Hacer una conexión (connection) es relacionar lo que lees con algo que ya conoces. Puedes conectar con otra asignatura (science, maths, history), con tu lengua materna y tu cultura (el español y las costumbres de Chile), con la vida cotidiana (la calle, la casa, el colegio), con tus experiencias personales o con otras culturas. Una conexión explica por qué el texto te importa o te recuerda algo.",
        "En inglés, estas frases te ayudan: «I learned about… in science class» (Aprendí sobre… en la clase de ciencias); «I read about… when I was in fifth grade» (Leí sobre… cuando estaba en quinto); «This reminds me of…» (Esto me recuerda…); «In Chile, we…» (En Chile, nosotros…). Usa in con un lugar o una asignatura y when con un momento. Después de when, usa una oración completa: when I was eleven.",
        "Una buena conexión es específica y se apoya en el texto. No basta decir «I like it»: explica la relación. Por ejemplo: «The text about the Moon reminds me of science class, because I learned about the phases in fifth grade». Compara: «I like it» no dice nada del texto; en cambio, la frase sobre la Luna relaciona un dato concreto con una asignatura. La conexión específica demuestra que comprendiste.",
    ],
    [("connection", "conexión: relación con algo que conozco"), ("I learned about… in…", "Aprendí sobre… en…"), ("I read about… when…", "Leí sobre… cuando…"), ("This reminds me of…", "Esto me recuerda…"), ("daily life", "vida cotidiana"), ("culture", "cultura")],
    [
        ("Conexión con una asignatura", MOON + " ¿Qué conexión con ciencias puedes hacer? Completa: «We read about the Moon ___ science class.»", ["La asignatura es un lugar: se usa in.", "Queda in science class.", "La frase relaciona el texto con la clase."], "in"),
        ("Conexión con la cultura", TEA + " Escribe una conexión con Chile.", ["El texto compara England y Chile.", "Una conexión puede usar In Chile, we…", "Puedo decir que en Chile tomamos once."], "In Chile, we have once with tea and bread"),
    ],
    [
        ("Escribir «I learned about the Moon at science class» con at.", "Se confunde la preposición.", "Con una asignatura o un lugar amplio se usa in."),
        ("Decir una conexión que no se relaciona con el texto.", "No se explica el vínculo.", "Usa un dato concreto del texto."),
    ],
    [
        (MOON + " ¿Qué conexión es correcta? a) I learned about the Moon phases in science class b) I learned about the Moon phases in art class.", "a) I learned about the Moon phases in science class.", "Las fases de la Luna se aprenden en ciencias."),
        (TEA + " ¿Qué asignatura o tema relacionas? a) cultura y costumbres b) matemática", "a) cultura y costumbres", "El texto compara dos costumbres de alimentación."),
        (LANES + " ¿Qué conexión con la vida cotidiana es adecuada? a) I see bike lanes near my school b) I eat sandwiches at four o'clock.", "a) I see bike lanes near my school.", "Relaciona las ciclovías con la calle."),
    ],
    [
        (MOON + " Completa: «I read about the phases of the Moon ___ I was in fifth grade.» Elige when o in.", "when", "Después viene una oración completa: I was in fifth grade."),
        (TEA + " ¿Qué frase conecta con la lengua materna? a) In Spanish, we say «once» for the afternoon meal b) The sandwiches are delicious.", "a) In Spanish, we say «once» for the afternoon meal.", "Relaciona el texto con el español y la cultura."),
        (LANES + " Completa: «This ___ me of the lane near my house.» Elige reminds o remind.", "reminds", "This es singular: reminds."),
    ],
    [
        (MOON + " Quieres hacer una conexión con matemática. ¿Qué dato del texto sirve? a) twenty-seven days b) new moon", "a) twenty-seven days", "Es una cantidad que se puede usar en cálculos."),
        (LANES + " Un compañero dice: «I like it». ¿Es una buena conexión? Responde sí o no.", "No", "No explica la relación con el texto."),
        (TEA + " ¿Qué palabra del texto relaciona dos culturas? a) both b) bread", "a) both", "Both significa ambos y une las dos costumbres."),
    ],
    [
        (MOON + " Elige la conexión mejor fundamentada. a) The Moon reflects the Sun, and I learned in science class that it does not make light b) The Moon is nice.", "a) The Moon reflects the Sun, and I learned in science class that it does not make light.", "Usa un dato del texto y una asignatura."),
        (TEA + " ¿Cuál es una conexión con otra cultura? a) In England, they have afternoon tea b) I like cake.", "a) In England, they have afternoon tea.", "Menciona la costumbre de otro país."),
    ],
    [
        (MOON + " Si la Luna tarda 27 días en dar la vuelta y pasaron 54 días, ¿cuántas vueltas completó?", "2", "Se divide el tiempo total entre la duración de una vuelta.", "54//27"),
        (LANES + " En una calle hay 3 ciclovías y cada una tiene 4 ciclistas. ¿Cuántos ciclistas hay? Dato de ejemplo.", "12", "Se multiplica el número de ciclovías por los ciclistas de cada una.", "3*4"),
    ],
    [("Lees: «Many people eat soup when it is cold.» Tu compañera dice: «In Chile, we eat cazuela when it is cold». ¿Qué tipo de conexión hace? a) con la cultura b) con matemática", "a) con la cultura", "Relaciona el texto con una comida de Chile.")],
    [
        ("¿Qué frase sirve para conectar con una clase?", "I learned about… in…", "Relaciona el texto con una asignatura."),
        ("¿Qué frase sirve para decir que el texto te recuerda algo?", "This reminds me of…", "Introduce una conexión."),
        ("¿Qué se usa antes de una oración completa: in o when?", "when", "When introduce un momento."),
    ],
    task("Lee este texto original: «Bees are important for plants. When a bee visits a flower, it carries pollen to another flower. In many places, farmers keep bees to help the fruit trees. We need bees to have apples, pears and many other fruits.» (pollen = polen, farmers = agricultores, pears = peras, fruits = frutas). Escribe tres conexiones en inglés: una con ciencias, una con tu vida cotidiana y una con tu cultura. Usa I learned about… in… y In Chile, we….", "Ciencias: I learned about pollen in science class. Vida cotidiana: This reminds me of the apples I eat at lunch. Cultura: In Chile, we eat many fruits, such as apples and pears.", ["escribe tres conexiones de tres tipos", "usa un dato del texto en cada una", "usa las frases propuestas"], ["hoja con tres frases", "nota del adulto"], ["escribir solo «I like bees»", "no relacionar con el texto"], "Reconoce lo que acertó y ayuda a la persona a agregar un dato del texto en cada conexión."),
    "Relee el texto de las ciclovías y escribe en español una experiencia tuya con las bicicletas.",
    "Escribe una conexión entre el texto de la Luna y algo que viste en el cielo.",
)

# ---------------------------------------------------------------- clase 2: opiniones y sentimientos
SKATE = "«Jorge goes to the skate park on Saturdays. He likes skating because it is fun and he can meet friends. Last week, he fell and hurt his knee, so he felt a little afraid. But he tried again, and he was happy when he did a small jump.» (skate park = pista de skate, fell = se cayó, hurt = lastimó, knee = rodilla, tried = intentó, jump = salto)"
RULE = "«The school has a new rule: no phones in the classroom. Some students are angry because they use their phones to check the time. Other students are happy because they can concentrate better. The principal says that the rule helps everybody to learn.» (rule = regla, concentrate = concentrarse, principal = director, helps = ayuda)"
FILM = "«Last Friday, the class watched a film about a lost dog. At the end, the dog returned home. Some students cried, and others smiled. Marcela says: I think that the film is beautiful because it shows friendship. For example, the boy shares his food with the dog.» (film = película, lost = perdido, cried = lloraron, friendship = amistad, shares = comparte, food = comida)"

lesson(
    OA7, 2,
    "Los textos breves escritos en cada ejercicio y lápiz.",
    "Aprenderé a expresar mis opiniones y sentimientos y a justificarlos con because, I think that… y for example. Sirve para reaccionar a lo que leo o escucho con razones claras.",
    ["Sé que like significa gustar.", "Conozco los sentimientos happy, angry y afraid."],
    [
        "Una opinión (opinion) dice lo que piensas. Para expresarla se usa I think that… (Pienso que…) o I like… (Me gusta…). Un sentimiento (feeling) dice cómo te sientes: I'm feeling happy (me siento feliz), I'm feeling angry (me siento enojado/a), I'm feeling afraid (me siento asustado/a). Estas frases se usan tanto para hablar de ti como para reaccionar a un texto.",
        "Una opinión necesita una razón (reason). La palabra because (porque) introduce la razón: I like skating because it's fun. For example (por ejemplo) introduce un ejemplo concreto que apoya tu idea: I think the film is beautiful. For example, the boy shares his food with the dog. La estructura completa es: opinión + because + razón + for example + ejemplo.",
        "Para que tu justificación sea buena, la razón debe tener relación con la opinión y debe apoyarse en algo del texto. «I like the film because it is long» no explica por qué es bueno. «I like the film because it shows friendship» sí lo hace. Cuando expreses un sentimiento, explica también qué lo causó: I'm feeling afraid because the dog is lost.",
    ],
    [("I think that…", "Pienso que…"), ("I like… because…", "Me gusta… porque…"), ("I'm feeling happy / angry / afraid", "Me siento feliz / enojado / asustado"), ("because", "porque: introduce la razón"), ("for example", "por ejemplo"), ("reason", "razón")],
    [
        ("Opinión con razón", "Completa: «I like swimming ___ it is relaxing.» Elige because o but.", ["Necesito una razón.", "Because introduce la razón.", "Queda because."], "because"),
        ("Sentimiento", "Lee: «The dog is lost, and the boy cannot find it.» Escribe cómo te sientes con la frase I'm feeling…", ["Elijo un sentimiento posible: afraid o sad.", "Lo uno con I'm feeling.", "Explico la razón con because."], "I'm feeling afraid because the dog is lost"),
    ],
    [
        ("Dar una opinión sin razón: «I like the film».", "Falta la fundamentación.", "Agrega because y una razón del texto."),
        ("Usar la razón equivocada: «I like skating because it rains».", "La razón no tiene relación con la opinión.", "La razón debe explicar la opinión."),
    ],
    [
        (SKATE + " ¿Por qué le gusta patinar a Jorge? a) porque es divertido y puede ver amigos b) porque lo hace sentir miedo", "a) porque es divertido y puede ver amigos", "Dice because it is fun and he can meet friends."),
        (RULE + " ¿Por qué algunos estudiantes están enojados? a) porque usan el celular para ver la hora b) porque no hay recreo", "a) porque usan el celular para ver la hora", "Dice because they use their phones to check the time."),
        (FILM + " ¿Qué opina Marcela? a) que la película es hermosa b) que la película es corta", "a) que la película es hermosa", "Dice I think that the film is beautiful."),
    ],
    [
        (SKATE + " ¿Cómo se sintió Jorge después de caerse? a) un poco asustado b) muy enojado", "a) un poco asustado", "Dice he felt a little afraid."),
        (RULE + " ¿Por qué otros estudiantes están contentos?", "Porque pueden concentrarse mejor", "Dice because they can concentrate better."),
        (FILM + " ¿Qué ejemplo da Marcela para apoyar su opinión?", "El niño comparte su comida con el perro", "Dice for example, the boy shares his food with the dog."),
    ],
    [
        ("Elige la opinión mejor justificada sobre la película. a) I think the film is beautiful because it shows friendship b) I think the film is beautiful because it has dogs.", "a) I think the film is beautiful because it shows friendship.", "La razón de a explica el valor de la película."),
        ("Elige la frase que expresa un sentimiento. a) I'm feeling happy b) I think that it is Friday.", "a) I'm feeling happy.", "Expresa cómo se siente quien habla."),
        (RULE + " ¿Cuál es una opinión? a) The principal says the rule helps everybody to learn b) The rule is about phones.", "a) The principal says the rule helps everybody to learn.", "Expresa lo que piensa el director; la otra opción describe un hecho."),
    ],
    [
        (SKATE + " Completa: «Jorge was happy ___ he did a small jump.» Elige when o because of.", "when", "When introduce el momento en que ocurrió."),
        (RULE + " Un estudiante dice: «I'm feeling angry because I like phones». ¿Es una buena justificación? Responde sí o no.", "No", "No se relaciona con la regla ni con el texto."),
    ],
    [
        (SKATE + " Ordena la reacción en este orden: opinión, razón y ejemplo. A) For example, he did a small jump. B) I think Jorge is brave. C) He is brave because he tried again after his fall.", "B, C, A", "Primero la opinión, luego la razón y por último el ejemplo."),
        (FILM + " Si 12 estudiantes lloraron y 8 sonrieron, ¿cuántos reaccionaron en total? Dato de ejemplo.", "20", "Se suman los dos grupos.", "12+8"),
    ],
    [("Escuchas: «Our school plays soccer on Friday. I'm feeling happy because I love the game.» Tu compañero dice: «I'm feeling happy because I love the game». ¿Qué parte es la razón? a) because I love the game b) I'm feeling happy", "a) because I love the game", "Because introduce la razón.")],
    [
        ("Al fundamentar tu opinión sobre un texto, ¿qué palabra introduce la razón?", "because", "Because significa porque y da la razón."),
        ("Para reaccionar a un texto, ¿qué frase abre una opinión?", "I think that…", "I think that significa pienso que."),
        ("¿Qué frase introduce un ejemplo?", "For example", "For example significa por ejemplo."),
    ],
    task("Lee este texto original: «At recess, a group of students plants a small garden. Mario brings seeds, and Lía brings water. Some students laugh at the idea, but after a month, they see green leaves. The teacher says: Now everybody wants to help!» (recess = recreo, garden = huerto, seeds = semillas, laugh at = reírse de, leaves = hojas). Escribe una opinión con I think that…, un sentimiento con I'm feeling… y una razón con because y un ejemplo con For example.", "I think that the garden is a good idea because it helps the school. For example, now everybody wants to help. I'm feeling happy because the plants grow.", ["escribe una opinión con razón", "escribe un sentimiento", "usa for example con un dato del texto"], ["hoja con tres frases"], ["escribir una razón sin relación", "olvidar for example"], "Reconoce lo que acertó y revisa con la persona que la razón explique la opinión."),
    "Relee el texto de la regla de los celulares y escribe tu opinión con because en español.",
    "Escribe en inglés cómo te sientes hoy con una razón.",
)

# ---------------------------------------------------------------- clase 3: resumir y sintetizar
LIGHT = "«The lighthouse of the town is very old. It was built in 1890 to help ships. Every night, a keeper turned on the big lamp at the top. Today, the lamp is automatic, and visitors can climb the 120 steps to see the sea. The lighthouse is now a small museum.» (lighthouse = faro, built = construido, ships = barcos, keeper = guardián, lamp = lámpara, automatic = automática, steps = escalones)"
BIKE = "«Daniela repaired her bike last weekend. First, she changed the flat tire. Then she cleaned the chain and put oil on it. Finally, she checked the brakes. She says the bike works better now, and she saves money because she does not need a new one.» (repaired = reparó, flat tire = neumático desinflado, chain = cadena, oil = aceite, brakes = frenos, saves = ahorra)"
FOOD = "«In Peru, potatoes grow in the mountains. There are thousands of kinds: red, yellow, purple and white. People cook them in many ways: boiled, baked or fried. Potatoes are important because they give energy and are cheap.» (potatoes = papas, mountains = montañas, kinds = tipos, purple = morado, boiled = hervidas, baked = al horno, fried = fritas, cheap = baratas)"

lesson(
    OA7, 3,
    "Los textos y esquemas escritos en cada ejercicio y lápiz.",
    "Aprenderé a resumir y sintetizar un texto con apoyo de un esquema de preguntas (who, what, where, when, why) y a escribir un resumen breve en inglés. Sirve para reaccionar a un texto mostrando que lo comprendí.",
    ["Sé responder preguntas con who, what y where.", "Conozco conectores como first, then y because."],
    [
        "Un resumen (summary) cuenta las ideas más importantes de un texto con pocas palabras y sin opiniones. Resumir no es copiar: eliges lo esencial y lo dices con tus palabras. Sintetizar (synthesize) es unir ideas de un texto en una idea más general. Por ejemplo, de tres detalles del faro puedes sintetizar: «El faro antiguo ahora es un museo».",
        "Un esquema (outline) te ayuda a resumir. Se compone de preguntas: Who? (¿quién?), What? (¿qué?), Where? (¿dónde?), When? (¿cuándo?), Why? (¿por qué?). Escribe una palabra clave para cada una. Después, une las respuestas en dos o tres oraciones con conectores: first, then, finally, because. Una buena regla es que el resumen sea más corto que el texto.",
        "Revisa tu resumen con tres preguntas: ¿incluí la idea principal?, ¿agregué algo que el texto no dice? y ¿es más corto que el texto? Evita los detalles menores, como las cifras exactas, a menos que sean la idea central. Con un buen resumen, otra persona entiende el texto sin leerlo.",
    ],
    [("summary", "resumen: ideas más importantes"), ("synthesize", "sintetizar: unir ideas en una idea general"), ("outline", "esquema de preguntas"), ("main idea", "idea principal"), ("detail", "detalle"), ("key words", "palabras clave")],
    [
        ("Esquema who-what-where", "Lee: «On Sunday, Rita and Pedro cleaned the beach.» (cleaned = limpiaron, beach = playa). Completa el esquema: Who? What? Where? When?", ["Who: Rita y Pedro.", "What: limpiaron.", "Where: la playa. When: el domingo."], "Who: Rita y Pedro. What: limpiaron. Where: la playa. When: el domingo"),
        ("Idea general", "Lee: «The library opens at eight. It has three floors. Students read, study and use computers there.» (floors = pisos). ¿Qué idea general sintetiza el texto?", ["Los tres datos hablan de la biblioteca.", "Se une lo que hacen los estudiantes.", "La idea es que la biblioteca sirve para estudiar."], "La biblioteca es un lugar para leer y estudiar"),
    ],
    [
        ("Copiar frases enteras del texto.", "No se resume con palabras propias.", "Elige palabras clave y une las ideas."),
        ("Agregar una opinión al resumen.", "Un resumen informa, no opina.", "Cuenta solo lo que dice el texto."),
    ],
    [
        (LIGHT + " ¿Qué es el faro hoy? a) un pequeño museo b) una casa privada", "a) un pequeño museo", "Dice The lighthouse is now a small museum."),
        (BIKE + " ¿Quién repara la bicicleta? a) Daniela b) su amiga", "a) Daniela", "Dice Daniela repaired her bike."),
        (FOOD + " ¿Dónde crecen las papas según el texto? a) en las montañas b) en el desierto", "a) en las montañas", "Dice potatoes grow in the mountains."),
    ],
    [
        (LIGHT + " Completa el esquema: When? ¿Cuándo se construyó el faro?", "En 1890", "Dice it was built in 1890."),
        (BIKE + " Completa el esquema: What? ¿Qué cosas hizo Daniela en la bicicleta? Menciona el primer paso.", "Cambió el neumático desinflado", "Dice First, she changed the flat tire."),
        (FOOD + " Completa el esquema: Why? ¿Por qué son importantes las papas?", "Porque dan energía y son baratas", "Dice because they give energy and are cheap."),
    ],
    [
        (LIGHT + " ¿Cuál es el mejor resumen? a) El faro antiguo ayudó a los barcos y hoy es un museo que se puede visitar b) El faro tiene 120 escalones.", "a) El faro antiguo ayudó a los barcos y hoy es un museo que se puede visitar.", "Incluye la idea principal; la otra solo da un detalle."),
        (BIKE + " ¿Cuál es el mejor resumen? a) Daniela reparó su bicicleta y ahorra dinero b) Daniela compró una bicicleta nueva.", "a) Daniela reparó su bicicleta y ahorra dinero.", "Es lo que dice el texto."),
        (FOOD + " ¿Cuál es el mejor resumen? a) En Perú hay muchas papas de colores que sirven de alimento b) Las papas se comen solo fritas.", "a) En Perú hay muchas papas de colores que sirven de alimento.", "Resume el tema; la otra opción contradice el texto."),
    ],
    [
        (LIGHT + " ¿Qué detalle sobra en un resumen breve? a) la cantidad de escalones b) que ahora es museo", "a) la cantidad de escalones", "Es un detalle menor."),
        (BIKE + " Ordena los pasos para el resumen. A) Revisó los frenos. B) Cambió el neumático. C) Limpió la cadena.", "B, C, A", "Siguen first, then y finally."),
    ],
    [
        (FOOD + " Un resumen dice: «Las papas de Perú son caras». ¿Qué error tiene? a) dice que son caras b) dice que son de Perú", "a) dice que son caras", "El texto dice que son cheap."),
        (LIGHT + " Si 4 visitantes suben 120 escalones cada uno, ¿cuántos escalones suben en total?", "480", "Cada visitante sube ciento veinte escalones.", "4*120"),
    ],
    [("Lee: «The students collected 30 kilos of paper in a week. Then they sold it and bought books.» (collected = juntaron, sold = vendieron). ¿Cuál es el mejor resumen? a) Reciclaron papel y compraron libros b) Compraron papel y vendieron libros", "a) Reciclaron papel y compraron libros", "Resume lo que hicieron.")],
    [
        ("¿Qué incluye el esquema de resumen?", "Who, what, where, when y why", "Son las preguntas básicas."),
        ("¿Un resumen debe ser más largo o más corto que el texto?", "Más corto", "Solo contiene lo esencial."),
        ("¿Se agregan opiniones en un resumen?", "No", "Solo se cuentan ideas del texto."),
    ],
    task("Lee este texto original: «The School Orchestra. The orchestra has twenty students. They practice on Tuesdays and Thursdays at four o'clock in the music room. In June, the orchestra plays at the town festival, so they practice a lot. Some students play the violin, and others play the flute. They are nervous but excited.» (orchestra = orquesta, practice = ensayan, festival = festival, violin = violín, flute = flauta, nervous = nerviosos, excited = emocionados). Haz un esquema Who–What–Where–When–Why y luego escribe un resumen de dos oraciones.", "Who: veinte estudiantes. What: ensayan y tocan. Where: sala de música y festival. When: martes y jueves, y en junio. Why: para tocar en el festival. Resumen: La orquesta ensaya dos veces por semana para tocar en el festival en junio. Los estudiantes están nerviosos pero emocionados.", ["completa el esquema con datos correctos", "escribe un resumen de dos oraciones", "no agrega datos que el texto no dice"], ["esquema y resumen"], ["copiar el texto completo", "agregar opiniones"], "Reconoce lo que acertó y ayuda a la persona a tachar los detalles menores."),
    "Relee el texto de la bicicleta y resume en una oración con first, then y finally.",
    "Resume en español, en dos líneas, un capítulo de un libro que hayas leído.",
)

# ---------------------------------------------------------------- clase 4: generar preguntas
CLUB = "«Every Tuesday, Sofía goes to the chess club. She plays with Mateo, and she usually wins. Last Tuesday, she lost the game because she was tired. Mateo smiled and said: Good game! After the match, they ate a sandwich.» (usually wins = por lo general gana, lost = perdió, tired = cansada, match = partida, ate = comieron)"
HERO = "«Miguel is a firefighter. He works at the fire station in the center of the city. He wakes up at five o'clock, and he checks the equipment. Yesterday, he helped a family leave a smoky house. He does his job because he wants to protect people.» (firefighter = bombero, equipment = equipo, smoky = con humo, protect = proteger)"
GAME2 = "«The school football team trains three times a week. The coach, Mrs. Soto, teaches the players new passes. Last Saturday, the team played against another school and won two to one. The players celebrated, and the coach gave everybody a bottle of water.» (trains = entrena, passes = pases, won = ganó, celebrated = celebraron)"

lesson(
    OA7, 4,
    "Los textos breves escritos en cada ejercicio y lápiz.",
    "Aprenderé a generar preguntas sobre un texto con why do/does…, do/does… y did… Sirve para dar una respuesta personal al texto y para investigar más sobre lo que leí.",
    ["Sé que do y does se usan en presente, y did en pasado.", "Conozco las palabras de pregunta who, what, where y why."],
    [
        "Hacer preguntas es una forma de reaccionar a un texto y de comprenderlo mejor. Para preguntar sobre rutinas y hechos habituales se usa do o does + sujeto + verbo en forma base: Does Sofía play chess? (¿Sofía juega ajedrez?), Do they train on Tuesdays? (¿entrenan los martes?). Does se usa con he, she e it; do, con I, you, we y they.",
        "Para preguntar por el motivo se usa why: Why does Miguel work at the fire station? (¿por qué trabaja Miguel en el cuartel?). Se responde con because. Para preguntar sobre el pasado se usa did + sujeto + verbo en forma base: Did Sofía win the game? (¿ganó Sofía?). La respuesta corta es Yes, she did o No, she didn't. Después de did y does el verbo va sin -s y sin -ed.",
        "Una buena pregunta tiene respuesta en el texto o te hace pensar más allá. Hay preguntas cerradas (responden sí o no) y abiertas (responden con información). Revisa el orden: palabra de pregunta + do/does/did + sujeto + verbo. Si falta el auxiliar, la pregunta queda mal: «Where Sofía plays?» es incorrecta; lo correcto es «Where does Sofía play?».",
    ],
    [("do / does", "auxiliares para preguntar en presente"), ("did", "auxiliar para preguntar en pasado"), ("why", "por qué"), ("because", "porque: respuesta a why"), ("Yes, she does / did", "respuesta corta afirmativa"), ("No, she doesn't / didn't", "respuesta corta negativa")],
    [
        ("Pregunta en presente", "Convierte en pregunta: «Mateo plays chess.»", ["Con Mateo uso does.", "Después de does el verbo va sin -s.", "Queda Does Mateo play chess?"], "Does Mateo play chess?"),
        ("Pregunta en pasado", "Convierte en pregunta: «Sofía lost the game.»", ["Uso did.", "El verbo vuelve a la forma base: lose.", "Queda Did Sofía lose the game?"], "Did Sofía lose the game?"),
    ],
    [
        ("Escribir «Does she plays?».", "Se conjuga el verbo después de does.", "Después de does el verbo va en forma base: Does she play?"),
        ("Escribir «Why Miguel works there?».", "Falta el auxiliar.", "Why does Miguel work there?"),
    ],
    [
        (CLUB + " Elige la pregunta correcta. a) «Does Sofía play chess?» b) «Do Sofía play chess?»", "a) Does Sofía play chess?", "Con Sofía (she) se usa does."),
        (HERO + " Elige la pregunta correcta. a) «Where does Miguel work?» b) «Where Miguel works?»", "a) Where does Miguel work?", "Falta el auxiliar en b."),
        (GAME2 + " Elige la pregunta correcta. a) «Did the team win?» b) «Did the team won?»", "a) Did the team win?", "Después de did el verbo va en forma base."),
    ],
    [
        (CLUB + " Responde: Does Sofía usually win? a) Yes, she does b) No, she doesn't.", "a) Yes, she does.", "Dice she usually wins."),
        (HERO + " Responde: Why does Miguel do his job?", "Porque quiere proteger a las personas", "Dice because he wants to protect people."),
        (GAME2 + " Responde: Did the team win last Saturday? a) Yes, it did b) No, it didn't.", "a) Yes, it did.", "Dice won two to one."),
    ],
    [
        (CLUB + " ¿Qué pregunta tiene su respuesta en el texto? a) «Why did Sofía lose the game?» b) «What is Mateo's favorite color?»", "a) Why did Sofía lose the game?", "El texto dice because she was tired."),
        (HERO + " Escribe la pregunta cuya respuesta es «At five o'clock». a) «What time does Miguel wake up?» b) «Where does Miguel work?»", "a) What time does Miguel wake up?", "El texto dice he wakes up at five o'clock."),
        (GAME2 + " ¿Qué pregunta se responde con «Mrs. Soto»? a) «Who is the coach?» b) «What is the score?»", "a) Who is the coach?", "Dice The coach, Mrs. Soto."),
    ],
    [
        (CLUB + " Completa: «___ Sofía eat a sandwich after the match?» Elige Did o Does.", "Did", "After the match está en pasado."),
        (HERO + " Completa: «Why ___ Miguel check the equipment?» Elige does o do.", "does", "Miguel es he y está en presente."),
    ],
    [
        (GAME2 + " ¿Cuál es una pregunta abierta, que no se responde con sí o no? a) «What does the coach teach?» b) «Does the team train?»", "a) What does the coach teach?", "Se responde con información: new passes."),
        (CLUB + " ¿Cuál es una pregunta cerrada? a) «Did Mateo smile?» b) «Why did Mateo smile?»", "a) Did Mateo smile?", "Se responde con sí o no."),
    ],
    [("Escuchas: «Yesterday, Ana visited a museum.» Quieres saber qué vio. ¿Qué pregunta haces? a) «What did Ana see?» b) «What Ana saw?»", "a) What did Ana see?", "En pasado se usa did más el verbo en forma base.")],
    [
        ("Para hacer una pregunta sobre un texto en pasado, ¿qué auxiliar usas?", "did", "Va antes del sujeto."),
        ("¿Con qué sujetos se usa does?", "He, she e it", "Es la tercera persona singular."),
        ("¿Qué palabra introduce la respuesta a why?", "because", "Da la razón."),
    ],
    task("Lee este texto original: «Tomás works at a bakery. He wakes up at four o'clock and makes the bread. Yesterday, he baked 50 loaves. He likes his job because the smell of fresh bread makes him happy.» (bakery = panadería, baked = horneó, loaves = panes, smell = olor). Escribe tres preguntas en inglés: una con does, una con did y una con why. Después escribe la respuesta de cada una.", "Does Tomás work at a bakery? Yes, he does. Did he bake 50 loaves yesterday? Yes, he did. Why does he like his job? Because the smell of fresh bread makes him happy.", ["escribe tres preguntas con la estructura correcta", "cada pregunta tiene su respuesta en el texto", "usa verbo en forma base después de does y did"], ["hoja con tres preguntas y respuestas"], ["escribir «Did he baked»", "olvidar el auxiliar"], "Reconoce lo que acertó y revisa con la persona el verbo después de does y did."),
    "Relee el texto del bombero y escribe en español dos preguntas que te gustaría hacerle.",
    "Escribe cinco preguntas en inglés para entrevistar a una persona de tu casa sobre su trabajo.",
)

# ---------------------------------------------------------------- clase 5: dramatizar y componer
MARKET = "Diálogo base para dramatizar. Vendedor: «Good morning! Can I help you?» Cliente: «Yes, please. I'm looking for some apples.» Vendedor: «We have red and green apples. Which do you like?» Cliente: «I prefer red apples because they are sweet. How much are they?» Vendedor: «They cost two thousand pesos per kilo.» (looking for = buscando, prefer = prefiero, sweet = dulces, cost = cuestan, per kilo = por kilo)"
LETTER = "Texto base: «Dear Ana, yesterday I visited a farm. I saw cows, sheep and chickens. I fed a baby sheep with a bottle. I think that farms are important because they give us food. For example, we get milk and eggs. I am feeling happy about my day. See you soon, Pablo.» (farm = granja, cows = vacas, sheep = ovejas, chickens = gallinas, fed = alimenté, bottle = mamadera, get = obtenemos, eggs = huevos)"
POSTER2 = "Afiche base: «Save water! Why? Because water is precious. For example, if you close the tap while you brush your teeth, you save water. I think that everybody can help. I feel worried when I see a running tap.» (save = ahorrar, precious = valiosa, tap = llave de agua, brush = cepillar, worried = preocupado, running = abierta)"

lesson(
    OA7, 5,
    "Los diálogos y textos base escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a reaccionar a un texto con una dramatización, una composición o un afiche, usando conexiones, opiniones con because, sentimientos y preguntas. Sirve para mostrar lo que comprendí de forma creativa y personal.",
    ["Sé expresar una opinión con I think that…", "Conozco las preguntas con do, does y did."],
    [
        "Hay varias formas de reaccionar a un texto: una dramatización (role play), en que dos o más personas actúan un diálogo; una composición (composition), que es un texto escrito con tus ideas; un resumen o un afiche con un mensaje. En todas, el contenido debe estar relacionado con el texto y usar lo que aprendiste: conexiones, opiniones con because, sentimientos y preguntas.",
        "Para dramatizar, define los personajes, el lugar y el propósito. Cada hablante usa frases cortas y claras: Can I help you? I prefer red apples because they are sweet. Pregunta y responde como en la vida real. Para componer, organiza: una idea principal (por ejemplo, farms are important), una razón con because y un ejemplo con for example. Termina con un sentimiento o una pregunta.",
        "Antes de entregar, revisa tu trabajo con una lista: ¿se entiende?, ¿tiene opinión y razón?, ¿tiene un ejemplo?, ¿corrijo mayúsculas y puntos? Si dramatizas, ensaya dos veces. Si escribes, lee en voz alta para detectar errores. Una buena reacción es personal pero se apoya en el texto.",
    ],
    [("role play", "dramatización: actuar un diálogo"), ("composition", "composición escrita"), ("because", "porque"), ("for example", "por ejemplo"), ("I feel / I am feeling", "me siento"), ("checklist", "lista de revisión")],
    [
        ("Ordenar un diálogo", "Ordena las líneas: A) «They cost two thousand pesos.» B) «How much are the apples?» C) «Good morning!»", ["El saludo va primero.", "Luego viene la pregunta.", "Después, la respuesta."], "C, B, A"),
        ("Revisar una composición", "Una composición dice: «I think farms are important. For example, they give us milk.» ¿Qué le falta? a) la razón con because b) un título", ["Hay opinión.", "El dato de la leche es un ejemplo.", "Falta because."], "a) la razón con because"),
    ],
    [
        ("Dramatizar leyendo una lista de frases sin escuchar al compañero.", "No se responde a lo que dice el otro.", "Escucha y responde al interlocutor."),
        ("Escribir una opinión sin ejemplo.", "No se fundamenta con un dato.", "Agrega for example con un ejemplo del texto."),
    ],
    [
        (MARKET + " ¿Qué manzanas prefiere el cliente? a) rojas b) verdes", "a) rojas", "Dice I prefer red apples."),
        (LETTER + " ¿Qué visitó Pablo? a) una granja b) un museo", "a) una granja", "Dice yesterday I visited a farm."),
        (POSTER2 + " ¿Qué mensaje principal tiene el afiche? a) ahorrar agua b) ahorrar electricidad", "a) ahorrar agua", "Dice Save water!"),
    ],
    [
        (MARKET + " ¿Cuánto cuestan las manzanas por kilo?", "$2.000", "Dice two thousand pesos per kilo."),
        (LETTER + " ¿Qué animales vio Pablo?", "Vacas, ovejas y gallinas", "Dice cows, sheep and chickens."),
        (POSTER2 + " ¿Qué se debe hacer mientras uno se cepilla los dientes?", "Cerrar la llave", "Dice close the tap while you brush your teeth."),
    ],
    [
        (MARKET + " Completa el diálogo con una frase de ayuda: «Vendedor: Good morning! ___» a) «Can I help you?» b) «See you soon.»", "a) Can I help you?", "Es la frase de saludo de un vendedor."),
        (LETTER + " ¿Qué justificación da Pablo para decir que las granjas son importantes? a) because they give us food b) because they are big", "a) because they give us food", "Dice because they give us food."),
        (POSTER2 + " ¿Qué sentimiento expresa el afiche? a) preocupación b) alegría", "a) preocupación", "Dice I feel worried."),
    ],
    [
        (LETTER + " ¿Qué ejemplo usa Pablo? a) la leche y los huevos b) los autos y los trenes", "a) la leche y los huevos", "Dice for example, we get milk and eggs."),
        (POSTER2 + " Un compañero dice que el afiche solo tiene hechos. ¿Tiene razón? Responde sí o no.", "No", "Tiene opiniones y sentimientos: I think that y I feel worried."),
    ],
    [
        (MARKET + " Si el cliente compra 3 kilos, ¿cuánto paga en pesos?", "$6.000", "Cada kilo cuesta dos mil pesos.", "3*2000"),
        (LETTER + " Pablo vio 8 ovejas y 5 gallinas. ¿Cuántos animales son en total? Dato de ejemplo.", "13", "Se suman ovejas y gallinas.", "8+5"),
    ],
    [("Quieres dramatizar una escena en una panadería. ¿Cuál es la primera línea adecuada? a) Good morning! I would like some bread, please b) I think farms are important.", "a) Good morning! I would like some bread, please.", "Es un saludo y una petición propios de una panadería.")],
    [
        ("Para reaccionar a un texto, ¿qué es un role play?", "Actuar un diálogo", "Los hablantes usan frases como en la vida real."),
        ("¿Qué estructura tiene una buena opinión escrita?", "Opinión, because, razón y ejemplo", "Así se fundamenta."),
        ("Antes de entregar tu reacción escrita, ¿qué revisas?", "Que se entienda y esté fundamentado", "Se corrigen errores."),
    ],
    task("Lee este texto original: «Parks are green places in the city. People walk, run and play there. In summer, many families have picnics under the trees. Parks are cleaner when everybody puts the trash in the bins.» (parks = parques, picnics = picnics, trash = basura, bins = basureros). Escribe una composición de cuatro frases en inglés con: una opinión con I think that…, una razón con because, un ejemplo con For example y un sentimiento con I feel….", "I think that parks are important because they are green places. For example, families have picnics there. I feel happy when the park is clean.", ["escribe las cuatro frases pedidas", "la razón se relaciona con la opinión", "usa un dato del texto como ejemplo"], ["hoja con la composición"], ["omitir el ejemplo", "usar una razón sin relación"], "Reconoce lo que acertó y revisa con la persona la lista de revisión de la clase."),
    "Dramatiza el diálogo del mercado con una persona de tu casa y cambia la fruta.",
    "Diseña un afiche en inglés con un título, una opinión con because y un dibujo.",
)
