"""Cuaderno del estudiante, 1.º medio Inglés (propuesta), EN1M OA 09 (estrategias para expresarse con claridad y fluidez).

Los esquemas, diálogos y errores de ejemplo son originales y están escritos en el enunciado, con pista en español.
Las tareas abiertas se practican en voz alta con una persona de tu casa.
"""
from __future__ import annotations

from student_content_en_m1_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA9 = "EN1M OA 09"
MATR = "Los esquemas y diálogos escritos en cada ejercicio; lápiz, hojas y una persona de tu casa para practicar en voz alta."

# ================================================================ OA 09 · clase 1: antes de hablar
DIAG = "Diagrama de ideas (de ejemplo). Centro: «My Town». Rama 1, Places: park, market, school. Rama 2, People: neighbors, teacher. Rama 3, Food: bread, fruit. (town = pueblo, neighbors = vecinos, bread = pan)"

lesson(
    OA9, 1, MATR,
    "Aprenderé a prepararme antes de hablar: practicar, organizar la información clave en un diagrama y hacer conexiones entre ideas. Sirve para hablar con más seguridad y orden.",
    ["Sé el vocabulario básico de mi tema.", "Sé que un esquema ordena las ideas."],
    [
        "Hablar bien en inglés empieza antes de abrir la boca. Primero, organiza la información clave en un diagrama (diagram): escribe el tema en el centro y alrededor las ideas principales con una o dos palabras clave cada una, no oraciones completas.",
        "Segundo, haz conexiones y establece relaciones entre las ideas: ¿qué lugar se relaciona con qué persona?, ¿qué comida se compra en el market? En «My Town», el market (Places) se relaciona con fruit (Food) y con neighbors (People). Esas conexiones te permiten pasar de una idea a otra con naturalidad: «In the market, the neighbors buy bread and fruit».",
        "Tercero, practica la presentación (practice) en voz alta, sola o con una persona de tu casa. Repetir te ayuda a recordar las palabras y a notar qué parte te cuesta. Un diagrama sirve como guía, no como guion para leer. Mira tus palabras clave y habla con tus propias frases. Si olvidas una palabra, el diagrama te devuelve al hilo. Antes de empezar, respira, mira a tu audiencia y decide con qué idea empezarás.",
    ],
    [("practice", "practicar en voz alta"), ("diagram", "diagrama: esquema con el tema al centro"), ("key word", "palabra clave"), ("connection", "conexión entre ideas"), ("organize", "organizar"), ("topic", "tema")],
    [
        ("Armar la conexión", DIAG + " ¿Qué conexión puedes hacer entre «market» y «fruit»?", ["Market está en la rama Places.", "Fruit está en la rama Food.", "En el market se vende fruta."], "En el market se compra fruta (Places se relaciona con Food)"),
        ("Palabra clave", "¿Qué conviene escribir en un diagrama: «park» o «There is a big park near my house where I play»?", ["Un diagrama usa palabras clave.", "Park es una palabra clave.", "La oración larga se dice al hablar."], "«park», porque es una palabra clave"),
    ],
    [
        ("Escribir en el diagrama oraciones completas para leerlas.", "Se vuelve un guion largo.", "Escribe solo palabras clave y habla con tus frases."),
        ("No practicar en voz alta antes de exponer.", "Se cree que basta con pensar.", "Practica en voz alta al menos dos veces."),
    ],
    [
        (DIAG + " ¿Cuántas ramas tiene el diagrama? A) tres B) cinco", "A) tres", "Places, People y Food."),
        (DIAG + " ¿Qué lugares nombra la rama Places?", "Park, market y school", "Son las tres palabras de esa rama."),
        (DIAG + " ¿Qué palabra está en el centro?", "My Town", "El centro lleva el tema."),
    ],
    [
        (DIAG + " ¿En qué rama está «bread»? A) Food B) People", "A) Food", "Bread es pan, un alimento."),
        (DIAG + " ¿Qué conviene hacer antes de hablar? A) practicar en voz alta B) memorizar todo palabra por palabra", "A) practicar en voz alta", "Practicar te ayuda a recordar sin memorizar."),
        (DIAG + " ¿Qué palabra clave de People podrías conectar con school? A) teacher B) bread", "A) teacher", "Un teacher trabaja en una school."),
    ],
    [
        ("Une cada idea con su conexión. 1) market 2) school 3) park Conexiones: a) teacher b) fruit c) families", "1-b, 2-a, 3-c", "Cada lugar se relaciona con personas o alimentos."),
        (DIAG + " Un estudiante dice: «In the market, the neighbors buy bread and fruit.» ¿Qué conexión hace? A) Places con People y Food B) solo Food", "A) Places con People y Food", "Une market, neighbors, bread y fruit."),
        (DIAG + " Quieres añadir una cuarta rama. ¿Cuál se relaciona con el tema? A) Festivals B) Volcanoes of Mars", "A) Festivals", "Los festivales se relacionan con un pueblo."),
    ],
    [
        ("Ordena con letras los pasos de preparación. A) hablar con tus frases usando el diagrama B) practicar en voz alta C) escribir palabras clave en un diagrama", "C, B, A", "Primero organizas, luego practicas y después hablas."),
        ("Un estudiante tiene el diagrama con 40 palabras en cada rama. ¿Qué le recomiendas? A) reducir a una o dos palabras clave por idea B) leer las 120 palabras", "A) reducir a una o dos palabras clave por idea", "Un diagrama muy cargado no ayuda a hablar."),
    ],
    [
        (DIAG + " Si hablas solo de la rama Food, ¿qué palabras usarías? A) bread y fruit B) park y school", "A) bread y fruit", "Son las palabras de esa rama."),
        ("Alguien dice que no necesita practicar porque ya lo escribió. ¿Qué le respondes? A) practicar en voz alta revela partes difíciles B) no hace falta practicar", "A) practicar en voz alta revela partes difíciles", "Escribir no reemplaza hablar."),
    ],
    [("Preparas una charla sobre tu colegio. En tu diagrama escribes: centro «My School»; ramas «Classes», «Friends» y «Sports». ¿Cuántas ramas tiene tu diagrama?", "3", "Hay tres ramas.")],
    [
        ("¿Qué pones en el centro de un diagrama?", "El tema", "Las ideas se organizan alrededor."),
        ("¿Qué escribes en las ramas?", "Palabras clave", "Evitas oraciones largas."),
        ("¿Para qué practicas en voz alta?", "Para recordar y notar lo que cuesta", "Mejora la fluidez."),
    ],
    task("Prepara una charla de 1 minuto sobre «My Favorite Place». Haz un diagrama con el tema al centro y tres ramas (por ejemplo, What I see, Who I go with, Why I like it), cada una con dos palabras clave. Practica en voz alta una vez con una persona de tu casa y anota qué parte se te hizo difícil.", "Centro: My Favorite Place. Ramas: What I see (trees, river), Who I go with (friends, family), Why I like it (quiet, fun). Parte difícil: no recordar la palabra river.", ["el diagrama tiene tema y tres ramas", "usa solo palabras clave", "practica en voz alta y anota una dificultad"], ["hoja con el diagrama", "nota de la persona oyente"], ["escribir oraciones completas", "no practicar en voz alta"], "Valora la organización del diagrama y ayuda a elegir mejores palabras clave."),
    "Vuelve a mirar el diagrama de «My Town» y escribe dos oraciones que conecten las ramas.",
    "Escribe en español un diagrama de ideas sobre tu fin de semana con tres ramas.",
)

