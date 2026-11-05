"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 05: presentación oral coherente con recursos multimodales.

El estudiante analiza guiones y diapositivas descritas en el enunciado y prepara una presentación breve con un adulto como
audiencia. Temas originales y seguros (fases de la Luna, saludos en el mundo, contaminación lumínica). Inglés americano.
Los títulos de clase del plan son genéricos; aquí se aplican a organización de ideas, recursos multimodales, funciones del
lenguaje y vocabulario, sonidos y voz, y audiencia, contexto y propósito.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 05"

# ------------------------------------------------------------------ clase 1: contenido y organización coherente
PI = "«Good morning. Today I will talk about the phases of the Moon. First, I will explain what a phase is. Then I will show the four main phases. Finally, I will tell you how long the cycle lasts.» (phases = fases, explain = explicar, main = principales, cycle = ciclo, lasts = dura)"
PB = "«The first main phase is the new moon: we cannot see the Moon. The second is the first quarter: we see half of it. The third is the full moon: we see all of it. The fourth is the last quarter: we see half of it again.» (new moon = luna nueva, quarter = cuarto, full moon = luna llena, half = la mitad)"
PC = "«To sum up, the Moon changes its shape because we see different parts of its lit side. The cycle lasts about twenty-nine days. Thank you for listening. Do you have any questions?» (to sum up = en resumen, shape = forma, lit = iluminado, side = lado, questions = preguntas)"
GI = "«Hello, everyone. My topic is greetings around the world. I will talk about three ways to say hello: a handshake, a bow and a kiss on the cheek. Let's start with the handshake.» (greetings = saludos, handshake = apretón de manos, bow = reverencia, kiss on the cheek = beso en la mejilla)"
GB = "«A handshake is common in many countries, especially at work. A bow is a way of greeting where you bend your body forward. For example, people do it in some Asian countries. In Chile, friends often greet with a kiss on the cheek. My cousin has a green dog.» (especially = sobre todo, bend = inclinas, forward = hacia adelante, Asian = asiáticos, friends = amigos)"

