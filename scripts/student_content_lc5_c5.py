"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS03 (comprender textos propios de su cultura, referidos a la realidad familiar, local y territorial, comentando
algunos elementos significativos y reconociendo palabras en lengua indígena o en castellano, culturalmente
significativas).

Criterio de autoría: los tres textos del cuaderno (familiar, local y territorial) y el cuarto de contraste son originales,
inventados solo para practicar y están rotulados como tales; no reproducen textos de ninguna editorial, comunidad ni
persona. Las únicas palabras en lengua indígena son saludos y palabras muy atestiguadas en mapuzugun (mari mari,
chaltumay, ko, mapu, ñuke, antü, kuyen, ruka), dadas con su glosa en la ficha. Las palabras del castellano de Chile (minga,
once) también se explican. No se inventa gramática ni significados rituales. Los textos reales de una comunidad quedan
para el docente, con permiso de esa comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS3 = "LC05 OA LS03"

CONSULT = " Recuerda: el sentido y el uso de las palabras de una lengua indígena los enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado. Puedes elegir un texto de una cultura que conozcas y no estás obligado a hablar de tu familia."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No exigir datos de la familia."

PALS = "Glosario de práctica: «ñuke» es madre, «ko» es agua, «mapu» es tierra, todas en mapuzugun, según la educadora tradicional. «Minga» es, en el castellano de Chile, un trabajo en que varias personas ayudan juntas. «Once» es la comida liviana de la tarde."
TA = "Texto A (inventado, realidad familiar): En mi casa, los domingos nos juntamos a la hora de once. Mi abuela prepara pan y nos cuenta cómo era el barrio cuando ella era niña. Dice que antes la gente hacía una minga cada vez que alguien construía una casa. Yo escucho con atención porque así aprendo cómo vivían. Mi abuela usa la palabra «ñuke» para hablar de su madre."
TB = "Texto B (inventado, realidad local): En el pueblo de Valle Claro, que no existe, hay una feria cada sábado. Las vecinas y los vecinos llevan verduras, pan y artesanías. Cerca de la entrada hay un cartel que dice «Bienvenidos» y «Mari mari». Una educadora tradicional explicó a los niños que ese saludo se usa al encontrarse con alguien. La feria termina a las dos de la tarde y todos ayudan a ordenar la plaza."
TC = "Texto C (inventado, realidad territorial): La Comunidad Ejemplo vive en un valle con un río, dos cerros y un bosque. La palabra «ko» se usa para hablar del agua y «mapu» para hablar de la tierra, según la educadora tradicional. En primavera las familias limpian el río en una minga. Se dice que cuidar el agua es cuidar el lugar donde se vive."


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


