"""Cuaderno del estudiante, 7.º básico Inglés (propuesta): EN07 OA 13, proceso de escritura para informar, opinar y narrar.

Los títulos de clase del plan son genéricos; aquí se reparten así: 1) organizar ideas, 2) redactar con conectores, 3) revisar y editar
(ortografía y puntuación), 4) texto de opinión con procesador de textos y diccionario en línea, 5) narrar y publicar. Las entradas de
diccionario y los textos son originales y están escritos en el enunciado; cada herramienta digital se explica y tiene su equivalente en papel.
"""
from __future__ import annotations

from student_content_en7_b import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA13 = "EN07 OA 13"

# ================================================================ OA 13 clase 1: organizar ideas
lesson(
    OA13, 1,
    "Los planes y textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé los cinco pasos del proceso de escritura y a organizar mis ideas antes de escribir. Sirve para que mis textos tengan un orden claro y solo ideas que corresponden al tema.",
    ["Sé escribir oraciones simples en inglés.", "Conozco las palabras inform, opinion y story."],
    [
        "Escribir bien es un proceso con cinco pasos: 1) organizar ideas (plan), 2) redactar un borrador (draft), 3) revisar el contenido (revise), 4) editar la forma, como ortografía y puntuación (edit), y 5) publicar la versión final (publish), es decir, compartirla con su lector. Seguir este orden evita errores y repeticiones.",
        "Para organizar las ideas, primero define el propósito (purpose): informar (inform), dar tu opinión con razones (opinion) o narrar lo que pasó (narrate). Luego anota el tema (topic), tres ideas principales y un detalle para cada una. Ejemplo de plan para informar: Topic: our school library. Idea 1: where it is (second floor). Idea 2: what it has (books and magazines). Idea 3: when it opens (8 a.m.).",
        "Una idea pertenece al plan solo si se relaciona con el tema. Si planificas la biblioteca, no incluyas el menú del casino. También conviene ordenar las ideas: de lo general a lo particular, o en el orden en que ocurrieron los hechos si narras. Por último, escribe un título (title) corto que diga de qué trata el texto.",
    ],
    [("writing process", "proceso de escritura"), ("plan", "plan: organizar ideas antes de escribir"), ("draft", "borrador"), ("revise", "revisar el contenido"), ("edit", "editar: corregir ortografía y puntuación"), ("publish", "publicar: compartir la versión final"), ("inform / opinion / narrate", "informar / opinar / narrar"), ("topic", "tema"), ("title", "título")],
    [
        ("Elegir el propósito", "Quieres contar qué pasó en tu último paseo de curso. ¿Qué propósito tiene tu texto? Opciones: inform / opinion / narrate.", ["Tienes que contar hechos que ya ocurrieron.", "Eso es narrar.", "El propósito es narrate."], "narrate"),
        ("Descartar una idea que no corresponde", "Plan. Topic: our school bus. Ideas: a) the bus is yellow b) the bus has 20 seats c) the price of ice cream. ¿Cuál idea no pertenece al tema? (Escribe la letra.)", ["Las ideas a y b hablan del bus.", "La idea c habla de helados.", "La idea que no corresponde es c."], "c"),
    ],
    [
        ("Empezar a escribir sin plan.", "Se piensa que planificar es perder tiempo.", "Dedica unos minutos a anotar tema, ideas y orden: así el borrador sale más claro."),
        ("Mezclar ideas de otro tema.", "No se compara cada idea con el tema.", "Pregunta si cada idea ayuda a explicar el tema; si no, sácala del plan."),
    ],
    [
        ("¿Cuál es el primer paso del proceso de escritura?", "Organizar las ideas", "Se planifica antes de redactar."),
        ("¿Qué significa «draft»?", "Borrador", "Es la primera versión completa del texto."),
        ("Escribir lo que piensas sobre los uniformes escolares y por qué. ¿Qué propósito tiene? Opciones: opinion / inform.", "opinion", "Se expresa lo que uno piensa y se da una razón."),
    ],
    [
        ("Plan. Topic: my dog Luna. Ideas: a) she is brown b) she likes to run c) the price of bread. ¿Cuál no pertenece al tema? (Escribe la letra.)", "c", "El precio del pan no habla de Luna."),
        ("Quieres decir cuántos días dura el año escolar y cuándo son las vacaciones. ¿Qué propósito es? Opciones: inform / narrate.", "inform", "Se entregan datos sin contar una historia."),
        ("Ordena los pasos del proceso. a) publish b) draft c) plan d) edit e) revise. Escribe las letras en orden.", "c, b, e, d, a", "Se planifica, se redacta, se revisa el contenido, se edita la forma y al final se publica."),
    ],
    [
        ("Plan. Topic: recycling at school. Ideas: 1) blue bin for paper 2) yellow bin for plastic 3) the cafeteria menu. ¿Qué número no pertenece al tema?", "3", "El menú del casino no habla de reciclaje."),
        ("Ordena los hechos de una narración. a) She arrived at school on time. b) Mia woke up late. c) She ran to the gate. Escribe las letras en orden.", "b, c, a", "Primero despierta tarde, luego corre y al final llega."),
        ("¿Qué título es mejor para un texto que informa sobre la biblioteca del colegio? a) Our School Library b) I like pizza", "a", "El título debe decir de qué trata el texto."),
    ],
    [
        ("Un compañero empezó a escribir sin plan y mezcló ideas. ¿Qué problema es probable? a) Las ideas pueden quedar desordenadas o faltar. b) El texto quedará sin palabras.", "a", "Sin plan, el orden y las ideas no se controlan."),
        ("Plan A: «I think homework is useful. Reason: it helps me remember. Example: I practice spelling». Plan B: «Homework. Spelling. Teachers». ¿Cuál es un plan completo para una opinión? Opciones: A / B.", "A", "El plan A tiene opinión, razón y ejemplo."),
    ],
    [
        ("Relaciona cada inicio con su propósito: 1) «Last Sunday I visited my aunt.» 2) «In my opinion, summer is the best season.» 3) «The park opens at 9 a.m.» Escribe: 1 …, 2 …, 3 … con narrate, opinion o inform.", "1 narrate, 2 opinion, 3 inform", "Cuenta un hecho pasado, da una opinión y entrega un dato."),
        ("Para informar sobre la huerta del colegio, ¿qué oración introduce mejor el tema? a) Yesterday I was very tired. b) Our school garden is behind the gym.", "b", "Presenta el tema y su ubicación."),
    ],
    [("Tu curso arma un diario mural sobre cuidar las plantas. ¿Cuál es el plan más completo? a) Topic: plants. Ideas: water, light, soil. Detail for each idea. b) Topic: plants. Ideas: pizza.", "a", "Tiene un tema, tres ideas relacionadas y detalles.")],
    [
        ("¿Cuáles son los cinco pasos del proceso de escritura?", "Organizar, redactar, revisar, editar y publicar", "Es el orden que se sigue al escribir un texto."),
        ("¿Qué se escribe en el plan además del tema?", "Ideas principales y detalles", "Así el borrador tiene contenido ordenado."),
        ("¿Qué significa «publish»?", "Publicar o compartir la versión final", "Es el último paso."),
    ],
    task("Lee estas tres consignas y escoge una: A) informar sobre un lugar de tu colegio, B) dar tu opinión sobre el largo del recreo, C) narrar un día divertido. En tu hoja haz el plan: propósito, tema, tres ideas con un detalle cada una, orden y un título. Después revisa que todas las ideas correspondan al tema.", "Purpose: inform. Topic: the school yard. Idea 1: where it is (behind the gym). Idea 2: what students do there (play and talk). Idea 3: rules (no running on the stairs). Order: place, activities, rules. Title: Our School Yard.", ["define propósito y tema", "tres ideas ordenadas, cada una con un detalle", "todas las ideas corresponden al tema", "título adecuado"], ["hoja con el plan completo"], ["incluir ideas de otro tema", "no definir el propósito"], "Pide que quite una idea y la reemplace por otra que corresponda mejor, explicando por qué."),
    "Copia los cinco pasos del proceso de escritura con su significado en español.",
    "Haz un segundo plan para otro propósito sobre el mismo tema y compara qué ideas cambian.",
)

