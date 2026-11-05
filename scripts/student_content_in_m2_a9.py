"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 09: ideas generales e información explícita en textos impresos o digitales.

Todos los textos están escritos en el enunciado (originales; los datos de ejemplo se rotulan «fictional»). Inglés americano.
Los títulos de clase del plan son genéricos; aquí se aplican a temas de interés, temas de otras asignaturas, contexto
inmediato y actualidad, otras culturas y temas globales, y temas menos conocidos con palabras nuevas.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 09"

# ------------------------------------------------------------------ clase 1: temas de interés
B1 = "«Blog post (fictional): My First Month of Skateboarding. Last month, I joined a skate club at the park. At first, I fell a lot, and my knees hurt. Now I have been skating three times a week, and I can ride down the small ramp. We always wear helmets and pads. The best part is the friendly group: neither my coach nor my classmates ever laugh at mistakes.» (blog post = publicación de blog, skateboarding = andar en skate, club = club, fell = me caí, knees = rodillas, hurt = dolían, ride down = bajar, ramp = rampa, helmets and pads = casco y protecciones, laugh = reírse, mistakes = errores)"
B2 = "«Forum post (fictional): Which phone camera apps do you use? Tomás: I mostly use the basic one. It is easy and free. Lía: I rarely use the basic one. I prefer an app with filters, though it takes more space. Tomás: Good point. I have little space on my phone.» (forum = foro, apps = aplicaciones, mostly = sobre todo, easy = fácil, filters = filtros, space = espacio)"
B3 = "«Guide (fictional): How to Start a Sketchbook. First, choose a topic you like. Second, write a list of three things to draw. Third, draw a quick test page. Finally, look at it and fix the lines you do not like. You only need a notebook and a pencil.» (guide = guía, sketchbook = cuaderno de dibujo, topic = tema, quick = rápida, test page = página de prueba, fix = mejorar, lines = líneas, notebook = cuaderno)"

lesson(
    OA, 1, MAT_R,
    "Aprenderé a leer textos impresos o digitales sobre temas de interés (publicaciones de blog, foros, guías) y a identificar su idea general y la información explícita. Sirve para comprender lo que me interesa y responder con datos del texto.",
    ["Sé leer textos cortos en inglés.", "Conozco palabras como first, then y finally."],
    [
        "La idea general (main idea) de un texto es lo más importante que dice. Para encontrarla, lee el título, la primera y la última oración y pregunta de qué trata todo el texto. Los textos de interés, como un blog o un foro, suelen tener una voz personal y mezclar hechos con opiniones. La información explícita (explicit information) es la que el texto dice con palabras claras: nombres, números, lugares, frecuencias y acciones.",
        "Para ubicar un dato explícito, lee primero la pregunta y busca palabras clave en el texto (scanning). Cuando encuentres el pasaje, relee con calma y comprueba que responde exactamente lo que se pregunta. Si hay dos datos parecidos, como three times a week y three months, fíjate en la unidad.",
        "En estos textos aparecen funciones del año: cantidades (little space, a few), frecuencia (rarely, three times a week), acciones que continúan (I have been skating), conectores (though, neither ... nor). Reconocerlos te ayuda a entender qué dice el autor y cómo lo dice.",
    ],
    [("main idea", "idea general"), ("explicit information", "información dicha con palabras claras"), ("scanning", "buscar un dato puntual"), ("blog post / forum", "publicación de blog / foro"), ("have been skating", "llevo andando en skate"), ("rarely", "rara vez")],
    [
        ("Idea general de un blog", B1 + " ¿Cuál es la idea general?", ["El título dice My First Month of Rock Climbing.", "El autor cuenta cómo mejoró y lo que le gusta.", "La idea es que empezó a escalar, mejoró y le gusta el grupo."], "Empezó a andar en skate, mejoró con la práctica y le gusta el grupo"),
        ("Dato explícito", B3 + " ¿Qué necesitas para empezar un cuaderno de dibujo?", ["Busco la frase You only need.", "Dice a notebook and a pencil.", "Respondo con esos dos datos."], "Un cuaderno y un lápiz"),
    ],
    [
        ("Responder con la opinión del lector y no con el texto.", "La pregunta pide lo que dice el texto.", "Vuelve al pasaje y copia el dato."),
        ("Confundir three times a week con three months.", "No se mira la unidad de tiempo.", "Mira la unidad: week o month."),
    ],
    [
        mr(B1, "¿Cuántas veces por semana practica skate el autor?", "Tres veces", ["Una vez", "Todos los días"], "Dice three times a week."),
        mr(B3, "¿Cuál es el primer paso?", "Elegir un tema que te guste", ["Dibujar una página de prueba", "Comprar lápices de colores"], "Dice First, choose a topic you like."),
        mr(B2, "¿Qué app prefiere Lía?", "Una con filtros", ["La básica", "Ninguna"], "Dice I prefer an app with filters."),
    ],
    [
        mr(B1, "¿Qué fue lo mejor, según el autor?", "El grupo amistoso", ["Las rampas más altas", "El parque nuevo"], "Dice The best part is the friendly group."),
        mr(B2, "¿Por qué Tomás usa la app básica?", "Porque es fácil, gratis y tiene poco espacio en el teléfono", ["Porque tiene muchos filtros", "Porque no tiene teléfono"], "Dice It is easy and free y I have little space."),
        mr(B3, "¿Cuántas cosas para dibujar se escriben en la lista?", "Tres", ["Dos", "Cinco"], "Dice a list of three things to draw."),
    ],
    [
        mr(B1, "¿Cuál es la oración verdadera?", "Ni el entrenador ni los compañeros se ríen de los errores", ["El autor bajó la rampa más difícil del parque", "El autor practica skate solo los domingos"], "Dice neither my coach nor my classmates ever laugh at mistakes."),
        mr(B2, "¿Qué app ocupa más espacio según el foro?", "La que tiene filtros", ["La básica", "Ninguna ocupa espacio"], "Lía dice it takes more space."),
        mr(B3, "¿Qué paso va después de dibujar la página de prueba?", "Mirarla y mejorar las líneas que no te gustan", ["Elegir otra vez el tema y escribir una nueva lista", "Comprar otro cuaderno y empezar la guía desde cero"], "Finally, look at it and fix the lines you do not like."),
    ],
    [
        mr(B1, "Un compañero dice que el autor practica skate desde hace un año. ¿Qué dato lo contradice?", "Dice Last month, I joined: empezó el mes pasado", ["Dice At first, I fell a lot: se cayó al principio", "Dice I can ride down the small ramp: ya baja la rampa"], "El texto menciona un mes, no un año."),
        mr(B2, "¿Quién usa más veces la app básica?", "Tomás", ["Lía", "Los dos por igual"], "Tomás dice que la usa casi siempre (mostly) y Lía dice que rara vez la usa."),
    ],
    [
        mr(B1, "¿Cuál es la idea general del texto?", "Que mejoró y que valora el apoyo del grupo", ["Que odia las rampas y piensa dejar el skate", "Que se aburrió del club y quiere cambiarse"], "Resume la progresión y lo mejor."),
        mr(B3, "¿Qué opinión del autor aparece en el texto?", "Una guía: usa First, Second, Third y Finally para ordenar pasos", ["Un foro: dos personas conversan y dan opiniones sobre apps", "Un blog: el autor cuenta lo que le pasó el mes pasado"], "Es una guía con pasos, no un texto de opinión."),
    ],
    [arith("El autor practica skate 3 veces por semana durante 4 semanas. ¿Cuántas veces practica en ese tiempo?", "3*4", "Se multiplica la frecuencia semanal por el número de semanas.", " veces")],
    [
        ("En Inglés de 2.º medio (OA 9, clase 1): ¿qué es la idea general?", "Lo más importante que dice el texto", "Resume el texto completo."),
        ("En Inglés de 2.º medio (OA 9, clase 1): ¿qué es scanning?", "Buscar un dato puntual", "Se busca una palabra clave."),
        ("En Inglés de 2.º medio (OA 9, clase 1): ¿qué es información explícita?", "La que el texto dice con palabras claras", "No hay que deducirla."),
    ],
    task("Lee: «Post (fictional): My Sunday Hobby. I usually go to the park on Sundays and sketch the trees. I have been drawing for two years. Few people draw there, though. Sometimes a neighbor sits with me, and we talk about our work.» (sketch = dibujar a lápiz, trees = árboles, sits = se sienta, work = trabajos). En inglés o español, escribe: la idea general, dos datos explícitos y una función del año que reconoces (cantidad, frecuencia o have been).", "Idea general: la autora dibuja árboles en el parque los domingos. Datos: lleva dos años dibujando; a veces la acompaña un vecino. Función: have been drawing (acción que continúa).", ["escribe la idea general", "da dos datos explícitos", "reconoce una función del año"], ["hoja con tres respuestas"], ["responder con una opinión", "confundir años con semanas"], "Pide que cite la frase exacta de cada dato."),
    "Elige un blog o un foro en inglés de un tema que te guste y lee solo el título y la primera oración. ¿De qué crees que trata?",
    "Cuenta en español la idea general del texto de skate en una oración.",
)

