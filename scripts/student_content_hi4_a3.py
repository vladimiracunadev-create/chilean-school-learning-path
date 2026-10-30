"""Material del estudiante de 4.º básico, Historia, Geografía y Ciencias Sociales: OA 03 (civilización inca) y OA 04 (comparación de civilizaciones americanas)."""
from __future__ import annotations

from student_lessons import arith, ex, register
from student_content_hi4_a import task

OA3 = "HI04 OA 03"
OA4 = "HI04 OA 04"

# ================================================================ OA 03 · INCAS
# ---------------------------------------------------------------- clase 1
I1 = ("Ficha inca 1: Los incas vivieron en los Andes de América del Sur. Su capital fue Cusco, en el actual Perú. Su imperio se llamó Tawantinsuyo y creció sobre todo durante el siglo XV. "
      "Llegó desde el sur de Colombia hasta el centro de Chile, pasando por Ecuador, Perú, Bolivia y el noroeste de Argentina. En Chile, su límite sur fue el río Maule. "
      "Lo gobernaba el Sapa Inca, la máxima autoridad. El imperio terminó cuando llegaron los españoles, hacia 1532. Su territorio tenía cordillera, costa, desierto y selva.")
register(
    OA3, 1,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio. Un mapa de América del Sur ayuda, pero no es necesario.",
    use="Aprenderé dónde y cuándo vivieron los incas y cómo se gobernaba su imperio. Sirve para ubicar su historia, que además llegó hasta Chile.",
    prior=["Sé qué es un imperio y qué es el tributo.", "Sé ubicar países de América del Sur en un mapa."],
    explain=[
        "Los incas vivieron en los Andes, la gran cordillera de América del Sur. Su capital fue Cusco, en el actual Perú. Su imperio se llamó Tawantinsuyo. Creció sobre todo durante el siglo XV, que son los años 1401 a 1500, y terminó cuando llegaron los españoles, hacia 1532.",
        "El Tawantinsuyo fue muy extenso. Iba desde el sur de Colombia hasta el centro de Chile y pasaba por Ecuador, Perú, Bolivia y el noroeste de Argentina. En Chile llegó hasta el río Maule. Por eso parte de nuestro territorio actual formó parte del imperio inca.",
        "Lo gobernaba el Sapa Inca, que era la máxima autoridad. Su territorio incluía cordillera, costa, desierto y selva, lugares muy distintos entre sí. Por eso, gobernar bien exigía organización y buenas comunicaciones, como veremos en las próximas clases.",
    ],
    vocab=[("Tawantinsuyo", "nombre del imperio inca"), ("Sapa Inca", "gobernante máximo del imperio inca"), ("Andes", "gran cordillera de América del Sur"), ("siglo", "periodo de cien años"), ("Cusco", "capital del imperio inca, en el actual Perú")],
    worked=[
        {"title": "Ubicar la capital", "problem": f"{I1} ¿Dónde estaba la capital de los incas?", "steps": ["Busco el nombre de la capital: Cusco.", "La ficha dice que está en el actual Perú."], "answer": "En Cusco, en el actual Perú"},
        {"title": "Relacionar con Chile", "problem": f"{I1} ¿Hasta dónde llegó el imperio inca en Chile?", "steps": ["Busco lo que dice la ficha sobre Chile.", "Dice que su límite sur fue el río Maule."], "answer": "Hasta el río Maule, en la zona central"},
    ],
    mistakes=[
        {"wrong": "Decir que el imperio inca estaba en México.", "why": "Se confunde con aztecas y mayas.", "fix": "Los incas vivieron en los Andes de América del Sur."},
        {"wrong": "Pensar que el imperio inca llegaba hasta el extremo sur de Chile.", "why": "No se recuerda el límite.", "fix": "Su límite sur en Chile fue el río Maule."},
    ],
    tiers={
        "recovery": [
            ex(f"{I1} ¿Cómo se llamaba el imperio inca?", "Tawantinsuyo", "La ficha da ese nombre."),
            ex(f"{I1} ¿Cuál fue la capital inca?", "Cusco", "La ficha lo indica."),
            ex(f"{I1} ¿Quién era la máxima autoridad inca?", "el Sapa Inca", "La ficha lo nombra."),
        ],
        "understand": [
            ex(f"{I1} ¿En qué continente y cordillera vivieron los incas?", "en América del Sur, en los Andes", "La ficha los ubica en los Andes de América del Sur."),
            ex(f"{I1} ¿Qué río fue el límite sur del imperio en Chile?", "el río Maule", "La ficha lo indica."),
            ex(f"{I1} ¿Los incas gobernaban un territorio de un solo paisaje o de paisajes muy distintos?", "de paisajes muy distintos", "Había cordillera, costa, desierto y selva."),
        ],
        "apply": [
            arith(f"{I1} El siglo XV termina en el año 1500. Los españoles llegaron hacia 1532. ¿Cuántos años pasaron entre ambos?", "1532-1500", "Se resta el año final menos el inicial.", " años"),
            ex(f"{I1} Los aztecas fundaron Tenochtitlán hacia 1325. ¿El imperio inca creció antes o después de esa fecha?", "después", "El siglo XV son los años 1401 a 1500, posteriores a 1325."),
            ex(f"{I1} ¿Qué país actual de esta lista formó parte del imperio inca: Perú o Brasil?", "Perú", "La ficha nombra a Perú, no a Brasil."),
        ],
        "reason": [
            ex(f"{I1} Tomás dice: «El imperio inca llegaba hasta Punta Arenas». ¿Qué dato de la ficha lo corrige?", "Su límite sur en Chile fue el río Maule", "Punta Arenas queda mucho más al sur."),
            ex(f"{I1} Ana dice: «Los incas vivieron en una selva de México». ¿Qué dos datos de la ficha la contradicen?", "Vivieron en los Andes de América del Sur, con capital en Cusco", "La ficha los ubica en América del Sur."),
        ],
        "challenge": [
            ex(f"{I1} Clasifica cada dato en «dónde», «cuándo» o «quién gobernaba»: a) el Sapa Inca; b) siglo XV; c) los Andes.", "a: quién gobernaba; b: cuándo; c: dónde", "Cada dato responde una pregunta distinta."),
            ex(f"{I1} Un mapa muestra el imperio inca terminando en el norte de Chile; otro, en el río Maule. ¿Cuál concuerda con la ficha?", "el que lo termina en el río Maule", "La ficha dice que el límite sur fue el Maule."),
        ],
    },
    context=[ex("Un cartel en un museo chileno dice: «Esta zona formó parte del imperio inca». ¿Qué dato de la ficha apoya que parte de Chile fue inca?", "En Chile, su límite sur fue el río Maule", "Ese dato indica que había territorio inca en Chile.")],
    selfcheck=[
        ex("¿Dónde vivieron los incas?", "en los Andes de América del Sur", "Allí se ubicó el Tawantinsuyo."),
        ex("¿Quién gobernaba el imperio inca?", "el Sapa Inca", "Era la máxima autoridad."),
        ex("¿Hasta qué río llegó el imperio inca en Chile?", "hasta el río Maule", "Fue su límite sur."),
    ],
    open_task=task(
        f"Dibuja un mapa simple de América del Sur con una mancha larga a lo largo de la costa del Pacífico para el imperio inca. Marca con un punto Cusco y con otro punto el río Maule en Chile. Escribe las palabras «Andes» y «Pacífico». {I1}",
        "América del Sur con una mancha larga junto al Pacífico, Cusco al norte y el Maule en la parte central de Chile.",
        ["mancha junto a los Andes", "Cusco al norte", "Maule en Chile"], ["mapa simple dibujado"], ["dibujar el imperio en México", "poner el Maule en el extremo sur"],
        "Pregunta por qué la mancha es larga y angosta. La respuesta esperada es que sigue la cordillera de los Andes."),
    reinforce="Cuenta a alguien dónde estaba Cusco y hasta dónde llegó el imperio inca en Chile.",
    extend="Escribe dos diferencias entre el territorio inca y la región maya.",
)

# ---------------------------------------------------------------- clase 2
I2 = ("Fuentes sobre los incas: (1) Machu Picchu, ruinas de una ciudad de piedra en la cordillera, construida en el siglo XV. "
      "(2) Un quipu: cuerdas con nudos de colores que servían para registrar cantidades. Los incas no usaron una escritura con letras. "
      "(3) Tramos del Camino del Inca, llamado Qhapaq Ñan, hechos de piedra y todavía visibles. "
      "(4) Un libro escrito en el siglo XVI por un cronista español que viajó por los Andes. "
      "(5) Un libro con dibujos y texto escrito a comienzos del siglo XVII por un autor indígena andino, que lo dirigió al rey de España para pedir justicia.")
