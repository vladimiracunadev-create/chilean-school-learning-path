"""Student material for 2.º básico Inglés, EN02 OA 13 (escritura con modelo) y OA 14 (escritura sobre la base de imágenes).

Las imágenes se describen entre corchetes porque el cuaderno no incluye ilustraciones; cada ejercicio trae su banco de palabras.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA13, OA14 = "EN02 OA 13", "EN02 OA 14"


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


# ================================================================ OA 13
lesson(
    OA13, 1,
    "Las oraciones modelo escritas en cada ejercicio, lápiz, borrador y un cuaderno con líneas.",
    "Aprenderé a copiar palabras y oraciones en inglés entendiendo qué significan. Sirve para escribir bien las primeras palabras y oraciones en inglés con ayuda de un modelo.",
    ["Sé escribir mi nombre y palabras cortas en español.", "Sé leer palabras como cat, dog y red."],
    [
        "Copiar (copy) es escribir lo mismo que ves en un modelo (model). Un modelo es una palabra u oración ya escrita que te sirve de guía. Antes de copiar, léela en voz alta y piensa qué significa. Por ejemplo, «I have a red cat» significa «tengo un gato rojo».",
        "Una oración en inglés empieza con letra mayúscula (capital letter), tiene un espacio (space) entre cada palabra y termina con un punto (period). Por ejemplo: «The dog is big.» Mira cada letra del modelo y escríbela en el mismo orden. Las palabras no se pegan: deja un espacio entre ellas.",
        "Para copiar bien, mira el modelo, di la palabra, escríbela y compárala. Si hay una letra distinta, bórrala y corrígela. Copiar con atención te ayuda a recordar la ortografía de las palabras. Recuerda que el pronombre I siempre va en mayúscula, aunque esté en medio de la oración.",
    ],
    [("copy", "copiar"), ("model", "modelo"), ("capital letter", "letra mayúscula"), ("space", "espacio"), ("period", "punto"), ("sentence", "oración")],
    [
        ("Copiar una oración", "Copia exactamente: «The dog is big.»", ["Leo la oración y entiendo: el perro es grande.", "Escribo la mayúscula en The.", "Dejo espacios y termino con punto."], "The dog is big."),
        ("Copiar con significado", "Modelo: «I have a red cat.» ¿Qué significa?", ["Leo cada palabra.", "I have es yo tengo.", "Red cat es gato rojo."], "Tengo un gato rojo"),
    ],
    [
        ("Escribir las palabras pegadas, como Thedogisbig.", "No se deja espacio entre las palabras.", "Deja un espacio entre cada palabra."),
        ("Olvidar el punto final.", "No se mira el final del modelo.", "Termina cada oración con un punto."),
    ],
    [
        ("¿Qué significa «copy»?", "Copiar", "Es escribir lo mismo que el modelo."),
        ("¿Con qué letra empieza una oración en inglés?", "Con mayúscula", "Todas las oraciones empiezan con mayúscula."),
        ("¿Qué signo va al final de la oración?", "Un punto", "Period es punto."),
    ],
    [
        ("¿Qué haces antes de copiar una oración?", "La leo y entiendo qué significa", "Copiar con sentido ayuda a recordarla."),
        ("¿Por qué debes dejar espacios entre palabras?", "Para que se puedan leer", "Las palabras pegadas se confunden."),
        ("¿Cómo compruebas tu copia?", "La comparo con el modelo letra por letra", "Así descubro errores."),
    ],
    [
        ("Copia exactamente: «I have a blue pen.»", "I have a blue pen.", "Copia con mayúscula, espacios y punto."),
        ("Copia exactamente: «The sun is hot.»", "The sun is hot.", "Se copian las cuatro palabras."),
        ("Modelo: «A cat is on the bed.» ¿Qué significa?", "Un gato está sobre la cama", "On the bed es sobre la cama."),
    ],
    [
        ("Un niño copió «the cat is red» desde el modelo «The cat is red.». ¿Qué dos cosas le faltan?", "La mayúscula y el punto", "El modelo tiene The con mayúscula y punto final."),
        ("Copia de «I like pizza.» hecha por Ana: «I likepizza.» ¿Qué error tiene?", "Falta un espacio entre like y pizza", "Cada palabra va separada."),
    ],
    [
        ("Encuentra la copia correcta del modelo «We have two dogs.»: (a) We have two dogs. (b) we have two dog", "a", "La a copia todas las palabras, la mayúscula y el punto."),
        ("Copia del modelo «She is a doctor.», escribiendo cada palabra con una barra entre ellas: She / is / a / doctor. Escribe la oración completa.", "She is a doctor.", "Se junta con espacios y se termina con punto."),
    ],
    [("En el cuaderno de inglés hay un modelo: «I like apples.» Tu profesor dice «Copy, please». ¿Qué escribes?", "I like apples.", "Se copia igual, con mayúscula y punto.")],
    [
        ("¿Cómo se dice «oración» en inglés?", "sentence", "Es una idea completa escrita."),
        ("¿Cómo se escribe yo en inglés cuando va en medio de una oración?", "I", "Siempre va en mayúscula."),
        ("¿Qué es un «model»?", "Un modelo", "Es un ejemplo escrito que copio."),
    ],
    task("Copia con lápiz en tu cuaderno estas tres oraciones: «I have a red ball.», «The dog is big.», «We like the park.» Después lee cada una en voz alta con un adulto, di qué significa en español y revisa con tu dedo que tengas mayúscula, espacios y punto.", "I have a red ball. / The dog is big. / We like the park.", ["copia las tres oraciones exactas", "usa mayúscula al inicio", "deja espacios entre palabras", "termina con punto"], ["el cuaderno"], ["pegar palabras", "olvidar el punto"], "Marca con un visto cada oración correcta y pide corregir con calma las otras."),
    "Copia tu nombre tres veces con mayúscula inicial.",
    "Copia dos oraciones de un libro en inglés y revisa tu copia con una lupa o con el dedo.",
)

lesson(
    OA13, 2,
    "Las oraciones con espacios y los bancos de palabras escritos en cada ejercicio, lápiz y cuaderno.",
    "Aprenderé a completar oraciones en inglés eligiendo la palabra correcta de un banco de palabras. Sirve para escribir con apoyo y entender el orden de las palabras.",
    ["Sé copiar oraciones con mayúscula, espacios y punto.", "Sé algunas palabras como apple, cat y red."],
    [
        "Completar (complete) una oración es escribir la palabra que falta. Para ayudarte hay un banco de palabras (word bank), que es una lista de palabras entre las que debes elegir. Por ejemplo: «The ___ is red.» con el banco: apple, dog, sun. La palabra correcta es apple, porque una manzana puede ser roja.",
        "Para elegir bien, lee toda la oración antes de escribir. Piensa qué tipo de palabra falta: ¿un animal, un color, una cantidad, un lugar? Prueba la palabra en la oración y pregunta si tiene sentido. Después, escribe la oración completa con mayúscula, espacios y punto.",
        "El orden de las palabras (word order) en inglés es muy importante. Normalmente decimos primero quién, luego qué hace o cómo es, y al final más datos. Por ejemplo: «The cat is black.» (El gato es negro). No se dice «Black the cat is». Si el orden cambia, la oración puede no tener sentido.",
    ],
    [("complete", "completar"), ("word bank", "banco de palabras"), ("word order", "orden de las palabras"), ("missing", "que falta"), ("choose", "elegir"), ("sentence", "oración")],
    [
        ("Elegir del banco", "Completa: «The ___ is red.» Banco: apple, dog, sun.", ["Leo la oración.", "Pienso: algo que puede ser rojo.", "Apple tiene sentido."], "The apple is red."),
        ("Cuidar el orden", "Ordena para escribir una oración: black / is / The cat.", ["Busco quién: The cat.", "Luego is.", "Luego black."], "The cat is black."),
    ],
    [
        ("Escribir una palabra del banco sin leer la oración.", "No se comprueba el sentido.", "Lee toda la oración y prueba la palabra."),
        ("Cambiar el orden: «Black the cat is».", "Se traduce palabra por palabra.", "Sigue el orden del modelo: quién, es, cómo."),
    ],
    [
        ("¿Qué significa «word bank»?", "Banco de palabras", "Es una lista de palabras para elegir."),
        ("¿Qué significa «missing»?", "Que falta", "La palabra que falta es la que debes escribir."),
        ("¿Qué significa «word order»?", "Orden de las palabras", "Cada palabra va en su lugar."),
    ],
    [
        ("¿Qué haces antes de elegir una palabra del banco?", "Leo toda la oración", "Así veo qué palabra tiene sentido."),
        ("¿Por qué importa el orden de las palabras?", "Porque cambia el sentido de la oración", "Un orden distinto puede confundir."),
        ("¿Qué compruebas al terminar?", "Mayúscula, espacios y punto", "Son las reglas de la oración."),
    ],
    [
        ("Completa con una palabra del banco (dog, apple, sun): «I have a ___.» Elige un animal.", "dog", "Solo dog es un animal."),
        ("Banco: yellow, blue, pink. Completa «The banana is ___.» (una banana madura)", "yellow", "Las bananas son amarillas."),
        ("Banco: two, ten, twenty. Completa «I have ___ hands.»", "two", "Se tienen dos manos."),
    ],
    [
        ("Banco: sun, moon, bird. Completa «The ___ is hot.» ¿Qué palabra es correcta?", "sun", "El sol es caliente."),
        ("Pablo escribió «The cat black is». ¿Cómo se ordena?", "The cat is black.", "El verbo is va después del sujeto."),
    ],
    [
        ("Completa «We play in the ___.» Banco: park, soup, shoe. Escribe la palabra y la oración completa.", "We play in the park.", "Park tiene sentido con play."),
        ("Banco: cold, hot, red. Completa «Ice is ___.»", "cold", "El hielo es frío."),
    ],
    [("En ciencias, tu profesora escribe «A plant needs ___». El banco tiene water, shoes, cake. ¿Qué eliges y por qué en una palabra?", "water", "Las plantas necesitan agua.")],
    [
        ("¿Cómo se dice «completar» en inglés?", "complete", "Es la acción de poner lo que falta."),
        ("Banco: red, cat, run. Completa «I like the red ___.» Elige el sustantivo.", "cat", "Cat es el nombre que puede ser red."),
        ("¿Qué es un banco de palabras?", "Una lista de palabras para elegir", "Facilita la escritura."),
    ],
    task("Completa cada oración con la palabra de su banco y escribe la oración completa en tu cuaderno: (1) «The ___ is yellow.» (sun, dog, book) (2) «I have a ___ pencil.» (blue, run, cat) (3) «We ___ in the park.» (play, red, apple). Luego revisa mayúscula, espacios y punto con un adulto.", "The sun is yellow. I have a blue pencil. We play in the park.", ["elige la palabra con sentido", "escribe la oración completa", "respeta el orden", "revisa mayúscula, espacios y punto"], ["el cuaderno"], ["elegir sin leer la oración", "olvidar el punto"], "Pide explicar por qué eligió cada palabra y corrige con calma."),
    "Escribe una oración con tu color favorito y la palabra «is».",
    "Inventa dos oraciones con espacios y un banco de tres palabras para que otra persona las complete.",
)

lesson(
    OA13, 3,
    "El modelo y los bancos de palabras escritos en cada ejercicio, lápiz y cuaderno.",
    "Aprenderé a cambiar una o dos palabras de un modelo para escribir una oración nueva. Sirve para escribir con mis propias ideas usando la estructura que ya conozco.",
    ["Sé copiar y completar oraciones.", "Sé palabras de colores, animales y objetos en inglés."],
    [
        "Un modelo se puede cambiar (change). Si el modelo dice «I have a blue pen», puedes cambiar blue por red y pen por book: «I have a red book». Cambiaste dos palabras y la estructura sigue igual. La estructura es la forma de la oración: I have a + color + objeto.",
        "Para cambiar un modelo, primero busca qué palabras puedes cambiar: los colores, los animales, las comidas, los números. Las palabras como I, have, a o is casi siempre se quedan. Cambia solo una o dos palabras a la vez y lee la oración nueva. ¿Tiene sentido? Si sí, escríbela.",
        "Cuidado con la palabra a. Antes de una palabra que empieza con vocal (a, e, i, o, u), como apple, egg u orange, se usa an: «an apple», «an egg». Antes de una que empieza con consonante se usa a: «a pen», «a dog». Hay unas pocas palabras especiales; aquí usamos solo ejemplos seguros. También cuida el plural: «I have two dogs», con s. Escribe la oración nueva con mayúscula, espacios y punto.",
    ],
    [("change", "cambiar"), ("structure", "estructura, forma de la oración"), ("a / an", "un, una"), ("blue pen", "bolígrafo azul"), ("two dogs", "dos perros"), ("new", "nuevo")],
    [
        ("Cambiar dos palabras", "Modelo: «I have a blue pen.» Cambia blue por red y pen por ball.", ["Mantengo I have a.", "Pongo red.", "Pongo ball."], "I have a red ball."),
        ("Usar an", "Modelo: «I have a dog.» Cambia dog por apple.", ["Apple empieza con vocal.", "Antes de vocal uso an.", "Escribo I have an apple."], "I have an apple."),
    ],
    [
        ("Escribir «a apple».", "No se mira si la palabra empieza con vocal.", "Antes de vocal se usa an: an apple."),
        ("Cambiar todas las palabras del modelo.", "Se pierde la estructura.", "Cambia solo las palabras de contenido."),
    ],
    [
        ("¿Qué significa «change»?", "Cambiar", "Es poner otra palabra."),
        ("¿Qué palabra usas antes de «apple»?", "an", "Apple empieza con vocal."),
        ("¿Qué palabra usas antes de «dog»?", "a", "Dog empieza con consonante."),
    ],
    [
        ("¿Qué palabras de un modelo conviene cambiar?", "Colores, animales, comidas o números", "Son palabras de contenido."),
        ("¿Qué palabras suelen mantenerse?", "I, have, a, is", "Forman la estructura."),
        ("¿Qué debes comprobar al cambiar una palabra?", "Que la oración tenga sentido", "Lo cambiado debe encajar."),
    ],
    [
        ("Modelo: «I have a red cat.» Cambia red por black. Escribe la oración.", "I have a black cat.", "Se cambia solo el color."),
        ("Modelo: «I like apples.» Cambia apples por bananas. Escribe la oración.", "I like bananas.", "Se cambia solo la comida."),
        ("Modelo: «The dog is big.» Cambia dog por cat y big por small.", "The cat is small.", "Se cambian dos palabras."),
    ],
    [
        ("Ema escribió «I have a egg». ¿Qué palabra debe cambiar?", "a por an", "Egg empieza con vocal."),
        ("Modelo: «I have two dogs.» Pedro cambia dogs por cats y escribe «I have two cat». ¿Qué le falta?", "La s de cats", "Con two se usa el plural."),
    ],
    [
        ("Modelo: «The sun is hot.» Cambia sun por ice y hot por cold.", "The ice is cold.", "El hielo es frío."),
        ("Modelo: «I have a pen.» Cambia pen por orange (naranja). Escribe la oración completa.", "I have an orange.", "Orange empieza con vocal."),
    ],
    [("Escribes una tarjeta para un amigo con el modelo «I like pizza.» ¿Cómo la cambias si te gustan las manzanas?", "I like apples.", "Se cambia solo la comida.")],
    [
        ("¿Cómo se dice «nuevo» en inglés?", "new", "Describe algo recién hecho."),
        ("Escribe «un huevo» en inglés con el artículo correcto.", "an egg", "Egg empieza con vocal."),
        ("Modelo: «I have a dog.» Cambia dog por fish.", "I have a fish.", "Se mantiene la estructura."),
    ],
    task("Con el modelo «I have a blue pen.», escribe tres oraciones nuevas en tu cuaderno cambiando una o dos palabras: (1) con otro color, (2) con otro objeto de la escuela (book, bag, ruler), (3) con an y un objeto como apple u orange. Luego lee las tres oraciones a un adulto y revisa mayúscula, espacios y punto.", "I have a red book. I have a green bag. I have an apple.", ["mantiene la estructura", "cambia una o dos palabras", "usa a o an correctamente", "revisa mayúscula, espacios y punto"], ["el cuaderno"], ["escribir a apple", "cambiar toda la oración"], "Lee con él las oraciones nuevas y celebra las que tienen sentido."),
    "Cambia el color del modelo «I have a blue pen.» tres veces.",
    "Escribe cinco oraciones nuevas a partir del modelo «I like apples.» cambiando la comida.",
)

lesson(
    OA13, 4,
    "El modelo y la lista de revisión escritos en cada ejercicio, lápiz, borrador y cuaderno.",
    "Aprenderé a escribir una oración o dos con un modelo y a revisarlas con una lista. Sirve para mejorar mi escritura en inglés antes de mostrarla.",
    ["Sé copiar, completar y cambiar un modelo.", "Sé usar mayúscula, espacios y punto."],
    [
        "Escribir y revisar (check) son dos partes de un mismo trabajo. Primero escribes con el modelo. Después revisas con una lista de cuatro preguntas: ¿empieza con mayúscula?, ¿hay espacios entre las palabras?, ¿termina con punto?, ¿las palabras se parecen a las del modelo y tienen sentido?",
        "Para revisar, lee tu oración en voz alta, señalando cada palabra con el dedo. Compara con el modelo letra por letra. Marca con un visto lo que está bien y subraya lo que debes corregir. Corregir un error no es malo: es una forma de aprender.",
        "Puedes escribir sobre temas conocidos o de otras asignaturas. En ciencias: «The plant needs water.» En matemática: «I have ten pencils.» En artes: «The picture is blue.» Usa un modelo, cambia las palabras necesarias y revisa antes de mostrar tu trabajo.",
    ],
    [("check", "revisar"), ("checklist", "lista de revisión"), ("correct", "corregir; correcto"), ("plant", "planta"), ("pencils", "lápices"), ("picture", "imagen, cuadro")],
    [
        ("Revisar una oración", "Oración: «the plant needs water». Modelo: «The plant needs water.» ¿Qué falta?", ["Miro la primera letra: falta la mayúscula.", "Miro el final: falta el punto.", "Los espacios están bien."], "Mayúscula en The y punto final"),
        ("Escribir con modelo", "Modelo: «I have ten pencils.» Escribe una oración nueva con cinco lápices.", ["Mantengo I have.", "Cinco es five.", "Termino con punto."], "I have five pencils."),
    ],
    [
        ("Entregar sin revisar.", "Se cree que escribir basta.", "Revisa con la lista antes de mostrar."),
        ("Borrar todo cuando hay un error.", "Se piensa que un error arruina el trabajo.", "Corrige solo la parte equivocada."),
    ],
    [
        ("¿Qué significa «check»?", "Revisar", "Es mirar con cuidado."),
        ("¿Cuántas cosas revisas en la lista de hoy?", "Cuatro", "Mayúscula, espacios, punto y sentido."),
        ("¿Qué significa «correct»?", "Corregir o correcto", "Se corrigen los errores."),
    ],
    [
        ("¿Por qué lees tu oración en voz alta al revisar?", "Para notar errores y ver cada palabra", "Oírla ayuda a encontrar problemas."),
        ("¿Qué haces con un error?", "Lo corrijo", "Corregir es parte de aprender."),
        ("¿Qué puedes usar para escribir sobre ciencias?", "Un modelo y las palabras del tema", "El modelo guía la estructura."),
    ],
    [
        ("Escribe con el modelo «I have ten pencils.» una oración con seis lápices.", "I have six pencils.", "Six es seis."),
        ("Revisa «the sun is yellow». Escríbela corregida.", "The sun is yellow.", "Se agrega mayúscula y punto."),
        ("Revisa «Wehave a ball.» Escríbela corregida.", "We have a ball.", "Falta el espacio."),
    ],
    [
        ("Ana dice que su oración está bien porque no la leyó otra vez. ¿Qué debe hacer?", "Revisarla con la lista", "Revisar descubre errores."),
        ("Lucas escribió «I have ten pencil.» ¿Qué corrige?", "Pencils con s", "Con ten se usa el plural."),
    ],
    [
        ("Escribe con el modelo «The plant needs water.» una oración sobre un gato y leche. Usa needs.", "The cat needs milk.", "Se cambian dos palabras."),
        ("Cuenta cuántos errores tiene «the cat is bigg» (mayúscula, ortografía y punto).", "3", "Falta mayúscula, sobra una g y falta el punto."),
    ],
    [("En ciencias escribes «the plant is green» y quieres entregarlo. Antes revisas con la lista. ¿Cómo queda?", "The plant is green.", "Se agrega mayúscula y punto.")],
    [
        ("¿Qué cuatro cosas revisas?", "Mayúscula, espacios, punto y sentido", "Son los pasos de la lista."),
        ("¿Cómo se dice «lápices» en inglés?", "pencils", "Es el plural de pencil."),
        ("¿Qué haces con el dedo al revisar?", "Señalo cada palabra", "Así no me salto ninguna."),
    ],
    task("Con el modelo «The plant needs water.» escribe dos oraciones nuevas: una sobre ciencias (por ejemplo «The dog needs food.») y una sobre tu escuela (por ejemplo «The class needs books.»). Revisa con la lista: mayúscula, espacios, punto y sentido. Marca con un visto cada punto y corrige lo que falte. Muestra el trabajo a un adulto.", "The dog needs food. The class needs books.", ["escribe dos oraciones con modelo", "revisa los cuatro puntos", "corrige al menos un error si lo hay", "mantiene la estructura"], ["el cuaderno con la lista marcada"], ["entregar sin revisar", "olvidar el punto"], "Pregunta qué corrigió y valora el cuidado."),
    "Revisa en voz alta una oración tuya con el dedo.",
    "Escribe dos oraciones con modelo sobre matemática, por ejemplo «I have five pencils.»",
)

# ================================================================ OA 14
lesson(
    OA14, 1,
    "Las descripciones de imágenes y los bancos de palabras escritos en cada ejercicio, lápiz y cuaderno.",
    "Aprenderé a escribir el nombre de animales, objetos, ocupaciones, partes de la casa, lugares y comida a partir de una imagen. Sirve para etiquetar y escribir oraciones simples sobre lo que veo.",
    ["Sé copiar y completar oraciones con modelo.", "Sé palabras como dog, apple y book.", "Sé usar a y an: a dog, an apple."],
    [
        "Una etiqueta (label) es una palabra escrita junto a una imagen para decir qué es. Por ejemplo, bajo la imagen de un perro escribes «dog». Con más palabras puedes escribir una oración: «It is a dog.» (es un perro). Para ocupaciones: «She is a teacher.» Para lugares de la casa: «This is the kitchen.»",
        "Estas son palabras que puedes usar. Animales: dog, cat, bird, fish. Objetos: book, chair, table, bag. Partes de la casa: kitchen (cocina), bedroom (dormitorio), bathroom (baño), door (puerta), window (ventana). Ocupaciones: teacher (profesora), doctor (médico), cook (cocinero), farmer (agricultor). Lugares: school, park, library. Comida: apple, bread, milk, rice.",
        "Para escribir sobre una imagen, sigue tres pasos: mira la imagen, elige la palabra del banco y escribe la etiqueta o la oración con mayúscula, espacios y punto. Antes de terminar, compara tu escritura con la imagen. Si el banco tiene palabras que no usas, está bien: no todas son para esta imagen.",
    ],
    [("label", "etiqueta"), ("kitchen", "cocina"), ("bedroom", "dormitorio"), ("teacher", "profesor/a"), ("farmer", "agricultor/a"), ("bread", "pan")],
    [
        ("Etiquetar un animal", "[Imagen: un perro.] Banco: dog, cat, bird. Escribe la etiqueta.", ["Miro la imagen: es un perro.", "Elijo dog.", "Escribo dog."], "dog"),
        ("Escribir una oración", "[Imagen: una mujer enseña en una sala.] Banco: teacher, doctor, cook. Escribe una oración con She is a.", ["Miro: enseña, es profesora.", "Elijo teacher.", "Escribo la oración completa."], "She is a teacher."),
    ],
    [
        ("Escribir una palabra que no corresponde a la imagen.", "No se mira bien la imagen.", "Mira la imagen y elige la palabra que coincide."),
        ("Escribir «She is teacher» sin a.", "Se olvida el artículo.", "Se escribe She is a teacher."),
    ],
    [
        ("¿Qué significa «label»?", "Etiqueta", "Es la palabra junto a una imagen."),
        ("¿Cómo se dice «cocina» (lugar de la casa) en inglés?", "kitchen", "Es el lugar donde se cocina."),
        ("¿Cómo se dice «profesora» en inglés?", "teacher", "Es la ocupación de quien enseña."),
    ],
    [
        ("¿Qué tres pasos sigues para escribir sobre una imagen?", "Miro la imagen, elijo la palabra y escribo", "Así la palabra coincide con la imagen."),
        ("¿Para qué sirve el banco de palabras?", "Para elegir la palabra correcta", "Ayuda con la ortografía."),
        ("¿Qué compruebas al final?", "Que la escritura coincida con la imagen", "La imagen es la prueba."),
    ],
    [
        ("[Imagen: un gato.] Banco: cat, dog, fish. Escribe la oración «It is a ___.»", "It is a cat.", "El banco tiene cat para la imagen."),
        ("[Imagen: un hombre con un tractor en un campo.] Banco: farmer, cook, doctor. Escribe «He is a ___.»", "He is a farmer.", "El tractor y el campo indican farmer."),
        ("[Imagen: una cama en una pieza.] Banco: kitchen, bedroom, bathroom. Escribe «This is the ___.»", "This is the bedroom.", "Una cama indica el dormitorio."),
    ],
    [
        ("[Imagen: una jarra de leche.] Una niña escribe «It is bread». ¿Qué debe cambiar?", "bread por milk", "La imagen muestra leche."),
        ("[Imagen: una mujer con delantal cocina.] Banco: teacher, cook. Un niño escribe «She is a teacher». ¿Es correcto?", "No; debe ser cook", "La mujer cocina."),
    ],
    [
        ("[Imagen: una manzana roja.] Completa con a o an: «It is ___ apple.» Escribe la oración completa.", "It is an apple.", "Apple empieza con vocal y lleva an."),
        ("[Imagen: una ventana.] Banco: window, door, table. Escribe una etiqueta.", "window", "La imagen muestra una ventana."),
    ],
    [("[Imagen: un niño frente a una escuela.] Quieres escribir el lugar. Banco: school, park, bed. Escribe «This is the ___.» completo.", "This is the school.", "La escuela es el lugar de la imagen.")],
    [
        ("¿Cómo se dice «dormitorio» en inglés?", "bedroom", "Es el lugar donde se duerme."),
        ("¿Cómo se dice «agricultor» en inglés?", "farmer", "Es quien trabaja en el campo."),
        ("¿Qué escribes bajo la imagen de un pan?", "bread", "Bread es pan."),
    ],
    task("En una hoja dibuja cuatro cosas: un animal, un objeto de la escuela, una parte de la casa y una comida. Bajo cada dibujo, escribe una etiqueta en inglés. Luego elige una y escribe una oración, por ejemplo «It is a dog.» Revisa mayúscula, espacios y punto.", "Dibujo de un perro: «dog». Oración: «It is a dog.»", ["cuatro etiquetas correctas", "una oración completa", "las palabras coinciden con las imágenes", "revisa mayúscula, espacios y punto"], ["la hoja con dibujos"], ["escribir palabras que no coinciden", "olvidar el punto"], "Pide leer las etiquetas en voz alta y celebra las que coinciden."),
    "Escribe etiquetas en inglés para tres objetos de tu pieza.",
    "Elige una ocupación y escribe una oración con He is a o She is a.",
)

lesson(
    OA14, 2,
    "Las descripciones de imágenes y los bancos de palabras escritos en cada ejercicio, lápiz y cuaderno.",
    "Aprenderé a escribir cómo se siente una persona y cuántas cosas hay, hasta veinte, mirando una imagen. Sirve para expresar sentimientos y cantidades por escrito en inglés.",
    ["Sé contar hasta veinte.", "Sé decir happy y sad."],
    [
        "Para escribir un sentimiento (feeling) usa «I am» o «He is» y una palabra: happy (contento), sad (triste), angry (enojado), scared (asustado), tired (cansado), surprised (sorprendido). Por ejemplo: «The girl is happy.» (la niña está contenta). Mira la cara de la imagen para elegir la palabra.",
        "Para escribir una cantidad usa «There are» y el número: «There are twelve apples.» (hay doce manzanas). Los números del once al veinte son: eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty. Si hay una sola, usa «There is one apple».",
        "Cuenta con atención antes de escribir: toca cada objeto una vez. Escribe el número con letras y no con cifras. Cuida la ortografía: fourteen lleva «four», pero forty (cuarenta) no. Nineteen termina en -teen, y twenty termina en -ty. Revisa con el banco de palabras.",
    ],
    [("angry", "enojado"), ("scared", "asustado"), ("tired", "cansado"), ("There are", "hay (varios)"), ("There is", "hay (uno)"), ("fourteen / nineteen", "catorce / diecinueve")],
    [
        ("Escribir un sentimiento", "[Imagen: un niño llorando.] Banco: happy, sad, angry. Escribe «The boy is ___.»", ["Miro la cara.", "Llorar indica tristeza.", "Elijo sad."], "The boy is sad."),
        ("Escribir una cantidad", "[Imagen: 12 manzanas.] Escribe una oración con There are y el número en inglés.", ["Cuento: son 12.", "Twelve es doce.", "Escribo There are twelve apples."], "There are twelve apples."),
    ],
    [
        ("Escribir el número con cifras: «There are 12 apples».", "No se usa la palabra del número.", "Escribe el número con letras: twelve."),
        ("Confundir fourteen con forty.", "Se parecen en el sonido.", "Fourteen es 14 y forty es 40."),
    ],
    [
        ("¿Qué significa «angry»?", "Enojado", "Es un sentimiento."),
        ("¿Cómo se escribe 15 en inglés?", "fifteen", "Es el número después de fourteen."),
        ("¿Qué significa «There are»?", "Hay (varios)", "Se usa para más de uno."),
    ],
    [
        ("¿Dónde miras para elegir el sentimiento?", "En la cara de la persona de la imagen", "La cara muestra cómo se siente."),
        ("¿Qué haces antes de escribir una cantidad?", "Cuento con atención", "Así el número es correcto."),
        ("¿Cuándo usas There is?", "Cuando hay una sola cosa", "Is es para uno."),
    ],
    [
        ("[Imagen: una niña sonriendo.] Banco: sad, happy, tired. Escribe «The girl is ___.»", "The girl is happy.", "Sonríe, está contenta."),
        ("[Imagen: 16 lápices.] Escribe el número en inglés: «There are ___ pencils.»", "There are sixteen pencils.", "Sixteen es dieciséis."),
        ("[Imagen: un niño bostezando.] Banco: tired, angry, happy. Escribe «He is ___.»", "He is tired.", "Bostezar indica cansancio."),
    ],
    [
        ("Un niño escribe «There are 20 books». ¿Cómo debe escribir el número?", "twenty", "Debe usar la palabra twenty."),
        ("[Imagen: un perro con ojos grandes ante un trueno.] Banco: scared, happy. ¿Qué sentimiento es?", "scared", "El trueno asusta."),
    ],
    [
        ("[Imagen: 18 estrellas.] Escribe la oración «There are ___ stars.» con el número.", "There are eighteen stars.", "Eighteen es dieciocho."),
        ("Cuenta ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● y escribe cuántos puntos hay en inglés.", "seventeen", "Son diecisiete puntos."),
    ],
    [("Mañana escribes una tarjeta sobre un niño que perdió su pelota: [Imagen: un niño con la cara triste]. Escribe una oración con The boy is.", "The boy is sad.", "La cara triste indica sad.")],
    [
        ("¿Cómo se dice «cansado» en inglés?", "tired", "Es la palabra de cansancio."),
        ("¿Cómo se escribe 19 en inglés?", "nineteen", "Termina en -teen."),
        ("¿Qué significa «scared»?", "Asustado", "Es un sentimiento."),
    ],
    task("Mira tu cara en un espejo con cuatro sentimientos: happy, sad, angry, scared. Dibuja una cara para cada uno y escribe «I am ___.» bajo cada una. Luego dibuja 15 puntos y escribe «There are fifteen dots.» Revisa mayúscula, espacios y punto.", "Cara contenta: «I am happy.» Quince puntos: «There are fifteen dots.»", ["cuatro caras con sentimiento distinto", "oraciones con I am", "cantidad con el número en inglés", "revisa mayúscula, espacios y punto"], ["la hoja con caras"], ["escribir el número con cifras", "elegir un sentimiento que no coincide"], "Valora que la palabra coincida con la cara."),
    "Escribe I am happy y I am tired en tu cuaderno.",
    "Dibuja entre 11 y 20 objetos y escribe cuántos hay en inglés.",
)

lesson(
    OA14, 3,
    "Las descripciones de imágenes y los bancos de palabras escritos en cada ejercicio, lápiz y cuaderno.",
    "Aprenderé a escribir dónde está un objeto a partir de una imagen. Sirve para describir ubicaciones con palabras de lugar.",
    ["Sé in, on y under.", "Sé nombres de objetos y partes de la casa."],
    [
        "Para escribir dónde está algo usa «is» y una palabra de lugar: «The cat is on the bed.» (el gato está sobre la cama). Las palabras de lugar son: in (dentro de), on (sobre), under (debajo de), next to (al lado de), behind (detrás de) y in front of (delante de).",
        "Mira la imagen con cuidado. ¿Dónde está el objeto respecto a otro? Si el gato está encima de la cama, escribes on. Si está debajo, under. Si está dentro de una caja, in. Si hay dos objetos juntos, next to. Después escribe: «The ___ is ___ the ___.»",
        "Para varias cosas usa «are»: «The books are on the table.» Cuida los espacios y escribe the con minúscula en medio de la oración. Al final revisa con la imagen: ¿la palabra de lugar coincide con lo que ves?",
    ],
    [("in", "dentro de"), ("on", "sobre"), ("under", "debajo de"), ("next to", "al lado de"), ("behind", "detrás de"), ("in front of", "delante de")],
    [
        ("Escribir ubicación", "[Imagen: un gato sobre una cama.] Escribe dónde está el gato.", ["Gato y cama.", "Está encima: on.", "Escribo la oración."], "The cat is on the bed."),
        ("Cambiar la palabra de lugar", "[Imagen: una pelota debajo de la mesa.] Escribe la oración.", ["Pelota y mesa.", "Debajo es under.", "Escribo la oración."], "The ball is under the table."),
    ],
    [
        ("Escribir on cuando el objeto está dentro.", "Se confunden las palabras de lugar.", "Dentro es in; sobre es on."),
        ("Olvidar is o are.", "Se escribe sin verbo.", "Escribe is o are antes del lugar."),
    ],
    [
        ("¿Qué significa «behind»?", "Detrás de", "Indica la parte de atrás."),
        ("¿Qué significa «next to»?", "Al lado de", "Dos cosas están juntas."),
        ("¿Qué palabra usas para algo dentro de una caja?", "in", "In es dentro."),
    ],
    [
        ("¿Qué miras en la imagen para elegir la palabra de lugar?", "Dónde está el objeto respecto al otro", "La posición determina la palabra."),
        ("¿Cuándo usas are?", "Cuando hay varias cosas", "Are acompaña al plural."),
        ("¿Qué compruebas al final?", "Que la palabra de lugar coincida con la imagen", "La imagen confirma."),
    ],
    [
        ("[Imagen: un libro sobre una silla.] Escribe «The book is ___ the chair.»", "The book is on the chair.", "Sobre se escribe on."),
        ("[Imagen: un pájaro dentro de una jaula.] Escribe «The bird is ___ the cage.»", "The bird is in the cage.", "Dentro de es in."),
        ("[Imagen: un perro al lado de una casa.] Escribe «The dog is ___ the house.»", "The dog is next to the house.", "Al lado de es next to."),
    ],
    [
        ("[Imagen: dos libros sobre la mesa.] Un niño escribe «The books is on the table». ¿Qué corrige?", "is por are", "Hay dos libros, plural."),
        ("[Imagen: una pelota detrás de un árbol.] Tomás escribe «in front of». ¿Qué debe escribir?", "behind", "La pelota está detrás."),
    ],
    [
        ("[Imagen: un gato debajo de la silla.] Escribe la oración completa con The cat is.", "The cat is under the chair.", "Under es debajo de."),
        ("[Imagen: un niño delante de la puerta.] Escribe «The boy is ___ the door.»", "The boy is in front of the door.", "Delante de es in front of."),
    ],
    [("Mamá pregunta por tu mochila. La ves sobre el sofá. Escribe la oración en una nota.", "The bag is on the sofa.", "Sobre se escribe on.")],
    [
        ("¿Cómo se dice «debajo de» en inglés?", "under", "Es la palabra para abajo."),
        ("¿Cómo se dice «delante de» en inglés?", "in front of", "Son tres palabras."),
        ("Completa con is o are: «The pencils ___ in the box.»", "are", "Pencils es plural."),
    ],
    task("Mira tu pieza o sala y elige cuatro objetos. Escribe una oración para cada uno con una palabra de lugar distinta: on, in, under, next to. Por ejemplo, «The pencil is on the table.» Dibuja cada ubicación con una flecha. Revisa con un adulto mayúscula, espacios y punto.", "The pencil is on the table. The book is in the bag. The shoe is under the bed. The lamp is next to the bed.", ["escribe cuatro oraciones", "usa cuatro palabras de lugar distintas", "usa is o are", "revisa la ortografía"], ["la hoja con dibujos"], ["confundir in y on", "olvidar is"], "Pide mostrar cada objeto y comprueba que la palabra de lugar coincida."),
    "Escribe una oración con la palabra on y otra con under.",
    "Dibuja una escena con cinco objetos y escribe cinco oraciones de lugar.",
)

lesson(
    OA14, 4,
    "Las descripciones de imágenes y los bancos de palabras escritos en cada ejercicio, lápiz y cuaderno.",
    "Aprenderé a escribir lo que alguien hace en este momento a partir de una imagen. Sirve para describir acciones con is o are y un verbo terminado en -ing.",
    ["Sé verbos como run, read y eat.", "Sé decir He is y She is."],
    [
        "Para escribir lo que pasa ahora, usa «is» o «are» y un verbo con -ing. «The boy is running.» (el niño está corriendo). «The girls are reading.» (las niñas están leyendo). «I am drawing.» (estoy dibujando). El verbo con -ing dice que la acción está pasando ahora.",
        "Mira la imagen y responde dos preguntas: ¿quién es? y ¿qué hace? Después elige el verbo del banco, agrega -ing y escribe. Algunos verbos cambian: run se escribe running, swim se escribe swimming, sit se escribe sitting, write se escribe writing y make se escribe making.",
        "Para una persona usa is. Para varias usa are. Para ti usa am o I'm, y con you usa are. Escribe con mayúscula al comienzo, deja espacios y termina con punto. Revisa que la acción sea la que muestra la imagen.",
    ],
    [("is / are", "está / están"), ("running", "corriendo"), ("reading", "leyendo"), ("eating", "comiendo"), ("swimming", "nadando"), ("writing", "escribiendo")],
    [
        ("Escribir una acción", "[Imagen: un niño corre.] Banco: run, read. Escribe la oración.", ["Miro: corre.", "Run se escribe running.", "Uso is porque es uno."], "The boy is running."),
        ("Acción de varios", "[Imagen: dos niñas leen.] Escribe la oración con They.", ["Son varias.", "Uso are.", "Read más ing es reading."], "They are reading."),
    ],
    [
        ("Escribir «The boy runing».", "No se duplica la n ni se pone is.", "Se escribe The boy is running."),
        ("Usar is con they.", "No se cambia el verbo.", "Con they se usa are."),
    ],
    [
        ("¿Qué significa «eating»?", "Comiendo", "Eat más ing."),
        ("¿Qué significa «swimming»?", "Nadando", "Swim más ing."),
        ("¿Qué terminación indica acción ahora?", "-ing", "Se agrega al final del verbo."),
    ],
    [
        ("¿Qué dos palabras van antes del verbo con -ing?", "is o are", "Son los verbos auxiliares."),
        ("¿Cuándo usas are?", "Con varias personas", "Are acompaña al plural."),
        ("¿Cómo se escribe run con -ing?", "running", "Se duplica la n."),
    ],
    [
        ("[Imagen: una niña come una manzana.] Banco: eat, drink. Escribe «She is ___ an apple.»", "She is eating an apple.", "Eat más ing es eating."),
        ("[Imagen: tres niños nadan.] Escribe «They ___ swimming.»", "They are swimming.", "Con they se usa are."),
        ("[Imagen: un gato duerme.] Escribe «The cat is ___.»", "The cat is sleeping.", "Sleep más ing es sleeping."),
    ],
    [
        ("Un niño escribe «The girl reading». ¿Qué palabra falta?", "is", "Se necesita is antes del verbo con -ing."),
        ("[Imagen: dos perros corren.] Ema escribe «The dogs is running». ¿Qué corrige?", "is por are", "Hay dos perros."),
    ],
    [
        ("[Imagen: un niño escribe una carta.] Escribe la oración con He is.", "He is writing a letter.", "Write pierde la e y recibe ing."),
        ("[Imagen: una niña sentada en una silla.] Escribe la oración con She is.", "She is sitting on a chair.", "Sit duplica la t."),
    ],
    [("Mandas un mensaje a tu abuela con una foto de tu hermano que juega a la pelota. Escribe la oración «My brother is ___ with a ball.» con play.", "My brother is playing with a ball.", "Play más ing es playing.")],
    [
        ("¿Cómo se dice «bebiendo» en inglés?", "drinking", "Drink más ing."),
        ("¿Cómo se dice «saltando» en inglés?", "jumping", "Jump más ing."),
        ("¿Qué verbo auxiliar usas con you?", "are", "Con you se usa are."),
    ],
    task("Elige tres personas de tu familia o tres personajes y dibuja lo que hacen ahora. Debajo de cada dibujo escribe una oración, por ejemplo «She is reading.», «He is eating.» y «They are playing.» Revisa que lleven is o are, el verbo con -ing, la mayúscula y el punto.", "She is reading. He is eating. They are playing.", ["tres oraciones", "usa is o are", "usa el verbo con -ing", "la acción coincide con el dibujo"], ["la hoja"], ["olvidar is", "escribir runing"], "Pide leer las oraciones y comparar con cada dibujo."),
    "Escribe I'm writing para lo que haces ahora.",
    "Dibuja cinco acciones y escribe una oración para cada una.",
)

lesson(
    OA14, 5,
    "Las descripciones de imágenes, el modelo de tarjeta y los bancos de palabras escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir una tarjeta de información breve juntando lo aprendido: identificar, describir, cantidad, ubicación y acción. Sirve para presentar un tema con varias oraciones simples.",
    ["Sé etiquetar, escribir sentimientos, cantidades, lugares y acciones.", "Sé revisar mayúscula, espacios y punto."],
    [
        "Una tarjeta de información (information card) tiene un título y tres o cuatro oraciones sobre una imagen. Por ejemplo, para un perro: «My dog. It is a dog. It is brown. It is under the table. It is sleeping.» Cada oración dice algo distinto: qué es, cómo es, dónde está y qué hace.",
        "Para escribir tu tarjeta usa lo aprendido. Identificar: «It is a dog.» Describir: «It is big.» Cantidad: «I have two dogs.» Lugar: «It is on the sofa.» Acción: «It is sleeping.» Sentimiento: «It is happy.» Elige las que coinciden con la imagen y escríbelas en orden.",
        "Antes de terminar, revisa la tarjeta con la lista: mayúscula, espacios, punto y que la información coincida con la imagen. Puedes dibujar la imagen en la tarjeta o dejar un espacio. No escribas datos privados: nada de dirección ni teléfono. Muestra la tarjeta a un adulto y léela en voz alta.",
    ],
    [("information card", "tarjeta de información"), ("title", "título"), ("It is a...", "es un..."), ("It is on...", "está sobre..."), ("It is sleeping", "está durmiendo"), ("happy", "contento")],
    [
        ("Armar una tarjeta", "[Imagen: un gato negro durmiendo sobre un sofá.] Escribe cuatro oraciones: qué es, cómo es, dónde está y qué hace.", ["It is a cat.", "It is black.", "Dónde: on the sofa. Qué hace: sleeping."], "It is a cat. It is black. It is on the sofa. It is sleeping."),
        ("Revisar la tarjeta", "Una tarjeta dice «my dog. it is brown it is big.» ¿Qué corriges?", ["Mayúscula en My e It.", "Punto después de brown.", "Punto al final."], "My dog. It is brown. It is big."),
    ],
    [
        ("Escribir datos que la imagen no muestra.", "Se inventa sin mirar.", "Escribe solo lo que se ve en la imagen."),
        ("Poner datos privados en la tarjeta.", "Se piensa que hay que dar todo.", "Usa solo información segura."),
    ],
    [
        ("¿Qué es una tarjeta de información?", "Un título y algunas oraciones sobre una imagen", "Reúne información en pocas oraciones."),
        ("¿Qué significa «It is sleeping»?", "Está durmiendo", "Sleeping es durmiendo."),
        ("¿Qué compruebas al final?", "Mayúscula, espacios, punto e información correcta", "Así queda clara."),
    ],
    [
        ("¿Qué tipos de información puedes poner en una tarjeta?", "Qué es, cómo es, cuántos hay, dónde está y qué hace", "Combina las funciones aprendidas."),
        ("¿Por qué debes escribir solo lo que ves en la imagen?", "Porque la tarjeta debe coincidir con la imagen", "La imagen es la fuente."),
        ("¿Qué datos no incluyes?", "Dirección y teléfono", "Son datos privados."),
    ],
    [
        ("[Imagen: un pájaro azul en un árbol.] Escribe «It is a ___ bird.» con el color.", "It is a blue bird.", "Blue es azul."),
        ("[Imagen: tres peces en una pecera.] Escribe «There are ___ fish.» con el número en inglés.", "There are three fish.", "Three es tres."),
        ("[Imagen: una niña lee un libro.] Escribe la oración con She is.", "She is reading a book.", "Read más ing es reading."),
    ],
    [
        ("Una tarjeta sobre un perro dice «It is a cat». ¿Qué está mal?", "El animal: debe decir dog", "La imagen muestra un perro."),
        ("Ana escribe tres oraciones seguidas sin puntos. ¿Qué falta?", "Un punto al final de cada oración", "Cada oración termina con punto."),
    ],
    [
        ("[Imagen: un niño feliz con una pelota roja bajo la mesa.] Escribe con He is el sentimiento del niño: «He is ___.»", "He is happy.", "Happy es contento."),
        ("[Imagen: una pelota roja bajo la mesa.] Escribe la oración «The ball is ___ the table.» con la palabra de lugar.", "The ball is under the table.", "Under es debajo de."),
    ],
    [("Preparas una tarjeta para tu clase sobre un conejo: [Imagen: un conejo blanco que come una zanahoria]. Escribe dos oraciones: qué es y qué hace. Usa banco: rabbit, carrot, eating.", "It is a rabbit. It is eating a carrot.", "Se escribe qué es y qué hace.")],
    [
        ("¿Cómo se dice «tarjeta» en inglés?", "card", "Es una hoja pequeña con información."),
        ("¿Cómo se dice «título» en inglés?", "title", "Es el nombre de la tarjeta."),
        ("¿Qué revisas con la lista de revisión?", "Mayúscula, espacios, punto y sentido", "Son cuatro puntos."),
    ],
    task("Elige un animal o personaje que conozcas y dibújalo. Escribe una tarjeta de información con título y cuatro oraciones: qué es, cómo es, dónde está y qué hace. Por ejemplo: «My cat. It is a cat. It is black. It is on the sofa. It is sleeping.» Revisa con la lista y léela a un adulto.", "My cat. It is a cat. It is black. It is on the sofa. It is sleeping.", ["título y cuatro oraciones", "la información coincide con el dibujo", "usa is, palabras de lugar y -ing", "revisa mayúscula, espacios y punto"], ["la tarjeta"], ["no usar punto", "datos que el dibujo no muestra"], "Pregunta qué parte de la tarjeta fue la más fácil y felicítalo por revisar."),
    "Dibuja un animal y escribe una oración que diga cómo es.",
    "Haz otra tarjeta con una comida y una ocupación, con tres oraciones cada una.",
)
