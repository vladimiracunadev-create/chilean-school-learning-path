"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 11 (clases 3 a 5): trama y conflicto, expresiones y vocabulario, análisis integrado.

Continúa student_content_in_m2_b (clases 1 y 2). Textos literarios originales y breves, con glosario en español dentro del
enunciado. Inglés americano. Los títulos de clase del plan son genéricos; aquí se aplican a trama (inicio, desarrollo, final)
y conflicto, expresiones idiomáticas y vocabulario temático, y análisis integrado de un cuento, un poema y una tira cómica.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 11"

# ------------------------------------------------------------------ clase 3: trama y conflicto
ST1 = "«The Lost Letter (original story). Nico found a letter on the street addressed to Mrs. Alba, an old neighbor. He wanted to read it, but he knew it was private. After a long walk, he left it in her mailbox. The next day, she thanked him with a smile.» (letter = carta, addressed to = dirigida a, private = privada, mailbox = buzón, thanked = agradeció)"
ST2 = "«The Fog on the Pass (original story). Four hikers crossed a mountain pass. Clouds came fast, and the wind grew strong. The path disappeared in the fog. They stopped, waited until the fog opened, and walked back together.» (pass = paso de montaña, hikers = excursionistas, clouds = nubes, wind = viento, path = sendero, fog = niebla, waited = esperaron)"
ST3 = "«Two Sisters (original story). Lía and Eva shared a room. Lía loved loud music, but Eva needed silence to study. They argued every evening. One day, they made a schedule: music from five to six, silence after six. Both felt relieved.» (shared = compartían, loud = fuerte, silence = silencio, argued = discutían, schedule = horario, relieved = aliviadas)"
ST4 = "«The Red Ribbon (original story). In the village of Ardent, everyone had to wear gray. Tamar loved colors. She sewed a red ribbon and wore it to the market. At first, people stared. Then a child laughed and asked for a ribbon too. By the end of the year, the market was full of colors.» (village = aldea, wear = vestir, gray = gris, sewed = cosió, ribbon = cinta, stared = miraron fijo, market = feria)"
ST5 = "«The Piano (original story). Dani wanted to play at the school concert, but she was afraid of making a mistake. Every night, she practiced alone. On the day of the concert, her hands shook. She played the first notes slowly, took a breath and finished the song. The audience clapped.» (afraid = con miedo, mistake = error, practiced = practicaba, shook = temblaron, notes = notas, breath = respiración, audience = público, clapped = aplaudió)"