# ================================================================ OA 13 clase 2: redactar con conectores
lesson(
    OA13, 2,
    "Los planes y párrafos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a pasar de un plan a un borrador usando oraciones completas y conectores. Sirve para que mis ideas se lean unidas y no como una lista suelta.",
    ["Conozco los cinco pasos del proceso de escritura.", "Sé que una oración en inglés tiene sujeto y verbo."],
    [
        "Redactar es convertir el plan en un párrafo. Una buena estructura tiene tres partes: una oración de tema (topic sentence) que presenta la idea, oraciones de apoyo (supporting sentences) con detalles y una oración final (closing) que cierra. Ejemplo: «Our school garden is behind the gym. It has tomatoes and lettuce. Also, students water the plants every week. It is a quiet place to learn».",
        "Los conectores (connectors) unen ideas: and (suma), but (contraste), because (razón), so (resultado), also (además), for example (por ejemplo). Para ordenar pasos se usan first, then, after that y finally. Cuando un conector abre una oración, va seguido de coma: First, I wash the fruit.",
        "Escribe oraciones completas con sujeto: It is cold, no Is cold. Evita traducir palabra por palabra del español: no se dice I have 13 years, sino I am 13 years old. Usa las palabras y estructuras que ya conoces, y no te detengas a corregir cada detalle en el borrador: eso viene después, al revisar y editar.",
    ],
    [("topic sentence", "oración de tema"), ("supporting sentence", "oración de apoyo"), ("closing", "oración final"), ("also", "además"), ("for example", "por ejemplo"), ("then / after that", "luego / después de eso"), ("connector", "conector")],
    [
        ("Elegir el conector de razón", "Completa: «Tom is tired ___ he played football all afternoon.» Opciones: because / but.", ["La segunda parte explica la causa del cansancio.", "Una razón se une con because.", "Queda because."], "because"),
        ("Ordenar oraciones en un párrafo", "Ordena. a) It has tomatoes and lettuce. b) Our school garden is behind the gym. c) Also, students water the plants. Escribe las letras en orden.", ["La oración de tema va primero.", "Luego van los detalles.", "El orden es b, a, c."], "b, a, c"),
    ],
    [
        ("Escribir «Is cold today» o «I have 13 years».", "Se traduce palabra por palabra del español.", "Escribe oraciones completas: It is cold today. I am 13 years old."),
        ("Escribir una lista de oraciones sin conectores.", "Se piensa que cada oración puede ir sola.", "Une las ideas con and, but, because, so, also o first, then, finally."),
    ],
    [
        ("¿Qué significa «also»?", "Además", "Suma una idea nueva."),
        ("Completa: «I like tennis, ___ I don't like golf.» Opciones: but / and.", "but", "Marca un contraste entre dos gustos."),
        ("Párrafo: «My brother loves music. He plays the guitar. He sings too.» ¿Cuál es la oración de tema?", "My brother loves music", "Presenta la idea que explican las demás oraciones."),
    ],
    [
        ("¿Qué oración tiene sujeto? a) It is cold today. b) Is cold today.", "a", "Una oración en inglés necesita sujeto, como it."),
        ("¿Cómo se dice «Tengo 13 años»? a) I have 13 years. b) I am 13 years old.", "b", "En inglés la edad se dice con el verbo ser."),
        ("Completa: «First, I wash the fruit. ___, I cut it.» Opciones: Then / Because.", "Then", "Then continúa una secuencia."),
    ],
    [
        ("Une las ideas: «I like pizza.» «I don't like onions.» a) I like pizza, but I don't like onions. b) I like pizza, because I don't like onions.", "a", "Los dos gustos son distintos y se unen con but."),
        ("Une las ideas: «The bus was late.» «I arrived late.» a) The bus was late, so I arrived late. b) The bus was late, because I arrived late.", "a", "Llegar tarde es el efecto del atraso del bus."),
        ("Completa con dos conectores en orden: «I usually walk to school, ___ today I took the bus ___ it was raining.» Escribe los dos.", "but, because", "Primero un contraste y luego una razón."),
    ],
    [
        ("Texto: «I think dogs are great. They are friendly. For example, my dog waits for me at the door.» ¿Qué función cumple For example? a) Da un ejemplo. b) Señala una secuencia.", "a", "Presenta un caso concreto que apoya la idea."),
        ("Párrafo: «My city is big. It has a river. It has two parks.» ¿Qué parte falta: topic sentence, supporting sentences o closing?", "closing", "Hay oración de tema y detalles, pero no hay cierre."),
    ],
    [
        ("Elige el párrafo mejor redactado. a) Beach. Big. Swim cousins. b) My favorite place is the beach. It is big and sunny. Also, I swim there with my cousins.", "b", "Tiene oración de tema, detalles y un conector."),
        ("¿Qué oración sirve de cierre para un párrafo sobre la huerta del colegio? a) Our school garden is a nice place to learn. b) The garden is behind the gym.", "a", "Resume la idea y cierra; la otra solo da un dato de ubicación."),
    ],
    [("Redactas un aviso para el diario mural sobre cuidar la cancha. ¿Qué texto usa mejor oraciones completas y conectores? a) The field is old, so please do not leave trash. Also, use the bins. b) Field old. Trash no. Bin.", "a", "Usa oraciones completas, un resultado con so y un conector also.")],
    [
        ("¿Qué partes tiene un párrafo bien redactado?", "Oración de tema, apoyos y cierre", "Así se presenta, se explica y se cierra."),
        ("¿Qué conector introduce una razón?", "Because", "Explica por qué ocurre algo."),
        ("¿Qué signo va después de First al comienzo de una oración?", "Una coma", "Separa el conector del resto."),
    ],
    task("Lee este plan: Topic: my favorite season. Ideas: 1) the weather 2) what I do 3) why I like it. Escribe en tu hoja un borrador de un párrafo de cinco a siete oraciones: una de tema, tres de apoyo y una de cierre. Usa al menos tres conectores distintos (and, but, because, so, also, first, then, finally). Subraya cada conector.", "My favorite season is summer. The weather is hot and sunny. I swim with my friends, and I eat ice cream. Also, I don't have homework, so I have free time. I like it because it is fun.", ["tiene oración de tema, apoyos y cierre", "usa al menos tres conectores distintos bien elegidos", "todas las oraciones tienen sujeto y verbo"], ["hoja con el borrador y los conectores subrayados"], ["lista de oraciones sin conectores", "traducir palabra por palabra"], "Pide que cambie un conector por otro y explique si cambia el sentido."),
    "Copia el párrafo modelo de la huerta y subraya la oración de tema y los conectores.",
    "Escribe dos versiones de un mismo párrafo: una sin conectores y otra con conectores, y compara cuál se entiende mejor.",
)

