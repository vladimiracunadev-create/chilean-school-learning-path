"""Material del estudiante de 2.º básico, Historia, Geografía y Ciencias Sociales: OA 01 (modos de vida de pueblos originarios precolombinos)."""
from __future__ import annotations

from student_lessons import ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


OA = "HI02 OA 01"

FICHA = ("Ficha de pueblos (los lugares son aproximados): aimara, norte, altiplano y valles; chango, costa del norte, junto al mar; "
         "mapuche, centro y sur, bosques, ríos y tierras de cultivo; selk'nam, extremo sur, Tierra del Fuego, llanuras y bosques fríos con guanacos; "
         "rapa nui, Rapa Nui o Isla de Pascua, una isla del océano Pacífico, lejos de la costa del continente.")

# ---------------------------------------------------------------- clase 1
register(
    OA, 1,
    materials="Lápiz y papel. La ficha de los pueblos está escrita en cada ejercicio. Un mapa de Chile de tu casa o de un libro sirve, pero no es necesario.",
    use="Aprenderé que antes de la llegada de los españoles vivieron en Chile pueblos distintos, en lugares distintos. Sirve para no pensar que todos vivían igual.",
    prior=["Sé que Chile es largo y angosto.", "Sé que hay norte, centro y sur."],
    explain=[
        "Hace mucho tiempo, antes de que llegaran los españoles, ya vivían personas en el territorio de lo que hoy es Chile. Ese tiempo se llama periodo precolombino. No eran un solo pueblo: eran muchos pueblos, y cada uno tenía su propio modo de vida.",
        "Un pueblo es un grupo de personas con una historia, un idioma y costumbres compartidas. Los aimara vivían en el norte, en el altiplano y los valles. Los changos vivían en la costa del norte. Los mapuche vivían en el centro y el sur. Los selk'nam vivían en Tierra del Fuego, en el extremo sur. Los rapa nui vivían en una isla del océano Pacífico, llamada Rapa Nui o Isla de Pascua.",
        "El lugar donde vive un pueblo se llama territorio. Cada territorio tenía un paisaje y recursos distintos: mar, desierto, bosque, ríos o llanuras. Por eso cada pueblo comía, trabajaba y construía de forma diferente. Los pueblos no vivían entre las fronteras de hoy, y por eso los lugares son aproximados.",
    ],
    vocab=[("pueblo", "grupo de personas con historia, idioma y costumbres compartidas"), ("precolombino", "tiempo de antes de la llegada de los europeos"), ("territorio", "lugar donde vive un pueblo"), ("recurso", "algo de la naturaleza que las personas usan para vivir"), ("aproximado", "casi exacto, pero no perfecto")],
    worked=[
        {"title": "Ubicar un pueblo", "problem": f"{FICHA} ¿En qué zona de Chile vivían los changos?", "steps": ["Busco chango en la ficha.", "La ficha dice: costa del norte, junto al mar."], "answer": "En la costa del norte"},
        {"title": "Relacionar paisaje y pueblo", "problem": f"{FICHA} Un pueblo vivía en un lugar frío con guanacos. ¿Cuál era?", "steps": ["Busco la pista guanacos y frío.", "Esa pista aparece en selk'nam, extremo sur."], "answer": "Los selk'nam"},
    ],
    mistakes=[
        {"wrong": "Decir que todos los pueblos originarios vivían igual.", "why": "Se piensa que hubo un solo pueblo.", "fix": "Mira la ficha: cada pueblo tenía su territorio, su paisaje y sus costumbres."},
        {"wrong": "Decir que los pueblos originarios solo existieron en el pasado.", "why": "Se olvida que hay personas de esos pueblos hoy.", "fix": "Escribe «vivían» para el pasado, y recuerda que hoy hay personas de esos pueblos."},
    ],
    tiers={
        "recovery": [
            ex(f"{FICHA} ¿En qué parte del país vivían los mapuche?", "en el centro y el sur", "La ficha ubica a los mapuche en el centro y sur."),
            ex(f"{FICHA} ¿Qué pueblo vivía junto al mar, en la costa del norte?", "los changos", "La costa del norte es el territorio de los changos."),
            ex("La palabra precolombino habla de un tiempo. ¿Es antes o después de la llegada de los europeos?", "antes", "Precolombino es el tiempo anterior a esa llegada."),
        ],
        "understand": [
            ex(f"{FICHA} ¿Qué pueblo vivía en el altiplano?", "los aimara", "El altiplano está en el territorio aimara."),
            ex("Explica con tus palabras qué es un territorio.", "El lugar donde vive un pueblo", "Territorio es el lugar donde un pueblo vive y consigue sus recursos."),
            ex("Escribe una razón por la cual los pueblos no vivían igual. Elige: A) tenían paisajes distintos, B) todos vivían en el mismo lugar.", "A", "Cada pueblo tenía un paisaje y recursos distintos."),
        ],
        "apply": [
            ex(f"{FICHA} Un pueblo vivía entre bosques, ríos y tierras de cultivo. ¿Cuál era?", "los mapuche", "Bosques, ríos y cultivo son pistas del territorio mapuche."),
            ex(f"{FICHA} Ordena de más al norte a más al sur: selk'nam, aimara, mapuche.", "aimara, mapuche, selk'nam", "El aimara está en el norte, el mapuche en el centro-sur y el selk'nam en el extremo sur."),
            ex(f"{FICHA} ¿Qué pueblo vivía en una isla del océano Pacífico?", "los rapa nui", "La ficha ubica a los rapa nui en la isla Rapa Nui."),
        ],
        "reason": [
            ex("Tomás dice: «Todos los pueblos originarios comían exactamente lo mismo». Usa la ficha: ¿tiene razón?", "No; vivían en paisajes distintos y tenían recursos distintos", "Mar, desierto, bosque y llanura dan alimentos diferentes."),
            ex("Una profesora dice: «Los pueblos originarios vivían en el territorio de Chile, pero con otras fronteras». ¿Es una afirmación correcta o incorrecta?", "correcta", "Las fronteras actuales se fijaron después; por eso los lugares son aproximados."),
        ],
        "challenge": [
            ex(f"{FICHA} Mateo escribió: «Los selk'nam vivían en la costa del norte». Corrige su error.", "Los selk'nam vivían en el extremo sur, en Tierra del Fuego", "La ficha ubica a los selk'nam en el extremo sur."),
            ex(f"{FICHA} Dos pueblos del continente vivían en la zona norte. Escríbelos.", "aimara y chango", "Los aimara y los changos aparecen en el norte."),
        ],
    },
    context=[ex("Camila hace un cartel para su curso con el título «Los pueblos de Chile antes de los españoles». Quiere poner la palabra que habla de ese tiempo. ¿Qué palabra de la clase debe usar?", "precolombino", "Esa palabra nombra el tiempo anterior a la llegada de los europeos.")],
    selfcheck=[
        ex(f"{FICHA} ¿Dónde vivían los aimara?", "en el norte, en el altiplano y los valles", "Así lo dice la ficha."),
        ex("¿Cómo se llama el lugar donde vive un pueblo?", "territorio", "Territorio es el lugar que habita un pueblo."),
        ex("¿Los pueblos precolombinos eran uno solo o muchos?", "muchos", "Cada pueblo tenía su territorio y su modo de vida."),
    ],
    open_task=task(
        f"Dibuja un mapa muy simple de Chile como una franja larga. Marca con un punto cada uno de los cinco pueblos de esta ficha y escribe su nombre. {FICHA} Escribe debajo de cada nombre una palabra del paisaje en que vivía.",
        "Franja larga. Arriba, aimara con la palabra altiplano. Arriba junto al borde izquierdo, chango con la palabra mar. En el medio y abajo, mapuche con la palabra bosque. Abajo del todo, selk'nam con la palabra guanaco. Aparte, en el mar a la izquierda de la franja, rapa nui con la palabra isla.",
        ["cinco pueblos ubicados", "rapa nui como isla en el mar", "una palabra de paisaje por pueblo"], ["mapa dibujado", "nombres escritos"], ["poner a los selk'nam en el norte", "poner a los rapa nui en el continente"],
        "Pide que diga en voz alta qué pueblo está más al norte y cuál está más al sur. Recuerda que los lugares son aproximados."),
    reinforce="Repite en voz alta los cinco pueblos y la zona donde vivían, mirando la ficha.",
    extend="Escribe una razón por la cual un pueblo de la costa y uno del bosque no tendrían las mismas herramientas.",
)

