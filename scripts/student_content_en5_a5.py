"""Student material for 5.º básico Inglés (propuesta), EN05 OA 09 (sonidos /g/ y /dʒ/ en textos orales) y OA 10 (comunicación oral con apoyo).

Los textos orales (poemas, adivinanzas, trabalenguas, monólogos y diálogos) son originales y se leen en voz alta con un adulto.
La producción oral (repetir, decir un monólogo, presentar) la observa y comenta un adulto: este cuaderno no puede escucharla ni corregirla.
Las imágenes y diapositivas se describen con palabras dentro del enunciado.
"""
from __future__ import annotations

from student_content_en5_a import ADULT, lesson
from student_content_ma01_b import task
from student_lessons import arith

OA9 = "EN05 OA 09"
OA10 = "EN05 OA 10"

SOUNDS = "Palabras con /g/: go, ago, egg, goat, game, big, dog, green, bag, garden, gate, again, tiger, finger. Palabras con /dʒ/: jacket, jam, jump, juice, jungle, July, jeans, general, giant, giraffe, gym, age, page, orange, bridge."
TWISTER_G = "«Gus the goat gets a green gift.» (Gus = nombre de un cabrito, gets = recibe, gift = regalo)"
TWISTER_J = "«June and Jack jump in the jungle with a giant giraffe.» (jump = saltan, jungle = selva, giant = gigante)"
MONO = "«My name is Gabi. I go to the gym in July. I wear green jeans and a jacket. I have a big dog and a juicy orange.» (gym = gimnasio, wear = uso, jeans = pantalones de mezclilla, juicy = jugosa)"

# ================================================================ OA 09
lesson(
    OA9, 1,
    "Los trabalenguas, poemas y listas escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a reconocer y producir el sonido /g/ de go, ago y egg en trabalenguas y poemas. Sirve para decir con claridad palabras inglesas con ese sonido.",
    ["Conozco el sonido /g/ de «gato» en español.", "Sé que la g puede sonar /g/ o /dʒ/ en inglés."],
    [
        "El sonido /g/ es el mismo de la «g» de «gato» en español. En inglés aparece al comienzo (go, goat, game), en el medio (ago, tiger, finger) y al final (egg, big, dog). Se hace con la parte de atrás de la lengua tocando el paladar; la garganta vibra. Puedes sentirlo poniendo un dedo en tu cuello.",
        "El sonido /g/ se escribe con g en go, game, big; con gg en egg, bigger; y con gu en guitar. La g suena /g/ casi siempre ante a, o, u (go, game, gum) y al final de la palabra (big, dog). Ante e o i a veces suena /g/ (get, give, girl) y a veces /dʒ/ (general, giant). Por eso hay que escuchar la palabra.",
        "Un trabalenguas (tongue twister) repite un mismo sonido para practicarlo. Dilo despacio primero, luego más rápido. Un poema o una canción también te ayudan a oír el sonido muchas veces. Hoy te fijarás en /g/: cuántas veces aparece, en qué parte de la palabra y cómo se escribe.",
    ],
    [("/g/", "sonido de go, ago, egg"), ("tongue twister", "trabalenguas"), ("goat", "cabra"), ("gift", "regalo"), ("gets", "recibe"), ("garden", "jardín")],
    [
        ("Contar palabras con /g/", ADULT + TWISTER_G + " ¿Cuántas palabras tienen el sonido /g/ al comienzo?", ["Escucho Gus: empieza con /g/.", "Escucho goat, gets, green y gift: también.", "Son cinco."], "5"),
        ("Posición del sonido", "Lee la palabra «finger» (dedo). ¿Dónde está el sonido /g/: al comienzo, en el medio o al final?", ["Digo fin-ger.", "El sonido /g/ está después de la primera sílaba.", "Está en el medio."], "En el medio"),
    ],
    [
        ("Contar dos sonidos /g/ en «egg» porque tiene dos letras g.", "Se confunde la escritura con el sonido.", "Egg se escribe con gg pero tiene un solo sonido /g/."),
        ("Decir que «girl» tiene el sonido /dʒ/ porque la g va antes de i.", "Se aplica una regla sin excepciones.", "Girl es una excepción: se dice con /g/."),
    ],
    [
        (SOUNDS + " ¿Tiene /g/ la palabra «dog»?", "Sí", "Dog termina con /g/."),
        (SOUNDS + " ¿Tiene /g/ la palabra «jungle» al comienzo?", "No", "Jungle empieza con /dʒ/."),
        ("¿Qué letras escriben el sonido /g/ en «egg»?", "gg", "Dos g seguidas escriben un solo sonido /g/."),
    ],
    [
        (ADULT + "«Greg has a green bag and a big dog.» (Greg = nombre de niño). ¿Cuántas palabras tienen /g/?", "5", "Greg, green, bag, big y dog."),
        (ADULT + "«Go, go, go to the garden gate!» (gate = portón). ¿Cuántas veces oyes el sonido /g/ al comienzo de una palabra?", "5", "Go, go, go, garden y gate."),
        ("Elige las palabras con /g/ al final: a) big, dog, bag b) jam, gym, page", "a)", "Big, dog y bag terminan en /g/."),
    ],
    [
        ("Elige la palabra con /g/ al comienzo: a) game b) giant", "a) game", "Game empieza como go y giant empieza con /dʒ/."),
        ("Dice un adulto: «big dog». ¿Cuántas palabras tienen /g/?", "2", "Big y dog terminan con /g/."),
        ("¿Qué sonido tiene la g de «ago» en el medio: /g/ o /dʒ/?", "/g/", "Ago suena como go en su segunda parte."),
    ],
    [
        ("Un compañero dice que «giraffe» empieza con /g/. ¿Qué sonido tiene?", "/dʒ/", "Giraffe empieza igual que general."),
        ("Elige la palabra con /g/ en el medio: a) tiger b) giant", "a) tiger", "Ti-ger tiene /g/ en el medio."),
    ],
    [
        (ADULT + "«I give a gift to Gus again and again.» (give = doy, again = otra vez, Gus = nombre de un cabrito). ¿Cuántas palabras dichas tienen /g/? Cuenta again cada vez que se dice.", "5", "Give, gift, Gus y again dos veces."),
        ("Ordena de más a menos palabras con /g/: A) «Gus gets a gift» B) «Go home» C) «I get a green gift for Gus».", "C, A, B", "C tiene cuatro (get, green, gift, Gus), A tiene tres y B tiene una."),
    ],
    [(ADULT + "En el jardín, un niño grita: «Look, a goat in the garden!» (look = mira). ¿Cuántas palabras tienen /g/?", "2", "Goat y garden.")],
    [
        ("¿Con qué parte de la boca se hace /g/?", "Con la parte de atrás de la lengua", "La lengua toca el paladar al fondo."),
        ("¿Qué es un trabalenguas?", "Un texto que repite un sonido para practicarlo", "Tongue twister practica sonidos."),
        ("¿Qué sonido tiene «green» al comienzo?", "/g/", "Green empieza como go."),
    ],
    task("Un adulto lee dos veces: «Gus the goat gets a green gift.» Repite el trabalenguas en voz alta tres veces, cada vez un poco más rápido. Luego escribe las cinco palabras con /g/ en tu hoja y subraya la letra g de cada una. Pide al adulto que te diga si se oyó claro el sonido.", "Gus, goat, gets, green, gift con la g subrayada. Repetí tres veces; el adulto confirmó el sonido.", ["repite tres veces", "escribe las cinco palabras", "subraya la g"], ["hoja con palabras", "nota del adulto"], ["confundir /g/ con /dʒ/", "olvidar una palabra"], "Aplaude el trabalenguas claro y practica con él, despacio, la palabra donde se confundió."),
    "Pide a un adulto que diga go, ago y egg y señala dónde está el sonido /g/ en cada palabra.",
    "Escribe una oración de cinco palabras con al menos tres palabras con /g/.",
)

