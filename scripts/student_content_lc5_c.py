"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR05 (reconocer los usos de la lengua indígena en espacios sociales o comunitarios, valorando su importancia para la
identidad del pueblo y su aporte a la revitalización de la lengua).

Criterio de autoría: todas las fichas, comunidades, escuelas y personas son inventadas solo para practicar y están
rotuladas como tales. Las únicas palabras en lengua indígena son saludos y palabras muy atestiguadas (mari mari,
chaltumay) y el nombre de las lenguas (mapuzugun, aymara, rapa nui). No se inventa gramática, pronunciación ni
significados rituales. No se afirma nada sobre cuántas personas hablan una lengua. La pertenencia a un pueblo nunca se
mide por cuánto se habla la lengua. Cada tarea abierta remite al educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LR5 = "LC05 OA LR05"

CONSULT = " Recuerda: cómo se usa, se escribe y se dice la lengua en tu comunidad lo enseñan el educador o la educadora tradicional y las personas de tu comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. Nunca evaluar la identidad ni el origen de un estudiante."


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


# ============================================================ LR05 clase 1 · situar pueblo, territorio y fuente
FA = "Ficha A (inventada para practicar): Pueblo: mapuche. Territorio: Comunidad Ejemplo, en el sur de Chile. Fuente: la educadora tradicional de la Escuela Ejemplo, que conversó con el curso en abril. Autorización: ella permite contar lo que dijo, pero solo para esta clase. Uso de la lengua que cuenta: se saluda con «mari mari» al empezar el taller."
FB = "Ficha B (inventada): Pueblo: no se indica. Territorio: no se indica. Fuente: «me contaron». Uso de la lengua: se usa en reuniones."
FC = "Ficha C (inventada): Pueblo: aymara. Territorio: Comunidad Muestra. Fuente: un taller con un educador tradicional. Uso de la lengua: el taller comienza con un saludo y luego se conversa."

