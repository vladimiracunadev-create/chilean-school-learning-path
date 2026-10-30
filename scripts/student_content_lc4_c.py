"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR04 (escritura de palabras y frases en contexto de rescate y revitalización) y OA LR05 (expresiones de la lengua
indígena en contextos artísticos y de producción ancestral, con recursos digitales).

Criterio de autoría: todas las fichas, escuelas, listas y personas son inventadas solo para practicar y están rotuladas
como tales; no se adapta ningún relato, diseño ni rito tradicional. Las únicas expresiones en lengua indígena son
saludos y palabras muy atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke) y el nombre de la lengua
mapuche en dos escrituras usadas (mapuzugun, mapudungun). No se inventa gramática, pronunciación, significado de
dibujos de textiles ni de cerámicas. Las frases de LR04 son frases en castellano con la palabra indígena entre
paréntesis; las frases completas en lengua indígena las enseña el educador/a tradicional. Los recursos digitales se
describen sin marcas ni enlaces y siempre con un adulto. Cada tarea abierta remite al educador/a tradicional o a la
comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LR4, LR5 = "LC04 OA LR04", "LC04 OA LR05"

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


# =================================================================== LR04 clase 1 · modelos y variantes
CARTEL_N = "Cartel Norte (inventado): la educadora tradicional de la Escuela Ejemplo Norte escribe el nombre de la lengua mapuche como «mapuzugun»."
CARTEL_S = "Cartel Sur (inventado): el educador tradicional de la Escuela Ejemplo Sur escribe el nombre de la lengua mapuche como «mapudungun»."

L(
    LR4, 1,
    materials="Lápiz y hoja. Los carteles y las fichas están escritos en este cuaderno; son inventados para practicar y no pertenecen a ninguna escuela real.",
    use="Aprenderé a observar un modelo escrito, a notar que una misma palabra puede escribirse de más de una forma y a no corregir a quien sabe. Sirve para escribir con respeto en una lengua que se está recuperando.",
    prior=["Sé copiar una palabra letra por letra desde un modelo.", "Sé leer una ficha de procedencia y distinguir fuente y permiso."],
    explain=[
        "Un modelo es un ejemplo bien escrito que miro antes de escribir. En una lengua indígena, el modelo lo entrega una fuente: el educador o la educadora tradicional, un libro de la comunidad o un cartel de la escuela. Primero observo el modelo con calma, letra por letra, y anoto de dónde viene.",
        "Una variante es otra manera, también válida, de escribir o decir la misma palabra. Hay variantes porque los pueblos usan distintos sistemas de escritura y porque la lengua cambia según el territorio. Por ejemplo, el nombre de la lengua mapuche se ve escrito «mapuzugun» y también «mapudungun».",
        "Cuando veo dos variantes no digo que una está mala ni elijo la que me gusta más. Anoto las dos con su fuente. Si necesito escribir una en mi trabajo, uso la que me entregó la fuente de mi escuela y pregunto al educador tradicional cuál corresponde. Yo no decido ni mezclo las variantes.",
    ],
    vocab=[("modelo", "ejemplo bien escrito que se mira antes de escribir"), ("variante", "otra manera válida de escribir o decir la misma palabra"), ("grafía", "forma de escribir una palabra con letras"), ("fuente", "persona o texto que enseña cómo se escribe una palabra"), ("unificar", "dejar una sola forma donde había varias")],
    worked=[
        W("Dos carteles, dos escrituras", CARTEL_N + " " + CARTEL_S + " ¿Cuál cartel está mal escrito?", ["Leo la fuente de cada cartel: una educadora y un educador tradicionales.", "Los dos nombran la misma lengua con escrituras distintas.", "Cada uno usa una variante de su escuela."], "ninguno: son dos variantes con su fuente"),
        W("Observar letra por letra", "Modelo: «ñuke». Una niña copió «nuke». ¿Qué letra del modelo falta en su copia?", ["Comparo las dos palabras letra por letra.", "El modelo empieza con ñ y la copia con n.", "Falta la ñ, la letra con tilde sobre la n."], "la ñ"),
    ],
    mistakes=[
        M("Decir que «mapudungun» está mal porque yo aprendí «mapuzugun».", "Son dos variantes y cada una tiene su fuente.", "Anoto las dos con su fuente y pregunto al educador tradicional cuál usar."),
        M("Cambiar una letra del modelo porque creo que se ve mejor.", "Estaría inventando una escritura que nadie enseñó.", "Copio el modelo tal cual y consulto antes de cambiar algo."),
    ],
    R=[
        ex(CARTEL_N + " ¿Cómo escribe esa escuela el nombre de la lengua?", "mapuzugun", "El cartel Norte usa esa escritura."),
        ex(CARTEL_S + " ¿Cómo escribe esa escuela el nombre de la lengua?", "mapudungun", "El cartel Sur usa esa escritura."),
        ex("Un modelo es un ejemplo bien escrito que miro antes de escribir. ¿Debo mirarlo antes o después de escribir?", "antes", "Primero observo el modelo y luego escribo."),
    ],
    C=[
        ex("Verdadero o falso: dos escrituras distintas de una misma palabra pueden ser ambas válidas si cada una viene de una fuente.", "Verdadero", "Eso es una variante."),
        ex("En los carteles Norte y Sur, ¿qué dice cada uno: que la lengua tiene nombres distintos o que el mismo nombre se escribe de dos formas?", "que el mismo nombre se escribe de dos formas", "Nombran la misma lengua con dos escrituras."),
        ex("Modelo: «kuyen». Copia de un niño: «kuyen». ¿La copia es igual al modelo? Sí o No.", "Sí", "Las dos tienen las mismas cinco letras en el mismo orden."),
    ],
    A=[
        ex("Modelo: «antü». Copias de tres niños: Ana «antu», Beto «antü», Cata «anto». ¿Quién copió igual que el modelo?", "Beto", "Solo Beto conserva la ü."),
        ex("Modelo: «ruka». Copia de Lía: «ruko». ¿Qué letra cambió: la primera o la última?", "la última", "El modelo termina en a y la copia termina en o."),
        ex("Fichas de procedencia: A) Fuente: educadora tradicional; permiso: sí. B) Fuente: «lo vi en una pantalla»; permiso: no se indica. ¿Cuál ficha sirve mejor como modelo para escribir?", "A", "Solo A tiene una fuente que enseña y un permiso."),
    ],
    Z=[
        ex("Una niña ve «mapuzugun» en un cartel y «mapudungun» en otro. Dice: «Uno está equivocado, voy a tachar el segundo». ¿Hace bien? Sí o No.", "No", "Son dos variantes y no le corresponde corregir."),
        ex("Dos escuelas escriben una palabra distinta y un niño propone inventar una tercera forma que junte las dos. ¿Qué responde mejor la clase: A) «Hagámoslo». B) «Preguntemos al educador tradicional»?", "B", "Unificar o crear una forma lo decide quien tiene autoridad en la lengua."),
    ],
    D=[
        ex("Observa estas copias del modelo «ñuke» (que significa madre según la ficha): 1) «ñuke», 2) «nuke», 3) «ñuke». ¿Cuántas copias son iguales al modelo?", "2", "Las copias 1 y 3 son iguales; la 2 no tiene ñ."),
        ex("Ordena los pasos para usar un modelo: A) copio letra por letra. B) anoto la fuente. C) miro el modelo con calma. Escribe las letras en orden.", "C, B, A", "Observo, anoto de dónde viene y recién copio."),
    ],
    context=[ex("Tu escuela recibe un cartel con «mapudungun» y tu cuaderno dice «mapuzugun». La profesora pregunta qué hacer. ¿Respondes «Anotemos las dos y preguntemos al educador tradicional» o «Borremos una»?", "«Anotemos las dos y preguntemos al educador tradicional»", "Ambas son variantes y consultar es lo respetuoso.")],
    selfcheck=[
        ex("¿Cómo se llama otra manera válida de escribir la misma palabra?", "variante", "Una variante es una escritura distinta pero válida."),
        ex("Si dudo cómo se escribe una palabra de la lengua, ¿invento la forma o pregunto?", "pregunto", "No se inventa: se consulta a quien la enseña."),
        ex("¿Quién me entrega el modelo para escribir una palabra en lengua indígena?", "el educador o la educadora tradicional", "Esa persona o la comunidad es la fuente."),
    ],
    task=T(
        "Lee estos dos carteles inventados para practicar. " + CARTEL_N + " " + CARTEL_S + " " + FICHA_PAL + " En tu cuaderno copia con cuidado cada escritura del nombre de la lengua con la escuela que la usa, copia la palabra «ñuke» desde la ficha y escribe una oración que diga por qué no tachas ninguna variante. Termina con una pregunta para el educador o la educadora tradicional.",
        "Norte: mapuzugun. Sur: mapudungun. Copia: ñuke. No tacho ninguna porque cada escuela tiene su fuente. Pregunta: ¿cuál variante usamos en nuestra escuela?",
        ["copia las dos escrituras sin cambiar letras", "copia «ñuke» con ñ", "explica que no se tacha una variante", "formula una pregunta para el educador/a tradicional"],
        ["palabras copiadas en el cuaderno", "oración y pregunta escritas"],
        ["tachar una variante", "cambiar la ñ por n"],
        "Revisa letra por letra la copia con el modelo; si tachó una variante, conversa por qué ambas tienen fuente. No corregir desde la sala la forma de la lengua.",
    ),
    reinforce="Copia «ko», «antü» y «mapu» desde la ficha y verifica con el dedo, letra por letra, que tu copia sea igual al modelo.",
    extend="Explica con tus palabras a una persona de tu casa qué es una variante y por qué no se tacha ninguna.",
)

