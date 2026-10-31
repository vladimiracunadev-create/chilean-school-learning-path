"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR04 (escribir oraciones y textos breves en lengua indígena o en castellano, incorporando conceptos o expresiones en
la lengua, en situaciones como ceremonias, rogativas y salidas a terreno) y OA LR05 (explicar el sentido de la
revitalización y/o fortalecimiento de la lengua, reconociendo neologismos y préstamos lingüísticos).

Criterio de autoría: todas las fichas, comunidades, escuelas, talleres y personas son inventadas solo para practicar y
están rotuladas como tales; no describen lo que hace ningún pueblo real. Las únicas expresiones en lengua indígena son
saludos y agradecimientos muy atestiguados (mari mari y chaltumay en mapuzugun; iorana y maururu en rapa nui) y los
nombres de las lenguas. No se inventa gramática, pronunciación ni significados rituales. Las ceremonias y rogativas
solo se mencionan como situaciones en las que se escribe una invitación o un agradecimiento; nunca se describe lo que
ocurre en su interior. Cada tarea abierta remite al educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LR4 = "LC06 OA LR04"
LR5 = "LC06 OA LR05"

CONSULT = " Recuerda: cómo se usa, se escribe y se dice la lengua en tu comunidad lo enseñan el educador o la educadora tradicional y las personas de tu comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. Nunca evaluar la identidad ni el origen de un estudiante."


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement + CONSULT, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback + FEEDBACK_ADD}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ============================================================ LR04 clase 1 · situar la situación de escritura
SA = "Situación A (inventada para practicar): el curso visitará el taller de tejido de la Comunidad Ejemplo, del pueblo mapuche. La educadora tradicional recibirá al curso y pidió una tarjeta de agradecimiento escrita, sin fotos de las personas."
SB = "Situación B (inventada): la Escuela Ejemplo quiere invitar a las familias a una ceremonia abierta organizada por una comunidad rapa nui. Los organizadores piden una invitación breve y avisan que lo que ocurre dentro de la ceremonia lo cuentan solo ellos."
SC = "Situación C (inventada): un curso quiere escribir un cartel para su sala con el saludo «mari mari». El educador tradicional de la escuela autorizó ese saludo, pero pidió que no se agreguen otras frases en la lengua que él no haya revisado."

L(
    LR4, 1,
    materials="Lápiz y hoja. Las tres situaciones están escritas aquí y son inventadas para practicar. No necesitas ningún dispositivo.",
    use="Aprenderé a mirar la situación en que voy a escribir (una ceremonia, una rogativa o una salida a terreno) y a decidir qué texto corresponde, a quién va dirigido y qué expresiones en lengua indígena puedo incluir con permiso.",
    prior=["Sé que cada pueblo tiene su propia lengua, como el mapuzugun del pueblo mapuche.", "Sé que una información sobre una comunidad necesita una fuente y un permiso."],
    explain=[
        "Un texto breve nace de una situación comunicativa. Para entenderla me hago cuatro preguntas: ¿quién escribe?, ¿a quién le escribe?, ¿para qué? y ¿dónde y cuándo se leerá? Una salida a terreno es una visita a un lugar o a una comunidad para aprender allí. Una ceremonia es un encuentro con un sentido cultural o espiritual. Una rogativa es una ceremonia de petición.",
        "Si quiero incluir una expresión en lengua indígena, ubico su pueblo y su fuente. «Mari mari» es un saludo en mapuzugun, la lengua del pueblo mapuche. La escribo solo si una fuente, como el educador o la educadora tradicional, me la entregó y me dio permiso. No uso en un texto para un pueblo una expresión de otro pueblo.",
        "Hay textos que sí puedo escribir, como una invitación, un agradecimiento o un cartel de bienvenida. Lo que se dice o se hace dentro de una ceremonia o de una rogativa lo cuentan solo quienes la conducen: yo no lo invento ni lo describo. Si un dato me falta, lo anoto como «por preguntar» y me detengo.",
    ],
    vocab=[("situación comunicativa", "el quién, a quién, para qué y dónde de un texto"), ("salida a terreno", "visita a un lugar o comunidad para aprender allí"), ("rogativa", "ceremonia de petición"), ("destinatario", "persona a quien va dirigido un texto"), ("mapuzugun", "lengua del pueblo mapuche")],
    worked=[
        W("Responder las cuatro preguntas", SA + " ¿Quién escribe, a quién y para qué?", ["Quien escribe es el curso que visitará el taller.", "Le escribe a la educadora tradicional que lo recibirá.", "El propósito es agradecer la visita."], "el curso escribe a la educadora tradicional para agradecer"),
        W("Decidir qué no se escribe", SB + " ¿Puede la invitación explicar lo que ocurre dentro de la ceremonia?", ["Releo el aviso de los organizadores.", "Dicen que eso lo cuentan solo ellos.", "La invitación solo debe invitar: día, lugar y bienvenida."], "no: eso lo cuentan solo los organizadores"),
    ],
    mistakes=[
        M("Escribir en la invitación cómo es la ceremonia por dentro.", "Lo que ocurre dentro lo cuentan quienes la conducen; yo no lo sé ni debo inventarlo.", "Escribo solo la invitación: quién invita, a quién, dónde y cuándo."),
        M("Agregar una frase en lengua indígena vista en un cartel sin saber de qué pueblo es.", "Puede ser de otro pueblo o estar mal escrita.", "Uso solo expresiones que una fuente me entregó y permitió usar."),
    ],
    R=[
        ex(SA + " ¿A quién va dirigida la tarjeta de la situación A?", "a la educadora tradicional de la Comunidad Ejemplo", "Ella recibirá al curso y pidió la tarjeta."),
        ex(SB + " ¿Qué piden los organizadores: una invitación breve o un informe largo?", "una invitación breve", "Así lo dice la situación B."),
        ex("Una rogativa, ¿es una ceremonia de petición o una fiesta de cumpleaños?", "una ceremonia de petición", "Así se definió en esta clase."),
    ],
    C=[
        ex(SC + " ¿Quién autorizó el saludo «mari mari» en la situación C?", "el educador tradicional de la escuela", "La situación C nombra a quien dio el permiso."),
        ex(SB + " ¿Quiénes pueden contar lo que ocurre dentro de la ceremonia: los organizadores o el curso que escribe la invitación?", "los organizadores", "Ellos mismos lo avisaron."),
        ex("Verdadero o falso: basta haber visto una expresión en un cartel para escribirla en un texto, aunque no se sepa de qué pueblo es.", "Falso", "Hay que conocer pueblo, fuente y permiso."),
    ],
    A=[
        ex(SA + " Ordena los pasos para preparar la tarjeta. A) escribir el borrador. B) responder quién, a quién, para qué y dónde. C) pedir a la educadora que revise lo que dice. Escribe las letras en orden.", "B, A, C", "Primero entiendo la situación, luego escribo y al final se revisa con quien sabe."),
        ex(SC + " Un estudiante quiere agregar al cartel otra frase en la lengua que vio en un video. ¿Puede hacerlo sin consultar al educador? Sí o No.", "No", "El educador pidió que no se agregue ninguna frase que él no haya revisado."),
        arith(SA + " El curso decide que la tarjeta tenga como máximo 6 oraciones. Ya escribió 3 en la primera hoja y 2 en la segunda. ¿Cuántas oraciones más puede agregar?", "6-3-2", "Se restan las ya escritas del máximo."),
    ],
    Z=[
        ex(SB + " Elige la oración que sí corresponde a la invitación. A) «Las familias están invitadas a llegar puntualmente a la ceremonia abierta». B) «Dentro de la ceremonia ocurren estos pasos, que explicamos uno por uno». Escribe la letra.", "A", "La B describe el interior de la ceremonia, que no corresponde al curso."),
        ex(SA + " Un compañero escribe la tarjeta como un aviso para todo el curso, sin nombrar a la educadora. ¿Qué pregunta de las cuatro responde mal: quién escribe, a quién le escribe, para qué o dónde se leerá?", "a quién le escribe", "El texto debe dirigirse a la educadora."),
    ],
    D=[
        ex(SB + " " + SC + " Un curso quiere usar el permiso del educador de la situación C para escribir una expresión rapa nui en la invitación de la situación B. ¿Sirve ese permiso? Sí o No.", "No", "El permiso de una fuente vale para su pueblo y su expresión, no para la de otro pueblo."),
        arith("En un curso de 25 estudiantes, 19 entregaron su ficha con las cuatro respuestas de la situación comunicativa completas. ¿Cuántos estudiantes todavía no la completan?", "25-19", "Se restan los que entregaron del total del curso."),
    ],
    context=[ex("Tu curso irá a una feria de artesanía de una comunidad y quieres escribir un agradecimiento. ¿Qué haces primero: responder quién, a quién, para qué y dónde, o buscar en internet una frase en lengua para decorar el texto?", "responder quién, a quién, para qué y dónde", "Primero se entiende la situación; las expresiones en lengua vienen de una fuente con permiso.")],
    selfcheck=[
        ex("¿Qué pregunta busca saber a quién va dirigido el texto: «para qué» o «a quién»?", "a quién", "Esa pregunta nombra al destinatario."),
        ex("Si me falta un dato sobre la ceremonia, ¿lo invento o lo anoto como «por preguntar»?", "lo anoto como «por preguntar»", "No se inventa lo que no se sabe."),
        ex("¿«Mari mari» es un saludo en mapuzugun o en rapa nui?", "en mapuzugun", "Es un saludo de la lengua del pueblo mapuche."),
    ],
    task=T(
        "Lee esta situación inventada: «La Escuela Ejemplo visitará la feria de lana de la Comunidad Muestra, del pueblo mapuche. Una artesana recibirá al curso y autorizó que se la salude con «mari mari» en una tarjeta. No autorizó fotos ni que se cuente lo que conversen en la feria.» En tu cuaderno responde las cuatro preguntas (quién escribe, a quién, para qué, dónde y cuándo se leerá) y escribe dos oraciones de la tarjeta, una con el saludo «mari mari» y otra que agradezca sin contar nada que no esté autorizado.",
        "Quién escribe: el curso. A quién: a la artesana. Para qué: agradecer su recibimiento. Dónde: se entregará en la feria. Oraciones: «Mari mari, estimada artesana.» «Gracias por recibir a nuestro curso en la feria.»",
        ["responde las cuatro preguntas", "usa «mari mari» como la fuente lo autorizó", "no agrega frases en lengua que no se entregaron", "no cuenta nada que no esté autorizado"],
        ["cuatro respuestas escritas", "dos oraciones de la tarjeta"],
        ["agregar frases en la lengua que no se entregaron", "contar la conversación de la feria"],
        "Pide que muestre en la situación escrita el dato que autoriza cada cosa que incluyó; lo que no tenga respaldo se saca.",
    ),
    reinforce="Vuelve a leer las situaciones A, B y C y subraya con colores distintos quién escribe y a quién.",
    extend="Escribe tu propia situación inventada de salida a terreno con las cuatro preguntas respondidas, y marca qué cosas no se podrían escribir.",
)