L(
    LR5, 1,
    materials="Lápiz y hoja. Las fichas están escritas aquí y son inventadas para practicar. No necesitas ningún dispositivo ni materiales especiales.",
    use="Aprenderé a ubicar, antes de hablar de los usos de una lengua indígena, de qué pueblo y territorio hablo, cuál es mi fuente y quién autoriza. Sirve para no mezclar a un pueblo con otro ni contar como cierto lo que no sé.",
    prior=["Sé que en Chile hay varios pueblos indígenas y que cada uno tiene su historia.", "Sé que lo que se aprende de una cultura se cuenta con respeto y citando a quien lo enseñó."],
    explain=[
        "Una lengua indígena se usa en espacios sociales o comunitarios: la casa, la escuela, una reunión, una radio. Para contar esos usos, primero los ubico. Pregunto: ¿de qué pueblo hablo?, ¿en qué territorio, es decir, en qué lugar vive esa comunidad?, ¿quién me lo contó o dónde lo leí? y ¿esa persona autoriza que lo cuente?",
        "Cada pueblo tiene su propia lengua. Por ejemplo, la lengua del pueblo mapuche es el mapuzugun, la del pueblo aymara es el aymara y la del pueblo rapa nui es el rapa nui. Por eso no puedo decir que lo que ocurre en una comunidad ocurre igual en todas. Eso se llama generalizar, y es un error frecuente cuando hablamos de pueblos distintos.",
        "La fuente es la persona, la institución o el documento de donde viene la información. Una fuente buena dice quién habla, desde dónde y con qué permiso. Si un dato no tiene fuente, o no sé de qué pueblo es, lo anoto como «por preguntar» y me detengo. Así cuido a las personas que me enseñan.",
    ],
    vocab=[("territorio", "el lugar donde vive y se desarrolla una comunidad"), ("fuente", "persona o documento de donde viene un dato"), ("autorización", "el permiso para contar o usar algo"), ("generalizar", "decir que lo de uno es igual para todos"), ("uso comunitario", "forma en que la comunidad usa la lengua en espacios compartidos")],
    worked=[
        W("Leer una ficha completa", FA + " ¿De qué pueblo habla la ficha y cuál es su fuente?", ["Busco la línea «Pueblo»: dice mapuche.", "Busco la línea «Fuente»: la educadora tradicional de la Escuela Ejemplo.", "Uno los dos datos en una frase."], "Habla del pueblo mapuche y la fuente es la educadora tradicional de la Escuela Ejemplo"),
        W("Detectar una ficha incompleta", FB + " ¿Se puede contar el uso con esta ficha?", ["Reviso pueblo, territorio y fuente.", "Los tres datos faltan o no están claros: «me contaron» no dice quién.", "Me detengo y pregunto antes de contar."], "No: faltan el pueblo, el territorio y una fuente clara"),
    ],
    mistakes=[
        M("Escribir «todos los pueblos saludan igual» porque una ficha lo dice de uno.", "Una ficha describe una comunidad, no a todas.", "Escribo «en la Comunidad Ejemplo se saluda así», con su pueblo y territorio."),
        M("Contar un uso de la lengua sin decir quién me lo contó.", "Sin fuente nadie puede comprobar ni preguntar.", "Anoto la fuente y si autoriza antes de contar."),
    ],
    R=[
        ex(FA + " ¿Qué pueblo menciona la ficha A?", "mapuche", "La línea «Pueblo» lo dice."),
        ex(FA + " ¿Quién es la fuente de la ficha A?", "la educadora tradicional de la Escuela Ejemplo", "La línea «Fuente» nombra a la educadora."),
        ex("Un territorio, ¿es el lugar donde vive y se desarrolla una comunidad o el nombre de un libro?", "el lugar donde vive y se desarrolla una comunidad", "Así se definió territorio en esta clase."),
    ],
    C=[
        ex(FA + " Verdadero o falso: la ficha A permite contar lo que dijo la educadora en cualquier lugar y siempre.", "Falso", "La ficha dice que el permiso es solo para esta clase."),
        ex("Une cada pueblo con su lengua: A) mapuche, B) aymara, C) rapa nui. Lenguas: 1) aymara, 2) mapuzugun, 3) rapa nui. Escribe los tres pares.", "A-2, B-1, C-3", "La lengua mapuche es el mapuzugun, la aymara es el aymara y la rapa nui es el rapa nui."),
        ex("Una niña dice: «La radio de mi comunidad usa la lengua, así que todos los pueblos usan la lengua en la radio». ¿Esa frase generaliza? Sí o No.", "Sí", "Pasa de una comunidad a todos los pueblos."),
    ],
    A=[
        ex(FA + " La ficha A tiene cinco datos: pueblo, territorio, fuente, autorización y uso. Si se borra el dato de autorización, ¿cuántos datos quedan?", "4", "Cinco datos menos uno.", "5-1"),
        ex(FB + " De estos tres datos, ¿cuáles faltan o no están claros: pueblo, territorio, fuente?", "los tres", "La ficha B no indica pueblo ni territorio, y «me contaron» no es una fuente."),
        ex("Ordena para ubicar un uso de la lengua: A) escribo el uso que cuenta la fuente. B) pregunto de qué pueblo y territorio es. C) anoto quién es la fuente y si autoriza. Escribe las letras en orden.", "B, C, A", "Primero ubico pueblo y territorio, luego la fuente y al final escribo el uso."),
    ],
    Z=[
        ex("Un estudiante escribe sobre la ficha A: «Todos los mapuche saludan así en todas partes». ¿Qué sabemos con seguridad: solo lo de la Comunidad Ejemplo o lo de todos los mapuche?", "solo lo de la Comunidad Ejemplo", "La ficha describe una sola comunidad."),
        ex("A un niño se le olvidó quién le contó un uso de la lengua. ¿Qué es mejor: A) contarlo igual o B) preguntar otra vez por la fuente antes de contarlo?", "B", "Sin fuente no se puede comprobar ni pedir permiso."),
    ],
    D=[
        ex(FA + " " + FC + " ¿La ficha A y la ficha C se contradicen? Sí o No.", "No", "Describen comunidades de pueblos distintos y cada una vale para la suya."),
        arith("Un curso de 30 estudiantes entregó fichas de cinco datos. 18 fichas están completas. ¿Cuántas fichas están incompletas?", "30-18", "Se restan las completas del total."),
    ],
    context=[ex("Quieres contar cómo se usa una lengua indígena en tu localidad. Antes de escribir, ¿qué haces primero: anotar pueblo, territorio y fuente o escribir lo que crees saber?", "anotar pueblo, territorio y fuente", "Primero se ubica y se cita la fuente.")],
    selfcheck=[
        ex("¿Qué dato me dice de dónde viene la información: el territorio o la fuente?", "la fuente", "La fuente es de donde viene el dato."),
        ex("Si no sé de qué pueblo es un dato, ¿lo cuento igual o lo anoto como «por preguntar»?", "lo anoto como «por preguntar»", "Un dato sin pueblo se pregunta antes."),
        ex("¿Se puede decir que todos los pueblos usan la lengua del mismo modo? Sí o No.", "No", "Cada comunidad tiene sus propios usos."),
    ],
    task=T(
        "Lee esta ficha inventada: «Pueblo: aymara. Territorio: Comunidad Muestra. Fuente: un educador tradicional que visitó el curso. Autorización: puede contarse en la sala. Uso: el taller comienza con un saludo.» En tu cuaderno escribe dos frases que cuenten este uso sin generalizar y nombrando la fuente. Después escribe una pregunta que le harías al educador o educadora tradicional de tu escuela sobre cómo se usa la lengua en tu comunidad.",
        "Según un educador tradicional que visitó el curso, en la Comunidad Muestra, del pueblo aymara, el taller comienza con un saludo. Esto describe a esa comunidad y no a todas. Pregunta: ¿en qué momentos se usa la lengua en nuestra comunidad?",
        ["nombra la fuente", "indica pueblo y territorio", "no generaliza a otros pueblos", "formula una pregunta para el educador/a tradicional"],
        ["dos frases escritas en el cuaderno", "pregunta escrita o dicha en voz alta"],
        ["decir «todos los aymara»", "no nombrar la fuente"],
        "Si el estudiante generalizó, pídele que agregue «en la Comunidad Muestra» y «según…». Aprecia las preguntas honestas.",
    ),
    reinforce="Vuelve a leer la ficha A y subraya con lápiz el pueblo, el territorio y la fuente.",
    extend="Inventa una ficha con los cinco datos sobre un espacio de tu escuela donde podría usarse una lengua indígena, y márcala como inventada.",
)

