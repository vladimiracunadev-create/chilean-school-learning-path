"""Cuaderno del estudiante, 1.º medio Inglés (propuesta), EN1M OA 08 (exposición oral multimodal con conciencia de audiencia).

Los textos, esquemas y datos son originales (los datos son «de ejemplo»). Las tareas abiertas se presentan ante una persona de tu casa.
"""
from __future__ import annotations

from student_content_en_m1_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA8 = "EN1M OA 08"
MATR = "Los esquemas, diapositivas descritas y textos escritos en cada ejercicio; lápiz, hojas y una persona de tu casa como audiencia."

# ================================================================ OA 08 · clase 1: audiencia, contexto y propósito
AUD = "Situaciones. S1: hablarás 3 minutos a niños de 8 años sobre reciclaje, en la sala, sin proyector. S2: hablarás 5 minutos a la directora para pedir bancas nuevas para el patio, con una presentación de 4 diapositivas. S3: hablarás 2 minutos a tus compañeros sobre tu pasatiempo, en una clase de Inglés. (recycling = reciclaje, principal = directora, benches = bancas, hobby = pasatiempo)"

lesson(
    OA8, 1, MATR,
    "Aprenderé a pensar en la audiencia, el contexto y el propósito antes de preparar una exposición oral. Sirve para elegir qué decir, con qué palabras y con qué apoyos para que tu mensaje funcione.",
    ["Sé presentar un tema en pocas frases.", "Sé el vocabulario de mi tema."],
    [
        "Una exposición oral (oral presentation) es un mensaje que se presenta ante un público. Tres preguntas guían su preparación. La audiencia (audience) responde «¿quiénes me escuchan?»: niños, autoridades o compañeros. El contexto (context) responde «¿dónde y cuánto tiempo tengo?»: sala sin proyector, 3 minutos. El propósito (purpose) responde «¿para qué hablo?»: informar, convencer o entretener.",
        "Esas tres respuestas cambian la exposición. Para niños de 8 años, usas frases cortas, palabras simples y un objeto o dibujo grande. Para la directora, usas un lenguaje formal (Good morning, Mrs. Ríos. I would like to ask...), datos concretos y una petición clara. Para compañeros, puedes usar un tono más cercano, pero con orden. Un mismo tema se presenta distinto según quién escucha.",
        "Antes de escribir tu guion, completa esta ficha: Audience: ____. Context: ____. Purpose: ____. Esa ficha te ayuda a decidir si necesitas datos, imágenes, ejemplos o humor. Una exposición bien pensada para la audiencia es más clara y más persuasiva.",
    ],
    [("audience", "audiencia: quienes escuchan"), ("context", "contexto: lugar, tiempo y situación"), ("purpose", "propósito: para qué hablo"), ("formal", "formal: respetuoso, con frases completas"), ("informal", "informal: cercano, entre amigos"), ("request", "petición")],
    [
        ("Ficha de planificación", AUD + " Completa la ficha para S1: audiencia, contexto y propósito.", ["Audiencia: niños de 8 años.", "Contexto: sala sin proyector, 3 minutos.", "Propósito: informar sobre reciclaje."], "Audiencia: niños de 8 años; contexto: sala sin proyector, 3 minutos; propósito: informar sobre reciclaje"),
        ("Elegir el tono", AUD + " Para S2 (la directora), ¿qué saludo es más adecuado: «Hey, give us benches!» o «Good morning, Mrs. Ríos. I would like to ask for new benches»?", ["La audiencia es una autoridad.", "Pedir bancas es una petición formal.", "El saludo respetuoso es el segundo."], "Good morning, Mrs. Ríos. I would like to ask for new benches"),
    ],
    [
        ("Preparar una sola exposición para cualquier público.", "No se piensa en quién escucha.", "Completa la ficha de audiencia, contexto y propósito antes de escribir."),
        ("Usar palabras difíciles con niños pequeños.", "Se piensa en lo que uno sabe, no en lo que ellos entienden.", "Usa frases cortas y ejemplos cercanos."),
    ],
    [
        (AUD + " En S3, ¿quiénes te escuchan? A) tus compañeros B) la directora", "A) tus compañeros", "S3 dice que hablarás a tus compañeros."),
        (AUD + " En S2, ¿cuántos minutos tienes?", "5", "S2 indica 5 minutos."),
        (AUD + " En S1, ¿qué apoyo no podrás usar? A) un proyector B) un dibujo grande", "A) un proyector", "S1 dice que no hay proyector."),
    ],
    [
        (AUD + " ¿Cuál es el propósito en S2? A) convencer a la directora de comprar bancas B) entretener a niños", "A) convencer a la directora de comprar bancas", "Pides un cambio, por lo tanto convences."),
        (AUD + " ¿Qué tipo de lenguaje conviene en S1? A) simple, con frases cortas B) técnico y con palabras raras", "A) simple, con frases cortas", "La audiencia son niños de 8 años."),
        (AUD + " ¿Cuál es el contexto de S3? A) una clase de Inglés de 2 minutos B) una reunión formal de 5 minutos", "A) una clase de Inglés de 2 minutos", "Lo dice la situación S3."),
    ],
    [
        (AUD + " En S2, ¿cuántas diapositivas planeas usar?", "4", "S2 dice una presentación de 4 diapositivas."),
        ("Une cada audiencia con su saludo. 1) niños de 8 años 2) directora 3) compañeros Saludos: a) Good morning, Mrs. Ríos. b) Hi, kids! c) Hello, everyone.", "1-b, 2-a, 3-c", "Cada saludo se ajusta a su público."),
        (AUD + " En S1 quieres mostrar cómo se separa el papel del plástico. ¿Qué apoyo conviene? A) dos cajas con dibujos grandes B) un gráfico con 20 cifras", "A) dos cajas con dibujos grandes", "Para niños pequeños sirve algo visual y simple."),
    ],
    [
        ("Un estudiante empieza S2 con «Hey, listen up!». ¿Qué problema tiene? A) es demasiado informal para una autoridad B) es muy largo", "A) es demasiado informal para una autoridad", "El registro no se ajusta a la audiencia."),
        (AUD + " Para S2, ¿qué dato fortalecería la petición? A) cuántos estudiantes hay en el patio durante el recreo (dato de ejemplo) B) cuántas bancas hay en la plaza del barrio", "A) cuántos estudiantes hay en el patio durante el recreo (dato de ejemplo)", "Un dato concreto apoya la solicitud."),
    ],
    [
        (AUD + " Si usas el mismo guion para S1 y S2, ¿qué ocurre probablemente? A) uno de los dos públicos no entenderá o se sentirá poco respetado B) funciona igual en los dos", "A) uno de los dos públicos no entenderá o se sentirá poco respetado", "Cada audiencia necesita un lenguaje y un tono distintos."),
        (AUD + " En S3, ¿qué propósito es más probable? A) informar y entretener con tu pasatiempo B) convencer de comprar algo", "A) informar y entretener con tu pasatiempo", "Es una clase y hablas de un pasatiempo."),
    ],
    [("Lees un aviso del colegio: «Dear parents, the meeting will be on Monday at six. Please confirm your attendance.» (parents = apoderados, attendance = asistencia). ¿Qué audiencia tiene el aviso?", "Apoderados (adultos)", "El saludo Dear parents lo muestra.")],
    [
        ("¿Qué tres cosas defines antes de preparar una exposición?", "Audiencia, contexto y propósito", "Orientan todas las decisiones."),
        ("¿Qué lenguaje usas con una autoridad?", "Formal", "Así se muestra respeto."),
        ("¿Qué significa purpose?", "Propósito: para qué hablo", "Define qué quiero lograr."),
    ],
    task("Completa la ficha para esta situación: presentarás 3 minutos a tus compañeros de curso un lugar de Chile que te gusta, con una lámina. Escribe en tu hoja: Audience, Context, Purpose y un saludo en inglés adecuado (por ejemplo, Good morning, everyone. Today I will talk about…).", "Audience: classmates. Context: classroom, 3 minutes, one poster. Purpose: inform and interest them. Saludo: Good morning, everyone. Today I will talk about a place I like.", ["completa las tres partes de la ficha", "el saludo se ajusta a la audiencia", "relaciona el apoyo con el contexto"], ["hoja con la ficha", "nota de la persona oyente"], ["dejar la ficha incompleta", "usar un saludo informal con una autoridad"], "Reconoce la ficha y ayuda a elegir un saludo más ajustado si no calza."),
    "Vuelve a leer las tres situaciones y escribe un saludo en inglés para cada una.",
    "Escribe en español una audiencia, un contexto y un propósito distintos de los de la clase para una exposición propia.",
)

