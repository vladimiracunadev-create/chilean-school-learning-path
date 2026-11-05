"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 14: proceso de escritura independiente en distintos géneros.

El estudiante trabaja con borradores, listas de criterios, entradas de diccionario en línea y pantallas de procesador de textos
descritas en el enunciado. Textos originales, inglés americano. Los títulos de clase del plan son genéricos; aquí se aplican a
planificar según un criterio, redactar, revisar contenido y organización, editar con diccionario en línea y publicar con
procesador de textos.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 14"

# ------------------------------------------------------------------ clase 1: géneros, criterio y organizar ideas
CR = "Criterio de evaluación (de ejemplo) para un folleto del club de teatro: 1) Título claro. 2) Entre 60 y 80 palabras. 3) Tres datos: día, hora y lugar. 4) Al menos dos conectores. 5) Una imagen con pie de foto."
BS = "Lluvia de ideas para un folleto de un taller de fotografía: photos, Saturday, 3 p.m., library, free, cameras, tips, beginners, bring your phone, snacks."
OU = "Esquema (outline) del folleto: Title: Photo Workshop. Introduction: what it is. Body 1: day, time, place. Body 2: what to bring. Closing: invitation."
GN = "Géneros: 1) diario personal (journal), 2) instrucciones, 3) folleto, 4) biografía, 5) carta, 6) resumen, 7) poema o canción, 8) cuento, 9) correo electrónico, 10) artículo, 11) rima, 12) descripción."

