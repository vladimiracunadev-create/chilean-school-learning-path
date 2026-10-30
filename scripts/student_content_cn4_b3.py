"""Cuaderno del estudiante, 4.º básico Ciencias Naturales: OA 15 (capas internas de la Tierra) y OA 16 (placas tectónicas y cambios de la superficie)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA15, OA16 = "CN04 OA 15", "CN04 OA 16"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 15
register(
    OA15, 1,
    materials="Plasticina o masa de sal de tres colores, o lápices de colores y papel. Para el modelo no hace falta cortar nada: se forma con bolitas y capas.",
    use="Aprenderé que la Tierra por dentro tiene tres capas y en qué orden están. Sirve para entender qué hay bajo nuestros pies.",
    prior=["Sé que la Tierra es una esfera.", "Sé que vivimos sobre una superficie de roca y suelo."],
    explain=[
        "La Tierra no es igual por dentro que por fuera. Tiene tres capas, una dentro de otra: la corteza, el manto y el núcleo. La corteza es la capa de afuera, donde vivimos. Debajo está el manto, y en el centro del planeta está el núcleo.",
        "Los científicos no pueden llegar al centro de la Tierra. El agujero más profundo que se ha hecho llega a unos 12 kilómetros, y el manto y el núcleo están mucho más abajo. Por eso estudian las capas con modelos y con las ondas que producen los sismos, que viajan por el interior.",
        "Un modelo es una representación sencilla de algo real. Puedo hacer un modelo de la Tierra con bolitas de plasticina: una bolita pequeña de un color para el núcleo, una capa gruesa de otro color para el manto y una capa muy delgada para la corteza. El modelo ayuda a ver el orden, pero no es la Tierra real.",
    ],
    vocab=[("corteza", "capa externa y delgada de la Tierra"), ("manto", "capa que está bajo la corteza; es la más gruesa"), ("núcleo", "capa del centro de la Tierra"), ("capa", "parte que está sobre o bajo otra"), ("modelo", "representación sencilla de algo real")],
    worked=[
        {"title": "Ordenar las capas", "problem": "Ordena las capas de la Tierra desde la superficie hasta el centro.", "steps": ["La capa de afuera, donde vivimos, es la corteza.", "Debajo de la corteza está el manto.", "En el centro está el núcleo."], "answer": "Corteza, manto y núcleo"},
        {"title": "Suma de capas", "problem": "Con datos redondeados, la corteza y el manto juntos llegan hasta unos 2.900 km de profundidad y desde ahí al centro hay unos 3.470 km (el núcleo). ¿Cuántos km hay desde la superficie hasta el centro?", "steps": ["Sumo las dos distancias: 2.900 + 3.470.", "El resultado es la distancia aproximada al centro."], "answer": "6.370 km aproximadamente"},
    ],
    mistakes=[
        {"wrong": "Pensar que la Tierra es sólida y pareja por dentro.", "why": "Solo vemos la superficie.", "fix": "Por dentro tiene tres capas distintas."},
        {"wrong": "Decir que el núcleo está justo bajo nuestros pies.", "why": "Se piensa que todo lo de abajo es el centro.", "fix": "Bajo nuestros pies está primero la corteza; el núcleo está muy lejos, en el centro."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas capas tiene la Tierra por dentro?", "Tres", "Son la corteza, el manto y el núcleo."),
            ex("¿Cuál es la capa externa de la Tierra?", "La corteza", "Es la capa donde vivimos."),
            ex("Completa: el ___ está en el centro de la Tierra (núcleo o manto).", "núcleo", "Es la capa más interna."),
        ],
        "understand": [
            ex("¿Qué capa de la Tierra está entre la corteza y el núcleo?", "El manto", "Está en el medio."),
            ex("¿Por qué los científicos usan modelos para estudiar el interior de la Tierra?", "Porque no se puede llegar al centro", "No podemos ver ni cavar hasta el centro."),
            ex("En Ciencias, ¿qué es un modelo?", "Una representación sencilla de algo real", "Ayuda a entender sin tener el objeto real."),
        ],
        "apply": [
            ex("Ordena de afuera hacia adentro: núcleo, corteza, manto.", "Corteza, manto, núcleo", "Es el orden desde la superficie al centro."),
            arith("Con datos redondeados, la corteza y el manto juntos llegan a 2.900 km de profundidad y el núcleo tiene 3.470 km hasta el centro. ¿Cuántos km hay desde la superficie hasta el centro?", "2900+3470", "Se suman las dos distancias.", " km"),
            ex("En un modelo de plasticina, ¿qué capa representa la bolita pequeña del centro?", "El núcleo", "Es la capa central."),
        ],
        "reason": [
            ex("En un modelo, una compañera hizo la corteza más gruesa que el manto. ¿Qué error cometió?", "La corteza es mucho más delgada que el manto", "El manto es la capa más gruesa."),
            ex("¿Por qué el modelo de plasticina no es igual a la Tierra real?", "Porque es una representación sencilla", "Un modelo muestra el orden, pero no todos los detalles."),
        ],
        "challenge": [
            arith("Con datos redondeados, el núcleo mide 3.470 km hasta el centro y el manto 2.900 km de espesor. ¿Cuántos km más mide el núcleo que el manto?", "3470-2900", "Se resta la medida menor de la mayor.", " km"),
            ex("El agujero más profundo hecho por personas llega a 12 km y la corteza tiene unos 30 km en muchos lugares. ¿Ha llegado a perforar completamente la corteza?", "No", "12 km es menos que 30 km."),
        ],
    },
    context=[ex("Un niño dice que, si cava un hoyo muy profundo en su patio, llegará al núcleo. Con lo que aprendiste, ¿qué capa encontraría primero?", "La corteza", "Bajo el suelo está primero la corteza.")],
    selfcheck=[
        ex("¿Cuáles son las tres capas de la Tierra?", "Corteza, manto y núcleo", "Son las tres capas del interior."),
        ex("¿Cuál es la capa más externa?", "La corteza", "Es la que está en la superficie."),
        ex("¿Cuál es la capa del centro?", "El núcleo", "Está en el centro del planeta."),
    ],
    open_task=task(
        "Haz un modelo de la Tierra con plasticina de tres colores: una bolita para el núcleo, una capa más gruesa que la rodea para el manto y una capa muy delgada para la corteza. Si no tienes plasticina, haz un dibujo de tres círculos, uno dentro del otro. Rotula cada capa y escribe una frase que diga una ventaja y un límite de tu modelo.",
        "Núcleo: bolita roja al centro; manto: capa gruesa naranja; corteza: capa delgada marrón. Ventaja: muestra el orden. Límite: no está a escala real y no muestra la temperatura.",
        ["tres capas en el orden correcto", "las capas están rotuladas", "ventaja y límite del modelo"],
        ["modelo o dibujo", "rótulos", "frase de ventaja y límite"],
        ["invertir el orden", "dibujar la corteza más gruesa que el manto"],
        "Reconoce el modelo y pide revisar el grosor relativo si la corteza no es delgada.",
    ),
    reinforce="Dibuja un círculo, divídelo en tres capas y escribe sus nombres de adentro hacia afuera.",
    extend="Averigua qué instrumento registra las ondas de los sismos y cómo ayudan a conocer el interior de la Tierra.",
)

register(
    OA15, 2,
    materials="Papel y lápices. Solo se usan descripciones escritas; no se necesitan materiales especiales.",
    use="Aprenderé cómo son la corteza y el manto: de qué están hechos, qué tan rígidos son y cuánta temperatura tienen. Sirve para entender por qué la superficie es sólida y por qué hay volcanes.",
    prior=["Sé que la Tierra tiene tres capas.", "Sé que el orden es corteza, manto y núcleo."],
    explain=[
        "La corteza es la capa más delgada y la más fría. Está formada por rocas sólidas y rígidas. Rígido quiere decir que no se dobla ni fluye. En la corteza están los continentes, los océanos y todo lo que vemos. Debajo del suelo de la superficie la temperatura va aumentando con la profundidad.",
        "El manto es la capa más gruesa de la Tierra. También está formado por rocas, pero mucho más calientes que las de la corteza. La parte superior del manto es rígida, como la corteza. Más abajo, las rocas están tan calientes que fluyen muy, muy lentamente, como una plasticina que se deforma durante millones de años.",
        "Al ir bajando de la corteza al manto, la temperatura aumenta. En el manto hay roca derretida llamada magma en algunos lugares. Cuando sale a la superficie por un volcán, se llama lava. La corteza y la parte alta del manto forman una capa rígida que se mueve en bloques, como veremos más adelante.",
    ],
    vocab=[("roca", "material duro que forma el suelo y las montañas"), ("rígido", "que no se dobla ni fluye con facilidad"), ("fluir", "moverse como un líquido, muy lento"), ("magma", "roca derretida bajo la superficie"), ("lava", "magma que sale por un volcán")],
    worked=[
        {"title": "Comparar espesor", "problem": "La corteza tiene unos 30 km de espesor y el manto unos 2.900 km. ¿Cuál es más gruesa?", "steps": ["Comparo los números: 2.900 es mayor que 30.", "El manto es mucho más grueso."], "answer": "El manto"},
        {"title": "Cómo cambia la temperatura", "problem": "Al bajar desde la corteza hacia el manto, ¿la temperatura sube o baja?", "steps": ["La corteza es la capa más fría.", "En el manto las rocas están más calientes."], "answer": "Sube"},
    ],
    mistakes=[
        {"wrong": "Decir que el manto es un océano de líquido.", "why": "Se piensa que fluir significa ser líquido.", "fix": "El manto es en su mayor parte roca sólida; solo fluye muy lento."},
        {"wrong": "Pensar que magma y lava son lo mismo en todos los casos.", "why": "Se usan como si fueran sinónimos.", "fix": "Magma está bajo la superficie; lava es magma que salió afuera."},
    ],
    tiers={
        "recovery": [
            ex("¿De qué está formada la corteza: de rocas o de agua?", "De rocas", "Es sólida y rocosa."),
            ex("¿Cuál capa es más gruesa: la corteza o el manto?", "El manto", "El manto mide miles de kilómetros."),
            ex("Completa: al bajar al manto la temperatura ___ (sube o baja).", "sube", "El manto es más caliente que la corteza."),
        ],
        "understand": [
            ex("¿Qué significa que la corteza sea rígida?", "Que no se dobla ni fluye con facilidad", "Rígido es duro."),
            ex("¿Cómo se llama la roca derretida bajo la superficie?", "Magma", "Cuando sale a la superficie se llama lava."),
            ex("¿Qué diferencia hay entre magma y lava?", "El magma está bajo la superficie y la lava salió afuera", "Depende de dónde esté."),
        ],
        "apply": [
            arith("El manto mide 2.900 km y la corteza 30 km. ¿Cuántos km más grueso es el manto?", "2900-30", "Se resta el espesor de la corteza.", " km"),
            ex("Un volcán expulsa roca derretida que corre por la ladera. ¿Se llama magma o lava?", "Lava", "Ya salió a la superficie."),
            ex("Clasifica como característica de la corteza o del manto: más delgada; más gruesa; más fría; más caliente.", "Corteza: más delgada y más fría. Manto: más gruesa y más caliente", "Cada pareja describe una capa."),
        ],
        "reason": [
            ex("Un niño dice que el manto es líquido porque «fluye». ¿Qué le explicas?", "Que es roca sólida que fluye muy lentamente", "Fluye durante millones de años."),
            ex("¿Por qué la superficie de la Tierra es sólida si el interior es muy caliente?", "Porque la corteza es una capa de roca fría y rígida", "La corteza está más fría que el manto."),
        ],
        "challenge": [
            ex("Si pudieras bajar por un túnel imaginario desde la superficie, ¿qué cambia primero: la temperatura aumenta o disminuye?", "Aumenta", "La temperatura sube con la profundidad."),
            ex("Una amiga dice: «el manto es más delgado que la corteza porque está más lejos». ¿Qué datos la corrigen?", "El manto mide unos 2.900 km y la corteza unos 30 km", "El manto es mucho más grueso."),
        ],
    },
    context=[ex("En Chile hay volcanes activos que a veces expulsan roca derretida. ¿De qué capa viene el magma que alimenta un volcán?", "Del interior, bajo la corteza, en el manto", "El magma se forma donde las rocas están muy calientes.")],
    selfcheck=[
        ex("¿Qué capa de la Tierra es la más delgada?", "La corteza", "Mide solo decenas de kilómetros."),
        ex("¿Qué capa es la más gruesa?", "El manto", "Tiene unos 2.900 km."),
        ex("¿Cuándo se llama lava a la roca derretida?", "Cuando sale a la superficie", "Bajo tierra se llama magma."),
    ],
    open_task=task(
        "Completa esta tabla con una palabra en cada casilla: Corteza (delgada o gruesa; fría o caliente; rígida o fluye), Manto (delgado o grueso; frío o caliente; rígido arriba o fluye abajo). Luego escribe una frase que explique por qué la superficie es sólida.",
        "Corteza: delgada, fría, rígida. Manto: grueso, caliente, rígido arriba y fluye muy lento abajo. La superficie es sólida porque la corteza es una capa de roca fría y rígida.",
        ["tabla completa", "diferencia espesor y temperatura", "frase con rigidez de la corteza"],
        ["tabla", "frase explicativa"],
        ["decir que el manto es líquido", "confundir espesores"],
        "Valora la tabla y pide corregir cualquier casilla errónea.",
    ),
    reinforce="Escribe tres diferencias entre la corteza y el manto.",
    extend="Averigua qué tipo de roca es común en la zona donde vives.",
)

register(
    OA15, 3,
    materials="Papel, lápices de colores. Los datos de temperatura están escritos en el cuaderno; no se hacen experimentos con calor.",
    use="Aprenderé cómo es el núcleo de la Tierra: de qué está hecho, si es sólido o líquido y qué temperatura tiene. Sirve para completar el modelo de las tres capas.",
    prior=["Sé que la Tierra tiene corteza, manto y núcleo.", "Sé que la temperatura aumenta al ir hacia el interior."],
    explain=[
        "El núcleo es la capa del centro de la Tierra. Está formado principalmente por metales: hierro y níquel. Se divide en dos partes. El núcleo externo es líquido, es decir, el metal está fundido y se mueve. El núcleo interno es sólido, aunque está muy caliente, porque la presión es enorme.",
        "El núcleo es la parte más caliente de la Tierra. Se calcula que el núcleo interno tiene temperaturas de alrededor de 5.000 °C, parecidas a las de la superficie del Sol. A tanta profundidad no se puede medir con un termómetro; se calcula con modelos y con el estudio de las ondas sísmicas.",
        "Ahora puedo comparar las capas. La corteza es rocosa, rígida y fría; el manto es rocoso, caliente y fluye lentamente; el núcleo es metálico, con una parte líquida y otra sólida, y es la capa más caliente. En los tres casos la temperatura aumenta hacia el centro.",
    ],
    vocab=[("núcleo externo", "parte líquida del núcleo, hecha de metal fundido"), ("núcleo interno", "parte sólida del centro de la Tierra"), ("metal", "material duro y brillante, como el hierro"), ("presión", "fuerza que aprieta sobre una superficie"), ("fundido", "derretido por mucho calor")],
    worked=[
        {"title": "Características del núcleo", "problem": "¿De qué está hecho el núcleo y en qué estados está?", "steps": ["Está hecho principalmente de hierro y níquel, que son metales.", "El externo es líquido y el interno es sólido."], "answer": "Metales; externo líquido e interno sólido"},
        {"title": "Cambio de temperatura", "problem": "La temperatura de una zona del manto es 1.000 °C y la del núcleo interno es 5.000 °C. ¿Cuántos °C más caliente es el núcleo interno?", "steps": ["Resto la menor de la mayor.", "5.000 − 1.000 = 4.000."], "answer": "4.000 °C más"},
    ],
    mistakes=[
        {"wrong": "Decir que todo el núcleo es líquido.", "why": "Se piensa que como está tan caliente, todo se derrite.", "fix": "El núcleo interno es sólido por la enorme presión; solo el externo es líquido."},
        {"wrong": "Pensar que el núcleo está hecho de roca como el manto.", "why": "Se generaliza desde las capas de arriba.", "fix": "El núcleo es de metales, principalmente hierro y níquel."},
    ],
    tiers={
        "recovery": [
            ex("¿De qué materiales está hecho el núcleo?", "De metales, hierro y níquel", "Es principalmente metálico."),
            ex("¿El núcleo externo es sólido o líquido?", "Líquido", "Es metal fundido."),
            ex("¿El núcleo interno es sólido o líquido?", "Sólido", "La presión lo mantiene sólido."),
        ],
        "understand": [
            ex("¿Qué capa es la más caliente de la Tierra?", "El núcleo", "Está en el centro."),
            ex("¿Por qué el núcleo interno es sólido aunque está muy caliente?", "Porque la presión es enorme", "La presión lo mantiene sólido."),
            ex("¿Por qué no se puede medir la temperatura del núcleo con un termómetro?", "Porque no se puede llegar hasta ahí", "Se estima con modelos."),
        ],
        "apply": [
            arith("El núcleo interno está a unos 5.000 °C y la superficie de la corteza a 15 °C. ¿Cuántos °C más caliente es el núcleo interno?", "5000-15", "Se resta la temperatura menor de la mayor.", " °C"),
            ex("Clasifica cada característica como corteza, manto o núcleo: capa metálica; capa más fría; capa más gruesa.", "Núcleo: capa metálica. Corteza: capa más fría. Manto: capa más gruesa", "Cada rasgo se asocia con una sola capa."),
            ex("Ordena de menos a más caliente: núcleo, corteza, manto.", "Corteza, manto, núcleo", "La temperatura aumenta hacia el centro."),
        ],
        "reason": [
            ex("Un compañero dice que el núcleo es de roca como el manto. Usa lo aprendido para corregirlo.", "El núcleo es de hierro y níquel, que son metales", "Su composición es metálica."),
            ex("Tomás dice que el centro de la Tierra es líquido porque está muy caliente. ¿Qué dato lo contradice?", "El núcleo interno es sólido por la presión", "Solo el núcleo externo es líquido."),
        ],
        "challenge": [
            ex("Si la temperatura aumenta hacia el centro, ¿qué esperarías de la temperatura del manto comparada con la del núcleo?", "Que sea menor que la del núcleo", "El manto está más lejos del centro."),
            ex("Una tabla dice que el manto está a 1.000 °C y el núcleo interno a 5.000 °C. Otra afirma que el manto es más caliente que el núcleo. ¿Qué tabla concuerda con lo aprendido?", "La primera", "El núcleo es la capa más caliente."),
        ],
    },
    context=[ex("En un museo, un panel dice que el interior de la Tierra tiene una parte líquida de metal que se mueve. ¿De qué parte habla: núcleo externo o corteza?", "Núcleo externo", "Es metal fundido en el centro.")],
    selfcheck=[
        ex("¿Cuál es la capa más caliente de la Tierra?", "El núcleo", "Está en el centro."),
        ex("¿Qué dos metales forman principalmente el núcleo?", "Hierro y níquel", "Son sus materiales principales."),
        ex("¿Cuál parte del núcleo es líquida?", "El núcleo externo", "El interno es sólido."),
    ],
    open_task=task(
        "Completa una tabla de comparación con las tres capas: composición (roca o metal), estado (sólido, fluye lento o líquido y sólido) y temperatura (fría, caliente o más caliente). Luego dibuja las capas en orden y pinta cada una con un color distinto.",
        "Corteza: roca, sólida y rígida, fría. Manto: roca, parte rígida y parte que fluye lento, caliente. Núcleo: metal, externo líquido e interno sólido, más caliente.",
        ["tabla con tres capas", "composición y estado correctos", "dibujo ordenado"],
        ["tabla", "dibujo"],
        ["decir que el núcleo es roca", "decir que todo el núcleo es líquido"],
        "Reconoce la tabla y pide revisar la composición del núcleo si falla.",
    ),
    reinforce="Escribe una oración con la palabra «núcleo» que diga una característica de esa capa.",
    extend="Averigua para qué sirve el campo magnético de la Tierra y qué relación tiene con el núcleo.",
)

register(
    OA15, 4,
    materials="Papel, lápiz y los datos de las tablas escritas aquí. Si quieres, usa tu modelo de plasticina de la primera clase.",
    use="Aprenderé a comparar las capas con una tabla y a explicar qué muestra y qué no muestra un modelo. Sirve para usar los modelos con cuidado y sin errores.",
    prior=["Conozco la composición, rigidez y temperatura de las tres capas.", "Sé que un modelo es una representación sencilla."],
    explain=[
        "Para comparar las capas uso tres criterios: composición (de qué están hechas), rigidez (si son rígidas o fluyen) y temperatura. Corteza: rocas rígidas y frías. Manto: rocas calientes, rígidas arriba y que fluyen lento abajo. Núcleo: metales, líquido por fuera y sólido por dentro, muy caliente.",
        "Los modelos tienen ventajas y límites. Un dibujo en círculos muestra el orden y los nombres de las capas. Pero no muestra el verdadero espesor de cada capa, ni la temperatura, ni que el manto fluye. Un modelo bueno es el que sirve para su propósito, y un buen científico dice cuáles son sus límites.",
        "Si dos modelos dicen cosas distintas, los comparo con la evidencia. La evidencia son datos, como el espesor de cada capa, las ondas de los sismos y las rocas que salen de los volcanes. Si un modelo no concuerda con la evidencia, hay que corregirlo.",
    ],
    vocab=[("criterio", "regla o pregunta con la que comparo"), ("composición", "de qué está hecho algo"), ("rigidez", "qué tan duro y poco flexible es un material"), ("evidencia", "datos que apoyan una explicación"), ("escala", "relación entre el tamaño de un modelo y el real")],
    worked=[
        {"title": "Comparar capas", "problem": "¿Qué capa es de metal, caliente y tiene una parte líquida?", "steps": ["Es una capa metálica: el núcleo.", "Su parte externa es líquida y es la más caliente."], "answer": "El núcleo"},
        {"title": "Límite del modelo", "problem": "Un dibujo muestra la corteza tan gruesa como el manto. ¿Qué límite tiene?", "steps": ["En la realidad, la corteza mide unos 30 km y el manto unos 2.900 km.", "El dibujo no está a escala."], "answer": "No muestra el espesor real de las capas"},
    ],
    mistakes=[
        {"wrong": "Creer que un modelo es una copia exacta de la realidad.", "why": "El dibujo parece real.", "fix": "Un modelo muestra algunas ideas y deja otras fuera."},
        {"wrong": "Elegir un modelo solo porque se ve más bonito.", "why": "No se compara con evidencia.", "fix": "Elige el que concuerda con los datos."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué capa es de metal?", "El núcleo", "Su composición es hierro y níquel."),
            ex("¿Qué capa es de roca fría y rígida?", "La corteza", "Es la capa externa."),
            ex("¿Qué capa tiene roca caliente que fluye lentamente?", "El manto", "Su parte baja fluye muy lento."),
        ],
        "understand": [
            ex("¿Qué significa que un dibujo del interior de la Tierra no esté «a escala»?", "Que los tamaños no son los reales", "La escala relaciona el dibujo con el tamaño real."),
            ex("¿Qué es la evidencia en Ciencias?", "Datos que apoyan una explicación", "Sirve para comprobar un modelo."),
            ex("¿Para qué sirve comparar con criterios como composición y temperatura?", "Para ver las diferencias entre capas", "Cada criterio resalta algo distinto."),
        ],
        "apply": [
            ex("Clasifica en corteza, manto o núcleo: capa más delgada; capa de hierro y níquel; capa más gruesa.", "Corteza: más delgada. Núcleo: hierro y níquel. Manto: más gruesa", "Cada rasgo identifica una capa."),
            arith("Una escala dice que 1 cm del dibujo representa 1.000 km reales. Si el manto mide 3 cm en el dibujo, ¿cuántos km representa?", "3*1000", "Se multiplica cada cm por 1.000 km.", " km"),
            ex("Un modelo muestra el núcleo como una sola bola sólida. ¿Qué límite tiene según lo que aprendiste?", "No muestra que el núcleo externo es líquido", "Un modelo así simplifica la realidad."),
        ],
        "reason": [
            ex("Dos dibujos: A muestra la corteza muy delgada y el manto muy grueso; B los muestra de igual grosor. Con los datos reales, ¿cuál es más fiel?", "El dibujo A", "El manto es mucho más grueso que la corteza."),
            ex("Un compañero dice que el modelo de plasticina es inútil porque no es real. ¿Qué respondes?", "Sirve para mostrar el orden de las capas, aunque tenga límites", "Un modelo vale por su propósito."),
        ],
        "challenge": [
            ex("Quieres corregir un modelo que no muestra que la temperatura aumenta hacia el centro. ¿Qué agregarías?", "Una escala de colores o números de temperatura", "Así muestra el cambio de temperatura."),
            ex("Los científicos usan las ondas de los sismos para estudiar el interior. ¿Qué tipo de recurso es esa información para los modelos?", "Evidencia", "Son datos que apoyan o corrigen el modelo."),
        ],
    },
    context=[ex("Un afiche de la escuela pinta la corteza de azul. Una compañera dice que entonces la corteza es de agua. ¿Qué le respondes?", "Que la corteza es de roca y el color solo es parte del modelo", "El color de un modelo no indica la composición real.")],
    selfcheck=[
        ex("¿Qué capa es la más caliente?", "El núcleo", "Está en el centro."),
        ex("¿Qué debe decir quien usa un modelo?", "También sus límites", "Un modelo siempre simplifica."),
        ex("¿Qué apoya o corrige un modelo?", "La evidencia", "Los datos lo comprueban."),
    ],
    open_task=task(
        "Compara estos dos modelos del interior de la Tierra con los datos reales (corteza unos 30 km, manto unos 2.900 km, núcleo unos 3.470 km hasta el centro). Modelo 1: tres círculos con la corteza muy delgada. Modelo 2: tres anillos de igual grosor. Escribe cuál se parece más a la realidad, un límite de cada uno y qué evidencia usaste.",
        "El modelo 1 se parece más porque la corteza es mucho más delgada. Límite del 1: no muestra la temperatura. Límite del 2: no respeta los grosores. Evidencia: los espesores de cada capa.",
        ["elige un modelo con datos", "nombra un límite de cada modelo", "cita evidencia"],
        ["frases", "cuadro comparativo"],
        ["elegir sin usar datos", "decir que un modelo no tiene límites"],
        "Valora que use los espesores y pide agregar un límite si falta.",
    ),
    reinforce="Elige una capa y escribe cómo se llama, de qué está hecha y qué temperatura tiene.",
    extend="Piensa cómo mejorarías tu modelo de plasticina para mostrar la temperatura de cada capa.",
)

# ---------------------------------------------------------------- OA 16
register(
    OA16, 1,
    materials="Un trozo de cartón o una hoja que puedas dividir en piezas con las manos, y una regla. Las distancias de movimiento se dan escritas.",
    use="Aprenderé que la superficie de la Tierra está dividida en placas que se mueven muy lento. Sirve para explicar por qué cambia la superficie de la Tierra.",
    prior=["Sé que la Tierra tiene corteza, manto y núcleo.", "Sé que la corteza es una capa rígida y el manto fluye lentamente."],
    explain=[
        "La corteza y la parte alta del manto forman una capa rígida. Esa capa no es una sola pieza: está partida en grandes bloques llamados placas tectónicas. Piensa en un huevo cocido con la cáscara quebrada: los trozos de cáscara son las placas.",
        "Las placas se mueven sobre el manto, que fluye lentamente, y avanzan muy poco: unos pocos centímetros por año. Es tan lento que no lo sentimos. Pero en millones de años, ese movimiento cambia la posición de los continentes y forma montañas y océanos.",
        "Chile está en el borde de dos placas: la placa de Nazca, bajo el océano Pacífico, y la placa Sudamericana, donde está nuestro continente. Esas placas se encuentran frente a nuestra costa. Por eso en Chile hay muchos sismos y volcanes.",
    ],
    vocab=[("placa tectónica", "gran bloque rígido de la corteza y la parte alta del manto"), ("tectónica", "relacionada con el movimiento y la forma de la corteza"), ("continente", "gran masa de tierra"), ("borde", "lugar donde se encuentran dos placas"), ("avanzar", "moverse hacia adelante")],
    worked=[
        {"title": "Cuánto se mueve una placa", "problem": "Supón una placa que avanza 5 cm por año. ¿Cuántos cm avanza en 10 años?", "steps": ["Avanza 5 cm cada año.", "Multiplico 5 × 10."], "answer": "50 cm"},
        {"title": "Las placas de Chile", "problem": "¿Qué dos placas se encuentran frente a la costa de Chile?", "steps": ["Bajo el Pacífico está la placa de Nazca.", "Bajo el continente está la placa Sudamericana."], "answer": "Nazca y Sudamericana"},
    ],
    mistakes=[
        {"wrong": "Pensar que las placas se mueven rápido, como un auto.", "why": "Sus efectos son grandes, y se supone que son veloces.", "fix": "Se mueven unos pocos cm por año; los cambios grandes tardan millones de años."},
        {"wrong": "Creer que los continentes flotan sobre agua.", "why": "Se imagina que flotan como barcos.", "fix": "Las placas se mueven sobre el manto, que es roca que fluye muy lento."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llaman los grandes bloques en que está partida la capa rígida de la Tierra?", "Placas tectónicas", "Son bloques de corteza y parte del manto."),
            ex("¿Las placas se mueven rápido o muy lento?", "Muy lento", "Avanzan pocos cm por año."),
            ex("Completa: frente a la costa de Chile, la placa Sudamericana se encuentra con la placa de ___.", "Nazca", "La placa de Nazca está bajo el Pacífico."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es una placa tectónica?", "Un gran bloque rígido de la corteza y la parte alta del manto", "Esa es su definición."),
            ex("¿Sobre qué capa se mueven las placas?", "Sobre el manto", "El manto fluye lentamente."),
            ex("¿Por qué no sentimos que las placas se mueven?", "Porque avanzan muy poquito, unos cm al año", "El movimiento es muy lento."),
        ],
        "apply": [
            arith("Una placa avanza 4 cm por año. ¿Cuántos cm avanza en 25 años?", "4*25", "Se multiplica por los años.", " cm"),
            arith("Una placa avanza 6 cm por año. ¿Cuántos cm avanza en 100 años?", "6*100", "Se multiplica por los años.", " cm"),
            ex("Un compañero dice que frente a la costa de Chile, bajo el océano Pacífico, está la placa Sudamericana. ¿Qué le corriges?", "Bajo el Pacífico está la placa de Nazca; la Sudamericana está bajo el continente", "Son las dos placas que se encuentran frente a Chile."),
        ],
        "reason": [
            ex("Un niño dice que la Tierra es una sola pieza sólida. ¿Cómo lo corriges?", "La capa rígida está partida en placas", "Las placas son bloques."),
            ex("Dos placas se mueven 5 cm por año. Un niño dice que en un año los continentes cambian mucho. ¿Qué respondes?", "Se mueven muy poco; los cambios grandes tardan millones de años", "5 cm al año es muy lento."),
        ],
        "challenge": [
            arith("Una placa avanza 5 cm por año. ¿Cuántos centímetros avanza en 1.000 años?", "5*1000", "Se multiplica por los años.", " cm"),
            ex("5.000 cm equivalen a 50 m (1 m = 100 cm). Si una placa avanza 5.000 cm en mil años, ¿cuántos metros son?", "50 m", "5.000 ÷ 100 = 50."),
        ],
    },
    context=[ex("Ana vive en una ciudad de la costa de Chile y siente temblores a veces. Su profesor le dice que la placa de Nazca empuja a la Sudamericana. ¿Qué tienen en común las dos placas?", "Son bloques de la capa rígida que se mueven", "Ambas son placas tectónicas.")],
    selfcheck=[
        ex("¿Cómo se llaman los bloques de la capa rígida de la Tierra?", "Placas tectónicas", "Es el nombre científico."),
        ex("¿Las placas se mueven rápido?", "No, muy lento", "Pocos cm por año."),
        ex("¿Qué placa está bajo el Pacífico frente a Chile?", "La placa de Nazca", "Es la placa oceánica de esa zona."),
    ],
    open_task=task(
        "Con una hoja de papel, rómpela con las manos en cuatro trozos y júntalos como un rompecabezas: es un modelo de placas. Si no puedes, dibuja la Tierra con cuatro placas y rotula Nazca y Sudamericana. Escribe una ventaja y un límite del modelo.",
        "Modelo: papel roto en cuatro trozos. Ventaja: muestra que la capa rígida está partida. Límite: no muestra el movimiento lento ni el manto bajo las placas.",
        ["hace el modelo o dibujo", "rotula las dos placas de Chile", "ventaja y límite"],
        ["modelo o dibujo", "frase"],
        ["decir que la Tierra es una pieza entera", "no mencionar el movimiento lento"],
        "Reconoce el modelo y pide mejorar el límite si es muy general.",
    ),
    reinforce="Explica con tus palabras por qué decimos que las placas «se mueven», aunque no lo sintamos.",
    extend="Busca en un mapa del mundo cuántas placas grandes se ven y anota sus nombres.",
)

register(
    OA16, 2,
    materials="Dos libros o dos trozos de cartón y plasticina. Las situaciones se describen en el cuaderno.",
    use="Aprenderé qué ocurre cuando las placas chocan, se separan o se deslizan. Sirve para explicar por qué hay montañas, volcanes y sismos en algunos lugares.",
    prior=["Sé que la superficie de la Tierra está dividida en placas.", "Sé que las placas se mueven muy lento."],
    explain=[
        "Las placas se mueven en distintas direcciones. En el borde donde se encuentran pueden pasar tres cosas. Pueden chocar, pueden separarse o pueden deslizarse una al lado de la otra. Cada movimiento cambia la superficie de la Tierra de una manera distinta.",
        "Cuando dos placas chocan, una puede hundirse bajo la otra o se pueden levantar montañas. Frente a Chile, la placa de Nazca se hunde bajo la placa Sudamericana. Ese choque levantó la cordillera de los Andes y produce volcanes y muchos sismos.",
        "Cuando dos placas se separan, sale magma y se forma nueva corteza, como en el fondo de algunos océanos. Cuando se deslizan, se traban y luego saltan, lo que produce sismos. En todos los casos, el movimiento de las placas cambia la superficie muy despacio, durante millones de años.",
    ],
    vocab=[("chocar", "encontrarse con fuerza"), ("separarse", "alejarse una placa de otra"), ("deslizarse", "moverse una placa al lado de otra"), ("cordillera", "cadena larga de montañas"), ("hundirse", "pasar por debajo de otra cosa")],
    worked=[
        {"title": "Choque de placas", "problem": "Dos placas chocan y una se hunde bajo la otra. ¿Qué cambios en la superficie pueden pasar?", "steps": ["La presión levanta la corteza en el borde.", "Se forman montañas, volcanes y se producen sismos."], "answer": "Se forman montañas y volcanes, y hay sismos"},
        {"title": "Con plasticina", "problem": "Empujas dos barras de plasticina una contra otra sobre la mesa. ¿Qué observas en el lugar donde se juntan?", "steps": ["Las dos piezas se empujan y se juntan.", "El borde se arruga y sube."], "answer": "Se levanta y forma un relieve, como una montaña"},
    ],
    mistakes=[
        {"wrong": "Decir que los volcanes y las montañas aparecen por casualidad.", "why": "No se relacionan con las placas.", "fix": "Muchas montañas y volcanes se forman en bordes de placas."},
        {"wrong": "Pensar que solo hay sismos donde hay volcanes.", "why": "Se asocian los dos fenómenos.", "fix": "Los sismos también ocurren en bordes donde las placas se deslizan."},
    ],
    tiers={
        "recovery": [
            ex("Dos placas chocan. ¿Qué puede formarse: montañas o un mar nuevo?", "Montañas", "El choque levanta la corteza."),
            ex("¿Cómo se llama la cadena de montañas que cruza Chile de norte a sur?", "La cordillera de los Andes", "Es el relieve levantado por el choque de placas."),
            ex("Completa: cuando dos placas se ___, sale magma y se forma nueva corteza (separan o chocan).", "separan", "Al alejarse, el magma sube."),
        ],
        "understand": [
            ex("¿Cuáles son los tres movimientos posibles en el borde de dos placas?", "Chocar, separarse y deslizarse", "Son los tres tipos."),
            ex("¿Qué placa se hunde bajo cuál frente a Chile?", "La placa de Nazca bajo la placa Sudamericana", "Esa es la interacción de la zona."),
            ex("¿Por qué las placas, al deslizarse, pueden producir sismos?", "Porque se traban y luego saltan", "Ese salto libera energía."),
        ],
        "apply": [
            ex("Clasifica el movimiento: dos placas se acercan; dos placas se alejan; dos placas se rozan lado a lado.", "Chocan; se separan; se deslizan", "Cada frase describe un movimiento."),
            ex("En una zona hay una cordillera alta, volcanes en fila y muchos sismos. ¿Qué movimiento de placas explica estas tres cosas juntas?", "El choque de placas", "Ese movimiento levanta montañas, forma volcanes y produce sismos."),
            ex("Un volcán aparece cerca del borde donde una placa se hunde. ¿De dónde sale el magma?", "Del interior, bajo la corteza, donde las rocas están muy calientes", "Allí se forma el magma."),
        ],
        "reason": [
            ex("Un compañero dice que los Andes se formaron por el viento. ¿Qué explicación mejor tienes?", "Se levantaron por el choque entre la placa de Nazca y la Sudamericana", "El viento solo los desgasta."),
            ex("En un mapa, los volcanes de Chile están alineados a lo largo de la cordillera. ¿Qué indica esta línea?", "Que están cerca del borde donde chocan las placas", "El borde sigue esa dirección."),
        ],
        "challenge": [
            ex("Dos placas se alejan un par de cm al año en el fondo del océano. ¿Qué sale por la grieta que se abre?", "Magma", "Sube desde el manto y forma nueva corteza."),
            ex("Un video afirma que el movimiento de las placas «hoy mismo» puede levantar una montaña en una semana. ¿Es razonable?", "No", "Los cambios tardan millones de años."),
        ],
    },
    context=[ex("En Islandia hay una grieta enorme que se agranda unos centímetros cada año y por donde sale magma. ¿Qué movimiento de placas ocurre ahí?", "Las placas se separan", "Al separarse, sube magma y se forma nueva corteza.")],
    selfcheck=[
        ex("¿Cuántos movimientos posibles hay en el borde de dos placas?", "Tres", "Chocar, separarse y deslizarse."),
        ex("¿Qué formó el choque de la placa de Nazca con la Sudamericana?", "La cordillera de los Andes", "El choque levantó montañas."),
        ex("¿Qué sale cuando dos placas se separan?", "Magma", "Forma nueva corteza."),
    ],
    open_task=task(
        "Con dos trozos de plasticina sobre una mesa, empuja uno contra el otro y luego aléjalos. Si no puedes, usa esta descripción: al empujar, el borde se arruga y sube; al alejar, queda un hueco. Dibuja y rotula tres movimientos de placas (chocar, separarse y deslizarse) y escribe un efecto de cada uno en la superficie.",
        "Chocar: se levantan montañas y volcanes. Separarse: sale magma y se forma nueva corteza. Deslizarse: se acumula esfuerzo y se producen sismos.",
        ["tres movimientos rotulados", "un efecto por cada uno", "relación con las placas de Chile"],
        ["tres dibujos", "tres frases"],
        ["confundir chocar con separarse", "no relacionar con la superficie"],
        "Valora los tres dibujos y pide corregir cualquier efecto confundido.",
    ),
    reinforce="Mira un mapa de Chile y anota dónde está la cordillera de los Andes.",
    extend="Averigua qué es la fosa marina que se forma cuando una placa se hunde bajo otra.",
)

register(
    OA16, 3,
    materials="Una bandeja con arena seca y un vaso con agua baja, o los dibujos descritos en el cuaderno. Trabaja con cuidado y sin llenar mucho el agua.",
    use="Aprenderé qué es un sismo y un tsunami y cómo se relacionan con las placas. Sirve para entender por qué ocurren en Chile y qué cambian en la superficie.",
    prior=["Sé que las placas se mueven y se traban.", "Sé que la placa de Nazca se hunde bajo la Sudamericana."],
    explain=[
        "Un sismo es un temblor de la tierra. Ocurre cuando las placas, que llevaban tiempo trabadas, se sueltan de golpe y liberan energía. Esa energía viaja como ondas por la corteza y hace temblar el suelo. El lugar bajo tierra donde empieza el sismo se llama foco. El punto de la superficie que queda justo sobre el foco se llama epicentro. Mientras más lejos del epicentro, más débil se siente el sismo.",
        "Un tsunami es una serie de olas muy grandes que se forman cuando el fondo del mar se mueve de golpe, por ejemplo, en un sismo grande bajo el océano. El agua se desplaza y las olas viajan hasta la costa. Pueden llegar minutos u horas después del sismo.",
        "Los sismos y los tsunamis cambian la superficie. Un sismo puede agrietar el suelo, hacer caer cerros o levantar la costa. Un tsunami puede inundar la costa, arrastrar arena y cambiar la playa. Por eso es importante saber qué hacer, lo que veremos en la unidad de prevención.",
    ],
    vocab=[("sismo", "temblor de la tierra"), ("epicentro", "punto de la superficie sobre el lugar donde se origina el sismo"), ("tsunami", "serie de olas muy grandes causadas por el movimiento del fondo del mar"), ("energía", "capacidad de producir cambios o movimiento"), ("onda", "movimiento que se propaga")],
    worked=[
        {"title": "Causa de un sismo", "problem": "¿Por qué ocurre un sismo?", "steps": ["Las placas se traban y acumulan esfuerzo.", "Se sueltan de golpe y liberan energía como ondas."], "answer": "Porque las placas se sueltan de golpe y liberan energía"},
        {"title": "Cómo se forma un tsunami", "problem": "Un sismo mueve el fondo del mar frente a la costa. ¿Qué puede pasar con el agua?", "steps": ["El fondo del mar se mueve de golpe.", "Empuja el agua y se forman olas muy grandes."], "answer": "Se puede formar un tsunami"},
    ],
    mistakes=[
        {"wrong": "Decir que el tsunami es lo mismo que una ola grande de tormenta.", "why": "Ambos son olas.", "fix": "El tsunami nace por el movimiento del fondo del mar, no por el viento."},
        {"wrong": "Pensar que el epicentro es el lugar donde empieza el sismo bajo tierra.", "why": "Se confunde con el foco.", "fix": "El epicentro está en la superficie, justo sobre el origen del sismo."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es un sismo?", "Un temblor de la tierra", "Es el movimiento del suelo."),
            ex("¿Un tsunami se forma por el viento o por el movimiento del fondo del mar?", "Por el movimiento del fondo del mar", "No lo causa el viento."),
            ex("Completa: el ___ es el punto de la superficie sobre el origen del sismo (epicentro o cráter).", "epicentro", "Está sobre el origen del sismo."),
        ],
        "understand": [
            ex("¿Qué libera un sismo cuando las placas se sueltan de golpe?", "Energía", "Viaja como ondas por la corteza."),
            ex("¿Por qué ocurren muchos sismos en Chile?", "Porque la placa de Nazca y la Sudamericana se encuentran", "Su choque acumula y libera energía."),
            ex("¿Por qué un sismo grande bajo el mar puede producir un tsunami?", "Porque mueve el fondo del mar y el agua", "Ese movimiento empuja el agua."),
        ],
        "apply": [
            ex("Clasifica como sismo o tsunami: suelo que tiembla; olas muy grandes que llegan a la costa.", "Suelo que tiembla: sismo. Olas muy grandes: tsunami", "Cada fenómeno afecta un medio distinto."),
            ex("Un sismo ocurre bajo el océano a 100 km de la costa. ¿Qué otro fenómeno puede producir?", "Un tsunami", "Mueve el fondo del mar."),
            arith("Un sismo ocurre a las 15:10 y las olas de un tsunami llegan a la costa a las 15:55. ¿Cuántos minutos pasaron entre ambos hechos?", "55-10", "Se restan los minutos de las dos horas.", " minutos"),
        ],
        "reason": [
            ex("Una niña dice que si tiembla mucho en una ciudad costera hay que alejarse del mar. ¿Qué fenómeno justifica su advertencia?", "El posible tsunami", "Un sismo fuerte puede mover el fondo del mar."),
            ex("Dos amigos discuten: uno dice que el epicentro está bajo tierra y el otro que está en la superficie. ¿Quién tiene razón?", "El que dice que está en la superficie", "El epicentro está sobre el origen del sismo."),
        ],
        "challenge": [
            ex("Dos sismos de la misma energía tienen su epicentro a distinta distancia de una ciudad: A a 10 km y B a 300 km. ¿Cuál esperas que se sienta más fuerte en la ciudad?", "El sismo A, con epicentro a 10 km", "Las ondas se debilitan al viajar más lejos."),
            ex("Un tsunami llega a la costa y deja un tronco en la arena. ¿Qué cambio de la superficie muestra esto?", "Que el agua llegó más arriba de la playa", "El mar avanzó sobre la tierra."),
        ],
    },
    context=[ex("En la costa del centro de Chile, el 2010 hubo un sismo muy grande seguido de olas. Con lo aprendido, ¿qué relación hay entre el sismo y las olas?", "El sismo movió el fondo del mar y produjo las olas", "Ese movimiento causa el tsunami.")],
    selfcheck=[
        ex("¿Qué libera un sismo?", "Energía", "Por eso hace temblar el suelo."),
        ex("¿Qué causa un tsunami?", "El movimiento del fondo del mar", "Empuja el agua."),
        ex("¿Dónde está el epicentro?", "En la superficie, sobre el origen del sismo", "Es el punto de arriba."),
    ],
    open_task=task(
        "En una bandeja con arena y agua baja (o en un dibujo), imagina que el fondo se levanta de golpe: ¿qué pasa con el agua? Si no puedes hacer el modelo, dibuja el fondo del mar, la costa y una flecha de olas. Escribe con tus palabras cómo se forma un tsunami y qué límite tiene tu modelo.",
        "Si el fondo se levanta de golpe, empuja el agua y se forman olas hacia la costa. Límite: un tsunami real mueve muchísima más agua y viaja cientos de kilómetros.",
        ["explica la causa", "usa el movimiento del fondo", "señala un límite del modelo"],
        ["dibujo o foto", "frase explicativa"],
        ["decir que el viento causa el tsunami", "no mencionar el movimiento del fondo"],
        "Valora la explicación causal y pide completar el límite del modelo.",
    ),
    reinforce="Escribe con tus palabras la diferencia entre sismo y tsunami.",
    extend="Averigua qué significa «zona de evacuación por tsunami» en una ciudad costera de Chile.",
)

register(
    OA16, 4,
    materials="Papel y lápices de colores. Usa los dibujos y datos del cuaderno; no se necesitan materiales especiales.",
    use="Aprenderé cómo se producen las erupciones volcánicas y a resumir con un modelo los cambios de la superficie. Sirve para explicar los volcanes de Chile y evaluar un modelo.",
    prior=["Sé que el magma es roca derretida bajo la superficie.", "Sé que hay volcanes cerca de los bordes de placas."],
    explain=[
        "Un volcán es una abertura de la corteza por la que sale magma desde el interior. Cuando el magma sube y sale, ocurre una erupción. El magma que sale se llama lava; también salen gases y cenizas, que son trocitos muy pequeños de roca.",
        "Muchos volcanes se forman donde una placa se hunde bajo otra, como en Chile. La placa que se hunde se calienta, se forma magma y este sube por grietas hasta la superficie. Con muchas erupciones, la lava y la ceniza se acumulan y forman una montaña en forma de cono.",
        "Un modelo puede ser un dibujo con las capas, una placa que se hunde y un volcán. Sirve para mostrar el origen del magma, pero tiene límites: no muestra el tamaño real ni el tiempo tan largo que tardan estos cambios. En Chile hay muchos volcanes, por ejemplo el Villarrica, y el movimiento de las placas cambia la superficie hace millones de años.",
    ],
    vocab=[("volcán", "abertura de la corteza por donde sale magma"), ("erupción", "salida de lava, gases y ceniza de un volcán"), ("ceniza volcánica", "trocitos muy pequeños de roca que expulsa un volcán"), ("cono", "forma de montaña con la punta arriba"), ("cráter", "hueco en la cima del volcán")],
    worked=[
        {"title": "Camino del magma", "problem": "Ordena: el magma sale por el cráter; la placa se hunde y se calienta; el magma sube por grietas.", "steps": ["Primero, la placa se hunde y se calienta.", "Luego el magma sube por grietas.", "Por último, sale por el cráter."], "answer": "Placa se hunde, magma sube por grietas, sale por el cráter"},
        {"title": "Cambio lento", "problem": "Supón que un volcán crece 2 cm cada año con sus erupciones. ¿Cuánto crece en 50 años?", "steps": ["Crece 2 cm por año.", "Multiplico 2 × 50."], "answer": "100 cm"},
    ],
    mistakes=[
        {"wrong": "Pensar que un volcán es una montaña con fuego dentro.", "why": "Se imagina un fuego como el de una chimenea.", "fix": "El magma es roca derretida muy caliente, no es fuego."},
        {"wrong": "Creer que un modelo de volcán de la escuela muestra la erupción real.", "why": "Parece completo.", "fix": "El modelo explica el origen del magma, pero no su tamaño ni su duración reales."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llama la roca derretida que sale de un volcán?", "Lava", "Antes de salir se llama magma."),
            ex("¿Cómo se llama la salida de lava y gases de un volcán?", "Erupción", "Es la actividad del volcán."),
            ex("Completa: la ___ volcánica son trocitos muy pequeños de roca (ceniza o arena).", "ceniza", "La expulsa el volcán."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es un volcán?", "Una abertura de la corteza por donde sale magma", "Esa es la definición."),
            ex("¿Por qué hay muchos volcanes en Chile?", "Porque una placa se hunde bajo otra", "Eso produce magma que sube."),
            ex("¿Cómo se forma el cono de un volcán?", "Con la lava y la ceniza que se acumulan", "Las erupciones construyen la montaña."),
        ],
        "apply": [
            arith("Supón que un volcán crece 3 cm cada año. ¿Cuántos cm crece en 40 años?", "3*40", "Se multiplica por los años.", " cm"),
            ex("Clasifica como sismo, tsunami o erupción: suelo que tiembla; olas del mar; salida de lava.", "Sismo; tsunami; erupción", "Cada frase describe un fenómeno distinto."),
            ex("Una placa se hunde bajo otra y el magma sube por grietas. ¿Qué forma de relieve puede aparecer?", "Un volcán", "El magma que sale forma el cono."),
        ],
        "reason": [
            ex("Un niño dice: «los volcanes son fuego que sale de la tierra». ¿Cómo lo corriges?", "Lo que sale es roca derretida, el magma o lava", "El magma está caliente, pero no es fuego."),
            ex("Un afiche muestra un volcán y las capas de la Tierra, pero dibuja la corteza tan gruesa como el manto. ¿Qué límite tiene?", "No respeta los grosores reales", "No está a escala."),
        ],
        "challenge": [
            ex("Haz un resumen: ¿qué tienen en común sismos, tsunamis y erupciones respecto a las placas?", "Todos se relacionan con el movimiento de las placas", "Ocurren por la interacción de las placas."),
            ex("Una compañera afirma que la superficie de la Tierra siempre ha sido igual. ¿Qué dos ejemplos de cambio puedes dar?", "Montañas que se levantan y volcanes que crecen", "Son cambios por el movimiento de las placas."),
        ],
    },
    context=[ex("Mientras viaja al sur, Pedro ve el volcán Villarrica con un cono perfecto. ¿Qué material acumulado de erupciones pasadas forma ese cono?", "Lava y ceniza", "Las erupciones apilan esos materiales.")],
    selfcheck=[
        ex("¿Qué sale de un volcán en una erupción?", "Lava, gases y ceniza", "Son sus productos."),
        ex("¿Dónde se origina el magma?", "En el interior de la Tierra, bajo la corteza", "Allí las rocas están muy calientes."),
        ex("¿Qué fenómenos del movimiento de placas estudiamos?", "Sismos, tsunamis y erupciones", "Son los tres cambios de la unidad."),
    ],
    open_task=task(
        "Dibuja un corte de la Tierra con la placa de Nazca hundiéndose bajo la Sudamericana, el camino del magma y un volcán. Rotula las placas, el magma, el cráter y la ceniza. Agrega una ventaja y un límite de tu dibujo como modelo, y escribe una frase que una el movimiento de placas con sismos, tsunamis y volcanes.",
        "Ventaja: muestra de dónde sale el magma. Límite: no está a escala y no muestra el tiempo. Frase: el movimiento de las placas produce sismos, puede provocar tsunamis y alimenta los volcanes.",
        ["rótulos correctos", "ventaja y límite", "frase que une los tres fenómenos"],
        ["dibujo", "frase"],
        ["decir que el magma es fuego", "no unir con las placas"],
        "Valora el dibujo claro y pide completar la frase si falta algún fenómeno.",
    ),
    reinforce="Haz una tabla de tres columnas (sismo, tsunami, erupción) y escribe una causa y un efecto en cada una.",
    extend="Averigua el nombre de otro volcán de Chile y en qué región se encuentra.",
)