# ------------------------------------------------------------------ clase 2: temas de otras asignaturas
SC = "«Tides (science article). Tides are the rise and fall of the sea. They happen mostly because of the pull of the Moon's gravity. In many places, there are two high tides and two low tides each day. The Sun also has a smaller effect.» (tides = mareas, rise = subida, fall = bajada, pull = atracción, gravity = gravedad, high tide = marea alta, low tide = marea baja, effect = efecto)"
MT = "«Percentages (math text). A percentage shows a part of 100. If a shirt costs 20,000 pesos and has a 10% discount, you pay 18,000 pesos. A 50% discount means half the price.» (percentage = porcentaje, part = parte, discount = descuento, half = la mitad)"
GE = "«Map scale (geography text). A scale of 1:100,000 means that 1 centimeter on the map is 1 kilometer in real life. On a map with this scale, two towns that are 5 centimeters apart are 5 kilometers apart.» (scale = escala, real life = la realidad, apart = separadas)"
AR = "«Color wheel (art text). The primary colors are red, yellow and blue. If you mix red and yellow, you get orange. If you mix yellow and blue, you get green. Neither orange nor green is a primary color.» (color wheel = círculo cromático, primary = primario, mix = mezclas)"

lesson(
    OA, 2, MAT_R,
    "Aprenderé a leer textos breves de otras asignaturas (Ciencias, Matemática, Geografía, Artes) y a identificar su idea general e información explícita. Sirve para aprender contenidos en inglés y usar lo que sé de otras materias.",
    ["Sé leer datos y números en inglés.", "Conozco palabras como cost, half y part."],
    [
        "Los textos de otras asignaturas explican un concepto. Suelen tener una definición (Tides are the rise and fall of the sea), una causa (because of), un ejemplo (If a shirt costs...) y una regla (A scale of 1:100,000 means...). Para encontrar la idea general, pregunta: ¿qué concepto explica y qué dice de él?",
        "Para la información explícita, busca los términos clave de la asignatura, los números y las palabras de relación como because, if, means y neither ... nor. Usa lo que sabes de la asignatura: si en Matemática conoces los porcentajes, entenderás mejor 10% discount. Los conocimientos previos ayudan a deducir palabras que no conoces.",
        "En estos textos también aparecen las funciones del año: cantidades (two high tides each day), grados (a smaller effect), condiciones (If you mix red and yellow) y conectores (neither ... nor). Marca la definición, la causa y el ejemplo con colores distintos.",
    ],
    [("definition", "definición"), ("cause", "causa"), ("example", "ejemplo"), ("percentage / discount", "porcentaje / descuento"), ("scale", "escala"), ("primary colors", "colores primarios")],
    [
        ("Definición y causa", SC + " ¿Qué son las mareas y por qué ocurren?", ["Busco la definición: the rise and fall of the sea.", "Busco la causa: mostly because of the pull of the Moon's gravity.", "Respondo con ambas."], "La subida y bajada del mar; ocurren sobre todo por la atracción de la gravedad de la Luna"),
        ("Aplicar una regla", GE + " ¿Cuántos kilómetros separan dos pueblos que están a 5 centímetros en el mapa?", ["La escala dice 1 cm es 1 km.", "5 cm representan 5 km.", "Están a 5 kilómetros."], "5 kilómetros"),
    ],
    [
        ("Leer 1:100,000 como cien mil kilómetros por centímetro.", "La escala compara medidas distintas: centímetros en el mapa con la realidad.", "Usa la equivalencia que da el texto: 1 cm es 1 km."),
        ("Confundir 10% con la mitad.", "La mitad es 50%, no 10%.", "Busca la frase half the price."),
    ],
    [
        mr(SC, "¿Cuántas mareas altas hay en muchos lugares cada día?", "Dos", ["Una", "Cuatro"], "Dice two high tides and two low tides each day."),
        mr(AR, "¿Qué color resulta de mezclar rojo y amarillo?", "Anaranjado", ["Verde", "Azul"], "Dice If you mix red and yellow, you get orange."),
        mr(MT, "¿Qué significa un descuento de 50%?", "La mitad del precio", ["El doble del precio", "Un décimo del precio"], "Dice A 50% discount means half the price."),
    ],
    [
        mr(SC, "¿Qué efecto tiene el Sol en las mareas?", "Un efecto menor que el de la Luna", ["Ningún efecto en las mareas", "Es la causa principal de las mareas"], "Dice The Sun also has a smaller effect."),
        arith("Una polera cuesta 20.000 pesos y tiene un descuento del 10%, que son 2.000 pesos. ¿Cuántos pesos se pagan?", "20000-2000", "Al precio se le resta el descuento de 2.000 pesos.", " pesos"),
        mr(AR, "¿Cuáles son los colores primarios?", "Rojo, amarillo y azul", ["Rojo, verde y naranja", "Amarillo, verde y violeta"], "Dice The primary colors are red, yellow and blue."),
    ],
    [
        mr(GE, "¿Qué significa una escala de 1:100,000?", "1 centímetro del mapa son 1 kilómetro reales", ["1 metro del mapa son 100 kilómetros reales", "1 kilómetro del mapa es 1 centímetro en la realidad"], "Es la equivalencia que da el texto."),
        mr(AR, "¿Cuál es verdadera según el texto?", "Ni el naranja ni el verde son colores primarios", ["Todos los colores son primarios", "El verde es primario"], "Dice Neither orange nor green is a primary color."),
        mr(GE, "En un mapa con esta escala, dos pueblos están a 8 centímetros. ¿A cuántos kilómetros reales están?", "8 kilómetros", ["80 kilómetros", "800 kilómetros"], "Cada centímetro del mapa representa un kilómetro."),
    ],
    [
        mr(SC, "Un estudiante dice que las mareas ocurren solo por el Sol. ¿Qué dato lo contradice?", "El texto dice que ocurren sobre todo por la Luna", ["El texto no menciona el Sol", "El texto dice que no existen"], "Dice mostly because of the pull of the Moon's gravity."),
        mr(MT, "Otro estudiante dice que un descuento de 10% en una polera de 20.000 pesos sale a 10.000 pesos. ¿Qué respuesta es más acertada?", "No: se paga 18.000 pesos, porque el descuento es 2.000", ["Sí: se paga 10.000 pesos, porque el descuento es 10.000", "Sí: se paga 20.000 pesos, porque el descuento no se aplica"], "El 10% de 20.000 es 2.000."),
    ],
    [
        mr(AR, "¿Cuál de estas ideas resume el texto del círculo cromático?", "Con colores primarios se forman colores como naranja y verde", ["Los colores primarios son verdes", "El rojo se forma mezclando verde y azul"], "El texto explica mezclas."),
        mr(GE, "¿Cuál es la idea general del texto de geografía?", "Cómo leer distancias en un mapa con escala", ["Cómo se dibuja una montaña", "Cuál es el pueblo más grande"], "Explica la equivalencia de la escala."),
    ],
    [mr(SC + " " + MT, "Los dos textos explican algo con un dato numérico. ¿Cuál tiene un dato de frecuencia por día?", "El de las mareas: dos altas y dos bajas", ["El de porcentajes, que habla de descuentos", "Ninguno de los dos habla de frecuencia diaria"], "Dice two high tides and two low tides each day.")],
    [
        ("En Inglés de 2.º medio (OA 9, clase 2): ¿qué partes suele tener un texto de otra asignatura?", "Definición, causa, ejemplo y regla", "Ayudan a ubicar la información."),
        ("En Inglés de 2.º medio (OA 9, clase 2): ¿qué conocimiento ayuda a entender 10% discount?", "El de porcentajes de Matemática", "Los conocimientos previos facilitan entender."),
        ("En Inglés de 2.º medio (OA 9, clase 2): ¿qué significa half the price?", "La mitad del precio", "Half es la mitad."),
    ],
    task("Lee: «Seasons (science text). Chile is in the Southern Hemisphere. In January, it is summer in Chile because the Southern Hemisphere is tilted toward the Sun. In July, it is winter. When it is summer in Chile, it is winter in the Northern Hemisphere.» (seasons = estaciones, hemisphere = hemisferio, tilted = inclinado, toward = hacia). Escribe la idea general, dos datos explícitos y una conexión con lo que sabes de Ciencias o Geografía.", "Idea general: las estaciones dependen de la inclinación de la Tierra respecto al Sol. Datos: en enero es verano en Chile; en julio es invierno. Conexión: en Geografía vimos hemisferios.", ["escribe la idea general", "da dos datos explícitos", "conecta con otra asignatura"], ["hoja con tres respuestas"], ["inventar datos que no están", "olvidar la conexión"], "Pide que explique por qué es invierno en el hemisferio norte en enero."),
    "Lee en inglés un título de un texto de Ciencias y predice de qué trata.",
    "Busca en tu cuaderno de otra asignatura un término y escríbelo en inglés con su definición.",
)