# ============================================================ LS03 clase 1 · situar el texto
L(
    LS3, 1,
    materials="Lápiz y hoja. Los textos están escritos aquí y son inventados para practicar. Puede leerlos en voz alta una persona adulta.",
    use="Aprenderé a ubicar un texto de la cultura según lo que cuenta: la realidad familiar, la realidad local o la realidad territorial, y a reconocer su fuente. Sirve para entender de qué habla un texto antes de comentarlo.",
    prior=["Sé ubicar pueblo, territorio y fuente.", "Sé que las palabras de una lengua indígena se copian como las enseñó su fuente."],
    explain=[
        "Un texto propio de una cultura habla de cosas reales de la vida de una comunidad. Puede referirse a la realidad familiar, que es lo que ocurre en una casa o familia; a la realidad local, que es lo que ocurre en un pueblo, barrio o escuela; o a la realidad territorial, que es lo que se relaciona con el lugar amplio donde vive una comunidad: ríos, cerros, bosques.",
        "Para ubicar un texto me pregunto: ¿de quién habla?, ¿dónde ocurre?, ¿quién lo escribió o lo contó?, ¿en qué lengua están sus palabras? En esta clase uso tres textos de práctica, inventados: el texto A es familiar, el B es local y el C es territorial. Los marco como inventados porque no pertenecen a ninguna persona real.",
        "Al leer, me fijo también en las palabras destacadas. Algunas son de una lengua indígena, como «ñuke», «ko» y «mapu», que están explicadas en el glosario. Otras son del castellano de Chile, como «minga» y «once». Si en un texto aparece una palabra que no está en el glosario, pregunto qué significa en vez de adivinar.",
    ],
    vocab=[("realidad familiar", "lo que ocurre en una casa o familia"), ("realidad local", "lo que ocurre en un pueblo, barrio o escuela"), ("realidad territorial", "lo que se relaciona con el lugar amplio donde vive una comunidad"), ("glosario", "lista de palabras con su significado"), ("texto", "conjunto de oraciones que dicen algo")],
    worked=[
        W("Clasificar un texto", PALS + " " + TB + " ¿El texto B habla de la realidad familiar, local o territorial?", ["Veo de qué habla: de una feria en un pueblo.", "Una feria de pueblo es algo que ocurre en un lugar compartido.", "Es la realidad local."], "local"),
        W("Reconocer una palabra del glosario", TA + " ¿Qué palabra del texto A está en el glosario como mapuzugun?", ["Busco una palabra entre comillas.", "Aparece «ñuke».", "El glosario dice que es madre."], "«ñuke», que significa madre"),
    ],
    mistakes=[
        M("Pensar que todos los textos de una cultura hablan solo de la familia.", "También hablan de lo local y del territorio.", "Pregunto si habla de la casa, del pueblo o del lugar amplio."),
        M("Adivinar el significado de una palabra que no está en el glosario.", "Puedo equivocarme y cambiar el sentido.", "Pregunto al educador o educadora tradicional."),
    ],
    R=[
        ex(TA + " ¿Qué día se juntan en la casa?", "los domingos", "El texto A lo dice."),
        ex(TB + " ¿Cuándo hay feria en Valle Claro?", "cada sábado", "El texto B lo dice."),
        ex(TC + " ¿Qué hay en el valle de la Comunidad Ejemplo?", "un río, dos cerros y un bosque", "El texto C lo dice."),
    ],
    C=[
        ex("Une cada texto con su tipo: A) texto A, B) texto B, C) texto C. Tipos: 1) territorial, 2) familiar, 3) local. Escribe los tres pares.", "A-2, B-3, C-1", "A habla de una casa, B de una feria del pueblo y C de un valle."),
        ex(PALS + " ¿Qué significa «ko» en el glosario?", "agua", "El glosario lo dice."),
        ex("Verdadero o falso: los textos de este cuaderno son inventados.", "Verdadero", "Están rotulados así."),
    ],
    A=[
        ex(TC + " " + PALS + " Con el glosario, ¿qué dos palabras de lengua indígena aparecen en el texto C?", "ko y mapu", "El texto C usa «ko» y «mapu»."),
        arith("En la feria de Valle Claro hay 14 puestos de verduras, 9 de pan y 6 de artesanías. ¿Cuántos puestos hay en total?", "14+9+6", "Se suman los tres tipos de puestos."),
        ex("Ordena para ubicar un texto: A) reviso las palabras en el glosario. B) leo de qué habla. C) decido si es familiar, local o territorial. Escribe las letras en orden.", "B, C, A", "Primero leo, luego decido el tipo y después reviso palabras."),
    ],
    Z=[
        ex(TB + " Un niño dice: «El texto B habla del territorio, porque menciona un pueblo». ¿Tiene razón? Sí o No.", "No", "Un pueblo y su feria son la realidad local."),
        ex("Encuentras en un texto la palabra «antü» sin glosario. ¿Qué es mejor: A) preguntar al educador o educadora tradicional o B) decir que significa lo que tú crees?", "A", "El significado lo enseña quien conoce la lengua."),
    ],
    D=[
        ex(TA + " ¿Qué elemento del texto A muestra una costumbre de ayuda entre vecinos: la minga o la once?", "la minga", "El texto dice que se hacía una minga al construir una casa."),
        ex(TC + " ¿Qué parte del texto C permite saber que es territorial: que habla de un valle con río y cerros o que habla de una once?", "que habla de un valle con río y cerros", "Los ríos y cerros son parte del territorio."),
    ],
    context=[ex("Te entregan un texto sobre una costumbre. Antes de comentarlo, ¿decides si habla de la familia, del pueblo o del territorio, o lo comentas sin leer de qué habla?", "decides si habla de la familia, del pueblo o del territorio", "Ubicar el texto va antes de comentarlo.")],
    selfcheck=[
        ex("Una feria de pueblo, ¿es realidad local o familiar?", "local", "Ocurre en un lugar compartido."),
        ex("¿El glosario sirve para saber el significado de las palabras? Sí o No.", "Sí", "Es una lista de palabras con su significado."),
        ex("Si una palabra no está en el glosario, ¿la adivino? Sí o No.", "No", "Se pregunta a quien enseña."),
    ],
    task=T(
        "Lee este texto D inventado: «En el barrio Los Pinos, que no existe, la escuela tiene un jardín. Cada otoño las familias que quieren ayudan a limpiarlo en una minga. Al final comparten una once. Un cartel en el jardín dice «Mari mari» y «Chaltumay», palabras que enseñó una educadora tradicional.» En tu cuaderno escribe: 1) el tipo de realidad (familiar, local o territorial) y por qué, 2) las palabras en lengua indígena y su significado según este cuaderno, 3) una palabra del castellano de Chile y su significado. Termina con una pregunta para el educador o educadora tradicional.",
        "Es local, porque habla de un barrio y su escuela. Palabras en lengua indígena: «mari mari» (saludo) y «chaltumay» (gracias). Palabra del castellano de Chile: «minga», trabajo en que varias personas ayudan juntas. Pregunta: ¿qué otras palabras de la lengua se usan en nuestra escuela?",
        ["clasifica el texto con una razón", "nombra las palabras con su significado", "distingue lengua indígena y castellano", "formula una pregunta"],
        ["tres respuestas escritas", "pregunta"],
        ["adivinar significados", "no distinguir lengua"],
        "Verifica que cada significado venga de este cuaderno o de la fuente y no sea inventado.",
    ),
    reinforce="Relee los textos A, B y C y subraya con un color las palabras del glosario.",
    extend="Escribe un texto de cuatro oraciones sobre la realidad local de tu barrio o escuela y dile a una persona de tu casa de qué tipo de realidad habla.",
)

