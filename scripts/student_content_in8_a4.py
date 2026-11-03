"""Cuaderno del estudiante, 8.º básico Inglés (oficial), IN08 OA 05 (presentación oral multimodal) y OA 06 (planificar, reparar y revisar el inglés hablado).

Las clases se trabajan por escrito, con las frases y los datos ya incluidos; la parte hablada se practica con una persona de tu casa.
"""
from __future__ import annotations

from student_content_in8_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA5 = "IN08 OA 05"
OA6 = "IN08 OA 06"
MAT = "Lápiz, una hoja y una persona de tu casa que te escuche; las frases y los datos vienen escritos en cada ejercicio."

# ================================================================== OA 5, clase 1
lesson(
    OA5, 1, MAT,
    "Aprenderé a pensar en la audiencia, el contexto y el propósito antes de presentar. Sirve para elegir el saludo, las palabras y las imágenes adecuadas.",
    ["Sé presentar una idea con frases cortas.", "Conozco saludos como Hello y Good morning."],
    [
        "Antes de presentar, hazte tres preguntas. ¿Quién me escucha? Esa es la audiencia (audience): niños pequeños, compañeros, la directora o familias. ¿Dónde y cuándo hablo? Ese es el contexto (context): una sala de clases, una feria o una reunión formal. ¿Para qué hablo? Ese es el propósito (purpose): informar, explicar un proceso, convencer o contar una experiencia.",
        "La audiencia cambia tus decisiones. Con niños pequeños usas palabras simples, frases cortas e imágenes grandes: Hello, friends! Look at this blue box. Con la directora usas un registro más formal: Good morning, Ms. Rojas. I would like to propose a recycling plan. El propósito también cambia el mensaje: para convencer pides algo, como Please vote for the green option; para explicar muestras pasos, como Today I will explain how paper becomes new paper.",
        "Una regla práctica de tiempo es una idea principal por cada minuto: en una presentación de tres minutos caben tres ideas principales. Es mejor decir pocas ideas bien explicadas que muchas ideas apuradas. Decir el propósito al comienzo ayuda a la audiencia a saber qué esperar.",
    ],
    [("audience", "audiencia: las personas que escuchan"), ("context", "contexto: lugar y situación de la presentación"), ("purpose", "propósito: para qué se presenta"), ("formal", "formal: cuidado, como con una directora"), ("informal", "informal: cercano, como con amigos"), ("persuade", "persuadir: convencer a otros")],
    [
        ("Elegir según la audiencia", "Vas a presentar a niños de 2.º básico cómo reciclar papel. ¿Cuál inicio eliges: «Hello, friends! Look at this blue box. It is for paper.» o «Good morning, esteemed members of the board.»?", ["La audiencia son niños pequeños.", "Necesito palabras simples y un objeto que puedan ver.", "El primer inicio usa saludo cercano, frases cortas y una caja azul."], "Hello, friends! Look at this blue box. It is for paper."),
        ("Reconocer el propósito", "«Please vote for the green option.» ¿Cuál es el propósito de esta frase?", ["La frase pide una acción a la audiencia.", "Quien habla quiere que la audiencia elija algo.", "El propósito es convencer."], "Convencer a la audiencia"),
    ],
    [
        ("Usar el mismo texto para todas las audiencias.", "Lo que funciona con compañeros puede ser difícil o muy informal para otras personas.", "Cambia las palabras y las imágenes según quién escucha."),
        ("Poner muchas ideas en una presentación corta.", "No se alcanzan a explicar y la audiencia se pierde.", "Usa una idea principal por minuto."),
    ],
    [
        ("Vas a presentar a la directora. ¿Qué inicio es más adecuado? a) Good morning, Ms. Rojas. I would like to propose a recycling plan. b) Hi guys, listen to me.", "a) Good morning, Ms. Rojas. I would like to propose a recycling plan.", "Es formal y dice el propósito."),
        ("¿Cuál es el propósito de «Today I will explain how paper becomes new paper»? a) explicar un proceso b) contar una anécdota", "a) explicar un proceso", "Dice que explicará cómo se hace papel nuevo."),
        ("Tu audiencia son niños pequeños. ¿Qué conviene usar? a) frases cortas, palabras simples e imágenes grandes b) frases largas y palabras difíciles", "a) frases cortas, palabras simples e imágenes grandes", "Se adapta el lenguaje a la audiencia."),
    ],
    [
        ("Quieres convencer a tu curso de elegir el museo en vez del zoológico. ¿Qué propósito tiene tu presentación? a) persuadir b) describir una receta", "a) persuadir", "Quieres que otros cambien su decisión."),
        ("Tu audiencia son abuelos que visitan el colegio y quieren saber cómo es el día escolar. ¿Qué tema eliges? a) My school day b) The structure of the atom", "a) My school day", "Responde a lo que la audiencia quiere saber."),
        ("Terminas una presentación para tu profesora. ¿Qué despedida es más adecuada? a) Thank you for listening. Are there any questions? b) Bye, I'm done.", "a) Thank you for listening. Are there any questions?", "Agradece y abre un espacio de preguntas."),
    ],
    [
        ("Lee dos aperturas. Apertura 1: «Hi, kids! Today we play with colours.» Apertura 2: «Good afternoon, ladies and gentlemen. I will present the annual budget.» ¿Cuál es adecuada para una presentación a niños de 6 años? a) la apertura 1 b) la apertura 2", "a) la apertura 1", "Usa un saludo cercano y palabras simples."),
        ("Tu propósito es explicar cómo se hace un barquito de papel. ¿Qué recurso es más útil? a) una hoja real que doblas paso a paso b) un gráfico de barras", "a) una hoja real que doblas paso a paso", "El objeto demuestra el proceso."),
        ("Debes informar a los apoderados la fecha de la feria. ¿Qué contexto exige un registro más formal? a) una reunión de apoderados b) un recreo con amigos", "a) una reunión de apoderados", "Es una situación formal con adultos."),
    ],
    [
        ("Ana y Luis presentan reciclaje a niños de ocho años. Ana usa palabras simples y un dibujo. Luis usa palabras técnicas y ninguna imagen. ¿Quién adaptó mejor su presentación? a) Ana b) Luis", "a) Ana", "Ajustó el lenguaje y los apoyos a la audiencia."),
        ("¿Por qué conviene decir el propósito al comienzo? a) porque la audiencia sabe qué esperar b) porque la presentación dura más", "a) porque la audiencia sabe qué esperar", "Orienta la atención."),
    ],
    [
        ("Marta preparó 12 láminas con mucho texto para una presentación de tres minutos. ¿Qué cambio conviene? a) reducirlas a 3 láminas, una por idea principal b) agregar más texto", "a) reducirlas a 3 láminas, una por idea principal", "Con una idea por minuto, tres minutos admiten tres ideas."),
        ("¿Qué frase da un consejo y sirve para una presentación sobre seguridad en la calle? a) You should look both ways before crossing. b) You looked both ways.", "a) You should look both ways before crossing.", "Should + verbo da un consejo."),
    ],
    [("Presentas «Our River Clean-up» (la limpieza del río) en una feria de la comunidad, con familias. ¿Qué apoyo es más útil? a) fotos grandes y frases simples b) tablas pequeñas con muchos números", "a) fotos grandes y frases simples", "Las familias de distintas edades entienden mejor imágenes grandes y frases simples.")],
    [
        ("¿Cuáles son las tres preguntas antes de presentar?", "¿Quién escucha?, ¿en qué contexto? y ¿para qué?", "Audiencia, contexto y propósito."),
        ("En Inglés de 8.º (OA 5, clase 1): ¿Qué significa persuadir?", "Convencer a otros", "Es un propósito de presentación."),
        ("En una presentación de tres minutos, ¿cuántas ideas principales caben según la regla de la clase?", "3", "Una idea principal por minuto."),
    ],
    task("Imagina esta situación de ejemplo: presentarás «Healthy Breakfast» (desayuno saludable) a tu curso durante tres minutos para convencerlos de comer fruta. Escribe: 1) audiencia, 2) propósito, 3) un saludo de apertura en inglés y 4) tus tres ideas principales en inglés o en español.", "Audiencia: compañeros de curso. Propósito: convencer de comer fruta. Saludo: Hello, everyone. Today I want to talk about a healthy breakfast. Ideas: la fruta da energía; es fácil de llevar; cuesta poco.", ["nombra la audiencia y el propósito", "escribe un saludo adecuado", "anota tres ideas principales"], ["hoja con cuatro partes", "nota de una persona de tu casa"], ["usar un saludo demasiado informal", "poner más de tres ideas"], "Reconoce lo que acertó y ajusta solo la parte que no coincidía con la audiencia."),
    "Lee en voz alta los dos saludos de la clase, uno para niños pequeños y otro para la directora, y nota cómo cambia el tono.",
    "Escribe dos saludos de apertura para el mismo tema, uno para niños de siete años y otro para tus profesores.",
)