# ---------------------------------------------------------------- clase 2
NOM = ("Ficha de movilidad: los selk'nam cazaban guanacos y se trasladaban para seguirlos. Los changos se desplazaban por la costa en busca de peces y mariscos. "
       "Los aimara vivían en aldeas y cultivaban en terrazas. Los mapuche vivían en casas fijas llamadas ruka y cultivaban la tierra. "
       "Los rapa nui vivían en casas fijas en su isla, cultivaban camote y pescaban.")
register(
    OA, 2,
    materials="Lápiz y papel. La ficha de movilidad está escrita en cada ejercicio.",
    use="Aprenderé la diferencia entre vida nómada y vida sedentaria. Sirve para entender por qué algunos pueblos se movían y otros se quedaban, sin decir que uno era mejor.",
    prior=["Sé qué es un territorio.", "Sé que los pueblos vivían en paisajes distintos."],
    explain=[
        "Un pueblo nómada se traslada de un lugar a otro durante el año. Se mueve para encontrar alimentos, como animales para cazar, peces o frutos. Un pueblo sedentario vive casi siempre en el mismo lugar, en aldeas o casas fijas, y suele cultivar la tierra.",
        "Los selk'nam y los changos se movían por sus territorios para encontrar alimento. Los aimara, los mapuche y los rapa nui tenían aldeas o casas fijas y cultivos, y por eso vivían más tiempo en un mismo lugar. Algunos pueblos también se movían por temporadas, así que no siempre es una u otra de forma exacta.",
        "Ninguna forma de vida es mejor que la otra. Cada una era una buena respuesta al paisaje. Donde hay animales que se desplazan, moverse tiene sentido. Donde la tierra se puede cultivar, tiene sentido quedarse y cuidar las plantas.",
    ],
    vocab=[("nómada", "que se traslada de un lugar a otro"), ("sedentario", "que vive casi siempre en un mismo lugar"), ("aldea", "grupo de casas con un lugar de vida en común"), ("cultivar", "sembrar y cuidar plantas para comerlas"), ("temporada", "parte del año")],
    worked=[
        {"title": "Clasificar un pueblo", "problem": f"{NOM} ¿Los selk'nam eran nómadas o sedentarios?", "steps": ["Leo la ficha sobre los selk'nam.", "Cazaban guanacos y se trasladaban para seguirlos.", "Quien se traslada es nómada."], "answer": "Nómadas"},
        {"title": "Buscar la pista", "problem": f"{NOM} ¿Qué pista de la ficha muestra que los mapuche eran sedentarios?", "steps": ["Busco una pista de vivir en un lugar fijo.", "La ficha dice que tenían casas fijas llamadas ruka y que cultivaban la tierra."], "answer": "Tenían casas fijas y cultivaban"},
    ],
    mistakes=[
        {"wrong": "Decir que los nómadas eran menos avanzados que los sedentarios.", "why": "Se piensa que quedarse en un lugar es mejor.", "fix": "Cada forma de vida respondía al paisaje. Ninguna es mejor que la otra."},
        {"wrong": "Pensar que un pueblo sedentario nunca se movía.", "why": "Se toma la palabra de forma demasiado rígida.", "fix": "Los sedentarios vivían casi siempre en un lugar, pero podían moverse por temporadas."},
    ],
    tiers={
        "recovery": [
            ex("Si un pueblo se traslada de un lugar a otro, ¿es nómada o sedentario?", "nómada", "Nómada significa que se traslada."),
            ex("Si un pueblo vive en aldeas y cultiva la tierra, ¿es nómada o sedentario?", "sedentario", "Sedentario significa que vive en un lugar fijo y cultiva."),
            ex("¿Cultivar es sembrar y cuidar plantas o cazar animales?", "sembrar y cuidar plantas", "Cultivar es trabajar la tierra para tener plantas."),
        ],
        "understand": [
            ex(f"{NOM} ¿Por qué los selk'nam se trasladaban?", "Para seguir a los guanacos que cazaban", "Se movían para encontrar el alimento."),
            ex(f"{NOM} ¿Dónde cultivaban los aimara, según la ficha?", "en terrazas", "La ficha dice que cultivaban en terrazas."),
            ex("Elige la frase correcta: A) Los nómadas se quedaban en un mismo lugar todo el año. B) Los nómadas se movían para buscar alimentos.", "B", "Moverse para buscar alimento es lo propio de la vida nómada."),
        ],
        "apply": [
            ex(f"{NOM} Clasifica a los changos como nómadas o sedentarios.", "nómadas", "Se desplazaban por la costa buscando peces y mariscos."),
            ex(f"{NOM} Clasifica a los rapa nui como nómadas o sedentarios.", "sedentarios", "Tenían casas fijas en su isla y cultivaban camote."),
            ex("Una familia vive todo el año en la misma casa y tiene un huerto. ¿Su forma de vida se parece a la nómada o a la sedentaria?", "sedentaria", "Vive en un lugar fijo y cultiva."),
        ],
        "reason": [
            ex("Pedro dice: «Los pueblos nómadas eran mejores porque conocían más lugares». ¿Qué puedes responderle?", "Ninguna forma de vida es mejor; cada una respondía a su paisaje", "Una forma de vida no es mejor que otra."),
            ex("En un lugar con muchos animales que cambian de sitio con las estaciones, ¿qué forma de vida tiene más sentido: ser nómada o ser sedentario?", "ser nómada", "Seguir a los animales ayuda a encontrar alimento."),
        ],
        "challenge": [
            ex(f"{NOM} Ordena en dos grupos: selk'nam, mapuche, changos, aimara, rapa nui.", "Nómadas: selk'nam y changos. Sedentarios: mapuche, aimara y rapa nui", "Los primeros se trasladaban; los otros vivían en lugares fijos."),
            ex("Un pueblo vivía en aldeas, pero en verano algunas familias subían a otro valle con sus animales. ¿Es tan sencillo decir «nunca se movían»?", "No; eran sedentarios pero se movían por temporadas", "Algunos pueblos sedentarios se movían por temporadas."),
        ],
    },
    context=[ex("Un museo muestra una casa de piedra con terrazas de cultivo al lado, y otra casa de cuero que se puede desarmar y llevar. ¿Cuál de las dos pertenece a una forma de vida nómada?", "la casa de cuero que se puede desarmar y llevar", "Es fácil de trasladar, como necesita un pueblo que se mueve.")],
    selfcheck=[
        ex("¿Quién vive casi siempre en un mismo lugar: un pueblo nómada o uno sedentario?", "sedentario", "Sedentario viene de quedarse."),
        ex(f"{NOM} ¿Cómo se llama la casa fija mapuche?", "ruka", "La ficha la llama ruka."),
        ex("¿Una forma de vida es mejor que otra?", "no", "Cada una responde al paisaje."),
    ],
    open_task=task(
        f"Haz una tabla con dos columnas: nómadas y sedentarios. {NOM} Escribe cada pueblo en su columna y, debajo, una razón con la pista de la ficha.",
        "Nómadas: selk'nam (seguían guanacos) y changos (buscaban peces por la costa). Sedentarios: aimara (aldeas y terrazas), mapuche (ruka y cultivo) y rapa nui (casas fijas y camote).",
        ["cinco pueblos clasificados", "una razón de la ficha por pueblo", "no dice que uno sea mejor"], ["tabla escrita"], ["poner a los changos o a los rapa nui en la columna equivocada", "decir que los nómadas eran atrasados"],
        "Pregunta por qué cada pueblo vivía así y no de otra manera. Si dice «mejor» o «peor», recuerda que son formas de vida distintas."),
    reinforce="Explica a alguien en casa qué significa nómada y qué significa sedentario con un ejemplo.",
    extend="Escribe qué cosas tendría que llevar una familia nómada y qué cosas podría dejar en casa una familia sedentaria.",
)

