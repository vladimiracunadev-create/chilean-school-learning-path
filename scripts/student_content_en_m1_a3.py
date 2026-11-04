"""Cuaderno del estudiante, 1.º medio Inglés (propuesta), EN1M OA 03 (estrategias para escuchar: predecir, propósito, claves, gestos y entonación, pedir clarificación, resumir e inferir).

Las «escuchas» las lee un adulto en voz alta con el guion escrito en el enunciado; los gestos y los tonos van descritos entre corchetes.
Textos originales con pista en español.
"""
from __future__ import annotations

from student_content_en_m1_a import ADULT, MAT, lesson
from student_content_ma01_b import task
from student_lessons import arith

OA3 = "EN1M OA 03"

# ================================================================ OA 03 · clase 1: predecir y escuchar con un propósito
FISH = "«Good morning! Welcome to the fish market. Today the hake is fresh and costs six thousand pesos a kilo. The shrimp are cheaper: four thousand. Please ask for a bag if you need one. We close at two.» (hake = merluza, shrimp = camarones, cheaper = más baratos, bag = bolsa, close = cerramos)"
PARK = "«Good morning, hikers. Today's guided walk lasts three hours. Please stay on the path, carry water and do not feed the animals. The meeting point is the information center at nine.» (hikers = caminantes, guided walk = caminata guiada, path = sendero, feed = alimentar, meeting point = punto de encuentro)"
MENU = "«School radio. Tomorrow's lunch: lentils with rice, a green salad and an apple. The vegetarian option is pasta with tomato sauce.» (lunch = almuerzo, lentils = lentejas, vegetarian = vegetariano, sauce = salsa)"

lesson(
    OA3, 1, MAT,
    "Aprenderé a predecir lo que voy a oír y a escuchar con un propósito. Sirve para entender más rápido un aviso o una charla porque ya sé qué dato buscar.",
    ["Sé reconocer el tema por el título.", "Sé los números en inglés."],
    [
        "Predecir (to predict) es imaginar, antes de escuchar, qué palabras y datos aparecerán. Para hacerlo usas el título, el lugar donde estás y lo que ya sabes (conocimientos previos). Si el título es «A Morning at the Fish Market», es probable que oigas palabras como fresh, price y kilo. Una predicción es una hipótesis: puede confirmarse o corregirse.",
        "Escuchar con un propósito (listening with a purpose) es decidir antes qué necesitas saber: un precio, una hora, una regla. Ese propósito dirige tu atención. Si quieres comprar lo más barato, prestas atención a las cifras; si vas a una caminata, a las instrucciones. Así no te pierdes en los detalles que no necesitas.",
        "Después de escuchar, confirma tus predicciones: ¿acerté o debo corregir? Corregir una predicción no es un error, es parte de la estrategia. Anota solo lo que conecta con tu propósito, y haz un cálculo con los datos si el propósito lo requiere, por ejemplo cuánto pagas por dos productos.",
    ],
    [("predict", "predecir: imaginar lo que se va a oír"), ("purpose", "propósito: para qué escucho"), ("prior knowledge", "conocimientos previos"), ("confirm", "confirmar: comprobar si acerté"), ("cheaper", "más barato"), ("meeting point", "punto de encuentro")],
    [
        ("Predecir con el título", "Antes de escuchar, el título es «A Morning at the Fish Market». ¿Qué tres palabras crees que oirás? Elige las de la lista: fresh, referee, price, kilo, goal.", ["El título habla de un mercado de pescado.", "Un mercado lleva palabras de comprar y vender: fresh, price, kilo.", "Referee y goal son de deportes."], "Fresh, price y kilo"),
        ("Escuchar con un propósito", ADULT + FISH + " Tu propósito es comprar lo más barato. ¿Qué producto eliges?", ["Busco las cifras: merluza 6.000, camarones 4.000.", "El guion dice The shrimp are cheaper.", "El más barato es el camarón."], "Los camarones, a 4.000 pesos el kilo"),
    ],
    [
        ("Ignorar el propósito y anotar todo.", "Se intenta recordar cada palabra.", "Decide antes qué necesitas y anota solo eso."),
        ("Insistir en una predicción que no se confirma.", "Se piensa que corregir es un fracaso.", "Compara con el guion y cambia la hipótesis."),
    ],
    [
        ("El título es «The School Football Final». ¿Qué palabras es más probable que oigas? A) goal, referee, score B) fresh, price, kilo", "A) goal, referee, score", "Una final de fútbol se relaciona con goles, árbitro y marcador."),
        (ADULT + FISH + " ¿Cuánto cuesta el kilo de merluza?", "6.000 pesos", "El guion dice six thousand pesos a kilo."),
        (ADULT + PARK + " ¿Cuál es el punto de encuentro?", "El centro de información, a las nueve", "Dice the information center at nine."),
    ],
    [
        ("El título es «A Guided Walk in the Park» y quieres saber qué hacer en la caminata. ¿A qué parte escuchas con más atención? A) a las instrucciones con stay, carry y do not B) al saludo", "A) a las instrucciones con stay, carry y do not", "Tu propósito son las reglas, y están en esas frases."),
        (ADULT + FISH + " Predijiste que oirías precios. ¿Se confirma? A) sí, el guion dice six thousand y four thousand B) no, no hay precios", "A) sí, el guion dice six thousand y four thousand", "Hay dos precios en el guion."),
        (ADULT + PARK + " ¿Qué está prohibido hacer?", "Alimentar a los animales", "El guion dice do not feed the animals."),
    ],
    [
        arith(ADULT + FISH + " Compras dos kilos de merluza y un kilo de camarones. ¿Cuántos pesos pagas?", "2*6000+4000", "Se multiplican los dos kilos de merluza y se suman los camarones."),
        (ADULT + FISH + " ¿A qué hora cierra el mercado?", "A las dos", "El guion dice We close at two."),
        arith(ADULT + PARK + " La caminata empieza a las 9 y dura 3 horas. ¿A qué hora, en formato de 24 horas, termina?", "9+3", "Se suma la duración a la hora de inicio: termina a las 12, mediodía."),
    ],
    [
        (ADULT + PARK + " Ana quiere saber a qué hora llegar y Luis quiere saber qué llevar. ¿Qué datos anota cada uno? A) Ana: nine; Luis: water B) Ana: three hours; Luis: the path", "A) Ana: nine; Luis: water", "La hora de llegada es nine y lo que se lleva es water."),
        (ADULT + MENU + " Predijiste que habría un menú de pescado. ¿Qué haces? A) corrijo mi predicción porque el menú trae lentejas B) ignoro el guion", "A) corrijo mi predicción porque el menú trae lentejas", "Comparar con el guion permite corregir la hipótesis."),
    ],
    [
        (ADULT + PARK + " Un compañero predijo que pedirían un permiso especial para entrar. ¿Qué pasa con su predicción? A) no se confirma, el guion no menciona permiso B) se confirma", "A) no se confirma, el guion no menciona permiso", "Ninguna frase del guion habla de permisos."),
        (ADULT + FISH + " Tu propósito es llegar antes del cierre. ¿Qué dato necesitas? A) la hora de cierre: two B) el precio del camarón", "A) la hora de cierre: two", "El propósito marca el dato que importa."),
    ],
    [(ADULT + MENU + " Una estudiante vegetariana escucha el menú. ¿Qué opción le corresponde?", "Pasta con salsa de tomate", "El guion dice The vegetarian option is pasta with tomato sauce.")],
    [
        ("¿Qué es predecir antes de escuchar?", "Imaginar qué palabras o datos aparecerán", "Se usa el título y lo que ya sabes."),
        ("¿Qué haces si tu predicción no se confirma?", "La corrijo con lo que dice el guion", "Es parte de la estrategia."),
        ("¿Qué significa escuchar con un propósito?", "Decidir antes qué dato necesito", "El propósito dirige tu atención."),
    ],
    task("Un adulto lee dos veces este aviso: «Attention, cyclists. The bike tour starts on Saturday at eight from the main square. The tour is twelve kilometers long. Bring a helmet and water. If it rains, the tour moves to Sunday.» (cyclists = ciclistas, tour = paseo, long = de largo, helmet = casco, moves = se cambia). Antes de escuchar, escribe dos palabras que predices y tu propósito (por ejemplo, saber qué llevar). Luego anota el dato exacto de tu propósito y confirma si tus palabras aparecieron.", "Predicción: bike, helmet. Propósito: saber qué llevar. Dato: casco y agua. Se confirmaron bike y helmet.", ["escribe una predicción antes de escuchar", "anota un dato que responde al propósito", "confirma o corrige su predicción"], ["hoja con predicción, propósito y dato", "nota del adulto"], ["anotar todo sin propósito", "no confirmar la predicción"], "Valora la predicción y ayuda a la persona a revisar cuál dato respondió a su propósito."),
    "Pide a un adulto que lea otra vez el aviso del parque y escribe tu propósito antes de escuchar.",
    "Escribe en español tres palabras que predices para el título «A Day at the Beach» y, después, cuáles usarías si el título fuera «A Day at the Hospital».",
)

