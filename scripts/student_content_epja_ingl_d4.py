"""Inglés EPJA Nivel 2, módulo 4 (parte 4): OAD-16, comprender un video (transcripción escrita) y crear un texto sobre trabajos inusuales. No hay audio ni video: los videos se trabajan como transcripción."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-16"

F1 = ("Text (example): Some jobs are common, like driver or cook. Other jobs are unusual. Paula is a beekeeper: she works with bees on a farm. "
      "Tom is a window cleaner: he cleans windows on tall buildings. Mr. Vega is a cave guide: he works inside a cave and shows it to visitors. He always wears a helmet.")

F2 = ("Place list (example). Paula works on a farm. She goes to the farm by bus and waits for the bus at the bus stop. The bees are inside the boxes. "
      "The boxes are next to a tree. At noon Paula eats lunch at a table next to the boxes. Tom works on a tall building. Mr. Vega works inside a cave.")

F3 = ("Explanation sheet (example). Always and generally show a habit: Tom generally cleans windows in the morning. Now and at the moment show an action in progress: Tom is cleaning a window now. "
      "Question: What is Tom doing at the moment? Answer: He is cleaning a window on the roof.")

F4 = (GUION + "Transcription of an example video: «Welcome to our video about unusual jobs. Today we meet Paula. Paula is a beekeeper. She generally works on a farm in the morning. "
      "At the moment she is walking to the boxes next to the trees. She is wearing a white suit and a hat. She always uses smoke and works slowly. "
      "Inside the boxes there are thousands of bees. Paula says: I love my job because it is quiet.»")

F5 = ("Model text (example), «My uncle's job»: My uncle Iván is a lighthouse keeper. He lives next to the sea. He always checks the light at night. "
      "He generally goes to the town on Saturdays. At the moment he is fixing a window inside the lighthouse. His job is unusual because he works alone, but he likes it.")

F6 = (GUION + "Transcription of an example video: «Our next job is very unusual. Lena is a tea taster. She works at a tea company, in a small office next to a garden. "
      "She tastes about twenty teas every day. She generally starts at nine. Right now she is smelling a green tea. "
      "She says: I don't drink coffee at work because it changes the taste.»")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de los trabajos que ya conozco y leo un texto sobre tres trabajos inusuales.",
    prior=["Conozco nombres de trabajos comunes en inglés.", "Uso el presente simple con he y she.", "Sé que hay trabajos poco comunes."],
    explain=[
        "Un trabajo inusual es un trabajo poco común, pero real. Para presentar un trabajo en inglés se usa el verbo to be: Paula is a beekeeper. Después se agrega dónde trabaja y qué hace: she works with bees on a farm.",
        "Para decir qué hace una persona usa el presente simple: Tom cleans windows. Con he, she e it el verbo lleva «-s». La palabra always significa «siempre» y va antes del verbo: He always wears a helmet.",
        "Las palabras on e inside dicen dónde: on a farm, on tall buildings, inside a cave. Hoy las ves en un texto; mañana las aprenderás mejor. Subraya el nombre del trabajo y el lugar en cada oración.",
    ],
    vocab=[("job", "trabajo, oficio"), ("beekeeper", "apicultor o apicultora"), ("window cleaner", "limpiavidrios"), ("guide", "guía"), ("visitors", "visitantes"), ("helmet", "casco")],
    worked=[
        ("Presentar un trabajo", "Quieres decir que Tom es limpiavidrios.", ["Uso to be: is.", "Agrego a y el nombre del trabajo."], "Tom is a window cleaner."),
        ("Decir dónde trabaja", "El señor Vega trabaja dentro de una cueva.", ["Verbo con «-s»: works.", "Agrego inside a cave."], "Mr. Vega works inside a cave."),
    ],
    mistakes=[("Escribir «Tom clean windows» sin la «-s».", "Con he el presente simple lleva «-s».", "Escribe Tom cleans windows."),
              ("Escribir «She is works on a farm».", "No se mezclan is y el verbo en presente simple.", "Escribe She works on a farm.")],
    T=[
        ("abc", "{F} Which job is Paula's?", "She is a beekeeper", "She is a window cleaner", "She is a cave guide", "El texto dice que Paula es apicultora y trabaja con abejas."),
        ("ab", "{F} Where does Mr. Vega work?", "Inside a cave", "On a tall building", "El texto dice que trabaja inside a cave."),
        ("abc", "{F} What does Tom clean?", "Windows", "Boxes", "Caves", "El texto dice que Tom limpia ventanas en edificios altos."),
        ("{F} What does Mr. Vega always wear? Write one word.", "helmet", "El texto dice He always wears a helmet, es decir, un casco."),
        ("ab", "{F} Who works on tall buildings?", "Tom", "Paula", "El texto dice que Tom limpia ventanas on tall buildings."),
        ("abc", "What does «visitors» mean?", "Visitantes", "Vecinos", "Vendedores", "Visitors son las personas que visitan un lugar."),
        ("abc", "Complete: Tom ___ windows on tall buildings.", "cleans", "clean", "cleaning", "Con Tom (he) el verbo lleva «-s»."),
        ("abc", "Complete: Paula ___ with bees on a farm.", "works", "work", "working", "Con Paula (she) el verbo lleva «-s»."),
        ("ab", "{F} Which sentence is true?", "Mr. Vega shows the cave to visitors", "Mr. Vega shows the farm to bees", "El texto dice que Mr. Vega muestra la cueva a los visitantes."),
        ("abc", "What does «unusual» mean?", "Poco común", "Muy común", "Muy caro", "Unusual describe algo que no es habitual."),
        ("ab", "Choose the correct sentence.", "Tom is a window cleaner", "Tom are a window cleaner", "Con Tom se usa is, la forma de to be para he."),
        ("abc", "Put the words in order: works / inside / Mr. Vega / a cave", "Mr. Vega works inside a cave", "Mr. Vega work inside a cave", "Works Mr. Vega inside a cave", "El orden es sujeto, verbo y lugar."),
        ("ab", "Make this sentence negative: «Paula cleans windows.»", "Paula doesn't clean windows", "Paula doesn't cleans windows", "Después de doesn't el verbo queda sin «-s»."),
    ],
    ctx=("abc", "En una reunión de vecinos, Camila cuenta que su primo trabaja con abejas en un campo. ¿Qué frase usa para presentar su trabajo?", "My cousin is a beekeeper", "My cousin beekeeper", "My cousin are a beekeeper", "Para presentar un trabajo se usa is y a antes del oficio."),
    sc=[("En Inglés: ¿cómo dices «Ella es apicultora»?", "She is a beekeeper", "Se usa to be con el nombre del trabajo."),
        ("En Inglés: ¿qué significa «always»?", "Siempre", "Always indica que algo ocurre todas las veces."),
        ("En Inglés: ¿qué significa «inside a cave»?", "Dentro de una cueva", "Inside indica que algo está en el interior.")],
    op=("Escribe en tu cuaderno cuatro oraciones sobre dos trabajos poco comunes que inventes o conozcas (sin nombres reales). Dices qué trabajo es y dónde se hace.",
        "Rosa is a mountain guide. She works on a mountain. Pedro is a roof painter. He works on tall roofs.",
        ["usa is con el nombre del trabajo", "usa el verbo con «-s» con he o she", "dice dónde se hace el trabajo"],
        ["cuatro oraciones escritas"],
        ["olvidar la «-s» con he o she", "usar nombres de personas reales"],
        "Pregunta: «¿Qué trabajo inusual me llamó más la atención y por qué?»."),
    reinforce="Escribe el nombre de tres trabajos comunes y uno inusual, en inglés.",
    extend="Busca en tu barrio un trabajo poco común y escríbelo en dos oraciones.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo las palabras de lugar to, on, inside, next to y at para contar dónde se hace un trabajo.",
    prior=["Digo dónde trabaja una persona.", "Reconozco on e inside.", "Entiendo oraciones con to be y presente simple."],
    explain=[
        "Las preposiciones de lugar dicen dónde está algo o hacia dónde se va. On significa «sobre» o «en» una superficie: on a farm, on a tall building. Inside significa «dentro de». Next to significa «al lado de». At se usa para un punto del espacio, como at the bus stop o at a table.",
        "To se usa con verbos de movimiento y dice hacia dónde: She goes to the farm. She walks to the boxes. No mezcles to con las otras: no se dice at to ni inside to.",
        "Para leer una lista de lugares, imagina la escena y dibújala en tu cuaderno con flechas. Así ves dónde están las cosas y qué hace cada persona. Los textos son ejemplos inventados.",
    ],
    vocab=[("to", "hacia, a"), ("on", "sobre, en"), ("inside", "dentro de"), ("next to", "al lado de"), ("at", "en (un punto)"), ("noon", "mediodía")],
    worked=[
        ("Elegir la preposición", "Las abejas están en las cajas, es decir, adentro.", ["Pregunto: ¿están dentro o al lado?", "Están dentro: inside."], "The bees are inside the boxes."),
        ("Decir hacia dónde va", "Paula va a la granja en bus.", ["Verbo de movimiento: goes.", "Hacia dónde: to the farm."], "Paula goes to the farm by bus."),
    ],
    mistakes=[("Escribir «She goes at the farm».", "Con verbos de movimiento se usa to, no at.", "Escribe She goes to the farm."),
              ("Usar next to cuando quieres decir dentro.", "Next to es al lado, no adentro.", "Si está en el interior, usa inside.")],
    T=[
        ("abc", "{F} Where are the bees?", "Inside the boxes", "At the bus stop", "On the bus", "El texto dice que las abejas están inside the boxes."),
        ("ab", "{F} Where are the boxes?", "Next to a tree", "Inside a cave", "El texto dice que las cajas están next to a tree."),
        ("{F} Paula goes to the farm by ___. Write one word.", "bus", "El texto dice She goes to the farm by bus."),
        ("abc", "{F} Where does Paula eat lunch?", "At a table next to the boxes", "On a tall building", "Inside a cave", "El texto dice que come en una mesa al lado de las cajas."),
        ("ab", "{F} When does Paula eat lunch?", "At noon", "At night", "El texto dice At noon, es decir, al mediodía."),
        ("abc", "{F} Where does Tom work?", "On a tall building", "Inside a cave", "On a farm", "El texto dice que Tom trabaja on a tall building."),
        ("abc", "What does «next to» mean?", "Al lado de", "Dentro de", "Lejos de", "Next to indica que algo está junto a otra cosa."),
        ("abc", "What does «inside» mean?", "Dentro de", "Encima de", "Detrás de", "Inside indica el interior de algo."),
        ("abc", "Complete: Paula goes ___ the farm by bus.", "to", "at", "next", "Con un verbo de movimiento se usa to."),
        ("abc", "The bees are in the boxes, so they are ___ the boxes.", "inside", "next to", "on", "Si están en el interior, se usa inside."),
        ("ab", "Complete: Paula waits for the bus ___ the bus stop.", "at", "to", "Para un punto como el paradero se usa at."),
        ("ab", "Put the words in order: next to / The boxes / are / a tree", "The boxes are next to a tree", "The boxes next to are a tree", "El orden es sujeto, verbo to be y lugar."),
        ("abc", "Which sentence is correct?", "Paula walks to the boxes", "Paula walks at the boxes", "Paula walks inside to the boxes", "Con walk se usa to para decir hacia dónde."),
    ],
    ctx=("abc", "Para llegar a tu trabajo nuevo, un compañero te dice dónde está la oficina. Quieres decir que está al lado de la panadería. ¿Qué dices?", "The office is next to the bakery", "The office is at to the bakery", "The office is inside to the bakery", "Next to se usa para decir que algo está al lado de otra cosa."),
    sc=[("En Inglés: ¿qué preposición se usa para decir hacia dónde vas?", "to", "To se usa con verbos de movimiento."),
        ("En Inglés: ¿cómo dices «dentro de una caja»?", "Inside a box", "Inside indica que algo está en el interior de otra cosa."),
        ("En Inglés: ¿qué significa «next to»?", "Al lado de", "Next to indica que algo está junto a otra cosa.")],
    op=("Dibuja en tu cuaderno un lugar de trabajo inventado y escribe cuatro oraciones con to, on, inside, next to o at.",
        "The workers go to the warehouse. The boxes are inside the warehouse. The truck is next to the door. The driver waits at the gate.",
        ["usa cuatro preposiciones de lugar distintas", "las oraciones tienen sujeto y verbo", "el dibujo coincide con el texto"],
        ["dibujo y cuatro oraciones escritas"],
        ["usar at con verbos de movimiento", "confundir inside con next to"],
        "Pregunta: «¿Qué palabra de lugar usé para decir dónde está cada cosa?»."),
    reinforce="Mira tu casa o tu trabajo y di en voz alta tres cosas con next to.",
    extend="Escribe cuatro oraciones con inside sobre cosas que están dentro de algo en tu casa.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a distinguir lo que alguien hace siempre y lo que está haciendo ahora, con always, generally, now y at the moment.",
    prior=["Uso el presente simple.", "Entiendo la forma de to be.", "Sé decir lugares con on, inside y next to."],
    explain=[
        "El presente simple dice lo que ocurre de costumbre: Tom generally cleans windows in the morning. Va con palabras como always y generally. El presente continuo dice lo que ocurre ahora: Tom is cleaning a window now. Va con palabras como now y at the moment.",
        "Paso 1: mira la palabra de tiempo. Si dice always o generally, usa el presente simple. Si dice now o at the moment, usa to be + verbo con -ing: is cleaning, is eating, are working. Paso 2: escribe el verbo. Paso 3: agrega el lugar.",
        "La pregunta del presente continuo es What is Tom doing at the moment? y se responde con He is cleaning a window on the roof. No hay que memorizar tablas largas: mira la palabra de tiempo y elige.",
    ],
    vocab=[("generally", "por lo general"), ("now", "ahora"), ("at the moment", "en este momento"), ("roof", "techo"), ("is cleaning", "está limpiando"), ("lunch", "almuerzo")],
    worked=[
        ("Elegir el tiempo", "Palabra de tiempo: generally.", ["Generally muestra costumbre.", "Uso el presente simple."], "Tom generally cleans windows in the morning."),
        ("Elegir el tiempo", "Palabra de tiempo: now.", ["Now muestra que ocurre ahora.", "Uso to be + verbo con -ing."], "Tom is cleaning a window now."),
    ],
    mistakes=[("Escribir «Tom cleans a window now».", "Con now se usa to be + verbo con -ing.", "Escribe Tom is cleaning a window now."),
              ("Escribir «Tom is generally cleaning».", "Generally muestra costumbre y pide el presente simple.", "Escribe Tom generally cleans.")],
    T=[
        ("abc", "{F} Which words show a habit?", "Always and generally", "Now and at the moment", "Only on", "El texto dice que always y generally muestran una costumbre."),
        ("ab", "{F} Which sentence says what Tom is doing now?", "Tom is cleaning a window now", "Tom generally cleans windows", "La acción en progreso usa is cleaning con now."),
        ("abc", "Complete: Tom generally ___ windows in the morning.", "cleans", "is cleaning", "clean", "Con generally se usa el presente simple con «-s»."),
        ("abc", "Complete: Tom ___ a window now.", "is cleaning", "cleans", "clean", "Con now se usa is + verbo con -ing."),
        ("abc", "Complete: At the moment, Paula ___ lunch.", "is eating", "eats", "eat", "At the moment pide el presente continuo."),
        ("ab", "Choose the correct sentence.", "Mr. Vega always wears a helmet", "Mr. Vega always is wearing a helmet", "Always muestra costumbre y pide el presente simple."),
        ("{F} What is Tom doing at the moment? Complete: He is cleaning a ___ on the roof.", "window", "El texto dice He is cleaning a window on the roof."),
        ("abc", "Which question asks about what happens right now?", "What is Tom doing at the moment?", "What does Tom generally do?", "Where does Tom live?", "La pregunta con at the moment y is doing se refiere al ahora."),
        ("ab", "Spot the error and choose the correct sentence: «Tom cleaning a window now.»", "Tom is cleaning a window now", "Tom cleans a window now", "En el presente continuo se necesita is antes de cleaning."),
        ("abc", "Choose the negative of «Tom is cleaning a window».", "Tom isn't cleaning a window", "Tom doesn't cleaning a window", "Tom doesn't is cleaning a window", "En el presente continuo la negación es isn't."),
        ("abc", "What does «at the moment» mean?", "En este momento", "En la noche", "Todos los días", "At the moment indica el momento actual."),
        ("abc", "Put the words in order: is / now / working / Lena", "Lena is working now", "Lena working is now", "Is Lena now working", "El orden es sujeto, is, verbo con -ing y tiempo."),
        ("ab", "Which time word goes with the present simple?", "Generally", "Right now", "Generally muestra costumbre y se usa con el presente simple."),
    ],
    ctx=("abc", "Una compañera te llama y te pregunta qué haces en este momento. Estás almorzando. ¿Qué respondes?", "I am eating lunch", "I eat lunch", "I eating lunch", "Para lo que ocurre ahora se usa am + verbo con -ing."),
    sc=[("En Inglés: ¿qué tiempo usas con always o generally?", "El presente simple", "Esas palabras muestran una costumbre y no una acción de ahora."),
        ("En Inglés: ¿qué tiempo usas con now o at the moment?", "El presente continuo (to be + verbo con -ing)", "Esas palabras muestran una acción en progreso."),
        ("En Inglés: ¿cómo preguntas qué hace alguien ahora?", "What is he doing at the moment?", "La pregunta usa is y doing.")],
    op=("Escribe en tu cuaderno cuatro oraciones sobre una persona del trabajo inventado: dos con always o generally y dos con now o at the moment.",
        "Mr. Silva always opens the warehouse at eight. He generally drinks tea at ten. At the moment he is checking the boxes. Now he is talking to a driver.",
        ["usa dos oraciones con presente simple", "usa dos oraciones con presente continuo", "usa la palabra de tiempo correcta"],
        ["cuatro oraciones escritas"],
        ["mezclar la palabra de tiempo con el tiempo equivocado", "olvidar is antes del verbo con -ing"],
        "Pregunta: «¿Qué palabra de tiempo usé en cada oración?»."),
    reinforce="Escribe tres cosas que haces siempre y tres que haces ahora.",
    extend="Escribe cinco preguntas con What is ... doing at the moment? sobre cinco personas inventadas.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: leo la transcripción de un video de ejemplo sobre un trabajo inusual y respondo preguntas.",
    prior=["Distingo el presente simple del presente continuo.", "Entiendo las preposiciones de lugar.", "Sé buscar palabras clave en un texto."],
    explain=[
        "Este módulo no tiene video: trabajamos con la transcripción escrita de un video de ejemplo. Es un límite que declaramos: no se oye la pronunciación, pero se entrena la comprensión del contenido. Otra persona lo lee en voz alta o tú lo lees en voz baja.",
        "Antes de leer, haz una predicción con el título: ¿de qué trabaja la persona? Mientras lees, subraya el nombre del trabajo, el lugar, las palabras de tiempo y lo que hace la persona. Después de leer, responde con lo que dice la transcripción.",
        "En la transcripción hay oraciones de costumbre con generally y always, y una oración de ahora con at the moment. Distinguirlas te ayuda a entender la idea principal y los detalles. There are significa «hay» y se aprende como expresión.",
    ],
    vocab=[("beekeeper", "apicultor o apicultora"), ("smoke", "humo"), ("suit", "traje"), ("hat", "sombrero"), ("thousands of", "miles de"), ("love", "amar, querer mucho")],
    worked=[
        ("Buscar la idea principal", "El video habla de Paula, apicultora, de sus hábitos y de lo que hace ahora.", ["Busco el nombre del trabajo: beekeeper.", "Busco qué hace: trabaja en una granja."], "El tema es un día de trabajo de una apicultora"),
        ("Distinguir costumbre y ahora", "Oraciones: «She always uses smoke» y «She is walking to the boxes».", ["La primera tiene always: costumbre.", "La segunda tiene is walking: ahora."], "Costumbre y acción en progreso"),
    ],
    mistakes=[("Responder lo que supones y no lo que dice el texto.", "La respuesta debe estar en la transcripción.", "Vuelve a leer y subraya la frase que responde."),
              ("Creer que is walking muestra una costumbre.", "Is walking muestra lo que ocurre ahora.", "Mira la palabra de tiempo: at the moment, now.")],
    T=[
        ("abc", "{F} Who is the video about today?", "Paula", "Tom", "Lena", "La transcripción dice Today we meet Paula."),
        ("ab", "{F} What is Paula's job?", "Beekeeper", "Window cleaner", "La transcripción dice que Paula es apicultora."),
        ("abc", "{F} Where does Paula generally work in the morning?", "On a farm", "Inside a cave", "On a tall building", "La transcripción dice She generally works on a farm in the morning."),
        ("abc", "{F} What is Paula doing at the moment?", "Walking to the boxes next to the trees", "Eating lunch at a table", "Cleaning windows", "La transcripción dice que camina hacia las cajas."),
        ("ab", "{F} What is she wearing?", "A white suit and a hat", "A helmet and a coat", "La transcripción dice She is wearing a white suit and a hat."),
        ("{F} What does Paula always use? Write one word.", "smoke", "La transcripción dice She always uses smoke."),
        ("abc", "{F} Why does she love her job?", "Because it is quiet", "Because it is fast", "Because it is far", "Paula dice I love my job because it is quiet."),
        ("abc", "Complete: Paula generally ___ on a farm.", "works", "work", "is working", "Con generally se usa el presente simple con «-s»."),
        ("abc", "Complete: At the moment she ___ to the boxes.", "is walking", "walks", "walk", "At the moment pide el presente continuo."),
        ("ab", "{F} Which sentence is a habit?", "She always uses smoke", "She is walking to the boxes", "Always muestra una costumbre, no una acción que ocurre ahora."),
        ("ab", "{F} Which sentence is true?", "There are thousands of bees inside the boxes", "There are thousands of bees next to the bus", "La transcripción dice que dentro de las cajas hay miles de abejas."),
        ("abc", "{F} What is the main idea of the video?", "A beekeeper's work and why she likes it", "How to clean windows", "How to cook soup", "El video describe el trabajo de una apicultora."),
        ("abc", "Put the words in order: walking / is / Paula / now", "Paula is walking now", "Paula walking is now", "Is walking Paula now", "El orden es sujeto, is y verbo con -ing."),
    ],
    ctx=("abc", "Tu amiga te cuenta por teléfono que su hermano trabaja en un taller y, justo ahora, está pintando una puerta. ¿Qué frase usas para decir lo que hace ahora?", "He is painting a door at the moment", "He paints a door at the moment", "He painting a door at the moment", "At the moment pide to be + verbo con -ing."),
    sc=[("En Inglés: ¿qué haces antes de leer una transcripción?", "Predecir el tema con el título", "Predecir ayuda a entender lo que lees."),
        ("En Inglés: ¿cómo dices que alguien siempre usa humo?", "She always uses smoke", "Always va antes del verbo y con she el verbo lleva «-s»."),
        ("En Inglés: ¿cómo dices que camina ahora?", "She is walking", "El presente continuo usa is y -ing.")],
    op=("Pide a otra persona que lea en voz alta la transcripción y escribe tres datos que entiendas. Después escribe dos oraciones propias sobre el trabajo de Paula: una con always o generally y otra con now o at the moment. {F}",
        "Datos: Paula is a beekeeper. She works on a farm. She wears a white suit. Mis oraciones: She always uses smoke. At the moment she is walking to the boxes.",
        ["escribe tres datos correctos", "una oración con presente simple y otra con presente continuo", "usa un lugar con to, on, inside, next to o at"],
        ["tres datos y dos oraciones escritas"],
        ["inventar datos que no están en la transcripción", "mezclar los dos tiempos"],
        "Pregunta: «¿Qué palabra de tiempo me ayudó a elegir el tiempo?»."),
    reinforce="Lee la transcripción en voz baja y subraya las palabras de tiempo.",
    extend="Escribe cuatro preguntas sobre la transcripción para hacer a otra persona.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido: leo un texto modelo sobre un trabajo inusual y preparo el mío con una estructura clara.",
    prior=["Describo un trabajo con to be y presente simple.", "Uso palabras de lugar.", "Distingo costumbre y ahora."],
    explain=[
        "Un texto breve sobre un trabajo inusual tiene cuatro partes: presenta la persona y el trabajo (My uncle is a lighthouse keeper), dice dónde vive o trabaja, cuenta lo que hace siempre y lo que hace ahora, y termina con una razón (because).",
        "Usa el modelo como guía: copia la estructura y cambia los datos. La palabra but significa «pero» y une dos ideas: His job is unusual because he works alone, but he likes it. Escribe oraciones cortas y claras.",
        "Para evitar errores revisa tres cosas: el verbo con «-s» con he o she, la palabra de tiempo y las preposiciones de lugar. Escribe con datos inventados y no uses nombres ni lugares de personas reales.",
    ],
    vocab=[("lighthouse", "faro"), ("sea", "mar"), ("alone", "solo, sola"), ("fix", "arreglar"), ("town", "pueblo"), ("light", "luz")],
    worked=[
        ("Presentar a la persona", "Quieres decir que un amigo es guardafaros.", ["Uso My friend is.", "Agrego a lighthouse keeper."], "My friend is a lighthouse keeper."),
        ("Cerrar con una razón", "Quieres decir que el trabajo es inusual porque está solo.", ["Escribo His job is unusual.", "Agrego because he works alone."], "His job is unusual because he works alone."),
    ],
    mistakes=[("Escribir «He live next to the sea».", "Con he el verbo live lleva «-s»: lives.", "Revisa el verbo de cada oración con he o she."),
              ("Copiar el modelo sin cambiar los datos.", "Tu texto debe hablar de tu persona inventada.", "Cambia el nombre, el trabajo y el lugar.")],
    T=[
        ("abc", "{F} What is Iván's job?", "He is a lighthouse keeper", "He is a window cleaner", "He is a beekeeper", "El texto dice que Iván es guardafaros."),
        ("ab", "{F} Where does he live?", "Next to the sea", "Inside a cave", "El texto dice He lives next to the sea."),
        ("abc", "{F} What does he always do at night?", "He checks the light", "He goes to the town", "He fixes a window", "El texto dice He always checks the light at night."),
        ("ab", "{F} When does he generally go to the town?", "On Saturdays", "On Mondays", "El texto dice He generally goes to the town on Saturdays."),
        ("abc", "{F} What is he doing at the moment?", "Fixing a window inside the lighthouse", "Checking the light at night", "Going to the town", "El texto dice At the moment he is fixing a window inside the lighthouse."),
        ("abc", "{F} Why is the job unusual?", "Because he works alone", "Because he works at night with many people", "Because it is in a big city", "El texto da la razón: he works alone."),
        ("{F} What is the uncle's first name? Write one word.", "Iván", "El texto dice My uncle Iván."),
        ("abc", "Complete: My uncle always ___ the light at night.", "checks", "check", "is checking", "Con always y he se usa el verbo con «-s»."),
        ("abc", "Complete: At the moment he ___ a window.", "is fixing", "fixes", "fix", "At the moment pide el presente continuo."),
        ("ab", "Which sentence uses a place word?", "He lives next to the sea", "He is happy", "Next to indica el lugar donde vive."),
        ("abc", "Which sentence introduces a job well?", "My cousin is a roof painter", "My cousin painting roof", "My cousin are a painter", "Para presentar un trabajo se usa is, a y el oficio."),
        ("ab", "Complete: The lighthouse is ___ the sea.", "next to", "at to", "En ese contexto next to es la preposición correcta."),
        ("abc", "Put the words in order: always / checks / He / the light", "He always checks the light", "He checks always the light", "Always he the light checks", "Always va antes del verbo y después del sujeto."),
    ],
    ctx=("abc", "Tu vecino te cuenta que su amiga trabaja en un faro. Quieres escribir en tu cuaderno que ella vive al lado del mar. ¿Qué escribes?", "She lives next to the sea", "She live next to the sea", "She lives at to the sea", "Con she el verbo lleva «-s» y next to dice al lado de."),
    sc=[("En Inglés: ¿qué partes tiene el texto sobre un trabajo?", "Presentación, lugar, costumbre y ahora, y razón", "Esas partes hacen un texto completo."),
        ("En Inglés: ¿qué significa «but»?", "Pero", "But une dos ideas que se oponen."),
        ("En Inglés: ¿cómo escribes «Él vive al lado del mar»?", "He lives next to the sea", "Con he el verbo lleva «-s».")],
    op=("Escribe en tu cuaderno un texto de seis oraciones sobre el trabajo inusual de una persona inventada: presentación, lugar, una costumbre con always o generally, una acción con now, y una razón con because. No uses nombres ni datos reales.",
        "My neighbor Elena is a cave guide. She works inside a cave next to a river. She always wears a helmet. She generally starts at nine. At the moment she is talking to visitors. Her job is unusual because she works inside the mountain.",
        ["incluye presentación, lugar y razón", "usa un presente simple y un presente continuo", "usa dos preposiciones de lugar"],
        ["texto escrito de seis oraciones"],
        ["olvidar la «-s» con she", "copiar el modelo sin cambiar datos"],
        "Pregunta: «¿Qué oración muestra mejor lo inusual de este trabajo?»."),
    reinforce="Subraya en el modelo la oración de costumbre y la de ahora.",
    extend="Escribe una segunda versión de tu texto con otro trabajo inusual.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo aprendido: leo la transcripción de otro video de ejemplo, escribo mi texto final sobre un trabajo inusual y decido qué sigo practicando.",
    prior=["Distingo costumbre y ahora.", "Uso palabras de lugar.", "Escribo un texto breve con razón."],
    explain=[
        "Hoy usas todo el módulo: leer la transcripción de un video, subrayar las ideas y escribir tu texto. El video de ejemplo habla de una catadora de té. Se lee igual que el anterior: tema, lugar, costumbre, ahora y razón.",
        "Para revisar tu escritura usa esta lista: nombre y trabajo, lugar con una preposición, una costumbre con always o generally, una acción con now o at the moment, y una razón con because. Marca lo que ya haces bien y lo que quieres mejorar.",
        "Los pasos siguientes son pequeños: ver o leer un video corto en inglés con subtítulos, anotar cinco palabras nuevas y escribir una oración cada día. Aprender inglés de adulto es posible: lo importante es la constancia.",
    ],
    vocab=[("tea taster", "catador o catadora de té"), ("company", "empresa"), ("office", "oficina"), ("taste", "probar el sabor"), ("smell", "oler"), ("coffee", "café")],
    worked=[
        ("Costumbre y ahora en un texto", "Lena prueba veinte tés al día y ahora huele un té verde.", ["Costumbre: tastes twenty teas every day.", "Ahora: is smelling a green tea."], "She tastes twenty teas every day. Right now she is smelling a green tea."),
        ("Dar una razón", "Ella no toma café en el trabajo porque cambia el sabor.", ["Negación con she: doesn't.", "Razón con because."], "She doesn't drink coffee at work because it changes the taste."),
    ],
    mistakes=[("Escribir «Lena don't drink coffee».", "Con she la negación es doesn't.", "Escribe Lena doesn't drink coffee."),
              ("Escribir «She is smell a green tea».", "El presente continuo lleva el verbo con -ing.", "Escribe She is smelling a green tea.")],
    T=[
        ("abc", "{F} What is Lena's job?", "Tea taster", "Window cleaner", "Cave guide", "La transcripción dice que Lena es catadora de té."),
        ("ab", "{F} Where does she work?", "In a small office next to a garden", "Inside a cave", "La transcripción dice que trabaja en una oficina pequeña al lado de un jardín."),
        ("{F} How many teas does she taste every day? Write the number.", "20", "La transcripción dice about twenty teas every day."),
        ("abc", "{F} What time does she generally start?", "At nine", "At six", "At noon", "La transcripción dice She generally starts at nine."),
        ("ab", "{F} What is she doing right now?", "Smelling a green tea", "Drinking coffee", "La transcripción dice Right now she is smelling a green tea."),
        ("abc", "{F} Why doesn't she drink coffee at work?", "Because it changes the taste", "Because she doesn't like tea", "Because coffee is expensive", "Ella dice que el café cambia el sabor."),
        ("abc", "Complete: Lena ___ twenty teas every day.", "tastes", "taste", "is tasting", "Con Lena (she) y every day se usa el presente simple con «-s»."),
        ("abc", "Complete: Right now she ___ a green tea.", "is smelling", "smells", "smell", "Right now pide el presente continuo."),
        ("ab", "Spot the error and choose the correct sentence: «Lena don't drink coffee at work.»", "Lena doesn't drink coffee at work", "Lena doesn't drinks coffee at work", "Con Lena (she) la negación es doesn't y el verbo va sin «-s»."),
        ("abc", "Which is the best title for the video?", "An Unusual Job: Tea Taster", "How to Clean Windows", "A Day on the Bus", "El título debe resumir el tema del video."),
        ("abc", "Which words are time words in the transcription?", "Generally and right now", "Tea and coffee", "Office and garden", "Esas palabras indican costumbre y ahora."),
        ("abc", "Put the words in order: Lena / works / inside / a small office", "Lena works inside a small office", "Lena work inside a small office", "Works Lena a small office inside", "El orden es sujeto, verbo y lugar."),
        ("ab", "Which sentence is a good ending for a text about Lena?", "Her job is unusual because she tastes tea all day", "Her job is unusual because she cleans windows", "El final debe dar una razón que coincida con el trabajo."),
    ],
    ctx=("abc", "En el taller del centro te piden escribir una frase final sobre un trabajo inusual que presentaste: guía de cuevas. ¿Qué frase sirve?", "His job is unusual because he works inside a cave", "His job is unusual because works inside a cave", "His job unusual because he works inside a cave", "La razón con because necesita sujeto y verbo completos."),
    sc=[("En Inglés: ¿puedo presentar a una persona y su trabajo?", "Sí, con to be: She is a tea taster", "Se usa is, a y el nombre del trabajo."),
        ("En Inglés: ¿puedo decir qué hace siempre y qué hace ahora?", "Sí, con presente simple y presente continuo", "Cada tiempo se elige con su palabra de tiempo."),
        ("En Inglés: ¿puedo dar una razón?", "Sí, con because", "Because introduce la razón de algo.")],
    op=("Escribe tu texto final de siete a ocho oraciones sobre un trabajo inusual (real conocido sin nombres, o inventado): presentación, lugar con una preposición, costumbre con always o generally, acción con now, una oración negativa y una razón con because. Léelo en voz alta.",
        "My friend Lucas is a sound recordist. He works outside, next to rivers. He always carries a microphone. He generally starts at six. At the moment he is recording a bird inside a forest. He doesn't use a phone to record. His job is unusual because he listens to nature all day.",
        ["incluye todas las partes", "usa presente simple y presente continuo", "usa dos preposiciones de lugar y una negación"],
        ["texto escrito y leído en voz alta"],
        ["olvidar la «-s» con he o she", "usar datos personales reales"],
        "Pregunta: «¿Qué parte de mi texto me costó más y cómo la voy a practicar?»."),
    reinforce="Revisa tu texto con la lista: trabajo, lugar, costumbre, ahora y razón.",
    extend="Escribe un segundo texto sobre otro trabajo inusual y compáralo con el primero en tres oraciones.",
)
