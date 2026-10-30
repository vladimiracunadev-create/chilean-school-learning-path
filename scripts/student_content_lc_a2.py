"""Student material for 1.º básico Lengua y Cultura de los Pueblos Originarios Ancestrales, OA 09 (territorio, historia e identidad) y OA 10 (ser humano y naturaleza)."""
from __future__ import annotations

from student_content_lc_a1 import F_AYM, F_DIA, F_KAW, F_LICK, F_MAP, F_RN, L, M, T, W
from student_lessons import ex

OA9, OA10 = "LC01 OA 09", "LC01 OA 10"

ZONAS = "Tabla de ubicación (general): pueblo aymara, norte; pueblo lickanantay, norte; pueblo diaguita, Norte Chico; pueblo mapuche, centro y sur; pueblo rapa nui, isla en el Pacífico; pueblo kawésqar, canales del sur."

# ============================================================ OA 09 · Territorio, historia e identidad
L(
    OA9, 1,
    materials="Lápiz y hojas. La tabla de ubicación está escrita en este cuaderno, con datos generales.",
    use="Aprenderé a ubicar de forma general dónde viven algunos pueblos originarios de Chile usando una fuente. Sirve para no confundir ni mezclar los pueblos.",
    prior=["Sé que Chile es un país largo y angosto.", "Sé distinguir norte, centro y sur."],
    explain=[
        "En Chile viven varios pueblos originarios. Cada uno tiene su propio territorio, su historia y su cultura. Algunos viven en el norte, otros en el centro y el sur, otros en islas y otros en los canales del extremo sur.",
        "Para ubicar a un pueblo usamos una fuente: una ficha, un mapa de un libro confiable o la palabra del educador tradicional. Ubicamos de forma general, por zona, sin marcar casas ni lugares sagrados. Decimos, por ejemplo, que el pueblo aymara vive en el norte.",
        "Un pueblo puede vivir en más de un lugar y puede haber personas de un mismo pueblo en distintas zonas, incluso en ciudades. Por eso hablamos de zonas generales y evitamos decir «solo viven allí». Si dudamos, preguntamos y no marcamos en el mapa.",
    ],
    vocab=[("pueblo originario", "pueblo que ya vivía en estas tierras antes de la llegada de los españoles"), ("zona", "parte de un territorio, como norte o sur"), ("ubicar", "decir dónde está algo"), ("fuente", "ficha, libro o persona de donde viene el dato"), ("general", "sin entrar en detalles privados")],
    worked=[
        W("Ubicar con la tabla", ZONAS + " ¿En qué zona vive el pueblo mapuche?", ["Busco «mapuche» en la tabla.", "Leo la zona que dice la tabla.", "Respondo con la zona y con la fuente."], "En el centro y sur, según la tabla."),
        W("Cuando falta el dato", "La tabla no dice dónde vive un pueblo que Ana nombró. ¿Qué hace?", ["No lo ubica adivinando.", "Pregunta a una fuente: libro, profesor o educador tradicional.", "Anota que falta confirmar."], "Pregunta y anota que falta confirmar."),
    ],
    mistakes=[
        M("Ubicar un pueblo sin mirar la fuente.", "Puedes equivocarte de zona.", "Usa la tabla o una fuente confiable."),
        M("Decir que un pueblo solo vive en un lugar.", "Hay personas de cada pueblo en varios lugares.", "Habla de zonas generales y no de «solo»."),
    ],
    R=[
        ex(ZONAS + " ¿En qué zona vive el pueblo aymara?", "En el norte", "La tabla dice norte para el pueblo aymara."),
        ex(ZONAS + " ¿Qué pueblo vive en una isla del Pacífico?", "El pueblo rapa nui", "La tabla lo ubica en una isla."),
        ex(ZONAS + " ¿Qué pueblo vive en los canales del sur?", "El pueblo kawésqar", "Es el que la tabla ubica en los canales."),
    ],
    C=[
        ex("¿Qué usamos para ubicar un pueblo? A) una fuente confiable B) lo que me parece", "A", "Sin fuente podemos equivocarnos."),
        ex("Verdadero o falso: cada pueblo originario tiene exactamente el mismo territorio.", "Falso", "Cada pueblo tiene su propio territorio."),
        ex("Ubicar de forma general, ¿es marcar la casa de una familia? Sí o No.", "No", "Se ubica por zona y no por casas."),
    ],
    A=[
        ex("Une pueblo y zona. 1) diaguita 2) lickanantay 3) mapuche. a) norte b) Norte Chico c) centro y sur", "1-b, 2-a, 3-c", "Los datos están en la tabla de ubicación."),
        ex("Ficha: «" + F_DIA + "» ¿En qué zona vive el pueblo diaguita según la ficha?", "En el Norte Chico", "La ficha dice valles del Norte Chico."),
        ex("Ordena de norte a sur usando la tabla: mapuche, aymara, kawésqar.", "aymara, mapuche, kawésqar", "El norte viene primero, luego el centro y sur y al final los canales del sur."),
    ],
    Z=[
        ex("Camila dice que el pueblo mapuche vive en el norte. ¿Qué le muestras?", "La tabla: el pueblo mapuche vive en el centro y sur", "La fuente corrige el dato."),
        ex("Pedro dice que nadie del pueblo aymara vive en la ciudad. ¿Es seguro? Sí o No.", "No", "Hay personas de cada pueblo en muchos lugares."),
    ],
    D=[
        ex("Un mapa sin título tiene un círculo en un valle. ¿Puedes afirmar de qué pueblo es? Sí o No.", "No", "Sin fuente no se sabe."),
        ex("La tabla no tiene al pueblo que menciona Luz. ¿Qué le sugieres?", "Preguntar a una fuente confiable", "No se adivina la ubicación."),
    ],
    context=[ex("Tu curso arma un cartel de Chile con tres zonas: norte, centro y sur. Pone al pueblo aymara en el norte. ¿Dónde pone al pueblo kawésqar según la tabla: " + ZONAS + "?", "En los canales del sur", "La tabla lo ubica en el sur, en los canales.")],
    selfcheck=[ex("¿Qué usas para ubicar un pueblo?", "Una fuente", "Así se evita equivocarse."), ex("¿Dónde vive el pueblo rapa nui según la tabla?", "En una isla del Pacífico", "Así lo dice la tabla."), ex("¿Se marcan lugares sagrados en un mapa de clase?", "No", "Se ubica solo en forma general.")],
    task=T("Dibuja un Chile largo y angosto. Escribe en la zona correcta los nombres de tres pueblos de la tabla de ubicación (por ejemplo aymara, mapuche y kawésqar). Escribe abajo «Fuente: tabla del cuaderno». No marques casas ni lugares sagrados.",
           "Escribí aymara arriba (norte), mapuche en el medio (centro y sur) y kawésqar abajo (canales). Fuente: tabla del cuaderno.",
           ["ubica cada pueblo según la tabla", "cita la fuente", "no marca lugares delicados"], ["dibujo de Chile", "tres nombres", "fuente"], ["ubicar sin fuente", "marcar un punto exacto"],
           "Revisa cada nombre contra la tabla; si faltó la fuente, volver a pedirla."),
    reinforce="Pide a alguien que te lea la tabla y señala la zona de cada pueblo.",
    extend="Elige un pueblo de la tabla y escribe una pregunta sobre su historia para el educador tradicional.",
)