lesson(
    OA, 3, MAT_R,
    "Aprenderé a reconocer la trama (inicio, desarrollo y final) y el conflicto de un cuento: qué problema enfrenta el personaje, contra quién o contra qué, y cómo se resuelve. Sirve para explicar la estructura de una historia con evidencia.",
    ["Sé reconocer personajes y entorno.", "En 1.º medio vi el conflicto como un problema del personaje."],
    [
        "La trama (plot) es la secuencia de hechos de un relato. Tiene tres partes. El inicio (beginning) presenta a los personajes, el entorno y el problema. El desarrollo (development) muestra los hechos que aumentan la tensión hasta el momento de mayor tensión, llamado clímax (climax) o punto de giro. El final (end) muestra cómo se resuelve el problema o cómo cambia la situación.",
        "El conflicto (conflict) es el problema central. Puede ser de varios tipos: persona contra persona (person vs person), como dos hermanas que discuten; persona contra sí misma (person vs self), como una tentación o un miedo; persona contra la naturaleza (person vs nature), como una niebla en una montaña; y persona contra la sociedad (person vs society), como una regla que todos siguen. Para nombrar el conflicto, pregunta: ¿qué quiere el personaje y qué se lo impide?",
        "Al explicar, usa la estructura Beginning:... Development:... Climax:... End:... y agrega una pista del texto. Si una escena no cambia la situación, probablemente no es el clímax. El clímax es el punto en que el personaje debe actuar o decidir.",
    ],
    [("plot", "trama"), ("beginning / development / end", "inicio / desarrollo / final"), ("climax", "clímax: momento de mayor tensión"), ("conflict", "conflicto"), ("person vs self", "persona contra sí misma"), ("person vs nature / society", "persona contra la naturaleza / la sociedad")],
    [
        ("Partes de la trama", ST1 + " ¿Qué ocurre en el inicio, el desarrollo y el final?", ["Inicio: Nico encuentra una carta para la Sra. Alba.", "Desarrollo: quiere leerla, pero sabe que es privada, y camina un rato.", "Final: la deja en el buzón y ella le agradece."], "Inicio: encuentra la carta. Desarrollo: duda por la privacidad. Final: la deja en el buzón y ella le agradece"),
        ("Tipo de conflicto", ST2 + " ¿Qué tipo de conflicto es y cómo se resuelve?", ["Los excursionistas quieren cruzar el paso.", "La niebla y el viento se lo impiden.", "Es persona contra la naturaleza; se resuelve esperando y regresando juntos."], "Persona contra la naturaleza; esperan a que se abra la niebla y regresan juntos"),
    ],
    [
        ("Llamar conflicto a un personaje o a un lugar.", "El conflicto es un problema, no una persona ni un lugar.", "Nómbralo con una frase: ¿qué quiere y qué se lo impide?"),
        ("Pensar que el clímax es el final.", "El clímax es el punto de mayor tensión; el final muestra la resolución.", "Busca el momento en que el personaje decide o actúa."),
    ],
    [
        mr(ST3, "¿Qué tipo de conflicto hay?", "Persona contra persona", ["Persona contra la naturaleza", "Persona contra la sociedad"], "Las dos hermanas tienen necesidades distintas en la misma habitación."),
        mr(ST3, "¿Cómo se resuelve el conflicto?", "Con un horario compartido de música y silencio", ["Una duerme en la casa de una amiga", "Dejan de hablarse por unos días"], "Dice they made a schedule."),
        mr(ST4, "¿Quién se opone a Tamar al comienzo?", "La regla del pueblo de vestir de gris", ["La falta de dinero para comprar telas de colores", "El frío del invierno en la aldea"], "Dice everyone had to wear gray."),
    ],
    [
        mr(ST4, "¿Qué tipo de conflicto es?", "Persona contra la sociedad", ["Persona contra la naturaleza", "Persona contra sí misma"], "Tamar enfrenta una regla de todo el pueblo."),
        mr(ST5, "¿Qué miedo enfrenta Dani?", "Equivocarse frente al público", ["Perder el piano antes del concierto", "Llegar tarde al día del concierto"], "Dice she was afraid of making a mistake."),
        mr(ST1, "¿Cuál es el conflicto interno de Nico?", "Quiere leer la carta, pero sabe que es privada y de otra persona", ["No sabe dónde vive Mrs. Alba ni cómo entregarla", "No tiene tiempo para ir a su casa"], "Es una tentación contra su sentido de respeto."),
    ],
    [
        mr(ST5, "¿Cuál es el clímax del cuento?", "Cuando sus manos tiemblan y toca las primeras notas del concierto", ["Cuando practica cada noche a solas antes del concierto", "Cuando el público aplaude al final del concierto"], "Es el momento de mayor tensión y decisión."),
        mr(ST4, "¿Qué parte del texto marca el desarrollo?", "Tamar usa la cinta y un niño pide una", ["En la aldea de Ardent todos debían vestir de gris", "Al final del año la feria estaba llena de colores"], "Las otras dos son inicio y final."),
        arith("En un ejemplo inventado sobre la feria de Tamar, había 20 puestos grises al comienzo y, al final del año, 15 ya tenían colores. ¿Cuántos puestos seguían grises?", "20-15", "Se restan los puestos de colores de los puestos totales.", " puestos"),
    ],
    [
        mr(ST2, "Un lector dice que el clímax es cuando regresan juntos. ¿Qué respuesta es más acertada?", "El clímax es cuando el sendero desaparece en la niebla; regresar es la resolución", ["Tiene razón: regresar juntos es el clímax porque es el final del cuento", "No hay clímax, porque el cuento no tiene problema"], "El punto de mayor tensión es la pérdida del sendero."),
        mr(ST1, "Otro lector dice que Nico gana porque obtiene dinero. ¿Qué falla?", "El texto no menciona dinero; la recompensa es la sonrisa de la señora Alba", ["Que Nico no es el protagonista del cuento, sino la señora Alba", "Que el cuento termina antes de que ella responda"], "La resolución es moral, no material."),
    ],
    [
        mr(ST3 + " " + ST4, "Compara los conflictos de los dos cuentos. ¿Qué tienen en común?", "Ambos se resuelven con un cambio o un acuerdo que permite convivir mejor", ["En ambos, el conflicto es persona contra sí misma", "En ambos, un adulto impone la solución a los demás desde el principio"], "En los dos cuentos, el cambio permite la convivencia."),
        mr(ST5, "¿Qué conflicto resume mejor el cuento de Dani?", "Dani quiere tocar en el concierto, pero el miedo a equivocarse se lo impide", ["Dani quiere comprar un piano, pero no tiene dinero", "Dani quiere cambiarse a otra escuela, pero sus padres no la dejan"], "Quiere tocar y el miedo la frena."),
    ],
    [mr(ST2, "Escribe un resumen de tres frases con inicio, desarrollo y final del cuento de los excursionistas. ¿Cuál es el más adecuado?", "Cuatro excursionistas cruzan un paso. La niebla borra el sendero. Esperan y regresan juntos", ["Cuatro excursionistas cruzan un paso y llegan a la cima. Celebran y bajan por otro camino", "Un excursionista se pierde en la niebla y los demás lo dejan atrás para llegar a tiempo"], "El resumen debe respetar los hechos del texto.")],
    [
        ("En Inglés de 2.º medio (OA 11, clase 3): ¿cuáles son las tres partes de la trama?", "Inicio, desarrollo y final", "En el desarrollo está el clímax."),
        ("En Inglés de 2.º medio (OA 11, clase 3): ¿qué es el clímax?", "El momento de mayor tensión de la historia", "Es el punto de giro."),
        ("En Inglés de 2.º medio (OA 11, clase 3): ¿qué tipo de conflicto es un personaje que debe decidir entre dos deseos propios?", "Persona contra sí misma", "El obstáculo está dentro del personaje."),
    ],
    task("Lee: «The Race (original story). Maya wanted to win the school race, but her friend Tito had hurt his foot. Maya was in first place when she saw Tito sitting alone. She stopped, helped him to the finish line and finished last. The crowd cheered for both.» (race = carrera, hurt = lastimado, foot = pie, finish line = meta, crowd = público, cheered = vitoreó). Escribe en tu hoja: inicio, desarrollo, clímax, final, tipo de conflicto y la pista del texto que lo muestra.", "Inicio: Maya quiere ganar. Desarrollo: ve a Tito solo. Clímax: se detiene. Final: lo ayuda y todos los aplauden. Conflicto: persona contra sí misma (ganar o ayudar). Pista: she stopped, helped him.", ["identifica las cuatro partes de la trama", "nombra el tipo de conflicto", "cita una pista del texto"], ["ficha de seis líneas en la hoja"], ["confundir clímax con final", "nombrar un conflicto sin pista"], "Pide que explique qué habría pasado si Maya no se detenía."),
    "Resume en tres frases un cuento que conozcas, con inicio, desarrollo y final.",
    "Piensa en una película y nombra su conflicto y su tipo, sin contar el final.",
)