# =================================================================== LR04 clase 2 · escribir palabras para nombrar
L(
    LR4, 2,
    materials="Lápiz, hoja y colores. La ficha de palabras y los dibujos descritos están en este cuaderno; son inventados para practicar.",
    use="Aprenderé a escribir una palabra de la ficha para nombrar un dibujo, un lugar o una cosa, anotando su significado y su fuente. Sirve para rotular con respeto en mi sala.",
    prior=["Sé observar un modelo y copiarlo letra por letra.", "Sé que una variante es otra escritura válida y que la fuente enseña cuál usar."],
    explain=[
        "Nombrar es poner una palabra al lado de lo que designa, como un rótulo en un dibujo o en una puerta. Para nombrar con una palabra de la lengua indígena, busco la palabra en la ficha, miro su significado y la copio letra por letra, sin cambiar ni agregar nada.",
        "Un rótulo completo tiene tres partes: la palabra en lengua indígena, su significado en castellano entre paréntesis y la fuente. Por ejemplo: «antü (sol), fuente: educadora de la Escuela Ejemplo». Así quien lo lee sabe qué dice, qué significa y de dónde viene.",
        "Elijo la palabra por su significado, no por su forma ni porque me gusta cómo suena. Si un dibujo muestra la luna, rotulo con la palabra que la ficha da para luna. Si la ficha no trae una palabra para lo que dibujé, no la invento: escribo el nombre en castellano y pregunto al educador tradicional.",
    ],
    vocab=[("nombrar", "poner una palabra junto a lo que designa"), ("rótulo", "palabra escrita junto a un dibujo, objeto o lugar"), ("significado", "lo que quiere decir una palabra"), ("fuente", "persona o texto que enseña la palabra"), ("designar", "indicar a qué cosa se refiere una palabra")],
    worked=[
        W("Elegir la palabra por su significado", FICHA_PAL + " Dibujo: una gota de agua. ¿Qué palabra de la ficha sirve para rotularlo?", ["Busco en la ficha una palabra cuyo significado sea agua.", "La ficha dice que «ko» es agua.", "El rótulo lleva «ko»."], "ko"),
        W("Armar un rótulo completo", FICHA_PAL + " Dibujo: la luna. Fuente: educadora de la Escuela Ejemplo. Escribe el rótulo con sus tres partes.", ["La palabra de la ficha para luna es «kuyen».", "Anoto el significado entre paréntesis: (luna).", "Agrego la fuente."], "kuyen (luna), fuente: educadora de la Escuela Ejemplo"),
    ],
    mistakes=[
        M("Rotular un dibujo de la casa con «mapu» porque me gustó cómo suena.", "«Mapu» es tierra; la casa mapuche es «ruka» según la ficha.", "Elijo la palabra por su significado en la ficha."),
        M("Escribir una palabra nueva en lengua indígena para un dibujo que la ficha no trae.", "Estaría inventando una palabra.", "Escribo el nombre en castellano y pregunto al educador tradicional."),
    ],
    R=[
        ex(FICHA_PAL + " ¿Qué palabra de la ficha significa «sol»?", "antü", "La ficha dice que «antü» es sol."),
        ex("Un rótulo completo tiene la palabra, su significado entre paréntesis y la fuente. ¿Cuántas partes tiene?", "3", "Palabra, significado y fuente son tres partes."),
        ex("Según la ficha, ¿qué palabra nombra la tierra: «mapu» o «ko»?", "mapu", "«Mapu» es tierra y «ko» es agua."),
    ],
    C=[
        ex("Dibujo: una casa mapuche con techo y puerta. ¿Con cuál palabra de la ficha lo rotulas: «ruka» o «ñuke»?", "ruka", "«Ruka» es la casa mapuche."),
        ex("Verdadero o falso: puedo elegir la palabra del rótulo porque me gusta cómo suena, sin mirar su significado.", "Falso", "Se elige por el significado que da la ficha."),
        ex("Rótulo: «antü (sol), fuente: educadora de la Escuela Ejemplo». ¿Qué parte del rótulo dice quién enseñó la palabra?", "la fuente", "La tercera parte nombra a quien la enseñó."),
    ],
    A=[
        ex("Dibujos: 1) el sol, 2) la luna, 3) el agua de un río. Con la ficha, escribe las palabras en ese orden.", "antü, kuyen, ko", "Cada una sale de la ficha según su significado."),
        ex(FICHA_PAL + " Un niño rotula el dibujo del sol como «antü (agua)». ¿Qué parte del rótulo está mal: la palabra o el significado entre paréntesis?", "el significado entre paréntesis", "«Antü» sí es la palabra para sol, pero el significado que escribió, agua, no corresponde."),
        ex("Dibujo: una montaña. La ficha no tiene palabra para montaña. ¿Qué haces: A) invento una palabra. B) rotulo «montaña» en castellano y pregunto al educador tradicional?", "B", "No se inventan palabras en la lengua."),
    ],
    Z=[
        ex("Una niña dice: «Rotulé la luna como «antü» porque suena más bonito». ¿Su rótulo es correcto? Sí o No.", "No", "«Antü» es sol; la luna es «kuyen» según la ficha."),
        ex("Un rótulo dice «ko» sin significado ni fuente. Opciones: A) está completo porque tiene la palabra. B) le faltan el significado y la fuente. ¿Cuál es cierta?", "B", "Un rótulo completo tiene tres partes."),
    ],
    D=[
        ex("Sala de práctica con cuatro cosas: el sol dibujado, el agua de una jarra, una maqueta de la casa mapuche y un dibujo de la tierra. ¿Cuántas de las cuatro se pueden rotular con una palabra de la ficha?", "4", "Las cuatro tienen palabra en la ficha: antü, ko, ruka y mapu."),
        ex("Ordena los pasos para rotular: A) copio la palabra letra por letra. B) busco su significado en la ficha. C) anoto la fuente. Escribe las letras en orden.", "B, A, C", "Primero elijo por significado, luego copio y al final anoto la fuente."),
    ],
    context=[ex("Quieres poner un rótulo en la puerta de la sala de práctica con la palabra para casa mapuche. ¿Escribes «ruka (casa mapuche)» con la fuente o inventas una palabra para sala?", "«ruka (casa mapuche)» con la fuente", "Solo se usa lo que la ficha da y se anota la fuente.")],
    selfcheck=[
        ex("¿Cómo elijo la palabra de un rótulo: por su significado o por cómo suena?", "por su significado", "El significado decide la palabra."),
        ex("Si la ficha no trae la palabra que necesito, ¿la invento o pregunto?", "pregunto", "Pregunto al educador tradicional."),
        ex("¿Cuántas partes tiene un rótulo completo?", "3", "Palabra, significado y fuente."),
    ],
    task=T(
        "Lee esta ficha inventada para practicar. " + FICHA_PAL + " Fuente: educadora tradicional de la Escuela Ejemplo. En tu cuaderno dibuja tres cosas de la ficha, por ejemplo el sol, la luna y el agua. Rotula cada dibujo con los tres datos: palabra, significado entre paréntesis y fuente. Después escribe una pregunta para el educador o la educadora tradicional sobre una cosa que dibujaste y que la ficha no nombre.",
        "antü (sol), fuente: educadora de la Escuela Ejemplo. kuyen (luna), fuente: educadora de la Escuela Ejemplo. ko (agua), fuente: educadora de la Escuela Ejemplo. Pregunta: ¿cómo se nombra el cerro?",
        ["rotula tres dibujos con palabra, significado y fuente", "copia cada palabra sin cambiar letras", "elige la palabra por su significado", "formula una pregunta para el educador/a tradicional"],
        ["tres dibujos rotulados", "pregunta escrita o dicha en voz alta"],
        ["rotular con una palabra que no corresponde", "inventar una palabra"],
        "Compara cada rótulo con la ficha; si inventó una palabra, pídele que la cambie por una pregunta al educador tradicional.",
    ),
    reinforce="Elige tres palabras de la ficha y escribe cada una dos veces mirando el modelo, con su significado entre paréntesis.",
    extend="Rotula cinco objetos de tu casa en castellano y escribe una pregunta para el educador tradicional sobre cómo se nombran en la lengua.",
)