lesson(
    OA, 1, MAT_R,
    "Aprenderé a planificar un texto según un criterio de evaluación: elegir el género, organizar las ideas con lluvia de ideas y esquema, y decidir el propósito y la audiencia. Sirve para escribir con orden y de forma independiente.",
    ["Sé escribir oraciones y párrafos simples.", "Sé reconocer el propósito de un texto."],
    [
        "El proceso de escritura (writing process) tiene cinco pasos: organizar ideas (plan), redactar (draft), revisar (revise), editar (edit) y publicar (publish). Antes del primer paso, lee el criterio de evaluación (criteria): es la lista de lo que tu texto debe cumplir, como el título, el largo, los datos y los conectores. Subraya cada punto y conviértelo en una tarea.",
        "Elige el género según el propósito. Un diario personal (journal) cuenta experiencias y sentimientos; las instrucciones (instructions) enseñan pasos; un folleto (brochure) informa o invita; una biografía cuenta la vida de alguien; una carta se escribe a una persona; un resumen explica lo esencial de otro texto; un poema o canción expresa ideas con ritmo o rima; un cuento narra hechos con personajes; un correo electrónico (email) es un mensaje breve con asunto, saludo y despedida; un artículo informa sobre un tema; una rima juega con palabras que suenan igual al final; una descripción dice cómo es algo con detalles. Cada género tiene su estructura: el folleto, título, datos e invitación; las instrucciones, pasos numerados.",
        "Para organizar ideas, haz primero una lluvia de ideas (brainstorm): escribe todo lo que se te ocurra sin juzgar. Luego agrupa, elimina lo que no sirve y ordénalo en un esquema (outline): título, introducción, desarrollo y cierre. Con ese esquema tendrás tu mapa para redactar.",
    ],
    [("writing process", "proceso de escritura"), ("criteria", "criterios de evaluación"), ("brainstorm", "lluvia de ideas"), ("outline", "esquema"), ("genre", "género"), ("audience", "audiencia")],
    [
        ("Convertir el criterio en tareas", CR + " ¿Qué debes incluir en el folleto?", ["Subrayo cada número del criterio.", "Título, 60 a 80 palabras, día, hora y lugar, dos conectores, una imagen.", "Cada punto es una tarea."], "Título, entre 60 y 80 palabras, día, hora y lugar, dos conectores y una imagen con pie de foto"),
        ("De la lluvia de ideas al esquema", BS + " ¿Qué ideas pertenecen a Body 1 (day, time, place)?", ["Busco los datos de lugar y tiempo.", "Saturday, 3 p.m. y library.", "Esas van en Body 1."], "Saturday, 3 p.m. y library"),
    ],
    [
        ("Empezar a escribir sin leer el criterio.", "Puedes olvidar un punto que se evalúa.", "Léelo, subráyalo y conviértelo en tareas."),
        ("Poner en el esquema ideas que no sirven.", "El texto pierde foco.", "Elimina lo que no se relacione con el propósito."),
    ],
    [
        mr(CR, "¿Cuántos datos de información exige el criterio?", "Tres", ["Dos", "Cinco"], "El punto 3 pide día, hora y lugar."),
        mr(GN, "¿Qué género enseña pasos?", "Instrucciones", ["Diario personal", "Poema"], "Las instrucciones se organizan en pasos."),
        mr(OU, "¿Qué va en el cierre del folleto?", "Una invitación", ["Los datos de la hora", "El título"], "El esquema dice Closing: invitation."),
    ],
    [
        mr(BS, "¿Qué idea de la lluvia de ideas pertenece a lo que se debe llevar?", "bring your phone", ["Saturday at 3 p.m.", "free for everyone"], "Es parte de lo que llevar."),
        mr(GN, "¿Qué género se dirige a una sola persona?", "Carta", ["Folleto", "Resumen"], "Una carta tiene un destinatario."),
        mr(CR, "¿Qué mínimo de palabras pide el criterio?", "60 palabras", ["80 palabras", "6 palabras"], "Dice Entre 60 y 80 palabras."),
    ],
    [
        mc("Quieres contar lo que sentiste el primer día de un taller. ¿Qué género eliges?", "Diario personal", ["Folleto", "Instrucciones"], "El journal cuenta experiencias y sentimientos."),
        arith("El criterio pide entre 60 y 80 palabras. Tu borrador tiene 54 palabras. ¿Cuántas palabras necesitas agregar como mínimo?", "60-54", "Se resta lo que tienes del mínimo pedido.", " palabras"),
        mr(OU, "¿Qué idea del cierre queda bien en el esquema?", "Come and learn with us this Saturday!", ["The workshop is on Saturday at 3 p.m.", "Cameras take good pictures of people"], "Cumple la función de invitar; las otras dan datos o explican."),
    ],
    [
        mr(BS + " " + OU, "Un compañero dice que snacks es importante para Body 1. ¿Qué respuesta es más acertada?", "No: snacks va en Body 2, con lo que se lleva", ["Sí: todo lo que se come o se bebe va en Body 1", "No existe Body 2"], "Hay que ordenar por función."),
        mr(CR, "Una compañera pregunta si puede omitir la imagen. ¿Qué responde alguien que lee con cuidado?", "No: el criterio la exige con pie de foto", ["Sí: es opcional", "Solo si es corta"], "El punto 5 lo indica."),
    ],
    [
        mr(GN, "Debes contar la vida de una persona que admiras, con hechos y fechas. ¿Qué género es mejor?", "Una biografía breve", ["Un folleto", "Instrucciones"], "Cuenta la vida de alguien."),
        mc("¿Qué paso sigue después de la lluvia de ideas?", "Agrupar y ordenar en un esquema", ["Publicar el folleto terminado en el panel", "Editar la ortografía"], "El esquema organiza las ideas."),
    ],
    [mr(CR, "Convierte el criterio en una lista de verificación. ¿Cuál respeta cada punto?", "Title; 60–80 words; day, time, place; two connectors; image with caption", ["Title; 80 words; day, time, place; one connector; image with caption", "Title; 60–80 words; day and place; two connectors; image with caption"], "Respeta cada punto del criterio: número de palabras, tres datos y dos conectores.")],
    [
        ("En Inglés de 2.º medio (OA 14, clase 1): ¿cuáles son los cinco pasos del proceso de escritura?", "Organizar ideas, redactar, revisar, editar y publicar", "Es el orden del proceso."),
        ("En Inglés de 2.º medio (OA 14, clase 1): ¿para qué sirve un esquema?", "Para ordenar las ideas antes de redactar", "Es el mapa del texto."),
        ("En Inglés de 2.º medio (OA 14, clase 1): ¿qué haces primero con un criterio de evaluación?", "Lo leo y lo convierto en tareas", "Así no olvidas puntos."),
    ],
    task("Elige un género de la lista (diario, instrucciones, folleto, biografía, carta, resumen, poema, cuento, correo electrónico, artículo, rima o descripción) y un tema de tu interés. Escribe el propósito, la audiencia, una lluvia de ideas de ocho palabras en inglés y un esquema de cuatro partes. Sigue este ejemplo.", "Género: instrucciones. Tema: how to make a bookmark. Propósito: enseñar. Audiencia: compañeros. Lluvia: paper, scissors, marker, fold, decorate, name, ribbon, glue. Esquema: Title; Materials; Steps; Closing.", ["define género, propósito y audiencia", "lluvia de ideas de ocho palabras", "esquema de cuatro partes"], ["hoja con las cuatro partes"], ["lluvia de ideas con palabras que no se relacionan", "esquema sin orden"], "Pide que quite una idea y explique por qué."),
    "Escribe en tu cuaderno la lista de verificación del criterio del folleto.",
    "Haz una lluvia de ideas en español sobre un tema de tu casa y agrúpala.",
)

# ------------------------------------------------------------------ clase 2: redactar a partir del esquema
D1 = "Esquema: Title: How to Make a Bookmark. Materials: paper, scissors, marker. Steps: 1) cut a strip, 2) draw a design, 3) write your name. Closing: use it in your favorite book. (bookmark = marcapáginas, strip = tira, scissors = tijeras, marker = plumón)"
D2 = "Borrador (primer párrafo): «Hello, I want to teach you how make a bookmark it is easy.»"
D3 = "Borrador mejorado: «Hello! Today I will show you how to make a bookmark. It is easy and you only need three things.»"
D4 = "Párrafo del cuerpo: «First, cut a strip of paper. Next, draw a design with a marker. Then write your name on it. Finally, put your bookmark in a book.»"
D5 = "Folleto (borrador): «Join the photo workshop on Saturday. We will learn to take good pictures. Bring your phone.»"

