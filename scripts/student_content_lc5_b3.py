"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF05 (características de la lengua indígena y formación de palabras por aglutinación y reduplicación) y OA LF06
(recursos tecnológicos para registrar y narrar situaciones y prácticas, en lengua indígena).

Criterio de autoría: las comunidades, las personas, las fichas y los guiones son INVENTADOS y están en castellano; no
pertenecen a ningún pueblo. Para describir cómo se forman palabras se usa una «lengua de práctica» inventada, Rin
(distinta de Tolu, usada en LF04), cuyas reglas se escriben completas en cada ejercicio. No se afirma ninguna forma,
palabra ni rasgo gramatical de una lengua indígena real; solo se dice que en Chile hay varias lenguas indígenas, con el
mapuzugun y el rapa nui como ejemplos ya trabajados. En LF06 los recursos digitales se describen sin marcas ni enlaces,
siempre con una persona adulta y sin publicar en línea; nunca se registran ceremonias, lugares de respeto ni personas sin
permiso. La forma tradicional de decir, narrar y describir en lengua indígena la enseñan el educador/a tradicional y la
comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LF5, LF6 = "LC05 OA LF05", "LC05 OA LF06"

CONSULT = " Recuerda: lo tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Consúltales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No evaluar la identidad ni la fluidez de nadie."


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


MAT = "Lápiz y hojas. Las reglas, las fichas y los guiones están escritos en este cuaderno y son inventados para practicar; no son de ningún pueblo."

RIN = ("Reglas de la lengua de práctica Rin (inventada; no es de ningún pueblo): fen = árbol; sal = agua; mur = piedra; kol = camino. "
       "Piezas: wa- = nuestro (va al comienzo); -ik = pequeño (va justo después de la raíz); -an = lugar donde hay (va después de la raíz o de -ik); "
       "-ek = varios (va al final). Si se repite la raíz, significa «de juguete». Orden: wa- + raíz + -ik + -an + -ek.")

# ============================================================ OA LF05 · características y formación de palabras
L(
    LF5, 1,
    materials=MAT,
    use="Aprenderé a situar las características de una lengua indígena: qué rasgos se pueden describir, de dónde sale esa información y por qué no se generaliza a otras lenguas. Sirve para explicar una lengua con respeto y sin inventar.",
    prior=["Sé que aglutinar es pegar piezas y reduplicar es repetir.", "Sé que Tolu es una lengua inventada de práctica."],
    explain=[
        "Una lengua tiene características: los sonidos que usa, cómo arma las palabras, en qué orden pone las partes de una frase y qué significados dan sus piezas. Para describir una lengua indígena necesitamos una fuente confiable, como el educador tradicional, un libro escrito con hablantes o una ficha preparada con la comunidad. Sin fuente, no se describe.",
        "En Chile hay varias lenguas indígenas, como el mapuzugun y el rapa nui, y cada una tiene sus propias características. Lo que se dice de una no se dice de las otras. Por eso, antes de explicar una característica, situamos de qué lengua habla la ficha, quién la preparó y con qué permiso. También anotamos qué no sabemos.",
        "Para practicar la descripción usamos Rin, una lengua inventada, distinta de Tolu. Con ella aprendemos a nombrar sus características: qué raíces tiene, qué piezas se pegan y qué significa repetir una raíz. Describir una lengua no es juzgarla: es explicar cómo funciona. Con Rin no se afirma nada de ningún pueblo real.",
    ],
    vocab=[("característica", "rasgo que describe cómo es una lengua"), ("gramática", "conjunto de reglas de una lengua"), ("ficha de lengua", "texto que resume datos de una lengua y de su fuente"), ("fuente confiable", "persona o libro preparado con quienes hablan la lengua"), ("generalizar", "decir que algo vale para todas las lenguas")],
    worked=[
        W("Leer las reglas de una lengua", RIN + " ¿Qué dice la regla sobre repetir la raíz?", ["Busco «se repite la raíz».", "Dice que significa «de juguete»."], "Que significa «de juguete»."),
        W("No generalizar", "Una niña dice: «Como en Rin se pegan piezas, todas las lenguas indígenas se arman igual». ¿Qué corrige?", ["Rin es una lengua inventada.", "Cada lengua tiene sus reglas."], "Rin no representa a ninguna lengua real; cada lengua se describe con su fuente."),
    ],
    mistakes=[
        M("Describir una lengua sin fuente.", "Puedo afirmar algo falso.", "Uso al educador tradicional o una ficha preparada con la comunidad."),
        M("Decir que lo que vale para una lengua vale para todas.", "Cada lengua tiene sus reglas.", "Nombro la lengua de la que hablo."),
    ],
    R=[
        ex(RIN + " ¿Qué significa «sal» en Rin?", "Agua", "Lo dice la regla."),
        ex("Describir una lengua necesita: A) una fuente confiable B) solo mi imaginación", "A", "Sin fuente no se describe."),
        ex("¿Cuál es una lengua indígena de Chile que ya conocemos: el mapuzugun o Rin?", "El mapuzugun", "Rin es inventada."),
    ],
    C=[
        ex("Verdadero o falso: Rin es la lengua de un pueblo de Chile.", "Falso", "Rin es inventada para practicar."),
        ex("¿Qué es una característica de una lengua? A) un rasgo que la describe B) una opinión sobre ella", "A", "Describe cómo es la lengua."),
        ex("Verdadero o falso: lo que se dice de una lengua indígena vale para todas.", "Falso", "Cada una tiene sus reglas."),
    ],
    A=[
        ex(RIN + " ¿Qué significa «mur» en Rin?", "Piedra", "Lo dice la regla."),
        ex(RIN + " ¿Qué pieza va siempre al final de la palabra: «-ek» o «wa-»?", "-ek", "Según la regla, -ek va al final."),
        ex("Une cada dato con su fuente. 1) «ko» es agua 2) «fen» es árbol en Rin. a) ficha de palabras en mapuzugun b) reglas de Rin inventadas", "1-a, 2-b", "Cada dato viene de una fuente distinta."),
    ],
    Z=[
        ex("Tomás escribe: «En todas las lenguas indígenas, repetir una palabra significa “de juguete”», porque así pasa en Rin. ¿Qué error comete?", "Generaliza una regla de una lengua inventada", "Rin es inventada y no representa otras lenguas."),
        ex("Quieres explicar una característica del mapuzugun. ¿Qué haces primero? A) buscar una fuente confiable o preguntar al educador tradicional B) inventar un ejemplo", "A", "Hay que apoyarse en quien conoce la lengua."),
    ],
    D=[
        ex("Dos explicaciones. E1: «Según el educador tradicional, en nuestra lengua se hace así». E2: «Todo el mundo sabe que se hace así». ¿Cuál indica la fuente?", "E1", "E2 no dice quién lo sabe."),
        ex("Si no sabes una característica de la lengua de tu comunidad, ¿qué escribes? A) «No lo sé; lo consultaré» B) una característica inventada", "A", "Es honesto y respetuoso."),
    ],
    context=[ex("En una exposición, un compañero dice cómo se arman las palabras de una lengua indígena, pero no dice de dónde lo sabe. ¿Qué le preguntas? A) ¿cuál es tu fuente? B) ¿por qué hablas tan fuerte?", "A", "La fuente permite comprobar la información.")],
    selfcheck=[
        ex("Nombra dos características que se pueden describir de una lengua.", "Dos entre: sonidos, cómo arma palabras, orden de las partes, significado de las piezas", "Son rasgos de una lengua."),
        ex("Verdadero o falso: describir una lengua es lo mismo que juzgarla.", "Falso", "Describir es explicar cómo funciona."),
        ex(RIN + " ¿Qué significa «kol»?", "Camino", "Lo dice la regla."),
    ],
    task=T("Con las reglas de Rin: «" + RIN + "» completa una ficha de lengua con cuatro filas: «Lengua», «Qué sé de ella» (tres datos de las reglas), «De dónde viene lo que sé» y «Qué no sé». Luego escribe una frase que explique por qué lo que dice la ficha de Rin no vale para el mapuzugun ni para el rapa nui.",
           "Lengua: Rin (inventada). Qué sé: fen es árbol; la pieza -ik significa pequeño; repetir la raíz significa de juguete. Viene de: las reglas inventadas del cuaderno. No sé: cómo se pronuncia. Lo de Rin no vale para el mapuzugun ni el rapa nui porque Rin es inventada y cada lengua tiene sus propias reglas.",
           ["completa la ficha con datos de las reglas", "indica la fuente", "evita generalizar"], ["ficha de cuatro filas", "frase final"], ["inventar rasgos de una lengua real", "generalizar"],
           "Pedir que muestre en las reglas cada dato; valorar que escriba lo que no sabe."),
    reinforce="Copia las reglas de Rin y marca con un color las piezas que se pegan a la raíz.",
    extend="Escribe dos preguntas para el educador tradicional sobre cómo se arman las palabras en la lengua de tu comunidad.",
)

