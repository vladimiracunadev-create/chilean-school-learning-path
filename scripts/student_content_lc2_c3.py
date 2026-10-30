"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS03 (textos en castellano con palabras de culturas originarias), LS04 (escritura de palabras con elementos
significativos de la cultura) y LS05 (recursos tecnológicos para escuchar y ver aspectos de la cultura).

Criterio de autoría: los textos, fichas y descripciones de recursos son inventados para practicar y se declaran como
tales. Las palabras de origen indígena usadas son de uso general en el castellano de Chile y su origen es amplio y
conocido: del quechua (choclo, palta, papa, guagua, cóndor, puma, llama, pampa) y del mapuzugun (copihue, pudú).
No se inventan significados, ritos ni gramática. Cada tarea abierta remite al educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS3, LS4, LS5 = "LC02 OA LS03", "LC02 OA LS04", "LC02 OA LS05"

CONSULT = " Recuerda: el significado cultural de las palabras, su escritura en cada lengua y su pronunciación las enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

FICHA_ORI = ("Ficha de origen: «choclo» (maíz tierno), «palta» (fruta de pulpa verde), «papa», «guagua» (bebé), «cóndor» (ave grande de los Andes), "
             "«puma», «llama» y «pampa» (llanura) vienen del quechua, una lengua de los Andes. «Copihue» (flor roja del sur) y «pudú» (ciervo muy pequeño) vienen del mapuzugun.")


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


# =================================================================== LS03 · textos con palabras de culturas originarias
L(
    LS3, 1,
    materials="Lápiz y hoja. Los textos de práctica y la ficha de origen están escritos aquí; los textos son inventados.",
    use="Aprenderé a encontrar en un texto en castellano las palabras que vienen de lenguas originarias. Sirve para darme cuenta de cuánto de nuestra lengua cotidiana viene de otras culturas.",
    prior=["Sé leer un texto corto en castellano.", "Sé qué es una fuente."],
    explain=[
        "El castellano que hablamos en Chile tiene muchas palabras que vienen de lenguas originarias. Las usamos todos los días sin pensarlo. Por ejemplo: choclo, palta, papa, guagua, cóndor, puma, llama, pampa, copihue y pudú.",
        "Una palabra de origen indígena es una palabra que llegó al castellano desde una lengua de un pueblo originario. Esa lengua puede ser el quechua o el mapuzugun, por ejemplo. Para saber el origen de una palabra miro una ficha o un diccionario; no lo adivino.",
        "Cuando leo un texto, busco esas palabras y las marco. Después leo la ficha de origen y veo de qué lengua vienen. Así reconozco que estas palabras son parte de la cultura de esos pueblos y las uso con respeto.",
    ],
    vocab=[("origen", "lugar o lengua de donde viene una palabra"), ("quechua", "lengua de los Andes, hablada por el pueblo quechua"), ("mapuzugun", "lengua del pueblo mapuche"), ("diccionario", "libro que explica palabras"), ("cotidiano", "de todos los días")],
    worked=[
        W("Marcar las palabras", "Texto de práctica (inventado): «En la feria compramos choclo y palta para la cena.» " + FICHA_ORI + " ¿Qué palabras vienen de una lengua originaria?", ["Leo el texto y busco palabras de la ficha.", "Encuentro «choclo».", "También encuentro «palta»."], "choclo y palta"),
        W("Buscar el origen", "En el texto aparece «cóndor». ¿De qué lengua viene según la ficha?", ["Busco «cóndor» en la ficha.", "Dice que viene del quechua.", "El origen es el quechua."], "del quechua"),
    ],
    mistakes=[
        M("Pensar que una palabra no es de otra lengua porque la usamos todos los días.", "Llegó hace tiempo y ya parece castellano.", "Reviso la ficha de origen."),
        M("Decir el origen de una palabra sin revisar una fuente.", "Puedo equivocarme.", "Uso la ficha o un diccionario."),
    ],
    R=[
        ex("Texto de práctica (inventado): «La guagua duerme.» " + FICHA_ORI + " ¿Qué palabra viene de una lengua originaria?", "guagua", "La ficha dice que «guagua» viene del quechua."),
        ex(FICHA_ORI + " ¿De qué lengua viene «copihue»?", "del mapuzugun", "La ficha lo dice."),
        ex("¿Dónde reviso el origen de una palabra: en una ficha o lo adivino?", "en una ficha", "Una ficha o un diccionario me da el dato."),
    ],
    C=[
        ex("Texto: «En el cerro vimos un cóndor y una llama.» " + FICHA_ORI + " ¿Cuántas palabras de origen indígena hay?", "2", "«Cóndor» y «llama» son las dos."),
        ex("Verdadero o falso: «papa» es una palabra de origen quechua según la ficha.", "Verdadero", "La ficha dice que viene del quechua."),
        ex(FICHA_ORI + " ¿Qué es un pudú?", "un ciervo muy pequeño", "La ficha dice que es un ciervo muy pequeño."),
    ],
    A=[
        ex("Texto de práctica (inventado): «Ayer comí choclo, papa y pan.» " + FICHA_ORI + " ¿Qué palabra del texto NO es de origen indígena?", "pan", "«Pan» no está en la ficha."),
        ex("Texto: «En la pampa vimos un puma.» " + FICHA_ORI + " ¿Cuántas palabras vienen del quechua?", "2", "«Pampa» y «puma» vienen del quechua."),
        ex("Texto: «El pudú se escondió entre los copihues.» " + FICHA_ORI + " ¿De qué lengua vienen las dos palabras indígenas?", "del mapuzugun", "La ficha dice que ambas vienen del mapuzugun."),
    ],
    Z=[
        ex("Tomás dice: «Palta es una palabra inventada por mi familia». ¿Qué le muestra la ficha?", "que viene del quechua", "La ficha dice que «palta» viene del quechua."),
        ex("¿Por qué conviene revisar una ficha o diccionario para saber el origen de una palabra?", "para no equivocarme", "Evita decir un dato falso."),
    ],
    D=[
        ex("La ficha tiene 10 palabras de origen indígena y ya encontraste 6 en un texto. ¿Cuántas faltan de encontrar?", "4", "10 − 6 = 4 palabras."),
        ex("Texto: «El cóndor y el puma son animales de los Andes.» ¿Qué dos palabras podrías marcar como de origen quechua?", "cóndor y puma", "Ambas están en la ficha."),
    ],
    context=[ex("En el almuerzo, tu familia comenta que sirvieron choclo y palta. Tu hermana dice que son palabras de otra lengua. ¿De cuál, según la ficha?", "del quechua", "La ficha dice que ambas vienen del quechua.")],
    selfcheck=[
        ex("¿Qué es una palabra de origen indígena?", "una palabra que llegó al castellano desde una lengua originaria", "Eso significa origen indígena."),
        ex("Nombra una palabra de origen quechua.", "choclo, palta, papa, guagua, cóndor, puma, llama o pampa", "Todas están en la ficha."),
        ex("¿De qué lengua viene «copihue»?", "del mapuzugun", "La ficha lo dice."),
    ],
    task=T(
        "Lee este texto de práctica inventado: «El sábado fuimos a la pampa con mi abuela. Vimos una llama y un cóndor. Comimos choclo con palta. En casa, la guagua dormía.» Con la ficha de origen, subraya las palabras de origen indígena y escribe una lista con su lengua. Después escribe una pregunta para el educador tradicional sobre alguna de esas palabras.",
        "pampa (quechua), llama (quechua), cóndor (quechua), choclo (quechua), palta (quechua), guagua (quechua). Pregunta: ¿cómo se llaman estos animales en la lengua de su pueblo?",
        ["encuentra las seis palabras", "escribe la lengua con la ficha", "formula una pregunta"],
        ["texto subrayado", "lista con las lenguas"],
        ["no encontrar todas las palabras", "inventar un origen"],
        "Valora que usó la ficha; si inventó un origen, vuelve a la ficha.",
    ),
    reinforce="Di en voz alta tres palabras de origen indígena que usas en tu casa.",
    extend="Pregunta a alguien de tu casa qué palabras de origen indígena usa y anota dos.",
)

