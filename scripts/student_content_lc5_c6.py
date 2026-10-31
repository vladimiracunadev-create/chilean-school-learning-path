"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS04 (desarrollar la escritura para transmitir mensajes que incluyan algunas palabras o expresiones en lengua
indígena, o en castellano, culturalmente significativas, en diversas situaciones del medio natural, social y cultural).

Criterio de autoría: todos los mensajes, escuelas y personas son inventados solo para practicar y están rotulados como
tales. Los mensajes se escriben en castellano; las únicas palabras en lengua indígena son «mari mari» (saludo) y
«chaltumay» (gracias), ambas en mapuzugun, con su glosa. Las palabras del castellano de Chile (minga, once) se explican.
No se inventan frases en lengua indígena: las frases completas las enseña el educador/a tradicional. Los mensajes no
llevan datos personales, direcciones ni teléfonos; usan nombres de curso o de cargo. Los mensajes reales se revisan con el
educador/a tradicional antes de enviarse.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS4 = "LC05 OA LS04"

CONSULT = " Recuerda: cómo se escriben y cuándo se usan las palabras de una lengua indígena lo enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de enviar tu mensaje. No escribas datos personales, direcciones ni teléfonos."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

GLO = "Glosario de práctica: «mari mari» es un saludo en mapuzugun que se dice al encontrarse con alguien. «Chaltumay» quiere decir gracias en mapuzugun. «Minga» es, en el castellano de Chile, un trabajo en que varias personas ayudan juntas. «Once» es la comida liviana de la tarde."
MS1 = "Mensaje 1 (inventado). Para: la señora directora. «Mari mari, señora directora. El 5.º básico quiere invitarla a una minga para limpiar el patio el viernes a las diez. Si usted puede, nos alegraría mucho. Chaltumay por su tiempo. Un saludo, el 5.º básico.»"
MS2 = "Mensaje 2 (inventado). Para: el curso. «Hola. Mañana traigan una bolsa para la minga del jardín. No olviden agua para tomar. Gracias. El comité del curso.»"


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