lesson(
    OA, 1, MAT_R,
    "Aprenderé a organizar una presentación oral en introducción, desarrollo y cierre, con ideas conectadas y un plan claro. Sirve para que la audiencia siga tu presentación y entienda lo importante.",
    ["Sé escribir ideas con first, then y finally.", "Sé distinguir la idea principal de los detalles."],
    [
        "Una presentación oral coherente tiene tres partes. La introducción (introduction) saluda, dice el tema y anuncia el plan: Today I will talk about... First, I will... Then... Finally... El desarrollo (body) presenta cada punto con una idea principal y un ejemplo. El cierre (conclusion) resume con To sum up, agradece con Thank you for listening y pregunta Do you have any questions?",
        "La coherencia (coherence) significa que todas las ideas se relacionan con el tema y siguen un orden. Usa palabras de secuencia: first, second, third, next, finally. Usa palabras para dar ejemplos: for example. Si una oración no se relaciona con el tema, como My cousin has a green dog en una presentación de saludos, se elimina.",
        "Para preparar tu presentación, haz un esquema: tema, tres puntos, un ejemplo por punto y una frase de cierre. Practica diciendo cada parte en voz alta. Si puedes explicar tu esquema en un minuto, tu presentación está organizada.",
    ],
    [("introduction", "introducción: saluda, dice el tema y el plan"), ("body", "desarrollo: puntos y ejemplos"), ("conclusion", "cierre: resumen y agradecimiento"), ("to sum up", "en resumen"), ("for example", "por ejemplo"), ("coherence", "coherencia: ideas ordenadas y relacionadas")],
    [
        ("Reconocer la introducción", PI + " ¿Qué dice el hablante en la primera oración, en la segunda y en las últimas?", ["Good morning es un saludo.", "Today I will talk about... dice el tema.", "First, Then y Finally anuncian el plan."], "Saluda, dice el tema y anuncia el plan"),
        ("Quitar lo que no pertenece", GB + " ¿Qué oración no pertenece a la presentación y por qué?", ["El tema son los saludos del mundo.", "Casi todas las oraciones hablan de saludos.", "My cousin has a green dog no se relaciona con el tema: se elimina."], "My cousin has a green dog, porque no habla de saludos"),
    ],
    [
        ("Empezar con el desarrollo sin decir el tema.", "La audiencia no sabe de qué hablarás ni qué viene.", "Comienza con saludo, tema y plan."),
        ("Agregar datos que no se relacionan con el tema.", "Rompen la coherencia y distraen.", "Revisa cada oración: ¿ayuda al tema?"),
    ],
    [
        mr(PC, "¿Qué parte de una presentación es este texto?", "El cierre", ["La introducción", "El desarrollo"], "Dice To sum up y Thank you for listening."),
        mr(PI, "¿Qué palabra anuncia el último punto del plan?", "Finally", ["First", "Then"], "Finally introduce el último punto."),
        mc("¿Qué frase pertenece a una introducción?", "Today I will talk about...", ["Thank you for listening", "To sum up the main ideas"], "Las otras dos son frases de cierre."),
    ],
    [
        mr(PB, "¿Qué palabras de secuencia organizan este desarrollo?", "first, second, third y fourth", ["because, so y but", "always, often y never"], "The first, the second, the third y the fourth ordenan las fases."),
        mc("¿Para qué sirve la frase for example en una presentación?", "Para dar un caso que aclara una idea", ["Para despedirse", "Para cambiar de tema"], "Introduce un ejemplo."),
        mr(GI, "¿Qué tres ideas anuncia el hablante?", "Tres saludos: apretón, reverencia y beso", ["Tres comidas típicas para recibir visitas", "Tres países donde viven sus primos y amigos"], "Dice three ways to say hello."),
    ],
    [
        mr(PC, "¿Qué dato resume el ciclo completo de la Luna?", "Dura unos veintinueve días", ["Dura una semana", "Dura un mes de treinta y cinco días"], "Dice The cycle lasts about twenty-nine days."),
        mc("Tienes que ordenar las partes de una presentación. ¿Cuál es el orden correcto?", "Introducción, desarrollo y cierre", ["Cierre, introducción y desarrollo", "Desarrollo, cierre e introducción"], "La estructura lógica va de presentar a cerrar."),
        mr(GB, "¿Qué ejemplo se da de saludo con reverencia?", "Algunos países de Asia", ["Chile", "Todos los lugares de trabajo"], "Dice people do it in some Asian countries."),
    ],
    [
        mc("Un estudiante empieza así: «Phases. The Moon. Thank you.» ¿Qué le falta?", "Una introducción completa con saludo, tema y plan, y un desarrollo", ["Más palabras sueltas", "Solo cambiar la voz"], "Presentar sin plan ni desarrollo deja la audiencia sin guía."),
        mr(PB, "Un compañero propone agregar al desarrollo: «The Moon is a good place for a picnic». ¿Qué opinas?", "Debe eliminarse: no explica las fases", ["Debe quedar porque hace reír", "Debe ir al principio"], "No se relaciona con el tema del desarrollo."),
    ],
    [
        mr(PI + " " + PC, "¿Qué anuncio de la introducción se cumple en el cierre?", "Que se dirá cuánto dura el ciclo", ["Que se mostrarán fotos", "Que se dará un ejemplo de cada fase"], "Finally, I will tell you how long the cycle lasts se cumple con about twenty-nine days."),
        arith("Una presentación dura 6 minutos. La introducción usa 1 minuto, el cierre usa 1 minuto y el resto se reparte en 4 puntos iguales. ¿Cuántos minutos dedica a cada punto?", "(6-1-1)//4", "Se restan introducción y cierre y se reparte el tiempo restante en cuatro.", " minuto"),
    ],
    [mr(GI + " " + GB, "Escribe la oración que sobra y qué idea del plan cumple la oración sobre Chile.", "My cousin has a green dog; la de Chile ilustra el beso en la mejilla", ["The handshake; la de Chile ilustra la reverencia", "A bow; la de Chile ilustra el apretón de manos"], "Solo la oración del primo no pertenece; la de Chile da un ejemplo del tercer saludo.")],
    [
        ("En Inglés de 2.º medio (OA 5, clase 1): ¿cuáles son las tres partes de una presentación?", "Introducción, desarrollo y cierre", "Es la estructura básica."),
        ("En Inglés de 2.º medio (OA 5, clase 1): ¿qué frase anuncia el resumen final?", "To sum up", "Equivale a en resumen."),
        ("En Inglés de 2.º medio (OA 5, clase 1): ¿qué significa que una presentación sea coherente?", "Que todas sus ideas se relacionan con el tema y siguen un orden", "La coherencia es orden y relación."),
    ],
    task("Prepara un esquema para una presentación de 2 minutos sobre un tema a elección entre: «My favorite hobby», «A place I like» o «A person I admire». Escribe en inglés una introducción de tres oraciones, tres puntos con un ejemplo cada uno y una oración de cierre. Preséntala a un adulto, que marca si el orden se entiende.", "Hello. Today I will talk about my favorite hobby. First, I will say what it is. Then I will explain why I like it. Finally, I will give an example. Point 1: it is drawing. Example: I draw every weekend. Point 2: it relaxes me. Example: after school I feel calm. Point 3: I can do it anywhere. Example: I draw on the bus. To sum up, drawing is my favorite hobby. Thank you.", ["incluye saludo, tema y plan", "tres puntos con un ejemplo cada uno", "un cierre con resumen"], ["esquema en la hoja", "nota del adulto"], ["no anunciar el plan", "agregar una idea que no pertenece al tema"], "Pide que elimine una oración que no ayude y explique por qué."),
    "Lee el texto de la Luna en voz alta y marca con colores la introducción, el desarrollo y el cierre.",
    "Escribe en español el esquema de una presentación sobre tu comida favorita con tres puntos.",
)

# ------------------------------------------------------------------ clase 2: recursos multimodales
S1 = "Diapositiva A de «Light pollution» (contaminación lumínica): 12 líneas de texto pequeño, sin imágenes y con tres colores de letra distintos."
S2 = "Diapositiva B de «Light pollution»: título grande «City lights hide the stars», una foto de una ciudad de noche y una sola frase: «In cities, we see fewer stars.»"
S3 = "Gráfico de ejemplo para «Light pollution»: barras con las estrellas que se ven a simple vista en tres lugares de ejemplo: ciudad = 20, pueblo = 200, campo = 2.000. (datos de ejemplo, no reales)"
S4 = "Cartel de ejemplo para presentar «Greetings around the world»: tres dibujos grandes (apretón de manos, reverencia, beso en la mejilla) y bajo cada uno una palabra: handshake, bow, kiss."
S5 = "Diapositiva C de «The Moon»: un dibujo de las cuatro fases en una fila, con la palabra de cada fase debajo y una flecha que muestra el orden."
S6 = "Presentación D: el estudiante lee todo su texto sin levantar la vista, con las manos en los bolsillos, frente a una pantalla vacía."