# ------------------------------------------------------------------ OA 5, clase 2
lesson(
    OA5, 2, MAT,
    "Aprenderé a organizar las ideas de una presentación con un inicio, un desarrollo y un cierre, y a unirlas con conectores. Sirve para que la audiencia siga lo que digo.",
    ["Sé que una presentación tiene un propósito.", "Conozco first, next, then y finally."],
    [
        "Una presentación coherente (coherent) tiene tres partes. El inicio (opening) saluda, dice el tema y presenta el propósito: Hello, everyone. Today I will talk about our school garden. El desarrollo (body) explica las ideas principales, una por una, con un ejemplo o dato. El cierre (closing) resume y agradece: In short, the garden teaches us to work as a team. Thank you for listening.",
        "Los conectores ayudan a pasar de una idea a otra: first (primero), second (segundo), next (a continuación), then (después), also (además), finally (por último) e in short (en resumen). Cada idea del desarrollo debe relacionarse con el tema. Una frase que no tiene relación, como My cousin has a red bike, rompe la coherencia y debe quedar fuera.",
        "Para organizar tus ideas, usa una tarjeta o un esquema con cinco casilleros: opening, idea 1, idea 2, idea 3 y closing. Escribe en cada casillero solo palabras clave. Así recuerdas el orden sin leer un texto completo. Antes de presentar, comprueba que cada idea tiene su conector.",
    ],
    [("opening", "inicio: saludo, tema y propósito"), ("body", "desarrollo: las ideas principales"), ("closing", "cierre: resumen y agradecimiento"), ("coherent", "coherente: las ideas se relacionan y siguen un orden"), ("in short", "en resumen"), ("organizer", "esquema para ordenar las ideas")],
    [
        ("Ordenar las partes", "Ordena escribiendo los números: (1) Finally, we sell the vegetables at the fair. (2) Hello, everyone. Today I will talk about our school garden. (3) First, we clean the soil. (4) Thank you for listening.", ["La apertura es la frase 2.", "Luego viene la primera idea con First, que es la 3.", "Después la última idea con Finally, que es la 1, y al final el agradecimiento, que es la 4."], "2, 3, 1, 4"),
        ("Quitar lo que no pertenece", "En una presentación sobre el huerto escolar aparece la frase «My cousin has a red bike». ¿La dejarías o la sacarías?", ["El tema es el huerto escolar.", "La bicicleta del primo no se relaciona con el tema.", "Rompe la coherencia, así que se saca."], "La sacaría, porque no se relaciona con el tema"),
    ],
    [
        ("Empezar a hablar sin decir el tema.", "La audiencia no sabe de qué se trata.", "Di el tema y el propósito en la primera frase."),
        ("Terminar de golpe, sin resumen ni agradecimiento.", "La audiencia no sabe que terminaste ni cuál era la idea final.", "Cierra con In short y Thank you for listening."),
    ],
    [
        ("¿Cuál es la frase de apertura? a) Hello, everyone. Today I will talk about our school garden. b) Finally, we sell the vegetables at the school fair.", "a) Hello, everyone. Today I will talk about our school garden.", "Saluda y dice el tema."),
        ("¿Cuál es la frase de cierre? a) Thank you for listening. Do you have any questions? b) First, we clean the soil.", "a) Thank you for listening. Do you have any questions?", "Agradece y abre preguntas."),
        ("¿Qué palabra marca la primera idea? a) First b) Finally", "a) First", "First significa primero."),
    ],
    [
        ("¿Qué frase no pertenece a una presentación sobre el huerto escolar? a) My cousin has a red bike. b) Second, we water the plants every morning.", "a) My cousin has a red bike.", "No se relaciona con el huerto."),
        ("¿Para qué sirve «In short»? a) para resumir al final b) para empezar la presentación", "a) para resumir al final", "In short significa en resumen."),
        ("Ordena escribiendo los números: (1) Finally, we sell the vegetables. (2) Hello, everyone. Today I will talk about our school garden. (3) First, we clean the soil.", "2, 3, 1", "Primero va la apertura, luego First y al final Finally."),
    ],
    [
        ("Elige el conector: «We water the plants every morning, ___ they grow strong.» a) so b) until", "a) so", "El riego tiene como resultado que crecen fuertes."),
        ("Completa los conectores en orden: «___, we clean the soil. ___, we water the plants. ___, we sell vegetables.» a) First – Next – Finally b) Finally – First – Next", "a) First – Next – Finally", "Siguen el orden de las acciones."),
        ("El modelo de la clase habla de limpiar la tierra, regar las plantas y vender las verduras. ¿Cuántas ideas principales tiene el desarrollo?", "3", "Son tres ideas: limpiar, regar y vender."),
    ],
    [
        ("Pedro empezó con «Finally» y terminó con «First». ¿Qué problema tiene su presentación? a) los conectores no siguen el orden de las ideas b) usó demasiados saludos", "a) los conectores no siguen el orden de las ideas", "Finally debe ir al final y First al comienzo."),
        ("Una presentación termina en la última idea, sin cierre. ¿Qué le falta? a) un resumen y un agradecimiento b) un título", "a) un resumen y un agradecimiento", "El cierre resume y agradece."),
    ],
    [
        ("Marta presenta «My favourite sport: swimming». ¿Qué frase es el cierre? a) In short, swimming is fun and healthy. Thank you! b) I swim on Mondays.", "a) In short, swimming is fun and healthy. Thank you!", "Resume la idea y agradece."),
        ("Marta dice «Swimming is good». ¿Qué agregarías para apoyar la idea? a) un ejemplo: it makes my arms strong b) otra idea sin relación con la natación", "a) un ejemplo: it makes my arms strong", "Cada idea necesita un ejemplo o dato que la apoye."),
    ],
    [("Tienes dos minutos para presentar «My day at school». ¿Qué estructura es más clara? a) saludo, tres actividades con first, then y finally, y cierre b) tres saludos seguidos y un chiste", "a) saludo, tres actividades con first, then y finally, y cierre", "Tiene inicio, desarrollo con conectores y cierre.")],
    [
        ("En Inglés de 8.º (OA 5, clase 2): ¿qué partes ordenan una presentación coherente?", "Inicio, desarrollo y cierre", "Opening, body y closing."),
        ("En Inglés de 8.º (OA 5, clase 2): ¿Qué significa «in short»?", "En resumen", "Se usa para resumir al final."),
        ("¿Para qué sirve un esquema de cinco casilleros?", "Para ordenar la apertura, tres ideas y el cierre", "Ayuda a recordar el orden."),
    ],
    task("Imagina que presentarás «A Day at the Beach» (de ejemplo). Completa un esquema de cinco casilleros: opening, idea 1, idea 2, idea 3 y closing. Escribe en cada casillero una frase corta en inglés y usa first, next y finally en las tres ideas.", "Opening: Hello, everyone. Today I will talk about a day at the beach. Idea 1: First, we put on sun cream. Idea 2: Next, we play in the sand. Idea 3: Finally, we swim in the sea. Closing: In short, it was a great day. Thank you!", ["completa los cinco casilleros", "usa first, next y finally", "todas las ideas se relacionan con el tema"], ["esquema de cinco casilleros", "nota de una persona de tu casa"], ["incluir una idea sin relación con la playa", "omitir el cierre"], "Reconoce los casilleros bien hechos y ajusta el orden de los conectores."),
    "Lee en voz alta el modelo del huerto escolar y marca con un lápiz de color los conectores.",
    "Elige un tema de tu agrado y escribe un esquema de cinco casilleros con apertura, tres ideas con conectores y cierre.",
)