# ---------------------------------------------------------------- clase 3
TEC = ("Ficha de tecnologías: los changos usaban balsas hechas con cuero de lobo marino para pescar en el mar. Los aimara armaban terrazas de cultivo en los cerros y casas de piedra. "
       "Los mapuche hacían la ruka con madera y paja, con techo inclinado para la lluvia. Los selk'nam usaban arco y flecha, y una vivienda de cuero de guanaco que cortaba el viento. "
       "Los rapa nui tallaron moai en piedra volcánica y construyeron casas alargadas con forma de bote dado vuelta.")
register(
    OA, 3,
    materials="Lápiz y papel. La ficha de tecnologías está escrita en cada ejercicio.",
    use="Aprenderé que las herramientas y las casas de los pueblos servían para vivir en su paisaje. Sirve para explicar por qué eran distintas.",
    prior=["Sé qué es nómada y sedentario.", "Sé que los paisajes eran distintos."],
    explain=[
        "La tecnología son los objetos y las técnicas que las personas inventan para resolver necesidades. Una herramienta es un objeto que sirve para hacer un trabajo. Una vivienda es el lugar donde se vive y se protege uno del clima.",
        "Cada pueblo usó lo que había cerca. Los changos hicieron balsas de cuero de lobo marino para pescar. Los aimara armaron terrazas en los cerros para cultivar en la pendiente. Los mapuche construyeron la ruka con madera y paja, con techo inclinado para que escurra la lluvia. Los selk'nam usaron cuero de guanaco para su vivienda, que cortaba el viento frío. Los rapa nui, en su isla volcánica, tallaron los moai en piedra volcánica.",
        "Para explicar una tecnología hay tres preguntas. ¿Qué forma tiene? ¿De qué material está hecha? ¿Para qué sirve? Si juntas las tres respuestas, entiendes cómo ayudaba a vivir en el medio natural, que es el paisaje y el clima de un lugar.",
    ],
    vocab=[("tecnología", "objetos y técnicas para resolver necesidades"), ("herramienta", "objeto que sirve para hacer un trabajo"), ("vivienda", "lugar donde se vive y se protege uno del clima"), ("material", "cosa con que se hace un objeto, como madera o cuero"), ("medio natural", "paisaje y clima de un lugar")],
    worked=[
        {"title": "Forma, material y uso", "problem": f"{TEC} Describe la balsa de los changos con forma, material y uso.", "steps": ["Material: cuero de lobo marino.", "Uso: pescar en el mar.", "Forma: es una balsa, sirve para flotar sobre el agua."], "answer": "Balsa de cuero de lobo marino para pescar"},
        {"title": "Relacionar con el medio", "problem": f"{TEC} ¿Por qué la ruka tenía techo inclinado?", "steps": ["En el sur llueve mucho.", "El techo inclinado deja escurrir el agua."], "answer": "Para que escurra la lluvia"},
    ],
    mistakes=[
        {"wrong": "Decir que los pueblos usaban materiales que no tenían cerca.", "why": "No se piensa en el paisaje.", "fix": "Cada pueblo usaba recursos cercanos: cuero, piedra, madera o paja."},
        {"wrong": "Decir que todas las viviendas eran de madera.", "why": "Se generaliza una sola casa.", "fix": "Hubo casas de piedra, de madera y paja, y de cuero de guanaco."},
    ],
    tiers={
        "recovery": [
            ex(f"{TEC} ¿De qué material estaba hecha la balsa de los changos?", "cuero de lobo marino", "La ficha lo dice."),
            ex(f"{TEC} ¿Qué construían los aimara en los cerros para cultivar?", "terrazas", "Las terrazas son escalones de tierra en la ladera."),
            ex("Una herramienta, ¿es un objeto que sirve para hacer un trabajo o un tipo de clima?", "un objeto que sirve para hacer un trabajo", "Esa es la definición de herramienta."),
        ],
        "understand": [
            ex(f"{TEC} ¿Qué materiales usaban los mapuche para la ruka?", "madera y paja", "La ficha cita esos dos materiales."),
            ex(f"{TEC} ¿Para qué servía el arco y la flecha de los selk'nam?", "para cazar", "Eran sus herramientas de caza, por ejemplo de guanacos."),
            ex("¿Qué es el medio natural: el paisaje y clima del lugar, o la comida de la casa?", "el paisaje y el clima del lugar", "Medio natural es lo que rodea a un pueblo."),
        ],
        "apply": [
            ex(f"{TEC} Los selk'nam vivían en un lugar frío y con viento. ¿Qué característica de su vivienda les ayudaba?", "cuero de guanaco que cortaba el viento", "El cuero protegía del frío y del viento."),
            ex(f"{TEC} Une cada pueblo con su tecnología: A) changos, B) aimara, C) rapa nui. 1) terrazas, 2) balsa de cuero, 3) moai de piedra volcánica.", "A con 2; B con 1; C con 3", "Los changos pescaban en el mar, los aimara cultivaban en cerros y los rapa nui tallaron moai."),
            ex("En un cerro muy inclinado, ¿qué ayuda a cultivar: una terraza como escalón plano o un campo empinado?", "una terraza como escalón plano", "La terraza deja un suelo plano donde crecen las plantas."),
        ],
        "reason": [
            ex("Javiera dice que los changos podrían usar una balsa de cuero porque vivían junto al mar. ¿Qué dato respalda su idea?", "Vivían junto al mar y necesitaban pescar", "La balsa sirve para el trabajo que se hacía en ese medio."),
            ex("Un niño dice: «La ruka sirve igual en el desierto que en el bosque lluvioso». Explica por qué es dudoso, usando el techo.", "El techo inclinado sirve para lluvia, que es abundante en el sur", "La ruka respondía a la lluvia del sur."),
        ],
        "challenge": [
            ex(f"{TEC} Escribe forma, material y uso de la vivienda selk'nam.", "Vivienda de cuero de guanaco que cortaba el viento", "Se nombra el material, el uso y la función contra el clima."),
            ex("¿Por qué tenía sentido que los selk'nam usaran cuero de guanaco en su vivienda?", "Porque tenían guanacos cerca y necesitaban protegerse del frío y del viento", "Usaban un recurso cercano que además cortaba el viento."),
        ],
    },
    context=[ex("Un cartel de museo dice: «Terraza de cultivo aimara, construida con piedras en la ladera». ¿Qué problema del paisaje resuelve esta tecnología?", "cultivar en un cerro inclinado", "Permite tener suelo plano en la pendiente.")],
    selfcheck=[
        ex("¿Qué usaban los changos para pescar en el mar?", "balsas de cuero de lobo marino", "Así lo dice la ficha."),
        ex("¿Con qué hacían los mapuche su ruka?", "madera y paja", "La ficha cita esos materiales."),
        ex("¿La vivienda es para protegerse del clima o para pescar?", "para protegerse del clima", "Esa es su función principal."),
    ],
    open_task=task(
        f"Elige una tecnología de esta ficha y dibújala. {TEC} Debajo escribe: pueblo, material, para qué servía y qué problema del lugar resolvía.",
        "Dibujo de la ruka. Pueblo: mapuche. Material: madera y paja. Servía para vivir y protegerse. Resolvía el problema de la lluvia con su techo inclinado.",
        ["una tecnología de la ficha", "material correcto", "uso explicado", "problema del lugar nombrado"], ["dibujo", "cuatro datos escritos"], ["dibujar una casa moderna", "no decir el material"],
        "Pregunta qué habría pasado si el material no estuviera cerca. Esto ayuda a ver que el medio natural decide qué se usa."),
    reinforce="Mira tu casa y nombra de qué material está hecho el techo y para qué sirve.",
    extend="Compara en una frase una vivienda del sur lluvioso con una del extremo sur frío y ventoso.",
)

