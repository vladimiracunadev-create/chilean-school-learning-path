"""Material del estudiante de 3.º básico, Historia, Geografía y Ciencias Sociales: OA 03 (necesidades y respuestas culturales) y OA 04 (modos de vida antiguos y actuales)."""
from __future__ import annotations

from student_lessons import ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


OA3 = "HI03 OA 03"
OA4 = "HI03 OA 04"

# ================================================================ OA 03
# ---------------------------------------------------------------- clase 1
N1 = ("Ficha de necesidades: todas las personas necesitan alimento, agua, ropa que las abrigue, un lugar donde vivir y sentirse seguras. "
      "Los griegos y los romanos de la Antigüedad tenían las mismas necesidades que nosotros, pero las resolvían a su manera. "
      "Alimento: en Grecia y en Roma se comía pan, aceitunas y queso; cerca del mar también pescado. "
      "Ropa: los griegos usaban el quitón, una túnica de lana o lino; los romanos también usaban túnica, y los ciudadanos hombres una toga encima. "
      "Vivienda: en Atenas, casas con habitaciones alrededor de un patio; en Roma, familias ricas en una domus con patio y muchas otras en insulae de varios pisos.")
register(
    OA3, 1,
    materials="Lápiz y papel. La ficha de necesidades está escrita en cada ejercicio.",
    use="Aprenderé que todas las personas tienen las mismas necesidades, y que las culturas las resuelven de maneras distintas. Sirve para explicar semejanzas y diferencias entre griegos y romanos.",
    prior=["Sé algo de la vida cotidiana en Grecia y en Roma.", "Sé qué es una necesidad básica."],
    explain=[
        "Una necesidad es algo que las personas requieren para vivir bien. Todas las personas del mundo necesitan alimento, agua, ropa que las abrigue, un lugar donde vivir y sentirse seguras. Esto era cierto para los griegos, para los romanos y también para nosotros.",
        "Lo que cambia es cómo cada cultura resuelve esas necesidades. Una cultura es el modo de vida de un pueblo: sus costumbres, su comida, su ropa y sus ideas. Los griegos y los romanos comían pan, aceitunas y queso, y usaban túnicas. Pero las viviendas eran distintas: en Roma muchas familias vivían en insulae, edificios de varios pisos.",
        "Para explicar con un ejemplo concreto, usa esta idea: la necesidad es la misma, la respuesta puede ser distinta. Por ejemplo, la necesidad de abrigarse se resolvía con una túnica de lana, o con una toga encima. Y no es lo mismo «distinto» que «mejor».",
    ],
    vocab=[("necesidad", "algo que las personas requieren para vivir bien"), ("cultura", "modo de vida de un pueblo: costumbres, comida, ropa e ideas"), ("alimento", "comida que necesita el cuerpo"), ("vivienda", "lugar donde se vive"), ("respuesta", "forma en que se resuelve una necesidad")],
    worked=[
        {"title": "Necesidad y respuesta", "problem": f"{N1} Necesidad: abrigarse. ¿Cómo la resolvían los griegos?", "steps": ["Busco la palabra ropa en la ficha.", "Los griegos usaban el quitón, una túnica de lana o lino."], "answer": "Con el quitón, una túnica de lana o lino"},
        {"title": "Una misma necesidad, dos respuestas", "problem": f"{N1} Necesidad: vivienda. Compara Atenas y Roma.", "steps": ["En Atenas: casas con patio.", "En Roma: domus con patio e insulae de varios pisos.", "La necesidad es la misma, pero en Roma hubo una respuesta más: los edificios altos."], "answer": "Las dos necesitaban vivienda; en Roma, además, había insulae"},
    ],
    mistakes=[
        {"wrong": "Decir que los griegos no necesitaban agua ni comida como nosotros.", "why": "Se piensa que son muy distintos a nosotros.", "fix": "Todas las personas tienen las mismas necesidades básicas."},
        {"wrong": "Decir que una cultura resolvió la necesidad «mejor» que otra.", "why": "Se confunde distinto con mejor.", "fix": "Di en qué se parecen y en qué se diferencian, sin decir cuál es mejor."},
    ],
    tiers={
        "recovery": [
            ex(f"{N1} Nombra dos alimentos que se comían en Grecia y en Roma.", "dos de: pan, aceitunas, queso", "La ficha los menciona."),
            ex(f"{N1} ¿Qué usaban los griegos para abrigarse?", "el quitón, una túnica", "La ficha lo dice."),
            ex("Una necesidad, ¿es algo que se requiere para vivir bien o un juego?", "algo que se requiere para vivir bien", "Esa es la definición de necesidad."),
        ],
        "understand": [
            ex(f"{N1} ¿Tenían los griegos y romanos las mismas necesidades básicas que nosotros?", "sí", "La ficha dice que eran las mismas."),
            ex(f"{N1} ¿Qué es una cultura?", "el modo de vida de un pueblo", "Incluye costumbres, comida, ropa e ideas."),
            ex(f"{N1} ¿Qué tipo de vivienda de Roma tenía varios pisos?", "la insula", "Las insulae eran edificios altos."),
        ],
        "apply": [
            ex(f"{N1} Une cada necesidad con una respuesta de la ficha: A) alimento; B) vivienda. 1) casa con patio; 2) pan y aceitunas.", "A con 2; B con 1", "El pan es alimento y la casa es vivienda."),
            ex(f"{N1} Una niña romana se pone una túnica para abrigarse. ¿Qué necesidad resuelve?", "ropa que abrigue", "La túnica abriga."),
            ex(f"{N1} Un pescador griego vende pescado en el puerto. ¿Qué necesidad ayuda a resolver?", "el alimento", "El pescado es alimento."),
        ],
        "reason": [
            ex(f"{N1} Luis dice: «Los romanos no necesitaban casa porque dormían al aire libre». ¿Qué dato de la ficha lo corrige?", "Tenían viviendas como la domus y la insula", "La ficha describe sus viviendas."),
            ex("Ana dice: «Si las insulae eran distintas de las casas atenienses, entonces los romanos eran mejores». ¿Es correcto?", "No, distinto no significa mejor", "Cada cultura resolvía según su lugar."),
        ],
        "challenge": [
            ex(f"{N1} ¿Qué alimentos tienen en común Grecia y Roma, según la ficha?", "pan, aceitunas y queso", "La ficha los nombra para ambas."),
            ex(f"{N1} ¿Qué cosa tenía Roma en su ropa que no menciona la ficha para Grecia?", "la toga de los ciudadanos hombres", "La ficha solo menciona la toga para Roma."),
        ],
    },
    context=[ex("En tu casa hay alimento, agua, ropa y un lugar donde dormir. ¿Qué necesidades básicas resuelve, según la ficha?", "alimento, agua, ropa y vivienda", "Son las necesidades que nombra la ficha.")],
    selfcheck=[
        ex("¿Qué es una cultura?", "el modo de vida de un pueblo", "Incluye costumbres, comida y ropa."),
        ex("¿Las necesidades básicas eran distintas para griegos y romanos?", "no, eran las mismas", "Todas las personas tienen las mismas necesidades."),
        ex("¿Qué casa romana tenía varios pisos?", "la insula", "Era un edificio de varios pisos."),
    ],
    open_task=task(
        f"Haz una tabla con tres columnas: «Necesidad», «Cómo la resolvían en Grecia» y «Cómo la resolvían en Roma». Completa tres filas con alimento, ropa y vivienda. {N1}",
        "Alimento: pan, aceitunas y queso; lo mismo en Roma. Ropa: quitón; túnica y toga. Vivienda: casa con patio; domus e insula.",
        ["tres necesidades", "datos de la ficha", "no dice que uno sea mejor"], ["tabla completa"], ["inventar datos", "decir que una cultura era mejor"],
        "Pregunta qué se parecía y qué cambiaba en cada fila."),
    reinforce="Nombra las cinco necesidades básicas de la ficha.",
    extend="Escribe cómo resuelves hoy una de esas necesidades y en qué se parece a Grecia o a Roma.",
)

