"""Material del estudiante de 4.º básico, Historia, Geografía y Ciencias Sociales: OA 01 (civilización maya) y OA 02 (civilización azteca)."""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


OA1 = "HI04 OA 01"
OA2 = "HI04 OA 02"

# ================================================================ OA 01 · MAYAS
# ---------------------------------------------------------------- clase 1
M1 = ("Ficha maya 1: Los mayas vivieron en el sur de Mesoamérica, una gran región cultural de México y Centroamérica. Hoy su territorio es el sur de México, Guatemala, Belice y partes de Honduras y El Salvador. "
      "La península de Yucatán, una zona plana y cálida, está en el sur de México. Muchas ciudades mayas estaban en la selva tropical. "
      "Su época de mayor esplendor, el período clásico, fue entre los años 250 y 900 d.C. Los mayas no formaban un solo reino: tenían muchas ciudades-estado independientes, "
      "como Tikal, Palenque y Copán. Cada ciudad-estado tenía su propio gobernante y sus nobles.")
register(
    OA1, 1,
    materials="Lápiz y papel. La ficha maya está escrita en cada ejercicio. Un mapa de América de tu casa o de un libro ayuda, pero no es necesario.",
    use="Aprenderé dónde y cuándo vivieron los mayas y cómo se organizaban para gobernar. Sirve para ubicar toda su historia en el mapa y en el tiempo.",
    prior=["Sé leer un mapa y encontrar el norte y el sur.", "Sé que la Antigüedad es un tiempo muy lejano.", "Sé que una línea de tiempo ordena hechos."],
    explain=[
        "Los mayas formaron una de las grandes civilizaciones de América. Una civilización es una sociedad grande y organizada, con ciudades, gobierno, escritura y comercio. Los mayas vivieron en el sur de Mesoamérica, una gran región cultural de México y Centroamérica. Hoy su territorio abarca el sur de México, Guatemala, Belice y partes de Honduras y El Salvador.",
        "Su época de mayor esplendor, llamada período clásico, fue entre los años 250 y 900 d.C. Las letras d.C. significan «después de Cristo» y sirven para contar los años de nuestra era. Muchos edificios mayas se construyeron entonces, en medio de la selva tropical y en la península de Yucatán.",
        "Los mayas no tenían un solo país ni un solo rey para todos. Tenían ciudades-estado: cada ciudad con sus tierras vecinas, su gobernante y sus nobles, como Tikal, Palenque o Copán. A veces las ciudades se aliaban y a veces peleaban entre sí. Compartían la cultura, pero no un único gobierno.",
    ],
    vocab=[("civilización", "sociedad grande y organizada, con ciudades, gobierno y escritura"), ("Mesoamérica", "gran región cultural de México y Centroamérica; los mayas vivieron en su parte sur"), ("ciudad-estado", "ciudad con su propio gobernante que manda sobre sus tierras vecinas"), ("período clásico", "época de mayor esplendor maya, entre 250 y 900 d.C."), ("noble", "persona de una familia importante que ayudaba a gobernar")],
    worked=[
        {"title": "Decir dónde", "problem": f"{M1} ¿Dónde vivieron los mayas?", "steps": ["Busco en la ficha dónde vivieron.", "Leo que vivieron en el sur de Mesoamérica: hoy es el sur de México, Guatemala, Belice y partes de Honduras y El Salvador."], "answer": "En el sur de México y en parte de Centroamérica"},
        {"title": "Calcular una duración", "problem": f"{M1} ¿Cuántos años duró el período clásico?", "steps": ["Busco el inicio y el fin: 250 y 900 d.C.", "Resto: 900 − 250 = 650."], "answer": "650 años"},
    ],
    mistakes=[
        {"wrong": "Decir que los mayas eran un solo imperio con un solo rey.", "why": "Se piensa en un país actual.", "fix": "Recuerda que eran muchas ciudades-estado, cada una con su gobernante."},
        {"wrong": "Ubicar a los mayas en el sur de Sudamérica.", "why": "Se confunde Centroamérica con Sudamérica.", "fix": "Busca México y Centroamérica: los mayas vivieron ahí."},
    ],
    tiers={
        "recovery": [
            ex(f"{M1} ¿Cómo se llama la gran región cultural en cuya parte sur vivieron los mayas?", "Mesoamérica", "La ficha nombra a Mesoamérica como esa región."),
            ex(f"{M1} ¿Una ciudad-estado maya tenía su propio gobernante o dependía de un único rey de todos los mayas?", "tenía su propio gobernante", "Cada ciudad-estado tenía gobernante y nobles propios."),
            arith(f"{M1} El período clásico fue entre 250 y 900 d.C. ¿Cuántos años duró?", "900-250", "Se resta el año final menos el inicial.", " años"),
        ],
        "understand": [
            ex(f"{M1} ¿Cuál de estas es una ciudad-estado maya: Tikal o Machu Picchu?", "Tikal", "La ficha nombra a Tikal entre las ciudades-estado mayas."),
            ex(f"{M1} ¿Qué país actual de esta lista tiene territorio de la región maya: Guatemala o Chile?", "Guatemala", "La ficha incluye a Guatemala en la región maya."),
            ex("Elige la frase correcta. A) Los mayas formaban un solo reino con un solo gobierno. B) Los mayas tenían muchas ciudades-estado independientes.", "B", "Cada ciudad-estado tenía su propio gobernante."),
        ],
        "apply": [
            ex(f"{M1} Un compañero dice que los mayas del período clásico vivían en el año 1500 d.C. ¿Está dentro del período clásico?", "No", "El período clásico terminó en el año 900 d.C. y 1500 es posterior."),
            ex(f"{M1} Quieres marcar en un mapa la península de Yucatán. ¿En qué país actual la buscas?", "México", "La ficha dice que Yucatán está en el sur de México."),
            ex(f"{M1} Si Palenque y Copán tuvieron una disputa, ¿eran dos ciudades-estado distintas o dos barrios de la misma ciudad?", "dos ciudades-estado distintas", "Cada una era independiente y tenía su gobernante."),
        ],
        "reason": [
            ex(f"{M1} Tomás dice: «Tikal y Copán eran barrios de una misma ciudad». Corrige su error con un dato de la ficha.", "Eran ciudades-estado independientes, cada una con su propio gobernante", "La ficha dice que no eran un solo reino."),
            ex(f"{M1} Ana dice: «Los mayas vivían en un desierto de Sudamérica». ¿Qué dos datos de la ficha la contradicen?", "Vivían en el sur de México y Centroamérica, y en la selva tropical", "La ficha ubica a los mayas en México y Centroamérica, con selva."),
        ],
        "challenge": [
            ex(f"{M1} Clasifica cada dato en «dónde», «cuándo» o «cómo se gobernaban»: a) entre 250 y 900 d.C.; b) selva tropical y Yucatán; c) cada ciudad con su gobernante.", "a: cuándo; b: dónde; c: cómo se gobernaban", "a es tiempo, b es lugar y c es organización política."),
            ex(f"{M1} Mapa A pone a los mayas en el sur de Sudamérica. Mapa B los pone en el sur de México y en Centroamérica. ¿Cuál concuerda con la ficha?", "el mapa B", "La ficha ubica a los mayas en el sur de México y en Centroamérica."),
        ],
    },
    context=[ex("Un cartel de museo dice: «Estela de Copán, período clásico». ¿Qué parte del cartel indica la ciudad y cuál la época?", "Ciudad: Copán. Época: período clásico", "Copán es una ciudad-estado y el período clásico es el tiempo.")],
    selfcheck=[
        ex("¿Dónde vivieron los mayas?", "en el sur de México y en Centroamérica", "Allí se ubica el territorio maya."),
        ex("¿Qué es una ciudad-estado maya?", "una ciudad con su propio gobernante que mandaba sobre sus tierras vecinas", "Cada ciudad se gobernaba por separado."),
        ex(f"{M1} ¿Entre qué años fue el período clásico maya?", "entre 250 y 900 d.C.", "Así lo indica la ficha."),
    ],
    open_task=task(
        f"Haz dos dibujos. Primero, una línea de tiempo con tres puntos: «250 d.C.», «900 d.C.» y «hoy». Pinta de color el tramo entre 250 y 900 d.C. y escribe «período clásico». Segundo, un mapa simple: dibuja un rectángulo para América, marca el sur de México y Centroamérica con una mancha y escribe «mayas». Dibuja tres puntos dentro de la mancha y ponles los nombres Tikal, Palenque y Copán. {M1}",
        "Línea con 250, 900 y hoy, y el tramo clásico pintado. Mapa con mancha en México y Centroamérica y tres ciudades marcadas.",
        ["orden correcto de los años", "región maya en el sur de México y Centroamérica", "tres ciudades-estado nombradas"], ["línea de tiempo dibujada", "mapa simple dibujado"], ["ubicar a los mayas en Sudamérica", "dibujar una sola ciudad como capital de todos"],
        "Pide que explique en voz alta por qué dibujó tres ciudades y no una. Si dice «porque eran independientes», vas bien."),
    reinforce="Repite en voz alta: dónde vivieron los mayas, cuándo fue su período clásico y qué es una ciudad-estado.",
    extend="Escribe dos diferencias entre una ciudad-estado maya y un país como Chile hoy.",
)

