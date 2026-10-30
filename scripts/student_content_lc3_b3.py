"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF04 (escritura de oraciones con expresiones y palabras para nombrar y caracterizar) y OA LF05 (recursos
tecnológicos para expresar ideas, hechos o sentimientos en creaciones audiovisuales o escritas).

Criterio de autoría: las oraciones modelo, los planes y las fichas de práctica son inventados y están en castellano;
solo incorporan palabras de lengua indígena ya atestiguadas y con su ficha (ko, antü, kuyen, ruka, mapu, ñuke en
mapuzugun; mari mari, chaltumay, iorana, maururu). Cómo se construye una oración completa, qué palabras sirven para
caracterizar y cómo se escribe en la lengua las enseña el educador/a tradicional: el cuaderno solo practica copiar
con exactitud y revisar. En LF05 no se publica nada ni se graba a nadie sin permiso: todo queda en casa o en el curso,
con un adulto. No se nombran marcas ni programas.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LF4, LF5 = "LC03 OA LF04", "LC03 OA LF05"

CONSULT = " Recuerda: la forma tradicional de escribir y usar estas palabras la enseñan el educador o la educadora tradicional y tu comunidad. Consúltales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de escritura, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

FICHA_PAL = "Ficha de palabras en mapuzugun: «ko» es agua, «antü» es sol, «kuyen» es luna, «ruka» es casa, «mapu» es tierra, «ñuke» es madre."
FICHA_EXP = "Ficha de expresiones: «mari mari» es un saludo en mapuzugun y «chaltumay» es «gracias» en mapuzugun."


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


# =================================================================== LF04 · oraciones con palabras para nombrar y caracterizar
L(
    LF4, 1,
    materials="Lápiz y hoja. La ficha y las oraciones modelo están escritas en este cuaderno. Son inventadas, están en castellano y traen una palabra de la ficha.",
    use="Aprenderé a observar cómo una oración nombra algo con una palabra en lengua indígena y a copiarla con exactitud. Sirve para escribir con cuidado y respetar la grafía.",
    prior=["Sé leer una palabra de la ficha con su significado.", "Sé que no invento palabras en lengua indígena."],
    explain=[
        "Nombrar es decir cómo se llama algo. Para escribir oraciones con una palabra en lengua indígena, primero observo un modelo. Veo cuál es la palabra, qué significa según la ficha y cómo se escribió.",
        "Después copio la palabra igual al modelo, letra por letra. Cuido las letras especiales como la ñ y la ü. Si cambio una letra, puedo escribir otra palabra. La copio mirando la ficha, no de memoria.",
        "En este cuaderno las oraciones están en castellano y llevan la palabra entre comillas, con su significado al lado. Cómo se arma una oración completa en la lengua indígena lo enseña el educador o la educadora tradicional. Yo no invento esa parte.",
    ],
    vocab=[("nombrar", "decir cómo se llama algo"), ("modelo", "ejemplo que miro para copiar la forma"), ("copiar", "escribir igual a lo que veo"), ("grafía", "la manera de escribir una palabra con sus letras"), ("oración", "grupo de palabras que dice una idea completa")],
    worked=[
        W("Encontrar la palabra que nombra", "Oración modelo: «Vi «kuyen», la luna, en el cielo.» " + FICHA_PAL + " ¿Qué palabra de la oración nombra la luna en mapuzugun?", ["Busco la palabra entre comillas.", "Es «kuyen».", "La ficha confirma que «kuyen» es luna."], "«kuyen»"),
        W("Contar las palabras", "Oración modelo: «Vi «kuyen», la luna, en el cielo.» ¿Cuántas palabras tiene?", ["Cuento una por una: Vi, kuyen, la, luna, en, el, cielo.", "Son siete.", "Reviso otra vez y son 7."], "7 palabras"),
    ],
    mistakes=[
        M("Cambiar una letra porque «suena igual».", "Puedo escribir otra palabra o una forma que no es.", "Copio letra por letra mirando la ficha."),
        M("Escribir la palabra de memoria sin mirar el modelo.", "Puedo olvidar una ñ o una ü.", "Miro el modelo mientras copio y lo comparo al final."),
    ],
    R=[
        ex("Nombrar es: A) decir cómo se llama algo B) decir dónde está algo.", "A", "Nombrar es decir el nombre."),
        ex("Oración: «Vi «kuyen», la luna, en el cielo.» ¿Qué palabra está entre comillas?", "kuyen", "La palabra en mapuzugun va entre comillas."),
        ex(FICHA_PAL + " ¿Qué nombra la palabra «ko»?", "agua", "La ficha dice que «ko» es agua."),
    ],
    C=[
        ex("Verdadero o falso: copiar una palabra de la ficha es escribirla igual, letra por letra.", "Verdadero", "Copiar es escribir igual."),
        ex("¿Cuál copia bien la palabra «ñuke»? A) ñuke B) nuke C) ñuque", "A", "Es la que conserva todas las letras de la ficha."),
        ex("Oración: «Entré a la «ruka», la casa, y saludé.» ¿Qué nombra «ruka»?", "la casa", "La oración la explica con «la casa»."),
    ],
    A=[
        ex("¿Cuántas palabras tiene la oración «Tomé «ko», agua fresca, en el recreo.»?", "7", "Cuento: Tomé, ko, agua, fresca, en, el, recreo."),
        ex("Dos oraciones: 1) «Miré «antü», el sol, y era muy brillante.» 2) «Pisé «mapu», la tierra, y estaba mojada.» ¿Qué palabra en mapuzugun aparece en la segunda?", "mapu", "La segunda tiene «mapu» entre comillas."),
        ex(FICHA_PAL + " Oración: «Pisé «mapu», la tierra, y estaba mojada.» ¿Qué dice la ficha que significa «mapu»?", "tierra", "La ficha dice que «mapu» es tierra."),
    ],
    Z=[
        ex("Pedro escribió «kuien» en vez de «kuyen», porque suenan igual. ¿Está bien? Responde Sí o No.", "No", "Se copia igual a la ficha."),
        ex("La ficha no trae la palabra para «perro». Ana inventa una. ¿Está bien? Responde Sí o No.", "No", "No se inventan palabras en lengua indígena."),
    ],
    D=[
        ex("Ordena los pasos para copiar: C) comparo mi copia con la ficha A) leo la palabra y su significado B) la escribo letra por letra. Escribe las letras.", "A, B, C", "Leo, escribo y luego compruebo."),
        arith("La ficha tiene 6 palabras y ya copiaste 4. ¿Cuántas te faltan?", "6 - 4", "Resto las copiadas del total."),
    ],
    context=[ex(FICHA_PAL + " En el cuaderno de un compañero lees «Vi «kuyen», la luna». Tú ves que escribió «kuien». ¿Qué le dices: «Compáralo con la ficha» o «Así está bien»?", "«Compáralo con la ficha»", "La ficha dice que se escribe «kuyen».")],
    selfcheck=[
        ex("¿Cómo se llama decir cómo se llama algo?", "nombrar", "Nombrar es decir el nombre."),
        ex("¿Qué miro mientras copio una palabra?", "la ficha", "La ficha tiene la grafía correcta."),
        ex("¿Quién enseña cómo se arma una oración en la lengua indígena?", "el educador tradicional o la comunidad", "Yo no invento esa parte."),
    ],
    task=T(
        "Usa la ficha de palabras y esta oración modelo: «Entré a la «ruka», la casa, y saludé.» Copia la oración en tu cuaderno cuidando cada letra. Subraya la palabra en mapuzugun y escribe su significado según la ficha. Después copia otra palabra de la ficha (a tu elección entre ko, antü, kuyen, mapu o ñuke) con su significado. Termina con una pregunta para la educadora tradicional sobre cómo se arma una oración en la lengua.",
        "Entré a la «ruka», la casa, y saludé. Subrayado: ruka = casa. Otra palabra: ko = agua. Pregunta: ¿cómo se dice una oración completa con «ko»?",
        ["copia la oración sin cambiar letras", "subraya la palabra y escribe su significado", "copia otra palabra de la ficha", "hace una pregunta a la educadora"],
        ["oración copiada en el cuaderno", "pregunta escrita o dicha en voz alta"],
        ["cambiar letras de la palabra", "inventar una oración en la lengua indígena"],
        "Valora la exactitud de la copia; si inventó palabras, pídele que las reemplace por una palabra de la ficha.",
    ),
    reinforce="Copia con mucho cuidado la palabra «ñuke» tres veces y compara con la ficha.",
    extend="Observa otra oración modelo de esta clase y cuenta cuántas palabras tiene en castellano y cuántas en mapuzugun.",
)