# ============================================================ LS03 clase 2 · comprender con límites declarados
L(
    LS3, 2,
    materials="Lápiz y hoja. Los textos están escritos aquí y son inventados para practicar.",
    use="Aprenderé a comprender un texto cultural con detalle: qué dice con claridad, qué se puede deducir con pistas y qué el texto no dice. Sirve para comentar sin inventar.",
    prior=["Sé ubicar un texto como familiar, local o territorial.", "Sé usar un glosario."],
    explain=[
        "Comprender un texto es entender lo que dice. Hay tres niveles. Lo que el texto dice con claridad se llama información explícita, como «la feria termina a las dos». Lo que puedo deducir con pistas del texto se llama inferencia, como «la feria es importante para el pueblo porque todos ayudan a ordenar la plaza». Y hay cosas que el texto no dice: no puedo saber cuántas personas van a la feria si no lo informa.",
        "Para no inventar, hago tres cosas. Subrayo la oración que sostiene mi respuesta. Compruebo que la inferencia tenga una pista. Y declaro los límites: «el texto no dice cuántas personas van». Un límite no es un error, sino una forma honesta de leer. Si necesito más información, pregunto a una persona de mi comunidad o al educador tradicional.",
        "En un texto cultural también hay palabras del castellano de Chile y de lenguas indígenas. Las busco en el glosario o pregunto. Cuando una palabra explica una costumbre, como «minga», la relaciono con lo que el texto cuenta. Así comprendo mejor el sentido de la costumbre en el texto.",
    ],
    vocab=[("información explícita", "lo que el texto dice con claridad"), ("inferencia", "lo que deduzco con pistas del texto"), ("pista", "dato del texto que apoya una conclusión"), ("límite", "lo que el texto no dice"), ("subrayar", "marcar una oración con una línea")],
    worked=[
        W("Responder con información explícita", TB + " ¿A qué hora termina la feria?", ["Busco la hora en el texto.", "Dice: la feria termina a las dos de la tarde.", "Esa es la información explícita."], "a las dos de la tarde"),
        W("Hacer una inferencia con pista", TB + " ¿Por qué se puede pensar que la feria es importante para el pueblo?", ["Busco una pista: todos ayudan a ordenar la plaza.", "Si todos ayudan, es importante para ellos.", "Es una inferencia con pista."], "porque todos ayudan a ordenar la plaza"),
    ],
    mistakes=[
        M("Responder algo que el texto no dice, como cuántas personas van.", "El texto no entrega ese dato.", "Digo «el texto no lo dice»."),
        M("Hacer una inferencia sin pista.", "Es solo una idea mía.", "Busco una pista en el texto antes de concluir."),
    ],
    R=[
        ex(TA + " ¿Qué prepara la abuela?", "pan", "El texto A lo dice."),
        ex(TC + " ¿Qué hacen las familias en primavera?", "limpian el río en una minga", "El texto C lo dice."),
        ex(TB + " ¿Qué dice el cartel de la feria?", "«Bienvenidos» y «Mari mari»", "El texto B lo dice."),
    ],
    C=[
        ex("Clasifica con E (explícita) o I (inferencia): 1) la feria termina a las dos. 2) la feria es importante para el pueblo. 3) hay una feria cada sábado. Usa el texto B. Escribe las tres letras.", "1 E, 2 I, 3 E", "Las 1 y 3 están escritas; la 2 se deduce."),
        ex(TA + " ¿Para qué usa la abuela la palabra «ñuke»?", "para hablar de su madre", "El texto A lo dice."),
        ex(TC + " Según el texto C, ¿qué se dice que es cuidar el agua?", "cuidar el lugar donde se vive", "El texto C lo dice."),
    ],
    A=[
        ex(TB + " ¿El texto B dice cuántas personas van a la feria? Sí o No.", "No", "No entrega ese dato."),
        arith("Supón que una feria empieza a las 10 y termina a las 14 horas. ¿Cuántas horas dura?", "14-10", "Se resta la hora de inicio de la hora de término."),
        ex(TA + " Elige la inferencia con pista: A) «La abuela es importante para la familia, porque quien narra escucha con atención sus historias». B) «La abuela tiene 90 años». Escribe la letra.", "A", "A tiene una pista en el texto; B no."),
    ],
    Z=[
        ex(TC + " Un niño dice: «El texto C dice que todos los pueblos limpian los ríos en primavera». ¿Lo dice el texto? Sí o No.", "No", "Habla solo de la Comunidad Ejemplo."),
        ex(TA + " Una niña concluye: «La abuela vivió siempre en el mismo barrio». ¿Tiene pista en el texto? Sí o No.", "No", "El texto no informa dónde vivió siempre."),
    ],
    D=[
        ex(TB + " Elige el mejor límite que declarar al comentar: A) «El texto no dice qué se vende en cada puesto». B) «El texto es malo». Escribe la letra.", "A", "A señala algo que el texto no informa."),
        ex(TC + " Si quieres saber qué otras costumbres tiene esa comunidad, ¿qué haces: A) preguntas a una persona de la comunidad o al educador tradicional o B) lo inventas?", "A", "Más información se pregunta a quien conoce."),
    ],
    context=[ex("Lees un texto sobre tu barrio y alguien te pregunta algo que el texto no dice. ¿Respondes «el texto no lo dice» o inventas una respuesta?", "respondes «el texto no lo dice»", "Leer con honestidad es declarar los límites.")],
    selfcheck=[
        ex("Lo que el texto dice con claridad, ¿es explícito o una inferencia?", "explícito", "Está escrito con claridad en el texto."),
        ex("¿Una inferencia necesita una pista del texto? Sí o No.", "Sí", "Si no, es solo una idea mía."),
        ex("Si el texto no informa algo, ¿lo invento? Sí o No.", "No", "Declaro el límite."),
    ],
    task=T(
        "Lee este texto E inventado: «En la escuela Camino Alto, que no existe, los jueves el curso riega el huerto. Un cartel junto a la llave de agua dice «ko» y otro cartel, en la puerta, dice «chaltumay», palabras que enseñó una educadora tradicional. A veces el huerto da lechugas y otras veces no.» En tu cuaderno escribe: dos datos explícitos, una inferencia con su pista y un límite. Usa el glosario de esta clase. Termina con una pregunta para el educador o educadora tradicional.",
        "Explícitos: los jueves riegan el huerto; hay carteles con «ko» y «chaltumay». Inferencia: el huerto es importante para el curso, porque lo riegan todas las semanas. Límite: el texto no dice cuántas lechugas da. Pregunta: ¿cómo se usa la palabra «ko» en nuestra comunidad?",
        ["dos datos explícitos correctos", "inferencia con pista", "límite claro", "formula una pregunta"],
        ["datos, inferencia y límite escritos", "pregunta"],
        ["inferir sin pista", "confundir explícito con inferencia"],
        "Pide que subraye en el texto la pista de su inferencia.",
    ),
    reinforce="Relee el texto B y subraya con un color la información explícita y con otro las pistas de una inferencia.",
    extend="Escribe una inferencia con pista y un límite para el texto C.",
)

