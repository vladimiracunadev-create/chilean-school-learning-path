"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF01 (historias de eventos socioculturales o espirituales de otros pueblos, cosmovisiones y opinión
fundamentada) y OA LF02 (exposición y diálogo oral: análisis, registros formal y no formal, énfasis).

Criterio de autoría: todas las comunidades, los lugares, las personas, los eventos y los relatos son INVENTADOS solo
para practicar y se rotulan así. No se afirma nada de lengua, ritos, fechas de celebraciones, arte, cosmovisión ni roles
de un pueblo concreto. Las únicas palabras en lengua indígena son saludos y agradecimientos muy atestiguados
(«mari mari» y «chaltumay» en mapuzugun; «iorana» y «maururu» en rapa nui). No se inventa gramática, pronunciación,
grafía ni significados rituales. Ningún ejercicio exige saber una lengua indígena: lo que se dice en lengua lo enseñan
el educador o la educadora tradicional y la comunidad. Los otros módulos lc6_* importan los ayudantes de este archivo.
"""
from __future__ import annotations

import re
import zlib

from student_lessons import arith, ex, register

LF1, LF2 = "LC06 OA LF01", "LC06 OA LF02"

CONSULT = " Recuerda: lo que se dice en la lengua y las prácticas de un pueblo las enseñan el educador o la educadora tradicional y las personas de la comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. Nunca evaluar la identidad ni el origen de un estudiante."


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement + CONSULT, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback + FEEDBACK_ADD}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def vf(q, truth, why):
    """Verdadero o falso."""
    return ex("Verdadero o falso: " + q, "Verdadero" if truth else "Falso", why)


def ab(q, right, wrong, why, right_first=True):
    """Dos alternativas; la respuesta es la letra de la correcta."""
    if right_first:
        return ex(f"{q} A) {right} B) {wrong}", "A", why)
    return ex(f"{q} A) {wrong} B) {right}", "B", why)


_OPTIONS = re.compile(r"^(?P<stem>.*?) A\) (?P<a>.*?) B\) (?P<b>.*)$", re.S)


def _balance(items):
    """Alterna de forma determinista la posición de la alternativa correcta para que no sea casi siempre la A."""
    for item in items:
        match = _OPTIONS.match(item["q"])
        if item["a"] in ("A", "B") and match and zlib.crc32(item["q"].encode("utf-8")) % 2:
            item["q"] = f"{match['stem']} A) {match['b']} B) {match['a']}"
            item["a"] = "B" if item["a"] == "A" else "A"
    return items


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, context, selfcheck, task, reinforce, extend):
    for group in (R, C, A, Z, D, context, selfcheck):
        _balance(group)
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


MAT = "Lápiz y hojas. Los relatos, las fichas y las listas están escritos en este cuaderno. Las comunidades, los lugares, las personas y los eventos son inventados y no corresponden a ningún pueblo real."

# ============================================================ OA LF01 · Historias de eventos de otros pueblos
L(
    LF1, 1, materials=MAT,
    use="Aprenderé a situar un evento sociocultural o espiritual de otro pueblo: decir qué comunidad lo vive, quién lo cuenta, si hay permiso y qué no se cuenta. Sirve para disfrutar una historia ajena sin apropiarme de ella.",
    prior=["Sé que una fuente es la persona que entrega un dato.", "Sé que cada comunidad cuenta su territorio y sus costumbres a su manera."],
    explain=[
        "Un evento sociocultural es una reunión en que las personas de una comunidad comparten una costumbre: una cosecha, una fiesta, un trabajo en común o un encuentro para recordar. Un evento espiritual es aquel en que la comunidad se relaciona con lo que considera sagrado. Muchos eventos tienen las dos cosas a la vez.",
        "Cuando leemos o escuchamos la historia de un evento de otro pueblo, primero la situamos. Una ficha situada dice la comunidad, el evento, la fuente, el permiso y el límite. La fuente es la persona que cuenta; el permiso, que esa persona autorizó compartir; el límite, lo que no se cuenta porque la comunidad lo reserva.",
        "Disfrutar una historia ajena no es apropiarse de ella. Se disfruta escuchando con atención y valorando lo que enseña, pero siempre se dice de quién es. Lo que la comunidad guarda para sí se respeta, aunque dé curiosidad. Cómo se opina en la lengua indígena lo trabajas con el educador o la educadora tradicional.",
    ],
    vocab=[("evento sociocultural", "reunión en que una comunidad comparte una costumbre"), ("evento espiritual", "reunión en que la comunidad se relaciona con lo que considera sagrado"), ("ficha situada", "hoja que dice comunidad, evento, fuente, permiso y límite"), ("permiso", "autorización de la fuente para compartir lo que contó"), ("apropiarse", "usar algo ajeno como si fuera propio")],
    worked=[
        W("Leer una ficha situada", "Ficha inventada. Comunidad: Cerro Alegre (no es un pueblo real). Evento: Encuentro de la Primera Cosecha. Fuente: doña Rosa, vecina. Permiso: doña Rosa autorizó usar el relato en la escuela. Límite: no se cuenta la parte reservada del encuentro. ¿Qué evento es, quién lo cuenta y qué no se cuenta?",
          ["El evento aparece después de la palabra «Evento»: Encuentro de la Primera Cosecha.", "La fuente es doña Rosa y ella dio permiso.", "El límite dice que la parte reservada no se cuenta."], "Es el Encuentro de la Primera Cosecha, lo cuenta doña Rosa y no se cuenta la parte reservada."),
        W("Detectar un dato que falta", "Ficha inventada. Comunidad: Bahía Larga. Evento: Fiesta de la Mar en Calma. Fuente: don Ignacio, pescador. Permiso: no dice. ¿Puedes usar el relato en un trabajo?", ["Reviso los cinco datos de la ficha.", "El permiso no aparece escrito.", "Sin permiso no sé si la fuente quiere que se comparta."], "No: primero hay que pedir el permiso a don Ignacio o a la comunidad."),
    ],
    mistakes=[
        M("Pensar que un evento solo es «espiritual» si es serio y callado.", "Muchos eventos mezclan fiesta, trabajo y respeto a lo sagrado.", "Pregúntate qué hace la comunidad y qué valor le da ella."),
        M("Contar la parte reservada porque «ya la leí».", "Haberla leído no da derecho a repetirla.", "Respeta el límite de la ficha y escribe solo lo permitido."),
    ],
    R=[
        ex("Ficha: «Comunidad: Alto Sauce. Evento: Día de las Semillas. Fuente: doña Gladys.» ¿Cómo se llama el evento?", "Día de las Semillas", "El nombre aparece después de la palabra «Evento»."),
        ex("En la misma ficha, ¿quién es la fuente?", "Doña Gladys", "La ficha nombra a doña Gladys como fuente."),
        ex("La ficha dice «Límite: no se cuentan los nombres de las familias». ¿Escribes esos nombres en tu trabajo? Responde Sí o No.", "No", "El límite lo prohíbe."),
    ],
    C=[
        vf("un evento sociocultural puede ser una cosecha en que las familias comparten una costumbre.", True, "Es una reunión que comparte una costumbre."),
        ab("¿Qué es un evento espiritual?", "una reunión en que la comunidad se relaciona con lo que considera sagrado", "un partido de pelota entre dos cursos", "Lo espiritual se relaciona con lo que cada comunidad considera sagrado."),
        vf("si leí la parte reservada de un evento, ya puedo contarla a mis compañeros.", False, "Lo reservado se respeta aunque se haya leído."),
    ],
    A=[
        ex("Ficha incompleta: «Comunidad: Alto Sauce. Evento: Día de las Semillas. Fuente: no dice. Permiso: no dice.» ¿Qué datos faltan para usarla? A) fuente y permiso B) fotos y música", "A", "Sin fuente ni permiso la ficha no sirve."),
        ex("Clasifica cada dato como COMUNIDAD, EVENTO o FUENTE: a) doña Gladys b) Alto Sauce c) Día de las Semillas.", "a fuente, b comunidad, c evento", "Doña Gladys cuenta, Alto Sauce es el lugar y el Día de las Semillas es lo que se celebra."),
        ex("Relato inventado: «En Alto Sauce, cada familia trae un puñado de semillas. Una persona mayor dice unas palabras sobre ellas y esa parte es solo de la comunidad. Después se siembra una chacra común.» ¿Qué parte no puedes contar con detalle?", "La parte en que la persona mayor dice unas palabras sobre las semillas", "El relato dice que esa parte es solo de la comunidad."),
    ],
    Z=[
        ex("Camila escribe: «Todos los pueblos celebran una cosecha como la de Alto Sauce». ¿Qué error comete?", "Generaliza una ficha a todos los pueblos", "Una comunidad no representa a todas."),
        ex("Un compañero cuenta el relato de Alto Sauce como si fuera una historia de su familia. ¿Qué falla?", "No atribuye el relato a doña Gladys ni a su comunidad", "Contar sin decir de quién es apropia el relato."),
    ],
    D=[
        ex("En Alto Sauce las familias siembran una chacra común; en Playa Mansa el primer pescado se reparte entre las casas que no salieron. Alguien escribe: «Se reparte el primer pescado». ¿De qué comunidad viene el dato?", "De Playa Mansa", "El reparto del primer pescado es de Playa Mansa."),
        ab("¿Se puede disfrutar un relato y, al mismo tiempo, respetar lo que la comunidad reserva?", "sí, se disfruta lo permitido y se respeta el límite", "no, hay que contarlo todo para disfrutarlo", "Disfrutar y respetar el límite no se oponen."),
    ],
    context=[ab("Tu curso quiere presentar en un acto escolar el relato de Alto Sauce. Antes de hacerlo, ¿qué conviene?", "pedir permiso, decir quién cuenta y respetar el límite", "ensayar rápido y presentarlo sin mencionar a nadie", "Un acto escolar también necesita permiso y atribución.", right_first=False)],
    selfcheck=[
        ex("Nombra tres datos que debe tener una ficha situada.", "Tres entre: comunidad, evento, fuente, permiso, límite", "Son los datos que permiten situar el relato."),
        vf("el límite de una ficha dice lo que la comunidad prefiere no contar.", True, "El límite marca lo reservado."),
        ex("Si tienes una duda sobre una costumbre de un pueblo real, ¿a quién consultas? A) al educador tradicional o a la comunidad B) a nadie, lo imagino", "A", "Ellos son la fuente."),
    ],
    task=T("Lee este relato inventado de doña Norma, de la comunidad Rincón Alto: «Cuando llegan las primeras lluvias, las familias se juntan en la cancha del pueblo. Cada una trae una olla grande y se comparte la comida entre todos. Una persona mayor pronuncia unas palabras de agradecimiento que son solo para la comunidad.» Haz una ficha con estos campos: comunidad, evento, fuente, qué cuenta el relato y qué límite pondrías. Termina con una frase que empiece con «Me gustó…».",
           "Comunidad: Rincón Alto. Evento: reunión de las primeras lluvias. Fuente: doña Norma. Cuenta: las familias comparten comida en la cancha. Límite: no se cuentan las palabras de agradecimiento. Me gustó que todas las familias compartieran lo que traen.",
           ["completa la ficha con datos del relato", "pone un límite", "expresa qué le gustó"], ["ficha completa", "frase con «Me gustó…»"], ["agregar datos que el relato no dice", "contar la parte reservada"],
           "Pedir que muestre en qué línea del relato está cada dato; valorar que respete la parte reservada."),
    reinforce="Subraya en la ficha de Cerro Alegre la comunidad, el evento, la fuente, el permiso y el límite con cinco colores.",
    extend="Explica con tus palabras por qué disfrutar la historia de otro pueblo no es lo mismo que apropiarse de ella.",
)

L(
    LF1, 2, materials=MAT,
    use="Aprenderé a leer la historia de un evento separando lo que dice el relato, lo que interpreto y lo que no se cuenta. Sirve para comprender sin inventar y para decir qué me gustó.",
    prior=["Sé situar un evento con su ficha.", "Sé que lo reservado por una comunidad se respeta."],
    explain=[
        "Comprender una historia es saber qué ocurrió, quiénes participaron, dónde y por qué importa para quienes la cuentan. Para lograrlo, separamos tres cosas. Primero, lo que el relato dice, con sus palabras. Segundo, lo que yo interpreto, que es una idea mía. Tercero, lo que no se cuenta o yo no sé.",
        "Disfrutar es otra cosa: es expresar qué me gustó, qué me sorprendió o qué me hizo pensar. Disfrutar no obliga a creer ni a imitar. Puedo decir «me gustó que compartieran la comida» sin afirmar nada sobre lo que piensa la comunidad.",
        "Lo que interpreto lo marco con «yo pienso que». Lo que el relato no explica lo marco con «el relato no lo dice». Así, quien me escucha sabe qué viene de la comunidad y qué viene de mí. Si quiero saber más, preparo una pregunta para el educador o la educadora tradicional.",
    ],
    vocab=[("comprender", "saber qué ocurrió, quiénes participaron y por qué importa"), ("disfrutar", "expresar qué me gustó o qué me hizo pensar"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("límite", "lo que no se cuenta o no se sabe"), ("detalle", "dato pequeño del relato que ayuda a comprender")],
    worked=[
        W("Separar tres cosas", "Relato inventado de don Ignacio, de Bahía Larga: «Cuando el mar amanece en calma, los pescadores sacan sus botes juntos. Al volver, el primer pescado se reparte entre las casas que no pudieron salir. Hay una frase de despedida que solo conoce la comunidad». Separa lo que dice, lo que interpreto y lo que no se cuenta.", ["Dice: el primer pescado se reparte entre las casas que no salieron.", "Interpreto: yo pienso que reparten así para que nadie se quede sin comida.", "No se cuenta: la frase de despedida."], "Dice: reparten el primer pescado. Interpreto: es para cuidar a quienes no salieron. No se cuenta: la frase de despedida."),
        W("Distinguir comprender y disfrutar", "Una niña escribe: «Me encantó la parte del reparto del pescado». Otro escribe: «Los pescadores salen juntos». ¿Quién expresa que disfrutó y quién que comprendió?", ["La primera frase dice «me encantó»: es un gusto personal.", "La segunda cuenta un hecho del relato.", "Una es disfrute y la otra, comprensión."], "La niña expresa que disfrutó; el otro compañero muestra que comprendió."),
    ],
    mistakes=[
        M("Escribir mi interpretación como si la hubiera dicho la fuente.", "Se atribuye a la comunidad algo que no dijo.", "Marca mis ideas con «yo pienso que»."),
        M("Rellenar con ideas lo que la comunidad decidió no contar.", "Lo reservado se respeta; inventarlo puede ser falso e irrespetuoso.", "Escribe «el relato no lo dice»."),
    ],
    R=[
        ex("Relato inventado de doña Gladys: «Cada familia trae un puñado de semillas a la plaza». ¿Qué trae cada familia?", "Un puñado de semillas", "El relato lo dice así."),
        ex("¿Una interpretación es una idea mía o un dato del relato?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Si el relato no explica algo, ¿qué escribes? A) el relato no lo dice B) lo invento", "A", "No se rellenan los vacíos con ideas inventadas."),
    ],
    C=[
        vf("disfrutar un relato significa que debo creer todo lo que dice o imitarlo.", False, "Disfrutar es expresar mi gusto; no obliga a creer ni a imitar."),
        ab("¿Con qué marca escribo mis ideas?", "«yo pienso que»", "«la comunidad dice que»", "Así no se confunden con la fuente."),
        vf("«me sorprendió la olla grande de comida» expresa disfrute.", True, "Dice lo que me sorprendió, es una reacción personal."),
    ],
    A=[
        ex("Relato inventado: «En Quebrada Seca, antes de partir al cerro, cada persona lleva un poco de agua para otra». Clasifica en DICE EL RELATO o INTERPRETO: a) cada persona lleva agua para otra b) la comunidad se cuida mucho.", "a dice el relato, b interpreto", "La primera está escrita; la segunda es una suposición."),
        ex("Don Ignacio dice: «Hay una frase de despedida que solo conoce la comunidad». ¿Qué puedes escribir en tu trabajo sobre esa frase? A) que existe y que no se cuenta B) una frase inventada por ti", "A", "Solo se afirma que existe; su contenido se respeta."),
        ex("Una niña lee «los botes salen juntos» y escribe «Los pescadores creen que salir juntos trae suerte». ¿Qué dato no está en el relato?", "Que creen que trae suerte", "El relato dice que salen juntos, no por qué."),
    ],
    Z=[
        ex("Rodrigo escribe, sin marcarlo: «Los pescadores son los más generosos del mundo». ¿Qué debería hacer con esa frase?", "Marcarla como su opinión o quitarla", "No está en el relato, así que es opinión."),
        ex("¿Por qué conviene escribir los límites al final de un trabajo? A) para mostrar hasta dónde llega lo afirmado B) para llenar la hoja", "A", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        ex("Relato: «Las familias de Alto Sauce tejen una manta común durante la fiesta». Dos frases: Uno: «Se teje una manta común». Otro: «La manta tiene un significado sagrado». ¿Cuál se queda en el relato?", "La primera", "La segunda agrega algo que el relato no dice."),
        ex("Don Ignacio no contó por qué el mar en calma es importante para la fiesta. ¿Qué escribes en los límites? A) no sé por qué la calma es importante B) es importante por un animal", "A", "Declarar lo que no sé evita inventar."),
    ],
    context=[ab("Para un afiche escolar, un compañero quiere dibujar la frase de despedida que la comunidad guarda solo para sí. ¿Qué le dices?", "que esa parte se respeta y no se dibuja", "que la dibuje inventándola", "El límite del relato dice que esa frase no se cuenta.")],
    selfcheck=[
        ex("Nombra las tres cosas que separo al leer un relato.", "Lo que dice el relato, lo que interpreto y lo que no se cuenta", "Son los tres pasos de la lectura con límites."),
        vf("puedo completar con mi imaginación lo que la comunidad no contó.", False, "Eso sería inventar."),
        ex("¿Qué escribes cuando el relato no explica algo? Escribe una frase corta.", "El relato no lo dice", "Es la manera honesta de marcar un vacío."),
    ],
    task=T("Lee este relato inventado de doña Berta, de Llano Claro: «Al terminar la esquila, las familias cocinan juntas en el patio de la escuela. Los más pequeños llevan el pan a cada mesa. Hay un canto de gracias que solo se canta entre la comunidad.» Haz tres columnas: «El relato dice», «Yo interpreto» y «No se cuenta». Pon al menos dos datos en cada una. Agrega una frase que empiece con «Lo que más me gustó fue…».",
           "El relato dice: cocinan juntas en el patio; los pequeños llevan el pan. Yo interpreto: yo pienso que los niños aprenden a participar. No se cuenta: el canto de gracias. Lo que más me gustó fue que los niños llevaran el pan.",
           ["separa tres columnas", "usa datos del relato", "marca sus ideas como interpretación"], ["tabla de tres columnas", "frase de disfrute"], ["escribir interpretaciones como datos", "inventar el canto reservado"],
           "Pedir que indique en qué línea del relato está cada dato; valorar que deje sin completar lo no contado."),
    reinforce="Subraya con un color lo que dice el relato de Bahía Larga y con otro lo que interpretas.",
    extend="Explica por qué callar una parte del evento puede ser una manera de cuidarlo, usando el relato de Bahía Larga.",
)

L(
    LF1, 3, materials=MAT,
    use="Aprenderé a encontrar relaciones entre un evento, su territorio, las personas que participan y lo que enseña, y a dialogar con un evento de mi propio entorno. Sirve para entender por qué el evento importa a su comunidad.",
    prior=["Sé separar lo que dice un relato de lo que interpreto.", "Sé que no debo jerarquizar comunidades."],
    explain=[
        "Un evento se relaciona con muchas cosas. Se relaciona con el territorio, porque ocurre en un lugar y a veces en una estación del año. Se relaciona con las personas, porque cada una tiene un papel. Y se relaciona con un saber o un valor, como compartir, agradecer o cuidar. Esas relaciones se buscan en el relato, sin inventarlas.",
        "Un diálogo de conocimientos ocurre cuando ponemos en conversación lo que sabe una comunidad con lo que sabemos nosotros, sin decir que uno vale más. Para dialogar, primero preguntamos y escuchamos; después contamos algo de nuestro entorno que se parezca o sea distinto, por ejemplo un encuentro de vecinos de nuestro barrio.",
        "Al comparar, usamos los mismos criterios para las dos partes: dónde ocurre, quiénes participan y qué valor aparece. Anotamos semejanzas y diferencias. Que dos eventos se parezcan no significa que sean iguales, y que sean distintos no significa que uno sea mejor.",
    ],
    vocab=[("relación cultural", "unión entre dos cosas de un relato, como un lugar y un valor"), ("valor", "idea que una comunidad considera importante, como compartir o cuidar"), ("diálogo de conocimientos", "conversación en que se escucha lo que sabe cada parte sin decir que una vale más"), ("semejanza", "algo parecido entre dos eventos"), ("criterio", "punto igual para comparar dos cosas")],
    worked=[
        W("Encontrar relaciones en un relato", "Relato inventado de doña Rosa, de Cerro Alegre: «Al terminar el verano llevamos a la plaza lo mejor de nuestra huerta. Reparten pan de calabaza entre todos». ¿Qué relaciones aparecen?", ["Con el territorio: la huerta y la época, el fin del verano.", "Con las personas: todas las familias llevan algo.", "Con un valor: compartir lo que se cosechó."], "Se relacionan huerta y época, familias participantes y el valor de compartir la cosecha."),
        W("Dialogar con mi entorno", "Después de leer el relato de Cerro Alegre, una niña cuenta: «En mi barrio hacemos una once compartida cuando termina el año». ¿Cómo dialoga con el relato?", ["Busca algo parecido en su entorno: una comida compartida.", "No dice que la suya sea mejor ni igual.", "Anota una semejanza: ambos comparten comida."], "Dialoga comparando sin jerarquizar y nombra una semejanza: compartir comida."),
    ],
    mistakes=[
        M("Decir que el evento de mi barrio es igual al del relato.", "Se parecen en un punto, pero tienen otro origen y otro sentido.", "Escribe qué se parece y qué es distinto."),
        M("Inventar el valor de un evento sin que el relato lo diga.", "El sentido de un evento lo explica la comunidad.", "Marca «yo pienso que» y consulta al educador o educadora tradicional."),
    ],
    R=[
        ex("Relato inventado: «En Playa Mansa, los pescadores salen juntos cuando el mar está en calma». ¿Con qué lugar se relaciona el evento? A) el mar B) la montaña", "A", "El relato habla del mar en calma."),
        ex("Relato: «Cada familia trae una olla grande». ¿Quiénes participan? A) las familias B) un solo vecino", "A", "El relato dice cada familia."),
        ex("¿Qué es un valor, en un evento cultural? Elige: A) una idea que la comunidad considera importante, como compartir B) el precio de la comida", "A", "Un valor es una idea importante para la comunidad."),
    ],
    C=[
        vf("comparar dos eventos significa decir cuál es mejor.", False, "Comparar es buscar semejanzas y diferencias."),
        ab("En un diálogo de conocimientos, ¿qué se hace primero?", "preguntar y escuchar", "corregir a la otra persona", "Escuchar permite comprender antes de comparar."),
        vf("si dos eventos se parecen en algo, entonces son iguales.", False, "Se parecen en un punto, pero pueden ser distintos en otros."),
    ],
    A=[
        ex("Criterio «quiénes participan». Alto Sauce: cada familia trae semillas. Rincón Alto: cada familia trae una olla. ¿Qué semejanza hay? A) participan todas las familias B) participa un solo vecino", "A", "En ambas, todas las familias aportan algo."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) en ambas comunidades se comparte algo b) una comparte semillas y la otra comida.", "a semejanza, b diferencia", "La primera es algo común; la segunda, algo distinto."),
        ex("Relato: «El sendero lleva a la caleta donde se reparte el pescado». Completa: el sendero lleva hasta…", "La caleta", "El relato dice que el sendero lleva a la caleta."),
    ],
    Z=[
        ex("Paula escribe: «La fiesta de Alto Sauce es mejor que la de Rincón Alto porque trae más gente». ¿Qué error comete?", "Jerarquiza dos eventos", "Cada comunidad vive su evento a su manera; la cantidad de personas no lo hace mejor."),
        ex("Pedro dice que, como dos eventos comparten comida, todos los pueblos hacen lo mismo. ¿Por qué no es válido? A) dos casos no alcanzan para hablar de todos B) porque no comparten nada", "A", "Hay muchos pueblos y cada uno cuenta su propia relación."),
    ],
    D=[
        ex("Tabla con el criterio «valor que aparece»: Alto Sauce, compartir semillas; Rincón Alto, compartir comida. ¿Cuál afirmación es correcta? A) en ambos eventos aparece compartir B) solo en uno se comparte", "A", "Las dos fuentes muestran compartir."),
        ex("Quieres escribir sobre una tercera comunidad, Pampa Verde, pero no tienes ficha. ¿Qué haces? A) la dejo fuera hasta tener su ficha B) la describo por parecido a las otras", "A", "No se describe a una comunidad sin su propia fuente."),
    ],
    context=[ab("En un panel escolar, dos grupos presentan Alto Sauce y Rincón Alto. Un visitante pregunta cuál evento es el más valioso. ¿Qué respondes?", "cada comunidad lo vive a su manera y no se ordenan", "el de las semillas", "Comparar no es jerarquizar.")],
    selfcheck=[
        ex("Escribe una semejanza entre Alto Sauce y Rincón Alto según este cuaderno.", "En ambas las familias comparten algo", "Aparece en los dos relatos."),
        vf("puedo decir que un evento es mejor que otro si me gusta más.", False, "Eso es jerarquizar por gusto personal."),
        ex("¿Qué usas para comparar bien? A) los mismos criterios para los dos eventos B) criterios distintos para cada uno", "A", "Con criterios iguales la comparación es justa."),
    ],
    task=T("Lee dos relatos inventados. Cerro Alegre (doña Rosa): «Al terminar el verano llevamos a la plaza lo mejor de la huerta y repartimos pan de calabaza». Bahía Larga (don Ignacio): «Cuando el mar está en calma salimos juntos y repartimos el primer pescado». Haz una tabla con tres criterios: dónde ocurre, quiénes participan y qué valor aparece. Agrega una semejanza, una diferencia y un hecho de tu barrio que dialogue con ellos (por ejemplo, un día en que los vecinos limpian la calle juntos).",
           "Cerro Alegre: plaza, familias, compartir la cosecha. Bahía Larga: mar, pescadores, compartir el primer pescado. Semejanza: en ambas se comparte. Diferencia: una es de huerta y la otra, de mar. En mi barrio los vecinos limpian la calle juntos, y eso se parece porque trabajan en común.",
           ["usa tres criterios iguales para ambas", "escribe una semejanza y una diferencia", "no jerarquiza", "dialoga con un hecho de su entorno"], ["tabla comparativa", "dos frases y un ejemplo propio"], ["decir cuál es mejor", "generalizar a todos los pueblos"],
           "Pedir que muestre cada dato en el relato; valorar que no ordene de mejor a peor."),
    reinforce="Subraya con verde las semejanzas y con azul las diferencias en tu tabla.",
    extend="Escribe una pregunta que le harías a doña Rosa para entender mejor por qué se reparte el pan de calabaza.",
)

L(
    LF1, 4, materials=MAT,
    use="Aprenderé a dar una opinión fundamentada sobre una historia de otro pueblo, diciendo de quién es cada dato. Sirve para opinar con respeto y sin hablar por otros.",
    prior=["Sé buscar relaciones culturales en un relato.", "Sé separar lo que dice la fuente de lo que opino."],
    explain=[
        "Una opinión fundamentada es una opinión con razones tomadas del relato. Tiene dos partes: lo que pienso y la razón. Se puede escribir así: «Opino que… porque el relato dice que…». La razón es un dato del relato, no un deseo mío. Si la razón no está en el relato, la opinión queda sin fundamento.",
        "Una respuesta atribuida dice de quién viene cada dato: «según doña Rosa…» o «don Ignacio cuenta que…». Así se distingue la voz de la comunidad de la mía. Además agregamos un límite, es decir, lo que no sé o no se cuenta, y una pregunta para el educador o la educadora tradicional.",
        "Fundamentar una opinión en la lengua indígena que corresponda es un trabajo compartido: tú preparas la idea y la razón en castellano; el educador o la educadora te enseña cómo se dice en la lengua de tu comunidad. Nunca se inventan palabras ni frases por cuenta propia.",
    ],
    vocab=[("opinión fundamentada", "opinión que incluye una razón tomada del relato"), ("atribuir", "decir de quién viene un dato"), ("fundamento", "razón del relato que respalda una opinión"), ("devolución", "mostrar lo escrito a la comunidad o al educador para que lo revise"), ("límite", "lo que no sé o no se cuenta")],
    worked=[
        W("Armar una opinión fundamentada", "Relato inventado de doña Norma, de Rincón Alto: «Cuando llegan las primeras lluvias, cada familia trae una olla y se comparte la comida entre todos». Escribe una opinión fundamentada.", ["Idea: me parece bonito el evento.", "Razón del relato: se comparte la comida entre todos.", "Se une con la fórmula: Opino que es un evento acogedor porque, según doña Norma, se comparte la comida entre todos."], "Opino que el evento es acogedor porque, según doña Norma, se comparte la comida entre todos."),
        W("Corregir una atribución", "Un niño escribe: «En Rincón Alto la lluvia es lo más sagrado». ¿Qué falta?", ["No dice quién lo afirma.", "El relato habla de compartir comida, no de lo sagrado.", "Hay que atribuir y quitar lo que no está."], "Faltó atribuir a doña Norma y quitar «lo más sagrado», que no está en el relato."),
    ],
    mistakes=[
        M("Escribir «los pueblos indígenas piensan que…» a partir de un solo relato.", "Un relato habla de una comunidad.", "Escribe «según doña Norma, de Rincón Alto…»."),
        M("Dar una opinión sin razón.", "Sin razón nadie sabe en qué se apoya.", "Agrega «porque el relato dice que…»."),
    ],
    R=[
        ex("¿Con qué frase empiezas para atribuir un dato a don Ignacio? A) «Don Ignacio cuenta que…» B) «Todos saben que…»", "A", "Nombra a la fuente."),
        ex("¿Cuántas partes tiene una opinión fundamentada: una o dos? Escribe el número.", "2", "Son lo que pienso y la razón."),
        vf("la razón de una opinión fundamentada se toma del relato.", True, "Por eso se llama fundamentada."),
    ],
    C=[
        ex("¿Qué es una respuesta atribuida? A) una en que cada dato dice de quién viene B) una sin nombres", "A", "Atribuir es nombrar la fuente."),
        vf("puedo escribir «los pueblos indígenas piensan lo mismo» después de leer un solo relato.", False, "Un relato no representa a todos los pueblos."),
        ab("¿Quién enseña cómo se dice mi opinión en la lengua indígena de mi comunidad?", "el educador o la educadora tradicional", "yo, inventando las palabras", "La lengua se aprende de quien la enseña en la comunidad."),
    ],
    A=[
        ex("Relato de don Ignacio: «Los botes salen juntos cuando el mar está en calma». Completa la atribución: «Don Ignacio cuenta que los botes…»", "Salen juntos cuando el mar está en calma", "Repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o RAZÓN PROPIA: a) doña Norma cuenta que se comparte la comida b) yo pienso que eso une a las familias.", "a fuente, b razón propia", "La primera es un dato atribuido; la segunda es una idea propia."),
        ex("Opinión: «Opino que el evento enseña a compartir porque, según doña Norma, se reparte la comida». ¿Cuál es la razón?", "Según doña Norma, se reparte la comida", "Es el dato del relato que respalda la opinión."),
    ],
    Z=[
        ex("Marta escribe una opinión que dice «Opino que el evento es hermoso porque sí». ¿Qué mejoraría? A) agregar una razón del relato B) agregar más adjetivos", "A", "Una opinión fundamentada necesita una razón del relato."),
        ex("¿Por qué conviene mostrar tu trabajo a la comunidad o al educador? A) porque ellos pueden corregir errores sobre su cultura B) porque es obligatorio decorar", "A", "Ellos conocen su propia cultura."),
    ],
    D=[
        ex("Dos opiniones sobre el mismo relato («se comparte la comida entre todos»). Uno: «Opino que es un evento alegre porque se comparte la comida». Otro: «Opino que es un evento triste porque sí». ¿Cuál está mejor fundamentada?", "La primera", "Tiene una razón tomada del relato."),
        ex("Don Ignacio no explicó por qué la fiesta se hace con el mar en calma. ¿Qué escribes en el límite? A) no sé por qué se hace con el mar en calma B) se hace porque el mar se enoja", "A", "Declarar lo que no sé evita inventar."),
    ],
    context=[ab("En una conversación, un compañero pregunta qué piensas del evento de Rincón Alto. ¿Cómo respondes?", "doy mi opinión con una razón del relato y digo de quién es el relato", "digo que a todos los pueblos les pasa lo mismo", "Una opinión fundamentada se apoya en el relato y atribuye la fuente.")],
    selfcheck=[
        ex("Escribe la fórmula de una opinión fundamentada con tus palabras.", "Opino que… porque el relato dice que…", "Une la idea con una razón del relato."),
        vf("mi opinión puede ser distinta a la de un compañero y ambas ser respetables.", True, "Opinar distinto es posible si cada uno se apoya en el relato."),
        ex("¿Qué haces si necesitas decir tu opinión en la lengua de tu comunidad? A) consulto al educador o educadora tradicional B) invento las palabras", "A", "Ellos enseñan la lengua."),
    ],
    task=T("Lee este relato inventado de don Patricio, de Costa Mansa: «Al amanecer de la cosecha del alga, las familias bajan juntas a la orilla. Los más jóvenes ayudan a cargar los canastos de los mayores. Hay una oración que se dice solo en la comunidad.» Escribe una opinión fundamentada con la fórmula «Opino que… porque, según don Patricio…», una frase de límites y una pregunta para el educador o educadora tradicional.",
           "Opino que el evento muestra respeto por los mayores porque, según don Patricio, los jóvenes cargan los canastos de los mayores. Límite: no sé qué se dice en la oración. Pregunta: ¿cómo se cuida esa oración en la comunidad?",
           ["usa la fórmula con razón del relato", "atribuye a don Patricio", "declara un límite y formula una pregunta"], ["opinión escrita", "frase de límites", "pregunta"], ["opinar sin razón", "inventar la oración reservada"],
           "Pedir que señale la línea del relato que sirve de razón; valorar que deje sin completar la oración."),
    reinforce="Subraya la razón en tres opiniones que escribas sobre un mismo relato.",
    extend="Escribe una segunda opinión sobre el mismo relato con otra razón distinta y compara cuál se apoya mejor.",
)

L(
    LF1, 5, materials=MAT,
    use="Aprenderé a contrastar dos historias de eventos de pueblos distintos sin decir cuál es mejor, valorando sus cosmovisiones. Sirve para dialogar entre culturas con respeto.",
    prior=["Sé dar una opinión fundamentada.", "Sé comparar con los mismos criterios."],
    explain=[
        "La cosmovisión es la manera en que un pueblo entiende el mundo, la naturaleza y la vida. Cada pueblo tiene la suya, y no hay una que valga más que otra. Cuando dos relatos muestran formas distintas de entender el mundo, no buscamos un ganador: buscamos entender qué enseña cada uno.",
        "Contrastar es poner dos relatos lado a lado para ver sus semejanzas y diferencias. Para hacerlo sin jerarquizar, usamos los mismos criterios con ambos, describimos con las palabras de cada fuente y evitamos palabras como «mejor», «peor», «atrasado» o «avanzado». Preguntamos qué valor muestra cada uno.",
        "Valorar una cosmovisión significa reconocer que tiene sentido para quienes la viven y que podemos aprender de ella. No significa que debamos adoptarla ni que debamos rechazarla. Una opinión fundamentada puede decir: «Valoro que en este relato se cuide a quienes no pudieron salir, porque según don Ignacio se reparte el primer pescado entre sus casas».",
    ],
    vocab=[("cosmovisión", "manera en que un pueblo entiende el mundo, la naturaleza y la vida"), ("contrastar", "poner dos cosas lado a lado para ver semejanzas y diferencias"), ("jerarquizar", "decir que algo es mejor o más importante que otra cosa"), ("valorar", "reconocer que algo tiene sentido y puede enseñarnos"), ("respeto", "tratar a otros y sus ideas con consideración")],
    worked=[
        W("Contrastar sin jerarquizar", "Cerro Alegre (relato inventado): una persona mayor agradece a la tierra al terminar la cosecha. Bahía Larga: se agradece repartiendo el primer pescado entre las casas que no salieron. Contrasta con el criterio «cómo se agradece».", ["En Cerro Alegre se agradece con palabras de una persona mayor.", "En Bahía Larga se agradece repartiendo.", "Semejanza: en ambas hay gratitud. Diferencia: el modo."], "Ambas muestran gratitud; una la expresa con palabras y la otra, repartiendo alimento. No se dice cuál es mejor."),
        W("Corregir un juicio", "Un niño escribe: «Agradecer repartiendo pescado es más útil que agradecer con palabras». ¿Qué falla?", ["Dice «más útil», que es un orden.", "Las fuentes no comparan su utilidad.", "Hay que describir cómo agradece cada una."], "Falla porque jerarquiza; debe decir cómo agradece cada comunidad."),
    ],
    mistakes=[
        M("Usar palabras como «atrasado» o «avanzado» para hablar de una comunidad.", "Son juicios, no descripciones.", "Describe con las palabras de la fuente."),
        M("Pensar que valorar una cosmovisión obliga a adoptarla.", "Valorar es reconocer su sentido.", "Escribe qué te enseña y qué sigue siendo distinto para ti."),
    ],
    R=[
        ex("Relato inventado: «En Alto Sauce se siembra una chacra común». ¿Qué se hace en común? A) una chacra B) un viaje", "A", "El relato dice chacra común."),
        ex("¿Cómo se llama la manera en que un pueblo entiende el mundo y la vida? A) cosmovisión B) mapa", "A", "Esa es la definición de cosmovisión."),
        ex("En Bahía Larga se reparte el primer pescado. ¿Entre quiénes? A) entre las casas que no pudieron salir B) entre los turistas", "A", "El relato lo dice así."),
    ],
    C=[
        vf("contrastar dos relatos significa decidir cuál comunidad es mejor.", False, "Contrastar es ver semejanzas y diferencias."),
        ab("¿Qué palabra evitas al contrastar sin jerarquizar?", "«atrasado»", "«en cambio»", "«Atrasado» es un juicio; «en cambio» marca diferencia."),
        vf("valorar una cosmovisión significa reconocer que tiene sentido para quienes la viven.", True, "Valorar es reconocer su sentido sin imponerlo ni rechazarlo."),
    ],
    A=[
        ex("Criterio «qué se comparte». Alto Sauce: semillas. Rincón Alto: comida. ¿Qué escribes como diferencia? A) en una se comparten semillas y en la otra comida B) una comunidad es más generosa", "A", "La diferencia se describe sin juicio."),
        ex("Clasifica en DESCRIPCIÓN o JUICIO: a) la comunidad reparte el primer pescado b) la comunidad es más atrasada que la de la ciudad.", "a descripción, b juicio", "La primera dice lo que hacen; la segunda ordena sin fundamento."),
        ex("Completa con una semejanza: «Alto Sauce y Rincón Alto se parecen porque en ambas las familias…»", "Comparten algo", "Ambos relatos muestran que las familias comparten."),
    ],
    Z=[
        ex("Lucas escribe: «El agradecimiento de Cerro Alegre es el verdadero y el de Bahía Larga no». ¿Qué error comete?", "Jerarquiza dos formas de agradecer", "Ninguna fuente dice que una sea la verdadera."),
        ex("Un compañero dice que, para valorar el relato, hay que creer lo mismo que la comunidad. ¿Es correcto? A) no, valorar es reconocer su sentido y aprender B) sí, hay que adoptar su cosmovisión", "A", "Valorar no obliga a adoptar."),
    ],
    D=[
        ex("Dos frases sobre agradecer: Una: «Cerro Alegre agradece con palabras; Bahía Larga, repartiendo alimento». Otra: «Bahía Larga agradece mejor porque reparte». ¿Cuál contrasta sin jerarquizar?", "La primera", "La segunda ordena con la palabra «mejor»."),
        ex("Te piden comparar tres comunidades, pero solo tienes la ficha de dos. ¿Qué haces? A) comparo las dos que tengo y aviso que falta la tercera B) invento la tercera", "A", "No se inventa una comunidad sin su fuente."),
    ],
    context=[ab("En clases, un compañero dice que los eventos que usan canto son más importantes que los que usan comida. ¿Qué le respondes?", "que cada comunidad vive el suyo a su manera y no se ordenan", "que tiene razón porque el canto es más antiguo", "No hay una fuente que ordene los eventos.")],
    selfcheck=[
        ex("Escribe una palabra que sí puedes usar para contrastar sin jerarquizar.", "En cambio, semejanza, diferencia o también", "Marcan diferencia o semejanza sin ordenar."),
        vf("al contrastar dos comunidades uso criterios distintos para cada una.", False, "Los criterios deben ser los mismos."),
        ex("¿Qué escribes si no sabes por qué una comunidad hace algo? A) no lo sé, se lo preguntaría al educador B) lo invento", "A", "Declarar lo que no sé evita inventar."),
    ],
    task=T("Lee dos relatos inventados. Costa Mansa (don Patricio): «Las familias bajan juntas a la orilla al amanecer de la cosecha del alga y los jóvenes cargan los canastos de los mayores». Quebrada Seca (doña Marisol): «Antes de partir al cerro, cada persona lleva un poco de agua para otra y se despide de las casas». Escribe un contraste con el criterio «cómo se cuida a otras personas» y una frase que empiece con «Valoro que…». No uses las palabras «mejor» ni «peor».",
           "Costa Mansa: los jóvenes cargan los canastos de los mayores. Quebrada Seca: cada persona lleva agua para otra. Semejanza: en ambas se cuida a otras personas. Diferencia: una lo hace con trabajo y la otra con agua. Valoro que en los dos relatos las personas se ayuden.",
           ["usa el mismo criterio con ambos relatos", "escribe semejanza y diferencia", "evita «mejor» y «peor»", "valora con una razón"], ["contraste escrito", "frase con «Valoro que…»"], ["jerarquizar", "inventar datos"],
           "Pedir que señale en el relato cada dato; valorar que valore sin ordenar."),
    reinforce="Cambia en un contraste las palabras «mejor» y «peor» por descripciones de lo que hace cada comunidad.",
    extend="Explica con tus palabras por qué valorar una cosmovisión distinta no obliga a pensar igual.",
)

L(
    LF1, 6, materials=MAT,
    use="Aprenderé a comunicar mi trabajo sobre la historia de un evento de otro pueblo y a pedir su validación al educador o a la comunidad. Sirve para compartir con respeto y corregir a tiempo.",
    prior=["Sé dar una opinión fundamentada y atribuida.", "Sé contrastar sin jerarquizar."],
    explain=[
        "Comunicar lo aprendido es contar a otros, de forma clara y respetuosa, la historia que leímos. Para que sea respetuosa, el trabajo debe tener cuatro cosas: quién cuenta (la fuente), de qué comunidad es, qué dice el relato y qué límite se respetó. Después viene una cosa más importante: la validación.",
        "Validar es mostrar el trabajo al educador o a la educadora tradicional, o a la comunidad, para que digan si algo está mal, incompleto o no debería compartirse. Se pide con una frase amable: «¿Puede revisar si lo que escribí es correcto?». Si corrigen algo, se agradece y se cambia el trabajo.",
        "Si el educador o la comunidad dicen que una parte no debe mostrarse, se quita sin discutir. Es mejor un trabajo más corto y respetuoso que uno completo con una parte indebida. Al final se hace la devolución: se agradece y se muestra la versión corregida.",
    ],
    vocab=[("validar", "pedir a quien sabe que revise si el trabajo es correcto y respetuoso"), ("devolución", "mostrar a la fuente el trabajo terminado y agradecer"), ("comunicar", "contar a otros lo aprendido de forma clara"), ("reservado", "que la comunidad prefiere no compartir"), ("agradecer", "reconocer lo que otra persona nos dio")],
    worked=[
        W("Revisar un trabajo antes de compartir", "Un grupo prepara un cartel sobre Bahía Larga. Tiene: título, nombre de don Ignacio como fuente, un resumen del relato y la frase reservada de despedida. ¿Qué cambias antes de mostrarlo?", ["El título, la fuente y el resumen están bien.", "La frase reservada no puede mostrarse.", "Quito esa frase y pido validación del cartel."], "Se quita la frase reservada y se pide validación antes de mostrar el cartel."),
        W("Pedir validación", "Escribe una frase para pedir validación al educador tradicional.", ["Saludo con respeto.", "Digo qué trabajo hice.", "Pido que revise si es correcto y respetuoso."], "«Mari mari, educador. Hice este trabajo sobre el relato de Bahía Larga. ¿Puede revisar si es correcto y respetuoso?»"),
    ],
    mistakes=[
        M("Mostrar el trabajo en público antes de que lo revise la comunidad.", "Puede tener errores o partes que no se deben compartir.", "Pide validación antes."),
        M("Discutir cuando el educador pide quitar una parte.", "Quien sabe decide qué se comparte.", "Quita la parte y agradece."),
    ],
    R=[
        ex("¿Qué significa validar un trabajo? A) pedir a quien sabe que lo revise B) ponerle una nota", "A", "Validar es pedir revisión a la fuente o al educador."),
        ex("¿A quién le muestras primero un trabajo sobre una cultura? A) al educador tradicional o a la comunidad B) solo a tus amigos", "A", "Ellos pueden revisar lo que dices sobre su cultura."),
        ex("Si el educador dice «esa parte no se muestra», ¿qué haces? A) la quito B) la dejo igual", "A", "Se respeta lo que la comunidad pide no mostrar."),
    ],
    C=[
        vf("un trabajo respetuoso lleva el nombre de la fuente y el límite que se respetó.", True, "Atribuir y declarar límites es parte de respetar."),
        vf("si el educador pide quitar una parte, conviene discutir hasta convencerlo.", False, "Quien sabe decide qué se comparte; se quita y se agradece."),
        ab("¿Qué es la devolución?", "mostrar a la fuente el trabajo terminado y agradecer", "vender el trabajo", "La devolución es una forma de agradecer y cerrar el trabajo."),
    ],
    A=[
        ex("Cartel de un grupo: título, nombre de la fuente, resumen del relato, dibujo del lugar reservado. ¿Qué parte quitas? ", "El dibujo del lugar reservado", "Lo reservado no se muestra."),
        ex("Ordena los pasos: 1) corregir con lo que dijo el educador 2) hacer el trabajo 3) pedir validación 4) agradecer. Escribe el orden con los números.", "2, 3, 1, 4", "Primero se hace, luego se valida, se corrige y se agradece."),
        ex("Una frase para pedir validación empieza con un saludo. ¿Cuál de estas sirve? A) «Mari mari, ¿puede revisar mi trabajo?» B) «Entrégueme mi nota»", "A", "Incluye saludo y pide revisión con respeto."),
    ],
    Z=[
        ex("Un grupo dice: «Nuestro trabajo está perfecto, no necesita validación». ¿Qué le falta? A) pedir revisión a quien sabe de la cultura B) más colores", "A", "Nadie debe dar por perfecto un trabajo sobre la cultura de otros sin revisión."),
        ex("Una niña quita una parte del cartel porque la comunidad lo pidió y el cartel queda más corto. ¿Perdió valor el trabajo?", "No", "Un trabajo respetuoso vale más que uno completo con una parte indebida."),
    ],
    D=[
        ex("Dos carteles sobre el mismo relato: Uno tiene fuente, límite y validación. Otro es más largo pero sin fuente ni validación. ¿Cuál comunica con más respeto?", "El primero", "Tiene lo que pide un trabajo respetuoso."),
        ex("El educador sugiere cambiar una frase de tu cartel. Tú crees que está bien. ¿Qué haces? A) la cambio y le agradezco B) la dejo porque yo lo escribí", "A", "El educador conoce su cultura mejor que tú."),
    ],
    context=[ab("Tu curso organiza una muestra para las familias con trabajos sobre relatos de otros pueblos. ¿Qué conviene antes?", "que cada trabajo sea revisado por el educador o la comunidad", "colgar todo sin revisar", "Revisar evita errores y respeta lo reservado.")],
    selfcheck=[
        ex("Nombra las cuatro cosas que debe tener un trabajo respetuoso.", "Fuente, comunidad, lo que dice el relato y el límite", "Son los datos que permiten comunicar con respeto."),
        vf("después de validar, se agradece y se muestra la versión corregida.", True, "Esa es la devolución."),
        ex("¿Qué haces si una parte del trabajo no se debe compartir? A) la quito B) la escondo en una esquina", "A", "No se comparte y no se deja escondida."),
    ],
    task=T("Con el relato de Costa Mansa de la clase 4 (don Patricio), prepara un mini cartel con: título, fuente, comunidad, dos datos del relato, un límite y tu opinión fundamentada en una frase. Escribe además la frase con la que pedirías validación al educador o a la educadora tradicional.",
           "Título: La cosecha del alga en Costa Mansa (relato inventado). Fuente: don Patricio. Datos: las familias bajan juntas a la orilla; los jóvenes cargan los canastos. Límite: no se cuenta la oración. Opino que es un evento de respeto porque los jóvenes ayudan a los mayores. Validación: «¿Puede revisar si lo que escribí es correcto y respetuoso?»",
           ["incluye fuente, comunidad, datos y límite", "opinión con razón", "frase de validación"], ["cartel escrito", "frase de validación"], ["incluir la parte reservada", "omitir la fuente"],
           "Pedir que señale dónde aparece cada elemento; valorar que la frase de validación sea respetuosa."),
    reinforce="Haz una lista de verificación con los cuatro datos que debe tener un trabajo respetuoso y revisa tu cartel con ella.",
    extend="Escribe cómo agradecerías al educador o educadora tradicional después de que revise tu trabajo.",
)

# ============================================================ OA LF02 · Exposición y diálogo oral
VF2 = "Ficha situada (inventada). Comunidad: Valle Seco (no es un pueblo real). Tema que se puede exponer: el trabajo del riego comunitario. Fuente: doña Natalia, vecina. Permiso: doña Natalia autorizó usar sus palabras en la escuela. Límite: no se expone dónde se guarda el registro de turnos del agua."

L(
    LF2, 1, materials=MAT,
    use="Aprenderé a preparar una exposición oral situando el tema: de qué comunidad es, quién lo cuenta, qué se puede decir y qué no. Sirve para analizar aspectos de una cultura sin hablar por otros.",
    prior=["Sé situar un evento con su ficha.", "Sé que lo que se dice en la lengua lo enseña el educador o la educadora tradicional."],
    explain=[
        "Una exposición oral es una presentación en que una persona explica un tema a otras. Un diálogo es una conversación en que dos o más personas se turnan para hablar y escuchar. En ambos, el análisis consiste en separar un tema en partes y explicar cada una: qué es, cómo ocurre y qué significa para las personas.",
        "Los aspectos socioculturales son los que tienen que ver con la vida en común: cómo se organiza el trabajo, cómo se reparten las tareas, cómo se cuida el lugar. Los aspectos espirituales tienen que ver con lo que la comunidad considera sagrado. De estos últimos solo se expone lo que la comunidad autoriza.",
        "Antes de hablar, situamos el tema con una ficha: comunidad, tema, fuente, permiso y límite. Luego definimos para quién hablamos, porque no es lo mismo exponer a mis compañeros que conversar con una autoridad tradicional. Las palabras en la lengua indígena y su pronunciación las enseña el educador o la educadora tradicional.",
    ],
    vocab=[("exposición oral", "presentación en que una persona explica un tema a otras"), ("diálogo", "conversación en que las personas se turnan para hablar y escuchar"), ("análisis", "separar un tema en partes y explicar cada una"), ("aspecto sociocultural", "parte de la vida en común, como el trabajo o el cuidado del lugar"), ("audiencia", "las personas que escuchan una exposición")],
    worked=[
        W("Situar un tema de exposición", VF2 + " ¿De qué se puede hablar y qué queda fuera?", ["El tema autorizado es el trabajo del riego comunitario.", "La fuente es doña Natalia y dio permiso.", "El registro de turnos del agua no se expone."], "Se puede exponer el trabajo del riego comunitario según doña Natalia; no se expone dónde se guarda el registro de turnos."),
        W("Analizar un tema en partes", "Tema: el trabajo del riego comunitario. Sepáralo en tres partes para una exposición de 3 minutos.", ["Parte 1: qué es el riego comunitario.", "Parte 2: cómo se organizan los turnos.", "Parte 3: qué significa para la comunidad, según la fuente."], "Tres partes: qué es, cómo se organiza y qué significa para la comunidad."),
    ],
    mistakes=[
        M("Hablar de «los pueblos indígenas» como si fueran uno solo.", "Cada pueblo y cada comunidad tienen su propia forma de vivir.", "Nombra la comunidad y la fuente."),
        M("Exponer una parte reservada porque «es interesante».", "El interés no da permiso.", "Respeta el límite de la ficha."),
    ],
    R=[
        ex("Ficha: «Comunidad: Lago Espejo. Tema: la pesca en bote pequeño. Fuente: don Teodoro.» ¿Quién es la fuente?", "Don Teodoro", "La ficha lo nombra como fuente."),
        ex("¿Una exposición oral la hace una persona o dos que se turnan? Responde «una» o «dos».", "Una", "En una exposición una persona explica el tema; en un diálogo se turnan."),
        ex("La ficha dice «Límite: no se expone dónde están los lugares de respeto». ¿Los mencionas en tu exposición? Sí o No.", "No", "El límite lo prohíbe."),
    ],
    C=[
        vf("analizar un tema es separarlo en partes y explicar cada una.", True, "Esa es la definición de análisis."),
        ab("¿Cuál es un aspecto sociocultural?", "cómo una comunidad organiza el trabajo del riego", "el color de tu lápiz", "El trabajo en común es parte de la vida de la comunidad."),
        vf("de los aspectos espirituales se puede exponer todo lo que uno encuentre.", False, "Solo se expone lo que la comunidad autoriza."),
    ],
    A=[
        ex("Una ficha trae comunidad y tema, pero no fuente ni permiso. ¿Qué haces primero? A) pido esos datos antes de exponer B) expongo igual", "A", "Sin fuente ni permiso se detiene la actividad."),
        ex("Clasifica en TEMA, FUENTE o LÍMITE: a) don Teodoro b) la pesca en bote pequeño c) no se exponen los lugares de respeto.", "a fuente, b tema, c límite", "Cada dato cumple un papel distinto en la ficha."),
        ex("Tema: la pesca en bote pequeño en Lago Espejo. Si lo dividieras en tres partes, ¿cuál sirve como segunda? A) cómo se organiza la salida de los botes B) un chiste sobre peces", "A", "Una parte de análisis explica cómo ocurre."),
    ],
    Z=[
        ex("Julián va a exponer ante sus compañeros y ante una autoridad tradicional, y piensa hablar igual con ambos. ¿Qué debería considerar? A) la audiencia, porque cambia la manera de hablar B) nada", "A", "La audiencia influye en cómo se habla."),
        ex("Ana dice: «Expongo todo lo que sé de la comunidad porque lo vi en un video». ¿Qué falta? A) fuente, permiso y límites B) más imágenes", "A", "Un video no reemplaza la autorización de la comunidad."),
    ],
    D=[
        ex("Dos tarjetas: Una dice «Comunidad: Lago Espejo, fuente don Teodoro, permiso sí». Otra dice «Comunidad: Río Claro, fuente doña Lucía, permiso no dice». ¿Con cuál puedes preparar una exposición ahora?", "Con la de Lago Espejo", "La de Río Claro no tiene permiso."),
        ex("Un tema de exposición es demasiado grande para 3 minutos. ¿Qué haces? A) elijo una parte autorizada del tema B) hablo más rápido", "A", "Mejor una parte clara que todo apurado."),
    ],
    context=[ab("Tu curso quiere invitar a un adulto de la comunidad a una exposición. ¿Qué conviene preparar antes?", "la ficha con tema, fuente, permiso y límite", "solo un afiche llamativo", "Con la ficha se sabe de qué se puede hablar.")],
    selfcheck=[
        ex("Nombra los cinco datos de una ficha situada.", "Comunidad, tema, fuente, permiso y límite", "Son los datos de la ficha."),
        vf("la audiencia influye en cómo preparo una exposición.", True, "No se habla igual a un compañero que a una autoridad tradicional."),
        ex("¿Quién enseña cómo se pronuncia una palabra en la lengua indígena de mi comunidad? A) el educador o la educadora tradicional B) un buscador de internet", "A", "La pronunciación se aprende de quien habla la lengua."),
    ],
    task=T("Lee esta ficha inventada y haz el plan de una exposición de 3 minutos: Comunidad: Lago Espejo. Tema: la pesca en bote pequeño. Fuente: don Teodoro, que cuenta que los botes salen de a dos personas y que las redes se arreglan entre todos los días de calma. Permiso: sí. Límite: no se exponen los lugares de respeto del lago. Escribe: a quién va dirigida la exposición, tres partes del análisis y qué dejarías fuera.",
           "Audiencia: mis compañeros. Parte 1: qué es la pesca en bote pequeño. Parte 2: cómo se organizan (salen de a dos y arreglan redes entre todos). Parte 3: qué significa, según don Teodoro, trabajar en común. Fuera: los lugares de respeto del lago.",
           ["identifica audiencia", "divide el tema en tres partes", "respeta el límite"], ["plan escrito", "lista de lo que queda fuera"], ["exponer lo reservado", "no atribuir a la fuente"],
           "Pedir que señale en la ficha de dónde sale cada parte; valorar que deje fuera lo reservado."),
    reinforce="Subraya en la ficha de Valle Seco el tema, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica por qué la audiencia cambia la forma de preparar una exposición.",
)

L(
    LF2, 2, materials=MAT,
    use="Aprenderé a escuchar una exposición y tomar notas con límites declarados: qué dijo la fuente, qué entendí yo y qué no se explicó. Sirve para preparar buenas preguntas en un diálogo.",
    prior=["Sé situar un tema con su ficha.", "Sé separar lo que dice la fuente de lo que interpreto."],
    explain=[
        "Escuchar bien una exposición no es solo oír. Es seguir las ideas, anotar las palabras clave y distinguir tres cosas: lo que la persona dijo, lo que yo entendí por mi cuenta y lo que no se explicó. Con esas notas puedo después hacer preguntas útiles.",
        "Las palabras clave son las que sostienen la idea principal. En una exposición sobre el riego comunitario, por ejemplo, «turnos», «acequia» y «familias» son palabras clave. Se anotan con letras claras, sin copiar frases enteras. Si aparece una palabra en lengua indígena, se escribe tal como la dice el educador o la educadora y se pregunta cómo se pronuncia.",
        "Un buen oyente también respeta los silencios. Si quien expone dice «esto es solo de la comunidad», no insiste ni pregunta por esa parte. Anota «reservado» y sigue. Las preguntas se formulan para entender mejor lo que sí se contó.",
    ],
    vocab=[("palabra clave", "palabra que sostiene la idea principal"), ("tomar notas", "anotar lo importante mientras se escucha"), ("idea principal", "lo más importante que se dice en una exposición"), ("reservado", "que la comunidad prefiere no compartir"), ("pregunta de comprensión", "pregunta para entender mejor lo que se contó")],
    worked=[
        W("Tomar notas", "Exposición inventada de doña Natalia, de Valle Seco, leída por una persona adulta: «Las familias de Valle Seco se turnan para abrir el agua de la acequia. Cada turno dura una mañana. Hay un registro de turnos que solo guarda la comunidad». Anota las palabras clave y los límites.", ["Palabras clave: familias, turnos, acequia, mañana.", "Idea principal: el agua se reparte por turnos.", "Reservado: el registro de turnos."], "Claves: familias, turnos, acequia. Idea: el agua se reparte por turnos. Reservado: el registro de turnos."),
        W("Formular una pregunta de comprensión", "Con las notas anteriores, escribe una pregunta que no insista en lo reservado.", ["Elijo algo que sí se contó: cada turno dura una mañana.", "Pregunto por el cómo, no por lo reservado.", "Pregunta: ¿cómo se avisa a la familia que le toca el turno?"], "«¿Cómo se avisa a la familia que le toca el turno?» pregunta por lo contado y no por lo reservado."),
    ],
    mistakes=[
        M("Anotar todo, palabra por palabra.", "Se pierde el hilo de la idea principal.", "Anota solo palabras clave."),
        M("Insistir en preguntas sobre lo que la persona dijo que era reservado.", "No respeta el límite.", "Pregunta por lo contado."),
    ],
    R=[
        ex("Exposición leída: «Las familias de Valle Seco se turnan para abrir el agua de la acequia. Cada turno dura una mañana». ¿Cuánto dura cada turno de agua? A) una mañana B) una semana", "A", "La exposición dice una mañana."),
        ex("Exposición leída: «Las familias de Valle Seco se turnan para abrir el agua de la acequia». ¿Quiénes se turnan? A) las familias B) los profesores", "A", "Las familias se turnan para abrir el agua."),
        ex("¿Qué se anota en las notas: palabras clave o frases completas? Responde «palabras clave» o «frases completas».", "Palabras clave", "Así no se pierde el hilo."),
    ],
    C=[
        vf("una persona que escucha bien respeta cuando dicen que algo es solo de la comunidad.", True, "Respetar lo reservado es parte de escuchar."),
        ab("¿Qué es la idea principal?", "lo más importante que se dice", "el último dato", "La idea principal sostiene toda la exposición."),
        vf("las palabras en lengua indígena que escucho las escribo como me parezca.", False, "Se escriben como indique el educador o la educadora."),
    ],
    A=[
        ex("Exposición leída: «Los botes salen de a dos. Las redes se arreglan entre todos los días de calma. Los lugares de respeto del lago no se muestran». ¿Cuáles son dos palabras clave? A) botes y redes B) ayer y mañana", "A", "Son los elementos que sostienen la exposición; «lugares de respeto» queda reservado."),
        ex("Exposición leída: «Los botes salen de a dos». Escribe la idea principal en cinco palabras o menos.", "Los botes salen de a dos (o una frase equivalente)", "Es la idea que contiene el dato."),
        ex("Exposición leída: «Los botes salen de a dos. Las redes se arreglan entre todos los días de calma. Los lugares de respeto del lago no se muestran». ¿Qué anotas como «reservado»? A) los lugares de respeto B) las redes", "A", "Es lo que la exposición dice que no se muestra."),
    ],
    Z=[
        ex("Camilo pregunta tres veces por los lugares de respeto del lago, aunque la exposición dijo que no se cuentan. ¿Qué error comete?", "No respeta el límite declarado", "El límite pide no insistir."),
        ex("Beatriz anotó «las redes se arreglan en calma» y «seguro es una ceremonia». ¿Cuál es una interpretación suya? A) la segunda B) la primera", "A", "La exposición no dijo que sea una ceremonia."),
    ],
    D=[
        ex("Una exposición sobre el lago dijo: «Los botes salen de a dos. Los lugares de respeto del lago no se cuentan». Lee estas dos preguntas posteriores: Una: «¿Cuántos botes salen cada día de calma?». Otra: «¿Dónde están exactamente los lugares de respeto?». ¿Cuál es adecuada?", "La primera", "La segunda pregunta por lo reservado."),
        ex("Un oyente anotó solo la mitad de la exposición porque copió frases completas. ¿Qué técnica le falta? A) anotar palabras clave B) escribir más rápido", "A", "Las palabras clave resumen sin perder el hilo."),
    ],
    context=[ab("En un diálogo después de la exposición, una compañera pregunta algo que la persona dijo que era reservado. ¿Qué haces?", "sugiero preguntar por lo que sí se contó", "la apoyo para que insista", "Se respeta el límite declarado.")],
    selfcheck=[
        ex("Nombra las tres cosas que distingo al escuchar una exposición.", "Lo que dijo la fuente, lo que entendí yo y lo que no se explicó", "Son las tres notas del oyente."),
        vf("si escucho una palabra en lengua indígena, pregunto cómo se pronuncia.", True, "El educador o la comunidad enseñan la pronunciación."),
        ex("Escribe una pregunta de comprensión sobre una exposición de turnos de agua.", "¿Cómo se avisa a cada familia su turno?", "Pregunta por algo contado."),
    ],
    task=T("Pide a una persona de tu casa que te lea en voz alta este texto inventado de don Teodoro, de Lago Espejo: «Los botes salen de a dos personas. Una rema y la otra vigila las redes. Cuando termina el día, se reparte lo pescado entre las casas de la orilla. Hay un lugar del lago que la comunidad cuida en silencio.» Mientras escuchas, anota palabras clave, la idea principal, lo reservado y una pregunta de comprensión.",
           "Claves: botes, de a dos, redes, reparto. Idea principal: se pesca en pareja y se reparte. Reservado: el lugar del lago. Pregunta: ¿cómo se decide a qué casas llega cada parte?",
           ["anota palabras clave", "identifica lo reservado", "formula una pregunta de comprensión"], ["notas escritas", "pregunta"], ["copiar frases enteras", "preguntar por lo reservado"],
           "Pedir que muestre dónde apareció cada dato en la lectura; valorar que respete lo reservado."),
    reinforce="Vuelve a escuchar el texto y subraya con un color las palabras que usaste como clave.",
    extend="Escribe dos preguntas de comprensión distintas sobre la exposición de Valle Seco.",
)

L(
    LF2, 3, materials=MAT,
    use="Aprenderé a elegir un registro formal o no formal según con quién hablo, y a reconocer qué cambia (saludo, trato, vocabulario) sin inventar palabras en lengua indígena. Sirve para exponer y dialogar con respeto.",
    prior=["Sé preparar una exposición situando el tema.", "Sé tomar notas con límites."],
    explain=[
        "El registro es la manera de hablar que elegimos según la situación y la persona. El registro formal se usa con autoridades, personas mayores o en actos públicos: saludamos con respeto, usamos «usted», hablamos con calma y cuidamos el vocabulario. El registro no formal se usa con compañeros y amistades: es más cercano y relajado.",
        "En el diálogo con una autoridad tradicional o con una persona mayor, el registro formal muestra respeto. Un saludo muy conocido en mapuzugun es «mari mari»; sirve para saludar a muchas personas, y cómo se saluda en cada ocasión lo enseña el educador o la educadora. En rapa nui, un saludo conocido es «iorana».",
        "Cambiar de registro no es cambiar de identidad: es adaptar la forma al momento. Para elegir bien, nos preguntamos con quién hablo, dónde estoy y para qué hablo. Con esas tres respuestas decidimos el trato, el tono y el tipo de palabras.",
    ],
    vocab=[("registro formal", "manera respetuosa y cuidada de hablar con autoridades o en actos públicos"), ("registro no formal", "manera cercana de hablar con compañeros y amistades"), ("trato", "manera de dirigirse a alguien, como «tú» o «usted»"), ("mari mari", "saludo muy conocido en mapuzugun"), ("iorana", "saludo muy conocido en rapa nui")],
    worked=[
        W("Elegir el registro", "Situación 1: conversas con tu compañero en el recreo. Situación 2: saludas a una persona mayor de la comunidad que visita tu curso. ¿Qué registro usas en cada una?", ["Pregunto con quién hablo: compañero y persona mayor.", "En el recreo, el trato es cercano: no formal.", "Con la persona mayor, trato respetuoso: formal."], "Situación 1, no formal; situación 2, formal."),
        W("Reescribir en registro formal", "Frase no formal: «Oye, cuéntame cómo hacen el riego». Reescríbela en registro formal para una persona mayor.", ["Cambio «oye» por un saludo respetuoso.", "Cambio «cuéntame» por «¿podría contarme…?».", "Uso «usted»."], "«Buenos días. ¿Podría contarme cómo organizan el riego?»"),
    ],
    mistakes=[
        M("Hablar con la misma manera a todas las personas.", "No se adapta a la situación.", "Pregúntate con quién hablas y dónde estás."),
        M("Pensar que el registro formal es «hablar difícil».", "La formalidad es respeto, no palabras complicadas.", "Usa frases claras con trato respetuoso."),
    ],
    R=[
        ex("¿Qué registro usas con tu mejor amigo en el patio? A) no formal B) formal", "A", "Es una conversación cercana."),
        ex("¿Qué registro usas con una autoridad tradicional que visita tu escuela? A) formal B) no formal", "A", "Se muestra respeto con un trato formal."),
        ex("¿Qué saludo muy conocido en mapuzugun aparece en esta clase?", "Mari mari", "Es el saludo atestiguado de la clase."),
    ],
    C=[
        vf("el registro formal consiste en usar palabras difíciles.", False, "Formal es respetuoso y claro, no difícil."),
        ab("¿Qué tres preguntas ayudan a elegir el registro?", "con quién hablo, dónde estoy y para qué hablo", "qué ropa tengo, qué hora es y cuántos años tengo", "Esas preguntas definen la situación."),
        vf("cambiar de registro significa cambiar de identidad.", False, "Solo adapto la forma al momento."),
    ],
    A=[
        ex("Clasifica en FORMAL o NO FORMAL: a) «Buenas tardes, ¿podría explicarnos?» b) «Oye, ¿me pasas ese lápiz?»", "a formal, b no formal", "La primera tiene saludo y «podría»; la segunda es cercana."),
        ex("Reescribe en registro formal: «Dime qué hacen el domingo». Elige: A) «¿Podría decirme qué hacen el domingo?» B) «Dime rápido qué hacen»", "A", "Lleva el trato respetuoso."),
        ex("Un compañero quiere saludar a una autoridad tradicional con «¿qué onda?». ¿Qué registro usa y cuál sería más adecuado?", "Usa no formal; sería más adecuado el formal", "Con una autoridad se muestra respeto."),
    ],
    Z=[
        ex("Daniela expone ante el curso y ante una persona mayor de la comunidad. Habla relajada y usa bromas. ¿Qué error comete? A) no adapta el registro a la audiencia B) habla demasiado bajo", "A", "Debe cuidar el trato con la persona mayor."),
        ex("Ignacio dice «saludo siempre con ‘mari mari’ y ya sé hablar mapuzugun». ¿Qué tiene de erróneo? A) un saludo no es dominar una lengua B) saludar está prohibido", "A", "Saludar es un paso; la lengua se aprende con el educador."),
    ],
    D=[
        ex("Una exposición se dirige a la comunidad escolar. Dos frases de inicio: Una: «Mari mari, buenos días. Hoy presentaré un tema». Otra: «Ya, empecemos, no importa». ¿Cuál es adecuada?", "La primera", "Tiene saludo respetuoso y presenta el tema."),
        ex("Una persona sabe que va a hablar con una autoridad tradicional. ¿Qué hace antes? A) pregunta cómo saludar y cómo dirigirse B) improvisa", "A", "Quien sabe orienta sobre el saludo y el trato."),
    ],
    context=[ab("Vas a conversar con una persona mayor de la comunidad en una visita a terreno. ¿Cómo inicias?", "con un saludo respetuoso y «usted»", "con una broma", "El respeto se muestra en el trato.")],
    selfcheck=[
        ex("Escribe una diferencia entre el registro formal y el no formal.", "El formal es respetuoso y cuidado; el no formal es cercano y relajado", "Resume la diferencia."),
        vf("«iorana» es un saludo muy conocido en rapa nui.", True, "Está atestiguado como saludo."),
        ex("¿Quién te orienta sobre cómo saludar en la lengua de tu comunidad? A) el educador o la educadora tradicional B) tu imaginación", "A", "Ellos enseñan los saludos."),
    ],
    task=T("Imagina que debes hacer dos intervenciones: una al saludar a una persona mayor que visita tu curso y otra al conversar con tu grupo de trabajo. Escribe cuatro oraciones: dos en registro formal y dos en registro no formal, sobre el mismo tema: cómo organizar una visita a terreno. Marca cuál es cuál y subraya el trato («usted», «tú»).",
           "Formal: «Buenos días. ¿Podría contarnos cómo se organizan las visitas?» y «Le agradecemos que nos reciba». No formal: «Oye, ¿quién lleva las hojas?» y «Yo llevo los lápices». Con el educador pregunto cómo saludar en la lengua.",
           ["escribe dos formales y dos no formales", "subraya el trato", "mantiene el tema"], ["cuatro oraciones marcadas"], ["usar «tú» en la formal", "confundir formal con difícil"],
           "Pedir que explique por qué cada oración es formal o no; valorar el respeto."),
    reinforce="Convierte tres frases no formales en frases formales.",
    extend="Explica con un ejemplo por qué el registro formal es una forma de respeto.",
)

L(
    LF2, 4, materials=MAT,
    use="Aprenderé a construir una exposición oral con inicio, desarrollo y cierre, atribuyendo cada dato y usando énfasis (destacar una palabra). Sirve para que mi exposición se entienda y sea respetuosa.",
    prior=["Sé elegir el registro.", "Sé tomar notas y respetar lo reservado."],
    explain=[
        "Una exposición clara tiene tres momentos. En el inicio saludo, digo mi nombre, presento el tema y nombro la fuente. En el desarrollo explico las partes del tema, una por una, con datos atribuidos: «según doña Natalia…». En el cierre resumo la idea principal, declaro los límites y agradezco a la fuente.",
        "El énfasis es destacar con la voz una palabra o idea importante: se dice un poco más fuerte, más lento o con una pausa antes. Por ejemplo: «Cada turno dura UNA MAÑANA». El énfasis ayuda a que las personas recuerden el dato más importante. Se usa poco: si se destaca todo, no se destaca nada.",
        "La pronunciación de palabras en lengua indígena la enseña el educador o la educadora; ensayamos con él o ella antes de exponer. Hablar con calma, mirar a la audiencia y hacer pausas cortas mejora la comprensión. Una exposición de 3 minutos tiene tiempo para un inicio breve, dos o tres datos y un cierre.",
    ],
    vocab=[("inicio", "momento en que saludo y presento el tema"), ("desarrollo", "momento en que explico las partes del tema"), ("cierre", "momento en que resumo, declaro límites y agradezco"), ("énfasis", "destacar con la voz una palabra o idea importante"), ("pausa", "silencio breve para que se entienda mejor")],
    worked=[
        W("Armar una exposición con tres momentos", "Tema: los turnos de agua de Valle Seco (inventado). Fuente: doña Natalia. Ordena estos enunciados: a) «Cada turno dura una mañana, según doña Natalia» b) «Gracias, doña Natalia, por compartir su experiencia» c) «Mari mari, hoy hablaré de los turnos de agua».", ["El saludo y la presentación van primero: c.", "El dato atribuido va en el desarrollo: a.", "El agradecimiento va al final: b."], "Orden: c, a, b."),
        W("Elegir un énfasis", "Frase: «Los botes salen de a dos personas». ¿Qué palabra destacas para resaltar la idea principal?", ["La idea principal es la cantidad de personas.", "La palabra que lleva esa idea es «dos».", "Digo «dos» más lento y con una pausa antes."], "Destaco «dos»."),
    ],
    mistakes=[
        M("Poner énfasis en todas las palabras.", "Si todo se destaca, nada se destaca.", "Elige una palabra clave por frase importante."),
        M("Olvidar el cierre.", "Sin cierre la audiencia no sabe qué recordar ni si terminó.", "Resume, declara límites y agradece."),
    ],
    R=[
        ex("¿En qué momento de la exposición saludas y presentas el tema? A) en el inicio B) en el cierre", "A", "El inicio es para saludar y presentar."),
        ex("¿En qué momento agradeces a la fuente? A) en el cierre B) en el desarrollo", "A", "El cierre incluye el agradecimiento."),
        ex("¿Qué es el énfasis? A) destacar con la voz una palabra importante B) hablar muy fuerte siempre", "A", "Es destacar solo lo importante."),
    ],
    C=[
        vf("el desarrollo de una exposición incluye los datos atribuidos a la fuente.", True, "En el desarrollo se explican las partes con datos y fuente."),
        vf("conviene poner énfasis en todas las palabras de la frase.", False, "Si todo se destaca, nada se destaca."),
        ab("¿Con quién ensayas la pronunciación de una palabra en lengua indígena?", "con el educador o la educadora tradicional", "con un compañero que la oyó una vez", "Quien enseña la lengua puede corregir la pronunciación."),
    ],
    A=[
        ex("Ordena los momentos poniendo 1, 2 y 3: a) agradezco a la fuente b) saludo y presento el tema c) explico los datos. Escribe el orden de letras.", "b, c, a", "Inicio, desarrollo y cierre."),
        ex("Frase: «Cada familia tiene un turno de UNA MAÑANA». ¿Qué palabras tienen el énfasis? A) una mañana B) cada familia", "A", "Las mayúsculas marcan el énfasis en «una mañana»."),
        ex("Clasifica en INICIO, DESARROLLO o CIERRE: a) «Según don Teodoro, los botes salen de a dos» b) «Muchas gracias por escucharme» c) «Hoy presentaré la pesca en Lago Espejo».", "a desarrollo, b cierre, c inicio", "Cada frase cumple un papel distinto en la exposición."),
    ],
    Z=[
        ex("Sofía termina su exposición diciendo solo «ya». ¿Qué le falta? A) resumen, límites y agradecimiento B) más risas", "A", "El cierre debe incluir esas tres cosas."),
        ex("Un compañero usa énfasis en cada palabra de la frase. ¿Qué consecuencia tiene? A) la audiencia no distingue lo importante B) la audiencia entiende mejor", "A", "Si todo se destaca, nada se destaca."),
    ],
    D=[
        arith("Una exposición dura 3 minutos en total. El inicio usa 30 segundos y el cierre, 30 segundos. ¿Cuántos segundos quedan para el desarrollo? (1 minuto = 60 segundos)", "3*60-30-30", "Se resta el inicio y el cierre del tiempo total.", " segundos"),
        ex("Para una exposición de 3 minutos tienes cuatro datos, pero solo cabe tiempo para tres. ¿Qué haces? A) elijo los tres más importantes y respeto el tiempo B) hablo más rápido", "A", "Elegir y priorizar mantiene la claridad."),
    ],
    context=[ab("Vas a exponer ante tu curso y una visita de la comunidad. ¿Qué ensayas con el educador antes?", "la pronunciación de las palabras en lengua y el saludo", "solo los chistes del inicio", "Esas partes las valida quien enseña la lengua.")],
    selfcheck=[
        ex("Nombra los tres momentos de una exposición.", "Inicio, desarrollo y cierre", "Son las tres partes."),
        vf("el énfasis ayuda a recordar el dato más importante.", True, "Destacar con la voz marca lo principal."),
        ex("¿Qué frase atribuye un dato? A) «Según doña Natalia, el turno dura una mañana» B) «Dicen que el turno dura una mañana»", "A", "Nombra a la fuente."),
    ],
    task=T("Con este texto inventado de doña Natalia, de Valle Seco: «Las familias se turnan para abrir el agua. Cada turno dura una mañana. Después, la familia avisa a la siguiente.» Escribe el guion de una exposición de 1 minuto con inicio, desarrollo y cierre. Marca con mayúsculas una palabra de énfasis en el desarrollo y anota una pausa con (…). Ensaya en voz alta con una persona de tu casa.",
           "Inicio: Mari mari, hoy hablaré de los turnos de agua. Desarrollo: Según doña Natalia, cada turno dura UNA MAÑANA (…) y después la familia avisa a la siguiente. Cierre: Gracias, doña Natalia, por compartir. Límite: no sé cómo se registra el turno.",
           ["tiene inicio, desarrollo y cierre", "atribuye a la fuente", "marca énfasis y pausa"], ["guion escrito", "ensayo en voz alta"], ["olvidar el cierre", "destacar todas las palabras"],
           "Pedir que lea en voz alta y señale el énfasis; valorar la atribución."),
    reinforce="Marca con tres colores el inicio, el desarrollo y el cierre de tu guion.",
    extend="Escribe un segundo cierre distinto para tu exposición, que declare un límite y agradezca.",
)

L(
    LF2, 5, materials=MAT,
    use="Aprenderé a dialogar a partir de dos exposiciones de comunidades distintas, preguntando para comprender y comparando sin jerarquizar. Sirve para conversar con respeto entre culturas.",
    prior=["Sé armar una exposición con inicio, desarrollo y cierre.", "Sé contrastar sin jerarquizar."],
    explain=[
        "Un diálogo se construye entre varias personas que se turnan. Cada una escucha, responde y pregunta. Para que sea respetuoso, hay reglas simples: no interrumpir, esperar el turno, mirar a quien habla y preguntar para entender, no para corregir. Cuando algo no queda claro, se dice «¿puedes explicar eso un poco más?».",
        "Dialogar sobre dos exposiciones de comunidades distintas permite comparar. Usamos los mismos criterios: qué hace cada comunidad, con quién lo hace y para qué. Anotamos semejanzas y diferencias. Evitamos frases como «ellos lo hacen mejor» y usamos frases como «en cambio» o «a diferencia de».",
        "Al final del diálogo conviene resumir lo que cada persona aportó. Se puede decir: «Según la primera exposición…, según la segunda…». Así reconocemos cada voz. Si surge algo que no sabemos, anotamos la duda para llevarla al educador o a la educadora tradicional.",
    ],
    vocab=[("turno", "momento que le corresponde hablar a cada persona"), ("interrumpir", "hablar cuando otra persona todavía no termina"), ("pregunta para comprender", "pregunta que busca entender mejor, no corregir"), ("a diferencia de", "expresión que marca una diferencia sin ordenar"), ("aportar", "dar una idea o un dato a la conversación")],
    worked=[
        W("Preguntar para comprender", "Exposición A (Valle Seco): «Cada turno de agua dura una mañana». Exposición B (Lago Espejo): «Los botes salen de a dos». Escribe una pregunta para comprender sobre A.", ["Elijo un dato contado: el turno dura una mañana.", "Pregunto por el cómo: ¿cómo saben cuándo termina el turno?", "No pido ni corrijo."], "«¿Cómo saben cuándo termina el turno?»"),
        W("Comparar sin jerarquizar", "Compara A y B con el criterio «cómo se organiza el trabajo».", ["A: las familias se turnan.", "B: los botes salen de a dos.", "Semejanza: en ambas se trabaja de manera organizada. Diferencia: uno por turnos y otro por parejas."], "Ambas se organizan; una por turnos y la otra por parejas. No se dice cuál es mejor."),
    ],
    mistakes=[
        M("Interrumpir a quien habla porque ya sé lo que dirá.", "Rompe el diálogo y no respeta el turno.", "Espera, anota y pregunta al final."),
        M("Preguntar para demostrar que la otra persona se equivoca.", "El diálogo busca comprender.", "Formula la pregunta con «¿cómo…?» o «¿puedes explicar…?»."),
    ],
    R=[
        ex("En un diálogo, ¿cuándo hablas? A) en mi turno B) cuando quiera, aunque interrumpa", "A", "Se respeta el turno."),
        ex("¿Qué expresión marca una diferencia sin ordenar? A) «a diferencia de» B) «es mejor que»", "A", "Marca la diferencia."),
        ex("Si algo no quedó claro, ¿qué dices? A) «¿puedes explicar eso un poco más?» B) «no entendiste»", "A", "Pide ayuda con respeto."),
    ],
    C=[
        vf("preguntar para comprender es lo mismo que preguntar para corregir.", False, "Una busca entender; la otra, mostrar un error."),
        ab("¿Qué hace un buen participante de un diálogo?", "escucha, espera su turno y pregunta", "habla más fuerte que los demás", "Esas conductas hacen respetuoso el diálogo."),
        vf("al final de un diálogo conviene resumir lo que cada persona aportó.", True, "Reconoce cada voz."),
    ],
    A=[
        ex("Exposición C (Costa Mansa): «Los jóvenes cargan los canastos». Escribe una pregunta para comprender, elige: A) «¿Cómo se organizan los jóvenes para cargarlos?» B) «¿Por qué lo hacen mal?»", "A", "Pregunta por el cómo y sin juicio."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) en ambas comunidades se trabaja entre varios b) una usa turnos y otra, parejas.", "a semejanza, b diferencia", "La primera es común; la segunda marca algo distinto."),
        ex("Resume con «según…»: Valle Seco, turnos de agua; Lago Espejo, botes de a dos. Completa: «Según doña Natalia, el agua se reparte por…»", "Turnos", "Es lo que dice la exposición A."),
    ],
    Z=[
        ex("En un diálogo, Pablo dice: «La comunidad de Lago Espejo trabaja mejor porque es de a dos». ¿Qué error comete?", "Jerarquiza sin fundamento", "La exposición no compara quién trabaja mejor."),
        ex("María siempre habla primero y no deja que otros terminen. ¿Qué regla rompe? A) respetar los turnos B) usar el registro formal", "A", "Interrumpir rompe el turno."),
    ],
    D=[
        ex("En el diálogo salió una duda: ¿por qué los turnos duran una mañana? Nadie lo sabe. ¿Qué hacen? A) anotan la duda para el educador o la comunidad B) la inventan", "A", "Las dudas culturales se consultan."),
        ex("Dos resúmenes del diálogo: Uno: «Según doña Natalia, hay turnos; según don Teodoro, hay parejas». Otro: «Los dos pueblos son iguales». ¿Cuál reconoce cada voz?", "El primero", "El segundo mezcla y generaliza."),
    ],
    context=[ab("En una asamblea escolar dos grupos exponen comunidades distintas. Una compañera propone votar cuál comunidad es mejor. ¿Qué respondes?", "que no se vota, porque se dialoga para comprender", "que votemos rápido", "Dialogar no es competir.")],
    selfcheck=[
        ex("Escribe una regla del diálogo respetuoso.", "No interrumpir y esperar el turno", "Son reglas de conversación respetuosa."),
        vf("una pregunta para comprender empieza buscando corregir.", False, "Comprender no es corregir."),
        ex("¿Qué haces con una duda que nadie puede responder? A) la anoto y la llevo al educador o a la comunidad B) la invento", "A", "Ellos son la fuente."),
    ],
    task=T("Dialoga con una persona de tu casa a partir de estas dos mini exposiciones inventadas. A (Valle Seco, doña Natalia): «Las familias se turnan para abrir el agua; cada turno dura una mañana». B (Lago Espejo, don Teodoro): «Los botes salen de a dos y lo pescado se reparte entre las casas de la orilla». Escribe tres preguntas para comprender (dos para A y una para B), una semejanza y una diferencia con los mismos criterios, y un resumen que empiece con «Según…».",
           "Preguntas: ¿cómo avisan el siguiente turno?; ¿qué hacen en el turno?; ¿cómo deciden qué casa recibe cada parte? Semejanza: ambas organizan el trabajo. Diferencia: una por turnos, otra por parejas. Resumen: Según doña Natalia, hay turnos; según don Teodoro, los botes salen de a dos.",
           ["formula preguntas para comprender", "compara con los mismos criterios", "resume con atribución"], ["tres preguntas", "semejanza y diferencia", "resumen"], ["preguntar para corregir", "jerarquizar"],
           "Pedir que explique por qué cada pregunta busca comprender; valorar el resumen atribuido."),
    reinforce="Cambia dos preguntas que buscan corregir por preguntas que buscan comprender.",
    extend="Escribe cinco frases que sirvan para pedir la palabra y esperar tu turno con respeto.",
)

L(
    LF2, 6, materials=MAT,
    use="Aprenderé a ensayar y presentar una exposición con criterios claros y a pedir validación al educador o a la comunidad. Sirve para exponer con calidad y respeto.",
    prior=["Sé armar una exposición y dialogar.", "Sé que la pronunciación en lengua la valida el educador."],
    explain=[
        "Antes de presentar, ensayamos. El ensayo permite comprobar cuatro criterios: claridad (se entiende lo que digo), volumen y ritmo (ni muy bajo ni muy rápido), atribución (nombro a la fuente) y respeto de los límites (no cuento lo reservado). Cada criterio vale hasta 3 puntos, así que una exposición puede sumar hasta 12 puntos.",
        "Después del ensayo pedimos retroalimentación: una persona escucha y dice qué estuvo bien y qué se puede mejorar, siempre con ejemplos. La retroalimentación no es un reto, es una ayuda. Con ella corregimos el guion y volvemos a ensayar.",
        "Antes de la presentación final, el educador o la educadora tradicional valida la pronunciación y el saludo en lengua, y la comunidad puede revisar lo que se dice sobre su cultura. Si hay algo que no deba mostrarse, se quita. Al terminar, agradecemos a la fuente y a quien nos ayudó.",
    ],
    vocab=[("ensayo", "práctica previa de una presentación"), ("retroalimentación", "ayuda que dice qué estuvo bien y qué mejorar"), ("claridad", "que se entienda lo que digo"), ("ritmo", "velocidad con que hablo"), ("validación", "revisión de quien sabe para confirmar que es correcto")],
    worked=[
        W("Puntuar un ensayo", "Un ensayo obtuvo: claridad 3, volumen y ritmo 2, atribución 3, respeto de límites 3. ¿Cuántos puntos suma?", ["Sumo los cuatro criterios.", "3 + 2 + 3 + 3 da el total.", "Comparo con el máximo de 12."], "Suma 11 de 12 puntos."),
        W("Dar retroalimentación", "Un compañero habla muy rápido y no nombra a la fuente. Escribe una retroalimentación con ayuda.", ["Primero digo qué estuvo bien: se entendía el tema.", "Luego sugiero hablar más lento y nombrar a la fuente.", "Doy un ejemplo: «Según don Teodoro…»."], "«Se entendía el tema. Para mejorar, habla más lento y nombra a la fuente, por ejemplo: ‘Según don Teodoro…’»."),
    ],
    mistakes=[
        M("Presentar sin ensayar.", "No se descubren los errores ni el tiempo.", "Ensaya al menos una vez en voz alta."),
        M("Dar retroalimentación diciendo solo «estuvo malo».", "No dice qué mejorar.", "Di qué estuvo bien, qué mejorar y un ejemplo."),
    ],
    R=[
        ex("¿Cuántos criterios se revisan en el ensayo de esta clase? Escribe el número.", "4", "Son claridad, volumen y ritmo, atribución y límites."),
        ex("¿Quién valida la pronunciación en lengua indígena? A) el educador o la educadora tradicional B) un compañero que adivina", "A", "Quien enseña la lengua la valida."),
        ex("¿Cuál es el máximo de puntos del ensayo? A) 12 B) 3", "A", "Cuatro criterios de hasta 3 puntos suman 12."),
    ],
    C=[
        vf("la retroalimentación es una ayuda y dice qué estuvo bien y qué mejorar.", True, "Es una ayuda con ejemplos."),
        vf("si algo no debe mostrarse según la comunidad, se deja de todos modos.", False, "Se quita para respetar lo pedido."),
        ab("¿Para qué sirve ensayar?", "para detectar errores y controlar el tiempo", "para memorizar sin entender", "El ensayo permite corregir antes de presentar."),
    ],
    A=[
        arith("Un ensayo obtuvo: claridad 2, volumen y ritmo 3, atribución 3 y respeto de límites 2. ¿Cuántos puntos suma?", "2+3+3+2", "Se suman los cuatro criterios.", " puntos"),
        arith("Un grupo quiere llegar a 10 puntos de 12. Ya tiene 7. ¿Cuántos puntos le faltan?", "10-7", "Se resta lo que tiene de la meta.", " puntos"),
        ex("Retroalimentación: elige la mejor. A) «Hablaste muy bajo; sube un poco el volumen, por ejemplo al nombrar a la fuente» B) «Estuvo feo»", "A", "Dice qué mejorar y da un ejemplo."),
    ],
    Z=[
        ex("Un grupo obtuvo 12 puntos en el ensayo y dice que no necesita validación. ¿Qué falta? A) validación de pronunciación y contenido por el educador o la comunidad B) más puntos", "A", "El puntaje no reemplaza la validación."),
        ex("Una niña obtiene 0 puntos en atribución. ¿Qué debe hacer? A) nombrar a la fuente en el guion B) hablar más fuerte", "A", "El criterio que falta es nombrar a la fuente."),
    ],
    D=[
        arith("Un curso tiene 4 grupos y cada ensayo dura 3 minutos con 2 minutos de retroalimentación. ¿Cuántos minutos necesita en total?", "4*(3+2)", "Cada grupo usa 5 minutos y son 4 grupos.", " minutos"),
        ex("Un grupo quita de su exposición una parte que la comunidad pidió no mostrar y baja de 12 a 11 puntos por tiempo. ¿Hizo bien? Responde Sí o No.", "Sí", "Respetar el límite vale más que un punto."),
    ],
    context=[ab("Antes del acto del Día Internacional de los Pueblos Indígenas (9 de agosto) en tu escuela, un grupo va a exponer. ¿Qué conviene?", "ensayar, pedir retroalimentación y validación", "improvisar", "El acto es una presentación pública y se valida antes.")],
    selfcheck=[
        ex("Nombra dos de los cuatro criterios del ensayo.", "Dos entre: claridad, volumen y ritmo, atribución, respeto de límites", "Son los criterios de esta clase."),
        vf("al terminar la exposición, se agradece a la fuente.", True, "Es parte del cierre."),
        ex("¿Qué haces si el educador corrige tu pronunciación? A) la ensayo de nuevo y agradezco B) insisto en la mía", "A", "El educador enseña la pronunciación."),
    ],
    task=T("Con tu guion de la clase 4 (turnos de agua de Valle Seco, doña Natalia), haz un ensayo con una persona de tu casa. Que ella califique de 0 a 3 cada criterio: claridad, volumen y ritmo, atribución y respeto de límites. Suma los puntos, anota una cosa que estuvo bien y una por mejorar y escribe la pregunta que le harías al educador para validar tu pronunciación.",
           "Claridad 3, volumen 2, atribución 3, límites 3: suma 11 de 12. Estuvo bien: nombré a doña Natalia. Mejorar: hablar más fuerte. Pregunta: «¿Puede revisar si estoy diciendo bien el saludo en la lengua de mi comunidad?»",
           ["califica los cuatro criterios", "suma correctamente", "anota logro y mejora", "formula pregunta de validación"], ["tabla de puntos", "pregunta al educador"], ["no sumar bien", "omitir la validación"],
           "Pedir que muestre los puntos y la suma; valorar que pida validación."),
    reinforce="Haz una tabla con los cuatro criterios y el puntaje de tu ensayo.",
    extend="Escribe una retroalimentación para otro compañero con un logro, una mejora y un ejemplo.",
)
