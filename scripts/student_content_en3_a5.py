"""Student material for 3.º básico Inglés (propuesta), EN03 OA 05 (reaccionar a lo escuchado: dibujos, mímica, dramatización y frases escritas).

Las «escuchas» las lee un adulto; el guion va en el enunciado. Las respuestas personales usan personajes inventados para no compartir datos privados.
"""
from __future__ import annotations

from student_content_en3_a import ADULT, E, lesson, task
from student_lessons import arith

OA5 = "EN03 OA 05"

lesson(
    OA5, 1,
    "El texto escrito en cada ejercicio, que lee un adulto; hoja, lápiz y lápices de colores o solo lápiz grafito.",
    "Aprenderé a responder a lo que escucho con un dibujo que muestre lo que dice el texto y a ponerle etiquetas en inglés. Sirve para mostrar que entendí sin necesidad de hablar mucho.",
    ["Sé los colores yellow, green y brown.", "Conozco las palabras sun, tree y dog."],
    [
        "Un dibujo puede ser una respuesta a lo que escuchas. Primero escucha y anota los datos del texto: cosas, colores, tamaños y cantidades. Luego dibuja justo eso. Si el texto dice «I see a big yellow sun», dibujas un sol grande y amarillo. Después puedes agregar una idea tuya, pero sin cambiar lo que dijo el texto.",
        "Las etiquetas (labels) son palabras escritas junto al dibujo que dicen qué es cada cosa, por ejemplo «a green tree». En inglés, el color va antes del objeto: green tree, no tree green. Si hay tamaño y color, el tamaño va primero: «a big yellow sun». Palabras de hoy: big (grande), small (pequeño), I see (yo veo).",
        "Para revisar tu dibujo, haz una lista: ¿hay el número correcto de cosas? ¿están los colores? ¿están los tamaños? Si alguna falla, corrige el dibujo y no el texto. El texto es la evidencia de tu dibujo.",
    ],
    [("draw", "dibujar"), ("label", "etiqueta"), ("I see", "yo veo"), ("big / small", "grande / pequeño"), ("yellow / green / brown", "amarillo / verde / café"), ("sun / tree / dog", "sol / árbol / perro")],
    [
        ("Dibujar lo que dice el texto", ADULT + "«I see a big yellow sun. I see two green trees. I see a small brown dog.» ¿Cuántos árboles dibujas y de qué color?", ["Busco trees.", "Oigo two green trees.", "Dibujo dos árboles verdes."], "Dos árboles verdes"),
        ("Escribir una etiqueta", "Quieres poner una etiqueta a un árbol verde. ¿Cuál es correcta: a) a green tree b) a tree green?", ["En inglés el color va antes del objeto.", "Green va antes de tree.", "La etiqueta correcta es la a."], "a"),
    ],
    [
        ("Dibujar algo distinto de lo que dice el texto.", "No se comprobó con el texto.", "Haz una lista de cosas, colores, tamaños y números antes de dibujar."),
        ("Escribir el color después del objeto, como «tree green».", "Se usa el orden del español.", "En inglés el color va antes: green tree."),
    ],
    [
        (ADULT + "«I see a big yellow sun.» ¿De qué color pintas el sol?", "Amarillo", "Yellow es amarillo."),
        (ADULT + "«I see two green trees.» ¿Cuántos árboles dibujas?", "2", "Two es dos."),
        (ADULT + "«I see a small brown dog.» ¿Qué animal dibujas?", "Un perro", "Dog es perro."),
    ],
    [
        ("¿Qué debe tener un dibujo que responde a un texto oral?", "Lo que dice el texto: cosas, colores, tamaños y números", "El texto es la evidencia."),
        ("¿Qué es una etiqueta (label)?", "Una palabra escrita junto al dibujo que dice qué es", "Ayuda a mostrar que entendí."),
        ("¿Para qué agregar una idea propia a un dibujo?", "Para hacer mi respuesta personal sin cambiar lo que dijo el texto", "Primero va el texto y luego mi idea."),
    ],
    [
        (ADULT + "«I see a big yellow sun. I see two green trees.» ¿Qué dibujo es correcto: a) un sol grande amarillo y dos árboles verdes b) un sol pequeño rojo y un árbol verde?", "a", "Coincide con big, yellow y two green trees."),
        ("Quieres una etiqueta para un sol grande y amarillo. ¿Cuál es correcta: a) a big yellow sun b) a yellow big sun?", "a", "El tamaño va antes del color."),
        (ADULT + "«I see a small brown dog.» ¿Qué dos palabras describen al perro?", "small y brown", "Small es pequeño y brown es café."),
    ],
    [
        ("Lucía dibujó tres árboles, pero el texto decía «two green trees». ¿Qué debe cambiar?", "Dibujar solo dos árboles", "Two es dos."),
        ("Pedro pintó el sol azul. ¿Qué parte del texto prueba que se equivocó?", "big yellow sun", "Yellow es amarillo."),
    ],
    [
        arith(ADULT + "«I see a big yellow sun. I see two green trees. I see a small brown dog.» ¿Cuántas cosas dibujas en total: un sol, dos árboles y un perro?", "1+2+1", "Se suman todas las cosas que dibujas."),
        ("Ordena las palabras de la etiqueta: yellow, sun, big, a.", "a big yellow sun", "Va primero el artículo, luego tamaño, color y objeto."),
    ],
    [(ADULT + "En la clase de arte, un amigo te cuenta lo que ve: «I see a small green tree.» ¿Qué dibujas?", "Un árbol pequeño y verde", "Small es pequeño y green es verde.")],
    [
        ("¿Qué significa «label»?", "Etiqueta", "Es la palabra que acompaña a un dibujo."),
        (ADULT + "«I see a big dog.» ¿De qué tamaño dibujas el perro?", "Grande", "Big es grande."),
        ("¿Dónde va el color en inglés: antes o después del objeto?", "Antes", "En inglés se dice green tree."),
    ],
    task("Un adulto lee dos veces: «I see a big yellow sun. I see two green trees. I see a small brown dog.» Dibuja lo que oíste y escribe tres etiquetas: a big yellow sun, two green trees, a small brown dog. Después agrega una cosa tuya (por ejemplo una nube) sin cambiar lo que dijo el texto.", "Un dibujo con sol amarillo grande, dos árboles verdes y un perro café pequeño con sus tres etiquetas.", ["dibuja las tres cosas con color y cantidad correctos", "escribe las tres etiquetas con el color antes del objeto", "agrega una idea propia sin cambiar el texto"], ["dibujo", "nota del adulto"], ["dibujar tres árboles", "escribir tree green"], "Reconoce los datos bien representados y revisa con él cada etiqueta contra el texto."),
    "Pide a un adulto que diga «big yellow sun» y dibuja solo el sol.",
    "Dibuja otra escena con cuatro cosas, escribe una etiqueta para cada una y pide a otra persona que compruebe si coinciden.",
)