register(
    OA3, 2,
    materials="Lápiz y papel. Las fuentes están escritas en cada ejercicio.",
    use="Aprenderé a distinguir qué fuentes dejaron los propios incas y cuáles escribieron otras personas. Sirve para saber cuánto confiar en cada una.",
    prior=["Sé que la procedencia es quién hizo la fuente, cuándo y para qué.", "Sé dónde vivieron los incas."],
    explain=[
        "Los incas no usaron una escritura con letras. Por eso conocemos su historia por otras fuentes: ruinas como Machu Picchu, caminos de piedra, objetos y los quipus. Un quipu es un conjunto de cuerdas con nudos de colores que servía para registrar cantidades, como animales o productos. Aún hay mucho de los quipus que no se comprende.",
        "También hay textos escritos después de la llegada de los españoles. Un cronista español del siglo XVI escribió lo que vio y le contaron. Lo hizo desde su mirada de extranjero. Un autor indígena andino escribió a comienzos del siglo XVII y dibujó la vida bajo los incas y bajo los españoles, para pedir justicia al rey.",
        "Para usar una fuente preguntamos: ¿quién la hizo, cuándo y para qué? Un texto escrito por un extranjero y otro escrito por un andino pueden contar lo mismo de forma distinta. Por eso conviene comparar varias fuentes antes de sacar una conclusión.",
    ],
    vocab=[("quipu", "cuerdas con nudos de colores usadas para registrar cantidades"), ("Qhapaq Ñan", "camino principal del imperio inca"), ("cronista", "persona que escribe lo que ve o le cuentan"), ("indígena", "perteneciente a un pueblo originario"), ("procedencia", "quién hizo la fuente, cuándo y para qué")],
    worked=[
        {"title": "Distinguir autores", "problem": f"{I2} ¿Qué fuente escribió un cronista español?", "steps": ["Busco la palabra español.", "La fuente 4 lo dice."], "answer": "La fuente 4"},
        {"title": "Reconocer un límite", "problem": f"{I2} ¿Un quipu nos dice qué pensaban los incas de sus dioses?", "steps": ["El quipu registra cantidades con nudos.", "No habla de creencias."], "answer": "No, el quipu registraba cantidades"},
    ],
    mistakes=[
        {"wrong": "Decir que los incas escribían con letras.", "why": "Se piensa en nuestra escritura.", "fix": "Usaron quipus: cuerdas con nudos que registraban cantidades."},
        {"wrong": "Creer que el texto del cronista español es lo que pensaban los incas.", "why": "No se pregunta quién escribió.", "fix": "Pregunta por la procedencia: él miraba desde afuera."},
    ],
    tiers={
        "recovery": [
            ex(f"{I2} ¿Qué es un quipu?", "cuerdas con nudos de colores para registrar cantidades", "La ficha lo define así."),
            ex(f"{I2} ¿Qué fuente son ruinas de una ciudad de piedra en la cordillera?", "Machu Picchu", "La fuente 1 es Machu Picchu."),
            ex(f"{I2} ¿Cómo se llama el camino inca de piedra?", "Qhapaq Ñan", "La ficha lo llama Camino del Inca o Qhapaq Ñan."),
        ],
        "understand": [
            ex(f"{I2} ¿Por qué conocemos a los incas por otras fuentes además de la escritura?", "porque no usaron una escritura con letras", "La ficha lo dice."),
            ex(f"{I2} ¿A quién dirigió su libro el autor indígena de la fuente 5?", "al rey de España", "La ficha lo dice."),
            ex(f"{I2} ¿Cuál es más antigua: la fuente 4 (siglo XVI) o la fuente 5 (comienzos del siglo XVII)?", "la fuente 4", "El siglo XVI es anterior al XVII."),
        ],
        "apply": [
            ex(f"{I2} Quieres saber cómo eran las construcciones de piedra incas. ¿Qué fuente usas?", "la fuente 1 (Machu Picchu)", "Muestra una ciudad de piedra."),
            ex(f"{I2} Quieres saber cómo registraban cantidades de productos. ¿Qué fuente usas?", "la fuente 2 (el quipu)", "El quipu servía para registrar cantidades."),
            ex(f"{I2} Une cada fuente con su autor: A) fuente 4; B) fuente 5. 1) un autor indígena andino; 2) un cronista español.", "A con 2; B con 1", "Cada una tiene un autor distinto."),
        ],
        "reason": [
            ex(f"{I2} Pedro dice: «El cronista español nos cuenta exactamente lo que pensaban los incas». ¿Qué problema tiene su frase?", "El cronista miraba desde afuera y pudo equivocarse o juzgar con sus ideas", "Su procedencia es de extranjero."),
            ex(f"{I2} Clara dice: «El autor indígena de la fuente 5 escribió para pedir justicia, así que su relato no tiene propósito». ¿Es cierto?", "No, su propósito era pedir justicia al rey", "Toda fuente tiene un propósito."),
        ],
        "challenge": [
            ex(f"{I2} Para comparar la mirada de un extranjero con la de un andino, ¿qué dos fuentes enfrentarías?", "la fuente 4 con la fuente 5", "Una la escribió un español y la otra, un andino."),
            ex(f"{I2} Elige la pregunta que estas fuentes no pueden responder. A) ¿Qué materiales usaron en Machu Picchu? B) ¿Cuál era el nombre de un niño que vivió en Cusco?", "B", "Ninguna fuente de la ficha entrega nombres de niños."),
        ],
    },
    context=[ex("Una turista ve un quipu y dice: «Es un libro con letras». ¿Cómo la corriges con la ficha?", "Es un conjunto de cuerdas con nudos que registraba cantidades; los incas no usaron letras", "La ficha explica qué era un quipu.")],
    selfcheck=[
        ex("¿Los incas escribían con letras?", "No, usaban quipus", "La ficha lo dice."),
        ex("¿Qué tres preguntas forman la procedencia de una fuente?", "quién la hizo, cuándo y para qué", "Con ellas se evalúa la fuente."),
        ex(f"{I2} ¿Qué fuente la escribió un autor indígena andino?", "la fuente 5", "Es el libro con dibujos dirigido al rey de España."),
    ],
    open_task=task(
        f"Haz una tabla con las columnas «fuente», «quién la hizo» y «qué nos dice». Completa dos filas: el quipu (fuente 2) y el libro del autor indígena (fuente 5). Después escribe una cosa que cada una no nos dice. {I2}",
        "Quipu: los incas; registra cantidades; no dice qué pensaban los incas. Libro: un autor indígena andino; muestra la vida bajo incas y españoles y pide justicia; no dice cómo era un día cualquiera.",
        ["dos filas completas", "quién la hizo bien indicado", "un límite por fuente"], ["tabla completa"], ["decir que el quipu era escritura con letras", "confundir al autor de cada fuente"],
        "Pregunta cuál de las dos fuentes le sirve más para saber cuánto se producía y por qué."),
    reinforce="Nombra tres fuentes sobre los incas y di quién las hizo.",
    extend="Imagina cómo registrarías con nudos de cuerda la cantidad de útiles de tu mochila.",
)

# ---------------------------------------------------------------- clase 3
I3 = ("Ficha inca 3: Para sembrar en las laderas de los cerros, los incas hicieron andenes, que son terrazas escalonadas. Cultivaban papa, maíz y quinua. "
      "Criaban llamas y alpacas, que daban lana y cargaban cosas. Con la papa hacían chuño, una papa deshidratada por el frío y el sol, que duraba mucho tiempo. "
      "El Estado guardaba alimentos y telas en almacenes. Los incas no usaban dinero. Las personas hacían trabajo por turnos para el Estado, llamado mita. "
      "La sociedad tenía al Sapa Inca y a los nobles, a los funcionarios y a la gente común, que era la mayoría. Los hombres trabajaban el campo, construían y servían en el ejército. "
      "Las mujeres hilaban, tejían, cocinaban y cuidaban a los hijos. Los tejidos eran muy valiosos.")
