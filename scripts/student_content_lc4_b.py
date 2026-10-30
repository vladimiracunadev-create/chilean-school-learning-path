"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 17 (relación entre el ser humano, la naturaleza y el cosmos, vinculada a la ciencia desde la perspectiva
indígena), OA LF01 (comprensión de relatos orales en lengua indígena) y OA LF02 (comunicación oral en lengua
indígena sobre aspectos de la cosmovisión).

Criterio de autoría: todos los relatos, tarjetas, diálogos, personajes y registros de práctica son inventados,
están en castellano y se declaran como tales; no pertenecen a ningún pueblo. No se atribuye a ningún pueblo un
conocimiento del cielo, un símbolo, una constelación, un calendario ni un significado espiritual: las
observaciones que se practican (sombras, luna, agua) las puede hacer cualquier persona en su entorno. Las únicas
expresiones en lengua indígena son las ya atestiguadas en 2.º y 3.º (mari mari, chaltumay, ko, antü, kuyen, ruka,
mapu, ñuke en mapuzugun; iorana, maururu en rapa nui) y siempre con su ficha. No se escribe pronunciación ni
gramática, ni se asegura a quién, cuándo o en qué ceremonias se dice nada. La forma tradicional la enseñan el
educador/a tradicional y la comunidad; cada tarea abierta lo remite a ellos.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA17, LF1, LF2 = "LC04 OA 17", "LC04 OA LF01", "LC04 OA LF02"

CONSULT = " Recuerda: lo que es tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Consúltales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No evaluar la identidad ni la fluidez de nadie."

FICHA_PAL = "Ficha de palabras (de práctica): en mapuzugun «ko» es agua, «antü» es sol, «kuyen» es luna, «ruka» es casa, «mapu» es tierra, «ñuke» es madre. «mari mari» es un saludo y «chaltumay» es «gracias» en mapuzugun. «iorana» es un saludo y «maururu» es «gracias» en rapa nui."


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


# =================================================================== OA 17 · ser humano, naturaleza y cosmos
L(
    OA17, 1,
    materials="Lápiz y hoja. Las fichas están escritas en este cuaderno y son inventadas para practicar; no son de ningún pueblo.",
    use="Aprenderé a preguntar de dónde viene un saber sobre la naturaleza y el cosmos y qué límites tiene. Sirve para respetar los saberes de los pueblos originarios y no apropiarme de ellos.",
    prior=["Sé que cada pueblo originario tiene su propia cultura y sus propios saberes.", "Sé que toda creación o dato tiene una procedencia."],
    explain=[
        "El cosmos es todo lo que existe: la tierra, el agua, el sol, la luna y las estrellas. La naturaleza es la parte que nos rodea, como las plantas, los animales y los ríos. Los seres humanos viven en relación con ambos. Muchos pueblos originarios construyeron saberes observando su territorio con mucha atención. Esos saberes sirven, por ejemplo, para cuidar el agua o para organizar el trabajo. Se pueden llamar ciencia desde la perspectiva indígena.",
        "Cada saber tiene una procedencia: de qué pueblo viene, de qué territorio y qué persona o comunidad lo cuida. También puede tener un resguardo, que son los límites que la comunidad pone sobre quién lo cuenta, cuándo y cómo. Yo no decido esos límites; los respeto.",
        "Para trabajar con cuidado uso una ficha de cinco datos: pueblo, territorio, fuente, permiso y límites. Si falta un dato, detengo la actividad y pregunto al educador o a la educadora tradicional. Aprender es escuchar con respeto. Apropiarse es decir que un saber ajeno es mío.",
    ],
    vocab=[("cosmos", "todo lo que existe, incluidos el sol, la luna y las estrellas"), ("saber", "algo que se aprende y se usa para vivir"), ("procedencia", "de dónde viene un saber"), ("resguardo", "límites que una comunidad pone al uso de algo suyo"), ("apropiarse", "decir que algo ajeno es mío")],
    worked=[
        W("Leer una ficha completa", "Ficha inventada. Pueblo: no corresponde, es una observación propia. Territorio: patio de una escuela de práctica. Fuente: dibujo de Camila, de 4.º. Permiso: Camila dice que sí. Límites: ninguno. ¿Quién es la fuente?", ["Busco el dato «fuente».", "Dice: dibujo de Camila, de 4.º.", "Los cinco datos están escritos."], "Camila, de 4.º"),
        W("Ficha con un dato que falta", "Hugo encontró un papel que dice cuándo sembrar según la luna. No dice de qué pueblo viene ni si se puede copiar. ¿Qué datos faltan y qué hace?", ["Faltan el pueblo, la fuente y el permiso.", "Sin esos datos no puedo seguir.", "Detengo la actividad y pregunto al educador tradicional."], "Faltan pueblo, fuente y permiso; detiene la actividad y pregunta"),
    ],
    mistakes=[
        M("Contar un saber de un pueblo como si lo hubiera descubierto yo.", "Eso es apropiarse: el saber tiene una procedencia y una comunidad que lo cuida.", "Digo de dónde viene y quién me lo enseñó."),
        M("Seguir con la actividad aunque falte el permiso.", "Sin permiso no sé si el saber se puede compartir.", "Me detengo y pregunto antes de usarlo."),
    ],
    R=[
        ex("¿Qué es el cosmos: A) todo lo que existe, como la tierra, el sol y las estrellas B) una sola casa?", "A", "Cosmos es todo lo que existe, incluidos el cielo y la tierra."),
        ex("Un saber de un pueblo se cuida. ¿Quién decide cómo se comparte: A) cualquier persona B) la comunidad que lo cuida?", "B", "Los límites los pone la comunidad que lo cuida."),
        ex("La ficha de procedencia pide pueblo, territorio, fuente, permiso y límites. ¿Cuántos datos son?", "5", "Se cuentan cinco datos distintos en la lista."),
    ],
    C=[
        ex("Verdadero o falso: si no sé de qué pueblo viene un saber, puedo decir que es de mi curso.", "Falso", "Eso sería apropiarme de un saber con otra procedencia."),
        arith("Una ficha tiene escrito solo el dato de la fuente. Debe tener 5 datos. ¿Cuántos datos faltan?", "5 - 1", "Faltan los datos que no están escritos."),
        ex("Apropiarse de un saber es: A) decir que un saber ajeno es mío B) escucharlo con respeto.", "A", "Apropiarse es quedarse con algo ajeno como propio."),
    ],
    A=[
        ex("Ordena los pasos: A) detengo la actividad B) veo que falta el permiso C) pregunto al educador tradicional. Escribe las letras.", "B, A, C", "Primero noto la falta, luego me detengo y al final pregunto."),
        ex("Ficha: «Pueblo: sin dato. Territorio: sin dato. Fuente: un afiche viejo. Permiso: sin dato. Límites: sin dato». ¿Qué dato sí tiene la ficha?", "la fuente", "Solo el dato de la fuente está escrito."),
        ex("¿Qué dato de la ficha responde a la pregunta «¿me dejaron usarlo?»: pueblo, permiso o territorio?", "permiso", "El permiso dice si puedo usar el saber."),
    ],
    Z=[
        ex("Nico dice: «Vi un video de una comunidad que lee el cielo; lo voy a contar como si lo hubiera descubierto yo». ¿Qué error comete: A) se apropia del saber B) cita su fuente?", "A", "Cuenta un saber ajeno como propio, sin procedencia."),
        ex("Ficha X: cinco datos escritos y permiso «sí». Ficha Y: permiso «no sé». ¿Con cuál ficha puedes seguir trabajando, X o Y?", "X", "La ficha Y tiene un permiso dudoso y debe detenerse."),
    ],
    D=[
        arith("Un curso revisa 6 fichas. Hay 4 con los cinco datos. ¿Cuántas fichas deben detenerse hasta completar sus datos?", "6 - 4", "Se detienen las fichas que no están completas."),
        ex("Ana vio una foto sin fuente. ¿Qué debe hacer primero: A) preguntar al educador tradicional de dónde viene B) escribir un significado que se le ocurra?", "A", "Sin fuente, inventar un significado sería falso e irrespetuoso."),
    ],
    context=[ex("En la biblioteca, tu curso encuentra un papel sin título que explica cuándo sembrar según la luna. ¿Qué haces primero: «Lo copio al cuaderno» o «Averiguo su fuente y pregunto al educador tradicional»?", "«Averiguo su fuente y pregunto al educador tradicional»", "Sin fuente ni permiso no se copia un saber.")],
    selfcheck=[
        ex("¿Cómo se llama el dato que dice de dónde viene un saber?", "procedencia", "Procedencia significa de dónde viene."),
        ex("¿Cómo se llaman los límites que una comunidad pone al uso de un saber suyo?", "resguardo", "Resguardo es el cuidado y límite sobre lo propio."),
        ex("Si falta un dato de la ficha, ¿qué hago: sigo o detengo la actividad?", "detengo la actividad", "Sin todos los datos no puedo asegurar que sea correcto."),
    ],
    task=T(
        "Completa la ficha de cinco datos para esta observación tuya: «el sol sale cada mañana por el mismo lado del cielo». Pueblo: escribe que no es saber de un pueblo. Territorio, fuente, permiso y límites: complétalos tú. Después escribe una pregunta para el educador tradicional sobre cómo observa el cielo su pueblo.",
        "Pueblo: no corresponde, es observación propia. Territorio: mi casa. Fuente: yo. Permiso: sí. Límites: ninguno. Pregunta: ¿cómo observa el cielo su pueblo?",
        ["completa los cinco datos de la ficha", "distingue su observación propia de un saber de un pueblo", "escribe una pregunta al educador/a tradicional"],
        ["ficha escrita en el cuaderno", "pregunta escrita o dicha en voz alta"],
        ["dejar datos en blanco", "atribuir a un pueblo algo que él o ella solo observó"],
        "Valora que reconoció procedencia y permiso; si atribuyó su observación a un pueblo, pídele que distinga lo propio de lo aprendido y que pregunte a quien enseña.",
    ),
    reinforce="Di en voz alta los cinco datos de la ficha de procedencia y qué haces si falta uno.",
    extend="Explica a una persona de tu casa por qué no basta con ver o leer un saber para poder contarlo como propio.",
)