L(
    LF5, 2,
    materials=MAT,
    use="Aprenderé a analizar la construcción de palabras formadas por aglutinación y reduplicación: separar sus piezas, decir qué aporta cada una y describir el orden. Sirve para explicar cómo se arma una palabra.",
    prior=["Sé situar las características de una lengua con una ficha.", "Sé que cada pieza tiene un lugar fijo en Rin."],
    explain=[
        "Analizar una palabra es separarla en sus partes y explicar qué hace cada una. En Rin, «fen-ik-an» tiene la raíz «fen» (árbol), la pieza «-ik» (pequeño) y la pieza «-an» (lugar donde hay). Se lee: «lugar donde hay arbolitos». Cada pieza aporta un significado y ocupa un lugar fijo en la palabra.",
        "Para describir la construcción de una palabra seguimos tres pasos. Primero, separamos con guiones. Segundo, decimos qué significa cada parte. Tercero, explicamos el orden: primero va wa-, luego la raíz, después -ik, -an y por último -ek. Si una palabra no respeta el orden, no está bien formada en Rin.",
        "La reduplicación se analiza igual: se repite la raíz y se agrega su significado. En Rin, «fen-fen» es «un árbol de juguete». Si se combina con otras piezas, primero se repite la raíz y después se pegan las demás: «wa-fen-fen-ik» sería «nuestro arbolito de juguete». Estos análisis son solo de práctica y no describen ninguna lengua real.",
    ],
    vocab=[("analizar", "separar una palabra en partes y explicar cada una"), ("orden de las piezas", "lugar que ocupa cada pieza dentro de la palabra"), ("bien formada", "armada siguiendo las reglas de la lengua"), ("raíz", "parte principal de la palabra"), ("sufijo", "pieza que se pega después de la raíz")],
    worked=[
        W("Analizar una palabra", RIN + " Analiza «wa-sal-ik».", ["wa- = nuestro; sal = agua; -ik = pequeño.", "El orden es correcto."], "Nuestra agüita (nuestra agua pequeña)."),
        W("Revisar el orden", RIN + " ¿Está bien formada «sal-wa»?", ["wa- debe ir al comienzo.", "Aquí está después de la raíz."], "No: debería ser «wa-sal»."),
    ],
    mistakes=[
        M("Traducir sin separar las piezas.", "No se ve qué aporta cada una.", "Separo con guiones y traduzco pieza por pieza."),
        M("Cambiar el orden de las piezas.", "En Rin el orden es fijo.", "Reviso la regla del orden."),
    ],
    R=[
        ex(RIN + " ¿Qué significa «fen-an»?", "Lugar donde hay árboles", "fen es árbol y -an es lugar donde hay."),
        ex(RIN + " ¿Qué pieza significa «pequeño»?", "-ik", "Lo dice la regla."),
        ex(RIN + " ¿Qué significa «mur-mur»?", "Una piedra de juguete", "Repetir la raíz es de juguete."),
    ],
    C=[
        ex(RIN + " Verdadero o falso: «wa-fen» significa «nuestro árbol».", "Verdadero", "wa- es nuestro y fen árbol."),
        ex("Analizar una palabra es: A) separarla en partes y explicar cada una B) cambiarle el significado", "A", "Es el procedimiento de la clase."),
        ex(RIN + " ¿Qué lugar ocupa «wa-» en la palabra: al comienzo o al final?", "Al comienzo", "Lo dice la regla."),
    ],
    A=[
        ex(RIN + " Analiza «kol-an» y escribe qué significa.", "kol + an: lugar donde hay caminos", "kol es camino y -an es lugar donde hay."),
        ex(RIN + " Escribe «nuestro arbolito» en Rin.", "wa-fen-ik", "wa-, raíz y -ik en ese orden."),
        ex(RIN + " Escribe «piedra de juguete» en Rin.", "mur-mur", "Se repite la raíz."),
    ],
    Z=[
        ex(RIN + " Marta escribió «fen-an-ik» para «lugar donde hay arbolitos». ¿Qué error tiene?", "-ik debe ir antes de -an", "El orden es raíz, -ik y -an: fen-ik-an."),
        ex(RIN + " Ana dice que «sal-sal» significa «mucha agua». ¿Es correcto? Responde Sí o No.", "No", "Significa agua de juguete."),
    ],
    D=[
        ex(RIN + " Analiza «wa-kol-an-ek».", "nuestro + camino + lugar donde hay + varios: nuestros lugares donde hay caminos", "Cada pieza respeta su orden."),
        ex(RIN + " Escribe «nuestro arbolito de juguete» en Rin.", "wa-fen-fen-ik", "Se repite la raíz antes de pegar -ik."),
    ],
    context=[ex("En tu escuela alguien lee una palabra larga en lengua indígena y dice que significa una oración. ¿Qué propones? A) pedir al educador tradicional que muestre sus partes B) adivinar las partes", "A", "Solo quien conoce la lengua puede separarlas.")],
    selfcheck=[
        ex("Nombra los tres pasos para describir una palabra.", "Separar, decir qué significa cada parte y explicar el orden", "Son los pasos de la clase."),
        ex(RIN + " ¿Cuál es el orden de las piezas en Rin?", "wa-, raíz, -ik, -an, -ek", "Es el orden de la regla."),
        ex("Verdadero o falso: estos análisis describen una lengua indígena real.", "Falso", "Rin es inventada."),
    ],
    task=T("Con las reglas de Rin: «" + RIN + "» analiza estas cuatro palabras en una tabla de tres columnas (palabra separada, qué aporta cada parte, significado completo): wa-mur, fen-ik-an, kol-kol y wa-sal-ik-an. Escribe después una frase que explique el orden de las piezas.",
           "wa-mur: wa (nuestro) + mur (piedra): nuestra piedra. fen-ik-an: fen + ik + an: lugar donde hay arbolitos. kol-kol: camino de juguete. wa-sal-ik-an: nuestro lugar donde hay agüitas. Orden: wa-, raíz, -ik, -an, -ek.",
           ["separa cada palabra", "explica qué aporta cada parte", "enuncia el orden"], ["tabla de tres columnas", "frase del orden"], ["traducir sin separar", "cambiar el orden"],
           "Pedir que señale cada pieza en las reglas; valorar la frase del orden."),
    reinforce="Analiza en tu hoja «wa-fen» y «sal-an» con el procedimiento de tres pasos.",
    extend="Arma tres palabras de Rin que respeten el orden y analízalas.",
)