L(
    OA9, 2,
    materials="Lápiz y hojas. Una línea del tiempo muy simple está escrita en el cuaderno.",
    use="Aprenderé que los pueblos originarios tienen una historia larga y que siguen vivos hoy. Sirve para hablar de ellos en pasado y en presente.",
    prior=["Sé qué es el pasado y qué es el presente.", "Sé que mis abuelos vivieron antes que yo."],
    explain=[
        "Los pueblos originarios ya vivían en lo que hoy es Chile mucho antes de que llegaran los españoles. Tienen una historia muy larga, que cuentan los mayores, que se estudia en libros y que se guarda en el territorio.",
        "Esa historia no terminó. Hoy los pueblos originarios siguen viviendo, trabajando, estudiando y cuidando su cultura. Por eso es un error hablar de ellos solo como si fueran del pasado. Su historia es una historia viva.",
        "Para contar su historia usamos fuentes: relatos de la comunidad con permiso, libros confiables y los educadores tradicionales. Cuando hablamos del pasado, no olvidamos el presente: decimos qué pasaba antes y qué pasa hoy.",
    ],
    vocab=[("pasado", "lo que ocurrió antes"), ("presente", "lo que ocurre hoy"), ("historia viva", "historia que sigue ocurriendo y sigue siendo contada"), ("línea del tiempo", "dibujo que ordena sucesos de antes a después"), ("antes de", "en un tiempo anterior a otra cosa")],
    worked=[
        W("Pasado y presente", "«El pueblo aymara criaba llamas y hoy muchas familias aún las crían.» ¿Qué parte es pasado y cuál presente?", ["«Criaba» es pasado.", "«Aún las crían» es presente.", "La práctica continúa."], "Pasado: criaba. Presente: aún las crían."),
        W("Ordenar una línea", "Ordena: hoy se estudia la historia; los pueblos ya vivían aquí; llegaron los españoles. ¿Cuál es el orden?", ["Primero ya vivían aquí.", "Luego llegaron los españoles.", "Al final, hoy se sigue contando la historia."], "1) ya vivían aquí, 2) llegaron los españoles, 3) hoy se sigue contando."),
    ],
    mistakes=[
        M("Hablar de los pueblos originarios solo en pasado.", "Siguen viviendo hoy.", "Usa también el presente: «viven», «cuidan», «enseñan»."),
        M("Decir que su historia empezó con los españoles.", "Ya vivían aquí mucho antes.", "Parte contando que ya vivían aquí."),
    ],
    R=[
        ex("¿Los pueblos originarios ya vivían aquí antes de que llegaran los españoles? Sí o No.", "Sí", "Su historia es anterior."),
        ex("¿Los pueblos originarios existen hoy? Sí o No.", "Sí", "Siguen viviendo y cuidando su cultura."),
        ex("«Hoy» habla del pasado o del presente.", "Del presente", "Hoy es el momento actual."),
    ],
    C=[
        ex("Verdadero o falso: la historia de un pueblo originario terminó hace mucho.", "Falso", "Es una historia viva."),
        ex("¿Cuál frase habla del presente? A) «Los mayores contaban» B) «Hoy los niños aprenden»", "B", "«Hoy» y «aprenden» están en presente."),
        ex("¿De dónde sacamos la historia? A) de fuentes confiables B) de lo que imaginamos", "A", "Se cuenta con fuentes."),
    ],
    A=[
        ex("Clasifica cada frase como PASADO o PRESENTE: a) «Navegaban en canoas» b) «Hoy cuidan su cultura» c) «Vivían junto al mar».", "a) pasado, b) presente, c) pasado", "Navegaban y vivían están en pasado; cuidan, en presente."),
        ex("Ordena: 1) llegaron los españoles 2) hoy los pueblos siguen vivos 3) ya vivían aquí los pueblos originarios.", "3, 1, 2", "Primero ya vivían aquí, luego llegaron y hoy siguen vivos."),
        ex("Escribe una frase que una el pasado y el presente de un pueblo, usando «antes… y hoy…».", "Respuesta aceptable: «Antes criaban llamas y hoy las siguen criando»", "La frase une antes y hoy."),
    ],
    Z=[
        ex("Tomás dice: «Los pueblos originarios ya no existen». ¿Qué error tiene?", "Olvida que siguen vivos hoy", "Viven y cuidan su cultura."),
        ex("¿Por qué conviene decir «antes y hoy» al hablar de un pueblo?", "Porque su historia continúa", "Une el pasado con el presente."),
    ],
    D=[
        ex("Una ficha dice: «El pueblo kawésqar navegaba en canoas». ¿Basta para decir que hoy ya no existe? Sí o No.", "No", "La ficha habla de un tiempo; no dice que haya desaparecido."),
        ex("Dos fuentes dan datos distintos de una fecha. ¿Qué haces?", "Pregunto al educador o busco otra fuente", "No se elige sin comprobar."),
    ],
    context=[ex("Una niña dice: «Mi vecino sabe tejer como antes y hoy enseña a los niños». ¿Qué palabra señala el presente?", "Hoy", "«Hoy» marca el presente.")],
    selfcheck=[ex("¿Los pueblos originarios solo existieron antes?", "No", "Viven hoy, siguen presentes."), ex("¿Qué es una historia viva?", "Una historia que sigue ocurriendo y contándose", "Continúa en el presente."), ex("¿Qué palabra usas para el presente?", "Hoy", "Marca el tiempo actual.")],
    task=T("Escribe dos frases sobre el pueblo aymara usando esta información de la ficha: «" + F_AYM + "». Una frase debe empezar con «Antes…» y otra con «Hoy…». Si no sabes lo que pasa hoy, escribe en cambio una pregunta para preguntar al educador tradicional.",
           "Antes, el pueblo aymara criaba llamas y alpacas en el altiplano. Hoy quiero preguntar al educador cómo las cuidan las familias.",
           ["usa pasado y presente", "se apoya en la ficha", "no inventa datos del presente"], ["dos frases o una frase y una pregunta"], ["hablar solo en pasado", "inventar un dato actual"],
           "Reconoce que une pasado y presente; si inventó un dato actual, transformarlo en pregunta."),
    reinforce="Dibuja una línea con «antes» a la izquierda y «hoy» a la derecha y pega una palabra en cada lado.",
    extend="Escribe una pregunta sobre lo que hacen hoy los niños de un pueblo originario, para el educador tradicional.",
)