# ------------------------------------------------------------------ OA 5, clase 3
lesson(
    OA5, 3, MAT,
    "Aprenderé a elegir recursos multimodales (imágenes, gráficos, objetos, gestos y voz) que refuerzan el mensaje. Sirve para que la audiencia entienda mejor y recuerde lo que presento.",
    ["Sé organizar una presentación en tres partes.", "Sé leer un gráfico de barras sencillo."],
    [
        "Un recurso multimodal (multimodal resource) es cualquier forma de comunicar además de las palabras: una imagen, un gráfico, un objeto real, un gesto o el tono de la voz. Usar varios recursos juntos ayuda a que el mensaje se entienda mejor. Un buen recurso refuerza el mensaje; uno que solo decora, como un dragón en una charla sobre el agua, distrae.",
        "Cada recurso sirve para algo. Una lámina debe tener pocas palabras y una imagen clara: una idea por lámina. Un gráfico de barras muestra cantidades y permite comparar de un vistazo, como cuántos compañeros prefieren cada deporte. Un objeto real, como una hoja doblada, ayuda a demostrar un paso. Los gestos, como apuntar a la imagen al decir look at this picture, dirigen la atención.",
        "La voz también es un recurso. Habla con un volumen que se oiga hasta el último puesto, di más fuerte las palabras clave y haz una pausa corta después de una idea importante. Mira a tu audiencia, no solo a tu lámina. Si lees todo el texto de la lámina de espaldas al público, no aprovechas ningún recurso.",
    ],
    [("multimodal", "que usa varios modos: palabras, imágenes, gestos y voz"), ("slide", "lámina o diapositiva"), ("bar chart", "gráfico de barras"), ("gesture", "gesto"), ("eye contact", "contacto visual: mirar a la audiencia"), ("pause", "pausa: un breve silencio")],
    [
        ("Elegir un gráfico", "En una encuesta de ejemplo, 12 compañeros prefieren fútbol, 8 vóleibol y 5 natación. ¿Qué recurso muestra mejor quién prefiere cada deporte?", ["Hay tres categorías con cantidades.", "Un gráfico de barras compara cantidades de un vistazo.", "La barra de fútbol será la más alta."], "Un gráfico de barras"),
        ("Dar un gesto", "Dices «Look at this picture». ¿Qué gesto refuerza mejor tu frase?", ["La frase pide mirar una imagen.", "El gesto debe dirigir la atención a la imagen.", "Apuntar a la imagen lo logra."], "Apuntar a la imagen"),
    ],
    [
        ("Poner párrafos largos en la lámina.", "La audiencia lee en vez de escuchar y se pierde.", "Usa pocas palabras y una imagen."),
        ("Usar imágenes solo porque son bonitas.", "Una imagen que no se relaciona con el mensaje distrae.", "Elige imágenes que refuercen la idea."),
    ],
    [
        ("¿Qué lámina es mejor para una idea? a) una imagen y tres palabras b) un párrafo largo", "a) una imagen y tres palabras", "Pocas palabras y una imagen son más fáciles de seguir."),
        ("¿Qué recurso muestra mejor las cantidades de la encuesta? a) un gráfico de barras b) una foto de un estadio", "a) un gráfico de barras", "Compara cantidades de un vistazo."),
        ("Dices «look at this picture». ¿Qué gesto refuerza? a) apuntar a la imagen b) mirar el techo", "a) apuntar a la imagen", "El gesto dirige la atención a lo que dices."),
    ],
    [
        arith("En otra encuesta de ejemplo, 14 prefieren fútbol, 9 vóleibol y 6 natación. ¿Cuántos compañeros respondieron en total?", "14+9+6", "Se suman las tres cantidades.", " compañeros"),
        ("En otra encuesta de ejemplo (fútbol 14, vóleibol 9, natación 6), ¿qué barra será la más alta? a) la de fútbol b) la de natación", "a) la de fútbol", "Tiene la mayor cantidad."),
        arith("En esa otra encuesta de ejemplo, ¿cuántos compañeros más prefieren fútbol que natación?", "14-6", "Se resta la cantidad menor a la mayor.", " compañeros"),
    ],
    [
        ("Quieres mostrar cómo doblar una hoja para hacer un barquito. ¿Qué recurso es mejor? a) mostrarlo con una hoja real mientras hablas b) leer un texto largo", "a) mostrarlo con una hoja real mientras hablas", "Un objeto real demuestra el paso."),
        ("En tu discurso hay una palabra clave importante. ¿Qué haces con la voz? a) la dices más fuerte y haces una pausa b) la dices en voz baja y rápido", "a) la dices más fuerte y haces una pausa", "La voz destaca lo importante."),
        ("Lámina A: 6 palabras y una imagen. Lámina B: 60 palabras. ¿Cuál es más adecuada? a) la A b) la B", "a) la A", "Menos texto permite mirar a la audiencia."),
    ],
    [
        ("Ana lee en voz alta todo el texto de su lámina de espaldas a la audiencia. ¿Qué problema tiene? a) no hay contacto visual ni usa recursos que refuercen el mensaje b) habla demasiado bajo", "a) no hay contacto visual ni usa recursos que refuercen el mensaje", "Mirar a la audiencia es parte de una presentación multimodal."),
        ("Pedro pone un dragón en una charla sobre el agua. ¿Es un buen apoyo? a) no, porque no refuerza el mensaje b) sí, porque es bonito", "a) no, porque no refuerza el mensaje", "Una imagen debe reforzar la idea."),
    ],
    [
        ("Quieres decir que otro curso prefiere fútbol (14), vóleibol (9) y natación (6). ¿Qué combinación es mejor? a) un gráfico de barras, señalar la barra más alta y decir «Football is the most popular» b) una tabla de veinticinco filas leída completa", "a) un gráfico de barras, señalar la barra más alta y decir «Football is the most popular»", "Combina gráfico, gesto y palabras."),
        ("Luis usa una foto, señala con la mano y muestra una hoja real. ¿Cuántos recursos distintos usa?", "3", "Son una imagen, un gesto y un objeto."),
    ],
    [("Presentas «Our Town's Market» (el mercado de tu pueblo) a visitantes que no lo conocen. ¿Qué recurso es más útil? a) una foto grande del mercado y apuntar a los puestos b) una lista de precios muy larga", "a) una foto grande del mercado y apuntar a los puestos", "Muestra el lugar y dirige la atención.")],
    [
        ("En Inglés de 8.º (OA 5, clase 3): ¿qué significa que una presentación use recursos multimodales?", "Que comunica con otras formas además de las palabras", "Por ejemplo, imágenes, gestos o voz."),
        ("En Inglés de 8.º (OA 5, clase 3): ¿Cuántas palabras conviene poner en una lámina?", "Pocas", "Una idea por lámina."),
        ("¿Qué gráfico compara cantidades?", "El gráfico de barras", "Muestra la cantidad de cada categoría."),
    ],
    task("Imagina que presentarás «Recycling Paper» a tu curso. Elige y escribe tres recursos multimodales (uno visual, uno gestual y uno de voz) y di para qué sirve cada uno. Usa esta información de ejemplo: el curso usa 30 hojas por semana y reutiliza 10.", "Visual: una lámina con dos barras (30 y 10). Gestual: apuntar a la barra más alta. Voz: decir más fuerte «thirty» y hacer una pausa.", ["nombra un recurso visual, uno gestual y uno de voz", "explica para qué sirve cada uno", "usa los datos de ejemplo"], ["hoja con tres recursos", "nota de una persona de tu casa"], ["poner una imagen que no se relaciona", "no explicar para qué sirve"], "Reconoce el recurso mejor elegido y ajusta el que no refuerza el mensaje."),
    "Practica una frase con una pausa corta y la palabra clave dicha más fuerte, frente a una persona de tu casa.",
    "Dibuja una lámina para una idea de tu presentación con una imagen y no más de cinco palabras.",
)