lesson(
    OA9, 2,
    "Los trabalenguas, adivinanzas y poemas escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a reconocer y producir el sonido /dʒ/ de jacket, general y age en trabalenguas y poemas. Sirve para decir con claridad palabras inglesas con ese sonido.",
    ["Conozco el sonido /g/ de la clase anterior.", "Sé que la j inglesa suena /dʒ/."],
    [
        "El sonido /dʒ/ no existe igual en español. Se parece a una «ch» pero con la garganta vibrando: empieza con la lengua pegada arriba, como para decir «ch», y se suelta con la voz. Aparece al comienzo (jacket, jam, giant), en el medio (magic, energy) y al final (age, page, bridge).",
        "Se escribe de varias formas. Con j: jacket, jam, jump, juice, July. Con g ante e, i o y: general, giant, gym. Con ge al final: age, page, large. Con dge al final: bridge, badge. En orange, la g también suena /dʒ/. Si hay una j en inglés, casi siempre suena /dʒ/.",
        "El trabalenguas «June and Jack jump in the jungle with a giant giraffe» repite /dʒ/ muchas veces. Practícalo despacio. Pon el dedo en tu cuello: siente la vibración. Compara con /g/, donde la lengua va atrás. Hoy contarás cuántas veces aparece /dʒ/ y cómo se escribe en cada palabra.",
    ],
    [("/dʒ/", "sonido de jacket, general, age"), ("jungle", "selva"), ("giant", "gigante"), ("giraffe", "jirafa"), ("orange", "naranja"), ("bridge", "puente")],
    [
        ("Contar palabras con /dʒ/", ADULT + TWISTER_J + " ¿Cuántas palabras tienen el sonido /dʒ/?", ["Escucho June, Jack, jump y jungle.", "Escucho giant y giraffe.", "Son seis."], "6"),
        ("Escritura del sonido", "En «bridge», ¿cómo se escribe el sonido /dʒ/ al final?", ["Miro el final de la palabra.", "Termina en dge.", "Se escribe dge."], "dge"),
    ],
    [
        ("Decir que «jacket» empieza con /g/.", "Se confunde la j con la g.", "La j suena /dʒ/ en jacket."),
        ("Pensar que en «orange» la g suena /g/.", "Se aplica la regla de /g/.", "En orange, la g suena /dʒ/."),
    ],
    [
        (SOUNDS + " ¿Tiene /dʒ/ la palabra «page»?", "Sí", "Page termina con /dʒ/."),
        (SOUNDS + " ¿Tiene /dʒ/ la palabra «garden»?", "No", "Garden empieza con /g/."),
        ("¿Cómo se parece el sonido /dʒ/ a un sonido del español?", "A la ch, pero con la garganta vibrando", "Se hace con la lengua pegada arriba y con voz."),
    ],
    [
        (ADULT + "«July has juice and jam.» ¿Cuántas palabras tienen /dʒ/?", "3", "July, juice y jam."),
        (ADULT + "«A large orange is on the page.» (large = grande). ¿Cuántas palabras tienen /dʒ/?", "3", "Large, orange y page."),
        ("Elige las palabras con /dʒ/ al comienzo: a) jam, jump, giant b) go, game, gate", "a)", "Jam, jump y giant empiezan con /dʒ/."),
    ],
    [
        ("Elige la palabra con /dʒ/ en el medio: a) magic b) tiger", "a) magic", "Ma-gic tiene /dʒ/ y ti-ger tiene /g/."),
        (ADULT + "«Jim has a huge jar.» (huge = enorme, jar = frasco). ¿Cuántas palabras tienen /dʒ/?", "3", "Jim, huge y jar."),
        ("¿Con qué sonido termina «orange»: /g/ o /dʒ/?", "/dʒ/", "La g final de orange suena /dʒ/."),
    ],
    [
        ("Elige la palabra con /dʒ/ al final: a) bridge b) big", "a) bridge", "Bridge termina con /dʒ/ y big con /g/."),
        ("Clasifica «gym». ¿/g/ o /dʒ/?", "/dʒ/", "Gym empieza igual que general."),
    ],
    [
        ("Adivinanza: «I am orange. I am a fruit. You can make juice from me.» (fruit = fruta). ¿Qué soy? Escribe la respuesta y di cuántas veces aparece /dʒ/ en esa palabra.", "orange; una vez", "Orange tiene /dʒ/ en la g final."),
        ("Adivinanza: «I have a long neck. I live in a hot place. I eat leaves from tall trees.» (neck = cuello, hot = caluroso, tall = alto). ¿Qué soy?", "giraffe", "La jirafa tiene el cuello largo y come hojas de árboles altos."),
    ],
    [(ADULT + "En una feria, un niño dice: «Orange juice, please!» (please = por favor). ¿Cuántas palabras tienen /dʒ/?", "2", "Orange y juice.")],
    [
        ("¿Cómo se escribe /dʒ/ en «age»?", "ge", "Age termina en ge."),
        ("¿Cómo suena la g de «general»?", "/dʒ/", "General empieza con /dʒ/."),
        ("¿Qué sonido tiene «jungle» al comienzo?", "/dʒ/", "La j suena /dʒ/."),
    ],
    task("Un adulto lee dos veces: «June and Jack jump in the jungle with a giant giraffe.» Repite el trabalenguas en voz alta tres veces. Después escribe las seis palabras con /dʒ/ y marca cómo se escribe el sonido (j o g). Pide al adulto que escuche tu /dʒ/.", "June, Jack, jump, jungle (j); giant, giraffe (g).", ["repite tres veces", "escribe seis palabras", "marca j o g"], ["hoja con palabras", "nota del adulto"], ["decir que giraffe tiene /g/", "olvidar jungle"], "Aplaude las seis palabras halladas y practica con él, despacio, el comienzo de jungle."),
    "Pide a un adulto que diga jam, jacket y age y repite cada palabra tocando tu cuello.",
    "Escribe una oración con tres palabras con /dʒ/ y dila en voz alta.",
)