# ============================================================ LR05 clase 2 · escuchar o leer con límites declarados
TEX = "Texto de práctica (inventado): Una vecina de la Comunidad Ejemplo cuenta que, cuando era niña, la lengua se hablaba sobre todo en la casa. Hoy también se oye en el taller de la escuela y en un programa de la radio comunitaria los sábados por la mañana. Ella cree que los niños aprenden mejor si escuchan a las personas mayores. Aclara que habla solo por su comunidad y que no sabe cómo es en otros lugares."

L(
    LR5, 2,
    materials="Lápiz y hoja. El texto está escrito aquí y es inventado para practicar. Puede leerlo una persona adulta en voz alta.",
    use="Aprenderé a escuchar o leer lo que dice una persona sobre los usos de su lengua y a separar lo que ella afirma, lo que yo pienso y los límites que ella declara. Sirve para entender sin cambiar lo que dijo.",
    prior=["Sé ubicar pueblo, territorio y fuente.", "Sé que no se puede generalizar de una comunidad a todas."],
    explain=[
        "Cuando escucho o leo a una persona hablar de cómo usa su lengua, hago tres cosas. Primero anoto lo que dice, tal como lo dijo. Segundo, anoto aparte lo que yo interpreto o pienso. Tercero, busco los límites que ella declara: dónde, cuándo y hasta qué punto vale lo que cuenta.",
        "Un hecho que cuenta la fuente es, por ejemplo, «hay un taller en la escuela». Una opinión de la fuente es «creo que los niños aprenden mejor con los mayores»: se cita como opinión suya, con la palabra «cree». Una interpretación mía sería «entonces la lengua ya está salvada». Eso no lo dijo ella y no debo atribuírselo.",
        "Un límite declarado es una frase como «hablo solo por mi comunidad». Me avisa que no puedo usar su relato para otros lugares. Al contar lo que escuché empiezo con «Según…» y dejo claro qué es de ella y qué es mío. Si no entiendo una palabra, pregunto al educador o educadora tradicional en vez de adivinar.",
    ],
    vocab=[("hecho que cuenta la fuente", "algo que la persona afirma que ocurre"), ("opinión", "lo que alguien cree o piensa"), ("interpretación", "lo que yo concluyo, aunque la fuente no lo dijo"), ("límite declarado", "aviso de hasta dónde vale lo que se cuenta"), ("atribuir", "decir quién dijo algo")],
    worked=[
        W("Separar hecho y opinión", TEX + " ¿«Hay un programa de radio los sábados» es hecho o es opinión?", ["Busco la frase en el texto: se oye en un programa de radio los sábados.", "La vecina la cuenta como algo que ocurre.", "No dice «cree» ni «piensa»."], "es un hecho que cuenta la fuente"),
        W("Encontrar el límite", TEX + " ¿Qué límite declara la vecina?", ["Busco una frase que avise hasta dónde vale su relato.", "Dice que habla solo por su comunidad y no sabe cómo es en otros lugares.", "Ese es el límite."], "habla solo por su comunidad y no sabe cómo es en otros lugares"),
    ],
    mistakes=[
        M("Escribir «la vecina dice que la lengua ya está salvada».", "Ella no dijo eso: es mi interpretación.", "Escribo solo lo que dijo y marco mi idea aparte como mía."),
        M("Usar su relato para contar cómo se usa la lengua en otra región.", "Ella declaró que no sabe cómo es en otros lugares.", "Respeto el límite: lo cuento solo para su comunidad."),
    ],
    R=[
        ex(TEX + " ¿Dónde se hablaba la lengua sobre todo cuando ella era niña?", "en la casa", "El texto lo dice al comienzo."),
        ex(TEX + " ¿Qué día se transmite el programa de la radio comunitaria?", "los sábados", "El texto dice los sábados por la mañana."),
        ex(TEX + " ¿La vecina es la fuente o la lectora del texto?", "la fuente", "Ella es quien cuenta."),
    ],
    C=[
        ex(TEX + " ¿«Los niños aprenden mejor si escuchan a los mayores» es un hecho o una opinión de la vecina?", "una opinión de la vecina", "El texto dice que ella lo cree."),
        ex(TEX + " Un compañero resume: «La radio es el lugar más importante de toda la región». ¿Lo dijo la fuente o es interpretación del compañero?", "es interpretación del compañero", "El texto no dice eso."),
        ex("¿Una frase como «hablo solo por mi comunidad» es un límite declarado o un hecho sobre la radio?", "un límite declarado", "Avisa hasta dónde vale su relato."),
    ],
    A=[
        ex(TEX + " Cuenta los lugares distintos donde se usa la lengua, antes y hoy, según el texto. ¿Cuántos son?", "3", "Uno de antes y dos de hoy: 1 + 2.", "1+2"),
        ex(TEX + " Clasifica cada frase como H (hecho que cuenta la fuente) o I (interpretación mía): 1) hay un taller en la escuela. 2) por eso la lengua está salvada. 3) hay un programa los sábados. Escribe las tres letras.", "1 H, 2 I, 3 H", "La frase 2 no está en el texto."),
        ex("Una persona anotó 7 afirmaciones sobre lo que escuchó. 5 las dijo la fuente. El resto son ideas del que escuchó. ¿Cuántas son ideas del que escuchó?", "2", "Siete menos cinco.", "7-5"),
    ],
    Z=[
        ex(TEX + " Un niño quiere escribir «En Chile entero se usa la lengua solo en la casa». ¿Respeta el límite de la vecina? Sí o No.", "No", "Ella habla solo por su comunidad."),
        ex("Escuchas una palabra de la lengua que no entiendes. ¿Qué es mejor: A) adivinar qué significa o B) preguntar al educador o educadora tradicional?", "B", "Adivinar puede cambiar el sentido sin que nadie lo note."),
    ],
    D=[
        ex(TEX + " Elige el mejor resumen: A) «Según una vecina de la Comunidad Ejemplo, hoy la lengua se oye en la escuela y en la radio; ella habla solo por su comunidad». B) «La lengua se oye en todas las escuelas y radios». C) «La vecina cree que la lengua ya no se habla». Escribe la letra.", "A", "Es la única que atribuye a la fuente y mantiene el límite."),
        ex("Ordena lo que haces al escuchar: A) declaro el límite. B) anoto lo que dice la fuente. C) anoto aparte lo que yo pienso. Escribe las letras en orden.", "B, C, A", "Primero lo dicho, luego lo mío y al final el límite."),
    ],
    context=[ex("Una persona mayor de tu localidad te cuenta cómo usa su lengua. Al escribirlo, ¿empiezas con «Según…» o lo escribes como si lo supieras tú?", "con «Según…»", "Así se atribuye lo dicho a su fuente.")],
    selfcheck=[
        ex("Lo que yo concluyo aunque la fuente no lo dijo, ¿es un hecho de la fuente o una interpretación?", "una interpretación", "La fuente no lo afirmó."),
        ex("Si la fuente dice «hablo solo por mi comunidad», ¿puedo usar su relato para otra región? Sí o No.", "No", "Ese es su límite declarado."),
        ex("¿Qué palabra uso para citar a quien lo dijo: «según» o «seguro»?", "según", "Según atribuye lo dicho a una fuente."),
    ],
    task=T(
        "Lee este texto inventado: «Un joven de la Comunidad Muestra cuenta que en su casa se usa la lengua para saludar y que en la sede comunitaria se hace una reunión una vez al mes. Cree que más jóvenes participarían si hubiera juegos. Dice que no sabe cómo es en otras comunidades.» En tu cuaderno haz tres listas cortas: lo que dijo como hecho, lo que opina él y el límite que declara. Luego escribe una frase que empiece con «Según…» y respete ese límite.",
        "Hechos: en su casa se saluda con la lengua; hay una reunión mensual en la sede. Opinión: más jóvenes participarían con juegos. Límite: no sabe cómo es en otras comunidades. Frase: Según un joven de la Comunidad Muestra, en su casa se usa la lengua para saludar; él no sabe cómo es en otras comunidades.",
        ["separa hechos y opinión", "nombra el límite declarado", "usa «según»", "no agrega ideas que la fuente no dijo"],
        ["tres listas escritas", "frase con «Según…»"],
        ["mezclar su opinión con los hechos", "borrar el límite"],
        "Pide que subraye en el texto cada dato que usó; lo que no esté subrayado es suyo y debe marcarse como tal.",
    ),
    reinforce="Relee el texto de la vecina y subraya con dos colores lo que ella afirma y lo que ella cree.",
    extend="Inventa tres frases sobre un uso de la lengua: un hecho, una opinión y un límite. Pídele a una persona de tu casa que adivine cuál es cuál.",
)