lesson(
    OA5, 2,
    "Las frases escritas en cada ejercicio, que lee un adulto; un espacio libre y seguro para moverte.",
    "Aprenderé a responder a lo que escucho con una mímica: mostrar con el cuerpo y el rostro lo que dice el texto. Sirve para mostrar que entendí sin hablar.",
    ["Sé acciones como jump, read y eat.", "Sé sentimientos como happy, sad y tired."],
    [
        "Mimar (mime) es mostrar con el cuerpo y la cara, sin hablar, lo que dice un texto. Si escuchas «I'm tired», haces cara de sueño, bajas los hombros y bostezas. Si escuchas «I'm jumping», saltas con cuidado. Si escuchas «I'm eating an apple», haces como que sostienes una manzana y la comes. Las frases con -ing dicen lo que pasa ahora: «Ben is running» significa «Ben está corriendo».",
        "Antes de mimar, escucha la palabra clave del sentimiento o de la acción: happy, sad, tired, jumping, reading, eating, swimming, sleeping. Cada una tiene su movimiento. Haz un movimiento claro y despacio, para que otra persona lo pueda entender. Así muestras que comprendiste el texto.",
        "Cuando hay varias acciones, mímalas en el orden en que las oyes o en el orden que dicen las palabras. Si no estás seguro, escucha de nuevo. Mimar no requiere hablar inglés perfecto: lo importante es que el movimiento coincida con la palabra.",
    ],
    [("mime", "mímica, mostrar con el cuerpo"), ("face", "cara"), ("hands", "manos"), ("tired", "cansado"), ("jumping", "saltando"), ("eating an apple", "comiendo una manzana"), ("two times", "dos veces")],
    [
        ("Mímica de un sentimiento", ADULT + "«I'm tired.» ¿Qué mimas: a) bostezar y bajar los hombros b) saltar con los brazos arriba?", ["Busco la palabra del sentimiento: tired.", "Tired es cansado.", "Un cansado bosteza y baja los hombros."], "a"),
        ("Mímica de una acción", ADULT + "«I'm eating an apple.» ¿Qué mimas?", ["Busco eating.", "Eating es comiendo.", "Hago como que como una manzana."], "Comer una manzana"),
    ],
    [
        ("Mimar una acción distinta de la que dice el texto.", "No se escuchó la palabra clave.", "Escucha la palabra de acción antes de mimar."),
        ("Mimar tan rápido que nadie entiende.", "Falta claridad.", "Haz movimientos claros y despacio."),
    ],
    [
        (ADULT + "«I'm tired.» ¿Qué mimas: a) bostezar y bajar los hombros b) saltar con los brazos arriba?", "a", "Tired es cansado."),
        (ADULT + "«I'm jumping.» ¿Qué mimas?", "Saltar", "Jumping significa saltando."),
        (ADULT + "«I'm eating an apple.» ¿Qué mimas?", "Comer una manzana", "Eating an apple significa comiendo una manzana."),
    ],
    [
        ("¿Qué es mimar?", "Mostrar con el cuerpo y la cara, sin hablar", "La mímica no usa palabras."),
        ("¿Cómo mimas la palabra «sad»?", "Con cara triste y hombros caídos", "Sad es triste."),
        ("¿Para qué sirve mimar lo que escuchas?", "Para mostrar que lo entendí", "El movimiento muestra la comprensión."),
    ],
    [
        (ADULT + "«Ana is swimming. Ben is sleeping.» ¿Qué mimas primero?", "Nadar", "Ana is swimming se oye primero."),
        (ADULT + "«I'm happy. I'm jumping.» ¿Qué dos cosas mimas?", "Cara de feliz y saltar", "Happy y jumping son las dos palabras clave."),
        (ADULT + "«Tom is reading.» ¿Qué mimas?", "Leer un libro", "Reading es leyendo."),
    ],
    [
        ("Ana mimó dormir cuando el texto decía «Ben is running». ¿Qué debió mimar?", "Correr", "Running es corriendo."),
        ("¿Por qué conviene escuchar antes de mimar?", "Para saber qué acción pide el texto", "La palabra de acción dice qué mimar."),
    ],
    [
        (ADULT + "«Jump two times. Then I'm tired.» ¿Cuántos saltos haces y qué mimas al final?", "2 saltos y cansancio", "Two times son dos y tired es cansado."),
        (ADULT + "«Ana is reading. Then she is eating. Last she is sleeping.» Ordena: A) dormir B) comer C) leer.", "C, B, A", "El orden es read, eat y sleep."),
    ],
    [(ADULT + "En el recreo, un amigo dice: «I'm happy! I'm jumping!» ¿Qué haces para mostrar que entiendes?", "Pongo cara de feliz y salto", "Happy y jumping se mima junto.")],
    [
        ("¿Qué significa «sleeping»?", "Durmiendo", "Es una acción que puedes mimar."),
        (ADULT + "«Ben is running.» ¿Qué mimas?", "Correr", "Running es correr."),
        ("¿Cómo mimas «happy»?", "Con cara alegre y sonrisa", "Happy es feliz."),
    ],
    task("Un adulto lee dos veces: «I'm happy. I'm jumping. I'm tired. I'm sleeping.» Mima cada frase en orden, en un espacio libre y seguro. Después di en inglés una de las palabras que mimaste, por ejemplo happy.", "Cara feliz, saltar con cuidado, cara cansada y dormir; dice happy.", ["mima las cuatro frases en orden", "dice una palabra en inglés", "los movimientos coinciden con cada palabra"], ["nota del adulto", "foto o video con permiso de la familia"], ["mimar en otro orden", "mimar happy con cara triste"], "Reconoce las mímicas claras y repite con él la palabra que le costó."),
    "Pide a un adulto que diga «sad» y muestra con la cara cómo se ve.",
    "Elige tres palabras de acción y haz una mímica para que otra persona adivine cuál es cada una.",
)

