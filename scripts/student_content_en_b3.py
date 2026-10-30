"""Student material for 1.º básico Inglés (propuesta), EN01 OA 12 (comunicación oral con apoyo para funciones conocidas)."""
from __future__ import annotations

from student_lessons import ex, register

OA12 = "EN01 OA 12"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def T(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


register(
    OA12, 1,
    materials="Tarjetas de preguntas escritas en este cuaderno, lápiz y un adulto para conversar. Para practicar usa nombres inventados si quieres.",
    use="Aprenderé a decir mi nombre, mi edad y lo que me gusta en inglés, y a decidir qué datos no debo compartir. Sirve para presentarme de forma segura.",
    prior=["Sé decir Hello.", "Sé contar hasta diez."],
    explain=[
        "Para compartir información personal usamos frases cortas. I am Ana significa yo soy Ana. I am six significa tengo seis años: en inglés se dice yo soy seis. También puedes decir I like red (me gusta el rojo) para contar un gusto. Dos preguntas que oirás: What is your name? (¿cómo te llamas?) y How old are you? (¿cuántos años tienes?).",
        "No todos los datos se comparten. Tu dirección, tu número de teléfono y tu apellido completo son privados: no los digas a personas que no conoces. Si te los piden, por ejemplo con Where do you live? (¿dónde vives?) o What is your phone number? (¿cuál es tu número de teléfono?), puedes decir No, thank you (no, gracias) y avisar a un adulto.",
        "Practica con datos simples: un nombre (puede ser inventado), una edad y un gusto. Por ejemplo: I am Ana. I am six. I like red. Escucha la pregunta, responde con una frase corta y mira a la persona. Así hablas con seguridad.",
    ],
    vocab=[("I am", "yo soy / yo tengo (con la edad)"), ("six", "seis"), ("seven", "siete"), ("I like", "me gusta"), ("No, thank you", "no, gracias"), ("private", "privado: no se comparte")],
    worked=[
        W("Decir mi nombre y edad", "Te llamas Tom y tienes siete años. ¿Qué dices en inglés?",
          ["Digo mi nombre con I am: I am Tom.", "Digo mi edad con I am: I am seven.", "Junto las dos frases."],
          "I am Tom. I am seven."),
        W("Decidir qué compartir", "Un desconocido pregunta: What is your phone number? ¿Qué haces?",
          ["Pienso: el teléfono es un dato privado.", "Digo No, thank you.", "Aviso a un adulto de confianza."],
          "No, thank you, y aviso a un adulto."),
    ],
    mistakes=[
        M("Decir I have six para la edad.", "En español se dice tengo seis.", "En inglés se usa I am six."),
        M("Compartir la dirección con cualquiera.", "No se piensa en la seguridad.", "Los datos privados no se comparten; di No, thank you."),
    ],
    tiers=T(
        [ex("¿Qué significa I am Ana?", "Yo soy Ana", "I am es yo soy."),
         ex("¿Cómo se dice seis en inglés?", "six", "Six es seis."),
         ex("¿Qué significa I like red?", "Me gusta el rojo", "Like es gustar y red es rojo.")],
        [ex("¿Se puede compartir la dirección de mi casa con alguien que no conozco?", "No", "Es un dato privado."),
         ex("¿Qué dices si te piden un dato privado?", "No, thank you", "Es una forma amable de decir no."),
         ex("¿Qué verbo se usa en inglés para decir la edad: am o have?", "am", "Se dice I am seven.")],
        [ex("Eres Pia y tienes siete años. Escribe en inglés tu nombre y tu edad.", "I am Pia. I am seven.", "Se usa I am para las dos."),
         ex("Te gusta el color verde. Escribe la frase en inglés.", "I like green", "Like es gustar y green es verde."),
         ex("Tienes seis años. Completa: I am ___. Opciones: six o sit.", "six", "Six es seis años.")],
        [ex("Un niño dice I have seven para su edad. ¿Qué error hay?", "Debe decir I am seven", "En inglés la edad se dice con am."),
         ex("¿Por qué no hay que decir el teléfono a un desconocido?", "Porque es un dato privado y puede ser peligroso", "La privacidad protege a las personas.")],
        [ex("Un adulto lee la pregunta: What is your name? How old are you? Escribe una respuesta con los datos Lia y seis años.", "I am Lia. I am six.", "Se responde nombre y edad."),
         ex("Te preguntan: Where do you live? Escribe tu respuesta segura en inglés.", "No, thank you", "Es la respuesta cortés para un dato privado.")],
    ),
    context=[ex("En una fiesta, una persona nueva te pregunta cuántos años tienes. Tienes siete. Responde en inglés.", "I am seven", "Se usa I am con la edad.")],
    selfcheck=[ex("¿Cómo dices tu nombre en inglés?", "I am y tu nombre", "I am Tom, por ejemplo."),
               ex("¿Qué dato es privado: nombre de mi mascota o mi dirección?", "Mi dirección", "La dirección permite ubicar mi casa."),
               ex("¿Cómo dices me gusta el azul?", "I like blue", "Like es gustar y blue es azul.")],
    open_task=task("Con un adulto, completa este modelo con datos inventados o tuyos si quieres: I am ___. I am ___. I like ___. Después responde No, thank you cuando el adulto te pregunte tu teléfono. Escribe tus tres frases.",
                   "I am Lia. I am six. I like yellow. Cuando mi mamá preguntó el teléfono, dije No, thank you.",
                   ["dice nombre, edad y gusto", "usa I am para la edad", "rechaza dato privado"], ["tres frases escritas", "demostración oral"], ["I have para la edad", "compartir datos privados"],
                   "Celebra la frase completa. Recuerda con calma qué datos no se comparten."),
    reinforce="Repite I am y tu nombre frente a un espejo.",
    extend="Escribe tres gustos tuyos con I like y léelos a un adulto.",
)

register(
    OA12, 2,
    materials="La lista de números del 1 al 20 y las frases están escritas en este cuaderno. Necesitas lápiz y un adulto.",
    use="Aprenderé a decir lo que puedo hacer y a contar objetos hasta veinte en inglés. Sirve para hablar de mis habilidades y cantidades.",
    prior=["Sé contar hasta veinte en español.", "Sé decir I like."],
    explain=[
        "Para decir lo que puedes hacer, usa I can (yo puedo) más un verbo: I can run (puedo correr), I can swim (puedo nadar), I can jump (puedo saltar). Si no puedes, dices I cannot: I cannot swim (no puedo nadar).",
        "Para contar hasta veinte en inglés: one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty. Para decir cantidades usa I have (yo tengo) y el número: I have twelve pencils.",
        "Fíjate: cuando hay más de uno, la palabra suele terminar en s: pencil, pencils. Practica con objetos de tu casa: cuenta tus lápices, tus fichas o tus libros, y di el número en inglés.",
    ],
    vocab=[("I can", "yo puedo"), ("run / swim / jump", "correr / nadar / saltar"), ("I have", "yo tengo"), ("eleven", "once"), ("twelve", "doce"), ("twenty", "veinte")],
    worked=[
        W("Decir lo que puedo hacer", "Sabes saltar pero no nadar. ¿Qué dices?",
          ["Para lo que sí puedo: I can jump.", "Para lo que no puedo: I cannot swim.", "Junto las frases."],
          "I can jump. I cannot swim."),
        W("Contar con número en inglés", "Tienes 12 lápices. ¿Qué dices?",
          ["Cuento hasta doce: one, two, ... twelve.", "Uso I have.", "Escribo el número con letras y la palabra en plural."],
          "I have twelve pencils."),
    ],
    mistakes=[
        M("Decir I can to run.", "Se copia la estructura del español.", "Después de can va el verbo solo: I can run."),
        M("Confundir thirteen con thirty.", "Los números suenan parecidos.", "Thirteen es trece; thirty es treinta."),
    ],
    tiers=T(
        [ex("¿Qué significa I can swim?", "Puedo nadar", "Swim es nadar y can es poder."),
         ex("¿Cómo se dice doce en inglés?", "twelve", "Twelve es doce."),
         ex("¿Cómo se dice veinte en inglés?", "twenty", "Twenty es veinte.")],
        [ex("¿Cuál va después de can: run o to run?", "run", "El verbo va solo después de can."),
         ex("¿Qué significa I cannot jump?", "No puedo saltar", "Cannot es no poder."),
         ex("¿Cuál es mayor: fifteen o eleven?", "fifteen", "Quince es mayor que once.")],
        [ex("Puedes correr. Escribe la frase en inglés.", "I can run", "Can más el verbo run."),
         ex("Escribe en inglés: Tengo catorce libros. (catorce = fourteen)", "I have fourteen books", "I have más el número y books."),
         ex("Los números son seventeen, eighteen y nineteen. ¿Cuál de ellos es 18?", "eighteen", "Eighteen es dieciocho.")],
        [ex("Pedro escribió I can to swim. ¿Qué error hay?", "Sobra to", "Después de can va el verbo directo."),
         ex("Una niña dice I have thirty books pero tiene trece. ¿Qué número debió decir?", "thirteen", "Thirteen es trece.")],
        [ex("Un adulto lee: I have sixteen red balls. Escribe cuántas pelotas rojas tiene (con cifras).", "16", "Sixteen es dieciséis."),
         ex("Sabes contar hasta 20. Completa la frase en inglés: I can count to ___. Escribe el número con letras.", "twenty", "Twenty es veinte.")],
    ),
    context=[ex("En la plaza un niño te pregunta qué puedes hacer. Sabes correr y saltar. Responde con dos frases en inglés.", "I can run. I can jump.", "Can más el verbo se usa para habilidades.")],
    selfcheck=[ex("¿Cómo se dice puedo saltar?", "I can jump", "Jump es saltar."),
               ex("¿Cómo se dice trece?", "thirteen", "Thirteen es trece."),
               ex("¿Qué significa I have?", "Yo tengo", "Have es tener.")],
    open_task=task("Con un adulto, completa estas frases con lo que es verdad para ti: I can ___ (run, jump o swim). I cannot ___ (elige otro verbo). I have ___ pencils o crayons (crayons = lápices de cera; cuéntalos y di el número en inglés). Dibuja los objetos que contaste.",
                   "I can jump. I cannot swim. I have twelve crayons. Dibujé doce lápices de cera.",
                   ["usa can y cannot", "usa el verbo sin to", "dice un número bien"], ["tres frases escritas", "dibujo de los objetos"], ["I can to", "confundir thirteen y thirty"],
                   "Celebra la cantidad correcta. Ayuda a repetir el número si se confunde."),
    reinforce="Cuenta en inglés hasta veinte mientras subes una escalera o das pasos.",
    extend="Averigua cuántas cosas distintas tienes en tu pieza y di I have ___.",
)

register(
    OA12, 3,
    materials="Imágenes descritas y oraciones escritas en este cuaderno, lápiz y un adulto.",
    use="Aprenderé a identificar y describir animales, comida, ocupaciones y lugares de la escuela. Sirve para decir lo que veo con frases simples.",
    prior=["Conozco animales y colores en inglés.", "Sé decir It is."],
    explain=[
        "Para identificar algo usamos It is a ___ (es un ___) o This is a ___. Con animales: It is a dog (es un perro). Con comida: It is an apple (es una manzana). Si la palabra empieza con vocal se usa an: an apple, an elephant.",
        "Para ocupaciones se dice He is a teacher (él es profesor), She is a doctor (ella es doctora) o I am a cook (yo soy cocinero). Para lugares de la escuela: library (biblioteca), classroom (sala), playground (patio) y gym (gimnasio).",
        "Para describir, agrega un color o un tamaño: It is a big red apple (es una manzana grande y roja). Primero va el tamaño y después el color. Practica con imágenes y habla despacio, con ayuda del adulto.",
    ],
    vocab=[("dog / cat", "perro / gato"), ("apple / banana", "manzana / plátano"), ("teacher", "profesor/a"), ("doctor", "doctor/a"), ("library", "biblioteca"), ("playground", "patio de juegos")],
    worked=[
        W("Identificar un animal", "Ves un animal con orejas largas, que hace guau. ¿Qué dices?",
          ["Pienso: es un perro.", "Uso It is a.", "Digo la palabra dog."],
          "It is a dog."),
        W("Elegir a o an", "Quieres decir que es una manzana roja. ¿Usas a o an?",
          ["Apple empieza con la vocal a.", "Con vocal se usa el artículo an.", "Digo an apple."],
          "It is an apple. It is red."),
    ],
    mistakes=[
        M("Decir a apple.", "Se usa siempre a.", "Si empieza con vocal, usa an."),
        M("Confundir teacher con doctor.", "Suenan raro al principio.", "Usa el dibujo: teacher enseña, doctor cura."),
    ],
    tiers=T(
        [ex("¿Qué significa dog?", "Perro", "Dog es perro."),
         ex("¿Qué significa library?", "Biblioteca", "Library es biblioteca."),
         ex("¿Cómo se dice profesor/a en inglés?", "teacher", "Teacher enseña en la escuela.")],
        [ex("¿Qué se dice con apple: a o an?", "an", "Apple empieza con vocal."),
         ex("¿Qué frase se usa para identificar un animal: It is a ___ o I can ___?", "It is a ___", "Se usa para decir qué es algo."),
         ex("¿Dónde juegas en el recreo: playground o library?", "playground", "Playground es patio de juegos.")],
        [ex("Ves una banana amarilla. Escribe en inglés: es una banana.", "It is a banana", "Banana empieza con consonante: a."),
         ex("Tu tía es doctora. Escribe en inglés: ella es doctora.", "She is a doctor", "She is a más la ocupación; doctor sirve para doctor y doctora."),
         ex("Estás en el lugar de la escuela donde hay muchos libros para leer y pedir prestados. Escribe en inglés: es la biblioteca.", "It is the library", "Library es biblioteca.")],
        [ex("Ana dice It is a elephant. ¿Qué error hay?", "Debe decir an elephant", "Elephant empieza con vocal."),
         ex("Pedro dice He is a dog para su amigo profesor. ¿Qué cambiaría?", "dog por teacher", "Teacher es profesor.")],
        [ex("Un adulto lee: She is a cook. It is a big red apple. ¿Qué ocupación se nombra?", "cook (cocinera)", "Cook es cocinero o cocinera."),
         ex("Escribe una oración con tamaño y color: una pelota grande y verde.", "It is a big green ball", "Primero tamaño y luego color.")],
    ),
    context=[ex("En la escuela, un niño nuevo pregunta qué es el lugar donde se leen libros. Respóndele en inglés.", "It is the library", "Library es biblioteca.")],
    selfcheck=[ex("¿Cómo se dice manzana?", "apple", "Apple es manzana."),
               ex("¿Cómo se dice patio de juegos?", "playground", "Es el lugar de recreo."),
               ex("¿Cómo dices que ella es doctora?", "She is a doctor", "She is a más la ocupación.")],
    open_task=task("Mira estas cuatro cosas: un gato, una banana, un profesor, la biblioteca. Para cada una escribe una oración en inglés: It is a cat. It is a banana. He is a teacher. It is the library. Después dibuja una de las cuatro.",
                   "It is a cat. It is a banana. He is a teacher. It is the library. Dibujé al gato.",
                   ["usa a o an bien", "usa It is o He is", "dibujo coincide"], ["cuatro oraciones", "un dibujo"], ["a apple", "confundir he y it"],
                   "Pide que lea cada oración señalando su dibujo. Celebra los aciertos."),
    reinforce="Nombra cinco animales o comidas de tu casa con It is a o It is an.",
    extend="Escribe tres oraciones sobre ocupaciones de personas que conozcas con ayuda de un adulto.",
)

register(
    OA12, 4,
    materials="Frases de prohibición y petición escritas en este cuaderno, un adulto para practicar y lápiz.",
    use="Aprenderé a decir lo que no se debe hacer y a pedir comida en inglés. Sirve para cuidar normas y pedir con respeto.",
    prior=["Conozco run, eat y shout.", "Conozco please y thank you."],
    explain=[
        "Para decir que algo no se debe hacer, se usa Don't + verbo: Don't run (no corras), Don't shout (no grites), Don't eat here (no comas aquí). El verbo va al lado de Don't, sin cambios. Y se dice con un tono firme pero amable.",
        "Para pedir comida usamos Can I have ___, please? (¿puedo tener ___, por favor?). Por ejemplo: Can I have an apple, please? Quien da responde Here you are (aquí tienes) y tú dices Thank you. Para preguntar si hay algo, se dice Do you have ___? (¿tienes ___?).",
        "Recuerda ser amable: usa please y thank you. Con la prohibición no hace falta enojarse: Don't run, please. Practica con un adulto: uno prohíbe y otro pide, y cambien de papel.",
    ],
    vocab=[("Don't run", "no corras"), ("Don't shout", "no grites"), ("Can I have...?", "¿puedo tener...?"), ("Here you are", "aquí tienes"), ("Do you have...?", "¿tienes...?"), ("please", "por favor")],
    worked=[
        W("Decir una prohibición", "En la biblioteca los niños gritan. ¿Qué dices?",
          ["Pienso en la acción que no se debe hacer: gritar.", "Uso Don't + shout.", "Agrego please para ser amable."],
          "Don't shout, please."),
        W("Pedir comida", "Quieres una manzana. ¿Qué dices y cómo respondes si te la dan?",
          ["Pido con Can I have.", "Agrego please.", "Al recibirla, digo Thank you."],
          "Can I have an apple, please? ... Thank you."),
    ],
    mistakes=[
        M("Decir Don't to run.", "Se copia la estructura del español.", "Después de Don't va el verbo solo: Don't run."),
        M("Pedir sin please.", "Se habla rápido.", "Agrega please para pedir con respeto."),
    ],
    tiers=T(
        [ex("¿Qué significa Don't run?", "No corras", "Don't es no y run es correr."),
         ex("¿Qué significa Here you are?", "Aquí tienes", "Se dice al entregar algo."),
         ex("¿Cómo se dice por favor?", "please", "Please es por favor.")],
        [ex("¿Cuál va después de Don't: run o to run?", "run", "El verbo va solo."),
         ex("¿Qué significa Can I have an apple, please?", "¿Puedo tener una manzana, por favor?", "Es la forma de pedir con respeto."),
         ex("Alguien te da algo y dice Here you are. ¿Qué respondes?", "Thank you", "Se agradece al recibir.")],
        [ex("En la sala hay ruido. Escribe en inglés: No grites, por favor.", "Don't shout, please", "Don't más shout."),
         ex("Quieres un plátano. Escribe la petición completa en inglés. (plátano = banana)", "Can I have a banana, please?", "Can I have más el alimento."),
         ex("Tu hermano corre por la biblioteca. Escribe la frase que usarías.", "Don't run", "Don't más run.")],
        [ex("Un niño dice Don't to shout. ¿Qué error hay?", "Sobra to", "Después de Don't va el verbo solo."),
         ex("Ana pide Give me an apple. ¿Qué frase más amable le sugieres?", "Can I have an apple, please?", "Incluye please y es una pregunta.")],
        [ex("Un adulto lee: Don't eat in the library. Can I have water, please? Escribe cuál es la prohibición.", "Don't eat in the library", "Don't indica prohibición."),
         ex("Escribe un diálogo de dos líneas: pides una pera (pear) y te responden Here you are. Escribe tus dos líneas.", "Can I have a pear, please? Thank you.", "Pido con please y agradezco al recibir.")],
    ),
    context=[ex("En el recreo hay un cartel que dice Don't run. ¿Qué te pide el cartel?", "Que no corra", "Don't run es no corras.")],
    selfcheck=[ex("¿Cómo se dice no grites?", "Don't shout", "Shout es gritar."),
               ex("¿Cómo pides una manzana?", "Can I have an apple, please?", "Es la fórmula de petición."),
               ex("¿Qué dices al recibir algo?", "Thank you", "Se agradece con esas palabras.")],
    open_task=task("Con un adulto, usa estas dos situaciones. 1) Estás en la biblioteca y alguien grita: di la frase de prohibición. 2) Quieres una manzana en el almuerzo: pídela. Escribe tus dos frases y practícalas en voz alta.",
                   "1) Don't shout, please. 2) Can I have an apple, please? Thank you.",
                   ["usa Don't + verbo", "usa Can I have", "usa please y thank you"], ["dos frases escritas", "demostración oral"], ["Don't to", "pedir sin please"],
                   "Celebra la amabilidad. Pide repetir con tono firme y cortés."),
    reinforce="Cuando veas un cartel de prohibición, di en inglés qué no se debe hacer.",
    extend="Escribe tres prohibiciones de tu casa con Don't y léelas a un adulto.",
)

register(
    OA12, 5,
    materials="Imágenes descritas de una sala, objetos y acciones escritas en este cuaderno, lápiz y un adulto.",
    use="Aprenderé a decir dónde están los objetos y qué acciones ocurren ahora. Sirve para describir lo que veo en una escena.",
    prior=["Conozco on, in y under.", "Conozco run, eat y read."],
    explain=[
        "Para decir dónde está algo, usa Where is ___? (¿dónde está ___?) y responde It is on the table (está sobre la mesa), It is in the bag (está en la bolsa), It is under the bed (está debajo de la cama) o It is next to the door (está al lado de la puerta).",
        "Para decir lo que alguien hace ahora, usa is o are más el verbo con ing: He is running (él está corriendo), She is eating (ella está comiendo), They are reading (ellos están leyendo). Con I se usa am: I am jumping (yo estoy saltando).",
        "Algunas palabras cambian al agregar ing: run se convierte en running y sit en sitting, porque duplican la última letra. Eat se convierte en eating y read en reading. Practica con una escena y descríbela con ayuda del adulto.",
    ],
    vocab=[("on", "sobre"), ("in", "dentro de"), ("under", "debajo de"), ("next to", "al lado de"), ("He is running", "él está corriendo"), ("They are reading", "ellos están leyendo")],
    worked=[
        W("Decir dónde está algo", "Una pelota está debajo de la cama. Pregunta: Where is the ball?",
          ["Entiendo la pregunta: ¿dónde está la pelota?", "Veo la pelota debajo de la cama.", "Respondo con under."],
          "It is under the bed."),
        W("Decir una acción ahora", "Un niño corre en el patio. ¿Qué dices?",
          ["Uso He is.", "El verbo run se escribe running.", "Junto las partes."],
          "He is running."),
    ],
    mistakes=[
        M("Decir He running sin is.", "Se olvida el verbo is.", "Siempre is, are o am antes del verbo con ing."),
        M("Escribir runing con una sola n.", "Se agrega ing sin duplicar.", "Run duplica la n: running."),
    ],
    tiers=T(
        [ex("¿Qué significa on?", "Sobre", "On es sobre."),
         ex("¿Qué significa under?", "Debajo de", "Under es debajo."),
         ex("¿Qué significa She is eating?", "Ella está comiendo", "Eating es comiendo.")],
        [ex("Where is the cat? It is ___ the bed (debajo). Elige: under o on.", "under", "El gato está debajo."),
         ex("¿Qué se usa antes de running con He: is o are?", "is", "He se usa con is."),
         ex("¿Qué se usa antes de reading con They: is o are?", "are", "They se usa con are.")],
        [ex("La mochila está sobre la silla. Escribe en inglés: está sobre la silla.", "It is on the chair", "On es sobre."),
         ex("Una niña lee en el patio. Escribe en inglés lo que hace ahora.", "She is reading", "Reading es leyendo."),
         ex("Tus dos amigos comen en el patio. Escribe en inglés lo que hacen ahora.", "They are eating", "They are más eating.")],
        [ex("Un niño escribió He runing. ¿Qué dos errores hay?", "Falta is y es running", "Falta el verbo is y la n se duplica."),
         ex("Julia dice The ball is on the table pero la pelota está debajo de la mesa. ¿Qué palabra cambias?", "on por under", "Under es debajo.")],
        [ex("Un adulto lee: The book is in the bag. The dog is sleeping. Escribe dónde está el libro.", "In the bag", "In es dentro de."),
         ex("Escribe dos oraciones sobre una escena: el gato está sobre la mesa y el niño está saltando.", "The cat is on the table. The boy is jumping.", "Cada oración usa is más una palabra de lugar o acción.")],
    ),
    context=[ex("Tu mamá te pregunta por teléfono: Where is the ball? La pelota está debajo del sillón. Responde en inglés.", "It is under the sofa", "Under es debajo.")],
    selfcheck=[ex("¿Cómo se dice dentro de?", "in", "In es dentro de."),
               ex("¿Cómo dices él está corriendo?", "He is running", "Is más running."),
               ex("¿Cómo preguntas dónde está algo?", "Where is...?", "Where es dónde.")],
    open_task=task("Con un adulto, mira tu pieza o tu casa. Escribe dos oraciones de lugar: It is on the ___. It is in the ___. Y dos de acción ahora: I am ___ing (por ejemplo I am reading) y He/She is ___ing. Dibuja la escena.",
                   "The book is on the table. The ball is in the bag. I am reading. She is eating. Dibujé mi mesa con un libro.",
                   ["usa on e in correctamente", "usa is o am con ing", "dibujo coincide"], ["cuatro oraciones", "dibujo de escena"], ["olvidar is", "runing sin duplicar"],
                   "Celebra una oración correcta antes de corregir. Revisa la ortografía del ing."),
    reinforce="Pregunta Where is...? sobre tres cosas de tu casa.",
    extend="Escribe una escena del patio con cuatro acciones usando is y are.",
)