# ------------------------------------------------------------------ OA 5, clase 4
lesson(
    OA5, 4, MAT,
    "Aprenderé a usar las funciones del lenguaje y el vocabulario del año dentro de una presentación: comparar, expresar gustos, cantidades y planes. Sirve para que mi presentación sea clara y correcta.",
    ["Sé organizar una presentación con inicio, desarrollo y cierre.", "Conozco adjetivos como big, small, popular y relaxing."],
    [
        "En una presentación usas funciones del lenguaje (language functions), que son las cosas que haces con las palabras. Para comparar dos cosas: Football is more popular than tennis; My bag is heavier than your bag. Para comparar tres o más: She is the tallest student. Para expresar gustos y deseos: I love swimming; I enjoy drawing; I don't mind waiting; I'd like to talk about my town (me gustaría hablar de mi pueblo). Para hablar de cantidades: There are a lot of people; Several students came.",
        "Para planes y predicciones usas be going to o will: We are going to build a garden next year; The new library will open next month. Para justificar una opinión: I think swimming is better than running because it is gentle for the knees. Para ordenar ideas: first, next, then, finally. Tu presentación debe incluir al menos dos o tres de estas funciones, bien usadas.",
        "Para revisar tus frases, comprueba la forma. En comparaciones, los adjetivos cortos llevan -er (heavier) y los largos usan more (more popular). Después de enjoy y love usamos el verbo con -ing (I enjoy swimming, no I enjoy to swim). Para planes con going to necesitas el verbo be (I am going to visit my grandma).",
    ],
    [("language function", "función del lenguaje: lo que haces al hablar"), ("compare", "comparar"), ("I enjoy + -ing", "disfruto haciendo algo"), ("a lot of / several", "mucho/varios"), ("be going to", "plan futuro: voy a..."), ("will", "futuro: haré / será")],
    [
        ("Comparar dos cosas", "Completa: «My bag is ___ than your bag» (heavy). ¿Qué forma correcta usas: heavier o more heavy?", ["Heavy es un adjetivo corto.", "Los adjetivos cortos llevan -er; heavy cambia la y por i.", "La forma es heavier."], "Heavier"),
        ("Hablar de un plan", "Quieres decir que visitarás a tu abuela la próxima semana. ¿Cuál frase es correcta: «I am going to visit my grandma next week» o «I am go to visit my grandma next week»?", ["Para planes usamos be going to + verbo.", "Falta el -ing en go: going.", "La primera frase es correcta."], "I am going to visit my grandma next week"),
    ],
    [
        ("Decir «I enjoy to swim».", "Después de enjoy el verbo lleva -ing.", "Di I enjoy swimming."),
        ("Decir «more big» para comparar.", "Big es un adjetivo corto y lleva -er.", "Di bigger."),
    ],
    [
        ("Para comparar dos deportes, ¿qué frase es correcta? a) Football is more popular than tennis. b) Football is more popular that tennis.", "a) Football is more popular than tennis.", "En comparaciones se usa than."),
        ("¿Qué frase expresa un gusto correctamente? a) I enjoy swimming. b) I enjoy swim.", "a) I enjoy swimming.", "Enjoy va con verbo + -ing."),
        ("¿Qué frase expresa un plan? a) We are going to visit the museum next week. b) We are go to visit the museum next week.", "a) We are going to visit the museum next week.", "Be going to + verbo expresa un plan."),
    ],
    [
        ("¿Para qué sirve «I'd like to talk about my town»? a) para decir con cortesía lo que quieres hacer b) para comparar dos cosas", "a) para decir con cortesía lo que quieres hacer", "I'd like to es una forma cortés de decir lo que quieres."),
        ("¿Qué significa «several students»? a) varios estudiantes b) ningún estudiante", "a) varios estudiantes", "Several indica una cantidad de más de dos."),
        ("¿Qué frase habla de una cantidad? a) There are a lot of people in the plaza. b) The people is plaza.", "a) There are a lot of people in the plaza.", "A lot of indica mucha cantidad y la oración está bien formada."),
    ],
    [
        ("Completa: «She is the ___ student in the class» (tall). a) tallest b) most tall", "a) tallest", "Tall es corto y su superlativo lleva the + -est."),
        ("Completa: «I ___ buy a bike next month.» a) am going to b) am go to", "a) am going to", "Para un plan se usa be going to."),
        ("Completa: «The new library ___ open next year.» a) will b) is will", "a) will", "Will + verbo anuncia un hecho futuro."),
    ],
    [
        ("¿Qué función cumple «The new library will open next year»? a) anunciar algo futuro b) expresar un gusto", "a) anunciar algo futuro", "Will + verbo habla del futuro."),
        ("Daniel dice «I enjoy to swim». ¿Qué corriges? a) I enjoy swimming b) I enjoying swim", "a) I enjoy swimming", "Después de enjoy va el verbo con -ing."),
    ],
    [
        ("¿Cuál es la mejor oración para justificar una opinión? a) I think swimming is better than running because it is gentle for the knees. b) Swimming better running.", "a) I think swimming is better than running because it is gentle for the knees.", "Tiene opinión, comparación y razón."),
        ("En «First, I will compare two parks», ¿qué palabra marca el orden de las ideas? a) First b) compare", "a) First", "First marca el primer paso."),
    ],
    [("Presentas tus planes del verano. ¿Qué frase es la más adecuada? a) Next summer, I am going to learn to swim. b) Next summer, I learn swimming now.", "a) Next summer, I am going to learn to swim.", "Next summer pide una forma de futuro con be going to.")],
    [
        ("¿Qué lleva el verbo después de «enjoy»?", "-ing", "Se dice I enjoy swimming."),
        ("En Inglés de 8.º (OA 5, clase 4): ¿Cómo comparas dos cosas con un adjetivo corto?", "Adjetivo + -er + than", "Por ejemplo, heavier than."),
        ("¿Qué usas para un plan?", "Be going to + verbo", "Por ejemplo, I am going to visit."),
    ],
    task("Imagina que presentas «My Weekend» (de ejemplo) y debes incluir cuatro frases: 1) un gusto con enjoy o love, 2) una comparación, 3) un plan con going to y 4) una cantidad con a lot of o several. Escribe las cuatro frases en inglés.", "I enjoy cycling. The park is bigger than the square. Next weekend, I am going to visit my cousin. There are a lot of trees in the park.", ["escribe las cuatro frases", "usa -ing después de enjoy", "usa than en la comparación y be going to en el plan"], ["hoja con cuatro frases", "nota de una persona de tu casa"], ["I enjoy to cycle", "more big than"], "Reconoce las frases correctas y corrige solo la forma que no sigue la regla."),
    "Di en voz alta las cuatro frases modelo de la clase y marca con un color el -ing, el than y el going to.",
    "Escribe una presentación de cinco frases sobre tu ciudad con una comparación, un gusto, un plan y una cantidad.",
)

# ------------------------------------------------------------------ OA 5, clase 5
S5 = "This week, three students helped the farmer. They watched the rain and wanted to thank him."

lesson(
    OA5, 5, MAT,
    "Aprenderé a revisar los sonidos del guion de una presentación (/ð/, /θ/, /w/, /r/ y la terminación -ed) y a practicar las palabras difíciles. Sirve para que la audiencia me entienda con claridad.",
    ["Sé que th tiene dos sonidos: /ð/ y /θ/.", "Sé que -ed suena /d/, /t/ o /ɪd/."],
    [
        "Antes de presentar, revisa los sonidos de tu guion. Busca las palabras con th y decide si suenan /ð/ (the, this, they, mother) o /θ/ (three, thank, birthday). Busca las palabras que empiezan con /w/ (week, wanted, water) y con /r/ (rain, ready, red). Recuerda que en write y wrong la w no suena y empiezan con /r/.",
        "Revisa también los verbos en pasado. La terminación -ed suena /t/ después de sonidos como /p/, /k/ y ch (helped, walked, watched), /d/ después de vocales y sonidos sonoros (lived, played) e /ɪd/ después de /t/ o /d/ (wanted, decided). Marca cada verbo con una de estas tres señales para saber cómo decirlo.",
        "Después, practica en voz alta. Elige las cuatro o cinco palabras más difíciles de tu guion y repítelas despacio. Luego di la frase completa. Si puedes, graba tu voz o pide a una persona de tu casa que te escuche. No se trata de tener un acento perfecto, sino de pronunciar los sonidos de modo que se entienda cada palabra.",
    ],
    [("sound", "sonido"), ("script", "guion de la presentación"), ("practise", "practicar"), ("mark", "marcar"), ("clear", "claro"), ("record", "grabar")],
    [
        ("Marcar el sonido de th", f"Guion: «{S5}» ¿Cuántas palabras tienen el sonido /ð/? (palabras con th: this, three, the, they, the, thank)", ["This, the, they y the tienen /ð/.", "Three y thank tienen /θ/.", "Son 4 con /ð/."], "4"),
        ("Marcar la terminación -ed", f"Guion: «{S5}» Clasifica helped, watched y wanted según el sonido de -ed.", ["Help y watch terminan en sonido sordo: /t/.", "Want termina en /t/: se agrega /ɪd/.", "Helped y watched /t/; wanted /ɪd/."], "Helped y watched: /t/; wanted: /ɪd/"),
    ],
    [
        ("Decir la th de this como una d.", "Se pierde el sonido /ð/ y suena dis.", "Pon la lengua entre los dientes y haz vibrar la garganta."),
        ("Decir wanted en una sílaba.", "Después de /t/ la terminación suena /ɪd/ y agrega una sílaba.", "Di wan-ted."),
    ],
    [
        ("¿Cómo suena la th de «three»? a) /θ/ b) /ð/", "a) /θ/", "Three tiene th sorda."),
        ("¿Cuál es la terminación del pasado del verbo «wanted» en tu guion? a) /ɪd/ b) /t/", "a) /ɪd/", "Want termina en /t/."),
        ("¿Cómo suena la terminación -ed de «helped»? a) /t/ b) /d/", "a) /t/", "Help termina en /p/, un sonido sordo."),
    ],
    [
        (f"Guion: «{S5}» ¿Cuántas palabras tienen el sonido /θ/? (palabras con th: this, three, the, they, the, thank)", "2", "Three y thank tienen /θ/."),
        (f"Guion: «{S5}» ¿Cuántas palabras empiezan con el sonido /w/? (palabras: week, watched, wanted, students, rain)", "3", "Week, watched y wanted empiezan con /w/."),
        (f"Guion: «{S5}» ¿Qué palabra empieza con /r/? a) rain b) week", "a) rain", "Rain empieza con /r/."),
    ],
    [
        ("Clasifica estas palabras de tu guion: this, thank, mother, month. Escribe cuáles tienen /ð/ y cuáles /θ/.", "/ð/: this, mother; /θ/: thank, month", "This y mother tienen /ð/; thank y month tienen /θ/."),
        ("¿Cómo suena la terminación -ed de «cleaned»? a) /d/ b) /t/", "a) /d/", "Clean termina en /n/, un sonido sonoro."),
        ("En tu guion aparece «write». ¿Con qué sonido empieza? a) /r/ b) /w/", "a) /r/", "En write la w es muda."),
    ],
    [
        ("Ema dice «dis week» en lugar de «this week». ¿Qué sonido debe corregir? a) /ð/ b) /w/", "a) /ð/", "This empieza con /ð/, no con d."),
        ("Para practicar mejor, ¿qué conviene hacer primero? a) elegir las palabras más difíciles del guion y repetirlas despacio b) leer todo el guion una sola vez, rápido", "a) elegir las palabras más difíciles del guion y repetirlas despacio", "Practicar lo difícil mejora más rápido."),
    ],
    [
        ("Marca los sonidos del guion «Last week, Lucía watched the rain and wanted a red umbrella». ¿Cuántos verbos tienen la terminación /ɪd/?", "1", "Solo wanted suena /ɪd/; watched suena /t/."),
        ("En el guion «Their brother thanked three friends», ¿cuántas palabras tienen /ð/? (palabras con th: their, brother, thanked, three)", "2", "Their y brother tienen /ð/; thanked y three tienen /θ/."),
    ],
    [("Antes de una presentación, quieres comprobar tu pronunciación. ¿Qué es más útil? a) grabar tu voz y compararla con el guion b) no practicar para no ponerte nervioso", "a) grabar tu voz y compararla con el guion", "Escuchar tu voz te muestra qué sonido cambiar.")],
    [
        ("¿Cómo suena th en «the»?", "/ð/", "Es una palabra pequeña con th sonora."),
        ("En Inglés de 8.º (OA 5, clase 5): ¿Cómo suena -ed después de /t/?", "/ɪd/", "Agrega una sílaba."),
        ("¿Para qué marcar los sonidos del guion?", "Para saber qué palabras practicar", "Ayuda a pronunciar con claridad."),
    ],
    task("Lee este guion de ejemplo y marca: «Last week, we visited the farm. Three children helped the farmer and watched the animals. They wanted to thank everyone.» Escribe en tu hoja una lista con las palabras con /ð/, las palabras con /θ/ y los cuatro verbos en pasado con su sonido (/d/, /t/ o /ɪd/).", "/ð/: the, they; /θ/: three, thank; verbos: visited /ɪd/, helped /t/, watched /t/, wanted /ɪd/.", ["marca las palabras con th", "clasifica los verbos en pasado", "practica en voz alta las palabras difíciles"], ["lista de sonidos", "nota de una persona de tu casa"], ["poner visited como /d/", "confundir three con the"], "Reconoce lo que marcó bien y repasa las dos terminaciones /t/ e /ɪd/."),
    "Lee en voz alta el guion de la clase tres veces, cada vez un poco más rápido, sin perder los sonidos.",
    "Escribe un guion de tres frases con al menos una palabra de cada sonido (/ð/, /θ/, /w/, /r/) y un verbo con -ed.",
)