# ------------------------------------------------------------------ clase 3: contexto inmediato y actualidad
BU = "«School bulletin: The art fair will take place on Thursday in the gym. Students must bring their projects by 8 a.m. Parents can visit between 2 and 4 p.m. A few places are still available for new projects. Sign up at the office by Monday.» (bulletin = boletín, art fair = feria de arte, gym = gimnasio, bring = traer, parents = apoderados, places = cupos, available = disponibles, sign up = inscribirse, office = secretaría)"
LN = "«Neighborhood Library Extends Hours (fictional). The Santa Rosa library will now stay open until 8 p.m. from Monday to Thursday. The Saturday and Sunday hours have not changed. The library made the change after many students asked for more study time.» (extends = amplía, hours = horario, stay open = permanecer abierta, asked = pidieron, study time = tiempo de estudio)"
HW = "«Heat Waves in Cities (article, fictional). When the temperature stays very high for several days, it is called a heat wave. Cities can be hotter than nearby fields because buildings and roads keep heat. As a result, some city councils open cooling centers and plant more trees.» (heat wave = ola de calor, nearby = cercanos, fields = campos, roads = calles, keep = retienen, city councils = municipalidades, cooling centers = centros de enfriamiento, plant = plantar)"
WB = "«Website notice (fictional). Our online store will be closed for maintenance on Saturday, from midnight to 6 a.m. You can still read the catalog, but you cannot buy. We are sorry about this inconvenience.» (store = tienda, maintenance = mantención, midnight = medianoche, catalog = catálogo, inconvenience = inconveniente)"