# ============================================================ LR05 clase 3 · relaciones culturales: uso, identidad, revitalización
ESP = "Ficha de espacios (inventada para practicar), Comunidad Ejemplo. Espacio 1, la casa: personas mayores conversan con sus nietas y nietos en la lengua. Espacio 2, la escuela: un taller con la educadora tradicional. Espacio 3, la radio: un programa semanal que también se escucha en casas lejanas del territorio. Espacio 4, la sede comunitaria: cada reunión comienza con un saludo en la lengua. Espacio 5, la entrada de la sede: un letrero que dice «Bienvenidos» en castellano y en la lengua."

L(
    LR5, 3,
    materials="Lápiz y hoja. La ficha está escrita aquí y es inventada para practicar. No necesitas dispositivos.",
    use="Aprenderé a relacionar los usos de una lengua indígena con la identidad del pueblo y con la revitalización de esa lengua. Sirve para explicar por qué importa usarla en muchos espacios y no solo en uno.",
    prior=["Sé ubicar pueblo, territorio y fuente.", "Sé separar lo que dice la fuente de lo que pienso yo."],
    explain=[
        "La identidad de un pueblo es aquello que sus personas reconocen como propio: su historia, su territorio, sus formas de vivir y también su lengua. Cuando la lengua se usa en espacios de la comunidad, ayuda a que las personas sientan que pertenecen a algo compartido. Pero nadie deja de pertenecer a su pueblo por hablar poco o nada su lengua. La pertenencia no se mide por cuánto se habla.",
        "La revitalización es el conjunto de acciones para que una lengua se use otra vez en más lugares y por más personas. Una lengua se revitaliza cuando hay espacios donde se escucha, se practica y se enseña: la casa, la escuela, la radio, las reuniones. Cada espacio aporta algo distinto. La escuela da práctica guiada, la radio llega lejos y el letrero hace visible la lengua.",
        "También cuenta la reciprocidad: dar y recibir con cuidado. Quien aprende de una persona o de una comunidad devuelve algo, como agradecer, cuidar lo aprendido y no usarlo sin permiso. Al relacionar usos, identidad y revitalización siempre digo de qué comunidad hablo, porque cada una vive este proceso a su manera.",
    ],
    vocab=[("identidad", "lo que un pueblo reconoce como propio"), ("revitalización", "acciones para que una lengua se use en más lugares y por más personas"), ("reciprocidad", "dar y recibir con cuidado y respeto"), ("pertenecer", "ser parte de un pueblo o una comunidad"), ("espacio comunitario", "lugar que la comunidad comparte")],
    worked=[
        W("Relacionar un espacio con su aporte", ESP + " ¿Qué aporta el espacio 3, la radio?", ["Leo el espacio 3 en la ficha.", "El programa se escucha también en casas lejanas del territorio.", "Entonces la lengua llega a personas que no están en la reunión."], "la lengua llega a personas que viven lejos"),
        W("Responder sobre identidad", "Un niño dice: «Hablo muy poco la lengua de mi pueblo, entonces no soy parte de él». ¿Es correcto?", ["Recuerdo que la identidad incluye historia, territorio y formas de vivir.", "La pertenencia no se mide por cuánto se habla la lengua.", "Concluyo que no es correcto."], "no es correcto: la pertenencia no depende de cuánto se habla la lengua"),
    ],
    mistakes=[
        M("Pensar que quien no habla la lengua no pertenece a su pueblo.", "La identidad tiene muchos elementos, no solo la lengua.", "Digo que la lengua es un elemento importante y que la pertenencia no se mide por hablarla."),
        M("Creer que un solo espacio, como la escuela, basta para revitalizar una lengua.", "Cada espacio aporta algo distinto.", "Nombro varios espacios y lo que aporta cada uno."),
    ],
    R=[
        ex(ESP + " ¿En qué espacio conversan las personas mayores con sus nietas y nietos en la lengua?", "la casa", "Es el espacio 1."),
        ex(ESP + " ¿Qué espacio tiene un taller con la educadora tradicional?", "la escuela", "Es el espacio 2."),
        ex("Revitalizar una lengua, ¿es lograr que se use otra vez en más lugares y por más personas o dejarla guardada sin usar?", "lograr que se use otra vez en más lugares y por más personas", "Así se definió en la clase."),
    ],
    C=[
        ex(ESP + " ¿Qué espacio hace visible la lengua con un letrero?", "la entrada de la sede", "Es el espacio 5."),
        ex(ESP + " Verdadero o falso: según la ficha, la radio se escucha solo dentro de la sede.", "Falso", "La ficha dice que también se escucha en casas lejanas."),
        ex("Verdadero o falso: quien habla poco su lengua no pertenece a su pueblo.", "Falso", "La pertenencia no se mide por cuánto se habla."),
    ],
    A=[
        ex(ESP + " Une cada espacio con su aporte: A) la escuela, B) la radio, C) el letrero. Aportes: 1) llega lejos, 2) hace visible la lengua, 3) da práctica guiada. Escribe los tres pares.", "A-3, B-1, C-2", "El taller guía la práctica, la radio llega lejos y el letrero hace visible."),
        ex(ESP + " La ficha tiene 5 espacios. La casa y la escuela son 2 de ellos. ¿Cuántos son los otros espacios de la ficha?", "3", "Cinco menos dos.", "5-2"),
        ex("En una comunidad inventada una persona dice: «Me enseñaron un saludo y quiero devolver algo». ¿Qué acción muestra reciprocidad: A) agradecer a quien enseñó y cuidar lo aprendido, o B) usar el saludo en un video sin pedir permiso?", "A", "Reciprocidad es devolver con respeto."),
    ],
    Z=[
        ex(ESP + " Si solo existiera el espacio 2, la escuela, ¿habría tantas ocasiones de escuchar la lengua como con los cinco espacios? Sí o No.", "No", "Cada espacio aporta ocasiones distintas."),
        ex("Una niña dice: «Si las personas mayores usan la lengua en la casa, eso ayuda a la revitalización». ¿Estás de acuerdo con ella según lo que enseña esta clase? Sí o No.", "Sí", "La casa es un espacio donde se escucha y se practica."),
    ],
    D=[
        ex("Dos estudiantes discuten. Ana dice «la lengua es parte de la identidad». Bruno dice «sin hablar la lengua no se es parte del pueblo». ¿Quién se equivoca?", "Bruno", "La lengua es parte de la identidad, pero la pertenencia no se mide por hablarla."),
        ex(ESP + " Ordena de menor a mayor alcance geográfico estos tres espacios: A) la casa, B) la radio, C) la sede comunitaria. Piensa en a cuánta gente llega la lengua. Escribe las letras. Regla: la casa llega a menos personas y la radio a más.", "A, C, B", "La casa llega a pocas personas, la sede a una comunidad y la radio llega más lejos."),
    ],
    context=[ex("En tu escuela se quiere ayudar a que una lengua indígena se use más. ¿Cuál idea crea un espacio nuevo: A) colocar un letrero de bienvenida en la lengua con ayuda del educador tradicional o B) esperar a que alguien lo haga?", "A", "Un letrero es un espacio nuevo donde la lengua se ve.")],
    selfcheck=[
        ex("¿Revitalizar es usar la lengua en más lugares y por más personas? Sí o No.", "Sí", "Esa es la definición vista."),
        ex("¿La identidad de un pueblo es solo su lengua? Sí o No.", "No", "También incluye historia, territorio y formas de vivir."),
        ex("Quien aprende de una comunidad y devuelve agradecimiento y cuidado, ¿practica reciprocidad o competencia?", "reciprocidad", "Devolver con cuidado es reciprocidad."),
    ],
    task=T(
        "Lee esta ficha inventada: «En la Comunidad Muestra hay cuatro espacios: la casa, un taller en la escuela, un programa de radio y un cartel en la plaza. Una persona de la comunidad dice que la lengua es parte de lo que la hace sentirse de su pueblo.» En tu cuaderno haz una tabla de dos columnas: espacio y qué aporta a que la lengua se use más. Después escribe una frase que explique cómo se relacionan uso, identidad y revitalización y otra frase que diga qué devolverías tú a quien te enseña.",
        "Casa: se escucha y se practica. Taller: práctica guiada. Radio: llega lejos. Cartel: hace visible la lengua. Frase: Cuando la lengua se usa en varios espacios, más personas la escuchan y se sienten parte de su pueblo, y eso ayuda a revitalizarla. Devolvería agradecimiento y cuidado de lo aprendido.",
        ["relaciona cada espacio con un aporte distinto", "explica uso, identidad y revitalización", "no mide la pertenencia por hablar la lengua", "propone una forma de reciprocidad"],
        ["tabla de dos columnas", "dos frases escritas"],
        ["decir que quien no habla no pertenece", "repetir el mismo aporte para todos los espacios"],
        "Si la tabla repite aportes, pide que piense a quién llega cada espacio y qué hace allí la lengua.",
    ),
    reinforce="Relee la ficha de espacios y dibuja un esquema con una flecha desde cada espacio hasta su aporte.",
    extend="Escribe un párrafo de cuatro oraciones sobre qué espacios nuevos podría tener una lengua indígena en tu localidad, sin inventar palabras de la lengua.",
)

