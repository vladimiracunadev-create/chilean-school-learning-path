"""Cuaderno del estudiante, 7.º básico Inglés (oficial), IN07 OA 09 (comprensión de ideas generales e información explícita en
textos escritos adaptados, impresos o digitales). Todos los textos son originales y están escritos en cada enunciado
con su glosa en español; los elementos visuales se describen con palabras.
"""
from __future__ import annotations

from student_content_in7_a import lesson, task
from student_lessons import arith

OA9 = "IN07 OA 09"
MAT = "Los textos y datos escritos en cada ejercicio, lápiz y, si quieres, un destacador o un lápiz de color para subrayar las pistas."

EMAIL = "«From: Mr. Díaz. To: Parents of 7A. Subject: Science trip. Dear parents, our class will visit the planetarium next Thursday. The bus leaves at 8:30 and returns at 1:00. Please sign the permission form by Monday. Best regards, Mr. Díaz» (parents = apoderados, planetarium = planetario, leaves = sale, returns = vuelve, sign = firmar, permission form = autorización)"
FLYER = "«BIKE REPAIR DAY. Saturday, 10:00 to 14:00. School yard. Free! Bring your bike. Volunteers will fix flat tires and brakes. Bring a helmet if you want a safety check.» (repair = reparación, free = gratis, volunteers = voluntarios, flat tires = neumáticos pinchados, brakes = frenos, safety check = revisión de seguridad)"
WEB = "«Welcome to the City Museum. Opening hours: Tuesday to Sunday, 10:00 to 18:00. Tickets: adults $4,000, children $2,000. Free entry on the first Sunday of each month. Closed on Mondays.» (opening hours = horario de atención, tickets = entradas, adults = adultos, children = niños, free entry = entrada gratis, closed = cerrado)"
COMIC = "«Why I Read Comics. Many adults think comics are not real reading. I disagree. Comics help me imagine places, and the pictures help me understand new words. Last month I read a comic about explorers, and then I borrowed a book about maps from the library.» (comics = historietas, disagree = no estar de acuerdo, imagine = imaginar, pictures = dibujos, explorers = exploradores, borrowed = pedí prestado)"
CHOIR = "«School Choir Wins Regional Prize. The Santa Rosa School choir won first place at the regional music festival on Saturday. Twenty-four students sang three songs. The judges liked the clear voices and the teamwork. The choir will perform again at the school anniversary.» (choir = coro, prize = premio, first place = primer lugar, judges = jurado, teamwork = trabajo en equipo, perform = presentarse, anniversary = aniversario)"
CAMP = "«Summer Camp at Lake Azul. Dates: 6 to 10 January. Activities: Monday kayaking, Tuesday painting, Wednesday hiking, Thursday games, Friday party. Price: $60,000 per child. The price includes lunch and a T-shirt. Bring: sunscreen, a hat and a water bottle. Registration until 20 December.» (camp = campamento, kayaking = kayak, painting = pintura, hiking = caminata, includes = incluye, T-shirt = polera, sunscreen = bloqueador, registration = inscripción)"
PLANT = "«How a Plant Drinks. Roots take water from the soil. The stem carries the water up. The leaves use sunlight to make food.» Diagrama descrito: una flecha parte de la raíz (roots), pasa por el tallo (stem) y llega a las hojas (leaves). Pie de imagen: «Water travels up from the roots to the leaves.» (soil = tierra, carries = lleva, sunlight = luz del sol, travels = viaja)"
CHART = "Gráfico de barras descrito: libros leídos por curso en octubre. 7A: 45, 7B: 38, 7C: 52. Pie del gráfico: «Class 7C read the most books.» (read = leyó, the most = la mayor cantidad)"
LIGHT = "«On Rock Island there is a small lighthouse. Every evening, the keeper, Mr. Soto, turns on the light at seven. Boats use the light to stay away from the rocks. In winter, strong winds make the island very cold, so Mr. Soto wears a thick coat. Visitors can climb the 60 steps on Saturdays.» (lighthouse = faro, keeper = farero, turns on = enciende, rocks = rocas, winds = vientos, thick = grueso, coat = abrigo, steps = escalones)"