L(
    LF5, 3,
    materials=MAT,
    use="Aprenderé a describir el uso de palabras formadas por aglutinación y reduplicación en situaciones reales: para qué sirve cada tipo de palabra y qué relación tiene con el territorio. Sirve para explicar por qué una lengua arma así sus palabras.",
    prior=["Sé analizar palabras con piezas y con raíz repetida.", "Sé que Rin es inventada."],
    explain=[
        "Las palabras se usan para algo: nombrar lugares, decir cuántos hay, decir cómo es algo o hablar de lo que nos pertenece. Con piezas pegadas, una lengua puede decir mucho en una sola palabra. En Rin, «fen-an» nombra un lugar (donde hay árboles) y «wa-» dice que algo es de nosotros. Así se nombra el territorio y la pertenencia.",
        "En castellano también hay piezas que nombran lugares: «pinar» es un lugar con pinos, «naranjal» uno con naranjos y «arenal» uno con mucha arena. Son sufijos que se pegan a la raíz, igual que «-an» en Rin. Esto nos ayuda a entender la idea, pero cada lengua indígena real tiene sus propias formas, que enseña el educador tradicional.",
        "Describir el uso de una palabra es decir en qué situación la usaríamos. Por ejemplo, «wa-fen-an» sirve para decir «nuestra arboleda». No inventamos usos culturales: no decimos que una palabra se use en un rito o que tenga un valor sagrado si la fuente no lo dice. Para esas cosas, preguntamos a la comunidad.",
    ],
    vocab=[("uso de una palabra", "situación en que se emplea una palabra"), ("nombrar", "dar nombre a algo"), ("pertenencia", "decir de quién es algo"), ("sufijo de lugar", "pieza que dice «lugar donde hay…», como el -al de «naranjal»"), ("situación", "momento o contexto en que se habla")],
    worked=[
        W("Elegir la palabra para una situación", RIN + " Quieres decir «lugar donde hay piedras». ¿Qué palabra de Rin usas?", ["Piedra es mur.", "Lugar donde hay es -an."], "mur-an"),
        W("Comparar con el castellano", "En castellano, «pinar» es un lugar con pinos. ¿Qué pieza dice «lugar con» en pinar?", ["La raíz es pin(o).", "La pieza que se pega es -ar."], "La pieza -ar."),
    ],
    mistakes=[
        M("Decir que una palabra se usa en un rito sin que la fuente lo diga.", "Invento un uso cultural.", "Describo solo el uso que dice la fuente."),
        M("Creer que todas las lenguas nombran lugares con una pieza como -an.", "Es una regla de Rin.", "Hablo solo de la lengua que describo."),
    ],
    R=[
        ex(RIN + " ¿Qué pieza de Rin dice «de nosotros»?", "wa-", "Es la pieza para nuestro."),
        ex("En castellano, «naranjal» es un lugar con: A) naranjos B) pinos", "A", "El sufijo -al nombra el lugar."),
        ex(RIN + " ¿Qué palabra de Rin nombra «lugar donde hay agua»?", "sal-an", "sal es agua y -an es lugar donde hay."),
    ],
    C=[
        ex("Verdadero o falso: una palabra con piezas puede decir mucho en una sola palabra.", "Verdadero", "Por ejemplo, wa-fen-an."),
        ex("Verdadero o falso: puedo decir que una palabra indígena es sagrada si me parece importante.", "Falso", "Eso lo dice la comunidad."),
        ex("En castellano, ¿qué pieza se pega a «arena» para nombrar un lugar con mucha arena: -al o -ar?", "-al", "La palabra correcta es arenal."),
    ],
    A=[
        ex(RIN + " Escribe «nuestro lugar donde hay agua» en Rin.", "wa-sal-an", "wa-, raíz y -an en ese orden."),
        ex(RIN + " Escribe «lugares donde hay piedras» en Rin.", "mur-an-ek", "La raíz, -an y -ek al final."),
        ex("Une cada situación con la palabra de Rin. 1) decir «nuestro camino» 2) decir «camino de juguete». a) kol-kol b) wa-kol", "1-b, 2-a", "wa- dice nuestro y repetir la raíz dice de juguete."),
    ],
    Z=[
        ex("Luis dice: «En Rin se usa fen-fen en una ceremonia». ¿Qué error comete?", "Inventa un uso ceremonial", "Las reglas solo dicen que significa de juguete."),
        ex("Un compañero afirma que en el mapuzugun también se usa -an para lugares, porque así es en Rin. ¿Qué falla? A) usa una regla inventada B) está bien", "A", "Rin es inventada."),
    ],
    D=[
        ex(RIN + " Escribe «nuestras arboledas» en Rin respetando el orden.", "wa-fen-an-ek", "wa-, raíz, -an y -ek."),
        ex("Elige la frase que describe el uso sin inventar: A) «Con wa-fen-an se dice nuestra arboleda» B) «Con wa-fen-an se llama a los espíritus»", "A", "La B inventa un uso espiritual."),
    ],
    context=[ex("Quieres rotular un mapa de tu comunidad con palabras de la lengua indígena. ¿Qué haces? A) pido al educador tradicional los nombres y su escritura B) invento nombres con piezas que me suenan bien", "A", "Los nombres de lugares los enseña la comunidad.")],
    selfcheck=[
        ex("Escribe dos usos que puede tener una palabra con piezas.", "Nombrar un lugar y decir de quién es algo", "Son usos de la clase."),
        ex(RIN + " ¿Cómo se dice «nuestra piedra» en Rin?", "wa-mur", "wa- y la raíz."),
        ex("Verdadero o falso: puedo afirmar el uso cultural de una palabra sin fuente.", "Falso", "Se pregunta a la comunidad."),
    ],
    task=T("Con las reglas de Rin: «" + RIN + "» arma cinco palabras que nombren lugares o pertenencias de una comunidad imaginaria (por ejemplo, nuestra arboleda, un lugar donde hay agua, un camino). Para cada una escribe la palabra, su traducción y una situación en la que la usarías. Termina con una pregunta que le harías al educador tradicional sobre cómo se nombran los lugares en la lengua de tu comunidad.",
           "wa-fen-an: nuestra arboleda; para rotular un lugar del mapa. sal-an: lugar donde hay agua; para marcar una vertiente. kol: camino; para el sendero. wa-mur: nuestra piedra; para mostrarla. mur-an: lugar donde hay piedras. Pregunta: ¿cómo se nombran los lugares de nuestra comunidad en nuestra lengua?",
           ["respeta las reglas de Rin", "traduce y da una situación", "no inventa usos culturales"], ["cinco palabras con traducción y situación", "pregunta escrita"], ["inventar usos ceremoniales", "mezclar Rin con lenguas reales"],
           "Pedir que explique cada palabra con las reglas; valorar que no invente significados culturales."),
    reinforce="Escribe cinco lugares del castellano que se nombran con -ar o -al, como pinar o naranjal.",
    extend="Explica con tus palabras por qué nombrar un lugar con una pieza de la lengua muestra una relación con el territorio.",
)