# ================================================================== OA 6, clase 1
lesson(
    OA6, 1, MAT,
    "Aprenderé a prepararme antes de hablar: practicar, repetir, prever el vocabulario clave, usar expresiones de uso común y preparar un apoyo organizativo y visual. Sirve para hablar con más seguridad.",
    ["Sé organizar una presentación con inicio, desarrollo y cierre.", "Conozco expresiones como My name is... y I like..."],
    [
        "Antes de hablar (before speaking) hay cinco estrategias. Practicar la presentación varias veces en voz alta. Repetir las frases difíciles. Predecir el vocabulario clave que necesitarás: si hablas de un viaje a la playa, esperas sand, waves, towel y sun cream. Aprender expresiones de uso común (chunks): My favourite place is..., It is near..., I like it because... Y preparar un apoyo organizativo (una tarjeta con palabras clave) y un apoyo visual (una imagen o un objeto).",
        "Una tarjeta de apoyo no es un guion completo. Lleva tres o cuatro palabras clave por idea, no frases enteras. Así hablas mirando a la audiencia y recuerdas el orden. También conviene medir el tiempo: si tienes dos minutos y tu práctica dura tres, debes recortar una idea o acortar los ejemplos.",
        "Practica con un objetivo: primero, di la presentación completa sin detenerte; después, repite solo las partes difíciles; por último, di todo otra vez con la tarjeta. Cada práctica mejora la fluidez, es decir, la facilidad para hablar sin pausas largas.",
    ],
    [("rehearse / practise", "ensayar / practicar"), ("chunk", "expresión de uso común"), ("key vocabulary", "vocabulario clave del tema"), ("cue card", "tarjeta de apoyo con palabras clave"), ("fluency", "fluidez: hablar con facilidad"), ("time", "tiempo")],
    [
        ("Prever vocabulario", "Vas a hablar de «A trip to the beach». ¿Cuáles de estas palabras es más probable que necesites: sand, waves, mountain, towel?", ["El tema es la playa.", "Sand, waves y towel se relacionan con la playa.", "Mountain no."], "Sand, waves y towel"),
        ("Medir el tiempo", "Debes hablar dos minutos y tu práctica dura tres minutos. ¿Cuánto tiempo debes recortar?", ["Tu práctica dura 3 minutos.", "Debes hablar solo 2.", "Se restan: 3 - 2 = 1."], "1 minuto"),
    ],
    [
        ("Escribir el guion completo en la tarjeta y leerlo.", "No miras a la audiencia y hablas sin naturalidad.", "Escribe solo palabras clave."),
        ("Practicar solo una vez antes de presentar.", "Hay frases que se traban.", "Repite varias veces y trabaja las partes difíciles."),
    ],
    [
        ("Vas a hablar de la playa. ¿Qué palabra es más probable que necesites? a) towel b) microscope", "a) towel", "Una toalla se relaciona con la playa."),
        ("¿Qué lleva una tarjeta de apoyo? a) palabras clave b) el guion completo", "a) palabras clave", "Sirve para recordar el orden."),
        ("¿Qué expresión de uso común sirve para empezar? a) My favourite place is... b) Place favourite my is...", "a) My favourite place is...", "Tiene el orden correcto en inglés."),
    ],
    [
        arith("Tu presentación debe durar 3 minutos y en el ensayo dura 5. ¿Cuántos minutos debes recortar?", "5-3", "Se resta el tiempo permitido al tiempo del ensayo.", " minutos"),
        ("¿Qué es un chunk? a) un grupo de palabras que se usa junto b) una palabra muy larga", "a) un grupo de palabras que se usa junto", "Por ejemplo, I like it because..."),
        ("Para preparar un apoyo visual, ¿qué eliges para hablar de tu mascota? a) una foto de tu mascota b) un mapa de otro país", "a) una foto de tu mascota", "Refuerza lo que dices."),
    ],
    [
        ("Vas a hablar de «My Pet» (tu mascota). ¿Qué grupo de palabras es más útil prever? a) feed, walk, tail, cute b) engine, galaxy, volcano, tax", "a) feed, walk, tail, cute", "Son palabras del tema de las mascotas."),
        ("Mateo escribe en su tarjeta una frase completa de 25 palabras para cada idea. ¿Qué conviene cambiar? a) dejar solo tres o cuatro palabras clave por idea b) agregar más frases", "a) dejar solo tres o cuatro palabras clave por idea", "Una tarjeta de apoyo lleva palabras clave."),
        arith("La primera práctica de tu presentación duró 2 minutos y 40 segundos (160 segundos) y debe durar 2 minutos (120 segundos). ¿Cuántos segundos debes recortar?", "160-120", "Se resta el tiempo permitido al tiempo del ensayo.", " segundos"),
    ],
    [
        ("Ordena las acciones de una buena práctica con los números: (1) di todo otra vez con la tarjeta, (2) di la presentación completa sin detenerte, (3) repite solo las partes difíciles.", "2, 3, 1", "Primero completa, luego trabajas lo difícil y al final con la tarjeta."),
        ("Matías practicó solo una vez y se trabó en dos frases. ¿Qué le conviene? a) repetir esas dos frases varias veces b) cambiar de tema", "a) repetir esas dos frases varias veces", "Repetir mejora la fluidez."),
    ],
    [
        ("Tienes que hablar de «My weekend» y predices estas palabras: movie, friends, homework, pizza. Una persona dice que también necesitas «dinosaur». ¿Es necesaria? a) no, no se relaciona con tu tema b) sí, siempre", "a) no, no se relaciona con tu tema", "Prever vocabulario es pensar en tu tema."),
        ("Una tarjeta tiene: «Opening: hello, topic / Idea 1: sand, play / Idea 2: swim, sun / Closing: thank you». ¿Cuántas ideas principales tiene?", "2", "Tiene Idea 1 e Idea 2."),
    ],
    [("Tienes una exposición en tres días. ¿Qué plan es más útil? a) practicar cada día en voz alta con tu tarjeta b) leer el guion en silencio la noche anterior", "a) practicar cada día en voz alta con tu tarjeta", "La práctica en voz alta mejora la fluidez.")],
    [
        ("¿Cuáles son tres estrategias antes de hablar?", "Practicar, prever vocabulario y preparar apoyos", "Ayudan a hablar con seguridad."),
        ("En Inglés de 8.º (OA 6, clase 1): ¿Qué es una tarjeta de apoyo?", "Una tarjeta con palabras clave", "No es el guion completo."),
        ("¿Para qué sirve medir el tiempo del ensayo?", "Para ajustar la presentación al tiempo disponible", "Se recorta si es necesario."),
    ],
    task("Imagina que hablarás dos minutos sobre «My Favourite Place» (de ejemplo). Escribe: 1) cinco palabras que predices que usarás, 2) dos expresiones de uso común (chunks) en inglés y 3) una tarjeta de apoyo con tres casilleros (opening, idea, closing) con solo palabras clave.", "Palabras: place, near, like, because, friends. Chunks: My favourite place is... / I like it because... Tarjeta: opening: hello + place; idea: near house, play; closing: thank you.", ["predice cinco palabras", "escribe dos chunks", "arma la tarjeta con palabras clave"], ["hoja con tres partes", "nota de una persona de tu casa"], ["escribir frases completas en la tarjeta", "usar palabras que no se relacionan"], "Reconoce lo que acertó y reduce la tarjeta a palabras clave."),
    "Practica en voz alta tres veces la apertura de tu presentación hasta que salga sin trabarte.",
    "Prepara una tarjeta de apoyo para presentar tu comida favorita, con solo diez palabras en total.",
)

