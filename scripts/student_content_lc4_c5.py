"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS06 (registro con recursos tecnológicos de experiencias cotidianas y significativas de la vida familiar y
comunitaria, incorporando algunas palabras culturalmente significativas, desde el castellano y el contexto comunitario).

Criterio de autoría: todas las fichas, registros, escuelas y personas son inventados solo para practicar y están
rotulados como tales. El registro se escribe sobre todo en castellano y las únicas palabras en lengua indígena son
saludos y palabras muy atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke); no se inventa gramática,
pronunciación ni significados rituales. Los recursos tecnológicos se describen sin marcas ni enlaces y siempre con un
adulto; en toda actividad hay alternativa sin tecnología. No se piden datos personales ni de la familia: se habla de
«una persona de tu casa». Cada tarea abierta remite al educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS6 = "LC04 OA LS06"

CONSULT = " Recuerda: la forma tradicional de escribir, decir y usar estas palabras la enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de escritura, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

FICHA_SAL = "Ficha: «mari mari» es un saludo y «chaltumay» quiere decir «gracias», ambas en mapuzugun."
FICHA_PAL = "Ficha de palabras en mapuzugun (de práctica): «ko» es agua, «antü» es sol, «kuyen» es luna, «ruka» es la casa mapuche, «mapu» es tierra, «ñuke» es madre."


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


# =================================================================== LS06 clase 1 · propósito, fuente y autorización
FICHA_HUERTO = "Ficha de registro H (inventada para practicar): Experiencia: el curso de la Escuela Ejemplo planta lechugas en el huerto de la escuela. Para qué: contar a las familias cómo se cuida una planta. Idioma del registro: castellano, con las palabras «ko» (agua) y «mapu» (tierra), enseñadas por la educadora tradicional de la escuela. Autorización de las personas que aparecen: no aparecen rostros. Autorización de la educadora para las palabras: sí, para la reunión de familias."