lesson(
    OA, 3, MAT_R,
    "Aprenderé a leer textos de mi contexto inmediato y de actualidad (boletines, noticias, avisos de sitios web) y a identificar su idea general e información explícita. Sirve para enterarme de lo que ocurre a mi alrededor.",
    ["Sé leer avisos y noticias cortas.", "Conozco fechas, horas y verbos modales."],
    [
        "Los textos del contexto inmediato informan algo cercano: un boletín escolar, un aviso de una biblioteca, una nota de un sitio web. Responden a las preguntas who, what, where y when, y suelen incluir una acción que debes hacer, como Sign up at the office by Monday. Las noticias de actualidad explican un hecho reciente y su causa o consecuencia: Cities can be hotter... As a result, some city councils open cooling centers.",
        "Para encontrar la idea general, lee el título y la primera oración. Para la información explícita, busca fechas, horas, lugares y condiciones: until 8 p.m., from Monday to Thursday, between 2 and 4 p.m. Cuidado con las limitaciones: You can still read the catalog, but you cannot buy; la palabra but marca un contraste que cambia lo que puedes hacer.",
        "También reconoce funciones del año: cantidad (a few places), tiempo (now, will, by Monday), consecuencia (as a result) y cortesía (we are sorry about this inconvenience). En una noticia, distingue el hecho de la opinión.",
    ],
    [("bulletin / notice", "boletín / aviso"), ("sign up", "inscribirse"), ("by Monday", "a más tardar el lunes"), ("between 2 and 4", "entre las 2 y las 4"), ("as a result", "como resultado"), ("sorry about", "lamento lo de")],
    [
        ("Idea general y acción", BU + " ¿Cuál es la idea general y qué debes hacer para presentar un proyecto?", ["La idea es informar sobre la feria de arte.", "Quedan algunos cupos y hay que inscribirse.", "Sign up at the office by Monday."], "Informar la feria de arte; para participar, inscribirse en secretaría antes del lunes"),
        ("Hecho y consecuencia", HW + " ¿Por qué las ciudades pueden ser más calientes que los campos?", ["Busco la causa: because.", "Buildings and roads keep heat.", "Por eso las ciudades se calientan más."], "Porque los edificios y las calles retienen calor"),
    ],
    [
        ("Pensar que Sign up by Monday significa el lunes en la mañana.", "By Monday significa a más tardar el lunes.", "Piensa en el plazo, no en una hora."),
        ("Ignorar el but que limita la acción.", "Se entiende que puedes comprar durante la mantención.", "Lee el contraste: puedes leer, pero no comprar."),
    ],
    [
        mr(BU, "¿Dónde será la feria de arte?", "En el gimnasio", ["En la biblioteca", "En el patio"], "Dice in the gym."),
        mr(LN, "¿Hasta qué hora estará abierta la biblioteca de lunes a jueves?", "Hasta las 8 p.m.", ["Hasta las 6 p.m.", "Hasta las 10 p.m."], "Dice until 8 p.m. from Monday to Thursday."),
        mr(WB, "¿Qué puedes hacer durante la mantención?", "Leer el catálogo", ["Comprar", "Llamar a la tienda"], "Dice you can still read the catalog."),
    ],
    [
        mr(BU, "¿A qué hora deben traer los proyectos?", "A las 8 a.m.", ["A las 2 p.m.", "A las 4 p.m."], "Dice by 8 a.m."),
        mr(LN, "¿Qué horario no cambió?", "El de sábado y domingo", ["El de lunes a jueves", "Ninguno"], "Dice The Saturday and Sunday hours have not changed."),
        mr(HW, "¿Qué es una ola de calor?", "Cuando la temperatura permanece muy alta varios días", ["Un solo día de calor", "Un viento muy fuerte"], "Dice stays very high for several days."),
    ],
    [
        mr(BU, "¿Cuándo pueden visitar los apoderados?", "Entre las 2 y las 4 p.m.", ["A las 8 a.m.", "Después de las 4 p.m."], "Dice between 2 and 4 p.m."),
        mr(HW, "¿Qué hacen algunas municipalidades como resultado?", "Abren centros de enfriamiento y plantan más árboles", ["Cierran las calles", "Prohíben los edificios"], "Dice as a result, some city councils open cooling centers and plant more trees."),
        mr(WB, "¿Cuándo estará cerrada la tienda?", "Sábado, de medianoche a las 6 a.m.", ["Domingo a las 6 p.m., hasta la medianoche", "Todo el sábado, desde las 6 a.m. hasta la noche"], "Dice on Saturday, from midnight to 6 a.m."),
    ],
    [
        mr(LN, "¿Por qué la biblioteca cambió el horario?", "Porque muchos estudiantes pidieron más tiempo de estudio", ["Porque no tenía clientes", "Porque quería cerrar"], "Dice after many students asked for more study time."),
        arith("La biblioteca antes cerraba a las 6 p.m. y ahora cierra a las 8 p.m. de lunes a jueves. ¿Cuántas horas más abre al día?", "20-18", "Se restan la hora antigua y la nueva en formato de 24 horas.", " horas"),
    ],
    [
        mr(BU, "Un estudiante dice que los cupos se acabaron. ¿Qué dato del boletín lo contradice?", "Dice que quedan algunos cupos disponibles", ["Dice que los cupos son gratis", "Dice que la feria es el jueves"], "Dice A few places are still available."),
        mr(HW, "Otro estudiante dice que los árboles son la causa de las olas de calor. ¿Qué respuesta es mejor?", "No: los árboles son parte de la solución, no la causa", ["Sí: porque los árboles dan calor a las calles", "No se puede saber: el texto no habla de los árboles"], "El texto los presenta como parte de la respuesta."),
    ],
    [mr(WB, "Un cliente quiere comprar el sábado a las 5 a.m. ¿Qué ocurrirá?", "No podrá comprar: la tienda estará en mantención", ["Podrá comprar con descuento durante la mantención", "Podrá comprar solo por teléfono durante la mantención"], "Entre medianoche y las 6 a.m. no se puede comprar.")],
    [
        ("En Inglés de 2.º medio (OA 9, clase 3): ¿qué significa by Monday?", "A más tardar el lunes", "Indica un plazo."),
        ("En Inglés de 2.º medio (OA 9, clase 3): ¿qué marca la palabra but?", "Un contraste", "Cambia lo que puedes hacer."),
        ("En Inglés de 2.º medio (OA 9, clase 3): ¿qué preguntas contesta un aviso?", "Who, what, where y when", "Son los datos básicos."),
    ],
    task("Lee: «Class notice (fictional). The school trip to the aquarium is on Friday, April 5. We will leave at 8:30 a.m. and return at 3 p.m. The cost is 4,000 pesos. Please bring lunch. Few seats remain on the bus, so sign up by Wednesday.» (trip = paseo, aquarium = acuario, leave = salir, return = regresar, cost = costo, seats = asientos). Responde en inglés o español: idea general, hora de salida, costo, qué traer y plazo para inscribirse.", "Idea general: aviso del paseo al acuario. Salida: 8:30 a.m. Costo: 4.000 pesos. Traer: almuerzo. Plazo: miércoles.", ["responde las cinco preguntas", "usa datos del aviso", "no inventa información"], ["hoja con cinco respuestas"], ["confundir la hora de salida con la de regreso", "olvidar el plazo"], "Pide que explique qué significa few seats remain."),
    "Lee en voz alta el boletín escolar con un adulto y subraya las fechas y horas.",
    "Busca un aviso o noticia en español de tu barrio y anota las preguntas who, what, where y when.",
)