lesson(
    OA5, 3,
    "El guion de la escena escrito en cada ejercicio; un compañero o una persona de tu casa para leer las líneas y un espacio libre y seguro.",
    "Aprenderé a dramatizar una escena corta: actuar los personajes con voz y cuerpo. Sirve para responder a una historia mostrando lo que entendí.",
    ["Sé quiénes son los speakers de un diálogo.", "Sé que Wow muestra sorpresa."],
    [
        "Dramatizar (dramatize) es actuar una escena de una historia con la voz, la cara y el cuerpo. No hace falta dramatizar toda la historia: elige un momento clave (key moment), que es la parte más importante. En la escena de la caja que verás abajo, el momento clave es cuando aparece el gato.",
        "Aquí hay un guion corto con dos personajes. Leo: «Look! A box!» Mia: «Open it, please!» Leo: «Wow! A cat!» (Look = mira, Open it = ábrela, Wow = ¡guau!). Una línea es lo que dice un personaje en su turno. Cada persona actúa un personaje y lee solo sus líneas.",
        "Para actuar bien, usa la voz que corresponde: «Wow! A cat!» se dice con sorpresa. Usa gestos: mirar una caja, abrirla, sonreír. Si una frase dice «Here!», significa «¡Toma!» y se dice mientras se ofrece algo. Practica dos veces antes de mostrarlo.",
    ],
    [("dramatize", "actuar una escena"), ("key moment", "momento clave"), ("line", "línea: lo que dice un personaje"), ("Look!", "¡mira!"), ("Open it, please!", "¡ábrela, por favor!"), ("Wow!", "¡guau!, expresión de sorpresa")],
    [
        ("Quién dice qué", "Escena. Leo: «Look! A box!» Mia: «Open it, please!» Leo: «Wow! A cat!» ¿Quién dice «Open it, please»?", ["Busco la frase en el guion.", "Está después del nombre Mia.", "La dice Mia."], "Mia"),
        ("Voz y emoción", "En la misma escena, ¿con qué emoción dices «Wow! A cat!»: sorpresa o sueño?", ["Wow muestra sorpresa.", "Un gato aparece de repente.", "La voz es de sorpresa."], "Sorpresa"),
    ],
    [
        ("Dramatizar toda la historia sin elegir una parte.", "Es muy largo para mostrar bien.", "Elige un momento clave y actúalo."),
        ("Decir las líneas sin cambiar la voz ni el cuerpo.", "No se muestra la emoción.", "Cambia la voz y usa gestos que coincidan."),
    ],
    [
        ("Escena. Leo: «Look! A box!» Mia: «Open it, please!» Leo: «Wow! A cat!» ¿Cuántos personajes hablan?", "2", "Hablan Leo y Mia."),
        ("En la misma escena, ¿quién dice «Open it, please»?", "Mia", "Esa línea está después de Mia."),
        ("¿Qué significa «Wow»?", "Una expresión de sorpresa", "Se dice cuando algo te sorprende."),
    ],
    [
        ("¿Qué es dramatizar?", "Actuar una escena con la voz y el cuerpo", "Dramatizar es representar."),
        ("¿Qué es un momento clave de una historia?", "La parte más importante", "Es lo que mejor se puede actuar."),
        ("¿Con qué emoción se dice «Wow! A cat!»?", "Con sorpresa", "Wow muestra sorpresa."),
    ],
    [
        ("Ordena las líneas de la escena: A) «Wow! A cat!» B) «Open it, please!» C) «Look! A box!»", "C, B, A", "Primero Look, luego Open it y por último Wow."),
        ("En el guion, ¿quién dice «Wow! A cat!»?", "Leo", "Esa línea está después de Leo."),
        ("Si actúas a Mia, ¿qué frase dices?", "Open it, please!", "Es la única línea de Mia."),
    ],
    [
        ("Un grupo quiere dramatizar un cuento largo completo. ¿Qué es mejor hacer?", "Elegir solo un momento clave", "Una escena corta se actúa mejor."),
        ("Marta dice «Wow! A cat!» con voz triste. ¿Qué no coincide?", "La emoción: Wow muestra sorpresa", "La voz debe coincidir con la emoción."),
    ],
    [
        ("En el guion, ¿cuántas líneas dice Leo?", "2", "Leo dice Look! A box! y Wow! A cat!."),
        (ADULT + "«Ana: I'm hungry! Ben: Here! An apple!» (hungry = con hambre, here = ¡toma!). ¿Quién ofrece la manzana?", "Ben", "Ben dice Here! An apple!."),
    ],
    [("En el recreo, dos amigos actúan: Leo: «Look! A box!» Mia: «Open it, please!» Leo: «Wow! A cat!» ¿Cuál es el momento clave?", "Cuando aparece el gato", "La sorpresa del gato es lo más importante.")],
    [
        ("¿Qué significa «line» en un guion?", "Lo que dice un personaje en su turno", "Cada turno es una línea."),
        ("¿Qué significa «Look!»?", "¡Mira!", "Look es mirar."),
        ("¿Qué conviene hacer antes de mostrar la escena a otras personas?", "Practicarla", "Practicar mejora la actuación."),
    ],
    task("Con un compañero o una persona de tu casa, lean y actúen dos veces esta escena: Leo: «Look! A box!» Mia: «Open it, please!» Leo: «Wow! A cat!» Uno hace a Leo y el otro a Mia. Usen gestos de mirar y abrir una caja, y voz de sorpresa en la última línea.", "Actúan la escena con gestos y voz de sorpresa en Wow! A cat!.", ["dice sus líneas en el orden del guion", "usa gestos que coinciden", "usa voz de sorpresa en la última línea"], ["nota del adulto", "foto o video con permiso de la familia"], ["decir las líneas en otro orden", "usar voz triste en Wow"], "Reconoce el gesto más claro y repite con él la última línea con sorpresa."),
    "Pide a un adulto que diga «Wow!» con sorpresa y repite con la misma voz.",
    "Cambia el animal del guion (por ejemplo un perro) y actúa de nuevo la escena con las mismas líneas.",
)