lesson(
    OA, 2, MAT_R,
    "Aprenderé a elegir recursos multimodales (imágenes, gráficos, carteles, gestos, objetos) que refuercen el mensaje de una presentación. Sirve para que la audiencia entienda y recuerde mejor tus ideas.",
    ["Sé organizar una presentación en tres partes.", "Conozco palabras para describir imágenes."],
    [
        "Un recurso multimodal es todo medio que se suma a las palabras: una diapositiva, una foto, un gráfico, un cartel, un objeto, un gesto o un sonido. Un buen recurso refuerza el mensaje: no lo repite entero ni lo contradice. Debe ser visible desde el fondo, tener poco texto y estar relacionado con la idea.",
        "Reglas útiles para diapositivas: una idea por diapositiva, pocas palabras, letras grandes, buen contraste y una imagen relevante. Un gráfico debe tener título y datos claros; si los datos son inventados, se rotulan como de ejemplo. Los gestos también ayudan: señalar la imagen mientras la explicas, mirar a la audiencia y usar las manos para mostrar un tamaño o un orden.",
        "Antes de usar un recurso, pregúntate: ¿qué idea refuerza?, ¿se entiende en cinco segundos?, ¿es creativo sin distraer? Si tienes más texto que imagen, pasa algo del texto a tu voz. Tu voz explica; la diapositiva muestra.",
    ],
    [("multimodal resource", "recurso que combina palabras con imagen, gráfico, gesto o sonido"), ("slide", "diapositiva"), ("graph", "gráfico"), ("poster", "cartel"), ("gesture", "gesto"), ("eye contact", "contacto visual")],
    [
        ("Elegir entre dos diapositivas", S1 + " " + S2 + " ¿Cuál refuerza mejor el mensaje?", ["La A tiene demasiado texto pequeño.", "La B tiene un título, una imagen y una sola frase.", "La B es más fácil de entender."], "La B, porque tiene poco texto y una imagen relevante"),
        ("Usar un gráfico", S3 + " ¿Qué idea refuerza este gráfico?", ["Las barras comparan ciudad, pueblo y campo.", "La barra del campo es la más alta.", "Muestra que donde hay menos luces se ven más estrellas."], "Que se ven más estrellas donde hay menos luces"),
    ],
    [
        ("Poner todo el texto en la diapositiva y leerlo.", "La audiencia lee y no te escucha.", "Pon palabras clave y explica con tu voz."),
        ("Usar una imagen bonita que no se relaciona con la idea.", "Distrae y no refuerza el mensaje.", "Elige una imagen que muestre la idea."),
    ],
    [
        mc("¿Qué diapositiva es más clara?", "Una con título, una imagen y una frase", ["Una con doce líneas pequeñas", "Una con tres colores y mucho texto"], "Pocas palabras y una imagen se entienden en segundos."),
        mc("Un gráfico para una presentación debe tener", "un título y datos claros", ["muchos colores sin explicación", "solo un dibujo sin números"], "Sin título ni datos no se entiende qué muestra."),
        mr(S4, "¿Qué palabras acompañan los dibujos?", "handshake, bow y kiss", ["hello, goodbye y thanks", "left, right y center"], "Cada dibujo lleva la palabra del saludo."),
    ],
    [
        mr(S5, "¿Para qué sirve la flecha de esta diapositiva?", "Para mostrar el orden de las fases", ["Para decorar la diapositiva", "Para indicar cuál fase es la más grande"], "La flecha organiza la secuencia."),
        mr(S3, "¿En qué lugar de ejemplo se ven más estrellas?", "En el campo", ["En la ciudad", "En el pueblo"], "El campo tiene 2.000, la mayor cifra."),
        mr(S6, "¿Qué recursos le faltan a esta presentación?", "Mirar al público y usar apoyo visual", ["Más volumen sin mirar", "Más texto en la pantalla"], "Leer sin mirar ni usar recursos no conecta con la audiencia."),
    ],
    [
        mc("Tu idea es que las estrellas se ven menos en las ciudades. ¿Qué recurso la refuerza mejor?", "Una foto de una ciudad de noche con pocas estrellas", ["Una foto de una ciudad en pleno día", "Una foto del campo lleno de estrellas"], "La imagen está relacionada con la idea."),
        mc("¿Qué gesto ayuda cuando muestras el cartel de los saludos?", "Señalar el dibujo que explicas", ["Mirar solo el cartel sin mirar al público", "Señalar con la mano sin decir nada"], "Señalar orienta la mirada de la audiencia."),
        arith("Para el gráfico de ejemplo de la ciudad (20 estrellas) y el pueblo (200 estrellas), ¿cuántas estrellas más se ven en el pueblo?", "200-20", "Se resta la cifra de la ciudad de la del pueblo.", " estrellas"),
    ],
    [
        mr(S1 + " " + S2, "Una compañera dice que la diapositiva A es mejor porque tiene más información. ¿Qué respuesta es más acertada?", "La B comunica más: la audiencia la entiende rápido", ["Tiene razón, porque más texto siempre explica mejor", "Las dos son iguales, porque tratan el mismo tema"], "Una diapositiva con demasiado texto no se lee mientras alguien habla."),
        mc("Un estudiante usa un gráfico con números inventados, pero no lo dice. ¿Qué debe hacer?", "Rotularlo como de ejemplo", ["Nada, porque a nadie le importa", "Quitar el título"], "Los datos inventados se rotulan como de ejemplo."),
    ],
    [
        mr(S2, "Tienes la diapositiva B y dices: «In cities, we see fewer stars». ¿Qué debes agregar con tu voz?", "Un ejemplo que no está en la diapositiva", ["La misma frase repetida con más volumen", "Nada más, porque la diapositiva ya lo dice todo"], "La voz amplía lo que la imagen muestra."),
        mc("¿Cuál es la mejor combinación para presentar tres tipos de saludo?", "Un cartel con tres dibujos, una palabra clave por dibujo y gestos al explicar", ["Un párrafo largo", "Solo gestos sin explicar"], "Combina imagen, palabra y gesto de forma coherente."),
    ],
    [mr(S5 + " " + S6, "Debes mejorar la presentación D con la diapositiva C. ¿Qué tres cambios propones?", "Usar la diapositiva, mirar al público y explicar con tus palabras señalando la flecha", ["Leer más rápido, no mirar y apagar la pantalla", "Cambiar el tema y no usar diapositiva"], "Cada cambio suma un recurso multimodal.")],
    [
        ("En Inglés de 2.º medio (OA 5, clase 2): ¿qué es un recurso multimodal?", "Un recurso que combina palabras con imagen, gráfico, gesto o sonido", "Refuerza el mensaje."),
        ("En Inglés de 2.º medio (OA 5, clase 2): ¿cuántas ideas conviene poner en una diapositiva?", "Una", "Una idea por diapositiva facilita entenderla."),
        ("En Inglés de 2.º medio (OA 5, clase 2): ¿cómo se rotulan datos inventados en un gráfico?", "Como de ejemplo", "Así no se confunden con datos reales."),
    ],
    task("Prepara un recurso para presentar este tema: «Three ways to greet someone». Dibuja o describe un cartel con tres imágenes y una palabra clave cada una, y escribe dos frases para explicarlo mientras lo señalas. Presenta a un adulto y pídele que marque si entendió las tres ideas sin leer.", "Cartel: handshake, bow, kiss on the cheek, con un dibujo cada uno. Frases: In many countries, people shake hands. In some places, people bow. [señala el dibujo]", ["tres imágenes con una palabra clave cada una", "dos frases en inglés relacionadas con el cartel", "usa gestos al explicar"], ["cartel en la hoja", "nota del adulto"], ["poner demasiado texto en el cartel", "usar imágenes sin relación con la idea"], "Pide que quite una palabra del cartel y compruebe si la imagen sola se entiende."),
    "Diseña en tu cuaderno una diapositiva con título, una imagen y una frase sobre las fases de la Luna.",
    "Observa un afiche de tu barrio y escribe en español qué hace que se entienda rápido.",
)