# ---------------------------------------------------------------- clase 2: parafrasear, sinónimos y expresiones frecuentes
LIST2 = "Sinónimos de ejemplo: big = large, begin = start, smart = clever, shop = store, quick = fast. Expresiones frecuentes (chunks): «I'd like to talk about…», «As you can see…», «What I mean is…», «In other words…», «As far as I know…». (synonym = sinónimo, chunk = bloque de palabras que se usa junto)"

lesson(
    OA9, 2, MATR,
    "Aprenderé a hablar con claridad usando sinónimos, parafraseo y expresiones frecuentes (chunks). Sirve para no quedarse en blanco cuando olvidas una palabra y para sonar más natural.",
    ["Sé muchas palabras básicas del inglés.", "Sé que una misma idea se puede decir de varias formas."],
    [
        "Parafrasear (to paraphrase) es decir la misma idea con otras palabras. Si olvidas la palabra umbrella, puedes decir «the thing you open when it rains». Con ese rodeo, tu mensaje se entiende y la conversación continúa. Un sinónimo (synonym) es una palabra con un significado parecido: big y large, begin y start, quick y fast. Conocer un par de sinónimos te da alternativas cuando una palabra se te escapa.",
        "Los chunks son bloques de palabras que se usan juntos y se aprenden como una unidad: I'd like to talk about…, As you can see…, What I mean is…, In other words…, As far as I know…. Con los chunks hablas más rápido porque no armas la frase palabra por palabra. In other words… y What I mean is… son especialmente útiles para parafrasear cuando alguien no te entendió.",
        "Una buena estrategia: si no sabes una palabra, piensa en 1) un sinónimo que conozcas, 2) una descripción de para qué sirve o cómo es, y 3) un chunk que te dé tiempo. Por ejemplo: «What I mean is… the thing you open when it rains». Practica con tres palabras al día.",
    ],
    [("paraphrase", "parafrasear: decir lo mismo con otras palabras"), ("synonym", "sinónimo: palabra de significado parecido"), ("chunk", "bloque de palabras que va junto"), ("In other words…", "En otras palabras…"), ("What I mean is…", "Lo que quiero decir es…"), ("As far as I know…", "Hasta donde sé…")],
    [
        ("Sinónimo", LIST2 + " ¿Qué sinónimo de «big» puedes usar?", ["Busco big en la lista.", "Aparece big = large.", "Large significa grande."], "Large"),
        ("Parafrasear", "Olvidaste la palabra «umbrella». ¿Cómo la describes en inglés con palabras sencillas?", ["Pienso para qué sirve.", "Se abre cuando llueve.", "Lo digo: the thing you open when it rains."], "The thing you open when it rains"),
    ],
    [
        ("Quedarse en silencio cuando se olvida una palabra.", "Se piensa que no se puede continuar.", "Parafrasea: describe la palabra o usa un sinónimo."),
        ("Traducir un chunk palabra por palabra.", "Se pierde el sentido.", "Aprende el bloque completo: As far as I know…"),
    ],
    [
        (LIST2 + " ¿Qué significa «begin»? A) empezar B) terminar", "A) empezar", "Begin es un sinónimo de start."),
        (LIST2 + " ¿Qué sinónimo hay para «quick»?", "Fast", "La lista dice quick = fast."),
        (LIST2 + " ¿Qué chunk usas para decir «como puedes ver»? A) As you can see… B) In other words…", "A) As you can see…", "Es la expresión para señalar algo visible."),
    ],
    [
        (LIST2 + " ¿Qué chunk usas para explicar otra vez lo mismo con otras palabras? A) In other words… B) I'd like to talk about…", "A) In other words…", "Introduce una reformulación."),
        (LIST2 + " ¿Qué sinónimo corresponde a «shop»? A) store B) smart", "A) store", "La lista dice shop = store."),
        ("Olvidaste la palabra «ladder» (escalera de mano). ¿Qué descripción sirve? A) the tool you climb to reach high places B) the tool you use to cut paper", "A) the tool you climb to reach high places", "Describe su uso con palabras simples."),
    ],
    [
        ("Completa con el chunk: «____ , it is a big city.» (hasta donde sé) A) As far as I know B) As you can see", "A) As far as I know", "Se usa cuando no estás seguro de un dato."),
        ("Completa con un sinónimo de smart: «My sister is very ____ .» A) clever B) tired", "A) clever", "Clever es un sinónimo de smart."),
        ("Une cada situación con la frase que ayuda. 1) quieres introducir tu tema 2) quieres reformular 3) señalas un gráfico Frases: a) In other words… b) I'd like to talk about… c) As you can see…", "1-b, 2-a, 3-c", "Cada chunk cumple una función."),
    ],
    [
        ("Una persona no entendió «The weather is chilly». Tú dices: «What I mean is, it is a little cold.» ¿Qué estrategia usas? A) parafrasear B) cambiar de tema", "A) parafrasear", "Dices lo mismo con otras palabras."),
        ("Un estudiante dice «My cat is large». Otra forma de decir lo mismo es: A) My cat is big B) My cat is tiny", "A) My cat is big", "Large y big son sinónimos."),
    ],
    [
        ("Un estudiante olvidó «fridge» y dijo «the machine that keeps food cold». ¿Qué estrategia usó? A) describir la función B) usar un sinónimo exacto", "A) describir la función", "Explicó para qué sirve."),
        ("Quieres explicar «sandcastle» sin saber la palabra. ¿Cuál descripción es más clara? A) a house made of sand on the beach B) something I like", "A) a house made of sand on the beach", "Da características concretas."),
    ],
    [("Alguien te pregunta «What is a ‘bakery’?» y respondes: «A shop where people buy bread.» ¿Qué estrategia usas?", "Parafrasear con una descripción", "Defines la palabra con otras palabras.")],
    [
        ("En Inglés: ¿Qué significa parafrasear?", "Decir lo mismo con otras palabras", "Evita quedarse en blanco."),
        ("¿Qué es un chunk?", "Un bloque de palabras que se usa junto", "Ayuda a hablar con fluidez."),
        ("¿Qué chunk introduce una reformulación?", "In other words…", "Reformula lo dicho."),
    ],
    task("Explica en inglés, con palabras sencillas y sin decir la palabra, estos tres objetos a una persona de tu casa: 1) a clock, 2) a key, 3) a bicycle. Usa al menos un chunk (What I mean is… o In other words…) y un sinónimo (big = large, quick = fast). Escribe en tu hoja las tres descripciones.", "1) A clock is the thing on the wall that shows the time. 2) A key is a small object that opens a door. In other words, you need it to enter a house. 3) A bicycle is a vehicle with two wheels; it is quick and you ride it.", ["describe sin nombrar el objeto", "usa un chunk y un sinónimo", "la persona adivina al menos dos objetos"], ["hoja con tres descripciones", "nota de la persona oyente"], ["decir la palabra en español", "dar una descripción demasiado vaga"], "Valora las descripciones claras y mejora las vagas con un detalle concreto."),
    "Vuelve a leer la lista de sinónimos y escribe una oración en inglés con cada uno.",
    "Escribe en español tres palabras en inglés que olvidas con frecuencia y cómo las describirías.",
)