lesson(
    OA5, 4,
    "Las frases escritas en cada ejercicio; lápiz y hoja.",
    "Aprenderé a decir qué me gusta o qué no me gusta y a dar una razón sencilla. Sirve para expresar mis preferencias y opiniones en inglés.",
    ["Sé decir I like con un objeto.", "Conozco palabras como bike, dog, red y cold."],
    [
        "Para decir una preferencia se usa I like, que significa «me gusta». Para decir que algo no te gusta se usa I don't like. Después va lo que te gusta: «I like my bike» significa «me gusta mi bicicleta». Esa es tu preferencia (preference).",
        "Para dar una razón se usa because (porque) y luego it is con una palabra que describe: «I like my bike because it is red». La razón es it is red. Otras palabras que puedes usar: fast (rápido), soft (suave), fun (divertido), yummy (rico) y cold (frío). Con una razón, tu opinión (opinion) se entiende mejor.",
        "Una opinión completa tiene dos partes: lo que te gusta o no te gusta y por qué. Ejemplo: «I don't like the rain because it is cold». Es normal que las personas tengan opiniones diferentes. Escribe tus frases con cuidado y revisa que la razón explique la preferencia.",
    ],
    [("I like", "me gusta"), ("I don't like", "no me gusta"), ("because", "porque"), ("it is", "es"), ("fast / soft / fun / yummy", "rápido / suave / divertido / rico"), ("opinion", "opinión")],
    [
        ("Preferencia y razón", "Lee: «I like my bike because it is red.» ¿Cuál es la preferencia y cuál la razón?", ["La preferencia va después de I like: my bike.", "La razón va después de because: it is red.", "Separo las dos partes."], "Preferencia: mi bicicleta; razón: es roja"),
        ("Lo que no me gusta", "Lee: «I don't like the rain because it is cold.» (rain = lluvia, cold = fría). ¿Le gusta la lluvia?", ["Busco I don't like.", "Eso significa no me gusta.", "La razón es que es fría."], "No"),
    ],
    [
        ("Decir solo «I like cats» sin razón.", "Falta explicar por qué.", "Agrega because y una razón con it is."),
        ("Usar la razón sin conectarla, como «I like my bike. Red.»", "La razón queda suelta.", "Usa because it is red para unir las dos ideas."),
    ],
    [
        ("¿Qué significa «I like»?", "Me gusta", "Es la forma de decir una preferencia."),
        ("¿Qué significa «I don't like»?", "No me gusta", "Don't like indica que algo no gusta."),
        ("¿Qué significa «because»?", "Porque", "Introduce la razón."),
    ],
    [
        ("En «I like my bike because it is red», ¿cuál es la razón?", "It is red", "Después de because viene la razón."),
        ("¿Cuántas partes tiene una opinión completa con razón?", "Dos: lo que me gusta y por qué", "Una es la preferencia y la otra la razón."),
        ("¿Para qué sirve dar una razón?", "Para explicar mejor mi opinión", "La razón apoya la preferencia."),
    ],
    [
        ("Completa: «I like the dog ___ it is fast.» (fast = rápido).", "because", "Because introduce la razón."),
        ("Ordena las palabras: bike / my / I / like.", "I like my bike", "Primero va I like y luego el objeto."),
        ("Lee: «I don't like the rain because it is cold.» ¿Le gusta la lluvia a la persona?", "No", "I don't like significa no me gusta."),
    ],
    [
        ("Ana escribe «I like cats» y nada más. ¿Qué le falta a su opinión para estar completa?", "Una razón con because", "Una opinión con razón tiene dos partes."),
        ("Pablo escribe: «I like my bike because it is fast.» ¿Cuál es la razón?", "It is fast", "Después de because aparece la razón."),
    ],
    [
        ("¿Cuál es una opinión completa: a) I like pizza. b) I like pizza because it is yummy. (yummy = rico)", "b", "Tiene preferencia y razón."),
        ("Ordena los tres trozos para formar una opinión: «because» / «I like the cat» / «it is soft».", "I like the cat because it is soft", "Primero la preferencia, luego because y la razón."),
    ],
    [("En clase, una niña escribe: «I like the park because it is fun.» (park = parque, fun = divertido). ¿Qué le gusta y por qué?", "El parque, porque es divertido", "I like es el gusto y because it is fun es la razón.")],
    [
        ("¿Cómo se dice «opinión» en inglés?", "opinion", "Opinion es opinión."),
        ("¿Qué significa «it is soft»?", "Es suave", "Soft es suave."),
        ("Completa con una palabra: «I ___ my dog.» (me gusta mi perro).", "like", "I like significa me gusta."),
    ],
    task("Escribe en una hoja dos opiniones con esta forma: «I like ... because it is ...» y «I don't like ... because it is ...». Puedes elegir entre las cosas: the rain (la lluvia), my bike (mi bicicleta), the cat (el gato) y las razones: cold, red, soft, fast, fun. Una opinión debe decir que sí te gusta y otra que no.", "I like the cat because it is soft. I don't like the rain because it is cold.", ["escribe una opinión con I like y because", "escribe una opinión con I don't like y because", "la razón explica la preferencia"], ["hoja con las dos frases", "nota del adulto"], ["escribir las frases sin because", "razón que no explica la preferencia"], "Reconoce las partes de cada frase y revisa con él que la razón explique la preferencia."),
    "Pide a un adulto que diga «I like» y «I don't like» y marca con el pulgar arriba o abajo.",
    "Escribe tres opiniones sobre comidas o animales con I like y because.",
)