# ============================================================ LR04 clase 2 · leer un modelo con límites
TM = "Tarjeta modelo (inventada para practicar): «Querida educadora Ejemplo: mari mari. Hoy nuestro curso visitó su taller de tejido y aprendimos cómo se prepara la lana. Chaltumay por recibirnos. Cuando volvamos a clases, contaremos a las familias solo lo que usted nos autorizó contar. Curso 6.º A, Escuela Ejemplo.»"

L(
    LR4, 2,
    materials="Lápiz y hoja. La tarjeta modelo está escrita aquí y es inventada para practicar. Puede leerla en voz alta una persona adulta.",
    use="Aprenderé a leer un texto modelo para ver sus partes, encontrar las expresiones en lengua indígena y reconocer qué límites respeta. Sirve para escribir mis propios textos breves sin inventar nada.",
    prior=["Sé responder quién escribe, a quién, para qué y dónde.", "Sé que «mari mari» es un saludo en mapuzugun."],
    explain=[
        "Un buen modelo se lee con lápiz en la mano. Primero marco las partes del texto: saludo, qué se hizo, agradecimiento, compromiso y firma. Luego subrayo las expresiones en lengua indígena. «Mari mari» es un saludo en mapuzugun y «chaltumay» es una forma de agradecer, también en mapuzugun. Las copio siempre tal como las entregó la fuente.",
        "Después busco los límites. Un límite es una frase que avisa hasta dónde se cuenta o se puede decir algo. En la tarjeta modelo el curso promete contar a las familias solo lo que la educadora autorizó. Eso protege lo que pertenece a la comunidad. Un texto bien escrito dice lo que vivió el curso, pero no cuenta lo que no le corresponde contar.",
        "Por último separo lo que el texto afirma de lo que yo imagino. La tarjeta dice que el curso aprendió cómo se prepara la lana, pero no explica los pasos. Entonces yo no puedo agregar pasos inventados al leerla. Si una palabra o una frase en lengua me genera dudas, no adivino: lo anoto para preguntárselo al educador o a la educadora tradicional.",
    ],
    vocab=[("parte del texto", "cada bloque con una función, como el saludo o la firma"), ("expresión", "frase o palabra breve que se usa en una situación"), ("límite", "aviso de hasta dónde se cuenta o se puede decir algo"), ("compromiso", "promesa de hacer algo"), ("chaltumay", "forma de agradecer en mapuzugun")],
    worked=[
        W("Encontrar las expresiones en lengua", TM + " ¿Cuántas expresiones en lengua indígena tiene la tarjeta y cuáles son?", ["Busco palabras que no sean castellano.", "Encuentro «mari mari» y «chaltumay».", "Son dos."], "dos: mari mari y chaltumay"),
        W("Reconocer el límite", TM + " ¿Qué límite respeta el curso?", ["Busco la frase que promete algo sobre lo que se contará.", "Dice que contarán solo lo que la educadora autorizó.", "Ese es el límite."], "contar solo lo que la educadora autorizó contar"),
    ],
    mistakes=[
        M("Copiar «chaltumay» con otra escritura para que «se vea más bonita».", "Cambiar la escritura puede alterar la palabra que entregó la fuente.", "La copio igual que como la entregó la fuente."),
        M("Leer la tarjeta y agregar los pasos del tejido que «seguro» se hicieron.", "El texto no los dice y yo no los sé.", "Me quedo con lo que dice el texto y anoto mis dudas para preguntar."),
    ],
    R=[
        ex(TM + " ¿Cuál es el saludo en lengua indígena de la tarjeta modelo?", "mari mari", "Aparece al comienzo, después de «Querida educadora Ejemplo»."),
        ex(TM + " ¿Qué visitó el curso: un taller de tejido o una radio?", "un taller de tejido", "La segunda oración lo dice."),
        ex(TM + " ¿Con qué expresión en lengua se agradece en la tarjeta?", "chaltumay", "Está antes de «por recibirnos»."),
    ],
    C=[
        ex(TM + " ¿Qué promete el curso a las familias: contar todo lo que vio o contar solo lo que la educadora autorizó?", "contar solo lo que la educadora autorizó", "Es el compromiso que expresa el límite."),
        ex(TM + " Verdadero o falso: la tarjeta explica paso a paso cómo se prepara la lana.", "Falso", "Solo dice que el curso aprendió cómo se prepara; no da los pasos."),
        ex(TM + " ¿Quién firma la tarjeta: el curso 6.º A de la Escuela Ejemplo o la educadora?", "el curso 6.º A de la Escuela Ejemplo", "La firma está al final del texto."),
    ],
    A=[
        ex("Ordena las partes de la tarjeta modelo. A) firma. B) saludo. C) agradecimiento. D) compromiso de contar solo lo autorizado. E) lo que se hizo en la visita. Escribe las letras en orden.", "B, E, C, D, A", "El modelo saluda, cuenta la visita, agradece, promete y firma."),
        arith("Tres cursos escribieron tarjetas iguales a la tarjeta modelo, cada una con 2 expresiones en lengua. ¿Cuántas expresiones en lengua hay en total?", "3*2", "Se multiplica el número de tarjetas por las expresiones de cada una."),
        ex(TM + " Un compañero dice que la tarjeta contiene tres expresiones en lengua porque cuenta «Escuela Ejemplo». ¿Está bien contado? Sí o No.", "No", "«Escuela Ejemplo» es un nombre en castellano; las expresiones en lengua son dos."),
    ],
    Z=[
        ex(TM + " Un compañero propone agregar: «y nos explicaron para qué sirve cada paso de la rogativa». ¿Puede el curso escribir eso sin permiso? Sí o No.", "No", "Lo que ocurre en una rogativa lo cuentan solo quienes la conducen."),
        ex("Tu fuente te entregó la palabra «chaltumay». Para que suene mejor, la escribes «chal-tu-mai». ¿Qué debes hacer: copiarla tal cual la entregó la fuente o dejar tu versión?", "copiarla tal cual la entregó la fuente", "Cambiar la escritura puede alterar la palabra."),
    ],
    D=[
        ex(TM + " Compara dos versiones de la oración del compromiso. A) «Contaremos a las familias todo lo que vimos.» B) «Contaremos a las familias solo lo que usted nos autorizó contar.» ¿Cuál respeta el límite? Escribe la letra.", "B", "La A no reconoce que hay cosas que no se pueden contar."),
        ex("El educador tradicional no alcanzó a revisar «chaltumay» y la tarjeta se entrega mañana. ¿Qué es mejor: dejar «chaltumay» sin revisar o escribir «Gracias por recibirnos» en castellano?", "escribir «Gracias por recibirnos» en castellano", "Si la expresión no está revisada, el agradecimiento se puede escribir en castellano sin cambiar su sentido."),
    ],
    context=[ex("En una salida a terreno, una persona de la comunidad te cuenta una historia y te pide que no la repitas fuera de la visita. Al escribir tu informe, ¿incluyes la historia o escribes que la escuchaste sin contarla?", "escribes que la escuchaste sin contarla", "El límite que pidió la persona se respeta también por escrito.")],
    selfcheck=[
        ex("Un límite, ¿avisa hasta dónde se puede contar algo o decora el texto?", "avisa hasta dónde se puede contar algo", "Esa es su función."),
        ex("¿Debo adivinar el significado de una palabra en lengua que no entiendo? Sí o No.", "No", "Se anota y se pregunta al educador o educadora tradicional."),
        ex("¿Cuál de estas es una expresión en lengua indígena: «gracias» o «chaltumay»?", "chaltumay", "Gracias es castellano; chaltumay es mapuzugun."),
    ],
    task=T(
        "Lee esta tarjeta inventada: «Estimado educador: mari mari. Hoy visitamos el huerto de la Comunidad Muestra y aprendimos sobre las papas de la zona. Chaltumay por enseñarnos. Contaremos a nuestras familias solo lo que usted nos permita. Curso 6.º B.» En tu cuaderno haz tres cosas: marca las cinco partes del texto con letras (saludo, visita, agradecimiento, compromiso, firma), subraya las expresiones en lengua y escribe en una frase el límite que respeta.",
        "Saludo: Estimado educador: mari mari. Visita: Hoy visitamos el huerto... papas. Agradecimiento: Chaltumay por enseñarnos. Compromiso: Contaremos... permita. Firma: Curso 6.º B. Expresiones: mari mari, chaltumay. Límite: contar solo lo que el educador permita.",
        ["marca las cinco partes", "subraya las dos expresiones en lengua", "escribe el límite con sus palabras", "no agrega datos que el texto no dice"],
        ["texto marcado en el cuaderno", "frase con el límite"],
        ["marcar «papas» como expresión en lengua", "agregar datos inventados sobre el huerto"],
        "Pide que lea en voz alta cada parte marcada y diga qué función cumple; si duda, vuelve a la lista de partes.",
    ),
    reinforce="Copia la tarjeta modelo y pon una letra distinta sobre cada una de sus cinco partes.",
    extend="Escribe una versión de la tarjeta modelo para un museo, sin usar ninguna expresión en lengua y manteniendo el límite.",
)

# ============================================================ LR04 clase 3 · relacionar expresiones, pueblos y situaciones
LISTA = "Lista de expresiones (las palabras son reales y entregadas por la fuente; las situaciones son inventadas para practicar): «mari mari», saludo en mapuzugun, lengua del pueblo mapuche. «Chaltumay», agradecimiento en mapuzugun. «Iorana», saludo en rapa nui, lengua del pueblo rapa nui. «Maururu», agradecimiento en rapa nui."