L(
    LS3, 2,
    materials="Lápiz y hoja. Las fichas están escritas aquí; son de práctica.",
    use="Aprenderé a ubicar de qué lengua y de qué cultura viene una palabra. Sirve para no mezclar los pueblos y para reconocer a quienes crearon esas palabras.",
    prior=["Sé qué es una palabra de origen indígena.", "Sé usar una ficha de origen."],
    explain=[
        "El quechua es una lengua de los Andes. La hablan pueblos quechua de varios países, y en Chile también vive el pueblo quechua en el norte. El mapuzugun es la lengua del pueblo mapuche. Muchas palabras que usamos vienen de estas lenguas.",
        "Para dar el contexto de una palabra digo tres datos: la palabra, la lengua de donde viene y lo que significa. Por ejemplo: «cóndor» viene del quechua y es un ave grande de los Andes. «Copihue» viene del mapuzugun y es una flor roja del sur.",
        "La fuente de estos datos es una ficha o un diccionario. No mezclo lenguas. No digo que «puma» sea mapuche si la ficha dice que viene del quechua. Si no tengo el dato, escribo una pregunta.",
    ],
    vocab=[("contexto", "datos que ayudan a entender una palabra: lengua, lugar, significado"), ("quechua", "lengua de los Andes"), ("mapuzugun", "lengua del pueblo mapuche"), ("mezclar", "juntar cosas distintas como si fueran iguales"), ("significado", "lo que quiere decir una palabra")],
    worked=[
        W("Dar los tres datos", FICHA_ORI + " Doy los tres datos de «llama».", ["Palabra: llama.", "Lengua: quechua, según la ficha.", "Significado: animal de los Andes."], "llama; quechua; animal de los Andes"),
        W("No mezclar lenguas", "Un niño dice: «Pudú es una palabra quechua». Según la ficha, ¿es cierto?", ["Busco «pudú» en la ficha.", "Dice que viene del mapuzugun.", "El niño mezcló las lenguas."], "No; viene del mapuzugun"),
    ],
    mistakes=[
        M("Decir que todas las palabras de origen indígena vienen del mismo pueblo.", "Cada una viene de una lengua distinta.", "Reviso la lengua de cada palabra en la ficha."),
        M("Dar solo la palabra sin lengua ni significado.", "Falta contexto.", "Doy los tres datos: palabra, lengua y significado."),
    ],
    R=[
        ex(FICHA_ORI + " ¿De qué lengua viene «puma»?", "del quechua", "La ficha lo dice."),
        ex(FICHA_ORI + " ¿Qué es el copihue?", "una flor roja del sur", "La ficha lo dice."),
        ex("¿Cuántos datos doy para el contexto de una palabra?", "3", "Son palabra, lengua y significado."),
    ],
    C=[
        ex(FICHA_ORI + " Verdadero o falso: «cóndor» viene del mapuzugun.", "Falso", "Viene del quechua."),
        ex(FICHA_ORI + " ¿Qué lengua es la del pueblo mapuche: quechua o mapuzugun?", "mapuzugun", "El mapuzugun es la lengua mapuche."),
        ex(FICHA_ORI + " ¿Qué significa «pampa»?", "llanura", "La ficha dice llanura."),
    ],
    A=[
        ex(FICHA_ORI + " Elige los tres datos de «copihue»: A) copihue; mapuzugun; flor roja del sur B) copihue; quechua; ave.", "A", "A coincide con la ficha."),
        ex(FICHA_ORI + " Clasifica: ¿cuántas de estas palabras vienen del mapuzugun: copihue, pudú, llama, choclo?", "2", "Solo «copihue» y «pudú»."),
        ex(FICHA_ORI + " Escribe los datos de «guagua» en orden (palabra, lengua, significado).", "guagua; quechua; bebé", "La ficha dice que significa bebé y viene del quechua."),
    ],
    Z=[
        ex("Julia dice: «Todas las palabras de la ficha vienen del mapuzugun». ¿Tiene razón? Responde Sí o No.", "No", "La mayoría viene del quechua."),
        ex("¿Por qué es importante decir de qué lengua viene una palabra?", "para reconocer a quienes la crearon", "Así no se mezclan los pueblos ni se olvida su aporte."),
    ],
    D=[
        ex(FICHA_ORI + " La ficha tiene 8 palabras del quechua y 2 del mapuzugun. ¿Cuántas palabras tiene en total?", "10", "8 + 2 = 10."),
        ex(FICHA_ORI + " ¿Qué lengua tiene más palabras en la ficha: quechua o mapuzugun?", "quechua", "Tiene 8 y el mapuzugun tiene 2."),
    ],
    context=[ex("Escuchas en la radio una receta que dice: «agrega palta y choclo». Quieres explicarle a tu hermano de dónde vienen las palabras. Según la ficha, ¿qué le dices?", "que vienen del quechua", "La ficha dice que ambas vienen del quechua.")],
    selfcheck=[
        ex("¿Cuáles son los tres datos del contexto de una palabra?", "palabra, lengua y significado", "Esos tres datos forman el contexto."),
        ex("¿De qué lengua viene «pudú»?", "del mapuzugun", "La ficha lo dice."),
        ex("¿Puedo decir que todas las palabras vienen del mismo pueblo?", "No", "Cada una viene de su lengua."),
    ],
    task=T(
        "Haz una tabla de cuatro filas con las palabras «llama», «guagua», «copihue» y «pudú». En tres columnas escribe: palabra, lengua y significado, usando la ficha de origen. Pinta de verde las que vienen del quechua y de azul las del mapuzugun. Al final escribe una pregunta para el educador tradicional sobre alguna palabra.",
        "llama | quechua | animal de los Andes (verde). guagua | quechua | bebé (verde). copihue | mapuzugun | flor roja del sur (azul). pudú | mapuzugun | ciervo muy pequeño (azul). Pregunta: ¿cómo se dice «bebé» en su lengua?",
        ["completa la tabla con la ficha", "colorea según la lengua", "formula una pregunta"],
        ["tabla en el cuaderno", "pregunta escrita"],
        ["mezclar las lenguas", "inventar el significado"],
        "Valora que usó la ficha; si mezcló lenguas, revisa la ficha con él.",
    ),
    reinforce="Elige una palabra de la ficha y di en voz alta sus tres datos.",
    extend="Averigua con un adulto dónde viste o escuchaste hoy una de estas palabras y anótalo.",
)

L(
    LS3, 3,
    materials="Lápiz y hoja. El texto de práctica está escrito aquí; es inventado.",
    use="Aprenderé a comprender un texto corto con palabras de origen indígena y a relacionar cada palabra con lo que nombra. Sirve para entender lo que leo y respetar su origen.",
    prior=["Sé contestar quién, dónde y qué pasa.", "Sé usar la ficha de origen."],
    explain=[
        "Comprender un texto es entender de qué trata, quién actúa, dónde ocurre y qué pasa. Cuando el texto tiene palabras de origen indígena, las relaciono con lo que nombran: choclo con el maíz tierno, palta con la fruta verde, guagua con un bebé, cóndor con el ave de los Andes.",
        "Después me pregunto: ¿cómo ayuda esta palabra a entender el texto? Por ejemplo, si leo «la guagua duerme en su cuna», la palabra guagua me dice quién duerme. Si leo «el cóndor vuela sobre el cerro», me dice qué ave vuela.",
        "Solo digo lo que el texto dice. No agrego significados especiales de una cultura que no estén en el texto o en la ficha. Si me queda una duda, la escribo como pregunta.",
    ],
    vocab=[("comprender", "entender lo que dice un texto"), ("relacionar", "unir una palabra con lo que nombra"), ("trata de", "de qué habla el texto"), ("cuna", "cama pequeña de un bebé"), ("cerro", "elevación del terreno")],
    worked=[
        W("Qué trata el texto", "Texto de práctica (inventado): «Ana ayudó a su mamá a pelar choclos para el almuerzo.» ¿De qué trata?", ["Veo quién actúa: Ana y su mamá.", "Veo qué hacen: pelan choclos.", "Trata de preparar el almuerzo."], "de preparar el almuerzo"),
        W("Relacionar la palabra", "En el texto aparece «choclo». " + FICHA_ORI + " ¿Qué es un choclo?", ["Busco «choclo» en la ficha.", "Dice: maíz tierno.", "Es el maíz tierno."], "el maíz tierno"),
    ],
    mistakes=[
        M("Agregar al texto un significado que no dice.", "Me imaginé algo que no está.", "Solo uso lo que dice el texto y la ficha."),
        M("No relacionar la palabra con su significado.", "Pasé de largo la palabra.", "Busco cada palabra en la ficha."),
    ],
    R=[
        ex("Texto de práctica (inventado): «El cóndor vuela sobre el cerro.» ¿Quién vuela?", "el cóndor", "El texto lo dice."),
        ex("Texto: «La guagua duerme en su cuna.» " + FICHA_ORI + " ¿Quién duerme?", "un bebé", "«Guagua» es bebé."),
        ex(FICHA_ORI + " ¿Qué es un choclo?", "maíz tierno", "La ficha lo dice."),
    ],
    C=[
        ex("Texto de práctica (inventado): «Luis comió palta con pan.» ¿Qué comió con pan?", "palta", "El texto lo dice."),
        ex("Texto: «Un puma caminó por la pampa.» " + FICHA_ORI + " ¿Dónde caminó el puma?", "por la pampa", "El texto lo dice."),
        ex("Verdadero o falso: puedo agregar al texto significados especiales que no están escritos.", "Falso", "Solo digo lo que el texto dice."),
    ],
    A=[
        ex("Texto de práctica (inventado): «Sara vio un pudú entre los copihues y se quedó quieta.» " + FICHA_ORI + " ¿Qué animal vio Sara?", "un pudú", "El texto lo dice."),
        ex("Mismo texto de Sara. ¿Qué hizo Sara después de ver al animal?", "se quedó quieta", "El texto lo dice."),
        ex("Mismo texto de Sara. ¿Qué flores había?", "copihues", "El texto dice «copihues»."),
    ],
    Z=[
        ex("Nico dice que el texto de Sara cuenta una ceremonia secreta. ¿El texto lo dice? Responde Sí o No.", "No", "El texto solo cuenta que Sara vio un pudú."),
        ex("¿Por qué se entiende mejor el texto si sé qué es un copihue?", "porque sé qué flores hay", "Conocer la palabra ayuda a imaginar la escena."),
    ],
    D=[
        ex("Texto: «El mercado vendía 4 cajas de palta y 3 de choclo.» ¿Cuántas cajas hay en total?", "7", "4 + 3 = 7 cajas."),
        ex("Texto de práctica (inventado): «Ayer, Rosa vio una llama en el cerro y dibujó un puma.» ¿Qué animal dibujó Rosa?", "un puma", "El texto dice que dibujó un puma."),
    ],
    context=[ex("Un cartel de la escuela dice: «Hoy almuerzo con choclo». Un compañero de primero no sabe qué es. ¿Qué le explicas?", "que es un maíz tierno", "La ficha lo dice.")],
    selfcheck=[
        ex("¿Qué hago con una palabra de origen indígena que no entiendo?", "la busco en la ficha", "La ficha dice qué es."),
        ex("¿Puedo agregar significados que el texto no dice?", "No", "Solo digo lo que dice el texto."),
        ex("¿Qué es una guagua?", "un bebé", "La ficha lo dice."),
    ],
    task=T(
        "Lee este texto de práctica inventado: «Martina y su abuelo fueron a la pampa. Vieron un cóndor volar sobre el cerro. Después compraron choclo y palta en la feria. Martina le dio las gracias a su abuelo.» Responde en tu cuaderno: ¿quiénes van?, ¿adónde van?, ¿qué ven?, ¿qué compran? y ¿qué palabras de origen indígena aparecen? Dibuja la escena.",
        "Martina y su abuelo. A la pampa. Un cóndor. Choclo y palta. Palabras: pampa, cóndor, choclo y palta. Dibujo: dos personas, un ave en el cielo y comida.",
        ["responde las cinco preguntas con el texto", "encuentra las palabras indígenas", "no agrega hechos"],
        ["respuestas en el cuaderno", "dibujo de la escena"],
        ["inventar hechos", "olvidar una palabra"],
        "Valora la comprensión con el texto; si agregó hechos, invítalo a volver a leerlo.",
    ),
    reinforce="Cuenta con tus palabras de qué trata el texto de Martina.",
    extend="Lee un texto corto de tu casa y busca una palabra que venga de una lengua originaria.",
)