L(
    OA9, 3,
    materials="Lápiz y hojas. Los textos para comparar están escritos en el cuaderno.",
    use="Aprenderé que dentro de un mismo pueblo hay personas, familias y lugares distintos. Sirve para no dar una descripción única de nadie.",
    prior=["Sé que cada persona es distinta.", "Sé que hay familias de muchas maneras."],
    explain=[
        "Un pueblo originario no es igual en todas partes. Dentro de un mismo pueblo hay familias que viven en el campo y otras en la ciudad; unas se dedican a un trabajo y otras a otro; unas hablan más una lengua y otras menos. Hay muchas maneras de ser de un pueblo.",
        "Por eso evitamos la descripción única. No decimos «todas las personas del pueblo hacen esto» ni «todas visten así». Preferimos decir «algunas personas», «en algunas comunidades» o «según esta fuente».",
        "La identidad es lo que una persona siente que es y a qué pueblo y comunidad siente que pertenece. Nadie decide por otro cómo debe ser. Respetamos cómo cada persona vive y cuenta su identidad.",
    ],
    vocab=[("identidad", "lo que una persona siente que es y a qué grupo pertenece"), ("diversidad", "que hay muchas maneras distintas"), ("generalizar", "decir que todos son iguales"), ("algunas", "no todas; solo una parte"), ("comunidad", "grupo de personas que viven y trabajan juntas")],
    worked=[
        W("Cambiar «todos» por «algunos»", "Frase: «Todas las personas del pueblo mapuche viven en el campo». ¿Cómo la corriges?", ["Hay personas del pueblo mapuche en ciudades.", "No todas viven en el campo.", "Escribo: «Algunas personas viven en el campo y otras en la ciudad»."], "«Algunas personas viven en el campo y otras en la ciudad.»"),
        W("Respetar la identidad", "Un niño dice que su vecina «no es suficientemente indígena» porque vive en la ciudad. ¿Qué le dices?", ["Cada persona vive su identidad a su manera.", "Vivir en la ciudad no quita la pertenencia.", "No juzgo a otras personas."], "Que no se juzga la identidad de otra persona."),
    ],
    mistakes=[
        M("Decir «todos son iguales» al hablar de un pueblo.", "Dentro de un pueblo hay mucha diversidad.", "Usa «algunos» o «según esta fuente»."),
        M("Decidir si alguien «es o no es» de un pueblo.", "La identidad la siente cada persona.", "Respeta cómo cada uno se presenta."),
    ],
    R=[
        ex("¿Cuál frase generaliza? A) «Todos hacen lo mismo» B) «Algunos hacen esto»", "A", "«Todos» dice que son iguales."),
        ex("Dentro de un pueblo, ¿todas las personas viven igual? Sí o No.", "No", "Hay muchas maneras de vivir."),
        ex("¿Qué palabra evita la generalización? A) todos B) algunas", "B", "«Algunas» deja ver la diversidad."),
    ],
    C=[
        ex("Verdadero o falso: una persona puede vivir en la ciudad y sentirse parte de su pueblo.", "Verdadero", "La identidad no depende del lugar."),
        ex("¿Qué es la identidad?", "Lo que una persona siente que es y a qué grupo pertenece", "Es algo personal y también de comunidad."),
        ex("¿Qué frase usarías para describir a un pueblo con respeto? A) «Según esta fuente…» B) «Todos son así…»", "A", "Cita la fuente y no generaliza."),
    ],
    A=[
        ex("Corrige con «algunas»: «Todas las familias del pueblo aymara crían llamas».", "Algunas familias del pueblo aymara crían llamas", "Se cambia «todas» por «algunas»."),
        ex("Marca las frases respetuosas: a) «Algunas personas del pueblo viven en la ciudad» b) «Nadie del pueblo vive en la ciudad» c) «Según la ficha, el pueblo vive en el norte».", "a y c", "La b generaliza."),
        ex("Une la frase con su problema. 1) «Todos son iguales» 2) «Ya no es de su pueblo». a) niega la pertenencia b) generaliza", "1-b, 2-a", "La primera generaliza; la segunda niega la identidad."),
    ],
    Z=[
        ex("Ana ve una foto de una niña con ropa de ciudad y dice: «No es mapuche». ¿Qué error comete?", "Juzga la identidad por la ropa", "No se puede saber a qué pueblo se pertenece mirando una foto."),
        ex("¿Por qué «algunas» es mejor que «todas» para hablar de un pueblo?", "Porque dentro del pueblo hay diversidad", "No todos viven ni hacen lo mismo."),
    ],
    D=[
        ex("Un libro dice: «Los pueblos del norte son todos pastores». ¿Qué pregunta haces?", "¿Todos? ¿Qué dice la fuente de algunos?", "Duda de la generalización."),
        ex("Rosa cuenta que su familia hace algo distinto a lo que dice la ficha. ¿La ficha o Rosa se equivoca?", "Ninguna; puede haber diferencias entre familias", "La ficha describe de forma general."),
    ],
    context=[ex("Dos primos del pueblo diaguita viven uno en un valle y otro en una ciudad. Un niño dice que el del valle es «más diaguita». ¿Qué le respondes?", "Que los dos pertenecen a su pueblo por igual", "La pertenencia no depende del lugar de vida.")],
    selfcheck=[ex("¿Qué palabra evita generalizar?", "Algunas", "Muestra que no son todos."), ex("¿Quién decide la identidad de una persona?", "Ella misma", "Es lo que siente que es."), ex("¿Hay diversidad dentro de un pueblo?", "Sí", "Hay muchas maneras de vivir.")],
    task=T("Corrige estas tres frases para que no generalicen: a) «Todos los pueblos originarios viven en el campo.» b) «Todas las familias del pueblo aymara hacen lo mismo.» c) «Nadie del pueblo mapuche vive en una ciudad.». Escribe cada una con «algunas», «según la ficha» o «hay personas que…».",
           "a) Algunos pueblos viven en el campo y otros en ciudades. b) Según la ficha, algunas familias aymara crían llamas. c) Hay personas del pueblo mapuche que viven en ciudades.",
           ["evita «todos» y «nadie»", "cita fuente o usa «algunas»", "mantiene el respeto"], ["tres frases corregidas"], ["usar «todos» de nuevo", "negar la identidad de alguien"],
           "Valora el cambio de «todos» a «algunas» y revisa que no haya juicios sobre quién «es» o no de un pueblo."),
    reinforce="Cambia dos frases con «todos» por frases con «algunos».",
    extend="Escribe una pregunta para el educador tradicional sobre la diversidad de familias de su pueblo.",
)