# ------------------------------------------------------------------ OA 6, clase 2
lesson(
    OA6, 2, MAT,
    "Aprenderé a usar rellenos temporales (well, you know, let me think, sure) y gestos mientras hablo. Sirve para ganar tiempo para pensar sin quedarme en silencio.",
    ["Sé organizar ideas en una presentación.", "Conozco expresiones de cortesía como please y thank you."],
    [
        "Al hablar (while speaking) a veces necesitas un momento para pensar. En vez de quedarte en silencio, puedes usar rellenos temporales (fillers): Well... (bueno), Let me think... (déjame pensar), You know... (ya sabes), I mean... (quiero decir), Actually... (en realidad) y, para aceptar una petición, Sure! Estas expresiones dan tiempo y suenan naturales si se usan poco.",
        "Cada relleno tiene un uso. Well... y Let me think... sirven cuando piensas una respuesta. You know... conecta una idea con algo que la otra persona conoce: It is near the market, you know. Sure! responde a una petición: ¿Can you show the picture? Sure! Si abusas de los rellenos, la audiencia pierde el hilo; usa uno cada tanto, no en cada frase.",
        "Los gestos (gestures) y la mirada también ayudan. Si no recuerdas una palabra, puedes mostrar el tamaño con las manos, contar con los dedos o señalar un objeto. Mantén contacto visual con tu audiencia y haz una pausa breve para pensar. Un silencio corto es mejor que decir muchas veces eh.",
    ],
    [("filler", "relleno: palabra para ganar tiempo"), ("Well...", "Bueno..."), ("Let me think...", "Déjame pensar..."), ("You know...", "Ya sabes..."), ("Sure!", "¡Claro!"), ("gesture", "gesto")],
    [
        ("Elegir un relleno", "Alguien te pregunta algo y necesitas pensar. ¿Qué relleno usas: «Well, let me think...» o «Sure!»?", ["Necesito tiempo para pensar.", "Well, let me think... da tiempo.", "Sure! es una respuesta afirmativa a una petición."], "Well, let me think..."),
        ("Responder con Sure", "Una compañera te dice: «Can you show the picture, please?» ¿Qué respondes?", ["Es una petición.", "Quiero aceptar.", "Respondo Sure!"], "Sure!"),
    ],
    [
        ("Quedarse en silencio largo cuando no se recuerda una palabra.", "La audiencia no sabe si terminaste.", "Usa un relleno o un gesto y sigue."),
        ("Usar un relleno en cada frase.", "Distrae y confunde.", "Úsalo solo cuando necesites pensar."),
    ],
    [
        ("Necesitas pensar la respuesta. ¿Qué dices? a) Well, let me think... b) Goodbye!", "a) Well, let me think...", "Es un relleno para ganar tiempo."),
        ("Te piden que muestres una imagen. ¿Qué respondes? a) Sure! b) Never!", "a) Sure!", "Sure! acepta la petición."),
        ("¿Qué significa «You know...»? a) ya sabes... b) no entiendo", "a) ya sabes...", "Conecta con algo que el otro conoce."),
    ],
    [
        ("No recuerdas la palabra «umbrella». ¿Qué gesto te ayuda? a) mostrar con las manos un objeto que se abre sobre la cabeza b) quedarte callado", "a) mostrar con las manos un objeto que se abre sobre la cabeza", "El gesto da una pista a la audiencia."),
        ("¿Cuál frase usa bien un relleno? a) It is near the market, you know. b) You know you know you know.", "a) It is near the market, you know.", "Un relleno se usa una vez y con sentido."),
        ("Quieres decir «en otras palabras, es muy pequeño». ¿Qué relleno usas? a) I mean, it is very small. b) Sure, it is very small.", "a) I mean, it is very small.", "I mean aclara o reformula."),
    ],
    [
        ("Quieres conectar tu idea con algo que tu audiencia ya conoce: «The plaza is near the school, ___.» ¿Qué relleno usas? a) you know b) let me think", "a) you know", "You know conecta con lo que el otro ya sabe."),
        ("¿Cuántos rellenos hay en «Well, I think it is big, you know, and, well, it is old, I mean, very old»? (rellenos: well, you know, I mean)", "4", "Well aparece dos veces, más you know y I mean."),
        ("Quieres decir que algo es enorme pero no recuerdas «enormous». ¿Qué gesto sirve? a) abrir los brazos mostrando un tamaño grande b) taparte la boca", "a) abrir los brazos mostrando un tamaño grande", "El gesto muestra el tamaño."),
    ],
    [
        ("Elena usa «well» antes de cada frase de su presentación (siete veces en dos minutos). ¿Qué le conviene? a) usar el relleno solo cuando necesite pensar b) usarlo más", "a) usar el relleno solo cuando necesite pensar", "El exceso de rellenos distrae."),
        ("Pedro se queda 15 segundos en silencio. ¿Qué podría hacer? a) decir «Let me think...» o mostrar un gesto y continuar b) abandonar la presentación", "a) decir «Let me think...» o mostrar un gesto y continuar", "Así recupera el hilo."),
    ],
    [
        ("Ordena la conversación con los números: (1) Sure! Here it is. (2) Can you pass me the red marker, please? (3) Thanks!", "2, 1, 3", "Primero piden, luego aceptan y al final agradecen."),
        ("Una profesora pregunta: «Why is the sea salty?». No lo sabes, pero quieres ganar tiempo. ¿Cuál es la mejor opción? a) Well, let me think... b) Pass me the book.", "a) Well, let me think...", "Gana tiempo y no cambia de tema."),
    ],
    [("Tu amiga te pide: «Can you help me with this sentence?». Quieres aceptar con naturalidad y luego pensar un momento. ¿Cuál orden sirve? a) Sure! Well, let me think... b) Well, never. Sure.", "a) Sure! Well, let me think...", "Acepta primero y luego usa un relleno para pensar.")],
    [
        ("¿Para qué sirven los rellenos?", "Para ganar tiempo al pensar", "Evitan silencios largos."),
        ("En Inglés de 8.º (OA 6, clase 2): ¿Qué significa «Let me think»?", "Déjame pensar", "Es un relleno."),
        ("¿Qué haces con las manos si olvidas una palabra?", "Usar un gesto que muestre su significado", "Ayuda a la audiencia."),
    ],
    task("Escribe una mini conversación de cuatro líneas entre dos amigos. Una persona pide algo, la otra acepta con «Sure!», y luego una tercera frase usa «Well, let me think...» para responder una pregunta. Incluye un gesto entre paréntesis.", "A: Can you show me your photo? B: Sure! (shows the photo) A: Where is it? B: Well, let me think... it is near the lake.", ["usa Sure! para aceptar", "usa un relleno para pensar", "incluye un gesto entre paréntesis"], ["diálogo de cuatro líneas", "nota de una persona de tu casa"], ["usar el relleno para cambiar de tema", "no incluir un gesto"], "Reconoce el uso correcto del relleno y ajusta el que no ayuda al diálogo."),
    "Practica con una persona de tu casa decir «Sure!» y «Well, let me think...» con un tono natural.",
    "Escribe dos situaciones de clase en que usarías un relleno distinto y qué dirías en cada una.",
)