# ------------------------------------------------------------------ clase 4: otras culturas y temas globales
CU1 = "«Greeting Customs (article). In many countries, people shake hands when they meet. In Japan, a bow is common. In Chile, friends often kiss on the cheek. Learning local customs helps travelers show respect.» (customs = costumbres, shake hands = dar la mano, bow = reverencia, kiss on the cheek = beso en la mejilla, travelers = viajeros, respect = respeto)"
CU2 = "«A Letter from a Student in Linora (a made-up country). Hello! I live in a town near a big park. School starts at 8, and many of us walk to class. At lunch, we usually eat rice and beans. On Saturdays, I have been helping my aunt at her fruit stand.» (letter = carta, rice = arroz, beans = porotos, aunt = tía, fruit stand = puesto de frutas)"
GL1 = "«Why Do Languages Disappear? (article, fictional examples). Some languages have only a few speakers. When children stop learning the language at home, it can slowly disappear. Teachers and families can help by using it in songs, stories and daily life.» (languages = idiomas, speakers = hablantes, disappear = desaparecer, slowly = lentamente, daily life = vida diaria)"
GL2 = "«Internet Access Around the World (fictional summary). In some towns, a large number of students use the internet every day. In others, few families have a connection. Libraries and schools often offer free access, so students can do homework.» (access = acceso, connection = conexión, free = gratis, homework = tarea)"