L(
    LR4, 3,
    materials="Lápiz y hoja. La lista de expresiones está escrita aquí; las situaciones son inventadas para practicar.",
    use="Aprenderé a relacionar cada expresión en lengua indígena con su pueblo y con la situación en que se usa, y a ver por qué saludar y agradecer expresan respeto. Sirve para no mezclar lenguas de pueblos distintos en un mismo texto.",
    prior=["Sé leer un texto modelo y reconocer sus partes y sus límites.", "Sé que «mari mari» y «chaltumay» son del mapuzugun."],
    explain=[
        "Cada expresión pertenece a una lengua y a un pueblo. «Mari mari» y «chaltumay» son del mapuzugun, la lengua del pueblo mapuche. «Iorana» y «maururu» son del rapa nui, la lengua del pueblo rapa nui. Si escribo a una comunidad mapuche, uso expresiones mapuzugun que me entregó una fuente; si escribo a una comunidad rapa nui, uso expresiones rapa nui. No las intercambio.",
        "También cada expresión se relaciona con una situación. Un saludo se usa al comenzar un encuentro o un texto; un agradecimiento se usa al recibir algo o al despedirse. Saludar y agradecer con la expresión de la comunidad es una forma de respeto y de reciprocidad: reconozco lo que me ofrecen y respondo con cuidado.",
        "Relacionar también significa pensar en mi propia experiencia. En mi casa y en mi curso hay otros saludos y agradecimientos, y todos expresan cuidado hacia las personas. Pero no comparo diciendo que unos valen más que otros. Solo observo qué se parece y qué cambia, y escribo siempre desde qué comunidad y qué fuente hablo.",
    ],
    vocab=[("agradecimiento", "forma de reconocer lo que otra persona nos da"), ("reciprocidad", "dar y recibir con cuidado y respeto"), ("rapa nui", "lengua del pueblo rapa nui"), ("saludo", "expresión con que se comienza un encuentro"), ("relación cultural", "vínculo entre una expresión, su pueblo y su situación de uso")],
    worked=[
        W("Elegir la expresión de un pueblo", LISTA + " Escribes a una comunidad rapa nui para saludarla. ¿Qué expresión eliges?", ["Busco la expresión que sea saludo.", "Debe ser del pueblo rapa nui, no del mapuche.", "El saludo rapa nui de la lista es «iorana»."], "iorana"),
        W("Elegir para agradecer", LISTA + " Despides una visita a un taller mapuche y quieres agradecer en la lengua. ¿Qué expresión eliges?", ["Necesito un agradecimiento.", "Como el taller es mapuche, busco el agradecimiento en mapuzugun.", "Es «chaltumay»."], "chaltumay"),
    ],
    mistakes=[
        M("Usar «iorana» en una tarjeta para una comunidad mapuche.", "«Iorana» es del rapa nui, no del mapuzugun.", "Uso el saludo del mapuzugun que me entregó la fuente: «mari mari»."),
        M("Decir que el saludo de mi casa vale menos que el de una lengua indígena.", "Compararlos sin jerarquizar es parte del respeto.", "Digo qué se parece y qué cambia, sin decir cuál vale más."),
    ],
    R=[
        ex(LISTA + " ¿Qué expresión es saludo en rapa nui?", "iorana", "La lista lo indica."),
        ex(LISTA + " ¿Qué expresión es agradecimiento en rapa nui?", "maururu", "La lista lo indica."),
        ex(LISTA + " ¿De qué pueblo es la lengua mapuzugun?", "del pueblo mapuche", "La lista lo dice."),
    ],
    C=[
        ex(LISTA + " Une cada expresión con su lengua: A) mari mari, B) maururu, C) chaltumay. Lenguas: 1) mapuzugun, 2) rapa nui. Escribe los tres pares.", "A-1, B-2, C-1", "Mari mari y chaltumay son del mapuzugun; maururu es del rapa nui."),
        ex("Un saludo, ¿se usa al comenzar un encuentro o al terminar un agradecimiento?", "al comenzar un encuentro", "Ese es su uso en un texto o en una visita."),
        ex("Verdadero o falso: se puede usar una expresión rapa nui en una tarjeta para una comunidad mapuche.", "Falso", "Cada expresión se usa con la comunidad de su pueblo."),
    ],
    A=[
        ex(LISTA + " Une cada situación con la expresión correcta. 1) Llegas a una feria mapuche y saludas. 2) Te despides de un guía rapa nui y agradeces. 3) Escribes un agradecimiento a una artesana mapuche. Opciones: iorana, maururu, mari mari, chaltumay. Escribe tres pares (el número y la expresión).", "1 mari mari, 2 maururu, 3 chaltumay", "Saludo mapuche, agradecimiento rapa nui y agradecimiento mapuche."),
        arith(LISTA + " La lista tiene 4 expresiones y 2 de ellas son del rapa nui. ¿Cuántas son del mapuzugun?", "4-2", "Se restan las del rapa nui del total."),
        ex("Un curso quiere saludar y agradecer en un mismo texto a una comunidad rapa nui. ¿Qué pareja de expresiones debe usar: iorana y maururu o mari mari y chaltumay?", "iorana y maururu", "Son el saludo y el agradecimiento del rapa nui."),
    ],
    Z=[
        ex("Dos estudiantes escriben tarjetas. Ana usa «mari mari» para una comunidad mapuche. Tomás usa «mari mari» para una comunidad rapa nui. ¿Quién usó la expresión según su pueblo?", "Ana", "«Mari mari» es del mapuzugun."),
        ex("Un estudiante dice: «En mi casa se saluda con un abrazo; eso vale menos que un saludo en lengua indígena». ¿Está comparando sin jerarquizar? Sí o No.", "No", "Dice que uno vale menos que otro."),
    ],
    D=[
        ex("Una niña escribe: «Los saludos de mi casa y los saludos en mapuzugun expresan cuidado hacia las personas; cambia la lengua y la forma». ¿Compara sin jerarquizar? Sí o No.", "Sí", "Señala qué se parece y qué cambia, sin decir cuál vale más."),
        ex("Para una comunidad mapuche escribes «Mari mari. Chaltumay por la visita». El educador solo revisó «mari mari». ¿Puedes mantener «chaltumay» sin consultarlo? Sí o No.", "No", "Una expresión no revisada o no entregada por la fuente se consulta antes."),
    ],
    context=[ex("Tu curso recibirá en la escuela a una comunidad rapa nui. Quieres preparar un letrero de bienvenida. ¿Escribes «iorana» si el educador tradicional de tu escuela te lo entregó y autorizó, o lo copias de un video sin preguntar?", "lo escribes si el educador te lo entregó y autorizó", "Con fuente y permiso la expresión se usa con respeto.")],
    selfcheck=[
        ex("¿«Chaltumay» es una expresión del mapuzugun o del rapa nui?", "del mapuzugun", "Se entregó como agradecimiento mapuzugun."),
        ex("Al comparar mi saludo con otro, ¿digo cuál vale más o qué se parece y qué cambia?", "qué se parece y qué cambia", "Comparar sin jerarquizar es parte del respeto."),
        ex("¿Qué expresión sirve para agradecer en rapa nui: maururu o iorana?", "maururu", "Iorana es el saludo."),
    ],
    task=T(
        "Lee estas dos situaciones inventadas. Situación 1: tu curso visita un taller de lana de una comunidad mapuche. Situación 2: tu curso es recibido por un guía rapa nui en un museo. Con las expresiones de la lista de esta clase, escribe en tu cuaderno una oración de saludo y una de agradecimiento para cada situación, usando solo las expresiones que corresponden al pueblo de cada una. Luego escribe una oración que compare cómo agradecen en tu casa y en una de las situaciones, sin decir cuál es mejor.",
        "Situación 1: «Mari mari, educadora. Chaltumay por recibirnos.» Situación 2: «Iorana, guía. Maururu por mostrarnos el museo.» Comparación: «En mi casa se agradece diciendo gracias y en el museo con maururu; cambia la lengua, pero en ambos casos se reconoce lo recibido.»",
        ["usa las expresiones del pueblo correcto", "incluye un saludo y un agradecimiento por situación", "compara sin jerarquizar", "no inventa otras expresiones en lengua"],
        ["cuatro oraciones escritas", "una oración de comparación"],
        ["mezclar expresiones de pueblos distintos", "decir que una forma de agradecer es mejor"],
        "Si mezcla las expresiones, muéstrale la lista y pídele que las reubique por pueblo.",
    ),
    reinforce="Haz una tabla de dos columnas, mapuzugun y rapa nui, y copia en cada una sus dos expresiones de la lista.",
    extend="Escribe una nota breve que explique por qué agradecer es un acto de reciprocidad, sin mencionar ninguna expresión en lengua.",
)

# ============================================================ LR04 clase 4 · un texto breve atribuido
FV = "Ficha de la visita (inventada para practicar): Lugar: taller de lana de la Comunidad Ejemplo, pueblo mapuche. Persona que recibió al curso: la educadora tradicional. Lo que autorizó contar: que el taller funciona los jueves y que las personas aprenden a preparar lana. Saludo autorizado: «mari mari». Agradecimiento autorizado: «chaltumay». Lo que pidió no contar: lo que conversaron las personas dentro del taller."