# ------------------------------------------------------------------ clase 3: funciones del lenguaje y vocabulario
F1 = "«In my survey, a large number of students walk to school, but a small number take the bus. Few students come by car. There is little time at lunch, so many students eat quickly.» (survey = encuesta, walk = caminan, take the bus = toman el bus, by car = en auto, lunch = almuerzo, quickly = rápido)"
F2 = "«I usually practice guitar after school. I often play with a friend, and sometimes we play for ages. I have been playing for two years. I hardly ever miss a practice.» (guitar = guitarra, for ages = por mucho tiempo, miss = faltar, practice = ensayo)"
F3 = "«Neither the museum nor the library is open on Mondays. You can either visit them on Tuesday or wait until Saturday. The library is very good, though. As a result, I go there every week.» (open = abierto, wait until = esperar hasta, very good = muy buena, every week = cada semana)"
F4 = "«The teacher said she had checked all the projects. She told us to bring the final version on Friday. I think we would finish earlier if we worked together.» (checked = revisó, final version = versión final, earlier = antes, worked = trabajáramos)"
F5 = "«If I were you, I would practice the presentation twice. You ought to speak slowly. Would you like some help with the slides? I'd rather present first, if possible.» (practice = practicar, ought to = deberías, slides = diapositivas, I'd rather = preferiría, if possible = si es posible)"

