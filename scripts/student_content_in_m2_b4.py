"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 13: historias e información con recursos multimodales.

El estudiante analiza y completa borradores escritos con imágenes descritas en el enunciado y produce sus propios textos
con papel y lápiz. Textos originales, inglés americano. Los títulos de clase del plan son genéricos; aquí se aplican a
elegir mensaje y recursos, experiencias personales con fotos y globos, información interdisciplinaria con infografía,
temas globales y culturas de otros países, y creación a partir de un texto leído.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 13"

# ------------------------------------------------------------------ clase 1: mensaje, propósito y recursos
M1 = "Borrador A. Texto: «Last Saturday, I helped my cousin move to a new apartment. We carried boxes and put books on shelves. At the end, we were tired but happy.» Recurso: ninguno."
M2 = "Borrador B. Texto: «Last Saturday, I helped my cousin move.» Recursos: una foto de cajas apiladas con la etiqueta «Books», una foto de dos personas sentadas en el piso y una flecha que dice «Tired but happy!»."
M3 = "Cartel C para informar sobre un taller de dibujo: título «Draw with Us!», una foto de manos dibujando, y tres líneas: «Every Thursday. 4:00 p.m. Room 3.»"
M4 = "Cartel D para el mismo taller: 15 líneas de texto pequeño, sin foto, con tres tipos de letra y cinco colores."

lesson(
    OA, 1, MAT_R,
    "Aprenderé a elegir el mensaje, el propósito y los recursos multimodales (fotos, dibujos, globos, títulos, flechas) para escribir una historia o un texto informativo creativo y efectivo. Sirve para que cada imagen y cada palabra aporten al mensaje.",
    ["Sé escribir oraciones simples y compuestas.", "Sé reconocer el propósito de un texto."],
    [
        "Antes de escribir, decide tres cosas. Primero, el mensaje (message): ¿qué quieres que entienda el lector? Segundo, el propósito (purpose): ¿contar, informar, convencer o entretener? Tercero, los recursos multimodales (multimodal resources): ¿qué imágenes, títulos, globos de diálogo, flechas o colores ayudarán? Un recurso es útil si refuerza el mensaje y no lo repite entero.",
        "Una historia multimodal combina palabras e imágenes: cada foto o dibujo muestra un momento y el texto agrega lo que la imagen no dice, como los sentimientos o la causa. Un texto informativo combina título, datos breves, imágenes con etiquetas y colores que ordenan. Usa letras grandes, pocos textos por imagen y colores que se lean bien.",
        "Revisa con tres preguntas: ¿se entiende el mensaje en cinco segundos?, ¿cada recurso tiene una función? y ¿hay algo que sobra? Si una imagen no ayuda, quítala. Si el texto es largo, divídelo en pasos o viñetas.",
    ],
    [("message", "mensaje"), ("multimodal resource", "recurso que combina palabras con imagen u otro medio"), ("caption", "pie de foto"), ("speech bubble", "globo de diálogo"), ("label", "etiqueta"), ("headline", "título llamativo")],
    [
        ("Comparar dos borradores", M1 + " " + M2 + " ¿Cuál comunica mejor la experiencia y por qué?", ["El borrador A solo tiene texto.", "El B suma fotos, etiquetas y una flecha con sentimiento.", "El B muestra la experiencia con más recursos."], "El B, porque usa fotos, etiqueta y una flecha que muestra el sentimiento"),
        ("Evaluar carteles", M3 + " " + M4 + " ¿Cuál es más efectivo y por qué?", ["El C tiene título claro, foto y datos breves.", "El D tiene demasiado texto y colores.", "El C se entiende en pocos segundos."], "El C, porque tiene título, foto y datos breves"),
    ],
    [
        ("Poner mucho texto en un cartel.", "El lector no alcanza a leer.", "Usa título, imagen y pocos datos."),
        ("Usar imágenes que repiten el texto exactamente.", "No agregan información.", "Agrega algo con la imagen: un sentimiento, un lugar."),
    ],
    [
        mr(M3, "¿Qué día es el taller?", "Los jueves", ["Los sábados", "Todos los días"], "Dice Every Thursday."),
        mc("¿Qué recurso agrega un sentimiento a una historia?", "Una flecha o globo con la emoción", ["Una lista de precios", "Una tabla de horarios"], "Los globos muestran emociones."),
        mr(M2, "¿Qué dice la etiqueta de la caja?", "Books", ["Shoes", "Toys"], "Dice una etiqueta «Books»."),
    ],
    [
        mr(M2, "¿Qué sentimiento muestra la flecha?", "Cansancio y alegría", ["Enojo", "Miedo"], "Dice Tired but happy!"),
        mr(M3, "¿Qué hace la foto de manos dibujando?", "Muestra de qué trata el taller", ["Indica la hora", "Indica el costo"], "Refuerza el tema."),
        mr(M4, "¿Qué problema tiene este cartel?", "Demasiado texto pequeño y muchos colores", ["No tiene título", "Tiene una foto muy grande"], "Quince líneas y cinco colores dificultan la lectura."),
    ],
    [
        mc("Quieres informar un cambio de horario de un club. ¿Qué cartel es mejor?", "Título grande y la hora nueva en grande", ["Un párrafo largo con todas las novedades", "Una foto del club sin texto"], "Se entiende en segundos."),
        mc("Quieres contar una experiencia con tres fotos. ¿Qué agregas a cada foto?", "Un pie con lo que no se ve en la foto", ["Una repetición exacta de lo que se ve", "Un título igual para las tres fotos"], "El pie agrega información."),
        arith("Un cartel tiene un título de 3 palabras, una línea de datos de 6 palabras y otra de 4 palabras. ¿Cuántas palabras tiene en total?", "3+6+4", "Se suman las palabras de cada parte.", " palabras"),
    ],
    [
        mr(M1, "Un compañero dice que el borrador A es mejor porque tiene más palabras. ¿Qué respuesta es más acertada?", "No necesariamente: más palabras no siempre comunican mejor; el B usa imágenes que refuerzan", ["Sí: más palabras es mejor", "El A tiene imágenes"], "La efectividad depende de cómo se combinan los recursos."),
        mr(M4, "Una compañera propone agregar más colores al cartel D para que se vea más creativo. ¿Qué respuesta es mejor?", "No: la creatividad debe ayudar a leer, no dificultarlo", ["Sí: más colores siempre se ve mejor y llama la atención", "Sí: hay que quitar el título para ganar espacio"], "Los recursos deben reforzar el mensaje."),
    ],
    [
        mr(M2, "Escribe un título para el borrador B. ¿Cuál es el más adecuado?", "A Busy Saturday: Moving Day", ["The Weather in Winter", "How Planes Fly"], "Se relaciona con la historia."),
        mr(M3, "Escribe un pie de foto para la foto del cartel C. ¿Cuál es el más adecuado?", "Learn to draw with friends every Thursday", ["Drawing is bad", "Buy a pencil"], "Refuerza el mensaje del taller."),
    ],
    [mc("Debes escribir una historia con tres fotos sobre tu primer día en un lugar nuevo. ¿Cuál es el mejor plan?", "Foto 1: llegada y sentimiento; foto 2: un reto; foto 3: la solución", ["Tres fotos del mismo momento con el mismo pie de foto", "Foto 1: la solución; foto 2: el reto; foto 3: la llegada"], "Cada foto cumple una función en la historia.")],
    [
        ("En Inglés de 2.º medio (OA 13, clase 1): ¿qué tres cosas decides antes de escribir?", "El mensaje, el propósito y los recursos", "Guían el texto."),
        ("En Inglés de 2.º medio (OA 13, clase 1): ¿qué es un pie de foto?", "Un texto breve que explica o completa la imagen", "Se escribe bajo la foto."),
        ("En Inglés de 2.º medio (OA 13, clase 1): ¿cuándo un recurso es útil?", "Cuando refuerza el mensaje", "No debe sobrar."),
    ],
    task("Elige un tema: «A day I was proud of myself», «A place I like in my city» o «An important lesson». Escribe un mensaje de una oración, un propósito y una lista de tres recursos multimodales que usarías (por ejemplo, fotos con pie de foto, un título y un globo). Luego escribe el primer pie de foto en inglés. Sigue este ejemplo.", "Tema: A place I like in my city. Mensaje: The park near my house makes me feel calm. Propósito: contar. Recursos: foto del parque con pie de foto, título, globo con una frase mía. Pie: Sunday morning at the park: no homework, only sun.", ["define mensaje y propósito", "propone tres recursos con una función", "escribe un pie de foto en inglés"], ["hoja con cuatro respuestas"], ["usar recursos sin función", "pie de foto que repite la imagen"], "Pide que quite un recurso y explique cómo cambia el mensaje."),
    "Dibuja un cartel de tres elementos para anunciar una actividad de tu curso.",
    "Observa un afiche y escribe en español qué función tiene cada recurso.",
)