# ---------------------------------------------------------------- clase 2: conocimientos previos y frases clave
DRILL = "«Today we will practice the earthquake drill. Remember that you must not run outside during the shaking. The most important thing is to protect your head. First drop to the floor, then cover under a table, and hold on until it stops. After that, follow the teacher to the safe zone. Do not use the elevator.» (earthquake drill = simulacro de sismo, shaking = remezón, protect = proteger, head = cabeza, drop = agacharse, cover = cubrirse, hold on = afirmarse, safe zone = zona segura, elevator = ascensor)"
COACH = "«Remember, team: the match is on Saturday at four. The key is to pass the ball quickly. Don't forget your water bottle. And above all, have fun.» (match = partido, pass = pasar, key = la clave, bottle = botella, above all = sobre todo)"
EXAM = "«For the exam, my main advice is to sleep well. Also, practice with old tests. Do not study only the night before. In conclusion, start early and rest.» (exam = prueba, advice = consejo, old tests = pruebas antiguas, in conclusion = en conclusión)"

lesson(
    OA3, 2, MAT,
    "Aprenderé a usar lo que ya sé y las frases clave (the most important thing is…, remember that…, in conclusion…) para encontrar lo esencial. Sirve para entender instrucciones importantes aunque no entienda todas las palabras.",
    ["Sé predecir con el título.", "Sé las palabras first, then y after that."],
    [
        "Los conocimientos previos (prior knowledge) son lo que ya sabes de un tema. Si has participado en un simulacro de sismo en tu colegio, ya sabes que hay que protegerse la cabeza y no usar el ascensor. Ese saber te ayuda a entender el texto en inglés: reconoces palabras como drop, cover y hold on porque conoces la secuencia. Cuando conectas lo que oyes con lo que sabes, entiendes más rápido.",
        "Las frases clave (key phrases) avisan que viene algo importante: The most important thing is…, Remember that…, The key is…, My main advice is…, Above all…, In conclusion…. También las negaciones fuertes: Do not…, You must not…. Cuando las oyes, enfoca tu atención en lo que viene después. Esa es la información esencial del mensaje.",
        "Una buena estrategia es escuchar dos veces con tareas distintas. En la primera, buscas las frases clave y anotas lo que sigue. En la segunda, completas los detalles (a qué hora, dónde). Si no entiendes una palabra, usa tu conocimiento previo para adivinar su sentido por el contexto.",
    ],
    [("prior knowledge", "conocimientos previos"), ("key phrase", "frase clave: anuncia lo importante"), ("The most important thing is…", "Lo más importante es…"), ("Remember that…", "Recuerda que…"), ("above all", "sobre todo"), ("in conclusion", "en conclusión")],
    [
        ("Frase clave", ADULT + DRILL + " ¿Qué es lo más importante según el guion?", ["Busco la frase clave The most important thing is.", "Lo que sigue es to protect your head.", "Eso es lo esencial."], "Proteger la cabeza"),
        ("Conocimiento previo", ADULT + DRILL + " ¿Qué tres acciones, en orden, conforman el procedimiento?", ["Conozco el simulacro: agacharse, cubrirse y afirmarse.", "El guion dice First drop, then cover y hold on.", "Las tres acciones siguen ese orden."], "Agacharse (drop), cubrirse (cover) y afirmarse (hold on)"),
    ],
    [
        ("No escuchar lo que sigue a una frase clave.", "Se anota la frase y no el contenido.", "Después de The most important thing is…, escribe lo que viene."),
        ("Pensar que lo que ya sé no sirve en inglés.", "Se cree que el idioma separa los conocimientos.", "Conecta lo que ya sabes con las palabras que oyes."),
    ],
    [
        (ADULT + DRILL + " ¿Qué no se debe usar? A) el ascensor B) la escalera", "A) el ascensor", "El guion dice Do not use the elevator."),
        (ADULT + COACH + " ¿Qué día es el partido?", "El sábado a las cuatro", "Dice on Saturday at four."),
        (ADULT + EXAM + " ¿Qué consejo principal da? A) dormir bien B) estudiar toda la noche", "A) dormir bien", "My main advice es dormir bien."),
    ],
    [
        (ADULT + COACH + " ¿Cuál es la clave del juego según el entrenador? A) pasar la pelota rápido B) correr solo", "A) pasar la pelota rápido", "The key is to pass the ball quickly."),
        (ADULT + EXAM + " ¿Qué frase anuncia el cierre del mensaje? A) In conclusion B) Also", "A) In conclusion", "In conclusion se usa para cerrar."),
        (ADULT + DRILL + " ¿Adónde se va después de que el remezón se detiene?", "A la zona segura, siguiendo a la profesora", "El guion dice follow the teacher to the safe zone."),
    ],
    [
        (ADULT + COACH + " ¿Qué no debe olvidar cada jugador? A) una botella de agua B) un paraguas", "A) una botella de agua", "El guion dice Don't forget your water bottle."),
        (ADULT + EXAM + " ¿Qué recomienda hacer con las pruebas antiguas? A) practicar con ellas B) botarlas", "A) practicar con ellas", "Dice practice with old tests."),
        (ADULT + DRILL + " ¿Qué significa «Remember that you must not run outside»? A) hay que recordar no salir corriendo B) conviene correr hacia afuera", "A) hay que recordar no salir corriendo", "Remember that avisa algo importante y must not prohíbe."),
    ],
    [
        (ADULT + EXAM + " Un estudiante dice que el guion recomienda estudiar solo la noche anterior. ¿Qué frase lo corrige? A) Do not study only the night before B) Start early and rest", "A) Do not study only the night before", "La negación fuerte contradice su idea."),
        (ADULT + COACH + " ¿Qué frase clave muestra lo que el entrenador valora más? A) And above all, have fun B) Remember, team", "A) And above all, have fun", "Above all introduce lo más importante."),
    ],
    [
        ("Une cada frase clave con lo que anuncia. 1) Remember that… 2) In conclusion… 3) Do not… Anuncian: a) una prohibición b) una recomendación para recordar c) un cierre", "1-b, 2-c, 3-a", "Cada frase clave tiene una función."),
        (ADULT + DRILL + " Tu conocimiento previo dice que en un sismo se agacha, se cubre y se afirma. ¿Qué palabra del guion corresponde a «afirmarse»? A) hold on B) follow", "A) hold on", "Hold on significa agarrarse, afirmarse."),
    ],
    [(ADULT + "«Attention, students. Remember that the library closes at four today. The most important thing is to return your books before then. Do not leave them on the tables.» (return = devolver, leave = dejar, tables = mesas). ¿Qué es lo más importante?", "Devolver los libros antes de las cuatro", "Aparece después de The most important thing is.")],
    [
        ("¿Qué anuncia la frase «The most important thing is…»?", "Lo esencial del mensaje", "Lo que sigue es lo más relevante."),
        ("¿Para qué sirve el conocimiento previo al escuchar?", "Para conectar lo que oigo con lo que ya sé", "Ayuda a entender más rápido."),
        ("¿Qué expresa «Do not…»?", "Una prohibición", "Marca algo que no se debe hacer."),
    ],
    task("Un adulto lee dos veces este aviso: «Welcome to the school lab. Remember that you must wear a lab coat. The most important thing is to wash your hands at the end. Do not eat or drink in the lab. In conclusion, work carefully and ask for help.» (lab coat = delantal, wash = lavar, eat or drink = comer o beber, carefully = con cuidado). En tu hoja escribe las tres frases clave que oíste, lo que anuncia cada una y qué conocimiento previo te ayudó.", "Remember that (usar delantal), The most important thing is (lavarse las manos al final), Do not (no comer ni beber), In conclusion (trabajar con cuidado y pedir ayuda). Conocimiento previo: normas de laboratorio del colegio.", ["nombra al menos tres frases clave", "escribe lo que viene después de cada una", "menciona un conocimiento previo propio"], ["hoja con frases clave y mensajes", "nota del adulto"], ["anotar la frase clave sin el mensaje", "no relacionar con lo que ya sabe"], "Reconoce las frases clave logradas y repasa lo que anuncia cada una."),
    "Pide a un adulto que lea otra vez el aviso del simulacro y subraya cada frase clave.",
    "Escribe en español tres cosas que ya sabes de las normas de tu laboratorio o de tu gimnasio y que te ayudarían a entender un aviso en inglés.",
)