L(
    LS3, 4,
    materials="Lápiz y hoja. Los textos y las respuestas de ejemplo están escritos aquí.",
    use="Aprenderé a responder preguntas sobre un texto usando sus palabras y diciendo de dónde vienen los datos. Sirve para hablar de las culturas originarias sin apropiarme.",
    prior=["Sé comprender un texto corto.", "Sé que debo nombrar la fuente."],
    explain=[
        "Responder con evidencia es contestar usando lo que dice el texto y decir en qué parte lo encontré. Puedo empezar con «El texto dice…» o «Según la ficha…». Así se ve de dónde viene mi respuesta.",
        "Apropiarme sería decir que un conocimiento es mío cuando viene de una cultura. Por ejemplo, decir «yo inventé la palabra guagua». No lo hago. Digo que «guagua» viene del quechua, según la ficha, y que significa bebé.",
        "También cuido cómo hablo de las personas. Hablo de «el pueblo quechua» o «el pueblo mapuche» con respeto, sin generalizar a todos los pueblos. Y si no tengo un dato, pregunto.",
    ],
    vocab=[("evidencia", "parte del texto o ficha que prueba mi respuesta"), ("según", "palabra para decir quién lo dice"), ("generalizar", "decir de todos algo que solo sé de uno"), ("apropiarse", "decir que es mío algo de otros"), ("respuesta", "lo que contesto a una pregunta")],
    worked=[
        W("Responder con evidencia", "Texto de práctica (inventado): «Pedro vio una llama en el cerro.» Pregunta: ¿qué vio Pedro? ¿Cómo respondo?", ["Busco en el texto: una llama.", "Escribo: «El texto dice que Pedro vio una llama».", "Digo dónde: en el cerro."], "El texto dice que Pedro vio una llama en el cerro."),
        W("No apropiarme", "Mi hermano dice: «Yo inventé la palabra choclo». ¿Qué le respondo según la ficha?", ["Busco «choclo» en la ficha.", "Dice que viene del quechua.", "Le digo: «Según la ficha, viene del quechua»."], "Según la ficha, «choclo» viene del quechua."),
    ],
    mistakes=[
        M("Responder sin decir de dónde saqué el dato.", "No se ve si lo pensé o lo leí.", "Empiezo con «El texto dice…» o «Según la ficha…»."),
        M("Decir «los pueblos originarios hacen esto» a partir de un solo ejemplo.", "Estoy generalizando.", "Hablo del pueblo del que habla el texto."),
    ],
    R=[
        ex("¿Con qué dos palabras puedo empezar mi respuesta: «El texto dice» o «Yo adiviné»?", "«El texto dice»", "Muestra de dónde viene el dato."),
        ex("Texto: «Pedro vio una llama en el cerro.» ¿Qué vio Pedro?", "una llama", "El texto lo dice."),
        ex("¿Debo decir que yo inventé una palabra que viene del quechua? Responde Sí o No.", "No", "Eso es apropiarme."),
    ],
    C=[
        ex("Verdadero o falso: puedo generalizar y decir de todos los pueblos lo que sé de uno.", "Falso", "Cada pueblo es distinto."),
        ex("Respuesta A: «Según la ficha, «guagua» viene del quechua.» Respuesta B: «Yo lo sé.» ¿Cuál tiene evidencia?", "A", "A dice de dónde viene el dato."),
        ex("¿Qué significa apropiarse?", "decir que es mío algo de otros", "Es tomar lo que es de otros."),
    ],
    A=[
        ex("Texto de práctica (inventado): «Marta comió choclo en la pampa.» Pregunta: ¿dónde comió Marta? Elige: A) «El texto dice que comió en la pampa.» B) «Creo que en su casa.»", "A", "A usa el texto."),
        ex("Pregunta: ¿qué comió Marta (mismo texto)? Responde empezando con «El texto dice».", "El texto dice que comió choclo.", "Empieza con la evidencia y usa lo que dice el texto."),
        ex("Pregunta: ¿de qué lengua viene «choclo»? Elige: A) «Según la ficha, del quechua.» B) «Del inglés.»", "A", "La ficha lo dice."),
    ],
    Z=[
        ex("Berta dice: «Los pueblos originarios comen choclo todos los días». ¿Qué problema tiene la frase?", "generaliza", "Dice algo de todos sin saberlo."),
        ex("¿Por qué conviene decir «Según la ficha»?", "para mostrar de dónde viene el dato", "Así no mezclo mi idea con la fuente."),
    ],
    D=[
        ex("Tienes 6 preguntas y respondes 2 con «El texto dice». ¿Cuántas te faltan por responder así?", "4", "6 − 2 = 4."),
        ex("Una respuesta dice: «El cóndor es de los mapuche». La ficha dice que «cóndor» viene del quechua. ¿Qué debes corregir?", "que la palabra viene del quechua", "La respuesta mezcló la lengua."),
    ],
    context=[ex("En clase, un compañero dice: «La palabra palta la inventé yo». Quieres corregir con respeto. ¿Qué frase usas: «Según la ficha, viene del quechua» o «Eres mentiroso»?", "«Según la ficha, viene del quechua»", "Corrige con evidencia y sin ofender.")],
    selfcheck=[
        ex("¿Con qué empiezo una respuesta con evidencia?", "con «El texto dice» o «Según la ficha»", "Muestra de dónde viene."),
        ex("¿Puedo decir que yo inventé una palabra de otra cultura?", "No", "Sería apropiarme de algo que viene de otra cultura."),
        ex("En Lengua y Cultura: ¿Qué es generalizar?", "decir de todos algo que solo sé de uno", "Es un error."),
    ],
    task=T(
        "Lee este texto de práctica inventado: «En el cerro, Nico vio un puma y una llama. Su abuela le contó que la palabra puma viene del quechua.» Responde en tu cuaderno tres preguntas, cada una empezando con «El texto dice…»: 1) ¿Qué vio Nico? 2) ¿Dónde? 3) ¿De qué lengua viene la palabra puma? Escribe una frase de agradecimiento a quien te enseñó la ficha de origen.",
        "1) El texto dice que Nico vio un puma y una llama. 2) El texto dice que fue en el cerro. 3) El texto dice que puma viene del quechua. Gracias por enseñarme la ficha.",
        ["responde con «El texto dice»", "usa lo que dice el texto", "agradece a la fuente"],
        ["respuestas escritas", "agradecimiento"],
        ["responder sin evidencia", "generalizar"],
        "Valora que usó el texto; si respondió sin evidencia, practica la frase «El texto dice».",
    ),
    reinforce="Responde en voz alta una pregunta del texto empezando con «El texto dice».",
    extend="Lee un cuento y responde dos preguntas empezando con «El texto dice».",
)

L(
    LS3, 5,
    materials="Lápiz y hoja. Los textos para revisar están escritos aquí; son inventados.",
    use="Aprenderé a revisar un texto sobre culturas originarias para detectar errores y estereotipos. Sirve para que lo que leo y escribo sea verdadero y respetuoso.",
    prior=["Sé responder con evidencia.", "Sé qué es un estereotipo."],
    explain=[
        "Revisar un texto es leerlo de nuevo con tres preguntas. ¿Los datos son verdaderos? ¿Las palabras de origen indígena se usan con su significado? ¿Muestra a los pueblos como son hoy, sin repetir ideas falsas?",
        "Hay errores típicos. Uno es decir que las palabras indígenas son «raras» o «de otro mundo»: son parte de nuestro castellano. Otro es decir que los pueblos originarios «ya no existen». Otro es dar un significado equivocado, como decir que guagua es una comida.",
        "Si encuentro un error, lo marco, lo explico con la ficha y propongo una frase corregida. Si no estoy seguro, anoto una pregunta para el educador o la educadora tradicional.",
    ],
    vocab=[("revisar", "leer de nuevo para encontrar errores"), ("error", "algo que no es verdadero o no está bien"), ("estereotipo", "imagen simple y repetida que muestra a todos iguales"), ("proponer", "decir cómo se puede mejorar"), ("frase corregida", "frase nueva sin el error")],
    worked=[
        W("Encontrar un error", "Texto de práctica (inventado): «La guagua es una comida típica». " + FICHA_ORI + " ¿Qué error tiene?", ["Busco «guagua» en la ficha.", "Dice que es un bebé.", "El texto dice que es una comida: está equivocado."], "guagua es un bebé, no una comida"),
        W("Proponer una corrección", "Texto de práctica (inventado): «Los pueblos originarios ya no existen». ¿Cómo lo corrijo?", ["Pienso: hoy viven personas de pueblos originarios en Chile.", "El texto es falso.", "Escribo: «Hoy hay pueblos originarios en Chile»."], "Hoy hay pueblos originarios en Chile."),
    ],
    mistakes=[
        M("Aceptar un texto porque suena seguro.", "Puede tener errores aunque suene seguro.", "Reviso con las tres preguntas."),
        M("Corregir sin decir por qué.", "El otro no entiende el error.", "Explico con la ficha."),
    ],
    R=[
        ex("¿Cuántas preguntas hago para revisar un texto?", "3", "Son datos verdaderos, significado correcto y trato respetuoso."),
        ex("Texto: «La palta es un animal.» ¿Es verdadero o falso?", "Falso", "Palta es una fruta."),
        ex(FICHA_ORI + " ¿Qué es un cóndor: un ave o un pez?", "un ave", "La ficha dice que es un ave de los Andes."),
    ],
    C=[
        ex("Verdadero o falso: «Las palabras de origen indígena no son parte del castellano.»", "Falso", "Usamos muchas todos los días."),
        ex("Texto de práctica (inventado): «El copihue es un pájaro.» " + FICHA_ORI + " ¿Qué es en realidad?", "una flor roja", "La ficha dice que es una flor roja del sur."),
        ex("Texto: «Los pueblos originarios son solo del pasado.» ¿Es un estereotipo?", "Sí", "Ignora que hoy hay pueblos originarios."),
    ],
    A=[
        ex("Corrige la frase «Guagua es una comida» usando la ficha: elige A) «Guagua es un bebé.» B) «Guagua es un animal.»", "A", "A coincide con la ficha."),
        ex("Texto: «Pudú es un ciervo muy grande.» " + FICHA_ORI + " ¿Qué palabra está mal?", "grande", "La ficha dice que es muy pequeño."),
        ex("Revisaste 5 textos y encontraste errores en 2. ¿Cuántos estaban bien?", "3", "5 − 2 = 3."),
    ],
    Z=[
        ex("Gabi dice: «Si el texto es de un libro, no tiene errores». ¿Está bien? Responde Sí o No.", "No", "Hay que revisar igual con la ficha."),
        ex("¿Por qué es mejor explicar un error con la ficha?", "para que se entienda", "La ficha muestra el dato verdadero."),
    ],
    D=[
        ex("Texto de práctica (inventado): «La llama y el cóndor son palabras de los mapuche.» " + FICHA_ORI + " ¿Qué error tiene?", "viene del quechua, no del mapuzugun", "La ficha dice que ambas vienen del quechua."),
        ex("Un texto tiene 3 errores y corriges 1. ¿Cuántos errores faltan por corregir?", "2", "3 − 1 = 2."),
    ],
    context=[ex("Un afiche de tu escuela dice: «Palta y choclo: comidas raras de otro mundo». ¿Qué dato corrige el afiche: «son comidas comunes y sus nombres vienen del quechua» o «son comidas de otro planeta»?", "«son comidas comunes y sus nombres vienen del quechua»", "Son parte de nuestra comida y de nuestro castellano.")],
    selfcheck=[
        ex("¿Qué hago si no estoy seguro de un dato?", "lo pregunto al educador tradicional", "Preguntar evita errores."),
        ex("¿Qué es una frase corregida?", "frase nueva sin el error", "Es la versión mejorada."),
        ex("¿Cuántas preguntas hago al revisar un texto sobre culturas?", "3", "Son tres preguntas de revisión."),
    ],
    task=T(
        "Revisa estas tres frases de práctica inventadas con la ficha de origen. A) «Guagua es una comida típica.» B) «El copihue es una flor roja del sur.» C) «Los pueblos originarios solo existieron antes.» En tu cuaderno escribe cuáles están bien y cuáles hay que corregir. Para cada una que corrijas, escribe la frase corregida y por qué. Escribe una pregunta para el educador tradicional.",
        "A: corregir: «Guagua es un bebé», según la ficha. B: bien. C: corregir: «Hoy hay pueblos originarios». Pregunta: ¿cómo se dice «bebé» en la lengua de su pueblo?",
        ["identifica B como correcta", "corrige A y C con una razón", "formula una pregunta"],
        ["tabla de revisión", "frases corregidas"],
        ["aceptar errores", "corregir sin razón"],
        "Valora la revisión con las tres preguntas; si aceptó un error, vuelve a la ficha.",
    ),
    reinforce="Busca el error en esta frase y dilo en voz alta: «El pudú es una flor».",
    extend="Escribe una frase verdadera con la palabra «cóndor» y revísala con las tres preguntas.",
)