lesson(
    OA9, 3,
    "Los pares de palabras escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a distinguir /g/ de /dʒ/ en pares de palabras parecidas, como bag y badge. Sirve para no confundir palabras al escuchar y al hablar.",
    ["Conozco los sonidos /g/ y /dʒ/.", "Sé repetir palabras en voz alta."],
    [
        "Hay palabras que suenan casi igual, pero cambian solo en /g/ o en /dʒ/. Se llaman pares mínimos (minimal pairs). Por ejemplo, bag (bolso) y badge (insignia) se parecen, pero bag termina en /g/ y badge termina en /dʒ/. Otros pares son get / jet, leg / ledge y gust / just.",
        "Get (obtener) empieza con /g/ y jet (avión a reacción) empieza con /dʒ/. Leg (pierna) termina con /g/ y ledge (borde o repisa) termina con /dʒ/. Para distinguirlos, escucha el sonido distinto y repite varias veces cada palabra. Si dudas, fíjate en la vibración: /dʒ/ comienza con la lengua pegada arriba.",
        "Una buena práctica es escuchar dos palabras y decir si son iguales o distintas, y cuál tiene /g/ y cuál /dʒ/. También puedes marcar el par con un color: verde para /g/ y naranja para /dʒ/. Con práctica, tus oídos y tu boca se acostumbran.",
    ],
    [("minimal pair", "par de palabras que cambian en un solo sonido"), ("bag / badge", "bolso / insignia"), ("get / jet", "obtener / avión a reacción"), ("leg / ledge", "pierna / borde"), ("gust / just", "ráfaga / solo"), ("same / different", "iguales / distintas")],
    [
        ("Cuál tiene /dʒ/", ADULT + "Dice: «bag» y «badge». ¿Cuál termina con /dʒ/?", ["Escucho el final de cada palabra.", "Bag termina con /g/.", "Badge termina con /dʒ/."], "badge"),
        ("Iguales o distintas", "Lee: «get» y «jet». ¿Son iguales o distintas, y cuál empieza con /g/?", ["Los comienzos cambian.", "Get empieza como go.", "Son distintas; get tiene /g/."], "Distintas; get tiene /g/"),
    ],
    [
        ("Decir que bag y badge son la misma palabra.", "Se pasa por alto el sonido final.", "Escucha: bag termina con /g/ y badge con /dʒ/."),
        ("Cambiar get por jet al hablar.", "Se confunden /g/ y /dʒ/ al comienzo.", "Get es obtener y jet es avión a reacción."),
    ],
    [
        ("¿Qué sonido tiene el final de «leg»?", "/g/", "Leg termina en /g/."),
        ("¿Qué sonido tiene el final de «ledge»?", "/dʒ/", "Ledge termina en /dʒ/."),
        ("¿Qué es un par mínimo?", "Dos palabras que cambian en un solo sonido", "Por ejemplo, bag y badge."),
    ],
    [
        (ADULT + "Dice: «get, jet, get». ¿Cuántas veces dice una palabra con /dʒ/?", "1", "Solo jet tiene /dʒ/."),
        ("Elige el par con /g/ y /dʒ/ al final: a) bag / badge b) bag / big", "a)", "Badge termina con /dʒ/ y bag con /g/."),
        ("Dice: «just». ¿Empieza con /g/ o con /dʒ/?", "/dʒ/", "Just empieza como jam."),
    ],
    [
        (ADULT + "Dice: «ledge». ¿Termina con /g/ o con /dʒ/?", "/dʒ/", "Ledge termina como badge."),
        ("Elige el par de palabras que cambia entre /g/ y /dʒ/: a) get / jet b) get / got", "a) get / jet", "En get / jet cambia /g/ por /dʒ/ al comienzo; en get / got solo cambia la vocal."),
        ("Dijiste «bag» cuando querías decir «badge». ¿Qué sonido cambió?", "El final: dijiste /g/ en vez de /dʒ/", "Bag termina con /g/ y badge con /dʒ/."),
    ],
    [
        ("Un adulto dice «gust». Tú escribes un cartel «/dʒ/». ¿Es correcto?", "No; gust empieza con /g/", "Gust empieza como go."),
        ("Clasifica estas palabras: get, jet, leg, ledge. ¿Cuántas tienen /g/?", "2", "Get y leg tienen /g/."),
    ],
    [
        ("Une cada palabra con su significado: «jet» y «get». a) avión a reacción b) obtener. ¿Qué significa jet?", "Avión a reacción", "Jet es un avión rápido."),
        ("Lee: «I get a jet.» (I get = consigo). ¿Cuántas palabras con /g/ y cuántas con /dʒ/?", "1 con /g/ y 1 con /dʒ/", "Get tiene /g/ y jet tiene /dʒ/."),
    ],
    [(ADULT + "En la tienda, un niño pregunta: «Do you have a badge or a bag?» (Do you have = ¿tienes?, or = o). ¿Cuál de las dos palabras tiene /dʒ/?", "badge", "Bag termina con /g/ y badge con /dʒ/.")],
    [
        ("¿Qué significa «badge»?", "Insignia", "Es una chapita que se lleva en la ropa."),
        ("¿Qué significa «leg»?", "Pierna", "Leg es pierna."),
        ("¿Qué sonido tiene «jet» al comienzo?", "/dʒ/", "Jet empieza con /dʒ/."),
    ],
    task("Un adulto lee dos veces los pares: bag / badge, get / jet, leg / ledge. En tu hoja haz una tabla con dos columnas, /g/ y /dʒ/, y escribe las seis palabras donde corresponda. Después di cada par en voz alta y pide al adulto que diga cuál palabra dijiste.", "/g/: bag, get, leg. /dʒ/: badge, jet, ledge.", ["tabla con las seis palabras", "tres en cada columna", "dice los pares en voz alta"], ["tabla en la hoja", "nota del adulto"], ["poner badge en /g/", "no decir los pares en voz alta"], "Reconoce el par bien dicho y repite con él el que más le costó."),
    "Pide a un adulto que diga bag o badge sin que veas y adivina cuál fue.",
    "Escribe dos oraciones en español usando bag, badge, get o jet, y léelas en inglés en voz alta.",
)

