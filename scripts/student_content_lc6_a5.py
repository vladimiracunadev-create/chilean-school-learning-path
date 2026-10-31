"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 15 (patrimonio cultural de otros pueblos indígenas y de otras culturas) y
OA 16 (relación entre ser humano, naturaleza y cosmos, vinculada a la ciencia desde la perspectiva indígena).

Las comunidades, personas y testimonios son INVENTADOS y se rotulan así; no se describe ningún saber ni práctica de
un pueblo real. Los dos únicos datos externos son el reconocimiento de la UNESCO al Parque Nacional Rapa Nui (1995) y
a los asentamientos y la momificación artificial de la cultura Chinchorro (2021): requieren revisión de especialista.
Lo tradicional lo enseñan el educador o la educadora tradicional y la comunidad.
"""
from __future__ import annotations

from student_content_lc6_a import L, M, MAT, T, W
from student_lessons import arith, ex

OA15, OA16 = "LC06 OA 15", "LC06 OA 16"

# ------------------------------------------------------------------ OA 15
FPP = ("Ficha situada (inventada). Comunidad: Pueblo Piedra (no es un pueblo real). Territorio: una plaza con un muro de piedra, un camino antiguo y cerros. "
       "Fuente y responsable: don Anselmo, vecino de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: don Anselmo autorizó usar esta ficha en la escuela. "
       "Límite: no se cuentan los lugares de los cerros que la comunidad resguarda.")
TPP = ("Testimonio inventado de don Anselmo, de Pueblo Piedra: «El muro de piedra lo levantaron mis antepasados y cada año lo reparamos entre todos. También guardamos canciones que se cantan durante el trabajo. "
       "Algunas personas de afuera quieren llevarse piedras como recuerdo, y eso no nos gusta. Hay lugares de los cerros que no mostramos.»")
TVF = ("Testimonio inventado de doña Ximena, de Villa Ferroviaria (pueblo ferroviario, no indígena): «La estación antigua la cuidamos entre los vecinos. Guardamos fotos y cuentos de los antiguos trabajadores del tren. "
       "Cada año repintamos las bancas. A veces alguien se lleva un clavo viejo de recuerdo, y eso nos duele.»")
UNESCO = ("En 1995 la UNESCO declaró Patrimonio Mundial el Parque Nacional Rapa Nui, en Chile. En 2021 declaró Patrimonio Mundial los asentamientos y la momificación artificial de la cultura Chinchorro, en el norte de Chile.")

L(
    OA15, 1, materials=MAT,
    use="Aprenderé a situar un patrimonio cultural: de qué comunidad es, quién lo cuenta y qué no se cuenta. Sirve para conocer y valorar el patrimonio de otros pueblos y culturas sin hablar por ellos.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que cada comunidad cuenta lo suyo a su manera."],
    explain=[
        "El patrimonio cultural es el conjunto de bienes y saberes que una comunidad recibió de sus antepasados, cuida y quiere transmitir a las nuevas generaciones. Hay dos grandes tipos. El patrimonio material son cosas que se pueden tocar, como un muro, un camino, una vasija o un edificio. El patrimonio inmaterial son saberes y prácticas que no se tocan, como un relato, una canción, una lengua o una forma de trabajar.",
        "Cada pueblo y cada cultura tiene su patrimonio. Conocerlo es aprender qué es y de quién es. Valorarlo es reconocer su importancia para quienes lo cuidan y entender que hay que protegerlo. Muchos patrimonios indígenas pertenecen a la comunidad que los creó, y no son de cualquiera: se visitan y se estudian con respeto y con permiso.",
        "Antes de conocer un patrimonio hay que situarlo. La ficha situada dice la comunidad, el territorio, la fuente, el permiso y el límite. Con ella sabemos de quién es el relato y qué no se cuenta. Lo que dice una ficha vale para esa comunidad y no para todos los pueblos.",
    ],
    vocab=[("patrimonio cultural", "bienes y saberes que una comunidad recibió de sus antepasados, cuida y quiere transmitir"), ("patrimonio material", "cosas que se pueden tocar, como un muro o una vasija"), ("patrimonio inmaterial", "saberes y prácticas que no se tocan, como un relato o una canción"), ("proteger", "cuidar algo para que no se pierda ni se dañe"), ("fuente", "persona o texto que entrega el dato")],
    worked=[
        W("Leer una ficha situada", FPP + " ¿De quién es el relato y qué no se cuenta?", ["La comunidad es Pueblo Piedra y la fuente es don Anselmo.", "Él dio permiso para usar la ficha en la escuela.", "El límite dice que no se cuentan los lugares de los cerros que la comunidad resguarda."], "El relato es de don Anselmo, de Pueblo Piedra; no se cuentan los lugares resguardados de los cerros."),
        W("Clasificar un patrimonio", "En Pueblo Piedra hay un muro de piedra levantado por los antepasados y canciones que se cantan durante el trabajo. ¿Cuál es material y cuál inmaterial?", ["El muro se puede tocar: es material.", "Las canciones no se tocan: son inmateriales."], "El muro es patrimonio material; las canciones, patrimonio inmaterial."),
    ],
    mistakes=[
        M("Pensar que patrimonio es solo lo que se puede ver, como edificios.", "También hay patrimonio inmaterial: relatos, canciones, saberes.", "Pregúntate si se puede tocar o si es un saber o práctica."),
        M("Decir que el patrimonio de Pueblo Piedra es el de todos los pueblos indígenas.", "La ficha habla de una sola comunidad.", "Escribe «según don Anselmo, en Pueblo Piedra…»."),
    ],
    R=[
        ex("Según la ficha de Pueblo Piedra, ¿quién es la fuente?", "Don Anselmo", "La ficha lo nombra como fuente y responsable."),
        ex("¿Qué territorio tiene Pueblo Piedra? A) una plaza con muro de piedra, un camino antiguo y cerros B) un lago y un bosque", "A", "El lago y el bosque son de otra ficha."),
        ex("La ficha de Pueblo Piedra dice que no se cuentan ciertos lugares de los cerros. ¿Los ubicas en tu trabajo? Responde Sí o No.", "No", "El límite de la ficha lo prohíbe."),
    ],
    C=[
        ex("En Lengua y Cultura, ¿qué es el patrimonio cultural? A) cualquier objeto viejo B) bienes y saberes que una comunidad recibió, cuida y quiere transmitir", "B", "El patrimonio se cuida y se transmite."),
        ex("Verdadero o falso: una canción que se transmite de generación en generación es patrimonio inmaterial.", "Verdadero", "No se toca; es un saber y una práctica."),
        ex("Verdadero o falso: el patrimonio de Pueblo Piedra sirve para hablar de todos los pueblos indígenas.", "Falso", "Una comunidad no representa a todos los pueblos."),
    ],
    A=[
        ex("Clasifica en MATERIAL o INMATERIAL: a) un camino antiguo b) un relato que se cuenta de generación en generación.", "a material, b inmaterial", "El camino se toca; el relato es un saber."),
        ex("Don Anselmo dice: «Cada año reparamos el muro entre todos». ¿Qué muestra esa frase? A) que el muro se abandonó B) que la comunidad cuida su patrimonio", "B", "Reparar entre todos es cuidar."),
        ex("Tema: el patrimonio. Una compañera trae una ficha con comunidad y fuente, pero sin permiso. ¿Qué falta? A) el color del papel B) la autorización de la fuente para compartir", "B", "El permiso es parte de una ficha situada."),
    ],
    Z=[
        ex("Pablo escribe: «Como Pueblo Piedra tiene un muro, todos los pueblos indígenas tienen muros de piedra». ¿Qué error comete?", "Generaliza una comunidad a todos los pueblos", "Un testimonio no representa a todos los pueblos."),
        ex("¿Por qué conviene pedir permiso antes de conocer el patrimonio de una comunidad? A) porque pertenece a la comunidad que lo cuida B) porque es una norma sin razón", "A", "El patrimonio tiene dueños y cuidadores."),
    ],
    D=[
        ex("Una ficha dice solo: «Comunidad: Pueblo Piedra. Patrimonio: un muro». ¿Qué datos faltan?", "Fuente, permiso y límite", "La ficha situada exige esos tres datos además de comunidad y territorio."),
        ex("Un cartel dice: «Todos los pueblos cantan mientras trabajan, como en Pueblo Piedra». ¿Qué corriges? A) escribo «según don Anselmo (persona inventada), en Pueblo Piedra…» B) lo dejo igual", "A", "El cartel debe atribuir el dato a esa fuente."),
    ],
    context=[ex("En una excursión visitan un sitio de una comunidad real. Un compañero quiere llevarse una piedra como recuerdo. ¿Qué haces? A) le explico que es patrimonio de la comunidad y que no se debe sacar nada B) lo dejo, porque es solo una piedra", "A", "Sacar piezas de un sitio daña el patrimonio.")],
    selfcheck=[
        ex("Nombra los dos tipos de patrimonio de esta clase.", "Material e inmaterial", "Son los dos tipos de la explicación."),
        ex("Verdadero o falso: conocer un patrimonio es lo mismo que valorarlo.", "Falso", "Conocer es saber qué es; valorar es reconocer su importancia."),
        ex("Ante una duda sobre el patrimonio de una comunidad real, ¿qué haces? A) pregunto al educador tradicional B) lo supongo", "A", "Él o ella es la fuente."),
    ],
    task=T("Lee esta nota inventada de don Anselmo: «En Pueblo Piedra hay un muro que cuidamos entre todos y canciones de trabajo que nos enseñaron los mayores. De los lugares de los cerros no hablamos con visitas.» Haz una ficha con: comunidad, fuente, patrimonio material, patrimonio inmaterial, qué dice la fuente y un límite. Luego escribe una frase con «Yo pienso que…» sobre por qué es importante cuidar ese patrimonio.",
           "Comunidad: Pueblo Piedra. Fuente: don Anselmo. Material: el muro. Inmaterial: las canciones de trabajo. Dice: cuidan el muro entre todos y los mayores enseñaron las canciones. Límite: no se cuentan los lugares de los cerros. Yo pienso que cuidar el muro y las canciones ayuda a que los jóvenes conozcan su historia.",
           ["completa la ficha con datos de la nota", "distingue material e inmaterial", "pone un límite"], ["ficha completa", "frase con «Yo pienso que»"], ["inventar canciones o lugares", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea de la nota está cada dato; valorar que no escriba canciones inventadas."),
    reinforce="Subraya en la ficha de Pueblo Piedra la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué el patrimonio inmaterial también necesita protección.",
)

L(
    OA15, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre patrimonio con límites declarados: qué dice la fuente, qué tipo de patrimonio es, qué interpreto yo y qué no se cuenta.",
    prior=["Sé situar un patrimonio con su ficha.", "Sé distinguir patrimonio material de inmaterial."],
    explain=[
        "Un testimonio sobre patrimonio cuenta qué se cuida, quiénes lo cuidan, cómo y qué lo amenaza. Para leerlo con respeto separamos cuatro cosas. Lo que la fuente dice, con sus palabras. El tipo de patrimonio que aparece: material o inmaterial. Lo que yo interpreto, que es una idea mía. Y lo que no se cuenta o no sé.",
        "En el testimonio de don Anselmo, el muro de piedra es patrimonio material y las canciones de trabajo son patrimonio inmaterial. También cuenta una amenaza: personas de afuera quieren llevarse piedras como recuerdo. No cuenta cuántas piedras se han perdido. Si yo agrego una cifra o un nombre, estoy inventando.",
        "Leer con límites declarados significa decir hasta dónde llega lo que afirmo. Los lugares de los cerros que la comunidad resguarda se respetan y no se piden ni se describen. Para saber más sobre un patrimonio real, preguntamos al educador o a la educadora tradicional y pedimos permiso antes de difundirlo.",
    ],
    vocab=[("amenaza", "algo que puede dañar o hacer perder el patrimonio"), ("difundir", "dar a conocer a muchas personas"), ("resguardar", "cuidar algo y no mostrarlo a todos"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("límite", "lo que no se cuenta o no se sabe")],
    worked=[
        W("Separar cuatro cosas", TPP + " Separa lo que dice, el tipo de patrimonio, lo que interpreto y lo que no se cuenta.", ["Dice: el muro lo levantaron los antepasados y cada año lo reparan entre todos.", "Tipo: el muro es material; las canciones de trabajo son inmateriales.", "Interpreto: yo pienso que reparar entre todos mantiene unida a la comunidad.", "No se cuenta: cuáles son los lugares de los cerros que no se muestran."], "Dice: el muro lo reparan entre todos cada año. Tipo: material e inmaterial. Interpreto: reparar une a la comunidad. No se cuenta: los lugares de los cerros."),
        W("Detectar un agregado", "Una niña escribe: «Don Anselmo cuenta que ya se llevaron la mitad de las piedras». ¿Está bien?", ["Reviso el testimonio: dice que algunas personas quieren llevarse piedras.", "No dice cuántas se llevaron.", "La niña inventó una cifra."], "No: inventa una cantidad que el testimonio no dice."),
    ],
    mistakes=[
        M("Agregar cifras o nombres que la fuente no dio.", "Se inventan datos.", "Escribe «el testimonio no lo dice»."),
        M("Escribir mi interpretación como si la hubiera dicho la fuente.", "Se atribuye a la comunidad algo que no dijo.", "Marca mis ideas con «yo pienso que»."),
    ],
    R=[
        ex("Según don Anselmo, ¿quién levantó el muro: sus antepasados o una empresa?", "Sus antepasados", "El testimonio lo dice así."),
        ex("Tema: el patrimonio. Una interpretación, ¿es una idea mía o un dato de la fuente?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Si el testimonio no dice cuántas piedras se perdieron, ¿qué escribes? A) se perdieron veinte B) el testimonio no lo dice", "B", "No se inventan cifras."),
    ],
    C=[
        ex("Don Anselmo dice: «Guardamos canciones que se cantan durante el trabajo». ¿Qué tipo de patrimonio es? A) inmaterial B) material", "A", "Una canción no se toca."),
        ex("Verdadero o falso: que personas de afuera quieran llevarse piedras es una amenaza para el patrimonio.", "Verdadero", "Sacar piedras daña el muro."),
        ex("Verdadero o falso: respetar los lugares que la comunidad resguarda es parte de leer con límites.", "Verdadero", "Lo resguardado no se pide ni se describe."),
    ],
    A=[
        ex("Doña Ximena, de un pueblo ferroviario, dice: «La estación antigua la cuidamos entre los vecinos». Clasifica en DICE LA FUENTE o INTERPRETO: a) los vecinos cuidan la estación b) la estación es el lugar más querido del pueblo.", "a dice la fuente, b interpreto", "La segunda es una idea de quien lee."),
        ex("Doña Ximena dice: «Guardamos fotos y cuentos de los antiguos trabajadores del tren». ¿Qué tipo de patrimonio incluye? A) material (fotos) e inmaterial (cuentos) B) solo material", "A", "Las fotos se tocan; los cuentos son un saber."),
        ex("Un niño escribe: «Don Anselmo cuenta que el muro tiene mil años». ¿Qué dato no está en el testimonio?", "Que el muro tiene mil años", "El testimonio dice que lo levantaron los antepasados, sin precisar años."),
    ],
    Z=[
        ex("Rodrigo escribe, sin marcarlo: «Las canciones de trabajo de Pueblo Piedra son las más bonitas». ¿Qué debería hacer con esa frase?", "Quitarla porque ordena y no está en la fuente", "No está en el testimonio y jerarquiza."),
        ex("Tema: el patrimonio. ¿Por qué conviene escribir los límites al final del trabajo? A) para mostrar hasta dónde llega lo afirmado B) para llenar la hoja", "A", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        ex("Dos frases. 1) «Don Anselmo cuenta que reparan el muro cada año». 2) «Don Anselmo cuenta que el muro es sagrado». ¿Cuál se queda en la fuente?", "La primera", "La segunda agrega algo que el testimonio no contiene."),
        ex("Don Anselmo no contó qué canciones guardan. ¿Qué escribes en los límites? A) guardan una canción sobre el muro B) no sé qué canciones guardan", "B", "Declarar lo que no sé evita inventar."),
    ],
    context=[ex("Para un afiche escolar, un compañero quiere inventar una canción «típica de Pueblo Piedra». ¿Qué le dices? A) que la escriba con mucha emoción B) que no la invente porque el patrimonio de una comunidad no se inventa", "B", "No se inventa el patrimonio de una comunidad.")],
    selfcheck=[
        ex("Nombra las cuatro cosas que separo al leer un testimonio sobre patrimonio.", "Lo que dice la fuente, el tipo de patrimonio, lo que interpreto y lo que no se cuenta", "Son los pasos de la lectura con límites."),
        ex("Tema: el patrimonio. Verdadero o falso: puedo completar con mi imaginación lo que la comunidad no contó.", "Falso", "Eso sería inventar."),
        ex("Tema: el patrimonio. ¿Qué escribes cuando el testimonio no explica algo? Escribe una frase corta.", "El testimonio no lo dice", "Es la manera honesta de marcar un vacío."),
    ],
    task=T("Lee este testimonio inventado de doña Ximena, de Villa Ferroviaria: «Mi abuelo trabajó en el tren y guardó su farol. Lo mostramos en la fiesta de la estación una vez al año. También recordamos los silbidos del tren antiguo. Hay fotos que guardamos y no mostramos.» Haz cuatro columnas: «La fuente dice», «Tipo de patrimonio», «Yo interpreto» y «No se cuenta». Pon al menos un dato en cada una. Cierra con una frase de límites.",
           "La fuente dice: su abuelo trabajó en el tren y guardó su farol, que muestran en la fiesta de la estación; recuerdan los silbidos del tren antiguo. Tipo: el farol es material; los silbidos recordados, inmateriales. Yo interpreto: yo pienso que mostrar el farol una vez al año ayuda a recordar. No se cuenta: las fotos que no muestran. Límite: no sé cuándo es la fiesta.",
           ["separa cuatro columnas", "distingue material e inmaterial", "marca sus ideas como interpretación"], ["tabla de cuatro columnas", "frase de límites"], ["escribir interpretaciones como datos", "inventar lo no mostrado"],
           "Pedir que indique en qué línea del testimonio está cada dato; valorar que deje sin completar lo no contado."),
    reinforce="Subraya con un color lo que dice la fuente y con otro lo que interpretas en el testimonio de doña Ximena.",
    extend="Explica por qué guardar algunas fotos sin mostrarlas puede ser una manera de cuidar un patrimonio.",
)

L(
    OA15, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre el patrimonio, quienes lo cuidan y lo que lo amenaza en dos comunidades inventadas, y a compararlas sin decir que un patrimonio vale más que otro.",
    prior=["Sé leer un testimonio con límites.", "Sé distinguir patrimonio material de inmaterial."],
    explain=[
        "Un patrimonio se relaciona con tres cosas: las personas que lo cuidan, las prácticas con que se cuida y las amenazas que enfrenta. Por ejemplo, un muro se relaciona con las familias que lo reparan cada año y con el riesgo de que alguien se lleve piedras. Un cuento se relaciona con quienes lo cuentan y con el riesgo de que deje de contarse.",
        "Comparamos dos testimonios inventados: el de don Anselmo, de Pueblo Piedra, y el de doña Ximena, de Villa Ferroviaria, un pueblo no indígena. En ambos, los vecinos cuidan un bien material y guardan recuerdos inmateriales. En ambos, personas de afuera se llevan recuerdos y eso les duele. Hay diferencias: un muro de piedra y canciones frente a una estación y cuentos del tren.",
        "Para comparar usamos los mismos criterios: qué patrimonio material y cuál inmaterial hay, quién lo cuida y qué lo amenaza. No decimos que un patrimonio valga más que otro. Y dos testimonios no bastan para decir que todos los pueblos cuidan igual su patrimonio.",
    ],
    vocab=[("amenaza", "algo que puede dañar o hacer perder el patrimonio"), ("cuidar", "hacer lo necesario para que algo no se pierda ni se dañe"), ("semejanza", "algo parecido entre dos patrimonios"), ("diferencia", "algo distinto entre dos patrimonios"), ("criterio", "punto de comparación igual para los dos casos")],
    worked=[
        W("Relacionar patrimonio, cuidado y amenaza", TPP + " ¿Qué relación hay entre el muro, quienes lo cuidan y lo que lo amenaza?", ["El muro lo reparan entre todos cada año: eso es el cuidado.", "Personas de afuera quieren llevarse piedras: eso es la amenaza.", "El cuidado comunitario responde a esa amenaza."], "El muro se cuida entre todos y la amenaza es que se lleven piedras como recuerdo."),
        W("Comparar con un criterio", TVF + " Criterio: «qué lo amenaza». Don Anselmo: que se lleven piedras. Doña Ximena: que se lleven clavos viejos. ¿Qué semejanza hay?", ["En Pueblo Piedra se llevan piedras como recuerdo.", "En Villa Ferroviaria se llevan clavos viejos como recuerdo.", "En ambos casos alguien se lleva partes del patrimonio como recuerdo."], "Semejanza: en ambos casos se llevan partes del patrimonio como recuerdo."),
    ],
    mistakes=[
        M("Decir que el patrimonio de una comunidad vale más que el de otra.", "Comparar no es ordenar por valor.", "Describe semejanzas y diferencias con los mismos criterios."),
        M("Concluir que todos los pueblos cuidan su patrimonio igual porque dos testimonios se parecen.", "Dos ejemplos no representan a todos los pueblos.", "Escribe «en estos dos testimonios» y no más."),
    ],
    R=[
        ex("¿Qué cuidan los vecinos de Villa Ferroviaria: la estación antigua o el muro de piedra?", "La estación antigua", "El muro es de Pueblo Piedra."),
        ex("En Pueblo Piedra, ¿quiénes reparan el muro cada año? A) una empresa B) toda la comunidad", "B", "Don Anselmo dice que lo reparan entre todos."),
        ex("¿Qué se llevan de recuerdo en Villa Ferroviaria: clavos viejos o piedras?", "Clavos viejos", "Las piedras son de Pueblo Piedra."),
    ],
    C=[
        ex("Verdadero o falso: comparar dos patrimonios significa decir cuál vale más.", "Falso", "Comparar es buscar semejanzas y diferencias."),
        ex("¿Qué es un criterio de comparación? A) un punto igual para los dos patrimonios, como «qué lo amenaza» B) la opinión de quien compara", "A", "El criterio permite comparar con el mismo punto."),
        ex("Verdadero o falso: si dos comunidades cuidan algo parecido, todos los pueblos cuidan igual su patrimonio.", "Falso", "Dos casos no representan a todos los pueblos."),
    ],
    A=[
        ex("Criterio: «quién lo cuida». Pueblo Piedra: la comunidad. Villa Ferroviaria: los vecinos. ¿Qué semejanza hay? A) en ambos lo cuida un grupo de vecinos B) en ambos lo cuida una sola persona", "A", "Los dos testimonios hablan de cuidado colectivo."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) ambas comunidades guardan recuerdos inmateriales b) una cuida un muro y la otra, una estación.", "a semejanza, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        ex("Doña Ximena dice: «Cada año repintamos las bancas». ¿Qué práctica de cuidado muestra? A) abandono del patrimonio B) mantenimiento anual del patrimonio", "B", "Repintar cada año es mantener."),
    ],
    Z=[
        ex("Ana dice: «El patrimonio de Villa Ferroviaria vale menos porque es más reciente». ¿Qué falla en su comparación?", "Ordena por valor sin criterio ni fuente", "Comparar no es jerarquizar."),
        ex("Un compañero escribe: «Como en estos dos casos se llevan recuerdos, en todo el país pasa lo mismo». ¿Qué debería escribir? A) «en todo el país» B) «en estos dos testimonios»", "B", "Dos testimonios no representan al país."),
    ],
    D=[
        ex("Dos conclusiones. 1) «En estos dos testimonios, los vecinos cuidan un bien material y guardan recuerdos inmateriales». 2) «Los pueblos indígenas cuidan mejor su patrimonio que los demás». ¿Cuál está bien formulada?", "La primera", "La segunda ordena a dos grupos."),
        ex("Alguien dice que Villa Ferroviaria «hace una procesión con el farol». El testimonio solo dice que muestran el farol en la fiesta de la estación una vez al año. ¿Qué parte es interpretación? A) la procesión B) la fiesta de la estación", "A", "El testimonio no habla de procesión."),
    ],
    context=[ex("Tu curso arma un panel sobre cuidar el patrimonio. Una compañera quiere titularlo «Los indígenas cuidan y los demás, no». ¿Qué título respeta lo aprendido? A) «Quién cuida mejor» B) «Dos comunidades cuidan su patrimonio de distintas maneras»", "B", "El título A compara sin jerarquizar.")],
    selfcheck=[
        ex("Escribe una relación entre un patrimonio, su cuidado y su amenaza con el testimonio de don Anselmo.", "El muro se repara entre todos y la amenaza es que se lleven piedras", "Une patrimonio, cuidado y amenaza."),
        ex("Verdadero o falso: puedo ordenar dos patrimonios de más a menos valioso.", "Falso", "Cada comunidad valora el suyo."),
        ex("Nombra un criterio de comparación para dos patrimonios.", "Por ejemplo: qué lo amenaza", "Debe ser un punto igual para ambos."),
    ],
    task=T("Compara estos dos patrimonios inventados. Pueblo Piedra (don Anselmo): «Cuidamos un muro de piedra entre todos y guardamos canciones de trabajo; nos preocupa que se lleven piedras». Villa Ferroviaria (doña Ximena): «Cuidamos la estación entre los vecinos y guardamos cuentos del tren; nos preocupa que se lleven clavos viejos». Haz una tabla con tres criterios: «patrimonio material e inmaterial», «quién lo cuida» y «qué lo amenaza». Escribe una semejanza, una diferencia y una frase que termine con «en estos dos testimonios».",
           "Material e inmaterial: muro y canciones; estación y cuentos. Quién cuida: la comunidad; los vecinos. Amenaza: que se lleven piedras; que se lleven clavos viejos. Semejanza: en ambos casos los vecinos cuidan juntos y les preocupa que se lleven partes. Diferencia: un patrimonio es un muro con canciones y el otro, una estación con cuentos. Esto se ve en estos dos testimonios.",
           ["usa los mismos criterios para ambos", "distingue semejanza y diferencia", "no jerarquiza"], ["tabla de tres criterios", "semejanza y diferencia"], ["decir cuál patrimonio vale más", "generalizar a todos los pueblos"],
           "Pedir que muestre en la tabla la fila que respalda cada semejanza; valorar que no ordene los patrimonios."),
    reinforce="Marca en la tabla con un color las semejanzas y con otro las diferencias.",
    extend="Agrega un cuarto criterio (por ejemplo, «qué se comparte con visitantes») y explica qué deberías preguntar para completarlo.",
)

L(
    OA15, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida que conozca y valore un patrimonio cultural, con fuente, reflexión, límite, pregunta y una propuesta de cuidado.",
    prior=["Sé relacionar patrimonio, cuidado y amenaza.", "Sé comparar dos patrimonios sin jerarquizar."],
    explain=[
        "Una respuesta atribuida sobre patrimonio tiene cinco partes. Primero, el dato de la fuente con su nombre: «Don Anselmo cuenta que…». Segundo, el tipo de patrimonio: material o inmaterial. Tercero, el cuidado y la amenaza que aparecen. Cuarto, tu reflexión con «yo pienso que» y un límite. Quinto, una pregunta para el educador tradicional y una propuesta de cuidado respetuosa.",
        "Una propuesta de cuidado es una idea concreta para proteger el patrimonio sin dañarlo ni quitárselo a la comunidad. Por ejemplo: visitarlo con permiso, no sacar piezas, pedir a la comunidad cómo prefiere que se hable de él y reconocer siempre quién lo cuida. Una propuesta nunca decide por la comunidad: solo invita.",
        "Una buena respuesta no exagera, no inventa canciones ni lugares y no habla por todo un pueblo. Reconoce lo que no sabe y respeta lo que la comunidad resguarda. Al final se devuelve a la comunidad o al educador, para que la revise y corrija lo que no esté bien dicho.",
    ],
    vocab=[("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("propuesta de cuidado", "idea concreta para proteger un patrimonio sin dañarlo ni quitárselo a su comunidad"), ("reconocer", "decir quién cuida o creó algo"), ("exagerar", "decir más de lo que la fuente dijo"), ("devolución", "mostrar el trabajo a la comunidad o al educador para que lo revisen")],
    worked=[
        W("Armar una respuesta", TPP + " Arma una respuesta atribuida de cinco partes.", ["Dato: don Anselmo cuenta que reparan el muro cada año entre todos y guardan canciones de trabajo.", "Tipo: el muro es patrimonio material; las canciones, inmaterial.", "Cuidado y amenaza: cuidan reparando; la amenaza es que se lleven piedras.", "Reflexión, límite, pregunta y propuesta: yo pienso que reparar entre todos mantiene el muro vivo; no sé qué canciones guardan; propongo visitar con permiso y no sacar piedras; preguntaré al educador tradicional."], "Respuesta con dato atribuido, tipo de patrimonio, cuidado y amenaza, reflexión con límite, pregunta y propuesta."),
        W("Revisar una propuesta", "Una niña propone: «Llevemos piedras del muro a la escuela para hacer un museo». ¿Es una buena propuesta de cuidado?", ["Sacar piedras daña el muro.", "No pide permiso a la comunidad.", "Va contra lo que don Anselmo dice que no les gusta."], "No: daña el patrimonio y no respeta lo que la comunidad pide."),
    ],
    mistakes=[
        M("Proponer sacar piezas de un patrimonio para «protegerlo» en otro lugar.", "Daña el patrimonio y desconoce a la comunidad.", "Propón visitar con permiso y reconocer a quien lo cuida."),
        M("No marcar qué parte es opinión mía.", "El lector no distingue la voz de la comunidad de la mía.", "Usa «yo pienso que…»."),
    ],
    R=[
        ex("¿Con qué frase atribuyes un dato a don Anselmo? A) «Todos saben que…» B) «Don Anselmo cuenta que…»", "B", "Nombra a la fuente."),
        ex("Tema: el patrimonio. ¿Cuántas partes tiene la respuesta atribuida de esta clase? Escribe el número.", "5", "Son dato, tipo de patrimonio, cuidado y amenaza, reflexión con límite, y pregunta con propuesta."),
        ex("Tema: el patrimonio. Verdadero o falso: mi reflexión es una idea mía y no del testimonio.", "Verdadero", "Por eso se marca como mía."),
    ],
    C=[
        ex("¿Qué es una propuesta de cuidado? A) una idea para proteger un patrimonio sin dañarlo ni quitárselo a su comunidad B) una orden a la comunidad", "A", "Invita; no ordena."),
        ex("Verdadero o falso: una propuesta de cuidado puede decidir por la comunidad qué mostrar.", "Falso", "La comunidad decide qué comparte."),
        ex("Tema: el patrimonio. ¿Para qué sirve el límite? A) para ocultar errores B) para decir qué no sé ni se cuenta", "B", "El límite muestra hasta dónde llega lo afirmado."),
    ],
    A=[
        ex("Testimonio de doña Ximena: «Cada año repintamos las bancas». Completa la atribución: «Doña Ximena cuenta que cada año…»", "Repintan las bancas", "Se repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) don Anselmo cuenta que cada año reparan el muro b) yo pienso que reparar entre todos hace que lo sientan suyo.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        ex("Una propuesta dice: «Visitemos el muro con permiso, no saquemos piedras y digamos que lo cuida Pueblo Piedra». ¿Qué cumple? A) permiso, no dañar y reconocer B) sacar piezas", "A", "La propuesta incluye los tres cuidados."),
    ],
    Z=[
        ex("Tema: el patrimonio. Marta escribe una respuesta sin límite. ¿Qué mejoraría? A) agregar más datos inventados B) agregar lo que no sé o no se cuenta", "B", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu respuesta al educador tradicional? A) porque conoce el patrimonio de su pueblo y puede corregir errores B) porque es una tarea de decoración", "A", "Quien conoce su cultura puede corregir lo equivocado."),
    ],
    D=[
        ex("Dos reflexiones. 1) «Don Anselmo cuenta que reparan el muro entre todos; yo pienso que eso une a la comunidad». 2) «Don Anselmo demuestra que su muro es el patrimonio más importante del país». ¿Cuál está bien construida?", "La primera", "La segunda exagera y jerarquiza."),
        ex("Un compañero agrega que Pueblo Piedra «seguro tiene un tesoro escondido». El testimonio no lo menciona. ¿Qué debe hacer?", "Quitarlo porque no está en la fuente", "Lo que la fuente no dijo no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre cómo cuida su patrimonio Pueblo Piedra. ¿Qué empieza mejor? A) «Don Anselmo cuenta que…» B) «Todos los pueblos indígenas cuidan su patrimonio…»", "A", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cinco partes de una respuesta atribuida sobre patrimonio.", "Dato de la fuente, tipo de patrimonio, cuidado y amenaza, reflexión con límite, y pregunta con propuesta", "Están en la explicación."),
        ex("Tema: el patrimonio. Verdadero o falso: debo marcar qué parte es mi opinión.", "Verdadero", "Así no se confunde con la fuente."),
        ex("Tema: el patrimonio. ¿Qué haces al terminar? A) mostrarlo a la comunidad o al educador para que lo revise B) guardarlo sin mostrarlo", "A", "Es la devolución."),
    ],
    task=T("Usa este testimonio inventado de doña Ximena: «En Villa Ferroviaria cuidamos la estación entre los vecinos. Cada año hacemos una limpieza y contamos cuentos del tren a los niños. Algunas personas se llevan objetos de recuerdo. Hay fotos que no mostramos.» Escribe una respuesta de cinco partes: 1) dato de doña Ximena, 2) tipo de patrimonio, 3) cuidado y amenaza, 4) tu reflexión con «yo pienso que» y un límite, 5) una pregunta para el educador tradicional y una propuesta de cuidado que invite sin decidir por la comunidad.",
           "1) Doña Ximena cuenta que cuidan la estación, la limpian cada año y cuentan cuentos del tren a los niños. 2) La estación es patrimonio material; los cuentos, inmaterial. 3) Cuidan limpiando; la amenaza es que se llevan objetos. 4) Yo pienso que contar cuentos a los niños mantiene viva la historia; no sé qué fotos guardan. 5) Pregunta: ¿cómo cuidan su patrimonio los pueblos indígenas? Propuesta: visitar con permiso y no llevarse objetos.",
           ["atribuye cada dato", "distingue tipos y amenazas", "propone sin decidir por la comunidad"], ["texto de cinco partes"], ["generalizar a todos los pueblos", "proponer sacar piezas"],
           "Pedir que señale la línea del testimonio que respalda su reflexión."),
    reinforce="Numera del 1 al 5 las partes de tu respuesta para comprobar que están todas.",
    extend="Reescribe tu propuesta de cuidado para el muro de Pueblo Piedra usando el testimonio de don Anselmo.",
)

L(
    OA15, 5, materials=MAT,
    use="Aprenderé a contrastar sin jerarquizar tres patrimonios: uno inventado de una comunidad indígena, uno de un pueblo no indígena y ejemplos reconocidos por la UNESCO. Así veré que un reconocimiento no hace que otros valgan menos.",
    prior=["Sé armar una respuesta atribuida.", "Sé comparar dos patrimonios con criterios iguales."],
    explain=[
        "Contrastar es poner varios patrimonios uno al lado del otro para ver en qué coinciden y en qué se diferencian. Sin jerarquizar quiere decir que no los ordenamos de «más valioso» a «menos valioso». Cada patrimonio importa para quienes lo cuidan, tenga o no un reconocimiento oficial.",
        "La UNESCO es un organismo internacional que reconoce algunos sitios como Patrimonio Mundial. En 1995 declaró Patrimonio Mundial el Parque Nacional Rapa Nui, en Chile. En 2021 declaró Patrimonio Mundial los asentamientos y la momificación artificial de la cultura Chinchorro, en el norte de Chile. Estos son ejemplos de patrimonio de pueblos indígenas con un reconocimiento internacional.",
        "Que un patrimonio tenga ese reconocimiento no significa que otros valgan menos: el muro de una comunidad pequeña también importa para quienes lo cuidan. Para contrastar usamos criterios iguales y, si queremos conocer un patrimonio real, buscamos fuentes confiables y preguntamos a la comunidad y al educador tradicional.",
    ],
    vocab=[("UNESCO", "organismo internacional que, entre otras tareas, reconoce sitios como Patrimonio Mundial"), ("Patrimonio Mundial", "reconocimiento internacional a un sitio por su valor para la humanidad"), ("contrastar", "poner varios patrimonios juntos para ver en qué coinciden y en qué se diferencian"), ("jerarquizar", "ordenar de más a menos valioso"), ("criterio", "punto de comparación igual para todos")],
    worked=[
        W("Contrastar tres patrimonios", "Pueblo Piedra: un muro y canciones; lo cuida la comunidad. Villa Ferroviaria: una estación y cuentos; la cuidan los vecinos. Parque Nacional Rapa Nui: reconocido por la UNESCO como Patrimonio Mundial. Criterio: «quién lo cuida o lo reconoce». ¿En qué coinciden los dos primeros?", ["Pueblo Piedra lo cuida la comunidad.", "Villa Ferroviaria lo cuidan los vecinos.", "En los dos, lo cuida un grupo de personas de la misma comunidad."], "Los dos primeros coinciden en que los cuida un grupo de vecinos de la comunidad."),
        W("Evitar una jerarquía", "Un niño dice: «Como Rapa Nui es Patrimonio Mundial, el muro de Pueblo Piedra no importa». ¿Qué error hay?", ["Un reconocimiento internacional no quita valor a otros patrimonios.", "El muro importa para quienes lo cuidan.", "Comparar no es ordenar por valor."], "Jerarquiza por el reconocimiento oficial: el muro importa para quienes lo cuidan."),
    ],
    mistakes=[
        M("Pensar que solo es patrimonio lo que reconoce la UNESCO.", "Cada comunidad tiene patrimonio, tenga o no ese reconocimiento.", "Valora el patrimonio por lo que significa para quienes lo cuidan."),
        M("Decir que contrastar significa que todos los patrimonios son iguales.", "Cada uno tiene su propia historia y sentido.", "Compara con criterios iguales y anota semejanzas y diferencias."),
    ],
    R=[
        ex("¿En qué año la UNESCO declaró Patrimonio Mundial el Parque Nacional Rapa Nui?", "1995", "Así lo indica la explicación de la clase."),
        ex("¿En qué año la UNESCO declaró Patrimonio Mundial los asentamientos y la momificación artificial de la cultura Chinchorro?", "2021", "Así lo indica la explicación de la clase."),
        ex("Contrastar, ¿es poner patrimonios juntos para ver coincidencias y diferencias o es elegir el más valioso?", "Poner patrimonios juntos para ver coincidencias y diferencias", "Contrastar no es elegir el más valioso."),
    ],
    C=[
        ex("Verdadero o falso: un patrimonio sin reconocimiento de la UNESCO no es patrimonio.", "Falso", "Cada comunidad tiene patrimonio, tenga o no ese reconocimiento."),
        ex("¿Por qué se usan criterios iguales para los tres patrimonios? A) para llenar la tabla B) para no tratar a uno mejor que otro", "B", "Los criterios iguales evitan el trato desigual."),
        ex("Verdadero o falso: tres ejemplos bastan para describir el patrimonio de todos los pueblos.", "Falso", "Tres ejemplos no representan a todos."),
    ],
    A=[
        arith("La UNESCO declaró Patrimonio Mundial el Parque Nacional Rapa Nui en 1995 y la cultura Chinchorro en 2021. ¿Cuántos años pasaron entre ambos reconocimientos?", "2021-1995", "Se restan los años."),
        ex("Clasifica en COINCIDENCIA o DIFERENCIA: a) los tres patrimonios son cuidados o reconocidos por personas que valoran su importancia b) solo uno de ellos, Rapa Nui, tiene reconocimiento de la UNESCO.", "a coincidencia, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        ex("Un joven dice: «El muro de Pueblo Piedra vale menos porque no es Patrimonio Mundial». ¿Qué falla? A) ordena por valor según un reconocimiento B) usa el nombre del pueblo", "A", "Contrastar no es jerarquizar."),
    ],
    Z=[
        ex("Ana dice: «Lo único importante de los pueblos indígenas es lo que reconoce la UNESCO». ¿Qué evidencia de la clase la contradice?", "El muro y las canciones de Pueblo Piedra también importan a su comunidad", "Un patrimonio importa sin reconocimiento oficial."),
        ex("Un compañero concluye: «Como Rapa Nui y Chinchorro son indígenas y famosos, todo patrimonio indígena es famoso». ¿Qué debería escribir? A) «estos dos casos son reconocidos por la UNESCO» B) «todos son famosos»", "A", "Dos casos no representan a todos."),
    ],
    D=[
        ex("Dos conclusiones. 1) «En estos tres ejemplos, el patrimonio importa para quienes lo cuidan o lo reconocen». 2) «El patrimonio con reconocimiento internacional es mejor». ¿Cuál está bien formulada?", "La primera", "La segunda ordena sin criterio."),
        ex("Un grupo quiere visitar un sitio de una comunidad real. ¿Qué hace primero? A) pedir permiso y preguntar cómo prefiere la comunidad que se visite B) llegar sin avisar", "A", "El patrimonio tiene cuidadores que deciden cómo se visita."),
    ],
    context=[ex("En tu curso hacen una lista de «los patrimonios más importantes del país». Una compañera dice que solo deben aparecer los reconocidos por la UNESCO. ¿Qué le propones? A) dejar solo los reconocidos B) incluir también patrimonios locales y explicar por qué importan a sus comunidades", "B", "Los patrimonios locales también importan.")],
    selfcheck=[
        ex("Escribe qué es la UNESCO con tus palabras.", "Un organismo internacional que reconoce sitios como Patrimonio Mundial", "Es la definición de la clase."),
        ex("Verdadero o falso: puedo ordenar tres patrimonios de más a menos valioso.", "Falso", "Contrastar no es jerarquizar."),
        ex("Nombra un criterio de contraste para tres patrimonios.", "Por ejemplo: quién lo cuida o lo reconoce", "Debe ser un punto igual para todos."),
    ],
    task=T("Contrasta estos tres patrimonios. Pueblo Piedra (inventado, don Anselmo): «Un muro de piedra y canciones de trabajo; lo cuida la comunidad». Villa Ferroviaria (inventado, doña Ximena): «Una estación y cuentos del tren; la cuidan los vecinos». Parque Nacional Rapa Nui (real): «Reconocido por la UNESCO en 1995 como Patrimonio Mundial». Haz una tabla con tres criterios: «qué patrimonio es», «quién lo cuida o lo reconoce» y «qué sabemos de su cuidado» (si no lo dice, escribe «no lo dice»). Escribe una coincidencia, una diferencia y una frase que muestre cómo evitarías decir que uno vale más.",
           "Qué es: muro y canciones; estación y cuentos; un parque nacional. Quién cuida o reconoce: la comunidad; los vecinos; la UNESCO. Qué sabemos del cuidado: la comunidad lo repara; los vecinos limpian; no lo dice. Coincidencia: los tres importan para quienes los cuidan o reconocen. Diferencia: solo uno es Patrimonio Mundial. Para no jerarquizar, diría que cada uno importa a su manera.",
           ["usa los mismos criterios para los tres", "distingue coincidencia y diferencia", "escribe «no lo dice» donde corresponde"], ["tabla de tres criterios", "coincidencia, diferencia y frase"], ["decir cuál vale más", "inventar datos de Rapa Nui"],
           "Pedir que muestre en la tabla la fila que respalda cada afirmación; valorar que no invente datos de un patrimonio real."),
    reinforce="Marca en la tabla con un color las coincidencias y con otro las diferencias.",
    extend="Explica por qué un patrimonio puede ser importante para su comunidad aunque nadie fuera de ella lo conozca.",
)

# ------------------------------------------------------------------ OA 16
FCC = ("Ficha situada (inventada). Comunidad: Cumbre Clara (no es un pueblo real). Territorio: una cumbre con cielo despejado, chacras y una vertiente. "
       "Fuente y responsable: doña Aurora, vecina de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Aurora autorizó usar esta ficha en la escuela. "
       "Límite: no se cuentan los conocimientos que la comunidad enseña solo a sus jóvenes.")
TCC = ("Testimonio inventado de doña Aurora, de Cumbre Clara: «Mi abuelo miraba la Luna y las plantas para saber cuándo sembrar. Anotaba cuántos días pasaban entre una luna llena y la siguiente. "
       "Para nosotros lo que pasa en el cielo y lo que pasa en la tierra están relacionados. Hay conocimientos que solo se enseñan en la comunidad.»")

L(
    OA16, 1, materials=MAT,
    use="Aprenderé a situar un conocimiento de la relación entre el ser humano, la naturaleza y el cosmos: de qué comunidad es, quién lo cuenta y qué no se cuenta. Sirve para valorar la ciencia desde la perspectiva indígena sin hablar por otros.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que cada pueblo entiende el cosmos a su manera."],
    explain=[
        "La ciencia es el conjunto de conocimientos que se obtienen observando con atención, anotando lo que se ve, repitiendo las observaciones y sacando conclusiones. Muchos pueblos indígenas han construido conocimientos de ese tipo a lo largo del tiempo: observan el cielo, las plantas, el agua y los animales, y usan lo que aprenden para decidir cuándo sembrar, cuándo pescar o cómo cuidar un lugar.",
        "La perspectiva indígena de la ciencia suele unir lo que se observa con una manera de entender la relación entre el ser humano, la naturaleza y el cosmos: lo que pasa en el cielo y lo que pasa en la tierra no están separados. Cada pueblo la formula a su manera y la transmite de forma oral, practicando y acompañando a los mayores.",
        "Una manifestación es una forma de expresar lo que se piensa o se siente: un relato, un dibujo, una canción, un esquema, un tejido. Podemos valorar el conocimiento de una comunidad y expresar lo que aprendimos con una manifestación propia. Antes hay que situarlo: la ficha situada dice la comunidad, la fuente, el permiso y el límite.",
    ],
    vocab=[("ciencia", "conocimientos que se obtienen observando, anotando, repitiendo y sacando conclusiones"), ("observar", "mirar con atención para aprender de lo que se ve"), ("cosmos", "universo que rodea a las personas, que cada cultura entiende a su manera"), ("manifestación", "forma de expresar lo que se piensa o se siente, como un dibujo o un relato"), ("fuente", "persona o texto que entrega el dato")],
    worked=[
        W("Leer una ficha situada", FCC + " ¿De quién es el conocimiento y qué no se cuenta?", ["La comunidad es Cumbre Clara y la fuente es doña Aurora.", "Ella dio permiso para usar la ficha en la escuela.", "El límite dice que no se cuentan los conocimientos reservados a los jóvenes."], "El conocimiento es de doña Aurora, de Cumbre Clara; no se cuentan los conocimientos reservados a los jóvenes."),
        W("Reconocer observación y uso", "Doña Aurora cuenta que su abuelo miraba la Luna y las plantas para saber cuándo sembrar. ¿Qué es la observación y qué es el uso?", ["Observar es mirar la Luna y las plantas.", "Usar lo observado es decidir cuándo sembrar."], "Observación: mirar la Luna y las plantas. Uso: decidir cuándo sembrar."),
    ],
    mistakes=[
        M("Pensar que el conocimiento indígena no es ciencia porque no está en un libro.", "La ciencia se basa en observar, anotar y concluir, sea oral o escrita.", "Busca la observación, el registro y el uso."),
        M("Decir que el conocimiento de Cumbre Clara es el de todos los pueblos indígenas.", "La ficha habla de una sola comunidad.", "Escribe «según doña Aurora, en Cumbre Clara…»."),
    ],
    R=[
        ex("Según la ficha de Cumbre Clara, ¿quién es la fuente?", "Doña Aurora", "La ficha la nombra como fuente y responsable."),
        ex("¿Qué territorio tiene Cumbre Clara? A) una caleta con puerto B) una cumbre con cielo despejado, chacras y una vertiente", "B", "La caleta y el puerto son de otras fichas."),
        ex("La ficha de Cumbre Clara dice que no se cuentan los conocimientos reservados a los jóvenes. ¿Los inventas para completar tu trabajo? Responde Sí o No.", "No", "El límite de la ficha lo prohíbe."),
    ],
    C=[
        ex("En Lengua y Cultura, ¿qué hace la ciencia? A) obtiene conocimientos observando, anotando, repitiendo y concluyendo B) solo memoriza datos", "A", "Esos son sus pasos centrales."),
        ex("Verdadero o falso: un conocimiento transmitido oralmente no puede ser ciencia.", "Falso", "Lo que importa es observar, registrar y concluir, sea oral o escrito."),
        ex("Verdadero o falso: el conocimiento de Cumbre Clara sirve para hablar de todos los pueblos indígenas.", "Falso", "Una comunidad no representa a todos los pueblos."),
    ],
    A=[
        ex("Clasifica en OBSERVACIÓN o USO: a) mirar la forma de la Luna cada noche b) decidir cuándo sembrar según lo observado.", "a observación, b uso", "Mirar es observar; decidir es usar lo aprendido."),
        ex("Doña Aurora dice: «Anotaba cuántos días pasaban entre una luna llena y la siguiente». ¿Qué paso de la ciencia muestra? A) adivinar B) registrar lo observado", "B", "Anotar es registrar."),
        ex("Una compañera trae una ficha con comunidad y fuente, pero sin límite. ¿Qué falta? A) la hora del día B) lo que no se puede contar", "B", "El límite dice qué no se cuenta."),
    ],
    Z=[
        ex("Pablo escribe: «Como el abuelo de doña Aurora miraba la Luna, todos los pueblos indígenas siembran por la Luna». ¿Qué error comete?", "Generaliza un caso a todos los pueblos", "Un testimonio no representa a todos los pueblos."),
        ex("¿Por qué conviene situar la fuente antes de valorar un conocimiento? A) porque cada comunidad lo formula a su manera B) para escribir más rápido", "A", "Situar muestra de quién es el conocimiento."),
    ],
    D=[
        ex("Una ficha dice solo: «Comunidad: Cumbre Clara. Conocimiento: observar la Luna». ¿Qué datos faltan?", "Fuente, permiso y límite", "La ficha situada exige esos tres datos además de comunidad y territorio."),
        arith("Doña Aurora anota que una luna llena fue el día 3 de un mes de 30 días y la siguiente fue el día 2 del mes que sigue. ¿Cuántos días pasaron entre ambas?", "(30-3)+2", "Se suman los días que faltan para terminar el mes y los del mes siguiente."),
    ],
    context=[ex("Un compañero quiere decir en su trabajo que una comunidad real «sabe cuándo llueve mirando la Luna». No tiene ninguna fuente. ¿Qué haces? A) pregunto de dónde viene ese dato y consulto al educador tradicional B) lo escribo porque suena bien", "A", "Sin fuente no se afirma nada sobre una comunidad.")],
    selfcheck=[
        ex("Nombra dos pasos que usa la ciencia para obtener conocimientos.", "Dos entre: observar, anotar, repetir, concluir", "Son los pasos de la explicación."),
        ex("Verdadero o falso: una manifestación puede ser un dibujo, un relato o una canción.", "Verdadero", "Es una forma de expresar lo que se piensa o se siente."),
        ex("Ante una duda sobre un conocimiento de una comunidad real, ¿qué haces? A) pregunto al educador tradicional B) lo supongo", "A", "Él o ella es la fuente."),
    ],
    task=T("Lee esta nota inventada de doña Aurora: «En Cumbre Clara mi abuelo miraba el cielo de noche y las hojas de las plantas por la mañana. Con eso decidía cuándo sembrar. Hay conocimientos que damos solo a los jóvenes.» Haz una ficha con: comunidad, fuente, qué observaba, para qué lo usaba, qué dice la fuente y un límite. Luego escribe una frase con «Yo pienso que…» sobre qué relación ve doña Aurora entre el cielo y la tierra.",
           "Comunidad: Cumbre Clara. Fuente: doña Aurora. Observaba: el cielo de noche y las hojas de las plantas. Lo usaba para: decidir cuándo sembrar. Dice: su abuelo decidía cuándo sembrar mirando el cielo y las plantas. Límite: no se cuentan los conocimientos reservados a los jóvenes. Yo pienso que doña Aurora ve el cielo y la tierra como parte de un mismo conocimiento para vivir.",
           ["completa la ficha con datos de la nota", "separa la fuente de su opinión", "pone un límite"], ["ficha completa", "frase con «Yo pienso que»"], ["inventar los conocimientos reservados", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea de la nota está cada dato; valorar que respete el límite."),
    reinforce="Subraya en la ficha de Cumbre Clara la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué observar con atención es el primer paso de cualquier ciencia.",
)

L(
    OA16, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre ciencia desde la perspectiva indígena con límites declarados: qué dice la fuente, qué observa y registra, qué interpreto yo y qué no se cuenta.",
    prior=["Sé situar un conocimiento con su ficha.", "Sé que la ciencia observa, anota y concluye."],
    explain=[
        "Un testimonio sobre ciencia desde una comunidad puede contar qué se observa, cómo se registra, para qué se usa y cómo se enseña. Para leerlo con respeto separamos cuatro cosas. Lo que la fuente dice, con sus palabras. Lo que se observa, se registra o se usa. Lo que yo interpreto, que es una idea mía. Y lo que no se cuenta o no sé.",
        "En el testimonio de doña Aurora, mirar la Luna y las plantas es observar, anotar los días entre una luna llena y la siguiente es registrar, y decidir cuándo sembrar es usar lo aprendido. Además dice que lo que pasa en el cielo y lo que pasa en la tierra están relacionados. No cuenta cómo explican esa relación. Si yo agrego una explicación, estoy inventando. Un dato de ciencia: entre una luna llena y la siguiente pasan alrededor de 29 o 30 días (unos 29,5 en promedio), así que una cuenta de 29 o 30 es razonable.",
        "Leer con límites declarados significa decir hasta dónde llega lo que afirmo. Los conocimientos que la comunidad enseña solo a sus jóvenes se respetan y no se piden ni se describen. Si queremos saber más sobre cómo una comunidad real conoce el cielo y la tierra, preguntamos al educador o a la educadora tradicional.",
    ],
    vocab=[("registrar", "anotar lo observado para recordarlo y compararlo"), ("luna llena", "momento en que vemos la Luna completa e iluminada"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("relacionar", "unir dos cosas que se influyen o se explican entre sí"), ("límite", "lo que no se cuenta o no se sabe")],
    worked=[
        W("Separar cuatro cosas", TCC + " Separa lo que dice, lo que se observa o registra, lo que interpreto y lo que no se cuenta.", ["Dice: su abuelo miraba la Luna y las plantas para saber cuándo sembrar.", "Observa: la Luna y las plantas; registra: cuántos días pasan entre dos lunas llenas.", "Interpreto: yo pienso que anotar los días ayudaba a prever el momento de siembra.", "No se cuenta: cómo explican la relación entre el cielo y la tierra."], "Dice: miraba la Luna y las plantas. Observa y registra: la Luna y los días entre lunas llenas. Interpreto: anotar ayudaba a prever la siembra. No se cuenta: cómo explican la relación."),
        W("Detectar un agregado", "Un niño escribe: «Doña Aurora cuenta que la Luna hace crecer las plantas». ¿Está bien?", ["Reviso el testimonio: dice que el abuelo miraba la Luna y las plantas para saber cuándo sembrar.", "No dice que la Luna haga crecer las plantas.", "El niño agregó una explicación que la fuente no dio."], "No: agrega una explicación que doña Aurora no dio."),
    ],
    mistakes=[
        M("Agregar explicaciones que la fuente no dio.", "Se inventa un saber que la comunidad no contó.", "Escribe «el testimonio no lo dice»."),
        M("Escribir mi interpretación como si la hubiera dicho la fuente.", "Se atribuye a la comunidad algo que no dijo.", "Marca mis ideas con «yo pienso que»."),
    ],
    R=[
        ex("Según doña Aurora, ¿qué miraba su abuelo: la Luna y las plantas o los pájaros?", "La Luna y las plantas", "El testimonio lo dice así."),
        ex("Tema: la ciencia y el cosmos. Una interpretación, ¿es una idea mía o un dato de la fuente?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Si el testimonio no explica por qué el cielo y la tierra se relacionan, ¿qué escribes? A) el testimonio no lo dice B) por la fuerza de la Luna", "A", "No se inventan explicaciones."),
    ],
    C=[
        ex("Doña Aurora dice: «Anotaba cuántos días pasaban entre una luna llena y la siguiente». ¿Qué paso es? A) concluir B) registrar", "B", "Anotar es registrar."),
        ex("Verdadero o falso: puedo agregar una explicación probable si la fuente no la dio.", "Falso", "Eso sería inventar."),
        ex("Verdadero o falso: respetar lo que la comunidad enseña solo a sus jóvenes es parte de leer con límites.", "Verdadero", "Lo reservado no se pide ni se describe."),
    ],
    A=[
        ex("Doña Aurora dice: «Para nosotros lo que pasa en el cielo y en la tierra están relacionados». Clasifica en DICE LA FUENTE o INTERPRETO: a) cielo y tierra están relacionados b) por eso todos los pueblos miran el cielo.", "a dice la fuente, b interpreto", "La segunda generaliza y no está en el testimonio."),
        arith("En una anotación inventada, doña Aurora cuenta 29 días entre una luna llena y la siguiente. Si observa 3 ciclos seguidos iguales a ese, ¿cuántos días de observación son en total?", "3*29", "Se multiplica el número de ciclos por los días de cada uno."),
        ex("Un niño escribe: «Doña Aurora cuenta que las estrellas son sus antepasados». ¿Qué dato no está en el testimonio?", "Que las estrellas son sus antepasados", "El testimonio no habla de antepasados en el cielo."),
    ],
    Z=[
        ex("Rodrigo escribe, sin marcarlo: «El conocimiento de Cumbre Clara es más exacto que la ciencia de la escuela». ¿Qué debería hacer con esa frase?", "Quitarla porque ordena y no está en la fuente", "No está en el testimonio y jerarquiza."),
        ex("Tema: la ciencia y el cosmos. ¿Por qué conviene escribir los límites al final del trabajo? A) para llenar la hoja B) para mostrar hasta dónde llega lo afirmado", "B", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        ex("Dos frases. 1) «Doña Aurora cuenta que su abuelo anotaba los días entre lunas llenas». 2) «Doña Aurora cuenta que su abuelo anotaba los eclipses». ¿Cuál se queda en la fuente?", "La primera", "La segunda agrega algo que el testimonio no contiene."),
        ex("Doña Aurora no contó cuántos años observó su abuelo. ¿Qué escribes en los límites? A) no sé cuántos años observó B) observó por veinte años", "A", "Declarar lo que no sé evita inventar."),
    ],
    context=[ex("Para un afiche escolar, un compañero quiere dibujar un «calendario ancestral de Cumbre Clara» con símbolos. El testimonio no habla de símbolos. ¿Qué le dices? A) que lo dibuje con muchos símbolos B) que no lo invente porque el conocimiento de una comunidad no se inventa", "B", "No se inventan saberes que la fuente no cuenta.")],
    selfcheck=[
        ex("Nombra las cuatro cosas que separo al leer un testimonio sobre ciencia desde una comunidad.", "Lo que dice la fuente, lo que se observa o registra, lo que interpreto y lo que no se cuenta", "Son los pasos de la lectura con límites."),
        ex("Tema: la ciencia y el cosmos. Verdadero o falso: puedo completar con mi imaginación lo que la comunidad no contó.", "Falso", "Eso sería inventar."),
        ex("Tema: la ciencia y el cosmos. ¿Qué escribes cuando el testimonio no explica algo? Escribe una frase corta.", "El testimonio no lo dice", "Es la manera honesta de marcar un vacío."),
    ],
    task=T("Lee este testimonio inventado de doña Aurora: «Mi abuelo anotaba en una libreta cuántas noches pasaban entre luna llena y luna llena. Cuando los números se repetían, decía que podía confiar en su cuenta. Después miraba las plantas del huerto para decidir si sembraba. De otros conocimientos no hablamos con visitas.» Haz cuatro columnas: «La fuente dice», «Observa o registra», «Yo interpreto» y «No se cuenta». Pon al menos un dato en cada una. Cierra con una frase de límites.",
           "La fuente dice: su abuelo anotaba en una libreta cuántas noches pasaban entre lunas llenas y miraba las plantas del huerto antes de sembrar. Observa o registra: noches entre lunas llenas; las plantas. Yo interpreto: yo pienso que repetir la cuenta le daba seguridad. No se cuenta: los otros conocimientos. Límite: no sé cuántos números repetidos necesitaba.",
           ["separa cuatro columnas", "usa datos del testimonio", "marca sus ideas como interpretación"], ["tabla de cuatro columnas", "frase de límites"], ["escribir interpretaciones como datos", "inventar los conocimientos reservados"],
           "Pedir que indique en qué línea del testimonio está cada dato; valorar que deje sin completar lo no contado."),
    reinforce="Subraya con un color lo que dice la fuente y con otro lo que interpretas en el testimonio de doña Aurora.",
    extend="Explica por qué repetir una observación varias veces hace más confiable una conclusión.",
)

L(
    OA16, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre la ciencia escolar y la ciencia desde la perspectiva de una comunidad indígena inventada, viendo semejanzas y diferencias sin decir que una es mejor.",
    prior=["Sé leer un testimonio con límites.", "Sé que la ciencia observa, registra y concluye."],
    explain=[
        "La ciencia escolar y el conocimiento de una comunidad pueden dialogar. Ambos parten de observar con atención, registran lo que ven, repiten las observaciones y usan lo aprendido para decidir. Por ejemplo, un cuaderno de observación de la Luna en la escuela y la libreta del abuelo de doña Aurora cumplen un papel parecido.",
        "También hay diferencias. La ciencia escolar suele expresarse con medidas y explicaciones escritas que se comparten en libros. El conocimiento de una comunidad suele transmitirse oralmente y practicando, y puede incluir una manera de entender la relación entre el ser humano, la naturaleza y el cosmos que va más allá de los datos. Las dos son valiosas, y cada una se entiende desde su propia manera de conocer.",
        "Para comparar usamos los mismos criterios: qué se observa, cómo se registra, para qué se usa y cómo se transmite. No decimos que una sea «más científica» que la otra. Y dos testimonios no bastan para decir que todas las comunidades ni todas las escuelas trabajan igual.",
    ],
    vocab=[("diálogo de saberes", "encuentro respetuoso entre formas distintas de conocer"), ("medida", "número que dice cuánto mide o dura algo"), ("transmitir", "pasar un conocimiento de unas personas a otras"), ("semejanza", "algo parecido entre dos formas de conocer"), ("criterio", "punto de comparación igual para los dos casos")],
    worked=[
        W("Comparar con un criterio", "Escuela (inventada): un cuaderno donde una clase anota la forma de la Luna cada noche durante un mes. Cumbre Clara: el abuelo anota los días entre una luna llena y la siguiente. Criterio: «cómo se registra». ¿Qué semejanza hay?", ["La escuela anota en un cuaderno.", "El abuelo anota en una libreta.", "En los dos casos se registra por escrito lo observado."], "Semejanza: en ambos casos se anota por escrito lo observado."),
        W("Reconocer una diferencia", "Escuela: la clase comparte los datos en un informe escrito. Cumbre Clara: la comunidad transmite su conocimiento oralmente y practicando. Criterio: «cómo se transmite». ¿Qué diferencia hay?", ["La escuela transmite por informe escrito.", "La comunidad transmite oralmente y practicando.", "Las formas de transmitir son distintas."], "Diferencia: la escuela transmite por escrito; la comunidad, oralmente y practicando."),
    ],
    mistakes=[
        M("Decir que la ciencia escolar es «la verdadera ciencia» y el conocimiento de la comunidad no.", "Ambas observan, registran y concluyen a su manera.", "Compara con criterios iguales."),
        M("Concluir que todas las comunidades registran como Cumbre Clara.", "Dos ejemplos no representan a todos.", "Escribe «en estos dos casos»."),
    ],
    R=[
        ex("¿Qué anota el abuelo de doña Aurora: los días entre una luna llena y la siguiente o el precio de las semillas?", "Los días entre una luna llena y la siguiente", "Así lo dice el testimonio."),
        ex("En el ejemplo de la escuela, ¿qué anota la clase: la forma de la Luna cada noche o el color de las plantas?", "La forma de la Luna cada noche", "Es el registro del cuaderno de la escuela."),
        ex("¿Dónde anota el abuelo: en una libreta o en un mapa?", "En una libreta", "Doña Aurora lo cuenta en su testimonio."),
    ],
    C=[
        ex("Verdadero o falso: la ciencia escolar y el conocimiento de una comunidad pueden partir ambos de la observación.", "Verdadero", "Los dos observan con atención."),
        ex("¿Qué es un criterio de comparación? A) la opinión de quien compara B) un punto igual para los dos casos, como «cómo se registra»", "B", "El criterio permite comparar con el mismo punto."),
        ex("Verdadero o falso: comparar significa decir que una forma de conocer es «más científica».", "Falso", "Comparar es buscar semejanzas y diferencias."),
    ],
    A=[
        ex("Criterio: «para qué se usa». Escuela: para entender cuánto dura un ciclo de la Luna. Cumbre Clara: para decidir cuándo sembrar. ¿Qué diferencia hay? A) se usa para fines distintos B) se usa para lo mismo", "A", "Cada caso usa lo aprendido para algo distinto."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) ambos observan la Luna con atención b) una comunidad transmite oralmente y la escuela, por escrito.", "a semejanza, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        arith("En la escuela, la clase anota la forma de la Luna durante 28 noches. Cumbre Clara anota durante 2 ciclos de 29 días (datos inventados). ¿Cuántos días más anota Cumbre Clara?", "2*29-28", "Se calculan los días de Cumbre Clara y se resta el total de la escuela."),
    ],
    Z=[
        ex("Ana dice: «El cuaderno de la escuela es más científico que la libreta del abuelo». ¿Qué falla en su comparación?", "Ordena dos formas de conocer sin criterio ni fuente", "Comparar no es jerarquizar."),
        ex("Un compañero escribe: «Como ambos observan la Luna, todos los pueblos y todas las escuelas observan igual». ¿Qué debería escribir? A) «en todos los casos» B) «en estos dos casos»", "B", "Dos casos no representan a todos."),
    ],
    D=[
        ex("Dos conclusiones. 1) «En estos dos casos, ambos observan, registran y usan lo aprendido». 2) «La libreta del abuelo es una superstición y el cuaderno de la escuela es ciencia». ¿Cuál está bien formulada?", "La primera", "La segunda jerarquiza y descalifica."),
        ex("Una compañera dice que el abuelo de doña Aurora «usaba una tabla con símbolos». El testimonio solo habla de números en una libreta. ¿Qué parte es interpretación? A) la libreta con números B) la tabla con símbolos", "B", "El testimonio no menciona símbolos."),
    ],
    context=[ex("Tu curso hace una feria de ciencias. Una compañera propone invitar a un mayor de una comunidad a contar cómo observa el cielo, con su permiso. ¿Qué ventaja tiene? A) ofrece otra manera de conocer que dialoga con la ciencia escolar B) reemplaza la feria de ciencias", "A", "El diálogo de saberes suma, no reemplaza.")],
    selfcheck=[
        ex("Escribe una semejanza entre la ciencia escolar y el conocimiento de Cumbre Clara.", "Ambos observan y registran", "Esa semejanza aparece en la explicación."),
        ex("Verdadero o falso: puedo ordenar dos formas de conocer de más a menos científica.", "Falso", "Cada una se entiende desde su manera de conocer."),
        ex("Nombra un criterio de comparación para dos formas de conocer.", "Por ejemplo: cómo se transmite", "Debe ser un punto igual para ambas."),
    ],
    task=T("Compara estas dos formas de conocer. Escuela (inventada): «Una clase anota cada noche la forma de la Luna durante un mes y escribe un informe». Cumbre Clara (doña Aurora): «Mi abuelo anotaba los días entre lunas llenas, miraba las plantas y decidía cuándo sembrar; lo aprendí acompañándolo». Haz una tabla con cuatro criterios: «qué se observa», «cómo se registra», «para qué se usa» y «cómo se transmite». Escribe una semejanza, una diferencia y una frase que termine con «en estos dos casos».",
           "Qué se observa: la forma de la Luna; la Luna y las plantas. Cómo se registra: cuaderno; libreta. Para qué: entender el ciclo; decidir cuándo sembrar. Cómo se transmite: informe escrito; acompañando a los mayores. Semejanza: ambos observan la Luna y anotan. Diferencia: para qué se usa y cómo se transmite. Esto se ve en estos dos casos.",
           ["usa los mismos criterios para ambos", "distingue semejanza y diferencia", "no jerarquiza"], ["tabla de cuatro criterios", "semejanza y diferencia"], ["decir cuál es más científica", "generalizar a todas las comunidades"],
           "Pedir que muestre en la tabla la fila que respalda cada semejanza; valorar que no ordene las formas de conocer."),
    reinforce="Marca en la tabla con un color las semejanzas y con otro las diferencias.",
    extend="Explica cómo podrían trabajar juntas una clase y una comunidad para entender mejor el cielo, con permiso de la comunidad.",
)

L(
    OA16, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida que valore el sentido de la relación entre el ser humano, la naturaleza y el cosmos desde una comunidad, y a expresarlo con una manifestación propia.",
    prior=["Sé comparar la ciencia escolar con el conocimiento de una comunidad.", "Sé leer un testimonio con límites."],
    explain=[
        "Una respuesta atribuida sobre ciencia desde la perspectiva indígena tiene cinco partes. Primero, el dato de la fuente con su nombre: «Doña Aurora cuenta que…». Segundo, lo que se observa y para qué se usa. Tercero, la relación entre ser humano, naturaleza y cosmos que aparece en el testimonio. Cuarto, tu reflexión con «yo pienso que» y un límite. Quinto, una pregunta para el educador tradicional.",
        "Además de escribir, podemos expresar lo que aprendimos a través de una manifestación propia: un dibujo, un poema corto, un esquema o un relato. La manifestación es nuestra y no pretende reproducir lo que la comunidad guarda ni inventar una práctica ancestral. Al presentarla, decimos que es una expresión nuestra inspirada en lo que escuchamos o leímos.",
        "Una buena respuesta no exagera, no inventa explicaciones y no habla por todo un pueblo. Reconoce lo que no sabe y respeta lo que la comunidad reserva. Al final se devuelve a la comunidad o al educador, para que la revise y corrija lo que no esté bien dicho.",
    ],
    vocab=[("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("manifestación", "forma de expresar lo que se piensa o se siente, como un dibujo o un poema"), ("esquema", "dibujo simple que muestra partes de algo y cómo se relacionan"), ("inspirada en", "creada a partir de algo que se vio o escuchó, sin copiarlo"), ("devolución", "mostrar el trabajo a la comunidad o al educador para que lo revisen")],
    worked=[
        W("Armar una respuesta", TCC + " Arma una respuesta atribuida de cinco partes.", ["Dato: doña Aurora cuenta que su abuelo miraba la Luna y las plantas para saber cuándo sembrar.", "Observa y usa: la Luna y las plantas, para decidir la siembra.", "Relación: ella dice que lo que pasa en el cielo y en la tierra están relacionados.", "Reflexión, límite y pregunta: yo pienso que esa relación ayuda a cuidar el trabajo del año; no sé cómo la explican; preguntaré al educador tradicional."], "Respuesta con dato atribuido, observación y uso, relación, reflexión con límite y pregunta."),
        W("Revisar una manifestación", "Un niño dibuja un símbolo y escribe debajo: «Este es el símbolo ancestral de Cumbre Clara para la Luna». ¿Qué problema tiene?", ["El testimonio no habla de ningún símbolo.", "El niño presenta algo suyo como si fuera de la comunidad.", "Debería escribir que es un dibujo propio inspirado en el testimonio."], "Presenta algo inventado como si fuera de la comunidad; debe decir que es un dibujo propio."),
    ],
    mistakes=[
        M("Presentar una manifestación inventada como si fuera ancestral.", "Se falsea un saber que la comunidad no contó.", "Escribe que es una expresión propia inspirada en el testimonio."),
        M("No marcar qué parte es opinión mía.", "El lector no distingue la voz de la comunidad de la mía.", "Usa «yo pienso que…»."),
    ],
    R=[
        ex("¿Con qué frase atribuyes un dato a doña Aurora? A) «Doña Aurora cuenta que…» B) «Todos saben que…»", "A", "Nombra a la fuente."),
        ex("Tema: la ciencia y el cosmos. ¿Cuántas partes tiene la respuesta atribuida de esta clase? Escribe el número.", "5", "Son dato, observación y uso, relación, reflexión con límite y pregunta."),
        ex("Tema: la ciencia y el cosmos. Verdadero o falso: mi reflexión es una idea mía y no del testimonio.", "Verdadero", "Por eso se marca como mía."),
    ],
    C=[
        ex("¿Qué es una manifestación? A) una orden de la comunidad B) una forma de expresar lo que se piensa o se siente, como un dibujo", "B", "Es una expresión propia."),
        ex("Verdadero o falso: puedo presentar mi dibujo como un símbolo ancestral de una comunidad.", "Falso", "Sería presentar algo inventado como ajeno."),
        ex("Tema: la ciencia y el cosmos. ¿Para qué sirve la pregunta final? A) para consultar al educador tradicional lo que no sé B) para terminar rápido", "A", "La pregunta señala lo que se debe consultar."),
    ],
    A=[
        ex("Testimonio de doña Aurora: «Mi abuelo miraba la Luna y las plantas». Completa la atribución: «Doña Aurora cuenta que su abuelo miraba…»", "La Luna y las plantas", "Se repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) doña Aurora cuenta que anotaban los días entre lunas llenas b) yo pienso que anotar daba orden al trabajo.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        ex("Un esquema dice: «Dibujo propio inspirado en el testimonio de doña Aurora: Luna, planta y persona unidas por una línea». ¿Qué hace bien? A) lo presenta como ancestral B) aclara que es una expresión propia", "B", "Dice que es dibujo propio inspirado en el testimonio."),
    ],
    Z=[
        ex("Tema: la ciencia y el cosmos. Marta escribe una respuesta sin límite. ¿Qué mejoraría? A) agregar lo que no sé o no se cuenta B) agregar más datos inventados", "A", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu respuesta y tu manifestación al educador tradicional? A) porque es una tarea de decoración B) porque conoce el saber de su pueblo y puede corregir errores", "B", "Quien conoce su cultura puede corregir lo equivocado."),
    ],
    D=[
        ex("Dos reflexiones. 1) «Doña Aurora cuenta que cielo y tierra están relacionados; yo pienso que eso ayuda a cuidar el trabajo del año». 2) «Doña Aurora demuestra que su ciencia es mejor que la de la escuela». ¿Cuál está bien construida?", "La primera", "La segunda exagera y jerarquiza."),
        ex("Un compañero agrega que en Cumbre Clara «seguro hacen un baile a la Luna». El testimonio no lo menciona. ¿Qué debe hacer?", "Quitarlo porque no está en la fuente", "Lo que la fuente no dijo no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre cómo observaba el cielo el abuelo de doña Aurora. ¿Qué empieza mejor? A) «Doña Aurora cuenta que…» B) «Todos los pueblos indígenas miran el cielo para…»", "A", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cinco partes de una respuesta atribuida sobre ciencia desde una comunidad.", "Dato de la fuente, observación y uso, relación, reflexión con límite y pregunta", "Están en la explicación."),
        ex("Tema: la ciencia y el cosmos. Verdadero o falso: debo marcar qué parte es mi opinión.", "Verdadero", "Así no se confunde con la fuente."),
        ex("Tema: la ciencia y el cosmos. ¿Qué haces al terminar? A) guardarlo sin mostrarlo B) mostrarlo a la comunidad o al educador para que lo revise", "B", "Es la devolución."),
    ],
    task=T("Usa este testimonio inventado de doña Aurora: «En Cumbre Clara miramos la Luna para ordenar el trabajo del año. Mi abuelo anotaba los días entre lunas llenas. Lo que pasa en el cielo y lo que pasa en la tierra están relacionados. De otros conocimientos no hablamos con visitas.» Escribe una respuesta de cinco partes: 1) dato de doña Aurora, 2) lo que se observa y para qué se usa, 3) la relación entre ser humano, naturaleza y cosmos que aparece, 4) tu reflexión con «yo pienso que» y un límite, 5) una pregunta para el educador tradicional. Después haz una manifestación propia: un dibujo simple o un poema de dos líneas sobre la Luna, y escribe debajo «expresión propia inspirada en el testimonio de doña Aurora».",
           "1) Doña Aurora cuenta que miran la Luna para ordenar el trabajo del año y que su abuelo anotaba los días entre lunas llenas. 2) Observan la Luna; la usan para ordenar el trabajo. 3) Cielo y tierra están relacionados. 4) Yo pienso que anotar daba orden al trabajo; no sé cómo explican la relación. 5) Pregunta: ¿cómo explica mi pueblo la relación entre el cielo y la tierra? Poema: «La Luna crece y se achica / y el huerto espera con calma». Expresión propia inspirada en el testimonio de doña Aurora.",
           ["atribuye cada dato", "incluye límite y pregunta", "aclara que la manifestación es propia"], ["texto de cinco partes", "dibujo o poema con nota de autoría"], ["presentar la manifestación como ancestral", "inventar explicaciones"],
           "Pedir que señale la línea del testimonio que respalda su reflexión; valorar que la manifestación diga que es propia."),
    reinforce="Numera del 1 al 5 las partes de tu respuesta para comprobar que están todas.",
    extend="Escribe una segunda manifestación propia (un esquema) con la Luna, una planta y una persona, y la nota que aclara que es tuya.",
)