L(
    LS6, 1,
    materials="Lápiz y hoja. Las fichas están escritas aquí; son inventadas para practicar. Si usas un dispositivo, hazlo siempre con una persona adulta; también puedes hacer todo en papel.",
    use="Aprenderé a decidir, antes de registrar una experiencia de mi vida diaria con un recurso tecnológico, para qué la registro, en qué idioma, de quién son las palabras que incluiré y quién autoriza. Sirve para contar mis experiencias sin faltar el respeto a nadie.",
    prior=["Sé que registrar es dejar guardada una experiencia.", "Sé que las palabras de la lengua indígena las enseña el educador o la educadora tradicional."],
    explain=[
        "Una experiencia cotidiana es algo que vivo en mi día a día, como cuidar una planta, preparar la sala para una visita o ayudar en una actividad del curso. Una experiencia significativa es la que me importa o enseña algo. Puedo contarla y registrarla con un recurso tecnológico: un texto escrito en el computador, una grabación de audio o una foto sin rostros.",
        "Mi registro puede estar escrito en castellano, que es la lengua que uso para contar, e incluir algunas palabras significativas de la lengua indígena. Esas palabras vienen de una fuente que las enseñó y autorizó. Antes de empezar decido: ¿qué experiencia cuento?, ¿para qué?, ¿en qué idioma?, ¿quién enseñó las palabras?, ¿quién autoriza?",
        "En mi registro hablo de lo que hice yo y de lo que pasó en la sala. No cuento cosas privadas de una persona de mi casa ni de otra familia. Si quiero incluir una voz o una imagen de alguien, le pido permiso. Si falta una respuesta de la ficha, me detengo y pregunto antes de registrar.",
    ],
    vocab=[("experiencia cotidiana", "algo que vivo en mi día a día"), ("experiencia significativa", "algo que me importa o me enseña"), ("recurso tecnológico", "aparato o programa que sirve para registrar"), ("registrar", "dejar guardado un hecho"), ("autorización", "el sí de las personas para registrar o usar algo")],
    worked=[
        W("Leer la ficha", FICHA_HUERTO + " ¿En qué idioma está el registro?", ["Busco la línea «Idioma del registro».", "Dice: castellano, con las palabras «ko» y «mapu».", "El idioma principal es el castellano."], "castellano, con dos palabras de la lengua indígena"),
        W("Detenerse si falta un dato", "Ficha I (inventada): Experiencia: un paseo del curso. Para qué: no se indica. Idioma: castellano. Palabras en lengua indígena: «antü», sin fuente. Autorización: no se indica. ¿Se puede empezar a registrar?", ["Reviso los datos de la ficha.", "Faltan el propósito, la fuente y la autorización.", "Me detengo y pregunto antes de registrar."], "no: faltan el propósito, la fuente y la autorización"),
    ],
    mistakes=[
        M("Registrar una conversación privada de una persona de mi casa porque me pareció interesante.", "Es un asunto privado que no me corresponde compartir.", "Registro solo lo que yo hice y lo que pasó en la sala."),
        M("Poner muchas palabras en lengua indígena para que el registro «se vea» cultural.", "Solo puedo usar las que enseñó y autorizó la fuente.", "Uso pocas palabras, bien elegidas y con su fuente."),
    ],
    R=[
        ex(FICHA_HUERTO + " ¿Qué planta plantan los niños en el huerto?", "lechugas", "La ficha lo dice en la línea «Experiencia»."),
        ex(FICHA_HUERTO + " ¿Para qué se registra esta experiencia?", "para contar a las familias cómo se cuida una planta", "Es el propósito de la ficha."),
        ex("Una experiencia cotidiana, ¿es algo que vivo en mi día a día o algo que nunca viví?", "algo que vivo en mi día a día", "Cotidiana quiere decir de todos los días."),
    ],
    C=[
        ex(FICHA_HUERTO + " ¿Qué dos palabras de la lengua indígena lleva el registro?", "ko y mapu", "La ficha las nombra."),
        ex("Verdadero o falso: puedo registrar una conversación privada de una persona de mi casa.", "Falso", "Es un asunto privado."),
        ex(FICHA_HUERTO + " Según la ficha, ¿aparecen rostros en el registro? Sí o No.", "No", "La ficha dice que no aparecen rostros."),
    ],
    A=[
        ex("Cinco preguntas antes de registrar: qué, para qué, en qué idioma, quién enseñó las palabras y quién autoriza. La ficha I responde solo la primera y la tercera. ¿Cuántas preguntas faltan?", "3", "5 − 2 = 3."),
        ex(FICHA_HUERTO + " La educadora autorizó las palabras «para la reunión de familias». ¿Puede el curso mostrar el registro a otro colegio? Sí o No.", "No", "El permiso es solo para la reunión de familias."),
        ex("Tres experiencias: A) cómo cuidamos una planta en el huerto. B) una pelea privada entre dos familias. C) cómo preparamos la sala para una visita. ¿Cuáles son adecuadas para registrar? Escribe las letras.", "A y C", "B es un asunto privado."),
    ],
    Z=[
        ex("Una niña dice: «Si registro en castellano, no necesito decir de dónde vienen las palabras indígenas que usaré». ¿Tiene razón? Sí o No.", "No", "Las palabras de la lengua siempre llevan su fuente."),
        ex("Un niño quiere agregar una foto de un compañero regando la planta. ¿Qué es mejor: A) preguntar a él y a su familia y, si no quieren, usar una foto de las manos o la planta. B) subirla igual?", "A", "Sin autorización no aparece su rostro."),
    ],
    D=[
        ex("Ordena antes de registrar: A) decido el propósito. B) pido autorización. C) anoto la fuente de las palabras. D) registro. Escribe las letras en orden.", "A, C, B, D", "Primero propósito y fuente, luego autorización y al final registro."),
        arith("De 24 estudiantes del curso, 6 no quieren aparecer en el registro. ¿Cuántos pueden aparecer si todos los demás autorizan?", "24-6", "Se restan los que no quieren aparecer."),
    ],
    context=[ex("Quieres contar con un audio cómo cuidas una planta en casa y mencionar la palabra «ko». ¿Dices de dónde viene la palabra o la usas sin decir?", "dices de dónde viene la palabra", "La fuente se nombra siempre.")],
    selfcheck=[
        ex("¿Qué decido primero: el propósito o el almacenamiento?", "el propósito", "Antes de registrar defino para qué."),
        ex("Si falta la fuente de una palabra, ¿sigo adelante o me detengo y pregunto?", "me detengo y pregunto", "Sin fuente no sé si es correcta."),
        ex("¿Puedo contar cosas privadas de una persona de mi casa en el registro? Sí o No.", "No", "Son asuntos privados."),
    ],
    task=T(
        "Lee esta situación inventada para practicar: «Un curso quiere registrar con un computador, y con un adulto, un texto breve en castellano que cuente cómo cuidan un huerto en la escuela. Quieren incluir las palabras «ko» y «mapu».» " + FICHA_PAL + " En tu cuaderno completa una ficha de registro con cinco líneas: qué se registra, para qué, idioma, quién enseñó las palabras y quién autoriza. Si no sabes un dato, escribe «por preguntar». Termina con una pregunta para el educador o la educadora tradicional.",
        "Qué: cómo cuidamos el huerto. Para qué: contar a las familias. Idioma: castellano con «ko» y «mapu». Palabras enseñadas por: la educadora tradicional. Autoriza: por preguntar. Pregunta: ¿podemos guardar este registro para la próxima reunión?",
        ["completa las cinco líneas", "nombra la fuente de las palabras", "escribe «por preguntar» donde no sabe", "formula una pregunta para el educador/a tradicional"],
        ["ficha de registro de cinco líneas", "pregunta escrita o dicha en voz alta"],
        ["inventar la autorización", "no anotar la fuente"],
        "Comprueba que las cinco líneas sean reales; si inventó una autorización, pídele que escriba «por preguntar».",
    ),
    reinforce="Vuelve a leer la ficha H y señala con el dedo la línea del propósito, la del idioma y la de la autorización.",
    extend="Escribe una ficha de registro de cinco líneas para otra actividad de tu sala.",
)

