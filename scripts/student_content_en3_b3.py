"""Student material for 3.º básico Inglés, EN03 OA 12 (expresión oral con apoyo) y OA 13 (escritura con modelo).

Los personajes de las fichas son inventados. Las imágenes se describen entre corchetes porque el cuaderno no incluye ilustraciones.
Cada estructura se enseña en la propia clase antes de usarla. Las reglas de plural, -ing y a/an se limitan a casos seguros.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA12, OA13 = "EN03 OA 12", "EN03 OA 13"

NUM = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
       11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
       18: "eighteen", 19: "nineteen", 20: "twenty"}


def dots(n: int) -> str:
    return " ".join("●" * n)


def E(rows):
    return [ex(q, a, w) for q, a, w in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 12
lesson(
    OA12, 1,
    "Las fichas de personajes inventados escritas en esta clase, lápiz y una persona de tu casa para hacer el diálogo.",
    "Aprenderé a compartir información segura en inglés (nombre de pila, edad, país y gustos) usando personajes inventados. Sirve para presentarme y conocer a otras personas sin dar datos privados.",
    ["Sé decir hello.", "Sé contar hasta diez en español."],
    [
        "Para decir tu nombre usa «My name is Mia» (me llamo Mia). Para decir tu edad usa «I'm eight» (tengo ocho años). Para decir de dónde eres usa «I'm from Chile» (soy de Chile). Para decir lo que te gusta usa «I like pizza» (me gusta la pizza). Para decir tu color favorito usa «My favorite color is blue» (mi color favorito es el azul). En este cuaderno usamos «soccer» para el fútbol, que es la palabra de Estados Unidos; en Inglaterra y en otros países se dice «football». Los números del uno al diez son: one, two, three, four, five, six, seven, eight, nine, ten.",
        "Para preguntar a otra persona se usan cuatro preguntas: «What's your name?» (¿cómo te llamas?), «How old are you?» (¿cuántos años tienes?), «Where are you from?» (¿de dónde eres?) y «What do you like?» (¿qué te gusta?). Respondes con las frases que aprendiste. En inglés no se dice «I have eight years»; se dice «I'm eight».",
        "Hay datos privados que no se comparten con personas que no conoces: dirección, teléfono, nombre del colegio y claves. En esta clase usamos personajes inventados y solo datos seguros: nombre de pila, edad, país y gustos. Si alguien te pide un dato privado, puedes decir «No, thank you» (no, gracias) y avisar a una persona adulta.",
    ],
    [("My name is...", "me llamo..."), ("I'm...", "tengo... años"), ("I'm from...", "soy de..."), ("I like...", "me gusta..."), ("What's your name?", "¿cómo te llamas?"), ("How old are you?", "¿cuántos años tienes?")],
    [
        ("Presentar a Mia", "Ficha: Mia, 8 años, de Chile, le gusta la pizza. Tú eres Mia. ¿Qué dices en cuatro frases?", ["Uso My name is para el nombre.", "Uso I'm para la edad.", "Uso I'm from para el país y I like para el gusto."], "My name is Mia. I'm eight. I'm from Chile. I like pizza."),
        ("Responder una pregunta", "Ficha: Max, 9 años. Te preguntan «How old are you?» y eres Max. ¿Qué respondes?", ["Entiendo que preguntan la edad.", "Respondo con I'm.", "Digo nine."], "I'm nine."),
    ],
    [
        ("Decir «I have eight years».", "Se traduce palabra por palabra desde el español.", "En inglés se dice I'm eight."),
        ("Dar la dirección para presentarse.", "Se cree que hay que contar muchos datos.", "Usa nombre de pila, edad, país y gustos; guarda lo privado."),
    ],
    [
        ("¿Cómo se dice «Me llamo Ana» en inglés?", "My name is Ana", "My name is dice el nombre."),
        ("Completa: «I'm ___ Chile.» (soy de)", "from", "From indica el origen."),
        ("¿Qué significa «I like pizza»?", "Me gusta la pizza", "Like es gustar."),
    ],
    [
        ("¿Qué significa «How old are you?»", "¿Cuántos años tienes?", "Pregunta por la edad."),
        ("Ficha: Mia, 8 años, de Chile. Te preguntan «Where are you from?» y eres Mia. ¿Qué respondes?", "I'm from Chile", "Se usa I'm from y el país."),
        ("¿Qué datos son seguros para presentarte?", "Nombre de pila, edad, país y gustos", "No dicen dónde vives."),
    ],
    [
        ("Ficha: Max, 9 años. Completa: «I'm ___.» (el número en inglés)", "nine", "Nine es nueve."),
        ("Ficha: Max, le gusta el fútbol (soccer). Te preguntan «What do you like?» y eres Max. Escribe la respuesta de tres palabras.", "I like soccer", "Se usa I like y el gusto."),
        ("Ordena las palabras: from / I'm / Peru. Escribe la oración.", "I'm from Peru", "Primero va I'm y después from y el país."),
    ],
    [
        ("Ana dice «I have eight years». ¿Cómo se corrige para decir que tiene ocho años?", "I'm eight", "En inglés se usa I'm más el número."),
        ("Una persona que no conoces, en un juego en línea, te pide tu dirección. ¿Qué haces?", "No la doy y aviso a una persona adulta", "La dirección es un dato privado."),
    ],
    [
        ("Eres Mia y te preguntan «How old are you?». Escribe tu respuesta completa en inglés.", "I'm eight", "Mia tiene ocho años."),
        ("¿Qué pregunta haces para saber de qué país es una persona? Escribe la pregunta en inglés.", "Where are you from?", "Where are you from? pregunta el país."),
    ],
    [("Un compañero nuevo de la clase de inglés, personaje inventado, te pregunta «What's your name?». Eres Mia. Responde en inglés con una frase.", "My name is Mia", "Se usa My name is y tu nombre.")],
    [
        ("¿Cómo se dice «¿cuántos años tienes?» en inglés?", "How old are you?", "Es la pregunta por la edad."),
        ("¿Qué significa «What do you like?»", "¿Qué te gusta?", "Pregunta por los gustos."),
        ("¿Cómo se dice «Mi color favorito es el azul»?", "My favorite color is blue", "Favorite es favorito; el color es un dato seguro."),
    ],
    task("Con una persona de tu casa, jueguen a conocerse con personajes inventados. Ficha de Mia: 8 años, Chile, pizza. Ficha de Max: 9 años, Perú, fútbol (soccer). Uno hace de Mia y el otro de Max. Pregunten por turnos: «What's your name?», «How old are you?», «Where are you from?», «What do you like?» y respondan con las frases «My name is...», «I'm...», «I'm from...», «I like...».", "«What's your name?» «My name is Max.» «How old are you?» «I'm nine.» «Where are you from?» «I'm from Peru.» «What do you like?» «I like soccer.»", ["hace las cuatro preguntas", "responde con las cuatro frases", "usa solo los datos de la ficha", "no inventa datos privados"], ["nota de la persona que jugó con él o ella"], ["decir I have eight years", "dar dirección o teléfono"], "Valora que mantuvo los datos seguros y repite con él o ella la pregunta que le costó."),
    "Di en inglés tu nombre de pila y tu edad frente a un espejo.",
    "Inventa un personaje con nombre, edad, país y un gusto, y escribe cuatro frases en inglés para presentarlo.",
)

lesson(
    OA12, 2,
    "Las frases escritas en cada ejercicio y, si quieres, veinte objetos pequeños de casa (como fichas de papel) y una persona para hacer el diálogo.",
    "Aprenderé a decir lo que puedo y no puedo hacer con «I can» e «I can't», y a decir cantidades hasta veinte con «I have» y «There are». Sirve para contar y hablar de habilidades en inglés.",
    ["Sé contar hasta veinte en español.", "Sé verbos como run, jump y swim."],
    [
        "Para decir una habilidad usa «I can» (yo puedo): «I can swim» (puedo nadar). Para decir que no puedes usa «I can't»: «I can't fly» (no puedo volar). Para preguntar usa «Can you swim?» (¿puedes nadar?). Respondes «Yes, I can» (sí puedo) o «No, I can't» (no puedo). Después de can va el verbo solo.",
        "Para decir una cantidad usa «I have» y un número: «I have twelve pencils» (tengo doce lápices). Para decir cuántas cosas hay en un lugar usa «There are»: «There are fifteen apples» (hay quince manzanas). Los números del once al veinte son: eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty. Para preguntar usa «How many apples?» (¿cuántas manzanas?).",
        "Los números del trece al diecinueve terminan en -teen: thirteen, fourteen... nineteen. Para contar bien, toca cada objeto una sola vez y no te saltes ninguno. Cuando respondas, di una frase completa: «There are fifteen» (hay quince).",
    ],
    [("I can", "yo puedo"), ("I can't", "yo no puedo"), ("Can you...?", "¿puedes...?"), ("How many?", "¿cuántos?"), ("eleven / twelve", "once / doce"), ("twenty", "veinte")],
    [
        ("Decir una habilidad", "Sabes nadar pero no volar. ¿Qué dices en dos frases?", ["Para nadar uso I can swim.", "Para volar uso I can't fly.", "Junto las dos frases."], "I can swim. I can't fly."),
        ("Decir una cantidad", "Tienes 12 lápices. ¿Qué dices?", ["Uso I have.", "El doce se escribe twelve.", "Agrego pencils."], "I have twelve pencils."),
    ],
    [
        ("Decir «I am can swim».", "Se mezclan am y can.", "Después de can va el verbo solo: I can swim."),
        ("Saltarse un objeto al contar o contarlo dos veces.", "Se cuenta sin tocar cada objeto.", "Toca cada objeto una sola vez."),
    ],
    [
        ("¿Qué significa «I can't»?", "No puedo", "Es la forma negativa de I can."),
        ("¿Cómo se dice 12 en inglés?", "twelve", "Es el número después de eleven."),
        ("¿Qué significa «How many?»", "¿Cuántos?", "Se usa para preguntar cantidades."),
    ],
    [
        ("¿Cómo respondes «Can you jump?» si puedes?", "Yes, I can", "Es la respuesta corta afirmativa."),
        ("¿Qué terminación tienen los números del 13 al 19?", "-teen", "Es el final de esos números."),
        ("¿Qué palabra se usa para decir que no puedes hacer algo?", "can't", "I can't significa no puedo."),
    ],
    [
        ("Completa: «I ___ run.» (puedo)", "can", "I can run es puedo correr."),
        ("Completa con el número en inglés: «I have ___ apples.» (15)", "fifteen", "Fifteen es quince."),
        ("Escribe en español la frase «I can't fly».", "No puedo volar", "Fly es volar y can't es no puedo."),
    ],
    [
        ("Alguien dice «I am can swim». ¿Cómo se corrige?", "I can swim", "Can no lleva am antes."),
        (f"En una bolsa hay estas fichas: {dots(18)}. Completa con el número en inglés: «There are ___ counters.»", "eighteen", "Hay 18 fichas, y 18 es eighteen."),
    ],
    [
        (f"Cuenta los puntos: {dots(13)}. Escribe cuántos hay, en inglés.", "thirteen", "Hay 13 puntos y 13 es thirteen."),
        (f"Hay {dots(14)} manzanas y luego llegan 5 más. ¿Cuántas hay en total? Escribe el número en inglés.", "nineteen", "14 más 5 son 19, nineteen."),
    ],
    [("Un niño dice «I have twenty cars» (cars son autos) y tú quieres preguntar cuántos autos tiene, sin repetir el número. Escribe la pregunta en inglés con How many.", "How many cars?", "How many pregunta la cantidad.")],
    [
        ("¿Cómo se dice 20 en inglés?", "twenty", "Es el número final de la serie."),
        ("¿Qué significa «Can you swim?»", "¿Puedes nadar?", "Can you es puedes."),
        ("Responde si no puedes volar: «No, I ___.»", "can't", "No, I can't es la respuesta corta."),
    ],
    task("Con una persona de tu casa, cuenta 20 objetos pequeños (como fichas de papel) en inglés, del one al twenty, tocando cada uno. Luego responde dos preguntas: «Can you swim?» y «Can you jump?» con respuesta corta. Por último di en voz alta dos frases tuyas: «I can ___» y «I can't ___», y una cantidad: «I have ___ ...».", "«One, two, three... twenty.» «Yes, I can.» «I can swim. I can't fly.» «I have twelve pencils.»", ["cuenta hasta twenty sin saltarse números", "usa can y can't", "responde con respuesta corta", "dice una cantidad con I have o There are"], ["nota de la persona que contó con él o ella"], ["saltarse un número", "decir I am can"], "Celebra los números bien dichos y repite con él o ella los que terminan en -teen."),
    "Cuenta tus dedos hasta veinte en inglés usando manos y pies.",
    "Escribe tres frases con I can y dos con I can't sobre cosas que haces tú.",
)

lesson(
    OA12, 3,
    "Las frases y descripciones escritas en cada ejercicio, un lápiz y una persona de tu casa para hacer el diálogo.",
    "Aprenderé a describir animales, comida, ocupaciones y lugares de la escuela, y a decir qué está prohibido con «Don't...». Sirve para hablar de lo que veo y de las reglas de la escuela.",
    ["Sé animales y comidas en inglés.", "Sé colores: red, blue, green, yellow, brown."],
    [
        "Para decir qué es algo usa «It is a dog» (es un perro) o «It is an elephant» (es un elefante). Se usa «an» antes de las palabras que empiezan con sonido de vocal (a, e, i, o, u), como elephant, apple y egg. Para describir usa «It is» y una palabra: «It is big» (es grande), «It is small» (es pequeño), «It is brown» (es café). Para la comida: «The apple is red» (la manzana es roja).",
        "Para las ocupaciones: «He is a doctor» (él es doctor) y «She is a teacher» (ella es profesora). También se dice «She is a farmer» (ella es agricultora) y «He is a cook» (él es cocinero). Los lugares de la escuela son: classroom (sala), library (biblioteca), playground (patio de juegos) y gym (gimnasio). Se describen así: «This is the library. It is quiet» (esta es la biblioteca; es tranquila).",
        "Para decir que algo está prohibido usa «Don't» y un verbo: «Don't run!» (¡no corras!), «Don't shout!» (¡no grites!), «Don't push!» (¡no empujes!). Es una orden para cuidar a todos: dila con voz firme pero amable. Para un lugar agrega «in the...»: «Don't shout in the library» (no grites en la biblioteca).",
    ],
    [("big / small", "grande / pequeño"), ("He is / She is", "él es / ella es"), ("library", "biblioteca"), ("Don't run!", "¡no corras!"), ("Don't shout!", "¡no grites!"), ("quiet", "tranquilo, en silencio")],
    [
        ("Describir un animal", "Un oso grande y café. ¿Qué dices? (bear es oso)", ["Digo qué es: It is a bear.", "Describo: It is big.", "Agrego el color: brown."], "It is a bear. It is big and brown."),
        ("Decir una prohibición", "Un niño corre en la sala. ¿Qué dices?", ["Uso Don't.", "El verbo es run.", "Agrego un lugar si quiero."], "Don't run!"),
    ],
    [
        ("Decir «No run!» para prohibir.", "Se traduce palabra por palabra.", "Usa Don't y el verbo: Don't run!"),
        ("Decir «He is teacher» sin a.", "Se olvida la palabra a.", "Se dice He is a teacher."),
    ],
    [
        ("¿Qué significa «Don't shout!»?", "¡No grites!", "Shout es gritar y don't es no."),
        ("¿Qué significa «library»?", "Biblioteca", "Es el lugar de los libros."),
        ("¿Qué significa «small»?", "Pequeño", "Es lo contrario de big."),
    ],
    [
        ("¿Qué dos palabras se usan para prohibir algo?", "Don't y un verbo", "Don't va delante del verbo."),
        ("¿Cuál describe bien a un gato negro y pequeño? (a) «It is black and small.» (b) «It black small.»", "a", "Se usa It is antes de las características."),
        ("¿Para qué sirven las prohibiciones en la escuela?", "Para cuidar a todos", "Las reglas protegen."),
    ],
    [
        ("Completa: «She is a ___.» (profesora)", "teacher", "Teacher es profesora."),
        ("Completa: «Don't ___ in the library!» (gritar)", "shout", "Shout es gritar."),
        ("Completa: «The banana is ___.» (amarilla)", "yellow", "Yellow es amarillo."),
    ],
    [
        ("Tomás dice «He is teacher» sobre su profesor. ¿Qué palabra le falta?", "a", "Se dice He is a teacher."),
        ("Una niña dice «Don't running!». ¿Cómo se corrige?", "Don't run!", "Después de Don't va el verbo solo."),
    ],
    [
        ("[Un elefante grande y gris.] Completa: «It is an elephant. It is ___ and gray.» (grande)", "big", "Big es grande."),
        ("[Un niño empuja a otro en la fila.] Escribe la prohibición en inglés con dos palabras.", "Don't push", "Push es empujar."),
    ],
    [("En el pasillo de la escuela alguien grita. Dile en inglés, con dos palabras, que no grite.", "Don't shout", "Se usa para pedir silencio.")],
    [
        ("¿Cómo se dice «patio de juegos» en inglés?", "playground", "Es el lugar donde se juega en el recreo."),
        ("¿Cómo se dice «grande» en inglés?", "big", "Es lo contrario de small."),
        ("¿Qué significa «He is a doctor»?", "Él es doctor", "Doctor es una ocupación."),
    ],
    task("Con una persona de tu casa, haz tres descripciones: (1) un animal, por ejemplo un perro: «It is a dog. It is big. It is brown.» (2) una ocupación: «She is a teacher.» (3) un lugar de tu escuela: «This is the library. It is quiet.» Luego di dos prohibiciones: «Don't run!» y «Don't shout!» con voz amable. Dibuja uno de los tres para apoyarte.", "«It is a dog. It is big. It is brown. She is a teacher. This is the library. Don't run!»", ["describe un animal", "dice una ocupación con a", "describe un lugar", "usa Don't con un verbo"], ["el dibujo", "nota de la persona que escuchó"], ["olvidar a en las ocupaciones", "decir Don't running"], "Valora la descripción y repite con él o ella las prohibiciones con voz amable."),
    "Dibuja un animal y escribe una frase con It is.",
    "Escribe tres reglas de tu sala en inglés con Don't.",
)

lesson(
    OA12, 4,
    "Las frases y preguntas escritas en cada ejercicio, algunos objetos de casa (una pelota, una caja, una mesa) y una persona de tu casa.",
    "Aprenderé a preguntar y responder sobre comida con «Do you like...?» y «Can I have...?», y a decir dónde está un objeto. Sirve para pedir información y ubicar cosas en inglés.",
    ["Sé nombres de comida y objetos.", "Sé que in significa dentro y on significa sobre."],
    [
        "Para preguntar por un gusto de comida usa «Do you like apples?» (¿te gustan las manzanas?). Respondes «Yes, I do» (sí) o «No, I don't» (no). Para pedir comida usa «Can I have an apple, please?» (¿puedo tener una manzana, por favor?). Quien da dice «Here you are» (aquí tienes). Se usa «an» antes de apple porque empieza con vocal.",
        "Para saber dónde está algo usa «Where is the ball?» (¿dónde está la pelota?). Para responder usa palabras de lugar: in (dentro de), on (sobre), under (debajo de), next to (al lado de), behind (detrás de). Por ejemplo: «It's under the table» (está debajo de la mesa). «It's» es la forma corta de «it is».",
        "Usa objetos reales para practicar. Pon una pelota sobre la mesa, bajo la mesa y en una caja, y di cada vez: «It's on the table», «It's under the table», «It's in the box». Mirar el objeto te ayuda a recordar la palabra de lugar.",
    ],
    [("Do you like...?", "¿te gusta...?"), ("Yes, I do / No, I don't", "sí / no"), ("Where is...?", "¿dónde está...?"), ("in / on / under", "dentro de / sobre / debajo de"), ("next to", "al lado de"), ("behind", "detrás de")],
    [
        ("Preguntar por comida", "Quieres saber si a tu amigo le gustan las bananas. ¿Qué preguntas?", ["Uso Do you like.", "Digo bananas.", "Cierro con signo de interrogación."], "Do you like bananas?"),
        ("Decir dónde está", "La pelota está debajo de la mesa. ¿Qué respondes a «Where is the ball?»", ["Busco la palabra under.", "Digo It's under.", "Agrego the table."], "It's under the table."),
    ],
    [
        ("Responder «Yes, I like» a una pregunta con Do.", "Se mezcla la forma de la respuesta.", "Responde Yes, I do."),
        ("Usar on cuando algo está dentro de una caja.", "Se confunden las palabras de lugar.", "Dentro es in; sobre es on."),
    ],
    [
        ("¿Qué significa «under»?", "Debajo de", "Indica abajo de algo."),
        ("¿Qué significa «Where is the ball?»", "¿Dónde está la pelota?", "Where es dónde."),
        ("¿Qué significa «Yes, I do»?", "Sí, me gusta", "Responde a Do you like...?"),
    ],
    [
        ("¿Qué palabra de lugar significa «sobre»?", "on", "On indica encima de algo."),
        ("¿Cómo respondes «Do you like pizza?» si no te gusta?", "No, I don't", "Es la respuesta negativa."),
        ("¿Cuál es la diferencia entre in y on?", "In es dentro de y on es sobre", "Indican posiciones distintas."),
    ],
    [
        ("Completa: «The cat is ___ the box.» (dentro de)", "in", "In significa dentro de."),
        ("Completa: «The book is ___ the table.» (sobre)", "on", "On significa sobre."),
        ("Te preguntan «Do you like milk?» y a ti sí te gusta. Escribe la respuesta corta.", "Yes, I do", "Do se repite en la respuesta."),
    ],
    [
        ("[La pelota está detrás de la silla.] Completa: «It's ___ the chair.»", "behind", "Behind significa detrás de."),
        ("Ana pregunta «Where is the apple?» y Leo responde «It's on the box». La manzana está dentro de la caja. ¿Qué palabra debe cambiar Leo?", "on por in", "Si está dentro, se usa in."),
    ],
    [
        ("[El gato está al lado del perro.] Completa con dos palabras: «The cat is ___ the dog.»", "next to", "Next to es al lado de."),
        ("Pregunta: «Where is the apple?» [La manzana está en la caja.] Escribe la respuesta con It's.", "It's in the box", "In indica dentro."),
    ],
    [("Una persona de tu casa pregunta «Where is the ball?» y la pelota está bajo la cama. Responde en inglés con It's (bed es cama).", "It's under the bed", "Under es debajo de y bed es cama.")],
    [
        ("¿Cómo se dice «detrás de» en inglés?", "behind", "Es una palabra de lugar."),
        ("¿Cómo pides una manzana con amabilidad?", "Can I have an apple, please?", "Se usa Can I have y please."),
        ("Escribe cómo preguntas si a alguien le gustan las manzanas.", "Do you like apples?", "Se usa Do you like."),
    ],
    task("Con una persona de tu casa, pon una pelota (u otro objeto seguro) en cinco lugares: sobre la mesa, bajo la mesa, dentro de una caja, al lado de una silla y detrás de la silla. La otra persona pregunta «Where is the ball?» y tú respondes «It's ___ the ___». Después ella pregunta «Do you like apples?» y respondes Yes, I do o No, I don't. Por último pide una fruta: «Can I have an apple, please?».", "«It's on the table.» «It's in the box.» «Yes, I do.» «Can I have an apple, please?»", ["usa cinco palabras de lugar", "responde con It's...", "responde la pregunta de gusto", "pide comida con Can I have...?"], ["nota de la persona que preguntó"], ["confundir in y on", "responder Yes, I like"], "Mueve el objeto con él o ella para reforzar cada palabra de lugar."),
    "Pon un lápiz en tres lugares y di «It's ___ the ___» cada vez.",
    "Escribe una pregunta y su respuesta sobre un alimento y otra sobre un objeto.",
)

lesson(
    OA12, 5,
    "Las frases escritas en cada ejercicio, una persona de tu casa para hacer mímica y espacio libre para moverte con cuidado.",
    "Aprenderé a decir lo que alguien hace en este momento con «is», «are» y la terminación -ing. Sirve para describir acciones que ocurren ahora.",
    ["Sé verbos básicos: read, eat, play, sleep.", "Sé decir He is y She is."],
    [
        "Para decir lo que pasa ahora usa «is» o «are» y el verbo con -ing. «She is reading» (ella está leyendo). «He is eating» (él está comiendo). «They are playing» (ellos están jugando). Para hablar de ti: «I'm drawing» (estoy dibujando). Usa «is» con he, she e it; «are» con they; «I'm» con yo.",
        "Con estos verbos solo se agrega -ing: read → reading, eat → eating, play → playing, draw → drawing, sing → singing, jump → jumping, drink → drinking, sleep → sleeping. Tres verbos duplican la última letra: run → running, swim → swimming, sit → sitting. Dos verbos pierden la e: write → writing, dance → dancing.",
        "Para preguntar usa «What are you doing?» (¿qué estás haciendo?). Respondes «I'm reading». Para preguntar por otra persona: «What is he doing?» (¿qué está haciendo él?). Mira una imagen o haz mímica con una persona de tu casa para practicar. Haz los movimientos con cuidado y sin correr dentro de casa.",
    ],
    [("I'm... -ing", "estoy haciendo"), ("He is / She is", "él / ella está"), ("They are", "ellos están"), ("reading", "leyendo"), ("eating", "comiendo"), ("What are you doing?", "¿qué estás haciendo?")],
    [
        ("Describir una acción", "[Una niña lee un libro.] ¿Qué dices?", ["Uso She is.", "El verbo es read.", "Le agrego -ing."], "She is reading."),
        ("Verbo que duplica la letra", "[Dos niños corren.] ¿Qué dices?", ["Uso They are.", "Run se escribe running.", "Duplico la n."], "They are running."),
    ],
    [
        ("Decir «She reading» sin is.", "Se olvida is o are.", "Siempre va is o are antes del verbo con -ing."),
        ("Escribir runing con una sola n.", "No se duplica la consonante.", "Run se escribe running."),
    ],
    [
        ("¿Qué significa «He is eating»?", "Él está comiendo", "Is eating es está comiendo."),
        ("¿Qué significa «What are you doing?»", "¿Qué estás haciendo?", "Pregunta por la acción ahora."),
        ("¿Qué terminación tienen los verbos que cuentan lo que pasa ahora?", "-ing", "Se agrega al final del verbo."),
    ],
    [
        ("¿Cuándo usas «are»?", "Con they", "Con varias personas se usa are."),
        ("¿Cómo respondes «What are you doing?» si estás leyendo?", "I'm reading", "I'm más el verbo con -ing."),
        ("¿Cómo se escribe «swim» con -ing?", "swimming", "Se duplica la m."),
    ],
    [
        ("Completa: «She is ___.» (leyendo)", "reading", "Read más ing."),
        ("[Un niño bebe agua.] Completa: «He is ___ water.»", "drinking", "Drinking es bebiendo."),
        ("[Dos niñas juegan.] Completa: «They ___ playing.»", "are", "Con they se usa are."),
    ],
    [
        ("Marta dice «He eating a banana». ¿Qué palabra le falta?", "is", "Se necesita is antes de eating."),
        ("Luis escribe «sitting» como «siting». ¿Qué letra falta?", "t", "Sit duplica la t."),
    ],
    [
        ("[Un gato duerme.] Escribe la oración completa con It is.", "It is sleeping", "Sleep más ing."),
        ("[Dos niños escriben en sus cuadernos.] Completa: «They are ___.» (escribiendo)", "writing", "Write pierde la e y recibe ing."),
    ],
    [("Estás en una videollamada con un amigo y él pregunta «What are you doing?». Estás dibujando. Responde en inglés.", "I'm drawing", "Draw más ing.")],
    [
        ("¿Cómo se dice «jugando» en inglés?", "playing", "Play más ing."),
        ("¿Qué significa «They are running»?", "Ellos están corriendo", "Running es corriendo."),
        ("¿Qué escribes antes del verbo con ing en «He ___ reading»?", "is", "Con he se usa is."),
    ],
    task("Con una persona de tu casa, haz mímica de cinco acciones: reading, eating, drinking, sleeping y jumping (salta con cuidado). La otra persona hace una mímica y pregunta «What is he doing?» o «What is she doing?» imaginando un personaje; tú respondes «He is reading» o «She is reading». Luego cambian: tú haces la mímica y ella responde. Al final, di qué haces tú: «I'm ...».", "La persona simula leer. Tú dices «She is reading». Luego, «I'm jumping».", ["usa is o are", "usa verbos con -ing", "reconoce las cinco acciones", "usa What is he doing?"], ["nota de la persona que hizo la mímica"], ["olvidar is", "escribir runing"], "Repite con él o ella las acciones que le costaron."),
    "Mira a alguien de tu casa y di en inglés lo que hace ahora.",
    "Escribe tres frases con -ing sobre lo que hacen ahora tres personas que conoces o tres personajes que dibujes.",
)

# ================================================================ OA 13
lesson(
    OA13, 1,
    "Las frases escritas en cada ejercicio, lápiz grafito, goma y una hoja con renglones.",
    "Aprenderé a copiar oraciones simples en inglés por bloques con sentido, cuidando la letra mayúscula, los espacios y el punto. Sirve para escribir bien desde un modelo.",
    ["Sé escribir mi nombre.", "Sé que las oraciones empiezan con mayúscula en español."],
    [
        "Copiar bien no es escribir letra por letra sin pensar. Se copia por bloques con sentido (chunks): «My name is» | «Ana» | «.» Cada bloque se lee, se tapa y se escribe de memoria, y luego se compara con el modelo. Así te fijas en el significado: «My name is Ana» quiere decir me llamo Ana.",
        "En inglés, como en español, cada oración empieza con mayúscula (capital letter). Los nombres de personas, como Ana, también llevan mayúscula. La palabra I (yo) siempre se escribe con mayúscula. Entre palabra y palabra hay un espacio, y al final de la oración va un punto (period).",
        "Para revisar tu copia haz tres preguntas: ¿empieza con mayúscula?, ¿hay un espacio entre las palabras?, ¿termina con punto? Si falta algo, corrige con lápiz. Copiar con cuidado hace que tu escritura se entienda y te ayuda a recordar cómo se escriben las palabras.",
    ],
    [("copy", "copiar"), ("capital letter", "letra mayúscula"), ("space", "espacio"), ("period", "punto final"), ("My name is...", "me llamo..."), ("I'm...", "tengo... años")],
    [
        ("Copiar por bloques", "Modelo: «My name is Ana.» ¿Cómo lo copias?", ["Divido en bloques: My name is | Ana | punto.", "Leo un bloque, lo tapo y lo escribo.", "Comparo con el modelo."], "My name is Ana."),
        ("Revisar una copia", "Una copia dice: «my name is ana». Compárala con el modelo «My name is Ana.»", ["Falta la mayúscula al comienzo.", "Falta la mayúscula en Ana.", "Falta el punto final."], "Se corrige a My name is Ana."),
    ],
    [
        ("Copiar sin mayúscula al comienzo.", "No se mira el modelo con atención.", "Revisa la primera letra de cada oración."),
        ("Pegar las palabras sin espacio.", "Se copia como una sola palabra.", "Deja un espacio entre palabras."),
    ],
    [
        ("Copia exactamente: «I like pizza.»", "I like pizza.", "Se copia con mayúscula en I y punto final."),
        ("¿Qué signo va al final de la oración «I like pizza»?", "Un punto", "El punto cierra la oración."),
        ("¿Qué significa «My name is Ana»?", "Me llamo Ana", "My name is dice el nombre."),
    ],
    [
        ("¿Con qué letra empieza una oración en inglés?", "Con mayúscula", "Todas empiezan con mayúscula."),
        ("¿Cómo se escribe la palabra I (yo) en medio de una oración?", "Con mayúscula", "I siempre es mayúscula."),
        ("¿Por qué se copia por bloques con sentido?", "Para fijarse en el significado y no escribir sin pensar", "Los bloques ayudan a entender lo que se copia."),
    ],
    [
        ("Copia exactamente: «I'm eight.»", "I'm eight.", "Se copia con mayúscula en I, apóstrofo y punto."),
        ("Copia exactamente: «The cat is big.»", "The cat is big.", "Se copia con mayúscula en The y punto final."),
        ("Copia exactamente: «She is a teacher.»", "She is a teacher.", "Se copian las cuatro palabras con punto final."),
    ],
    [
        ("Un niño copió «i like pizza» con minúsculas. ¿Qué dos cosas corriges?", "La mayúscula de I y el punto final", "I siempre es mayúscula y la oración termina con punto."),
        ("Una niña copió «Mynameis Ana.» ¿Qué falta?", "Los espacios entre las palabras", "Cada palabra se separa con un espacio."),
    ],
    [
        ("Modelo: «My name is Leo.» Una copia dice «My name is leo.» ¿Qué palabra corriges?", "leo por Leo", "Los nombres llevan mayúscula."),
        ("Modelo: «The dog is brown.» Una copia dice «The dog brown.» ¿Qué palabra falta?", "is", "Falta is entre dog y brown."),
    ],
    [("En la sala de clases hay un cartel con el modelo «We like the library.» (library es biblioteca). Copia el cartel en tu cuaderno por bloques.", "We like the library.", "Se copia con mayúscula en We y punto final.")],
    [
        ("¿Cómo se dice «punto final» en inglés?", "period", "Es el signo al final de la oración."),
        ("¿Cómo se dice «mayúscula» en inglés?", "capital letter", "Es la letra grande del comienzo."),
        ("Entre palabra y palabra, ¿qué dejas?", "Un espacio", "Así las palabras se leen separadas."),
    ],
    task("Copia en tu cuaderno por bloques con sentido estas tres oraciones modelo: (1) «My name is Ana.» (2) «I like pizza.» (3) «The cat is big.» Lee un bloque, tápalo y escríbelo de memoria; luego compara con el modelo. Revisa en cada oración la mayúscula, los espacios y el punto. Una persona de tu casa revisa tu copia.", "My name is Ana. I like pizza. The cat is big.", ["copia las tres oraciones", "usa mayúscula, espacios y punto", "copia por bloques", "corrige con lápiz si algo falta"], ["la copia en el cuaderno", "nota de la persona que revisó"], ["copiar sin mayúscula", "escribir las palabras pegadas"], "Pide que lea la copia en voz alta y señala con el dedo mayúscula, espacios y punto."),
    "Copia dos oraciones de este cuaderno en tu cuaderno de inglés y revísalas.",
    "Copia el nombre de tres animales y su descripción: «It is big.»",
)

lesson(
    OA13, 2,
    "Los bancos de palabras escritos en cada ejercicio, lápiz y una hoja con renglones.",
    "Aprenderé a completar oraciones simples en inglés usando un banco de palabras. Sirve para escribir oraciones correctas elegiendo la palabra que tiene sentido.",
    ["Sé copiar oraciones cuidando la mayúscula y el punto.", "Sé algunas palabras de animales y colores."],
    [
        "Un banco de palabras (word bank) es una lista de palabras que puedes usar para completar una oración. Primero lee la oración completa e intenta entenderla. Luego mira el espacio en blanco, que se escribe así: ___. Por último elige del banco la palabra que tiene sentido y escríbela.",
        "Para elegir bien, fíjate en el modelo: «I have a ___.» con el banco: cat, dog, red. Cat y dog son animales y sirven: «I have a cat». Red es un color y no sirve en esa oración porque «I have a red» quedaría incompleta. También importa el orden de las palabras (word order): primero el color y después el animal: «a red cat», no «a cat red».",
        "Cuando termines, lee la oración entera en voz alta. Si suena bien y tiene sentido, está lista. Después revisa la mayúscula al comienzo, los espacios entre las palabras y el punto final. Si una palabra del banco no cabe en ningún espacio, es un distractor y no se usa.",
    ],
    [("word bank", "banco de palabras"), ("complete", "completar"), ("word order", "orden de las palabras"), ("cat", "gato"), ("dog", "perro"), ("red", "rojo")],
    [
        ("Completar con sentido", "Oración: «I have a ___.» Banco: cat, dog, red. Completa con un animal; usa cat.", ["Leo la oración completa.", "Busco una palabra que sea un animal.", "Cat es un animal y encaja."], "I have a cat."),
        ("Cuidar el orden", "Oración: «I have a ___ cat.» Banco: red, big. Completa con red.", ["El color va antes del animal.", "Pongo red delante de cat.", "Releo la oración."], "I have a red cat."),
    ],
    [
        ("Elegir una palabra solo porque está primero en el banco.", "No se revisa el sentido.", "Lee la oración completa antes de elegir."),
        ("Escribir el color después del animal, como «a cat red».", "Se copia el orden del español.", "En inglés el color va antes: a red cat."),
    ],
    [
        ("¿Qué es un «word bank»?", "Una lista de palabras para completar", "Se usa para elegir la palabra correcta."),
        ("¿Qué significa «complete»?", "Completar", "Es llenar el espacio de la oración."),
        ("¿Qué significa «red»?", "Rojo", "Es un color."),
    ],
    [
        ("Oración: «I have a ___.» Banco: dog, big. ¿Cuál completa mejor?", "dog", "Dog es un animal y encaja después de a."),
        ("¿Por qué no se usa una palabra del banco que no cabe?", "Porque no tiene sentido en la oración", "Es un distractor."),
        ("¿Qué haces al terminar de completar?", "Leo la oración y reviso mayúscula, espacios y punto", "Así compruebo que está bien."),
    ],
    [
        ("Completa con una palabra del banco (cat, red): «The ___ is big.»", "cat", "Cat es el nombre del animal que es grande."),
        ("Completa con una palabra del banco (blue, bird): «I have a ___ ball.»", "blue", "Blue es un color y va antes de ball."),
        ("Completa con una palabra del banco (like, red): «I ___ pizza.»", "like", "Con I se usa like."),
    ],
    [
        ("Pedro escribió «I have a cat red». ¿Cómo debe quedar la oración?", "I have a red cat", "El color va antes del animal."),
        ("Ana completó «The dog is ___.» con apple. Banco: apple, brown. ¿Cuál palabra debió usar?", "brown", "Brown describe al perro y apple no."),
    ],
    [
        ("Completa la oración con las palabras del banco (big, cat): «The ___ is ___.» Escribe las dos palabras separadas por coma, en ese orden: animal y descripción.", "cat, big", "The cat is big tiene sentido."),
        ("Oración: «She is a ___.» Banco: teacher, blue, run. ¿Cuál completa?", "teacher", "Teacher es una ocupación y va después de a."),
    ],
    [("Tu profesora te da la oración «I have a ___ dog.» con el banco: brown, jump. Completa con la palabra del banco que tiene sentido.", "brown", "Brown describe a un perro y jump es un verbo.")],
    [
        ("¿Cómo se dice «orden de las palabras» en inglés?", "word order", "Es el orden de las palabras en la oración."),
        ("¿Qué se hace con una palabra del banco que no sirve?", "No se usa", "Solo se usa la que tiene sentido."),
        ("En Ciencias: «A bee can ___.» Banco: fly, red. Escribe la palabra que completa la oración.", "fly", "Una abeja puede volar; red es un color y no encaja después de can."),
    ],
    task("Completa estas cuatro oraciones eligiendo del banco de palabras: (1) «I have a ___.» (cat, red) (2) «The dog is ___.» (brown, apple) (3) «She is a ___.» (teacher, blue) (4) «I like ___.» (pizza, run). Escribe cada oración completa en tu cuaderno con mayúscula, espacios y punto. Lee cada una en voz alta a una persona de tu casa.", "(1) I have a cat. (2) The dog is brown. (3) She is a teacher. (4) I like pizza.", ["completa las cuatro con sentido", "usa solo palabras del banco", "escribe mayúscula, espacios y punto", "lee en voz alta"], ["las oraciones escritas", "nota de la persona que escuchó"], ["elegir sin leer la oración", "poner el color después del animal"], "Pregunta por qué eligió cada palabra y celebra las oraciones bien ordenadas."),
    "Escribe dos oraciones con I have a y una palabra de animal.",
    "Inventa un banco de tres palabras y una oración con espacio para un compañero.",
)

lesson(
    OA13, 3,
    "Las oraciones modelo escritas en cada ejercicio, lápiz y una hoja con renglones.",
    "Aprenderé a cambiar una parte de una oración modelo (el animal, el color o el número) y a escribir una oración nueva con sentido. Sirve para escribir más sin empezar de cero.",
    ["Sé copiar y completar oraciones.", "Sé animales, colores y números hasta diez."],
    [
        "Una forma de escribir con apoyo es transformar un modelo: cambias solo una parte y mantienes el resto. Modelo: «I have a red ball.» (tengo una pelota roja). Si cambias red por blue, escribes «I have a blue ball». Si cambias ball por bag (mochila), escribes «I have a red bag». Cada cambio debe tener sentido.",
        "También puedes cambiar la cantidad. Con un objeto se usa «a» o «an»: «I have a cat». Con más de uno se usa el número y se agrega -s al final del nombre: «I have two cats» (tengo dos gatos), «I have three dogs», «I have four books». Esta regla funciona para palabras como cat, dog, book, ball, bag y pencil. Antes de apple se usa an: «an apple»; con más, «three apples».",
        "Para revisar la oración nueva, hazte tres preguntas: ¿cambié solo una parte?, ¿tiene sentido?, ¿conservé la mayúscula, los espacios y el punto? Si cambias el número, no olvides cambiar también a por el número y agregar la -s.",
    ],
    [("change", "cambiar"), ("model", "modelo"), ("two cats", "dos gatos"), ("three dogs", "tres perros"), ("bag", "mochila o bolso"), ("blue", "azul")],
    [
        ("Cambiar el color", "Modelo: «I have a red ball.» Cambia red por blue. ¿Qué escribes?", ["Mantengo I have a ... ball.", "Cambio solo red por blue.", "Reviso la mayúscula y el punto."], "I have a blue ball."),
        ("Cambiar la cantidad", "Modelo: «I have a cat.» Quieres decir que tienes dos gatos. ¿Qué escribes?", ["Cambio a por two.", "Agrego -s a cat.", "Escribo cats."], "I have two cats."),
    ],
    [
        ("Cambiar el número y olvidar la -s: «I have two cat».", "Se mantiene la forma del singular.", "Con dos o más se agrega -s: two cats."),
        ("Cambiar tantas partes que ya no queda el modelo.", "Se pierde el apoyo del modelo.", "Cambia solo una parte a la vez."),
    ],
    [
        ("Modelo: «I have a red ball.» Cambia red por blue. Escribe la oración nueva.", "I have a blue ball.", "Solo cambia el color."),
        ("¿Qué significa «I have two cats»?", "Tengo dos gatos", "Two es dos y cats es gatos."),
        ("¿Qué se agrega a cat para hablar de más de un gato?", "La letra s", "Cat se convierte en cats."),
    ],
    [
        ("Modelo: «I have a dog.» Cambia dog por cat. Escribe la oración.", "I have a cat.", "Solo cambia el animal."),
        ("Modelo: «I have a cat.» Cambia a por three y escribe la oración con tres gatos.", "I have three cats.", "Se agrega -s a cat."),
        ("¿Qué tres preguntas haces para revisar una oración nueva?", "Cambié solo una parte, tiene sentido y cuidé mayúscula, espacios y punto", "Así reviso la oración."),
    ],
    [
        ("Modelo: «I have a red bag.» Cambia bag por book (libro). Escribe la oración.", "I have a red book.", "Solo cambia el objeto."),
        ("Modelo: «I have a book.» Escribe la oración con cuatro libros.", "I have four books.", "Four es cuatro y se agrega -s."),
        ("Modelo: «I have a cat.» Cambia cat por apple (manzana). Escribe la oración.", "I have an apple.", "Antes de apple se usa an."),
    ],
    [
        ("Paula escribió «I have two ball». ¿Cómo se corrige?", "I have two balls", "Con dos o más se agrega -s."),
        ("Modelo: «I have a dog.» Tomás cambió y escribió «I have a dog red». ¿Cómo debe quedar con red?", "I have a red dog", "El color va antes del animal."),
    ],
    [
        ("Modelo: «I have a blue ball.» Cambia a blue ball por tres pelotas azules. Escribe la oración.", "I have three blue balls.", "Se cambia a por three y se agrega -s a ball."),
        ("Modelo: «The cat is big.» Cambia cat por dog y big por small. Escribe la oración.", "The dog is small.", "Se cambian dos partes en el modelo."),
    ],
    [("En la lista de materiales de la clase de arte dice «I have a pencil.» (pencil es lápiz). Necesitas escribir que tienes cinco lápices. Escribe la oración.", "I have five pencils.", "Five es cinco y se agrega -s.")],
    [
        ("¿Cómo se dice «modelo» en inglés?", "model", "Es la oración que se usa como guía."),
        ("¿Qué significa «I have three dogs»?", "Tengo tres perros", "Three es tres y dogs es perros."),
        ("¿Cuál de estas palabras lleva an delante: apple, cat o book?", "apple", "Apple empieza con vocal."),
    ],
    task("Con el modelo «I have a red ball.» escribe cuatro oraciones nuevas, cambiando una parte cada vez: (1) cambia el color por blue; (2) cambia ball por bag; (3) cambia a por two y escribe two balls; (4) cambia red ball por apple (manzana) y usa an. Escribe cada oración con mayúscula, espacios y punto. Léelas a una persona de tu casa.", "(1) I have a blue ball. (2) I have a red bag. (3) I have two red balls. (4) I have an apple.", ["cambia una parte por vez", "agrega -s con dos o más", "escribe mayúscula, espacios y punto", "las oraciones tienen sentido"], ["las cuatro oraciones escritas", "nota de la persona que las escuchó"], ["olvidar la -s", "poner el color después del animal"], "Pide que lea la oración y que diga qué parte cambió."),
    "Cambia una palabra en la oración «I have a cat.» y escríbela en tu cuaderno.",
    "Escribe tres oraciones con I have y números del uno al cinco.",
)

lesson(
    OA13, 4,
    "El modelo, la lista de revisión escrita en esta clase, lápiz grafito, goma y una hoja con renglones.",
    "Aprenderé a escribir una oración nueva a partir de un modelo y de una imagen, y a revisarla con una lista. Sirve para escribir con apoyo y mejorar mi texto.",
    ["Sé copiar, completar y cambiar una parte del modelo.", "Sé que la oración lleva mayúscula, espacios y punto."],
    [
        "Escribir con apoyo tiene tres pasos: mirar el modelo, escribir y revisar. Modelo: «The cat is on the chair.» (el gato está sobre la silla). Imagen descrita: [un perro bajo la mesa]. Mantienes la forma y cambias las partes: «The dog is under the table.» (el perro está debajo de la mesa).",
        "Antes de entregar revisa con esta lista: (1) la oración empieza con mayúscula; (2) hay un espacio entre cada palabra; (3) las palabras están en el orden del modelo; (4) tiene sentido con la imagen; (5) termina con punto. La palabra I siempre lleva mayúscula, y los nombres propios, como Ana, también.",
        "Si encuentras un error, corrígelo con lápiz y vuelve a leer la oración en voz alta. No es un problema equivocarse: revisar es parte de escribir. Si no estás seguro de cómo se escribe una palabra, mira el modelo o el banco de palabras antes de inventarla.",
    ],
    [("model", "modelo"), ("check", "revisar"), ("word order", "orden de las palabras"), ("capital letter", "letra mayúscula"), ("space", "espacio"), ("period", "punto final")],
    [
        ("Escribir con un modelo y una imagen", "Modelo: «The cat is on the chair.» Imagen: [un perro bajo la mesa]. ¿Qué escribes?", ["Mantengo la forma The ... is ... the ....", "Cambio cat por dog, on por under, chair por table.", "Reviso la oración."], "The dog is under the table."),
        ("Revisar con la lista", "Una oración dice «the dog is under the table». ¿Qué corriges con la lista?", ["Reviso la mayúscula: falta en The.", "Reviso los espacios: están bien.", "Reviso el punto: falta."], "The dog is under the table."),
    ],
    [
        ("Entregar la oración sin revisarla.", "Se piensa que escribir una vez es suficiente.", "Revisa con la lista antes de entregar."),
        ("Cambiar el orden de las palabras sin darse cuenta.", "Se escribe como en español.", "Compara el orden con el del modelo."),
    ],
    [
        ("¿Cuántos pasos tiene escribir con apoyo?", "Tres: mirar el modelo, escribir y revisar", "Esos son los pasos de la clase."),
        ("¿Qué significa «check»?", "Revisar", "Se usa para comprobar la oración."),
        ("¿Con qué signo termina la oración?", "Con un punto", "El punto cierra la oración."),
    ],
    [
        ("¿Qué compruebas con la mayúscula en la lista?", "Que la oración empieza con una letra mayúscula", "Es el primer punto de la lista."),
        ("¿Qué haces si no sabes escribir una palabra?", "Miro el modelo o el banco de palabras", "Ahí está la palabra escrita."),
        ("¿Qué haces con un error que encuentras?", "Lo corrijo con lápiz", "Corregir es parte de escribir."),
    ],
    [
        ("Modelo: «The cat is on the chair.» Imagen: [un perro sobre la mesa]. Escribe la oración nueva.", "The dog is on the table.", "Se cambian cat por dog y chair por table."),
        ("Modelo: «The ball is in the box.» Imagen: [una pelota bajo la mesa]. Escribe la oración nueva.", "The ball is under the table.", "Se cambian in por under y box por table."),
        ("Modelo: «She is a teacher.» Imagen: [un hombre que es doctor]. Escribe la oración nueva.", "He is a doctor.", "Se cambian She por He y teacher por doctor."),
    ],
    [
        ("Ana escribió «The cat on is the chair». ¿Qué problema tiene?", "El orden de las palabras", "Debe ser The cat is on the chair."),
        ("Leo revisó su oración y encontró «the dog is brown» sin mayúscula ni punto. ¿Cómo debe quedar?", "The dog is brown.", "Se agrega la mayúscula y el punto."),
    ],
    [
        ("Ordena las palabras para formar una oración: dog / The / brown / is. Escribe la oración con punto.", "The dog is brown.", "Se respeta el orden sujeto, verbo y descripción."),
        ("Modelo: «I have a cat.» Imagen: [dos pelotas que son tuyas]. Escribe la oración con two balls.", "I have two balls.", "Se cambia a cat por two balls con -s."),
    ],
    [("Tu profesora pega en la pizarra el modelo «The book is on the table.» y una imagen descrita: [una mochila debajo de la silla]. Escribe tu oración con bag, under y chair.", "The bag is under the chair.", "Se mantiene la forma y se cambian las tres partes.")],
    [
        ("¿Qué lista usas para revisar tu oración?", "La lista de revisión de la clase", "Tiene cinco puntos."),
        ("¿Qué significa «The dog is under the table»?", "El perro está debajo de la mesa", "Under es debajo de."),
        ("¿Se puede entregar sin revisar?", "No", "La revisión forma parte de escribir."),
    ],
    task("Escribe dos oraciones a partir de modelos e imágenes. (1) Modelo: «The cat is on the chair.» Imagen: [un perro bajo la mesa]. (2) Modelo: «I have a red ball.» Imagen: [dos mochilas azules que son tuyas]. Revisa cada una con la lista: mayúscula, espacios, orden, sentido con la imagen y punto. Lee tus oraciones a una persona de tu casa y corrige con lápiz si algo falta.", "(1) The dog is under the table. (2) I have two blue bags.", ["escribe las dos oraciones", "mantiene la forma del modelo", "revisa con la lista", "tiene sentido con la imagen"], ["las dos oraciones escritas", "nota de la persona que las escuchó"], ["no revisar", "cambiar el orden de las palabras"], "Pregunta qué cambió y qué corrigió; valora el uso de la lista."),
    "Escribe una oración con un modelo de este cuaderno y revisa los cinco puntos.",
    "Escribe tres oraciones nuevas a partir del modelo «The cat is on the chair.»",
)