lesson(
    OA, 4, MAT_R,
    "Aprenderé a leer textos sobre otras culturas y temas globales y a identificar su idea general e información explícita. Sirve para conocer cómo viven otras personas y comparar con mi realidad con respeto.",
    ["Sé leer textos informativos.", "Conozco palabras como custom y country."],
    [
        "Los textos sobre otras culturas describen costumbres: cómo se saluda, qué se come, cómo es la vida escolar. Los textos de interés global tratan de temas que afectan a muchos países: idiomas, acceso a internet, el clima. Para entenderlos, identifica el tema, el lugar y las ideas principales, y distingue los datos de las opiniones del autor. Los textos de ejemplo de esta clase son ficticios o generales: sirven para practicar, no para afirmar hechos de un país.",
        "Al leer sobre otra cultura, evita las generalizaciones: no todas las personas de un país hacen lo mismo. Las palabras many, some, often y usually matizan: In many countries, people shake hands. Observa también los contrastes (In Japan..., In Chile...) y las comparaciones con tu cultura: Where I live, we usually... Esto muestra respeto y curiosidad.",
        "Para encontrar información explícita, busca los lugares, las frecuencias y los números. Para la idea general, pregunta qué quiere mostrar el autor: costumbres distintas, un problema global o una solución. Las funciones del año, como few, a large number of y often, aparecen para hablar de cantidades y frecuencias.",
    ],
    [("customs", "costumbres"), ("many / some / few", "muchos / algunos / pocos"), ("generalization", "generalización: decir que todos hacen lo mismo"), ("global issue", "problema global"), ("access", "acceso"), ("respect", "respeto")],
    [
        ("Contrastar costumbres", CU1 + " ¿Qué costumbre menciona para Chile y cuál para Japón?", ["Busco los nombres de los países.", "En Chile, los amigos suelen darse un beso en la mejilla.", "En Japón es común hacer una reverencia."], "Chile: beso en la mejilla; Japón: reverencia"),
        ("Idea global", GL1 + " ¿Cuál es la idea general?", ["El tema son los idiomas que pueden desaparecer.", "El texto dice por qué ocurre y qué pueden hacer familias y profesores.", "Es un problema y una forma de ayudar."], "Algunos idiomas pueden desaparecer cuando los niños dejan de aprenderlos, pero familias y profesores pueden ayudar usándolos"),
    ],
    [
        ("Pensar que todos los habitantes de un país hacen lo mismo.", "Los textos usan many, some o often para matizar.", "Fíjate en las palabras que indican cantidad."),
        ("Decir que una cultura es mejor que otra.", "El texto describe costumbres, no las ordena.", "Describe y compara con respeto."),
    ],
    [
        mr(CU1, "¿Qué se hace en muchos países al conocer a alguien?", "Dar la mano", ["Hacer una reverencia siempre", "Abrazarse siempre"], "Dice In many countries, people shake hands."),
        mr(CU2, "¿A qué hora empieza la escuela de la estudiante de Linora del texto?", "A las 8", ["A las 10", "A las 6"], "Dice School starts at 8."),
        mr(GL2, "¿Qué ofrecen a menudo las bibliotecas y escuelas?", "Acceso gratuito a internet", ["Computadores de regalo", "Clases de música"], "Dice libraries and schools often offer free access."),
    ],
    [
        mr(CU2, "¿Qué suele comer la estudiante en el almuerzo?", "Arroz con porotos", ["Pan con queso", "Pollo con papas"], "Dice we usually eat rice and beans."),
        mr(CU2, "¿Qué ha estado haciendo los sábados?", "Ayudando a su tía en un puesto de frutas", ["Estudiando inglés", "Jugando en el parque"], "Dice I have been helping my aunt at her fruit stand."),
        mr(GL1, "¿Cómo pueden ayudar los profesores y las familias?", "Usándolo en canciones, historias y la vida diaria", ["Prohibiendo el idioma en la escuela y en la casa", "Cambiando de idioma en las canciones y en la vida diaria"], "Dice by using it in songs, stories and daily life."),
    ],
    [
        mr(GL2, "¿Qué diferencia presenta el texto entre algunos pueblos?", "En unos muchos usan internet y en otros pocos tienen conexión", ["En todos los pueblos hay la misma conexión a internet", "En ninguno de los pueblos hay escuelas ni bibliotecas"], "Dice In some towns, a large number... In others, few families..."),
        mr(CU1, "¿Qué dice el texto que ayuda a los viajeros?", "Conocer las costumbres locales", ["Hablar muy fuerte", "Cambiar de ropa"], "Dice Learning local customs helps travelers show respect."),
        mr(GL1, "¿Qué significa only a few speakers?", "Muy pocos hablantes", ["Muchos hablantes", "Ningún hablante"], "A few indica una cantidad pequeña."),
    ],
    [
        mr(CU1, "Un estudiante dice «All Chileans kiss on the cheek». ¿Qué corrige el texto?", "El texto dice que los amigos suelen hacerlo, no todos", ["Dice que nadie lo hace", "Dice que solo ocurre en Japón"], "Dice friends often kiss, lo que no es lo mismo que todos."),
        mr(CU2, "Otro estudiante dice que la carta describe a un país entero. ¿Qué respuesta es mejor?", "No: describe la vida de una estudiante, no de todo el país", ["Sí: describe las costumbres de todos los habitantes", "Sí: es un informe oficial que describe todo el país"], "Es una carta personal y ficticia."),
    ],
    [
        mr(GL1 + " " + CU1, "Hay dos textos: el de los idiomas y el de los saludos. ¿Cuál es más probable que proponga una solución?", "El de los idiomas: dice cómo pueden ayudar familias y profesores", ["El de los saludos: explica cómo saludar a personas de otros países", "Ninguno de los dos: ambos solo describen costumbres y problemas"], "El texto de idiomas propone usarlo en la vida diaria."),
        mr(GL2, "Si en un pueblo solo pocas familias tienen conexión, ¿qué puede hacer una escuela según el texto?", "Ofrecer acceso gratis", ["Cerrar la biblioteca", "Cobrar por internet"], "El texto dice que escuelas y bibliotecas ofrecen free access."),
    ],
    [mr(CU1 + " " + CU2, "Compara los dos textos. ¿Qué idea comparten?", "Que las costumbres cambian según el lugar", ["Que en todas partes comen arroz", "Que solo en Chile se saluda"], "Ambos describen costumbres de lugares distintos.")],
    [
        ("En Inglés de 2.º medio (OA 9, clase 4): ¿qué palabras evitan generalizar sobre una cultura?", "Many, some, often y usually", "Marcan que no todos hacen lo mismo."),
        ("En Inglés de 2.º medio (OA 9, clase 4): ¿qué haces al leer una costumbre distinta a la tuya?", "Describo y comparo con respeto", "Sin juzgar a nadie."),
        ("En Inglés de 2.º medio (OA 9, clase 4): ¿qué es un problema global?", "Uno que afecta a muchos países", "Por ejemplo, el acceso a internet."),
    ],
    task("Lee: «Festivals of Light (article, general). In many cultures, people celebrate with lights during the darkest months of the year. Families often decorate their homes with colorful lamps, share food and sing songs. Some festivals last for a day, and others last for several days.» (festivals = festivales, light = luz, celebrate = celebran, darkest = más oscuros, decorate = decoran, colorful lamps = lámparas de colores, share = compartir). Escribe la idea general, dos datos y una comparación con una fiesta de tu cultura.", "Idea general: muchas culturas celebran con luces en los meses oscuros. Datos: se comparten comidas y canciones; duran un día o varios. Comparación: en mi familia compartimos comida en las fiestas.", ["escribe la idea general", "da dos datos explícitos", "compara con respeto sin generalizar"], ["hoja con tres respuestas"], ["decir que todas las culturas lo hacen igual", "no comparar con la propia"], "Pide que busque una palabra del texto que matice la generalización."),
    "Lee otra vez el texto de saludos y marca las palabras many, some y often.",
    "Investiga con una persona de tu casa una costumbre de tu familia y escribe en español cómo se compara con la del texto de Linora.",
)

