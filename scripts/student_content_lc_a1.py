"""Student material for 1.º básico Lengua y Cultura de los Pueblos Originarios Ancestrales, OA 07 (territorio) y OA 08 (memoria familiar).

Criterio de autoría: solo contenidos generales de cultura y territorio que se pueden afirmar con certeza;
ningún ejercicio exige saber una lengua indígena; toda tarea abierta remite al educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import ex, register

OA7, OA8 = "LC01 OA 07", "LC01 OA 08"

CONSULT = " Recuerda: la forma tradicional de hacer o contar esto la enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales a ellos antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."


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


# Fichas breves con datos generales y ampliamente conocidos (se escriben completas para que nadie tenga que buscarlas).
F_LICK = "Pueblo lickanantay: vive en el desierto de Atacama, donde hay oasis, un gran salar y volcanes. El agua es muy valiosa."
F_AYM = "Pueblo aymara: vive en el norte de Chile, en el altiplano, entre cerros y volcanes. Cría llamas y alpacas y cultiva papas."
F_RN = "Pueblo rapa nui: vive en una isla del océano Pacífico, con volcanes, costa y los moai, grandes figuras de piedra."
F_KAW = "Pueblo kawésqar: vive en los canales de la Patagonia occidental, donde hay mar, islas, lluvia y bosques. Navega en canoas."
F_DIA = "Pueblo diaguita: vive en los valles del Norte Chico, junto a los ríos Elqui, Limarí y Huasco. Hace cerámica con dibujos geométricos."
F_MAP = "Pueblo mapuche: vive sobre todo en el centro y sur de Chile, donde hay ríos, lagos, bosques y volcanes."

# ============================================================ OA 07 · Territorio ancestral e identidad
L(
    OA7, 1,
    materials="Lápiz, hojas y colores. Las fichas con los datos están escritas en este cuaderno; no necesitas buscar nada.",
    use="Aprenderé a describir un territorio mirando el agua, el relieve, los caminos, los nombres y lo que la gente hace allí. Sirve para entender que un territorio es mucho más que una línea en un mapa.",
    prior=["Sé qué es un río, un cerro y un camino.", "Sé que en Chile viven distintos pueblos originarios."],
    explain=[
        "El territorio ancestral es el lugar donde un pueblo originario ha vivido, ha cuidado la tierra y ha guardado su memoria durante mucho tiempo. No es solo un terreno. También son los ríos, los cerros, los caminos, los nombres de los lugares y lo que las personas hacen allí.",
        "Para describir un territorio podemos mirar cinco cosas: el agua, el relieve, los caminos, los nombres y las prácticas. El agua puede ser un río, un lago, un mar o un salar. El relieve puede ser un cerro, un volcán, un valle o una isla.",
        "Cada pueblo tiene su propio territorio y es distinto de los demás. El del pueblo lickanantay es un desierto con oasis; el del pueblo kawésqar tiene canales y mar. Por eso no se puede decir que todos los pueblos viven igual. Y si no sabemos de qué pueblo es un paisaje, preguntamos y no adivinamos.",
    ],
    vocab=[("territorio ancestral", "lugar donde un pueblo ha vivido y cuidado la tierra por mucho tiempo"), ("paisaje", "lo que se ve en un lugar: agua, cerros, plantas"), ("relieve", "las formas de la tierra, como cerros, valles y volcanes"), ("práctica", "algo que las personas hacen en un lugar"), ("fuente", "la persona o el texto que nos dio el dato")],
    worked=[
        W("Describir con la ficha", F_LICK + " ¿Qué agua y qué relieve nombra la ficha?", ["Busco palabras de agua: oasis, salar.", "Busco palabras de relieve: volcanes.", "También veo el clima: desierto."], "Agua: oasis y salar. Relieve: volcanes."),
        W("No adivinar el pueblo", "Una foto sin título muestra un salar. ¿De qué pueblo es?", ["Un salar existe en varios lugares.", "La foto no dice quién la tomó ni de qué pueblo habla.", "Pregunto al profesor o a una fuente antes de afirmar."], "No se puede saber sin una fuente."),
    ],
    mistakes=[
        M("Decir que el territorio es solo una línea en el mapa.", "Se olvida lo que la gente hace y recuerda en ese lugar.", "Describe también agua, relieve, caminos, nombres y prácticas."),
        M("Pensar que todos los pueblos viven en el mismo tipo de paisaje.", "Cada pueblo tiene un territorio distinto.", "Mira la ficha de cada pueblo y compara sin mezclar."),
    ],
    R=[
        ex("Ficha: " + F_AYM + " ¿Cuál de estas cosas es un animal de la ficha? A) cerros B) llamas C) volcanes", "B) llamas", "Las llamas son animales; los cerros y volcanes son relieve."),
        ex("El mar, un río y un lago son parte del paisaje. ¿Son agua, relieve o camino?", "Agua", "Mar, río y lago son agua."),
        ex("Un cerro y un volcán son formas altas de la tierra. ¿Son agua o relieve?", "Relieve", "El relieve son las formas de la tierra."),
    ],
    C=[
        ex("¿Cuál frase describe un paisaje? A) «Mi vecina vive en la casa azul.» B) «Hay canales, islas y mucha lluvia.»", "B", "La frase B habla de agua y de formas de la tierra."),
        ex("Verdadero o falso: el territorio ancestral es solo la dirección de la casa de una familia.", "Falso", "Es el lugar de un pueblo entero, con su memoria y sus prácticas."),
        ex("Para describir un territorio se miran: agua, relieve, caminos, nombres y prácticas. ¿Cuántas cosas son?", "5", "Se cuentan una a una: agua, relieve, caminos, nombres y prácticas."),
    ],
    A=[
        ex("Pon cada palabra en su grupo, AGUA o RELIEVE: río, cerro, lago, volcán, mar.", "Agua: río, lago, mar. Relieve: cerro, volcán.", "Río, lago y mar son agua; cerro y volcán son formas de la tierra."),
        ex("Une cada pueblo con su paisaje. 1) rapa nui 2) lickanantay 3) kawésqar. a) salar y desierto b) isla en el Pacífico c) canales y canoas", "1-b, 2-a, 3-c", "Cada dato está en la ficha de su pueblo."),
        ex("Ficha: " + F_DIA + " ¿Qué tres ríos nombra la ficha?", "Elqui, Limarí y Huasco", "La ficha dice que viven junto a esos tres ríos."),
    ],
    Z=[
        ex("Pedro dice: «El territorio es solo lo que sale en el mapa». Ana dice: «También son los caminos, los nombres y lo que la gente hace allí». ¿Quién describe mejor el territorio?", "Ana", "Un territorio incluye prácticas y memoria, no solo lo dibujado."),
        ex("Lucía dice: «Todos los pueblos viven en el desierto como el lickanantay». ¿Por qué se equivoca?", "Porque cada pueblo tiene su territorio: hay islas, canales y valles", "Las fichas muestran paisajes distintos para pueblos distintos."),
    ],
    D=[
        ex("Una niña ve una foto de montañas con nieve y corrales con llamas, sin título. ¿Puede afirmar de qué pueblo es? Responde Sí o No y explica.", "No; falta una fuente", "Una foto sin título no dice qué pueblo es; hay que preguntar o buscar la fuente."),
        ex("Ficha: " + F_RN + " Escribe una frase con un elemento de agua y uno de relieve.", "Hay mar (agua) y volcanes (relieve)", "La ficha nombra costa y océano, y volcanes."),
    ],
    context=[ex("En clase leen: «" + F_KAW + "» Julia dice que ese pueblo cultiva papas en el altiplano. ¿Tiene razón?", "No", "La ficha habla de canales y canoas; las papas del altiplano son de la ficha aymara.")],
    selfcheck=[ex("¿Qué cinco cosas se miran al describir un territorio?", "Agua, relieve, caminos, nombres y prácticas", "Son las cinco ideas de la explicación."), ex("Si no sabes de qué pueblo es una foto, ¿qué haces?", "Pregunto y busco la fuente", "No se adivina el pueblo."), ex("Verdadero o falso: todos los pueblos tienen el mismo paisaje.", "Falso", "Cada territorio es distinto.")],
    task=T("Elige UNA ficha de las que están escritas arriba (aymara, rapa nui, kawésqar o diaguita). Dibuja su paisaje y escribe debajo una palabra de agua, una de relieve y una frase que diga qué hace la gente allí. No dibujes lugares sagrados ni casas de personas.",
           "Elegí la ficha kawésqar. Dibujé el mar, una isla y una canoa. Escribí: agua = mar; relieve = isla; la gente navega en canoas.",
           ["usa solo datos de la ficha", "nombra agua y relieve", "incluye una práctica"], ["dibujo", "tres palabras escritas", "frase con la fuente (la ficha)"], ["mezclar datos de dos fichas", "inventar un dato que no dice la ficha"],
           "Reconoce lo que sí viene de la ficha y pregunta de dónde sacó cada dato; si agregó algo nuevo, conversar si tiene fuente."),
    reinforce="Mira la ficha lickanantay y subraya con un color las palabras de agua y con otro las de relieve.",
    extend="Compara las fichas aymara y kawésqar: escribe una cosa distinta de su paisaje.",
)

L(
    OA7, 2,
    materials="Lápiz y hojas. Los nombres de lugares que se usan están escritos en el cuaderno.",
    use="Aprenderé que los nombres de los lugares guardan memoria. Sirve para valorar un nombre sin inventar lo que significa.",
    prior=["Sé que cada lugar tiene un nombre.", "Sé que en Chile se hablan el español y otras lenguas."],
    explain=[
        "Los lugares tienen nombres, y los nombres cuentan historias. Un nombre puede recordar quién vivió allí, qué había en ese lugar o qué pasó. Por eso los nombres de los lugares son parte de la memoria de un pueblo.",
        "En Chile, algunos lugares tienen nombres en lenguas de los pueblos originarios y otros tienen nombres en español. Rapa Nui, por ejemplo, es el nombre de la isla, del pueblo y de su lengua. Si un cartel dice «Río Claro», sus palabras son del español.",
        "Cuando un nombre viene de una lengua indígena, no debemos inventar su significado. Si queremos saberlo, preguntamos al educador o educadora tradicional, o a un libro confiable. Un significado inventado puede ser falso y faltar al respeto a la memoria de ese pueblo.",
    ],
    vocab=[("nombre de lugar", "palabra con que se llama a un lugar"), ("memoria", "lo que un pueblo recuerda y cuenta"), ("significado", "lo que quiere decir una palabra"), ("lengua", "idioma que habla un pueblo"), ("fuente confiable", "persona o libro que sabe del tema y dice de dónde lo sabe")],
    worked=[
        W("Leer un nombre", "Un cartel dice «Cerro Grande». ¿Qué lengua usan sus palabras y qué nos cuenta?", ["«Cerro» y «grande» son palabras del español.", "Cuenta cómo es el lugar: un cerro alto.", "No necesito inventar nada más."], "Español; describe el lugar."),
        W("Un nombre que no entiendo", "Un niño no sabe qué significa el nombre de un pueblo cercano. ¿Qué hace?", ["No inventa un significado.", "Pregunta a una persona que sepa, como el educador tradicional.", "Anota su respuesta y dice quién se la dio."], "Pregunta y anota la fuente."),
    ],
    mistakes=[
        M("Inventar qué significa un nombre porque «suena a indígena».", "Un significado inventado puede ser falso.", "Pregunta a una fuente confiable y anota quién lo dijo."),
        M("Pensar que los nombres en español no guardan memoria.", "Todos los nombres de lugar cuentan algo.", "Pregunta por qué se llama así el lugar."),
    ],
    R=[
        ex("Un cartel dice «Río Claro». ¿Sus palabras son del español o de una lengua indígena?", "Del español", "«Río» y «claro» son palabras españolas."),
        ex("Rapa Nui es el nombre de la isla, del pueblo y de su lengua. ¿Cuántas cosas nombra?", "3", "La isla, el pueblo y la lengua son tres cosas."),
        ex("¿Los nombres de lugares guardan memoria? Sí o No.", "Sí", "Cuentan quién vivió allí o cómo es el lugar."),
    ],
    C=[
        ex("¿Qué haces si no sabes qué significa un nombre de lugar? A) Invento uno B) Pregunto a una fuente confiable", "B", "Inventar puede dar un dato falso."),
        ex("Verdadero o falso: «Cerro Alto» tiene palabras del español.", "Verdadero", "«Cerro» y «alto» son español."),
        ex("¿Para qué sirven los nombres de los lugares para un pueblo?", "Para guardar y contar su memoria", "Cada nombre recuerda algo del lugar o de su historia."),
    ],
    A=[
        ex("Lee los nombres: Río Seco, Cerro Verde, Rapa Nui, Lago Chico. ¿Cuál es el nombre que también nombra a un pueblo y a su lengua?", "Rapa Nui", "Solo Rapa Nui nombra isla, pueblo y lengua a la vez."),
        ex("Marca solo los nombres de lugar que tienen palabras del español: Valle Hondo, Rapa Nui, Cabo Largo.", "Valle Hondo y Cabo Largo", "Esas dos tienen palabras españolas."),
        ex("Ordena los pasos: 1) anoto quién me lo dijo 2) pregunto al educador tradicional 3) no invento. ¿Cuál es el orden correcto?", "3, 2, 1", "Primero no invento, luego pregunto, al final anoto la fuente."),
    ],
    Z=[
        ex("Tomás dice: «Ese nombre suena indígena, seguro significa agua bonita». ¿Qué error comete?", "Inventa el significado sin fuente", "Solo una fuente confiable puede decir qué significa."),
        ex("Rosa dice que los nombres en español no cuentan nada del pasado. ¿Tiene razón?", "No", "También recuerdan cómo es el lugar o quién llegó."),
    ],
    D=[
        ex("Un libro dice sin autor: «Este nombre significa estrella dorada». ¿Basta para estar seguro? Responde Sí o No.", "No", "No dice quién lo sabe ni de dónde viene el dato."),
        ex("Dos vecinos dan significados distintos a un mismo nombre. ¿Qué es mejor hacer?", "Preguntar al educador tradicional o a la comunidad", "Puede haber más de una explicación y alguien que sabe debe orientar."),
    ],
    context=[ex("El curso hace una lista de lugares cercanos: Plaza Nueva, Río Seco y Rapa Nui. Rapa Nui está en el océano Pacífico. ¿Qué nombre de la lista no es del barrio, aunque sea de Chile?", "Rapa Nui", "Es la isla del Pacífico, lejos de un barrio cualquiera.")],
    selfcheck=[ex("¿Por qué no se inventa el significado de un nombre?", "Porque puede ser falso", "Sin fuente se puede dar un dato falso."), ex("¿A quién puedes preguntar?", "Al educador o educadora tradicional", "Es quien puede enseñar ese saber."), ex("¿Los nombres guardan memoria?", "Sí", "Cuentan cosas del lugar.")],
    task=T("Mira esta lista de nombres: Río Seco, Cerro Verde, Rapa Nui, Valle Hondo. Escribe cuáles tienen palabras del español y cuáles no. Luego escribe una pregunta que le harías al educador tradicional sobre un nombre de lugar de tu zona.",
           "Río Seco, Cerro Verde y Valle Hondo tienen palabras del español. Rapa Nui es el nombre de una isla, de un pueblo y de su lengua. Mi pregunta: ¿qué cuenta el nombre de este cerro?",
           ["clasifica los nombres", "no inventa significados", "formula una pregunta respetuosa"], ["lista clasificada", "pregunta escrita"], ["inventar significados", "decir que un nombre es indígena sin saberlo"],
           "Valora la pregunta y verifica que no haya significados inventados; si inventó uno, pedir que lo marque como «por confirmar»."),
    reinforce="Lee en voz alta tres nombres de lugares del cuaderno y di cuáles tienen palabras del español.",
    extend="Escribe una pregunta sobre el nombre de un lugar que te gustaría hacer a una persona mayor de tu comunidad.",
)

L(
    OA7, 3,
    materials="Lápiz y hojas. Los casos están escritos en este cuaderno.",
    use="Aprenderé que los pueblos y los territorios cambian con el tiempo, y que las personas siguen perteneciendo a su pueblo aunque cambien de lugar.",
    prior=["Sé que las personas pueden mudarse.", "Sé qué es una ciudad."],
    explain=[
        "Un pueblo originario puede recorrer su territorio para vivir mejor. Algunos criaban animales y se movían con ellos de un lugar a otro según la estación. El pueblo kawésqar navegaba en canoas por los canales. Moverse no significa dejar de pertenecer al territorio.",
        "Con el tiempo hay cambios: llegan caminos, pueblos y ciudades, y algunas personas se mudan. Hoy muchas personas de pueblos originarios viven en ciudades y siguen perteneciendo a su pueblo y recordando su historia.",
        "Por eso no decimos que alguien «dejó de ser» de su pueblo porque vive lejos o usa un celular. La pertenencia se mantiene en la memoria, la familia y la comunidad. Cambiar de lugar no borra la identidad.",
    ],
    vocab=[("movilidad", "moverse de un lugar a otro"), ("continuidad", "algo que sigue a pesar del tiempo"), ("pertenencia", "sentirse parte de un pueblo o una comunidad"), ("ciudad", "lugar grande con muchas casas y servicios"), ("cambio", "algo que antes era de una manera y ahora es de otra")],
    worked=[
        W("Moverse sin perder el lugar", "Una familia sube con sus animales a los pastos altos en verano y baja en invierno. ¿Dejó de pertenecer a su territorio?", ["Se mueve siguiendo las estaciones.", "Siempre vuelve a los mismos lugares.", "Moverse es una forma de cuidar el territorio."], "No; moverse no quita la pertenencia."),
        W("Vivir en la ciudad", "Camila vive en una ciudad y recuerda las historias de su abuela, de un pueblo originario. ¿Sigue perteneciendo a su pueblo?", ["La pertenencia está en la memoria y en la familia.", "Vivir en ciudad es un cambio, no una pérdida.", "Ella decide cómo cuenta su historia."], "Sí, sigue perteneciendo."),
    ],
    mistakes=[
        M("Pensar que quien vive en la ciudad ya no es de su pueblo.", "La pertenencia no depende del lugar donde vives.", "Reconoce que hay cambios y también continuidad."),
        M("Creer que los pueblos originarios solo existieron antes.", "Los pueblos viven hoy y siguen cambiando.", "Habla de ellos también en presente."),
    ],
    R=[
        ex("Una familia lleva sus animales a otro pasto según la estación. ¿Eso es moverse o quedarse siempre?", "Moverse", "Cambia de lugar siguiendo las estaciones."),
        ex("El pueblo kawésqar navegaba en canoas. ¿Se movía por tierra o por el mar?", "Por el mar", "Sus canoas recorrían los canales."),
        ex("¿Una persona puede vivir en una ciudad y sentirse parte de su pueblo? Sí o No.", "Sí", "La pertenencia está en la memoria y la comunidad."),
    ],
    C=[
        ex("Verdadero o falso: si alguien se muda, deja de pertenecer a su pueblo.", "Falso", "La pertenencia no depende de dónde vives."),
        ex("¿Qué es un cambio? A) Algo que sigue igual B) Algo que antes era de una forma y ahora de otra", "B", "Cambio es pasar de una forma a otra."),
        ex("¿Los pueblos originarios viven hoy o solo existieron antes?", "Viven hoy", "Siguen vivos, con su cultura."),
    ],
    A=[
        ex("Clasifica cada caso como CAMBIO o CONTINUIDAD: a) llegó un camino nuevo b) una abuela cuenta la misma historia c) se construyó una ciudad cerca.", "a) cambio, b) continuidad, c) cambio", "Lo nuevo es cambio; lo que sigue contándose es continuidad."),
        ex("Une cada caso con su idea. 1) Una familia se muda a la ciudad 2) Siguen contando una historia antigua. a) cambio b) continuidad", "1-a, 2-b", "Mudarse es cambio; contar la historia de siempre es continuidad."),
        ex("Luz se mudó a otra ciudad y dice: «Sigo siendo de mi pueblo». ¿Qué le responde alguien que respeta? A) «Ya no lo eres» B) «Tienes derecho a sentirlo así»", "B", "No negamos la pertenencia de nadie."),
    ],
    Z=[
        ex("Beto dice: «Los pueblos originarios solo viven en el campo». ¿Qué le dices?", "Que muchas personas viven en ciudades y siguen siendo de su pueblo", "Hay personas de pueblos originarios en campo y en ciudad."),
        ex("¿Por qué moverse con los animales no es perder el territorio?", "Porque lo recorren y vuelven a los mismos lugares", "Sigue siendo su lugar de vida."),
    ],
    D=[
        ex("Ana ve una foto de una joven con celular en una comunidad. Dice: «Ya no es indígena». ¿Es un buen razonamiento? Sí o No.", "No", "Usar tecnología no borra la identidad."),
        ex("Una niña cuenta algo que le contó su abuelo de otro pueblo. ¿Qué debes preguntar antes de repetirlo?", "De quién es el relato y si se puede compartir", "Hay que respetar la fuente y el permiso."),
    ],
    context=[ex("Una vecina dice: «Mi abuelo criaba animales en la cordillera, hoy vivo en una ciudad y sigo siendo de mi pueblo». ¿Qué parte es cambio y cuál continuidad?", "Cambio: vive en ciudad. Continuidad: sigue siendo de su pueblo", "Se mudó, pero la pertenencia se mantiene.")],
    selfcheck=[ex("¿Moverse quita la pertenencia?", "No", "Se puede cambiar de lugar y seguir perteneciendo."), ex("En Lengua y Cultura: ¿Los pueblos originarios existen hoy?", "Sí", "Viven y cambian hoy."), ex("Da un ejemplo de cambio.", "Llega un camino o se construye una ciudad", "Es algo nuevo en el lugar.")],
    task=T("Lee este caso: «Tomás vive en una ciudad. Su familia viene de un pueblo originario del sur. Su abuela le cuenta historias de su tierra y él las dibuja.» Escribe un cambio y una continuidad del caso, y una frase respetuosa que le dirías a Tomás.",
           "Cambio: Tomás vive en la ciudad. Continuidad: sigue recibiendo las historias de su abuela. Frase: «Tu historia es importante».",
           ["identifica un cambio y una continuidad", "no niega la pertenencia", "usa lenguaje respetuoso"], ["dos frases", "frase para Tomás"], ["decir que Tomás ya no es de su pueblo"],
           "Destaca el respeto en la frase final; si negó la pertenencia, volver a leer la explicación juntos."),
    reinforce="Cuenta con tus palabras la diferencia entre cambio y continuidad con un ejemplo de tu casa.",
    extend="Escribe una pregunta para una persona mayor de tu comunidad sobre cómo cambió un lugar que conoce.",
)

L(
    OA7, 4,
    materials="Lápiz y hojas. Las descripciones para revisar están escritas en el cuaderno.",
    use="Aprenderé a escribir una descripción de un territorio diciendo de dónde saqué cada dato. Sirve para contar con verdad y respeto.",
    prior=["Sé describir lo que veo.", "Sé que una fuente es de dónde viene un dato."],
    explain=[
        "Una buena descripción dice qué pueblo es, cómo es su paisaje y qué hace la gente allí. Además dice de dónde sacamos esos datos. Eso se llama citar la fuente. La fuente puede ser una ficha, un libro, una conversación con el educador tradicional o una persona de la comunidad.",
        "Distinguimos tres cosas: lo que dice la fuente, lo que yo pienso y lo que no sé. Si no sé algo, lo escribo como pregunta. Por ejemplo, si la ficha no dice cuántas personas viven allí, no invento una cifra.",
        "Una descripción respetuosa no mezcla pueblos, no dice que todos son iguales y no cuenta secretos de un lugar sagrado. Podemos decir: «Según la ficha del pueblo kawésqar, viven en los canales». Esa frase cuida a quien nos enseñó.",
    ],
    vocab=[("describir", "decir cómo es algo"), ("citar la fuente", "decir de dónde viene el dato"), ("dato", "información que podemos comprobar"), ("opinión", "lo que yo pienso"), ("respetuoso", "que cuida a las personas y a lo que cuentan")],
    worked=[
        W("Escribir con fuente", "Usa la ficha: «" + F_DIA + "» Escribe una frase con fuente.", ["Escribo el pueblo: diaguita.", "Agrego el paisaje: valles del Norte Chico y tres ríos.", "Empiezo con «Según la ficha»."], "Según la ficha, el pueblo diaguita vive en valles del Norte Chico junto a tres ríos."),
        W("Separar dato y opinión", "«El territorio aymara es bonito.» ¿Es dato u opinión?", ["Lo bonito depende de cada persona.", "No se puede comprobar con una ficha.", "Es una opinión."], "Opinión."),
    ],
    mistakes=[
        M("Escribir datos sin decir de dónde salieron.", "Nadie puede comprobarlos.", "Empieza con «Según la ficha…» o «Según el educador tradicional…»."),
        M("Mezclar datos de dos pueblos en una descripción.", "Cada pueblo tiene su propio territorio.", "Usa una ficha por pueblo y no las mezcles."),
    ],
    R=[
        ex("¿Cuál empieza bien una descripción con fuente? A) «Según la ficha, el pueblo aymara…» B) «Dicen que…»", "A", "A dice cuál es la fuente."),
        ex("«El altiplano tiene cerros» ¿es dato o es opinión?", "Dato", "Se puede comprobar en la ficha."),
        ex("«Es el lugar más lindo» ¿es dato o es opinión?", "Opinión", "Cada persona puede pensar distinto."),
    ],
    C=[
        ex("¿Qué debe decir una buena descripción? A) el pueblo, el paisaje y la fuente B) solo un adjetivo", "A", "Así se entiende de qué pueblo y de dónde sale el dato."),
        ex("La ficha no dice cuántas personas viven en un lugar. ¿Inventas una cifra? Sí o No.", "No", "Inventar un dato puede ser falso."),
        ex("Verdadero o falso: citar la fuente es decir de dónde sacaste un dato.", "Verdadero", "Eso significa citar la fuente."),
    ],
    A=[
        ex("Ficha: «" + F_KAW + "» Escribe una frase con fuente sobre el agua de ese territorio.", "Según la ficha, el pueblo kawésqar vive en canales y mar", "La frase incluye la fuente y el dato de agua."),
        ex("Marca los datos que NO vienen de la ficha lickanantay: oasis, selva, salar, volcanes, nieve eterna.", "selva y nieve eterna", "La ficha solo nombra oasis, salar, volcanes y desierto."),
        ex("Ordena para escribir bien: 1) escribo el dato 2) digo la fuente («Según la ficha») 3) escribo el pueblo. ¿Qué orden es correcto?", "2, 3, 1", "Primero la fuente («Según la ficha»), luego el pueblo y al final el dato."),
    ],
    Z=[
        ex("Rosa escribió: «Los pueblos originarios viven todos en la montaña». ¿Qué falla tiene?", "Generaliza: cada pueblo tiene su territorio", "Hay pueblos de isla, de canales, de valles y de desierto."),
        ex("Una descripción cuenta dónde queda un cementerio sagrado con detalles. ¿Es respetuosa? Sí o No.", "No", "Los lugares sagrados no se exponen sin permiso de la comunidad."),
    ],
    D=[
        ex("Camila dice que su descripción es buena porque suena linda, aunque no tiene fuente. ¿Estás de acuerdo? Sí o No.", "No", "Una buena descripción necesita fuente."),
        ex("Un compañero usó la ficha rapa nui para describir el pueblo aymara. ¿Qué le dices?", "Que cada pueblo tiene su ficha y no se mezclan", "Los datos de un pueblo no sirven para otro."),
    ],
    context=[ex("Tu curso escribe un cartel con la ficha aymara: «" + F_AYM + "» ¿Cuál frase sirve de título? A) «Pueblo aymara: altiplano, cerros y llamas» B) «Todos los pueblos son iguales»", "A", "A resume la ficha; B es una generalización.")],
    selfcheck=[ex("¿Qué es citar la fuente?", "Decir de dónde viene el dato", "Así se puede comprobar."), ex("Si no sé un dato, ¿qué hago?", "Lo escribo como pregunta", "No se inventa."), ex("¿Se pueden mezclar fichas de pueblos distintos?", "No", "Cada pueblo tiene sus propios datos.")],
    task=T("Elige una ficha escrita en esta clase (por ejemplo la diaguita o la rapa nui). Escribe 3 frases: el pueblo, dos datos de su paisaje y la fuente («Según la ficha…»). Agrega una pregunta que no sabes.",
           "Según la ficha, el pueblo rapa nui vive en una isla del Pacífico. Hay volcanes y moai. Mi pregunta: ¿qué cuentan los mayores sobre los moai?",
           ["nombra el pueblo", "usa datos de la ficha", "cita la fuente", "incluye una pregunta"], ["3 frases", "1 pregunta"], ["mezclar fichas", "inventar un dato"],
           "Reconoce la fuente citada y la pregunta; revisa que cada dato esté realmente en la ficha."),
    reinforce="Escribe una frase con «Según la ficha» sobre el pueblo aymara.",
    extend="Escribe una pregunta que le harías al educador tradicional sobre el territorio de tu zona.",
)

L(
    OA7, 5,
    materials="Hoja, lápices de colores. La ficha con los datos que puedes dibujar está escrita en el cuaderno.",
    use="Aprenderé a dibujar un mapa del territorio sin mostrar lugares sagrados o delicados. Sirve para compartir con cuidado.",
    prior=["Sé dibujar ríos, cerros y caminos.", "Sé que algunos lugares son muy especiales para las comunidades."],
    explain=[
        "Un mapa respetuoso muestra lo que la comunidad permite mostrar: ríos, cerros, caminos públicos, plazas y escuelas. No muestra lugares sagrados, cementerios, sitios ceremoniales ni casas de personas, a menos que la comunidad lo pida o lo autorice.",
        "Antes de hacer un mapa, preguntamos: ¿quién me dio estos datos?, ¿puedo compartirlos?, ¿qué no debo dibujar? Si no estamos seguros, no lo ponemos. Es mejor dejar un espacio en blanco que mostrar algo que debía quedar protegido.",
        "Un mapa también necesita un título, una leyenda y la fuente. La leyenda explica qué significa cada dibujo. Así quien lo mire entiende qué pueblo es, qué se ve y de dónde salió la información.",
    ],
    vocab=[("mapa", "dibujo de un lugar visto desde arriba"), ("leyenda", "cuadro que explica los signos del mapa"), ("lugar sagrado", "lugar muy especial que la comunidad cuida"), ("autorización", "permiso que da alguien para usar o mostrar algo"), ("sensible", "que puede dañar si se muestra sin cuidado")],
    worked=[
        W("Elegir qué dibujar", "Dibujas un mapa del pueblo aymara con la ficha: altiplano, cerros, llamas. La abuela de Ana te cuenta de un lugar ceremonial. ¿Lo dibujas?", ["Lo ceremonial es sensible.", "Nadie me autorizó a mostrarlo.", "Dejo solo cerros, altiplano y llamas."], "No lo dibujo."),
        W("Armar la leyenda", "Dibujaste un triángulo para cerros y una línea azul para un río. ¿Qué pones en la leyenda?", ["Dibujo el triángulo y escribo «cerro».", "Dibujo la línea azul y escribo «río».", "Agrego el título y la fuente."], "Triángulo = cerro; línea azul = río."),
    ],
    mistakes=[
        M("Dibujar un lugar sagrado porque lo contó un amigo.", "Quien lo contó quizás no tenía permiso de la comunidad.", "No lo dibujes; pregunta al educador tradicional qué se puede mostrar."),
        M("Hacer un mapa sin título, leyenda ni fuente.", "Nadie sabe qué muestra ni de dónde salió.", "Agrega título, leyenda y fuente."),
    ],
    R=[
        ex("¿Qué cosa puede ir en un mapa respetuoso? A) un río B) un cementerio sagrado", "A", "El río es público; el cementerio no se muestra sin permiso."),
        ex("La leyenda del mapa explica los signos. ¿Sí o No?", "Sí", "Dice qué significa cada dibujo."),
        ex("¿Qué va en un título: el nombre del pueblo o una receta de cocina?", "El nombre del pueblo", "El título dice qué muestra el mapa."),
    ],
    C=[
        ex("Verdadero o falso: se puede dibujar cualquier lugar si lo dices con respeto.", "Falso", "Algunos lugares no se dibujan sin autorización."),
        ex("Si no estás seguro de si puedes mostrar un lugar, ¿qué haces?", "No lo pongo y pregunto", "Es mejor proteger que equivocarse."),
        ex("¿Para qué sirve la leyenda?", "Para explicar los signos del mapa", "Dice qué significa cada símbolo."),
    ],
    A=[
        ex("Ficha: «" + F_KAW + "» Marca lo que sí puedes dibujar: canales, canoa, casa de una persona, mar.", "canales, canoa, mar", "La casa de una persona no debe mostrarse."),
        ex("Escribe una leyenda para estos signos: triángulo, línea azul, círculo verde (bosque).", "Triángulo = cerro; línea azul = río; círculo verde = bosque", "Cada signo tiene un significado."),
        ex("Ordena para hacer un mapa respetuoso: 1) dibujar 2) preguntar qué se puede mostrar 3) poner título y fuente.", "2, 1, 3", "Primero preguntar, luego dibujar y al final título y fuente."),
    ],
    Z=[
        ex("Pedro quiere marcar con una cruz un lugar ceremonial para que «todos lo encuentren». ¿Qué le dices?", "Que no lo muestre sin permiso de la comunidad", "Un lugar sagrado puede dañarse si se difunde."),
        ex("Lucía no dibujó un lugar porque no estaba segura. ¿Hizo bien? Sí o No.", "Sí", "Ante la duda se protege el lugar."),
    ],
    D=[
        ex("Una niña tiene un dato muy lindo de un sitio sagrado, pero nadie le dio permiso para compartirlo. ¿Puede ponerlo en un mapa de su curso? Sí o No.", "No", "Sin autorización no se muestra."),
        ex("Un mapa muestra una escuela y un río, con leyenda y fuente, pero no tiene título. ¿Qué le falta?", "El título", "Un mapa lleva título, leyenda y fuente; no tiene lugares sagrados, así que solo falta el título."),
    ],
    context=[ex("Tu curso hace un mapa del pueblo diaguita con la ficha: «" + F_DIA + "» ¿Qué dibujas? A) los tres ríos y los valles B) la casa de una familia", "A", "Los ríos y valles están en la ficha; la casa de una familia es privada.")],
    selfcheck=[ex("¿Qué NO se dibuja sin permiso?", "Lugares sagrados o delicados", "Pueden dañarse si se muestran."), ex("¿Qué tres cosas lleva un mapa?", "Título, leyenda y fuente", "Así se entiende y se puede comprobar."), ex("Si dudas, ¿qué haces?", "No lo pongo y pregunto", "Es mejor proteger.")],
    task=T("Dibuja en una hoja un mapa de uno de estos territorios, solo con los datos de su ficha: kawésqar (mar, canales, islas, canoa) o aymara (altiplano, cerros, llamas). Agrega título, leyenda y la frase «Fuente: ficha del cuaderno». No dibujes casas ni lugares sagrados.",
           "Mapa del pueblo kawésqar. Leyenda: línea azul = canal; círculo = isla; canoa = triángulo. Fuente: ficha del cuaderno.",
           ["usa solo datos de la ficha", "tiene título, leyenda y fuente", "no muestra lugares sagrados ni casas"], ["mapa dibujado", "leyenda"], ["dibujar casas de personas", "no poner fuente"],
           "Reconoce la leyenda y la fuente; si apareció un lugar delicado, conversar por qué no se muestra."),
    reinforce="Dibuja tres signos de mapa (río, cerro, camino) y escribe su leyenda.",
    extend="Escribe dos preguntas para la comunidad: qué se puede mostrar y qué no de un lugar de tu zona.",
)

# ============================================================ OA 08 · Memoria familiar y transmisión cultural
L(
    OA8, 1,
    materials="Lápiz y hojas. Los casos con historias, comidas y canciones inventadas para practicar están escritos en el cuaderno.",
    use="Aprenderé que las familias y las comunidades pasan conocimientos de una generación a otra. Sirve para valorar lo que nos enseñan los mayores.",
    prior=["Sé quiénes son los abuelos y las personas mayores.", "Sé contar un cuento corto."],
    explain=[
        "Las familias y las comunidades guardan memoria: cuentos, canciones, recetas, formas de cultivar, de tejer o de cuidar a los demás. Esa memoria se pasa de personas mayores a personas más jóvenes. A eso le llamamos transmisión cultural.",
        "Lo que se transmite puede ser un conocimiento, como cuándo sembrar; una habilidad, como tejer; un valor, como compartir; o un relato, como una historia de la comunidad. No todo se transmite con palabras: también se aprende mirando y haciendo.",
        "No todos los conocimientos se pueden contar a cualquiera. Algunos los guardan personas que la comunidad reconoce. Cuando una persona mayor nos cuenta algo, agradecemos y preguntamos si lo podemos compartir.",
    ],
    vocab=[("memoria", "lo que una familia o comunidad recuerda"), ("transmitir", "pasar algo a otra persona para que lo aprenda"), ("generación", "grupo de personas de edades parecidas"), ("relato", "historia que se cuenta"), ("conocimiento", "lo que se sabe de algo")],
    worked=[
        W("Qué se transmite", "Una abuela enseña a su nieta a hacer pan y le cuenta cómo lo hacía su mamá. ¿Qué se transmite?", ["Se transmite una habilidad: hacer pan.", "Se transmite un recuerdo familiar.", "Lo aprende haciendo con ella."], "Una habilidad y un recuerdo."),
        W("Quién puede contar", "Beto escuchó una historia muy especial de un anciano de la comunidad. ¿Puede contarla en toda la escuela?", ["Primero debe preguntar si se puede compartir.", "El anciano decide qué se cuenta y cómo.", "Si no lo autoriza, no la cuenta."], "Solo si la persona lo autoriza."),
    ],
    mistakes=[
        M("Pensar que solo se transmite con palabras.", "También se aprende observando y practicando.", "Pregunta qué se aprende mirando y haciendo."),
        M("Contar a todos una historia que te dijeron en confianza.", "La persona que la contó puede no querer que se difunda.", "Pregunta si la puedes compartir."),
    ],
    R=[
        ex("Una abuela enseña a tejer a su nieto. ¿Qué se transmite: una habilidad o un juguete?", "Una habilidad", "Tejer es algo que se sabe hacer."),
        ex("Una canción de la familia que se canta de abuelos a nietos, ¿es memoria? Sí o No.", "Sí", "Se recuerda y se pasa."),
        ex("¿Quiénes suelen transmitir conocimientos en una comunidad? A) las personas mayores B) nadie", "A", "Las personas mayores guardan mucha memoria."),
    ],
    C=[
        ex("Verdadero o falso: solo se aprende con palabras.", "Falso", "También se aprende mirando y haciendo."),
        ex("¿Qué es transmitir? A) pasar algo a otra persona B) guardar algo en un cajón", "A", "Se pasa un saber a otra persona."),
        ex("¿Qué haces si te cuentan algo muy especial?", "Agradezco y pregunto si lo puedo compartir", "Se respeta a quien lo contó."),
    ],
    A=[
        ex("Clasifica: a) cuento b) receta c) sembrar papas. Une con RELATO, RECETA o TÉCNICA.", "a) relato, b) receta, c) técnica", "Cada uno es un tipo de saber distinto."),
        ex("Escribe dos cosas que una familia puede transmitir.", "Respuesta aceptable: recetas y cuentos (u otra del texto)", "Cuentos, recetas, canciones y técnicas se transmiten."),
        ex("Lucía aprendió a hacer un nudo mirando a su tío. ¿Aprendió con palabras o mirando y haciendo?", "Mirando y haciendo", "Lo aprendió observando."),
    ],
    Z=[
        ex("Ana dice: «Mi abuelo nunca escribió nada, entonces no sabe nada». ¿Por qué se equivoca?", "Porque la memoria también se guarda y se cuenta sin escribir", "Los conocimientos pueden pasar por la voz y la práctica."),
        ex("¿Por qué agradecemos a quien nos cuenta un saber?", "Porque nos entregó algo valioso", "Es una forma de respeto."),
    ],
    D=[
        ex("Matías quiere grabar a su tía sin avisarle. ¿Está bien? Sí o No.", "No", "Primero se pide permiso."),
        ex("Un relato familiar se cuenta distinto en dos casas. ¿Cuál está equivocada?", "Ninguna se puede juzgar sin preguntar a los mayores", "Puede haber versiones distintas."),
    ],
    context=[ex("Una niña dice: «Mi abuela me enseñó una canción y cómo se hace un tejido». Cuenta cuántos saberes menciona.", "2", "Una canción y un tejido son dos saberes.")],
    selfcheck=[ex("¿Qué significa transmitir?", "Pasar un saber a otra persona", "Se enseña para que se aprenda."), ex("¿Todo se puede contar a cualquiera?", "No", "Hay saberes que se cuidan."), ex("¿Cómo puedes aprender sin palabras?", "Mirando y haciendo", "Se aprende observando y practicando.")],
    task=T("Escoge uno de estos casos escritos: a) una abuela enseña a hacer pan b) un tío enseña a atar un nudo c) una vecina canta una canción. Escribe qué se transmite, quién enseña y cómo aprende la niña o niño. No cuentes nada privado de tu familia.",
           "Caso b: se transmite una técnica (atar un nudo). Enseña el tío. El niño aprende mirando y probando.",
           ["dice qué se transmite", "dice quién enseña", "dice cómo se aprende"], ["tres frases escritas"], ["decir que solo se transmite con palabras"],
           "Reconoce las tres ideas; pregunta cómo sabría si ese saber se puede compartir."),
    reinforce="Dibuja a una persona mayor enseñando algo a una persona más joven.",
    extend="Escribe una pregunta que le harías a una persona mayor de tu comunidad sobre algo que ella sepa hacer.",
)

L(
    OA8, 2,
    materials="Lápiz y hojas. Las situaciones de enseñanza están escritas en el cuaderno.",
    use="Aprenderé quiénes enseñan y de qué maneras se enseña en las familias y comunidades: hablando, mirando y practicando.",
    prior=["Sé que las personas mayores enseñan.", "Sé que se aprende de varias maneras."],
    explain=[
        "En una comunidad, enseñan muchas personas: abuelos, tíos, madres y padres, vecinos y también el educador o la educadora tradicional. Cada uno puede enseñar cosas distintas. A veces enseña quien sabe más de un tema.",
        "Hay tres maneras de enseñar. Una es la oralidad: se cuenta con la palabra. Otra es la observación: se aprende mirando cómo lo hace otra persona. La tercera es la práctica: se aprende haciendo, con ayuda, una y otra vez.",
        "Muchas veces se usan las tres juntas. Por ejemplo, una abuela cuenta cómo se hace un tejido, lo muestra y luego te deja intentar. Para aprender bien hay que escuchar con atención, mirar con respeto y practicar con paciencia.",
    ],
    vocab=[("oralidad", "enseñar y aprender con la palabra dicha"), ("observar", "mirar con atención"), ("práctica", "aprender haciendo"), ("educador tradicional", "persona de la comunidad que enseña la cultura de su pueblo"), ("paciencia", "calma para seguir intentando")],
    worked=[
        W("Reconocer la manera", "Tomás miró cómo su tía amasaba el pan y después lo hizo él. ¿Cómo aprendió?", ["Primero miró.", "Después lo hizo.", "Eso es observación y práctica."], "Por observación y práctica."),
        W("Elegir quién enseña", "Rosa quiere saber cómo se hace un tejido tradicional. ¿A quién le puede preguntar?", ["A una persona que sepa tejer.", "Puede ser una tía, una abuela o el educador tradicional.", "Primero debe pedir permiso con respeto."], "A quien sabe tejer, como el educador tradicional o una persona mayor."),
    ],
    mistakes=[
        M("Pensar que solo enseña el profesor de la escuela.", "En la comunidad enseñan muchas personas.", "Reconoce también a abuelos, tíos y educadores tradicionales."),
        M("Querer aprender rápido sin practicar.", "Practicar toma tiempo.", "Ten paciencia y repite varias veces."),
    ],
    R=[
        ex("Una abuela cuenta un cuento con su voz. ¿Es oralidad, observación o práctica?", "Oralidad", "Se enseña con la palabra."),
        ex("Beto mira cómo su papá arma una red. ¿Aprende por oralidad u observación?", "Observación", "Aprende solo mirando."),
        ex("Ana prueba hacer un nudo varias veces. ¿Es práctica?", "Sí", "Aprende al hacer."),
    ],
    C=[
        ex("¿Quién puede enseñar en una comunidad? A) solo una persona B) abuelos, tíos, vecinos y educadores", "B", "Muchas personas enseñan."),
        ex("Verdadero o falso: observar es mirar con atención.", "Verdadero", "Observar es mirar con atención."),
        ex("¿Qué se necesita para aprender bien?", "Escuchar, mirar y practicar con paciencia", "Las tres maneras se combinan."),
    ],
    A=[
        ex("Une cada acción con su manera. 1) escuchar un cuento 2) mirar cómo se teje 3) tejer con ayuda. a) oralidad b) observación c) práctica", "1-a, 2-b, 3-c", "Escuchar es oralidad, mirar es observación y hacer es práctica."),
        ex("Lee: «La tía cuenta, muestra y deja intentar a Luz». ¿Qué maneras usa?", "Oralidad, observación y práctica", "Cuenta, muestra y deja hacer."),
        ex("Marca quiénes pueden enseñar: abuela, vecino que sabe, educadora tradicional, robot de juguete.", "abuela, vecino que sabe y educadora tradicional", "El robot de juguete no es una persona de la comunidad."),
    ],
    Z=[
        ex("Pedro no practicó y dice «no sé tejer». ¿Qué le falta?", "Practicar", "La práctica es parte de aprender."),
        ex("Lucía dice que solo se aprende con libros. ¿Qué le respondes?", "Que también se aprende escuchando, mirando y haciendo", "Hay tres maneras de enseñar."),
    ],
    D=[
        ex("Dos niños aprendieron a hacer pan distinto, uno con su tía y otro con su abuela. ¿Quién tiene la manera correcta?", "Ninguno se puede juzgar; son versiones de cada familia", "Cada familia tiene su manera."),
        ex("Un adulto no quiere enseñarte un saber. ¿Qué haces? A) Insisto hasta que lo cuente B) Respeto y agradezco", "B", "Hay saberes que no se comparten con todos."),
    ],
    context=[ex("En una comunidad, una abuela enseña a tejer: primero cuenta una historia, luego muestra los pasos y después deja que la niña pruebe. ¿Cuántas maneras de enseñar hay?", "3", "Cuenta, muestra y deja probar son tres maneras.")],
    selfcheck=[ex("Nombra una manera de enseñar.", "Oralidad, observación o práctica", "Son las tres maneras vistas."), ex("¿Quién enseña en una comunidad?", "Muchas personas", "No solo una."), ex("¿Qué necesitas para practicar?", "Paciencia", "Aprender toma tiempo.")],
    task=T("Dibuja una historieta de 3 cuadros con este caso: «Una tía enseña a su sobrina a atar un nudo». Cuadro 1: la tía cuenta. Cuadro 2: la tía muestra. Cuadro 3: la sobrina prueba. Escribe debajo de cada cuadro la palabra oralidad, observación o práctica.",
           "Cuadro 1: la tía habla (oralidad). Cuadro 2: la sobrina mira (observación). Cuadro 3: la sobrina ata el nudo (práctica).",
           ["dibuja tres cuadros", "nombra la manera en cada uno", "usa el orden del caso"], ["historieta", "tres palabras"], ["confundir observación con práctica"],
           "Pide que explique con su voz en qué se diferencian las tres maneras; no corregir su dibujo cultural."),
    reinforce="Cuenta a alguien cómo aprendiste algo mirando.",
    extend="Escribe a quién le preguntarías cómo se hace un tejido tradicional y por qué.",
)

L(
    OA8, 3,
    materials="Lápiz y hojas. Dos versiones de un mismo relato inventado están escritas en el cuaderno.",
    use="Aprenderé a comparar dos versiones de lo que cuentan familias distintas sin decir que una es mejor. Sirve para respetar la memoria de cada familia.",
    prior=["Sé qué es un relato.", "Sé que a veces dos personas cuentan lo mismo de manera distinta."],
    explain=[
        "Cuando muchas personas cuentan un mismo relato, a veces cambian algunos detalles. Una familia puede recordar un camino y otra un río. Eso no siempre significa que alguien miente: cada familia guarda su memoria a su manera.",
        "Con el tiempo hay cambios y también continuidades. Un cambio puede ser un nuevo material para un tejido. Una continuidad puede ser que la historia se siga contando. Podemos comparar dos versiones y ver qué se parece y qué es distinto.",
        "Al comparar no decimos «esta versión es mejor». Decimos qué tienen en común, qué cambia y a quién podemos preguntar para saber más. Cada versión merece respeto, y el educador tradicional puede ayudar a entender de dónde viene cada una.",
    ],
    vocab=[("versión", "una manera de contar o hacer algo"), ("comparar", "mirar qué se parece y qué es distinto"), ("detalle", "una parte pequeña de algo"), ("jerarquizar", "decir que algo es mejor o peor que otra cosa"), ("en común", "lo que dos cosas tienen igual")],
    worked=[
        W("Comparar dos versiones", "Versión de Luz: «En el cuento, el niño sigue un río». Versión de Beto: «En el cuento, el niño sigue un camino». ¿Qué cambia y qué se mantiene?", ["Cambia el río por el camino.", "Se mantiene que el niño avanza siguiendo algo.", "No digo cuál es la correcta."], "Cambia el río o camino; se mantiene el niño que avanza."),
        W("Respetar las versiones", "Dos amigos cuentan la misma historia con finales distintos. ¿Qué dices?", ["Cada familia la guarda a su manera.", "No digo cuál es mejor.", "Puedo preguntar a una persona mayor."], "Respeto ambas y pregunto."),
    ],
    mistakes=[
        M("Decir «tu versión está mal».", "Es la memoria de otra familia.", "Di qué se parece y qué cambia."),
        M("Pensar que si cambia un detalle, la historia es falsa.", "Los relatos se cuentan de varias formas.", "Busca lo que se mantiene."),
    ],
    R=[
        ex("Dos niños cuentan la misma historia con un detalle distinto. ¿Es normal que cambie un detalle? Sí o No.", "Sí", "Cada familia guarda la historia a su manera."),
        ex("Comparar es mirar qué se parece y qué es distinto. ¿Verdadero o falso?", "Verdadero", "Esa es la idea de comparar."),
        ex("«Tu versión está mal» ¿es una frase respetuosa?", "No", "Hay que respetar la memoria de cada familia."),
    ],
    C=[
        ex("¿Qué puedes decir al comparar? A) «Esta es mejor» B) «Estas dos se parecen en…»", "B", "Se compara sin jerarquizar."),
        ex("Verdadero o falso: si una versión cambia un detalle, es una mentira.", "Falso", "Puede ser otra memoria."),
        ex("¿A quién puedes preguntar para entender las versiones?", "A una persona mayor o al educador tradicional", "Ellos conocen la historia de la comunidad."),
    ],
    A=[
        ex("Versión A: «La niña sembró papas en primavera». Versión B: «La niña sembró papas cuando salió el sol». ¿Qué tienen en común?", "La niña sembró papas", "Las dos cuentan que la niña sembró papas."),
        ex("Versión A: «El abuelo canta al tejer». Versión B: «La abuela canta al tejer». ¿Qué cambia?", "Quién canta", "Cambia abuelo o abuela."),
        ex("Clasifica como CAMBIO o CONTINUIDAD: a) la historia se sigue contando b) se usa lana de otro color.", "a) continuidad, b) cambio", "Contar la historia es continuidad; el color nuevo es cambio."),
    ],
    Z=[
        ex("Ana dice que su versión del cuento es la única verdadera. ¿Qué le dices?", "Que otras familias pueden guardar otra versión", "Las versiones de cada familia valen."),
        ex("¿Por qué no se jerarquiza una versión?", "Porque cada una es la memoria de una familia", "Todas se respetan."),
    ],
    D=[
        ex("Matías y Rosa cuentan una historia con tres cosas iguales y una distinta. ¿Cuántas cosas se mantienen?", "3", "Tres son iguales; una cambia."),
        ex("Una versión dice «hubo mucha lluvia» y otra «llovió poco». Para saber más sin elegir, ¿qué haces?", "Pregunto a una persona mayor", "No se decide solo; se pregunta."),
    ],
    context=[ex("Dos primos cuentan cómo llegaron las llamas a su valle. Uno dice que llegaron en verano, otro que en invierno. ¿Qué es lo mejor que puedes hacer?", "Anotar las dos versiones y preguntar a una persona mayor", "Así se respeta cada recuerdo.")],
    selfcheck=[ex("¿Qué es una versión?", "Una manera de contar algo", "Es cómo lo cuenta una familia."), ex("Al comparar, ¿decimos cuál es mejor?", "No", "No se jerarquiza."), ex("¿Qué puedes buscar en dos versiones?", "Lo que se parece y lo que cambia", "Eso es comparar.")],
    task=T("Lee estas dos versiones inventadas. Versión 1: «Una niña lleva agua del río a su casa por la mañana». Versión 2: «Una niña lleva agua de la fuente a su casa por la tarde». Escribe una cosa que se mantiene y dos que cambian. No digas cuál es mejor.",
           "Se mantiene: una niña lleva agua a su casa. Cambian: de dónde saca el agua (río o fuente) y la hora (mañana o tarde).",
           ["dice lo que se mantiene", "dice lo que cambia", "no jerarquiza"], ["tres frases"], ["decir que una versión es mejor"],
           "Reconoce que no jerarquizó; si dijo «mejor», volver a la frase «ambas son memoria»."),
    reinforce="Cuenta a alguien una historia corta y pídele que te cuente la suya; mira qué se parece.",
    extend="Escribe una pregunta para una persona mayor: ¿cómo cuentan esta historia en tu familia?",
)

L(
    OA8, 4,
    materials="Lápiz y hojas. Un guion de conversación para pedir permiso está escrito en el cuaderno.",
    use="Aprenderé a registrar un relato o una enseñanza pidiendo permiso y agradeciendo. Sirve para no apropiarme de lo que otras personas me cuentan.",
    prior=["Sé pedir permiso.", "Sé escuchar sin interrumpir."],
    explain=[
        "Cuando una persona mayor nos cuenta algo, podemos escribirlo, dibujarlo o grabarlo. Pero lo primero es pedir permiso. Preguntamos: ¿puedo anotar lo que usted cuenta?, ¿puedo mostrarlo en la escuela?, ¿cómo quiere que escriba su nombre?",
        "Consentimiento significa que la persona dijo que sí, sabiendo para qué usaremos lo que nos cuenta. Si dice que no, o que solo una parte, respetamos eso. Nadie está obligado a contar. Tampoco debemos guardar o mostrar algo que nos pidieron no mostrar.",
        "Después agradecemos y devolvemos lo que hicimos: le mostramos el dibujo o el texto. Decimos de quién es el relato y no lo presentamos como nuestro. Así evitamos la apropiación, que es usar algo de otra persona como si fuera mío.",
    ],
    vocab=[("consentimiento", "permiso que alguien da sabiendo para qué se usará"), ("registrar", "anotar, dibujar o grabar algo para recordarlo"), ("apropiarse", "usar algo de otra persona como si fuera mío"), ("agradecer", "decir gracias por lo que recibí"), ("devolver", "mostrar a quien me ayudó lo que hice con lo que me contó")],
    worked=[
        W("Pedir permiso", "Ana quiere anotar una historia que le contó su vecino. ¿Qué dice primero?", ["Saluda con respeto.", "Pregunta: «¿Puedo anotar lo que usted cuenta?»", "Espera su respuesta."], "«¿Puedo anotar lo que usted cuenta?»"),
        W("Respetar un no", "Un vecino dice: «Cuéntalo a tu familia, pero no lo muestres en la escuela». ¿Qué hace Ana?", ["Entiende que el permiso es solo para su familia.", "No lo muestra en la escuela.", "Le agradece de todos modos."], "No lo muestra en la escuela."),
    ],
    mistakes=[
        M("Grabar o anotar sin avisar.", "La persona no sabe qué haremos con lo que dijo.", "Pide permiso antes de registrar."),
        M("Decir «lo inventé yo» sobre una historia que me contaron.", "Es apropiarse del relato de otra persona.", "Di siempre de quién es el relato."),
    ],
    R=[
        ex("Antes de anotar lo que cuenta una persona mayor, ¿qué haces? A) Pido permiso B) Anoto sin avisar", "A", "El permiso va primero."),
        ex("Si la persona dice que no, ¿se anota igual? Sí o No.", "No", "Se respeta el no."),
        ex("Después de que alguien te cuenta algo, ¿qué dices?", "Gracias", "Agradecer es parte del respeto."),
    ],
    C=[
        ex("¿Qué es el consentimiento? A) Un permiso con información B) Un regalo", "A", "La persona dice sí sabiendo para qué."),
        ex("Verdadero o falso: puedo decir que un relato es mío si lo anoté yo.", "Falso", "El relato es de quien lo contó."),
        ex("¿Qué es apropiarse?", "Usar algo de otra persona como si fuera mío", "Esa es la definición."),
    ],
    A=[
        ex("Ordena: 1) agradezco 2) pido permiso 3) anoto lo que me cuentan. ¿Qué orden es correcto?", "2, 3, 1", "Primero el permiso, luego anotar y al final agradecer."),
        ex("Completa la frase que le dirías a una abuela con la palabra correcta: «¿Puedo ______ lo que usted cuenta y mostrarlo en mi curso?» A) anotar B) romper", "A", "Anotar es registrar por escrito, con permiso."),
        ex("Una vecina dice «puedes dibujar, pero no escribir mi nombre». ¿Qué haces?", "Dibujo y no escribo su nombre", "Se respeta lo que autorizó."),
    ],
    Z=[
        ex("Pedro grabó un canto sin permiso y lo subió a internet. ¿Qué hizo mal?", "No tenía consentimiento", "Debió pedir permiso y explicar para qué."),
        ex("¿Por qué devolvemos lo que hicimos a quien nos contó?", "Para agradecer y mostrar cómo lo usamos", "Así la persona confía en nosotros."),
    ],
    D=[
        ex("Un abuelo dice que sí a que lo anotes, pero no a que lo muestres. ¿Qué debes hacer con tu texto?", "Guardarlo y no mostrarlo", "Solo tienes permiso de anotar."),
        ex("Una niña presenta un cuento de su vecino diciendo «yo lo escribí». ¿Qué falta?", "Decir de quién es el relato", "Hay que dar crédito a quien lo contó."),
    ],
    context=[ex("Luz visita a una vecina que sabe una canción. Quiere dibujar lo que cuenta. Escribe en orden dos cosas que hace antes de dibujar.", "Saluda y pide permiso", "Primero el respeto y el permiso.")],
    selfcheck=[ex("¿Qué se pide antes de registrar?", "Permiso", "Sin permiso no se registra."), ex("Si dicen no, ¿qué haces?", "Respeto el no", "Nadie está obligado."), ex("¿De quién es el relato?", "De quien lo contó", "No se presenta como propio.")],
    task=T("Usa este guion para practicar con alguien de tu casa o con un compañero. Di: «Buenos días. ¿Puedo anotar lo que usted cuenta sobre cómo se hace una comida? ¿Puedo mostrarlo en la escuela?». Escribe la respuesta que te dieron, qué permiso te dieron y cómo agradeciste. Si no puedes preguntar a nadie, escribe lo que harías con el caso inventado de una vecina que dice «sí, pero sin mi nombre».",
           "Mi vecina dijo que sí, pero sin escribir su nombre. Anoté la receta y no puse su nombre. Le dije gracias y le mostré mi hoja.",
           ["pide permiso", "respeta lo que autorizó", "agradece y devuelve"], ["texto breve con la respuesta", "frase de agradecimiento"], ["registrar sin pedir permiso", "usar el nombre sin autorización"],
           "Valora que pidió permiso y respetó el límite; si apareció algo privado, recordar que no se comparte."),
    reinforce="Practica la frase para pedir permiso con una persona de tu casa.",
    extend="Escribe cómo agradecerías a una persona que te contó una historia y qué le devolverías.",
)
