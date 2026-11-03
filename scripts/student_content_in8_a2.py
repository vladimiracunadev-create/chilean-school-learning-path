"""Cuaderno del estudiante, 8.º básico Inglés (oficial), IN08 OA 02 (lenguaje clave y sonidos inteligibles al escuchar).

Las «escuchas» las lee un adulto; las clases de sonidos traen las palabras escritas y se practican con una persona adulta.
"""
from __future__ import annotations

from student_content_in8_a import ADULT, MAT_L, lesson
from student_content_ma01_b import task

OA2 = "IN08 OA 02"
MAT_S = "Lápiz, una hoja y una persona adulta que pronuncie contigo; los ejercicios traen las palabras escritas."

CHAT1 = "«Rosa: Excuse me, how do I get to the library? Guard: Catch the number 8 bus and get off at the square. Rosa: That's OK, thanks. Guard: Let's hope it comes soon. Look at the board: it says five minutes.» (guard = guardia, catch = tomar, get off = bajarse, square = plaza, hope = esperar que, board = pizarra, minutes = minutos)"
CHAT2 = "«Hi Ian, I'm tired of waiting for slow videos. Maybe we can download the lesson tonight and watch it tomorrow at school. Let's ask Mr. Ruiz if that's possible.» (tired of = cansado de, slow = lentos, download = descargar, lesson = clase, tonight = esta noche, possible = posible)"
CHAT3 = "«Get on the bus at the front door, show your card and find a seat. When the bus reaches your street, press the red button and get off by the back door.» (front = delantera, card = tarjeta, seat = asiento, reaches = llega a, press = aprieta, button = botón, back = trasera)"