# ============================================================ LS04 clase 1 · situar el mensaje
L(
    LS4, 1,
    materials="Lápiz y hoja. Los mensajes están escritos aquí y son inventados para practicar. Puedes escribir todo en papel.",
    use="Aprenderé a decidir, antes de escribir un mensaje, para qué lo escribo, a quién va dirigido, en qué situación y qué palabras significativas incluiré con su fuente. Sirve para escribir mensajes claros y respetuosos.",
    prior=["Sé escuchar y exponer con palabras significativas.", "Sé que las palabras indígenas se copian como las enseñó su fuente."],
    explain=[
        "Un mensaje es un texto breve que transmite algo a otra persona: una invitación, un aviso, un agradecimiento o una petición. Antes de escribirlo, decido cuatro cosas: el propósito, es decir, para qué lo escribo; el destinatario, que es la persona que lo recibirá; la situación, que puede ser del medio natural, social o cultural; y las palabras significativas que usaré.",
        "Las situaciones son variadas. Una situación del medio natural es, por ejemplo, cuidar un río o un jardín. Una situación social es invitar a un vecino o agradecer a un curso. Una situación cultural es pedir a un educador tradicional que enseñe un saludo. En cada una puedo incluir palabras en castellano culturalmente significativas, como «minga», o una palabra de una lengua indígena, como «mari mari» o «chaltumay».",
        "Si uso una palabra indígena en mi mensaje, anoto quién me la enseñó y la copio tal cual. No escribo en nombre de otra persona ni uso su nombre sin permiso. Y no pongo datos personales, como direcciones o teléfonos. Con estas decisiones tomadas, escribir es más fácil y el mensaje queda claro.",
    ],
    vocab=[("mensaje", "texto breve que transmite algo a otra persona"), ("propósito", "para qué escribo"), ("destinatario", "persona que recibe el mensaje"), ("remitente", "persona o grupo que envía el mensaje"), ("situación", "momento o lugar en que se escribe el mensaje")],
    worked=[
        W("Reconocer propósito y destinatario", MS1 + " ¿Cuál es el propósito y quién es el destinatario?", ["Leo para qué escribe el curso: invitar a una minga.", "Veo para quién escribe: la señora directora.", "Los uno."], "propósito: invitar a una minga; destinatario: la directora"),
        W("Reconocer el tipo de situación", MS1 + " Según la clase, invitar a una persona es una situación social. ¿Qué tipo de situación es la del mensaje 1: natural, social o cultural?", ["El mensaje 1 invita a la señora directora a una minga.", "Invitar a una persona es una situación social.", "Entonces la situación es social."], "social"),
    ],
    mistakes=[
        M("Escribir el mensaje sin pensar a quién va dirigido.", "No sé qué tono usar ni qué decir.", "Primero decido el destinatario y el propósito."),
        M("Usar el nombre de una persona sin su permiso para firmar el mensaje.", "Hablo en su nombre sin que lo sepa.", "Firmo como curso o como yo, o pido permiso."),
    ],
    R=[
        ex(MS1 + " ¿Para quién es el mensaje 1?", "la señora directora", "Lo dice la línea «Para»."),
        ex(MS2 + " ¿Para quién es el mensaje 2?", "el curso", "Lo dice la línea «Para»."),
        ex("Un mensaje, ¿es un texto breve que transmite algo a otra persona o un libro largo?", "un texto breve que transmite algo a otra persona", "Así se definió mensaje."),
    ],
    C=[
        ex(MS1 + " ¿Qué día es la minga?", "el viernes", "El mensaje lo dice."),
        ex(MS2 + " ¿Qué debe traer el curso, además de agua?", "una bolsa", "El mensaje 2 lo dice."),
        ex(GLO + " ¿«Chaltumay» quiere decir gracias o hola?", "gracias", "El glosario lo dice."),
    ],
    A=[
        ex(MS1 + " " + MS2 + " Une cada mensaje con su propósito: A) mensaje 1, B) mensaje 2. Propósitos: 1) avisar qué traer a una minga, 2) invitar a una persona a una minga. Escribe los dos pares.", "A-2, B-1", "El mensaje 1 invita a la directora y el 2 avisa al curso."),
        arith("El curso tiene 30 estudiantes. Si 24 llevan una bolsa a la minga, ¿cuántos no la llevan?", "30-24", "Se restan los que llevan del total."),
        ex("Ordena las decisiones antes de escribir: A) elijo las palabras significativas y su fuente. B) decido el destinatario. C) decido el propósito. Escribe las letras en orden.", "C, B, A", "Primero el propósito, luego el destinatario y después las palabras."),
    ],
    Z=[
        ex("Quieres invitar a un educador tradicional a enseñar un saludo al curso. ¿Qué situación es: natural, social o cultural?", "cultural", "Se trata de aprender un saludo de una lengua."),
        ex("Un niño firma un mensaje con el nombre de la profesora sin preguntarle. ¿Es correcto? Sí o No.", "No", "No se escribe en nombre de otra persona sin permiso."),
    ],
    D=[
        ex("Dos mensajes de invitación. El 1 incluye saludo, propósito, fecha y despedida. El 2 solo dice «vengan». ¿Cuál es más claro: 1 o 2?", "1", "El 1 da la información necesaria."),
        ex("Quieres incluir «mari mari» en un mensaje. ¿Qué haces antes: A) pedir que el educador o educadora tradicional te confirme cómo se usa o B) usarlo sin saber?", "A", "Se comprueba el uso con quien enseña."),
    ],
    context=[ex("Quieres escribir una nota para invitar a los vecinos a limpiar la orilla de un río. ¿Primero decides propósito y destinatario o primero escribes la despedida?", "primero decides propósito y destinatario", "Las decisiones van antes de escribir.")],
    selfcheck=[
        ex("¿Quién recibe el mensaje: el destinatario o el remitente?", "el destinatario", "El remitente es quien lo envía."),
        ex("¿Puedo escribir mi dirección en un mensaje? Sí o No.", "No", "No se ponen datos personales."),
        ex("¿Debo anotar quién me enseñó una palabra indígena que uso? Sí o No.", "Sí", "Siempre se nombra la fuente."),
    ],
    task=T(
        "Elige una de estas tres situaciones inventadas: A) invitar a la comunidad a limpiar un sendero junto a un río (medio natural); B) agradecer a un curso que ayudó en una minga (social); C) pedir a un educador tradicional que enseñe un saludo (cultural). En tu cuaderno escribe una ficha con cuatro líneas: propósito, destinatario, situación y palabra significativa con su fuente. Si no sabes un dato, escribe «por preguntar». Termina con una pregunta para el educador o educadora tradicional.",
        "Propósito: agradecer a un curso por ayudar en una minga. Destinatario: el 4.º básico. Situación: social. Palabra: «chaltumay», enseñada por la educadora tradicional. Pregunta: ¿puedo escribir «chaltumay» así en la tarjeta?",
        ["completa las cuatro líneas", "elige bien el tipo de situación", "nombra la fuente de la palabra", "formula una pregunta"],
        ["ficha de cuatro líneas", "pregunta"],
        ["inventar fuente", "olvidar el destinatario"],
        "Verifica que el tipo de situación corresponda a la opción elegida.",
    ),
    reinforce="Relee los mensajes 1 y 2 y subraya con un color el propósito y con otro el destinatario.",
    extend="Escribe una ficha de cuatro líneas para un mensaje que invite a cuidar un jardín del colegio, sin datos personales.",
)

