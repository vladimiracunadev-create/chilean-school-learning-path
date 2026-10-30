"""Cuaderno del estudiante, 2.º básico Tecnología: OA 07 (búsqueda guiada y segura en internet)."""
from __future__ import annotations

from student_lessons import ex, register

OA7 = "TE02 OA 07"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": [ex(*i) for i in R], "understand": [ex(*i) for i in C], "apply": [ex(*i) for i in A], "reason": [ex(*i) for i in Z], "challenge": [ex(*i) for i in D]},
        context=[ex(*ctx)], selfcheck=[ex(*i) for i in sc], open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )




# ------------------------------------------------------------------ OA 07
# Todas las páginas, avisos y fichas de esta sección son EJEMPLOS FICTICIOS escritos para este cuaderno; no hay enlaces ni marcas.
reg(
    OA7, 1,
    materials="Un computador del colegio con navegador y una lista de sitios elegidos por tu profesor o profesora, con un adulto a tu lado. Si no hay conexión, trabaja con los ejemplos escritos de este cuaderno.",
    use="Aprenderé a entrar a internet por una ruta segura, con un adulto y solo a los sitios que mi profesor eligió. Sirve para buscar información sin riesgos.",
    prior=["Sé que internet se usa en computadores y tabletas.", "Sé que debo pedir ayuda a un adulto."],
    explain=[
        "Internet es una gran red que conecta computadores de todo el mundo. Un navegador es el programa que nos deja ver páginas de internet. Para buscar información de forma segura, entramos con un adulto y por una ruta que el profesor ya revisó, como una lista de sitios elegidos.",
        "Hay reglas de seguridad. No escribas tu nombre completo, dirección, teléfono ni el nombre de tu colegio en una página. No abras avisos que salten en la pantalla ni hagas clic en publicidad. No descargues archivos sin permiso del adulto. Si algo te asusta o no entiendes, cierra la pantalla y avisa.",
        "Las páginas de la lista del profesor son las que debes usar en la clase. Si ves un botón raro que dice «ganaste un premio», es publicidad: no lo toques. Un adulto de confianza te ayuda a decidir qué abrir. Con estas reglas, internet es una herramienta útil y segura.",
    ],
    vocab=[("internet", "red que conecta computadores de todo el mundo"), ("navegador", "programa que muestra las páginas de internet"), ("sitio", "conjunto de páginas de una institución o persona"), ("publicidad", "aviso que quiere que compres o hagas clic"), ("dato personal", "información sobre ti, como tu dirección")],
    worked=[
        ("Elegir por dónde entrar", "Tu profesora te dio una lista con tres sitios. Un aviso de la pantalla dice «Entra aquí y gana un premio». ¿Qué haces?", ["El aviso no está en la lista.", "Es publicidad.", "No hago clic y sigo con la lista."], "No hago clic y uso solo la lista de la profesora"),
        ("Proteger datos", "Una página te pide tu nombre completo y tu dirección para entrar. ¿Qué haces?", ["Son datos personales.", "No debo escribirlos.", "Aviso al adulto."], "No los escribo y aviso al adulto"),
    ],
    mistakes=[
        ("Hacer clic en un aviso que dice que ganaste un premio.", "Es publicidad y puede ser peligroso.", "No lo toques y avisa a un adulto."),
        ("Escribir tu dirección para entrar a una página.", "Es un dato personal.", "No lo escribas; pregunta al adulto."),
    ],
    R=[
        ("Un navegador muestra páginas de internet. ¿Verdadero o falso?", "Verdadero", "Esa es su función."),
        ("Para buscar en clase, ¿entras solo o con un adulto?", "Con un adulto", "Así es más seguro."),
        ("Un aviso dice «ganaste un premio». ¿Haces clic o lo ignoras?", "Lo ignoro", "Es publicidad y no se toca."),
    ],
    C=[
        ("¿Por qué se usa una lista de sitios elegidos por el profesor?", "Porque ya fueron revisados", "Son sitios más seguros."),
        ("Nombra dos datos personales que no debes escribir.", "Por ejemplo: nombre completo y dirección", "Son información sobre ti."),
        ("¿Qué haces si algo en la pantalla te asusta?", "Cierro y aviso a un adulto", "Pedir ayuda es lo correcto."),
    ],
    A=[
        ("Lista del profesor: sitio A, sitio B, sitio C. Un aviso te lleva al sitio D. ¿Entras al D?", "No", "No está en la lista."),
        ("Una página te pide tu teléfono. ¿Qué respondes?", "No lo escribo", "Es un dato personal."),
        ("Un archivo empieza a descargarse solo. ¿Qué haces?", "Aviso al adulto y no lo abro", "No se descarga sin permiso."),
    ],
    Z=[
        ("Dani dice: «Si un aviso es lindo, es seguro». ¿Tiene razón? Explica.", "No, porque un aviso lindo puede ser publicidad peligrosa", "El aspecto no asegura nada."),
        ("Un compañero escribió su dirección para participar en un concurso. ¿Qué le dices?", "Que no se escriben datos personales y que avise a un adulto", "Se protege la privacidad."),
    ],
    D=[
        ("Escribe tres reglas de seguridad para buscar en internet en la sala.", "Ir con un adulto; usar la lista del profesor; no escribir datos personales", "Tres reglas de esta clase."),
        ("Tienes 4 sitios en la lista y ya visitaste 1. ¿Cuántos faltan?", "3", "4 menos 1 es 3."),
    ],
    ctx=("Pía está en la sala con su profesora. Abre el sitio de la lista y aparece una ventana que dice «Haz clic para ver videos gratis». ¿Qué hace?", "No hace clic y avisa a su profesora", "Es publicidad y debe avisar."),
    sc=[
        ("¿Se entra con un adulto?", "Sí", "Es una regla de seguridad."),
        ("¿Se escribe la dirección de la casa?", "No", "Es un dato personal."),
        ("¿Se hace clic en los avisos?", "No", "Pueden ser peligrosos."),
    ],
    open_task=(
        "Lee estos cinco casos y escribe qué haces en cada uno. Caso 1: un aviso dice «ganaste un premio». Caso 2: una página te pide tu dirección. Caso 3: el profesor te da un sitio de la lista. Caso 4: se abre una ventana que no pediste. Caso 5: algo te asusta. Escribe una regla de seguridad que apliques en cada caso.",
        "Caso 1: ignoro el aviso. Caso 2: no escribo mi dirección. Caso 3: entro con el adulto. Caso 4: la cierro y aviso. Caso 5: cierro y pido ayuda.",
        ["responde los cinco casos", "no entrega datos personales", "usa solo la lista del profesor", "pide ayuda cuando corresponde"],
        ["hoja con cinco respuestas"],
        ["hacer clic en avisos", "escribir datos personales"],
        "Pregunta: «¿qué regla usaste?». Si respondió que haría clic, repasa por qué es riesgoso.",
    ),
    reinforce="Dile a un familiar dos reglas de seguridad para internet.",
    extend="Escribe un afiche con cuatro reglas de internet para tu sala.",
)