# ---------------------------------------------------------------- clase 2
M2 = ("Fuentes sobre los mayas: (1) Una estela, que es una piedra grande tallada, hecha por una ciudad maya hace más de mil años. Muestra a un gobernante con signos jeroglíficos que cuentan sus triunfos. "
      "(2) Un códice, que es un libro maya doblado como acordeón, de papel de corteza, con signos y dibujos de calendarios y astros. Se conservan muy pocos. "
      "(3) Las ruinas de una pirámide escalonada con un templo en la cima. "
      "(4) Un texto escrito en el siglo XVI por un religioso español, que cuenta cómo vivían los mayas que él conoció.")
register(
    OA1, 2,
    materials="Lápiz y papel. Las fuentes están escritas en cada ejercicio.",
    use="Aprenderé a preguntar quién hizo una fuente, cuándo y para qué. Sirve para saber cuánto podemos creerle y qué nos dice de los mayas.",
    prior=["Sé que una fuente entrega información sobre el pasado.", "Sé dónde y cuándo vivieron los mayas."],
    explain=[
        "Los historiadores conocen a los mayas por medio de fuentes: estelas, códices, ruinas, objetos y textos de otras épocas. Cada fuente es una pista. Para usarla bien, se pregunta por su procedencia: quién la hizo, cuándo la hizo y para qué la hizo.",
        "Una estela la hizo la propia ciudad maya. Muestra al gobernante con orgullo y sus triunfos, no la vida de todos los habitantes. Un códice también lo hicieron mayas, y sirve para conocer el calendario y los astros. Los jeroglíficos son la escritura maya: signos que se tallaban en piedra o se pintaban en códices. Unas ruinas, como una pirámide escalonada con un templo en la cima, muestran cómo construían los mayas, pero no hablan por sí solas.",
        "Un texto escrito por un español del siglo XVI es otra clase de fuente. Su autor vivió mucho después del período clásico y miró a los mayas desde sus propias ideas. Por eso debemos leerlo con cuidado, comparándolo con fuentes hechas por los mayas. Lo que una fuente no dice, no debemos inventarlo.",
    ],
    vocab=[("estela", "piedra grande tallada con imágenes y signos"), ("códice", "libro antiguo doblado como acordeón"), ("jeroglífico", "signo de la escritura maya que representa una palabra o un sonido"), ("procedencia", "quién hizo la fuente, cuándo y para qué"), ("ruinas", "restos de un edificio muy antiguo")],
    worked=[
        {"title": "Preguntar por la procedencia", "problem": f"{M2} ¿Quién hizo la fuente 1 y para qué?", "steps": ["Leo que la hizo una ciudad maya hace más de mil años.", "Muestra al gobernante y sus triunfos: sirve para honrarlo."], "answer": "La hizo una ciudad maya para mostrar al gobernante y sus triunfos"},
        {"title": "Reconocer un límite", "problem": f"{M2} ¿La fuente 3 nos dice qué comían los mayas?", "steps": ["La fuente 3 son ruinas de una pirámide con un templo.", "Muestra un edificio, no la comida."], "answer": "No, solo muestra cómo era un edificio"},
    ],
    mistakes=[
        {"wrong": "Creer que una fuente cuenta toda la historia.", "why": "Se piensa que una pista basta.", "fix": "Usa varias fuentes y di solo lo que cada una muestra."},
        {"wrong": "Creer todo lo que dice un texto solo porque es antiguo.", "why": "Se olvida preguntar quién lo escribió.", "fix": "Pregunta quién lo hizo, cuándo y para qué."},
    ],
    tiers={
        "recovery": [
            ex(f"{M2} ¿De qué material era el papel del códice?", "de corteza", "La ficha dice que era papel de corteza."),
            ex(f"{M2} ¿Quién hizo la estela: una ciudad maya o un religioso español?", "una ciudad maya", "La fuente 1 la hizo una ciudad maya."),
            ex(f"{M2} ¿Qué fuente es un texto escrito por alguien que no era maya?", "la fuente 4", "El religioso español escribió esa fuente."),
        ],
        "understand": [
            ex(f"{M2} ¿Qué cuenta con orgullo la estela de la fuente 1?", "los triunfos del gobernante", "La estela muestra al gobernante y sus triunfos."),
            ex(f"{M2} ¿Qué fuente sirve para saber cómo era un edificio maya?", "la fuente 3", "Las ruinas muestran la pirámide y el templo."),
            ex(f"{M2} ¿Cómo escribían los mayas en la estela de la fuente 1: con jeroglíficos o con letras como las nuestras?", "con jeroglíficos", "La ficha dice que la estela tiene signos jeroglíficos que cuentan sus triunfos."),
        ],
        "apply": [
            ex(f"{M2} Quieres saber cómo se anotaban los calendarios y los astros. ¿Qué fuente usas?", "la fuente 2", "El códice tiene dibujos de calendarios y astros."),
            ex(f"{M2} En la cima de la pirámide escalonada de la fuente 3 había un edificio. ¿Qué era?", "un templo", "La ficha dice que la pirámide tenía un templo en la cima."),
            ex(f"{M2} Une cada fuente con su procedencia: A) fuente 1; B) fuente 4. 1) escrita por un religioso español; 2) tallada por una ciudad maya.", "A con 2; B con 1", "La estela es maya y el texto del siglo XVI es español."),
        ],
        "reason": [
            ex(f"{M2} Pedro dice: «El texto del religioso lo dice todo con exactitud, porque él lo vio». ¿Se puede afirmar eso?", "No, él era de otra cultura, vivió mucho después y pudo equivocarse o juzgar con sus ideas", "Hay que revisar la procedencia y compararla con fuentes mayas."),
            ex(f"{M2} Clara afirma: «La estela prueba que los campesinos mayas eran felices». ¿Qué problema tiene su afirmación?", "La estela muestra al gobernante y sus triunfos, no la vida de los campesinos", "Una fuente no sirve para afirmar lo que no muestra."),
        ],
        "challenge": [
            ex(f"{M2} Para comparar la versión maya con la versión de un extranjero, ¿qué dos fuentes enfrentarías?", "la fuente 1 con la 4, o la 2 con la 4", "Una es hecha por mayas y la otra por un español."),
            ex(f"{M2} Elige la pregunta que las cuatro fuentes no pueden responder. A) ¿Qué mostraba una estela? B) ¿Cuál era el nombre de un campesino de Tikal?", "B", "Ninguna fuente de la ficha entrega nombres de campesinos."),
        ],
    },
    context=[ex("En un museo ves una estela y un cartel que dice: «Hecha por la ciudad de Copán para honrar a su gobernante». ¿Qué datos de procedencia entrega el cartel?", "Quién la hizo (la ciudad de Copán) y para qué (honrar a su gobernante)", "Responde quién y para qué, parte de la procedencia.")],
    selfcheck=[
        ex("¿Qué tres preguntas forman la procedencia de una fuente?", "quién la hizo, cuándo y para qué", "Con ellas se evalúa cuánto aporta la fuente."),
        ex(f"{M2} ¿Qué es un códice maya?", "un libro maya doblado como acordeón, de papel de corteza", "Así lo describe la ficha."),
        ex("Al usar una fuente, ¿se debe decir solo lo que ella muestra o también todo lo que yo imagine?", "solo lo que ella muestra", "Lo demás es una suposición sin respaldo."),
    ],
    open_task=task(
        f"Toma las fuentes 1 y 4 de esta ficha. {M2} Haz una tabla de tres columnas con los títulos «quién la hizo», «cuándo» y «para qué», y completa una fila para cada fuente. Después escribe una cosa que cada fuente no puede decirnos.",
        "Fuente 1: la hizo una ciudad maya; hace más de mil años; para honrar al gobernante; no dice cómo vivían los campesinos. Fuente 4: la escribió un religioso español; siglo XVI; para contar lo que vio; no dice lo que pensaban los mayas.",
        ["dos filas completas", "usa los datos de la ficha", "indica un límite de cada fuente"], ["tabla con dos filas", "dos límites escritos"], ["decir que una fuente lo explica todo", "confundir quién hizo cada fuente"],
        "Pregunta cuál de las dos fuentes le parece más cercana a la voz de los mayas y por qué."),
    reinforce="Nombra cuatro tipos de fuente sobre los mayas y di quién hizo cada una.",
    extend="Imagina que dentro de mil años estudian tu sala de clases. Escribe tres objetos que serían fuentes y qué dirían.",
)