# ---------------------------------------------------------------- clase 2
N2 = ("Ficha de recursos: un recurso es algo de la naturaleza que las personas usan, como el agua, la piedra, la madera, la tierra y el mar. "
      "Grecia tiene muchas montañas y poca tierra plana para cultivar, y está rodeada de mar. En Grecia se cultivaban olivos y uvas, se criaban cabras y ovejas, y se navegaba y pescaba. "
      "En Roma se hizo un gran sistema de acueductos que llevaba agua a la ciudad, y había fuentes públicas donde las personas la recogían. "
      "La organización es la forma en que un pueblo reparte tareas y toma decisiones: en Atenas, los ciudadanos decidían en una asamblea; en Roma, primero había cargos elegidos y más tarde gobernaron emperadores.")
register(
    OA3, 2,
    materials="Lápiz y papel. La ficha de recursos está escrita en cada ejercicio.",
    use="Aprenderé cómo los recursos del lugar y la forma de organizarse ayudaron a griegos y romanos a satisfacer sus necesidades. Sirve para explicar sus decisiones con ejemplos.",
    prior=["Sé que todas las personas tienen las mismas necesidades.", "Sé que Grecia tiene mar y montañas."],
    explain=[
        "Un recurso es algo de la naturaleza que las personas usan, como el agua, la piedra, la madera, la tierra y el mar. Cada pueblo usa los recursos que tiene cerca. Grecia tiene muchas montañas y poca tierra plana para cultivar. Por eso se cultivaban olivos y uvas y se criaban cabras y ovejas. Además, estaba rodeada de mar, por lo que se pescaba y se navegaba.",
        "Roma necesitaba mucha agua para una ciudad grande. Por eso construyó acueductos que traían agua desde lugares altos. En la ciudad había fuentes públicas donde las personas recogían agua. Así resolvieron la necesidad de agua con ingeniería.",
        "La organización también ayuda a satisfacer necesidades. Es la forma en que un pueblo reparte tareas y toma decisiones. En Atenas, los ciudadanos decidían en una asamblea. En Roma, primero hubo cargos elegidos y más tarde emperadores. Dos pueblos pueden resolver la misma necesidad con recursos y organización distintos.",
    ],
    vocab=[("recurso", "algo de la naturaleza que las personas usan"), ("organización", "forma de repartir tareas y tomar decisiones"), ("olivo", "árbol cuyo fruto es la aceituna"), ("fuente pública", "lugar de la ciudad donde la gente recogía agua"), ("cultivar", "sembrar y cuidar plantas para usarlas")],
    worked=[
        {"title": "Recurso y uso", "problem": f"{N2} Grecia tiene poca tierra plana. ¿Qué se cultivaba?", "steps": ["Busco qué se cultivaba.", "La ficha dice olivos y uvas."], "answer": "Olivos y uvas"},
        {"title": "Necesidad y organización", "problem": f"{N2} ¿Cómo decidían las cosas importantes los ciudadanos de Atenas?", "steps": ["Busco la organización de Atenas.", "Se reunían en una asamblea."], "answer": "En una asamblea"},
    ],
    mistakes=[
        {"wrong": "Decir que Grecia tenía mucha tierra plana para cultivar.", "why": "Se imagina un campo grande.", "fix": "La ficha dice que Grecia tiene muchas montañas y poca tierra plana."},
        {"wrong": "Decir que los acueductos eran para cultivar.", "why": "Se confunde agua con campo.", "fix": "Los acueductos llevaban agua a la ciudad."},
    ],
    tiers={
        "recovery": [
            ex(f"{N2} ¿Qué es un recurso?", "algo de la naturaleza que las personas usan", "Así lo define la ficha."),
            ex(f"{N2} ¿Qué rodeaba a Grecia?", "el mar", "La ficha dice que estaba rodeada de mar."),
            ex(f"{N2} ¿Qué llevaba agua a la ciudad de Roma?", "los acueductos", "Así lo dice la ficha."),
        ],
        "understand": [
            ex(f"{N2} ¿Por qué había poca tierra para cultivar en Grecia?", "porque tiene muchas montañas", "La ficha da esa causa."),
            ex(f"{N2} ¿Qué animales se criaban en Grecia?", "cabras y ovejas", "La ficha los menciona."),
            ex(f"{N2} ¿Para qué servía una fuente pública en Roma?", "para que las personas recogieran agua", "Así lo dice la ficha."),
        ],
        "apply": [
            ex(f"{N2} Un pueblo griego está junto al mar. ¿Qué dos actividades podía hacer con ese recurso?", "pescar y navegar", "La ficha lo dice."),
            ex(f"{N2} Una familia romana necesita agua para beber. ¿A qué lugar va?", "a una fuente pública", "Allí recogían agua."),
            ex(f"{N2} Une cada pueblo con su forma de decidir: A) Atenas; B) Roma primero. 1) cargos elegidos; 2) asamblea de ciudadanos.", "A con 2; B con 1", "Atenas tenía asamblea y Roma, al principio, cargos elegidos."),
        ],
        "reason": [
            ex(f"{N2} Pedro dice que los griegos cultivaban trigo en grandes llanuras. ¿Qué dato de la ficha lo contradice?", "Grecia tiene muchas montañas y poca tierra plana", "No hay grandes llanuras."),
            ex(f"{N2} ¿Por qué Roma necesitó acueductos?", "porque era una ciudad grande que necesitaba mucha agua", "Los acueductos resolvían esa necesidad."),
        ],
        "challenge": [
            ex(f"{N2} Compara. Atenas y Roma necesitaban decidir. ¿Cómo lo hacían al comienzo, según la ficha?", "Atenas con asamblea de ciudadanos; Roma con cargos elegidos", "Son organizaciones distintas."),
            ex(f"{N2} Une cada recurso de Grecia con lo que se hacía: A) el mar; B) la tierra de cultivo. 1) cultivar olivos y uvas; 2) pescar y navegar.", "A con 2; B con 1", "El mar sirve para pescar y navegar y la tierra para cultivar."),
        ],
    },
    context=[ex("Una ciudad de hoy trae el agua por tuberías desde un embalse. ¿Qué obra romana resolvía una necesidad parecida?", "los acueductos", "También llevaban agua a la ciudad.")],
    selfcheck=[
        ex("En Historia: ¿Qué es un recurso?", "algo de la naturaleza que las personas usan", "Por ejemplo, el agua."),
        ex("¿Qué se cultivaba en Grecia?", "olivos y uvas", "Eran sus cultivos."),
        ex("¿Cómo decidían los ciudadanos de Atenas?", "en una asamblea", "Se reunían a votar."),
    ],
    open_task=task(
        f"Elige Grecia o Roma. Dibuja o escribe tres recursos que tenía y una cosa que hacían con cada uno. {N2}",
        "Roma: agua (acueductos para llevarla), piedra (calzadas y puentes), tierra (campos). Grecia: mar (pescar y navegar), olivos (aceite), montañas (criar cabras).",
        ["tres recursos", "una acción por recurso", "datos de la ficha"], ["lista o dibujo"], ["poner recursos que no están en la ficha sin explicarlos", "no relacionar recurso y uso"],
        "Pregunta qué pasaría si faltara uno de esos recursos."),
    reinforce="Nombra dos recursos de Grecia y uno de Roma.",
    extend="Escribe un recurso de tu región y cómo lo usan las personas hoy.",
)