reg(
    OA7, 2,
    materials="Las tres fichas de fuentes ficticias de este cuaderno y un lápiz. Si hay conexión, el profesor puede mostrar un sitio real de su lista.",
    use="Aprenderé a leer la fuente de una página: quién la hizo, para qué y de cuándo es. Sirve para saber si puedo confiar en lo que dice.",
    prior=["Sé las reglas de seguridad en internet.", "Sé leer un texto corto."],
    explain=[
        "La fuente es el lugar de donde viene la información. Antes de usar un dato, hay que mirar la fuente. Pregunta tres cosas: ¿quién la hizo?, ¿para qué la hizo? y ¿de cuándo es? Una fuente confiable dice quién la escribió.",
        "Suele ser más confiable un sitio de una institución conocida, como un museo, una escuela, una universidad o un organismo público, que una página sin autor. También importa la fecha: una información muy antigua puede haber cambiado. Una página que quiere venderte algo busca convencerte.",
        "Ten cuidado con las páginas que no dicen quién las hizo, que están llenas de avisos o que prometen cosas increíbles. Si dudas, pregunta a tu profesor. Y recuerda: que algo esté en internet no lo hace verdadero. Estas tres preguntas son una ayuda sencilla, no una garantía: también una fuente conocida puede equivocarse, y por eso un adulto te ayuda a confirmar.",
    ],
    vocab=[("fuente", "lugar de donde viene la información"), ("autor", "quien escribió la información"), ("institución", "organización como un museo, una escuela o un organismo público"), ("fecha", "cuándo se escribió"), ("confiable", "que merece confianza")],
    worked=[
        ("Revisar una fuente", "Ficha 1 (ejemplo ficticio): «Museo de las Aves del Sur. Texto escrito por el equipo de científicas del museo. Año 2024». ¿Es confiable?", ["Dice quién: un museo y sus científicas.", "Dice la fecha: 2024.", "Es una institución."], "Sí, parece confiable"),
        ("Dudar de una fuente", "Ficha 2 (ejemplo ficticio): «Página sin autor, llena de avisos, que dice que un jugo cura todo». ¿Es confiable?", ["No dice quién la hizo.", "Tiene muchos avisos.", "Promete cosas increíbles."], "No, no es confiable"),
    ],
    mistakes=[
        ("Creer algo solo porque está en internet.", "Cualquiera puede escribir en internet.", "Revisa quién lo hizo, para qué y de cuándo es."),
        ("No mirar la fecha.", "La información puede ser antigua.", "Busca la fecha y compárala con hoy."),
    ],
    R=[
        ("Una fuente dice de dónde viene la información. ¿Verdadero o falso?", "Verdadero", "Esa es su definición."),
        ("Un museo es una institución. ¿Sí o no?", "Sí", "Es una organización conocida."),
        ("¿Una página que no dice quién la escribió es confiable?", "No", "No se sabe quién responde."),
    ],
    C=[
        ("Nombra las tres preguntas para revisar una fuente.", "¿Quién la hizo? ¿Para qué? ¿De cuándo es?", "Son las tres que enseña la clase."),
        ("¿Por qué importa la fecha?", "Porque la información puede estar desactualizada", "Los datos cambian."),
        ("¿Una página con muchos avisos y promesas increíbles es confiable?", "No", "Quiere convencer o vender."),
    ],
    A=[
        ("Ficha 3 (ejemplo ficticio): «Escuela del Valle, curso de 3° básico, trabajo sobre las plantas, año 2023». ¿Quién la hizo?", "El curso de 3° básico de la Escuela del Valle", "La ficha dice el autor."),
        ("Una página dice «Año 1990» y habla de computadores modernos. ¿Qué dudas?", "Si la información está actualizada", "La fecha es muy antigua."),
        ("De dos fuentes, A «Museo de las Aves del Sur, 2024» y B «Sin autor, sin fecha», ¿cuál usas?", "A", "Dice quién la hizo y de cuándo es."),
    ],
    Z=[
        ("Rafa dice: «Está en internet, así que es verdad». ¿Qué le respondes?", "Que cualquiera puede escribir en internet y hay que revisar la fuente", "Internet no garantiza que algo sea verdad."),
        ("Una página vende un producto y dice que es el mejor del mundo. ¿Para qué la hicieron?", "Para vender", "Su propósito es comercial."),
    ],
    D=[
        ("Compara dos fuentes: A «Museo, 2024, equipo del museo» y B «Blog sin autor, 2010». Escribe cuál es más confiable y dos razones.", "A, porque dice quién la hizo y es más reciente", "Autor claro y fecha."),
        ("La fuente A es de 2024 y la B de 2010. ¿Cuántos años de diferencia hay?", "14", "2024 menos 2010 es 14."),
    ],
    ctx=("Mati abre una página de su lista que dice (ejemplo ficticio) «Museo de las Rocas, equipo de educadoras, 2025». Otra página sin nombre le muestra muchos avisos. ¿Cuál usa y qué mira primero?", "Usa la del museo; mira quién la hizo y la fecha", "Es una institución con autor y fecha."),
    sc=[
        ("¿Se revisa quién hizo la información?", "Sí", "Es la primera pregunta."),
        ("¿La fecha importa?", "Sí", "Los datos cambian."),
        ("¿Todo lo de internet es verdad?", "No", "Hay que revisar la fuente."),
    ],
    open_task=(
        "Lee estas tres fichas ficticias. Ficha A: «Museo de las Aves del Sur, escrito por científicas del museo, 2024». Ficha B: «Página sin autor, muchos avisos, promete curar todo con un jugo». Ficha C: «Escuela del Valle, trabajo de 3° básico sobre las plantas, 2023». Para cada una escribe quién la hizo, para qué y si la usarías con una razón.",
        "A: la hizo un museo, para informar, sí la usaría. B: sin autor, para vender, no la usaría. C: la hizo un curso, para aprender, la usaría con ayuda del profesor.",
        ["responde quién, para qué y la fecha", "decide con una razón", "no confía solo porque está en internet"],
        ["tabla con tres fichas"],
        ["creer todo", "no mirar la fecha"],
        "Pregunta: «¿cómo sabes quién la hizo?». Si dice que no importa, revisa la regla de las tres preguntas.",
    ),
    reinforce="Mira un libro de tu casa y busca quién lo escribió y en qué año.",
    extend="Escribe una pregunta más para revisar una fuente.",
)