lesson(
    OA2, 1, MAT_L,
    "Aprenderé a reconocer palabras clave y expresiones de uso frecuente (catch, get off, tired of, let's, maybe) al escuchar. Sirve para entender mensajes aunque no conozcas todas las palabras.",
    ["Sé que no hace falta entender cada palabra para entender un mensaje.", "Conozco palabras de transporte como bus y station."],
    [
        "Las palabras clave (key words) son las que más información entregan: sustantivos, verbos, números y adjetivos importantes, como bus, download, five minutes o red button. Las palabras pequeñas, como the, of y to, ayudan, pero casi nunca son la clave. Al escuchar, atiende primero las palabras clave y úsalas para entender el resto.",
        "Una expresión de uso frecuente (chunk) es un grupo de palabras que se aprende junto. Ejemplos: catch a bus (tomar un bus), get on / get off the bus (subir / bajar del bus), look at (mirar), tired of (cansado de), maybe (quizás), that's OK (está bien) y let's + verbo (hagamos algo juntos). Si reconoces el grupo completo, entiendes más rápido que traduciendo palabra por palabra.",
        "El vocabulario temático (thematic vocabulary) son las palabras de un mismo tema. En el tema transporte aparecen bus, station, ticket, card, seat, platform y street. Cuando oyes varias palabras del mismo tema, ya sabes de qué se habla y puedes adivinar mejor las palabras desconocidas.",
    ],
    [("key words", "palabras clave: las que más información dan"), ("chunk", "expresión de uso frecuente: grupo de palabras que van juntas"), ("catch a bus", "tomar un bus"), ("get on / get off", "subirse / bajarse"), ("tired of", "cansado de"), ("let's", "hagamos algo juntos"), ("maybe", "quizás")],
    [
        ("Entender dos expresiones", ADULT + CHAT1 + " ¿Qué le dice el guardia a Rosa que haga?", ["Catch the number 8 bus significa tomar el bus 8.", "Get off at the square significa bajarse en la plaza.", "Junto las dos expresiones."], "Que tome el bus 8 y se baje en la plaza"),
        ("Elegir palabras clave", "Un adulto lee: «Maybe we can download the lesson tonight.» (download = descargar, lesson = clase, tonight = esta noche). ¿Cuáles son las palabras clave que hay que anotar?", ["Busco palabras con mucha información.", "Download, lesson y tonight dicen qué acción, qué cosa y cuándo.", "Maybe agrega que es una posibilidad."], "Download, lesson, tonight y maybe"),
    ],
    [
        ("Traducir catch como «atrapar» en catch a bus.", "Catch tiene varios significados y aquí forma parte de la expresión tomar un bus.", "Aprende catch a bus como un grupo y no palabra por palabra."),
        ("Pensar que maybe significa «seguro».", "Maybe indica una posibilidad, no una certeza.", "Recuerda: maybe es quizás o tal vez."),
    ],
    [
        (ADULT + CHAT1 + " ¿Qué significa «Catch the number 8 bus»? a) toma el bus número 8 b) atrapa el bus 8 mientras corre", "a) toma el bus número 8", "Catch a bus es una expresión que significa tomar un bus."),
        (ADULT + CHAT1 + " ¿Qué significa «get off at the square»? a) bájate en la plaza b) súbete en la plaza", "a) bájate en la plaza", "Get off es bajarse; get on es subirse."),
        (ADULT + CHAT2 + " ¿Qué significa «tired of waiting»? a) cansada de esperar b) con ganas de esperar", "a) cansada de esperar", "Tired of expresa que algo ya cansa o molesta."),
    ],
    [
        (ADULT + CHAT2 + " ¿Qué quiere hacer la persona con la clase? a) descargarla esta noche b) dibujarla mañana c) borrarla del computador", "a) descargarla esta noche", "Download es descargar y tonight es esta noche."),
        (ADULT + CHAT2 + " ¿Qué muestra la palabra «Maybe»? a) que es una posibilidad, no una certeza b) que la persona está completamente segura", "a) que es una posibilidad, no una certeza", "Maybe significa quizás."),
        (ADULT + CHAT1 + " ¿Qué hay que hacer con «Look at the board»? a) mirar el tablero para ver los minutos b) escribir en el tablero", "a) mirar el tablero para ver los minutos", "Look at es mirar, y el tablero dice cinco minutos."),
    ],
    [
        (ADULT + CHAT3 + " ¿Por qué puerta hay que bajar? a) por la trasera b) por la delantera", "a) por la trasera", "Dice get off by the back door."),
        (ADULT + CHAT3 + " ¿Qué hay que hacer para avisar que quieres bajar? a) apretar el botón rojo b) mostrar la tarjeta", "a) apretar el botón rojo", "Press the red button avisa la parada; la tarjeta se muestra al subir."),
        (ADULT + "«Please bring a notebook and two pencils to room twelve.» (bring = traer, notebook = cuaderno, pencils = lápices, room = sala). ¿Cuál palabra ayuda más a saber qué llevar? a) pencils b) please", "a) pencils", "Pencils nombra un objeto; please solo es una fórmula de cortesía."),
    ],
    [
        (ADULT + CHAT1 + " Rosa dice «That's OK, thanks». ¿Qué significa en esa situación? a) acepta la indicación y agradece b) rechaza la ayuda", "a) acepta la indicación y agradece", "That's OK aquí es una respuesta amable, y thanks es gracias."),
        (ADULT + CHAT2 + " ¿Qué hace la frase «Let's ask Mr. Ruiz»? a) propone preguntar juntos al profesor b) prohíbe preguntar", "a) propone preguntar juntos al profesor", "Let's + verbo invita a hacer algo en grupo."),
    ],
    [
        (ADULT + CHAT1 + " Iván entendió «baja en la biblioteca» y Rita entendió «baja en la plaza». ¿Quién tiene razón? a) Rita, porque el guardia dice get off at the square b) Iván, porque Rosa va a la biblioteca", "a) Rita, porque el guardia dice get off at the square", "La biblioteca es el destino; la plaza es dónde bajarse."),
        (ADULT + "«The bus station is next to the park.» (next to = junto a, park = parque). Un oyente solo entendió «bus station» y «park». ¿Qué logra saber? a) que habla de un lugar de transporte cerca de un parque b) que habla de comprar pasajes", "a) que habla de un lugar de transporte cerca de un parque", "Esas dos palabras clave bastan para saber el tema y el lugar."),
    ],
    [(ADULT + "En un paradero oyes: «Excuse me, does this bus go to the stadium? Yes, get on here and show your card.» (stadium = estadio, card = tarjeta). ¿Qué debes hacer para viajar? a) subir ahí y mostrar la tarjeta b) esperar otro bus", "a) subir ahí y mostrar la tarjeta", "Get on here es subir ahí y show your card es mostrar la tarjeta.")],
    [
        ("En Inglés de 8.º (OA 2, clase 1): ¿Qué es un chunk?", "Un grupo de palabras que se aprende junto", "Por ejemplo, tired of o catch a bus."),
        ("¿Qué significa «tired of»?", "Cansado de", "Expresa que algo ya cansa."),
        ("¿Qué palabras conviene anotar al escuchar?", "Las palabras clave", "Son las que más información entregan."),
    ],
    task("Un adulto lee dos veces este mensaje: «Hi Sofía, I'm tired of the long queue at the cafeteria. Let's bring our lunch tomorrow. Maybe we can eat in the garden, near the old tree.» (queue = fila, cafeteria = casino, lunch = almuerzo, garden = jardín, tree = árbol). Escribe cinco palabras clave y qué significan «tired of», «let's» y «maybe».", "Palabras clave: queue, cafeteria, lunch, garden, tree. Tired of = cansado de; let's = hagamos algo juntos; maybe = quizás.", ["anota cinco palabras clave", "explica las tres expresiones", "no traduce palabra por palabra sin sentido"], ["hoja con palabras clave", "nota del adulto"], ["anotar solo palabras como the y of", "traducir tired como cansado sin of"], "Reconoce las expresiones que acertó y vuelve a escuchar solo la frase donde falló."),
    "Pide a un adulto que lea el diálogo del bus y subraya las expresiones catch, get off y look at.",
    "Escribe tres frases en inglés con let's, maybe y tired of sobre una actividad de tu curso.",
)