# =================================================================== LR04 clase 3 · construir una frase simple
L(
    LR4, 3,
    materials="Lápiz y hoja. Las frases y la ficha están escritas en este cuaderno; son inventadas para practicar.",
    use="Aprenderé a escribir una frase simple en castellano que lleve una palabra de la lengua indígena entre paréntesis. Sirve para transmitir un mensaje corto sin inventar frases en la lengua.",
    prior=["Sé rotular con una palabra de la ficha, su significado y su fuente.", "Sé que una oración empieza con mayúscula y termina con punto."],
    explain=[
        "Una frase simple es un grupo de palabras que dice una idea completa, con quién hace algo y qué hace. Empieza con mayúscula y termina con punto. Por ejemplo: «El sol sale temprano.» Dice quién hace algo, el sol, y qué hace, salir temprano.",
        "En este cuaderno escribimos la frase en castellano y ponemos la palabra de la lengua indígena entre paréntesis, junto a su significado: «El sol (antü) sale temprano.» Así el mensaje se entiende y la palabra queda escrita igual que en la ficha. No cambio ni junto palabras en la lengua.",
        "Armar frases completas en la lengua indígena, con su gramática y su pronunciación, es algo que enseña el educador o la educadora tradicional. Yo no las invento ni las adivino. Mi frase se escribe en castellano con la palabra de la ficha, y si quiero decir más, pregunto cómo se dice.",
    ],
    vocab=[("frase", "grupo de palabras que dice una idea"), ("mayúscula", "letra grande con que empieza una oración"), ("punto", "signo que termina una oración"), ("paréntesis", "signos ( ) que encierran un dato extra"), ("mensaje", "idea que quiero comunicar")],
    worked=[
        W("Armar una frase con una palabra de la ficha", FICHA_PAL + " Arma una frase con «ko» (agua) y las palabras: bebo, el, agua, fría.", ["Pongo primero quien habla: «Bebo».", "Sigo con lo que bebo: «el agua (ko) fría».", "Pongo mayúscula al inicio y punto al final."], "Bebo el agua (ko) fría."),
        W("Revisar una frase", "Frase de un niño: «la luna (kuyen) brilla de noche». ¿Qué le falta?", ["Reviso el inicio: empieza con minúscula.", "Reviso el final: no tiene punto.", "Le faltan la mayúscula y el punto."], "una mayúscula al inicio y un punto al final"),
    ],
    mistakes=[
        M("Escribir una frase entera en la lengua indígena inventando las palabras que faltan.", "Estaría inventando gramática y palabras que nadie me enseñó.", "Escribo la frase en castellano con la palabra de la ficha entre paréntesis."),
        M("Poner el significado en lugar de la palabra de la lengua.", "El mensaje debe llevar la palabra de la ficha, escrita igual.", "Escribo la palabra entre paréntesis junto a su significado."),
    ],
    R=[
        ex("Frase: «El sol (antü) sale temprano.» ¿Qué palabra de la lengua indígena lleva?", "antü", "Está entre paréntesis."),
        ex("¿Con qué letra empieza una oración: con mayúscula o con minúscula?", "con mayúscula", "Toda oración empieza con mayúscula."),
        ex("¿Qué signo termina una oración: el punto o los paréntesis?", "el punto", "El punto cierra la oración."),
    ],
    C=[
        ex("¿Cuál frase está bien escrita? A) «El agua (ko) corre por el río.» B) «el agua (ko) corre por el río»", "A", "La A tiene mayúscula y punto."),
        ex("Verdadero o falso: puedo escribir una frase completa en la lengua indígena inventando las palabras que no conozco.", "Falso", "Esas frases las enseña el educador tradicional."),
        ex("En «La luna (kuyen) brilla de noche.», ¿qué significa la palabra entre paréntesis según la ficha?", "luna", "Según la ficha, «kuyen» es luna."),
    ],
    A=[
        ex("Ordena las palabras para formar una frase y agrega mayúscula y punto: casa, la, (ruka), limpia, está.", "La casa (ruka) está limpia.", "El sujeto va primero, luego el verbo y el resto."),
        ex("Completa con la palabra de la ficha que significa sol: «El ____ calienta la mañana.»", "antü", "La ficha dice que «antü» es sol."),
        ex("Frase: «Pisamos la tierra (mapu) con cuidado.» ¿Cuántas palabras tiene la frase sin contar el paréntesis ni su palabra?", "5", "Las palabras son: Pisamos, la, tierra, con, cuidado."),
    ],
    Z=[
        ex("Dos frases: 1) «El agua (ko) es clara.» 2) «El agua es clara (ko)» sin punto. ¿Cuál está mejor escrita y por qué?", "la 1, porque la palabra queda junto a lo que nombra y tiene punto", "La palabra va junto a «agua» y la oración termina con punto."),
        ex("Un niño dice: «Mi frase «Antü is mari mari» está en lengua indígena». ¿Qué problema tiene: mezcla lenguas e inventa o está perfecta?", "mezcla lenguas e inventa", "No es una frase de la lengua indígena; solo el educador tradicional la enseña."),
    ],
    D=[
        ex("Quieres escribir el mensaje «Hoy sale el sol» con la palabra de la ficha. ¿Cuál frase sirve mejor? A) «Hoy sale el sol (antü).» B) «Hoy sale el sol (kuyen).»", "A", "Sol es «antü»; «kuyen» es luna."),
        ex("Ordena los pasos para escribir una frase con una palabra de la ficha: A) escribo la frase en castellano. B) pongo la palabra entre paréntesis. C) agrego mayúscula y punto. D) elijo la palabra por su significado. Escribe las letras.", "D, A, B, C", "Primero elijo, luego escribo, agrego la palabra y reviso."),
    ],
    context=[ex("Debes escribir un aviso corto para la pizarra: «Hoy vemos la luna». ¿Escribes «Hoy vemos la luna (kuyen).» o «Hoy vemos la luna (antü).»?", "«Hoy vemos la luna (kuyen).»", "Kuyen es luna según la ficha.")],
    selfcheck=[
        ex("¿Dónde pongo la palabra de la lengua indígena en mi frase de este cuaderno: entre paréntesis o inventando una frase en la lengua?", "entre paréntesis", "Las frases completas las enseña el educador tradicional."),
        ex("¿Qué dos signos o letras revisa primero una frase: mayúscula y punto o paréntesis y comillas?", "mayúscula y punto", "Toda oración empieza con mayúscula y termina con punto."),
        ex("¿A quién le pregunto cómo se dice una frase completa en la lengua?", "al educador o la educadora tradicional", "Ellos enseñan las frases en la lengua."),
    ],
    task=T(
        "Escribe en tu cuaderno tres frases simples en castellano, cada una con una palabra de esta ficha entre paréntesis. " + FICHA_PAL + " Por ejemplo, puedes hablar del sol, de la luna o del agua. Revisa que cada frase tenga mayúscula, punto y la palabra escrita igual que la ficha. Termina con una pregunta para el educador o la educadora tradicional sobre cómo se diría una de tus frases completa en la lengua.",
        "El sol (antü) calienta la mañana. La luna (kuyen) brilla de noche. Tomo agua (ko) en el recreo. Pregunta: ¿cómo se dice completa la primera frase?",
        ["escribe tres frases simples", "usa una palabra de la ficha en cada frase", "cada frase tiene mayúscula y punto", "formula una pregunta para el educador/a tradicional"],
        ["tres frases escritas", "pregunta escrita o dicha en voz alta"],
        ["inventar frases en la lengua indígena", "olvidar la mayúscula o el punto"],
        "Revisa mayúscula, punto y que la palabra coincida con la ficha; si inventó una frase en la lengua, pide cambiarla por una pregunta.",
    ),
    reinforce="Elige una frase de las de esta clase, cópiala en tu cuaderno y subraya la palabra que viene de la ficha.",
    extend="Escribe cuatro frases con las palabras «ko», «antü», «kuyen» y «mapu», una en cada frase, y revisa mayúscula y punto.",
)

# =================================================================== LR04 clase 4 · revisar con una fuente válida
FICHA_REV = "Ficha de revisión (inventada): modelo de la educadora tradicional de la Escuela Ejemplo: «El sol (antü) y la luna (kuyen) acompañan el día y la noche.»"