L(
    OA17, 2,
    materials="Lápiz, hoja y un palo o lápiz largo. Los datos de práctica están escritos aquí. Seguridad: nunca mires directamente al sol; observa solo sus sombras.",
    use="Aprenderé a observar con cuidado el sol, la luna y el agua y a anotar lo que veo con fecha y medidas. Sirve para tener observaciones propias sin copiar símbolos ni saberes de otros.",
    prior=["Sé que un saber tiene procedencia y resguardo.", "Sé usar centímetros para medir una línea."],
    explain=[
        "Observar es mirar con atención y anotar. Una buena observación dice qué vi, cuándo y cuánto. Por ejemplo: «a las 12, la sombra del palo medía 40 cm». Una interpretación es lo que pienso que significa y no se ve directamente. Primero anoto lo que observo; después pienso qué podría significar.",
        "Hay cualidades del cielo y del agua que cambian con el tiempo. El sol sale por un lado y se pone por el lado opuesto. La sombra de un palo es más corta cuando el sol está más alto, cerca del mediodía (la hora exacta cambia según la época y el lugar), y más larga en la mañana y en la tarde. La luna cambia de forma durante cerca de un mes. El agua de un paño mojado desaparece al secarse. Estas observaciones las puede hacer cualquier persona en su entorno.",
        "Muchos pueblos originarios observaron durante mucho tiempo el sol, la luna y el agua para vivir mejor en su territorio. Lo que cada pueblo sabe y cómo lo explica lo cuenta su comunidad. Yo no copio sus símbolos ni invento sus explicaciones; hago mis propias anotaciones con mis palabras.",
    ],
    vocab=[("observación", "lo que veo y anoto con atención"), ("interpretación", "lo que pienso que significa algo"), ("sombra", "zona oscura que deja un objeto cuando la luz lo toca"), ("registro", "anotación ordenada con fecha y medidas"), ("cualidad", "cómo es algo: corto, largo, redondo")],
    worked=[
        W("Observación o interpretación", "Frase 1: «A las 9, la sombra del palo medía 90 cm». Frase 2: «El sol se enojó con el palo». ¿Cuál es una observación?", ["La frase 1 dice hora y medida que se puede comprobar.", "La frase 2 dice algo que no se puede medir."], "La frase 1"),
        W("Leer un registro de sombras", "Registro de práctica (inventado): 9 h, 90 cm; 12 h, 40 cm; 15 h, 85 cm. ¿A qué hora fue más corta la sombra y cuánto más corta que a las 9?", ["Comparo los tres números: 40 es el menor.", "Fue más corta a las 12.", "Resto 90 − 40 = 50."], "A las 12; 50 cm más corta"),
    ],
    mistakes=[
        M("Anotar «el cielo estaba lindo» y nada más.", "No dice qué vi ni se puede medir.", "Anoto hora, lugar y qué cambió."),
        M("Mirar directo al sol para ver cómo es.", "Puede dañar los ojos.", "Observo solo su sombra o la luz sobre el suelo."),
    ],
    R=[
        ex("Observar es: A) mirar con atención y anotar B) adivinar sin mirar.", "A", "La observación se apoya en lo que veo."),
        ex("«El palo tiene una sombra de 40 cm». ¿Esa frase es una observación o una interpretación?", "observación", "Dice una medida que se puede comprobar."),
        ex("Para ver cómo se mueve el sol, ¿miro directo al sol o miro su sombra?", "miro su sombra", "Mirar directo al sol daña los ojos."),
    ],
    C=[
        ex("Verdadero o falso: la sombra de un palo es igual de larga todo el día.", "Falso", "Cambia: es más corta cerca del mediodía."),
        ex("Une la idea con su tipo: «Anoté que la luna estaba redonda» y «La luna quiere decirme algo». Escribe «observación» e «interpretación» en ese orden.", "observación, interpretación", "La primera dice lo que vi; la segunda, lo que supongo."),
        ex("El sol sale por un lado del cielo. ¿Se pone por el mismo lado o por el lado opuesto?", "por el lado opuesto", "Cruza el cielo y se pone al otro lado."),
    ],
    A=[
        arith("Registro: sombra de 80 cm a las 10 h y de 50 cm a las 12 h. ¿Cuántos centímetros más corta fue a las 12 h?", "80 - 50", "Resto la sombra de las 12 de la de las 10."),
        ex("Registro de práctica: lunes 3 cm de agua en un vaso; martes 2 cm; miércoles 1 cm. ¿Qué día quedó menos agua?", "miércoles", "El miércoles tiene la medida menor: 1 cm."),
        ex("Ordena las anotaciones de la sombra de más larga a más corta: A) 40 cm B) 90 cm C) 85 cm. Escribe las letras.", "B, C, A", "Va de 90 a 85 y a 40."),
    ],
    Z=[
        ex("Rita anotó: «La luna estaba redonda el día 14». Tomás anotó: «La luna estaba triste». ¿Quién hizo una observación que se puede comprobar?", "Rita", "Tomás escribió una interpretación; Rita dio un dato."),
        ex("Un amigo copia un dibujo de una estrella de un afiche y dice «es un símbolo de mi registro». ¿Qué le falta: A) la procedencia del dibujo B) más colores?", "A", "No sabe de dónde viene ni si se puede copiar."),
    ],
    D=[
        arith("Una niña midió sombras durante 3 días: 40 cm, 38 cm y 42 cm a las 12 h. ¿Cuál es la suma de las tres medidas?", "40 + 38 + 42", "Sumo las tres medidas del registro."),
        ex("Frase: «Cada mañana el sol sale por el mismo lado, por eso es importante». ¿Cuál parte es observación: «el sol sale por el mismo lado» o «por eso es importante»?", "«el sol sale por el mismo lado»", "La segunda parte es una opinión."),
    ],
    context=[ex("En el patio clavas un palo en tierra blanda y mides su sombra a las 9, a las 12 y a las 15. ¿A qué hora esperas la sombra más corta: a las 9 o a las 12?", "a las 12", "Cerca del mediodía la sombra es más corta.")],
    selfcheck=[
        ex("¿Cómo se llama lo que pienso que significa algo y no se ve?", "interpretación", "Es lo que supongo, no lo que mido."),
        ex("¿Qué dos datos incluyo en un registro de sombra además de la medida?", "hora y fecha", "El registro necesita saber cuándo se midió."),
        ex("¿Puedo mirar directo al sol para observarlo?", "No", "Puede dañar los ojos."),
    ],
    task=T(
        "Haz un registro propio de una sombra: clava un palo o pon un lápiz parado en un lugar seguro y anota, a tres horas distintas del día, la medida de su sombra en centímetros. Si no puedes medir, dibuja la sombra y escribe «más larga» o «más corta». Escribe una observación y una interpretación tuya sobre lo que viste. No mires directo al sol.",
        "9 h: 70 cm; 12 h: 35 cm; 15 h: 65 cm. Observación: a las 12 la sombra fue más corta. Interpretación: pienso que el sol estaba más alto.",
        ["anota hora y medida de tres sombras", "separa una observación de una interpretación", "no copia símbolos ajenos"],
        ["registro escrito o dibujado en el cuaderno"],
        ["mirar directo al sol", "anotar solo opiniones y ninguna medida"],
        "Valora que anotó datos propios; si mezcló opinión y medida, pídele que las separe con dos columnas.",
    ),
    reinforce="Mide con una regla la sombra de un lápiz parado y di una observación y una interpretación.",
    extend="Cuenta a una persona de tu casa por qué una observación se puede comprobar y una interpretación no.",
)

L(
    OA17, 3,
    materials="Lápiz, hoja y colores. Los ejemplos están escritos aquí y son inventados.",
    use="Aprenderé a mostrar con una creación propia una relación entre una persona, la naturaleza y el cielo de mi entorno. Sirve para expresar lo que observo sin copiar símbolos de ningún pueblo.",
    prior=["Sé separar una observación de una interpretación.", "Sé que no copio símbolos sin conocer su procedencia."],
    explain=[
        "Una relación une dos cosas: una cosa cambia o ayuda a la otra. Por ejemplo, la lluvia llena el río, el río riega la huerta y la huerta da alimento a una persona. Los seres humanos, la naturaleza y el cosmos se pueden relacionar así: el sol da luz y calor, la luz ayuda a crecer a las plantas y las plantas alimentan a las personas.",
        "Puedo mostrar una relación con una cadena de tarjetas. Cada tarjeta lleva una sola cosa y una flecha indica a qué lleva. Hago un dibujo propio o un texto breve y uso mis propias líneas, no símbolos que vi en otro lugar. Una creación propia nace de lo que observé en mi entorno.",
        "Mi creación muestra mi mirada, no la de un pueblo. Si quiero saber cómo un pueblo explica estas relaciones, pregunto a su educador o educadora tradicional. Así aprendo sin inventar ni apropiarme.",
    ],
    vocab=[("relación", "unión en la que una cosa cambia o ayuda a otra"), ("cadena", "serie de pasos unidos uno tras otro"), ("flecha", "signo que muestra hacia dónde lleva un paso"), ("creación propia", "trabajo hecho con mis ideas y observaciones"), ("entorno", "lo que me rodea")],
    worked=[
        W("Armar una cadena", "Tarjetas: alimento, lluvia, huerta, río. Ordénalas como cadena: ¿qué va primero y qué va al final?", ["La lluvia llega primero y llena el río.", "El río riega la huerta.", "La huerta da el alimento, que va al final."], "lluvia → río → huerta → alimento"),
        W("Propio o copiado", "Sofía dibuja una espiral que vio en un afiche y dice que es su creación. Marta dibuja el recorrido que hizo la sombra de un palo. ¿Cuál es creación propia?", ["Sofía copió una figura de un afiche.", "Marta dibuja algo que observó ella misma."], "La de Marta"),
    ],
    mistakes=[
        M("Copiar una figura que vi en un afiche y decir que la inventé.", "No conozco su procedencia ni su significado.", "Dibujo con mis propias líneas lo que observé."),
        M("Poner dos cosas que no se relacionan en la misma cadena.", "Una cadena necesita que cada paso lleve al siguiente.", "Compruebo que cada flecha tenga sentido."),
    ],
    R=[
        ex("La lluvia llena el río. ¿Qué cosa cambia por la lluvia: A) el río B) una piedra seca?", "A", "El río recibe más agua por la lluvia."),
        ex("En una cadena, ¿para qué sirve la flecha: A) para decorar B) para mostrar a qué lleva cada paso?", "B", "La flecha indica el orden y la relación."),
        ex("Una creación propia se hace con: A) lo que observé yo B) un símbolo copiado de un afiche.", "A", "Propia significa nacida de mi observación."),
    ],
    C=[
        ex("Cadena: sol → luz → planta → alimento. ¿Qué paso viene después de «planta»?", "alimento", "La flecha lleva de la planta al alimento."),
        ex("Verdadero o falso: si copio una figura y la pinto de otro color, ya es mía.", "Falso", "Sigue siendo una figura de otra procedencia."),
        ex("Ideas: «el sol da calor» y «la tierra se calienta». ¿Cuál es la causa: «el sol da calor» o «la tierra se calienta»?", "«el sol da calor»", "El sol que da calor hace que la tierra se caliente."),
    ],
    A=[
        ex("Ordena como cadena: A) alimento B) lluvia C) huerta D) río. Escribe las letras.", "B, D, C, A", "Lluvia, río, huerta y alimento van en ese orden."),
        arith("Una cadena tiene 5 tarjetas. Ya pusiste 3. ¿Cuántas tarjetas faltan?", "5 - 3", "Faltan las tarjetas que no están puestas."),
        ex("Cadena con un paso que sobra: sol → luz → planta → zapato. ¿Qué paso sobra?", "zapato", "El zapato no se relaciona con la planta."),
    ],
    Z=[
        ex("Dos niños muestran una relación. Lalo: «la luna cambia, por eso anoto cada noche su forma». Mía: «copié esta figura de una tela». ¿Quién hizo una creación propia?", "Lalo", "Lalo parte de su observación; Mía copió una figura."),
        ex("¿Qué cadena tiene mejor relación: A) lluvia → río → huerta B) lluvia → zapato → río?", "A", "Cada paso de la A lleva al siguiente."),
    ],
    D=[
        arith("Camila observó la luna 7 noches y dibujó una forma cada noche. Luego observó 3 noches más. ¿Cuántos dibujos tiene en total?", "7 + 3", "Una forma por noche: 7 noches más 3 noches."),
        ex("Pedro dice: «Mi cadena muestra cómo explica el cielo un pueblo». ¿Qué debe cambiar: A) decir que es su mirada propia B) pintarla de otro color?", "A", "No puede hablar por un pueblo; sí por su observación."),
    ],
    context=[ex("Quieres mostrar a tu curso cómo el agua llega a las plantas de tu casa. ¿Qué dibujas: «una cadena lluvia → tierra → planta» o «un símbolo copiado de una revista»?", "«una cadena lluvia → tierra → planta»", "Es una relación que observas y puedes explicar.")],
    selfcheck=[
        ex("¿Cómo se llama el trabajo hecho con mis propias observaciones?", "creación propia", "Nace de lo que yo observé."),
        ex("¿Qué signo muestra a qué lleva cada paso de una cadena?", "la flecha", "La flecha ordena los pasos."),
        ex("¿Quién puede decirme cómo explica un pueblo estas relaciones?", "el educador o la educadora tradicional", "Ellos y la comunidad conocen su cosmovisión."),
    ],
    task=T(
        "Crea una cadena de cuatro tarjetas con flechas que muestre una relación entre una persona, la naturaleza y el cielo de tu entorno. Por ejemplo: sol → luz → planta → alimento. Dibuja con líneas propias. Escribe una frase que diga qué observaste. Escribe también una pregunta para el educador tradicional sobre cómo su pueblo ve estas relaciones.",
        "Lluvia → río → huerta → alimento. Observé que después de llover el río del cerro lleva más agua. Pregunta: ¿cómo ve su pueblo la relación con el agua?",
        ["arma una cadena de cuatro tarjetas con sentido", "explica lo que observó", "no copia símbolos ni atribuye su mirada a un pueblo"],
        ["cadena dibujada en el cuaderno", "frase y pregunta escritas"],
        ["copiar figuras de otra procedencia", "unir pasos que no se relacionan"],
        "Valora que la cadena sea propia y con sentido; si copió una figura, pídele que dibuje solo lo que observó y que pregunte a quien enseña.",
    ),
    reinforce="Elige una cadena de cuatro pasos de esta clase y explícala en voz alta con tus palabras.",
    extend="Muestra tu cadena a una persona de tu casa y pídele que diga qué paso relaciona con qué.",
)