# =================================================================== LS06 clase 2 · elegir un medio accesible y seguro
TABLA = "Tabla de medios (inventada para practicar). Medio A, texto escrito a mano: sin internet sí, sin cuenta sí, sin rostros sí, todos pueden participar sí. Medio B, audio con grabadora del colegio: sin internet sí, sin cuenta sí, sin rostros sí, todos pueden participar no (hay quien prefiere no hablar). Medio C, video en un sitio abierto: sin internet no, sin cuenta no, sin rostros no, todos pueden participar no. Medio D, dibujo con rótulos: sin internet sí, sin cuenta sí, sin rostros sí, todos pueden participar sí."

L(
    LS6, 2,
    materials="Lápiz y hoja. La tabla está escrita aquí; es inventada para practicar. No necesitas ningún dispositivo.",
    use="Aprenderé a comparar medios para registrar una experiencia con cuatro criterios (sin internet, sin cuenta, sin rostros y que todos puedan participar) y a elegir el más accesible y seguro. Sirve para registrar sin gastar de más ni exponer a nadie.",
    prior=["Sé que antes de registrar defino propósito, fuente y autorización.", "Sé que hay medios analógicos, sin tecnología."],
    explain=[
        "Para elegir un medio de registro comparo con criterios. Cuatro criterios útiles son: que funcione sin internet, que no pida crear una cuenta, que no muestre rostros y que todos puedan participar. Cada vez que un medio cumple un criterio, le doy un punto. El que suma más puntos es el más accesible y seguro.",
        "Accesible significa que todos pueden usarlo: quien no tiene internet, quien prefiere no hablar, quien tiene dificultad para escribir. Seguro significa que no expone datos ni imágenes de personas. Un texto escrito a mano o un dibujo con rótulos suelen cumplir los cuatro, aunque tienen sus propios límites: por ejemplo, un dibujo no guarda una voz.",
        "También pienso en el propósito. Si quiero guardar una voz autorizada, un audio con permiso puede servir, aunque cumpla menos criterios. Lo importante es elegir con razones y tener siempre una alternativa analógica. Registrar bien no exige tecnología nueva ni gastar dinero, sino cuidar a las personas y a las palabras.",
    ],
    vocab=[("criterio", "regla para comparar y decidir"), ("accesible", "que todos pueden usar"), ("seguro", "que no expone a las personas"), ("analógico", "sin tecnología digital"), ("participar", "tomar parte en una actividad")],
    worked=[
        W("Sumar puntos", TABLA + " ¿Cuántos puntos suma el medio B?", ["Cuento los «sí» del medio B.", "Sin internet sí, sin cuenta sí, sin rostros sí.", "Todos pueden participar: no."], "3"),
        W("Elegir el mejor", TABLA + " ¿Qué medios suman los cuatro puntos?", ["Cuento los puntos de cada medio.", "A tiene 4, B tiene 3, C tiene 0 y D tiene 4.", "Suman cuatro A y D."], "A y D"),
    ],
    mistakes=[
        M("Elegir el medio más moderno sin comparar criterios.", "Puede pedir cuenta, internet o mostrar rostros.", "Comparo con los cuatro criterios antes de elegir."),
        M("Pensar que un medio sin tecnología no sirve para registrar.", "Un texto o un dibujo guardan bien una experiencia.", "Elijo el medio que cumple más criterios y sirve al propósito."),
    ],
    R=[
        ex(TABLA + " ¿El medio A funciona sin internet? Sí o No.", "Sí", "La tabla dice sin internet sí."),
        ex(TABLA + " ¿Qué medio es el video en un sitio abierto: A, B, C o D?", "C", "Es el medio C."),
        ex("Un criterio es una regla para comparar y decidir. ¿Cuántos criterios usa esta tabla?", "4", "Se cuentan cuatro criterios."),
    ],
    C=[
        ex(TABLA + " ¿Cuál medio muestra rostros: B o C?", "C", "La tabla dice sin rostros no en el medio C."),
        ex("Verdadero o falso: un medio que pide crear una cuenta cumple el criterio «sin cuenta».", "Falso", "Si pide cuenta, no cumple ese criterio."),
        ex(TABLA + " ¿Cuántos puntos suma el medio C?", "0", "No cumple ningún criterio."),
    ],
    A=[
        ex(TABLA + " ¿Cuántos puntos suma el medio D, el dibujo con rótulos?", "4", "Cumple los cuatro criterios."),
        ex(TABLA + " Propósito: guardar una voz autorizada de una visita. ¿Qué medio permite guardar una voz: A, B o D?", "B", "El audio guarda la voz."),
        ex(TABLA + " Un curso sin internet y que quiere que todos participen. ¿Cuál no sirve: el medio C o el medio A?", "el medio C", "C necesita internet y no deja participar a todos."),
    ],
    Z=[
        ex("Una niña dice: «El medio con más puntos es siempre el mejor para cualquier propósito». ¿Tiene razón? Sí o No.", "No", "Hay que mirar también el propósito."),
        ex("Dos razones para elegir el medio D: A) cumple los cuatro criterios y sirve para contar el huerto. B) se ve moderno. ¿Cuál es una buena razón?", "A", "La B no se apoya en criterios."),
    ],
    D=[
        arith("Una tabla compara 4 medios y cada uno puede sumar hasta 4 puntos. ¿Cuántos puntos posibles hay entre todos los medios?", "4*4", "Se multiplican los medios por los puntos que cada uno puede sumar."),
        ex("Ordena para elegir un medio: A) elijo el que suma más y sirve al propósito. B) sumo los puntos de cada medio. C) reviso los cuatro criterios. Escribe las letras.", "C, B, A", "Criterios, puntos y elección."),
    ],
    context=[ex("Tu curso no tiene internet en la sala y quiere registrar el huerto. ¿Eligen el texto escrito a mano o el video en un sitio abierto?", "el texto escrito a mano", "Funciona sin internet y sin cuenta.")],
    selfcheck=[
        ex("¿Cuántos criterios compara la tabla: sin internet, sin cuenta, sin rostros y que todos participen?", "4", "Se cuentan cuatro criterios."),
        ex("Si no hay internet, ¿qué uso: un medio analógico o ninguno?", "un medio analógico", "Siempre hay una alternativa."),
        ex("¿Debo crear una cuenta con mis datos para registrar un trabajo del curso? Sí o No.", "No", "No se entregan datos sin necesidad."),
    ],
    task=T(
        "Lee esta tabla inventada para practicar. " + TABLA + " En tu cuaderno copia la tabla en formato de cuatro filas y cuatro columnas de criterios, y suma los puntos de cada medio. Escribe qué medio elegirías para registrar el huerto de la escuela con una visita que no quiere aparecer, y por qué. Termina con una pregunta para el educador o la educadora tradicional.",
        "A suma 4, B suma 3, C suma 0 y D suma 4. Elijo D, el dibujo con rótulos, porque suma 4, no muestra rostros y todos pueden participar. Pregunta: ¿qué palabras puedo rotular en el dibujo?",
        ["suma correctamente los puntos", "elige un medio que no muestre rostros", "justifica con los criterios", "formula una pregunta para el educador/a tradicional"],
        ["tabla con puntos", "elección y pregunta escritas"],
        ["elegir el video en sitio abierto", "no justificar"],
        "Comprueba la suma y que la elección cuide a la visita; si eligió el video, conversa por qué no cumple los criterios.",
    ),
    reinforce="Cuenta los «sí» de cada medio en la tabla y escribe el total al lado.",
    extend="Agrega un medio nuevo a la tabla (por ejemplo, una foto de las manos) y decide cuántos puntos suma.",
)