L(
    LR4, 4,
    materials="Lápiz y hoja. La ficha de la visita está escrita aquí y es inventada para practicar.",
    use="Aprenderé a escribir un texto breve de cuatro oraciones que atribuye la información a su fuente, usa las expresiones en lengua que fueron autorizadas y respeta lo que no se debe contar. Sirve para escribir informes de salidas a terreno sin inventar.",
    prior=["Sé ubicar la situación comunicativa y los límites de un texto.", "Sé que cada expresión en lengua se usa con el pueblo al que pertenece."],
    explain=[
        "Un texto breve atribuido tiene cuatro partes. Primero saluda, con la expresión en lengua autorizada si corresponde. Segundo, cuenta lo que aprendí diciendo quién me lo enseñó, por ejemplo «Según la educadora tradicional…». Tercero, agradece. Cuarto, declara el límite: que no cuento lo que no se me autorizó.",
        "Atribuir es decir de quién viene la información. Si escribo «las personas aprenden a preparar lana», sin decir quién lo contó, parece que lo sé yo o que vale para todas las comunidades. En cambio, «según la educadora tradicional de la Comunidad Ejemplo, las personas aprenden a preparar lana» dice la fuente y el lugar, y no generaliza.",
        "En la ficha de la visita está todo lo que puedo usar: lo autorizado, el saludo y el agradecimiento. Lo que no está en la ficha no lo agrego, aunque me parezca lógico. Si quiero saber algo más, lo anoto como pregunta para la educadora. Antes de entregar, le pido que lea el texto y diga si respeta lo que enseñó.",
    ],
    vocab=[("atribuir", "decir de quién viene la información"), ("autorizado", "con permiso para contarlo"), ("generalizar", "decir que lo de una comunidad vale para todas"), ("informe de visita", "texto que cuenta una salida a terreno"), ("borrador", "primera versión de un texto")],
    worked=[
        W("Armar la primera oración", FV + " Escribe una oración que salude y nombre a quien recibió al curso.", ["Uso el saludo autorizado: «mari mari».", "Nombro a la persona de la ficha: la educadora tradicional.", "Las uno en una oración."], "Mari mari, educadora tradicional."),
        W("Atribuir lo aprendido", FV + " Escribe una oración que cuente lo autorizado y lo atribuya.", ["Elijo un dato autorizado: el taller funciona los jueves.", "Empiezo con «Según…» y nombro la fuente y la comunidad.", "Escribo la oración completa."], "Según la educadora tradicional de la Comunidad Ejemplo, el taller funciona los jueves."),
    ],
    mistakes=[
        M("Escribir «las comunidades mapuche hacen siempre sus talleres los jueves».", "La ficha habla de una sola comunidad.", "Escribo «según la educadora de la Comunidad Ejemplo» y no generalizo."),
        M("Agregar «y es un taller con más de cien años de historia» porque suena bonito.", "Ese dato no está en la ficha.", "Solo uso lo que está en la ficha o lo que la educadora me confirme."),
    ],
    R=[
        ex(FV + " ¿Qué día funciona el taller según la ficha?", "los jueves", "La ficha lo dice como lo autorizado."),
        ex(FV + " ¿Qué saludo autorizó la educadora?", "mari mari", "Está en la ficha."),
        ex(FV + " ¿Qué agradecimiento autorizó la educadora?", "chaltumay", "Está en la ficha."),
    ],
    C=[
        ex(FV + " ¿Qué pidió la educadora que no se contara?", "lo que conversaron las personas dentro del taller", "La ficha lo dice como límite."),
        ex("Atribuir, ¿es decir de quién viene la información o inventar quién la dijo?", "decir de quién viene la información", "Esa es la definición vista en la clase."),
        ex(FV + " Verdadero o falso: según la ficha, la educadora autorizó contar que el taller tiene más de cien años.", "Falso", "Ese dato no está en la ficha."),
    ],
    A=[
        ex("Ordena las cuatro oraciones del texto breve. A) agradecimiento. B) límite. C) saludo. D) lo aprendido con su fuente. Escribe las letras en orden.", "C, D, A, B", "El texto saluda, cuenta lo aprendido, agradece y declara el límite."),
        ex(FV + " Elige la mejor oración para contar lo aprendido. A) «Los mapuche siempre preparan lana los jueves.» B) «Según la educadora tradicional de la Comunidad Ejemplo, las personas aprenden a preparar lana en el taller.» Escribe la letra.", "B", "Atribuye y no generaliza; la A generaliza."),
        arith("Un texto breve debe tener 4 oraciones. Un compañero escribió 3 oraciones y el resto de su texto son frases sueltas. ¿Cuántas oraciones le faltan?", "4-3", "Se restan las escritas de las cuatro pedidas."),
    ],
    Z=[
        ex(FV + " Una niña escribe: «La educadora nos mostró también un tejido ceremonial». ¿Esa información está en la ficha? Sí o No.", "No", "La ficha no menciona ningún tejido ceremonial."),
        ex(FV + " Un niño quiere contar la conversación que tuvieron dos personas dentro del taller. ¿Respeta el límite? Sí o No.", "No", "La educadora pidió no contarla."),
    ],
    D=[
        ex(FV + " Dos versiones del límite. A) «No contaremos lo que conversaron las personas dentro del taller.» B) «Tal vez más adelante contemos lo que conversaron las personas.» ¿Cuál respeta lo que pidió la educadora? Escribe la letra.", "A", "La B deja abierta la posibilidad de contarlo."),
        ex("Tu texto dice «Según la educadora…». Descubres que no sabes si ella autorizó nombrarla. ¿Qué haces: dejas su nombre igual o preguntas antes de entregar?", "preguntas antes de entregar", "El nombre de una persona se usa con su permiso."),
    ],
    context=[ex("Terminas una salida a terreno y debes escribir el informe de visita para tu curso. ¿Cuentas lo que una persona te dijo en privado sin pedirle permiso, o escribes solo lo que te autorizó contar?", "escribes solo lo que te autorizó contar", "Lo dicho en privado se cuenta solo con permiso.")],
    selfcheck=[
        ex("¿Qué palabra al comienzo de una oración indica la fuente: «según» o «siempre»?", "según", "Según nombra a quien dijo la información."),
        ex("¿Cuántas partes tiene el texto breve de esta clase?", "4", "Saludo, lo aprendido, agradecimiento y límite."),
        ex("Antes de entregar, ¿pido que lo lea el educador o la educadora tradicional? Sí o No.", "Sí", "Así reviso que respete lo enseñado."),
    ],
    task=T(
        "Lee esta ficha inventada: «Lugar: sala de radio de la Comunidad Muestra, pueblo rapa nui. Persona que recibió al curso: el locutor comunitario. Autorizó contar: que el programa se transmite los sábados. Saludo autorizado: «iorana». Agradecimiento autorizado: «maururu». Pidió no contar: los nombres de las personas que llaman al programa.» En tu cuaderno escribe un texto de cuatro oraciones (saludo, lo aprendido con su fuente, agradecimiento y límite) usando solo lo que está en la ficha.",
        "«Iorana, locutor comunitario. Según el locutor comunitario de la Comunidad Muestra, el programa se transmite los sábados. Maururu por recibir a nuestro curso. No contaremos los nombres de las personas que llaman al programa.»",
        ["tiene saludo con la expresión autorizada", "atribuye lo aprendido", "agradece con la expresión autorizada", "declara el límite y no agrega datos"],
        ["texto de cuatro oraciones"],
        ["agregar datos que no están en la ficha", "olvidar el límite"],
        "Pide que marque en la ficha cada dato que usó; todo lo que no esté marcado debe salir del texto.",
    ),
    reinforce="Copia las cuatro oraciones del ejemplo de la clase y rotula cada una con su función.",
    extend="Escribe una segunda versión de tu texto para un cartel de pasillo, de dos oraciones, que mantenga el límite.",
)

# ============================================================ LR04 clase 5 · contrastar dos textos sin jerarquizar
TA = "Texto A (inventado): «Mari mari, educadora. Chaltumay por recibirnos en el taller. Contaremos solo lo autorizado.» (escrito por el 6.º A para la educadora tradicional de una comunidad mapuche)."
TB = "Texto B (inventado): «Iorana, guía. Maururu por mostrarnos el museo.» (escrito por el 6.º B para un guía de una comunidad rapa nui)."

