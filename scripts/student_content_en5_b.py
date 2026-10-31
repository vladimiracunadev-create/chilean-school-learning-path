"""Cuaderno del estudiante, 5.º básico Inglés (propuesta): EN05 OA 11 (vocabulario temático, palabras frecuentes y expresiones del nivel).

Los textos en inglés son originales, muy breves y llevan pista en español. Cada palabra o estructura se enseña en la propia
clase antes de usarla. Sin audio externo: todo lo que hay que leer está escrito en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA11 = "EN05 OA 11"


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


# ================================================================ OA 11 clase 1: vocabulario temático (el día en la escuela)
lesson(
    OA11, 1,
    "Las listas de palabras y los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé palabras del tema «un día de escuela» y a elegir la palabra que calza con el propósito y el contexto de cada oración. Sirve para hablar y escribir sobre tu rutina en inglés.",
    ["Conozco palabras como school, breakfast y night.", "Sé que en inglés se puede hablar de lo que hago todos los días."],
    [
        "El vocabulario temático son palabras que pertenecen al mismo tema. Hoy el tema es «un día de escuela»: wake up (despertarse), brush my teeth (lavarme los dientes), have breakfast (tomar desayuno), go to school (ir a la escuela), do homework (hacer la tarea), have dinner (cenar) y go to bed (irme a la cama).",
        "También hay asignaturas (subjects): Math (Matemática), Science (Ciencias), Art (Artes), Music (Música) y English (Inglés). Para elegir bien una palabra, mira el propósito (para qué se dice) y el contexto (cuándo y dónde pasa). Una pista como «at night» (en la noche) te indica qué acción encaja.",
        "Varias palabras van juntas como un bloque: «have breakfast» no se separa. Aprende el bloque completo y no palabra por palabra. Con he, she o un nombre, have cambia a has: «Ana has breakfast». Cuando una palabra nueva aparezca, busca las pistas alrededor: la hora, el lugar o las otras palabras de la oración.",
    ],
    [("wake up", "despertarse"), ("brush my teeth", "lavarme los dientes"), ("have breakfast / dinner", "tomar desayuno / cenar"), ("do homework", "hacer la tarea"), ("go to bed", "irme a la cama"), ("subject", "asignatura"), ("Math / Science / Art / Music", "Matemática / Ciencias / Artes / Música")],
    [
        ("Elegir con la pista del contexto", "Completa: «At night, I ___.» Opciones: go to bed, have breakfast, go to school.", ["La pista es «at night» (en la noche).", "Have breakfast y go to school se hacen de día.", "De noche me voy a la cama."], "go to bed"),
        ("Encontrar la palabra que no calza", "En la lista «wake up, brush my teeth, have breakfast, have dinner», ¿qué acción NO es de la mañana?", ["Wake up, brush my teeth y have breakfast se hacen al comenzar el día.", "Dinner es la comida de la noche.", "Es la que no calza."], "have dinner"),
    ],
    [
        ("Traducir palabra por palabra «do homework» como «hacer casa».", "Se separa el bloque y se pierde el significado.", "Aprende el bloque completo: do homework significa hacer la tarea."),
        ("Elegir «have dinner» para la mañana.", "No se mira la pista de tiempo de la oración.", "Busca la pista: dinner es la comida de la noche."),
    ],
    [
        ("¿Qué significa «wake up»?", "Despertarse", "Wake up es dejar de dormir al comenzar el día."),
        ("¿Cómo se dice «hacer la tarea» en inglés?", "do homework", "Do homework es el bloque para hacer la tarea."),
        ("¿Qué significa «have dinner»?", "Cenar", "Dinner es la comida de la noche."),
    ],
    [
        ("Completa: «In the morning, I ___ my teeth.» Opciones: brush, drink, go.", "brush", "Brush my teeth es el bloque para lavarse los dientes."),
        ("¿Cuál de estas acciones se hace de noche: have breakfast, go to bed o go to school?", "go to bed", "Irse a la cama es la acción de la noche."),
        ("¿Qué asignatura es «Science»?", "Ciencias", "Science es la asignatura donde se estudia la naturaleza."),
    ],
    [
        ("Ordena estas acciones desde la mañana hasta la noche: go to bed, wake up, have dinner. Escríbelas separadas por comas.", "wake up, have dinner, go to bed", "Primero se despierta, luego se cena y al final se va a la cama."),
        ("Completa: «At 7:30, Ana ___ breakfast and then goes to school.» Opciones: has, sleeps, brushes.", "has", "Have breakfast es el bloque; con Ana se usa has."),
        ("Horario: «Monday: Math, Art. Tuesday: Science, Music.» (Monday = lunes, Tuesday = martes). ¿Qué día hay Music?", "Tuesday", "Music aparece en la línea de Tuesday."),
    ],
    [
        ("Tomás completó «I ___ dinner at night» con «wake up». ¿Por qué no calza?", "Porque wake up significa despertarse y no es una comida", "Después de dinner va un verbo de comer: have."),
        ("¿Cuál NO es una asignatura: Math, Art, brush my teeth, Music?", "brush my teeth", "Es una acción de rutina, no una asignatura."),
    ],
    [
        ("Texto: «I wake up at 7. I brush my teeth. I have breakfast. I go to school.» ¿Cuántas acciones de rutina hay?", "4", "Son wake up, brush my teeth, have breakfast y go to school."),
        ("¿Cuál oración tiene sentido? a) I brush my teeth in the morning and at night. b) I have breakfast at night and I wake up at dinner.", "a", "En la b las acciones no calzan con el momento del día."),
    ],
    [("Un compañero escribe en su diario: «Every day I do homework after school.» (every day = todos los días). ¿Qué hace después de la escuela?", "Hace la tarea", "Do homework significa hacer la tarea.")],
    [
        ("¿Qué significa «subject»?", "Asignatura", "Subject es cada ramo que se estudia en la escuela."),
        ("¿Qué pista de la oración «At night, I go to bed» te dice que es la noche?", "At night", "At night significa en la noche."),
        ("¿Qué significa «Music»?", "Música", "Music es la asignatura de la música."),
    ],
    task("Escribe en tu hoja una oración con cada una de estas tres palabras: wake up, do homework, go to bed. Usa estos modelos: «I wake up at 7.», «I do homework after school.», «I go to bed at 9.» Cambia la hora o el momento del día, y añade una asignatura (Math, Science, Art o Music).", "I wake up at 6. I do Math homework after school. I go to bed at 8.", ["usa las tres palabras con su bloque completo", "las acciones calzan con el momento del día", "incluye una asignatura"], ["hoja con tres oraciones"], ["separar el bloque, por ejemplo «do the homework» sin sentido", "poner una acción en un momento que no calza"], "Muestra la pista de tiempo que corresponde a cada acción y repasa con el estudiante los bloques completos."),
    "Dibuja tu día en cuatro cuadros y escribe debajo de cada uno: wake up, have breakfast, do homework, go to bed.",
    "Escribe tres oraciones sobre tu día con las asignaturas Art, Music y Science, por ejemplo «I like Music.».",
)

# ================================================================ OA 11 clase 2: palabras de uso frecuente
lesson(
    OA11, 2,
    "Los textos y las listas escritos en cada ejercicio, lápiz de dos colores o dos formas de subrayar.",
    "Aprenderé palabras que se usan muchísimo en inglés, como always, never, before y after, y a encontrar grupos de palabras (chunks) con sus pistas. Sirve para entender y escribir oraciones más completas.",
    ["Conozco el vocabulario de la rutina diaria.", "Sé que los verbos cambian un poco con he y she, por ejemplo has y wakes."],
    [
        "Las palabras de uso frecuente aparecen en casi todos los textos. Dicen cuántas veces o cuándo pasa algo: always (siempre), usually (por lo general), sometimes (a veces) y never (nunca). Ordenadas de más a menos veces: always, usually, sometimes, never.",
        "También ordenan el tiempo: before (antes de) y after (después de). En «I do homework before dinner», primero haces la tarea y después cenas. Otras palabras unen ideas: with (con) y because (porque). Con he, she o un nombre, el verbo lleva -s: «Lía wakes up», «Tomás plays».",
        "Un chunk es un grupo de palabras que siempre van juntas: every day (todos los días), after school (después de la escuela), in the morning (en la mañana), with my friends (con mis amigos). Para encontrar el sentido, ubica primero la palabra clave (key word) y luego el chunk que la acompaña.",
    ],
    [("always / usually", "siempre / por lo general"), ("sometimes / never", "a veces / nunca"), ("before / after", "antes de / después de"), ("every day", "todos los días"), ("with", "con"), ("chunk", "grupo de palabras que van juntas"), ("key word", "palabra clave")],
    [
        ("Ordenar por cuántas veces", "Ordena de más veces a menos veces: never, always, sometimes.", ["Always es todas las veces.", "Sometimes es algunas veces.", "Never es ninguna vez."], "always, sometimes, never"),
        ("Encontrar el chunk y la palabra clave", "En «I play with my friends after school», ¿qué chunk dice cuándo?", ["With my friends dice con quién.", "After school dice cuándo.", "El chunk de tiempo es after school."], "after school"),
    ],
    [
        ("Pensar que «never» significa «siempre».", "Se confunde con always, que también es una palabra de frecuencia.", "Never es nunca: ninguna vez. Always es siempre."),
        ("Entender «before dinner» como «después de la cena».", "Se confunden before y after.", "Before es antes de y after es después de."),
    ],
    [
        ("¿Qué significa «never»?", "Nunca", "Never indica que algo no pasa ninguna vez."),
        ("¿Cuál palabra significa «siempre»: always o sometimes?", "always", "Always es todas las veces."),
        ("¿Qué significa «after school»?", "Después de la escuela", "After es después de."),
    ],
    [
        ("En «I always brush my teeth», ¿qué palabra dice cuántas veces?", "always", "Always es la palabra de frecuencia de esa oración."),
        ("En «I play with my friends after school», ¿qué chunk dice con quién?", "with my friends", "With significa con y my friends son mis amigos."),
        ("Ordena de menos a más veces: always, never, sometimes.", "never, sometimes, always", "Nunca es cero, a veces es algunas y siempre es todas."),
    ],
    [
        ("Sofía come fruta todos los días. ¿Qué palabra elige para «Sofía ___ eats fruit»: always o never?", "always", "Todos los días es siempre."),
        ("«I do homework before dinner.» ¿Qué hago primero: la tarea o la cena?", "La tarea", "Before dinner significa antes de la cena."),
        ("«I brush my teeth after breakfast.» ¿Qué hago primero: desayunar o lavarme los dientes?", "Desayunar", "After breakfast significa después del desayuno."),
    ],
    [
        ("Pedro escribe «I never go to school on Saturday» (Saturday = sábado). ¿Va a la escuela los sábados?", "No", "Never significa ninguna vez."),
        ("¿Qué oración tiene el mismo sentido que «I do homework after dinner»? a) I have dinner and then I do homework. b) I do homework and then I have dinner.", "a", "After dinner indica que la cena va primero."),
    ],
    [
        ("Texto: «Lía always wakes up at 7. She sometimes has juice. She is never late.» (late = tarde, juice = jugo). ¿Cuántas palabras de frecuencia hay?", "3", "Son always, sometimes y never."),
        ("«Tomás plays soccer every day.» ¿Qué palabra de frecuencia se parece más en sentido a every day: never o always?", "always", "Todos los días equivale a siempre."),
    ],
    [("En el recreo, Camila dice: «I usually play with my friends in the morning.» ¿Con quién juega y cuándo?", "Con sus amigos, en la mañana", "With my friends dice con quién e in the morning dice cuándo.")],
    [
        ("¿Qué significa «sometimes»?", "A veces", "Sometimes indica algunas veces."),
        ("¿Qué significa «before»?", "Antes de", "Before va antes de lo que se nombra."),
        ("¿Qué es un chunk?", "Un grupo de palabras que van juntas", "Se aprende completo, como every day."),
    ],
    task("Lee este modelo: «I always wake up at 7. I sometimes have juice. I never go to bed late.» (juice = jugo). Escribe en tu hoja tres oraciones tuyas con always, sometimes y never. Luego subraya con un color la palabra de frecuencia y con otro el chunk de tiempo, como every day o after school.", "I always brush my teeth. I sometimes play after school. I never eat breakfast at night.", ["usa las tres palabras de frecuencia", "las oraciones son verdaderas para ti", "subraya la palabra clave y el chunk"], ["hoja con tres oraciones subrayadas"], ["poner always y never al revés", "olvidar el verbo"], "Pide que lea las tres oraciones y que explique con sus palabras cuántas veces ocurre cada una."),
    "Haz una tabla con dos columnas, «Before dinner» y «After dinner», y escribe dos cosas que haces en cada una.",
    "Escribe una oración con before y otra con after sobre lo que haces los fines de semana.",
)

# ================================================================ OA 11 clase 3: expresiones de uso común
lesson(
    OA11, 3,
    "Las situaciones escritas en cada ejercicio, lápiz y papel.",
    "Aprenderé expresiones de uso común, como It's time to go o It's late, y cuándo usarlas. Sirve para reaccionar en inglés en situaciones reales del colegio.",
    ["Conozco el vocabulario de la rutina y las palabras before y after.", "Sé que una oración en inglés lleva sujeto y verbo."],
    [
        "Una expresión de uso común es una frase hecha que se usa siempre igual en cierta situación. No se traduce palabra por palabra. «It's time to go» significa «es hora de irse»; «It's late» significa «es tarde»; «It's early» significa «es temprano».",
        "Otras expresiones útiles: «It's time for lunch» (es hora de almuerzo), «Hurry up!» (¡apúrate!), «Wait for me» (espérame), «Let's go!» (¡vamos!), «I'm sorry, I'm late» (perdón, llegué tarde), «See you tomorrow» (hasta mañana) y «Excuse me» (disculpa, permiso).",
        "Para saber cuál usar, mira el propósito (qué quieres lograr) y el contexto (dónde estás y qué pasa). Si la clase empezó hace diez minutos y llegas, dices «I'm sorry, I'm late». Si suena el timbre del final del día, dices «See you tomorrow».",
    ],
    [("It's time to go.", "Es hora de irse."), ("It's late. / It's early.", "Es tarde. / Es temprano."), ("It's time for lunch.", "Es hora de almuerzo."), ("Hurry up!", "¡Apúrate!"), ("Wait for me.", "Espérame."), ("I'm sorry, I'm late.", "Perdón, llegué tarde."), ("See you tomorrow.", "Hasta mañana.")],
    [
        ("Elegir la expresión de la situación", "Suena el timbre del final de clases. ¿Qué dices al despedirte de tu amigo? Opciones: Hurry up!, See you tomorrow, It's early.", ["El timbre del final indica que se termina el día.", "Se necesita una despedida.", "See you tomorrow es hasta mañana."], "See you tomorrow"),
        ("Reconocer el propósito", "Tu amiga camina muy lento y la clase ya empezó. ¿Qué le dices? Opciones: Wait for me, Hurry up!, See you tomorrow.", ["El propósito es que ella vaya más rápido.", "Wait for me pide esperar.", "Hurry up pide apurarse."], "Hurry up!"),
    ],
    [
        ("Traducir «It's time to go» como «Es tiempo de ir».", "Se traduce palabra por palabra y suena extraño.", "Aprende la expresión completa: Es hora de irse."),
        ("Decir «See you tomorrow» al llegar atrasado a la clase.", "No se mira el propósito: esa expresión es una despedida.", "Al llegar tarde se dice I'm sorry, I'm late."),
    ],
    [
        ("¿Qué significa «It's late»?", "Es tarde", "Late es tarde."),
        ("¿Qué significa «Hurry up!»?", "¡Apúrate!", "Se dice para pedir que alguien vaya más rápido."),
        ("¿Cómo se dice «Hasta mañana» en inglés?", "See you tomorrow", "Es la despedida para volver a verse mañana."),
    ],
    [
        ("Son las doce y todos tienen hambre. ¿Qué expresión calza: It's time for lunch o It's early?", "It's time for lunch", "Lunch es el almuerzo y a mediodía es la hora de comer."),
        ("Llegas diez minutos después del inicio de la clase. ¿Qué dices a tu profesora?", "I'm sorry, I'm late", "Es la disculpa por llegar tarde."),
        ("¿Qué expresión se usa para pedir que alguien no se vaya sin ti?", "Wait for me", "Wait for me significa espérame."),
    ],
    [
        ("Un amigo grita «Wait for me!» y tú ya estás en la puerta. ¿Qué te pide?", "Que lo esperes", "Wait for me significa espérame."),
        ("Es hora de partir al patio. ¿Qué expresión usas: It's time to go o It's early?", "It's time to go", "Time to go es hora de irse."),
        ("¿Qué expresión invita a ir juntos a un lugar: Let's go! o Excuse me?", "Let's go!", "Let's go es vamos."),
    ],
    [
        ("El bus escolar sale a las 8 y ya son las 8:05. ¿Qué expresión calza mejor: It's early o It's late?", "It's late", "Ya pasó la hora de salida."),
        ("Son las 5 de la mañana y todos duermen. ¿Calza «It's late»?", "No, calza It's early", "A las 5 de la mañana es temprano."),
    ],
    [
        ("Diálogo: «A: It's time to go. B: Wait for me!» (time to go = hora de irse). ¿Quién quiere que lo esperen?", "B", "B dice Wait for me, es decir, espérame."),
        ("Diálogo: «A: Excuse me. B: Yes?» ¿Para qué usa A la expresión «Excuse me»?", "Para pedir permiso o llamar la atención con cortesía", "Excuse me se dice para hablar con alguien o pasar entre otras personas."),
    ],
    [("Camila y Andrés están jugando y suena el timbre del final de la hora de almuerzo. Camila dice: «It's time to go!». ¿Qué quiere decir?", "Que es hora de irse", "Time to go es hora de irse.")],
    [
        ("¿Qué significa «It's early»?", "Es temprano", "Early es lo contrario de late."),
        ("¿Se traducen las expresiones palabra por palabra?", "No", "Se aprenden completas porque cada una tiene un significado propio."),
        ("¿Qué significa «Let's go!»?", "¡Vamos!", "Let's go invita a ir juntos."),
    ],
    task("Lee estas tres situaciones: (1) llegas atrasado a la clase de Art; (2) termina el día y te despides de tu curso; (3) tu amiga demora en guardar sus cosas y el bus ya llegó. Escribe en tu hoja la expresión en inglés para cada una (usa las de esta clase) y una oración nueva con It's late o It's early.", "(1) I'm sorry, I'm late. (2) See you tomorrow. (3) Hurry up! Nueva oración: It's early. I want to sleep.", ["elige la expresión que calza con cada situación", "escribe las expresiones completas", "forma una oración nueva con late o early"], ["hoja con tres expresiones y una oración"], ["traducir palabra por palabra", "mezclar la despedida con la disculpa"], "Elogia la expresión correcta y pide que explique cuál era el propósito de cada situación."),
    "Escribe en tarjetas cuatro expresiones de esta clase y, atrás de cada una, la situación en que se usa.",
    "Inventa un diálogo de dos líneas entre amigos en que uno diga «It's time to go» y el otro «Wait for me».",
)

# ================================================================ OA 11 clase 4: usar el vocabulario junto
lesson(
    OA11, 4,
    "Las palabras y los mensajes escritos en cada ejercicio, lápiz y hoja.",
    "Aprenderé a combinar vocabulario temático, palabras frecuentes y expresiones para armar un mensaje corto con sentido. Sirve para escribir y decir mensajes propios en inglés, con apoyo.",
    ["Conozco el vocabulario del día de escuela, always, never, before, after y It's time to go.", "Sé armar oraciones cortas con sujeto y verbo."],
    [
        "Para armar un mensaje elige tres cosas: una palabra del tema (como do homework), una palabra frecuente (como always o after) y, si hace falta, una expresión (como It's time to go o See you tomorrow). Cada una cumple un trabajo distinto en el mensaje.",
        "El orden importa. La palabra de frecuencia va antes del verbo: «I always brush my teeth». Los chunks de tiempo pueden ir al final: «I do homework after school». En una oración con he o she, el verbo cambia un poco: «She has breakfast». Do cambia a does: «She does homework».",
        "Cuando termines, revisa (revision) tu mensaje: ¿se entiende?, ¿cada palabra calza con la situación?, ¿empieza con mayúscula y termina con punto? Corregir y volver a leer es parte de escribir bien.",
    ],
    [("message", "mensaje"), ("revision", "revisión: volver a leer y corregir"), ("I always brush my teeth.", "Siempre me lavo los dientes."), ("She has breakfast.", "Ella toma desayuno."), ("See you tomorrow.", "Hasta mañana."), ("It's time to go.", "Es hora de irse.")],
    [
        ("Armar una oración con las palabras desordenadas", "Ordena para formar una oración que comience con I: homework / do / I / school / after.", ["Busco el sujeto I y el verbo do.", "Do homework es un bloque.", "After school va al final."], "I do homework after school"),
        ("Elegir la palabra que falta", "Completa: «He ___ breakfast at 7.» Opciones: have, has, haves.", ["El sujeto es He.", "Con he, have cambia.", "La forma correcta es has."], "has"),
    ],
    [
        ("Escribir «I brush always my teeth» con always en cualquier lugar.", "No se respeta el lugar de la palabra de frecuencia.", "Escribe I always brush my teeth: always va antes del verbo."),
        ("Escribir «He have breakfast».", "Con he o she, el verbo have cambia.", "Escribe He has breakfast."),
    ],
    [
        ("¿Dónde va always en «I ___ brush my teeth»: antes del verbo o al final?", "Antes del verbo", "La palabra de frecuencia va antes del verbo."),
        ("¿Cuál es la forma correcta con she: have o has?", "has", "Con he, she e it se usa has."),
        ("¿Qué expresión significa «Es hora de irse»?", "It's time to go", "Es la frase hecha para decir que hay que partir."),
    ],
    [
        ("Ordena para formar una oración que comience con She: breakfast / has / She / sometimes.", "She sometimes has breakfast", "El adverbio va antes del verbo has."),
        ("Completa con after: «I play ___ school.»", "after", "After school es un chunk de tiempo: después de la escuela."),
        ("Mensaje: «It's late. ___ Bye!» ¿Qué completa mejor: See you tomorrow o Wait for me?", "See you tomorrow", "Es una despedida que cierra el mensaje."),
    ],
    [
        ("Completa con has o have: «My brother ___ homework at 4.»", "has", "Con my brother (él) se usa has."),
        ("En «They ___ go to bed late» pones never. ¿Va antes o después de go?", "Antes", "La palabra de frecuencia va antes del verbo."),
        ("Une las ideas con and: «I brush my teeth.» «I go to bed.» ¿Qué oración queda bien? a) I brush my teeth and I go to bed. b) I brush my teeth and go I to bed.", "a", "And une las dos oraciones y mantiene el orden I go."),
    ],
    [
        ("¿Cuál oración está bien escrita? a) I never do homework late. b) I do never homework late.", "a", "La palabra de frecuencia va antes del verbo."),
        ("Ana revisa su mensaje: «he plays soccer after school» y le falta algo en la primera palabra y al final. ¿Qué le faltaba?", "Una mayúscula en He y un punto final", "Una oración comienza con mayúscula y termina con punto."),
    ],
    [
        ("Mensaje: «Hi Sofía! I always do homework after school. Today it's late. See you tomorrow!». ¿Qué palabra frecuente usa el mensaje?", "always", "Always es la palabra de frecuencia."),
        ("En el mismo mensaje, ¿qué expresión de despedida aparece?", "See you tomorrow", "Es la frase que cierra el mensaje."),
    ],
    [("Para recordar la rutina, Lucas escribe en un papel pegado al refrigerador: «I always brush my teeth after dinner. Then I go to bed.» ¿Qué hace después de lavarse los dientes?", "Se va a la cama", "Then I go to bed señala lo que viene después.")],
    [
        ("¿Qué revisas al terminar de escribir un mensaje?", "Que se entienda, que cada palabra calce y que lleve mayúscula y punto", "Revisar es volver a leer y corregir."),
        ("¿Cómo se completa «She ___ homework after school»? Opciones: do, does.", "does", "Con she, el verbo do cambia a does."),
        ("¿Dónde va sometimes en «I ___ play after school»?", "Antes del verbo", "Sometimes va antes de play."),
    ],
    task("Escribe un mensaje de cuatro líneas para un amigo o amiga que incluya: una acción de tu día (por ejemplo, do homework), una palabra de frecuencia (always, sometimes o never), un chunk de tiempo (after school, every day) y una expresión (It's late o See you tomorrow). Modelo: «Hi Pedro! I always do homework after school. It's late now. See you tomorrow!»", "Hi Ana! I sometimes play after school. I always brush my teeth every day. It's time to go. See you tomorrow!", ["incluye las cuatro cosas pedidas", "cada palabra calza con la situación", "tiene mayúsculas y puntos"], ["hoja con el mensaje de cuatro líneas"], ["poner la palabra de frecuencia después del verbo", "olvidar la mayúscula o el punto"], "Marca con un visto cada elemento logrado y pide que revise solo una cosa: mayúscula y punto."),
    "Pide a una persona de tu casa que te diga una hora del día y di en inglés una acción que haces a esa hora.",
    "Escribe un segundo mensaje, ahora de la tarde, con otra expresión del nivel, como Hurry up! o Wait for me.",
)