L(
    LR4, 4,
    materials="Lápiz, hoja y un lápiz de otro color para corregir. Los textos y fichas están escritos aquí; son inventados para practicar.",
    use="Aprenderé a revisar un escrito comparándolo con una fuente válida, letra por letra, sin cambiar lo que la fuente no corrige. Sirve para dejar mi trabajo bien escrito y con respeto.",
    prior=["Sé armar una frase simple con una palabra de la ficha.", "Sé que las variantes se anotan y no se corrigen entre sí."],
    explain=[
        "Revisar es leer de nuevo lo que escribí y compararlo con un modelo. La fuente válida es la que me dio el educador o la educadora tradicional, no una que veo suelta o que no tiene autor. Reviso tres cosas: la palabra de la lengua, su significado y la frase en castellano.",
        "Para revisar la palabra la comparo letra por letra con el modelo. Me fijo en las letras especiales, como la ü y la ñ, que no se pueden cambiar por u o n. Si una letra no coincide, la marco con otro color y la escribo igual al modelo. No agrego tildes que el modelo no tiene.",
        "Reviso la frase: mayúscula, punto y palabras completas. Y reviso la fuente: ¿anoté quién me enseñó? Si el modelo y mi duda no se pueden resolver, no decido yo. Dejo marcada la duda y se la pregunto a la educadora tradicional, y espero su respuesta antes de dar el trabajo por terminado.",
    ],
    vocab=[("revisar", "leer de nuevo y comparar con un modelo"), ("fuente válida", "persona o texto que enseña la forma y está identificado"), ("corregir", "cambiar un error para que quede como el modelo"), ("coincidir", "ser igual en todo"), ("duda", "algo que no sé y debo preguntar")],
    worked=[
        W("Comparar con el modelo", FICHA_REV + " Escrito de un niño: «El sol (antu) y la luna (kuyen) acompañan el día y la noche.» ¿Qué corrige?", ["Comparo las dos palabras de la lengua con el modelo.", "«Kuyen» coincide; «antu» no.", "Al niño le falta la ü: debe quedar «antü»."], "antu debe ser antü"),
        W("Dejar una duda marcada", "Una niña escribió «ko» pero no sabe si en su territorio hay otra escritura. El modelo de la educadora solo trae «ko». ¿Qué hace?", ["El modelo coincide con su escrito.", "Su duda no puede resolverla ella sola.", "La anota y se la pregunta a la educadora."], "marca la duda y se la pregunta a la educadora tradicional"),
    ],
    mistakes=[
        M("Corregir una palabra con una fuente que encontré suelta, sin autor.", "No sé si esa fuente es válida.", "Reviso con el modelo que me dio el educador tradicional."),
        M("Cambiar la ü por u «porque es más fácil de escribir».", "Cambia la palabra y deja de coincidir con el modelo.", "Copio la letra especial igual que el modelo."),
    ],
    R=[
        ex(FICHA_REV + " ¿Qué dos palabras de la lengua trae el modelo?", "antü y kuyen", "Están entre paréntesis en el modelo."),
        ex("Cuando reviso, ¿comparo mi escrito con un modelo o lo dejo como está?", "lo comparo con un modelo", "Revisar es comparar."),
        ex("¿Qué letras especiales del modelo no puedo cambiar: ü y ñ o a y e?", "ü y ñ", "No se cambian por u o n."),
    ],
    C=[
        ex("Modelo: «kuyen». Escrito: «kuyen». ¿Coinciden? Sí o No.", "Sí", "Las cinco letras son iguales y están en el mismo orden."),
        ex("Verdadero o falso: puedo agregar una tilde que el modelo no trae si me parece que se ve mejor.", "Falso", "Mi escrito debe coincidir con el modelo."),
        ex("Una fuente válida es A) un texto sin autor que vi suelto. B) lo que me enseñó el educador tradicional. ¿Cuál es?", "B", "Una fuente válida está identificada y enseña."),
    ],
    A=[
        ex("Modelo: «antü». Escrito de tres niños: Ana «antü», Beto «antu», Cata «antu». ¿Cuántos escribieron como el modelo?", "1", "Solo Ana conserva la ü."),
        ex("Modelo: «ñuke». Escrito: «nuke». ¿Qué letra debes corregir?", "la ñ", "La primera letra debe ser ñ."),
        ex("Escrito: «el agua (ko) es clara». Revisa y escribe cómo debe quedar la frase.", "El agua (ko) es clara.", "Faltan la mayúscula inicial y el punto final."),
    ],
    Z=[
        ex("Un niño dice: «Mi palabra no coincide con el modelo, pero la dejo porque a mí me gusta más». ¿Revisó bien? Sí o No.", "No", "Revisar es hacer que coincida con el modelo."),
        ex("Dos compañeros discuten cómo termina el modelo «ruka». Uno dice «termina en o». Otro dice «termina en a». El modelo de la educadora trae «ruka». ¿Quién tiene razón según el modelo?", "el de la a", "El modelo de la fuente es el que manda al copiar."),
    ],
    D=[
        ex(FICHA_REV + " Escrito: «el sol (antü) y la luna (kuien) acompañan el día y la noche». Cuenta los errores: mayúscula, palabra de la lengua y punto. ¿Cuántos errores hay en total?", "3", "Falta la mayúscula, «kuien» debe ser «kuyen» y falta el punto."),
        ex("Ordena los pasos de la revisión: A) anoto la fuente. B) comparo cada palabra con el modelo. C) marco lo que no coincide. D) pregunto lo que no puedo resolver. Escribe las letras.", "B, C, D, A", "Comparo, marco, pregunto y anoto la fuente."),
    ],
    context=[ex("Vas a pegar un cartel con «Mari mari» en la puerta y notas que escribiste «Mari marí». ¿Qué haces: lo comparas con el modelo y corriges o lo pegas igual?", "lo comparo con el modelo y corrijo", "Revisar con el modelo evita errores.")],
    selfcheck=[
        ex("¿Qué comparo en una revisión: mi escrito con un modelo o dos escritos míos?", "mi escrito con un modelo", "El modelo viene de una fuente válida."),
        ex("Si no puedo resolver una duda, ¿decido yo o pregunto al educador tradicional?", "pregunto al educador tradicional", "No decido solo sobre la lengua."),
        ex("¿Debo anotar la fuente en mi trabajo? Sí o No.", "Sí", "Dice de dónde vino lo escrito."),
    ],
    task=T(
        "Lee este modelo inventado para practicar. " + FICHA_REV + " Ahora lee el escrito de un compañero ficticio: «el sol (antü) y la luna (kuyen) acompañan el día y la noche». En tu cuaderno haz una tabla de dos columnas. En la primera escribe qué error encontraste y en la segunda cómo debe quedar. Después escribe cómo anotarás la fuente. Termina con una pregunta para la educadora tradicional.",
        "Error: falta la mayúscula inicial. Debe quedar «El sol…». Error: falta el punto final. Fuente: educadora de la Escuela Ejemplo. Pregunta: ¿cómo puedo revisar mejor mis palabras?",
        ["encuentra al menos dos errores de escritura", "escribe cómo debe quedar cada uno", "anota la fuente", "formula una pregunta para el educador/a tradicional"],
        ["tabla de dos columnas", "fuente y pregunta escritas"],
        ["cambiar palabras que sí coinciden con el modelo", "olvidar anotar la fuente"],
        "Comprueba que corrige solo lo que no coincide con el modelo; si cambió una palabra de la lengua que sí coincidía, vuelve a compararla letra por letra con él.",
    ),
    reinforce="Escribe «antü», «kuyen» y «mapu» mirando la ficha y revisa con un lápiz de color letra por letra.",
    extend="Escribe una frase con dos palabras de la ficha, déjala en blanco un rato y luego revísala como si fuera de otra persona.",
)