L(
    LF4, 2,
    materials="Lápiz y hoja. La ficha y los datos de práctica están escritos aquí. Los lugares y objetos son inventados.",
    use="Aprenderé a caracterizar, que es decir cómo es algo, para que una oración diga más. Sirve para describir con palabras claras y respetuosas.",
    prior=["Sé copiar una palabra de la ficha.", "Sé que una oración nombra algo."],
    explain=[
        "Caracterizar es decir cómo es algo. Si nombro la casa, puedo agregar cómo es: grande, pequeña, alta o tranquila. Estas palabras que dicen cómo es algo ayudan a que mi oración sea más clara.",
        "Una característica debe ser pertinente. Pertinente quiere decir que sirve para ese caso y es verdadera. Si el dibujo muestra una casa pequeña, digo pequeña, no grande. Para caracterizar uso palabras que conozco en castellano.",
        "No invento palabras en lengua indígena para caracterizar. Cuáles existen y cómo se usan lo enseña el educador o la educadora tradicional. Mi trabajo es observar bien, elegir una característica verdadera y escribirla con cuidado.",
    ],
    vocab=[("caracterizar", "decir cómo es algo"), ("característica", "una cualidad de algo, como grande o fresca"), ("pertinente", "que sirve para ese caso y es verdadera"), ("describir", "contar cómo es algo con palabras"), ("verdadera", "que coincide con lo que veo")],
    worked=[
        W("Elegir la característica pertinente", "Dibujo de práctica: una «ruka», la casa, con el techo bajo y pocas ventanas; es pequeña. ¿Qué característica es pertinente: pequeña o enorme?", ["Miro el dibujo: techo bajo y pocas ventanas.", "Pequeña coincide con lo que veo.", "Enorme no coincide."], "pequeña"),
        W("Unir nombre y característica", "Quiero escribir una oración con «ko», agua, que sale de una llave fría. ¿Qué característica uso?", ["Nombro: «ko», agua.", "Observo: sale de una llave fría.", "Agrego: fresca. La oración: «Tomé «ko», agua fresca»."], "agua fresca"),
    ],
    mistakes=[
        M("Elegir una característica que no coincide con lo que veo.", "La oración deja de ser verdadera.", "Observo primero y después escribo."),
        M("Inventar una palabra en lengua indígena para decir cómo es algo.", "No sé si esa palabra existe.", "Uso castellano y pregunto al educador tradicional."),
    ],
    R=[
        ex("Caracterizar es decir: A) cómo es algo B) cómo se llama algo.", "A", "Caracterizar es decir cómo es."),
        ex("«Fresca» en «agua fresca» es una característica del agua. ¿Es verdadero o falso?", "Verdadero", "Dice cómo es el agua."),
        ex("Pertinente quiere decir que la característica: A) sirve y es verdadera B) suena larga.", "A", "Pertinente es que sirve y es verdadera."),
    ],
    C=[
        ex("Dibujo de práctica: una luna llena, que se ve redonda. ¿Qué característica es pertinente: redonda o cuadrada?", "redonda", "Coincide con lo que se ve."),
        ex("Verdadero o falso: puedo inventar una palabra en lengua indígena para decir cómo es algo.", "Falso", "Eso lo enseña el educador tradicional."),
        ex("Oración: «Miré «antü», el sol, y era muy brillante.» ¿Cuál es la característica del sol?", "brillante", "Dice cómo es el sol."),
    ],
    A=[
        ex("Dibujo de práctica: una «ruka» (casa) con techo alto y varias ventanas; es grande. ¿Qué característica escribes: grande o diminuta?", "grande", "Coincide con el dibujo."),
        ex("Une cada palabra con una característica pertinente. 1) «ko» agua de una llave fría 2) «kuyen» luna llena. Opciones: fresca, redonda. Escribe las dos en orden.", "fresca, redonda", "El agua fría es fresca y la luna llena se ve redonda."),
        arith("En un dibujo hay 3 casas pequeñas y 2 casas grandes. ¿Cuántas casas hay en total?", "3 + 2", "Sumo las pequeñas y las grandes."),
    ],
    Z=[
        ex("Luis dijo: «Mi «ruka» es pequeña» mirando un dibujo de una casa grande. ¿Su característica es pertinente? Responde Sí o No.", "No", "No coincide con el dibujo."),
        ex("Ana no sabe una palabra en lengua indígena para decir «alta». ¿Qué es mejor: inventarla o usar «alta» en castellano y preguntar a la educadora?", "usar «alta» en castellano y preguntar a la educadora", "No se inventan palabras en lengua indígena."),
    ],
    D=[
        ex("Oración: «Pisé «mapu», la tierra, y estaba mojada.» Después de la lluvia, ¿es pertinente «mojada» para la tierra? Responde Sí o No.", "Sí", "La tierra después de la lluvia se moja."),
        arith("Escribes 4 oraciones y a cada una le agregas 2 características. ¿Cuántas características escribes?", "4 * 2", "Cuatro oraciones por dos características."),
    ],
    context=[ex("Miras desde la ventana y ves una casa pequeña con una sola ventana. Quieres escribir «Vi una «ruka», la casa, ____». ¿Qué completas: «pequeña» o «enorme»?", "«pequeña»", "Coincide con lo que veo.")],
    selfcheck=[
        ex("¿Qué hago al caracterizar: digo cómo es algo o cómo se llama?", "digo cómo es", "Caracterizar es decir cómo es."),
        ex("¿Qué significa que una característica sea pertinente?", "que sirve y es verdadera", "Coincide con lo que observo."),
        ex("¿Puedo inventar palabras en lengua indígena para describir?", "No", "Eso lo enseña el educador tradicional."),
    ],
    task=T(
        "Dibuja la «ruka» (casa) de práctica: una casa con el techo alto y tres ventanas. Escribe una oración con «ruka» que diga cómo es, en castellano y con la palabra copiada de la ficha. Luego dibuja el «kuyen» (luna) llena y escribe otra oración con una característica verdadera. Usa estas palabras para caracterizar: grande, pequeña, alta, redonda, brillante. Termina con una pregunta para la educadora sobre qué otras palabras se usan para describir.",
        "Vi una «ruka», la casa, alta y con tres ventanas. Vi «kuyen», la luna, redonda y brillante. Pregunta: ¿cómo se describe una casa en su lengua?",
        ["dibuja y escribe una oración por cada dibujo", "usa una característica verdadera", "copia bien las palabras de la ficha", "hace una pregunta a la educadora"],
        ["dos dibujos y dos oraciones", "pregunta escrita o dicha en voz alta"],
        ["elegir una característica que no coincide con el dibujo", "inventar palabras"],
        "Valora que caracterizó con lo que dibujó; si la característica no coincide, pídele que mire de nuevo su dibujo.",
    ),
    reinforce="Mira un objeto de tu casa y di dos características verdaderas.",
    extend="Escribe una oración sobre «antü» (sol) con una característica pertinente, y explica por qué es verdadera.",
)

