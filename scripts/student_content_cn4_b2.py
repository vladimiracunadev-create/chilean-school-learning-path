"""Cuaderno del estudiante, 4.º básico Ciencias Naturales: OA 13 (roce, peso y fuerza magnética) y OA 14 (diseño tecnológico que usa fuerzas)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA13, OA14 = "CN04 OA 13", "CN04 OA 14"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 13
register(
    OA13, 1,
    materials="Una caja pequeña de cartón con un libro dentro, una banda elástica gruesa y tres superficies: piso liso, alfombra o toalla, y una tabla. Arrastra con cuidado de no tropezar.",
    use="Aprenderé qué es la fuerza de roce y cómo cambia según las superficies. Sirve para entender por qué algunas cosas se arrastran fácil y otras cuesta mucho.",
    prior=["Sé que una fuerza es un empujón o un tirón.", "Sé que una fuerza puede detener un objeto."],
    explain=[
        "El roce es una fuerza que aparece cuando dos superficies se tocan y una se mueve sobre la otra. El roce se opone al movimiento: va en sentido contrario. Por eso un objeto que se desliza termina deteniéndose.",
        "El roce depende de las superficies. Entre superficies ásperas, como una caja y una alfombra, el roce es grande. Entre superficies lisas, como una caja y un piso pulido, el roce es menor. Con más roce hay que tirar con más fuerza para arrastrar.",
        "El roce también produce calor. Si froto mis manos rápido, se calientan. El roce sirve para frenar una bicicleta y para que los zapatos no resbalen. Pero también desgasta las cosas, como las suelas.",
    ],
    vocab=[("roce", "fuerza entre superficies que se tocan y que se opone al movimiento"), ("superficie", "parte de afuera de un objeto"), ("áspero", "con la superficie rugosa, no lisa"), ("liso", "con la superficie suave y pareja"), ("deslizar", "moverse sobre una superficie")],
    worked=[
        {"title": "Arrastrar una caja", "problem": "Una caja se arrastra con una banda elástica. En el piso liso la banda se alarga 4 cm y en la alfombra se alarga 9 cm. ¿Dónde hay más roce?", "steps": ["Más alargamiento significa que hay que tirar con más fuerza.", "En la alfombra se alargó más: 9 cm es mayor que 4 cm."], "answer": "En la alfombra"},
        {"title": "Frotar las manos", "problem": "Frotas las manos rápido y se calientan. ¿Qué fuerza lo causa?", "steps": ["Las dos manos se tocan y se mueven una contra la otra.", "Eso produce roce, y el roce da calor."], "answer": "La fuerza de roce"},
    ],
    mistakes=[
        {"wrong": "Decir que el roce ayuda a que el objeto siga moviéndose.", "why": "Se confunde con la fuerza de empuje.", "fix": "El roce se opone al movimiento y lo frena."},
        {"wrong": "Pensar que el roce solo ocurre en superficies ásperas.", "why": "Las superficies lisas parecen no tener roce.", "fix": "Hay roce entre cualquier superficie que se toca, pero es menor en las lisas."},
    ],
    tiers={
        "recovery": [
            ex("Una caja se desliza por el piso hasta detenerse. ¿Qué fuerza la frenó?", "El roce", "El roce se opone al movimiento."),
            ex("¿Hay más roce en una superficie áspera o en una lisa?", "En la áspera", "Las rugosidades se traban más."),
            ex("Completa: el roce se ___ al movimiento (opone o ayuda).", "opone", "Va en sentido contrario al movimiento."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es la fuerza de roce?", "Una fuerza entre superficies que se tocan y que se opone al movimiento", "Esa es su definición."),
            ex("¿Por qué se calientan las manos al frotarlas?", "Por el roce entre ellas", "El roce produce calor."),
            ex("Un zapato con suela lisa resbala en el piso mojado. ¿Qué le falta a la suela?", "Más roce", "Una suela con relieve agarra mejor."),
        ],
        "apply": [
            arith("Una banda se alarga 3 cm al arrastrar una caja sobre el piso liso y 8 cm sobre la alfombra. ¿Cuántos cm más se alargó sobre la alfombra?", "8-3", "Más alargamiento indica más fuerza y más roce.", " cm"),
            ex("Una caja se arrastra sobre una tabla lisa, una toalla y un trozo de goma rugosa. ¿En cuál esperas más roce?", "En la goma rugosa", "Es la superficie más áspera de las tres."),
            ex("Una bicicleta frena apretando las zapatas contra la rueda. ¿Qué fuerza usa para detenerse?", "El roce", "Las zapatas rozan la rueda y la frenan."),
        ],
        "reason": [
            ex("Dos amigos arrastran la misma caja: Pablo en el pasto y Rosa en el cemento liso. Pablo dice que le costó más. ¿Qué explicación das?", "El pasto tiene más roce que el cemento liso", "La superficie más áspera frena más."),
            ex("¿Por qué una caja que se desliza sobre hielo llega más lejos que sobre alfombra?", "Porque el hielo tiene menos roce", "Con menos roce el objeto se frena menos."),
        ],
        "challenge": [
            ex("Quieres probar si la alfombra tiene más roce que el piso. ¿Qué debes dejar igual en las dos pruebas?", "La caja, su contenido y la banda", "Solo debe cambiar la superficie."),
            ex("Tomás dice: «el roce es malo y deberíamos eliminarlo». Da un ejemplo de por qué el roce es útil.", "Los frenos y las suelas usan el roce para detener o no resbalar", "Sin roce no podríamos frenar ni caminar bien."),
        ],
    },
    context=[ex("En el invierno el patio de la escuela está mojado y liso. Camila corre y casi se cae. ¿Qué pasó con el roce entre sus zapatos y el piso?", "Disminuyó", "El agua lo hizo más liso y con menos roce.")],
    selfcheck=[
        ex("¿Hacia dónde actúa el roce: a favor o en contra del movimiento?", "En contra", "Se opone al movimiento."),
        ex("¿Qué superficie tiene más roce: lisa o áspera?", "Áspera", "Las rugosidades aumentan el roce."),
        ex("¿Qué se produce al frotar dos superficies rápidamente?", "Calor", "El roce produce calor."),
    ],
    open_task=task(
        "Si puedes, arrastra una caja con un libro dentro, atada a una banda elástica, sobre tres superficies, y mide cuánto se alarga la banda. Si no, usa estos datos: piso liso 3 cm; toalla 6 cm; alfombra 9 cm. Ordena las superficies de menos a más roce y escribe una conclusión.",
        "De menos a más roce: piso liso (3 cm), toalla (6 cm), alfombra (9 cm). Con más roce se alarga más la banda porque hay que tirar más fuerte.",
        ["ordena las tres superficies", "relaciona alargamiento con fuerza y roce", "mantiene igual la caja"],
        ["tabla", "orden escrito", "conclusión"],
        ["ordenar al revés", "no relacionar con el roce"],
        "Reconoce el orden correcto y pide explicar con la banda.",
    ),
    reinforce="Camina por tres superficies de tu casa con calcetines y anota cuál resbala más.",
    extend="Averigua por qué los neumáticos de los autos tienen dibujos y qué pasa cuando se desgastan.",
)

register(
    OA13, 2,
    materials="Una pelota blanda, una hoja de papel, un libro y una bolsa con algo liviano. Suelta objetos desde baja altura sobre el piso, sin que caigan sobre los pies.",
    use="Aprenderé qué es el peso y por qué los objetos caen. Sirve para explicar por qué no flotamos y por qué es más difícil levantar un objeto grande.",
    prior=["Sé que una fuerza puede mover objetos.", "Sé que la masa se mide con una balanza."],
    explain=[
        "El peso es la fuerza con que la Tierra atrae un objeto hacia su centro. Esa atracción se llama fuerza de gravedad. Por la gravedad, un objeto que suelto cae al suelo y nosotros no flotamos.",
        "La gravedad actúa siempre hacia abajo, es decir, hacia el centro de la Tierra. Cuanto más masa tiene un objeto, más fuerte lo atrae la Tierra y mayor es su peso. Por eso un balde con agua cuesta más levantar que uno vacío. Además, el aire frena los objetos que caen: una hoja de papel abierta cae más lento que la misma hoja hecha una bolita, porque el aire la frena más.",
        "En la vida diaria decimos «peso» a lo que marca la balanza en kilogramos, pero en Ciencias el peso es una fuerza. La masa de un objeto es la misma en cualquier lugar. El peso cambia: en la Luna la gravedad es menor y un objeto pesa menos que en la Tierra.",
    ],
    vocab=[("peso", "fuerza con que la Tierra atrae un objeto hacia su centro"), ("gravedad", "atracción de la Tierra sobre los objetos"), ("caer", "moverse hacia el suelo"), ("atraer", "tirar hacia sí"), ("centro de la Tierra", "punto del medio del planeta, hacia donde tira la gravedad")],
    worked=[
        {"title": "La manzana que cae", "problem": "Sueltas una manzana y cae al suelo. ¿Qué fuerza la hace caer y hacia dónde actúa?", "steps": ["La Tierra atrae la manzana: es la gravedad.", "La atracción es hacia el centro de la Tierra, o sea, hacia abajo."], "answer": "La gravedad, hacia abajo"},
        {"title": "Dos mochilas", "problem": "Una mochila tiene 2 kg y otra 5 kg. ¿Cuál tiene más peso en la Tierra?", "steps": ["Más masa significa mayor atracción de la Tierra.", "5 kg es mayor que 2 kg."], "answer": "La de 5 kg"},
    ],
    mistakes=[
        {"wrong": "Pensar que en la Luna la masa de un objeto cambia.", "why": "Se confunde masa con peso.", "fix": "La masa es la misma; el peso es menor porque la gravedad es menor."},
        {"wrong": "Decir que los objetos caen porque «quieren llegar al suelo».", "why": "Se explica con una intención y no con una fuerza.", "fix": "Caen porque la Tierra los atrae con la fuerza de gravedad."},
    ],
    tiers={
        "recovery": [
            ex("Sueltas una pelota. ¿Hacia dónde cae?", "Hacia abajo", "La gravedad la atrae hacia el suelo."),
            ex("¿Cómo se llama la atracción de la Tierra sobre los objetos?", "Gravedad", "Así se llama esa fuerza."),
            ex("Completa: el peso es una ___ (fuerza o masa).", "fuerza", "El peso es la fuerza de gravedad."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es el peso de un objeto?", "La fuerza con que la Tierra lo atrae", "Es la fuerza de gravedad sobre el objeto."),
            ex("¿Por qué no flotamos en el aire?", "Porque la gravedad nos atrae hacia la Tierra", "Esa fuerza nos mantiene en el suelo."),
            ex("¿Hacia qué punto tira la gravedad de la Tierra?", "Hacia su centro", "Por eso todo cae hacia abajo."),
        ],
        "apply": [
            ex("Un balde vacío y un balde con agua. ¿Cuál tiene más peso?", "El balde con agua", "Tiene más masa y la Tierra lo atrae más."),
            arith("Una mochila tiene 3 kg de masa y otra tiene 5 kg. ¿Cuántos kg más de masa tiene la segunda?", "5-3", "Más masa significa más peso.", " kg"),
            ex("Un astronauta tiene 60 kg de masa en la Tierra. ¿Cuántos kg de masa tiene en la Luna?", "60 kg", "La masa no cambia con el lugar."),
        ],
        "reason": [
            ex("Un niño dice: «en la Luna peso menos porque tengo menos masa». ¿Cuál es el error?", "La masa es igual; el peso es menor por la menor gravedad", "El peso depende de la gravedad."),
            ex("Una hoja de papel cae más lento que un libro. ¿Se debe a que la gravedad no actúa sobre la hoja?", "No", "La gravedad actúa en ambos; el aire frena más a la hoja."),
        ],
        "challenge": [
            ex("Soltar una pelota y una goma de borrar de la misma altura. ¿Qué fuerza común actúa sobre las dos al caer?", "La gravedad", "Atrae todos los objetos hacia abajo."),
            ex("Tienes una caja de 4 kg y otra de 1 kg. ¿Cuál cuesta más levantar y por qué?", "La de 4 kg, porque la Tierra la atrae con más fuerza", "Su peso es mayor."),
        ],
    },
    context=[ex("Una persona sube un saco de papas de 10 kg por una escalera y otra, un saco de 2 kg. ¿Cuál debe hacer más fuerza para sostenerlo contra la gravedad?", "La que sube el saco de 10 kg", "Su peso es mayor.")],
    selfcheck=[
        ex("¿Qué fuerza hace caer a los objetos?", "La gravedad", "La Tierra los atrae."),
        ex("¿La gravedad apunta hacia arriba o hacia abajo?", "Hacia abajo", "Va hacia el centro de la Tierra."),
        ex("Un objeto con más masa, ¿tiene más o menos peso?", "Más peso", "La Tierra lo atrae con más fuerza."),
    ],
    open_task=task(
        "Suelta con cuidado desde la misma altura una pelota blanda, una hoja de papel abierta y la misma hoja hecha una bolita, y observa cuál cae primero. Si no puedes, usa estos resultados: pelota y bolita llegan casi al mismo tiempo; la hoja abierta llega después. Escribe qué fuerza actúa en los tres objetos y por qué la hoja abierta tarda más.",
        "Sobre los tres actúa la gravedad. La hoja abierta tarda más porque el aire la frena más al tener más superficie.",
        ["nombra la gravedad", "compara los resultados", "explica con el aire"],
        ["tabla con lo observado", "frase explicativa"],
        ["decir que la gravedad no actúa en la hoja", "no mencionar la fuerza"],
        "Valora el uso de la gravedad y pide explicar el efecto del aire.",
    ),
    reinforce="Anota tres objetos de tu pieza y ordénalos del que crees que tiene más peso al que tiene menos.",
    extend="Averigua por qué un paracaídas ayuda a una persona a caer más lento.",
)

register(
    OA13, 3,
    materials="Un imán de refrigerador grande (que no se pueda tragar) y objetos: una tuerca de hierro, un clip de acero, papel aluminio, una cuchara de madera, una tela, una goma. Mantén el imán lejos de celulares y tarjetas.",
    use="Aprenderé cómo actúa la fuerza magnética de un imán y sobre qué objetos. Sirve para clasificar materiales y entender cómo se pegan algunos objetos.",
    prior=["Sé que una fuerza es un empujón o un tirón.", "Sé que hay objetos de metal y de otros materiales."],
    explain=[
        "Un imán es un objeto que atrae a algunos metales por medio de la fuerza magnética. Atrae al hierro y al acero (y a muy pocos metales más), como una tuerca de hierro o un clip de acero. No atrae a la madera, al plástico, a la goma, a la tela ni al papel aluminio.",
        "La fuerza magnética actúa a distancia: el imán atrae un clip sin tocarlo, y también a través de un papel o una tela delgados. Mientras más cerca está el objeto, más fuerte es la atracción. Los imanes tienen dos extremos llamados polos: norte y sur.",
        "Entre dos imanes, los polos distintos se atraen y los polos iguales se rechazan. Por eso, si acerco dos imanes de una manera se pegan y si doy vuelta uno, se empujan. Los imanes se cuidan lejos de aparatos electrónicos y de tarjetas.",
    ],
    vocab=[("imán", "objeto que atrae algunos metales con fuerza magnética"), ("fuerza magnética", "fuerza que ejerce un imán, incluso a distancia"), ("polo", "extremo de un imán donde la fuerza es más fuerte"), ("atraer", "tirar un objeto hacia sí"), ("repeler", "empujar un objeto lejos de sí")],
    worked=[
        {"title": "Qué atrae el imán", "problem": "Acercas un imán a una tuerca de hierro, a una cuchara de madera y a un papel aluminio. ¿A cuál atrae?", "steps": ["El hierro es un metal que el imán atrae.", "La madera y el papel aluminio no son atraídos."], "answer": "Solo a la tuerca de hierro"},
        {"title": "Dos imanes", "problem": "Al acercar dos imanes por sus polos distintos, ¿se atraen o se rechazan?", "steps": ["Polos distintos se atraen.", "Polos iguales se rechazan."], "answer": "Se atraen"},
    ],
    mistakes=[
        {"wrong": "Decir que el imán atrae todos los metales.", "why": "Se generaliza desde el hierro.", "fix": "Atrae al hierro y al acero, pero no al papel aluminio ni a la mayoría de los materiales."},
        {"wrong": "Pensar que el imán necesita tocar el objeto para atraerlo.", "why": "Se cree que toda fuerza es de contacto.", "fix": "La fuerza magnética actúa a distancia."},
    ],
    tiers={
        "recovery": [
            ex("¿Un imán atrae una tuerca de hierro?", "Sí", "El hierro es atraído por los imanes."),
            ex("¿Un imán atrae una cuchara de madera?", "No", "La madera no es atraída."),
            ex("Completa: los extremos de un imán se llaman ___ (polos o puntas).", "polos", "El norte y el sur son sus polos."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es la fuerza magnética?", "La fuerza que ejerce un imán sobre algunos metales", "Es la fuerza del imán."),
            ex("¿Por qué se dice que la fuerza magnética actúa a distancia?", "Porque atrae sin tocar el objeto", "No necesita contacto."),
            ex("Dos polos iguales de imanes distintos se acercan. ¿Se atraen o se rechazan?", "Se rechazan", "Polos iguales se empujan."),
        ],
        "apply": [
            ex("Clasifica en atrae o no atrae el imán: clip de acero, goma, tuerca de hierro, tela.", "Atrae: clip de acero y tuerca de hierro. No atrae: goma y tela", "Solo el hierro y el acero son atraídos."),
            ex("Un clip de acero está sobre una mesa y el imán se acerca sin tocarlo. El clip salta hacia el imán. ¿Qué tipo de fuerza actuó?", "Una fuerza magnética a distancia", "Actuó sin contacto."),
            ex("Un imán pegado a un refrigerador de metal sostiene una hoja de papel. ¿Qué fuerza sostiene el imán en el refrigerador?", "La fuerza magnética", "El refrigerador de acero atrae el imán."),
        ],
        "reason": [
            ex("Un niño dice que el imán atrae papel aluminio porque es de metal. Al probar, no pasa nada. ¿Qué concluyes?", "No todos los metales son atraídos por el imán", "El imán atrae al hierro y al acero, pero no al aluminio."),
            ex("Un imán atrae un clip por encima de una hoja de papel. ¿Cuál es la conclusión sobre la fuerza?", "Atraviesa materiales delgados como el papel", "El papel no la bloquea."),
        ],
        "challenge": [
            ex("Quieres separar clips de acero de trozos de plástico mezclados en una caja. ¿Qué herramienta usas y por qué sirve?", "Un imán, porque atrae solo los clips", "El plástico no es atraído."),
            ex("Dos imanes se rechazan y al dar vuelta uno de ellos, se atraen. ¿Qué cambió?", "Los polos que se enfrentan", "Pasaron de ser iguales a ser distintos."),
        ],
    },
    context=[ex("En la cocina, Isidora tiene un imán de refrigerador que sostiene una lista. Al acercarlo a la puerta de madera de un mueble, se cae. ¿Por qué?", "Porque la madera no es atraída por el imán", "La madera no responde a la fuerza magnética.")],
    selfcheck=[
        ex("¿Qué dos materiales atrae un imán?", "Hierro y acero", "Son los más comunes que atrae."),
        ex("Polos distintos de dos imanes, ¿se atraen o se rechazan?", "Se atraen", "Los polos distintos se atraen."),
        ex("¿La fuerza magnética actúa solo con contacto?", "No, actúa a distancia", "Atrae sin tocar."),
    ],
    open_task=task(
        "Con un imán grande y estos objetos, prueba cuáles atrae: tuerca de hierro, clip de acero, papel aluminio, cuchara de madera, goma, tela. Si no puedes, usa este resultado: atrae tuerca y clip; no atrae papel aluminio, madera, goma ni tela. Haz una tabla y escribe una regla que resuma qué materiales atrae el imán.",
        "Atrae tuerca de hierro y clip de acero. No atrae aluminio, madera, goma ni tela. Regla: el imán atrae al hierro y al acero, no a todos los materiales.",
        ["clasifica los seis objetos", "da una regla con material", "no generaliza a todos los metales"],
        ["tabla con seis filas", "regla escrita"],
        ["decir que atrae todos los metales", "mezclar objetos y materiales"],
        "Reconoce la tabla completa y pide revisar la regla si generaliza.",
    ),
    reinforce="Con una persona de tu casa, prueba el imán con cinco objetos y anota cuáles atrae.",
    extend="Averigua para qué sirven los imanes en las puertas de refrigeradores y en algunos cierres de mochilas.",
)

register(
    OA13, 4,
    materials="Un imán de refrigerador, clips de acero, un trozo de cartón y una regla. Trabaja con los datos escritos si no tienes materiales.",
    use="Aprenderé a comparar las tres fuerzas (roce, peso y magnética) y a explicar con datos una investigación. Sirve para reconocer cuál fuerza actúa en cada situación.",
    prior=["Sé que el roce se opone al movimiento.", "Sé que el peso es la gravedad y que el imán atrae hierro."],
    explain=[
        "Las tres fuerzas se distinguen por cuándo actúan y hacia dónde. El roce actúa cuando dos superficies se tocan y se opone al movimiento. El peso actúa siempre hacia el centro de la Tierra, sin contacto. La fuerza magnética actúa a distancia entre un imán y un objeto de hierro o acero.",
        "Para comparar, uso preguntas: ¿hay contacto? ¿Hacia dónde actúa? ¿Qué efecto produce? Si una caja se frena al deslizar sobre el piso, es roce. Si un libro cae de la mesa, es peso. Si un clip salta hacia un imán, es fuerza magnética.",
        "En una investigación puedo medir cuántos clips quedan pegados al otro lado de un cartón, poniendo más hojas de cartón entre el imán y los clips para aumentar la distancia. Cambio solo la distancia y cuento los clips. Así veo que, a mayor distancia, la fuerza magnética se debilita. La conclusión debe usar los datos y reconocer un límite.",
    ],
    vocab=[("contacto", "tocarse dos cosas"), ("distancia", "espacio entre dos objetos"), ("debilitar", "hacerse más débil"), ("comparar", "buscar semejanzas y diferencias"), ("clasificar", "ordenar según un criterio")],
    worked=[
        {"title": "Identificar la fuerza", "problem": "Un trineo en el pasto se detiene después de deslizar. ¿Qué fuerza lo detuvo?", "steps": ["Hay contacto entre el trineo y el pasto.", "La fuerza se opone al movimiento: es roce."], "answer": "El roce"},
        {"title": "Imán y distancia", "problem": "Un imán sostiene 8 clips con 1 cm de cartón entre ellos y 3 clips con 4 cm de cartón. ¿Cuántos clips menos sostiene a 4 cm de distancia?", "steps": ["A 1 cm levanta 8 clips; a 4 cm levanta 3 clips.", "Resto: 8 − 3 = 5."], "answer": "5 clips menos"},
    ],
    mistakes=[
        {"wrong": "Decir que el peso solo existe cuando se sostiene un objeto.", "why": "Se siente el peso en las manos y se olvida que actúa siempre.", "fix": "La gravedad atrae a todo objeto, también cuando está quieto en una mesa."},
        {"wrong": "Concluir que el imán es más fuerte lejos que cerca.", "why": "No se compara con datos.", "fix": "Los datos muestran que a menor distancia sostiene más clips."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué fuerza actúa sobre un objeto que cae?", "El peso (la gravedad)", "La Tierra lo atrae hacia abajo."),
            ex("¿Qué fuerza se opone al movimiento cuando una caja se arrastra?", "El roce", "El roce frena."),
            ex("¿Qué fuerza permite que un imán atraiga una tuerca de hierro sin tocarla?", "La fuerza magnética", "Actúa a distancia."),
        ],
        "understand": [
            ex("¿Cuál de las tres fuerzas necesita contacto entre superficies?", "El roce", "El peso y la magnética actúan sin tocar."),
            ex("¿Cuál de las tres fuerzas siempre apunta hacia el centro de la Tierra?", "El peso", "Es la gravedad."),
            ex("¿Por qué el imán solo afecta a algunos objetos?", "Porque solo atrae al hierro y al acero", "Su fuerza magnética no actúa sobre todos los materiales."),
        ],
        "apply": [
            ex("Identifica la fuerza: un clip de acero se pega al imán.", "Fuerza magnética", "Hay atracción de un imán sobre acero."),
            ex("Identifica la fuerza: una pelota que rueda por el pasto se detiene sola.", "Roce", "El pasto roza la pelota y la frena."),
            ex("Identifica la fuerza: una manzana suelta cae de un árbol.", "Peso (gravedad)", "La Tierra la atrae hacia abajo."),
        ],
        "reason": [
            arith("Un imán sostiene 9 clips con 1 cm de cartón de distancia y 4 clips con 5 cm de cartón. ¿Cuántos clips menos sostiene a 5 cm?", "9-4", "A mayor distancia, la fuerza magnética es menor.", " clips"),
            ex("Con los datos del imán anterior, ¿qué relación encuentras entre distancia y fuerza?", "A mayor distancia, menor fuerza", "Sostiene menos clips al alejarse."),
        ],
        "challenge": [
            ex("Un grupo cambió el imán y la distancia a la vez, y dice que la distancia afectó el resultado. ¿Por qué la conclusión no es confiable?", "Porque cambiaron dos cosas a la vez", "No se sabe cuál causó el cambio."),
            ex("Una caja de hierro descansa sobre una mesa. ¿Actúa el peso sobre ella aunque no se mueva?", "Sí", "La gravedad actúa siempre; la mesa la sostiene."),
        ],
    },
    context=[ex("Cecilia ve un imán que sostiene una llave de acero contra el refrigerador. ¿Qué fuerza hay entre el imán y la llave: roce, peso o magnética?", "Magnética", "La atracción del imán la mantiene pegada.")],
    selfcheck=[
        ex("¿Qué tres fuerzas estudiamos en esta clase?", "Roce, peso y fuerza magnética", "Son las tres fuerzas de la unidad."),
        ex("¿Cuál de ellas actúa a distancia: el roce o la fuerza magnética?", "La fuerza magnética", "El roce necesita contacto."),
        ex("En una investigación, ¿cuántas variables debo cambiar a la vez?", "Una", "Así se sabe qué causó el resultado."),
    ],
    open_task=task(
        "Usa estos datos de una prueba simulada: un imán sostuvo 10 clips con 1 cm de cartón entre él y los clips, 6 clips con 3 cm y 2 clips con 6 cm. Haz una tabla, calcula cuántos clips menos sostuvo a 6 cm que a 1 cm, y escribe tu conclusión y un límite de la prueba.",
        "A 6 cm sostuvo 8 clips menos que a 1 cm. Conclusión: a mayor distancia, menor fuerza magnética. Límite: se probó con un solo imán.",
        ["usa los números de la tabla", "calcula la diferencia", "propone un límite"],
        ["tabla", "cálculo", "conclusión"],
        ["concluir lo contrario a los datos", "no citar números"],
        "Valora la tabla y la conclusión con datos y pide mejorar el límite.",
    ),
    reinforce="Anota una situación de tu casa para cada una de las tres fuerzas (roce, peso y magnética).",
    extend="Piensa cómo comprobar si un imán más grande levanta más clips que uno pequeño y qué dejarías igual.",
)

# ---------------------------------------------------------------- OA 14
register(
    OA14, 1,
    materials="Papel, lápiz y objetos de la casa que usan fuerzas: una puerta con cierre o un carrito con ruedas. Todo se puede resolver con los casos escritos.",
    use="Aprenderé a reconocer un problema de la vida diaria y qué fuerza puede ayudar a resolverlo. Sirve para empezar a diseñar un objeto tecnológico.",
    prior=["Conozco las fuerzas de roce, peso y magnética.", "Sé que una fuerza puede mover o detener objetos."],
    explain=[
        "Un objeto tecnológico es algo que las personas diseñan y construyen para resolver un problema. Para diseñar bien, empiezo por entender el problema: qué necesita la persona, dónde y con qué recursos. Después busco qué fuerza puede ayudar.",
        "Por ejemplo, el problema puede ser mover una caja pesada por el patio. La fuerza que molesta es el roce del piso. Una solución son las ruedas, que reducen el roce. Otro problema es que una puerta se abre sola: un imán en el borde la mantiene cerrada con fuerza magnética.",
        "Un buen planteamiento dice: el problema, quién lo tiene, qué fuerza interviene y cómo sé que funciona. Por ejemplo, «la caja se debe mover con menos tirones». Con eso defino criterios de éxito que puedo medir, como cuántos centímetros se alarga una banda al tirar.",
    ],
    vocab=[("objeto tecnológico", "objeto diseñado por personas para resolver un problema"), ("problema", "situación que necesita una solución"), ("criterio de éxito", "dato con el que compruebo que mi solución funciona"), ("diseñar", "pensar y dibujar un objeto antes de construirlo"), ("construir", "armar el objeto planeado")],
    worked=[
        {"title": "Mover una caja", "problem": "La caja del patio pesa mucho y se arrastra con dificultad. ¿Qué fuerza molesta y qué solución puede ayudar?", "steps": ["Al arrastrar, el piso roza la caja.", "Las ruedas disminuyen ese roce."], "answer": "Molesta el roce; ayudan las ruedas"},
        {"title": "Puerta que se abre sola", "problem": "La puerta de un mueble de metal se abre sola. ¿Qué fuerza puede mantenerla cerrada?", "steps": ["Hay un borde de metal que un imán atrae.", "Un imán pegado a la puerta usa la fuerza magnética."], "answer": "Un imán, con fuerza magnética"},
    ],
    mistakes=[
        {"wrong": "Empezar a construir sin saber cuál es el problema.", "why": "Se quiere partir de inmediato con los materiales.", "fix": "Escribe primero el problema y qué necesita la persona."},
        {"wrong": "Pensar que un objeto tecnológico debe tener motor o electricidad.", "why": "Se asocia tecnología con aparatos electrónicos.", "fix": "Una rueda o un cierre magnético también son objetos tecnológicos."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es un objeto tecnológico?", "Un objeto diseñado para resolver un problema", "Se construye para una necesidad."),
            ex("¿Qué se debe entender primero al diseñar: el problema o los materiales?", "El problema", "Sin eso no se sabe qué resolver."),
            ex("Una rueda disminuye cuál de estas fuerzas: ¿el roce o el peso?", "El roce", "La rueda rueda en vez de arrastrarse."),
        ],
        "understand": [
            ex("¿Para qué sirve un criterio de éxito?", "Para comprobar con un dato si la solución funciona", "Se mide para saber si resolvió el problema."),
            ex("Un cierre magnético mantiene una puerta cerrada. ¿Qué fuerza usa?", "La fuerza magnética", "El imán atrae el metal."),
            ex("¿Es un cierre magnético un objeto tecnológico aunque no tenga motor ni pilas?", "Sí", "Se diseña para resolver el problema de mantener algo cerrado."),
        ],
        "apply": [
            ex("Problema: un carro con ladrillos es difícil de empujar por el pasto. ¿Qué fuerza molesta?", "El roce", "El pasto roza las ruedas o el fondo."),
            ex("Problema: una tabla de cortar resbala sobre el mesón. ¿Qué fuerza falta aumentar?", "El roce", "Con goma debajo, aumenta el roce y no resbala."),
            ex("Problema: una puerta de metal se abre sola. Entre un imán, una piedra y una tela, ¿qué eliges y por qué?", "El imán, porque usa fuerza magnética sobre el metal", "La piedra y la tela no atraen el metal."),
        ],
        "reason": [
            ex("Una compañera puso ruedas pequeñas a una caja pesada y sigue costando mover la caja por el pasto. Dice que las ruedas no sirven. ¿Qué dato falta para decidir?", "Cuánta fuerza se necesita sin ruedas y con ruedas (por ejemplo, cuánto se alarga una banda)", "Hay que comparar con una medida, no con una impresión."),
            ex("Dos propuestas para guardar una puerta cerrada: un cordel o un imán. ¿Qué criterio de éxito puede usarse para decidir?", "Que la puerta se mantenga cerrada sin ayuda", "Es un dato observable."),
        ],
        "challenge": [
            ex("Para mover una caja de 8 kg por el patio, una persona propone tirar de ella y otra, ponerla sobre rodillos redondos. ¿Cuál reduce más el roce?", "Ponerla sobre rodillos", "Rodar disminuye el roce comparado con arrastrar."),
            ex("Escribe un criterio de éxito medible para una solución que mueva una caja con menos esfuerzo.", "Que la banda elástica se alargue menos al tirar", "El alargamiento es un dato medible de la fuerza."),
        ],
    },
    context=[ex("En un taller, Matías necesita un objeto que mantenga una puerta de buzón de acero cerrada sin llave y sin electricidad. ¿Qué fuerza puede usar?", "Fuerza magnética", "Un imán la mantiene cerrada.")],
    selfcheck=[
        ex("¿Para qué se diseña un objeto tecnológico?", "Para resolver un problema", "Su propósito es una necesidad."),
        ex("¿Qué fuerza reduce una rueda?", "El roce", "Rodar frena menos que arrastrar."),
        ex("¿Qué se escribe antes de construir?", "El problema", "Es el primer paso del diseño."),
    ],
    open_task=task(
        "Elige uno de estos problemas: A) una caja pesada es difícil de arrastrar; B) una puerta de metal se abre sola; C) una tabla de cortar resbala. Escribe en tres líneas el problema, qué fuerza interviene y una idea de solución con un dibujo simple. Agrega un criterio de éxito medible.",
        "Problema A: la caja se arrastra con mucho roce. Fuerza: roce. Solución: poner ruedas o rodillos. Criterio: la banda se alarga menos de 4 cm al tirar.",
        ["identifica el problema", "nombra la fuerza correcta", "propone una solución y un criterio medible"],
        ["texto de tres líneas", "dibujo", "criterio escrito"],
        ["no nombrar ninguna fuerza", "criterio sin medida"],
        "Reconoce la elección y pide precisar el criterio de éxito si no es medible.",
    ),
    reinforce="Mira tres objetos de tu casa y escribe qué problema resuelven y qué fuerza usan.",
    extend="Averigua qué problema resolvió la invención de la rueda y cuándo la usamos hoy.",
)

register(
    OA14, 2,
    materials="Una caja liviana, una banda elástica, un trozo de tela, cartón, y cuatro lápices redondos o tubos de cartón como rodillos. Pruebas en piso plano.",
    use="Aprenderé a diseñar soluciones que aumenten o reduzcan el roce. Sirve para decidir qué materiales usar en cada diseño.",
    prior=["Sé que el roce se opone al movimiento.", "Sé que las superficies ásperas tienen más roce."],
    explain=[
        "A veces conviene reducir el roce y a veces aumentarlo. Para mover una caja por el patio, quiero menos roce: uso ruedas, rodillos o una superficie lisa. Para que un zapato no resbale, quiero más roce: uso una suela con relieve.",
        "Los diseñadores eligen el material según lo que necesitan. La goma agarra mejor que el plástico liso. Una tabla pulida desliza más que una alfombra. Un objeto con ruedas rueda en vez de arrastrarse, y eso reduce el roce.",
        "Para comprobar el diseño, hago una prueba justa: mismo objeto, mismo piso, misma forma de tirar. Mido, por ejemplo, cuántos centímetros se alarga una banda. Un diseño que reduce el roce hace que la banda se alargue menos.",
    ],
    vocab=[("reducir", "hacer menor"), ("aumentar", "hacer mayor"), ("rodillo", "cilindro que rueda bajo un objeto"), ("relieve", "partes altas y bajas de una superficie"), ("prueba justa", "prueba en que cambia una sola cosa")],
    worked=[
        {"title": "Caja sobre rodillos", "problem": "Una banda se alarga 8 cm al arrastrar una caja y 3 cm cuando la caja va sobre rodillos. ¿Cuánto redujo el diseño la fuerza medida?", "steps": ["Sin rodillos: 8 cm.", "Con rodillos: 3 cm.", "Resto: 8 − 3 = 5."], "answer": "5 cm menos"},
        {"title": "Suela que no resbala", "problem": "Un zapato resbala en el piso mojado. ¿Cómo aumentas el roce?", "steps": ["Pido una suela con relieve de goma.", "El relieve y la goma agarran el piso."], "answer": "Con una suela de goma con relieve"},
    ],
    mistakes=[
        {"wrong": "Querer siempre reducir el roce.", "why": "Se piensa que el roce solo es un problema.", "fix": "A veces necesitamos más roce, como en frenos, zapatos y mangos."},
        {"wrong": "Cambiar la caja y el piso a la vez al probar el diseño.", "why": "Se quieren probar muchas cosas juntas.", "fix": "Cambia solo el diseño y deja igual lo demás."},
    ],
    tiers={
        "recovery": [
            ex("Para que una caja se mueva más fácil, ¿quieres más o menos roce?", "Menos roce", "Con menos roce cuesta menos moverla."),
            ex("Para que un zapato no resbale, ¿quieres más o menos roce?", "Más roce", "Más roce da más agarre."),
            ex("Las ruedas, ¿aumentan o reducen el roce?", "Reducen", "Rodar frena menos que arrastrar."),
        ],
        "understand": [
            ex("¿Por qué una suela con relieve ayuda a no resbalar?", "Porque aumenta el roce con el piso", "Las partes altas agarran la superficie."),
            ex("¿Por qué un trineo desliza mejor sobre hielo que sobre pasto?", "Porque el hielo tiene menos roce", "La superficie lisa roza menos."),
            ex("¿Qué es una prueba justa en el diseño de un objeto?", "Cambiar solo una cosa y dejar igual las demás", "Así se sabe qué mejoró el resultado."),
        ],
        "apply": [
            arith("Una banda se alarga 10 cm al tirar una caja sin rodillos y 4 cm con rodillos. ¿Cuántos cm menos se alarga con rodillos?", "10-4", "El diseño con rodillos requiere menos fuerza.", " cm"),
            ex("Quieres un mango de herramienta que no se resbale de la mano mojada. ¿Qué material eliges: plástico liso o goma rugosa?", "Goma rugosa", "Tiene más roce con la mano."),
            ex("Quieres diseñar un patín para mover un mueble pesado sobre un piso de madera. ¿Eliges una base de tela suave y lisa o una base de goma rugosa?", "Una base de tela suave y lisa", "Reduce el roce y facilita el deslizamiento."),
        ],
        "reason": [
            ex("Dos compañeros midieron el alargamiento de la banda: A 7 cm con ruedas y B 2 cm con rodillos y piso más liso. Concluyen que los rodillos son mejores. ¿Qué problema tiene su prueba?", "Cambiaron el piso además del diseño", "No se sabe qué causó la diferencia."),
            ex("Un diseño usa ruedas de goma blanda en un piso muy rugoso. Una amiga propone ruedas de plástico duro. ¿Qué dato comparan para elegir?", "El alargamiento de la banda al tirar", "Se compara la fuerza necesaria."),
        ],
        "challenge": [
            ex("Tu diseño reduce el roce de una caja, pero la caja ahora rueda sola en una pendiente. ¿Qué agregarías para controlarla?", "Un freno que aumente el roce", "El freno controla el movimiento."),
            ex("Una silla con ruedas se desplaza sola en un piso inclinado. ¿Qué parte se puede diseñar para que esté quieta cuando se necesita?", "Un seguro de ruedas que aumente el roce", "El seguro frena las ruedas."),
        ],
    },
    context=[arith("Una escuela quiere mover una banca de 12 kg. Con arrastre, la banda se alarga 11 cm; con una base con ruedas se alarga 5 cm. ¿Cuántos cm menos?", "11-5", "La base con ruedas redujo el roce.", " cm")],
    selfcheck=[
        ex("¿Cuándo conviene aumentar el roce?", "Cuando queremos frenar o no resbalar", "Frenos y suelas necesitan agarre."),
        ex("¿Qué dispositivo reduce el roce al mover cosas?", "Las ruedas o los rodillos", "Rodar frena menos que arrastrar."),
        ex("¿Qué debe cambiar una prueba justa?", "Una sola cosa", "Así se aísla la causa."),
    ],
    open_task=task(
        "Diseña una solución para mover una caja pesada de un lado a otro del patio. Elige entre rodillos, ruedas o una tela lisa. Dibuja tu diseño, explica por qué reduce el roce y usa estos datos de la prueba: sin diseño la banda se alarga 9 cm; con rodillos 4 cm; con tela lisa 7 cm. Calcula cuál diseño es mejor y cuántos cm menos usa que sin diseño.",
        "Con rodillos la banda se alarga 4 cm, 5 cm menos que sin diseño (9 − 4). Es mejor que la tela lisa (7 cm).",
        ["elige un diseño y lo justifica con roce", "usa los datos para decidir", "calcula la diferencia"],
        ["dibujo", "cálculo", "justificación escrita"],
        ["elegir sin usar los datos", "no explicar con roce"],
        "Reconoce el uso de datos y pide mejorar la explicación si no menciona el roce.",
    ),
    reinforce="Observa dos zapatos de tu casa y di cuál tiene la suela con más roce y por qué.",
    extend="Averigua cómo se usan los rodamientos (bolitas de acero) para reducir el roce en máquinas.",
)

register(
    OA14, 3,
    materials="Una tabla o cartón firme y libros para armar una rampa, un lápiz y una regla como palanca, una caja liviana. No uses objetos pesados ni frágiles.",
    use="Aprenderé cómo una rampa y una palanca ayudan a mover cargas con menos fuerza. Sirve para diseñar objetos que levantan o suben cosas.",
    prior=["Sé que el peso es la fuerza de la gravedad.", "Sé que una fuerza más pequeña cuesta menos hacer."],
    explain=[
        "Una rampa es un plano inclinado. Para subir una caja a una altura, puedo levantarla de golpe o empujarla por una rampa. Con la rampa uso menos fuerza, pero recorro más camino. Mientras más larga y menos inclinada, menos fuerza se necesita.",
        "Una palanca es una barra que gira sobre un punto de apoyo. Un balancín es una palanca. Si empujo la barra lejos del punto de apoyo, necesito menos fuerza para levantar la carga. Si empujo cerca, necesito más fuerza.",
        "Ambos objetos usan la fuerza de manera inteligente. No hacen que el trabajo desaparezca: reparten el esfuerzo en más distancia. Para diseñar, decido la altura que quiero alcanzar y pruebo distintas inclinaciones, midiendo con una banda elástica cuánto se alarga.",
    ],
    vocab=[("rampa", "superficie inclinada que sirve para subir o bajar cosas"), ("palanca", "barra que gira sobre un punto de apoyo"), ("punto de apoyo", "lugar donde la palanca se sostiene y gira"), ("carga", "objeto que se quiere levantar o mover"), ("inclinación", "qué tan empinada es una superficie")],
    worked=[
        {"title": "Dos rampas", "problem": "Una caja sube por una rampa corta y empinada con un tirón de 12 cm de alargamiento de la banda, y por una larga y suave con 5 cm. ¿Cuál requiere menos fuerza?", "steps": ["Menos alargamiento significa menos fuerza.", "5 cm es menor que 12 cm."], "answer": "La rampa larga y suave"},
        {"title": "Palanca", "problem": "Quieres levantar una carga con una barra. ¿Dónde empujas para usar menos fuerza?", "steps": ["Lejos del punto de apoyo.", "Así se necesita menos fuerza para levantar la carga."], "answer": "Lejos del punto de apoyo"},
    ],
    mistakes=[
        {"wrong": "Pensar que la rampa quita todo el trabajo.", "why": "Parece fácil porque la fuerza es menor.", "fix": "Con la rampa se usa menos fuerza, pero se recorre más camino."},
        {"wrong": "Empujar la palanca cerca del punto de apoyo esperando que cueste menos.", "why": "Se piensa que cerca es más directo.", "fix": "Empujar lejos del punto de apoyo requiere menos fuerza."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es una rampa?", "Una superficie inclinada para subir o bajar cosas", "Es un plano inclinado."),
            ex("En una palanca, ¿cómo se llama el lugar donde gira la barra?", "Punto de apoyo", "Es el pivote de la palanca."),
            ex("¿Un balancín es una rampa o una palanca?", "Una palanca", "Es una barra que gira en un punto."),
        ],
        "understand": [
            ex("¿Qué ventaja tiene una rampa para subir una caja?", "Se usa menos fuerza", "El esfuerzo se reparte en más camino."),
            ex("¿Qué se paga a cambio de usar menos fuerza en una rampa?", "Se recorre más camino", "Es más larga."),
            ex("¿Dónde conviene empujar una palanca para usar menos fuerza?", "Lejos del punto de apoyo", "Así la palanca ayuda más."),
        ],
        "apply": [
            arith("Una banda se alarga 14 cm al subir una caja por una rampa empinada y 6 cm por una suave. ¿Cuántos cm menos con la suave?", "14-6", "Menos alargamiento indica menos fuerza.", " cm"),
            ex("Quieres subir una caja a un camión. ¿Eliges una rampa larga o corta con la misma altura?", "Una rampa larga", "Es menos empinada y requiere menos fuerza."),
            ex("Dos niños levantan la misma piedra con una barra: uno empuja el extremo cercano al punto de apoyo y el otro, el extremo lejano. ¿Quién necesita menos fuerza?", "El que empuja el extremo lejano", "La palanca ayuda más lejos del apoyo."),
        ],
        "reason": [
            ex("Un compañero dice que con una rampa «el trabajo desaparece». ¿Qué falta en su explicación?", "Que se recorre más camino a cambio de menos fuerza", "El esfuerzo se reparte."),
            ex("Para comparar rampas hay que subir la misma caja. ¿Por qué?", "Para que la fuerza dependa solo de la rampa", "Una caja distinta cambiaría el resultado."),
        ],
        "challenge": [
            ex("Una persona quiere subir una caja pesada de 10 kg hasta 1 m de altura. ¿Qué rampa conviene: una tabla de 2 m de largo o una de 4 m de largo?", "La de 4 m", "Es menos empinada y requiere menos fuerza."),
            ex("Con una barra y un apoyo, una niña levanta una piedra. Si mueve el apoyo más cerca de la piedra, ¿necesita más o menos fuerza al empujar el otro extremo?", "Menos fuerza", "Queda más lejos del apoyo."),
        ],
    },
    context=[ex("En una bodega, Rodrigo debe subir cajas a un camión de 1 m de altura y tiene una tabla de 2 m y otra de 4 m. ¿Cuál tabla le conviene para usar menos fuerza?", "La de 4 m", "Hace una rampa menos empinada.")],
    selfcheck=[
        ex("¿Una rampa permite usar menos o más fuerza?", "Menos fuerza", "Reparte el esfuerzo en más camino."),
        ex("¿Qué es el punto de apoyo?", "El lugar donde gira la palanca", "Es el pivote."),
        ex("¿Un balancín es una palanca?", "Sí", "Es una barra que gira sobre un apoyo."),
    ],
    open_task=task(
        "Con una tabla y libros, arma dos rampas para la misma caja: una corta y empinada y otra larga y suave, y mide con una banda cuánto se alarga. Si no puedes, usa estos datos: rampa corta 12 cm; rampa larga 5 cm. Escribe qué rampa requiere menos fuerza, cuántos cm menos y qué se pierde a cambio.",
        "La rampa larga requiere menos fuerza: 12 − 5 = 7 cm menos de alargamiento. A cambio se recorre más camino.",
        ["compara las dos rampas", "calcula la diferencia", "menciona el camino más largo"],
        ["tabla", "cálculo", "frase final"],
        ["decir que la rampa elimina el esfuerzo", "no relacionar alargamiento con fuerza"],
        "Valora la comparación con datos y pide completar la ventaja y el costo.",
    ),
    reinforce="Mira tu casa o tu barrio y anota dos rampas y una palanca que uses.",
    extend="Averigua por qué los caminos de un cerro a veces se hacen en zigzag como una rampa suave.",
)

register(
    OA14, 4,
    materials="Cartón, cinta adhesiva, dos imanes de refrigerador, una banda elástica gruesa, tijeras de punta redonda, un par de lápices. Construye con una persona adulta y cuida los dedos.",
    use="Aprenderé a planificar un objeto simple que use un imán o una banda elástica. Sirve para convertir una idea en un plan que se pueda construir.",
    prior=["Sé que el imán atrae hierro y acero.", "Sé que una banda elástica se estira y vuelve a su forma."],
    explain=[
        "Un plan de diseño tiene partes: el problema, un dibujo con medidas, la lista de materiales, los pasos para construir y cómo lo voy a probar. Un dibujo claro tiene nombres y medidas en centímetros. Así otra persona puede construir lo mismo.",
        "Los imanes se pueden usar en cierres, como el de una caja de cartón con tapa que se mantiene cerrada. Una banda elástica guarda fuerza al estirarse y la entrega al soltarse, como en un lanzador de papelitos. Con la banda se debe tener cuidado de no apuntar a nadie.",
        "Antes de construir hago una lista de pasos y el orden. Pienso en la seguridad: uso materiales sin filo, no apunto a personas y pido ayuda con las tijeras. Defino un criterio de éxito, por ejemplo: «la tapa debe quedar cerrada al mover la caja».",
    ],
    vocab=[("plan", "pasos y materiales que se escriben antes de construir"), ("medida", "largo, ancho o alto de una parte, en cm"), ("material", "cosa con la que se construye"), ("prototipo", "primera versión de un objeto para probar"), ("seguridad", "cuidado para evitar daños")],
    worked=[
        {"title": "Caja con cierre magnético", "problem": "Quieres que la tapa de una caja de cartón quede cerrada. ¿Qué materiales y qué idea usas?", "steps": ["Pego un imán en la tapa y un clip de acero en el borde de la caja.", "El imán atrae el acero y mantiene la tapa cerrada."], "answer": "Un imán en la tapa y un clip de acero en la caja"},
        {"title": "Medidas del plan", "problem": "En el plan, una tira de cartón mide 12 cm y otra mide 8 cm. ¿Cuántos cm de cartón se necesitan juntas?", "steps": ["Sumo las dos medidas: 12 + 8 = 20.", "Con 20 cm de cartón alcanzan las dos tiras."], "answer": "20 cm"},
    ],
    mistakes=[
        {"wrong": "Construir sin dibujar ni anotar medidas.", "why": "Se quiere empezar rápido.", "fix": "Dibuja y anota medidas en cm antes de cortar."},
        {"wrong": "Apuntar una banda elástica a otra persona para probarla.", "why": "Se piensa que es un juego sin riesgo.", "fix": "Prueba solo contra una pared o una caja, nunca hacia personas."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué se hace antes de construir un objeto: un plan o cortar materiales?", "Un plan", "El plan ordena la construcción."),
            ex("¿Qué fuerza mantiene cerrada una tapa con imán?", "La fuerza magnética", "El imán atrae el acero."),
            ex("Una banda elástica estirada guarda fuerza. ¿Qué pasa al soltarla?", "Vuelve a su forma y entrega esa fuerza", "La banda es un material elástico."),
        ],
        "understand": [
            ex("¿Por qué el dibujo del plan lleva medidas?", "Para que otra persona pueda construir lo mismo", "Las medidas aseguran que se vea igual."),
            ex("¿Qué es un prototipo?", "La primera versión de un objeto para probarla", "Se prueba y se mejora."),
            ex("¿Por qué no se apunta una banda elástica hacia personas?", "Porque puede lastimar", "Es un tema de seguridad."),
        ],
        "apply": [
            arith("Un lanzador tiene una base de 15 cm y una pared de 9 cm. ¿Cuántos cm miden juntos la base y la pared?", "15+9", "Se suman las dos medidas.", " cm"),
            ex("Ordena los pasos: probar, dibujar el plan, construir, escribir el problema.", "Escribir el problema, dibujar el plan, construir y probar", "Primero se entiende el problema y se planifica."),
            ex("Quieres que una tapa de cartón quede cerrada con un imán. ¿Qué otro material necesitas en la caja que el imán sí atraiga: un trozo de plástico o un clip de acero?", "Un clip de acero", "El imán atrae al acero."),
        ],
        "reason": [
            ex("Un grupo midió 10 cm en el dibujo, pero al construir hizo la pieza de 14 cm. ¿Qué error cometieron?", "No respetaron la medida del plan", "La pieza no coincide con el dibujo."),
            ex("Un criterio de éxito es «la tapa queda cerrada al mover la caja». ¿Cómo lo compruebas?", "Moviendo la caja y observando si se abre", "Se prueba con la acción descrita."),
        ],
        "challenge": [
            ex("Tu cierre magnético se despega al mover la caja. ¿Qué cambio puedes hacer para aumentar la fuerza magnética?", "Acercar los imanes o usar uno más grande", "Cuanto más cerca, más fuerte la atracción."),
            ex("En un diseño de elástico, quieres que el objeto llegue más lejos. ¿Qué cambias en la banda?", "La estiras más", "Una banda más estirada entrega más fuerza."),
        ],
    },
    context=[arith("Para armar la caja con cierre de imán, Sofía necesita cortar 4 tiras de cartón de 6 cm cada una. ¿Cuántos cm de tira necesita en total?", "4*6", "Se suman cuatro medidas iguales.", " cm")],
    selfcheck=[
        ex("¿Qué debe llevar un dibujo de diseño?", "Medidas y nombres de las partes", "Sirve para construir con precisión."),
        ex("¿Qué se hace con una banda elástica por seguridad?", "No se apunta a las personas", "Puede lastimar a alguien."),
        ex("¿Qué es un criterio de éxito?", "Un dato para comprobar si funciona", "Se mide al probar."),
    ],
    open_task=task(
        "Planifica una caja de cartón con tapa que se cierre con un imán. Escribe el problema, dibuja la caja con medidas (por ejemplo, 12 cm de largo, 8 cm de ancho y 5 cm de alto), haz la lista de materiales y de pasos, y un criterio de éxito. No hace falta construirla todavía.",
        "Problema: la tapa se abre sola. Materiales: cartón, cinta, un imán y un clip de acero. Medidas: 12 × 8 × 5 cm. Criterio: la tapa queda cerrada al mover la caja.",
        ["dibujo con medidas", "lista de materiales y pasos", "criterio de éxito medible"],
        ["dibujo", "lista", "criterio"],
        ["no incluir medidas", "no considerar seguridad"],
        "Reconoce un plan completo y pide agregar medidas si faltan.",
    ),
    reinforce="Haz el dibujo con medidas de un objeto de tu casa que cierre o sujete algo.",
    extend="Averigua cómo funciona el cierre magnético de un estuche o de la puerta de un refrigerador.",
)

register(
    OA14, 5,
    materials="El prototipo de la clase anterior, si lo hiciste, o los datos escritos. Papel y lápiz para registrar pruebas y mejoras. Cuida los dedos y no uses la banda hacia personas.",
    use="Aprenderé a probar un objeto, mejorarlo y comunicar su resultado de manera responsable. Sirve para terminar un diseño con evidencia y no solo con opiniones.",
    prior=["Sé planear un objeto con problema, dibujo y criterio de éxito.", "Sé comparar medidas y calcular diferencias."],
    explain=[
        "Después de construir, pruebo el objeto con el criterio de éxito. Hago varias pruebas y anoto los datos en una tabla. Si el criterio no se cumple, busco la causa y cambio una sola cosa a la vez.",
        "Comunicar el resultado significa contar el problema, la solución, los datos y las mejoras. Una buena conclusión cita números: «el cierre aguantó 8 de 10 movimientos» es mejor que «funcionó bien». También dice los límites: probé solo con una caja y en una mesa.",
        "Un diseño responsable cuida la seguridad y el ambiente: usa materiales reutilizados, sin filos, y se explica a otras personas cómo usarlo sin riesgo. Si no funciona, no es un fracaso: es información para mejorar.",
    ],
    vocab=[("prueba", "intento de usar el objeto para ver si funciona"), ("mejorar", "cambiar algo para que funcione mejor"), ("comunicar", "contar los resultados a otras personas"), ("reutilizar", "volver a usar un material en vez de botarlo"), ("evidencia", "datos que apoyan lo que se dice")],
    worked=[
        {"title": "Resultados de las pruebas", "problem": "Un cierre magnético se mantuvo cerrado en 7 de 10 movimientos de la caja. ¿En cuántos se abrió?", "steps": ["Total de pruebas: 10.", "Se mantuvo cerrado en 7.", "Se abrió en 10 − 7 = 3."], "answer": "En 3 pruebas"},
        {"title": "Una mejora", "problem": "El cierre se abre al mover mucho la caja. Proponen acercar el imán y agregar un segundo. ¿Cuántas cosas cambiaron y qué problema tiene la prueba?", "steps": ["Cambiaron dos cosas: la distancia y el número de imanes.", "No se sabe cuál produjo la mejora."], "answer": "Dos cosas; conviene cambiar una a la vez"},
    ],
    mistakes=[
        {"wrong": "Decir «funcionó bien» sin dar números.", "why": "Se resume con una opinión.", "fix": "Cita cuántas pruebas resultaron bien de cuántas."},
        {"wrong": "Cambiar varias partes del diseño a la vez para mejorarlo.", "why": "Se quiere arreglar todo rápido.", "fix": "Cambia una sola cosa y vuelve a probar."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué se hace después de construir el objeto?", "Probarlo", "Se comprueba si cumple el criterio."),
            ex("¿Qué debe citar una buena conclusión?", "Datos", "Los datos son la evidencia."),
            ex("Si una prueba falla, ¿es información para mejorar o un fracaso total?", "Información para mejorar", "Sirve para corregir el diseño."),
        ],
        "understand": [
            ex("¿Por qué conviene hacer varias pruebas del objeto?", "Para ver si el resultado se repite", "Una prueba sola puede ser casualidad."),
            ex("¿Qué significa reutilizar un material?", "Volver a usarlo en vez de botarlo", "Cuida el ambiente."),
            ex("¿Por qué se explican los límites de una prueba?", "Para decir qué tan segura es la conclusión", "Cada prueba tiene condiciones limitadas."),
        ],
        "apply": [
            arith("Un cierre se mantuvo cerrado en 8 de 12 pruebas. ¿En cuántas se abrió?", "12-8", "Se resta lo que funcionó del total.", " pruebas"),
            ex("Una tapa magnética se abrió en 4 de 10 pruebas. ¿Cumple el criterio «queda cerrada en al menos 9 de 10 pruebas»?", "No", "Quedó cerrada en 6, menos que 9."),
            ex("Una banda elástica lanza un papelito 40 cm. Mejoras el diseño cambiando solo el estiramiento y llega a 65 cm. ¿Cuántos cm más lejos llegó?", "25 cm", "65 − 40 = 25."),
        ],
        "reason": [
            ex("Un grupo escribe: «nuestro objeto funcionó». ¿Qué le falta a esa conclusión?", "Datos que lo muestren", "Sin números no hay evidencia."),
            ex("El imán se despegó cuando la caja tenía muchas hojas de papel entre el imán y el clip. ¿Qué explicación propones sobre la distancia?", "Que las hojas alejaron el imán del clip y bajó la fuerza", "A mayor distancia, menor fuerza magnética."),
        ],
        "challenge": [
            ex("Un grupo probó su rampa solo con una caja de 1 kg. ¿Cuál es un límite de su conclusión?", "No sabemos si funciona con cajas más pesadas", "Se probó con un solo caso."),
            ex("Una amiga dice que su objeto usa pilas porque «todo lo tecnológico las necesita». ¿Qué ejemplo de esta unidad muestra que no es así?", "La rampa o el cierre magnético", "Funcionan sin pilas."),
        ],
    },
    context=[ex("En una exposición, Valentina muestra una rampa de cartón y dice: «mi rampa sube cajas con menos fuerza: la banda se alarga 5 cm frente a 12 cm sin rampa». ¿Su conclusión usa evidencia?", "Sí", "Cita datos medidos.")],
    selfcheck=[
        ex("¿Qué se debe cambiar a la vez cuando mejoras un diseño?", "Una sola cosa", "Así se sabe qué mejoró."),
        ex("¿Qué dato muestra que un diseño funciona?", "Un resultado que cumple el criterio de éxito", "Se compara con el criterio."),
        ex("¿Qué cuidas al usar una banda elástica?", "No apuntar a personas", "Así se evitan lesiones."),
    ],
    open_task=task(
        "Usa estos datos simulados de un objeto de la clase anterior (cierre magnético con un solo imán): se mantuvo cerrado en 5 de 10 movimientos de la caja. Con un segundo imán, cerrado en 9 de 10. Calcula la mejora, escribe una conclusión con números, un límite y una medida de seguridad.",
        "Con dos imanes quedó cerrado en 4 pruebas más (9 − 5). Conclusión: el segundo imán mejoró el cierre. Límite: solo probamos con una caja. Seguridad: los imanes quedan pegados dentro de la tapa para que no se pierdan.",
        ["calcula la mejora", "cita datos en la conclusión", "incluye límite y seguridad"],
        ["cálculo", "conclusión", "frase de límite y seguridad"],
        ["conclusión sin números", "no mencionar seguridad"],
        "Valora que cite números y pide agregar un límite o seguridad si faltan.",
    ),
    reinforce="Escribe tres frases que cuenten el problema, la solución y un dato de prueba de un objeto que conozcas.",
    extend="Averigua cómo se reutilizan materiales en un taller de reciclaje cercano o en tu escuela.",
)
