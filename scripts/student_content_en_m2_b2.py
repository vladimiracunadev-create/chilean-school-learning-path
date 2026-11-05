"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 12: conocimiento y uso del lenguaje en textos escritos.

Textos originales y ficticios, con pista en español; todo lo que una pregunta nombra está escrito en el enunciado.
Los títulos de clase del plan son genéricos; aquí cada clase trabaja un grupo de funciones del OA en la escritura: frecuencia,
tiempo y grado; acuerdo, desacuerdo, opinión, posesión y tiempo (incluido I was left without… y has been working);
conectar ideas; énfasis en quien actúa e informar lo que otros dicen; y acciones anteriores en el pasado en un texto
conectado. Los ejercicios cerrados corrigen, completan y eligen; la escritura propia se evalúa en la tarea abierta.
"""
from __future__ import annotations

from en_m2_a_common import MAT_READ, arith, lesson, task

OA = "EN2M OA 12"

# ================================================== clase 1: frecuencia, tiempo y grado
SURV = "Mini encuesta escrita de ejemplo: «Q: How often do you read for pleasure? Lía: I usually read on Sundays. Q: How often do you use your phone in class? Ben: Hardly ever, because we are not allowed. Q: Are you good at maths? Tomás: I am rather good, but my sister is better. Q: When will you finish the project? Pia: Soon, I think by Friday.»\n(for pleasure = por placer, allowed = permitido, better = mejor, project = proyecto)"
PARA1 = "Párrafo de ejemplo: «My brother always wakes up early. He often runs in the park before school, and he sometimes goes with a friend. He is quite tired at night, so he goes to bed soon after dinner.»\n(wakes up = se despierta, runs = corre, tired = cansado)"

lesson(
    OA, 1, MAT_READ,
    "Aprenderé a escribir preguntas sobre frecuencia (How often…?) y a describir frecuencia, tiempo y grado con adverbios, usando una posición correcta en la oración. Sirve para escribir rutinas, encuestas y descripciones con precisión.",
    ["Sé el presente simple.", "Sé los días de la semana."],
    [
        "Para escribir una pregunta sobre frecuencia (frequency) usa How often + auxiliar + sujeto + verbo: How often do you practise sports? How often does she call you? Se responde con un adverbio de frecuencia (always, usually, often, sometimes, hardly ever, never) o con una expresión como once a week o twice a month. Recuerda que does se usa con he, she e it, y el verbo principal queda en forma simple.",
        "La posición del adverbio importa. Con un verbo principal va antes: I usually call her in the morning; he often runs. Con el verbo to be va después: She is always on time. Los adverbios de grado (degree) como rather, quite, very y pretty van antes del adjetivo: He is rather shy. Los adverbios de tiempo como soon, tomorrow o next week suelen ir al final: Susan will be here soon.",
        "Para escribir sobre una acción que empezó en el pasado y continúa, usa have/has been + -ing: He has been working during the summer. Agrega for o since cuando indiques cuánto dura. Al revisar tu texto, comprueba tres cosas: la forma de la pregunta, la posición del adverbio y la concordancia con he, she o it.",
    ],
    [("How often…?", "¿Con qué frecuencia…?"), ("always", "siempre"), ("hardly ever", "casi nunca"), ("rather", "bastante"), ("soon", "pronto"), ("has been working", "ha estado trabajando")],
    [
        ("Corregir una pregunta", "Elige la pregunta correcta: A) How often does she call you? B) How often she calls you?", ["Después de How often va el auxiliar.", "Con she se usa does y el verbo simple.", "La A."], "A"),
        ("Posición del adverbio", "Elige la oración correcta: A) She is always on time. B) She always is on time.", ["Con to be el adverbio va después.", "La A.", "La B está mal ordenada."], "A"),
    ],
    [
        ("Escribir How often you practise?", "Falta el auxiliar do.", "Escribe How often do you practise?"),
        ("Poner el adverbio antes de to be (She always is).", "Con to be va después.", "Escribe She is always."),
    ],
    [
        ("Lee: " + SURV + " ¿Cuándo lee Lía por placer? A) los domingos B) los viernes", "A", "Responde I usually read on Sundays."),
        ("Lee: " + PARA1 + " ¿Con qué frecuencia corre el hermano en el parque? A) a menudo B) nunca", "A", "El párrafo dice He often runs in the park."),
        ("Lee: " + SURV + " ¿Qué frecuencia tiene Ben para usar el teléfono en clase? A) casi nunca B) siempre", "A", "Responde Hardly ever."),
    ],
    [
        ("Elige la oración con adverbio bien ubicado: A) I usually walk to school. B) I walk usually to school.", "A", "El adverbio va antes del verbo principal."),
        ("Lee: " + SURV + " Elige la pregunta correcta para la respuesta de Tomás: A) Are you good at maths? B) Do you good at maths?", "A", "Con to be se hace la pregunta con Are."),
        ("Lee: " + PARA1 + " ¿Cuándo se va a la cama? A) pronto después de la cena B) antes del almuerzo", "A", "Dice soon after dinner."),
    ],
    [
        ("Completa: «How often ___ your brother play football?» A) does B) do", "A", "Con brother se usa does."),
        ("Elige la oración correcta: A) He has been working for two months. B) He has been work for two months.", "A", "Se necesita el verbo con -ing."),
        ("Lee: " + PARA1 + " Elige el adverbio de grado en He is quite tired: A) quite B) tired", "A", "Quite modifica al adjetivo tired."),
    ],
    [
        ("Lee: " + SURV + " Tomás escribe: I am rather good at maths. ¿Qué indica rather? A) bastante B) poco", "A", "Rather indica un grado alto moderado."),
        ("Lee: " + PARA1 + " Un compañero propone escribir: He runs often in the park. ¿Qué se corrige? A) el adverbio debe ir antes: he often runs B) falta una coma", "A", "Se coloca antes del verbo principal."),
    ],
    [
        ("Ordena de menos a más frecuente: a) never b) hardly ever c) sometimes d) always", "a, b, c, d", "Never es 0, hardly ever casi nunca, sometimes a veces y always siempre."),
        ("Elige la corrección de «She have been studying since June»: A) She has been studying since June. B) She have been study since June.", "A", "Con she se usa has y el verbo lleva -ing."),
    ],
    [("Lee: «Lucas exercises twice a week and plays football on Saturdays. Last month he trained three times a week.» ¿Cuántos días entrena en total en una semana normal, entre ejercicio y fútbol del sábado?", "3", "Hace ejercicio dos veces y agrega el sábado: 2 más 1 son 3.")],
    [
        ("¿Dónde va un adverbio de frecuencia con to be?", "Después del verbo to be", "She is always on time."),
        ("¿Cómo se pregunta por la frecuencia (en escritura de funciones)?", "How often + auxiliar + sujeto + verbo", "How often do you…?"),
        ("¿Qué se usa con una acción que continúa?", "Have/has been + -ing", "Has been working."),
    ],
    task("Escribe un mini texto de cuatro oraciones para un blog escolar sobre tus rutinas. Debe tener: una pregunta con How often, una oración con un adverbio de frecuencia, una con rather o quite y una con has/have been + -ing. Revisa la posición de los adverbios y la concordancia. Luego léelo en voz alta.", "Ejemplo: How often do you read? I usually read at night. I am quite tired on Mondays. I have been reading a novel for two weeks.", ["escribe una pregunta correcta con How often", "coloca bien los adverbios", "usa has/have been + -ing"], ["texto escrito de cuatro oraciones"], ["omitir el auxiliar en la pregunta", "poner el adverbio antes de to be"], "Lee el texto a una persona de tu casa y pide que marque las oraciones que no entendió."),
    "Reescribe cinco oraciones de tu cuaderno agregando un adverbio de frecuencia en la posición correcta.",
    "Escribe un cuestionario de cinco preguntas con How often y aplícalo a dos personas.",
)

# ================================================== clase 2: acuerdo, opinión, posesión y tiempo
FORUM2 = "Foro escolar de ejemplo: «Topic: Homework on weekends. Ana: I agree with the idea of less homework because we need time to rest. I believe that rest helps learning. Beto: I disagree with Ana. I believe in a little practice every day. I was left without time to finish the project last week. Carla: My opinion is that it depends on the subject. My classmate Diego has been working on a presentation during the summer.»\n(homework = tarea, weekends = fines de semana, rest = descansar, learning = aprendizaje, practice = práctica, left without = me quedé sin, project = proyecto, depends on = depende de, summer = verano)"

lesson(
    OA, 2, MAT_READ,
    "Aprenderé a escribir acuerdo, desacuerdo, opinión, posesión y tiempo con frases como I agree/disagree with…, I believe that/in…, I was left without… y he has been working… Sirve para escribir comentarios, foros y textos de opinión con razones.",
    ["Sé usar because.", "Sé el presente perfecto continuo básico."],
    [
        "Para escribir acuerdo y desacuerdo usa I agree with… (estoy de acuerdo con…) e I disagree with… (no estoy de acuerdo con…), seguidos de una persona o una idea y de because + razón: I agree with the idea because we need time to rest. Para escribir una opinión, usa I believe that + oración o I believe in + sustantivo: I believe that rest helps learning. I believe in teamwork. También sirven In my opinion… y My opinion is that…",
        "Para escribir posesión (possession) se usan adjetivos posesivos (my, your, his, her, our, their) y el genitivo sajón (’s): Diego’s presentation, my classmate’s notebook. La expresión I was left without… significa «me quedé sin…» y se usa para decir que algo faltó: I was left without time. Para el tiempo, has been working during the summer indica una acción que continúa; usa since o for con el período.",
        "En un comentario escrito, ordena tus ideas: primero tu postura (agree/disagree), luego la razón y por último un ejemplo. Usa conectores como because y though. Revisa que el verbo concuerde y que no repitas la misma frase. Un buen texto de opinión es respetuoso: Ana’s idea is interesting, but I disagree because…",
    ],
    [("I agree with", "estoy de acuerdo con"), ("I disagree with", "no estoy de acuerdo con"), ("I believe that", "creo que"), ("I believe in", "creo en"), ("I was left without", "me quedé sin"), ("’s", "marca de posesión: Diego’s")],
    [
        ("Elegir la frase", "Quieres escribir «creo en el trabajo en equipo». ¿Qué frase usas? A) I believe in teamwork. B) I believe teamwork in.", ["Se usa I believe in + sustantivo.", "La A.", "La B tiene orden incorrecto."], "A"),
        ("Posesión", "¿Cuál indica que la presentación es de Diego? A) Diego’s presentation B) The presentation Diego", ["La posesión se marca con ’s.", "La A.", "La B está incompleta."], "A"),
    ],
    [
        ("Escribir I am agree.", "En inglés se dice I agree, sin to be.", "Escribe I agree."),
        ("Escribir Diegos presentation.", "Falta el apóstrofo de posesión.", "Escribe Diego’s presentation."),
    ],
    [
        ("Lee: " + FORUM2 + " ¿Con qué idea está de acuerdo Ana? A) con menos tarea B) con más tarea", "A", "Ana dice I agree with the idea of less homework."),
        ("Lee: " + FORUM2 + " ¿Qué razón da Ana? A) necesitan tiempo para descansar B) la tarea es muy fácil", "A", "Dice because we need time to rest."),
        ("Lee: " + FORUM2 + " ¿En qué cree Beto? A) en un poco de práctica cada día B) en no practicar", "A", "Dice I believe in a little practice every day."),
    ],
    [
        ("Lee: " + FORUM2 + " ¿Qué significa I was left without time? A) me quedé sin tiempo B) tuve mucho tiempo", "A", "Beto lo dice sobre el proyecto de la semana pasada."),
        ("Lee: " + FORUM2 + " ¿Qué opinión expresa Carla? A) que depende de la asignatura B) que no debería haber tarea", "A", "Dice it depends on the subject."),
        ("Lee: " + FORUM2 + " ¿Quién ha estado trabajando durante el verano? A) Diego B) Beto", "A", "Dice Diego has been working on a presentation during the summer."),
    ],
    [
        ("Completa: «I ___ with your idea because it is realistic.» A) agree B) am agree", "A", "Se dice I agree."),
        ("Completa: «This is my sister___ bag.» A) ’s B) s’", "A", "La posesión de una sola persona se marca con ’s."),
        ("Lee: " + FORUM2 + " ¿Qué conector usa Ana para dar una razón? A) because B) though", "A", "Dice because we need time to rest."),
    ],
    [
        ("Lee: " + FORUM2 + " Beto responde a Ana con I disagree with Ana. ¿Qué debe agregar para que sea un buen comentario? A) una razón con because B) otro saludo", "A", "Una opinión necesita una razón."),
        ("Lee: " + FORUM2 + " ¿Cuál es la idea de Beto? A) practicar un poco cada día B) no hacer tarea", "A", "Dice a little practice every day."),
    ],
    [
        ("Ordena una opinión completa: a) because we need time to rest b) I agree with less homework c) For example, we can read for pleasure", "b, a, c", "Primero la postura, luego la razón y al final el ejemplo."),
        ("Elige la oración correcta: A) I was left without my notebook. B) I left without my notebook was.", "A", "La estructura es was left without + sustantivo."),
    ],
    [("Lee: «Tomás: I disagree with the new rule because it is too strict. Lía: I agree with Tomás, but I believe that a rule is needed.» (strict = estricta, needed = necesaria). ¿Qué agrega Lía a la opinión de Tomás?", "Que una norma es necesaria", "Dice but I believe that a rule is needed.")],
    [
        ("¿Cómo se escribe «creo que» en inglés?", "I believe that", "Se completa con una oración."),
        ("¿Qué es el genitivo sajón?", "La marca ’s de posesión", "Por ejemplo, Diego’s presentation."),
        ("¿Qué significa I was left without?", "Me quedé sin…", "Indica falta de algo."),
    ],
    task("Lee el tema de este foro de ejemplo: «Should students wear a uniform?» Escribe un comentario de cinco oraciones: tu postura con I agree/disagree with…, una razón con because, una opinión con I believe that o I believe in, una frase con ’s o un posesivo y, si puedes, una con I was left without. Revisa la ortografía y los apóstrofos.", "Ejemplo: I disagree with the uniform because students want to express their style. I believe in freedom with respect. My classmate’s opinion is similar. Last month, I was left without a clean shirt. Respect is the key.", ["postura clara con agree/disagree", "una razón con because", "usa posesivos o ’s correctamente"], ["comentario escrito de cinco oraciones"], ["escribir I am agree", "olvidar el apóstrofo"], "Lee tu comentario a una persona de tu casa y pregunta si mostraste tu postura con claridad."),
    "Reescribe cinco opiniones de tu curso con I agree/disagree y because.",
    "Escribe un breve foro de cuatro comentarios sobre una actividad del colegio.",
)

# ================================================== clase 3: conectar ideas
MAIL3 = "Correo de ejemplo: «Subject: Update on the school trip. Dear families, neither the museum nor the park is open on Monday, so we will visit on Tuesday. Either the bus or the train will take us, but we have not decided yet. The trip is long, though the students are excited. As soon as we have the final plan, we will send it to you. We will not go unless the weather is good. As a result, we ask you to check your email on Monday. Kind regards, Ms. Silva»\n(update = novedades, families = familias, museum = museo, decided = decidido, excited = entusiasmados, weather = clima, check = revisar)"

lesson(
    OA, 3, MAT_READ,
    "Aprenderé a conectar ideas por escrito con neither…nor, either…or, though, as a result, as soon as y unless, y a puntuar bien las oraciones. Sirve para escribir correos y textos conectados con claridad.",
    ["Sé conectores simples como and, but, so y because.", "Sé el futuro con will."],
    [
        "Neither…nor (ni… ni) se usa para negar dos opciones: Neither the museum nor the park is open. No uses otra negación en el verbo. Either…or (o… o) presenta dos opciones: Either the bus or the train will take us. Though (aunque) introduce un contraste y puede ir al inicio o al final con coma: The trip is long, though the students are excited. Unless (a menos que) equivale a if not: We will not go unless the weather is good.",
        "As soon as (tan pronto como) marca el momento en que algo ocurre: As soon as we have the plan, we will send it. Después de as soon as se usa el presente aunque hable del futuro. As a result (como resultado) muestra una consecuencia y va antes de una coma: As a result, we ask you to check your email. No confundas as a result con because: as a result va después del hecho, y because va antes de la causa.",
        "Al escribir, revisa la puntuación. Pon una coma después de as a result y de las frases iniciales (As soon as we have the plan, we will…). Evita las oraciones muy largas con muchos conectores. Cada conector debe relacionar dos ideas reales: contraste, condición, consecuencia, momento u opción. Lee tu texto en voz alta para comprobar el ritmo.",
    ],
    [("neither…nor", "ni… ni"), ("either…or", "o… o"), ("though", "aunque"), ("unless", "a menos que"), ("as soon as", "tan pronto como"), ("as a result", "como resultado")],
    [
        ("Elegir el conector", "Completa: «We will play outside ___ it rains.» A) unless B) as a result", ["Hay una condición.", "Unless equivale a a menos que.", "La A."], "A"),
        ("Puntuación", "¿Qué frase está bien puntuada? A) As a result, we stayed home. B) As a result we, stayed home.", ["Después de as a result va coma.", "La A.", "La B pone la coma en otro lugar."], "A"),
    ],
    [
        ("Escribir Neither Ana nor Ben didn’t come.", "No se usa doble negación.", "Escribe Neither Ana nor Ben came."),
        ("Escribir As soon as I will arrive.", "Después de as soon as se usa presente.", "Escribe As soon as I arrive."),
    ],
    [
        ("Lee: " + MAIL3 + " ¿Qué día visitarán el museo? A) el martes B) el lunes", "A", "Dice we will visit on Tuesday."),
        ("Lee: " + MAIL3 + " ¿Qué opciones de transporte menciona? A) el bus o el tren B) el auto o el bote", "A", "Dice Either the bus or the train."),
        ("Lee: " + MAIL3 + " ¿Qué ocurre apenas tengan el plan final? A) lo enviarán a las familias B) lo cambiarán", "A", "Dice As soon as we have the final plan, we will send it."),
    ],
    [
        ("Lee: " + MAIL3 + " ¿Qué lugares están cerrados el lunes? A) el museo y el parque B) solo el museo", "A", "Neither the museum nor the park is open."),
        ("Lee: " + MAIL3 + " ¿Qué muestra though en The trip is long, though the students are excited? A) un contraste B) una consecuencia", "A", "Largo y entusiasmados se oponen."),
        ("Lee: " + MAIL3 + " ¿Qué condición se pone para ir? A) que el clima sea bueno B) que sea martes", "A", "Dice unless the weather is good."),
    ],
    [
        ("Completa: «She is tired, ___ she keeps working.» A) though B) because", "A", "Tired y keeps working se oponen."),
        ("Completa: «___ I get home, I will call you.» A) As soon as B) Neither", "A", "Marca el momento de la llamada."),
        ("Lee: " + MAIL3 + " ¿Qué consecuencia se pide? A) que revisen su correo el lunes B) que no manden dinero", "A", "Dice As a result, we ask you to check your email on Monday."),
    ],
    [
        ("Lee: " + MAIL3 + " Un compañero escribe We will not go unless the weather is bad. ¿Qué cambia el sentido? A) debería ser good B) debería ser though", "A", "Con unless, la condición es que el clima sea bueno."),
        ("Elige la corrección: A) Neither Pia nor Leo came. B) Neither Pia nor Leo didn’t come.", "A", "Neither…nor ya es negativo."),
    ],
    [
        ("Une las ideas con el conector adecuado. 1) It was raining ___ we stayed home. 2) The film is long ___ it is great. 3) I will call you ___ I arrive. Conectores: a) though b) so (as a result) c) as soon as", "1-b, 2-a, 3-c", "Consecuencia, contraste y momento."),
        ("Ordena: a) As a result, b) it rained all day c) the match was cancelled", "b, a, c", "Primero el hecho y luego la consecuencia."),
    ],
    [("Lee: «Neither the printer nor the computer works. Either Mr. Soto or Ms. Vega will fix it.» (printer = impresora, works = funciona, fix = arreglar). ¿Quiénes pueden arreglarlo?", "Mr. Soto o Ms. Vega", "Dice Either Mr. Soto or Ms. Vega will fix it.")],
    [
        ("¿Qué muestra as a result?", "Una consecuencia", "Va después del hecho."),
        ("¿Qué tiempo se usa después de as soon as?", "El presente", "As soon as we arrive."),
        ("¿Qué significa unless (en escritura de funciones)?", "A menos que", "Es una condición."),
    ],
    task("Escribe un correo de cinco oraciones a una persona de tu curso sobre un cambio de planes para una actividad (por ejemplo, un trabajo en grupo). Usa neither…nor, either…or, though, as a result, as soon as y unless (al menos cuatro de los seis). Revisa la puntuación y que cada conector relacione dos ideas.", "Ejemplo: Subject: Change of plan. Neither Ana nor Leo can come on Friday, so we will meet on Monday. Either the library or the classroom will be free. I will send the notes as soon as I finish. We cannot start unless everyone brings the draft. As a result, please check your messages.", ["usa al menos cuatro conectores", "no usa doble negación", "revisa la puntuación"], ["correo escrito de cinco oraciones"], ["usar as soon as con will", "usar though como porque"], "Pide a una persona de tu casa que marque los conectores y diga qué relación crea cada uno."),
    "Escribe diez oraciones con distintos conectores sobre tu semana.",
    "Reescribe un párrafo corto de tu cuaderno agregando tres conectores de la clase.",
)

# ================================================== clase 4: énfasis y reporte
BLOG4 = "Entrada de blog de ejemplo: «We built the stage ourselves. My brother taught himself to play the guitar, and my cousin made the posters herself. The teacher said that the show was a success. She told us to rest. Our neighbour said that she had seen the posters on the street. A friend told me to write about it.»\n(stage = escenario, taught = enseñó, posters = afiches, success = éxito, rest = descansar, neighbour = vecina, street = calle)"

lesson(
    OA, 4, MAT_READ,
    "Aprenderé a escribir énfasis en quien realiza la acción con pronombres reflexivos y a informar por escrito lo que otros dicen (said that, told… to). Sirve para escribir relatos, noticias y entradas de blog con voces claras.",
    ["Sé el pasado simple.", "Sé los pronombres personales."],
    [
        "Los pronombres reflexivos (reflexive pronouns) son myself, yourself, himself, herself, itself, ourselves, yourselves y themselves. Para enfatizar quién hace la acción se ponen después del sujeto o al final de la oración: We built the stage ourselves. My cousin made the posters herself. Para decir que alguien hace algo a sí mismo se usan sin énfasis: She taught herself. Elige el reflexivo según el sujeto.",
        "Para informar lo que otros dicen (reported speech) se usan said that + oración o told + persona + to + verbo. The teacher said that the show was a success. She told us to rest. En el texto escrito, el tiempo suele retroceder: «The show is a success» pasa a She said the show was a success. «I have seen» pasa a She said she had seen. No se usan comillas en el estilo indirecto.",
        "En el estilo directo se usan comillas (quotation marks): The teacher said, “The show is a success.” Compara los dos estilos y elige el que convenga. Al revisar, comprueba: ¿el reflexivo concuerda con el sujeto?, ¿usé said that o told + persona?, ¿cambié el tiempo y los pronombres?",
    ],
    [("himself / herself", "reflexivos de he / she"), ("ourselves / themselves", "reflexivos de we / they"), ("said that", "dijo que"), ("told me to", "me dijo que"), ("reported speech", "estilo indirecto"), ("quotation marks", "comillas")],
    [
        ("Reflexivo", "Completa: «My sister made the cake ___.» A) herself B) himself", ["El sujeto es my sister.", "El reflexivo es herself.", "La A."], "A"),
        ("Estilo indirecto", "Pablo dijo: «I am happy.» ¿Cómo lo escribes en estilo indirecto? A) Pablo said he was happy. B) Pablo said I am happy.", ["Cambian el pronombre y el tiempo.", "La A.", "La B no los cambia."], "A"),
    ],
    [
        ("Escribir My brother taught itself.", "El reflexivo debe coincidir con el sujeto.", "Escribe himself."),
        ("Escribir She told that we rest.", "Told lleva persona y to.", "Escribe She told us to rest."),
    ],
    [
        ("Lee: " + BLOG4 + " ¿Quiénes construyeron el escenario? A) ellos mismos B) los profesores", "A", "Dice We built the stage ourselves."),
        ("Lee: " + BLOG4 + " ¿Qué instrumento aprendió el hermano por sí mismo? A) la guitarra B) el piano", "A", "Dice taught himself to play the guitar."),
        ("Lee: " + BLOG4 + " ¿Qué dijo la profesora sobre el espectáculo? A) que fue un éxito B) que fue largo", "A", "Dice the show was a success."),
    ],
    [
        ("Lee: " + BLOG4 + " ¿Qué les dijo la profesora que hicieran? A) que descansaran B) que ensayaran", "A", "Dice She told us to rest."),
        ("Lee: " + BLOG4 + " ¿Qué había visto la vecina? A) los afiches en la calle B) el escenario", "A", "Dice she had seen the posters on the street."),
        ("Lee: " + BLOG4 + " ¿Qué reflexivo usa para la prima? A) herself B) himself", "A", "Dice my cousin made the posters herself."),
    ],
    [
        ("Completa: «The students prepared the show ___.» A) themselves B) himself", "A", "El sujeto es plural: the students."),
        ("Completa: «Ana said that she ___ tired.» A) was B) is", "A", "En estilo indirecto el presente retrocede al pasado."),
        ("Completa: «Our coach told us ___ early.» A) to arrive B) arrive", "A", "Told + persona + to + verbo."),
    ],
    [
        ("Lee: " + BLOG4 + " Un compañero escribe She told that we rest. ¿Qué corrige? A) She told us to rest B) She said us rest", "A", "Told necesita persona y to."),
        ("Lee: " + BLOG4 + " ¿Cuál es el estilo directo de The teacher said that the show was a success? A) The teacher said, “The show is a success.” B) The teacher said, “The show was.”", "A", "En estilo directo el presente se mantiene."),
    ],
    [
        ("Elige la oración con el reflexivo correcto: A) I fixed the bike myself. B) I fixed the bike himself.", "A", "El sujeto es I; el reflexivo es myself."),
        ("Une cada oración directa con su reporte. 1) “I am busy.” 2) “I will call.” 3) “Go home.” Reportes: a) She said she would call. b) She told me to go home. c) She said she was busy.", "1-c, 2-a, 3-b", "Am pasa a was, will a would y la orden usa told + to."),
    ],
    [("Lee: «My friend said that she had painted the room herself. Her father told her to wear old clothes.» (painted = pintó, wear = usar). ¿Quién pintó el cuarto?", "Ella misma", "Dice she had painted the room herself.")],
    [
        ("¿Qué reflexivo corresponde a they?", "Themselves", "Enfatiza quién hace la acción."),
        ("¿Qué estructura se usa con told (en escritura de funciones)?", "Told + persona + to + verbo", "She told me to go."),
        ("¿Se usan comillas en el estilo indirecto?", "No", "Solo en el estilo directo."),
    ],
    task("Escribe una entrada de blog de cinco oraciones sobre una actividad que organizaron tú y tus compañeros. Usa dos pronombres reflexivos (ourselves, themselves, myself…), una oración con said that y una con told… to. Revisa que el reflexivo concuerde y que cambies el tiempo y los pronombres en el estilo indirecto.", "Ejemplo: We organised the sports day ourselves. Ana made the poster herself. The director said that the day was a success. He told us to clean the court. A friend said she had enjoyed it.", ["usa dos reflexivos correctos", "usa said that y told… to", "cambia bien el tiempo y los pronombres"], ["entrada de blog de cinco oraciones"], ["usar itself para una persona", "no cambiar el tiempo en el estilo indirecto"], "Lee tu texto a una persona de tu casa y pregunta quién hizo cada acción."),
    "Reescribe cinco frases con estilo directo como estilo indirecto.",
    "Escribe una noticia breve de seis oraciones que incluya dos citas indirectas.",
)

# ================================================== clase 5: acciones anteriores a otra en el pasado
STORY5W = "Texto de ejemplo: «When Elena arrived at the stadium, the match had already started. She had left her ticket at home, so she had to ask her friend for help. By the time her friend came, the first half had ended. She hadn’t eaten anything, because she had been in a hurry. Then she bought a sandwich and watched the second half.»\n(stadium = estadio, match = partido, ticket = entrada, half = tiempo, ended = terminó, in a hurry = apurada, bought = compró)"

lesson(
    OA, 5, MAT_READ,
    "Aprenderé a escribir acciones que ocurrieron antes de otra acción en el pasado con el pasado perfecto (had + participio), usando señales como when, before, after, by the time y already. Sirve para escribir relatos y explicar causas con orden.",
    ["Sé el pasado simple.", "Sé algunos participios irregulares."],
    [
        "El pasado perfecto (past perfect) se forma con had + participio pasado: had started, had left, had eaten. Se usa para la acción que ocurrió primero cuando hay dos acciones en el pasado: When Elena arrived, the match had already started. La acción más reciente va en pasado simple (arrived) y la anterior en pasado perfecto (had started). Muchos participios son irregulares: left, eaten, bought, written, lost, gone.",
        "La forma negativa es hadn’t (had not) + participio: She hadn’t eaten anything. La pregunta pone had antes del sujeto: Had she eaten? Se responde Yes, she had o No, she hadn’t. Las señales que ayudan: already (ya), before (antes), after (después), by the time (para cuando), when (cuando) y the day before (el día anterior). Con because se explican causas: She was hungry because she hadn’t eaten.",
        "Al escribir un relato, ordena los hechos y usa pasado perfecto solo para lo anterior. Si todas las acciones van en pasado perfecto, el texto se vuelve confuso. Revisa los participios, la concordancia y las comas. Lee tu texto y pregúntate: ¿se entiende qué ocurrió primero?",
    ],
    [("past perfect", "pasado perfecto"), ("had + participle", "had + participio"), ("hadn’t", "no había"), ("already", "ya"), ("by the time", "para cuando"), ("the day before", "el día anterior")],
    [
        ("Elegir la forma", "Completa: «When I arrived, they ___ the room.» A) had cleaned B) have clean", ["La limpieza ocurrió antes de que llegara.", "Se usa had cleaned.", "La A."], "A"),
        ("Orden de hechos", "Frase: «She had left before the rain started.» ¿Qué ocurrió primero? A) se fue B) llovió", ["Had left es el pasado perfecto.", "Ocurrió primero.", "La A."], "A"),
    ],
    [
        ("Escribir had went.", "Después de had va el participio gone.", "Escribe had gone."),
        ("Usar pasado perfecto en todas las oraciones.", "No se distingue qué ocurrió primero.", "Usa pasado simple para el hecho más reciente."),
    ],
    [
        ("Lee: " + STORY5W + " ¿Qué había dejado en casa Elena? A) su entrada B) su teléfono", "A", "Dice She had left her ticket at home."),
        ("Lee: " + STORY5W + " ¿Cómo estaba el partido cuando llegó? A) ya había empezado B) estaba por terminar", "A", "Dice the match had already started."),
        ("Lee: " + STORY5W + " ¿Qué compró al final? A) un sándwich B) una camiseta", "A", "Dice she bought a sandwich."),
    ],
    [
        ("Lee: " + STORY5W + " ¿Por qué no había comido? A) porque estaba apurada B) porque no tenía hambre", "A", "Dice because she had been in a hurry."),
        ("Lee: " + STORY5W + " ¿Qué había terminado cuando llegó su amigo? A) el primer tiempo B) el partido", "A", "Dice the first half had ended."),
        ("Completa: «By the time he called, I ___ asleep.» A) had fallen B) have fall", "A", "Se necesita had + participio."),
    ],
    [
        ("Elige la forma negativa correcta: A) She hadn’t eaten. B) She didn’t had eaten.", "A", "La negación se hace con hadn’t + participio."),
        ("Lee: " + STORY5W + " ¿Cuál es el participio de leave? A) left B) leaved", "A", "Es un verbo irregular."),
        ("Lee: " + STORY5W + " ¿Qué ocurrió primero? A) Elena dejó la entrada en casa B) Elena compró un sándwich", "A", "Había dejado la entrada antes de llegar."),
    ],
    [
        ("Lee: " + STORY5W + " Un compañero reescribe: Elena arrived and the match started. ¿Qué cambia? A) ya no se sabe que el partido empezó antes B) todo está igual", "A", "Se pierde el pasado perfecto."),
        ("Escribe la pregunta correcta: A) Had you finished the report? B) Did you had finished the report?", "A", "En pasado perfecto se invierte had y el sujeto."),
    ],
    [
        ("Ordena de primero a último: a) llegó al estadio b) dejó la entrada en casa c) compró el sándwich", "b, a, c", "Primero dejó la entrada, luego llegó y al final compró."),
        ("Une cada frase con su señal. 1) already 2) by the time 3) the day before. Significados: a) para cuando b) ya c) el día anterior", "1-b, 2-a, 3-c", "Cada señal acompaña el pasado perfecto."),
    ],
    [("Lee: «Leo was nervous because he hadn’t practised enough. He had studied for two hours, but he had forgotten the last part.» (nervous = nervioso, practised = practicó, forgotten = olvidado). ¿Cuántas horas había estudiado?", "2", "Dice for two hours.")],
    [
        ("¿Cómo se forma el pasado perfecto (en escritura de funciones)?", "Had + participio", "Marca la acción anterior."),
        ("¿Cómo se niega?", "Hadn’t + participio", "She hadn’t eaten."),
        ("¿Qué indica already?", "Que la acción ya había ocurrido", "Va con el pasado perfecto."),
    ],
    task("Escribe un relato de cinco oraciones sobre un día en que algo salió distinto de lo planeado. Usa tres frases con pasado perfecto (una afirmativa, una negativa y una con because), una con already o by the time, y revisa los participios irregulares. Cuenta qué ocurrió primero.", "Ejemplo: When I arrived, the bus had already gone. I hadn’t checked the schedule because I had been in a hurry. By the time my friend came, I had waited an hour. We took a taxi. It was a long day.", ["usa tres veces had + participio", "incluye already o by the time", "cuenta bien qué ocurrió primero"], ["relato escrito de cinco oraciones"], ["usar had went", "poner todo en pasado perfecto"], "Pide a una persona de tu casa que te cuente qué ocurrió primero y compara."),
    "Escribe cinco participios irregulares con su verbo base.",
    "Reescribe un párrafo corto en pasado simple usando pasado perfecto en las acciones anteriores.",
)