# ---------------------------------------------------------------- clase 3: gestos, entonación y acentuación
GUIDE = "«Welcome to our school. [points to the left] The library is on the left. [points to the right] The gym is on the right. [holds up three fingers] And we have three computer rooms upstairs.» (points = señala, holds up = levanta, fingers = dedos, upstairs = arriba)"
COLOR = "«I did not ask for a RED notebook. [stresses the word RED] I asked for a BLUE one. [stresses the word BLUE]» (notebook = cuaderno, asked for = pedí, stresses = acentúa)"
MOOD = "«Pedro: [slow, flat voice] Yes, I finished the project. Ana: [excited, high voice] Really? That's great! Pedro: [sighs] But the printer is broken.» (flat = sin emoción, sighs = suspira, printer = impresora, broken = rota)"

lesson(
    OA3, 3, MAT,
    "Aprenderé a usar los gestos del hablante y la entonación (la melodía de la voz) y la acentuación (qué palabra suena más fuerte) para entender mejor. Sirve para saber si alguien pregunta, afirma, se emociona o corrige.",
    ["Sé que una pregunta cierra con signo de interrogación.", "Sé que la voz sube y baja al hablar."],
    [
        "Un hablante dice más que sus palabras. Los gestos (gestures) señalan: si apunta a la izquierda y dice on the left, la información es doble. Los dedos pueden mostrar números y la cara muestra emoción. En una escucha sin imagen, un adulto puede describir esos gestos entre corchetes y tú los usas como pistas.",
        "La entonación (intonation) es la subida y bajada de la voz. En inglés, una pregunta de sí o no suele terminar con la voz que sube («You are coming? ↗»), y una afirmación termina con la voz que baja. Un tono emocionado y agudo muestra alegría; una voz plana y lenta puede mostrar cansancio o tristeza. La entonación cambia el sentido de la misma frase.",
        "La acentuación (stress) es la palabra o la sílaba que suena más fuerte. En «I asked for a BLUE one», la palabra fuerte muestra que se corrige un color. Si oyes una palabra acentuada, pregúntate qué se compara o se corrige. También cada palabra larga tiene una sílaba fuerte: thirTEEN y THIRty.",
    ],
    [("gesture", "gesto: movimiento que apoya lo que se dice"), ("intonation", "entonación: subida y bajada de la voz"), ("stress", "acento: lo que suena más fuerte"), ("rising", "que sube"), ("falling", "que baja"), ("flat", "plano, sin emoción")],
    [
        ("Pista de un gesto", ADULT + GUIDE + " ¿Dónde está el gimnasio?", ["La profesora apunta a la derecha.", "Además dice The gym is on the right.", "Gesto y palabras coinciden."], "A la derecha"),
        ("Acento que corrige", ADULT + COLOR + " ¿Qué color de cuaderno quería?", ["Las palabras RED y BLUE son las acentuadas.", "La persona corrige: no pidió rojo.", "Pidió azul."], "Azul"),
    ],
    [
        ("Ignorar los gestos descritos entre corchetes.", "Se escucha solo la parte hablada.", "Lee o escucha los gestos: pueden entregar un dato."),
        ("Creer que una frase siempre significa lo mismo.", "No se atiende a la entonación.", "Fíjate si la voz sube (pregunta) o baja (afirmación)."),
    ],
    [
        (ADULT + GUIDE + " ¿Cuántas salas de computación hay arriba?", "Tres", "Levanta tres dedos y dice three computer rooms."),
        (ADULT + MOOD + " ¿Cómo habla Ana? A) emocionada, con voz alta B) cansada, con voz plana", "A) emocionada, con voz alta", "El adulto describe excited, high voice."),
        ("La voz sube al final de «You are coming to the party?». ¿Qué es? A) una pregunta B) una orden", "A) una pregunta", "La entonación ascendente señala una pregunta de sí o no."),
    ],
    [
        (ADULT + GUIDE + " ¿Dónde está la biblioteca? A) a la izquierda B) a la derecha", "A) a la izquierda", "Señala a la izquierda y lo dice."),
        (ADULT + MOOD + " ¿Cuál es el problema de Pedro? A) la impresora está rota B) no terminó el proyecto", "A) la impresora está rota", "Pedro suspira y dice But the printer is broken."),
        (ADULT + COLOR + " ¿Qué color rechaza la persona? A) el rojo B) el azul", "A) el rojo", "Dice I did not ask for a RED notebook y acentúa RED para rechazarlo."),
    ],
    [
        (ADULT + MOOD + " ¿Cómo suena Pedro al decir que terminó el proyecto? A) sin entusiasmo B) muy alegre", "A) sin entusiasmo", "Habla con voz plana y lenta."),
        ("Cuando oyes «thirTEEN» con la fuerza en teen, ¿qué número es? A) 13 B) 30", "A) 13", "Thirteen lleva la fuerza al final; thirty en la primera sílaba."),
        (ADULT + GUIDE + " ¿Qué gesto acompaña a «three computer rooms»? A) levanta tres dedos B) aplaude tres veces", "A) levanta tres dedos", "El gesto repite la cifra y confirma el dato."),
    ],
    [
        ("Une cada pista con su efecto. 1) voz que sube al final 2) palabra acentuada 3) voz plana y lenta Efectos: a) corrige o compara b) pregunta c) poco ánimo", "1-b, 2-a, 3-c", "Cada rasgo de la voz cambia el sentido."),
        (ADULT + "«Mother: You did your homework? [voice goes up] Son: [voice goes down] Yes, I did.» (homework = tarea). ¿Quién hace la pregunta? A) la madre B) el hijo", "A) la madre", "Su voz sube al final: es una pregunta."),
    ],
    [
        (ADULT + "«I did not say he took my pen. [stress on SAID]» (pen = lápiz, took = tomó). Con la fuerza en SAID, ¿qué idea se destaca? A) quizás lo insinuó, pero no lo dijo B) nadie tomó el lápiz", "A) quizás lo insinuó, pero no lo dijo", "El acento en said sugiere que pudo darlo a entender sin decirlo."),
        (ADULT + "«I did not say he took my pen. [stress on HE]». Con la fuerza en HE, ¿qué idea se destaca? A) otra persona lo tomó B) nadie dijo nada", "A) otra persona lo tomó", "El acento en he separa a esa persona de otra."),
    ],
    [(ADULT + "«Teacher: [claps twice] Okay, everyone. [raises her hand] Silence, please. [points to the clock] We have ten minutes left.» (claps = aplaude, raises = levanta, clock = reloj, left = que quedan). ¿Qué indica con el gesto del reloj?", "Que quedan diez minutos", "Señala el reloj y dice ten minutes left.")],
    [
        ("¿Qué muestra una voz que sube al final de una frase?", "Una pregunta", "Es la entonación de las preguntas de sí o no."),
        ("¿Qué indica una palabra acentuada en una corrección?", "Qué dato se corrige", "El acento destaca lo que cambia."),
        ("¿Por qué conviene atender a los gestos?", "Porque dan información extra", "A veces repiten o aclaran el dato."),
    ],
    task("Un adulto lee dos veces esta escena, leyendo los gestos y tonos con la voz: «Waiter: [smiles, holds up one finger] Good evening. A table for one? Girl: [voice goes up] A table for two, please. Waiter: [looks at the door] Is someone coming? Girl: [looks at her phone, speaks slowly] Yes, my brother. He is late.» (waiter = garzón, table = mesa, door = puerta, late = atrasado). En tu hoja escribe: qué número cree el garzón al inicio, cuántas personas son en realidad, y qué pistas de gesto o voz lo muestran.", "El garzón cree que es una persona (levanta un dedo); son dos personas porque llega su hermano. Pistas: el dedo levantado, la voz que sube en A table for two y el gesto de mirar el teléfono con voz lenta para mostrar la tardanza.", ["indica que el garzón supone una persona", "indica que son dos personas", "cita al menos dos pistas de gesto o voz"], ["hoja con tres respuestas", "nota del adulto"], ["confundir quién cree qué", "no citar ninguna pista de voz"], "Valora las pistas citadas y relee con la persona los gestos entre corchetes."),
    "Pide a un adulto que lea de nuevo el diálogo de Pedro y Ana y copia las pistas de voz.",
    "Di en voz alta la frase «You are coming» de tres maneras (como pregunta, afirmación y sorpresa) y describe en español cómo cambia tu voz.",
)