reg(
    OA7, 3,
    materials="La página ficticia de este cuaderno y un lápiz. Si hay conexión, el profesor puede abrir un sitio real de su lista.",
    use="Aprenderé a encontrar un dato dentro de una página usando títulos, subtítulos y la búsqueda de la palabra. Sirve para no leer todo cuando busco algo.",
    prior=["Sé revisar una fuente.", "Sé leer títulos y subtítulos."],
    explain=[
        "Una página puede ser larga. No siempre hay que leerla toda. Mira los títulos y subtítulos: dicen de qué trata cada parte. Si buscas un dato, busca el subtítulo que se parece a lo que quieres saber.",
        "Muchos navegadores tienen una opción para buscar una palabra en la página. Escribes la palabra y el navegador marca dónde aparece. Esa opción se encuentra en el menú del navegador, bajo un nombre como «Buscar en la página» (puede variar). Así llegas rápido al lugar.",
        "Cuando encuentres el lugar, lee con calma el párrafo completo. Verifica que responde tu pregunta. A veces la palabra aparece en más de un lugar: revisa todos antes de decidir. Anota la respuesta y el subtítulo donde la hallaste.",
    ],
    vocab=[("título", "nombre grande de la página"), ("subtítulo", "nombre de una parte de la página"), ("buscar en la página", "opción que marca una palabra en el texto"), ("párrafo", "grupo de oraciones sobre una idea"), ("dato", "información concreta")],
    worked=[
        ("Elegir el subtítulo", "Página ficticia «Las abejas», con subtítulos: «Dónde viven», «Qué comen», «La miel». Quieres saber qué comen. ¿Qué subtítulo lees?", ["Busco una palabra parecida.", "«Qué comen» habla de comida.", "Leo ese subtítulo."], "«Qué comen»"),
        ("Buscar una palabra", "En la misma página quieres encontrar «colmena». ¿Qué haces?", ["Abro la opción Buscar en la página.", "Escribo colmena.", "Voy al lugar que se marca."], "Buscar la palabra colmena con la opción del navegador"),
    ],
    mistakes=[
        ("Leer toda la página para encontrar un dato.", "Se pierde tiempo.", "Usa títulos, subtítulos y la búsqueda de la palabra."),
        ("Quedarse con la primera vez que aparece la palabra.", "Puede no responder tu pregunta.", "Revisa todos los lugares marcados."),
    ],
    R=[
        ("Un subtítulo dice de qué trata una parte. ¿Verdadero o falso?", "Verdadero", "Esa es su función."),
        ("Para buscar una palabra en la página, ¿se usa Buscar en la página o Descargar?", "Buscar en la página", "Marca la palabra."),
        ("¿Se lee todo el texto siempre?", "No", "Se puede buscar la parte que sirve."),
    ],
    C=[
        ("¿Para qué sirven los subtítulos al buscar un dato?", "Para ubicar la parte que habla de eso", "Dicen de qué trata cada parte."),
        ("¿Qué hace la opción Buscar en la página?", "Marca dónde aparece una palabra", "Te lleva al lugar."),
        ("¿Por qué hay que leer el párrafo completo?", "Para comprobar que responde tu pregunta", "Una palabra sola puede confundir."),
    ],
    A=[
        ("Página ficticia «Las ballenas», subtítulos: «Dónde viven», «Cuánto miden», «Qué comen». Quieres saber cuánto miden. ¿Qué subtítulo lees?", "Cuánto miden", "Habla del tamaño."),
        ("En la misma página buscas la palabra «plancton». ¿Qué escribes en la opción Buscar en la página?", "plancton", "Es la palabra que quieres encontrar."),
        ("La palabra «agua» aparece en 3 lugares. ¿Cuántos lugares revisas antes de decidir?", "3", "Se revisan todos los lugares."),
    ],
    Z=[
        ("Ana buscó «hielo» y leyó solo la primera vez que aparece, en el subtítulo «Qué comen». ¿Qué debió hacer?", "Revisar los otros lugares donde aparece", "Puede haber más información."),
        ("Para saber dónde viven los pingüinos, ¿es mejor leer todo o buscar el subtítulo «Dónde viven»? Explica.", "Buscar el subtítulo, porque ahorra tiempo", "Ese subtítulo trata del tema."),
    ],
    D=[
        ("Página ficticia «El volcán», con subtítulos: «Qué es», «Partes del volcán», «Qué hacer si hay un temblor». Quieres saber cómo se llama la abertura de arriba. ¿Qué subtítulo lees primero y qué palabra buscas: «abertura» o «temblor»?", "Partes del volcán; la palabra abertura", "La abertura de arriba es una parte del volcán."),
        ("Una página tiene 8 párrafos. Solo 2 hablan de tu tema. ¿Cuántos no necesitas leer?", "6", "8 menos 2 es 6."),
    ],
    ctx=("Rita busca en una página de su lista cuántos años vive una tortuga. La página tiene los subtítulos «Dónde viven», «Cuántos años viven» y «Qué comen». ¿Qué subtítulo lee y qué palabra puede buscar?", "«Cuántos años viven»; la palabra años", "Ubica el dato rápido."),
    sc=[
        ("¿Los subtítulos ayudan a ubicar un tema?", "Sí", "Dicen de qué trata cada parte."),
        ("¿Se puede buscar una palabra?", "Sí", "Con Buscar en la página."),
        ("¿Se lee el párrafo completo?", "Sí", "Así se entiende bien."),
    ],
    open_task=(
        "Usa esta página ficticia llamada «Las abejas». Subtítulos: Dónde viven (Las abejas viven en colmenas.), Qué comen (Las abejas toman néctar de las flores.), La miel (Con el néctar las abejas hacen miel.). Responde: 1) ¿Qué subtítulo lees para saber qué comen? 2) ¿Qué palabra buscarías para saber de la miel? 3) ¿Qué comen las abejas?",
        "1) Qué comen. 2) miel. 3) Las abejas toman néctar de las flores.",
        ["elige el subtítulo correcto", "propone la palabra a buscar", "responde con el dato"],
        ["tres respuestas escritas"],
        ["leer todo sin ubicar", "no revisar el párrafo"],
        "Pregunta: «¿cómo supiste dónde mirar?». Si leyó todo, muestra cómo usar los subtítulos.",
    ),
    reinforce="Elige un libro de tu casa y busca un tema usando el índice.",
    extend="Escribe dos preguntas y di qué subtítulo usarías para cada una.",
)