# =================================================================== LS04 · escritura de palabras con elementos significativos
L(
    LS4, 1,
    materials="Lápiz, goma y hoja con líneas. Las palabras modelo están escritas aquí.",
    use="Aprenderé a escribir con cuidado palabras de origen indígena que usamos en castellano. Sirve para escribirlas bien y reconocer su origen.",
    prior=["Sé separar una palabra en sílabas.", "Sé copiar un modelo letra por letra."],
    explain=[
        "Escribir bien una palabra empieza con mirar el modelo. Las palabras de esta clase son: copihue, pudú, cóndor, choclo, palta, guagua y pampa. Las copio igual que el modelo, con sus tildes.",
        "Puedo ayudarme separando en sílabas, que son los golpes de voz de la palabra. «Co-pi-hue» tiene tres sílabas. «Pu-dú» tiene dos. «Cón-dor» tiene dos. «Cho-clo», «pal-ta», «gua-gua» y «pam-pa» también tienen dos. Contar las sílabas me ayuda a no dejar partes sin escribir.",
        "Algunas llevan tilde, como «pudú» y «cóndor». Otras no, como «choclo» o «palta». La tilde es parte de la palabra: si el modelo la trae, la copio. Si tengo dudas, pregunto a mi profesor o profesora.",
    ],
    vocab=[("sílaba", "golpe de voz en que se divide una palabra"), ("tilde", "rayita que se pone sobre una vocal, como en cóndor"), ("modelo", "palabra bien escrita que copio"), ("copiar", "escribir igual que el modelo"), ("origen", "lengua de donde viene una palabra")],
    worked=[
        W("Contar sílabas", "Modelo: «copihue». ¿Cuántas sílabas tiene?", ["Separo: co-pi-hue.", "Cuento: 1, 2, 3.", "Tiene tres sílabas."], "3"),
        W("Copiar con tilde", "Modelo: «cóndor». ¿Qué debo copiar con cuidado?", ["Miro la primera vocal: ó con tilde.", "La tilde es parte de la palabra.", "Escribo «cóndor» con la tilde."], "la tilde de la ó"),
    ],
    mistakes=[
        M("Copiar «condor» sin tilde.", "No miré la tilde del modelo.", "Toco la tilde con el dedo antes de escribir."),
        M("Dejar una sílaba sin escribir.", "Escribí rápido.", "Cuento las sílabas antes y después."),
    ],
    R=[
        ex("Modelo: «palta». ¿Cuántas sílabas tiene: pal-ta?", "2", "Hay dos golpes de voz."),
        ex("Modelo: «cóndor». ¿Qué letra lleva tilde?", "la ó", "La tilde está sobre la primera o."),
        ex("Modelo: «pampa». ¿Cuál es la primera letra?", "p", "Empieza con p."),
    ],
    C=[
        ex("Modelo: «guagua». Copias: A) guagua B) guaga C) gagua. ¿Cuál es igual al modelo?", "A", "A tiene las letras en el mismo orden."),
        ex("Verdadero o falso: «pudú» lleva tilde en la última u.", "Verdadero", "El modelo trae «pudú» con tilde."),
        ex("Modelo: «copihue». ¿Cuántas letras tiene?", "7", "c, o, p, i, h, u, e son siete letras."),
    ],
    A=[
        ex("Modelo: «choclo». Separa en sílabas y cuenta: ¿cho-clo tiene cuántas?", "2", "Hay dos sílabas."),
        arith("Modelo: «copihue» tiene 3 sílabas y «pudú» tiene 2. ¿Cuántas sílabas hay entre las dos palabras?", "3+2", "Se suman las sílabas de cada palabra."),
        ex("Modelo: «guagua». ¿Cuántas veces aparece la letra g?", "2", "g-u-a-g-u-a: hay una g al comienzo de cada sílaba."),
    ],
    Z=[
        ex("Pedro copió «condor» y dijo: «Da igual». ¿Qué le dices: «Copia lo que dice el modelo» o «Tienes razón»?", "«Copia lo que dice el modelo»", "La tilde es parte de la palabra."),
        ex("¿Por qué ayuda contar las sílabas al escribir?", "para no dejar partes sin escribir", "Revisa que estén todas las partes."),
    ],
    D=[
        ex("Escribes «copihue», «pudú» y «cóndor» una vez cada una. ¿Cuántas sílabas escribes en total?", "7", "3 + 2 + 2 = 7."),
        ex("De «choclo», «palta» y «cóndor», ¿cuál lleva tilde?", "cóndor", "Solo «cóndor» tiene tilde."),
    ],
    context=[ex("Tu curso escribe un cartel que dice «Visita al pudú». ¿Qué palabra del cartel lleva tilde?", "pudú", "La última letra lleva tilde.")],
    selfcheck=[
        ex("¿Qué miro antes de copiar una palabra?", "el modelo", "Copio igual que el modelo."),
        ex("¿Cuántas sílabas tiene «copihue»?", "3", "Se separa así: co-pi-hue."),
        ex("¿La tilde es parte de la palabra?", "Sí", "Si el modelo la trae, la copio."),
    ],
    task=T(
        "Elige tres palabras de esta lista: copihue, pudú, cóndor, choclo, palta, guagua, pampa. Cópialas dos veces cada una en tu cuaderno. Al lado de cada palabra escribe cuántas sílabas tiene y encierra en un círculo la tilde si la tiene. Revisa letra por letra con el modelo.",
        "copihue: co-pi-hue (3). pudú: pu-dú (2, con tilde). cóndor: cón-dor (2, con tilde). Revisé letra por letra.",
        ["copia las tres palabras sin errores", "cuenta las sílabas", "marca la tilde si corresponde"],
        ["cuaderno con las palabras", "tabla de sílabas"],
        ["omitir tildes", "contar mal las sílabas"],
        "Valora que revisó letra por letra; si omitió una tilde, muéstrale el modelo.",
    ),
    reinforce="Copia «cóndor» cuatro veces despacio y revisa la tilde.",
    extend="Escribe una frase con «choclo» y otra con «palta»; cuenta las sílabas de esas palabras.",
)