# ---------------------------------------------------------------- clase 3: rellenos, conectores y autocorrección
FILL = "Diálogo (de ejemplo). Ana: «What did you do yesterday?» Luis: «Well... I go... I mean, I went to the beach. It was... let me think... very windy.» Ana: «I see. Did you swim?» Luis: «No, but I... sorry, I played football on the sand. Then, after that, I had ice cream.» (windy = ventoso, sand = arena, ice cream = helado)"

lesson(
    OA9, 3, MATR,
    "Aprenderé a usar rellenos temporales (I mean…, I see…, well…, let me think), conectores y a autocorregirme al hablar. Sirve para ganar tiempo para pensar, mantener el hilo y corregir sin ponerte nervioso.",
    ["Sé el pasado simple.", "Sé conectores como then y after that."],
    [
        "Los rellenos temporales (fillers) son palabras o frases cortas que dices mientras piensas: Well…, Let me think…, I mean…, I see…, You know…. No son errores si se usan con moderación: muestran que estás pensando y evitan silencios largos. I see… también se usa para mostrar que entendiste lo que dijo la otra persona.",
        "Los conectores mantienen el hilo del discurso: then, after that, but, so, because. Autocorregirse (to self-correct) es corregir tú mismo un error al hablar. Se hace con frases como I mean…, sorry… o let me say that again: «I go... I mean, I went to the beach». Corregirte a tiempo demuestra que sabes la forma correcta.",
        "Para usar bien estas estrategias: no abuses de los rellenos (uno o dos por oración), usa conectores para unir ideas y corrige un error apenas lo notes, sin disculparte demasiado. Después de corregir, continúa con la idea. Una pausa corta, con un relleno, es mejor que un silencio largo.",
    ],
    [("filler", "relleno: palabra para ganar tiempo"), ("I mean…", "quiero decir… (para corregirse o aclarar)"), ("I see…", "ya veo…"), ("let me think", "déjame pensar"), ("self-correct", "autocorregirse"), ("connector", "conector: then, so, because")],
    [
        ("Autocorrección", FILL + " ¿Cuál fue el error de Luis y cómo lo corrigió?", ["Luis dice I go, que está en presente.", "Se da cuenta y dice I mean, I went.", "Corrige el verbo al pasado."], "Dijo «I go» y se corrigió con «I mean, I went»"),
        ("Relleno", FILL + " ¿Qué frase usa Luis para ganar tiempo antes de describir el viento?", ["Busco una frase de pensamiento.", "Dice let me think.", "Sirve para ganar tiempo."], "Let me think"),
    ],
    [
        ("Llenar cada oración con muchos rellenos.", "Se usan como muletilla.", "Usa uno o dos y haz una pausa corta."),
        ("Quedarse callado después de un error.", "Se siente vergüenza.", "Corrige con I mean… y continúa."),
    ],
    [
        (FILL + " ¿Adónde fue Luis ayer? A) a la playa B) al cine", "A) a la playa", "Dice I went to the beach."),
        (FILL + " ¿Qué dice Ana para mostrar que entendió? A) I see B) Sorry", "A) I see", "I see significa ya veo."),
        (FILL + " ¿Qué comió Luis después? A) helado B) pan", "A) helado", "Dice I had ice cream."),
    ],
    [
        (FILL + " ¿Qué conectores usa Luis al final? A) Then, after that B) Because, so", "A) Then, after that", "Ordenan lo que hizo."),
        (FILL + " ¿Qué jugó Luis en la arena? A) fútbol B) tenis", "A) fútbol", "Dice I played football on the sand."),
        ("Une cada frase con su función. 1) I mean… 2) I see… 3) Let me think… Funciones: a) ganar tiempo b) corregirse o aclarar c) mostrar que entendiste", "1-b, 2-c, 3-a", "Cada relleno cumple una función."),
    ],
    [
        ("Completa para autocorregirte: «She go... I mean, she ____ to school.» A) goes B) going", "A) goes", "En tercera persona del presente se agrega -s."),
        ("Completa para ganar tiempo: «____ ... I think the answer is B.» A) Let me think B) Thank you very much", "A) Let me think", "Es un relleno temporal."),
        ("Ordena las frases con letras para una corrección natural. A) I went to the park. B) I go... C) I mean...", "B, C, A", "Primero el error, luego la frase de corrección y al final la forma correcta."),
    ],
    [
        ("Un estudiante dice «I have... well... let me think... ten brothers» y se detiene. ¿Qué podría hacer? A) usar I mean y corregir el dato B) quedarse en silencio", "A) usar I mean y corregir el dato", "Corregir mantiene la conversación."),
        ("¿Cuál uso de los rellenos es mejor? A) un relleno y una pausa corta B) un relleno en cada palabra", "A) un relleno y una pausa corta", "La moderación hace el discurso natural."),
    ],
    [
        (FILL + " Luis dice «No, but I... sorry, I played football». ¿Qué hace con «sorry»? A) se interrumpe para corregir su respuesta B) se disculpa por faltar", "A) se interrumpe para corregir su respuesta", "Sorry marca que cambia lo que iba a decir."),
        (FILL + " ¿Cuántas veces se corrige Luis a sí mismo? A) dos veces B) una vez", "A) dos veces", "Se corrige con I mean (I go → I went) y con sorry (cambia lo que iba a decir)."),
    ],
    [("Dices «I eat breakfast... I mean, I ate breakfast at seven.» ¿Qué corriges?", "El tiempo del verbo: de presente a pasado", "Cambias eat por ate para hablar del pasado.")],
    [
        ("En Inglés: ¿Para qué sirven los rellenos?", "Para ganar tiempo al pensar", "Evitan silencios largos."),
        ("¿Qué frase sirve para autocorregirse?", "I mean…", "Introduce la forma correcta."),
        ("¿Qué indica I see…?", "Que entendiste lo que dijeron", "Así muestras que comprendiste."),
    ],
    task("Escribe y practica en voz alta con una persona de tu casa un minidiálogo de 4 turnos en inglés sobre qué hiciste ayer. Incluye al menos un relleno (well…, let me think…, I see…), una autocorrección con I mean… y dos conectores (then, after that, so o because). Anota en tu hoja el diálogo.", "A: What did you do yesterday? B: Well... I go... I mean, I went to my grandmother's house. A: I see. And then? B: After that, I helped her cook, so we ate together.", ["incluye un relleno y una autocorrección", "usa dos conectores", "dice el diálogo en voz alta"], ["hoja con el diálogo", "nota de la persona oyente"], ["no incluir autocorrección", "usar rellenos en todas las oraciones"], "Valora la naturalidad y ayuda a reducir los rellenos si son demasiados."),
    "Vuelve a leer el diálogo de Ana y Luis y subraya con colores los rellenos, las autocorrecciones y los conectores.",
    "Escribe en español dos situaciones en que usarías let me think y dos en que usarías I mean.",
)