# ------------------------------------------------------------------ clase 4: expresiones idiomáticas y vocabulario temático
ID1 = "«After years of arguments, Mr. Ríos decided to turn over a new leaf. He stopped shouting at work and started to listen. His colleagues were surprised, but they were pleased.» (arguments = discusiones, shouting = gritar, colleagues = compañeros de trabajo, pleased = contentos)"
ID2 = "«Sofía had been patient with the noise for weeks. When the neighbors played loud music at midnight again, it was the last straw. She knocked on their door.» (patient = paciente, noise = ruido, midnight = medianoche, knocked = golpeó)"
ID3 = "«Leo broke the vase by accident. At first, he wanted to hide the pieces, but then he decided to face the music and tell his mother the truth.» (vase = jarrón, by accident = sin querer, hide = esconder, pieces = trozos, truth = verdad)"
ID4 = "«The day before the audition, Marta got cold feet. She thought of staying home, but her friend reminded her how much she had practiced.» (audition = audición, staying = quedarse, reminded = recordó)"
TM1 = "«The journey began at dawn. Ana studied the map, followed the path and looked for the destination. Soon she was lost, but a kind stranger showed her the way.» (journey = viaje, dawn = amanecer, map = mapa, path = sendero, destination = destino, lost = perdida, stranger = desconocido)"
TM2 = "«The shadow in the corner made him shiver. His hands trembled, and he was afraid to move. Then the cat jumped out, and he laughed in relief.» (shadow = sombra, corner = rincón, shiver = estremecerse, trembled = temblaron, relief = alivio)"
TM3 = "«Rita and Joel shared everything. They trusted each other and always supported one another. When Joel moved to another city, Rita burst into tears, but they promised to write every week.» (shared = compartían, trusted = confiaban, supported = apoyaban, moved = se mudó, burst into tears = rompió en llanto, promised = prometieron)"

