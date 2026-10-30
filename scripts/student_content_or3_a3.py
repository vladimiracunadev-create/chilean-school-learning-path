"""Cuaderno del estudiante, 3.º básico Orientación: OA 05 (solidaridad, empatía, buen trato y rechazo de violencia) y OA 06 (resolución guiada de conflictos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA5, OA6 = "OR03 OA 05", "OR03 OA 06"


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 05
lesson(
    OA5, 1,
    "Una hoja y un lápiz. Los casos de personajes están escritos en los ejercicios. No necesitas contar nada tuyo.",
    "Aprenderé a ponerme en el lugar de otra persona sin hablar por ella. Sirve para entender mejor a los demás y tratarlos con respeto.",
    ["Sé que cada persona siente cosas distintas.", "Sé nombrar mis emociones."],
    [
        "La empatía es ponerte en el lugar de otra persona para entender cómo puede sentirse. Se hace mirando lo que pasa, escuchando y pensando: «¿Qué le habrá pasado?». La empatía no es sentir lo mismo que el otro ni arreglarle el problema. Es comprender y tratarlo con cuidado.",
        "Cuidado con hablar por otra persona. Si dices «yo sé que estás triste», puedes equivocarte. Mejor pregunta: «¿Cómo te sientes?» o «¿Quieres contarme?». Cada persona sabe lo que siente. Si no quiere contar, se respeta.",
        "Las personas pueden vivir lo mismo de manera distinta. Un ruido fuerte asusta a unos y a otros no. Una niña que llegó hace poco desde otro país o ciudad puede sentirse nerviosa en una sala nueva. Entender otra perspectiva ayuda a no burlarte y a acercarte con respeto. Todas las personas tienen derecho a opinar y a ser distintas, por ejemplo en sus gustos o en su forma de jugar, sin que nadie se burle.",
    ],
    [("empatía", "ponerme en el lugar de otro para entenderlo"), ("perspectiva", "la manera en que una persona ve algo"), ("respetar", "tratar con cuidado a otros"), ("suponer", "creer algo sin saberlo con seguridad"), ("preguntar", "pedir información a otra persona")],
    [
        W("Preguntar y no suponer", "Una compañera nueva está callada en el recreo. ¿Qué es mejor: decir «estás triste» o preguntar «¿quieres jugar con nosotros?»?", ["No sé cómo se siente.", "Una pregunta le da a ella la decisión.", "Preguntar respeta lo que siente."], "Preguntar «¿quieres jugar con nosotros?»"),
        W("Distintas perspectivas", "Un ruido fuerte asusta a Lalo, pero a Camila no. ¿Alguno siente algo incorrecto?", ["Cada persona reacciona distinto.", "Lo que siente cada uno es válido.", "Entenderlo es empatía."], "No, los dos sienten algo válido"),
    ],
    [
        M("Decir «yo sé cómo te sientes» sin preguntar.", "Se cree que la cara o la situación lo dicen todo.", "Pregunta y escucha; solo la persona sabe lo que siente."),
        M("Burlarme de quien reacciona distinto a mí.", "Se piensa que todos deberían sentir igual.", "Entiende que cada uno ve las cosas a su manera."),
    ],
    R=[
        ex("¿La empatía es ponerse en el lugar del otro?", "Sí", "Ayuda a entender cómo puede sentirse."),
        ex("Para saber cómo se siente alguien, ¿qué haces: adivinar o preguntar con respeto?", "Preguntar con respeto", "Solo la persona sabe lo que siente."),
        ex("¿Todas las personas sienten igual ante lo mismo?", "No", "Cada persona vive las cosas a su manera."),
    ],
    U=[
        ex("¿Por qué no conviene decir «yo sé que estás triste»?", "Porque puedo equivocarme", "No sabemos con seguridad lo que siente otro."),
        ex("Si alguien no quiere contar lo que siente, ¿qué haces?", "Lo respeto", "Cada uno decide qué cuenta."),
        ex("Un niño opina distinto del resto y le gusta jugar de otra manera. ¿Tiene derecho a ser así sin que se burlen?", "Sí", "Todos pueden opinar y ser diferentes, con respeto."),
    ],
    A=[
        ex("Una niña llegó hace dos días al curso y mira a todos sin hablar. Escribe una pregunta empática para ella.", "¿Quieres jugar con nosotros?", "Invita sin suponer cómo se siente."),
        ex("A Tomás le da miedo hablar adelante. Un compañero dice «es un cobarde». ¿Eso es empatía?", "No", "No intenta entender lo que Tomás siente."),
        ex("Elige la frase que no habla por el otro: «Tú estás enojado» o «¿Cómo estás?».", "«¿Cómo estás?»", "Pregunta y deja que la persona responda."),
    ],
    Z=[
        ex("Dos niñas ven a un compañero llorar. Una dice «seguro se cayó». La otra pregunta «¿puedo ayudarte?». ¿Cuál muestra empatía?", "La que pregunta si puede ayudar", "No supone y ofrece apoyo."),
        ex("Un niño dice: «Si yo no tengo miedo, nadie debería tenerlo». ¿Qué le falta entender?", "Que cada persona siente distinto", "Las emociones dependen de cada uno."),
    ],
    D=[
        arith("En un curso de 30 estudiantes, 3 llegaron este mes de otras ciudades. ¿Cuántos ya estaban antes?", "30-3", "Se resta los nuevos al total."),
        ex("Una niña recién llegada responde con timidez a las preguntas. ¿Es buena idea hablarle despacio y esperar su respuesta?", "Sí", "Le da tiempo y respeta su ritmo."),
    ],
    context=[ex("En el recreo, Nico ve que Mía está sola y le pregunta: «¿Cómo estás? ¿Quieres que juguemos?». Mía dice «hoy prefiero estar sola». Nico dice «está bien, aquí estaré si cambias de idea». ¿Fue empático?", "Sí", "Preguntó y respetó su respuesta.")],
    selfcheck=[ex("En Orientación: ¿puedo adivinar con seguridad lo que siente otro?", "No", "Debo preguntar con respeto."), ex("¿La empatía ayuda a convivir mejor?", "Sí", "Hace que trates con cuidado."), ex("¿Cada persona ve las cosas a su manera?", "Sí", "Existen perspectivas distintas.")],
    task=T("Lee el caso: una niña llegó de otra ciudad y en el recreo se queda mirando cómo juegan. Escribe dos preguntas empáticas que podrías hacerle y una cosa que no dirías porque hablaría por ella. Puedes usar la frase «¿Cómo estás?».", "Preguntas: «¿Cómo estás?», «¿Quieres jugar?». No diría «seguro estás triste».", ["dos preguntas respetuosas", "una frase que no diría y por qué", "no habla por ella"], ["respuestas escritas"], ["suponer lo que siente", "burlarse de su timidez"], "Reconoce las preguntas y revisa que no supongan nada."),
    reinforce="Escribe dos maneras de preguntar a alguien cómo se siente.",
    extend="Elige un personaje de un cuento y explica cómo pudo sentirse sin hablar por él.",
)

lesson(
    OA5, 2,
    "Una hoja y un lápiz. Las frases están escritas en los ejercicios. Puedes practicarlas en parejas.",
    "Aprenderé a practicar un buen trato que se vea y se escuche: saludar, despedirme, pedir por favor y agradecer. Sirve para que la sala sea un lugar agradable donde se aprende.",
    ["Sé saludar.", "Sé esperar mi turno."],
    [
        "El buen trato es tratar a los demás con respeto y amabilidad. Se nota en lo que haces y dices: saludar al llegar, despedirte al irte, pedir «por favor», decir «gracias», esperar tu turno y escuchar sin interrumpir. También se nota en el tono de voz y en los gestos, no solo en las palabras.",
        "El buen trato también cuida el lugar donde aprendemos. Eso significa hablar con voz adecuada, no interrumpir a quien trabaja, cuidar los materiales y mantener la sala ordenada. Así todos se pueden concentrar.",
        "Un buen trato no es obedecer sin pensar ni callar si algo te molesta. Puedes decir «no me gusta eso» con respeto. El buen trato se da en los dos sentidos: tú tratas bien y mereces buen trato.",
    ],
    [("buen trato", "tratar a otros con respeto y amabilidad"), ("saludar", "decir hola a otra persona"), ("agradecer", "decir gracias"), ("turno", "momento que me toca"), ("ambiente de aprendizaje", "lugar donde todos pueden estudiar y concentrarse")],
    [
        W("Pedir con buen trato", "Nico necesita un lápiz. ¿Qué dice con buen trato: «Dame un lápiz» o «¿Me prestas un lápiz, por favor?»?", ["La primera es una orden.", "La segunda pide con respeto.", "Usa «por favor»."], "«¿Me prestas un lápiz, por favor?»"),
        W("Cuidar el ambiente", "En clase, Rita termina antes y quiere conversar. ¿Qué hace con buen trato?", ["Otros siguen trabajando.", "Conversar fuerte los molesta.", "Espera en silencio o lee."], "Espera en silencio o lee"),
    ],
    [
        M("Creer que el buen trato es solo decir «por favor».", "Se miran las palabras y no los gestos ni el tono.", "También importa el tono, esperar y escuchar."),
        M("Callar si algo me molesta para ser «educado».", "Se confunde respeto con aguantar.", "Puedes decir «no me gusta eso» con respeto."),
    ],
    R=[
        ex("¿Saludar al llegar es buen trato?", "Sí", "Muestra respeto por los demás."),
        ex("¿Decir «gracias» es agradecer?", "Sí", "Reconoce lo que otro hizo."),
        ex("¿Esperar tu turno es buen trato?", "Sí", "Respeta a quienes están antes."),
    ],
    U=[
        ex("¿Por qué importa el tono de voz?", "Porque puede cambiar cómo se recibe un mensaje", "Un tono duro puede lastimar."),
        ex("¿Hablar bajo mientras otros trabajan cuida el ambiente?", "Sí", "Ayuda a que todos se concentren."),
        ex("¿Se puede decir «no me gusta eso» con buen trato?", "Sí", "Se dice con respeto y sin agredir."),
    ],
    A=[
        ex("Escribe una frase para pedir una hoja con buen trato.", "¿Me das una hoja, por favor?", "Usa «por favor» y pregunta."),
        ex("Un compañero te presta un borrador. Escribe qué dices.", "Gracias por prestarme el borrador", "Es una forma de agradecer."),
        ex("Elige la despedida con buen trato: «Ya me voy, no me molesten» o «Hasta mañana, que estén bien».", "«Hasta mañana, que estén bien»", "Es amable y cuida al grupo."),
    ],
    Z=[
        ex("Dos niños piden lo mismo: uno grita «¡Dame!» y el otro dice «¿Puedo, por favor?». ¿Quién mostró mejor trato?", "El que dijo «¿Puedo, por favor?»", "Pidió con respeto."),
        ex("Una niña dice «no me gusta que me interrumpan» con voz tranquila. ¿Eso es buen trato?", "Sí", "Se expresa con respeto."),
    ],
    D=[
        arith("En una semana, un curso practicó saludar 5 veces por día durante 4 días. ¿Cuántos saludos hubo?", "5*4", "Se repite cinco veces cuatro días."),
        ex("En el patio, alguien espera su turno en la fila y otro se adelanta. ¿Quién trata bien?", "El que espera su turno", "Respeta a los demás."),
    ],
    context=[ex("Al entrar a la sala, Marta dice «buenos días» y deja su mochila en su lugar. Al irse dice «hasta mañana». ¿Practica buen trato?", "Sí", "Saluda, se despide y cuida el orden.")],
    selfcheck=[ex("En Orientación: ¿el tono de voz es parte del buen trato?", "Sí", "Puede cuidar o lastimar."), ex("¿Interrumpir a quien trabaja cuida el ambiente?", "No", "Rompe la concentración."), ex("¿Puedo decir lo que me molesta con respeto?", "Sí", "El buen trato va en dos sentidos.")],
    task=T("Escribe cuatro frases con buen trato: una para saludar, una para pedir algo, una para agradecer y una para despedirte. Elige un lugar: la sala, el patio o la biblioteca. Practica las frases con un compañero o frente al espejo, cuidando el tono.", "Sala: «Buenos días». «¿Me prestas una regla, por favor?». «Gracias». «Hasta mañana».", ["cuatro frases amables", "usa por favor o gracias", "cuida el tono"], ["frases escritas o actuadas"], ["órdenes sin respeto", "solo palabras sin tono"], "Reconoce el buen trato y revisa el tono de voz."),
    reinforce="Anota dos veces hoy en que usaste «por favor» o «gracias».",
    extend="Inventa una regla de la sala para cuidar el ambiente de aprendizaje.",
)

lesson(
    OA5, 3,
    "Una hoja y un lápiz. Los casos de ayuda están escritos en los ejercicios.",
    "Aprenderé a ayudar a quien lo necesita sin hacerlo por él o ella y sin pasar por encima de lo que quiere. Sirve para ser solidario con respeto.",
    ["Sé que puedo ayudar a otros.", "Sé preguntar con respeto."],
    [
        "La solidaridad es ayudar a quien lo necesita y preocuparte por el bien del grupo. Ayudar puede ser compartir, acompañar, avisar a un adulto o enseñar. Todas las personas, tú también, necesitamos ayuda alguna vez. Ayudar no te hace mejor que nadie.",
        "Ayudar bien tiene dos pasos. Primero, pregunta: «¿Quieres ayuda?». A veces la persona prefiere hacerlo sola, y eso se respeta. Segundo, ayuda a que la persona pueda, sin hacerlo todo por ella. No es ayuda quitarle algo de las manos, ni hacer que se sienta menos.",
        "Si ves que alguien tiene un problema serio, como que lo están lastimando o se siente muy mal, tu ayuda es avisar a un adulto de confianza. No tienes que resolverlo solo. Avisar no es acusar.",
    ],
    [("solidaridad", "ayudar a quien lo necesita y cuidar al grupo"), ("ayuda", "apoyo que doy a otra persona"), ("respetar", "tomar en cuenta lo que el otro quiere"), ("sustituir", "hacer algo en lugar de otra persona"), ("avisar", "contar a un adulto para que ayude")],
    [
        W("Preguntar antes de ayudar", "Una compañera tiene un brazo enyesado y carga libros. ¿Qué haces primero?", ["No debes quitarle los libros.", "Le preguntas si quiere ayuda.", "Haces lo que ella te diga."], "Preguntar «¿quieres ayuda?»"),
        W("Ayudar sin hacerlo todo", "Beto no entiende un ejercicio. ¿Qué es mejor: hacerlo por él o explicarle el primer paso?", ["Hacerlo por él no lo ayuda a aprender.", "Explicar el primer paso lo deja avanzar.", "Elige explicar."], "Explicarle el primer paso"),
    ],
    [
        M("Hacer la tarea de otro «para ayudarlo».", "Se confunde ayudar con sustituir.", "Ayuda a que lo pueda hacer él o ella."),
        M("Ayudar a alguien sin preguntarle.", "Se cree que siempre quiere ayuda.", "Pregunta primero y acepta si dice no."),
    ],
    R=[
        ex("¿Antes de ayudar conviene preguntar?", "Sí", "La otra persona puede preferir hacerlo sola."),
        ex("¿Avisar a un adulto cuando alguien está en peligro es una forma de ayudar?", "Sí", "No tienes que resolverlo solo."),
        ex("¿Ayudar te hace mejor que otros?", "No", "Todos necesitamos ayuda alguna vez."),
    ],
    U=[
        ex("¿Qué es sustituir a una persona?", "Hacer algo en lugar de ella", "No deja que la persona aprenda o decida."),
        ex("Si alguien dice «prefiero hacerlo yo», ¿qué haces?", "Respeto lo que dice", "Cada uno decide cuándo necesita ayuda."),
        ex("¿Compartir tus lápices con quien no tiene es solidaridad?", "Sí", "Ayuda a alguien que lo necesita."),
    ],
    A=[
        ex("Escribe una pregunta para ofrecer ayuda a un compañero que no puede abrir su mochila.", "¿Quieres que te ayude?", "Ofrece sin imponer."),
        ex("Rita no entiende cómo se resuelve una suma. ¿Cuál es mejor ayuda: darle el resultado o mostrarle cómo contar?", "Mostrarle cómo contar", "Le permite aprender."),
        ex("Un compañero se cae y se lastima. ¿A quién avisas?", "A un adulto", "El adulto puede ayudar con seguridad."),
    ],
    Z=[
        ex("Una niña ayuda a un niño más pequeño a atarse los cordones haciéndolo ella. ¿Qué podría hacer para que él aprenda?", "Enseñarle los pasos y dejar que lo intente", "Ayudar es dejar que la persona pueda."),
        ex("Pedro ayuda a una compañera y luego cuenta a todo el curso que ella no sabía hacer el trabajo. ¿Respetó a su compañera?", "No", "La dejó expuesta ante todos sin que ella lo quisiera."),
    ],
    D=[
        arith("Un curso junta 12 cuadernos y otro curso 18 para una campaña. ¿Cuántos cuadernos juntaron entre los dos?", "12+18", "Se suman los cuadernos de ambos cursos."),
        ex("En un grupo, un niño nunca pide ayuda y trabaja solo. ¿Está mal pedir ayuda?", "No", "Pedir ayuda es una forma de cuidarse."),
    ],
    context=[ex("Una compañera con el brazo enyesado carga una caja pesada. Tomás le pregunta: «¿Te ayudo?». Ella dice «sí, por favor» y cargan juntos. ¿Ayudó con respeto?", "Sí", "Preguntó primero y colaboró con ella.")],
    selfcheck=[ex("En Orientación: ¿ayudar significa quitarle el trabajo a otro?", "No", "Es acompañar para que pueda."), ex("¿Puedo avisar a un adulto para ayudar?", "Sí", "A veces es lo mejor."), ex("¿Hay que preguntar antes de ayudar?", "Sí", "Se respeta lo que el otro quiere.")],
    task=T("Lee los casos: (1) un niño no encuentra su lápiz, (2) una niña carga mucho peso, (3) un compañero está solo y triste en el patio. Para cada uno escribe qué le preguntarías y qué ayuda ofrecerías sin hacerlo por él o ella. Si es serio, escribe a qué adulto avisarías.", "(1) «¿Quieres que busquemos juntos?». (2) «¿Te ayudo a cargar?». (3) «¿Quieres jugar?»; si sigue mal, aviso a una profesora.", ["pregunta antes de ayudar", "ofrece ayuda que no sustituye", "nombra a quién avisar en lo serio"], ["respuestas escritas"], ["hacer todo por el otro", "ayudar sin preguntar"], "Reconoce la pregunta y verifica que no sustituya al otro."),
    reinforce="Escribe tres formas distintas de ayudar a alguien.",
    extend="Explica la diferencia entre ayudar y hacer por el otro con un ejemplo de tu elección.",
)

lesson(
    OA5, 4,
    "Una hoja y un lápiz. Los casos están escritos en los ejercicios. Usa personajes; nadie tiene que contar lo que le ha pasado.",
    "Aprenderé a reconocer la violencia y la discriminación y a rechazarlas con seguridad. Sirve para cuidar a otros y a mí.",
    ["Sé que nadie debe ser tratado mal.", "Sé que puedo pedir ayuda."],
    [
        "La violencia es dañar a alguien a propósito, con golpes, empujones, insultos, burlas, amenazas o dejándolo afuera una y otra vez. La violencia no es un juego ni «cosa de iguales». Si pasa muchas veces, o si alguien tiene más poder o fuerza, es más grave.",
        "La discriminación es tratar peor a una persona solo por quien es: por su etnia, su género, su religión, su nacionalidad, su manera de hablar u otras características. Por ejemplo, burlarse del apellido de un niño o no dejar jugar a una niña por ser niña. Todas las personas tienen los mismos derechos.",
        "Si ves o vives violencia, rechazarla es posible. Puedes decir «para, eso no está bien», alejarte y avisar a un adulto de confianza. No te quedes callado ni hagas lo mismo de vuelta. Si te pasa a ti, no es tu culpa. Avisar no es acusar.",
    ],
    [("violencia", "dañar a alguien a propósito"), ("discriminación", "tratar peor a alguien por quien es"), ("etnia", "pueblo o grupo con una cultura común"), ("derecho", "algo que todas las personas merecen"), ("testigo", "persona que ve lo que ocurre")],
    [
        W("Violencia o desacuerdo", "Dos niños quieren usar el mismo balón y se ponen de acuerdo en turnos. Otro niño empuja y se ríe de uno una y otra vez. ¿Cuál es violencia?", ["El primer caso es un desacuerdo que se resolvió.", "Empujar y reírse una y otra vez daña a propósito.", "Eso es violencia."], "Empujar y reírse una y otra vez"),
        W("Discriminar", "Unos niños no dejan jugar a una niña porque llegó de otro país. ¿Es discriminación?", ["La tratan peor por su nacionalidad.", "No hay otra razón.", "Es discriminación."], "Sí, es discriminación"),
    ],
    [
        M("Pensar que la violencia entre compañeros es solo «juego de iguales».", "Se confunde un desacuerdo con dañar a alguien.", "Si daña o se repite, no es juego; pide ayuda."),
        M("Responder con violencia a la violencia.", "Se cree que así se frena.", "Di «para», aléjate y avisa a un adulto."),
    ],
    R=[
        ex("¿Insultar a alguien muchas veces es violencia?", "Sí", "Daña a propósito."),
        ex("¿Tratar peor a alguien por su nacionalidad es discriminación?", "Sí", "Se le trata peor por quien es."),
        ex("Si ves violencia, ¿es bueno avisar a un adulto?", "Sí", "Pedir ayuda protege."),
    ],
    U=[
        ex("¿En qué se diferencia un desacuerdo de la violencia?", "En que la violencia daña a propósito", "Un desacuerdo se puede resolver sin dañar."),
        ex("¿Todas las personas tienen los mismos derechos, sin importar su etnia o religión?", "Sí", "Los derechos son iguales para todos."),
        ex("Si te hacen sentir mal, ¿es tu culpa?", "No", "La responsabilidad es de quien daña."),
    ],
    A=[
        ex("Un compañero se burla del apellido de otro. ¿Qué frase puedes decir para rechazarlo?", "Para, eso no está bien", "Es corta y clara."),
        ex("¿Cómo clasificas «dejar fuera del juego a una niña por ser niña»: discriminación o desacuerdo?", "Discriminación", "La tratan peor por ser quien es."),
        ex("Si ves a alguien que sufre golpes, ¿qué haces primero: pegar a quien golpea o avisar a un adulto?", "Avisar a un adulto", "Es más seguro y ayuda de verdad."),
    ],
    Z=[
        ex("Dos niños dicen: «Esto es solo una broma». Pero el otro llora y pide que paren. ¿Es una broma?", "No", "Si daña y la persona pide parar, no es broma."),
        ex("Alguien dice «yo no hice nada, solo miré». ¿Mirar sin hacer nada ayuda a quien sufre?", "No, hay que parar, alejarse o avisar", "Un testigo puede ayudar si avisa."),
    ],
    D=[
        arith("En un curso de 25 estudiantes, 4 fueron testigos de una burla y avisaron. ¿Cuántos no avisaron?", "25-4", "Se resta los que avisaron al total."),
        ex("Un adulto no escucha cuando cuentas algo grave. ¿Qué haces?", "Sigo contando a otro adulto de confianza", "Hasta que alguien me ayude."),
    ],
    context=[ex("En el recreo, un grupo se ríe del acento de un niño nuevo. Una niña dice «para» y le cuenta a una profesora. ¿Rechazó la discriminación?", "Sí", "Lo detuvo y pidió ayuda.")],
    selfcheck=[ex("En Orientación: ¿la violencia es dañar a propósito?", "Sí", "Esa es su idea central."), ex("¿Puedo avisar a un adulto si hay violencia?", "Sí", "Avisar no es acusar."), ex("¿Todas las personas merecen buen trato?", "Sí", "Los derechos son para todos.")],
    task=T("Lee tres casos: (1) un niño amenaza a otro todos los días, (2) alguien se burla del apellido de una niña, (3) dos amigos discuten por un balón y acuerdan turnos, sin dañar a nadie. Marca cuál es violencia, cuál discriminación y cuál un desacuerdo. Después escribe una frase para rechazar y a quién avisarías.", "(1) violencia; (2) discriminación; (3) desacuerdo. Frase: «Para, eso no está bien». Aviso a una profesora.", ["clasifica los tres casos", "propone una frase para rechazar", "nombra a quién avisar"], ["tabla o frases escritas"], ["confundir desacuerdo y violencia", "responder con violencia"], "Reconoce la clasificación y verifica que no sugiera violencia."),
    reinforce="Escribe una frase corta para rechazar un trato injusto.",
    extend="Explica por qué «es solo una broma» no justifica dañar.",
)

lesson(
    OA5, 5,
    "Una hoja y un lápiz. Los casos están escritos en los ejercicios. Puedes trabajar con un personaje.",
    "Aprenderé a incluir a otros y a reparar un daño con seguridad. Sirve para que todos se sientan parte del grupo.",
    ["Sé rechazar la violencia.", "Sé que hay que respetar los derechos de todos."],
    [
        "Incluir es hacer que todas las personas puedan participar. Se puede incluir invitando a jugar, ajustando las reglas del juego para que todos puedan, cambiando de lugar o preguntando. Incluir también es respetar si alguien dice «hoy no quiero». Se invita, no se obliga.",
        "Reparar es hacer algo para arreglar un daño. Si lastimaste a alguien, puedes reconocer lo que hiciste, decir «lo siento» y preguntar cómo ayudar. Reparar es hacerse cargo y no repetirlo. Si alguien te lastimó, puedes pedir que repare, pero no estás obligado a perdonar ni a ser amigo enseguida.",
        "Con situaciones de violencia grave o repetida, la reparación se hace con un adulto presente. No se obliga a nadie a reconciliarse. Lo importante es que nadie corra peligro.",
    ],
    [("inclusión", "hacer que todos puedan participar"), ("invitar", "ofrecer a alguien ser parte"), ("reparar", "hacer algo para arreglar un daño"), ("perdonar", "dejar de guardar rabia hacia quien me dañó"), ("seguridad", "estar sin peligro")],
    [
        W("Incluir en el juego", "En un juego de pelota, Sol no puede correr rápido. ¿Cómo se puede incluir para que juegue?", ["Pregunta qué le acomoda.", "Cambiar la regla: todos caminan.", "Así todos participan."], "Cambiar la regla para que todos puedan jugar"),
        W("Reparar un daño", "Ema rompió sin querer el dibujo de Joaquín. ¿Cómo repara?", ["Reconoce lo que pasó.", "Dice «lo siento».", "Le ofrece ayudar a rehacerlo."], "Reconocer, decir lo siento y ofrecer ayuda"),
    ],
    [
        M("Pensar que reparar es solo decir «perdón».", "Se cree que la palabra arregla todo.", "Reparar es hacer algo para arreglar el daño."),
        M("Obligar a alguien a ser amigo de quien le hizo daño.", "Se piensa que reconciliarse lo arregla todo.", "Nadie está obligado a perdonar; se cuida la seguridad."),
    ],
    R=[
        ex("¿Incluir es hacer que todos puedan participar?", "Sí", "Nadie queda afuera."),
        ex("¿Reparar es arreglar el daño que hice?", "Sí", "Se hace algo concreto."),
        ex("¿Se puede obligar a alguien a perdonar?", "No", "Cada persona decide."),
    ],
    U=[
        ex("Si alguien dice «hoy no quiero jugar», ¿qué haces?", "Lo respeto y lo invito otro día", "Se invita y no se obliga."),
        ex("Nombra los tres pasos para reparar un daño.", "Reconocer lo que pasó, decir lo siento y ayudar", "Estos pasos arreglan el daño."),
        ex("En situaciones de violencia grave, ¿con quién se repara?", "Con un adulto presente", "Así nadie corre peligro."),
    ],
    A=[
        ex("Escribe una frase para invitar a una niña que está sola.", "¿Quieres jugar con nosotros?", "Invita sin obligar."),
        ex("Cambia una regla para incluir a quien no corre rápido: «todos corren» por…", "Todos caminan rápido o hacen turnos", "Todos pueden participar."),
        ex("Elige la reparación que arregla: «decir perdón y seguir» o «decir lo siento y ayudar a rehacer el trabajo».", "«Decir lo siento y ayudar a rehacer el trabajo»", "Hace algo concreto."),
    ],
    Z=[
        ex("Un niño es amenazado cada día. Le dicen «hagan las paces ya». ¿Es seguro obligar a eso?", "No", "Hay peligro y no se debe forzar."),
        ex("Una niña no quiere ser amiga de quien la lastimó. ¿Hizo algo malo?", "No", "Puede decidir con quién estar."),
    ],
    D=[
        arith("En una fiesta del curso, 9 niños jugaron a las cartas, 7 a la pelota y 6 a dibujar. ¿Cuántos niños participaron?", "9+7+6", "Se suman todos los que jugaron."),
        ex("Si un grupo cambia las reglas del juego para que todos participen, ¿está practicando la inclusión?", "Sí", "Ajusta para que nadie quede afuera."),
    ],
    context=[ex("En el curso, Beto empujó a Lola sin querer. Dijo «perdón, te empujé; ¿te ayudo a levantarte?». Lola dijo «sí». ¿Reparó?", "Sí", "Reconoció, se disculpó y ayudó.")],
    selfcheck=[ex("En Orientación: ¿se obliga a alguien a perdonar?", "No", "Cada uno decide."), ex("¿Se puede cambiar una regla para incluir a todos?", "Sí", "La inclusión ajusta."), ex("¿Reparar incluye hacer algo?", "Sí", "No basta con decir perdón.")],
    task=T("Lee dos casos: (1) a Sol no la dejan jugar porque corre lento; (2) Eli rompió sin querer el trabajo de Rafa. Para cada uno escribe qué harías para incluir o reparar. Agrega una frase que respete si la persona dice «hoy no».", "(1) Cambiar la regla: todos caminan y Sol juega. (2) «Lo siento, rompí tu trabajo; te ayudo a hacerlo de nuevo». Frase: «Está bien, otro día».", ["propone una inclusión concreta", "propone una reparación concreta", "respeta un «hoy no»"], ["frases escritas"], ["obligar a reconciliarse", "reparar solo con la palabra perdón"], "Reconoce las acciones y verifica que no obligue a nadie."),
    reinforce="Escribe una regla que haga a un juego más inclusivo.",
    extend="Escribe cómo sería una reparación cuando alguien no quiere perdonar todavía.",
)

# ================================================================ OA 06
lesson(
    OA6, 1,
    "Una hoja y un lápiz. Los casos de conflicto están escritos en los ejercicios. No tienes que contar uno propio.",
    "Aprenderé a separar lo que pasó, lo que creo, lo que siento y lo que necesito en un conflicto. Sirve para entender a los dos lados antes de buscar solución.",
    ["Sé que las personas pueden pensar distinto.", "Sé nombrar mis emociones."],
    [
        "Un conflicto es un desacuerdo entre personas que quieren cosas distintas. Es normal y puede resolverse sin dañar. Para entenderlo, conviene separar cuatro cosas. Los hechos: lo que pasó y se puede observar. Las interpretaciones: lo que cada uno cree que significa. Las emociones: lo que sintió. Y las necesidades: lo que cada uno quiere o necesita.",
        "Por ejemplo, Ana y Beto quieren el mismo columpio. Hecho: Ana llegó primero y Beto se subió. Interpretación de Ana: «Beto me lo quitó a propósito». Emoción: rabia. Necesidad: jugar un rato. Beto puede tener otra interpretación, como «no la vi». Cada uno tiene su perspectiva.",
        "Antes de buscar un culpable, intenta entender a los dos. Cuando separas hechos de interpretaciones, el conflicto baja de tamaño. Si hay golpes, amenazas o miedo, no es un conflicto entre iguales: se avisa a un adulto.",
    ],
    [("conflicto", "desacuerdo entre personas que quieren cosas distintas"), ("hecho", "lo que pasó y se puede observar"), ("interpretación", "lo que creo que significa lo que pasó"), ("necesidad", "lo que una persona necesita o quiere"), ("perspectiva", "la manera en que cada uno ve el conflicto")],
    [
        W("Hecho o interpretación", "«Beto se subió al columpio cuando Ana lo estaba esperando» y «Beto me lo quitó a propósito». ¿Cuál es el hecho?", ["Un hecho se puede observar.", "«A propósito» es lo que Ana cree.", "El hecho es lo primero."], "«Beto se subió al columpio cuando Ana lo estaba esperando»"),
        W("Necesidad", "Ana dice: «Quiero usar el columpio un rato». ¿Qué parte es la necesidad?", ["Es lo que ella quiere.", "Quiere jugar un rato.", "No dice culpa de nadie."], "Usar el columpio un rato"),
    ],
    [
        M("Buscar al culpable antes de entender qué pasó.", "Queremos defendernos rápido.", "Separa hechos, interpretaciones, emociones y necesidades de los dos."),
        M("Creer que mi versión es la única.", "Se olvida que el otro vio otra cosa.", "Escucha la perspectiva del otro."),
    ],
    R=[
        ex("¿Un hecho se puede observar?", "Sí", "Se ve o se escucha."),
        ex("¿Una interpretación es lo que creo que significa algo?", "Sí", "Puede ser verdad o no."),
        ex("¿Todo conflicto es un problema grave?", "No", "Muchos conflictos son normales y se resuelven."),
    ],
    U=[
        ex("¿Por qué conviene entender a los dos antes de buscar culpables?", "Porque cada uno tiene su perspectiva", "Así se ve el conflicto completo."),
        ex("Si hay golpes o amenazas, ¿es un conflicto entre iguales que se resuelve solo?", "No, se avisa a un adulto", "Hay violencia y riesgo."),
        ex("¿La emoción es parte del conflicto?", "Sí", "Lo que sentimos influye en cómo actuamos."),
    ],
    A=[
        ex("¿Cuál es el hecho: «Julia me ignoró» o «Julia no contestó cuando le hablé»?", "«Julia no contestó cuando le hablé»", "Describe lo que pasó, no lo que creo."),
        ex("¿Cómo clasificas «me dio rabia»: hecho, emoción o necesidad?", "Emoción", "Dice lo que sentí."),
        ex("Pedro dice «necesito que me devuelvan mi lápiz». ¿Es una necesidad?", "Sí", "Dice lo que necesita."),
    ],
    Z=[
        ex("Dos niños cuentan el mismo hecho con interpretaciones distintas: uno dice «lo hizo a propósito» y el otro «fue sin querer». ¿Cómo se puede saber?", "Preguntando a los dos", "Cada uno puede explicar su perspectiva."),
        ex("Una niña dice: «Seguro quiere pelear conmigo». ¿Eso es un hecho?", "No", "Es una interpretación."),
    ],
    D=[
        arith("Un grupo anotó 7 hechos y 5 interpretaciones sobre un conflicto. ¿Cuántas cosas anotó en total?", "7+5", "Se suman los hechos y las interpretaciones."),
        ex("En una lista hay: «me quitó el lápiz», «lo hizo para molestarme», «me dio rabia», «necesito mi lápiz». ¿Cuántos son hechos?", "1", "Solo «me quitó el lápiz» se puede observar."),
    ],
    context=[ex("Dos niños discuten por una pelota. La profesora pregunta: «¿Qué pasó? ¿Qué sintieron? ¿Qué necesitan?». ¿Está separando hechos, emociones y necesidades?", "Sí", "Ordena el conflicto en partes.")],
    selfcheck=[ex("En Orientación: ¿un conflicto es siempre malo?", "No", "Es un desacuerdo normal."), ex("¿Una interpretación puede ser distinta en cada persona?", "Sí", "Cada uno ve distinto."), ex("¿Hay que buscar culpables primero?", "No", "Primero se entiende.")],
    task=T("Lee: «Lola y Mario querían el mismo libro. Mario lo tomó primero. Lola se enojó y dijo que Mario es egoísta». Escribe en cuatro columnas o frases: un hecho, una interpretación, una emoción y una necesidad de Lola. Si quieres, hazlo también para Mario.", "Hecho: Mario tomó el libro primero. Interpretación: es egoísta. Emoción: enojo. Necesidad: leer el libro.", ["cuatro partes bien separadas", "la interpretación se marca como lo que ella cree", "no culpa a nadie"], ["tabla o frases escritas"], ["mezclar hechos con interpretaciones", "buscar culpables"], "Reconoce la separación y revisa que el hecho sea observable."),
    reinforce="Escribe un hecho y una interpretación de algo que viste hoy.",
    extend="Elige un conflicto de un cuento y sepáralo en hechos, interpretaciones, emociones y necesidades.",
)

lesson(
    OA6, 2,
    "Una hoja y un lápiz. Los diálogos están escritos en los ejercicios. Puedes practicarlos en parejas.",
    "Aprenderé a escuchar al otro y a decir lo que yo siento y necesito sin culpar. Sirve para que los dos lados se entiendan.",
    ["Sé separar hechos y emociones.", "Sé hacer una pausa."],
    [
        "Escuchar bien en un conflicto significa mirar a la persona, no interrumpir y entender lo que necesita. Después puedes reformular: decir con tus palabras lo que entendiste. Por ejemplo: «Entiendo que te enojaste porque necesitabas el libro». Así el otro sabe que lo escuchaste.",
        "Cuando hablas tú, usa un mensaje en primera persona: «Yo me sentí… cuando… porque necesito…». Por ejemplo: «Me sentí mal cuando tomaste el libro sin preguntar, porque necesito leerlo». No dice «tú eres egoísta». Dice lo que pasó, lo que sientes y lo que necesitas.",
        "Reformular y hablar en primera persona no significa que estés de acuerdo con todo. Significa que entiendes y te explicas con respeto. Después se buscan opciones. Si hay miedo o amenazas, se pide ayuda a un adulto.",
    ],
    [("reformular", "decir con mis palabras lo que entendí"), ("mensaje en primera persona", "frase que empieza con lo que yo siento o necesito"), ("acusar", "decir que alguien es culpable"), ("escuchar", "poner atención sin interrumpir"), ("necesito", "palabra para decir lo que quiero lograr")],
    [
        W("Mensaje en primera persona", "Reescribe «tú eres un egoísta» como mensaje en primera persona para Mario, que tomó el libro sin preguntar.", ["Cuenta qué pasó: tomó el libro sin preguntar.", "Di lo que sientes.", "Di lo que necesitas."], "Me sentí mal cuando tomaste el libro sin preguntar; necesito leerlo"),
        W("Reformular", "Mario dice: «Yo no sabía que querías ese libro». ¿Cuál es una reformulación: «Mientes» o «Entiendo que no sabías que lo querías»?", ["Reformular repite lo que entendí.", "«Mientes» acusa.", "La segunda muestra escucha."], "«Entiendo que no sabías que lo querías»"),
    ],
    [
        M("Empezar con «tú siempre…» o «tú eres…».", "Parece una forma de defenderse.", "Empieza con «yo me sentí…» y di lo que necesitas."),
        M("Interrumpir para dar mi versión.", "Siento que si no hablo ahora pierdo.", "Espera tu turno y luego reformula."),
    ],
    R=[
        ex("¿Escuchar bien incluye no interrumpir?", "Sí", "Permite entender al otro."),
        ex("¿Reformular es decir con mis palabras lo que entendí?", "Sí", "Muestra que escuché."),
        ex("¿Un mensaje en primera persona empieza con «yo me sentí»?", "Sí", "Habla de mí y no acusa."),
    ],
    U=[
        ex("¿Por qué conviene decir «yo me sentí…» y no «tú eres…»?", "Porque no acusa y dice lo que siento", "Así el otro puede escuchar."),
        ex("Reformular lo que dijo el otro, ¿significa estar de acuerdo?", "No", "Significa entender su versión."),
        ex("Si hay amenazas en el conflicto, ¿se resuelve con un mensaje en primera persona?", "No, se pide ayuda a un adulto", "Hay riesgo y no es un desacuerdo simple."),
    ],
    A=[
        ex("Reformula: «Estoy enojada porque nadie me eligió para el equipo».", "Entiendo que estás enojada porque no te eligieron para el equipo", "Repite lo que entendió sin juzgar."),
        ex("Escribe un mensaje en primera persona: te interrumpieron cuando hablabas y necesitas terminar.", "Me sentí mal cuando me interrumpieron; necesito terminar de hablar", "Usa «me sentí» y «necesito»."),
        ex("Elige la frase que escucha: «Cállate, ya sé» o «Cuéntame más».", "«Cuéntame más»", "Invita a seguir hablando."),
    ],
    Z=[
        ex("Dos niños: uno dice «tú siempre te adelantas» y otro «me sentí mal cuando te adelantaste, necesito mi turno». ¿Cuál ayuda más al diálogo?", "El segundo", "Dice lo que siente y necesita sin acusar."),
        ex("Una niña reformula y su compañero dice «sí, eso es». ¿Qué logró?", "Que se sintiera escuchado", "Entendió lo que el otro quiso decir."),
    ],
    D=[
        arith("En un conflicto, cada niño habla 2 minutos sin ser interrumpido. Si son 2 niños, ¿cuántos minutos hablan en total?", "2*2", "Cada uno usa 2 minutos para hablar."),
        ex("Un niño dice «necesito que me avises antes de usar mis cosas». ¿Eso es una emoción o una necesidad?", "Una necesidad", "Dice lo que quiere lograr y no lo que siente."),
    ],
    context=[ex("Dos niñas discuten por un cuaderno. Una dice: «Me sentí mal cuando lo usaste sin avisar, porque lo necesito para mi tarea». La otra responde: «Entiendo que necesitabas el cuaderno». ¿Escuchan y se explican bien?", "Sí", "Usan mensaje en primera persona y reformulan.")],
    selfcheck=[ex("En Orientación: ¿reformular es repetir con mis palabras?", "Sí", "Así muestro que entendí."), ex("¿«Tú eres malo» es un mensaje en primera persona?", "No", "Es una acusación."), ex("¿Interrumpir ayuda a escuchar?", "No", "Impide entender al otro.")],
    task=T("Lee: «Pedro usó los colores de Mía sin preguntar y ella se enojó». Escribe un mensaje en primera persona para Mía («Me sentí… cuando… porque necesito…») y una reformulación que Pedro podría decir. Practícalas con un compañero con un tono tranquilo.", "Mía: «Me sentí mal cuando usaste mis colores sin preguntar, porque los necesito para mi dibujo». Pedro: «Entiendo que necesitabas tus colores».", ["mensaje con sentí, cuando y necesito", "reformulación que repite lo que entendió", "no acusa ni culpa"], ["frases escritas o actuadas"], ["acusar con «tú eres»", "interrumpir"], "Reconoce el mensaje y verifica que la reformulación repita lo entendido."),
    reinforce="Escribe un mensaje en primera persona para un conflicto de tu elección.",
    extend="Reformula tres frases que escuches hoy en un diálogo de cuento.",
)

lesson(
    OA6, 3,
    "Una hoja y un lápiz. Las opciones de ejemplo están escritas en los ejercicios.",
    "Aprenderé a pensar varias opciones para resolver un conflicto y a elegir las que respetan los derechos de los dos. Sirve para llegar a acuerdos justos.",
    ["Sé separar hechos y necesidades.", "Sé escuchar y reformular."],
    [
        "Después de entender el conflicto, se buscan opciones: ideas para resolverlo. Una buena forma es pensar varias, sin criticarlas todavía. Por ejemplo, para un solo columpio: turnos de cinco minutos, jugar juntos otro juego, o cambiar mañana.",
        "Luego revisamos cada opción con tres preguntas. ¿Es justa para los dos? ¿Es segura? ¿Respeta los derechos de ambos? Los derechos incluyen no ser dañado, ser escuchado y poder decir que no. Las opciones que usan la fuerza, amenazan, esconden algo o dejan a alguien afuera no sirven.",
        "Una buena opción satisface la necesidad de los dos, al menos en parte. Si no se logra, se prueba otra o se pide ayuda a un adulto. No es perder: es buscar algo que sirva a ambos.",
    ],
    [("opción", "una idea posible para resolver algo"), ("justo", "que trata bien a las dos partes"), ("derecho", "algo que merece cada persona"), ("satisfacer", "dar lo que se necesita"), ("turno", "momento que le toca a cada uno")],
    [
        W("Revisar una opción", "Para un solo columpio, Ana propone turnos de cinco minutos. ¿Es una opción que respeta los derechos de los dos?", ["Los dos tienen su tiempo.", "Nadie se lastima.", "Es justa y segura."], "Sí, respeta los derechos de los dos"),
        W("Descartar una opción", "Beto propone: «El que sea más fuerte se queda con el columpio». ¿Sirve?", ["Usa la fuerza.", "Uno puede salir dañado.", "No es justa ni segura."], "No sirve"),
    ],
    [
        M("Elegir la primera opción sin revisar si es justa.", "Queremos terminar rápido.", "Revisa si es justa, segura y respeta a los dos."),
        M("Creer que un acuerdo es que uno gane y otro pierda.", "Se piensa en ganadores y perdedores.", "Busca algo que sirva a los dos."),
    ],
    R=[
        ex("¿Una opción es una idea posible para resolver el conflicto?", "Sí", "Se piensan varias."),
        ex("¿Usar la fuerza es una opción justa?", "No", "Puede dañar a alguien."),
        ex("¿Los turnos pueden ser una opción justa?", "Sí", "Cada uno tiene su momento."),
    ],
    U=[
        ex("¿Qué tres preguntas se usan para revisar una opción?", "Si es justa, segura y respeta los derechos de ambos", "Ayudan a elegir bien."),
        ex("Si una opción deja a alguien afuera, ¿sirve?", "No", "No respeta los derechos de esa persona."),
        ex("Si no hay acuerdo, ¿qué se puede hacer?", "Probar otra opción o pedir ayuda a un adulto", "No hay que abandonar."),
    ],
    A=[
        ex("Dos niños quieren el mismo balón. Escribe una opción de turnos.", "Cada uno juega diez minutos y luego cambian", "Los dos tienen tiempo."),
        ex("Elige la opción que respeta los derechos: «jugar los dos juntos a otra cosa» o «quitarle el balón al más chico».", "«Jugar los dos juntos a otra cosa»", "La otra usa la fuerza."),
        ex("Una opción dice «no le hablo a nadie hasta que me den el balón». ¿Es justa?", "No", "Presiona en vez de buscar un acuerdo."),
    ],
    Z=[
        ex("Dos opciones: a) turnos de cinco minutos; b) «quien grite más fuerte se lo queda». ¿Cuál respeta a los dos?", "La a", "La b no es justa ni segura."),
        ex("Un niño dice: «Si acepto turnos, pierdo». ¿Qué se le puede responder?", "Que los dos ganan al jugar", "El acuerdo sirve a ambos."),
    ],
    D=[
        arith("Hay 20 minutos de recreo y 4 niños quieren usar el columpio, cada uno la misma cantidad. ¿Cuántos minutos le tocan a cada uno?", "20//4", "El tiempo se reparte en partes iguales."),
        ex("Ana y Beto piensan tres opciones para el columpio: turnos de cinco minutos, jugar juntos a otra cosa y quitárselo al más débil. ¿Cuántas respetan los derechos de los dos?", "2", "Los turnos y jugar juntos son justos; quitarlo por la fuerza no."),
    ],
    context=[ex("Dos niñas quieren usar el único computador de la sala. La profesora dice: «Piensen tres opciones que sean justas». ¿Es buena idea pensar varias?", "Sí", "Se puede escoger la mejor.")],
    selfcheck=[ex("En Orientación: ¿una opción justa respeta a los dos?", "Sí", "Los derechos son para ambos."), ex("¿Se puede usar la fuerza para resolver?", "No", "La fuerza puede dañar a alguien."), ex("¿Se pueden pensar varias opciones?", "Sí", "Así hay más posibilidades.")],
    task=T("Lee el conflicto: dos niños quieren usar el mismo juego de mesa en el recreo, pero solo hay uno. Escribe tres opciones. Después revisa cada una con tres preguntas: ¿es justa?, ¿es segura?, ¿respeta los derechos de los dos? Marca cuál elegirías.", "1) Turnos de diez minutos. 2) Jugar juntos. 3) Usarlo mañana. Elijo jugar juntos: es justo y seguro.", ["tres opciones distintas", "revisa con las tres preguntas", "no incluye fuerza ni amenazas"], ["lista de opciones revisadas"], ["proponer opciones injustas", "elegir sin revisar"], "Reconoce las opciones y verifica que se hayan revisado."),
    reinforce="Escribe dos opciones para un conflicto del recreo.",
    extend="Explica por qué una opción que daña a alguien no es válida aunque sea rápida.",
)

lesson(
    OA6, 4,
    "Una hoja y un lápiz. Los acuerdos de ejemplo están escritos en los ejercicios. Para los casos de violencia, siempre hay un adulto presente.",
    "Aprenderé a hacer un acuerdo claro, a reparar y a pedir ayuda cuando el conflicto es grave. Sirve para cerrar el conflicto y cuidar a todos.",
    ["Sé proponer opciones justas.", "Sé escuchar y reformular."],
    [
        "Un acuerdo es una decisión que los dos aceptan. Un buen acuerdo es claro: dice quién hace qué y cuándo. Por ejemplo: «Cada uno usa el columpio cinco minutos, hoy y mañana». Se revisa después de un tiempo: si no funciona, se cambia. Un acuerdo no se impone ni se hace bajo presión.",
        "A veces el conflicto dañó a alguien. Entonces se repara: reconocer lo que pasó, decir «lo siento» y hacer algo concreto para arreglarlo. Quien fue dañado puede decir qué le ayudaría. La reparación no obliga a perdonar al instante.",
        "No todo conflicto se arregla entre compañeros. Si hay golpes, amenazas, burlas que se repiten, miedo o alguien que tiene más poder, hay que pedir ayuda a un adulto. Una mediación es cuando un adulto o una persona preparada ayuda a conversar. Pedir ayuda no es fracasar ni acusar.",
    ],
    [("acuerdo", "decisión que aceptan las dos partes"), ("reparación", "hacer algo para arreglar un daño"), ("mediación", "ayuda de un tercero para conversar"), ("revisar", "mirar después si el acuerdo funciona"), ("poder", "fuerza o ventaja de una persona sobre otra")],
    [
        W("Acuerdo claro", "¿Cuál es un acuerdo claro: «Seamos amigos» o «Cada uno usa el balón diez minutos, hoy y mañana»?", ["Un acuerdo dice quién, qué y cuándo.", "El segundo lo dice.", "El primero es muy general."], "«Cada uno usa el balón diez minutos, hoy y mañana»"),
        W("Pedir ayuda", "Un niño más grande amenaza a otro y le quita su colación cada día. ¿Se resuelve entre compañeros?", ["Hay amenazas y repetición.", "Hay desigualdad de poder.", "Hay que avisar a un adulto."], "No, hay que pedir ayuda a un adulto"),
    ],
    [
        M("Aceptar un acuerdo que no me gusta por miedo.", "Se teme que el otro se enoje.", "Un acuerdo se acepta con libertad. Si hay miedo, pide ayuda."),
        M("Creer que pedir ayuda a un adulto es acusar o fracasar.", "Se piensa que debo arreglarlo solo.", "Hay conflictos que necesitan ayuda; avisar protege."),
    ],
    R=[
        ex("¿Un acuerdo claro dice quién, qué y cuándo?", "Sí", "Así todos saben qué hacer."),
        ex("¿Se puede obligar a alguien a aceptar un acuerdo?", "No", "Un acuerdo se acepta con libertad."),
        ex("Si hay amenazas, ¿conviene pedir ayuda a un adulto?", "Sí", "Hay riesgo y no es entre iguales."),
    ],
    U=[
        ex("¿Qué es reparar después de un conflicto?", "Hacer algo concreto para arreglar el daño", "Reconocer y ayudar a arreglar."),
        ex("¿Qué se hace si el acuerdo no funciona?", "Se revisa y se cambia", "Los acuerdos se pueden ajustar."),
        ex("¿Pedir ayuda a un adulto es un fracaso?", "No", "Es una forma de cuidarse."),
    ],
    A=[
        ex("Escribe un acuerdo claro para compartir un computador entre dos niños.", "Cada uno lo usa 15 minutos, hoy y mañana", "Dice quién, cuánto y cuándo."),
        ex("Un niño rompió el dibujo de otro. Escribe una reparación concreta.", "Pedir perdón y ayudar a hacer otro dibujo", "Repara el daño con una acción."),
        ex("Un compañero te amenaza todos los días. ¿Qué haces: aceptar su acuerdo o avisar a un adulto?", "Avisar a un adulto", "Hay amenaza y desigualdad de poder."),
    ],
    Z=[
        ex("Dos niños acordaron turnos de cinco minutos, pero uno sigue pasándose. ¿Qué conviene?", "Revisar el acuerdo o pedir ayuda", "Un acuerdo que no se cumple se ajusta."),
        ex("Una niña dice «acepto porque me da miedo que me siga molestando». ¿Es un buen acuerdo?", "No", "El miedo no es libertad."),
    ],
    D=[
        arith("Un acuerdo da 10 minutos a cada uno de 3 niños. ¿Cuántos minutos hay en total?", "10*3", "Se reparte 10 minutos a cada uno."),
        ex("Un conflicto tiene golpes repetidos. ¿Quién debe ayudar a resolverlo: los mismos niños o un adulto?", "Un adulto", "Hay violencia y no es un desacuerdo entre iguales."),
    ],
    context=[ex("Dos niñas acuerdan turnos para la cuerda de saltar y, tras una semana, ven que funciona. ¿Revisaron el acuerdo?", "Sí", "Comprobaron si servía.")],
    selfcheck=[ex("En Orientación: ¿un acuerdo se hace con libertad?", "Sí", "Nadie puede forzarlo."), ex("¿Con golpes o amenazas conviene avisar?", "Sí", "Necesita un adulto."), ex("¿Reparar incluye hacer algo?", "Sí", "No basta con una palabra.")],
    task=T("Lee los casos: (A) dos niños se pelean por turnos de un juego, sin amenazas; (B) un compañero te empuja y te quita tus cosas todos los días. Para el caso A, escribe un acuerdo claro con quién, qué y cuándo. Para el caso B, escribe qué harías (parar, alejarte, contar) y a quién avisarías.", "A: cada uno juega diez minutos, hoy y mañana. B: digo «para», me alejo y se lo cuento a una profesora.", ["acuerdo con quién, qué y cuándo", "en B pide ayuda a un adulto", "no resuelve la violencia solo"], ["respuesta escrita"], ["resolver una amenaza solo", "acuerdo poco claro"], "Reconoce el acuerdo y verifica que el caso B se derive a un adulto."),
    reinforce="Escribe un acuerdo claro de tu curso sobre el uso de un material.",
    extend="Explica la diferencia entre un conflicto entre compañeros y una situación en que hay que avisar a un adulto.",
)