L(
    LF5, 4,
    materials=MAT,
    use="Aprenderé a explicar por escrito las características de una lengua y la formación de sus palabras, atribuyendo cada dato a su fuente. Sirve para escribir explicaciones claras y respetuosas.",
    prior=["Sé analizar palabras de Rin y describir su uso.", "Sé que una respuesta atribuida nombra la fuente."],
    explain=[
        "Una explicación atribuida de una lengua tiene cuatro partes. Primero, la fuente: «Según las reglas de Rin…». Segundo, la característica: «las palabras se arman pegando piezas». Tercero, un ejemplo: «fen-ik-an significa lugar donde hay arbolitos». Cuarto, un límite: «esto vale para Rin y no para otras lenguas».",
        "Para que la explicación sea clara, usamos palabras precisas: raíz, pieza, aglutinar, reduplicar y orden. Evitamos palabras que juzgan, como «primitiva», «más avanzada» o «difícil». Y evitamos «todas las lenguas» o «los pueblos indígenas». Si hablamos de una lengua real, indicamos cuál y quién nos lo enseñó.",
        "Antes de entregar, revisamos con una lista: ¿nombré la fuente?, ¿di un ejemplo?, ¿declaré un límite?, ¿evité juzgar? Y, si la explicación es sobre una lengua real, la mostramos al educador tradicional para que la valide. Nosotros podemos aprender y explicar, pero no reemplazamos a quienes hablan la lengua.",
    ],
    vocab=[("explicación atribuida", "explicación que dice de dónde viene cada dato"), ("ejemplo", "caso concreto que muestra una idea"), ("límite", "aclaración de hasta dónde vale lo que digo"), ("juzgar", "decir que algo es bueno o malo, mejor o peor"), ("validar", "pedir que lo revise quien corresponde")],
    worked=[
        W("Armar la explicación", RIN + " Explica cómo se arman las palabras en Rin.", ["Fuente: las reglas de Rin.", "Característica: se pegan piezas a una raíz.", "Ejemplo: fen-ik-an. Límite: vale solo para Rin."], "Según las reglas de Rin, las palabras se arman pegando piezas a una raíz; por ejemplo, fen-ik-an es «lugar donde hay arbolitos». Esto vale solo para Rin."),
        W("Corregir una explicación", "Explicación: «Las lenguas indígenas son primitivas porque pegan piezas». ¿Qué corrige?", ["«Primitivas» juzga.", "«Las lenguas indígenas» generaliza."], "Quita el juicio y dice cuál lengua y cuál fuente."),
    ],
    mistakes=[
        M("Usar palabras que juzgan una lengua.", "Descalifican a sus hablantes.", "Describo cómo funciona."),
        M("Entregar una explicación de una lengua real sin que la valide el educador tradicional.", "Puede tener errores.", "Se la muestro antes de entregar."),
    ],
    R=[
        ex("Completa: «Según las reglas de ___, las palabras se arman pegando piezas».", "Rin", "Es la lengua de práctica de estas reglas."),
        ex("Un límite de la explicación dice: A) “esto vale solo para esta lengua” B) “todas las lenguas son así”", "A", "El límite cuida de no generalizar."),
        ex(RIN + " ¿Qué ejemplo muestra una pieza de lugar: «fen-an» o «fen-fen»?", "fen-an", "-an es lugar donde hay."),
    ],
    C=[
        ex("Verdadero o falso: «primitiva» es una palabra que juzga una lengua.", "Verdadero", "Descalifica a quienes la hablan."),
        ex("Las cuatro partes de la explicación atribuida son: fuente, característica, ejemplo y… A) límite B) chiste", "A", "El límite evita generalizar."),
        ex("Verdadero o falso: una explicación sobre una lengua real debe validarla el educador tradicional.", "Verdadero", "Ellos conocen la lengua."),
    ],
    A=[
        ex("Ordena para armar una explicación: a) Esto vale solo para Rin b) Según las reglas de Rin c) las palabras se arman con piezas d) por ejemplo, fen-ik-an. Escribe las letras.", "b, c, d, a", "Fuente, característica, ejemplo y límite."),
        ex(RIN + " Elige el ejemplo que muestra reduplicación: A) kol-kol B) kol-an", "A", "Repite la raíz."),
        ex(RIN + " Completa: «Según Rin, la pieza ___ significa pequeño».", "-ik", "Lo dice la regla."),
    ],
    Z=[
        ex("Tomás escribe: «Todas las lenguas indígenas arman las palabras igual que Rin». ¿Qué parte de la explicación falta?", "El límite", "No aclara que vale solo para Rin."),
        ex("Una niña escribe sobre el mapuzugun usando solo reglas de Rin. ¿Qué error comete? A) mezcla una lengua inventada con una real B) escribió muy corto", "A", "Rin no describe ninguna lengua real."),
    ],
    D=[
        ex("Elige la explicación mejor atribuida: A) «Según las reglas de Rin, repetir la raíz significa de juguete; vale solo para Rin» B) «Repetir una raíz siempre significa de juguete»", "A", "La A nombra la fuente y declara el límite."),
        ex("Si el educador tradicional corrige tu explicación de la lengua de tu comunidad, ¿qué haces? A) la corrijo y le agradezco B) la defiendo", "A", "La validación se acepta."),
    ],
    context=[ex("En una prueba te piden explicar cómo se arman las palabras en una lengua. ¿Qué haces? A) escribo fuente, característica, ejemplo y límite B) copio una definición sin fuente", "A", "Es la estructura de una explicación atribuida.")],
    selfcheck=[
        ex("Nombra las cuatro partes de una explicación atribuida de una lengua.", "Fuente, característica, ejemplo y límite", "Son las partes de la clase."),
        ex("Verdadero o falso: puedo escribir «las lenguas indígenas son más simples».", "Falso", "Jerarquiza y generaliza."),
        ex(RIN + " ¿Cómo se escribe «piedra de juguete»?", "mur-mur", "Se repite la raíz."),
    ],
    task=T("Escribe una explicación de cuatro frases sobre cómo se arman las palabras en Rin, usando sus reglas: «" + RIN + "». Debe tener la fuente, una característica (aglutinar o reduplicar), un ejemplo de Rin con su traducción y un límite. Luego revísala con esta lista: ¿nombré la fuente?, ¿di un ejemplo?, ¿declaré un límite?, ¿evité juzgar? Anota qué cambiarías si tuvieras que explicar la lengua de tu comunidad.",
           "Según las reglas de Rin, las palabras se arman pegando piezas a una raíz. Por ejemplo, wa-fen-an es «nuestra arboleda». También se puede repetir la raíz: kol-kol es «camino de juguete». Esto vale solo para Rin. Para la lengua de mi comunidad pediría ejemplos al educador tradicional.",
           ["incluye fuente, característica, ejemplo y límite", "evita juzgar", "indica cómo trabajaría con una lengua real"], ["explicación de cuatro frases", "lista revisada"], ["generalizar", "usar palabras que juzgan"],
           "Pedir que señale cada parte de la explicación; valorar el límite declarado."),
    reinforce="Reescribe esta frase sin juzgar: «Las lenguas que pegan piezas son difíciles».",
    extend="Escribe una explicación atribuida sobre una palabra de castellano que se arma pegando partes.",
)

# ============================================================ OA LF06 · registro tecnológico autorizado
GUION = ("Guion de registro de práctica (inventado): «Hola, me llamo Tomás y hoy es un día de ejemplo. Estoy en la sede de la comunidad Lomas del Sur (inventada). "
         "Voy a contar la limpieza de la vertiente. Primero nos juntamos a las nueve de la mañana. Luego cada familia llevó una pala. "
         "Doña Clara contó que esta tarea se hace cada primavera. Después compartimos pan. Gracias a doña Clara por autorizarme a contarlo.»")
FICHA_R = ("Ficha de registro (inventada). Qué se registra: la narración de Tomás sobre la limpieza de la vertiente. Recurso: grabadora de voz, usada por un adulto de la escuela. "
           "Quién autoriza: doña Clara, de la comunidad Lomas del Sur (inventada). Dónde se guarda: en la computadora de la escuela, en una carpeta con acceso del curso. "
           "Con quién se comparte: solo con el curso y la comunidad. Límite: no se registra a ninguna persona sin su permiso ni el lugar de respeto de la comunidad.")