lesson(
    OA, 3, MAT_R,
    "Aprenderé a usar en una presentación las funciones del lenguaje del año: cantidad, frecuencia, conectores, lo que otros dijeron, consejos y ofrecimientos. Sirve para que tu presentación sea clara y precisa con el vocabulario del nivel.",
    ["Sé usar there is, there are y los adverbios de frecuencia.", "Conozco unless y as a result."],
    [
        "Para expresar cantidad usa a large number of y a small number of con cosas contables, few y a few con cosas contables, y little y a little con cosas incontables: a few students, a little time, little time. Para frecuencia usa usually, often, sometimes, hardly ever; para duración, for ages, since y for two years con la forma have been playing. Para grado, rather, quite y enough.",
        "Para unir ideas, usa neither ... nor, either ... or, though, unless, as soon as y as a result. Con neither ... nor, el verbo concuerda con el sujeto más cercano: Neither the museum nor the library is open. Para informar lo que otros dicen, retrocede el tiempo: She said she had checked the projects. Para aconsejar usa If I were you, I would...; para ofrecer, Would you like...?; para sugerir, You ought to...; para preferir, I'd rather...",
        "En una presentación, elige las funciones según tu propósito: cantidades para describir resultados de una encuesta, frecuencia para hábitos, conectores para explicar causas y consejos para cerrar con una recomendación. Revisa que cada frase tenga sentido en tu tema.",
    ],
    [("a large number of / a small number of", "una gran cantidad de / una pequeña cantidad de"), ("few / a few", "pocos / unos pocos (contables)"), ("little / a little", "poco / un poco (incontables)"), ("have been + -ing", "acción que empezó antes y continúa"), ("If I were you, I would...", "si yo fuera tú, yo..."), ("I'd rather", "preferiría")],
    [
        ("Cantidad en una encuesta", F1 + " ¿Cuántos estudiantes caminan y cuántos toman el bus?", ["A large number of significa una gran cantidad.", "A small number significa una pequeña cantidad.", "Muchos caminan y pocos toman el bus."], "Una gran cantidad camina y una pequeña cantidad toma el bus"),
        ("Un consejo", F5 + " ¿Qué consejo da el hablante y qué ofrece?", ["If I were you, I would practice twice es un consejo.", "Would you like some help es un ofrecimiento.", "Ought to speak slowly es otro consejo."], "Aconseja practicar dos veces y hablar despacio, y ofrece ayuda con las diapositivas"),
    ],
    [
        ("Usar few y little de forma intercambiable.", "Few va con contables y little con incontables.", "Pregunta si se puede contar: students sí, time no."),
        ("Decir She said she has checked al contar lo que otro dijo.", "El estilo indirecto retrocede el tiempo.", "Retrocede el tiempo: «I have checked» pasa a she had checked."),
    ],
    [
        mc("Completa: There is ____ time left, so we must hurry.", "little", ["few", "many"], "Time es incontable, por eso little."),
        mc("Completa: A ____ students came early, so we could start.", "few", ["little", "much"], "Students es contable; a few significa unos pocos."),
        mr(F2, "¿Qué expresión muestra que algo casi nunca ocurre?", "hardly ever", ["usually", "sometimes"], "Hardly ever es casi nunca."),
    ],
    [
        mr(F2, "¿Qué forma muestra una acción que empezó antes y continúa?", "I have been playing for two years", ["I usually practice guitar", "We sometimes play for ages with a friend"], "Have been playing une el pasado con el presente."),
        mr(F3, "¿Qué conector marca la consecuencia de que la biblioteca es muy buena?", "As a result", ["Neither", "Either"], "As a result introduce la consecuencia."),
        mr(F4, "¿Qué dijo la profesora?", "Que había revisado todos los proyectos", ["Que revisará los proyectos mañana", "Que no revisó ningún proyecto"], "She said she had checked all the projects."),
    ],
    [
        mc("Elige la forma correcta: Neither the museum nor the libraries ____ open on Mondays.", "are", ["is", "be"], "El verbo concuerda con libraries, el sujeto más cercano."),
        mc("Elige la frase de ofrecimiento más natural:", "Would you like some help with the slides?", ["You ought to help me with the slides.", "You ought to ask for help with the slides."], "Would you like...? ofrece ayuda."),
        mc("Elige el consejo correcto:", "If I were you, I would practice twice", ["If I am you, I will practice it twice", "If I were you, I practice twice every day"], "El consejo usa were y would."),
    ],
    [
        mr(F5, "¿Qué frase del texto expresa una preferencia sobre el orden de presentación?", "I'd rather present first, if possible", ["Would you like some help with the slides", "You ought to speak more slowly"], "I'd rather expresa una preferencia sobre el orden."),
        mr(F1, "Un estudiante dice que few students come by car, así que casi nadie usa auto. ¿Es correcta su lectura?", "Sí: few significa pocos, una cantidad muy pequeña", ["No: few significa unos cuantos, una cantidad suficiente", "No: few se usa solo con cosas incontables, como time"], "Few expresa una cantidad muy pequeña."),
    ],
    [
        mr(F3, "¿Con qué frecuencia va el hablante a la biblioteca?", "Cada semana", ["Solo los lunes", "Nunca"], "Dice As a result, I go there every week."),
        mr(F4, "Si la profesora hubiera dicho «I will check all the projects tomorrow», ¿cuál sería la forma correcta de contarlo ahora?", "She said she would check the projects the next day", ["She said she checks all the projects tomorrow", "She said she has checked the projects the next day"], "El estilo indirecto retrocede el tiempo."),
    ],
    [mr("«Our class survey asked 30 students about their lunch. A large number of them, 18, bring food from home. A small number, 4, buy food at school. The rest, 8, go home.»", "¿Cuántos estudiantes del texto no traen comida ni compran en el colegio?", "8", ["18", "4"], "Dice the rest, 8, go home.")],
    [
        ("En Inglés de 2.º medio (OA 5, clase 3): ¿con qué tipo de sustantivos se usa little?", "Con incontables", "Little time, little sugar."),
        ("En Inglés de 2.º medio (OA 5, clase 3): ¿qué frase sirve para aconsejar?", "If I were you, I would...", "Es la forma del consejo hipotético."),
        ("En Inglés de 2.º medio (OA 5, clase 3): ¿qué significa hardly ever?", "Casi nunca", "Es un adverbio de frecuencia baja."),
    ],
    task("Escribe una introducción de tres oraciones y un desarrollo de tres oraciones para una presentación breve sobre tus hábitos de estudio. Usa al menos cinco funciones: una cantidad, una frecuencia, un conector, un consejo y have been + -ing. Sigue este ejemplo y preséntala a un adulto.", "Hello. Today I will talk about my study habits. I usually study after school. A few of my classmates study with me, and I have been studying with a plan for two months. I take a break every forty minutes. As a result, I feel calmer. If I were you, I would try a plan too.", ["usa al menos cinco funciones del año", "las oraciones tienen sentido y orden", "la audiencia entiende el mensaje"], ["texto de seis oraciones en la hoja", "nota del adulto"], ["usar few con incontables", "no retroceder el tiempo en lo que otros dijeron"], "Pide que subraye cada función y diga cuál es."),
    "Escribe cinco oraciones con few, a few, little, a little y a large number of.",
    "Observa una encuesta de tu curso y escribe en español dos frases usando muchos, pocos y la mitad.",
)

# ------------------------------------------------------------------ clase 4: sonidos del idioma y cualidades de la voz
V1 = "«Today, two students will tell a special story about a stormy day. They usually study at the station.» (stormy = con tormenta, station = estación, special = especial)"
V2 = "«My decision is to speak slowly. My dad says television is useful, but I prefer to study.» (decision = decisión, useful = útil, prefer = prefiero)"
V3 = "«Good evening, ladies and gentlemen. [pause] Tonight, we will talk about the stars. [pause] First, light pollution.» (ladies and gentlemen = damas y caballeros, pause = pausa, tonight = esta noche, light pollution = contaminación lumínica)"
V4 = "«Here are two sentences. 1) I said I like the new bookshelf. 2) I said I LIKE the new bookshelf.» (bookshelf = estantería; las mayúsculas indican énfasis)"

