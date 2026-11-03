"""Cuaderno del estudiante, 8.º básico Inglés (oficial): IN08 OA 14, proceso de escritura en textos breves.

Los modelos en inglés son originales y breves, con glosario en español dentro del enunciado. Los pasos (organizar ideas,
redactar, revisar, editar y publicar), el uso de un modelo y de un criterio, y las herramientas (procesador de textos y
diccionario en línea) se practican con textos y fichas ya escritos en cada ejercicio. Los títulos de clase del plan son
genéricos: aquí se aplican a un paso del proceso por clase.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "IN08 OA 14"


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


# ============================================================ clase 1: organizar ideas (género, propósito y plan)
PL1 = "Plan de cuento. Character: Lola, a young fox. Setting: a forest in autumn. Problem: she cannot find food. Solution: a hedgehog shares apples with her. End: they become friends."
G_PL1 = "(fox = zorra; forest = bosque; autumn = otoño; find = encontrar; hedgehog = erizo; shares = comparte; become = se hacen)"
PL1B = "Plan de descripción. Place: the beach at night. See: dark sea and stars. Hear: quiet waves. Smell: salt. Feel: cold sand."
G_PL1B = "(beach = playa; stars = estrellas; waves = olas; salt = sal; sand = arena)"

lesson(
    OA, 1,
    "Las fichas de plan y las situaciones escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé el primer paso del proceso de escritura, organizar las ideas, eligiendo el género según mi propósito y llenando un plan. Sirve para empezar a escribir un texto breve en inglés sin quedarme en blanco.",
    ["Sé escribir oraciones simples en inglés.", "Conozco los géneros story, email y description."],
    [
        "El proceso de escritura (writing process) tiene cinco pasos: 1) organizar ideas (plan), 2) redactar un borrador (draft, la primera versión), 3) revisar (revise) el contenido y el orden, 4) editar (edit) la ortografía y la puntuación, y 5) publicar (publish) la versión final. En esta clase practicamos el primero. Planificar ahorra tiempo y evita olvidar datos importantes.",
        "Primero elige el género (genre) según tu propósito: un cuento (story) narra una historia; un correo electrónico (email) pide, invita o agradece; un folleto (brochure) informa con datos breves; una rima (rhyme) juega con sonidos; una descripción (description) muestra cómo es algo; una biografía (biography) cuenta la vida de una persona; las instrucciones (instructions) enseñan a hacer algo; un resumen (summary) cuenta lo esencial de otro texto.",
        "Después llena un plan con las partes del género. En un cuento: personaje, lugar, problema, solución y final. En una descripción: lugar y lo que ves, oyes, hueles y sientes. En un correo: quién escribe, qué pide, cuándo y dónde. Anota solo palabras clave. Si una idea no calza con el plan, no la uses. Un buen plan te permite escribir el borrador de forma ordenada.",
    ],
    [("writing process", "proceso de escritura"), ("plan / organize ideas", "planificar / organizar ideas"), ("draft", "borrador"), ("genre", "género de texto"), ("brochure", "folleto"), ("instructions", "instrucciones"), ("biography", "biografía"), ("summary", "resumen"), ("rhyme", "rima")],
    [
        ("Elegir el género según el propósito", "Quieres enseñar a un amigo cómo hacer un avión de papel. ¿Qué género eliges: instructions o biography?",
         ["El propósito es enseñar a hacer algo.", "Las instrucciones enseñan pasos.", "Una biografía cuenta la vida de alguien."], "Instructions."),
        ("Llenar un plan de descripción", "Quieres describir tu cocina. Pasos del plan: See, Hear, Smell. Anota una palabra para cada uno: ves una mesa amarilla, oyes una tetera y hueles pan. Escribe el plan en inglés (table = mesa; kettle = tetera; bread = pan).",
         ["Usa una palabra clave por casilla.", "See: yellow table. Hear: kettle.", "Smell: bread."], "See: yellow table. Hear: kettle. Smell: bread."),
    ],
    [
        ("Empezar a escribir sin plan.", "Se olvidan datos o se pierde el orden.", "Anota primero las ideas clave en un plan."),
        ("Poner en el plan ideas que no tienen relación con el propósito.", "El texto se vuelve confuso.", "Tacha lo que no apoya lo que quieres decir."),
    ],
    [
        ("El primer paso del proceso de escritura es: a) organizar ideas b) publicar", "a", "Se parte planificando antes de redactar."),
        ("«Draft» significa: a) borrador, primera versión b) versión final publicada", "a", "Un borrador se puede revisar y mejorar."),
        ("Para pedir algo por escrito a una persona, un género adecuado es: a) un correo electrónico b) una rima", "a", "Un correo permite pedir con datos claros."),
    ],
    [
        (f"Lee: {PL1} {G_PL1} ¿Cuál es el problema de Lola? a) She cannot find food b) She has a new friend", "a", "El plan dice Problem: she cannot find food."),
        (f"Lee: {PL1} {G_PL1} ¿Dónde ocurre el cuento? a) In a forest in autumn b) On a beach at night", "a", "El plan indica el lugar y la estación en Setting."),
        (f"Lee: {PL1} {G_PL1} ¿Para qué género es esta ficha? a) A story b) Instructions", "a", "Tiene personaje, lugar, problema, solución y final."),
    ],
    [
        ("Quieres contar la vida de una científica que admiras. ¿Qué género eliges? a) Biography b) Brochure", "a", "La biografía cuenta la vida de una persona."),
        ("Quieres explicar cómo llegar a la plaza desde el colegio. ¿Qué género eliges? a) Instructions b) Rhyme", "a", "Las instrucciones dan pasos en orden."),
        ("Quieres informar sobre un museo escolar con horarios y datos breves. ¿Qué género eliges? a) Brochure b) Biography", "a", "Un folleto presenta datos breves y claros."),
    ],
    [
        (f"Lee: {PL1B} {G_PL1B} ¿Qué idea no pertenece a este plan? a) My birthday party in March b) Cold sand", "a", "El plan describe la playa de noche, no una fiesta."),
        ("Ordena los primeros pasos del proceso: x) Write a first version y) Make a plan z) Read it again and improve it. Escribe las tres letras en orden.", "y, x, z", "Primero se planifica, luego se redacta y después se revisa."),
    ],
    [
        ("Pablo escribe un correo para invitar a su curso a una salida, pero olvida decir el día. ¿Qué paso del proceso le habría ayudado más? a) Organizar ideas con una lista de qué, cuándo y dónde b) Publicar antes", "a", "Un plan con cuándo y dónde evita olvidar datos."),
        (f"Lee: {PL1} {G_PL1} ¿Qué final calza con el problema y la solución? a) Lola thanks the hedgehog and they eat apples together b) Lola leaves the forest alone", "a", "El final responde a la solución: comparten manzanas y son amigos."),
    ],
    [("Tu curso prepara un folleto para la feria del colegio. Antes de escribir el borrador, haces una lista. ¿Cuál es la mejor? a) Date, place, activities, entry price b) My favourite colour, my pet, my teacher", "a", "Son los datos que un folleto necesita para informar.")],
    [
        ("En Inglés (oficial): ¿Cuáles son los cinco pasos del proceso de escritura?", "Organizar ideas, redactar, revisar, editar y publicar", "Es el proceso completo, en orden."),
        ("¿Qué escribes en un plan: oraciones largas o palabras clave?", "Palabras clave", "El plan es un esquema breve."),
        ("¿Qué género sirve para pedir, invitar o agradecer por escrito?", "Un correo electrónico", "El email sirve para comunicarse con un propósito."),
    ],
    task("Elige el género «story» y llena este plan en tu hoja: Character: un niño llamado Tomás. Setting: una plaza en invierno. Problem: pierde su gorro. Solution: ____. End: ____. Completa solución y final con palabras clave en inglés. (gorro = hat; plaza = square; invierno = winter)", "Character: Tomas. Setting: a square in winter. Problem: he loses his hat. Solution: a girl finds it. End: Tomas thanks her.", ["completa solución y final con palabras clave", "solución y final calzan con el problema", "usa inglés simple"], ["plan de cuento completo en la hoja"], ["dejar casillas vacías", "poner un final que no responde al problema"], "Pide que cambie el género a una descripción de la plaza y haga el plan con See, Hear y Feel."),
    "Copia la tabla de géneros y escribe una frase con el propósito de cada uno.",
    "Haz el plan de un correo para invitar a tu curso a una actividad, con Who, What, When y Where.",
)

# ============================================================ clase 2: redactar un borrador con un modelo (correo e instrucciones)
EM2 = "Subject: Book club. Hi Teo, I'm writing to ask if you can come to our book club on Friday at 4 p.m. We meet in the library. Please tell me by Wednesday. Thanks! Valeria"
G_EM2 = "(book club = club de lectura; meet = nos juntamos; tell = avisar)"
IN2 = "How to Make a Paper Hat. You need: one big sheet of paper. Step 1: Fold the sheet in half. Step 2: Fold the top corners down to the middle. Step 3: Fold the bottom edges up on both sides. Step 4: Open the bottom and press the hat into shape."
G_IN2 = "(hat = gorro; big = grande; sheet = hoja; fold = doblar; corners = esquinas; edges = bordes; open = abrir; press = presionar; shape = forma)"
EM2B = "Subject: Lost jacket. Dear Mr. Vidal, I'm writing to ask about a grey jacket. I left it in the gym on Tuesday. Could you please check the lost property box? Thank you, Camilo"
G_EM2B = "(lost = perdida; jacket = chaqueta; left = dejé; check = revisar; lost property box = caja de objetos perdidos)"
BM2 = "How to Make a Bookmark. You need: a strip of card, 5 cm wide and 15 cm long, and coloured pencils. Step 1: Draw a border around the card. Step 2: Write your name at the top. Step 3: Draw a picture in the middle. Step 4: Colour the picture."
G_BM2 = "(bookmark = marcapáginas; strip of card = tira de cartulina; wide = ancho; long = largo; border = borde; colour = pintar)"

lesson(
    OA, 2,
    "Los modelos de correo e instrucciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a redactar un borrador de un correo y de unas instrucciones siguiendo un modelo y sus partes. Sirve para escribir una primera versión completa, sin preocuparme todavía de los errores pequeños.",
    ["Conozco los géneros y el plan de escritura.", "Sé usar verbos en imperativo como fold y draw."],
    [
        "Redactar (to draft) es escribir la primera versión siguiendo tu plan. No te detengas a corregir cada palabra: lo importante es poner todas las ideas en orden. Un modelo (model) es un texto ya escrito del mismo género que te muestra sus partes. Puedes imitar su estructura, no copiar sus frases. Cada género tiene partes fijas.",
        "Un correo electrónico tiene: asunto (subject), saludo (greeting), propósito (I'm writing to ask / invite / thank), datos (when, where), petición (Could you please…?) y despedida con tu nombre. Unas instrucciones tienen: título, materiales (You need…), pasos numerados (Step 1, Step 2…) con verbos en imperativo (Fold, Draw, Colour) y, si hace falta, una advertencia (Be careful).",
        "Usa fórmulas útiles (chunks): «I'm writing to ask…», «Could you please…?», «Thank you for…», «Please tell me by…». En las instrucciones, un paso por línea y una sola acción por paso. Cuando termines el borrador, lee el modelo otra vez y comprueba con un criterio (criterion), una condición que debe cumplir tu texto: ¿están todas las partes? ¿hay día y hora? ¿los pasos están en orden?",
    ],
    [("draft", "redactar o borrador"), ("model", "modelo"), ("subject", "asunto"), ("greeting", "saludo"), ("You need…", "Necesitas…"), ("Step 1", "Paso 1"), ("Could you please…?", "¿Podrías…, por favor?"), ("criterion", "criterio")],
    [
        ("Reconocer las partes de un correo", f"Modelo: «{EM2}» {G_EM2} ¿Cuál es la oración del propósito?",
         ["El propósito dice por qué escribe.", "La fórmula I'm writing to ask… lo muestra.", "Esa oración es la del propósito."], "I'm writing to ask if you can come to our book club on Friday at 4 p.m."),
        ("Usar el modelo para completar unas instrucciones", f"Modelo: «{IN2}» {G_IN2} ¿Cuál es el material que necesitas?",
         ["Busca la frase You need.", "Después de los dos puntos está el material.", "Es una hoja grande de papel."], "One big sheet of paper."),
    ],
    [
        ("Escribir las instrucciones en un solo párrafo largo.", "Se pierde el orden de los pasos.", "Escribe un paso por línea: Step 1, Step 2…"),
        ("Dejar el correo sin propósito claro.", "El lector no sabe qué le pides.", "Agrega I'm writing to ask… con el motivo."),
    ],
    [
        ("En un correo, el «subject» es: a) el asunto b) la despedida", "a", "Indica de qué trata el correo."),
        ("Un verbo de instrucciones es: a) Fold b) Folded paper", "a", "Fold es la orden doblar."),
        ("En unas instrucciones, «You need…» introduce: a) los materiales b) el último paso", "a", "Lista lo que hace falta antes de empezar."),
    ],
    [
        (f"Lee: «{EM2B}» {G_EM2B} ¿Para qué escribe Camilo? a) To ask about a lost jacket b) To invite Mr. Vidal to a party", "a", "El propósito es preguntar por una chaqueta que dejó en el gimnasio."),
        (f"Lee: «{EM2B}» {G_EM2B} ¿Qué petición hace? a) Check the lost property box b) Buy a new jacket", "a", "Could you please check the lost property box? es la petición."),
        (f"Lee: «{EM2B}» {G_EM2B} ¿Qué saludo usa? a) Dear Mr. Vidal b) Hi buddy", "a", "Escribe a un adulto del colegio con un saludo formal."),
    ],
    [
        (f"Lee: «{BM2}» {G_BM2} ¿Cuántos pasos tiene? a) Four b) Five", "a", "El modelo numera Step 1 a Step 4."),
        (f"Lee: «{BM2}» {G_BM2} ¿Qué paso va después de «Write your name at the top»? a) Draw a picture in the middle b) Draw a border around the card", "a", "Es el Step 3; el borde es el Step 1."),
        (f"Lee: «{BM2}» {G_BM2} Si agregas un Step 5, elige el imperativo correcto para completar «Step 5: ___ your bookmark to a friend.» (give = dar) a) Give b) Gives", "a", "El imperativo usa el verbo sin s ni sujeto."),
    ],
    [
        (f"Lee: «{EM2B}» {G_EM2B} Criterio: el correo debe decir cuándo ocurrió el hecho. ¿Cumple? a) Sí, dice on Tuesday b) No, no da ninguna fecha", "a", "La frase I left it in the gym on Tuesday da el día."),
        (f"Lee: «{BM2}» {G_BM2} Un compañero propone ordenar los pasos así: Step 4, Step 1, Step 3, Step 2. ¿Qué problema tiene? a) El orden no tiene sentido, no se puede colorear antes de dibujar b) No tiene problema", "a", "Colorear (Step 4) depende de dibujar el dibujo (Step 3)."),
    ],
    [
        (f"Lee: «{EM2}» {G_EM2} ¿Qué frase del correo pide una respuesta antes de una fecha? a) Please tell me by Wednesday b) I'm writing to ask", "a", "Pide la respuesta con un plazo."),
        ("Quieres escribir un correo a tu profesora de Inglés para pedir que te preste un libro. ¿Qué borrador respeta el modelo? a) Subject: Borrow a book. Dear Ms. Soto, I'm writing to ask if I can borrow the book until Monday. Thank you, Elena b) Hello I want the book now", "a", "Tiene asunto, saludo, propósito, petición y despedida con nombre."),
    ],
    [("El centro de alumnos pide instrucciones para hacer una tarjeta de agradecimiento a un profesor: «You need: a sheet of card, a pencil, colour pens. Step 1: Fold the card in half. Step 2: Write Thank you on the front. Step 3: Draw a flower.» (card = cartulina; front = frente) Un compañero dice que falta un paso: firmar la tarjeta. ¿Dónde lo agregas? a) Como Step 4 al final b) Antes de You need", "a", "Firmar es la acción final y los pasos siguen un orden.")],
    [
        ("En Inglés (oficial): ¿Qué es un criterio?", "Una condición que debe cumplir tu texto", "Sirve para revisar el texto."),
        ("¿Qué escribes primero en un correo, antes del saludo: el asunto o la despedida?", "El asunto", "Subject indica de qué trata el correo."),
        ("En unas instrucciones, ¿cuántas acciones va en cada paso?", "Una", "Así los pasos son claros."),
    ],
    task("Mira este modelo de instrucciones y escribe un borrador de otras instrucciones con las mismas partes. Modelo: «How to Make a Paper Plane. You need: one sheet of paper. Step 1: Fold the sheet in half and open it again. Step 2: Fold the top corners to the middle line. Step 3: Fold the plane in half and fold the wings down.» (plane = avión; wings = alas) Tema para tu borrador: «How to Make a Paper Fan» (abanico). Escribe título, You need y tres pasos con imperativos.", "How to Make a Paper Fan. You need: one sheet of paper. Step 1: Fold the paper like an accordion. Step 2: Press the folds. Step 3: Hold one end and open the fan.", ["tiene título y You need", "tres pasos en orden con imperativo", "una acción por paso"], ["borrador de instrucciones en la hoja"], ["escribir pasos sin orden", "usar verbos que no son imperativos"], "Pide que intercambie su borrador con otra persona y que esa persona lo haga siguiendo solo los pasos."),
    "Copia las partes de un correo y de unas instrucciones en dos listas, con su significado.",
    "Escribe el borrador de un correo corto a un compañero para pedirle un cuaderno prestado, con asunto, saludo y despedida.",
)

# ============================================================ clase 3: revisar con un criterio (folleto y biografía)
BR3 = "Draft. Science Fair. Some experiments. Entry free."
CR3 = "Criterios del folleto: 1) un título que llama la atención; 2) tres datos: when, where, what; 3) frases cortas; 4) una invitación a participar."
MODEL3 = "Modelo de folleto. Title: Come to the Science Fair! When: Friday, 15:00 to 18:00. Where: school gym. Activities: robots, volcanoes, plants. Entry is free. Bring a friend!"
G3 = "(science fair = feria de ciencias; experiments = experimentos; gym = gimnasio; robots = robots; volcanoes = volcanes; plants = plantas; bring = trae)"
BIO3 = "Borrador de biografía de ejemplo. Marta Silva was born in 1990 in Temuco. She played the guitar at age eight. She became a music teacher."
CBIO3 = "Criterios de la biografía: 1) cuándo y dónde nació; 2) dos o tres hechos importantes en orden; 3) una frase final que diga por qué es importante; 4) verbos en pasado."
G_BIO3 = "(was born = nació; played = tocaba; age = edad; became = se convirtió en; teacher = profesora)"

lesson(
    OA, 3,
    "Los borradores, modelos y criterios escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a revisar un borrador con un criterio de evaluación, mirando primero el contenido y el orden, y después el lenguaje. Sirve para mejorar un folleto o una biografía antes de corregir las palabras.",
    ["Sé escribir un borrador siguiendo un modelo.", "Conozco el pasado simple was born, played y became."],
    [
        "Revisar (to revise) significa leer tu borrador y mejorarlo. Primero mira el contenido: ¿están las ideas y los datos que pide el género? Luego el orden: ¿las ideas siguen una secuencia clara? Recién al final te fijas en el lenguaje. Para revisar bien usa una lista de criterios (checklist), que son las condiciones que el texto debe cumplir. Lee tu texto una vez por cada criterio.",
        "Hay cuatro acciones de revisión: agregar (add) un dato que falta, quitar (delete) algo que sobra, cambiar de lugar (move) una idea y reemplazar (replace) una palabra poco clara. Un compañero también puede ayudarte con comentarios: «two stars and a wish» (dos cosas buenas, las estrellas, y una sugerencia, el deseo). Un comentario útil es específico: «Add the place» es mejor que «Improve it».",
        "En un folleto, los datos clave son título, cuándo, dónde, qué y una invitación. En una biografía de una persona, usa el pasado simple y cuenta los hechos en orden: nació (was born), hizo algo importante (played, studied, wrote, became) y por qué es importante hoy. Revisa con los criterios y marca con una cruz los que cumples y con un círculo los que debes mejorar.",
    ],
    [("revise", "revisar para mejorar"), ("checklist", "lista de criterios"), ("add / delete", "agregar / quitar"), ("move / replace", "cambiar de lugar / reemplazar"), ("two stars and a wish", "dos cosas buenas y una sugerencia"), ("was born", "nació"), ("became", "se convirtió en")],
    [
        ("Revisar un folleto con criterios", f"{CR3} {BR3} {G3} ¿Qué datos del criterio 2 faltan en el borrador y qué agregas?",
         ["Mira los criterios uno por uno.", "El borrador no dice cuándo ni dónde.", "Agrega When: Friday at 15:00 y Where: school gym."], "Faltan when (cuándo) y where (dónde)."),
        ("Reconocer la acción de revisión", "Un compañero comenta: «Delete the sentence about my dog; it is not related to the party». ¿Qué acción de revisión pide: add, delete o replace?",
         ["El verbo del comentario es delete.", "Pide quitar algo que sobra.", "La acción es delete."], "Delete."),
    ],
    [
        ("Corregir solo la ortografía y no revisar el contenido.", "Se mejora la forma pero faltan datos.", "Primero contenido y orden, después el lenguaje."),
        ("Comentar «Improve it».", "El comentario es demasiado general.", "Di exactamente qué agregar, quitar o cambiar."),
    ],
    [
        ("«Revise» significa: a) revisar para mejorar el texto b) publicar el texto", "a", "Revisar es mejorar el borrador."),
        ("Un criterio es: a) una condición que el texto debe cumplir b) un adjetivo de personalidad", "a", "Sirve para evaluar el texto."),
        ("«Delete» significa: a) quitar b) agregar", "a", "Delete es borrar o quitar."),
    ],
    [
        (f"Lee: {MODEL3} {G3} ¿Qué frase invita a participar? a) Bring a friend! b) Entry is free", "a", "Es la invitación del criterio 4."),
        (f"Lee: {MODEL3} {G3} ¿Cuándo es la feria? a) Friday, 15:00 to 18:00 b) Saturday, 10:00", "a", "El modelo indica When: Friday, 15:00 to 18:00."),
        (f"Lee: {MODEL3} {G3} ¿Qué título del modelo llama la atención? a) Come to the Science Fair! b) Entry is free", "a", "Es el título con exclamación e invitación."),
    ],
    [
        (f"Lee: {CBIO3} {BIO3} {G_BIO3} ¿Qué criterio no cumple el borrador? a) El 3, no dice por qué es importante b) El 4, no usa pasado", "a", "Usa pasado y sigue un orden, pero falta la frase final de importancia."),
        (f"Lee: {BIO3} {G_BIO3} Elige la frase que agregas para cumplir el criterio 3. a) She is important because she teaches children to love music b) She has a guitar", "a", "Explica por qué la persona es importante."),
        (f"Lee: {BIO3} {G_BIO3} Elige el verbo correcto: «She ___ a music teacher.» Opciones: became, becomes.", "became", "La biografía cuenta hechos pasados."),
    ],
    [
        (f"Lee: {CBIO3} {BIO3} {G_BIO3} Un compañero dice que falta el lugar de nacimiento. ¿Es correcto? a) No, dice in Temuco b) Sí, no dice nada", "a", "La frase was born in 1990 in Temuco da año y lugar."),
        (f"Lee: {CR3} {BR3} Un compañero dice: «Move the title to the bottom». ¿Por qué es mala idea? a) Un título llama la atención al comienzo b) Porque nunca hay título", "a", "El título debe ser lo primero que ve el lector."),
    ],
    [
        (f"Lee: {BR3} Revisa y compara con el modelo. El borrador dice «Some experiments». ¿Qué cambio de revisión sirve mejor? a) Replace it with Activities: robots, volcanoes, plants b) Delete the whole text", "a", "Reemplazar una frase vaga por datos concretos mejora el contenido."),
        ("Comentario «two stars and a wish» para un folleto: ★ The title is exciting. ★ The date is clear. Wish: ___. ¿Cuál es un deseo útil? a) Add where the fair is b) Make it nicer", "a", "Un deseo específico dice qué agregar."),
    ],
    [("En tu curso se hace una exhibición de biografías de personas de la comunidad. Una compañera escribió: «Rosa Pino was born in 1975. She sells bread. She is a baker.» (sells = vende; baker = panadera) Según el criterio 1 (cuándo y dónde nació), ¿qué dato falta? a) Where she was born b) When she was born", "a", "El texto da el año 1975, pero no dice el lugar de nacimiento.")],
    [
        ("¿Qué miras primero al revisar: el contenido o la ortografía?", "El contenido", "Primero las ideas y el orden."),
        ("¿Qué significa «two stars and a wish»?", "Dos cosas buenas y una sugerencia", "Es una forma de dar comentarios."),
        ("¿Qué tiempo verbal usas en una biografía: presente o pasado?", "Pasado", "Cuentas hechos de una vida."),
    ],
    task("Revisa este borrador de ejemplo con los criterios de la biografía: «Leo Vega was born in 1985 in Osorno. He studied biology. He is happy.» Criterios: 1) cuándo y dónde nació; 2) dos hechos importantes en orden; 3) una frase final sobre su importancia; 4) verbos en pasado. (biology = biología) En tu hoja anota qué criterios cumple, cuáles no y qué agregarías.", "Cumple el 1 (1985, Osorno). Cumple en parte el 4: was born y studied están en pasado, pero is happy está en presente. No cumple el 2, porque solo hay un hecho, ni el 3. Agregaría: He worked in a river park and taught students. He is important because he protects the river.", ["indica con claridad qué criterios cumple y cuáles no", "agrega al menos un hecho y una frase final", "usa pasado en los hechos"], ["lista de criterios y mejoras en la hoja"], ["decir que todo está bien sin revisar", "agregar datos que no se relacionan con la persona"], "Pide que escriba dos comentarios «two stars and a wish» para el borrador de un compañero."),
    "Copia la lista de acciones de revisión y escribe un ejemplo de cada una.",
    "Revisa con tres criterios un texto breve que escribiste y anota qué agregaste, quitaste o cambiaste.",
)

# ============================================================ clase 4: editar y usar herramientas (procesador de textos y diccionario en línea)
ED4 = "yesterday i go to the park with my freind. we play football and eat a sandwich."
DICA = "Ficha A (diccionario en línea). bank (noun): 1) a place where people keep money. Example: The bank is closed on Sunday. 2) the land along the side of a river. Example: We sat on the bank of the river."
DICB = "Ficha B (diccionario en línea). lend (verb): to give something to someone for a short time. Example: Ana lends me her notebook. borrow (verb): to take something from someone for a short time. Example: I borrow books from the library."
G_DIC4 = "(noun = sustantivo; verb = verbo; land = tierra; side = orilla; notebook = cuaderno)"

lesson(
    OA, 4,
    "Los textos con errores y las fichas de diccionario escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a editar un texto (ortografía, mayúsculas y puntuación) y a usar un procesador de textos y un diccionario en línea. Sirve para entregar un texto limpio y para elegir la palabra correcta.",
    ["Conozco los pasos de planificar, redactar y revisar.", "Sé el abecedario en inglés."],
    [
        "Editar (to edit) es corregir los errores de forma después de revisar el contenido. Mira cuatro cosas: la ortografía (spelling), las mayúsculas (capital letters), la puntuación (punctuation) y la concordancia entre sujeto y verbo (subject–verb agreement). En inglés, I y los nombres de personas, países, días y meses siempre van con mayúscula: Chile, Monday, March, Ana. Cada oración termina con punto, signo de interrogación o de exclamación. Dos ayudas: la regla i antes de e, salvo después de c (friend, receive), que tiene excepciones como their, neighbour y weird, y el apóstrofo en it's, que significa it is.",
        "El procesador de textos (word processor) ayuda: subraya en rojo lo que parece mal escrito y sugiere correcciones. Pero hay que decidir tú: el corrector no detecta una palabra bien escrita pero equivocada, como there en lugar de their. Otras funciones útiles son deshacer (undo), guardar (save) a menudo, usar negrita (bold) para títulos y contar palabras (word count). Antes de aceptar una sugerencia, comprueba que la palabra calza con el sentido.",
        "El diccionario en línea (online dictionary) te da la ficha de una palabra: la categoría (noun, verb, adjective), una o más definiciones numeradas y ejemplos. Muchas palabras tienen más de un significado: bank puede ser un banco o la orilla de un río. Lee los ejemplos y elige el significado que calza con tu oración. Con dos palabras parecidas, como lend y borrow, compara las fichas.",
    ],
    [("edit", "editar: corregir la forma"), ("spelling", "ortografía"), ("punctuation", "puntuación"), ("capital letter", "mayúscula"), ("word processor", "procesador de textos"), ("online dictionary", "diccionario en línea"), ("noun / verb", "sustantivo / verbo"), ("undo", "deshacer"), ("definition", "definición")],
    [
        ("Editar una oración", "Oración: «my sister live in chile.» Corrige mayúsculas, el verbo y el punto. (live = vive)",
         ["La oración debe empezar con mayúscula: My.", "Chile va con mayúscula.", "Con she/my sister el verbo lleva s: lives."], "My sister lives in Chile."),
        ("Elegir el significado en el diccionario", "Ficha: «bank (noun): 1) a place where people keep money; 2) the land along the side of a river.» Oración: «We had a picnic on the bank.» (picnic = picnic) ¿Qué significado calza?",
         ["Lee los dos significados.", "Un picnic ocurre al aire libre, junto a un río.", "Calza el significado 2."], "El significado 2: la orilla del río."),
    ],
    [
        ("Aceptar todas las sugerencias del corrector sin leer.", "El corrector puede cambiar una palabra por otra que no tiene sentido.", "Lee cada sugerencia y comprueba que calza con tu idea."),
        ("Escribir «i» y «monday» con minúscula.", "En inglés I y los días siempre van con mayúscula.", "Escribe I y Monday."),
    ],
    [
        ("«Spelling» se refiere a: a) la ortografía b) la edad", "a", "Es la forma correcta de escribir una palabra."),
        ("En inglés, ¿cuál va siempre con mayúscula? a) I b) and", "a", "La palabra I (yo) se escribe siempre con mayúscula."),
        ("«Undo» sirve para: a) deshacer un cambio b) subrayar en negrita", "a", "Deshace la última acción."),
    ],
    [
        (f"Lee: «{ED4}» (park = parque; freind = amigo mal escrito) ¿Cómo se escribe bien la palabra amigo? a) friend b) freind", "a", "La regla es i antes de e en friend."),
        (f"Lee: «{ED4}» ¿Qué cambio de mayúscula es necesario? a) i → I b) park → Park", "a", "La palabra yo en inglés es I."),
        (f"Lee: «{ED4}» ¿Qué verbo va en pasado, como indica yesterday? a) went b) go", "a", "El pasado de go es went."),
    ],
    [
        (f"Lee: {DICA} {G_DIC4} Oración: «I need to go to the bank to take out money.» (take out = sacar) ¿Qué significado usa? a) 1, el lugar para guardar dinero b) 2, la orilla de un río", "a", "Habla de dinero."),
        (f"Lee: {DICB} {G_DIC4} Completa: «Can you ___ me your pen?» Opciones: lend, borrow.", "lend", "Quien tiene el lápiz lo presta; lend es dar algo por un rato."),
        (f"Lee: {DICB} {G_DIC4} Completa: «I want to ___ your pen.» Opciones: borrow, lend.", "borrow", "Quien lo necesita lo toma por un rato."),
    ],
    [
        ("El corrector subraya en rojo la palabra «recieve». ¿Cuál es la ortografía correcta? a) receive b) receeve", "a", "La regla es i antes de e salvo después de c: receive."),
        ("Un texto dice: «I have two dogs. There names are Bruno and Luna.» El corrector no subraya nada. ¿Por qué hay un error? a) There está bien escrita pero se necesita their b) El texto no tiene errores", "a", "Their (de ellos) es la palabra correcta y el corrector no la detecta."),
    ],
    [
        (f"{DICA} {DICB} {G_DIC4} Con tu compañero comparan las fichas. Él tiene la ficha A y tú la B. Él pregunta cuántos verbos tiene tu ficha. ¿Qué respondes? Escribe el número.", "2", "La ficha B muestra lend y borrow, que son dos verbos."),
        (f"{DICA} {DICB} {G_DIC4} Pregunta de tu compañero: ¿qué categoría tiene bank según su ficha? a) Noun b) Verb", "a", "En la ficha A dice bank (noun)."),
    ],
    [("Escribes un blog escolar. El corrector del procesador de textos subraya la palabra «Valparaiso». Es el nombre de una ciudad. ¿Qué haces? a) Compruebo cómo se escribe el nombre en una fuente confiable antes de aceptar un cambio b) Acepto cualquier sugerencia", "a", "Los nombres propios a veces aparecen subrayados y no son error.")],
    [
        ("¿Qué letra del inglés siempre va con mayúscula para decir yo?", "I", "Se escribe I mayúscula siempre."),
        ("¿Qué paso es primero: revisar contenido o editar ortografía?", "Revisar contenido", "Primero se revisa el contenido y luego se edita."),
        ("¿Qué muestra una ficha de diccionario además del significado?", "Ejemplos", "Los ejemplos ayudan a elegir el significado."),
    ],
    task("Edita este texto en tu hoja: «my friend lives in chile. on monday she play basketball and she eat lunch at school. its a nice day.» (basketball = básquetbol; lunch = almuerzo; nice day = lindo día) Corrige mayúsculas, el verbo y el apóstrofo en it's. Anota qué cambiaste.", "My friend lives in Chile. On Monday she plays basketball and she eats lunch at school. It's a nice day. Cambios: mayúsculas My, Chile, On, Monday, It's; verbos plays y eats.", ["corrige todas las mayúsculas", "corrige los dos verbos con s", "usa it's con apóstrofo"], ["texto corregido y lista de cambios en la hoja"], ["olvidar una mayúscula", "dejar el verbo sin s"], "Pide que busque con un diccionario en línea el significado de una palabra nueva de este texto y escriba la definición."),
    "Copia las cuatro cosas que se revisan al editar y escribe un ejemplo de error de cada una.",
    "Elige una palabra nueva de tu cuaderno, busca su ficha en un diccionario en línea o impreso y copia categoría, definición y un ejemplo.",
)

# ============================================================ clase 5: publicar y resumir / rimar (respuesta independiente)
SU5 = "Rosa's Radio. Rosa is twelve and loves music. She makes a small radio at home with her uncle's help. Every Friday she plays songs and reads school news for her neighbours. Now thirty neighbours listen every week."
G_SU5 = "(radio = radio; uncle = tío; help = ayuda; plays = pone; news = noticias; neighbours = vecinos; listen = escuchan)"
RH5 = "I see the sun up in the sky, / A little bird goes flying by. / I smile and wave and say hello, / And off I go with a happy glow."
G_RH5 = "(sky = cielo; flying by = pasa volando; wave = saludo con la mano; glow = brillo)"

lesson(
    OA, 5,
    "Los textos, las rimas y las fichas de publicación escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a publicar la versión final de un texto, a escribir un resumen y una rima y a decidir cómo compartirlos. Sirve para presentar mi trabajo con claridad ante otras personas.",
    ["Sé planificar, redactar, revisar y editar un texto.", "Conozco palabras que riman, como cat y hat."],
    [
        "Publicar (to publish) es presentar la versión final de un texto a su audiencia: pegarla en el diario mural, enviarla por correo, subirla al blog del curso o leerla en voz alta. Antes de publicar, revisa una última vez con tu lista: título, nombre del autor, letra legible, fotos o dibujos con leyenda, ortografía revisada y un formato limpio (sin manchas ni tachones). Una buena presentación hace más fácil leer tu texto.",
        "Un resumen (summary) cuenta lo esencial de un texto con tus palabras: la idea principal y uno o dos datos importantes, en dos o tres oraciones, en presente y sin opinión. Ejemplo: «Rosa is twelve. She makes a small radio and shares music with her neighbours». Una rima (rhyme) usa palabras que terminan con el mismo sonido: sky–fly, say–day, sun–fun, hello–glow. Los versos riman cuando las palabras finales suenan igual, aunque se escriban distinto.",
        "Para trabajar de forma independiente, sigue los cinco pasos: planifica con palabras clave, escribe un borrador siguiendo un modelo, revisa con tu criterio, edita con el procesador de textos y el diccionario, y publica. Al final pide una opinión a otra persona con «two stars and a wish» y anota qué mejorarías la próxima vez.",
    ],
    [("publish", "publicar"), ("final copy", "versión final"), ("summary", "resumen"), ("main idea", "idea principal"), ("rhyme", "rima"), ("rhyming words", "palabras que riman"), ("audience", "audiencia: quién lee")],
    [
        ("Resumir un texto", f"Texto: «{SU5}» {G_SU5} Escribe un resumen de una oración.",
         ["Idea principal: Rosa hace una radio.", "Dato importante: comparte música con sus vecinos.", "Une las ideas en presente."], "Rosa makes a small radio and shares music with her neighbours."),
        ("Reconocer palabras que riman", f"Poema: «{RH5}» {G_RH5} ¿Qué palabra rima con sky?",
         ["Mira el final del verso 1: sky.", "El verso 2 termina en by.", "Sky y by suenan igual."], "by"),
    ],
    [
        ("Copiar el texto entero como resumen.", "Un resumen es mucho más corto que el texto.", "Escribe la idea principal y uno o dos datos."),
        ("Pensar que riman solo las palabras que se escriben igual al final.", "La rima depende del sonido, no de las letras.", "Compara cómo suenan: say y day riman."),
    ],
    [
        ("«Publish» significa: a) publicar b) revisar", "a", "Publicar es presentar la versión final."),
        ("Un resumen tiene: a) la idea principal y pocos datos b) todos los detalles", "a", "Resume lo esencial."),
        ("Cuál rima con «cat»: a) hat b) dog", "a", "Cat y hat terminan con el mismo sonido."),
    ],
    [
        (f"Lee: «{SU5}» {G_SU5} ¿Cuál es la idea principal? a) Rosa makes a small radio and shares music b) Rosa is twelve", "a", "La edad es un detalle; la idea es la radio y la música compartida."),
        (f"Lee: «{SU5}» {G_SU5} ¿Cuántos vecinos escuchan ahora? a) Thirty b) Twelve", "a", "El texto dice Now thirty neighbours listen every week."),
        (f"Lee: {RH5} {G_RH5} ¿Qué palabra rima con hello? a) glow b) sun", "a", "Hello y glow terminan con el mismo sonido -o."),
    ],
    [
        (f"Lee: «{SU5}» {G_SU5} Elige el mejor resumen. a) Twelve-year-old Rosa builds a small radio and shares music and news with her neighbours b) Rosa likes music and I think the radio is beautiful", "a", "Usa palabras propias y no incluye opinión."),
        ("Completa la rima: «I wear a hat, I pet my cat, and sit on the ___.» Opciones: mat, chair.", "mat", "Mat rima con hat y cat."),
        ("Completa la rima: «Every night I look at the moon, / and I sing a happy ___.» Opciones: tune, song.", "tune", "Tune rima con moon porque terminan con el mismo sonido."),
    ],
    [
        (f"Lee: «{SU5}» {G_SU5} Un compañero escribió en el resumen: «Rosa is the best girl in the world». ¿Qué error tiene? a) Es una opinión y no está en el texto b) Es demasiado corto", "a", "Un resumen no incluye opiniones."),
        ("Una compañera quiere publicar su texto en el diario mural del curso. ¿Qué verifica primero? a) Que el texto esté revisado, editado y limpio b) Que sea largo", "a", "Publicar requiere una versión final cuidada."),
    ],
    [
        ("Rima de una compañera: «I like the rain, it makes me smile, / I walk and walk for a long ___.» ¿Qué palabra rima con smile? a) while b) time", "a", "While y smile terminan con el mismo sonido."),
        ("Decide cómo publicar un resumen para tu abuela que vive lejos y no usa computador. a) Enviarle una carta escrita a mano con letra legible b) Subirlo a un blog que ella no puede abrir", "a", "La forma de publicar debe adaptarse a la audiencia."),
    ],
    [("Tu curso arma una revista escolar. Cada grupo debe entregar la versión final de un resumen. Elena entrega un texto con un título, su nombre, dos oraciones sobre la idea principal y cero errores. ¿Qué paso del proceso corresponde a entregarlo? a) Publicar b) Planificar", "a", "Presentar la versión final a la audiencia es publicar.")],
    [
        ("En Inglés (oficial): ¿Cuál es el último paso del proceso de escritura?", "Publicar", "Se presenta la versión final."),
        ("¿Cuántas oraciones tiene un buen resumen breve: dos o tres, o veinte?", "Dos o tres", "Debe ser corto."),
        ("¿Riman las palabras say y day? Responde sí o no.", "Sí", "Terminan con el mismo sonido."),
    ],
    task("Lee este texto: «Pia has a small garden on her balcony. She grows tomatoes and mint. Every morning she waters the plants. In summer she gives mint tea to her neighbours.» (balcony = balcón; grows = cultiva; mint = menta; waters = riega; gives = regala) En tu hoja escribe: un resumen de dos oraciones, una rima de dos versos sobre el jardín (las palabras finales deben sonar igual, como en day y say) y una lista de cinco cosas que revisarías antes de publicarlos.", "Resumen: Pia grows tomatoes and mint on her balcony. She waters them every morning and gives mint tea to her neighbours. Rima: Little leaves so fresh and green, / The prettiest garden I have seen. Lista: título, nombre, ortografía, letra legible, ilustración.", ["el resumen tiene idea principal y no incluye opinión", "los dos versos riman por el sonido final", "la lista incluye al menos cinco puntos"], ["resumen, rima y lista en la hoja"], ["copiar el texto como resumen", "elegir palabras que no riman"], "Pide que lea su rima en voz alta a una persona de su casa y ajuste una palabra si no suena igual."),
    "Copia las cinco cosas que debes revisar antes de publicar y marca las que ya hiciste en tu último trabajo.",
    "Escribe una rima de dos versos sobre tu desayuno, con palabras que terminen igual.",
)