lesson(
    OA, 2, MAT_R,
    "Aprenderé a redactar un borrador a partir de mi esquema: escribir una introducción, párrafos con una idea principal cada uno y un cierre. Sirve para convertir ideas en un texto que se entienda.",
    ["Sé organizar ideas en un esquema.", "Sé escribir oraciones con first, next y finally."],
    [
        "Redactar (to draft) es escribir tu primera versión siguiendo el esquema. No te preocupes por que sea perfecta: lo importante es escribir todas las ideas. Cada parte del esquema se convierte en un párrafo o en una sección. La introducción presenta el tema y el propósito: Today I will show you how to make a bookmark. El desarrollo da los datos o pasos con palabras de secuencia: First, Next, Then, Finally. El cierre termina con una invitación, un resumen o un consejo.",
        "En cada párrafo, escribe primero una oración principal (topic sentence) que diga la idea del párrafo y luego oraciones de apoyo con datos y ejemplos. Usa el vocabulario del tema, los conectores del año (and, but, because, so, though, as a result, as soon as) y estructuras que conozcas. Evita copiar frases de otros textos: usa tus palabras.",
        "Mantén el criterio a la vista y marca cada punto que ya cumpliste. Al terminar el borrador, haz una pausa antes de revisar. Mirar el texto después de un descanso ayuda a ver errores y huecos.",
    ],
    [("draft", "borrador"), ("topic sentence", "oración principal"), ("supporting sentence", "oración de apoyo"), ("introduction / closing", "introducción / cierre"), ("first / next / then / finally", "primero / luego / después / por fin"), ("take a break", "tomar un descanso")],
    [
        ("Convertir el esquema en párrafos", D1 + " ¿Cómo escribirías la oración de introducción?", ["Debo presentar el tema y el propósito.", "Uso Today I will show you how to...", "Escribo: Today I will show you how to make a bookmark."], "Today I will show you how to make a bookmark"),
        ("Oración principal", D4 + " ¿Cuál es la oración principal del párrafo y cuáles son de apoyo?", ["La primera oración abre los pasos.", "Las otras dan cada paso.", "La principal anuncia los pasos."], "La principal es First, cut a strip of paper; las otras son de apoyo"),
    ],
    [
        ("Intentar escribir perfecto desde el primer intento.", "Frena la escritura.", "Escribe todas las ideas y revisa después."),
        ("Escribir párrafos sin oración principal.", "Cuesta entender la idea del párrafo.", "Empieza cada párrafo con una oración que diga su idea."),
    ],
    [
        mr(D4, "¿Qué palabras de secuencia aparecen?", "First, next, then y finally", ["Because y so", "Although y unless"], "Ordenan los pasos."),
        mr(D1, "¿Cuántos pasos tiene el esquema?", "Tres", ["Dos", "Cinco"], "Dice 1), 2) y 3)."),
        mc("¿Qué va en una introducción?", "El tema y el propósito", ["La despedida", "La lista de errores"], "La introducción presenta."),
    ],
    [
        mr(D2 + " " + D3, "¿Qué mejora tiene el borrador mejorado?", "Tiene un saludo con signo, how to y las ideas separadas", ["Usa palabras más difíciles y más largas que el borrador anterior", "Agrega una opinión personal"], "La puntuación y la estructura mejoran."),
        mr(D4, "¿Qué hay que hacer en el segundo paso?", "Dibujar un diseño con un plumón", ["Cortar una tira", "Escribir el nombre"], "Next, draw a design with a marker."),
        mr(D1, "¿Cuál es el cierre del esquema?", "Usar el marcapáginas en su libro favorito", ["Cortar una tira", "Dibujar un diseño"], "Dice Closing: use it in your favorite book."),
    ],
    [
        mc("Completa: Today I will show you ____ make a bookmark.", "how to", ["how", "to how"], "How to + verbo."),
        mc("Une las dos últimas oraciones del folleto con un conector: We will learn to take good pictures ____ bring your phone.", "so", ["but", "although"], "Una oración es la consecuencia de la otra."),
        arith("El criterio pide 60 palabras como mínimo. Escribiste 22 en la introducción y 31 en el desarrollo. ¿Cuántas palabras faltan en el cierre?", "60-22-31", "Se resta lo escrito del mínimo.", " palabras"),
    ],
    [
        mr(D4, "Un compañero dice que no hace falta then si ya está next. ¿Qué respuesta es más acertada?", "Cada paso necesita su señal de orden", ["Tiene razón: con next basta para todo", "Los pasos de un texto no se ordenan"], "Cada paso necesita una señal."),
        mr(D2, "¿Qué dos errores tiene el primer párrafo del borrador?", "Falta to después de how y falta puntuación", ["Tiene demasiadas comas y mayúsculas", "Está en pasado y falta el verbo auxiliar will"], "Debe decir how to y separar con puntos: ... how to make a bookmark. It is easy."),
    ],
    [
        mr(D5, "Reescribe el folleto con una introducción. ¿Cuál es mejor?", "Do you like photos? Join our workshop on Saturday", ["Photos. Saturday. Workshop. Phone. Come.", "I do not know what to write about this"], "Presenta el tema y despierta interés."),
        mr(D1, "Una compañera propone agregar un paso 4: «paint the wall». ¿Qué corriges?", "No pertenece: un marcapáginas se hace con papel", ["Nada: es un paso más del esquema", "Debería ser el primer paso del esquema, no el cuarto"], "Debe respetar el tema del esquema."),
    ],
    [mr(D3, "Escribe el párrafo que sigue al borrador mejorado. ¿Cuál es el mejor comienzo?", "First, you need paper, scissors and a marker", ["Finally, put your bookmark in a book", "Today I will show you how to make a bookmark"], "Sigue el esquema: Materials.")],
    [
        ("En Inglés de 2.º medio (OA 14, clase 2): ¿qué es una oración principal?", "La que dice la idea del párrafo", "Las demás la apoyan."),
        ("En Inglés de 2.º medio (OA 14, clase 2): ¿qué hace una introducción?", "Presenta el tema y el propósito", "Orienta al lector."),
        ("En Inglés de 2.º medio (OA 14, clase 2): ¿qué haces al terminar un borrador?", "Una pausa antes de revisar", "Ayuda a ver errores."),
    ],
    task("Con el esquema que hiciste en la clase anterior, redacta un borrador de 60 a 80 palabras en inglés con introducción, desarrollo y cierre. Usa al menos dos conectores del año y tres palabras de secuencia. Cuenta tus palabras y márcalas. Sigue este ejemplo.", "Hello! Today I will show you how to make a bookmark. It is easy and you only need three things: paper, scissors and a marker. First, cut a strip of paper. Next, draw a design with a marker, because it makes the bookmark special. Then write your name. Finally, put it in your favorite book. As a result, you will never lose your page.", ["introducción, desarrollo y cierre", "dos conectores del año y secuencia", "entre 60 y 80 palabras"], ["borrador en la hoja con el conteo de palabras"], ["no tener oración principal", "pasarse o quedarse corto de palabras"], "Pide que marque con colores la introducción, el desarrollo y el cierre."),
    "Escribe tres introducciones distintas para el mismo tema.",
    "Escribe en español una receta de tu casa con inicio, pasos y cierre.",
)

