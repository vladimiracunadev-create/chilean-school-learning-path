"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 08: presentación oral con recursos multimodales.

Textos y guiones originales y ficticios, con pista en español; todo lo que una pregunta nombra está escrito en el enunciado.
Los títulos de clase del plan son genéricos; aquí cada clase trabaja un grupo del OA: contenido y organización coherente;
recursos multimodales; funciones del lenguaje y vocabulario; sonidos y cualidades de la voz; audiencia, contexto y propósito.
La producción oral real (hablar) se evalúa con la tarea abierta y una persona que escucha; los ejercicios cerrados trabajan
la planificación y el análisis de guiones.
"""
from __future__ import annotations

from en_m2_a_common import MAT_SPEAK, arith, lesson, task

OA = "EN2M OA 08"

# ================================================== clase 1: contenido y organización coherente
PRES1 = "«Good morning. My topic is traffic jams in big cities. First, I will explain what a traffic jam is. Second, I will show two causes. Finally, I will suggest one solution. A traffic jam is a long line of cars that move very slowly. One cause is that too many people travel at the same time. Another cause is road works. One solution is to use buses more often. In conclusion, traffic jams waste time, but we can reduce them. Thank you for listening.»\n(traffic jams = tacos, big cities = grandes ciudades, causes = causas, road works = obras viales, waste = hacer perder, reduce = reducir)"
PRES2 = "«Hello. Today I want to talk about volunteering. I will talk about why people volunteer. Then I will describe my own experience. At the end, I will give advice. People volunteer because they want to help. I helped at a youth centre last summer. I taught children to draw. My advice is to start with a small task.»\n(volunteering = voluntariado, youth centre = centro juvenil, taught = enseñé, advice = consejo, task = tarea)"

lesson(
    OA, 1, MAT_SPEAK,
    "Aprenderé a organizar una presentación oral con inicio, desarrollo y cierre, y con ideas coherentes apoyadas por datos. Sirve para que mi audiencia entienda de qué hablo, qué ideas importan y cómo termina.",
    ["Sé first, then y finally para ordenar ideas.", "Sé el presente simple y el pasado simple."],
    [
        "Una presentación oral (oral presentation) tiene tres partes. La introducción (introduction) saluda, dice el tema y anuncia el plan: My topic is… First, I will… Finally, I will… El desarrollo (body) explica cada idea con un dato o un ejemplo. La conclusión (conclusion) repite la idea principal y cierra: In conclusion,… Thank you for listening. Esta estructura ayuda a que tu audiencia no se pierda.",
        "La coherencia (coherence) significa que las ideas siguen un orden lógico y se relacionan. Para lograrla, usa conectores de orden (first, second, then, finally), de adición (also, another) y de causa (because). Cada idea necesita un dato exacto: una cifra, un lugar o un ejemplo. Una idea sin dato es débil, y un dato sin idea no se entiende.",
        "Para demostrar conocimiento del contenido (content knowledge), investiga y escribe solo lo que puedas explicar con tus palabras. Prepara una tarjeta con palabras clave, no un texto completo, para no leer. Practica en voz alta y mide el tiempo. Si usas una cifra, comprueba que sea correcta o dilo como ejemplo.",
    ],
    [("introduction", "introducción: saludo, tema y plan"), ("body", "desarrollo: ideas con datos"), ("conclusion", "conclusión: cierre"), ("coherence", "coherencia: orden lógico entre ideas"), ("in conclusion", "en conclusión"), ("topic", "tema")],
    [
        ("Parte de la presentación", "Frase: «Good morning. My topic is school clubs.» ¿Qué parte es? A) introducción B) conclusión", ["Saluda y anuncia el tema.", "Eso pertenece al inicio.", "Es la introducción."], "A) introducción"),
        ("Conector de orden", "¿Qué conector sirve para empezar a enumerar? A) First B) Finally", ["Busco el que inicia la lista.", "First es el primero.", "Finally es el último."], "A) First"),
    ],
    [
        ("Empezar a hablar sin decir cuál es el tema.", "La audiencia no sabe qué esperar.", "Anuncia tu tema y tu plan en la introducción."),
        ("Leer un texto completo, palabra por palabra.", "Se pierde el contacto con la audiencia.", "Usa tarjetas con palabras clave y practica."),
    ],
    [
        ("Lee: " + PRES1 + " ¿Cuál es el tema? A) los tacos en las ciudades B) el deporte", "A", "Dice My topic is traffic jams in big cities."),
        ("Lee: " + PRES1 + " ¿Cuántas causas presenta? A) dos B) cuatro", "A", "Anuncia I will show two causes."),
        ("Lee: " + PRES2 + " ¿Cuál es el tema? A) el voluntariado B) los viajes", "A", "Dice I want to talk about volunteering."),
    ],
    [
        ("Lee: " + PRES1 + " ¿Qué parte empieza con In conclusion? A) la conclusión B) la introducción", "A", "In conclusion anuncia el cierre."),
        ("Lee: " + PRES2 + " ¿Qué experiencia propia cuenta? A) ayudó en un centro juvenil B) viajó al extranjero", "A", "Dice I helped at a youth centre."),
        ("Lee: " + PRES1 + " ¿Qué solución propone? A) usar más los buses B) construir más autopistas", "A", "Dice use buses more often."),
    ],
    [
        ("Lee: " + PRES2 + " ¿Qué orden anuncia en la introducción? A) razones, experiencia y consejo B) consejo, razones y experiencia", "A", "Dice why people volunteer, then my own experience, at the end advice."),
        ("Lee: " + PRES1 + " ¿Qué frase explica la primera causa de los tacos? A) too many people travel at the same time B) a long line of cars", "A", "One cause is that too many people travel at the same time; la otra frase define qué es un taco."),
        ("Lee: " + PRES2 + " ¿Cuál es el consejo final de la presentación? A) empezar con una tarea pequeña B) trabajar solo", "A", "Dice My advice is to start with a small task."),
    ],
    [
        ("Lee: " + PRES2 + " ¿Qué falta en esta presentación para ser completa? A) una conclusión clara con agradecimiento B) un saludo", "A", "Termina con el consejo, pero no tiene frase de cierre."),
        ("Lee: " + PRES1 + " Un compañero dice que la presentación no es coherente. ¿Qué lo contradice? A) usa First, Second y Finally B) es corta", "A", "Los conectores de orden muestran coherencia."),
    ],
    [
        ("Ordena las partes: a) conclusión b) introducción c) desarrollo", "b, c, a", "Primero se presenta el tema, luego se explica y al final se cierra."),
        ("Lee: " + PRES2 + " Ordena lo que dice: a) consejo b) razones para ser voluntario c) su experiencia personal", "b, c, a", "Sigue el orden anunciado."),
    ],
    [("Lee: «Hello. My topic is school uniforms. First, I will explain the history. Second, I will give two opinions. Finally, I will give my own opinion.» (uniforms = uniformes, history = historia, opinions = opiniones). ¿Cuántos puntos anuncia en total?", "3", "Anuncia first, second y finally.")],
    [
        ("¿Qué tres partes tiene una presentación (en Inglés, 2.º medio)?", "Introducción, desarrollo y conclusión", "Ayudan a organizar las ideas."),
        ("¿Qué es la coherencia (en Inglés, 2.º medio)?", "El orden lógico de las ideas", "Las ideas se relacionan entre sí."),
        ("¿Qué debe llevar cada idea?", "Un dato o un ejemplo", "Así se demuestra conocimiento."),
    ],
    task("Elige uno de estos temas: A) mi pasatiempo, B) un deporte que me gusta. Escribe en una tarjeta: tema, plan de tres puntos con first, second, finally, un dato exacto por punto y una frase de cierre con In conclusion. Luego preséntalo en voz alta, de pie, a una persona de tu casa, en menos de dos minutos.", "Ejemplo: My topic is football. First, I will explain the rules. Second, I will describe my team. Finally, I will say why I like it. In conclusion, football is fun and friendly. Datos: 11 players; we train twice a week.", ["anuncia el tema y un plan de tres puntos", "cada punto lleva un dato", "termina con In conclusion y se entiende en voz alta"], ["tarjeta con palabras clave", "comentario de la persona que escuchó"], ["leer un texto completo", "omitir la conclusión"], "Pide a la persona que escuchó que repita tu plan de tres puntos para comprobar si fue claro."),
    "Practica tu presentación frente a un espejo y mide el tiempo.",
    "Escribe una presentación de 5 líneas sobre un tema de otra asignatura con la estructura de tres partes.",
)

# ================================================== clase 2: recursos multimodales
SLIDE1 = "Diapositiva de ejemplo A: Title: «Phones and Sleep». Texto en la diapositiva: 14 líneas pequeñas de texto, sin imágenes. El estudiante lee todo en voz alta."
SLIDE2 = "Diapositiva de ejemplo B: Title: «Phones and Sleep». Un gráfico de barras con dos columnas: 7 hours (sin teléfono) y 5 hours (con teléfono), de ejemplo. Un título claro: «Less phone, more sleep». El estudiante explica el gráfico con sus palabras."
PROP = "Un estudiante presenta «Healthy Breakfast» (desayuno saludable). Usa tres imágenes grandes de frutas, una mímica para mostrar «cut» y una pregunta a la audiencia: «What do you eat in the morning?»"

lesson(
    OA, 2, MAT_SPEAK,
    "Aprenderé a elegir recursos multimodales (imágenes, gráficos, objetos, gestos y la voz) para reforzar mi mensaje de forma creativa en una presentación oral. Sirve para que mi audiencia entienda mejor y se mantenga atenta.",
    ["Sé organizar una presentación con inicio, desarrollo y cierre.", "Sé leer un gráfico simple."],
    [
        "Un recurso multimodal (multimodal resource) usa más de un modo para comunicar: texto, imágenes, sonido, objetos, gestos y movimiento. Un buen recurso refuerza tu mensaje, no lo reemplaza. Una diapositiva (slide) con pocas palabras clave, una imagen grande o un gráfico ayuda más que una con párrafos largos. Si lees el texto de la diapositiva, la audiencia lee más rápido que tú y se aburre.",
        "Reglas simples: usa letra grande (no más de siete palabras por línea), una idea por diapositiva y colores con buen contraste. Los gráficos deben tener título y datos claros. Los gestos (gestures) y la mirada refuerzan lo que dices: señala la imagen, mira a la audiencia, cambia el tono para marcar lo importante. Una pregunta a la audiencia crea participación.",
        "Ser creativo (creative) significa elegir un recurso original que se relacione con el mensaje: un objeto, una breve mímica, una pregunta, un dibujo o una comparación. Pero la creatividad no debe distraer. Antes de usar un recurso, pregúntate: ¿ayuda a entender mi idea? Si la respuesta es no, quítalo.",
    ],
    [("multimodal", "con varios modos: texto, imagen, voz, gesto"), ("slide", "diapositiva"), ("graph", "gráfico"), ("gesture", "gesto"), ("eye contact", "contacto visual"), ("keyword", "palabra clave")],
    [
        ("Elegir recurso", "Quieres mostrar cuántas horas duermen los estudiantes. ¿Qué recurso conviene? A) un gráfico de barras B) un párrafo largo", ["Son cantidades para comparar.", "El gráfico las muestra rápido.", "Conviene un gráfico."], "A"),
        ("Diapositiva", "¿Cuál es una buena diapositiva? A) tres palabras clave y una imagen B) un párrafo de veinte líneas", ["La diapositiva debe ser breve.", "Las palabras clave y la imagen ayudan.", "La A."], "A"),
    ],
    [
        ("Leer palabra por palabra la diapositiva.", "La audiencia ya la leyó y pierde el interés.", "Habla con tus palabras y usa la diapositiva como apoyo."),
        ("Poner muchas imágenes que no se relacionan con el tema.", "Distraen y confunden.", "Elige solo las que apoyan una idea."),
    ],
    [
        ("Lee: " + SLIDE1 + " ¿Qué problema tiene esta diapositiva? A) demasiado texto y sin imágenes B) falta el título", "A", "Tiene 14 líneas y ninguna imagen."),
        ("Lee: " + SLIDE2 + " ¿Qué muestra el gráfico? A) las horas de sueño con y sin teléfono B) el precio de los teléfonos", "A", "Compara 7 horas con 5 horas."),
        ("Lee: " + PROP + " ¿Qué recurso usa para mostrar la acción de cortar? A) mímica B) un video", "A", "El texto dice una mímica para mostrar cut."),
    ],
    [
        ("Lee: " + SLIDE2 + " ¿Qué ventaja tiene sobre la A? A) es clara y tiene un gráfico con título B) tiene más palabras", "A", "El gráfico y el título claro ayudan al mensaje."),
        ("Lee: " + PROP + " ¿Para qué sirve la pregunta a la audiencia? A) para que participe B) para terminar antes", "A", "Una pregunta involucra a las personas."),
        ("Lee: " + SLIDE2 + " ¿Cuántas horas más duerme quien no usa teléfono, según el gráfico de ejemplo?", "2", "7 menos 5 son 2."),
    ],
    [
        ("Lee: " + PROP + " ¿Cuántas imágenes usa? A) tres B) cuatro", "A", "El texto dice tres imágenes grandes."),
        ("Lee: " + SLIDE1 + " ¿Qué harías para mejorarla? A) dejar tres palabras clave y agregar una imagen B) agregar más texto", "A", "Menos texto y una imagen apoyan mejor."),
        ("Lee: " + SLIDE2 + " ¿Qué frase del estudiante acompaña bien al gráfico? A) Look at the graph: seven hours is more than five. B) I am nervous.", "A", "La frase usa el gráfico para explicar la comparación."),
    ],
    [
        ("Lee: " + PROP + " Un compañero dice que las imágenes de frutas ayudan. ¿Por qué? A) porque se relacionan con el tema del desayuno B) porque son bonitas", "A", "Un recurso útil se conecta con el mensaje."),
        ("Lee: " + SLIDE1 + " Si el estudiante lee las 14 líneas, ¿qué pasa con la audiencia? A) se aburre y deja de escuchar B) entiende mejor", "A", "Escucha lo mismo que ya está escrito."),
    ],
    [
        ("Ordena de más a menos adecuado para una diapositiva: a) tres palabras clave y una imagen b) una lista de ocho palabras c) un párrafo largo", "a, b, c", "Menos texto y apoyo visual comunican mejor."),
        ("Lee: " + PROP + " Elige el recurso más creativo para mostrar «energy»: A) una mini mímica de saltar B) escribir solo la palabra", "A", "El gesto crea una imagen memorable."),
    ],
    [("Lee: «A student presents the idea of ‘Teamwork’ with a puzzle of six pieces. Each piece has the name of one student, and the puzzle is complete only when all six pieces are together.» (puzzle = rompecabezas, piece = pieza, together = juntas). ¿Cuántas piezas tiene?", "6", "El texto dice six pieces.")],
    [
        ("¿Qué es un recurso multimodal (en Inglés, 2.º medio)?", "Uno que usa más de un modo: texto, imagen, gesto o voz", "Refuerza el mensaje."),
        ("¿Qué debe tener una buena diapositiva?", "Pocas palabras y una imagen o gráfico", "Apoya al hablante."),
        ("¿Qué haces con un recurso que no ayuda?", "Lo quito", "Debe reforzar el mensaje."),
    ],
    task("Elige un tema: A) «Why teenagers need friends» o B) «Our school sports day». Dibuja una diapositiva de ejemplo con título, tres palabras clave y una imagen. Escribe un gesto, una pregunta a la audiencia y una frase en inglés para explicar la imagen. Preséntala a una persona de tu casa en menos de un minuto.", "Ejemplo: Title: Our school sports day. Keywords: race, team, fun. Imagen: dibujo de una pista. Gesto: señalar la imagen. Pregunta: Do you like races? Frase: Look at the picture: here the students are running.", ["usa pocas palabras y una imagen", "incluye un gesto y una pregunta", "la frase en inglés explica la imagen"], ["dibujo de la diapositiva", "comentario de la persona que escuchó"], ["escribir un párrafo largo", "usar una imagen sin relación con el tema"], "Pregunta a la persona que escuchó qué recurso la ayudó más."),
    "Mira una presentación escolar breve y anota tres recursos que ayudaron.",
    "Diseña tres diapositivas distintas para un mismo tema, con un gráfico, una imagen y una pregunta.",
)

# ================================================== clase 3: funciones del lenguaje y vocabulario
PRES3 = "«Hello. I am going to talk about my weekly routine. I usually wake up at seven. I often walk to school because it is close. I rarely eat in the cafeteria. I am quite good at maths, but I am not good at drawing. Yesterday, when my friend called, I had already finished my homework. My friend said that the Science test was easy. Neither she nor I studied much, so we were lucky. Would you like to know more? Thank you.»\n(routine = rutina, wake up = despertarse, close = cerca, rarely = rara vez, lucky = con suerte, would you like = te gustaría)"
PRES4 = "«Good afternoon. Today I will compare two clubs: chess and theatre. The chess club meets twice a week, but the theatre club meets only on Fridays. Chess is quieter than theatre. I believe that both clubs are useful. In my opinion, theatre helps you speak in public, though chess helps you think. As a result, I joined both.»\n(compare = comparar, quieter = más tranquilo, useful = útil, in public = en público, helps = ayuda, joined = me uní)"

lesson(
    OA, 3, MAT_SPEAK,
    "Aprenderé a usar apropiadamente en mi presentación las funciones del lenguaje del año, el vocabulario del nivel y expresiones de uso común. Sirve para que mis ideas se entiendan con variedad y precisión.",
    ["Sé usar adverbios de frecuencia y conectores simples.", "Sé el pasado simple."],
    [
        "Cada parte de una presentación necesita una función del lenguaje (language function): saludar y presentar el tema (I am going to talk about…), describir la frecuencia (I usually…, I rarely…), contar algo anterior (I had already finished my homework when my friend called), informar lo que otros dicen (My friend said that…), expresar opinión (In my opinion…, I believe that…), comparar (quieter than), conectar ideas (neither…nor, though, as a result) e invitar a participar (Would you like to know more?).",
        "El vocabulario del nivel (level vocabulary) incluye palabras frecuentes de tus temas: routine, compare, useful, join. Las palabras de uso frecuente (frequent words) y las expresiones comunes (common expressions), como in my opinion o for example, hacen que tu mensaje suene natural. Evita repetir siempre la misma palabra: usa sinónimos como big y large, o good y useful.",
        "Para elegir bien, relaciona cada función con tu mensaje. Si cuentas tu experiencia, usa pasado. Si comparas, usa más… que. Si das una opinión, usa I believe that o In my opinion y una razón con because. Revisa que el verbo concuerde con la persona (she studies, they study) y que los conectores unan ideas que realmente se relacionan.",
    ],
    [("language function", "función del lenguaje: lo que se hace al hablar"), ("in my opinion", "en mi opinión"), ("for example", "por ejemplo"), ("compare", "comparar"), ("rarely", "rara vez"), ("as a result", "como resultado")],
    [
        ("Función", "Frase: «I usually walk to school.» ¿Qué función cumple? A) describir frecuencia B) expresar acuerdo", ["Usually muestra cada cuánto.", "Describe una frecuencia.", "La A."], "A"),
        ("Opinión", "¿Qué frase expresa opinión? A) In my opinion, music is important. B) The class starts at eight.", ["In my opinion introduce una opinión.", "La B es un dato.", "La A."], "A"),
    ],
    [
        ("Usar siempre la misma palabra, como good.", "El vocabulario es pobre y repetitivo.", "Alterna sinónimos: good, useful, helpful."),
        ("Usar un conector que no corresponde (as a result sin consecuencia).", "El conector no une ideas relacionadas.", "Usa as a result solo cuando la segunda idea sea consecuencia de la primera."),
    ],
    [
        ("Lee: " + PRES3 + " ¿A qué hora se despierta? A) a las siete B) a las ocho", "A", "Dice I usually wake up at seven."),
        ("Lee: " + PRES4 + " ¿Cuántas veces a la semana se reúne el club de ajedrez? A) dos B) una", "A", "Dice twice a week."),
        ("Lee: " + PRES3 + " ¿Con qué frecuencia come en la cafetería? A) rara vez B) siempre", "A", "Dice I rarely eat in the cafeteria."),
    ],
    [
        ("Lee: " + PRES3 + " ¿Qué función cumple Would you like to know more? A) invitar a la audiencia B) despedirse", "A", "Es una pregunta para la audiencia."),
        ("Lee: " + PRES4 + " ¿Qué función cumple In my opinion? A) expresar opinión B) contar un hecho", "A", "Introduce lo que piensa el hablante."),
        ("Lee: " + PRES3 + " ¿Qué función cumple My friend said that the Science test was easy? A) informar lo que otro dijo B) dar un consejo", "A", "Said that introduce lo dicho por otra persona."),
    ],
    [
        ("Lee: " + PRES3 + " ¿Qué ya había hecho cuando su amigo llamó? A) había terminado su tarea B) había visto televisión", "A", "Dice I had already finished my homework."),
        ("Lee: " + PRES4 + " ¿Qué compara con quieter than? A) el ajedrez con el teatro B) el teatro con el cine", "A", "Dice Chess is quieter than theatre."),
        ("Completa con el adverbio adecuado: «I ___ eat breakfast; I eat it every day.» A) always B) never", "A", "Every day indica siempre."),
    ],
    [
        ("Lee: " + PRES4 + " ¿Qué consecuencia expresa As a result? A) se unió a ambos clubes B) dejó los dos clubes", "A", "Dice As a result, I joined both."),
        ("Lee: " + PRES3 + " ¿Qué muestra Neither she nor I studied much? A) que ninguno de los dos estudió mucho B) que los dos estudiaron mucho", "A", "Neither…nor niega ambos."),
    ],
    [
        ("Une cada oración con su función. 1) I rarely eat out. 2) I believe that sport is important. 3) My friend said that it was easy. Funciones: a) informar lo que otro dice b) describir frecuencia c) expresar opinión", "1-b, 2-c, 3-a", "Rarely es frecuencia, I believe es opinión y said that reporta."),
        ("Lee: " + PRES4 + " Sustituye useful por un sinónimo adecuado. A) helpful B) heavy", "A", "Helpful significa útil; heavy no."),
    ],
    [("Lee: «Good morning. I am going to talk about my hobby: photography. I usually take photos on weekends. My brother said that my best photo is of a cat. In my opinion, a camera is a tool for stories.» (hobby = pasatiempo, weekends = fines de semana, tool = herramienta). ¿De quién es la opinión sobre la cámara?", "Del hablante", "Dice In my opinion, a camera is a tool for stories.")],
    [
        ("¿Qué frase introduce una opinión (en Inglés, 2.º medio)?", "In my opinion…", "Anuncia lo que piensa el hablante."),
        ("¿Qué función cumple said that?", "Informar lo que dice otra persona", "Se usa para reportar."),
        ("¿Qué puedo hacer para no repetir palabras?", "Usar sinónimos", "Enriquece el mensaje."),
    ],
    task("Prepara una presentación de 60 segundos sobre tu semana o tu club favorito. Debe incluir: un saludo con I am going to talk about…, una frase de frecuencia (usually, rarely…), una frase de opinión con In my opinion o I believe that, una frase con said that y un conector (though, as a result, neither…nor). Escribe una tarjeta con palabras clave y preséntala a una persona de tu casa.", "Ejemplo: Hello. I am going to talk about my music club. We usually meet on Tuesdays. My teacher said that we are improving. In my opinion, music is relaxing. As a result, I practise at home.", ["usa cuatro funciones del lenguaje", "incluye un conector", "no repite siempre las mismas palabras"], ["tarjeta con palabras clave", "comentario de la persona que escuchó"], ["omitir el saludo", "usar un conector que no une ideas"], "Pregunta a la persona que escuchó cuál fue la frase que mejor entendió."),
    "Escribe diez expresiones comunes en una lista con su traducción y úsalas en frases.",
    "Escribe un guion de 80 palabras que incluya cuatro funciones del lenguaje diferentes.",
)

# ================================================== clase 4: sonidos y cualidades de la voz
SPEECH4 = "«Today I want to tell you about a special student at our school. He usually studies after dinner. He is good at drawing. His decision is to become a designer. He visits the station every day to take photos of the city.»\n(designer = diseñador, station = estación, decision = decisión)"

lesson(
    OA, 4, MAT_SPEAK,
    "Aprenderé a usar apropiadamente los sonidos /t/, /d/, /ʒ/, los grupos /sp/ y /st/ y la acentuación en palabras de dos o más sílabas y compuestas, al presentar. Sirve para que la audiencia entienda mi mensaje y para que mi voz suene clara.",
    ["Sé reconocer la sílaba más fuerte de una palabra.", "Sé leer palabras comunes en inglés."],
    [
        "Para ser entendido (intelligible) no hace falta tener un acento perfecto, pero sí cuidar algunos sonidos. En /t/ y /d/ iniciales (to, do), la lengua toca detrás de los dientes de arriba; con /t/ sale un soplo de aire, y con /d/ vibra la garganta. El sonido /ʒ/ de usually, decision y television es suave, como una /sh/ con la garganta vibrando. En special, student y study, pronuncia /sp/ y /st/ sin una e antes.",
        "La acentuación es parte del significado. En las palabras de dos o más sílabas, una sílaba suena más fuerte: de-SIGN-er, de-CI-sion, TA-ble. En las palabras compuestas (compound words), el acento suele estar en la primera parte: NOTEbook, CLASSroom, BIRTHday. Si acentúas mal, la audiencia puede no reconocer la palabra.",
        "Las cualidades de la voz (voice qualities) también importan: volumen (que te escuchen desde el fondo), velocidad (no demasiado rápido), pausas (para respirar y marcar ideas) y entonación (subir y bajar para mostrar lo importante). Practica con un amigo y grábate. Escúchate y marca las palabras que debes mejorar.",
    ],
    [("intelligible", "comprensible"), ("volume", "volumen"), ("pace", "velocidad"), ("pause", "pausa"), ("intonation", "entonación"), ("compound word", "palabra compuesta")],
    [
        ("Sonido", "¿Qué palabra tiene /ʒ/? A) decision B) special", ["Pienso en el sonido suave.", "Decision tiene /ʒ/.", "Special tiene /sp/."], "A"),
        ("Acento", "¿Dónde va el acento en birthday? A) en birth B) en day", ["Es una palabra compuesta.", "El acento va en la primera parte.", "BIRTHday."], "A"),
    ],
    [
        ("Hablar demasiado rápido sin pausas.", "La audiencia no alcanza a entender.", "Haz pausas después de cada idea."),
        ("Decir «espesial» o «estudent».", "Se agrega una vocal inicial por influencia del español.", "Pronuncia /sp/ y /st/ juntos."),
    ],
    [
        ("Lee: " + SPEECH4 + " ¿Qué palabra tiene el sonido /ʒ/? A) usually B) special", "A", "Usually contiene el sonido /ʒ/."),
        ("Lee: " + SPEECH4 + " ¿Qué palabra comienza con el grupo /sp/? A) special B) student", "A", "Special empieza con sp."),
        ("Lee: " + SPEECH4 + " ¿Qué palabra comienza con el grupo /st/? A) student B) special", "A", "Student empieza con st."),
    ],
    [
        ("Lee: " + SPEECH4 + " ¿Qué sílaba lleva más fuerza en decision? A) la segunda B) la primera", "A", "Se pronuncia de-CI-sion."),
        ("Lee: " + SPEECH4 + " ¿Qué palabra de la oración contiene /d/ inicial? A) dinner B) station", "A", "Dinner empieza con /d/; station, con /st/."),
        ("Lee: " + SPEECH4 + " ¿Cuál de estas palabras comienza con /t/? A) take B) designer", "A", "Take empieza con /t/."),
    ],
    [
        ("Una estudiante habla muy bajo. ¿Qué cualidad debe mejorar? A) el volumen B) la velocidad", "A", "La audiencia no la escucha desde el fondo."),
        ("Un estudiante habla sin pausas. ¿Qué debe mejorar? A) las pausas B) el color de la diapositiva", "A", "Las pausas marcan ideas."),
        ("¿Cuál palabra compuesta lleva el acento en la primera parte? A) NOTEbook B) note-BOOK", "A", "Las compuestas suelen llevar el acento en la primera parte."),
    ],
    [
        ("Un compañero dice «espeak» en vez de speak. ¿Qué corrección corresponde? A) decir speak sin e inicial B) decir seak", "A", "En inglés /sp/ es un grupo inicial."),
        ("Una estudiante dice usually con /s/ como en sun. ¿Qué sonido debe usar? A) /ʒ/ como en television B) /t/ como en tie", "A", "Usually tiene /ʒ/."),
    ],
    [
        ("Une la palabra con su acento: 1) designer 2) birthday 3) decision. Acentos: a) BIRTH-day b) de-SIGN-er c) de-CI-sion", "1-b, 2-a, 3-c", "Designer: segunda; birthday: primera; decision: segunda."),
        ("Marca la frase con mejor entonación para sonar entusiasta: A) con voz fuerte, con subidas y bajadas B) con voz plana", "A", "La entonación variada transmite entusiasmo."),
    ],
    [("Lee: «Students study special subjects at the station school.» (subjects = asignaturas). ¿Cuántas palabras comienzan con /st/ o /sp/? Cuenta solo las que empiezan con esos grupos.", "4", "Students, study, special y station comienzan con /st/ o /sp/; subjects no.")],
    [
        ("¿Dónde va el acento en una palabra compuesta?", "Suele ir en la primera parte", "Se dice NOTEbook."),
        ("¿Qué cualidad de la voz ayuda a marcar lo importante?", "La entonación", "Sube y baja la voz."),
        ("¿Qué sonido tiene usually?", "/ʒ/", "Es un sonido suave."),
    ],
    task("Lee en voz alta, dos veces, esta frase a una persona de tu casa: «Usually, the student studies in the classroom after the special lesson.» Luego graba o repite y marca en tu hoja: las palabras con /ʒ/, /st/ y /sp/, la palabra compuesta con su acento, y una pausa. Después pide a la persona que anote qué palabra le costó más entender.", "Palabras: usually (/ʒ/), student y studies (/st/), special (/sp/), classroom (CLASSroom). Pausa posible: después de Usually.", ["identifica las palabras con cada sonido", "marca el acento de classroom", "comenta una mejora"], ["hoja con marcas", "nota de la persona que escuchó"], ["agregar una e inicial", "no hacer pausas"], "Repite la frase tres veces y pide a la persona que cuente cuántas veces entendió todo."),
    "Graba tu voz leyendo un párrafo corto y escucha para detectar tres sonidos por mejorar.",
    "Escribe cinco palabras compuestas y marca el acento en cada una.",
)

# ================================================== clase 5: audiencia, contexto y propósito
CONTEXT1 = "Situación A: presentarás a tu curso, de 40 compañeros, cómo usar bien el tiempo antes de una prueba. Tienes 3 minutos. Situación B: presentarás a un grupo de profesores y familias el proyecto de tu club de robótica. Tienes 5 minutos. Situación C: presentarás a tres compañeros, en grupo pequeño, un resumen de un cuento. Tienes 2 minutos."

lesson(
    OA, 5, MAT_SPEAK,
    "Aprenderé a tomar conciencia de la audiencia, el contexto y el propósito antes de presentar, y a adaptar mi mensaje, mi registro y mi tiempo. Sirve para que mi presentación sea apropiada y eficaz para cada situación.",
    ["Sé organizar una presentación con tres partes.", "Sé la diferencia entre registro formal e informal."],
    [
        "La audiencia (audience) es quien te escucha: compañeros, profesores, familias o un grupo pequeño. El contexto (context) es la situación: lugar, tiempo, equipo y ocasión. El propósito (purpose) es lo que quieres lograr: informar, convencer, entretener o explicar. Estas tres preguntas guían tus decisiones antes de preparar la presentación.",
        "Si tu audiencia son compañeros, puedes usar un tono más informal, ejemplos de tu vida diaria y una pregunta divertida. Si son profesores y familias, usa un tono formal (Good morning, ladies and gentlemen), un lenguaje más cuidado y datos claros. Si el grupo es pequeño, puedes conversar y mirar a cada persona. El tiempo disponible también decide cuántas ideas puedes incluir: con tres minutos, una o dos ideas; con cinco, tres ideas.",
        "Adaptar el mensaje significa elegir las palabras, los ejemplos y los recursos según quién te escucha. Pregúntate: ¿conoce el tema?, ¿qué necesita saber?, ¿qué le interesa? Si la audiencia es nueva en el tema, define las palabras difíciles. Al terminar, pide preguntas y agradece: Thank you for listening. Do you have any questions?",
    ],
    [("audience", "audiencia: quien escucha"), ("context", "contexto: situación"), ("purpose", "propósito: lo que quiero lograr"), ("formal", "formal: cuidado, para ocasiones serias"), ("informal", "informal: cercano, entre amigos"), ("Do you have any questions?", "¿Tienen preguntas?")],
    [
        ("Registro", "Hablas a profesores y familias. ¿Qué saludo conviene? A) Good morning, ladies and gentlemen. B) Hey, guys!", ["La audiencia es formal.", "Se usa un saludo cuidado.", "La A."], "A"),
        ("Tiempo", "Tienes 3 minutos para una presentación. ¿Cuántas ideas conviene incluir? A) una o dos B) diez", ["El tiempo es corto.", "Pocas ideas bien explicadas.", "La A."], "A"),
    ],
    [
        ("Usar el mismo tono para cualquier audiencia.", "No se adapta al contexto.", "Pregúntate quién te escucha antes de preparar."),
        ("Incluir demasiadas ideas en poco tiempo.", "La audiencia no alcanza a comprender.", "Ajusta el contenido al tiempo."),
    ],
    [
        (CONTEXT1 + " ¿Cuántos minutos tienes en la situación B? A) cinco B) tres", "A", "La situación B dice 5 minutos."),
        (CONTEXT1 + " ¿Cuántos compañeros hay en la situación A? A) cuarenta B) tres", "A", "La situación A menciona 40 compañeros."),
        (CONTEXT1 + " ¿Quiénes forman la audiencia de la situación B? A) profesores y familias B) compañeros del curso", "A", "Dice un grupo de profesores y familias."),
    ],
    [
        (CONTEXT1 + " ¿Qué situación pide un tono más formal? A) la B B) la C", "A", "La B incluye profesores y familias."),
        (CONTEXT1 + " ¿Cuál es el propósito en la situación C? A) resumir un cuento B) convencer a profesores", "A", "En C se resume un cuento."),
        (CONTEXT1 + " ¿En qué situación el grupo es más pequeño? A) la C B) la A", "A", "Son tres compañeros."),
    ],
    [
        (CONTEXT1 + " En la situación A, ¿qué recurso conviene? A) una pregunta divertida y un ejemplo cercano B) un discurso largo y formal", "A", "A compañeros se les habla con ejemplos cercanos."),
        (CONTEXT1 + " En la situación B, ¿qué datos conviene mostrar? A) un gráfico simple con resultados B) un chiste", "A", "El contexto formal pide datos claros."),
        (CONTEXT1 + " ¿Cuántos minutos tienes en la situación C? A) dos B) cinco", "A", "La situación C dice 2 minutos."),
    ],
    [
        (CONTEXT1 + " En la situación A, ¿cuántas ideas conviene incluir en 3 minutos? A) dos B) siete", "A", "Dos ideas se pueden explicar con ejemplos en el tiempo disponible."),
        (CONTEXT1 + " Un compañero planea usar el mismo texto formal para las tres situaciones. ¿Qué problema tiene? A) no se adapta a la audiencia ni al tiempo B) usa demasiado inglés", "A", "Cada situación tiene audiencia, contexto y propósito distintos."),
    ],
    [
        ("Ordena los pasos para preparar: a) elegir ideas, ejemplos y recursos b) pensar en la audiencia, el contexto y el propósito c) practicar con el tiempo", "b, a, c", "Primero se analiza la situación, luego se elige el contenido y después se practica."),
        ("¿Qué cierre es mejor para una audiencia formal? A) Thank you for listening. Do you have any questions? B) That’s all, bye!", "A", "Es cortés y abre un espacio para preguntar."),
    ],
    [("Una estudiante tiene que explicar a niños de 8 años cómo cuidar los libros. ¿Qué cambiaría? A) usaría palabras simples y dibujos B) usaría palabras difíciles", "A", "El lenguaje debe adecuarse a la edad.")],
    [
        ("¿Qué tres preguntas guían la preparación?", "Audiencia, contexto y propósito", "Orientan cada decisión."),
        ("¿Qué cierre es adecuado?", "Thank you for listening", "Es un cierre cortés."),
        ("¿Qué decide cuántas ideas incluir?", "El tiempo disponible", "Menos tiempo, menos ideas."),
    ],
    task("Elige una de las tres situaciones siguientes: A) 3 minutos a tu curso sobre cómo estudiar mejor, B) 5 minutos a profesores y familias sobre un proyecto de club, C) 2 minutos a tres compañeros sobre un cuento. Escribe una tarjeta con: tu audiencia, tu propósito, un saludo adecuado, dos ideas con ejemplos, un recurso multimodal y un cierre. Preséntala en voz alta a una persona de tu casa y mide el tiempo.", "Ejemplo (A): Audience: classmates. Purpose: to inform. Greeting: Hi, everyone. Ideas: make a plan; take breaks. Resource: a picture of a timetable. Closing: Thank you. Any questions?", ["identifica audiencia y propósito", "adapta registro, ideas y tiempo", "usa un recurso y un cierre apropiado"], ["tarjeta con la planificación", "comentario de la persona que escuchó"], ["usar un registro que no calza con la audiencia", "pasarse del tiempo"], "Pregunta a la persona que escuchó si la presentación calzaba con la audiencia y el tiempo."),
    "Observa una presentación y anota cómo adapta el mensaje a su audiencia.",
    "Prepara la misma presentación de 1 minuto para dos audiencias distintas y anota las diferencias.",
)