# ================================================================ OA 13 clase 3: revisar y editar
lesson(
    OA13, 3,
    "Los textos y listas de revisión escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a revisar el contenido de mi texto y a editar la ortografía y la puntuación. Sirve para entregar un texto claro y sin errores que distraigan.",
    ["Sé redactar un borrador con conectores.", "Conozco el punto, la coma y los signos de interrogación."],
    [
        "Revisar (revise) es mirar el contenido: ¿cumple el propósito?, ¿faltan ideas?, ¿sobra alguna?, ¿el orden es claro?, ¿los conectores ayudan? Editar (edit) es corregir la forma: ortografía (spelling), mayúsculas y puntuación. Primero se revisa y después se edita, porque no tiene sentido corregir la ortografía de una oración que quizás vas a borrar.",
        "Mayúsculas: se usan al comienzo de una oración, en nombres de personas, días y meses (Monday, March, Chile) y en el pronombre I (My friend and I). Puntuación: el punto (.) cierra una oración; la coma (,) va después de First, Then, Finally y entre elementos de una lista: «I have a pen, a ruler and a notebook». El signo de interrogación (?) cierra la pregunta y en inglés no hay signo al comienzo: Do you like pizza?",
        "Ortografía de palabras frecuentes: friend (no freind), because (no becuse), people (no peple), Wednesday, tomorrow, beautiful. Usa una lista de revisión: 1) ¿cumple el propósito?, 2) ¿hay ideas que no corresponden?, 3) ¿están los conectores?, 4) ¿hay mayúsculas y puntos?, 5) ¿están bien escritas las palabras frecuentes? Revisa en voz alta y lee una vez cada punto.",
    ],
    [("revise", "revisar el contenido"), ("edit", "editar: corregir la forma"), ("spelling", "ortografía"), ("capital letter", "letra mayúscula"), ("period / comma / question mark", "punto / coma / signo de interrogación"), ("checklist", "lista de revisión"), ("friend / because / people", "amigo / porque / gente")],
    [
        ("Distinguir revisar y editar", "Agregar una idea que falta en un texto, ¿es revisar o editar? Opciones: revise / edit.", ["Agregar una idea cambia el contenido.", "Editar solo corrige la forma.", "Es revise."], "revise"),
        ("Corregir la coma", "Corrige: «First I wash my hands.» ¿Dónde falta la coma?", ["First abre la oración como conector.", "Después de un conector inicial va coma.", "La coma va después de First."], "después de First"),
    ],
    [
        ("Corregir la ortografía antes de revisar el contenido.", "Se pierde tiempo en oraciones que luego se borran.", "Primero revisa el contenido y después edita la forma."),
        ("Escribir un día de la semana con minúscula.", "Se piensa que son palabras comunes como en español.", "En inglés Monday y los meses llevan mayúscula."),
    ],
    [
        ("¿Qué significa «revise»?", "Revisar el contenido", "Se mira si las ideas cumplen el propósito."),
        ("¿Qué significa «edit»?", "Corregir la forma, como ortografía y puntuación", "No cambia las ideas principales."),
        ("¿Qué signo cierra una pregunta en inglés?", "?", "La pregunta termina con signo de interrogación y no lleva signo inicial."),
    ],
    [
        ("¿Cuál palabra está bien escrita? a) freind b) friend", "b", "La palabra correcta es friend."),
        ("¿Cuál oración está bien escrita? a) we visit my uncle on monday. b) We visit my uncle on Monday.", "b", "Se necesita mayúscula al comienzo y en Monday."),
        ("Sacar una oración que no corresponde al tema, ¿es revisar o editar? Opciones: revise / edit.", "revise", "Es un cambio de contenido."),
    ],
    [
        ("Completa el signo final: «Do you like pizza___» Opciones: ? / .", "?", "Es una pregunta."),
        ("«I have a pen a ruler and a notebook.» ¿Después de qué palabra falta una coma?", "pen", "Los elementos de una lista se separan con coma."),
        ("¿Cuántas palabras hay que corregir en «tomorow is wednesday»?", "2", "Hay que escribir Tomorrow y Wednesday."),
    ],
    [
        ("Un estudiante corrigió primero la ortografía y después borró la mitad de las oraciones. ¿Qué orden es mejor? a) Revisar y luego editar. b) Editar y luego revisar.", "a", "Así no se corrige lo que después se elimina."),
        ("Texto: «Our school garden is behind the gym. I love pizza. It has tomatoes.» ¿Qué oración se saca al revisar el contenido?", "I love pizza.", "No habla de la huerta del colegio."),
    ],
    [
        ("Cuenta los cambios de forma que necesita «last saturday we went to the park and we plaied football.»: mayúsculas y ortografía. ¿Cuántos son?", "3", "Hay que escribir Last, Saturday y played."),
        ("¿Cuál versión de la oración está bien editada? a) We have English class on Tuesday and Thursday. b) we have english class on tuesday and thursday.", "a", "Lleva mayúsculas en We, English y en los días."),
    ],
    [("Escribes una nota para tu profesora. ¿Cuál versión está bien editada? a) Thank you, Ms. Rojas. See you on Monday. b) thank you, Ms. Rojas. See you on monday.", "a", "Lleva mayúscula al comienzo, en Ms. Rojas y en Monday, y puntuación correcta.")],
    [
        ("¿Qué se hace primero: revisar o editar?", "Revisar", "Primero se arregla el contenido."),
        ("¿Qué letra lleva un día de la semana en inglés?", "Mayúscula", "Monday se escribe con M mayúscula."),
        ("¿Dónde va la coma en una lista de elementos?", "Entre los elementos", "Sirve para separar los elementos."),
    ],
    task("Lee este borrador y corrígelo en dos pasos en tu hoja. Borrador: «my freind and i went to the park on saturday. we played football. It was fun. do you like football. I love pizza». Paso 1, revisa el contenido (borra la oración que no corresponde). Paso 2, edita (mayúsculas, ortografía y puntuación). Escribe la versión final.", "My friend and I went to the park on Saturday. We played football. It was fun. Do you like football?", ["elimina la oración que no corresponde al tema", "corrige las mayúsculas, la ortografía y los signos", "escribe la versión final completa"], ["hoja con los dos pasos y la versión final"], ["corregir antes de revisar", "olvidar el signo de interrogación"], "Pide que explique qué cambió en cada paso y por qué."),
    "Copia la lista de revisión de la explicación y úsala sobre un texto tuyo de la clase anterior.",
    "Escribe un texto con diez errores de forma a propósito y pide a una persona de tu casa que los encuentre.",
)