# ------------------------------------------------------------------ clase 3: revisar contenido y organización
RV1 = "Borrador de un resumen: «The movie is about a girl. The girl lives in a small town. She finds a map. The map shows a hidden room. In the room there is a box. The box has old letters. The story is interesting. I like it.»"
RV2 = "Borrador de una carta: «Dear Sam, I am writing to invite you to my birthday party. My brother will bring a cake. It will be on Saturday. I also want to say I am sorry I missed your call. Please come at four.»"
RV3 = "Lista de revisión (de ejemplo): 1) ¿Tiene una idea principal clara? 2) ¿Cada párrafo trata una sola idea? 3) ¿Las ideas están en orden lógico? 4) ¿Hay detalles que sobran? 5) ¿El cierre responde al propósito?"
RV4 = "Texto con ideas repetidas: «The park is big. The park is very big. The park is huge. The park is also big and green.»"

lesson(
    OA, 3, MAT_R,
    "Aprenderé a revisar el contenido y la organización de mi borrador: comprobar que la idea principal esté clara, que las ideas estén en orden y que no haya repeticiones ni ideas que sobren. Sirve para mejorar el texto antes de editar los errores.",
    ["Sé escribir un borrador.", "Sé usar conectores."],
    [
        "Revisar (to revise) es mejorar el contenido y la organización del texto. No es corregir la ortografía: eso se hace después, al editar. Al revisar, hazte preguntas sobre el texto completo: ¿se entiende la idea principal?, ¿cada párrafo trata una sola idea?, ¿el orden es lógico?, ¿falta algo?, ¿sobra algo? y ¿el cierre responde al propósito?",
        "Puedes revisar con cuatro acciones: agregar (add) información que falta, quitar (delete) lo que sobra, reordenar (reorder) ideas y reemplazar (replace) palabras o frases por otras mejores. Por ejemplo, el texto The park is big. The park is very big repite la misma idea: conviene unirlas y agregar un detalle, como The park is big and green, with a lake in the middle.",
        "Usa una lista de revisión (checklist) o pide a un compañero que lea tu texto. Las preguntas de otra persona muestran dónde no se entiende. Marca los cambios con colores y guarda la versión anterior por si quieres volver a ella.",
    ],
    [("revise", "revisar: mejorar contenido y organización"), ("add / delete", "agregar / quitar"), ("reorder", "reordenar"), ("replace", "reemplazar"), ("checklist", "lista de revisión"), ("peer review", "revisión de un compañero")],
    [
        ("Detectar ideas que sobran", RV2 + " ¿Qué oración no pertenece a la invitación?", ["El propósito es invitar a una fiesta.", "La oración sobre perder la llamada habla de otra cosa.", "Se puede quitar o poner en otra carta."], "I also want to say I am sorry I missed your call"),
        ("Unir ideas repetidas", RV4 + " ¿Cómo mejoras el texto?", ["Todas las oraciones dicen que el parque es grande.", "Dejo una idea y agrego un detalle.", "Escribo: The park is big and green, with a lake in the middle."], "The park is big and green, with a lake in the middle"),
    ],
    [
        ("Corregir solo la ortografía al revisar.", "La revisión se centra en el contenido y la organización.", "Primero revisa las ideas; después edita los errores."),
        ("Dejar ideas repetidas porque suenan bien.", "No agregan información.", "Une, quita o reemplaza."),
    ],
    [
        mr(RV3, "¿Qué pregunta revisa el orden de las ideas?", "¿Las ideas están en orden lógico?", ["¿Hay errores de ortografía?", "¿Tiene mayúsculas?"], "Es la pregunta 3."),
        mr(RV1, "¿Qué idea principal tiene el borrador del resumen?", "Una niña descubre un mapa y una caja", ["Una niña se muda a un pueblo pequeño", "Una niña lee cartas antiguas en su casa"], "Resume los hechos."),
        mc("¿Qué significa reorder?", "Cambiar el orden de las ideas", ["Corregir la ortografía", "Dibujar"], "Reorder es reordenar."),
    ],
    [
        mr(RV1, "¿Cuántas oraciones del borrador son opiniones y no hechos?", "Dos", ["Una", "Seis"], "The story is interesting y I like it son opiniones; las otras seis son hechos."),
        mr(RV2, "¿Cuál es el propósito de la carta?", "Invitar a una fiesta", ["Pedir perdón", "Agradecer un regalo"], "Dice I am writing to invite you."),
        mr(RV3, "¿Qué pregunta de la lista ayuda a detectar ideas repetidas o innecesarias?", "¿Hay detalles que sobran?", ["¿Tiene una idea principal clara?", "¿El cierre responde al propósito?"], "La pregunta 4 trata de lo que sobra."),
    ],
    [
        mr(RV1, "Un resumen debe ser breve y objetivo. ¿Qué oraciones quitarías?", "The story is interesting. I like it", ["She finds a map. The map shows a hidden room", "The girl lives in a small town"], "El resumen no incluye opiniones propias."),
        mr(RV2, "¿Dónde pondrías la oración Please come at four?", "Justo después de It will be on Saturday", ["Al principio de la carta", "En el saludo"], "La hora acompaña a la fecha."),
        arith("Un borrador tiene 90 palabras y debes dejar entre 60 y 80. Quitas 15 palabras. ¿Cuántas palabras quedan?", "90-15", "Se resta lo que quitas del total.", " palabras"),
    ],
    [
        mr(RV4, "Un compañero propone cambiar big por large en cada oración. ¿Qué respuesta es más acertada?", "No: sigue repitiendo la misma idea", ["Sí: ahora la idea no se repite nada", "Hay que quitar todos los puntos"], "Hay que unir y agregar información."),
        mr(RV2, "Otro compañero dice que quitar la oración de la llamada empeora la carta. ¿Qué respuesta es mejor?", "No: esa oración distrae del propósito", ["Sí: la carta pierde sentido sin ella", "Sí: es la oración más importante de todas"], "Un texto debe tener un propósito claro."),
    ],
    [
        mr(RV1, "Une las ideas para mejorar: ¿cuál es la mejor reescritura del inicio?", "The girl lives in a small town and finds a map", ["The movie. A girl. A town. A map. A room.", "A map finds a girl in a small town in the movie"], "Une la información en una sola oración clara."),
        mr(RV3, "¿Qué pregunta puede hacerte un compañero para revisar tu cierre?", "¿Mi cierre responde al propósito?", ["¿Cuántas comas hay?", "¿Cuántas imágenes hay?"], "Se relaciona con el propósito."),
    ],
    [mc("Tu compañero lee tu texto y dice «No entiendo para qué escribes». ¿Qué parte del texto revisas?", "La introducción y el propósito", ["La ortografía de una palabra", "El color de la letra"], "El propósito está en la introducción.")],
    [
        ("En Inglés de 2.º medio (OA 14, clase 3): ¿qué cuatro acciones tiene la revisión?", "Agregar, quitar, reordenar y reemplazar", "Mejoran el contenido y la organización."),
        ("En Inglés de 2.º medio (OA 14, clase 3): ¿cuándo se corrige la ortografía?", "Al editar, después de revisar", "Se editan los errores al final."),
        ("En Inglés de 2.º medio (OA 14, clase 3): ¿para qué sirve la revisión de un compañero?", "Para ver dónde no se entiende el texto", "Otra persona detecta lo que tú no ves."),
    ],
    task("Toma tu borrador de la clase anterior y revísalo con la lista de revisión: marca con colores qué agregas, quitas, reordenas y reemplazas. Escribe la versión revisada y explica en español tres cambios. Sigue este ejemplo.", "Cambios: quité la oración que no se relacionaba con el tema; agregué un ejemplo; reordené los pasos 2 y 3. Versión revisada: Hello! Today I will show you how to make a bookmark. First...", ["usa la lista de revisión", "explica tres cambios", "la versión revisada es más clara"], ["borrador marcado", "versión revisada"], ["corregir solo la ortografía", "no explicar los cambios"], "Pide a un compañero que lea la versión revisada y diga la idea principal."),
    "Revisa un párrafo con ideas repetidas y reescríbelo en inglés.",
    "Pide a alguien que lea un texto tuyo y anota dos preguntas que te haga.",
)

