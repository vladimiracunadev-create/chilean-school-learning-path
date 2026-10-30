"""Student material for 3.º básico Inglés (propuesta), EN03 OA 01 (rimas, chants, canciones, cuentos y diálogos) y OA 02 (temas y funciones conocidas).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Cada palabra o estructura en inglés se explica en la clase antes de usarla, o lleva su pista en español.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1, OA2 = "EN03 OA 01", "EN03 OA 02"
ADULT = "Un adulto lee en voz alta (tapa el guion): "


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


# ================================================================ OA 01
lesson(
    OA1, 1,
    "Las rimas escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a encontrar los sonidos que se repiten al final de las líneas de una rima. Sirve para entender y seguir una rima en inglés aunque no conozca todas las palabras.",
    ["Sé que una rima une palabras con el mismo final, como cat y hat.", "Sé decir en inglés palabras como sun, run, tree y bee."],
    [
        "Una rima (rhyme) está formada por palabras que terminan con el mismo sonido. Day y play riman: las dos suenan «dei» al final. Lo que importa es el sonido, no cómo se escribe. Blue, two y shoe riman aunque se escriban distinto.",
        "En una rima hay sonidos que se repiten (repeated sounds). Escucha la última palabra de cada línea (line) y compárala con las otras. Night, light y kite terminan igual: suenan «nait», «lait» y «kait». Por eso riman.",
        "Ten cuidado con las palabras que se escriben parecido pero suenan distinto. Now suena «nau» y snow suena «snou», así que no riman. Di las palabras despacio y escucha solo el final antes de decidir.",
    ],
    [("rhyme", "rima: palabras con el mismo sonido final"), ("sound", "sonido"), ("line", "línea o verso de una rima"), ("repeat", "repetir"), ("day", "día"), ("play", "jugar")],
    [
        ("Encontrar la rima", ADULT + "«Play, play, play all day. Hip, hip, hooray!» (hooray = ¡hurra!). ¿Qué dos palabras riman con day?", ["Escucho el final de day: «dei».", "Play también termina en «dei».", "Hooray termina en «rei», que rima con day."], "play y hooray"),
        ("Palabras que se parecen pero no riman", "¿Riman now («nau») y go («gou»)?", ["Escucho el final de cada palabra.", "Now termina en «nau».", "Go termina en «gou», que es distinto."], "No riman"),
    ],
    [
        ("Pensar que riman solo las palabras que se escriben igual al final.", "Se mira la escritura y no el sonido.", "Escucha el sonido final: blue y shoe riman aunque se escriban distinto."),
        ("Pensar que now y snow riman porque terminan con las mismas letras.", "Las letras iguales pueden sonar distinto.", "Di las dos palabras: now suena «nau» y snow suena «snou»; no riman."),
    ],
    [
        (ADULT + "«Look at the sky. The kite is high.» (look at = mira, sky = cielo, kite = volantín, high = alto). ¿Qué dos palabras riman?", "sky y high", "Las dos terminan con el mismo sonido «ai»."),
        ("¿Riman day y play?", "Sí", "Las dos terminan con el sonido «dei»."),
        ("¿Riman night («nait») y nine («nain»)?", "No", "Sus sonidos finales son distintos: «ait» y «ain»."),
    ],
    [
        ("¿Qué parte de dos palabras escuchas para saber si riman?", "El sonido del final", "La rima está en los sonidos finales."),
        ("Blue y shoe se escriben muy distinto. ¿Riman?", "Sí, porque suenan igual al final", "Lo que importa es el sonido, no la escritura."),
        ("En una rima, ¿qué significa «repeated sound»?", "Un sonido que vuelve a aparecer en varias palabras", "Repeated significa repetido."),
    ],
    [
        (ADULT + "«Rain, rain, go away. I want to play.» (rain = lluvia, go away = vete, I want to = yo quiero). ¿Qué palabra rima con away: play, rain o want?", "play", "Away y play terminan con el sonido «ei»."),
        ("Elige la palabra que rima con light: night, lake o tree.", "night", "Light y night terminan con el sonido «ait»."),
        (ADULT + "«Sing, sing, ring, ring, a king!» (sing = cantar, ring = anillo, king = rey). ¿Cuántas palabras terminan en el sonido «-ing»?", "5", "Sing, sing, ring, ring y king: cinco palabras."),
    ],
    [
        ("Ana dice que now y snow riman porque se escriben casi igual. ¿Tiene razón?", "No; suenan «nau» y «snou», que son distintos", "Se comparan los sonidos finales, no las letras."),
        (ADULT + "«One, two, a big blue shoe. Three, four, an open door.» (open = abierta, door = puerta). En la segunda línea, ¿qué dos palabras riman?", "four y door", "Las dos terminan con el sonido «or»."),
    ],
    [
        (ADULT + "«Look at the sea, a bee and a tree. Come with me!» (look at = mira, sea = mar, come with me = ven conmigo). Sin contar bee, ¿cuántas palabras riman con bee?", "3", "Sea, tree y me suenan «i» al final."),
        ("Una palabra no rima con las otras tres: cake, lake, make, king. ¿Cuál es?", "king", "Cake, lake y make terminan en «eik»; king no."),
    ],
    [("En el recreo, un grupo dice: " + ADULT + "«We run in the sun. It is fun!» (we run = nosotros corremos, fun = diversión). Sin contar sun, ¿cuántas palabras riman con sun?", "2", "Run y fun terminan con el sonido «an».")],
    [
        ("¿Qué significa «rhyme»?", "Rima", "Es la palabra en inglés para palabras con el mismo sonido final."),
        ("¿Riman too y shoe?", "Sí", "Las dos suenan «u» al final."),
        (ADULT + "«Day, day, say, say, hooray!» ¿Cuántas veces oyes una palabra que rima con day?", "5", "Day, day, say, say y hooray riman."),
    ],
    task("Un adulto lee dos veces esta rima: «Sing, sing, ring, ring. Say hello to the king!» (say hello = di hola). Marca una palmada cada vez que oigas una palabra que termina en «-ing» y luego di en voz alta cuál de estas tres palabras rima con say: day, king o hello.", "Day rima con say.", ["marca las palabras con el sonido «-ing»", "dice una palabra que rima con say", "escucha el final y no el comienzo"], ["nota del adulto", "foto o video con permiso de la familia"], ["elegir king o hello, que no riman con say", "dar palmadas en palabras que no riman"], "Reconoce las palmadas correctas y repite con él, despacio, los finales «-ing» y «-ay»."),
    "Pide a un adulto que lea «night, light, kite» y haz una palmada en cada palabra. Después dibuja una luz y un volantín.",
    "Escribe una pareja de palabras que rimen con play (por ejemplo day) y haz una rima de dos líneas.",
)

lesson(
    OA1, 2,
    "Los chants escritos en cada ejercicio, que lee un adulto en voz alta; espacio libre para moverte con seguridad y lápiz.",
    "Aprenderé a seguir las acciones de un chant: qué hacer, cuántas veces y en qué orden. Sirve para participar en juegos y canciones en inglés mostrando que entiendo.",
    ["Sé que clap es aplaudir y stamp es pisar fuerte.", "Sé contar en inglés del uno al diez."],
    [
        "Un chant es un texto con ritmo que se dice en voz alta y se acompaña con movimientos. Escucha las palabras de acción: jump (saltar), hop (dar saltitos), spin around (girar sobre ti mismo), march (marchar), shake (sacudir) y stop (detenerse). También recuerda clap (aplaudir) y stamp (pisar fuerte).",
        "Después de la acción puede venir un número y la palabra times (veces). «Jump three times» significa «salta tres veces». Con then (luego) se unen dos acciones: «Clap, then stamp» significa «aplaude y luego pisa fuerte». El orden en que las oyes es el orden en que las haces.",
        "Para seguir un chant, escucha tres cosas: la acción, el número y el orden. Cuando oigas stop, te quedas quieto. Puedes mirar a otras personas, pero no copies sin escuchar: comprueba las palabras de acción antes de moverte.",
    ],
    [("jump", "saltar"), ("hop", "dar saltitos"), ("spin", "girar"), ("march", "marchar"), ("shake", "sacudir"), ("times", "veces"), ("then", "luego"), ("stop", "detenerse")],
    [
        ("Acción y número", ADULT + "«Jump three times!» ¿Qué haces y cuántas veces?", ["Oigo la acción: jump, saltar.", "Oigo three times: tres veces.", "Junto las dos pistas."], "Salto tres veces"),
        ("Dos acciones en orden", ADULT + "«Clap, then stamp. Stop!» ¿Qué haces primero y qué haces al final?", ["Primero oigo clap: aplaudir.", "Luego oigo stamp: pisar fuerte.", "Al final oigo stop: me detengo."], "Primero aplaudo, luego piso fuerte y al final me detengo"),
    ],
    [
        ("Hacer los movimientos aunque el chant diga otra acción, solo porque otros lo hacen.", "Se imita a otras personas sin escuchar la palabra de acción.", "Escucha la palabra de acción antes de moverte y comprueba con ella."),
        ("Ignorar la palabra times y hacer la acción una sola vez.", "No se escuchó el número.", "Escucha el número: «two times» son dos veces."),
    ],
    [
        (ADULT + "«Jump, jump, jump!» ¿Cuántas veces saltas?", "3", "Se dice jump tres veces."),
        (ADULT + "«Spin around!» (around = alrededor) ¿Qué haces?", "Giro", "Spin significa girar."),
        (ADULT + "«Stop!» ¿Qué haces?", "Me detengo y me quedo quieto", "Stop significa detenerse."),
    ],
    [
        (ADULT + "«Clap, then stamp.» ¿Qué haces primero?", "Aplaudo", "Clap aparece antes de then."),
        ("¿Qué significa «three times»?", "Tres veces", "Times es veces y three es tres."),
        ("¿Para qué sirve escuchar las palabras de acción de un chant?", "Para saber qué movimiento hacer y en qué orden", "Las palabras de acción dicen qué hacer."),
    ],
    [
        (ADULT + "«Hop two times. Then stop.» ¿Cuántos saltitos haces antes de detenerte?", "2", "Two times son dos veces."),
        (ADULT + "«Hands up! Hands down!» (hands = manos, up = arriba, down = abajo). ¿Qué haces en segundo lugar?", "Bajo las manos", "Hands down significa manos abajo y se oye segundo."),
        (ADULT + "«Shake your hands. Shake, shake, shake!» (your = tus) ¿Qué partes del cuerpo mueves?", "Las manos", "Hands significa manos."),
    ],
    [
        (ADULT + "«March, march, march. Stop!» ¿Cuántas veces marchas antes de parar?", "3", "March se dice tres veces antes de stop."),
        ("Luis giró tres veces cuando el chant decía «Hop three times». ¿Qué debió hacer?", "Dar tres saltitos", "Hop significa dar saltitos, no girar."),
    ],
    [
        arith(ADULT + "«Clap two times. Jump three times. Stop!» ¿Cuántos movimientos haces en total, contando palmadas y saltos, sin contar stop?", "2+3", "Se suman las palmadas y los saltos."),
        ("Un chant dice: «Clap two times. Jump three times. Stop.» Ordena estas tarjetas: 1) Stop 2) Jump three times 3) Clap two times. ¿En qué orden las haces?", "3, 2, 1", "Primero clap, luego jump y al final stop."),
    ],
    [(ADULT + "En el patio, una profesora dice: «Spin around. Then jump two times!» (around = alrededor) ¿Cuántos saltos haces después de girar?", "2", "Two times son dos veces.")],
    [
        ("¿Qué significa «shake»?", "Sacudir", "Es mover algo con movimientos rápidos."),
        (ADULT + "«Hop, hop, hop, hop. Stop!» ¿Cuántos saltitos haces?", "4", "Hop aparece cuatro veces."),
        ("¿Qué haces si dudas qué acción viene en el chant?", "Vuelvo a escuchar las palabras de acción", "No basta con copiar a otras personas."),
    ],
    task("Un adulto dice dos veces este chant: «Clap two times. Jump three times. Spin around. Stop!» Haz los movimientos en el orden que oyes, en un espacio libre y seguro. Cuando termines, di en inglés las tres acciones que hiciste: clap, jump y spin.", "Dos palmadas, tres saltos, un giro y quedarse quieto.", ["hace las acciones en orden", "respeta la cantidad de veces", "se detiene con stop"], ["nota del adulto", "foto o video con permiso de la familia"], ["cambiar el orden de las acciones", "no contar las veces"], "Aplaude el orden logrado y repite con él, despacio, la acción que le costó."),
    "Pide a un adulto que diga «jump, hop, spin» y haz cada acción una vez.",
    "Inventa un chant de tres líneas con las acciones march, clap y stop, por ejemplo «March three times. Clap two times. Stop!».",
)

lesson(
    OA1, 3,
    "Los cuentos y canciones cortas escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a ordenar lo que pasa en una canción o un cuento corto con las palabras first, next, then y last. Sirve para recordar y contar una historia en el orden correcto.",
    ["Sé que un cuento tiene un comienzo, una parte del medio y un final.", "Conozco las palabras water y sun."],
    [
        "Una historia o canción cuenta cosas en un orden. Las palabras first (primero), next (después), then (luego) y last (al final) te ayudan a seguir ese orden. Next y then dicen que algo viene después de lo anterior. Last dice que es lo último que pasa.",
        "En el cuento de hoy habla una persona que dice «I». Aprenderás cuatro acciones: I have (yo tengo), I put (yo pongo), I add (yo agrego) e I see (yo veo). También verás seed (semilla), pot (maceta), flower (flor), bread (pan), cheese (queso) y sandwich (sándwich).",
        "Para ordenar una historia, escucha las palabras de orden y piensa en lo que tiene sentido: una semilla va antes de una flor. Luego escribe 1, 2, 3, 4. Si dudas, vuelve a escuchar solo la palabra de orden que oíste.",
    ],
    [("first", "primero"), ("next", "después"), ("then", "luego"), ("last", "al final"), ("seed", "semilla"), ("pot", "maceta"), ("flower", "flor"), ("in the sun", "al sol"), ("I have / I put / I add / I see", "tengo / pongo / agrego / veo")],
    [
        ("La primera acción", ADULT + "«I have a seed. First, I put the seed in a pot. Next, I add water. Then I put the pot in the sun. Last, I see a flower!» ¿Qué hago primero?", ["Busco la palabra first.", "Después de first oigo: I put the seed in a pot.", "Eso es lo primero."], "Pongo la semilla en la maceta"),
        ("La última acción", "En el mismo cuento, ¿qué pasa al final?", ["Busco la palabra last.", "Después de last oigo: I see a flower.", "Eso ocurre al final."], "Veo una flor"),
    ],
    [
        ("Pensar que la flor pasa primero porque es lo más importante.", "Se ordena por importancia y no por las palabras de orden.", "Busca first y last: la flor viene después de last."),
        ("Ordenar solo por la palabra then y olvidar next.", "Se ignora una palabra de orden.", "Next y then dicen que algo viene después; usa ambas para ordenar."),
    ],
    [
        (ADULT + "«I have a seed. First, I put the seed in a pot. Next, I add water. Then I put the pot in the sun. Last, I see a flower!» Después de poner la semilla en la maceta, ¿qué hago?", "Agrego agua", "Next, que viene después de first, dice I add water."),
        ("¿Qué significa «next»?", "Después", "Next dice que algo viene a continuación."),
        ("¿Qué palabra dice que algo pasa al final: first, next o last?", "last", "Last significa al final."),
    ],
    [
        ("¿Para qué sirven first, next, then y last?", "Para decir en qué orden ocurre cada cosa", "Son palabras de orden de una historia."),
        ("¿Qué palabra va primero en una historia: first o last?", "first", "First significa primero."),
        ("En el cuento de la semilla, ¿qué significa «I see a flower»?", "Yo veo una flor", "I see es yo veo y flower es flor."),
    ],
    [
        ("Cuento: «I have a seed. First, I put the seed in a pot. Next, I add water. Then I put the pot in the sun. Last, I see a flower!» Ordena con 1, 2, 3, 4: A) Agrego agua. B) Veo una flor. C) Pongo la semilla en la maceta. D) Pongo la maceta al sol.", "C, A, D, B", "El orden es: maceta, agua, sol, flor."),
        (ADULT + "«First, I take the bread. Next, I add cheese. Then I close the sandwich. Last, I eat!» (take = tomo, add = agrego, close = cierro, eat = como). ¿Qué hago justo antes de cerrar el sándwich?", "Agrego queso", "Next dice que agrego queso, y then dice que cierro el sándwich."),
        (ADULT + "«First, I wake up. Next, I eat breakfast. Last, I go to school.» (wake up = me despierto, breakfast = desayuno, go to school = voy a la escuela). ¿Qué hago al final?", "Voy a la escuela", "Last dice que voy a la escuela."),
    ],
    [
        ("Pedro dice que la flor se ve primero. En el cuento de la semilla, ¿qué palabra de orden demuestra que no es así?", "last", "Dice «Last, I see a flower», o sea al final."),
        ("En el cuento del pan, ¿qué pasa después de agregar queso y antes de comer?", "Cierro el sándwich", "Primero agrego queso, luego cierro el sándwich y al final como."),
    ],
    [
        ("El cuento de la semilla tiene las palabras de orden first, next, then y last. ¿Cuántos pasos con palabra de orden tiene?", "4", "First, next, then y last son cuatro pasos."),
        ("Tarjetas del cuento del pan: A) Como. B) Agrego queso. C) Tomo el pan. D) Cierro el sándwich. Ordénalas según el cuento: «First, I take the bread. Next, I add cheese. Then I close the sandwich. Last, I eat!»", "C, B, D, A", "El cuento sigue ese orden: pan, queso, cerrar el sándwich, comer."),
    ],
    [(ADULT + "En la clase cantamos: «First I clap, next I jump, last I sit.» (sit = me siento). ¿Qué hago al final?", "Me siento", "Last dice que al final me siento.")],
    [
        ("¿Qué significa «first»?", "Primero", "First indica el comienzo del orden."),
        ("¿Qué significa «I add water»?", "Agrego agua", "I add es yo agrego y water es agua."),
        ("En un cuento, ¿qué te ayuda a saber el orden: las palabras de orden o el tamaño de las palabras?", "Las palabras de orden", "First, next, then y last indican el orden."),
    ],
    task("Un adulto lee dos veces este cuento: «First, I take the bread. Next, I add cheese. Then I close the sandwich. Last, I eat!» Dibuja cuatro cuadros numerados 1, 2, 3 y 4: uno para tomar el pan, otro para agregar queso, otro para cerrar el sándwich y otro para comer. Escribe debajo de cada uno la palabra de orden: first, next, then, last.", "1 first (tomar el pan), 2 next (agregar queso), 3 then (cerrar el sándwich), 4 last (comer).", ["dibuja los cuatro pasos en orden", "escribe first, next, then y last en el lugar correcto", "el último cuadro muestra la acción de comer"], ["dibujos del estudiante", "nota del adulto"], ["poner last antes de first", "no seguir el orden del cuento"], "Reconoce el orden correcto y vuelve a leer con él las palabras first y last."),
    "Pide a un adulto que lea «First, I put the seed in a pot. Last, I see a flower!» y muestra con las manos cuál va primero y cuál después.",
    "Inventa un cuento de tres líneas con first, next y last, por ejemplo sobre cómo te lavas las manos.",
)

lesson(
    OA1, 4,
    "Los diálogos escritos en cada ejercicio, que lee un adulto con dos voces distintas; lápiz y hoja para tapar el guion.",
    "Aprenderé a saber quién habla en un diálogo, qué dice cada persona y quién pregunta o responde. Sirve para entender conversaciones en inglés.",
    ["Sé saludar con hello.", "Sé que en una conversación hablan por turnos."],
    [
        "Un diálogo (dialogue) es una conversación entre dos o más personas. Cada persona que habla es un speaker. Para saber quién habla, mira el nombre antes de los dos puntos, por ejemplo «Ana:», o escucha el cambio de voz. Cada vez que cambia el speaker, comienza un turno nuevo.",
        "En los diálogos de hoy hay saludos y respuestas. How are you? significa «¿cómo estás?». I'm happy significa «estoy feliz» e I'm tired significa «estoy cansado o cansada». And you? significa «¿y tú?». Thank you es «gracias» y Yes es «sí».",
        "Una pregunta y su respuesta casi siempre las dicen speakers distintos. Para presentar a una persona se dice «This is my friend...», que significa «este es mi amigo» o «esta es mi amiga». También verás I have, que significa «yo tengo». Escucha y anota quién dice cada cosa.",
    ],
    [("dialogue", "conversación entre personas"), ("speaker", "persona que habla"), ("How are you?", "¿cómo estás?"), ("I'm happy / I'm tired", "estoy feliz / estoy cansado"), ("And you?", "¿y tú?"), ("This is my friend", "este es mi amigo / esta es mi amiga")],
    [
        ("Quién dice qué", ADULT + "«Ana: Hello, Ben! Ben: Hello, Ana! How are you? Ana: I'm happy. And you? Ben: I'm tired.» ¿Quién dice «I'm tired»?", ["Busco I'm tired.", "Antes de esa frase está el nombre Ben.", "Ben es el speaker."], "Ben"),
        ("Quién pregunta", "En el mismo diálogo, ¿quién pregunta «How are you?»", ["Busco How are you?", "Antes está el nombre Ben.", "Ben hace la pregunta y Ana responde."], "Ben"),
    ],
    [
        ("Pensar que quien responde también hizo la pregunta.", "Se confunden los turnos.", "Fíjate en el cambio de speaker: una persona pregunta y la otra responde."),
        ("Decir que hay un speaker porque la voz del adulto es una sola.", "Se cuenta al adulto y no a los personajes.", "Cuenta los nombres antes de los dos puntos: cada nombre es un speaker."),
    ],
    [
        (ADULT + "«Ana: Hello, Ben! Ben: Hello, Ana! How are you? Ana: I'm happy. And you? Ben: I'm tired.» ¿Cuántos speakers hay?", "2", "Hablan Ana y Ben."),
        (ADULT + "En el mismo diálogo, ¿quién dice «I'm happy»?", "Ana", "Ana responde que está feliz."),
        ("¿Qué significa «I'm tired»?", "Estoy cansado o cansada", "Tired significa cansado."),
    ],
    [
        ("En un diálogo, ¿qué es un speaker?", "La persona que habla en ese momento", "Speaker es la persona que dice cada turno."),
        ("¿Cómo puedes saber quién habla en un diálogo escrito?", "Por el nombre antes de los dos puntos", "El nombre indica quién dice cada línea."),
        ("¿Qué significa «And you?»", "¿Y tú?", "Se usa para preguntar lo mismo a la otra persona."),
    ],
    [
        (ADULT + "«Teacher: Open your book, please. Student: Yes, Miss. Teacher: Thank you.» (open your book = abre tu libro, please = por favor, Miss = señorita). ¿Quién dice «Thank you»?", "Teacher", "El turno de Teacher termina con Thank you."),
        (ADULT + "En el mismo diálogo, ¿quién dice «Yes, Miss»?", "Student", "Student responde a la profesora."),
        (ADULT + "«Leo: I have a red pencil. Sam: I have a blue pencil. Leo: Look! Two pencils!» (pencil = lápiz, look = mira). ¿Quién tiene el lápiz azul?", "Sam", "Sam dice «I have a blue pencil»."),
    ],
    [
        ("Un niño dice que Ana está cansada. Según el diálogo de Ana y Ben, ¿tiene razón?", "No, porque quien está cansado es Ben", "Ben dice «I'm tired» y Ana dice «I'm happy»."),
        (ADULT + "«Mia: Sam, this is my friend Leo. Leo: Hi, Sam! Sam: Hi, Leo!» (hi = hola). ¿Quién presenta a un amigo?", "Mia", "Mia dice «this is my friend Leo»."),
    ],
    [
        ("En el diálogo de Ana y Ben hay estos turnos: Ana, Ben, Ana, Ben. ¿Cuántos turnos hay en total?", "4", "Cada turno es una vez que habla un speaker; son cuatro."),
        (ADULT + "«Mia: Sam, this is my friend Leo. Leo: Hi, Sam! Sam: Hi, Leo!» ¿Cuántos speakers hay?", "3", "Hablan Mia, Leo y Sam."),
    ],
    [(ADULT + "En el recreo, dos niños conversan: «Ana: Hello, Ben! Ben: Hello, Ana! How are you? Ana: I'm happy. And you? Ben: I'm tired.» ¿Quién pregunta «And you?»", "Ana", "Ana devuelve la pregunta a Ben.")],
    [
        ("¿Cómo se dice «gracias» en inglés?", "Thank you", "Thank you es gracias."),
        ("¿Qué significa «dialogue»?", "Conversación entre personas", "Un diálogo tiene turnos de varios speakers."),
        (ADULT + "«Leo: I have a red pencil. Sam: I have a blue pencil.» ¿Quién tiene el lápiz rojo?", "Leo", "Leo dice «I have a red pencil»."),
    ],
    task("Un adulto lee con dos voces este diálogo: «Lia: Hello, Tom! Tom: Hello, Lia! How are you? Lia: I'm tired. And you? Tom: I'm happy.» Escucha dos veces y escribe en una hoja los dos nombres de los speakers. Debajo de cada uno, anota si dice I'm happy o I'm tired.", "Lia: I'm tired. Tom: I'm happy.", ["escribe Lia y Tom", "anota I'm tired bajo Lia", "anota I'm happy bajo Tom"], ["hoja con los nombres y las frases", "nota del adulto"], ["intercambiar quién está feliz y quién cansado", "escribir solo un speaker"], "Reconoce lo que ubicó bien y vuelve a escuchar solo el turno donde se equivocó."),
    "Pide a un adulto que diga «Hello, I'm tired» con voz cansada y «Hello, I'm happy» con voz alegre, y señala cuál es cuál.",
    "Escribe un diálogo de cuatro turnos entre tú y un amigo con Hello, How are you?, I'm happy y And you?.",
)

lesson(
    OA1, 5,
    "Cuatro textos cortos escritos en el enunciado (una rima, un chant, un cuento y un diálogo), que lee un adulto; lápiz y hoja para tapar el guion.",
    "Aprenderé a responder a un texto nuevo que escucho: reconozco qué tipo de texto es, busco las palabras clave y respondo con una acción, una elección o una palabra. Sirve para entender textos nuevos sin conocer todas las palabras.",
    ["Sé reconocer sonidos que se repiten en una rima.", "Sé seguir acciones de un chant, ordenar una historia y saber quién habla en un diálogo."],
    [
        "Cuando escuchas un texto nuevo, lo primero es saber qué tipo de texto es. Una rima tiene sonidos que se repiten al final de las líneas. Un chant tiene acciones y números. Una canción o un cuento tiene un orden con first, next, then y last. Un diálogo tiene speakers que se turnan.",
        "Después busca las palabras clave, que son las palabras que te dicen qué pasa: una acción, un número, un nombre o un objeto. No necesitas entender cada palabra. Hoy verás sleep tight (duerme bien, una despedida de la noche), bright (brillante), stars (estrellas), night (noche), cat (gato), big (grande), water (agua) y happy (feliz).",
        "Por último, responde de la forma que pide la tarea: con una acción, eligiendo una opción o diciendo una palabra. Siempre puedes mostrar qué parte del texto te dio la pista. Si dudas, vuelve a escuchar solo esa parte.",
    ],
    [("type of text", "tipo de texto"), ("key word", "palabra clave"), ("night", "noche"), ("bright", "brillante"), ("big", "grande"), ("happy", "feliz")],
    [
        ("Reconocer el tipo de texto", ADULT + "«Night, night, sleep tight. Stars are shining bright.» (sleep tight = duerme bien, stars = estrellas, shining = brillando). ¿Es una rima o un diálogo?", ["Escucho las palabras del final de las líneas.", "Tight y bright suenan «ait».", "Los sonidos finales se repiten."], "Una rima"),
        ("Palabras clave de un cuento", ADULT + "«Lola has a cat. The cat is big. Lola gives water to the cat. The cat is happy.» (has = tiene, gives = da). ¿Qué le da Lola al gato?", ["Busco gives.", "Después de gives oigo: water to the cat.", "Lola da agua al gato."], "Agua"),
    ],
    [
        ("Intentar traducir cada palabra antes de responder.", "Se pierde el hilo del texto.", "Busca las palabras clave y responde con lo que entendiste."),
        ("Responder sin mostrar qué parte del texto te dio la pista.", "No se vuelve a la evidencia.", "Señala la palabra clave que apoya tu respuesta."),
    ],
    [
        (ADULT + "«Night, night, sleep tight. Stars are shining bright.» ¿Qué dos palabras riman con night?", "tight y bright", "Las tres palabras terminan con el sonido «ait»."),
        (ADULT + "«Walk, walk, walk. Run, run, run. Stop! Now sit.» (walk = caminar, run = correr, now = ahora, sit = sentarse). ¿Es una rima, un chant o un diálogo? Piensa en las acciones.", "Un chant", "Tiene acciones y repeticiones para mover el cuerpo."),
        (ADULT + "«Lola has a cat. The cat is big. Lola gives water to the cat. The cat is happy.» ¿Cómo está el gato al final?", "Feliz", "Happy significa feliz."),
    ],
    [
        ("¿Qué debes hacer primero al escuchar un texto nuevo?", "Reconocer qué tipo de texto es", "Así sabes qué pistas buscar."),
        ("¿Qué es una palabra clave?", "Una palabra que dice qué pasa en el texto", "Puede ser una acción, un número, un nombre o un objeto."),
        ("¿Tienes que entender cada palabra para responder?", "No, basta con las palabras clave", "Las palabras clave dan la información importante."),
    ],
    [
        (ADULT + "«Walk, walk, walk. Run, run, run. Stop! Now sit.» ¿Qué haces cuando oyes stop?", "Me detengo", "Stop significa detenerse."),
        (ADULT + "«Lola has a cat. The cat is big.» ¿Qué tiene Lola?", "Un gato", "Has a cat significa tiene un gato."),
        (ADULT + "«Sam: Hello! Lola: Hello, Sam! Sam: Look, a cat! Lola: Yes, it is my cat.» (look = mira, my = mi). ¿De quién es el gato?", "De Lola", "Lola dice «it is my cat»."),
    ],
    [
        (ADULT + "«Walk, walk, walk. Run, run, run. Stop! Now sit.» ¿Qué haces después de correr?", "Me detengo y luego me siento", "Después de run viene stop y luego sit."),
        ("Un niño dice que «Night, night, sleep tight» es un diálogo porque tiene dos palabras night. ¿Tiene razón?", "No; es una rima porque tight y bright suenan igual al final", "Un diálogo necesita speakers que se turnan, y aquí no los hay."),
    ],
    [
        (ADULT + "«Walk, walk, walk. Run, run, run. Stop! Now sit.» ¿Cuántas acciones diferentes oyes sin contar stop?", "3", "Walk, run y sit son tres acciones diferentes."),
        ("Texto: «Lola has a cat. The cat is big. Lola gives water to the cat. The cat is happy.» Elige la frase que prueba que el gato está contento: a) The cat is big b) The cat is happy. ¿Cuál es?", "b", "Happy significa feliz y habla del estado del gato."),
    ],
    [(ADULT + "En clase, escuchas un texto nuevo: «Sam: Hello! Lola: Hello, Sam! Sam: Look, a cat! Lola: Yes, it is my cat.» ¿Es una rima, un chant o un diálogo?", "Un diálogo", "Hablan dos speakers por turnos.")],
    [
        ("¿Cómo se dice «noche» en inglés?", "night", "Night significa noche."),
        ("¿Qué significa «big»?", "Grande", "Big describe algo de gran tamaño."),
        ("¿Qué tipo de texto tiene sonidos que se repiten al final de las líneas?", "Una rima", "La rima repite los sonidos finales."),
    ],
    task("Un adulto lee dos veces este texto: «Walk, walk, walk. Run, run, run. Stop! Now sit.» Haz las acciones en el orden que oyes, en un espacio seguro. Luego di si es una rima, un chant o un diálogo y señala la palabra que te dio la pista (por ejemplo stop).", "Es un chant: la pista es que tiene acciones como walk, run y stop.", ["hace las acciones en orden", "nombra el tipo de texto", "señala una palabra clave como pista"], ["nota del adulto", "foto o video con permiso de la familia"], ["decir que es un diálogo", "no detenerse con stop"], "Muestra el orden logrado y vuelve con él sobre la palabra que le dio la pista."),
    "Pide a un adulto que lea «Night, night, sleep tight» y señala cuál palabra rima con night.",
    "Escribe una rima nueva de dos líneas que termine con sonido «ai», por ejemplo con sky y fly.",
)