L(
    LF4, 3,
    materials="Lápiz y hoja. El modelo de oración y el banco de palabras están escritos aquí. Todo es inventado y en castellano con palabras de la ficha.",
    use="Aprenderé a construir mi propia oración siguiendo un modelo. Sirve para escribir con orden usando palabras de la ficha, sin inventar.",
    prior=["Sé copiar una palabra de la ficha.", "Sé caracterizar con una palabra verdadera."],
    explain=[
        "Un modelo es una oración con espacios para completar. Mi modelo es: «Vi «palabra», su significado, y era característica». Por ejemplo: «Vi «antü», el sol, y era brillante».",
        "Para construir mi oración sigo cuatro pasos. Uno: elijo una palabra de la ficha. Dos: escribo su significado. Tres: observo y elijo una característica verdadera. Cuatro: leo mi oración y compruebo que tiene sentido.",
        "Mi oración no cambia la palabra de la ficha ni inventa partes en la lengua indígena. Una oración también puede comenzar con una expresión de la ficha de expresiones, como el saludo «mari mari», copiada igual. Si quiero decir algo que el modelo no permite, lo pregunto al educador o a la educadora tradicional. La lengua tiene su propia manera de armar oraciones y yo la aprendo de ellos.",
    ],
    vocab=[("construir", "armar algo poco a poco"), ("banco de palabras", "lista de palabras que puedo usar"), ("espacio", "lugar en blanco que debo completar"), ("sentido", "que la oración se entiende y es verdadera"), ("paso", "una parte ordenada de una tarea")],
    worked=[
        W("Completar el modelo", "Modelo: «Vi «____», ____, y era ____». " + FICHA_PAL + " Banco: brillante, tranquila. Quiero hablar del sol. ¿Cómo completo?", ["Elijo la palabra: «antü».", "Escribo su significado: el sol.", "Elijo una característica verdadera: brillante."], "Vi «antü», el sol, y era brillante."),
        W("Revisar el sentido", "La oración «Vi «antü», el sol, y era tranquila» ¿tiene sentido? Veo el sol brillando.", ["Miro lo que observé: el sol brillaba.", "«Tranquila» no describe bien lo que vi.", "Cambio por «brillante»."], "Mejor «brillante»"),
    ],
    mistakes=[
        M("Elegir una palabra del banco que no coincide con el significado.", "La oración queda sin sentido.", "Reviso el significado en la ficha."),
        M("Cambiar la forma de la palabra de la ficha para que suene mejor.", "Cambio la grafía.", "La copio igual a la ficha."),
    ],
    R=[
        ex(FICHA_PAL + " Modelo: «Vi «____», la luna, y era redonda». ¿Qué palabra de la ficha va en el espacio?", "kuyen", "La ficha dice que «kuyen» es luna."),
        ex("Los pasos para construir son: elegir palabra, escribir significado, elegir característica y: A) comprobar el sentido B) borrar todo.", "A", "El último paso es comprobar."),
        ex("Un lugar en blanco que debo completar se llama: A) espacio B) título.", "A", "Es el espacio del modelo."),
    ],
    C=[
        ex(FICHA_PAL + " Modelo: «Vi «____», el sol, y era brillante». ¿Qué palabra de la ficha va en el espacio?", "antü", "La ficha dice que «antü» es sol."),
        ex("Verdadero o falso: puedo cambiar las letras de la palabra de la ficha para que se vea mejor.", "Falso", "Se copia igual."),
        ex(FICHA_PAL + " Modelo: «Entré a la «____», la casa, y era pequeña». ¿Qué palabra va en el espacio?", "ruka", "La ficha dice que «ruka» es casa."),
    ],
    A=[
        ex(FICHA_PAL + " Modelo: «Tomé «____», agua, y estaba fresca». Completa con la palabra de la ficha para agua.", "ko", "La ficha dice que «ko» es agua."),
        ex("Ordena las palabras para armar la oración: era / Vi / «kuyen», / redonda. / la luna, / y. Escribe la oración.", "Vi «kuyen», la luna, y era redonda.", "Sigue el modelo: Vi, palabra, significado, y era, característica."),
        ex(FICHA_EXP + " Modelo: «____. Vi «antü», el sol, y era brillante.» ¿Qué expresión de la ficha va al comienzo para saludar?", "mari mari", "La ficha dice que «mari mari» es un saludo en mapuzugun."),
    ],
    Z=[
        ex("Rosa completó: «Vi «ruka», el sol, y era brillante». ¿Qué error tiene?", "«ruka» no significa sol", "La ficha dice que «ruka» es casa."),
        ex("Pedro dice: «Voy a inventar una parte nueva en la lengua indígena para mi oración». ¿Qué conviene: preguntar al educador tradicional o seguir inventando?", "preguntar al educador tradicional", "Esa parte la enseña quien conoce la lengua."),
    ],
    D=[
        ex(FICHA_PAL + " Construye la oración con el modelo para la tierra y la característica «mojada». Escribe la oración completa.", "Vi «mapu», la tierra, y estaba mojada.", "«Mapu» es tierra, y mojada es la característica."),
        arith("Construyes 3 oraciones con 7 palabras cada una. ¿Cuántas palabras escribiste en total?", "3 * 7", "Tres oraciones por siete palabras."),
    ],
    context=[ex(FICHA_PAL + " Quieres escribir en un cartel de tu sala una oración sobre el agua que bebes. Modelo: «Tomé «____», agua fresca». ¿Qué palabra de la ficha pones?", "ko", "La ficha dice que «ko» es agua.")],
    selfcheck=[
        ex("¿Cuántos pasos tiene la clase para construir una oración?", "4", "Son cuatro pasos."),
        ex("¿Qué hago al final: comprobar el sentido o borrar todo?", "comprobar el sentido", "Reviso que tenga sentido."),
        ex("¿Puedo inventar partes en la lengua indígena?", "No", "Eso lo enseña el educador tradicional."),
    ],
    task=T(
        "Usa el modelo «Vi «____», ____, y era ____». y la ficha de palabras. Construye dos oraciones diferentes, con dos palabras de la ficha a tu elección (por ejemplo antü, kuyen, ko, ruka, mapu o ñuke) y una característica verdadera para cada una. Escribe los cuatro pasos de tu trabajo (palabra, significado, característica, revisión) y una pregunta para la educadora tradicional.",
        "Vi «antü», el sol, y era brillante. Vi «kuyen», la luna, y era redonda. Pasos: palabra, significado, característica, revisión. Pregunta: ¿cómo se arma esta oración en su lengua?",
        ["construye dos oraciones con el modelo", "usa palabras de la ficha sin cambiarlas", "las características son verdaderas", "hace una pregunta a la educadora"],
        ["dos oraciones escritas", "pasos de trabajo"],
        ["inventar partes en la lengua indígena", "usar un significado distinto al de la ficha"],
        "Valora que siguió el modelo y revisó el sentido; si cambió una palabra de la ficha, pídele que la copie igual.",
    ),
    reinforce="Completa una vez más el modelo con otra palabra de la ficha y lee la oración en voz alta.",
    extend="Cambia la característica de una de tus oraciones y explica por qué la nueva también es verdadera.",
)