lesson(
    OA, 4, MAT_R,
    "Aprenderé a entender expresiones idiomáticas y de uso frecuente en textos literarios (como turn over a new leaf, the last straw, face the music, get cold feet) y vocabulario temático de viaje, miedo y amistad. Sirve para comprender el sentido de un relato sin traducir palabra por palabra.",
    ["Sé que las expresiones no se traducen palabra por palabra.", "Conozco break the ice y a piece of cake."],
    [
        "Las expresiones idiomáticas aparecen mucho en la literatura. Turn over a new leaf significa empezar de nuevo de forma positiva. The last straw es el último problema que hace perder la paciencia. Face the music significa aceptar las consecuencias de lo que hiciste. Get cold feet significa sentir miedo y querer echarse atrás antes de algo importante. Burst into tears significa ponerse a llorar de repente. Para entenderlas, usa el contexto: ¿qué hace el personaje y cómo se siente? Las palabras y frases clave son las que sostienen la idea del relato, como lost y destination en una historia de viaje.",
        "El vocabulario temático son palabras de un tema. En un relato de viaje aparecen journey, path, map, destination, lost y stranger. En un relato de miedo, shadow, shiver, tremble, afraid y relief. En un relato de amistad, trust, share, support, promise y miss. Si conoces el tema, puedes anticipar las palabras y entender el ambiente.",
        "Para responder preguntas, relaciona la expresión con la situación. En Sofía had been patient... it was the last straw, la paciencia estaba agotada. Pregúntate si el sentido literal tendría lógica; si no, es una expresión idiomática. Escribe su significado en tus palabras.",
    ],
    [("turn over a new leaf", "empezar de nuevo, de forma positiva"), ("the last straw", "la gota que rebalsó el vaso"), ("face the music", "aceptar las consecuencias"), ("get cold feet", "arrepentirse por miedo"), ("burst into tears", "ponerse a llorar de repente"), ("journey / destination", "viaje / destino")],
    [
        ("Entender una expresión por el contexto", ID1 + " ¿Qué quiere decir turn over a new leaf?", ["El Sr. Ríos dejó de gritar y empezó a escuchar.", "Cambió su forma de comportarse.", "La expresión significa empezar de nuevo, de forma positiva."], "Empezar de nuevo, de forma positiva"),
        ("Vocabulario temático", TM2 + " ¿Qué tema domina el texto y qué palabras lo muestran?", ["Hay sombra, estremecerse y temblar.", "Todas son palabras de miedo.", "El final trae alivio."], "El miedo; shadow, shiver, trembled y afraid lo muestran"),
    ],
    [
        ("Traducir the last straw como la última paja.", "Es una expresión que significa la gota que rebalsó el vaso.", "Busca en el contexto la paciencia que se agota."),
        ("Confundir face the music con tocar música.", "Significa aceptar las consecuencias.", "Mira qué decide hacer el personaje."),
    ],
    [
        mr(ID2, "¿Qué significa the last straw en este texto?", "El último problema que acabó con su paciencia", ["Un objeto que se rompe cuando se carga demasiado", "Una comida que Sofía prepara para los vecinos"], "Sofía había sido paciente por semanas y esto fue demasiado."),
        mr(ID3, "¿Qué decide hacer Leo al face the music?", "Contarle la verdad a su mamá sobre el jarrón", ["Esconder los trozos del jarrón", "Culpar a su hermano menor"], "Face the music es aceptar las consecuencias."),
        mr(ID4, "¿Qué le pasó a Marta antes de la audición?", "Sintió miedo y pensó en echarse atrás", ["Se puso muy contenta", "Perdió su instrumento"], "Get cold feet indica arrepentimiento por miedo."),
    ],
    [
        mr(TM1, "¿Qué palabras muestran el tema del viaje?", "journey, map, path y destination", ["shadow, shiver y trembled", "trust, share y support"], "Son las palabras del tema viaje."),
        mr(TM3, "¿Qué significa burst into tears?", "Ponerse a llorar de repente", ["Reírse a carcajadas", "Sentir miedo"], "El contexto es la despedida de un amigo."),
        mr(TM2, "¿Qué sentimiento hay al final del texto del miedo?", "Alivio", ["Más miedo", "Enojo"], "Dice he laughed in relief."),
    ],
    [
        mc("Completa con la expresión correcta: After the argument, he decided to ____ a new leaf.", "turn over", ["turn around", "take over"], "Se dice turn over a new leaf."),
        mc("Completa con la palabra correcta: Rita and Joel are best friends. They trust and ____ each other.", "support", ["mistrust", "ignore"], "Support es una palabra del tema de la amistad; las otras contradicen el sentido de mejores amigos."),
        mr(TM1, "Completa con la palabra del tema: Ana followed the ____ to the destination.", "path", ["shadow", "tears"], "Path es el sendero del viaje."),
    ],
    [
        mr(ID1, "Un lector dice que turn over a new leaf es dar vuelta una hoja de árbol. ¿Qué respuesta es más acertada?", "No: es una expresión; significa empezar de nuevo y cambiar de conducta", ["Sí: el texto habla de un árbol que pierde sus hojas", "No: significa dejar un trabajo por otro"], "El contexto habla de un cambio de conducta."),
        mr(ID2, "Otro lector dice que the last straw significa que fue la primera vez que hicieron ruido. ¿Qué respuesta es mejor?", "No: significa que fue el último de varios problemas", ["Sí: fue la primera vez", "Sí: fue la mejor vez"], "El texto dice que Sofía ya había sido paciente por semanas."),
    ],
    [
        mr(TM3, "¿Qué palabras muestran el tema de la amistad?", "shared, trusted y supported", ["shadow, shiver y afraid", "journey, map y path"], "Son las palabras de amistad."),
        mr(ID4, "¿Qué le recordó su amiga a Marta?", "Lo mucho que había practicado", ["Que no sabía tocar", "Que llegaba tarde"], "Dice reminded her how much she had practiced."),
    ],
    [mr(ID3, "¿Qué expresión de la lista usarías para describir que un personaje confiesa lo que hizo y acepta el castigo?", "Face the music", ["Get cold feet", "Burst into tears"], "Es aceptar las consecuencias de un acto.")],
    [
        ("En Inglés de 2.º medio (OA 11, clase 4): ¿qué significa get cold feet?", "Arrepentirse por miedo antes de algo importante", "Es una expresión idiomática."),
        ("En Inglés de 2.º medio (OA 11, clase 4): ¿qué significa the last straw?", "El último problema que agota la paciencia", "Se parece a la gota que rebalsa el vaso."),
        ("En Inglés de 2.º medio (OA 11, clase 4): ¿cómo se entiende una expresión nueva en un relato?", "Con el contexto de la situación y de los sentimientos", "El sentido literal no suele funcionar."),
    ],
    task("Lee: «Cata had been planning her first solo trip for months. The night before, she got cold feet and burst into tears. Her older brother said, Talk to Mom. Mom hugged her. Cata packed her map and, at dawn, began her journey.» (planning = planeando, solo trip = viaje sola, talk = habla, hugged = abrazó, packed = guardó). Escribe el significado de dos expresiones, tres palabras de vocabulario temático de viaje y el tema del texto.", "Get cold feet: sintió miedo y quiso echarse atrás. Burst into tears: se puso a llorar de repente. Vocabulario: trip, map, journey. Tema: enfrentar los miedos con apoyo permite avanzar.", ["explica dos expresiones", "nombra tres palabras temáticas", "escribe el tema"], ["hoja con tres respuestas"], ["traducir palabra por palabra", "confundir tema con asunto"], "Pide que explique en qué parte supo el significado de cada expresión."),
    "Escribe el significado en español de los seis términos del vocabulario de la clase.",
    "Busca en una canción en español un modismo y compara con uno en inglés.",
)