# ---------------------------------------------------------------- clase 4: apoyo visual y vacío de información
MAP = "Mapa de un barrio (de ejemplo): al norte está la biblioteca; en el centro, la plaza; al sur, la piscina; al este, la feria; al oeste, el colegio. La persona A mira el mapa; la persona B no lo ve y pregunta. (library = biblioteca, square = plaza, pool = piscina, market = feria, school = colegio)"
TABLE4 = "Tabla de horarios (de ejemplo): Lunes, taller de arte, 4 p.m. Martes, taller de música, 5 p.m. Jueves, taller de teatro, 4 p.m. (art = arte, music = música, theater = teatro)"

lesson(
    OA9, 4, "Un mapa y una tabla de horarios escritos en cada ejercicio; en la práctica real una persona (A) mira el recurso y la otra (B) pregunta; lápiz y hoja.",
    "Aprenderé a usar apoyo visual en distintos formatos (mapa, tabla, imagen) al hablar y a resolver un vacío de información: una persona tiene el dato y la otra lo pregunta. Sirve para dar indicaciones, explicar horarios y comprobar que se entendió.",
    ["Sé las preguntas Where is…? y When is…?", "Sé los puntos cardinales en inglés."],
    [
        "El apoyo visual (visual support) puede ser un mapa, una tabla, una foto o un gráfico. Se usa con frases que lo señalan: As you can see…, Here you can see…, This picture shows…, On the map…. Mientras dices la frase, apunta con el dedo o con un lápiz al lugar. Así la audiencia une lo que oye con lo que ve.",
        "En un vacío de información, una persona (A) tiene el apoyo visual y la otra (B) no. B pregunta: Where is the pool? A responde mirando el mapa: The pool is in the south. Para confirmar, B repite: So, the pool is in the south, right? Los puntos cardinales en inglés son north, south, east y west; el centro es the center. Para horarios, se usa On Monday at four.",
        "Cuando uses un apoyo visual, asegúrate de que lo que dices coincide con lo que se ve. Si apuntas al norte y dices south, la audiencia se confunde. Antes de hablar, practica la descripción del recurso con una persona de tu casa y pídele que repita lo que entendió.",
    ],
    [("visual support", "apoyo visual: mapa, tabla, imagen"), ("north / south / east / west", "norte / sur / este / oeste"), ("As you can see…", "Como puedes ver…"), ("Where is…?", "¿Dónde está…?"), ("On Monday at four", "El lunes a las cuatro"), ("point to", "apuntar a")],
    [
        ("Describir con el mapa", MAP + " Alguien pregunta «Where is the pool?». ¿Qué respondes en inglés?", ["Busco la piscina en el mapa.", "Está al sur.", "Digo: The pool is in the south."], "The pool is in the south"),
        ("Leer una tabla", TABLE4 + " Alguien pregunta «When is the music workshop?». ¿Qué respondes?", ["Busco música en la tabla.", "Es el martes a las cinco.", "Digo: On Tuesday at five."], "On Tuesday at five (el martes a las cinco)"),
    ],
    [
        ("Decir una dirección que no coincide con lo que se ve en el mapa.", "No se mira el recurso al hablar.", "Mira el mapa y apunta mientras hablas."),
        ("Responder sin confirmar lo que entendió la otra persona.", "Se da por hecho que se entendió.", "Pregunta So, …, right? para confirmar."),
    ],
    [
        (MAP + " ¿Qué hay al norte? A) la biblioteca B) la piscina", "A) la biblioteca", "El mapa dice que al norte está la biblioteca."),
        (MAP + " ¿Qué hay en el centro?", "La plaza", "El mapa dice que en el centro está la plaza."),
        (TABLE4 + " ¿A qué hora es el taller de teatro? A) a las cuatro B) a las cinco", "A) a las cuatro", "Dice jueves, taller de teatro, 4 p.m."),
    ],
    [
        (MAP + " ¿Qué hay al oeste? A) el colegio B) la feria", "A) el colegio", "El mapa dice que al oeste está el colegio."),
        (MAP + " ¿Cómo se dice «east» en español? A) este B) oeste", "A) este", "East es este; west es oeste."),
        (TABLE4 + " ¿Qué taller es el lunes? A) arte B) música", "A) arte", "La tabla dice lunes, taller de arte."),
    ],
    [
        (MAP + " B pregunta «Where is the market?». ¿Cuál es una buena respuesta de A? A) The market is in the east. B) The market is in the north.", "A) The market is in the east.", "El mapa dice que la feria está al este."),
        (TABLE4 + " B dice: «So, the art workshop is on Monday at four, right?» ¿Qué responde A? A) Yes, that's right. B) No, it's on Friday.", "A) Yes, that's right.", "El dato de B coincide con la tabla."),
        ("Une cada frase con su uso. 1) As you can see… 2) So, …, right? 3) Where is…? Usos: a) confirmar lo entendido b) preguntar un lugar c) señalar un recurso visual", "1-c, 2-a, 3-b", "Cada frase cumple una función en el intercambio."),
    ],
    [
        (MAP + " A dice «The school is in the east». ¿Qué parte del mapa lo corrige? A) el colegio está al oeste B) la feria está al sur", "A) el colegio está al oeste", "El mapa lo ubica al oeste."),
        (TABLE4 + " B dice «The theater workshop is on Wednesday». ¿Qué día es en realidad? A) jueves B) viernes", "A) jueves", "La tabla dice jueves, taller de teatro."),
    ],
    [
        (MAP + " A debe dar indicaciones de la plaza a la piscina. ¿Qué dirección es? A) hacia el sur B) hacia el norte", "A) hacia el sur", "La plaza está en el centro y la piscina al sur."),
        (TABLE4 + " Si un estudiante quiere asistir a los talleres de arte y teatro, ¿cuántas veces va en la semana? A) dos B) tres", "A) dos", "Arte (lunes) y teatro (jueves) son dos días."),
    ],
    [(MAP + " ¿Qué lugar queda al este de la plaza?", "La feria", "El mapa dice que al este está la feria.")],
    [
        ("¿Qué es un apoyo visual?", "Un mapa, tabla o imagen que refuerza lo que digo", "Ayuda a la audiencia."),
        ("¿Cómo se dice «oeste» en inglés?", "West", "Es el punto cardinal opuesto a east."),
        ("¿Qué frase confirma lo que entendiste?", "So, …, right?", "Repite el dato para verificarlo."),
    ],
    task("Dibuja un mapa simple de tu cuadra o de tu casa con cuatro lugares y los puntos cardinales (por ejemplo, la cocina al norte). Con una persona de tu casa que no ve el mapa, tú eres A y ella B: ella pregunta Where is…? por dos lugares; tú respondes en inglés y ella confirma con So, …, right? Anota en tu hoja las preguntas y respuestas.", "B: Where is the kitchen? A: The kitchen is in the north. B: So, the kitchen is in the north, right? A: Yes, that's right.", ["el mapa tiene cuatro lugares", "responde en inglés con los puntos cardinales", "confirma el dato con la otra persona"], ["hoja con el mapa", "nota de la persona oyente"], ["cambiar los puntos cardinales", "no confirmar"], "Valora la coincidencia entre lo que dice y lo que muestra el mapa."),
    "Vuelve a mirar el mapa del barrio y escribe tres frases con As you can see.",
    "Escribe en español dos situaciones en que usarías un mapa o una tabla para explicar algo.",
)