lesson(
    OA9, 4,
    "Las adivinanzas, poemas y diálogos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a escuchar, reproducir y crear adivinanzas, poemas y diálogos breves con palabras con /g/ y /dʒ/. Sirve para practicar los sonidos dentro de textos reales.",
    ["Conozco los sonidos /g/ y /dʒ/.", "Sé responder adivinanzas sencillas."],
    [
        "Una adivinanza (riddle) describe algo sin nombrarlo. Se resuelve con las pistas. «I am small and white. A hen makes me. I am an egg» es una adivinanza. En ella aparece la palabra egg con /g/. Las adivinanzas son buenas para practicar sonidos porque las dices varias veces.",
        "Un diálogo (dialogue) es una conversación entre dos o más personas. Un poema (poem) tiene versos que pueden rimar. En los dos, puedes buscar las palabras con /g/ y /dʒ/. Cuando reproduces (repeat) un texto, copias la pronunciación de quien lo lee. Cuando produces (produce) un texto, creas uno nuevo usando esas palabras.",
        "Para crear una adivinanza, elige una palabra con /g/ o /dʒ/ (como giraffe o goat) y escribe tres pistas cortas: dónde vive, cómo es y qué hace. Para un poema corto, escribe dos versos que rimen y que tengan dos palabras con esos sonidos. Léelos en voz alta para sentir los sonidos.",
    ],
    [("riddle", "adivinanza"), ("dialogue", "diálogo"), ("poem", "poema"), ("repeat", "repetir"), ("produce", "crear"), ("clue", "pista")],
    [
        ("Resolver una adivinanza", ADULT + "«I have a long neck. I live in a hot place. I eat leaves from tall trees.» (neck = cuello, hot = caluroso, leaves = hojas). ¿Qué soy y qué sonido tiene mi nombre al comienzo?", ["La pista es cuello largo y hojas de árboles altos.", "Soy una jirafa (giraffe).", "Empieza con /dʒ/."], "giraffe; /dʒ/"),
        ("Palabras de un diálogo", "Lee: «Gail: Do you want a green apple? Jack: No, thanks. I want an orange.» (want = quieres, apple = manzana). ¿Cuántas palabras tienen /g/ y cuántas /dʒ/?", ["Gail y green tienen /g/.", "Jack y orange tienen /dʒ/.", "Dos y dos."], "2 con /g/ y 2 con /dʒ/"),
    ],
    [
        ("Crear una adivinanza sin pistas.", "Nadie puede adivinar.", "Escribe tres pistas cortas."),
        ("Leer el poema sin pensar en los sonidos.", "No se practica la pronunciación.", "Léelo despacio y siente /g/ y /dʒ/."),
    ],
    [
        (ADULT + "«I am small and white. A hen makes me. You eat me for breakfast.» (hen = gallina, breakfast = desayuno). ¿Qué soy?", "egg", "El huevo lo pone una gallina."),
        (ADULT + "«I bark. I wag my tail. I am a pet.» (bark = ladro, wag = muevo). ¿Qué soy y con qué sonido termina mi nombre?", "dog; /g/", "El perro ladra y dog termina en /g/."),
        ("¿Qué es una adivinanza?", "Un texto que describe algo sin nombrarlo", "Se adivina con las pistas."),
    ],
    [
        ("Lee: «Gail: Do you want a green apple? Jack: No, thanks. I want an orange.» ¿Quién quiere una naranja?", "Jack", "Jack dice I want an orange."),
        ("Lee: «Gail: Do you want a green apple? Jack: No, thanks. I want an orange.» ¿Qué le ofrece Gail a Jack?", "Una manzana verde", "Dice a green apple."),
        ("Lee: «Jim jumps in the gym. Gus goes to the gym too.» ¿Cuántas palabras tienen /dʒ/?", "4", "Jim, jumps y las dos veces de gym."),
    ],
    [
        (ADULT + "«I am green. I live near water. I jump.» (water = agua). ¿Qué soy?", "frog", "La rana es verde, vive cerca del agua y salta."),
        ("Elige el verso que rima con dog: a) The frog b) The cat", "a) The frog", "Dog y frog terminan igual."),
        (ADULT + "«Jack: Is it a giant? Gail: No, it is a goat!» ¿Qué animal es?", "Una cabra", "Goat es cabra."),
    ],
    [
        ("Lee el poema: «Gus has a goat, a green and big goat. Jim has a jar, a jar of jam.» ¿Cuántas palabras con /g/ aparecen? Cuenta goat cada vez que se dice.", "5", "Gus, goat, green, big y goat."),
        ("Una compañera dice que la adivinanza del huevo no sirve para practicar /dʒ/. ¿Para qué sonido sirve? a) /g/ b) /dʒ/", "a) /g/", "Egg tiene /g/."),
    ],
    [
        ("Crea una pista corta para la palabra «goat»: a) I am a farm animal with horns. b) I am a color.", "a)", "La cabra es un animal de granja con cuernos."),
        ("Elige el verso que rima con «bridge»: a) The fridge b) The car", "a) The fridge", "Bridge y fridge terminan igual."),
    ],
    [(ADULT + "En el recreo, dos amigos hacen un diálogo: «Jill: Where is my jacket? Greg: It is on the gate.» (where = dónde, gate = portón). ¿Cuántas palabras tienen /g/ y /dʒ/ en total?", "4", "Jill, jacket, Greg y gate.")],
    [
        ("¿Qué significa «riddle»?", "Adivinanza", "Es un texto que se adivina con pistas."),
        ("¿Cuántas pistas escribes para una adivinanza?", "Tres", "Tres pistas cortas bastan."),
        ("¿Qué haces con un poema para practicar sonidos?", "Lo leo en voz alta", "Así siento los sonidos."),
    ],
    task("Crea una adivinanza de tres pistas cortas para la palabra «giraffe» y otra para «goat». Escríbelas en inglés con ayuda de estas palabras: neck (cuello), long (largo), farm (granja), animal (animal), milk (leche). Léelas en voz alta a un adulto, que debe adivinar la respuesta.", "Giraffe: I have a long neck. I eat leaves. I live in a hot place. Goat: I am an animal. I live on a farm. I give milk.", ["dos adivinanzas", "tres pistas cada una", "se leen en voz alta"], ["hoja con adivinanzas", "nota del adulto"], ["dar solo una pista", "no leerlas en voz alta"], "Aplaude las pistas claras y practica con él la pronunciación de giraffe y goat."),
    "Pide a un adulto que lea la adivinanza de la jirafa y levanta la mano cuando oigas el sonido /dʒ/.",
    "Escribe un poema de dos versos que rime con dos palabras con /g/ y dos con /dʒ/.",
)