# ------------------------------------------------------------------ clase 5: análisis integrado
IN1 = "«The Baker's Apprentice (original story). Teo wanted to be a baker, but his master, Mr. Vera, only asked him to wash the trays. Teo felt it was unfair. One evening, a customer ordered a birthday cake for the next morning. Mr. Vera was ill, and nobody else could bake it. Teo was not sure he could do it. He took a deep breath, remembered everything he had watched, and baked it. The next day, Mr. Vera handed him an apron with his name on it.» (baker = panadero, apprentice = aprendiz, master = maestro, wash = lavar, trays = bandejas, unfair = injusto, customer = cliente, ordered = encargó, ill = enfermo, bake = hornear, sure = seguro, apron = delantal)"
IN2 = "«Poem (original): The Lamp. / In the window, a small lamp, / it waits for you at night. / It does not shine for the whole street, / only for your way home.» (lamp = lámpara, window = ventana, shine = brillar, whole = entera, way home = camino a casa)"
IN3 = "Tira cómica (cuatro cuadros). Cuadro 1: Una niña mira un examen y dice: «I studied, but I am nervous». Cuadro 2: Camina por el pasillo repitiendo palabras. Cuadro 3: Entra a la sala y respira. Cuadro 4: Sale sonriendo y dice: «It was not so bad.» (exam = examen, nervous = nerviosa, hall = pasillo, breathes = respira, smiling = sonriendo, not so bad = no tan malo)"