register(
    OA3, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé cómo cultivaban y se alimentaban los incas y cómo se organizaba su sociedad. Sirve para describir su vida cotidiana con datos.",
    prior=["Sé dónde vivieron los incas.", "Sé qué es un imperio y qué es el tributo."],
    explain=[
        "Los incas vivían en una cordillera con muchas laderas empinadas. Para sembrar allí hicieron andenes, terrazas escalonadas que aprovechan la pendiente. Cultivaban papa, maíz y quinua. Criaban llamas y alpacas, que daban lana y cargaban bultos. Con la papa hacían chuño, que duraba mucho tiempo.",
        "No usaban dinero. En su lugar, las personas trabajaban por turnos para el Estado, trabajo llamado mita. El Estado guardaba alimentos y telas en almacenes y los repartía cuando hacía falta. Era una forma de organizar la economía de un imperio muy grande sin monedas.",
        "En la cima de la sociedad estaban el Sapa Inca y los nobles. Luego venían los funcionarios y, por último, la gente común, que era la mayoría y trabajaba la tierra. Los hombres trabajaban el campo, construían y servían en el ejército. Las mujeres hilaban, tejían, cocinaban y cuidaban a los hijos. Los tejidos eran muy valiosos.",
    ],
    vocab=[("andén", "terraza escalonada para cultivar en un cerro"), ("chuño", "papa deshidratada por el frío y el sol"), ("mita", "trabajo por turnos para el Estado inca"), ("almacén", "lugar para guardar alimentos y telas"), ("alpaca", "animal andino de lana fina")],
    worked=[
        {"title": "Explicar un cultivo", "problem": f"{I3} ¿Para qué servían los andenes?", "steps": ["Leo la definición: terrazas escalonadas en las laderas.", "Servían para sembrar en cerros empinados."], "answer": "Para sembrar en las laderas de los cerros"},
        {"title": "Explicar la economía", "problem": f"{I3} Si no usaban dinero, ¿cómo trabajaba la gente para el Estado?", "steps": ["Busco cómo se llamaba ese trabajo.", "Dice que trabajaban por turnos: la mita."], "answer": "Con la mita, trabajo por turnos para el Estado"},
    ],
    mistakes=[
        {"wrong": "Decir que los incas pagaban con monedas.", "why": "Se piensa en la economía actual.", "fix": "Recuerda que no usaban dinero: había mita y almacenes."},
        {"wrong": "Decir que los andenes servían para vivir.", "why": "Se piensa en escalones de una casa.", "fix": "Los andenes son terrazas para cultivar."},
    ],
    tiers={
        "recovery": [
            ex(f"{I3} ¿Qué son los andenes?", "terrazas escalonadas para sembrar en los cerros", "La ficha los define así."),
            ex(f"{I3} ¿Qué animales criaban los incas?", "llamas y alpacas", "La ficha los nombra."),
            ex(f"{I3} ¿Cómo se llama la papa deshidratada por el frío y el sol?", "chuño", "La ficha lo define."),
        ],
        "understand": [
            ex(f"{I3} ¿Usaban dinero los incas?", "No", "La ficha dice que no usaban dinero."),
            ex(f"{I3} ¿Qué guardaba el Estado en los almacenes?", "alimentos y telas", "La ficha lo indica."),
            ex(f"{I3} ¿Qué grupo de la sociedad inca era la mayoría?", "la gente común", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{I3} Una mujer inca hila lana de alpaca y teje una tela. ¿Qué rol de las mujeres cumple?", "hilar y tejer", "La ficha lo nombra como tarea de las mujeres."),
            ex(f"{I3} Un menú tiene papa, maíz y quinua. ¿Son cultivos incas de la ficha?", "Sí", "Los tres aparecen en la ficha."),
            ex(f"{I3} Un hombre trabaja unos días en la construcción de un camino para el Estado. ¿Cómo se llama ese trabajo por turnos?", "mita", "Es el nombre del trabajo para el Estado."),
        ],
        "reason": [
            ex(f"{I3} Luis dice: «Sin dinero, el Estado inca no podía repartir alimentos». ¿Qué dato de la ficha lo corrige?", "El Estado guardaba alimentos en almacenes y los repartía", "La ficha describe otra forma de organización."),
            ex(f"{I3} Ana dice: «Las mujeres incas no hacían nada valioso». ¿Qué dato de la ficha la contradice?", "Los tejidos que hacían eran muy valiosos", "La ficha lo dice."),
        ],
        "challenge": [
            ex(f"{I3} Clasifica en «cultivo», «economía» o «roles»: a) andenes; b) mita; c) las mujeres hilaban y tejían.", "a: cultivo; b: economía; c: roles", "Cada dato responde a una dimensión distinta."),
            ex(f"{I3} ¿Qué dimensión NO aparece en la ficha: la religión o la alimentación?", "la religión", "La ficha trata de cultivos, economía y sociedad."),
        ],
    },
    context=[ex("Una excursión visita un cerro con escalones de piedra donde crece maíz. ¿Cómo se llama esa forma de cultivo y para qué sirve?", "andén; para sembrar en una ladera", "Los andenes permiten cultivar en pendientes.")],
    selfcheck=[
        ex("¿Qué alimentos nombra la ficha para los incas?", "papa, maíz, quinua y chuño", "Son los alimentos de la ficha."),
        ex("¿Cómo se llama el trabajo por turnos para el Estado inca?", "mita", "Reemplazaba al dinero."),
        ex("¿Qué grupo de la sociedad inca estaba en la cima?", "el Sapa Inca y los nobles", "Así lo indica la ficha."),
    ],
    open_task=task(
        f"Dibuja un cerro con tres andenes y escribe en cada uno un cultivo: papa, maíz y quinua. Abajo escribe tres líneas: qué hacían los hombres, qué hacían las mujeres y cómo trabajaba la gente sin dinero. {I3}",
        "Cerro con tres andenes con papa, maíz y quinua. Hombres: campo, construcción y ejército. Mujeres: hilar, tejer, cocinar. Sin dinero: mita.",
        ["tres andenes con cultivos", "roles de hombres y mujeres", "mita explicada"], ["dibujo", "tres líneas"], ["decir que usaban dinero", "olvidar a las mujeres"],
        "Pregunta por qué los incas necesitaban andenes. La respuesta esperada es que las laderas son empinadas."),
    reinforce="Cuenta en voz alta qué cultivaban los incas y cómo se organizaba el trabajo.",
    extend="Escribe una semejanza y una diferencia entre los andenes incas y las chinampas aztecas.",
)

# ---------------------------------------------------------------- clase 4
I4 = ("Ficha inca 4: El Qhapaq Ñan era una red de caminos de miles de kilómetros que unía Cusco con todo el imperio. Los chasquis eran corredores que se relevaban para llevar mensajes. "
      "Cada cierto trecho había un tambo, una casa de descanso con alimentos y mantas. Los puentes colgantes se hacían con fibras de plantas. Los incas construyeron muros de piedras muy bien ajustadas. "
      "Adoraban a Inti, dios del Sol, y a la Pachamama, la Madre Tierra; también respetaban las montañas. Hacían ofrendas de chicha, hojas de coca y llamas. Según las crónicas, en ceremonias muy especiales hubo sacrificios humanos. "
      "Hoy el Qhapaq Ñan es Patrimonio Mundial de la UNESCO y en los Andes millones de personas hablan quechua. El cronista español ve el camino como útil para el imperio. El autor indígena muestra la carga de trabajo del pueblo.")
register(
    OA3, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé cómo se comunicaba el imperio inca, qué creían los incas y qué parte de su herencia continúa hoy. Sirve para comparar perspectivas, cambios y continuidades.",
    prior=["Sé qué es un imperio.", "Sé que las fuentes tienen perspectivas distintas."],
    explain=[
        "Para gobernar un territorio tan extenso, los incas construyeron el Qhapaq Ñan, una red de caminos de miles de kilómetros. Por ellos corrían los chasquis, mensajeros que se relevaban para llevar noticias rápido. Cada cierto trecho había un tambo, una casa de descanso con alimentos y mantas. También hacían puentes colgantes con fibras de plantas.",
        "Los incas adoraban a Inti, el dios Sol, y a la Pachamama, la Madre Tierra. También respetaban las montañas. Ofrecían chicha, hojas de coca y llamas. Según las crónicas, solo en ceremonias muy especiales hubo sacrificios humanos. Es un tema delicado que se debe explicar con respeto.",
        "Hay cambios y continuidades. Hoy el Qhapaq Ñan es Patrimonio Mundial de la UNESCO y millones de personas hablan quechua en los Andes. Además, las perspectivas varían: el cronista español destaca la utilidad del camino para el imperio; el autor indígena muestra la carga de trabajo del pueblo. Ambas miradas ayudan a comprender.",
    ],
    vocab=[("chasqui", "corredor que llevaba mensajes por los caminos incas"), ("tambo", "casa de descanso con alimentos en el camino"), ("Inti", "dios Sol de los incas"), ("Pachamama", "Madre Tierra en la cultura andina"), ("Patrimonio Mundial", "lugar que se protege por su valor para la humanidad")],
    worked=[
        {"title": "Explicar el correo inca", "problem": f"{I4} ¿Cómo viajaba un mensaje por el camino inca?", "steps": ["Busco quién llevaba los mensajes: los chasquis.", "Se relevaban y descansaban en los tambos."], "answer": "Los chasquis se relevaban para llevar el mensaje y descansaban en los tambos"},
        {"title": "Distinguir perspectivas", "problem": f"{I4} ¿Cómo mira el camino el cronista español y cómo lo mira el autor indígena?", "steps": ["El cronista destaca la utilidad para el imperio.", "El autor indígena muestra la carga de trabajo."], "answer": "El cronista, su utilidad; el autor indígena, la carga de trabajo del pueblo"},
    ],
    mistakes=[
        {"wrong": "Decir que los chasquis viajaban a caballo.", "why": "Se piensa en mensajeros de otras épocas.", "fix": "Los chasquis eran corredores que se relevaban a pie."},
        {"wrong": "Pensar que los incas ya no existen y nada de su cultura continúa.", "why": "Se confunde el imperio con el pueblo.", "fix": "Millones de personas hablan quechua hoy y el camino es patrimonio."},
    ],
    tiers={
        "recovery": [
            ex(f"{I4} ¿Cómo se llamaban los corredores que llevaban mensajes?", "chasquis", "La ficha los nombra."),
            ex(f"{I4} ¿Qué era un tambo?", "una casa de descanso con alimentos y mantas", "La ficha lo define así."),
            ex(f"{I4} ¿Qué dios era el Sol para los incas?", "Inti", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{I4} ¿Para qué servía el Qhapaq Ñan?", "para unir Cusco con todo el imperio", "La ficha lo dice."),
            ex(f"{I4} ¿Qué es la Pachamama?", "la Madre Tierra", "La ficha lo indica."),
            ex(f"{I4} ¿Qué idioma hablan hoy millones de personas en los Andes?", "quechua", "La ficha lo indica."),
        ],
        "apply": [
            arith(f"{I4} Imagina un tramo de camino de 24 kilómetros con un relevo cada 6 kilómetros. ¿Cuántos chasquis harían falta si cada uno corre un tramo de 6 kilómetros?", "24//6", "Se divide el camino en tramos de 6 kilómetros.", " chasquis"),
            ex(f"{I4} Clasifica como «cambio» o «continuidad»: hoy millones de personas hablan quechua.", "continuidad", "Es una lengua que viene desde la época inca."),
            ex(f"{I4} Clasifica como «cambio» o «continuidad»: ya no hay un Sapa Inca que gobierne el imperio.", "cambio", "El imperio terminó."),
        ],
        "reason": [
            ex(f"{I4} Sofía dice: «Los incas hacían sacrificios humanos todo el tiempo». ¿Qué dice realmente la ficha?", "Que según las crónicas hubo sacrificios humanos solo en ceremonias muy especiales", "La ficha limita el dato."),
            ex(f"{I4} Pedro dice que el cronista y el autor indígena opinan igual sobre el camino. ¿Es cierto?", "No, uno destaca su utilidad para el imperio y el otro la carga de trabajo del pueblo", "Tienen perspectivas distintas."),
        ],
        "challenge": [
            ex(f"{I4} ¿Qué fuente te sirve más para saber cómo vivió la gente común el trabajo del camino: la del cronista o la del autor indígena?", "la del autor indígena", "Muestra la carga de trabajo del pueblo."),
            ex(f"{I4} Clasifica en «comunicaciones», «religión» o «construcciones»: a) chasquis; b) Inti; c) muros de piedras ajustadas.", "a: comunicaciones; b: religión; c: construcciones", "Cada dato corresponde a una dimensión distinta."),
        ],
    },
    context=[ex("Una excursión camina por un tramo de piedra del Qhapaq Ñan. ¿Qué cambió y qué continúa en ese camino?", "cambió que ya no lo usan los chasquis del imperio; continúa que el camino sigue y se protege", "El camino sigue presente como patrimonio.")],
    selfcheck=[
        ex("¿Qué llevaban los chasquis?", "mensajes", "Eran corredores que llevaban noticias."),
        ex("¿Qué es el Qhapaq Ñan?", "una red de caminos que unía Cusco con el imperio", "Era el camino principal del imperio."),
        ex("¿Qué continuidad inca se mantiene hoy en los Andes?", "el quechua", "Millones de personas lo hablan."),
    ],
    open_task=task(
        f"Dibuja una línea de camino con tres tambos y dos chasquis, uno en cada tramo, y escribe encima «Qhapaq Ñan». Después escribe una frase con un cambio y otra con una continuidad entre el imperio inca y hoy. {I4}",
        "Camino con tres tambos y dos chasquis. Cambio: ya no hay Sapa Inca. Continuidad: se habla quechua y el camino es patrimonio.",
        ["camino con tambos y chasquis", "un cambio", "una continuidad"], ["dibujo", "dos frases"], ["dibujar a los chasquis a caballo", "confundir cambio con continuidad"],
        "Pregunta para qué había tambos cada cierto trecho. La respuesta esperada es que los chasquis descansaran y se alimentaran."),
    reinforce="Explica en voz alta cómo viajaba un mensaje inca y qué continúa hoy.",
    extend="Escribe una pregunta para el cronista español y otra para el autor indígena sobre el camino.",
)

# ---------------------------------------------------------------- clase 5
I5 = ("Ficha inca 5: Un historiador se pregunta cómo los incas pudieron gobernar un imperio tan grande. Reúne estos datos. (1) Una red de caminos unía el territorio. (2) Los chasquis llevaban mensajes con rapidez. "
      "(3) Los quipus registraban cantidades de personas, animales y productos. (4) El Estado guardaba alimentos en almacenes. (5) Los pueblos del imperio hacían trabajo por turnos, la mita. "
      "(6) Se difundió el quechua como lengua común. (7) Los especialistas no pueden leer con seguridad todo lo que dicen los quipus.")
register(
    OA3, 5,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a defender una conclusión sobre el imperio inca con evidencia y a reconocer un límite. Sirve para argumentar en historia sin inventar.",
    prior=["Sé que un argumento tiene afirmación, evidencia y límite.", "Sé cómo era la economía y la comunicación inca."],
    explain=[
        "Un imperio tan grande como el inca necesitaba organización. La pregunta de hoy es: ¿cómo lograron gobernar un territorio tan extenso? Para responder, usamos los datos de la ficha como evidencia y armamos un argumento con afirmación, evidencia y límite.",
        "Una buena afirmación es que el Estado inca se organizó con comunicaciones, registro y reparto del trabajo. La evidencia son los caminos, los chasquis, los quipus, los almacenes, la mita y el quechua como lengua común. Cada dato muestra una forma de conectar y administrar el imperio.",
        "También hay un límite. Los especialistas no pueden leer con seguridad todo lo que dicen los quipus. Entonces no podemos saber con exactitud cuánta información guardaban. Un buen argumento admite esto y no inventa. Dice: «el Estado se organizó con estos medios, aunque todavía hay cosas que no sabemos».",
    ],
    vocab=[("administrar", "organizar y dirigir algo, como un territorio"), ("lengua común", "idioma que entienden personas de muchos pueblos"), ("evidencia", "dato o fuente que apoya una idea"), ("límite", "lo que no sabemos o no podemos afirmar"), ("conclusión", "idea final después de analizar")],
    worked=[
        {"title": "Elegir evidencia", "problem": f"{I5} Afirmación: «Los incas lograban comunicar rápido el imperio». ¿Qué datos la apoyan?", "steps": ["Busco datos sobre comunicación.", "Los datos 1 y 2: caminos y chasquis."], "answer": "La red de caminos y los chasquis"},
        {"title": "Reconocer un límite", "problem": f"{I5} ¿Podemos saber exactamente toda la información de los quipus?", "steps": ["Busco el dato 7.", "Dice que los especialistas no pueden leerlo todo con seguridad."], "answer": "No, no todo se puede leer con seguridad"},
    ],
    mistakes=[
        {"wrong": "Decir que un solo medio, como los caminos, explica todo el gobierno inca.", "why": "Se usa una sola pista.", "fix": "Usa varios datos: caminos, quipus, almacenes, mita y lengua."},
        {"wrong": "Afirmar que sabemos todo lo que decían los quipus.", "why": "Se ignora el límite.", "fix": "Di que los especialistas no pueden leer todo con seguridad."},
    ],
    tiers={
        "recovery": [
            ex(f"{I5} ¿Quiénes llevaban mensajes con rapidez?", "los chasquis", "Es el dato 2."),
            ex(f"{I5} ¿Qué lengua se difundió como lengua común?", "el quechua", "Es el dato 6."),
            ex(f"{I5} ¿Qué registraban los quipus?", "cantidades de personas, animales y productos", "Es el dato 3."),
        ],
        "understand": [
            ex(f"{I5} ¿Qué guardaba el Estado en los almacenes?", "alimentos", "Es el dato 4."),
            ex(f"{I5} ¿Cómo se llamaba el trabajo por turnos?", "mita", "Es el dato 5."),
            ex(f"{I5} ¿Qué nos muestra el dato 7 sobre los quipus?", "que hay cosas que no podemos leer con seguridad", "Marca el límite del conocimiento."),
        ],
        "apply": [
            ex(f"{I5} Afirmación: «El Estado inca podía repartir alimentos». ¿Qué dato la apoya?", "el dato 4, los almacenes", "Guardaba alimentos para repartirlos."),
            ex(f"{I5} Afirmación: «Los incas podían entenderse entre pueblos distintos». ¿Qué dato la apoya?", "el dato 6, el quechua como lengua común", "Una lengua común facilita entenderse."),
            ex(f"{I5} Elige la mejor conclusión. A) Los quipus eran escritura con letras. B) Los incas gobernaron con caminos, mensajeros, registros y trabajo organizado, aunque no todo se conoce.", "B", "B usa varios datos y reconoce un límite."),
        ],
        "reason": [
            ex(f"{I5} Rosa dice: «Los caminos eran lo único que mantenía unido el imperio». ¿Qué otros dos datos de la ficha muestran que no era lo único?", "Los quipus y los almacenes, por ejemplo", "Hubo otros medios de organización."),
            ex(f"{I5} Pedro dice: «Entendemos por completo los quipus». ¿Qué dato lo corrige?", "El dato 7: los especialistas no pueden leerlos con seguridad", "La ficha reconoce un límite."),
        ],
        "challenge": [
            ex(f"{I5} Marca cada parte: afirmación, evidencia o límite. a) «Los incas organizaron bien su imperio». b) «Los chasquis llevaban mensajes con rapidez». c) «No se puede leer todo lo de los quipus».", "a: afirmación; b: evidencia; c: límite", "Cada frase cumple una función distinta."),
            ex(f"{I5} Dos estudiantes: Eva dice «Los incas gobernaron solo por la fuerza». Luis dice «Usaron caminos, registros y trabajo organizado». ¿Quién tiene más apoyo en la ficha?", "Luis", "La ficha no habla de fuerza, solo de medios de organización."),
        ],
    },
    context=[ex("Un turista dice: «Los incas no tenían cómo organizarse sin escritura». ¿Qué dato de la ficha usarías para responderle?", "Los quipus registraban cantidades de personas, animales y productos", "Muestra otra forma de registro.")],
    selfcheck=[
        ex("¿Qué dos datos muestran la comunicación en el imperio inca?", "los caminos y los chasquis", "Conectaban el territorio."),
        ex("¿Qué es un límite en un argumento?", "lo que no sabemos o no podemos afirmar", "Un buen argumento lo reconoce."),
        ex("¿Qué lengua común se difundió en el imperio?", "el quechua", "Facilitaba entenderse entre pueblos."),
    ],
    open_task=task(
        f"Responde por escrito: «¿Cómo gobernaron los incas un imperio tan grande?». Escribe cuatro frases: una afirmación, dos evidencias de la ficha y un límite. {I5}",
        "Pienso que los incas se organizaron con comunicaciones y registros. Tenían caminos y chasquis. También usaban quipus para registrar cantidades. Todavía no se pueden leer con seguridad todos los quipus.",
        ["afirmación clara", "dos evidencias de la ficha", "un límite"], ["cuatro frases"], ["usar una sola evidencia", "olvidar el límite"],
        "Pide que subraye la afirmación, encierre las evidencias y marque el límite."),
    reinforce="Explica a alguien de tu casa una forma en que los incas comunicaban su imperio.",
    extend="Escribe qué otra fuente necesitarías para saber más sobre cómo se repartía el trabajo.",
)

# ================================================================ OA 04 · COMPARACIÓN
# ---------------------------------------------------------------- clase 1
C1 = ("Ficha comparativa 1: MAYAS: sur de México y Centroamérica (parte sur de Mesoamérica); período clásico entre 250 y 900 d.C.; ciudades-estado. "
      "AZTECAS: centro de México; capital Tenochtitlán, fundada hacia 1325; imperio hasta 1521. "
      "INCAS: Andes de América del Sur; capital Cusco; imperio que creció en el siglo XV y terminó hacia 1532.")
register(
    OA4, 1,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio. Un mapa de América ayuda, pero no es necesario.",
    use="Aprenderé a comparar cuándo y dónde vivieron mayas, aztecas e incas. Sirve para no mezclar sus historias.",
    prior=["Sé dónde y cuándo vivió cada civilización.", "Sé leer una línea de tiempo."],
    explain=[
        "Comparar es mirar dos o más cosas para ver en qué se parecen y en qué se diferencian. Para comparar civilizaciones, primero necesitamos ubicarlas bien: dónde vivieron y en qué época. Los mayas, los aztecas y los incas fueron civilizaciones distintas y no vivieron todos en el mismo lugar ni al mismo tiempo.",
        "Los mayas vivieron en el sur de México y en Centroamérica, sobre todo entre 250 y 900 d.C., en ciudades-estado. Los aztecas vivieron en el centro de México y fundaron Tenochtitlán hacia 1325. Los incas vivieron en los Andes de América del Sur y su imperio creció en el siglo XV. Los aztecas y los incas coincidieron en el tiempo, y los mayas del período clásico fueron anteriores.",
        "Dos civilizaciones pueden compartir tiempo pero no lugar. Los aztecas y los incas vivieron al mismo tiempo, pero sin ser vecinos: unos en el centro de México y otros en los Andes. Una línea de tiempo y un mapa ayudan a comprobarlo.",
    ],
    vocab=[("comparar", "mirar en qué se parecen y en qué se diferencian dos o más cosas"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas son distintas"), ("simultáneo", "que ocurre al mismo tiempo"), ("línea de tiempo", "dibujo que ordena hechos por fecha")],
    worked=[
        {"title": "Ordenar en el tiempo", "problem": f"{C1} ¿Cuál civilización tuvo su período clásico antes: la maya o la azteca?", "steps": ["El período clásico maya termina en 900 d.C.", "Tenochtitlán se funda hacia 1325."], "answer": "La maya, porque terminó en 900 y los aztecas fundaron su capital hacia 1325"},
        {"title": "Ubicar en el espacio", "problem": f"{C1} ¿Cuál civilización vivió en América del Sur?", "steps": ["Busco quién vivió en los Andes de América del Sur.", "La ficha dice que fueron los incas."], "answer": "Los incas"},
    ],
    mistakes=[
        {"wrong": "Decir que mayas, aztecas e incas eran vecinos y vivían en el mismo lugar.", "why": "Se mezclan las tres civilizaciones.", "fix": "Ubica cada una en el mapa antes de comparar."},
        {"wrong": "Decir que los tres vivieron exactamente en la misma época.", "why": "No se revisan las fechas.", "fix": "Compara fechas: el clásico maya fue antes que aztecas e incas."},
    ],
    tiers={
        "recovery": [
            ex(f"{C1} ¿Qué civilización vivió en los Andes?", "los incas", "La ficha los ubica ahí."),
            ex(f"{C1} ¿Qué civilización fundó Tenochtitlán?", "los aztecas", "La ficha lo indica."),
            ex(f"{C1} ¿Cuál civilización tenía ciudades-estado?", "los mayas", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{C1} ¿Qué dos civilizaciones vivieron en México actual?", "los mayas (sur) y los aztecas (centro)", "La ficha ubica a ambas en México."),
            ex(f"{C1} ¿Qué es comparar?", "mirar en qué se parecen y en qué se diferencian", "Así se define comparar."),
            ex(f"{C1} ¿Cuál de las tres civilizaciones es anterior a las otras dos?", "la maya clásica", "Su período clásico terminó en 900."),
        ],
        "apply": [
            arith(f"{C1} El período clásico maya terminó en 900 y Tenochtitlán se fundó hacia 1325. ¿Cuántos años hay entre ambos hechos?", "1325-900", "Se resta el año posterior menos el anterior.", " años"),
            ex(f"{C1} Los aztecas fundaron su capital hacia 1325 y el imperio inca creció en el siglo XV. ¿Alguno de estos hechos fue claramente posterior al otro?", "El imperio inca creció después de la fundación de Tenochtitlán", "El siglo XV es posterior a 1325."),
            ex(f"{C1} ¿Cuál de las capitales de la ficha estaba más al sur: Tenochtitlán o Cusco?", "Cusco", "Cusco está en América del Sur."),
        ],
        "reason": [
            ex(f"{C1} Tomás dice: «Los aztecas y los incas vivieron al mismo tiempo, así que eran vecinos». ¿Qué datos de la ficha lo corrigen?", "Los aztecas vivieron en el centro de México y los incas en los Andes de América del Sur, lejos entre sí", "Coincidir en el tiempo no significa estar cerca."),
            ex(f"{C1} Ana dice: «Los mayas clásicos vieron a los aztecas fundar Tenochtitlán». ¿Qué dato de la ficha lo contradice?", "El período clásico maya terminó en 900 y Tenochtitlán se fundó hacia 1325", "Hay más de 400 años entre ambos."),
        ],
        "challenge": [
            ex(f"{C1} Clasifica cada dato en «dónde» o «cuándo»: a) Andes; b) siglo XV; c) centro de México; d) entre 250 y 900 d.C.", "a: dónde; b: cuándo; c: dónde; d: cuándo", "Dos nombran lugares y dos nombran épocas."),
            ex(f"{C1} Ordena de más antigua a más reciente la época de máximo desarrollo: aztecas (1325 a 1521), mayas (período clásico), incas (siglo XV).", "mayas, aztecas e incas (los dos últimos coinciden en el tiempo)", "El clásico maya precede a ambos; los otros dos se solapan."),
        ],
    },
    context=[ex("En un museo hay tres vitrinas: una de Tikal, una de Tenochtitlán y una de Cusco. ¿Qué civilización corresponde a cada una, en ese orden?", "mayas, aztecas e incas", "Cada ciudad pertenece a una civilización distinta.")],
    selfcheck=[
        ex("¿En qué región vivieron los mayas?", "en el sur de México y en Centroamérica", "La ficha los ubica ahí."),
        ex("¿Qué civilización vivió en los Andes?", "los incas", "Su capital fue Cusco."),
        ex("En Historia: ¿Qué es una semejanza?", "algo en que dos cosas se parecen", "Es lo contrario de una diferencia."),
    ],
    open_task=task(
        f"Haz dos dibujos. Primero, un mapa simple de América con tres manchas: sur de México y Centroamérica (mayas), centro de México (aztecas) y Andes (incas). Segundo, una línea de tiempo con los puntos 250, 900, 1325, 1500 y 1532, y escribe debajo qué civilización corresponde a cada punto. {C1}",
        "Mapa con tres manchas y línea de tiempo con 250 y 900 maya, 1325 azteca, 1500 y 1532 inca.",
        ["tres civilizaciones ubicadas", "años en orden", "civilización correcta por año"], ["mapa", "línea de tiempo"], ["mezclar las manchas", "ubicar a los incas en México"],
        "Pregunta cuáles dos civilizaciones coinciden en el tiempo y si eran vecinas."),
    reinforce="Cuenta dónde y cuándo vivió cada civilización sin mirar la ficha.",
    extend="Escribe dos preguntas que te gustaría comparar entre aztecas e incas.",
)

# ---------------------------------------------------------------- clase 2
C2 = ("Ficha comparativa 2: Fuentes de cada civilización. MAYAS: una estela con jeroglíficos hecha por una ciudad maya, y un códice de papel de corteza. "
      "AZTECAS: la Piedra del Sol, el Templo Mayor y un códice pintado por escribas indígenas por encargo de una autoridad española. "
      "INCAS: Machu Picchu, un quipu de cuerdas con nudos y un libro dibujado por un autor indígena andino. "
      "Los tres pueblos también aparecen en textos escritos por españoles del siglo XVI.")
register(
    OA4, 2,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a comparar qué fuentes dejaron mayas, aztecas e incas y cuánto nos dicen. Sirve para saber por qué conocemos a unos más que a otros en ciertos temas.",
    prior=["Sé qué es una fuente y qué es la procedencia.", "Sé qué son una estela, un códice y un quipu."],
    explain=[
        "Cada civilización dejó fuentes distintas. Los mayas dejaron estelas con jeroglíficos y códices. Los aztecas dejaron la Piedra del Sol, el Templo Mayor y un códice pintado después de la conquista. Los incas dejaron ciudades de piedra como Machu Picchu, quipus y un libro dibujado por un autor andino.",
        "Algunas fuentes tienen escritura con signos, como los jeroglíficos mayas. Otras registran de otra manera, como el quipu inca, que usa nudos para guardar cantidades. Por eso no podemos comparar el tipo de «escritura» sin explicar bien cada caso. Lo importante es preguntar qué información da cada fuente y qué no da.",
        "Además, de las tres civilizaciones existen textos escritos por españoles del siglo XVI. Esos textos son útiles, pero vienen de otra cultura y se escribieron en una situación de conquista. Para comparar bien, debemos cruzar varias fuentes: las que dejaron los propios pueblos y las de otros.",
    ],
    vocab=[("jeroglífico", "signo de la escritura maya"), ("quipu", "cuerdas con nudos para registrar cantidades"), ("códice", "libro pintado a mano"), ("cruzar fuentes", "comparar varias fuentes para confirmar un dato"), ("procedencia", "quién hizo la fuente, cuándo y para qué")],
    worked=[
        {"title": "Comparar tipos de fuente", "problem": f"{C2} ¿Qué diferencia hay entre una estela maya y un quipu inca?", "steps": ["La estela tiene jeroglíficos y dibujos tallados en piedra.", "El quipu usa cuerdas con nudos para guardar cantidades."], "answer": "La estela es piedra con signos; el quipu son cuerdas con nudos"},
        {"title": "Reconocer lo común", "problem": f"{C2} ¿Qué tienen en común los tres pueblos en cuanto a textos escritos por españoles?", "steps": ["Busco la última frase de la ficha.", "Los tres aparecen en textos de españoles del siglo XVI."], "answer": "Los tres aparecen en textos escritos por españoles del siglo XVI"},
    ],
    mistakes=[
        {"wrong": "Decir que el quipu era escritura con letras como la maya.", "why": "Se mezclan sistemas de registro.", "fix": "El quipu registraba cantidades con nudos; los jeroglíficos eran signos de escritura."},
        {"wrong": "Usar solo los textos de los españoles para comparar a las tres civilizaciones.", "why": "Se olvida su perspectiva externa.", "fix": "Cruza con fuentes hechas por los propios pueblos."},
    ],
    tiers={
        "recovery": [
            ex(f"{C2} ¿Qué fuente maya tiene jeroglíficos y es de piedra?", "la estela", "La ficha la nombra."),
            ex(f"{C2} ¿Qué fuente inca registra con nudos?", "el quipu", "La ficha lo indica."),
            ex(f"{C2} ¿Qué fuente azteca es un disco de piedra con el calendario?", "la Piedra del Sol", "La ficha la nombra."),
        ],
        "understand": [
            ex(f"{C2} ¿Qué tienen en común las fuentes de las tres civilizaciones sobre los textos de los españoles?", "los tres pueblos aparecen en textos de españoles del siglo XVI", "Lo dice la última frase."),
            ex(f"{C2} ¿El códice azteca fue encargado por los propios aztecas?", "No, por una autoridad española", "La ficha lo indica."),
            ex(f"{C2} ¿Qué fuente inca es una ciudad de piedra?", "Machu Picchu", "La ficha la nombra."),
        ],
        "apply": [
            ex(f"{C2} Quieres estudiar el calendario azteca. ¿Qué fuente usas?", "la Piedra del Sol", "Tiene signos del calendario."),
            ex(f"{C2} Quieres estudiar cómo registraban cantidades los incas. ¿Qué fuente usas?", "el quipu", "El quipu registraba cantidades."),
            ex(f"{C2} Quieres leer la versión de un gobernante maya sobre sus triunfos. ¿Qué fuente usas?", "la estela", "Cuenta los triunfos del gobernante."),
        ],
        "reason": [
            ex(f"{C2} Pedro dice: «Los españoles fueron testigos neutrales de las tres civilizaciones». ¿Qué problema tiene su frase?", "Los españoles escribían desde otra cultura y en una situación de conquista", "No son fuentes neutrales."),
            ex(f"{C2} Clara dice: «Con una sola fuente alcanza para comparar a los tres pueblos». ¿Qué debería hacer en cambio?", "Cruzar varias fuentes de cada pueblo", "Una fuente es solo una pista."),
        ],
        "challenge": [
            ex(f"{C2} Elige la pregunta que sirve para comparar fuentes. A) ¿Quién las hizo, cuándo y para qué? B) ¿Cuál civilización era mejor?", "A", "B no se responde con la procedencia de las fuentes."),
            ex(f"{C2} Une cada civilización con una fuente suya: A) mayas; B) aztecas; C) incas. 1) Piedra del Sol; 2) quipu; 3) estela con jeroglíficos.", "A con 3; B con 1; C con 2", "Cada fuente pertenece a una civilización."),
        ],
    },
    context=[ex("En un museo ves un cordón con muchos nudos de colores. ¿De qué civilización es y qué registraba?", "de los incas; registraba cantidades", "El quipu inca servía para guardar cantidades.")],
    selfcheck=[
        ex("¿Qué es un quipu?", "cuerdas con nudos de colores para registrar cantidades", "Era el sistema de registro inca."),
        ex("¿Qué son los jeroglíficos mayas?", "signos de la escritura maya", "Se tallaban en estelas y se pintaban en códices."),
        ex("¿Por qué conviene cruzar varias fuentes?", "porque cada una es solo una pista", "Cruzar permite confirmar los datos."),
    ],
    open_task=task(
        f"Haz una tabla de tres filas (mayas, aztecas, incas) y dos columnas: «una fuente» y «qué información da». Completa cada fila con una fuente de la ficha. Después escribe una frase que diga qué fuente nueva te gustaría tener para comparar mejor. {C2}",
        "Mayas: estela, da los triunfos del gobernante. Aztecas: Piedra del Sol, da el calendario. Incas: quipu, da cantidades. Me gustaría una fuente escrita por un campesino de cada pueblo.",
        ["tres filas completas", "información coherente con la fuente", "una fuente nueva propuesta"], ["tabla de tres filas", "una frase"], ["mezclar fuentes de un pueblo con otro", "decir que el quipu era escritura con letras"],
        "Pregunta qué fuente le da más información y por qué."),
    reinforce="Nombra una fuente de cada civilización y qué información da.",
    extend="Escribe una razón por la que un texto de un español del siglo XVI puede no contar toda la verdad.",
)

# ---------------------------------------------------------------- clase 3
C3 = ("Ficha comparativa 3: ORGANIZACIÓN POLÍTICA. Mayas: ciudades-estado con gobernante propio. Aztecas: imperio con emperador en Tenochtitlán. Incas: imperio con Sapa Inca en Cusco. "
      "CULTIVO. Mayas: milpa. Aztecas: chinampas. Incas: andenes. "
      "ALIMENTOS (ejemplos). Mayas: maíz, frijol, zapallo, chile y cacao. Aztecas: maíz, frijol, zapallo, chile, tomate y cacao. Incas: papa, maíz, quinua. "
      "CONSTRUCCIONES. Mayas: pirámides escalonadas con templo. Aztecas: Templo Mayor y calzadas. Incas: muros de piedra ajustada y Machu Picchu. "
      "SABERES. Mayas: jeroglíficos, calendario y cero. Aztecas: calendario de la Piedra del Sol. Incas: quipu y chasquis. "
      "SOCIEDAD. Mayas: gobernante y nobles, sacerdotes y escribas, comerciantes y artesanos, campesinos. Aztecas: emperador y nobles, sacerdotes y guerreros, comerciantes y artesanos, campesinos. Incas: Sapa Inca y nobles, funcionarios, gente común.")
register(
    OA4, 3,
    materials="Lápiz y papel. La tabla comparativa está escrita en cada ejercicio.",
    use="Aprenderé a ordenar los rasgos de mayas, aztecas e incas en una tabla para compararlos con evidencia. Sirve para ver semejanzas y diferencias con claridad.",
    prior=["Sé las características de cada civilización por separado.", "Sé qué es una semejanza y una diferencia."],
    explain=[
        "Una forma ordenada de comparar es usar criterios. Un criterio es el aspecto que miramos en todas las civilizaciones: la organización política, la sociedad, el cultivo, los alimentos, las construcciones y los saberes. Con criterios no comparamos al azar, sino siempre lo mismo en cada pueblo.",
        "Por ejemplo, en organización política, los mayas tenían ciudades-estado y los aztecas y los incas tenían imperios. En cultivo, los mayas usaban la milpa, los aztecas las chinampas y los incas los andenes. En alimentos, el maíz aparece en los tres, y cada pueblo tenía además otros alimentos propios, como el cacao, el tomate o la papa.",
        "En construcciones, los mayas levantaron pirámides escalonadas con templo, los aztecas el Templo Mayor y calzadas, y los incas muros de piedra muy ajustada. En saberes, los mayas destacaron por sus jeroglíficos, su calendario y el cero; los aztecas por su calendario; los incas por el quipu y los chasquis. En la sociedad, los tres pueblos tenían nobles en la cima y una mayoría de campesinos o gente común.",
    ],
    vocab=[("criterio", "aspecto que se mira para comparar"), ("organización política", "forma de gobernar"), ("cultivo", "forma de sembrar la tierra"), ("saberes", "conocimientos que una cultura desarrolló"), ("tabla comparativa", "cuadro que ordena rasgos para compararlos")],
    worked=[
        {"title": "Comparar con un criterio", "problem": f"{C3} Compara la organización política de mayas e incas.", "steps": ["Mayas: ciudades-estado con gobernante propio.", "Incas: un imperio con Sapa Inca en Cusco."], "answer": "Los mayas tenían varias ciudades-estado; los incas, un solo imperio con un Sapa Inca"},
        {"title": "Encontrar una semejanza", "problem": f"{C3} ¿Qué alimento aparece en los tres pueblos?", "steps": ["Reviso la fila de alimentos.", "El maíz está en los tres."], "answer": "El maíz"},
    ],
    mistakes=[
        {"wrong": "Comparar un rasgo de un pueblo con un aspecto distinto de otro.", "why": "No se usa el mismo criterio.", "fix": "Compara siempre el mismo criterio, por ejemplo cultivo con cultivo."},
        {"wrong": "Decir que los tres pueblos cultivaban igual.", "why": "Se ignoran las diferencias.", "fix": "Cada uno tenía su forma: milpa, chinampa o andén."},
    ],
    tiers={
        "recovery": [
            ex(f"{C3} ¿Qué forma de cultivo tenían los incas?", "andenes", "La tabla lo indica."),
            ex(f"{C3} ¿Qué forma de cultivo tenían los aztecas?", "chinampas", "La tabla lo indica."),
            ex(f"{C3} ¿Qué forma de cultivo tenían los mayas?", "milpa", "La tabla lo indica."),
        ],
        "understand": [
            ex(f"{C3} ¿Qué alimento aparece en las tres civilizaciones?", "el maíz", "Está en los tres."),
            ex(f"{C3} ¿Cuáles de las tres civilizaciones formaron imperios?", "los aztecas y los incas", "Los mayas tenían ciudades-estado."),
            ex(f"{C3} En las tres civilizaciones, ¿qué grupo estaba en la cima de la sociedad junto al gobernante: los nobles o los comerciantes?", "los nobles", "La fila de sociedad nombra a los nobles junto al gobernante en las tres."),
        ],
        "apply": [
            ex(f"{C3} ¿Qué alimento de la tabla aparece en la fila de los incas y no en la de mayas ni aztecas: la papa o el chile?", "la papa", "El chile está en las filas de mayas y aztecas."),
            ex(f"{C3} ¿Qué alimento aparece en las filas de mayas y aztecas, pero no en la de los incas: el cacao o la quinua?", "el cacao", "La quinua es de los incas."),
            ex(f"{C3} Una construcción de muros de piedra bien ajustada, ¿a qué civilización corresponde?", "a los incas", "La tabla lo indica."),
        ],
        "reason": [
            ex(f"{C3} Luis dice: «Los tres pueblos tenían imperios». ¿Qué dato de la tabla lo corrige?", "Los mayas tenían ciudades-estado", "Solo aztecas e incas formaron imperios."),
            ex(f"{C3} Ana dice: «El cero solo existía en los incas». ¿Qué dato de la tabla la contradice?", "Los mayas tenían el cero", "El cero aparece en la fila maya."),
        ],
        "challenge": [
            ex(f"{C3} Clasifica cada rasgo con su criterio (cultivo, construcciones o saberes): a) quipu; b) andenes; c) Templo Mayor.", "a: saberes; b: cultivo; c: construcciones", "Cada rasgo responde a un criterio."),
            ex(f"{C3} Los aztecas vivían en una isla de un lago y los incas, en laderas de cerros. ¿Qué cultivo usaba cada uno, en ese orden?", "chinampas y andenes", "Cada forma de cultivo se adaptó al lugar donde vivían."),
        ],
    },
    context=[ex("En una clase, tres grupos dibujan una pirámide escalonada con templo, una calzada sobre un lago y un muro de piedra ajustada. ¿A qué civilización corresponde cada dibujo, en ese orden?", "maya, azteca e inca", "Son los ejemplos de construcciones de la tabla.")],
    selfcheck=[
        ex("¿Qué criterio compara milpa, chinampas y andenes?", "el cultivo", "Son las tres formas de cultivar."),
        ex("¿Qué dos civilizaciones formaron imperios?", "los aztecas y los incas", "Los mayas eran ciudades-estado."),
        ex("¿Qué civilización de la tabla tenía jeroglíficos y cero?", "los mayas", "Ambos saberes aparecen en la fila maya."),
    ],
    open_task=task(
        f"Copia en una hoja una tabla con tres columnas (mayas, aztecas, incas) y seis filas (organización política, sociedad, cultivo, alimentos, construcciones, saberes). Rellénala con los datos de la ficha. Marca con verde una semejanza y con rojo una diferencia. {C3}",
        "Tabla completa. Semejanza: el maíz. Diferencia: los mayas tenían ciudades-estado y los otros, imperios.",
        ["tabla completa", "una semejanza", "una diferencia"], ["tabla con seis filas"], ["comparar distintos criterios entre sí", "olvidar a una civilización"],
        "Pregunta qué fila fue más fácil de comparar y por qué."),
    reinforce="Elige una fila de la tabla y explícala en voz alta.",
    extend="Agrega una fila a la tabla: ¿qué otro criterio te gustaría comparar?",
)

# ---------------------------------------------------------------- clase 4
C4 = ("Ficha comparativa 4: Semejanzas y diferencias entre las tres civilizaciones. "
      "(1) Las tres cultivaban maíz. (2) Las tres adoraban a muchos dioses y hacían ofrendas. (3) Los mayas se organizaban en ciudades-estado; aztecas e incas, en imperios que cobraban tributo o trabajo. "
      "(4) Los mayas escribían con jeroglíficos; los incas registraban cantidades con quipus. (5) Los incas no usaban dinero; los aztecas cobraban tributo en productos. "
      "Perspectivas: un cronista español comparó los imperios con los reinos de Europa. Un autor indígena los describió desde su propia experiencia.")
register(
    OA4, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a escribir semejanzas y diferencias entre las tres civilizaciones y a notar cuándo una comparación depende de la perspectiva de quien la hace.",
    prior=["Sé comparar con criterios.", "Sé que una perspectiva es un punto de vista."],
    explain=[
        "Para comparar bien escribimos semejanzas y diferencias. Una semejanza es algo que dos o más pueblos tienen en común, como cultivar maíz o adorar a muchos dioses. Una diferencia es algo que los separa, como las ciudades-estado mayas frente a los imperios azteca e inca.",
        "También conviene notar que los pueblos cambian con el tiempo, y que las comparaciones se hacen desde una perspectiva. Un cronista español comparó los imperios con los reinos de Europa, porque pensaba desde su mundo. Un autor indígena los describió desde su experiencia. Ninguna de las dos miradas es completa.",
        "Una buena comparación usa un criterio claro y datos concretos. No dice «unos eran mejores». Dice, por ejemplo: «los mayas se organizaron en ciudades-estado, mientras los aztecas y los incas formaron imperios». Así comparamos con evidencia, sin juicios apresurados.",
    ],
    vocab=[("semejanza", "algo que dos o más cosas tienen en común"), ("diferencia", "algo que separa a dos o más cosas"), ("perspectiva", "punto de vista de quien cuenta o compara"), ("dioses", "seres que se adoran en una religión"), ("juicio apresurado", "opinión sin suficiente evidencia")],
    worked=[
        {"title": "Escribir una semejanza", "problem": f"{C4} Escribe una semejanza entre las tres civilizaciones.", "steps": ["Busco algo que aparezca en las tres.", "Las tres cultivaban maíz y adoraban a muchos dioses."], "answer": "Las tres cultivaban maíz y adoraban a muchos dioses"},
        {"title": "Escribir una diferencia", "problem": f"{C4} Escribe una diferencia entre mayas e incas.", "steps": ["Miro la organización política.", "Los mayas tenían ciudades-estado y los incas, un imperio."], "answer": "Los mayas tenían ciudades-estado y los incas formaron un imperio"},
    ],
    mistakes=[
        {"wrong": "Decir «los incas eran mejores porque no usaban dinero».", "why": "Se mezclan juicios con comparaciones.", "fix": "Describe con datos: «los incas no usaban dinero y organizaban el trabajo con la mita»."},
        {"wrong": "Decir que las tres civilizaciones eran iguales.", "why": "Se ignoran las diferencias.", "fix": "Busca siempre tanto semejanzas como diferencias."},
    ],
    tiers={
        "recovery": [
            ex(f"{C4} ¿Qué cultivaban las tres civilizaciones?", "maíz", "Es la semejanza (1) de la ficha."),
            ex(f"{C4} ¿Cuántos dioses adoraban las tres civilizaciones: uno o muchos?", "muchos", "La semejanza (2) lo indica."),
            ex(f"{C4} ¿Qué civilización no formó un imperio?", "la maya", "Se organizó en ciudades-estado."),
        ],
        "understand": [
            ex(f"{C4} ¿Qué usaban los incas para registrar cantidades, mientras los mayas escribían con jeroglíficos?", "quipus", "La ficha lo indica."),
            ex(f"{C4} ¿Con qué cobraban el tributo los aztecas?", "con productos", "La ficha dice que cobraban tributo en productos."),
            ex(f"{C4} ¿Qué mirada tenía el cronista español al comparar los imperios?", "los comparó con los reinos de Europa", "Pensaba desde su mundo."),
        ],
        "apply": [
            ex(f"{C4} Clasifica como «semejanza» o «diferencia»: las tres civilizaciones cultivaban maíz.", "semejanza", "Es un rasgo compartido."),
            ex(f"{C4} Clasifica como «semejanza» o «diferencia»: los mayas tenían ciudades-estado y los aztecas, un imperio.", "diferencia", "Los separa su organización política."),
            ex(f"{C4} Clasifica como «semejanza» o «diferencia»: los mayas escribían con jeroglíficos y los incas registraban con quipus.", "diferencia", "Cada pueblo usaba un sistema distinto."),
        ],
        "reason": [
            ex(f"{C4} Sofía dice: «Los aztecas eran mejores que los mayas porque tenían un imperio». ¿Qué problema tiene su afirmación?", "Es un juicio sin criterio, solo muestra que eran diferentes", "Tener un imperio no prueba que sean mejores."),
            ex(f"{C4} Pedro dice que comparar con los reinos de Europa es una mirada completa. ¿Qué falta?", "La mirada propia de los pueblos americanos", "Es una perspectiva externa."),
        ],
        "challenge": [
            ex(f"{C4} Completa la comparación: los aztecas cobraban tributo en ___, mientras los incas organizaban el trabajo por turnos llamado ___.", "productos; mita", "Cada Estado tenía su propio sistema para conseguir lo que necesitaba."),
            ex(f"{C4} Marca cuál frase es una comparación con evidencia. A) «Los incas eran más inteligentes». B) «Los incas usaron quipus y los mayas jeroglíficos».", "B", "B usa datos concretos."),
        ],
    },
    context=[ex("Un compañero dice: «Los tres pueblos eran iguales porque todos tenían pirámides». ¿Qué dos diferencias podrías mostrarle con la ficha?", "Los mayas tenían ciudades-estado y los otros imperios; los incas usaban quipus", "Hay diferencias de organización y de registro.")],
    selfcheck=[
        ex("En Historia: ¿Qué es una semejanza?", "algo que dos o más cosas tienen en común", "Es un rasgo compartido."),
        ex("En Historia: ¿Qué es una diferencia?", "algo que separa a dos o más cosas", "Es un rasgo que no comparten."),
        ex("¿Por qué no se debe decir que una civilización era mejor sin datos?", "porque sería un juicio apresurado", "Se debe comparar con evidencia."),
    ],
    open_task=task(
        f"Escribe tres semejanzas y tres diferencias entre las civilizaciones, usando datos de la ficha. Después subraya la frase que te parezca mejor sostenida con evidencia. {C4}",
        "Semejanzas: cultivo del maíz, adoración de muchos dioses, construcciones de piedra. Diferencias: ciudades-estado frente a imperios, quipus frente a jeroglíficos, mita frente a tributo.",
        ["tres semejanzas con datos", "tres diferencias con datos", "una frase subrayada"], ["lista de seis frases"], ["escribir juicios sin evidencia", "repetir el mismo dato"],
        "Pide que lea una diferencia y que explique de qué criterio viene."),
    reinforce="Di en voz alta una semejanza y una diferencia entre dos civilizaciones.",
    extend="Escribe una pregunta que le harías al cronista español sobre su forma de comparar.",
)

# ---------------------------------------------------------------- clase 5
C5 = ("Ficha comparativa 5: Pregunta: ¿cuál civilización tuvo la mejor red de comunicación? Datos. "
      "Mayas: caminos entre ciudades y escritura en estelas y códices. Aztecas: calzadas en la capital y mercados con mucha gente. Incas: Qhapaq Ñan de miles de kilómetros, chasquis, tambos y quipus. "
      "No existe una medida única de «mejor». Depende del criterio: extensión, velocidad, escritura o comercio. Además, no todas las fuentes entregan datos equivalentes de cada pueblo.")
register(
    OA4, 5,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a defender una conclusión comparativa con criterios claros y a decir cuándo la evidencia no alcanza. Sirve para no decir «el mejor» sin explicar por qué.",
    prior=["Sé comparar con criterios.", "Sé que un argumento tiene afirmación, evidencia y límite."],
    explain=[
        "Cuando alguien pregunta «¿cuál fue la mejor civilización?», lo primero es preguntar: ¿mejor en qué? No existe una medida única de «mejor». Hay que elegir un criterio, como extensión de los caminos, velocidad de los mensajes, escritura o comercio. Con el criterio claro, la comparación tiene sentido.",
        "Por ejemplo, si el criterio es la extensión de la red de comunicación, los incas destacan: el Qhapaq Ñan tenía miles de kilómetros, con chasquis y tambos. Si el criterio es la escritura con signos, los mayas destacan por sus jeroglíficos. Si el criterio es el comercio en una gran ciudad, los aztecas destacan por sus mercados.",
        "Un buen argumento comparativo dice el criterio, da evidencia y reconoce un límite. Aquí el límite es que las fuentes no entregan datos equivalentes de cada pueblo, por lo que la comparación no es perfecta. La conclusión debe ser honesta con lo que sabemos.",
    ],
    vocab=[("criterio", "aspecto que se usa para comparar"), ("extensión", "qué tan grande es algo"), ("equivalente", "que vale lo mismo o es comparable"), ("conclusión", "idea final después de analizar"), ("límite", "lo que no podemos afirmar")],
    worked=[
        {"title": "Elegir un criterio", "problem": f"{C5} Si el criterio es la extensión de la red de comunicación, ¿qué civilización destaca?", "steps": ["Busco datos de extensión.", "Los incas tenían el Qhapaq Ñan de miles de kilómetros."], "answer": "Los incas, con el Qhapaq Ñan"},
        {"title": "Cambiar el criterio", "problem": f"{C5} Si el criterio es la escritura con signos, ¿qué civilización destaca?", "steps": ["Busco datos de escritura.", "Los mayas escribían en estelas y códices."], "answer": "Los mayas"},
    ],
    mistakes=[
        {"wrong": "Decir «los incas fueron los mejores» sin decir en qué.", "why": "No se define un criterio.", "fix": "Di: «en extensión de caminos, los incas destacan»."},
        {"wrong": "Concluir con total certeza usando datos incompletos.", "why": "Se ignoran los límites.", "fix": "Reconoce que las fuentes no son equivalentes."},
    ],
    tiers={
        "recovery": [
            ex(f"{C5} ¿Qué red de comunicación tenía miles de kilómetros?", "el Qhapaq Ñan inca", "La ficha lo indica."),
            ex(f"{C5} ¿Qué pueblo destaca por sus mercados con mucha gente?", "los aztecas", "La ficha lo indica."),
            ex(f"{C5} ¿Qué pueblo destaca por escribir con jeroglíficos?", "los mayas", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{C5} ¿Existe una medida única de «mejor»?", "No", "La ficha dice que depende del criterio."),
            ex(f"{C5} ¿Qué cuatro criterios nombra la ficha?", "extensión, velocidad, escritura y comercio", "Son los criterios de la ficha."),
            ex(f"{C5} ¿Por qué la comparación no es perfecta?", "porque las fuentes no entregan datos equivalentes de cada pueblo", "La ficha lo indica."),
        ],
        "apply": [
            ex(f"{C5} Con el criterio «extensión», ¿qué civilización destaca?", "los incas", "El Qhapaq Ñan tenía miles de kilómetros."),
            ex(f"{C5} Con el criterio «comercio en la ciudad capital», ¿qué civilización destaca?", "los aztecas", "Sus mercados tenían mucha gente."),
            ex(f"{C5} Elige la mejor conclusión. A) Los incas fueron los mejores en todo. B) Los incas destacan en extensión de caminos, los mayas en escritura y los aztecas en mercados.", "B", "B usa criterios y datos."),
        ],
        "reason": [
            ex(f"{C5} Ema dice: «Los aztecas no tuvieron comunicaciones». ¿Qué dato de la ficha la contradice?", "Tenían calzadas y mercados con mucha gente", "La ficha los muestra con comunicación y comercio."),
            ex(f"{C5} Luis dice: «Los mayas no tenían ninguna red». ¿Qué dato la contradice?", "Tenían caminos entre ciudades", "La ficha lo indica."),
        ],
        "challenge": [
            ex(f"{C5} Marca cada parte: afirmación, evidencia o límite. a) «En extensión, los incas destacan». b) «El Qhapaq Ñan tenía miles de kilómetros». c) «Las fuentes no son equivalentes en cada pueblo».", "a: afirmación; b: evidencia; c: límite", "Cada frase cumple una función distinta."),
            ex(f"{C5} Dos estudiantes: Rosa dice «Los incas fueron los mejores». Tomás dice «Con el criterio de extensión de caminos, los incas destacan, aunque las fuentes no son iguales para todos». ¿Quién argumenta mejor?", "Tomás", "Dice el criterio y el límite."),
        ],
    },
    context=[ex("Un amigo pregunta: «¿Quién mandaba mensajes más rápido?». ¿Qué datos de la ficha usarías, y qué límite reconocerías?", "los chasquis y tambos incas; que no hay datos equivalentes de los otros pueblos", "La ficha trae más datos de velocidad para los incas.")],
    selfcheck=[
        ex("¿Qué se debe aclarar antes de decir «el mejor»?", "el criterio", "Sin criterio no hay comparación."),
        ex("¿Qué civilización destaca por la extensión de sus caminos?", "los incas", "Por el Qhapaq Ñan."),
        ex("¿Qué es un límite en un argumento?", "lo que no podemos afirmar", "Un buen argumento lo reconoce."),
    ],
    open_task=task(
        f"Elige uno de estos criterios: extensión, escritura o comercio. Escribe un argumento de cuatro frases: criterio, civilización que destaca, una evidencia de la ficha y un límite. {C5}",
        "Con el criterio de extensión, los incas destacan. El Qhapaq Ñan tenía miles de kilómetros. Tenían chasquis y tambos. Las fuentes no son iguales para los tres pueblos.",
        ["criterio claro", "civilización que destaca", "una evidencia de la ficha", "un límite"], ["cuatro frases"], ["decir «el mejor» sin criterio", "olvidar el límite"],
        "Pide que cambie el criterio y vea si cambia la conclusión."),
    reinforce="Explica con tus palabras por qué «mejor» depende del criterio.",
    extend="Propón un criterio nuevo para comparar civilizaciones y di qué fuente necesitarías.",
)