# ---------------------------------------------------------------- clase 4: pedir repetición o clarificación
ROOM = "«Receptionist: The workshop is in room fifteen. You: Sorry, did you say fifteen or fifty? Receptionist: Fifteen, one-five. You: Thank you.» (receptionist = recepcionista, workshop = taller, did you say = ¿dijiste?)"
PAGE = "«Teacher: Open your books at page forty. Student: Could you repeat that, please? Teacher: Page forty, four-zero. Student: Oh, forty. Thanks.» (open = abrir, repeat = repetir, page = página)"
SPELL = "«Girl: My email is lucia dot vera at school dot cl. Boy: Sorry, could you speak more slowly? Girl: Of course. L-U-C-I-A dot V-E-R-A. Boy: So, you said Lucia dot Vera, right? Girl: Exactly.» (email = correo, dot = punto, slowly = más despacio, right = ¿cierto?)"

lesson(
    OA3, 4, "Los diálogos y tarjetas escritos en cada ejercicio; cada persona de la tarjeta sabe solo una parte del dato; lápiz y hoja.",
    "Aprenderé a pedir repetición o clarificación y a confirmar lo que entendí cuando una conversación no es clara. Sirve para no quedarse con una duda cuando alguien habla rápido o usa una palabra desconocida.",
    ["Sé saludar y dar las gracias en inglés.", "Sé los números en inglés."],
    [
        "En una conversación real nadie entiende todo a la primera. Los buenos oyentes usan frases para pedir ayuda. Para pedir repetición: Sorry, could you repeat that, please? Para pedir que hable más lento: Could you speak more slowly? Para preguntar el significado: What does … mean? Para confirmar un dato: Did you say fifteen or fifty? Para verificar que entendiste: So, you said …, right?",
        "Hay un orden útil: primero reconoces qué parte no entendiste (un número, una palabra, todo el mensaje), luego eliges la frase adecuada y después repites el dato para confirmar. Si no entendiste un número, no pidas que repita todo: pregunta por ese número. Si no entendiste una palabra, pide el significado o que la deletreen: Can you spell that?",
        "En una situación de vacío de información, cada persona tiene un dato que la otra no tiene. Para completar el dato hay que preguntar, escuchar y confirmar. Estas frases no son un signo de que no sabes inglés: son una estrategia que usan también quienes lo hablan como lengua materna.",
    ],
    [("Could you repeat that?", "¿Podrías repetir eso?"), ("Could you speak more slowly?", "¿Podrías hablar más despacio?"), ("What does … mean?", "¿Qué significa …?"), ("Did you say … or …?", "¿Dijiste … o …?"), ("So, you said …, right?", "Entonces, dijiste …, ¿cierto?"), ("spell", "deletrear")],
    [
        ("Pedir repetición", ADULT + PAGE + " ¿Qué frase usa la estudiante para pedir repetición?", ["Busco la frase que pide que repitan.", "La estudiante dice Could you repeat that, please?", "La profesora repite el dato."], "Could you repeat that, please?"),
        ("Confirmar un número", ADULT + ROOM + " ¿Cuál es el número de la sala?", ["La persona duda entre fifteen y fifty.", "La recepcionista confirma Fifteen, one-five.", "El número es 15."], "15"),
    ],
    [
        ("Quedarse callado y adivinar.", "Se siente vergüenza de preguntar.", "Usa una frase de clarificación: es una estrategia normal."),
        ("Pedir que repitan todo cuando solo falta un número.", "No se identifica qué parte no se entendió.", "Pregunta solo por la parte que no oíste: Did you say fifteen or fifty?"),
    ],
    [
        ("Quieres que alguien hable más lento. ¿Qué frase eliges? A) Could you speak more slowly? B) What does slow mean?", "A) Could you speak more slowly?", "La primera pide que baje la velocidad."),
        (ADULT + PAGE + " ¿En qué página abren los libros?", "En la 40", "La profesora repite Page forty, four-zero."),
        (ADULT + SPELL + " ¿Qué pide el chico cuando no entiende el correo? A) que hable más despacio B) que le preste el teléfono", "A) que hable más despacio", "Dice Could you speak more slowly?"),
    ],
    [
        ("Escuchaste «thirty» o «thirteen» y no estás seguro. ¿Qué dices? A) Did you say thirty or thirteen? B) What is your name?", "A) Did you say thirty or thirteen?", "La frase identifica el número dudoso."),
        (ADULT + SPELL + " ¿Qué hace el chico al final para verificar lo que entendió? A) dice So, you said Lucia dot Vera, right? B) pide el número de teléfono", "A) dice So, you said Lucia dot Vera, right?", "Repite el dato con right? para confirmarlo."),
        ("Une cada situación con su frase. 1) no entendiste una palabra 2) quieres confirmar lo que entendiste 3) necesitas que repitan Frases: a) What does that mean? b) So, you said…, right? c) Sorry, could you repeat that?", "1-a, 2-b, 3-c", "Cada frase corresponde a una necesidad."),
    ],
    [
        (ADULT + SPELL + " ¿Cómo se deletrea el nombre Lucía en el guion? A) L-U-C-I-A B) L-U-S-I-A", "A) L-U-C-I-A", "La chica deletrea L-U-C-I-A dot V-E-R-A."),
        (ADULT + ROOM + " ¿Cuál es la sala del taller? A) la quince B) la cincuenta", "A) la quince", "La recepcionista confirma Fifteen, one-five."),
        ("Quieres saber el significado de la palabra «form». ¿Qué dices? A) What does form mean? B) Could you repeat the page?", "A) What does form mean?", "La primera pide un significado."),
    ],
    [
        (ADULT + ROOM + " ¿Por qué pregunta fifteen or fifty? A) porque los dos números suenan parecidos B) porque no conoce la sala", "A) porque los dos números suenan parecidos", "Quince y cincuenta se confunden por su sonido."),
        (ADULT + "«A: The concert is on Saturday at seven. B: Sorry, did you say Saturday or Sunday? A: Saturday. S-A-T.» (concert = concierto). ¿Qué día es el concierto?", "El sábado", "A confirma Saturday."),
    ],
    [
        ("Ordena el diálogo de ayuda con letras. A) Sorry, could you repeat that? B) Page forty. C) The teacher says: open your books. D) Oh, forty. Thanks.", "C, A, B, D", "Primero la instrucción, luego se pide repetir, se repite y se agradece."),
        (ADULT + "«Ana: The meeting is at five. Leo: Sorry, where is it? Ana: I don't know the room. Leo: I know it: room seven. Ana: So, five o'clock in room seven, right? Leo: Exactly.» (meeting = reunión, room = sala). Ana sabe la hora y Leo sabe la sala. ¿Cuál es el acuerdo final?", "Reunión a las cinco en la sala siete", "Se unen los datos de ambas tarjetas."),
    ],
    [(ADULT + "«Mr. Pérez: Please send the form by Wednesday. Student: What does form mean? Mr. Pérez: A paper or a digital document to fill in. Student: Oh, formulario. Thank you.» (send = enviar, fill in = llenar). ¿Qué pidió aclarar el estudiante?", "El significado de form", "Pregunta What does form mean?")],
    [
        ("¿Qué frase sirve para pedir que repitan?", "Could you repeat that, please?", "Pide una repetición educada."),
        ("¿Qué frase confirma lo que entendiste?", "So, you said …, right?", "Repites el dato y verificas."),
        ("¿Qué pregunta sirve cuando no entiendes una palabra?", "What does … mean?", "Pide el significado."),
    ],
    task("Un adulto lee dos veces este diálogo, haciendo que habla rápido: «Clerk: The train leaves at six thirty from platform nineteen. You: Sorry, did you say nineteen or ninety? Clerk: Nineteen, one-nine. You: And the time? Could you repeat that, please? Clerk: Six thirty. You: So, six thirty from platform nineteen, right? Clerk: Exactly.» (clerk = empleado, platform = andén, leaves = sale). En tu hoja escribe las tres frases de clarificación que se usaron y el dato final confirmado.", "Frases: Did you say nineteen or ninety?; Could you repeat that, please?; So, six thirty from platform nineteen, right? Dato: el tren sale a las 6:30 del andén 19.", ["copia tres frases de clarificación", "indica el andén y la hora correctos", "explica para qué sirve cada frase"], ["hoja con frases y dato final", "nota del adulto"], ["confundir nineteen con ninety", "no copiar la frase de confirmación"], "Celebra las frases bien identificadas y repasa con la persona el orden: reconocer, preguntar y confirmar."),
    "Pide a un adulto que lea otra vez el diálogo de la sala quince y subraya la frase que confirma el número.",
    "Escribe en español una situación de tu semana en que habría que pedir repetir un dato y cuál frase en inglés usarías.",
)