lesson(
    OA9, 5,
    "El monólogo y las canciones cortas escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a presentar un monólogo breve (un texto que digo yo solo) y a cantar o recitar una estrofa original usando /g/ y /dʒ/. Sirve para mostrar que domino los sonidos al hablar.",
    ["Conozco los sonidos /g/ y /dʒ/.", "Sé presentarme con My name is..."],
    [
        "Un monólogo (monologue) es un texto que dice una sola persona. Puede presentarte, describir algo o contar algo corto. Para decirlo bien: lee primero en silencio, subraya las palabras con /g/ y /dʒ/, practica esas palabras y luego di todo el texto en voz alta, mirando a quien te escucha.",
        "Un ejemplo: «My name is Gabi. I go to the gym in July. I wear green jeans and a jacket. I have a big dog and a juicy orange.» En ese monólogo, hay palabras con /g/ (Gabi, go, green, big, dog) y palabras con /dʒ/ (gym, July, jeans, jacket, juicy, orange). Hay más palabras con /dʒ/ que con /g/.",
        "Una canción o un poema corto también puedes recitarlos, como «Jump, jump, jump, up and down! Go, go, go, all around town!» (up and down = arriba y abajo, all around = por todos lados, town = pueblo), donde down y town riman. Mantén un ritmo parejo, marca las palabras con el sonido y repite el coro. Si un compañero te escucha, pídele que te diga si el sonido /g/ o /dʒ/ se escuchó claro. Con práctica, tu pronunciación mejora.",
    ],
    [("monologue", "monólogo"), ("sing / recite", "cantar / recitar"), ("jeans", "pantalones de mezclilla"), ("juicy", "jugosa"), ("gym", "gimnasio"), ("wear", "usar o llevar puesto")],
    [
        ("Contar sonidos", ADULT + MONO + " ¿Cuántas palabras tienen /g/?", ["Escucho Gabi, go, green, big y dog.", "Cuento cinco.", "Hay cinco palabras con /g/."], "5"),
        ("Contar el otro sonido", "En el mismo monólogo, ¿cuántas palabras tienen /dʒ/?", ["Escucho gym, July, jeans, jacket, juicy y orange.", "Cuento seis.", "Hay seis palabras con /dʒ/."], "6"),
    ],
    [
        ("Decir el monólogo sin practicar las palabras difíciles.", "Los sonidos salen mal.", "Practica primero las palabras con /g/ y /dʒ/."),
        ("Hablar sin mirar a quien escucha.", "Se pierde contacto.", "Mira a la persona mientras hablas."),
    ],
    [
        (MONO + " ¿Qué lleva puesto Gabi? a) pantalones de mezclilla verdes y una chaqueta b) un abrigo rojo", "a)", "Dice I wear green jeans and a jacket."),
        (MONO + " ¿En qué mes va Gabi al gimnasio?", "En julio", "Dice in July."),
        (MONO + " ¿Qué mascota tiene Gabi?", "Un perro grande", "Dice a big dog."),
    ],
    [
        arith("Si en el monólogo hay 5 palabras con /g/ y 6 con /dʒ/, ¿cuántas palabras con los dos sonidos hay en total?", "5+6", "Se suman las de cada sonido."),
        ("¿Hay más palabras con /g/ o con /dʒ/ en el monólogo?", "Con /dʒ/", "Seis es más que cinco."),
        ("Elige la palabra con /dʒ/ en: «I have a big dog and a juicy orange.» a) juicy b) dog", "a) juicy", "Juicy empieza con /dʒ/ y dog termina con /g/."),
    ],
    [
        ("En el monólogo de Gabi, ¿cómo se llama quien habla?", "Gabi", "Empieza con My name is Gabi."),
        arith("En el monólogo de Gabi hay 6 palabras con /dʒ/ y 5 con /g/. ¿Cuántas más hay con /dʒ/?", "6-5", "Se resta la cantidad con /g/ a la cantidad con /dʒ/."),
        ("Elige la mejor forma de presentarte: a) My name is Gabi. b) Gabi my name.", "a)", "El orden correcto es sujeto, verbo y nombre."),
    ],
    [
        ("Un compañero dice que «jeans» empieza con /g/. ¿Está bien?", "No; jeans empieza con /dʒ/", "La j de jeans suena /dʒ/."),
        ("Lee la estrofa: «Jump, jump, jump, up and down! Go, go, go, all around town!» ¿Qué dos palabras riman? a) down y town b) jump y go", "a) down y town", "Down y town terminan con el mismo sonido."),
    ],
    [
        ("Completa tu monólogo: «My name is Jack. I have a ___ (dog/jam) and I like it.» Si quieres decir que tiene mermelada, ¿qué eliges?", "jam", "Jam es mermelada."),
        ("Elige el monólogo con más /dʒ/: a) «June has a jacket.» b) «Gus has a bag.»", "a)", "June y jacket tienen /dʒ/."),
    ],
    [(ADULT + "Un profesor dice: «Please, say your name and one thing you like.» (please = por favor, thing = cosa). Gabi responde con el monólogo. ¿Qué cosa dice que le gusta o tiene? a) un perro grande y una naranja b) un auto", "a)", "Dice I have a big dog and a juicy orange.")],
    [
        ("¿Qué es un monólogo?", "Un texto que dice una sola persona", "Mono- indica uno."),
        ("¿Qué haces antes de decir un monólogo?", "Practico las palabras con /g/ y /dʒ/", "Así las dices mejor."),
        ("¿Cuántas palabras con /g/ tiene el monólogo de Gabi?", "5", "Gabi, go, green, big y dog."),
    ],
    task("Escribe tu propio monólogo de cuatro oraciones que empiece con «My name is...» y tenga al menos dos palabras con /g/ y dos con /dʒ/. Ayúdate de estas palabras: go, green, big, dog, jacket, July, orange, jam. Léelo en voz alta a un adulto y pídele que marque si se oyeron claros /g/ y /dʒ/.", "My name is Eli. I go to school in July. I have a green jacket and a big dog. I like orange jam.", ["cuatro oraciones", "dos con /g/ y dos con /dʒ/", "lo lee en voz alta"], ["hoja con monólogo", "nota del adulto"], ["escribir menos de cuatro oraciones", "confundir /g/ con /dʒ/"], "Aplaude el monólogo y practica con él las palabras que sonaron menos claras."),
    "Lee en voz alta el monólogo de Gabi a una persona de tu casa y pídele que cuente cuántas veces oye /dʒ/.",
    "Graba, con permiso, o recita a una persona de tu casa un monólogo corto con /g/ y /dʒ/.",
)