L(
    LF6, 1,
    materials=MAT,
    use="Aprenderé a situar un registro con recursos tecnológicos: qué recurso se usa, qué se registra, quién autoriza, dónde se guarda y qué no se registra. Sirve para usar las tecnologías al servicio de la comunidad y no para apropiarme de lo suyo.",
    prior=["Sé que un relato o una práctica tiene dueños y se usa con permiso.", "Sé que lo reservado por la comunidad no se publica."],
    explain=[
        "Los recursos tecnológicos, como una grabadora de voz, una cámara, un programa para escribir o una presentación, permiten registrar y narrar situaciones personales, acontecimientos de la comunidad y prácticas tradicionales. Registrar es guardar algo para volver a escucharlo o verlo. Se hace siempre con una persona adulta y con permiso.",
        "Antes de registrar, situamos el registro con una ficha: qué se registra, con qué recurso, quién autoriza, dónde se guarda, con quién se comparte y cuál es el límite. Pedimos permiso a toda persona que habla o aparece. No registramos ceremonias, lugares de respeto ni a personas que no quieren. Tampoco publicamos nada en internet sin la autorización de la comunidad y de un adulto.",
        "Si el registro se hace en lengua indígena, la lengua la hablan o la enseñan personas de la comunidad y el educador tradicional. Nosotros ayudamos con la tecnología, pero no hablamos por ellos ni cambiamos lo que dicen. En este cuaderno practicamos con un registro inventado en castellano.",
    ],
    vocab=[("registrar", "guardar algo para volver a escucharlo o verlo"), ("recurso tecnológico", "herramienta digital, como una grabadora o una cámara"), ("autorizar", "dar permiso"), ("narrar", "contar lo que ocurrió"), ("límite de registro", "lo que no se graba ni se escribe")],
    worked=[
        W("Leer una ficha de registro", FICHA_R + " ¿Quién autoriza el registro?", ["Busco «Quién autoriza».", "Dice doña Clara."], "Doña Clara."),
        W("Detectar un límite", FICHA_R + " ¿Se puede registrar el lugar de respeto de la comunidad?", ["Reviso «Límite».", "Dice que no se registra."], "No."),
    ],
    mistakes=[
        M("Grabar sin pedir permiso porque «es solo para mí».", "Las personas que hablan o aparecen deciden.", "Pido permiso antes de grabar."),
        M("Subir un registro a internet sin permiso.", "La comunidad decide dónde se comparte.", "Solo comparto con quien la ficha indica."),
    ],
    R=[
        ex(FICHA_R + " ¿Qué recurso se usa?", "Una grabadora de voz", "La ficha lo indica."),
        ex(FICHA_R + " ¿Con quién se comparte el registro: con el curso y la comunidad o con todo internet?", "Con el curso y la comunidad", "Así lo indica la ficha."),
        ex("Registrar siempre se hace: A) con una persona adulta y con permiso B) a escondidas", "A", "Es la regla de la clase."),
    ],
    C=[
        ex("Verdadero o falso: puedo grabar a una persona sin pedirle permiso si es solo para mí.", "Falso", "Siempre se pide permiso."),
        ex("¿Para qué sirve la ficha de registro? A) para saber qué se registra, quién autoriza y qué no se registra B) para decorar", "A", "Sitúa y protege el registro."),
        ex("Verdadero o falso: las ceremonias y los lugares de respeto se registran.", "Falso", "Son parte de los límites."),
    ],
    A=[
        ex(FICHA_R + " ¿Dónde se guarda el registro?", "En la computadora de la escuela", "La ficha lo dice."),
        ex("Une cada dato de la ficha con su pregunta. 1) autoriza 2) recurso 3) límite. a) ¿con qué se registra? b) ¿qué no se registra? c) ¿quién da permiso?", "1-c, 2-a, 3-b", "Cada dato responde una pregunta."),
        ex("Una ficha de registro dice: «Qué se registra: una conversación. Recurso: cámara. Dónde se guarda: en la escuela». De estos dos datos, ¿cuál falta: quién autoriza o el recurso?", "Quién autoriza", "El recurso sí aparece."),
    ],
    Z=[
        ex("Pablo quiere subir a internet el registro de la limpieza de la vertiente «porque quedó lindo». ¿Qué falla? A) no tiene permiso de la comunidad ni de un adulto B) es muy largo", "A", "La ficha dice con quién se comparte."),
        ex("Una niña graba una conversación y alguien dice que no quiere salir en la grabación. ¿Qué debe hacer? A) borrar su parte y respetarlo B) dejarla igual", "A", "Cada persona decide si se registra."),
    ],
    D=[
        ex("Dos fichas. F1: tiene recurso, autorización y límite. F2: solo tiene recurso. ¿Con cuál puedes registrar?", "Con la F1", "La F2 no tiene permiso ni límite."),
        ex("Si no sabes si un lugar es de respeto para la comunidad, ¿qué haces antes de fotografiarlo? A) pregunto a la comunidad B) lo fotografío igual", "A", "La comunidad dice qué se registra."),
    ],
    context=[ex("En una actividad de la comunidad quieres filmar con el celular de un adulto de tu curso. ¿Qué haces primero? A) pedir permiso a la persona responsable y a quienes aparecen B) filmar y pedir permiso después", "A", "El permiso va antes.")],
    selfcheck=[
        ex("Nombra tres datos de la ficha de registro.", "Tres entre: qué se registra, recurso, quién autoriza, dónde se guarda, con quién se comparte, límite", "Son datos de la ficha."),
        ex("Verdadero o falso: puedo publicar un registro sin pedir permiso.", "Falso", "Se pide permiso a las personas y a la comunidad."),
        ex("¿Quién enseña la lengua indígena en un registro: el educador tradicional o la tecnología?", "El educador tradicional", "La tecnología solo ayuda a guardar."),
    ],
    task=T("Con la ficha de registro de práctica: «" + FICHA_R + "» haz tu propia ficha para registrar un acontecimiento inventado de tu escuela (por ejemplo, una reunión de curso). Escribe: qué se registra, recurso, quién autoriza, dónde se guarda, con quién se comparte y límite. Agrega una línea «Pediría permiso a…» con las personas que hablarían o aparecerían.",
           "Qué se registra: la reunión de curso. Recurso: grabadora de voz con ayuda de un adulto. Autoriza: la profesora jefa y quienes hablan. Se guarda: en la computadora de la escuela. Se comparte: con el curso. Límite: no se graba a quien no quiera. Pediría permiso a la profesora y a cada estudiante que hable.",
           ["completa los seis datos", "declara un límite", "nombra a quienes dan permiso"], ["ficha de registro completa", "línea de permisos"], ["registrar sin permiso", "publicar en internet"],
           "Pedir que explique quién da permiso a quién; valorar que declare lo que no se registra."),
    reinforce="Copia la ficha de registro y subraya con un color el límite.",
    extend="Escribe cuatro preguntas de permiso que harías antes de grabar una conversación.",
)

L(
    LF6, 2,
    materials=MAT,
    use="Aprenderé a escuchar o leer un registro con límites declarados: qué dice, qué no dice y qué faltó pedir. Sirve para comprobar que un registro respeta a las personas.",
    prior=["Sé situar un registro con una ficha.", "Sé que cada persona decide si se registra."],
    explain=[
        "Un registro, como el guion de una grabación, se escucha o se lee con atención para entender quién habla, dónde está, qué cuenta y cuándo ocurrió. También se revisa si cumple la ficha: si dice quién autorizó, si no incluye lo que debía quedar fuera y si agradece a quien contó. Un registro bien hecho respeta a las personas.",
        "Leer con límites declarados es decir tres cosas: lo que el registro dice, lo que no dice y lo que no debía registrarse. Por ejemplo, el guion de Tomás cuenta la limpieza de la vertiente, pero no dice cuántas familias fueron. Eso no se completa con ideas propias. Y si el guion nombra un lugar de respeto cuando la ficha lo prohíbe, hay que señalarlo.",
        "Cuando un registro es en lengua indígena, escuchamos con respeto y pedimos al educador tradicional que nos ayude a comprender. No traducimos por nuestra cuenta lo que no entendemos. Y si encontramos una parte que no debía registrarse, avisamos a un adulto para que se retire con la persona responsable.",
    ],
    vocab=[("guion", "texto escrito que dice qué se va a decir en una grabación"), ("fecha", "día en que ocurrió o se hizo algo"), ("agradecer", "reconocer a quien nos ayudó o autorizó"), ("revisar", "mirar un trabajo para comprobar que cumple lo acordado"), ("retirar", "sacar una parte de un registro")],
    worked=[
        W("Leer el registro", GUION + " ¿A qué hora se juntaron?", ["Busco la hora.", "Dice a las nueve de la mañana."], "A las nueve de la mañana."),
        W("Lo que no dice", GUION + " ¿Dice cuántas familias fueron?", ["Reviso el guion.", "No lo menciona."], "No, el guion no lo dice."),
    ],
    mistakes=[
        M("Completar con mi imaginación lo que el registro no dice.", "Atribuyo algo que no se contó.", "Digo que el registro no lo dice."),
        M("No revisar si el registro cumple la ficha.", "Puede quedar algo que no debía registrarse.", "Comparo el registro con la ficha."),
    ],
    R=[
        ex(GUION + " ¿Qué llevó cada familia?", "Una pala", "El guion lo dice."),
        ex(GUION + " ¿Cada cuánto se hace la limpieza según doña Clara?", "Cada primavera", "El guion lo dice."),
        ex(GUION + " ¿Qué compartieron después?", "Pan", "El guion lo menciona."),
    ],
    C=[
        ex(GUION + " Verdadero o falso: el guion dice cuántas familias participaron.", "Falso", "No lo menciona."),
        ex("Un registro bien hecho: A) respeta a las personas y cumple la ficha B) dura mucho", "A", "Eso lo hace correcto."),
        ex(GUION + " ¿A quién agradece Tomás al final?", "A doña Clara", "El guion termina agradeciéndole a ella."),
    ],
    A=[
        ex(GUION + " Ordena: a) compartieron pan b) se juntaron c) llevaron palas. Escribe las letras.", "b, c, a", "El guion sigue ese orden."),
        ex(GUION + " ¿Cuál afirmación está en el guion? A) la tarea se hace cada primavera B) la tarea se hace cada verano", "A", "La B no aparece."),
        ex(GUION + " Revisa con la ficha: «no se registra a ninguna persona sin su permiso». ¿Cumple el guion con la autorización de doña Clara? Responde Sí o No.", "Sí", "Tomás agradece a doña Clara por autorizarlo."),
    ],
    Z=[
        ex("En un registro se escucha: «Y ahora vamos al lugar de respeto de la comunidad para mostrarlo». La ficha lo prohíbe. ¿Qué haces? A) aviso a un adulto para retirarlo B) lo dejo", "A", "Esa parte no debía registrarse."),
        ex("Rafael dice: «Como el guion dice que la tarea se hace cada primavera, todas las comunidades la hacen igual». ¿Qué error comete?", "Generaliza lo que dice un registro", "El guion habla de una comunidad."),
    ],
    D=[
        ex("Dos lecturas del guion. L1: «Tomás cuenta que cada familia llevó una pala». L2: «Tomás cuenta que cada familia llevó 3 palas». ¿Cuál es fiel?", "L1", "L2 agrega un dato."),
        ex(GUION + " Si el guion no dice la fecha exacta, ¿qué respondes si te preguntan? A) «El registro no la dice» B) «Fue el 15 de septiembre»", "A", "No se inventan datos."),
    ],
    context=[ex("Al escuchar un registro de la comunidad, alguien menciona un nombre de persona que no pidió salir. ¿Qué haces? A) aviso a un adulto para que lo retire con la persona responsable B) lo comento con todo el curso", "A", "Se protege a la persona.")],
    selfcheck=[
        ex("Nombra las tres cosas que se declaran al leer con límites.", "Lo que dice, lo que no dice y lo que no debía registrarse", "Son los límites de la lectura."),
        ex(GUION + " ¿En qué lugar está Tomás?", "En la sede de Lomas del Sur", "El guion lo dice."),
        ex("Verdadero o falso: puedo completar con ideas mías lo que el registro no dice.", "Falso", "Se dice que no lo dice."),
    ],
    task=T("Lee el guion de práctica: «" + GUION.split("«", 1)[1].rstrip("»") + "» Haz una tabla de tres columnas: «El registro dice» (cuatro datos), «El registro no dice» (dos datos) y «Revisión con la ficha» (dos preguntas con respuesta sí o no, por ejemplo: ¿agradece a quien autorizó?). Escribe una frase con «Pediría ayuda al educador tradicional para…».",
           "Dice: Tomás está en la sede; cuenta la limpieza de la vertiente; se juntaron a las nueve; cada familia llevó una pala. No dice: cuántas familias fueron; cuánto duró. Revisión: ¿agradece a quien autorizó? Sí. ¿Menciona un lugar de respeto? No. Pediría ayuda al educador tradicional para contar esta tarea en la lengua de mi comunidad.",
           ["registra datos fieles", "reconoce lo que no dice", "revisa con la ficha"], ["tabla de tres columnas", "frase final"], ["inventar datos", "no revisar el registro"],
           "Pedir que muestre en el guion cada dato; valorar la revisión con la ficha."),
    reinforce="Subraya en el guion las personas y los lugares con colores distintos.",
    extend="Escribe tres preguntas que harías para revisar si un registro de la comunidad respeta su ficha.",
)