# ------------------------------------------------------------------ clase 2: experiencias personales con fotos y globos
E1 = "Historia con tres fotos. Foto 1: una niña frente a un portón cerrado; pie: «I arrived early, but the gate was closed.» Foto 2: la niña toca un timbre; pie: «I rang the bell and waited.» Foto 3: la niña entra con una sonrisa; pie: «Finally, the guard opened the door!» (gate = portón, rang the bell = toqué el timbre, guard = guardia)"
E2 = "Viñetas de un cómic (cuatro cuadros). Cuadro 1: Ben mira su mochila vacía; globo: «Where is my homework?» Cuadro 2: Ben busca bajo la cama. Cuadro 3: su hermana lo ve y se ríe; globo: «It's on the table!» Cuadro 4: Ben sonríe; texto: «Next time, I will use a checklist.» (homework = tarea, checklist = lista de verificación)"
E3 = "Entrada de diario (journal) con dibujo: «Dear journal, today I played in the school band for the first time. My hands were cold, but the audience clapped.» Dibujo: una trompeta, una nota musical y una flecha con «nervous!». (band = banda, audience = público, clapped = aplaudió, nervous = nervioso)"
E4 = "Texto en desorden: 1) «Finally, I felt proud.» 2) «First, I joined the school swimming team.» 3) «Then I learned the strokes.» 4) «After that, I swam in my first race.» (finally = por fin, joined = me uní, swimming team = equipo de natación, strokes = estilos de nado, race = carrera)"

