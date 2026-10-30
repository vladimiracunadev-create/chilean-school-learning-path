"""Student material for 2.º básico Inglés, EN02 OA 08 (estrategias de lectura) y OA 09 (reaccionar a lo leído).

Los textos en inglés son originales, muy breves, con pista en español. Las imágenes se describen entre
corchetes porque el cuaderno no incluye ilustraciones. Todo texto se puede leer en voz alta con un adulto.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA8, OA9 = "EN02 OA 08", "EN02 OA 09"


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
    "Los textos y las descripciones de imágenes escritos en cada ejercicio, lápiz y una hoja para tapar el texto mientras predices.",
    "Aprenderé a predecir de qué trata un texto en inglés mirando el título y la imagen, y a cambiar mi predicción si el texto dice otra cosa. Sirve para empezar a leer con una idea y entender mejor.",
    ["Sé leer palabras cortas en inglés como cat, dog y red.", "Sé que un título es el nombre de un texto."],
    [
        "Predecir (predict) es decir qué creo que va a pasar o de qué creo que trata un texto, antes de leerlo. Para predecir miro el título (title) y la imagen (picture). Puedo decir: «I think the story is about a frog», que significa «creo que el cuento trata de una rana».",
        "Una predicción es una buena idea, pero todavía no es un hecho. Cuando leo, comparo mi idea con lo que dice el texto. Si coincide, sigo leyendo. Si el texto dice otra cosa, cambio mi predicción: la reviso (revise) y digo lo nuevo.",
        "Cambiar una predicción no es un error. Los buenos lectores lo hacen todo el tiempo. Para decirlo en inglés puedes usar «I think... because...», que significa «creo que... porque...». El texto siempre manda: él es la prueba.",
    ],
    [("predict", "predecir, decir lo que creo que pasará"), ("title", "título"), ("picture", "imagen"), ("I think", "yo creo"), ("because", "porque"), ("revise", "cambiar o corregir una idea")],
    [
        ("Predecir con título e imagen", "Título: «The Little Frog». Imagen: [una rana verde sobre una hoja, cerca del agua]. ¿De qué crees que trata el cuento?", ["Leo el título: The Little Frog, la pequeña rana.", "Miro la imagen: hay una rana sobre una hoja.", "Ambas pistas hablan de una rana."], "I think the story is about a frog."),
        ("Revisar la predicción", "Predije: «The frog is sad». El texto dice: «The frog is happy. It jumps and sings.» ¿Qué debo hacer con mi predicción?", ["Comparo: yo dije sad (triste).", "El texto dice happy (contenta).", "No coinciden, así que cambio mi idea."], "Debo cambiarla: the frog is happy."),
    ],
    [
        ("Dejar la predicción aunque el texto diga otra cosa.", "Se cree que la primera idea nunca se puede cambiar.", "Compara con el texto y revisa tu predicción."),
        ("Predecir sin mirar el título ni la imagen.", "Se adivina sin pistas.", "Mira primero el título y la imagen: son tus pistas."),
    ],
    [
        ("Título: «My Dog Max». Imagen: [un perro con una pelota]. ¿De qué trata? (a) de un perro (b) de una pizza", "a, de un perro", "El título y la imagen hablan de un perro."),
        ("¿Qué significa «title»?", "Título", "Es el nombre del texto, que se lee antes de comenzar."),
        ("¿Qué significa «I think»?", "Yo creo", "Se usa para decir una idea o predicción."),
    ],
    [
        ("¿Qué es predecir antes de leer?", "Decir qué creo que pasará o de qué trata, usando pistas", "La predicción usa el título y la imagen."),
        ("¿Qué dos pistas miras antes de leer para predecir?", "El título y la imagen", "Son lo primero que se ve de un texto."),
        ("¿Por qué debes cambiar tu predicción si el texto dice algo distinto?", "Porque el texto es la prueba de lo que pasa", "Lo escrito corrige mi idea inicial."),
    ],
    [
        ("Título: «The Blue Bird». Imagen: [un pájaro azul en un árbol]. Completa en inglés: «I think the story is about a ___.»", "bird", "El título y la imagen muestran un pájaro, bird."),
        ("Mi predicción: «The girl is sad». El texto: «Ana is happy. She has a new red bike.» ¿Se mantiene o se cambia?", "Se cambia, porque Ana está feliz", "Happy significa contenta, no triste."),
        ("Título: «Lunch Time». Imagen: [un sándwich, una manzana y leche]. ¿De qué crees que trata? (a) de comida (b) de un viaje", "a, de comida", "Lunch es almuerzo y la imagen muestra comida."),
    ],
    [
        ("Predije «the story is about a cat». El texto dice: «Look at the dog! The dog is big.» Escribe en inglés la palabra que debo cambiar en mi predicción, la nueva.", "dog", "El texto habla de un perro, dog."),
        ("Tomás dice: «Mi predicción no puede cambiar nunca». ¿Tiene razón?", "No; se puede cambiar cuando el texto dice otra cosa", "Revisar la predicción es parte de leer bien."),
    ],
    [
        ("Título: «The Rainy Day». Imagen: [un niño con paraguas amarillo]. Elige la mejor predicción: (a) «I think it is sunny.» (b) «I think it is rainy.»", "b", "Rainy significa lluvioso, como indica el título."),
        ("Texto: «Leo has a ball. The ball is in the tree. Leo is sad.» Mi predicción era «Leo is happy». Escribe la predicción revisada, de tres palabras, en inglés.", "Leo is sad", "El texto dice que Leo está triste."),
    ],
    [("La profesora muestra la portada de «The Big Red Bus» con [un bus rojo con niños]. ¿Qué predicción es mejor? (a) «I think the story is about a bus.» (b) «I think the story is about a cake.»", "a", "La portada muestra un bus; bus es autobús.")],
    [
        ("¿Cómo se dice «imagen» en inglés?", "picture", "Es la palabra para una imagen o dibujo."),
        ("Mi predicción no coincide con el texto. ¿Qué hago?", "La reviso y digo la idea nueva", "El texto manda y corrige la predicción."),
        ("¿Qué quiere decir «because»?", "Porque", "Se usa para dar la razón de una idea."),
    ],
    task("Estas son tres portadas: (1) «My Green Frog», imagen: [una rana en una hoja]; (2) «The Birthday Cake», imagen: [una torta con velas]; (3) «The Funny Dog», imagen: [un perro con un sombrero]. Para cada una di en voz alta «I think the story is about a ___ because the picture shows a ___» con ayuda del adulto. Luego el adulto lee «The frog is on a log» y tú dices si cambias o no la primera predicción.", "«I think the story is about a frog because the picture shows a frog.»", ["usa el título o la imagen como pista", "dice «I think...» en las tres portadas", "da una razón con «because»", "dice si mantiene o cambia la predicción"], ["nota del adulto que escuchó las tres frases"], ["predecir sin dar una razón", "no mirar la imagen"], "Reconoce cada predicción con una razón y repite despacio con él la frase que le costó."),
    "Mira la portada de un libro que tengas en casa y di en español de qué crees que trata y por qué.",
    "Inventa un título corto en inglés, por ejemplo «The Happy Dog», y dibuja la imagen que lo acompaña. Dile a alguien qué predicen tu título y tu dibujo.",
)

lesson(
    OA8, 2,
    "Los textos escritos en cada ejercicio, lápiz y hoja para tapar las palabras. Un adulto puede leer en voz alta.",
    "Aprenderé a usar lo que ya sé y las palabras que ya conozco para entender un texto corto en inglés. Sirve para entender aunque no conozca todas las palabras.",
    ["Sé algunas palabras en inglés: cat, dog, red, blue, mom.", "Sé que hay palabras en inglés parecidas al español."],
    [
        "Cuando lees, no empiezas de cero. Ya sabes cosas (conocimientos previos o prior knowledge). Si un texto habla de una escuela, ya sabes que hay profesores y niños. Usar lo que sabes ayuda a entender lo que no conoces.",
        "Algunas palabras en inglés se parecen al español y se escriben casi igual: family (familia), animal (animal), chocolate (chocolate), music (música), color (color), park (parque). Son pistas muy buenas. Pero ten cuidado: hay palabras que parecen iguales y no lo son, y por eso debes revisar con el resto de la oración.",
        "Para leer mejor: busca primero las palabras que conoces, piensa qué sabes del tema y une todo con una idea. Si una palabra nueva aparece, usa las otras palabras de la oración como ayuda. Por ejemplo, en «The doctor is in the hospital», si conoces doctor y hospital, entiendes que el médico está en un lugar de salud.",
    ],
    [("prior knowledge", "lo que ya sé"), ("known word", "palabra que ya conozco"), ("family", "familia"), ("park", "parque"), ("music", "música"), ("doctor", "médico o médica")],
    [
        ("Usar palabras conocidas", "Lee: «The family is in the park. Dad has a banana.» ¿Qué palabras conoces porque se parecen al español?", ["Busco palabras parecidas.", "Family se parece a familia.", "Park se parece a parque, banana a banana."], "family, park y banana"),
        ("Usar lo que ya sé", "Lee: «The doctor is in the hospital.» ¿Dónde crees que está el doctor?", ["Conozco doctor y hospital.", "Sé que un médico trabaja en un hospital.", "Junto las dos ideas."], "El doctor está en el hospital"),
    ],
    [
        ("Pensar que una palabra parecida siempre significa lo mismo.", "Se confía solo en el parecido.", "Revisa la palabra con el resto de la oración."),
        ("Detenerse en la primera palabra que no conozco.", "Se cree que hay que entender todo.", "Sigue leyendo y usa las palabras conocidas como ayuda."),
    ],
    [
        ("¿Qué palabra en inglés se parece a «música»?", "music", "Se escribe casi igual y suena parecida."),
        ("¿Cómo se dice «familia» en inglés?", "family", "Se parece mucho al español."),
        ("¿Qué significa «prior knowledge»?", "Lo que ya sé", "Prior es antes y knowledge es conocimiento."),
    ],
    [
        ("¿Para qué sirve pensar lo que ya sé antes de leer?", "Para entender mejor y adivinar palabras nuevas", "Mis ideas previas se conectan con el texto."),
        ("¿Qué haces si hay una palabra que no conoces en una oración?", "Sigo leyendo y uso las palabras que sí conozco", "El resto de la oración da pistas."),
        ("¿Por qué hay que revisar una palabra parecida al español?", "Porque a veces no significa lo mismo", "Revisar con la oración evita errores."),
    ],
    [
        ("Texto: «Mom has chocolate and a banana.» ¿Qué palabras se parecen al español? Escribe las dos primeras que encuentres en el texto.", "chocolate, banana", "Se escriben casi igual que en español."),
        ("Texto: «The doctor is in the hospital.» Con lo que sé, ¿dónde está la persona que cuida a los enfermos? Responde en español.", "En el hospital", "Hospital es un lugar de salud."),
        ("Texto: «The cat drinks milk.» Con lo que sé de los gatos, ¿qué crees que significa «milk»? (a) leche (b) piedra", "a, leche", "Los gatos suelen tomar leche."),
    ],
    [
        ("Texto: «Anna likes music. She plays the piano.» ¿Qué crees que significa «plays the piano»? Responde en español, usando lo que sabes de la música.", "Toca el piano", "Music y piano son pistas conocidas."),
        ("Pedro dice que «park» no puede entenderse porque está en inglés. ¿Cómo lo ayudas?", "Park se parece a parque, una palabra que conoce", "Las palabras parecidas son una pista."),
    ],
    [
        ("Texto: «The animal is big and brown.» ¿Qué palabra del texto se parece a la palabra «animal» en español? Escríbela.", "animal", "Se escribe casi igual que en español."),
        ("Texto: «My family is in the kitchen.» Con lo que sabes de la cocina, ¿qué crees que hace la familia? (a) cocina o come (b) duerme en la cama", "a", "En la cocina se cocina o se come."),
    ],
    [("En una hoja dice: «Today is music class. We sing.» ¿Qué crees que hacen los niños? Responde en español.", "Cantan en la clase de música", "Music y sing son pistas conocidas.")],
    [
        ("¿Cómo se dice «parque» en inglés?", "park", "Se parece mucho a la palabra en español."),
        ("¿Qué haces primero para entender un texto nuevo?", "Busco las palabras que conozco", "Esas palabras dan una idea del tema."),
        ("¿Qué palabra en inglés es «color»?", "color", "Se escribe igual y significa lo mismo."),
    ],
    task("Lee con un adulto: «The family is in the park. Dad has a banana. Mom has chocolate. The dog is happy.» Subraya con lápiz las palabras que ya conocías y las que se parecen al español. Luego di en español de qué trata el texto en una frase.", "Subrayo family, park, banana, chocolate, dog. El texto trata de una familia en un parque.", ["subraya al menos cuatro palabras conocidas", "usa lo que sabe para entender", "dice en una frase de qué trata", "revisa con el texto si una palabra no coincide"], ["el texto subrayado", "nota del adulto"], ["subrayar solo una palabra", "decir una idea que el texto no dice"], "Celebra las palabras que reconoció y ayúdale a unirlas en una sola idea."),
    "Escribe en tu cuaderno cinco palabras en inglés que se parezcan al español y dibuja una al lado de cada una.",
    "Busca en casa tres objetos con una etiqueta en inglés y adivina qué dicen usando lo que ya sabes.",
)

lesson(
    OA8, 3,
    "Los textos y las descripciones de imágenes escritas en cada ejercicio; lápiz.",
    "Aprenderé a usar la imagen junto con el texto para entender. Sirve para confirmar que lo que leí es correcto y para entender palabras nuevas.",
    ["Sé predecir con el título y la imagen.", "Sé colores y animales básicos en inglés."],
    [
        "Las imágenes ayudan a entender el texto. Una imagen puede mostrar a los personajes, el lugar, lo que hacen y hasta lo que sienten. Se llama «picture clue» a una pista que da la imagen.",
        "Para usar las imágenes, haz tres pasos. Primero mira la imagen y di qué ves. Luego lee la oración. Por último compara: ¿la oración dice lo que muestra la imagen? Si coincide, entendiste. Si no coincide, vuelve a mirar y a leer.",
        "Una imagen también puede ayudar con una palabra nueva. Si el texto dice «The cat is on the mat» y la imagen muestra un gato sobre una alfombrita, puedes entender que mat es esa alfombra pequeña. Pero a veces la imagen no muestra todo. Por eso se usan las dos cosas: la imagen y el texto.",
    ],
    [("picture clue", "pista que da la imagen"), ("look", "mirar"), ("match", "coincidir, hacer pareja"), ("mat", "alfombrita"), ("on", "sobre, encima de"), ("hat", "sombrero o gorro")],
    [
        ("Imagen y oración", "Imagen: [una niña con un gorro azul y un paraguas amarillo]. Oración: «The girl has a blue hat.» ¿La oración coincide con la imagen?", ["Miro la imagen: gorro azul.", "Leo: blue hat.", "Coinciden."], "Sí, coincide"),
        ("Palabra nueva con la imagen", "Texto: «The cat is on the mat.» Imagen: [un gato sentado sobre una alfombrita]. ¿Qué crees que es «mat»?", ["Veo un gato sobre una alfombrita.", "El texto dice on the mat.", "Mat es lo que está debajo del gato."], "Una alfombrita"),
    ],
    [
        ("Leer sin mirar la imagen.", "Se pierde una pista importante.", "Mira la imagen antes de leer y compárala después."),
        ("Creer que la imagen dice todo el texto.", "Se olvida que el texto tiene más información.", "Usa la imagen y el texto juntos."),
    ],
    [
        ("¿Qué es un «picture clue»?", "Una pista que da la imagen", "Picture es imagen y clue es pista."),
        ("Imagen: [un perro café]. Oración: «The dog is brown.» ¿Coincide?", "Sí", "Brown es café y el perro es café."),
        ("¿Qué significa «look»?", "Mirar", "Es lo primero que se hace con una imagen."),
    ],
    [
        ("¿Cuáles son los tres pasos para usar la imagen con el texto?", "Miro la imagen, leo la oración y comparo", "Así compruebo si entendí."),
        ("¿Para qué sirve comparar la imagen con la oración?", "Para ver si entendí bien", "Si coinciden, la comprensión es correcta."),
        ("¿Por qué no basta solo la imagen para entender un texto?", "Porque el texto tiene más información", "La imagen no lo muestra todo."),
    ],
    [
        ("Imagen: [dos pelotas rojas]. Oración: «I have two red balls.» ¿Coincide con la imagen? Responde sí o no.", "Sí", "Two red balls son dos pelotas rojas."),
        ("Imagen: [un pájaro sobre una casa]. Oración: «The bird is in the house.» ¿Coincide? Responde sí o no.", "No", "La imagen muestra el pájaro sobre la casa, no dentro."),
        ("Imagen: [un niño con una manzana]. Escoge la oración que coincide: (a) «The boy has an apple.» (b) «The boy has a hat.»", "a", "Apple es manzana."),
    ],
    [
        ("Imagen: [una vaca blanca en el pasto]. Oración: «The cow is white.» Una niña dice que no coincide porque la vaca es negra. ¿Quién tiene razón según la imagen?", "La oración, porque la vaca es blanca", "La imagen muestra una vaca blanca."),
        ("Texto: «The kitten is under the table.» Imagen: [un gatito bajo una mesa]. Con la imagen, ¿qué crees que significa «under»?", "Debajo de", "El gatito está bajo la mesa."),
    ],
    [
        ("Imagen: [tres niños, uno con una pelota amarilla]. Escoge el texto que coincide: (a) «Three children play.» (b) «One child sleeps.»", "a", "Three children son tres niños y la imagen muestra niños jugando."),
        ("Imagen: [una niña que sonríe]. Oración incompleta: «The girl is ___.» Opciones: sad / happy. Escribe la palabra.", "happy", "Sonreír indica que está contenta."),
    ],
    [("Un libro dice «The duck is on the water» y tiene [un pato nadando en un lago]. Con la imagen, ¿qué significa «water»?", "Agua", "El pato nada en el agua.")],
    [
        ("¿Cómo se dice «imagen» en inglés?", "picture", "Es la palabra para imagen."),
        ("¿Qué hago si la oración y la imagen no coinciden?", "Vuelvo a mirar y a leer", "Reviso para entender mejor."),
        ("¿Qué significa «on»?", "Sobre o encima de", "Indica que algo está arriba de otra cosa."),
    ],
    task("Dibuja en una hoja un perro café sobre una alfombrita. Luego lee con un adulto estas dos oraciones: (1) «The dog is brown.» (2) «The dog is on the mat.» Señala en tu dibujo lo que dice cada oración. Después cambia el dibujo para que el perro esté bajo la mesa y lee «The dog is under the table.»", "Mi dibujo muestra un perro café sobre una alfombrita; señalo el perro y la alfombrita.", ["su dibujo coincide con las dos oraciones", "señala dónde dice cada cosa", "entiende on y under", "explica en español qué cambió"], ["el dibujo", "nota del adulto"], ["dibujar un perro de otro color", "poner el perro en un lugar equivocado"], "Valora cada detalle que coincide con el texto y pregúntale cómo lo supo."),
    "Mira una ilustración de un libro y di en español tres cosas que ves.",
    "Dibuja una escena y escribe una oración en inglés que la describa, por ejemplo «The cat is on the bed».",
)

lesson(
    OA8, 4,
    "Los textos escritos en cada ejercicio, lápiz y la ayuda de un adulto para leer en voz alta.",
    "Aprenderé a releer un texto con una pregunta en la cabeza y a leer en voz alta con ayuda. Sirve para encontrar respuestas y entender mejor.",
    ["Sé usar el título y la imagen para predecir.", "Sé que who es quién, what es qué y where es dónde."],
    [
        "Releer (reread) es leer otra vez. Muchas veces una segunda lectura ayuda a entender lo que no quedó claro. No es un castigo: los buenos lectores releen. Puedes releer una oración o todo el texto.",
        "Ayuda releer con una pregunta. Antes de leer de nuevo, elige una: Who is it? (¿quién es?), What does he or she have? (¿qué tiene?), Where is it? (¿dónde está?). Mientras relees, buscas la respuesta con tu dedo bajo las palabras. Cuando la encuentras, la dices en voz alta.",
        "También puedes leer en voz alta (read aloud), con un adulto o un amigo. Si lees en voz alta, oyes las palabras y notas mejor lo que dicen. Si una palabra es difícil, léela despacio, vuelve a la oración y piensa qué tiene sentido.",
    ],
    [("reread", "leer otra vez"), ("read aloud", "leer en voz alta"), ("who", "quién"), ("what", "qué"), ("where", "dónde"), ("answer", "respuesta")],
    [
        ("Releer para responder", "Texto: «Sam is at school. He has a red pencil and a green book.» Pregunta: What color is the pencil?", ["Releo buscando pencil.", "Leo: red pencil.", "Red es rojo."], "Red, rojo"),
        ("Preguntar dónde", "Texto: «Sam reads in the library.» Pregunta: Where does Sam read?", ["Releo buscando el lugar.", "Dice in the library.", "Library es biblioteca."], "En la biblioteca (in the library)"),
    ],
    [
        ("Contestar sin volver al texto.", "Se confía solo en la memoria.", "Relee con la pregunta y busca la respuesta con el dedo."),
        ("Leer todo muy rápido para terminar pronto.", "Se cree que leer rápido es leer bien.", "Lee despacio, en voz alta si puedes, y relee lo importante."),
    ],
    [
        ("¿Qué significa «reread»?", "Leer otra vez", "Re- indica repetir la lectura."),
        ("¿Qué significa «where»?", "Dónde", "Se usa para preguntar por un lugar."),
        ("¿Cómo se dice «leer en voz alta» en inglés?", "read aloud", "Es la expresión para leer en voz alta."),
    ],
    [
        ("¿Por qué ayuda releer con una pregunta en la cabeza?", "Porque busco una respuesta concreta", "La pregunta orienta la lectura."),
        ("¿Para qué sirve leer en voz alta?", "Para oír las palabras y entender mejor", "Oír ayuda a notar lo que dice el texto."),
        ("¿Qué haces cuando encuentras la respuesta?", "La digo en voz alta", "Así compruebo que la encontré."),
    ],
    [
        ("Texto: «Ana has a blue bag. In the bag she has an apple.» Pregunta: What does Ana have in the bag?", "An apple", "El texto dice an apple en la bolsa."),
        ("Texto: «Leo is in the garden. He has a yellow ball.» Pregunta: Where is Leo?", "In the garden", "Garden es jardín y es donde está Leo."),
        ("Texto: «The teacher is kind. She reads a story.» Pregunta: Who reads a story?", "The teacher", "Teacher es profesora y es quien lee."),
    ],
    [
        ("Texto: «Mia has two pets: a cat and a fish.» Después de releerlo, ¿cuántos animales tiene Mia?", "Dos", "Two pets son dos mascotas."),
        ("Ema leyó rápido «The bird is on the tree» y dijo que el pájaro estaba debajo. ¿Qué debe hacer para corregirlo?", "Releer la oración y fijarse en la palabra on", "On significa sobre, no debajo."),
    ],
    [
        ("Texto: «Tom has a red kite. The kite is in the sky. Tom is happy.» Reléelo y responde en inglés, con una palabra: ¿cómo se siente Tom?", "Happy", "El texto dice Tom is happy."),
        ("Texto: «Pablo has a cat. The cat is black. The cat sleeps on a chair.» Reléelo con la pregunta Where does the cat sleep? Responde en español.", "Sobre una silla", "On a chair significa sobre una silla."),
    ],
    [("Una profesora lee: «Lucy is in the kitchen. She has milk and a cookie.» Un niño pregunta qué tiene Lucy. ¿Qué responden releyendo? Responde en español.", "Leche y una galleta", "Milk es leche y cookie es galleta.")],
    [
        ("¿Qué significa «who»?", "Quién", "Se usa para preguntar por una persona o personaje."),
        ("¿Qué hago si no entiendo una oración?", "La releo despacio", "Una segunda lectura aclara la idea."),
        ("¿Para qué elijo una pregunta antes de releer?", "Para buscar una respuesta", "Da un propósito a la lectura."),
    ],
    task("Con un adulto, lee en voz alta dos veces este texto: «Rosa is at home. She has a brown dog. The dog sleeps on the sofa.» Antes de la segunda lectura elige una pregunta de esta lista: Who? What? Where? Relee con el dedo y dime la respuesta en español o en inglés.", "Pregunta: Where does the dog sleep? Respuesta: On the sofa, en el sofá.", ["lee en voz alta con ayuda", "elige una pregunta antes de releer", "señala con el dedo dónde está la respuesta", "responde correctamente"], ["nota del adulto"], ["no volver al texto para responder", "leer demasiado rápido"], "Pregunta qué parte del texto le dio la respuesta y felicítalo por volver a mirar."),
    "Lee en voz alta, a una mascota o un peluche, la frase «I have a red ball» tres veces, cada vez más despacio.",
    "Escribe una pregunta con who, what o where sobre este texto: «Leo has a green hat. It is on his head.» Respóndela.",
)

lesson(
    OA8, 5,
    "Los textos escritos en cada ejercicio, hojas de papel para dibujar y lápices de colores.",
    "Aprenderé a recontar un texto corto en el orden correcto, con ayuda de dibujos y palabras. Sirve para comprobar que entendí la historia y para contarla a otra persona.",
    ["Sé releer con una pregunta.", "Sé decir first, then y last."],
    [
        "Recontar (retell) es contar con tus palabras lo que pasó en un texto. Para recontar bien, primero entiendes el orden de los hechos. En inglés se usan las palabras first (primero), then (luego) y last (al final).",
        "Una ayuda es dibujar (draw). Haces un dibujo para cada parte del texto y los pones en orden. Después usas los dibujos para recontar. Si olvidas algo, miras el dibujo y relees esa parte.",
        "Recontar con apoyo significa que puedes usar dibujos, palabras clave o la ayuda de un adulto. Puedes decir: «First, Mia has a seed. Then she puts it in the ground. Last, she gives it water.» No necesitas repetir cada palabra del texto: lo importante son los hechos y su orden.",
    ],
    [("retell", "recontar"), ("draw", "dibujar"), ("first", "primero"), ("then", "luego"), ("last", "al final"), ("seed", "semilla")],
    [
        ("Ordenar los hechos", "Texto: «Mia has a seed. She puts it in the ground. She gives it water.» ¿Qué hace Mia primero?", ["Busco el primer hecho.", "Mia has a seed.", "Esa es la primera idea."], "Primero tiene una semilla"),
        ("Recontar con first, then, last", "Con ese texto, recuenta usando first, then y last.", ["First: Mia has a seed.", "Then: she puts it in the ground.", "Last: she gives it water."], "First, Mia has a seed. Then she puts it in the ground. Last, she gives it water."),
    ],
    [
        ("Contar los hechos desordenados.", "No se fija en el orden del texto.", "Usa first, then y last para ordenar."),
        ("Repetir el texto palabra por palabra.", "Se cree que recontar es memorizar.", "Cuenta lo importante con tus palabras."),
    ],
    [
        ("¿Qué significa «retell»?", "Recontar", "Re- es de nuevo y tell es decir."),
        ("¿Qué significa «last»?", "Al final", "Se usa para el último hecho."),
        ("¿Qué significa «draw»?", "Dibujar", "Dibujar ayuda a recontar."),
    ],
    [
        ("¿Para qué sirven los dibujos al recontar?", "Para recordar los hechos en orden", "Cada dibujo guarda una parte de la historia."),
        ("¿Qué palabras en inglés ayudan a ordenar un recuento?", "First, then y last", "Marcan el orden de los hechos."),
        ("¿Es necesario repetir el texto igual que está escrito?", "No; basta contar lo importante en orden", "Recontar es con mis propias palabras."),
    ],
    [
        ("Texto: «Leo has bread. He puts cheese on it. He eats it.» ¿Qué hace Leo al final (last)?", "Come el pan", "El último hecho es He eats it."),
        ("Ordena con números: (a) She waters it. (b) Ana has a seed. (c) She plants it (plant = plantar).", "b, c, a", "Primero tiene la semilla, luego la planta y al final la riega."),
        ("Completa con first, then o last: «___, Tom wakes up.» Es el primer hecho del día.", "First", "First indica el primer hecho."),
    ],
    [
        ("Texto: «The bird has a nest. It lays an egg (lay an egg = poner un huevo). The egg opens. A baby bird says peep!» ¿Qué pasa luego (then) de que el pájaro pone un huevo?", "El huevo se abre", "Después de lay an egg viene The egg opens."),
        ("Una niña recuenta: «Last, Mia has a seed. First, she waters it.» ¿Qué orden está mal? Responde en español.", "Dice last y first al revés", "Tener la semilla va primero y regar va al final."),
    ],
    [
        ("Texto: «Sam has a cup. He puts milk in it. He drinks it.» Dibuja tres cuadros en tu cabeza. ¿Qué dibujas en el cuadro del medio? Responde en español.", "Sam pone leche en el vaso", "El hecho del medio es He puts milk in it."),
        ("Recuenta con first, then, last: «Ana has a seed. Ana plants it. Ana waters it.» Escribe en inglés la frase del medio, que empieza con then y usa she.", "Then she plants it", "Then marca el segundo hecho: planta la semilla."),
    ],
    [("Un niño recuenta un cuento a su hermana con tres dibujos: un perro con un hueso, el perro cavando, el perro enterrando el hueso. ¿Cuál dibujo va en último lugar?", "El perro enterrando el hueso", "Es el último hecho de la secuencia.")],
    [
        ("¿Cómo se dice «primero» en inglés?", "first", "Es la palabra para el primer hecho."),
        ("¿Qué significa «then»?", "Luego", "Se usa para unir un hecho con el siguiente."),
        ("¿Qué me ayuda a recontar si olvido algo?", "Mirar mis dibujos y releer esa parte", "Los dibujos son el apoyo para recordar."),
    ],
    task("Lee con un adulto: «Mia has a seed. She puts it in the ground. She gives it water.» Dibuja tres cuadros, uno para cada hecho. Luego recuéntalo mirando los dibujos con las palabras first, then y last, con ayuda del adulto.", "Cuadro 1: Mia con una semilla. Cuadro 2: la semilla en la tierra. Cuadro 3: Mia con un regador. «First, Mia has a seed...»", ["tres dibujos en orden", "usa first, then y last", "cuenta los hechos importantes", "sigue el orden del texto"], ["los tres dibujos", "nota del adulto"], ["poner los dibujos en desorden", "olvidar el hecho final"], "Valora cada dibujo y pregúntale qué pasa entre un cuadro y otro."),
    "Recuenta en español lo que hiciste esta mañana usando primero, luego y al final.",
    "Dibuja tres cuadros sobre cómo te lavas las manos y escribe first, then, last bajo cada uno.",
)

# ================================================================ OA 09
lesson(
    OA9, 1,
    "Los textos escritos en cada ejercicio, hojas, lápices de colores y un lápiz.",
    "Aprenderé a mostrar lo que entendí de un texto en inglés dibujando un detalle y poniéndole una palabra. Sirve para responder a lo que leo sin necesitar muchas palabras.",
    ["Sé leer oraciones cortas con ayuda.", "Sé colores y animales en inglés."],
    [
        "Reaccionar a un texto es decir qué pensaste o sentiste cuando lo leíste. Una manera muy simple es dibujar una ilustración (illustration). Un dibujo puede mostrar lo que entendiste sin escribir ni hablar mucho.",
        "Para ilustrar un detalle, lee la oración y busca las palabras clave: quién, qué tiene y de qué color. Por ejemplo, en «The cat has a red hat», el detalle es un gato con un sombrero rojo. Dibuja justo eso, no otra cosa.",
        "Después puedes agregar una etiqueta (label) o una frase corta, por ejemplo «red hat». Así tu dibujo y tus palabras muestran que comprendiste. Cuando termines, compara con el texto y comprueba que tu dibujo diga lo mismo.",
    ],
    [("illustration", "ilustración, dibujo"), ("detail", "detalle"), ("label", "etiqueta"), ("draw", "dibujar"), ("hat", "sombrero"), ("red hat", "sombrero rojo")],
    [
        ("Ilustrar un detalle", "Texto: «The cat has a red hat.» ¿Qué dibujas?", ["Leo quién es: un gato.", "Leo qué tiene: un sombrero.", "Leo el color: rojo."], "Un gato con un sombrero rojo"),
        ("Etiquetar mi dibujo", "Mi dibujo muestra un gato con un sombrero rojo. ¿Qué etiqueta de dos palabras le pongo?", ["Elijo el detalle importante: el sombrero.", "Digo el color y el objeto.", "Lo escribo en inglés."], "red hat"),
    ],
    [
        ("Dibujar algo que el texto no dice.", "Se agrega una idea propia sin leer los detalles.", "Dibuja solo lo que dice el texto y luego compara."),
        ("Usar un color distinto al del texto.", "No se lee la palabra de color.", "Busca la palabra de color antes de pintar."),
    ],
    [
        ("¿Qué significa «illustration»?", "Ilustración o dibujo", "Es una imagen que muestra una idea."),
        ("Texto: «The dog is brown.» ¿De qué color pintas el perro?", "Café", "Brown significa café."),
        ("¿Qué significa «label»?", "Etiqueta", "Es una palabra escrita junto a un dibujo."),
    ],
    [
        ("¿Para qué sirve ilustrar un detalle de un texto?", "Para mostrar lo que entendí", "El dibujo evidencia mi comprensión."),
        ("¿Qué miras en la oración para saber qué dibujar?", "Quién es, qué tiene y de qué color", "Esos datos están en las palabras clave."),
        ("¿Por qué debes comparar tu dibujo con el texto?", "Para comprobar que dice lo mismo", "Así corrijo errores."),
    ],
    [
        ("Texto: «The bird is yellow.» ¿Qué color usas para el pájaro?", "Amarillo", "Yellow significa amarillo."),
        ("Texto: «The girl has two balls.» ¿Cuántas pelotas dibujas?", "2", "Two es dos."),
        ("Texto: «The fish is blue and small.» Escribe en español las dos características que dibujas.", "Azul y pequeño", "Blue es azul y small es pequeño."),
    ],
    [
        ("Ema dibuja un perro negro para la oración «The dog is white». ¿Qué debe cambiar?", "El color: debe ser blanco", "White significa blanco."),
        ("Texto: «The boy has a green bag.» Dos niños dibujan: Ana, un niño con mochila verde; Leo, un niño con mochila roja. ¿Quién dibujó bien?", "Ana", "Green es verde y Ana dibujó mochila verde."),
    ],
    [
        ("Texto: «A little frog sits on a big leaf.» Escribe en inglés, en una palabra, el nombre del animal.", "frog", "Little frog es la rana pequeña."),
        ("Texto: «The sun is yellow. The sky is blue.» Si dibujas solo el cielo, ¿de qué color es? Responde en inglés, una palabra.", "blue", "El texto dice que el cielo es azul."),
    ],
    [("Una profesora lee: «The cat is on the chair.» Tú dibujas el gato. ¿Dónde lo pones? Responde en español.", "Sobre la silla", "On the chair significa sobre la silla.")],
    [
        ("¿Cómo se dice «detalle» en inglés?", "detail", "Se parece mucho a la palabra en español."),
        ("¿Qué hago después de dibujar?", "Comparo mi dibujo con el texto", "Compruebo que dice lo mismo."),
        ("¿Qué significa «two balls»?", "Dos pelotas", "Two es dos y ball es pelota."),
    ],
    task("Un adulto lee: «The little bear has a blue hat. The bear sits on a big red chair.» Dibuja lo que entendiste y pon dos etiquetas en inglés: una para el sombrero y otra para la silla. Luego muéstrale el dibujo al adulto y di en español un detalle que quisiste mostrar.", "Dibujo de un osito con sombrero azul sentado en una silla roja grande. Etiquetas: blue hat, red chair.", ["dibuja los detalles del texto", "usa los colores correctos", "pone dos etiquetas en inglés", "explica un detalle"], ["el dibujo", "nota del adulto"], ["cambiar los colores", "olvidar la silla"], "Pregúntale por qué eligió esos colores y destaca los detalles correctos."),
    "Dibuja un perro verde con un sombrero amarillo y escribe una etiqueta en inglés.",
    "Inventa una oración corta como «The cat has a blue ball» y pídele a alguien que la dibuje.",
)

lesson(
    OA9, 2,
    "Los textos escritos en cada ejercicio; espacio libre en la sala o el patio y un adulto que lea en voz alta.",
    "Aprenderé a dramatizar un texto corto en inglés con gestos y movimientos. Sirve para comprender y sentir lo que pasa en el texto.",
    ["Sé verbos básicos: jump, run, sit, sleep.", "Sé que dramatizar es actuar."],
    [
        "Dramatizar (drama) es actuar un texto con el cuerpo, la cara y la voz. No necesitas decir todo el texto: con gestos y movimientos puedes mostrar qué pasa. Es una forma de reaccionar a lo que lees.",
        "Para dramatizar, primero lee el texto y busca los verbos, que son las palabras de acción: jump (saltar), run (correr), sit (sentarse), sleep (dormir). Después piensa cómo muestras cada acción con el cuerpo. Por ejemplo, para sleep cierras los ojos y pones las manos bajo la cabeza.",
        "También puedes mostrar cómo se siente un personaje: happy (contento) con una sonrisa, sad (triste) con la cara baja. Cuando dramatices, hazlo con respeto y de forma segura: sin empujar ni correr rápido. Si no quieres actuar frente a otros, puedes hacerlo solo o frente a un adulto.",
    ],
    [("drama", "dramatizar, actuar"), ("jump", "saltar"), ("run", "correr"), ("sit", "sentarse"), ("sleep", "dormir"), ("happy / sad", "contento / triste")],
    [
        ("Gesto para una acción", "Texto: «The rabbit jumps.» ¿Qué gesto haces?", ["Busco el verbo: jumps.", "Jump es saltar.", "Hago saltitos suaves."], "Salto suavemente"),
        ("Mostrar un sentimiento", "Texto: «The boy is sad.» ¿Cómo lo muestras con la cara y el cuerpo?", ["Busco la palabra sad.", "Sad es triste.", "Pongo la cara baja y los hombros caídos."], "Cara triste y cuerpo caído"),
    ],
    [
        ("Actuar rápido y sin cuidado.", "Se piensa que dramatizar es jugar fuerte.", "Muévete con calma, sin empujar."),
        ("Olvidar mirar el texto al actuar.", "Se improvisa algo distinto.", "Usa el verbo del texto para decidir tu gesto."),
    ],
    [
        ("¿Qué significa «sleep»?", "Dormir", "Es una acción que se puede actuar."),
        ("¿Qué gesto haces con «sit»?", "Me siento", "Sit significa sentarse."),
        ("¿Qué significa «run»?", "Correr", "Es una acción de movimiento."),
    ],
    [
        ("¿Para qué sirve dramatizar un texto?", "Para mostrar lo que entendí con el cuerpo", "El gesto muestra la comprensión."),
        ("¿Qué palabras del texto te dicen qué gestos hacer?", "Los verbos o palabras de acción", "Dicen lo que hacen los personajes."),
        ("¿Cómo dramatizas con seguridad?", "Me muevo con calma y sin empujar", "El cuidado evita accidentes."),
    ],
    [
        ("Texto: «The cat sleeps.» ¿Qué gesto haces?", "Cierro los ojos y apoyo la cabeza en las manos", "Sleep es dormir."),
        ("Texto: «The girl is happy.» ¿Qué cara pones?", "Una sonrisa", "Happy significa feliz."),
        ("Texto: «The dog runs.» ¿Qué movimiento haces con calma?", "Muevo las piernas como si corriera", "Run es correr."),
    ],
    [
        ("Texto: «The frog jumps and then sits.» Ordena tus gestos: (a) me siento (b) salto.", "b, a", "Primero salta y luego se sienta."),
        ("Una niña actúa «The bird flies» corriendo por toda la sala. ¿Qué puede cambiar para ser más segura?", "Mover los brazos como alas sin correr", "Fly es volar y se puede mostrar con los brazos."),
    ],
    [
        ("Texto: «A boy is tired. He sits. He sleeps.» Escribe en español los tres gestos en orden.", "Cara cansada, sentarme, dormir", "Tired es cansado, luego sit y sleep."),
        ("Texto: «Mia is sad. Then she is happy.» ¿Qué cambio de cara haces?", "De cara triste a una sonrisa", "Sad pasa a happy."),
    ],
    [("En clase leen «The little duck walks and sits». Un niño no quiere actuar frente a todos. ¿Qué puede hacer?", "Actuar solo o frente a un adulto", "Es una forma respetuosa de participar.")],
    [
        ("¿Cómo se dice «correr» en inglés?", "run", "Es un verbo de acción."),
        ("¿Qué significa «sad»?", "Triste", "Es un sentimiento."),
        ("¿Qué hago si no quiero actuar frente a otros?", "Lo hago solo o frente a un adulto", "Puedo participar de otra forma."),
    ],
    task("Un adulto lee: «The little rabbit jumps, runs, sits and sleeps.» Actúa cada verbo con calma, en ese orden, con un gesto distinto. Luego di en español qué fue lo más difícil de mostrar y con qué gesto lo resolviste.", "Salto suave, piernas que corren sin avanzar, me siento, apoyo la cabeza en las manos.", ["actúa los cuatro verbos en orden", "se mueve con seguridad", "usa gestos distintos", "explica un gesto"], ["video con permiso de la familia o nota del adulto"], ["saltar o correr sin cuidado", "olvidar un verbo"], "Valora la creatividad y pregúntale cuál gesto fue más claro."),
    "Muestra con un gesto cada uno: jump, sit, sleep.",
    "Inventa una escena de tres acciones con verbos en inglés y pide a alguien que adivine qué haces.",
)

lesson(
    OA9, 3,
    "Los textos escritos en cada ejercicio; lápiz. No se necesita compartir datos personales.",
    "Aprenderé a relacionar un texto en inglés con algo que me pasó o que sé, sin contar datos privados. Sirve para conectar lo que leo con mi vida de forma segura.",
    ["Sé decir «I have a dog» y «I like pizza».", "Sé que hay cosas privadas que no se comparten."],
    [
        "Una conexión (connection) es una idea que une un texto con tu vida, con algo que viste o con otro cuento. Puedes decir: «I have a pet too» (yo también tengo una mascota) o «I like the park too» (a mí también me gusta el parque).",
        "Una conexión segura no cuenta datos privados. No digas tu dirección, tu teléfono, el nombre de tu colegio ni los problemas de tu familia. Puedes usar cosas generales: «I like dogs», «I play with a ball», «I eat apples».",
        "Para conectar, lee el texto y pregúntate: ¿esto me recuerda algo? Si la respuesta es sí, di la conexión con una frase simple. Si no quieres compartirla, puedes decir «I pass» (paso) y está bien.",
    ],
    [("connection", "conexión"), ("too", "también"), ("pet", "mascota"), ("I like", "me gusta"), ("I have", "yo tengo"), ("I pass", "paso, no quiero responder")],
    [
        ("Conexión segura", "Texto: «Tom has a dog.» Mi conexión: tengo una mascota. ¿Cómo lo digo en inglés?", ["Uso I have.", "Uso a pet.", "Agrego too."], "I have a pet too."),
        ("Evitar datos privados", "Texto: «Ana plays in the park.» Alguien dice «Yo vivo en la calle... número...». ¿Es una conexión segura?", ["Dice una dirección.", "La dirección es dato privado.", "Una conexión segura no la incluye."], "No es segura; mejor decir I like the park too."),
    ],
    [
        ("Contar la dirección o el teléfono para conectar.", "Se cree que hay que dar detalles personales.", "Usa ideas generales como I like parks."),
        ("Pensar que hay que contestar siempre.", "No se sabe que existe «I pass».", "Puedes decir I pass si no quieres compartir."),
    ],
    [
        ("¿Qué significa «too» en «I like dogs too»?", "También", "Too une mi idea con la del texto."),
        ("¿Qué significa «pet»?", "Mascota", "Es un animal que vive en casa."),
        ("¿Qué significa «connection»?", "Conexión, una idea que une el texto con mi vida", "Une dos cosas."),
    ],
    [
        ("¿Qué datos nunca compartes en una conexión?", "Dirección, teléfono y datos privados", "Son datos personales que no se comparten."),
        ("¿Qué puedes decir si no quieres compartir una conexión?", "I pass", "Es una forma amable de no responder."),
        ("¿Qué pregunta te haces para encontrar una conexión?", "¿Esto me recuerda algo?", "Así unes el texto con tu experiencia."),
    ],
    [
        ("Texto: «Tom has a dog.» Completa en inglés: «I like dogs ___.»", "too", "Too significa también."),
        ("Texto: «Mia eats an apple.» Elige una conexión segura: (a) «I eat apples too.» (b) «My phone number is...»", "a", "La opción a no da datos privados."),
        ("Texto: «Leo plays with a ball.» Escribe en inglés la conexión: «I play with a ball ___.»", "too", "Too es también."),
    ],
    [
        ("Pedro dice «My house is on... street». ¿Qué debe cambiar para que sea segura su conexión?", "Quitar la dirección y decir algo general", "La dirección es un dato privado."),
        ("Texto: «The family eats pizza.» Ema dice «I like pizza too». ¿Es una buena conexión? Responde por qué.", "Sí, porque es general y relaciona el texto con ella", "No da datos privados."),
    ],
    [
        ("Texto: «Rosa has a cat and a fish.» Escribe en inglés una conexión para alguien que tiene un perro, con I have y too.", "I have a dog too", "Se usa I have y too."),
        ("Texto: «The children play in the park.» Escribe una conexión segura de cuatro palabras en inglés con I like y too, sobre el parque.", "I like parks too", "Park es parque y too es también."),
    ],
    [("En la clase leen «Sam has a kite». Una niña no quiere contar de su casa. ¿Qué puede decir en inglés? Responde con dos palabras.", "I pass", "Es una forma respetuosa de no responder.")],
    [
        ("¿Cómo se dice «también» en inglés?", "too", "Se usa al final de una frase."),
        ("¿Qué ejemplo es seguro? (a) «I like dogs.» (b) «My address is...»", "a", "No da datos privados."),
        ("¿Qué significa «pass»?", "Paso, no quiero responder", "Se usa para no compartir."),
    ],
    task("Un adulto lee: «Mia has a cat. The cat is white. Mia plays with the cat.» Elige una conexión segura, por ejemplo «I like cats too» o «I play with a ball too», y dila en voz alta. Luego di «I pass» para practicar cómo decir que no quieres compartir otra conexión.", "«I like cats too.» y luego «I pass.»", ["dice una conexión en inglés", "no da datos privados", "usa too o I like", "practica I pass"], ["nota del adulto"], ["decir datos personales", "no usar too"], "Valora que cuide su privacidad y repite con él la frase si le costó."),
    "Elige un animal que te gusta y di en inglés «I like ___ too».",
    "Escribe dos conexiones seguras con un cuento que conozcas, por ejemplo «I like the sun too».",
)

lesson(
    OA9, 4,
    "Los textos escritos en cada ejercicio; lápiz y tarjetas hechas con papel con una carita feliz, una triste y otra con pulgar arriba.",
    "Aprenderé a decir si me gusta o no un texto en inglés y qué sentí. Sirve para dar mi opinión con respeto y con palabras simples.",
    ["Sé decir happy y sad.", "Sé que opinar es decir lo que pienso."],
    [
        "Una preferencia (preference) es lo que te gusta más. Para decirlo usa «I like...» (me gusta) o «I don't like...» (no me gusta). Por ejemplo: «I like the story» o «I don't like the story». Después puedes agregar una razón con because: «I like it because it is funny».",
        "Un sentimiento (feeling) es lo que sientes: happy (contento), sad (triste), scared (asustado), surprised (sorprendido). Para decirlo usa «I feel...» o «I am...». Por ejemplo, «I feel happy». Una opinión (opinion) es lo que piensas del texto: funny (divertido), nice (lindo), scary (da miedo).",
        "Recuerda que todas las opiniones son válidas, pero se dicen con respeto. Nunca digas que algo es malo para ofender a alguien. Di «I don't like it» y la razón, no «it is awful». Y puedes decir «it is OK» (está bien) cuando no estás seguro.",
    ],
    [("I like / I don't like", "me gusta / no me gusta"), ("feeling", "sentimiento"), ("opinion", "opinión"), ("funny", "divertido"), ("scary", "que da miedo"), ("because", "porque")],
    [
        ("Dar una preferencia", "Texto: «The dog plays with a ball.» Me gusta. ¿Cómo lo digo con una razón?", ["Uso I like.", "Digo qué me gusta.", "Agrego because y la razón."], "I like the story because it is funny."),
        ("Decir un sentimiento", "Después de leer «The cat is lost but finds its home», me siento alegre. ¿Cómo lo digo en inglés?", ["Uso I feel.", "Alegre es happy.", "Junto las dos partes."], "I feel happy."),
    ],
    [
        ("Decir que algo es «malo» para ofender.", "No se piensa cómo se oye.", "Di I don't like it y una razón."),
        ("Copiar la opinión de otro sin pensarla.", "Se quiere decir lo que dice la mayoría.", "Tu opinión es tuya y se dice con respeto."),
    ],
    [
        ("¿Qué significa «I don't like»?", "No me gusta", "Es la forma negativa de I like."),
        ("¿Qué significa «funny»?", "Divertido", "Describe algo que da risa."),
        ("¿Qué significa «feeling»?", "Sentimiento", "Es lo que se siente."),
    ],
    [
        ("¿Para qué sirve decir una razón con because?", "Para explicar por qué pienso así", "La razón da sentido a mi opinión."),
        ("¿Cómo dices tu opinión sin ofender?", "Digo «I don't like it» y la razón", "Es respetuoso y claro."),
        ("¿Se puede tener una opinión distinta a la de otro compañero?", "Sí, todas las opiniones se respetan", "Cada persona piensa diferente."),
    ],
    [
        ("Completa: «I ___ the story» (me gusta).", "like", "I like significa me gusta."),
        ("Completa: «I feel ___» (triste).", "sad", "Sad significa triste."),
        ("Elige la frase para decir que da miedo: (a) «It is funny.» (b) «It is scary.»", "b", "Scary significa que da miedo."),
    ],
    [
        ("Lucas dice «I don't like you, story, because you are bad.» ¿Qué debe cambiar para ser más respetuoso?", "Decir una razón sobre el texto, como «it is sad»", "Así opina sin ofender a nadie."),
        ("Rosa lee un cuento de un perro que ayuda a un niño y dice «I feel happy». ¿Es lógico? Explica.", "Sí, porque el perro ayuda y eso alegra", "El sentimiento coincide con el texto."),
    ],
    [
        ("Ordena las palabras para formar la frase: because / I / it is nice / like it. Escribe la frase completa.", "I like it because it is nice", "Primero la opinión y luego la razón."),
        ("Texto: «The boy lost his ball. He is sad.» Escribe una frase en inglés de tres palabras para decir cómo se siente el niño.", "He is sad", "El texto dice que está triste."),
    ],
    [("Al terminar un cuento, el profesor pregunta «Do you like the story?». Un niño responde «Yes, I like it. It is funny.» ¿Qué opina el niño? Responde en español.", "Que el cuento le gusta y que es divertido", "Like es gustar y funny es divertido.")],
    [
        ("¿Cómo se dice «sentimiento» en inglés?", "feeling", "Es la palabra para lo que sentimos."),
        ("¿Qué significa «scary»?", "Que da miedo", "Describe algo que asusta."),
        ("¿Qué significa «I feel happy»?", "Me siento contento", "Feel es sentir y happy es contento."),
    ],
    task("Un adulto lee: «A little dog loses its toy. It looks under a bed. It looks behind a chair. The dog finds the toy and is happy.» Con tarjetas de carita feliz o triste, elige cómo te sientes. Luego di en inglés: «I like the story because...» y «I feel...».", "«I like the story because it is nice. I feel happy.»", ["dice si le gusta o no el texto", "da una razón con because", "dice un sentimiento con I feel", "se expresa con respeto"], ["nota del adulto"], ["decir solo yes o no", "ofender"], "Valora la razón y repite con él los sentimientos nuevos."),
    "Di en inglés si te gusta el color rojo: «I like red» o «I don't like red».",
    "Escribe una frase con I feel... para cada uno: happy, sad, scared.",
)

lesson(
    OA9, 5,
    "Los textos escritos en cada ejercicio; hojas, lápices de colores y un lugar de la casa para colgar un trabajo.",
    "Aprenderé a elegir una forma de responder a un texto: dibujar, actuar o escribir una frase. Sirve para mostrar lo que entendí y lo que pienso de muchas maneras.",
    ["Sé dibujar un detalle del texto.", "Sé actuar con gestos y decir «I like»."],
    [
        "Puedes responder a un texto de muchas formas (ways). Una es dibujar una ilustración. Otra es dramatizar con gestos. Otra es escribir palabras o frases, por ejemplo «I like it» o «It is funny». Tú eliges la que mejor muestra lo que entendiste.",
        "Una buena respuesta tiene tres partes. Muestra un detalle del texto, es decir, una evidencia (evidence). Dice qué sientes o piensas. Y cuida la privacidad: no incluye datos personales. Por ejemplo, un dibujo con una etiqueta «happy dog» y la frase «I like it».",
        "En una galería de respuestas (response gallery) se muestran los trabajos de todos. Mira con respeto, nunca te burles, y di algo amable: «I like the colors» (me gustan los colores). Cada respuesta es distinta y todas valen si se relacionan con el texto.",
    ],
    [("response", "respuesta, reacción"), ("gallery", "galería, exhibición"), ("evidence", "evidencia, prueba"), ("I like the colors", "me gustan los colores"), ("nice", "lindo, agradable"), ("draw / act / write", "dibujar / actuar / escribir")],
    [
        ("Elegir una forma de respuesta", "Texto: «The cat jumps on the bed.» Quiero mostrar que entendí sin hablar mucho. ¿Qué formas puedo usar?", ["Puedo dibujar el gato en la cama.", "Puedo actuar saltando suavemente.", "Puedo escribir «cat, bed»."], "Dibujar, actuar o escribir son válidas"),
        ("Comentario amable", "Veo el dibujo de un compañero con colores bonitos. ¿Qué digo en inglés?", ["Busco algo positivo.", "Uso I like.", "Digo los colores."], "I like the colors."),
    ],
    [
        ("Burlarse del trabajo de otro.", "No se respeta que cada uno responde diferente.", "Di algo amable como I like the colors."),
        ("Responder con algo que no tiene relación con el texto.", "No se vuelve al texto.", "Incluye un detalle del texto como evidencia."),
    ],
    [
        ("¿Qué significa «gallery»?", "Galería o exhibición", "Es un lugar donde se muestran trabajos."),
        ("¿Qué significa «evidence»?", "Evidencia o prueba", "Muestra que entendí el texto."),
        ("¿Qué significa «nice»?", "Lindo o agradable", "Se usa para elogiar algo."),
    ],
    [
        ("¿Cuáles son tres formas de responder a un texto?", "Dibujar, actuar y escribir", "Son las formas que aprendí."),
        ("¿Qué debe tener una buena respuesta?", "Un detalle del texto y lo que pienso o siento", "Combina evidencia y reacción."),
        ("¿Cómo debes comportarte en una galería de respuestas?", "Con respeto y diciendo algo amable", "Cada trabajo se valora."),
    ],
    [
        ("Texto: «The dog is brown.» Elige la respuesta que tiene evidencia del texto: (a) dibujo de un perro café (b) dibujo de un gato verde", "a", "El texto habla de un perro café."),
        ("Quiero mostrar con una palabra en mi dibujo que me siento contento con el cuento. ¿Qué palabra en inglés escribo?", "happy", "Happy muestra que me siento contento."),
        ("Texto: «The bird sings.» Quiero actuar. ¿Qué gesto uso?", "Abro y cierro la boca como cantando", "Sing es cantar."),
    ],
    [
        ("Un niño dibuja un barco para un texto sobre un perro. ¿Qué le falta a su respuesta?", "Relación con el texto", "El dibujo debe mostrar un detalle del texto."),
        ("Ana dice «Your drawing is bad» en la galería. ¿Qué debería decir en cambio?", "I like the colors o I like your drawing", "Un comentario amable es más respetuoso."),
    ],
    [
        ("Texto: «The girl has a red ball.» Escribe una etiqueta de dos palabras en inglés para ponerle a un dibujo.", "red ball", "Es el detalle del texto."),
        ("Texto: «The fish is happy.» Escribe en español dos formas distintas de responder a este texto.", "Dibujar un pez contento, actuar un pez nadando", "Cada forma muestra el detalle de otra manera."),
    ],
    [("En la galería, un compañero muestra un dibujo de un gato azul y dice «I feel happy». Tú quieres decir algo amable. ¿Qué dices en inglés?", "I like the blue cat o I like your drawing", "Es un comentario amable y concreto.")],
    [
        ("¿Cómo se dice «galería» en inglés?", "gallery", "Es el lugar donde se muestran los trabajos."),
        ("Una respuesta con dibujo, etiqueta y frase, ¿es válida?", "Sí, si se relaciona con el texto", "Muestra comprensión y reacción."),
        ("¿Cuál es un buen comentario amable? (a) «I like your colors.» (b) «It is ugly.»", "a", "La opción a es amable."),
    ],
    task("Un adulto lee: «The little fish is orange. It swims in the blue water. It is happy.» Elige una forma de respuesta: dibujar, actuar o escribir. Hazla y pon una frase en inglés, por ejemplo «happy fish» o «I like it». Luego muestra tu trabajo y recibe un comentario amable del adulto: «I like the colors».", "Dibujo de un pez naranja en agua azul con la frase «happy fish».", ["se relaciona con el texto", "incluye una frase en inglés", "muestra un sentimiento u opinión", "recibe el comentario con respeto"], ["el dibujo o la frase", "nota del adulto"], ["no usar el texto", "no incluir ninguna frase"], "Elogia un detalle concreto del trabajo y pregunta cómo lo eligió."),
    "Elige otra forma de responder al mismo texto del pez y hazla en dos minutos.",
    "Pide a un familiar que haga su propia respuesta al texto y compáralas con respeto.",
)