# ---------------------------------------------------------------- clase 4
ACT = ("Ficha de trabajos: entre los mapuche, las mujeres tejían en telar, cultivaban huertas y preparaban alimentos; los hombres cultivaban, cazaban, pescaban y levantaban la ruka. "
       "Entre los selk'nam, los hombres cazaban guanacos y las mujeres recolectaban alimentos y preparaban los cueros. Las niñas y los niños ayudaban en tareas más sencillas. "
       "Las descripciones son generales y pueden variar según el lugar y la época.")
CUL = ("Ficha de costumbres (datos generales): alimentación: los mapuche comían papa, maíz, porotos y piñones de la araucaria; los aimara, papa, quinua y carne de llama; "
       "los changos, pescados y mariscos; los selk'nam, carne de guanaco; los rapa nui, camote y pescado. Idioma: los mapuche hablaban el mapuzugun, los aimara el aimara y los rapa nui el rapa nui; de los changos se conoce poco su idioma. "
       "Creencias y fiestas: los mapuche hacían el ngillatun, una ceremonia para agradecer a la naturaleza, y celebraban el We Tripantu, el nuevo año, en invierno; los aimara respetaban a la Pachamama, la Madre Tierra; "
       "los selk'nam hacían el Hain, una ceremonia en que los jóvenes varones pasaban a ser adultos; los rapa nui tallaron moai que recordaban a sus antepasados.")