L(
    OA9, 4,
    materials="Lápiz y hojas. Una ficha completa y una tabla simple de evidencias están escritas en el cuaderno.",
    use="Aprenderé a explicar con fuentes cómo se relacionan el territorio, la historia y la identidad de un pueblo.",
    prior=["Sé qué es un territorio y qué es una fuente.", "Sé distinguir pasado y presente."],
    explain=[
        "El territorio, la historia y la identidad de un pueblo están unidos. El territorio es el lugar donde ese pueblo ha vivido; la historia cuenta lo que le ha pasado en ese lugar y la identidad es cómo las personas se sienten parte de ese pueblo y de ese lugar.",
        "Para explicar esa relación necesitamos evidencia: un dato de la ficha o de un libro confiable. Una explicación completa tiene tres partes: lo que dice la fuente sobre el territorio, algo de su historia y una idea sobre la identidad. Cada parte debe tener una fuente.",
        "Una buena explicación termina diciendo qué no sabemos y a quién le preguntaremos. Así mostramos respeto: no inventamos para completar lo que falta. Esa honestidad es parte de aprender con respeto.",
    ],
    vocab=[("evidencia", "dato que muestra que algo es verdad"), ("relación", "forma en que dos cosas se conectan"), ("explicación", "texto que dice por qué o cómo es algo"), ("síntesis", "resumen de lo más importante"), ("pregunta pendiente", "lo que todavía no sé y quiero preguntar")],
    worked=[
        W("Relacionar con evidencia", F_LICK + " ¿Cómo se relaciona el territorio con el cuidado del agua?", ["La ficha dice que el agua es muy valiosa.", "Eso explica por qué el agua es importante para la vida allí.", "Cito la ficha como evidencia."], "Según la ficha, el agua es muy valiosa en ese desierto."),
        W("Decir lo que falta", "La ficha no cuenta la historia del pueblo diaguita. ¿Qué haces?", ["No la invento.", "Escribo: «Falta saber su historia».", "Pregunto a una fuente confiable."], "Anoto que falta y pregunto."),
    ],
    mistakes=[
        M("Escribir una explicación sin evidencia.", "No se puede comprobar.", "Cita un dato de la ficha en cada parte."),
        M("Inventar la historia para que la explicación se vea completa.", "Un dato inventado puede ser falso.", "Escribe una pregunta pendiente."),
    ],
    R=[
        ex("¿Qué necesita una explicación para ser confiable? A) evidencia B) adornos", "A", "La evidencia muestra de dónde viene el dato."),
        ex("Territorio, historia e identidad, ¿están unidos? Sí o No.", "Sí", "Se relacionan entre sí."),
        ex("¿Qué escribes cuando falta un dato? A) lo invento B) una pregunta pendiente", "B", "No se inventa."),
    ],
    C=[
        ex("Verdadero o falso: una síntesis es un resumen de lo más importante.", "Verdadero", "Eso significa síntesis."),
        ex("¿Qué tres partes tiene una explicación completa?", "Territorio, historia e identidad", "Son las tres ideas unidas."),
        ex("¿Qué haces al final de la explicación? A) digo qué no sé y a quién preguntaré B) no digo nada", "A", "Así se muestra respeto."),
    ],
    A=[
        ex("Ficha: «" + F_RN + "» Escribe una frase de territorio con evidencia.", "Según la ficha, el pueblo rapa nui vive en una isla del Pacífico", "Incluye el pueblo, el dato y la fuente."),
        ex("Une cada frase con la idea: 1) «Vive junto a tres ríos» 2) «Ya vivía allí antes que los españoles» 3) «Las personas se sienten parte del pueblo». a) territorio b) historia c) identidad", "1-a, 2-b, 3-c", "Cada frase corresponde a una idea."),
        ex("Ordena para armar la explicación: 1) pregunta pendiente 2) territorio con fuente 3) identidad 4) historia.", "2, 4, 3, 1", "Primero territorio, luego historia, identidad y al final la pregunta."),
    ],
    Z=[
        ex("Beto escribió una explicación muy bonita pero sin ninguna fuente. ¿Es confiable? Sí o No.", "No", "Sin evidencia no se puede comprobar."),
        ex("Una síntesis dice: «El pueblo aymara vive en el norte» y cita la tabla. ¿Qué parte de la explicación cubre?", "El territorio", "Dice dónde vive el pueblo."),
    ],
    D=[
        ex("La ficha dice dónde vive un pueblo pero no cuenta su historia. ¿Puedes escribir la historia por tu cuenta? Sí o No.", "No", "Hay que buscar una fuente."),
        ex("Dos niños explican lo mismo con palabras distintas y ambos citan la ficha. ¿Hay uno incorrecto?", "No necesariamente; ambos usan evidencia", "Pueden decirlo de manera distinta."),
    ],
    context=[ex("Tu curso prepara un cartel: «Pueblo kawésqar: canales (territorio); navega en canoas (práctica); hoy sigue su historia (identidad)». ¿Cuántas ideas distintas tiene el cartel?", "3", "Territorio, práctica e identidad son tres ideas.")],
    selfcheck=[ex("¿Por qué se cita evidencia?", "Para poder comprobar el dato", "Así se confía en la explicación."), ex("¿Qué escribes si falta un dato?", "Una pregunta pendiente", "No se inventa."), ex("¿Qué tres ideas se relacionan?", "Territorio, historia e identidad", "Son las tres del tema.")],
    task=T("Elige una ficha escrita en este cuaderno (aymara, lickanantay o kawésqar). Escribe una explicación de 4 frases: 1) dónde vive, 2) un dato del paisaje, 3) una idea sobre la identidad (por ejemplo, que hoy las personas siguen sintiéndose parte del pueblo) y 4) una pregunta pendiente sobre su historia, que la ficha no cuenta.",
           "El pueblo lickanantay vive en el desierto de Atacama (ficha). Allí hay oasis y salar. Hoy las personas siguen sintiéndose parte de su pueblo. Quiero preguntar al educador qué historia de este territorio cuentan los mayores.",
           ["usa la ficha como evidencia", "relaciona territorio e identidad", "incluye una pregunta pendiente"], ["4 frases"], ["no citar la ficha", "inventar historia"],
           "Pide que muestre con el dedo en qué parte de la ficha está cada dato; las ideas de identidad deben ser respetuosas y generales."),
    reinforce="Subraya en la ficha los datos que sirven como evidencia.",
    extend="Escribe dos preguntas para la comunidad que ayudarían a completar tu explicación.",
)