# =================================================================== LS06 clase 3 · registrar sin exponer datos ni saberes restringidos
BORRADOR_3 = "Borrador de práctica (inventado): «Hoy, en el patio de la casa de mi vecina Rosa Díaz, en Calle Los Olmos 45, aprendimos cómo se cuida el agua (ko). La abuela nos contó una historia que dijo que es solo para la familia. Grabamos con el celular de Rosa, con la ubicación activada.»"

L(
    LS6, 3,
    materials="Lápiz y un lápiz de otro color para marcar. El borrador está escrito aquí; es inventado para practicar.",
    use="Aprenderé a detectar en un borrador los datos que expondrían a una persona y los saberes que no se deben registrar, y a corregirlos. Sirve para contar mis experiencias cuidando a las personas y lo que su comunidad resguarda.",
    prior=["Sé qué es un dato personal y qué es un saber restringido.", "Sé elegir un medio accesible y seguro."],
    explain=[
        "Un borrador es un primer texto que reviso antes de mostrar. Al revisarlo busco tres tipos de problemas. Datos personales: nombres con apellidos, direcciones, teléfonos y rostros, que permiten ubicar a una persona. Ubicación: dónde está una casa o un lugar, incluso si mi dispositivo la agrega solo. Saberes restringidos: historias o prácticas que una persona o comunidad dijo que no se comparten.",
        "Para corregir un dato personal lo reemplazo por una expresión general: «en una casa del barrio» en lugar de una dirección exacta. Para la ubicación, apago la ubicación del dispositivo y no escribo calles. Para un saber restringido, no lo registro: puedo escribir «una persona mayor nos contó una historia que no se comparte» o simplemente dejarlo afuera.",
        "Registro lo que sí puedo compartir: qué hice, qué aprendí y qué sentí, como «aprendimos a cuidar el agua (ko)». Si no sé si algo se puede registrar, pregunto antes y espero la respuesta. Si la persona que me contó algo dijo que era privado, aunque yo lo encuentre bonito, lo respeto y no lo registro.",
    ],
    vocab=[("borrador", "primer texto que se revisa antes de mostrar"), ("ubicación", "lugar exacto donde está una casa o una persona"), ("dato personal", "dato que identifica a una persona"), ("saber restringido", "conocimiento que no se comparte con cualquiera"), ("expresión general", "frase que no identifica a nadie, como «en una casa del barrio»")],
    worked=[
        W("Encontrar datos personales", BORRADOR_3 + " ¿Qué datos personales o de ubicación aparecen en la primera oración?", ["Leo la primera oración.", "Aparece el nombre completo «Rosa Díaz» y la dirección «Calle Los Olmos 45».", "Son un nombre con apellido y una dirección."], "el nombre completo de Rosa Díaz y la dirección Calle Los Olmos 45"),
        W("Qué hacer con el saber restringido", BORRADOR_3 + " ¿Qué se hace con la historia que «es solo para la familia»?", ["La persona dijo que es solo para la familia.", "Es un saber restringido.", "No se registra."], "no se registra"),
    ],
    mistakes=[
        M("Dejar la dirección «para que sepan dónde fue la actividad».", "Permite ubicar la casa de una persona.", "Escribo «en una casa del barrio» o «en la escuela»."),
        M("Registrar una historia que me pidieron no contar porque «me pareció linda».", "Rompo la confianza de quien la compartió.", "No la registro y respeto la decisión."),
    ],
    R=[
        ex(BORRADOR_3 + " ¿Qué nombre completo aparece en el borrador?", "Rosa Díaz", "Está en la primera oración."),
        ex(BORRADOR_3 + " ¿Qué palabra de la lengua indígena aparece en el borrador?", "ko", "Aparece entre paréntesis."),
        ex("Un saber restringido que una persona pidió no compartir, ¿lo registro o no lo registro?", "no lo registro", "Se respeta su decisión."),
    ],
    C=[
        ex("Verdadero o falso: una dirección exacta es un dato que no debo dejar en un registro.", "Verdadero", "Permite ubicar una casa."),
        ex("¿Qué expresión general reemplaza mejor «Calle Los Olmos 45»? A) «en una casa del barrio». B) «en la casa de Rosa».", "A", "La B identifica a una persona."),
        ex(BORRADOR_3 + " La última oración dice que se grabó con la ubicación activada. ¿Qué se debe hacer: apagar la ubicación o dejarla?", "apagar la ubicación", "La ubicación revela dónde está una persona."),
    ],
    A=[
        ex(BORRADOR_3 + " Cuenta los problemas: 1) nombre completo, 2) dirección, 3) historia restringida, 4) ubicación activada. ¿Cuántos problemas hay?", "4", "Se cuentan cuatro problemas."),
        ex("Reescribe «la casa de mi vecina Rosa Díaz» de forma general. ¿Cuál es mejor? A) «la casa de una vecina». B) «la casa de Rosa D.».", "A", "La B deja un nombre y una inicial."),
        ex("Una persona mayor te contó algo y dijo «esto es solo para la familia». ¿Qué escribes en tu registro: A) la historia completa. B) nada de esa historia?", "B", "Es un saber restringido."),
    ],
    Z=[
        ex("Una niña dice: «Si cambio el nombre por un apodo, ya no hay problema, aunque deje la dirección». ¿Tiene razón? Sí o No.", "No", "La dirección sigue permitiendo ubicar la casa."),
        ex("Dos reescrituras de la primera oración: A) «Hoy, en una casa del barrio, aprendimos cómo se cuida el agua (ko)». B) «Hoy, en la casa de Rosa, aprendimos cómo se cuida el agua (ko)». ¿Cuál protege mejor?", "A", "La B nombra a una persona."),
    ],
    D=[
        arith("Un borrador de práctica tiene 8 datos personales o de ubicación y el curso ya reemplazó 5 por expresiones generales. ¿Cuántos faltan por reemplazar?", "8-5", "Se restan los ya reemplazados del total."),
        ex("Ordena para revisar un borrador: A) reescribo con expresiones generales. B) busco datos personales y ubicación. C) busco saberes restringidos. D) pregunto lo que no sé. Escribe las letras.", "B, C, A, D", "Busco, reescribo y pregunto lo que queda."),
    ],
    context=[ex("Quieres registrar en el cuaderno del curso cómo ayudaste a plantar en tu casa. ¿Escribes «en mi casa de la calle…» o «en mi casa»?", "«en mi casa»", "No se escribe la dirección.")],
    selfcheck=[
        ex("¿Qué dato permite ubicar una casa: la dirección o el color de la puerta?", "la dirección", "Dice dónde está."),
        ex("Si dudo si algo se puede registrar, ¿lo registro o pregunto?", "pregunto", "Ante la duda se pregunta."),
        ex("¿Debo apagar la ubicación del dispositivo antes de registrar? Sí o No.", "Sí", "La ubicación revela dónde estoy."),
    ],
    task=T(
        "Corrige este borrador inventado para practicar. " + BORRADOR_3 + " " + FICHA_PAL + " En tu cuaderno escribe: 1) los cuatro problemas que encontraste, 2) una versión corregida de tres oraciones, que cuente qué aprendiste sobre el agua (ko) sin datos personales, ubicación ni saberes restringidos, 3) una pregunta para el educador o la educadora tradicional.",
        "Problemas: nombre completo, dirección, historia restringida y ubicación activada. Versión corregida: «Hoy, en una casa del barrio, aprendimos cómo se cuida el agua (ko). Una persona mayor nos contó algo que no se comparte. Registramos con la ubicación apagada». Pregunta: ¿cómo contamos una actividad sin exponer a la familia?",
        ["encuentra los cuatro problemas", "corrige sin datos personales ni ubicación", "no registra el saber restringido", "formula una pregunta para el educador/a tradicional"],
        ["lista de problemas", "versión corregida y pregunta escritas"],
        ["dejar la dirección", "registrar la historia"],
        "Revisa que no quede ningún dato personal; si dejó la historia o la dirección, conversa por qué se protege a las personas.",
    ),
    reinforce="Escribe tres expresiones generales para reemplazar un nombre, una dirección y un teléfono.",
    extend="Revisa un texto breve tuyo y subraya cualquier dato que permita ubicar a una persona.",
)

