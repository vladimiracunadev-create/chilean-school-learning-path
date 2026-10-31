"""Cuaderno del estudiante, 5.º básico Inglés (propuesta): EN05 OA 15 (proceso de escritura con herramientas digitales y de referencia).

Los textos en inglés son originales, muy breves y llevan pista en español. Cada palabra o estructura se enseña en la propia
clase antes de usarla. Sin audio externo: todo lo que hay que leer está escrito en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "EN05 OA 15"


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


# ================================================================ OA 15 clase 1: organizar ideas
lesson(
    OA, 1,
    "Las listas, planes y textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé el primer paso del proceso de escritura: organizar las ideas antes de escribir. Sirve para planear un texto breve con propósito, ideas ordenadas y sin ideas sobrantes.",
    ["Sé escribir oraciones cortas con modelo.", "Conozco first, then y finally."],
    [
        "El proceso de escritura (writing process) tiene cinco pasos: organizar ideas (organize ideas), redactar un borrador (draft), revisar (revise), editar (edit) y publicar (publish). Hoy trabajas el primero. Antes de escribir una oración, decide sobre qué vas a escribir (topic), para qué (purpose) y para quién (audience).",
        "Para organizar las ideas puedes hacer una lista o un mapa de ideas (mind map). En un mapa de ideas escribes el tema al centro y cada idea sale como una rama. Después revisas la lista: tacha lo que no tiene relación con el tema y ordena lo que queda, por ejemplo con first, then y finally.",
        "Un buen plan es corto y ordenado. «Topic: My school day. Ideas: I wake up at 7. I go to school. I do homework. I go to bed at 9.» Si una idea no habla del tema, como «my cousin has a red car», se quita. Con un plan claro, escribir el borrador es mucho más fácil.",
    ],
    [("writing process", "proceso de escritura"), ("organize ideas", "organizar ideas"), ("draft", "borrador"), ("topic / purpose / audience", "tema / propósito / a quién se escribe"), ("mind map", "mapa de ideas"), ("revise / edit / publish", "revisar / editar / publicar")],
    [
        ("Quitar una idea que no va", "Tema: My school day. Ideas: I wake up at 7 / I do homework after school / my cousin has a red car / I go to bed at 9. ¿Qué idea no va?", ["Cada idea debe hablar del día de escuela.", "Wake up, homework y go to bed son del día.", "El auto del primo no tiene relación."], "my cousin has a red car"),
        ("Ordenar un plan", "Ordena para el tema «My routine»: I go to bed. I wake up. I do homework.", ["Primero se despierta.", "Luego hace la tarea.", "Al final se va a dormir."], "I wake up. I do homework. I go to bed."),
    ],
    [
        ("Empezar a escribir sin planificar.", "El texto mezcla ideas y se pierde el orden.", "Primero anota y ordena tus ideas."),
        ("Dejar en el plan ideas que no hablan del tema.", "El texto se desvía.", "Tacha lo que no tiene relación con el tema."),
    ],
    [
        ("¿Cuál es el primer paso del proceso de escritura?", "Organizar las ideas", "Se piensa y se planifica antes de escribir."),
        ("¿Qué significa «draft»?", "Borrador", "Es la primera versión del texto."),
        ("¿Qué es un «mind map»?", "Un mapa de ideas", "Es un dibujo con el tema al centro y las ideas en ramas."),
    ],
    [
        ("En «I write an email to my friend», ¿quién es la audiencia (audience)?", "My friend", "La audiencia es quien lee el texto."),
        ("¿Cuál es el propósito de una invitación: avisar de un evento o contar un cuento?", "Avisar de un evento", "El propósito es para qué se escribe."),
        ("Mapa de ideas: «Centro: My pet. Ramas: name, food, tricks.» ¿Cuántas ramas tiene?", "3", "Las ramas son name, food y tricks."),
    ],
    [
        ("Elige la mejor oración de tema para un párrafo sobre tu mascota: a) I have a small dog called Max. b) Dog.", "a", "La a presenta el tema con una oración completa."),
        ("Plan para una invitación: «date, time, place, my favourite food». ¿Qué dato sobra?", "my favourite food", "No es un dato de la invitación."),
        ("Ordena: Finally, I go to bed. / First, I wake up. / Then, I do homework. Escribe las letras en orden: a) Finally... b) First... c) Then...", "b, c, a", "Se sigue first, then, finally."),
    ],
    [
        ("Pedro empieza a escribir sin planificar y su texto mezcla ideas. ¿Qué paso omitió?", "Organizar las ideas", "Es el primer paso del proceso."),
        ("¿Por qué conviene pensar en la audiencia?", "Para elegir las palabras y los datos que esa persona necesita", "El texto cambia según quien lo lea."),
    ],
    [
        {"q": "Plan: Tema: My birthday. Ideas: date, cake, friends, my homework, place. Se quita la idea que no va. ¿Cuántas ideas quedan?", "a": "4", "why": "Se resta la idea que sobra del total. Cálculo: 5 − 1 = 4.", "calc": "5-1"},
        ("En ese plan, ¿qué idea sobra?", "my homework", "No tiene relación con el cumpleaños."),
    ],
    [("Camila va a escribir sobre su fin de semana. Anota: «Saturday - park. Sunday - lunch. Monday - school.» ¿Qué anotación no pertenece al fin de semana?", "Monday - school", "Lunes no es parte del fin de semana.")],
    [
        ("¿Cuántos pasos tiene el proceso de escritura?", "5", "Son organizar, redactar, revisar, editar y publicar."),
        ("¿Qué haces con una idea que no habla del tema?", "La tachas", "El plan debe quedar solo con ideas útiles."),
        ("¿Qué significa «purpose»?", "Propósito", "Es para qué se escribe un texto."),
    ],
    task("Lee este plan: «Topic: My school day. Ideas: I wake up at 7. I do homework after school. I go to bed at 9.» Haz un plan igual en tu hoja para uno de estos temas: (a) My pet, (b) My favourite place, (c) My weekend. Anota el tema, el propósito, la audiencia y cuatro ideas. Tacha una idea que sobre y ordena el resto con números.", "Topic: My weekend. Purpose: tell my friend. Audience: my friend. Ideas: 1 play soccer, 2 see my friends, 3 do homework, 4 go to bed.", ["anota tema, propósito y audiencia", "cuatro ideas relacionadas con el tema", "las ideas están ordenadas"], ["hoja con el plan"], ["incluir ideas que no hablan del tema", "no ordenar las ideas"], "Lee las ideas en orden y pregunta qué idea quitaría."),
    "Dibuja un mapa de ideas con el tema al centro y tres ramas.",
    "Haz un mapa de ideas para escribir sobre tu escuela y tacha una idea que no sirva.",
)

# ================================================================ OA 15 clase 2: redactar el borrador
lesson(
    OA, 2,
    "Los modelos y borradores escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a redactar un borrador de un párrafo breve con oración de tema, oraciones de apoyo y cierre, usando un modelo. Sirve para pasar de las ideas del plan a un texto en inglés.",
    ["Sé hacer un plan con ideas ordenadas.", "Conozco el vocabulario de la rutina y las expresiones It's time to go e It's late."],
    [
        "Un párrafo tiene tres partes. La oración de tema (topic sentence) presenta de qué trata. Las oraciones de apoyo (supporting sentences) dan los detalles. La oración de cierre (closing sentence) termina el texto. Modelo: «My Saturday is busy. First, I wake up at eight and have breakfast. Then I play soccer with my friends. Finally, I do my homework. It's time to sleep!»",
        "El borrador (draft) es la primera versión: lo importante es escribir las ideas del plan en oraciones simples. Puedes usar el modelo y cambiar los datos. Usa las palabras de orden first, then, next y finally. Puedes incluir vocabulario del tema, palabras frecuentes como always o after, y expresiones como It's late.",
        "En el borrador no te detengas por una duda de ortografía: subraya la palabra y sigue. Más tarde la revisarás con un diccionario. Cada idea del plan se convierte en una oración. Mantén el propósito y a la persona que va a leer en mente.",
    ],
    [("topic sentence", "oración de tema"), ("supporting sentences", "oraciones de apoyo"), ("closing sentence", "oración de cierre"), ("draft", "borrador"), ("busy", "ocupado"), ("It's time to sleep.", "Es hora de dormir.")],
    [
        ("Encontrar la oración de tema", "Modelo: «My Saturday is busy. First, I wake up at eight. Then I play soccer. Finally, I do my homework.» ¿Cuál es la oración de tema?", ["La oración de tema presenta de qué trata el párrafo.", "La primera dice que el sábado es ocupado.", "Las otras dan detalles."], "My Saturday is busy."),
        ("Convertir una idea del plan en oración", "Idea del plan: «play soccer, friends». Escribe una oración con Then.", ["Uso la palabra de orden Then.", "Escribo sujeto y verbo: I play soccer.", "Agrego with my friends."], "Then I play soccer with my friends."),
    ],
    [
        ("Escribir una lista de palabras sueltas en vez de oraciones.", "Un borrador necesita oraciones completas.", "Convierte cada idea del plan en una oración con sujeto y verbo."),
        ("Detenerse en el borrador para corregir cada palabra.", "Se pierde el hilo de las ideas.", "Subraya la duda y sigue; revisarás después."),
    ],
    [
        ("¿Qué es la «topic sentence»?", "La oración que presenta el tema", "Dice de qué trata el párrafo."),
        ("¿Qué es la «closing sentence»?", "La oración de cierre", "Termina el párrafo."),
        ("¿Qué palabra de orden va en la primera oración de apoyo: First o Finally?", "First", "First es la primera."),
    ],
    [
        ("Modelo: «My Saturday is busy. First, I wake up at eight. Then I play soccer. Finally, I do my homework. It's time to sleep!» ¿Cuál es la oración de cierre?", "It's time to sleep!", "Es la última y termina el texto."),
        ("En el mismo modelo, ¿cuántas oraciones de apoyo hay?", "3", "Son las que empiezan con First, Then y Finally."),
        ("Une las ideas: «I wake up» y «I have breakfast» con and. ¿Cuál queda bien? a) I wake up and I have breakfast. b) I wake and up I have breakfast.", "a", "And une las dos oraciones sin cambiar el orden."),
    ],
    [
        ("Idea del plan: «homework, after school». Escribe la oración con I always, do y my homework.", "I always do my homework after school.", "Always va antes del verbo."),
        ("Completa con una expresión del nivel: «It's 10 o'clock at night. ___ Let's go to bed.» Opciones: It's late, It's early.", "It's late", "De noche y a esa hora ya es tarde."),
        ("Completa con then: «First, I eat breakfast. ___, I go to school.»", "Then", "Then une una acción con la siguiente."),
    ],
    [
        ("Un borrador dice: «soccer friends Saturday». ¿Qué le falta? a) Oraciones completas con sujeto y verbo. b) Más palabras sueltas.", "a", "Un borrador debe tener oraciones completas."),
        ("Pedro tiene tres oraciones: «I wake up. I eat breakfast. I do homework.» ¿Qué le falta para ser un párrafo con las tres partes?", "Una oración de tema y una de cierre", "Faltan la presentación y el cierre."),
    ],
    [
        ("Borrador: «My Sunday is relaxing. First, I read a book. Then I play with my cat. Finally, I draw. It's time to go to bed!» ¿Cuántas oraciones tiene en total?", "5", "Hay una de tema, tres de apoyo y una de cierre."),
        ("En ese borrador, ¿cuál es la oración de tema?", "My Sunday is relaxing.", "Presenta de qué trata."),
    ],
    [("Lucas quiere escribir sobre su recreo y arma una oración de apoyo con estas piezas. Ordénalas para que la oración comience con I: with / play / friends / my / I", "I play with my friends.", "Se arma una oración completa con sujeto, verbo y detalles.")],
    [
        ("¿Qué escribes en el borrador cuando dudas de una palabra?", "La subrayas y sigues", "Se corrige en el paso de revisar."),
        ("¿Cuántas partes tiene un párrafo?", "3", "Tema, apoyo y cierre."),
        ("¿Qué significa «draft»?", "Borrador", "Es la primera versión."),
    ],
    task("Lee este modelo: «My Saturday is busy. First, I wake up at eight and have breakfast. Then I play soccer with my friends. Finally, I do my homework. It's time to sleep!» Usa tu plan de la clase anterior, o este plan: «Topic: My school day. Ideas: wake up, school, homework, bed». Redacta en tu hoja un borrador de cinco oraciones con oración de tema, tres de apoyo con first, then y finally, y una de cierre con una expresión como It's late o It's time to go.", "My school day is long. First, I wake up at seven. Then I go to school. Finally, I do my homework. It's time to sleep!", ["tiene oración de tema, tres de apoyo y una de cierre", "usa first, then y finally", "usa una expresión del nivel"], ["hoja con el borrador"], ["escribir palabras sueltas", "olvidar el cierre"], "Pide que lea el borrador y señale cada parte con una flecha."),
    "Convierte cada una de tres ideas de un plan en una oración completa.",
    "Redacta un borrador de seis oraciones sobre un lugar que te gusta.",
)

# ================================================================ OA 15 clase 3: revisar el texto
lesson(
    OA, 3,
    "Los borradores escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a revisar un borrador: comprobar que se entienda, que tenga orden, que no repita ni deje sin decir algo. Sirve para mejorar las ideas antes de corregir la ortografía.",
    ["Sé que un párrafo tiene oración de tema, apoyo y cierre.", "Conozco el vocabulario de la rutina y first, then y finally."],
    [
        "Revisar (revise) es leer tu borrador y mejorar las ideas. No es corregir la ortografía; eso viene después, en el paso de editar. Al revisar, te preguntas: ¿se entiende lo que quiero decir?, ¿tiene un buen orden?, ¿repetí una idea?, ¿falta algún dato importante?, ¿usé las palabras del tema?",
        "Un borrador puede tener problemas de contenido. Ejemplo: «I have a dog. His name is Max. My dog is black. I have a dog.» La primera y la última oración repiten lo mismo. Se quita una y se agrega un dato nuevo, como «He likes to run». También puede faltar la oración de tema o el cierre.",
        "Pide a otra persona que lea tu texto y te diga cuál es la idea principal. Si no la encuentra, tu texto necesita más claridad. Una lista de control (checklist) te ayuda: ordena ideas, quita repeticiones, agrega lo que falta y comprueba que cada oración dé información sobre el tema.",
    ],
    [("revise", "revisar: mejorar las ideas"), ("checklist", "lista de control"), ("repeat", "repetir"), ("main idea", "idea principal"), ("missing", "que falta"), ("clear", "claro")],
    [
        ("Encontrar la repetición", "Borrador: «I have a dog. His name is Max. My dog is black. I have a dog.» ¿Cuál oración repite una idea?", ["Busco ideas que se dicen dos veces.", "La primera dice I have a dog.", "La última dice lo mismo."], "I have a dog (la última)"),
        ("Encontrar lo que falta", "Borrador: «First, I wake up. Then I go to school. Finally, I do homework.» ¿Qué parte del párrafo falta al comienzo?", ["Veo tres oraciones de apoyo.", "No hay una oración que presente el tema.", "Falta la oración de tema."], "La oración de tema"),
    ],
    [
        ("Revisar solo la ortografía.", "Eso se hace al editar; antes hay que mejorar las ideas.", "Primero revisa el orden, la claridad y lo que falta."),
        ("Dejar oraciones que repiten lo mismo.", "El texto se vuelve aburrido.", "Quita la repetición y agrega un dato nuevo."),
    ],
    [
        ("¿Qué significa «revise»?", "Revisar para mejorar las ideas", "Es el paso donde mejoras el contenido."),
        ("¿Qué es un «checklist»?", "Una lista de control", "Sirve para comprobar paso a paso."),
        ("¿Revisar es corregir solo la ortografía?", "No", "La ortografía se corrige al editar."),
    ],
    [
        ("Borrador: «I wake up. I eat. I wake up.» ¿Qué problema hay?", "Una oración se repite", "I wake up aparece dos veces."),
        ("Borrador: «First, I wake up. Finally, I go to bed.» ¿Qué palabra de orden del modelo de la clase anterior (First, Then, Finally) falta entre las dos?", "Then", "First, then y finally."),
        ("Una compañera lee tu texto y no entiende de qué trata. ¿Qué parte puede faltar: la oración de tema o la ortografía?", "La oración de tema", "La oración de tema presenta de qué trata."),
    ],
    [
        ("Borrador: «My pet is a cat. His name is Tom. He sleeps a lot.» Quiero agregar un dato nuevo. ¿Cuál sirve? a) He likes milk. b) I like pizza.", "a", "La a habla de la mascota; la b se sale del tema."),
        ("Borrador: «I have a dog. I have a dog. He is black.» Corrige quitando la repetición. Escribe el texto corregido (dos oraciones).", "I have a dog. He is black.", "Se elimina la oración repetida."),
        ("Borrador: «My Sunday is relaxing. I read a book. I play with my cat.» ¿Qué parte falta al final?", "La oración de cierre", "No hay una oración que termine el párrafo."),
    ],
    [
        ("Ana revisó su texto y dice: «Corregí la ortografía de dos palabras, así que ya revisé las ideas.» ¿Es correcto?", "No, corregir la ortografía pertenece al paso de editar", "Revisar las ideas es otra tarea."),
        ("Pedro agregó «I like pizza» a un texto sobre su perro. ¿Qué pasa con esa oración?", "No habla del tema del texto", "Debe quitarse o cambiarse."),
    ],
    [
        ("Texto A: «I wake up. I have breakfast. I go to school.» Texto B: «My morning is busy. First, I wake up. Then I have breakfast. Finally, I go to school.» ¿Cuál se entiende mejor y por qué? Escribe A o B.", "B", "El texto B tiene tema y orden con palabras de orden."),
        ("Borrador: «My cat is Tom. He is black. He likes milk. He is black.» ¿Qué oración se repite?", "He is black.", "Aparece dos veces."),
    ],
    [("En la escuela, la profesora lee en voz alta el borrador de Luis: «My weekend is fun. First, I play soccer. Then I visit my friend. Then I visit my friend.» ¿Qué debe revisar Luis?", "Quitar la oración repetida", "La última repite la anterior.")],
    [
        ("¿Qué pasos haces en el paso de revisar?", "Mejorar las ideas, el orden y quitar repeticiones", "Eso es revisar el contenido."),
        ("¿Quién puede ayudarte a revisar?", "Otra persona que lea tu texto", "Un lector te dice si se entiende la idea principal."),
        ("¿Qué haces si repites una idea?", "La quitas y agregas un dato nuevo", "Así el texto da más información."),
    ],
    task("Lee este borrador: «I have a dog. His name is Max. I have a dog. My cousin has a red car. He likes to run.» Revisa el borrador siguiendo la lista de control: (1) quita una oración repetida, (2) quita una idea que no habla del tema, (3) agrega una oración de cierre. Reescribe el texto mejorado en tu hoja.", "I have a dog. His name is Max. He likes to run. He is my best friend.", ["quita la repetición", "quita la idea del auto", "agrega un cierre"], ["hoja con el texto revisado"], ["corregir solo la ortografía", "dejar la idea que no va"], "Compara el antes y el después y celebra cada mejora."),
    "Lee tu borrador de la clase anterior y marca con una cruz cada oración que repite o no habla del tema.",
    "Haz una lista de control de cuatro preguntas para revisar tus propios textos.",
)

# ================================================================ OA 15 clase 4: editar y publicar con procesador de texto
lesson(
    OA, 4,
    "Los textos con errores escritos en cada ejercicio, lápiz y una hoja. Si hay un computador, el procesador de texto; si no, se trabaja en papel.",
    "Aprenderé a editar (corregir mayúsculas, puntuación, ortografía y verbos) y a publicar una copia limpia, usando las herramientas de un procesador de texto. Sirve para presentar un texto claro y bien escrito.",
    ["Sé revisar un borrador.", "Conozco las reglas de mayúscula y punto."],
    [
        "Editar (edit) es corregir la forma del texto: mayúscula al comienzo, punto al final, ortografía, y la forma de los verbos (por ejemplo, He likes y no He like). Se hace después de revisar las ideas. Primero revisas, luego editas. Los días de la semana y los nombres propios llevan mayúscula (Saturday, Max), y it's lleva apóstrofo.",
        "Un procesador de texto (word processor) es un programa para escribir. Marca con una línea roja las palabras que no reconoce (spell check). Tiene botones como Bold (negrita), Save (guardar), Print (imprimir), Undo (deshacer) y Copy / Paste (copiar / pegar). Pero ojo: la corrección automática puede equivocarse, por eso tú debes leer el texto.",
        "Publicar (publish) es entregar la versión final y limpia: con título, tu primer nombre y sin errores. Puedes imprimirla, pegarla en un diario mural o guardar el archivo para mostrarlo en clase. No publiques datos privados como tu dirección o teléfono. Todo uso de internet se hace con una persona adulta.",
    ],
    [("edit", "editar: corregir la forma del texto"), ("word processor", "procesador de texto"), ("spell check", "corrector ortográfico"), ("Bold / Save / Print / Undo", "negrita / guardar / imprimir / deshacer"), ("publish", "publicar: entregar la versión final"), ("title", "título")],
    [
        ("Corregir un texto", "Corrige: «my friend is funny. he like sports» Escribe el texto corregido.", ["Falta mayúscula en My y en He.", "Con he, like pasa a likes.", "Falta el punto final."], "My friend is funny. He likes sports."),
        ("Elegir el botón correcto", "Quieres guardar tu texto para no perderlo. ¿Qué botón usas: Save o Print?", ["Print es imprimir en papel.", "Save guarda el archivo.", "Necesito guardar."], "Save"),
    ],
    [
        ("Confiar solo en el corrector automático.", "El corrector puede equivocarse.", "Lee el texto tú mismo y comprueba cada corrección."),
        ("Publicar con datos privados, como la dirección.", "Se pone en riesgo tu seguridad.", "Publica solo tu primer nombre y el título."),
    ],
    [
        ("¿Qué significa «edit»?", "Editar: corregir la forma del texto", "Se corrigen mayúsculas, puntos, ortografía y verbos."),
        ("¿Qué botón sirve para imprimir: Print o Undo?", "Print", "Print significa imprimir."),
        ("¿Qué significa «Undo»?", "Deshacer", "Anula el último cambio."),
    ],
    [
        ("En un procesador de texto, ¿qué indica una línea roja bajo una palabra?", "Que la palabra puede estar mal escrita", "Es la señal del corrector ortográfico."),
        ("Corrige la ortografía de «freind». Escribe la palabra bien.", "friend", "Se escribe i antes de e."),
        ("¿Cuál va primero: revisar las ideas o editar la forma?", "Revisar las ideas", "Primero se mejora el contenido."),
    ],
    [
        ("Corrige: «she play soccer on saturday». Escribe la oración corregida.", "She plays soccer on Saturday.", "Se corrige mayúscula, verbo y punto."),
        ("Completa con la forma correcta: «He ___ breakfast every day.» Opciones: have, has.", "has", "Con he se usa has."),
        ("Corrige: «i feel tired becouse its late». Escribe la oración corregida.", "I feel tired because it's late.", "Se corrige I, because, it's y el punto."),
    ],
    [
        ("El corrector marca con rojo la palabra «Max» (nombre de un perro). ¿Debes cambiarla?", "No, es un nombre propio", "El corrector no conoce algunos nombres."),
        ("¿Qué dato NO debes publicar: tu título o tu dirección?", "Tu dirección", "Es un dato privado."),
    ],
    [
        ("Texto: «my pet is a cat. its name is tom. he sleeps a lot» ¿Cuántas mayúsculas faltan? (cuenta las letras iniciales de las tres oraciones y el nombre Tom)", "4", "Faltan en my, its, he y la T de Tom."),
        ("En ese texto, ¿cuántos puntos finales faltan?", "1", "Solo falta el punto de la última oración."),
    ],
    [("Valentina termina su cuento y le sale una línea roja bajo la palabra «recieve». ¿Cómo se escribe correctamente?", "receive", "La regla es i antes de e salvo después de c.")],
    [
        ("¿Qué botón usas para dar formato de negrita: Bold o Save?", "Bold", "Bold es negrita."),
        ("¿Qué significa «publish»?", "Publicar: entregar la versión final", "Es el último paso del proceso."),
        ("¿Qué puedes poner en la versión publicada además del texto?", "El título y tu primer nombre", "No se ponen datos privados."),
    ],
    task("Lee este texto con errores: «my friend lia is funny. she like to play soccer. we play on saturday and its fun». Reescríbelo corregido en tu hoja (mayúsculas, puntos, verbos y apóstrofo). Luego haz una copia limpia con título y tu primer nombre, como en una publicación. Si tienes un computador, escríbelo en un procesador de texto con una persona adulta y usa Save.", "My friend Lia is funny. She likes to play soccer. We play on Saturday and it's fun.", ["corrige mayúsculas, verbos y apóstrofo", "agrega título y primer nombre", "no incluye datos privados"], ["hoja con el texto editado y la copia limpia"], ["confiar solo en el corrector", "poner datos privados"], "Compara el original con la copia limpia y nombra tres correcciones."),
    "Escribe una lista de cinco botones de un procesador de texto y para qué sirven.",
    "Edita el borrador que escribiste en la clase 2 y haz una copia limpia con título.",
)

# ================================================================ OA 15 clase 5: usar un diccionario en línea
lesson(
    OA, 5,
    "Las entradas de diccionario escritas en cada ejercicio, lápiz y una hoja. Si tienes un computador, un diccionario en línea con una persona adulta.",
    "Aprenderé a leer la entrada de un diccionario en línea (significado, tipo de palabra, ejemplo) y a usarla para elegir y escribir mejor una palabra. Sirve para escribir con más precisión y revisar la ortografía.",
    ["Conozco el proceso de escritura.", "Sé el orden del alfabeto."],
    [
        "Un diccionario en línea (online dictionary) es un sitio donde buscas una palabra y aparece su entrada (entry). La entrada muestra la palabra, el tipo de palabra (noun = sustantivo, verb = verbo, adjective = adjetivo), el significado (meaning) y una oración de ejemplo (example). Algunas palabras tienen más de un significado.",
        "Ejemplo de entrada: «friendly (adjective): kind and happy to meet people. Example: My teacher is friendly.» Y otra: «bat (noun): 1. an animal that flies at night. 2. a stick for hitting a ball. Example: A bat sleeps in a cave.» Para elegir el significado correcto, lee el ejemplo y mira las palabras de tu oración.",
        "También usas el diccionario para revisar la ortografía: si escribes «frend», lo buscas y ves que es friend. Para buscar, ordena las palabras por la primera letra, luego por la segunda y así con las siguientes. Usa solo el diccionario que tu profesor o una persona adulta te indique y no escribas datos privados.",
    ],
    [("online dictionary", "diccionario en línea"), ("entry", "entrada: lo que aparece sobre una palabra"), ("noun / verb / adjective", "sustantivo / verbo / adjetivo"), ("meaning", "significado"), ("example", "ejemplo"), ("alphabetical order", "orden alfabético")],
    [
        ("Elegir el significado correcto", "Entrada de bat: 1. an animal that flies at night. 2. a stick for hitting a ball. Oración: «A bat sleeps in a cave.» (cave = cueva). ¿Qué significado calza?", ["La oración habla de dormir en una cueva.", "El animal duerme en una cueva.", "Es el significado 1."], "1"),
        ("Leer el tipo de palabra", "Entrada: «friendly (adjective): kind and happy to meet people.» ¿Qué tipo de palabra es friendly?", ["Busco el paréntesis.", "Dice adjective.", "Es un adjetivo."], "Un adjetivo"),
    ],
    [
        ("Elegir siempre el primer significado sin leer el ejemplo.", "Una palabra puede tener más de un significado.", "Lee el ejemplo y compáralo con tu oración."),
        ("Escribir una palabra de oído sin revisarla.", "Se cometen errores de ortografía.", "Búscala en el diccionario y compara."),
    ],
    [
        ("¿Qué significa «noun»?", "Sustantivo", "Es una palabra que nombra cosas o personas."),
        ("¿Qué muestra una «entry» de un diccionario?", "El significado, el tipo de palabra y un ejemplo", "Es la información de una palabra."),
        ("¿Qué significa «meaning»?", "Significado", "Es lo que quiere decir una palabra."),
    ],
    [
        ("Entrada: «homework (noun): work from school that you do at home.» ¿Qué tipo de palabra es homework?", "Un sustantivo", "El paréntesis dice noun."),
        ("Entrada de bat: 1. an animal that flies at night. 2. a stick for hitting a ball. Oración: «The player has a bat.» ¿Qué significado calza?", "2", "El jugador usa un palo para golpear una pelota."),
        ("Ordena alfabéticamente: cat, apple, banana. Escribe las tres palabras separadas por comas.", "apple, banana, cat", "A viene antes que b y c."),
    ],
    [
        ("Escribiste «frend». Buscas en el diccionario y aparece «friend». ¿Cuál es la ortografía correcta?", "friend", "El diccionario muestra la palabra bien escrita."),
        ("Usa la entrada «quiet (adjective): with little or no noise. Example: The library is quiet.» Escribe tu oración sobre una sala de clases con quiet.", "The classroom is quiet.", "Se usa el adjetivo con is como en el ejemplo."),
        ("Ordena alfabéticamente: school, sun, sad.", "sad, school, sun", "Todas empiezan con s; la segunda letra define: a, c, u."),
    ],
    [
        ("Pedro lee «bat» y escribe «I play with a bat» para hablar del animal. ¿Qué error cometió?", "Eligió el significado equivocado", "Un animal no sirve para jugar de ese modo."),
        ("Un diccionario en línea te pide tu nombre completo y tu dirección. ¿Qué haces?", "No lo escribo y aviso a un adulto", "Los datos privados no se comparten."),
    ],
    [
        ("Entrada: «busy (adjective): with a lot to do. Example: My Saturday is busy.» Lee: «My teacher is very busy today.» ¿Qué significado usa la palabra busy?", "Con mucho que hacer", "Ese es el significado de la entrada."),
        ("Ordena alfabéticamente: pen, pet, pea.", "pea, pen, pet", "Las dos primeras letras son iguales; la tercera ordena: a, n, t."),
    ],
    [("Antes de publicar su cuento, Daniela busca «recieve» en el diccionario en línea y ve la entrada «receive (verb): to get something». ¿Qué corrige?", "Escribe receive", "El diccionario muestra la ortografía correcta.")],
    [
        ("¿Qué muestra la parte «Example» de una entrada?", "Una oración que usa la palabra", "Ayuda a entender cómo se usa."),
        ("¿Qué significa «adjective»?", "Adjetivo", "Describe cómo es algo o alguien."),
        ("¿Por qué conviene leer el ejemplo?", "Porque ayuda a elegir el significado", "La palabra puede tener varios significados."),
    ],
    task("Elige estas tres entradas: «friendly (adjective): kind and happy to meet people. Example: My teacher is friendly.», «busy (adjective): with a lot to do. Example: My Saturday is busy.» y «quiet (adjective): with little or no noise. Example: The library is quiet.» Escribe en tu hoja una oración propia con cada palabra, usando el ejemplo como modelo. Después ordena las tres palabras alfabéticamente. Si tienes computador, busca con una persona adulta otra palabra que quieras usar y copia su significado y su ejemplo.", "My cousin is friendly. My teacher is busy today. The park is quiet. Orden: busy, friendly, quiet.", ["escribe una oración con cada palabra", "las oraciones se parecen al ejemplo y tienen sentido", "ordena alfabéticamente: busy, friendly, quiet"], ["hoja con tres oraciones y la lista ordenada"], ["usar la palabra con otro significado", "ordenar solo por la primera letra cuando hay empate"], "Lee el ejemplo del diccionario y compáralo con la oración escrita."),
    "Busca en un diccionario (de papel o en línea) una palabra nueva y anota su tipo, su significado y un ejemplo.",
    "Escribe el borrador de un párrafo corto y marca tres palabras que revisarías con un diccionario.",
)