# ================================================================ OA 10
lesson(
    OA10, 1,
    "Los diálogos y carteles descritos en cada ejercicio y lápiz.",
    "Aprenderé a mantener un diálogo corto usando un cartel o una imagen como apoyo. Sirve para preguntar y responder sobre temas del año, como rutinas, animales y comidas.",
    ["Sé saludar y despedirme en inglés.", "Conozco What's your favorite...? y I like..."],
    [
        "Para conversar con apoyo visual, usa una imagen o un cartel (poster) como guía. Imagina un cartel «My Week» con dibujos: lunes (fútbol), miércoles (piano) y viernes (cine). Con él puedes preguntar «What do you do on Monday?» (¿qué haces el lunes?) y responder «I play football».",
        "Un diálogo tiene un saludo (Hello, Hi), preguntas y respuestas, y una despedida (See you, Bye). Algunas preguntas comunes: «What's your favorite animal?» (¿cuál es tu animal favorito?), «Do you like pizza?» (¿te gusta la pizza?) y «What do you do after school?» (¿qué haces después del colegio?). Las respuestas deben tener sujeto y verbo: «I like dogs.»",
        "Mira el cartel antes de hablar. Señala con el dedo lo que nombras. Si no recuerdas una palabra, usa el dibujo o pide ayuda con «How do you say...?». Habla despacio y escucha a tu compañero. En los diálogos se alternan los turnos: uno pregunta y el otro responde, y después cambian.",
    ],
    [("poster", "cartel"), ("My Week", "mi semana"), ("What do you do on Monday?", "¿qué haces el lunes?"), ("favorite", "favorito"), ("after school", "después del colegio"), ("See you", "nos vemos")],
    [
        ("Responder usando el cartel", "Cartel «My Week»: lunes - fútbol; miércoles - piano; viernes - cine. Tu compañero pregunta: «What do you do on Wednesday?» ¿Qué respondes?", ["Busco miércoles en el cartel.", "Dice piano.", "Respondo I play the piano."], "I play the piano"),
        ("Hacer una pregunta", "Con el mismo cartel quieres saber qué hace tu compañero el viernes. ¿Qué preguntas?", ["Uso What do you do on...?", "Pongo Friday.", "Pregunto What do you do on Friday?"], "What do you do on Friday?"),
    ],
    [
        ("Responder solo con una palabra: «Piano.»", "La respuesta queda incompleta.", "Responde con una oración: I play the piano."),
        ("Hablar sin mirar el cartel.", "Se pierde el apoyo visual.", "Señala el cartel mientras hablas."),
    ],
    [
        ("Cartel «My Week»: lunes - fútbol; miércoles - piano; viernes - cine. ¿Qué haces el lunes? ¿Cómo respondes? a) I play football b) I watch a film", "a)", "El cartel dice fútbol el lunes."),
        ("¿Qué significa «What's your favorite animal?»", "¿Cuál es tu animal favorito?", "Favorite es favorito."),
        ("Elige una despedida: a) See you tomorrow b) What's your name?", "a)", "See you tomorrow es una despedida."),
    ],
    [
        ("Completa el diálogo: «A: Do you like pizza? B: ___.» Elige: a) Yes, I do b) Yes, I am", "a) Yes, I do", "Se responde con do."),
        ("Cartel «My Week». Tu compañero pregunta «What do you do on Friday?». ¿Cómo respondes? a) I watch a film b) I play football", "a)", "El cartel dice cine el viernes."),
        ("¿Qué frase usas para pedir una palabra que no recuerdas? a) How do you say...? b) Goodbye", "a)", "Sirve para pedir ayuda con una palabra."),
    ],
    [
        ("Completa: «What ___ you do on Monday?» Elige do o is.", "do", "Con you se usa do."),
        ("Te preguntan «Do you like soup?» y a ti no te gusta. ¿Cómo respondes? a) No, I don't b) No, I'm not", "a)", "Se responde con don't."),
        ("Cartel «My Week»: lunes - fútbol; miércoles - piano; viernes - cine. ¿Qué día vas al cine?", "El viernes", "El cartel muestra cine el viernes."),
    ],
    [
        ("Un compañero responde «Football» sin oración a «What do you do on Monday?». ¿Cómo mejoras su respuesta?", "I play football", "Se agrega sujeto y verbo."),
        ("Ordena el diálogo: A) I play football. B) Hi! C) What do you do on Monday? D) Bye!", "B, C, A, D", "Saludo, pregunta, respuesta y despedida."),
    ],
    [
        ("Cartel «My Pets»: dog - 2; cat - 1; fish - 3. Preguntan: «How many fish do you have?». ¿Qué respondes?", "I have three fish", "El cartel dice tres peces."),
        arith("En el cartel anterior, ¿cuántas mascotas hay en total?", "2+1+3", "Se suman las mascotas de cada tipo."),
    ],
    [("Cartel «Food I like»: pizza, apple, soup. Un compañero pregunta: «Do you like soup?». Si el cartel dice que te gusta, ¿qué respondes? a) Yes, I do b) No, I don't", "a)", "Responde afirmativamente porque el cartel incluye soup.")],
    [
        ("¿Qué es un cartel de apoyo?", "Una imagen que ayuda a hablar", "Poster es cartel."),
        ("¿Cómo responde bien: con una palabra o con una oración?", "Con una oración", "Así se entiende mejor."),
        ("¿Qué significa «See you»?", "Nos vemos", "Es una despedida."),
    ],
    task("Con el cartel «My Week» (lunes - fútbol; miércoles - piano; viernes - cine), prepara un diálogo de seis líneas con una persona de tu casa. Debe tener saludo, dos preguntas con What do you do on...?, dos respuestas y una despedida. Usa el cartel que dibujarás en tu hoja.", "A: Hi! B: Hello! A: What do you do on Monday? B: I play football. A: What do you do on Friday? B: I watch a film. A: Bye!", ["saludo", "dos preguntas", "dos respuestas completas", "despedida"], ["cartel dibujado", "nota del adulto"], ["respuestas de una palabra", "olvidar la despedida"], "Aplaude el diálogo y practica con él las respuestas completas."),
    "Mira tu cartel y pregunta a una persona de tu casa: What do you do on Monday?",
    "Dibuja un cartel de tus tres comidas favoritas y escribe tres preguntas con Do you like...?",
)

lesson(
    OA10, 2,
    "Las diapositivas descritas en cada ejercicio y lápiz.",
    "Aprenderé a preparar y presentar una exposición breve con apoyo visual. Sirve para presentar un tema del año, como un animal o una comida, con ayuda de diapositivas.",
    ["Sé decir Today I'm going to talk about...", "Sé dar datos simples con It has... y It eats..."],
    [
        "Una presentación (presentation) tiene tres partes. En el inicio (introduction) dices el tema: «Today I'm going to talk about my favorite animal, the dog». En el desarrollo (body) das tres datos: «It has four legs. It eats meat. It likes to play». En el cierre (conclusion) dices «Thank you for listening» y preguntas «Do you have any questions?».",
        "El apoyo visual (visual support) puede ser un cartel, un dibujo o unas diapositivas (slides). Cada diapositiva tiene una idea y pocas palabras, y una imagen. Por ejemplo: diapositiva 1, título «My Dog»; diapositiva 2, «It has four legs»; diapositiva 3, «It eats meat»; diapositiva 4, «Thank you!». No leas la diapositiva: úsala para recordar.",
        "Prepara tu presentación con un orden: título, tres datos, cierre. Ensaya en voz alta con un cronómetro. Habla despacio, mira a tu audiencia y señala la imagen. Si usas un dispositivo digital, hazlo con un adulto presente y sin conectarte a internet. Un dibujo en cartulina sirve igual.",
    ],
    [("introduction", "inicio"), ("body", "desarrollo"), ("conclusion", "cierre"), ("slide", "diapositiva"), ("visual support", "apoyo visual"), ("Do you have any questions?", "¿tienen preguntas?")],
    [
        ("Ordenar diapositivas", "Diapositivas: A) «Thank you!» B) «My Dog» C) «It has four legs» D) «It eats meat». ¿En qué orden las presentas?", ["Primero el título.", "Luego los datos.", "Al final el agradecimiento."], "B, C, D, A"),
        ("Escoger la frase de inicio", "Para empezar la presentación, ¿qué dices? a) Today I'm going to talk about my dog. b) Thank you for listening.", ["El inicio presenta el tema.", "La a) lo hace.", "La b) es de cierre."], "a)"),
    ],
    [
        ("Poner mucho texto en cada diapositiva.", "El público lee y no escucha.", "Una idea y pocas palabras por diapositiva."),
        ("Leer la diapositiva en voz alta sin mirar a nadie.", "No se conecta con la audiencia.", "Usa la diapositiva como apoyo y mira a las personas."),
    ],
    [
        ("¿Cuántas partes tiene una presentación?", "Tres", "Inicio, desarrollo y cierre."),
        ("En el desarrollo, ¿cuántos datos das según el modelo?", "Tres", "Se dan tres datos."),
        ("¿Qué frase usas en el cierre? a) Thank you for listening. b) Today I'm going to talk about...", "a)", "Es el agradecimiento final."),
    ],
    [
        ("Diapositivas «My Cat»: «It has soft fur» «It sleeps a lot» «It likes fish». ¿Cuántos datos hay?", "3", "Hay tres frases."),
        ("En la presentación «My Cat», ¿cuál es un dato? a) It likes fish b) Thank you!", "a)", "It likes fish es información sobre el gato."),
        ("En la diapositiva 1 pones el título. ¿Cuál es mejor? a) My Cat b) The Cat Cat Cat Cat", "a) My Cat", "El título debe ser corto."),
    ],
    [
        ("En «Today I'm going to talk about pizza», ¿cuál es el tema de la presentación?", "La pizza", "La frase dice el tema."),
        ("¿Cuántas ideas debe tener cada diapositiva?", "Una", "Una idea y pocas palabras."),
        ("Ordena: A) Thank you for listening. B) It has four legs. C) Today I'm going to talk about my dog.", "C, B, A", "Inicio, desarrollo y cierre."),
    ],
    [
        ("Un compañero escribió doce líneas en una diapositiva. ¿Qué consejo le das?", "Dejar una idea y pocas palabras", "Una diapositiva debe ser breve."),
        ("Elige el cierre más adecuado: a) Thank you for listening. Do you have any questions? b) Goodbye, I don't know.", "a)", "Agradece y pregunta."),
    ],
    [
        arith("Tu presentación tiene 4 diapositivas y cada una dura 30 segundos. ¿Cuántos segundos dura en total?", "4*30", "Se multiplican las diapositivas por los segundos de cada una."),
        arith("Tienes 3 minutos, que son 180 segundos, y cada diapositiva dura 30 segundos. ¿Cuántas diapositivas caben?", "180//30", "Se divide el tiempo total entre lo que dura cada diapositiva."),
    ],
    [("Preparas una presentación sobre «My Favorite Food». ¿Qué apoyo visual usas? a) un dibujo de la comida b) una foto de un auto", "a)", "El dibujo se relaciona con el tema.")],
    [
        ("¿Qué es una diapositiva?", "Una página de apoyo con una idea y una imagen", "Slide es diapositiva."),
        ("¿Qué frase abre la presentación?", "Today I'm going to talk about...", "Es la frase de inicio."),
        ("¿Qué haces con la diapositiva mientras hablas?", "La uso como apoyo y miro a la audiencia", "No se lee solo."),
    ],
    task("Prepara una presentación de cuatro diapositivas sobre tu animal favorito. En tu hoja dibuja las cuatro diapositivas: título, dos datos con dibujo (por ejemplo, It has... / It eats...) y cierre con Thank you!. Después preséntala en voz alta a una persona de tu casa, usando el inicio Today I'm going to talk about... y mirándola mientras hablas.", "1 My Dog; 2 It has four legs; 3 It eats meat; 4 Thank you! Presentación con inicio y cierre.", ["cuatro diapositivas", "inicio y cierre", "mira a la audiencia"], ["hoja con diapositivas", "nota del adulto"], ["muchas palabras por diapositiva", "olvidar el cierre"], "Aplaude las diapositivas claras y ensaya con él el inicio y el cierre."),
    "Practica en voz alta tu frase de inicio y la de cierre frente a un espejo o a una persona.",
    "Prepara otra presentación de tres diapositivas sobre tu comida favorita.",
)