L(
    OA17, 4,
    materials="Lápiz y hoja. Las frases de práctica están escritas en este cuaderno y son inventadas.",
    use="Aprenderé a explicar mis decisiones y a decir con claridad qué sé yo y qué debe decir la comunidad. Sirve para hablar de la relación con la naturaleza y el cosmos sin inventar ni hablar por otros.",
    prior=["Sé separar observación e interpretación.", "Sé armar una cadena de relaciones con sentido."],
    explain=[
        "Cuando explico mi trabajo digo tres cosas: qué decidí, por qué lo decidí y qué observación lo apoya. Por ejemplo: «Puse la lluvia primero porque observé que el río sube después de llover».",
        "También digo los límites de lo que sé. Hay frases que puedo afirmar porque las observé yo. Hay frases que son solo mi interpretación y las marco así. Y hay frases sobre el significado espiritual o la historia de un pueblo, que no me corresponde afirmar: eso lo explican el educador o la educadora tradicional y la comunidad.",
        "Una buena explicación usa la palabra «porque», nombra la fuente de cada dato y no habla por todo un pueblo. Decir «no lo sé, lo preguntaré» también es una respuesta correcta y respetuosa.",
    ],
    vocab=[("decisión", "elección que hago y puedo explicar"), ("límite", "hasta dónde puedo afirmar algo"), ("fuente", "persona o material de donde viene un dato"), ("afirmar", "decir que algo es verdad"), ("comunidad", "grupo de personas que comparten un territorio y una cultura")],
    worked=[
        W("Clasificar frases", "Frase: «Observé que el río subió después de llover». ¿Es algo que puedo afirmar, una interpretación mía o algo que debe decir la comunidad?", ["Yo lo observé.", "Tiene un dato comprobable."], "Puedo afirmarlo porque lo observé"),
        W("Un límite de lo que sé", "Pregunta de un compañero: «¿Qué significa para un pueblo una estrella del cielo?». ¿Qué respuesta respeta los límites?", ["No conozco la explicación de ese pueblo.", "Debo decir que no lo sé y que lo preguntaré al educador tradicional."], "«No lo sé; lo preguntaré al educador tradicional»"),
    ],
    mistakes=[
        M("Decir «todos los pueblos creen que el sol es sagrado».", "Hablo por muchos pueblos sin saberlo y cada uno tiene su propia mirada.", "Hablo solo de lo que observé y de lo que la comunidad me autorizó a decir."),
        M("Explicar sin decir por qué.", "Sin razón no se entiende mi decisión.", "Uso «porque» y cito mi observación."),
    ],
    R=[
        ex("Una explicación usa la palabra «porque». ¿Para qué sirve: A) para decir la razón B) para cambiar de tema?", "A", "«Porque» introduce la razón de la decisión."),
        ex("«Observé que la sombra era corta a las 12». ¿Eso lo puedo afirmar o debe decirlo la comunidad?", "lo puedo afirmar", "Es algo que observé yo."),
        ex("Si no sé algo, ¿una respuesta correcta es «no lo sé; lo preguntaré» o inventar una respuesta?", "«no lo sé; lo preguntaré»", "Inventar no es respetuoso ni verdadero."),
    ],
    C=[
        ex("Verdadero o falso: puedo explicar qué significa una estrella para un pueblo aunque nadie me lo haya enseñado.", "Falso", "Ese significado lo explica la comunidad."),
        ex("Frase: «Pienso que la luna cambia porque cambia mi ánimo». ¿Es una observación o una interpretación mía?", "interpretación mía", "No se puede comprobar con una medida."),
        ex("¿Qué dato apoya esta decisión: «puse la lluvia primero porque observé que el río sube después de llover»?", "el río sube después de llover", "Es la observación que da la razón."),
    ],
    A=[
        ex("Según la clase, una explicación dice tres cosas. Ordénalas: A) la observación que lo apoya B) lo que decidí C) por qué lo decidí. Escribe las letras.", "B, C, A", "Primero la decisión, luego la razón y por último la observación que la apoya."),
        arith("Un registro tiene 6 frases. 4 son observaciones. ¿Cuántas frases son interpretaciones?", "6 - 4", "Las demás frases son interpretaciones."),
        ex("Clasifica «el agua de un vaso baja cada día»: A) lo observé B) debe decirlo la comunidad.", "A", "Es un dato que se mide con una regla."),
    ],
    Z=[
        ex("Lola dice: «Todos los pueblos originarios miran la luna de la misma manera». ¿Qué error tiene: A) habla por todos B) cita su fuente?", "A", "Cada pueblo tiene su mirada y Lola no puede hablar por todos."),
        ex("Dos explicaciones. Eva: «Puse el sol antes porque da luz a la planta». Gaspar: «Lo puse antes porque sí». ¿Cuál explicación está mejor hecha?", "la de Eva", "Eva da una razón con relación observable."),
    ],
    D=[
        arith("Un niño escribió 9 líneas en su trabajo. 5 son observaciones, 2 son interpretaciones y las demás son preguntas para el educador tradicional. ¿Cuántas preguntas escribió?", "9 - 5 - 2", "Resto las observaciones y las interpretaciones del total."),
        ex("Una persona dice: «Mi cadena de tarjetas es tal como la de un pueblo vecino». ¿Qué le falta a esa frase: A) una fuente y un permiso B) más flechas?", "A", "No dice de dónde sabe cómo es la del pueblo ni si pudo usarla."),
    ],
    context=[ex("Muestras tu cadena sol → luz → planta → alimento y un compañero te pregunta qué significa el sol para un pueblo. ¿Respondes «Es sagrado para todos» o «No lo sé; lo preguntaré al educador tradicional»?", "«No lo sé; lo preguntaré al educador tradicional»", "No puedo afirmar lo que no me enseñó la comunidad.")],
    selfcheck=[
        ex("¿Qué palabra uso para dar la razón de una decisión?", "porque", "«Porque» une la decisión con su razón."),
        ex("¿Quién explica el significado espiritual de algo para un pueblo?", "el educador o la educadora tradicional y la comunidad", "Ellos conocen y cuidan ese saber."),
        ex("¿Una frase que mido con una regla es una observación o una interpretación?", "observación", "Se puede comprobar con una medida."),
    ],
    task=T(
        "Toma tu cadena de la clase 3 o esta cadena: lluvia → río → huerta → alimento. Escribe tres frases: una que puedas afirmar porque la observaste, una que sea solo tu interpretación y una pregunta que le harías al educador tradicional. Después explica en voz alta por qué ordenaste así tus tarjetas, usando «porque».",
        "Puedo afirmar: después de llover, el río lleva más agua. Mi interpretación: pienso que por eso la huerta crece. Pregunta: ¿cómo cuida su pueblo el agua?",
        ["escribe una frase que afirma por observación", "marca una frase como interpretación", "formula una pregunta para quien enseña", "explica con «porque»"],
        ["tres frases escritas y explicación oral"],
        ["hablar por todo un pueblo", "no marcar qué es observación y qué es interpretación"],
        "Valora que reconoció los límites de lo que sabe; si habló por un pueblo, pídele que lo reformule como pregunta para quien enseña.",
    ),
    reinforce="Di en voz alta una frase que puedes afirmar, una que es interpretación tuya y una que debe responder la comunidad.",
    extend="Explica a una persona de tu casa por qué decir «no lo sé; lo preguntaré» también es respetuoso.",
)