L(
    LS4, 2,
    materials="Lápiz y hoja. Las tarjetas de origen están escritas aquí.",
    use="Aprenderé a escribir una palabra junto con su origen y la fuente que me lo dice. Sirve para que otras personas sepan de dónde viene lo que escribo.",
    prior=["Sé copiar una palabra con su tilde.", "Sé usar la ficha de origen."],
    explain=[
        "Cuando escribo una palabra de origen indígena, puedo agregar una nota de origen. La nota dice de qué lengua viene y qué significa. Por ejemplo: «copihue (del mapuzugun): flor roja del sur». Eso me ayuda a recordar y a respetar su origen.",
        "La nota tiene cuatro partes: la palabra, el paréntesis con la lengua, dos puntos y el significado. Primero escribo la palabra igual al modelo. Luego pongo la lengua entre paréntesis. Después el significado.",
        "La información de la nota la saco de una ficha o de un diccionario, y lo digo: «Fuente: ficha de origen». Si no tengo el dato, no lo invento. Dejo la nota incompleta y pregunto.",
    ],
    vocab=[("nota de origen", "frase breve que dice de qué lengua viene una palabra"), ("paréntesis", "signos ( ) que encierran un dato"), ("significado", "lo que quiere decir una palabra"), ("fuente", "ficha o diccionario de donde saqué el dato"), ("incompleta", "a la que le falta una parte")],
    worked=[
        W("Escribir una nota", FICHA_ORI + " Escribo la nota de «cóndor».", ["Escribo la palabra: cóndor.", "Agrego la lengua entre paréntesis: (del quechua).", "Agrego el significado: ave grande de los Andes."], "cóndor (del quechua): ave grande de los Andes"),
        W("Nota incompleta", "Quiero hacer la nota de una palabra que no está en la ficha. ¿Qué hago?", ["Veo que no tengo el dato de la lengua.", "No lo invento.", "Dejo la nota incompleta y escribo una pregunta."], "dejo la nota incompleta y pregunto"),
    ],
    mistakes=[
        M("Poner la lengua equivocada en la nota.", "No revisé la ficha.", "Reviso la ficha antes de escribir la lengua."),
        M("Olvidar la fuente.", "Pensé que no era necesaria.", "Agrego «Fuente: ficha de origen»."),
    ],
    R=[
        ex(FICHA_ORI + " ¿De qué lengua viene «palta»?", "del quechua", "La ficha lo dice."),
        ex(FICHA_ORI + " ¿Qué significa «pampa»?", "llanura", "La ficha lo dice."),
        ex("En la nota de origen, ¿entre qué signos va la lengua: paréntesis o comillas?", "paréntesis", "La lengua va entre paréntesis."),
    ],
    C=[
        ex("Nota: «pudú (del mapuzugun): ciervo muy pequeño». ¿Cuántas partes tiene la nota: palabra, lengua y significado?", "3", "Son tres partes."),
        ex(FICHA_ORI + " Verdadero o falso: «copihue (del quechua)» es una nota correcta.", "Falso", "La ficha dice que viene del mapuzugun."),
        ex("Si no tengo el dato en la ficha, ¿lo invento o pregunto?", "pregunto", "No invento datos."),
    ],
    A=[
        ex(FICHA_ORI + " Escribe la nota de «llama». Elige: A) llama (del quechua): animal de los Andes. B) llama (del mapuzugun): animal de los Andes.", "A", "La ficha dice que viene del quechua."),
        ex(FICHA_ORI + " Elige la nota correcta de «choclo»: A) choclo (del quechua): maíz tierno. B) choclo: ave.", "A", "A tiene lengua y significado correctos."),
        ex(FICHA_ORI + " ¿Qué parte falta en «guagua: bebé»?", "la lengua entre paréntesis", "Debe decir (del quechua)."),
    ],
    Z=[
        ex("Raúl dice: «No importa poner la lengua, con la palabra basta». ¿Qué ganas al poner la lengua?", "se sabe de dónde viene la palabra", "Reconoce su origen."),
        ex("¿Por qué agrego «Fuente: ficha de origen»?", "para que se sepa de dónde saqué el dato", "Muestra la fuente."),
    ],
    D=[
        ex("Haces notas de origen de 4 palabras. Cada una tiene 3 partes. ¿Cuántas partes escribes?", "12", "4 × 3 = 12 partes."),
        ex(FICHA_ORI + " ¿Cuántas notas de origen puedes escribir con la ficha si usas solo las palabras del mapuzugun?", "2", "Son «copihue» y «pudú»."),
    ],
    context=[ex("Tu curso hace un diccionario ilustrado. Para «cóndor» ponen una nota de origen. ¿Qué lengua escribes entre paréntesis?", "del quechua", "La ficha dice que «cóndor» viene del quechua.")],
    selfcheck=[
        ex("¿Qué partes tiene una nota de origen?", "palabra, lengua y significado", "Son las tres."),
        ex("¿De dónde saco los datos de la nota?", "de la ficha o un diccionario", "Son las fuentes."),
        ex("Si no tengo un dato, ¿qué hago?", "pregunto", "No invento datos que no tengo."),
    ],
    task=T(
        "Usa la ficha de origen para escribir notas de origen de tres palabras: copihue, llama y guagua. Cada nota debe tener palabra, lengua entre paréntesis y significado. Escribe también «Fuente: ficha de origen». Dibuja una pequeña ilustración para cada una.",
        "copihue (del mapuzugun): flor roja del sur. llama (del quechua): animal de los Andes. guagua (del quechua): bebé. Fuente: ficha de origen.",
        ["escribe las tres notas con las tres partes", "usa la lengua que dice la ficha", "anota la fuente"],
        ["notas en el cuaderno", "ilustraciones"],
        ["poner la lengua equivocada", "olvidar la fuente"],
        "Valora que las notas están completas; si puso una lengua equivocada, revisa la ficha con él.",
    ),
    reinforce="Escribe la nota de origen de «pampa» y léela en voz alta.",
    extend="Haz una nota de origen para una palabra que aprendas en esta semana, con ayuda de un adulto.",
)

L(
    LS4, 3,
    materials="Lápiz y hoja. Las frases modelo están escritas aquí.",
    use="Aprenderé a escribir frases que usan palabras de origen indígena con su significado verdadero. Sirve para expresar ideas claras que muestran lo que significa cada palabra.",
    prior=["Sé escribir una oración con mayúscula y punto.", "Sé el significado de las palabras de la ficha."],
    explain=[
        "Una frase con una palabra de origen indígena debe mostrar su significado. Si escribo «El pudú es un ciervo muy pequeño», muestro qué es un pudú. Si escribo «El pudú es una flor», estoy equivocado.",
        "Para escribir una buena frase, uso la ficha de origen. Luego pienso en una idea que sea verdadera y la escribo con mayúscula al inicio y punto al final. Puedo usar el modelo: «El/La ____ es ____».",
        "También puedo hacer frases con acciones: «La guagua duerme». «El cóndor vuela». Reviso que la acción tenga sentido para esa palabra. Si no estoy seguro, pregunto o elijo otra palabra.",
    ],
    vocab=[("frase", "grupo de palabras que dice una idea"), ("verdadera", "que coincide con la realidad"), ("acción", "lo que hace alguien o algo"), ("sentido", "que se entiende bien"), ("modelo de frase", "frase que sirve para escribir otras iguales")],
    worked=[
        W("Completar una frase", FICHA_ORI + " Completa: «El pudú es un ____ muy pequeño».", ["Busco «pudú» en la ficha.", "Es un ciervo.", "Escribo: «El pudú es un ciervo muy pequeño»."], "ciervo"),
        W("Revisar la acción", "Frase: «El copihue corre por el bosque». ¿Tiene sentido?", ["Pienso: ¿una flor corre?", "No: las flores no corren.", "La frase no tiene sentido; la cambio por «El copihue crece en el bosque»."], "No tiene sentido; se corrige con «crece»"),
    ],
    mistakes=[
        M("Escribir una frase con un significado equivocado.", "No revisé la ficha.", "Compruebo el significado antes de escribir."),
        M("Olvidar la mayúscula y el punto.", "Pensé solo en la palabra especial.", "Reviso al final."),
    ],
    R=[
        ex(FICHA_ORI + " ¿Qué es el copihue?", "una flor roja del sur", "La ficha lo dice."),
        ex(FICHA_ORI + " ¿Qué es la guagua?", "un bebé", "La ficha lo dice."),
        ex("¿Con qué signo termina mi frase: punto o coma?", "punto", "La oración termina con punto."),
    ],
    C=[
        ex("Frase: «El cóndor vuela sobre el cerro.» ¿Tiene sentido?", "Sí", "Un cóndor es un ave que vuela."),
        ex("Frase: «La palta ladra.» ¿Tiene sentido?", "No", "Una fruta no ladra."),
        ex(FICHA_ORI + " Frase: «El pudú es un ciervo muy pequeño.» ¿Coincide con la ficha?", "Sí", "La ficha dice que es un ciervo muy pequeño."),
    ],
    A=[
        ex(FICHA_ORI + " Completa con una palabra de la ficha: «El ____ es el maíz tierno».", "choclo", "La ficha dice que el choclo es maíz tierno."),
        ex(FICHA_ORI + " Completa: «La ____ duerme en su cuna».", "guagua", "Guagua es un bebé."),
        ex(FICHA_ORI + " Escribe una frase verdadera con «pampa». Elige: A) «La pampa es una llanura.» B) «La pampa es un pájaro.»", "A", "A coincide con la ficha."),
    ],
    Z=[
        ex("Lola escribió: «El cóndor es una fruta». ¿Qué debe cambiar?", "fruta por ave", "El cóndor es un ave grande de los Andes."),
        ex("¿Por qué es importante que mi frase sea verdadera?", "para mostrar el significado real", "Así respeto la palabra."),
    ],
    D=[
        ex("Escribes 3 frases verdaderas y 2 con errores. ¿Cuántas frases escribiste en total?", "5", "3 + 2 = 5."),
        ex(FICHA_ORI + " Elige la frase correcta: A) «El pudú es un pez.» B) «El pudú es un ciervo muy pequeño.»", "B", "La ficha dice que es un ciervo."),
    ],
    context=[ex("Estás haciendo un cartel que dice «El ____ es un ave grande de los Andes». ¿Qué palabra de la ficha completa la frase?", "cóndor", "La ficha dice que el cóndor es un ave grande de los Andes.")],
    selfcheck=[
        ex("¿Qué debe mostrar mi frase con una palabra de origen indígena?", "su significado", "La frase debe mostrar su significado verdadero."),
        ex("¿Con qué empiezo y termino mi frase?", "mayúscula y punto", "Empieza con letra grande y termina con punto."),
        ex("¿Qué hago si no estoy seguro del significado?", "reviso la ficha", "La ficha tiene el dato."),
    ],
    task=T(
        "Escribe cuatro frases verdaderas con cuatro palabras distintas de la ficha de origen (por ejemplo: copihue, pudú, cóndor, choclo, palta, guagua, llama, pampa). Cada frase debe mostrar el significado de la palabra. Revisa que tengan mayúscula y punto. Dibuja una de las frases.",
        "El copihue es una flor roja del sur. El cóndor vuela sobre el cerro. El choclo es maíz tierno. La guagua duerme en su cuna.",
        ["escribe cuatro frases con cuatro palabras", "los significados son verdaderos", "mayúscula y punto"],
        ["frases escritas", "dibujo de una frase"],
        ["significados equivocados", "olvidar punto o mayúscula"],
        "Valora que las frases sean verdaderas; si hay errores, pide que revise la ficha.",
    ),
    reinforce="Escribe una frase con «llama» y léela en voz alta.",
    extend="Escribe una frase con dos palabras de origen indígena que sea verdadera.",
)