# ---------------------------------------------------------------- clase 2: contenido y coherencia
NEIGH = "Guion de una exposición (ordenado al azar): 1) «To sum up, my neighborhood is quiet and friendly.» 2) «Good morning, everyone. Today I will talk about my neighborhood.» 3) «Second, there is a small market with fresh fruit.» 4) «Thank you for listening. Do you have any questions?» 5) «First, it has a big park where families play on weekends.» 6) «Third, the neighbors are friendly and help each other.» (neighborhood = barrio, park = parque, market = feria, fresh = fresca, neighbors = vecinos, each other = unos a otros, to sum up = en resumen)"

lesson(
    OA8, 2, MATR,
    "Aprenderé a organizar las ideas de una exposición con apertura, desarrollo y cierre, y a comprobar que cada idea se relaciona con el tema. Sirve para que tu exposición se entienda y muestre que conoces el contenido.",
    ["Sé que el orden de las ideas importa.", "Sé las palabras first, second, third."],
    [
        "Una exposición coherente tiene tres partes. En la apertura (opening) saludas, presentas el tema y dices el propósito: «Good morning, everyone. Today I will talk about my neighborhood». En el desarrollo (body) presentas entre dos y cuatro ideas, cada una con una palabra de orden (First, Second, Third) y un ejemplo o dato. En el cierre (closing) resumes con To sum up…, agradeces con Thank you for listening e invitas a preguntar.",
        "Coherencia (coherence) significa que todas las ideas se relacionan con el tema y siguen un orden lógico. Si en la exposición sobre el barrio aparece «My cousin likes pizza», esa idea no pertenece: se elimina o se conecta. El conocimiento del contenido (content knowledge) se nota en los ejemplos concretos y los datos correctos: «a small market with fresh fruit» es más claro que «there are things».",
        "Antes de exponer, escribe un esquema: tema, tres ideas y una frase de cierre. Léelo en voz alta y comprueba tres cosas: ¿cada idea tiene un ejemplo?, ¿están en orden?, ¿alguna idea sobra? Practicar con una persona de tu casa te muestra qué se entiende y qué no.",
    ],
    [("opening", "apertura: saludo, tema y propósito"), ("body", "desarrollo: ideas con ejemplos"), ("closing", "cierre: resumen y agradecimiento"), ("coherence", "coherencia: las ideas se relacionan y siguen un orden"), ("to sum up", "en resumen"), ("example", "ejemplo")],
    [
        ("Ordenar un guion", NEIGH + " ¿Cuál es el orden correcto de los números?", ["La apertura es la 2.", "Las ideas van First (5), Second (3) y Third (6).", "El cierre es 1 y luego 4."], "2, 5, 3, 6, 1, 4"),
        ("Idea que sobra", "En una exposición sobre el barrio, un estudiante incluye «My cousin likes pizza». ¿Esa idea pertenece al desarrollo?", ["El tema es el barrio.", "El gusto de un primo por la pizza no se relaciona.", "Debe eliminarse."], "No, porque no se relaciona con el barrio"),
    ],
    [
        ("Poner ideas sin orden ni palabras de orden.", "No se organiza el desarrollo.", "Usa First, Second y Third para ordenar."),
        ("Agregar una idea que no se relaciona.", "Se llena el tiempo sin pensar en la coherencia.", "Revisa que cada idea responda al tema."),
    ],
    [
        (NEIGH + " ¿Qué frase abre la exposición? A) Good morning, everyone. Today I will talk about my neighborhood. B) Thank you for listening.", "A) Good morning, everyone. Today I will talk about my neighborhood.", "Saluda y presenta el tema."),
        (NEIGH + " ¿Qué frase cierra la exposición? A) Thank you for listening. Do you have any questions? B) First, it has a big park.", "A) Thank you for listening. Do you have any questions?", "Agradece e invita a preguntar."),
        (NEIGH + " ¿Qué se vende en el mercado pequeño? A) fruta fresca B) ropa", "A) fruta fresca", "Dice a small market with fresh fruit."),
    ],
    [
        (NEIGH + " ¿Cuántas ideas tiene el desarrollo? A) tres B) dos", "A) tres", "Son First, Second y Third."),
        (NEIGH + " ¿Qué palabra introduce el resumen? A) To sum up B) Third", "A) To sum up", "Resume el mensaje final."),
        (NEIGH + " ¿Qué hacen las familias en el parque? A) juegan los fines de semana B) trabajan", "A) juegan los fines de semana", "Dice families play on weekends."),
    ],
    [
        ("Ordena con letras las partes de una exposición. A) closing B) body C) opening", "C, B, A", "Primero apertura, luego desarrollo y al final cierre."),
        (NEIGH + " ¿Qué idea del desarrollo habla de las personas? A) la tercera: los vecinos son amistosos B) la primera: el parque", "A) la tercera: los vecinos son amistosos", "Dice the neighbors are friendly and help each other."),
        ("Une cada idea con su ejemplo. 1) Fresh food 2) Friendly neighbors 3) Green spaces Ejemplos: a) a market with fruit b) a big park c) neighbors help each other", "1-a, 2-c, 3-b", "Cada ejemplo concreta la idea."),
    ],
    [
        ("Un estudiante dice: «First, my town has a beach. Second, I like football. Third, there is a lighthouse.» ¿Cuál idea no se relaciona con el tema «mi pueblo»? A) la segunda: I like football B) la primera: a beach", "A) la segunda: I like football", "El gusto personal no describe el pueblo."),
        (NEIGH + " ¿Qué parte falta si el estudiante omite To sum up? A) un resumen del mensaje B) el saludo", "A) un resumen del mensaje", "To sum up abre el cierre."),
    ],
    [
        (NEIGH + " Una persona del público pregunta: «Do the neighbors help each other?» ¿Qué respondes con tu guion? A) Yes, they do; the third idea says so B) No, they don't", "A) Yes, they do; the third idea says so", "El guion dice que los vecinos se ayudan."),
        ("Un estudiante empieza con «Today I will talk about my neighborhood» pero no dice su nombre ni saluda. ¿Qué mejora la apertura? A) agregar Good morning, everyone B) quitar el tema", "A) agregar Good morning, everyone", "La apertura lleva saludo y tema."),
    ],
    [("Una exposición dice: «First, plastic bottles are everywhere. Second, they take years to break down. Finally, we can use water bottles again.» (break down = descomponerse, again = de nuevo). ¿Qué conector abre la última idea?", "Finally", "Introduce la última idea.")],
    [
        ("¿Qué contiene la apertura?", "Saludo, tema y propósito", "Prepara a la audiencia."),
        ("¿Qué significa coherencia?", "Que las ideas se relacionan con el tema y siguen un orden", "Es la unidad del mensaje."),
        ("¿Qué frase puede abrir el cierre?", "To sum up", "Resume lo dicho."),
    ],
    task("Con este tema y estas ideas, arma el esquema de una exposición de 1 minuto: Tema: «My favorite sport». Ideas posibles: A) where I play it, B) who I play with, C) why I like it, D) my cousin's phone. En tu hoja escribe la apertura, tres ideas en orden (descarta una) con First/Second/Third y un cierre con To sum up.", "Apertura: Good morning. Today I will talk about my favorite sport. First, where I play it. Second, who I play with. Third, why I like it. Cierre: To sum up, I love this sport because it is fun. Thank you. Se descarta D.", ["descarta la idea que no pertenece", "usa First, Second y Third", "escribe apertura y cierre completos"], ["hoja con el esquema", "nota de la persona oyente"], ["incluir la idea del teléfono del primo", "olvidar el cierre"], "Valora el orden y revisa que cada idea tenga un ejemplo."),
    "Vuelve a ordenar el guion del barrio sin mirar la respuesta y compáralo con la solución.",
    "Escribe en español el esquema (apertura, tres ideas y cierre) de una exposición de 1 minuto sobre tu comida favorita.",
)