lesson(
    OA, 5, MAT_R,
    "Aprenderé a analizar de forma integrada un cuento, un poema y una tira cómica: tema, personajes y caracterización, entorno, trama, conflicto y expresiones. Sirve para mostrar con evidencia lo que entiendo de un texto literario.",
    ["Sé identificar tema, personajes, entorno y trama.", "Conozco expresiones y vocabulario temático."],
    [
        "El análisis integrado reúne todos los elementos literarios. Primero identifica el género (cuento, poema, tira cómica). Segundo, el entorno: tiempo y lugar. Tercero, los personajes y su caracterización con evidencia. Cuarto, el conflicto y la trama: inicio, desarrollo, clímax y final. Quinto, el tema, escrito como una idea general y apoyado con dos pistas. Sexto, las palabras y expresiones clave.",
        "Usa una ficha con una fila para cada elemento y una columna de evidencia. Cada respuesta debe tener una cita o una acción del texto. Por ejemplo: Teo is determined (rasgo); he baked the cake (evidencia); the conflict is person vs self, because he doubts himself (conflicto). En un poema, el entorno puede ser un lugar simbólico y el tema aparece en imágenes. En una tira cómica, las viñetas y los gestos son parte de la evidencia.",
        "Revisa tu ficha con tres preguntas: ¿está cada afirmación apoyada en el texto?, ¿el tema es una idea completa y no solo un objeto? y ¿el conflicto responde qué quiere el personaje y qué se lo impide? Si algo falla, vuelve al texto.",
    ],
    [("literary analysis", "análisis literario"), ("evidence", "evidencia: dato del texto"), ("setting", "entorno: tiempo y lugar"), ("trait", "rasgo del personaje"), ("theme", "tema: idea general"), ("imagery", "imágenes del poema")],
    [
        ("Analizar un cuento", IN1 + " ¿Cuál es el conflicto y cómo se resuelve?", ["Teo quiere ser panadero, pero solo lava bandejas.", "El conflicto es que no le dan oportunidad.", "Se resuelve cuando hornea la torta y recibe un delantal."], "Teo quiere ser panadero y no le dan oportunidad; la consigue al hornear la torta y recibe un delantal"),
        ("Analizar una tira cómica", IN3 + " ¿Cuál es el tema?", ["La niña está nerviosa al comienzo.", "Se prepara y entra respirando.", "Sale sonriendo: enfrentar un examen con calma ayuda."], "Enfrentar los nervios con calma permite salir adelante"),
    ],
    [
        ("Responder sin evidencia.", "Una afirmación sin cita es una opinión.", "Agrega una pista o una acción del texto."),
        ("Escribir el tema como una sola palabra.", "Un tema es una idea completa.", "Escríbelo como oración."),
    ],
    [
        mr(IN1, "¿Cuál es el entorno del cuento?", "Una panadería", ["Un colegio", "Una montaña"], "Hay un maestro, un aprendiz y un cliente que encarga una torta."),
        mr(IN2, "¿Qué género es?", "Un poema", ["Una tira cómica", "Una obra de teatro"], "Tiene versos con imágenes."),
        mr(IN3, "¿Qué dice la niña en el último cuadro?", "It was not so bad", ["I studied, but I am nervous", "This is impossible"], "En el cuadro 4 sale sonriendo y dice It was not so bad."),
    ],
    [
        mr(IN1, "¿Qué rasgo muestra Teo al hornear la torta?", "Determinación", ["Pereza", "Egoísmo"], "Se anima y hornea a pesar de su duda."),
        mr(IN2, "¿Qué muestra la imagen de una lámpara que brilla solo para tu camino a casa?", "Cuidado personal por alguien", ["Mucha luz para toda la calle", "Miedo a la oscuridad"], "La lámpara es para una persona, no para toda la calle."),
        mr(IN3, "¿Cuál es el clímax de la tira?", "Cuando entra a la sala y respira", ["Cuando mira el examen", "Cuando sonríe"], "Es el momento de mayor tensión."),
    ],
    [
        mr(IN1, "¿Qué parte es el final del cuento?", "Mr. Vera le da un delantal con su nombre", ["Teo lava las bandejas de la panadería", "Un cliente encarga una torta de cumpleaños"], "Es la resolución."),
        mr(IN2, "¿Cuál es el tema del poema?", "El cariño es una luz que acompaña a alguien", ["Una lámpara que se queda en la ventana de noche", "La noche es oscura y la calle está vacía"], "Es una idea general apoyada en la imagen."),
        mr(IN3, "¿Qué ocurre justo antes de que la niña entre a la sala?", "Camina por el pasillo repitiendo palabras", ["Sale sonriendo y dice que no fue tan malo", "Mira el examen y dice que está nerviosa"], "Es el cuadro 2: se prepara repitiendo palabras antes de entrar."),
    ],
    [
        mr(IN1, "Un lector dice que el tema del cuento es «cakes». ¿Qué corriges?", "Que es un asunto; el tema sería: confiar en uno mismo permite crecer y aprender", ["Nada, porque una palabra clave resume bien todo el cuento de Teo", "Que cakes es el título"], "Un tema es una idea completa."),
        mr(IN1 + " " + IN3, "Compara los dos textos. ¿Qué tienen en común?", "Ambos personajes enfrentan una duda y la superan con calma", ["Los dos cuentos son de miedo y de suspenso", "Ninguno tiene conflicto, porque todo sale bien"], "Teo duda de sí mismo y la niña está nerviosa."),
    ],
    [
        mr(IN2, "Un lector dice que el poema es triste porque habla de la noche. ¿Qué respuesta es más acertada?", "No necesariamente: la lámpara que espera da calidez", ["Sí: la noche es siempre triste", "Sí: porque no hay personas"], "La imagen de la lámpara que espera es cálida."),
        arith("En un ejemplo inventado, Teo hornea 12 bandejas de pan y Mr. Vera vende 5 al mediodía. ¿Cuántas bandejas quedan?", "12-5", "Se restan las bandejas vendidas del total.", " bandejas"),
    ],
    [mr(IN1, "Escribe una evidencia que apoye que Teo se siente injustamente tratado al comienzo. ¿Cuál es la mejor?", "Teo felt it was unfair", ["A customer brought a broken clock", "Mr. Vera was ill"], "Es la frase que muestra su sentimiento.")],
    [
        ("En Inglés de 2.º medio (OA 11, clase 5): ¿qué debe tener cada afirmación del análisis?", "Evidencia del texto", "Es lo que distingue el análisis de la opinión."),
        ("En Inglés de 2.º medio (OA 11, clase 5): ¿cómo se escribe el tema?", "Como una idea completa", "No basta una palabra."),
        ("En Inglés de 2.º medio (OA 11, clase 5): ¿qué es el entorno?", "El tiempo y el lugar del texto", "Incluye el lugar y el momento."),
    ],
    task("Lee este cuento original: «Ana's Voice. Ana wanted to read her poem aloud at school, but she felt shy. In the hall, her knees shook. A classmate smiled at her. She began slowly, and the audience listened. When she finished, the room was silent for a second and then everyone clapped.» (aloud = en voz alta, shy = tímida, knees = rodillas, shook = temblaron, audience = público, silent = en silencio, clapped = aplaudieron). Completa una ficha con: entorno, personaje y rasgo con evidencia, conflicto, clímax, final, tema con dos pistas y una expresión o palabra temática.", "Entorno: un colegio. Personaje: Ana, tímida; her knees shook. Conflicto: persona contra sí misma. Clímax: she began slowly. Final: everyone clapped. Tema: enfrentar la timidez con apoyo da seguridad; pistas: a classmate smiled y the audience listened. Vocabulario: shy.", ["completa siete filas", "cada afirmación tiene evidencia", "escribe el tema como idea completa"], ["ficha de siete filas en la hoja"], ["responder sin evidencia", "escribir el tema como una palabra"], "Pide que cambie una evidencia por otra del texto y compruebe si el tema se mantiene."),
    "Haz una ficha de análisis con seis filas sobre el poema de la lámpara.",
    "Elige un cuento corto en español y haz una ficha de análisis con evidencias.",
)