# ------------------------------------------------------------------ clase 1
lesson(
    OA9, 1, MAT,
    "Aprenderé a reconocer el formato de un texto escrito (correo, volante, página web, receta, biografía) y su propósito. Sirve para saber qué información buscar antes de leer los detalles.",
    ["Sé que un texto tiene un propósito.", "Conozco palabras como dear, free y tickets."],
    [
        "Los textos escritos tienen distintos formatos (formats), y cada formato tiene pistas propias. Un correo electrónico (email) lleva From, To y Subject, comienza con Dear... y termina con Best regards. Un volante o aviso (flyer, notice) usa letras grandes, fecha, lugar y palabras que invitan, como Free! Una página web (web page) muestra títulos como Welcome, menús y datos de horarios o precios. Una receta (recipe) tiene Ingredients y Method. Una biografía (biography) cuenta la vida de una persona con frases como was born (nació) y fechas.",
        "El propósito (purpose) es lo que el texto quiere lograr: informar, invitar, pedir algo o explicar cómo hacer algo. El correo del profesor informa una salida y pide una firma. El volante invita a un día de reparación de bicicletas. La página del museo informa horarios y precios. Reconocer el formato te dice qué datos buscar: en un correo, quién escribe y qué pide; en un volante, cuándo y dónde.",
        "Para decidir, mira primero lo que no es el texto principal: el título, las etiquetas, los números y los signos de exclamación. Luego lee la primera y la última frase. No necesitas entender todo para reconocer el formato. Con esa información ya puedes predecir qué tipo de datos aparecerán.",
    ],
    [("email", "correo electrónico"), ("flyer", "volante o aviso"), ("web page", "página web"), ("recipe", "receta"), ("biography", "biografía"), ("purpose", "propósito"), ("format", "formato: forma en que se presenta un texto")],
    [
        ("Reconocer el formato", EMAIL + " ¿Qué formato tiene y qué pista lo muestra?", ["Veo From, To y Subject al comienzo.", "Termina con Best regards.", "Es un correo electrónico."], "Es un correo electrónico: tiene From, To, Subject y Best regards"),
        ("Reconocer el propósito", FLYER + " ¿Cuál es el propósito?", ["Hay letras grandes y Free!.", "Dice Bring your bike.", "Invita a un día de reparación de bicicletas."], "Invitar a un día de reparación gratuita de bicicletas"),
    ],
    [
        ("Pensar que un texto con números es siempre una página web.", "Se mira un solo rasgo.", "Fíjate en varias pistas: encabezado, saludo y despedida."),
        ("Leer detalles antes de saber el formato.", "No se sabe qué buscar.", "Reconoce primero el formato y el propósito."),
    ],
    [
        (EMAIL + " ¿Qué formato tiene? a) un correo electrónico b) una receta", "a) un correo electrónico", "Tiene From, To y Subject."),
        (FLYER + " ¿Qué formato tiene? a) un volante o aviso b) una biografía", "a) un volante o aviso", "Usa letras grandes y datos del evento."),
        (WEB + " ¿Qué formato tiene? a) una página web b) un correo", "a) una página web", "Tiene Welcome, horarios y precios."),
    ],
    [
        (EMAIL + " ¿Cuál es el propósito? a) informar una salida y pedir una firma b) vender entradas", "a) informar una salida y pedir una firma", "Dice la salida y Please sign the permission form."),
        (FLYER + " ¿Qué palabra muestra que es gratis?", "Free", "Free! aparece en el volante."),
        (WEB + " ¿Qué palabras anuncian los horarios?", "Opening hours", "Opening hours son los horarios de atención."),
    ],
    [
        ("«Dear Mrs. Pérez, thank you for your message. Best regards, Ana». ¿Qué formato tiene? a) un correo o carta b) una receta", "a) un correo o carta", "Dear y Best regards son saludo y despedida."),
        ("«Ingredients: two eggs, one cup of flour. Method: mix and bake.» (flour = harina, bake = hornear). ¿Qué formato tiene? a) una receta b) un aviso", "a) una receta", "Ingredients y Method son partes de una receta."),
        ("«María was born in a small town. She wrote her first book at 20.» (was born = nació). ¿Qué formato tiene? a) una biografía b) una página web", "a) una biografía", "Cuenta la vida de una persona."),
    ],
    [
        (FLYER + " Tiene letras grandes, «Free!» y «Bring your bike». ¿Qué tipo de lenguaje usa? a) lenguaje que invita b) lenguaje técnico", "a) lenguaje que invita", "Busca atraer a las personas."),
        ("¿Por qué conviene reconocer el formato antes de leer? a) para saber qué información buscar b) para leer más rápido sin pensar", "a) para saber qué información buscar", "Cada formato entrega datos distintos."),
    ],
    [
        (EMAIL + " ¿Qué debe hacer el apoderado antes del lunes?", "Firmar la autorización", "Dice sign the permission form by Monday."),
        arith(WEB + " ¿Cuántos pesos paga una familia con un adulto y dos niños?", "4000+2*2000", "Se suma la entrada del adulto y las de los niños.", " pesos"),
    ],
    [("Ves un cartel: «LOST CAT. Brown and small. Please tell the school office if you see it.» (lost = perdido, office = oficina). ¿Cuál es su propósito? a) pedir ayuda para encontrar un gato b) vender un gato", "a) pedir ayuda para encontrar un gato", "Dice lost y pide avisar si lo ven.")],
    [
        ("¿Qué pistas tiene un correo electrónico?", "From, To, Subject, Dear y Best regards", "Muestran el formato."),
        ("En Inglés de 7.º (OA 9, clase 1): ¿Qué es el propósito de un texto?", "Lo que quiere lograr", "Puede informar, invitar o explicar."),
        ("¿Qué significa «free»?", "Gratis", "En un volante indica que no se paga."),
    ],
    task("Observa estos tres mini textos: A) «Subject: Homework. Dear Ms. Vera, I have a question about page 20. Best regards, Pablo» B) «CLEAN-UP DAY. Sunday 9:00. Park. Bring gloves. Free snack!» (gloves = guantes) C) «Welcome to our library. Open Monday to Friday, 8:00 to 17:00.» Escribe el formato y el propósito de cada uno.", "A: correo, hacer una pregunta. B: volante, invitar a limpiar el parque. C: página web, informar el horario.", ["identifica el formato de los tres", "indica el propósito de cada uno", "cita una pista"], ["hoja con tres formatos y propósitos", "nota de quien revisó"], ["confundir B con un correo", "no indicar el propósito"], "Reconoce los formatos acertados y repasa con quien te apoya las pistas de cada uno."),
    "Busca en casa un volante o aviso en español y di su formato, propósito y dos pistas.",
    "Escribe un volante breve en inglés para invitar a un partido en tu colegio.",
)