# =================================================================== LR05 clase 1 · acordar propósito y límites
L(
    LR5, 1,
    materials="Lápiz y hoja. Las situaciones están escritas en este cuaderno; son inventadas para practicar. Si usas un dispositivo, hazlo siempre con una persona adulta.",
    use="Aprenderé qué es una expresión en un textil o una cerámica, a decidir el propósito de un recurso digital pequeño y a fijar límites antes de empezar. Sirve para valorar la identidad de un pueblo sin apropiarme de lo que no me corresponde.",
    prior=["Sé que las palabras de la lengua indígena las enseña el educador o la educadora tradicional.", "Sé leer una ficha de procedencia."],
    explain=[
        "La textilería es el trabajo de tejer telas, y la alfarería es el trabajo de hacer objetos con greda, como vasijas. Son oficios ancestrales: los pueblos originarios los practican hace mucho tiempo y los traspasan de generación en generación. Estos objetos pueden llevar dibujos y a veces palabras de la lengua.",
        "Los dibujos y signos de un textil o de una cerámica pueden tener un significado para el pueblo o la familia que los hace. Ese significado lo explican quien teje o modela y la comunidad. Yo no lo adivino ni lo explico, y no copio un diseño tradicional para usarlo en mis trabajos. Lo miro con respeto y pregunto.",
        "Para un recurso digital pequeño, como un afiche o una presentación, primero acuerdo el propósito, que es para qué lo hago, y los límites: qué palabras uso, quién las autoriza, quién lo verá y dónde se guarda. Si falta una respuesta, me detengo y pregunto al educador tradicional.",
    ],
    vocab=[("textilería", "oficio de tejer telas"), ("alfarería", "oficio de modelar objetos con greda"), ("propósito", "para qué hago un recurso"), ("límite", "lo que acuerdo no hacer"), ("recurso digital", "trabajo hecho o mostrado en un dispositivo")],
    worked=[
        W("Elegir el propósito", "Un curso quiere hacer un afiche digital para que las familias valoren la alfarería de su territorio. ¿Cuál es el propósito: valorar la alfarería o vender vasijas?", ["Leo qué quiere el curso: que las familias valoren la alfarería.", "No se habla de vender.", "El propósito es valorar."], "valorar la alfarería"),
        W("Fijar un límite", "El curso quiere copiar un dibujo de un textil tradicional en el afiche. El educador tradicional no ha dado permiso. ¿Qué hace el curso?", ["Reviso si hay permiso: no hay.", "Un dibujo de un textil puede tener un significado que no me corresponde explicar.", "No lo copia y pregunta antes."], "no lo copia y pregunta al educador tradicional"),
    ],
    mistakes=[
        M("Copiar un dibujo de un textil tradicional para decorar mi afiche.", "Puede tener un significado que cuida una familia o un pueblo.", "No lo copio y pregunto al educador tradicional qué puedo usar."),
        M("Empezar el recurso digital sin decir para qué es.", "Sin propósito no sé qué palabras ni qué límites elegir.", "Anoto primero el propósito y los límites."),
    ],
    R=[
        ex("La textilería, ¿es el oficio de tejer telas o de modelar greda?", "tejer telas", "La alfarería es la que modela greda."),
        ex("La alfarería, ¿hace vasijas con greda o con tela?", "con greda", "Alfarería es modelar objetos con greda."),
        ex("Antes de hacer un recurso digital, ¿acuerdo primero el propósito o lo dejo para el final?", "primero el propósito", "Sin propósito no hay límites claros."),
    ],
    C=[
        ex("Verdadero o falso: los dibujos de una vasija tradicional siempre significan lo que yo imagino.", "Falso", "Su significado lo explican quienes la hacen y la comunidad."),
        ex("Un límite del recurso es A) qué palabras no uso sin permiso. B) el color de la hoja. ¿Cuál es un límite cultural?", "A", "Un límite cultural cuida lo que no puedo usar sin permiso."),
        ex("Propósito de un afiche: «mostrar con respeto un oficio ancestral». ¿Responde a «para qué lo hago»? Sí o No.", "Sí", "Dice para qué se hace el recurso."),
    ],
    A=[
        ex("Tres propósitos: 1) hacer reír con las palabras de la lengua. 2) valorar con respeto el trabajo de las tejedoras. 3) copiar diseños para venderlos. ¿Cuál es respetuoso?", "2", "Valorar con respeto no se apropia de nada."),
        ex("Además del propósito, los límites que acuerdo son: qué palabras uso, quién las autoriza, quién lo verá y dónde se guarda. ¿Cuántos límites son?", "4", "Son cuatro límites."),
        ex("Una niña propone usar en el afiche las palabras «ko» y «antü». La lista autorizada de la educadora trae «ko», «antü» y «mari mari». ¿Están permitidas esas palabras? Sí o No.", "Sí", "Ambas están en la lista autorizada."),
    ],
    Z=[
        ex("Un niño dice: «Si el diseño de un textil es bonito, lo copio en mi recurso». ¿Tiene razón? Sí o No.", "No", "El diseño puede tener significado y no se copia sin permiso."),
        ex("El curso no sabe si puede mostrar el afiche a otros cursos. ¿Qué hace mejor: A) lo publica y ve qué pasa. B) acuerda con el educador tradicional quién lo verá antes de empezar?", "B", "Los límites se fijan antes."),
    ],
    D=[
        ex("Ordena los pasos: A) empiezo el recurso. B) acuerdo el propósito. C) fijo los límites. Escribe las letras en orden.", "B, C, A", "Primero acuerdo el propósito, luego fijo los límites y recién empiezo."),
        ex("Un afiche de práctica tendrá 3 palabras de la lista autorizada, 2 imágenes dibujadas por el curso y 1 título. ¿Cuántos elementos tiene el afiche en total?", "6", "3 + 2 + 1 = 6 elementos."),
    ],
    context=[ex("Tu curso hace un afiche sobre una vasija de práctica (inventada). Una compañera quiere agregar una explicación del dibujo de la vasija. ¿Qué propones: «Pidamos que lo explique el educador tradicional» o «Inventemos la explicación»?", "«Pidamos que lo explique el educador tradicional»", "El significado lo da quien lo cuida.")],
    selfcheck=[
        ex("¿Qué es el propósito de un recurso: para qué lo hago o con qué lo hago?", "para qué lo hago", "Propósito es el para qué."),
        ex("Si no hay permiso para usar un dibujo tradicional, ¿lo copio o pregunto?", "pregunto", "Pido permiso antes de usarlo."),
        ex("¿Quién explica el significado de los dibujos de un textil tradicional?", "quien lo teje y la comunidad", "Yo no lo adivino."),
    ],
    task=T(
        "Imagina un afiche digital de práctica (inventado) para que las familias valoren el oficio de la textilería o de la alfarería. Escribe en tu cuaderno: 1) el propósito del afiche en una oración, 2) tres límites que acuerdas (por ejemplo: qué no copiarás, quién lo verá, dónde se guarda), 3) las palabras que usarías de esta lista: «mari mari», «chaltumay», «ko», «antü». Si no sabes algo del oficio, escribe una pregunta para el educador o la educadora tradicional.",
        "Propósito: que las familias valoren la alfarería del territorio. Límites: no copio dibujos tradicionales, lo ve solo el curso, se guarda en la sala. Palabras: mari mari y chaltumay. Pregunta: ¿qué dibujos de la greda puedo mostrar?",
        ["escribe un propósito claro", "escribe tres límites", "usa solo palabras de la lista", "formula una pregunta para el educador/a tradicional"],
        ["propósito, límites y palabras escritos", "pregunta escrita o dicha en voz alta"],
        ["copiar diseños tradicionales", "no fijar límites"],
        "Confirma que el propósito sea respetuoso y que los límites cuiden lo cultural; si propone copiar un diseño, conversa por qué se pregunta antes.",
    ),
    reinforce="Escribe con tus palabras qué es la textilería y qué es la alfarería, cada una en una oración.",
    extend="Explica por qué se acuerda el propósito antes de hacer un afiche digital y qué pasaría si se hace al final.",
)

# =================================================================== LR05 clase 2 · seleccionar expresiones autorizadas
LISTA_AUT = "Lista autorizada de práctica (inventada): la educadora tradicional de una Escuela Ejemplo autoriza usar en el recurso del curso «mari mari» (saludo), «chaltumay» (gracias) y «ko» (agua), todas en mapuzugun. Las demás palabras no están autorizadas hasta que ella las revise."

L(
    LR5, 2,
    materials="Lápiz y hoja. Las listas y los textos están escritos aquí; son inventados para practicar.",
    use="Aprenderé a elegir, de una lista que da la fuente, las expresiones que sí puedo usar en un recurso y a dejar fuera las que no tienen permiso. Sirve para valorar la lengua sin usar palabras sin autorización.",
    prior=["Sé que un recurso digital tiene propósito y límites.", "Sé que no copio dibujos ni palabras sin permiso."],
    explain=[
        "Una expresión autorizada es una palabra o frase que la fuente me permitió usar y que figura en una lista escrita. La lista dice la expresión, su significado y para qué se puede usar. Si una palabra no está en la lista, no la uso, aunque la haya visto en otro lugar.",
        "Para seleccionar hago tres pasos. Primero leo la lista completa. Segundo relaciono el propósito de mi recurso con las expresiones: si mi afiche da la bienvenida, busco el saludo; si agradece, busco «gracias». Tercero escribo solo las que sirven, con el significado entre paréntesis.",
        "Seleccionar también es dejar cosas fuera. Una expresión puede estar autorizada y no servir a mi propósito, y la dejo. Otra puede servir y no estar autorizada, y la dejo hasta tener permiso. Y si dudo, pregunto antes de usarla. La palabra no me pertenece: la cuida una comunidad.",
    ],
    vocab=[("autorizada", "con permiso escrito de la fuente"), ("seleccionar", "elegir algunas cosas de un grupo"), ("lista", "papel que ordena varios datos"), ("relacionar", "unir dos ideas porque tienen que ver"), ("dejar fuera", "no incluir algo en el recurso")],
    worked=[
        W("Elegir según el propósito", LISTA_AUT + " Un afiche quiere dar la bienvenida. ¿Qué expresión eliges?", ["El propósito es dar la bienvenida.", "En la lista, «mari mari» es un saludo.", "Elijo «mari mari»."], "mari mari"),
        W("Dejar fuera una palabra sin permiso", LISTA_AUT + " Un niño quiere usar «antü». ¿Puede usarla?", ["Busco «antü» en la lista.", "No está: la lista trae «mari mari», «chaltumay» y «ko».", "No la usa hasta que la educadora la revise."], "no puede usarla todavía; pregunta a la educadora"),
    ],
    mistakes=[
        M("Usar una palabra porque la vi en otro cartel, aunque no esté en mi lista.", "Esa palabra no tiene el permiso de mi fuente.", "Uso solo lo que está en la lista y pregunto por lo demás."),
        M("Usar todas las palabras de la lista aunque no tengan que ver con mi propósito.", "El recurso queda confuso.", "Elijo solo las que sirven a mi propósito."),
    ],
    R=[
        ex(LISTA_AUT + " ¿Cuántas expresiones autorizadas trae la lista?", "3", "Son «mari mari», «chaltumay» y «ko»."),
        ex("Según la lista, ¿«chaltumay» quiere decir «gracias» o «saludo»?", "gracias", "La lista lo dice entre paréntesis."),
        ex("Una palabra que no está en la lista, ¿puedo usarla? Sí o No.", "No", "Falta el permiso de la fuente."),
    ],
    C=[
        ex("Propósito: agradecer a las familias. Según la lista, ¿qué expresión eliges: «mari mari» o «chaltumay»?", "chaltumay", "Es la que significa gracias."),
        ex("Verdadero o falso: una expresión autorizada siempre debe usarse en mi recurso.", "Falso", "Solo si sirve a mi propósito."),
        ex("Según la lista, ¿«ko» significa agua o luna?", "agua", "La lista lo dice así."),
    ],
    A=[
        ex("Un recurso quiere dar la bienvenida y hablar del agua. Con la lista, ¿qué dos expresiones eliges?", "mari mari y ko", "Una saluda y la otra nombra el agua."),
        ex("Cuatro palabras que un curso quiere usar: «mari mari», «kuyen», «ko», «ruka». Con la lista, ¿cuántas están autorizadas?", "2", "Solo «mari mari» y «ko» están en la lista."),
        ex("Un niño dice: «Usaré «kuyen» porque la vi en un cartel». ¿Qué le recomiendas: A) usarla. B) pedir permiso a la educadora antes?", "B", "No está en la lista."),
    ],
    Z=[
        ex("Propósito del afiche: agradecer. La lista trae «mari mari», «chaltumay» y «ko». ¿Es obligatorio usar las tres porque están en la lista? Sí o No.", "No", "Elijo solo las que sirven al propósito, aquí «chaltumay»."),
        ex("Un recurso quiere usar tres palabras: dos están en la lista y una no. ¿Qué es mejor: A) usar las tres. B) usar las dos de la lista y pedir permiso para la tercera?", "B", "El permiso va antes del uso."),
    ],
    D=[
        ex("Lista: 3 expresiones. El curso quiere 5 palabras para el afiche. ¿Cuántas palabras faltan por autorizar?", "2", "5 − 3 = 2."),
        ex("Ordena los pasos: A) escribo las elegidas con su significado. B) leo la lista completa. C) relaciono mi propósito con las expresiones. Escribe las letras.", "B, C, A", "Primero leo, luego relaciono y al final escribo."),
    ],
    context=[ex("En tu escuela alguien propone usar «ñuke» en un cartel. La lista del curso trae «mari mari», «chaltumay» y «ko». ¿Qué haces: pides permiso a la educadora o lo pones igual?", "pido permiso a la educadora", "No está en la lista.")],
    selfcheck=[
        ex("¿Qué dice la lista autorizada?", "qué expresiones puedo usar y qué significan", "La lista da permiso y significado."),
        ex("Si una expresión no está en la lista, ¿la uso o pregunto?", "pregunto", "Se pide permiso."),
        ex("¿Debo usar todas las expresiones de la lista aunque no sirvan a mi propósito? Sí o No.", "No", "Elijo solo las que sirven."),
    ],
    task=T(
        "Lee esta lista inventada para practicar. " + LISTA_AUT + " En tu cuaderno escribe: 1) el propósito de un afiche pequeño (por ejemplo, dar la bienvenida a una visita), 2) las expresiones de la lista que elegirías, con su significado, 3) una palabra que no usarás porque no está en la lista, y 4) una pregunta para la educadora tradicional.",
        "Propósito: dar la bienvenida a una visita. Elijo «mari mari» (saludo) y «chaltumay» (gracias). No usaré «kuyen» porque no está en la lista. Pregunta: ¿puedo usar otra palabra para el afiche?",
        ["escribe un propósito", "elige solo expresiones de la lista", "nombra una palabra que deja fuera", "formula una pregunta para el educador/a tradicional"],
        ["propósito y selección escritos", "pregunta escrita o dicha en voz alta"],
        ["usar palabras fuera de la lista", "elegir sin relación con el propósito"],
        "Comprueba que usó solo palabras de la lista; si agregó una que no está, pídele que la cambie por una pregunta a la educadora.",
    ),
    reinforce="Vuelve a leer la lista y subraya las expresiones que sirven para dar la bienvenida.",
    extend="Escribe dos propósitos distintos para dos afiches y elige las expresiones de la lista que sirven a cada uno.",
)

