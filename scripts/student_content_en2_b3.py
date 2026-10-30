"""Student material for 2.º básico Inglés, EN02 OA 12 (expresión oral con apoyo para funciones conocidas).

Datos personales: solo nombre de pila, edad, país y gustos; nunca dirección, teléfono ni datos sensibles.
Las situaciones se describen con imágenes entre corchetes porque el cuaderno no incluye ilustraciones.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA12 = "EN02 OA 12"


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


lesson(
    OA12, 1,
    "Las frases y preguntas escritas en cada ejercicio, un adulto para conversar y, si quieres, un dibujo tuyo. No se escriben direcciones ni teléfonos.",
    "Aprenderé a compartir información personal segura en inglés: mi nombre, mi edad, mi país y lo que me gusta. Sirve para presentarme y conocer a otros sin entregar datos privados.",
    ["Sé decir hello y I'm...", "Sé decir mi nombre y mi edad."],
    [
        "Para decir tu nombre usa «My name is Ana» (me llamo Ana). Para decir tu edad usa «I'm seven» (tengo siete años). Para decir de qué país eres usa «I'm from Chile» (soy de Chile). Para decir lo que te gusta usa «I like pizza» (me gusta la pizza).",
        "Para preguntar a otro, usa cuatro preguntas: «What's your name?» (¿cómo te llamas?), «How old are you?» (¿cuántos años tienes?), «Where are you from?» (¿de dónde eres?) y «What do you like?» (¿qué te gusta?). Puedes responder con las frases que aprendiste. Mira a la persona y habla con voz clara.",
        "Hay información que es privada y no se comparte con personas que no conoces: tu dirección, tu teléfono, el nombre de tu colegio y las claves. En esta clase solo usamos datos seguros: nombre de pila, edad, país y gustos. Si alguien te pide un dato privado, puedes decir «No, thank you» (no, gracias) y avisar a un adulto.",
    ],
    [("My name is...", "me llamo..."), ("I'm...", "tengo... años"), ("I'm from...", "soy de..."), ("I like...", "me gusta..."), ("What's your name?", "¿cómo te llamas?"), ("How old are you?", "¿cuántos años tienes?")],
    [
        ("Presentación segura", "Te llamas Leo, tienes ocho años y eres de Chile. ¿Qué dices en tres frases?", ["Digo mi nombre con My name is.", "Digo la edad con I'm.", "Digo el país con I'm from."], "My name is Leo. I'm eight. I'm from Chile."),
        ("Responder una pregunta", "Te preguntan «How old are you?» y tienes siete años. ¿Qué respondes?", ["Entiendo que preguntan la edad.", "Respondo con I'm.", "Digo el número en inglés."], "I'm seven."),
    ],
    [
        ("Decir «I have seven years».", "Se traduce palabra por palabra del español.", "En inglés se dice I'm seven."),
        ("Contar la dirección para presentarse.", "Se cree que hay que dar muchos datos.", "Usa nombre, edad, país y gustos; guarda lo privado."),
    ],
    [
        ("¿Qué significa «My name is Ana»?", "Me llamo Ana", "My name is dice el nombre."),
        ("¿Cómo se dice «tengo siete años» en inglés?", "I'm seven", "En inglés se usa I'm."),
        ("¿Qué significa «I'm from Chile»?", "Soy de Chile", "From indica el origen."),
    ],
    [
        ("¿Qué datos personales son seguros para compartir al presentarte?", "Nombre de pila, edad, país y gustos", "No identifican dónde vives."),
        ("¿Qué datos no compartes con personas que no conoces?", "Dirección, teléfono y clave", "Son datos privados."),
        ("¿Qué puedes decir si te piden un dato privado?", "No, thank you, y aviso a un adulto", "Es una forma segura de decir que no."),
    ],
    [
        ("Completa: «My ___ is Ana.» (nombre)", "name", "Name es nombre."),
        ("Completa: «I'm ___ Chile.» (de)", "from", "From significa de, de origen."),
        ("Completa para decir que te gusta el helado: «I ___ ice cream.»", "like", "Like es gustar."),
    ],
    [
        ("Ana dice «I'm seven years». ¿Qué corriges para decir tengo siete años?", "Digo I'm seven, sin years", "En inglés se usa I'm más el número."),
        ("Un desconocido en un juego en línea te pide tu dirección. ¿Qué haces?", "No la doy y aviso a un adulto", "La dirección es un dato privado."),
    ],
    [
        ("Ordena para formar la pregunta: your / What's / name / ? Escribe la pregunta.", "What's your name?", "Es la pregunta para el nombre."),
        ("Responde a «Where are you from?» si eres de Chile. Escribe tres palabras en inglés.", "I'm from Chile", "Se usa I'm from y el país."),
    ],
    [("En la clase una niña nueva te pregunta «What's your name?». Te llamas Camila. Responde en inglés con una frase.", "My name is Camila", "Se usa My name is y tu nombre.")],
    [
        ("¿Cómo se dice «¿cuántos años tienes?» en inglés?", "How old are you?", "Es la pregunta de la edad."),
        ("¿Qué significa «Where are you from?»", "¿De dónde eres?", "Where es dónde y from es de."),
        ("¿Es seguro decir «I like pizza»?", "Sí", "Es un gusto, no un dato privado."),
    ],
    task("Con un adulto, juega a conocerse. El adulto pregunta: «What's your name?», «How old are you?», «Where are you from?», «What do you like?». Tú respondes con las frases del modelo: «My name is...», «I'm...», «I'm from Chile» y «I like...». Luego pregunta tú las mismas preguntas al adulto. Recuerda no decir dirección ni teléfono.", "«My name is Leo. I'm eight. I'm from Chile. I like pizza.»", ["responde las cuatro preguntas", "usa las frases del modelo", "pregunta al adulto", "no da datos privados"], ["nota del adulto"], ["decir I have seven years", "dar la dirección"], "Valora que cuidó sus datos y repite la pregunta que le costó."),
    "Di tu nombre y tu edad en inglés frente a un espejo.",
    "Escribe tres frases de tu presentación segura y léelas en voz alta a tu familia.",
)

lesson(
    OA12, 2,
    "Las frases y preguntas escritas en cada ejercicio, objetos pequeños de casa (lápices, fichas) hasta veinte y un adulto.",
    "Aprenderé a decir lo que puedo hacer con «I can» y a decir cantidades hasta veinte con «I have». Sirve para contar y hablar de habilidades en inglés.",
    ["Sé contar hasta veinte en español.", "Sé verbos como run, jump y swim."],
    [
        "Para decir una habilidad usa «I can» (yo puedo): «I can swim» (puedo nadar). Para decir que no puedes usa «I can't»: «I can't fly» (no puedo volar). Para preguntar: «Can you swim?» Respondes «Yes, I can» o «No, I can't».",
        "Para decir una cantidad usa «I have» y un número: «I have twelve pencils» (tengo doce lápices). Del uno al diez: one, two, three, four, five, six, seven, eight, nine, ten. Los números del once al veinte son: eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty. Para preguntar cuántos usa «How many...?»: «How many apples?» (¿cuántas manzanas?).",
        "Ten cuidado con los números: thirteen y thirty suenan parecido, pero thirteen es 13. Fíjate en el final: -teen (13 al 19). Para contar, toca cada objeto una sola vez. Y cuando respondas con un número, usa una frase completa: «There are fifteen» (hay quince).",
    ],
    [("I can", "yo puedo"), ("I can't", "yo no puedo"), ("Can you...?", "¿puedes...?"), ("How many?", "¿cuántos?"), ("eleven / twelve", "once / doce"), ("twenty", "veinte")],
    [
        ("Decir una habilidad", "Sabes nadar pero no volar. ¿Qué dices?", ["Para nadar uso I can swim.", "Para volar uso I can't fly.", "Junto las dos frases."], "I can swim. I can't fly."),
        ("Decir una cantidad", "Tienes 12 lápices. ¿Qué dices?", ["Uso I have.", "El doce es twelve.", "Agrego pencils."], "I have twelve pencils."),
    ],
    [
        ("Decir «I am can swim».", "Se mezclan am y can.", "Después de can va el verbo solo: I can swim."),
        ("Confundir thirteen con thirty.", "Suenan parecido.", "13 termina en -teen y 30 termina en -ty."),
    ],
    [
        ("¿Qué significa «I can't»?", "No puedo", "Es la forma negativa de I can."),
        ("¿Cómo se dice 12 en inglés?", "twelve", "Es el número después de eleven."),
        ("¿Qué significa «How many?»", "¿Cuántos?", "Se usa para preguntar cantidades."),
    ],
    [
        ("¿Qué palabra se usa para decir que no puedes?", "can't", "I can't significa no puedo."),
        ("¿Cómo respondes «Can you jump?» si puedes?", "Yes, I can", "Es la respuesta corta."),
        ("¿Qué terminación tienen los números del 13 al 19?", "-teen", "Es el final de esos números."),
    ],
    [
        ("Completa: «I ___ run.» (puedo)", "can", "I can run significa puedo correr."),
        ("Completa: «I have ___ apples.» (quince)", "fifteen", "Fifteen es quince."),
        ("Escribe en español la frase «I can't fly».", "No puedo volar", "Fly es volar y can't es no puedo."),
    ],
    [
        ("Alguien dice «I am can swim». ¿Cómo se corrige?", "I can swim", "Can no lleva am antes."),
        ("En una bolsa hay 18 fichas. Completa con el número en inglés: «There are ___ counters.»", "eighteen", "Eighteen es dieciocho."),
    ],
    [
        ("Cuenta las manzanas: ● ● ● ● ● ● ● ● ● ● ● ● ●. Escribe cuántas hay, en inglés.", "thirteen", "Son trece manzanas y 13 es thirteen."),
        ("Tienes 14 lápices y 5 gomas. ¿Cuántos objetos hay en total? Escribe el número en inglés.", "nineteen", "14 más 5 son 19, nineteen."),
    ],
    [("Un niño dice «I have twenty cars» y tú quieres preguntar cuántos autos son. ¿Qué preguntas en inglés? Usa How many.", "How many cars?", "Es la pregunta por la cantidad.")],
    [
        ("¿Cómo se dice 20 en inglés?", "twenty", "Es el número final de la serie."),
        ("¿Qué significa «Can you swim?»", "¿Puedes nadar?", "Can you es puedes."),
        ("Responde si no puedes volar: «No, I ___.»", "can't", "No, I can't."),
    ],
    task("Con un adulto, cuenta 20 objetos pequeños (por ejemplo lentejas o fichas de papel) en inglés, del uno al veinte. Después responde dos preguntas del adulto: «Can you swim?» y «Can you jump?» con una respuesta corta. Por último di en voz alta dos frases tuyas: «I can ___» y «I can't ___».", "«One, two, three... twenty. Yes, I can. I can swim. I can't fly.»", ["cuenta hasta twenty", "usa can y can't", "responde con respuesta corta", "dice cantidades con I have o There are"], ["nota del adulto"], ["saltarse un número", "decir I am can"], "Celebra los números bien dichos y repite thirteen y thirty."),
    "Cuenta tus dedos hasta veinte en inglés usando manos y pies.",
    "Escribe tres frases con I can y dos con I can't.",
)

lesson(
    OA12, 3,
    "Las frases y descripciones escritas en cada ejercicio, un adulto y, si quieres, un dibujo de tu escuela.",
    "Aprenderé a describir animales, comida, ocupaciones y lugares de la escuela, y a decir qué está prohibido. Sirve para hablar de lo que veo y de las reglas de la escuela en inglés.",
    ["Sé animales y comidas en inglés.", "Sé colores: red, blue, green, yellow, brown."],
    [
        "Para describir usa «It is» y una palabra: «It is big» (es grande), «It is small» (es pequeño), «It is brown» (es café). Para decir qué es: «It is a dog». Para describir comida: «The apple is red» (la manzana es roja). Para ocupaciones: «He is a doctor», «She is a teacher» (él es doctor, ella es profesora).",
        "Los lugares de la escuela son: classroom (sala), library (biblioteca), playground (patio de juegos), gym (gimnasio) y cafeteria (comedor). Se describen con «This is the library. It is quiet» (esta es la biblioteca; es tranquila). Quiet significa en silencio.",
        "Para decir que algo está prohibido usa «Don't» y un verbo: «Don't run!» (¡no corras!), «Don't shout!» (¡no grites!), «Don't push!» (¡no empujes!). Es una orden para cuidar a todos. Dilo con voz firme pero amable. En la biblioteca: «Don't shout in the library».",
    ],
    [("big / small", "grande / pequeño"), ("He is / She is", "él es / ella es"), ("library", "biblioteca"), ("Don't run!", "¡no corras!"), ("Don't shout!", "¡no grites!"), ("quiet", "en silencio, tranquilo")],
    [
        ("Describir un animal", "Un oso grande y café. ¿Qué dices?", ["Uso It is.", "Digo big.", "Digo brown."], "It is big and brown."),
        ("Decir una prohibición", "Un niño corre en la sala. ¿Qué dices?", ["Uso Don't.", "El verbo es run.", "Agrego un lugar si quiero."], "Don't run!"),
    ],
    [
        ("Decir «No run!» para prohibir.", "Se traduce palabra por palabra.", "Usa Don't y el verbo: Don't run!"),
        ("Decir «He is teacher» sin a.", "Se olvida el artículo.", "Se dice He is a teacher."),
    ],
    [
        ("¿Qué significa «Don't shout!»?", "¡No grites!", "Shout es gritar y don't es no."),
        ("¿Qué significa «library»?", "Biblioteca", "Es el lugar de los libros."),
        ("¿Qué significa «small»?", "Pequeño", "Es lo contrario de big."),
    ],
    [
        ("¿Qué dos palabras se usan para prohibir algo?", "Don't y un verbo", "Don't va delante del verbo."),
        ("¿Cómo describes un gato negro y pequeño?", "It is black and small", "Se usa It is y las dos características."),
        ("¿Para qué sirven las prohibiciones en la escuela?", "Para cuidar a todos", "Las reglas protegen."),
    ],
    [
        ("Completa: «She is a ___.» (profesora)", "teacher", "Teacher es profesora."),
        ("Completa: «Don't ___ in the library!» (gritar)", "shout", "Shout es gritar."),
        ("Completa: «The banana is ___.» (amarilla)", "yellow", "Yellow es amarillo."),
    ],
    [
        ("Tomás dice «He is teacher» para su profesor. ¿Qué palabra le falta?", "a", "Se dice He is a teacher."),
        ("Una niña dice «Don't running!». ¿Cómo se corrige?", "Don't run!", "Después de Don't va el verbo solo."),
    ],
    [
        ("Describe en inglés [un elefante grande y gris]: «It is ___ and gray.» (grande)", "big", "Big es grande."),
        ("Escribe la prohibición en inglés para el patio: [un niño empuja a otro]. Dos palabras.", "Don't push", "Push es empujar."),
    ],
    [("En el pasillo de la escuela alguien grita. ¿Qué le dices en inglés, amable, con dos palabras?", "Don't shout", "Se usa para pedir silencio.")],
    [
        ("¿Cómo se dice «comedor de la escuela» en inglés?", "cafeteria", "Es el lugar donde se come en la escuela."),
        ("¿Qué significa «playground»?", "Patio de juegos", "Es el lugar de recreo."),
        ("¿Cómo se dice «grande» en inglés?", "big", "Es lo contrario de small."),
    ],
    task("Con un adulto, haz tres descripciones: (1) un animal que elijas, por ejemplo un perro: «It is a dog. It is big. It is brown.» (2) una ocupación: «She is a teacher». (3) un lugar de tu escuela: «This is the library. It is quiet». Luego di dos prohibiciones: «Don't run!» y «Don't shout!».", "«It is a dog. It is big. It is brown. This is the library. Don't run!»", ["describe un animal", "dice una ocupación", "describe un lugar", "usa Don't"], ["nota del adulto"], ["olvidar a en ocupaciones", "decir Don't running"], "Valora la descripción y repite las prohibiciones con voz amable."),
    "Dibuja un animal de tu elección y escribe una frase con It is.",
    "Escribe tres reglas de tu sala en inglés con Don't.",
)

lesson(
    OA12, 4,
    "Las frases y preguntas escritas en cada ejercicio, algunos objetos de casa (una pelota, una caja, una mesa) y un adulto.",
    "Aprenderé a pedir información sobre comida y a decir dónde está un objeto. Sirve para preguntar y responder con palabras de lugar en inglés.",
    ["Sé nombres de comida y objetos.", "Sé que in significa dentro y on significa sobre."],
    [
        "Para preguntar por la comida usa «Do you like apples?» (¿te gustan las manzanas?). Respondes «Yes, I do» (sí) o «No, I don't» (no). También puedes preguntar «What's in the bag?» (¿qué hay en la bolsa?) y responder «An apple» (una manzana; delante de apple se usa an).",
        "Para saber dónde está algo usa «Where is the ball?» (¿dónde está la pelota?). Para responder usa palabras de lugar: in (dentro de), on (sobre), under (debajo de), next to (al lado de), behind (detrás de), in front of (delante de). Por ejemplo: «It's under the table» (está debajo de la mesa).",
        "Usa objetos reales para practicar. Pon una pelota sobre la mesa, bajo la mesa y en una caja, y di cada vez: «It's on the table», «It's under the table», «It's in the box». Mirar el objeto te ayuda a recordar la palabra de lugar.",
    ],
    [("Do you like...?", "¿te gusta...?"), ("Yes, I do / No, I don't", "sí / no"), ("Where is...?", "¿dónde está...?"), ("in / on / under", "dentro / sobre / debajo"), ("next to", "al lado de"), ("behind", "detrás de")],
    [
        ("Preguntar por comida", "Quieres saber si a tu amigo le gustan las manzanas. ¿Qué preguntas?", ["Uso Do you like.", "Digo apples.", "Cierro con signo de interrogación."], "Do you like apples?"),
        ("Decir dónde está", "La pelota está debajo de la mesa. ¿Qué respondes a «Where is the ball?»", ["Busco la palabra under.", "Digo it's under.", "Agrego the table."], "It's under the table."),
    ],
    [
        ("Responder «Yes, I like» a una pregunta con do.", "Se mezcla la forma.", "Responde Yes, I do."),
        ("Usar on cuando está dentro.", "Se confunden las palabras de lugar.", "Dentro es in; sobre es on."),
    ],
    [
        ("¿Qué significa «under»?", "Debajo de", "Indica abajo de algo."),
        ("¿Qué significa «Where is the ball?»", "¿Dónde está la pelota?", "Where es dónde."),
        ("¿Qué significa «Yes, I do»?", "Sí, me gusta", "Responde a Do you like...?"),
    ],
    [
        ("¿Qué palabra de lugar significa «sobre»?", "on", "On indica encima de algo."),
        ("¿Cómo respondes «Do you like pizza?» si no te gusta?", "No, I don't", "Es la respuesta negativa."),
        ("¿Cuál es la diferencia entre in y on?", "In es dentro y on es sobre", "Indican posiciones distintas."),
    ],
    [
        ("Completa: «The cat is ___ the box.» (dentro de)", "in", "In significa dentro de."),
        ("Completa: «The book is ___ the table.» (sobre)", "on", "On significa sobre."),
        ("Responde: «Do you like milk?» Tú sí. Escribe una respuesta corta.", "Yes, I do", "Do se repite en la respuesta."),
    ],
    [
        ("[La pelota está detrás de la silla.] Completa: «It's ___ the chair.»", "behind", "Behind significa detrás de."),
        ("Ana pregunta «What's in the bag?» y Leo responde «It's on the bag». ¿Qué palabra debe cambiar?", "on por in", "Si está dentro, se usa in."),
    ],
    [
        ("[El gato está al lado del perro.] Completa con dos palabras: «The cat is ___ the dog.»", "next to", "Next to es al lado de."),
        ("Pregunta: «Where is the apple?» [La manzana está en la caja.] Escribe la respuesta con It's.", "It's in the box", "In indica dentro."),
    ],
    [("Tu mamá pregunta «Where is the ball?» y la pelota está bajo la cama. Responde en inglés con cuatro palabras.", "It's under the bed", "Under es debajo de y bed es cama.")],
    [
        ("¿Cómo se dice «detrás de» en inglés?", "behind", "Es una palabra de lugar."),
        ("¿Qué significa «What's in the bag?»", "¿Qué hay en la bolsa?", "In the bag es dentro de la bolsa."),
        ("Escribe cómo preguntas si a alguien le gustan las bananas.", "Do you like bananas?", "Se usa Do you like."),
    ],
    task("Con un adulto, pon una pelota (u otro objeto) en seis lugares: sobre la mesa, bajo la mesa, dentro de una caja, al lado de la silla, detrás de la silla y delante de la silla. El adulto pregunta «Where is the ball?» y tú respondes con «It's ___ the ___». Después pregunta «Do you like apples?» y responde con Yes, I do o No, I don't.", "«It's on the table.» «It's in the box.» «Yes, I do.»", ["usa seis palabras de lugar", "responde con It's...", "responde la pregunta de gusto", "mira el objeto al hablar"], ["nota del adulto"], ["confundir in y on", "responder Yes, I like"], "Repite las palabras de lugar con él y mueve el objeto para reforzarlas."),
    "Pon un lápiz en tres lugares y di «It's ___ the ___» cada vez.",
    "Escribe una pregunta y su respuesta sobre un alimento y sobre un objeto.",
)

lesson(
    OA12, 5,
    "Las frases escritas en cada ejercicio, un adulto o familiar para hacer mímica y espacio libre para moverte con cuidado.",
    "Aprenderé a decir lo que alguien hace en este momento con «is» y la terminación -ing. Sirve para describir acciones que ocurren ahora.",
    ["Sé verbos básicos: run, eat, read, sleep.", "Sé decir He is y She is."],
    [
        "Para decir lo que pasa ahora usa «is» o «are» y un verbo con -ing. «She is reading» (ella está leyendo). «He is eating» (él está comiendo). «They are playing» (ellos están jugando). Para hablar de ti: «I'm drawing» (estoy dibujando).",
        "Para preguntar usa «What are you doing?» (¿qué estás haciendo?). Respondes «I'm reading». Para preguntar por otra persona: «What is he doing?» (¿qué está haciendo él?). Algunos verbos duplican la última letra: run se convierte en running, swim en swimming y sit en sitting. Si el verbo termina en e, como write (escribir), se quita la e: writing.",
        "Mira una imagen o haz mímica con un adulto para practicar. Si alguien está comiendo, dices «He is eating». Si dos niños corren, «They are running». Usa «is» con he, she e it, «are» con they, we y you, e «I'm» con yo.",
    ],
    [("I'm... -ing", "estoy haciendo"), ("He is / She is", "él / ella está"), ("They are", "ellos están"), ("reading", "leyendo"), ("eating", "comiendo"), ("What are you doing?", "¿qué estás haciendo?")],
    [
        ("Describir una acción", "[Una niña lee un libro.] ¿Qué dices?", ["Uso She is.", "El verbo es read.", "Le agrego -ing."], "She is reading."),
        ("Verbo que duplica", "[Dos niños corren.] ¿Qué dices?", ["Uso They are.", "Run se escribe running.", "Duplico la n."], "They are running."),
    ],
    [
        ("Decir «She reading» sin is.", "Se olvida el verbo auxiliar.", "Siempre is o are antes del verbo con -ing."),
        ("Escribir runing con una sola n.", "No se duplica la consonante.", "Run se escribe running."),
    ],
    [
        ("¿Qué significa «He is eating»?", "Él está comiendo", "Is eating es está comiendo."),
        ("¿Qué significa «What are you doing?»", "¿Qué estás haciendo?", "Pregunta por la acción ahora."),
        ("¿Qué terminación tienen los verbos que describen acciones ahora?", "-ing", "Se agrega al final del verbo."),
    ],
    [
        ("¿Cuándo usas «are»?", "Con they y we", "Con varias personas se usa are."),
        ("¿Cómo respondes «What are you doing?» si lees?", "I'm reading", "I'm más el verbo con -ing."),
        ("¿Cómo se escribe «swim» con -ing?", "swimming", "Se duplica la m."),
    ],
    [
        ("Completa: «She is ___.» (leyendo)", "reading", "Read más ing."),
        ("[Un niño bebe agua.] Completa: «He is ___ water.»", "drinking", "Drinking es bebiendo."),
        ("[Dos niñas juegan.] Completa: «They ___ playing.»", "are", "Con they se usa are."),
    ],
    [
        ("Marta dice «He eating a banana». ¿Qué palabra le falta?", "is", "Se necesita is."),
        ("Luis escribe «sitting» como «siting». ¿Qué letra falta?", "t", "Sit duplica la t."),
    ],
    [
        ("[Un gato duerme.] Escribe la oración completa con It is.", "It is sleeping", "Sleep más ing."),
        ("[Dos niños escriben en sus cuadernos.] Escribe la oración: They are ___. (verbo con -ing)", "writing", "Write pierde la e y recibe ing."),
    ],
    [("Estás en una videollamada con tu abuela y ella pregunta «What are you doing?». Estás dibujando. Responde en inglés.", "I'm drawing", "Draw más ing.")],
    [
        ("¿Cómo se dice «jugando» en inglés?", "playing", "Play más ing."),
        ("¿Qué significa «They are running»?", "Ellos están corriendo", "Running es corriendo."),
        ("¿Qué escribes antes del verbo con ing?", "is o are", "Es el verbo auxiliar."),
    ],
    task("Con un adulto, haz mímica de cinco acciones: reading, eating, drinking, sleeping y running. El adulto hace una mímica y pregunta «What is he doing?» o «What is she doing?» (puedes imaginar un personaje); tú respondes «He is reading» o «She is reading». Luego cambian: tú haces la mímica y el adulto responde. Al final, tú dices qué haces tú: «I'm ...».", "El adulto simula leer. Tú dices «He is reading». Luego, «I'm jumping».", ["usa is o are", "usa verbos con -ing", "reconoce las cinco acciones", "pregunta What are you doing?"], ["nota del adulto"], ["olvidar is", "escribir runing"], "Haz más mímica de las acciones que le costaron."),
    "Mira a alguien de tu casa y di en inglés lo que hace ahora.",
    "Escribe tres frases con -ing sobre lo que hacen tres personas de tu familia ahora.",
)