L(
    LR4, 5,
    materials="Lápiz y hoja. Los dos textos están escritos aquí y son inventados para practicar.",
    use="Aprenderé a comparar dos textos breves escritos para situaciones y pueblos distintos, diciendo qué se parece y qué cambia, sin decir que uno es mejor persona, mejor cultura o más auténtico. Sirve para valorar la diversidad de los pueblos.",
    prior=["Sé escribir un texto breve atribuido y con límites.", "Sé que cada expresión en lengua pertenece a un pueblo."],
    explain=[
        "Comparar es mirar dos cosas con los mismos criterios. Para dos textos breves puedo usar criterios como: a quién va dirigido, qué expresiones en lengua usa, cuántas oraciones tiene y si declara un límite. Cada criterio se responde para cada texto y luego se anota qué se parece y qué cambia.",
        "Jerarquizar es decir que algo vale más que otra cosa: «este pueblo es más auténtico», «esta lengua es más importante». En este tema no jerarquizamos, porque cada pueblo, cada lengua y cada situación tienen su propio valor. Sí puedo decir que un texto cumple mejor su propósito en su situación, si doy una razón observable, como «declara el límite que pidió la fuente».",
        "Una comparación respetuosa nombra la fuente y la comunidad de cada texto, no generaliza y no usa palabras como «mejor», «más verdadero» o «más puro» para pueblos o lenguas. Si una duda cultural aparece, la consulto con el educador o la educadora tradicional. Al final escribo una frase que resuma las semejanzas y las diferencias.",
    ],
    vocab=[("comparar", "mirar dos cosas con los mismos criterios"), ("criterio", "aspecto que se usa para comparar"), ("jerarquizar", "decir que algo vale más que otra cosa"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas cambian")],
    worked=[
        W("Comparar con un criterio", TA + " " + TB + " Compara los dos textos según su destinatario.", ["En el texto A se escribe a una educadora tradicional de una comunidad mapuche.", "En el texto B se escribe a un guía de una comunidad rapa nui.", "Son personas y pueblos distintos."], "A va a una educadora mapuche y B a un guía rapa nui: el destinatario cambia"),
        W("Reconocer una jerarquización", "Alguien dice: «El texto A es más auténtico que el B porque usa más palabras en lengua». ¿Compara o jerarquiza?", ["La frase dice que A es más auténtico.", "Decir que algo es más auténtico es poner uno sobre otro.", "Además, la cantidad de palabras no mide la autenticidad."], "jerarquiza"),
    ],
    mistakes=[
        M("Escribir «el texto del pueblo mapuche es mejor que el del pueblo rapa nui».", "Ningún pueblo ni lengua vale más que otro.", "Escribo qué se parece y qué cambia, y uso criterios observables."),
        M("Comparar sin usar los mismos criterios para los dos textos.", "Si miro cosas distintas en cada uno, la comparación no sirve.", "Elijo los criterios primero y los respondo para ambos textos."),
    ],
    R=[
        ex(TA + " ¿Qué saludo en lengua usa el texto A?", "mari mari", "Es la primera expresión del texto A."),
        ex(TB + " ¿Qué agradecimiento en lengua usa el texto B?", "maururu", "Aparece en la segunda oración del texto B."),
        ex("Jerarquizar, ¿es decir que algo vale más que otra cosa o mirar dos cosas con los mismos criterios?", "decir que algo vale más que otra cosa", "Esa es la definición de la clase."),
    ],
    C=[
        ex(TA + " " + TB + " ¿Cuál de los dos textos declara un límite sobre lo que contará?", "el texto A", "El A dice «Contaremos solo lo autorizado»."),
        ex(TA + " " + TB + " ¿Qué lengua usan las expresiones del texto A y cuáles las del B?", "el A usa mapuzugun y el B usa rapa nui", "Mari mari y chaltumay son mapuzugun; iorana y maururu son rapa nui."),
        ex("Verdadero o falso: es correcto decir «la lengua de este texto es más importante que la del otro».", "Falso", "Eso jerarquiza lenguas; cada una tiene su valor."),
    ],
    A=[
        arith(TA + " " + TB + " Cuenta las oraciones del texto A y las del texto B, tal como están puntuadas. ¿Cuántas oraciones hay entre los dos textos?", "3+2", "El A tiene tres oraciones y el B tiene dos."),
        ex(TA + " " + TB + " Completa la comparación con A o B: la persona que recibió al curso es una educadora en el texto ___ y un guía en el texto ___. Escribe las dos letras en orden.", "A, B", "El A se dirige a una educadora y el B a un guía."),
        ex("Clasifica cada frase como C (compara) o J (jerarquiza). 1) «Los dos textos agradecen, pero con expresiones de lenguas distintas». 2) «El texto B es más puro». 3) «El A tiene tres oraciones y el B dos». Escribe las tres letras.", "1 C, 2 J, 3 C", "Solo la frase 2 pone un texto sobre el otro."),
    ],
    Z=[
        ex(TA + " " + TB + " Un compañero dice que el texto A es mejor porque tiene más oraciones. ¿Esa razón basta para decir que un texto es mejor persona o mejor cultura? Sí o No.", "No", "La cantidad de oraciones no mide el valor de un pueblo ni de una lengua."),
        ex(TA + " " + TB + " Se puede decir que el texto A cumple mejor lo pedido en la clase anterior, que era declarar el límite. Esa afirmación, ¿usa una razón observable o juzga a las personas?", "usa una razón observable", "Se apoya en una frase del texto: «Contaremos solo lo autorizado»."),
    ],
    D=[
        ex(TA + " " + TB + " Elige la mejor frase de cierre. A) «Ambos textos saludan y agradecen con la lengua de cada comunidad; el A además declara un límite». B) «El texto A es más auténtico que el B». C) «El texto B no sirve porque es más corto». Escribe la letra.", "A", "Resume semejanzas y diferencias sin jerarquizar."),
        ex("Escribes una comparación y dudas si una expresión está bien escrita. ¿Qué haces: la corriges por tu cuenta o la consultas con el educador o la educadora tradicional?", "la consultas con el educador o la educadora tradicional", "Solo quien conoce la lengua puede confirmarla."),
    ],
    context=[ex("Dos cursos hicieron un cartel de bienvenida, uno para una comunidad mapuche y otro para una comunidad rapa nui. Quieres decir cuál te gustó más. ¿Dices que uno es más verdadero o explicas qué se parece y qué cambia entre ambos?", "explicas qué se parece y qué cambia entre ambos", "Así se compara sin jerarquizar pueblos ni lenguas.")],
    selfcheck=[
        ex("¿Cuántos textos compara esta clase: uno o dos?", "dos", "Se comparan el texto A y el texto B."),
        ex("Una palabra que jerarquiza es «igual» o «más puro». ¿Cuál jerarquiza?", "más puro", "Pone una cosa sobre otra."),
        ex("¿Debo usar los mismos criterios para los dos textos? Sí o No.", "Sí", "Así la comparación es justa."),
    ],
    task=T(
        "Lee estos dos textos inventados. Texto 1 (para una comunidad mapuche): «Mari mari, artesana. Chaltumay por enseñarnos. Contaremos solo lo autorizado.» Texto 2 (para una comunidad rapa nui): «Iorana, bailarín. Maururu por su visita a la escuela.» En tu cuaderno haz una tabla con dos columnas y estas filas: destinatario, expresiones en lengua, número de oraciones, declara un límite. Luego escribe una frase de cierre que diga una semejanza y una diferencia, sin jerarquizar.",
        "Destinatario: artesana / bailarín. Expresiones: mari mari y chaltumay / iorana y maururu. Oraciones: 3 / 2. Límite: sí / no. Cierre: «Los dos textos saludan y agradecen con la lengua de cada comunidad; el primero declara un límite y el segundo no.»",
        ["completa las cuatro filas para ambos textos", "usa los mismos criterios", "escribe una semejanza y una diferencia", "no jerarquiza"],
        ["tabla de comparación", "frase de cierre"],
        ["decir que un pueblo es mejor", "no completar una fila"],
        "Si aparece una jerarquización, pídele que cambie la palabra por un criterio observable de la tabla.",
    ),
    reinforce="Copia los textos A y B y subraya en cada uno el saludo y el agradecimiento con un color distinto.",
    extend="Escribe una comparación entre uno de los textos de la clase y una tarjeta de agradecimiento de tu casa, sin jerarquizar.",
)


# ============================================================ LR05 clase 1 · situar la revitalización
CR = "Ficha de comunidad (inventada para practicar): Pueblo: mapuche. Comunidad Ejemplo. Fuente: la coordinadora del taller de lengua, que visitó la escuela en agosto. Autorización: permite contar lo que dijo para trabajos escolares. Acciones: un taller de lengua semanal para niñas y niños, un programa de radio comunitaria y letreros con saludos en la sede."
CS = "Ficha sin datos (inventada): «Hay un movimiento para recuperar la lengua. Me lo contaron en una reunión. Funciona muy bien en todos lados.»"

L(
    LR5, 1,
    materials="Lápiz y hoja. Las fichas están escritas aquí y son inventadas para practicar. No necesitas ningún dispositivo.",
    use="Aprenderé qué significan revitalizar y fortalecer una lengua, y a situar de qué pueblo, comunidad y fuente hablo antes de explicar su sentido. Sirve para explicar sin generalizar.",
    prior=["Sé que cada pueblo tiene su lengua y que una información necesita fuente y permiso.", "Sé que no se mide la pertenencia a un pueblo por hablar su lengua."],
    explain=[
        "Revitalizar una lengua es hacer que vuelva a usarse en más lugares y por más personas. Fortalecerla es hacerla más firme cuando todavía se usa, por ejemplo con talleres, programas de radio, libros y letreros. Algunas comunidades hablan de revitalización, otras de fortalecimiento: la palabra la elige cada comunidad según su situación.",
        "Para explicar el sentido de estas acciones primero las ubico. Pregunto: ¿de qué pueblo y comunidad hablo?, ¿quién me lo contó?, ¿tengo su permiso? Una ficha completa responde esas preguntas. Una ficha como «me lo contaron» y «funciona en todos lados» no sirve, porque no dice de qué pueblo ni de qué fuente viene, y generaliza a todas partes.",
        "El sentido de revitalizar no es obligar a nadie a hablar. Es abrir posibilidades para que quienes quieran aprender o seguir usando su lengua puedan hacerlo, con respeto por cada historia personal. Hablo de una comunidad concreta, como la Comunidad Ejemplo de las fichas, y nunca digo que lo que ocurre allí ocurre igual en todas las comunidades.",
    ],
    vocab=[("revitalización", "acciones para que una lengua se use otra vez en más lugares y por más personas"), ("fortalecimiento", "acciones para afirmar una lengua que todavía se usa"), ("taller de lengua", "espacio organizado para practicar y enseñar una lengua"), ("fuente", "persona o documento de donde viene un dato"), ("generalizar", "decir que lo de una comunidad vale para todas")],
    worked=[
        W("Leer una ficha completa", CR + " ¿Qué acciones de revitalización menciona la ficha?", ["Busco la línea «Acciones».", "Nombra un taller semanal, un programa de radio y letreros.", "Cuento tres acciones."], "un taller semanal, un programa de radio y letreros con saludos"),
        W("Detectar una ficha que no sirve", CS + " ¿Se puede explicar el sentido de la revitalización con esta ficha?", ["Busco pueblo, comunidad y fuente.", "No aparecen: solo dice «me lo contaron».", "Además dice «en todos lados», que generaliza."], "no: faltan pueblo, comunidad y fuente, y generaliza"),
    ],
    mistakes=[
        M("Decir que revitalizar es obligar a hablar la lengua.", "El sentido es abrir posibilidades para usarla, no obligar.", "Explico que se crean espacios para quienes quieran aprender o usarla."),
        M("Escribir «todas las comunidades hacen talleres de lengua» a partir de una sola ficha.", "Una ficha cuenta una comunidad, no todas.", "Escribo «en la Comunidad Ejemplo hay un taller de lengua»."),
    ],
    R=[
        ex(CR + " ¿De qué pueblo es la Comunidad Ejemplo según la ficha?", "mapuche", "La línea «Pueblo» lo dice."),
        ex(CR + " ¿Quién es la fuente de la ficha?", "la coordinadora del taller de lengua", "La ficha nombra a quien contó."),
        ex("Revitalizar una lengua, ¿es hacer que vuelva a usarse en más lugares y por más personas o prohibir su uso?", "hacer que vuelva a usarse en más lugares y por más personas", "Así se definió en la clase."),
    ],
    C=[
        ex(CR + " ¿Cuántas acciones de revitalización enumera la ficha?", "3", "Taller, radio y letreros.", "1+1+1"),
        ex(CS + " ¿Qué palabra de la ficha sin datos muestra que generaliza: «muy bien» o «en todos lados»?", "en todos lados", "Esa frase dice que ocurre en cualquier lugar."),
        ex("Verdadero o falso: fortalecer una lengua es solo para lenguas que ya nadie usa.", "Falso", "Fortalecer es afirmar una lengua que todavía se usa."),
    ],
    A=[
        ex(CR + " Ordena para explicar el sentido con esta ficha. A) cuento una acción de revitalización. B) nombro pueblo, comunidad y fuente. C) aclaro que hablo solo de esta comunidad. Escribe las letras en orden.", "B, A, C", "Primero ubico la fuente, luego cuento la acción y al final declaro el límite."),
        ex(CR + " Elige la mejor frase. A) «Según la coordinadora del taller de lengua de la Comunidad Ejemplo, hay un taller semanal para niñas y niños.» B) «Todos los pueblos hacen un taller semanal.» Escribe la letra.", "A", "Atribuye y no generaliza."),
        arith(CR + " Supón que el taller se hace una vez por semana y que cada taller dura 2 horas. ¿Cuántas horas de taller hay en 4 semanas?", "2*4", "Dos horas por semana durante cuatro semanas."),
    ],
    Z=[
        ex(CR + " Un niño agrega a la ficha: «y las personas de la comunidad que no hablan la lengua ya no son parte del pueblo». ¿Es correcto escribir eso? Sí o No.", "No", "La pertenencia no se mide por hablar la lengua."),
        ex(CS + " Para completar la ficha sin datos, ¿qué conviene hacer: preguntar quién contó y de qué comunidad habla, o escribir de todos modos la explicación?", "preguntar quién contó y de qué comunidad habla", "Sin fuente no se puede explicar con seguridad."),
    ],
    D=[
        ex(CR + " La coordinadora dice que habla del taller de su comunidad. Una compañera quiere usar la ficha para explicar qué hacen en otra región. ¿Puede? Sí o No.", "No", "La ficha vale solo para la Comunidad Ejemplo."),
        arith("En un curso de 28 estudiantes, 17 completaron una ficha como la de la Comunidad Ejemplo con pueblo, comunidad y fuente. ¿Cuántas fichas están incompletas?", "28-17", "Se restan las completas del total."),
    ],
    context=[ex("En tu localidad hay un programa de radio escolar con saludos en una lengua indígena. Quieres explicar su sentido a tu curso. ¿Qué dato necesitas primero: quién lo organiza y con qué permiso, o cuántas personas lo escuchan?", "quién lo organiza y con qué permiso", "Primero se necesita la fuente y la autorización.")],
    selfcheck=[
        ex("¿Qué acción busca que una lengua vuelva a usarse: revitalizar o dejarla sin practicar?", "revitalizar", "Revitalizar busca que vuelva a usarse en más lugares y por más personas."),
        ex("Si una ficha no dice de qué pueblo habla, ¿la uso igual? Sí o No.", "No", "Se anota «por preguntar» y se detiene el trabajo."),
        ex("¿Una sola ficha permite hablar de todas las comunidades? Sí o No.", "No", "Describe una comunidad."),
    ],
    task=T(
        "Lee esta ficha inventada: «Pueblo: aymara. Comunidad Muestra. Fuente: un educador tradicional que visitó la escuela. Autorización: puede contarse en la sala. Acciones: un taller de lengua los viernes y un cartel de bienvenida en la entrada de la sede. Aclara que habla solo por su comunidad.» En tu cuaderno escribe un párrafo de tres oraciones que explique qué hace la comunidad por su lengua. Nombra la fuente, no generalices y no agregues datos que no estén en la ficha.",
        "Según un educador tradicional de la Comunidad Muestra, del pueblo aymara, la comunidad hace un taller de lengua los viernes y puso un cartel de bienvenida en la entrada de la sede. Con esas acciones se da espacio para usar la lengua. Él habla solo por su comunidad.",
        ["nombra la fuente y el pueblo", "menciona las dos acciones de la ficha", "no generaliza", "declara el límite"],
        ["párrafo de tres oraciones"],
        ["generalizar a todos los pueblos", "agregar acciones que la ficha no tiene"],
        "Si agregó datos, pídele que los marque; lo que no esté en la ficha debe salir.",
    ),
    reinforce="Vuelve a leer la ficha de la Comunidad Ejemplo y subraya sus tres acciones con tres colores.",
    extend="Inventa una ficha con las mismas partes sobre un espacio de tu escuela donde una lengua indígena podría usarse, y rotúlala como inventada.",
)

# ============================================================ LR05 clase 2 · escuchar un testimonio con límites
TT = "Testimonio (inventado para practicar): una coordinadora de un taller de lengua de la Comunidad Muestra cuenta: «Hace cinco años el taller tenía 8 participantes y hoy tiene 20. Lo que buscamos es que niñas y niños escuchen la lengua desde pequeños. Yo creo que, cuando aparecen cosas nuevas, como un aparato que no existía, las palabras para nombrarlas deben acordarse entre las personas que hablan la lengua, y no inventarlas una sola persona. Hablo solo de mi taller. Nadie deja de ser parte de nuestro pueblo por hablar poco la lengua.»"

L(
    LR5, 2,
    materials="Lápiz y hoja. El testimonio está escrito aquí y es inventado para practicar. Puede leerlo en voz alta una persona adulta.",
    use="Aprenderé a escuchar o leer una explicación sobre por qué se fortalece una lengua y a separar hechos, opiniones y límites declarados por la fuente. Sirve para explicar el sentido de la revitalización sin cambiar lo que alguien dijo.",
    prior=["Sé qué significan revitalizar y fortalecer una lengua.", "Sé que una ficha o un relato describe una sola comunidad."],
    explain=[
        "Cuando alguien explica por qué se fortalece su lengua, escucho en tres planos. Los hechos son lo que cuenta como ocurrido, como que el taller pasó de 8 a 20 participantes. Las opiniones son lo que cree, y se citan con palabras como «cree que». Los límites son sus avisos de hasta dónde vale lo que dice, como «hablo solo de mi taller».",
        "Aparte de lo que dijo la fuente, está lo que yo interpreto. Si leo que hay más participantes y pienso «entonces ya no hay problema», esa idea es mía: no la dijo ella y no puedo atribuírsela. Para evitarlo, escribo primero lo que dijo con «según» y marco mis ideas con «yo pienso».",
        "En el testimonio aparece una idea importante: las palabras nuevas para cosas nuevas se acuerdan entre quienes hablan la lengua. Eso quiere decir que una persona sola no las inventa. También aparece una frase sobre identidad: nadie deja de ser parte de su pueblo por hablar poco la lengua. Ambas ideas son parte de lo que la fuente cree y las cito como suyas.",
    ],
    vocab=[("participante", "persona que asiste a una actividad"), ("hecho", "algo que la fuente cuenta como ocurrido"), ("opinión", "lo que alguien cree o piensa"), ("límite declarado", "aviso de hasta dónde vale lo que se dice"), ("acordar", "ponerse de acuerdo entre varias personas")],
    worked=[
        W("Separar hecho y opinión", TT + " ¿«El taller pasó de 8 a 20 participantes» es un hecho o una opinión?", ["Busco la frase en el testimonio.", "La coordinadora la cuenta como algo ocurrido, con cifras.", "No usa «creo»."], "es un hecho que cuenta la fuente"),
        W("Detectar una interpretación mía", TT + " Una lectora escribe: «Entonces la lengua ya está fuera de peligro». ¿Lo dijo la coordinadora?", ["Busco esa frase en el testimonio.", "No aparece.", "Es una conclusión de la lectora."], "no: es una interpretación de la lectora"),
    ],
    mistakes=[
        M("Escribir «la coordinadora dice que la lengua ya no necesita ayuda».", "Ella no dijo eso; es una conclusión mía.", "Escribo solo lo que dijo y marco lo mío con «yo pienso»."),
        M("Usar el testimonio para explicar lo que ocurre en todos los talleres de lengua del país.", "Ella habló solo de su taller.", "Respeto su límite y hablo solo de ese taller."),
    ],
    R=[
        ex(TT + " ¿Cuántos participantes tiene el taller hoy?", "20", "El testimonio lo dice: «hoy tiene 20»."),
        ex(TT + " ¿Cuántos participantes tenía hace cinco años?", "8", "Está en la primera oración."),
        ex(TT + " ¿Qué busca el taller según la coordinadora?", "que niñas y niños escuchen la lengua desde pequeños", "La segunda oración lo dice."),
    ],
    C=[
        ex(TT + " ¿Cuál es el límite que declara la coordinadora?", "habla solo de su taller", "Ella lo dice con esas palabras."),
        ex(TT + " «Las palabras para cosas nuevas deben acordarse entre quienes hablan la lengua», ¿es un hecho o una opinión de la coordinadora?", "una opinión de la coordinadora", "El testimonio dice «yo creo que»."),
        ex(TT + " Verdadero o falso: según la coordinadora, quien habla poco la lengua deja de ser parte de su pueblo.", "Falso", "Ella dice lo contrario."),
    ],
    A=[
        arith(TT + " ¿Cuántos participantes más tiene el taller hoy que hace cinco años?", "20-8", "Se resta la cantidad antigua de la actual."),
        ex(TT + " Clasifica cada frase como H (hecho de la fuente), O (opinión de la fuente) o I (interpretación mía). 1) El taller tiene hoy 20 participantes. 2) Las palabras nuevas se acuerdan entre hablantes. 3) Entonces ya no hay peligro para la lengua. Escribe las tres letras.", "1 H, 2 O, 3 I", "La frase 3 no está en el testimonio."),
        ex(TT + " Ordena lo que haces al leer. A) declaro el límite. B) anoto lo que dice la fuente. C) anoto aparte lo que pienso yo. Escribe las letras en orden.", "B, C, A", "Primero lo dicho, luego lo mío y al final el límite."),
    ],
    Z=[
        ex(TT + " Un estudiante quiere escribir: «En todo Chile los talleres de lengua han crecido de 8 a 20 personas». ¿Respeta el límite de la coordinadora? Sí o No.", "No", "Ella habló solo de su taller."),
        ex(TT + " En la sala, alguien propone una palabra nueva en lengua indígena para nombrar un aparato. Según la coordinadora, ¿quién debe acordar esa palabra: una sola persona o quienes hablan la lengua?", "quienes hablan la lengua", "Ella cree que se acuerda entre hablantes."),
    ],
    D=[
        ex(TT + " Elige el mejor resumen. A) «Según una coordinadora de la Comunidad Muestra, su taller pasó de 8 a 20 participantes y busca que niñas y niños escuchen la lengua; ella habla solo de su taller». B) «Los talleres de lengua de todo el país crecieron». C) «La coordinadora cree que la lengua ya está salvada». Escribe la letra.", "A", "Es la única que atribuye y mantiene el límite."),
        ex("Una persona que escucha anotó 9 afirmaciones. 6 las dijo la fuente y el resto son ideas de quien escuchó. Si cada idea de quien escuchó se marca con «yo pienso», ¿cuántas veces aparece «yo pienso»?", "3", "Nueve menos seis son las ideas propias.", "9-6"),
    ],
    context=[ex("Un familiar mayor te explica por qué le importa hablar su lengua. Al escribirlo, ¿empiezas con «Según…» y marcas tus ideas con «yo pienso» o lo escribes todo mezclado?", "empiezas con «Según…» y marcas tus ideas con «yo pienso»", "Así se distingue lo que dijo del aporte propio.")],
    selfcheck=[
        ex("¿Una frase como «creo que» introduce un hecho o una opinión?", "una opinión", "«Creo que» muestra lo que alguien piensa."),
        ex("Si la fuente dice «hablo solo de mi taller», ¿puedo usar su relato para otros talleres? Sí o No.", "No", "Ese es su límite."),
        ex("Una conclusión que saqué yo y que la fuente no dijo, ¿es hecho de la fuente o interpretación mía?", "interpretación mía", "La fuente no la afirmó."),
    ],
    task=T(
        "Lee este testimonio inventado: «Un joven de la Comunidad Ejemplo cuenta que su club de lectura se reúne dos veces al mes y que en cada sesión se lee un cuento en la lengua y en castellano. Cree que más jóvenes se sumarían si hubiera premios. Aclara que no sabe cómo funcionan los clubes de otras comunidades.» En tu cuaderno haz tres listas: hechos que cuenta, opinión que da y límite que declara. Después escribe dos oraciones con «Según…» y una con «yo pienso».",
        "Hechos: el club se reúne dos veces al mes; en cada sesión se lee un cuento en la lengua y en castellano. Opinión: más jóvenes se sumarían con premios. Límite: no sabe cómo funcionan otros clubes. Frases: «Según un joven de la Comunidad Ejemplo, el club se reúne dos veces al mes.» «Según él, se lee un cuento en la lengua y en castellano.» «Yo pienso que leer en dos lenguas ayuda a aprender.»",
        ["separa hechos, opinión y límite", "usa «según» para lo que dijo la fuente", "marca lo propio con «yo pienso»", "no agrega datos"],
        ["tres listas", "tres oraciones"],
        ["mezclar su opinión con los hechos", "borrar el límite"],
        "Pide que subraye en el testimonio cada dato que usó; lo que no esté subrayado debe llevar «yo pienso».",
    ),
    reinforce="Relee el testimonio de la coordinadora y subraya con un color los hechos y con otro la opinión.",
    extend="Escribe tres frases sobre una actividad de tu escuela: un hecho, una opinión y un límite, y pide a alguien que adivine cuál es cuál.",
)

# ============================================================ LR05 clase 3 · préstamos y neologismos
PN = "Cuadro de palabras (la información lingüística es general; los ejemplos son para practicar): PRÉSTAMO es una palabra que una lengua toma de otra. Ejemplos en castellano: «fútbol» (del inglés), «escáner» (del inglés), «guagua» (del quechua), «palta» (del quechua), «copihue» (del mapuzugun). NEOLOGISMO es una palabra nueva que surge en una lengua, muchas veces uniendo piezas que ya existen. Ejemplos en castellano: «alunizar» (de «luna»), «pantallazo» (de «pantalla»)."

L(
    LR5, 3,
    materials="Lápiz y hoja. El cuadro de palabras está escrito aquí. No necesitas dispositivos.",
    use="Aprenderé a reconocer préstamos y neologismos y a explicar cómo ayudan a una lengua a expresar cosas nuevas. Sirve para entender que una lengua cambia sin dejar de ser suya.",
    prior=["Sé explicar qué significa revitalizar una lengua.", "Sé que las palabras nuevas en una lengua indígena las acuerdan quienes la hablan."],
    explain=[
        "Todas las lenguas cambian. Una forma de cambiar es tomar palabras de otra lengua: eso se llama préstamo. En castellano usamos «fútbol» y «escáner», que vienen del inglés, y también palabras de lenguas indígenas, como «guagua» y «palta», del quechua, y «copihue», del mapuzugun. Por eso, cuando hablamos castellano en Chile, usamos palabras de pueblos originarios casi sin darnos cuenta.",
        "Otra forma de cambiar es crear palabras nuevas con piezas que la lengua ya tiene: eso se llama neologismo. Para hablar de llegar a la luna se creó «alunizar», a partir de «luna». Un neologismo sirve para nombrar una cosa nueva o una idea nueva. Cuando una palabra nueva se usa y todos la entienden, deja de parecer nueva.",
        "Las lenguas indígenas también pueden incorporar préstamos y crear neologismos para expresar ideas actuales. Pero esas palabras no las inventa un estudiante: las acuerdan las personas que hablan la lengua, con sus educadores, sus mayores y sus especialistas. Mi tarea es reconocerlas, entender para qué sirven y consultar. Y cambiar no hace a una lengua menos auténtica: una lengua viva se renueva.",
    ],
    vocab=[("préstamo", "palabra que una lengua toma de otra"), ("neologismo", "palabra nueva que surge en una lengua"), ("quechua", "lengua del pueblo quechua"), ("lengua viva", "lengua que se usa y cambia con sus hablantes"), ("expresar", "decir lo que pienso o siento")],
    worked=[
        W("Clasificar una palabra", PN + " ¿«Guagua» es préstamo o neologismo?", ["Según el cuadro, guagua viene del quechua.", "Una palabra que viene de otra lengua es un préstamo.", "Entonces es préstamo."], "préstamo, del quechua"),
        W("Explicar para qué sirve", PN + " ¿Para qué sirve el neologismo «alunizar»?", ["Está formado con «luna», que ya existía en castellano.", "Nombra algo nuevo: llegar a la luna.", "Sirve para expresar esa idea con una sola palabra."], "sirve para nombrar con una palabra una idea nueva usando piezas que la lengua ya tiene"),
    ],
    mistakes=[
        M("Decir que «guagua» es una palabra inventada hace poco.", "Es un préstamo del quechua, no un invento reciente.", "La clasifico como préstamo y nombro su lengua de origen."),
        M("Pensar que usar préstamos hace a una lengua menos auténtica.", "Todas las lenguas toman y crean palabras y siguen siendo suyas.", "Explico que una lengua viva se renueva."),
    ],
    R=[
        ex(PN + " ¿De qué lengua viene «fútbol» según el cuadro?", "del inglés", "El cuadro lo dice."),
        ex(PN + " ¿De qué lengua viene «copihue» según el cuadro?", "del mapuzugun", "El cuadro lo dice."),
        ex("Un préstamo, ¿es una palabra que una lengua toma de otra o una palabra que se borra del diccionario?", "una palabra que una lengua toma de otra", "Esa es la definición de la clase."),
    ],
    C=[
        ex(PN + " ¿«Pantallazo» es préstamo o neologismo según el cuadro?", "neologismo", "Está formado con «pantalla»."),
        ex(PN + " ¿Cuáles de estas palabras vienen de lenguas indígenas: palta, escáner, guagua, fútbol? Escribe las dos.", "palta y guagua", "Ambas vienen del quechua; escáner y fútbol vienen del inglés."),
        ex("Verdadero o falso: un neologismo se crea con piezas que la lengua ya tiene, muchas veces.", "Verdadero", "Así se explicó en la clase."),
    ],
    A=[
        ex(PN + " Clasifica cada palabra como P (préstamo) o N (neologismo): 1) escáner, 2) alunizar, 3) copihue, 4) pantallazo. Escribe las cuatro letras.", "1 P, 2 N, 3 P, 4 N", "Escáner y copihue vienen de otras lenguas; alunizar y pantallazo se crearon con piezas del castellano."),
        arith(PN + " En el cuadro hay 5 ejemplos de préstamos y 2 de neologismos. ¿Cuántos ejemplos hay en total?", "5+2", "Se suman los ejemplos de los dos grupos."),
        ex(PN + " ¿Cuántos préstamos del cuadro vienen de lenguas indígenas: 3 o 5?", "3", "Son guagua, palta y copihue.", "1+1+1"),
    ],
    Z=[
        ex("Un estudiante quiere inventar por su cuenta una palabra en mapuzugun para «computador». ¿Es lo correcto o conviene consultar al educador o a la comunidad que habla la lengua?", "consultar al educador o a la comunidad que habla la lengua", "Las palabras nuevas las acuerdan quienes hablan la lengua."),
        ex("Alguien dice: «El castellano que hablamos ya no es puro porque tiene guagua y palta». ¿Es correcto? Sí o No.", "No", "Todas las lenguas tienen préstamos y siguen siendo suyas."),
    ],
    D=[
        ex(PN + " Explica con una opción cómo ayudan los préstamos a expresarse. A) permiten nombrar cosas que antes no tenían nombre en esa lengua. B) obligan a dejar de hablar la lengua propia. Escribe la letra.", "A", "Los préstamos amplían las palabras disponibles."),
        ex("Un joven dice: «Si mi lengua incorpora un préstamo, entonces mi lengua está desapareciendo». ¿Qué respuesta es mejor: A) «las lenguas vivas toman y crean palabras» o B) «sí, es una mala señal»? Escribe la letra.", "A", "Tomar palabras es parte normal de toda lengua viva."),
    ],
    context=[ex("En tu casa alguien dice «guagua» para hablar de un bebé. Tu hermano dice que esa palabra no es castellano. ¿Qué le respondes: que es un préstamo del quechua usado en castellano o que está mal dicha?", "que es un préstamo del quechua usado en castellano", "Es una palabra de origen quechua que el castellano incorporó.")],
    selfcheck=[
        ex("¿«Alunizar» es un neologismo o un préstamo del inglés?", "un neologismo", "Se creó a partir de «luna»."),
        ex("¿Quién acuerda las palabras nuevas en una lengua indígena: una persona sola o quienes hablan la lengua?", "quienes hablan la lengua", "Es una decisión de la comunidad de hablantes."),
        ex("¿Una lengua viva cambia o nunca cambia?", "cambia", "Las lenguas vivas se renuevan."),
    ],
    task=T(
        "Lee este cuadro: «Palabras de uso cotidiano en Chile: choclo (del quechua), curanto (del mapuzugun), clic (del inglés), videollamada (palabra nueva formada con piezas del castellano).» En tu cuaderno escribe una tabla con tres columnas: palabra, tipo (préstamo o neologismo) y lengua de origen o piezas. Luego escribe dos oraciones que expliquen por qué incorporar palabras no hace menos auténtica a una lengua. No inventes palabras en lenguas indígenas.",
        "Choclo, préstamo, quechua. Curanto, préstamo, mapuzugun. Clic, préstamo, inglés. Videollamada, neologismo, «video» y «llamada». Explicación: «Todas las lenguas vivas toman palabras de otras y crean palabras nuevas. Eso las ayuda a expresar ideas actuales.»",
        ["clasifica correctamente las cuatro palabras", "indica lengua de origen o piezas", "explica por qué incorporar palabras no resta autenticidad", "no inventa palabras en lenguas indígenas"],
        ["tabla de tres columnas", "dos oraciones"],
        ["llamar neologismo a un préstamo", "inventar una palabra en una lengua indígena"],
        "Si dudó con una palabra, pídele que busque en el cuadro de qué lengua viene o con qué piezas se formó.",
    ),
    reinforce="Copia el cuadro de la clase y subraya con un color los préstamos y con otro los neologismos.",
    extend="Escribe una lista de cuatro palabras que usas en casa y averigua con una persona mayor si alguna viene de una lengua indígena.",
)

# ============================================================ LR05 clase 4 · explicación atribuida
FEX = "Ficha de explicación (inventada para practicar): Fuente: una educadora tradicional de la Escuela Ejemplo, del pueblo mapuche. Autorización: puede contarse en la sala. Dijo: «Cuando hacemos el taller de lengua, las niñas y los niños aprenden saludos y juegos. Usamos palabras que vienen del castellano, como «computador», cuando hablamos de cosas nuevas, y también usamos palabras de nuestra lengua que ya son parte del castellano de Chile. Esto nos ayuda a comunicar nuestras ideas. Hablo solo de mi escuela.»"

L(
    LR5, 4,
    materials="Lápiz y hoja. La ficha de explicación está escrita aquí y es inventada para practicar.",
    use="Aprenderé a escribir una explicación de cinco oraciones sobre el sentido de fortalecer una lengua, que atribuye la información a su fuente, da un ejemplo de préstamo o neologismo y declara el límite. Sirve para explicar sin inventar ni generalizar.",
    prior=["Sé qué significan revitalizar y fortalecer una lengua.", "Sé reconocer préstamos y neologismos."],
    explain=[
        "Una explicación atribuida tiene cinco partes. Primero nombra la fuente y la comunidad con «según». Segundo, dice qué hace la comunidad por su lengua. Tercero, da un ejemplo de préstamo o de neologismo. Cuarto, dice para qué sirve: cómo ayuda a comunicar ideas. Quinto, declara el límite: que la fuente habla solo de su caso.",
        "El ejemplo debe salir de la ficha o del cuadro de la clase, no de mi imaginación. Si la ficha dice que usan «computador» cuando hablan de cosas nuevas, puedo decir que es una palabra del castellano que se usa en el taller. No puedo agregar una palabra en lengua indígena que la ficha no entregó, porque no sé cómo se dice ni cómo se escribe.",
        "Para explicar el sentido, uso la razón que da la fuente: aprender y usar palabras, también las nuevas y las prestadas, ayuda a comunicar ideas en la comunidad y en otros lugares. Marco mi propia opinión con «yo pienso» y le pido a la educadora tradicional que lea mi explicación antes de darla por terminada.",
    ],
    vocab=[("explicación atribuida", "texto que dice de quién viene lo que explica"), ("comunicar", "hacer llegar una idea a otra persona"), ("ejemplo", "caso concreto que aclara una idea"), ("límite", "aviso de hasta dónde vale lo que se dice"), ("sentido", "razón o propósito de una acción")],
    worked=[
        W("Armar la primera oración", FEX + " Escribe una oración que nombre la fuente y la comunidad.", ["Tomo los datos de la ficha: educadora tradicional de la Escuela Ejemplo, pueblo mapuche.", "Empiezo con «Según…».", "Escribo la oración."], "Según una educadora tradicional de la Escuela Ejemplo, del pueblo mapuche, en el taller de lengua se aprenden saludos y juegos."),
        W("Elegir el ejemplo", FEX + " ¿Qué palabra de la ficha sirve de ejemplo de préstamo del castellano?", ["Busco una palabra que se use para hablar de cosas nuevas.", "La ficha menciona «computador».", "Es un ejemplo que la fuente dio."], "computador"),
    ],
    mistakes=[
        M("Agregar una palabra mapuzugun inventada como ejemplo de neologismo.", "No sé cómo se dice ni cómo se escribe, y las palabras nuevas se acuerdan entre hablantes.", "Uso solo los ejemplos de la ficha y anoto mi duda para la educadora."),
        M("Terminar la explicación sin el límite.", "Parece que la fuente habla de todas las escuelas.", "Cierro con «ella habla solo de su escuela»."),
    ],
    R=[
        ex(FEX + " ¿De qué escuela es la educadora de la ficha?", "de la Escuela Ejemplo", "La ficha la nombra."),
        ex(FEX + " ¿Qué aprenden las niñas y los niños en el taller de lengua?", "saludos y juegos", "La educadora lo dice."),
        ex(FEX + " ¿Qué palabra del castellano menciona la educadora para hablar de cosas nuevas?", "computador", "Está en la ficha."),
    ],
    C=[
        ex(FEX + " Según la educadora, ¿para qué ayuda usar palabras de distintos orígenes?", "comunicar sus ideas", "La ficha lo dice al final."),
        ex(FEX + " ¿Cuál es el límite que declara la educadora?", "habla solo de su escuela", "Ella cierra con esa frase."),
        ex(FEX + " Verdadero o falso: la ficha entrega una palabra nueva en mapuzugun para «computador».", "Falso", "La ficha no entrega ninguna palabra mapuzugun."),
    ],
    A=[
        ex("Ordena las cinco partes de la explicación. A) límite. B) ejemplo de préstamo o neologismo. C) fuente. D) para qué sirve. E) lo que hace la comunidad. Escribe las letras en orden.", "C, E, B, D, A", "Se parte por la fuente y se cierra con el límite."),
        ex(FEX + " Elige la mejor oración sobre el ejemplo. A) «Según la educadora, en el taller se usa «computador» para hablar de cosas nuevas.» B) «En todos los talleres de lengua se usa computador.» Escribe la letra.", "A", "Atribuye y no generaliza."),
        arith("Una explicación debe tener 5 partes. Un compañero escribió la fuente, lo que hace la comunidad y el ejemplo. ¿Cuántas partes le faltan?", "5-3", "Se restan las escritas de las cinco pedidas."),
    ],
    Z=[
        ex(FEX + " Una niña agrega: «y las niñas y niños del taller ya hablan perfecto». ¿Está en la ficha? Sí o No.", "No", "La ficha no mide cuánto hablan los niños."),
        ex(FEX + " Un niño escribe «yo pienso que aprender palabras nuevas nos ayuda a comunicarnos». ¿La idea está marcada como propia? Sí o No.", "Sí", "Empieza con «yo pienso»."),
    ],
    D=[
        ex(FEX + " Dos versiones del cierre. A) «La educadora habla solo de su escuela.» B) «Todas las escuelas mapuche hacen lo mismo.» ¿Cuál respeta el límite? Escribe la letra.", "A", "La B generaliza más allá de la ficha."),
        ex("Al revisar tu explicación notas que usaste una palabra en mapuzugun que no está en la ficha. ¿Qué haces: la dejas porque la viste en un video o la sacas y consultas a la educadora?", "la sacas y consultas a la educadora", "Una palabra que no entregó la fuente se consulta antes."),
    ],
    context=[ex("Tu curso presentará en una jornada de la escuela qué hace una comunidad por su lengua. Una persona mayor te dio permiso para contar su relato. ¿Empiezas diciendo «Según…» y su comunidad, o lo presentas como si fuera tu propia investigación?", "empiezas diciendo «Según…» y su comunidad", "Se atribuye la información a quien la entregó.")],
    selfcheck=[
        ex("¿Cuántas partes tiene la explicación atribuida de esta clase?", "5", "Fuente, acción, ejemplo, para qué sirve y límite."),
        ex("¿Puedo agregar una palabra en lengua indígena que no entregó la fuente? Sí o No.", "No", "No se inventa lengua; se consulta."),
        ex("¿Qué palabra marca una idea mía: «yo pienso» o «según»?", "yo pienso", "«Según» atribuye lo dicho a la fuente."),
    ],
    task=T(
        "Lee esta ficha inventada: «Fuente: un educador tradicional de la Escuela Muestra, pueblo rapa nui. Autorización: puede contarse en la sala. Dijo: «En el taller de lengua hacemos canciones nuevas con palabras del castellano y de nuestra lengua para hablar de las cosas de hoy. Eso ayuda a que las niñas y los niños quieran usar la lengua. Hablo solo de mi taller».» En tu cuaderno escribe una explicación de cinco oraciones con estas partes: fuente, lo que hace la comunidad, ejemplo tomado de la ficha, para qué sirve y límite. No agregues palabras en lengua que la ficha no tenga.",
        "Según un educador tradicional de la Escuela Muestra, del pueblo rapa nui, en el taller de lengua se hacen canciones nuevas. Se mezclan palabras del castellano y de su lengua para hablar de las cosas de hoy. Eso ayuda a que las niñas y los niños quieran usar la lengua. Él habla solo de su taller. Yo pienso que así la lengua se renueva.",
        ["nombra la fuente y el pueblo", "usa un ejemplo de la ficha", "explica para qué sirve", "declara el límite y marca lo propio"],
        ["explicación de cinco oraciones"],
        ["inventar palabras en lengua", "olvidar el límite"],
        "Pide que subraye en la ficha cada dato que usó; todo lo no subrayado debe llevar «yo pienso» o salir.",
    ),
    reinforce="Copia las cinco oraciones del ejemplo de la clase y rotula cada una con el número de su parte.",
    extend="Escribe una segunda explicación sobre el mismo taller que se dirija a las familias, con las mismas cinco partes.",
)
