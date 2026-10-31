"""Cuaderno del estudiante, 7.º básico Inglés (propuesta), EN07 OA 08 (presentación oral multimodal).

Los guiones de las presentaciones están escritos en cada enunciado, con pista en español. Los datos son sencillos y comprobables.
La pronunciación se practica leyendo en voz alta con una persona de la casa; la clase no depende de audio externo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_en7_a import lesson

OA8 = "EN07 OA 08"

# ---------------------------------------------------------------- clase 1: contenido y organización
FLAMINGO = "«Good morning. Today I will talk about flamingos. First, where they live: in salt lakes in northern Chile. Second, what they eat: tiny algae and small animals. This food makes their feathers pink. Finally, flamingos often stand on one leg to rest. In conclusion, flamingos are special birds. Thank you. Do you have questions?» (flamingos = flamencos, salt lakes = salares, northern = del norte, tiny = diminutos, algae = algas, feathers = plumas, leg = pata, rest = descansar)"
SKATE = "«Hello, everybody. My topic is my hobby: skateboarding. I started two years ago. First, I learned to keep my balance. Then I learned small jumps. My favorite thing is skating with friends at the park. My hobby is fun, and it keeps me active. Thanks for listening.» (hobby = pasatiempo, balance = equilibrio, jumps = saltos, keeps me active = me mantiene activo)"
COMPOST = "«Today I want to show you how to make a simple compost. First, collect fruit and vegetable waste. Second, add dry leaves. Next, mix them in a bin. Then wait two months. Finally, use the compost for plants. In conclusion, compost helps the garden and reduces waste. Do you have any questions?» (compost = compost, waste = restos, dry leaves = hojas secas, bin = recipiente, reduces = reduce)"

lesson(
    OA8, 1,
    "Los guiones de presentaciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a organizar una presentación oral con introducción, desarrollo y conclusión, y a mostrar que conozco el contenido con ideas coherentes. Sirve para presentar un tema ante el curso con orden y seguridad.",
    ["Sé usar first, second, next y finally.", "Conozco palabras como topic, hobby y conclusion."],
    [
        "Una presentación oral (oral presentation) tiene tres partes. La introducción (introduction) saluda, dice el tema y anuncia qué vas a contar: «Today I will talk about flamingos». El desarrollo (body) explica las ideas principales en orden, con first, second, next y finally. La conclusión (conclusion) cierra el tema con una frase como «In conclusion…» y agradece o invita a preguntar: «Thank you. Do you have questions?».",
        "Para mostrar que conoces el contenido (content knowledge), incluye datos exactos y comprobables, no solo opiniones. Cada idea debe estar relacionada con el tema. Una oración que no se relaciona, como hablar de fútbol dentro de una presentación sobre flamencos, se llama off-topic y debe eliminarse. También conviene explicar cada idea con una oración de apoyo: dato + ejemplo.",
        "Antes de presentar, haz un esquema (outline) con una palabra clave por idea: topic – where – food – feathers – conclusion. Organizar las ideas ayuda a ser coherente (coherent): cada parte conduce a la siguiente. Practica en voz alta y mide el tiempo. Una presentación clara no necesita muchas palabras, pero sí un orden lógico.",
    ],
    [("introduction", "introducción: saludo y tema"), ("body", "desarrollo: ideas principales"), ("conclusion", "conclusión: cierre"), ("off-topic", "fuera del tema"), ("outline", "esquema de ideas"), ("coherent", "coherente: las ideas se conectan")],
    [
        ("Identificar la introducción", "Lee: «Hello, everyone. Today I will talk about volcanoes. First, what a volcano is…» (volcanoes = volcanes). ¿Qué frase anuncia el tema?", ["Busco la frase con I will talk about.", "Anuncia el tema.", "Es la introducción."], "Today I will talk about volcanoes"),
        ("Detectar lo que sobra", "Una presentación sobre los pingüinos dice: «Penguins swim very well. They eat fish. My favorite color is blue.» (penguins = pingüinos). ¿Qué oración está fuera del tema?", ["Reviso que cada frase hable de pingüinos.", "My favorite color is blue no se relaciona.", "Es la oración off-topic."], "My favorite color is blue"),
    ],
    [
        ("Empezar a hablar sin decir cuál es el tema.", "El público no sabe de qué trata.", "Anuncia el tema en la introducción."),
        ("Terminar la presentación sin una conclusión.", "Queda inconclusa.", "Cierra con In conclusion y agradece."),
    ],
    [
        (FLAMINGO + " ¿Cuál es el tema? a) los flamencos b) los pingüinos", "a) los flamencos", "Dice Today I will talk about flamingos."),
        (SKATE + " ¿Cuál es el tema? a) el skate, el pasatiempo del hablante b) la cocina", "a) el skate, el pasatiempo del hablante", "Dice My topic is my hobby: skateboarding."),
        (COMPOST + " ¿Qué parte es «Do you have any questions?»? a) la conclusión b) la introducción", "a) la conclusión", "Cierra y abre un espacio para preguntas."),
    ],
    [
        (FLAMINGO + " ¿Dónde viven los flamencos según el hablante?", "En salares del norte de Chile", "Dice in salt lakes in northern Chile."),
        (SKATE + " ¿Cuándo empezó a patinar?", "Hace dos años", "Dice I started two years ago."),
        (COMPOST + " ¿Cuánto tiempo hay que esperar?", "Dos meses", "Dice then wait two months."),
    ],
    [
        (FLAMINGO + " ¿Qué palabra marca la segunda idea? a) second b) finally", "a) second", "Second introduce la segunda idea."),
        (SKATE + " Ordena el desarrollo. A) Aprendió saltos pequeños. B) Aprendió a mantener el equilibrio. C) Patina con amigos en el parque.", "B, A, C", "Sigue first, then y my favorite thing."),
        (COMPOST + " ¿Qué se hace después de agregar las hojas secas? a) mezclar b) esperar dos meses", "a) mezclar", "Next, mix them in a bin."),
    ],
    [
        (FLAMINGO + " Un compañero propone agregar «I like football». ¿Qué problema tendría? a) estaría fuera del tema b) sería muy largo", "a) estaría fuera del tema", "El tema son los flamencos."),
        (SKATE + " ¿Qué dato apoya la idea de que el skate lo mantiene activo? a) skating with friends at the park b) I started two years ago", "a) skating with friends at the park", "Patinar es una actividad física."),
    ],
    [
        (FLAMINGO + " El discurso tiene 3 ideas principales (dónde viven, qué comen y cómo descansan). Si cada idea dura 2 minutos, ¿cuánto dura el desarrollo?", "6", "Se multiplican las ideas por los minutos de cada una.", "3*2"),
        (COMPOST + " Ordena las partes del guion. A) Conclusión: In conclusion, compost helps the garden. B) Introducción: Today I want to show you how to make a simple compost. C) Desarrollo: First, collect fruit and vegetable waste.", "B, C, A", "Primero la introducción, luego el desarrollo y al final la conclusión."),
    ],
    [("Preparas una presentación sobre las abejas. Escribes: «Hello. Today I will talk about bees. First, bees make honey. Second, bees help plants. In conclusion, bees are important. Thank you.» ¿Falta alguna parte? Responde sí o no.", "No", "Tiene introducción, desarrollo y conclusión.")],
    [
        ("¿Cuáles son las tres partes de una presentación?", "Introducción, desarrollo y conclusión", "Organizan el contenido."),
        ("¿Qué frase introduce una conclusión?", "In conclusion", "Significa en conclusión."),
        ("¿Qué es una idea off-topic?", "Una idea fuera del tema", "No se relaciona con el tema."),
    ],
    task("Prepara una presentación de tres partes sobre este tema: «My favorite animal». Ideas ya listas que puedes usar: nombre del animal, dónde vive, qué come y por qué te gusta. Escribe: una introducción de dos frases con Today I will talk about…, un desarrollo con first, second y finally, y una conclusión con In conclusion y Thank you.", "Hello. Today I will talk about my favorite animal: the dog. First, dogs live with people. Second, dogs eat meat and dry food. Finally, I like dogs because they are loyal. In conclusion, dogs are good friends. Thank you.", ["incluye introducción, desarrollo y conclusión", "usa first, second y finally", "todas las ideas se relacionan con el tema"], ["hoja con el guion", "nota de la persona que escuchó"], ["no anunciar el tema", "agregar una idea fuera del tema"], "Reconoce lo que acertó y ayuda a la persona a ordenar las ideas con un esquema de palabras clave."),
    "Lee en voz alta la presentación de los flamencos a una persona de tu casa y mide cuánto dura.",
    "Cambia el tema de la presentación de los flamencos por otro animal y reescribe la introducción.",
)

# ---------------------------------------------------------------- clase 2: funciones del lenguaje y vocabulario
SCHOOL = "«Hello. My presentation is about my school. It is a big school with 600 students. The library is on the second floor, and its books are old but interesting. Our teachers are very kind. Every Friday, we have a short meeting in the yard. Yesterday, we planted two trees because the yard has no shade. If the trees grow, we will have a green yard.» (kind = amables, meeting = reunión, planted = plantamos, shade = sombra)"
SPACE = "«Today I will talk about the planets. The solar system has eight planets. Mercury is the closest to the Sun, and Neptune is the farthest. Earth is our home, and it has water. Jupiter is the biggest planet. Venus is very hot. If you visit Mars, you will see red rocks.» (planets = planetas, solar system = sistema solar, closest = más cercano, farthest = más lejano, home = hogar, rocks = rocas)"
MENU = "«I will present the school menu for next week. On Monday, we eat rice and chicken. On Tuesday, there is vegetable soup because it is a cold day. Every Wednesday we have fruit. On Thursday, the cook prepares pasta, and on Friday we usually eat fish. The students' favorite day is Thursday.» (menu = menú, chicken = pollo, soup = sopa, vegetable = verdura, cook = cocinera, fish = pescado, favorite = favorito)"

lesson(
    OA8, 2,
    "Los guiones de presentaciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a usar en una presentación las funciones del lenguaje (posesión, tiempo, causa, condición) y el vocabulario temático de mi tema. Sirve para hablar con precisión y variedad al presentar.",
    ["Sé usar 's para la posesión y because para la causa.", "Conozco palabras de lugares y de comida."],
    [
        "Una presentación necesita vocabulario temático (thematic vocabulary): palabras propias del tema. En una presentación sobre el sistema solar, las palabras temáticas son planet, Sun, closest, farthest y solar system. Si presentas el menú del colegio, usas rice, soup, pasta y fish. Antes de hablar, haz una lista de diez palabras del tema, con la pronunciación y el significado.",
        "También usa funciones del lenguaje. Para mostrar posesión: the students' favorite day (el día favorito de los estudiantes), Earth is our home. Para decir el tiempo: on Monday, every Wednesday, yesterday. Para explicar causa: because it is a cold day. Para condición: if the trees grow, we will have a green yard. Cada función hace tu presentación más clara y variada.",
        "Evita repetir siempre las mismas palabras. En lugar de decir «big» muchas veces, puedes usar biggest, large o huge, si conoces su significado. Usa palabras de uso frecuente y expresiones de uso común, como every Friday o in conclusion. Revisa tu guion con una lista: ¿hay vocabulario temático?, ¿hay una causa con because?, ¿hay una condición con if? Esa lista te ayuda a mejorar tu mensaje.",
    ],
    [("thematic vocabulary", "vocabulario propio del tema"), ("possession", "posesión: 's, our, their"), ("time expression", "expresión de tiempo: every Friday, yesterday"), ("because", "porque: causa"), ("if", "si: condición"), ("biggest / closest", "el más grande / el más cercano")],
    [
        ("Vocabulario temático", "Clasifica las palabras para una presentación sobre frutas: apple, orange, soup, banana. ¿Cuál no es del tema?", ["Reviso cuáles son frutas.", "Apple, orange y banana son frutas.", "Soup no es una fruta."], "soup"),
        ("Función de causa", "Completa: «We eat soup ___ it is cold.» Elige because o but.", ["Necesito explicar la razón.", "Because introduce la causa.", "Queda because."], "because"),
    ],
    [
        ("Usar siempre «big» y no variar el vocabulario.", "Se empobrece el mensaje.", "Usa palabras como biggest, large o huge si las conoces."),
        ("Olvidar la causa o la condición.", "El discurso solo enumera datos.", "Agrega because e if para explicar y relacionar ideas."),
    ],
    [
        (SCHOOL + " ¿Dónde está la biblioteca? a) en el segundo piso b) en el patio", "a) en el segundo piso", "Dice on the second floor."),
        (SPACE + " ¿Cuál es el planeta más grande? a) Júpiter b) Mercurio", "a) Júpiter", "Dice Jupiter is the biggest planet."),
        (MENU + " ¿Qué se come los miércoles? a) fruta b) pasta", "a) fruta", "Dice Every Wednesday we have fruit."),
    ],
    [
        (SCHOOL + " ¿Por qué plantaron dos árboles?", "Porque el patio no tiene sombra", "Dice because the yard has no shade."),
        (SPACE + " ¿Qué planeta está más cerca del Sol?", "Mercurio", "Dice Mercury is the closest to the Sun."),
        (MENU + " ¿Por qué hay sopa de verduras el martes?", "Porque es un día frío", "Dice because it is a cold day."),
    ],
    [
        (SCHOOL + " ¿Qué función expresa «If the trees grow, we will have a green yard»? a) condición b) posesión", "a) condición", "Usa if y will."),
        (SPACE + " ¿Qué función expresa «Earth is our home»? a) posesión b) tiempo", "a) posesión", "Our muestra pertenencia."),
        (MENU + " ¿Qué expresión de tiempo aparece en «Every Wednesday»? a) frecuencia b) causa", "a) frecuencia", "Every indica cada cuánto ocurre."),
    ],
    [
        (SPACE + " ¿Qué palabras son vocabulario temático del texto? a) planets, Sun, closest b) happy, pencil, chair", "a) planets, Sun, closest", "Pertenecen al tema del sistema solar."),
        (MENU + " Un compañero dice «The students favorite day is Thursday» sin apóstrofo. ¿Cómo se corrige? a) The students' favorite day b) The student favorite day", "a) The students' favorite day", "Plural regular: apóstrofo después de la s."),
    ],
    [
        (SCHOOL + " Si hay 600 estudiantes y cada curso tiene 30, ¿cuántos cursos hay?", "20", "Se divide el total entre el número de estudiantes por curso.", "600//30"),
        (SPACE + " Si en tu presentación hablas de 2 planetas por diapositiva y hay 8 planetas, ¿cuántas diapositivas necesitas?", "4", "Se reparten ocho planetas de dos en dos.", "8//2"),
    ],
    [("Preparas una presentación sobre el clima en Chile. ¿Qué vocabulario temático usarías? a) rainy, sunny, temperature b) pasta, soup, rice", "a) rainy, sunny, temperature", "Son palabras del tema del clima.")],
    [
        ("En una presentación, ¿qué es el thematic vocabulary?", "Palabras propias del tema", "Hacen precisa la presentación."),
        ("En un guion de presentación, ¿qué palabra introduce una condición?", "if", "Se usa con will en el resultado."),
        ("¿Cómo se escribe «los días favoritos de los estudiantes»?", "The students' favorite days", "Se usa el apóstrofo después de la s."),
    ],
    task("Prepara una presentación de cuatro frases sobre tu colegio o tu curso con esta lista de palabras ya dada: library, teachers, students, Friday, yard. Incluye una posesión (with 's), una causa con because y una condición con if. Ejemplo de inicio: «Hello. Today I will talk about my class.»", "Hello. Today I will talk about my class. The students' favorite place is the yard because it is big. Every Friday, we play there. If it rains, we will stay in the library.", ["usa al menos cuatro palabras de la lista", "incluye posesión, causa y condición", "las frases se relacionan con el tema"], ["hoja con cuatro frases"], ["escribir la condición con will después de if", "olvidar el apóstrofo"], "Reconoce lo que acertó y revisa con la persona que cada función tenga su palabra (’s, because, if)."),
    "Relee la presentación del menú y subraya con tres colores las palabras de tiempo, causa y posesión.",
    "Escribe una lista de diez palabras de un tema que te guste, con su significado.",
)

# ---------------------------------------------------------------- clase 3: sonidos /z/, /s/ y /h/
ZOO = "Trabalenguas original (un adulto lo lee despacio): «Sam sees seven zebras at the zoo. The zebras are sad, but the zookeeper has a big blue bus.» (zebras = cebras, zookeeper = cuidador del zoológico, sad = triste)"
HOUSE = "Presentación breve para leer en voz alta: «Hello, everyone. My house is in a hot city. Every hour, my hamster runs on his wheel. He is very happy and honest about his hunger.» (hamster = hámster, wheel = rueda, hunger = hambre)"
PLURAL = "Lista de palabras para leer en voz alta: dogs, cats, bags, books, cups, pens."

lesson(
    OA8, 3,
    "Los trabalenguas y las listas de palabras escritos en cada ejercicio y lápiz. Una persona de tu casa puede escuchar tu lectura en voz alta.",
    "Aprenderé a usar de forma apropiada los sonidos /s/ y /z/ (sad y zoo) y el sonido inicial /h/ (hot y hour). Sirve para que mi presentación sea más clara para quien me escucha.",
    ["Sé que las letras s, z y h existen en español.", "Conozco palabras como zoo, sun, hot y hour."],
    [
        "El sonido /s/ es como la s de «sad» o «sun»: el aire sale sin vibración. El sonido /z/ es como la z inglesa de «zoo»: el aire sale con vibración. Para sentirlo, pon la mano en tu garganta: con /z/ vibra y con /s/ no vibra. En español existe la s, pero no la z con vibración, por eso hay que practicarla. Pares como sip y zip o ice y eyes cambian de significado según el sonido.",
        "La letra s puede sonar /s/ o /z/. En los plurales, suena /z/ después de sonidos con vibración (dogs, bags, pens) y /s/ después de sonidos sin vibración (cats, books, cups). En palabras como buses, el final suena como /iz/. La letra z suena /z/ en la mayoría de las palabras que verás aquí: zoo, zebra, zero.",
        "El sonido /h/ al inicio se pronuncia soplando aire, como en hot, house o hamster. En español la h es muda, pero en inglés la h inicial suena, por eso se dice «hot» con soplo. Atención: hay palabras con h muda, como hour y honest, que se pronuncian como «our» y «onest». Para practicar, repite el trabalenguas despacio, luego más rápido, y graba o pide a alguien que te escuche.",
    ],
    [("/s/", "sonido sin vibración: sad, sun"), ("/z/", "sonido con vibración: zoo, dogs"), ("/h/", "soplo inicial: hot, house"), ("silent h", "h muda: hour, honest"), ("tongue twister", "trabalenguas"), ("plural -s", "terminación de plural")],
    [
        ("Clasificar /s/ y /z/", "Clasifica las palabras sad, zoo, zero, sun. ¿Cuáles empiezan con /z/?", ["Sad y sun empiezan con s: /s/.", "Zoo y zero empiezan con z: /z/.", "La z siempre suena /z/."], "zoo y zero"),
        ("Sonido /h/", "Clasifica las palabras hot, hour, house, honest. ¿Cuáles tienen h muda?", ["Hot y house se pronuncian con soplo.", "Hour y honest empiezan sin soplo.", "Tienen h muda."], "hour y honest"),
    ],
    [
        ("Decir «ice» con vibración y que suene como «eyes».", "Se confunden /s/ y /z/.", "Ice termina en /s/ y eyes termina en /z/."),
        ("Pronunciar la h de «hour».", "Se aplica la h inicial a una palabra con h muda.", "Hour se dice como our."),
    ],
    [
        ("¿Qué palabra empieza con /z/? a) zebra b) sad", "a) zebra", "Zebra empieza con el sonido /z/."),
        ("¿Qué palabra tiene h muda? a) hour b) hot", "a) hour", "En hour no se pronuncia la h."),
        (ZOO + " ¿Qué animal aparece en el trabalenguas? a) cebras b) caballos", "a) cebras", "Dice seven zebras."),
    ],
    [
        (PLURAL + " ¿Qué plural termina con /z/? a) dogs b) cats", "a) dogs", "Dogs termina después de g, un sonido con voz."),
        (PLURAL + " ¿Qué plural termina con /s/? a) books b) bags", "a) books", "Books termina después de k, un sonido sin voz."),
        (HOUSE + " ¿Qué palabra de la lectura empieza con soplo /h/? a) hamster b) hour", "a) hamster", "Hamster se pronuncia con /h/."),
    ],
    [
        (ZOO + " ¿Qué palabra tiene el sonido /z/ al inicio? a) zebras b) sees", "a) zebras", "Zebras empieza con z, que suena /z/."),
        (HOUSE + " En la lectura, ¿qué palabra tiene h muda? a) honest b) hunger", "a) honest", "Honest se pronuncia como onest."),
        ("¿Cómo se pronuncia el final de «buses»? a) /iz/ b) /s/", "a) /iz/", "Después de s, el plural suena como iz."),
    ],
    [
        ("¿Cuál par cambia de significado por el sonido /s/ y /z/? a) sip y zip b) hot y hat", "a) sip y zip", "La diferencia es /s/ contra /z/."),
        (HOUSE + " Una compañera dice «hour» con /h/. ¿Qué corrección haces? a) se dice sin /h/, como our b) se dice con más soplo", "a) se dice sin /h/, como our", "Hour tiene h muda."),
    ],
    [
        ("Cuenta cuántas palabras de la lista tienen sonido /z/: dogs, cats, bags, books, cups, pens.", "3", "Dogs, bags y pens terminan con /z/."),
        ("Cuenta cuántas palabras tienen h inicial que se pronuncia: hot, hour, house, honest, hand.", "3", "Hot, house y hand tienen /h/."),
    ],
    [("Quieres presentar el tema «My zoo trip». ¿Qué palabras del tema practicarías con /z/? a) zoo y zebra b) sun y sad", "a) zoo y zebra", "Empiezan con el sonido /z/.")],
    [
        ("¿Cómo sientes la diferencia entre /s/ y /z/?", "Con /z/ vibra la garganta", "Con /s/ no vibra."),
        ("¿Cómo se pronuncia «honest»?", "Sin /h/, como onest", "Tiene h muda."),
        ("¿Qué plural suena /s/? ", "cats", "Termina después de t, un sonido sin voz."),
    ],
    task("Practica con una persona de tu casa. Lee en voz alta, despacio y luego rápido, este trabalenguas original: «Sue sees six sad zebras in the zoo. Henry has a hot hat, and he holds it for an hour.» (sees = ve, six = seis, holds = sostiene). Después escribe: dos palabras con /z/, dos con /s/ y dos con /h/ que viste en el trabalenguas. Marca la palabra con h muda.", "Con /z/: zebras y zoo. Con /s/: Sue y sad. Con /h/: Henry y hot. H muda: hour.", ["clasifica correctamente las palabras", "marca hour como h muda", "lee el trabalenguas con apoyo del adulto"], ["hoja con la clasificación", "nota de quien escuchó"], ["pronunciar la h de hour", "decir que zoo empieza con /s/"], "Reconoce lo que acertó y practica con la persona sentir la vibración en la garganta con /z/."),
    "Repite tres veces el trabalenguas «Sam sees seven zebras at the zoo» y pide a alguien que cuente cuántas veces dijiste /z/.",
    "Escribe cinco palabras del colegio que terminen en -s y marca si suenan /s/ o /z/.",
)

# ---------------------------------------------------------------- clase 4: recursos multimodales
SLIDEA = "Diapositiva A de ejemplo (título «Our Recycling Day»): una imagen grande de tres tarros de colores y tres frases cortas: «Blue: paper. Yellow: plastic. Green: glass.» Total: 6 palabras sin contar el título. (paper = papel, plastic = plástico, glass = vidrio)"
SLIDEB = "Diapositiva B de ejemplo (título «Our Recycling Day»): un párrafo de 85 palabras en letra muy pequeña, sin imágenes."
GESTURE = "Cuando un presentador dice «This plant is very tall», estira el brazo hacia arriba. Cuando dice «The pot is small», junta las manos para mostrar un tamaño pequeño."

lesson(
    OA8, 4,
    "Las descripciones de diapositivas y gestos escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a elegir recursos multimodales (imágenes, diapositivas, gestos y objetos) que refuercen el mensaje de una presentación de forma creativa. Sirve para que mi mensaje se entienda mejor y sea más atractivo.",
    ["Sé organizar una presentación en tres partes.", "Conozco palabras como slide, picture y gesture."],
    [
        "Multimodal significa que el mensaje usa más de un modo para comunicarse: palabras, imágenes, gestos, sonidos, objetos y movimiento. Los recursos multimodales (multimodal resources) apoyan lo que dices; no lo reemplazan. Una diapositiva (slide) con una imagen clara ayuda a recordar la idea. Un gesto, como mostrar «alto» con el brazo, ayuda a entender la palabra tall.",
        "Para que una diapositiva sea efectiva sigue estas reglas de esta clase: una idea por diapositiva, no más de 15 palabras, letra grande y una imagen que se relacione con la idea. Evita copiar un párrafo largo: el público lee en vez de escucharte. Las palabras de la diapositiva son pistas; la explicación la entregas tú hablando. Elige colores con buen contraste, por ejemplo, letras oscuras sobre fondo claro.",
        "Los recursos también deben ser creativos. Puedes mostrar un objeto real, hacer un dibujo, usar una tabla o hacer un gesto. Pregúntate: ¿qué recurso refuerza mejor este mensaje? Si explicas una secuencia de pasos, una tabla o una línea de tiempo ayuda. Si explicas un animal, una imagen sirve. Practica con tus recursos antes de presentar.",
    ],
    [("multimodal", "con más de un modo: palabras, imagen, gesto"), ("slide", "diapositiva"), ("gesture", "gesto"), ("contrast", "contraste: diferencia entre letra y fondo"), ("resource", "recurso que apoya el mensaje"), ("creative", "creativo")],
    [
        ("Elegir un recurso", "Vas a explicar cómo es un cactus. ¿Qué recurso refuerza mejor tu mensaje: una imagen de un cactus o una tabla de números?", ["Quiero que vean cómo es.", "La imagen muestra su forma.", "La tabla de números no ayuda."], "Una imagen de un cactus"),
        ("Contraste", "¿Qué combinación se lee mejor: letras amarillas sobre fondo blanco o letras negras sobre fondo blanco?", ["El contraste debe ser fuerte.", "El amarillo sobre blanco es difícil de leer.", "El negro sobre blanco es claro."], "Letras negras sobre fondo blanco"),
    ],
    [
        ("Pegar un párrafo completo en la diapositiva y leerlo.", "El público lee en vez de escuchar.", "Escribe palabras clave y explica con tus palabras."),
        ("Mostrar una imagen que no se relaciona con la idea.", "Distrae al público.", "Elige imágenes que refuercen el mensaje."),
    ],
    [
        (SLIDEA + " ¿Cumple la regla de las 15 palabras? a) sí b) no", "a) sí", "Tiene 6 palabras."),
        (SLIDEB + " ¿Cumple la regla de una idea y pocas palabras? a) no b) sí", "a) no", "Tiene 85 palabras, mucho más de 15."),
        (GESTURE + " ¿Qué refuerza el gesto de estirar el brazo hacia arriba? a) la palabra tall b) la palabra small", "a) la palabra tall", "Muestra una altura grande."),
    ],
    [
        (SLIDEA + " ¿Qué imagen apoya el tema? a) tres tarros de colores b) un partido de fútbol", "a) tres tarros de colores", "La imagen se relaciona con el reciclaje."),
        (SLIDEB + " ¿Qué problema tiene esta diapositiva?", "Tiene demasiado texto y ninguna imagen", "Son 85 palabras en letra pequeña sin apoyo visual."),
        (GESTURE + " ¿Qué refuerza el gesto de juntar las manos? a) la palabra small b) la palabra tall", "a) la palabra small", "Muestra un tamaño pequeño."),
    ],
    [
        ("Quieres explicar cuatro pasos para plantar una semilla. ¿Qué recurso conviene? a) una línea de tiempo con dibujos b) una sola foto de un árbol", "a) una línea de tiempo con dibujos", "Muestra el orden de los pasos."),
        ("Quieres mostrar cuántos estudiantes eligen cada fruta. ¿Qué recurso conviene? a) un gráfico de barras b) un poema", "a) un gráfico de barras", "Permite comparar cantidades de un vistazo."),
        ("Quieres que el público entienda la palabra «round». ¿Qué gesto o recurso sirve? a) dibujar un círculo en el aire b) cruzar los brazos", "a) dibujar un círculo en el aire", "El gesto muestra la forma redonda."),
    ],
    [
        (SLIDEB + " Para mejorarla, ¿cuál es el mejor cambio? a) reducir a pocas palabras clave y agregar una imagen b) aumentar el tamaño del párrafo", "a) reducir a pocas palabras clave y agregar una imagen", "Cumple las reglas de la clase."),
        ("Una diapositiva tiene 40 palabras. Según la regla de 15 palabras, ¿cuántas palabras hay que quitar como mínimo?", "25", "Se resta el máximo permitido al total.", "40-15"),
    ],
    [
        ("Una presentación tiene 6 diapositivas y cada una cumple la regla de 15 palabras como máximo. ¿Cuál es el máximo de palabras en total?", "90", "Seis diapositivas por quince palabras.", "6*15"),
        ("Elige la mejor combinación para presentar a los flamencos. a) imagen de un flamenco, palabra clave «pink» y un gesto de pararse en una pierna b) párrafo largo sin imágenes", "a) imagen de un flamenco, palabra clave «pink» y un gesto de pararse en una pierna", "Combina imagen, palabras y gesto."),
    ],
    [("Un compañero dice: «Mi diapositiva tiene una foto de un perro, pero mi tema es el reciclaje». ¿Qué le sugieres? a) cambiar la foto por una que muestre reciclaje b) agregar más fotos de perros", "a) cambiar la foto por una que muestre reciclaje", "La imagen debe reforzar el tema.")],
    [
        ("¿Qué significa multimodal?", "Que usa más de un modo para comunicar", "Palabras, imágenes y gestos."),
        ("¿Cuántas palabras como máximo debe tener una diapositiva en esta clase?", "15", "Es la regla de la clase."),
        ("¿Qué se debe hacer con un párrafo largo?", "Convertirlo en palabras clave", "Así el público te escucha."),
    ],
    task("Diseña tres diapositivas de ejemplo para explicar «A healthy breakfast» con esta lista de ideas ya dada: 1) frutas, 2) leche o agua, 3) pan integral. Para cada una escribe el título, una imagen que dibujarías y no más de 10 palabras. Después describe un gesto que usarías al hablar.", "Diapositiva 1: Fruit — dibujo de una manzana y un plátano — «Fruit gives vitamins». Diapositiva 2: Milk or water — dibujo de un vaso — «Drink every morning». Diapositiva 3: Bread — dibujo de un pan — «Whole-grain bread gives energy». Gesto: abrir las manos para mostrar el plato.", ["diseña tres diapositivas con título e imagen", "cada texto tiene 10 palabras o menos", "propone un gesto coherente con el mensaje"], ["hoja con tres diapositivas"], ["escribir más de 10 palabras por diapositiva", "elegir imágenes que no se relacionan con el desayuno"], "Reconoce lo que acertó y ayuda a la persona a contar las palabras de cada diapositiva."),
    "Dibuja la diapositiva A con la imagen de los tarros y practica explicarla en voz alta con un gesto.",
    "Cambia el tema de las diapositivas a «My city» y propón tres imágenes.",
)

# ---------------------------------------------------------------- clase 5: audiencia, contexto y propósito
TO_YOUNG = "Guion 1: «Hello, friends! Today we will talk about fruit. Look! This is an apple. It is red and round. Do you like apples?» (round = redonda, friends = amigos)"
TO_DIRECTOR = "Guion 2: «Good morning, Madam Director. I would like to present a proposal about recycling in our school. First, we need three bins. Second, we will have a Green Team. We believe this will help the environment.» (proposal = propuesta, environment = medio ambiente)"
TO_CLASS = "Guion 3: «Hi, everybody! Today I will talk about my favorite band. They play pop music and they are awesome! Listen to this short song. Do you know it?» (band = banda, awesome = genial)"

lesson(
    OA8, 5,
    "Las descripciones de situaciones y los textos de presentaciones escritos en cada ejercicio y lápiz.",
    "Aprenderé a tener conciencia de la audiencia, el contexto y el propósito al presentar: a quién le hablo, dónde estoy y para qué hablo. Sirve para adaptar mi lenguaje, mi tono y mis recursos y lograr que mi mensaje llegue.",
    ["Sé organizar una presentación con introducción, desarrollo y conclusión.", "Conozco palabras como friends, director y proposal."],
    [
        "La audiencia (audience) es el público que te escucha. El contexto (context) es la situación: el lugar, el momento y el tiempo que tienes. El propósito (purpose) es para qué presentas: informar, persuadir (convencer) o entretener. Antes de hablar, responde tres preguntas: ¿a quién le hablo?, ¿dónde? y ¿para qué? Las respuestas cambian lo que dices.",
        "Adapta tu lenguaje a la audiencia. Con niños pequeños, usa frases cortas, palabras simples, gestos y preguntas: «Do you like apples?». Con la directora o con un jurado, usa un tono formal (formal): «Good morning, Madam Director. I would like to present…». Con tus compañeros puedes usar un tono más cercano (informal): «Hi, everybody!». El propósito también orienta: para persuadir, da razones con because; para informar, da datos.",
        "También adapta los recursos y el tiempo. Si hablas en un patio con ruido, usa imágenes grandes y voz fuerte. Si tienes tres minutos, selecciona tres ideas. Si el público ya sabe el tema, agrega un dato nuevo. Una presentación efectiva es la que el público entiende y recuerda. Observa su reacción y ajusta el ritmo.",
    ],
    [("audience", "público que escucha"), ("context", "situación: lugar y tiempo"), ("purpose", "para qué presento: informar, persuadir, entretener"), ("formal / informal", "tono serio / tono cercano"), ("persuade", "convencer"), ("proposal", "propuesta")],
    [
        ("Identificar la audiencia", TO_YOUNG + " ¿Quién es la audiencia?", ["Veo la palabra friends y frases muy simples.", "Pregunta Do you like apples? como a niños pequeños.", "La audiencia son niños pequeños."], "Niños pequeños"),
        ("Tono formal", "Elige el saludo para una directora: «Good morning, Madam Director» o «Hey, what's up?».", ["La directora pide respeto.", "El primero es formal.", "El segundo es muy informal."], "Good morning, Madam Director"),
    ],
    [
        ("Usar el mismo lenguaje con todas las audiencias.", "No se adapta el mensaje.", "Cambia el tono, el vocabulario y los recursos según el público."),
        ("Presentar sin pensar en el tiempo disponible.", "No se selecciona lo esencial.", "Prepara solo las ideas que caben en el tiempo."),
    ],
    [
        (TO_DIRECTOR + " ¿Qué tono usa? a) formal b) informal", "a) formal", "Usa Madam Director y I would like to present."),
        (TO_CLASS + " ¿Cuál es el propósito? a) entretener y compartir un gusto b) pedir un permiso formal", "a) entretener y compartir un gusto", "Habla de su banda favorita y pone una canción."),
        (TO_YOUNG + " ¿Qué recurso usa para atraer a niños pequeños? a) preguntas y objetos b) párrafos largos", "a) preguntas y objetos", "Pregunta Do you like apples? y muestra una manzana."),
    ],
    [
        (TO_DIRECTOR + " ¿Qué propone la presentación?", "Reciclar en el colegio con tres tarros y un equipo verde", "Dice three bins y a Green Team."),
        (TO_CLASS + " ¿Qué saludo informal usa? a) «Hi, everybody!» b) «Good morning, Madam Director.»", "a) Hi, everybody!", "Es el saludo cercano para sus compañeros."),
        (TO_YOUNG + " ¿Cómo es la manzana? a) roja y redonda b) verde y cuadrada", "a) roja y redonda", "Dice red and round."),
    ],
    [
        ("Vas a convencer al director de comprar más libros. ¿Cuál es tu propósito? a) persuadir b) entretener", "a) persuadir", "Quieres que acepte una propuesta."),
        ("Vas a mostrar un trabajo de ciencias a niños de primero. ¿Qué cambias? a) usas frases cortas y dibujos grandes b) usas palabras técnicas largas", "a) usas frases cortas y dibujos grandes", "El lenguaje debe ser simple."),
        ("Tienes 3 minutos para presentar. ¿Qué haces? a) eliges tres ideas principales b) preparas diez ideas", "a) eliges tres ideas principales", "Se adapta al tiempo disponible."),
    ],
    [
        ("Un compañero usa «Hey guys!» para saludar a la directora. ¿Qué adaptación necesita? a) un saludo formal b) más gestos", "a) un saludo formal", "La audiencia es una autoridad."),
        (TO_DIRECTOR + " Para persuadir, ¿qué palabra de las siguientes ayuda a dar una razón? a) because b) hello", "a) because", "Because introduce la razón."),
    ],
    [
        ("Hay 5 estudiantes y cada uno presenta durante 3 minutos. ¿Cuántos minutos dura la sesión?", "15", "Se multiplica el número de estudiantes por los minutos de cada uno.", "5*3"),
        ("Una sesión dura 20 minutos y las presentaciones ocupan 15. ¿Cuántos minutos quedan para preguntas?", "5", "Se resta el tiempo usado.", "20-15"),
    ],
    [("Presentarás un resumen de un libro al curso para convencerlos de leerlo. ¿Qué haces? a) das razones y usas un tono entusiasta b) lees todo el libro", "a) das razones y usas un tono entusiasta", "Tu propósito es persuadir.")],
    [
        ("¿Qué tres preguntas ayudan a adaptar una presentación?", "¿A quién? ¿Dónde? ¿Para qué?", "Son audiencia, contexto y propósito."),
        ("¿Qué tono usas con una autoridad?", "Formal", "El tono formal muestra respeto."),
        ("¿Qué propósitos puede tener una presentación?", "Informar, persuadir o entretener", "Orientan lo que dices."),
    ],
    task("Elige una de estas situaciones: A) presentar tu mascota a niños de 6 años, B) pedir a la directora un nuevo recreo de lectura. Escribe un guion de cuatro frases en inglés que se adapte a la audiencia, con un saludo apropiado, una razón con because y un cierre. Lista de apoyo: «Hello, friends!», «Good morning, Madam Director», «because», «Thank you».", "B) Good morning, Madam Director. I would like to ask for a reading break. Reading helps us concentrate because it is quiet. Thank you.", ["elige un saludo adecuado a la audiencia", "incluye una razón con because", "mantiene el tono formal o infantil según la situación"], ["hoja con guion de cuatro frases"], ["usar un saludo informal con la directora", "no incluir razón"], "Reconoce lo que acertó y revisa con la persona si el tono coincide con la audiencia."),
    "Relee los tres guiones y subraya con un color las palabras formales y con otro las informales.",
    "Cambia la presentación de los flamencos para niños de 6 años.",
)