# ============================================================ OA 10 · Relación entre ser humano y naturaleza
L(
    OA10, 1,
    materials="Lápiz, hojas y colores. Las escenas están escritas en el cuaderno; puedes mirar por la ventana si quieres.",
    use="Aprenderé a mirar la naturaleza como un conjunto de seres que se relacionan entre sí y con las personas.",
    prior=["Sé nombrar animales, plantas y elementos como agua y tierra.", "Sé que las personas usan el agua y las plantas."],
    explain=[
        "La naturaleza está formada por muchos seres: el agua, la tierra, el aire, las plantas, los animales y también las personas. Todos se relacionan. Las plantas necesitan agua, los animales comen plantas y las personas cuidan o usan lo que la naturaleza ofrece.",
        "Muchos pueblos originarios entienden que las personas son parte de la naturaleza y no están separadas de ella. Por eso observan con atención cómo viven los seres, qué necesitan y qué pasa cuando cambian las estaciones.",
        "Para observar relaciones miramos dos cosas: quiénes son los seres y qué acciones hay entre ellos. Por ejemplo, en la escena «la llama come pasto junto al arroyo» los seres son la llama, el pasto y el arroyo, y las acciones son comer y estar junto al agua.",
    ],
    vocab=[("naturaleza", "todos los seres vivos y los elementos como agua y tierra"), ("ser vivo", "algo que nace, crece y muere, como plantas y animales"), ("relación", "forma en que dos seres se conectan"), ("acción", "lo que hace un ser"), ("estación", "tiempo del año: verano, otoño, invierno o primavera")],
    worked=[
        W("Seres y acciones", "Escena: «El niño riega el huerto y los pájaros beben en el charco». ¿Qué seres y qué acciones hay?", ["Seres: niño, huerto, pájaros, agua.", "Acciones: regar y beber.", "Todos usan el agua."], "Seres: niño, huerto, pájaros y agua. Acciones: regar y beber."),
        W("Una cadena de relaciones", "La lluvia cae, crece el pasto y la llama come pasto. ¿Cómo se conectan?", ["La lluvia ayuda al pasto.", "El pasto alimenta a la llama.", "Todo depende del agua."], "La lluvia ayuda al pasto y el pasto alimenta a la llama."),
    ],
    mistakes=[
        M("Pensar que las personas están separadas de la naturaleza.", "Las personas también viven de ella y la cuidan.", "Incluye a las personas entre los seres de la escena."),
        M("Nombrar solo animales y olvidar el agua o la tierra.", "El agua y la tierra también son parte de la naturaleza.", "Mira también los elementos."),
    ],
    R=[
        ex("Escena: «La alpaca come pasto». ¿Cuál es la acción? A) comer B) pasto", "A) comer", "Comer es lo que hace la alpaca."),
        ex("Escena: «El río moja la tierra». ¿Qué ser es un elemento: el río o la alpaca?", "El río", "El río es agua."),
        ex("Las plantas necesitan agua. ¿Verdadero o falso?", "Verdadero", "Sin agua no crecen."),
    ],
    C=[
        ex("¿Qué incluye la naturaleza? A) solo animales B) agua, tierra, plantas, animales y personas", "B", "Todos son parte de la naturaleza."),
        ex("Verdadero o falso: las personas están separadas de la naturaleza.", "Falso", "Las personas son parte de ella."),
        ex("¿Qué miramos al observar relaciones?", "Los seres y las acciones", "Con eso entendemos cómo se conectan."),
    ],
    A=[
        ex("Escena: «El niño planta un arbolito y lo riega». Escribe los dos seres vivos.", "niño y arbolito", "Son los dos seres vivos que aparecen en la escena."),
        ex("Une cada ser con su acción. 1) el niño 2) el pájaro 3) la lluvia. a) bebe b) cae c) riega", "1-c, 2-a, 3-b", "Cada acción corresponde a un ser."),
        ex("Escena: «La lluvia cae, crece el pasto y comen las vacas». Ordena la cadena.", "lluvia, pasto, vacas", "La lluvia ayuda al pasto y el pasto alimenta a las vacas."),
    ],
    Z=[
        ex("Camila dice que si no hay agua solo les pasa algo a las plantas. ¿Qué error tiene?", "También afecta a los animales y a las personas", "Todos dependen del agua."),
        ex("¿Por qué es importante observar con atención la naturaleza?", "Para entender qué necesitan los seres y cómo cambian", "Así sabemos cómo cuidarlos."),
    ],
    D=[
        ex("En una escena hay un río, tres patos y un niño que mira. Sin contar el río, ¿cuántos seres vivos hay?", "4", "Tres patos más un niño."),
        ex("Si desaparece el agua de un charco, ¿a quiénes afecta? A) solo al charco B) a los seres que lo usan", "B", "Los seres dependen del agua."),
    ],
    context=[ex("En un valle hay un río, una niña y 4 gorriones. Cuenta solo a la niña y a los gorriones: ¿cuántos seres vivos son?", "5", "Una niña más cuatro gorriones suman 5 seres vivos.")],
    selfcheck=[ex("¿Las personas son parte de la naturaleza?", "Sí", "Viven en ella."), ex("¿Qué necesitan las plantas?", "Agua", "Sin agua no crecen."), ex("¿Qué observas en una relación?", "Seres y acciones", "Son las dos cosas que se miran.")],
    task=T("Observa un lugar de tu casa o del patio (una planta, un charco, un árbol, el cielo). Si no puedes salir, usa esta escena: «Un niño riega una maceta; una abeja visita la flor; el sol calienta la tierra». Dibuja la escena y escribe tres seres y tres acciones.",
           "Seres: niño, abeja, flor. Acciones: regar, visitar, calentar.",
           ["nombra seres", "nombra acciones", "incluye a las personas"], ["dibujo", "lista de seres y acciones"], ["olvidar elementos como agua o sol"],
           "Reconoce lo que observó y pide que explique una relación; invitar a preguntar al educador tradicional cómo mira su pueblo esa relación."),
    reinforce="Dibuja un ser vivo y una acción que haga con otro ser.",
    extend="Escribe una pregunta sobre cómo cuida un pueblo originario un río, un cerro o un bosque.",
)