# ---------------------------------------------------------------- clase 3
M3 = ("Ficha maya 3: Los campesinos mayas cultivaban maíz, frijol, zapallo y chile en la milpa, un terreno donde se siembran varias plantas juntas. "
      "El maíz era el alimento principal; se molía para hacer tortillas. También se tomaba una bebida de cacao muy apreciada. "
      "La sociedad tenía grupos: el gobernante y los nobles; los sacerdotes y escribas; los comerciantes y artesanos; y los campesinos, que eran la mayoría. "
      "Los hombres trabajaban el campo, cazaban y combatían. Las mujeres molían el maíz, tejían telas y criaban a los hijos. Algunas mujeres nobles llegaron a gobernar ciudades.")
register(
    OA1, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé qué comían los mayas, cómo se organizaba su sociedad y qué hacían hombres y mujeres. Sirve para describir su vida cotidiana con evidencia.",
    prior=["Sé dónde vivieron los mayas.", "Sé que una ciudad-estado tenía gobernante y nobles."],
    explain=[
        "Los mayas eran sobre todo agricultores. En la milpa sembraban varias plantas juntas: maíz, frijol, zapallo y chile. El maíz era el alimento principal y se molía para hacer tortillas. También bebían cacao, una bebida hecha con las semillas del árbol del cacao.",
        "La sociedad maya estaba ordenada en grupos. Arriba estaban el gobernante y los nobles. Luego venían los sacerdotes y los escribas, que anotaban hechos con jeroglíficos. Después, los comerciantes y artesanos. Los campesinos eran la mayoría y alimentaban a toda la ciudad con su trabajo.",
        "Hombres y mujeres tenían tareas distintas. Los hombres trabajaban el campo, cazaban y combatían. Las mujeres molían el maíz, tejían telas y criaban a los hijos. Pero hubo excepciones: algunas mujeres de familias nobles gobernaron ciudades. Por eso no basta decir que «las mujeres solo hacían tareas de la casa».",
    ],
    vocab=[("milpa", "terreno donde se siembran varias plantas juntas, como maíz y frijol"), ("escriba", "persona que escribía con jeroglíficos"), ("artesano", "persona que hace objetos con sus manos, como vasijas o telas"), ("cacao", "árbol cuyas semillas sirven para hacer una bebida"), ("oficio", "trabajo que una persona sabe hacer")],
    worked=[
        {"title": "Reconocer un alimento", "problem": f"{M3} ¿Cuál era el alimento principal de los mayas?", "steps": ["Busco la palabra «principal» en la ficha.", "Dice que el maíz era el alimento principal."], "answer": "El maíz"},
        {"title": "Clasificar un oficio", "problem": f"{M3} Una persona anotaba los hechos del gobernante con jeroglíficos. ¿A qué grupo pertenecía?", "steps": ["Busco quién escribía: los escribas.", "Los escribas estaban con los sacerdotes."], "answer": "A los sacerdotes y escribas"},
    ],
    mistakes=[
        {"wrong": "Decir que solo los nobles tenían trabajos importantes.", "why": "No se piensa en el trabajo de los campesinos.", "fix": "Recuerda que los campesinos eran la mayoría y alimentaban a la ciudad."},
        {"wrong": "Decir que las mujeres mayas nunca gobernaron.", "why": "Se generaliza más de lo que dice la fuente.", "fix": "Lee la ficha: algunas mujeres nobles gobernaron ciudades."},
    ],
    tiers={
        "recovery": [
            ex(f"{M3} ¿Qué es la milpa?", "un terreno donde se siembran varias plantas juntas", "La ficha define la milpa de ese modo."),
            ex(f"{M3} ¿Cuál era el alimento principal de los mayas?", "el maíz", "La ficha dice que el maíz era el principal."),
            ex(f"{M3} ¿Qué grupo de la sociedad era la mayoría?", "los campesinos", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{M3} ¿Qué hacían las mujeres con el maíz?", "lo molían", "Molían el maíz para hacer tortillas."),
            ex(f"{M3} ¿Quiénes gobernaban las ciudades-estado, según los grupos de la ficha?", "el gobernante y los nobles", "Estaban en la cima de la sociedad."),
            ex(f"{M3} ¿Cuál de estas plantas NO era un cultivo maya de la ficha: frijol, chile o trigo?", "trigo", "La ficha no nombra el trigo."),
        ],
        "apply": [
            ex(f"{M3} Una persona sembraba maíz y frijol en la milpa. ¿A qué grupo pertenecía?", "a los campesinos", "Los campesinos cultivaban esas plantas."),
            ex(f"{M3} Un menú tiene tortillas de maíz, frijoles y zapallo. ¿Todos esos alimentos vienen de cultivos de la ficha?", "Sí", "El maíz, el frijol y el zapallo se nombran en la ficha."),
            ex(f"{M3} Une cada persona con su grupo: A) un comerciante; B) un sacerdote; C) una persona que cultiva maíz. 1) sacerdotes y escribas; 2) campesinos; 3) comerciantes y artesanos.", "A con 3; B con 1; C con 2", "Cada uno se ubica según los grupos que da la ficha."),
        ],
        "reason": [
            ex(f"{M3} Ana dice: «Las mujeres mayas nunca ocuparon cargos importantes». ¿Qué dato de la ficha la contradice?", "Algunas mujeres nobles llegaron a gobernar ciudades", "La ficha menciona mujeres gobernantes."),
            ex(f"{M3} Luis dice: «Los campesinos eran pocos porque la ficha nombra primero al gobernante». ¿Tiene razón?", "No, los campesinos eran la mayoría", "El orden en que se nombran los grupos no cambia cuántos eran."),
        ],
        "challenge": [
            ex(f"{M3} Clasifica cada dato en «economía», «organización de la sociedad» o «roles de hombres y mujeres»: a) cultivar la milpa; b) nobles, sacerdotes y campesinos; c) las mujeres tejían telas.", "a: economía; b: organización de la sociedad; c: roles de hombres y mujeres", "Cada dato responde a una dimensión distinta de la vida maya."),
            ex(f"{M3} ¿Qué dimensión de la vida maya NO aparece en la ficha: la religión o la alimentación?", "la religión", "La ficha trata de alimentación, sociedad y roles, no de religión."),
        ],
    },
    context=[ex("Un museo muestra una vasija para beber cacao y un cartel que dice «de una familia noble». ¿Qué dato de la ficha apoya que el cacao era una bebida apreciada?", "También se tomaba una bebida de cacao muy apreciada", "La ficha dice que era apreciada, aunque no dice quiénes la tomaban.")],
    selfcheck=[
        ex("¿Qué plantas se sembraban juntas en la milpa maya?", "maíz, frijol, zapallo y chile", "Son los cultivos que nombra la ficha."),
        ex("¿Qué hacía un escriba maya?", "anotaba hechos con jeroglíficos", "Era el encargado de escribir."),
        ex("¿Qué mujeres llegaron a gobernar ciudades mayas?", "algunas mujeres nobles", "La ficha indica que hubo mujeres gobernantes de familias nobles."),
    ],
    open_task=task(
        f"Dibuja una pirámide de cuatro pisos para mostrar la sociedad maya. Escribe los grupos en este orden, de arriba hacia abajo: gobernante y nobles; sacerdotes y escribas; comerciantes y artesanos; campesinos. Luego, al lado, haz una lista de tres alimentos mayas. {M3}",
        "Pirámide con cuatro pisos nombrados y una lista con maíz, frijol y cacao.",
        ["cuatro grupos en orden", "tres alimentos de la ficha"], ["pirámide dibujada", "lista de alimentos"], ["poner a los campesinos arriba", "incluir alimentos que no están en la ficha"],
        "Pregunta por qué los campesinos son el piso más ancho. La idea esperada es que eran la mayoría."),
    reinforce="Cuenta en voz alta qué comían los mayas y quién hacía cada trabajo.",
    extend="Escribe qué grupo maya te gustaría ser y qué haría tu día, usando solo datos de la ficha.",
)

# ---------------------------------------------------------------- clase 4
M4 = ("Ficha maya 4: Los mayas adoraban a muchos dioses, como los de la lluvia, el maíz y el Sol. Hacían ceremonias en templos y plazas, con ofrendas de alimentos e incienso. "
      "En algunos ritos importantes hubo sacrificios humanos, a menudo de prisioneros de guerra. Las ciudades-estado a veces guerreaban entre sí para capturar prisioneros y ganar poder. "
      "Los sacerdotes observaban el Sol, la Luna y Venus, y llevaron un calendario muy preciso. Para contar usaban puntos, barras y una concha: un punto vale 1, una barra vale 5 y la concha vale 0. "
      "Dos fuentes: la estela de un gobernante cuenta con orgullo que capturó prisioneros. Un religioso español del siglo XVI escribió que esos ritos eran crueles.")
register(
    OA1, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio. Puedes usar palitos o porotos para representar puntos y barras.",
    use="Aprenderé sobre la religión, la guerra, la astronomía y la matemática de los mayas, y cómo distintas fuentes los miran con perspectivas diferentes.",
    prior=["Sé que cada fuente tiene una procedencia.", "Sé que las ciudades-estado eran independientes."],
    explain=[
        "Los mayas creían en muchos dioses de la naturaleza: la lluvia, el maíz, el Sol. Para pedirles ayuda hacían ceremonias con ofrendas. En algunos ritos importantes hubo sacrificios humanos, en general de prisioneros de guerra. Es un tema delicado: debemos describirlo con respeto y sin exagerar.",
        "Los mayas también fueron grandes observadores del cielo. Los sacerdotes seguían el Sol, la Luna y Venus y armaron un calendario muy preciso. Para contar usaban tres signos: un punto vale 1, una barra vale 5 y una concha vale 0. Así, dos barras y tres puntos escriben 13, porque 5 + 5 + 3 = 13.",
        "Una perspectiva es el punto de vista de quien cuenta algo. La estela del gobernante cuenta con orgullo que capturó prisioneros. El religioso español, en cambio, los llama crueles. Las dos fuentes hablan del mismo tipo de hecho, pero con perspectivas distintas. Para comprender bien, comparamos ambas y no nos quedamos con una sola.",
    ],
    vocab=[("perspectiva", "punto de vista desde el que alguien cuenta algo"), ("ofrenda", "regalo que se entrega a los dioses"), ("sacrificio", "ofrenda ritual en que se entrega una vida"), ("calendario", "sistema para contar los días y los años"), ("astronomía", "estudio de los astros, como el Sol y la Luna")],
    worked=[
        {"title": "Leer un número maya", "problem": "Un número maya tiene dos barras y tres puntos. ¿Qué número es? (un punto vale 1 y una barra vale 5)", "steps": ["Dos barras valen 5 + 5 = 10.", "Tres puntos valen 3. Sumo 10 + 3."], "answer": "13"},
        {"title": "Distinguir perspectivas", "problem": f"{M4} ¿Cómo miran el mismo tipo de hecho el gobernante de la estela y el religioso español?", "steps": ["El gobernante cuenta con orgullo que capturó prisioneros.", "El religioso dice que esos ritos eran crueles."], "answer": "El gobernante lo mira con orgullo y el religioso con condena"},
    ],
    mistakes=[
        {"wrong": "Pensar que todos los mayas participaban de sacrificios humanos todo el tiempo.", "why": "Se exagera un dato sin leerlo bien.", "fix": "Recuerda: fueron en algunos ritos importantes, a menudo con prisioneros de guerra."},
        {"wrong": "Leer una barra como 1 y un punto como 5.", "why": "Se cambian los valores.", "fix": "Un punto vale 1, una barra vale 5 y la concha vale 0."},
    ],
    tiers={
        "recovery": [
            ex(f"{M4} ¿Cuánto vale la concha en la numeración maya?", "0", "La ficha dice que la concha vale 0."),
            ex(f"{M4} ¿Qué astro, además del Sol y la Luna, observaban los sacerdotes?", "Venus", "La ficha nombra a Venus."),
            ex(f"{M4} ¿Para qué guerreaban a veces las ciudades-estado?", "para capturar prisioneros y ganar poder", "La ficha da esos dos motivos."),
        ],
        "understand": [
            ex(f"{M4} ¿A quiénes se ofrecían las ceremonias y ofrendas mayas?", "a sus dioses", "Los mayas adoraban a muchos dioses."),
            ex(f"{M4} ¿Qué es una perspectiva?", "el punto de vista desde el que alguien cuenta algo", "Quien cuenta algo lo hace desde su mirada."),
            ex(f"{M4} ¿Quién escribió que los ritos eran crueles: el gobernante de la estela o el religioso español?", "el religioso español", "El gobernante contaba su triunfo con orgullo."),
        ],
        "apply": [
            arith(f"{M4} Un número maya tiene dos barras y un punto. Un punto vale 1 y una barra vale 5. ¿Qué número es?", "5*2+1", "Se suman dos barras y un punto.", ""),
            arith(f"{M4} Un número maya tiene una barra y cuatro puntos. ¿Qué número es?", "5+4", "Una barra vale 5 y cuatro puntos valen 4.", ""),
            arith(f"{M4} Un número maya tiene tres barras. ¿Qué número es?", "5*3", "Tres barras valen 5 + 5 + 5.", ""),
        ],
        "reason": [
            ex(f"{M4} Sofía dice: «Los mayas hacían sacrificios humanos todos los días». ¿Qué dice realmente la ficha?", "Que en algunos ritos importantes hubo sacrificios, a menudo de prisioneros de guerra", "La ficha no dice que fueran diarios ni generales."),
            ex(f"{M4} Pedro dice que la estela y el religioso cuentan lo mismo con las mismas palabras. ¿Es cierto?", "No, la estela lo cuenta con orgullo y el religioso lo juzga cruel", "Tienen perspectivas distintas."),
        ],
        "challenge": [
            arith(f"{M4} Suma estos dos números mayas: uno con una barra y dos puntos, y otro con dos barras. ¿Cuánto suman?", "5+2+5*2", "Primero 7 y luego 10, y se suman.", ""),
            ex(f"{M4} Para entender mejor los ritos mayas, ¿conviene leer solo la estela, solo al religioso o ambos?", "ambos", "Dos perspectivas se completan y muestran los límites de cada una."),
        ],
    },
    context=[ex("Un amigo dice: «El religioso español no fue justo con los mayas». Para saberlo mejor, ¿qué debe hacer?", "Leer también fuentes hechas por los mayas y comparar", "Comparar perspectivas permite juzgar con más evidencia.")],
    selfcheck=[
        ex("¿Qué valen un punto, una barra y la concha en la numeración maya?", "un punto vale 1, una barra vale 5 y la concha vale 0", "Son los valores de los tres signos."),
        ex("¿Qué observaban los sacerdotes mayas en el cielo?", "el Sol, la Luna y Venus", "Con eso armaron su calendario."),
        ex("¿Por qué dos fuentes pueden contar de forma distinta el mismo tipo de hecho?", "porque tienen perspectivas distintas", "Cada autor lo mira desde su punto de vista."),
    ],
    open_task=task(
        f"Dibuja en un papel los números 17 y 12 con la numeración maya, usando puntos y barras. Debajo de cada dibujo escribe la suma que lo comprueba, por ejemplo 5 + 5 + 1 = 11. Después escribe una frase que explique qué vale la concha. {M4}",
        "17 = tres barras y dos puntos (5 + 5 + 5 + 2). 12 = dos barras y dos puntos (5 + 5 + 2). La concha vale 0.",
        ["17 con tres barras y dos puntos", "12 con dos barras y dos puntos", "suma escrita bajo cada dibujo"], ["dibujo de los números"], ["usar un punto para valer 5", "olvidar que la concha vale 0"],
        "Pide que sume en voz alta sus barras y sus puntos para comprobar el resultado."),
    reinforce="Escribe tres números mayas con puntos y barras y lee cuánto valen.",
    extend="Escribe dos preguntas que harías para comparar la estela y el texto del religioso.",
)