register(
    OA, 4,
    materials="Lápiz y papel. La ficha de trabajos está escrita en cada ejercicio.",
    use="Aprenderé qué trabajos hacían mujeres, hombres, niñas y niños en los pueblos originarios. Sirve para entender que todos los trabajos eran importantes.",
    prior=["Sé qué es una vivienda.", "Sé que los pueblos tenían herramientas."],
    explain=[
        "En los pueblos originarios, las personas hacían trabajos distintos según el pueblo, la edad y el lugar. Había actividades como cultivar, cazar, pescar, tejer, construir, cocinar y recolectar frutos. Todas eran necesarias para que el pueblo viviera bien.",
        "Entre los mapuche, las mujeres tejían en telar, cultivaban huertas y preparaban alimentos. Los hombres cultivaban, cazaban, pescaban y levantaban la ruka. Entre los selk'nam, los hombres cazaban guanacos y las mujeres recolectaban y preparaban los cueros. Las niñas y niños ayudaban en tareas sencillas.",
        "Cuidado: hoy tenemos otras ideas sobre trabajos de hombres y de mujeres, y no debemos aplicarlas al pasado sin mirar las fuentes. Tampoco hay que decir que un solo trabajo era más importante. Una fuente es algo que nos da información, como un relato, un dibujo o un objeto.",
        "Un pueblo también tenía costumbres: qué comía, qué idioma hablaba, qué creía y qué fiestas celebraba. Una creencia es una idea en que un pueblo cree, y una ceremonia es un acto especial que se hace por esa creencia. Los mapuche comían papa y maíz y hacían el ngillatun para agradecer a la naturaleza. Los aimara respetaban a la Pachamama, la Madre Tierra. Los selk'nam hacían el Hain. Los rapa nui tallaron moai para recordar a sus antepasados. Las ceremonias merecen respeto.",
    ],
    vocab=[("actividad", "trabajo o tarea que se hace"), ("recolectar", "juntar frutos, semillas o mariscos de la naturaleza"), ("telar", "armazón para tejer telas"), ("rol", "tarea que cumple una persona en su grupo"), ("estereotipo", "idea fija y simple sobre un grupo"), ("ceremonia", "acto especial que un pueblo hace por una creencia")],
    worked=[
        {"title": "Leer un trabajo en la ficha", "problem": f"{ACT} ¿Quién cazaba guanacos entre los selk'nam?", "steps": ["Busco selk'nam en la ficha.", "La ficha dice que los hombres cazaban guanacos."], "answer": "Los hombres"},
        {"title": "Evitar el estereotipo", "problem": f"{ACT} Ana dice: «Las mujeres solo cocinaban». ¿Qué dice la ficha?", "steps": ["La ficha dice que las mujeres mapuche tejían, cultivaban y preparaban alimentos.", "Entonces hacían varios trabajos."], "answer": "Las mujeres hacían varios trabajos, no solo cocinar"},
    ],
    mistakes=[
        {"wrong": "Decir que un trabajo era más importante que otro.", "why": "Se compara según ideas de hoy.", "fix": "Todas las tareas ayudaban a que el pueblo viviera."},
        {"wrong": "Pensar que las niñas y los niños no hacían nada.", "why": "Se olvida que ayudaban en la vida diaria.", "fix": "Ayudaban en tareas sencillas, según el pueblo."},
    ],
    tiers={
        "recovery": [
            ex(f"{ACT} ¿Quiénes tejían en telar entre los mapuche?", "las mujeres", "La ficha lo indica."),
            ex(f"{CUL} ¿Qué fiesta celebraban los mapuche en invierno?", "el We Tripantu", "La ficha dice que celebraban el We Tripantu, el nuevo año."),
            ex("Recolectar, ¿es juntar frutos de la naturaleza o fabricar un telar?", "juntar frutos de la naturaleza", "Recolectar es juntar lo que da la naturaleza."),
        ],
        "understand": [
            ex(f"{ACT} ¿Qué hacían las mujeres selk'nam, según la ficha?", "recolectaban alimentos y preparaban los cueros", "Es lo que dice la ficha."),
            ex(f"{CUL} ¿Qué idioma hablaban los mapuche?", "el mapuzugun", "La ficha lo indica."),
            ex("¿Para qué sirve decir que las descripciones son generales?", "Porque pueden variar según el lugar y la época", "No todos los grupos hacían igual."),
        ],
        "apply": [
            ex(f"{ACT} Une el trabajo con quien lo hacía entre los mapuche: 1) tejer en telar, 2) levantar la ruka. A) mujeres, B) hombres.", "1 con A; 2 con B", "Así lo dice la ficha."),
            ex(f"{CUL} ¿Qué alimentos principales tenían los changos, según la ficha?", "pescados y mariscos", "Vivían junto al mar."),
            ex(f"{ACT} ¿Qué trabajo hacían los hombres mapuche además de levantar la ruka?", "cultivar, cazar o pescar", "La ficha menciona esos tres."),
        ],
        "reason": [
            ex("Un niño dice: «Los hombres hacían todo y las mujeres nada». Usa la ficha: ¿tiene razón?", "No; las mujeres tejían, cultivaban, recolectaban y preparaban cueros", "La ficha muestra que ellas hacían trabajos importantes."),
            ex("Una compañera dice: «Hoy las niñas hacen deporte, así que antes también». ¿Por qué es mejor mirar la fuente?", "Porque el pasado puede ser distinto de hoy", "Hay que usar fuentes y no suponer."),
        ],
        "challenge": [
            ex(f"{ACT} Escribe una frase con cuidado que explique el trabajo entre los selk'nam.", "Entre los selk'nam, los hombres cazaban guanacos y las mujeres recolectaban y preparaban los cueros", "Incluye a hombres y mujeres con sus tareas."),
            ex(f"{CUL} Une cada pueblo con su creencia o ceremonia: A) mapuche, B) aimara, C) rapa nui. 1) moai que recordaban a los antepasados, 2) ngillatun, 3) respeto a la Pachamama.", "A con 2; B con 3; C con 1", "Cada pueblo tenía sus propias creencias."),
        ],
    },
    context=[ex("En un libro hay un dibujo de una mujer mapuche frente a un telar y un hombre levantando la estructura de una ruka. ¿Qué dos trabajos muestra el dibujo?", "tejer y construir la ruka", "Muestran las tareas de tejer y de construir.")],
    selfcheck=[
        ex(f"{ACT} ¿Qué cazaban los hombres selk'nam?", "guanacos", "Así lo dice la ficha."),
        ex("¿Qué es un estereotipo?", "una idea fija y simple sobre un grupo", "Los estereotipos simplifican a las personas."),
        ex("¿Una fuente da información o la oculta?", "da información", "Una fuente informa sobre el pasado."),
    ],
    open_task=task(
        f"Dibuja una escena de la vida diaria mapuche con tres personas: una mujer, un hombre y un niño o niña. {ACT} Escribe qué trabajo hace cada una según la ficha.",
        "Mujer: teje en telar. Hombre: levanta la ruka. Niña: ayuda a recoger frutos. Aclaro que estoy usando una ficha general.",
        ["tres personas dibujadas", "trabajos tomados de la ficha", "sin estereotipos de hoy"], ["dibujo", "tres frases escritas"], ["dibujar cosas modernas como celulares", "decir que las mujeres solo cocinaban"],
        "Pregunta de dónde sacó cada trabajo. Debe responder: de la ficha."),
    reinforce="Escribe un trabajo de cada persona que aparece en la ficha mapuche.",
    extend="Explica por qué dos pueblos distintos, como los mapuche y los selk'nam, tenían trabajos y alimentos distintos.",
)