# ------------------------------------------------------------------ clase 5: temas menos conocidos y palabras nuevas
BR = "«Braille (reference text). Braille is a system of raised dots that blind and low-vision people read with their fingers. It was developed in the 1800s by Louis Braille, a young French student who was blind. Each letter is a group of dots in a small cell. Today, many public places have signs in Braille.» (reference text = texto informativo, raised dots = puntos en relieve, blind = ciego, low-vision = baja visión, fingers = dedos, developed = desarrolló, cell = celda, signs = letreros)"
BE = "«Beekeeping (reference text). Beekeepers take care of bees in boxes called hives. A hive has one queen and many worker bees. Worker bees collect nectar from flowers and make honey. Beekeepers wear protective clothes and work slowly and calmly.» (beekeeping = apicultura, beekeepers = apicultores, bees = abejas, hives = colmenas, queen = reina, worker bees = abejas obreras, nectar = néctar, honey = miel, protective = de protección)"
OR = "«Origami (reference text). Origami is the art of folding paper into shapes, such as animals and flowers. It comes from Japan. People use only paper, and usually no scissors. Beginners often start with a simple boat or a crane.» (scissors = tijeras, folding = doblar, shapes = figuras, comes from = viene de, beginners = principiantes, crane = grulla)"
SK = "«Urban Sketching (reference text). Urban sketching means drawing the places you see in your city, outdoors, quickly. Sketchers carry a small notebook and a pen. They draw buildings, streets and people. Many groups meet once a month to sketch together.» (urban = urbano, sketching = dibujar croquis, outdoors = al aire libre, quickly = rápido, carry = llevan, buildings = edificios)"

