"""Student material for 3.º básico Matemática, OA 18 (ángulos con referentes de 45° y 90°)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA18 = "MA03 OA 18"

REF = "Referentes: la esquina de una hoja de cuaderno mide 90°; si doblas esa esquina por la mitad, cada parte mide 45°."
ANG = "Ángulo A: cabe justo en la esquina de una hoja. Ángulo B: es la mitad de esa esquina. Ángulo C: es claramente más abierto que la mitad de la esquina y claramente más cerrado que toda la esquina. Ángulo D: sobrepasa la esquina de la hoja."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA18, 1,
    materials="Lápiz, papel y, si quieres, unas tijeras de juguete o dos lápices para formar ángulos. Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé qué es un ángulo y dónde se encuentran ángulos en los giros. Sirve para describir cuánto se abre o cuánto gira algo.",
    prior=["Sé qué es un cuarto de vuelta y una media vuelta.", "Sé decir izquierda, derecha, arriba y abajo."],
    explain=[
        "Un ángulo se forma cuando dos líneas parten del mismo punto. Las líneas se llaman lados y el punto donde se juntan se llama vértice. El ángulo es la abertura entre los dos lados. Si abres unas tijeras, entre las dos hojas hay un ángulo.",
        "Un ángulo también aparece cuando algo gira. Si la aguja de un reloj parte en el 12 y gira hasta el 3, entre su posición inicial y la final se forma un ángulo. Mientras más gira, mayor es el ángulo.",
        "Lo que importa es la abertura y no el largo de los lados. Unas tijeras grandes y unas pequeñas, abiertas igual, forman el mismo ángulo. Para comparar dos ángulos, compara cuánto se abren, no qué tan largos son los lados.",
    ],
    vocab=[("ángulo", "abertura entre dos líneas que parten del mismo punto"), ("lado", "cada una de las dos líneas de un ángulo"), ("vértice", "punto donde se juntan los dos lados"), ("abertura", "cuánto se separan los lados"), ("giro", "movimiento de dar vueltas alrededor de un punto")],
    worked=[
        {"title": "Partes de un ángulo", "problem": "Unas tijeras se abren. ¿Cuál es el vértice del ángulo y cuáles son sus lados?", "steps": ["El vértice es el punto donde se juntan las dos hojas, el tornillo.", "Los lados son las dos hojas."], "answer": "El vértice es el tornillo y los lados son las hojas"},
        {"title": "Comparar ángulos", "problem": "Unas tijeras grandes y unas pequeñas están abiertas de igual manera. ¿Cuál forma el mayor ángulo?", "steps": ["Comparo la abertura, no el largo de las hojas.", "Las dos se abren igual.", "Los dos ángulos son iguales."], "answer": "Ninguna; forman el mismo ángulo"},
    ],
    mistakes=[
        {"wrong": "Decir que el ángulo de unas tijeras grandes es mayor porque sus hojas son más largas.", "why": "Se compara el largo de los lados.", "fix": "El ángulo es la abertura; si se abren igual, los ángulos son iguales."},
        {"wrong": "Decir que el vértice de un ángulo es uno de sus lados.", "why": "Se confunden el punto y las líneas.", "fix": "El vértice es el punto donde se juntan los dos lados."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llaman las dos líneas que forman un ángulo?", "Lados", "Son las líneas que parten del vértice."),
            ex("¿Cómo se llama el punto donde se juntan los lados de un ángulo?", "Vértice", "Es el punto de partida de los dos lados."),
            ex("Un ángulo, ¿mide la abertura entre los lados o el largo de los lados?", "La abertura entre los lados", "El largo no cambia el ángulo."),
        ],
        "understand": [
            ex("Un abanico grande y uno pequeño están abiertos igual. ¿Tienen el mismo ángulo?", "Sí", "La abertura es la misma."),
            ex("Una puerta se abre apenas y otra se abre mucho. ¿Cuál forma el mayor ángulo?", "La que se abre mucho", "Mayor abertura es mayor ángulo."),
            ex("La aguja de un reloj gira de una posición a otra. ¿Se forma un ángulo entre ambas posiciones?", "Sí", "Los dos lados son las posiciones inicial y final de la aguja."),
        ],
        "apply": [
            ex("¿Cuál muestra un ángulo: una pelota, unas tijeras abiertas o una moneda?", "Unas tijeras abiertas", "Tienen dos lados que parten de un punto."),
            ex("Una aguja de reloj parte en el 12 y llega al 3. ¿Giró un cuarto de vuelta o media vuelta?", "Un cuarto de vuelta", "Del 12 al 3 hay una cuarta parte del reloj."),
            ex("Al abrir un computador portátil, la pantalla y el teclado forman un ángulo. ¿Dónde está el vértice?", "En la bisagra, donde se juntan", "Allí parten los dos lados."),
        ],
        "reason": [
            ex("Luis dice que un caballete alto y uno bajo, abiertos igual, tienen ángulos distintos porque uno es más largo. ¿Qué error comete?", "Compara el largo de los lados y no la abertura", "El ángulo depende de la abertura."),
            ex("Un ángulo A tiene lados de 3 cm y otro ángulo B tiene lados de 10 cm, pero ambos se abren igual. ¿Cuál es mayor?", "Ninguno; son iguales", "Tienen la misma abertura."),
        ],
        "challenge": [
            ex("Tres agujas de reloj parten del 12. La aguja A llega al 1, la B llega al 3 y la C llega al 2. Ordena sus giros de menor a mayor.", "A, C, B", "Del 12 al 1 es menos que al 2, y al 2 es menos que al 3."),
            ex("Un cuarto de vuelta forma el mismo ángulo que la esquina de una hoja. ¿Verdadero o falso?", "Verdadero", "La esquina de una hoja es un cuarto de vuelta."),
        ],
    },
    context=[ex("Un abanico de papel se abre. ¿Dónde están los lados del ángulo que forma el abanico abierto?", "En las dos varillas de los extremos", "Los lados salen del punto donde se juntan las varillas.")],
    selfcheck=[
        ex("En unas tijeras abiertas, ¿el tornillo que une las hojas es el vértice o un lado del ángulo?", "El vértice", "Es el punto donde se juntan las hojas."),
        ex("Dos ángulos tienen la misma abertura, pero uno tiene lados más largos. ¿Son iguales?", "Sí", "El largo no cambia el ángulo."),
        ex("La aguja de un reloj gira más. ¿El ángulo se hace mayor o menor?", "Mayor", "A más giro, más abertura."),
    ],
    open_task=task(
        "Con dos lápices o dos palitos unidos por un extremo, forma tres ángulos: uno poco abierto, uno medio y uno muy abierto. Dibuja cada ángulo, marca su vértice con un punto y escribe cuál es el menor y cuál es el mayor. Luego prueba con lápices más largos y di si cambia el ángulo.",
        "Ángulo 1: poco abierto (el menor). Ángulo 2: medio. Ángulo 3: muy abierto (el mayor). Con lápices más largos, si los abro igual, el ángulo es el mismo.",
        ["dibuja tres ángulos distintos", "marca el vértice", "ordena de menor a mayor", "explica que el largo no cambia el ángulo"],
        ["tres dibujos", "orden escrito", "explicación"],
        ["comparar el largo de los lados", "olvidar el vértice"],
        "Pide que muestre con los lápices que el ángulo no cambia al alargar los lados. Reconoce la comparación por abertura.",
    ),
    reinforce="Abre y cierra una puerta o unas tijeras y di cuándo el ángulo es mayor y cuándo es menor.",
    extend="Busca cinco ángulos en tu casa, como la esquina de un libro o un abanico, y dibuja cada uno marcando su vértice.",
)

register(
    OA18, 2,
    materials="Una hoja de papel cualquiera (de cuaderno, de diario o de revista), lápiz. Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé a construir un referente de 90° doblando una hoja. Sirve para comparar otros ángulos con él cuando no tengo transportador.",
    prior=["Sé qué es un ángulo y sus partes.", "Sé qué es un cuarto de vuelta."],
    explain=[
        "Un ángulo de 90° es una esquina como la de una hoja de cuaderno o de un libro. Se llama ángulo recto. También es un cuarto de vuelta: cuatro ángulos de 90° completan una vuelta entera. El símbolo ° se lee grados.",
        "Puedes fabricar un ángulo de 90° con cualquier papel. Dobla el papel por la mitad. Luego dobla de nuevo, haciendo que el borde doblado coincida consigo mismo. Al abrir, los dos dobleces se cruzan y forman cuatro ángulos iguales de 90°. Uno de ellos sirve como referente.",
        "Para comparar un ángulo con el referente, pon el vértice del referente sobre el vértice del ángulo y un lado sobre el otro. Si el otro lado queda justo, el ángulo mide 90°. Si queda dentro del referente, mide menos de 90°. Si el referente queda dentro del ángulo, mide más de 90°.",
    ],
    vocab=[("grados (°)", "unidad con que se mide un ángulo"), ("ángulo recto", "ángulo de 90°, como la esquina de una hoja"), ("referente", "ángulo conocido que sirve para comparar"), ("coincidir", "quedar justo encima, sin sobrar ni faltar"), ("cuarto de vuelta", "giro que forma un ángulo de 90°")],
    worked=[
        {"title": "Construir el referente", "problem": "Describe cómo fabricar un ángulo de 90° con una hoja cualquiera.", "steps": ["Doblo la hoja por la mitad, formando un borde recto.", "Doblo otra vez, haciendo que el borde doblado coincida consigo mismo.", "Abro: los dos dobleces se cruzan y forman ángulos de 90°."], "answer": "Dos dobleces; donde se cruzan forman ángulos de 90°"},
        {"title": "Comparar con el referente", "problem": "Un ángulo se coloca sobre mi referente de 90° y un lado queda dentro del referente. ¿Mide más o menos de 90°?", "steps": ["Si un lado queda dentro del referente, el ángulo es más cerrado.", "Más cerrado que 90° significa menor que 90°."], "answer": "Menos de 90°"},
    ],
    mistakes=[
        {"wrong": "Decir que un ángulo mide 90° porque sus lados son largos.", "why": "Se mira el largo de los lados.", "fix": "Compara con el referente de 90°: si los lados coinciden, mide 90°."},
        {"wrong": "Doblar la hoja una sola vez y decir que ya tiene un ángulo de 90°.", "why": "Un doblez forma un borde recto, no una esquina.", "fix": "Hace falta el segundo doblez que coincida consigo mismo."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuánto mide el ángulo de la esquina de una hoja de cuaderno?", "90°", "Es un ángulo recto."),
            ex("¿Cuántos ángulos de 90° tiene un cuadrado en total?", "4", "Un cuadrado tiene 4 esquinas rectas."),
            ex("¿Cuántos dobleces necesitas para fabricar un ángulo de 90° con una hoja?", "2", "El primero hace un borde recto y el segundo forma la esquina."),
        ],
        "understand": [
            ex("¿Para qué sirve un referente de 90°?", "Para comparar otros ángulos con él", "Se mide por comparación."),
            ex("Un ángulo es más cerrado que el referente de 90°. ¿Mide más o menos de 90°?", "Menos", "Más cerrado es menor."),
            ex("Un cuarto de vuelta, ¿cuántos grados forma?", "90°", "Un cuarto de vuelta es un ángulo recto."),
        ],
        "apply": [
            ex("Pones un ángulo sobre tu referente y coincide justo. ¿Cuánto mide?", "90°", "Coincide con el ángulo recto."),
            ex("Pones un ángulo sobre tu referente y sus lados quedan dentro del referente. ¿Mide más o menos de 90°?", "Menos de 90°", "Es más cerrado."),
            ex("Pones un ángulo sobre tu referente y el referente queda dentro del ángulo. ¿Mide más o menos de 90°?", "Más de 90°", "Es más abierto."),
        ],
        "reason": [
            ex("Rita dice que su ángulo mide 90° porque sus lados son muy largos. ¿Qué error comete?", "Mira el largo y no la abertura; debe compararlo con el referente", "El largo no cambia el ángulo."),
            ex("Sofía dobló una hoja una sola vez y dice que tiene un ángulo de 90°. ¿Qué le falta?", "El segundo doblez, que coincida consigo mismo", "Un doblez da un borde recto, no una esquina."),
        ],
        "challenge": [
            ex("¿Cuántos ángulos de 90° completan una vuelta entera?", "4", "Cuatro cuartos de vuelta hacen una vuelta."),
            ex("Una aguja de reloj gira desde el 12 hasta el 6, pasando por el 3. ¿Cuántos ángulos de 90° recorrió?", "2", "Del 12 al 3 es uno y del 3 al 6 es otro."),
        ],
    },
    context=[ex("La esquina de una ventana cuadrada se compara con el referente de 90° y coincide. ¿Cuánto mide el ángulo de esa esquina?", "90°", "Coincide con el ángulo recto.")],
    selfcheck=[
        ex("¿Cuántos grados mide un ángulo recto?", "90°", "Así se define."),
        ex("¿Es correcto fabricar un referente de 90° con cualquier hoja?", "Sí", "Los dos dobleces siempre dan una esquina recta."),
        ex("Si un ángulo sobrepasa a tu referente, ¿mide más o menos de 90°?", "Más", "Es más abierto."),
    ],
    open_task=task(
        "Fabrica tu referente de 90° con una hoja: dobla por la mitad y luego dobla de nuevo haciendo coincidir el borde consigo mismo. Úsalo para clasificar cuatro ángulos de tu casa (esquina de un libro, esquina de una mesa, unas tijeras poco abiertas y una puerta muy abierta): escribe si miden 90°, menos de 90° o más de 90°.",
        "Esquina del libro: 90°. Esquina de la mesa: 90°. Tijeras abiertas poco: menos de 90°. Puerta muy abierta: más de 90°. Usé mi referente doblado.",
        ["fabrica el referente con dos dobleces", "compara con el vértice sobre el vértice", "clasifica cuatro ángulos", "explica cómo decidió"],
        ["referente de papel", "lista de cuatro ángulos"],
        ["comparar el largo de los lados", "olvidar poner vértice con vértice"],
        "Pide que muestre cómo pone vértice sobre vértice. Reconoce que clasifique con el referente.",
    ),
    reinforce="Con tu referente, busca tres esquinas en tu casa que midan 90° y una que no.",
    extend="Con tu referente, compara el ángulo de una puerta cuando está abierta. ¿Más o menos de 90°?",
)

register(
    OA18, 3,
    materials=f"Tu referente de 90° hecho con una hoja y lápiz. {REF}",
    use="Aprenderé a estimar la medida de un ángulo con los referentes de 45° y de 90°. Sirve para decir cuánto mide un ángulo sin medirlo con exactitud.",
    prior=["Sé que un ángulo recto mide 90°.", "Sé comparar un ángulo con un referente."],
    explain=[
        "Estimar es decir una medida cercana, sin medir con exactitud. Para estimar un ángulo usamos dos referentes: 90° y 45°. " + REF + " Para hacer el referente de 45°, dobla la esquina de modo que un lado quede justo sobre el otro: el doblez parte el ángulo en dos partes iguales. Cada parte mide 90 ÷ 2 = 45°.",
        "Compara el ángulo con los referentes. Si es casi como la mitad de la esquina, estima 45°. Si es casi como la esquina, estima 90°. Si es más cerrado que 45°, mide menos de 45°. Si está entre los dos, mide entre 45° y 90°. Si se abre más que la esquina, mide más de 90°.",
        "Una buena estimación se explica con el referente: «mide cerca de 45° porque ocupa la mitad de la esquina de la hoja». No se necesita ser exacto, solo cercano.",
    ],
    vocab=[("estimar", "decir una medida cercana sin medir con exactitud"), ("45°", "medida de la mitad de un ángulo recto"), ("90°", "medida de un ángulo recto"), ("entre 45° y 90°", "más abierto que 45° y más cerrado que 90°"), ("referente", "medida conocida que sirve para comparar")],
    worked=[
        {"title": "La mitad del ángulo recto", "problem": "Doblas por la mitad la esquina de una hoja. ¿Cuánto mide cada parte?", "steps": ["La esquina mide 90°.", "La mitad de 90 es 45.", "Cada parte mide 45°."], "answer": "45°"},
        {"title": "Estimar un ángulo", "problem": "Un ángulo ocupa más o menos la mitad de la esquina de una hoja. ¿Qué medida estimas?", "steps": ["La esquina entera mide 90°.", "La mitad de la esquina mide 45°.", "Estimo cerca de 45°."], "answer": "Cerca de 45°"},
    ],
    mistakes=[
        {"wrong": "Estimar 90° para un ángulo que ocupa la mitad de la esquina.", "why": "No se compara con la mitad del referente.", "fix": "La mitad de 90° es 45°: estima 45°."},
        {"wrong": "Pensar que estimar es medir con exactitud.", "why": "Se confunde estimar con medir.", "fix": "Estimar es acercarse con ayuda de los referentes."},
    ],
    tiers={
        "recovery": [
            arith("¿Cuánto mide la mitad de un ángulo de 90°?", "90//2", "Se divide 90 en dos partes iguales.", "°"),
            ex("¿Cuántos ángulos de 45° forman un ángulo de 90°?", "2", "Dos mitades forman un entero."),
            ex("Un ángulo coincide justo con tu referente de 45°. ¿Cuánto estimas que mide?", "45°", "Coincide con el referente de 45°."),
        ],
        "understand": [
            ex("Un ángulo es más cerrado que 45°. ¿Mide más o menos de 45°?", "Menos de 45°", "Más cerrado es menor."),
            ex("Un ángulo es más abierto que la esquina de una hoja. ¿Mide más o menos de 90°?", "Más de 90°", "Más abierto es mayor."),
            ex("Para estimar un ángulo, ¿con qué referentes lo comparas?", "Con 45° y con 90°", "Son los dos referentes que tenemos."),
        ],
        "apply": [
            ex("Un ángulo ocupa más o menos la mitad de la esquina de una hoja. ¿Qué estimas: 20°, 45° o 90°?", "45°", "La mitad de 90° es 45°."),
            arith("Pones dos ángulos de 45° juntos. ¿Cuánto mide el ángulo que forman?", "45+45", "Se suman las dos aberturas.", "°"),
            ex("Un ángulo es un poco menor que la esquina de una hoja. ¿Qué estimación es mejor: 10°, 80° o 150°?", "80°", "Es cercano a 90° pero un poco menor."),
        ],
        "reason": [
            ex("Pablo estima 90° para un ángulo que ocupa la mitad de la esquina de una hoja. ¿Qué error comete y qué debería estimar?", "No usa la mitad del referente; debería estimar 45°", "La mitad de 90° es 45°."),
            ex("Ana dice que estimar es medir con exactitud. ¿Tiene razón?", "No; estimar es acercarse con ayuda de referentes", "No se necesita un valor exacto."),
        ],
        "challenge": [
            ex("Un ángulo es mayor que 45° y menor que 90°. ¿Cuál puede ser su medida: 30°, 60° o 120°?", "60°", "60 es mayor que 45 y menor que 90."),
            arith("¿Cuántos ángulos de 45° se necesitan para completar una vuelta entera? Una vuelta tiene 4 ángulos de 90°.", "4*2", "Cada ángulo de 90° tiene 2 de 45°.", " ángulos"),
        ],
    },
    context=[ex("Un abanico se abre hasta formar un ángulo que ocupa la mitad de la esquina de una hoja. ¿Qué medida estimas?", "Cerca de 45°", "Es la mitad de 90°.")],
    selfcheck=[
        arith("¿Cuánto mide el doble de un ángulo de 45°?", "45*2", "Dos ángulos de 45° juntos forman un ángulo recto.", "°"),
        ex("Un ángulo coincide con la esquina de una hoja. ¿Qué estimas?", "90°", "Es un ángulo recto."),
        ex("Un ángulo es más abierto que 45° y más cerrado que 90°. ¿Mide más o menos de 45°?", "Más de 45°", "Está entre 45° y 90°."),
    ],
    open_task=task(
        "Con tu referente de 90°, dóblalo por la mitad para fabricar el referente de 45°. Dibuja tres ángulos distintos (uno cerca de 45°, uno cerca de 90° y uno entre 45° y 90°) y estima su medida. Escribe cómo lo decidiste con los referentes.",
        "Ángulo 1: cerca de 45°, porque coincide con mi referente de 45°. Ángulo 2: cerca de 90°, porque coincide con la esquina de la hoja. Ángulo 3: entre 45° y 90°, porque es más abierto que 45° y más cerrado que 90°.",
        ["fabrica los dos referentes", "dibuja tres ángulos distintos", "estima con los referentes", "explica cada decisión"],
        ["referentes de papel", "tres dibujos", "estimaciones"],
        ["estimar sin comparar", "confundir 45° con 90°"],
        "Pide que ponga los referentes sobre sus ángulos. Reconoce la explicación con el referente.",
    ),
    reinforce="Dobla una hoja para ver 90° y 45°. Abre las tijeras hasta formar cerca de 45° y luego cerca de 90°.",
    extend="Estima el ángulo que forma una puerta cuando la abres hasta la mitad de una esquina. Explica con tus referentes.",
)

register(
    OA18, 4,
    materials=f"Tu referente de 90° y el de 45° hechos con una hoja, y lápiz. {REF} {ANG}",
    use="Aprenderé a clasificar ángulos del entorno usando los referentes de 45° y 90°. Sirve para describir ángulos que encuentro en mi casa o en la calle.",
    prior=["Sé qué es un ángulo y sus partes.", "Sé estimar ángulos con 45° y 90°."],
    explain=[
        "Clasificar ángulos es ordenarlos en grupos según su medida. Con los referentes de 45° y 90° tenemos cinco grupos: menor que 45°, cerca de 45°, entre 45° y 90°, cerca de 90° y mayor que 90°.",
        "Para decidir, pon el vértice del ángulo sobre el vértice de tu referente. Si el ángulo coincide con el de 45°, está en «cerca de 45°». Si coincide con el de 90°, está en «cerca de 90°». Si queda entre los dos, está en «entre 45° y 90°». Si es más cerrado que el de 45°, es menor que 45°. Si sobrepasa el de 90°, es mayor que 90°.",
        "En el entorno hay muchos ángulos: la esquina de un libro (90°), las agujas de un reloj, un abanico, una puerta entreabierta, las patas de un caballete. Cada uno cae en uno de los cinco grupos.",
    ],
    vocab=[("clasificar", "agrupar según una propiedad"), ("menor que 45°", "más cerrado que el referente de 45°"), ("entre 45° y 90°", "más abierto que 45° y más cerrado que 90°"), ("mayor que 90°", "más abierto que la esquina de una hoja"), ("entorno", "lo que nos rodea")],
    worked=[
        {"title": "Clasificar con los referentes", "problem": f"{ANG} ¿En qué grupo cae el ángulo A?", "steps": ["El ángulo A cabe justo en la esquina de la hoja.", "La esquina de la hoja mide 90°.", "Cae en «cerca de 90°»."], "answer": "Cerca de 90°"},
        {"title": "Ángulo más abierto que la esquina", "problem": f"{ANG} ¿En qué grupo cae el ángulo D?", "steps": ["D sobrepasa la esquina de la hoja.", "Es más abierto que 90°.", "Cae en «mayor que 90°»."], "answer": "Mayor que 90°"},
    ],
    mistakes=[
        {"wrong": "Clasificar un ángulo según el largo de sus lados.", "why": "Se mira el largo y no la abertura.", "fix": "Compara la abertura con los referentes, poniendo vértice sobre vértice."},
        {"wrong": "Decir que un ángulo que no coincide con la esquina, pero es más abierto que la mitad de ella, está «cerca de 90°».", "why": "No se compara con los dos referentes.", "fix": "Si es más abierto que 45° y más cerrado que 90°, está entre 45° y 90°."},
    ],
    tiers={
        "recovery": [
            ex(f"{ANG} ¿Cuál ángulo cae en el grupo «cerca de 90°»?", "A", "Es el que cabe justo en la esquina de la hoja."),
            ex(f"{ANG} ¿En qué grupo cae el ángulo B?", "Cerca de 45°", "Es la mitad de la esquina."),
            ex(f"{ANG} ¿Cuál ángulo cae en el grupo «mayor que 90°»?", "D", "Es el que sobrepasa la esquina de la hoja."),
        ],
        "understand": [
            ex("Un ángulo es más cerrado que tu referente de 45°. ¿En qué grupo cae?", "Menor que 45°", "Es más cerrado que el menor referente."),
            ex(f"{ANG} ¿En qué grupo cae el ángulo C?", "Entre 45° y 90°", "Es más abierto que la mitad y más cerrado que toda la esquina."),
            ex("¿Qué se hace primero al comparar un ángulo con un referente: poner vértice sobre vértice o mirar el largo de los lados?", "Poner vértice sobre vértice", "Así se comparan las aberturas."),
        ],
        "apply": [
            ex("La esquina de un libro coincide con tu referente de 90°. ¿En qué grupo cae?", "Cerca de 90°", "Coincide con el ángulo recto."),
            ex("Las tijeras se abren poco, y el ángulo es más cerrado que tu referente de 45°. ¿En qué grupo cae?", "Menor que 45°", "Es más cerrado que 45°."),
            ex("Una puerta se abre más que la esquina de una hoja. ¿En qué grupo cae su ángulo?", "Mayor que 90°", "Sobrepasa el ángulo recto."),
        ],
        "reason": [
            ex("Lía clasifica un ángulo porque «sus lados son largos». ¿Qué error comete y qué debería comparar?", "Mira el largo; debería comparar la abertura con los referentes", "El largo no cambia el ángulo."),
            ex(f"{ANG} Teo dice que C está «cerca de 90°» porque es más grande que B. ¿Tiene razón?", "No; es bastante menor que la esquina entera, así que está entre 45° y 90°", "Para ser cerca de 90°, debería casi coincidir con la esquina."),
        ],
        "challenge": [
            ex("Ordena de menor a mayor estos ángulos: P cerca de 90°, Q cerca de 45°, R mayor que 90°.", "Q, P, R", "45° es menor que 90° y 90° es menor que más de 90°."),
            ex("Una aguja de reloj gira desde el 12 hasta el 3 y otra desde el 12 hasta el 1. ¿Cuál forma un ángulo mayor?", "La que llega al 3", "Giró más que la otra aguja."),
        ],
    },
    context=[ex("Las patas de un caballete de pintura se abren y forman un ángulo parecido a la esquina de una hoja, un poco menos. ¿En qué grupo lo clasificas?", "Cerca de 90°", "Es casi como la esquina de la hoja.")],
    selfcheck=[
        ex("¿Cuántos grupos de ángulos usamos con los referentes de 45° y 90°?", "5", "Son menor que 45°, cerca de 45°, entre 45° y 90°, cerca de 90° y mayor que 90°."),
        ex(f"{ANG} ¿Cuál ángulo cae en «cerca de 45°»?", "B", "Es la mitad de la esquina."),
        ex("Un ángulo es igual al de la esquina de un libro. ¿Mide 45° o 90°?", "90°", "Es un ángulo recto."),
    ],
    open_task=task(
        "Con tus referentes de 45° y 90°, busca en tu casa cuatro ángulos (por ejemplo, la esquina de una mesa, unas tijeras abiertas, una puerta abierta y el abanico de las patas de una silla). Clasifica cada uno en uno de los cinco grupos y explica cómo lo decidiste con tus referentes. Escribe si algún grupo te quedó sin ejemplos.",
        "Esquina de la mesa: cerca de 90°. Tijeras casi cerradas: menor que 45°. Puerta abierta: mayor que 90°. Patas de la silla: entre 45° y 90°. Usé mis referentes poniendo vértice sobre vértice. Me faltó ejemplo para «cerca de 45°».",
        ["clasifica cuatro ángulos reales", "usa los referentes", "explica la decisión", "indica grupos sin ejemplo"],
        ["lista de ángulos", "grupos", "explicación"],
        ["clasificar por el largo de los lados", "no usar los referentes"],
        "Pide que ponga el referente sobre cada ángulo. Reconoce que busque ejemplos para todos los grupos.",
    ),
    reinforce="Con tus referentes, encuentra un ángulo de cada grupo en tu casa. Si no hay uno, fabrícalo con dos lápices.",
    extend="Haz un cartel con cinco ángulos de tu entorno, uno de cada grupo, con su dibujo y su clasificación.",
)