# ------------------------------------------------------------------ OA 6, clase 3
lesson(
    OA6, 3, MAT,
    "Aprenderé a parafrasear, usar sinónimos y pedir ayuda cuando no sé una palabra. Sirve para seguir hablando aunque me falte vocabulario.",
    ["Sé usar rellenos para ganar tiempo.", "Conozco palabras como big, small y happy."],
    [
        "Si no recuerdas una palabra, no te detengas. Parafrasear (to paraphrase) es explicar con otras palabras lo que quieres decir. Si no sabes decir umbrella, puedes decir a thing you use when it rains. Si no recuerdas library, puedes decir a place where you borrow books. La audiencia entiende y tú sigues hablando.",
        "Otra estrategia es usar un sinónimo (synonym), una palabra con significado parecido: big y large, small y little, begin y start, quick y fast, happy y glad. Si olvidas una, usas la otra. Los sinónimos no siempre son idénticos, pero sirven mientras recuerdas la palabra.",
        "También puedes pedir ayuda (ask for help) con frases cortas: How do you say «paraguas» in English? What's the word for...? Can you help me, please? Does this word mean...? Pedir ayuda no es un error; es una estrategia para comunicarte. Después de recibir la palabra, repítela para recordarla.",
    ],
    [("paraphrase", "parafrasear: decir lo mismo con otras palabras"), ("synonym", "sinónimo: palabra de significado parecido"), ("How do you say...?", "¿Cómo se dice...?"), ("What's the word for...?", "¿Cuál es la palabra para...?"), ("big / large", "grande"), ("begin / start", "comenzar")],
    [
        ("Parafrasear una palabra", "No recuerdas la palabra «rabbit» (conejo). ¿Cuál es una buena paráfrasis: «an animal with long ears that jumps» o «a big building»?", ["Una paráfrasis describe la cosa.", "Un conejo tiene orejas largas y salta.", "La primera frase lo describe."], "An animal with long ears that jumps"),
        ("Usar un sinónimo", "Olvidaste la palabra «begin». ¿Qué sinónimo usas?", ["Begin significa comenzar.", "Otra palabra con ese significado es start.", "Uso start."], "Start"),
    ],
    [
        ("Detenerse y no decir nada cuando falta una palabra.", "Se interrumpe la comunicación.", "Parafrasea, usa un sinónimo o pide ayuda."),
        ("Pensar que pedir ayuda es un error.", "Pedir ayuda es una estrategia válida para comunicarse.", "Di How do you say...? y sigue."),
    ],
    [
        ("¿Qué frase parafrasea «umbrella»? a) a thing you use when it rains b) a thing you eat for lunch", "a) a thing you use when it rains", "Describe para qué sirve un paraguas."),
        ("¿Cuál es un sinónimo de «big»? a) large b) tiny", "a) large", "Large y big significan grande."),
        ("¿Qué frase pide la palabra en inglés? a) How do you say «paraguas» in English? b) Where is the umbrella?", "a) How do you say «paraguas» in English?", "Pide la palabra en otro idioma."),
    ],
    [
        ("Olvidaste «library». ¿Cuál paráfrasis sirve mejor? a) a place where you borrow books b) a place where you buy shoes", "a) a place where you borrow books", "Describe una biblioteca."),
        ("¿Cuál es un sinónimo de «quick»? a) fast b) slow", "a) fast", "Quick y fast significan rápido."),
        ("Olvidaste la palabra «fridge». ¿Qué paráfrasis sirve? a) a machine that keeps food cold b) a machine that makes music", "a) a machine that keeps food cold", "Describe la función de un refrigerador."),
    ],
    [
        ("Quieres decir «happy» pero no recuerdas la palabra. ¿Qué sinónimo puedes usar? a) glad b) angry", "a) glad", "Glad y happy significan contento."),
        ("Para pedir ayuda cuando olvidas una palabra, ¿qué frase usas? a) What's the word for...? b) Goodbye, see you.", "a) What's the word for...?", "Pide la palabra que falta."),
        ("Quieres decir que una película dura poco. ¿Qué frase usas? a) The film is very short. b) The film is very tall.", "a) The film is very short.", "Una película que dura poco es short."),
    ],
    [
        ("Pedro no sabe «towel». Dice: «the thing you use after the shower to dry your body». ¿Qué estrategia usó? a) parafrasear b) usar un sinónimo", "a) parafrasear", "Explicó la palabra con otras palabras."),
        ("Ana pide: «How do you say «lápiz» in English?». ¿Qué estrategia usó? a) pedir ayuda b) parafrasear", "a) pedir ayuda", "Preguntó cómo se dice la palabra."),
    ],
    [
        ("Elige la mejor paráfrasis para «bakery»: a) a shop where you buy bread b) a shop where you buy tires", "a) a shop where you buy bread", "Describe una panadería."),
        ("¿Cuál es un sinónimo de «begin» y también el contrario de «finish»? a) start b) enjoy", "a) start", "Start significa comenzar, igual que begin."),
    ],
    [("En una conversación, quieres decir «tablero» (blackboard) y no recuerdas la palabra. ¿Cuál sería la mejor secuencia? a) Say: The thing on the wall where the teacher writes. Then ask: What's the word for it? b) Stop talking", "a) Say: The thing on the wall where the teacher writes. Then ask: What's the word for it?", "Parafrasea y pide ayuda a la vez.")],
    [
        ("En Inglés de 8.º (OA 6, clase 3): ¿cómo te ayuda parafrasear cuando olvidas una palabra?", "Diciendo lo mismo con otras palabras", "Sirve cuando falta una palabra."),
        ("En Inglés de 8.º (OA 6, clase 3): ¿Qué es un sinónimo?", "Una palabra con significado parecido", "Por ejemplo, big y large."),
        ("¿Qué frase pide ayuda con una palabra?", "How do you say...?", "Pide la palabra en inglés."),
    ],
    task("Imagina que no sabes decir estas tres palabras: «scissors» (tijeras), «pillow» (almohada) y «bridge» (puente). Para cada una, escribe una paráfrasis en inglés. Luego escribe la frase con la que pedirías ayuda para una de ellas.", "Scissors: a tool for cutting paper. Pillow: a soft thing for your head in bed. Bridge: a way to cross a river. Ayuda: How do you say «puente» in English?", ["escribe tres paráfrasis", "cada una describe la función", "escribe una frase de ayuda"], ["hoja con tres paráfrasis", "nota de una persona de tu casa"], ["traducir palabra por palabra", "no describir la función"], "Reconoce la paráfrasis más clara y ajusta la que no explica para qué sirve la cosa."),
    "Con una persona de tu casa, juega: describe una palabra en inglés con otras palabras y que adivine cuál es.",
    "Escribe cinco pares de sinónimos en inglés y úsalos en frases.",
)

# ------------------------------------------------------------------ OA 6, clase 4
lesson(
    OA6, 4, MAT,
    "Aprenderé a usar conectores al hablar (and, but, because, so, then, also, until, first, next, finally) para unir mis ideas. Sirve para que mis frases suenen conectadas y claras.",
    ["Sé reconocer conectores al escuchar.", "Conozco frases simples como I like football."],
    [
        "Al hablar, los conectores unen frases cortas en una idea más completa. And suma ideas: I like football and I play every Saturday. But contrasta: I like tea, but I don't like coffee. Because da una razón: I stayed home because it rained. So da un resultado: It rained, so I stayed home. Then indica orden: I washed my hands, then I ate. Also añade una idea más: I also help my mother. Until marca un límite de tiempo: I waited until six.",
        "Para hablar con más fluidez, no hace falta usar frases largas: dos frases cortas bien unidas bastan. Piensa en la relación entre dos ideas (suma, contraste, razón, resultado, orden) y elige el conector. Al comienzo de una presentación, usa first y next; para cerrar, finally e in short.",
        "Activar el uso de conectores significa decidir usarlos mientras hablas, no solo cuando escribes. Antes de hablar, escribe en tu tarjeta los conectores que usarás: first, because, then. Mientras hablas, cada vez que terminas una frase pregúntate: ¿qué relación tiene con la siguiente?",
    ],
    [("and", "y (suma)"), ("but", "pero (contraste)"), ("because", "porque (razón)"), ("so", "así que (resultado)"), ("then", "luego (orden)"), ("until", "hasta que")],
    [
        ("Elegir un conector", "Completa: «I was tired, ___ I went to bed early.» ¿Usas so o but?", ["La segunda idea es un resultado de estar cansado.", "So introduce un resultado.", "Uso so."], "So"),
        ("Unir dos frases", "Une las frases «I like tea» y «I don't like coffee» con el conector adecuado.", ["Las dos ideas se contrastan.", "El conector de contraste es but.", "I like tea, but I don't like coffee."], "I like tea, but I don't like coffee"),
    ],
    [
        ("Usar and cuando hay contraste.", "And suma ideas, no las contrasta.", "Usa but para contrastar."),
        ("Poner because delante del resultado.", "Because va con la razón; el resultado va con so.", "Pregunta cuál idea es la razón."),
    ],
    [
        ("Elige el conector: «I stayed home ___ it rained.» a) because b) so", "a) because", "It rained es la razón."),
        ("Elige el conector: «I wash my hands, ___ I eat.» a) then b) but", "a) then", "Indica el orden de las acciones."),
        ("Elige el conector: «She plays the piano ___ she also sings.» a) and b) until", "a) and", "Suma dos acciones."),
    ],
    [
        ("Elige el conector: «I like the beach, ___ I don't like the sand.» a) but b) so", "a) but", "Hay un contraste entre lo que gusta y lo que no."),
        ("Elige el conector: «I waited ___ the bus came.» a) until b) because", "a) until", "Marca el momento en que termina la espera."),
        ("Elige el conector: «We were late, ___ we took a taxi.» a) so b) until", "a) so", "Tomar un taxi es el resultado de llegar tarde."),
    ],
    [
        ("Une con el mejor conector: «I helped my sister. I also washed the dishes.» ¿Qué palabra suma una idea más? a) also b) but", "a) also", "Also añade otra acción."),
        ("Elige la mejor opción para unir en una sola idea: «It was cold. I wore a jacket.» a) It was cold, so I wore a jacket. b) It was cold, until I wore a jacket.", "a) It was cold, so I wore a jacket.", "Llevar chaqueta es el resultado del frío."),
        ("Ordena con números las ideas: (1) Finally, I sent the email. (2) First, I wrote the email. (3) Then, I read it twice.", "2, 3, 1", "Los conectores marcan el orden."),
    ],
    [
        ("Ana dice: «I was hungry, because I ate a sandwich». ¿Qué corriges? a) usar so en lugar de because b) usar and c) quitar el sandwich", "a) usar so en lugar de because", "Comer es el resultado del hambre."),
        ("¿Por qué «I like football, but I play every day» suena raro? a) porque no hay contraste entre las dos ideas b) porque falta una palabra", "a) porque no hay contraste entre las dos ideas", "But exige contraste; aquí conviene and."),
    ],
    [
        ("Construye una respuesta de dos frases con un conector a la pregunta «Why were you late?». Elige la mejor: a) I missed the bus, so I walked. b) I missed the bus, but I like walking.", "a) I missed the bus, so I walked.", "Explica la causa y el resultado."),
        ("¿Qué conector usarías para decir «hasta las ocho» en «I studied ___ eight o'clock»? a) until b) so", "a) until", "Until marca el límite de tiempo."),
    ],
    [("En tu presentación quieres explicar por qué te gusta el fútbol. ¿Qué frase usa bien un conector de razón? a) I like football because it is fun. b) I like football, so it is fun because.", "a) I like football because it is fun.", "Because introduce la razón.")],
    [
        ("En Inglés de 8.º (OA 6, clase 4): ¿con qué conector das la razón de algo al hablar?", "Because", "Because significa porque y da la razón."),
        ("En Inglés de 8.º (OA 6, clase 4): ¿Qué conector introduce un resultado?", "So", "Significa así que o por eso."),
        ("¿Qué conector marca contraste?", "But", "But significa pero y contrasta ideas."),
    ],
    task("Imagina que cuentas qué hiciste ayer y debes usar al menos cuatro conectores distintos. Con esta información de ejemplo: te levantaste temprano, tomaste desayuno, esperaste el bus, fuiste al colegio, te gustó la clase de arte. Escribe cuatro frases en inglés con first, then, because y until.", "First, I got up early. Then, I had breakfast. I waited for the bus until seven because it was late. I liked art class because it was fun.", ["usa cuatro conectores distintos", "cada conector tiene sentido", "las frases cuentan lo dado"], ["hoja con cuatro frases", "nota de una persona de tu casa"], ["usar because con un resultado", "usar until sin un momento"], "Reconoce los conectores bien usados y revisa la relación en el que no calza."),
    "Di en voz alta las cuatro frases modelo y marca con un lápiz el conector en cada una.",
    "Escribe un párrafo de cinco frases sobre tu fin de semana usando and, but, because, so y then.",
)