# =================================================================== OA LF01 · comprensión de relatos orales
RELATO = "Relato de práctica (inventado; no es de ningún pueblo): «Hace mucho, un cerro llamado Alto Claro no tenía sombra. Los animales no encontraban descanso al mediodía. Una niña, Lía, subió tres días con una vasija de agua. En la cima regó una semilla. Pasaron muchas lunas y creció un árbol. Desde entonces el cerro tiene sombra y los animales descansan bajo ella.»"

L(
    LF1, 1,
    materials="Lápiz y hoja. Las tarjetas y el relato de práctica están escritos aquí; son inventados y no son de ningún pueblo. Un adulto puede leer en voz alta.",
    use="Aprenderé a situar quién cuenta un relato, a quién y en qué contexto. Sirve para escuchar relatos orales con respeto y saber de dónde vienen.",
    prior=["Sé que los relatos orales se transmiten de boca en boca.", "Sé que cada pueblo tiene sus propios relatos."],
    explain=[
        "Un relato oral es una historia que se cuenta con la voz y se transmite de boca en boca. Algunos relatos explican cómo empezó el mundo o cómo surgió un lugar. Esos relatos pertenecen a un pueblo y a una comunidad que los cuida, y llevan su cosmovisión, es decir, su manera de ver el mundo.",
        "Antes de escuchar, situamos el relato con una tarjeta de contexto de cinco datos: quién lo cuenta, a quién, dónde, cuándo y para qué. También anotamos si se puede registrar, por ejemplo grabar o escribir, y quién lo permite. Si no se puede, solo se escucha.",
        "Un relato real en lengua indígena lo cuenta una persona de la comunidad o el educador tradicional. En este cuaderno practicamos con un relato inventado en castellano, solo para aprender a escuchar. La forma en que se cuenta un relato real, las palabras exactas y los momentos adecuados los define la comunidad.",
    ],
    vocab=[("relato oral", "historia que se cuenta con la voz"), ("cosmovisión", "manera en que un pueblo ve y entiende el mundo"), ("contexto", "quién, a quién, dónde, cuándo y para qué se cuenta"), ("registrar", "grabar o escribir lo que se cuenta"), ("comunidad", "grupo de personas que comparten un territorio y una cultura")],
    worked=[
        W("Leer una tarjeta de contexto", "Tarjeta inventada. Quién cuenta: la abuela Rosa. A quién: al curso de 4.º. Dónde: en el patio. Cuándo: una tarde. Para qué: para conocer un relato de práctica. Registro: no permitido. ¿Se puede grabar el relato?", ["Busco el dato de registro.", "Dice «no permitido»."], "No, solo se escucha"),
        W("Un dato que falta", "Tarjeta: «Quién cuenta: don Luis. A quién: al curso. Dónde: en la sala. Cuándo: (sin dato). Para qué: (sin dato)». ¿Qué datos faltan?", ["Reviso los cinco datos.", "Faltan cuándo y para qué."], "Faltan cuándo y para qué"),
    ],
    mistakes=[
        M("Grabar un relato sin preguntar.", "Quien cuenta y la comunidad deciden si se registra.", "Pregunto antes y, si no hay permiso, solo escucho."),
        M("Pensar que un relato es de quien lo escuchó.", "El relato pertenece al pueblo que lo cuida.", "Digo quién lo contó y de qué comunidad viene."),
    ],
    R=[
        ex("Un relato oral se cuenta con: A) la voz B) un video obligatorio.", "A", "Oral significa contado con la voz."),
        ex("La cosmovisión es la manera en que un pueblo: A) ve y entiende el mundo B) cocina.", "A", "Cosmovisión es mirada del mundo."),
        ex("Si no hay permiso para grabar, ¿qué hago: grabo igual o solo escucho?", "solo escucho", "Sin permiso no se registra."),
    ],
    C=[
        ex("Tarjeta: «Quién cuenta: la abuela Rosa». ¿Qué dato de contexto responde eso: quién, dónde o cuándo?", "quién", "Dice la persona que cuenta."),
        ex("Verdadero o falso: un relato fundacional pertenece a quien lo escucha.", "Falso", "Pertenece al pueblo que lo cuida."),
        arith("La tarjeta de contexto debe tener 5 datos y una tiene 3 escritos. ¿Cuántos faltan?", "5 - 3", "Faltan los datos no escritos."),
    ],
    A=[
        ex("Ordena las acciones antes de escuchar: A) escucho en silencio B) leo la tarjeta de contexto C) pregunto si se puede registrar. Escribe las letras.", "B, C, A", "Primero sitúo, luego pregunto y por último escucho."),
        ex(RELATO + " ¿Cómo se llama el cerro?", "Alto Claro", "El relato dice el nombre del cerro."),
        ex(RELATO + " ¿Cuántos días subió Lía?", "tres", "El relato dice que subió tres días."),
    ],
    Z=[
        ex("Tarjeta: «Quién cuenta: don Luis. A quién: al curso. Registro: no permitido». Mateo quiere grabar para su casa. ¿Puede hacerlo? Responde Sí o No.", "No", "La tarjeta no permite registrar."),
        ex("Ana dice: «Ese relato lo escuché una vez, así que ahora es mío». ¿Qué le falta: A) decir de qué comunidad viene B) cambiarle el título?", "A", "Un relato tiene procedencia."),
    ],
    D=[
        arith("En una sala hay 4 tarjetas de contexto. Solo 1 está completa. ¿Cuántas tarjetas faltan por completar?", "4 - 1", "Faltan las que no están completas."),
        ex("Una persona quiere publicar un relato que le contaron, sin avisar. ¿Qué debe hacer primero: A) pedir permiso a quien lo contó B) elegir una foto?", "A", "El permiso es antes de publicar."),
    ],
    context=[ex("Un familiar de la escuela viene a contar un relato. Antes de que empiece, ¿qué datos del contexto preguntas: «¿quién cuenta, a quién, dónde, cuándo y para qué?» o «¿cuánto dura?»?", "«¿quién cuenta, a quién, dónde, cuándo y para qué?»", "Esos cinco datos sitúan el relato.")],
    selfcheck=[
        ex("¿Cómo se llama la manera en que un pueblo ve el mundo?", "cosmovisión", "Eso significa cosmovisión."),
        ex("¿Qué cinco datos tiene la tarjeta de contexto? Nombra uno.", "quién cuenta, a quién, dónde, cuándo o para qué", "Son los cinco datos del contexto."),
        ex("¿Quién decide si un relato se registra: la persona que escucha o quien lo cuenta?", "quien lo cuenta", "El permiso lo da quien lo cuenta y la comunidad."),
    ],
    task=T(
        "Completa una tarjeta de contexto de cinco datos para este relato de práctica inventado: «Alto Claro», contado por tu profesor/a o por otra persona adulta. Escribe quién cuenta, a quién, dónde, cuándo y para qué. Añade si hay permiso para registrar. Después pregunta al educador tradicional cómo se cuenta un relato real en su pueblo.",
        "Quién cuenta: mi profesora. A quién: a mi curso. Dónde: en la sala. Cuándo: hoy. Para qué: para practicar. Registro: no. Pregunta: ¿cómo se cuenta un relato real?",
        ["completa los cinco datos de contexto", "indica si hay permiso de registro", "formula una pregunta para quien enseña"],
        ["tarjeta escrita en el cuaderno"],
        ["omitir el permiso de registro", "tratar el relato inventado como si fuera de un pueblo"],
        "Valora que situó el relato; si omitió el permiso, pídele que lo agregue y que pregunte a quien enseña.",
    ),
    reinforce="Di en voz alta los cinco datos de contexto de un relato.",
    extend="Explica a una persona de tu casa por qué no se graba un relato sin permiso.",
)

L(
    LF1, 2,
    materials="Lápiz y hoja. El relato de práctica está escrito aquí y es inventado. Una persona puede leerlo en voz alta; si no, léelo tú en voz baja.",
    use="Aprenderé a escuchar un relato la primera vez solo para disfrutarlo y a anotar lo que sentí. Sirve para escuchar con atención antes de analizar.",
    prior=["Sé situar un relato con una tarjeta de contexto.", "Sé que algunos relatos no se pueden registrar."],
    explain=[
        "La primera vez que escucho un relato, solo disfruto. No interrumpo, no tomo notas largas y miro a quien cuenta. Escuchar con atención también es una forma de respeto hacia la persona y hacia lo que ella cuida.",
        "Al terminar, anoto tres cosas: qué sentí, qué imagen recuerdo y qué palabra me llamó la atención. Una emoción puede ser alegría, calma, curiosidad, sorpresa o tristeza. No hay emociones correctas o incorrectas: cada persona siente distinto.",
        "Después, en una segunda escucha, reviso los hechos: qué pasó, a quién le pasó y dónde. Hoy practico con el relato inventado «Alto Claro». Para un relato real en lengua indígena, el educador tradicional dice cuándo y cómo se puede escuchar y qué se puede comentar.",
    ],
    vocab=[("disfrutar", "gozar y sentirse a gusto con algo"), ("atención", "mirar y escuchar con cuidado"), ("emoción", "lo que siento: alegría, calma, sorpresa"), ("imagen", "lo que veo en mi mente cuando escucho"), ("interrumpir", "cortar a quien habla")],
    worked=[
        W("Primera escucha", RELATO + " Después de escucharlo, Paula dice sentir calma. ¿Qué anota Paula como emoción?", ["Busco la emoción que dice la persona.", "Dice calma."], "calma"),
        W("Qué hago mientras escucho", "Mientras don Luis cuenta, Beto quiere preguntar algo. ¿Qué hace Beto para respetar el relato?", ["Escuchar sin interrumpir.", "Anotar su duda y preguntar al final."], "Anota su duda y pregunta cuando termina"),
    ],
    mistakes=[
        M("Interrumpir para preguntar cada detalle.", "Corta el relato y quita atención a los demás.", "Anoto la duda y pregunto al final."),
        M("Decir «ese relato no me gustó» y no explicar nada.", "No dice qué sentí ni por qué.", "Digo qué sentí o qué imagen recuerdo."),
    ],
    R=[
        ex("La primera vez que escucho un relato, ¿para qué escucho: A) para disfrutarlo B) para dar una prueba?", "A", "La primera escucha es para disfrutar."),
        ex("Una emoción es: A) lo que siento B) el nombre del cerro.", "A", "Emoción es sentimiento."),
        ex("Si tengo una duda mientras alguien cuenta, ¿pregunto al final o interrumpo?", "pregunto al final", "Interrumpir corta el relato."),
    ],
    C=[
        ex(RELATO + " ¿Qué animales aparecen descansando bajo la sombra: A) los animales del cerro B) los peces?", "A", "El relato dice «los animales»."),
        ex("Verdadero o falso: hay una emoción correcta que todos deben sentir con un relato.", "Falso", "Cada persona siente distinto."),
        ex(RELATO + " ¿Qué llevó Lía al subir: una vasija de agua o una manta?", "una vasija de agua", "El relato menciona la vasija de agua."),
    ],
    A=[
        ex("Según la clase, ¿qué va primero? Ordena: A) anoto qué sentí B) escucho el relato completo sin interrumpir. Escribe las letras.", "B, A", "La primera vez solo escucho; las anotaciones van al terminar."),
        ex(RELATO + " ¿Qué regó Lía en la cima: una semilla o una piedra?", "una semilla", "El relato dice que regó una semilla."),
        arith("Imagina que Lía subió 3 días y volvió en 2 días. ¿Cuántos días caminó en total?", "3 + 2", "Sumo los días de ida y de vuelta."),
    ],
    Z=[
        ex("Dos comentarios sobre «Alto Claro». Eva: «Sentí calma cuando creció el árbol». Gaspar: «Fue aburrido». ¿Cuál dice qué sintió y en qué parte del relato?", "el de Eva", "Eva da emoción y momento del relato."),
        ex("Un compañero habla mientras escuchas. ¿Qué haces: A) mirar a quien cuenta y seguir escuchando B) gritarle?", "A", "Mantengo la atención sin faltar el respeto."),
    ],
    D=[
        arith("En un curso de 30 estudiantes, 12 dijeron que sintieron calma. ¿Cuántos NO dijeron calma?", "30 - 12", "Resto los que dijeron calma del total."),
        ex("Una niña dice: «El relato real no me lo contaron entero, así que lo completo yo». ¿Qué debe hacer: A) preguntar al educador tradicional qué falta B) inventar el final?", "A", "Inventar el final cambia un relato que no es suyo."),
    ],
    context=[ex("El educador tradicional va a contar un relato al curso. ¿Qué haces durante el relato: «escucho en silencio y miro a quien cuenta» o «converso con mi vecino»?", "«escucho en silencio y miro a quien cuenta»", "Es una forma de respeto y atención.")],
    selfcheck=[
        ex("¿Para qué escucho la primera vez un relato?", "para disfrutarlo", "La primera escucha es para disfrutar."),
        ex("Nombra una emoción que puede sentir una persona al escuchar un relato.", "calma, alegría, sorpresa, curiosidad o tristeza", "Todas son emociones posibles."),
        ex("¿Cuándo pregunto mis dudas?", "al final", "Así no interrumpo el relato."),
    ],
    task=T(
        "Escucha o lee en voz baja el relato de práctica «Alto Claro»: " + RELATO + " Después anota tres cosas: qué sentiste, qué imagen recuerdas y qué palabra te llamó la atención. Puedes dibujar la imagen. Si no quieres decir lo que sentiste, escribe una emoción de un personaje inventado.",
        "Sentí curiosidad. Recuerdo a la niña regando la semilla. La palabra que me llamó la atención fue «cima».",
        ["anota una emoción", "describe una imagen del relato", "elige una palabra del texto"],
        ["tres anotaciones en el cuaderno"],
        ["escribir solo «me gustó»", "copiar el relato completo"],
        "Valora que anotó emoción, imagen y palabra; no pidas que cuente vivencias personales. Si copió el relato, pídele que use sus palabras.",
    ),
    reinforce="Cuenta con tus palabras qué imagen recuerdas de «Alto Claro».",
    extend="Pide a una persona de tu casa que te cuente algo breve y cuéntale después qué sentiste al escucharla.",
)