# ---------------------------------------------------------------- clase 5: después de hablar
ERR = "Registro de errores de ejemplo (frases dichas por un estudiante): 1) «I have 15 years.» 2) «She go to school at eight.» 3) «I am agree with you.» 4) «People is happy.» 5) «I live here since five years.» (years = años, agree = estar de acuerdo, happy = contentos, since = desde, for = durante)"

lesson(
    OA9, 5, MATR,
    "Aprenderé a evaluar mi forma de hablar después de hacerlo: identificar mis debilidades, registrar mis errores y corregirlos con ayuda de recursos (diccionario, apuntes). Sirve para mejorar con cada práctica.",
    ["Sé usar un diccionario o mis apuntes.", "Sé que equivocarse es parte de aprender."],
    [
        "Después de hablar, haz una revisión (review). Primero identifica tus debilidades (weaknesses): ¿qué sonidos, palabras o estructuras te costaron?, ¿dónde te quedaste en blanco? Segundo, registra tus errores en una lista (error log): escribe la frase como la dijiste y la forma correcta. Tercero, busca ayuda en recursos: diccionario, apuntes de clase, tabla de verbos o una persona que pueda explicarte.",
        "Algunos errores frecuentes de quienes hablan español son: «I have 15 years» (se dice I am 15 years old), «She go» (con he, she, it el verbo lleva -s: she goes), «I am agree» (se dice I agree, sin am), «People is» (people es plural: people are) y «since five years» (con un período se usa for: for five years; since se usa con un punto de inicio, como since 2020).",
        "Para corregir un error de forma duradera, escribe la forma correcta en una oración completa y repítela en voz alta tres veces. Cada semana revisa tu lista y elimina los errores que ya no cometes. Marca con una estrella los que se repiten: esos son tus prioridades de práctica.",
    ],
    [("review", "revisión después de hablar"), ("weakness", "debilidad: lo que me cuesta"), ("error log", "registro de errores"), ("correct form", "forma correcta"), ("dictionary", "diccionario"), ("priority", "prioridad")],
    [
        ("Corregir un error", ERR + " Corrige el error 2.", ["La oración es She go to school.", "Con she, el verbo lleva -s.", "Queda: She goes to school at eight."], "She goes to school at eight."),
        ("Elegir for o since", ERR + " Corrige el error 5.", ["Five years es un período.", "Con un período se usa for.", "Queda: I have lived here for five years."], "I have lived here for five years."),
    ],
    [
        ("Corregir sin escribir la forma correcta.", "El cambio se olvida.", "Anota error y forma correcta en tu lista."),
        ("Pensar que los errores indican que no sabes inglés.", "Se ve el error como un fracaso.", "Los errores muestran qué practicar."),
    ],
    [
        (ERR + " ¿Cuál es la forma correcta del error 1? A) I am 15 years old. B) I have 15 years.", "A) I am 15 years old.", "En inglés la edad se dice con be, no con have."),
        (ERR + " ¿Cuál es la forma correcta del error 3? A) I agree with you. B) I am agree with you.", "A) I agree with you.", "Agree es un verbo; no lleva am."),
        (ERR + " ¿Qué es un error log?", "Una lista de errores con su forma correcta", "Sirve para revisar tus avances."),
    ],
    [
        (ERR + " ¿Cuál es la forma correcta del error 4? A) People are happy. B) People is happy.", "A) People are happy.", "People es plural."),
        (ERR + " ¿Qué recurso usarías para verificar «agree»? A) un diccionario B) una tabla de horarios", "A) un diccionario", "Muestra cómo se usa la palabra."),
        (ERR + " ¿En cuál error el problema es el verbo en tercera persona? A) She go to school B) I have 15 years", "A) She go to school", "Con she, el verbo lleva -s."),
    ],
    [
        arith(ERR + " Un estudiante registra 5 errores y corrige 3 en la semana. ¿Cuántos le quedan por corregir?", "5-3", "Se resta lo corregido de lo registrado."),
        ("Une cada error con su corrección. 1) I am agree. 2) People is. 3) She go. Correcciones: a) She goes. b) I agree. c) People are.", "1-b, 2-c, 3-a", "Cada corrección cambia la forma incorrecta."),
        ("Ordena los pasos de la pos hablada con letras. A) corregir con un recurso B) registrar el error C) identificar una debilidad", "C, B, A", "Primero identificas, luego registras y después corriges."),
    ],
    [
        (ERR + " Un estudiante usa since en «I live here since 2020». ¿Es correcta? A) Hay que decir: I have lived here since 2020. B) Está bien como está.", "A) Hay que decir: I have lived here since 2020.", "Con since y un punto de inicio se usa el presente perfecto."),
        ("¿Qué error es más urgente de corregir si lo repites en cada frase? A) el que se repite siempre B) el que ocurrió una sola vez", "A) el que se repite siempre", "Un error repetido es una prioridad."),
    ],
    [
        ("Un estudiante escribe en su lista: «I go yesterday → I went yesterday». ¿Qué aprende? A) el pasado de go es went B) el pasado de go es goed", "A) el pasado de go es went", "Go es irregular y su pasado es went."),
        (ERR + " ¿Cuál de los cinco errores se corrige cambiando since por for? A) el número 5 B) el número 1", "A) el número 5", "Five years es un período y con un período se usa for."),
    ],
    [("Un estudiante dice «Yesterday I buyed a book». ¿Cómo lo corrige en su lista?", "Yesterday I bought a book.", "El pasado de buy es bought, un verbo irregular.")],
    [
        ("¿Qué haces después de hablar para mejorar?", "Identificar debilidades y registrar errores", "Así sabes qué practicar."),
        ("¿Qué recursos ayudan a corregir?", "Diccionario, apuntes y una persona que explique", "Dan la forma correcta."),
        ("¿Qué error se debe priorizar?", "El que se repite más", "Mejorarlo da más resultado."),
    ],
    task("Después de decir en voz alta una presentación de 1 minuto sobre tu día a una persona de tu casa, haz un registro con tres columnas: 1) lo que dije, 2) la forma correcta, 3) el recurso que usé (diccionario, apuntes o persona). Anota tres errores o dudas, aunque sean pequeños, y repite en voz alta cada forma correcta tres veces.", "1) «I go to school yesterday» / I went to school yesterday / apuntes de verbos irregulares. 2) «I have 15 years» / I am 15 years old / diccionario. 3) «She like music» / She likes music / apuntes.", ["anota tres errores o dudas con su forma correcta", "indica un recurso para cada uno", "repite en voz alta las formas correctas"], ["hoja con el registro", "nota de la persona oyente"], ["anotar solo el error sin corrección", "no repetir en voz alta"], "Valora el registro completo y revisa que las correcciones sean correctas."),
    "Vuelve al registro de errores y reescribe las cinco frases correctas en tu cuaderno.",
    "Escribe en español dos debilidades que notes en tu forma de hablar inglés y un recurso para mejorar cada una.",
)