# ============================================================ LS03 clase 3 · relaciones culturales: elementos significativos
L(
    LS3, 3,
    materials="Lápiz y hoja. Los textos están escritos aquí y son inventados para practicar.",
    use="Aprenderé a identificar elementos significativos de un texto cultural (lugares, costumbres, personas, palabras) y a explicar por qué importan para la comunidad. Sirve para comentar un texto con razones.",
    prior=["Sé distinguir lo explícito de la inferencia.", "Sé usar el glosario."],
    explain=[
        "Un elemento significativo es algo del texto que tiene valor para la comunidad de la que habla. Puede ser un lugar, como el río del texto C; una costumbre, como la minga; una persona, como la abuela del texto A o la educadora tradicional del texto B; o una palabra, como «ñuke», «ko» o «mapu». Los elementos significativos me ayudan a entender qué cuida o valora esa comunidad.",
        "Para comentar un elemento, hago tres pasos. Primero lo nombro. Segundo, explico por qué importa con una pista del texto: «el río importa porque las familias lo limpian en primavera». Tercero, lo relaciono con otro elemento: «la minga y el río se relacionan porque la minga sirve para cuidar el río». Así muestro relaciones entre elementos.",
        "Cuando comento, no hablo en nombre de la comunidad. Digo «según el texto». Y no explico significados espirituales ni profundos si el texto no los da. Si quiero saber más sobre un elemento de una cultura, lo pregunto a una persona de esa comunidad o al educador tradicional.",
    ],
    vocab=[("elemento significativo", "algo del texto que tiene valor para la comunidad"), ("relacionar", "unir dos ideas porque tienen conexión"), ("comentar", "decir lo que pienso con razones"), ("costumbre", "algo que una comunidad hace y repite"), ("valorar", "reconocer que algo importa")],
    worked=[
        W("Nombrar elementos", TC + " Nombra dos lugares significativos del texto C.", ["Busco lugares: el valle, el río, los cerros, el bosque.", "El texto resalta el río y el agua.", "Nombro el río y el valle."], "por ejemplo, el río y el valle"),
        W("Explicar con una pista", TC + " ¿Por qué importa el río para la Comunidad Ejemplo?", ["Busco una pista: las familias lo limpian en primavera.", "Si lo limpian juntas, lo cuidan.", "Y el texto dice que cuidar el agua es cuidar el lugar donde se vive."], "porque las familias lo limpian y cuidar el agua es cuidar el lugar donde se vive"),
    ],
    mistakes=[
        M("Decir que algo es importante sin dar una pista del texto.", "Es solo mi idea.", "Escribo «según el texto…» y doy la pista."),
        M("Explicar un significado espiritual que el texto no da.", "No puedo saberlo desde el texto.", "Comento solo lo que el texto dice y pregunto al educador por lo demás."),
    ],
    R=[
        ex(TC + " ¿Qué hacen las familias con el río en primavera?", "lo limpian", "El texto lo dice."),
        ex(TA + " ¿Quién cuenta cómo era el barrio?", "la abuela", "El texto A lo dice."),
        ex(PALS + " ¿Qué quiere decir «mapu»?", "tierra", "El glosario lo dice."),
    ],
    C=[
        ex("Clasifica con L (lugar), C (costumbre), P (persona) o W (palabra): 1) el río. 2) la minga. 3) la educadora tradicional. 4) «ñuke». Escribe las cuatro letras.", "1 L, 2 C, 3 P, 4 W", "Cada elemento es de un tipo distinto."),
        ex(TB + " ¿Qué elemento del texto B muestra respeto por una lengua indígena: el cartel con «Mari mari» o la lista de verduras?", "el cartel con «Mari mari»", "El cartel usa un saludo en mapuzugun."),
        ex(TC + " ¿Qué dice el texto C sobre cuidar el agua?", "que es cuidar el lugar donde se vive", "Es la última oración."),
    ],
    A=[
        ex(TC + " " + PALS + " Une cada elemento con su relación: A) minga, B) «ko», C) río. Relaciones: 1) palabra para hablar del agua, 2) lugar que se cuida, 3) costumbre para cuidar. Escribe los tres pares.", "A-3, B-1, C-2", "Según los textos, la minga cuida el río, «ko» es agua y el río es un lugar."),
        arith("El texto C nombra 4 lugares (valle, río, cerros y bosque) y 2 palabras de lengua indígena. ¿Cuántos lugares y palabras de lengua indígena hay en total?", "4+2", "Se suman lugares y palabras."),
        ex(TB + " Elige la mejor explicación de por qué importa la feria: A) «Según el texto, importa porque todos ayudan a ordenar la plaza». B) «Importa porque es la mejor del país». Escribe la letra.", "A", "A usa una pista del texto."),
    ],
    Z=[
        ex(TA + " Un niño dice: «En el texto A, la minga se hace solo en verano». ¿Lo dice el texto? Sí o No.", "No", "El texto solo dice que se hacía una minga cuando alguien construía una casa."),
        ex(TC + " Una niña dice: «El río y la minga se relacionan, porque la minga sirve para limpiar el río». ¿Tiene una pista del texto? Sí o No.", "Sí", "El texto dice que las familias limpian el río en una minga."),
    ],
    D=[
        ex(TA + " " + TC + " ¿Qué costumbre aparece en los dos textos: la minga o la feria?", "la minga", "Aparece en A y en C."),
        ex(TB + " ¿Cuál de estos elementos del texto B es una palabra de una lengua indígena: «Mari mari» o «Bienvenidos»?", "«Mari mari»", "Según el texto, «Mari mari» es un saludo que enseñó una educadora tradicional; «Bienvenidos» es castellano."),
    ],
    context=[ex("Lees un texto sobre una costumbre de tu barrio. ¿Dices por qué un elemento importa usando una pista del texto o solo dices que te parece importante?", "dices por qué importa usando una pista del texto", "Los comentarios necesitan una razón del texto.")],
    selfcheck=[
        ex("Un elemento significativo, ¿tiene valor para la comunidad? Sí o No.", "Sí", "Así se definió."),
        ex("Al comentar, ¿uso «según el texto»? Sí o No.", "Sí", "Así atribuyo lo que digo al texto."),
        ex("¿Debo explicar un significado espiritual que el texto no da? Sí o No.", "No", "Comento solo lo que dice el texto."),
    ],
    task=T(
        "Lee este texto F inventado: «En un cerro inventado llamado Alto Verde, la comunidad de la Escuela Ejemplo planta árboles cada primavera en una minga. La profesora cuenta que el cerro les da sombra y agua. Un letrero dice «Mari mari» en la entrada y «Chaltumay» en la salida, palabras que enseñó una educadora tradicional.» En tu cuaderno haz una tabla de tres columnas: elemento significativo, tipo (lugar, costumbre, persona o palabra) y por qué importa según el texto. Incluye al menos cuatro elementos. Termina con una pregunta para el educador o educadora tradicional.",
        "Cerro Alto Verde / lugar / les da sombra y agua. Minga de plantar árboles / costumbre / cuidan el cerro entre todos. Profesora / persona / cuenta lo que da el cerro. «Mari mari» y «chaltumay» / palabras / se usan en el letrero, enseñadas por una educadora tradicional. Pregunta: ¿qué lugares son importantes en nuestra comunidad?",
        ["identifica al menos cuatro elementos", "los clasifica bien", "explica por qué importa con una pista", "formula una pregunta"],
        ["tabla de tres columnas", "pregunta"],
        ["explicar sin pista", "inventar significados"],
        "Pide que señale en el texto la pista de cada explicación.",
    ),
    reinforce="Relee el texto C y haz una lista de sus elementos significativos.",
    extend="Escribe un párrafo de cuatro oraciones que relacione dos elementos del texto A, usando «según el texto».",
)