SECUENCIA = "Relato de práctica (inventado): «Una vez, una laguna se secó. Primero, los patos se fueron. Después, Tomás cavó un canal. Luego llegó la lluvia por el canal. Al final, la laguna se llenó y volvieron los patos.»"

L(
    LF1, 3,
    materials="Lápiz y hoja. Los relatos de práctica están escritos aquí y son inventados.",
    use="Aprenderé a ordenar los hechos de un relato y a ver cómo un hecho lleva a otro. Sirve para comprender qué pasó y por qué.",
    prior=["Sé escuchar un relato la primera vez para disfrutarlo.", "Sé situar quién, dónde y cuándo."],
    explain=[
        "La secuencia es el orden en que pasan los hechos. Las palabras primero, después, luego y al final ayudan a ordenarlos. Cuando reconstruyo la secuencia, cuento un relato en orden con mis propias palabras sin cambiar sus hechos.",
        "Los hechos de un relato se relacionan. Una causa es lo que hace que algo pase. Un efecto es lo que pasa a consecuencia. Si una laguna se seca, los patos se van: la sequía es la causa y que se vayan los patos es el efecto. La palabra «porque» une causa y efecto.",
        "Cuando reconstruyo un relato no agrego hechos nuevos ni quito partes. Si no recuerdo una parte, vuelvo a escuchar. En un relato real, el educador tradicional cuida cómo se cuenta, y yo lo cuento solo si me dan permiso.",
    ],
    vocab=[("secuencia", "orden en que pasan los hechos"), ("causa", "lo que hace que algo pase"), ("efecto", "lo que pasa a consecuencia"), ("reconstruir", "volver a armar en orden"), ("hecho", "algo que pasa en un relato")],
    worked=[
        W("Ordenar hechos", SECUENCIA + " Ordena: A) llegó la lluvia B) la laguna se secó C) los patos se fueron.", ["Primero se secó la laguna.", "Después se fueron los patos.", "Luego llegó la lluvia."], "B, C, A"),
        W("Causa y efecto", "En el relato, los patos se fueron porque la laguna se secó. ¿Cuál es la causa y cuál el efecto?", ["La laguna seca hace que los patos se vayan.", "La causa es la laguna seca y el efecto es que se van los patos."], "Causa: la laguna se secó. Efecto: los patos se fueron"),
    ],
    mistakes=[
        M("Contar el final antes que el principio.", "Se pierde la secuencia y el relato no se entiende.", "Uso primero, después, luego y al final."),
        M("Agregar un personaje que no estaba.", "Cambia los hechos del relato.", "Cuento solo lo que escuché."),
    ],
    R=[
        ex("La secuencia es el orden en que pasan los hechos. ¿Qué palabra usamos para contar lo que pasa antes de todo lo demás: primero o al final?", "primero", "Primero indica el inicio de la secuencia."),
        ex("La causa es lo que hace que algo pase. «La laguna se seca» ¿es causa o efecto de que los patos se vayan?", "causa", "La sequía provoca que se vayan."),
        ex(SECUENCIA + " ¿Qué cavó Tomás: un canal o un pozo?", "un canal", "El relato dice que cavó un canal."),
    ],
    C=[
        ex(SECUENCIA + " ¿Qué pasó al final?", "la laguna se llenó y volvieron los patos", "Es la última parte del relato."),
        ex("Verdadero o falso: al reconstruir un relato puedo agregar un personaje nuevo.", "Falso", "Debo contar solo lo que se dijo."),
        ex(SECUENCIA + " ¿Qué palabra marca el último hecho: primero, luego o al final?", "al final", "El relato dice «Al final»."),
    ],
    A=[
        ex("Ordena según el relato de la laguna: A) la laguna se llenó B) Tomás cavó un canal C) los patos se fueron D) llegó la lluvia. Escribe las letras.", "C, B, D, A", "Se fueron los patos, Tomás cavó, llegó la lluvia y se llenó."),
        arith("Los patos se fueron 3 días antes de que Tomás cavara el canal. Tomás cavó durante 2 días. ¿Cuántos días pasaron en total desde que se fueron los patos hasta que terminó el canal?", "3 + 2", "Sumo los días de espera y de trabajo."),
        ex("Une la causa con su efecto: «llovió por el canal» y «la laguna se llenó». ¿Cuál es la causa?", "llovió por el canal", "La lluvia llena la laguna."),
    ],
    Z=[
        ex("Rita cuenta: «Primero se llenó la laguna y después se secó». ¿Respeta la secuencia del relato? Responde Sí o No.", "No", "En el relato primero se seca y después se llena."),
        ex("Dos explicaciones de por qué volvieron los patos. Eva: «Porque la laguna se llenó». Gaspar: «Porque sí». ¿Cuál usa una causa del relato?", "la de Eva", "La laguna llena es la causa."),
    ],
    D=[
        arith("Un relato tiene 5 hechos. En una reconstrucción, un niño contó 3 y olvidó el resto. ¿Cuántos hechos olvidó?", "5 - 3", "Faltan los hechos no contados."),
        ex("Al reconstruir un relato real contado por una persona de la comunidad, ¿debo cambiar el final si no me gusta? Responde Sí o No.", "No", "El relato pertenece a quien lo cuida y no se cambia."),
    ],
    context=[ex("Quieres contar a tu familia el relato de la laguna. ¿Qué haces: «lo cuento en el orden en que pasó» o «lo cuento empezando por el final»?", "«lo cuento en el orden en que pasó»", "Respeto la secuencia del relato.")],
    selfcheck=[
        ex("¿Cómo se llama el orden en que pasan los hechos?", "secuencia", "Eso es la secuencia."),
        ex("¿Qué palabra une una causa con su efecto?", "porque", "«Porque» une causa y efecto."),
        ex("Si no recuerdo una parte, ¿qué hago: invento o vuelvo a escuchar?", "vuelvo a escuchar", "No agrego hechos que no estaban."),
    ],
    task=T(
        "Reconstruye en cuatro frases el relato inventado de la laguna: " + SECUENCIA + " Usa las palabras primero, después, luego y al final. Después escribe una causa y su efecto que veas en el relato.",
        "Primero la laguna se secó. Después los patos se fueron. Luego Tomás cavó un canal. Al final volvió el agua. Causa: llovió. Efecto: la laguna se llenó.",
        ["escribe los cuatro hechos en orden", "usa las palabras de secuencia", "identifica una causa y un efecto"],
        ["cuatro frases escritas en el cuaderno"],
        ["alterar el orden de los hechos", "agregar hechos que no están"],
        "Valora que mantuvo el orden; si agregó hechos, pídele que vuelva a leer el relato.",
    ),
    reinforce="Cuenta en voz alta el relato de la laguna usando primero, después, luego y al final.",
    extend="Pide a una persona de tu casa que te cuente una historia corta y ordénala con esas cuatro palabras.",
)