lesson(
    OA, 2, MAT_R,
    "Aprenderé a escribir una experiencia personal con fotos o viñetas, pies de foto, globos de diálogo y una secuencia clara (first, then, after that, finally). Sirve para contar una historia que se entiende mejor porque texto e imagen se complementan.",
    ["Sé contar hechos en pasado.", "Conozco first, then y finally."],
    [
        "Una experiencia personal multimodal cuenta lo que te pasó con palabras e imágenes. Cada foto o cuadro muestra un momento. El pie de foto (caption) dice lo que la imagen no muestra: el lugar, la hora, lo que sentías. Un globo de diálogo (speech bubble) muestra lo que alguien dijo, entre comillas. Una nota de sentimiento (feeling note) puede ser una flecha con una palabra, como nervous!",
        "La secuencia es importante. Usa first, then, after that, later y finally para ordenar. Cuenta en pasado (arrived, rang, opened) y usa had + participio solo cuando una acción ocurrió antes de otra pasada, como I had forgotten my bag, so I returned home. Para un plan futuro usa will: I will use a checklist next time. Mantén el mismo orden en las imágenes y en el texto.",
        "Un buen final muestra qué cambió o qué aprendiste: Next time, I will use a checklist. Pregúntate: ¿mi historia tiene inicio, desarrollo y final?, ¿cada pie de foto agrega algo? y ¿los sentimientos se entienden?",
    ],
    [("caption", "pie de foto"), ("speech bubble", "globo de diálogo"), ("first / then / after that / finally", "primero / luego / después de eso / por fin"), ("journal", "diario personal"), ("feeling note", "nota de sentimiento"), ("next time", "la próxima vez")],
    [
        ("Ordenar una experiencia", E4 + " Ordena las oraciones para contar la experiencia.", ["Busco first: la 2.", "Luego Then: la 3; After that: la 4.", "Finally: la 1."], "2, 3, 4, 1"),
        ("Pie de foto que agrega información", E1 + " ¿Qué agrega el pie de la foto 1 que la imagen no dice?", ["La imagen muestra un portón cerrado.", "El pie dice que llegó temprano.", "Agrega el sentimiento y el momento."], "Que la niña llegó temprano pero el portón estaba cerrado"),
    ],
    [
        ("Contar una experiencia sin orden claro.", "El lector se confunde.", "Usa first, then, after that y finally."),
        ("Poner pies de foto que describen lo que ya se ve.", "No agregan información.", "Agrega lo que no se ve: sentimiento, lugar o razón."),
    ],
    [
        mr(E1, "¿Qué hace la niña en la foto 2?", "Toca el timbre y espera", ["Se va del portón sin esperar", "Come algo junto al guardia"], "Dice I rang the bell and waited."),
        mr(E2, "¿Qué dice la hermana?", "It's on the table", ["It's under the bed", "I don't know"], "Dice el globo del cuadro 3."),
        mr(E3, "¿Qué sintió quien escribe el diario al comenzar?", "Nervios", ["Enojo", "Aburrimiento"], "La flecha dice nervous."),
    ],
    [
        mr(E2, "¿Qué aprende Ben al final?", "Usará una lista la próxima vez", ["Dejará la tarea para otro día", "Dejará de buscar bajo la cama"], "Dice Next time, I will use a checklist."),
        mr(E1, "¿Qué palabra marca el último paso del relato de la niña?", "Finally", ["First", "After that"], "Finally introduce el final."),
        mr(E3, "¿Qué hizo el público?", "Aplaudió", ["Se fue del lugar", "Se rió con ganas"], "Dice the audience clapped."),
    ],
    [
        mr(E4, "¿Qué conector va con la primera oración de la secuencia?", "First", ["Finally", "After that"], "La acción de unirse al equipo es la primera."),
        mr(E2, "¿Qué tiempo usa el final de la historia de Ben, Next time, I will use a checklist?", "Futuro con will, para un plan", ["Pasado simple, porque cuenta un hecho", "Presente continuo, porque ocurre ahora"], "Will + verbo anuncia un plan futuro."),
        mc("Quieres mostrar lo que dijo tu amigo en tu cómic. ¿Qué recurso usas?", "Un globo de diálogo", ["Un título", "Un pie de foto largo"], "Los globos muestran lo que se dice."),
    ],
    [
        mr(E1, "Una compañera dice que el pie de la foto 3 no es necesario porque la foto muestra una sonrisa. ¿Qué respuesta es más acertada?", "Es útil porque explica por qué sonríe: el guardia abrió la puerta", ["Tiene razón: la foto basta", "El pie repite exactamente la foto"], "El pie agrega la causa."),
        mr(E3, "Otro compañero dice que el dibujo del diario ya dice todo. ¿Qué respuesta es mejor?", "El texto agrega las manos frías y el aplauso", ["Tiene razón: el dibujo ya muestra todo el texto", "El dibujo no tiene ningún sentido en el diario"], "Texto e imagen se complementan."),
    ],
    [
        mr(E2 + " " + E3, "¿Qué tienen en común el cómic de Ben y el diario?", "Ambos cuentan una experiencia con un final positivo", ["Ambos son noticias", "Ambos son avisos"], "Ben sonríe y el público aplaude."),
        mr(E4, "Escribe una oración de cierre para la historia del equipo de natación. ¿Cuál es la más adecuada?", "Now I swim every week and I feel proud", ["The swimming team is the best team in the world", "Swimming is a sport that people do in water"], "Muestra el cambio y no compara."),
    ],
    [mr(E1, "Quieres agregar una cuarta foto a la historia de la niña. ¿Cuál tiene sentido?", "Foto 4: saluda a su profesora; pie «My day began well»", ["Foto 4: vuelve al portón; pie «The gate was closed again»", "Foto 4: llega al portón; pie «I arrived early»"], "Continúa la secuencia sin repetir las fotos anteriores.")],
    [
        ("En Inglés de 2.º medio (OA 13, clase 2): ¿qué hace un pie de foto?", "Agrega información que la imagen no muestra", "Completa la imagen."),
        ("En Inglés de 2.º medio (OA 13, clase 2): ¿qué conectores ordenan una secuencia?", "First, then, after that y finally", "Ordenan los hechos."),
        ("En Inglés de 2.º medio (OA 13, clase 2): ¿qué muestra un globo de diálogo?", "Lo que dice un personaje", "Se escribe entre comillas."),
    ],
    task("Escribe una historia de tres fotos o dibujos sobre «A time I solved a problem». Para cada imagen, describe en español qué se ve y escribe en inglés un pie de foto de una oración. Usa first, then y finally, y agrega un globo de diálogo en una de las imágenes. Sigue este ejemplo.", "Foto 1: una niña con un celular sin batería. Pie: First, my phone died on the bus. Foto 2: ella pregunta a una señora. Globo: «Can I borrow a charger?» Pie: Then I asked for help. Foto 3: celular cargando. Pie: Finally, I could call my mom.", ["tres imágenes con pie de foto", "usa first, then y finally", "incluye un globo de diálogo"], ["tres imágenes en la hoja", "pies de foto en inglés"], ["pies de foto que repiten la imagen", "no mantener el orden"], "Pide que cambie el final por otro posible y ajuste el pie."),
    "Escribe en tu cuaderno cuatro pies de foto para fotos de tu fin de semana.",
    "Cuenta a una persona de tu casa una experiencia tuya con tres fotos y explica qué agrega cada una.",
)