L(
    LS4, 4,
    materials="Lápiz, hoja y colores. El modelo de tarjeta de palabra está escrito aquí.",
    use="Aprenderé a hacer una tarjeta de palabra con su origen, mi dibujo y la fuente, sin quedarme con algo que no es mío. Sirve para compartir lo que aprendí con respeto.",
    prior=["Sé escribir una nota de origen.", "Sé que debo agradecer a la fuente."],
    explain=[
        "Una tarjeta de palabra tiene cuatro partes: la palabra bien escrita, su origen, mi dibujo y la fuente. Es una forma de mostrar lo que aprendí sin decir que es mío. Por ejemplo: palabra «copihue», origen «del mapuzugun», dibujo de una flor roja y fuente «ficha de origen».",
        "Cuando comparto mi tarjeta, digo: «Esto lo aprendí de la ficha de origen». No uso la palabra como si fuera una marca ni la cambio. Tampoco copio dibujos o fotos de otras personas sin permiso: hago mi propio dibujo.",
        "Al final agradezco a quien me enseñó. Puedo decir «gracias» a mi profesora o al educador tradicional. Una tarjeta bien hecha muestra respeto por la palabra y por la cultura de la que viene.",
    ],
    vocab=[("tarjeta de palabra", "papel con una palabra, su origen, un dibujo y la fuente"), ("marca", "nombre que usa una empresa para vender algo"), ("compartir", "mostrar mi trabajo a otros"), ("permiso", "una respuesta de sí de quien corresponde"), ("agradecer", "decir gracias a quien me ayudó")],
    worked=[
        W("Armar una tarjeta", FICHA_ORI + " Armo la tarjeta de «pudú».", ["Palabra: pudú.", "Origen: del mapuzugun.", "Dibujo: un ciervo pequeño. Fuente: ficha de origen."], "pudú; del mapuzugun; dibujo de un ciervo pequeño; ficha de origen"),
        W("Dibujo propio", "Quiero poner en mi tarjeta una foto de un cóndor que vi en internet. ¿Qué hago?", ["No sé de quién es la foto.", "Mejor hago mi propio dibujo.", "Así no copio algo sin permiso."], "hago mi propio dibujo"),
    ],
    mistakes=[
        M("Copiar el dibujo de otra persona sin permiso.", "El dibujo es de su autor.", "Hago mi propio dibujo."),
        M("Usar la palabra como nombre de un producto o un juego.", "Convierte una palabra cultural en una marca.", "La uso solo para aprender y explicar."),
    ],
    R=[
        ex("¿Cuántas partes tiene la tarjeta de palabra?", "4", "Son palabra, origen, dibujo y fuente."),
        ex("¿Quién hace el dibujo de mi tarjeta: yo o alguien que no conozco?", "yo", "Hago mi propio dibujo."),
        ex("¿Qué digo al final a quien me enseñó: gracias o nada?", "gracias", "Agradezco a quien me enseñó."),
    ],
    C=[
        ex("Verdadero o falso: puedo usar una palabra cultural como nombre de un producto para vender.", "Falso", "Eso convierte la palabra en una marca."),
        ex(FICHA_ORI + " Tarjeta: «cóndor; del quechua; dibujo; ficha de origen». ¿Qué parte es la fuente?", "ficha de origen", "La fuente es de dónde saqué el dato."),
        ex("¿Qué es mejor para el dibujo: uno propio o una foto de internet sin permiso?", "uno propio", "Así no copio algo ajeno."),
    ],
    A=[
        ex(FICHA_ORI + " Arma la tarjeta de «llama» en orden: palabra, origen, dibujo, fuente. ¿Qué origen pones?", "del quechua", "La ficha lo dice."),
        ex("Tarjeta incompleta: «copihue; del mapuzugun; dibujo». ¿Qué parte falta?", "la fuente", "Faltan los datos de dónde saqué el dato."),
        ex("Quieres compartir tu tarjeta con tu curso. ¿Qué dices primero: «Esto lo aprendí de la ficha de origen» o «Esto lo inventé yo»?", "«Esto lo aprendí de la ficha de origen»", "Reconoce la fuente."),
    ],
    Z=[
        ex("Alonso dice: «Si hago una tarjeta bonita, ya no necesito la fuente». ¿Tiene razón? Responde Sí o No.", "No", "La fuente muestra de dónde viene el dato."),
        ex("¿Por qué agradezco a quien me enseñó la palabra?", "porque compartió su saber", "Es una forma de respeto."),
    ],
    D=[
        ex("Haces 4 tarjetas y cada una tiene 4 partes. ¿Cuántas partes haces en total?", "16", "4 × 4 = 16."),
        ex("Tienes 5 tarjetas y regalas 2 a tu curso. ¿Cuántas te quedan?", "3", "5 − 2 = 3."),
    ],
    context=[ex("Tu curso hará una exposición de tarjetas de palabras en el pasillo. Una niña quiere pegar la foto de un niño como dibujo. ¿Qué le sugieres: hacer su propio dibujo o pegar la foto sin preguntar?", "hacer su propio dibujo", "La foto de una persona se cuida y se pide permiso.")],
    selfcheck=[
        ex("¿Cuáles son las cuatro partes de la tarjeta?", "palabra, origen, dibujo y fuente", "Son las cuatro."),
        ex("¿Puedo copiar un dibujo ajeno sin permiso?", "No", "Hago mi propio dibujo."),
        ex("¿Qué hago al terminar?", "agradezco", "Digo gracias a quien me enseñó."),
    ],
    task=T(
        "Haz una tarjeta de palabra para «copihue» o para «cóndor» (elige una). Debe llevar: la palabra bien escrita (con tilde si corresponde), su origen según la ficha de origen, tu propio dibujo y la fuente. Escribe al final una frase de agradecimiento. Cuida que tu tarjeta no use la palabra como marca ni lleve fotos de personas.",
        "Palabra: copihue. Origen: del mapuzugun. Dibujo: flor roja. Fuente: ficha de origen. Gracias por enseñarme la ficha.",
        ["tarjeta con las cuatro partes", "dibujo propio", "frase de agradecimiento"],
        ["tarjeta terminada", "frase de agradecimiento"],
        ["copiar dibujos ajenos", "usar la palabra como marca"],
        "Valora la tarjeta completa y respetuosa; si copió un dibujo, invítalo a hacer el suyo.",
    ),
    reinforce="Revisa tu tarjeta con la lista de las cuatro partes.",
    extend="Haz una segunda tarjeta con otra palabra y comparte las dos con tu familia, diciendo la fuente.",
)

# =================================================================== LS05 · recursos tecnológicos para conocer aspectos de la cultura
L(
    LS5, 1,
    materials="Lápiz y hoja. Las fichas de recursos están escritas aquí; son inventadas para practicar. Si usas un aparato, siempre con un adulto.",
    use="Aprenderé qué recursos tecnológicos me permiten escuchar y ver aspectos de una cultura y cuál elegir. Sirve para aprender con cuidado.",
    prior=["Sé qué es un audio y un video.", "Sé usar la tecnología con un adulto."],
    explain=[
        "Un recurso tecnológico es un aparato o programa que me ayuda a conocer algo. Para escuchar música, un relato o una entrevista uso audios o la radio. Para ver una danza, un tejido o un paisaje uso fotos o videos. Los museos también tienen recursos para ver desde un computador.",
        "Antes de elegir, me pregunto qué quiero conocer. Si quiero escuchar cómo suena una música, elijo un audio. Si quiero ver cómo se hace un tejido, elijo un video. Si quiero ver un objeto de cerca, elijo una foto.",
        "Siempre lo uso con un adulto. No pongo mi nombre ni mi dirección en ninguna página. Y elijo recursos hechos o autorizados por la comunidad, la escuela o una institución conocida.",
    ],
    vocab=[("recurso", "algo que me ayuda a conocer o hacer una cosa"), ("audio", "sonido grabado"), ("video", "imágenes en movimiento con sonido"), ("foto", "imagen fija"), ("institución", "grupo organizado, como una escuela o un museo")],
    worked=[
        W("Elegir para ver", "Quiero ver cómo se hace un tejido. ¿Qué recurso elijo: audio o video?", ["Quiero ver un proceso.", "Un audio no tiene imagen.", "Elijo un video."], "un video"),
        W("Elegir para escuchar", "Quiero escuchar cómo suena una entrevista. ¿Qué recurso elijo: audio o foto?", ["Quiero escuchar.", "Una foto no suena.", "Elijo un audio."], "un audio"),
    ],
    mistakes=[
        M("Elegir un recurso sin saber para qué lo quiero.", "No pensé qué quería conocer.", "Primero me pregunto qué quiero conocer."),
        M("Poner mi nombre en una página.", "Esos datos son privados.", "No escribo datos personales."),
    ],
    R=[
        ex("Para escuchar una entrevista, ¿elijo un audio o una foto?", "un audio", "El audio tiene sonido."),
        ex("Para ver un objeto de cerca, ¿elijo una foto o una radio?", "una foto", "La foto muestra la imagen."),
        ex("Para ver cómo se hace algo, ¿elijo un video o un audio?", "un video", "El video muestra el proceso."),
    ],
    C=[
        ex("Verdadero o falso: puedo usar internet solo, sin avisar a un adulto.", "Falso", "Debo usarlo con un adulto."),
        ex("¿Qué pregunta me hago antes de elegir un recurso: «¿qué quiero conocer?» o «¿cuál es más grande?»", "«¿qué quiero conocer?»", "Esa pregunta define qué recurso me sirve."),
        ex("¿Qué dato no debo escribir en una página: mi nombre completo o la palabra «copihue»?", "mi nombre completo", "Los datos personales son privados."),
    ],
    A=[
        ex("Une la necesidad con el recurso: 1) escuchar una canción de la escuela 2) ver una danza 3) ver un tejido de cerca. Recursos: audio, video, foto. Escribe la lista.", "audio, video, foto", "Cada recurso sirve para esa necesidad."),
        ex("Ficha de recurso (inventada): «Video de una escuela; con permiso de las familias; dura 4 minutos». ¿Cuántos minutos dura?", "4", "La ficha dice 4 minutos."),
        ex("Ficha (inventada): «Audio de una radio de la escuela». ¿Es un recurso para escuchar o para ver?", "para escuchar", "El audio se escucha."),
    ],
    Z=[
        ex("Camila dice: «Cualquier video sirve, aunque no sepa quién lo hizo». ¿Tiene razón? Responde Sí o No.", "No", "Es importante saber quién lo hizo."),
        ex("¿Por qué conviene elegir recursos de una institución conocida?", "porque tienen autoría y permisos", "Se sabe quién los hizo."),
    ],
    D=[
        ex("Tienes 3 audios, 2 videos y 4 fotos autorizados. ¿Cuántos recursos tienes?", "9", "3 + 2 + 4 = 9."),
        ex("Viste 2 de los 5 videos autorizados. ¿Cuántos faltan?", "3", "5 − 2 = 3."),
    ],
    context=[ex("Tu profesora te ofrece ver un video de la escuela con la educadora tradicional enseñando a tejer. ¿Es un recurso para ver o para escuchar?", "para ver (y escuchar)", "Un video tiene imagen y sonido.")],
    selfcheck=[
        ex("¿Qué recurso uso para escuchar?", "un audio", "El audio es sonido."),
        ex("¿Con quién uso la tecnología?", "con un adulto", "Siempre uso la tecnología acompañado."),
        ex("¿Qué dato personal no pongo en una página?", "mi nombre completo", "Es un dato privado."),
    ],
    task=T(
        "En tu cuaderno haz una tabla con tres filas. Fila 1: quiero escuchar una entrevista (recurso: audio). Fila 2: quiero ver una danza (recurso: video). Fila 3: quiero ver un objeto de cerca (recurso: foto). Dibuja un aparato en cada fila y escribe una regla para usarlos con cuidado.",
        "Escuchar entrevista: audio. Ver danza: video. Ver objeto: foto. Regla: los uso con un adulto y sin datos personales.",
        ["une cada necesidad con un recurso", "dibuja un aparato", "escribe una regla de cuidado"],
        ["tabla en el cuaderno", "dibujos"],
        ["usar la tecnología sin un adulto", "poner datos personales"],
        "Valora la tabla y la regla; si olvidó al adulto, recuérdalo con una pregunta.",
    ),
    reinforce="Nombra tres recursos tecnológicos y di para qué sirve cada uno.",
    extend="Cuenta a alguien de tu casa qué recursos usarías para conocer un baile de otra cultura.",
)