L(
    LF1, 4,
    materials="Lápiz y hoja. El relato de práctica está escrito aquí y es inventado.",
    use="Aprenderé a dar una opinión sobre un relato usando datos del relato y a conectar con lo que conozco solo si quiero. Sirve para expresar lo que pienso sin tener que contar cosas privadas.",
    prior=["Sé ordenar los hechos de un relato.", "Sé reconocer emociones."],
    explain=[
        "Una opinión es lo que pienso o siento sobre algo. Una opinión fundamentada dice por qué lo pienso y se apoya en un dato del relato. Por ejemplo: «Me gustó que Tomás cavara el canal porque ayudó a que volviera el agua».",
        "También puedo conectar un relato con lo que ya conozco, como un lugar o un cuidado de la naturaleza. Pero nadie está obligado a contar cosas de su familia o de su vida. Puedo conectar con un ejemplo inventado, con un lugar que conozco por los libros o simplemente pasar.",
        "Para opinar uso tres pasos: digo qué pienso, digo porque y cito una parte del relato. Si el relato es real y viene de un pueblo, mi opinión no debe corregirlo ni burlarse. Si tengo una duda cultural, la pregunto al educador tradicional.",
    ],
    vocab=[("opinión", "lo que pienso o siento sobre algo"), ("fundamentar", "dar la razón de lo que digo"), ("conectar", "relacionar algo con otra cosa que conozco"), ("dato", "parte concreta del texto que apoya una idea"), ("respeto", "trato cuidadoso hacia otros y lo suyo")],
    worked=[
        W("Opinión fundamentada", SECUENCIA + " Opinión: «Me gustó que Tomás cavara el canal porque ayudó a que volviera el agua». ¿Qué dato del relato la apoya?", ["Busco la razón: ayudó a que volviera el agua.", "El relato dice que llegó la lluvia por el canal."], "Que la lluvia llegó por el canal"),
        W("Conectar sin contar de la familia", "Marta no quiere contar nada de su casa. ¿Cómo puede conectar con el relato de la laguna?", ["Puede usar un ejemplo inventado.", "O puede hablar del cuidado del agua en general, sin nombrar a su familia."], "Con un ejemplo inventado o general"),
    ],
    mistakes=[
        M("Decir «es lindo» sin dar razón.", "No se sabe por qué lo pienso.", "Agrego «porque» y un dato del relato."),
        M("Obligar a alguien a contar algo de su familia.", "No es seguro ni respetuoso.", "Ofrezco opciones: ejemplo inventado o pasar."),
    ],
    R=[
        ex("Una opinión fundamentada dice por qué lo pienso. ¿Qué palabra la introduce: porque o ayer?", "porque", "«Porque» introduce la razón."),
        ex("Conectar es relacionar un relato con: A) algo que ya conozco B) una pregunta sin respuesta.", "A", "Conectar es unir con lo que ya sé."),
        ex("Si no quiero hablar de mi casa, ¿puedo pasar o debo contarlo?", "puedo pasar", "Nadie está obligado a contar cosas privadas."),
    ],
    C=[
        ex("Opinión: «Me gustó que volvieran los patos porque la laguna se llenó». ¿Qué dato del relato apoya la opinión?", "la laguna se llenó", "Es la razón que da la opinión."),
        ex("Verdadero o falso: todos deben decir la misma opinión sobre un relato.", "Falso", "Cada persona puede pensar distinto, con razones."),
        ex("Ejemplo inventado: «Un niño cuida el agua de un riachuelo». ¿Conecta con el relato de la laguna: sí o no?", "sí", "Ambos tratan del cuidado del agua."),
    ],
    A=[
        ex("Ordena una opinión: A) cito una parte del relato B) digo qué pienso C) digo porque. Escribe las letras en el orden en que las usaría.", "B, C, A", "Primero opino, luego doy la razón y luego el dato."),
        arith("En un curso de 28 estudiantes, 10 opinaron sobre el relato en voz alta. ¿Cuántos estudiantes faltan por opinar?", "28 - 10", "Resto los que opinaron del total."),
        ex("Escribe «sí» o «no»: ¿«Me gustó porque Tomás ayudó a que volviera el agua» es una opinión fundamentada?", "sí", "Tiene razón y dato del relato."),
    ],
    Z=[
        ex("Eva: «Me gustó porque sí». Gaspar: «Me gustó porque los patos volvieron al final». ¿Quién fundamentó su opinión?", "Gaspar", "Gaspar dio un dato del relato."),
        ex("Un compañero se burla de la opinión de otro. ¿Qué haces: A) recuerdo que cada uno puede opinar con respeto B) me burlo yo también?", "A", "El respeto permite opiniones distintas."),
    ],
    D=[
        arith("De 20 comentarios del curso, 8 tenían razón con dato del relato. ¿Cuántos comentarios no tenían razón con dato?", "20 - 8", "Resto los comentarios fundamentados del total."),
        ex("Una persona opina sobre un relato real de un pueblo: «está mal contado». ¿Qué conviene hacer primero: A) preguntar al educador tradicional cómo se cuenta B) corregirlo ella misma?", "A", "La forma de contar la define la comunidad."),
    ],
    context=[ex("Tu curso escuchó un relato y te preguntan si quieres opinar. ¿Qué dices: «Me gustó cuando… porque…» o «No sé, no dije nada»?", "«Me gustó cuando… porque…»", "Es una opinión con razón.")],
    selfcheck=[
        ex("¿Cómo se llama dar la razón de lo que pienso?", "fundamentar", "Fundamentar es dar razones."),
        ex("¿Qué palabra uso para dar la razón?", "porque", "«Porque» introduce la razón."),
        ex("¿Estoy obligado a contar cosas de mi familia para opinar?", "No", "Puedo usar un ejemplo inventado o pasar."),
    ],
    task=T(
        "Escribe una opinión fundamentada sobre el relato de la laguna: " + SECUENCIA + " Usa este modelo: «Me gustó / no me gustó… porque… En el relato dice…». Después escribe una conexión con un ejemplo inventado sobre el cuidado del agua. No escribas nada de tu familia.",
        "Me gustó que los patos volvieran porque la laguna se llenó. En el relato dice «al final la laguna se llenó». Ejemplo inventado: un niño cuida el agua de un riachuelo.",
        ["escribe una opinión con razón y dato del relato", "conecta con un ejemplo inventado", "no cuenta nada privado"],
        ["opinión y conexión escritas en el cuaderno"],
        ["opinar sin razón", "contar cosas privadas de su casa"],
        "Valora que usó razón y dato; si contó algo privado, recuérdale que puede usar un ejemplo inventado.",
    ),
    reinforce="Di en voz alta tu opinión sobre el relato de la laguna con «porque» y un dato.",
    extend="Pide a una persona de tu casa su opinión sobre el relato y escucha su razón sin discutir.",
)

# =================================================================== OA LF02 · comunicación oral en lengua indígena
L(
    LF2, 1,
    materials="Lápiz y hoja. " + FICHA_PAL,
    use="Aprenderé a reconocer en qué situación hablo y con quién, antes de decir una expresión. Sirve para que mis palabras sean adecuadas y respetuosas.",
    prior=["Sé que «mari mari» e «iorana» son saludos.", "Sé que «chaltumay» y «maururu» significan gracias."],
    explain=[
        "Una situación comunicativa es el momento en que hablo con alguien. Tiene un interlocutor, que es la persona con quien hablo, un lugar y un propósito. No hablo igual con un amigo, con una abuela o con un educador tradicional.",
        "Antes de decir una expresión en lengua indígena pregunto: ¿con quién hablo?, ¿dónde estoy?, ¿para qué hablo? Un saludo como «mari mari» o «iorana» sirve para saludar, pero cuándo y a quién se dice lo enseñan el educador tradicional y la comunidad. En este cuaderno practico con diálogos inventados.",
        "Si no estoy seguro, pido ayuda: «¿puede enseñarme cómo se dice?». Pedir ayuda es parte de aprender una lengua. No tengo que saber todo, y nadie evalúa mi identidad por lo que sé o no sé decir.",
    ],
    vocab=[("situación comunicativa", "momento en que hablo con alguien"), ("interlocutor", "persona con quien hablo"), ("propósito", "para qué hablo"), ("saludo", "palabra o frase para empezar a conversar"), ("pedir ayuda", "preguntar a quien sabe para aprender")],
    worked=[
        W("Identificar interlocutor", "Diálogo inventado. Ana llega a la sala y dice «mari mari» a su educadora tradicional. ¿Quién es el interlocutor de Ana?", ["Busco con quién habla Ana.", "Habla con su educadora tradicional."], "Su educadora tradicional"),
        W("Elegir qué hacer si dudo", "Beto quiere saludar a una visita con una expresión de una ficha, pero no sabe si es adecuado. ¿Qué hace?", ["No está seguro.", "Pide ayuda al educador tradicional."], "Pregunta al educador tradicional antes de usarla"),
    ],
    mistakes=[
        M("Decir una expresión sin saber cuándo se usa.", "Puede no ser adecuada para esa situación.", "Pregunto al educador tradicional cuándo y a quién se dice."),
        M("Burlarse de quien no sabe decir una palabra.", "Todos estamos aprendiendo y la burla hiere.", "Ofrezco ayuda con respeto."),
    ],
    R=[
        ex("El interlocutor es: A) la persona con quien hablo B) el lugar donde está la sala.", "A", "Interlocutor es quien habla conmigo."),
        ex("«mari mari» es un saludo en: A) mapuzugun B) rapa nui.", "A", "La ficha dice que es mapuzugun."),
        ex("«iorana» es un saludo en: A) mapuzugun B) rapa nui.", "B", "La ficha dice que es rapa nui."),
    ],
    C=[
        ex("Verdadero o falso: hablo igual con un amigo que con una autoridad de la comunidad.", "Falso", "El interlocutor cambia la manera de hablar."),
        ex("La ficha dice: «chaltumay» es «gracias». ¿En qué lengua?", "mapuzugun", "La ficha lo indica."),
        ex("Si dudo si una expresión es adecuada, ¿pregunto al educador tradicional o la uso igual?", "pregunto al educador tradicional", "Él o ella sabe cuándo se usa."),
    ],
    A=[
        ex("Ordena antes de hablar: A) digo mi saludo B) miro con quién hablo C) pregunto si es adecuado. Escribe las letras.", "B, C, A", "Miro, pregunto y luego saludo."),
        ex("Diálogo inventado: Mateo dice «Maururu» a la educadora que le prestó un lápiz. ¿Qué quiso decir según la ficha?", "gracias", "«Maururu» es gracias en rapa nui."),
        arith("En una visita, 6 niños saludan con «mari mari» y 4 con «iorana». ¿Cuántos niños saludaron en total con estos dos saludos?", "6 + 4", "Sumo los dos grupos."),
    ],
    Z=[
        ex("Lalo dice: «Voy a usar esta expresión con todos porque la aprendí». ¿Qué debe preguntarse primero: A) con quién hablo y si es adecuado B) cuántas palabras sabe?", "A", "La situación y el interlocutor importan."),
        ex("Dos niños quieren decir «gracias» a un educador tradicional que enseña mapuzugun. Eva dice «chaltumay» y Gaspar dice «maururu». ¿Qué palabra de la ficha corresponde a mapuzugun?", "chaltumay", "«chaltumay» es gracias en mapuzugun."),
    ],
    D=[
        arith("Un curso tiene 5 situaciones para practicar y ya revisó 3. ¿Cuántas situaciones faltan por revisar?", "5 - 3", "Faltan las que no se han revisado."),
        ex("Una persona se ríe cuando un compañero dice mal una palabra. ¿Qué es mejor hacer: A) ofrecer ayuda con respeto B) seguir riéndose?", "A", "El respeto ayuda a aprender."),
    ],
    context=[ex("Llega un familiar a la escuela y quieres saludarlo con una expresión de la ficha. ¿Qué haces primero: «le pregunto al educador tradicional cuándo se usa» o «lo saludo sin pensar»?", "«le pregunto al educador tradicional cuándo se usa»", "Así uso la expresión de forma adecuada.")],
    selfcheck=[
        ex("¿Cómo se llama la persona con quien hablo?", "interlocutor", "Interlocutor es quien conversa conmigo."),
        ex("¿Qué significa «chaltumay» según la ficha?", "gracias", "Es gracias en mapuzugun."),
        ex("Si no sé algo, ¿qué hago?", "pido ayuda", "Pedir ayuda es parte de aprender."),
    ],
    task=T(
        "Elige una de estas tres situaciones inventadas: llegas a la sala y saludas a la educadora; recibes un lápiz prestado; llega una visita. Escribe con quién hablas, dónde estás, para qué hablas y qué expresión de la ficha podrías usar. Escribe también una pregunta para el educador tradicional sobre cuándo se usa esa expresión.",
        "Situación: recibo un lápiz prestado. Interlocutor: mi compañera. Lugar: la sala. Propósito: agradecer. Expresión: «chaltumay». Pregunta: ¿cuándo se dice chaltumay?",
        ["identifica interlocutor, lugar y propósito", "elige una expresión de la ficha", "escribe una pregunta al educador/a tradicional"],
        ["situación escrita en el cuaderno"],
        ["usar una expresión que no está en la ficha", "no preguntar cuándo se usa"],
        "Valora que reconoció la situación; si inventó una palabra, pídele que use solo las de la ficha y que pregunte a quien enseña.",
    ),
    reinforce="Di en voz alta con quién hablarías, dónde y para qué en una de las situaciones de la clase.",
    extend="Pregunta a una persona de tu casa cómo cambia su manera de saludar según con quién habla.",
)