# ============================================================ LR05 clase 4 · respuesta atribuida
FUE = "Ficha de fuente (inventada): Comunidad Ejemplo, pueblo mapuche. Persona que cuenta: la educadora tradicional de la Escuela Ejemplo. Lo que cuenta: el taller de los jueves empieza con «mari mari» y todas las personas responden el saludo. Dice que es importante porque así los niños y las niñas escuchan la lengua con alegría. Aclara que cada comunidad tiene sus propias costumbres."

L(
    LR5, 4,
    materials="Lápiz y hoja. La ficha está escrita aquí y es inventada para practicar. No necesitas dispositivos.",
    use="Aprenderé a escribir una respuesta corta sobre un uso de la lengua indígena y su importancia, diciendo de quién es la información y hasta dónde vale. Sirve para explicar lo que aprendí sin quitarle la voz a nadie.",
    prior=["Sé separar lo que dice la fuente de lo que pienso.", "Sé relacionar usos de la lengua con identidad y revitalización."],
    explain=[
        "Una respuesta atribuida es una respuesta que dice de quién es lo que cuenta. Tiene cuatro partes. La primera atribuye: «Según la educadora tradicional de la Escuela Ejemplo…». La segunda dice el uso: «…el taller de los jueves empieza con un saludo». La tercera explica por qué importa: «…porque los niños escuchan la lengua con alegría». La cuarta declara el límite: «Esto vale para esa comunidad».",
        "Al escribir uso solo las palabras de la lengua que la fuente me dio, como «mari mari», y las copio tal cual. No invento palabras ni explico sentidos que nadie me contó. Si quiero decir algo mío, lo marco con «yo pienso». Así se distingue lo que aprendí de otros de lo que concluyo yo.",
        "Después reviso mi respuesta con una pregunta: ¿alguien podría saber de dónde salió cada dato? Si la respuesta es sí, está bien atribuida. Si no, agrego la fuente o quito el dato. Y antes de compartirla, pregunto al educador o educadora tradicional si lo que escribí respeta lo que se enseñó.",
    ],
    vocab=[("atribuir", "decir quién es la fuente de un dato"), ("respuesta atribuida", "respuesta que dice de quién es la información"), ("límite", "hasta dónde vale lo que se cuenta"), ("copiar tal cual", "escribir una palabra igual que como me la enseñaron"), ("compartir", "mostrar mi trabajo a otras personas")],
    worked=[
        W("Armar una respuesta", FUE + " Escribe la primera parte de una respuesta atribuida.", ["La primera parte atribuye.", "Nombro a la persona y su lugar.", "Empiezo con «Según»."], "Según la educadora tradicional de la Escuela Ejemplo,"),
        W("Revisar una respuesta", "Una respuesta dice: «Los mapuche siempre saludan con mari mari en todos los talleres del país». ¿Qué parte falta o sobra?", ["Busco la atribución: no hay fuente.", "Busco el límite: dice «siempre» y «todo el país».", "Eso generaliza más de lo que dice la ficha."], "falta la fuente y sobra la generalización"),
    ],
    mistakes=[
        M("Escribir la respuesta sin decir quién lo contó.", "Nadie puede comprobar de dónde salió.", "Empiezo con «Según…» y nombro la fuente."),
        M("Agregar mi propia explicación como si la hubiera dicho la fuente.", "Le quito la voz y le pongo palabras que no dijo.", "Marco mis ideas con «yo pienso»."),
    ],
    R=[
        ex(FUE + " ¿Quién cuenta lo que dice la ficha?", "la educadora tradicional de la Escuela Ejemplo", "La ficha nombra a quien cuenta."),
        ex(FUE + " ¿Con qué saludo empieza el taller de los jueves?", "mari mari", "La ficha lo dice."),
        ex("Una respuesta atribuida, ¿dice de quién es la información o la deja sin fuente?", "dice de quién es la información", "Eso significa atribuida."),
    ],
    C=[
        ex(FUE + " Según la ficha, ¿por qué es importante el saludo?", "porque los niños y las niñas escuchan la lengua con alegría", "La ficha da esa razón."),
        ex(FUE + " ¿Qué límite declara la educadora?", "que cada comunidad tiene sus propias costumbres", "Lo dice al final de la ficha."),
        ex("¿Qué parte de la respuesta atribuida explica por qué el uso es importante: la atribución, la importancia o el límite?", "la importancia", "La tercera parte dice por qué importa el uso."),
    ],
    A=[
        ex("Ordena las partes de la respuesta: A) límite. B) atribución. C) importancia. D) uso. Escribe las letras en orden.", "B, D, C, A", "Atribuyo, cuento el uso, explico por qué importa y declaro el límite."),
        ex(FUE + " Elige la mejor respuesta atribuida: A) «Según la educadora tradicional de la Escuela Ejemplo, el taller empieza con «mari mari» y así los niños escuchan la lengua con alegría; esto vale para esa comunidad». B) «Todos los talleres empiezan con mari mari». Escribe la letra.", "A", "Atribuye, da el uso, la importancia y el límite."),
        ex("Una respuesta tiene 4 partes. A un estudiante le faltan 2. ¿Cuántas partes escribió?", "2", "Cuatro menos dos.", "4-2"),
    ],
    Z=[
        ex(FUE + " Una niña agrega a su respuesta: «Todas las familias de la comunidad participan cada jueves». ¿Esa idea está en la ficha? Sí o No.", "No", "La ficha no dice cuántas familias participan."),
        ex(FUE + " Si la niña quiere dar su opinión, ¿cómo debe marcarla: con «yo pienso» o escribiéndola como si fuera de la educadora?", "con «yo pienso»", "Así se distingue lo mío de lo dicho por la fuente."),
    ],
    D=[
        ex("Una respuesta dice: «Según una vecina, el taller empieza con un saludo». ¿Qué parte falta para estar completa: el límite, el uso o la atribución?", "el límite", "Atribuye y cuenta el uso, pero no dice hasta dónde vale."),
        ex("Una respuesta usa la palabra «mari mari» escrita «mari-mari-mari». La ficha la escribe «mari mari». ¿Qué debe hacer quien escribe: copiarla tal cual la ficha o cambiarla a su gusto?", "copiarla tal cual la ficha", "Las palabras se copian como las enseñó la fuente."),
    ],
    context=[ex("Vas a contar en tu curso lo que una persona mayor te explicó sobre su lengua. ¿Dices su nombre o cargo, si ella lo autoriza, o dices «un señor me dijo»?", "dices su nombre o cargo, si ella lo autoriza", "Una fuente clara y con permiso es mejor.")],
    selfcheck=[
        ex("¿Con qué palabra empieza una respuesta atribuida: «según» o «siempre»?", "según", "Según nombra la fuente."),
        ex("¿Debo inventar el significado de una palabra que no entiendo? Sí o No.", "No", "Se pregunta al educador o educadora tradicional."),
        ex("Antes de compartir mi respuesta, ¿pregunto al educador o educadora tradicional? Sí o No.", "Sí", "Así reviso que respete lo enseñado."),
    ],
    task=T(
        "Lee esta ficha inventada: «Comunidad Muestra, pueblo aymara. Un educador tradicional cuenta que en su comunidad la reunión de padres comienza con un saludo y que eso ayuda a que se escuche la lengua. Dice que habla solo por su comunidad.» En tu cuaderno escribe una respuesta de cuatro oraciones con estas partes: atribución, uso, importancia y límite. No agregues palabras de la lengua que la ficha no tenga.",
        "Según un educador tradicional de la Comunidad Muestra, del pueblo aymara, la reunión de padres comienza con un saludo. Eso ayuda a que se escuche la lengua. Él habla solo por su comunidad. Yo pienso que es una buena forma de acercar a las familias.",
        ["tiene atribución", "cuenta un uso", "explica por qué importa", "declara el límite y marca lo propio con «yo pienso»"],
        ["respuesta de cuatro oraciones"],
        ["omitir la fuente", "agregar palabras de la lengua inventadas"],
        "Pide que subraye en la ficha cada dato usado; si algo no está subrayado, debe marcarse como idea propia.",
    ),
    reinforce="Copia la respuesta modelo del ejemplo y subraya con un color cada una de las cuatro partes.",
    extend="Escribe dos respuestas atribuidas sobre el mismo uso, una con límite y otra sin él, y explica cuál es mejor y por qué.",
)