# ------------------------------------------------------------------ clase 3: información interdisciplinaria con infografía
IG1 = "Infografía A sobre las capas de la Tierra (Ciencias): título «Layers of the Earth»; un dibujo de la Tierra cortada con tres etiquetas: crust (corteza) en la capa exterior, mantle (manto) en la capa del medio, core (núcleo) en el centro. Frase: «The crust is the thinnest layer.»"
IG2 = "Infografía B de Matemática: título «Perimeter of a Rectangle». Dibujo de un rectángulo de 6 cm por 4 cm. Fórmula: P = 2 × (length + width). Cálculo: 2 × (6 + 4) = 20 cm. (length = largo, width = ancho, perimeter = perímetro)"
IG3 = "Línea de tiempo de Historia (de ejemplo, inventada): título «School Timeline». 1950: school founded; 1980: new library; 2000: computer room; 2020: science lab. (founded = fundada, library = biblioteca, computer room = sala de computación, lab = laboratorio)"
IG4 = "Infografía C mal diseñada: sin título, con letras muy pequeñas, tres colores de fondo y datos que no se entienden."

lesson(
    OA, 3, MAT_R,
    "Aprenderé a escribir información relevante de otras asignaturas (Ciencias, Matemática, Historia) con infografías, etiquetas, fórmulas y líneas de tiempo. Sirve para explicar contenidos de forma clara y visual.",
    ["Sé escribir títulos y etiquetas.", "Conozco palabras de Ciencias y Matemática."],
    [
        "Una infografía (infographic) combina texto breve, imágenes, datos y etiquetas para explicar una idea. Para escribir una, elige un título que diga el tema, selecciona los datos más importantes, ordénalos y apóyalos con una imagen o un diagrama. Cada etiqueta (label) nombra una parte del dibujo. Una fórmula o un cálculo debe estar paso a paso y con unidades.",
        "Cada asignatura tiene recursos propios. En Ciencias, los diagramas rotulados explican partes: The crust is the thinnest layer. En Matemática, una fórmula con un ejemplo numérico: P = 2 × (length + width). En Historia, una línea de tiempo con fechas y hechos. Usa frases cortas en presente simple para definiciones y hechos permanentes, y en pasado simple para hechos históricos: The school was founded in 1950.",
        "Revisa tu infografía: ¿el título dice el tema?, ¿las etiquetas están junto a su parte?, ¿los números tienen unidad? y ¿hay una sola idea principal? Si usas datos inventados, escribe «de ejemplo» en la infografía.",
    ],
    [("infographic", "infografía"), ("label", "etiqueta"), ("diagram", "diagrama"), ("formula", "fórmula"), ("timeline", "línea de tiempo"), ("example data", "datos de ejemplo")],
    [
        ("Etiquetar un diagrama", IG1 + " ¿Qué capa está en el centro?", ["Busco la etiqueta del centro.", "Dice core en el centro.", "Core es el núcleo."], "El núcleo (core)"),
        ("Usar una fórmula", IG2 + " ¿Cuál es el perímetro de un rectángulo de 6 cm por 4 cm?", ["Aplico P = 2 × (6 + 4).", "6 + 4 = 10.", "2 × 10 = 20 cm."], "20 cm"),
    ],
    [
        ("Escribir una fórmula sin unidades ni ejemplo.", "No se entiende cómo usarla.", "Agrega un ejemplo con unidades."),
        ("Mezclar fechas y hechos en desorden.", "La línea de tiempo pierde sentido.", "Ordénalos de la fecha más antigua a la más reciente."),
    ],
    [
        mr(IG1, "¿Cuál es la capa más delgada?", "La corteza", ["El manto", "El núcleo de la Tierra"], "Dice The crust is the thinnest layer."),
        mr(IG3, "¿Qué se fundó en 1950?", "La escuela", ["La biblioteca", "El laboratorio"], "Dice 1950: school founded."),
        mc("¿Para qué sirven las etiquetas de un diagrama?", "Para nombrar las partes del dibujo", ["Para decorar el dibujo con muchos colores", "Para sumar números"], "Cada etiqueta señala una parte."),
    ],
    [
        mr(IG3, "¿En qué año se agregó la sala de computación?", "En 2000", ["En 1980", "En 2020"], "Dice 2000: computer room."),
        mr(IG2, "¿Qué significa width?", "Ancho", ["Largo", "Perímetro"], "El glosario lo indica."),
        mr(IG4, "¿Qué problema tiene la infografía C?", "No tiene título, tiene letras muy pequeñas y colores que distraen", ["Tiene demasiadas fotos", "Tiene fórmulas"], "Dice sin título y letras muy pequeñas."),
    ],
    [
        arith("Un rectángulo mide 8 cm de largo y 3 cm de ancho. Usando P = 2 × (largo + ancho), ¿cuál es su perímetro?", "2*(8+3)", "Se suman largo y ancho y se multiplica por dos.", " cm"),
        mr(IG3, "¿Cuántos años pasaron entre la fundación (1950) y el laboratorio (2020)?", "70 años", ["60 años", "20 años"], "2020 menos 1950 son 70."),
        mr(IG1, "¿Cuántas capas se muestran con etiqueta?", "Tres", ["Dos", "Cuatro"], "Son crust, mantle y core."),
    ],
    [
        mr(IG3, "Una compañera propone escribir The school was found in 1950. ¿Qué corriges?", "The school was founded in 1950", ["The school is found in 1950", "The school finds in 1950"], "Un hecho histórico va en pasado, y el verbo es found/founded: was founded."),
        mr(IG2, "Un compañero escribe P = 2 × 6 + 4 = 16 cm. ¿Qué falla?", "Falta el paréntesis: 2 × (6 + 4) = 20 cm", ["Nada", "Debería restar"], "La fórmula suma largo y ancho antes de multiplicar."),
    ],
    [
        mr(IG1 + " " + IG4, "Compara las dos infografías. ¿Qué tiene la A que le falta a la C?", "Título y una idea principal clara", ["Más colores y más fotos", "Más texto en letras pequeñas y tres colores"], "Esos elementos aclaran el mensaje."),
        mr(IG3, "Quieres agregar una fecha a la línea de tiempo: «2010: school party». ¿Dónde va?", "Entre 2000 y 2020", ["Antes de 1950", "Después de 2020, al final"], "Se ordena cronológicamente."),
    ],
    [mc("Quieres hacer una infografía sobre las fases de una planta (semilla, brote, hoja, flor). ¿Qué recurso es el mejor?", "Un dibujo con cuatro etiquetas y flechas que muestren el orden", ["Un párrafo largo", "Una tabla de precios"], "El orden se muestra mejor con flechas.")],
    [
        ("En Inglés de 2.º medio (OA 13, clase 3): ¿qué debe tener el título de una infografía?", "El tema", "Orienta al lector."),
        ("En Inglés de 2.º medio (OA 13, clase 3): ¿qué se agrega a una fórmula para que se entienda?", "Un ejemplo con unidades", "Muestra cómo se usa."),
        ("En Inglés de 2.º medio (OA 13, clase 3): ¿cómo se ordenan los hechos de una línea de tiempo?", "De los más antiguos a los más recientes", "El orden cronológico es la regla."),
    ],
    task("Elige una asignatura (Ciencias, Matemática o Historia) y escribe en inglés el contenido de una infografía: un título, tres etiquetas o datos, una fórmula o fecha, y una frase de cierre. Dibuja el diseño en la hoja. Sigue este ejemplo.", "Ciencias: «Parts of a Plant». Etiquetas: roots, stem, leaves. Frase: Leaves make food for the plant. Cierre: Plants need light to grow.", ["título que dice el tema", "tres etiquetas o datos correctos", "una frase de cierre"], ["diseño dibujado en la hoja"], ["etiquetas sin relación con el dibujo", "olvidar el título"], "Pide que explique la relación entre dos etiquetas de la infografía."),
    "Dibuja una infografía con título y tres etiquetas sobre cualquier tema de Ciencias.",
    "Busca una infografía en una revista y anota qué hace que se entienda bien.",
)