L(
    LF6, 3,
    materials=MAT,
    use="Aprenderé a elegir el recurso tecnológico adecuado para narrar una situación o describir una práctica, y a ver cómo se relaciona con la cultura oral. Sirve para que la tecnología ayude a conservar y no a cambiar lo que la comunidad cuenta.",
    prior=["Sé leer un registro con límites declarados.", "Sé que toda grabación o foto necesita permiso."],
    explain=[
        "Cada recurso sirve para algo distinto. La grabadora de voz guarda la voz y es útil para narrar con palabras. La cámara de fotos guarda cómo se ve algo, como una planta o un instrumento, y sirve para mostrar. Un programa para escribir guarda textos como listas y descripciones. Una presentación junta imágenes y textos para explicar a otras personas.",
        "En la tradición oral, la palabra hablada es muy importante. Por eso, la grabación de voz puede ayudar a conservar relatos y conversaciones tal como se dijeron, siempre con permiso. Si la práctica se explica mejor mostrando, como los pasos de un tejido, conviene usar fotos o dibujos con texto. No todo debe registrarse: hay cosas que la comunidad prefiere guardar.",
        "Elegimos el recurso preguntando tres cosas: qué quiero guardar, quién lo autoriza y quién lo va a usar. Si queremos narrar en la lengua de la comunidad, la persona que la habla es quien narra, y nosotros ayudamos con el recurso. No cambiamos lo que dice ni agregamos efectos que lo deformen.",
    ],
    vocab=[("grabadora de voz", "recurso que guarda sonidos y voces"), ("cámara de fotos", "recurso que guarda cómo se ve algo"), ("procesador de textos", "programa para escribir y guardar textos"), ("presentación", "conjunto de láminas con imágenes y textos para explicar algo"), ("conservar", "guardar algo para que no se pierda")],
    worked=[
        W("Elegir el recurso", "Quieres guardar una conversación de unos minutos con una persona de la comunidad. ¿Qué recurso eliges?", ["Lo importante es la voz.", "La grabadora de voz guarda la voz."], "La grabadora de voz."),
        W("Elegir para mostrar", "Quieres mostrar cómo se ve una planta de la huerta de la comunidad. ¿Qué recurso eliges?", ["Lo importante es cómo se ve.", "La cámara guarda la imagen."], "La cámara de fotos (con permiso)."),
    ],
    mistakes=[
        M("Usar un solo recurso para todo.", "No siempre guarda lo que se necesita.", "Elijo según lo que quiero guardar."),
        M("Agregar música o efectos a una voz de la comunidad.", "Cambia cómo se escucha lo que dijo.", "Dejo la voz tal como se dijo."),
    ],
    R=[
        ex("Para guardar la voz de una persona eliges: A) una grabadora de voz B) una cámara de fotos", "A", "La grabadora guarda sonidos."),
        ex("Para guardar cómo se ve una planta eliges: A) una cámara de fotos B) una grabadora", "A", "La cámara guarda imágenes."),
        ex("Para escribir una lista de pasos eliges: A) un procesador de textos B) una cámara", "A", "El procesador de textos guarda textos."),
    ],
    C=[
        ex("Verdadero o falso: la grabación de voz puede ayudar a conservar lo que se dijo tal como se dijo.", "Verdadero", "Guarda las palabras y la voz."),
        ex("Verdadero o falso: todo lo de la comunidad debe registrarse con tecnología.", "Falso", "La comunidad decide qué se guarda."),
        ex("Si la persona que narra habla la lengua indígena, ¿quién narra: ella o yo?", "Ella", "Yo ayudo con el recurso."),
    ],
    A=[
        ex("Une cada propósito con el recurso. 1) guardar una narración 2) mostrar cómo se ve un telar 3) escribir los pasos. a) cámara b) grabadora c) procesador de textos", "1-b, 2-a, 3-c", "Cada recurso guarda algo distinto."),
        ex("Quieres explicar a tu curso cómo se hace una práctica de la comunidad con fotos y frases. ¿Qué recurso eliges? A) una presentación B) solo una grabadora", "A", "Junta imágenes y textos."),
        ex("Una persona mayor cuenta un acontecimiento de la comunidad y no quiere salir en fotos, pero acepta la grabación de voz. ¿Qué usas?", "La grabadora de voz", "Respeta su decisión."),
    ],
    Z=[
        ex("Tomás quiere agregar música de fondo a la voz de doña Clara «para que suene más lindo». ¿Qué falla?", "Cambia lo que ella dijo", "La voz debe quedar tal como se dijo."),
        ex("Una niña dice: «Si grabé la voz, ya no hace falta preguntar nada al educador». ¿Qué falla? A) la voz no reemplaza su validación B) nada", "A", "La validación la hace el educador."),
    ],
    D=[
        ex("Quieres guardar los pasos de una práctica de la comunidad: ¿qué conjunto es más completo? A) fotos con frases y una narración de voz B) solo una foto", "A", "Muestra y cuenta."),
        ex("Si un recurso no es adecuado para lo que la comunidad autorizó, ¿qué haces? A) elijo otro o no registro B) lo uso igual", "A", "El permiso manda."),
    ],
    context=[ex("Tu curso quiere guardar un relato de una persona mayor de la comunidad. ¿Qué recurso consultas con ella? A) la grabadora de voz B) un programa de dibujo", "A", "La voz es lo que importa.")],
    selfcheck=[
        ex("Escribe qué guarda una cámara de fotos.", "Cómo se ve algo", "La cámara guarda imágenes de lo que se ve."),
        ex("Verdadero o falso: la tecnología puede cambiar lo que dice la comunidad si agrego efectos.", "Verdadero", "Por eso no se agregan."),
        ex("¿Qué tres preguntas hago para elegir el recurso?", "Qué quiero guardar, quién lo autoriza y quién lo va a usar", "Son las preguntas de la clase."),
    ],
    task=T("Elige tres situaciones inventadas: (a) guardar una conversación con una vecina sobre su huerta; (b) mostrar cómo se ve una herramienta de tejer; (c) escribir los pasos para sembrar una semilla. Para cada una escribe qué recurso usarías, por qué y quién debe dar permiso. Termina con una frase sobre qué no registrarías aunque fuera posible.",
           "a) Grabadora de voz, porque importa lo que dice la vecina; ella debe dar permiso. b) Cámara de fotos, porque importa cómo se ve; permiso de la persona dueña de la herramienta. c) Procesador de textos, porque son pasos; permiso de quien enseña. No registraría ningún lugar de respeto.",
           ["elige recursos adecuados", "justifica la elección", "nombra quién autoriza"], ["tres situaciones resueltas", "frase final"], ["usar un solo recurso", "no pedir permiso"],
           "Pedir que explique por qué cada recurso guarda lo que se necesita; valorar el límite final."),
    reinforce="Escribe en una tabla cuatro recursos y qué guarda cada uno.",
    extend="Explica por qué la palabra hablada puede guardarse mejor con la voz que con un texto.",
)