# ------------------------------------------------------------------ OA 6, clase 5
lesson(
    OA6, 5, MAT,
    "Aprenderé a revisar mi inglés hablado después de hablar: registrar mis errores y corregirlos con ayuda de mi docente y de recursos. Sirve para mejorar en cada presentación.",
    ["Sé usar estrategias antes y durante el habla.", "Conozco reglas como el -s del presente y el -ed del pasado."],
    [
        "Después de hablar (after speaking) conviene revisar cómo te fue. Un registro de errores (error log) es una tabla con tres columnas: lo que dije, la forma correcta y la regla o recurso que me ayuda. Por ejemplo: «He go to school» / «He goes to school» / en presente, he y she llevan -s.",
        "Los errores más frecuentes en estudiantes de español son: He go (correcto: he goes), I am agree (correcto: I agree), I have 14 years (correcto: I am 14 years old), she don't (correcto: she doesn't), more big (correcto: bigger), I didn't went (correcto: I didn't go), make homework (correcto: do homework) y dis (correcto: this con /ð/). Al registrarlos, aprendes a reconocerlos antes de decirlos.",
        "Para corregir, usa ayuda: tu docente, un diccionario o un cuaderno de reglas. Escribe la forma correcta y una frase nueva con ella. Después, practica esa frase en voz alta. Elige uno o dos errores por vez, no todos, para no cansarte. En la próxima presentación, revisa si ese error desapareció.",
    ],
    [("error log", "registro de errores: tabla de lo que corriges"), ("correct form", "forma correcta"), ("rule", "regla"), ("review", "revisar"), ("resource", "recurso: diccionario, cuaderno, docente"), ("feedback", "comentarios para mejorar")],
    [
        ("Corregir un error", "Un compañero dice «He go to school». ¿Cuál es la forma correcta?", ["En presente, he lleva -s en el verbo.", "Go pasa a goes.", "He goes to school."], "He goes to school"),
        ("Completar el registro", "Registro de errores: dije «I am agree». ¿Qué escribes como forma correcta?", ["Agree es un verbo en sí mismo.", "No necesita am.", "I agree."], "I agree"),
    ],
    [
        ("Querer corregir todos los errores al mismo tiempo.", "Es difícil recordar tantas reglas a la vez.", "Elige uno o dos errores por presentación."),
        ("No escribir la forma correcta, solo la regla.", "Sin la frase correcta es más difícil practicarla.", "Escribe siempre una frase correcta nueva."),
    ],
    [
        ("¿Cuál es la forma correcta? a) She has a dog. b) She have a dog.", "a) She has a dog.", "Con she se usa has."),
        ("¿Cuál es la forma correcta? a) I am 14 years old. b) I have 14 years.", "a) I am 14 years old.", "Para la edad se usa be, no have."),
        ("¿Cuál es la forma correcta? a) I didn't go to school. b) I didn't went to school.", "a) I didn't go to school.", "Después de didn't el verbo va en base."),
    ],
    [
        ("¿Cuál es la forma correcta? a) The red bag is bigger. b) The red bag is more big.", "a) The red bag is bigger.", "Big es corto y lleva -er."),
        ("¿Cuál es la forma correcta? a) I do my homework. b) I make my homework.", "a) I do my homework.", "Homework va con do."),
        ("¿Qué tres columnas tiene un registro de errores? a) lo que dije, forma correcta y regla b) nombre, edad y curso", "a) lo que dije, forma correcta y regla", "Ordena el error, su corrección y el recurso."),
    ],
    [
        ("Completa el registro: lo que dije: «Yesterday I play football». ¿Cuál es la forma correcta? a) Yesterday I played football. b) Yesterday I plays football.", "a) Yesterday I played football.", "Yesterday pide pasado con -ed."),
        ("Completa el registro: lo que dije: «dis is my brother». ¿Qué debes corregir? a) el sonido /ð/ de this b) el verbo is", "a) el sonido /ð/ de this", "This empieza con /ð/, no con d."),
        ("Julia anotó: «She don't like fish». ¿Cuál es la forma correcta? a) She doesn't like fish. b) She not like fish.", "a) She doesn't like fish.", "Con she se usa doesn't."),
    ],
    [
        ("Después de una presentación, cometiste 7 errores distintos. ¿Cuántos conviene trabajar primero? a) uno o dos b) los siete a la vez", "a) uno o dos", "Es más realista y efectivo."),
        ("Tras corregir un error, ¿qué conviene hacer? a) escribir una frase nueva y practicarla en voz alta b) olvidarlo", "a) escribir una frase nueva y practicarla en voz alta", "Practicar fija la forma correcta."),
    ],
    [
        ("Un registro de errores dice: «He go» / «He goes» / «-s con he y she». ¿Qué tipo de error es? a) de verbo en presente b) de pronunciación", "a) de verbo en presente", "Falta el -s en el presente."),
        ("Elena registró «more tall» y corrigió «taller». ¿Qué regla anotó? a) adjetivos cortos llevan -er b) adjetivos largos llevan more", "a) adjetivos cortos llevan -er", "Tall es corto."),
    ],
    [("Quieres revisar tu último discurso. ¿Qué recurso sirve más para confirmar si «make homework» es correcto? a) un diccionario o tu docente b) adivinar", "a) un diccionario o tu docente", "Son recursos confiables.")],
    [
        ("¿Para qué sirve un registro de errores?", "Para registrar y corregir lo que dije mal", "Ayuda a mejorar en cada presentación."),
        ("En Inglés de 8.º (OA 6, clase 5): ¿Cuál es la forma correcta de «I have 14 years»?", "I am 14 years old", "La edad se dice con be."),
        ("¿Quién puede ayudarte a corregir?", "El docente y los recursos como el diccionario", "Son apoyos para revisar."),
    ],
    task("Con este texto de ejemplo, en que un compañero habló, completa un registro de errores con tres columnas (lo que dijo / forma correcta / regla): «He go to school. I am agree with you. She have two brothers.»", "He go / He goes / en presente he lleva -s; I am agree / I agree / agree no lleva am; She have / She has / con she se usa has.", ["anota los tres errores", "escribe la forma correcta de cada uno", "dice una regla breve"], ["tabla de tres filas", "nota de una persona de tu casa"], ["escribir la regla sin la forma correcta", "corregir solo uno"], "Reconoce las correcciones acertadas y revisa la regla de las que dudó con tu docente."),
    "Mira tu último trabajo en inglés y escribe tres errores con su forma correcta.",
    "Practica en voz alta cada frase corregida de tu registro tres veces.",
)