# ------------------------------------------------------------------ clase 4: temas de interés global y culturas de otros países
GF1 = "Ficha de datos (fact file) sobre «Musical Instruments Around the World» (general). Datos: In the Andes, people play the panpipes, a set of tubes of different sizes. In many countries, the drum is used in festivals. The guitar has six strings in most models. Imagen: tres instrumentos dibujados con etiquetas. (panpipes = zampoña, tubes = tubos, strings = cuerdas, models = modelos)"
GF2 = "Ficha sobre «Languages of the World» (general). Datos: Spanish and English are spoken in many countries. Many people speak more than one language. Some languages have very few speakers today. Imagen: un mapamundi con puntos de colores."
GF3 = "Afiche mal escrito sobre una fiesta de otro país: «All people in that country eat the same food and wear the same clothes.» (all people = todas las personas, same = mismo, clothes = ropa)"
GF4 = "Ficha de ejemplo (inventada) sobre un país ficticio, Linora: «In Linora, children often walk to school together. Lunch is usually a soup and bread. The national sport is table tennis.» (usually = por lo general, soup = sopa, table tennis = tenis de mesa)"

lesson(
    OA, 4, MAT_R,
    "Aprenderé a escribir información relevante sobre temas de interés global y sobre la cultura de otros países, con datos generales y recursos visuales, evitando generalizaciones. Sirve para comunicar lo que aprendo con respeto y claridad.",
    ["Sé escribir fichas de datos.", "Conozco palabras como many, some y often."],
    [
        "Una ficha de datos (fact file) presenta información breve y ordenada sobre un tema: título, datos clave, imagen con etiquetas y una frase de cierre. Para temas de interés global, como los idiomas del mundo o los instrumentos musicales, usa datos generales que estés seguro de que son verdaderos. Si no estás seguro de un dato, no lo escribas o márcalo como de ejemplo.",
        "Al escribir sobre otras culturas, evita las generalizaciones. En lugar de All people eat the same food, escribe In many countries, people often eat rice; In some places, people usually... Las palabras many, some, often, usually, most y a few matizan. Describe, no juzgues: usa palabras neutrales como different, traditional y common. Si escribes sobre un país real, usa solo datos que domines y nombra tu fuente.",
        "Revisa tu ficha con tres preguntas: ¿cada dato es verdadero o está marcado como de ejemplo?, ¿evité las generalizaciones? y ¿el texto es respetuoso? Un buen texto no compara culturas diciendo cuál es mejor.",
    ],
    [("fact file", "ficha de datos"), ("global issue", "tema global"), ("generalization", "generalización"), ("many / some / often / usually", "matizadores"), ("traditional", "tradicional"), ("source", "fuente")],
    [
        ("Evaluar datos seguros", GF1 + " ¿Los datos son generales o muy específicos? ¿Qué haces antes de publicar la ficha?", ["Many countries y most models son expresiones generales.", "No hay cifras exactas que pueda equivocar.", "Aun así reviso una fuente antes de publicar."], "Son datos generales con matizadores; aun así reviso una fuente antes de publicar"),
        ("Evitar generalizar", GF3 + " ¿Cómo lo corriges?", ["All people es una generalización.", "Uso many o some.", "Escribo: In that country, many people eat traditional food during the festival."], "In that country, many people eat traditional food during the festival"),
    ],
    [
        ("Escribir All people in X do Y.", "Ninguna cultura es igual para todas las personas.", "Usa many, some, often o usually."),
        ("Presentar un dato inventado como real.", "Puede transmitir información falsa.", "Márcalo como de ejemplo."),
    ],
    [
        mr(GF2, "¿Cuántos idiomas habla mucha gente según la ficha?", "Más de uno", ["Ninguno", "Exactamente uno"], "Dice Many people speak more than one language."),
        mr(GF4, "¿Qué comen por lo general en el almuerzo en Linora?", "Sopa y pan", ["Arroz y carne", "Fruta"], "Dice Lunch is usually a soup and bread."),
        mc("¿Qué palabra suaviza una generalización?", "many", ["all", "never"], "Many deja espacio a las excepciones."),
    ],
    [
        mr(GF1, "¿Qué instrumento se menciona de los Andes?", "La zampoña", ["La guitarra eléctrica", "El piano"], "La ficha dice panpipes."),
        mr(GF4, "¿Qué deporte nacional de Linora se menciona?", "El tenis de mesa", ["El fútbol", "El básquetbol de calle"], "Dice The national sport is table tennis."),
        mr(GF2, "¿Qué dice la ficha de los idiomas con pocos hablantes?", "Que algunos tienen muy pocos hablantes", ["Que todos los idiomas tienen millones de hablantes", "Que no hay idiomas pequeños"], "Dice Some languages have very few speakers today."),
    ],
    [
        mr(GF3, "¿Qué palabra de la oración causa el problema?", "All", ["Eat", "Country"], "All generaliza a todos."),
        mc("Corrige la generalización: «All students in that country wear uniforms» (uniforms = uniformes).", "Many students in that country wear uniforms", ["Every student in that country wears uniforms", "All students in that country wear uniforms always"], "Many matiza la oración; every y always siguen generalizando."),
        mc("Corrige: «In Linora, all kids walk to school». ¿Cuál es mejor?", "In Linora, children often walk to school together", ["In Linora, children always walk to school together", "In Linora, no children walk to school at all"], "Often permite excepciones."),
    ],
    [
        mr(GF3, "Un compañero dice que el afiche mal escrito sobre una fiesta es respetuoso. ¿Qué respuesta es más acertada?", "No del todo: generaliza a todas las personas", ["Sí: es perfecta y respetuosa con todos", "Es falsa en todo y debe borrarse"], "Hay que matizar."),
        mr(GF4, "Una compañera pregunta si los datos de Linora son reales. ¿Qué responde alguien que lee con cuidado?", "No: Linora es un país ficticio", ["Sí: son reales y se pueden citar", "No se sabe: falta la fuente del país"], "Linora es inventada y la ficha es de ejemplo."),
    ],
    [
        mr(GF1 + " " + GF2, "¿Qué idea global comparten estas dos fichas?", "Que hay muchas formas de expresarse", ["Que todos los pueblos hablan el mismo idioma", "Que solo existe un tipo de instrumento"], "Instrumentos e idiomas muestran diversidad."),
        mr(GF3, "Escribe una oración mejor sobre una fiesta. ¿Cuál es adecuada?", "During the festival, many families share traditional food and music", ["During the festival, all people eat the same food and dance", "The festival is the best in the world and the others are boring"], "Matiza y evita comparar."),
    ],
    [mr(GF4, "Quieres agregar una frase de cierre a la ficha de Linora. ¿Cuál es adecuada?", "In Linora, people enjoy sports and school meals together", ["Linora is better than all countries", "No one in Linora likes music"], "Describe sin juzgar ni generalizar.")],
    [
        ("En Inglés de 2.º medio (OA 13, clase 4): ¿qué palabras evitan las generalizaciones?", "Many, some, often y usually", "Dejan espacio a las excepciones."),
        ("En Inglés de 2.º medio (OA 13, clase 4): ¿qué haces si no estás seguro de un dato?", "No lo uso o lo marco como de ejemplo", "Se evita información falsa."),
        ("En Inglés de 2.º medio (OA 13, clase 4): ¿qué parte tiene una ficha de datos?", "Título, datos clave, imagen con etiquetas y cierre", "Es su estructura básica."),
    ],
    task("Escribe una ficha de datos para un país ficticio llamado Marden: título, tres datos con many, some, often o usually, una imagen descrita con dos etiquetas y una frase de cierre respetuosa. Rotula la ficha como «de ejemplo». Sigue este ejemplo.", "Título: Marden (de ejemplo). Datos: Many people in Marden enjoy music. Children often play outdoors. Some families celebrate in spring. Imagen: un mapa con las etiquetas mountain y river. Cierre: Marden has traditions that people share.", ["título y rótulo de ejemplo", "tres datos con matizadores", "una frase de cierre respetuosa"], ["ficha en la hoja"], ["usar all o never", "presentar datos inventados como reales"], "Pide que explique por qué eligió cada matizador."),
    "Reescribe tres frases generalizadoras con many, some o often.",
    "Pregunta a una persona de tu casa por una costumbre de tu familia y escríbela con often o usually.",
)