# ---------------------------------------------------------------- clase 3: recursos multimodales
BOT = "Datos de ejemplo: botellas plásticas recolectadas por curso: 1.º A 24, 1.º B 31, 1.º C 18. (bottles = botellas, collected = recolectadas)"
SLIDEA = "Diapositiva A: tiene un párrafo de 90 palabras en letra pequeña, sin imágenes y con tres colores de fondo distintos."
SLIDEB = "Diapositiva B: tiene el título «Plastic Bottles», un dibujo grande de una botella y tres palabras: collect, clean, reuse."

lesson(
    OA8, 3, MATR,
    "Aprenderé a reforzar el mensaje de una exposición con recursos multimodales: diapositivas, imágenes, gráficos, gestos y voz. Sirve para que la audiencia entienda y recuerde mejor tus ideas.",
    ["Sé organizar una exposición en tres partes.", "Sé leer una tabla de datos."],
    [
        "Un recurso multimodal (multimodal resource) es cualquier apoyo que usa más de un canal: lo que se ve (diapositivas, imágenes, gráficos, carteles), lo que se oye (la voz, las pausas) y lo que se hace (gestos, objetos). Un buen recurso refuerza tu mensaje, no lo repite palabra por palabra. Una diapositiva con un párrafo de 90 palabras obliga a leer y no a escuchar; en cambio, una con título, imagen grande y tres palabras clave acompaña lo que dices.",
        "Reglas útiles: una idea por diapositiva, letra grande, pocas palabras, una imagen relevante y colores con buen contraste. Un gráfico de barras sirve para comparar cantidades (cuántas botellas recolectó cada curso). Un diagrama sirve para mostrar un proceso. Las imágenes con rótulos sirven para enseñar vocabulario. La voz también es un recurso: habla con claridad, haz pausas y mira a la audiencia.",
        "Elige el recurso según lo que quieres mostrar: comparación, proceso, secuencia o vocabulario. Practica con tus recursos antes de la exposición, porque un recurso mal usado distrae. Y piensa en la audiencia: si hay niños pequeños, un objeto real o un dibujo grande funciona mejor.",
    ],
    [("multimodal", "que usa más de un canal: ver, oír, hacer"), ("slide", "diapositiva"), ("chart", "gráfico"), ("key word", "palabra clave"), ("gesture", "gesto"), ("contrast", "contraste de colores")],
    [
        ("Elegir la mejor diapositiva", SLIDEA + " " + SLIDEB + " ¿Cuál diapositiva funciona mejor y por qué?", ["La A tiene demasiado texto y letra pequeña.", "La B tiene título, imagen grande y tres palabras clave.", "La B acompaña lo que dices en vez de reemplazarlo."], "La B, porque tiene pocas palabras, una imagen grande y una idea clara"),
        ("Elegir un gráfico", BOT + " ¿Qué recurso sirve para comparar cuántas botellas recolectó cada curso?", ["Quiero comparar tres cantidades.", "Un gráfico de barras muestra cantidades lado a lado.", "Es el recurso más claro."], "Un gráfico de barras"),
    ],
    [
        ("Leer la diapositiva en voz alta.", "El recurso repite el texto y se pierde el contacto con la audiencia.", "Usa palabras clave y explica con tus propias palabras."),
        ("Usar muchos colores y textos en una sola diapositiva.", "Se piensa que más es mejor.", "Una idea por diapositiva y buen contraste."),
    ],
    [
        (BOT + " ¿Qué curso recolectó más botellas?", "1.º B, con 31", "Es el valor mayor de la tabla."),
        (BOT + " ¿Qué curso recolectó menos botellas?", "1.º C, con 18", "Es el valor menor de la tabla."),
        (SLIDEB + " ¿Cuántas palabras clave tiene? A) tres B) cinco", "A) tres", "Dice collect, clean y reuse."),
    ],
    [
        arith(BOT + " ¿Cuántas botellas recolectaron en total los tres cursos?", "24+31+18", "Se suman las tres cantidades."),
        (SLIDEA + " ¿Cuál es su principal problema? A) demasiado texto en letra pequeña B) tiene una imagen grande", "A) demasiado texto en letra pequeña", "El texto largo dificulta escuchar y leer a la vez."),
        arith(BOT + " ¿Cuántas botellas más recolectó 1.º B que 1.º C?", "31-18", "Se resta la cantidad menor de la mayor."),
    ],
    [
        ("Quieres mostrar el proceso de reciclaje paso a paso. ¿Qué recurso conviene? A) un diagrama con flechas B) un párrafo largo", "A) un diagrama con flechas", "Los diagramas muestran procesos."),
        ("Quieres enseñar las palabras bottle, bag y box a niños. ¿Qué recurso conviene? A) imágenes con rótulos B) un gráfico de barras", "A) imágenes con rótulos", "Asocian palabra e imagen."),
        ("Une cada necesidad con su recurso. 1) comparar cantidades 2) mostrar un proceso 3) enseñar vocabulario Recursos: a) diagrama b) gráfico de barras c) imágenes con rótulos", "1-b, 2-a, 3-c", "Cada recurso cumple una función distinta."),
    ],
    [
        (SLIDEB + " Durante la exposición, ¿qué gesto refuerza la imagen de la botella? A) mostrar la imagen con la mano y mirar a la audiencia B) darle la espalda a la audiencia", "A) mostrar la imagen con la mano y mirar a la audiencia", "El gesto dirige la atención y mantiene el contacto."),
        (BOT + " Un compañero dice que 1.º A recolectó más que 1.º B. ¿Cómo lo corriges con el gráfico? A) 1.º B recolectó 31 y 1.º A, 24 B) 1.º A recolectó 31", "A) 1.º B recolectó 31 y 1.º A, 24", "La tabla muestra lo contrario."),
    ],
    [
        (SLIDEA + " " + SLIDEB + " ¿Qué cambio mejoraría la diapositiva A? A) reducir el texto a tres palabras clave y agregar una imagen grande B) agregar más colores", "A) reducir el texto a tres palabras clave y agregar una imagen grande", "Se acerca al modelo de la diapositiva B."),
        ("Presentarás a niños de 8 años cómo se separa la basura. ¿Qué recurso sería mejor? A) tres cajas con dibujos grandes y objetos reales limpios B) una tabla con 30 cifras", "A) tres cajas con dibujos grandes y objetos reales limpios", "Es visual y concreto para esa edad."),
    ],
    [("Una diapositiva tiene el título «Our School Garden» y una foto grande. Una persona habla y la señala. ¿Qué dos canales se usan? A) ver y oír B) solo escribir", "A) ver y oír", "Se ve la foto y se oye la voz.")],
    [
        ("¿Qué es un recurso multimodal?", "Un apoyo que usa más de un canal, como ver y oír", "Refuerza el mensaje."),
        ("En Inglés: ¿Cuántas ideas lleva una diapositiva?", "Una", "Así no se sobrecarga."),
        ("¿Qué gráfico sirve para comparar cantidades?", "El gráfico de barras", "Muestra las cantidades lado a lado."),
    ],
    task("Con estos datos de ejemplo: gramos de basura por día en tu casa: lunes 300, martes 250, miércoles 400 (ficticios). Diseña en tu hoja una diapositiva para mostrar la comparación (dibuja un gráfico de barras con sus rótulos), escribe el título en inglés y tres palabras clave, y di en voz alta a una persona de tu casa una frase en inglés que acompañe el gráfico.", "Título: Our Trash this Week. Gráfico de barras con lunes 300, martes 250 y miércoles 400. Palabras clave: Monday, Tuesday, Wednesday. Frase: On Wednesday we had the most trash.", ["el gráfico representa los tres datos", "la diapositiva tiene título y pocas palabras", "la frase en inglés acompaña el gráfico"], ["dibujo del gráfico", "nota de la persona oyente"], ["escribir un párrafo largo en la diapositiva", "cambiar los datos"], "Valora la claridad del gráfico y ayuda a reducir el texto si hace falta."),
    "Vuelve a mirar la diapositiva A y escribe cómo la dibujarías con una imagen y tres palabras.",
    "Escribe en español dos gestos y dos pausas que usarías en una exposición.",
)