lesson(
    OA, 5, MAT_R,
    "Aprenderé a leer textos sobre temas menos conocidos, deduciendo palabras nuevas por el contexto y encontrando la idea general y los datos explícitos. Sirve para entender textos aunque el tema o el vocabulario sean nuevos.",
    ["Sé identificar la idea general.", "Sé usar el contexto para adivinar palabras."],
    [
        "Cuando el tema es poco conocido, no necesitas entender cada palabra. Lee el título y la primera oración: suelen contener una definición, como Braille is a system of raised dots... Subraya las palabras que se repiten, porque muestran el tema. Para una palabra nueva, mira las palabras que la rodean: antes, después y los ejemplos.",
        "El contexto ayuda de varias formas. A veces el texto define la palabra (Beekeepers take care of bees in boxes called hives). A veces da un ejemplo (shapes, such as animals and flowers). A veces da un contraste o una causa. Si aun así no la entiendes, mira si se parece a una palabra en español (nectar, origami) o pregúntate si necesitas esa palabra para responder.",
        "Después de leer, escribe la idea general en una oración y tres datos explícitos. Comprueba que cada dato está en el texto. Los textos de esta clase son informativos y breves; sus datos son generales y no incluyen cifras que debas memorizar.",
    ],
    [("definition", "definición dentro del texto"), ("context clue", "pista del contexto"), ("such as", "como, por ejemplo"), ("called", "llamado"), ("cognate", "palabra parecida al español"), ("reference text", "texto informativo")],
    [
        ("Deducir una palabra por una definición", BE + " ¿Qué es una hive?", ["El texto dice boxes called hives.", "Los apicultores cuidan abejas en cajas.", "Una hive es una colmena."], "Una colmena: la caja donde viven las abejas"),
        ("Deducir una palabra por un ejemplo", OR + " ¿Qué significa shapes?", ["Dice shapes, such as animals and flowers.", "Los ejemplos son animales y flores.", "Shapes son figuras."], "Figuras, como animales y flores"),
    ],
    [
        ("Detenerse en una palabra nueva y dejar de leer.", "Se pierde el hilo del texto.", "Sigue leyendo y usa el contexto."),
        ("Adivinar sin mirar el contexto.", "Puedes elegir un significado que no encaja.", "Busca definiciones o ejemplos cerca de la palabra."),
    ],
    [
        mr(BR, "¿Qué es Braille?", "Un sistema de puntos en relieve para leer con los dedos", ["Un tipo de música", "Un idioma hablado"], "Dice a system of raised dots that ... people read with their fingers."),
        mr(BE, "¿Qué hacen las abejas obreras?", "Recogen néctar de las flores y hacen miel", ["Cuidan a los apicultores", "Cortan la caja"], "Dice Worker bees collect nectar from flowers and make honey."),
        mr(OR, "¿De dónde viene el origami?", "De Japón", ["De Chile", "De Francia"], "Dice It comes from Japan."),
    ],
    [
        mr(BR, "¿Quién desarrolló Braille?", "Un joven estudiante francés que era ciego", ["Un profesor de música", "Un médico alemán"], "Dice by Louis Braille, a young French student who was blind."),
        mr(SK, "¿Qué llevan los dibujantes urbanos?", "Un cuaderno pequeño y un lápiz pasta", ["Un caballete y una mesa", "Una cámara de video"], "Dice a small notebook and a pen."),
        mr(OR, "¿Con qué empiezan a menudo los principiantes?", "Con un bote o una grulla simples", ["Con un dragón difícil", "Con una pelota de papel"], "Dice Beginners often start with a simple boat or a crane."),
    ],
    [
        mr(BR, "¿Qué significa cell en este texto?", "Un espacio pequeño con un grupo de puntos para una letra", ["Una celda pequeña de cárcel donde se guardan las letras", "Un teléfono celular que lee los puntos con la pantalla"], "Dice Each letter is a group of dots in a small cell."),
        mr(BE, "¿Qué ropa usan los apicultores?", "Ropa de protección", ["Ropa de colores brillantes para atraer a las abejas", "Ninguna ropa especial para trabajar"], "Dice protective clothes."),
        mr(SK, "¿Cada cuánto se juntan muchos grupos de dibujantes?", "Una vez al mes", ["Todos los días", "Una vez al año"], "Dice once a month."),
    ],
    [
        mr(BR, "Un estudiante dice que Braille se lee con los ojos. ¿Qué dato lo contradice?", "Dice que se lee con los dedos", ["Dice que fue creado en el siglo XXI", "Dice que tiene letras"], "El texto menciona fingers."),
        mr(BE, "Un compañero dice que una colmena tiene muchas reinas. ¿Qué dice el texto?", "Que tiene una reina y muchas abejas obreras", ["Que tiene dos reinas y pocas abejas obreras", "Que no tiene reina y solo tiene abejas obreras"], "Dice A hive has one queen and many worker bees."),
    ],
    [
        mr(OR, "¿Cuál es la idea general del texto sobre el origami?", "Es el arte de doblar papel en figuras y viene de Japón", ["Es el arte de cortar papel", "Es un juego de cartas"], "Resume la definición y el origen."),
        mr(SK, "¿Cuál es la idea general del texto de urban sketching?", "Dibujar rápido y al aire libre lugares de la ciudad", ["Pintar solo retratos de personas en un estudio", "Fotografiar edificios de la ciudad con una cámara"], "Define la actividad."),
    ],
    [mr(BR, "Pregunta de comprensión: ¿qué ocurre hoy en muchos lugares públicos?", "Hay letreros en Braille", ["No hay letreros", "Solo hay letreros en francés"], "Dice Today, many public places have signs in Braille.")],
    [
        ("En Inglés de 2.º medio (OA 9, clase 5): ¿qué indica such as?", "Que viene un ejemplo", "Introduce unos ejemplos."),
        ("En Inglés de 2.º medio (OA 9, clase 5): ¿qué haces con una palabra nueva en un texto?", "Uso el contexto sin dejar de leer", "El contexto da el sentido."),
        ("En Inglés de 2.º medio (OA 9, clase 5): ¿dónde suele estar la definición de un tema nuevo?", "En el título o la primera oración", "Ahí se presenta el tema."),
    ],
    task("Lee: «Sundials (reference text). A sundial is a clock that uses the Sun. It has a flat plate with numbers and a thin pointer called a gnomon. When the Sun moves, the shadow of the pointer moves too, and it shows the hour. People in many places have used sundials for a very long time. A sundial does not work at night or on cloudy days.» (sundial = reloj de sol, flat plate = placa plana, thin pointer = varilla delgada, shadow = sombra, shows = muestra, hour = hora, cloudy = nublado). Escribe la idea general, tres datos y el significado de una palabra nueva deducida por el contexto.", "Idea general: un reloj de sol es un reloj que usa el Sol para mostrar la hora. Datos: tiene una placa con números y una varilla; la sombra se mueve cuando se mueve el Sol; no funciona de noche ni en días nublados. Palabra: gnomon, la varilla delgada que hace la sombra.", ["escribe la idea general", "da tres datos explícitos", "deduce una palabra nueva por el contexto"], ["hoja con cinco respuestas"], ["inventar datos", "no usar el contexto"], "Pide que señale la frase que le permitió deducir la palabra."),
    "Elige un tema que no conozcas en inglés y lee solo el título y la primera oración.",
    "Cuenta a una persona de tu casa, en español, de qué trata uno de los textos de esta clase.",
)
