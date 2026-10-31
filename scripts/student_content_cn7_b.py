"""Cuaderno del estudiante, 7.º básico Ciencias Naturales: OA 11 (ciclo y transformación de las rocas)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA11 = "CN07 OA 11"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 11, clase 1
register(
    OA11, 1,
    materials="Papel y lápiz. Las descripciones de las rocas están escritas en el cuaderno. Si quieres, mira una piedra de tu casa o del patio, sin romperla ni golpearla.",
    use="Aprenderé a reconocer los rasgos de las rocas ígneas, sedimentarias y metamórficas. Sirve para clasificar una roca usando evidencia y no solo su color.",
    prior=["Sé que un modelo ayuda a explicar lo que no se ve.", "Sé separar una observación de una interpretación."],
    explain=[
        "Una roca es un material sólido de la Tierra formado por uno o más minerales. Un mineral es una sustancia sólida natural, con composición definida, como el cuarzo. Las rocas se agrupan en tres familias según cómo se formaron: ígneas, sedimentarias y metamórficas.",
        "Las rocas ígneas se forman cuando el magma (roca fundida bajo la superficie) o la lava (roca fundida que sale a la superficie) se enfría y se endurece. Tienen cristales entrelazados, vidrio o pequeños agujeros de gas, y no tienen capas ni fósiles. Las sedimentarias se forman cuando fragmentos de otras rocas o restos de seres vivos, llamados sedimentos, se acumulan y se unen. Se ven en capas (estratos), a veces con fósiles. Las metamórficas se forman cuando una roca cambia por mucha presión y temperatura, sin fundirse del todo. Muestran bandas o cristales alineados.",
        "Para clasificar una roca, usa sus rasgos como evidencia: cristales, capas, fósiles, bandas, vidrio. El color no basta, porque rocas de familias distintas pueden ser del mismo color. Si los rasgos no alcanzan, la respuesta prudente es decir que falta evidencia.",
    ],
    vocab=[("roca", "material sólido de la Tierra formado por uno o más minerales"), ("mineral", "sustancia sólida natural de composición definida"), ("magma", "roca fundida bajo la superficie"), ("lava", "roca fundida que sale a la superficie"), ("sedimento", "fragmento de roca o resto de ser vivo que se acumula"), ("estrato", "capa de una roca sedimentaria"), ("fósil", "resto o huella de un ser vivo antiguo conservado en una roca")],
    worked=[
        {"title": "Clasificar por capas y fósil", "problem": "Una roca está formada por capas horizontales de granos finos y en una capa se ve la huella de una concha. ¿A qué familia pertenece?", "steps": ["Las capas indican sedimentos acumulados.", "La huella de una concha es un fósil, que se conserva en rocas formadas a baja temperatura."], "answer": "Sedimentaria"},
        {"title": "Clasificar por bandas", "problem": "Una roca muy dura muestra bandas claras y oscuras de cristales alineados. No tiene fósiles ni granos sueltos. ¿Qué familia es más probable?", "steps": ["Los cristales alineados en bandas se forman bajo mucha presión.", "No hay granos sueltos ni fósiles, así que no es sedimentaria."], "answer": "Metamórfica"},
    ],
    mistakes=[
        {"wrong": "Clasificar una roca por su color.", "why": "Se usa un rasgo que no depende de cómo se formó.", "fix": "Mira cristales, capas, fósiles o bandas."},
        {"wrong": "Decir que el cuarzo es una roca.", "why": "Se confunde mineral con roca.", "fix": "El cuarzo es un mineral; las rocas se forman de uno o más minerales."},
    ],
    tiers={
        "recovery": [
            ex("Una roca se formó cuando lava se enfrió y se endureció. ¿A qué familia pertenece?", "Ígnea", "Las rocas ígneas se forman al enfriarse material fundido."),
            ex("Una roca se ve en capas y contiene la huella de un helecho. ¿A qué familia pertenece?", "Sedimentaria", "Las capas y los fósiles son rasgos de rocas sedimentarias."),
            ex("Una roca se formó cuando otra roca recibió mucha presión y temperatura sin fundirse del todo. ¿A qué familia pertenece?", "Metamórfica", "Metamórfica significa roca que cambió por presión y temperatura."),
        ],
        "understand": [
            ex("¿Qué es un mineral: (a) una sustancia sólida natural de composición definida, (b) una roca con fósiles o (c) lava endurecida?", "(a)", "Un mineral es una sustancia sólida natural de composición definida, como el cuarzo."),
            ex("¿Cuál de las dos sale a la superficie: el magma o la lava?", "La lava", "El magma está bajo la superficie y la lava es la roca fundida que sale."),
            ex("¿Por qué una roca ígnea no suele tener fósiles?", "Porque el material fundido está muy caliente y destruye los restos de seres vivos", "Los fósiles se conservan en sedimentos a baja temperatura, no en roca fundida."),
        ],
        "apply": [
            ex("Roca A: granos redondeados de arena unidos entre sí, en capas de 2 cm y de 3 cm. ¿A qué familia pertenece?", "Sedimentaria", "Los granos unidos y las capas son rasgos de rocas sedimentarias."),
            ex("Roca B: cristales grandes claros y oscuros entrelazados, sin capas ni fósiles. ¿A qué familia pertenece?", "Ígnea", "Los cristales entrelazados sin capas se forman al enfriarse magma."),
            arith("Una roca ígnea de 240 g tiene tres minerales. El cuarzo pesa 90 g y el segundo mineral pesa 110 g. ¿Cuántos gramos pesa el tercer mineral?", "240-90-110", "Se resta el peso de los dos minerales conocidos al peso total.", " g"),
        ],
        "reason": [
            ex("Ana dice que la roca X es sedimentaria porque tiene bandas. Pero las bandas de X son de cristales alineados, sin granos sueltos ni fósiles, y X es muy dura. ¿Qué familia es más probable y qué dato decide?", "Metamórfica; son bandas de cristales alineados y no capas de sedimentos", "Las capas sedimentarias tienen granos o fósiles; los cristales alineados indican presión."),
            ex("Un compañero afirma que el cuarzo es una roca ígnea. ¿Qué confusión de vocabulario cometió?", "Confundió mineral con roca", "El cuarzo es un mineral; una roca ígnea puede contener cuarzo."),
        ],
        "challenge": [
            ex("M: bandas de cristales alineados. N: cristales entrelazados sin capas. O: capas de granos con conchas. Escribe las letras en el orden ígnea, sedimentaria, metamórfica.", "N, O, M", "N se enfrió desde material fundido, O se acumuló en capas y M cambió por presión."),
            ex("Una muestra es dura, de un solo color gris, sin capas, sin fósiles y sin cristales visibles. ¿Alcanza con esos rasgos para clasificarla con seguridad?", "No, falta evidencia", "Rocas de familias distintas pueden verse así; hay que buscar más rasgos."),
        ],
    },
    context=[ex("En una playa de arena oscura de origen volcánico, una persona encuentra una piedra negra, brillante como vidrio, sin capas ni granos. ¿A qué familia es más probable que pertenezca?", "Ígnea", "El aspecto de vidrio sin capas se forma cuando la lava se enfría rápido.")],
    selfcheck=[
        ex("¿Qué rasgo tienen las rocas sedimentarias que casi nunca tienen las ígneas?", "Capas", "Las capas vienen de sedimentos que se acumulan uno sobre otro."),
        ex("¿Qué dos condiciones forman una roca metamórfica?", "Mucha presión y mucha temperatura", "Son los factores que cambian una roca sin fundirla del todo."),
        ex("¿La lava se forma bajo la superficie o sale a ella?", "Sale a la superficie", "Bajo la superficie se llama magma."),
    ],
    open_task=task(
        "Clasifica estas tres rocas de ejemplo. Roca 1: capas finas de color café con una huella de hoja. Roca 2: cristales pequeños entrelazados, con agujeritos de gas, sin capas. Roca 3: bandas claras y oscuras de cristales alineados, muy dura. Haz una tabla con la familia de cada una y el rasgo que te decide. Si tienes una piedra en casa, descríbela con la misma tabla y escribe si te falta evidencia para clasificarla.",
        "Roca 1: sedimentaria, porque tiene capas y un fósil. Roca 2: ígnea, porque tiene cristales entrelazados y agujeros de gas. Roca 3: metamórfica, porque las bandas son de cristales alineados.",
        ["tres rocas clasificadas", "un rasgo como evidencia en cada una", "diferencia entre rasgo observado y color"],
        ["tabla con familia y rasgo", "mención de la evidencia que falta en la piedra propia"],
        ["clasificar por color", "no escribir el rasgo que decide"],
        "Pregunta qué otro rasgo necesitarías para estar seguro en la piedra que no pudiste clasificar.",
    ),
    reinforce="Escribe una frase con la palabra «sedimento» y otra con la palabra «magma» que expliquen cada una.",
    extend="Con permiso de una persona de tu casa, mira una piedra del patio o de una plaza y anota tres rasgos que ves, sin golpearla.",
)

# ================================================================ OA 11, clase 2
register(
    OA11, 2,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a relacionar el enfriamiento, la sedimentación, la presión y la temperatura con la roca que se forma. Sirve para explicar por qué dos rocas del mismo origen se ven distintas.",
    prior=["Conozco las tres familias de rocas y sus rasgos.", "Sé que lava y magma son roca fundida."],
    explain=[
        "El enfriamiento explica las rocas ígneas. Si el magma se enfría lentamente bajo tierra, los cristales tienen tiempo de crecer y la roca, como el granito, tiene cristales grandes. Si la lava se enfría rápido en la superficie, los cristales son pequeños, como en el basalto, o no alcanzan a formarse y queda un vidrio, como en la obsidiana.",
        "La sedimentación explica las sedimentarias. Agua, viento o hielo transportan sedimentos y los depositan en capas; la capa de abajo es la más antigua. El peso de las capas de arriba aprieta los granos (compactación) y minerales disueltos los pegan (cementación). Así la arena forma arenisca y el barro fino forma lutita.",
        "La presión y la temperatura explican las metamórficas. Si una roca queda enterrada a mucha profundidad, cerca de magma o en el choque de placas, sus minerales se reordenan sin fundirse. La lutita pasa a pizarra, la caliza a mármol y la arenisca a cuarcita. Si la temperatura sube tanto que la roca se funde, ya no es metamorfismo: se forma magma.",
    ],
    vocab=[("cristal", "sólido con átomos ordenados que forma un mineral"), ("compactación", "apretamiento de sedimentos por el peso de las capas de arriba"), ("cementación", "unión de granos por minerales disueltos que se endurecen"), ("metamorfismo", "cambio de una roca por presión y temperatura, sin fundirse del todo"), ("lutita", "roca sedimentaria de barro o arcilla muy fina")],
    worked=[
        {"title": "Tamaño de cristales", "problem": "Dos rocas ígneas tienen cristales de 8 mm y de 1 mm. ¿Cuál se enfrió más lento?", "steps": ["Los cristales crecen más cuando hay más tiempo.", "Los de 8 mm son más grandes, así que hubo más tiempo."], "answer": "La de cristales de 8 mm"},
        {"title": "Un cambio por presión y temperatura", "problem": "Una caliza queda enterrada y se calienta cerca de magma, sin fundirse. ¿Qué roca se forma y por qué?", "steps": ["La caliza cambia por calor y presión.", "Como no se funde, es metamorfismo: la caliza forma mármol."], "answer": "Mármol, una roca metamórfica"},
    ],
    mistakes=[
        {"wrong": "Decir que el mármol se formó al fundirse la caliza y volver a enfriarse.", "why": "Se confunde metamorfismo con fusión.", "fix": "Si se funde y enfría, la roca nueva es ígnea; en el metamorfismo la roca no se funde del todo."},
        {"wrong": "Pensar que la capa de arriba de una secuencia es la más antigua.", "why": "Se ignora el orden de depósito.", "fix": "Los sedimentos se depositan uno sobre otro: la capa de abajo es la más antigua."},
    ],
    tiers={
        "recovery": [
            ex("Magma que se enfría lentamente dentro de la Tierra, ¿forma cristales grandes o pequeños?", "Grandes", "Con más tiempo, los cristales crecen más."),
            ex("El peso de capas gruesas de sedimento aprieta los granos de las capas de abajo. ¿Cómo se llama este proceso?", "Compactación", "La compactación reduce los espacios entre granos."),
            ex("Una lutita enterrada y calentada sin fundirse cambia a pizarra. ¿Qué dos factores actúan?", "Presión y temperatura", "Son los factores del metamorfismo."),
        ],
        "understand": [
            ex("Dos rocas ígneas tienen cristales de 10 mm y de 1 mm. ¿Cuál se enfrió más rápido?", "La de 1 mm", "Los cristales pequeños indican poco tiempo para crecer."),
            ex("¿Qué hace cada proceso: (a) la compactación aprieta los granos y la cementación los pega, (b) la compactación los pega y la cementación los aprieta o (c) ambos los funden?", "(a)", "Compactar es apretar y cementar es unir con minerales disueltos."),
            ex("La arenisca tiene como material de origen arena. ¿Qué proceso la convierte en cuarcita?", "El metamorfismo", "La presión y la temperatura reordenan sus minerales."),
        ],
        "apply": [
            arith("Un pozo muestra, de abajo hacia arriba, cuatro capas de 15 cm, 22 cm, 18 cm y 30 cm. ¿Cuántos centímetros mide el conjunto?", "15+22+18+30", "Se suman los grosores de las capas.", " cm"),
            arith("Supón que a la temperatura de la superficie, 15 °C, se suman 25 °C por cada kilómetro de profundidad (valores de ejemplo). ¿Qué temperatura hay a 4 km?", "15+4*25", "Se multiplica la profundidad por el aumento por kilómetro y se suma la temperatura inicial.", " °C"),
            ex("Una colada de lava se enfría en contacto con el aire, en pocos días. ¿Qué tamaño de cristales se espera?", "Pequeños o ninguno", "Enfriarse rápido no deja tiempo para que los cristales crezcan."),
        ],
        "reason": [
            ex("En un corte de terreno, la capa que contiene un fósil de concha está debajo de otra capa con otro fósil. ¿Cuál se depositó primero?", "La capa de abajo", "Los sedimentos se acumulan uno sobre otro, sin alteraciones."),
            ex("Granito: cristales de 6 mm. Obsidiana: sin cristales, parece vidrio. Ordena de enfriamiento más lento a más rápido.", "Granito, obsidiana", "Más tiempo permite cristales; la obsidiana se enfrió tan rápido que no se formaron."),
        ],
        "challenge": [
            arith("Con los mismos valores de ejemplo (15 °C en la superficie y 25 °C más por cada kilómetro), ¿a cuántos kilómetros de profundidad se alcanzan 165 °C?", "(165-15)//25", "Se resta la temperatura de la superficie y se divide por el aumento por kilómetro.", " km"),
            ex("Una geóloga dice que cierta roca nueva surgió porque otra se calentó a mil grados hasta fundirse completamente. ¿Qué familia tendrá la roca nueva al enfriarse?", "Ígnea", "Si la roca se funde por completo, al enfriarse forma una roca ígnea."),
        ],
    },
    context=[ex("Una cantera extrae mármol blanco, de cristales pequeños y apretados, sin capas. Los geólogos dicen que antes fue caliza. ¿Qué dos condiciones actuaron para el cambio?", "Mucha presión y mucha temperatura", "El mármol es una roca metamórfica de la caliza.")],
    selfcheck=[
        ex("¿Qué roca ígnea tiene cristales grandes: la de enfriamiento lento o la de enfriamiento rápido?", "La de enfriamiento lento", "Hay más tiempo para que los cristales crezcan."),
        ex("En una secuencia de capas sin alteraciones, ¿cuál es la más antigua?", "La de abajo", "Se depositó primero."),
        ex("¿Qué roca se forma si la caliza cambia por calor y presión sin fundirse?", "Mármol", "Es la roca metamórfica de la caliza."),
    ],
    open_task=task(
        "Una persona midió los cristales de tres rocas ígneas de ejemplo: roca P, 9 mm; roca Q, 2 mm; roca R, sin cristales y brillante. Ordénalas de enfriamiento más lento a más rápido y explica cada posición con una frase. Después escribe cómo cambiaría la historia de la roca P si hubiera quedado enterrada mucho tiempo bajo presión sin fundirse.",
        "Orden: P, Q, R. P tiene los cristales más grandes porque se enfrió lento. Si P se entierra con presión y calor sin fundirse, sus cristales se reordenan y pasa a ser metamórfica.",
        ["orden correcto P, Q, R", "una explicación por roca", "metamorfismo como cambio sin fusión"],
        ["orden escrito", "frases de explicación"],
        ["decir que el metamorfismo funde la roca", "ordenar al revés"],
        "Pregunta qué dato necesitarías para saber a cuántos kilómetros de profundidad se enfrió P.",
    ),
    reinforce="Escribe con tus palabras la diferencia entre compactación y cementación.",
    extend="Averigua con una persona de tu casa en qué lugar de tu región hay mármol, granito o arenisca usados en edificios, y anota una roca y su uso.",
)

# ================================================================ OA 11, clase 3
register(
    OA11, 3,
    materials="Papel y lápiz. Las rutas del ciclo están escritas en el cuaderno.",
    use="Aprenderé a construir un modelo del ciclo de las rocas con rutas posibles y sin un inicio obligatorio. Sirve para explicar cómo una roca puede transformarse en otra.",
    prior=["Sé qué factores forman cada familia de rocas.", "Sé que un modelo es una representación con límites."],
    explain=[
        "El ciclo de las rocas es un modelo de flechas que muestra cómo una roca puede transformarse en otra. Los procesos principales son: fusión (una roca se derrite y forma magma), enfriamiento (el magma o la lava se endurece y forma una roca ígnea), meteorización (la roca se rompe y altera en su lugar por agua, hielo, viento o seres vivos) y erosión (los fragmentos son arrastrados). Luego viene la sedimentación (se depositan), la compactación y cementación (forman una roca sedimentaria) y el metamorfismo (presión y temperatura forman una roca metamórfica).",
        "Este ciclo no tiene un inicio obligatorio ni un único camino. Una roca ígnea puede meteorizarse y formar sedimentos, o puede metamorfizarse sin romperse. Una sedimentaria puede fundirse y dar magma. Una metamórfica puede volver a metamorfizarse o ser meteorizada.",
        "Para construir el modelo, parte desde cualquier roca, elige un proceso y sigue la flecha. Cada flecha debe llevar el nombre del proceso, porque la flecha sin nombre no explica nada.",
    ],
    vocab=[("fusión", "paso de roca sólida a roca fundida"), ("meteorización", "rotura y alteración de una roca en su lugar"), ("erosión", "desgaste y arrastre de fragmentos por agua, viento o hielo"), ("sedimentación", "depósito de los sedimentos"), ("proceso", "cambio que ocurre en un tiempo determinado")],
    worked=[
        {"title": "De granito a arenisca", "problem": "Un granito de una montaña termina como arenisca en una cuenca. Nombra los procesos en orden.", "steps": ["Primero la roca se rompe: meteorización.", "Los fragmentos son arrastrados: erosión; luego se depositan: sedimentación; finalmente se aprietan y pegan: compactación y cementación."], "answer": "Meteorización, erosión, sedimentación, compactación y cementación"},
        {"title": "De metamórfica a ígnea", "problem": "Un mármol se hunde tanto que se funde y luego el magma sube y se enfría. ¿Qué familia se forma y por qué procesos?", "steps": ["Fundirse es fusión y forma magma.", "Cuando el magma se enfría, se forma una roca ígnea."], "answer": "Ígnea, por fusión y enfriamiento"},
    ],
    mistakes=[
        {"wrong": "Creer que el ciclo siempre parte del magma y va en un solo sentido.", "why": "Se lee el modelo como una línea y no como una red de rutas.", "fix": "Cualquier roca puede ser el punto de partida y hay varias rutas."},
        {"wrong": "Usar «erosión» para cualquier cambio.", "why": "Se confunde con meteorización o metamorfismo.", "fix": "La erosión arrastra fragmentos; la meteorización los rompe en su lugar."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué proceso transforma el magma en roca ígnea?", "El enfriamiento", "Al enfriarse, el magma se endurece."),
            ex("¿Qué proceso rompe una roca en fragmentos pequeños, sin moverlos?", "La meteorización", "Rompe y altera la roca en su lugar."),
            ex("¿Qué proceso arrastra los fragmentos de roca por agua, viento o hielo?", "La erosión", "Desgasta y transporta los fragmentos."),
        ],
        "understand": [
            ex("¿Debe el ciclo comenzar siempre en el magma? Responde sí o no.", "No", "Cualquier roca puede ser el punto de partida."),
            ex("¿Qué proceso convierte sedimentos sueltos en roca sedimentaria: (a) fusión, (b) compactación y cementación o (c) metamorfismo?", "(b)", "Apretar y pegar los granos forma la roca sedimentaria."),
            ex("Una roca ígnea es enterrada, se funde y vuelve a enfriarse. ¿Qué tipo de roca resulta?", "Ígnea", "Todo lo que se enfría desde material fundido forma roca ígnea."),
        ],
        "apply": [
            ex("Una arenisca queda enterrada y recibe calor y presión sin fundirse. ¿Qué roca se produce y cómo se llama el proceso?", "Cuarcita; metamorfismo", "El cambio por calor y presión sin fundirse es metamorfismo."),
            ex("Una montaña de granito se desgasta por lluvia y viento y sus granos se acumulan en un valle. Nombra los tres procesos en orden.", "Meteorización, erosión, sedimentación", "Primero se rompe, luego se arrastra y al final se deposita."),
            ex("Una roca metamórfica se hunde, se funde y el magma se enfría. ¿Qué familia se forma?", "Ígnea", "El enfriamiento de magma forma roca ígnea."),
        ],
        "reason": [
            ex("Camila afirma que el ciclo es una línea: ígnea, sedimentaria, metamórfica, magma, siempre en ese orden. Una roca ígnea es enterrada y recibe presión y temperatura sin fundirse. ¿A qué familia pasa sin ser sedimentaria antes, y qué dice eso del modelo de Camila?", "Pasa a metamórfica; el modelo de Camila no incluye esa ruta", "El ciclo tiene varias rutas, no solo una."),
            ex("Una roca de superficie va a convertirse en sedimentaria. ¿Qué proceso actúa primero sobre ella?", "La meteorización", "Primero debe romperse para formar fragmentos."),
        ],
        "challenge": [
            ex("Un modelo A solo conecta cada familia con la siguiente en círculo (ígnea, sedimentaria, metamórfica). Una pizarra metamórfica se erosiona y forma arenisca. ¿Qué ruta no está en el modelo A?", "De metamórfica a sedimentaria", "El modelo A solo sigue un sentido y no incluye esa ruta."),
            ex("Una sedimentaria quiere convertirse en ígnea. ¿Por qué estado debe pasar la roca antes?", "Por magma, mediante la fusión", "Para formar una ígnea debe derretirse y luego enfriarse."),
        ],
    },
    context=[ex("En la desembocadura de un río se acumulan arena y piedrecillas arrastradas desde la montaña. ¿Qué dos procesos del ciclo se ven en acción?", "Erosión (transporte) y sedimentación", "Los fragmentos se arrastran y luego se depositan.")],
    selfcheck=[
        ex("¿Qué proceso forma magma a partir de una roca?", "Fusión", "Es el paso de roca sólida a roca fundida."),
        ex("¿Tiene el ciclo de las rocas un único camino?", "No", "Existen varias rutas entre las familias."),
        ex("¿Qué se escribe sobre cada flecha de un buen modelo del ciclo?", "El nombre del proceso", "Sin nombre la flecha no explica el cambio."),
    ],
    open_task=task(
        "Dibuja un ciclo de las rocas con cinco cajas: magma, roca ígnea, sedimentos, roca sedimentaria y roca metamórfica. Une las cajas con al menos seis flechas y escribe el nombre del proceso sobre cada una. Marca con una estrella una ruta corta que no pase por todas las cajas y escribe qué proceso nombra la flecha de esa ruta.",
        "Ejemplo de ruta corta: roca ígnea a roca metamórfica, proceso: metamorfismo. Otra: roca sedimentaria a magma, proceso: fusión.",
        ["cinco cajas", "al menos seis flechas con proceso", "una ruta corta marcada"],
        ["diagrama de cajas y flechas", "ruta marcada"],
        ["flechas sin nombre", "dibujar una línea sin rutas alternativas"],
        "Pregunta por qué tu modelo no tiene un inicio obligatorio.",
    ),
    reinforce="Escribe dos rutas distintas para que una roca ígnea termine como roca metamórfica.",
    extend="Averigua con una persona de tu casa si ha visto en algún lugar rocas partidas por el hielo o las raíces, y relaciónalo con la meteorización.",
)

# ================================================================ OA 11, clase 4
register(
    OA11, 4,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé a explicar las transformaciones de las rocas considerando cuánto tardan. Sirve para entender por qué no podemos ver el ciclo completo en una vida.",
    prior=["Conozco los procesos del ciclo de las rocas.", "Sé calcular con milímetros, centímetros y metros."],
    explain=[
        "Los procesos del ciclo ocurren a ritmos muy distintos. Una colada de lava de superficie se endurece en días o meses. Una capa de sedimento puede crecer solo unos milímetros por año. Convertir ese sedimento en roca y luego en metamórfica puede tardar millones de años. Por eso el ciclo completo no se observa en una vida humana.",
        "Para estudiar procesos tan lentos se usan evidencias y cálculos. Si se conoce cuánto sedimento se acumula por año, se puede estimar cuánto tardó una capa. Recuerda que 1 m equivale a 1.000 mm. Si una capa crece 2 mm por año, en 1.000 años crece 2.000 mm, es decir, 2 m. Los datos de esta clase son de ejemplo y las velocidades reales cambian según el lugar.",
        "Estos cálculos suponen una velocidad constante, y eso casi nunca ocurre: una crecida del río puede depositar más sedimento en un día que en años tranquilos. Por eso, una estimación se dice «aproximadamente» y se acompaña de su límite.",
    ],
    vocab=[("tasa", "cantidad que cambia en cada unidad de tiempo, como mm por año"), ("estimación", "valor aproximado calculado con datos"), ("escala de tiempo", "duración típica de un proceso"), ("constante", "que no cambia"), ("millón", "mil veces mil, 1.000.000")],
    worked=[
        {"title": "Cuánto crece una capa", "problem": "Un lago recibe 3 mm de sedimento por año (dato de ejemplo). ¿Cuánto crece la capa en 500 años?", "steps": ["Se multiplica la tasa por los años: 3 × 500 = 1.500.", "La unidad es milímetros."], "answer": "1.500 mm"},
        {"title": "Cuánto tardó una capa", "problem": "Una capa de 10 m se formó con una tasa de 5 mm por año. ¿Cuántos años tardó?", "steps": ["10 m son 10.000 mm.", "Se divide 10.000 por 5: 2.000."], "answer": "2.000 años"},
    ],
    mistakes=[
        {"wrong": "Dividir 10 por 5 sin pasar los metros a milímetros.", "why": "Se mezclan unidades distintas.", "fix": "Convierte primero: 10 m = 10.000 mm."},
        {"wrong": "Afirmar que una capa tardó exactamente 2.000 años.", "why": "Se olvida que la tasa no es constante.", "fix": "Di «aproximadamente» y nombra la suposición."},
    ],
    tiers={
        "recovery": [
            ex("Un proceso tarda 10 años y otro tarda 10 millones de años. ¿Cuál podría observarse completo en la vida de una persona?", "El de 10 años", "Una vida humana dura unas pocas décadas, no millones de años."),
            ex("El magma que se enfría profundo tarda miles de años o más; la lava en la superficie tarda días o meses. ¿Cuál forma cristales más grandes?", "El magma profundo", "Enfriarse más lento permite que los cristales crezcan."),
            ex("¿Cuántos milímetros son 3 metros?", "3.000 mm", "1 m equivale a 1.000 mm."),
        ],
        "understand": [
            ex("¿Por qué no se puede observar el ciclo completo de una roca en una vida humana?", "Porque muchos procesos tardan miles o millones de años", "El tiempo humano es mucho menor que el tiempo del ciclo."),
            ex("Los geólogos no pueden esperar millones de años. ¿Cómo reconstruyen procesos lentos: (a) cronometrando un proceso completo o (b) leyendo evidencias que quedaron en las rocas, como capas y fósiles?", "(b)", "Las capas y los fósiles son un registro que queda en la roca."),
            ex("¿Qué dice la palabra «aproximadamente» en una estimación de edad: que el valor es exacto o que el valor depende de suposiciones?", "Que depende de suposiciones", "La tasa real puede cambiar en el tiempo."),
        ],
        "apply": [
            arith("Una laguna recibe 4 mm de sedimento por año (dato de ejemplo). ¿Cuántos milímetros se acumulan en 250 años?", "4*250", "Se multiplica la tasa por los años.", " mm"),
            arith("Una capa de 9 m se formó con una tasa de 3 mm por año (dato de ejemplo). ¿Cuántos años tardó, aproximadamente?", "9*1000//3", "Se pasan los metros a milímetros y se divide por la tasa.", " años"),
            arith("Un acantilado tiene 20 capas. Si cada capa tardó 500 años (dato de ejemplo), ¿cuántos años representan las 20 capas?", "20*500", "Se multiplica el número de capas por los años de cada una.", " años"),
        ],
        "reason": [
            ex("Marco dice: «Como yo nunca vi formarse una roca sedimentaria, el ciclo es falso». ¿Qué error comete?", "Confunde no haberlo visto con no tener evidencia; el proceso es muy lento", "El registro en las rocas muestra procesos que no caben en una vida."),
            ex("La capa X y la capa Y miden 3 m cada una. X creció a 1 mm por año e Y a 2 mm por año. ¿Cuál tardó más y cuántas veces más?", "X; el doble", "Con la mitad de la tasa, tarda el doble de años."),
        ],
        "challenge": [
            arith("Una capa de 12 m creció a 2 mm por año, con tasa constante (dato de ejemplo). ¿Cuántos años tardó?", "12*1000//2", "Se pasan 12 m a milímetros y se divide por la tasa.", " años"),
            arith("Un valle recibe sedimento a 4 mm por año durante 1.500 años y luego a 2 mm por año durante 1.000 años (datos de ejemplo). ¿Cuántos milímetros se acumularon en total?", "4*1500+2*1000", "Se calcula cada período y se suman.", " mm"),
        ],
    },
    context=[ex("Un geólogo observa en un corte de terreno una capa de arcilla de 6 m. Sabe que en ese lugar se acumulan unos 2 mm por año (dato de ejemplo). ¿Qué cálculo le permite estimar el tiempo?", "6 m = 6.000 mm y 6.000 ÷ 2 = 3.000 años, aproximadamente", "Se divide el grosor total por la tasa de acumulación.")],
    selfcheck=[
        ex("¿Cuántos milímetros tiene 1 metro?", "1.000 mm", "Es la equivalencia entre metro y milímetro."),
        ex("Si una capa crece 5 mm por año, ¿cuántos mm crece en 100 años?", "500 mm", "5 × 100 = 500."),
        ex("¿Qué proceso del ciclo es más lento: el enfriamiento de una colada de lava o la formación de una roca metamórfica?", "La formación de una roca metamórfica", "Puede tardar millones de años."),
    ],
    open_task=task(
        "Usa este dato de ejemplo: un lago acumula 2 mm de sedimento por año. Calcula cuánto sedimento se acumula en 100 años, en 1.000 años y en 10.000 años. Anota cada resultado en milímetros y en metros. Después escribe una frase con «aproximadamente» y una limitación del cálculo.",
        "En 100 años: 200 mm, es decir, 0,2 m. En 1.000 años: 2.000 mm, es decir, 2 m. En 10.000 años: 20.000 mm, es decir, 20 m. Aproximadamente, porque la tasa real no es constante. Limitación: la tasa real cambia con las crecidas.",
        ["tres cálculos correctos", "milímetros y metros", "una limitación de la tasa constante"],
        ["tabla de años y milímetros", "frase con limitación"],
        ["olvidar la conversión a metros", "no escribir la suposición de tasa constante"],
        "Pregunta cuánto tardaría en formarse una capa de 5 m con esa tasa.",
    ),
    reinforce="Convierte a milímetros 4 m, 7 m y 12 m.",
    extend="Averigua con una persona de tu casa cuánto crece en un año algo lento que conozca, como una uña o una planta, y compáralo con 2 mm por año.",
)

# ================================================================ OA 11, clase 5
register(
    OA11, 5,
    materials="Papel y lápiz. Los modelos y las evidencias están escritos en el cuaderno.",
    use="Aprenderé a revisar qué explica y qué no explica el modelo del ciclo de las rocas. Sirve para saber cuándo conviene mejorar un modelo.",
    prior=["Sé construir el ciclo de las rocas con rutas.", "Sé que los procesos tienen escalas de tiempo muy distintas."],
    explain=[
        "Un modelo es útil si explica las observaciones y permite predecir, y hay que revisar sus límites. El ciclo de las rocas explica cómo una roca puede transformarse en otra y por qué hay tres familias. Predice, por ejemplo, que una roca metamórfica con un fósil deformado fue antes una roca sedimentaria, o que el gneis, una roca metamórfica con bandas, puede venir del granito.",
        "Pero el modelo tiene alcances limitados. No muestra cuánto tarda cada proceso, ni a qué profundidad ocurre, ni qué minerales hay. Las flechas pueden hacer pensar que toda roca recorre el círculo completo, cuando muchas pasan millones de años sin cambiar. Tampoco muestra el papel del movimiento de las placas, que lleva rocas a mayor profundidad.",
        "Para mejorar un modelo se agregan datos que faltan, como tiempos o profundidades, y se anota qué sigue sin explicar. Un modelo se compara con otro con un criterio claro, por ejemplo cuántas observaciones explica cada uno. Esa revisión es parte del trabajo científico.",
    ],
    vocab=[("alcance", "lo que un modelo logra explicar"), ("limitación", "algo que el modelo no muestra o muestra mal"), ("predicción", "resultado que se espera según el modelo"), ("criterio", "regla para comparar y decidir"), ("evidencia", "dato que apoya una explicación")],
    worked=[
        {"title": "Predecir con el modelo", "problem": "Se encuentra una pizarra con un fósil de concha aplastado. ¿Qué familia tuvo antes y por qué?", "steps": ["Los fósiles se conservan en rocas sedimentarias.", "La pizarra viene de la lutita, que es sedimentaria."], "answer": "Sedimentaria"},
        {"title": "Contar observaciones explicadas", "problem": "Hay 5 observaciones. El modelo A explica 2 y el modelo B explica 5. ¿Cuántas más explica B?", "steps": ["B explica 5 observaciones.", "A explica 2: 5 − 2 = 3."], "answer": "3 observaciones más"},
    ],
    mistakes=[
        {"wrong": "Pensar que el modelo es perfecto porque explica varias observaciones.", "why": "Se olvidan los límites.", "fix": "Anota siempre qué no muestra el modelo."},
        {"wrong": "Concluir que toda roca recorre el círculo completo.", "why": "Se interpretan las flechas como un orden obligatorio.", "fix": "Las rutas son posibles, no obligatorias."},
    ],
    tiers={
        "recovery": [
            ex("¿Un modelo del ciclo de las rocas muestra cuánto tarda cada proceso? Responde sí o no.", "No", "Los tiempos son una limitación del modelo básico."),
            ex("¿Qué familia de rocas suele contener fósiles?", "Sedimentaria", "Se forma por acumulación de sedimentos a baja temperatura."),
            ex("Un modelo explica 3 de 3 observaciones y otro explica 1 de 3. Con el criterio «explica más observaciones», ¿cuál es mejor?", "El primero", "Explica más observaciones."),
        ],
        "understand": [
            ex("¿Cuál es una limitación del modelo: (a) explica cómo el granito se puede transformar en arenisca o (b) no muestra cuánto tarda el proceso?", "(b)", "Los tiempos no aparecen en el diagrama de flechas."),
            ex("Las flechas del ciclo, ¿indican un orden obligatorio o rutas posibles?", "Rutas posibles", "Cada roca puede seguir caminos distintos."),
            ex("¿Para qué sirve comparar dos modelos con un criterio?", "Para decidir con el mismo patrón cuál explica mejor", "Sin criterio, la elección sería una opinión."),
        ],
        "apply": [
            ex("Se halla un gneis, una roca metamórfica con bandas, que tiene los mismos minerales de un granito y ningún rastro de capas ni de fósiles. ¿Qué familia pudo tener antes?", "Ígnea", "El gneis puede formarse a partir de granito por presión y temperatura."),
            arith("En un cuadro con 8 observaciones, el modelo P explica 6. ¿Cuántas observaciones no explica?", "8-6", "Se resta lo explicado al total.", " observaciones"),
            arith("En 4 casos distintos, el modelo explicó 3, 5, 4 y 2 observaciones. ¿Cuántas explicó en total?", "3+5+4+2", "Se suman los resultados de los cuatro casos.", " observaciones"),
        ],
        "reason": [
            ex("Un estudiante dice que su modelo es mejor porque tiene más colores. ¿Qué criterio olvidó?", "Cuántas observaciones explica", "El color no ayuda a explicar los procesos."),
            ex("Observación: en un cerro de granito hay arena en la base, pero no hay arenisca. ¿Qué proceso falta, según el modelo, para que la arena se vuelva roca?", "Compactación y cementación", "Los sedimentos sueltos aún no se han apretado ni pegado."),
        ],
        "challenge": [
            ex("El modelo A dibuja un círculo con una sola ruta; el modelo B dibuja una red con rutas alternativas y nombres de procesos. Observación: una ígnea pasa directo a metamórfica. ¿Qué modelo la explica y por qué?", "El modelo B, porque tiene la ruta alternativa", "El modelo A solo incluye una ruta y no puede mostrarla."),
            ex("Una compañera propone agregar al modelo una columna de tiempos (días, miles de años, millones de años). ¿Qué limitación del modelo corregiría?", "La falta de escalas de tiempo", "La columna muestra cuánto tarda cada proceso."),
        ],
    },
    context=[ex("Una persona dice: «Las rocas del cerro de mi pueblo son de piedra, así que no cambian nunca». Con el modelo del ciclo y sus escalas de tiempo, ¿qué respuesta corresponde?", "Cambian, pero tan despacio que no lo notamos en una vida", "Los procesos del ciclo tardan miles o millones de años.")],
    selfcheck=[
        ex("¿Qué sirve para mejorar un modelo: agregar los datos que le faltan o esconder sus límites?", "Agregar los datos que le faltan", "Mejorar un modelo implica agregar información."),
        ex("¿Una roca metamórfica con un fósil deformado fue antes de qué familia?", "Sedimentaria", "El fósil se conservó en un sedimento."),
        ex("¿Qué debe acompañar a un modelo según la ciencia?", "Sus limitaciones", "Ningún modelo es una copia exacta."),
    ],
    open_task=task(
        "Compara estos dos modelos con cuatro observaciones: (1) un granito se rompe y sus granos forman una arenisca, (2) una arenisca se transforma en cuarcita, (3) una pizarra se erosiona y forma una arenisca, (4) una arenisca se funde y al enfriarse forma una roca ígnea. Modelo A: círculo ígnea, sedimentaria, metamórfica, otra vez ígnea, con flechas sin nombre. Modelo B: red con rutas en todas las direcciones y el nombre de cada proceso. Un modelo explica una observación si tiene la ruta que ella necesita. Haz un cuadro con sí o no para cada observación en cada modelo, escribe cuál modelo explica más y una limitación que siga existiendo en ambos.",
        "A: 1 sí, 2 sí, 3 no, 4 no. B: 1 sí, 2 sí, 3 sí, 4 sí. B explica más porque tiene más rutas. Limitación: ninguno muestra cuánto tarda cada proceso.",
        ["cuadro con las cuatro observaciones", "conclusión con criterio", "una limitación común"],
        ["cuadro completo", "frase de conclusión"],
        ["elegir sin contar", "no escribir ninguna limitación"],
        "Pregunta qué dato nuevo cambiaría tu conclusión.",
    ),
    reinforce="Escribe una limitación del ciclo de las rocas y cómo podrías mejorarla.",
    extend="Averigua con una persona de tu casa qué otro modelo usa para explicar algo que no se ve, como un mapa o una maqueta, y qué límites tiene.",
)