# =================================================================== LS06 clase 4 · revisar lengua, contexto, autoría y almacenamiento
DIARIO = "Registro de práctica (inventado): «Diario de la sala. Hoy el curso cuidó el huerto. Echamos ko a las lechugas y quitamos los palos de la mapu. Los textos los escribió el curso y las palabras ko y mapu las enseñó la educadora tradicional. Lo guardamos en la carpeta de la sala.»"

L(
    LS6, 4,
    materials="Lápiz y un lápiz de otro color para marcar. El registro y las fichas están escritos aquí; son inventados para practicar.",
    use="Aprenderé a revisar un registro con cuatro preguntas: lengua, contexto, autoría y almacenamiento, y a decidir si está listo o si hay que corregirlo. Sirve para entregar un registro cuidadoso de mi vida diaria.",
    prior=["Sé corregir datos personales y saberes restringidos.", "Sé elegir un medio accesible y seguro."],
    explain=[
        "Revisar un registro es leerlo con cuatro preguntas. La lengua: ¿está escrito claro en castellano y las palabras de la lengua indígena están iguales a la ficha? El contexto: ¿dice cuándo, dónde y para qué ocurrió la experiencia? La autoría: ¿dice quién lo escribió y quién enseñó las palabras? El almacenamiento: ¿dónde se guarda y quién puede verlo?",
        "Reviso la lengua comparando cada palabra con la ficha: «ko» es agua y «mapu» es tierra. Una palabra no debe cambiar ni de letra ni de sentido. Reviso el contexto buscando datos como «hoy» y «en el huerto de la escuela». Reviso la autoría buscando quién escribió y quién enseñó. Y reviso el almacenamiento preguntándome si coincide con el permiso: guardo donde se autorizó.",
        "Además me pregunto dos cosas finales. ¿Hay datos personales o saberes restringidos que se me hayan pasado? ¿El registro sirve al propósito que escribí al inicio? Si todas las respuestas son sí, el registro está listo para mostrarse a la audiencia autorizada. Si alguna falla, lo corrijo primero y pregunto al educador tradicional lo que no sé.",
    ],
    vocab=[("lengua", "cómo está escrito el registro y sus palabras"), ("contexto", "cuándo, dónde y para qué ocurrió algo"), ("autoría", "quién escribió y quién enseñó las palabras"), ("almacenamiento", "lugar donde se guarda el registro"), ("audiencia autorizada", "personas que pueden ver el registro")],
    worked=[
        W("Revisar la lengua", DIARIO + " " + FICHA_PAL + " ¿Las palabras «ko» y «mapu» están bien usadas?", ["«Echamos ko a las lechugas»: ko es agua, tiene sentido.", "«Quitamos los palos de la mapu»: mapu es tierra, tiene sentido.", "Están bien usadas."], "sí"),
        W("Revisar el almacenamiento", DIARIO + " Permiso: guardar solo en la sala. ¿Coincide el almacenamiento?", ["Busco dónde se guarda: en la carpeta de la sala.", "El permiso dice solo en la sala.", "Coincide."], "sí, se guarda en la carpeta de la sala"),
    ],
    mistakes=[
        M("Revisar solo la ortografía y olvidar el contexto, la autoría y el almacenamiento.", "Un registro bien escrito puede igual exponer a alguien o usar un permiso mal.", "Reviso las cuatro preguntas."),
        M("Cambiar una palabra de la ficha porque «suena mejor».", "Deja de coincidir con la ficha de la fuente.", "Dejo la palabra igual a la ficha."),
    ],
    R=[
        ex(DIARIO + " ¿Qué hizo el curso hoy?", "cuidó el huerto", "La primera oración lo dice."),
        ex(DIARIO + " ¿Quién enseñó las palabras «ko» y «mapu»?", "la educadora tradicional", "El registro lo dice."),
        ex("Las cuatro preguntas de revisión son lengua, contexto, autoría y almacenamiento. ¿Cuántas son?", "4", "Se cuentan cuatro."),
    ],
    C=[
        ex(DIARIO + " ¿Dónde se guardó el registro?", "en la carpeta de la sala", "La última oración lo dice."),
        ex("Verdadero o falso: puedo dar por listo un registro si la lengua está bien escrita aunque no diga quién lo escribió.", "Falso", "Falta la autoría."),
        ex(DIARIO + " La palabra «hoy» y «en el huerto», ¿responden a qué pregunta de revisión: al contexto o al almacenamiento?", "al contexto", "Dicen cuándo y dónde ocurrió."),
    ],
    A=[
        ex("Cuatro respuestas de revisión del diario: lengua sí, contexto sí, autoría sí, almacenamiento sí. ¿Está listo para mostrar? Sí o No.", "Sí", "Cumple las cuatro preguntas."),
        ex("Registro J (inventado): «Hoy aprendimos cómo se dice ko. Lo guardamos en un sitio abierto». Permiso: guardar solo en la sala. ¿Qué pregunta falla: la de lengua o la de almacenamiento?", "la de almacenamiento", "El sitio abierto no coincide con el permiso."),
        ex("Un registro dice «Palabras enseñadas por la educadora tradicional» pero no dice quién lo escribió. ¿Falta nombrar a quién escribió o a quien enseñó?", "a quien escribió", "Ya está nombrada quien enseñó."),
    ],
    Z=[
        ex("Una niña dice: «Si guardo dos copias, una en la sala y otra en un sitio abierto, igual respeto el permiso». ¿Tiene razón? Sí o No.", "No", "La copia en el sitio abierto no respeta el permiso."),
        ex("Dos revisiones: A) leo el registro y reviso las cuatro preguntas. B) lo leo rápido y lo muestro. ¿Cuál cuida mejor el trabajo?", "A", "La A no deja preguntas sin revisar."),
    ],
    D=[
        arith("Un curso revisó 5 registros y 2 tenían un problema de almacenamiento. ¿Cuántos estaban bien guardados?", "5-2", "Se restan los que tenían el problema."),
        ex("Ordena la revisión: A) reviso dónde se guarda. B) reviso que diga quién escribió y quién enseñó. C) compruebo las palabras con la ficha. D) reviso cuándo y dónde ocurrió. Escribe las letras en el orden de las preguntas (lengua, contexto, autoría, almacenamiento).", "C, D, B, A", "Lengua, contexto, autoría y almacenamiento."),
    ],
    context=[ex("Terminaste tu registro y falta que la educadora lo vea. Un compañero dice «Mostrémoslo igual». ¿Respondes «Primero que lo revise la educadora» o «Sí, mostrémoslo»?", "«Primero que lo revise la educadora»", "La fuente debe revisarlo.")],
    selfcheck=[
        ex("¿Qué comparo para revisar la lengua: mi texto con la ficha de la fuente o con mi memoria?", "con la ficha de la fuente", "La ficha es la referencia."),
        ex("Si el almacenamiento no coincide con el permiso, ¿corrijo o lo dejo?", "corrijo", "Debe respetar el permiso."),
        ex("¿La audiencia autorizada es la que la fuente permitió? Sí o No.", "Sí", "La fuente define quiénes pueden ver."),
    ],
    task=T(
        "Revisa este registro inventado para practicar. Registro K: «Hoy en la sala escribimos nuestro diario. Dijimos mari marí y chaltumay a la visita. Lo guardamos en un sitio abierto». " + FICHA_SAL + " Permiso: guardar solo en la sala. En tu cuaderno haz una tabla de cuatro filas (lengua, contexto, autoría, almacenamiento). En cada fila escribe qué encontraste y cómo lo corregirías. Termina con una pregunta para el educador o la educadora tradicional.",
        "Lengua: «marí» debe ser «mari». Contexto: bien, dice hoy y en la sala. Autoría: falta decir quién enseñó las palabras y quién escribió. Almacenamiento: debe guardarse en la sala, no en un sitio abierto. Pregunta: ¿podemos guardar una copia en papel?",
        ["completa las cuatro filas", "detecta el error de lengua", "corrige el almacenamiento según el permiso", "formula una pregunta para el educador/a tradicional"],
        ["tabla de revisión de cuatro filas", "pregunta escrita o dicha en voz alta"],
        ["revisar solo la ortografía", "dejar el sitio abierto"],
        "Verifica que revisó las cuatro preguntas; si dejó el sitio abierto, conversa por qué no coincide con el permiso.",
    ),
    reinforce="Escribe en una tarjeta las cuatro preguntas de revisión y revisa con ellas un texto tuyo.",
    extend="Explica a una persona de tu casa por qué un registro se guarda donde la fuente lo permitió.",
)
