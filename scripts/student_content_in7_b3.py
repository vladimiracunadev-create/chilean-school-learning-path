"""Cuaderno del estudiante, 7.º básico Inglés (oficial): IN07 OA 13, historias e información con recursos multimodales.

Los textos en inglés son originales, breves y llevan glosario en español dentro del enunciado. Las imágenes que se
mencionan se describen con palabras dentro del enunciado, para que se pueda resolver sin material externo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "IN07 OA 13"


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


# ============================================================ clase 1: propósito, género y audiencia
lesson(
    OA, 1,
    "Las situaciones y los bancos de palabras escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a elegir para qué escribo, qué tipo de texto uso y quién lo leerá. Sirve para que mis historias e información en inglés lleguen bien a quien las lee.",
    ["Sé escribir oraciones simples en inglés.", "Conozco palabras como email, poster y story."],
    [
        "Antes de escribir se deciden tres cosas. El propósito (purpose) es para qué escribes: contar una experiencia (to tell), dar información (to inform) o invitar a una acción (to invite). El género (genre) es el tipo de texto: un correo (email), una postal (postcard), un afiche (poster), un cuento (short story), un perfil cultural (cultural profile) o una entrada de diario (diary entry).",
        "La audiencia (audience) es quien leerá: tus compañeros, una profesora, un niño pequeño o un amigo de otro país. Según la audiencia cambia el tono y las palabras. A un amigo le escribes Hi Sam! y Bye!; a una profesora, Dear Ms. Rojas y Best wishes. Un afiche usa frases cortas y grandes; un correo usa oraciones completas.",
        "Los temas pueden ser una experiencia personal (a school trip), un contenido de otra asignatura (the water cycle), un problema global (plastic in the sea), la cultura de otro país o algo que leíste. Cuando eliges propósito, género y audiencia juntos, tu texto queda claro. Anótalos en una línea antes de empezar: «I write a ___ for ___ to ___».",
    ],
    [("purpose", "propósito"), ("genre", "género: tipo de texto"), ("audience", "audiencia: quien lee"), ("to inform", "informar"), ("to invite", "invitar"), ("diary entry", "entrada de diario"), ("pen pal", "amigo por correspondencia")],
    [
        ("Elegir propósito, género y audiencia", "Situación: quieres contarle a tu amigo por correspondencia de otro país cómo fue tu paseo de curso. (pen pal = amigo por correspondencia; school trip = paseo de curso) ¿Qué propósito, género y audiencia eliges?",
         ["Cuentas una experiencia personal: el propósito es contar.", "Escribes a una persona concreta: el género puede ser un correo o una postal.", "La audiencia es tu amigo por correspondencia."], "Propósito: contar una experiencia. Género: correo o postal. Audiencia: mi amigo por correspondencia."),
        ("Ajustar el tono a la audiencia", "Escribes a tu profesora de Ciencias para avisar que llegarás atrasado. ¿Cuál saludo usas: «Hi, teacher!» o «Dear Ms. Silva,»?",
         ["La audiencia es una profesora: pide un tono respetuoso.", "«Dear Ms. Silva,» es un saludo formal.", "«Hi, teacher!» es muy informal."], "Dear Ms. Silva,"),
    ],
    [
        ("Usar el mismo texto y tono para cualquier audiencia.", "No se piensa en quién lee.", "Antes de escribir, anota la audiencia y ajusta saludo y palabras."),
        ("Escribir sin saber para qué.", "Falta decidir el propósito.", "Completa: «I write a ___ for ___ to ___»."),
    ],
    [
        ("En Inglés (oficial): ¿Qué es la audiencia de un texto?", "Las personas que lo leerán", "Por ella se elige el tono."),
        ("Quieres invitar a tus compañeros a una limpieza de playa. ¿Qué propósito tiene tu texto? a) Invitar b) Contar un recuerdo", "a", "Pides que participen en una acción."),
        ("¿Cuál es un género? a) poster b) happy", "a", "Poster es un tipo de texto; happy es una palabra de sentimiento."),
    ],
    [
        ("Quieres dar información sobre el ciclo del agua (the water cycle) a niños de 8 años. ¿Qué propósito es? a) Informar b) Invitar", "a", "Explicas un contenido; no pides una acción."),
        ("Escribes a un amigo muy cercano. ¿Qué saludo es mejor? a) Hi Pedro! b) Dear Mr. Gonzalez,", "a", "Con un amigo cercano se usa un tono informal."),
        ("Quieres mostrar a tu curso las fiestas de un país lejano. ¿Qué género es mejor? a) cultural profile b) shopping list", "a", "El perfil cultural describe costumbres de un lugar."),
    ],
    [
        ("Elige el afiche más claro para la audiencia: niños pequeños. a) «Plant a tree! Join us on Friday!» b) «We hereby request the voluntary participation of individuals in reforestation activities.» (reforestation = reforestación)", "a", "Usa frases cortas y sencillas, adecuadas para niños pequeños."),
        ("Quieres contar un recuerdo de tu cumpleaños. ¿Qué género sirve mejor para contar un recuerdo personal? a) diary entry b) weather report", "a", "El diario sirve para experiencias personales."),
        ("Un texto dice: «Dear Mr. Fuentes, I am writing to ask for a book.» (ask for = pedir) ¿Cuál es la audiencia más probable? a) un adulto al que se respeta b) un amigo de infancia", "a", "Dear Mr. y la petición formal indican un tono respetuoso."),
    ],
    [
        ("Sofía y Tomás escriben sobre el plástico en el mar. Sofía quiere informar con datos; Tomás quiere pedir a sus compañeros que dejen de usar bolsas. ¿Qué propósito tiene el texto de Tomás? a) Invitar a actuar b) Contar un recuerdo", "a", "Quiere que otros cambien su conducta."),
        ("Si el propósito es dar información y la audiencia es tu curso, ¿qué recurso ayuda más? a) Un título y datos ordenados b) Un poema de amor", "a", "Un título y datos facilitan entender la información."),
    ],
    [
        ("Lee los datos: Texto 1 es «Hi Dani! Come to my party on Saturday!» y Texto 2 es «Dear Director, we request permission to use the gym on Friday.» (permission = permiso; gym = gimnasio) ¿Cuál texto tiene audiencia formal? Escribe 1 o 2.", "2", "Dear Director y la petición de permiso indican un tono formal."),
        ("Un afiche invita a niños de 6 años a una función de títeres (puppets). ¿Cuál es el mejor texto para esa audiencia? a) «Puppet show! Friday at 4!» b) «We cordially invite you to a puppet performance on Friday afternoon.»", "a", "Frases cortas y claras son adecuadas para niños pequeños."),
    ],
    [("Tu profesor te da tres situaciones: invitar a tu curso a una campaña de reciclaje, contarle a tu abuela por qué te gustó un museo y explicar a un niño pequeño cómo cuidar el agua. Para la primera conviene escribir: a) un afiche con frases cortas b) una carta larga", "a", "Un afiche con frases cortas invita y se lee rápido.")],
    [
        ("¿Qué tres cosas decides antes de escribir?", "Propósito, género y audiencia", "Ordenan todo el texto."),
        ("«Dear Ms. Rojas» es un saludo: a) formal b) informal", "a", "Se usa con una profesora, de modo respetuoso."),
        ("Completa: «I write a postcard for my cousin to ___.» Opciones: share news about my holiday, divide numbers.", "share news about my holiday", "Una postal sirve para compartir noticias de las vacaciones."),
    ],
    task("Lee estas dos situaciones: 1) Quieres explicar a niños de 8 años por qué cuidar el agua. 2) Quieres contarle a tu tío que vive lejos qué hiciste en tus vacaciones. En tu hoja escribe, para cada una: propósito, género y audiencia, y un saludo adecuado. Usa las palabras del vocabulario.", "1) Informar; afiche; niños de 8 años; Hi, kids! 2) Contar; correo o postal; mi tío; Dear Uncle Luis,", ["define propósito, género y audiencia para ambas", "el saludo calza con la audiencia", "usa palabras del vocabulario"], ["hoja con dos fichas"], ["usar el mismo género para ambas", "olvidar a la audiencia"], "Pregunta cómo cambiaría la ficha si la audiencia fuera el director."),
    "Copia los siete términos de la tabla con su significado.",
    "Escribe tres saludos en inglés: uno informal, uno formal y uno para un afiche.",
)

# ============================================================ clase 2: planificar con un organizador
lesson(
    OA, 2,
    "Las notas y organizadores escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a ordenar mis ideas con un organizador visual antes de escribir: un cuadro de preguntas, un mapa de ideas o un guion gráfico. Sirve para que mi texto tenga orden y no se me olvide nada importante.",
    ["Sé elegir propósito, género y audiencia.", "Conozco las palabras who, what, where, when y why."],
    [
        "Un organizador visual (visual organizer) es un dibujo o una tabla donde ordenas ideas antes de escribir. El cuadro de las cinco preguntas (5W chart) usa Who? (¿quién?), What? (¿qué?), Where? (¿dónde?), When? (¿cuándo?) y Why? (¿por qué?). Sirve para experiencias, noticias y cuentos.",
        "El mapa de ideas (mind map) pone el tema al centro y las ideas alrededor, como ramas. Sirve para información: por ejemplo, el centro dice «Plastic in the sea» y las ramas «Causes», «Effects», «Solutions». El guion gráfico (storyboard) divide la historia en cuadros numerados: inicio, problema y final, con un dibujo y una frase en cada uno.",
        "Al planificar, escribe palabras clave, no oraciones completas. Si una idea no calza con el tema o el propósito, descártala. Luego revisa el organizador: ¿están todas las partes? ¿están en el orden en que lo contarás? Un buen plan te ahorra volver a escribir después.",
    ],
    [("5W chart", "cuadro de las cinco preguntas"), ("mind map", "mapa de ideas"), ("storyboard", "guion gráfico"), ("cause", "causa"), ("effect", "efecto"), ("solution", "solución"), ("plan", "planificar")],
    [
        ("Llenar un cuadro de cinco preguntas", "Notas: «Ana, school garden, Friday, plant tomatoes, to eat healthy food». (tomatoes = tomates; healthy = sano) Ordénalas en Who, What, Where, When y Why.",
         ["Ana responde Who.", "Plant tomatoes responde What; school garden, Where; Friday, When.", "To eat healthy food responde Why."], "Who: Ana. What: plant tomatoes. Where: school garden. When: Friday. Why: to eat healthy food."),
        ("Elegir qué va en un mapa de ideas", "Tema central: «Plastic in the sea». Ramas: Causes, Effects, Solutions. ¿Dónde pondrías «Use cloth bags» (bolsas de tela)?",
         ["La idea dice qué hacer para ayudar.", "Eso es una solución.", "Va en la rama Solutions."], "En la rama Solutions."),
    ],
    [
        ("Escribir oraciones completas en el organizador.", "Se confunde planificar con redactar.", "Anota solo palabras clave; las oraciones vienen después."),
        ("Dejar en el plan ideas que no calzan con el tema.", "No se revisa el propósito.", "Tacha lo que no apoye lo que quieres decir."),
    ],
    [
        ("¿Qué pregunta responde «Where?»", "¿Dónde?", "Where? pide el lugar."),
        ("En un mapa de ideas, el tema va: a) al centro b) en una esquina", "a", "Las ideas se ordenan alrededor del tema central."),
        ("Un storyboard sirve para: a) ordenar una historia en cuadros b) calcular distancias", "a", "Muestra inicio, problema y final con dibujos."),
    ],
    [
        ("Notas: «Leo, soccer, the park, Saturday, because he likes sports». Según el cuadro 5W, ¿qué respuesta es Where?", "the park", "El parque es el lugar."),
        ("Mapa de ideas con el tema «Healthy habits» (hábitos sanos). ¿Qué rama sobra? a) Sleep eight hours b) Football score", "b", "El resultado de un partido no se relaciona con hábitos sanos."),
        ("Storyboard de cuatro cuadros de una historia: 1) A girl loses her cat. 2) She puts up signs. 3) A boy finds the cat. 4) The cat is home. ¿Qué cuadro presenta el problema?", "1", "En el cuadro 1 se pierde el gato."),
    ],
    [
        ("Notas para un perfil de un país: «Brazil, Portuguese, football, big country». (big = grande) Ordénalas: ¿qué nota es el nombre del país?", "Brazil", "Es el dato central."),
        ("Quieres escribir sobre el reciclaje en tu colegio. Tienes estas ideas: «bins for paper», «bins for plastic», «my favourite cartoon». (bins = basureros) ¿Cuál no va en tu plan?", "my favourite cartoon", "No se relaciona con el reciclaje."),
        ("Cuadro 5W de un cuento: Who = a fox, What = looks for food, Where = in the forest, When = at night. Falta Why. ¿Cuál puede ser? a) because it is hungry b) because it is Monday", "a", "Buscar comida se explica por el hambre."),
    ],
    [
        ("Dos compañeros ordenan «Use a bike, Walk to school, Take the bus» en un mapa de ideas sobre el transporte. Uno los pone en «Problems», el otro en «Ways to help the planet». ¿Quién tiene razón? Escribe Problems o Ways to help.", "Ways to help", "Son acciones que ayudan al planeta, no problemas."),
        ("Planificas un correo con 5W: Who = Marta, What = invites you to a party, Where = her house, When = Sunday 4 pm. ¿Qué dato falta del cuadro? a) Why b) Email address", "a", "Falta el motivo de la invitación."),
    ],
    [
        ("Notas: «big waves, surfing, beach, summer, my cousin». Tu propósito es contar un paseo. ¿Qué nota responde Who? Escribe la nota.", "my cousin", "Indica quién participa."),
        ("Storyboard con 3 cuadros: Cuadro 1 muestra a un niño con un perro. Cuadro 3 muestra al niño feliz. ¿Qué debe mostrar el cuadro 2? a) El problema o la acción central b) El nombre del autor", "a", "El cuadro central desarrolla el problema."),
    ],
    [("Tu profesora te pide escribir sobre cómo cuidar el agua. En tu mapa de ideas tienes las ramas: Home, School y Street. ¿Dónde pones «Turn off the tap while brushing teeth»? (tap = llave) a) Home b) Street", "a", "Esa acción se hace en la casa, al lavarse los dientes.")],
    [
        ("¿Cuáles son las cinco preguntas del cuadro 5W?", "Who, What, Where, When y Why", "Cubren los datos básicos."),
        ("¿Qué escribes en un organizador: oraciones o palabras clave?", "Palabras clave", "El organizador es un plan, no el texto final."),
        ("Una rama «Solutions» en un mapa de ideas incluye: a) maneras de ayudar b) causas del problema", "a", "Solutions son soluciones."),
    ],
    task("Lee estas notas para un texto sobre una campaña de limpieza: «Camila, Pedro, the beach, Saturday morning, clean the sand, to protect the sea animals, I like football». (sand = arena; protect = proteger; sea animals = animales marinos) En tu hoja dibuja un cuadro 5W y colócalas. Tacha la nota que no calza. Después dibuja un storyboard de tres cuadros con una frase en cada uno.", "Who: Camila y Pedro. What: clean the sand. Where: the beach. When: Saturday morning. Why: to protect the sea animals. Tachar: I like football.", ["ubica cada nota en la pregunta correcta", "tacha la nota que no calza", "el storyboard tiene inicio, problema y final"], ["cuadro 5W y storyboard en la hoja"], ["poner una nota en la pregunta equivocada", "dejar la nota irrelevante"], "Pide que explique por qué la nota tachada no aporta."),
    "Dibuja un cuadro 5W en blanco y escribe las cinco preguntas con su significado.",
    "Haz un mapa de ideas con tema «My school» y tres ramas con una palabra clave cada una.",
)

# ============================================================ clase 3: redactar un mensaje completo
lesson(
    OA, 3,
    "Los borradores y bancos de frases escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a redactar un mensaje completo, con inicio, desarrollo y cierre, a partir de mi plan. Sirve para que quien me lea entienda mi texto sin preguntarme nada.",
    ["Sé planificar con un cuadro 5W.", "Sé escribir oraciones con sujeto y verbo."],
    [
        "Un mensaje completo tiene tres partes. El inicio (opening) presenta el tema o la situación: «Last Saturday, I went to the beach with my class.» El desarrollo (body) da los detalles en orden: qué pasó, dónde, con quién y por qué. El cierre (closing) termina con una idea final o un saludo: «It was a great day!» o «See you soon!».",
        "Escribe un borrador (draft) pasando cada nota de tu plan a una oración. Una oración tiene al menos sujeto y verbo: «We cleaned the sand.» Une las ideas con and, but, because y then. No te detengas a corregir cada falta ahora: lo importante en un borrador es que todas las ideas estén.",
        "Un mensaje completo responde las preguntas del lector: quién, qué, dónde, cuándo y por qué. Si falta una respuesta, el lector se queda con dudas. Usa palabras de orden como first, next, then y finally para guiar. Al terminar, léelo en voz baja y pregúntate si tiene inicio, desarrollo y cierre.",
    ],
    [("opening", "inicio"), ("body", "desarrollo"), ("closing", "cierre"), ("draft", "borrador"), ("detail", "detalle"), ("first / next / finally", "primero / luego / finalmente"), ("topic sentence", "oración que presenta el tema")],
    [
        ("Reconocer las tres partes", "Texto: «Last Friday, I visited a farm with my class. We saw cows, hens and sheep. A farmer showed us how to milk a cow. It was a great day!» (farm = granja; hens = gallinas; sheep = ovejas; milk = ordeñar) ¿Cuál es el inicio, el desarrollo y el cierre?",
         ["La primera oración presenta el paseo.", "La segunda y la tercera dan detalles.", "La última cierra con una opinión."], "Inicio: Last Friday I visited a farm. Desarrollo: vimos animales y el granjero mostró cómo ordeñar. Cierre: It was a great day!"),
        ("Pasar una nota a oración", "Nota del plan: «Ana, school garden, Friday, plant tomatoes». Escribe una oración completa.",
         ["Une quién, qué, dónde y cuándo.", "Usa un verbo en pasado: planted.", "Ana planted tomatoes in the school garden on Friday."], "Ana planted tomatoes in the school garden on Friday."),
    ],
    [
        ("Escribir solo palabras sueltas en el borrador.", "Se deja el plan como texto.", "Convierte cada nota en una oración con sujeto y verbo."),
        ("Terminar sin cierre.", "Se corta el texto cuando se acaban los datos.", "Agrega una frase final como «It was fun!» o «See you soon!»."),
    ],
    [
        ("¿Qué parte presenta el tema?", "El inicio (opening)", "Es la primera parte del mensaje."),
        ("¿Cuál es una oración completa? a) We cleaned the sand b) Cleaned the sand.", "a", "Tiene sujeto (We) y verbo (cleaned)."),
        ("Para el cierre de un correo a un amigo, ¿qué sirve? a) See you soon! b) Last Monday I", "a", "Se despide con una idea final."),
    ],
    [
        ("Ordena las partes: x) We played games and ate lunch. y) Last Sunday, I went to the park with my cousins. z) It was a fun day! Escribe las letras de inicio, desarrollo y cierre.", "y, x, z", "Primero presenta el paseo, luego los detalles y al final el cierre."),
        ("Elige el mejor inicio para un mensaje sobre un paseo al zoológico. a) Last Tuesday, my class visited the zoo b) Many animals.", "a", "El inicio presenta cuándo y quién fue de paseo."),
        ("Completa con la palabra de orden: «___ we saw the monkeys. Then we saw the lions.» Opciones: First, Finally.", "First", "Primero va antes de then y marca el comienzo."),
    ],
    [
        ("Tienes las notas «Leo, soccer, the park, Saturday». ¿Qué versión es una oración completa? a) Leo played soccer in the park on Saturday b) Leo soccer park Saturday.", "a", "La primera es una oración completa con verbo."),
        ("Un correo dice: «Hi Ana! Yesterday I made a cake with my mom. First we mixed the eggs, then we baked it.» (mixed = mezclamos; baked = horneamos) Falta el cierre. ¿Cuál sirve? a) It was delicious! Bye! b) Hi Ana!", "a", "Termina con una idea final y una despedida."),
        ("Lee: «We saw a big whale. It was beautiful.» (whale = ballena) ¿Qué pregunta del lector queda sin respuesta? a) Where? b) Who?", "a", "No se dice en qué lugar la vieron."),
    ],
    [
        ("Un borrador dice: «The beach. Sand. Friends.» ¿Qué le falta? a) Oraciones completas con verbo b) Más palabras sueltas", "a", "Solo hay palabras sueltas; faltan oraciones."),
        ("Lee: «I visited a farm. We saw cows. I like pizza. The farmer was kind.» (kind = amable) ¿Qué oración sobra? Escribe cuál.", "I like pizza", "No se relaciona con la visita a la granja."),
    ],
    [
        ("Lee el mensaje: «Dear Aunt Rosa, last week my class planted ten trees in the park. We worked together. I am happy because the park is greener now.» (planted = plantó; greener = más verde) ¿Qué función tiene la última oración? a) Cierra con una razón b) Presenta el tema", "a", "Termina con una idea final."),
        ("Para escribir sobre un problema global, como la basura en la calle, ¿qué orden de tres oraciones es el mejor? a) Tema, detalle, cierre b) Cierre, tema, detalle", "a", "Un mensaje completo se organiza en ese orden."),
    ],
    [("En una prueba te piden escribir tres oraciones sobre tu recreo ideal. ¿Cuál es el mejor inicio? a) At recess, I like playing soccer with my friends. b) Soccer with friends", "a", "Presenta el tema con una oración completa.")],
    [
        ("¿Cuáles son las tres partes de un mensaje completo?", "Inicio, desarrollo y cierre", "Estructuran el texto."),
        ("¿Qué es un borrador?", "Una primera versión que se puede mejorar", "Se corrige después."),
        ("Completa: «___ we packed our bags. Then we left.» Opciones: First, Finally.", "First", "La primera acción lleva First."),
    ],
    task("Usa este plan: «Who: my class and I. What: visited a museum of science. Where: Santiago. When: last Thursday. Why: to learn about space. Detail: we saw a model of the Moon.» (museum = museo; space = espacio; model = maqueta) En tu hoja escribe un mensaje de cinco oraciones para tu amigo por correspondencia con saludo, inicio, desarrollo con dos detalles y cierre.", "Hi Tom! Last Thursday, my class and I visited a science museum in Santiago. We went to learn about space. We saw a model of the Moon. The guide told us many facts. It was a great day! Bye!", ["usa todos los datos del plan", "tiene inicio, desarrollo y cierre", "las oraciones tienen sujeto y verbo"], ["mensaje de cinco oraciones en la hoja"], ["dejar fuera el dónde o el cuándo", "terminar sin cierre"], "Pide que subraye con colores inicio, desarrollo y cierre."),
    "Copia el modelo de tres partes de la explicación con un ejemplo propio en cada una.",
    "Escribe un mensaje de cuatro oraciones sobre tu desayuno, con inicio, desarrollo y cierre.",
)

# ============================================================ clase 4: integrar imagen y diseño
lesson(
    OA, 4,
    "Las descripciones de imágenes y diseños escritas en cada ejercicio, lápiz, una hoja y lápices de colores.",
    "Aprenderé a elegir una imagen, a escribir un pie de foto y a ordenar el diseño de mi texto para reforzar el mensaje. Sirve para que mi afiche, mi folleto o mi historia comuniquen mejor.",
    ["Sé escribir un mensaje con inicio, desarrollo y cierre.", "Sé qué es un título y un subtítulo."],
    [
        "Un texto multimodal combina palabras con otros recursos: imágenes (images), colores, tamaños de letra, listas y títulos. Estos recursos deben reforzar el mensaje, no solo decorar. Si escribes sobre reciclaje, una imagen de basureros de colores ayuda; una imagen de un partido de fútbol no.",
        "El pie de foto (caption) es una frase corta bajo la imagen que explica lo que se ve: «Students recycle paper at school.» El título (title) va arriba y en letra grande. Los subtítulos (headings) separan partes. Una lista con viñetas (bullet points) ordena ideas cortas: • Use both sides of the paper. El diseño (layout) debe guiar la lectura: primero el título, luego la imagen, luego el texto.",
        "Cuando usas una imagen o una idea que no es tuya, indica la fuente (source): «Photo: my own», «Drawing: by me» o «Source: school book». Así reconoces a quien la creó. No copies textos ajenos. Si dibujas tú, tu dibujo es tuyo; si usas el de otra persona, anota de dónde viene.",
    ],
    [("image", "imagen"), ("caption", "pie de foto"), ("layout", "diseño: cómo se ordena la página"), ("heading", "subtítulo o encabezado"), ("bullet point", "viñeta de lista"), ("source", "fuente: de dónde viene"), ("reinforce", "reforzar")],
    [
        ("Elegir la imagen que refuerza el mensaje", "Escribes sobre cuidar el agua. Imágenes: a) Una llave goteando (dripping tap) b) Un partido de fútbol. ¿Cuál refuerza el mensaje?",
         ["El tema es el agua.", "Una llave goteando se relaciona con desperdiciar agua.", "El partido no tiene relación."], "La llave goteando."),
        ("Escribir un pie de foto", "Imagen: tres niños plantan un árbol en el patio. Escribe un pie de foto en inglés.",
         ["Dice lo que se ve: children, plant, tree.", "Es una frase corta.", "Children plant a tree in the school yard."], "Children plant a tree in the school yard."),
    ],
    [
        ("Poner una imagen bonita que no se relaciona con el texto.", "Se usa la imagen para decorar.", "Elige una imagen que refuerce lo que dice el texto."),
        ("Usar imágenes ajenas sin decir de dónde son.", "Se olvida citar la fuente.", "Escribe «Source:» o usa tus propios dibujos."),
    ],
    [
        ("En Inglés (oficial): ¿Qué es un pie de foto?", "Una frase corta bajo la imagen que explica lo que se ve", "Ayuda a entender la imagen."),
        ("¿Dónde va el título? a) Arriba y en letra grande b) Al final y muy pequeño", "a", "El título guía la lectura desde el comienzo."),
        ("Una viñeta de lista (bullet point) sirve para: a) ordenar ideas cortas b) escribir un poema largo", "a", "Las listas organizan datos cortos."),
    ],
    [
        ("Escribes sobre reciclaje. ¿Qué imagen refuerza el mensaje? a) Basureros de colores b) Un volantín", "a", "Se relaciona con separar los residuos."),
        ("Imagen: una niña riega una planta con un regador. ¿Qué pie de foto calza? a) A girl waters a plant b) A boy eats lunch.", "a", "Describe la acción de la imagen."),
        ("Para citar tu propio dibujo, escribes: a) Drawing: by me b) Drawing: the Internet", "a", "Se dice que el dibujo es tuyo."),
    ],
    [
        ("Tu afiche dice: «Turn off the light!» Imagen: una ampolleta encendida en una pieza vacía. (light bulb = ampolleta) ¿La imagen refuerza el mensaje? Responde sí o no.", "Sí", "Muestra luz encendida sin nadie, lo que el mensaje pide evitar."),
        ("Ordena el diseño de un folleto: x) Texto con datos y viñetas y) Título z) Imagen con pie de foto. Escribe el orden más claro de lectura.", "y, z, x", "Primero el título, luego la imagen y por último el texto."),
        ("Una foto de un parque lleva este pie: «A bus stops at the school.» ¿Calza con la foto? Responde sí o no.", "No", "Habla de un bus y la foto muestra un parque."),
    ],
    [
        ("Compañera A usa un título pequeño y pone la imagen al final. Compañero B usa un título grande arriba. Para guiar la lectura, ¿cuál lo hace mejor? Escribe A o B.", "B", "El título grande arriba guía desde el inicio."),
        ("Tu folleto sobre ahorrar agua tiene dos imágenes: una llave goteando y una piscina con gente. Solo cabe una. Si el texto dice «Close the tap», ¿cuál eliges? Escribe la imagen.", "la llave goteando", "Calza con el mensaje de cerrar la llave."),
    ],
    [
        ("Lee este folleto: «Title: Save Paper! • Use both sides. • Reuse old notebooks. • Recycle at school. Photo: students with a paper bin. Source: own photo.» (reuse = reutilizar; bin = basurero) ¿Cuántos puntos con viñetas tiene?", "3", "Hay tres líneas con viñeta: both sides, old notebooks y recycle."),
        ("Mismo folleto: «Title: Save Paper! • Use both sides. • Reuse old notebooks. • Recycle at school. Photo: students with a paper bin. Source: own photo.» ¿De quién es la foto? Responde en español.", "Propia", "Dice Source: own photo."),
    ],
    [("Tienes un afiche sobre cuidar las plazas. Falta un pie de foto para la imagen de un niño que recoge basura. ¿Cuál escribes? a) A boy picks up litter b) A dog sleeps.", "a", "Describe lo que se ve en la imagen.")],
    [
        ("¿Para qué sirve la fuente (source) de una imagen?", "Para decir de dónde viene", "Reconoce a quien la hizo."),
        ("Una imagen debe: a) reforzar el mensaje b) solo decorar", "a", "Debe tener relación con el texto."),
        ("¿Qué recurso agrupa ideas cortas en una lista? a) Bullet points b) Captions", "a", "Las viñetas ordenan datos cortos."),
    ],
    task("Imagina un afiche para tu colegio sobre «Walk to school» (ir caminando al colegio). En tu hoja diseña: a) un título en inglés, b) una descripción de la imagen principal con su pie de foto, c) tres viñetas con consejos cortos, d) la fuente de la imagen, e) un dibujo rápido del orden de la página.", "a) Walk to School! b) Imagen: niños caminando juntos; pie: Children walk to school together. c) • Walk with a friend. • Use the crosswalk. • Look both ways. d) Drawing: by me. e) Título, imagen, viñetas.", ["la imagen refuerza el título", "el pie de foto describe la imagen", "indica la fuente", "el orden guía la lectura"], ["afiche con título, imagen, pie, viñetas y fuente"], ["imagen sin relación con el tema", "no citar la fuente"], "Pide que explique cómo ayuda cada recurso a entender el mensaje."),
    "Copia el vocabulario de la tabla con un dibujo pequeño en image, bullet point y heading.",
    "Escribe pies de foto en inglés para dos fotos imaginarias de tu familia o tus mascotas, sin nombres propios.",
)

# ============================================================ clase 5: revisar para dar claridad y efecto
lesson(
    OA, 5,
    "Los borradores escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a revisar mi texto para que sea más claro y tenga más efecto en quien lee. Sirve para mejorar un borrador cambiando palabras vagas, repeticiones y el orden de las ideas.",
    ["Sé redactar un mensaje con inicio, desarrollo y cierre.", "Conozco palabras como good, nice, big y very."],
    [
        "Revisar (to revise) es mejorar el borrador. Primero revisa el contenido: ¿se entiende el propósito?, ¿están todas las ideas?, ¿están en un orden lógico?, ¿sobra algo que no apoya el tema? Después revisa la claridad y el efecto: ¿las palabras son precisas?, ¿hay repeticiones?, ¿el lector entenderá y sentirá lo que quieres?",
        "Una herramienta útil es reemplazar las palabras vagas por palabras precisas. En vez de nice, usa beautiful, friendly o delicious. En vez de «We went», puedes decir «We walked» o «We climbed». También conviene evitar repetir la misma palabra tres veces: usa he, she, it, they o un sinónimo. Para dar efecto, agrega un detalle con los sentidos: «The water was icy and clear.»",
        "Usa una lista de revisión (checklist): 1) ¿Dice lo que quería? 2) ¿Tiene inicio, desarrollo y cierre? 3) ¿Sobra o falta algo? 4) ¿Cambié palabras vagas? 5) ¿Funciona la imagen o el diseño? Revisa de a una cosa por vez. Al final, lee en voz alta: si algo suena confuso, vuelve a escribirlo.",
    ],
    [("revise", "revisar y mejorar"), ("clear", "claro"), ("vague", "vago, poco preciso"), ("precise", "preciso"), ("repeat", "repetir"), ("detail", "detalle"), ("checklist", "lista de revisión")],
    [
        ("Cambiar una palabra vaga por una precisa", "Oración: «We ate a nice soup.» (soup = sopa) Mejórala con una palabra más precisa: delicious o hot (caliente).",
         ["Nice no dice qué tipo de bueno es.", "Delicious dice que sabía rico.", "We ate a delicious soup."], "We ate a delicious soup."),
        ("Evitar la repetición", "Texto: «Marta has a dog. Marta's dog is brown. Marta's dog likes to run.» (brown = café) Reescríbelo con menos repeticiones.",
         ["Marta se repite tres veces.", "Usa he, she o it.", "Marta has a dog. It is brown and it likes to run."], "Marta has a dog. It is brown and likes to run."),
    ],
    [
        ("Corregir solo la ortografía y creer que ya está revisado.", "Se mira solo la forma y no el contenido.", "Revisa primero ideas y orden; después las faltas."),
        ("Repetir la misma palabra en cada oración.", "Se usa lo primero que se viene a la mente.", "Usa he, she, it, they o un sinónimo."),
    ],
    [
        ("En Inglés (oficial): ¿Qué significa «revise»?", "Revisar y mejorar un texto", "Se hace después del borrador."),
        ("Una palabra vaga es: a) nice b) delicious", "a", "Nice puede significar muchas cosas."),
        ("¿Qué revisas primero: contenido o faltas de ortografía?", "El contenido", "Las ideas y el orden van antes."),
    ],
    [
        ("Mejora la oración «We went to the beach» con un verbo más preciso. a) We walked to the beach b) We went to the beach and we went to the sea.", "a", "Walked dice cómo fueron."),
        ("Reemplaza la palabra vaga en: «It was a good movie.» a) It was an exciting movie b) It was a good good movie.", "a", "Exciting aporta una idea precisa."),
        ("Texto: «The bird is blue. The bird is small. The bird sings.» ¿Cómo cambias la repetición? a) The bird is small and blue, and it sings b) The bird is blue and the bird is small and the bird sings.", "a", "Une ideas y usa it."),
    ],
    [
        ("Borrador: «Last Friday we planted trees. I love pizza. We worked together.» ¿Qué oración quitas al revisar el contenido?", "I love pizza", "No apoya el tema de plantar árboles."),
        ("Borrador: «We were tired. We finished. We cleaned the beach. We started to clean.» ¿Cuál es el orden lógico? a) We started to clean. We cleaned the beach. We finished. We were tired. b) Como está", "a", "Las acciones van en el orden en que ocurren."),
        ("Quieres dar efecto con un detalle de los sentidos: «The water was ___.» Opciones: icy and clear, nice and good.", "icy and clear", "Da una imagen precisa del agua."),
    ],
    [
        ("Un compañero cambia «She is nice» por «She is nice and very nice». ¿Mejora la claridad? Responde sí o no.", "No", "Repite la palabra vaga sin agregar información."),
        ("Mejora el final. ¿Cuál tiene más efecto y deja una idea? a) «That day I learned to share, and I felt proud.» b) «The end.»", "a", "Da una idea final y un sentimiento."),
    ],
    [
        ("Revisa: «My cat is nice. My cat sleeps. My cat eats.» Elige la mejor versión. a) My cat is friendly. It sleeps a lot and eats fish b) My cat is nice. My cat sleeps and my cat eats.", "a", "Cambia nice por friendly y evita repeticiones."),
        ("Borrador: «First we ate lunch. Next we cooked rice. Then we made a salad. Finally we washed the dishes.» (rice = arroz; dishes = platos) ¿Qué oración está mal ubicada en el orden lógico? Escríbela.", "First we ate lunch", "Se come después de cocinar y preparar la ensalada, no antes."),
    ],
    [("Escribes un correo y tu profesora te pregunta qué cambiarías para que sea más claro. ¿Cuál es la mejor revisión? a) Cambiar «a good day» por «a sunny and relaxing day» b) Agregar tres veces «very very very»", "a", "Aporta precisión y detalles.")],
    [
        ("¿Qué es una lista de revisión?", "Una lista de preguntas para mejorar un texto", "Guía los pasos de la revisión."),
        ("Reemplaza «nice» en: «We saw a ___ house.» Opciones: beautiful, good.", "beautiful", "Beautiful dice qué tan bonita era."),
        ("¿Para qué lees en voz alta tu texto? a) Para detectar partes confusas b) Para memorizarlo", "a", "Si suena confuso, hay que reescribir."),
    ],
    task("Revisa este borrador: «I went to a place. It was good. I saw things. They were nice. The end.» (place = lugar; things = cosas) En tu hoja reescríbelo en cuatro oraciones: invéntale un lugar, cambia al menos tres palabras vagas por palabras precisas, evita repetir y agrega un cierre con una idea final. Luego marca con un círculo los cambios.", "Last week I visited the zoo. I saw tall giraffes and playful monkeys. The monkeys were very funny. I learned how to look after animals. (ejemplo)", ["reemplaza al menos tres palabras vagas", "evita la repetición", "tiene un cierre con idea final"], ["borrador reescrito con los cambios marcados"], ["corregir solo la ortografía", "mantener «good» y «nice» sin cambio"], "Pregunta cuál cambio mejoró más la claridad."),
    "Copia la lista de revisión de la explicación y úsala sobre un texto tuyo corto.",
    "Escribe tres oraciones con palabras vagas y reescríbelas con palabras precisas.",
)