lesson(
    OA10, 3,
    "Las situaciones de grupo escritas en cada ejercicio y lápiz.",
    "Aprenderé a trabajar en una actividad grupal en inglés: repartir roles, dar turnos y usar frases para colaborar. Sirve para planear algo en grupo hablando inglés.",
    ["Sé que en un grupo hay turnos.", "Conozco Let's... y I agree."],
    [
        "En una actividad grupal (group activity) cada persona tiene un rol (role). Roles comunes: leader (líder, organiza), secretary (secretario, anota), speaker (portavoz, presenta) y timekeeper (quien controla el tiempo). Elegir roles evita confusiones y deja trabajar a todos.",
        "Para colaborar usa frases: «Let's start» (empecemos), «What do you think?» (¿qué piensas?), «I agree» (estoy de acuerdo), «Good idea!» (¡buena idea!), «Your turn» (tu turno), «Can you repeat, please?» (¿puedes repetir?) y «I have a question» (tengo una pregunta). Estas frases son corteses y ayudan a seguir un orden.",
        "Un buen grupo escucha, espera su turno y respeta las ideas de los demás. Si no estás de acuerdo, di «I see your point, but I think...» (entiendo tu punto, pero creo que...). Al final, el portavoz presenta lo que decidió el grupo. Usa un cartel con el plan escrito.",
    ],
    [("leader", "líder"), ("secretary", "secretario"), ("speaker", "portavoz"), ("timekeeper", "quien controla el tiempo"), ("Let's start", "empecemos"), ("Your turn", "tu turno")],
    [
        ("Elegir un rol", "Un grupo de cuatro necesita a alguien que anote las ideas. ¿Qué rol es? a) secretary b) timekeeper", ["Anotar ideas es escribir.", "La secretaria o el secretario anota.", "El rol es secretary."], "a)"),
        ("Usar una frase", "Quieres que otra persona hable. ¿Qué dices? a) Your turn b) Let's start", ["Quiero pasar el turno.", "Your turn significa tu turno.", "Digo Your turn."], "a) Your turn"),
    ],
    [
        ("Hablar todos a la vez.", "No se entiende nada.", "Espera tu turno y escucha."),
        ("Decir «No!» sin explicar cuando no estás de acuerdo.", "Es poco amable.", "Di I see your point, but I think..."),
    ],
    [
        ("¿Qué hace el timekeeper?", "Controla el tiempo", "Time es tiempo."),
        ("¿Qué significa «Good idea!»?", "¡Buena idea!", "Se usa para apoyar una propuesta."),
        ("¿Qué frase usas para empezar el trabajo? a) Let's start b) Goodbye", "a)", "Let's start es empecemos."),
    ],
    [
        ("Un compañero propone hacer un cartel de animales. ¿Cómo muestras que estás de acuerdo? a) I agree b) I disagree", "a) I agree", "Agree es estar de acuerdo."),
        ("No entendiste lo que dijo un compañero. ¿Qué dices? a) Can you repeat, please? b) Good idea!", "a)", "Se pide repetir."),
        ("Un grupo de cuatro tiene los roles leader, secretary, speaker y timekeeper. ¿Cuántos roles hay?", "4", "Son cuatro roles distintos."),
    ],
    [
        ("Estás en desacuerdo y quieres decirlo con cortesía. ¿Qué frase eliges? a) I see your point, but I think... b) You are wrong.", "a)", "La primera frase es cortés."),
        ("¿Qué significa «Can you repeat, please?»", "¿Puedes repetir, por favor?", "Se usa para pedir que repitan."),
        arith("En un grupo de 4 integrantes, cada uno habla 2 minutos. ¿Cuántos minutos hablan entre todos?", "4*2", "Se multiplican los integrantes por los minutos."),
    ],
    [
        arith("Un grupo tiene 20 minutos. Dedican 5 a pensar, 10 a hacer el cartel y el resto a ensayar. ¿Cuántos minutos ensayan?", "20-5-10", "Se restan al total los minutos de pensar y de hacer el cartel."),
        ("Un compañero siempre habla sin dejar hablar a otros. ¿Qué frase le dices? a) Your turn, please b) I agree", "a)", "Se le recuerda el orden de los turnos."),
    ],
    [
        ("Un grupo debe presentar un cartel. ¿Quién debería hablar frente al curso? a) El speaker b) El secretary", "a) El speaker", "El speaker o portavoz presenta."),
        ("Si el grupo quiere decidir entre dos colores, ¿qué pregunta usa? a) What do you think? b) Where is the bus?", "a)", "What do you think? pide opiniones."),
    ],
    [("Tu grupo prepara una presentación sobre las frutas con 3 carteles. Cada integrante hace 1 cartel. ¿Cuántos integrantes hay?", "3", "3 carteles y un cartel por integrante.")],
    [
        ("¿Qué significa «Your turn»?", "Tu turno", "Se usa para pasar la palabra."),
        ("¿Qué es el leader?", "Quien organiza el grupo", "Leader es líder."),
        ("¿Qué frase usas para pedir una opinión?", "What do you think?", "Pregunta qué piensa el otro."),
    ],
    task("Imagina que tu grupo de cuatro debe presentar un cartel sobre «Our Favorite Foods». Escribe en tu hoja un diálogo de seis líneas entre cuatro integrantes en que: se reparten los roles (leader, secretary, speaker, timekeeper), alguien da una idea, otro dice I agree y otro dice Your turn.", "Leo: Let's start! Who is the leader? Ana: I am the leader. Tom: I am the secretary. Eva: I agree! I am the speaker. Leo: I am the timekeeper. Ana: Tom, your turn!", ["seis líneas", "los cuatro roles", "usa I agree y Your turn"], ["hoja con diálogo", "nota del adulto"], ["no usar frases de colaboración", "olvidar un rol"], "Aplaude la colaboración y practica con él las frases en voz alta."),
    "Practica en voz alta las frases Let's start, Good idea! y Your turn con una persona de tu casa.",
    "Escribe una lista de los cuatro roles y la tarea de cada uno.",
)