# ============================================================ LS04 clase 2 · leer mensajes con límites
MS3 = "Mensaje 3 (inventado). «Chaltumay. Quiero decirle que ayer fue bonita la minga. Mari mari. El 5.º básico.»"
MS4 = "Mensaje 4 (inventado). Para: el educador tradicional de la escuela. «Mari mari, educador. El 5.º básico le pide que nos enseñe cómo se usa un saludo en nuestra comunidad. Podemos reunirnos el jueves después de la once. Muchas gracias por su ayuda. Atentamente, el 5.º básico.»"

L(
    LS4, 2,
    materials="Lápiz y hoja. Los mensajes están escritos aquí y son inventados para practicar.",
    use="Aprenderé a leer un mensaje y a reconocer sus partes (saludo, mensaje, despedida), si tiene palabras significativas bien usadas y qué le falta. Sirve para revisar los mensajes antes de enviarlos.",
    prior=["Sé decidir propósito, destinatario y situación.", "Sé el uso de «mari mari» y «chaltumay»."],
    explain=[
        "Un mensaje bien escrito tiene partes. Empieza con un saludo, que puede ser «mari mari» si corresponde, o «hola» o «buenos días». Sigue el cuerpo, donde digo lo que quiero: invito, aviso, agradezco o pido. Termina con una despedida y la firma de quien lo envía, que puede ser el curso. Si le falta una parte, hay que agregarla.",
        "El mensaje 4 tiene saludo («mari mari, educador»), cuerpo (pide que enseñe cómo se usa un saludo), fecha («el jueves después de la once») y despedida con agradecimiento. El mensaje 3 usa «chaltumay» al comienzo, pero esa palabra es para agradecer, no para saludar. Además no dice a quién va dirigido. Si leo un mensaje así, lo corrijo con respeto.",
        "También reviso los límites: el mensaje no debe tener datos personales ni hablar en nombre de otra persona. Y reviso la extensión: un mensaje breve tiene entre tres y seis oraciones. Un mensaje claro permite que quien lo lea sepa qué se pide y cuándo, sin tener que adivinar.",
    ],
    vocab=[("saludo", "primera parte del mensaje"), ("cuerpo", "parte donde digo lo que quiero"), ("despedida", "parte final del mensaje"), ("firma", "nombre de quien envía el mensaje"), ("clara", "que se entiende sin adivinar")],
    worked=[
        W("Reconocer las partes", MS4 + " ¿Cuál es el saludo del mensaje 4?", ["Leo el comienzo del mensaje.", "Dice: «Mari mari, educador».", "Ese es el saludo."], "«Mari mari, educador»"),
        W("Detectar el uso equivocado", MS3 + " ¿Qué error tiene el uso de «chaltumay» en el mensaje 3?", ["«Chaltumay» es una palabra para agradecer.", "En el mensaje 3 se usa como saludo al comienzo.", "El saludo correcto sería «mari mari»."], "se usa para saludar, pero «chaltumay» es para agradecer"),
    ],
    mistakes=[
        M("Usar «chaltumay» para saludar al comenzar el mensaje.", "Es una palabra para agradecer.", "Uso «mari mari» o «hola» para saludar y «chaltumay» para agradecer."),
        M("Enviar un mensaje sin saber a quién va dirigido.", "Nadie sabe para quién es.", "Escribo la línea «Para» con el destinatario."),
    ],
    R=[
        ex(MS4 + " ¿A quién escribe el 5.º básico?", "al educador tradicional de la escuela", "Lo dice la línea «Para»."),
        ex(MS4 + " ¿Qué día proponen reunirse?", "el jueves", "El mensaje lo dice."),
        ex(MS3 + " ¿Con qué palabra comienza el mensaje 3?", "chaltumay", "El mensaje 3 empieza con esa palabra."),
    ],
    C=[
        ex(MS4 + " ¿Qué piden en el mensaje 4?", "que enseñe cómo se usa un saludo en su comunidad", "El mensaje 4 lo dice."),
        ex(MS3 + " Verdadero o falso: el mensaje 3 dice a quién va dirigido.", "Falso", "No tiene línea «Para»."),
        ex(GLO + " ¿«Mari mari» es un saludo o una despedida?", "un saludo", "El glosario lo dice."),
    ],
    A=[
        ex("Ordena las partes del mensaje: A) despedida. B) cuerpo. C) saludo. Escribe las letras en orden.", "C, B, A", "Un mensaje empieza con saludo, sigue el cuerpo y termina con la despedida."),
        arith("El mensaje 4 tiene 5 oraciones. Se quiere que tenga como máximo 6. ¿Cuántas oraciones más se pueden agregar?", "6-5", "Se resta lo que tiene del máximo."),
        ex(MS4 + " ¿Qué palabras significativas usa el mensaje 4: «mari mari» y «once», o «minga» y «chaltumay»?", "«mari mari» y «once»", "El mensaje 4 usa esas dos."),
    ],
    Z=[
        ex(MS3 + " Un compañero lo corrige así: «Mari mari. Quiero decirle que ayer fue bonita la minga. Chaltumay. El 5.º básico». ¿Mejoró el uso de las palabras? Sí o No.", "Sí", "Ahora «mari mari» saluda y «chaltumay» agradece."),
        ex(MS3 + " Aun corregido, el mensaje 3 no dice a quién va. ¿Qué falta: el destinatario o la firma?", "el destinatario", "La firma ya está: el 5.º básico."),
    ],
    D=[
        ex(MS4 + " Elige el cambio que NO conviene: A) agregar su dirección. B) agregar la hora de la reunión. C) agregar una despedida. Escribe la letra.", "A", "No se ponen datos personales."),
        ex(MS2 + " ¿Qué dato falta en el mensaje 2: el destinatario o la hora de la minga?", "la hora de la minga", "El destinatario está en la línea «Para»; la hora no se indica."),
    ],
    context=[ex("Un compañero te muestra un mensaje que tiene «chaltumay» al comienzo para saludar. ¿Le dices con respeto que esa palabra es para agradecer o lo dejas así?", "le dices con respeto que esa palabra es para agradecer", "Se corrige con respeto según la fuente.")],
    selfcheck=[
        ex("¿Qué parte del mensaje dice lo que quiero: el cuerpo o la firma?", "el cuerpo", "En el cuerpo digo lo que quiero."),
        ex("¿Debo revisar que no tenga datos personales? Sí o No.", "Sí", "Los mensajes no llevan datos personales."),
        ex("¿Un mensaje breve puede tener entre tres y seis oraciones? Sí o No.", "Sí", "Así se explicó en la clase."),
    ],
    task=T(
        "Lee este mensaje inventado: «Mari mari. Quiero decirles que el sábado habrá una minga en la plaza. Traigan guantes. Chaltumay.» En tu cuaderno escribe: 1) las partes que tiene, 2) las partes que le faltan, 3) una versión corregida que tenga destinatario («Para: las familias del curso»), saludo, cuerpo con la hora (las diez de la mañana), despedida y firma. Usa «mari mari» y «chaltumay» en su lugar. Termina con una pregunta para el educador o educadora tradicional.",
        "Tiene saludo, cuerpo y agradecimiento. Le faltan destinatario, hora y firma. Versión corregida: Para: las familias del curso. Mari mari. El sábado a las diez de la mañana habrá una minga en la plaza. Traigan guantes. Chaltumay por su ayuda. El 5.º básico. Pregunta: ¿está bien usado el saludo en este mensaje?",
        ["reconoce partes y faltantes", "corrige usando cada palabra en su lugar", "agrega destinatario, hora y firma", "formula una pregunta"],
        ["análisis y versión corregida", "pregunta"],
        ["usar chaltumay para saludar", "agregar datos personales"],
        "Revisa que cada palabra aparezca en el lugar correcto del mensaje.",
    ),
    reinforce="Relee el mensaje 4 y subraya con colores el saludo, el cuerpo y la despedida.",
    extend="Escribe un mensaje de cuatro oraciones para agradecer a un curso que ayudó en una minga, sin datos personales.",
)

