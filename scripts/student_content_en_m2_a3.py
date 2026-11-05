"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 03: estrategias para apoyar la comprensión de textos escuchados.

Las «escuchas» las lee una persona adulta en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Las acotaciones entre corchetes describen gestos o entonación que la persona adulta puede imitar. Textos originales, con pista en español.
Cada clase trabaja un grupo de estrategias del OA: predecir y escuchar con propósito; focalizar en frases clave y apoyos del hablante;
preguntar, confirmar y pedir repetición; inferir con claves de contexto y de voz; tomar notas y resumir.
"""
from __future__ import annotations

from en_m2_a_common import ADULT, MAT, arith, lesson, task

OA = "EN2M OA 03"

# ================================================== clase 1: predecir, propósito y conocimientos previos
FAIR = "«Good morning, everyone. Welcome to the careers fair. This year we have guests from a hospital, a bakery, a radio station and a bank. Each guest will speak for ten minutes. Then you can ask questions. Please choose two talks and listen for what the job needs: studies, skills and daily tasks.» (careers fair = feria de oficios, guests = invitados, bank = banco, skills = habilidades, daily tasks = tareas diarias)"
DOCTOR = "«I work in a children’s hospital. I start at seven, I check my patients and I talk to their families. To do this job, you need many years of studies, patience and good communication.» (children’s hospital = hospital infantil, patients = pacientes, patience = paciencia, communication = comunicación)"
BAKER = "«Our bakery opens at five in the morning. First, we make the dough, then we bake the bread. At eight, customers arrive. I like the smell of fresh bread, but I do not like waking up so early.» (dough = masa, bake = hornear, customers = clientes, smell = olor, fresh = fresco, waking up = despertarse)"

lesson(
    OA, 1, MAT,
    "Aprenderé a hacer predicciones antes de escuchar, a escuchar con un propósito y a usar lo que ya sé del tema, y luego a confirmar mis predicciones. Sirve para entender mejor un texto oral aunque tenga palabras nuevas.",
    ["Sé identificar el propósito y el tema de un texto oral.", "Sé que un texto tiene datos y detalles."],
    [
        "Una predicción (prediction) es una idea de lo que vas a oír, antes de oírlo. Se hace con el título, el contexto y lo que ya sabes (prior knowledge). Si el título dice careers fair, puedes predecir palabras como job, studies o skills. Después de escuchar, confirma (confirm) tu predicción: ¿ocurrió lo que pensabas? Si no, corrígela.",
        "Escuchar con un propósito (listening for a purpose) significa decidir qué quieres encontrar antes de oír: una hora, un nombre, una opinión o una instrucción. Cuando tienes un propósito, tu atención se enfoca en la información útil y no se pierde en palabras que no necesitas. Por ejemplo, si el propósito es saber qué estudios necesita un trabajo, buscas palabras como studies o years.",
        "Una buena rutina tiene tres pasos: antes de escuchar, predice y elige qué buscar; mientras escuchas, busca esas palabras y anota pistas; después, compara con tu predicción. Las predicciones no tienen que ser correctas: sirven para que el cerebro esté listo. Si una palabra nueva aparece, usa lo que ya sabes del tema para adivinar su significado.",
    ],
    [("prediction", "predicción: idea de lo que oiré"), ("prior knowledge", "conocimientos previos"), ("purpose", "propósito: lo que busco al escuchar"), ("confirm", "confirmar"), ("careers fair", "feria de oficios y profesiones")],
    [
        ("Predecir con un título", "El título de una charla es «My first day at a radio station». ¿Qué palabra esperas oír? A) microphone B) newspaper", ["Pienso en el tema: una estación de radio.", "Una palabra relacionada es microphone.", "Newspaper es de otro medio, no de la radio."], "A) microphone"),
        ("Elegir un propósito", ADULT + "«The lunch menu today is soup, rice with chicken and a fruit salad. Dessert is yogurt.» (menu = menú, dessert = postre). Si tu propósito es saber el postre, ¿qué palabra buscas?", ["Mi propósito es el postre.", "Busco la palabra dessert.", "Después de dessert dice yogurt."], "Yogurt"),
    ],
    [
        ("Pensar que una predicción incorrecta es un fracaso.", "La predicción solo prepara la atención; se corrige al escuchar.", "Compara con el texto y cambia tu idea si es necesario."),
        ("Escuchar sin decidir qué buscar.", "Sin propósito, toda la información parece igual de importante.", "Antes de escuchar, escribe una pregunta que quieres responder."),
    ],
    [
        (ADULT + FAIR + " ¿Cuántos minutos hablará cada invitado? A) diez B) veinte", "A", "El guion dice ten minutes."),
        (ADULT + DOCTOR + " ¿A qué hora empieza a trabajar la persona? A) a las siete B) a las seis", "A", "El guion dice I start at seven."),
        (ADULT + BAKER + " ¿A qué hora abre la panadería? A) a las cinco de la mañana B) a las ocho", "A", "El guion dice opens at five in the morning; las ocho es cuando llegan los clientes."),
    ],
    [
        (ADULT + FAIR + " ¿Qué le piden al estudiante hacer antes de escuchar a los invitados? A) elegir dos charlas y escuchar qué necesita el trabajo B) hacer una pregunta cada diez minutos", "A", "El guion dice choose two talks and listen for what the job needs."),
        (ADULT + DOCTOR + " Además de revisar a sus pacientes, ¿con quiénes habla la persona? A) con las familias de los pacientes B) con otros médicos", "A", "El guion dice I talk to their families."),
        (ADULT + BAKER + " Tu propósito es saber qué le gusta a la persona. ¿Qué palabra buscas? A) like B) arrive", "A", "Like señala una preferencia: I like the smell of fresh bread."),
    ],
    [
        ("Antes de escuchar un aviso con el título «Lost dog near the park», ¿qué dos palabras es mejor predecir? A) dog y park B) cake y exam", "A", "El título nombra los lugares y personajes del aviso."),
        (ADULT + BAKER + " ¿Qué le disgusta a la persona de su trabajo? A) levantarse tan temprano B) el olor del pan", "A", "Dice I do not like waking up so early."),
        (ADULT + DOCTOR + " Tu predicción antes de oír era que el texto hablaba de un banco. ¿Se confirma? A) no, habla de un hospital B) sí, habla de dinero", "A", "El guion dice children’s hospital, por eso se corrige la predicción."),
    ],
    [
        (ADULT + FAIR + " Un compañero predijo que habría un invitado de un circo. ¿Se confirma? A) no, los invitados son de un hospital, una panadería, una radio y un banco B) sí, el circo es uno de los invitados", "A", "El guion no nombra un circo."),
        (ADULT + DOCTOR + " ¿Qué dos cualidades menciona el texto, además de estudiar? A) paciencia y buena comunicación B) rapidez y fuerza", "A", "Dice patience and good communication."),
    ],
    [
        (ADULT + BAKER + " Ordena lo que ocurre en la panadería: a) llegan los clientes b) se hornea el pan c) se hace la masa", "c, b, a", "First, make the dough, then bake the bread y después llegan los clientes."),
        (ADULT + FAIR + " ¿Cuál de estos propósitos de escucha es más útil si necesitas decidir qué charla elegir? A) buscar qué necesita cada trabajo B) contar los invitados", "A", "El guion pide escuchar qué necesita cada trabajo para decidir bien."),
    ],
    [(ADULT + "«Excuse me, students. The science fair starts at ten in the main hall. Teams, please bring your posters before nine thirty. The teacher will give you a number.» (posters = afiches, hall = salón, give = dar). Predice qué palabra oirás después de «Teams, please bring your…» y confirma con el guion: ¿qué deben llevar?", "Los afiches antes de las nueve y media", "El guion dice bring your posters before nine thirty.")],
    [
        ("¿Qué es una predicción (en Inglés, 2.º medio)?", "Una idea de lo que voy a oír, antes de oírlo", "Se basa en el título y en lo que ya sabes."),
        ("¿Qué haces con una predicción después de escuchar?", "La confirmo o la corrijo", "Sirve para comprender mejor."),
        ("¿Qué significa escuchar con un propósito (en Inglés, 2.º medio)?", "Decidir qué busco antes de oír", "Así la atención se enfoca."),
    ],
    task("Una persona adulta lee dos veces: «Hello, students. This is the school radio. Today’s topic is volunteering. Our guest, Paula, helps at an animal shelter every Saturday. She feeds the dogs, cleans their beds and plays with them for an hour. She says that the best part is seeing a dog find a new home.» (volunteering = voluntariado, shelter = refugio, feeds = alimenta, beds = camas, find = encontrar, home = hogar). Antes de que lean, escribe en tu hoja una predicción de tres palabras. Después anota qué se confirmó y qué no, y responde: ¿cuántas horas juega con ellos?", "Predicciones posibles: dog, shelter, volunteer. Se confirman las que aparezcan en el guion (dog, shelter). Juega una hora con los perros.", ["escribe tres palabras antes de escuchar", "dice cuáles se confirmaron con el guion", "responde la pregunta con el dato correcto"], ["hoja con la predicción y la comparación", "nota de la persona que leyó"], ["escribir la predicción después de oír el guion", "inventar un dato que no está en el guion"], "Marca en tu hoja en verde las palabras que coincidieron y en rojo las que no aparecieron."),
    "Antes de escuchar un aviso, escribe tres palabras que esperas oír y revisa cuántas se confirmaron.",
    "Escribe un título imaginario para una charla y predice cinco palabras que aparecerían en ella.",
)

# ================================================== clase 2: frases clave, gestos y entonación
MURAL = "«[Points to the wall] Look at this mural. It shows our neighbourhood in the past. [Raises voice] And here, this is the most important part! Can you see the small blue door? [Smiles] That door belonged to the first library in the area. [Lowers voice] Please do not touch the paint.» (mural = mural, neighbourhood = barrio, door = puerta, belonged to = pertenecía a, area = zona, touch = tocar, paint = pintura)"
REPAIR = "«[Shows a bike wheel] Today I will show you how to fix a flat tyre. First, take off the wheel. [Mimes] Then pull out the old tube carefully. After that, put in the new tube. Finally, check the air. [Raises voice] Do not forget the last step: check the air twice!» (fix = reparar, flat tyre = neumático pinchado, tube = cámara, carefully = con cuidado, twice = dos veces, mimes = hace mímica)"
INTONE = "«[Rising voice] You are coming to the party tonight? Great. I thought you were busy. [Flat voice] Fine.» (party = fiesta, busy = ocupado)"

lesson(
    OA, 2, MAT,
    "Aprenderé a prestar atención a las expresiones o frases clave y a usar apoyos como los gestos y la entonación del hablante para entender mejor un texto oral. Sirve para seguir instrucciones y explicaciones aunque no entienda todo.",
    ["Sé hacer predicciones antes de escuchar.", "Sé identificar el tema de un texto."],
    [
        "Las frases clave (key phrases) son las que contienen la información más importante. Suelen aparecer después de expresiones que anuncian algo: the most important part is…, remember that…, first, then, finally, do not forget… Cuando las oyes, es una señal para escuchar con más atención y anotar la palabra principal.",
        "Los hablantes también usan apoyos para ayudarte. Los gestos (gestures) señalan, muestran o imitan lo que se dice: apuntar a un lugar, mostrar un objeto o hacer mímica. La entonación (intonation) es la subida y bajada de la voz. Una voz más fuerte o más alta marca lo importante, una voz baja avisa un secreto o una advertencia, y una voz que sube al final suele indicar una pregunta.",
        "Estas pistas no cambian el sentido de las palabras, pero lo apoyan. Si alguien dice Fine con voz plana después de una pregunta alegre, la entonación puede mostrar que no está tan contento. Por eso, cuando escuches, mira al hablante, fíjate en la voz y combina esas pistas con las palabras que sí entiendes.",
    ],
    [("key phrase", "frase clave: contiene la información más importante"), ("gesture", "gesto: movimiento para apoyar lo que se dice"), ("intonation", "entonación: subida y bajada de la voz"), ("do not forget", "no olvides"), ("most important", "lo más importante")],
    [
        ("Frase clave por señal", ADULT + "«Remember that the pool opens at seven. The most important rule is to shower before swimming.» (pool = piscina, rule = regla, shower = ducharse). ¿Cuál es la regla más importante?", ["La señal The most important rule anuncia la frase clave.", "Después dice to shower before swimming.", "Es la regla de ducharse."], "Ducharse antes de nadar"),
        ("Apoyo de la entonación", "Una persona dice «Are you ready?» con la voz subiendo al final. ¿Qué tipo de oración es? A) una pregunta B) una orden", ["La voz sube al final.", "Eso suele indicar una pregunta.", "Una orden suele bajar."], "A) una pregunta"),
    ],
    [
        ("Esperar a entender todas las palabras antes de decidir qué es importante.", "Se ignoran las señales de la voz y de los gestos.", "Busca frases como the most important y la voz más fuerte."),
        ("Pensar que la entonación sube al final en todas las oraciones.", "La subida es típica de preguntas, no de afirmaciones.", "Fíjate en la voz y en las palabras de pregunta."),
    ],
    [
        (ADULT + MURAL + " ¿De qué color es la puerta pequeña? A) azul B) roja", "A", "El guion dice the small blue door."),
        (ADULT + REPAIR + " ¿Qué se hace primero para arreglar el neumático? A) sacar la rueda B) revisar el aire", "A", "El guion dice First, take off the wheel."),
        (ADULT + INTONE + " ¿Cómo suena la última palabra, Fine? A) con voz plana B) con voz alegre", "A", "Lleva la anotación Flat voice."),
    ],
    [
        (ADULT + MURAL + " ¿A qué señal de la voz corresponde la parte más importante? A) la voz sube B) la voz baja", "A", "Antes de la frase clave el hablante levanta la voz."),
        (ADULT + REPAIR + " ¿Qué muestra el hablante con el gesto de la rueda? A) el objeto sobre el que va a explicar B) que se terminó la clase", "A", "Muestra la rueda de bicicleta antes de explicar."),
        (ADULT + MURAL + " ¿Qué pidió el hablante con voz baja? A) no tocar la pintura B) mirar la puerta", "A", "Dice Please do not touch the paint."),
    ],
    [
        (ADULT + REPAIR + " ¿Cuántas veces hay que revisar el aire? A) dos B) una", "A", "El guion dice check the air twice."),
        (ADULT + MURAL + " ¿A qué lugar perteneció la puerta azul? A) a la primera biblioteca de la zona B) a un museo", "A", "Dice That door belonged to the first library in the area."),
        (ADULT + INTONE + " ¿Qué muestra la voz que sube en la primera frase? A) que es una pregunta B) que es una orden", "A", "La anotación Rising voice muestra que You are coming to the party tonight? es una pregunta."),
    ],
    [
        (ADULT + REPAIR + " El hablante levanta la voz en Do not forget the last step. ¿Qué significa? A) que ese paso es importante B) que ya terminó", "A", "La voz fuerte marca lo importante."),
        (ADULT + INTONE + " La persona dice Fine con voz plana. ¿Qué podría sentir? A) que no está muy contenta B) que está muy feliz", "A", "La voz plana, después de una frase alegre, sugiere poco entusiasmo."),
    ],
    [
        (ADULT + MURAL + " Ordena lo que el hablante muestra: a) la puerta azul b) el mural completo c) la advertencia sobre la pintura", "b, a, c", "Primero habla del mural, luego señala la puerta y al final pide no tocar la pintura."),
        (ADULT + REPAIR + " ¿Qué tres pasos se nombran con una palabra de orden? A) first, then, finally B) always, never, maybe", "A", "El guion usa First, Then y Finally para ordenar."),
    ],
    [(ADULT + "«[Points to a poster] This is our timetable. The workshop is on Friday, not on Thursday. [Raises voice] Not Thursday, Friday! Please write it down.» (timetable = horario, workshop = taller, write down = anotar). ¿Qué día es el taller?", "El viernes", "El hablante lo repite con voz fuerte: Not Thursday, Friday.")],
    [
        ("¿Para qué sirven los gestos del hablante?", "Para apoyar lo que dice", "Muestran o señalan lo que se explica."),
        ("¿Qué indica una voz más fuerte en una frase?", "Que es importante", "Marca lo que debo recordar."),
        ("¿Qué indica una voz que sube al final?", "Una pregunta", "Es una pista de la entonación."),
    ],
    task("Una persona adulta lee dos veces y hace los gestos: «[Holds a card] Today I will show you how to make a school badge. First, draw a circle on paper. [Mimes drawing] Then write your name inside. [Raises voice] The most important thing is to write it big. Finally, ask a teacher to approve it.» (badge = insignia, circle = círculo, inside = adentro, big = grande, approve = aprobar). En tu hoja escribe: los pasos con first, then y finally, la frase clave y un gesto que ayudó.", "Pasos: dibujar un círculo; escribir el nombre adentro; pedirle a un profesor que lo apruebe. Frase clave: escribirlo grande. Gesto: mostrar la tarjeta o hacer mímica de dibujar.", ["ordena los tres pasos", "dice la frase clave", "nombra un gesto"], ["hoja con tres secciones", "nota de la persona que leyó"], ["cambiar el orden de los pasos", "escribir un gesto que no se hizo"], "Pide a la persona que repita la frase clave con la voz fuerte y comprueba que coincide con la que escribiste."),
    "Mira un video corto sin sonido de alguien que explica un procedimiento y anota qué gestos entiendes.",
    "Practica leer una pregunta y una afirmación con entonación distinta y pide a alguien que adivine cuál es cuál.",
)

# ================================================== clase 3: preguntar para confirmar, pedir repetición
LOST = "«Visitor: Excuse me, could you tell me how to get to the bus station? Guard: Of course. Go straight along this street, turn left at the bank, and the station is on your right. Visitor: Sorry, could you say that again, please? Guard: Sure. Straight, left at the bank, station on the right. Visitor: So, I turn left at the bank. Guard: That’s right.» (guard = guardia, straight = derecho, turn left = doblar a la izquierda, bank = banco, right = derecha, say again = repetir)"
TIMES = "«Coach: Training is on Monday at seven. Player: Seven in the morning? Coach: No, in the evening. Seven p.m. Player: Do you mean seven o’clock in the evening? Coach: Yes, exactly.» (training = entrenamiento, evening = última parte de la tarde, mean = querer decir)"
PLAN = "«Teacher: The group project is due on the fifth. Student: Sorry, did you say the fifth or the fifteenth? Teacher: The fifth. Student: Could you speak more slowly? I did not understand the last part. Teacher: Of course. The project needs a poster and a short talk.» (due = para entregar, slowly = despacio, understand = entender)"

lesson(
    OA, 3, MAT,
    "Aprenderé a preguntar para confirmar que entendí, a confirmar mis predicciones y a pedir repetición o aclaración durante una conversación. Sirve para no quedarme con dudas cuando alguien me da una dirección, una hora o una instrucción.",
    ["Sé hacer predicciones y escuchar con un propósito.", "Sé decir please y excuse me."],
    [
        "En una conversación no hace falta entender todo a la primera. Puedes pedir repetición (ask for repetition): Could you say that again, please? o Sorry, I did not catch that. Puedes pedir que hablen más despacio: Could you speak more slowly? Y puedes pedir una aclaración (clarification): What do you mean? o Do you mean…? Estas frases muestran interés y no son una falta de respeto.",
        "Para confirmar (confirm) que entendiste, repite con tus palabras lo que oíste y agrega una pregunta: So, I turn left at the bank? o Seven in the morning? La otra persona dice Yes, that’s right o No, in the evening. Cuando confirmas, también compruebas tu predicción: si pensabas que el entrenamiento era en la mañana y te corrigen, ya sabes qué ajustar.",
        "Un buen orden es: escucha, repite el dato clave, pregunta si es correcto y anota. Si dos datos suenan parecidos, como fifth y fifteenth o thirteen y thirty, pide que lo confirmen. Es preferible preguntar una vez más que llegar a un lugar equivocado. Usa siempre un tono amable: Sorry, could you…? o Excuse me, do you mean…?",
    ],
    [("Could you say that again?", "¿Podría repetir eso?"), ("Could you speak more slowly?", "¿Podría hablar más despacio?"), ("Do you mean…?", "¿Quiere decir…?"), ("So…?", "Entonces…? (para confirmar)"), ("I did not catch that", "No alcancé a oírlo"), ("That’s right", "Eso es correcto")],
    [
        ("Pedir repetición", "No entendiste la hora que dijo tu entrenador. ¿Cuál es una frase amable para pedir repetición? A) Could you say that again, please? B) That’s right.", ["Necesito que repita.", "Could you say that again es una petición amable.", "That’s right sirve para confirmar."], "A"),
        ("Confirmar un dato", "Una persona dice: «The meeting is at four thirty.» Para confirmar, ¿qué dices? A) So, it is at four thirty? B) Could you speak more slowly?", ["Quiero comprobar la hora.", "Repito el dato y pregunto.", "So… sirve para confirmar."], "A"),
    ],
    [
        ("Quedarse callado cuando no se entiende un dato importante.", "Se corre el riesgo de ir al lugar o a la hora equivocados.", "Usa Could you say that again? o Do you mean…?"),
        ("Usar That’s right para pedir repetición.", "Esa frase confirma, no pide que repitan.", "Usa Sorry, could you say that again?"),
    ],
    [
        (ADULT + LOST + " ¿Qué lugar busca el visitante? A) la estación de buses B) el banco", "A", "El visitante pregunta cómo llegar al bus station."),
        (ADULT + TIMES + " ¿A qué hora es el entrenamiento? A) a las siete de la tarde (7 p.m.) B) a las siete de la mañana", "A", "El entrenador corrige: Seven p.m."),
        (ADULT + PLAN + " ¿Qué debe llevar el proyecto? A) un afiche y una charla corta B) un video", "A", "La profesora dice a poster and a short talk."),
    ],
    [
        (ADULT + LOST + " ¿Qué frase usa el visitante para pedir repetición? A) Could you say that again, please? B) That’s right.", "A", "Pide a la guardia que repita."),
        (ADULT + TIMES + " ¿Qué hace el jugador cuando dice Seven in the morning? A) confirma el dato con una pregunta B) rechaza el entrenamiento", "A", "Repite la hora y pregunta; el entrenador corrige."),
        (ADULT + PLAN + " ¿Qué pidió el estudiante para entender mejor? A) que hablaran más despacio B) que se cambiara la fecha", "A", "Dice Could you speak more slowly?"),
    ],
    [
        (ADULT + LOST + " ¿Dónde debe doblar el visitante? A) a la izquierda en el banco B) a la derecha en el banco", "A", "El guion dice turn left at the bank."),
        (ADULT + PLAN + " ¿Cuál es la fecha de entrega que confirma la profesora? A) el cinco B) el quince", "A", "Responde The fifth cuando el estudiante pregunta si es the fifth or the fifteenth."),
        (ADULT + TIMES + " Seven p.m. son las 19:00. ¿Qué pregunta confirma esta hora? A) Do you mean seven o’clock in the evening? B) Could you say that again?", "A", "Do you mean… confirma la hora que entendió."),
    ],
    [
        (ADULT + PLAN + " ¿Por qué es útil la pregunta fifth or fifteenth? A) porque las dos palabras suenan parecidas y cambian la fecha B) porque la profesora habla rápido", "A", "El estudiante confirma un dato que se puede confundir."),
        (ADULT + LOST + " La guardia repite solo lo importante: Straight, left at the bank, station on the right. ¿Por qué es útil? A) porque entrega los datos clave sin palabras extra B) porque cambia la ruta", "A", "Al repetir, se destacan los puntos clave."),
    ],
    [
        (ADULT + TIMES + " Ordena la conversación: a) el entrenador corrige la hora b) el jugador confirma con una pregunta c) el entrenador dice la hora inicial", "c, b, a", "Primero dice la hora, luego el jugador confirma y después lo corrigen."),
        (ADULT + PLAN + " El estudiante no entendió la última parte. ¿Qué datos quedan claros después? A) entregar el cinco, con afiche y charla B) entregar el quince, sin afiche", "A", "La profesora repite los datos clave."),
    ],
    [(ADULT + "«Friend: Let’s meet at the ice-cream shop on Pine Street. You: Sorry, did you say Pine Street or Fine Street? Friend: Pine. P-I-N-E. You: Thanks. And what time? Friend: Five thirty.» (ice-cream shop = heladería, street = calle). ¿Cómo se escribe el nombre de la calle y a qué hora quedaron?", "Pine Street; a las cinco y media", "El amigo deletrea P-I-N-E y dice five thirty.")],
    [
        ("¿Cómo se pide que repitan algo en inglés?", "Could you say that again, please?", "Es una frase amable."),
        ("¿Para qué sirve So, I turn left at the bank?", "Para confirmar lo que entendí", "Repite el dato y pregunta."),
        ("¿Cómo se pide que hablen más lento?", "Could you speak more slowly?", "Se usa en inglés para pedir ayuda al escuchar."),
    ],
    task("Una persona adulta lee: «Here is the schedule for the field trip. We leave at eight fifteen from the main gate. The bus number is eighteen. Bring lunch and a hat.» (schedule = programa, main gate = portón principal, hat = sombrero). Tú no entendiste la hora y el número del bus. En tu hoja escribe tres frases que dirías para pedir repetición y confirmar. Luego anota los datos correctos que confirmaste.", "Frases posibles: Could you say that again, please? Do you mean eight fifteen? So, the bus number is eighteen? Datos: salida a las 8:15 del portón principal; bus 18; llevar almuerzo, y un sombrero.", ["escribe tres frases correctas de petición o confirmación", "anota los datos correctos del guion", "usa un tono amable"], ["hoja con frases y datos", "nota de la persona que leyó"], ["usar solo That’s right", "anotar 80 en lugar de 18"], "Compara con el guion la hora y el número del bus; si cambiaste algo, vuelve a pedir repetición."),
    "Practica con una persona de tu casa: pídele que diga una dirección y confirma el dato clave.",
    "Escribe tres frases para pedir aclaración en una clase de inglés cuando no entiendes una palabra.",
)

# ================================================== clase 4: inferencias con claves de contexto y de voz
CALL = "«[Quick, worried voice] Mum, it’s me. I’m at the school gate, but nobody is here. The lights are off. I can hear my own steps. [Voice drops] Maybe I got the date wrong.» (worried = preocupado, gate = portón, lights = luces, steps = pasos, date = fecha, wrong = equivocado)"
SHOP = "«[Cheerful voice] Welcome! Today you can try all the sizes. [Whispers] Between us, the blue ones are almost sold out. [Normal voice] The cashier is on your right.» (cheerful = alegre, sizes = tallas, whispers = susurra, sold out = agotados, cashier = caja)"
BELL = "«[Loud voice] Attention, please! The fire drill will start in five minutes. [Calmer] Remember: do not run. Walk to the patio in a line and stay with your teacher.» (fire drill = simulacro, patio = patio, line = fila, stay = quedarse)"

lesson(
    OA, 4, MAT,
    "Aprenderé a hacer inferencias con claves de contexto (tema, participantes, apoyo visual) y claves de la voz (entonación y acento). Sirve para entender lo que no se dice directamente, como cómo se siente alguien o dónde ocurre una situación.",
    ["Sé usar gestos y entonación como apoyo.", "Sé confirmar mis predicciones."],
    [
        "Una inferencia (inference) es una idea que no se dice con palabras, pero que se entiende por las pistas. Para inferir, combina lo que sabes con lo que oyes. Las claves de contexto (context clues) son el tema de que se habla, quiénes son los participantes (participants) y lo que se ve (visual support), como un cartel, un mapa o un objeto.",
        "Las claves de la voz (phonological clues) también ayudan. Una voz rápida y baja puede mostrar preocupación. Una voz alegre muestra entusiasmo. Una voz que baja al final suele mostrar duda, tristeza o cierre. El acento en una palabra (stress) marca lo que el hablante quiere que notes: en I said BLUE, not red, el acento aclara el color.",
        "Para inferir, sigue tres pasos: 1) escribe lo que oyes literalmente; 2) añade la pista de contexto o de voz; 3) formula una idea con palabras como probably, maybe o seems. Por ejemplo, si alguien dice que está en el portón y que nadie está allí, con voz preocupada, puedes inferir que quizá se equivocó de día. No todas las inferencias son seguras: siempre busca una prueba en el texto.",
    ],
    [("inference", "inferencia: idea que se deduce de pistas"), ("context clues", "claves de contexto: tema, participantes, apoyo visual"), ("phonological clues", "claves de voz: entonación y acento"), ("probably", "probablemente"), ("maybe", "quizás"), ("seems", "parece")],
    [
        ("Inferir un sentimiento", ADULT + "«[Slow, sad voice] I did not pass the test. I studied a lot, but I made too many mistakes.» (pass = aprobar, mistakes = errores). ¿Cómo se siente la persona?", ["La voz es lenta y triste.", "El texto dice que estudió y no aprobó.", "Probablemente se siente triste o decepcionada."], "Triste o decepcionada"),
        ("Inferir un lugar", ADULT + "«Please show your ticket at the door. The film begins in five minutes, and the sound is very loud.» (ticket = entrada, begins = comienza, loud = fuerte). ¿Dónde ocurre?", ["Hay tickets, door y film.", "Los participantes esperan para ver una película.", "El lugar es un cine."], "En un cine"),
    ],
    [
        ("Inferir sin ninguna prueba del texto.", "Una idea sin pistas es una suposición.", "Busca una frase o una pista de voz que apoye tu idea."),
        ("Pensar que una voz baja siempre significa tristeza.", "Puede indicar secreto, duda o cansancio.", "Combina la voz con las palabras y el contexto."),
    ],
    [
        (ADULT + CALL + " ¿Dónde está la persona? A) en el portón del colegio B) en su casa", "A", "El guion dice I’m at the school gate."),
        (ADULT + SHOP + " ¿Dónde está la caja? A) a la derecha B) a la izquierda", "A", "El guion dice on your right."),
        (ADULT + BELL + " ¿Cuántos minutos faltan para el simulacro? A) cinco B) quince", "A", "El guion dice in five minutes."),
    ],
    [
        (ADULT + CALL + " ¿Qué siente la persona al hablar? A) preocupación B) alegría", "A", "La voz rápida y las luces apagadas muestran preocupación."),
        (ADULT + SHOP + " ¿Qué te dice con un susurro? A) que casi no quedan los de color azul B) que la caja está cerrada", "A", "Between us, the blue ones are almost sold out."),
        (ADULT + BELL + " ¿Por qué habla más calmado el hablante en Remember: do not run? A) para dar calma B) para hacer un chiste", "A", "El tono tranquilo busca dar seguridad en una situación de riesgo."),
    ],
    [
        (ADULT + CALL + " ¿Qué podría haber ocurrido? A) que la persona se equivocó de fecha B) que el colegio se mudó", "A", "El guion dice Maybe I got the date wrong."),
        (ADULT + BELL + " ¿Qué se espera que hagan los estudiantes? A) caminar en fila al patio con su profesor B) correr a la puerta", "A", "El guion indica walk to the patio in a line and stay with your teacher."),
        (ADULT + SHOP + " ¿Qué se puede inferir del lugar? A) que es una tienda de ropa o calzado B) que es un hospital", "A", "Hay tallas (sizes), una caja y artículos azules que se agotan."),
    ],
    [
        (ADULT + CALL + " ¿Qué dato apoya inferir que el edificio está vacío? A) nobody is here y the lights are off B) Mum, it’s me", "A", "Nobody is here y the lights are off describen el edificio vacío; Mum, it’s me solo dice quién llama."),
        (ADULT + SHOP + " Alguien infiere que la tienda no tiene tallas. ¿Qué dato lo contradice? A) You can try all the sizes B) The cashier is on your right", "A", "El hablante dice que se pueden probar todas las tallas."),
    ],
    [
        ("Una voz dice «I said BLUE, not red» con acento fuerte en BLUE. ¿Qué quiere aclarar? A) el color correcto es azul B) que el objeto es rojo", "A", "El acento marca la palabra que corrige un error."),
        (ADULT + BELL + " El hablante empieza con voz fuerte y luego habla más calmado. ¿Qué dos intenciones muestra? A) llamar la atención y luego dar tranquilidad B) bromear y despedirse", "A", "Primero avisa con fuerza y luego calma con instrucciones claras."),
    ],
    [(ADULT + "«[Hurried voice] I am so sorry! The bus was late, and now I have no time. Can you start without me? I will be there in fifteen minutes.» (hurried = apurado, start = empezar, without = sin). ¿Cuánto tiempo calcula que tardará en llegar?", "Quince minutos", "El hablante dice fifteen minutes; su voz apurada apoya que llegará tarde.")],
    [
        ("¿Qué es una inferencia (en Inglés, 2.º medio)?", "Una idea que se deduce de pistas", "No se dice directamente en el texto."),
        ("¿Qué son las claves de contexto?", "Tema, participantes y apoyo visual", "Ayudan a entender lo que no se dice."),
        ("¿Qué claves de la voz ayudan a inferir?", "La entonación y el acento", "Muestran emociones e importancia."),
    ],
    task("Una persona adulta lee dos veces con la voz que indica cada corchete: «[Sleepy voice] Hello? Yes, it’s me. [Yawns] Sorry, I was asleep. [Cheerful voice] But I’m awake now! What time is it? [Surprised] Eleven in the morning! I need to hurry, my class starts at noon.» (asleep = dormido, awake = despierto, hurry = apurarse, noon = mediodía). En tu hoja escribe: tres inferencias con una pista de voz o de contexto y la hora a la que empieza su clase.", "Inferencias posibles: se acaba de despertar (voz soñolienta); no le preocupa porque la voz es alegre; se apura porque tiene poco tiempo. Hora: al mediodía.", ["escribe tres inferencias razonables", "cada una tiene una pista", "dice la hora de la clase"], ["hoja con tres inferencias y una hora", "nota de la persona que leyó"], ["inferir algo sin ninguna pista", "decir que la clase es a las once"], "Pregunta a la persona que leyó qué sintió al hacer cada voz y compara con tus inferencias."),
    "Mira una escena de una película sin sonido y anota qué inferencias puedes hacer con las imágenes.",
    "Escribe una situación de cuatro líneas con indicaciones de voz entre corchetes para que otra persona infiera cómo se siente el personaje.",
)

# ================================================== clase 5: tomar notas y resumir
TALK = "«Good afternoon. Today I will explain how to run a good meeting. There are four tips. First, send the plan one day before, so everyone can read it. Second, start on time, even if somebody is late. Third, give each person two minutes to speak. Finally, write down the decisions and send them after the meeting.» (run a meeting = dirigir una reunión, tips = consejos, on time = a la hora, decisions = decisiones)"
PODCAST = "«Welcome to Teen Tech. This week we talk about a new rule for phones in class. The school will keep phones in a box during lessons, except when the teacher asks for them. Students can use them at the break. The director says that the rule will start in March and will be checked after two months.» (rule = norma, box = caja, lessons = clases, except = excepto, break = recreo, checked = revisada)"
TRAIN = "«Hello, travellers. The train to the north leaves from platform five at ten forty. Please note: the platform changed from three to five. Tickets can be bought at the machine or at window two. Students pay half price with their card.» (platform = andén, changed = cambió, machine = máquina, window = ventanilla, half price = mitad de precio)"

lesson(
    OA, 5, MAT,
    "Aprenderé a tomar notas de lo que escucho y a resumir algunas ideas relevantes con apoyo. Sirve para recordar una explicación, un aviso o una charla sin escribir todo.",
    ["Sé escuchar con un propósito.", "Sé reconocer palabras clave y conectores."],
    [
        "Tomar notas (note-taking) no es escribir todo lo que oyes. Es anotar solo las palabras clave en forma corta: números, nombres, lugares y verbos importantes. Puedes usar abreviaturas (min, pm, no.), flechas y listas numeradas. Si el hablante dice first, second, third, escribe 1, 2, 3 y una o dos palabras para cada punto.",
        "Un resumen (summary) es una versión corta que conserva las ideas relevantes. Para resumir, responde tres preguntas con tus notas: ¿de qué habla?, ¿qué dice de importante? y ¿qué datos son necesarios? Deja fuera los ejemplos y los datos secundarios. Un resumen en inglés puede empezar con The speaker explains… o The text says that…",
        "Antes de resumir, compara tus notas con lo que recuerdas. Si falta un número o un nombre, pide a quien habló que lo repita. Con apoyo (support), como una lista de preguntas o una tabla ya preparada, resumir es más fácil: completas casillas con palabras clave y después las unes en una oración. Revisa siempre que no hayas cambiado ningún dato.",
    ],
    [("note-taking", "tomar notas"), ("summary", "resumen: versión corta con lo importante"), ("key word", "palabra clave"), ("abbreviation", "abreviatura"), ("support", "apoyo: guía o tabla para ayudar")],
    [
        ("Tomar notas con números", ADULT + "«The film club has three rules. One, arrive on time. Two, turn off phones. Three, do not talk during the film.» (film = película, turn off = apagar). Escribe las tres reglas en notas cortas.", ["Uso 1, 2, 3.", "Anoto solo las palabras clave.", "1: on time, 2: phones off, 3: no talking."], "1. llegar a tiempo; 2. apagar celulares; 3. no hablar durante la película"),
        ("Resumir en una oración", ADULT + "«I train on Mondays and Thursdays. On Mondays I run, and on Thursdays I swim. I always train after school.» (train = entrenar, run = correr, swim = nadar). ¿Cuál es un buen resumen? A) The speaker trains twice a week, after school. B) The speaker likes swimming.", ["Un resumen incluye lo central.", "La opción A dice cuántas veces y cuándo.", "La B es un solo detalle."], "A"),
    ],
    [
        ("Escribir frases completas y perderse la siguiente idea.", "Se anota demasiado y se deja de escuchar.", "Anota solo palabras clave y números."),
        ("Resumir copiando un ejemplo del texto.", "Un ejemplo no representa la idea general.", "Escribe la idea que une los puntos principales."),
    ],
    [
        (ADULT + TALK + " ¿Cuántos consejos da el hablante? A) cuatro B) tres", "A", "El guion dice There are four tips."),
        (ADULT + PODCAST + " ¿Cuándo comenzará la norma? A) en marzo B) en abril", "A", "El guion dice will start in March."),
        (ADULT + TRAIN + " ¿Desde qué andén sale el tren? A) del cinco B) del tres", "A", "El guion dice platform five; el tres era el andén anterior."),
    ],
    [
        (ADULT + TALK + " ¿Qué nota resume el segundo consejo? A) empezar a la hora B) enviar el plan antes", "A", "Second, start on time."),
        (ADULT + PODCAST + " ¿Qué nota corta resume la norma? A) celulares en una caja durante las clases B) celulares prohibidos siempre", "A", "Los celulares se usan en el recreo y cuando la profesora los pide."),
        (ADULT + TRAIN + " ¿Cuál es la nota más completa? A) tren norte, 10:40, andén 5 B) tren, 10", "A", "Incluye destino, hora y andén."),
    ],
    [
        (ADULT + TALK + " ¿Cuántos minutos puede hablar cada persona? A) dos B) diez", "A", "El guion dice two minutes."),
        (ADULT + PODCAST + " ¿Cuántos meses pasarán hasta que se revise la norma? A) dos B) seis", "A", "Dice will be checked after two months."),
        arith(ADULT + TRAIN + " Un pasaje normal cuesta 12000 pesos y los estudiantes pagan la mitad. ¿Cuántos pesos paga un estudiante?", "12000//2", "Se divide el precio normal en dos."),
    ],
    [
        (ADULT + TALK + " ¿Cuál es el mejor resumen? A) The speaker explains four tips for a good meeting. B) The speaker likes long meetings.", "A", "Dice el tema y el número de consejos."),
        (ADULT + PODCAST + " Un compañero resumió que los celulares se prohíben todo el día. ¿Qué dato lo corrige? A) se pueden usar en el recreo B) la norma empieza en marzo", "A", "El guion dice Students can use them at the break."),
    ],
    [
        (ADULT + TRAIN + " Ordena las notas según el guion: a) comprar boletos b) cambio de andén c) hora de salida", "c, b, a", "Primero la hora y el andén, luego el cambio y después los boletos."),
        (ADULT + TALK + " ¿Qué se debe anotar después de la reunión? A) las decisiones B) los chistes", "A", "El guion dice write down the decisions."),
    ],
    [(ADULT + "«For the school trip we need three things: a permission note, a snack and a rain jacket. The bus leaves at seven forty-five.» (permission note = autorización, snack = colación, jacket = chaqueta). Anota los datos clave en una lista corta y responde: ¿a qué hora sale el bus?", "A las siete y cuarenta y cinco", "El guion dice seven forty-five.")],
    [
        ("¿Qué se anota al tomar notas?", "Solo palabras clave", "No hace falta escribir frases completas."),
        ("¿Qué contiene un buen resumen?", "Las ideas relevantes", "Deja fuera los detalles secundarios."),
        ("¿Cómo puede empezar un resumen en inglés?", "The speaker explains…", "Es una forma de resumir lo que se dijo."),
    ],
    task("Una persona adulta lee dos veces: «Good evening. This is the weekly sports report. The school basketball team won on Tuesday, 48 to 40. The girls’ team plays on Saturday at four. We need two volunteers to help with the scoreboard. If you want to help, talk to Mr. Núñez before Friday.» (scoreboard = marcador, volunteers = voluntarios). En tu hoja escribe: notas cortas con cinco datos y un resumen de una oración que empiece con The speaker explains.", "Notas: equipo ganó martes 48-40; mujeres juegan sábado 4 pm; 2 voluntarios; marcador; hablar con Mr. Núñez antes del viernes. Resumen: The speaker explains the sports results and asks for two volunteers.", ["anota cinco datos correctos", "el resumen conserva la idea general", "usa palabras clave"], ["hoja con notas y resumen", "nota de la persona que leyó"], ["anotar 40 a 48", "copiar el guion completo"], "Compara tus cifras con el guion: si una no coincide, pide que te lo lean otra vez."),
    "Mira o escucha una noticia breve y anota cinco palabras clave y un resumen de una línea.",
    "Escribe en tu cuaderno un símbolo o abreviatura para cinco palabras que se repiten mucho al tomar notas.",
)