L(
    LF4, 4,
    materials="Lápiz, hoja y un lápiz de otro color para corregir. La ficha y las oraciones están escritas aquí.",
    use="Aprenderé a revisar una oración en tres cosas: significado, grafía y contexto. Sirve para mejorar mi escritura sin llamar «error» a una variante.",
    prior=["Sé construir una oración con un modelo.", "Sé que una palabra puede tener variantes."],
    explain=[
        "Revisar es mirar de nuevo mi oración para mejorarla. Reviso tres cosas. El significado: la palabra dice lo mismo que la ficha. La grafía: la copié igual, letra por letra. El contexto: la oración tiene sentido en la situación.",
        "Cuando encuentro un problema, uso un lápiz de otro color y escribo la corrección. Si dudo de una letra, miro la ficha. Si una palabra tiene dos escrituras en dos fuentes, no la tacho: anoto las dos y pregunto cuál usa la comunidad.",
        "Revisar es cuidar. En estos ejercicios la ficha es mi referencia: una letra cambiada por descuido es un error de copia, y una escritura distinta que viene de otra fuente es una variante, no un error. Si no estoy seguro de algo, lo pregunto al educador o a la educadora tradicional y espero su respuesta antes de decir que algo está mal.",
    ],
    vocab=[("revisar", "mirar de nuevo para mejorar"), ("significado", "lo que quiere decir una palabra"), ("grafía", "cómo se escribe una palabra"), ("contexto", "la situación en que se usa una oración"), ("variante", "otra forma válida de escribir lo mismo")],
    worked=[
        W("Revisar el significado", FICHA_PAL + " Oración: «Vi «ruka», el sol, y era brillante.» ¿Qué parte falla?", ["Reviso el significado de «ruka» en la ficha: casa.", "La oración dice que es el sol.", "Falla el significado."], "El significado: «ruka» es casa, no sol"),
        W("Revisar la grafía", FICHA_PAL + " Oración: «Tomé «ko», agua fresca.» y otra: «Tomé «kó», agua fresca.» ¿Cuál tiene la grafía como la ficha?", ["La ficha dice «ko».", "La primera usa «ko».", "La segunda cambió letras."], "La primera"),
    ],
    mistakes=[
        M("Corregir una palabra solo porque yo la escribí distinto.", "Puede ser una variante válida.", "Anoto las dos y pregunto."),
        M("Revisar solo la ortografía en castellano y no el significado.", "La palabra puede estar bien escrita y mal usada.", "Reviso significado, grafía y contexto."),
    ],
    R=[
        ex("Reviso tres cosas: significado, grafía y: A) contexto B) color.", "A", "La tercera es el contexto."),
        ex("La grafía es: A) cómo se escribe una palabra B) lo que quiere decir.", "A", "Grafía es la escritura."),
        ex("Para corregir uso un lápiz de: A) otro color B) el mismo y borro todo.", "A", "Así veo qué cambié."),
    ],
    C=[
        ex(FICHA_PAL + " Oración: «Vi «mapu», la luna, y era redonda.» ¿Qué falla: el significado, la grafía o el contexto?", "el significado", "«Mapu» es tierra, no luna."),
        ex(FICHA_PAL + " Oración: «Vi «kuien», la luna, y era redonda.» ¿Qué falla: el significado, la grafía o el contexto?", "la grafía", "La ficha escribe «kuyen»."),
        ex("Verdadero o falso: si dos fuentes escriben distinto una palabra, tacho una de las dos.", "Falso", "Anoto las dos y pregunto."),
    ],
    A=[
        ex(FICHA_PAL + " Oración: «Tomé «ko», agua fresca, en el recreo.» ¿Cumple con significado, grafía y contexto? Responde Sí o No.", "Sí", "«Ko» es agua y la oración tiene sentido."),
        arith("Una revisión tiene 3 partes: significado, grafía y contexto. Revisaste 2. ¿Cuántas te faltan?", "3 - 2", "Resto las revisadas de las tres."),
        ex(FICHA_PAL + " Oración: «Vi «antü», el sol, y era de noche.» El sol es del día. ¿Qué parte falla?", "el contexto", "Dice sol y de noche, que no tiene sentido."),
    ],
    Z=[
        ex("Camila dice: «Mi libro escribe «ruca», así que «ruka» está mal». ¿Tiene razón? Responde Sí o No.", "No", "Pueden ser variantes."),
        ex("Una oración está bien escrita pero la palabra tiene otro significado en la ficha. ¿Está correcta la oración? Responde Sí o No.", "No", "Revisar es significado, grafía y contexto."),
    ],
    D=[
        ex("Ordena el proceso de revisión: C) corrijo con otro color A) leo mi oración B) reviso significado, grafía y contexto. Escribe las letras.", "A, B, C", "Leo, reviso y recién después corrijo."),
        arith("Revisas 4 oraciones y encuentras 2 problemas en cada una. ¿Cuántos problemas encontraste?", "4 * 2", "Cuatro oraciones por dos problemas."),
    ],
    context=[ex(FICHA_PAL + " Tu compañero escribió en un cartel «Entré a la «ruka», la tierra». Quieres ayudarlo con respeto. ¿Qué le dices: «Mira la ficha: «ruka» es casa» o «Está horrible»?", "«Mira la ficha: «ruka» es casa»", "Señalo el dato de la ficha con respeto.")],
    selfcheck=[
        ex("¿Qué tres cosas reviso en una oración?", "significado, grafía y contexto", "Son los tres criterios de revisión."),
        ex("¿Una variante es un error?", "No", "Puede ser una forma válida."),
        ex("¿Qué hago si no estoy seguro de algo?", "pregunto al educador tradicional", "Espero su respuesta antes de decir que está mal."),
    ],
    task=T(
        "Revisa estas tres oraciones inventadas con la ficha de palabras: 1) «Vi «kuien», la luna, y era redonda.» 2) «Tomé «ko», agua fresca, en el recreo.» 3) «Entré a la «ruka», la tierra, y saludé.» Para cada una escribe si está bien o qué falla (significado, grafía o contexto) y cómo la corregirías con otro color. Termina con una pregunta para la educadora tradicional sobre una palabra que tenga más de una escritura.",
        "1) Falla la grafía: debe decir «kuyen». 2) Está bien. 3) Falla el significado: «ruka» es casa, no tierra. Pregunta: ¿qué forma de «ruka» usan en su comunidad?",
        ["revisa las tres oraciones", "nombra qué falla en cada una", "propone una corrección", "hace una pregunta a la educadora"],
        ["revisión escrita", "pregunta escrita o dicha en voz alta"],
        ["tachar una variante", "no revisar el significado"],
        "Valora que revisó con la ficha; si tachó una variante, invítalo a anotar ambas y preguntar.",
    ),
    reinforce="Elige una oración tuya de la clase anterior y revisa en voz alta: significado, grafía y contexto.",
    extend="Inventa una oración con un error de grafía para que otra persona lo encuentre con la ficha.",
)