lesson(
    OA, 4, MAT_R,
    "Aprenderé a pronunciar con claridad los sonidos /t/, /d/, /ʒ/, /sp/ y /st/ en una presentación y a usar las cualidades de la voz: acento, énfasis, pausas, ritmo y volumen. Sirve para que la audiencia te entienda y te siga.",
    ["Sé distinguir /t/ y /d/.", "Sé ubicar el acento en palabras de dos sílabas."],
    [
        "Para presentar con claridad, cuida los sonidos de la unidad. El /t/ inicial (today, two) lleva una pequeña ráfaga de aire y el /d/ inicial (decision, day) hace vibrar la garganta. El sonido /ʒ/ de usually, decision y television es como un sh sonoro. Las combinaciones /sp/ y /st/ (special, study, station) empiezan sin vocal antes, no como especial ni estudy.",
        "Las cualidades de la voz son el acento de palabra, el énfasis, las pausas, el ritmo y el volumen. En una palabra de dos sílabas, ubica el acento: STUdent, deCIDE. En palabras compuestas, el acento va en la primera parte: BOOKshelf. El énfasis destaca la palabra importante: I said I LIKE the bookshelf. Una pausa corta después de una idea da tiempo a la audiencia.",
        "Habla un poco más despacio que en una conversación, con volumen que llegue al fondo de la sala. Marca en tu texto los lugares de pausa con una línea y las palabras con énfasis con mayúsculas. Practica tres veces y graba o pide a un adulto que te escuche.",
    ],
    [("/t/ /d/", "sonidos iniciales de today y decision"), ("/ʒ/", "sonido de usually y television"), ("/sp/ /st/", "combinaciones iniciales sin vocal antes"), ("stress", "acento de palabra"), ("emphasis", "énfasis: palabra dicha con más fuerza"), ("pause", "pausa")],
    [
        ("Contar sonidos", V1 + " ¿Cuántas palabras tienen el sonido /ʒ/?", ["Busco palabras como usually.", "Usually tiene /ʒ/.", "No hay otra palabra con ese sonido."], "Una: usually"),
        ("Énfasis en una oración", V4 + " ¿Qué cambia en la oración 2?", ["En la oración 2, LIKE se dice con más fuerza.", "Eso destaca que le gusta, quizá contra otra opinión.", "El énfasis cambia lo que quiere destacar el hablante."], "Destaca la palabra like"),
    ],
    [
        ("Decir estudy en lugar de study.", "Se agrega una vocal inicial por el español.", "Empieza con /st/ directamente."),
        ("Hablar sin pausas.", "La audiencia no alcanza a procesar las ideas.", "Marca pausas después de cada idea."),
    ],
    [
        mr(V2, "¿En qué palabra aparece /ʒ/ además de television?", "decision", ["speak", "dad"], "Decision y television comparten el sonido /ʒ/."),
        mc("¿Qué palabra empieza con /sp/?", "speak", ["study", "today"], "Speak empieza con /sp/; study con /st/."),
        mc("¿Dónde cae el acento en student?", "En la primera sílaba", ["En la segunda sílaba", "En ninguna sílaba: se dice parejo"], "Student se pronuncia STUdent."),
    ],
    [
        mr(V1, "¿Cuántas palabras empiezan con /st/?", "Cinco: students, stormy, story, study y station", ["Cuatro: students, story, study y station", "Dos: students y special"], "Study también empieza con /st/."),
        mr(V3, "¿Para qué sirven las pausas marcadas?", "Para dar tiempo a la audiencia entre ideas", ["Para olvidar el texto que preparaste", "Para hablar más fuerte durante toda la idea"], "Las pausas separan ideas."),
        mc("¿Dónde cae el acento en bookshelf?", "En book", ["En shelf", "En las dos por igual"], "En un compuesto el acento va en la primera parte."),
    ],
    [
        mc("Tu audiencia está en el fondo de una sala grande. ¿Qué ajustas?", "El volumen y el ritmo, más despacio", ["Hablar más rápido para terminar antes", "Hablar en voz baja para no cansarse"], "Se necesita volumen y ritmo para llegar al fondo."),
        mr(V2, "¿Dónde cae el acento en decision?", "En la segunda sílaba: deCIsion", ["En la primera sílaba", "En la tercera sílaba"], "Decision lleva el acento en CI."),
        mr(V4, "Si quieres decir que te gusta la estantería nueva, no la vieja, ¿qué palabra enfatizas?", "new", ["said", "I"], "Se enfatiza la palabra que contrasta."),
    ],
    [
        mr("Una estudiante pronuncia «especial» y «estudy» en su presentación.", "¿Qué debe cambiar?", "Empezar special y study sin vocal inicial", ["Agregar una e delante de special y study", "Hablar más rápido para que no se note"], "En inglés las palabras empiezan con /sp/ y /st/."),
        mc("¿Cuál recomendación ayuda más a una voz poco clara?", "Practicar tres veces con pausas", ["Leer el texto sin mirar a la audiencia", "Hablar muy rápido para terminar antes"], "La práctica con pausas mejora la claridad."),
    ],
    [
        mr(V1, "En «Today, two students will tell a special story», ¿cuántas palabras empiezan con /t/?", "Tres: today, two y tell", ["Dos: today y two", "Cuatro: today, two, tell y students"], "Students empieza con /st/, no con /t/."),
        mr(V2, "¿Qué palabras de este texto empiezan con el sonido /d/?", "decision y dad", ["decision y television", "dad y study"], "Decision y dad empiezan con /d/; television empieza con /t/ y study con /st/."),
    ],
    [mr(V3, "Imagina que quieres practicar este texto. Escribe dónde pondrías el énfasis en la última frase para destacar la contaminación lumínica.", "Pondría el énfasis en light pollution", ["Pondría el énfasis en First, porque abre la frase", "No pondría énfasis en ninguna palabra: se dice todo parejo"], "El tema central es el que se destaca.")],
    [
        ("En Inglés de 2.º medio (OA 5, clase 4): ¿qué sonido tiene la palabra usually en el medio?", "/ʒ/", "Es el sh sonoro."),
        ("En Inglés de 2.º medio (OA 5, clase 4): ¿qué sirve para destacar una palabra importante?", "El énfasis", "Se dice con más fuerza."),
        ("En Inglés de 2.º medio (OA 5, clase 4): ¿qué marcas en tu guion para recordar dónde detenerte?", "Las pausas", "Se señalan con una línea."),
    ],
    task("Escribe cuatro oraciones sobre tu tema de presentación. Marca con una línea (/) las pausas y con mayúsculas la palabra con énfasis. Lee en voz alta a un adulto y pide que marque si se entienden los sonidos /t/, /d/, /ʒ/, /sp/ y /st/. Sigue este ejemplo.", "Today I will talk about the stars. / Usually, we STUDY at night. / A special telescope helps us. / Thank you.", ["cuatro oraciones con pausas y énfasis", "incluye al menos tres sonidos de la clase", "el adulto entiende cada palabra"], ["hoja con el guion marcado", "nota del adulto"], ["decir una vocal antes de s", "hablar sin pausas"], "Pide que repita la oración que más le costó hasta que salga clara."),
    "Lee en voz alta el texto sobre la Luna con una pausa después de cada punto.",
    "Graba tu voz diciendo tres frases y escribe en español qué mejorarías.",
)