# ---------------------------------------------------------------- clase 5: resumir e inferir con claves
TRIP = "«Manuel: [slow, low voice] I don't think I can go on the trip. Teacher: What's wrong? Manuel: My grandmother is in the hospital. Teacher: [softly] I'm sorry. Of course you can stay. Let me know if you need anything.» (trip = salida, hospital = hospital, softly = con voz suave, let me know = avísame)"
CENTER = "«This week at the community center: Monday, painting class at four. Wednesday, English club at five thirty. Friday, film night at seven; the film is a comedy. Entrance is free for all activities.» (painting = pintura, club = taller, film = película, comedy = comedia, entrance = entrada, free = gratis)"
SHOP = "«Customer: [frowns, looks at the shoes] These shoes are... interesting. Seller: [smiles] They are very comfortable. Customer: [puts them back on the shelf, voice goes down] How much are they? Seller: Forty thousand pesos. Customer: [shakes head] Maybe next time.» (frowns = frunce el ceño, shoes = zapatos, shelf = estante, shakes head = niega con la cabeza, maybe next time = quizás la próxima vez)"

lesson(
    OA3, 5, MAT,
    "Aprenderé a resumir las ideas relevantes de lo que escucho y a hacer inferencias con claves del contexto (tema, participantes, gestos) y de la voz (entonación y acentuación). Sirve para entender lo que alguien quiere decir sin decirlo.",
    ["Sé predecir, usar frases clave y pedir clarificación.", "Sé reconocer gestos y entonación."],
    [
        "Resumir (to summarize) es decir con pocas palabras las ideas más importantes, sin copiar frases ni agregar datos. Un buen resumen responde quién, qué, cuándo y dónde, y deja afuera los ejemplos. «Esta semana el centro comunitario ofrece pintura el lunes, inglés el miércoles y una película el viernes, todo gratis» resume el texto en una frase.",
        "Una inferencia (inference) es una conclusión que sacas de pistas porque el texto no la dice. Si Manuel habla con voz baja y lenta y su abuela está en el hospital, puedes inferir que está preocupado, aunque no use esa palabra. Las pistas del contexto son el tema, quiénes hablan y qué hacen; las pistas de la voz son la entonación, el ritmo y el acento.",
        "Para que tu inferencia sea válida debe apoyarse en al menos una pista del guion. «El cliente no quiere comprar» se apoya en el gesto de negar con la cabeza y en las palabras Maybe next time. Una inferencia sin pista es una suposición. Escribe siempre la pista que usaste.",
    ],
    [("summarize", "resumir: decir lo esencial en pocas palabras"), ("inference", "inferencia: conclusión basada en pistas"), ("clue", "pista"), ("context", "contexto: tema, personas y situación"), ("worried", "preocupado"), ("maybe next time", "quizás la próxima vez")],
    [
        ("Resumir", ADULT + CENTER + " Resume el aviso en una frase.", ["Identifico el tema: actividades de la semana.", "Anoto los días: lunes, miércoles y viernes.", "Agrego que la entrada es gratis."], "El centro comunitario ofrece pintura el lunes, inglés el miércoles y una película el viernes, y todo es gratis"),
        ("Inferir una emoción", ADULT + TRIP + " ¿Cómo se siente Manuel? Da una pista.", ["Habla con voz baja y lenta.", "Su abuela está en el hospital.", "Se infiere que está triste o preocupado."], "Está preocupado o triste: lo muestran su voz baja y que su abuela está en el hospital"),
    ],
    [
        ("Resumir copiando todas las frases.", "No se separa lo esencial de los detalles.", "Escribe una frase propia con quién, qué y cuándo."),
        ("Inferir sin citar una pista.", "La conclusión parece un hecho.", "Agrega la pista del guion que la apoya."),
    ],
    [
        (ADULT + CENTER + " ¿Qué día es la noche de cine? A) el viernes B) el lunes", "A) el viernes", "El guion dice Friday, film night at seven."),
        (ADULT + CENTER + " ¿Cuánto cuesta la entrada?", "Nada: es gratis", "Dice Entrance is free for all activities."),
        (ADULT + TRIP + " ¿Qué le dice la profesora a Manuel? A) que puede quedarse B) que debe ir", "A) que puede quedarse", "Dice Of course you can stay."),
    ],
    [
        (ADULT + SHOP + " ¿Qué se infiere del cliente? A) que no quiere comprar los zapatos B) que quiere comprar dos pares", "A) que no quiere comprar los zapatos", "Niega con la cabeza y dice Maybe next time."),
        (ADULT + TRIP + " ¿Qué pista de voz usa la profesora? A) habla suave B) grita", "A) habla suave", "El guion dice softly."),
        (ADULT + SHOP + " ¿Cuánto cuestan los zapatos?", "40.000 pesos", "El vendedor dice forty thousand pesos."),
    ],
    [
        (ADULT + SHOP + " ¿Qué pista muestra que el cliente no está convencido? A) frunce el ceño y baja la voz B) sonríe y compra", "A) frunce el ceño y baja la voz", "Esos gestos muestran duda."),
        (ADULT + TRIP + " ¿Cuál es el mejor resumen? A) Manuel no puede ir a la salida porque su abuela está en el hospital, y la profesora lo comprende B) Manuel no quiere ir porque le aburre", "A) Manuel no puede ir a la salida porque su abuela está en el hospital, y la profesora lo comprende", "Incluye quién, qué y por qué sin inventar."),
        (ADULT + CENTER + " ¿Cuántas actividades se nombran y en qué días? A) tres: lunes, miércoles y viernes B) dos: sábado y domingo", "A) tres: lunes, miércoles y viernes", "El guion nombra pintura, inglés y cine en esos días."),
    ],
    [
        (ADULT + SHOP + " Un compañero infiere que al cliente le encantaron los zapatos. ¿Qué pista lo corrige? A) los pone de vuelta en el estante y niega con la cabeza B) pregunta el precio", "A) los pone de vuelta en el estante y niega con la cabeza", "Esos gestos contradicen su idea."),
        (ADULT + "«Sofía: [fast, high voice] I got the scholarship! Dad: [hugs her, voice breaks] I am so proud of you.» (scholarship = beca, hugs = abraza, voice breaks = se le quiebra la voz, proud = orgulloso). ¿Qué infieres del padre? A) que está emocionado B) que está enojado", "A) que está emocionado", "Abraza a su hija y se le quiebra la voz de orgullo."),
    ],
    [
        (ADULT + CENTER + " ¿Qué propósito tiene el aviso? A) informar y atraer a la gente B) pedir dinero", "A) informar y atraer a la gente", "Resume actividades y dice que son gratis."),
        (ADULT + "«Girl: [looks at the sky, hugs her arms] It's cold. Boy: [takes off his jacket] Here, take mine.» (sky = cielo, hugs her arms = se abraza los brazos, takes off = se saca). ¿Qué hace el chico y por qué? A) le presta su chaqueta porque ella tiene frío B) se va porque tiene frío", "A) le presta su chaqueta porque ella tiene frío", "Las pistas son el gesto de ella y la frase Take mine."),
    ],
    [(ADULT + "«Man: [looks at his watch, speaks fast] The bus is late again. I will miss the interview. Woman: [calmly] Do not worry. There is another bus in ten minutes.» (watch = reloj de pulsera, miss = perder, interview = entrevista, calmly = con calma). ¿Cómo se siente el hombre?", "Nervioso o apurado", "Mira su reloj y habla rápido porque podría perder la entrevista.")],
    [
        ("En Inglés: ¿Qué es una inferencia?", "Una conclusión que se saca de pistas", "El texto no la dice directamente."),
        ("¿Qué debe tener siempre una inferencia?", "Una pista del guion que la apoye", "Si no, es una suposición."),
        ("¿Qué se omite al resumir?", "Los ejemplos y detalles menores", "Se deja lo esencial."),
    ],
    task("Un adulto lee dos veces esta escena: «Teacher: [looks at the clock, frowns] It is nine thirty. The test starts in five minutes. Boy: [runs in, breathing hard] Sorry! The bus broke down! Teacher: [softly] Sit down. Take a deep breath. You still have time.» (frowns = frunce el ceño, breathing hard = respirando agitado, broke down = se descompuso, deep breath = respiración profunda). En tu hoja escribe: un resumen de una frase, qué sentimiento infieres en el chico y qué pista usaste.", "Resumen: un estudiante llega atrasado a la prueba porque el bus se descompuso y la profesora lo tranquiliza. Inferencia: está nervioso o agitado; pista: corre y respira agitado.", ["resume en una frase con quién, qué y por qué", "infiere un sentimiento coherente", "cita una pista del guion"], ["hoja con resumen, inferencia y pista", "nota del adulto"], ["copiar el guion completo", "inferir sin pista"], "Valora la pista citada y ayuda a acortar el resumen a lo esencial."),
    "Pide a un adulto que lea otra vez la escena de la zapatería y escribe dos inferencias, cada una con su pista.",
    "Escribe en español dos pistas de voz o de gesto que usarías para mostrar que alguien está nervioso.",
)