L(
    LS5, 2,
    materials="Lápiz y hoja. Las fichas de recursos están escritas aquí y son inventadas para practicar.",
    use="Aprenderé a revisar quién hizo un recurso, de qué cultura habla y si tiene permiso. Sirve para usar solo recursos respetuosos.",
    prior=["Sé elegir un recurso para escuchar o ver.", "Sé que una fuente debe ser confiable."],
    explain=[
        "Antes de ver o escuchar un recurso, reviso cuatro datos: quién lo hizo (la autoría), de qué cultura habla, para qué se hizo y si tiene permiso para compartirse. Estos datos están en la ficha del recurso, que suele estar al comienzo o al final.",
        "La autoría es importante porque el recurso tiene dueño. Puede ser una persona, una escuela, una comunidad o una institución. Si el recurso muestra a una comunidad, esa comunidad debe haber dado permiso.",
        "Si la ficha no dice quién lo hizo, mejor pregunto a un adulto antes de usarlo. Un recurso sin autoría puede tener errores o no tener permiso. Prefiero uno con ficha completa.",
    ],
    vocab=[("autoría", "quién hizo el recurso"), ("permiso", "autorización para compartir algo"), ("ficha del recurso", "datos que dicen quién lo hizo y para qué"), ("completa", "que tiene todos los datos"), ("institución", "grupo organizado, como una escuela o un museo")],
    worked=[
        W("Leer la ficha", "Ficha del recurso (inventada): «Video: Tejer en la escuela. Autoría: educadora tradicional de la escuela. Pueblo: aymara. Permiso: sí». ¿Quién hizo el video?", ["Busco «Autoría».", "Dice: educadora tradicional de la escuela.", "Ella lo hizo."], "la educadora tradicional de la escuela"),
        W("Ficha incompleta", "Ficha (inventada): «Audio: Canto antiguo. Autoría: ?. Pueblo: ?. Permiso: ?». ¿Lo uso?", ["Veo que faltan tres datos.", "No sé quién lo hizo ni si tiene permiso.", "Pregunto a un adulto antes de usarlo."], "no lo uso hasta preguntar"),
    ],
    mistakes=[
        M("Usar un recurso sin leer su ficha.", "No sé quién lo hizo.", "Siempre leo la ficha."),
        M("Pensar que todo lo que está en internet se puede usar.", "Muchos recursos tienen dueño.", "Reviso el permiso."),
    ],
    R=[
        ex("Ficha: «Autoría: una escuela». ¿Quién hizo el recurso?", "una escuela", "La ficha lo dice."),
        ex("¿Cuántos datos reviso en la ficha de un recurso?", "4", "Son autoría, cultura, para qué se hizo y permiso."),
        ex("Si la ficha dice «Permiso: sí», ¿puedo usar el recurso?", "Sí, para lo que dice la ficha", "El permiso lo autoriza."),
    ],
    C=[
        ex("Verdadero o falso: un recurso sin autoría es igual de bueno que uno con ficha completa.", "Falso", "Hay más riesgo de errores."),
        ex("Ficha: «Pueblo: mapuche». ¿Qué dato me da: el pueblo o el permiso?", "el pueblo", "La ficha dice de qué cultura habla."),
        ex("Ficha: «Permiso: ?». ¿Qué hago: uso el recurso o pregunto?", "pregunto", "Primero compruebo el permiso."),
    ],
    A=[
        ex("Fichas inventadas: A) «Autoría: museo; Permiso: sí» B) «Autoría: ?; Permiso: ?». ¿Cuál elijo?", "A", "A tiene los datos completos."),
        ex("Una ficha trae autoría, pueblo, para qué se hizo y permiso. ¿Cuántos datos tiene?", "4", "Los datos son autoría, pueblo, propósito y permiso."),
        ex("Ficha: «Autoría: escuela; Pueblo: ?; Permiso: sí». ¿Qué dato falta?", "el pueblo", "El pueblo tiene signo de pregunta."),
    ],
    Z=[
        ex("Pablo dice: «Si lo vi en una página, es seguro». ¿Qué le falta saber?", "quién lo hizo y si tiene permiso", "Esos datos están en la ficha."),
        ex("¿Por qué es importante el permiso de una comunidad?", "porque ella decide qué comparte", "Respeta su saber."),
    ],
    D=[
        ex("Revisas 8 fichas y 3 están incompletas. ¿Cuántas están completas?", "5", "8 − 3 = 5."),
        ex("Tienes 4 datos por ficha y revisas 3 fichas. ¿Cuántos datos revisas?", "12", "4 × 3 = 12."),
    ],
    context=[ex("Tu profesora quiere mostrar un audio de la escuela. La ficha dice «Autoría: curso de 3.° básico; Permiso: sí». ¿Puede mostrarlo?", "Sí", "La ficha dice que hay permiso.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es la autoría?", "quién hizo el recurso", "Es el dueño."),
        ex("¿Qué hago si la ficha no tiene permiso?", "pregunto a un adulto", "No lo uso sin permiso."),
        ex("¿Cuántos datos reviso de un recurso antes de usarlo?", "4", "Los datos son autoría, pueblo, propósito y permiso."),
    ],
    task=T(
        "Revisa estas dos fichas de práctica inventadas. A) «Video: Una danza de la escuela. Autoría: el curso. Pueblo: aymara. Permiso: sí.» B) «Audio: Un canto. Autoría: ?. Pueblo: ?. Permiso: ?.» En tu cuaderno escribe cuál usarías y por qué, y qué dato faltaría en la otra. Después escribe una pregunta para el educador tradicional.",
        "Uso A porque tiene autoría, pueblo y permiso. A B le faltan autoría, pueblo y permiso. Pregunta: ¿cómo se pide permiso para usar un canto?",
        ["elige la ficha completa", "nombra los datos que faltan", "formula una pregunta"],
        ["respuestas en el cuaderno", "pregunta escrita"],
        ["usar el recurso sin ficha", "inventar datos"],
        "Valora la revisión de la ficha; si eligió el recurso sin datos, vuelve a los cuatro datos.",
    ),
    reinforce="Di en voz alta los cuatro datos que reviso antes de usar un recurso.",
    extend="Pregunta a un adulto cómo reconoce si un video o audio tiene permiso.",
)