# ---------------------------------------------------------------- clase 4: funciones del lenguaje y vocabulario temático
FEST2 = "Datos del festival cultural (de ejemplo): lugar, el gimnasio; día, sábado; hora, 4 de la tarde; entradas, 2.000 pesos; voluntarios, 15; atracciones, danza, teatro y comida tradicional. (festival = festival, gym = gimnasio, volunteers = voluntarios, dance = danza, theater = teatro)"

lesson(
    OA8, 4, "Una tarjeta de datos y un guion de preguntas del público escritos en cada ejercicio; cada ejercicio cambia quién tiene el dato; lápiz y hoja.",
    "Aprenderé a usar funciones del lenguaje (abrir, ordenar, ejemplificar, resumir, agradecer, responder preguntas) y vocabulario del tema en una exposición. Sirve para hablar con claridad y manejar preguntas del público.",
    ["Sé organizar una exposición en tres partes.", "Sé el vocabulario básico del festival (stage, ticket, volunteers)."],
    [
        "En una exposición se usan frases fijas que cumplen funciones. Para abrir: Good morning, everyone. Today I'm going to talk about… Para ordenar: First…, Next…, Finally…. Para ejemplificar: For example… Para pasar a otra idea: Now let's move to… Para resumir: To sum up… Para agradecer: Thank you for listening. Para responder una pregunta: That's a good question. I think…",
        "El vocabulario temático (thematic vocabulary) son las palabras del tema. Para un festival: stage (escenario), ticket (entrada), volunteers (voluntarios), dance (danza), traditional food (comida tradicional), rehearsal (ensayo). Usar las palabras exactas muestra que conoces el tema y hace que tu mensaje sea más preciso que decir «cosas».",
        "Cuando alguien del público pregunta, escucha la pregunta, repite con tus palabras si no estás seguro y responde con un dato de tu tarjeta: «When is the festival?» → «The festival is on Saturday at four». Si no sabes, usa una frase honesta: «I'm not sure, but I can find out».",
    ],
    [("stage", "escenario"), ("ticket", "entrada"), ("volunteers", "voluntarios"), ("To sum up", "En resumen"), ("That's a good question", "Esa es una buena pregunta"), ("I'm not sure, but I can find out", "No estoy seguro, pero puedo averiguarlo")],
    [
        ("Responder una pregunta", FEST2 + " Una persona pregunta «How much is a ticket?». ¿Qué respondes en español y en inglés?", ["Busco el dato de las entradas: 2.000 pesos.", "Respondo en una oración completa.", "The ticket costs two thousand pesos."], "2.000 pesos: The ticket costs two thousand pesos"),
        ("Elegir la función", "La frase «To sum up, the festival has dance, theater and food» ¿qué función cumple? Elige: abrir, resumir o agradecer.", ["To sum up significa en resumen.", "La frase reúne las ideas principales.", "Cumple la función de resumir."], "Resumir"),
    ],
    [
        ("Responder «cosas» en lugar del vocabulario del tema.", "No se aprendió la palabra exacta.", "Usa stage, ticket, volunteers y otras palabras del tema."),
        ("Inventar una respuesta cuando no se sabe.", "Se evita decir «no sé».", "Di I'm not sure, but I can find out."),
    ],
    [
        (FEST2 + " ¿Dónde es el festival? A) en el gimnasio B) en la plaza", "A) en el gimnasio", "Dice lugar, el gimnasio."),
        (FEST2 + " ¿Qué palabra en inglés significa «escenario»? A) stage B) ticket", "A) stage", "Stage es escenario; ticket es entrada."),
        (FEST2 + " ¿Qué frase abre la exposición? A) Today I'm going to talk about the school festival. B) Thank you for listening.", "A) Today I'm going to talk about the school festival.", "Abre con saludo y tema."),
    ],
    [
        (FEST2 + " Una persona pregunta «When is the festival?». ¿Qué respondes? A) It is on Saturday at four. B) It is in the gym.", "A) It is on Saturday at four.", "Responde a When con día y hora."),
        (FEST2 + " ¿Qué palabra en inglés designa a las personas que ayudan sin recibir pago? A) volunteers B) tickets", "A) volunteers", "Voluntarios se dice volunteers."),
        (FEST2 + " ¿Qué atracciones hay? A) danza, teatro y comida tradicional B) fútbol y cine", "A) danza, teatro y comida tradicional", "Es lo que dice el dato de atracciones."),
    ],
    [
        ("Une cada función con su frase. 1) agradecer 2) ejemplificar 3) pasar a otra idea Frases: a) For example… b) Thank you for listening. c) Now let's move to…", "1-b, 2-a, 3-c", "Cada frase hace algo distinto en la exposición."),
        (FEST2 + " Alguien pregunta «How many volunteers are there?». ¿Cuál es la respuesta correcta? A) There are fifteen volunteers. B) There are five volunteers.", "A) There are fifteen volunteers.", "El dato dice voluntarios, 15."),
        (FEST2 + " Alguien pregunta «Is there food?». ¿Qué respondes con el dato? A) Yes, there is traditional food. B) No, there is only dance.", "A) Yes, there is traditional food.", "El dato incluye comida tradicional."),
    ],
    [
        (FEST2 + " Alguien pregunta «How many people will come?», dato que no tienes. ¿Qué respuesta es más honesta? A) I'm not sure, but I can find out. B) Exactly two hundred.", "A) I'm not sure, but I can find out.", "No se debe inventar un dato."),
        ("Elige la mejor oración para pasar del tema «atracciones» al tema «entradas». A) Now let's move to the tickets. B) Thank you for listening.", "A) Now let's move to the tickets.", "Now let's move to… cumple esa función."),
    ],
    [
        (FEST2 + " Un estudiante dice: «The festival is on Sunday». ¿Qué parte del dato lo corrige? A) el día es sábado B) el lugar es el gimnasio", "A) el día es sábado", "La tarjeta dice día, sábado."),
        arith(FEST2 + " Cinco amigos compran una entrada cada uno. ¿Cuántos pesos pagan en total?", "5*2000", "Se multiplica el valor de la entrada por cinco."),
    ],
    [("En una exposición oyes: «Now let's move to the second idea.» ¿Qué función cumple? A) pasar a otra idea B) agradecer", "A) pasar a otra idea", "Now let's move to… anuncia un cambio de idea.")],
    [
        ("¿Qué frase abre una exposición?", "Good morning, everyone. Today I'm going to talk about…", "Saluda y presenta el tema."),
        ("¿Cómo respondes si no sabes un dato?", "I'm not sure, but I can find out", "Es honesto y educado."),
        ("¿Qué es el vocabulario temático?", "Las palabras propias del tema", "Hacen más preciso el mensaje."),
    ],
    task("Con estos datos de ejemplo: «School book fair: library, Friday, 10 a.m., free entry, 20 volunteers, books for children and teenagers». (book fair = feria del libro, free entry = entrada gratis). Escribe en tu hoja una apertura de dos frases, una frase para pasar de una idea a otra, una respuesta a la pregunta «Is it free?» y un agradecimiento final.", "Good morning, everyone. Today I'm going to talk about the school book fair. Now let's move to the entry. Yes, it is free. Thank you for listening.", ["usa cuatro funciones del lenguaje", "usa al menos dos palabras del tema", "responde con un dato de la ficha"], ["hoja con las cuatro frases", "nota de la persona oyente"], ["no usar vocabulario del tema", "inventar datos"], "Valora las funciones usadas y ayuda a precisar el vocabulario."),
    "Vuelve a leer las frases del festival y subraya las que sirven para abrir, ordenar y cerrar.",
    "Escribe en español tres preguntas que el público podría hacer sobre un festival y cómo las responderías con una tarjeta de datos.",
)