# ------------------------------------------------------------------ clase 2
ROUTINE = "«First, Leo checks the bus time. Then he packs his lunch. He also takes an umbrella because the sky is grey. He waits until the bus comes, so he is never late.» (checks = revisa, packs = guarda, lunch = almuerzo, umbrella = paraguas, sky = cielo, grey = gris, waits = espera, never = nunca, late = atrasado)"
LAKE = "«We wanted to go to the lake, but it rained all morning. So we stayed home and played cards. Then the sun came out, and we also had time for a short walk. We walked until it was dark.» (lake = lago, rained = llovió, stayed = nos quedamos, cards = naipes, sun = sol, came out = salió, short = corta, dark = oscuro)"

lesson(
    OA2, 2, MAT_L,
    "Aprenderé a reconocer los conectores then, also, so y until, junto con los del año anterior (and, but, because, first, next), al escuchar. Sirve para seguir el orden y la relación entre las ideas.",
    ["Sé que and une ideas y but muestra contraste.", "Conozco first, next y because."],
    [
        "Un conector (connector) es una palabra que une ideas y muestra cómo se relacionan. Al escucharlos entiendes el orden y las razones sin entender cada palabra. First y next abren una secuencia; then significa luego o después y también marca el siguiente paso. Also significa además o también y suma una idea más.",
        "So significa por eso o así que e introduce un resultado: It rained, so we stayed home (Llovió, así que nos quedamos). Because significa porque e introduce una razón: We stayed home because it rained. Until significa hasta que y marca el momento en que algo termina: He waits until the bus comes. But marca un contraste y and une ideas parecidas.",
        "Al escuchar, anota el conector y la idea que viene después. Pregúntate qué relación muestra: orden (first, next, then), suma (also, and), contraste (but), razón (because), resultado (so) o límite de tiempo (until). Esa pregunta te permite resumir el texto con tus palabras.",
    ],
    [("then", "luego, después"), ("also", "además, también"), ("so", "por eso, así que (resultado)"), ("until", "hasta que"), ("because", "porque (razón)"), ("but", "pero (contraste)")],
    [
        ("Relación que muestra so", ADULT + ROUTINE + " ¿Qué muestra la palabra so en «so he is never late»?", ["So viene después de que Leo espera el bus.", "Lo que sigue, never late, es el resultado.", "So introduce un resultado."], "Un resultado: por eso nunca llega tarde"),
        ("Relación que muestra until", ADULT + LAKE + " ¿Hasta cuándo caminaron?", ["Busco until.", "Dice We walked until it was dark.", "Until marca el límite: hasta que oscureció."], "Hasta que oscureció"),
    ],
    [
        ("Confundir because con so.", "Because introduce la razón y so introduce el resultado; se cambian de lugar.", "Pregunta qué pasó primero: la razón va con because y el resultado con so."),
        ("Pensar que until significa «mientras».", "Until marca el final de la acción, no su duración completa.", "Tradúcelo como hasta que."),
    ],
    [
        (ADULT + ROUTINE + " ¿Qué conector marca el paso que sigue a revisar la hora del bus? a) then b) until", "a) then", "Then significa luego y marca el siguiente paso."),
        (ADULT + LAKE + " ¿Qué conector muestra que querían ir al lago, pero pasó otra cosa? a) but b) also", "a) but", "But marca contraste con lo que querían."),
        (ADULT + ROUTINE + " ¿Qué conector agrega una cosa más que lleva Leo? a) also b) so", "a) also", "Also agrega que además lleva un paraguas."),
    ],
    [
        (ADULT + ROUTINE + " ¿Por qué Leo lleva paraguas? a) porque el cielo está gris b) porque el bus llega tarde", "a) porque el cielo está gris", "Dice because the sky is grey."),
        (ADULT + LAKE + " ¿Por qué se quedaron en casa? a) porque llovió toda la mañana b) porque no había bus", "a) porque llovió toda la mañana", "Dice it rained all morning, so we stayed home."),
        (ADULT + LAKE + " ¿Qué hicieron después de jugar naipes y cuando salió el sol? a) también salieron a una caminata corta b) volvieron al lago", "a) también salieron a una caminata corta", "Dice we also had time for a short walk."),
    ],
    [
        ("Elige el conector: «I was tired, ___ I went to bed early.» a) so b) but", "a) so", "El resultado de estar cansado es acostarse temprano."),
        ("Elige el conector: «I like tea, ___ I don't like coffee.» a) but b) also", "a) but", "Se contrastan dos gustos opuestos."),
        ("Elige el conector: «Wait here ___ I come back.» a) until b) because", "a) until", "Hay que esperar hasta que vuelva."),
    ],
    [
        ("¿Qué frase introduce la razón? a) We stayed home because it rained. b) It rained, so we stayed home.", "a) We stayed home because it rained.", "Because introduce la razón: llovió."),
        ("Ordena los pasos por los conectores: «Finally, I send it. First, I write the email. Then, I read it twice.» (email = correo, twice = dos veces). Escribe las acciones en orden: write, read, send.", "write, read, send", "First es el primero, then el siguiente y finally el último."),
    ],
    [
        ("Escucha: «Ema studied until nine, so she was tired, but she also cooked dinner.» (studied = estudió, cooked = cocinó, dinner = cena). Hay cuatro conectores. ¿Cuál muestra el resultado de estudiar mucho? a) so b) but c) until", "a) so", "So introduce el resultado: estaba cansada."),
        (ADULT + ROUTINE + " Pedro dice que Leo lleva paraguas porque el bus llega tarde. ¿Qué frase del texto muestra el error? a) because the sky is grey b) so he is never late", "a) because the sky is grey", "Because explica la razón del paraguas: el cielo está gris."),
    ],
    [(ADULT + "Escuchas un mensaje: «First, check your bag. Then, close the windows. Also, turn off the lights. Wait until everyone is outside, so nobody stays inside.» (check = revisa, close = cierra, turn off = apaga, lights = luces, outside = afuera, nobody = nadie, inside = adentro). ¿Hasta cuándo hay que esperar? a) hasta que todos estén afuera b) hasta que lleguen los profesores", "a) hasta que todos estén afuera", "Dice wait until everyone is outside.")],
    [
        ("¿Qué relación muestra «so»?", "Un resultado", "So significa por eso o así que."),
        ("¿Qué significa «until»?", "Hasta que", "Marca el límite de una acción."),
        ("¿Para qué sirve «also»?", "Para agregar una idea más", "Significa además o también."),
    ],
    task("Un adulto lee dos veces este texto: «First, Gaby opens the window. Then she waters the plants. She also cleans the table because it is dusty. She works until the clock says four, so her room is ready for the visit.» (waters = riega, dusty = con polvo, clock = reloj, ready = lista, visit = visita). Escribe en tu hoja los conectores que oíste y qué relación muestra cada uno.", "First (orden), then (siguiente paso), also (suma), because (razón), until (hasta cuándo), so (resultado).", ["anota al menos cuatro conectores", "dice la relación de cada uno", "no inventa conectores"], ["hoja con conectores y relaciones", "nota del adulto"], ["confundir because con so", "decir que until es porque"], "Reconoce los conectores que acertó y vuelve a escuchar la última frase para ubicar until y so."),
    "Pide a un adulto que lea el texto de Leo y levanta la mano cuando oigas first, then, also, because, until o so.",
    "Escribe en español tres frases de tu rutina y tradúcelas al inglés con then, also y so.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA2, 3, MAT_S,
    "Aprenderé a distinguir los dos sonidos de th: /ð/ (como en this) y /θ/ (como en three). Sirve para entender y pronunciar palabras como mother, birthday, Thursday y that.",
    ["Sé que en inglés el sonido de una letra puede cambiar.", "Conozco palabras como the, three y mother."],
    [
        "La combinación th tiene dos sonidos en inglés. En español de Chile ninguno aparece al comienzo de una palabra (la d suave de «nada» se parece a /ð/, pero en inglés se usa también al empezar). El sonido /ð/ es sonoro: pones la punta de la lengua entre los dientes y haces vibrar la garganta, como en this, that, the, they, then, mother y brother. El sonido /θ/ es sordo: la lengua está en el mismo lugar, pero solo sale aire, sin vibrar, como en three, thank, think, thirty, month y birthday.",
        "Para saber si sientes vibración, toca tu garganta con los dedos. Con this, la garganta vibra. Con three, no vibra. Un error frecuente en hablantes de español es decir una d (dis en vez de this) o una t o una s (tree o sree en vez de three). Eso puede cambiar el significado: three (tres) y tree (árbol) son palabras distintas.",
        "Una guía útil: las palabras pequeñas que señalan o unen, como the, this, that, they, them, then, there y than, tienen /ð/. También lo tienen las palabras con -ther en el medio: mother, father, brother, together y weather. Las palabras de números, de pensar o agradecer, como three, thirty, thank y think, y las que terminan en -th, como month y mouth, tienen /θ/. Thursday y birthday también tienen /θ/.",
    ],
    [("/ð/", "th sonora: la garganta vibra (this, mother)"), ("/θ/", "th sorda: solo sale aire (three, birthday)"), ("voiced", "sonora: con vibración en la garganta"), ("voiceless", "sorda: sin vibración"), ("three / tree", "tres / árbol: se distinguen por el sonido inicial"), ("month", "mes")],
    [
        ("Clasificar una palabra", "¿Qué sonido tiene la th de «mother»?", ["Mother tiene -ther en el medio.", "Las palabras con -ther tienen /ð/.", "Mother tiene /ð/."], "/ð/"),
        ("Corregir un error", "Ana dice «tree» cuando quería decir three (tres). ¿Qué sonido cambió?", ["Three empieza con /θ/.", "Ana usó una t en su lugar.", "Cambió /θ/ por t y dijo árbol (tree)."], "Cambió /θ/ por una t"),
    ],
    [
        ("Pensar que todas las th suenan igual.", "En inglés hay dos sonidos de th y cambian la pronunciación.", "Fíjate en si la garganta vibra: sí en this, no en three."),
        ("Pronunciar this como «dis».", "El sonido /ð/ no es una d; la lengua va entre los dientes.", "Pon la punta de la lengua entre los dientes y haz vibrar la garganta."),
    ],
    [
        ("¿Qué sonido tiene la th de «this»? a) /ð/ b) /θ/", "a) /ð/", "This es una palabra que señala y tiene th sonora."),
        ("¿Qué sonido tiene la th de «three»? a) /θ/ b) /ð/", "a) /θ/", "Three es un número y tiene th sorda."),
        ("¿Qué sonido tiene la th de «birthday»? a) /θ/ b) /ð/", "a) /θ/", "Birthday tiene th sorda, sin vibración."),
    ],
    [
        ("¿Qué sonido tiene la th de «brother»? a) /ð/ b) /θ/", "a) /ð/", "Las palabras con -ther en el medio tienen /ð/."),
        ("¿Qué sonido tiene la th de «Thursday»? a) /θ/ b) /ð/", "a) /θ/", "Thursday empieza con th sorda."),
        ("¿Qué palabra tiene /ð/? a) weather b) thirty c) month", "a) weather", "Weather tiene -ther en el medio; las otras tienen /θ/."),
    ],
    [
        ("Clasifica estas palabras según el sonido de th: the, thank, weather, month, together, thirty. Escribe qué palabras tienen /ð/ y cuáles /θ/.", "/ð/: the, weather, together; /θ/: thank, month, thirty", "The y las palabras con -ther tienen /ð/; thank, month y thirty tienen /θ/."),
        ("Ema dice «dis» cuando quería decir this. ¿Qué cambió? a) reemplazó /ð/ por una d b) reemplazó /θ/ por una s", "a) reemplazó /ð/ por una d", "This tiene /ð/, no una d."),
        ("En «Their brother thinks that three months is a long time», ¿cuántas palabras tienen /ð/? (palabras con th: their, brother, thinks, that, three, months)", "3", "Their, brother y that tienen /ð/; thinks, three y months tienen /θ/."),
    ],
    [
        ("Sam dice: «Todas las palabras con th suenan igual». ¿Qué par de palabras lo contradice? a) this y three b) this y that", "a) this y three", "This tiene /ð/ y three tiene /θ/."),
        ("¿Por qué three y tree son palabras distintas? a) porque el sonido inicial cambia el significado b) porque se escriben igual", "a) porque el sonido inicial cambia el significado", "Un solo sonido distinto cambia tres por árbol."),
    ],
    [
        ("En «My mother thanks them on Thursday», ¿cuántas palabras tienen /θ/? (palabras con th: mother, thanks, them, Thursday)", "2", "Thanks y Thursday tienen /θ/; mother y them tienen /ð/."),
        ("Marta dice «I sink it is the sird day». Quería decir «I think it is the third day» (pienso que es el tercer día). ¿Qué sonido cambió? a) /θ/ por s b) /ð/ por d", "a) /θ/ por s", "Think y third empiezan con /θ/, no con s."),
    ],
    [("Te presentas en clase: «This is my brother. His birthday is in the third month.» (month = mes). Las palabras con th son: this, brother, birthday, the, third, month. ¿Cuántas tienen /θ/?", "3", "Birthday, third y month tienen /θ/; this, brother y the tienen /ð/.")],
    [
        ("¿Cómo sabes que una th es /ð/?", "La garganta vibra", "Con th sonora hay vibración."),
        ("En Inglés de 8.º (OA 2, clase 3): ¿Qué sonido tiene la th de «thank»?", "/θ/", "Es th sorda."),
        ("¿Qué sonido tiene la th de «that»?", "/ð/", "Es una palabra que señala."),
    ],
    task("Con una persona adulta, lee en voz alta esta serie y marca la th de cada palabra: the, three, brother, thank, they, month, weather, thirty. Escribe dos listas: palabras con /ð/ y palabras con /θ/. Luego di una oración con dos palabras de cada lista.", "/ð/: the, brother, they, weather; /θ/: three, thank, month, thirty. Oración de ejemplo: My brother thanks three friends.", ["separa bien las ocho palabras", "dice la oración sin cambiar th por d, t o s", "toca la garganta para comprobar la vibración"], ["dos listas", "oración dicha en voz alta", "nota del adulto"], ["decir dis o tree", "mezclar birthday con /ð/"], "Reconoce las palabras que clasificó bien y repasa solo las que cambió con la ayuda de la garganta."),
    "Di en voz alta this, that, the y toca la garganta; luego three, thank, think y compara.",
    "Escribe una oración con tres palabras de /ð/ y otra con tres de /θ/, y léelas a una persona adulta.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA2, 4, MAT_S,
    "Aprenderé a reconocer y pronunciar los sonidos iniciales /w/ (week) y /r/ (ready). Sirve para no confundir pares como west y rest o wing y ring.",
    ["Sé que en inglés la letra w a veces no suena.", "Conozco palabras como week, red y room."],
    [
        "El sonido /w/ aparece al comienzo de week, water, window, want, when y where. Para hacerlo, redondea los labios como para decir «u» y ábrelos rápido: week suena casi como «uik». Un error común es agregar una g antes («guater», «guik»). También hay palabras con /w/ que no empiezan con w, como one y once.",
        "El sonido /r/ aparece al comienzo de ready, red, room, rain y run. No es la erre del español: la lengua no vibra ni toca el paladar; se curva hacia atrás y los labios se redondean un poco. Cuidado con la escritura: en write, wrong y wrist la w no suena y la palabra empieza con /r/. Write y right suenan igual al comienzo.",
        "Las palabras que solo cambian entre /w/ y /r/ forman pares que se confunden: west y rest, wing y ring, wide y ride, wake y rake. Un mismo sonido cambiado puede cambiar el significado. Al escuchar, atiende al primer sonido y al contexto de la frase.",
    ],
    [("/w/", "sonido inicial de week: labios redondos, como una «u»"), ("/r/", "sonido inicial de ready: lengua curvada, sin vibrar"), ("silent w", "w que no suena (write, wrong)"), ("west / rest", "oeste / descanso"), ("wing / ring", "ala / anillo"), ("wide / ride", "ancho / paseo")],
    [
        ("Clasificar por sonido inicial", "¿Con qué sonido empieza «write»?", ["Write tiene una w al comienzo.", "En write la w no suena.", "Empieza con /r/."], "/r/"),
        ("Corregir un error", "Pedro dice «guater» cuando quería decir water. ¿Qué sonido cambió?", ["Water empieza con /w/.", "Pedro usó una g.", "Hay que redondear los labios, como una u."], "Cambió /w/ por una g"),
    ],
    [
        ("Pronunciar week como «guik».", "Se agrega una g antes; /w/ usa solo los labios redondeados, sin g.", "Redondea los labios como para decir u y ábrelos."),
        ("Creer que en write la w suena.", "En write, wrong y wrist la w es muda.", "Pronuncia write con /r/."),
    ],
    [
        ("¿Qué sonido inicial escuchas en la palabra «week»? a) /w/ b) /r/", "a) /w/", "Week empieza con w que suena."),
        ("¿Con qué sonido empieza «red»? a) /r/ b) /w/", "a) /r/", "Red empieza con /r/."),
        ("¿Qué sonido inicial escuchas en la palabra «window»? a) /w/ b) /r/", "a) /w/", "Window empieza con /w/."),
    ],
    [
        ("¿Con qué sonido empieza «wrong»? a) /r/ b) /w/", "a) /r/", "En wrong la w es muda."),
        ("¿Con qué sonido empieza «one»? a) /w/ b) /r/", "a) /w/", "One suena como «uan»; empieza con /w/ aunque se escriba con o."),
        ("¿Qué palabra empieza con /r/? a) rain b) where c) water", "a) rain", "Where y water empiezan con /w/."),
    ],
    [
        ("Clasifica estas palabras según su primer sonido: week, ready, wrong, where, rain, one. Escribe cuáles empiezan con /w/ y cuáles con /r/.", "/w/: week, where, one; /r/: ready, wrong, rain", "Wrong tiene w muda; one empieza con /w/."),
        ("Ema quiere decir «ring» (anillo), pero dice «wing» (ala). ¿Qué sonido cambió? a) /r/ por /w/ b) /w/ por /r/", "a) /r/ por /w/", "Ring empieza con /r/; wing empieza con /w/."),
        ("Elige la palabra que empieza con /w/ y significa «ancho»: a) wide b) ride", "a) wide", "Wide es ancho; ride es paseo y empieza con /r/."),
    ],
    [
        ("Julia dice «Todas las palabras con w comienzan con /w/». ¿Qué palabra lo contradice? a) write b) week", "a) write", "En write la w es muda y empieza con /r/."),
        ("¿Qué par de palabras solo se diferencia por /w/ y /r/ al comienzo? a) west y rest b) week y weak", "a) west y rest", "Solo cambia el primer sonido: /w/ y /r/."),
    ],
    [
        ("¿Cuántas palabras de «Where were we in the last week of May?» empiezan con /w/? (palabras: where, were, we, in, the, last, week, of, May)", "4", "Where, were, we y week empiezan con /w/."),
        ("Si dices «I ride to school» pero el oyente entiende «I wide to school», ¿qué sonido cambió? a) /r/ por /w/ b) /w/ por /r/", "a) /r/ por /w/", "Ride empieza con /r/, no con /w/."),
    ],
    [("En una conversación quieres decir «Is the window open?» (¿está abierta la ventana?). ¿Con qué sonido debes comenzar la palabra window? a) /w/ b) /r/", "a) /w/", "Window empieza con /w/, con los labios redondeados.")],
    [
        ("¿Cómo se hace el sonido /w/?", "Redondeando los labios como para decir u", "Week suena casi como «uik»."),
        ("En Inglés de 8.º (OA 2, clase 4): ¿Con qué sonido empieza «write»?", "/r/", "La w es muda."),
        ("¿La /r/ del inglés vibra como la del español?", "No", "La lengua se curva y no vibra."),
    ],
    task("Con una persona adulta, lee estas palabras en voz alta: week, ready, wrong, water, red, window, write, rain. Escribe dos listas: las que empiezan con /w/ y las que empiezan con /r/. Luego di una oración con una palabra de cada lista.", "/w/: week, water, window; /r/: ready, wrong, red, write, rain. Oración: The red window is ready.", ["separa bien las ocho palabras", "dice la oración sin cambiar /w/ por g", "reconoce las dos palabras con w muda"], ["dos listas", "oración dicha en voz alta", "nota del adulto"], ["poner wrong entre las /w/", "decir guater"], "Reconoce lo que clasificó bien y revisa solo las palabras con w muda."),
    "Di week, water y window redondeando los labios; luego ready, red y rain curvando la lengua.",
    "Escribe una oración que use los pares west y rest, y léela despacio para marcar la diferencia.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA2, 5, MAT_S,
    "Aprenderé a reconocer los tres sonidos finales de los verbos regulares en pasado: /d/ (lived), /t/ (helped) e /ɪd/ (decided). Sirve para escuchar y decir bien el pasado.",
    ["Sé que los verbos regulares forman el pasado con -ed.", "Conozco verbos como walk, play y want."],
    [
        "Los verbos regulares forman el pasado con -ed, pero esa terminación suena de tres formas. Se pronuncia /t/ en helped, walked, laughed, danced, washed y watched. Se pronuncia /d/ en lived, played, cleaned, opened, called y arrived. Se pronuncia /ɪd/ (con una sílaba más) en decided, wanted, needed, visited y painted.",
        "La regla depende del último sonido del verbo, no de su última letra. Si el verbo termina en los sonidos /p/, /k/, /f/, /s/, /ʃ/ (sh) o /tʃ/ (ch), la terminación suena /t/: help, walk, laugh, dance, wash, watch. Si termina en /t/ o /d/, suena /ɪd/ y se agrega una sílaba: want, need, decide, paint. En los demás casos, es decir, después de una vocal o de un sonido sonoro, suena /d/: live, play, clean, open, call.",
        "Hay un cuidado importante: danced termina con la letra d, pero suena /t/, porque dance termina con el sonido /s/. Al escuchar, cuenta las sílabas: wanted tiene dos (wan-ted); walked tiene una. Si lo dices mal, puedes confundir el tiempo: I walk (hoy) y I walked (ayer).",
    ],
    [("/d/", "terminación sonora: lived, played"), ("/t/", "terminación sorda: helped, walked"), ("/ɪd/", "terminación con sílaba extra: decided, wanted"), ("regular verb", "verbo regular: el pasado termina en -ed"), ("past", "pasado"), ("syllable", "sílaba"), ("sonoro / sordo", "con vibración en la garganta / sin vibración")],
    [
        ("Clasificar un verbo", "¿Cómo suena la terminación -ed de «helped»?", ["Help termina en el sonido /p/.", "Después de /p/ la terminación suena /t/.", "Helped termina en /t/."], "/t/"),
        ("Clasificar con sílaba extra", "¿Cómo suena la terminación -ed de «decided»?", ["Decide termina en el sonido /d/.", "Después de /t/ o /d/ se agrega una sílaba: /ɪd/.", "Decided tiene tres sílabas: de-ci-ded."], "/ɪd/"),
    ],
    [
        ("Decir danced con una d final.", "Dance termina con el sonido /s/, así que -ed suena /t/.", "Fíjate en el último sonido del verbo, no en su letra."),
        ("Decir wanted en una sílaba.", "Después de /t/ o /d/ la terminación suena /ɪd/ y agrega una sílaba.", "Cuenta las sílabas: wan-ted."),
    ],
    [
        ("¿Cómo suena la terminación -ed de «lived»? a) /d/ b) /t/", "a) /d/", "Live termina en el sonido /v/, que es sonoro."),
        ("¿Cómo suena la terminación -ed de «walked»? a) /t/ b) /d/", "a) /t/", "Walk termina en /k/, que es sordo."),
        ("¿Qué terminación tiene el verbo «wanted» en pasado? a) /ɪd/ b) /t/", "a) /ɪd/", "Want termina en /t/, así que suena /ɪd/."),
    ],
    [
        ("¿Cómo suena la terminación -ed de «played»? a) /d/ b) /ɪd/", "a) /d/", "Play termina en vocal, así que suena /d/."),
        ("¿Cuántas sílabas tiene «needed»? a) 2 b) 1", "a) 2", "Need termina en /d/, por lo que suena /ɪd/ y se agrega una sílaba: nee-ded."),
        ("¿Cuál de estos verbos en pasado suena /t/ al final? a) washed b) cleaned c) painted", "a) washed", "Wash termina en /ʃ/ (sh), un sonido sordo."),
    ],
    [
        ("Clasifica estos verbos según el sonido de -ed: played, walked, wanted, cleaned, washed, needed. Escribe cuáles suenan /d/, /t/ e /ɪd/.", "/d/: played, cleaned; /t/: walked, washed; /ɪd/: wanted, needed", "Play y clean terminan en sonido sonoro; walk y wash en sordo; want y need en /t/ y /d/."),
        ("¿Cómo suena la terminación -ed de «danced»? a) /t/ b) /d/", "a) /t/", "Dance termina con el sonido /s/, que es sordo."),
        ("Ana lee «visited» en dos sílabas (vi-sited). ¿Cuántas sílabas tiene en realidad? a) 3 b) 2", "a) 3", "Visit termina en /t/, así que suena /ɪd/: vi-si-ted."),
    ],
    [
        ("Carla dice: «Todos los verbos que terminan en -ed suenan igual». ¿Qué par de verbos la contradice? a) helped y decided b) walked y washed", "a) helped y decided", "Helped suena /t/ y decided suena /ɪd/."),
        ("¿Por qué «laughed» suena /t/ al final? a) porque laugh termina en el sonido /f/ b) porque termina en la letra h", "a) porque laugh termina en el sonido /f/", "El sonido /f/ es sordo, por eso -ed suena /t/."),
    ],
    [
        ("En «Yesterday I cleaned, painted and watched a film» (película), ¿cuántos verbos tienen la terminación /ɪd/?", "1", "Solo painted suena /ɪd/; cleaned suena /d/ y watched suena /t/."),
        ("Si dices «I wanted» pero el oyente entiende «I want», ¿qué se perdió? a) la sílaba extra /ɪd/ del pasado b) la letra w", "a) la sílaba extra /ɪd/ del pasado", "Sin /ɪd/ suena como el presente."),
    ],
    [("Cuentas lo que hiciste ayer: «I cooked, cleaned and decided to rest.» (cooked = cociné, cleaned = limpié, decided = decidí, rest = descansar). ¿Cuál de los tres verbos tiene la terminación /ɪd/? a) decided b) cooked c) cleaned", "a) decided", "Decide termina en /d/, así que se agrega /ɪd/. Cooked suena /t/ y cleaned suena /d/.")],
    [
        ("¿De qué depende el sonido de -ed?", "Del último sonido del verbo", "No depende de la última letra."),
        ("En Inglés de 8.º (OA 2, clase 5): ¿Cómo suena -ed en «lived»?", "/d/", "Live termina en un sonido sonoro."),
        ("¿Cuándo suena -ed como /ɪd/?", "Cuando el verbo termina en /t/ o /d/", "Se agrega una sílaba."),
    ],
    task("Con una persona adulta, lee estos verbos en pasado en voz alta: lived, helped, decided, walked, played, painted, washed, opened. Escribe tres listas: /d/, /t/ e /ɪd/. Luego di una oración con un verbo de cada lista.", "/d/: lived, played, opened; /t/: helped, walked, washed; /ɪd/: decided, painted. Oración: I walked, opened the door and painted the wall.", ["clasifica bien los ocho verbos", "dice la oración marcando cada terminación", "agrega la sílaba extra en decided y painted"], ["tres listas", "oración dicha en voz alta", "nota del adulto"], ["decir helped con d", "decir wanted en una sílaba"], "Reconoce los verbos que clasificó bien y repasa solo los que dudó con la regla del último sonido."),
    "Di lived, helped y decided en voz alta y marca con una palmada las sílabas de cada uno.",
    "Escribe cinco verbos regulares nuevos, ponlos en pasado y clasifícalos en /d/, /t/ o /ɪd/.",
)