# =================================================================== LF05 · recursos tecnológicos y creación en lengua indígena
L(
    LF5, 1,
    materials="Lápiz y hoja. Los planes y las situaciones están escritos aquí y son inventados. No se necesita ningún aparato: la clase se trabaja en papel. Cualquier uso de aparatos es con un adulto presente.",
    use="Aprenderé a definir qué quiero decir, para quién lo digo y qué debo cuidar antes de usar un recurso tecnológico. Sirve para crear con respeto, sin exponer a nadie.",
    prior=["Sé que la voz, la imagen y los saberes de las personas se cuidan.", "Sé que debo pedir permiso antes de grabar o copiar."],
    explain=[
        "Un recurso tecnológico es una herramienta para crear o comunicar. Puede ser una grabadora de voz, una cámara, un computador o una tableta. Antes de usarlo, planifico con tres preguntas.",
        "Primera: ¿cuál es mi mensaje? El mensaje es la idea, el hecho o el sentimiento que quiero comunicar, por ejemplo: «Gracias, educadora». Segunda: ¿para quién es? Esa es mi audiencia, como mi curso o mi familia. Tercera: ¿qué debo resguardar? Resguardar es cuidar lo que no puedo mostrar sin permiso.",
        "Debo resguardar la voz y la imagen de otras personas, los datos personales y los saberes que cuida la comunidad. Tampoco subo nada a internet. Todo lo que hago queda en mi casa o en mi curso, con un adulto, hasta que la persona responsable y la comunidad digan otra cosa.",
    ],
    vocab=[("recurso tecnológico", "herramienta para crear o comunicar, como una grabadora"), ("mensaje", "idea, hecho o sentimiento que quiero comunicar"), ("audiencia", "las personas para quienes hago mi creación"), ("resguardar", "cuidar lo que no puedo mostrar sin permiso"), ("publicar", "poner algo a la vista de muchas personas")],
    worked=[
        W("Armar el plan", "Rosa quiere agradecer a la educadora. Mensaje: «Gracias, educadora». Audiencia: su curso. ¿Qué otra pregunta le falta responder antes de usar un recurso?", ["Ya respondió el mensaje.", "Ya respondió la audiencia.", "Falta: qué debe resguardar."], "Qué debe resguardar"),
        W("Detectar lo que se resguarda", "Rosa piensa grabar la voz de la educadora sin avisar. ¿Qué debe resguardar?", ["La voz de otra persona se cuida.", "Primero necesita permiso.", "Debe pedirlo antes de grabar."], "La voz de la educadora; pedir permiso"),
    ],
    mistakes=[
        M("Grabar o fotografiar a alguien sin avisar.", "Su voz y su imagen se cuidan.", "Pido permiso antes."),
        M("Subir mi creación a internet apenas la termino.", "Aún no sé quién la verá ni si hay permisos.", "Se queda en casa o en el curso, con un adulto."),
    ],
    R=[
        ex("El mensaje es: A) la idea que quiero comunicar B) el color de la hoja.", "A", "Mensaje es lo que quiero decir."),
        ex("La audiencia son: A) las personas para quienes hago algo B) los lápices.", "A", "Audiencia es el público."),
        ex("Antes de grabar la voz de alguien, ¿pido permiso o grabo sin avisar?", "pido permiso", "Su voz se cuida."),
    ],
    C=[
        ex("Verdadero o falso: al terminar mi creación debo subirla de inmediato a internet.", "Falso", "Se queda en casa o en el curso, con un adulto."),
        ex("Plan: mensaje «Gracias, educadora»; audiencia: mi curso. ¿Cuál es la audiencia?", "mi curso", "Es para quién está hecho el mensaje."),
        ex("¿Qué es resguardar: A) cuidar lo que no puedo mostrar sin permiso B) mostrarlo todo?", "A", "Resguardar es cuidar."),
    ],
    A=[
        arith("Un plan tiene 3 preguntas: mensaje, audiencia y resguardo. Rosa respondió 2. ¿Cuántas le faltan?", "3 - 2", "Resto las respondidas."),
        ex("Elige qué debe resguardar Pedro si quiere filmar el patio: A) la imagen de los niños que aparecen B) el color del cielo.", "A", "Las imágenes de las personas se cuidan."),
        ex("Une cada pregunta con su respuesta. 1) ¿Cuál es mi mensaje? 2) ¿Para quién es? Respuestas: A) mi curso B) «Gracias». Escribe las letras en orden.", "B, A", "El mensaje es «Gracias» y la audiencia es mi curso."),
    ],
    Z=[
        ex("Luis dice: «Si es para mi curso, no necesito pedir permiso a nadie». ¿Tiene razón? Responde Sí o No.", "No", "Debo pedir permiso a las personas que aparecen o hablan."),
        ex("Ana quiere usar un saber que cuida la comunidad en su video. ¿Qué es mejor: preguntar al educador tradicional o usarlo sin preguntar?", "preguntar al educador tradicional", "Los saberes de la comunidad se cuidan."),
    ],
    D=[
        ex("Ordena el plan: C) pienso qué resguardar A) decido mi mensaje B) decido mi audiencia. Escribe las letras del orden de la clase.", "A, B, C", "Mensaje, audiencia y resguardo."),
        ex("Dos planes: 1) mensaje claro, audiencia clara, resguardo claro. 2) solo mensaje. ¿Cuál puede seguir adelante?", "1", "Tiene las tres respuestas."),
    ],
    context=[ex("Quieres grabar un mensaje de agradecimiento para tu curso con la voz de un compañero. Él no sabe todavía. ¿Qué haces primero: le pido permiso o lo grabo de sorpresa?", "le pido permiso", "Su voz se cuida.")],
    selfcheck=[
        ex("¿Cuáles son las tres preguntas del plan?", "mensaje, audiencia y resguardo", "Son las tres preguntas de la clase."),
        ex("¿Dónde queda lo que creo con aparatos hasta que haya permiso?", "en mi casa o en mi curso, con un adulto", "No se sube a internet."),
        ex("¿Puedo grabar la voz de otra persona sin avisar?", "No", "Debo pedir permiso."),
    ],
    task=T(
        "Haz en tu cuaderno un plan de tres preguntas para un mensaje de agradecimiento. Mensaje: puedes usar «Gracias, educadora» o «chaltumay» (gracias en mapuzugun). Audiencia: tu curso o tu casa. Resguardo: escribe dos cosas que cuidarás (por ejemplo, la voz de otras personas y tus datos personales). Todo lo haces en papel; no usas internet. Termina con una pregunta para la educadora tradicional sobre qué se puede grabar y qué no.",
        "Mensaje: «Gracias, educadora». Audiencia: mi curso. Resguardo: no grabaré voces sin permiso; no pondré mi dirección. Pregunta: ¿qué cosas de la comunidad no se pueden grabar?",
        ["escribe mensaje, audiencia y dos cosas que resguarda", "no usa internet", "hace una pregunta a la educadora"],
        ["plan escrito en el cuaderno", "pregunta escrita o dicha en voz alta"],
        ["dejar el resguardo en blanco", "proponer subir algo a internet sin permiso"],
        "Valora que pensó en el cuidado de otras personas; si propuso publicar, ayúdalo a mantenerlo en casa o en el curso.",
    ),
    reinforce="Di en voz alta tu mensaje, tu audiencia y una cosa que resguardarás.",
    extend="Haz el mismo plan para un segundo mensaje distinto y compara qué resguardas en cada uno.",
)