# ============================================================ LS03 clase 4 · comentario atribuido con evidencia
L(
    LS3, 4,
    materials="Lápiz y hoja. Los textos están escritos aquí y son inventados para practicar.",
    use="Aprenderé a escribir un comentario breve sobre un texto cultural: decir qué elemento comento, citar una frase del texto como evidencia, explicar por qué importa y declarar el límite. Sirve para comentar con orden y sin inventar.",
    prior=["Sé identificar elementos significativos.", "Sé declarar límites al leer."],
    explain=[
        "Un comentario atribuido tiene cuatro partes. Primero, nombro el elemento que comento: «Comento el río del texto C». Segundo, cito la evidencia, es decir, una frase del texto que lo sostiene: «el texto dice que las familias limpian el río en una minga». Tercero, explico por qué importa: «Importa porque cuidar el agua es cuidar el lugar donde se vive». Cuarto, declaro el límite: «El texto no dice cuántas familias participan».",
        "Cuando cito una frase del texto, la copio igual y la pongo entre comillas, o la resumo diciendo «el texto dice…». No cambio las palabras en lengua indígena ni invento otras. Si mi comentario incluye una opinión mía, la marco con «yo pienso». Así se distingue lo que dice el texto de lo que pienso yo.",
        "Antes de entregar mi comentario, lo reviso: ¿nombré el elemento?, ¿incluí la evidencia?, ¿expliqué por qué importa?, ¿declaré un límite? Si falta algo, lo agrego. Y si el texto es real y de una comunidad, pido que alguien de la comunidad o el educador tradicional lo revise antes de mostrarlo.",
    ],
    vocab=[("evidencia", "frase o dato del texto que apoya lo que digo"), ("citar", "copiar una frase del texto entre comillas"), ("comentario", "texto breve en que explico lo que pienso con razones"), ("límite", "lo que el texto no dice"), ("revisar", "mirar de nuevo para corregir")],
    worked=[
        W("Armar el comentario", TC + " Escribe la evidencia para comentar el río.", ["Busco la frase que habla del río.", "Dice: las familias limpian el río en una minga.", "La cito: «el texto dice que las familias limpian el río en una minga»."], "«el texto dice que las familias limpian el río en una minga»"),
        W("Detectar la parte faltante", "Un comentario dice: «Comento la feria. Importa porque es muy bonita». ¿Qué parte falta?", ["Hay elemento: la feria.", "Hay explicación débil: «es muy bonita» no es evidencia.", "Faltan la evidencia del texto y el límite."], "faltan la evidencia del texto y el límite"),
    ],
    mistakes=[
        M("Comentar sin citar ninguna frase del texto.", "No se puede comprobar de dónde sale la idea.", "Cito una frase o escribo «el texto dice…»."),
        M("Cambiar una palabra de la lengua indígena al citar.", "Se cambia lo que enseñó la fuente.", "Copio la palabra tal cual."),
    ],
    R=[
        ex(TB + " ¿Cuál es una frase del texto B que habla del saludo en el cartel?", "Cerca de la entrada hay un cartel que dice «Bienvenidos» y «Mari mari»", "Es la oración del cartel."),
        ex("La evidencia en un comentario, ¿es una frase del texto que apoya mi idea o una opinión sin razón?", "una frase del texto que apoya mi idea", "Así se definió evidencia."),
        ex("Citar, ¿es copiar una frase del texto entre comillas o cambiarla?", "copiar una frase del texto entre comillas", "Así se definió citar."),
    ],
    C=[
        ex("¿Qué parte del comentario es la frase del texto que apoya mi idea: el elemento, la evidencia o el límite?", "la evidencia", "La evidencia es la frase del texto que sostiene lo que digo."),
        ex(TC + " Verdadero o falso: para comentar el río puedo citar «las familias limpian el río en una minga».", "Verdadero", "Es una frase del texto C."),
        ex("¿Dónde marco mi opinión en un comentario: con «yo pienso» o escondida en la evidencia?", "con «yo pienso»", "Así se distingue de lo que dice el texto."),
    ],
    A=[
        ex("Ordena las partes del comentario: A) límite. B) evidencia. C) elemento. D) importancia. Escribe las letras en orden.", "C, B, D, A", "Nombro, cito, explico y declaro el límite."),
        ex(TA + " Elige el mejor comentario: A) «Comento la minga del texto A. El texto dice que antes la gente hacía una minga cuando alguien construía una casa. Importa porque era una forma de ayudarse. El texto no dice cuántas personas participaban». B) «La minga es lo mejor del mundo». Escribe la letra.", "A", "A tiene las cuatro partes."),
        arith("Un curso escribe 28 comentarios. 4 no tienen límite. ¿Cuántos comentarios sí tienen límite?", "28-4", "Se restan los que no lo tienen del total."),
    ],
    Z=[
        ex(TC + " Una niña cita: «las familias limpian el río en una minga» pero escribe «la minga se hace en todo Chile». ¿Eso está en el texto? Sí o No.", "No", "El texto C solo habla de la Comunidad Ejemplo."),
        ex(TA + " " + PALS + " Un niño quiere escribir la palabra de otra manera al citar el texto A, que la escribe «ñuke». ¿Debe copiarla tal cual del texto? Sí o No.", "Sí", "Se copia la palabra como la enseñó la fuente."),
    ],
    D=[
        ex(TB + " Un comentario dice: «Comento la feria. El texto dice que los vecinos ayudan a ordenar la plaza. Importa porque une a las personas». ¿Qué parte le falta: el límite o el elemento?", "el límite", "Tiene elemento, evidencia e importancia."),
        ex(TA + " Para el comentario de la abuela, ¿qué es mejor límite: A) «El texto no dice cuántos años tiene la abuela» o B) «La abuela es muy importante»?", "A", "Un límite señala algo que el texto no dice."),
    ],
    context=[ex("Vas a comentar un texto sobre una costumbre de tu comunidad. ¿Citas una frase del texto o solo das tu opinión?", "citas una frase del texto", "Los comentarios se apoyan en evidencia del texto.")],
    selfcheck=[
        ex("¿Cuál es la última parte del comentario: el límite o el elemento?", "el límite", "Primero nombro y al final declaro el límite."),
        ex("¿Cambio las palabras indígenas al citar? Sí o No.", "No", "Se copian tal cual."),
        ex("¿Marco mis opiniones con «yo pienso»? Sí o No.", "Sí", "Así no se confunden con el texto."),
    ],
    task=T(
        "Lee el texto B de esta clase (la feria de Valle Claro). En tu cuaderno escribe un comentario de cuatro oraciones sobre un elemento significativo que elijas. Debe tener: el elemento que comentas, una frase del texto como evidencia (puedes empezar con «el texto dice»), por qué importa y un límite. Agrega una frase de «yo pienso». Termina con una pregunta para el educador o educadora tradicional sobre palabras de la lengua en lugares públicos.",
        "Comento el cartel de la entrada. El texto dice que cerca de la entrada hay un cartel con «Bienvenidos» y «Mari mari». Importa porque muestra respeto por una lengua indígena en un lugar compartido. El texto no dice quién hizo el cartel. Yo pienso que es una buena forma de recibir. Pregunta: ¿qué palabras de la lengua conviene poner en un cartel de nuestra comunidad?",
        ["nombra el elemento", "cita evidencia del texto", "explica por qué importa", "declara el límite y marca lo propio"],
        ["comentario de cuatro oraciones", "pregunta"],
        ["comentar sin evidencia", "inventar significados"],
        "Pide que subraye en el texto la frase usada como evidencia.",
    ),
    reinforce="Copia el comentario modelo y subraya con un color cada una de sus cuatro partes.",
    extend="Escribe un comentario sobre el texto A con las cuatro partes y compáralo con el de un compañero.",
)