# ------------------------------------------------------------------ clase 5: audiencia, contexto y propósito
AU1 = "Situación A: presentas «Greetings around the world» a un grupo de niños de 8 años en una biblioteca, durante 3 minutos, para que se diviertan y aprendan dos saludos."
AU2 = "Situación B: presentas «Light pollution» a profesores y apoderados en una reunión formal de 10 minutos, para que apoyen apagar luces de la cancha por la noche."
AU3 = "Situación C: presentas «The phases of the Moon» a tu curso, durante 5 minutos, como trabajo de Ciencias."
AU4 = "«Hey, kids! Do you know how people say hello? Shake hands! Bow! Kiss on the cheek! Let's try it together.» (kids = niños, say hello = saludar, try = probar)"
AU5 = "«Good evening. Thank you for coming. Tonight I will explain how outdoor lights affect our view of the stars and propose a simple measure for our school.» (outdoor lights = luces exteriores, affect = afectan, propose = propongo, measure = medida)"

lesson(
    OA, 5, MAT_R,
    "Aprenderé a adaptar una presentación a su audiencia, al contexto y al propósito: elegir el vocabulario, el tono, el tiempo y los recursos. Sirve para que el mismo tema se entienda bien en situaciones distintas.",
    ["Sé organizar una presentación y elegir recursos.", "Conozco el registro formal y el informal."],
    [
        "Antes de presentar, responde tres preguntas. ¿Quién es la audiencia (audience)? ¿Cuál es el contexto (context): lugar, tiempo y formalidad? ¿Cuál es el propósito (purpose): informar, convencer, enseñar o entretener? Con eso decides el vocabulario, el tono, la cantidad de datos y los recursos.",
        "Con niños, usa palabras simples, juegos y gestos grandes. Con adultos en una reunión formal, usa un tono respetuoso, datos claros y una propuesta concreta. Con compañeros de curso, mezcla explicación y ejemplos cercanos. El registro formal usa Good evening, Thank you for coming y Ladies and gentlemen; el informal usa Hey y Let's try it. Si tu propósito es convencer, termina con una petición concreta.",
        "El tiempo también importa: una presentación de tres minutos tiene pocos puntos y mucha claridad; una de diez minutos admite más datos y preguntas. Ensaya con el reloj y recorta lo que no cabe.",
    ],
    [("audience", "audiencia"), ("context", "contexto: lugar, tiempo y formalidad"), ("purpose", "propósito: para qué presentas"), ("formal / informal", "formal / informal"), ("tone", "tono"), ("proposal", "propuesta")],
    [
        ("Adaptar a niños", AU1 + " ¿Qué recursos y vocabulario conviene usar?", ["La audiencia son niños de 8 años.", "Conviene un tono alegre, palabras simples y gestos grandes.", "Un saludo así sería Hey, kids! y una invitación como Let's try it together."], "Un tono alegre, palabras simples, juegos y gestos grandes"),
        ("Adaptar a adultos", AU2 + " ¿Qué tono y qué cierre conviene usar?", ["La audiencia son adultos en una reunión formal.", "Conviene un tono respetuoso y datos claros.", "El propósito es convencer, así que el cierre es una petición concreta."], "Un tono formal y un cierre con la petición de apagar las luces"),
    ],
    [
        ("Usar la misma presentación para cualquier audiencia.", "No todos tienen el mismo nivel ni la misma necesidad.", "Cambia el vocabulario, el tono y los ejemplos."),
        ("Terminar una presentación para convencer sin pedir nada concreto.", "La audiencia no sabe qué hacer.", "Cierra con una petición clara."),
    ],
    [
        mc("Hablas a niños de 8 años. ¿Qué saludo es más adecuado?", "Hey, kids!", ["Ladies and gentlemen", "Good evening, esteemed guests"], "Con niños se usa un tono cercano."),
        mc("¿Qué pregunta ayuda a decidir el tono de una presentación?", "¿Quién es la audiencia?", ["¿De qué color es mi camisa?", "¿Cuántas letras tiene el título?"], "El tono depende de quién escucha."),
        mr(AU4, "¿Qué hace el hablante para involucrar a los niños?", "Les propone probar los saludos", ["Les da un examen sobre los saludos", "Les lee un informe con muchos datos"], "Dice Let's try it together."),
    ],
    [
        mr(AU5, "¿Cuál es el propósito de este inicio?", "Explicar un problema y proponer una medida", ["Contar un chiste para empezar la reunión", "Enseñar un juego a los apoderados"], "Dice I will explain... and propose a simple measure."),
        mr(AU3, "¿Cuál es el propósito de la situación C?", "Informar al curso sobre las fases de la Luna", ["Convencer a los profesores de cambiar el reglamento", "Entretener a niños de ocho años con un juego"], "Es un trabajo de Ciencias para enseñar."),
        mc("¿Qué es más adecuado para una reunión formal?", "Thank you for coming", ["Hey, guys, thanks for being here!", "What's up, everybody?"], "Es una fórmula formal de agradecimiento."),
    ],
    [
        mr(AU2, "Presentas light pollution a niños de 8 años, no a adultos como en la situación B. ¿Qué cambias?", "El vocabulario y los ejemplos, más simples", ["El tema, que cambiarías por otro más fácil para ellos", "Los datos, que serían más numerosos y técnicos para impresionar"], "Se adapta el lenguaje, no el tema."),
        arith("Una presentación de la situación B dura 10 minutos. La introducción usa 2 minutos, el cierre 2 minutos y las preguntas 3 minutos. ¿Cuántos minutos quedan para el desarrollo?", "10-2-2-3", "Se restan los otros tres bloques del tiempo total.", " minutos"),
        mc("Tu presentación formal dura 10 minutos, pero tu guion alcanza para 14. ¿Qué haces?", "Recortar puntos menos importantes", ["Hablar más rápido para que todo quepa", "Saltarte el cierre y las preguntas"], "Se recorta lo secundario y se conserva la estructura."),
    ],
    [
        mr(AU2, "Un compañero propone terminar con «That's all, bye». ¿Por qué no es lo mejor?", "Porque falta una petición concreta y formal", ["Porque a los adultos se les cuenta un chiste al final", "Porque los adultos no necesitan una despedida formal"], "Se necesita un cierre formal y una propuesta."),
        mr(AU1, "Un estudiante usa estadísticas con muchos números para niños de 8 años. ¿Qué opinas?", "Conviene reducir los números y usar ejemplos concretos", ["Conviene agregar más números", "Conviene hablar sin mirar"], "Los niños necesitan ejemplos simples."),
    ],
    [
        mr(AU3, "Quieres adaptar la presentación de la Luna a niños de 8 años. ¿Qué cambias?", "El lenguaje y los recursos: dibujos y gestos", ["El tema, que sería otro más fácil, y el propósito", "El orden de las fases y el número de fases"], "El tema se mantiene; cambian lenguaje y recursos."),
        mr(AU2 + " " + AU5, "¿Qué rasgo de AU5 es adecuado para la situación B?", "El saludo formal y la propuesta que anuncia", ["El tono infantil y los juegos con el público", "El juego con los saludos y los dibujos grandes"], "Coincide con adultos y propósito de convencer."),
    ],
    [mc("Debes presentar tu hobby en una feria escolar para visitantes de distintas edades. ¿Qué combinación es la mejor?", "Palabras simples, un cartel con imágenes, pocos puntos y una pregunta para el público", ["Palabras técnicas, un texto largo y ninguna pregunta", "Solo una lectura muy rápida"], "Se adapta a una audiencia variada con claridad.")],
    [
        ("En Inglés de 2.º medio (OA 5, clase 5): ¿qué tres preguntas se responden antes de presentar?", "Quién es la audiencia, cuál es el contexto y cuál es el propósito", "Con eso se decide el tono."),
        ("En Inglés de 2.º medio (OA 5, clase 5): ¿cómo conviene terminar una presentación para convencer?", "Con una petición concreta", "Dice qué debe hacer la audiencia."),
        ("En Inglés de 2.º medio (OA 5, clase 5): ¿qué se ajusta si la presentación es más corta?", "La cantidad de puntos", "Se recortan los menos importantes."),
    ],
    task("Elige una de estas situaciones para tu presentación sobre «Greetings around the world»: A) niños de 8 años, 3 minutos; B) profesores, 5 minutos, formal. Escribe en inglés una introducción de dos oraciones adaptada y un cierre de una oración, y explica en español dos cambios que hiciste por la audiencia. Presenta a un adulto.", "Situación A: Hey, kids! Today we will learn two ways to say hello. Cierre: Now you know two ways to say hello. Cambios: palabras simples y juego con gestos.", ["adapta el tono a la audiencia elegida", "incluye una introducción y un cierre", "explica dos cambios"], ["hoja con el texto y los cambios", "nota del adulto"], ["usar un tono formal con niños", "no cambiar nada entre audiencias"], "Pide que lea la introducción en el tono de la otra audiencia y compare."),
    "Escribe en tu cuaderno el saludo inicial que usarías para niños y el que usarías para profesores.",
    "Observa una charla en la tele o internet y anota en español cómo adapta el tono a su audiencia.",
)