# =================================================================== LR05 clase 3 · diseñar un recurso pequeño
PLAN = "Plan de práctica (inventado): afiche de bienvenida con 1 título, 2 palabras autorizadas con su significado, 1 dibujo del curso, 1 línea de fuente y 1 línea de «quién lo hizo»."

L(
    LR5, 3,
    materials="Lápiz, hoja y colores. Si usas un dispositivo, hazlo con una persona adulta. Todo lo que necesitas está escrito aquí; el diseño es de práctica y se puede hacer en papel.",
    use="Aprenderé a planificar un recurso digital pequeño: elegir sus partes, ordenarlas y comprobar que tengan sentido. Sirve para crear algo claro, sin copiar diseños ajenos.",
    prior=["Sé elegir expresiones autorizadas de una lista.", "Sé que los dibujos tradicionales de textiles y cerámicas no se copian sin permiso."],
    explain=[
        "Diseñar es pensar y ordenar las partes de un recurso antes de hacerlo. Un recurso pequeño puede ser un afiche, una presentación de tres láminas o una tarjeta digital. Antes de usar el dispositivo hago un boceto en papel: un dibujo simple con lo que va y dónde va.",
        "Cada recurso tiene partes: un título que dice de qué trata, las expresiones autorizadas con su significado, una imagen hecha por el curso, la fuente que enseñó las palabras y el nombre de quienes lo hicieron. Dibujo cada parte en su lugar y compruebo que no sobre ni falte ninguna.",
        "Las imágenes las dibujamos nosotros. No copiamos el dibujo de un textil ni de una vasija tradicional, porque puede tener un significado que no nos corresponde. Y no agrego palabras que no estén en la lista. Un buen diseño es sencillo, se lee fácil y cumple su propósito.",
    ],
    vocab=[("diseñar", "pensar y ordenar las partes de algo antes de hacerlo"), ("boceto", "dibujo simple que muestra cómo quedará"), ("título", "frase que dice de qué trata"), ("lámina", "página de una presentación"), ("imagen propia", "dibujo hecho por el curso")],
    worked=[
        W("Contar las partes de un plan", PLAN + " ¿Cuántas partes tiene el afiche?", ["Sumo las partes: título 1, palabras 2, dibujo 1, fuente 1, quién lo hizo 1.", "1 + 2 + 1 + 1 + 1 = 6."], "6"),
        W("Detectar lo que sobra", "Plan: título, palabra «mari mari» autorizada, dibujo del diseño de un textil tradicional copiado de un libro, fuente, autores. ¿Qué parte no corresponde?", ["Reviso cada parte.", "El dibujo copiado del textil puede tener un significado que no nos corresponde.", "No corresponde ese dibujo; el curso hace uno propio."], "el dibujo copiado del textil"),
    ],
    mistakes=[
        M("Dibujar el diseño de un textil tradicional porque se ve bonito.", "Puede tener un significado que no me corresponde explicar ni copiar.", "Hago un dibujo propio y pregunto qué se puede mostrar."),
        M("Llenar el afiche de palabras en lengua indígena para que se vea importante.", "Solo puedo usar las autorizadas y que sirvan al propósito.", "Dejo pocas palabras, bien elegidas."),
    ],
    R=[
        ex(PLAN + " ¿Cuántas palabras autorizadas lleva el plan?", "2", "Lo dice el plan."),
        ex("Un boceto, ¿es un dibujo simple de cómo quedará o el producto terminado?", "un dibujo simple de cómo quedará", "Se hace antes de crear."),
        ex("Un título, ¿dice de qué trata el recurso o quién lo hizo?", "de qué trata", "El título presenta el tema."),
    ],
    C=[
        ex("Verdadero o falso: la imagen del afiche puede ser un dibujo copiado de un textil tradicional si se ve bonito.", "Falso", "No se copia sin permiso."),
        ex("En el plan, ¿qué parte dice quién enseñó las palabras?", "la fuente", "La línea de fuente nombra a quien las enseñó."),
        ex("Un recurso pequeño de tres láminas, ¿cuántas páginas tiene?", "3", "Una lámina es una página."),
    ],
    A=[
        ex("Plan de una presentación: lámina 1 título, lámina 2 dos palabras con significado, lámina 3 fuente y autores. ¿Cuántas láminas tiene?", "3", "Hay tres láminas."),
        ex("Partes de un afiche: título, dos palabras, dibujo, fuente. Se le agrega una parte de «quién lo hizo». ¿Cuántas partes tiene ahora (contando cada palabra como una)?", "6", "4 + 1 + 1 = 6 contando las dos palabras por separado."),
        ex("El curso planifica un afiche con 2 palabras de una lista de 3. ¿Cuántas palabras de la lista dejará fuera?", "1", "3 − 2 = 1."),
    ],
    Z=[
        ex("Una niña dice: «Mi diseño tiene diez palabras en lengua indígena, así que es mejor». La lista autorizada trae solo 3. ¿Tiene razón? Sí o No.", "No", "Solo se pueden usar las autorizadas."),
        ex("Dos bocetos: A) título, 2 palabras autorizadas con significado, dibujo propio, fuente y autores. B) título, 8 palabras sin permiso, diseño copiado de un textil. ¿Cuál cumple mejor?", "A", "El A respeta permisos y no copia."),
    ],
    D=[
        ex("Un curso hará 4 láminas con 2 palabras distintas en cada una, sin repetir ninguna palabra en todo el recurso. Su lista autorizada tiene solo 3 palabras. ¿Cuántas palabras necesita en total y cuántas le faltan por autorizar?", "8 y 5", "4 × 2 = 8 palabras, 8 − 3 = 5 sin autorizar."),
        ex("Ordena los pasos del diseño: A) reviso que estén todas las partes. B) dibujo el boceto en papel. C) pienso qué partes llevará mi recurso. Escribe las letras.", "C, B, A", "Primero pienso las partes, luego dibujo el boceto y al final reviso."),
    ],
    context=[ex("Quieres un boceto de una tarjeta digital para dar las gracias a una visita. ¿Qué dibujas: una imagen propia del curso o el diseño de un textil de un libro?", "una imagen propia del curso", "No se copian diseños tradicionales sin permiso.")],
    selfcheck=[
        ex("¿Qué hago antes de usar el dispositivo: un boceto en papel o nada?", "un boceto en papel", "El boceto ayuda a ordenar."),
        ex("¿Quién hace las imágenes de mi recurso: el curso o un diseño tradicional copiado?", "el curso", "Las imágenes son propias."),
        ex("¿Puedo agregar palabras que no estén en la lista autorizada? Sí o No.", "No", "Solo las autorizadas."),
    ],
    task=T(
        "Haz en papel un boceto de un afiche pequeño (inventado) para agradecer a una visita. " + LISTA_AUT + " Dibuja un rectángulo grande y marca dentro seis lugares con estos nombres: título, palabra 1 con significado, palabra 2 con significado, dibujo propio, fuente, quién lo hizo. Escribe en cada lugar lo que irá. Termina con una pregunta para la educadora tradicional sobre algo que quieras agregar.",
        "Título: Gracias por venir. Palabra 1: chaltumay (gracias). Palabra 2: mari mari (saludo). Dibujo propio: dos manos del curso. Fuente: educadora de la Escuela Ejemplo. Quién lo hizo: el curso. Pregunta: ¿puedo agregar otra palabra?",
        ["marca los seis lugares", "usa solo palabras de la lista", "el dibujo es propio", "formula una pregunta para el educador/a tradicional"],
        ["boceto en papel con seis lugares", "pregunta escrita o dicha en voz alta"],
        ["copiar un diseño tradicional", "olvidar la fuente"],
        "Verifica que estén las seis partes y que no haya diseños copiados; si hay una palabra fuera de la lista, pídele que la cambie por una pregunta.",
    ),
    reinforce="Cuenta con tu dedo las seis partes de un afiche y di en voz alta qué va en cada una.",
    extend="Diseña en papel un boceto de una presentación de tres láminas con la misma lista autorizada.",
)

