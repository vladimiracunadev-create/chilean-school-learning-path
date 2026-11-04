"""Cuaderno del estudiante, 1.º medio Inglés (propuesta): EN1M OA 13, proceso de escritura independiente: organizar, redactar, revisar, editar y publicar.

Todos los textos en inglés son originales, breves y ficticios, con pista en español. Los títulos de clase del plan son
genéricos; aquí cada clase trabaja un paso del proceso: organizar ideas, redactar con variedad de palabras y conectores,
revisar y editar, ortografía y apóstrofe, y publicar con procesador de textos y diccionario en línea. Todo se puede
hacer también a mano; las herramientas digitales se describen dentro de la clase. Sin audio ni material externo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA13 = "EN1M OA 13"


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


# ================================================================ clase 1: organizar ideas
lesson(
    OA13, 1,
    "Los temas, ideas y esquemas escritos en cada ejercicio, lápiz y una hoja. Sin materiales especiales.",
    "Aprenderé a organizar ideas antes de escribir: fijar el propósito y la audiencia, reunir ideas, descartar las que no sirven y armar un esquema. Sirve para que el texto tenga orden y no se mezclen ideas.",
    ["Sé escribir oraciones simples y párrafos cortos en inglés.", "Conozco los propósitos de informar, explicar, opinar y narrar."],
    [
        "El proceso de escritura (writing process) tiene cinco pasos: organizar ideas, redactar (draft), revisar, editar y publicar. Esta clase trabaja el primero. Antes de escribir define el propósito (purpose): informar (dar datos), explicar (cómo o por qué), expresar una opinión o narrar (contar una historia). Define también la audiencia (audience, quién lee), porque cambia las palabras y el tono.",
        "Después reúne ideas con una lluvia de ideas (brainstorm): anota todo lo que se te ocurre, en palabras sueltas. Puedes hacer un mapa de ideas (mind map): el tema va en el centro y las ideas alrededor. Luego elimina las que no pertenecen al tema y agrupa las que se repiten. Por último arma un esquema (outline): una oración de tema (topic sentence) que presenta la idea central, de dos a cuatro puntos con detalles de apoyo (supporting details) y una conclusión.",
        "Modelo. Tema: a quiet corner in school. Propósito: opinar. Audiencia: la directora. Lluvia de ideas: students can read; it is calm; I like blue chairs; it helps students focus; the bus is late. Tras eliminar lo que no pertenece (the bus is late) y lo poco relevante (I like blue chairs), el esquema queda: Topic sentence: A quiet corner would help students. Point 1: they can read. Point 2: it is calm, so they can focus. Conclusion: we should create one.",
    ],
    [("writing process", "proceso de escritura: organizar, redactar, revisar, editar y publicar"), ("purpose", "propósito: para qué escribes"), ("audience", "audiencia: quién va a leer"), ("brainstorm", "lluvia de ideas: anotar todo lo que se te ocurre"), ("mind map", "mapa de ideas con el tema al centro"), ("outline", "esquema: plan ordenado del texto"), ("topic sentence", "oración de tema: presenta la idea central"), ("supporting detail", "detalle de apoyo")],
    [
        ("Descartar una idea que no pertenece", "Tema: Benefits of exercise. Ideas: it gives energy; it helps sleep; my cousin lives in Temuco; it improves mood. ¿Qué idea no pertenece al tema?", ["Cada idea debe hablar de los beneficios del ejercicio.", "Las tres primeras lo hacen.", "Falta relación en my cousin lives in Temuco."], "my cousin lives in Temuco"),
        ("Elegir el propósito", "Quieres contar a tu curso qué pasó en un paseo ficticio. ¿Cuál es tu propósito: informar, explicar, opinar o narrar?", ["Cuentas hechos en orden.", "Es una historia de lo ocurrido.", "El propósito es narrar."], "narrar"),
    ],
    [
        ("Empezar a redactar sin pensar el propósito.", "Se piensa que organizar es una pérdida de tiempo.", "Escribe primero propósito y audiencia: así sabrás qué incluir."),
        ("Dejar en el esquema todas las ideas de la lluvia de ideas.", "Se cree que cuantas más ideas, mejor texto.", "Elimina las que no pertenecen al tema y agrupa las repetidas."),
    ],
    [
        ("¿Cuál es el primer paso del proceso de escritura? A) organizar ideas B) publicar", "A", "Antes de redactar se organiza lo que se va a decir."),
        ("Escribirás qué hiciste el sábado. ¿Qué propósito es? A) narrar B) opinar", "A", "Cuentas hechos en orden: narrar."),
        ("Un mapa de ideas es A) el tema en el centro con ideas alrededor B) la copia final del texto", "A", "Sirve para ver ideas antes de escribir."),
    ],
    [
        ("«Dear mayor, I think the park needs more bins because it is dirty.» ¿Qué propósito tiene? A) informar B) expresar una opinión C) narrar", "B", "I think y la petición muestran un juicio personal."),
        ("Tema: Benefits of reading. Ideas: improves vocabulary; helps you relax; my pencil case is red; gives new ideas. ¿Qué idea no pertenece?", "my pencil case is red", "No habla de los beneficios de leer."),
        ("Debes escribir para un niño de 7 años. ¿Qué conviene usar? A) palabras simples y oraciones cortas B) vocabulario técnico y oraciones largas", "A", "La audiencia determina el nivel de las palabras."),
    ],
    [
        ("Ordena las partes de un esquema y escribe las letras en orden: a) Conclusion b) Topic sentence c) Point 1 d) Point 2", "b, c, d, a", "Se parte con la oración de tema y se cierra con la conclusión."),
        arith("Un esquema tiene 1 oración de tema, 3 puntos con 2 detalles cada uno y 1 conclusión. ¿Cuántas líneas tiene en total?", "1+3+3*2+1", "Se suman la oración de tema, los puntos, los detalles y la conclusión."),
        ("Puntos del esquema: grow vegetables; share the work; learn to wait. ¿Qué oración de tema los cubre a los tres? A) School gardens teach food and teamwork B) I like gardens.", "A", "Resume los tres puntos y no solo una preferencia."),
    ],
    [
        ("Esquema para informar sobre una salida: date: Friday; place: science museum; cost: $3.000; my favourite colour is blue. ¿Qué idea sobra?", "my favourite colour is blue", "No es un dato de la salida."),
        ("Texto para los apoderados en el sitio del colegio. ¿Qué tono corresponde? A) formal, con fechas completas B) con apodos y bromas", "A", "Los apoderados son una audiencia formal."),
    ],
    [
        arith("Una lluvia de ideas trae 9 ideas: 2 no pertenecen al tema y 3 repiten otras ideas. ¿Cuántas ideas distintas y pertinentes quedan?", "9-2-3", "Se restan las ideas que no sirven."),
        ("Esquema. Topic sentence: Our school needs more bike racks. Point 1: 40 students ride bikes. Point 2: racks protect bikes. Conclusion: we should buy them. ¿Qué propósito sugiere? A) explicar un proceso B) expresar una opinión", "B", "Needs y should muestran una postura personal."),
    ],
    [("La radio escolar ficticia necesita un texto para informar a los estudiantes sobre un taller. Notas: club meets Tuesday; it is free; bring a pencil; my dog is called Rocky. ¿Qué idea no va en el texto? A) bring a pencil B) my dog is called Rocky", "B", "No es un dato del taller.")],
    [
        ("¿Qué cuatro propósitos vimos?", "Informar, explicar, opinar y narrar", "Son los propósitos de la clase."),
        ("¿Qué hace la oración de tema?", "Presenta la idea central", "Va al comienzo del esquema."),
        ("¿Qué haces con las ideas repetidas?", "Las agrupas", "Se junta lo repetido en una sola."),
    ],
    task("Lee este encargo: tu curso quiere pedir a la dirección más tiempo de recreo. Propósito: opinar. Audiencia: la directora. Ideas de ejemplo: students are tired after 90 minutes; they can play and talk; more exercise helps focus; my backpack is blue; some teachers agree. Escribe en una hoja el propósito y la audiencia, tacha lo que no pertenece, y arma un esquema con oración de tema, dos puntos con detalle y una conclusión.", "Purpose: opinion. Audience: the principal. Crossed out: my backpack is blue. Topic sentence: A longer break would help students. Point 1: they are tired after 90 minutes. Point 2: exercise helps them focus. Conclusion: we ask for ten more minutes.", ["escribe propósito y audiencia", "elimina las ideas que no pertenecen", "arma un esquema con oración de tema, puntos y conclusión"], ["hoja con propósito, audiencia, ideas tachadas y esquema"], ["dejar todas las ideas", "no tener oración de tema"], "Muestra tu esquema a una persona de tu casa y pregunta qué punto le parece más fuerte."),
    "Haz una lluvia de ideas de seis palabras sobre tu deporte favorito y tacha dos.",
    "Cambia la audiencia del esquema a un niño de 7 años y reescribe la oración de tema con palabras más simples.",
)

# ================================================================ clase 2: redactar con variedad
lesson(
    OA13, 2,
    "Los esquemas, borradores y listas de palabras escritos en cada ejercicio, lápiz y una hoja. Un computador es opcional.",
    "Aprenderé a redactar un primer borrador con variedad de palabras, oraciones y conectores. Sirve para que el texto no repita siempre las mismas palabras y que las ideas queden unidas.",
    ["Conozco el esquema con oración de tema y puntos.", "Sé usar because, but y and."],
    [
        "El borrador (draft) es la primera versión completa del texto. Se escribe siguiendo el esquema, sin detenerse a corregir cada detalle de ortografía. Cada párrafo trae una oración de tema y de dos a cuatro oraciones de apoyo. Para que el texto sea rico, mezcla palabras de uso frecuente (good, big, said) con otras menos frecuentes (excellent, huge, replied), siempre que conozcas su significado exacto.",
        "Los conectores (connectors) unen las ideas y le dicen al lector qué relación hay: because y so expresan causa y resultado (It rained, so we stayed home); however y but expresan contraste (The ticket is cheap. However, the trip is long); although (aunque) también contrasta, pero no se usa junto con but (Although it was cold, we went out); also e in addition suman información; for example introduce un ejemplo; first, then y finally ordenan una secuencia. Cuida que cada conector tenga una coma cuando abre la oración: However, … For example, …",
        "También varía las oraciones: alterna cortas y largas, y no empieces todas con el mismo sujeto. Compara «I went to the market. I bought apples. I bought pears.» con «On Saturday I went to the market, where I bought apples and pears». Al terminar el borrador no lo mires como definitivo: lo revisarás después. Aquí el propósito (purpose) es dejar las ideas del esquema por escrito, con orden y con conectores.",
    ],
    [("draft", "borrador: primera versión completa del texto"), ("connector", "conector: palabra que une ideas"), ("however", "sin embargo (contraste)"), ("although", "aunque (contraste; sin but)"), ("for example", "por ejemplo"), ("in addition", "además"), ("so", "así que (resultado)"), ("excellent / huge", "excelente / enorme (palabras menos frecuentes)"), ("replied", "respondió")],
    [
        ("Elegir el conector de contraste", "Completa: «The museum is interesting. ___, the tickets are expensive.» Opciones: However / In addition.", ["La segunda idea se opone a la primera.", "Para un contraste se usa However.", "Queda However."], "However"),
        ("Cambiar una palabra repetida", "Frase: «The mountain was big and the lake was big.» Reemplaza el primer big por huge y escribe la frase completa.", ["Se cambia solo el primer big.", "Huge es una palabra menos frecuente que big.", "Queda: The mountain was huge and the lake was big."], "The mountain was huge and the lake was big."),
    ],
    [
        ("Repetir good tres veces seguidas en tres oraciones.", "Se usan solo palabras frecuentes que ya conocemos.", "Cambia una por excellent o wonderful."),
        ("Poner un conector sin coma al empezar: «However the tickets are expensive».", "Se olvida la coma después de un conector inicial.", "Se escribe However, the tickets are expensive."),
    ],
    [
        ("Because expresa A) causa B) contraste", "A", "Because explica la razón de algo."),
        ("However expresa A) contraste B) ejemplo", "A", "Introduce una idea que se opone a la anterior."),
        ("¿Cuál es una palabra menos frecuente que big? A) huge B) nice", "A", "Huge significa muy grande; nice no se refiere al tamaño."),
    ],
    [
        ("Completa con un conector de contraste: «I like football. ___, I prefer swimming.» Opciones: However / Because.", "However", "La segunda idea contrasta con la primera."),
        ("For example introduce A) un ejemplo B) una conclusión", "A", "Se usa para dar un caso concreto."),
        ("¿Qué palabra menos frecuente puede reemplazar a good en «The soup was good»? A) excellent B) bad", "A", "Excellent es menos frecuente y de sentido parecido; bad significa lo contrario."),
    ],
    [
        ("Completa: «The bus was late, ___ we walked.» (resultado)", "so", "So introduce el resultado de que el bus llegó tarde."),
        ("Completa para ordenar: «___, mix the flour and the eggs. Then bake it for 20 minutes.»", "First", "First abre la secuencia que sigue con then."),
        ("Une las ideas: «It was raining» y «we played football». ¿Qué opción es correcta? A) Although it was raining, we played football B) Although it was raining, but we played football.", "A", "Although no se combina con but en la misma oración."),
    ],
    [
        ("Texto: «The film was good. The actors were good. The music was good.» ¿Qué cambio mejora más el borrador? A) Reemplazar dos good por excellent y wonderful B) Agregar una cuarta oración con good", "A", "Varía las palabras; la otra opción repite más good."),
        ("Borrador: «I went to the market. I bought apples. I bought pears. I walked home.» ¿Qué problema tiene? A) Todas las oraciones empiezan igual B) Tiene faltas de ortografía", "A", "Las cuatro empiezan con I y no hay variedad."),
    ],
    [
        ("Une las dos oraciones con because: «Ana slept early. She was tired.» A) Ana slept early because she was tired B) Ana was tired because she slept early.", "A", "Estar cansada es la causa y dormir temprano es el resultado."),
        ("Completa con el conector: «The tickets are cheap. ___, many students cannot go because it is far.» A) However B) For example", "A", "La segunda idea se opone a la primera."),
    ],
    [("Un blog escolar ficticio tiene dos borradores sobre la biblioteca. Borrador 1: «The library is open until 6. It has many books. It has quiet tables.» Borrador 2: «The library is open until 6, so students can study after class. It also has many books and quiet tables.» ¿Cuál tiene más variedad y conectores? A) El borrador 1 B) El borrador 2", "B", "Usa so y also, y alterna ideas en oraciones más largas.")],
    [
        ("¿Qué conector sirve para dar un ejemplo?", "For example", "Introduce un caso concreto."),
        ("¿Qué se escribe después de However al comienzo de una oración?", "Una coma", "Separa el conector del resto."),
        ("¿Qué puedes cambiar si repites big muchas veces?", "Una palabra menos frecuente", "Por ejemplo huge o enormous."),
    ],
    task("Lee este encargo: con este esquema (más recreo), escribe en una hoja un borrador de un párrafo de cinco a siete oraciones para la directora. Esquema: Topic sentence: A longer break would help students. Point 1: they are tired after 90 minutes. Point 2: exercise helps them focus. Conclusion: we ask for ten more minutes. Incluye al menos tres conectores distintos (por ejemplo because, however, for example, finally), una palabra menos frecuente como exhausted o excellent y oraciones que no empiecen todas igual. No te detengas a corregir: eso será después.", "A longer break would help students. They are exhausted after 90 minutes of class, so they cannot focus. For example, in the last period many of them look tired. However, a ten-minute break gives them energy. Also, they can talk with friends. Finally, we ask you to try it for a month.", ["usa al menos tres conectores distintos", "usa una palabra menos frecuente y no repite palabras", "oraciones con inicios variados siguiendo el esquema"], ["hoja con el borrador del párrafo y los conectores subrayados"], ["empezar todas las oraciones igual", "repetir la misma palabra"], "Lee el borrador a una persona de tu casa y anota qué conector le ayudó más a seguir las ideas."),
    "Escribe cinco oraciones con un conector distinto cada una (because, so, however, for example, also).",
    "Reescribe un párrafo de tu cuaderno cambiando tres palabras repetidas por otras de significado parecido.",
)

# ================================================================ clase 3: revisar y editar
lesson(
    OA13, 3,
    "Los borradores, listas de verificación y comentarios escritos en cada ejercicio, lápiz y una hoja. Sin materiales especiales.",
    "Aprenderé a revisar el contenido y la organización de un texto y luego a editarlo para corregir errores. Sirve para mejorar el borrador con calma, en dos pasadas y con ayuda de una lista.",
    ["Sé escribir un borrador con conectores.", "Conozco mayúsculas, puntos y formas verbales básicas."],
    [
        "Revisar (revise) y editar (edit) no son lo mismo. Al revisar, miras el contenido y la organización: ¿el propósito se entiende?, ¿cada párrafo tiene una sola idea?, ¿el orden es lógico?, ¿hay detalles suficientes?, ¿se usan conectores? Aquí puedes agregar, quitar, mover o cambiar oraciones. Al editar, corriges la forma: ortografía, mayúsculas, puntuación y gramática, como la -s del verbo con he, she e it.",
        "El orden importa: primero revisa y luego edita, porque no tiene sentido corregir la ortografía de una oración que vas a borrar. Usa una lista de verificación (checklist). Para revisar: 1) propósito claro; 2) una idea por párrafo; 3) orden lógico; 4) al menos dos detalles; 5) conectores. Para editar: 1) mayúsculas; 2) punto final; 3) verbos; 4) ortografía.",
        "La retroalimentación (feedback) de un compañero ayuda mucho si es concreta. Una fórmula útil tiene tres partes: I like… (algo que funciona), A question: … (una duda), A suggestion: … (algo que cambiar). «It is good» no ayuda. «A suggestion: add one detail about the old tools» sí.",
    ],
    [("revise", "revisar: mejorar contenido y organización"), ("edit", "editar: corregir ortografía, puntuación y gramática"), ("checklist", "lista de verificación"), ("feedback", "retroalimentación: comentarios para mejorar"), ("detail", "detalle"), ("capital letter", "mayúscula"), ("full stop", "punto final"), ("suggestion", "sugerencia")],
    [
        ("Clasificar un cambio", "Cambio: agregar a una oración el dato de cuántas personas fueron a la visita. ¿Es revisar o editar?", ["Agrega contenido nuevo al texto.", "No corrige ortografía ni gramática.", "Es revisar."], "Revisar"),
        ("Editar una oración", "Corrige las mayúsculas y el punto: «we visited the library on tuesday».", ["Va mayúscula al inicio y en Tuesday.", "Falta el punto final.", "Queda: We visited the library on Tuesday."], "We visited the library on Tuesday."),
    ],
    [
        ("Corregir las faltas de ortografía antes de decidir qué oraciones borrar.", "Se piensa que editar va primero.", "Primero revisa el contenido y luego edita la forma."),
        ("Escribir como comentario: «It is good».", "No dice qué mejorar.", "Escribe una sugerencia concreta: add one detail."),
    ],
    [
        ("Corregir un punto o una coma es A) editar B) revisar", "A", "Es un cambio de forma."),
        ("¿Qué se hace primero? A) revisar B) editar", "A", "Primero se corrige el contenido y la organización."),
        ("Mover una oración a otro párrafo es A) revisar B) editar", "A", "Cambia la organización del texto."),
    ],
    [
        ("Un compañero escribe: «I like your text. A question: what was your favourite tool? A suggestion: add the day.» ¿Qué parte es la sugerencia? Responde con las palabras de la sugerencia.", "add the day", "Después de A suggestion va lo que se propone cambiar."),
        ("¿Qué comentario es más útil? A) It is good B) A suggestion: add one detail about the old tools.", "B", "Indica qué cambiar y dónde."),
        ("«She go to school» tiene un error de A) gramática B) contenido", "A", "Con she el verbo lleva -s: goes."),
    ],
    [
        ("Edita: «we went to the park on monday». Escribe la oración corregida.", "We went to the park on Monday.", "Se corrigen las mayúsculas de We y Monday y se agrega el punto."),
        ("Después de «We saw old tools.», ¿qué oración agrega un detalle? A) They were more than 100 years old B) I like pizza.", "A", "Da un dato sobre las herramientas y no cambia de tema."),
        ("Borrador: «1. We arrived at the museum at 10. 2. We went home at 4. 3. We saw a huge map at noon.» ¿Qué cambio de orden conviene? A) Mover la oración 2 al final B) Mover la oración 3 al comienzo", "A", "El regreso a casa va después de lo que ocurrió al mediodía."),
    ],
    [
        ("Cuenta los errores: «mia like football. she prefer tennis.» (mayúsculas y verbos). Responde con un número.", "4", "Faltan mayúsculas en Mia y She, y los verbos like y prefer deben ser likes y prefers."),
        ("Propósito: informar sobre el museo. El párrafo trae tres oraciones del museo y una del menú del almuerzo. ¿Qué acción de revisión conviene? A) quitar la oración del menú B) añadir otra del menú", "A", "No pertenece al propósito."),
    ],
    [
        ("¿Qué tarea hacer primero? A) Revisar que cada párrafo tenga una idea B) Chequear la ortografía de cada palabra", "A", "El contenido se arregla antes de editar la forma."),
        ("Una lista de revisión tiene 5 criterios: propósito, una idea por párrafo, orden, dos detalles y conectores. Un borrador cumple propósito y una idea por párrafo; tiene el orden cambiado, solo un detalle y ningún conector. ¿Cuántos criterios cumple?", "2", "Solo cumple los dos primeros."),
    ],
    [("Un blog escolar ficticio recibe esta revisión de un compañero. Texto: «We went to the zoo. We saw lions. We saw monkeys.» Comentarios: A) A suggestion: add the day and one detail about the lions B) It is nice. ¿Cuál ayuda más a mejorar? Elige.", "A", "Da una acción concreta para el contenido.")],
    [
        ("¿Qué corrige el paso de editar?", "La forma: ortografía, puntuación y gramática", "No cambia las ideas."),
        ("¿Cuántas partes tiene la fórmula de feedback de la clase?", "3", "I like, a question y a suggestion."),
        ("¿Qué va primero: revisar o editar?", "Revisar", "Se arregla el contenido antes que la forma."),
    ],
    task("Lee este borrador ficticio: «last friday we goes to the museum. we saw old tools. the museum is in the city centre. we had lunch. we saw a huge map at noon.» Propósito: informar sobre la visita. Escribe en una hoja: primero una revisión (qué moverías o agregarías, con dos cambios), luego la versión editada con mayúsculas, punto y verbo corregidos, y por último un comentario con las tres partes de feedback.", "Revision: move the sentence about the city centre to the start; add one detail about the tools. Edited: Last Friday we went to the museum. It is in the city centre. We saw old tools. We saw a huge map at noon. We had lunch. Feedback: I like the huge map. A question: how old were the tools? A suggestion: add the time of the visit.", ["hace al menos dos cambios de contenido antes de editar", "corrige mayúsculas, punto y la forma verbal", "escribe feedback con las tres partes"], ["hoja con revisión, texto editado y comentario"], ["editar antes de revisar", "comentar solo «it is good»"], "Pide a una persona de tu casa que lea tu versión final y diga si el orden de las ideas le parece lógico."),
    "Escribe tres oraciones con errores de mayúsculas y pásalas a la forma correcta.",
    "Revisa un párrafo tuyo con la lista de cinco criterios y anota cuántos cumple.",
)

# ================================================================ clase 4: ortografía y apóstrofe
lesson(
    OA13, 4,
    "Los textos y listas de palabras escritos en cada ejercicio, lápiz y una hoja. Sin materiales especiales.",
    "Aprenderé a usar el apóstrofe en contracciones y posesivos, a distinguir its/it's y their/there/they're, y a mantener una ortografía consistente. Sirve para dejar un texto limpio antes de publicarlo.",
    ["Conozco contracciones como don't y I'm.", "Sé que hay palabras que suenan igual y se escriben distinto."],
    [
        "El apóstrofe (') tiene dos usos principales. Primero, en las contracciones, indica letras omitidas: do not → don't; it is → it's; they are → they're; I have → I've; we have → we've. Segundo, en el posesivo, indica a quién pertenece algo: Ana's bag (la mochila de Ana). Con un solo dueño se añade 's: the student's room. Con varios dueños que ya terminan en -s se añade solo el apóstrofe: the students' room (varios estudiantes). Si el plural no termina en -s, se añade 's: the children's park.",
        "No se usa apóstrofe para formar plurales simples (two apples, no «apple's»). Hay pares que suenan igual y se confunden: its (de él/ella/eso: The dog wagged its tail) frente a it's (it is); there (allí: There are five chairs), their (de ellos: their books) y they're (they are). Si no sabes cuál usar, prueba reemplazar por it is o they are: si funciona, lleva apóstrofe.",
        "También debes ser consistente: elige una variante de la ortografía y mantenla en todo el texto. Por ejemplo, colour y favourite (británico) o color y favorite (estadounidense), pero no mezclarlas. Otras palabras frecuentes que conviene fijar: because, friend, different, beautiful, tomorrow, necessary. Lee tu texto palabra por palabra y marca las dudas para revisarlas.",
    ],
    [("apostrophe", "apóstrofe (')"), ("contraction", "contracción: do not → don't"), ("possessive", "posesivo: indica a quién pertenece algo"), ("its / it's", "de eso / es o está"), ("their / there / they're", "de ellos / allí / ellos son"), ("consistent", "consistente: siempre igual"), ("colour / color", "dos variantes de la misma palabra"), ("because / tomorrow", "porque / mañana")],
    [
        ("Distinguir its e it's", "Completa con its o it's: «The dog wagged ___ tail.»", ["Prueba con it is: The dog wagged it is tail no tiene sentido.", "Se trata de la cola del perro: posesivo.", "Queda its."], "its"),
        ("Formar un posesivo", "Escribe con apóstrofo «el cuaderno de Sofía» (the notebook of Sofia).", ["Hay un solo dueño: Sofia.", "Se añade 's.", "Queda Sofia's notebook."], "Sofia's notebook"),
    ],
    [
        ("Escribir «two apple's» para el plural.", "Se cree que todo -s necesita apóstrofe.", "El plural simple no lleva apóstrofe: two apples."),
        ("Escribir «Its a lovely day».", "Se confunde its con it's.", "Se prueba con it is: It's a lovely day."),
    ],
    [
        ("Don't significa A) do not B) does not", "A", "La contracción reemplaza la o de not."),
        ("«Ana's bag» significa A) la mochila de Ana B) Ana es una mochila", "A", "El 's indica posesión."),
        ("It's es la contracción de A) it is B) it was", "A", "La contracción de it is lleva apóstrofo."),
    ],
    [
        ("Completa con there, their o they're: «___ are three windows in the room.»", "There", "Indica la existencia de algo en un lugar: there are."),
        ("«The students' room» habla de A) un estudiante B) varios estudiantes", "B", "El apóstrofe después de -s indica varios dueños."),
        ("Completa con their o they're: «The students did ___ homework.»", "their", "Indica que la tarea es de ellos."),
    ],
    [
        ("Escribe la contracción de they are.", "they're", "Se omite la a y se coloca apóstrofo."),
        ("Escribe la contracción de we have.", "we've", "Se omiten las letras ha y se coloca apóstrofo."),
        ("Elige la palabra bien escrita para decir «mañana». A) tomorrow B) tommorow", "A", "Tomorrow lleva una sola m y dos r."),
    ],
    [
        ("Texto: «My favourite colour is blue. My friend's favorite color is green.» ¿Qué problema tiene? A) Mezcla dos ortografías de las mismas palabras B) El apóstrofe de friend's está mal", "A", "Usa favourite/colour y favorite/color en el mismo texto."),
        ("Corrige solo la palabra mal escrita: «The cat licked it's paw.» Escribe la palabra correcta.", "its", "Se trata de la pata del gato: posesivo, sin apóstrofe."),
    ],
    [
        ("Texto: «Its a lovely day and the childrens park is full. Theyre playing.» ¿Cuántos apóstrofes faltan en total?", "3", "Faltan en It's, children's y They're."),
        ("El cuarto es de todos los profesores del colegio. ¿Cómo se escribe? A) the teachers' room B) the teacher's room", "A", "El posesivo plural lleva el apóstrofe después de la s."),
    ],
    [("Un afiche escolar ficticio tiene dos versiones. Versión 1: «It's the students' club, and they're meeting at 4.» Versión 2: «Its the student's club, and their meeting at 4.» ¿Cuál está bien escrita? A) La versión 1 B) La versión 2", "A", "Usa los apóstrofes correctos en it's, students' y they're.")],
    [
        ("¿Qué prueba te ayuda a decidir entre its e it's?", "Reemplazar por it is", "Si la frase funciona con it is, se escribe it's."),
        ("¿Se usa apóstrofe en un plural simple?", "No", "Es two apples, no apple's."),
        ("¿Qué significa ser consistente?", "Mantener la misma ortografía en todo el texto", "No mezclar color con colour."),
    ],
    task("Lee este texto ficticio: «Its the childrens birthday and theyre happy. The teachers room (la sala de todos los profesores) is full of balloons. My favourite colour is red but Ana's favorite color is green.» Escribe en una hoja la versión corregida con los apóstrofes, mantén una sola variante de ortografía y anota una lista de los tres errores que más te costaron.", "It's the children's birthday and they're happy. The teachers' room is full of balloons. My favourite colour is red but Ana's favourite colour is green. Hard errors: its/it's; children's; keeping favourite/colour.", ["corrige it's, children's, they're y teachers'", "mantiene una sola variante de ortografía", "anota los errores más difíciles"], ["hoja con el texto corregido y la lista de tres errores"], ["usar apóstrofe en plurales simples", "mezclar variantes de ortografía"], "Pide a una persona de tu casa que dicte tres frases con it's/its y compruébalas contigo."),
    "Escribe cinco contracciones y su forma completa.",
    "Escribe dos oraciones con posesivo de un solo dueño y dos con varios dueños.",
)

# ================================================================ clase 5: publicar con procesador de textos y diccionario en línea
lesson(
    OA13, 5,
    "Los textos, entradas de diccionario y listas escritos en cada ejercicio, lápiz y una hoja. El procesador de textos y el diccionario en línea son opcionales: todo se puede hacer a mano.",
    "Aprenderé a usar un procesador de textos y un diccionario en línea para pulir un texto y a publicarlo en un formato claro. Sirve para que el trabajo final llegue a su audiencia sin errores y con buena presentación.",
    ["Sé revisar y editar un borrador.", "Conozco partes de la oración como sustantivo, verbo y adjetivo."],
    [
        "Publicar (publish) es el último paso: compartir el texto final con su audiencia (audience). Un procesador de textos (word processor) te ayuda con herramientas como el corrector ortográfico (spell checker), que subraya palabras que no reconoce, el conteo de palabras (word count), los títulos (headings) con tamaño mayor, y los comentarios (comments) para que otra persona sugiera cambios sin modificar el texto. Al terminar se guarda en un formato estable como PDF.",
        "El corrector tiene un límite: no detecta una palabra bien escrita pero mal elegida. En «We go to the beech on Saturday» no marca beech porque existe (un árbol), aunque la palabra correcta sea beach. Por eso hay que leer en voz alta. El diccionario en línea (online dictionary) entrega la palabra (headword), la parte de la oración (noun, verb, adjective), la definición, una oración de ejemplo y, a veces, sinónimos (synonyms). Ejemplo ficticio: «huge (adjective): very big. Example: A huge tree grows in the yard. Synonym: enormous».",
        "Pasos finales de publicación: 1) lee en voz alta; 2) corrige lo último; 3) guarda como PDF o imprime con título de 18 puntos; 4) agrega tu nombre y la fecha; 5) comparte con la audiencia. Sin computador puedes hacer lo mismo a mano: escribe la versión final en limpio, subraya los títulos y pide a otra persona que la lea.",
    ],
    [("publish", "publicar: compartir el texto final"), ("word processor", "procesador de textos"), ("spell checker", "corrector ortográfico"), ("word count", "conteo de palabras"), ("online dictionary", "diccionario en línea"), ("headword", "palabra principal de una entrada"), ("synonym", "sinónimo: palabra con significado parecido"), ("comment", "comentario en el margen de un documento")],
    [
        ("Leer una entrada de diccionario", "Entrada de ejemplo: «huge (adjective): very big. Example: A huge tree grows in the yard. Synonym: enormous». ¿A qué parte de la oración pertenece huge?", ["Entre paréntesis dice adjective.", "Un adjetivo describe a un sustantivo.", "La parte de la oración es adjetivo."], "adjetivo"),
        ("Usar un sinónimo", "Cambia very big por un sinónimo de la entrada de huge: «It is a very big park.»", ["Huge significa very big.", "Se reemplaza very big por huge.", "Queda: It is a huge park."], "It is a huge park."),
    ],
    [
        ("Confiar solo en el corrector ortográfico.", "Se cree que si no está subrayado, está bien.", "Lee en voz alta para detectar palabras bien escritas pero mal elegidas."),
        ("Copiar la primera definición del diccionario sin leer el ejemplo.", "Se supone que una palabra tiene un solo uso.", "Lee la definición y la oración de ejemplo para elegir la palabra adecuada."),
    ],
    [
        ("¿Cuál es el último paso del proceso de escritura? A) publicar B) organizar ideas", "A", "Publicar es compartir el texto final."),
        ("Entrada: «reply (verb): to answer. Example: She replied quickly.» Reply es A) un verbo B) un adjetivo", "A", "Entre paréntesis dice verb."),
        ("Si el corrector subraya en rojo una palabra, A) puede estar mal escrita B) está siempre bien escrita", "A", "El subrayado avisa que no la reconoce."),
    ],
    [
        ("¿Qué herramienta permite que un compañero sugiera cambios sin modificar el texto? Responde en inglés.", "comments", "Los comentarios se escriben en el margen."),
        ("El corrector no subraya «Their are five books». ¿Por qué? A) Porque there y their son palabras reales B) Porque la oración es correcta", "A", "El corrector no ve que se eligió la palabra equivocada."),
        ("¿Por qué conviene guardar como PDF? A) Para mantener el formato al compartir B) Para cambiar la ortografía", "A", "Un PDF se ve igual en cualquier dispositivo."),
    ],
    [
        ("Entrada: «reply (verb): to answer. Example: She replied quickly.» Completa: «He ___ to my message yesterday.»", "replied", "El pasado de reply es replied."),
        ("Entrada de ejemplo: «delighted (adjective): very happy. Example: She was delighted with the gift. Synonym: thrilled». Reescribe «We were very happy with the result» con delighted.", "We were delighted with the result.", "Delighted reemplaza a very happy."),
        ("Ordena los pasos de publicación y escribe las letras en orden: a) save as PDF b) read aloud c) fix last errors d) share with the audience", "b, c, a, d", "Se lee, se corrige, se guarda y se comparte."),
    ],
    [
        ("Texto: «We are going to the beech on Saturday.» El corrector no marca beech. ¿Qué palabra corriges?", "beech", "Debe ser beach, pero beech existe, por eso no se marca."),
        ("¿Qué dato del diccionario ayuda más a usar bien una palabra nueva? A) Una oración de ejemplo B) El número de página", "A", "Muestra el uso real de la palabra."),
    ],
    [
        arith("Un texto tiene 120 palabras y el límite es 150. ¿Cuántas palabras puedes agregar antes de pasarte?", "150-120", "Se resta el texto actual al límite.", " palabras"),
        ("Un afiche para todo el colegio. ¿Qué formato conviene? A) Letra grande, título de 18 puntos B) Letra muy pequeña para que quepa más", "A", "Una audiencia amplia necesita letra grande."),
    ],
    [("Una columna del diario escolar ficticio tiene esta lista de revisión final. Hecho: título, corrector, lectura en voz alta. Pendiente: nombre y fecha. ¿Qué falta antes de publicar? A) Escribir nombre y fecha B) Cambiar el título por el nombre", "A", "La lista pide agregar el nombre y la fecha antes de compartir.")],
    [
        ("¿Qué herramienta del procesador de textos cuenta las palabras?", "El conteo de palabras", "Sirve para ajustar el límite."),
        ("¿Qué entrega un diccionario en línea además de la definición?", "Parte de la oración, ejemplo y sinónimos", "Esos datos ayudan a usar la palabra."),
        ("¿Por qué hay que leer en voz alta?", "Para encontrar errores que el corrector no marca", "El corrector no ve palabras reales mal elegidas."),
    ],
    task("Lee este encargo: publica tu texto final del recreo con estos pasos. Datos de ejemplo: borrador final de 90 palabras, límite de 150; usa esta entrada de ejemplo: «exhausted (adjective): very tired. Example: They were exhausted after the game. Synonym: worn out». En una hoja (o en el computador) escribe: el título, la frase con exhausted en lugar de very tired, tu nombre y la fecha de ejemplo, y la lista de los cinco pasos de publicación con una marca en cada uno.", "Title: A longer break for our school. Sentence: They are exhausted after 90 minutes of class. Name and date: Ana, 12 November (example). Steps: read aloud, fix last errors, save as PDF or print, add name and date, share.", ["usa una palabra del diccionario según su ejemplo", "incluye título, nombre y fecha", "marca los cinco pasos de publicación"], ["hoja o documento con el texto final y la lista de pasos marcada"], ["publicar sin leer en voz alta", "olvidar el nombre o la fecha"], "Entrega tu texto final a una persona de tu casa y pídele que lo lea en voz alta para comprobar que se entiende."),
    "Busca en un diccionario (en papel o en línea) tres palabras y anota parte de la oración y una oración de ejemplo.",
    "Escribe las instrucciones de cómo publicar un texto en cinco pasos para un compañero.",
)