# ============================================================ LS04 clase 3 · relaciones culturales: tono y situación
REG = "Ficha de tono (de práctica): Para una persona adulta o una autoridad, en Chile se usa un trato respetuoso, con «usted» o «señora/señor», como en «le pedimos que nos enseñe». Para compañeros de curso se puede usar un trato cercano, con «tú» o «ustedes», como en «les contamos que habrá una minga». En ambos casos se usan palabras amables como «por favor» y «gracias»."

L(
    LS4, 3,
    materials="Lápiz y hoja. La ficha está escrita aquí y es de práctica. No necesitas dispositivos.",
    use="Aprenderé a elegir el tono y las palabras significativas según la persona que recibirá el mensaje y la situación (natural, social o cultural). Sirve para escribir mensajes adecuados a cada caso.",
    prior=["Sé las partes de un mensaje.", "Sé usar «mari mari» y «chaltumay» en su situación."],
    explain=[
        "No escribo igual a una autoridad que a un compañero. A una persona adulta o a una autoridad le escribo con un trato respetuoso, con «usted» o «señora» y «señor». A un compañero le puedo escribir con un trato cercano, con «tú» o «ustedes». En los dos casos soy amable: uso «por favor» y «gracias».",
        "La situación también orienta mis palabras. En una situación del medio natural, como cuidar un río, puedo usar palabras que nombran la acción, como «minga». En una situación social, como invitar a un curso, uso un lenguaje claro y alegre. En una situación cultural, como pedir a un educador tradicional que enseñe un saludo, uso un trato muy respetuoso y pido, no exijo.",
        "Las palabras significativas ayudan a expresar respeto y reconocimiento. Un saludo como «mari mari» al comenzar un mensaje a un educador tradicional muestra respeto por la lengua, si lo usé como me lo enseñaron. Pero no lleno el mensaje de palabras que no conozco. Prefiero pocas palabras y bien usadas, y siempre consulto antes de enviar.",
    ],
    vocab=[("tono", "manera de hablar o escribir según la persona y la situación"), ("trato respetuoso", "forma de hablar con «usted» o «señora/señor»"), ("trato cercano", "forma de hablar con «tú» o «ustedes»"), ("autoridad", "persona que dirige o tiene un cargo"), ("amable", "que trata bien a los demás")],
    worked=[
        W("Elegir el trato", REG + " Escribes a la directora. ¿Qué trato usas?", ["La directora es una autoridad adulta.", "Para ella uso un trato respetuoso.", "Escribo «le pedimos» en vez de «te pedimos»."], "trato respetuoso, con «usted»"),
        W("Elegir la palabra según la situación", "Quieres pedir a un educador tradicional que te enseñe un saludo. ¿Qué situación es y qué tono usas?", ["Se trata de aprender una palabra de una lengua: situación cultural.", "El educador es una persona adulta.", "Uso un trato muy respetuoso y pido, no exijo."], "cultural, con trato muy respetuoso"),
    ],
    mistakes=[
        M("Escribir a una autoridad con un tono demasiado informal.", "No muestra respeto.", "Uso «usted» y palabras amables."),
        M("Exigir en vez de pedir cuando escribo a un educador tradicional.", "No es una forma respetuosa de pedir a quien enseña.", "Digo «le pedimos» o «nos gustaría»."),
    ],
    R=[
        ex(REG + " ¿Qué trato se usa para una persona adulta?", "respetuoso, con «usted»", "La ficha lo dice."),
        ex(REG + " ¿Qué trato se puede usar para compañeros de curso?", "cercano, con «tú» o «ustedes»", "La ficha lo dice."),
        ex(REG + " ¿Qué palabras amables menciona la ficha?", "«por favor» y «gracias»", "La ficha las nombra."),
    ],
    C=[
        ex("Clasifica con R (trato respetuoso) o C (trato cercano): 1) «le pedimos que nos enseñe». 2) «les contamos que habrá una minga». 3) «señora directora, queremos invitarla». Escribe las tres letras.", "1 R, 2 C, 3 R", "«Le», «señora» y «invitarla» van con trato respetuoso."),
        ex("Verdadero o falso: a un educador tradicional le escribo con tono muy respetuoso.", "Verdadero", "Se pide con respeto a quien enseña."),
        ex("Pedir, ¿es decir con amabilidad lo que necesito o exigirlo?", "decir con amabilidad lo que necesito", "En el mensaje se pide, no se exige."),
    ],
    A=[
        ex(REG + " Une cada mensaje con su trato: A) a la directora, B) a los compañeros de curso. Tratos: 1) cercano, 2) respetuoso. Escribe los dos pares.", "A-2, B-1", "La directora es una autoridad adulta y los compañeros reciben un trato cercano."),
        arith("Un curso escribe 5 mensajes a autoridades y 8 a compañeros. ¿Cuántos mensajes escribe en total?", "5+8", "Se suman las dos clases de mensajes."),
        ex("Elige la mejor forma de pedir ayuda a una autoridad: A) «Le pedimos, por favor, que nos ayude con la minga». B) «Ayúdanos con la minga ahora». Escribe la letra.", "A", "A usa trato respetuoso y pide."),
    ],
    Z=[
        ex("Una niña quiere comenzar con «mari mari» un mensaje a un educador tradicional, pero no sabe si lo escribe bien. ¿Qué es mejor: A) consultar al educador o educadora tradicional o B) enviar igual?", "A", "Se confirma con quien enseña."),
        ex("Un niño escribe a sus compañeros con «usted». ¿Es un error grave? Sí o No.", "No", "Puede sonar muy formal, pero no falta el respeto."),
    ],
    D=[
        ex("Dos mensajes a una autoridad. El 1 dice «Mari mari, señora. Le pedimos, por favor, que nos autorice a hacer una minga». El 2 dice «Autorícenos la minga». ¿Cuál es más adecuado: 1 o 2?", "1", "El 1 usa trato respetuoso y pide con amabilidad."),
        ex("Quieres agradecer a un curso que ayudó en una minga. ¿Qué tono es adecuado: cercano o muy formal?", "cercano", "Se agradece a compañeros con trato cercano."),
    ],
    context=[ex("Vas a escribir una nota a un vecino mayor para invitarlo a la feria del curso. ¿Usas «usted» y palabras amables o lo tuteas sin saludar?", "usas «usted» y palabras amables", "A una persona mayor se le escribe con respeto.")],
    selfcheck=[
        ex("A una autoridad, ¿le escribo con trato respetuoso o cercano?", "respetuoso", "Es una persona adulta con un cargo."),
        ex("¿Debo usar muchas palabras que no conozco para que el mensaje se vea cultural? Sí o No.", "No", "Prefiero pocas y bien usadas."),
        ex("Pedir algo con amabilidad, ¿es lo mismo que exigirlo? Sí o No.", "No", "Pedir es respetuoso."),
    ],
    task=T(
        "Escribe dos mensajes de práctica en tu cuaderno sobre la misma minga para limpiar una orilla de río: uno para la directora (con trato respetuoso) y otro para tus compañeros de curso (con trato cercano). Cada mensaje debe tener saludo, cuerpo con fecha y hora inventadas, despedida y firma. Usa «mari mari» y «chaltumay» donde corresponda y la palabra «minga» al menos una vez. Termina con una pregunta para el educador o educadora tradicional.",
        "A la directora: Para: la señora directora. Mari mari, señora directora. Le pedimos que autorice una minga para limpiar la orilla del río el sábado a las diez. Chaltumay por su tiempo. El 5.º básico. A los compañeros: Para: el curso. Hola. Les contamos que el sábado a las diez habrá una minga en el río. Traigan guantes. Gracias. El comité. Pregunta: ¿qué otros saludos se pueden usar en un mensaje?",
        ["usa trato respetuoso y cercano según el caso", "incluye las cuatro partes del mensaje", "usa las palabras en su situación", "formula una pregunta"],
        ["dos mensajes escritos", "pregunta"],
        ["usar el mismo tono en ambos", "usar chaltumay para saludar"],
        "Compara los dos mensajes y pregunta qué cambió entre uno y otro.",
    ),
    reinforce="Copia la ficha de tono y subraya con un color las palabras del trato respetuoso y con otro las del trato cercano.",
    extend="Escribe el mismo aviso de una feria en dos tonos y explica por qué cambia cada uno.",
)