lesson(
    OA10, 4,
    "El gráfico descrito y los criterios escritos en cada ejercicio y lápiz.",
    "Aprenderé a presentar con un apoyo visual, responder preguntas del público y revisar mi presentación con criterios simples. Sirve para mejorar mi comunicación oral.",
    ["Sé armar una presentación con inicio, desarrollo y cierre.", "Sé leer un gráfico de barras simple."],
    [
        "En la presentación puedes usar un gráfico o una tabla como apoyo. Por ejemplo, un gráfico de barras: dogs 5, cats 3, fish 2 (mascotas de un curso). Para presentarlo: «This chart shows our pets. Five students have a dog, three have a cat and two have a fish» (este gráfico muestra nuestras mascotas...). Señala las barras al hablar.",
        "Después de presentar, el público puede preguntar. Preguntas comunes: «How many students have a cat?» (¿cuántos estudiantes tienen un gato?), «What is your favorite pet?» (¿cuál es tu mascota favorita?). Respondes con una oración completa: «Three students have a cat.» Si no sabes, di «I don't know, but I can find out» (no sé, pero puedo averiguarlo).",
        "Revisa tu presentación con criterios (criteria): ¿hablé claro y despacio?, ¿miré a la audiencia?, ¿usé el apoyo visual?, ¿usé palabras que aprendí?, ¿respondí las preguntas? Marca cada uno con una cruz. Así sabes qué mejorar. Una persona de tu casa puede ayudarte a evaluar.",
    ],
    [("chart", "gráfico"), ("This chart shows...", "este gráfico muestra..."), ("How many students have...?", "¿cuántos estudiantes tienen...?"), ("criteria", "criterios"), ("I don't know, but I can find out", "no sé, pero puedo averiguarlo"), ("pets", "mascotas")],
    [
        ("Presentar un gráfico", "Gráfico de mascotas: dogs 5, cats 3, fish 2. ¿Cómo dices que 5 estudiantes tienen perro? a) Five students have a dog. b) Five students have a fish.", ["Busco dogs en el gráfico.", "Dogs es 5.", "La a) lo dice bien."], "a)"),
        ("Responder una pregunta", "Preguntan: «How many students have a cat?». Según el gráfico de mascotas, ¿qué respondes?", ["Busco cats.", "Cats es 3.", "Respondo Three students have a cat."], "Three students have a cat"),
    ],
    [
        ("Responder con una sola palabra: «Three.»", "La respuesta es incompleta.", "Responde con una oración: Three students have a cat."),
        ("Inventar una respuesta si no se sabe.", "Se da un dato falso.", "Di I don't know, but I can find out."),
    ],
    [
        ("Gráfico de mascotas: dogs 5, cats 3, fish 2. ¿Cuántos estudiantes tienen peces?", "2", "El gráfico dice fish 2."),
        ("¿Qué significa «This chart shows...»?", "Este gráfico muestra...", "Es una forma de presentar un gráfico."),
        ("¿Qué criterio revisa si hablaste claro? a) Hablé claro y despacio b) Dibujé mucho", "a)", "El criterio se relaciona con la voz."),
    ],
    [
        arith("Gráfico de mascotas: dogs 5, cats 3, fish 2. ¿Cuántos estudiantes hay en total?", "5+3+2", "Se suman las tres barras."),
        arith("En el mismo gráfico, ¿cuántos más tienen perro que gato?", "5-3", "Se resta el número de gatos al de perros."),
        ("Te preguntan algo que no sabes. ¿Qué dices? a) I don't know, but I can find out. b) I know everything.", "a)", "Es honesto y cortés."),
    ],
    [
        ("Gráfico de comidas: pizza 6, soup 2, pasta 4. ¿Cuál es la barra más baja?", "soup", "El 2 es el número menor."),
        arith("En el mismo gráfico, ¿cuántos estudiantes más eligen pizza que sopa?", "6-2", "Se resta el número de sopa al de pizza."),
        ("Quieres señalar una barra mientras hablas. ¿Qué dices? a) Look at this bar b) Goodbye", "a)", "Look at this bar significa mira esta barra."),
    ],
    [
        ("Un compañero presentó el gráfico sin mirar a la audiencia ni señalar las barras. ¿Qué criterios no cumplió?", "Mirar a la audiencia y usar el apoyo visual", "Dos de los criterios no se cumplieron."),
        arith("Para evaluar tu presentación marcas 4 criterios de 5. ¿Cuántos te faltan por cumplir?", "5-4", "Se resta lo cumplido al total."),
    ],
    [
        ("Gráfico de comidas: pizza 6, soup 2, pasta 4. Preguntan: «Which food is the most popular?». ¿Qué respondes? (popular = popular)", "Pizza", "Pizza tiene el 6, el mayor número."),
        arith("En el mismo gráfico, ¿cuántos estudiantes eligieron pasta o sopa?", "4+2", "Se suman las barras de pasta y de sopa."),
    ],
    [("Tu criterio dice «Used the visual support». Presentaste con tu gráfico y lo señalaste. ¿Cumpliste el criterio?", "Sí", "Usaste el apoyo visual.")],
    [
        ("¿Qué es un criterio de evaluación?", "Una pregunta que sirve para revisar mi trabajo", "Los criterios ayudan a mejorar."),
        ("¿Qué respondes si no sabes? ", "I don't know, but I can find out", "Es una respuesta honesta y cortés."),
        ("¿Cómo respondes una pregunta: con una palabra o con una oración?", "Con una oración", "Así hablas inglés completo."),
    ],
    task("Prepara un gráfico de barras con las mascotas de tres amigos o familiares (por ejemplo, perro, gato, pez) y preséntalo en voz alta a una persona de tu casa con la frase This chart shows... Pide que te haga una pregunta con How many...? y respóndela con una oración completa. Después marca cuatro criterios: hablé claro, miré a la audiencia, usé el gráfico, respondí la pregunta.", "This chart shows our pets. Two have a dog... Pregunta: How many have a cat? Respuesta: One person has a cat. Criterios marcados.", ["usa This chart shows", "responde con una oración", "marca cuatro criterios"], ["gráfico dibujado", "nota del adulto"], ["responder con una palabra", "no marcar criterios"], "Aplaude la presentación y revisa con él los criterios marcados."),
    "Presenta oralmente el gráfico de mascotas del ejemplo, usando This chart shows...",
    "Haz otro gráfico con tres de tus actividades favoritas y práctica una presentación de 1 minuto.",
)
