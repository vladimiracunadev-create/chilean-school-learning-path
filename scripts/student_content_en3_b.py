"""Student material for 3.º básico Inglés, EN03 OA 08 (estrategias de comprensión lectora) y OA 09 (reaccionar a lo leído).

Los textos en inglés son originales, muy breves y con pista en español. Las imágenes se describen entre
corchetes porque el cuaderno no incluye ilustraciones. Cada estructura se enseña en la propia clase antes de usarla.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA8, OA9 = "EN03 OA 08", "EN03 OA 09"


def E(rows):
    return [ex(q, a, w) for q, a, w in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 08
lesson(
    OA8, 1,
    "Los títulos, las imágenes descritas y los textos escritos en cada ejercicio, lápiz y una hoja para tapar el texto mientras predices. Una persona de tu casa puede leer en voz alta.",
    "Aprenderé a predecir de qué trata un texto en inglés mirando el título y la imagen, y a confirmar o cambiar mi predicción cuando leo. Sirve para empezar a leer con una idea y entender mejor.",
    ["Sé leer palabras cortas en inglés como cat, dog, red y big.", "Sé que el título es el nombre de un texto."],
    [
        "Antes de leer, un buen lector mira el título (title) y la imagen (image) y hace una predicción. Predecir (predict) es decir qué creo que pasará o de qué trata el texto. En inglés se dice: «I think the story is about a dog» (creo que el cuento trata de un perro).",
        "Una predicción necesita una razón. La razón es una pista: una palabra del título o un objeto de la imagen. La palabra «because» significa «porque» y une la idea con su razón: «I think the story is about a dog because the picture shows a dog».",
        "Mientras lees, comparas tu idea con el texto. Si el texto dice lo mismo, confirmas (confirm) tu predicción. Si dice otra cosa, la cambias y dices «Now I think...» (ahora creo que...). Cambiar una predicción no es un error: es parte de leer bien.",
    ],
    [("predict", "predecir, decir lo que creo que pasará"), ("title", "título"), ("image", "imagen"), ("confirm", "confirmar, ver que mi idea es correcta"), ("because", "porque"), ("Now I think...", "ahora creo que...")],
    [
        ("Predecir con título e imagen", "Título: «The Little Boat». Imagen: [un bote azul pequeño en el mar]. ¿Qué predicción dices?", ["Leo el título: boat es bote.", "Miro la imagen: hay un bote en el mar.", "Digo mi idea y la razón con because."], "I think the story is about a boat because the picture shows a boat."),
        ("Cambiar la predicción", "Predije: «Mia is sad». El texto dice: «Mia has a red balloon. She is happy.» (balloon es globo; happy es contenta). ¿Qué hago con mi predicción?", ["Comparo: yo dije sad (triste).", "El texto dice happy (contenta).", "No coinciden, así que cambio mi idea."], "La cambio: Now I think Mia is happy."),
    ],
    [
        ("Dejar la predicción aunque el texto diga otra cosa.", "Se cree que la primera idea no se puede cambiar.", "Compara con el texto y cambia tu predicción con «Now I think...»."),
        ("Predecir sin mirar el título ni la imagen.", "Se adivina sin pistas.", "Mira primero el título y la imagen: son tus pistas."),
    ],
    [
        ("Título: «The Brown Dog». Imagen: [un perro café]. Completa: «I think the story is about a ___.» (perro)", "dog", "El título y la imagen hablan de un perro."),
        ("¿Qué significa «predict»?", "Predecir, decir lo que creo que pasará", "Predict es adivinar con pistas antes de leer."),
        ("¿Qué significa «because»?", "Porque", "Esta palabra une la idea con su razón."),
    ],
    [
        ("¿Qué dos pistas miras antes de leer para predecir?", "El título y la imagen", "Son lo primero que se ve de un texto."),
        ("Título: «A Rainy Day». Imagen: [un niño con un paraguas amarillo bajo la lluvia]. Elige la predicción que coincide: (a) «I think the story is about a rainy day.» (b) «I think the story is about a hot day.»", "a", "Rainy day es día de lluvia, como muestra la imagen."),
        ("Mi predicción es «The cat is sad». El texto dice: «The cat has milk. It is happy.» ¿Confirmo o cambio mi predicción?", "La cambio", "El texto dice happy, que es contento y no triste."),
    ],
    [
        ("Título: «The Big Pizza». Imagen: [una pizza grande con queso]. Completa: «I think the story is about a big ___.»", "pizza", "El título y la imagen muestran una pizza."),
        ("Predije «Tom is happy». El texto dice: «Tom is sad. He has no ball.» Escribe en inglés la palabra del texto que cambia mi idea (triste).", "sad", "Sad significa triste y el texto la dice."),
        ("Título: «The Green Frog». Elige la mejor razón: (a) «I think it is about a frog because the title says frog.» (b) «I think it is about a frog because I like cookies.»", "a", "La razón correcta es una pista del título."),
    ],
    [
        ("Ana predijo «the story is about a bird» sin mirar nada. Título: «The Funny Fish». Imagen: [un pez con un sombrero]. ¿Es buena su predicción? (fish significa pez)", "No, porque el título y la imagen muestran un pez", "Una buena predicción usa las pistas de la portada."),
        ("Predicción: «Sam is at school.» Texto: «Sam has a ball. He is in the park.» (park es parque). ¿Se mantiene la predicción?", "No, se cambia porque Sam está en el parque", "El texto dice park, no school."),
    ],
    [
        ("Título: «The Owl at Night». Imagen: [un búho en un árbol bajo la luna]. Elige la mejor predicción: (a) «I think the story is at night because the picture shows the moon.» (b) «I think the story is at school because the picture shows a tree.»", "a", "Night es noche y la luna es una pista de la noche."),
        ("Ordena los pasos para leer bien: (1) comparo con el texto, (2) miro el título y la imagen, (3) digo mi predicción. Escribe los números en orden.", "2, 3, 1", "Primero miro, luego predigo y por último comparo."),
    ],
    [("En la biblioteca ves el libro «The Yellow Duck» con [un pato amarillo en un charco] (duck significa pato). Elige la predicción: (a) «I think the story is about a duck.» (b) «I think the story is about a car.»", "a", "El título y la imagen muestran un pato.")],
    [
        ("¿Cómo se dice «imagen» en inglés?", "image", "Es la palabra inglesa para imagen."),
        ("Mi predicción no coincide con el texto. ¿Qué hago?", "La cambio y digo la idea nueva", "El texto es la prueba y corrige la predicción."),
        ("¿Qué significa «Now I think...»?", "Ahora creo que...", "Se usa para decir la idea nueva."),
    ],
    task("Estas son tres portadas: (1) «My Green Frog», imagen: [una rana en una hoja]; (2) «The Birthday Cake», imagen: [una torta con velas]; (3) «The Funny Dog», imagen: [un perro con un sombrero]. Para cada una di en voz alta «I think the story is about a ___ because the picture shows a ___». Después la otra persona lee «The frog is on a log» (log es tronco) y tú dices si mantienes o cambias la primera predicción.", "«I think the story is about a frog because the picture shows a frog.»", ["usa el título o la imagen como pista", "dice «I think...» en las tres portadas", "da una razón con because", "dice si mantiene o cambia la predicción"], ["nota de la persona que escuchó las tres frases"], ["predecir sin dar una razón", "no mirar la imagen"], "Reconoce cada predicción con su razón y repite despacio con el niño o la niña la frase que le costó."),
    "Mira la portada de un libro de tu casa y di en español de qué crees que trata y por qué.",
    "Inventa un título corto en inglés, por ejemplo «The Happy Cat», dibuja la imagen y di qué predice tu portada.",
)

lesson(
    OA8, 2,
    "Los textos escritos en cada ejercicio, lápiz y una hoja para tapar las palabras. Una persona de tu casa puede leer en voz alta.",
    "Aprenderé a usar lo que ya sé para entender un texto corto en inglés, con cuidado de no suponer lo que el texto no dice. Sirve para entender aunque no conozca todas las palabras.",
    ["Sé algunas palabras en inglés: cat, dog, red, blue.", "Sé predecir con el título y la imagen."],
    [
        "Cuando lees no empiezas de cero: ya sabes cosas. Eso se llama conocimientos previos (prior knowledge). Si el texto habla de un hospital, ya sabes que ahí hay doctores. Usar lo que sabes ayuda a entender palabras nuevas.",
        "Algunas palabras en inglés se parecen al español: family (familia), animal (animal), music (música), chocolate (chocolate), color (color), park (parque). Son buenas pistas. Pero ten cuidado: «library» se parece a «librería», y significa biblioteca. «Carpet» se parece a «carpeta», y significa alfombra. Por eso hay que revisar con el resto de la oración.",
        "Usa lo que sabes con cuidado: el texto manda. Si el texto dice «The dog has a hat» (el perro tiene un sombrero), eso es lo que ocurre en la historia, aunque en la vida real los perros no usan sombrero. Primero lee, después conecta con lo que sabes.",
    ],
    [("prior knowledge", "lo que ya sé"), ("family", "familia"), ("library", "biblioteca"), ("carpet", "alfombra"), ("hospital", "hospital"), ("hat", "sombrero")],
    [
        ("Usar lo que ya sé", "Lee: «The doctor is in the hospital.» (doctor y hospital se parecen al español). ¿Dónde crees que está el doctor?", ["Conozco doctor y hospital.", "Sé que un doctor trabaja en un hospital.", "Junto las dos ideas."], "El doctor está en el hospital."),
        ("Ojo con una palabra parecida", "Lee: «There is a blue carpet in the room.» Una niña cree que carpet es carpeta. ¿Qué significa en realidad?", ["Carpet se parece a carpeta.", "Pero «blue carpet in the room» (alfombra azul en la pieza) tiene más sentido.", "Reviso con el resto de la oración y con lo que sé."], "Carpet significa alfombra."),
    ],
    [
        ("Pensar que una palabra parecida siempre significa lo mismo.", "Se confía solo en el parecido.", "Revisa la palabra con el resto de la oración."),
        ("Cambiar lo que dice el texto porque no calza con lo que yo sé.", "Se olvida que el texto cuenta su propia historia.", "Lee lo que el texto dice y después conéctalo con lo que sabes."),
    ],
    [
        ("¿Qué palabra en inglés se parece a «música»?", "music", "Se escribe casi igual en inglés."),
        ("¿Cómo se dice «familia» en inglés?", "family", "Se parece mucho al español."),
        ("¿Qué significa «prior knowledge»?", "Lo que ya sé", "Prior es antes y knowledge es conocimiento."),
    ],
    [
        ("¿Para qué sirve pensar en lo que ya sé antes de leer?", "Para entender mejor y adivinar palabras nuevas", "Mis ideas previas se conectan con el texto."),
        ("¿Qué significa «library» en español?", "Biblioteca", "Parece librería, pero es el lugar de los libros."),
        ("El texto dice «The dog has a hat». ¿Qué tiene el perro según el texto?", "Un sombrero", "El texto manda aunque no sea común."),
    ],
    [
        ("Texto: «Mom has chocolate and a guitar.» Escribe las dos palabras del texto que se parecen al español.", "chocolate, guitar", "Se escriben casi igual que en español."),
        ("Texto: «The doctor is in the hospital.» Con lo que sabes, ¿qué persona cuida a las personas enfermas? Escribe la palabra en inglés del texto.", "doctor", "Doctor es la persona que cuida la salud."),
        ("Texto: «The cat drinks milk.» (drinks es toma). Con lo que sabes de los gatos, ¿qué crees que significa «milk»? (a) leche (b) piedra", "a", "Un gato toma leche, no piedra."),
    ],
    [
        ("Texto: «Anna plays the piano. She likes music.» ¿Qué crees que significa «plays the piano»? Responde en español.", "Toca el piano", "Piano y music son pistas conocidas."),
        ("Pedro dice que «park» no puede entenderse porque está en inglés. ¿Cómo lo ayudas?", "Park se parece a parque, una palabra que conoce", "Las palabras parecidas son una pista."),
    ],
    [
        ("Texto: «The animal is big and brown.» ¿Qué palabra del texto se parece a «animal» en español? Escríbela.", "animal", "Se escribe igual en los dos idiomas."),
        ("Texto: «The family is in the kitchen.» (kitchen es cocina). Con lo que sabes, ¿dónde está la familia? Responde en español.", "En la cocina", "Kitchen es el lugar de la casa donde se cocina."),
    ],
    [("Un cartel en el colegio dice: «Library: quiet, please.» (quiet es en silencio). Con lo que sabes, ¿qué lugar es la library? Responde en español.", "La biblioteca", "El silencio y los libros son pistas de la biblioteca.")],
    [
        ("¿Cómo se dice «parque» en inglés?", "park", "Se parece mucho a la palabra en español."),
        ("¿Qué haces con una palabra que se parece al español?", "La reviso con el resto de la oración", "Revisar evita errores como librería y library."),
        ("¿Qué significa «carpet»?", "Alfombra", "Se parece a carpeta, pero significa alfombra."),
    ],
    task("Lee con una persona de tu casa: «The family is in the park. Dad has a guitar. The dog has a hat. The library is next to the park.» (next to es al lado de). Subraya con lápiz las palabras que se parecen al español. Luego di en español de qué trata el texto y qué dice el texto sobre el perro, sin cambiarlo.", "Subrayo family, park, guitar, library. El texto trata de una familia en un parque. El perro tiene un sombrero.", ["subraya al menos cuatro palabras conocidas", "usa lo que sabe para entender", "dice en español qué dice el texto sobre el perro", "revisa library con el resto del texto"], ["el texto subrayado", "nota de la persona que escuchó"], ["subrayar solo una palabra", "decir que el perro no puede tener sombrero"], "Celebra las palabras que reconoció y ayuda a unirlas en una sola idea."),
    "Escribe cinco palabras en inglés que se parezcan al español y dibuja una al lado de cada una.",
    "Busca en casa tres objetos con una etiqueta en inglés y adivina qué dicen, revisando con el dibujo o con el producto.",
)

lesson(
    OA8, 3,
    "Los textos y las imágenes descritas en cada ejercicio; lápiz.",
    "Aprenderé a relacionar el texto con la imagen que lo acompaña. Sirve para comprobar que entendí y para entender palabras nuevas.",
    ["Sé predecir con título e imagen.", "Sé colores y animales básicos en inglés."],
    [
        "Las imágenes ayudan a entender el texto. Una imagen puede mostrar personajes, lugares y acciones. A una ayuda que da la imagen se le llama picture clue (pista de la imagen).",
        "Para usarla, sigue tres pasos. Primero mira la imagen y di qué ves. Luego lee la oración. Por último compara (compare): ¿la oración dice lo que muestra la imagen? Si coincide, la oración y la imagen «match» (hacen pareja). Si no coincide, vuelve a mirar y a leer.",
        "Una imagen también ayuda con una palabra nueva. Si el texto dice «The cat is on the mat» y la imagen muestra un gato sentado sobre una alfombrita, entiendes que mat es esa alfombrita. Pero la imagen no muestra todo: por ejemplo, no dice el nombre del gato. Usa siempre la imagen y el texto juntos.",
    ],
    [("picture clue", "pista que da la imagen"), ("match", "coincidir, hacer pareja"), ("compare", "comparar"), ("mat", "alfombrita"), ("on", "sobre, encima de"), ("hat", "sombrero")],
    [
        ("Imagen y oración", "Imagen: [una niña con un sombrero azul]. Oración: «The girl has a blue hat.» ¿La oración coincide con la imagen?", ["Miro la imagen: sombrero azul.", "Leo: blue hat.", "Coinciden."], "Sí, coincide."),
        ("Palabra nueva con la imagen", "Texto: «The cat is on the mat.» Imagen: [un gato sentado sobre una alfombrita]. ¿Qué crees que es «mat»?", ["Veo un gato sobre una alfombrita.", "El texto dice on the mat.", "Mat es lo que está debajo del gato."], "Una alfombrita."),
    ],
    [
        ("Leer sin mirar la imagen.", "Se pierde una pista importante.", "Mira la imagen antes de leer y compárala después."),
        ("Creer que la imagen cuenta todo el texto.", "Se olvida que el texto tiene más información.", "Usa la imagen y el texto juntos."),
    ],
    [
        ("¿Qué es un «picture clue»?", "Una pista que da la imagen", "Picture es imagen y clue es pista."),
        ("Imagen: [un perro café]. Oración: «The dog is brown.» (brown es café). ¿Coincide? Responde sí o no.", "Sí", "La imagen muestra un perro café."),
        ("¿Qué significa «match»?", "Coincidir, hacer pareja", "Se usa cuando imagen y oración dicen lo mismo."),
    ],
    [
        ("¿Cuáles son los tres pasos para usar la imagen con el texto?", "Miro la imagen, leo la oración y comparo", "Así compruebo si entendí."),
        ("¿Para qué sirve comparar la imagen con la oración?", "Para ver si entendí bien", "Si coinciden, la comprensión es correcta."),
        ("¿Por qué no basta solo la imagen para entender un texto?", "Porque el texto tiene más información", "La imagen no lo muestra todo."),
    ],
    [
        ("Imagen: [dos pelotas rojas]. Oración: «I have two red balls.» (balls es pelotas). ¿Coincide? Responde sí o no.", "Sí", "Two red balls son dos pelotas rojas."),
        ("Imagen: [un pájaro sobre una casa]. Oración: «The bird is in the house.» (in es dentro de; house es casa). ¿Coincide? Responde sí o no.", "No", "La imagen muestra el pájaro sobre la casa, no dentro."),
        ("Imagen: [un niño con una manzana]. Elige la oración que coincide: (a) «The boy has an apple.» (b) «The boy has a hat.»", "a", "Apple es manzana."),
    ],
    [
        ("Imagen: [una vaca blanca en el pasto]. Oración: «The cow is white.» (cow es vaca; white es blanca). Un niño dice que no coincide porque la vaca es negra. ¿Quién tiene razón según la imagen?", "La oración, porque la vaca es blanca", "La imagen muestra una vaca blanca."),
        ("Texto: «The kitten is under the table.» (kitten es gatito; table es mesa). Imagen: [un gatito bajo una mesa]. Con la imagen, ¿qué crees que significa «under»?", "Debajo de", "El gatito está bajo la mesa."),
    ],
    [
        ("Imagen: [tres niños jugando]. Elige el texto que coincide: (a) «Three children play.» (b) «One child sleeps.» (children son niños; sleeps es duerme)", "a", "Three children son tres niños y la imagen muestra niños jugando."),
        ("Imagen: [una niña que sonríe]. Completa: «The girl is ___.» Opciones: sad (triste) / happy (contenta). Escribe la palabra.", "happy", "Una niña que sonríe está contenta."),
    ],
    [("Un cuento dice: «Leo has a red kite.» y su imagen muestra [un niño con una cometa azul]. ¿Qué parte de la oración no coincide con la imagen? (kite es cometa)", "El color, red", "La cometa de la imagen es azul, no roja.")],
    [
        ("¿Cómo se dice «sombrero» en inglés?", "hat", "Es la palabra inglesa para sombrero."),
        ("Si la oración y la imagen no coinciden, ¿qué hago?", "Vuelvo a mirar y a leer", "Así busco la diferencia."),
        ("¿Qué significa «on» en «on the mat»?", "Sobre", "On indica que algo está encima."),
    ],
    task("Imagen A: [un gato negro sobre una mesa]. Imagen B: [dos manzanas rojas dentro de una caja]. Oraciones: (1) «The black cat is on the table.» (table es mesa) (2) «Two red apples are in the box.» (in es dentro de; box es caja) (3) «The cat is under the table.» Une cada oración con la imagen que corresponde y escribe cuál oración no coincide con ninguna imagen. Después dibuja una imagen para esa oración.", "La oración 1 va con A; la 2 va con B; la 3 no coincide con ninguna y la dibujo con el gato debajo de la mesa.", ["une las oraciones 1 y 2 con la imagen correcta", "identifica la oración 3 como sin pareja", "dibuja la oración 3 con el gato debajo de la mesa", "explica con la palabra on, in o under"], ["el dibujo", "nota de la persona que escuchó"], ["unir por el color sin leer toda la oración", "ignorar la palabra under"], "Pregunta qué palabra de la oración le dio la pista y repite en voz alta on, in y under."),
    "Mira una imagen de un libro de casa y di en español una cosa que la imagen cuenta y otra que no cuenta.",
    "Escribe una oración en inglés sobre un dibujo tuyo, por ejemplo «The cat is on the mat», y pide a alguien que diga si coincide.",
)

lesson(
    OA8, 4,
    "Los textos escritos en cada ejercicio, un lápiz para subrayar y una persona de tu casa para leer en voz alta.",
    "Aprenderé a releer un texto para buscar la respuesta a una pregunta concreta, y a leer en voz alta para escuchar mejor las oraciones. Sirve para no adivinar y responder con pruebas del texto.",
    ["Sé predecir y usar la imagen.", "Sé que Who, What y Where son palabras para preguntar."],
    [
        "Releer (reread) es leer otra vez. Es útil cuando tienes una pregunta concreta. Primero lee la pregunta. Luego vuelve al texto, busca la palabra clave y subraya la oración que contiene la respuesta. No necesitas leer todo de nuevo con la misma atención.",
        "Las preguntas empiezan con palabras que debes conocer: Who (quién), What (qué), Where (dónde), What color (de qué color). Si la pregunta empieza con Who, buscas una persona o un animal. Si empieza con Where, buscas un lugar. Si dice What color, buscas un color.",
        "Leer en voz alta (read aloud) también ayuda: al escuchar las oraciones despacio, entiendes mejor dónde empieza y dónde termina cada idea. Puedes leer en voz alta tú mismo o escuchar a una persona de tu casa. Siempre vuelve al texto para comprobar tu respuesta.",
    ],
    [("reread", "leer otra vez"), ("read aloud", "leer en voz alta"), ("Who?", "¿quién?"), ("What?", "¿qué?"), ("Where?", "¿dónde?"), ("What color?", "¿de qué color?")],
    [
        ("Releer para una pregunta", "Texto: «Lia has a small dog. The dog is white. They go to the park.» Pregunta: What color is the dog? (white es blanco)", ["Leo la pregunta: busco un color.", "Releo y encuentro the dog is white.", "Subrayo white."], "El perro es blanco (white)."),
        ("Quién y dónde", "Mismo texto. Pregunta: Where do they go? (park es parque)", ["La pregunta Where busca un lugar.", "Releo la última oración: They go to the park.", "El lugar es el parque."], "Van al parque (the park)."),
    ],
    [
        ("Responder sin volver al texto.", "Se contesta con lo primero que se recuerda.", "Relee y subraya la oración que contiene la respuesta."),
        ("Leer toda la pregunta como si fuera una sola palabra.", "No se mira la primera palabra de la pregunta.", "Mira Who, What, Where o What color para saber qué buscar."),
    ],
    [
        ("¿Qué significa «reread»?", "Leer otra vez", "Re significa otra vez y read es leer."),
        ("¿Qué significa «Where?»", "¿Dónde?", "Pregunta por un lugar."),
        ("¿Qué significa «read aloud»?", "Leer en voz alta", "Aloud es en voz alta."),
    ],
    [
        ("¿Qué busca una pregunta que empieza con «Who»?", "Una persona o un animal", "Who pregunta por quién."),
        ("¿Qué busca una pregunta que empieza con «What color»?", "Un color", "Pregunta de qué color es algo."),
        ("¿Para qué subrayas la oración de la respuesta?", "Para tener la prueba en el texto", "La oración subrayada muestra de dónde viene la respuesta."),
    ],
    [
        ("Texto: «Lia has a small dog. The dog is white.» Pregunta: Who has a dog? Escribe el nombre.", "Lia", "El texto dice Lia has a small dog."),
        ("Texto: «Tom has a green bag. His bag is on the chair.» (chair es silla). Pregunta: What color is the bag? Escribe la palabra en inglés.", "green", "El texto dice green bag."),
        ("Texto: «The cat is on the chair.» Pregunta: Where is the cat? Responde en español.", "Sobre la silla", "On the chair significa sobre la silla."),
    ],
    [
        ("Texto: «Sam has a red ball. Mia has a blue ball.» Pregunta: What color is the ball Mia has? (blue es azul). Escribe la palabra en inglés.", "blue", "La pelota de Mia es blue."),
        ("Texto: «Ana reads a book in the library.» Pregunta: Where does Ana read? Responde en español.", "En la biblioteca", "In the library es en la biblioteca."),
    ],
    [
        ("Texto: «Leo has a small cat. The cat is black. It sleeps on the carpet.» (sleeps es duerme). Pregunta: Where does the cat sleep? Responde en español.", "Sobre la alfombra", "On the carpet es sobre la alfombra."),
        ("Texto: «Pip is a mouse. Pip has a big hat. The hat is red.» (mouse es ratón). Pregunta: What color is the hat? Escribe la palabra en inglés.", "red", "El texto dice the hat is red."),
    ],
    [("Tu profesora te da la pregunta «Who has the kite?» y el texto «Tom has the kite. Mia has the ball.» (kite es cometa; ball es pelota). Escribe el nombre que responde la pregunta.", "Tom", "El texto dice que Tom tiene la cometa.")],
    [
        ("¿Qué significa «Who?»", "¿Quién?", "Pregunta por una persona."),
        ("Si no encuentras la respuesta, ¿qué haces?", "Releo el texto con la pregunta en mente", "Releer ayuda a encontrar la oración."),
        ("¿Qué ayuda a escuchar mejor las oraciones del texto?", "Leer en voz alta", "Al leer despacio se oyen las ideas."),
    ],
    task("Lee en voz alta, con una persona de tu casa, este texto más largo: «Mia has a small bird. The bird is yellow. Its name is Sunny. Sunny sings in the garden every morning. Mia gives Sunny water and seeds. Then Sunny sits on Mia's hand.» (Its name is Sunny es: Se llama Sunny; sings es canta; garden es jardín; every morning es todas las mañanas; Mia's hand es la mano de Mia; gives es da; water es agua; seeds son semillas; then es luego; sits es se sienta). Responde las preguntas, releyendo y subrayando la oración que te da cada respuesta: (1) Who has a bird? (2) What color is the bird? (3) Where does the bird sing? (4) Where does Sunny sit at the end?", "(1) Mia. (2) Yellow. (3) In the garden. (4) On Mia's hand. Subrayo cada oración.", ["lee en voz alta el texto", "responde las cuatro preguntas", "subraya la oración de cada respuesta", "relee antes de responder"], ["el texto subrayado", "nota de la persona que escuchó"], ["responder de memoria", "no mirar la primera palabra de la pregunta"], "Pide que muestre con el dedo la oración de la respuesta y celebra que vuelva al texto."),
    "Lee en voz alta dos veces el texto de la tarea y di si la segunda lectura te ayudó a entender más.",
    "Escribe en español dos preguntas que se puedan responder con el texto de la tarea y pide a alguien que las responda releyendo.",
)

lesson(
    OA8, 5,
    "Los textos escritos en cada ejercicio, lápices de colores o un lápiz grafito y una hoja para dibujar. Una persona de tu casa para escuchar.",
    "Aprenderé a elegir una estrategia para reparar mi comprensión cuando no entiendo, y a explicar por qué la elegí. Sirve para seguir leyendo sin quedarme atascado.",
    ["Sé predecir, usar la imagen y releer.", "Sé que read aloud es leer en voz alta."],
    [
        "A veces no entiendes una parte del texto. Reparar la comprensión (repair) es usar una estrategia para entender mejor. Hay cinco estrategias: reread (leer otra vez), look at the picture (mirar la imagen), read aloud (leer en voz alta), draw (dibujar lo que entendí) y retell (contar con tus palabras lo que pasó, con ayuda de otra persona).",
        "Elegir bien depende del problema. Si no sabes qué dice una oración, relee. Si el texto tiene una imagen que muestra la palabra nueva, mira la imagen. Si una oración se te enreda al leerla, léela en voz alta. Si quieres mostrar que entendiste, dibuja o cuenta lo que pasó.",
        "Después de usar la estrategia, explica en pocas palabras qué hiciste: «I reread the sentence», «I look at the picture», «I read aloud», «I draw», «I retell the story». Significan: releo la oración, miro la imagen, leo en voz alta, dibujo, cuento la historia. Si todavía no entiendes, prueba otra estrategia.",
    ],
    [("repair", "reparar, arreglar la comprensión"), ("reread", "leer otra vez"), ("look at the picture", "mirar la imagen"), ("read aloud", "leer en voz alta"), ("draw", "dibujar"), ("retell", "contar otra vez con mis palabras")],
    [
        ("Palabra nueva con imagen", "Texto: «Dad has a kite.» Imagen: [un papá con una cometa en la mano]. No conoces la palabra kite. ¿Qué estrategia usas?", ["El problema es una palabra nueva.", "Hay una imagen que la muestra.", "Miro la imagen."], "Look at the picture: kite es cometa."),
        ("Mostrar que entendí", "Leíste: «A small cat sleeps on a chair.» Quieres mostrar lo que entendiste sin hablar. ¿Qué estrategia usas?", ["Quiero mostrarlo sin hablar.", "Puedo dibujarlo.", "Dibujo un gato pequeño sobre una silla."], "Draw: dibujo un gato durmiendo en una silla."),
    ],
    [
        ("Usar siempre la misma estrategia sin pensar en el problema.", "Se cree que una sola sirve para todo.", "Elige la estrategia según el problema."),
        ("Dejar de leer cuando algo no se entiende.", "Se piensa que no hay solución.", "Usa una estrategia de reparación y sigue leyendo."),
    ],
    [
        ("¿Qué significa «repair»?", "Reparar, arreglar la comprensión", "Se usa cuando algo no se entendió."),
        ("¿Cómo se dice «dibujar» en inglés?", "draw", "Es la palabra inglesa para dibujar."),
        ("¿Qué significa «retell»?", "Contar otra vez con mis palabras", "Re es otra vez y tell es contar."),
    ],
    [
        ("No entiendes una oración larga. ¿Qué estrategia usas primero? (a) reread (b) look at the picture", "a", "Releer ayuda cuando la oración no se entiende."),
        ("La palabra nueva aparece al lado de una imagen que la muestra. ¿Qué estrategia usas? (a) look at the picture (b) read aloud", "a", "La imagen muestra el significado de la palabra."),
        ("¿Por qué se explica qué estrategia usaste?", "Para saber qué hice y por qué", "Explicar muestra que tomé una decisión."),
    ],
    [
        ("Completa: «I ___ the sentence.» (releo)", "reread", "Reread es leer otra vez."),
        ("Completa: «I look at the ___.» (imagen)", "picture", "Picture es imagen."),
        ("Quieres mostrar lo que entendiste con un dibujo. Completa: «I ___.»", "draw", "Draw es dibujar."),
    ],
    [
        ("Ana lee muy rápido y no sabe quién tiene la pelota. Elige una estrategia: (a) retell (b) reread", "b", "Releer sirve para buscar quién tiene la pelota."),
        ("Leo no entiende «The bird is on the nest» (nest es nido), pero la imagen muestra un pájaro sobre un nido. ¿Qué estrategia usa?", "Look at the picture", "La imagen aclara la palabra nest."),
    ],
    [
        ("Texto: «The cat drinks milk. Then it sleeps.» (then es luego). Después de leer, cuentas con ayuda lo que pasó. ¿Qué estrategia usas?", "Retell", "Contar lo que pasó es retell."),
        ("Texto: «Sam jumps. Sam runs. Sam is tired.» (tired es cansado). Una palabra se te enreda al leer y quieres escucharla. ¿Qué estrategia usas?", "Read aloud", "Leer en voz alta ayuda a escuchar las palabras."),
    ],
    [("Lees: «Mia has a red balloon» y no sabes qué es balloon, pero no hay imagen. ¿Qué estrategia usas primero? (a) reread la oración y buscar pistas (b) look at the picture", "a", "No hay imagen, así que se relee y se usan las otras palabras.")],
    [
        ("¿Cómo se dice «leer en voz alta» en inglés?", "read aloud", "Es una estrategia para escuchar el texto."),
        ("¿Cuál es la mejor estrategia para una palabra que se muestra en una imagen?", "Look at the picture", "La imagen da la pista."),
        ("Si una estrategia no funciona, ¿qué haces?", "Pruebo otra", "Se puede cambiar de estrategia."),
    ],
    task("Lee con una persona de tu casa este texto más largo: «The little mouse has a big hat. The hat is red. The mouse jumps and the hat jumps too. Then the mouse runs to the garden. The cat is in the garden. The mouse is not happy. It runs home.» (mouse es ratón; jumps es salta; too es también; then es luego; runs es corre; garden es jardín; home es a casa). Elige una estrategia de reparación para una parte que te cueste: reread, read aloud, draw o retell. Úsala, di en español por qué la elegiste y di una frase en inglés: «I reread», «I read aloud», «I draw» o «I retell». Termina contando con tus palabras qué pasó.", "Releo la última parte porque no entendía por qué el ratón corre a casa. Digo: «I reread». Cuento: el ratón salta, va al jardín, ve al gato y corre a casa.", ["lee el texto", "elige una estrategia", "explica por qué la eligió", "dice la frase en inglés de su estrategia", "cuenta qué pasó con sus palabras"], ["el dibujo o la nota de la persona que escuchó"], ["elegir sin explicar", "no probar otra si la primera no ayuda"], "Valora que explique su decisión y sugiere otra estrategia si no entendió."),
    "Cuenta en español a una persona de tu casa qué estrategia usas tú cuando no entiendes algo.",
    "Dibuja el texto del ratón y el sombrero y escribe una frase en inglés bajo el dibujo, por ejemplo «The hat is red».",
)

# ================================================================ OA 09
lesson(
    OA9, 1,
    "Los textos escritos en cada ejercicio, lápices de colores y una hoja en blanco.",
    "Aprenderé a mostrar lo que entendí de un texto con una ilustración que tenga una idea del texto como prueba. Sirve para responder a la lectura sin tener que escribir mucho.",
    ["Sé leer oraciones cortas.", "Sé algunos colores y objetos en inglés."],
    [
        "Reaccionar a lo leído es mostrar lo que entendiste y lo que sentiste. Una forma es hacer una ilustración (illustration): un dibujo que muestra una idea del texto. Por ejemplo, el texto «Tom has a red kite» se ilustra con un niño que tiene una cometa roja.",
        "Una buena ilustración usa pruebas del texto: los personajes, los colores, el lugar y lo que hacen. Antes de dibujar, subraya en el texto las palabras que vas a mostrar. Por ejemplo: «The kite is in the tree» (la cometa está en el árbol). Si dibujas la cometa en el suelo, no coincide con el texto.",
        "También puedes mostrar una preferencia (preference), lo que te gusta. Dibuja tu parte favorita y escribe «I like...» (me gusta...). Pero primero la ilustración debe ser fiel al texto. Después puedes agregar colores y detalles propios, como el cielo, que no cambien lo que el texto dice.",
    ],
    [("illustration", "ilustración, dibujo que muestra una idea"), ("kite", "cometa"), ("tree", "árbol"), ("preference", "preferencia, lo que me gusta"), ("I like...", "me gusta..."), ("favorite", "favorito")],
    [
        ("Dibujar una idea con pruebas", "Texto: «Tom has a red kite. The kite is in the tree.» ¿Qué debe mostrar la ilustración?", ["Subrayo Tom, red kite y in the tree.", "Dibujo a Tom.", "Dibujo la cometa roja en el árbol."], "Tom y una cometa roja dentro del árbol."),
        ("Revisar una ilustración", "Texto: «Mia has a blue hat.» Un dibujo muestra una niña con un sombrero verde. ¿Es fiel al texto?", ["El texto dice blue (azul).", "El dibujo muestra verde.", "No coincide."], "No: el sombrero debe ser azul."),
    ],
    [
        ("Dibujar algo que no está en el texto.", "Se agrega una idea propia que cambia el texto.", "Dibuja primero lo que el texto dice."),
        ("Dibujar sin subrayar antes las pistas.", "Se olvida un color o un lugar.", "Subraya los personajes, los colores y el lugar."),
    ],
    [
        ("¿Qué es una «illustration»?", "Un dibujo que muestra una idea del texto", "Es una forma de responder a la lectura."),
        ("¿Cómo se dice «cometa» en inglés?", "kite", "Es la palabra inglesa para cometa."),
        ("¿Qué significa «I like...»?", "Me gusta...", "Se usa para decir una preferencia."),
    ],
    [
        ("Texto: «Tom has a red kite.» ¿De qué color debe ser la cometa en el dibujo?", "Roja", "Red significa rojo."),
        ("Texto: «The kite is in the tree.» ¿Dónde se dibuja la cometa? (in the tree es en el árbol)", "En el árbol", "El texto dice dónde está la cometa."),
        ("¿Qué subrayas antes de dibujar?", "Personajes, colores y lugar del texto", "Esas son las pruebas que muestra el dibujo."),
    ],
    [
        ("Texto: «Ana has a green bag.» Elige la ilustración que coincide: (a) una niña con una mochila verde (b) una niña con un sombrero verde", "a", "Bag es mochila o bolso, y es verde."),
        ("Texto: «The cat is on the chair.» Elige la ilustración que coincide: (a) un gato sobre una silla (b) un gato bajo una silla", "a", "On significa sobre."),
        ("Texto: «Two birds are in the tree.» (two es dos; birds son pájaros). ¿Cuántos pájaros se dibujan?", "2", "Two es dos."),
    ],
    [
        ("Texto: «Leo has a blue ball.» El dibujo de Pedro muestra un niño con una pelota roja. ¿Qué parte cambia Pedro y qué debe corregir?", "El color; debe pintar la pelota azul", "El texto dice blue."),
        ("Texto: «The dog is under the table.» Sofía dibuja el perro sobre la mesa. ¿Qué palabra del texto no usó bien?", "under", "Under significa debajo de."),
    ],
    [
        ("Texto: «Mia has a small cat. The cat is black. It is on the chair.» (small es pequeño). En la ilustración, ¿de qué color es el gato y dónde está? Responde en español, separado por una coma.", "Negro, sobre la silla", "Black es negro y on the chair es sobre la silla."),
        ("Texto: «The red kite is in the tree.» Un niño agrega un sol grande. ¿La ilustración sigue siendo fiel al texto si la cometa está en el árbol? Responde sí o no.", "Sí", "El sol agrega un detalle sin cambiar el texto."),
    ],
    [("Tu profesora lee: «The yellow bird is on the green tree.» Elige la ilustración correcta: (a) un pájaro amarillo sobre un árbol verde (b) un pájaro verde sobre un árbol amarillo", "a", "Yellow bird es pájaro amarillo y green tree es árbol verde.")],
    [
        ("¿Cómo se dice «árbol» en inglés?", "tree", "Es la palabra inglesa para árbol."),
        ("¿Qué significa «favorite»?", "Favorito", "Es lo que más me gusta."),
        ("¿Por qué una ilustración debe tener pruebas del texto?", "Para mostrar que entendí lo que decía", "Las pruebas hacen fiel el dibujo."),
    ],
    task("Lee este texto: «Sam has a green frog. The frog is on a big leaf. The leaf is in the water.» (frog es rana; leaf es hoja; water es agua). Subraya las palabras que vas a dibujar y haz una ilustración. Escribe debajo una frase: «I like the ___» (por ejemplo frog).", "Dibujo a Sam, una rana verde sobre una hoja grande en el agua. Escribo: «I like the frog».", ["subraya pruebas del texto", "dibuja los tres lugares y objetos del texto", "no cambia lo que el texto dice", "escribe «I like the ___»"], ["el dibujo con la frase", "nota de la persona que escuchó"], ["dibujar la rana fuera del agua", "olvidar el color verde"], "Pide que señale en el dibujo cada prueba subrayada y celebra los detalles fieles."),
    "Dibuja la oración «The cat is on the chair» y escribe su título en inglés.",
    "Cambia el color de un objeto en el texto de la tarea y escribe la oración nueva en inglés; dibuja la versión nueva.",
)

lesson(
    OA9, 2,
    "Los textos escritos en cada ejercicio y, si quieres, plasticina, papel, tijeras de punta redonda y objetos de la casa que no se rompan. Hazlo con una persona de tu casa.",
    "Aprenderé a construir una figura o una escena para mostrar lo que entendí de un texto. Sirve para representar lugares y objetos con las palabras on, in y under.",
    ["Sé hacer una ilustración fiel al texto.", "Sé algunos objetos de la casa en inglés."],
    [
        "Otra forma de responder a un texto es armar una figura (figure) o una escena (scene) con objetos de casa, papel o plasticina. Una escena muestra varios objetos juntos, como una pequeña maqueta. No necesitas materiales especiales: sirve una caja, una taza de plástico, una pelota o un muñeco.",
        "Las palabras de lugar son la clave: «on» significa sobre, «in» significa dentro de y «under» significa debajo de. En «The ball is on the box» la pelota está sobre la caja. En «The ball is in the box» está dentro. En «The ball is under the box» está debajo. Armar la escena te ayuda a recordar estas palabras.",
        "Para armar una buena escena, lee la oración, subraya los objetos y la palabra de lugar, y ubica los objetos uno por uno. Al terminar, vuelve al texto y comprueba: ¿mi escena dice lo mismo que el texto? Si no, cámbiala. Siempre usa objetos seguros, sin vidrios ni filos.",
    ],
    [("scene", "escena"), ("figure", "figura"), ("on", "sobre"), ("in", "dentro de"), ("under", "debajo de"), ("box", "caja")],
    [
        ("Armar una escena", "Texto: «The ball is on the box.» ¿Cómo armas la escena?", ["Busco una pelota y una caja.", "La palabra de lugar es on.", "Pongo la pelota encima de la caja."], "La pelota está sobre la caja."),
        ("Cambiar la escena", "La escena muestra una pelota sobre una caja. Ahora el texto dice: «The ball is under the box.» ¿Qué cambias?", ["Leo la palabra nueva: under.", "Under es debajo de.", "Muevo la pelota debajo de la caja."], "Pongo la pelota debajo de la caja."),
    ],
    [
        ("Poner el objeto en cualquier lugar sin leer la palabra de lugar.", "No se revisa on, in o under.", "Subraya la palabra de lugar antes de armar."),
        ("Confundir in con on.", "Se piensa que significan lo mismo.", "In es dentro; on es encima."),
    ],
    [
        ("¿Qué significa «under»?", "Debajo de", "Indica abajo de algo."),
        ("¿Qué significa «on»?", "Sobre, encima de", "Indica encima de algo."),
        ("¿Qué es una «scene»?", "Una escena, objetos armados juntos", "Es una representación del texto."),
    ],
    [
        ("Texto: «The cat is in the box.» ¿Dónde está el gato en la escena? (a) dentro de la caja (b) sobre la caja", "a", "In significa dentro de."),
        ("Texto: «The book is on the table.» (book es libro; table es mesa). ¿Dónde pones el libro?", "Sobre la mesa", "On significa sobre."),
        ("¿Qué haces al terminar de armar tu escena?", "La comparo con el texto", "Así compruebo que sea fiel."),
    ],
    [
        ("Completa: «The pencil is ___ the box.» (dentro de la caja). Escribe una palabra en inglés.", "in", "In significa dentro de."),
        ("Completa: «The ball is ___ the chair.» (debajo de la silla). Escribe una palabra en inglés.", "under", "Under significa debajo de."),
        ("Completa: «The toy is ___ the table.» (sobre la mesa). Escribe una palabra en inglés.", "on", "On significa sobre."),
    ],
    [
        ("Texto: «The ball is on the box. The cup is under the box.» (cup es taza). Describe en español dónde queda cada objeto, separados por punto y coma.", "La pelota queda sobre la caja; la taza queda debajo de la caja", "Se leen las dos palabras de lugar."),
        ("Una niña puso un muñeco dentro de una caja, pero el texto decía «The doll is on the box.» (doll es muñeca). ¿Qué corrige?", "Pone la muñeca sobre la caja", "On significa sobre."),
    ],
    [
        ("Texto: «The red ball is in the box. The blue ball is on the box.» ¿De qué color es la pelota que queda dentro?", "Roja", "Red ball is in the box."),
        ("Texto: «The cat is under the chair. The dog is on the chair.» ¿Qué animal queda debajo de la silla? Escribe la palabra en inglés.", "cat", "El gato está bajo la silla."),
    ],
    [("Un compañero arma esta escena: un lápiz sobre un cuaderno. El texto dice «The pencil is in the notebook.» (notebook es cuaderno). ¿Qué palabra de lugar debe mostrar su escena?", "in", "El texto dice in, que es dentro de.")],
    [
        ("¿Cómo se dice «caja» en inglés?", "box", "Es la palabra inglesa para caja."),
        ("¿Qué significa «The ball is in the box»?", "La pelota está dentro de la caja", "In significa dentro de."),
        ("¿Qué materiales sirven para armar una escena?", "Objetos de casa, papel o plasticina seguros", "No hace falta nada especial."),
    ],
    task("Con objetos seguros de casa (una caja, una taza de plástico o papel, una pelota o un papel arrugado) arma la escena del texto: «The ball is in the box. The cup is on the box. The pencil is under the table.» (pencil es lápiz; table es mesa). Para cada oración di en voz alta la frase en inglés mientras muestras la escena. Una persona de tu casa te mira y marca si la escena coincide con cada oración.", "Pongo la pelota dentro de la caja, la taza encima de la caja y el lápiz debajo de la mesa. Digo las tres frases.", ["arma las tres partes de la escena", "usa in, on y under bien", "dice las frases en inglés", "compara su escena con el texto"], ["foto o dibujo de la escena", "nota de la persona que la marcó"], ["confundir in con on", "no ubicar el lápiz"], "Si una parte no coincide, mueve el objeto con él o ella y repite la palabra de lugar."),
    "Ordena tu pieza o tu escritorio como una escena y describe un objeto con la palabra on.",
    "Escribe tres oraciones en inglés con on, in y under sobre tres objetos de tu casa.",
)

lesson(
    OA9, 3,
    "El texto del mini diálogo escrito en esta clase, espacio libre para actuar con cuidado y una persona de tu casa que lea con tu apoyo.",
    "Aprenderé a dramatizar un diálogo corto con voz, gestos y cara, y a justificar mis gestos con una frase del texto. Sirve para mostrar lo que entendí y lo que sentí al leer.",
    ["Sé decir hello y thank you.", "Sé leer un diálogo con dos personajes."],
    [
        "Una dramatización (dramatization) es actuar un texto. Cada personaje dice sus palabras y usa gestos y la cara para mostrar lo que siente. En un diálogo, el nombre del personaje está antes de los dos puntos: «Mia: Hello!» significa que Mia dice «Hello!».",
        "Los gestos deben tener una prueba en el texto. Si el texto dice «Oh no! My pencil!» (¡Oh, no! ¡Mi lápiz!), puedes hacer cara de preocupación porque la frase muestra que algo pasó. Si dice «Here you are» (aquí tienes), puedes extender la mano para entregar algo. Si dice «Thank you» (gracias), sonríes.",
        "Para dramatizar bien: lee el diálogo una vez, subraya la frase que justifica cada gesto, practica con tu pareja y actúa con voz clara. No necesitas actuar perfecto ni imitar un acento. Cuida el espacio: no corras ni empujes, y avisa antes de tocar el objeto de otra persona.",
    ],
    [("dramatization", "dramatización, actuar un texto"), ("gesture", "gesto"), ("Here you are", "aquí tienes"), ("Thank you", "gracias"), ("Oh no!", "¡oh, no!"), ("pencil", "lápiz")],
    [
        ("Justificar un gesto", "Mia dice: «Oh no! My pencil!». ¿Qué cara haces y qué frase la justifica?", ["Leo la frase de Mia.", "Oh no muestra una preocupación.", "Hago cara de preocupación."], "Cara de preocupación, justificada por «Oh no! My pencil!»."),
        ("Elegir el gesto", "Leo dice: «Here you are.» ¿Qué gesto haces?", ["Here you are es aquí tienes.", "Se dice al entregar algo.", "Extiendo la mano con el lápiz."], "Extiendo la mano para entregar el lápiz."),
    ],
    [
        ("Actuar sin leer qué dice el texto.", "Se inventan gestos que no tienen relación.", "Subraya la frase que justifica cada gesto."),
        ("Pensar que hay que actuar con acento perfecto.", "Se confunde actuar con imitar.", "Importa que se entienda y que el gesto tenga prueba en el texto."),
    ],
    [
        ("¿Qué significa «Thank you»?", "Gracias", "Se dice al recibir algo."),
        ("¿Qué significa «Here you are»?", "Aquí tienes", "Se dice al entregar algo."),
        ("¿Quién dice «Hello!» en «Mia: Hello!»?", "Mia", "El nombre antes de los dos puntos dice la frase."),
    ],
    [
        ("Mia dice «Thank you». ¿Qué cara haces? (a) sonrío (b) lloro", "a", "Thank you es una frase de agradecimiento."),
        ("¿Qué gesto va con «Here you are»?", "Entregar un objeto con la mano", "Esa frase se dice al dar algo."),
        ("¿Por qué se subraya la frase que justifica el gesto?", "Para tener una prueba en el texto", "El gesto debe salir de lo que el texto dice."),
    ],
    [
        ("Completa: «Mia: Oh no! My ___!» (lápiz)", "pencil", "Pencil es lápiz."),
        ("Completa: «Leo: Here you ___.»", "are", "La frase completa es Here you are."),
        ("Completa: «Mia: Thank ___!»", "you", "La frase completa es Thank you."),
    ],
    [
        ("Un niño actúa «Mia: Thank you!» con cara de enojo. ¿Qué corriges y por qué?", "Debe sonreír, porque thank you es agradecer", "El gesto debe coincidir con la frase."),
        ("Leo dice «Here you are» y se queda con el lápiz. ¿Qué gesto falta?", "Entregar el lápiz", "Here you are significa aquí tienes."),
    ],
    [
        ("Diálogo: «Mia: Oh no! My pencil! Leo: Here you are. Mia: Thank you!» Las tres acciones son preocupación, sonrisa y entrega. Escríbelas en el orden en que ocurren en el diálogo.", "preocupación, entrega, sonrisa", "Primero Mia se preocupa, luego Leo entrega y por último Mia agradece."),
        ("¿Quién entrega el lápiz en el diálogo anterior? Escribe el nombre.", "Leo", "Leo dice Here you are."),
    ],
    [("En el recreo, un compañero te presta un lápiz. Eliges decir en inglés para dramatizar el diálogo: (a) «Thank you!» (b) «Oh no!»", "a", "Thank you es la frase de agradecimiento.")],
    [
        ("¿Cómo se dice «gracias» en inglés?", "Thank you", "Es la frase para agradecer."),
        ("¿Qué muestra una dramatización?", "Lo que entendí y sentí con voz y gestos", "Es una forma de responder a lo leído."),
        ("¿Es necesario imitar un acento para dramatizar bien?", "No", "Lo importante es que se entienda."),
    ],
    task("Con una persona de tu casa, lean y actúen este diálogo: «Mia: Oh no! My pencil! Leo: Here you are. Mia: Thank you!» Subrayen la frase que justifica cada gesto. Cada uno dice sus frases con voz clara y gestos, sin correr ni empujar. Después cambien de personaje y repitan.", "Mia hace cara de preocupación al decir «Oh no!», Leo entrega el lápiz con «Here you are», Mia sonríe con «Thank you!».", ["dice las tres frases", "hace un gesto que coincide con cada frase", "subraya la frase que justifica cada gesto", "cambia de personaje"], ["nota de la persona que actuó con él o ella"], ["actuar un gesto que contradice la frase", "no cambiar de personaje"], "Valora los gestos que se entienden y repite la frase que le costó."),
    "Actúa el diálogo frente a un espejo y mira si tu cara coincide con la frase.",
    "Escribe en español qué gesto haces para cada frase del diálogo y qué palabra de la frase te lo dice.",
)

lesson(
    OA9, 4,
    "El texto breve de esta clase, lápiz y una persona de tu casa para leer en voz alta.",
    "Aprenderé a reaccionar a un texto escribiendo una palabra o una frase corta, como «funny» o «I like the hat». Sirve para decir qué sentí y qué me gustó.",
    ["Sé leer oraciones breves.", "Sé decir happy y sad."],
    [
        "Después de leer, puedes responder con palabras o con frases escritas. Una palabra (word) puede decir cómo te sentiste: happy (contento), sad (triste), funny (divertido). Una frase (phrase) o una oración (sentence) puede decir más: «I like the hat» (me gusta el sombrero).",
        "Para escribir tu reacción, usa tres pasos. Primero lee el texto. Luego elige una palabra de sentimiento: funny, happy o sad. Por último escribe una frase con «I like...» y la parte del texto que te gustó. Recuerda empezar con mayúscula y terminar con punto.",
        "Todas las respuestas son válidas si son honestas, pero necesitan relación con el texto. Si el texto cuenta algo gracioso, «funny» es una buena palabra. Si el texto cuenta algo triste, «sad» es mejor. Escribe una frase con una parte del texto, no con algo que no se leyó.",
    ],
    [("word", "palabra"), ("phrase", "frase corta"), ("sentence", "oración"), ("funny", "divertido, gracioso"), ("I like...", "me gusta..."), ("hat", "sombrero")],
    [
        ("Elegir una palabra", "Texto: «Pip is a little mouse. He has a big hat. Pip jumps. The hat jumps too.» (mouse es ratón; jumps es salta). ¿Qué palabra de sentimiento escribes si te hizo reír?", ["Leo el texto: el sombrero también salta.", "Me hizo reír.", "La palabra es funny."], "funny"),
        ("Escribir una frase", "Mismo texto. Quieres decir que te gustó el sombrero. ¿Qué frase escribes?", ["Uso I like.", "Escribo the hat, porque es lo que me gustó.", "Empiezo con mayúscula y termino con punto."], "I like the hat."),
    ],
    [
        ("Escribir una reacción que no tiene relación con el texto.", "Se escribe una opinión sin leer.", "Escribe una palabra o una frase que salga del texto."),
        ("Escribir la frase sin mayúscula ni punto.", "Se olvida cómo se escribe una oración.", "Empieza con mayúscula y termina con punto."),
    ],
    [
        ("¿Qué significa «funny»?", "Divertido, gracioso", "Se dice de algo que da risa."),
        ("¿Cómo se dice «me gusta» en inglés?", "I like", "Se usa para decir una preferencia."),
        ("¿Qué es una «word»?", "Una palabra", "Word es palabra."),
    ],
    [
        ("Texto: «The cat is sad. It has no toy.» (toy es juguete). ¿Qué palabra de sentimiento va mejor, sad o funny?", "sad", "El texto dice que el gato está triste."),
        ("¿Con qué letra empieza una oración en inglés?", "Con mayúscula", "Las oraciones empiezan con mayúscula."),
        ("¿Con qué signo termina una oración como «I like the hat»?", "Con punto", "El punto cierra la oración."),
    ],
    [
        ("Completa: «I ___ the hat.» (me gusta)", "like", "Like es gustar."),
        ("Completa con una palabra de sentimiento: «The story is ___.» (divertido)", "funny", "Funny significa divertido."),
        ("Escribe una frase de cuatro palabras con I like, the y la palabra mouse (ratón).", "I like the mouse", "Se usa I like y la parte que gustó."),
    ],
    [
        ("Ana escribe: «i like the hat» sin mayúscula ni punto. ¿Qué dos cosas corriges?", "La mayúscula de I y el punto final", "I se escribe siempre con mayúscula y la oración termina con punto."),
        ("Leo escribió «The story is sad», pero el sombrero que salta le dio risa. ¿Qué palabra debe usar en lugar de sad?", "funny", "Funny dice que algo dio risa."),
    ],
    [
        ("Texto: «Pip is a little mouse. Pip jumps. The hat jumps too.» Escribe una frase con I like que hable de Pip. Debe tener tres palabras.", "I like Pip", "Se escribe I like y el nombre del personaje."),
        ("Texto del ejercicio anterior. Escribe una palabra de sentimiento en inglés que mejor represente lo gracioso de un sombrero que salta.", "funny", "Funny significa gracioso."),
    ],
    [("Terminas de leer en clase y la profesora pide una palabra para tu sentimiento. El texto contaba cómo un gato amarillo juega con una pelota y se divierte. Elige: (a) funny (b) sad", "a", "Funny va con una escena divertida.")],
    [
        ("¿Cómo se dice «oración» en inglés?", "sentence", "Una sentence tiene mayúscula y punto."),
        ("¿Para qué sirve una palabra de sentimiento al responder a un texto?", "Para decir cómo me sentí al leer", "Muestra mi reacción."),
        ("¿Qué letra siempre se escribe con mayúscula cuando se refiere a mí en inglés?", "I", "La palabra I (yo) siempre va con mayúscula."),
    ],
    task("Lee con una persona de tu casa: «Pip is a little mouse. He has a big hat. Pip jumps. The hat jumps too.» Responde con una palabra de sentimiento (funny, happy o sad) y escribe dos frases cortas: «I like the ___.» y «The story is ___.» Revisa que cada frase empiece con mayúscula y termine con punto.", "funny. I like the hat. The story is funny.", ["lee el texto", "elige una palabra de sentimiento con relación al texto", "escribe dos frases con I like y The story is", "usa mayúscula y punto"], ["las frases escritas", "nota de la persona que leyó con él o ella"], ["escribir sin mayúscula ni punto", "usar sad en un texto gracioso"], "Lee las frases en voz alta con él o ella y celebra la parte del texto que eligió."),
    "Escribe en español qué palabra de sentimiento te dio un cuento que conozcas y por qué.",
    "Escribe tres palabras de sentimiento en inglés y dibuja una cara para cada una.",
)

lesson(
    OA9, 5,
    "El texto breve y las frases escritas en esta clase, lápiz y una persona de tu casa para escuchar tu opinión.",
    "Aprenderé a dar una opinión sobre un texto y a apoyarla con una frase del texto. Sirve para explicar por qué me gustó o no me gustó una lectura.",
    ["Sé escribir I like y The story is funny.", "Sé que because significa porque."],
    [
        "Una opinión (opinion) es lo que piensas sobre un texto. En inglés se dice: «I like the story» (me gusta el cuento) o «I don't like the story» (no me gusta el cuento). «Don't» es una forma corta de «do not» y significa «no». Las dos opiniones son válidas.",
        "Para apoyar tu opinión, usa «because» (porque) y una razón que salga del texto. «I like the story because it is funny» (me gusta el cuento porque es divertido). La razón puede ser una palabra, como funny o sad, o una parte del texto, como «The hat jumps too» (el sombrero también salta).",
        "Una buena opinión tiene tres partes: lo que opinas, la palabra because y la razón. Una razón sin prueba, como «porque sí», no ayuda. Cuando des tu razón, busca la parte del texto y señálala. Escucha con respeto la opinión de otras personas, aunque piensen distinto. También puedes conectar el texto con tu vida: «I have a hat too» significa «yo también tengo un sombrero» (have es tener; too es también).",
    ],
    [("opinion", "opinión"), ("I like...", "me gusta..."), ("I don't like...", "no me gusta..."), ("because", "porque"), ("funny", "divertido"), ("story", "cuento, historia")],
    [
        ("Dar una opinión con razón", "Texto: «Pip is a little mouse. He has a big hat. The hat jumps too.» Te gustó porque es divertido. ¿Qué escribes?", ["Digo mi opinión: I like the story.", "Agrego because.", "La razón es funny."], "I like the story because it is funny."),
        ("Opinión negativa con respeto", "Texto: «The cat is sad. It has no toy.» No te gustó porque es triste. ¿Qué escribes?", ["Digo I don't like the story.", "Agrego because.", "La razón es sad."], "I don't like the story because it is sad."),
    ],
    [
        ("Dar una razón que no sale del texto.", "Se escribe una razón sin relación con lo leído.", "Elige una razón que se pueda mostrar en el texto."),
        ("Olvidar because.", "No se une la opinión con la razón.", "Escribe la opinión, because y la razón."),
    ],
    [
        ("¿Qué significa «I don't like the story»?", "No me gusta el cuento", "Don't significa no."),
        ("¿Qué significa «opinion»?", "Opinión", "Es lo que pienso sobre el texto."),
        ("¿Qué palabra une la opinión con la razón?", "because", "Because significa porque."),
    ],
    [
        ("¿Cuáles son las tres partes de una buena opinión?", "Lo que opino, because y la razón", "Así la opinión queda apoyada."),
        ("¿De dónde debe salir la razón de una opinión?", "Del texto", "El texto es la prueba."),
        ("Si una persona opina distinto a ti, ¿qué haces?", "La escucho con respeto", "Las opiniones pueden ser distintas."),
    ],
    [
        ("Completa: «I like the story ___ it is funny.» (porque)", "because", "Because es porque."),
        ("Completa con la forma corta de do not: «I ___ like the story because it is sad.»", "don't", "Don't significa no y va antes de like."),
        ("Texto: «The hat jumps too.» Completa: «The story is ___ because the hat jumps.» (divertido)", "funny", "Un sombrero que salta es gracioso."),
    ],
    [
        ("Pedro escribe: «I like the story because I like pizza.» ¿Es buena su razón con el texto del sombrero que salta? Responde sí o no.", "No", "La razón no sale del texto."),
        ("Marta escribe: «I like the story. funny» ¿Qué le falta a su opinión?", "because y una oración completa", "Debe unir la opinión con la razón: because it is funny."),
    ],
    [
        ("Ordena las palabras para formar una opinión: funny / because / like / I / the story / it / is. Escribe la oración completa.", "I like the story because it is funny", "Se unen opinión, because y razón."),
        ("Elige la mejor razón para «I like the story because...»: (a) «the hat jumps» (b) «my shoes are blue».", "a", "La razón sale del texto."),
    ],
    [("Después de escuchar el cuento del sombrero que salta, tu profesora pregunta «Do you like the story?» (¿te gusta el cuento?). Tú dices que no. Escribe tu respuesta en inglés con cinco palabras (no me gusta el cuento).", "I don't like the story", "Don't significa no y story es cuento.")],
    [
        ("¿Cómo se dice «porque» en inglés?", "because", "Une la opinión con la razón."),
        ("¿Qué significa «I have a hat too»?", "Yo también tengo un sombrero", "Have es tener y too es también: conecta el texto con mi vida."),
        ("¿Qué significa «story»?", "Cuento, historia", "Es el texto que se lee."),
    ],
    task("Lee: «Pip is a little mouse. He has a big hat. Pip jumps. The hat jumps too.» Escribe tu opinión con una de estas dos oraciones y completa la razón: «I like the story because it is ___.» o «I don't like the story because it is ___.» (Palabras posibles: funny, sad.) Muéstrala a una persona de tu casa, léela en voz alta y señala la parte del texto que apoya tu razón.", "I like the story because it is funny. Señalo «The hat jumps too».", ["escribe su opinión", "usa because", "da una razón que sale del texto", "señala la parte del texto"], ["la oración escrita", "nota de la persona que escuchó"], ["razón sin relación con el texto", "olvidar because"], "Valora la razón y pregunta qué parte del texto la apoya, sin imponer una opinión."),
    "Pregunta a una persona de tu casa si le gusta un cuento que conozca y por qué, y escucha su opinión.",
    "Escribe en español una opinión sobre un libro de tu casa con dos razones del libro.",
)