# ------------------------------------------------------------------ clase 4: editar con diccionario en línea
ED1 = "Texto con errores: «My freind recieved a letter yesterday. We was very exited becuase the letter come from Canada.» (friend = amigo, receive = recibir, excited = emocionados, because = porque)"
ED2 = "Texto editado: «My friend received a letter yesterday. We were very excited because the letter came from Canada.»"
DIC = "Entrada de diccionario en línea (de ejemplo). Palabra: patient. Clase: adjective. Pronunciación: /ˈpeɪʃənt/. Significado: able to wait calmly. Ejemplo: She was patient while waiting for the bus. Sinónimo: calm. Opuesto: impatient. También sustantivo (noun): a person who receives medical care."
DIC2 = "Entrada de diccionario en línea (de ejemplo). Palabra: borrow. Clase: verb. Significado: to take something and give it back later. Ejemplo: Can I borrow your pen? Ojo: lend es lo contrario (lend, lent = dar algo prestado; lent es el pasado)."
CH = "Lista de edición (de ejemplo): 1) Mayúsculas al inicio de cada oración y en nombres. 2) Punto final o signo de interrogación. 3) Concordancia sujeto-verbo. 4) Tiempo verbal coherente. 5) Ortografía de palabras frecuentes."

lesson(
    OA, 4, MAT_R,
    "Aprenderé a editar mi texto: corregir ortografía, puntuación, mayúsculas y concordancia, y a usar un diccionario en línea para comprobar significados, clases de palabra, ejemplos y sinónimos. Sirve para entregar un texto correcto y bien escrito.",
    ["Sé revisar contenido y organización.", "Conozco palabras frecuentes de ortografía."],
    [
        "Editar (to edit) es corregir los errores de la forma después de revisar el contenido. Usa una lista de edición: mayúsculas al comienzo de las oraciones y en los nombres; puntuación (punto, coma, signos de interrogación y comillas); concordancia entre sujeto y verbo (she receives, we were); tiempo verbal coherente (yesterday pide pasado); y ortografía de palabras frecuentes (friend, receive, excited, because).",
        "Un diccionario en línea (online dictionary) ayuda a comprobar una palabra. Una entrada trae la clase de palabra (noun, verb, adjective), la pronunciación, el significado, un ejemplo y, a veces, sinónimos y opuestos. Si dudas entre dos palabras, como borrow y lend, lee el ejemplo para ver cómo se usa. También puedes escribir la palabra y ver si el diccionario sugiere otra ortografía.",
        "Edita despacio, leyendo cada oración y marcando los errores con un color. Lee tu texto en voz alta para encontrar errores de concordancia. Cuando corrijas, no cambies el contenido ya revisado, a menos que veas un error de sentido.",
    ],
    [("edit", "editar: corregir la forma"), ("spelling / punctuation", "ortografía / puntuación"), ("subject-verb agreement", "concordancia sujeto-verbo"), ("online dictionary", "diccionario en línea"), ("part of speech", "clase de palabra"), ("synonym / opposite", "sinónimo / opuesto")],
    [
        ("Corregir con la lista de edición", ED1 + " Corrige los errores.", ["Ortografía: freind, recieved, exited, becuase.", "Concordancia: we was → we were.", "Tiempo: the letter come → came, porque yesterday pide pasado."], "My friend received a letter yesterday. We were very excited because the letter came from Canada"),
        ("Usar una entrada de diccionario", DIC + " ¿Qué clase de palabra es patient y qué significa?", ["La entrada dice adjective.", "El significado es able to wait calmly.", "Significa que espera con calma."], "Es un adjetivo: que espera con calma"),
    ],
    [
        ("Cambiar el contenido al editar.", "La edición se centra en la forma.", "Corrige la forma sin cambiar las ideas."),
        ("Confiar solo en el corrector automático.", "No detecta todos los errores de sentido.", "Revisa tú también y consulta el diccionario."),
    ],
    [
        mc("¿Cuál es la ortografía correcta?", "friend", ["freind", "frend"], "En inglés es friend, con ie."),
        mc("¿Cuál es la ortografía correcta?", "because", ["becuase", "becouse"], "Se escribe because."),
        mr(DIC2, "¿Qué significa borrow?", "Tomar algo para devolverlo luego", ["Dar algo prestado", "Comprar algo"], "El diccionario lo define así."),
    ],
    [
        mr(DIC, "¿Cuál es el opuesto de patient?", "impatient", ["calm", "careful"], "La entrada indica Opuesto: impatient."),
        mr(DIC2, "Quieres pedir una goma de borrar a un compañero. ¿Cuál es la oración correcta?", "Can I borrow your eraser?", ["Can I lend your eraser?", "Can I borrowing your eraser?"], "Borrow es tomar prestado."),
        mr(ED1, "¿Qué error de concordancia aparece?", "We was", ["She said", "From Canada"], "Con we se usa were."),
    ],
    [
        mr(CH, "¿Qué punto de la lista corresponde a corregir the letter come?", "Tiempo verbal coherente (punto 4)", ["Mayúsculas (punto 1)", "Puntuación (punto 2)"], "Come debe ser came porque yesterday pide pasado."),
        mc("Corrige: «yesterday i go to school».", "Yesterday I went to school", ["Yesterday I go to school", "Yesterday i went to school"], "Mayúsculas y pasado."),
        arith("Tu texto tiene 12 errores de ortografía, 5 de concordancia y 4 de puntuación. Corriges todos los de ortografía y todos los de puntuación. ¿Cuántos errores quedan?", "12+5+4-12-4", "Se suman los errores y se restan los corregidos.", " errores"),
    ],
    [
        mr(ED2, "Compara con el texto con errores. ¿Qué cambió en come?", "Pasó a came, porque yesterday pide pasado", ["Pasó a comes", "No cambió"], "El pasado simple indica un hecho terminado ayer."),
        mr(DIC, "Un compañero dice que en She is a patient person la palabra patient es un sustantivo. ¿Qué responde alguien que consulta el diccionario?", "Aquí es adjetivo; el sustantivo es otro", ["Es siempre un sustantivo, en todos los casos", "No existe como adjetivo en inglés"], "La entrada muestra las dos clases: adjective (esperar con calma) y noun (paciente médico)."),
    ],
    [
        mr(ED1, "Edita la oración «We was very exited». ¿Cuál es la correcta?", "We were very excited", ["We was very excited", "We were very exitted"], "Concordancia y ortografía."),
        mr(CH, "¿Qué punto de la lista revisa un signo de interrogación faltante?", "Puntuación", ["Concordancia", "Tiempo"], "El punto 2 trata de puntuación."),
    ],
    [mr(DIC2, "Una compañera escribe «Can you borrow me your pen?». ¿Qué corriges con el diccionario?", "Can you lend me your pen?", ["Nada: la oración ya es correcta", "Can you borrowing me your pen?"], "Lend es dar prestado; borrow, tomar prestado.")],
    [
        ("En Inglés de 2.º medio (OA 14, clase 4): ¿qué se corrige al editar?", "La forma: ortografía, puntuación, concordancia y tiempo", "No se cambia el contenido."),
        ("En Inglés de 2.º medio (OA 14, clase 4): ¿qué información trae una entrada de diccionario?", "Clase de palabra, significado, ejemplo, sinónimos y opuestos", "Ayuda a usar la palabra."),
        ("En Inglés de 2.º medio (OA 14, clase 4): ¿cuál es la diferencia entre borrow y lend?", "Borrow es tomar prestado; lend es dar prestado", "Son acciones contrarias."),
    ],
    task("Corrige este texto con la lista de edición y una consulta a un diccionario en línea (o a la entrada de la clase): «yesterday my brother lend me his bike but i was very scared becuase the road was wet.» (lend = prestar, pasado lent; scared = asustado, road = camino, wet = mojado). Escribe la versión editada y la palabra que consultaste con su clase y significado.", "Yesterday my brother lent me his bike, but I was very scared because the road was wet. Consulté lend: verbo, dar algo prestado.", ["corrige mayúsculas, ortografía y verbo", "consulta una palabra y anota su clase y significado", "no cambia el contenido"], ["texto editado en la hoja"], ["no corregir lend", "cambiar las ideas"], "Pide que lea el texto en voz alta para comprobar la concordancia."),
    "Edita tu borrador revisado con la lista de edición y marca cada corrección.",
    "Busca una palabra nueva en un diccionario en línea y anota su clase, significado y un ejemplo.",
)

