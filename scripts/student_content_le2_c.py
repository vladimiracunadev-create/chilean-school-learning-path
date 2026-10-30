"""Cuaderno del estudiante, 2.º básico Lenguaje y Comunicación: OA 17 (proceso de escritura, revisión y edición)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA17 = "LE02 OA 17"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, ctx, sc, open_args, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=sc, open_task=task(*open_args), reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 17 · clase 1
reg(
    OA17, 1,
    "Las notas y borradores de este cuaderno, una hoja y un lápiz. No se necesitan otros materiales.",
    "Aprenderé a pensar para qué escribo y a escribir un primer borrador con comienzo y cierre. Sirve para que mis ideas queden ordenadas desde el principio.",
    ["Sé escribir oraciones cortas.", "Sé que un texto se escribe para alguien."],
    [
        "Antes de escribir, piensa para qué escribes. Eso se llama propósito. Puedes escribir para invitar, para contar algo que pasó o para explicar cómo se hace algo. El propósito te dice qué debes poner en el texto.",
        "Después escribe un borrador. El borrador es la primera versión de tu texto. No tiene que ser perfecto, porque lo vas a mejorar más tarde. Lo importante es que tenga un comienzo, que dice de qué trata, un desarrollo, con los datos, y un cierre, que termina la idea.",
        "Por ejemplo, para invitar a una amiga puedes escribir: «Hola, Sofía. Te invito a mi casa el sábado. ¡Te espero!». El comienzo es el saludo y la invitación. El cierre es «¡Te espero!». Si algo no te gusta, lo cambias después.",
    ],
    [("propósito", "lo que quiero lograr al escribir"), ("borrador", "la primera versión de un texto, que se puede mejorar"), ("comienzo", "la parte con que empieza un texto"), ("desarrollo", "la parte del medio, con los datos"), ("cierre", "la parte con que termina un texto"), ("invitar", "pedirle a alguien que venga a un lugar o actividad")],
    [
        ("Elegir el propósito", "Quiero escribir una nota para que mi curso venga a la feria de libros del viernes. ¿Cuál es mi propósito?", ["Leo qué quiero lograr: que mi curso venga.", "Pedir que alguien venga es invitar."], "El propósito es invitar."),
        ("Escribir un borrador con comienzo y cierre", "Propósito: invitar al curso a la feria de libros del viernes. Escribe un borrador de tres oraciones.", ["Comienzo: «Los invito a la feria de libros el viernes».", "Desarrollo: «Habrá cuentos y juegos».", "Cierre: «¡Los esperamos!»."], "Los invito a la feria de libros el viernes. Habrá cuentos y juegos. ¡Los esperamos!"),
    ],
    [("Esperar a que el texto salga perfecto antes de escribir.", "Se cree que el borrador debe estar listo a la primera.", "Escribe sin miedo: después lo revisas."), ("Terminar el texto sin cierre.", "Se deja de escribir cuando se acaban las ideas.", "Agrega una oración final que cierre la idea.")],
    [
        E("Escribo una nota para invitar a una amiga a jugar. ¿Cuál es mi propósito: invitar, contar o explicar?", "Invitar", "Pido que venga a jugar, y eso es invitar."),
        E("¿Un borrador es la primera versión o la versión final de un texto?", "La primera versión", "El borrador se escribe antes de mejorarlo."),
        E("En la nota «Hola, Sofía. Te invito a mi casa el sábado. ¡Chao!», ¿qué palabras son el saludo del comienzo?", "Hola, Sofía", "El saludo está al empezar la nota."),
    ],
    [
        E("¿Para qué sirve pensar el propósito antes de escribir?", "Para saber qué quiero lograr con mi texto", "El propósito guía lo que escribo."),
        E("Quiero contar que se me cayó el helado. Texto A: «Ayer se me cayó el helado en la plaza. Me puse triste. Mi papá me compró otro.» Texto B: «Helado. Plaza. Triste.» ¿Cuál tiene comienzo y cierre?", "El texto A", "El texto A cuenta qué pasó y termina; el B solo tiene palabras sueltas."),
        E("Pedro escribió: «Mi gato duerme en la ventana. Le gusta el sol.» ¿Qué frase sirve de cierre: a) «Por eso es mi gato favorito.» o b) «La ventana tiene vidrio.»?", "a", "Termina la idea del gato; la b agrega otro dato."),
    ],
    [
        E("Quiero explicar cómo se riega una planta. ¿Cuál es mi propósito?", "Explicar", "Digo cómo se hace algo."),
        E("Ordena los pasos del escritor con las letras: A) escribir el borrador, B) pensar para qué escribo, C) volver a leer lo escrito.", "B, A, C", "Primero pienso el propósito, luego escribo y al final releo."),
        E("Propósito: contar un paseo. ¿Qué comienzo es mejor: a) «Ayer fui al parque con mi abuela.» o b) «Muy bueno.»?", "a", "Dice quién, cuándo y dónde; la b no cuenta nada."),
    ],
    [
        E("Tomás dice: «Mi borrador tiene errores, así que no lo voy a escribir». ¿Hace bien? Explica.", "No hace bien, porque el borrador puede tener errores y se corrigen después", "El borrador es para mejorarlo más tarde."),
        E("Ana quería contar un paseo, pero escribió: «Los invito a mi cumpleaños». ¿Coincide con su propósito?", "No", "Invitar no es lo mismo que contar un paseo."),
    ],
    [
        E("Un texto tiene estas partes: «Hola, abuela.» «Hoy vi un payaso en el circo.» «Te quiero mucho. Chao.» ¿Cuál es el cierre?", "Te quiero mucho. Chao.", "Es la parte que despide y termina el texto."),
        arith("Un borrador debe tener 3 oraciones: comienzo, desarrollo y cierre. Luis ya escribió 2. ¿Cuántas le faltan?", "3-2", "Faltan las que no ha escrito."),
    ],
    [E("Tu profesora te pide avisar a las familias: «Mañana hay reunión de curso a las 5 de la tarde en la sala». ¿Cuál es el propósito y qué dos datos importantes no pueden faltar?", "Avisar o informar; cuándo (mañana, 5 de la tarde) y dónde (en la sala)", "Un aviso necesita decir cuándo y dónde.")],
    [
        E("¿Qué parte de un borrador dice de qué trata el texto: el comienzo o el cierre?", "El comienzo", "Es lo primero que lee quien lee."),
        E("Si mi texto es una invitación, ¿qué debo avisar además de «los invito»: el día o el color del papel?", "El día", "El día dice cuándo es la invitación."),
        E("¿Un borrador puede cambiarse después?", "Sí", "Se escribe para mejorarlo más tarde."),
    ],
    ("Elige UNA de estas tres ideas y escribe un borrador de tres oraciones (comienzo, desarrollo y cierre). Idea A: invitar a un amigo a jugar en la plaza. Idea B: contar lo que hiciste el fin de semana. Idea C: explicar cómo preparar pan con palta. Antes, anota tu propósito en una línea.",
     "Idea A. Propósito: invitar. «Te invito a jugar a la pelota en la plaza el sábado. Llevaré mi pelota roja. ¡Ven con ganas de jugar!»",
     ["anota el propósito", "tiene comienzo y cierre", "tiene tres oraciones que se entienden"], ["hoja con el propósito y el borrador"], ["escribir una sola palabra", "olvidar el cierre"],
     "Pregunta: «¿Para qué escribiste esto?». Si el cierre falta, pide que agregue una oración que despida o termine la idea."),
    "Escribe una nota de dos oraciones para invitar a alguien de tu casa a ver una película.",
    "Escribe dos comienzos distintos para el mismo texto y di cuál te gusta más.",
)

# ================================================================ OA 17 · clase 2
reg(
    OA17, 2,
    "Un borrador de este cuaderno, dos lápices de colores distintos y una hoja.",
    "Aprenderé a releer mi borrador como autor y a marcar lo que quiero mejorar. Sirve para que mi texto se entienda mejor.",
    ["Sé escribir un borrador corto.", "Sé qué es un propósito."],
    [
        "Un autor es la persona que escribe el texto. Después de escribir, un buen autor relee su borrador. Releer es volver a leer con atención para encontrar lo que se puede mejorar.",
        "Cuando relees, hazte tres preguntas. ¿Se entiende lo que quise decir? ¿Cumple mi propósito? ¿Le falta o le sobra algo? Con un lápiz de color marca lo que quieres cambiar, pero no lo borres todavía.",
        "Por ejemplo, lees: «Fui al parque. Fue lindo. Fui al parque». Notas que la primera y la última oración se repiten. Esa parte sobra. Marcarla es el primer paso de la revisión.",
    ],
    [("autor", "persona que escribe un texto"), ("releer", "volver a leer con atención"), ("revisar", "mirar el texto para encontrar qué mejorar"), ("sobrar", "haber algo de más"), ("marcar", "hacer una señal con lápiz")],
    [
        ("Encontrar lo que se repite", "Relee: «Mi perro es grande. Come mucho. Mi perro es grande.» ¿Qué parte sobra?", ["Leo las tres oraciones.", "La primera y la tercera dicen lo mismo.", "Una de las dos sobra."], "Sobra «Mi perro es grande» repetida."),
        ("Encontrar lo que falta", "Relee: «Ayer fui a la plaza. Me subí al.» ¿Qué falta?", ["La segunda oración queda cortada.", "Después de «al» falta decir a qué me subí."], "Falta una palabra, por ejemplo: «Me subí al columpio»."),
    ],
    [("Borrar todo el texto al releer.", "Se piensa que un error arruina todo.", "Marca solo lo que quieres cambiar."), ("Releer sin hacerse preguntas.", "Se lee rápido y se salta lo importante.", "Hazte las tres preguntas: ¿se entiende?, ¿cumple mi propósito?, ¿falta o sobra algo?")],
    [
        E("¿Quién es el autor de un texto: la persona que lo escribe o la que lo lee?", "La persona que lo escribe", "Autor significa quien crea el texto."),
        E("Releer, ¿es escribir de nuevo o volver a leer con atención?", "Volver a leer con atención", "Se relee para mejorar el borrador."),
        E("En «Mi gato es negro. Mi gato es negro.», ¿qué pasa con la segunda oración?", "Se repite", "Dice lo mismo que la primera."),
    ],
    [
        E("Menciona dos de las tres preguntas para releer.", "¿Se entiende? y ¿cumple mi propósito? (o ¿falta o sobra algo?)", "Esas preguntas guían la revisión."),
        E("Lees: «Comí pan. Después me fui a.» ¿Qué problema tiene la segunda oración?", "Está incompleta, falta decir adónde se fue", "Termina sin decir el lugar."),
        E("¿Para qué se marca con color antes de borrar?", "Para ver qué quiero mejorar sin perder el texto", "Marcar permite decidir después."),
    ],
    [
        E("Lee: «Hoy llueve. Hoy llueve mucho. Llevé paraguas.» ¿Qué oración parece repetida?", "Hoy llueve", "La segunda ya incluye esa idea con más información."),
        E("Mi propósito es invitar, pero escribí: «El sábado fui al cine». ¿Cumple mi propósito?", "No", "Cuenta lo que hice; no invita."),
        E("Lee: «Mi hermana canta. Mi hermana canta lindo.» ¿Qué puedo hacer para no repetir?", "Dejar solo «Mi hermana canta lindo»", "Une las dos ideas en una oración."),
    ],
    [
        E("Un niño releyó y dijo: «Me gusta todo, no cambio nada». El texto es: «Fui. Comí. Fui.» ¿Revisó bien?", "No, porque hay una palabra repetida y las ideas son muy cortas", "Al releer con preguntas se ve que falta información."),
        E("Ana marcó en azul lo que le gusta y en rojo lo que quiere cambiar. ¿Por qué usó dos colores?", "Para diferenciar lo que está bien de lo que va a mejorar", "Los colores ordenan la revisión."),
    ],
    [
        E("Un borrador dice: «Fui al zoológico. Vi un elefante. Vi un elefante. Era gigante». ¿Cuántas veces aparece la oración «Vi un elefante»?", "2", "La oración sale en dos lugares del borrador, así que se repite dos veces."),
        E("Lee: «Pedro tiene un perro. Se llama Rex. Pedro tiene un perro.» ¿Qué oración sobra?", "La última", "Repite la primera idea."),
    ],
    [E("Escribes: «Mi cumpleaños es el sábado. Habrá torta. Te invito.» y quieres invitar. Releyendo con el propósito, ¿qué dato importante falta?", "A qué hora o en qué lugar es el cumpleaños", "Una invitación debe decir dónde y cuándo.")],
    [
        E("¿Marco con lápiz de color o borro todo cuando reviso?", "Marco con lápiz de color", "Marcar permite decidir qué cambiar."),
        E("Si mi texto no se entiende, ¿qué pregunta de revisión no estoy cumpliendo?", "¿Se entiende lo que quise decir?", "Esa pregunta pregunta por la claridad."),
        E("¿Revisar es lo mismo que terminar de escribir?", "No", "Revisar es mejorar un borrador ya escrito."),
    ],
    ("Relee este borrador y marca con dos colores. Con azul, una oración que te gusta; con rojo, lo que quieres cambiar. Borrador: «Fui a la playa con mi tía. Hacía calor. Fui a la playa con mi tía. Me bañé y después me quedé dormido en la.» Luego escribe qué cambiarías (al menos dos cambios).",
     "Azul: «Hacía calor». Rojo: la oración repetida «Fui a la playa con mi tía» y la última, que está incompleta. Cambios: borrar la repetida y terminar la frase: «me quedé dormido en la arena».",
     ["marca con dos colores", "encuentra lo repetido", "encuentra lo incompleto"], ["borrador con marcas de color y dos cambios escritos"], ["borrar todo", "no encontrar la oración incompleta"],
     "Pregunta: «¿Qué oración dice lo mismo que otra?». Si no ve la oración incompleta, léela en voz alta junto al estudiante."),
    "Relee uno de tus textos y marca con color una cosa que cambiarías.",
    "Escribe un borrador de tres oraciones con una repetición y pide a alguien que la encuentre.",
)

# ================================================================ OA 17 · clase 3
reg(
    OA17, 3,
    "Los textos de este cuaderno, lápiz y hoja. Sirve cualquier lápiz de color para marcar.",
    "Aprenderé a escribir oraciones con mayúscula al inicio y punto al final. Sirve para que el lector sepa dónde empieza y dónde termina cada idea.",
    ["Sé qué es una oración.", "Conozco las letras mayúsculas y minúsculas."],
    [
        "Una oración es un grupo de palabras que dice una idea completa. Cuando escribimos, cada oración empieza con mayúscula y termina con punto. Así el lector sabe dónde empieza y dónde termina cada idea.",
        "Mira este texto: «hoy fui al parque me subí al columpio comí una manzana». Cuesta leerlo porque todo está pegado. Si lo ordenamos queda: «Hoy fui al parque. Me subí al columpio. Comí una manzana». Ahora hay tres ideas y se entiende mejor.",
        "Para revisar, lee tu texto en voz alta. Cuando tu voz hace una pausa larga porque termina una idea, ahí va un punto. La palabra que sigue empieza con mayúscula.",
    ],
    [("oración", "palabras que dicen una idea completa"), ("mayúscula", "letra grande con que empieza una oración"), ("punto", "signo con que termina una oración"), ("idea", "lo que pienso y quiero decir"), ("pausa", "momento en que la voz se detiene")],
    [
        ("Separar un texto en oraciones", "Ordena: «ayer llovió mucho me puse mis botas jugué en los charcos».", ["Encuentro tres ideas: llovió, me puse botas, jugué en los charcos.", "Cada una empieza con mayúscula y termina con punto."], "Ayer llovió mucho. Me puse mis botas. Jugué en los charcos."),
        ("Usar la voz para encontrar el punto", "Lee en voz alta: «Mi abuela hace pan es muy rico». ¿Dónde hay una pausa?", ["Leo: «Mi abuela hace pan» y mi voz se detiene.", "Después empieza otra idea: «es muy rico»."], "Mi abuela hace pan. Es muy rico."),
    ],
    [("Escribir un punto al final y seguir con minúscula.", "Se olvida que una idea nueva empieza con mayúscula.", "Después del punto, la primera letra es mayúscula."), ("Escribir todo seguido, sin puntos.", "No se piensa dónde termina cada idea.", "Lee en voz alta y pon punto en cada pausa larga.")],
    [
        E("En Lenguaje: ¿Con qué letra empieza una oración: mayúscula o minúscula?", "Mayúscula", "Una oración nueva siempre empieza con letra grande."),
        E("¿Con qué signo termina una oración que no pregunta ni exclama?", "Punto", "El punto cierra la idea."),
        E("En «Mi perro corre. Es veloz.», ¿cuántas oraciones hay?", "2", "Hay dos ideas, cada una con su punto."),
    ],
    [
        E("¿Por qué es difícil leer «hoy fui al parque me subí al columpio»?", "Porque no tiene mayúsculas ni puntos que separen las ideas", "Sin límites, todo se junta."),
        E("Cuál está bien escrita: a) «el gato duerme.» o b) «El gato duerme.»", "b", "Empieza con mayúscula y termina con punto."),
        E("Escribe la oración «la niña lee un libro» corregida.", "La niña lee un libro.", "Se agrega mayúscula al inicio y punto al final."),
    ],
    [
        E("Ordena con mayúsculas y puntos: «llegó el verano hace calor vamos a la playa».", "Llegó el verano. Hace calor. Vamos a la playa.", "Hay tres ideas, cada una con su límite."),
        E("Corrige: «mi mamá cocina. es rica la comida».", "Mi mamá cocina. Es rica la comida.", "Cada oración empieza con mayúscula."),
        E("Pon los puntos y mayúsculas que faltan: «mi hermano juega fútbol es muy bueno».", "Mi hermano juega fútbol. Es muy bueno.", "Hay dos ideas separadas por una pausa."),
    ],
    [
        E("Sofía dice: «Un punto es como una pausa final». ¿Tiene razón? Explica con un ejemplo breve.", "Sí, porque en «Salí a jugar. Volví a las seis.» la voz se detiene al terminar cada idea", "El punto marca la pausa donde termina la idea."),
        E("En «Ayer fui al cine. me gustó mucho.» hay un error. ¿Cuál es?", "«me» debe empezar con mayúscula después del punto", "Una oración nueva comienza con mayúscula."),
    ],
    [
        E("¿Cuántas oraciones tiene este texto bien puntuado? «Hoy es lunes. Tengo clases. Me gusta leer. Después juego.»", "4", "Cada punto cierra una oración."),
        E("El texto «mi amigo se llama Tomás tiene un perro café» tiene dos ideas. Escribe cómo debe quedar.", "Mi amigo se llama Tomás. Tiene un perro café.", "La primera idea termina antes de «tiene»."),
    ],
    [E("Quieres escribirle a tu tío: «hola tío te escribo para contarte que me fue bien en la escuela». Reescríbelo en dos oraciones, con mayúsculas, una coma después del saludo y puntos.", "Hola, tío. Te escribo para contarte que me fue bien en la escuela.", "El saludo y el mensaje son ideas distintas.")],
    [
        E("¿Cuál sigue siempre después del punto: letra minúscula o mayúscula?", "Mayúscula", "Se inicia una oración nueva."),
        E("Si leo en voz alta y mi voz se detiene al terminar una idea, ¿qué signo va?", "Punto", "El punto marca esa pausa."),
        E("¿«hoy llueve» está completo con mayúscula y punto?", "No, falta mayúscula y punto: Hoy llueve.", "Falta empezar con mayúscula y cerrar la oración."),
    ],
    ("Arregla este texto: pon mayúsculas al inicio de cada oración y puntos al final. «el sábado fui a la feria mi papá compró frutillas yo ayudé a cargar la bolsa estaba muy contento». Luego léelo en voz alta a alguien.",
     "El sábado fui a la feria. Mi papá compró frutillas. Yo ayudé a cargar la bolsa. Estaba muy contento.",
     ["usa mayúscula al inicio de cada oración", "pone punto al final", "separa las cuatro ideas"], ["texto reescrito en la hoja"], ["olvidar una mayúscula después del punto", "dejar dos ideas unidas"],
     "Pide que lea en voz alta y que levante la mano cada vez que su voz se detiene; ahí debe haber un punto."),
    "Lee un cuento corto de un libro de tu casa y cuenta cuántas oraciones tiene su primer párrafo.",
    "Escribe un texto de cuatro oraciones sobre tu día, con mayúsculas y puntos.",
)

# ================================================================ OA 17 · clase 4
reg(
    OA17, 4,
    "Las frases de este cuaderno, lápiz y hoja. Un adulto puede leer las frases en voz alta.",
    "Aprenderé a cambiar palabras repetidas o poco precisas por otras más variadas. Sirve para que mi texto sea más claro e interesante.",
    ["Sé escribir oraciones con mayúscula y punto.", "Conozco palabras como «bonito», «cosa» y «hacer»."],
    [
        "Cuando escribimos, a veces usamos siempre las mismas palabras: cosa, bonito, hacer, dijo. Eso es un vocabulario poco variado. Un vocabulario variado usa palabras distintas y más precisas para decir lo que queremos.",
        "Por ejemplo, en vez de «una cosa bonita» puedes escribir «una flor perfumada» o «un dibujo colorido». Así el lector se imagina mejor lo que quieres decir. Y en vez de repetir «dijo, dijo, dijo» puedes usar «contó», «preguntó» o «gritó».",
        "Para cambiar una palabra, piensa qué quieres decir de verdad y busca otra que encaje. Después lee la frase de nuevo para comprobar que tiene sentido.",
    ],
    [("vocabulario", "las palabras que conozco y uso"), ("preciso", "que dice exactamente lo que se quiere decir"), ("variado", "con palabras diferentes y no repetidas"), ("sinónimo", "palabra que significa casi lo mismo que otra"), ("encajar", "quedar bien en la frase")],
    [
        ("Cambiar una palabra repetida", "Mejora: «Mi abuelo dijo un cuento. Después dijo otro. Luego dijo adiós».", ["Veo que «dijo» se repite tres veces.", "Busco palabras que digan más: contó, relató, se despidió."], "Mi abuelo contó un cuento. Después relató otro. Luego se despidió."),
        ("Cambiar «cosa» por una palabra precisa", "En «Vi una cosa grande en el patio. La cosa tenía cuatro patas y ladraba», ¿qué palabra precisa reemplaza «cosa»?", ["Las pistas son «cuatro patas» y «ladraba».", "El animal es un perro."], "Vi un perro grande en el patio. El perro tenía cuatro patas y ladraba."),
    ],
    [("Cambiar una palabra por otra que no encaja.", "Se elige una palabra solo porque suena difícil.", "Lee la frase de nuevo y comprueba que tenga sentido."), ("Usar siempre «bonito» para todo.", "Es la primera palabra que se viene a la cabeza.", "Piensa cómo es de verdad: colorido, suave, brillante, tranquilo.")],
    [
        E("¿Cuál palabra dice más: «cosa» o «mochila»?", "mochila", "«Mochila» nombra un objeto exacto."),
        E("En «Mi tía dijo hola y dijo chao», ¿qué palabra se repite?", "dijo", "Aparece dos veces."),
        E("¿Un vocabulario variado usa palabras iguales o diferentes?", "Diferentes", "Variado significa que no se repite siempre lo mismo."),
    ],
    [
        E("Elige la palabra más precisa para «La niña hizo un dibujo»: a) pintó b) hizo otra cosa.", "a", "«Pintó» dice mejor lo que hizo."),
        E("¿Qué palabra es más precisa para el animal de la granja que da leche y hace «mu»: «animal» o «vaca»?", "vaca", "Nombra exactamente al animal."),
        E("En vez de «dijo» al preguntar algo, ¿qué verbo puede ser mejor: «preguntó» o «escribió»?", "preguntó", "Una pregunta se dice con «preguntó»."),
    ],
    [
        E("Mejora «Es un paisaje bonito» usando una palabra más precisa entre: tranquilo, cosa, hecho.", "Es un paisaje tranquilo.", "«Tranquilo» describe mejor que «bonito» y encaja."),
        E("Cambia «dijo» por un verbo que exprese que habló muy fuerte: «Mi papá dijo desde el patio: ¡Ya voy!».", "gritó", "«Gritó» muestra la voz fuerte."),
        E("Reemplaza «cosa» en «Me regalaron una cosa para escribir» por una palabra exacta que sirva para escribir.", "lápiz (también sirve bolígrafo)", "Son objetos que sirven para escribir."),
    ],
    [
        E("Lee: «Fui a un lugar bonito y vi cosas bonitas». ¿Qué problema tiene el vocabulario?", "Repite «bonito» y usa «cosas», que no dice qué se vio", "Faltan palabras precisas y variadas."),
        E("Pedro cambió «caminó» por «voló» en «El niño caminó al colegio». ¿Encaja la nueva palabra?", "No", "Un niño no vuela al colegio, no tiene sentido."),
    ],
    [
        E("Mejora esta oración usando dos palabras distintas: «Me comí una cosa rica y la cosa estaba rica». Escribe una versión, por ejemplo con manzana y jugosa.", "Me comí una manzana jugosa y estaba dulce.", "Se cambia «cosa» por un nombre exacto y se varía «rica»."),
        E("¿Cuántas veces se repite «dijo» en «Dijo que sí, dijo que no y dijo que tal vez»?", "3", "Aparece tres veces."),
    ],
    [E("Estás escribiendo una nota para tu profesora: «Fui a un lugar bonito y vi una cosa bonita». Cambia las dos palabras repetidas por otras precisas. Por ejemplo, si fuiste a la playa y viste una concha.", "Fui a la playa y vi una concha brillante.", "Se cambia «lugar» por «playa», «cosa» por «concha» y se agrega una palabra exacta, «brillante».")],
    [
        E("¿Qué es un sinónimo?", "Una palabra que significa casi lo mismo que otra", "Los sinónimos ayudan a no repetir."),
        E("Para no repetir «grande», ¿sirve «enorme»?", "Sí", "«Enorme» significa muy grande."),
        E("Después de cambiar una palabra, ¿qué debo hacer?", "Releer la frase para ver si tiene sentido", "Así compruebo que la palabra encaja."),
    ],
    ("Mejora este borrador cambiando al menos tres palabras repetidas o poco precisas. Borrador: «Mi tío me dio una cosa bonita. Era una cosa bonita para dibujar. Dijo que me la regalaba y dijo que me cuidara». Puedes usar estas ideas: lápiz, colorido, entregó, aconsejó.",
     "Mi tío me regaló un lápiz colorido. Era un lápiz ideal para dibujar. Me lo entregó y me aconsejó que lo cuidara.",
     ["cambia al menos tres palabras", "las nuevas encajan", "el texto se entiende"], ["borrador mejorado con las palabras cambiadas subrayadas"], ["cambiar sin leer de nuevo", "dejar «cosa» sin cambio"],
     "Pide que lea la versión nueva en voz alta y diga qué palabra le gustó más y por qué."),
    "Escribe tres formas distintas de decir «grande» y úsalas en tres oraciones.",
    "Busca en un cuento dos verbos que reemplacen a «dijo» y anótalos con su oración.",
)

# ================================================================ OA 17 · clase 5
reg(
    OA17, 5,
    "Los textos de este cuaderno, lápiz y hoja. Ideal trabajar con un compañero o con alguien de la casa.",
    "Aprenderé a recibir y dar sugerencias de forma amable, sin cambiar el texto del otro. Sirve para mejorar mis textos con la ayuda de otros.",
    ["Sé revisar un borrador.", "Sé que un autor decide sobre su propio texto."],
    [
        "Otras personas pueden ayudarte a mejorar tu texto. Una sugerencia es una idea que alguien te da para que lo pienses. Puede venir de un compañero o de la profesora. Tú, como autor, decides si la usas o no.",
        "Para dar una sugerencia amable, primero di algo que te gustó. Después propón un cambio con palabras como «podrías» o «quizás». Por ejemplo: «Me gustó tu final. Podrías agregar el día en que pasó». No digas «está mal» ni escribas en el texto del otro.",
        "Para recibir una sugerencia, escucha con calma y da las gracias. Piensa si ayuda a cumplir tu propósito. Si sirve, la usas; si no, explicas por qué lo dejas igual. El texto sigue siendo tuyo.",
    ],
    [("sugerencia", "una idea para mejorar algo"), ("autor", "quien escribió el texto y decide cómo queda"), ("amable", "que trata bien a los demás"), ("opinar", "decir lo que pienso"), ("agradecer", "decir gracias")],
    [
        ("Dar una sugerencia amable", "Luis leyó el texto de Ana: «Mi perro Toby es chico. Toby come mucho». Luis cree que falta decir de qué color es. ¿Cómo puede sugerirlo?", ["Primero dice algo que le gustó: «Me gustó que cuentas cómo come Toby».", "Luego propone el cambio: «Podrías agregar de qué color es»."], "Me gustó cómo cuentas que come Toby. Podrías agregar de qué color es."),
        ("Decidir como autor", "Ana recibió la sugerencia de agregar el color de Toby. Ella piensa que sirve para imaginarlo mejor. ¿Qué hace?", ["Piensa si la sugerencia ayuda a su propósito.", "Decide usarla, agradece y escribe el color."], "Ana agradece y agrega: «Toby es café»."),
    ],
    [("Escribir directo en el texto del compañero.", "Se cree que corregir es cambiar lo del otro.", "Di la sugerencia y deja que el autor escriba."), ("Decir «Está mal».", "No se piensa cómo se sentirá el autor.", "Di algo que te gustó y luego «podrías…».")],
    [
        E("¿Quién decide si usar una sugerencia: el autor o el compañero?", "El autor", "El texto es del autor."),
        E("¿Qué se dice primero en una sugerencia amable: algo que gustó o un error?", "Algo que gustó", "Empezar con lo bueno ayuda a escuchar."),
        E("¿Con qué palabra puedo proponer un cambio: «podrías» o «debes»?", "Podrías", "«Podrías» es una forma amable de sugerir."),
    ],
    [
        E("¿Para qué sirve una sugerencia?", "Para pensar una forma de mejorar el texto", "Es una idea, no una orden."),
        E("Tomás escribió: «Fui al zoológico». Carla dice: «Qué mal escribes». ¿Es una sugerencia amable?", "No", "No dice nada útil y puede herir."),
        E("¿Cuál sugerencia es mejor: a) «Podrías contar qué animal te gustó más» o b) «Tu texto es aburrido»?", "a", "La a es amable y propone un cambio concreto."),
    ],
    [
        E("Texto de Pía: «Mi casa es azul». Escribe una sugerencia amable para que agregue dónde está su casa.", "Me gustó que cuentas el color. Podrías agregar dónde está tu casa.", "Empieza con algo bueno y propone un cambio."),
        E("Si una sugerencia ayuda a cumplir mi propósito, ¿la uso o no?", "La uso", "Mejora mi texto."),
        E("Ana recibe esta sugerencia: «Podrías poner el título». Ella lo agrega. ¿Qué dice después?", "Gracias", "Se agradece cuando alguien ayuda."),
    ],
    [
        E("Marcos no quiere cambiar el final porque su propósito es dejar un misterio. ¿Puede dejarlo igual?", "Sí, si explica por qué", "El autor decide si la sugerencia sirve a su propósito."),
        E("Rosa le sugiere a Eva: «Cambia tu texto por el mío». ¿Es una buena sugerencia?", "No", "No se debe reemplazar la voz del autor."),
    ],
    [
        E("Un compañero te dice: «Podrías agregar cuándo pasó». Tu texto es: «Fui a la plaza con mi papá». Escribe cómo queda con «el domingo».", "El domingo fui a la plaza con mi papá.", "Se agrega cuándo ocurrió."),
        E("De estas tres frases, ¿cuáles son sugerencias amables? 1) «Quizás podrías agregar un final.» 2) «Esto no sirve.» 3) «Me gustó tu inicio.» Responde con los números.", "1 y 3", "Son amables; la 2 critica sin ayudar."),
    ],
    [E("Una compañera lee tu texto «Mi gato come pescado» y te dice: «Me gustó que cuentas qué come. Podrías agregar su nombre». Responde como autor: ¿qué le dices y qué escribes?", "Gracias. Escribo: «Mi gato Mishi come pescado».", "Se agradece y se decide usar la idea.")],
    [
        E("Si no estoy de acuerdo con una sugerencia, ¿qué puedo hacer?", "Explicar con calma por qué la dejo igual", "El autor decide, pero respeta a quien ayuda."),
        E("¿Una sugerencia es una orden?", "No", "Es una idea para pensar."),
        E("¿Qué hace un buen revisor con el texto del compañero: escribe en él o conversa?", "Conversa", "El texto sigue siendo del autor."),
    ],
    ("Lee este texto de un compañero y escribe una sugerencia amable de dos oraciones (algo que te gustó + algo que podría agregar). Texto: «Ayer fui a la casa de mi tío. Jugamos con su perro. Fue divertido». Después imagina que eres el autor y escribe cómo cambiarías el texto si usas tu sugerencia.",
     "Me gustó que cuentas con quién jugaste. Podrías agregar cómo se llama el perro. Cambio: «Jugamos con su perro Bruno».",
     ["empieza con algo positivo", "usa «podrías» o «quizás»", "el cambio sugerido es concreto"], ["dos oraciones de sugerencia y el texto con el cambio"], ["decir «está mal»", "reescribir todo el texto del compañero"],
     "Pregunta: «¿Qué le diste primero, algo bueno o el cambio?». Recuerda que el autor decide."),
    "Pídele a alguien de tu casa una sugerencia para un texto tuyo y anótala.",
    "Escribe tres frases amables para sugerir cambios a un texto.",
)

# ================================================================ OA 17 · clase 6
reg(
    OA17, 6,
    "Un borrador revisado de este cuaderno, lápiz y hoja limpia para pasar en limpio.",
    "Aprenderé a editar mi texto para publicarlo: corregir concordancia, ortografía y presentación. Sirve para que otros lo lean sin dificultad.",
    ["Sé releer y mejorar mi borrador.", "Sé usar mayúsculas y puntos."],
    [
        "Editar es dejar el texto listo para que otros lo lean. Cuando ya revisaste las ideas, miras los detalles: la concordancia, la ortografía y la presentación. Después lo pasas en limpio.",
        "La concordancia es que las palabras coincidan en género y número. Se dice «los gatos pequeños», no «los gato pequeño». La ortografía es escribir bien las letras, como «hoy» y «quiero». La presentación es la letra clara, un título y márgenes ordenados.",
        "Para editar, usa una lista: ¿mayúsculas y puntos?, ¿palabras que concuerdan?, ¿palabras bien escritas?, ¿letra clara y título? Marca cada cosa cuando la compruebas.",
    ],
    [("editar", "corregir detalles para dejar el texto listo"), ("concordancia", "que las palabras coincidan en género y número"), ("ortografía", "escribir las palabras con las letras correctas"), ("presentación", "cómo se ve el texto: letra, título y orden"), ("publicar", "mostrar el texto a otros")],
    [
        ("Corregir la concordancia", "Edita: «Los niño juegan con las pelota roja».", ["Reviso «los niño»: «los» es plural, así que es «los niños».", "Reviso «las pelota roja»: las pelotas rojas."], "Los niños juegan con las pelotas rojas."),
        ("Corregir ortografía y mayúscula", "Edita: «ayer qeriamos ir al parque». Corrige.", ["La oración empieza con mayúscula: Ayer.", "El sonido «k» antes de la e se escribe «que», y «queríamos» lleva tilde en la «í»."], "Ayer queríamos ir al parque."),
    ],
    [("Pasar en limpio sin revisar la concordancia.", "Se piensa que ya está listo.", "Usa una lista de edición antes de copiar."), ("Hacer letra muy pequeña o apretada.", "Se quiere escribir rápido.", "Escribe con letra clara y deja espacio entre líneas.")],
    [
        E("Editar, ¿es dejar el texto listo para otros o escribir un texto nuevo?", "Dejar el texto listo para otros", "Se corrigen detalles para publicar."),
        E("Cuál tiene concordancia: a) «los perros grande» o b) «los perros grandes»", "b", "Perros y grandes están en plural."),
        E("¿Qué parte de la edición revisa la letra clara y el título?", "La presentación", "Habla de cómo se ve el texto."),
    ],
    [
        E("¿Qué se revisa en la ortografía?", "Que las palabras tengan las letras correctas", "Escribir bien las palabras."),
        E("En «la flores rojas», ¿cuál palabra no concuerda?", "la", "Debe decir «las flores rojas»."),
        E("¿Cuál es correcta: «tengo un gato blancos» o «tengo un gato blanco»?", "Tengo un gato blanco", "Un gato y blanco están en singular."),
    ],
    [
        E("Edita sin cambiar la palabra «niñas»: «los niñas juegan».", "Las niñas juegan.", "«Niñas» es femenino plural, así que lleva «las»."),
        E("Edita: «mi abuela cocina empanadas». ¿Qué falta?", "Mayúscula inicial y punto: Mi abuela cocina empanadas.", "Una oración empieza con mayúscula y termina con punto."),
        E("Edita la ortografía de «kiero un helado»: ¿cómo se escribe «quiero»?", "quiero", "El sonido «k» antes de la «i» se escribe «qu»: quiero."),
    ],
    [
        E("Un niño dice: «Pasé mi texto en limpio sin revisarlo». ¿Qué riesgo hay?", "Que queden errores en la copia final", "Se pasa el texto sin corregir."),
        E("¿Por qué conviene mirar primero las ideas y después los detalles?", "Porque si cambio las ideas, tendría que corregir los detalles de nuevo", "Revisar primero las ideas ahorra trabajo."),
    ],
    [
        E("Edita: «los gato duerme en las casa». Escríbelo bien.", "Los gatos duermen en las casas.", "Hay que ajustar el número en cada palabra."),
        arith("Un texto tiene 4 cosas por revisar (mayúsculas y puntos, concordancia, ortografía, presentación). Ya revisaste 3. ¿Cuántas faltan?", "4-3", "Faltan las que no has comprobado."),
    ],
    [E("Vas a publicar este aviso en la sala: «el viernes traiga un libro para la feria». Edita mayúscula, punto y escribe «traigan» en plural porque habla a todos.", "El viernes traigan un libro para la feria.", "Se corrige mayúscula, punto y verbo en plural.")],
    [
        E("¿Qué hago después de editar: lo paso en limpio o lo tiro?", "Lo paso en limpio", "Es el paso final antes de publicar."),
        E("¿Una lista de edición ayuda a no olvidar nada?", "Sí", "Permite marcar cada cosa que revisé."),
        E("¿Qué debe tener un buen título: ser claro o muy largo?", "Ser claro", "Dice de qué trata el texto."),
    ],
    ("Edita este texto con la lista (mayúsculas y puntos, concordancia, ortografía, presentación) y escribe la versión final con título. Texto: «mi amiga y yo juegan a la pelota en el patio nos gustaron mucho los juegos». Son dos oraciones y el verbo «juegan» no concuerda con «mi amiga y yo».",
     "Título: El patio y la pelota. Mi amiga y yo jugamos a la pelota en el patio. Nos gustaron mucho los juegos.",
     ["corrige concordancia", "usa mayúsculas y puntos", "agrega un título y letra clara"], ["texto final en limpio con título"], ["olvidar el título", "dejar «juegan» sin corregir"],
     "Pide que marque cada punto de la lista a medida que lo revisa. Si pasó por alto algo, señala la línea, no el error."),
    "Edita una carta corta que hayas escrito antes con la lista de edición.",
    "Haz tu propia lista de edición de cinco puntos y úsala con un texto.",
)