# ---------------------------------------------------------------- clase 5
PAN = ("Ficha del pueblo aimara: viven en el norte, en el altiplano y los valles. Eran sedentarios, en aldeas. Cultivaban papa y quinua en terrazas, y criaban llamas y alpacas. "
       "Construían casas de piedra. Comían papa, quinua y carne de llama. Respetaban a la Pachamama, la Madre Tierra. Su idioma es el aimara. Fuente 1: relato de un libro de historia. Fuente 2: fotografía de terrazas de cultivo en un cerro.")
register(
    OA, 5,
    materials="Lápiz y papel. La ficha del pueblo aimara y las dos fuentes están escritas en cada ejercicio.",
    use="Aprenderé a armar una pequeña descripción de un pueblo con mapa, rasgos y fuentes. Sirve para juntar todo lo aprendido y decir de dónde viene cada dato.",
    prior=["Sé ubicar un pueblo en su territorio.", "Sé qué eran nómada, sedentario, tecnología y roles."],
    explain=[
        "Una descripción de un pueblo junta varios datos: dónde vivía, qué paisaje tenía, si era nómada o sedentario, qué herramientas y casas usaba, qué trabajos hacía, qué comía, qué creía y qué idioma hablaba. Todos esos datos forman su modo de vida.",
        "Para que una descripción sea confiable, cada dato debe tener una fuente. Una fuente puede ser un relato, una fotografía, un dibujo o un objeto de museo. Al escribir, indica de dónde sacaste cada dato, por ejemplo: «según la fotografía de las terrazas».",
        "También hay que ser cuidadoso. No escribas que todos los pueblos eran iguales ni que hoy ya no existen. Escribe «vivían» para el pasado, y recuerda que hay personas de esos pueblos en el presente. Un buen panel tiene un mapa, tres rasgos y dos fuentes.",
    ],
    vocab=[("modo de vida", "forma en que un pueblo vive, trabaja y se alimenta"), ("rasgo", "característica de algo"), ("panel", "cartel con mapa, datos y dibujos"), ("fuente", "algo que da información, como un relato o una fotografía"), ("idioma", "lengua que habla un pueblo")],
    worked=[
        {"title": "Elegir tres rasgos", "problem": f"{PAN} Elige tres rasgos del pueblo aimara para un panel.", "steps": ["Elijo un rasgo de lugar: vivían en el altiplano y los valles.", "Elijo un rasgo de trabajo: cultivaban papa y quinua en terrazas.", "Elijo un rasgo de cultura: su idioma era el aimara."], "answer": "Altiplano y valles; papa y quinua en terrazas; idioma aimara"},
        {"title": "Citar la fuente", "problem": f"{PAN} ¿Qué fuente muestra las terrazas de cultivo?", "steps": ["Reviso las dos fuentes.", "La fuente 2 es una fotografía de terrazas en un cerro."], "answer": "La fuente 2, la fotografía"},
    ],
    mistakes=[
        {"wrong": "Escribir datos sin decir de dónde salieron.", "why": "Se olvida que una descripción necesita fuentes.", "fix": "Después de cada dato anota: «según la fuente 1» o «según la fuente 2»."},
        {"wrong": "Escribir que el pueblo aimara ya no existe.", "why": "Se piensa que los pueblos originarios solo viven en el pasado.", "fix": "Hay personas aimara hoy. En el panel usa «vivían» para hablar del pasado."},
    ],
    tiers={
        "recovery": [
            ex(f"{PAN} ¿En qué zona vivían los aimara?", "en el norte, en el altiplano y los valles", "Así lo dice la ficha."),
            ex(f"{PAN} ¿Eran nómadas o sedentarios?", "sedentarios", "Vivían en aldeas."),
            ex(f"{PAN} ¿A quién respetaban los aimara, según la ficha?", "a la Pachamama, la Madre Tierra", "La ficha nombra sus creencias."),
        ],
        "understand": [
            ex(f"{PAN} ¿Qué comían los aimara, según la ficha?", "papa, quinua y carne de llama", "La ficha lo indica."),
            ex(f"{PAN} ¿Qué cultivaban en las terrazas?", "papa y quinua", "La ficha lo indica."),
            ex("¿Qué es una fuente? Elige: A) un relato, una fotografía o un objeto que informa, B) una fuente de agua.", "A", "En historia, una fuente es algo que da información."),
        ],
        "apply": [
            ex(f"{PAN} Completa: «Los aimara construían casas de ___, según la ficha».", "piedra", "La ficha cita casas de piedra."),
            ex(f"{PAN} Escribe un rasgo de lugar, uno de trabajo y uno de cultura para un panel.", "altiplano; cultivo de terrazas; idioma aimara (u otros de la ficha)", "Cualquier combinación correcta de la ficha sirve."),
            ex(f"{PAN} Escribe qué fuente apoya la frase «cultivaban terrazas en los cerros».", "la fuente 2, la fotografía", "La fotografía muestra las terrazas."),
        ],
        "reason": [
            ex(f"{PAN} Un compañero escribe: «Los aimara eran nómadas». Corrige y justifica con la ficha.", "Eran sedentarios porque vivían en aldeas y cultivaban terrazas", "La ficha da dos pistas de vida sedentaria."),
            ex("Una frase del panel dice «Los aimara ya no existen». ¿Qué cambio haces?", "Hay personas aimara hoy; uso vivían para el pasado", "Los pueblos originarios también viven hoy."),
        ],
        "challenge": [
            ex(f"{PAN} Redacta una frase de tu panel con un dato y su fuente.", "Los aimara cultivaban papa y quinua en terrazas, según el relato", "Debe incluir un dato correcto y su fuente."),
            ex("Además del relato y la fotografía, ¿qué otra fuente podría servir para saber cómo vivían los aimara?", "un objeto de museo, un dibujo u otro", "Objetos y dibujos también dan información."),
        ],
    },
    context=[ex("Una profesora quiere hacer un panel del pueblo aimara con un mapa. ¿Qué parte del mapa de Chile debe marcar: el norte o el extremo sur?", "el norte", "Los aimara vivían en el norte, en el altiplano.")],
    selfcheck=[
        ex(f"{PAN} ¿Qué casas construían los aimara?", "de piedra", "La ficha dice casas de piedra."),
        ex("¿Cuántos rasgos y cuántas fuentes lleva un buen panel de la clase?", "tres rasgos y dos fuentes", "Eso se pide para el panel."),
        ex("Para hablar del pasado, ¿qué verbo conviene: vivían o viven?", "vivían", "El pasado se escribe con vivían."),
    ],
    open_task=task(
        f"Arma un panel en una hoja con: un mapa muy simple de Chile con el norte marcado, tres rasgos y las dos fuentes de la ficha. {PAN} Escribe cada rasgo con su fuente.",
        "Mapa con una flecha al norte. Rasgo 1: vivían en aldeas (relato). Rasgo 2: cultivaban papa y quinua en terrazas (fotografía). Rasgo 3: hablaban el aimara (relato).",
        ["mapa con el norte", "tres rasgos", "dos fuentes identificadas"], ["panel dibujado y escrito"], ["no indicar la fuente", "escribir que los aimara ya no existen"],
        "Pide que lea un rasgo y diga de qué fuente salió. Si no lo sabe, vuelve a la ficha."),
    reinforce="Cuenta a alguien en casa los tres rasgos de tu panel con sus fuentes.",
    extend="Elige otro pueblo de la clase 1 y escribe qué dos fuentes necesitarías para hacer un panel.",
)