# ------------------------------------------------------------------ clase 5: publicar con procesador de textos
WP = "Pantalla de ejemplo de un procesador de textos. Barra de herramientas: Bold (negrita), Italic (cursiva), Font size (tamaño de letra), Bullets (viñetas), Spell check (revisor de ortografía), Insert image (insertar imagen), Save (guardar), Print (imprimir), Undo (deshacer)."
PB1 = "Versión final de un folleto (descrita): título «Photo Workshop» en negrita y letra grande; tres viñetas con día, hora y lugar; una imagen con pie de foto; letra legible de 12 puntos; sin errores marcados por el revisor."
PB2 = "Versión final mal presentada: sin título, letra de 7 puntos, tres tipos de letra distintos, imagen sin pie de foto y varias palabras subrayadas en rojo por el revisor."

lesson(
    OA, 5, MAT_R,
    "Aprenderé a publicar mi texto con un procesador de textos: dar formato (título, tamaño de letra, viñetas), usar el revisor de ortografía, insertar una imagen, guardar y comprobar la versión final con el criterio. Sirve para presentar un texto claro y cuidado.",
    ["Sé revisar y editar un texto.", "Conozco las herramientas básicas de un procesador."],
    [
        "Publicar (to publish) es presentar la versión final a su audiencia. Con un procesador de textos puedes dar formato: usar negrita (Bold) para el título, un tamaño de letra legible (por ejemplo 12 puntos), viñetas (Bullets) para listas e imágenes con pie de foto. Usa un máximo de dos tipos de letra y colores que se lean bien. El revisor de ortografía (Spell check) marca las palabras que podría haber escrito mal; tú decides si el cambio es correcto.",
        "Antes de publicar, relee tu texto con el criterio y revisa la lista de verificación: título, extensión, datos pedidos, conectores, imagen con pie de foto y presentación. Guarda tu archivo (Save) con un nombre claro, como photo-workshop-final. Si lo vas a imprimir, previsualiza primero (Print preview). Si lo vas a compartir, comprueba que la imagen y el texto se vean bien.",
        "Después de publicar, reflexiona: ¿qué parte del proceso fue más fácil o más difícil?, ¿qué errores repetiste?, ¿qué harás distinto la próxima vez? Anota tus metas para mejorar. Así el proceso de escritura se vuelve un hábito.",
    ],
    [("publish", "publicar"), ("format", "dar formato"), ("Bold / Italic", "negrita / cursiva"), ("Bullets", "viñetas"), ("Spell check", "revisor de ortografía"), ("Save / Print preview", "guardar / vista previa de impresión")],
    [
        ("Elegir herramientas", WP + " ¿Qué herramientas usas para dar formato al título y a una lista?", ["Para el título: Bold y Font size.", "Para la lista: Bullets.", "Respondo con ambas."], "Bold y Font size para el título; Bullets para la lista"),
        ("Comparar dos versiones finales", PB1 + " " + PB2 + " ¿Cuál es mejor y por qué?", ["La primera tiene título, viñetas, imagen con pie y letra legible.", "La segunda no tiene título y la letra es muy pequeña.", "La primera cumple el criterio."], "La primera, porque tiene título, viñetas, imagen con pie y letra legible"),
    ],
    [
        ("Aceptar todo lo que sugiere el revisor automático.", "Puede cambiar una palabra correcta por otra equivocada.", "Revisa cada sugerencia con tu criterio."),
        ("Usar cuatro tipos de letra distintos.", "El texto se ve desordenado.", "Usa un máximo de dos tipos de letra."),
    ],
    [
        mr(WP, "¿Qué herramienta sirve para deshacer un cambio?", "Undo", ["Print", "Bullets"], "Undo deshace la última acción."),
        mr(WP, "¿Qué herramienta marca posibles errores de ortografía?", "Spell check", ["Bold", "Insert image"], "Es el revisor de ortografía."),
        mr(PB1, "¿Cuántas viñetas tiene el folleto final?", "Tres", ["Dos", "Cinco"], "Dice tres viñetas con día, hora y lugar."),
    ],
    [
        mr(PB2, "¿Qué problema tiene la letra del folleto mal presentado?", "Es de 7 puntos y de tres tipos distintos", ["Es muy grande", "Es de un solo tipo"], "Es muy pequeña y variada."),
        mr(PB1, "¿Qué letra tiene el folleto final?", "Legible, de 12 puntos", ["De 7 puntos", "Muy decorada"], "Dice letra legible de 12 puntos."),
        mc("¿Cuándo usas Print preview?", "Antes de imprimir, para ver cómo quedará", ["Después de guardar el archivo", "Solo si no hay errores"], "Previsualiza para evitar sorpresas."),
    ],
    [
        mc("Quieres que tu título se vea más importante. ¿Qué haces?", "Usar negrita y un tamaño mayor", ["Escribirlo en un color claro sobre fondo blanco", "Borrar el título"], "Se destaca con formato legible."),
        mc("El revisor subraya el nombre propio Lautaro, que está bien escrito. ¿Qué haces?", "Dejarlo así: el nombre está bien escrito", ["Cambiarlo por la palabra que sugiere el revisor", "Borrar la oración completa"], "Tú decides si el aviso es correcto."),
        arith("El criterio pide 60 a 80 palabras. Tu versión final tiene 72 palabras. ¿Cuántas palabras más puedes agregar sin pasarte del máximo de 80?", "80-72", "Se resta lo escrito del máximo permitido.", " palabras"),
    ],
    [
        mr(PB2, "Un compañero dice que con arreglar el revisor ya está listo. ¿Qué responde alguien que lee con cuidado?", "No: también faltan el título y el pie de foto", ["Sí: arreglar las palabras subrayadas basta para publicar", "No: solo faltan más colores y más imágenes"], "La presentación incluye varios elementos."),
        mr(PB1, "Otro compañero dice que las viñetas son un adorno. ¿Qué responde alguien que lee con cuidado?", "Sirven para ordenar los datos de forma clara", ["Son solo para decorar", "Son obligatorias en todos los textos"], "Ordenan la información."),
    ],
    [
        mr(PB1 + " " + PB2, "¿Qué criterio del folleto no cumple la versión mal presentada?", "Imagen con pie de foto y título claro", ["Tres datos", "Dos conectores"], "La versión mala carece de título y pie de foto."),
        mc("Después de publicar, ¿qué reflexión ayuda más a mejorar?", "Anotar mis errores y qué haré distinto", ["Olvidar el trabajo y empezar otro texto", "Cambiar siempre de tema y de género"], "La reflexión mejora el proceso."),
    ],
    [mc("Vas a publicar tu texto en un panel del colegio. ¿Qué verificas antes de imprimir?", "Título, letra legible, imagen con pie", ["Solo el color y el tipo de papel", "Solo la hora y el día en que se imprime"], "Es la lista de verificación final.")],
    [
        ("En Inglés de 2.º medio (OA 14, clase 5): ¿qué herramienta usa un procesador para marcar errores de ortografía?", "El revisor de ortografía", "Es una ayuda, no una garantía."),
        ("En Inglés de 2.º medio (OA 14, clase 5): ¿para qué sirve Print preview?", "Para ver cómo quedará antes de imprimir", "Evita errores de presentación."),
        ("En Inglés de 2.º medio (OA 14, clase 5): ¿qué haces después de publicar?", "Reflexiono sobre mi proceso y fijo metas", "Cierra el proceso de escritura."),
    ],
    task("Elige tu versión editada de la clase anterior y prepárala para publicar con un procesador de textos (o a mano, imitando el formato): título en negrita, letra legible, una lista con viñetas, una imagen con pie de foto. Escribe una lista de verificación con el criterio y marca lo que cumples. Escribe una reflexión de tres frases en español. Sigue este ejemplo.", "Lista: título sí; 60 a 80 palabras sí; viñetas sí; imagen con pie sí; dos conectores sí. Reflexión: lo más difícil fue revisar el orden; repetí errores de concordancia; la próxima vez leeré en voz alta.", ["aplica el formato pedido", "marca el criterio", "escribe una reflexión de tres frases"], ["versión publicada", "lista y reflexión"], ["publicar sin comprobar el criterio", "no reflexionar sobre el proceso"], "Pide que cambie un formato y explique si mejora la lectura."),
    "Diseña a mano una página con título, viñetas e imagen y compárala con la lista de verificación.",
    "Muestra tu texto final a una persona de tu casa y anota su opinión sobre cómo se ve.",
)