# ---------------------------------------------------------------- clase 3
N3 = ("Ficha de tecnologías e intercambios: la tecnología son los objetos y técnicas que se inventan para resolver necesidades. "
      "Los griegos construyeron barcos para navegar por el Mediterráneo y llevar aceite, vino y cerámica en jarras llamadas ánforas. "
      "Los romanos construyeron calzadas, que son caminos de piedra, para mover soldados y mercaderías, y puertos para recibir barcos. "
      "Un intercambio es dar algo y recibir otra cosa. Puede ser un trueque, que es cambiar una cosa por otra, o una compra con monedas. Griegos y romanos usaban monedas.")
register(
    OA3, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé cómo la tecnología y el intercambio ayudaban a griegos y romanos a conseguir lo que necesitaban. Sirve para explicar con ejemplos concretos.",
    prior=["Sé qué es un recurso.", "Sé que Grecia tenía mar y Roma tenía acueductos."],
    explain=[
        "La tecnología son los objetos y las técnicas que las personas inventan para resolver necesidades. Los griegos construyeron barcos para navegar por el Mediterráneo. En ellos llevaban aceite, vino y cerámica en jarras llamadas ánforas.",
        "Los romanos construyeron calzadas, caminos de piedra que servían para mover soldados y mercaderías. También construyeron puertos donde llegaban barcos. Gracias a esos caminos y puertos, las cosas viajaban de un lugar a otro y llegaban a más personas. Los romanos también navegaban y los griegos también tenían caminos: aquí vemos un ejemplo de cada pueblo.",
        "Un intercambio es dar algo y recibir otra cosa. Puede ser un trueque, que es cambiar una cosa por otra, o una compra con monedas. Griegos y romanos usaban monedas. Comerciar permitía conseguir lo que no había cerca, como productos de otras tierras.",
    ],
    vocab=[("tecnología", "objetos y técnicas para resolver necesidades"), ("ánfora", "jarra grande para guardar y transportar aceite o vino"), ("trueque", "cambiar una cosa por otra sin usar dinero"), ("comerciar", "comprar, vender o cambiar productos"), ("puerto", "lugar de la costa donde llegan y salen barcos")],
    worked=[
        {"title": "Tecnología y necesidad", "problem": f"{N3} ¿Qué construyeron los romanos para mover soldados y mercaderías?", "steps": ["Busco soldados y mercaderías.", "La ficha dice que eran calzadas."], "answer": "Calzadas"},
        {"title": "Tipos de intercambio", "problem": f"{N3} Una persona cambia dos jarras de aceite por una bolsa de higos. ¿Es trueque o compra con monedas?", "steps": ["Se cambia una cosa por otra.", "No se usa dinero."], "answer": "Trueque"},
    ],
    mistakes=[
        {"wrong": "Decir que los griegos no comerciaban.", "why": "Se piensa que vivían aislados.", "fix": "Navegaban por el Mediterráneo y comerciaban."},
        {"wrong": "Decir que el trueque usa monedas.", "why": "Se mezclan las dos formas.", "fix": "El trueque cambia una cosa por otra sin dinero."},
    ],
    tiers={
        "recovery": [
            ex(f"{N3} ¿Qué es un trueque?", "cambiar una cosa por otra", "Así lo define la ficha."),
            ex(f"{N3} ¿Qué eran las ánforas?", "jarras para llevar aceite y vino", "Así lo dice la ficha."),
            ex(f"{N3} ¿Qué eran las calzadas?", "caminos de piedra", "Así lo dice la ficha."),
        ],
        "understand": [
            ex(f"{N3} ¿Para qué construyeron los griegos barcos?", "para navegar por el Mediterráneo y llevar productos", "La ficha lo explica."),
            ex(f"{N3} ¿Qué recibían los barcos en los puertos romanos?", "mercaderías", "Los puertos recibían barcos con productos."),
            ex(f"{N3} ¿Griegos y romanos usaban monedas?", "sí", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{N3} Un mercader griego lleva aceite en ánforas por mar. ¿Qué tecnología usa?", "un barco", "Los barcos llevaban los productos."),
            ex(f"{N3} Un soldado romano debe llegar rápido a otra ciudad. ¿Qué obra le ayuda?", "una calzada", "Las calzadas servían para mover soldados."),
            ex(f"{N3} Ana entrega cuatro huevos y recibe una jarra de aceite. ¿Es trueque o compra?", "trueque", "Cambia una cosa por otra, sin dinero."),
        ],
        "reason": [
            ex(f"{N3} Ema dice: «Los barcos griegos servían solo para pelear». Corrígela con la ficha.", "También servían para llevar aceite, vino y cerámica", "La ficha dice que se usaban para comerciar."),
            ex(f"{N3} ¿Por qué el comercio era útil para conseguir lo que no había cerca?", "porque se podían traer productos de otras tierras", "Comerciar conecta lugares."),
        ],
        "challenge": [
            ex(f"{N3} Según los ejemplos de la ficha, compara la tecnología de griegos y romanos para mover mercaderías.", "Los griegos usaban barcos y los romanos calzadas y puertos", "Cada uno resolvía con su lugar."),
            ex("Elige la frase correcta. A) El trueque necesita monedas. B) El trueque no necesita monedas.", "B", "Es cambiar una cosa por otra."),
        ],
    },
    context=[ex("En una feria de tu barrio, dos vecinos cambian verduras por huevos. ¿Qué forma de intercambio antiguo es?", "trueque", "Cambian una cosa por otra sin dinero.")],
    selfcheck=[
        ex("¿Qué es un intercambio?", "dar algo y recibir otra cosa", "Puede ser trueque o compra."),
        ex("¿Qué construyeron los romanos para mover soldados?", "calzadas", "Eran caminos de piedra."),
        ex("¿Qué usaban los griegos para llevar aceite por mar?", "barcos y ánforas", "Los barcos y las jarras llamadas ánforas."),
    ],
    open_task=task(
        f"Dibuja un barco griego con tres ánforas y un camino de piedra romano con un carro. Escribe una frase para cada dibujo que diga qué necesidad ayudaba a resolver. {N3}",
        "Barco con ánforas: sirve para llevar aceite y vino a otros lugares y conseguir lo que no hay cerca. Camino con carro: sirve para mover soldados y productos entre ciudades.",
        ["dos tecnologías correctas", "frase con la necesidad", "datos de la ficha"], ["dibujos con frases"], ["decir que el barco es romano", "no explicar la necesidad"],
        "Pregunta qué cambiaría si no existieran esas tecnologías."),
    reinforce="Explica con un ejemplo qué es un trueque.",
    extend="Escribe una forma de intercambio de hoy que no existía en la Antigüedad.",
)

# ---------------------------------------------------------------- clase 4
N4 = ("Ficha de comparación. Atenas: casas con patio; la asamblea de ciudadanos decidía; barcos y ánforas para comerciar; olivos, uvas y cabras. "
      "Roma: domus con patio e insulae de varios pisos; cargos elegidos y más tarde emperadores; acueductos, calzadas y puertos; trigo, aceitunas y uvas. "
      "Regla de la clase: se puede comparar sin decir que una cultura es mejor. Se usan las palabras «se parecen en», «se diferencian en» y «cada una respondió a su lugar».")
register(
    OA3, 4,
    materials="Lápiz y papel. La ficha de comparación está escrita en cada ejercicio.",
    use="Aprenderé a explicar cómo griegos y romanos resolvieron necesidades, sin decir que uno fue mejor. Sirve para hablar de otras culturas con respeto y con ejemplos.",
    prior=["Sé qué son necesidades, recursos y tecnologías.", "Sé qué es una cultura."],
    explain=[
        "Comparar es mirar qué se parece y qué es distinto. Para comparar bien necesitamos ejemplos concretos, como casas, caminos o formas de decidir. Con esos ejemplos podemos explicar cómo diferentes culturas enfrentaron los mismos desafíos.",
        "Los griegos y los romanos necesitaban alimento, agua, vivienda y seguridad. Cada uno usó los recursos que tenía cerca. Los griegos navegaron, cultivaron olivos y criaron cabras. Los romanos construyeron acueductos, calzadas y puertos. Estos son solo algunos ejemplos, porque ambos pueblos hicieron muchas más cosas. Ninguno es «mejor»: cada uno respondió a su lugar y a su tiempo.",
        "Para explicar sin poner a una cultura sobre otra, usa tres frases: «se parecen en», «se diferencian en» y «cada una respondió a su lugar». Evita decir «más avanzado» o «más atrasado». Esas palabras comparan sin entender las razones.",
    ],
    vocab=[("comparar", "mirar qué se parece y qué es distinto"), ("desafío", "algo difícil que hay que resolver"), ("ejemplo concreto", "caso preciso que se puede nombrar"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas son distintas")],
    worked=[
        {"title": "Una semejanza", "problem": f"{N4} Escribe una semejanza entre Atenas y Roma.", "steps": ["Busco algo igual en ambas.", "Las dos tenían casas con patio."], "answer": "Las dos tenían casas con patio"},
        {"title": "Una diferencia con respeto", "problem": f"{N4} ¿Cómo decidían en cada lugar?", "steps": ["En Atenas, una asamblea de ciudadanos.", "En Roma, cargos elegidos y más tarde emperadores.", "No digo cuál es mejor."], "answer": "Se diferencian: asamblea en Atenas y cargos elegidos o emperadores en Roma"},
    ],
    mistakes=[
        {"wrong": "Decir que los romanos eran más avanzados que los griegos.", "why": "Se compara sin entender el contexto.", "fix": "Di en qué se diferencian y por qué cada uno respondió a su lugar."},
        {"wrong": "Comparar sin dar ejemplos.", "why": "Se dice «eran distintos» sin explicar.", "fix": "Nombra un ejemplo concreto, como las casas o las formas de decidir."},
    ],
    tiers={
        "recovery": [
            ex(f"{N4} ¿Qué construyeron los romanos para llevar agua?", "acueductos", "La ficha lo dice."),
            ex(f"{N4} ¿Qué animales criaban los griegos?", "cabras", "La ficha los menciona."),
            ex("Comparar, ¿es mirar qué se parece y qué es distinto o decir quién es mejor?", "mirar qué se parece y qué es distinto", "Esa es la definición de comparar."),
        ],
        "understand": [
            ex(f"{N4} Escribe una diferencia en las viviendas de Atenas y Roma.", "Roma tenía insulae de varios pisos", "La ficha no menciona esos edificios en Atenas."),
            ex(f"{N4} ¿Qué frase de la regla ayuda a no decir que una cultura es mejor?", "cada una respondió a su lugar", "Reconoce el contexto."),
            ex(f"{N4} Nombra una semejanza y una diferencia entre Atenas y Roma.", "Semejanza: casas con patio. Diferencia: formas de decidir", "Las dos tenían casas con patio."),
        ],
        "apply": [
            ex(f"{N4} Elige la frase que compara con respeto. A) Los romanos eran más avanzados. B) Los romanos y los griegos usaron recursos distintos.", "B", "B explica sin juzgar."),
            ex(f"{N4} Une cada necesidad con la solución romana: A) agua; B) mover soldados. 1) calzadas; 2) acueductos.", "A con 2; B con 1", "Los acueductos traían agua y las calzadas movían soldados."),
            ex(f"{N4} Completa con una palabra de la regla: «Los griegos y los romanos ___ en que tenían casas con patio».", "se parecen", "Se usa «se parecen en»."),
        ],
        "reason": [
            ex(f"{N4} Un niño dice que los griegos eran atrasados porque no tenían acueductos. ¿Qué le respondes?", "Cada cultura respondió a su lugar y a sus recursos, y no se puede decir que uno fue atrasado", "Hay que comparar con respeto."),
            ex(f"{N4} ¿Por qué decir «mejor» puede ser un problema al comparar culturas?", "porque no se entienden las razones de cada una", "Cada cultura responde a su lugar y su tiempo."),
        ],
        "challenge": [
            ex(f"{N4} Completa con los ejemplos de la ficha: «Para mover mercaderías, los griegos usaban ___ y los romanos ___».", "barcos y ánforas; calzadas y puertos", "La ficha da esos datos para cada pueblo."),
            ex(f"{N4} Elige el mejor ejemplo concreto para explicar cómo respondieron al mar. A) Los griegos navegaron con barcos. B) Los griegos eran valientes.", "A", "A es un ejemplo concreto; B no explica el mar."),
        ],
    },
    context=[ex("Dos amigos discuten sobre quién tenía mejores caminos. Uno dice «Roma era mejor porque tenía calzadas». ¿Cómo puede decirlo de forma respetuosa?", "Roma construyó calzadas para mover soldados y mercaderías", "Se enuncia el hecho sin decir mejor o peor.")],
    selfcheck=[
        ex("¿Qué frase evita decir que una cultura es mejor?", "cada una respondió a su lugar", "Explica sin juzgar."),
        ex("En Historia: ¿Qué es una semejanza?", "algo en que dos cosas se parecen", "Es lo que tienen en común."),
        ex("¿Qué se necesita para comparar bien?", "ejemplos concretos", "Sin ejemplos no se entiende."),
    ],
    open_task=task(
        f"Escribe un párrafo de 5 líneas que explique cómo los griegos y los romanos resolvieron la necesidad de agua, de alimento o de moverse. Elige una necesidad y usa «se parecen en», «se diferencian en» y «cada una respondió a su lugar». {N4}",
        "Necesidad: moverse. Griegos y romanos se parecen en que necesitaban mover productos. Se diferencian en que, en los ejemplos de la ficha, los griegos usaban barcos y los romanos calzadas. Cada una respondió a su lugar.",
        ["usa las tres frases", "da un ejemplo concreto de cada cultura", "no usa «mejor» ni «atrasado»"], ["párrafo de cinco líneas"], ["decir que una cultura era mejor", "no dar ejemplos"],
        "Subraya las tres frases y pregunta si falta algún ejemplo."),
    reinforce="Di en voz alta una semejanza y una diferencia entre griegos y romanos.",
    extend="Aplica la regla de la clase a otro caso: compara tu casa con una casa de la Antigüedad sin decir cuál es mejor.",
)

# ================================================================ OA 04
# ---------------------------------------------------------------- clase 1
C1 = ("Ficha de criterios. Para comparar modos de vida usamos criterios: costumbres, trabajos y oficios, creencias, vestimenta y ciudad. "
      "Tabla de datos. Antigüedad (Grecia y Roma): costumbres, los niños varones de familias con medios, en Atenas, iban a la escuela y las niñas aprendían en casa; trabajos, agricultor, alfarero, marinero, soldado, comerciante; "
      "creencias, muchos dioses; vestimenta, túnica de lana o lino; ciudad, plaza central (ágora o foro) y templos. "
      "Hoy en Chile: costumbres, todos los niños y niñas van a la escuela; trabajos, profesora, médico, chofer, panadero, comerciante, agricultor, programador; creencias, cada persona o familia cree distinto; "
      "vestimenta, ropa de algodón y de telas fabricadas, como polera y pantalón; ciudad, plaza en el centro, calles pavimentadas, agua por cañerías, electricidad.")
register(
    OA4, 1,
    materials="Lápiz y papel. La tabla de datos está escrita en cada ejercicio.",
    use="Aprenderé a comparar la vida de la Antigüedad con la mía usando criterios. Sirve para ver qué cambió y qué continúa.",
    prior=["Sé algo de la vida de Grecia y Roma.", "Sé qué es comparar."],
    explain=[
        "Un criterio es un aspecto que usamos para comparar. Para comparar modos de vida usamos criterios como costumbres, trabajos y oficios, creencias, vestimenta y la ciudad. Con criterios, la comparación es ordenada y no se mezclan los temas.",
        "Una continuidad es algo que se mantiene igual o casi igual con el tiempo. Un cambio es algo que ya no es como antes. Por ejemplo, las personas siguen vistiendo ropa que las abriga: eso continúa. Pero hoy la ropa se fabrica con máquinas, y eso cambió.",
        "Para comparar, mira siempre el mismo criterio en los dos tiempos. Primero dices cómo era en la Antigüedad. Luego cómo es hoy. Al final dices qué continúa y qué cambió. No uses «mejor» o «peor»: son modos de vida de tiempos distintos.",
    ],
    vocab=[("criterio", "aspecto que se usa para comparar"), ("continuidad", "algo que se mantiene con el tiempo"), ("cambio", "algo que ya no es como antes"), ("oficio", "trabajo que se hace con una habilidad"), ("vestimenta", "ropa que usa una persona")],
    worked=[
        {"title": "Comparar un criterio", "problem": f"{C1} Compara los trabajos de la Antigüedad y de hoy.", "steps": ["Antigüedad: agricultor, alfarero, marinero, soldado, comerciante.", "Hoy: profesora, médico, chofer, panadero, comerciante, agricultor, programador.", "Coinciden agricultor y comerciante, así que continúan; programador es nuevo."], "answer": "Continúan el agricultor y el comerciante; cambió que hoy hay oficios nuevos"},
        {"title": "Cambio en la escuela", "problem": f"{C1} ¿Qué cambió en la escuela?", "steps": ["En Atenas iban niños varones de familias con medios.", "Hoy van todos los niños y niñas."], "answer": "Hoy van niñas y niños"},
    ],
    mistakes=[
        {"wrong": "Comparar sin usar el mismo criterio en los dos tiempos.", "why": "Se mezclan temas distintos.", "fix": "Elige un criterio, como la vestimenta, y compara los dos tiempos."},
        {"wrong": "Decir que la vida de antes era peor que la de hoy.", "why": "Se juzga en vez de comparar.", "fix": "Di qué cambió y qué continúa, sin juzgar."},
    ],
    tiers={
        "recovery": [
            ex(f"{C1} Nombra dos criterios para comparar modos de vida.", "dos de: costumbres, trabajos y oficios, creencias, vestimenta, ciudad", "La ficha los nombra."),
            ex(f"{C1} ¿Qué es un criterio?", "un aspecto que se usa para comparar", "Así lo define la clase."),
            ex(f"{C1} ¿Qué eran el ágora y el foro?", "plazas centrales de la ciudad", "La ficha los menciona como parte de la ciudad."),
        ],
        "understand": [
            ex(f"{C1} ¿Qué es una continuidad?", "algo que se mantiene con el tiempo", "Así lo define la clase."),
            ex(f"{C1} ¿Qué es un cambio?", "algo que ya no es como antes", "Así lo define la clase."),
            ex(f"{C1} Nombra un oficio de la Antigüedad y uno de hoy.", "por ejemplo, alfarero y programador", "La ficha tiene ambas listas."),
        ],
        "apply": [
            ex(f"{C1} Clasifica como continuidad o cambio: personas que usan ropa para abrigarse.", "continuidad", "Se mantiene la necesidad de abrigarse."),
            ex(f"{C1} Clasifica como continuidad o cambio: niñas que van a la escuela.", "cambio", "En Atenas las niñas aprendían en casa."),
            ex(f"{C1} Clasifica como continuidad o cambio: las calles de las ciudades tienen electricidad.", "cambio", "La ficha no la menciona para la ciudad antigua."),
        ],
        "reason": [
            ex(f"{C1} Sofía dice: «Hoy las ciudades tienen electricidad, y eso prueba que la gente de la Antigüedad era menos inteligente». ¿Qué le respondes?", "No se compara así; cambió la tecnología, no la inteligencia", "La tecnología cambia con el tiempo."),
            ex(f"{C1} Tomás compara los trabajos de Grecia con la vestimenta de hoy. ¿Qué error comete?", "no usa el mismo criterio", "Hay que comparar el mismo criterio en los dos tiempos."),
        ],
        "challenge": [
            ex(f"{C1} Escribe dos continuidades y un cambio entre la Antigüedad y hoy usando la tabla.", "Continuidades: usar ropa para abrigarse; haber plaza central en la ciudad. Cambio: hoy van a la escuela niñas y niños", "Otras respuestas con la tabla también sirven."),
            ex("Elige la comparación bien hecha. A) Los griegos vestían túnicas y hoy vestimos polera: cambió la ropa pero sigue la necesidad de abrigarse. B) Los griegos eran peores.", "A", "A compara con un criterio."),
        ],
    },
    context=[ex("Para una exposición, un niño debe comparar la ropa de hoy con la de la Antigüedad. ¿Qué criterio debe usar?", "vestimenta", "La ropa es la vestimenta.")],
    selfcheck=[
        ex("¿Qué es una continuidad?", "algo que se mantiene con el tiempo", "Sigue siendo igual."),
        ex("¿Qué es un cambio?", "algo que ya no es como antes", "Ya no es igual."),
        ex("¿Se debe usar el mismo criterio en los dos tiempos?", "sí", "Así se compara bien."),
    ],
    open_task=task(
        f"Haz una tabla con dos columnas: «En la Antigüedad» y «Hoy». Elige tres criterios de la tabla de datos y completa con datos de la ficha. {C1} Marca cada fila con «continúa» o «cambió».",
        "Vestimenta: túnica de lana o lino / polera y pantalón; cambió el tipo de ropa y continúa la necesidad de abrigarse. Escuela: niños varones / niñas y niños; cambió. Ciudad: plaza central / calles y plazas; continúa la plaza.",
        ["tres criterios", "datos de la ficha", "continuidad o cambio marcado"], ["tabla completa"], ["mezclar criterios", "usar «mejor» o «peor»"],
        "Pregunta cuál criterio cambió más y por qué."),
    reinforce="Repite en voz alta los cinco criterios de comparación.",
    extend="Elige un objeto de tu casa y escribe qué objeto de la Antigüedad cumplía una función parecida.",
)

# ---------------------------------------------------------------- clase 2
C2 = ("Ficha de costumbres y vida familiar. Antigüedad: en Atenas, los niños varones de familias con medios iban a la escuela y aprendían a leer, a escribir, música y gimnasia; las niñas aprendían en casa. "
      "Los niños griegos y romanos jugaban con muñecas, trompos y aros. Las casas tenían patio. La familia vivía junta y las tareas de la casa las hacían miembros de la familia o personas esclavizadas. "
      "Hoy en Chile: la educación escolar es obligatoria para niñas y niños. Hay juegos como las muñecas, el trompo y el aro, y también juegos con pantallas. "
      "Las familias son distintas: hay familias grandes y pequeñas, y en muchas de ellas las tareas de la casa se comparten.")
register(
    OA4, 2,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a comparar las costumbres y la vida familiar de la Antigüedad con las de hoy. Sirve para ver continuidades y cambios.",
    prior=["Sé qué es un criterio.", "Sé qué es continuidad y cambio."],
    explain=[
        "Las costumbres son las formas de actuar que se repiten en un pueblo. Una costumbre es la escuela, los juegos y la vida de la familia. En Atenas, iban a la escuela los niños varones de familias con medios. Aprendían a leer, a escribir, música y gimnasia. Las niñas aprendían en casa.",
        "Los niños griegos y romanos jugaban con muñecas, trompos y aros. Hoy hay juegos parecidos, como el trompo y la muñeca. Eso es una continuidad. También hay juegos nuevos, como los de pantalla, y eso es un cambio.",
        "Hoy en Chile todos los niños y las niñas deben ir a la escuela. Eso cambió mucho. Las familias de hoy son de distintos tamaños, y en muchas de ellas las tareas de la casa se comparten. Cuando comparas la vida familiar, habla de lo que sabes con certeza y no de lo que imaginas.",
    ],
    vocab=[("costumbre", "forma de actuar que se repite en un pueblo"), ("gimnasia", "ejercicios para el cuerpo"), ("obligatoria", "que todos deben cumplir"), ("integrante", "persona que forma parte de una familia o grupo"), ("juego", "actividad que se hace para divertirse")],
    worked=[
        {"title": "Continuidad en juegos", "problem": f"{C2} Nombra un juego que continúa hasta hoy.", "steps": ["Busco juegos en la Antigüedad: muñecas, trompos y aros.", "Busco juegos de hoy: muñecas, trompo y aro.", "Coinciden."], "answer": "La muñeca, el trompo o el aro"},
        {"title": "Cambio en la escuela", "problem": f"{C2} ¿Qué cambió entre la escuela de Atenas y la de hoy?", "steps": ["En Atenas iban los varones.", "Hoy la escuela es obligatoria para niñas y niños."], "answer": "Hoy van niñas y niños"},
    ],
    mistakes=[
        {"wrong": "Decir que las niñas no aprendían nada en la Antigüedad.", "why": "Se piensa que aprender es solo ir a la escuela.", "fix": "La ficha dice que aprendían en casa, pero no iban a la escuela en Atenas."},
        {"wrong": "Decir que los juegos de antes y de hoy son totalmente distintos.", "why": "No se buscan semejanzas.", "fix": "Hay juegos que continúan, como el trompo y la muñeca."},
    ],
    tiers={
        "recovery": [
            ex(f"{C2} ¿Qué aprendían los niños varones en la escuela de Atenas? Nombra dos.", "dos de: leer, escribir, música, gimnasia", "La ficha los nombra."),
            ex(f"{C2} Nombra dos juegos de los niños griegos y romanos.", "dos de: muñecas, trompos, aros", "La ficha los nombra."),
            ex(f"{C2} Hoy en Chile, ¿la escuela es obligatoria?", "sí", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{C2} ¿Dónde aprendían las niñas de Atenas?", "en casa", "La ficha lo dice."),
            ex(f"{C2} ¿Qué es una costumbre?", "una forma de actuar que se repite en un pueblo", "Así lo define la clase."),
            ex(f"{C2} ¿Qué juegos nuevos hay hoy?", "los juegos con pantallas", "La ficha los nombra."),
        ],
        "apply": [
            ex(f"{C2} Clasifica como continuidad o cambio: jugar con un trompo.", "continuidad", "Se jugaba antes y se juega hoy."),
            ex(f"{C2} Clasifica como continuidad o cambio: niñas que van a la escuela.", "cambio", "En Atenas las niñas aprendían en casa."),
            ex(f"{C2} Clasifica como continuidad o cambio: jugar con muñecas.", "continuidad", "Se jugaba antes y se juega hoy."),
        ],
        "reason": [
            ex(f"{C2} Juan dice: «Los niños de la Antigüedad no jugaban». ¿Qué dato de la ficha lo corrige?", "Jugaban con muñecas, trompos y aros", "La ficha los menciona."),
            ex(f"{C2} Marta dice: «Hoy las niñas no van a la escuela, como en Atenas». Corrígela.", "Hoy la escuela es obligatoria para niñas y niños", "Habla del pasado como si fuera hoy."),
        ],
        "challenge": [
            ex(f"{C2} Escribe una continuidad y un cambio en los juegos entre la Antigüedad y hoy.", "Continuidad: el trompo. Cambio: hoy hay juegos con pantallas", "La ficha da ambos datos."),
            ex("Elige la frase que habla con certeza. A) Las niñas de Atenas aprendían en casa, según la ficha. B) Las niñas de Atenas eran felices.", "A", "Solo A está en la ficha."),
        ],
    },
    context=[ex("Un niño dice que su trompo es como el de los niños de Atenas. ¿Es una continuidad o un cambio?", "continuidad", "El juego se mantiene.")],
    selfcheck=[
        ex("¿Los niños y niñas de hoy van a la escuela?", "sí, es obligatoria", "Es un cambio frente a Atenas."),
        ex("¿Qué juego continúa desde la Antigüedad?", "el trompo", "También las muñecas y los aros."),
        ex("¿Dónde aprendían las niñas de Atenas?", "en casa", "No iban a la escuela."),
    ],
    open_task=task(
        f"Haz una tabla con dos columnas, «Antigüedad» y «Hoy». Completa tres filas: escuela, juegos y tareas de la casa. Marca cada una con «continúa» o «cambió». {C2}",
        "Escuela: varones en la escuela y niñas en casa / niñas y niños en la escuela: cambió. Juegos: muñecas, trompos y aros / también esos juegos y los de pantalla: continúa y cambió. Tareas de la casa: familia y esclavizados / integrantes de la familia: cambió.",
        ["tres filas", "datos de la ficha", "marca continúa o cambió"], ["tabla completa"], ["no usar la ficha", "inventar datos de personas reales"],
        "Pregunta con qué juego le gustaría jugar de la Antigüedad."),
    reinforce="Explica a una persona de tu casa un juego que continúa desde la Antigüedad.",
    extend="Pregunta a una persona mayor que conozcas a qué jugaba de niña o niño y compara con un juego de la ficha.",
)

# ---------------------------------------------------------------- clase 3
C3 = ("Ficha de trabajos y desigualdad. Oficios de la Antigüedad: agricultor, que cultiva la tierra; alfarero, que hace vasijas de arcilla; marinero, que navega; soldado; comerciante; constructor, que levanta edificios. "
      "En Grecia y en Roma había personas libres y personas esclavizadas. Los esclavizados trabajaban sin libertad y sin pago, en casas, campos y talleres. "
      "Hoy en Chile: la ley dice que las personas no pueden ser esclavizadas, y el trabajo se paga con un sueldo. Hay oficios como panadero, profesora, chofer, constructor y programador.")
register(
    OA4, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé qué trabajos había en la Antigüedad y qué diferencias había entre las personas. Sirve para comparar con el trabajo de hoy.",
    prior=["Sé qué es un oficio.", "Sé qué es un esclavo."],
    explain=[
        "Un oficio es un trabajo que se hace con una habilidad. En la Antigüedad había oficios como agricultor, alfarero, marinero, soldado, comerciante y constructor. Hoy también hay constructores, comerciantes y panaderos, aunque hay muchos oficios nuevos, como programador.",
        "En Grecia y en Roma había personas libres y personas esclavizadas. Los esclavizados trabajaban sin libertad y sin pago. Eso era una desigualdad: las personas no tenían los mismos derechos. Hoy, en Chile, la ley no permite que alguien sea esclavizado, y el trabajo se paga con un sueldo.",
        "Al comparar el trabajo de antes con el de hoy, hay continuidades y cambios. Continúa que las personas trabajan para tener lo que necesitan. Cambió que hoy hay leyes que protegen a las personas que trabajan. Lo que cambió no fue solo la tecnología, también cambiaron las ideas sobre los derechos.",
    ],
    vocab=[("oficio", "trabajo que se hace con una habilidad"), ("alfarero", "persona que hace vasijas de arcilla"), ("esclavizado", "persona obligada a trabajar sin libertad ni pago"), ("desigualdad", "falta de los mismos derechos entre personas"), ("sueldo", "dinero que se paga por un trabajo")],
    worked=[
        {"title": "Un oficio que continúa", "problem": f"{C3} Nombra un oficio de la Antigüedad que también existe hoy.", "steps": ["Antigüedad: agricultor, alfarero, marinero, soldado, comerciante, constructor.", "Hoy: panadero, profesora, chofer, constructor, programador.", "Coincide constructor."], "answer": "Constructor"},
        {"title": "Un cambio en el trabajo", "problem": f"{C3} ¿Qué cambió entre trabajar sin libertad y trabajar hoy?", "steps": ["Antes había esclavizados sin pago.", "Hoy la ley prohíbe la esclavitud y el trabajo se paga."], "answer": "Hoy el trabajo se paga con un sueldo y nadie puede ser esclavizado"},
    ],
    mistakes=[
        {"wrong": "Decir que todas las personas de la Antigüedad eran libres.", "why": "Se olvida la esclavitud.", "fix": "Había personas libres y personas esclavizadas."},
        {"wrong": "Decir que los oficios de hoy no tienen relación con los de antes.", "why": "No se buscan continuidades.", "fix": "Hay oficios que continúan, como constructor y comerciante."},
    ],
    tiers={
        "recovery": [
            ex(f"{C3} ¿Qué hace un alfarero?", "vasijas de arcilla", "La ficha lo define."),
            ex(f"{C3} ¿Qué hace un agricultor?", "cultiva la tierra", "La ficha lo define."),
            ex(f"{C3} Hoy en Chile, ¿puede una persona ser esclavizada?", "no", "La ley no lo permite."),
        ],
        "understand": [
            ex(f"{C3} ¿Qué es una desigualdad?", "falta de los mismos derechos entre personas", "Así la define la clase."),
            ex(f"{C3} ¿Cómo trabajaban los esclavizados?", "sin libertad y sin pago", "Así lo dice la ficha."),
            ex(f"{C3} ¿Qué recibe hoy una persona por su trabajo?", "un sueldo", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{C3} Clasifica como continuidad o cambio: hay constructores.", "continuidad", "El oficio existe en ambos tiempos."),
            ex(f"{C3} Clasifica como continuidad o cambio: la ley no permite esclavizar a nadie.", "cambio", "En la Antigüedad había esclavizados."),
            ex(f"{C3} Una persona fabrica vasijas de arcilla. ¿Qué oficio de la ficha es?", "alfarero", "El alfarero hace vasijas."),
        ],
        "reason": [
            ex(f"{C3} Rosa dice que el trabajo de un esclavizado era igual al de un trabajador de hoy. ¿Qué diferencia le muestras?", "El esclavizado no tenía libertad ni pago", "Hoy hay sueldo y libertad."),
            ex(f"{C3} ¿Por qué decimos que la esclavitud fue una desigualdad?", "porque las personas no tenían los mismos derechos", "Algunas no eran libres."),
        ],
        "challenge": [
            ex(f"{C3} Compara dos oficios: marinero y chofer. ¿Qué tienen en común?", "los dos trasladan personas o cosas", "Uno lo hace por mar y el otro por calles."),
            ex("Elige la frase más respetuosa. A) Los esclavizados eran personas con menos derechos. B) Los esclavizados no importaban.", "A", "A describe sin despreciar."),
        ],
    },
    context=[ex("Un museo muestra una vasija hecha por un alfarero. ¿Qué oficio de hoy sería parecido, si alguien hace objetos de arcilla o cerámica?", "alfarero o ceramista", "Hace objetos de arcilla.")],
    selfcheck=[
        ex("¿Qué es un oficio?", "un trabajo que se hace con una habilidad", "Es un trabajo especial."),
        ex("¿Qué es un esclavizado?", "una persona obligada a trabajar sin libertad ni pago", "No tenía derechos."),
        ex("¿Qué recibe hoy quien trabaja?", "un sueldo", "Se paga el trabajo."),
    ],
    open_task=task(
        f"Haz una tabla de tres oficios: uno de la Antigüedad que ya no es común, uno que continúa y uno que existe solo hoy. Usa la ficha. {C3} Escribe una frase que diga qué cambió en las ideas sobre los derechos.",
        "Alfarero (menos frecuente en las ciudades hoy); constructor (continúa); programador (solo hoy). Cambió que hoy nadie puede ser esclavizado y todas las personas tienen derechos.",
        ["tres oficios correctos", "una frase sobre derechos", "no desprecia a los esclavizados"], ["tabla con frase"], ["decir que antes todos eran libres", "inventar oficios"],
        "Pregunta por qué hoy se paga el trabajo."),
    reinforce="Nombra tres oficios de la Antigüedad y tres de hoy.",
    extend="Entrevista a una persona adulta que conozcas sobre su oficio y escribe en qué se parece a un oficio antiguo.",
)

# ---------------------------------------------------------------- clase 4
C4 = ("Ficha de ciudades y creencias. Atenas: en un cerro llamado Acrópolis había templos, entre ellos el Partenón. El ágora era la plaza para comprar, vender y conversar. "
      "Roma: tenía el foro, las termas, el Coliseo y calles con edificios de varios pisos. Los romanos construyeron acueductos para llevar agua. "
      "Creencias: los griegos y los romanos creían en muchos dioses y les hacían ofrendas en templos. Los dioses tenían nombres distintos en cada pueblo; por ejemplo, el rey de los dioses era Zeus para los griegos y Júpiter para los romanos. "
      "Hoy en Chile: las ciudades tienen cañerías, electricidad, semáforos y edificios altos. En Chile las personas pueden creer en distintas religiones o en ninguna: hay libertad de creencias.")
register(
    OA4, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a comparar las ciudades y las creencias de la Antigüedad con las de hoy. Sirve para explicar cambios y continuidades con respeto.",
    prior=["Sé qué es un criterio.", "Sé qué es una continuidad y un cambio."],
    explain=[
        "Las ciudades de la Antigüedad tenían lugares importantes. Atenas tenía la Acrópolis, un cerro con templos como el Partenón, y el ágora, una plaza. Roma tenía el foro, las termas, el Coliseo y edificios de varios pisos. También tenía acueductos que llevaban agua.",
        "Las ciudades de hoy tienen cañerías, electricidad, semáforos y edificios altos. Eso cambió. Pero también continúan cosas: las ciudades siguen teniendo plazas, templos o iglesias y lugares donde la gente se junta.",
        "Griegos y romanos creían en muchos dioses y les hacían ofrendas en templos. Los dioses tenían nombres distintos: el rey de los dioses era Zeus para los griegos y Júpiter para los romanos. Hoy en Chile hay libertad de creencias. Eso significa que cada persona puede creer en distintas religiones o en ninguna, y hay que respetarlas todas.",
    ],
    vocab=[("Acrópolis", "cerro de Atenas con templos"), ("ofrenda", "regalo que se entrega a un dios"), ("templo", "edificio para honrar a los dioses"), ("creencia", "idea en la que una persona confía, sobre dioses o sobre el mundo"), ("libertad de creencias", "derecho a creer lo que cada persona decida")],
    worked=[
        {"title": "Comparar lugares", "problem": f"{C4} ¿Qué lugar de Atenas se parece al foro de Roma?", "steps": ["El foro era el centro de la ciudad romana.", "En Atenas, el centro para comprar y conversar era el ágora."], "answer": "El ágora"},
        {"title": "Creencias", "problem": f"{C4} ¿Qué nombre tenía el rey de los dioses en Roma?", "steps": ["Busco el rey de los dioses.", "Para los griegos era Zeus y para los romanos Júpiter."], "answer": "Júpiter"},
    ],
    mistakes=[
        {"wrong": "Decir que hoy todas las personas creen lo mismo.", "why": "Se generaliza.", "fix": "Hoy hay libertad de creencias y cada persona puede creer distinto."},
        {"wrong": "Decir que los dioses de Grecia y Roma eran exactamente los mismos con los mismos nombres.", "why": "Se ignoran los nombres distintos.", "fix": "Los nombres eran distintos, como Zeus y Júpiter."},
    ],
    tiers={
        "recovery": [
            ex(f"{C4} ¿Cómo se llamaba el cerro de Atenas con templos?", "Acrópolis", "La ficha lo nombra."),
            ex(f"{C4} Nombra dos lugares de Roma.", "dos de: foro, termas, Coliseo", "La ficha los nombra."),
            ex(f"{C4} ¿Qué es un templo?", "un edificio para honrar a los dioses", "Así lo define la clase."),
        ],
        "understand": [
            ex(f"{C4} ¿Qué hacían los griegos y romanos en los templos?", "ofrendas a los dioses", "La ficha lo dice."),
            ex(f"{C4} ¿Qué es la libertad de creencias?", "el derecho a creer lo que cada persona decida", "Así la define la clase."),
            ex(f"{C4} ¿Cómo se llamaba Zeus entre los romanos?", "Júpiter", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{C4} Clasifica como continuidad o cambio: las ciudades tienen una plaza donde se junta la gente.", "continuidad", "El ágora y el foro tenían ese uso."),
            ex(f"{C4} Clasifica como continuidad o cambio: las ciudades tienen semáforos.", "cambio", "No existían en la Antigüedad."),
            ex(f"{C4} Clasifica como continuidad o cambio: hay templos o iglesias en las ciudades.", "continuidad", "Había templos en Atenas y Roma y hay lugares de culto hoy."),
        ],
        "reason": [
            ex(f"{C4} Ema dice que todas las personas de hoy en Chile creen en dioses griegos. Corrígela con la ficha.", "Hoy hay libertad de creencias y las personas creen distinto", "Cada persona decide lo que cree."),
            ex(f"{C4} ¿Por qué hay que respetar las creencias de las personas?", "porque cada persona puede creer distinto", "Es la libertad de creencias."),
        ],
        "challenge": [
            ex(f"{C4} Compara el agua en Roma y hoy. ¿Cómo llegaba antes y cómo llega ahora?", "Antes, por acueductos; ahora, por cañerías", "Cambió la forma, no la necesidad."),
            ex("Elige la frase correcta. A) Los dioses romanos se llamaban igual que los griegos. B) Algunos dioses tenían nombres distintos en cada pueblo.", "B", "Zeus y Júpiter lo muestran."),
        ],
    },
    context=[ex("Un viajero visita la Acrópolis y ve el Partenón. ¿Qué tipo de edificio es, según la ficha?", "un templo", "El Partenón era un templo.")],
    selfcheck=[
        ex("¿Qué había en la Acrópolis?", "templos, como el Partenón", "Era un cerro con templos."),
        ex("¿Qué es la libertad de creencias?", "el derecho a creer lo que cada persona decida", "Hoy se respeta."),
        ex("¿Cómo llegaba el agua a Roma?", "por acueductos", "Los romanos los construyeron."),
    ],
    open_task=task(
        f"Haz un cartel con dos columnas: «Ciudad de la Antigüedad» y «Ciudad de hoy». Escribe tres lugares en cada una, y encierra en un círculo los que continúan. {C4} Agrega una frase que muestre respeto por las creencias.",
        "Antigüedad: ágora, templos, acueductos. Hoy: plazas, iglesias o templos, cañerías. Se encierran las plazas y los templos. Frase: cada persona puede creer distinto y hay que respetarlo.",
        ["tres lugares por columna", "continuidades marcadas", "frase de respeto"], ["cartel completo"], ["inventar lugares", "burlarse de una creencia"],
        "Pregunta cuál lugar de la ciudad antigua le gustaría visitar."),
    reinforce="Nombra tres lugares de las ciudades antiguas y para qué servían.",
    extend="Compara en una frase el foro de Roma con una plaza de tu ciudad.",
)
