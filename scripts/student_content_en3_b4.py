"""Student material for 3.º básico Inglés, EN03 OA 14 (escritura de apoyo en imágenes sobre temas conocidos).

Las imágenes se describen entre corchetes porque el cuaderno no incluye ilustraciones; los puntos ● representan objetos para contar.
Cada estructura se enseña en la propia clase antes de usarla. Las reglas de a/an, plural y -ing se limitan a casos seguros.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA14 = "EN03 OA 14"


def dots(n: int) -> str:
    return " ".join("●" * n)


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


lesson(
    OA14, 1,
    "Las imágenes descritas en cada ejercicio, lápiz grafito, goma y una hoja con renglones para dibujar y rotular.",
    "Aprenderé a escribir una etiqueta (label) precisa para animales, objetos, partes de la casa, ocupaciones, lugares y comidas a partir de una imagen. Sirve para nombrar con claridad lo que veo en inglés.",
    ["Sé copiar y completar oraciones con un modelo.", "Sé algunas palabras de animales, comida y objetos."],
    [
        "Una etiqueta (label) es una palabra o frase corta que nombra lo que muestra una imagen. Con animales y objetos se escribe «a» antes de una palabra que empieza con sonido de consonante: a dog (un perro), a cat (un gato), a book (un libro), a chair (una silla). Se escribe «an» antes de apple (manzana), egg (huevo), elephant (elefante) y orange (naranja).",
        "Las partes de la casa son: kitchen (cocina), bedroom (dormitorio), bathroom (baño), living room (living) y garden (jardín). Las ocupaciones son: teacher (profesor o profesora), doctor, cook (cocinero o cocinera) y farmer (agricultor o agricultora). Los lugares de la escuela son: library (biblioteca), playground (patio de juegos), classroom (sala) y gym (gimnasio). Con las ocupaciones se usa a (a teacher, a doctor) y los lugares suelen escribirse con the (the library, the kitchen).",
        "Algunas comidas como milk (leche), bread (pan) y water (agua) no llevan a ni an: se escribe solo «milk». Para ser preciso (precisely), mira bien la imagen y escribe la palabra exacta, con el artículo correcto cuando corresponda. Revisa que la palabra empiece sin errores y que no escribas otra cosa por apuro.",
    ],
    [("label", "etiqueta"), ("a / an", "un, una"), ("kitchen", "cocina"), ("bedroom", "dormitorio"), ("teacher", "profesor o profesora"), ("milk", "leche")],
    [
        ("Etiquetar un animal", "Imagen: [un perro café]. Escribe la etiqueta.", ["Reconozco el animal: perro es dog.", "Dog empieza con consonante.", "Uso a."], "a dog"),
        ("Etiquetar con an", "Imagen: [una manzana roja]. Escribe la etiqueta.", ["Reconozco la fruta: apple.", "Apple empieza con vocal.", "Uso an."], "an apple"),
    ],
    [
        ("Escribir «a apple».", "Se usa a por costumbre antes de una vocal.", "Antes de apple se escribe an."),
        ("Escribir «a milk».", "Se piensa que todas las palabras llevan a.", "Milk no lleva a ni an."),
    ],
    [
        ("Imagen: [un gato negro]. Escribe la etiqueta en inglés.", "a cat", "Gato es cat y empieza con consonante."),
        ("Imagen: [una persona que enseña frente a una pizarra]. Opciones: teacher, farmer. Escribe la etiqueta con a.", "a teacher", "La pizarra y enseñar muestran que es profesora o profesor."),
        ("¿Qué significa «label»?", "Etiqueta", "Es una palabra o frase que nombra la imagen."),
    ],
    [
        ("Imagen: [un huevo]. Escribe la etiqueta con a o an.", "an egg", "Egg empieza con vocal."),
        ("Imagen: [una cocina con una olla]. Escribe el nombre del lugar de la casa en inglés.", "kitchen", "Kitchen es cocina."),
        ("Imagen: [un vaso de leche]. ¿Cuál etiqueta es correcta? (a) a milk (b) milk", "b", "Milk no lleva a."),
    ],
    [
        ("Imagen: [una mujer con un maletín y un estetoscopio]. Escribe la ocupación con a, en inglés.", "a doctor", "El estetoscopio muestra que es doctora; doctor es la palabra."),
        ("Imagen: [un edificio con muchos libros para leer]. Escribe el lugar de la escuela con the, en inglés.", "the library", "Library es biblioteca."),
        ("Imagen: [una sala con colchonetas y pelotas para hacer ejercicio]. Opciones: gym, library. Escribe el lugar de la escuela con the.", "the gym", "Gym es gimnasio."),
    ],
    [
        ("Una niña escribe «a elephant» para un elefante. ¿Cómo se corrige?", "an elephant", "Elephant empieza con vocal."),
        ("Pedro escribe «a orange» para una naranja. ¿Cómo se corrige?", "an orange", "Orange empieza con vocal."),
    ],
    [
        ("Imagen: [una persona con un delantal que prepara comida en un restaurante]. Opciones: teacher, cook, farmer. Escribe la etiqueta con a.", "a cook", "El delantal y la comida muestran que cocina."),
        ("Imagen: [un campo con vacas y una persona que las cuida]. Opciones: farmer, doctor. Escribe la etiqueta con a.", "a farmer", "El campo y las vacas muestran un agricultor."),
    ],
    [("Estás haciendo carteles para tu sala. Para el dibujo de [una pelota y niños corriendo afuera], elige la etiqueta: (a) playground (b) bathroom", "a", "Playground es el patio de juegos.")],
    [
        ("Imagen: [una sala con pupitres y una pizarra]. Escribe la etiqueta del lugar de la escuela con the, en inglés.", "the classroom", "Classroom es sala de clases."),
        ("¿Cuándo se usa an en vez de a?", "Cuando la palabra empieza con sonido de vocal", "Apple, egg y orange empiezan con vocal."),
        ("Escribe la etiqueta de una imagen de un pan sin a ni an.", "bread", "Bread no lleva a."),
    ],
    task("Rotula en inglés estos seis dibujos, que puedes dibujar tú o imaginar: (1) un perro, (2) una manzana, (3) un huevo, (4) una cocina, (5) un doctor, (6) una biblioteca. Escribe cada etiqueta con a o an cuando corresponda (cocina y biblioteca van con the o solas). Muéstrala a una persona de tu casa y léela en voz alta.", "a dog, an apple, an egg, the kitchen, a doctor, the library", ["escribe las seis etiquetas", "usa a y an correctamente", "las palabras están bien escritas", "las lee en voz alta"], ["los dibujos con etiquetas", "nota de la persona que revisó"], ["escribir a apple", "escribir a milk"], "Revisa con él o ella a y an y celebra las etiquetas precisas."),
    "Rotula tres objetos de tu pieza con una etiqueta en inglés.",
    "Haz una lista de cinco comidas en inglés con la etiqueta correcta, sin olvidar milk y bread.",
)

lesson(
    OA14, 2,
    "Las imágenes descritas y los puntos ● para contar escritos en cada ejercicio, lápiz y una hoja con renglones.",
    "Aprenderé a escribir cómo se siente alguien (happy, sad, angry, tired, hungry) y a escribir cantidades hasta veinte con «There are». Sirve para describir imágenes con sentimientos y números.",
    ["Sé el verbo is y los números hasta diez.", "Sé escribir una oración con mayúscula y punto."],
    [
        "Para escribir un sentimiento (feeling) usa «is» o «am»: «She is happy» (ella está contenta), «He is sad» (él está triste), «I am tired» (estoy cansado o cansada). Otros sentimientos son angry (enojado), hungry (con hambre) y tired (cansado). Mira la cara en la imagen: una sonrisa es happy; lágrimas son sad; el ceño fruncido es angry; un bostezo es tired; una mano en la guata y un plato vacío es hungry.",
        "Para escribir una cantidad usa «There is one...» si hay uno y «There are...» si hay más: «There is one apple» (hay una manzana), «There are five apples» (hay cinco manzanas). En esta clase solo usamos nombres con -s fácil: apple → apples, ball → balls, book → books, cat → cats. Los números del uno al veinte son: one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty.",
        "Antes de escribir, cuenta los objetos tocando cada uno una vez. Luego escribe la cantidad con letras, no con números: «There are twelve balls», no «There are 12 balls». Revisa que el número, el nombre en plural y el punto final estén bien. Si hay solo uno, el nombre va sin -s.",
    ],
    [("feeling", "sentimiento"), ("happy / sad", "contento / triste"), ("angry / tired", "enojado / cansado"), ("hungry", "con hambre"), ("There is one", "hay uno"), ("There are", "hay (varios)")],
    [
        ("Escribir un sentimiento", "Imagen: [una niña que llora]. Escribe una oración con She is.", ["La cara muestra lágrimas.", "Lágrimas es sad.", "Escribo She is sad."], "She is sad."),
        ("Escribir una cantidad", f"Imagen: {dots(7)} (siete manzanas). Escribe cuántas hay.", ["Cuento tocando cada una: 7.", "7 es seven.", "Uso There are y apples."], "There are seven apples."),
    ],
    [
        ("Escribir «There are 7 apples» con número.", "Se escribe el número en cifras.", "Escribe el número con letras: seven."),
        ("Escribir «There are one apple».", "Se usa are con uno.", "Con uno se dice There is one apple."),
    ],
    [
        ("Imagen: [un niño que sonríe]. Completa: «He is ___.»", "happy", "Una sonrisa muestra que está contento."),
        ("¿Cómo se dice 12 en inglés?", "twelve", "Es el número después de eleven."),
        ("¿Qué significa «tired»?", "Cansado", "Se usa para decir cómo se siente alguien."),
    ],
    [
        ("Imagen: [un niño con el ceño fruncido y los brazos cruzados]. Escribe la oración con He is.", "He is angry.", "El ceño fruncido muestra que está enojado."),
        ("Imagen: [un niño que bosteza]. Completa: «He is ___.»", "tired", "Un bostezo muestra cansancio."),
        ("¿Cuándo escribes «There is one»?", "Cuando hay solo uno", "Is va con uno."),
    ],
    [
        (f"Imagen: {dots(5)} (cinco pelotas). Escribe cuántas hay, con There are y balls.", "There are five balls.", "5 es five y el nombre lleva -s."),
        (f"Imagen: {dots(13)} (trece libros). Escribe cuántos hay, con There are y books.", "There are thirteen books.", "13 es thirteen."),
        (f"Imagen: {dots(1)} (un gato). Escribe la oración con There is one.", "There is one cat.", "Con uno se usa is y el nombre sin -s."),
    ],
    [
        ("Una niña escribe «There are 8 cats» con cifra. ¿Cómo lo escribes con letras?", "There are eight cats.", "8 se escribe eight."),
        ("Paula escribe «There are one ball». ¿Cómo se corrige?", "There is one ball.", "Con uno se usa is."),
    ],
    [
        (f"Cuenta: {dots(16)}. Son pelotas. Escribe la oración completa.", "There are sixteen balls.", "Hay 16 pelotas, sixteen."),
        (f"Hay {dots(9)} manzanas y luego comen {dots(2)}. ¿Cuántas quedan? Escribe la oración con There are y apples.", "There are seven apples.", "9 menos 2 son 7, seven."),
    ],
    [("Para el cartel de una feria escolar, la imagen muestra [una niña con las manos en la guata frente a un plato vacío]. Elige la oración correcta: (a) She is hungry. (b) She is angry.", "a", "La guata y el plato vacío muestran hambre.")],
    [
        ("¿Cómo se dice «contento» en inglés?", "happy", "Es un sentimiento."),
        ("¿Cómo escribes 20 con letras?", "twenty", "Es el número final de la lista."),
        ("¿Qué letra se agrega a apple si hay varias manzanas?", "s", "Apple se convierte en apples."),
    ],
    task("Mira estas dos imágenes y escribe una oración para cada una. Imagen 1: [una niña con una gran sonrisa que sostiene un globo]. Imagen 2: " + dots(14) + " (catorce lápices). Para la imagen 1 escribe cómo se siente la niña; para la imagen 2 escribe cuántos lápices (pencils) hay. Después inventa y escribe una oración con un sentimiento y otra con una cantidad hasta veinte. Revisa mayúscula, número escrito con letras y punto.", "She is happy. There are fourteen pencils.", ["escribe un sentimiento con is", "escribe la cantidad con letras", "usa There are y plural", "revisa mayúscula y punto"], ["las cuatro oraciones", "nota de la persona que revisó"], ["escribir el número en cifras", "usar are con uno"], "Pide que cuente de nuevo los objetos y revise el plural."),
    "Escribe una oración con un sentimiento tuyo de hoy, por ejemplo I am happy.",
    "Cuenta objetos de tu pieza y escribe tres oraciones con There are y un número hasta veinte.",
)

lesson(
    OA14, 3,
    "Las imágenes descritas en cada ejercicio, algunos objetos de casa para colocar en distintos lugares y lápiz.",
    "Aprenderé a escribir dónde está un objeto con in, on, under, next to, behind e in front of, también en partes de la casa. Sirve para describir la ubicación de objetos en una imagen.",
    ["Sé The cat is big.", "Sé las palabras in, on y under."],
    [
        "Para escribir dónde está algo usa «is» y una palabra de lugar: «The ball is in the box» (la pelota está en la caja). Las palabras de lugar son: in (dentro de), on (sobre), under (debajo de), next to (al lado de), behind (detrás de) e in front of (delante de). Siempre van antes de «the» y del lugar: «The cat is under the table».",
        "También puedes escribir en qué parte de la casa está algo: «The bed is in the bedroom» (la cama está en el dormitorio), «The sofa is in the living room» (el sofá está en el living), «The plant is in the garden» (la planta está en el jardín). Aquí in significa «en» un lugar grande.",
        "Para escribir bien, mira la imagen y responde dos preguntas: ¿qué objeto es? y ¿dónde está? Luego escribe «The (objeto) is (palabra de lugar) the (lugar)». Revisa que la palabra de lugar sea la que muestra la imagen: no es lo mismo on que under. Cierra con un punto.",
    ],
    [("in front of", "delante de"), ("behind", "detrás de"), ("next to", "al lado de"), ("bedroom", "dormitorio"), ("living room", "living"), ("sofa", "sofá")],
    [
        ("Escribir la ubicación", "Imagen: [una pelota debajo de una mesa]. Escribe una oración.", ["El objeto es la pelota: the ball.", "La palabra de lugar es under.", "El lugar es the table."], "The ball is under the table."),
        ("Ubicar en la casa", "Imagen: [una cama en un dormitorio]. Escribe una oración.", ["El objeto es the bed.", "El lugar es the bedroom.", "Uso in."], "The bed is in the bedroom."),
    ],
    [
        ("Escribir «The ball is in the table» para una pelota debajo de la mesa.", "Se elige una palabra de lugar sin mirar la imagen.", "Mira la imagen y escribe under."),
        ("Olvidar el verbo is: «The cat under the chair».", "Se traduce palabra por palabra.", "Escribe The cat is under the chair."),
    ],
    [
        ("Imagen: [un libro sobre una mesa]. Completa: «The book is ___ the table.»", "on", "On significa sobre."),
        ("Imagen: [un gato dentro de una caja]. Completa: «The cat is ___ the box.»", "in", "In significa dentro de."),
        ("¿Qué significa «behind»?", "Detrás de", "Es una palabra de lugar."),
    ],
    [
        ("Imagen: [un perro al lado de una silla]. Completa con dos palabras: «The dog is ___ the chair.»", "next to", "Next to es al lado de."),
        ("Imagen: [una mochila detrás de una puerta]. Completa: «The bag is ___ the door.»", "behind", "Behind es detrás de."),
        ("Imagen: [un niño delante de la casa]. Completa con tres palabras: «The boy is ___ the house.»", "in front of", "In front of es delante de."),
    ],
    [
        ("Imagen: [una pelota sobre una caja]. Escribe la oración con The ball.", "The ball is on the box.", "On indica sobre."),
        ("Imagen: [un sofá en el living]. Escribe la oración con The sofa.", "The sofa is in the living room.", "In indica dentro de la parte de la casa."),
        ("Imagen: [una planta en el jardín]. Escribe la oración con The plant (planta).", "The plant is in the garden.", "Garden es jardín."),
    ],
    [
        ("Marta escribe «The cat is on the box» para un gato dentro de una caja. ¿Qué palabra cambia?", "on por in", "In significa dentro de."),
        ("Leo escribe «The ball is in front of the chair» para una pelota detrás de la silla. ¿Qué cambia?", "in front of por behind", "La imagen muestra detrás de."),
    ],
    [
        ("Imagen: [un lápiz sobre una mesa y un lápiz debajo de la mesa]. Escribe la oración del lápiz que está debajo, con The pencil.", "The pencil is under the table.", "Under indica debajo de."),
        ("Ordena las palabras: is / The / behind / the door / bag. Escribe la oración con punto.", "The bag is behind the door.", "Se respeta The objeto is lugar."),
    ],
    [("En un cartel de tu pieza ayudas a ordenar. La imagen muestra [una mochila debajo de la cama]. Escribe la oración con The bag y the bed.", "The bag is under the bed.", "Under indica debajo de.")],
    [
        ("¿Cómo se dice «al lado de» en inglés?", "next to", "Es una palabra de lugar de dos palabras."),
        ("¿Qué significa «The sofa is in the living room»?", "El sofá está en el living", "Living room es el living."),
        ("¿Qué dos preguntas te haces antes de escribir la ubicación?", "Qué objeto es y dónde está", "Así sabes qué escribir."),
    ],
    task("Mira estas tres imágenes y escribe una oración para cada una: (1) [una pelota debajo de una silla]; (2) [un gato sobre una cama]; (3) [una planta en el jardín]. Luego usa un objeto de tu casa y colócalo delante de, detrás de y al lado de otro objeto; escribe tres oraciones. Revisa cada una con mayúscula, espacios, is y punto.", "(1) The ball is under the chair. (2) The cat is on the bed. (3) The plant is in the garden.", ["escribe las tres oraciones", "usa la palabra de lugar correcta", "usa is y the", "escribe mayúscula y punto"], ["las seis oraciones", "nota de la persona que revisó"], ["elegir una palabra de lugar sin mirar", "olvidar is"], "Pide que mueva el objeto y vuelva a leer la oración para comprobarla."),
    "Escribe tres oraciones sobre dónde están tres objetos de tu escritorio.",
    "Dibuja tu pieza y escribe cuatro etiquetas con una oración de ubicación.",
)

lesson(
    OA14, 4,
    "Las imágenes descritas en cada ejercicio, lápiz y una persona de tu casa para hacer mímica.",
    "Aprenderé a escribir lo que se ve que alguien hace en una imagen con «is/are» y -ing. Sirve para describir acciones que ocurren ahora.",
    ["Sé verbos básicos: read, eat, play, sleep.", "Sé escribir The boy is big."],
    [
        "Para escribir lo que alguien hace en la imagen usa «is» o «are» y el verbo con -ing: «The boy is reading» (el niño está leyendo), «The girl is eating» (la niña está comiendo), «The dog is sleeping» (el perro está durmiendo). Si hay más de una persona, usa «are» y agrega -s al nombre: «The girls are playing» (las niñas están jugando), «The boys are singing» (los niños están cantando).",
        "Con estos verbos solo se agrega -ing: read, eat, play, draw, sing, jump, drink, sleep, paint. Estos tres duplican la última letra: run → running, swim → swimming, sit → sitting. Estos dos pierden la e: write → writing, dance → dancing. Para escribir sin errores, di el verbo con -ing en voz alta y compara con la lista.",
        "Antes de escribir, mira quién está en la imagen y qué hace. Primero escribe el sujeto (the boy, the girls), luego is o are y al final el verbo con -ing. Revisa que el sujeto y is/are coincidan: uno es is; varios son are. Cierra con un punto.",
    ],
    [("reading", "leyendo"), ("playing", "jugando"), ("running", "corriendo"), ("writing", "escribiendo"), ("The girls are...", "las niñas están..."), ("The boy is...", "el niño está...")],
    [
        ("Escribir una acción", "Imagen: [un niño que lee un libro]. Escribe una oración.", ["El sujeto es the boy.", "El verbo es read, con -ing: reading.", "Uso is."], "The boy is reading."),
        ("Escribir varias personas", "Imagen: [dos niñas que corren]. Escribe una oración.", ["El sujeto es the girls.", "Con varias personas uso are.", "Run se escribe running."], "The girls are running."),
    ],
    [
        ("Escribir «The girls is playing».", "Se usa is con varias personas.", "Con varias personas se usa are."),
        ("Escribir «The boy is runing».", "No se duplica la n.", "Run se escribe running."),
    ],
    [
        ("Imagen: [un perro que duerme]. Completa: «The dog is ___.»", "sleeping", "Sleep más ing."),
        ("Imagen: [una niña que come una manzana]. Completa: «The girl is ___.»", "eating", "Eat más ing."),
        ("¿Qué significa «The girls are playing»?", "Las niñas están jugando", "Are y playing indican una acción ahora."),
    ],
    [
        ("Imagen: [un niño que bebe agua]. Completa: «The boy is ___ water.»", "drinking", "Drink más ing."),
        ("Imagen: [dos niños que cantan]. Completa: «The boys ___ singing.»", "are", "Con varios sujetos se usa are."),
        ("¿Cómo se escribe «swim» con -ing?", "swimming", "Se duplica la m."),
    ],
    [
        ("Imagen: [una niña que escribe en su cuaderno]. Escribe la oración con The girl.", "The girl is writing.", "Write pierde la e y recibe ing."),
        ("Imagen: [dos niños que juegan en el patio]. Escribe la oración con The boys.", "The boys are playing.", "Play más ing con are."),
        ("Imagen: [un niño sentado en una silla]. Escribe la oración con The boy y sitting.", "The boy is sitting.", "Sit duplica la t."),
    ],
    [
        ("Ana escribe «The cat sleeping». ¿Qué palabra le falta?", "is", "Antes de sleeping va is."),
        ("Leo escribe «The girls is dancing». ¿Qué palabra corriges?", "is por are", "Con varias personas se usa are."),
    ],
    [
        ("Imagen: [una niña que baila]. Escribe la oración con The girl y dancing.", "The girl is dancing.", "Dance pierde la e y recibe ing."),
        ("Ordena las palabras: is / The / jumping / dog. Escribe la oración con punto.", "The dog is jumping.", "Se respeta sujeto, is y verbo con -ing."),
    ],
    [("En una exposición, la imagen dice [dos niños que dibujan]. Escribe la oración que va debajo, con The boys y drawing.", "The boys are drawing.", "Con varios niños se usa are y draw más ing.")],
    [
        ("¿Cómo se dice «leyendo» en inglés?", "reading", "Read más ing."),
        ("¿Cuándo usas «are» en vez de «is»?", "Cuando hay varias personas", "Are va con varios sujetos."),
        ("¿Cómo se escribe «run» con -ing?", "running", "Se duplica la n."),
    ],
    task("Escribe una oración para cada imagen: (1) [una niña que lee un libro]; (2) [dos niños que corren]; (3) [un perro que duerme]; (4) [una niña que escribe]. Revisa que is/are coincida con el sujeto y que cada verbo con -ing esté bien escrito. Luego haz una mímica con una persona de tu casa y escribe una oración sobre lo que hace.", "(1) The girl is reading. (2) The boys are running. (3) The dog is sleeping. (4) The girl is writing.", ["escribe las cuatro oraciones", "usa is o are según el sujeto", "escribe bien running y writing", "escribe mayúscula y punto"], ["las oraciones escritas", "nota de la persona que revisó"], ["decir The girls is", "escribir runing"], "Pide que diga el verbo con -ing en voz alta antes de escribir."),
    "Mira por la ventana y escribe una oración sobre lo que alguien hace ahora.",
    "Escribe tres oraciones sobre las acciones de tres personas o personajes que dibujes.",
)

lesson(
    OA14, 5,
    "La imagen descrita, el modelo de ficha y la lista de revisión escritos en esta clase, lápiz grafito, goma y una hoja.",
    "Aprenderé a crear y revisar una mini ficha de información con una etiqueta, un sentimiento, una cantidad, una ubicación y una acción sobre una imagen. Sirve para reunir lo aprendido en un texto corto.",
    ["Sé etiquetar, escribir sentimientos, cantidades, ubicaciones y acciones.", "Sé revisar mayúscula, espacios y punto."],
    [
        "Una ficha de información (information card) reúne varias oraciones cortas sobre una imagen. Esta ficha tiene cinco líneas: etiqueta (a boy), sentimiento (He is happy.), cantidad (There are three apples.), ubicación (The cat is under the table.) y acción (The boy is reading.). Imagen: [un niño que lee y sonríe en el living, tres manzanas sobre la mesa y un gato debajo de la mesa].",
        "Para escribir la ficha, mira la imagen y busca cada dato. Escribe una línea por dato, con mayúscula al comienzo, espacios entre las palabras y punto final. Después revisa con esta lista: (1) a o an bien usado; (2) is o are correcto; (3) número escrito con letras; (4) verbo con -ing bien escrito; (5) palabra de lugar que coincide con la imagen.",
        "Revisar es parte de escribir. Si encuentras un error, corrígelo y vuelve a leer la línea en voz alta. Luego muestra tu ficha a otra persona y pregunta si se entiende. Una buena ficha tiene frases correctas, claras y que corresponden a la imagen.",
    ],
    [("information card", "ficha de información"), ("label", "etiqueta"), ("feeling", "sentimiento"), ("quantity", "cantidad"), ("location", "ubicación"), ("action", "acción")],
    [
        ("Armar la ficha", "Imagen: [un niño que lee y sonríe en el living, tres manzanas sobre la mesa, un gato debajo de la mesa]. Escribe la línea de la acción.", ["La acción es leer.", "El sujeto es the boy.", "Escribo is y reading."], "The boy is reading."),
        ("Revisar una línea", "Una línea dice «there are three apple on the table». ¿Qué corriges?", ["Falta la mayúscula en There.", "Apple debe ser apples.", "Falta el punto final."], "There are three apples on the table."),
    ],
    [
        ("Escribir una ficha con datos que no están en la imagen.", "Se inventan datos sin mirar.", "Escribe solo lo que se ve."),
        ("Entregar la ficha sin usar la lista de revisión.", "Se cree que escribir una vez es suficiente.", "Revisa con la lista antes de entregar."),
    ],
    [
        ("Imagen: [un niño que sonríe]. Escribe la línea del sentimiento con He.", "He is happy.", "La sonrisa muestra que está contento."),
        ("Imagen: [un gato debajo de una mesa]. Escribe la línea de ubicación con The cat.", "The cat is under the table.", "Under es debajo de."),
        ("¿Cuántas líneas tiene la ficha de la clase?", "5", "Etiqueta, sentimiento, cantidad, ubicación y acción."),
    ],
    [
        (f"Imagen: {dots(3)} (tres manzanas). Escribe la línea de cantidad con There are y apples.", "There are three apples.", "3 es three y el nombre lleva -s."),
        ("Imagen: [un niño]. Escribe la línea de etiqueta con a.", "a boy", "Boy empieza con consonante."),
        ("¿Qué compruebas con la lista de revisión en el punto 5?", "Que la palabra de lugar coincide con la imagen", "Es el último punto de la lista."),
    ],
    [
        ("Imagen: [un niño que lee]. Escribe la línea de acción con The boy.", "The boy is reading.", "Read más ing."),
        ("Imagen: [una niña que dibuja]. Escribe la línea de acción con The girl.", "The girl is drawing.", "Draw más ing."),
        ("Imagen: [un perro sobre la cama]. Escribe la línea de ubicación con The dog.", "The dog is on the bed.", "On indica sobre."),
    ],
    [
        ("Una línea dice «The girls is reading.» ¿Qué corriges?", "is por are", "Con varias niñas se usa are."),
        ("Una línea dice «There are twelve ball.» ¿Qué corriges?", "ball por balls", "Con doce se agrega -s."),
    ],
    [
        ("Ficha incompleta: una imagen muestra [una niña que sonríe]. Una persona escribió «She is sad.» ¿Qué palabra corriges y cuál es la correcta?", "sad por happy", "La sonrisa muestra que está contenta."),
        ("Una ficha dice «The cat is next to the table.» pero la imagen muestra [un gato debajo de la mesa]. Escribe la línea corregida.", "The cat is under the table.", "La imagen muestra debajo de."),
    ],
    [("Para una exposición del curso, la imagen es [un niño que sonríe y lee, tres manzanas sobre la mesa y un gato debajo de la mesa]. Escribe la línea del sentimiento y luego la línea de la cantidad, en ese orden, cada una con su punto.", "He is happy. There are three apples.", "Se escriben las dos líneas con is y are.")],
    [
        ("¿Cómo se dice «ficha de información» en inglés?", "information card", "Es el texto con cinco líneas."),
        ("¿Para qué sirve la lista de revisión?", "Para encontrar y corregir errores", "Revisar mejora el texto."),
        ("¿Qué escribes en una ficha: solo lo que se ve o también lo que inventas?", "Solo lo que se ve", "La ficha debe coincidir con la imagen."),
    ],
    task("Mira esta imagen: [una niña que escribe y sonríe en la sala de clases; cuatro libros sobre un escritorio; una mochila debajo del escritorio]. (desk es escritorio; bag es mochila). Escribe una ficha de cinco líneas: (1) etiqueta de la niña, (2) su sentimiento, (3) la cantidad de libros, (4) la ubicación de la mochila y (5) la acción de la niña. Revisa con la lista (a/an, is/are, número con letras, -ing, palabra de lugar) y corrige con lápiz. Muestra la ficha a una persona de tu casa.", "a girl. She is happy. There are four books. The bag is under the desk. The girl is writing.", ["escribe las cinco líneas", "usa a, is/are, número y -ing correctos", "la ubicación coincide con la imagen", "revisa con la lista y corrige"], ["la ficha escrita y corregida", "nota de la persona que la leyó"], ["inventar datos", "no revisar con la lista"], "Pregunta qué corrigió y valora que cada línea coincide con la imagen."),
    "Dibuja una escena simple y escribe una ficha de cinco líneas sobre tu dibujo.",
    "Escribe una ficha de información sobre una foto de tu casa, sin datos personales.",
)