L(
    LF2, 2,
    materials="Lápiz y hoja. " + FICHA_PAL,
    use="Aprenderé a ensayar las palabras de la ficha tal como me las enseñen y a pedir apoyo. Sirve para decir expresiones validadas sin inventar cómo suenan.",
    prior=["Sé reconocer la situación y el interlocutor.", "Sé usar la ficha de palabras."],
    explain=[
        "Una expresión validada es una palabra o frase que una persona de la comunidad o el educador tradicional ya confirmó. Las palabras de la ficha están validadas para practicar. No invento otras ni adivino cómo se dicen.",
        "Para ensayar hago cuatro pasos: escucho a quien sabe, repito en voz baja, repito con ayuda y uso la expresión en una situación real o de práctica. Si no escucho a nadie, no escribo cómo suena, porque no puedo inventar una pronunciación. En este cuaderno solo leo y escribo las palabras con la grafía que traen en la ficha.",
        "Cuando me equivoco, no pasa nada: pido ayuda y lo intento de nuevo. Una expresión tiene un significado y una situación de uso. Aprendo las dos cosas. Si me preguntan por una palabra que no sé, digo «aún no lo sé» y lo pregunto.",
    ],
    vocab=[("expresión validada", "palabra o frase confirmada por quien sabe"), ("ensayar", "practicar para hacerlo mejor"), ("grafía", "forma de escribir una palabra"), ("pronunciación", "cómo suena una palabra al decirla"), ("apoyo", "ayuda de otra persona")],
    worked=[
        W("Pasos de ensayo", "Marta quiere practicar «ko». ¿Qué hace primero según los cuatro pasos?", ["El primer paso es escuchar a quien sabe.", "No inventa cómo suena."], "Escucha a quien sabe"),
        W("Significado y uso", "Ficha: «antü» es sol. Rita dice que «antü» es luna. ¿Qué debe hacer?", ["Mira la ficha: antü es sol y kuyen es luna.", "Corrige su error y repite."], "Corrige: antü es sol y kuyen es luna"),
    ],
    mistakes=[
        M("Escribir cómo suena una palabra con letras que invento.", "No sé cómo se pronuncia y puedo cambiar el sentido.", "Escribo solo la grafía de la ficha y pido que me la enseñen en voz alta."),
        M("Cambiar una letra porque me parece parecida.", "Una letra distinta puede cambiar la palabra.", "Copio la palabra letra por letra de la ficha."),
    ],
    R=[
        ex("Una expresión validada es una que: A) confirmó una persona que sabe B) inventé yo.", "A", "Validada significa confirmada por quien sabe."),
        ex("Según la ficha, «kuyen» es: A) sol B) luna.", "B", "La ficha lo dice."),
        ex("Según la ficha, «ko» es: A) agua B) tierra.", "A", "La ficha lo dice."),
    ],
    C=[
        ex("Verdadero o falso: puedo escribir cómo suena una palabra con letras que invento.", "Falso", "No sé cómo suena y puedo equivocarme."),
        ex("Ordena los pasos de ensayo: A) repito con ayuda B) escucho a quien sabe C) repito en voz baja. Escribe las letras de los tres primeros pasos.", "B, C, A", "Primero escucho, luego repito y luego repito con ayuda."),
        ex("¿Qué palabra de la ficha significa tierra?", "mapu", "La ficha dice «mapu» es tierra."),
    ],
    A=[
        ex("¿Qué palabra de la ficha empieza con la letra ñ?", "ñuke", "En la ficha, «ñuke» (madre) es la única que empieza con ñ."),
        ex("La ficha escribe «ruka». Si copio «ruca», ¿quedó escrita igual que en la ficha: sí o no?", "no", "Las letras no son las mismas; en este cuaderno copio la grafía de la ficha y pregunto al educador tradicional por otras formas."),
        arith("Practicas 3 palabras de la ficha cada día durante 4 días. ¿Cuántas palabras practicaste?", "3 * 4", "Multiplico palabras por día por los días."),
    ],
    Z=[
        ex("Lola dice: «Voy a usar esta palabra que me la inventé porque suena parecida». ¿Qué error comete: A) inventa una palabra B) usa la ficha?", "A", "Una palabra inventada no es validada."),
        ex("Dos niños copian «antü». Eva escribe «antü» y Gaspar escribe «antu». ¿Quién copió exactamente la ficha?", "Eva", "Eva escribió la ü igual que la ficha."),
    ],
    D=[
        arith("En una lista hay 6 palabras de la ficha. Ya ensayaste 2. ¿Cuántas faltan por ensayar?", "6 - 2", "Resto las ensayadas del total."),
        ex("Una persona dice «aún no lo sé» cuando le preguntan una palabra. ¿Es una respuesta válida: sí o no?", "sí", "Decir que aún no lo sabe es honesto y respetuoso."),
    ],
    context=[ex("Quieres decir «agua» en mapuzugun. ¿Qué haces: «uso «ko» de la ficha y pido que me la enseñen en voz alta» o «invento una palabra que suene bonita»?", "«uso «ko» de la ficha y pido que me la enseñen en voz alta»", "Uso solo palabras validadas y aprendo su sonido de quien sabe.")],
    selfcheck=[
        ex("¿Qué significa «antü» en la ficha?", "sol", "La ficha dice sol."),
        ex("¿Cuál es el primer paso para ensayar una palabra?", "escuchar a quien sabe", "Primero escucho a quien sabe."),
        ex("Si me equivoco, ¿qué hago?", "pido ayuda y lo intento de nuevo", "Equivocarse es parte de aprender."),
    ],
    task=T(
        "Elige tres palabras de la ficha. Para cada una escribe la palabra con su grafía exacta y su significado. Después escribe cómo vas a ensayar: a quién le vas a pedir que te la diga en voz alta y en qué momento. No escribas cómo suenan.",
        "ko: agua. antü: sol. mapu: tierra. La ensayo con el educador tradicional el lunes. Le pido que la diga en voz alta.",
        ["copia tres palabras con grafía exacta", "escribe su significado", "dice a quién pedirá ayuda"],
        ["tres palabras escritas con su significado"],
        ["cambiar una letra", "escribir cómo suena sin haberlo escuchado"],
        "Valora que copió con exactitud; si cambió letras, pídele que compare con la ficha.",
    ),
    reinforce="Mira la ficha, cubre el significado y di el de dos palabras.",
    extend="Pide a una persona de tu casa que te pregunte el significado de dos palabras de la ficha.",
)

DIALOGO = "Diálogo de práctica (inventado): Ana: «Mari mari». Educadora: «Buenos días, Ana». Ana: «Hoy quiero aprender una palabra». Educadora: «Veamos ko; es agua en mapuzugun». Ana: «Chaltumay»."