L(
    LF5, 2,
    materials="Lápiz y hoja. La tabla de recursos y las situaciones están escritas aquí. No se necesita ningún aparato.",
    use="Aprenderé a elegir el recurso adecuado para mi mensaje y a pedir permiso. Sirve para crear de forma segura y respetuosa.",
    prior=["Sé hacer un plan con mensaje, audiencia y resguardo.", "Sé que debo pedir permiso para usar la voz o la imagen de otros."],
    explain=[
        "Elegir un recurso es decidir qué herramienta sirve mejor para mi mensaje. Si quiero que se oiga mi voz, uso audio. Si quiero mostrar un dibujo en movimiento, uso video. Si quiero dejar una frase escrita, uso un texto. Un mismo mensaje puede hacerse de varias maneras.",
        "Cada recurso pide permisos. El audio necesita permiso de las personas cuya voz aparece. El video y la foto necesitan permiso de quienes se ven. El texto y las imágenes de otros necesitan permiso de su autor. Mi propio dibujo y mi propia voz los puedo usar, si decido hacerlo.",
        "También elijo un recurso al que todos puedan acceder. Si en mi casa no hay aparatos, puedo usar papel, lápiz y mi voz con un adulto. Un recurso más simple no es peor: lo importante es que mi mensaje se entienda y se cuide a las personas.",
    ],
    vocab=[("audio", "registro de sonido o voz"), ("video", "imágenes en movimiento con o sin sonido"), ("texto", "palabras escritas"), ("permiso", "aviso de que sí puedo usar algo"), ("acceso", "posibilidad de usar o recibir algo")],
    worked=[
        W("Elegir según el mensaje", "Rosa quiere que su curso escuche un saludo con su propia voz: «Mari mari». ¿Qué recurso le sirve: audio, video o texto?", ["Quiere que se oiga su voz.", "El audio registra voz.", "Es su propia voz, así que no necesita permiso de otras personas."], "audio"),
        W("Elegir el permiso", "Pedro quiere hacer un video de sus compañeros jugando. ¿De quién necesita permiso?", ["En el video se ve a sus compañeros.", "Su imagen se cuida.", "Debe pedir permiso a cada uno y a un adulto."], "De cada compañero que aparece y de un adulto"),
    ],
    mistakes=[
        M("Usar la foto de otra persona sin preguntar.", "Su imagen se cuida.", "Pido permiso antes de usarla."),
        M("Pensar que solo vale un recurso con aparatos.", "No todas las personas tienen acceso a ellos.", "Puedo usar papel, lápiz y mi voz con un adulto."),
    ],
    R=[
        ex("Si quiero que se escuche mi voz, uso: A) audio B) un dibujo mudo.", "A", "El audio registra la voz."),
        ex("Palabras escritas son un: A) texto B) audio.", "A", "El texto se escribe."),
        ex("Para usar la voz de otra persona, ¿pido permiso o no hace falta?", "pido permiso", "Su voz se cuida."),
    ],
    C=[
        ex("Verdadero o falso: un mensaje solo se puede hacer con un recurso con aparatos.", "Falso", "También puede hacerse con papel, lápiz y mi voz."),
        ex("Quiero mostrar un dibujo mío con una frase. ¿Qué recurso me sirve: texto con imagen o solo un audio?", "texto con imagen", "El dibujo y la frase se ven."),
        ex("Quiero usar el dibujo de una compañera. ¿De quién necesito permiso?", "de mi compañera", "Ella es la autora."),
    ],
    A=[
        ex("Tabla: audio = voz, video = imagen y voz, texto = palabras escritas. Mensaje: dejar escrita la palabra «chaltumay» en un cartel. ¿Qué recurso eliges?", "texto", "Es una palabra escrita."),
        arith("Tienes 3 recursos posibles (audio, video, texto) para cada uno de 2 mensajes. ¿Cuántas combinaciones hay?", "3 * 2", "Tres recursos por dos mensajes."),
        ex("En tu casa no hay aparatos. ¿Qué es mejor: dejar de crear o usar papel, lápiz y tu voz con un adulto?", "usar papel, lápiz y tu voz con un adulto", "Un recurso simple también sirve."),
    ],
    Z=[
        ex("Tomás dice: «Si el video es corto, no necesito permiso de nadie». ¿Tiene razón? Responde Sí o No.", "No", "El permiso no depende de cuánto dure."),
        ex("Una niña quiere filmar la ceremonia de una comunidad. ¿Qué debe hacer primero: preguntar a la comunidad y al educador tradicional o filmar de lejos?", "preguntar a la comunidad y al educador tradicional", "Esas prácticas las cuida la comunidad."),
    ],
    D=[
        ex("Ordena para usar un recurso: C) lo uso con un adulto A) elijo el recurso B) pido los permisos. Escribe las letras.", "A, B, C", "Elijo, pido permiso y luego uso."),
        arith("Para un trabajo pides permiso a 4 compañeros y a 2 adultos. ¿A cuántas personas pides permiso?", "4 + 2", "Sumo compañeros y adultos."),
    ],
    context=[ex("Quieres incluir la foto de tu profesora en un cartel. ¿Qué haces: le pregunto si puedo o la pongo sin avisar?", "le pregunto si puedo", "Su imagen se cuida.")],
    selfcheck=[
        ex("¿Qué recurso uso para una frase escrita?", "texto", "El texto es palabras escritas."),
        ex("¿A quién pido permiso para usar su dibujo?", "a su autor o autora", "Es quien lo creó."),
        ex("¿Es peor un recurso simple como papel y lápiz?", "No", "Lo importante es el mensaje y el cuidado."),
    ],
    task=T(
        "Completa esta tabla en tu cuaderno con tres mensajes: 1) un saludo con «mari mari»; 2) un cartel con la palabra «ko» y el dibujo de gotas; 3) un agradecimiento con «chaltumay». Para cada uno escribe qué recurso usarías (audio, video o texto), qué permiso necesitarías y si lo puedes hacer sin aparatos. Termina con una pregunta para la educadora tradicional sobre qué palabras puedes usar en un recurso.",
        "1) Audio, mi propia voz; sin aparatos puedo decirlo en voz alta. 2) Texto con dibujo; permiso: ninguno, es mío. 3) Texto; permiso: ninguno. Pregunta: ¿qué palabras puedo usar en un cartel?",
        ["elige un recurso para cada mensaje", "nombra el permiso necesario", "indica si puede hacerlo sin aparatos", "hace una pregunta a la educadora"],
        ["tabla de tres filas", "pregunta escrita o dicha en voz alta"],
        ["no pedir permiso para la voz de otros", "pensar que se necesitan aparatos siempre"],
        "Valora que cuidó permisos y acceso; si olvidó un permiso, pídele que lo agregue.",
    ),
    reinforce="Di en voz alta qué recurso usarías para dejar escrita una palabra y cuál para que se oiga tu voz.",
    extend="Explica a otra persona por qué un recurso simple puede ser tan bueno como uno con aparatos.",
)