L(
    OA10, 2,
    materials="Lápiz y hojas. Los casos están escritos en el cuaderno.",
    use="Aprenderé que cuidar la naturaleza es una responsabilidad de ida y vuelta: ella nos da y nosotros cuidamos y agradecemos.",
    prior=["Sé que el agua y las plantas nos sirven.", "Sé decir gracias."],
    explain=[
        "La naturaleza nos da agua, alimento, leña y lugares donde vivir. Muchos pueblos originarios entienden que quien recibe también debe cuidar y agradecer. Eso se llama reciprocidad: dar y recibir con respeto.",
        "En los pueblos andinos, como el aymara y el quechua, se habla de la Pachamama, la Madre Tierra, a la que se agradece. Cada pueblo tiene sus propias formas de agradecer y de cuidar, y las enseñan las personas que conocen su cultura. No las inventamos ni las imitamos.",
        "Nosotros podemos practicar la reciprocidad con acciones sencillas: tomar solo el agua que necesitamos, no botar basura, no arrancar plantas por jugar y agradecer lo que recibimos. Cuidar es una responsabilidad de todos.",
    ],
    vocab=[("reciprocidad", "dar y recibir con respeto, de ida y vuelta"), ("cuidar", "proteger para que no se dañe"), ("agradecer", "decir o mostrar gracias por lo recibido"), ("responsabilidad", "algo que me toca hacer bien"), ("Pachamama", "nombre andino de la Madre Tierra")],
    worked=[
        W("Reciprocidad en una acción", "Ana usa agua para regar y al final cierra bien la llave. ¿Cómo practica la reciprocidad?", ["Recibe agua.", "Cuida que no se gaste de más.", "Eso es cuidar a cambio de recibir."], "Usa lo que necesita y cuida que no se pierda."),
        W("Elegir la acción que cuida", "¿Qué cuida más el río: botar basura o recogerla? ", ["Botar basura lo ensucia.", "Recogerla lo protege.", "Cuidar es proteger."], "Recoger la basura."),
    ],
    mistakes=[
        M("Pensar que la naturaleza solo está para que la usemos.", "Quien recibe también debe cuidar.", "Después de usar, devuelve cuidado."),
        M("Inventar una ceremonia para agradecer.", "Cada pueblo tiene sus propias formas y las enseña su comunidad.", "Agradece con acciones simples y pregunta al educador tradicional."),
    ],
    R=[
        ex("Reciprocidad es dar y recibir con respeto. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("¿Qué cuida el agua? A) cerrar la llave B) dejarla abierta", "A", "Cerrar la llave evita gastarla."),
        ex("Cuando alguien te da algo, ¿qué dices?", "Gracias", "Agradecer es parte del respeto."),
    ],
    C=[
        ex("¿Qué significa Pachamama en los pueblos andinos? A) Madre Tierra B) un animal", "A", "Es el nombre andino de la Madre Tierra."),
        ex("Verdadero o falso: cuidar es tarea solo de las personas mayores.", "Falso", "Cuidar nos toca a todos."),
        ex("¿Quién enseña cómo agradece y cuida un pueblo a su manera?", "Las personas que conocen su cultura, como el educador tradicional", "Ellos saben las formas propias."),
    ],
    A=[
        ex("Clasifica cada acción como CUIDA o DAÑA: a) recoger papeles del suelo b) arrancar flores por jugar c) cerrar la llave.", "a) cuida, b) daña, c) cuida", "Recoger y cerrar la llave protegen; arrancar flores por jugar daña."),
        ex("Une cada situación con la acción que devuelve cuidado. 1) Usé mucha agua para regar. 2) Mi curso ensució el patio. 3) Me regalaron una fruta. a) recojo lo que ensucié b) uso menos agua la próxima vez c) digo gracias", "1-b, 2-a, 3-c", "Cada acción responde a su situación: usar menos agua, limpiar y agradecer."),
        ex("Ordena una acción de cuidado: 1) agradezco 2) tomo solo lo necesario 3) recibo agua.", "3, 2, 1", "Primero recibo, luego uso lo necesario y al final agradezco."),
    ],
    Z=[
        ex("Pedro dice: «Voy a hacer una ceremonia como las de los pueblos, así que la invento». ¿Qué le dices?", "Que la forma propia la enseña la comunidad y que no se inventa", "Se respeta lo que cada pueblo enseña."),
        ex("¿Por qué decimos que cuidar es de ida y vuelta?", "Porque recibimos y también damos cuidado", "Es lo que significa reciprocidad."),
    ],
    D=[
        ex("Un niño toma 5 flores del jardín para jugar y solo necesita 1 para su dibujo. ¿Cuántas tomó de más?", "4", "5 − 1 = 4 flores de más."),
        ex("Una comunidad dice que un río se cuida de cierta manera. ¿Esa manera es igual para todos los pueblos? Sí o No.", "No", "Cada pueblo tiene sus formas."),
    ],
    context=[ex("En un huerto, Luz recibió tomates y siembra una semilla nueva. ¿Qué practica?", "Reciprocidad", "Recibe y devuelve cuidado.")],
    selfcheck=[ex("¿Qué es reciprocidad?", "Dar y recibir con respeto", "Es de ida y vuelta."), ex("¿Qué es la Pachamama?", "La Madre Tierra en los pueblos andinos", "Es su nombre andino."), ex("Nombra una acción que cuida.", "Recoger basura o cerrar la llave", "Protegen el entorno.")],
    task=T("Escribe una lista de 3 acciones que puedes hacer en tu casa o escuela para cuidar el agua, las plantas o el suelo, usando las que están en esta clase (cerrar la llave, recoger basura, regar con cuidado). Dibuja una y escribe cómo agradeces lo que recibes de la naturaleza con palabras tuyas.",
           "Acciones: cerrar la llave, recoger papeles y regar la planta con poquita agua. Agradezco diciendo gracias al agua cuando bebo.",
           ["escribe tres acciones", "relaciona recibir y cuidar", "no inventa ceremonias"], ["lista", "dibujo", "frase de agradecimiento"], ["inventar un rito"],
           "Valora las acciones y que no haya inventado ritos; invitar a preguntar cómo se agradece en la comunidad."),
    reinforce="Cuenta a alguien una acción que cuida el agua.",
    extend="Escribe una pregunta sobre cómo agradece a la naturaleza un pueblo originario, para el educador tradicional.",
)