# =================================================================== LR05 clase 4 · crear sin reemplazar voces
L(
    LR5, 4,
    materials="Lápiz y hoja. Las situaciones están escritas aquí. Si usas un dispositivo para grabar o escribir, hazlo con una persona adulta y solo con permiso.",
    use="Aprenderé a crear mi recurso sin reemplazar la voz del educador tradicional ni de otras personas, y a decir qué hice yo y qué viene de la fuente. Sirve para crear con respeto y dar crédito.",
    prior=["Sé diseñar un recurso pequeño.", "Sé que solo uso las expresiones autorizadas."],
    explain=[
        "Reemplazar una voz es hacer que parezca que alguien dijo lo que no dijo, o poner otra voz en su lugar. Por ejemplo, grabar a un compañero imitando a una visita, o hacer que un programa de computador «hable» la lengua indígena. La lengua se aprende de personas que la saben. Un programa no la enseña bien ni reemplaza a la comunidad.",
        "En mi creación distingo claramente lo mío y lo que viene de la fuente. Lo mío es el título, el dibujo, la organización y mis oraciones en castellano. Lo que viene de la fuente son las palabras de la lista y su significado, que anoto con su fuente. No cambio ni acorto ninguna palabra.",
        "Si quiero incluir la voz de una persona, le pido permiso, le explico para qué y dónde se mostrará, y respeto si dice que no. Una grabación, una foto o un texto de otra persona solo se usan con su permiso y con su nombre, si ella lo desea. Mi creación suma, no reemplaza.",
    ],
    vocab=[("reemplazar", "poner algo o a alguien en el lugar de otro"), ("crédito", "decir quién hizo o enseñó algo"), ("permiso", "el sí de la persona para usar su voz o su trabajo"), ("imitar", "hacer lo que hace otro, a veces para burlarse"), ("sumar", "agregar algo propio sin quitar lo de otros")],
    worked=[
        W("Qué es mío y qué es de la fuente", "Un afiche tiene: a) título escrito por el curso, b) palabra «chaltumay» con significado de la educadora, c) dibujo del curso, d) fuente. ¿Cuántas partes son del curso?", ["Reviso quién hizo cada parte.", "El título y el dibujo son del curso.", "La palabra viene de la educadora y la fuente es un dato."], "2 (el título y el dibujo)"),
        W("Pedir permiso para una voz", "Un niño quiere grabar a la educadora diciendo «mari mari» para su presentación. ¿Qué hace primero?", ["La voz es de la educadora, no mía.", "Le pregunta si puede, para qué y dónde se mostrará.", "Si dice que no, respeta su decisión."], "le pide permiso y le explica para qué y dónde se mostrará"),
    ],
    mistakes=[
        M("Usar un programa de computador para que «hable» la lengua indígena en mi presentación.", "No reemplaza a quien enseña la lengua y puede decir mal las palabras.", "Uso las palabras escritas de la lista o invito al educador tradicional."),
        M("Grabar a un compañero imitando la voz de una visita.", "Puede ser una burla y no tengo permiso de la visita.", "No imito voces. Pregunto a la visita si quiere participar."),
    ],
    R=[
        ex("Reemplazar una voz, ¿es poner otra voz en lugar de la persona o pedir permiso a la persona?", "poner otra voz en lugar de la persona", "Eso es reemplazar."),
        ex("El título y el dibujo hechos por mi curso, ¿son partes mías o de la fuente?", "partes mías", "Los creó el curso."),
        ex("¿Qué debo pedir antes de usar la voz de una persona: permiso o aplausos?", "permiso", "El permiso es lo primero."),
    ],
    C=[
        ex("Verdadero o falso: un programa de computador puede reemplazar al educador tradicional para enseñar la lengua.", "Falso", "La lengua la enseñan las personas que la saben."),
        ex("Si una visita dice que no quiere ser grabada, ¿qué hago: respeto su decisión o grabo igual?", "respeto su decisión", "El permiso puede ser un no."),
        ex("Una creación que «suma» agrega algo propio. ¿Sumar es lo contrario de reemplazar? Sí o No.", "Sí", "Sumar no quita lo de otros."),
    ],
    A=[
        ex("Partes de un afiche: título (curso), dibujo (curso), palabras (educadora), significado (educadora), fuente (dato). ¿Cuántas son del curso?", "2", "Solo el título y el dibujo son del curso."),
        ex("Acciones: A) pido permiso para usar una foto. B) pongo la voz de un programa como si fuera de la visita. C) anoto la fuente. D) cambio una palabra de la lista. ¿Cuáles son respetuosas? Escribe las letras.", "A y C", "B y D reemplazan o cambian lo de otros."),
        ex("Un compañero dice que quiere publicar la foto de la educadora sin preguntarle. ¿Qué le propones: A) preguntarle antes. B) publicarla igual?", "A", "Se pide permiso."),
    ],
    Z=[
        ex("Una niña dice: «Si cambio una letra de la palabra de la lista, mi afiche será más original». ¿Hace bien? Sí o No.", "No", "Cambiar una palabra de la lista la deja mal escrita."),
        ex("Un grupo crea una grabación imitando la voz de una visita para reírse. ¿Qué problema tiene: es una burla y no tiene permiso, o es muy larga?", "es una burla y no tiene permiso", "La imitación sin permiso puede dañar."),
    ],
    D=[
        ex("Un recurso lleva 5 elementos: 2 son del curso y 3 vienen de la fuente. ¿Qué parte del recurso es de la fuente: 2 de 5 o 3 de 5?", "3 de 5", "Son los 3 elementos que no creó el curso."),
        ex("Ordena para incluir una voz: A) explico para qué y dónde se mostrará. B) pregunto si quiere participar. C) acepto su respuesta. Escribe las letras.", "B, A, C", "Pregunto, explico y acepto su decisión."),
    ],
    context=[ex("Una visita contó que no quiere que su voz salga en ninguna presentación. Tu curso ya tiene una grabación. ¿La borras y respetas su decisión o la guardas por si acaso?", "la borro y respeto su decisión", "La decisión de la persona manda.")],
    selfcheck=[
        ex("¿Qué es crear sin reemplazar voces?", "sumar algo propio sin poner mi voz en lugar de otros", "La creación suma."),
        ex("Si quiero la voz de una persona, ¿qué hago primero?", "pido permiso", "El permiso va antes."),
        ex("¿Una máquina que lee palabras de la lengua reemplaza a quien enseña la lengua? Sí o No.", "No", "Sigue siendo necesaria la persona."),
    ],
    task=T(
        "Lee esta situación inventada para practicar: «Un curso prepara una presentación de tres láminas para agradecer a una visita. Un niño propone usar un programa que lea en voz alta las palabras en lengua indígena. Otra niña propone invitar a la educadora a decirlas, si ella quiere.» " + LISTA_AUT + " En tu cuaderno escribe: 1) qué propuesta es mejor y por qué, 2) qué partes serán del curso y qué partes vendrán de la fuente, 3) una pregunta para la educadora tradicional.",
        "La segunda propuesta, porque la voz de la educadora no se reemplaza. Del curso: título y dibujo. De la fuente: las palabras «chaltumay» y «mari mari». Pregunta: ¿quiere decir usted las palabras si queremos grabarlas?",
        ["elige la propuesta que no reemplaza la voz", "separa lo del curso y lo de la fuente", "no inventa palabras", "formula una pregunta para el educador/a tradicional"],
        ["elección y partes escritas", "pregunta escrita o dicha en voz alta"],
        ["elegir la voz de un programa", "no dar crédito a la fuente"],
        "Observa que distinga lo propio de lo que viene de la fuente; si elige reemplazar la voz, conversa por qué la lengua la enseñan las personas que la saben.",
    ),
    reinforce="Escribe tres cosas que puede crear tu curso (título, dibujo, organización) y una que no puede reemplazar (la voz de la educadora).",
    extend="Escribe un mensaje de dos líneas para pedir permiso a una persona antes de mostrar su trabajo.",
)