lesson(
    OA5, 5,
    "El texto y las frases escritos en cada ejercicio, que lee un adulto; hoja y lápiz.",
    "Aprenderé a conectar lo que escucho con una experiencia inventada y segura, usando too y Me too. Sirve para reaccionar a una historia sin contar cosas privadas.",
    ["Sé decir I like y I can.", "Sé que Lola es un personaje de un cuento."],
    [
        "Conectar es relacionar lo que escuchas con tu propia experiencia. Para hacerlo en inglés se usa too, que significa «también». «Lola is happy. I'm happy too» significa «Lola está feliz. Yo también estoy feliz». Otra forma corta es «Me too!», que significa «¡yo también!».",
        "Para cuidar tu privacidad, usa una experiencia ficticia (inventada) y segura. No escribas tu dirección, tu teléfono, tu apellido ni el nombre de tu escuela. Puedes inventar un personaje o una situación. Por ejemplo: «Lola has a cat. I have a cat too», aunque sea un juego de imaginación.",
        "Una buena conexión tiene dos partes: lo que dice el texto y lo que tú agregas con too. Debe coincidir con la idea del texto. Si el texto habla de un gato y tú hablas de un lápiz, no hay conexión. También puedes usar can: «Lola can swim. I can swim too».",
    ],
    [("too", "también"), ("Me too!", "¡yo también!"), ("connect", "conectar"), ("fictional", "ficticio, inventado"), ("private", "privado"), ("has / can swim", "tiene / sabe nadar")],
    [
        ("Conectar con too", ADULT + "«Lola is happy.» ¿Qué frase conecta con el texto: a) I'm happy too. b) I'm tired.", ["El texto dice happy.", "Too significa también.", "La frase a repite la idea con too."], "a"),
        ("Cuidar la privacidad", "Marta quiere conectar con un cuento escribiendo su dirección. ¿Es buena idea?", ["La dirección es un dato privado.", "Se puede inventar una experiencia ficticia.", "No se comparte."], "No; usa una experiencia inventada"),
    ],
    [
        ("Conectar con una idea distinta del texto.", "No hay relación entre la frase y el texto.", "Usa too para repetir la misma idea del texto."),
        ("Contar datos privados para conectar.", "Se comparte información que debe cuidarse.", "Inventa un personaje o una situación segura."),
    ],
    [
        ("¿Qué significa «too»?", "También", "Too une mi idea con la del texto."),
        ("¿Qué significa «Me too!»?", "¡Yo también!", "Es una forma corta de conectar."),
        (ADULT + "«Lola is happy.» ¿Qué frase conecta: a) I'm happy too. b) I'm tired?", "a", "Repite la idea de happy con too."),
    ],
    [
        ("¿Qué es una experiencia ficticia?", "Una situación inventada, no real", "Sirve para conectar sin contar cosas privadas."),
        ("¿Por qué usamos experiencias inventadas al conectar?", "Para cuidar la privacidad", "No se comparten datos personales."),
        ("¿Qué dos partes tiene una buena conexión?", "Lo que dice el texto y lo que yo agrego con too", "Debe haber relación entre ambas."),
    ],
    [
        (ADULT + "«Lola can draw. Lola is happy.» ¿Qué conexión usa too y la habilidad de Lola: a) I can draw too. b) I can't draw.", "a", "Repite la habilidad con too."),
        ("Completa: «Lola has a red bike. I have a red bike ___.»", "too", "Too significa también."),
        ("Escribe en inglés: «Yo también estoy feliz».", "I'm happy too", "Happy es feliz y too es también."),
    ],
    [
        (ADULT + "«Lola has a cat.» ¿Qué conexión con too tiene sentido: a) I have a cat too. b) I like the sun.", "a", "Repite la idea del gato con too."),
        ("Marta quiere escribir su dirección para conectar con el cuento. ¿Es una buena idea?", "No, porque es un dato privado", "Se debe usar una experiencia inventada."),
    ],
    [
        (ADULT + "«Lola can swim.» Completa tu conexión: «I can swim ___.»", "too", "Too significa también."),
        ("Ordena las palabras: too / happy / I'm.", "I'm happy too", "I'm happy va primero y too al final."),
    ],
    [("Después de escuchar «Lola has a cat», una niña dice: «I have a fish too.» Tú sabes que ella inventa el pez para jugar. ¿Tiene sentido su conexión con el cuento?", "Sí; conecta con la idea de tener una mascota", "Tener una mascota se relaciona con el cuento y usa too.")],
    [
        ("¿Cómo se dice «también» en inglés?", "too", "Too es también."),
        (ADULT + "«Lola is happy.» ¿Cómo dices que tú también lo estás?", "I'm happy too", "I'm happy too repite la idea."),
        ("¿Qué datos no debes escribir al conectar con un texto?", "Dirección, teléfono, apellido o escuela", "Son datos privados."),
    ],
    task("Un adulto lee dos veces: «Lola is happy. Lola has a red bike.» Escribe dos frases de conexión con too usando un personaje inventado, no tus datos privados. Pueden ser: «I'm happy too.» y «I have a red bike too.»", "I'm happy too. I have a red bike too.", ["escribe dos frases con too", "las frases coinciden con el texto", "no incluye datos privados"], ["hoja con las frases", "nota del adulto"], ["escribir frases sin too", "agregar un dato privado"], "Reconoce las frases que conectan y revisa con él que no incluya datos privados."),
    "Pide a un adulto que diga «Me too!» y respóndele con la misma frase.",
    "Escribe dos frases con too para otro personaje que invente, por ejemplo «Sam can run. I can run too».",
)