L(
    OA10, 3,
    materials="Lápiz y hojas. Los textos para comparar están escritos en el cuaderno.",
    use="Aprenderé a comparar distintas maneras de mirar la naturaleza sin decir que una es mejor que otra.",
    prior=["Sé qué es comparar.", "Sé que hay diferentes personas y pueblos."],
    explain=[
        "Las personas miran la naturaleza de maneras distintas. Un científico mide y anota. Una familia agricultora observa cuándo sembrar. Un pueblo originario puede entender que la tierra es una madre, como la Pachamama en los pueblos andinos. Cada manera enseña algo.",
        "Comparar es ver qué se parece y qué es distinto. En estas tres maneras se parece que todas observan, y todas cuidan lo que necesitan. Se diferencian en las palabras que usan y en lo que les importa más.",
        "Cuando comparamos no decimos «esta es mejor». Decimos cómo mira cada una y qué podemos aprender. Si no entendemos una manera de mirar, preguntamos con respeto y escuchamos a quien la enseña.",
    ],
    vocab=[("perspectiva", "manera de mirar algo"), ("comparar", "ver qué se parece y qué es distinto"), ("jerarquizar", "decir que algo es mejor o peor"), ("científico", "persona que estudia la naturaleza midiendo y anotando"), ("agricultor", "persona que cultiva la tierra")],
    worked=[
        W("Comparar dos perspectivas", "Perspectiva A: «La tierra es una madre y se le agradece». Perspectiva B: «La tierra se mide y se estudia con instrumentos». ¿Qué se parece?", ["Las dos miran la tierra con atención.", "Las dos buscan cuidar o conocerla.", "Se diferencian en las palabras que usan."], "Las dos observan y quieren cuidar o conocer la tierra."),
        W("No jerarquizar", "Un niño dice que la manera científica es mejor que la de los pueblos. ¿Qué le respondes?", ["Cada manera sirve para algo distinto.", "No se dice cuál es mejor.", "Podemos aprender de ambas."], "No se jerarquiza; aprendemos de ambas."),
    ],
    mistakes=[
        M("Decir que una perspectiva es «mejor» que otra.", "Cada una nace de una experiencia distinta.", "Di qué se parece y qué es distinto."),
        M("Creer que todos los pueblos miran la naturaleza igual.", "Cada pueblo tiene su propia mirada.", "Habla de «el pueblo…» con una fuente, no de «todos»."),
    ],
    R=[
        ex("Comparar es ver qué se parece y qué es distinto. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("¿Se dice cuál perspectiva es mejor al comparar? Sí o No.", "No", "No se jerarquiza."),
        ex("Un científico mide la lluvia con un vaso. ¿Observa o no observa?", "Observa", "Mide y anota."),
    ],
    C=[
        ex("¿Qué se parece en las perspectivas de la explicación? A) todas observan B) todas son idénticas", "A", "Todas miran con atención."),
        ex("Verdadero o falso: hay una sola manera correcta de mirar la naturaleza.", "Falso", "Hay varias maneras que enseñan algo."),
        ex("¿Qué haces si no entiendes una perspectiva?", "Pregunto con respeto y escucho", "No se descarta."),
    ],
    A=[
        ex("Perspectiva 1: «Observo cuándo florecen las plantas para saber cuándo sembrar». Perspectiva 2: «Anoto cuántos milímetros llueve cada día». ¿Qué tienen en común?", "Las dos observan la naturaleza", "Ambas miran con atención."),
        ex("Une cada persona con su manera de mirar. 1) científico 2) agricultor 3) persona de un pueblo andino que agradece a la Madre Tierra. a) mide y anota b) observa cuándo sembrar c) agradece a la Madre Tierra", "1-a, 2-b, 3-c", "Cada una tiene su manera."),
        ex("Marca las frases que NO jerarquizan: a) «Esta manera es mejor» b) «Cada manera enseña algo» c) «Aprendo de las dos».", "b y c", "La a dice cuál es mejor."),
    ],
    Z=[
        ex("Ana dice: «Los pueblos originarios no saben de la naturaleza porque no usan instrumentos». ¿Qué error comete?", "Jerarquiza y desconoce que observan y saben mucho", "Su saber viene de la observación y la experiencia."),
        ex("¿Por qué no basta una sola perspectiva para entender la naturaleza?", "Porque cada una enseña algo distinto", "Se complementan entre sí."),
    ],
    D=[
        ex("Una familia agricultora y una persona de una comunidad indígena observan el clima y las plantas para decidir cuándo sembrar. ¿Qué tienen en común?", "Ambas observan para decidir", "La observación orienta la decisión."),
        ex("Un libro dice «los pueblos del norte creen todos lo mismo». ¿Qué cuidado tienes?", "Dudar del «todos» y revisar la fuente", "Así evita generalizar."),
    ],
    context=[ex("Dos niños hablan de la lluvia: uno dice «es agua que cae de las nubes» y otro «es un regalo que se agradece». ¿Quién tiene la razón?", "Los dos", "Son dos maneras de mirar que pueden convivir.")],
    selfcheck=[ex("En Lengua y Cultura de los Pueblos Originarios, ¿qué es una perspectiva?", "Una manera de mirar algo", "Cambia según la persona."), ex("¿Se jerarquiza una perspectiva?", "No", "Cada una enseña algo."), ex("¿Qué se hace al comparar?", "Ver qué se parece y qué es distinto", "Es lo que significa comparar.")],
    task=T("Lee estas dos frases: A) «La tierra se cuida con un huerto sin basura.» B) «La tierra es una madre a quien se agradece, como en los pueblos andinos.» Escribe una cosa que se parece, una que es distinta, y una frase para decir «ninguna es mejor».",
           "Se parece: las dos cuidan la tierra. Es distinto: una habla del huerto y otra de una madre. Frase: «Cada manera de mirar enseña algo».",
           ["compara sin jerarquizar", "nombra una semejanza y una diferencia", "usa lenguaje respetuoso"], ["tres frases"], ["decir cuál es mejor"],
           "Reconoce la frase final; si jerarquizó, invitarlo a volver a leer ambas con curiosidad."),
    reinforce="Compara dos hojas de plantas distintas y di qué se parece y qué es distinto.",
    extend="Escribe una pregunta sobre cómo mira la naturaleza un pueblo originario, para el educador tradicional.",
)

L(
    OA10, 4,
    materials="Lápiz y hojas. Una lista de compromisos posibles está escrita en el cuaderno.",
    use="Aprenderé a proponer un compromiso real y pequeño para cuidar la naturaleza, coherente con lo que enseñó la fuente.",
    prior=["Sé qué es cuidar.", "Sé qué es un compromiso."],
    explain=[
        "Un compromiso es una promesa de hacer algo. Un buen compromiso es pequeño, claro y se puede cumplir. Por ejemplo: «esta semana recogeré los papeles del patio» o «cerraré la llave mientras me lavo los dientes».",
        "Un compromiso respetuoso se parece a lo que aprendimos de la fuente. Si la fuente dice que el agua es valiosa en el desierto, un compromiso coherente es cuidar el agua. No copiamos ceremonias ni usamos símbolos de un pueblo si no nos los enseñaron.",
        "Para cumplir un compromiso, lo escribimos, decimos cuándo lo haremos y cómo sabremos que lo cumplimos. Al final revisamos y compartimos lo que aprendimos con quien nos enseñó.",
    ],
    vocab=[("compromiso", "promesa de hacer algo"), ("coherente", "que va de acuerdo con lo que aprendí"), ("cumplir", "hacer lo prometido"), ("evidencia", "prueba de que lo hice"), ("revisar", "mirar si lo logré")],
    worked=[
        W("Armar un compromiso", "La ficha dice que en el desierto el agua es muy valiosa. ¿Qué compromiso es coherente?", ["Debe cuidar el agua.", "Debe ser pequeño y posible.", "Digo cuándo lo haré."], "«Esta semana cerraré la llave mientras me lavo los dientes.»"),
        W("Revisar el compromiso", "Luz prometió regar la planta cada día y lo hizo 5 días de 7. ¿Cumplió?", ["Compara lo prometido con lo hecho.", "Hizo 5 de 7 días.", "Cumplió parte; puede mejorar."], "Cumplió 5 de 7 días."),
    ],
    mistakes=[
        M("Prometer algo muy grande.", "No se puede cumplir y desanima.", "Elige algo pequeño y posible."),
        M("Copiar un rito o símbolo de un pueblo como compromiso.", "Quizás no nos lo enseñaron ni nos corresponde.", "Elige una acción tuya, simple y respetuosa."),
    ],
    R=[
        ex("Un compromiso es una promesa de hacer algo. ¿Verdadero o falso?", "Verdadero", "Eso significa compromiso."),
        ex("¿Qué compromiso es más posible? A) cuidar todos los ríos del mundo B) recoger papeles del patio", "B", "Es pequeño y se puede cumplir."),
        ex("Si prometo regar una planta, ¿qué debo hacer? A) regarla B) olvidarla", "A", "Cumplir es hacer lo prometido."),
    ],
    C=[
        ex("¿Qué es un compromiso coherente? A) el que va de acuerdo con lo que aprendí B) uno al azar", "A", "Coherente significa que concuerda."),
        ex("Verdadero o falso: puedo copiar una ceremonia de un pueblo como mi compromiso.", "Falso", "Eso corresponde a la comunidad que la enseña."),
        ex("¿Qué debe decir un buen compromiso?", "Qué haré y cuándo", "Debe ser claro."),
    ],
    A=[
        ex("Ficha: «" + F_LICK + "» Escribe un compromiso coherente con la importancia del agua.", "Respuesta aceptable: «Cerraré la llave mientras me lavo los dientes»", "Cuida el agua, que la ficha dice valiosa."),
        ex("Marca los compromisos pequeños y posibles: a) cerrar la llave al lavarme los dientes b) limpiar todo un bosque c) recoger papeles del patio.", "a y c", "El b es demasiado grande."),
        ex("Ordena: 1) revisar si cumplí 2) escribir el compromiso 3) cumplirlo. ¿Qué orden es correcto?", "2, 3, 1", "Se escribe, se cumple y luego se revisa."),
    ],
    Z=[
        ex("Pedro prometió cuidar el agua pero dejó la llave abierta. ¿Qué no fue coherente?", "No hizo lo que dijo", "Su acción no coincidió con su promesa."),
        ex("¿Por qué mostramos nuestro compromiso a quien nos enseñó?", "Para agradecer y compartir lo aprendido", "Es parte de la reciprocidad."),
    ],
    D=[
        ex("Rosa prometió 7 días de riego y cumplió 6. ¿Cuántos días le faltaron?", "1", "7 − 6 = 1 día."),
        ex("Un compañero dice que su compromiso es hacer un rito que vio en una foto. ¿Qué le sugieres?", "Elegir una acción propia y preguntar al educador tradicional", "Los ritos los enseña la comunidad."),
    ],
    context=[ex("Una escuela decide cuidar un pequeño huerto durante 4 semanas. Si riegan 3 veces por semana, ¿cuántos riegos son en total?", "12", "4 semanas × 3 riegos = 12 riegos.")],
    selfcheck=[ex("En Lengua y Cultura de los Pueblos Originarios, ¿qué es un compromiso?", "Una promesa de hacer algo", "Es una promesa."), ex("¿Cómo debe ser un compromiso?", "Pequeño, claro y posible", "Para poder cumplirlo."), ex("¿Qué haces al final?", "Reviso si lo cumplí", "Compruebo lo que logré.")],
    task=T("Escribe tu compromiso de cuidado en una frase («Esta semana yo…»). Elige una de estas ideas o escribe otra parecida: cerrar la llave al lavarme los dientes, recoger papeles del patio, regar una planta. Dibuja una tabla de 7 casillas (una por día) y marca los días que lo cumples.",
           "Esta semana yo cerraré la llave mientras me lavo los dientes. Marcaré cada día en mi tabla.",
           ["es pequeño y posible", "tiene fecha", "tiene forma de revisarlo"], ["frase", "tabla de 7 días"], ["prometer algo imposible", "copiar un rito"],
           "Valora lo concreto; ayuda a reducirlo si es demasiado grande. Invitar a contar el resultado al educador tradicional o a la comunidad."),
    reinforce="Marca en una tabla de 3 días si cumpliste un compromiso pequeño.",
    extend="Pregunta a una persona mayor qué hace ella para cuidar el agua o la tierra y anota su respuesta con permiso.",
)