L(
    LF5, 3,
    materials="Lápiz, hoja y colores. El guion de práctica está escrito aquí. Si hay un adulto y un aparato disponible, solo se graba tu propia voz, solo para tu casa o tu curso. Nada se sube a internet.",
    use="Aprenderé a crear un registro breve: un guion de audio o un cartel escrito con palabras de la ficha. Sirve para expresar un mensaje y practicar con cuidado.",
    prior=["Sé armar un plan con mensaje, audiencia y resguardo.", "Sé elegir un recurso con permiso."],
    explain=[
        "Un registro breve es una creación corta, de menos de un minuto o de unas pocas líneas. Puede ser un audio con mi voz, un cartel o una tarjeta. Antes de usar un aparato, hago un guion en papel. El guion es el texto de lo que voy a decir o escribir.",
        "Mi guion tiene tres partes: saludo, mensaje y cierre. Por ejemplo: saludo con «mari mari»; mensaje en castellano: «Hoy aprendí que ko es agua»; cierre con «chaltumay». Uso solo palabras de la ficha y las copio igual. Cuento cuántos segundos dura cuando lo leo en voz alta.",
        "Ensayo el guion antes de registrarlo. Si grabo, lo hago solo con mi voz, con un adulto presente, y guardo el archivo con un nombre sin datos personales, como «saludo_curso». No lo publico. Lo muestro en mi curso o en mi casa, si decido hacerlo.",
    ],
    vocab=[("registro", "creación guardada que puedo mostrar después"), ("guion", "texto de lo que voy a decir o escribir"), ("segundo", "unidad de tiempo; 60 segundos son un minuto"), ("archivo", "documento o grabación guardada en un aparato"), ("ensayar", "practicar antes de mostrar")],
    worked=[
        W("Armar el guion", "Guion de práctica (inventado): saludo con «mari mari»; mensaje: «Hoy aprendí que ko es agua»; cierre con «chaltumay». ¿Cuántas partes tiene el guion?", ["Cuento: saludo, mensaje y cierre.", "Son tres partes.", "Compruebo el orden."], "3 partes"),
        W("Calcular el tiempo", "Leíste el saludo en 4 segundos, el mensaje en 8 segundos y el cierre en 3 segundos. ¿Cuántos segundos dura todo?", ["Sumo 4 + 8 + 3.", "4 + 8 = 12.", "12 + 3 = 15."], "15 segundos"),
    ],
    mistakes=[
        M("Grabar sin ensayar el guion.", "Me trabo y tengo que repetir muchas veces.", "Lo ensayo en voz alta antes de registrarlo."),
        M("Poner mi nombre completo y mi dirección en el nombre del archivo.", "Son datos personales.", "Uso un nombre simple como «saludo_curso»."),
    ],
    R=[
        ex("Un guion tiene saludo, mensaje y: A) cierre B) dirección.", "A", "La tercera parte es el cierre."),
        ex("El texto de lo que voy a decir se llama: A) guion B) archivo.", "A", "Guion es el texto del registro."),
        ex("Un archivo con mi grabación, ¿lo nombro con mi dirección o con un nombre simple?", "con un nombre simple", "Evito datos personales."),
    ],
    C=[
        ex("Verdadero o falso: puedo publicar mi grabación apenas la termino.", "Falso", "Se queda en casa o en el curso."),
        ex("Guion: saludo «mari mari», mensaje «Hoy aprendí que ko es agua», cierre «chaltumay». ¿Cuál es el cierre?", "chaltumay", "Es la última parte."),
        ex("Si grabo, ¿la voz de quién uso: la mía o la de otra persona sin avisar?", "la mía", "Solo grabo mi propia voz."),
    ],
    A=[
        arith("El saludo dura 3 segundos, el mensaje 10 segundos y el cierre 3 segundos. ¿Cuántos segundos dura el registro?", "3 + 10 + 3", "Sumo las tres partes."),
        ex("Elige el mejor nombre de archivo: A) saludo_curso B) Luisa_Pérez_calle_Los_Pinos_12.", "A", "A no lleva datos personales."),
        arith("Un minuto tiene 60 segundos. Tu registro dura 25 segundos. ¿Cuántos segundos le faltan para completar un minuto?", "60 - 25", "Resto lo que dura de 60."),
    ],
    Z=[
        ex("Pedro dice: «Mi nombre y mi dirección deben ir en el archivo para que lo encuentren». ¿Tiene razón? Responde Sí o No.", "No", "Son datos personales que no se ponen."),
        ex("Una niña graba la voz de su compañero «de sorpresa». ¿Qué debe hacer ahora: borrar la grabación y pedir permiso o publicarla?", "borrar la grabación y pedir permiso", "Su voz se cuida."),
    ],
    D=[
        ex("Ordena: C) lo muestro en mi curso A) escribo el guion B) lo ensayo en voz alta. Escribe las letras.", "A, B, C", "Escribo, ensayo y muestro."),
        arith("Ensayas el guion 4 veces y cada ensayo dura 15 segundos. ¿Cuántos segundos ensayaste?", "4 * 15", "Cuatro ensayos por quince segundos."),
    ],
    context=[ex("Tu familia te presta un aparato para grabar tu saludo. ¿Qué haces: grabo mi propia voz y guardo el archivo en la casa o grabo a mi vecino sin avisar?", "grabo mi propia voz y guardo el archivo en la casa", "Cuido a las otras personas y mis datos.")],
    selfcheck=[
        ex("¿Cuáles son las tres partes del guion?", "saludo, mensaje y cierre", "Son las tres partes."),
        ex("¿Dónde muestro mi registro?", "en mi curso o en mi casa", "No lo subo a internet."),
        ex("¿Qué nombre pongo al archivo: simple o con mis datos?", "simple", "Cuido mis datos personales."),
    ],
    task=T(
        "Escribe un guion de tres partes para un registro de menos de un minuto. Saludo: «mari mari». Mensaje: una frase en castellano que diga una idea sobre el agua, el sol o la luna, usando «ko», «antü» o «kuyen» con su significado. Cierre: «chaltumay». Lee el guion en voz alta, cuenta cuántos segundos dura con la ayuda de un adulto y escribe el tiempo. Si hay un aparato y un adulto, puedes grabar tu propia voz; si no, solo lo ensayas. Elige un nombre de archivo sin datos personales.",
        "Saludo: «Mari mari». Mensaje: «Vi «kuyen», la luna, y era redonda». Cierre: «Chaltumay». Duración: 14 segundos. Nombre del archivo: saludo_curso.",
        ["escribe las tres partes del guion", "copia bien las palabras de la ficha", "dice cuántos segundos dura", "elige un nombre sin datos personales"],
        ["guion escrito", "lectura en voz alta o grabación de su propia voz en casa"],
        ["grabar la voz de otras personas sin permiso", "poner datos personales en el nombre"],
        "Valora el cuidado de los datos y la exactitud de las palabras; si grabó a otros sin permiso, pídele que lo borre y pida permiso.",
    ),
    reinforce="Lee tu guion en voz alta y cuenta con un adulto cuántos segundos dura.",
    extend="Cambia el mensaje de tu guion por otro tema y calcula cuántos segundos duraría ahora.",
)