# ------------------------------------------------------------------ clase 5: textos leídos y creación multimodal
TL1 = "«The Compass (original story). Rafa found an old compass in his grandfather's trunk. He thought it was broken because the needle always pointed north, not to his house. One day, he got lost in a park. He remembered his grandfather saying, The compass does not show where home is; it shows where you are. Rafa found the south gate and walked home.» (compass = brújula, trunk = baúl, needle = aguja, pointed = apuntaba, lost = perdido, gate = portón)"
TL2 = "«Bella the Street Cat (original story). Bella lived near a school and visited the classrooms at lunch. The students shared food and made her a bed. When winter came, they asked the principal if she could stay inside. He said yes, and Bella stayed with them.» (street cat = gata callejera, shared = compartieron, bed = camita, principal = director, stay = quedarse)"

lesson(
    OA, 5, MAT_R,
    "Aprenderé a escribir una respuesta creativa a un texto leído, con recursos multimodales: una tira cómica, un afiche o una carta con ilustración. Sirve para mostrar lo que entendí y compartirlo de forma original.",
    ["Sé resumir un texto.", "Sé usar pies de foto y globos."],
    [
        "Un texto leído puede inspirar una respuesta creativa (creative response): una tira cómica con globos de diálogo, un afiche con título y eslogan, una carta de un personaje a otro, un diario del protagonista. Para que la respuesta sea buena, debe mantener los hechos del texto, mostrar su idea principal y agregar algo propio, como un sentimiento o una moraleja.",
        "Primero, vuelve al texto y anota los hechos clave y la idea principal: en The Compass, Rafa aprende que la brújula muestra dónde estás. Segundo, elige el formato y los recursos: cuatro cuadros, globos con frases cortas, un pie de foto. Tercero, escribe el texto con claridad y revísalo: ¿respeta los hechos?, ¿tiene un título?, ¿la idea principal se entiende?",
        "Si cambias un dato del texto, decláralo como invención tuya (My version). Si copias frases del texto, usa comillas. En una respuesta creativa, tu voz importa: usa tus palabras, ejemplos y emociones, siempre apoyados en el texto.",
    ],
    [("creative response", "respuesta creativa a un texto"), ("comic strip", "tira cómica"), ("slogan", "eslogan"), ("moral", "moraleja"), ("main idea", "idea principal"), ("my version", "mi versión")],
    [
        ("Hechos clave y recurso", TL1 + " ¿Qué recurso eliges para una tira de cuatro cuadros y qué muestra cada cuadro?", ["Cuadro 1: Rafa encuentra la brújula.", "Cuadro 2: la cree rota. Cuadro 3: se pierde en el parque. Cuadro 4: recuerda las palabras y encuentra el portón.", "Cada cuadro tiene un hecho clave."], "Cuatro cuadros: encuentra la brújula, la cree rota, se pierde, recuerda y encuentra el portón"),
        ("Moraleja", TL1 + " ¿Cuál es una moraleja adecuada?", ["Rafa entiende que la brújula muestra dónde estás.", "Eso le ayuda a ubicarse.", "La moraleja: conocer dónde estás te ayuda a encontrar el camino."], "Saber dónde estás ayuda a encontrar el camino"),
    ],
    [
        ("Cambiar los hechos del texto sin decirlo.", "El lector cree que es el texto original.", "Escribe «My version» si cambias algo."),
        ("Hacer una respuesta que no tenga relación con la idea principal.", "No muestra comprensión del texto.", "Relaciónala con la idea principal."),
    ],
    [
        mr(TL2, "¿Qué hicieron los estudiantes por Bella?", "Compartieron comida y le hicieron una camita", ["La echaron del colegio cuando llegó el invierno", "La llevaron al veterinario del barrio"], "Dice The students shared food and made her a bed."),
        mr(TL1, "¿Dónde encontró Rafa la brújula?", "En el baúl de su abuelo", ["En un parque", "En su casa"], "Dice in his grandfather's trunk."),
        mc("¿Qué es una moraleja?", "Una enseñanza que deja la historia", ["El título del texto", "El nombre del personaje"], "Es la lección final."),
    ],
    [
        mr(TL2, "¿Qué pidieron los estudiantes al director?", "Que Bella pudiera quedarse adentro", ["Que la sacara", "Que cambiara la escuela"], "Dice they asked the principal if she could stay inside."),
        mr(TL1, "¿Qué creyó Rafa de la brújula?", "Que estaba rota", ["Que era nueva", "Que era de su amigo"], "Dice He thought it was broken."),
        mr(TL2, "¿Qué idea principal tiene el cuento de Bella?", "La solidaridad de los estudiantes ayudó a la gata", ["Los gatos de la calle son peligrosos para la escuela", "El director decide todo sin escuchar a nadie"], "Es el tema del texto."),
    ],
    [
        mr(TL2, "Planifica un afiche para el cuento de Bella. ¿Qué título y eslogan son adecuados?", "Title: Bella Finds a Home. Slogan: Little acts of kindness change lives.", ["Title: Bella Leaves the Town. Slogan: Be careful with street cats.", "Title: School Rules. Slogan: No pets here!"], "Relacionan el afiche con la idea principal."),
        mr(TL1, "En una tira cómica, ¿qué globo usas en el cuadro 4 de la historia de Rafa?", "«The compass shows where I am!»", ["«I hate the park!»", "«Buy a new compass!»"], "Es la idea principal."),
        arith("Un afiche permite como máximo 20 palabras. El título usa 4, el eslogan 6 y los pies de foto 5 palabras. ¿Cuántas palabras más caben?", "20-4-6-5", "Se restan las palabras usadas del máximo permitido.", " palabras"),
    ],
    [
        mr(TL2, "Un compañero dibuja a Bella como un perro. ¿Qué falla?", "Cambia un hecho: Bella es una gata", ["Nada: es solo un dibujo creativo", "Falta dibujar al director junto a ella"], "Hay que mantener los hechos del texto."),
        mr(TL1, "Otro compañero escribe que Rafa nunca se perdió. ¿Qué falla?", "Contradice el texto: se perdió", ["Nada: es una versión más alegre", "Es mejor así, porque el cuento termina bien"], "El texto dice he got lost."),
    ],
    [
        mr(TL2 + " " + TL1, "¿Qué tienen en común los dos cuentos?", "En ambos, alguien encuentra un lugar seguro", ["En ambos, un personaje se pierde y nadie lo ayuda", "En ambos, un personaje viaja a otra ciudad"], "Rafa vuelve a casa y Bella se queda en la escuela."),
        mr(TL1, "Quieres cambiar el final del cuento y presentarlo como tuyo. ¿Cómo lo señalas?", "Escribes «My version» y lo explicas", ["No dices nada y lo presentas igual", "Borras el título original y el autor"], "Declaras tu creación."),
    ],
    [mr(TL2, "Escribe una carta de Bella a los estudiantes. ¿Qué frase es adecuada?", "Dear students, thank you for the bed and the food", ["Dear principal, I hate this school", "Dear Rafa, here is a compass"], "Mantiene la relación con el texto.")],
    [
        ("En Inglés de 2.º medio (OA 13, clase 5): ¿qué debe mantener una respuesta creativa a un texto?", "Los hechos del texto y su idea principal", "Así muestra comprensión."),
        ("En Inglés de 2.º medio (OA 13, clase 5): ¿qué escribes si cambias un hecho?", "My version", "Declara que es tu versión."),
        ("En Inglés de 2.º medio (OA 13, clase 5): ¿qué es una moraleja?", "La enseñanza final", "Resume la lección."),
    ],
    task("Elige uno de los dos cuentos (The Compass o Bella the Street Cat) y crea una respuesta multimodal: una tira cómica de cuatro cuadros o un afiche. Escribe en inglés un título, dos pies de foto o globos y una moraleja de una oración. Revisa que respeta los hechos. Sigue este ejemplo.", "Cuento: Bella. Afiche: título «Bella Finds a Home»; imagen de una gata en una sala; globo «Thank you!»; moraleja: Kindness can give someone a home.", ["respeta los hechos del texto", "incluye título, dos textos breves y moraleja", "se entiende la idea principal"], ["tira o afiche en la hoja"], ["cambiar hechos sin declararlo", "olvidar la moraleja"], "Pide que explique qué agregó de propio a la respuesta."),
    "Haz una tira cómica de tres cuadros con globos sobre un cuento que leíste.",
    "Cuenta a alguien de tu casa un cuento y dibuja con él un cuadro clave.",
)