L(
    LS5, 3,
    materials="Lápiz y hoja. La descripción del video de práctica y la ficha de notas están escritas aquí.",
    use="Aprenderé a ver o escuchar un recurso y anotar lo que observo sin cambiarlo. Sirve para comprender un aspecto de la cultura con atención.",
    prior=["Sé revisar la ficha de un recurso.", "Sé describir con los sentidos."],
    explain=[
        "Cuando veo o escucho un recurso, tomo notas. Una nota es una anotación breve de lo que vi o escuché. Anoto qué vi, qué oí y qué me gustaría preguntar. No anoto cosas que no vi.",
        "Mi ficha de notas tiene tres partes: «Vi», «Oí» y «Pregunto». En «Vi» escribo cosas que veo, como personas, objetos, colores. En «Oí» escribo sonidos, palabras o música. En «Pregunto» escribo dudas para el educador o la educadora tradicional.",
        "No tomo capturas ni grabo a personas sin permiso. Y no saco conclusiones grandes de un video pequeño. Si veo una danza, digo «en este video vi…», no «todos los pueblos hacen esto».",
    ],
    vocab=[("nota", "anotación breve"), ("capturar", "sacar una foto de la pantalla"), ("conclusión", "idea final que saco de lo que observo"), ("duda", "algo que no entendí y quiero preguntar"), ("danza", "baile")],
    worked=[
        W("Tomar notas", "Video de práctica (descrito): «Se ve a una persona tejiendo en un telar; se oye agua de un río». ¿Qué anoto en «Vi»?", ["Busco lo que se ve.", "Se ve una persona tejiendo en un telar.", "Escribo eso."], "una persona tejiendo en un telar"),
        W("Anotar una duda", "En el mismo video, no entiendo para qué sirve un hilo largo. ¿Dónde lo anoto?", ["Es una duda.", "Va en «Pregunto».", "Escribo: ¿para qué sirve el hilo largo?"], "en «Pregunto»"),
    ],
    mistakes=[
        M("Anotar lo que me imagino y no lo que vi.", "Quise completar la historia.", "Anoto solo lo que veo y oigo."),
        M("Sacar capturas de personas sin permiso.", "Las imágenes de personas se cuidan.", "Tomo notas con palabras y dibujos."),
    ],
    R=[
        ex("Video de práctica (descrito): «Se ve a una persona tejiendo». ¿Qué hace la persona?", "teje", "El texto lo dice."),
        ex("En mi ficha de notas, ¿qué va en «Oí»: sonidos o dibujos?", "sonidos", "«Oí» es para lo que escucho."),
        ex("¿Dónde anoto una duda: en «Vi» o en «Pregunto»?", "en «Pregunto»", "Las dudas van en «Pregunto»."),
    ],
    C=[
        ex("Verdadero o falso: puedo sacar capturas de la cara de una persona del video sin permiso.", "Falso", "Se cuida la imagen de las personas."),
        ex("Video: «Se oye música de flauta y tambor». ¿Eso va en «Vi» o en «Oí»?", "en «Oí»", "La música es un sonido que se escucha."),
        ex("Si un video muestra una danza, ¿puedo decir que todos los pueblos bailan igual?", "No", "Un video no muestra a todos los pueblos."),
    ],
    A=[
        ex("Video de práctica (descrito): «Hay lana de colores, un telar y se oye una voz». Clasifica: ¿cuántos elementos van en «Vi»?", "2", "La lana de colores y el telar."),
        ex("Mismo video. ¿Qué elemento va en «Oí»?", "una voz", "Es un sonido."),
        ex("Mismo video. Escribe una pregunta para «Pregunto»: elige A) «¿Cómo se eligen los colores de la lana?» B) «¿Por qué no me dejan verlo?»", "A", "A es una duda sobre lo visto."),
    ],
    Z=[
        ex("Marcos dice: «Vi un baile, así que todos bailan igual». ¿Qué error tiene?", "generaliza", "Un video no representa a todos."),
        ex("¿Por qué es mejor anotar «en este video vi…»?", "porque solo hablo de lo que vi", "Así evito generalizar a otros pueblos."),
    ],
    D=[
        ex("Anotaste 3 cosas en «Vi», 2 en «Oí» y 1 en «Pregunto». ¿Cuántas notas hiciste?", "6", "3 + 2 + 1 = 6."),
        ex("Tienes 6 notas y 2 son dudas. ¿Cuántas no son dudas?", "4", "6 − 2 = 4."),
    ],
    context=[ex("Tu curso ve un video corto de la escuela donde la educadora tradicional muestra un telar. Un compañero anota «la educadora es famosa en todo Chile». ¿Eso lo vio en el video?", "No", "No lo mostró el video.")],
    selfcheck=[
        ex("¿Cuáles son las tres partes de mi ficha de notas?", "Vi, Oí y Pregunto", "Esas son las tres partes de la ficha."),
        ex("¿Qué no hago con personas del video?", "capturas sin permiso", "Cuido su imagen."),
        ex("¿Qué frase uso para no generalizar?", "en este video vi", "Hablo solo del video."),
    ],
    task=T(
        "Lee esta descripción de un video de práctica inventado: «Se ve a una persona hilando lana con un huso. Hay lana de dos colores sobre una mesa. Se oye música suave de flauta». Completa en tu cuaderno una ficha de notas con las tres partes: Vi, Oí y Pregunto. Dibuja una escena. Escribe una pregunta para el educador tradicional.",
        "Vi: una persona hilando con un huso; lana de dos colores. Oí: música de flauta. Pregunto: ¿cómo se hila la lana? Dibujo: persona con huso.",
        ["completa Vi, Oí y Pregunto", "anota solo lo que se describe", "formula una pregunta"],
        ["ficha de notas", "dibujo"],
        ["anotar cosas que no están", "generalizar"],
        "Valora que solo anotó lo del video; si agregó cosas, vuelve a la descripción.",
    ),
    reinforce="Haz una ficha de notas de algo que veas hoy, con Vi, Oí y Pregunto.",
    extend="Cuenta a alguien de tu casa cómo tomas notas de un video sin sacar capturas de personas.",
)

L(
    LS5, 4,
    materials="Lápiz, hoja y colores. Los modelos de agradecimiento y las situaciones están escritos aquí.",
    use="Aprenderé a compartir lo que aprendí de un recurso sin apropiarme, diciendo la autoría y pidiendo permiso. Sirve para respetar a quienes hicieron el recurso y a la cultura de la que habla.",
    prior=["Sé revisar la ficha de un recurso.", "Sé tomar notas de lo que veo y oigo."],
    explain=[
        "Compartir es mostrar a otros lo que aprendí. Puedo contar con mis palabras, hacer un dibujo o exponer mis notas. Siempre digo de qué recurso lo aprendí y quién lo hizo. Eso se llama citar la autoría.",
        "No me apropio cuando no digo que el recurso es mío, no lo corto ni lo cambio, no le saco partes para hacer bromas y no lo publico sin permiso. Si quiero mostrar un recurso en otro lugar, pido permiso a quien lo hizo o a mi profesor o profesora.",
        "Al final agradezco. Puedo escribir: «Gracias a la autora o al autor del video por compartirlo». Una buena forma de compartir cuida a la cultura, a las personas del video y a quien lo creó.",
    ],
    vocab=[("citar", "decir de dónde viene lo que aprendí"), ("autoría", "quién hizo el recurso"), ("publicar", "mostrar algo a mucha gente"), ("apropiarse", "decir que es mío algo que es de otros"), ("exponer", "mostrar y explicar mi trabajo")],
    worked=[
        W("Citar la autoría", "Aprendí de un video de la escuela hecho por el curso de 3.° básico. ¿Cómo lo cito?", ["Digo qué recurso: un video de la escuela.", "Digo quién lo hizo: el curso de 3.° básico.", "Lo escribo: «Aprendí de un video del curso de 3.° básico»."], "Aprendí de un video del curso de 3.° básico."),
        W("Pedir permiso", "Quiero mostrar el video en otro curso. ¿Qué hago primero?", ["Pienso: el video tiene autoría.", "Debo pedir permiso a quien lo hizo o a mi profesora.", "Pregunto antes de mostrarlo."], "pedir permiso"),
    ],
    mistakes=[
        M("Decir que el video lo hice yo.", "Me apropié de un trabajo ajeno.", "Digo quién lo hizo."),
        M("Publicar un video de la escuela sin permiso.", "No sé si se puede compartir.", "Pido permiso antes."),
    ],
    R=[
        ex("¿Cómo se llama decir de dónde viene lo que aprendí: citar o esconder?", "citar", "Citar es decir la fuente."),
        ex("Si un video lo hizo mi curso, ¿quién tiene la autoría: mi curso o yo solo?", "mi curso", "El curso lo hizo."),
        ex("¿Debo agradecer al autor de un recurso: Sí o No?", "Sí", "Es una forma de respeto."),
    ],
    C=[
        ex("Verdadero o falso: puedo cortar un video y hacer una broma con él.", "Falso", "Eso no respeta a las personas ni a la cultura."),
        ex("¿Qué debo pedir antes de mostrar un recurso en otro lugar: permiso o aplausos?", "permiso", "Se pide permiso."),
        ex("Frase A: «Aprendí de un video de la escuela.» Frase B: «Yo hice este video.» ¿Cuál cita la fuente?", "A", "A dice de dónde lo aprendí."),
    ],
    A=[
        ex("Eliges la mejor forma de compartir: A) «Lo vi en un video del museo y aprendí esto.» B) «Esto lo sé yo.»", "A", "A cita la fuente."),
        ex("Quieres agradecer. Elige: A) «Gracias por compartir el video.» B) «No me sirvió.»", "A", "A agradece con respeto."),
        ex("Quieres mostrar el video de la escuela a otro curso. ¿Qué hago primero: pido permiso o lo muestro?", "pido permiso", "Primero el permiso."),
    ],
    Z=[
        ex("Ale dice: «Voy a subir el video a todas las redes para que todos lo vean». ¿Qué le falta? ", "permiso de quien lo hizo", "Hay que preguntar antes de publicar."),
        ex("¿Por qué cito la autoría?", "para reconocer a quien lo hizo", "Es una forma de respeto."),
    ],
    D=[
        ex("Mostrarás 3 recursos y de cada uno dirás 2 datos de autoría. ¿Cuántos datos dirás?", "6", "3 × 2 = 6."),
        ex("Tienes 5 recursos y pides permiso para 3. ¿Para cuántos te falta pedir permiso?", "2", "5 − 3 = 2."),
    ],
    context=[ex("Tu curso hará una exposición con lo que aprendió de un video del museo regional. ¿Qué escriben en un cartel: «Video del museo regional» o «Video nuestro»?", "«Video del museo regional»", "Cita la fuente.")],
    selfcheck=[
        ex("¿Qué es citar?", "decir de dónde viene lo que aprendí", "Es decir la fuente."),
        ex("¿Qué pido antes de publicar un recurso?", "permiso", "Se pide permiso."),
        ex("¿Qué digo al final de compartir?", "gracias", "Se agradece a quien compartió."),
    ],
    task=T(
        "Prepara una exposición de un minuto sobre un recurso de práctica: «Video de la escuela: una educadora tradicional enseña a hilar lana; autoría: el curso de 3.° básico; permiso: sí». En tu cuaderno escribe tres frases: 1) qué aprendiste, 2) la autoría del recurso y 3) un agradecimiento. Dibuja una escena. Practica en voz alta.",
        "Aprendí que la lana se hila con un huso. Lo vi en un video del curso de 3.° básico. Gracias por compartirlo. Dibujo: persona con huso.",
        ["escribe las tres frases", "cita la autoría", "agradece"],
        ["frases en el cuaderno", "exposición oral"],
        ["decir que el recurso es suyo", "olvidar el agradecimiento"],
        "Valora que citó la autoría y agradeció; si no, practica la frase de cita.",
    ),
    reinforce="Practica en voz alta: «Lo aprendí de… Gracias por compartirlo».",
    extend="Explica a alguien de tu casa por qué es importante citar la autoría de un video.",
)