# ================================================================ OA 13 clase 4: opinión, procesador de textos y diccionario en línea
lesson(
    OA13, 4,
    "Las entradas de diccionario y los textos escritos en cada ejercicio, lápiz y una hoja. Opcional: un computador o un celular con diccionario en línea; todo se puede hacer también con un diccionario de papel.",
    "Aprenderé a escribir un texto de opinión y a usar un procesador de textos y un diccionario en línea con criterio. Sirve para escribir con apoyo de herramientas sin dejar que ellas decidan por mí.",
    ["Conozco el proceso de escritura y la revisión.", "Sé que una palabra puede tener más de un significado."],
    [
        "Un texto de opinión tiene cuatro partes: tu opinión (I think…, In my opinion…), una razón con because, un ejemplo con For example y un cierre. Ejemplo: «In my opinion, we need more trees. They give shade because they are big. For example, we can sit under a tree at recess. That's why we need more trees».",
        "Un procesador de textos (word processor) sirve para escribir, copiar y mover oraciones, cambiar el tamaño de letra y contar palabras. Su corrector subraya en rojo las palabras que no conoce (recieve → receive), pero no detecta todo: no marca their en «Their is a dog», porque their existe, aunque ahí corresponde There. Tú decides: el corrector ayuda, pero no piensa por ti.",
        "Un diccionario en línea muestra para cada palabra su categoría (n. = sustantivo, v. = verbo, adj. = adjetivo), uno o más significados y oraciones de ejemplo. Si hay varios significados, lee el ejemplo y elige el que calza con tu oración. Sirve para comprobar significado, ortografía y ejemplo de uso. Si no tienes aparato, un diccionario de papel o una lista de palabras funciona igual.",
    ],
    [("opinion", "opinión"), ("In my opinion", "en mi opinión"), ("For example", "por ejemplo"), ("word processor", "procesador de textos"), ("spell checker", "corrector ortográfico"), ("online dictionary", "diccionario en línea"), ("n. / v. / adj.", "sustantivo / verbo / adjetivo"), ("their / there", "de ellos / allí, hay")],
    [
        ("Elegir el significado según el ejemplo", "Entrada: «bank (n.) 1. a place where people keep money: I put money in the bank. 2. the land next to a river: We sat on the river bank». ¿Qué significado calza con «We sat on the bank of the river»? Escribe 1 o 2.", ["Lee las oraciones de ejemplo.", "La oración habla de un río.", "Calza el significado 2."], "2"),
        ("Decidir con el corrector", "El corrector subraya «recieve» y sugiere «receive». ¿Qué haces? Opciones: comprobar que receive es la palabra que quiero y aceptar / aceptar cualquier cambio sin mirar.", ["El corrector ayuda, pero tú decides.", "Debes comprobar que la palabra sugerida es la que quieres.", "Compruebas y aceptas."], "comprobar que receive es la palabra que quiero y aceptar"),
    ],
    [
        ("Aceptar todas las sugerencias del corrector sin leer.", "Se cree que el corrector entiende el sentido.", "Lee cada sugerencia y comprueba que calza con tu oración."),
        ("Escribir una opinión sin razón.", "Se cree que decir «I think…» basta.", "Agrega because y un ejemplo con For example."),
    ],
    [
        ("¿Qué significa «In my opinion»?", "En mi opinión", "Introduce lo que tú piensas."),
        ("¿Qué hace un procesador de textos?", "Permite escribir y corregir un texto en el computador", "Sirve para escribir, mover, corregir y contar palabras."),
        ("En un diccionario, ¿qué significa «adj.»?", "Adjetivo", "Indica la categoría de la palabra."),
    ],
    [
        ("¿Qué inicio de opinión es mejor? a) In my opinion, dogs are great pets. b) Dogs are animals with four legs.", "a", "Muestra lo que el autor piensa."),
        ("Entrada: «light (n.) 1. energy from the sun or a lamp. (adj.) 2. not heavy». En «My backpack is light today», ¿cuál significado calza? a) luz b) liviano", "b", "Se habla de peso, no de luz."),
        ("Completa: «I think tennis is fun ___ I play with friends.» Opciones: because / but.", "because", "La segunda parte da la razón de su opinión."),
    ],
    [
        ("El procesador no subraya «their» en «Their is a dog in the park». ¿Qué debes hacer? a) Revisar yo mismo el sentido y escribir There. b) Confiar en que está bien porque no hay subrayado.", "a", "El corrector no detecta una palabra que existe pero no va ahí."),
        ("En «In my opinion, we need more trees. They give shade. For example, we can sit under a tree at recess», ¿cuál oración da el ejemplo?", "For example, we can sit under a tree at recess.", "Es la oración que empieza con For example."),
        ("¿Cuál opinión es más fuerte? a) I think homework is boring because it takes a long time. b) I think homework is boring.", "a", "Agrega una razón."),
    ],
    [
        ("Entrada: «fine (adj.) 1. very good: I'm fine, thanks. 2. thin: fine hair. (n.) 3. money you pay as a punishment: a parking fine». En «The library gives a fine if you return a book late», ¿qué significado calza? Escribe 1, 2 o 3.", "3", "Se habla de dinero que se paga como castigo."),
        arith("Tu texto debe tener al menos 40 palabras. El contador del procesador de textos dice 33. ¿Cuántas palabras debes agregar como mínimo?", "40 - 33", "Se resta lo que tiene a lo que debe tener.", " palabras"),
    ],
    [
        ("Escribes en el computador y el corrector subraya «Wendsday». ¿Cuál es la ortografía correcta? Opciones: Wednesday / Wensday.", "Wednesday", "Es la forma correcta del día de la semana."),
        ("Quieres comprobar el significado de «shade» (sombra). ¿Qué parte del diccionario te sirve para ver cómo se usa? Opciones: oraciones de ejemplo / número de página.", "oraciones de ejemplo", "Los ejemplos muestran cómo se usa la palabra."),
    ],
    [("Escribes una opinión para el diario del colegio: ¿Debe haber un rato de silencio después del almuerzo? ¿Cuál texto es mejor? a) In my opinion, we need quiet time after lunch because students are tired. For example, many students rest their heads. b) We need quiet time.", "a", "Tiene opinión, razón y ejemplo.")],
    [
        ("¿Qué partes tiene una opinión bien escrita?", "Opinión, razón, ejemplo y cierre", "Así se justifica lo que se piensa."),
        ("¿Por qué no hay que confiar solo en el corrector ortográfico?", "Porque no detecta palabras que existen pero no corresponden", "Por ejemplo their en vez de there."),
        ("Si una palabra tiene varios significados, ¿qué miras para elegir?", "El ejemplo", "Compara la oración de ejemplo con la tuya."),
    ],
    task("Lee este encargo: escribe un texto de opinión de cinco oraciones sobre este tema: ¿Debe el colegio tener más tiempo de recreo? Incluye tu opinión (In my opinion o I think), una razón con because, un ejemplo con For example y un cierre. Si tienes un computador, escríbelo ahí y usa el corrector; si no, usa lápiz. Anota una palabra que revisarías en un diccionario y qué significado elegirías.", "In my opinion, we need a longer recess because students are tired after class. For example, many students need time to play and talk. A longer recess helps us study better. That's why I think we need more time. Word to check: recess (recreo).", ["incluye opinión, razón con because y ejemplo", "tiene una oración de cierre", "anota una palabra para el diccionario y un significado"], ["hoja o archivo con el texto y la palabra elegida"], ["no dar razones", "aceptar sugerencias del corrector sin leer"], "Pide que cambie la razón por otra y explique si la opinión sigue siendo convincente."),
    "Copia las cuatro partes de la opinión modelo y subraya cada una con un color distinto.",
    "Busca en un diccionario, de papel o en línea, una palabra con dos significados y escribe una oración con cada uno.",
)