# ---------------------------------------------------------------- clase 5: sonidos y práctica
TALK5 = "«Good afternoon. Today I will talk about my vacation. Last year my family took a train from the station to a town in the south. We had a yellow tent near a big tree. At the information office, they gave us a map. The weather was nice, so we could swim. It was the best trip of the year.» (vacation = vacaciones, station = estación, tent = carpa, information office = oficina de informaciones, weather = clima, swim = nadar, trip = viaje)"

lesson(
    OA8, 5, MATR,
    "Aprenderé a usar con claridad los sonidos del inglés en una exposición: vocales largas y cortas (feet/fit), tr y dr (tree/dress), el sonido inicial /j/ (year, yes) y el final -tion (vacation). Sirve para que la audiencia te entienda y para evitar cambiar el significado de una palabra.",
    ["Sé que los sonidos del inglés pueden distinguir palabras.", "Sé leer una exposición corta."],
    [
        "Cuatro grupos de sonidos suelen causar confusiones. Vocal larga /iː/ (feet, sheep, seat) frente a vocal corta /ɪ/ (fit, ship, sit): cambia el significado, como oveja y barco. Tr y dr al comienzo de palabra (tree, train, dress, drink) se pronuncian casi como «chr» y «jr»; no separes la t o la d de la r. El sonido inicial /j/ de year y yes se parece a la y de «yo». El final -tion suena «shən»: vacation, station, information.",
        "En una exposición, estos sonidos se notan más en las palabras clave. Prepárate marcando en tu guion las palabras difíciles y practicándolas despacio. Si pronuncias ship cuando querías decir sheep, tu audiencia entenderá otra cosa. Graba o pide a una persona de tu casa que te escuche y te diga qué palabras suenan confusas.",
        "Practica en tres pasos: 1) lee en voz alta solo las palabras difíciles; 2) lee la frase completa; 3) lee todo el guion con ritmo, haciendo pausas. Si cometes un error, corrígete y sigue: autocorregirse es parte de hablar bien.",
    ],
    [("long vowel", "vocal larga: feet"), ("short vowel", "vocal corta: fit"), ("tr / dr", "tree suena «chri»; dress suena «jres»"), ("/j/", "sonido de year y yes"), ("-tion", "suena «shən»: vacation"), ("pause", "pausa")],
    [
        ("Clasificar sonidos", TALK5 + " ¿Qué palabras del guion terminan en -tion? Escribe las tres.", ["Busco palabras que terminen en -tion.", "Encuentro vacation, station e information.", "Las tres suenan shən al final."], "Vacation, station e information"),
        ("Sonido inicial", TALK5 + " ¿Qué palabras del guion empiezan con el sonido /j/? Escríbelas.", ["Busco palabras con y al inicio: yellow, year.", "Esas dos empiezan con el sonido /j/.", "Son year y yellow."], "Year y yellow"),
    ],
    [
        ("Pronunciar tion con t.", "Se lee como en español.", "Recuerda que -tion suena shən."),
        ("Decir sheep y ship igual.", "Se usa una sola i del español.", "Alarga la vocal en sheep y hazla breve en ship."),
    ],
    [
        (TALK5 + " ¿Qué palabra del guion tiene el sonido tr al comienzo? A) train B) south", "A) train", "Train empieza con tr."),
        (TALK5 + " ¿Qué palabra tiene vocal larga? A) tree B) map", "A) tree", "Tree lleva ee y su vocal es larga."),
        (TALK5 + " ¿De qué color era la carpa? A) amarilla B) roja", "A) amarilla", "El guion dice a yellow tent."),
    ],
    [
        ("Un adulto te lee dos palabras: «sheep» y «ship». ¿Cuál tiene la vocal corta? A) ship B) sheep", "A) ship", "Ship lleva i breve; sheep lleva ee larga."),
        ("¿Cuál de estas palabras comienza con el sonido /j/? A) year B) jet", "A) year", "Year empieza con /j/; jet con /dʒ/."),
        ("¿Cómo suena la combinación inicial de «dress»? A) como «jr» B) como «tr»", "A) como «jr»", "Dr suena parecido a jr."),
    ],
    [
        ("Clasifica según la vocal: seat, sit, feet, fit. Escribe las que tienen vocal larga y las que tienen vocal corta.", "Largas: seat, feet. Cortas: sit, fit", "Ea y ee dan el sonido largo; i sola da el corto."),
        (TALK5 + " ¿Qué palabra del guion tiene vocal corta, como fit? A) trip B) tree", "A) trip", "Trip lleva una i breve; tree lleva ee, que es larga."),
        ("Une cada sonido con su palabra de ejemplo. 1) vocal larga 2) tr 3) /j/ Palabras: a) tree b) feet c) yes", "1-b, 2-a, 3-c", "Feet tiene vocal larga, tree empieza con tr y yes con /j/."),
    ],
    [
        ("Quieres decir «barco» y dices sheep. ¿Qué entenderá tu audiencia? A) oveja B) barco", "A) oveja", "Sheep significa oveja; la vocal larga cambia el significado."),
        (TALK5 + " ¿Cuántas palabras del guion empiezan con tr?", "3", "Son train, tree y trip."),
    ],
    [
        (TALK5 + " Un estudiante lee «station» con t al final. ¿Cómo lo corriges? A) se dice «stei-shən» B) se dice «stei-tion»", "A) se dice «stei-shən»", "El final -tion suena shən."),
        ("Un estudiante dice «jear» en vez de year. ¿Qué sonido debe cambiar? A) el inicial, que debe ser /j/ B) el final", "A) el inicial, que debe ser /j/", "Year empieza con /j/, como la y de yo."),
    ],
    [("Lees en voz alta: «We took a train near a tree.» (took = tomamos). ¿Qué dos palabras empiezan con tr?", "train y tree", "Las dos empiezan con tr.")],
    [
        ("¿Cómo suena el final de vacation?", "«shən»", "Es la pronunciación de -tion."),
        ("¿Qué sonido empieza year?", "/j/, como la y de yo", "No es jet."),
        ("¿Qué haces si te equivocas al hablar?", "Me corrijo y sigo", "Autocorregirse es parte de hablar bien."),
    ],
    task("Lee en voz alta, frente a una persona de tu casa, este guion original: «Good morning. This year I visited a train station. There was a tree near the entrance. Yesterday I read the information board. Then I drank a drink and sat on a seat.» (entrance = entrada, board = panel). En tu hoja marca: las palabras con -tion, con tr, con dr y con /j/, y una palabra con vocal larga.", "Con -tion: station, information. Con tr: train, tree. Con dr: drank, drink. Con /j/: year, yesterday. Vocal larga: seat o tree.", ["marca cada grupo correctamente", "lee con la persona y pide que oiga los sonidos", "se autocorrige si se equivoca"], ["hoja con palabras marcadas", "nota de la persona oyente"], ["pronunciar tion con t", "separar la t o la d de la r"], "Valora los sonidos logrados y practica solo los difíciles tres veces más."),
    "Vuelve a leer el guion de las vacaciones y marca las palabras con -tion y con /j/.",
    "Escribe en español tres palabras del inglés que te cuesten pronunciar y cómo las practicarás.",
)