# =================================================================== LR05 clase 5 · devolver, atribuir y controlar acceso
L(
    LR5, 5,
    materials="Lápiz y hoja. Las situaciones están escritas aquí. Todo es de práctica y se puede hacer en papel; si usas un dispositivo, hazlo con una persona adulta.",
    use="Aprenderé a devolver mi trabajo a la fuente para que lo revise, a atribuir (nombrar a quien enseñó) y a decidir quién puede ver mi recurso. Sirve para cuidar las palabras y a las personas.",
    prior=["Sé crear un recurso sin reemplazar voces.", "Sé que cada recurso tiene límites acordados."],
    explain=[
        "Devolver es mostrar mi trabajo terminado a quien me enseñó las palabras, antes de mostrarlo a otros. La educadora o el educador tradicional lo revisa, me dice si algo hay que cambiar y puede decir cuánto se puede mostrar. Mi recurso no está listo hasta que ella o él lo vea.",
        "Atribuir es escribir en el recurso quién enseñó las palabras y quiénes lo hicieron: «Palabras enseñadas por la educadora tradicional de la Escuela Ejemplo. Hecho por el curso». Así no me apropio de lo que me enseñaron y quien lo ve sabe de dónde viene.",
        "Controlar el acceso es decidir quién puede ver el recurso y dónde queda guardado. Puede ser solo el curso, las familias en una reunión, o toda la escuela. Si la fuente dijo solo dentro de la sala, no lo muestro afuera. No publico en lugares abiertos y no uso datos personales como apellidos, direcciones o fotos de rostros.",
    ],
    vocab=[("devolver", "mostrar mi trabajo a quien me enseñó, para que lo revise"), ("atribuir", "escribir quién enseñó o hizo algo"), ("acceso", "quién puede ver o usar el recurso"), ("publicar", "dejar algo visible para cualquier persona"), ("dato personal", "dato que identifica a una persona, como su dirección")],
    worked=[
        W("Revisar la atribución", "Afiche con la frase: «Palabras enseñadas por la educadora tradicional de la Escuela Ejemplo. Hecho por el curso». ¿Está atribuido? Sí o No.", ["Busco quién enseñó: la educadora tradicional.", "Busco quién lo hizo: el curso.", "Están los dos datos."], "Sí"),
        W("Elegir el acceso", "La educadora autorizó mostrar el recurso solo dentro de la sala. Un niño quiere subirlo a un sitio abierto de internet. ¿Puede?", ["Reviso el permiso: solo dentro de la sala.", "Un sitio abierto lo ve cualquier persona.", "No puede."], "No"),
    ],
    mistakes=[
        M("Mostrar el recurso a otros cursos antes de que lo vea la educadora.", "Ella puede corregir un error o decir que no se muestre.", "Primero lo devuelvo a la fuente."),
        M("Poner en el afiche el apellido y la dirección de un compañero.", "Son datos personales que no deben circular.", "Pongo solo «el curso» o el nombre que cada persona autorice."),
    ],
    R=[
        ex("Devolver mi trabajo, ¿es mostrarlo a la fuente antes de mostrarlo a otros o regalarlo?", "mostrarlo a la fuente antes de mostrarlo a otros", "Así lo revisa quien me enseñó."),
        ex("Atribuir, ¿es escribir quién enseñó y quién hizo el recurso o borrar los nombres?", "escribir quién enseñó y quién hizo el recurso", "Atribuir da crédito a quienes participaron."),
        ex("Si la fuente dijo «solo dentro de la sala», ¿puedo publicarlo en un sitio abierto? Sí o No.", "No", "Se respeta el permiso."),
    ],
    C=[
        ex("Verdadero o falso: puedo escribir la dirección de mi casa en el afiche para que me ubiquen.", "Falso", "Es un dato personal."),
        ex("¿Qué es controlar el acceso: decidir quién puede ver el recurso o decidir qué color tiene?", "decidir quién puede ver el recurso", "Acceso es quién lo ve."),
        ex("El recurso dice «Palabras enseñadas por la educadora tradicional». ¿Qué parte de la atribución muestra?", "quién enseñó las palabras", "Nombra a la fuente."),
    ],
    A=[
        ex("Datos de un afiche: 1) fuente de las palabras, 2) quiénes lo hicieron, 3) para quién es. ¿Cuántos datos de atribución tiene el afiche si trae solo el 1 y el 2?", "2", "La atribución nombra quién enseñó y quién hizo."),
        ex("El permiso de la educadora: «solo para familias en la reunión del curso». ¿Quién puede ver el recurso: las familias en la reunión o todo internet?", "las familias en la reunión", "Eso dice el permiso."),
        ex("Un niño quiere escribir al pie del afiche el nombre y el apellido de un compañero. ¿Qué hacen: A) piden permiso a la persona y a su familia, y usan solo su primer nombre si lo permiten. B) los ponen sin preguntar?", "A", "Los datos personales exigen permiso."),
    ],
    Z=[
        ex("Una niña dice: «Si el recurso queda lindo, no necesita que la educadora lo vea». ¿Tiene razón? Sí o No.", "No", "La fuente debe revisarlo."),
        ex("Un afiche dice «Hecho por el curso» pero no nombra a la educadora que enseñó las palabras. ¿Qué le falta?", "la atribución de la fuente", "Falta nombrar quién enseñó."),
    ],
    D=[
        ex("Ordena los pasos: A) lo muestro a las familias que el permiso indica. B) lo devuelvo a la educadora para que lo revise. C) termino mi afiche. Escribe las letras.", "C, B, A", "Termino, devuelvo para que lo revisen y recién muestro."),
        ex("Un recurso se mostrará a 2 cursos de 30 estudiantes cada uno, pero la educadora solo autorizó a 1 curso de 30. ¿A cuántos estudiantes de más se mostraría sin permiso?", "30", "60 − 30 = 30."),
    ],
    context=[ex("Terminaste el afiche y un familiar quiere compartirlo en una red social. Tu educadora dijo «solo dentro de la sala». ¿Respondes «Mejor no, el permiso es para la sala» o «Sí, compártelo»?", "«Mejor no, el permiso es para la sala»", "El permiso limita dónde se muestra.")],
    selfcheck=[
        ex("¿A quién devuelvo mi trabajo antes de mostrarlo a otros?", "a la educadora o el educador tradicional", "Ellos enseñaron las palabras."),
        ex("¿Qué datos no pongo en un recurso: apellidos y direcciones o títulos?", "apellidos y direcciones", "Son datos personales."),
        ex("¿Qué escribo para dar crédito: la atribución o el acceso?", "la atribución", "Atribuir es dar crédito."),
    ],
    task=T(
        "Lee este caso inventado para practicar. Un curso hizo un afiche de agradecimiento con las palabras «chaltumay» y «mari mari». La educadora tradicional lo revisó y dijo que se puede mostrar solo a las familias en una reunión del curso. En tu cuaderno escribe: 1) la frase de atribución que irá al pie del afiche, 2) quién lo podrá ver, 3) dónde se guardará (por ejemplo, en la sala), 4) un dato personal que no pondrás. Termina con una pregunta para la educadora tradicional.",
        "Atribución: «Palabras enseñadas por la educadora tradicional de la Escuela Ejemplo. Hecho por el curso». Lo verán las familias en la reunión. Se guarda en la sala. No pondré direcciones. Pregunta: ¿cómo agradecemos mejor a quienes nos enseñan?",
        ["escribe una atribución con fuente y autores", "dice quién lo puede ver según el permiso", "nombra dónde se guarda", "formula una pregunta para el educador/a tradicional"],
        ["atribución, acceso y almacenamiento escritos", "pregunta escrita o dicha en voz alta"],
        ["olvidar la atribución", "ampliar el acceso más allá del permiso"],
        "Verifica que respete el permiso y que no incluya datos personales; si amplió el acceso, repasen qué dijo la educadora y por qué.",
    ),
    reinforce="Escribe una frase de atribución con tus propias palabras para un trabajo del curso.",
    extend="Explica a una persona de tu casa por qué mostramos nuestro trabajo a la educadora antes de mostrarlo a otros.",
)