# ================================================================ OA 13 clase 5: narrar y publicar
lesson(
    OA13, 5,
    "Las narraciones y listas de revisión escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir una narración breve y a recorrer todo el proceso hasta publicarla. Sirve para contar lo que pasó con orden y para compartirlo con otros de forma segura.",
    ["Conozco los cinco pasos del proceso de escritura.", "Sé que el pasado de go es went."],
    [
        "Una narración cuenta qué pasó: tiene personajes, lugar, tiempo, hechos en orden y un final. Se escribe en pasado y usa palabras de tiempo: Last Friday (el viernes pasado), yesterday, first, then, after that, finally, suddenly. Verbos regulares agregan -ed: visited (visité), walked (caminé), helped (ayudé). Algunos son irregulares: go–went, see–saw, eat–ate, find–found, have–had, be–was/were.",
        "El proceso completo sirve de lista de trabajo: 1) plan: personajes, lugar, tres hechos, final; 2) borrador con conectores; 3) revisión del contenido (¿están todos los hechos en orden?, ¿hay final?); 4) edición de ortografía, mayúsculas y puntuación; 5) publicación: copia en limpio, título y tu nombre de pila. Publicar significa compartirlo con un lector, por ejemplo en el diario mural o leyéndolo en voz alta.",
        "Al publicar, cuida tu privacidad: no escribas direcciones, teléfonos ni datos que identifiquen a otras personas. Si el texto va a un sitio en línea, pide primero permiso a una persona adulta. Una buena versión final se ve ordenada: título arriba, párrafos claros, letra legible y sin tachones.",
    ],
    [("narrative", "narración"), ("last Friday", "el viernes pasado"), ("went / saw / found", "fue / vio / encontró"), ("visited / walked / helped", "visité / caminé / ayudé"), ("suddenly", "de repente"), ("publish", "publicar: compartir la versión final")],
    [
        ("Elegir el pasado", "Completa: «Last Sunday, we ___ to the beach.» Opciones: went / go.", ["Last Sunday indica un tiempo pasado.", "El pasado de go es irregular.", "Queda went."], "went"),
        ("Ordenar una narración", "Ordena. a) Finally, we found the dog under a bench. b) Last Friday, my dog Max ran away. c) First, we looked in the park. d) Then we asked a neighbor. Escribe las letras en orden.", ["La narración empieza con el hecho inicial.", "Luego siguen First, Then y Finally.", "El orden es b, c, d, a."], "b, c, d, a"),
    ],
    [
        ("Escribir «Yesterday I see a rainbow».", "Se mezclan tiempos verbales.", "Si la narración está en pasado, usa saw."),
        ("Publicar con datos personales como dirección o teléfono.", "No se piensa en quién puede leer el texto.", "Publica solo tu nombre de pila y sin datos privados."),
    ],
    [
        ("¿Qué significa «publish»?", "Publicar o compartir la versión final", "Es el último paso del proceso."),
        ("¿Cuál es el pasado de go? Opciones: went / goed.", "went", "Go es un verbo irregular."),
        ("¿Qué palabra marca un hecho inesperado en una narración?", "Suddenly", "Significa de repente."),
    ],
    [
        ("Completa: «Yesterday, I ___ my grandmother.» Opciones: visited / visit.", "visited", "Yesterday indica pasado y visit es regular."),
        ("Ordena los pasos finales. a) edit b) publish c) revise d) draft. Escribe las letras en orden.", "d, c, a, b", "Se redacta el borrador, se revisa el contenido, se edita la forma y se publica."),
        ("Al publicar un texto en el diario mural, ¿qué no debes escribir? a) Tu nombre de pila b) Tu dirección", "b", "Una dirección es un dato privado."),
    ],
    [
        ("Completa: «Yesterday I ___ a rainbow.» Opciones: saw / see.", "saw", "El pasado de see es saw."),
        ("¿Cuál texto es una narración (cuenta lo que pasó)? a) Last Friday, we cleaned the yard and found a lost ball. b) The school yard is big and has trees.", "a", "Cuenta hechos en orden y en pasado."),
        ("Copiar el texto en limpio, ponerle título y escribir tu nombre de pila, ¿a qué paso del proceso corresponde? Opciones: publish / revise.", "publish", "Prepara la versión final para compartir."),
    ],
    [
        ("Tu compañero tiene plan y borrador, pero no revisó ni editó. ¿Qué dos pasos le faltan antes de publicar? (Escribe los dos en orden.)", "revise y edit", "Primero se revisa el contenido y luego se edita la forma."),
        ("Un texto en pasado contiene «walked», «helped» y «saw». ¿Cuántos verbos son irregulares?", "1", "Solo saw es irregular; walked y helped son regulares."),
    ],
    [
        ("Corrige el verbo: «Last night I eat pizza with my friends.» Opciones: ate / eated.", "ate", "Eat es irregular y su pasado es ate."),
        ("Una narración comienza «Last Monday, Leo found a coin». ¿En qué tiempo está? Opciones: pasado / presente.", "pasado", "Last Monday y found indican pasado."),
    ],
    [("Para el diario mural, tu curso publica narraciones. ¿Qué versión final está lista? a) Título, párrafos ordenados, ortografía revisada y mi nombre de pila. b) Un borrador con tachones y mi dirección.", "a", "Es una versión final ordenada que cuida los datos privados.")],
    [
        ("¿Cuál es la lista de pasos del proceso de escritura?", "Organizar, redactar, revisar, editar y publicar", "Es el camino de un texto."),
        ("¿En qué tiempo se escribe una narración?", "En pasado", "Cuenta hechos que ya ocurrieron."),
        ("¿Qué datos no debes publicar?", "Dirección y teléfono", "Son datos privados."),
    ],
    task("Lee este encargo: escribe una narración de cinco a siete oraciones sobre un día divertido (real o imaginario). Haz todo el proceso en tu hoja: 1) plan (personajes, lugar, tres hechos, final), 2) borrador con first, then y finally, 3) revisión del contenido, 4) edición de ortografía y puntuación, 5) versión final con título y tu nombre de pila. Marca cada paso cuando lo termines.", "Title: A Rainy Day. Last Saturday, Sofia and her cousin went to the park. Suddenly, it started to rain. First, they ran under a tree. Then they played with the water. Finally, they went home and drank hot milk. By Sofia.", ["muestra los cinco pasos del proceso", "la narración está en pasado y en orden", "tiene final, título y nombre de pila", "no incluye datos privados"], ["hoja con plan, borrador, cambios y versión final"], ["mezclar presente y pasado", "no revisar ni editar antes de publicar"], "Pide que lea el texto en voz alta a una persona de su casa y anote qué cambiaría después de escuchar."),
    "Copia la lista de verbos irregulares de la explicación y escribe una oración con cada uno.",
    "Escribe la misma narración desde el punto de vista de otro personaje y compara qué cambia.",
)
