"""Cuaderno del estudiante, 8.º básico Inglés (propuesta): EN08 OA 13, clases 4 y 5 (editar con diccionario y procesador de textos; publicar).

Las entradas de diccionario y los textos son originales y breves, con pista en español. Los títulos de clase del plan
son genéricos; aquí cada clase aplica un paso del proceso de escritura.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA13 = "EN08 OA 13"


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ================================================================ clase 4: editar
lesson(
    OA13, 4,
    "Los textos y las entradas de diccionario escritos en cada ejercicio, lápiz y una hoja. Un computador es opcional.",
    "Aprenderé a editar un texto: corregir ortografía, mayúsculas y puntuación, con los dos puntos incluidos, y a usar un diccionario en línea y el corrector de un procesador de textos. Sirve para que el texto final sea claro y correcto.",
    ["Sé revisar un borrador con una lista de preguntas.", "Conozco el uso del punto, la coma y las mayúsculas."],
    [
        "Editar es el paso que viene después de revisar. Se corrige la ortografía (spelling), las mayúsculas (los días, los meses, los idiomas y el comienzo de cada oración) y la puntuación. Palabras de uso frecuente que suelen escribirse mal: because (no «becouse»), friend (no «freind»), beautiful (no «beutiful»), library (no «libary»), Wednesday y together. Cuidado con their (de ellos: their books) y there (allí o hay: there are two books).",
        "Los dos puntos (colon) se escriben después de una oración completa para anunciar una lista o una explicación: We need three things: a pen, a ruler and a notebook. There is one problem: the bin is full. No se escriben justo después de un verbo, como en «We visited: the museum». Dentro de la lista, los elementos se separan con comas.",
        "El diccionario en línea muestra para cada palabra su categoría (noun = sustantivo, verb = verbo, adjective = adjetivo), su significado y una oración de ejemplo. Elige el significado que calza con tu oración. El procesador de textos subraya en rojo las palabras mal escritas y ofrece sugerencias, pero no siempre detecta la palabra equivocada si está bien escrita, por ejemplo there en vez de their. Revisa tú también.",
    ],
    [("edit", "editar: corregir ortografía, mayúsculas y puntuación"), ("spelling", "ortografía"), ("colon", "dos puntos (:)"), ("dictionary entry", "entrada de diccionario: palabra, categoría, significado y ejemplo"), ("noun / verb / adjective", "sustantivo / verbo / adjetivo"), ("spellcheck", "corrector ortográfico"), ("capital letter", "letra mayúscula"), ("their / there", "de ellos / allí o hay")],
    [
        ("Corregir la ortografía", "Corrige: «My freind has a beutiful libary.»", ["Busca las palabras de uso frecuente mal escritas.", "freind pasa a friend, beutiful a beautiful, libary a library.", "Reescribe la oración completa."], "My friend has a beautiful library."),
        ("Poner dos puntos en una lista", "Agrega los signos que faltan: «We need three things a pen a ruler and a notebook.»", ["Los dos puntos van después de la oración completa.", "Los elementos de la lista se separan con comas.", "Queda We need three things: a pen, a ruler and a notebook."], "We need three things: a pen, a ruler and a notebook."),
    ],
    [
        ("Escribir «We visited: the museum, the park and the zoo».", "Los dos puntos no van justo después de un verbo.", "Escribe We visited three places: the museum, the park and the zoo."),
        ("Aceptar siempre lo que sugiere el corrector.", "El corrector no ve si la palabra, bien escrita, es la equivocada.", "Lee cada sugerencia y comprueba si calza con tu oración."),
    ],
    [
        ("Elige la ortografía correcta: A) friend B) freind", "A", "Friend se escribe f-r-i-e-n-d, con ie después de la r."),
        ("¿Qué oración usa bien los dos puntos? A) I need three things: a pen, a ruler and a notebook. B) I need: three things a pen.", "A", "Los dos puntos van después de una oración completa y anuncian la lista."),
        ("Escribe con mayúsculas donde corresponda: «on monday we have english». Copia las tres palabras que necesitan mayúscula, separadas por comas.", "On, Monday, English", "Se escribe con mayúscula el comienzo de la oración, el día y el idioma."),
    ],
    [
        ("Entrada de diccionario: «borrow (verb): to take something from someone and give it back later. Example: I borrow books from the library.» ¿Qué significa borrow? A) Pedir prestado B) Regalar", "A", "La definición dice tomar algo y devolverlo después."),
        ("El corrector sugiere cambiar «their» por «there» en «The students lost their books.» ¿Qué palabra es correcta? A) their B) there", "A", "Their significa de ellos: los libros son de los estudiantes. There indica un lugar o hay."),
        ("Entrada: «beautiful (adjective): very nice to look at.» ¿Qué categoría tiene beautiful? A) Adjetivo B) Verbo", "A", "La entrada lo marca como adjective."),
    ],
    [
        ("Corrige las palabras mal escritas: «Becouse the library is quiet, my freind studies there.»", "Because the library is quiet, my friend studies there.", "Las dos palabras frecuentes se escriben because y friend."),
        ("Agrega los dos puntos: «There is one problem the bin is full.»", "There is one problem: the bin is full.", "Los dos puntos anuncian la explicación."),
        ("Agrega mayúsculas y punto final: «on friday we visited the library»", "On Friday we visited the library.", "Se escribe con mayúscula el comienzo y el día, y se cierra con punto."),
    ],
    [
        ("¿Qué oración está bien? A) We visited: the museum, the park and the zoo. B) We visited three places: the museum, the park and the zoo.", "B", "Los dos puntos van después de una oración completa."),
        ("El corrector no subraya «there» en «The students lost there books». ¿Por qué puede haber un error? A) La palabra está bien escrita pero es la equivocada para ese sentido B) El programa está roto", "A", "Para el sentido de la oración debía ser their."),
    ],
    [
        ("Entradas: «light (noun): what makes things visible» y «light (adjective): not heavy». En «My backpack is light today.», ¿qué entrada corresponde? A) light (noun) B) light (adjective)", "B", "En la oración describe cuánto pesa la mochila."),
        ("Escribe la oración corregida: «There are three clubs chess art and music.» (usa dos puntos y comas)", "There are three clubs: chess, art and music.", "Después de la oración completa van los dos puntos y la lista se separa con comas."),
    ],
    [("Revisas el afiche final de la feria. ¿Qué línea está bien editada? A) We have three clubs: chess, art and music. B) We have: three clubs chess, art and music.", "A", "Los dos puntos van tras la oración completa y la lista lleva comas.")],
    [
        ("¿Qué se corrige al editar?", "Ortografía, mayúsculas y puntuación", "Esto viene después de revisar las ideas."),
        ("¿Para qué sirven los dos puntos?", "Para anunciar una lista o una explicación", "Se escriben después de una oración completa."),
        ("¿Qué muestra una entrada de diccionario?", "Categoría, significado y ejemplo", "Ayuda a elegir el sentido correcto."),
    ],
    task("Lee este encargo: edita en tu hoja este texto con errores. «on wednesday our class visited the libary. we saw many books and my freind borrowed three things a novel a dictionary and a comic. the librarian was very nice becouse she helped us.» Corrige la ortografía, las mayúsculas, los dos puntos y las comas, y anota cuántos errores corregiste.", "On Wednesday our class visited the library. We saw many books and my friend borrowed three things: a novel, a dictionary and a comic. The librarian was very nice because she helped us.", ["corrige palabras como library, friend y because", "pone mayúsculas al inicio de las oraciones y en Wednesday", "usa dos puntos y comas en la lista"], ["hoja con el texto corregido"], ["dejar los dos puntos después de un verbo", "confiar solo en el corrector"], "Pide a una persona de tu casa que lea tu texto corregido y busque algún error que se te haya pasado."),
    "Escribe una lista de diez palabras de uso frecuente y comprueba su ortografía con un diccionario.",
    "Busca en un diccionario una palabra con dos significados y escribe una oración para cada uno.",
)

# ================================================================ clase 5: publicar y escribir de forma independiente
lesson(
    OA13, 5,
    "Los textos y las listas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a publicar un texto: preparar la versión final, elegir un formato y compartirlo con cuidado. Sirve para presentar un texto a una audiencia real sin exponer datos personales y para repetir todo el proceso de escritura de forma independiente.",
    ["Conozco los pasos de organizar, redactar, revisar y editar.", "Sé qué son un título y un pie de foto."],
    [
        "Publicar (publish) es compartir la versión final con una audiencia. Antes de hacerlo, prepara una copia limpia: título, texto sin errores, nombre del autor y, si hay imágenes, con su pie de foto y su crédito (por ejemplo, Photo: Class 8B). Elige el formato según quien lo leerá: un afiche para el pasillo, una revista del curso para las familias o un blog del colegio.",
        "Publica con cuidado. Nunca pongas datos personales, como tu apellido completo, tu dirección o tu teléfono. Firma solo con tu nombre y curso: By Mateo, 8C. No publiques fotos de otras personas sin su permiso y el de sus familias. Un procesador de textos ayuda a dar formato: títulos más grandes, párrafos separados y una letra legible.",
        "Escribir de forma independiente es hacer todos los pasos por tu cuenta: organizar ideas, redactar, revisar, editar y publicar. Usa una lista final de comprobación: 1) título; 2) texto claro y sin errores; 3) nombre del autor sin datos personales; 4) imagen con pie de foto y crédito. Cuenta cuántos puntos cumples antes de publicar.",
    ],
    [("publish", "publicar: compartir la versión final"), ("final copy", "copia final: versión limpia y corregida"), ("title", "título"), ("byline", "firma: By + nombre del autor"), ("credit", "crédito: quién hizo la imagen"), ("permission", "permiso"), ("format", "formato: afiche, revista o blog"), ("audience", "audiencia: quienes leerán el texto")],
    [
        ("Escribir la firma sin datos personales", "Eres Mateo, del curso 8C. Escribe la firma que publicarías con tu texto, usando By.", ["La firma lleva solo el nombre y el curso.", "No lleva apellido ni dirección.", "Queda By Mateo, 8C."], "By Mateo, 8C"),
        ("Contar los puntos de la lista final", "Lista: título sí, texto sin errores sí, firma sí, imagen con pie de foto no. ¿Cuántos de los 4 puntos se cumplen?", ["Cuenta los síes.", "Título, texto y firma son tres.", "La imagen no cumple."], "3"),
    ],
    [
        ("Publicar con apellido completo y dirección.", "Expone datos personales que no se deben compartir.", "Firma solo con tu nombre y curso."),
        ("Publicar sin editar el texto.", "Los errores confunden y restan seriedad.", "Termina de editar antes de compartir."),
    ],
    [
        ("Publicar significa A) compartir la versión final B) escribir el primer borrador", "A", "Es el último paso del proceso."),
        ("¿Qué dato no se debe publicar en un blog del curso? A) La dirección de tu casa B) El título de tu texto", "A", "Es un dato personal."),
        ("Una copia final tiene A) título y texto claro B) palabras tachadas", "A", "La copia final está limpia y presentada."),
    ],
    [
        ("El texto es para las familias del curso. ¿Qué formato llega mejor a ellas? A) Una revista impresa del curso B) Una nota en la pizarra de la sala", "A", "La familia puede llevarla a casa; la pizarra se borra."),
        ("¿Qué firma evita datos personales? A) By Ana, 8B B) By Ana Pérez, Calle Los Aromos 123", "A", "Solo lleva el nombre de pila y el curso."),
        ("¿Para qué sirve el crédito «Photo: Class 8B»? A) Muestra quién hizo la imagen B) Oculta quién la hizo", "A", "Reconoce a quienes hicieron la foto."),
    ],
    [
        ("¿Qué paso va justo antes de publicar? Responde con el nombre del paso en español.", "Editar", "El orden es organizar, redactar, revisar, editar y publicar."),
        ("Lista de comprobación final: título sí, texto sin errores no, firma sí, imagen con pie de foto sí. ¿Cuántos puntos se cumplen de 4?", "3", "Falla solo el texto sin errores."),
        ("Escribe la firma de Sofía, del curso 8A, usando By y sin apellido.", "By Sofía, 8A", "La firma lleva el nombre y el curso."),
    ],
    [
        ("Quieres publicar en un sitio abierto una foto de tus compañeros. ¿Qué haces primero? A) Pedir permiso a ellos y a sus familias B) Publicarla rápido", "A", "Es necesario tener permiso antes de compartir imágenes de otras personas."),
        ("¿Por qué se edita antes de publicar? A) Los lectores entienden mejor un texto sin errores B) Para que el texto sea más largo", "A", "Los errores dificultan la lectura."),
    ],
    [
        ("Marta hizo esto: 1) anotó una lista de ideas y un esquema, 2) escribió el texto completo, 3) agregó una razón y quitó una oración fuera del tema, 4) corrigió «becouse» y puso dos puntos. ¿Cuál es el único paso del proceso que aún no hizo?", "Publicar", "Ya organizó, redactó, revisó y editó."),
        ("Marta agregó una razón a su texto y quitó una oración que no iba con el tema. ¿Cómo se llama ese paso del proceso? Responde con una palabra en español.", "Revisar", "Mejoró las ideas y el contenido del texto."),
    ],
    [("El afiche de la feria de tu curso necesita título, un texto breve del curso 8C y una foto. ¿Qué afiche sigue los criterios de publicación? A) Título, texto final claro, firma «By Class 8C» y foto con pie de foto B) Borrador con palabras tachadas y sin título", "A", "Cumple con la copia final, la firma sin datos personales y la imagen con pie de foto.")],
    [
        ("¿Cuál es el último paso del proceso de escritura?", "Publicar", "Se comparte la versión final."),
        ("¿Con qué datos se firma un texto publicado?", "Nombre y curso", "Sin apellido, dirección ni teléfono."),
        ("¿Qué se necesita para publicar la foto de otra persona?", "Su permiso", "Y el de su familia."),
    ],
    task("Lee este encargo: haz todo el proceso por tu cuenta con este tema: «A place I like in my neighbourhood» (un lugar que me gusta de mi barrio). Escribe en hojas separadas el propósito y el esquema, el borrador de seis a ocho oraciones, la lista de cambios al revisar y editar, y la copia final con título, firma sin datos personales y un dibujo con pie de foto. Cuenta al final cuántos de los cuatro puntos de la lista de comprobación cumples.", "Title: My Favourite Park. Purpose: inform. Final copy: My Favourite Park. There is a park near my house. It is small but clean. It has two big trees, a blue slide and four benches. Children play there after school. I go there once a week because it is quiet. I think it is a good place for everyone. By Mateo, 8C. Caption: The blue slide in the park. Drawing: Mateo.", ["tiene propósito, esquema, borrador, cambios y copia final", "la firma no tiene datos personales", "cumple los cuatro puntos de la lista de comprobación"], ["conjunto de hojas con todos los pasos y la copia final"], ["saltarse el esquema o la edición", "firmar con apellido y dirección"], "Muestra tu copia final a una persona de tu casa y pregunta si entiende el texto sin que se lo expliques."),
    "Escribe en una hoja los cinco pasos del proceso y una frase que diga qué haces en cada uno.",
    "Elige un formato distinto (afiche, revista o blog) para el mismo texto y explica cómo cambia la presentación.",
)