L(
    LF6, 4,
    materials=MAT,
    use="Aprenderé a construir un guion para narrar una situación personal o un acontecimiento de la comunidad, con datos de registro, créditos y agradecimientos. Sirve para que un registro sea claro, atribuido y respetuoso.",
    prior=["Sé elegir el recurso adecuado y revisar un registro con su ficha.", "Sé usar «según» para atribuir una idea."],
    explain=[
        "Un guion de registro tiene cuatro partes. Primero, la presentación: quién habla, qué día es y dónde está. Segundo, la narración: qué ocurrió, con quiénes y en qué orden. Tercero, la atribución: de quién viene lo que se cuenta, con frases como «según doña Clara». Cuarto, el cierre: agradecimiento a quien autorizó y mención de que se pidió permiso.",
        "Para narrar una situación personal, hablamos solo de lo nuestro y evitamos datos privados, como la dirección o los nombres de personas que no autorizaron. Para narrar un acontecimiento de la comunidad, contamos lo que vimos y lo que nos contaron, indicando quién lo contó. No hablamos por la comunidad completa ni agregamos explicaciones que nadie dio.",
        "Si queremos narrar en la lengua indígena de la comunidad, pedimos al educador tradicional que nos ayude a decir y escribir el guion, y anotamos quién nos ayudó. Antes de usar el registro, lo mostramos a la persona que autorizó. Así cuidamos que lo contado sea fiel y respetuoso.",
    ],
    vocab=[("presentación", "parte inicial del guion: quién, cuándo y dónde"), ("narración", "parte que cuenta lo que ocurrió"), ("atribución", "decir de quién viene lo que se cuenta"), ("cierre", "parte final que agradece y avisa del permiso"), ("dato privado", "información personal que no se comparte, como una dirección")],
    worked=[
        W("Ordenar un guion", "Partes: a) Gracias a doña Clara por autorizarme b) Hoy es un día de ejemplo y estoy en la sede c) Doña Clara contó que se limpia la vertiente d) Nos juntamos a las nueve. ¿En qué orden va el guion?", ["Primero la presentación.", "Luego la narración y la atribución.", "Al final el agradecimiento."], "b, d, c, a"),
        W("Quitar un dato privado", "Borrador: «Vivo en la calle Los Olmos 123 y hoy fuimos a limpiar la vertiente». ¿Qué corriges?", ["La dirección es un dato privado.", "La quito."], "«Hoy fuimos a limpiar la vertiente»."),
    ],
    mistakes=[
        M("Poner mi dirección o la de otras personas en el guion.", "Son datos privados.", "No los incluyo."),
        M("Contar una explicación que nadie dio.", "Atribuyo algo inventado a la comunidad.", "Cuento solo lo que vi o lo que me contaron, con el nombre de quien lo contó."),
    ],
    R=[
        ex("La primera parte de un guion es: A) la presentación B) el cierre", "A", "Se empieza diciendo quién, cuándo y dónde."),
        ex("El agradecimiento va: A) al final B) al comienzo", "A", "Está en el cierre."),
        ex("Una dirección de casa es: A) un dato privado B) un dato que siempre se comparte", "A", "No se comparte."),
    ],
    C=[
        ex("¿Qué frase atribuye? A) «Según doña Clara, se limpia cada primavera» B) «Se limpia cada primavera»", "A", "La A dice de quién viene."),
        ex("Verdadero o falso: puedo contar una explicación que nadie dio si suena bien.", "Falso", "Se cuenta lo que vi o me contaron."),
        ex("Verdadero o falso: el guion debe decir que se pidió permiso.", "Verdadero", "Es parte del cierre."),
    ],
    A=[
        ex("Ordena las partes del guion: a) agradezco b) narro c) me presento d) atribuyo lo que me contaron. Escribe las letras.", "c, b, d, a", "Presentación, narración, atribución y cierre."),
        ex("Borrador: «Mi amiga Ana, que vive en Pasaje Sur 45, dijo que sí». ¿Qué dato debes quitar?", "La dirección de Ana", "Es un dato privado."),
        ex("¿Qué tres datos da la presentación de un guion? A) quién habla, qué día es y dónde está B) qué se come, qué se lleva y quién gana", "A", "La presentación dice quién, cuándo y dónde."),
    ],
    Z=[
        ex("Camila narra: «Esta tarea es sagrada para toda la comunidad». Nadie lo dijo. ¿Qué falla?", "Inventa un significado que nadie dio", "Solo la comunidad dice qué es sagrado."),
        ex("Un compañero quiere usar el registro sin mostrárselo a doña Clara. ¿Qué debe hacer? A) mostrárselo antes de usarlo B) usarlo igual", "A", "La persona que autorizó debe revisarlo."),
    ],
    D=[
        ex("Dos cierres. C1: «Gracias a doña Clara por autorizarme». C2: «Gracias por escucharme». ¿Cuál cumple lo que pide el guion?", "C1", "Agradece a quien autorizó."),
        ex("Si no estás seguro de un dato de la comunidad, ¿qué escribes en el guion? A) «No lo sé; lo consultaré» B) un dato probable", "A", "No se inventan datos."),
    ],
    context=[ex("Te piden narrar un acontecimiento de tu comunidad para un registro. ¿Qué haces antes de grabar? A) preparo el guion con presentación, narración, atribución y cierre B) improviso sin permiso", "A", "El guion cuida el respeto.")],
    selfcheck=[
        ex("Nombra las cuatro partes de un guion de registro.", "Presentación, narración, atribución y cierre", "Son las partes de la clase."),
        ex("Verdadero o falso: debo incluir mi dirección para que se sepa quién soy.", "Falso", "Es un dato privado."),
        ex("¿Quién debe revisar el registro antes de usarlo: la persona que autorizó o nadie?", "La persona que autorizó", "Así se cuida que sea fiel."),
    ],
    task=T("Escribe un guion de seis frases para narrar un acontecimiento inventado de una comunidad (por ejemplo, una reunión de vecinos para limpiar un camino). Incluye: presentación (nombre inventado, día de ejemplo y lugar), tres frases de narración, una frase de atribución con «según…» y un cierre con agradecimiento y permiso. Revisa que no tenga datos privados y anota quién lo revisaría antes de usarlo.",
           "Me llamo Rosa, hoy es un día de ejemplo y estoy en la sede. Los vecinos se juntaron a las diez. Cada uno llevó una escoba. Después compartimos un té. Según don Mateo, esta reunión se hace una vez al año. Gracias a don Mateo por autorizarme a contarlo. Revisor: don Mateo y un adulto de la escuela.",
           ["incluye las cuatro partes", "atribuye con «según»", "no incluye datos privados"], ["guion de seis frases", "nota de revisión"], ["poner datos privados", "inventar explicaciones"],
           "Pedir que señale las cuatro partes; valorar que anote quién revisa."),
    reinforce="Reordena un guion desordenado de cuatro frases en tu cuaderno.",
    extend="Escribe una versión del guion donde pidas ayuda al educador tradicional para decirlo en la lengua de tu comunidad.",
)