# ============================================================ LS04 clase 4 · mensaje final atribuido
CRED4 = "Ficha de créditos del mensaje (inventada): Remitente: el 5.º básico de la Escuela Ejemplo. Destinatario: el educador tradicional de la escuela. Propósito: pedirle que enseñe cómo se usa el saludo «mari mari» en la comunidad. Palabras significativas: «mari mari» (saludo en mapuzugun, enseñado por el educador) y «once» (castellano de Chile). Revisión: el educador revisará el mensaje antes de enviarlo. Datos personales: ninguno."

L(
    LS4, 4,
    materials="Lápiz y hoja. La ficha está escrita aquí y es inventada para practicar. Puedes escribir todo en papel.",
    use="Aprenderé a escribir un mensaje completo con sus créditos: quién lo envía, a quién va, qué palabras significativas usa y de quién son, y quién lo revisa. Sirve para enviar mensajes claros, atribuidos y respetuosos.",
    prior=["Sé las partes de un mensaje y el tono adecuado.", "Sé que cada palabra indígena lleva su fuente."],
    explain=[
        "Un mensaje final tiene dos cosas: el texto del mensaje y una ficha de créditos. El texto lleva destinatario, saludo, cuerpo, despedida y firma. La ficha de créditos dice quién lo envía, a quién va, para qué, qué palabras significativas usa y de quién son, quién lo revisa y que no contiene datos personales.",
        "Cuando uso una palabra de una lengua indígena, anoto su fuente en los créditos y la copio tal cual. Cuando uso una palabra del castellano de Chile con valor cultural, como «minga», también explico qué significa. Si el mensaje trata de algo que es de una comunidad, pido que alguien de la comunidad o el educador tradicional lo revise antes de enviarlo.",
        "Revisar es leer de nuevo con una lista: ¿está el destinatario?, ¿el saludo y la despedida?, ¿el tono es el adecuado?, ¿cada palabra significativa está en su lugar y con su fuente?, ¿no hay datos personales?, ¿lo revisó quien corresponde? Si respondo sí a todas, el mensaje está listo.",
    ],
    vocab=[("créditos", "ficha con remitente, destinatario, propósito, palabras y revisión"), ("revisión", "lectura de quien corresponde antes de enviar"), ("fuente", "persona que enseñó una palabra"), ("lista de revisión", "preguntas para comprobar que el mensaje está completo"), ("enviar", "hacer llegar el mensaje al destinatario")],
    worked=[
        W("Leer los créditos", CRED4 + " ¿Quién enseñó el saludo «mari mari»?", ["Busco las palabras significativas.", "Dice: enseñado por el educador.", "Ese es la fuente."], "el educador tradicional de la escuela"),
        W("Detectar un crédito faltante", "Créditos incompletos (inventados): Remitente: el curso. Destinatario: la directora. Propósito: invitar a una minga. Datos personales: ninguno. ¿Qué dos datos faltan?", ["Los créditos tienen seis datos: remitente, destinatario, propósito, palabras con su fuente, revisión y datos personales.", "Aparecen remitente, destinatario, propósito y datos personales.", "Faltan las palabras con su fuente y la revisión."], "faltan las palabras significativas con su fuente y la revisión"),
    ],
    mistakes=[
        M("Enviar el mensaje sin que lo revise el educador o educadora tradicional cuando usa palabras de la lengua.", "Puede haber errores de uso.", "Pido la revisión antes de enviar."),
        M("Poner datos personales en los créditos.", "Expongo a personas.", "Uso el nombre del curso o el cargo."),
    ],
    R=[
        ex(CRED4 + " ¿Quién es el remitente?", "el 5.º básico de la Escuela Ejemplo", "Lo dice la línea «Remitente»."),
        ex(CRED4 + " ¿Quién es el destinatario?", "el educador tradicional de la escuela", "Lo dice la línea «Destinatario»."),
        ex(CRED4 + " ¿Qué propósito tiene el mensaje?", "pedirle que enseñe cómo se usa el saludo «mari mari» en la comunidad", "Lo dice la línea «Propósito»."),
    ],
    C=[
        ex(CRED4 + " ¿Quién revisará el mensaje antes de enviarlo?", "el educador", "Lo dice la línea «Revisión»."),
        ex(CRED4 + " Verdadero o falso: los créditos incluyen datos personales.", "Falso", "Dicen «Datos personales: ninguno»."),
        ex("Los créditos, ¿son una ficha con remitente, destinatario y fuentes o la parte que dice lo que quiero?", "una ficha con remitente, destinatario y fuentes", "El cuerpo es la parte que dice lo que quiero."),
    ],
    A=[
        ex("Ordena el trabajo final: A) pido la revisión. B) escribo el mensaje. C) completo los créditos. D) envío. Escribe las letras en orden.", "B, C, A, D", "Escribo, completo créditos, pido revisión y envío."),
        arith("Una lista de revisión tiene 6 preguntas y un mensaje responde sí a 4. ¿Cuántas faltan por cumplir?", "6-4", "Se restan las cumplidas del total."),
        ex(CRED4 + " ¿Cuál de estas palabras es del castellano de Chile: «mari mari» o «once»?", "«once»", "Los créditos lo indican."),
    ],
    Z=[
        ex("Un niño dice: «Mi mensaje está tan bonito que no necesita créditos». ¿Es correcto? Sí o No.", "No", "Los créditos permiten comprobar fuentes y permisos."),
        ex("Una niña usa «chaltumay» en su mensaje y no anota la fuente. ¿Qué debe hacer antes de enviar: A) agregar la fuente en los créditos o B) borrar los créditos?", "A", "Cada palabra indígena lleva su fuente."),
    ],
    D=[
        ex("Dos mensajes. El 1 tiene créditos completos y fue revisado. El 2 no tiene créditos ni revisión. ¿Cuál puede enviarse: 1 o 2?", "1", "El 2 no cumple las reglas."),
        ex("Un mensaje a un vecino mayor usa trato cercano y no tiene firma. ¿Qué dos mejoras hacen falta: trato respetuoso y firma, o cambiar el destinatario?", "trato respetuoso y firma", "A una persona mayor se le escribe con respeto y se firma."),
    ],
    context=[ex("Escribiste una nota para agradecer a un grupo que ayudó en una minga. Antes de enviarla, ¿la revisas con la lista y anotas las fuentes o la envías de inmediato?", "la revisas con la lista y anotas las fuentes", "Revisar y atribuir va antes de enviar.")],
    selfcheck=[
        ex("¿Los créditos dicen quién es el remitente? Sí o No.", "Sí", "Es uno de sus datos."),
        ex("Si uso una palabra indígena, ¿anoto quién me la enseñó? Sí o No.", "Sí", "Siempre se anota la fuente."),
        ex("¿Debo poner mi dirección en los créditos? Sí o No.", "No", "No se ponen datos personales."),
    ],
    task=T(
        "Escribe un mensaje final de práctica. Situación inventada: el 5.º básico de la Escuela Muestra quiere agradecer a un curso de 4.º básico que ayudó a ordenar la biblioteca y quiere invitarlo a una once el viernes a las cuatro. En tu cuaderno escribe: 1) el mensaje con destinatario, saludo, cuerpo, despedida y firma, usando «chaltumay» y «once» en su lugar; 2) la ficha de créditos con remitente, destinatario, propósito, palabras con su fuente, revisión y datos personales. Si no sabes un dato, escribe «por preguntar». Termina con una pregunta para el educador o educadora tradicional.",
        "Mensaje: Para: el 4.º básico. Hola, 4.º básico. Queremos darles las gracias por ayudarnos a ordenar la biblioteca. Chaltumay. Los invitamos a una once el viernes a las cuatro. Un saludo, el 5.º básico. Créditos: Remitente: 5.º básico de la Escuela Muestra. Destinatario: 4.º básico. Propósito: agradecer e invitar. Palabras: «chaltumay» (gracias en mapuzugun, enseñada por el educador tradicional) y «once» (castellano de Chile). Revisión: por preguntar. Datos personales: ninguno. Pregunta: ¿puede revisar el mensaje antes de que lo enviemos?",
        ["mensaje con las cinco partes", "créditos completos", "palabras en su lugar con fuente", "formula una pregunta"],
        ["mensaje y ficha de créditos", "pregunta"],
        ["omitir créditos", "no anotar la fuente"],
        "Revisa dato por dato los créditos y pide que corrija solo lo que falte.",
    ),
    reinforce="Copia la ficha de créditos de esta clase y numera cada uno de sus seis datos.",
    extend="Escribe los seis datos de créditos para un mensaje que invite a la comunidad a cuidar una orilla de río, con una palabra significativa y su fuente.",
)