# ============================================================ LS03 clase 5 · contrastar textos sin jerarquizar
TD = "Texto D (inventado, realidad territorial, otro valle): La Comunidad Muestra vive cerca de un lago, rodeado de pastizales. Las familias cuidan el lago y llevan a sus animales a pastar en verano. Según el educador tradicional de la escuela, la palabra «ko» se usa para hablar del agua. En otoño cada familia limpia la orilla durante una minga."

L(
    LS3, 5,
    materials="Lápiz y hoja. Los textos están escritos aquí y son inventados para practicar.",
    use="Aprenderé a comparar dos textos culturales de territorios distintos, mirando parecidos y diferencias en elementos y palabras, sin decir cuál es mejor. Sirve para valorar la diversidad de los territorios.",
    prior=["Sé comentar un elemento con evidencia.", "Sé que cada comunidad cuenta lo suyo."],
    explain=[
        "Dos textos de territorios distintos pueden hablar de lo mismo de maneras diferentes. El texto C habla de un valle con un río y cerros; el texto D, de un lago con pastizales. En los dos se cuida el agua y se hace una minga, pero en estaciones distintas: primavera en uno y otoño en otro. Esas diferencias no hacen a un territorio mejor que otro.",
        "Para contrastar uso una tabla de tres columnas: igual, distinto y evidencia. En cada celda escribo una frase del texto. Por ejemplo, igual: «ambos usan la palabra “ko” para el agua». Distinto: «uno limpia el río en primavera y el otro la orilla del lago en otoño». La evidencia es la frase del texto que lo sostiene.",
        "No jerarquizo. No digo que el valle sea más importante que el lago, ni que una comunidad cuide mejor. Describo lo que dice cada texto. Y declaro el límite: dos textos no representan a todas las comunidades. Si quiero saber cómo es otra comunidad, pregunto a sus integrantes o al educador tradicional.",
    ],
    vocab=[("territorio", "lugar amplio donde vive una comunidad"), ("contrastar", "comparar para ver parecidos y diferencias"), ("jerarquizar", "ordenar en mejor y peor"), ("estación", "cada una de las cuatro partes del año"), ("tabla comparativa", "cuadro para ordenar parecidos y diferencias")],
    worked=[
        W("Encontrar lo igual", TC + " " + TD + " ¿Qué costumbre tienen en común los textos C y D?", ["Busco una costumbre que aparezca en ambos.", "En C las familias limpian el río en una minga.", "En D limpian la orilla en una minga."], "una minga para cuidar el agua"),
        W("Encontrar lo distinto", TC + " " + TD + " ¿En qué estación hacen la minga las comunidades de C y D?", ["En C es en primavera.", "En D es en otoño.", "Son estaciones distintas."], "C en primavera y D en otoño"),
    ],
    mistakes=[
        M("Decir que un territorio es más importante que otro.", "Cada territorio importa a su comunidad.", "Describo lo que dice cada texto sin ordenarlos."),
        M("Pensar que dos textos representan a todas las comunidades.", "Solo hablan de dos comunidades.", "Declaro el límite: solo hablan de estas dos."),
    ],
    R=[
        ex(TD + " ¿Qué hay cerca de la Comunidad Muestra?", "un lago", "El texto D lo dice."),
        ex(TD + " ¿Qué palabra se usa para hablar del agua?", "ko", "El texto D lo dice."),
        ex(TC + " ¿Qué hay en el valle de la Comunidad Ejemplo?", "un río, dos cerros y un bosque", "El texto C lo dice."),
    ],
    C=[
        ex(TC + " " + TD + " Verdadero o falso: en los dos textos se usa la palabra «ko».", "Verdadero", "Los dos la mencionan para hablar del agua."),
        ex(TC + " " + TD + " ¿En qué estación limpia el agua la comunidad del texto D?", "en otoño", "El texto D lo dice."),
        ex("Contrastar, ¿es comparar para ver parecidos y diferencias o elegir el mejor?", "comparar para ver parecidos y diferencias", "Así se definió contrastar."),
    ],
    A=[
        ex(TC + " " + TD + " Clasifica con I (igual) o D (distinto): 1) ambas comunidades hacen una minga. 2) una vive junto a un río y otra junto a un lago. 3) ambas usan «ko» para hablar del agua. Escribe las tres letras.", "1 I, 2 D, 3 I", "La 2 es la única diferencia."),
        arith("La tabla comparativa tiene 8 filas. 5 son «igual». ¿Cuántas son «distinto»?", "8-5", "Se restan las iguales del total."),
        ex(TC + " " + TD + " Elige la frase que compara sin jerarquizar: A) «En el texto C se limpia el río en primavera y en el texto D la orilla del lago en otoño». B) «El territorio del texto C es mejor». Escribe la letra.", "A", "A solo describe."),
    ],
    Z=[
        ex("Una niña dice: «Como los dos textos hablan de una minga, todas las comunidades hacen una minga». ¿Qué falla: generaliza a todas las comunidades o confunde las estaciones? Escribe la que corresponde.", "generaliza a todas las comunidades", "Dos textos no representan a todas las comunidades."),
        ex(TC + " " + TD + " Un niño dice: «La Comunidad Muestra cuida mejor porque limpia en otoño». ¿Hay evidencia en los textos de que cuide mejor? Sí o No.", "No", "Los textos no comparan quién cuida mejor."),
    ],
    D=[
        ex(TC + " " + TD + " ¿Qué dato aparece en D y no en C: que las familias llevan a sus animales a pastar en verano o que hay una minga?", "que las familias llevan a sus animales a pastar en verano", "La minga aparece en ambos."),
        ex("Un curso compara un texto de práctica con un texto real de una comunidad, con permiso. ¿Qué debe hacer: A) citar la fuente y describir sin ordenar en mejor y peor o B) decir cuál es más auténtico?", "A", "Se contrasta con fuente y sin jerarquizar."),
    ],
    context=[ex("Tu curso recibe dos textos de dos comunidades distintas sobre una misma costumbre. ¿Los comparas diciendo qué tienen igual y distinto o dices cuál comunidad lo hace mejor?", "los comparas diciendo qué tienen igual y distinto", "Se compara sin ordenar en mejor y peor.")],
    selfcheck=[
        ex("¿Se puede decir que un territorio es mejor que otro? Sí o No.", "No", "Cada territorio importa a su comunidad."),
        ex("En la tabla, ¿qué columna muestra los parecidos: igual o distinto?", "igual", "Igual muestra lo que se comparte."),
        ex("Dos textos, ¿representan a todas las comunidades? Sí o No.", "No", "Solo hablan de dos."),
    ],
    task=T(
        "Lee estos dos textos inventados. Texto G: «En la Comunidad Alta, junto a una montaña, las familias cuidan una vertiente y la limpian en invierno en una minga; usan la palabra «ko» para hablar del agua». Texto H: «En la Comunidad Baja, junto a un estero, las familias cuidan el estero y lo limpian en verano en una minga; usan la palabra «ko» para hablar del agua». En tu cuaderno haz una tabla de tres columnas (igual, distinto, evidencia) con al menos dos filas por columna. Escribe luego dos frases que comparen sin decir cuál es mejor. Termina con una pregunta para el educador o educadora tradicional.",
        "Igual: ambas cuidan el agua con una minga y usan «ko». Distinto: una cuida una vertiente en invierno y la otra un estero en verano. Evidencia: frases de los textos. Frases: La Comunidad Alta limpia su vertiente en invierno. La Comunidad Baja limpia su estero en verano. Pregunta: ¿cómo cuidan el agua en nuestra comunidad?",
        ["identifica lo igual y lo distinto", "da evidencia del texto", "compara sin jerarquizar", "formula una pregunta"],
        ["tabla de tres columnas", "dos frases comparativas"],
        ["decir cuál comunidad es mejor", "olvidar la evidencia"],
        "Si aparece un juicio de valor, pide que lo reemplace por una descripción.",
    ),
    reinforce="Relee los textos C y D y subraya con un color lo igual y con otro lo distinto.",
    extend="Escribe un párrafo de cuatro oraciones que explique por qué dos comunidades pueden cuidar el agua de maneras distintas y por qué eso es valioso.",
)