L(
    LF6, 5,
    materials=MAT,
    use="Aprenderé a comparar recursos de registro, como el audio, la foto y el texto, y a cuidar y devolver los registros a la comunidad sin decir que uno es mejor. Sirve para decidir con criterio y proteger lo que la comunidad confía.",
    prior=["Sé elegir recursos y escribir un guion de registro.", "Sé que contrastar es distinto de jerarquizar."],
    explain=[
        "Cada recurso conserva algo distinto y tiene límites. El audio conserva la voz, el ritmo y las pausas, pero no muestra gestos. La foto conserva cómo se ve algo en un instante, pero no cuenta lo que ocurrió antes ni después. El texto conserva los datos y el orden, pero no la voz. Ninguno es mejor en todo: sirven para cosas distintas.",
        "Para contrastar usamos criterios neutros: qué conserva, qué no conserva, qué riesgos tiene para las personas y quién puede usarlo. El audio y la foto pueden mostrar a una persona sin que lo quiera, por eso piden permiso; el texto puede cambiar las palabras si se copia mal. Siempre decimos «sirve para…» y «no sirve para…» sin juzgar.",
        "Después de registrar, cuidamos el registro: se guarda donde indica la ficha, se hace una copia con un adulto y se muestra a la comunidad. Devolver el registro es una forma de reciprocidad: la comunidad nos enseñó y nosotros le devolvemos lo que aprendimos. Si la comunidad pide retirar o cambiar algo, lo hacemos.",
    ],
    vocab=[("conservar", "guardar algo para que no se pierda"), ("riesgo", "posibilidad de que algo salga mal"), ("copia", "otro ejemplar guardado de un registro"), ("devolución", "volver a entregar a la comunidad lo que se registró"), ("reciprocidad", "dar de vuelta a quien nos dio")],
    worked=[
        W("Contrastar dos recursos", "Compara audio y foto con el criterio «qué conserva».", ["El audio conserva la voz y las pausas.", "La foto conserva cómo se ve algo en un instante."], "El audio conserva lo que se dijo; la foto, cómo se veía algo."),
        W("Devolver un registro", "Terminaste un registro con permiso de doña Clara. ¿Qué haces después?", ["Guardo una copia con un adulto.", "Se lo muestro a doña Clara y a la comunidad."], "Lo guardo donde indica la ficha y lo devuelvo mostrándolo."),
    ],
    mistakes=[
        M("Decir que el audio es mejor que el texto.", "Cada uno conserva algo distinto.", "Comparo qué conserva cada uno."),
        M("Guardar el registro y no devolverlo.", "La comunidad no sabe qué se hizo con lo que contó.", "Muestro el resultado a la comunidad."),
    ],
    R=[
        ex("El audio conserva: A) la voz y las pausas B) los colores", "A", "El audio guarda sonidos."),
        ex("La foto conserva: A) cómo se ve algo en un instante B) lo que se dijo", "A", "La foto guarda una imagen."),
        ex("Devolver un registro significa: A) mostrarlo a la comunidad B) borrarlo", "A", "Es una forma de reciprocidad."),
    ],
    C=[
        ex("Verdadero o falso: el texto conserva la voz de quien habló.", "Falso", "El texto conserva datos y orden, no la voz."),
        ex("Verdadero o falso: un recurso puede ser mejor en todo.", "Falso", "Cada uno sirve para cosas distintas."),
        ex("¿Qué es la reciprocidad? A) dar de vuelta a quien nos dio B) guardar todo para mí", "A", "La comunidad nos enseñó y le devolvemos."),
    ],
    A=[
        ex("Compara con el criterio «qué no conserva». Audio: no muestra gestos. Foto: ___. Completa con una opción: A) no cuenta lo que ocurrió antes ni después B) no muestra nada", "A", "Una foto es un instante."),
        ex("Une cada recurso con un riesgo. 1) audio o foto de una persona 2) texto copiado. a) puede cambiar las palabras b) puede mostrar a alguien sin permiso", "1-b, 2-a", "Cada recurso tiene un riesgo distinto."),
        ex("Quieres guardar los pasos exactos de una práctica y también cómo se ve. ¿Qué combinas? A) texto y fotos B) solo audio", "A", "Texto y fotos se complementan entre sí."),
    ],
    Z=[
        ex("Un compañero dice: «El audio es mejor porque se escucha la voz». ¿Qué error comete?", "Jerarquiza sin comparar lo que conserva cada recurso", "Cada recurso conserva algo distinto."),
        ex("La comunidad pide retirar una parte del registro ya hecho. ¿Qué haces? A) la retiro y aviso a un adulto B) la dejo porque ya está", "A", "La comunidad decide."),
    ],
    D=[
        ex("Elige la comparación respetuosa: A) «El audio conserva la voz; el texto conserva el orden de los datos» B) «El texto es más serio que el audio»", "A", "La A describe lo que conserva."),
        ex("Si el registro tiene una parte con una persona que no quiere salir, ¿qué debes hacer antes de devolverlo? A) quitar esa parte B) avisar a todos", "A", "Se respeta su decisión."),
    ],
    context=[ex("Terminaste un registro con ayuda de un adulto y quieres compartirlo en una red social. La ficha dice que se comparte solo con el curso y la comunidad. ¿Qué haces? A) no lo subo y lo muestro a la comunidad B) lo subo porque es bueno", "A", "La ficha manda.")],
    selfcheck=[
        ex("Nombra un criterio neutro para comparar recursos de registro.", "Qué conserva, qué no conserva, qué riesgos tiene o quién puede usarlo", "Son criterios de la clase."),
        ex("Verdadero o falso: devolver un registro a la comunidad es una forma de agradecer.", "Verdadero", "Devolver es una forma de reciprocidad."),
        ex("Verdadero o falso: puedo cambiar un registro sin avisar si me parece mejor.", "Falso", "La comunidad decide."),
    ],
    task=T("Haz una tabla de tres columnas (audio, foto, texto) con tres filas: «qué conserva», «qué no conserva» y «qué riesgo tiene para las personas». Escribe una semejanza, una diferencia y una frase que explique por qué no se debe decir cuál recurso es mejor. Termina con un plan de devolución de cuatro pasos: guardar, hacer copia con un adulto, mostrar a la comunidad y pedir correcciones.",
           "Audio: conserva voz y pausas; no muestra gestos; puede grabar a alguien sin permiso. Foto: conserva cómo se ve algo; no cuenta lo que pasó antes; puede mostrar a alguien sin permiso. Texto: conserva datos y orden; no conserva la voz; puede cambiar palabras al copiar. Semejanza: los tres guardan información. Diferencia: cada uno guarda algo distinto. No se dice cuál es mejor porque sirven para cosas distintas. Devolución: guardar, copia con un adulto, mostrar a la comunidad y pedir correcciones.",
           ["usa criterios neutros", "no jerarquiza", "incluye plan de devolución"], ["tabla de comparación", "semejanza y diferencia", "plan de cuatro pasos"], ["decir cuál recurso es mejor", "olvidar la devolución"],
           "Pedir que justifique cada celda; valorar el plan de devolución."),
    reinforce="Escribe tres frases «sirve para…» y tres «no sirve para…» sobre el audio, la foto y el texto.",
    extend="Explica con tus palabras por qué devolver un registro a la comunidad es parte de usar bien la tecnología.",
)