reg(
    OA7, 4,
    materials="El texto ficticio de este cuaderno, una hoja y un lápiz. No copies lo que lees: úsalo para decir con tus palabras.",
    use="Aprenderé a sacar información de una página y a decirla con mis propias palabras, anotando de dónde viene. Sirve para aprender y para no copiar.",
    prior=["Sé ubicar un dato en una página.", "Sé revisar una fuente."],
    explain=[
        "Extraer información es sacar de una página las ideas que sirven. Una forma segura es leer un párrafo, taparlo con la mano y decir con tus palabras lo que entendiste. Si copias, no sabes si entendiste y puedes tomar el trabajo de otra persona.",
        "Para decirlo con tus palabras, busca la idea principal. Es lo más importante que dice el párrafo. Luego cuéntala con palabras simples. Puedes usar sinónimos, que son palabras con el mismo significado, y frases más cortas.",
        "Siempre anota la fuente: el nombre del sitio y el título de la página. Así quien lea tu trabajo sabe de dónde viene. Y cuida tu privacidad: no pongas datos personales en lo que escribes. Una buena ficha tiene tema, idea con tus palabras y fuente.",
    ],
    vocab=[("extraer", "sacar las ideas que sirven"), ("idea principal", "lo más importante que dice un párrafo"), ("con tus palabras", "sin copiar, dicho de otra forma"), ("sinónimo", "palabra con significado parecido"), ("anotar la fuente", "escribir de dónde viene la información")],
    worked=[
        ("Decir con otras palabras", "Texto ficticio: «Las abejas viven en colmenas y trabajan en grupo». Dilo con tus palabras.", ["La idea principal: viven juntas y trabajan juntas.", "Uso palabras simples.", "No copio la frase."], "Las abejas viven juntas en un lugar y hacen su trabajo entre todas"),
        ("Anotar la fuente", "Sacaste la información de la página «Las abejas» del sitio ficticio «Museo de la Naturaleza». ¿Qué anotas?", ["El nombre del sitio.", "El título de la página.", "Los escribo bajo mi ficha."], "Museo de la Naturaleza, página «Las abejas»"),
    ],
    mistakes=[
        ("Copiar el párrafo tal cual.", "No muestra que entendiste y es tomar el texto de otro.", "Léelo, ciérralo y cuéntalo con tus palabras."),
        ("No anotar la fuente.", "No se sabe de dónde salió.", "Escribe el sitio y el título de la página."),
    ],
    R=[
        ("¿«Con tus palabras» significa copiar o decir de otra forma?", "Decir de otra forma", "Así muestras que entendiste."),
        ("La idea principal es lo más importante. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ("¿Se anota la fuente al final?", "Sí", "Así se sabe de dónde viene."),
    ],
    C=[
        ("¿Por qué no conviene copiar un párrafo?", "Porque no muestra que entendiste", "Copiar no es entender."),
        ("¿Qué datos lleva la fuente?", "El nombre del sitio y el título de la página", "Con eso se ubica."),
        ("En Tecnología: ¿Qué es un sinónimo?", "Una palabra con significado parecido", "Ayuda a decirlo con otras palabras."),
    ],
    A=[
        ("Texto ficticio: «La miel se hace con el néctar de las flores». Elige la idea principal: la miel viene del néctar, o las flores son rojas.", "La miel viene del néctar", "Es lo que dice el texto."),
        ("Texto ficticio: «Las ballenas son mamíferos que viven en el mar». Di con otras palabras dónde viven.", "Viven en el océano, en el agua salada", "Es el dato del texto dicho de otra forma."),
        ("Usaste la página «Las ballenas» del sitio ficticio «Museo del Mar». Escribe la fuente.", "Museo del Mar, página «Las ballenas»", "Sitio y título."),
    ],
    Z=[
        ("Eli copió un párrafo entero y no sabe qué significa. ¿Qué debe hacer?", "Leerlo de nuevo, cerrarlo y contarlo con sus palabras", "Así comprueba que entendió."),
        ("Dos niños escriben lo mismo palabra por palabra. ¿Qué puede haber pasado?", "Copiaron del mismo texto", "No lo dijeron con palabras propias."),
    ],
    D=[
        ("Texto ficticio: «El zorro vive en el bosque y de noche busca comida». Escribe la idea con tus palabras y la fuente (sitio «Reserva Verde», página «El zorro»).", "El zorro busca su comida de noche en el bosque. Fuente: Reserva Verde, página «El zorro»", "Palabras propias y fuente."),
        ("Una ficha tiene 3 partes: tema, idea y fuente. Tienes tema e idea. ¿Cuántas partes faltan?", "1", "3 menos 2 es 1."),
    ],
    ctx=("Lía usó la página «Los pingüinos» del sitio ficticio «Museo Polar». El texto dice: «Los pingüinos no vuelan, pero nadan muy bien». Escribe su ficha con tema, idea con sus palabras y fuente.", "Tema: pingüinos. Idea: no vuelan, pero son buenos nadadores. Fuente: Museo Polar, página «Los pingüinos»", "Tres partes con palabras propias."),
    sc=[
        ("¿Se escribe con tus palabras?", "Sí", "Así se aprende."),
        ("¿Se anota la fuente?", "Sí", "Para saber de dónde vino."),
        ("¿Se copia el párrafo?", "No", "Debe decirse de otro modo."),
    ],
    open_task=(
        "Lee este texto ficticio de la página «Las abejas» del sitio «Museo de la Naturaleza»: «Las abejas viven en colmenas. Salen a buscar néctar de las flores. Con ese néctar hacen miel. Trabajan en grupo para cuidar la colmena.». Escribe tu ficha con tema, dos ideas con tus palabras y la fuente. No copies frases completas.",
        "Tema: abejas. Ideas: viven juntas en un hogar y cuidan su hogar entre todas; fabrican miel con lo que sacan de las flores. Fuente: Museo de la Naturaleza, página «Las abejas».",
        ["escribe el tema", "da dos ideas con palabras propias", "anota la fuente", "no copia frases completas"],
        ["ficha escrita"],
        ["copiar el texto", "olvidar la fuente"],
        "Pregunta: «¿cómo dirías esto sin mirar el texto?». Si copió, pídele cerrar el texto y contarlo.",
    ),
    reinforce="Cuéntale a alguien algo que leíste hoy con tus palabras.",
    extend="Haz una ficha de otro tema con dos ideas y la fuente.",
)