L(
    LF5, 4,
    materials="Lápiz, hoja y el guion o cartel de la clase anterior. La lista de revisión está escrita aquí.",
    use="Aprenderé a revisar mi creación en tres cosas: la lengua, la autoría y el acceso. Sirve para cuidar lo que comparto antes de mostrarlo.",
    prior=["Sé crear un registro breve con un guion.", "Sé que debo pedir permiso y cuidar los datos."],
    explain=[
        "Antes de mostrar mi creación, la reviso con tres preguntas. Lengua: ¿las palabras en lengua indígena están copiadas igual que la ficha y tienen sentido? Autoría: ¿está claro quién hizo cada parte y de dónde vienen las palabras? Acceso: ¿quién podrá verla o escucharla y puede entenderla?",
        "En autoría anoto quién hizo qué. Mi voz, mi dibujo y mis frases son míos. Las palabras vienen de la ficha de este cuaderno, y la educadora tradicional confirma cómo se usan de verdad. Si usé algo de otra persona, lo nombro y pido permiso. Si no sé de dónde viene algo, no lo uso.",
        "En acceso pienso en todos: ¿se entiende si no se oye bien?, ¿tiene el texto escrito?, ¿alguien que no oye puede entender? Una creación con texto y voz llega a más personas. Y mientras no haya permiso, la creación se muestra solo en casa o en el curso.",
    ],
    vocab=[("acceso", "que las personas puedan ver, oír y entender algo"), ("autoría", "quién hizo cada parte"), ("revisar", "mirar de nuevo para mejorar"), ("crédito", "decir quién hizo algo o de dónde viene"), ("lista de revisión", "preguntas que repaso antes de terminar")],
    worked=[
        W("Revisar la lengua", FICHA_PAL + " Mi cartel dice «Vi «kuien», la luna». ¿Qué corrijo en la parte de lengua?", ["Comparo con la ficha: es «kuyen».", "Mi cartel cambió una letra.", "Corrijo a «kuyen»."], "Corrijo «kuien» por «kuyen»"),
        W("Revisar el acceso", "Mi registro es solo un audio. Un compañero con dificultad para oír no lo puede entender. ¿Qué agrego?", ["Pienso en el acceso.", "Agrego el texto escrito de lo que digo.", "Así llega a más personas."], "El texto escrito de lo que digo"),
    ],
    mistakes=[
        M("Usar una frase que copié sin saber de quién era.", "No puedo reconocer a su autor ni pedir permiso.", "Uso solo lo que sé de dónde viene."),
        M("Pensar que todos pueden oír mi audio.", "Algunas personas necesitan texto.", "Agrego texto escrito o dibujo."),
    ],
    R=[
        ex("Las tres cosas que reviso son lengua, autoría y: A) acceso B) color.", "A", "La tercera es el acceso."),
        ex("La autoría dice: A) quién hizo cada parte B) cuántas hojas tiene.", "A", "Autoría es quién lo hizo."),
        ex("Decir quién hizo algo o de dónde viene se llama: A) crédito B) cierre.", "A", "El crédito reconoce a la fuente."),
    ],
    C=[
        ex("Verdadero o falso: un audio sin texto lo entienden todas las personas.", "Falso", "Algunas personas necesitan texto."),
        ex(FICHA_PAL + " Mi cartel dice «Tomé «ko», agua fresca». ¿La parte de lengua está bien según la ficha?", "Sí", "«Ko» está copiada igual y es agua."),
        ex("Si no sé de dónde viene una frase, ¿la uso o no la uso?", "no la uso", "No puedo dar crédito ni pedir permiso."),
    ],
    A=[
        arith("La lista de revisión tiene 3 preguntas y ya contestaste 2. ¿Cuántas te faltan?", "3 - 2", "Resto las contestadas."),
        ex("Mi creación usa una imagen que dibujó mi compañera. ¿Qué anoto en autoría: «Dibujo de mi compañera, con su permiso» o nada?", "«Dibujo de mi compañera, con su permiso»", "Anoto quién lo hizo y que hay permiso."),
        ex("Quiero que mi mensaje llegue a más personas. ¿Qué agrego a mi audio: A) texto escrito B) más ruido?", "A", "El texto ayuda a quien no oye bien."),
    ],
    Z=[
        ex("Luis dice: «Como mi audio es corto, no necesito revisar la autoría». ¿Tiene razón? Responde Sí o No.", "No", "Siempre reviso lengua, autoría y acceso."),
        ex("Una niña quiere subir su registro a internet para que más gente lo vea. ¿Qué es mejor: preguntar a un adulto y a la comunidad antes o subirlo de inmediato?", "preguntar a un adulto y a la comunidad antes", "Mientras no haya permiso, se muestra solo en casa o en el curso."),
    ],
    D=[
        ex("Ordena para terminar: C) muestro mi creación en mi curso A) reviso lengua, autoría y acceso B) corrijo lo que encontré. Escribe las letras.", "A, B, C", "Reviso, corrijo y muestro."),
        arith("Revisas 3 creaciones y en cada una anotas 3 créditos. ¿Cuántos créditos anotas?", "3 * 3", "Tres creaciones por tres créditos."),
    ],
    context=[ex("Tu curso hará una muestra en la sala. Tu cartel dice «Tomé «ko»» pero no pusiste tu nombre ni de dónde vienen las palabras. ¿Qué agregas: crédito con mi nombre y «palabras de la ficha» o nada?", "crédito con mi nombre y «palabras de la ficha»", "Así se reconoce la autoría y la fuente.")],
    selfcheck=[
        ex("¿Qué tres cosas reviso antes de mostrar mi creación?", "lengua, autoría y acceso", "Son las tres de la lista."),
        ex("¿A quién pido permiso si uso su dibujo?", "a su autor o autora", "Es quien lo creó."),
        ex("¿Dónde muestro mi creación si no hay otros permisos?", "en mi casa o en mi curso", "No la subo a internet."),
    ],
    task=T(
        "Toma tu guion o cartel de la clase anterior, o usa este cartel de práctica: Vi «kuien», la luna, y era redonda. «Chaltumay». Haz la revisión en una tabla de tres filas. En lengua: compara con la ficha y escribe lo que corriges. En autoría: escribe quién hizo cada parte y de dónde vienen las palabras. En acceso: escribe qué agregarías para que más personas lo entiendan. Termina con una pregunta para la educadora tradicional sobre cómo cuidar las palabras de su lengua al publicarlas.",
        "Lengua: «kuien» debe ser «kuyen». Autoría: frase mía; palabras de la ficha. Acceso: agrego dibujo y texto grande. Pregunta: ¿qué palabras no se deben mostrar fuera de la comunidad?",
        ["revisa las tres partes", "corrige la lengua con la ficha", "anota autoría y fuente", "propone una mejora de acceso", "hace una pregunta a la educadora"],
        ["tabla de revisión", "pregunta escrita o dicha en voz alta"],
        ["no revisar la autoría", "pensar que ya está lista para publicar"],
        "Valora que revisó los tres criterios; si dejó pasar «kuien», pídele que compare con la ficha.",
    ),
    reinforce="Mira tu creación y di en voz alta una cosa que mejorarías en lengua, otra en autoría y otra en acceso.",
    extend="Escribe una lista de revisión propia de tres preguntas y úsala con otra creación de tu curso.",
)