L(
    LF2, 3,
    materials="Lápiz y hoja. " + FICHA_PAL,
    use="Aprenderé a sostener un diálogo breve con turnos: saludo, idea, escucha y agradecimiento. Sirve para conversar con respeto sobre algo del mundo, usando expresiones de la ficha.",
    prior=["Sé reconocer la situación y el interlocutor.", "Sé que solo uso expresiones validadas."],
    explain=[
        "Un diálogo es una conversación entre dos o más personas que hablan por turnos. En un diálogo breve hay cuatro partes: un saludo, una idea o comentario, la escucha de lo que responde la otra persona y un agradecimiento o despedida.",
        "Mi idea o comentario puede ser sobre algo de la naturaleza o del mundo que observé, por ejemplo el agua o el sol. Digo la idea en castellano y puedo usar una palabra o expresión de la ficha cuando corresponde. Por ejemplo: «El ko, el agua, es importante para las plantas». La palabra de la ficha va tal como está escrita.",
        "Escuchar es tan importante como hablar. Espero mi turno, miro a la persona y respondo a lo que dijo. Si no entiendo, pregunto: «¿puede repetir?». Qué expresiones tradicionales usar y cuándo lo enseñan el educador tradicional y la comunidad.",
    ],
    vocab=[("diálogo", "conversación por turnos"), ("turno", "momento en que me toca hablar"), ("comentario", "idea que digo sobre un tema"), ("despedida", "palabras para terminar una conversación"), ("escuchar", "atender a lo que otra persona dice")],
    worked=[
        W("Partes de un diálogo", DIALOGO + " ¿Qué parte del diálogo es el saludo?", ["Busco lo primero que dice Ana.", "Dice «Mari mari»."], "«Mari mari»"),
        W("Responder a lo que dice el otro", "La educadora dice: ««ko» es agua en mapuzugun». ¿Qué responde bien Ana: A) «Chaltumay», gracias B) «¿Y la tarea?»", ["Ana agradece lo que le enseñaron.", "La respuesta A responde a lo que se dijo."], "A"),
    ],
    mistakes=[
        M("Hablar a la vez que otra persona.", "No escucho y no se entiende.", "Espero mi turno."),
        M("Decir una idea que no tiene relación con lo que se conversa.", "El diálogo pierde sentido.", "Respondo a lo que dijo la otra persona."),
    ],
    R=[
        ex("En un diálogo se habla: A) por turnos B) todos a la vez.", "A", "Dialogar es hablar por turnos."),
        ex(DIALOGO + " ¿Quién dijo «Chaltumay»?", "Ana", "Ana lo dice al final."),
        ex("Un buen saludo al comenzar un diálogo es «mari mari». ¿Es un saludo o una despedida?", "saludo", "La ficha dice que es un saludo."),
    ],
    C=[
        ex(DIALOGO + " ¿Qué palabra aprendió Ana?", "ko", "La educadora le enseñó «ko»."),
        ex("Verdadero o falso: para dialogar basta con hablar; no hace falta escuchar.", "Falso", "Escuchar es parte del diálogo."),
        ex("Si no entiendo lo que dijo la otra persona, ¿qué digo: «¿puede repetir?» o nada?", "«¿puede repetir?»", "Pedir que repita ayuda a entender."),
    ],
    A=[
        ex("Ordena las partes de un diálogo breve: A) agradezco B) saludo C) comento una idea D) escucho la respuesta. Escribe las letras.", "B, C, D, A", "Saludo, comento, escucho y agradezco."),
        arith("En un diálogo, Ana habla 3 veces y la educadora 2 veces. ¿Cuántos turnos hubo?", "3 + 2", "Sumo los turnos de las dos personas."),
        ex("Completa el comentario: «El ___ es importante para las plantas». Usa la palabra de la ficha que significa agua.", "ko", "La ficha dice «ko» es agua."),
    ],
    Z=[
        ex("Rita responde: «Chaltumay» cuando la educadora le enseña una palabra. Gaspar responde: «No me importa». ¿Quién responde respetando el diálogo?", "Rita", "Rita agradece lo que le enseñan."),
        ex("Una niña usa «antü» para decir «luna» en su diálogo. ¿Qué error cometió: A) confundió una palabra de la ficha B) no saludó?", "A", "«antü» es sol, no luna."),
    ],
    D=[
        arith("Un diálogo de práctica tiene 8 turnos. Ya escribiste 5. ¿Cuántos turnos faltan?", "8 - 5", "Faltan los turnos no escritos."),
        ex("Dos personas conversan y una usa la palabra «ruka». ¿Qué significa según la ficha?", "casa", "La ficha dice «ruka» es casa."),
    ],
    context=[ex("Llega una persona nueva a tu sala y quieres conversar con ella sobre el agua. ¿Qué haces primero: «la saludo» o «le hablo sin mirarla»?", "«la saludo»", "El diálogo empieza con un saludo.")],
    selfcheck=[
        ex("¿Cuántas partes tiene un diálogo breve según esta clase?", "4", "Son saludo, idea, escucha y agradecimiento."),
        ex("¿Qué es un turno?", "el momento en que me toca hablar", "Dialogar es hablar por turnos."),
        ex("¿Qué digo si no entendí?", "¿puede repetir?", "Pedir que repita ayuda a entender."),
    ],
    task=T(
        "Escribe un diálogo de al menos cuatro turnos con una persona inventada. Debe tener saludo, un comentario sobre el agua o el sol, una respuesta de la otra persona y un agradecimiento. Usa al menos una palabra de la ficha. " + FICHA_PAL,
        "Yo: «Mari mari». Persona: «Hola». Yo: «El antü, el sol, da luz a las plantas». Persona: «Es cierto». Yo: «Chaltumay».",
        ["incluye saludo, comentario, respuesta y agradecimiento", "usa una palabra de la ficha con su grafía", "respeta los turnos"],
        ["diálogo escrito en el cuaderno"],
        ["no incluir respuesta de la otra persona", "usar palabras que no están en la ficha"],
        "Valora que el diálogo tenga las cuatro partes; si usó una palabra inventada, pídele que use solo las de la ficha.",
    ),
    reinforce="Practica en voz alta tu diálogo con una persona de tu casa o con un peluche.",
    extend="Pregunta a una persona de tu casa qué dice al saludar y al despedirse.",
)

L(
    LF2, 4,
    materials="Lápiz y hoja. " + FICHA_PAL,
    use="Aprenderé que una lengua puede tener variantes y que cada una merece respeto. Sirve para comunicarme sin burlarme de cómo habla otra persona.",
    prior=["Sé sostener un diálogo breve.", "Sé usar solo expresiones validadas."],
    explain=[
        "Una variante es una manera distinta de decir o escribir lo mismo, según el lugar o la comunidad. Todas las lenguas tienen variantes: en castellano, por ejemplo, un mismo objeto puede tener distintos nombres en distintos lugares. Las lenguas indígenas también pueden tenerlas.",
        "Una variante no es un error. Si una persona dice una palabra distinta a la de la ficha, no es mejor ni peor: puede venir de otro lugar. Lo que hago es preguntar: «¿de dónde viene esta forma?, ¿puede enseñarme?». Qué variante usa cada comunidad, cómo se escribe y cómo suena lo explican el educador tradicional y la comunidad.",
        "Cuando comunico algo, respeto la variante de la persona que enseña. No la corrijo ni me burlo, y tampoco invento una variante nueva. Si quiero usar una expresión de la ficha y la persona que enseña usa otra forma, aprendo la forma de esa persona.",
    ],
    vocab=[("variante", "forma distinta de decir o escribir lo mismo"), ("territorio", "lugar donde vive una comunidad"), ("respetar", "tratar con cuidado y sin burla"), ("corregir", "cambiar algo para que quede bien"), ("comunidad", "grupo de personas que comparten territorio y cultura")],
    worked=[
        W("Variante no es error", "Una niña dice una palabra distinta a la de la ficha para el mismo significado. Una compañera dice que está mal. ¿Qué es mejor responder?", ["Puede ser otra variante.", "Preguntamos de dónde viene y no corregimos."], "Preguntar de dónde viene esa forma"),
        W("Aprender la variante de quien enseña", "El educador tradicional usa una forma distinta a la de la ficha. ¿Qué forma aprende Marta?", ["Quien enseña define su variante.", "Marta aprende la forma del educador."], "La forma del educador tradicional"),
    ],
    mistakes=[
        M("Decir «tú lo dices mal» cuando otra persona usa otra variante.", "Una variante no es un error.", "Pregunto con curiosidad de dónde viene."),
        M("Inventar una nueva variante.", "No tengo saber para crearla.", "Aprendo la que me enseñan."),
    ],
    R=[
        ex("Una variante es: A) una forma distinta de decir o escribir lo mismo B) un error siempre.", "A", "Variante no es error."),
        ex("Si una persona usa otra variante, ¿me burlo o pregunto con respeto?", "pregunto con respeto", "La burla no ayuda a aprender."),
        ex("Las variantes pueden venir de distintos: A) lugares y comunidades B) colores de lápiz.", "A", "Dependen del lugar y la comunidad."),
    ],
    C=[
        ex("Verdadero o falso: toda palabra diferente a la de la ficha es un error.", "Falso", "Puede ser otra variante."),
        ex("Si el educador tradicional enseña una forma distinta a la ficha, ¿cuál aprendo: la de quien enseña o la que me parece mejor?", "la de quien enseña", "Quien enseña conoce su variante."),
        ex("¿Quién explica qué variante usa una comunidad: el educador tradicional o un compañero que no sabe?", "el educador tradicional", "Él o ella conoce la lengua de su comunidad."),
    ],
    A=[
        ex("Oyes una variante que no conocías. ¿Qué haces: A) pregunto con respeto de dónde viene y aprendo la forma de quien enseña B) la cambio por la de la ficha sin avisar?", "A", "Una variante no es un error: pregunto y aprendo de quien enseña."),
        arith("Un curso conoce 3 variantes de una palabra en castellano y escuchó 2 más. ¿Cuántas variantes distintas conoce ahora?", "3 + 2", "Sumo las variantes conocidas y las nuevas."),
        ex("Dos niñas dicen un mismo objeto con nombres distintos en castellano. ¿Cuál es la manera correcta de reaccionar: A) preguntar de dónde viene cada nombre B) decir que una está equivocada?", "A", "Cada forma puede tener un origen."),
    ],
    Z=[
        ex("Eva: «La forma de mi abuela es distinta, pero también es buena». Gaspar: «Solo la ficha está bien». ¿Quién respeta las variantes?", "Eva", "Eva acepta que hay distintas formas."),
        ex("Una persona quiere crear una forma nueva «para unificar» las variantes. ¿Qué debe hacer primero: A) preguntar al educador tradicional y a la comunidad B) decidir ella misma?", "A", "Las decisiones sobre la lengua las toma la comunidad."),
    ],
    D=[
        arith("En un curso, 12 estudiantes oyeron una variante nueva y 7 la repitieron con ayuda. ¿Cuántos NO la repitieron?", "12 - 7", "Resto los que repitieron del total."),
        ex("Un compañero corrige a otro: «lo dices mal». ¿Qué le puedes decir: A) «Quizás es otra variante; preguntemos» B) «Sí, está mal»?", "A", "Una variante no es un error."),
    ],
    context=[ex("Una visita usa una forma de saludar distinta a la de tu ficha. ¿Qué haces: «le pregunto con respeto de dónde viene esa forma» o «le digo que está equivocada»?", "«le pregunto con respeto de dónde viene esa forma»", "Una variante no es un error y se respeta.")],
    selfcheck=[
        ex("¿Cómo se llama una forma distinta de decir lo mismo?", "variante", "Eso es una variante."),
        ex("¿Una variante es un error?", "No", "Es otra manera válida de decir o escribir."),
        ex("¿Quién explica las variantes de una comunidad?", "el educador tradicional y la comunidad", "Ellos conocen su lengua."),
    ],
    task=T(
        "Escribe una pequeña guía de tres frases para tu curso sobre cómo respetar las variantes cuando alguien usa una forma distinta. Incluye una frase que no corrija, una que pregunte con respeto y una que invite a aprender de la persona que enseña. Escribe también una pregunta para el educador tradicional sobre las variantes de su lengua.",
        "1) No digo que está mal. 2) Pregunto: ¿de dónde viene esa forma? 3) Aprendo la forma de quien enseña. Pregunta: ¿qué variante usa su comunidad?",
        ["escribe tres frases respetuosas", "no corrige ni se burla", "formula una pregunta para quien enseña"],
        ["guía escrita en el cuaderno"],
        ["decir que una variante está mal", "inventar una variante"],
        "Valora que respetó las variantes; si corrigió, pídele que lo reformule como pregunta.",
    ),
    reinforce="Di en voz alta una frase para preguntar de dónde viene una forma distinta.",
    extend="Pregunta a una persona de tu casa si conoce un objeto que tenga dos nombres en distintos lugares.",
)