# ------------------------------------------------------------------ clase 2
lesson(
    OA9, 2, MAT,
    "Aprenderé a identificar la idea principal de un texto escrito y a distinguirla de los detalles. Sirve para resumir lo esencial de lo que leo.",
    ["Sé reconocer el formato y el propósito de un texto.", "Conozco palabras como comics, choir y prize."],
    [
        "La idea principal (main idea) es lo más importante que dice un texto; los detalles (details) son los datos que la apoyan. En una noticia, el titular (headline) suele resumir la idea principal: School Choir Wins Regional Prize. Los datos como Twenty-four students sang three songs son detalles. En un texto de opinión, la idea principal es lo que el autor defiende; en el texto de los cómics, es que los cómics también son una lectura útil.",
        "Para encontrarla, haz tres preguntas: ¿de qué trata?, ¿qué dice el autor sobre ese tema? y ¿qué frase resume todo? Fíjate en el título, en la primera y última frase de cada párrafo, y en las palabras que se repiten. Palabras como but, however (sin embargo) y I disagree marcan un contraste que suele introducir la idea del autor.",
        "Una buena idea principal es completa pero breve. Si es demasiado pequeña (explorers) es solo un detalle. Si es demasiado amplia (libros), no dice nada específico. Para comprobarla, pregúntate si todos los detalles del texto la apoyan. Si un detalle no encaja, tu idea principal probablemente es muy pequeña.",
    ],
    [("main idea", "idea principal"), ("detail", "detalle"), ("headline", "titular"), ("topic", "tema"), ("I disagree", "no estoy de acuerdo"), ("author", "autor")],
    [
        ("Idea principal de una noticia", CHOIR + " ¿Cuál es la idea principal?", ["Leo el titular: School Choir Wins Regional Prize.", "El resto del texto da detalles.", "La idea es que el coro ganó un premio regional."], "El coro del colegio ganó un premio regional"),
        ("Idea del autor", COMIC + " ¿Qué defiende el autor?", ["Busco I disagree.", "Rechaza que los cómics no sean lectura.", "Defiende que los cómics son una lectura útil."], "Que los cómics son una lectura útil"),
    ],
    [
        ("Elegir un detalle como idea principal.", "Se toma una parte pequeña del texto.", "Pregúntate si todos los datos apoyan tu idea."),
        ("Escribir una idea tan amplia que sirve para cualquier texto.", "No dice nada específico.", "Agrega qué dice el texto sobre el tema."),
    ],
    [
        (COMIC + " ¿De qué trata el texto? a) de los cómics como lectura b) de cómo dibujar", "a) de los cómics como lectura", "Se repite comics y reading."),
        (CHOIR + " ¿Cuál es el titular?", "School Choir Wins Regional Prize", "Es el título de la noticia."),
        (COMIC + " ¿Quién dice «I disagree»? a) el autor b) los adultos", "a) el autor", "El autor responde a lo que piensan los adultos."),
    ],
    [
        (COMIC + " ¿Cuál es la idea principal? a) los cómics son una lectura útil b) los adultos leen más que los niños", "a) los cómics son una lectura útil", "Defiende los cómics como lectura."),
        (CHOIR + " ¿Cuál es un detalle y no la idea principal? a) Twenty-four students sang three songs. b) The choir won a prize.", "a) Twenty-four students sang three songs.", "Es un dato de apoyo."),
        (COMIC + " ¿Qué dice el texto que piensan muchos adultos?", "Que los cómics no son lectura de verdad", "Dice comics are not real reading."),
    ],
    [
        (CHOIR + " ¿Cuál es la mejor idea principal? a) el coro ganó un premio regional por su trabajo b) el festival fue el domingo", "a) el coro ganó un premio regional por su trabajo", "Resume el titular y el cuerpo."),
        (COMIC + " ¿Qué frase apoya la idea principal? a) the pictures help me understand new words b) last month I read a comic", "a) the pictures help me understand new words", "Explica por qué los cómics ayudan."),
        (CHOIR + " ¿El titular resume la idea principal? Responde sí o no.", "Sí", "School Choir Wins Regional Prize resume la noticia."),
    ],
    [
        ("Un compañero dice que la idea principal del texto de los cómics es «explorers». ¿Qué error comete? a) confunde un detalle con la idea principal b) no leyó nada", "a) confunde un detalle con la idea principal", "Explorers es solo un ejemplo."),
        (CHOIR + " ¿Qué titular alternativo sirve? a) Choir wins prize b) Judges like clear voices", "a) Choir wins prize", "Resume la noticia."),
    ],
    [
        arith(CHOIR + " Si los 24 estudiantes se dividen en 4 filas iguales, ¿cuántos hay por fila?", "24//4", "Se reparten los 24 estudiantes entre las 4 filas.", " estudiantes"),
        (COMIC + " ¿Qué palabra muestra el contraste con lo que dicen los adultos?", "disagree", "I disagree rechaza la idea de los adultos."),
    ],
    [("Un cartel de la biblioteca dice: «A new quiet corner opens on Monday. Students can read, draw or write there.» (quiet corner = rincón tranquilo, draw = dibujar, write = escribir). ¿Cuál es la idea principal? a) la biblioteca abre un rincón tranquilo para leer, dibujar o escribir b) los estudiantes deben comprar cuadernos", "a) la biblioteca abre un rincón tranquilo para leer, dibujar o escribir", "Resume lo que anuncia el cartel.")],
    [
        ("¿Qué es la idea principal?", "Lo más importante que dice el texto", "Los detalles la apoyan."),
        ("¿Dónde suele estar la idea principal en una noticia?", "En el titular y en la primera frase", "Resume la noticia."),
        ("En Inglés de 7.º (OA 9, clase 2): ¿Qué significa «I disagree»?", "No estoy de acuerdo", "Marca una opinión distinta."),
    ],
    task("Lee este texto: «Many people think that cats and dogs cannot be friends. In my house, they are. My cat Luna and my dog Rocky sleep together every night, and they play with the same ball. They show that different animals can live in peace.» (friends = amigos, sleep = duermen, ball = pelota, peace = paz). Escribe la idea principal en una frase y dos detalles.", "Idea principal: animales distintos pueden ser amigos. Detalles: duermen juntos; juegan con la misma pelota.", ["una idea principal completa y breve", "dos detalles del texto", "no copia el texto"], ["hoja con idea y detalles", "nota de quien revisó"], ["elegir un detalle como idea", "inventar un detalle"], "Reconoce lo que acertó y pregunta qué frase resume todo el texto."),
    "Subraya con un lápiz de color la frase que resume el texto de los cómics.",
    "Escribe un titular en inglés de siete palabras para una noticia sobre una feria del libro.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA9, 3, MAT,
    "Aprenderé a ubicar información explícita en un texto escrito: fechas, precios, actividades, lugares y objetos. Sirve para responder con exactitud usando lo que el texto dice.",
    ["Sé reconocer el formato de un texto.", "Conozco los meses y los días en inglés."],
    [
        "La información explícita (explicit information) es la que el texto dice directamente. Para encontrarla, lee la pregunta primero y decide qué dato buscas: when (fecha u hora), where (lugar), how much (precio), how many (cantidad) o what (cosa o actividad). Luego busca en el texto la palabra clave de la pregunta, como Price, Dates, Bring o Registration.",
        "En textos con listas y datos, como el campamento de verano, cada línea tiene una etiqueta: Dates, Activities, Price, Bring, Registration. Las etiquetas te guían. Fíjate en los números y en las fechas: 6 to 10 January son cinco días si cuentas el 6 y el 10. Con una lista como Monday kayaking, Tuesday painting, Wednesday hiking, relaciona cada día con su actividad.",
        "Responde solo con lo que el texto dice. Si el texto no menciona el transporte, no puedes afirmar que está incluido. Al terminar, vuelve al texto y subraya la frase que comprueba tu respuesta. Si no la encuentras, probablemente estás suponiendo.",
    ],
    [("dates", "fechas"), ("price", "precio"), ("includes", "incluye"), ("bring", "traer"), ("registration", "inscripción"), ("explicit", "dicho directamente")],
    [
        ("Ubicar una actividad", CAMP + " ¿Qué actividad hay el miércoles?", ["Busco Wednesday.", "Dice Wednesday hiking.", "Hiking es caminata."], "Una caminata"),
        ("Ubicar un precio", CAMP + " ¿Cuánto cuesta el campamento por niño?", ["Busco Price.", "Dice $60,000 per child.", "Son sesenta mil pesos."], "$60.000"),
    ],
    [
        ("Afirmar algo que el texto no dice.", "Se supone en vez de buscar la frase.", "Responde solo con datos escritos en el texto."),
        ("Contar mal los días de un rango.", "No se cuenta el primer o el último día.", "Cuenta incluyendo el día de inicio y el de término."),
    ],
    [
        (CAMP + " ¿Cuántos días dura el campamento, del 6 al 10 de enero contando ambos días?", "5", "Son los días 6, 7, 8, 9 y 10."),
        (CAMP + " ¿Qué día es la fiesta?", "El viernes", "Dice Friday party."),
        (CAMP + " ¿Cuánto cuesta por niño?", "$60.000", "Dice Price: $60,000 per child."),
    ],
    [
        (CAMP + " ¿Qué incluye el precio? a) almuerzo y una polera b) transporte y cena", "a) almuerzo y una polera", "Dice includes lunch and a T-shirt."),
        (CAMP + " ¿Hasta cuándo es la inscripción?", "Hasta el 20 de diciembre", "Dice Registration until 20 December."),
        (CAMP + " ¿Cuántas cosas hay que llevar según el aviso?", "3", "Dice Bring: sunscreen, a hat and a water bottle; son tres objetos."),
    ],
    [
        arith(CAMP + " ¿Cuántos pesos pagan dos hermanos por el campamento?", "2*60000", "Cada niño paga $60.000.", " pesos"),
        (CAMP + " ¿Qué actividad ocurre antes de painting? a) kayaking b) hiking", "a) kayaking", "El lunes hay kayak y el martes pintura."),
        (CAMP + " ¿Dónde es el campamento?", "En el Lago Azul", "Dice Lake Azul."),
    ],
    [
        ("Un apoderado dice que el campamento incluye transporte. ¿Lo dice el texto? Responde sí o no.", "No", "Solo dice que incluye almuerzo y polera."),
        (CAMP + " ¿Qué dato responde la pregunta «Where»? a) Lake Azul b) 6 to 10 January", "a) Lake Azul", "Es el lugar."),
    ],
    [
        arith(CAMP + " Un niño paga $20.000 hoy y el resto en dos cuotas iguales. ¿Cuánto es cada cuota?", "(60000-20000)//2", "Se resta lo ya pagado y se divide entre las dos cuotas.", " pesos"),
        (CAMP + " ¿Cuántas actividades distintas se nombran?", "5", "Son una por día, de lunes a viernes."),
    ],
    [(CAMP + " Hoy es 15 de diciembre y quieres inscribir a una persona de tu casa. ¿Estás a tiempo? Responde sí o no.", "Sí", "La inscripción es hasta el 20 de diciembre.")],
    [
        ("En Inglés de 7.º (OA 9, clase 3): ¿Qué es información explícita?", "La que el texto dice directamente", "No se supone."),
        ("¿Qué pregunta busca un precio?", "How much", "How much es cuánto."),
        ("En Inglés de 7.º (OA 9, clase 3): ¿Qué haces al terminar de responder?", "Vuelvo al texto y subrayo la frase que lo comprueba", "Así compruebo mi respuesta."),
    ],
    task("Lee este aviso: «Chess Tournament at Santa Clara School. Date: 12 December. Time: 10:00 to 15:00. Players: 7th to 8th grade. Prize: a chess board. Bring: your own pencil. Registration: with Mr. Vera by 5 December.» (tournament = torneo, players = jugadores, prize = premio, board = tablero). Escribe en tu hoja la fecha, el horario, el premio y el último día para inscribirse.", "12 de diciembre; 10:00 a 15:00; un tablero de ajedrez; 5 de diciembre.", ["anota los cuatro datos", "usa solo lo que dice el texto", "cita la etiqueta de cada dato"], ["hoja con cuatro datos", "nota de quien revisó"], ["confundir la fecha con el plazo de inscripción", "inventar un dato"], "Reconoce los datos acertados y revisa las etiquetas del aviso."),
    "Subraya con colores distintos las fechas, los precios y los objetos en el texto del campamento.",
    "Escribe cuatro preguntas con when, where, how much y what sobre el aviso del torneo de ajedrez.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA9, 4, MAT,
    "Aprenderé a relacionar el texto con elementos visuales como diagramas, gráficos, mapas y pies de imagen. Sirve para comprender mejor y comprobar que la imagen y el texto dicen lo mismo.",
    ["Sé ubicar información explícita.", "Sé leer un gráfico de barras sencillo."],
    [
        "Los elementos visuales (visual elements) completan el texto: un diagrama muestra el recorrido del agua en una planta, un gráfico de barras compara cantidades y un mapa ubica lugares. El pie de imagen (caption) es una frase breve que explica la imagen: Water travels up from the roots to the leaves. Las etiquetas (labels), como roots o stem, nombran las partes.",
        "Para integrar texto e imagen, lee primero el título y el pie, luego observa la imagen y después el texto. Comprueba si dicen lo mismo. En un gráfico, busca el número de cada barra y compara. En un diagrama con flechas, sigue el orden de las flechas. Si el pie dice que la clase 7C leyó más y las barras muestran 45, 38 y 52, la barra de 7C es la más alta, así que el pie es correcto.",
        "A veces la imagen aporta información que el texto no tiene, como las cantidades exactas. Otras veces el texto explica lo que la imagen solo muestra. Los buenos lectores usan las dos fuentes. Si el texto y la imagen se contradicen, vuelve a leer con cuidado y decide qué dato es el correcto.",
    ],
    [("diagram", "diagrama"), ("caption", "pie de imagen"), ("label", "etiqueta"), ("chart", "gráfico"), ("map", "mapa"), ("arrow", "flecha")],
    [
        ("Leer un diagrama", PLANT + " ¿Qué parte de la planta toma el agua del suelo?", ["Busco Roots take water from the soil.", "Las raíces están en el diagrama.", "Las raíces toman el agua."], "Las raíces"),
        ("Leer un gráfico", CHART + " ¿Qué curso leyó más libros?", ["Comparo 45, 38 y 52.", "52 es el número mayor.", "Lo leyó el 7C."], "7C"),
    ],
    [
        ("Mirar solo la imagen y no leer el pie.", "Se pierde información que el pie explica.", "Lee el pie y las etiquetas antes de interpretar."),
        ("Pasar por alto un número del gráfico.", "Se compara a ojo y se comete un error.", "Lee el número de cada barra."),
    ],
    [
        (PLANT + " ¿Qué parte absorbe el agua? a) las raíces b) las hojas", "a) las raíces", "Roots take water from the soil."),
        (CHART + " ¿Cuántos libros leyó 7B?", "38", "Es el dato de la barra de 7B."),
        (CHART + " ¿Qué curso leyó más libros?", "7C", "Tiene 52, el número mayor."),
    ],
    [
        (PLANT + " ¿Qué muestra el pie de imagen? a) el recorrido del agua desde las raíces hasta las hojas b) los frutos de la planta", "a) el recorrido del agua desde las raíces hasta las hojas", "Dice Water travels up from the roots to the leaves."),
        arith(CHART + " ¿Cuántos libros más leyó 7C que 7B?", "52-38", "Se resta el dato de 7B al de 7C.", " libros"),
        (PLANT + " ¿En qué orden van las flechas del diagrama? a) raíces, tallo, hojas b) hojas, tallo, raíces", "a) raíces, tallo, hojas", "La flecha parte de la raíz y llega a las hojas."),
    ],
    [
        arith(CHART + " ¿Cuántos libros leyeron en total los tres cursos?", "45+38+52", "Se suman los tres datos.", " libros"),
        (PLANT + " ¿Qué hacen las hojas, según el texto?", "Usan la luz del sol para hacer alimento", "Dice The leaves use sunlight to make food."),
        ("Mapa descrito: la biblioteca está junto al gimnasio y la cafetería queda al otro lado del patio. ¿Qué lugar está junto a la biblioteca?", "El gimnasio", "El mapa lo ubica al lado."),
    ],
    [
        (CHART + " Un compañero dice que 7A leyó más libros que 7C. ¿Concuerda con el gráfico? Responde sí o no.", "No", "7A tiene 45 y 7C tiene 52."),
        ("¿Por qué una imagen complementa un texto? a) porque entrega datos o muestra lo que el texto explica b) porque solo lo decora", "a) porque entrega datos o muestra lo que el texto explica", "Texto e imagen se apoyan."),
    ],
    [
        arith(CHART + " Si los tres cursos hubieran leído lo mismo, ¿cuántos libros leería cada uno?", "(45+38+52)//3", "Se suman los tres datos y se reparten entre tres.", " libros"),
        (CHART + " ¿Cuántos cursos leyeron más de 40 libros? Responde con un número.", "2", "7A (45) y 7C (52) superan los 40."),
    ],
    [("Un afiche muestra un mapa del parque con una flecha roja «You are here» junto al lago. El texto dice: «The picnic area is 200 meters north of the lake.» (north = al norte, area = zona). ¿Hacia dónde debes ir desde el lago?", "Hacia el norte", "El texto ubica el área de picnic al norte del lago.")],
    [
        ("En Inglés de 7.º (OA 9, clase 4): ¿Qué es un pie de imagen?", "Una frase que explica la imagen", "Está bajo la imagen."),
        ("¿Para qué sirven las etiquetas de un diagrama?", "Para nombrar sus partes", "Identifican cada elemento."),
        ("¿Qué haces si el texto y la imagen se contradicen?", "Vuelvo a leer con cuidado", "Debo decidir qué dato es el correcto."),
    ],
    task("Observa este gráfico descrito: pasajeros de tres buses en un día. Bus 1: 30, Bus 2: 45, Bus 3: 25. Pie: «Bus 2 carried the most passengers.» (passengers = pasajeros, carried = llevó). Dibuja el gráfico en tu hoja y escribe si el pie es correcto, cuántos pasajeros hubo en total y cuántos más llevó el Bus 2 que el Bus 3.", "Es correcto: 45 es el mayor. Total: 100 pasajeros. El Bus 2 llevó 20 más que el Bus 3.", ["dibuja las tres barras", "comprueba el pie", "calcula el total y la diferencia"], ["hoja con el gráfico y los cálculos", "nota de quien revisó"], ["no comparar con el pie", "error de suma"], "Reconoce los cálculos correctos y revisa cómo se leen las barras."),
    "Dibuja un diagrama sencillo del recorrido del agua en una planta con flechas y tres etiquetas en inglés.",
    "Escribe un pie de imagen de una frase en inglés para una foto de tu curso.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA9, 5, MAT,
    "Aprenderé a responder preguntas sobre un texto citando la frase que respalda mi respuesta. Sirve para demostrar que lo que digo se basa en lo que el texto dice.",
    ["Sé ubicar información explícita y usar elementos visuales.", "Conozco because y so."],
    [
        "Citar una pista (cite a clue) significa copiar o señalar la frase del texto que respalda tu respuesta. Una respuesta completa tiene dos partes: la respuesta y la cita. Por ejemplo: Mr. Soto wears a thick coat because strong winds make the island very cold. La cita es la frase que explica por qué. Cita solo la parte necesaria, no el párrafo completo.",
        "Sigue estos pasos. Primero, lee la pregunta y subraya la palabra clave. Segundo, busca esa palabra o un sinónimo en el texto. Tercero, copia la frase que contiene la respuesta. Cuarto, escribe la respuesta con tus palabras y agrega la cita entre comillas. Si el texto no dice algo, no lo inventes: responde que el texto no lo dice.",
        "Distingue entre lo que el texto dice (explícito) y lo que tú supones. Si el texto dice que el farero enciende la luz a las siete, pero no dice dónde vive, no puedes afirmar nada sobre su casa. Las citas dan seriedad a tu respuesta y te ayudan a revisar si te equivocaste.",
    ],
    [("cite", "citar: señalar la frase del texto"), ("clue", "pista"), ("according to the text", "según el texto"), ("lighthouse", "faro"), ("keeper", "farero"), ("steps", "escalones")],
    [
        ("Responder con cita", LIGHT + " ¿A qué hora enciende la luz el farero? Responde y cita.", ["Busco turns on the light.", "La frase dice Every evening... at seven.", "Responde a las siete y cita la frase."], "A las siete; cita: turns on the light at seven"),
        ("Elegir la cita correcta", LIGHT + " ¿Qué frase respalda que los visitantes pueden subir los sábados?", ["Busco Visitors.", "Dice Visitors can climb the 60 steps on Saturdays.", "Esa es la cita."], "Visitors can climb the 60 steps on Saturdays"),
    ],
    [
        ("Dar la respuesta sin citar nada.", "No se sabe de dónde sale la respuesta.", "Agrega siempre la frase del texto."),
        ("Citar un párrafo entero.", "La pista queda perdida.", "Cita solo la frase necesaria."),
    ],
    [
        (LIGHT + " ¿A qué hora se enciende la luz?", "A las siete", "Dice turns on the light at seven."),
        (LIGHT + " ¿Cuántos escalones tiene el faro?", "60", "Dice the 60 steps."),
        (LIGHT + " ¿Qué día pueden subir los visitantes?", "Los sábados", "Dice on Saturdays."),
    ],
    [
        (LIGHT + " ¿Por qué usa un abrigo grueso el farero? a) porque los vientos fuertes hacen que la isla esté muy fría b) porque le gusta el color", "a) porque los vientos fuertes hacen que la isla esté muy fría", "Dice strong winds make the island very cold."),
        (LIGHT + " ¿Para qué sirve la luz del faro? a) para que los botes se alejen de las rocas b) para pescar de noche", "a) para que los botes se alejen de las rocas", "Dice Boats use the light to stay away from the rocks."),
        (LIGHT + " ¿Cuál es la cita para «Who turns on the light»? a) the keeper, Mr. Soto b) boats use the light", "a) the keeper, Mr. Soto", "Nombra a quien enciende la luz."),
    ],
    [
        (LIGHT + " ¿Dónde está el faro? Responde y cita.", "En Rock Island; cita: On Rock Island there is a small lighthouse", "Es la primera frase del texto."),
        arith(LIGHT + " Si 3 visitantes suben cada uno los 60 escalones, ¿cuántos escalones suben entre todos?", "3*60", "Se multiplica la cantidad de visitantes por los escalones.", " escalones"),
        (LIGHT + " Un lector dice que Mr. Soto vive en una ciudad. ¿Lo dice el texto? Responde sí o no.", "No", "El texto no habla de dónde vive."),
    ],
    [
        (LIGHT + " ¿Qué respuesta es mejor? a) Because strong winds make the island very cold. b) Because he likes coats.", "a) Because strong winds make the island very cold.", "Es la cita del texto."),
        ("¿Por qué conviene citar el texto? a) para mostrar de dónde sale mi respuesta b) para escribir más", "a) para mostrar de dónde sale mi respuesta", "La cita comprueba lo que digo."),
    ],
    [
        (LIGHT + " Responde con la cita: ¿qué hacen los botes con la luz?", "Boats use the light to stay away from the rocks", "Es la frase del texto que habla de los botes."),
        (LIGHT + " ¿Cuántas oraciones tiene el texto?", "5", "Se cuentan los puntos finales: son cinco oraciones."),
    ],
    [(LIGHT + " En una prueba te preguntan «When can visitors climb the lighthouse?». ¿Cuál es la mejor respuesta? a) On Saturdays, because the text says: Visitors can climb the 60 steps on Saturdays. b) I think on Sunday.", "a) On Saturdays, because the text says: Visitors can climb the 60 steps on Saturdays.", "Incluye la respuesta y la cita.")],
    [
        ("En Inglés de 7.º (OA 9, clase 5): ¿Qué dos partes tiene una buena respuesta?", "La respuesta y la cita", "La cita respalda la respuesta."),
        ("¿Qué haces si el texto no dice algo?", "Respondo que el texto no lo dice", "No debo inventar."),
        ("¿Cuánto del texto debo citar?", "Solo la frase necesaria", "Una cita corta es más clara."),
    ],
    task("Lee este texto: «The Library Garden. Behind the school library there is a small garden. Every Wednesday, the students of 7C water the plants and read there. In October, they planted 15 flowers. The librarian says the garden is quiet and good for reading.» (behind = detrás de, water = regar, planted = plantaron, librarian = bibliotecaria, quiet = tranquilo). Responde dos preguntas con cita: 1) ¿Quién riega las plantas? 2) ¿Cuántas flores plantaron?", "1) Los estudiantes de 7C; cita: the students of 7C water the plants. 2) 15; cita: they planted 15 flowers.", ["responde las dos preguntas", "cita una frase por respuesta", "usa solo el texto"], ["hoja con respuestas y citas", "nota de quien revisó"], ["no citar", "citar un párrafo completo"], "Reconoce las respuestas con cita y revisa que cada frase sea corta y exacta."),
    "Lee un texto breve en inglés del colegio y escribe una pregunta y su respuesta con cita.",
    "Escribe tres preguntas sobre el texto del faro y responde cada una con su cita.",
)
